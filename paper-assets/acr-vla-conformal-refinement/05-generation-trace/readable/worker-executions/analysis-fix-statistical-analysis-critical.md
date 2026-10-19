# analysis fix statistical analysis critical

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 121
- **Recorded user turns:** 0
- **Tool calls:** 46
- **Original source:** `logs/workers/worker_analysis_fix-statistical-analysis-critical_20260520T045526.log`
- **Structured JSON:** [`77b999cda56e20950cc9.json`](../../sessions/77/77b999cda56e20950cc9.json)

## Before a recorded user message

121 recorded events

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
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only",
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
  "uuid": "be87bf79-7f60-4c94-bc41-809ae65d18a3",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779259200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "e6852aeb-df1a-4b4d-b856-cf7038c4ede9",
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this down:

1. Read the current statistical_analysis.py
2. Read the registry to get latest experiment data
3. SSH to servers to verify suspicious data points
4. Fix the script (change norm01 → norm02 as main config)
5. Run the script and save output
6. Report the summary table

Let me start by reading the current script and the registry in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "bfa6c966-0808-4825-b2e8-a9f6fe346736",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ScRVinL1FmBduoLWcDzy1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12120,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12120
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

_source line 5_

Let me start by reading the current script and the registry data in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "c598f800-1dd9-401f-a644-d7e44b572337",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ScRVinL1FmBduoLWcDzy1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12120,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12120
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01V5MbYTRVeHiNvpVd722MZv`</summary>

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
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "3f3492b9-f828-46be-a0ef-317b6c16a614",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ScRVinL1FmBduoLWcDzy1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12120,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12120
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

_source line 7 · 2026-05-20T04:55:44.486Z_

<details><summary>↩ Tool result · `toolu_01V5MbYTRVeHiNvpVd722MZv`</summary>

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
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "9d9b32f7-424b-46fb-8d7f-937865ded46e",
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

_source line 8_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RqsamYq9454N1i4bvT8ATr`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "5b135fb3-4699-4a19-a72f-d61f1075e5f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ScRVinL1FmBduoLWcDzy1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12120,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12120
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

_source line 9 · 2026-05-20T04:55:45.644Z_

<details><summary>↩ Tool result · `toolu_01RqsamYq9454N1i4bvT8ATr`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
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
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "a5c211ad-bde3-4e42-8ce9-0a287b16a2e6",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Assistant

_source line 10_

Now let me read the registry for all successful experiments and verify the suspicious data points on the servers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "43dc76ed-7300-4cc7-bacc-ba9d0baffd21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8HB7q4FkZBbk8G166JcpV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7738,
      "cache_read_input_tokens": 23961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7738
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

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01Um1uM58s27Xe8LZhC7rf5S`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "filters": {
    "conclusion": "success"
  },
  "limit": 0,
  "fields": [
    "experiment_id",
    "benchmark",
    "method",
    "seed",
    "metrics",
    "config",
    "updated_at",
    "notes"
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
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "27f3ab9c-7241-41b9-a3ce-bf7fe1e5c061",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8HB7q4FkZBbk8G166JcpV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7738,
      "cache_read_input_tokens": 23961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7738
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

_source line 12 · 2026-05-20T04:55:54.609Z_

<details><summary>↩ Tool result · `toolu_01Um1uM58s27Xe8LZhC7rf5S`</summary>

```text
Error: result (80,607 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "8ca0475a-edbe-4921-bad7-2161d0695d6b",
  "tool_use_result": {
    "content": "Error: result (80,607 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval-vla-only-spatial-seed50\": {\"updated_at\": \"2026-05-20T04:13:56.340Z\", \"metrics\": {\"success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}}, \"eval-crm-spatial-seed48\": {\"updated_at\": \"2026-05-20T04:13:53.186Z\", \"metrics\": {\"success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total\": 100}}, \"eval-argmin-object-k5-seed44-r2\": {\"updated_at\": \"2026-05-20T04:10:36.445Z\", \"metrics\": {\"sr\": 0.11, \"sr_pct\": \"11%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.2, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.3, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-obs-only-spatial-norm02-seed46-r2\": {\"updated_at\": \"2026-05-20T04:10:34.598Z\", \"metrics\": {\"sr\": 0.33, \"sr_pct\": \"33.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 1, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0.1, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.8, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}}, \"eval-vla-only-goal-seed44-r2\": {\"updated_at\": \"2026-05-20T04:10:32.773Z\", \"metrics\": {\"overall_success_rate\": 0.73, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.6, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.8}}}, \"eval-adaptive-k-p25-seed43\": {\"updated_at\": \"2026-05-20T03:15:36.605Z\", \"metrics\": {\"success_rate\": 0.13, \"avg_actual_k\": 4.788, \"fast_path_ratio\": 0.6515, \"total_steps\": 28207, \"fast_steps\": 18377, \"full_steps\": 9830}}, \"eval-adaptive-k-p50-seed43\": {\"updated_at\": \"2026-05-20T03:15:32.975Z\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.81, \"fast_path_ratio\": 0.7737, \"total_steps\": 27813, \"fast_steps\": 21520, \"full_steps\": 6293}}, \"eval-obs-only-spatial-norm02-seed48\": {\"updated_at\": \"2026-05-20T03:14:41.521Z\", \"metrics\": {\"success_rate\": 0.35, \"per_task\": {\"between_plate_and_ramekin\": 0.8, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.4, \"on_wooden_cabinet\": 0}}}, \"eval-adaptive-k-p25-seed42\": {\"updated_at\": \"2026-05-20T03:05:13.741Z\", \"metrics\": {\"success_rate\": 0.15, \"avg_actual_k\": 4.8, \"fast_path_ratio\": 0.65}}, \"eval-adaptive-k-p50-seed42\": {\"updated_at\": \"2026-05-20T02:55:44.980Z\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.72, \"fast_path_ratio\": 0.785}}, \"eval-adaptive-k-p75-seed43\": {\"updated_at\": \"2026-05-20T02:55:37.755Z\", \"metrics\": {\"success_rate\": 0.13, \"avg_actual_k\": 3.15, \"fast_path_ratio\": 0.856}}, \"eval-crm-goal-seed46\": {\"updated_at\": \"2026-05-20T02:54:29.366Z\", \"metrics\": {\"overall_success_rate\": 0.72, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 1, \"put_the_cream_cheese_in_the_bowl\": 0.4, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.3}}}, \"eval-adaptive-k-p90-seed44\": {\"updated_at\": \"2026-05-20T02:52:29.115Z\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 2.58, \"fast_path_ratio\": 0.928}}, \"eval-adaptive-k-p75-seed42\": {\"updated_at\": \"2026-05-20T02:52:22.430Z\", \"metrics\": {\"success_rate\": 0.12, \"avg_actual_k\": 3.07, \"fast_path_ratio\": 0.866}}, \"eval-adaptive-k-p50-seed44\": {\"updated_at\": \"2026-05-20T02:40:24.520Z\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 3.909, \"fast_path_ratio\": 0.761, \"total_steps\": 28067, \"fast_steps\": 21368, \"full_steps\": 6699}}, \"eval-adaptive-k-p75-seed44\": {\"updated_at\": \"2026-05-20T02:40:21.205Z\", \"metrics\": {\"success_rate\": 0.16, \"avg_actual_k\": 3.022, \"fast_path_ratio\": 0.872, \"total_steps\": 27724, \"fast_steps\": 24181, \"full_steps\": 3543}}, \"eval-adaptive-k-p90-seed43\": {\"updated_at\": \"2026-05-20T02:40:15.747Z\", \"metrics\": {\"success_rate\": 0.14, \"avg_actual_k\": 2.612, \"fast_path_ratio\": 0.923, \"total_steps\": 27935, \"fast_steps\": 25797, \"full_steps\": 2138}}, \"eval-adaptive-k-p90-seed42\": {\"updated_at\": \"2026-05-20T02:40:12.273Z\", \"metrics\": {\"success_rate\": 0.12, \"avg_actual_k\": 2.672, \"fast_path_ratio\": 0.916, \"total_steps\": 28258, \"fast_steps\": 25886, \"full_steps\": 2372}}, \"eval-vla-only-spatial-seed47\": {\"updated_at\": \"2026-05-20T01:39:25.709Z\", \"metrics\": {\"overall_success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"successful_rollouts\": 30}}, \"eval-crm-long-seed47\": {\"updated_at\": \"2026-05-20T00:21:06.698Z\", \"metrics\": {\"success_rate\": 0.17, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.5, \"LIVING_ROOM_SCENE5_mugs_on_plates\": 0.2, \"STUDY_SCENE1_book_in_caddy\": 0.2, \"LIVING_ROOM_SCENE2_soup_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cheese_butter_basket\": 0, \"KITCHEN_SCENE4_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE6_mug_pudding\": 0, \"LIVING_ROOM_SCENE1_soup_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-vla-only-object-seed48\": {\"updated_at\": \"2026-05-20T00:19:44.143Z\", \"metrics\": {\"success_rate\": 0.1, \"n_episodes\": 100}}, \"eval-vla-only-long-seed48\": {\"updated_at\": \"2026-05-20T00:16:50.121Z\", \"metrics\": {\"success_rate\": 0.14, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.8, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_right\": 0.3, \"STUDY_SCENE1_book_in_back_compartment\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_pudding\": 0.1, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-vla-only-object-seed50\": {\"updated_at\": \"2026-05-20T00:16:32.874Z\", \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100, \"successes\": 9, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}}, \"eval-crm-long-seed46\": {\"updated_at\": \"2026-05-20T00:13:08.430Z\", \"metrics\": {\"success_rate\": 0.18, \"n_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_turn_on_stove_put_moka_pot\": 0.9, \"KITCHEN_SCENE6_mug_in_microwave_close\": 0.5, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_right\": 0.2, \"STUDY_SCENE1_book_in_back_compartment\": 0.2, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_in_drawer\": 0, \"LIVING_ROOM_SCENE6_white_mug_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-goal-seed45-r2\": {\"updated_at\": \"2026-05-20T00:11:46.069Z\", \"metrics\": {\"success_rate\": 0.65, \"n_episodes\": 100, \"per_task\": {\"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_bowl_on_top_of_the_cabinet\": 0.8, \"open_the_middle_drawer_of_the_cabinet\": 0.7, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"put_the_wine_bottle_on_the_rack\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2, \"put_the_cream_cheese_in_the_bowl\": 0.2}}}, \"eval-crm-goal-seed44-r2\": {\"updated_at\": \"2026-05-20T00:11:07.345Z\", \"metrics\": {\"success_rate\": 0.64, \"n_episodes\": 100, \"per_task\": {\"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_bowl_on_the_stove\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"open_the_middle_drawer_of_the_cabinet\": 0.6, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"put_the_wine_bottle_on_the_rack\": 0.4, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2}}}, \"eval-obs-only-spatial-norm02-seed43-r2\": {\"updated_at\": \"2026-05-19T23:20:20.286Z\", \"metrics\": {\"overall_success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"on_stove\": 0, \"next_to_plate\": 0.2, \"on_wooden_cabinet\": 0}}}, \"k2-l2-calibration-phase1\": {\"updated_at\": \"2026-05-19T22:38:04.117Z\", \"metrics\": {\"k2l2_vs_k10var_rho\": 0.9979, \"k2l2_vs_k10var_pvalue\": 0, \"k2l2_vs_fmvd_rho\": 0.0925, \"k2l2_vs_fmvd_pvalue\": 6.03e-29, \"k10var_vs_fmvd_rho\": 0.0825, \"k10var_vs_fmvd_pvalue\": 2.33e-23, \"n_samples\": 14512, \"k2l2_mean\": 0.0807, \"k2l2_std\": 0.0361, \"go_nogo_k2_proxy\": \"GO (rho=0.9979)\", \"go_nogo_fmvd_signal\": \"NO-GO (rho=0.09)\"}}, \"eval-crm-long-seed45\": {\"updated_at\": \"2026-05-19T22:15:17.800Z\", \"metrics\": {\"overall_success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 18}}, \"eval-vla-only-goal-seed43\": {\"updated_at\": \"2026-05-19T21:32:22.969Z\", \"metrics\": {\"overall_success_rate\": 0.69, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.5, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.4, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.6}}}, \"eval-vla-only-goal-seed42\": {\"updated_at\": \"2026-05-19T21:32:21.219Z\", \"metrics\": {\"overall_success_rate\": 0.71, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.6, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.7, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.2, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}}, \"eval-vla-only-object-seed47\": {\"updated_at\": \"2026-05-19T21:32:10.689Z\", \"metrics\": {\"overall_success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2, \"alphabet_soup\": 0, \"cream_cheese\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0}}}, \"eval-crm-long-seed44\": {\"updated_at\": \"2026-05-19T21:32:07.617Z\", \"metrics\": {\"overall_success_rate\": 0.2, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.6, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.3, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-long-seed43\": {\"updated_at\": \"2026-05-19T21:32:03.390Z\", \"metrics\": {\"overall_success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.3, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-long-seed42\": {\"updated_at\": \"2026-05-19T21:31:58.213Z\", \"metrics\": {\"overall_success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE6_mug_microwave\": 0.4, \"LIVING_ROOM_SCENE5_mugs_plates\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.2, \"LIVING_ROOM_SCENE6_mug_plate_pudding\": 0.1, \"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter\": 0, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese\": 0, \"KITCHEN_SCENE8_both_moka_pots\": 0}}}, \"eval-crm-goal-seed42\": {\"updated_at\": \"2026-05-19T21:22:37.560Z\", \"metrics\": {\"overall_success_rate\": 0.67, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.4, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.2, \"put_the_bowl_on_top_of_the_cabinet\": 1, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.2, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.4}}}, \"eval-crm-goal-seed43\": {\"updated_at\": \"2026-05-19T21:19:08.468Z\", \"metrics\": {\"overall_success_rate\": 0.72, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.8, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.6, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.5, \"put_the_bowl_on_top_of_the_cabinet\": 0.9, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.3, \"turn_on_the_stove\": 1, \"put_the_bowl_on_the_plate\": 1, \"put_the_wine_bottle_on_the_rack\": 0.4}}}, \"eval-vla-only-spatial-seed46\": {\"updated_at\": \"2026-05-19T21:15:20.345Z\", \"metrics\": {\"overall_success_rate\": 0.3, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"successful_rollouts\": 30}}, \"eval-vla-only-long-seed47\": {\"updated_at\": \"2026-05-19T21:14:38.930Z\", \"metrics\": {\"overall_success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 100, \"successful_rollouts\": 14, \"per_task\": {\"put_both_alphabet_soup_and_tomato_sauce_in_basket\": 0, \"put_both_cream_cheese_box_and_butter_in_basket\": 0, \"turn_on_stove_put_moka_pot\": 0.8, \"put_black_bowl_in_bottom_drawer\": 0, \"put_white_mug_left_plate_yellow_mug_right_plate\": 0.4, \"pick_up_book_place_in_caddy\": 0.1, \"put_white_mug_on_plate_chocolate_pudding_right\": 0.1, \"put_both_alphabet_soup_and_cream_cheese_in_basket\": 0, \"put_both_moka_pots_on_stove\": 0, \"put_yellow_white_mug_in_microwave\": 0}}, \"notes\": \"Cron false positive: eval 脚本无 W&B/sentinel，进程正常退出被误判 failed。实际已完成全部 10 tasks。SR=14.0%，与已有 seeds 一致 (mean~14.2%)。手动修正 conclusion=success。\"}, \"eval-vla-only-goal-seed45\": {\"updated_at\": \"2026-05-19T20:10:50.847Z\", \"metrics\": {\"overall_success_rate\": 0.63, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.3, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.3, \"push_the_plate_to_the_front_of_the_stove\": 0.9, \"put_the_cream_cheese_in_the_bowl\": 0.1, \"turn_on_the_stove\": 0.8, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.8}}}, \"eval-vla-only-goal-seed46\": {\"updated_at\": \"2026-05-19T20:08:19.990Z\", \"metrics\": {\"overall_success_rate\": 0.71, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"total_successes\": 71, \"per_task\": {\"open_the_middle_drawer_of_the_cabinet\": 0.9, \"put_the_bowl_on_the_stove\": 0.9, \"put_the_wine_bottle_on_top_of_the_cabinet\": 0.5, \"open_the_top_drawer_and_put_the_bowl_inside\": 0.4, \"put_the_bowl_on_top_of_the_cabinet\": 0.6, \"push_the_plate_to_the_front_of_the_stove\": 0.8, \"put_the_cream_cheese_in_the_bowl\": 0.5, \"turn_on_the_stove\": 0.9, \"put_the_bowl_on_the_plate\": 0.9, \"put_the_wine_bottle_on_the_rack\": 0.7}}, \"notes\": \"Cron false positive: eval completed normally (71.0%), but no W&B/sentinel → auto-resolved as failed. Manually corrected to success.\"}, \"eval-vla-only-long-seed46\": {\"updated_at\": \"2026-05-19T20:08:18.540Z\", \"metrics\": {\"overall_success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\": 0, \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\": 0, \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\": 0.9, \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\": 0, \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\": 0.5, \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\": 0.1, \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\": 0.1, \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\": 0, \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\": 0, \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\": 0.2}}, \"notes\": \"Cron false positive: eval completed normally (18.0%), but no W&B/sentinel → auto-resolved as failed. Manually corrected to success.\"}, \"eval-obs-only-object-norm005-seed48\": {\"updated_at\": \"2026-05-19T19:37:16.188Z\", \"metrics\": {\"sr\": 0.17, \"sr_pct\": \"17.0%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.1, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.3, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}}, \"eval-vla-only-long-seed45\": {\"updated_at\": \"2026-05-19T19:21:47.544Z\", \"metrics\": {\"overall_success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\": 0, \"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\": 0, \"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\": 1, \"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\": 0, \"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\": 0.2, \"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\": 0.2, \"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\": 0.1, \"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\": 0, \"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\": 0, \"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\": 0.2}}}, \"eval-perdof-object-norm003-seed47\": {\"updated_at\": \"2026-05-19T19:05:12.052Z\", \"metrics\": {\"overall_success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-perdof-object-norm005-seed47\": {\"updated_at\": \"2026-05-19T19:05:09.001Z\", \"metrics\": {\"overall_success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-vla-only-long-seed44\": {\"updated_at\": \"2026-05-19T18:38:52.937Z\", \"metrics\": {\"overall_success_rate\": 0.12, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.2, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.1}}}, \"eval-vla-only-long-seed42\": {\"updated_at\": \"2026-05-19T18:38:48.009Z\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.8, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.1, \"STUDY_SCENE1_book_caddy\": 0.1, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.1}}}, \"eval-vla-only-long-seed43\": {\"updated_at\": \"2026-05-19T18:33:56.305Z\", \"metrics\": {\"overall_success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"LIVING_ROOM_SCENE2_alphabet_soup_tomato_sauce_basket\": 0, \"LIVING_ROOM_SCENE2_cream_cheese_butter_basket\": 0, \"KITCHEN_SCENE3_stove_moka_pot\": 0.7, \"KITCHEN_SCENE4_black_bowl_drawer\": 0, \"LIVING_ROOM_SCENE5_white_mug_left_yellow_mug_right\": 0.3, \"STUDY_SCENE1_book_caddy\": 0, \"LIVING_ROOM_SCENE6_white_mug_plate_chocolate_pudding\": 0.1, \"LIVING_ROOM_SCENE1_alphabet_soup_cream_cheese_basket\": 0, \"KITCHEN_SCENE8_both_moka_pots_stove\": 0, \"KITCHEN_SCENE6_yellow_white_mug_microwave\": 0.2}}}, \"eval-obs-only-spatial-norm02-seed47\": {\"updated_at\": \"2026-05-19T18:04:19.943Z\", \"metrics\": {\"overall_success_rate\": 0.32, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.8, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0.1, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}}, \"eval-random-selection-object-k5-seed45-r2\": {\"updated_at\": \"2026-05-19T16:31:13.969Z\", \"metrics\": {\"success_rate\": 0.07, \"successes\": 7, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed44-r2\": {\"updated_at\": \"2026-05-19T16:31:10.982Z\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed43-r2\": {\"updated_at\": \"2026-05-19T16:31:08.997Z\", \"metrics\": {\"success_rate\": 0.11, \"successes\": 11, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-random-selection-object-k5-seed42-r2\": {\"updated_at\": \"2026-05-19T16:31:06.453Z\", \"metrics\": {\"success_rate\": 0.14, \"successes\": 14, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed44-r2\": {\"updated_at\": \"2026-05-19T16:30:37.908Z\", \"metrics\": {\"success_rate\": 0.37, \"successes\": 37, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-k5-seed45-r2\": {\"updated_at\": \"2026-05-19T16:30:18.549Z\", \"metrics\": {\"success_rate\": 0.34, \"successes\": 34, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_bowl_between_plate_ramekin\": 0.9, \"pick_up_bowl_next_to_ramekin\": 1, \"pick_up_bowl_from_table_center\": 0, \"pick_up_bowl_on_cookie_box\": 0.3, \"pick_up_bowl_in_top_drawer\": 0.1, \"pick_up_bowl_on_ramekin\": 0, \"pick_up_bowl_next_to_cookie_box\": 0.9, \"pick_up_bowl_on_stove\": 0, \"pick_up_bowl_next_to_plate\": 0.2, \"pick_up_bowl_on_wooden_cabinet\": 0}}}, \"plan_602-latency-profiling\": {\"updated_at\": \"2026-05-19T16:17:38.007Z\", \"metrics\": {\"vla_encode_ms\": 28.4, \"crm_forward_ms\": 0.246, \"preprocess_ms\": 0.96, \"batched_K1_ms\": 180, \"batched_K5_ms\": 182.3, \"batched_K10_ms\": 162.3, \"batched_K20_ms\": 167.4, \"sequential_K1_ms\": 177, \"sequential_K5_ms\": 891.7, \"sequential_K10_ms\": 1638.9, \"sequential_K20_ms\": 3245.8, \"cgs_K10_ms\": 6.3, \"full_pipe_K10_ms\": 200.7, \"full_pipe_K20_ms\": 199.7, \"vla_model_mb\": 884.1, \"crm_model_mb\": 1.8, \"peak_K20_mb\": 1085.1}}, \"eval-vla-only-spatial-seed45\": {\"updated_at\": \"2026-05-19T16:06:09.222Z\", \"metrics\": {\"success_rate\": 0.27, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.7, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.2, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm005-seed45-r2\": {\"updated_at\": \"2026-05-19T16:06:07.907Z\", \"metrics\": {\"success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"sr_pct\": \"10%\"}}, \"eval-vla-only-spatial-seed44\": {\"updated_at\": \"2026-05-19T15:30:01.540Z\", \"metrics\": {\"success_rate\": 0.31, \"successes\": 31, \"total\": 100, \"per_task\": {\"pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate\": 0.6, \"pick_up_the_black_bowl_next_to_the_ramekin_and_place_it_on_the_plate\": 1, \"pick_up_the_black_bowl_from_table_center_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_cookie_box_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_in_the_top_drawer_of_the_wooden_cabinet_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_cookie_box_and_place_it_on_the_plate\": 0.9, \"pick_up_the_black_bowl_on_the_stove_and_place_it_on_the_plate\": 0, \"pick_up_the_black_bowl_next_to_the_plate_and_place_it_on_the_plate\": 0.3, \"pick_up_the_black_bowl_on_the_wooden_cabinet_and_place_it_on_the_plate\": 0}}}, \"eval-obs-only-object-default-seed48-r2\": {\"updated_at\": \"2026-05-19T14:58:17.531Z\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}, \"notes\": \"误判 failed: cron 检测到 tmux session 死亡，但实验已正常完成并写入完整 JSON。手动验证 output JSON 完整（59 行，10 tasks × 10 rollouts）。success_rate=0.17，与原 seed48 (bjb2-28827) 一致。\"}, \"eval-vla-only-spatial-seed43\": {\"updated_at\": \"2026-05-19T14:43:19.646Z\", \"metrics\": {\"success_rate\": 0.29, \"successes\": 29, \"total\": 100, \"per_task\": {\"between_plate_and_ramekin\": 0.7, \"next_to_ramekin\": 0.8, \"from_table_center\": 0.1, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.1, \"on_wooden_cabinet\": 0}}}, \"eval-vla-only-spatial-seed42\": {\"updated_at\": \"2026-05-19T14:38:29.599Z\", \"metrics\": {\"success_rate\": 0.3, \"per_task\": {\"between_plate_and_ramekin\": 0.6, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.2, \"in_top_drawer\": 0, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.9, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}}, \"eval-obs-only-spatial-norm02-seed44\": {\"updated_at\": \"2026-05-19T14:26:11.536Z\", \"metrics\": {\"success_rate\": 0.36, \"successes\": 36, \"total\": 100}}, \"eval-obs-only-object-norm003-seed47-r2\": {\"updated_at\": \"2026-05-19T14:25:56.640Z\", \"notes\": \"2026-05-19 12:58 UTC: FALSE ALARM — cron 检测到旧进程 EXIT_CODE=129(被 kill 的重复进程 PID 892663)，误标为 failed。实际进程 PID 894900 仍在 bjb1-32546 GPU 3 正常运行，5/10 tasks 完成 (T1=0%, T2=0%, T3=20%, T4=30%, T5=0%)。已恢复 RUNNING。\", \"metrics\": {\"success_rate\": 0.15, \"successes\": 15, \"total\": 100}}, \"eval-obs-only-object-norm003-seed48\": {\"updated_at\": \"2026-05-19T14:00:43.326Z\", \"notes\": \"2026-05-19 12:58 UTC: FALSE ALARM 确认 — PID 67825 在 bjb1-18228 GPU 1 正常运行中。已完成 5/10 tasks + T6 进行中 (T1=0%, T2=0%, T3=20%, T4=40%, T5=0%, T6 doing 5/10=1/5)。conclusion=failed 为误标(cron 误报)，无法设 null。\", \"metrics\": {\"success_rate\": 0.15, \"successes\": 15, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 2, \"bbq_sauce\": 4, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 0, \"milk\": 2, \"chocolate_pudding\": 4, \"orange_juice\": 2}}}, \"eval-perdof-object-norm01-seed43\": {\"updated_at\": \"2026-05-19T13:39:15.552Z\", \"metrics\": {\"sr\": 0.12, \"sr_pct\": \"12%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}}, \"eval-obs-only-object-default-seed45-r2\": {\"updated_at\": \"2026-05-19T13:35:23.895Z\", \"metrics\": {\"sr\": 0.18, \"sr_pct\": \"18%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}}, \"eval-argmin-object-k5-seed42\": {\"updated_at\": \"2026-05-19T13:30:16.050Z\", \"metrics\": {\"sr\": 0.15, \"sr_pct\": \"15%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-argmin-object-k5-seed45\": {\"updated_at\": \"2026-05-19T13:26:50.930Z\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.3}}}, \"eval-argmin-object-k5-seed43\": {\"updated_at\": \"2026-05-19T13:26:46.918Z\", \"metrics\": {\"sr\": 0.13, \"sr_pct\": \"13%\", \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm03-seed43\": {\"updated_at\": \"2026-05-19T13:24:40.192Z\", \"metrics\": {\"sr\": 5, \"sr_pct\": \"5%\", \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-spatial-norm02-seed45\": {\"updated_at\": \"2026-05-19T13:12:13.645Z\", \"metrics\": {\"success_rate\": 0.34, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 34}}, \"eval-obs-only-object-norm003-seed44-bjb2\": {\"updated_at\": \"2026-05-19T12:59:25.958Z\", \"notes\": \"2026-05-19 21:00 UTC: 实验实际成功完成。JSON 输出在 /root/logs/eval_object_obs_only_norm003_seed44.json (注意：路径是 /root/logs/ 而非 /root/acr-vla-conformal-refinement/logs/)。10/10 tasks 全部完成，overall SR=17% (17/100)。误标 failed 原因：startup recovery 发现 RUNNING 状态无 cron 监控和 PID 信息，自动标记为 failed。\"}, \"train-crm-k1-accg-object-seed42-full\": {\"updated_at\": \"2026-05-19T12:48:29.290Z\"}, \"plan_701-precompute-k1-spatial\": {\"updated_at\": \"2026-05-19T12:48:27.021Z\"}, \"plan_701-crm-k1-train\": {\"updated_at\": \"2026-05-19T12:48:10.176Z\"}, \"eval_obs_only_norm03_seed48\": {\"updated_at\": \"2026-05-19T12:48:06.312Z\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 16}}, \"eval_obs_only_norm01_seed48\": {\"updated_at\": \"2026-05-19T12:48:03.869Z\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"successes\": 18}}, \"eval-lto-splitA-vla-only-r3\": {\"updated_at\": \"2026-05-19T12:48:01.446Z\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"eval-lto-splitA-vla-only-r2\": {\"updated_at\": \"2026-05-19T12:47:58.882Z\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"crm-lto-splitA-train\": {\"updated_at\": \"2026-05-19T12:47:52.436Z\"}, \"eval-perdof-object-norm003-seed48\": {\"updated_at\": \"2026-05-19T12:23:18.801Z\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-spatial-norm02-k5-seed43\": {\"updated_at\": \"2026-05-19T11:34:16.077Z\", \"metrics\": {\"success_rate\": 0.32, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-k5-seed48\": {\"updated_at\": \"2026-05-19T11:34:12.397Z\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-spatial-norm02-k5-seed42\": {\"updated_at\": \"2026-05-19T11:31:39.191Z\", \"metrics\": {\"success_rate\": 0.35, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-k5-seed46\": {\"updated_at\": \"2026-05-19T11:30:55.300Z\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-lto-splitA-vla-only-v2\": {\"updated_at\": \"2026-05-19T11:30:43.198Z\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 5, \"n_rollouts\": 10, \"total_rollouts\": 50, \"successes\": 7}}, \"eval-perdof-object-norm03-seed47\": {\"updated_at\": \"2026-05-19T11:30:17.012Z\", \"metrics\": {\"success_rate\": 0.05, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-obs-only-object-default-seed48\": {\"updated_at\": \"2026-05-19T11:30:15.785Z\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-perdof-object-norm003-seed46\": {\"updated_at\": \"2026-05-19T11:30:14.493Z\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-perdof-object-norm005-seed46\": {\"updated_at\": \"2026-05-19T11:29:18.036Z\", \"metrics\": {\"success_rate\": 0.11, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-obs-only-object-norm02-k5-seed47\": {\"updated_at\": \"2026-05-19T11:27:53.132Z\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed45\": {\"updated_at\": \"2026-05-19T11:27:25.914Z\", \"metrics\": {\"success_rate\": 0.1, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-obs-only-object-norm005-seed47\": {\"updated_at\": \"2026-05-19T11:27:24.704Z\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-perdof-object-norm01-seed48\": {\"updated_at\": \"2026-05-19T11:25:28.189Z\", \"metrics\": {\"success_rate\": 0.12, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束. JSON 位于 /root/logs/ 而非项目 logs/ 目录\"}, \"eval-obs-only-object-default-seed47\": {\"updated_at\": \"2026-05-19T11:25:18.480Z\", \"metrics\": {\"success_rate\": 0.16, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-perdof-object-norm03-seed46\": {\"updated_at\": \"2026-05-19T11:25:13.541Z\", \"metrics\": {\"success_rate\": 0.04, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-obs-only-object-norm03-seed46\": {\"updated_at\": \"2026-05-19T11:25:11.008Z\", \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-scalar-object-seed46\": {\"updated_at\": \"2026-05-19T11:25:07.860Z\", \"metrics\": {\"success_rate\": 0.09, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-obs-only-object-norm01-seed47\": {\"updated_at\": \"2026-05-19T11:25:01.605Z\", \"metrics\": {\"success_rate\": 0.17, \"total_rollouts\": 100}, \"notes\": \"采集时间 2026-05-19, 进程已自然结束\"}, \"eval-obs-only-object-norm01-seed45-r2\": {\"updated_at\": \"2026-05-19T05:02:02.994Z\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"crm-lto-splitA-train-fixed\": {\"updated_at\": \"2026-05-19T04:32:49.103Z\"}, \"eval-perdof-object-norm003-seed43\": {\"updated_at\": \"2026-05-19T03:28:52.476Z\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-norm005-seed43\": {\"updated_at\": \"2026-05-19T02:56:00.676Z\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-default-seed43\": {\"updated_at\": \"2026-05-19T01:44:05.704Z\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-seed48-r2\": {\"updated_at\": \"2026-05-19T01:40:59.658Z\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-default-seed45\": {\"updated_at\": \"2026-05-19T01:38:34.712Z\", \"metrics\": {\"success_rate\": 0, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-k5-seed45\": {\"updated_at\": \"2026-05-19T01:33:59.345Z\", \"metrics\": {\"success_rate\": 0.15, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-vla-only-object-seed46\": {\"updated_at\": \"2026-05-19T01:33:32.294Z\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed48\": {\"updated_at\": \"2026-05-19T01:32:13.545Z\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm02-k5-seed44\": {\"updated_at\": \"2026-05-18T21:05:50.448Z\", \"metrics\": {\"success_rate\": 0.17, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed44\": {\"updated_at\": \"2026-05-18T19:54:45.657Z\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm01-seed42\": {\"updated_at\": \"2026-05-18T18:53:10.563Z\", \"metrics\": {\"success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed42\": {\"updated_at\": \"2026-05-18T18:53:09.494Z\", \"metrics\": {\"success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm01-seed46-r3\": {\"updated_at\": \"2026-05-18T16:48:10.654Z\", \"metrics\": {\"success_rate\": 0.18, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed45\": {\"updated_at\": \"2026-05-18T16:48:08.690Z\", \"metrics\": {\"success_rate\": 0.14, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-random-selection-object-seed43\": {\"updated_at\": \"2026-05-18T15:50:02.402Z\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0, 0.1, 0.1, 0, 0.1, 0, 0.1, 0.2, 0.3]}}, \"eval-perdof-object-norm005-seed44\": {\"updated_at\": \"2026-05-18T15:18:13.193Z\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.2, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.2, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-vla-only-object-seed45-r2\": {\"updated_at\": \"2026-05-18T14:17:30.462Z\", \"metrics\": {\"overall_success_rate\": 0.11, \"n_tasks\": 10, \"n_rollouts_per_task\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.3, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm03-seed48\": {\"updated_at\": \"2026-05-18T13:27:03.418Z\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100}}, \"eval-obs-only-object-norm005-seed44\": {\"updated_at\": \"2026-05-18T13:07:06.200Z\", \"metrics\": {\"success_rate\": 0.16, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_episodes\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}}, \"eval-obs-only-object-norm02-k5-seed43\": {\"updated_at\": \"2026-05-18T12:39:30.555Z\", \"metrics\": {\"success_rate\": 0.19, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.2, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}}, \"eval-random-selection-object-seed42\": {\"updated_at\": \"2026-05-18T12:20:08.756Z\", \"metrics\": {\"success_rate\": 0.13, \"n_tasks\": 10, \"n_rollouts\": 10, \"total_rollouts\": 100, \"per_task_sr\": [0, 0.1, 0.1, 0.4, 0, 0.2, 0, 0.1, 0.2, 0.2]}}, \"eval-perdof-object-norm02-seed43\": {\"updated_at\": \"2026-05-18T10:56:45.558Z\", \"metrics\": {\"success_rate\": 0.09, \"n_tasks\": 10, \"n_rollouts\": 10}}, \"eval-obs-only-object-norm01-seed45\": {\"updated_at\": \"2026-05-18T07:05:03.603Z\", \"notes\": \"PID 474319 died, GPU idle 28h+. Ghost experiment — process dead but registry not updated.\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-obs-only-object-norm02-k5-seed42\": {\"updated_at\": \"2026-05-18T07:05:02.646Z\", \"metrics\": {\"overall_success_rate\": 0.14}}, \"eval-acr-spatial-v3\": {\"updated_at\": \"2026-05-18T05:54:17.209Z\", \"metrics\": {\"tasks_done\": \"4/10\", \"overall_success_rate\": 0.025, \"total_successes\": 1, \"total_rollouts\": 40, \"per_task_partial\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.1, \"pick_up_black_bowl_next_to_ramekin\": 0, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0}, \"snapshot_time\": \"2026-05-14T18:15Z\"}}, \"eval-perdof-object-norm02-seed47\": {\"updated_at\": \"2026-05-18T04:37:10.886Z\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-default-seed46\": {\"updated_at\": \"2026-05-18T03:03:50.286Z\", \"metrics\": {\"overall_sr\": 0.15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-perdof-object-norm02-seed46\": {\"updated_at\": \"2026-05-18T02:24:22.787Z\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-obs-only-object-norm005-seed43-r2\": {\"updated_at\": \"2026-05-18T00:42:42.174Z\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}}, \"eval-perdof-object-norm02-seed43-r3\": {\"updated_at\": \"2026-05-17T23:17:06.378Z\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100}}, \"eval-perdof-object-norm01-seed47-bjb1\": {\"updated_at\": \"2026-05-17T23:00:33.671Z\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100}}, \"eval-openvla-object-vla-only-seed42-v2\": {\"updated_at\": \"2026-05-17T22:39:25.302Z\", \"metrics\": {\"overall_sr\": 0.69, \"n_tasks\": 10, \"n_trials_per_task\": 10, \"total_rollouts\": 100}}, \"eval-perdof-object-norm01-seed46-r2\": {\"updated_at\": \"2026-05-17T21:01:12.153Z\", \"metrics\": {\"overall_sr\": 0.1, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"plan_602-latency-profile\": {\"updated_at\": \"2026-05-17T18:35:42.842Z\", \"metrics\": {\"vla_encode_prefix_ms\": 33.5, \"vla_sample_K1_ms\": 192.6, \"vla_sample_K5_ms\": 965.3, \"vla_sample_K10_ms\": 1913.7, \"vla_sample_K20_ms\": 3858.2, \"cgs_ms\": 6.2, \"crm_forward_ms\": 0.3, \"full_pipeline_K10_ms\": 1908.2, \"acr_overhead_pct\": 0.34}}, \"train-crm-k1-accg-object-seed42-v2\": {\"updated_at\": \"2026-05-17T18:31:23.291Z\", \"notes\": \"Retry after W&B API key crash. Added --no_wandb. Precompute cache reused (65,223 samples). Training restarted from scratch (epoch 1/50). PID 447923 on cuda:0, tmux session: train-crm-k1-v2.\", \"metrics\": {\"best_val_loss\": 0.007199, \"total_epochs\": 50, \"train_samples\": 65223, \"obs_dim\": \"4x960D\", \"multi_scale\": true}}, \"eval-obs-only-object-default-seed45\": {\"updated_at\": \"2026-05-17T17:32:15.936Z\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks\": 10, \"rollouts_per_task\": 20, \"total_successes\": 24, \"total_rollouts\": 200}}, \"eval-scalar-object-seed45\": {\"updated_at\": \"2026-05-17T17:29:34.723Z\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"best_task\": \"chocolate_pudding_0.25\", \"worst_task\": \"alphabet_soup_0.0\"}}, \"eval-perdof-object-norm02-seed45\": {\"updated_at\": \"2026-05-17T17:03:14.729Z\", \"metrics\": {\"overall_success_rate\": 0.09, \"successes\": 18, \"total\": 200, \"n_tasks\": 10, \"n_rollouts_per_task\": 20}, \"notes\": \"perdof ε=0.2 seed45: 9% (18/200). Cross-seed: seed42=11%, seed43=9%, seed44=10%, seed45=9%. Mean ~9.75%.\"}, \"eval-perdof-object-norm02-seed44\": {\"updated_at\": \"2026-05-17T16:52:17.419Z\", \"metrics\": {\"overall_success_rate\": 0.1, \"successes\": 10, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"train-crm-k1-accg-object-seed42-fallback\": {\"updated_at\": \"2026-05-17T15:19:16.626Z\", \"metrics\": {\"best_val_loss\": 0.006505, \"best_epoch\": 43, \"total_epochs\": 50, \"train_samples\": 4857, \"obs_dim\": 960, \"multi_scale\": false, \"wall_clock_seconds\": 914.9}}, \"eval-obs-only-object-norm02-seed47\": {\"updated_at\": \"2026-05-17T11:05:43.649Z\", \"metrics\": {\"success_rate\": 0.2, \"successes\": 20, \"total\": 100, \"benchmark\": \"object\", \"mode\": \"obs_only\", \"norm\": 0.2, \"seed\": 47}}, \"eval-obs-only-object-norm02-seed46\": {\"updated_at\": \"2026-05-17T10:54:36.728Z\", \"metrics\": {\"success_rate\": 0.15, \"total_episodes\": 100, \"successes\": 15, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 2, \"bbq_sauce\": 3, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 4, \"orange_juice\": 3}}}, \"eval-argmin-object-seed47\": {\"updated_at\": \"2026-05-17T10:54:02.629Z\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 47, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.2}}}, \"eval-perdof-object-norm01-seed45\": {\"updated_at\": \"2026-05-17T10:22:14.183Z\", \"metrics\": {\"overall_sr\": 0.11, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}, \"seed\": 45, \"benchmark\": \"object\", \"mode\": \"crm_perdof\", \"max_correction_norm\": 0.1}}, \"eval-argmin-object-seed46\": {\"updated_at\": \"2026-05-17T10:19:26.819Z\", \"metrics\": {\"overall_sr\": 0.1, \"total_successes\": 10, \"total_rollouts\": 100, \"n_rollouts_per_task\": 10, \"seed\": 46, \"benchmark\": \"object\", \"K\": 10, \"mode\": \"reconvla\", \"baseline_mode\": \"single\", \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.1, \"orange_juice\": 0.1}}}, \"eval-obs-only-object-norm03-seed45-r2\": {\"updated_at\": \"2026-05-17T07:02:49.285Z\", \"metrics\": {\"overall_success_rate\": 14, \"total_successes\": 14, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 10, \"milk\": 10, \"chocolate_pudding\": 30, \"orange_juice\": 30}, \"max_correction_norm\": 0.3, \"seed\": 45, \"mode\": \"crm_obs_only\", \"benchmark\": \"object\"}}, \"eval-vla-mean-object-seed45\": {\"updated_at\": \"2026-05-17T06:54:28.933Z\", \"metrics\": {\"overall_sr\": 0.13, \"total_success\": 13, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"multi_seed_summary\": \"seed42=12%, seed43=15%, seed44=10%, seed45=13%, mean=12.5%\"}}, \"eval-argmin-object-seed45\": {\"updated_at\": \"2026-05-17T06:53:28.467Z\", \"metrics\": {\"overall_sr\": 0.12, \"successes\": 12, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}}, \"eval-direct-correction-object-seed42-r3\": {\"updated_at\": \"2026-05-17T04:48:50.296Z\", \"metrics\": {\"success_rate\": 0.14, \"total_episodes\": 100, \"successes\": 14, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 1, \"salad_dressing\": 1, \"bbq_sauce\": 4, \"ketchup\": 0, \"tomato_sauce\": 1, \"butter\": 1, \"milk\": 1, \"chocolate_pudding\": 3, \"orange_juice\": 2}}}, \"eval-vla-mean-spatial\": {\"updated_at\": \"2026-05-17T03:15:31.664Z\", \"metrics\": {\"overall_success_rate_10tasks\": 0.32, \"total_successes\": 32, \"total_trials\": 100, \"T1\": 0.7, \"T2\": 1, \"T3\": 0, \"T4\": 0.3, \"T5\": 0, \"T6\": 0, \"T7\": 0.8, \"T8\": 0, \"T9\": 0.3, \"T10\": 0.1}}, \"eval-acr-object-obs-only-norm02\": {\"updated_at\": \"2026-05-17T03:15:28.368Z\", \"metrics\": {\"overall_sr\": 0.22, \"total_success\": 22, \"total_rollouts\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.4, \"ketchup\": 0.2, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.6, \"orange_juice\": 0.3}}}, \"eval-spatial-v7-full\": {\"updated_at\": \"2026-05-17T03:15:26.392Z\", \"metrics\": {\"overall_success_rate\": 0.3, \"total_successes\": 30, \"total_episodes\": 100, \"n_tasks\": 10, \"n_rollouts\": 10, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.2, \"pick_up_black_bowl_in_top_drawer\": 0, \"pick_up_black_bowl_on_ramekin\": 0, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.3, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}}, \"eval-object-v8-full\": {\"updated_at\": \"2026-05-17T03:15:25.342Z\", \"metrics\": {\"overall_success_rate\": 0.13, \"total_successes\": 13, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"precompute-v5-shard2\": {\"updated_at\": \"2026-05-17T03:15:19.323Z\"}, \"precompute-v5-shard1\": {\"updated_at\": \"2026-05-17T03:15:18.177Z\"}, \"precompute-v5-shard0\": {\"updated_at\": \"2026-05-17T03:15:17.511Z\"}, \"precompute-v4-shard2\": {\"updated_at\": \"2026-05-17T03:15:16.391Z\"}, \"precompute-v4-shard1\": {\"updated_at\": \"2026-05-17T03:15:15.362Z\"}, \"precompute-v4-shard0\": {\"updated_at\": \"2026-05-17T03:15:14.415Z\"}, \"eval-obs-only-object-norm01-seed44\": {\"updated_at\": \"2026-05-17T03:15:05.867Z\", \"metrics\": {\"overall_sr\": 0.16, \"total_success\": 16, \"total_rollouts\": 100, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.3, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-vla-only-object-seed45\": {\"updated_at\": \"2026-05-17T03:15:04.317Z\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 18, \"total\": 200, \"tasks_done\": 10}}, \"eval-vla-only-object-seed43\": {\"updated_at\": \"2026-05-17T03:15:03.364Z\", \"metrics\": {\"overall_sr\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"source\": \"json_file_verified_by_worker\"}, \"notes\": \"seed=43 VLA-only 12% = seed=42 12%，baseline 跨 seed 完全一致。per-task 分布略有差异（seed43: chocolate_pudding 40% vs seed42: 20%, bbq_sauce 30% vs 20%），但总 SR 相同。确认 VLA-only 作为稳定 baseline。seed=43 六方对比表第一个完成点。\"}, \"eval-vla-mean-spatial-t10\": {\"updated_at\": \"2026-05-17T03:14:58.588Z\", \"metrics\": {\"T10_on_wooden_shelf\": \"10% (1/10)\", \"note\": \"Only ran task 9 (start_task=9). T10 = wooden shelf task.\"}}, \"eval-reconvla-spatial-v3\": {\"updated_at\": \"2026-05-17T03:14:57.896Z\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_rollouts\": 100, \"per_task\": {\"pick_up_black_bowl_between_plate_and_ramekin\": 0.6, \"pick_up_black_bowl_next_to_ramekin\": 1, \"pick_up_black_bowl_from_table_center\": 0, \"pick_up_black_bowl_on_cookie_box\": 0.3, \"pick_up_black_bowl_in_top_drawer\": 0.1, \"pick_up_black_bowl_on_ramekin\": 0.1, \"pick_up_black_bowl_next_to_cookie_box\": 0.9, \"pick_up_black_bowl_on_stove\": 0, \"pick_up_black_bowl_next_to_plate\": 0.4, \"pick_up_black_bowl_on_wooden_cabinet\": 0}}}, \"crm-train-v2-scalar-unc\": {\"updated_at\": \"2026-05-17T03:14:56.290Z\", \"metrics\": {\"best_val_loss\": 0.047202, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.069679, \"comparison_vs_old\": \"old_6D_buggy=0.008379, new=0.047202 (loss metric changed with v2 fix)\"}}, \"crm-train-v2-perdof\": {\"updated_at\": \"2026-05-17T03:14:55.328Z\", \"metrics\": {\"best_val_loss\": 0.051684, \"best_epoch\": 48, \"total_epochs\": 50, \"final_train_loss\": 0.076748, \"comparison_vs_old\": \"old_6D_buggy=0.009046, new=0.051684 (loss metric changed with v2 fix)\"}}, \"crm-train-v2-obs-only\": {\"updated_at\": \"2026-05-17T03:14:53.940Z\", \"metrics\": {\"best_val_loss\": 0.050501, \"best_epoch\": 50, \"total_epochs\": 50, \"final_train_loss\": 0.074839, \"comparison_vs_old\": \"old_6D_buggy=0.018312, new=0.050501 (loss metric changed with v2 fix)\"}}, \"precompute-shard2\": {\"updated_at\": \"2026-05-17T03:13:50.200Z\"}, \"precompute-shard1\": {\"updated_at\": \"2026-05-17T03:13:49.286Z\"}, \"precompute-shard0\": {\"updated_at\": \"2026-05-17T03:13:43.682Z\"}, \"precompute-k5\": {\"updated_at\": \"2026-05-17T03:13:41.787Z\", \"metrics\": {\"spatial_samples\": 12167, \"object_samples\": 14570, \"total_samples\": 26737, \"spatial_cache_mb\": 106, \"object_cache_mb\": 127, \"total_cache_mb\": 233, \"runtime_min\": 107}}, \"mvp-point-reaching\": {\"updated_at\": \"2026-05-17T03:13:35.534Z\", \"metrics\": {\"group1_oracle\": {\"A_scalar\": {\"mse_x\": 0.180218, \"mse_y\": 0.02497, \"mse_z\": 0.024232, \"total\": 0.076473}, \"B_perDOF\": {\"mse_x\": 0.172652, \"mse_y\": 0.015544, \"mse_z\": 0.01561, \"total\": 0.067935}, \"C_none\": {\"mse_x\": 0.22706, \"mse_y\": 0.025542, \"mse_z\": 0.024753, \"total\": 0.092451}}, \"group2_oracle\": {\"A_scalar\": {\"mse_x\": 0.064642, \"mse_y\": 0.023836, \"mse_z\": 0.022967, \"total\": 0.037148}, \"B_perDOF\": {\"mse_x\": 0.053403, \"mse_y\": 0.015695, \"mse_z\": 0.01573, \"total\": 0.028276}, \"C_none\": {\"mse_x\": 0.084178, \"mse_y\": 0.025427, \"mse_z\": 0.024798, \"total\": 0.044801}}, \"group3_oracle\": {\"A_scalar\": {\"mse_x\": 0.042948, \"mse_y\": 0.023218, \"mse_z\": 0.022365, \"total\": 0.02951}, \"B_perDOF\": {\"mse_x\": 0.033008, \"mse_y\": 0.015621, \"mse_z\": 0.015647, \"total\": 0.021425}, \"C_none\": {\"mse_x\": 0.053043, \"mse_y\": 0.025523, \"mse_z\": 0.024741, \"total\": 0.034436}}, \"group4_K10\": {\"A_scalar\": {\"mse_x\": 0.187418, \"mse_y\": 0.024701, \"mse_z\": 0.024277, \"total\": 0.078799}, \"B_perDOF\": {\"mse_x\": 0.182888, \"mse_y\": 0.019072, \"mse_z\": 0.018475, \"total\": 0.073478}, \"C_none\": {\"mse_x\": 0.21507, \"mse_y\": 0.02496, \"mse_z\": 0.024637, \"total\": 0.088223}}, \"group5_K10\": {\"A_scalar\": {\"mse_x\": 0.064895, \"mse_y\": 0.02386, \"mse_z\": 0.023596, \"total\": 0.037451}, \"B_perDOF\": {\"mse_x\": 0.05851, \"mse_y\": 0.018868, \"mse_z\": 0.018471, \"total\": 0.03195}, \"C_none\": {\"mse_x\": 0.077047, \"mse_y\": 0.024825, \"mse_z\": 0.02464, \"total\": 0.042171}}, \"group6_K10\": {\"A_scalar\": {\"mse_x\": 0.041848, \"mse_y\": 0.02344, \"mse_z\": 0.023207, \"total\": 0.029498}, \"B_perDOF\": {\"mse_x\": 0.036348, \"mse_y\": 0.018736, \"mse_z\": 0.018453, \"total\": 0.024512}, \"C_none\": {\"mse_x\": 0.048365, \"mse_y\": 0.024827, \"mse_z\": 0.024577, \"total\": 0.03259}}, \"pass_criteria\": {\"group1\": \"PASS\", \"group4\": \"PASS\", \"overall\": \"SUCCESS\"}, \"summary_pct_improvements\": {\"reference_group\": \"group4_K10 (sigma=0.5/0.1/0.1, K=10 estimated uncertainty)\", \"perDOF_vs_scalar_total\": 6.75, \"perDOF_vs_none_total\": 16.71, \"perDOF_vs_scalar_y_axis\": 22.79, \"perDOF_vs_scalar_z_axis\": 23.9, \"paper_claims\": {\"6.7_pct_over_scalar\": \"group4 total: (0.078799-0.073478)/0.078799 = 6.75%\", \"16.7_pct_over_none\": \"group4 total: (0.088223-0.073478)/0.088223 = 16.71%\", \"22_24_pct_per_axis\": \"group4 y: 22.79%, z: 23.90%\"}}}}, \"eval-obs-only-object-default-seed44\": {\"updated_at\": \"2026-05-17T03:09:38.443Z\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-mag-perdof-norm005-object\": {\"updated_at\": \"2026-05-17T03:09:30.045Z\", \"metrics\": {\"overall_sr\": 0.14, \"successes\": 14, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}}, \"eval-mag-perdof-norm02-seed43-object-r3\": {\"updated_at\": \"2026-05-17T03:09:27.225Z\", \"metrics\": {\"overall_sr\": 0.09, \"successes\": 9, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.1, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}, \"vs_seed42\": \"-2pp (11% → 9%)\", \"pooled_2seed_perdof_02\": \"10% (20/200)\"}}, \"eval-mag-perdof-norm03-object-r3\": {\"updated_at\": \"2026-05-17T03:09:17.332Z\", \"metrics\": {\"overall_sr\": 0.04, \"successes\": 4, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10}}, \"eval-mag-obsonly-norm005\": {\"updated_at\": \"2026-05-17T03:09:15.263Z\", \"metrics\": {\"benchmark\": \"spatial\", \"mode\": \"crm_obs_only\", \"max_correction_norm\": 0.05, \"n_rollouts\": 10, \"K\": 10, \"overall_sr\": 35, \"total_success\": 35, \"total_episodes\": 100, \"per_task\": {\"T0_between_plate_ramekin\": 80, \"T1_next_to_ramekin\": 90, \"T2_table_center\": 0, \"T3_on_cookie_box\": 40, \"T4_top_drawer\": 10, \"T5_on_ramekin\": 0, \"T6_next_to_cookie_box\": 80, \"T7_on_stove\": 0, \"T8_next_to_plate\": 50, \"T9_on_wooden_cabinet\": 0}}}, \"eval-mag-obsonly-norm003-b2\": {\"updated_at\": \"2026-05-17T03:09:11.273Z\", \"notes\": \"Ghost PID 211962 killed, b2 now running solo on bjb2-40593 cuda:0. PID 227434 confirmed alive (15min uptime, model loaded, eval executing, GPU 6185MiB/24564MiB, 12% util).\", \"metrics\": {\"overall_sr_10task\": 0.34, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task\": {\"between_plate_and_ramekin\": 0.9, \"next_to_ramekin\": 1, \"from_table_center\": 0, \"on_cookie_box\": 0.3, \"in_top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 0.8, \"on_stove\": 0, \"next_to_plate\": 0.3, \"on_wooden_cabinet\": 0}}}, \"eval-mag-obsonly-norm03-object\": {\"updated_at\": \"2026-05-17T03:09:10.586Z\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.19, \"successes\": 19, \"total\": 100}}, \"eval-mag-obsonly-norm005-object\": {\"updated_at\": \"2026-05-17T03:09:06.864Z\", \"metrics\": {\"overall_sr\": 0.13, \"tasks_completed\": 10, \"total_rollouts\": 100, \"successes\": 13, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"eval-obs-only-object-norm02-seed45\": {\"updated_at\": \"2026-05-16T21:33:38.747Z\", \"metrics\": {\"overall_sr\": 0.16, \"successes\": 16, \"total_rollouts\": 100, \"tasks_completed\": \"10/10\"}}, \"eval-obs-only-object-norm03-seed44\": {\"updated_at\": \"2026-05-16T19:37:12.898Z\", \"metrics\": {\"overall_sr\": 0.18, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.2, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-vla-mean-object-seed44\": {\"updated_at\": \"2026-05-16T18:36:08.965Z\", \"metrics\": {\"overall_sr\": 0.1, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.3, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0.1, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0.1, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 0, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.2, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.2}}}, \"eval-argmin-object-seed44-r2\": {\"updated_at\": \"2026-05-16T15:34:00.414Z\", \"metrics\": {\"overall_sr\": 0.13, \"successes\": 13, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.2}, \"note\": \"EXIT_CODE=129 was SIGHUP after completion, results valid. log: logs/eval_object_reconvla_seed44.json\"}}, \"eval-obs-only-object-norm02-seed44-r2\": {\"updated_at\": \"2026-05-16T15:25:14.349Z\", \"metrics\": {\"overall_sr\": 0.16, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}}}, \"eval-acr-object-v4-default-r2\": {\"updated_at\": \"2026-05-16T09:00:15.290Z\", \"metrics\": {\"overall_sr\": 0, \"successes\": 0, \"total\": 100, \"tasks_done\": 10, \"tasks_total\": 10, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0, \"bbq_sauce\": 0, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0, \"orange_juice\": 0}, \"note\": \"actual mode=crm_perdof with default norm (~1.42), NOT crm_default. Confirms catastrophic failure at uncontrolled correction magnitude.\"}}, \"eval-mag-perdof-norm003-object\": {\"updated_at\": \"2026-05-16T08:37:12.296Z\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.14, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.1}}}, \"eval-obs-only-object-norm02-seed43-r2\": {\"updated_at\": \"2026-05-16T07:46:23.704Z\", \"metrics\": {\"overall_sr\": 0.16, \"successes\": 16, \"total\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}, \"vs_seed42\": \"-6pp (22% → 16%)\", \"vs_argmin_seed43\": \"-1pp (17% → 16%)\", \"pooled_2seed_obs_only_02\": \"19% (38/200)\", \"pooled_2seed_argmin\": \"14.5% (29/200)\"}}, \"eval-vla-only-object-seed44-r2\": {\"updated_at\": \"2026-05-16T07:13:29.827Z\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.1, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.2}}}, \"eval-acr-object-obs-only-default\": {\"updated_at\": \"2026-05-16T07:09:01.967Z\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"overall_sr\": 0.17, \"per_task_sr\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.4, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.5, \"orange_juice\": 0.3}}}, \"eval-scalar-object-seed43\": {\"updated_at\": \"2026-05-16T06:04:05.747Z\", \"metrics\": {\"tasks_done\": 10, \"tasks_total\": 10, \"avg_sr\": 10, \"per_task_sr\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 30, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0, \"pick_up_the_milk_and_place_it_in_the_basket\": 10, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 30, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 30}}}, \"eval-mag-obsonly-norm003-object\": {\"updated_at\": \"2026-05-16T05:56:01.541Z\", \"metrics\": {\"overall_sr\": 0.16, \"tasks_done\": 100, \"tasks_total\": 100, \"per_task\": {\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\": 0, \"pick_up_the_cream_cheese_and_place_it_in_the_basket\": 0.2, \"pick_up_the_salad_dressing_and_place_it_in_the_basket\": 0.1, \"pick_up_the_bbq_sauce_and_place_it_in_the_basket\": 0.4, \"pick_up_the_ketchup_and_place_it_in_the_basket\": 0, \"pick_up_the_tomato_sauce_and_place_it_in_the_basket\": 0, \"pick_up_the_butter_and_place_it_in_the_basket\": 0.1, \"pick_up_the_milk_and_place_it_in_the_basket\": 0.2, \"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\": 0.3, \"pick_up_the_orange_juice_and_place_it_in_the_basket\": 0.3}}}, \"eval-vla-mean-object-seed43\": {\"updated_at\": \"2026-05-16T04:53:17.141Z\", \"metrics\": {\"overall_sr\": 0.15, \"tasks_done\": 10, \"tasks_total\": 10, \"total_success\": 15, \"total_rollouts\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.1, \"milk\": 0.3, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.1}}}, \"eval-perdof-object-seed43\": {\"updated_at\": \"2026-05-16T03:15:39.287Z\", \"metrics\": {\"overall_success_rate\": 0.12, \"tasks_done\": 10, \"tasks_total\": 10, \"total_rollouts\": 100, \"total_successes\": 12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0, \"milk\": 0, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.3}}}, \"eval-argmin-object-seed43\": {\"updated_at\": \"2026-05-16T00:37:43.289Z\", \"metrics\": {\"overall_success_rate\": 0.17, \"total_successes\": 17, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0.1, \"tomato_sauce\": 0.1, \"butter\": 0.2, \"milk\": 0.3, \"chocolate_pudding\": 0.4, \"orange_juice\": 0.2}}}, \"eval-mag-obsonly-norm03-r2\": {\"updated_at\": \"2026-05-15T17:22:51.755Z\", \"metrics\": {\"bowl_between\": 0.9, \"next_to_ramekin\": 1, \"table_center\": 0, \"cookie_box\": 0.3, \"top_drawer\": 0.1, \"on_ramekin\": 0, \"next_to_cookie_box\": 1, \"stove\": 0, \"next_to_plate\": 0.3, \"wooden_cabinet\": 0, \"overall_SR\": 0.36}}, \"eval-vla-mean-object\": {\"updated_at\": \"2026-05-15T17:01:25.883Z\", \"metrics\": {\"benchmark\": \"object\", \"mode\": \"vla_only\", \"baseline_mode\": \"mean\", \"n_rollouts\": 10, \"K\": 10, \"seed\": 42, \"overall_sr\": 12, \"total_success\": 12, \"total_rollouts\": 100, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 10, \"bbq_sauce\": 30, \"ketchup\": 10, \"tomato_sauce\": 10, \"butter\": 0, \"milk\": 20, \"chocolate_pudding\": 30, \"orange_juice\": 10}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_vla_mean.json\"}}, \"eval-reconvla-object\": {\"updated_at\": \"2026-05-15T16:25:17.101Z\", \"metrics\": {\"overall_sr\": 0.12, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0, \"salad_dressing\": 0.1, \"bbq_sauce\": 0.3, \"ketchup\": 0, \"tomato_sauce\": 0, \"butter\": 0.1, \"milk\": 0.1, \"chocolate_pudding\": 0.3, \"orange_juice\": 0.3}, \"n_rollouts\": 10, \"total_episodes\": 100, \"total_successes\": 12}}, \"eval-acr-object-v4-obs-only\": {\"updated_at\": \"2026-05-15T16:23:01.718Z\", \"metrics\": {\"overall_sr\": \"19.0% (19/100)\", \"total_success\": 19, \"total_rollouts\": 100, \"mode\": \"obs_only\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"tasks_done\": \"10/10\", \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"10%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"40%\", \"ketchup\": \"10%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"20%\", \"chocolate_pudding\": \"50%\", \"orange_juice\": \"30%\"}, \"json_output\": \"/root/acr-vla-conformal-refinement/logs/eval_object_obs_only.json\"}}, \"eval-acr-object-v4-perdof\": {\"updated_at\": \"2026-05-15T15:45:38.531Z\", \"metrics\": {\"overall_sr\": \"11.0% (11/100)\", \"total_success\": 11, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"object\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"alphabet_soup\": \"0%\", \"cream_cheese\": \"0%\", \"salad_dressing\": \"20%\", \"bbq_sauce\": \"30%\", \"ketchup\": \"0%\", \"tomato_sauce\": \"0%\", \"butter\": \"10%\", \"milk\": \"0%\", \"chocolate_pudding\": \"20%\", \"orange_juice\": \"30%\"}, \"note\": \"perdof object 11% vs argmin ~7% (partial). obs_only leads at ~14% (8/10). Confirms perdof not competitive on object.\"}}, \"eval-acr-spatial-v4-scalar-r2\": {\"updated_at\": \"2026-05-15T13:18:27.852Z\", \"metrics\": {\"overall_sr\": \"32.0% (32/100)\", \"total_success\": 32, \"total_rollouts\": 100, \"mode\": \"scalar_unc\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"10%\", \"T9\": \"10%\"}, \"note\": \"D030 confirmed: scalar_unc spatial 32% vs argmin 34% = -2pp. T0-T2 from original eval-acr-spatial-v4-scalar, T3-T9 from r2 restart. All CRM variants dead on spatial.\"}}, \"eval-acr-spatial-v4-obs-only-r3\": {\"updated_at\": \"2026-05-15T11:15:11.801Z\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"crm_obs_only\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"90%\", \"T1\": \"100%\", \"T2\": \"0%\", \"T3\": \"40%\", \"T4\": \"10%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"0%\", \"T8\": \"20%\", \"T9\": \"0%\"}, \"r3_subset_T6_T9\": \"27.5% (11/40)\", \"note\": \"D030: obs_only spatial 10-task = 35%. vs argmin 34% = +1pp. Scenario C threshold (>=39%) NOT MET. Earlier T0-T5 advantage (+5pp) wiped out by T6-T9.\"}}, \"eval-acr-spatial-v4-small-r2\": {\"updated_at\": \"2026-05-15T09:10:21.153Z\", \"notes\": \"[D027] Framing 暂不裁决。Scenario A/B/C 取决于 magnitude sweep + object benchmark 结果。spatial matched-task perdof=argmin (0pp) 意味着 Scenario A 在 spatial 上不可能。\", \"metrics\": {\"overall_sr\": \"35.0% (35/100)\", \"total_success\": 35, \"total_rollouts\": 100, \"mode\": \"perdof\", \"benchmark\": \"spatial\", \"max_correction_norm\": 0.1, \"seed\": 42, \"K\": 10, \"per_task\": {\"T0\": \"60%\", \"T1\": \"100%\", \"T2\": \"10%\", \"T3\": \"40%\", \"T4\": \"0%\", \"T5\": \"0%\", \"T6\": \"90%\", \"T7\": \"10%\", \"T8\": \"40%\", \"T9\": \"0%\"}, \"note\": \"D029: perdof spatial complete 10-task = 35%. vs argmin 34% = +1pp. Kill criterion triggered — per-DOF claim dead on spatial.\"}}, \"eval-argmin-only-spatial-r2\": {\"updated_at\": \"2026-05-15T06:39:37.926Z\", \"metrics\": {\"overall_success_rate\": 0.34, \"total_successes\": 34, \"total_trials\": 100, \"per_task\": {\"T0_between_plate_and_ramekin\": 0.6, \"T1_next_to_ramekin\": 1, \"T2_from_table_center\": 0, \"T3_on_cookie_box\": 0.3, \"T4_in_top_drawer\": 0.1, \"T5_on_ramekin\": 0.1, \"T6_next_to_cookie_box\": 0.9, \"T7_on_stove\": 0, \"T8_next_to_plate\": 0.3, \"T9_on_wooden_cabinet\": 0.1}, \"note\": \"T0-T8 from original run (eval-argmin-only-spatial), T9 from r2 restart. Combined 10-task result.\"}, \"notes\": \"10-task complete. T9 (wooden_cabinet) = 10%. Overall 34% (34/100). T0-T8 from original run, T9 from r2 restart. Clean exit. bjb1-18228 cuda:0 now FREE.\"}, \"eval-vla-only-object\": {\"updated_at\": \"2026-05-15T04:47:47.959Z\", \"metrics\": {\"overall_sr\": 0.12, \"total_success\": 12, \"total_trials\": 100, \"per_task\": {\"alphabet_soup\": 0, \"cream_cheese\": 0.1, \"salad_dressing\": 0.2, \"bbq_sauce\": 0.2, \"ketchup\": 0, \"tomato_sauce\": 0.1, \"butter\": 0, \"milk\": 0.1, \"chocolate_pudding\": 0.2, \"orange_juice\": 0.3}}}, \"crm-train-v3-norm-scalar-unc\": {\"updated_at\": \"2026-05-14T22:05:42.608Z\", \"metrics\": {\"best_epoch\": 46, \"best_val_loss\": 0.037354, \"final_train_loss\": 0.053422, \"final_val_loss\": 0.03737}}, \"crm-train-v3-norm-obs-only\": {\"updated_at\": \"2026-05-14T22:05:28.289Z\", \"metrics\": {\"best_epoch\": 48, \"best_val_loss\": 0.01645, \"final_train_loss\": 0.025576, \"final_val_loss\": 0.01645, \"total_epochs\": 50}}, \"crm-train-v3-norm\": {\"updated_at\": \"2026-05-14T20:05:22.677Z\"}}, \"count\": 211, \"total\": 211, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.7248}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01X6HiBnSADAvYTw8JBEfE4W`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*seed43*\" -o -name \"*reconvla*seed43*argmin*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "4102acee-41d8-411b-9016-0071c334f991",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8HB7q4FkZBbk8G166JcpV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7738,
      "cache_read_input_tokens": 23961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7738
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

_source line 14 · 2026-05-20T04:55:54.764Z_

<details><summary>↩ Tool result · `toolu_01X6HiBnSADAvYTw8JBEfE4W`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "91522fff-a60c-4334-8df0-92963db0ad02",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0112uNfPM2Y5Y62s39EP6bJy`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*long*vla*seed48*\" -o -name \"*vla*long*seed48*\" -o -name \"*vla_only*long*seed48*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "875936ae-9cb4-4269-93f7-5fad3004291d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B8HB7q4FkZBbk8G166JcpV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7738,
      "cache_read_input_tokens": 23961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7738
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

_source line 16 · 2026-05-20T04:55:55.582Z_

<details><summary>↩ Tool result · `toolu_0112uNfPM2Y5Y62s39EP6bJy`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "0938c2ae-b824-4dee-8457-183d78fe252e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
The `-o` flag in `find` is being interpreted as a shell metacharacter issue. Let me fix the find commands and read the registry data in chunks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "ef9b4224-ac4f-4853-bb64-41f3a2bd1747",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AA8UouCqkp7QQuWzTvBByt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1103,
      "cache_read_input_tokens": 31699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1103
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

_source line 18_

The `-o` in find commands is being blocked. Let me fix the SSH commands and start reading the registry data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "05a9fb4d-7dfa-4807-b25a-8f7d8b4080b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AA8UouCqkp7QQuWzTvBByt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1103,
      "cache_read_input_tokens": 31699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1103
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

_source line 19_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Qab79FaDYo7eMyZyFUWYqy`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "4ba1a584-309f-4edf-beec-07da4976963d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AA8UouCqkp7QQuWzTvBByt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1103,
      "cache_read_input_tokens": 31699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1103
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

_source line 20 · 2026-05-20T04:56:03.015Z_

<details><summary>↩ Tool result · `toolu_01Qab79FaDYo7eMyZyFUWYqy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.94}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "932b71af-c3d3-4f14-aaa2-077cd3516952",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.94}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.94}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01MDeCRQp2qht76X2TLc5igV`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*long*seed48*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "461a6ef9-c7f7-4ffd-a201-5e719eb7128f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AA8UouCqkp7QQuWzTvBByt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1103,
      "cache_read_input_tokens": 31699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1103
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

_source line 22 · 2026-05-20T04:56:03.402Z_

<details><summary>↩ Tool result · `toolu_01MDeCRQp2qht76X2TLc5igV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "f78a5ccd-b34d-4edd-9c62-aec53087bab3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.34}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_012d1RfLYp9vCdzhus4E53dc`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "be3a2841-af1c-41d5-8f71-91d8b56dfe2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AA8UouCqkp7QQuWzTvBByt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1103,
      "cache_read_input_tokens": 31699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1103
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

_source line 24 · 2026-05-20T04:56:05.209Z_

<details><summary>↩ Tool result · reported error · `toolu_012d1RfLYp9vCdzhus4E53dc`</summary>

```text
File content (38393 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "889b8edc-63a7-431a-a56e-eeae5ea0912a",
  "tool_use_result": "Error: File content (38393 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
The registry data is large. Let me read it in chunks and also try the other servers for the suspicious data points.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "168324ac-5d0f-4b9e-8d6f-ab330770b86b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuvX5R7rDLpH8qnTvyxeX5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 32802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 835
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

_source line 26_

Let me read the registry data in chunks and try other servers for the suspicious files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "29630436-e07c-4189-b8f0-31a8a6e1a54e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuvX5R7rDLpH8qnTvyxeX5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 32802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 835
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

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_019Gp3xQzAfgKuR2wm1tViqv`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt",
  "limit": 150,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "04bfe935-7122-40b3-b35a-b15a1db761cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuvX5R7rDLpH8qnTvyxeX5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 32802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 835
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

_source line 28 · 2026-05-20T04:56:12.937Z_

<details><summary>↩ Tool result · reported error · `toolu_019Gp3xQzAfgKuR2wm1tViqv`</summary>

```text
File content (38393 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "1e06cb45-25c3-46d8-afde-d71dabb64fd6",
  "tool_use_result": "Error: File content (38393 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01848bUmgYNry9GK6qDbWqxZ`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "1cbbe804-3b6f-4a70-8a0c-9d2752854743",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuvX5R7rDLpH8qnTvyxeX5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 32802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 835
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

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TkUwgpmNwNT49hiU2Q6juV`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*long*seed48*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "eab352e6-50b2-477f-bf79-8f1a2d903466",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PuvX5R7rDLpH8qnTvyxeX5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 835,
      "cache_read_input_tokens": 32802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 835
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

_source line 31 · 2026-05-20T04:56:14.950Z_

<details><summary>↩ Tool result · `toolu_01848bUmgYNry9GK6qDbWqxZ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.85}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "2ccc15d6-08c2-45f4-929b-c22aeec82cec",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.85}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.85}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T04:56:15.367Z_

<details><summary>↩ Tool result · `toolu_01TkUwgpmNwNT49hiU2Q6juV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "050cb22d-6010-4a99-ab0f-fa1326a2257a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
I found the files on bjb1-32546. Now let me read them and also use Bash to parse the registry JSON. Let me also search for the argmin K=10 seed43 on that server.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "0e7a1c91-3bd5-4fb8-b4ea-5663d75de22c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTGVgHSDEuWiJ2y5WiMiGp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 798,
      "cache_read_input_tokens": 33637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 798
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

_source line 34_

Found files on bjb1-32546. Let me read them and search for argmin K=10 seed43 specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "fb153489-1420-4af0-a99b-37b28227eb3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTGVgHSDEuWiJ2y5WiMiGp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 798,
      "cache_read_input_tokens": 33637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 798
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

_source line 35_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01B5nHPRbDN15kXfS4hivvgK`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "d8b15fe3-f93e-4d5a-aaaa-5e2c7e353f3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTGVgHSDEuWiJ2y5WiMiGp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 798,
      "cache_read_input_tokens": 33637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 798
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

_source line 36 · 2026-05-20T04:56:22.198Z_

<details><summary>↩ Tool result · `toolu_01B5nHPRbDN15kXfS4hivvgK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"reconvla\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.13,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "cf8f1cbd-ed90-4599-ac53-b44d3e056de5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"reconvla\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"object\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.13,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n      \\\\\\\"successes\\\\\\\": 3,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n      \\\\\\\"successes\\\\\\\": 3,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_butter_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n      \\\\\\\"successes\\\\\\\": 1,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_milk_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n      \\\\\\\"successes\\\\\\\": 1,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n      \\\\\\\"successes\\\\\\\": 3,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n      \\\\\\\"successes\\\\\\\": 2,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"reconvla\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"object\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.13,\\n  \\\"per_task\\\": {\\n    \\\"pick_up_the_alphabet_soup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_cream_cheese_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_salad_dressing_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_bbq_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_ketchup_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_tomato_sauce_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_butter_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_milk_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_chocolate_pudding_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    },\\n    \\\"pick_up_the_orange_juice_and_place_it_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01WnJz4ajBiUFipJM2k5DfM5`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "cat /root/acr-vla-conformal-refinement/logs/eval_long_obs_only_norm02_seed48.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "d3bf425e-a94f-46b4-95c5-87c416265866",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTGVgHSDEuWiJ2y5WiMiGp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 798,
      "cache_read_input_tokens": 33637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 798
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

_source line 38 · 2026-05-20T04:56:23.128Z_

<details><summary>↩ Tool result · `toolu_01WnJz4ajBiUFipJM2k5DfM5`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.15,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 8,\\n      \\\"total\\\": 10\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "1f4abe68-7679-4b9e-8f14-8fd80045c02c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"mode\\\\\\\": \\\\\\\"crm_obs_only\\\\\\\",\\\\n  \\\\\\\"baseline_mode\\\\\\\": \\\\\\\"single\\\\\\\",\\\\n  \\\\\\\"benchmark\\\\\\\": \\\\\\\"long\\\\\\\",\\\\n  \\\\\\\"n_rollouts\\\\\\\": 10,\\\\n  \\\\\\\"overall_success_rate\\\\\\\": 0.15,\\\\n  \\\\\\\"per_task\\\\\\\": {\\\\n    \\\\\\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.8,\\\\n      \\\\\\\"successes\\\\\\\": 8,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n      \\\\\\\"successes\\\\\\\": 1,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.2,\\\\n      \\\\\\\"successes\\\\\\\": 2,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.1,\\\\n      \\\\\\\"successes\\\\\\\": 1,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.0,\\\\n      \\\\\\\"successes\\\\\\\": 0,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    },\\\\n    \\\\\\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\\\\\": {\\\\n      \\\\\\\"success_rate\\\\\\\": 0.3,\\\\n      \\\\\\\"successes\\\\\\\": 3,\\\\n      \\\\\\\"total\\\\\\\": 10\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mode\\\": \\\"crm_obs_only\\\",\\n  \\\"baseline_mode\\\": \\\"single\\\",\\n  \\\"benchmark\\\": \\\"long\\\",\\n  \\\"n_rollouts\\\": 10,\\n  \\\"overall_success_rate\\\": 0.15,\\n  \\\"per_task\\\": {\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_alphabet_soup_and_the_tomato_sauce_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"LIVING_ROOM_SCENE2_put_both_the_cream_cheese_box_and_the_butter_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"KITCHEN_SCENE3_turn_on_the_stove_and_put_the_moka_pot_on_it\\\": {\\n      \\\"success_rate\\\": 0.8,\\n      \\\"successes\\\": 8,\\n      \\\"total\\\": 10\\n    },\\n    \\\"KITCHEN_SCENE4_put_the_black_bowl_in_the_bottom_drawer_of_the_cabinet_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"LIVING_ROOM_SCENE5_put_the_white_mug_on_the_left_plate_and_put_the_yellow_and_white_mug_on_the_right_plate\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"STUDY_SCENE1_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy\\\": {\\n      \\\"success_rate\\\": 0.2,\\n      \\\"successes\\\": 2,\\n      \\\"total\\\": 10\\n    },\\n    \\\"LIVING_ROOM_SCENE6_put_the_white_mug_on_the_plate_and_put_the_chocolate_pudding_to_the_right_of_the_plate\\\": {\\n      \\\"success_rate\\\": 0.1,\\n      \\\"successes\\\": 1,\\n      \\\"total\\\": 10\\n    },\\n    \\\"LIVING_ROOM_SCENE1_put_both_the_alphabet_soup_and_the_cream_cheese_box_in_the_basket\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"KITCHEN_SCENE8_put_both_moka_pots_on_the_stove\\\": {\\n      \\\"success_rate\\\": 0.0,\\n      \\\"successes\\\": 0,\\n      \\\"total\\\": 10\\n    },\\n    \\\"KITCHEN_SCENE6_put_the_yellow_and_white_mug_in_the_microwave_and_close_it\\\": {\\n      \\\"success_rate\\\": 0.3,\\n      \\\"successes\\\": 3,\\n      \\\"total\\\": 10\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_012eT9A6QFtq9HCitLJ5DUCV`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*k10*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "e1f36ada-0d4a-4ba6-86da-6d50205f3ae7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTGVgHSDEuWiJ2y5WiMiGp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 798,
      "cache_read_input_tokens": 33637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 798
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

_source line 40 · 2026-05-20T04:56:24.080Z_

<details><summary>↩ Tool result · `toolu_012eT9A6QFtq9HCitLJ5DUCV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "e98da814-3f1f-490e-903f-08a63bc9d128",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_01BqVEee9TTUb4qtVRtZwvZe`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\ndata = json.load(sys.stdin)\nexps = json.loads(data['result'])\n\n# Group by benchmark and method\ngroups = {}\nfor exp in exps:\n    bench = exp.get('benchmark', 'unknown')\n    method = exp.get('method', 'unknown')\n    seed = exp.get('seed', '?')\n    metrics = exp.get('metrics', {})\n    sr = metrics.get('success_rate', metrics.get('overall_success_rate', metrics.get('overall_sr', '?')))\n    config = exp.get('config', {})\n    exp_id = exp.get('experiment_id', '?')\n    updated = exp.get('updated_at', '?')\n    notes = exp.get('notes', '')\n    \n    key = f'{bench}|{method}'\n    if key not in groups:\n        groups[key] = []\n    groups[key].append({\n        'seed': seed, 'sr': sr, 'config': config, \n        'exp_id': exp_id, 'updated': updated, 'notes': notes\n    })\n\n# Print grouped\nfor key in sorted(groups.keys()):\n    bench, method = key.split('|')\n    entries = groups[key]\n    # Sort by seed\n    entries.sort(key=lambda x: str(x['seed']))\n    print(f'\\n=== {bench} | {method} ({len(entries)} exps) ===')\n    for e in entries:\n        config_str = ''\n        if e['config']:\n            norm = e['config'].get('norm_eps', e['config'].get('epsilon', ''))\n            k = e['config'].get('K', e['config'].get('k', ''))\n            p = e['config'].get('percentile', '')\n            if norm: config_str += f' eps={norm}'\n            if k: config_str += f' K={k}'\n            if p: config_str += f' p={p}'\n        print(f'  seed={e[\\\"seed\\\"]} SR={e[\\\"sr\\\"]}{config_str} | {e[\\\"exp_id\\\"]} | {e[\\\"updated\\\"][:10] if e[\\\"updated\\\"] != \\\"?\\\" else \\\"?\\\"} | {e[\\\"notes\\\"][:50] if e[\\\"notes\\\"] else \\\"\\\"}')\n\" 2>&1 | head -300",
  "description": "Parse registry JSON to extract all experiments grouped by benchmark/method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "47ccdaf7-53cc-4c03-98c5-835c72de1333",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTGVgHSDEuWiJ2y5WiMiGp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 798,
      "cache_read_input_tokens": 33637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 798
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

_source line 42 · 2026-05-20T04:56:32.731Z_

<details><summary>↩ Tool result · `toolu_01BqVEee9TTUb4qtVRtZwvZe`</summary>

```text
Traceback (most recent call last):
  File "&lt;string>", line 10, in &lt;module>
    bench = exp.get('benchmark', 'unknown')
            ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "611f5f93-b803-4acc-ae97-c0a3a10d9c64",
  "tool_use_result": {
    "stdout": "Traceback (most recent call last):\n  File \"&lt;string>\", line 10, in &lt;module>\n    bench = exp.get('benchmark', 'unknown')\n            ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'",
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

<details><summary>Logged reasoning block</summary>

```text
The registry result is a JSON string that needs to be parsed differently. Let me also check that the argmin K=10 seed43 doesn't exist on bjb1-32546 (only K=5 found). The long seed48 file on bjb1-32546 is a CRM file, not VLA-only. Let me also search on the other servers.

Key findings so far:
1. Argmin K=5 seed43 on bjb1-32546: SR=0.13, mode=reconvla, benchmark=object — this is argmin K=5, not K=10
2. Long seed48 on bjb1-32546: mode=crm_obs_only, SR=0.15, benchmark=long — this is CRM, not VLA-only


Now I need to refine my search approach and check the remaining servers for these configurations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "07d49267-b622-4661-8d7e-3aef06356d4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vyq7pT64vcWh3W9DVnkHGa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3516,
      "cache_read_input_tokens": 34435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3516
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

_source line 44_

The argmin seed43 file on bjb1-32546 is K=5 (SR=0.13), not K=10. The long seed48 file is CRM (SR=0.15), not VLA-only. Let me fix the JSON parsing and search more servers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "980240de-bd24-4838-b857-a826f310c695",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vyq7pT64vcWh3W9DVnkHGa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3516,
      "cache_read_input_tokens": 34435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3516
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

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_01Nkvt9zdQSGkjzukrfcg4SW`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\ndata = json.load(sys.stdin)\nresult_str = data['result']\nexps = json.loads(result_str)\n\n# Check if exps is a list of dicts or list of strings\nif isinstance(exps, list) and len(exps) > 0:\n    if isinstance(exps[0], str):\n        exps = [json.loads(e) for e in exps]\n    print(f'Total experiments: {len(exps)}')\n    print(f'Type of first: {type(exps[0])}')\n    if isinstance(exps[0], dict):\n        print(f'Keys: {list(exps[0].keys())[:10]}')\n        # Print first entry\n        print(json.dumps(exps[0], indent=2)[:500])\nelif isinstance(exps, dict):\n    print(f'Dict with keys: {list(exps.keys())[:10]}')\n    # Maybe it's experiment_id -> experiment_data\n    first_key = list(exps.keys())[0]\n    print(f'First key: {first_key}')\n    print(json.dumps(exps[first_key], indent=2)[:500])\n\" 2>&1",
  "description": "Inspect registry JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "fcffe187-a70d-48a3-b0ef-30042dd6d3c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vyq7pT64vcWh3W9DVnkHGa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3516,
      "cache_read_input_tokens": 34435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3516
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

_source line 46 · 2026-05-20T04:56:55.440Z_

<details><summary>↩ Tool result · `toolu_01Nkvt9zdQSGkjzukrfcg4SW`</summary>

```text
Dict with keys: ['success', 'data', 'error', 'metadata']
First key: success
true
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "0556a8e9-0ed0-4862-826b-f4f1df339746",
  "tool_use_result": {
    "stdout": "Dict with keys: ['success', 'data', 'error', 'metadata']\nFirst key: success\ntrue",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0196yg4bncPx2eGm1orTHfaQ`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "c81bb468-edc1-4374-a671-a16aca17a915",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vyq7pT64vcWh3W9DVnkHGa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3516,
      "cache_read_input_tokens": 34435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3516
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

_source line 48_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013wqpaA4dMR8RrNdHCE7eFH`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*long*seed48*vla*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "bf5af3e5-b6ae-4003-aaf0-2683ab966f1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vyq7pT64vcWh3W9DVnkHGa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3516,
      "cache_read_input_tokens": 34435,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3516
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

_source line 49 · 2026-05-20T04:56:56.410Z_

<details><summary>↩ Tool result · `toolu_0196yg4bncPx2eGm1orTHfaQ`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.79}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "5cb89c8b-3657-4b61-802b-a7f108b768b8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.79}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.79}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T04:56:56.828Z_

<details><summary>↩ Tool result · `toolu_013wqpaA4dMR8RrNdHCE7eFH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "1e64dfb6-ca85-4459-83de-41729b51ac18",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
The registry result is nested: `{success, data, error, metadata}` where `data` contains the actual experiments. Let me parse it properly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "ddcdcbb5-34ee-41e9-8e6a-c654ceba9216",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J416zULMyds3AAKzDxJJuK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1336,
      "cache_read_input_tokens": 37951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1336
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

<details open><summary>🔧 Tool call — Bash · `toolu_01KQH2AtG4kDvT5bbaBExEZb`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\nraw = json.load(sys.stdin)\nresult_str = raw['result']\nparsed = json.loads(result_str)\ndata = parsed.get('data', parsed)\n\nif isinstance(data, dict) and 'experiments' in data:\n    exps = data['experiments']\nelif isinstance(data, list):\n    exps = data\nelif isinstance(data, dict):\n    # Try to find the experiments\n    print('data keys:', list(data.keys())[:20])\n    # Maybe data itself is {exp_id: exp_data}\n    first_key = list(data.keys())[0]\n    first_val = data[first_key]\n    print(f'first key type: {type(first_key)}, val type: {type(first_val)}')\n    if isinstance(first_val, dict):\n        print(json.dumps(first_val, indent=2)[:800])\n    else:\n        print(str(first_val)[:500])\n    sys.exit(0)\nelse:\n    print(f'Unexpected type: {type(data)}')\n    sys.exit(1)\n\nprint(f'Total experiments: {len(exps)}')\n\" 2>&1",
  "description": "Parse registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "c9faaf24-c8f8-4459-86bc-c8a66dcdf1d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J416zULMyds3AAKzDxJJuK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1336,
      "cache_read_input_tokens": 37951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1336
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

_source line 53 · 2026-05-20T04:57:05.222Z_

<details><summary>↩ Tool result · `toolu_01KQH2AtG4kDvT5bbaBExEZb`</summary>

```text
Total experiments: 211
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "c1e7bd3b-9d2a-4c36-8a77-795605a901b2",
  "tool_use_result": {
    "stdout": "Total experiments: 211",
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

_source line 54_

<details open><summary>🔧 Tool call — Bash · `toolu_01Sz1kkvJuF2uE9Dtzyk1C77`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\nraw = json.load(sys.stdin)\nparsed = json.loads(raw['result'])\nexps = parsed.get('data', parsed) if isinstance(parsed, dict) else parsed\n\n# Group by benchmark+method, extract SR\ngroups = {}\nfor exp in exps:\n    bench = exp.get('benchmark', 'unknown')\n    method = exp.get('method', 'unknown')\n    seed = exp.get('seed', '?')\n    metrics = exp.get('metrics', {})\n    if isinstance(metrics, str):\n        metrics = json.loads(metrics)\n    sr = metrics.get('success_rate', metrics.get('overall_success_rate', metrics.get('overall_sr', '?')))\n    config = exp.get('config', {})\n    if isinstance(config, str):\n        config = json.loads(config)\n    exp_id = exp.get('experiment_id', '?')\n    updated = exp.get('updated_at', '?')\n    notes = str(exp.get('notes', '') or '')\n    \n    key = f'{bench}|{method}'\n    if key not in groups:\n        groups[key] = []\n    groups[key].append({\n        'seed': seed, 'sr': sr, 'config': config, \n        'exp_id': exp_id, 'updated': str(updated)[:10], 'notes': notes[:60]\n    })\n\nfor key in sorted(groups.keys()):\n    bench, method = key.split('|', 1)\n    entries = groups[key]\n    entries.sort(key=lambda x: (str(x['seed']), x['updated']))\n    print(f'\\n=== {bench} | {method} ({len(entries)} exps) ===')\n    for e in entries:\n        config_str = ''\n        if e['config'] and isinstance(e['config'], dict):\n            for ck in ['norm_eps', 'epsilon', 'K', 'k', 'percentile', 'mode']:\n                if ck in e['config']:\n                    config_str += f' {ck}={e[\\\"config\\\"][ck]}'\n        print(f'  seed={e[\\\"seed\\\"]} SR={e[\\\"sr\\\"]}{config_str} | {e[\\\"exp_id\\\"]} | {e[\\\"updated\\\"]} | {e[\\\"notes\\\"]}')\n\" 2>&1",
  "description": "Parse and group all registry experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "fc140428-1c00-4870-b620-51474c0302c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BxVUE1RnC2GHJqqQR2MieP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 528,
      "cache_read_input_tokens": 39287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 528
      },
      "output_tokens": 73,
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

_source line 55 · 2026-05-20T04:57:17.439Z_

<details><summary>↩ Tool result · reported error · `toolu_01Sz1kkvJuF2uE9Dtzyk1C77`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 11, in &lt;module>
    bench = exp.get('benchmark', 'unknown')
            ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "d05c9177-3482-4065-8288-b27fd87dfa5c",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 11, in &lt;module>\n    bench = exp.get('benchmark', 'unknown')\n            ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'"
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Bash · `toolu_01Y8N9sLULXSoS53MXgKVpU7`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\nraw = json.load(sys.stdin)\nparsed = json.loads(raw['result'])\ndata = parsed.get('data', parsed) if isinstance(parsed, dict) else parsed\n\nif isinstance(data, list):\n    print(f'List of {len(data)} items')\n    print(f'First item type: {type(data[0])}')\n    if isinstance(data[0], str):\n        first = json.loads(data[0])\n        print(json.dumps(first, indent=2)[:600])\n    else:\n        print(json.dumps(data[0], indent=2)[:600])\n\" 2>&1",
  "description": "Check individual experiment structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "2b1bcd75-873e-4103-81da-6e294036a2de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QWwdhtcWAL1XiWeRprr7EJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 39815,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 860
      },
      "output_tokens": 73,
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

_source line 57 · 2026-05-20T04:57:22.488Z_

<details><summary>↩ Tool result · `toolu_01Y8N9sLULXSoS53MXgKVpU7`</summary>

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
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "47d92f59-736f-4bb9-8577-583bf209c66b",
  "tool_use_result": {
    "stdout": "",
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

_source line 58_

<details open><summary>🔧 Tool call — Bash · `toolu_01PTjTs1rmoXEHhRLUx23i3k`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\nraw = json.load(sys.stdin)\nresult_str = raw['result']\nparsed = json.loads(result_str)\n\n# Navigate to the actual data\nif isinstance(parsed, dict):\n    if 'data' in parsed:\n        data = parsed['data']\n    else:\n        data = parsed\nelse:\n    data = parsed\n\nprint(f'type(data)={type(data).__name__}')\nif isinstance(data, list):\n    print(f'len={len(data)}')\n    for i, item in enumerate(data[:3]):\n        print(f'  [{i}] type={type(item).__name__}')\n        if isinstance(item, str):\n            sub = json.loads(item) if item.startswith('{') else item\n            print(f'       parsed type={type(sub).__name__}')\n            if isinstance(sub, dict):\n                print(f'       keys={list(sub.keys())[:8]}')\n        elif isinstance(item, dict):\n            print(f'       keys={list(item.keys())[:8]}')\nelif isinstance(data, dict):\n    print(f'keys={list(data.keys())[:15]}')\n    for k in list(data.keys())[:3]:\n        v = data[k]\n        print(f'  {k}: type={type(v).__name__}, val={str(v)[:100]}')\n\" 2>&1",
  "description": "Debug registry data structure at data level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "6b5355fa-c829-4f51-a534-5852c4e30cd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tjF6apLLSZ7AimiTWEq1z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 347,
      "cache_read_input_tokens": 40675,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 347
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

_source line 59 · 2026-05-20T04:57:29.716Z_

<details><summary>↩ Tool result · `toolu_01PTjTs1rmoXEHhRLUx23i3k`</summary>

```text
type(data)=dict
keys=['experiments', 'count', 'total', 'baseline']
  experiments: type=dict, val={'eval-vla-only-spatial-seed50': {'updated_at': '2026-05-20T04:13:56.340Z', 'metrics': {'success_rat
  count: type=int, val=211
  total: type=int, val=211
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "c1abbfaf-285b-407c-808b-ce927c025f78",
  "tool_use_result": {
    "stdout": "type(data)=dict\nkeys=['experiments', 'count', 'total', 'baseline']\n  experiments: type=dict, val={'eval-vla-only-spatial-seed50': {'updated_at': '2026-05-20T04:13:56.340Z', 'metrics': {'success_rat\n  count: type=int, val=211\n  total: type=int, val=211",
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

_source line 60_

<details open><summary>🔧 Tool call — Bash · `toolu_01DcrxXGs5rbyo8gsDHmWYNK`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/2c831810-b162-4fab-9231-54578fcd9e23/tool-results/mcp-agent-ml-research-read_registry-1779252954586.txt | python3 -c \"\nimport json, sys\n\nraw = json.load(sys.stdin)\nparsed = json.loads(raw['result'])\nexps_dict = parsed['data']['experiments']\n\n# Group by benchmark+method\ngroups = {}\nfor exp_id, exp in exps_dict.items():\n    bench = exp.get('benchmark', 'unknown')\n    method = exp.get('method', 'unknown')\n    seed = exp.get('seed', '?')\n    metrics = exp.get('metrics', {})\n    if isinstance(metrics, str):\n        metrics = json.loads(metrics)\n    sr = metrics.get('success_rate', metrics.get('overall_success_rate', metrics.get('overall_sr', '?')))\n    config = exp.get('config', {})\n    if isinstance(config, str):\n        config = json.loads(config)\n    updated = str(exp.get('updated_at', '?'))[:10]\n    notes = str(exp.get('notes', '') or '')[:60]\n    \n    key = f'{bench}|{method}'\n    if key not in groups:\n        groups[key] = []\n    groups[key].append({\n        'seed': seed, 'sr': sr, 'config': config, \n        'exp_id': exp_id, 'updated': updated, 'notes': notes\n    })\n\nfor key in sorted(groups.keys()):\n    bench, method = key.split('|', 1)\n    entries = groups[key]\n    entries.sort(key=lambda x: (str(x['seed']), x['updated']))\n    print(f'\\n=== {bench} | {method} ({len(entries)} exps) ===')\n    for e in entries:\n        config_str = ''\n        if e['config'] and isinstance(e['config'], dict):\n            for ck in ['norm_eps', 'epsilon', 'K', 'k', 'percentile', 'mode', 'norm']:\n                if ck in e['config']:\n                    config_str += f' {ck}={e[\\\"config\\\"][ck]}'\n        print(f'  seed={e[\\\"seed\\\"]} SR={e[\\\"sr\\\"]}{config_str} | {e[\\\"exp_id\\\"]} | {e[\\\"updated\\\"]} | {e[\\\"notes\\\"]}')\n\" 2>&1",
  "description": "Parse registry experiments grouped by benchmark/method",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "897ef8ee-bebd-403d-abb2-2832e89c9da8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QFKr2NUKv1BNN2RS957BmB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 628,
      "cache_read_input_tokens": 41022,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 628
      },
      "output_tokens": 73,
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

_source line 61 · 2026-05-20T04:57:40.767Z_

<details><summary>↩ Tool result · `toolu_01DcrxXGs5rbyo8gsDHmWYNK`</summary>

```text
=== unknown | unknown (211 exps) ===
  seed=? SR=? | crm-train-v3-norm-scalar-unc | 2026-05-14 | 
  seed=? SR=? | crm-train-v3-norm-obs-only | 2026-05-14 | 
  seed=? SR=? | crm-train-v3-norm | 2026-05-14 | 
  seed=? SR=? | eval-mag-obsonly-norm03-r2 | 2026-05-15 | 
  seed=? SR=12 | eval-vla-mean-object | 2026-05-15 | 
  seed=? SR=0.12 | eval-reconvla-object | 2026-05-15 | 
  seed=? SR=19.0% (19/100) | eval-acr-object-v4-obs-only | 2026-05-15 | 
  seed=? SR=11.0% (11/100) | eval-acr-object-v4-perdof | 2026-05-15 | 
  seed=? SR=32.0% (32/100) | eval-acr-spatial-v4-scalar-r2 | 2026-05-15 | 
  seed=? SR=35.0% (35/100) | eval-acr-spatial-v4-obs-only-r3 | 2026-05-15 | 
  seed=? SR=35.0% (35/100) | eval-acr-spatial-v4-small-r2 | 2026-05-15 | [D027] Framing 暂不裁决。Scenario A/B/C 取决于 magnitude sweep + obj
  seed=? SR=0.34 | eval-argmin-only-spatial-r2 | 2026-05-15 | 10-task complete. T9 (wooden_cabinet) = 10%. Overall 34% (34
  seed=? SR=0.12 | eval-vla-only-object | 2026-05-15 | 
  seed=? SR=0.16 | eval-obs-only-object-norm02-seed45 | 2026-05-16 | 
  seed=? SR=0.18 | eval-obs-only-object-norm03-seed44 | 2026-05-16 | 
  seed=? SR=0.1 | eval-vla-mean-object-seed44 | 2026-05-16 | 
  seed=? SR=0.13 | eval-argmin-object-seed44-r2 | 2026-05-16 | 
  seed=? SR=0.16 | eval-obs-only-object-norm02-seed44-r2 | 2026-05-16 | 
  seed=? SR=0 | eval-acr-object-v4-default-r2 | 2026-05-16 | 
  seed=? SR=0.14 | eval-mag-perdof-norm003-object | 2026-05-16 | 
  seed=? SR=0.16 | eval-obs-only-object-norm02-seed43-r2 | 2026-05-16 | 
  seed=? SR=0.1 | eval-vla-only-object-seed44-r2 | 2026-05-16 | 
  seed=? SR=0.17 | eval-acr-object-obs-only-default | 2026-05-16 | 
  seed=? SR=? | eval-scalar-object-seed43 | 2026-05-16 | 
  seed=? SR=0.16 | eval-mag-obsonly-norm003-object | 2026-05-16 | 
  seed=? SR=0.15 | eval-vla-mean-object-seed43 | 2026-05-16 | 
  seed=? SR=0.12 | eval-perdof-object-seed43 | 2026-05-16 | 
  seed=? SR=0.17 | eval-argmin-object-seed43 | 2026-05-16 | 
  seed=? SR=0.09 | eval-perdof-object-norm02-seed43-r3 | 2026-05-17 | 
  seed=? SR=0.14 | eval-perdof-object-norm01-seed47-bjb1 | 2026-05-17 | 
  seed=? SR=0.69 | eval-openvla-object-vla-only-seed42-v2 | 2026-05-17 | 
  seed=? SR=0.1 | eval-perdof-object-norm01-seed46-r2 | 2026-05-17 | 
  seed=? SR=? | plan_602-latency-profile | 2026-05-17 | 
  seed=? SR=? | train-crm-k1-accg-object-seed42-v2 | 2026-05-17 | Retry after W&B API key crash. Added --no_wandb. Precompute 
  seed=? SR=0.12 | eval-obs-only-object-default-seed45 | 2026-05-17 | 
  seed=? SR=0.09 | eval-scalar-object-seed45 | 2026-05-17 | 
  seed=? SR=0.09 | eval-perdof-object-norm02-seed45 | 2026-05-17 | perdof ε=0.2 seed45: 9% (18/200). Cross-seed: seed42=11%, se
  seed=? SR=0.1 | eval-perdof-object-norm02-seed44 | 2026-05-17 | 
  seed=? SR=? | train-crm-k1-accg-object-seed42-fallback | 2026-05-17 | 
  seed=? SR=0.2 | eval-obs-only-object-norm02-seed47 | 2026-05-17 | 
  seed=? SR=0.15 | eval-obs-only-object-norm02-seed46 | 2026-05-17 | 
  seed=? SR=0.1 | eval-argmin-object-seed47 | 2026-05-17 | 
  seed=? SR=0.11 | eval-perdof-object-norm01-seed45 | 2026-05-17 | 
  seed=? SR=0.1 | eval-argmin-object-seed46 | 2026-05-17 | 
  seed=? SR=14 | eval-obs-only-object-norm03-seed45-r2 | 2026-05-17 | 
  seed=? SR=0.13 | eval-vla-mean-object-seed45 | 2026-05-17 | 
  seed=? SR=0.12 | eval-argmin-object-seed45 | 2026-05-17 | 
  seed=? SR=0.14 | eval-direct-correction-object-seed42-r3 | 2026-05-17 | 
  seed=? SR=? | eval-vla-mean-spatial | 2026-05-17 | 
  seed=? SR=0.22 | eval-acr-object-obs-only-norm02 | 2026-05-17 | 
  seed=? SR=0.3 | eval-spatial-v7-full | 2026-05-17 | 
  seed=? SR=0.13 | eval-object-v8-full | 2026-05-17 | 
  seed=? SR=? | precompute-v5-shard2 | 2026-05-17 | 
  seed=? SR=? | precompute-v5-shard1 | 2026-05-17 | 
  seed=? SR=? | precompute-v5-shard0 | 2026-05-17 | 
  seed=? SR=? | precompute-v4-shard2 | 2026-05-17 | 
  seed=? SR=? | precompute-v4-shard1 | 2026-05-17 | 
  seed=? SR=? | precompute-v4-shard0 | 2026-05-17 | 
  seed=? SR=0.16 | eval-obs-only-object-norm01-seed44 | 2026-05-17 | 
  seed=? SR=0.09 | eval-vla-only-object-seed45 | 2026-05-17 | 
  seed=? SR=0.12 | eval-vla-only-object-seed43 | 2026-05-17 | seed=43 VLA-only 12% = seed=42 12%，baseline 跨 seed 完全一致。per-
  seed=? SR=? | eval-vla-mean-spatial-t10 | 2026-05-17 | 
  seed=? SR=0.34 | eval-reconvla-spatial-v3 | 2026-05-17 | 
  seed=? SR=? | crm-train-v2-scalar-unc | 2026-05-17 | 
  seed=? SR=? | crm-train-v2-perdof | 2026-05-17 | 
  seed=? SR=? | crm-train-v2-obs-only | 2026-05-17 | 
  seed=? SR=? | precompute-shard2 | 2026-05-17 | 
  seed=? SR=? | precompute-shard1 | 2026-05-17 | 
  seed=? SR=? | precompute-shard0 | 2026-05-17 | 
  seed=? SR=? | precompute-k5 | 2026-05-17 | 
  seed=? SR=? | mvp-point-reaching | 2026-05-17 | 
  seed=? SR=0.16 | eval-obs-only-object-default-seed44 | 2026-05-17 | 
  seed=? SR=0.14 | eval-mag-perdof-norm005-object | 2026-05-17 | 
  seed=? SR=0.09 | eval-mag-perdof-norm02-seed43-object-r3 | 2026-05-17 | 
  seed=? SR=0.04 | eval-mag-perdof-norm03-object-r3 | 2026-05-17 | 
  seed=? SR=35 | eval-mag-obsonly-norm005 | 2026-05-17 | 
  seed=? SR=? | eval-mag-obsonly-norm003-b2 | 2026-05-17 | Ghost PID 211962 killed, b2 now running solo on bjb2-40593 c
  seed=? SR=0.19 | eval-mag-obsonly-norm03-object | 2026-05-17 | 
  seed=? SR=0.13 | eval-mag-obsonly-norm005-object | 2026-05-17 | 
  seed=? SR=0.17 | eval-obs-only-object-norm02-k5-seed44 | 2026-05-18 | 
  seed=? SR=0.13 | eval-random-selection-object-seed44 | 2026-05-18 | 
  seed=? SR=0.11 | eval-perdof-object-norm01-seed42 | 2026-05-18 | 
  seed=? SR=0.19 | eval-obs-only-object-norm01-seed42 | 2026-05-18 | 
  seed=? SR=0.18 | eval-obs-only-object-norm01-seed46-r3 | 2026-05-18 | 
  seed=? SR=0.14 | eval-obs-only-object-norm005-seed45 | 2026-05-18 | 
  seed=? SR=0.09 | eval-random-selection-object-seed43 | 2026-05-18 | 
  seed=? SR=0.09 | eval-perdof-object-norm005-seed44 | 2026-05-18 | 
  seed=? SR=0.11 | eval-vla-only-object-seed45-r2 | 2026-05-18 | 
  seed=? SR=0.16 | eval-obs-only-object-norm03-seed48 | 2026-05-18 | 
  seed=? SR=0.16 | eval-obs-only-object-norm005-seed44 | 2026-05-18 | 
  seed=? SR=0.19 | eval-obs-only-object-norm02-k5-seed43 | 2026-05-18 | 
  seed=? SR=0.13 | eval-random-selection-object-seed42 | 2026-05-18 | 
  seed=? SR=0.09 | eval-perdof-object-norm02-seed43 | 2026-05-18 | 
  seed=? SR=0.14 | eval-obs-only-object-norm01-seed45 | 2026-05-18 | PID 474319 died, GPU idle 28h+. Ghost experiment — process d
  seed=? SR=0.14 | eval-obs-only-object-norm02-k5-seed42 | 2026-05-18 | 
  seed=? SR=0.025 | eval-acr-spatial-v3 | 2026-05-18 | 
  seed=? SR=0.11 | eval-perdof-object-norm02-seed47 | 2026-05-18 | 
  seed=? SR=0.15 | eval-obs-only-object-default-seed46 | 2026-05-18 | 
  seed=? SR=0.09 | eval-perdof-object-norm02-seed46 | 2026-05-18 | 
  seed=? SR=0.14 | eval-obs-only-object-norm005-seed43-r2 | 2026-05-18 | 
  seed=? SR=0.34 | eval-obs-only-spatial-norm02-seed43-r2 | 2026-05-19 | 
  seed=? SR=? | k2-l2-calibration-phase1 | 2026-05-19 | 
  seed=? SR=0.18 | eval-crm-long-seed45 | 2026-05-19 | 
  seed=? SR=0.69 | eval-vla-only-goal-seed43 | 2026-05-19 | 
  seed=? SR=0.71 | eval-vla-only-goal-seed42 | 2026-05-19 | 
  seed=? SR=0.1 | eval-vla-only-object-seed47 | 2026-05-19 | 
  seed=? SR=0.2 | eval-crm-long-seed44 | 2026-05-19 | 
  seed=? SR=0.15 | eval-crm-long-seed43 | 2026-05-19 | 
  seed=? SR=0.17 | eval-crm-long-seed42 | 2026-05-19 | 
  seed=? SR=0.67 | eval-crm-goal-seed42 | 2026-05-19 | 
  seed=? SR=0.72 | eval-crm-goal-seed43 | 2026-05-19 | 
  seed=? SR=0.3 | eval-vla-only-spatial-seed46 | 2026-05-19 | 
  seed=? SR=0.14 | eval-vla-only-long-seed47 | 2026-05-19 | Cron false positive: eval 脚本无 W&B/sentinel，进程正常退出被误判 failed。
  seed=? SR=0.63 | eval-vla-only-goal-seed45 | 2026-05-19 | 
  seed=? SR=0.71 | eval-vla-only-goal-seed46 | 2026-05-19 | Cron false positive: eval completed normally (71.0%), but no
  seed=? SR=0.18 | eval-vla-only-long-seed46 | 2026-05-19 | Cron false positive: eval completed normally (18.0%), but no
  seed=? SR=? | eval-obs-only-object-norm005-seed48 | 2026-05-19 | 
  seed=? SR=0.17 | eval-vla-only-long-seed45 | 2026-05-19 | 
  seed=? SR=0.15 | eval-perdof-object-norm003-seed47 | 2026-05-19 | 
  seed=? SR=0.1 | eval-perdof-object-norm005-seed47 | 2026-05-19 | 
  seed=? SR=0.12 | eval-vla-only-long-seed44 | 2026-05-19 | 
  seed=? SR=0.11 | eval-vla-only-long-seed42 | 2026-05-19 | 
  seed=? SR=0.13 | eval-vla-only-long-seed43 | 2026-05-19 | 
  seed=? SR=0.32 | eval-obs-only-spatial-norm02-seed47 | 2026-05-19 | 
  seed=? SR=0.07 | eval-random-selection-object-k5-seed45-r2 | 2026-05-19 | 
  seed=? SR=0.1 | eval-random-selection-object-k5-seed44-r2 | 2026-05-19 | 
  seed=? SR=0.11 | eval-random-selection-object-k5-seed43-r2 | 2026-05-19 | 
  seed=? SR=0.14 | eval-random-selection-object-k5-seed42-r2 | 2026-05-19 | 
  seed=? SR=0.37 | eval-obs-only-spatial-norm02-k5-seed44-r2 | 2026-05-19 | 
  seed=? SR=0.34 | eval-obs-only-spatial-norm02-k5-seed45-r2 | 2026-05-19 | 
  seed=? SR=? | plan_602-latency-profiling | 2026-05-19 | 
  seed=? SR=0.27 | eval-vla-only-spatial-seed45 | 2026-05-19 | 
  seed=? SR=0.1 | eval-perdof-object-norm005-seed45-r2 | 2026-05-19 | 
  seed=? SR=0.31 | eval-vla-only-spatial-seed44 | 2026-05-19 | 
  seed=? SR=0.17 | eval-obs-only-object-default-seed48-r2 | 2026-05-19 | 误判 failed: cron 检测到 tmux session 死亡，但实验已正常完成并写入完整 JSON。手动验证 
  seed=? SR=0.29 | eval-vla-only-spatial-seed43 | 2026-05-19 | 
  seed=? SR=0.3 | eval-vla-only-spatial-seed42 | 2026-05-19 | 
  seed=? SR=0.36 | eval-obs-only-spatial-norm02-seed44 | 2026-05-19 | 
  seed=? SR=0.15 | eval-obs-only-object-norm003-seed47-r2 | 2026-05-19 | 2026-05-19 12:58 UTC: FALSE ALARM — cron 检测到旧进程 EXIT_CODE=12
  seed=? SR=0.15 | eval-obs-only-object-norm003-seed48 | 2026-05-19 | 2026-05-19 12:58 UTC: FALSE ALARM 确认 — PID 67825 在 bjb1-1822
  seed=? SR=? | eval-perdof-object-norm01-seed43 | 2026-05-19 | 
  seed=? SR=? | eval-obs-only-object-default-seed45-r2 | 2026-05-19 | 
  seed=? SR=? | eval-argmin-object-k5-seed42 | 2026-05-19 | 
  seed=? SR=? | eval-argmin-object-k5-seed45 | 2026-05-19 | 
  seed=? SR=? | eval-argmin-object-k5-seed43 | 2026-05-19 | 
  seed=? SR=? | eval-perdof-object-norm03-seed43 | 2026-05-19 | 
  seed=? SR=0.34 | eval-obs-only-spatial-norm02-seed45 | 2026-05-19 | 
  seed=? SR=? | eval-obs-only-object-norm003-seed44-bjb2 | 2026-05-19 | 2026-05-19 21:00 UTC: 实验实际成功完成。JSON 输出在 /root/logs/eval_obje
  seed=? SR=? | train-crm-k1-accg-object-seed42-full | 2026-05-19 | 
  seed=? SR=? | plan_701-precompute-k1-spatial | 2026-05-19 | 
  seed=? SR=? | plan_701-crm-k1-train | 2026-05-19 | 
  seed=? SR=0.16 | eval_obs_only_norm03_seed48 | 2026-05-19 | 
  seed=? SR=0.18 | eval_obs_only_norm01_seed48 | 2026-05-19 | 
  seed=? SR=0.14 | eval-lto-splitA-vla-only-r3 | 2026-05-19 | 
  seed=? SR=0.14 | eval-lto-splitA-vla-only-r2 | 2026-05-19 | 
  seed=? SR=? | crm-lto-splitA-train | 2026-05-19 | 
  seed=? SR=0.13 | eval-perdof-object-norm003-seed48 | 2026-05-19 | 
  seed=? SR=0.32 | eval-obs-only-spatial-norm02-k5-seed43 | 2026-05-19 | 
  seed=? SR=0.18 | eval-obs-only-object-norm02-k5-seed48 | 2026-05-19 | 
  seed=? SR=0.35 | eval-obs-only-spatial-norm02-k5-seed42 | 2026-05-19 | 
  seed=? SR=0.16 | eval-obs-only-object-norm02-k5-seed46 | 2026-05-19 | 
  seed=? SR=0.14 | eval-lto-splitA-vla-only-v2 | 2026-05-19 | 
  seed=? SR=0.05 | eval-perdof-object-norm03-seed47 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束
  seed=? SR=0.17 | eval-obs-only-object-default-seed48 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束
  seed=? SR=0.09 | eval-perdof-object-norm003-seed46 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束
  seed=? SR=0.11 | eval-perdof-object-norm005-seed46 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束
  seed=? SR=0.13 | eval-obs-only-object-norm02-k5-seed47 | 2026-05-19 | 
  seed=? SR=0.1 | eval-random-selection-object-seed45 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束
  seed=? SR=0.14 | eval-obs-only-object-norm005-seed47 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束
  seed=? SR=0.12 | eval-perdof-object-norm01-seed48 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束. JSON 位于 /root/logs/ 而非项目 logs/ 目录
  seed=? SR=0.16 | eval-obs-only-object-default-seed47 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束
  seed=? SR=0.04 | eval-perdof-object-norm03-seed46 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束
  seed=? SR=0.17 | eval-obs-only-object-norm03-seed46 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束
  seed=? SR=0.09 | eval-scalar-object-seed46 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束
  seed=? SR=0.17 | eval-obs-only-object-norm01-seed47 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束
  seed=? SR=0.17 | eval-obs-only-object-norm01-seed45-r2 | 2026-05-19 | 
  seed=? SR=? | crm-lto-splitA-train-fixed | 2026-05-19 | 
  seed=? SR=0.13 | eval-perdof-object-norm003-seed43 | 2026-05-19 | 
  seed=? SR=0.13 | eval-perdof-object-norm005-seed43 | 2026-05-19 | 
  seed=? SR=0 | eval-perdof-object-default-seed43 | 2026-05-19 | 
  seed=? SR=0.18 | eval-obs-only-object-norm02-seed48-r2 | 2026-05-19 | 
  seed=? SR=0 | eval-perdof-object-default-seed45 | 2026-05-19 | 
  seed=? SR=0.15 | eval-obs-only-object-norm02-k5-seed45 | 2026-05-19 | 
  seed=? SR=0.13 | eval-vla-only-object-seed46 | 2026-05-19 | 
  seed=? SR=0.18 | eval-obs-only-object-norm01-seed48 | 2026-05-19 | 
  seed=? SR=0.3 | eval-vla-only-spatial-seed50 | 2026-05-20 | 
  seed=? SR=0.35 | eval-crm-spatial-seed48 | 2026-05-20 | 
  seed=? SR=? | eval-argmin-object-k5-seed44-r2 | 2026-05-20 | 
  seed=? SR=? | eval-obs-only-spatial-norm02-seed46-r2 | 2026-05-20 | 
  seed=? SR=0.73 | eval-vla-only-goal-seed44-r2 | 2026-05-20 | 
  seed=? SR=0.13 | eval-adaptive-k-p25-seed43 | 2026-05-20 | 
  seed=? SR=0.16 | eval-adaptive-k-p50-seed43 | 2026-05-20 | 
  seed=? SR=0.35 | eval-obs-only-spatial-norm02-seed48 | 2026-05-20 | 
  seed=? SR=0.15 | eval-adaptive-k-p25-seed42 | 2026-05-20 | 
  seed=? SR=0.16 | eval-adaptive-k-p50-seed42 | 2026-05-20 | 
  seed=? SR=0.13 | eval-adaptive-k-p75-seed43 | 2026-05-20 | 
  seed=? SR=0.72 | eval-crm-goal-seed46 | 2026-05-20 | 
  seed=? SR=0.14 | eval-adaptive-k-p90-seed44 | 2026-05-20 | 
  seed=? SR=0.12 | eval-adaptive-k-p75-seed42 | 2026-05-20 | 
  seed=? SR=0.14 | eval-adaptive-k-p50-seed44 | 2026-05-20 | 
  seed=? SR=0.16 | eval-adaptive-k-p75-seed44 | 2026-05-20 | 
  seed=? SR=0.14 | eval-adaptive-k-p90-seed43 | 2026-05-20 | 
  seed=? SR=0.12 | eval-adaptive-k-p90-seed42 | 2026-05-20 | 
  seed=? SR=0.3 | eval-vla-only-spatial-seed47 | 2026-05-20 | 
  seed=? SR=0.17 | eval-crm-long-seed47 | 2026-05-20 | 
  seed=? SR=0.1 | eval-vla-only-object-seed48 | 2026-05-20 | 
  seed=? SR=0.14 | eval-vla-only-long-seed48 | 2026-05-20 | 
  seed=? SR=0.09 | eval-vla-only-object-seed50 | 2026-05-20 | 
  seed=? SR=0.18 | eval-crm-long-seed46 | 2026-05-20 | 
  seed=? SR=0.65 | eval-crm-goal-seed45-r2 | 2026-05-20 | 
  seed=? SR=0.64 | eval-crm-goal-seed44-r2 | 2026-05-20 |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "79aec064-aca2-48f4-be7d-8c17d382ed16",
  "tool_use_result": {
    "stdout": "=== unknown | unknown (211 exps) ===\n  seed=? SR=? | crm-train-v3-norm-scalar-unc | 2026-05-14 | \n  seed=? SR=? | crm-train-v3-norm-obs-only | 2026-05-14 | \n  seed=? SR=? | crm-train-v3-norm | 2026-05-14 | \n  seed=? SR=? | eval-mag-obsonly-norm03-r2 | 2026-05-15 | \n  seed=? SR=12 | eval-vla-mean-object | 2026-05-15 | \n  seed=? SR=0.12 | eval-reconvla-object | 2026-05-15 | \n  seed=? SR=19.0% (19/100) | eval-acr-object-v4-obs-only | 2026-05-15 | \n  seed=? SR=11.0% (11/100) | eval-acr-object-v4-perdof | 2026-05-15 | \n  seed=? SR=32.0% (32/100) | eval-acr-spatial-v4-scalar-r2 | 2026-05-15 | \n  seed=? SR=35.0% (35/100) | eval-acr-spatial-v4-obs-only-r3 | 2026-05-15 | \n  seed=? SR=35.0% (35/100) | eval-acr-spatial-v4-small-r2 | 2026-05-15 | [D027] Framing 暂不裁决。Scenario A/B/C 取决于 magnitude sweep + obj\n  seed=? SR=0.34 | eval-argmin-only-spatial-r2 | 2026-05-15 | 10-task complete. T9 (wooden_cabinet) = 10%. Overall 34% (34\n  seed=? SR=0.12 | eval-vla-only-object | 2026-05-15 | \n  seed=? SR=0.16 | eval-obs-only-object-norm02-seed45 | 2026-05-16 | \n  seed=? SR=0.18 | eval-obs-only-object-norm03-seed44 | 2026-05-16 | \n  seed=? SR=0.1 | eval-vla-mean-object-seed44 | 2026-05-16 | \n  seed=? SR=0.13 | eval-argmin-object-seed44-r2 | 2026-05-16 | \n  seed=? SR=0.16 | eval-obs-only-object-norm02-seed44-r2 | 2026-05-16 | \n  seed=? SR=0 | eval-acr-object-v4-default-r2 | 2026-05-16 | \n  seed=? SR=0.14 | eval-mag-perdof-norm003-object | 2026-05-16 | \n  seed=? SR=0.16 | eval-obs-only-object-norm02-seed43-r2 | 2026-05-16 | \n  seed=? SR=0.1 | eval-vla-only-object-seed44-r2 | 2026-05-16 | \n  seed=? SR=0.17 | eval-acr-object-obs-only-default | 2026-05-16 | \n  seed=? SR=? | eval-scalar-object-seed43 | 2026-05-16 | \n  seed=? SR=0.16 | eval-mag-obsonly-norm003-object | 2026-05-16 | \n  seed=? SR=0.15 | eval-vla-mean-object-seed43 | 2026-05-16 | \n  seed=? SR=0.12 | eval-perdof-object-seed43 | 2026-05-16 | \n  seed=? SR=0.17 | eval-argmin-object-seed43 | 2026-05-16 | \n  seed=? SR=0.09 | eval-perdof-object-norm02-seed43-r3 | 2026-05-17 | \n  seed=? SR=0.14 | eval-perdof-object-norm01-seed47-bjb1 | 2026-05-17 | \n  seed=? SR=0.69 | eval-openvla-object-vla-only-seed42-v2 | 2026-05-17 | \n  seed=? SR=0.1 | eval-perdof-object-norm01-seed46-r2 | 2026-05-17 | \n  seed=? SR=? | plan_602-latency-profile | 2026-05-17 | \n  seed=? SR=? | train-crm-k1-accg-object-seed42-v2 | 2026-05-17 | Retry after W&B API key crash. Added --no_wandb. Precompute \n  seed=? SR=0.12 | eval-obs-only-object-default-seed45 | 2026-05-17 | \n  seed=? SR=0.09 | eval-scalar-object-seed45 | 2026-05-17 | \n  seed=? SR=0.09 | eval-perdof-object-norm02-seed45 | 2026-05-17 | perdof ε=0.2 seed45: 9% (18/200). Cross-seed: seed42=11%, se\n  seed=? SR=0.1 | eval-perdof-object-norm02-seed44 | 2026-05-17 | \n  seed=? SR=? | train-crm-k1-accg-object-seed42-fallback | 2026-05-17 | \n  seed=? SR=0.2 | eval-obs-only-object-norm02-seed47 | 2026-05-17 | \n  seed=? SR=0.15 | eval-obs-only-object-norm02-seed46 | 2026-05-17 | \n  seed=? SR=0.1 | eval-argmin-object-seed47 | 2026-05-17 | \n  seed=? SR=0.11 | eval-perdof-object-norm01-seed45 | 2026-05-17 | \n  seed=? SR=0.1 | eval-argmin-object-seed46 | 2026-05-17 | \n  seed=? SR=14 | eval-obs-only-object-norm03-seed45-r2 | 2026-05-17 | \n  seed=? SR=0.13 | eval-vla-mean-object-seed45 | 2026-05-17 | \n  seed=? SR=0.12 | eval-argmin-object-seed45 | 2026-05-17 | \n  seed=? SR=0.14 | eval-direct-correction-object-seed42-r3 | 2026-05-17 | \n  seed=? SR=? | eval-vla-mean-spatial | 2026-05-17 | \n  seed=? SR=0.22 | eval-acr-object-obs-only-norm02 | 2026-05-17 | \n  seed=? SR=0.3 | eval-spatial-v7-full | 2026-05-17 | \n  seed=? SR=0.13 | eval-object-v8-full | 2026-05-17 | \n  seed=? SR=? | precompute-v5-shard2 | 2026-05-17 | \n  seed=? SR=? | precompute-v5-shard1 | 2026-05-17 | \n  seed=? SR=? | precompute-v5-shard0 | 2026-05-17 | \n  seed=? SR=? | precompute-v4-shard2 | 2026-05-17 | \n  seed=? SR=? | precompute-v4-shard1 | 2026-05-17 | \n  seed=? SR=? | precompute-v4-shard0 | 2026-05-17 | \n  seed=? SR=0.16 | eval-obs-only-object-norm01-seed44 | 2026-05-17 | \n  seed=? SR=0.09 | eval-vla-only-object-seed45 | 2026-05-17 | \n  seed=? SR=0.12 | eval-vla-only-object-seed43 | 2026-05-17 | seed=43 VLA-only 12% = seed=42 12%，baseline 跨 seed 完全一致。per-\n  seed=? SR=? | eval-vla-mean-spatial-t10 | 2026-05-17 | \n  seed=? SR=0.34 | eval-reconvla-spatial-v3 | 2026-05-17 | \n  seed=? SR=? | crm-train-v2-scalar-unc | 2026-05-17 | \n  seed=? SR=? | crm-train-v2-perdof | 2026-05-17 | \n  seed=? SR=? | crm-train-v2-obs-only | 2026-05-17 | \n  seed=? SR=? | precompute-shard2 | 2026-05-17 | \n  seed=? SR=? | precompute-shard1 | 2026-05-17 | \n  seed=? SR=? | precompute-shard0 | 2026-05-17 | \n  seed=? SR=? | precompute-k5 | 2026-05-17 | \n  seed=? SR=? | mvp-point-reaching | 2026-05-17 | \n  seed=? SR=0.16 | eval-obs-only-object-default-seed44 | 2026-05-17 | \n  seed=? SR=0.14 | eval-mag-perdof-norm005-object | 2026-05-17 | \n  seed=? SR=0.09 | eval-mag-perdof-norm02-seed43-object-r3 | 2026-05-17 | \n  seed=? SR=0.04 | eval-mag-perdof-norm03-object-r3 | 2026-05-17 | \n  seed=? SR=35 | eval-mag-obsonly-norm005 | 2026-05-17 | \n  seed=? SR=? | eval-mag-obsonly-norm003-b2 | 2026-05-17 | Ghost PID 211962 killed, b2 now running solo on bjb2-40593 c\n  seed=? SR=0.19 | eval-mag-obsonly-norm03-object | 2026-05-17 | \n  seed=? SR=0.13 | eval-mag-obsonly-norm005-object | 2026-05-17 | \n  seed=? SR=0.17 | eval-obs-only-object-norm02-k5-seed44 | 2026-05-18 | \n  seed=? SR=0.13 | eval-random-selection-object-seed44 | 2026-05-18 | \n  seed=? SR=0.11 | eval-perdof-object-norm01-seed42 | 2026-05-18 | \n  seed=? SR=0.19 | eval-obs-only-object-norm01-seed42 | 2026-05-18 | \n  seed=? SR=0.18 | eval-obs-only-object-norm01-seed46-r3 | 2026-05-18 | \n  seed=? SR=0.14 | eval-obs-only-object-norm005-seed45 | 2026-05-18 | \n  seed=? SR=0.09 | eval-random-selection-object-seed43 | 2026-05-18 | \n  seed=? SR=0.09 | eval-perdof-object-norm005-seed44 | 2026-05-18 | \n  seed=? SR=0.11 | eval-vla-only-object-seed45-r2 | 2026-05-18 | \n  seed=? SR=0.16 | eval-obs-only-object-norm03-seed48 | 2026-05-18 | \n  seed=? SR=0.16 | eval-obs-only-object-norm005-seed44 | 2026-05-18 | \n  seed=? SR=0.19 | eval-obs-only-object-norm02-k5-seed43 | 2026-05-18 | \n  seed=? SR=0.13 | eval-random-selection-object-seed42 | 2026-05-18 | \n  seed=? SR=0.09 | eval-perdof-object-norm02-seed43 | 2026-05-18 | \n  seed=? SR=0.14 | eval-obs-only-object-norm01-seed45 | 2026-05-18 | PID 474319 died, GPU idle 28h+. Ghost experiment — process d\n  seed=? SR=0.14 | eval-obs-only-object-norm02-k5-seed42 | 2026-05-18 | \n  seed=? SR=0.025 | eval-acr-spatial-v3 | 2026-05-18 | \n  seed=? SR=0.11 | eval-perdof-object-norm02-seed47 | 2026-05-18 | \n  seed=? SR=0.15 | eval-obs-only-object-default-seed46 | 2026-05-18 | \n  seed=? SR=0.09 | eval-perdof-object-norm02-seed46 | 2026-05-18 | \n  seed=? SR=0.14 | eval-obs-only-object-norm005-seed43-r2 | 2026-05-18 | \n  seed=? SR=0.34 | eval-obs-only-spatial-norm02-seed43-r2 | 2026-05-19 | \n  seed=? SR=? | k2-l2-calibration-phase1 | 2026-05-19 | \n  seed=? SR=0.18 | eval-crm-long-seed45 | 2026-05-19 | \n  seed=? SR=0.69 | eval-vla-only-goal-seed43 | 2026-05-19 | \n  seed=? SR=0.71 | eval-vla-only-goal-seed42 | 2026-05-19 | \n  seed=? SR=0.1 | eval-vla-only-object-seed47 | 2026-05-19 | \n  seed=? SR=0.2 | eval-crm-long-seed44 | 2026-05-19 | \n  seed=? SR=0.15 | eval-crm-long-seed43 | 2026-05-19 | \n  seed=? SR=0.17 | eval-crm-long-seed42 | 2026-05-19 | \n  seed=? SR=0.67 | eval-crm-goal-seed42 | 2026-05-19 | \n  seed=? SR=0.72 | eval-crm-goal-seed43 | 2026-05-19 | \n  seed=? SR=0.3 | eval-vla-only-spatial-seed46 | 2026-05-19 | \n  seed=? SR=0.14 | eval-vla-only-long-seed47 | 2026-05-19 | Cron false positive: eval 脚本无 W&B/sentinel，进程正常退出被误判 failed。\n  seed=? SR=0.63 | eval-vla-only-goal-seed45 | 2026-05-19 | \n  seed=? SR=0.71 | eval-vla-only-goal-seed46 | 2026-05-19 | Cron false positive: eval completed normally (71.0%), but no\n  seed=? SR=0.18 | eval-vla-only-long-seed46 | 2026-05-19 | Cron false positive: eval completed normally (18.0%), but no\n  seed=? SR=? | eval-obs-only-object-norm005-seed48 | 2026-05-19 | \n  seed=? SR=0.17 | eval-vla-only-long-seed45 | 2026-05-19 | \n  seed=? SR=0.15 | eval-perdof-object-norm003-seed47 | 2026-05-19 | \n  seed=? SR=0.1 | eval-perdof-object-norm005-seed47 | 2026-05-19 | \n  seed=? SR=0.12 | eval-vla-only-long-seed44 | 2026-05-19 | \n  seed=? SR=0.11 | eval-vla-only-long-seed42 | 2026-05-19 | \n  seed=? SR=0.13 | eval-vla-only-long-seed43 | 2026-05-19 | \n  seed=? SR=0.32 | eval-obs-only-spatial-norm02-seed47 | 2026-05-19 | \n  seed=? SR=0.07 | eval-random-selection-object-k5-seed45-r2 | 2026-05-19 | \n  seed=? SR=0.1 | eval-random-selection-object-k5-seed44-r2 | 2026-05-19 | \n  seed=? SR=0.11 | eval-random-selection-object-k5-seed43-r2 | 2026-05-19 | \n  seed=? SR=0.14 | eval-random-selection-object-k5-seed42-r2 | 2026-05-19 | \n  seed=? SR=0.37 | eval-obs-only-spatial-norm02-k5-seed44-r2 | 2026-05-19 | \n  seed=? SR=0.34 | eval-obs-only-spatial-norm02-k5-seed45-r2 | 2026-05-19 | \n  seed=? SR=? | plan_602-latency-profiling | 2026-05-19 | \n  seed=? SR=0.27 | eval-vla-only-spatial-seed45 | 2026-05-19 | \n  seed=? SR=0.1 | eval-perdof-object-norm005-seed45-r2 | 2026-05-19 | \n  seed=? SR=0.31 | eval-vla-only-spatial-seed44 | 2026-05-19 | \n  seed=? SR=0.17 | eval-obs-only-object-default-seed48-r2 | 2026-05-19 | 误判 failed: cron 检测到 tmux session 死亡，但实验已正常完成并写入完整 JSON。手动验证 \n  seed=? SR=0.29 | eval-vla-only-spatial-seed43 | 2026-05-19 | \n  seed=? SR=0.3 | eval-vla-only-spatial-seed42 | 2026-05-19 | \n  seed=? SR=0.36 | eval-obs-only-spatial-norm02-seed44 | 2026-05-19 | \n  seed=? SR=0.15 | eval-obs-only-object-norm003-seed47-r2 | 2026-05-19 | 2026-05-19 12:58 UTC: FALSE ALARM — cron 检测到旧进程 EXIT_CODE=12\n  seed=? SR=0.15 | eval-obs-only-object-norm003-seed48 | 2026-05-19 | 2026-05-19 12:58 UTC: FALSE ALARM 确认 — PID 67825 在 bjb1-1822\n  seed=? SR=? | eval-perdof-object-norm01-seed43 | 2026-05-19 | \n  seed=? SR=? | eval-obs-only-object-default-seed45-r2 | 2026-05-19 | \n  seed=? SR=? | eval-argmin-object-k5-seed42 | 2026-05-19 | \n  seed=? SR=? | eval-argmin-object-k5-seed45 | 2026-05-19 | \n  seed=? SR=? | eval-argmin-object-k5-seed43 | 2026-05-19 | \n  seed=? SR=? | eval-perdof-object-norm03-seed43 | 2026-05-19 | \n  seed=? SR=0.34 | eval-obs-only-spatial-norm02-seed45 | 2026-05-19 | \n  seed=? SR=? | eval-obs-only-object-norm003-seed44-bjb2 | 2026-05-19 | 2026-05-19 21:00 UTC: 实验实际成功完成。JSON 输出在 /root/logs/eval_obje\n  seed=? SR=? | train-crm-k1-accg-object-seed42-full | 2026-05-19 | \n  seed=? SR=? | plan_701-precompute-k1-spatial | 2026-05-19 | \n  seed=? SR=? | plan_701-crm-k1-train | 2026-05-19 | \n  seed=? SR=0.16 | eval_obs_only_norm03_seed48 | 2026-05-19 | \n  seed=? SR=0.18 | eval_obs_only_norm01_seed48 | 2026-05-19 | \n  seed=? SR=0.14 | eval-lto-splitA-vla-only-r3 | 2026-05-19 | \n  seed=? SR=0.14 | eval-lto-splitA-vla-only-r2 | 2026-05-19 | \n  seed=? SR=? | crm-lto-splitA-train | 2026-05-19 | \n  seed=? SR=0.13 | eval-perdof-object-norm003-seed48 | 2026-05-19 | \n  seed=? SR=0.32 | eval-obs-only-spatial-norm02-k5-seed43 | 2026-05-19 | \n  seed=? SR=0.18 | eval-obs-only-object-norm02-k5-seed48 | 2026-05-19 | \n  seed=? SR=0.35 | eval-obs-only-spatial-norm02-k5-seed42 | 2026-05-19 | \n  seed=? SR=0.16 | eval-obs-only-object-norm02-k5-seed46 | 2026-05-19 | \n  seed=? SR=0.14 | eval-lto-splitA-vla-only-v2 | 2026-05-19 | \n  seed=? SR=0.05 | eval-perdof-object-norm03-seed47 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束\n  seed=? SR=0.17 | eval-obs-only-object-default-seed48 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束\n  seed=? SR=0.09 | eval-perdof-object-norm003-seed46 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束\n  seed=? SR=0.11 | eval-perdof-object-norm005-seed46 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束\n  seed=? SR=0.13 | eval-obs-only-object-norm02-k5-seed47 | 2026-05-19 | \n  seed=? SR=0.1 | eval-random-selection-object-seed45 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束\n  seed=? SR=0.14 | eval-obs-only-object-norm005-seed47 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束\n  seed=? SR=0.12 | eval-perdof-object-norm01-seed48 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束. JSON 位于 /root/logs/ 而非项目 logs/ 目录\n  seed=? SR=0.16 | eval-obs-only-object-default-seed47 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束\n  seed=? SR=0.04 | eval-perdof-object-norm03-seed46 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束\n  seed=? SR=0.17 | eval-obs-only-object-norm03-seed46 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束\n  seed=? SR=0.09 | eval-scalar-object-seed46 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束\n  seed=? SR=0.17 | eval-obs-only-object-norm01-seed47 | 2026-05-19 | 采集时间 2026-05-19, 进程已自然结束\n  seed=? SR=0.17 | eval-obs-only-object-norm01-seed45-r2 | 2026-05-19 | \n  seed=? SR=? | crm-lto-splitA-train-fixed | 2026-05-19 | \n  seed=? SR=0.13 | eval-perdof-object-norm003-seed43 | 2026-05-19 | \n  seed=? SR=0.13 | eval-perdof-object-norm005-seed43 | 2026-05-19 | \n  seed=? SR=0 | eval-perdof-object-default-seed43 | 2026-05-19 | \n  seed=? SR=0.18 | eval-obs-only-object-norm02-seed48-r2 | 2026-05-19 | \n  seed=? SR=0 | eval-perdof-object-default-seed45 | 2026-05-19 | \n  seed=? SR=0.15 | eval-obs-only-object-norm02-k5-seed45 | 2026-05-19 | \n  seed=? SR=0.13 | eval-vla-only-object-seed46 | 2026-05-19 | \n  seed=? SR=0.18 | eval-obs-only-object-norm01-seed48 | 2026-05-19 | \n  seed=? SR=0.3 | eval-vla-only-spatial-seed50 | 2026-05-20 | \n  seed=? SR=0.35 | eval-crm-spatial-seed48 | 2026-05-20 | \n  seed=? SR=? | eval-argmin-object-k5-seed44-r2 | 2026-05-20 | \n  seed=? SR=? | eval-obs-only-spatial-norm02-seed46-r2 | 2026-05-20 | \n  seed=? SR=0.73 | eval-vla-only-goal-seed44-r2 | 2026-05-20 | \n  seed=? SR=0.13 | eval-adaptive-k-p25-seed43 | 2026-05-20 | \n  seed=? SR=0.16 | eval-adaptive-k-p50-seed43 | 2026-05-20 | \n  seed=? SR=0.35 | eval-obs-only-spatial-norm02-seed48 | 2026-05-20 | \n  seed=? SR=0.15 | eval-adaptive-k-p25-seed42 | 2026-05-20 | \n  seed=? SR=0.16 | eval-adaptive-k-p50-seed42 | 2026-05-20 | \n  seed=? SR=0.13 | eval-adaptive-k-p75-seed43 | 2026-05-20 | \n  seed=? SR=0.72 | eval-crm-goal-seed46 | 2026-05-20 | \n  seed=? SR=0.14 | eval-adaptive-k-p90-seed44 | 2026-05-20 | \n  seed=? SR=0.12 | eval-adaptive-k-p75-seed42 | 2026-05-20 | \n  seed=? SR=0.14 | eval-adaptive-k-p50-seed44 | 2026-05-20 | \n  seed=? SR=0.16 | eval-adaptive-k-p75-seed44 | 2026-05-20 | \n  seed=? SR=0.14 | eval-adaptive-k-p90-seed43 | 2026-05-20 | \n  seed=? SR=0.12 | eval-adaptive-k-p90-seed42 | 2026-05-20 | \n  seed=? SR=0.3 | eval-vla-only-spatial-seed47 | 2026-05-20 | \n  seed=? SR=0.17 | eval-crm-long-seed47 | 2026-05-20 | \n  seed=? SR=0.1 | eval-vla-only-object-seed48 | 2026-05-20 | \n  seed=? SR=0.14 | eval-vla-only-long-seed48 | 2026-05-20 | \n  seed=? SR=0.09 | eval-vla-only-object-seed50 | 2026-05-20 | \n  seed=? SR=0.18 | eval-crm-long-seed46 | 2026-05-20 | \n  seed=? SR=0.65 | eval-crm-goal-seed45-r2 | 2026-05-20 | \n  seed=? SR=0.64 | eval-crm-goal-seed44-r2 | 2026-05-20 |",
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

_source line 62_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full registry data. Let me extract the key data points. The registry doesn't store seed/benchmark/method as separate fields - they're encoded in the experiment_id. Let me parse them more carefully.

Let me now compile the corrected data:

**LIBERO-Spatial**
CRM obs_only (norm02 K=10):
- seed42: not found as norm02 k10... use K=5: 0.35
- seed43-r2: 0.34 (eval-obs-only-spatial-norm02-seed43-r2)


- seed44: 0.36 (eval-obs-only-spatial-norm02-seed44)
- seed45: 0.34 (eval-obs-only-spatial-norm02-seed45)
- seed46-r2: pending (eval-obs-only-spatial-norm02-seed46-r2 - no SR shown)
- seed47: 0.32 (eval-obs-only-spatial-norm02-seed47)
- seed48: 0.35 (eval-obs-only-spatial-norm02-seed48 OR eval-crm-spatial-seed48)

CRM spatial K=5:
- seed42: 0.35 (eval-obs-only-spatial-norm02-k5-seed42)
- seed43: continuing to extract the remaining results... I'm noticing some discrepancies in the VLA-only spatial results—the user mentioned seeds 48, 49, and 50 with specific scores, but I'm only seeing seed50 in the registry listing. Let me cross-check what's actually recorded versus what was reported. I'm checking the registry entries for CRM-Goal and noticing that seed47 with SR=0.69 isn't showing up in the data I have, even though the user mentioned it should be included. Let me verify whether it's actually in the registry or if there's a discrepancy between what the user is telling me and what the current data shows. I'm cross-referencing the verification task results now. For Argmin K=10 with seed43, I found SR=0.17 in the registry, though there are other seed variants with slightly different scores. The file from bjb1-32546 shows a different configuration with K=5 that gave SR=0.13, so I need to make sure I'm matching the right experimental setup.

For the VLA-only long task with seed48, the registry shows SR=0.14, which aligns with one entry in the original script, but the user's mention of "14% vs 11%" suggests there might be a discrepancy I need to investigate further by looking at the complete dataset. I'm confirming the VLA-only Long seed48 value is 0.14 from the registry, which resolves the discrepancy with the 0.11 in vla_long_user. Now I'm checking the CRM Long results across the same seed range to compare performance.

I notice there's a potential CRM Long seed48 entry that hasn't been registered yet, so I need to search across all servers for any missing argmin K=10 seed43 data and verify the experiment IDs more carefully to ensure I'm capturing the complete dataset. Looking at the adaptive-K results across different percentile thresholds and seeds, I'm seeing 11 entries total which matches what the user mentioned about the completion status. The data spans p25 through p90 with seeds 42-44, and the success rates cluster around 0.12-0.16 range. Now I need to check what else might be missing from the full dataset. I need to update the main config for the Object class, then refresh the registry data and verify those suspicious data points—particularly the K=10 seed43 argmin file and the missing VLA/CRM entries. Let me search the registry more systematically and check bjb2-28827 via SSH if needed, then run the full script once I've confirmed what I'm working with.

Now I'm compiling the comprehensive registry data for LIBERO-Spatial, organizing the CRM results by seed and filtering out duplicates to get a clean dataset for the script. I'm cross-referencing the K=5 results now—seed42 through seed45 with their respective success rates—and comparing them against the K=10 preferred configuration to determine which seeds give the best coverage across both settings. I need to make sure each seed appears only once, using the latest version when there are multiple revisions. Looking at the VLA-only goal metrics, I have five seeds with scores ranging from 0.63 to 0.73. Now I'm checking the CRM goal results to compile those scores as well.

The user mentioned seed47 with a score of 0.69 that isn't in the registry, but I'll include it since they explicitly requested it. Moving on to the LIBERO-Object results, I'm gathering the CRM norm02 K=10 metrics across the seeds. Finishing up the norm01 results with that last seed value, then moving through the VLA-only object metrics across multiple seeds. I'm noticing something odd though—there's one entry labeled "openvla-object-vla-only-seed42-v2" showing a success rate of 0.69, which seems way out of line with the rest of the VLA-only results hovering around 0.09-0.13. That's suspicious and might be a mislabeled Goal result or a different model entirely.

For the VLA-only object benchmark, I'm taking the latest versions where available—seed45's r2 variant at 0.11 instead of the earlier 0.09—and compiling eight seeds total. Then I've got one Argmin K=10 entry at 0.17 from seed43.

Looking at the remaining Argmin K=10 results, I'm seeing seed44-r2 through seed47 ranging from 0.13 down to 0.10. But the K=5 variants are problematic—they're not showing success rates in the registry even though the script itself has hardcoded values like 0.15 and 0.13, so I need to figure out whether those experiments are still running or if there's a registration issue. I need to update the main configuration to use norm02 as the baseline instead of norm01, refresh the seed collections from the registry, incorporate the new data points the user mentioned, and verify that argmin K=10 seed43 value of 0.17 by checking the server logs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "c60e70ed-93af-4349-80bb-61e20a78ac57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141LqDXpJ3dTiAqRxsxVPf8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8895,
      "cache_read_input_tokens": 41650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8895
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

_source line 63_

Good, I have the full registry data. Let me search for the argmin K=10 seed43 JSON file on the remaining servers and also check for CRM Goal seed47.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "de2eb5db-2bf3-4e2e-8e2c-8bea7b3584f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141LqDXpJ3dTiAqRxsxVPf8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8895,
      "cache_read_input_tokens": 41650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8895
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

_source line 64_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_018DD4tqccui85uRVHTd9UPF`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*object*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "03763dc2-729f-4df1-9f9f-8dea8cc61094",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141LqDXpJ3dTiAqRxsxVPf8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8895,
      "cache_read_input_tokens": 41650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8895
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

_source line 65 · 2026-05-20T04:59:27.157Z_

<details><summary>↩ Tool result · `toolu_018DD4tqccui85uRVHTd9UPF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "c2f05e77-9340-4973-b431-cb8f50b4b3b0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01GjhCuhwdLgidNmomPCAYtz`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*goal*seed47*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "31da6558-187b-45c6-8fdb-c748531cdb4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141LqDXpJ3dTiAqRxsxVPf8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8895,
      "cache_read_input_tokens": 41650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8895
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

_source line 67 · 2026-05-20T04:59:28.141Z_

<details><summary>↩ Tool result · `toolu_01GjhCuhwdLgidNmomPCAYtz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "eb5165b8-9474-42c0-8f10-d30c3e9f93d2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01F723d9N2mhtAundN4k5HGo`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*vla*spatial*seed48*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "01d3795f-44fc-4b05-9a84-f8598b67bb5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141LqDXpJ3dTiAqRxsxVPf8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8895,
      "cache_read_input_tokens": 41650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8895
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

_source line 69 · 2026-05-20T04:59:29.029Z_

<details><summary>↩ Tool result · `toolu_01F723d9N2mhtAundN4k5HGo`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "2a6325c5-979d-45d5-9087-a9aa0b7a4b62",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PCQC8bYTRE41ghZH1cQ7a1`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*vla*spatial*seed49*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "32d2bfca-e4ea-4021-8da5-52e1381bac7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0141LqDXpJ3dTiAqRxsxVPf8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8895,
      "cache_read_input_tokens": 41650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8895
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

_source line 71 · 2026-05-20T04:59:29.645Z_

<details><summary>↩ Tool result · `toolu_01PCQC8bYTRE41ghZH1cQ7a1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "7371149c-9277-4acf-a15f-763426f2cdbc",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 72_

Not on bjb2-40593. Let me check bjb1-18228 and bjb1-32546 for the remaining files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "0aff6478-231f-42fb-b995-f6001f7ce875",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALvoqtPpSCuLGsAVMC6Dtu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6998,
      "cache_read_input_tokens": 50545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6998
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

_source line 73_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01R7zLSQP1fzkiJRUnAQQyYe`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*object*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "7c73959f-c93b-4f85-a121-1262e9da419a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALvoqtPpSCuLGsAVMC6Dtu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6998,
      "cache_read_input_tokens": 50545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6998
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

_source line 74 · 2026-05-20T04:59:34.454Z_

<details><summary>↩ Tool result · `toolu_01R7zLSQP1fzkiJRUnAQQyYe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "f7328c78-0174-4282-b96c-18aef96f45bd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 75_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_016PLhXL2ecBUGPfYdQpQknz`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*goal*seed47*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "216c59ee-6718-4a70-8710-1ea725c2f151",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALvoqtPpSCuLGsAVMC6Dtu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6998,
      "cache_read_input_tokens": 50545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6998
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

_source line 76 · 2026-05-20T04:59:35.401Z_

<details><summary>↩ Tool result · `toolu_016PLhXL2ecBUGPfYdQpQknz`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "a6af5b24-6b1a-4c9b-b1b4-9f578e429ea1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.36}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01ATfb48fiXRcwnSpudinWZf`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*vla*spatial*seed48*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "1037d1b7-0d95-4bc1-a6ed-a9349e5ceba8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALvoqtPpSCuLGsAVMC6Dtu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6998,
      "cache_read_input_tokens": 50545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6998
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

_source line 78 · 2026-05-20T04:59:36.359Z_

<details><summary>↩ Tool result · `toolu_01ATfb48fiXRcwnSpudinWZf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "2c469148-1b5c-42b2-a2dc-b2ac2b960646",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 79_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011gxJgYKJU9TRXAPqoSj3Ja`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*vla*long*seed48*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "148e2b09-38c9-4091-8a74-492be9dfcf14",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALvoqtPpSCuLGsAVMC6Dtu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6998,
      "cache_read_input_tokens": 50545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6998
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

_source line 80 · 2026-05-20T04:59:37.274Z_

<details><summary>↩ Tool result · `toolu_011gxJgYKJU9TRXAPqoSj3Ja`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "85a57e65-4606-4180-853f-f6502d2c3422",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 81_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SfKLWz3PRrpPjG5GShHwUC`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*object*k10*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "e2872f99-fd70-4990-ae7d-4669fd2b9567",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALvoqtPpSCuLGsAVMC6Dtu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6998,
      "cache_read_input_tokens": 50545,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6998
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

_source line 82 · 2026-05-20T04:59:37.913Z_

<details><summary>↩ Tool result · `toolu_01SfKLWz3PRrpPjG5GShHwUC`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "8ade25ca-16df-4ad3-98af-abe99d16deb2",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 83_

<details><summary>Logged reasoning block</summary>

```text
None of these files exist on the other servers. Let me check the bjb2-28827 server and also look for the argmin K=10 seed43 file with different naming conventions. It may also be in /root/logs/ instead of /root/acr-vla-conformal-refinement/logs/.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "86c4adf5-a1fd-4e63-8caa-006c841733ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDdocCZeinKg57RL4dv7Pk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 57543,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1123
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

_source line 84_

Let me check the other server and alternative paths.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "1da7e7d1-3441-4b05-9712-c3ac8d420345",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDdocCZeinKg57RL4dv7Pk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 57543,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1123
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

_source line 85_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01PAkmYs3c8XHycMS8Mu28ih`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/logs/ -name \"*argmin*seed43*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "d081cab2-09f3-490e-99b0-405137734384",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDdocCZeinKg57RL4dv7Pk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 57543,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1123
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

_source line 86 · 2026-05-20T04:59:42.629Z_

<details><summary>↩ Tool result · `toolu_01PAkmYs3c8XHycMS8Mu28ih`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "d818554d-305f-4c7a-9fa2-e100dd0d422f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 87_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013CvQZhaF9Xy3dUS912AZTX`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "5a5e6a57-260a-4055-b27a-e9220d6c571b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDdocCZeinKg57RL4dv7Pk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 57543,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1123
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

_source line 88 · 2026-05-20T04:59:43.973Z_

<details><summary>↩ Tool result · `toolu_013CvQZhaF9Xy3dUS912AZTX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "66e90f95-fac7-4eb6-bfe4-6d40d9340a54",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/acr-vla-conformal-refinement/logs/eval_object_argmin_k5_seed43.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 89_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01TEpRjnhhFJ7BGmKpg1bYmQ`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/logs/ -name \"*argmin*seed43*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "3ce6cc8e-5b73-4671-bc31-3709c2f2b2b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDdocCZeinKg57RL4dv7Pk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 57543,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1123
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

_source line 90 · 2026-05-20T04:59:44.532Z_

<details><summary>↩ Tool result · `toolu_01TEpRjnhhFJ7BGmKpg1bYmQ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "a24e1fdc-37f7-4861-a3e9-f3b78202132a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 91_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01HkwCi9HwRyW8qYqjCiwnTT`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/logs/ -name \"*long*seed48*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "5e4acc2c-c063-48be-a125-7888c3e2bb11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDdocCZeinKg57RL4dv7Pk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 57543,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1123
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

_source line 92 · 2026-05-20T04:59:44.997Z_

<details><summary>↩ Tool result · `toolu_01HkwCi9HwRyW8qYqjCiwnTT`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "0f1a137f-e562-4513-9713-b6b5bd8a93e7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 93_

<details><summary>Logged reasoning block</summary>

```text
The `2>/dev/null` has `>` which is being blocked. Let me try without error redirection. Also, on bjb1-32546, the only argmin seed43 file is K=5, not K=10. The K=10 seed43 data point in the registry (eval-argmin-object-seed43: 0.17) doesn't have a corresponding JSON file on any of the servers I've checked.

Let me search /root/logs/ paths without the `2>/dev/null` redirect.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "6727e0b2-a255-406a-b20a-bdb55bcfd7c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzE4ZoHi5JLXyQvoMQBgvB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 58666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1142
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

_source line 94_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_011pDcTU7k4ADJLZx6EJhPwM`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/logs/ -name \"*argmin*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "68337cd2-3c1b-4c14-b6eb-e751b24b5305",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzE4ZoHi5JLXyQvoMQBgvB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 58666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1142
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

_source line 95_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013U3YxX6ZBQQpo8p8j4PJqF`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/logs/ -name \"*argmin*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "a19b7b52-cf71-4385-9f47-1a13a28b2c77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzE4ZoHi5JLXyQvoMQBgvB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 58666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1142
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

_source line 96 · 2026-05-20T04:59:51.913Z_

<details><summary>↩ Tool result · `toolu_011pDcTU7k4ADJLZx6EJhPwM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "41d6eb4d-6d37-444e-b7d3-bfbabf804c4a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-20T04:59:52.280Z_

<details><summary>↩ Tool result · `toolu_013U3YxX6ZBQQpo8p8j4PJqF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "4d79283e-8ea3-4852-b69e-097c2bbc2a38",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 98_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SYq7GrjpM9aBCC68FssKGF`</summary>

```json
{
  "server": "bjb1-18228",
  "command": "find /root/logs/ -name \"*long*seed48*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "a64329f7-3e23-48c6-9cbb-7aa3e57c33ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzE4ZoHi5JLXyQvoMQBgvB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 58666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1142
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

_source line 99 · 2026-05-20T04:59:53.017Z_

<details><summary>↩ Tool result · `toolu_01SYq7GrjpM9aBCC68FssKGF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "3dff46f1-ece2-47f7-9cc3-5c68ea6f6c29",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 100_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01SbhfTXDDDpLdy6GKa7au4U`</summary>

```json
{
  "server": "bjb1-32546",
  "command": "find /root/logs/ -name \"*long*seed48*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "3cff487f-1ba7-4c69-8f2c-19431bbbad01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzE4ZoHi5JLXyQvoMQBgvB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 58666,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1142
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

_source line 101 · 2026-05-20T04:59:53.443Z_

<details><summary>↩ Tool result · `toolu_01SbhfTXDDDpLdy6GKa7au4U`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "6b6daf11-faf4-4367-bef6-967fa652faa9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 102_

<details><summary>Logged reasoning block</summary>

```text
OK, I couldn't find the argmin K=10 seed43 file or the VLA long seed48 file on any of the servers. The only argmin seed43 file I found is the K=5 version on bjb1-32546 (SR=0.13). The eval-vla-only-long-seed48 is in the registry with SR=0.14.

For the argmin K=10 seed43 = 0.17 data point: The registry says eval-argmin-object-seed43: SR=0.17. The original JSON file may have been lost or moved. 

The K=5 version for the same seed is 0.13, and other K=10 seeds range from 0.10-0.13, so 0.17 stands out as an outlier. I'll include it since it's registered, but note the discrepancy. The VLA-only Long seed48 at 0.14 is confirmed in the registry.

Now I'm reviewing the specific data points the user mentioned to make sure I have everything accounted for before compiling the corrected script. Now I'm compiling the complete dataset with the corrected benchmark configurations and verified registry values, organizing the LIBERO-Spatial results by seed and K-parameter settings. Now I'm compiling the performance metrics for LIBERO-Long across both model variants, with CRM showing stronger results around 0.17 average compared to VLA-only's 0.14 average, then moving into the LIBERO-Goal benchmark results. Now I'm looking at the LIBERO-Object results, pulling the CRM norm02 K=10 scores as the primary benchmark across six seeds, then cross-referencing with the norm01 supplementary data to see how performance varies across different normalization approaches. Now I'm compiling the VLA-only results with the additional seed50 data point, then moving through the Argmin K=10 configuration where seed43 flagged as an outlier due to JSON verification issues, and finally noting the earlier Argmin K=5 result that isn't currently in the registry.

Looking at the updated metrics across the Adaptive-K percentiles—seed42, seed43, and seed44 showing varying performance at the p25, p50, p75, and p90 thresholds—I'm ready to refactor the script to use the normalized CRM object as the foundation.

The key structural shifts are moving norm02 to primary status, consolidating all comparison tables around it, and pushing norm01 into supplementary analysis. I'm also incorporating the corrected seed values, particularly the VLA Long seed48 adjustment to 0.14, and adding the new data points for CRM Goal and VLA Spatial seeds.

One issue I'm flagging: I can't locate the JSON file for argmin K=10 seed43 on the accessible servers—the registry shows it as eval-argmin-object-seed43 with SR=0.17, so it may have been on a decommissioned server. I'll retain the value but note it as a potential outlier, and I should check bjb2-28827 as another server option.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "09440cf6-cff3-4f87-bdcb-41cb33cda5ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013AHms83kqNvUZM2AjhFY87",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 59808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 954
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

_source line 103_

Let me check bjb2-28827 for the argmin K=10 seed43 file and the VLA long seed48 file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "c4a20af7-5729-453f-a23b-d8d055b1c859",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013AHms83kqNvUZM2AjhFY87",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 59808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 954
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

_source line 104_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01V5p59j8NvM1DG2qvJujb9x`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*argmin*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "9c4340e4-ca88-49b1-8069-6fdedb5e0a52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013AHms83kqNvUZM2AjhFY87",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 59808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 954
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

_source line 105_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_013KGCLEf3KWidDrWf27uxBu`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/acr-vla-conformal-refinement/logs/ -name \"*long*seed48*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "eb9f8191-6127-495a-98ba-f1463761db5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013AHms83kqNvUZM2AjhFY87",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 59808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 954
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

_source line 106 · 2026-05-20T05:00:40.323Z_

<details><summary>↩ Tool result · `toolu_01V5p59j8NvM1DG2qvJujb9x`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "3ae0833e-db8b-463d-8338-5d6e9f7e6de8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.91}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-20T05:00:40.709Z_

<details><summary>↩ Tool result · `toolu_013KGCLEf3KWidDrWf27uxBu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "79546ae3-cde4-401a-bff3-22d0d03fad52",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.37}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 108_

<details><summary>Logged reasoning block</summary>

```text
Neither file found on bjb2-28827 either. Let me try the /root/logs/ directory on bjb2-28827 and bjb2-40593 as well.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "0cedab13-686d-497e-a485-d9171a7ca1fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CxpXrzV5QvJbLYYVUU9agP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3005,
      "cache_read_input_tokens": 60762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3005
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

_source line 109_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01NbSkbv3G5hsm3QTCjhRLZK`</summary>

```json
{
  "server": "bjb2-28827",
  "command": "find /root/logs/ -name \"*argmin*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "ff3832c4-b121-4453-b1b8-95f78b3187da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CxpXrzV5QvJbLYYVUU9agP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3005,
      "cache_read_input_tokens": 60762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3005
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

_source line 110_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0178YnWdCr7PsAYEtQJ798uz`</summary>

```json
{
  "server": "bjb2-40593",
  "command": "find /root/logs/ -name \"*argmin*seed43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "8f7a8213-30af-4b06-9963-30f190208968",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CxpXrzV5QvJbLYYVUU9agP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3005,
      "cache_read_input_tokens": 60762,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3005
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

_source line 111 · 2026-05-20T05:00:45.664Z_

<details><summary>↩ Tool result · `toolu_01NbSkbv3G5hsm3QTCjhRLZK`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "f8f44ea6-f3f1-4e00-ad82-0fea395744eb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-20T05:00:45.993Z_

<details><summary>↩ Tool result · `toolu_0178YnWdCr7PsAYEtQJ798uz`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/logs/': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "e5f2e288-a0f5-4fb6-9f9a-2fcf60f7fe43",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"find: '/root/logs/': No such file or directory\\\\n\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/logs/': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 113_

<details><summary>Logged reasoning block</summary>

```text
The argmin K=10 seed43 JSON file cannot be found on any of the 4 servers. The registry entry exists (eval-argmin-object-seed43: SR=0.17), so the data is from the registry but the original JSON may have been lost or was on a since-decommissioned server. Given that:
- Argmin K=10 seed43 = 0.17 is a severe outlier (other seeds: 0.10-0.13)
- The only seed43 argmin file I can find is K=5 with SR=0.13


- I can't verify the original JSON

I'll note this as an unverified outlier in the script comments and keep it in the data since it's in the registry. For VLA-only Long seed48, the registry says 0.14, which I'll accept. Now I'm ready to build the corrected script with norm02 K=10 as the primary Object config, keeping norm01 as supplementary, and updating all the summary tables accordingly.

I'm consolidating the data into a single authoritative dataset, removing the duplicate user-provided versus registry splits, and incorporating the new seeds: CRM-Goal seed47 at 0.69, VLA-Spatial seed48 at 0.30 and seed49 at 0.29, plus the confirmed VLA Long seed48 at 0.14.

Writing the corrected script...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "cb9057f1-326b-4e5a-855b-1b1302a2dabb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013usyUeJe6w5hNkWuSmo2qK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 503,
      "cache_read_input_tokens": 63767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 503
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

_source line 114_

Verification complete. Argmin K=10 seed43 JSON cannot be found on any of the 4 servers — the registry value (0.17) is unverifiable. VLA Long seed48 = 0.14 is confirmed by the registry. Now writing the corrected script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "5d20f2bf-d29d-47a1-b8dc-ebce65b5600b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013usyUeJe6w5hNkWuSmo2qK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 503,
      "cache_read_input_tokens": 63767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 503
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

_source line 115_

<details open><summary>🔧 Tool call — Write · `toolu_01Hqq4QwWeWJ9opsjNisDjNW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35]  # s42(k5), s43-r2, s44, s45, s47, s48\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # s42, s43, s44, s45, s46, s47\n\n# VLA-only Long (seeds 42-48)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]  # s42, s43, s44, s45, s46, s47, s48\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71]  # s42, s43, s44-r2, s45, s46\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13]  # s42, s43\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_long)\nprint_group_stats(\"VLA-only (n=7)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=5)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "45cd41c9-9d26-4de0-8dda-2e079a058eff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013usyUeJe6w5hNkWuSmo2qK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 503,
      "cache_read_input_tokens": 63767,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 503
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

_source line 116 · 2026-05-20T05:02:08.836Z_

<details><summary>↩ Tool result · `toolu_01Hqq4QwWeWJ9opsjNisDjNW`</summary>

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
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "2ad1b28b-65a0-49e2-b89e-fbea3b83097f",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/statistical_analysis.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\nPrimary CRM config for Object: norm02 (ε=0.2), K=10.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA (from registry, conclusion=success, 2026-05-20)\n# Each seed appears once; r2/r3 supersedes earlier runs.\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback\ncrm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35]  # s42(k5), s43-r2, s44, s45, s47, s48\n\n# VLA-only Spatial (seeds 42-50)\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50\n\n# --- LIBERO-Long ---\n# CRM obs_only Long (seeds 42-47)\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # s42, s43, s44, s45, s46, s47\n\n# VLA-only Long (seeds 42-48)\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]  # s42, s43, s44, s45, s46, s47, s48\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal (seeds 42-47)\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47\n\n# VLA-only Goal (seeds 42-46)\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71]  # s42, s43, s44-r2, s45, s46\n\n# --- LIBERO-Object ---\n# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)\ncrm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2\n\n# Supplementary: CRM obs_only norm01 (seeds 42-48)\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48\n\n# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)\ncrm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48\n\n# VLA-only Object (seeds 42-50, using r2 for seed45)\nvla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50\n\n# --- Argmin Object ---\n# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45\n\n# --- Adaptive-K Object ---\nadaptive_k_p25 = [0.15, 0.13]  # s42, s43\nadaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44\nadaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44\nadaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_spatial)\nprint_group_stats(\"VLA-only (n=9)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)\n\n# ============================================================================\n# 2. LIBERO-LONG\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_long)\nprint_group_stats(\"VLA-only (n=7)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\n# ============================================================================\n# 3. LIBERO-GOAL\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint_group_stats(\"CRM obs_only (n=6)\", crm_goal)\nprint_group_stats(\"VLA-only (n=5)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT (primary: norm02 K=10)\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [PRIMARY: CRM norm02 K=10]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm01]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [Supplementary: CRM norm02 K=5]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)\nrun_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")\nprint_separator('-')\n\ndef get_vla_baseline(bench):\n    if bench == \"LIBERO-Spatial\": return vla_spatial\n    if bench == \"LIBERO-Long\": return vla_long\n    if bench == \"LIBERO-Goal\": return vla_goal\n    if bench == \"LIBERO-Object\": return vla_object\n    return None\n\ndef print_summary_row(bench, method, vals, is_vla=False):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    baseline = get_vla_baseline(bench)\n    if is_vla or baseline is None:\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")\n    else:\n        bl_arr = np.array(baseline)\n        diff = mean - bl_arr.mean()\n        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)\n        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")\n\nprint_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)\nprint_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)\nprint()\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)\nprint_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY SIGNIFICANCE RESULTS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),\n    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),\n    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),\n    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\n# ============================================================================\n# 9. VERIFICATION NOTES\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"VERIFICATION NOTES\")\nprint_separator()\nprint(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")\nprint(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")\nprint(\"  Registry value retained but unverified.\")\nprint(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")\nprint(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")\nprint(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 6,
        "newStart": 3,
        "newLines": 8,
        "lines": [
          " Statistical analysis of ACR-VLA Conformal Refinement experiments.",
          " Compares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.",
          " Also includes Argmin and Adaptive-K baselines.",
          "+",
          "+Primary CRM config for Object: norm02 (ε=0.2), K=10.",
          " \"\"\"",
          " ",
          " import numpy as np"
        ]
      },
      {
        "oldStart": 12,
        "oldLines": 31,
        "newStart": 14,
        "newLines": 24,
        "lines": [
          "     print(char * width)",
          " ",
          " def print_group_stats(name, values):",
          "-    \"\"\"Print mean +/- std for a group.\"\"\"",
          "     arr = np.array(values)",
          "     print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"",
          "           f\"min={arr.min():.4f}, max={arr.max():.4f}\")",
          "     print(f\"    values: {[round(v, 4) for v in values]}\")",
          " ",
          " def run_tests(name_a, vals_a, name_b, vals_b):",
          "-    \"\"\"Run t-test and Mann-Whitney U test between two groups.\"\"\"",
          "     a = np.array(vals_a)",
          "     b = np.array(vals_b)",
          " ",
          "-    # Independent two-sample t-test (Welch's, unequal variance)",
          "     t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)",
          "-",
          "-    # Mann-Whitney U test (non-parametric)",
          "     u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')",
          " ",
          "-    # Effect size: Cohen's d",
          "     pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /",
          "                          (len(a) + len(b) - 2))",
          "     cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')",
          " ",
          "-    # Difference",
          "     diff = a.mean() - b.mean()",
          "-    diff_pct = diff * 100  # percentage points",
          "+    diff_pct = diff * 100",
          " ",
          "     print(f\"\\n  {name_a} vs {name_b}:\")",
          "     print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")"
        ]
      },
      {
        "oldStart": 47,
        "oldLines": 86,
        "newStart": 42,
        "newLines": 54,
        "lines": [
          "     return t_pval, u_pval",
          " ",
          " # ============================================================================",
          "-# DATA FROM REGISTRY (verified from all experiments with conclusion=success)",
          "+# DATA (from registry, conclusion=success, 2026-05-20)",
          "+# Each seed appears once; r2/r3 supersedes earlier runs.",
          " # ============================================================================",
          " ",
          " # --- LIBERO-Spatial ---",
          "-# CRM obs_only (norm02 variants, K=5 and K=10): seeds 42-48",
          "-# From registry: seed42=0.35, seed43=0.32(k5) or 0.34(norm02-r2), seed44=0.37(k5-r2) or 0.36(norm02),",
          "-# seed45=0.34(k5-r2) or 0.34(norm02), seed46=0.33(r2), seed47=0.32(norm02), seed48=0.35(norm02 and crm-spatial)",
          "-# Using the best-matched K=10 norm02 experiments (primary config):",
          "-crm_spatial = [0.34, 0.36, 0.34, 0.33, 0.32, 0.35]  # seeds 43-r2, 44, 45, 46-r2, 47, 48",
          "-# K=5 variants:",
          "-crm_spatial_k5 = [0.35, 0.32, 0.37, 0.34]  # seeds 42, 43, 44-r2, 45-r2",
          "-# Combined unique seeds (using K=10 when available, K=5 for seed42):",
          "-crm_spatial_all = [0.35, 0.34, 0.36, 0.34, 0.33, 0.32, 0.35]  # seeds 42(k5), 43-r2, 44, 45, 46-r2, 47, 48",
          "-# Fallback from user-provided data (n=8):",
          "-crm_spatial_user = [0.32, 0.34, 0.36, 0.34, 0.34, 0.33, 0.32, 0.35]",
          "+# CRM obs_only norm02 K=10 (seeds 43-48); seed42 uses K=5 fallback",
          "+crm_spatial = [0.35, 0.34, 0.36, 0.34, 0.32, 0.35]  # s42(k5), s43-r2, s44, s45, s47, s48",
          " ",
          "-# VLA-only Spatial: seeds 42-50",
          "-vla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30]  # seeds 42, 43, 44, 45, 46, 47, 50",
          "-# Fallback from user-provided data (n=9):",
          "-vla_spatial_user = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.30, 0.29]",
          "+# VLA-only Spatial (seeds 42-50)",
          "+vla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.29, 0.30]  # s42, s43, s44, s45, s46, s47, s48, s49, s50",
          " ",
          " # --- LIBERO-Long ---",
          "-# CRM obs_only Long: seeds 42-47",
          "-crm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # seeds 42, 43, 44, 45, 46, 47",
          "-# User-provided (same):",
          "-crm_long_user = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]",
          "+# CRM obs_only Long (seeds 42-47)",
          "+crm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # s42, s43, s44, s45, s46, s47",
          " ",
          "-# VLA-only Long: seeds 42-48",
          "-vla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]  # seeds 42, 43, 44, 45, 46, 47, 48",
          "-# User-provided (n=7):",
          "-vla_long_user = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.11]",
          "+# VLA-only Long (seeds 42-48)",
          "+vla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]  # s42, s43, s44, s45, s46, s47, s48",
          " ",
          " # --- LIBERO-Goal ---",
          "-# CRM obs_only Goal: seeds 42-46",
          "-crm_goal = [0.67, 0.72, 0.64, 0.65, 0.72]  # seeds 42, 43, 44-r2, 45-r2, 46",
          "-# User-provided (same):",
          "-crm_goal_user = [0.67, 0.72, 0.64, 0.65, 0.72]",
          "+# CRM obs_only Goal (seeds 42-47)",
          "+crm_goal = [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]  # s42, s43, s44-r2, s45-r2, s46, s47",
          " ",
          "-# VLA-only Goal: seeds 42-46",
          "-vla_goal = [0.71, 0.69, 0.73, 0.63, 0.71]  # seeds 42, 43, 44-r2, 45, 46",
          "-# User-provided (same):",
          "-vla_goal_user = [0.71, 0.69, 0.73, 0.63, 0.71]",
          "+# VLA-only Goal (seeds 42-46)",
          "+vla_goal = [0.71, 0.69, 0.73, 0.63, 0.71]  # s42, s43, s44-r2, s45, s46",
          " ",
          " # --- LIBERO-Object ---",
          "-# CRM obs_only Object (norm02, K=10): seeds from registry",
          "-# Using norm02 K=10 results: seed43-r2=0.16, seed44-r2=0.16, seed45=0.16, seed46=0.15, seed47=0.20, seed48-r2=0.18",
          "-# Using norm01 results: seed42=0.19, seed44=0.16, seed45-r2=0.17, seed46-r3=0.18, seed47=0.17, seed48=0.18",
          "-# Using norm02 K=5 results: seed42=0.14, seed43=0.19, seed44=0.17, seed45=0.15, seed46=0.16, seed47=0.13, seed48=0.18",
          "-# We'll use norm01 as the primary CRM config (best performing, consistent config):",
          "-crm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # seeds 42, 44, 45-r2, 46-r3, 47, 48",
          "-# norm02 K=10:",
          "-crm_object_norm02 = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # seeds 43-r2, 44-r2, 45, 46, 47, 48-r2",
          "-# norm02 K=5:",
          "-crm_object_norm02_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # seeds 42-48",
          "+# PRIMARY: CRM obs_only norm02 K=10 (seeds 43-48)",
          "+crm_object = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # s43-r2, s44-r2, s45, s46, s47, s48-r2",
          " ",
          "-# VLA-only Object: from registry",
          "-# seed42=0.12 (overall_sr), seed43=0.12 (overall_sr), seed44-r2=0.10, seed45=0.09(overall_sr),",
          "-# seed45-r2=0.11, seed46=0.13, seed47=0.10, seed48=0.10, seed50=0.09",
          "-vla_object = [0.12, 0.12, 0.10, 0.09, 0.13, 0.10, 0.10, 0.09]  # seeds 42, 43, 44-r2, 45, 46, 47, 48, 50",
          "-# Using seed45-r2 instead of seed45 (more recent run):",
          "-vla_object_alt = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]",
          "+# Supplementary: CRM obs_only norm01 (seeds 42-48)",
          "+crm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # s42, s44, s45-r2, s46-r3, s47, s48",
          " ",
          "-# --- Argmin Object ---",
          "-# K=10: seed43=0.17, seed44-r2=0.13, seed45=0.12, seed46=0.10, seed47=0.10",
          "-argmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]",
          "-# K=5: seed42=0.15, seed43=0.13, seed44-r2=0.11, seed45=0.13",
          "-argmin_object_k5 = [0.15, 0.13, 0.11, 0.13]",
          "+# Supplementary: CRM obs_only norm02 K=5 (seeds 42-48)",
          "+crm_object_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # s42, s43, s44, s45, s46, s47, s48",
          " ",
          "-# Argmin Spatial (only 1 data point from registry)",
          "-argmin_spatial = [0.34]",
          "+# VLA-only Object (seeds 42-50, using r2 for seed45)",
          "+vla_object = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]  # s42, s43, s44-r2, s45-r2, s46, s47, s48, s50",
          " ",
          "+# --- Argmin Object ---",
          "+# K=10: seed43=0.17 is outlier (JSON not found on any server for verification)",
          "+argmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]  # s43, s44-r2, s45, s46, s47",
          "+argmin_object_k5 = [0.15, 0.13, 0.11, 0.13]  # s42, s43, s44-r2, s45",
          "+",
          " # --- Adaptive-K Object ---",
          "-# p25: seed42=0.15, seed43=0.13",
          "-adaptive_k_p25 = [0.15, 0.13]",
          "-# p50: seed42=0.16, seed43=0.16, seed44=0.14",
          "-adaptive_k_p50 = [0.16, 0.16, 0.14]",
          "-# p75: seed42=0.12, seed43=0.13, seed44=0.16",
          "-adaptive_k_p75 = [0.12, 0.13, 0.16]",
          "-# p90: seed42=0.12, seed43=0.14, seed44=0.14",
          "-adaptive_k_p90 = [0.12, 0.14, 0.14]",
          "+adaptive_k_p25 = [0.15, 0.13]  # s42, s43",
          "+adaptive_k_p50 = [0.16, 0.16, 0.14]  # s42, s43, s44",
          "+adaptive_k_p75 = [0.12, 0.13, 0.16]  # s42, s43, s44",
          "+adaptive_k_p90 = [0.12, 0.14, 0.14]  # s42, s43, s44",
          " ",
          " ",
          " # ============================================================================"
        ]
      },
      {
        "oldStart": 136,
        "oldLines": 69,
        "newStart": 99,
        "newLines": 55,
        "lines": [
          " print_separator()",
          " print(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")",
          " print(\"All success rates are fractions (0.0 to 1.0)\")",
          "+print(\"Object benchmark primary CRM config: norm02 (ε=0.2), K=10\")",
          " print_separator()",
          " ",
          " # ============================================================================",
          "-# 1. LIBERO-SPATIAL: CRM vs VLA-only",
          "+# 1. LIBERO-SPATIAL",
          " # ============================================================================",
          " print(\"\\n1. LIBERO-SPATIAL\")",
          " print_separator('-')",
          "-print(\"\\n  [Registry data]\")",
          "-print_group_stats(\"CRM obs_only (registry, n=7)\", crm_spatial_all)",
          "-print_group_stats(\"VLA-only (registry, n=7)\", vla_spatial)",
          "-run_tests(\"CRM\", crm_spatial_all, \"VLA-only\", vla_spatial)",
          "+print_group_stats(\"CRM obs_only (n=6)\", crm_spatial)",
          "+print_group_stats(\"VLA-only (n=9)\", vla_spatial)",
          "+run_tests(\"CRM\", crm_spatial, \"VLA-only\", vla_spatial)",
          " ",
          "-print(\"\\n  [User-provided data]\")",
          "-print_group_stats(\"CRM obs_only (user, n=8)\", crm_spatial_user)",
          "-print_group_stats(\"VLA-only (user, n=9)\", vla_spatial_user)",
          "-run_tests(\"CRM\", crm_spatial_user, \"VLA-only\", vla_spatial_user)",
          "-",
          " # ============================================================================",
          "-# 2. LIBERO-LONG: CRM vs VLA-only",
          "+# 2. LIBERO-LONG",
          " # ============================================================================",
          " print(\"\\n\\n2. LIBERO-LONG\")",
          " print_separator('-')",
          "-print(\"\\n  [Registry data]\")",
          "-print_group_stats(\"CRM obs_only (registry, n=6)\", crm_long)",
          "-print_group_stats(\"VLA-only (registry, n=7)\", vla_long)",
          "+print_group_stats(\"CRM obs_only (n=6)\", crm_long)",
          "+print_group_stats(\"VLA-only (n=7)\", vla_long)",
          " run_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)",
          " ",
          "-print(\"\\n  [User-provided data]\")",
          "-print_group_stats(\"CRM obs_only (user, n=6)\", crm_long_user)",
          "-print_group_stats(\"VLA-only (user, n=7)\", vla_long_user)",
          "-run_tests(\"CRM\", crm_long_user, \"VLA-only\", vla_long_user)",
          "-",
          " # ============================================================================",
          "-# 3. LIBERO-GOAL: CRM vs VLA-only",
          "+# 3. LIBERO-GOAL",
          " # ============================================================================",
          " print(\"\\n\\n3. LIBERO-GOAL\")",
          " print_separator('-')",
          "-print(\"\\n  [Registry data = User-provided data]\")",
          "-print_group_stats(\"CRM obs_only (n=5)\", crm_goal)",
          "+print_group_stats(\"CRM obs_only (n=6)\", crm_goal)",
          " print_group_stats(\"VLA-only (n=5)\", vla_goal)",
          " run_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)",
          " ",
          " # ============================================================================",
          "-# 4. LIBERO-OBJECT: CRM vs VLA-only",
          "+# 4. LIBERO-OBJECT (primary: norm02 K=10)",
          " # ============================================================================",
          " print(\"\\n\\n4. LIBERO-OBJECT\")",
          " print_separator('-')",
          " ",
          "-print(\"\\n  [CRM norm01 config]\")",
          "-print_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)",
          "+print(\"\\n  [PRIMARY: CRM norm02 K=10]\")",
          "+print_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object)",
          " print_group_stats(\"VLA-only (n=8)\", vla_object)",
          "+run_tests(\"CRM norm02 K=10\", crm_object, \"VLA-only\", vla_object)",
          "+",
          "+print(\"\\n  [Supplementary: CRM norm01]\")",
          "+print_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)",
          " run_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)",
          " ",
          "-print(\"\\n  [CRM norm02 K=10 config]\")",
          "-print_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object_norm02)",
          "-print_group_stats(\"VLA-only (n=8)\", vla_object)",
          "-run_tests(\"CRM norm02\", crm_object_norm02, \"VLA-only\", vla_object)",
          "+print(\"\\n  [Supplementary: CRM norm02 K=5]\")",
          "+print_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_k5)",
          "+run_tests(\"CRM norm02 K=5\", crm_object_k5, \"VLA-only\", vla_object)",
          " ",
          "-print(\"\\n  [CRM norm02 K=5 config]\")",
          "-print_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_norm02_k5)",
          "-print_group_stats(\"VLA-only (n=8)\", vla_object)",
          "-run_tests(\"CRM norm02 K=5\", crm_object_norm02_k5, \"VLA-only\", vla_object)",
          "-",
          " # ============================================================================",
          " # 5. ARGMIN BASELINES (Object)",
          " # ============================================================================"
        ]
      },
      {
        "oldStart": 207,
        "oldLines": 12,
        "newStart": 156,
        "newLines": 12,
        "lines": [
          " print_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)",
          " print_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)",
          " print_group_stats(\"VLA-only (n=8)\", vla_object)",
          "-print_group_stats(\"CRM norm01 (n=6)\", crm_object_norm01)",
          "+print_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)",
          " ",
          " print(\"\\n  Argmin K=10 vs VLA-only:\")",
          " run_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)",
          "-print(\"\\n  Argmin K=10 vs CRM norm01:\")",
          "-run_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm01\", crm_object_norm01)",
          "+print(\"\\n  Argmin K=10 vs CRM norm02 K=10:\")",
          "+run_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm02\", crm_object)",
          " ",
          " # ============================================================================",
          " # 6. ADAPTIVE-K BASELINES (Object)"
        ]
      },
      {
        "oldStart": 226,
        "oldLines": 12,
        "newStart": 175,
        "newLines": 12,
        "lines": [
          " all_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90",
          " print_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)",
          " print_group_stats(\"VLA-only (n=8)\", vla_object)",
          "-print_group_stats(\"CRM norm01 (n=6)\", crm_object_norm01)",
          "+print_group_stats(\"CRM norm02 K=10 (n=6)\", crm_object)",
          " ",
          " print(\"\\n  Adaptive-K (all) vs VLA-only:\")",
          " run_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)",
          "-print(\"\\n  Adaptive-K (all) vs CRM norm01:\")",
          "-run_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm01\", crm_object_norm01)",
          "+print(\"\\n  Adaptive-K (all) vs CRM norm02 K=10:\")",
          "+run_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm02\", crm_object)",
          " ",
          " # ============================================================================",
          " # 7. SUMMARY TABLE"
        ]
      },
      {
        "oldStart": 240,
        "oldLines": 38,
        "newStart": 189,
        "newLines": 50,
        "lines": [
          " print_separator()",
          " print(\"SUMMARY TABLE\")",
          " print_separator()",
          "-print(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'95% CI':>15}\")",
          "+print(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'Δ vs VLA':>9} {'p-value':>10} {'Sig':>5}\")",
          " print_separator('-')",
          " ",
          "-def print_row(bench, method, vals):",
          "+def get_vla_baseline(bench):",
          "+    if bench == \"LIBERO-Spatial\": return vla_spatial",
          "+    if bench == \"LIBERO-Long\": return vla_long",
          "+    if bench == \"LIBERO-Goal\": return vla_goal",
          "+    if bench == \"LIBERO-Object\": return vla_object",
          "+    return None",
          "+",
          "+def print_summary_row(bench, method, vals, is_vla=False):",
          "     arr = np.array(vals)",
          "     n = len(arr)",
          "     mean = arr.mean()",
          "     std = arr.std(ddof=1)",
          "-    se = std / np.sqrt(n)",
          "-    ci_lo = mean - 1.96 * se",
          "-    ci_hi = mean + 1.96 * se",
          "-    print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} [{ci_lo:.4f}, {ci_hi:.4f}]\")",
          "+    baseline = get_vla_baseline(bench)",
          "+    if is_vla or baseline is None:",
          "+        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {'—':>9} {'—':>10} {'—':>5}\")",
          "+    else:",
          "+        bl_arr = np.array(baseline)",
          "+        diff = mean - bl_arr.mean()",
          "+        _, t_pval = stats.ttest_ind(arr, bl_arr, equal_var=False)",
          "+        sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'",
          "+        print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} {diff:>+9.4f} {t_pval:>10.6f} {sig:>5}\")",
          " ",
          "-print_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial_all)",
          "-print_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial)",
          "+print_summary_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial)",
          "+print_summary_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial, is_vla=True)",
          " print()",
          "-print_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)",
          "-print_row(\"LIBERO-Long\", \"VLA-only\", vla_long)",
          "+print_summary_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)",
          "+print_summary_row(\"LIBERO-Long\", \"VLA-only\", vla_long, is_vla=True)",
          " print()",
          "-print_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)",
          "-print_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal)",
          "+print_summary_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)",
          "+print_summary_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal, is_vla=True)",
          " print()",
          "-print_row(\"LIBERO-Object\", \"CRM norm01\", crm_object_norm01)",
          "-print_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object_norm02)",
          "-print_row(\"LIBERO-Object\", \"CRM norm02 K=5\", crm_object_norm02_k5)",
          "-print_row(\"LIBERO-Object\", \"VLA-only\", vla_object)",
          "-print_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)",
          "-print_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)",
          "-print_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)",
          "+print_summary_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object)",
          "+print_summary_row(\"LIBERO-Object\", \"CRM norm01 (supp)\", crm_object_norm01)",
          "+print_summary_row(\"LIBERO-Object\", \"CRM norm02 K=5 (supp)\", crm_object_k5)",
          "+print_summary_row(\"LIBERO-Object\", \"VLA-only\", vla_object, is_vla=True)",
          "+print_summary_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)",
          "+print_summary_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)",
          "+print_summary_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)",
          " ",
          " # ============================================================================",
          "-# 8. KEY FINDINGS",
          "+# 8. KEY SIGNIFICANCE RESULTS",
          " # ============================================================================",
          " print(\"\\n\")",
          " print_separator()"
        ]
      },
      {
        "oldStart": 279,
        "oldLines": 13,
        "newStart": 240,
        "newLines": 15,
        "lines": [
          " print_separator()",
          " ",
          " tests = [",
          "-    (\"Spatial: CRM vs VLA\", crm_spatial_all, vla_spatial),",
          "+    (\"Spatial: CRM vs VLA\", crm_spatial, vla_spatial),",
          "     (\"Long: CRM vs VLA\", crm_long, vla_long),",
          "     (\"Goal: CRM vs VLA\", crm_goal, vla_goal),",
          "-    (\"Object(norm01): CRM vs VLA\", crm_object_norm01, vla_object),",
          "-    (\"Object(norm02): CRM vs VLA\", crm_object_norm02, vla_object),",
          "+    (\"Object(norm02): CRM vs VLA\", crm_object, vla_object),",
          "+    (\"Object(norm01-supp): CRM vs VLA\", crm_object_norm01, vla_object),",
          "     (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),",
          "-    (\"Object: CRM-norm01 vs Argmin-K10\", crm_object_norm01, argmin_object_k10),",
          "+    (\"Object: CRM-norm02 vs Argmin-K10\", crm_object, argmin_object_k10),",
          "+    (\"Object: Adaptive-K vs VLA\", all_adaptive, vla_object),",
          "+    (\"Object: CRM-norm02 vs Adaptive-K\", crm_object, all_adaptive),",
          " ]",
          " ",
          " print(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")"
        ]
      },
      {
        "oldStart": 301,
        "oldLines": 6,
        "newStart": 264,
        "newLines": 20,
        "lines": [
          "     sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'",
          "     print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")",
          " ",
          "+# ============================================================================",
          "+# 9. VERIFICATION NOTES",
          "+# ============================================================================",
          "+print(\"\\n\")",
          "+print_separator()",
          "+print(\"VERIFICATION NOTES\")",
          "+print_separator()",
          "+print(\"- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\")",
          "+print(\"  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\")",
          "+print(\"  Registry value retained but unverified.\")",
          "+print(\"- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\")",
          "+print(\"- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\")",
          "+print(\"- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\")",
          "+",
          " print(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")",
          " print()",
          " print_separator()"
        ]
      }
    ],
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nStatistical analysis of ACR-VLA Conformal Refinement experiments.\nCompares CRM (obs_only) vs VLA-only baselines across LIBERO benchmarks.\nAlso includes Argmin and Adaptive-K baselines.\n\"\"\"\n\nimport numpy as np\nfrom scipy import stats\n\ndef print_separator(char='=', width=80):\n    print(char * width)\n\ndef print_group_stats(name, values):\n    \"\"\"Print mean +/- std for a group.\"\"\"\n    arr = np.array(values)\n    print(f\"  {name}: n={len(arr)}, mean={arr.mean():.4f}, std={arr.std(ddof=1):.4f}, \"\n          f\"min={arr.min():.4f}, max={arr.max():.4f}\")\n    print(f\"    values: {[round(v, 4) for v in values]}\")\n\ndef run_tests(name_a, vals_a, name_b, vals_b):\n    \"\"\"Run t-test and Mann-Whitney U test between two groups.\"\"\"\n    a = np.array(vals_a)\n    b = np.array(vals_b)\n\n    # Independent two-sample t-test (Welch's, unequal variance)\n    t_stat, t_pval = stats.ttest_ind(a, b, equal_var=False)\n\n    # Mann-Whitney U test (non-parametric)\n    u_stat, u_pval = stats.mannwhitneyu(a, b, alternative='two-sided')\n\n    # Effect size: Cohen's d\n    pooled_std = np.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    cohens_d = (a.mean() - b.mean()) / pooled_std if pooled_std > 0 else float('inf')\n\n    # Difference\n    diff = a.mean() - b.mean()\n    diff_pct = diff * 100  # percentage points\n\n    print(f\"\\n  {name_a} vs {name_b}:\")\n    print(f\"    Difference: {diff:+.4f} ({diff_pct:+.2f} pp)\")\n    print(f\"    Welch's t-test: t={t_stat:.4f}, p={t_pval:.6f} {'***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Mann-Whitney U: U={u_stat:.1f}, p={u_pval:.6f} {'***' if u_pval < 0.001 else '**' if u_pval < 0.01 else '*' if u_pval < 0.05 else 'n.s.'}\")\n    print(f\"    Cohen's d: {cohens_d:.4f} ({'large' if abs(cohens_d) > 0.8 else 'medium' if abs(cohens_d) > 0.5 else 'small' if abs(cohens_d) > 0.2 else 'negligible'})\")\n\n    return t_pval, u_pval\n\n# ============================================================================\n# DATA FROM REGISTRY (verified from all experiments with conclusion=success)\n# ============================================================================\n\n# --- LIBERO-Spatial ---\n# CRM obs_only (norm02 variants, K=5 and K=10): seeds 42-48\n# From registry: seed42=0.35, seed43=0.32(k5) or 0.34(norm02-r2), seed44=0.37(k5-r2) or 0.36(norm02),\n# seed45=0.34(k5-r2) or 0.34(norm02), seed46=0.33(r2), seed47=0.32(norm02), seed48=0.35(norm02 and crm-spatial)\n# Using the best-matched K=10 norm02 experiments (primary config):\ncrm_spatial = [0.34, 0.36, 0.34, 0.33, 0.32, 0.35]  # seeds 43-r2, 44, 45, 46-r2, 47, 48\n# K=5 variants:\ncrm_spatial_k5 = [0.35, 0.32, 0.37, 0.34]  # seeds 42, 43, 44-r2, 45-r2\n# Combined unique seeds (using K=10 when available, K=5 for seed42):\ncrm_spatial_all = [0.35, 0.34, 0.36, 0.34, 0.33, 0.32, 0.35]  # seeds 42(k5), 43-r2, 44, 45, 46-r2, 47, 48\n# Fallback from user-provided data (n=8):\ncrm_spatial_user = [0.32, 0.34, 0.36, 0.34, 0.34, 0.33, 0.32, 0.35]\n\n# VLA-only Spatial: seeds 42-50\nvla_spatial = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30]  # seeds 42, 43, 44, 45, 46, 47, 50\n# Fallback from user-provided data (n=9):\nvla_spatial_user = [0.30, 0.29, 0.31, 0.27, 0.30, 0.30, 0.30, 0.30, 0.29]\n\n# --- LIBERO-Long ---\n# CRM obs_only Long: seeds 42-47\ncrm_long = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]  # seeds 42, 43, 44, 45, 46, 47\n# User-provided (same):\ncrm_long_user = [0.17, 0.15, 0.20, 0.18, 0.18, 0.17]\n\n# VLA-only Long: seeds 42-48\nvla_long = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]  # seeds 42, 43, 44, 45, 46, 47, 48\n# User-provided (n=7):\nvla_long_user = [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.11]\n\n# --- LIBERO-Goal ---\n# CRM obs_only Goal: seeds 42-46\ncrm_goal = [0.67, 0.72, 0.64, 0.65, 0.72]  # seeds 42, 43, 44-r2, 45-r2, 46\n# User-provided (same):\ncrm_goal_user = [0.67, 0.72, 0.64, 0.65, 0.72]\n\n# VLA-only Goal: seeds 42-46\nvla_goal = [0.71, 0.69, 0.73, 0.63, 0.71]  # seeds 42, 43, 44-r2, 45, 46\n# User-provided (same):\nvla_goal_user = [0.71, 0.69, 0.73, 0.63, 0.71]\n\n# --- LIBERO-Object ---\n# CRM obs_only Object (norm02, K=10): seeds from registry\n# Using norm02 K=10 results: seed43-r2=0.16, seed44-r2=0.16, seed45=0.16, seed46=0.15, seed47=0.20, seed48-r2=0.18\n# Using norm01 results: seed42=0.19, seed44=0.16, seed45-r2=0.17, seed46-r3=0.18, seed47=0.17, seed48=0.18\n# Using norm02 K=5 results: seed42=0.14, seed43=0.19, seed44=0.17, seed45=0.15, seed46=0.16, seed47=0.13, seed48=0.18\n# We'll use norm01 as the primary CRM config (best performing, consistent config):\ncrm_object_norm01 = [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]  # seeds 42, 44, 45-r2, 46-r3, 47, 48\n# norm02 K=10:\ncrm_object_norm02 = [0.16, 0.16, 0.16, 0.15, 0.20, 0.18]  # seeds 43-r2, 44-r2, 45, 46, 47, 48-r2\n# norm02 K=5:\ncrm_object_norm02_k5 = [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]  # seeds 42-48\n\n# VLA-only Object: from registry\n# seed42=0.12 (overall_sr), seed43=0.12 (overall_sr), seed44-r2=0.10, seed45=0.09(overall_sr),\n# seed45-r2=0.11, seed46=0.13, seed47=0.10, seed48=0.10, seed50=0.09\nvla_object = [0.12, 0.12, 0.10, 0.09, 0.13, 0.10, 0.10, 0.09]  # seeds 42, 43, 44-r2, 45, 46, 47, 48, 50\n# Using seed45-r2 instead of seed45 (more recent run):\nvla_object_alt = [0.12, 0.12, 0.10, 0.11, 0.13, 0.10, 0.10, 0.09]\n\n# --- Argmin Object ---\n# K=10: seed43=0.17, seed44-r2=0.13, seed45=0.12, seed46=0.10, seed47=0.10\nargmin_object_k10 = [0.17, 0.13, 0.12, 0.10, 0.10]\n# K=5: seed42=0.15, seed43=0.13, seed44-r2=0.11, seed45=0.13\nargmin_object_k5 = [0.15, 0.13, 0.11, 0.13]\n\n# Argmin Spatial (only 1 data point from registry)\nargmin_spatial = [0.34]\n\n# --- Adaptive-K Object ---\n# p25: seed42=0.15, seed43=0.13\nadaptive_k_p25 = [0.15, 0.13]\n# p50: seed42=0.16, seed43=0.16, seed44=0.14\nadaptive_k_p50 = [0.16, 0.16, 0.14]\n# p75: seed42=0.12, seed43=0.13, seed44=0.16\nadaptive_k_p75 = [0.12, 0.13, 0.16]\n# p90: seed42=0.12, seed43=0.14, seed44=0.14\nadaptive_k_p90 = [0.12, 0.14, 0.14]\n\n\n# ============================================================================\n# ANALYSIS\n# ============================================================================\n\nprint_separator()\nprint(\"STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\")\nprint(\"All success rates are fractions (0.0 to 1.0)\")\nprint_separator()\n\n# ============================================================================\n# 1. LIBERO-SPATIAL: CRM vs VLA-only\n# ============================================================================\nprint(\"\\n1. LIBERO-SPATIAL\")\nprint_separator('-')\nprint(\"\\n  [Registry data]\")\nprint_group_stats(\"CRM obs_only (registry, n=7)\", crm_spatial_all)\nprint_group_stats(\"VLA-only (registry, n=7)\", vla_spatial)\nrun_tests(\"CRM\", crm_spatial_all, \"VLA-only\", vla_spatial)\n\nprint(\"\\n  [User-provided data]\")\nprint_group_stats(\"CRM obs_only (user, n=8)\", crm_spatial_user)\nprint_group_stats(\"VLA-only (user, n=9)\", vla_spatial_user)\nrun_tests(\"CRM\", crm_spatial_user, \"VLA-only\", vla_spatial_user)\n\n# ============================================================================\n# 2. LIBERO-LONG: CRM vs VLA-only\n# ============================================================================\nprint(\"\\n\\n2. LIBERO-LONG\")\nprint_separator('-')\nprint(\"\\n  [Registry data]\")\nprint_group_stats(\"CRM obs_only (registry, n=6)\", crm_long)\nprint_group_stats(\"VLA-only (registry, n=7)\", vla_long)\nrun_tests(\"CRM\", crm_long, \"VLA-only\", vla_long)\n\nprint(\"\\n  [User-provided data]\")\nprint_group_stats(\"CRM obs_only (user, n=6)\", crm_long_user)\nprint_group_stats(\"VLA-only (user, n=7)\", vla_long_user)\nrun_tests(\"CRM\", crm_long_user, \"VLA-only\", vla_long_user)\n\n# ============================================================================\n# 3. LIBERO-GOAL: CRM vs VLA-only\n# ============================================================================\nprint(\"\\n\\n3. LIBERO-GOAL\")\nprint_separator('-')\nprint(\"\\n  [Registry data = User-provided data]\")\nprint_group_stats(\"CRM obs_only (n=5)\", crm_goal)\nprint_group_stats(\"VLA-only (n=5)\", vla_goal)\nrun_tests(\"CRM\", crm_goal, \"VLA-only\", vla_goal)\n\n# ============================================================================\n# 4. LIBERO-OBJECT: CRM vs VLA-only\n# ============================================================================\nprint(\"\\n\\n4. LIBERO-OBJECT\")\nprint_separator('-')\n\nprint(\"\\n  [CRM norm01 config]\")\nprint_group_stats(\"CRM obs_only norm01 (n=6)\", crm_object_norm01)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm01\", crm_object_norm01, \"VLA-only\", vla_object)\n\nprint(\"\\n  [CRM norm02 K=10 config]\")\nprint_group_stats(\"CRM obs_only norm02 K=10 (n=6)\", crm_object_norm02)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02\", crm_object_norm02, \"VLA-only\", vla_object)\n\nprint(\"\\n  [CRM norm02 K=5 config]\")\nprint_group_stats(\"CRM obs_only norm02 K=5 (n=7)\", crm_object_norm02_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nrun_tests(\"CRM norm02 K=5\", crm_object_norm02_k5, \"VLA-only\", vla_object)\n\n# ============================================================================\n# 5. ARGMIN BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n5. ARGMIN BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Argmin K=10 (n=5)\", argmin_object_k10)\nprint_group_stats(\"Argmin K=5 (n=4)\", argmin_object_k5)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm01 (n=6)\", crm_object_norm01)\n\nprint(\"\\n  Argmin K=10 vs VLA-only:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"VLA-only\", vla_object)\nprint(\"\\n  Argmin K=10 vs CRM norm01:\")\nrun_tests(\"Argmin K=10\", argmin_object_k10, \"CRM norm01\", crm_object_norm01)\n\n# ============================================================================\n# 6. ADAPTIVE-K BASELINES (Object)\n# ============================================================================\nprint(\"\\n\\n6. ADAPTIVE-K BASELINES (Object)\")\nprint_separator('-')\nprint_group_stats(\"Adaptive-K p25 (n=2)\", adaptive_k_p25)\nprint_group_stats(\"Adaptive-K p50 (n=3)\", adaptive_k_p50)\nprint_group_stats(\"Adaptive-K p75 (n=3)\", adaptive_k_p75)\nprint_group_stats(\"Adaptive-K p90 (n=3)\", adaptive_k_p90)\nall_adaptive = adaptive_k_p25 + adaptive_k_p50 + adaptive_k_p75 + adaptive_k_p90\nprint_group_stats(\"Adaptive-K all (n=11)\", all_adaptive)\nprint_group_stats(\"VLA-only (n=8)\", vla_object)\nprint_group_stats(\"CRM norm01 (n=6)\", crm_object_norm01)\n\nprint(\"\\n  Adaptive-K (all) vs VLA-only:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"VLA-only\", vla_object)\nprint(\"\\n  Adaptive-K (all) vs CRM norm01:\")\nrun_tests(\"Adaptive-K all\", all_adaptive, \"CRM norm01\", crm_object_norm01)\n\n# ============================================================================\n# 7. SUMMARY TABLE\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"SUMMARY TABLE\")\nprint_separator()\nprint(f\"{'Benchmark':<18} {'Method':<22} {'n':>3} {'Mean':>7} {'Std':>7} {'95% CI':>15}\")\nprint_separator('-')\n\ndef print_row(bench, method, vals):\n    arr = np.array(vals)\n    n = len(arr)\n    mean = arr.mean()\n    std = arr.std(ddof=1)\n    se = std / np.sqrt(n)\n    ci_lo = mean - 1.96 * se\n    ci_hi = mean + 1.96 * se\n    print(f\"{bench:<18} {method:<22} {n:>3} {mean:>7.4f} {std:>7.4f} [{ci_lo:.4f}, {ci_hi:.4f}]\")\n\nprint_row(\"LIBERO-Spatial\", \"CRM obs_only\", crm_spatial_all)\nprint_row(\"LIBERO-Spatial\", \"VLA-only\", vla_spatial)\nprint()\nprint_row(\"LIBERO-Long\", \"CRM obs_only\", crm_long)\nprint_row(\"LIBERO-Long\", \"VLA-only\", vla_long)\nprint()\nprint_row(\"LIBERO-Goal\", \"CRM obs_only\", crm_goal)\nprint_row(\"LIBERO-Goal\", \"VLA-only\", vla_goal)\nprint()\nprint_row(\"LIBERO-Object\", \"CRM norm01\", crm_object_norm01)\nprint_row(\"LIBERO-Object\", \"CRM norm02 K=10\", crm_object_norm02)\nprint_row(\"LIBERO-Object\", \"CRM norm02 K=5\", crm_object_norm02_k5)\nprint_row(\"LIBERO-Object\", \"VLA-only\", vla_object)\nprint_row(\"LIBERO-Object\", \"Argmin K=10\", argmin_object_k10)\nprint_row(\"LIBERO-Object\", \"Argmin K=5\", argmin_object_k5)\nprint_row(\"LIBERO-Object\", \"Adaptive-K (all)\", all_adaptive)\n\n# ============================================================================\n# 8. KEY FINDINGS\n# ============================================================================\nprint(\"\\n\")\nprint_separator()\nprint(\"KEY SIGNIFICANCE RESULTS\")\nprint_separator()\n\ntests = [\n    (\"Spatial: CRM vs VLA\", crm_spatial_all, vla_spatial),\n    (\"Long: CRM vs VLA\", crm_long, vla_long),\n    (\"Goal: CRM vs VLA\", crm_goal, vla_goal),\n    (\"Object(norm01): CRM vs VLA\", crm_object_norm01, vla_object),\n    (\"Object(norm02): CRM vs VLA\", crm_object_norm02, vla_object),\n    (\"Object: Argmin-K10 vs VLA\", argmin_object_k10, vla_object),\n    (\"Object: CRM-norm01 vs Argmin-K10\", crm_object_norm01, argmin_object_k10),\n]\n\nprint(f\"\\n{'Comparison':<40} {'Diff':>7} {'t-test p':>10} {'MW-U p':>10} {'Sig':>5} {'Cohen d':>9}\")\nprint('-' * 85)\nfor name, a, b in tests:\n    arr_a, arr_b = np.array(a), np.array(b)\n    diff = arr_a.mean() - arr_b.mean()\n    t_stat, t_pval = stats.ttest_ind(arr_a, arr_b, equal_var=False)\n    u_stat, u_pval = stats.mannwhitneyu(arr_a, arr_b, alternative='two-sided')\n    pooled_std = np.sqrt(((len(a)-1)*arr_a.std(ddof=1)**2 + (len(b)-1)*arr_b.std(ddof=1)**2) /\n                         (len(a) + len(b) - 2))\n    d = diff / pooled_std if pooled_std > 0 else float('inf')\n    sig = '***' if t_pval < 0.001 else '**' if t_pval < 0.01 else '*' if t_pval < 0.05 else 'n.s.'\n    print(f\"{name:<40} {diff:>+.4f} {t_pval:>10.6f} {u_pval:>10.6f} {sig:>5} {d:>+9.4f}\")\n\nprint(\"\\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\")\nprint()\nprint_separator()\nprint(\"END OF ANALYSIS\")\nprint_separator()\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 117_

Now running the script and saving output.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "d8b961c8-3695-4b5a-b892-d43e118f3de2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqaaV8C9QfKJsAzTK1S71e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5903,
      "cache_read_input_tokens": 64270,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5903
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

_source line 118_

<details open><summary>🔧 Tool call — Bash · `toolu_01P6AmmQ8fNbXdkZRZdQUZCx`</summary>

```json
{
  "command": "python3 artifacts/statistical_analysis.py 2>&1 | tee artifacts/statistical_analysis_output.txt",
  "description": "Run statistical analysis script and save output",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "138631a4-5216-4860-8aa5-efd28adbd021",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RqaaV8C9QfKJsAzTK1S71e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5903,
      "cache_read_input_tokens": 64270,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5903
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

_source line 119 · 2026-05-20T05:02:14.605Z_

<details><summary>↩ Tool result · `toolu_01P6AmmQ8fNbXdkZRZdQUZCx`</summary>

```text
================================================================================
STATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments
All success rates are fractions (0.0 to 1.0)
Object benchmark primary CRM config: norm02 (ε=0.2), K=10
================================================================================

1. LIBERO-SPATIAL
--------------------------------------------------------------------------------
  CRM obs_only (n=6): n=6, mean=0.3433, std=0.0137, min=0.3200, max=0.3600
    values: [0.35, 0.34, 0.36, 0.34, 0.32, 0.35]
  VLA-only (n=9): n=9, mean=0.2956, std=0.0113, min=0.2700, max=0.3100
    values: [0.3, 0.29, 0.31, 0.27, 0.3, 0.3, 0.3, 0.29, 0.3]

  CRM vs VLA-only:
    Difference: +0.0478 (+4.78 pp)
    Welch's t-test: t=7.0980, p=0.000046 ***
    Mann-Whitney U: U=54.0, p=0.001426 **
    Cohen's d: 3.8955 (large)


2. LIBERO-LONG
--------------------------------------------------------------------------------
  CRM obs_only (n=6): n=6, mean=0.1750, std=0.0164, min=0.1500, max=0.2000
    values: [0.17, 0.15, 0.2, 0.18, 0.18, 0.17]
  VLA-only (n=7): n=7, mean=0.1414, std=0.0254, min=0.1100, max=0.1800
    values: [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]

  CRM vs VLA-only:
    Difference: +0.0336 (+3.36 pp)
    Welch's t-test: t=2.8628, p=0.016373 *
    Mann-Whitney U: U=36.0, p=0.035947 *
    Cohen's d: 1.5388 (large)


3. LIBERO-GOAL
--------------------------------------------------------------------------------
  CRM obs_only (n=6): n=6, mean=0.6817, std=0.0343, min=0.6400, max=0.7200
    values: [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]
  VLA-only (n=5): n=5, mean=0.6940, std=0.0385, min=0.6300, max=0.7300
    values: [0.71, 0.69, 0.73, 0.63, 0.71]

  CRM vs VLA-only:
    Difference: -0.0123 (-1.23 pp)
    Welch's t-test: t=-0.5560, p=0.593106 n.s.
    Mann-Whitney U: U=12.5, p=0.713124 n.s.
    Cohen's d: -0.3406 (small)


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
  VLA-only (n=8): n=8, mean=0.1088, std=0.0136, min=0.0900, max=0.1300
    values: [0.12, 0.12, 0.1, 0.11, 0.13, 0.1, 0.1, 0.09]
  CRM norm02 K=10 (n=6): n=6, mean=0.1683, std=0.0183, min=0.1500, max=0.2000
    values: [0.16, 0.16, 0.16, 0.15, 0.2, 0.18]

  Adaptive-K (all) vs VLA-only:

  Adaptive-K all vs VLA-only:
    Difference: +0.0322 (+3.22 pp)
    Welch's t-test: t=4.8583, p=0.000170 ***
    Mann-Whitney U: U=83.0, p=0.001300 **
    Cohen's d: 2.2166 (large)

  Adaptive-K (all) vs CRM norm02 K=10:

  Adaptive-K all vs CRM norm02:
    Difference: -0.0274 (-2.74 pp)
    Welch's t-test: t=-3.1266, p=0.012535 *
    Mann-Whitney U: U=8.0, p=0.011463 *
    Cohen's d: -1.6848 (large)


================================================================================
SUMMARY TABLE
================================================================================
Benchmark          Method                   n    Mean     Std  Δ vs VLA    p-value   Sig
--------------------------------------------------------------------------------
LIBERO-Spatial     CRM obs_only             6  0.3433  0.0137   +0.0478   0.000046   ***
LIBERO-Spatial     VLA-only                 9  0.2956  0.0113         —          —     —

LIBERO-Long        CRM obs_only             6  0.1750  0.0164   +0.0336   0.016373     *
LIBERO-Long        VLA-only                 7  0.1414  0.0254         —          —     —

LIBERO-Goal        CRM obs_only             6  0.6817  0.0343   -0.0123   0.593106  n.s.
LIBERO-Goal        VLA-only                 5  0.6940  0.0385         —          —     —

LIBERO-Object      CRM norm02 K=10          6  0.1683  0.0183   +0.0596   0.000095   ***
LIBERO-Object      CRM norm01 (supp)        6  0.1750  0.0105   +0.0663   0.000000   ***
LIBERO-Object      CRM norm02 K=5 (supp)    7  0.1600  0.0216   +0.0512   0.000312   ***
LIBERO-Object      VLA-only                 8  0.1088  0.0136         —          —     —
LIBERO-Object      Argmin K=10              5  0.1240  0.0288   +0.0152   0.316589  n.s.
LIBERO-Object      Argmin K=5               4  0.1300  0.0163   +0.0212   0.073136  n.s.
LIBERO-Object      Adaptive-K (all)        11  0.1409  0.0151   +0.0322   0.000170   ***


================================================================================
KEY SIGNIFICANCE RESULTS
================================================================================

Comparison                                  Diff   t-test p     MW-U p   Sig   Cohen d
-------------------------------------------------------------------------------------
Spatial: CRM vs VLA                      +0.0478   0.000046   0.001426   ***   +3.8955
Long: CRM vs VLA                         +0.0336   0.016373   0.035947     *   +1.5388
Goal: CRM vs VLA                         -0.0123   0.593106   0.713124  n.s.   -0.3406
Object(norm02): CRM vs VLA               +0.0596   0.000095   0.002182   ***   +3.7868
Object(norm01-supp): CRM vs VLA          +0.0663   0.000000   0.002232   ***   +5.3538
Object: Argmin-K10 vs VLA                +0.0152   0.316589   0.362759  n.s.   +0.7451
Object: CRM-norm02 vs Argmin-K10         +0.0443   0.022297   0.052478     *   +1.8803
Object: Adaptive-K vs VLA                +0.0322   0.000170   0.001300   ***   +2.2166
Object: CRM-norm02 vs Adaptive-K         +0.0274   0.012535   0.011463     *   +1.6848


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
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "e7aae686-edd1-4e7a-8946-b4550930f1f8",
  "tool_use_result": {
    "stdout": "================================================================================\nSTATISTICAL ANALYSIS: ACR-VLA Conformal Refinement Experiments\nAll success rates are fractions (0.0 to 1.0)\nObject benchmark primary CRM config: norm02 (ε=0.2), K=10\n================================================================================\n\n1. LIBERO-SPATIAL\n--------------------------------------------------------------------------------\n  CRM obs_only (n=6): n=6, mean=0.3433, std=0.0137, min=0.3200, max=0.3600\n    values: [0.35, 0.34, 0.36, 0.34, 0.32, 0.35]\n  VLA-only (n=9): n=9, mean=0.2956, std=0.0113, min=0.2700, max=0.3100\n    values: [0.3, 0.29, 0.31, 0.27, 0.3, 0.3, 0.3, 0.29, 0.3]\n\n  CRM vs VLA-only:\n    Difference: +0.0478 (+4.78 pp)\n    Welch's t-test: t=7.0980, p=0.000046 ***\n    Mann-Whitney U: U=54.0, p=0.001426 **\n    Cohen's d: 3.8955 (large)\n\n\n2. LIBERO-LONG\n--------------------------------------------------------------------------------\n  CRM obs_only (n=6): n=6, mean=0.1750, std=0.0164, min=0.1500, max=0.2000\n    values: [0.17, 0.15, 0.2, 0.18, 0.18, 0.17]\n  VLA-only (n=7): n=7, mean=0.1414, std=0.0254, min=0.1100, max=0.1800\n    values: [0.11, 0.13, 0.12, 0.17, 0.18, 0.14, 0.14]\n\n  CRM vs VLA-only:\n    Difference: +0.0336 (+3.36 pp)\n    Welch's t-test: t=2.8628, p=0.016373 *\n    Mann-Whitney U: U=36.0, p=0.035947 *\n    Cohen's d: 1.5388 (large)\n\n\n3. LIBERO-GOAL\n--------------------------------------------------------------------------------\n  CRM obs_only (n=6): n=6, mean=0.6817, std=0.0343, min=0.6400, max=0.7200\n    values: [0.67, 0.72, 0.64, 0.65, 0.72, 0.69]\n  VLA-only (n=5): n=5, mean=0.6940, std=0.0385, min=0.6300, max=0.7300\n    values: [0.71, 0.69, 0.73, 0.63, 0.71]\n\n  CRM vs VLA-only:\n    Difference: -0.0123 (-1.23 pp)\n    Welch's t-test: t=-0.5560, p=0.593106 n.s.\n    Mann-Whitney U: U=12.5, p=0.713124 n.s.\n    Cohen's d: -0.3406 (small)\n\n\n4. LIBERO-OBJECT\n--------------------------------------------------------------------------------\n\n  [PRIMARY: CRM norm02 K=10]\n  CRM obs_only norm02 K=10 (n=6): n=6, mean=0.1683, std=0.0183, min=0.1500, max=0.2000\n    values: [0.16, 0.16, 0.16, 0.15, 0.2, 0.18]\n  VLA-only (n=8): n=8, mean=0.1088, std=0.0136, min=0.0900, max=0.1300\n    values: [0.12, 0.12, 0.1, 0.11, 0.13, 0.1, 0.1, 0.09]\n\n  CRM norm02 K=10 vs VLA-only:\n    Difference: +0.0596 (+5.96 pp)\n    Welch's t-test: t=6.6993, p=0.000095 ***\n    Mann-Whitney U: U=48.0, p=0.002182 **\n    Cohen's d: 3.7868 (large)\n\n  [Supplementary: CRM norm01]\n  CRM obs_only norm01 (n=6): n=6, mean=0.1750, std=0.0105, min=0.1600, max=0.1900\n    values: [0.19, 0.16, 0.17, 0.18, 0.17, 0.18]\n\n  CRM norm01 vs VLA-only:\n    Difference: +0.0663 (+6.62 pp)\n    Welch's t-test: t=10.3058, p=0.000000 ***\n    Mann-Whitney U: U=48.0, p=0.002232 **\n    Cohen's d: 5.3538 (large)\n\n  [Supplementary: CRM norm02 K=5]\n  CRM obs_only norm02 K=5 (n=7): n=7, mean=0.1600, std=0.0216, min=0.1300, max=0.1900\n    values: [0.14, 0.19, 0.17, 0.15, 0.16, 0.13, 0.18]\n\n  CRM norm02 K=5 vs VLA-only:\n    Difference: +0.0512 (+5.12 pp)\n    Welch's t-test: t=5.4125, p=0.000312 ***\n    Mann-Whitney U: U=55.5, p=0.001681 **\n    Cohen's d: 2.8903 (large)\n\n\n5. ARGMIN BASELINES (Object)\n--------------------------------------------------------------------------------\n  Argmin K=10 (n=5): n=5, mean=0.1240, std=0.0288, min=0.1000, max=0.1700\n    values: [0.17, 0.13, 0.12, 0.1, 0.1]\n  Argmin K=5 (n=4): n=4, mean=0.1300, std=0.0163, min=0.1100, max=0.1500\n    values: [0.15, 0.13, 0.11, 0.13]\n  VLA-only (n=8): n=8, mean=0.1088, std=0.0136, min=0.0900, max=0.1300\n    values: [0.12, 0.12, 0.1, 0.11, 0.13, 0.1, 0.1, 0.09]\n  CRM norm02 K=10 (n=6): n=6, mean=0.1683, std=0.0183, min=0.1500, max=0.2000\n    values: [0.16, 0.16, 0.16, 0.15, 0.2, 0.18]\n\n  Argmin K=10 vs VLA-only:\n\n  Argmin K=10 vs VLA-only:\n    Difference: +0.0152 (+1.52 pp)\n    Welch's t-test: t=1.1093, p=0.316589 n.s.\n    Mann-Whitney U: U=26.5, p=0.362759 n.s.\n    Cohen's d: 0.7451 (medium)\n\n  Argmin K=10 vs CRM norm02 K=10:\n\n  Argmin K=10 vs CRM norm02:\n    Difference: -0.0443 (-4.43 pp)\n    Welch's t-test: t=-2.9747, p=0.022297 *\n    Mann-Whitney U: U=4.0, p=0.052478 n.s.\n    Cohen's d: -1.8803 (large)\n\n\n6. ADAPTIVE-K BASELINES (Object)\n--------------------------------------------------------------------------------\n  Adaptive-K p25 (n=2): n=2, mean=0.1400, std=0.0141, min=0.1300, max=0.1500\n    values: [0.15, 0.13]\n  Adaptive-K p50 (n=3): n=3, mean=0.1533, std=0.0115, min=0.1400, max=0.1600\n    values: [0.16, 0.16, 0.14]\n  Adaptive-K p75 (n=3): n=3, mean=0.1367, std=0.0208, min=0.1200, max=0.1600\n    values: [0.12, 0.13, 0.16]\n  Adaptive-K p90 (n=3): n=3, mean=0.1333, std=0.0115, min=0.1200, max=0.1400\n    values: [0.12, 0.14, 0.14]\n  Adaptive-K all (n=11): n=11, mean=0.1409, std=0.0151, min=0.1200, max=0.1600\n    values: [0.15, 0.13, 0.16, 0.16, 0.14, 0.12, 0.13, 0.16, 0.12, 0.14, 0.14]\n  VLA-only (n=8): n=8, mean=0.1088, std=0.0136, min=0.0900, max=0.1300\n    values: [0.12, 0.12, 0.1, 0.11, 0.13, 0.1, 0.1, 0.09]\n  CRM norm02 K=10 (n=6): n=6, mean=0.1683, std=0.0183, min=0.1500, max=0.2000\n    values: [0.16, 0.16, 0.16, 0.15, 0.2, 0.18]\n\n  Adaptive-K (all) vs VLA-only:\n\n  Adaptive-K all vs VLA-only:\n    Difference: +0.0322 (+3.22 pp)\n    Welch's t-test: t=4.8583, p=0.000170 ***\n    Mann-Whitney U: U=83.0, p=0.001300 **\n    Cohen's d: 2.2166 (large)\n\n  Adaptive-K (all) vs CRM norm02 K=10:\n\n  Adaptive-K all vs CRM norm02:\n    Difference: -0.0274 (-2.74 pp)\n    Welch's t-test: t=-3.1266, p=0.012535 *\n    Mann-Whitney U: U=8.0, p=0.011463 *\n    Cohen's d: -1.6848 (large)\n\n\n================================================================================\nSUMMARY TABLE\n================================================================================\nBenchmark          Method                   n    Mean     Std  Δ vs VLA    p-value   Sig\n--------------------------------------------------------------------------------\nLIBERO-Spatial     CRM obs_only             6  0.3433  0.0137   +0.0478   0.000046   ***\nLIBERO-Spatial     VLA-only                 9  0.2956  0.0113         —          —     —\n\nLIBERO-Long        CRM obs_only             6  0.1750  0.0164   +0.0336   0.016373     *\nLIBERO-Long        VLA-only                 7  0.1414  0.0254         —          —     —\n\nLIBERO-Goal        CRM obs_only             6  0.6817  0.0343   -0.0123   0.593106  n.s.\nLIBERO-Goal        VLA-only                 5  0.6940  0.0385         —          —     —\n\nLIBERO-Object      CRM norm02 K=10          6  0.1683  0.0183   +0.0596   0.000095   ***\nLIBERO-Object      CRM norm01 (supp)        6  0.1750  0.0105   +0.0663   0.000000   ***\nLIBERO-Object      CRM norm02 K=5 (supp)    7  0.1600  0.0216   +0.0512   0.000312   ***\nLIBERO-Object      VLA-only                 8  0.1088  0.0136         —          —     —\nLIBERO-Object      Argmin K=10              5  0.1240  0.0288   +0.0152   0.316589  n.s.\nLIBERO-Object      Argmin K=5               4  0.1300  0.0163   +0.0212   0.073136  n.s.\nLIBERO-Object      Adaptive-K (all)        11  0.1409  0.0151   +0.0322   0.000170   ***\n\n\n================================================================================\nKEY SIGNIFICANCE RESULTS\n================================================================================\n\nComparison                                  Diff   t-test p     MW-U p   Sig   Cohen d\n-------------------------------------------------------------------------------------\nSpatial: CRM vs VLA                      +0.0478   0.000046   0.001426   ***   +3.8955\nLong: CRM vs VLA                         +0.0336   0.016373   0.035947     *   +1.5388\nGoal: CRM vs VLA                         -0.0123   0.593106   0.713124  n.s.   -0.3406\nObject(norm02): CRM vs VLA               +0.0596   0.000095   0.002182   ***   +3.7868\nObject(norm01-supp): CRM vs VLA          +0.0663   0.000000   0.002232   ***   +5.3538\nObject: Argmin-K10 vs VLA                +0.0152   0.316589   0.362759  n.s.   +0.7451\nObject: CRM-norm02 vs Argmin-K10         +0.0443   0.022297   0.052478     *   +1.8803\nObject: Adaptive-K vs VLA                +0.0322   0.000170   0.001300   ***   +2.2166\nObject: CRM-norm02 vs Adaptive-K         +0.0274   0.012535   0.011463     *   +1.6848\n\n\n================================================================================\nVERIFICATION NOTES\n================================================================================\n- Argmin K=10 seed43 = 0.17: severe outlier (other seeds 0.10-0.13).\n  Original JSON not found on any server (bjb2-40593, bjb2-28827, bjb1-18228, bjb1-32546).\n  Registry value retained but unverified.\n- VLA-only Long seed48 = 0.14: confirmed by registry (eval-vla-only-long-seed48).\n- CRM-Goal seed47 = 0.69: included per Director directive (not yet in registry).\n- VLA-Spatial seed48=0.30, seed49=0.29: included per Director directive.\n\nSignificance levels: *** p<0.001, ** p<0.01, * p<0.05, n.s. not significant\n\n================================================================================\nEND OF ANALYSIS\n================================================================================",
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

_source line 120_

Script ran successfully. Output saved to `artifacts/statistical_analysis_output.txt`.

---

## 修正后 Summary Table

| Benchmark | Method | n | Mean | Std | Δ vs VLA | p-value | Sig |
|---|---|---|---|---|---|---|---|
| LIBERO-Spatial | CRM obs_only | 6 | 0.3433 | 0.0137 | +0.0478 | 0.000046 | *** |
| LIBERO-Spatial | VLA-only | 9 | 0.2956 | 0.0113 | — | — | — |
| LIBERO-Long | CRM obs_only | 6 | 0.1750 | 0.0164 | +0.0336 | 0.016373 | * |
| LIBERO-Long | VLA-only | 7 | 0.1414 | 0.0254 | — | — | — |
| LIBERO-Goal | CRM obs_only | 6 | 0.6817 | 0.0343 | -0.0123 | 0.593106 | n.s. |
| LIBERO-Goal | VLA-only | 5 | 0.6940 | 0.0385 | — | — | — |
| LIBERO-Object | CRM norm02 K=10 | 6 | 0.1683 | 0.0183 | +0.0596 | 0.000095 | *** |
| LIBERO-Object | CRM norm01 (supp) | 6 | 0.1750 | 0.0105 | +0.0663 | <0.000001 | *** |
| LIBERO-Object | CRM norm02 K=5 (supp) | 7 | 0.1600 | 0.0216 | +0.0512 | 0.000312 | *** |
| LIBERO-Object | VLA-only | 8 | 0.1088 | 0.0136 | — | — | — |
| LIBERO-Object | Argmin K=10 | 5 | 0.1240 | 0.0288 | +0.0152 | 0.316589 | n.s. |
| LIBERO-Object | Argmin K=5 | 4 | 0.1300 | 0.0163 | +0.0212 | 0.073136 | n.s. |
| LIBERO-Object | Adaptive-K (all) | 11 | 0.1409 | 0.0151 | +0.0322 | 0.000170 | *** |

## 修正内容总结

1. **Object 主配置改为 norm02 (ε=0.2) K=10** — 所有 summary table 和 comparison 中 Object 的 CRM 用 `crm_object` (norm02 K=10)，norm01 降为 supplementary
2. **新增数据**: CRM-Goal seed47=0.69 (n:5→6), VLA-Spatial seed48=0.30/seed49=0.29/seed50=0.30 (n:7→9)
3. **VLA-Long seed48 = 0.14** 已确认
4. **Argmin K=10 seed43 = 0.17**: 在 4 台服务器均未找到原始 JSON，registry 值保留但标注为 unverified outlier

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "uuid": "1ba2be9a-2db2-4192-93c5-12f019ed716a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RK9eMQs5fKC1CgSHtUu1RA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4084,
      "cache_read_input_tokens": 70173,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4084
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

_source line 121_

Script ran successfully. Output saved to `artifacts/statistical_analysis_output.txt`.

---

## 修正后 Summary Table

| Benchmark | Method | n | Mean | Std | Δ vs VLA | p-value | Sig |
|---|---|---|---|---|---|---|---|
| LIBERO-Spatial | CRM obs_only | 6 | 0.3433 | 0.0137 | +0.0478 | 0.000046 | *** |
| LIBERO-Spatial | VLA-only | 9 | 0.2956 | 0.0113 | — | — | — |
| LIBERO-Long | CRM obs_only | 6 | 0.1750 | 0.0164 | +0.0336 | 0.016373 | * |
| LIBERO-Long | VLA-only | 7 | 0.1414 | 0.0254 | — | — | — |
| LIBERO-Goal | CRM obs_only | 6 | 0.6817 | 0.0343 | -0.0123 | 0.593106 | n.s. |
| LIBERO-Goal | VLA-only | 5 | 0.6940 | 0.0385 | — | — | — |
| LIBERO-Object | CRM norm02 K=10 | 6 | 0.1683 | 0.0183 | +0.0596 | 0.000095 | *** |
| LIBERO-Object | CRM norm01 (supp) | 6 | 0.1750 | 0.0105 | +0.0663 | <0.000001 | *** |
| LIBERO-Object | CRM norm02 K=5 (supp) | 7 | 0.1600 | 0.0216 | +0.0512 | 0.000312 | *** |
| LIBERO-Object | VLA-only | 8 | 0.1088 | 0.0136 | — | — | — |
| LIBERO-Object | Argmin K=10 | 5 | 0.1240 | 0.0288 | +0.0152 | 0.316589 | n.s. |
| LIBERO-Object | Argmin K=5 | 4 | 0.1300 | 0.0163 | +0.0212 | 0.073136 | n.s. |
| LIBERO-Object | Adaptive-K (all) | 11 | 0.1409 | 0.0151 | +0.0322 | 0.000170 | *** |

## 修正内容总结

1. **Object 主配置改为 norm02 (ε=0.2) K=10** — 所有 summary table 和 comparison 中 Object 的 CRM 用 `crm_object` (norm02 K=10)，norm01 降为 supplementary
2. **新增数据**: CRM-Goal seed47=0.69 (n:5→6), VLA-Spatial seed48=0.30/seed49=0.29/seed50=0.30 (n:7→9)
3. **VLA-Long seed48 = 0.14** 已确认
4. **Argmin K=10 seed43 = 0.17**: 在 4 台服务器均未找到原始 JSON，registry 值保留但标注为 unverified outlier

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 413204,
  "duration_api_ms": 408374,
  "num_turns": 47,
  "stop_reason": "end_turn",
  "session_id": "2c831810-b162-4fab-9231-54578fcd9e23",
  "total_cost_usd": 1.4615534999999997,
  "usage": {
    "input_tokens": 24,
    "cache_creation_input_tokens": 62416,
    "cache_read_input_tokens": 894309,
    "output_tokens": 24892,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 62416,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 904,
        "cache_read_input_tokens": 70173,
        "cache_creation_input_tokens": 4084,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4084
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1799,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001879,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 24,
      "outputTokens": 24892,
      "cacheReadInputTokens": 894309,
      "cacheCreationInputTokens": 62416,
      "webSearchRequests": 0,
      "costUSD": 1.4596744999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "31d852c9-7ec0-4ab3-a4e5-95b6ba231a93"
}
```

</details>

---
