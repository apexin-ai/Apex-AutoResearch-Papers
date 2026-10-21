# code gemma budget sweep

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_code_gemma-budget-sweep_20260521T221030.log`
- **Structured JSON:** [`2f34d984c7d35d0e7a80.json`](../../sessions/2f/2f34d984c7d35d0e7a80.json)

## Before a recorded user message

27 recorded events

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
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
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
  "uuid": "d1eb6faa-2ca0-465c-9065-01adbddd5971",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu-ec-hte-llm-annotation/memory/"
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
    "resetsAt": 1779418800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b1495374-2fae-4e55-a920-70c5612a3f3c",
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc"
}
```

---

### Assistant

_source line 4_

I'll start by reading the reference script and the Gemma CSV to understand the data and template.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "b62d53f6-5183-4b71-8a4e-f42fc5e030ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCsjheZyN8cuyjm7aJZBwi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6315,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6315
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

<details open><summary>🔧 Tool call — Read · `toolu_015caEVRETf2tV4ZD4DMqyWf`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_budget_sweep_k4.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "b5e5276b-8402-4c96-9fba-e12ce6d71068",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCsjheZyN8cuyjm7aJZBwi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6315,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6315
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

_source line 6 · 2026-05-21T22:10:43.143Z_

<details><summary>↩ Tool result · `toolu_015caEVRETf2tV4ZD4DMqyWf`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Budget sensitivity sweep for Llama K=4 real confusion matrices.
4	
5	Sweeps n_expert in {100, 200, 500, 1000, 2000} with 50 MC seeds each.
6	Uses MAP-EB instead of Gibbs for speed (250 total runs).
7	
8	|Bias| metric: |mean(estimate - truth) across seeds| averaged across cells.
9	"""
10	
11	import time
12	import warnings
13	import numpy as np
14	import pandas as pd
15	from scipy.optimize import minimize_scalar
16	from scipy.special import gammaln
17	
18	warnings.filterwarnings('ignore')
19	
20	# === Config ===
21	
22	N = 5000
23	N_EXPERT_LIST = [100, 200, 500, 1000, 2000]
24	N_MC = 50
25	SEED_BASE = 0
26	
27	SUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']
28	SUBGROUP_WEIGHTS = np.array([0.386, 0.218, 0.258, 0.138])
29	
30	SUBGROUP_CM = {
31	    'False_medium': {'fpr': 0.235, 'fnr': 0.319},
32	    'False_short':  {'fpr': 0.310, 'fnr': 0.212},
33	    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},
34	    'True_short':   {'fpr': 0.091, 'fnr': 0.190},
35	}
36	
37	P_Z1 = 0.652
38	P_T1 = 0.5
39	TAU_Z0 = 0.35
40	TAU_Z1 = 0.65
41	
42	
43	def get_cm_matrix(fpr, fnr):
44	    return np.array([[1 - fpr, fpr],
45	                     [fnr, 1 - fnr]])
46	
47	
48	# === Estimators ===
49	
50	def diff_in_means(Y, T, mask):
51	    t1 = mask & (T == 1)
52	    t0 = mask & (T == 0)
53	    n1, n0 = t1.sum(), t0.sum()
54	    if n1 < 2 or n0 < 2:
55	        return np.nan, np.nan
56	    y1, y0 = Y[t1], Y[t0]
57	    tau_hat = y1.mean() - y0.mean()
58	    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
59	    return tau_hat, se
60	
61	
62	def estimate_confusion_matrix(z_true, z_hat):
63	    C = np.zeros((2, 2))
64	    for zt in [0, 1]:
65	        mask = z_true == zt
66	        n = mask.sum()
67	        for zh in [0, 1]:
68	            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
69	    return C
70	
71	
72	def estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):
73	    C = {}
74	    for s in labels:
75	        ms = subgroups == s
76	        C_s = np.zeros((2, 2))
77	        for zt in [0, 1]:
78	            mask = ms & (z_true == zt)
79	            n = mask.sum()
80	            for zh in [0, 1]:
81	                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
82	        C[s] = C_s
83	    return C
84	
85	
86	def build_mixing_matrix(C, p_z, p_z_hat):
87	    M = np.zeros((2, 2))
88	    for zh in [0, 1]:
89	        for z in [0, 1]:
90	            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5
91	    return M
92	
93	
94	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
95	    cond = np.linalg.cond(M)
96	    if cond > cond_threshold:
97	        return tau_obs.copy(), se_obs.copy()
98	    det = np.linalg.det(M)
99	    if abs(det) < 1e-10:
100	        return tau_obs.copy(), se_obs.copy()
101	    Mi = np.linalg.inv(M)
102	    tau_c = Mi @ tau_obs
103	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
104	    return tau_c, se_c
105	
106	
107	# === MAP-EB ===
108	
109	def _dirmult_neg_ll(alpha, counts_z):
110	    a = alpha / 2.0
111	    if a < 1e-10:
112	        return 1e10
113	    ll = 0.0
114	    for c0, c1 in counts_z:
115	        n = c0 + c1
116	        if n == 0:
117	            continue
118	        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)
119	        ll -= 2 * gammaln(a) - gammaln(2 * a)
120	    return -ll
121	
122	
123	def estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):
124	    hp_rate = 1.0 / hp_scale
125	    k = len(labels)
126	    alpha_opt = np.zeros(2)
127	
128	    for z in [0, 1]:
129	        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]
130	        total = sum(c0 + c1 for c0, c1 in cl)
131	        if total == 0:
132	            alpha_opt[z] = hp_shape * hp_scale
133	            continue
134	
135	        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):
136	            nll = _dirmult_neg_ll(a, _cl)
137	            if a < 1e-10:
138	                return 1e10
139	            log_prior = (_shape - 1.0) * np.log(a) - _rate * a
140	            return nll - log_prior
141	
142	        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')
143	        alpha_opt[z] = res.x
144	
145	    C = {}
146	    for i, s in enumerate(labels):
147	        C_s = np.zeros((2, 2))
148	        for z in [0, 1]:
149	            a = alpha_opt[z] / 2.0
150	            n_sz = counts[i, z, :].sum()
151	            d = n_sz + 2 * a
152	            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5
153	            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5
154	        C[s] = C_s
155	
156	    return C, alpha_opt
157	
158	
159	def get_counts(z_true, z_hat, subgroups, labels):
160	    k = len(labels)
161	    counts = np.zeros((k, 2, 2), dtype=int)
162	    for i, s in enumerate(labels):
163	        ms = subgroups == s
164	        for z in [0, 1]:
165	            mz = ms & (z_true == z)
166	            counts[i, z, 0] = (z_hat[mz] == 0).sum()
167	            counts[i, z, 1] = (z_hat[mz] == 1).sum()
168	    return counts
169	
170	
171	# === DGP ===
172	
173	def generate_data(seed, n_expert):
174	    rng = np.random.RandomState(seed)
175	
176	    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)
177	    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])
178	
179	    Z = rng.binomial(1, P_Z1, N)
180	    T = rng.binomial(1, P_T1, N)
181	
182	    Z_hat = np.empty(N, dtype=int)
183	    for i in range(4):
184	        s_mask = S_idx == i
185	        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],
186	                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])
187	        z_s = Z[s_mask]
188	        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])
189	        Z_hat[s_mask] = rng.binomial(1, p_obs1)
190	
191	    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)
192	    eps = rng.randn(N)
193	    Y = 1.0 + tau_vals * T + eps
194	
195	    expert_idx = rng.choice(N, n_expert, replace=False)
196	    expert_mask = np.zeros(N, dtype=bool)
197	    expert_mask[expert_idx] = True
198	
199	    return {
200	        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,
201	        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,
202	    }
203	
204	
205	# === MC Runner ===
206	
207	def run_one_mc(data, seed):
208	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
209	    expert_mask = data['expert_mask']
210	
211	    z_exp = Z[expert_mask]
212	    zh_exp = Z_hat[expert_mask]
213	    s_exp = S[expert_mask]
214	
215	    C_global = estimate_confusion_matrix(z_exp, zh_exp)
216	    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])
217	    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])
218	    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)
219	
220	    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)
221	
222	    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)
223	    C_hb, _ = estimate_cm_hb_map_eb(counts, SUBGROUP_LABELS)
224	
225	    M_mle_sub = {}
226	    M_hb_sub = {}
227	    for s_val in SUBGROUP_LABELS:
228	        sm_exp = (s_exp == s_val)
229	        sm_all = (S == s_val)
230	        if sm_exp.sum() >= 4:
231	            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])
232	        else:
233	            p_z_s = p_z_global
234	        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])
235	        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)
236	        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)
237	
238	    rows = []
239	
240	    for s_val in SUBGROUP_LABELS:
241	        s_mask = S == s_val
242	
243	        for z_level in [0, 1]:
244	            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0
245	
246	            # Naive
247	            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))
248	            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan
249	            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan
250	            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0
251	            rows.append({
252	                'seed': seed, 'method': 'naive', 'subgroup': s_val,
253	                'z_level': z_level,
254	                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,
255	                'cate_est': th_nv, 'cate_true': oracle_cate,
256	                'coverage': cov_nv,
257	            })
258	
259	            # Observed CATE in Z_hat=0 and Z_hat=1 cells
260	            tau_obs = np.array([
261	                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],
262	                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],
263	            ])
264	            se_obs = np.array([
265	                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],
266	                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],
267	            ])
268	
269	            if not np.any(np.isnan(tau_obs)):
270	                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)
271	                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]
272	
273	                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)
274	                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]
275	
276	                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)
277	                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]
278	            else:
279	                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan
280	
281	            # Global corrected
282	            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan
283	            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan
284	            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0
285	            rows.append({
286	                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,
287	                'z_level': z_level,
288	                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,
289	                'cate_est': th_gc, 'cate_true': oracle_cate,
290	                'coverage': cov_gc,
291	            })
292	
293	            # Stratified MLE
294	            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan
295	            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan
296	            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0
297	            rows.append({
298	                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,
299	                'z_level': z_level,
300	                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,
301	                'cate_est': th_ml, 'cate_true': oracle_cate,
302	                'coverage': cov_ml,
303	            })
304	
305	            # HB EC-HTE (MAP-EB)
306	            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan
307	            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan
308	            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0
309	            rows.append({
310	                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,
311	                'z_level': z_level,
312	                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,
313	                'cate_est': th_hb, 'cate_true': oracle_cate,
314	                'coverage': cov_hb,
315	            })
316	
317	    return rows
318	
319	
320	# === Corrected |Bias| aggregation ===
321	
322	def compute_corrected_abs_bias(df):
323	    """
324	    |Bias| = average across cells of |mean(estimate - truth) across seeds|.
325	    For each (method, n_expert): average over (subgroup, z_level) cells of |mean bias|.
326	    """
327	    cell_bias = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias']
328	                 .mean().abs().reset_index(name='abs_mean_bias'))
329	    return (cell_bias.groupby(['n_expert', 'method'])['abs_mean_bias']
330	            .mean().reset_index(name='abs_bias'))
331	
332	
333	def compute_rmse(df):
334	    """RMSE = sqrt(mean(bias^2)) averaged across cells."""
335	    cell_rmse = (df.assign(bias_sq=df['bias'] ** 2)
336	                 .groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias_sq']
337	                 .mean().apply(np.sqrt).reset_index(name='rmse'))
338	    return (cell_rmse.groupby(['n_expert', 'method'])['rmse']
339	            .mean().reset_index(name='rmse'))
340	
341	
342	def compute_coverage(df):
343	    return (df.groupby(['n_expert', 'method'])['coverage']
344	            .mean().reset_index(name='coverage'))
345	
346	
347	# === Analysis Report ===
348	
349	def write_analysis(df_raw, outpath):
350	    abs_bias = compute_corrected_abs_bias(df_raw)
351	    rmse = compute_rmse(df_raw)
352	    cov = compute_coverage(df_raw)
353	
354	    summary = abs_bias.merge(rmse, on=['n_expert', 'method']).merge(cov, on=['n_expert', 'method'])
355	
356	    lines = []
357	    lines.append("# Budget Sensitivity Sweep: Llama K=4 Real CM\n")
358	    lines.append("## Design\n")
359	    lines.append(f"- N={N}, P(Z=1)={P_Z1}, K=4 subgroups")
360	    lines.append(f"- tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1 - TAU_Z0:.1f}")
361	    lines.append(f"- n_expert sweep: {N_EXPERT_LIST}")
362	    lines.append(f"- {N_MC} MC seeds per budget")
363	    lines.append("- HB method: MAP-EB (Gamma(3,1) prior)")
364	    lines.append(f"- |Bias| = avg across cells of |mean(bias) across seeds|")
365	    lines.append("")
366	
367	    lines.append("## Summary Table\n")
368	    lines.append("| n_expert | |Bias|_naive | |Bias|_global | |Bias|_strat | |Bias|_echte | RMSE_naive | RMSE_global | RMSE_strat | RMSE_echte | Cov_echte | HB_wins_bias? | HB_wins_rmse? |")
369	    lines.append("|----------|-------------|--------------|-------------|-------------|------------|-------------|------------|------------|-----------|---------------|---------------|")
370	
371	    for ne in N_EXPERT_LIST:
372	        sub = summary[summary['n_expert'] == ne]
373	        vals = {}
374	        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:
375	            row = sub[sub['method'] == m]
376	            if len(row) > 0:
377	                vals[m] = {
378	                    'abs_bias': row.iloc[0]['abs_bias'],
379	                    'rmse': row.iloc[0]['rmse'],
380	                    'coverage': row.iloc[0]['coverage'],
381	                }
382	            else:
383	                vals[m] = {'abs_bias': np.nan, 'rmse': np.nan, 'coverage': np.nan}
384	
385	        hb_wins_bias = "YES" if vals['hb_ec_hte']['abs_bias'] < vals['naive']['abs_bias'] else "no"
386	        hb_wins_rmse = "YES" if vals['hb_ec_hte']['rmse'] < vals['naive']['rmse'] else "no"
387	
388	        lines.append(
389	            f"| {ne} "
390	            f"| {vals['naive']['abs_bias']:.4f} "
391	            f"| {vals['global_corrected']['abs_bias']:.4f} "
392	            f"| {vals['stratified_mle']['abs_bias']:.4f} "
393	            f"| {vals['hb_ec_hte']['abs_bias']:.4f} "
394	            f"| {vals['naive']['rmse']:.4f} "
395	            f"| {vals['global_corrected']['rmse']:.4f} "
396	            f"| {vals['stratified_mle']['rmse']:.4f} "
397	            f"| {vals['hb_ec_hte']['rmse']:.4f} "
398	            f"| {vals['hb_ec_hte']['coverage']:.3f} "
399	            f"| {hb_wins_bias} "
400	            f"| {hb_wins_rmse} |"
401	        )
402	    lines.append("")
403	
404	    # Crossover analysis
405	    lines.append("## Crossover Analysis\n")
406	    crossover_bias = None
407	    crossover_rmse = None
408	    for ne in N_EXPERT_LIST:
409	        sub = summary[summary['n_expert'] == ne]
410	        hb = sub[sub['method'] == 'hb_ec_hte']
411	        nv = sub[sub['method'] == 'naive']
412	        if len(hb) > 0 and len(nv) > 0:
413	            if hb.iloc[0]['abs_bias'] < nv.iloc[0]['abs_bias'] and crossover_bias is None:
414	                crossover_bias = ne
415	            if hb.iloc[0]['rmse'] < nv.iloc[0]['rmse'] and crossover_rmse is None:
416	                crossover_rmse = ne
417	
418	    if crossover_bias is not None:
419	        lines.append(f"- **|Bias| crossover**: EC-HTE beats Naive at n_expert={crossover_bias}")
420	    else:
421	        lines.append("- **|Bias| crossover**: EC-HTE never beats Naive in tested range")
422	    if crossover_rmse is not None:
423	        lines.append(f"- **RMSE crossover**: EC-HTE beats Naive at n_expert={crossover_rmse}")
424	    else:
425	        lines.append("- **RMSE crossover**: EC-HTE never beats Naive in tested range")
426	    lines.append("")
427	
428	    # Bias-variance decomposition per budget
429	    lines.append("## Bias-Variance Decomposition (per budget)\n")
430	    lines.append("| n_expert | Method | Bias^2 | Variance | MSE |")
431	    lines.append("|----------|--------|--------|----------|-----|")
432	    for ne in N_EXPERT_LIST:
433	        for m in ['naive', 'hb_ec_hte']:
434	            sub_df = df_raw[(df_raw['n_expert'] == ne) & (df_raw['method'] == m)]
435	            cell_stats = (sub_df.groupby(['subgroup', 'z_level'])['bias']
436	                          .agg(['mean', 'var', 'count']).reset_index())
437	            mean_bias_sq = (cell_stats['mean'] ** 2).mean()
438	            variance = cell_stats['var'].mean()
439	            mse = mean_bias_sq + variance
440	            lines.append(f"| {ne} | {m} | {mean_bias_sq:.4f} | {variance:.4f} | {mse:.4f} |")
441	    lines.append("")
442	
443	    report = "\n".join(lines)
444	    with open(outpath, 'w') as f:
445	        f.write(report)
446	    print(f"Wrote {outpath}")
447	
448	
449	# === Main ===
450	
451	if __name__ == '__main__':
452	    print("Budget Sensitivity Sweep: Llama K=4 Real CM")
453	    print(f"N={N}, budgets={N_EXPERT_LIST}, seeds={N_MC}")
454	    print(f"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}")
455	    print()
456	
457	    out_dir = 'artifacts/c1_multi_llm'
458	
459	    # Dry run: 1 budget, 1 seed
460	    print("=== Dry run (n_expert=100, 1 seed) ===")
461	    data = generate_data(SEED_BASE, 100)
462	    rows = run_one_mc(data, SEED_BASE)
463	    df_dry = pd.DataFrame(rows)
464	    df_dry['n_expert'] = 100
465	    print(f"Dry run OK: {len(df_dry)} rows, columns: {list(df_dry.columns)}")
466	    for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:
467	        sub = df_dry[df_dry['method'] == m]
468	        bias = sub['bias'].abs().mean()
469	        print(f"  {m:20s}: mean |bias| = {bias:.4f}")
470	    print()
471	
472	    # Full run
473	    print(f"=== Full run ({len(N_EXPERT_LIST)} budgets x {N_MC} seeds) ===")
474	    all_results = []
475	    t0 = time.time()
476	    total_runs = len(N_EXPERT_LIST) * N_MC
477	    run_count = 0
478	
479	    for n_expert in N_EXPERT_LIST:
480	        print(f"\n--- n_expert = {n_expert} ---")
481	        t_budget = time.time()
482	        for mc in range(N_MC):
483	            seed = SEED_BASE + mc
484	            data = generate_data(seed, n_expert)
485	            mc_rows = run_one_mc(data, seed)
486	            for r in mc_rows:
487	                r['n_expert'] = n_expert
488	            all_results.extend(mc_rows)
489	            run_count += 1
490	            if (mc + 1) % 10 == 0:
491	                elapsed = time.time() - t0
492	                eta = elapsed / run_count * (total_runs - run_count)
493	                print(f"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s")
494	        budget_time = time.time() - t_budget
495	        print(f"  n_expert={n_expert} done in {budget_time:.1f}s")
496	
497	    total_time = time.time() - t0
498	    print(f"\nTotal time: {total_time:.1f}s")
499	
500	    df_raw = pd.DataFrame(all_results)
501	
502	    # Save results CSV
503	    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage']
504	    df_raw[col_order].to_csv(f'{out_dir}/budget_sweep_k4_results.csv', index=False)
505	    print(f"Saved budget_sweep_k4_results.csv ({len(df_raw)} rows)")
506	
507	    # Write analysis
508	    write_analysis(df_raw, f'{out_dir}/budget_sweep_k4_analysis.md')
509	
510	    # Print summary
511	    print("\n=== Summary ===")
512	    abs_bias = compute_corrected_abs_bias(df_raw)
513	    rmse_df = compute_rmse(df_raw)
514	    summary = abs_bias.merge(rmse_df, on=['n_expert', 'method'])
515	    for ne in N_EXPERT_LIST:
516	        print(f"\n  n_expert={ne}:")
517	        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:
518	            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]
519	            if len(row) > 0:
520	                print(f"    {m:20s}: |Bias|={row.iloc[0]['abs_bias']:.4f}  RMSE={row.iloc[0]['rmse']:.4f}")
521	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "9d8fb380-eaf1-42a2-93a4-f1a07882a3a2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_budget_sweep_k4.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nBudget sensitivity sweep for Llama K=4 real confusion matrices.\n\nSweeps n_expert in {100, 200, 500, 1000, 2000} with 50 MC seeds each.\nUses MAP-EB instead of Gibbs for speed (250 total runs).\n\n|Bias| metric: |mean(estimate - truth) across seeds| averaged across cells.\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.optimize import minimize_scalar\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT_LIST = [100, 200, 500, 1000, 2000]\nN_MC = 50\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']\nSUBGROUP_WEIGHTS = np.array([0.386, 0.218, 0.258, 0.138])\n\nSUBGROUP_CM = {\n    'False_medium': {'fpr': 0.235, 'fnr': 0.319},\n    'False_short':  {'fpr': 0.310, 'fnr': 0.212},\n    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},\n    'True_short':   {'fpr': 0.091, 'fnr': 0.190},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\nTAU_Z0 = 0.35\nTAU_Z1 = 0.65\n\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === MAP-EB ===\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):\n    hp_rate = 1.0 / hp_scale\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = hp_shape * hp_scale\n            continue\n\n        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):\n            nll = _dirmult_neg_ll(a, _cl)\n            if a < 1e-10:\n                return 1e10\n            log_prior = (_shape - 1.0) * np.log(a) - _rate * a\n            return nll - log_prior\n\n        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n_sz = counts[i, z, :].sum()\n            d = n_sz + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    return C, alpha_opt\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\n# === DGP ===\n\ndef generate_data(seed, n_expert):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(4):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb, _ = estimate_cm_hb_map_eb(counts, SUBGROUP_LABELS)\n\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'cate_est': th_nv, 'cate_true': oracle_cate,\n                'coverage': cov_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'cate_est': th_gc, 'cate_true': oracle_cate,\n                'coverage': cov_gc,\n            })\n\n            # Stratified MLE\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'cate_est': th_ml, 'cate_true': oracle_cate,\n                'coverage': cov_ml,\n            })\n\n            # HB EC-HTE (MAP-EB)\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'cate_est': th_hb, 'cate_true': oracle_cate,\n                'coverage': cov_hb,\n            })\n\n    return rows\n\n\n# === Corrected |Bias| aggregation ===\n\ndef compute_corrected_abs_bias(df):\n    \"\"\"\n    |Bias| = average across cells of |mean(estimate - truth) across seeds|.\n    For each (method, n_expert): average over (subgroup, z_level) cells of |mean bias|.\n    \"\"\"\n    cell_bias = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias']\n                 .mean().abs().reset_index(name='abs_mean_bias'))\n    return (cell_bias.groupby(['n_expert', 'method'])['abs_mean_bias']\n            .mean().reset_index(name='abs_bias'))\n\n\ndef compute_rmse(df):\n    \"\"\"RMSE = sqrt(mean(bias^2)) averaged across cells.\"\"\"\n    cell_rmse = (df.assign(bias_sq=df['bias'] ** 2)\n                 .groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias_sq']\n                 .mean().apply(np.sqrt).reset_index(name='rmse'))\n    return (cell_rmse.groupby(['n_expert', 'method'])['rmse']\n            .mean().reset_index(name='rmse'))\n\n\ndef compute_coverage(df):\n    return (df.groupby(['n_expert', 'method'])['coverage']\n            .mean().reset_index(name='coverage'))\n\n\n# === Analysis Report ===\n\ndef write_analysis(df_raw, outpath):\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse = compute_rmse(df_raw)\n    cov = compute_coverage(df_raw)\n\n    summary = abs_bias.merge(rmse, on=['n_expert', 'method']).merge(cov, on=['n_expert', 'method'])\n\n    lines = []\n    lines.append(\"# Budget Sensitivity Sweep: Llama K=4 Real CM\\n\")\n    lines.append(\"## Design\\n\")\n    lines.append(f\"- N={N}, P(Z=1)={P_Z1}, K=4 subgroups\")\n    lines.append(f\"- tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1 - TAU_Z0:.1f}\")\n    lines.append(f\"- n_expert sweep: {N_EXPERT_LIST}\")\n    lines.append(f\"- {N_MC} MC seeds per budget\")\n    lines.append(\"- HB method: MAP-EB (Gamma(3,1) prior)\")\n    lines.append(f\"- |Bias| = avg across cells of |mean(bias) across seeds|\")\n    lines.append(\"\")\n\n    lines.append(\"## Summary Table\\n\")\n    lines.append(\"| n_expert | |Bias|_naive | |Bias|_global | |Bias|_strat | |Bias|_echte | RMSE_naive | RMSE_global | RMSE_strat | RMSE_echte | Cov_echte | HB_wins_bias? | HB_wins_rmse? |\")\n    lines.append(\"|----------|-------------|--------------|-------------|-------------|------------|-------------|------------|------------|-----------|---------------|---------------|\")\n\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        vals = {}\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            row = sub[sub['method'] == m]\n            if len(row) > 0:\n                vals[m] = {\n                    'abs_bias': row.iloc[0]['abs_bias'],\n                    'rmse': row.iloc[0]['rmse'],\n                    'coverage': row.iloc[0]['coverage'],\n                }\n            else:\n                vals[m] = {'abs_bias': np.nan, 'rmse': np.nan, 'coverage': np.nan}\n\n        hb_wins_bias = \"YES\" if vals['hb_ec_hte']['abs_bias'] < vals['naive']['abs_bias'] else \"no\"\n        hb_wins_rmse = \"YES\" if vals['hb_ec_hte']['rmse'] < vals['naive']['rmse'] else \"no\"\n\n        lines.append(\n            f\"| {ne} \"\n            f\"| {vals['naive']['abs_bias']:.4f} \"\n            f\"| {vals['global_corrected']['abs_bias']:.4f} \"\n            f\"| {vals['stratified_mle']['abs_bias']:.4f} \"\n            f\"| {vals['hb_ec_hte']['abs_bias']:.4f} \"\n            f\"| {vals['naive']['rmse']:.4f} \"\n            f\"| {vals['global_corrected']['rmse']:.4f} \"\n            f\"| {vals['stratified_mle']['rmse']:.4f} \"\n            f\"| {vals['hb_ec_hte']['rmse']:.4f} \"\n            f\"| {vals['hb_ec_hte']['coverage']:.3f} \"\n            f\"| {hb_wins_bias} \"\n            f\"| {hb_wins_rmse} |\"\n        )\n    lines.append(\"\")\n\n    # Crossover analysis\n    lines.append(\"## Crossover Analysis\\n\")\n    crossover_bias = None\n    crossover_rmse = None\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        hb = sub[sub['method'] == 'hb_ec_hte']\n        nv = sub[sub['method'] == 'naive']\n        if len(hb) > 0 and len(nv) > 0:\n            if hb.iloc[0]['abs_bias'] < nv.iloc[0]['abs_bias'] and crossover_bias is None:\n                crossover_bias = ne\n            if hb.iloc[0]['rmse'] < nv.iloc[0]['rmse'] and crossover_rmse is None:\n                crossover_rmse = ne\n\n    if crossover_bias is not None:\n        lines.append(f\"- **|Bias| crossover**: EC-HTE beats Naive at n_expert={crossover_bias}\")\n    else:\n        lines.append(\"- **|Bias| crossover**: EC-HTE never beats Naive in tested range\")\n    if crossover_rmse is not None:\n        lines.append(f\"- **RMSE crossover**: EC-HTE beats Naive at n_expert={crossover_rmse}\")\n    else:\n        lines.append(\"- **RMSE crossover**: EC-HTE never beats Naive in tested range\")\n    lines.append(\"\")\n\n    # Bias-variance decomposition per budget\n    lines.append(\"## Bias-Variance Decomposition (per budget)\\n\")\n    lines.append(\"| n_expert | Method | Bias^2 | Variance | MSE |\")\n    lines.append(\"|----------|--------|--------|----------|-----|\")\n    for ne in N_EXPERT_LIST:\n        for m in ['naive', 'hb_ec_hte']:\n            sub_df = df_raw[(df_raw['n_expert'] == ne) & (df_raw['method'] == m)]\n            cell_stats = (sub_df.groupby(['subgroup', 'z_level'])['bias']\n                          .agg(['mean', 'var', 'count']).reset_index())\n            mean_bias_sq = (cell_stats['mean'] ** 2).mean()\n            variance = cell_stats['var'].mean()\n            mse = mean_bias_sq + variance\n            lines.append(f\"| {ne} | {m} | {mean_bias_sq:.4f} | {variance:.4f} | {mse:.4f} |\")\n    lines.append(\"\")\n\n    report = \"\\n\".join(lines)\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"Budget Sensitivity Sweep: Llama K=4 Real CM\")\n    print(f\"N={N}, budgets={N_EXPERT_LIST}, seeds={N_MC}\")\n    print(f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}\")\n    print()\n\n    out_dir = 'artifacts/c1_multi_llm'\n\n    # Dry run: 1 budget, 1 seed\n    print(\"=== Dry run (n_expert=100, 1 seed) ===\")\n    data = generate_data(SEED_BASE, 100)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    df_dry['n_expert'] = 100\n    print(f\"Dry run OK: {len(df_dry)} rows, columns: {list(df_dry.columns)}\")\n    for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n    print()\n\n    # Full run\n    print(f\"=== Full run ({len(N_EXPERT_LIST)} budgets x {N_MC} seeds) ===\")\n    all_results = []\n    t0 = time.time()\n    total_runs = len(N_EXPERT_LIST) * N_MC\n    run_count = 0\n\n    for n_expert in N_EXPERT_LIST:\n        print(f\"\\n--- n_expert = {n_expert} ---\")\n        t_budget = time.time()\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            data = generate_data(seed, n_expert)\n            mc_rows = run_one_mc(data, seed)\n            for r in mc_rows:\n                r['n_expert'] = n_expert\n            all_results.extend(mc_rows)\n            run_count += 1\n            if (mc + 1) % 10 == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / run_count * (total_runs - run_count)\n                print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n        budget_time = time.time() - t_budget\n        print(f\"  n_expert={n_expert} done in {budget_time:.1f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(all_results)\n\n    # Save results CSV\n    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage']\n    df_raw[col_order].to_csv(f'{out_dir}/budget_sweep_k4_results.csv', index=False)\n    print(f\"Saved budget_sweep_k4_results.csv ({len(df_raw)} rows)\")\n\n    # Write analysis\n    write_analysis(df_raw, f'{out_dir}/budget_sweep_k4_analysis.md')\n\n    # Print summary\n    print(\"\\n=== Summary ===\")\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse_df = compute_rmse(df_raw)\n    summary = abs_bias.merge(rmse_df, on=['n_expert', 'method'])\n    for ne in N_EXPERT_LIST:\n        print(f\"\\n  n_expert={ne}:\")\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n            if len(row) > 0:\n                print(f\"    {m:20s}: |Bias|={row.iloc[0]['abs_bias']:.4f}  RMSE={row.iloc[0]['rmse']:.4f}\")\n",
      "numLines": 521,
      "startLine": 1,
      "totalLines": 521
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01ERBHaocvBtaMbWzFd1YgeN`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/gemma2_9b_balanced.csv",
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
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "75b4ab86-95af-49d9-aaa5-3da5b1d87572",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TCsjheZyN8cuyjm7aJZBwi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6315,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6315
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

_source line 8 · 2026-05-21T22:10:43.499Z_

<details><summary>↩ Tool result · `toolu_01ERBHaocvBtaMbWzFd1YgeN`</summary>

```text
1	idx,text,true_label,llm_label,z,has_hashtag,has_mention,text_length_bin
2	10476,"when you jacked into your house without keys. hell yeah, i'm david blaine jr.",2,2,1,False,False,short
3	1824,Cigarettes and Valentines,1,1,1,False,False,short
4	409,@user we'll miss you in Seattle! Especially when you win your NL Cy Young award!,2,2,1,False,True,medium
5	12149,I'm not going to sack Tony romo but I will sack dak,0,0,0,False,False,short
6	4506,@user Article reminds us Obama's new policy towards #Cuba follows path #Canada has taken all along #cdnpoli,1,1,1,True,True,medium
7	4012,@user @user Link to review for #ThisIsUs isn't launching.,1,0,1,True,True,short
8	3657,@user The same media that hides from the truth about the Clinton Foundation...,0,0,0,False,True,short
9	2286,Oh. my. God. Bernie is a white supremacist Nazi. The warning signs have been there for years and we never noticed!!…,0,0,0,False,False,medium
10	12066,"@user such as telling us exactly what we have to do as my points already made with gun control, health care, business, speech, ect.",1,0,1,False,True,medium
11	1679,The latest one hundred people you should know! Thanks to @user @user @user #chile #isis,1,2,1,True,True,medium
12	11087,@user @user twenty bags of rusted dicks.,0,0,0,False,True,short
13	12135,Finally watching Scream Queens episode 5 after what feels like forever!! #ScreamQueens,2,2,1,True,False,medium
14	8935,@user she'd claimed Thomistic view of ensoulment showed church's oppositon to abortion is recent develpmnt & Benedict wasn't having it,1,1,1,False,True,medium
15	1424,Preparations Continue For #Tesla's #Model3 Launch #ElectricVehicles #GoGreen #GoElectric #GreenerDriving,1,2,1,True,False,medium
16	9674,"Manasseh, Amon, Josiah. Pray Kim Jong Un follows Josiah's example-find the book of the Law discarded by ancestors.…",1,1,1,False,False,medium
17	6912,"Donald, take it easy my friend, but I can't wait to see u start building that thick high wall on the Mexican border to seal ur legacy",1,0,1,False,False,medium
18	520,Sharon needles is doing Melania trump n the crowd is chanting CULEERAA,0,0,0,False,False,short
19	488,My Grandmother would kill the #mannequinchallenge....she's dead #RIP,0,0,0,True,False,short
20	1535,@user ensure good voter registration in Nyanza region and its environ as a strategy of early victory come nxt year august,1,2,1,False,True,medium
21	3582,#Russian media: Is Mikheil Saakashvili planning new revolution in Ukraine?: Former Georgian President and…,1,1,1,True,False,medium
22	3811,"In other news, Trump waves goodbye to Petro Poroshenko, President of Ukraine",1,1,1,False,False,short
23	8279,"@user I'm not saying they will, but they can; also: will of the ppl? HRC is winning popular vote by 2 mill, so ... 😉",1,2,1,False,True,medium
24	9863,Happy funeral to all Liam's girls.AMÈM LIAM PAYNE #MtvStarsNiallHoran #MPN #OneDirection,1,0,1,True,False,medium
25	434,@user @user @user @user @user ummm vaccines have avoided over 700000 deaths since the nineties...,2,2,1,False,True,medium
26	9195,@user @user @user actually I don't care about her pc anything I care about integrity when reporting. she doesn't,0,0,0,False,True,medium
27	3257,#Repost @user with repostapp・・・#nationalfastfoodday 🍟,1,2,1,True,True,short
28	11731,Abysmally dumb leftists. Blind sheep aping #Hillary propaganda. Trump has no history of extremism in his entire lif…,0,0,0,True,False,medium
29	10647,@user pope Francis ministering to wicked afflicted and effected,0,2,0,False,True,short
30	11490,"Thank u for what, for bailing out rogue banks? For negligence of his own, for racist killer cops, for war crimes, f…",0,0,0,False,False,medium
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "90bccf5d-9de8-4314-9cb4-a4b2d1f03ce5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/gemma2_9b_balanced.csv",
      "content": "idx,text,true_label,llm_label,z,has_hashtag,has_mention,text_length_bin\n10476,\"when you jacked into your house without keys. hell yeah, i'm david blaine jr.\",2,2,1,False,False,short\n1824,Cigarettes and Valentines,1,1,1,False,False,short\n409,@user we'll miss you in Seattle! Especially when you win your NL Cy Young award!,2,2,1,False,True,medium\n12149,I'm not going to sack Tony romo but I will sack dak,0,0,0,False,False,short\n4506,@user Article reminds us Obama's new policy towards #Cuba follows path #Canada has taken all along #cdnpoli,1,1,1,True,True,medium\n4012,@user @user Link to review for #ThisIsUs isn't launching.,1,0,1,True,True,short\n3657,@user The same media that hides from the truth about the Clinton Foundation...,0,0,0,False,True,short\n2286,Oh. my. God. Bernie is a white supremacist Nazi. The warning signs have been there for years and we never noticed!!…,0,0,0,False,False,medium\n12066,\"@user such as telling us exactly what we have to do as my points already made with gun control, health care, business, speech, ect.\",1,0,1,False,True,medium\n1679,The latest one hundred people you should know! Thanks to @user @user @user #chile #isis,1,2,1,True,True,medium\n11087,@user @user twenty bags of rusted dicks.,0,0,0,False,True,short\n12135,Finally watching Scream Queens episode 5 after what feels like forever!! #ScreamQueens,2,2,1,True,False,medium\n8935,@user she'd claimed Thomistic view of ensoulment showed church's oppositon to abortion is recent develpmnt & Benedict wasn't having it,1,1,1,False,True,medium\n1424,Preparations Continue For #Tesla's #Model3 Launch #ElectricVehicles #GoGreen #GoElectric #GreenerDriving,1,2,1,True,False,medium\n9674,\"Manasseh, Amon, Josiah. Pray Kim Jong Un follows Josiah's example-find the book of the Law discarded by ancestors.…\",1,1,1,False,False,medium\n6912,\"Donald, take it easy my friend, but I can't wait to see u start building that thick high wall on the Mexican border to seal ur legacy\",1,0,1,False,False,medium\n520,Sharon needles is doing Melania trump n the crowd is chanting CULEERAA,0,0,0,False,False,short\n488,My Grandmother would kill the #mannequinchallenge....she's dead #RIP,0,0,0,True,False,short\n1535,@user ensure good voter registration in Nyanza region and its environ as a strategy of early victory come nxt year august,1,2,1,False,True,medium\n3582,#Russian media: Is Mikheil Saakashvili planning new revolution in Ukraine?: Former Georgian President and…,1,1,1,True,False,medium\n3811,\"In other news, Trump waves goodbye to Petro Poroshenko, President of Ukraine\",1,1,1,False,False,short\n8279,\"@user I'm not saying they will, but they can; also: will of the ppl? HRC is winning popular vote by 2 mill, so ... 😉\",1,2,1,False,True,medium\n9863,Happy funeral to all Liam's girls.AMÈM LIAM PAYNE #MtvStarsNiallHoran #MPN #OneDirection,1,0,1,True,False,medium\n434,@user @user @user @user @user ummm vaccines have avoided over 700000 deaths since the nineties...,2,2,1,False,True,medium\n9195,@user @user @user actually I don't care about her pc anything I care about integrity when reporting. she doesn't,0,0,0,False,True,medium\n3257,#Repost @user with repostapp・・・#nationalfastfoodday 🍟,1,2,1,True,True,short\n11731,Abysmally dumb leftists. Blind sheep aping #Hillary propaganda. Trump has no history of extremism in his entire lif…,0,0,0,True,False,medium\n10647,@user pope Francis ministering to wicked afflicted and effected,0,2,0,False,True,short\n11490,\"Thank u for what, for bailing out rogue banks? For negligence of his own, for racist killer cops, for war crimes, f…\",0,0,0,False,False,medium",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 502
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I understand the reference script and the data format. Let me:

1. First compute Gemma's per-subgroup CM from the CSV
2. Then create the budget sweep scripts for K=4 and K=2

Let me first understand the data better - I need to compute:
- Balanced Z: Z=1 if true_label >= 1, Z_hat=1 if llm_label >= 1
- K=4 subgroups: has_hashtag × text_length_bin (excluding "long" bin)
- K=2 subgroups: just has_hashtag


Now I'll write a Python script that handles all of this end-to-end.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "9b1ada3e-b651-4280-b2fa-39e40ff87417",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0144BVmMkQ2z3zrEEf7RTmZq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10342,
      "cache_read_input_tokens": 18156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10342
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

Now I'll write a single Python script that computes the CM profile from the CSV and runs both K=4 and K=2 budget sweeps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "be0489c1-4552-406d-8488-8fb10c3840a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0144BVmMkQ2z3zrEEf7RTmZq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10342,
      "cache_read_input_tokens": 18156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10342
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

<details open><summary>🔧 Tool call — Write · `toolu_01YCZ5Dh752uppihoFaaL1Ui`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_gemma_sweep.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nGemma-2-9B full pipeline: CM profile + budget sweep (K=4 and K=2).\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.optimize import minimize_scalar\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\nOUT_DIR = 'artifacts/c1_multi_llm'\n\n# === Step 1: Compute per-subgroup CM from CSV ===\n\ndef compute_cm_profile(csv_path):\n    df = pd.read_csv(csv_path)\n\n    # Balanced binary Z\n    df['Z'] = (df['true_label'] >= 1).astype(int)\n    df['Z_hat'] = (df['llm_label'] >= 1).astype(int)\n\n    # Global stats\n    acc = (df['Z'] == df['Z_hat']).mean()\n    p_z1 = df['Z'].mean()\n\n    # Global FPR, FNR\n    neg = df[df['Z'] == 0]\n    pos = df[df['Z'] == 1]\n    fpr_global = (neg['Z_hat'] == 1).mean()\n    fnr_global = (pos['Z_hat'] == 0).mean()\n\n    print(f\"=== Gemma CM Profile ===\")\n    print(f\"N = {len(df)}, Accuracy = {acc:.3f}\")\n    print(f\"P(Z=1) = {p_z1:.3f}\")\n    print(f\"Global FPR = {fpr_global:.3f}, FNR = {fnr_global:.3f}\")\n    print(f\"Delta_pi = |FPR - FNR| = {abs(fpr_global - fnr_global):.3f}\")\n    print()\n\n    # K=4: has_hashtag x text_length_bin (exclude \"long\")\n    df_k4 = df[df['text_length_bin'] != 'long'].copy()\n    df_k4['subgroup'] = df_k4['has_hashtag'].astype(str) + '_' + df_k4['text_length_bin']\n    k4_labels = sorted(df_k4['subgroup'].unique())\n\n    print(f\"K=4 subgroups (excluding 'long'): {k4_labels}\")\n    print(f\"K=4 sample size: {len(df_k4)}\")\n\n    k4_cm = {}\n    k4_weights = {}\n    k4_pi = {}\n    k4_kappa = {}\n\n    for s in k4_labels:\n        sub = df_k4[df_k4['subgroup'] == s]\n        n_s = len(sub)\n        w_s = n_s / len(df_k4)\n        neg_s = sub[sub['Z'] == 0]\n        pos_s = sub[sub['Z'] == 1]\n        fpr_s = (neg_s['Z_hat'] == 1).mean() if len(neg_s) > 0 else 0.0\n        fnr_s = (pos_s['Z_hat'] == 0).mean() if len(pos_s) > 0 else 0.0\n        pi_s = sub['Z'].mean()\n        kappa_s = 1.0 / (1.0 - fpr_s - fnr_s) if abs(1.0 - fpr_s - fnr_s) > 1e-10 else float('inf')\n\n        k4_cm[s] = {'fpr': round(fpr_s, 3), 'fnr': round(fnr_s, 3)}\n        k4_weights[s] = round(w_s, 3)\n        k4_pi[s] = round(pi_s, 3)\n        k4_kappa[s] = round(kappa_s, 2)\n\n        print(f\"  {s:20s}: n={n_s:4d}, w={w_s:.3f}, pi={pi_s:.3f}, FPR={fpr_s:.3f}, FNR={fnr_s:.3f}, kappa={kappa_s:.2f}\")\n\n    print()\n\n    # K=2: has_hashtag only\n    df['subgroup_k2'] = df['has_hashtag'].astype(str)\n    k2_labels = sorted(df['subgroup_k2'].unique())\n\n    print(f\"K=2 subgroups: {k2_labels}\")\n\n    k2_cm = {}\n    k2_weights = {}\n    k2_pi = {}\n    k2_kappa = {}\n\n    for s in k2_labels:\n        sub = df[df['subgroup_k2'] == s]\n        n_s = len(sub)\n        w_s = n_s / len(df)\n        neg_s = sub[sub['Z'] == 0]\n        pos_s = sub[sub['Z'] == 1]\n        fpr_s = (neg_s['Z_hat'] == 1).mean() if len(neg_s) > 0 else 0.0\n        fnr_s = (pos_s['Z_hat'] == 0).mean() if len(pos_s) > 0 else 0.0\n        pi_s = sub['Z'].mean()\n        kappa_s = 1.0 / (1.0 - fpr_s - fnr_s) if abs(1.0 - fpr_s - fnr_s) > 1e-10 else float('inf')\n\n        k2_cm[s] = {'fpr': round(fpr_s, 3), 'fnr': round(fnr_s, 3)}\n        k2_weights[s] = round(w_s, 3)\n        k2_pi[s] = round(pi_s, 3)\n        k2_kappa[s] = round(kappa_s, 2)\n\n        print(f\"  {s:20s}: n={n_s:4d}, w={w_s:.3f}, pi={pi_s:.3f}, FPR={fpr_s:.3f}, FNR={fnr_s:.3f}, kappa={kappa_s:.2f}\")\n\n    print()\n\n    # Write CM profile markdown\n    lines = []\n    lines.append(\"# Gemma-2-9B Confusion Matrix Profile\\n\")\n    lines.append(\"## Global Statistics\\n\")\n    lines.append(f\"- N = {len(df)}\")\n    lines.append(f\"- Accuracy = {acc:.3f}\")\n    lines.append(f\"- P(Z=1) = {p_z1:.3f}\")\n    lines.append(f\"- Global FPR = {fpr_global:.3f}\")\n    lines.append(f\"- Global FNR = {fnr_global:.3f}\")\n    lines.append(f\"- Delta_pi = |FPR - FNR| = {abs(fpr_global - fnr_global):.3f}\")\n    lines.append(f\"- FNR > FPR asymmetry: {'YES' if fnr_global > fpr_global else 'NO'}\")\n    lines.append(\"\")\n\n    lines.append(\"## K=4 Subgroups (has_hashtag x text_length_bin, excl. long)\\n\")\n    lines.append(f\"- Sample size (excl. long): {len(df_k4)}\")\n    lines.append(\"\")\n    lines.append(\"| Subgroup | n | Weight | pi_s | FPR | FNR | kappa |\")\n    lines.append(\"|----------|---|--------|------|-----|-----|-------|\")\n    for s in k4_labels:\n        sub = df_k4[df_k4['subgroup'] == s]\n        lines.append(f\"| {s} | {len(sub)} | {k4_weights[s]:.3f} | {k4_pi[s]:.3f} | {k4_cm[s]['fpr']:.3f} | {k4_cm[s]['fnr']:.3f} | {k4_kappa[s]:.2f} |\")\n    lines.append(\"\")\n\n    max_kappa_k4 = max(k4_kappa.values())\n    lines.append(f\"- Max kappa = {max_kappa_k4:.2f}\")\n    prop2_count = sum(1 for s in k4_labels if k4_kappa[s] > 2.0)\n    lines.append(f\"- Prop2 triggered (kappa > 2): {prop2_count}/{len(k4_labels)}\")\n    lines.append(\"\")\n\n    lines.append(\"## K=2 Subgroups (has_hashtag only)\\n\")\n    lines.append(\"| Subgroup | n | Weight | pi_s | FPR | FNR | kappa |\")\n    lines.append(\"|----------|---|--------|------|-----|-----|-------|\")\n    for s in k2_labels:\n        sub = df[df['subgroup_k2'] == s]\n        lines.append(f\"| {s} | {len(sub)} | {k2_weights[s]:.3f} | {k2_pi[s]:.3f} | {k2_cm[s]['fpr']:.3f} | {k2_cm[s]['fnr']:.3f} | {k2_kappa[s]:.2f} |\")\n    lines.append(\"\")\n\n    max_kappa_k2 = max(k2_kappa.values())\n    lines.append(f\"- Max kappa = {max_kappa_k2:.2f}\")\n    lines.append(\"\")\n\n    profile_path = f'{OUT_DIR}/gemma_cm_profile.md'\n    with open(profile_path, 'w') as f:\n        f.write(\"\\n\".join(lines))\n    print(f\"Wrote {profile_path}\")\n\n    return {\n        'p_z1': p_z1,\n        'k4': {'labels': k4_labels, 'weights': k4_weights, 'cm': k4_cm},\n        'k2': {'labels': k2_labels, 'weights': k2_weights, 'cm': k2_cm},\n    }\n\n\n# === Config ===\n\nN = 5000\nN_EXPERT_LIST = [100, 200, 500, 1000, 2000]\nN_MC = 50\nSEED_BASE = 0\nTAU_Z0 = 0.35\nTAU_Z1 = 0.65\n\n\n# === Estimators ===\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === MAP-EB ===\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):\n    hp_rate = 1.0 / hp_scale\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = hp_shape * hp_scale\n            continue\n\n        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):\n            nll = _dirmult_neg_ll(a, _cl)\n            if a < 1e-10:\n                return 1e10\n            log_prior = (_shape - 1.0) * np.log(a) - _rate * a\n            return nll - log_prior\n\n        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n_sz = counts[i, z, :].sum()\n            d = n_sz + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    return C, alpha_opt\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\n# === DGP ===\n\ndef generate_data(seed, n_expert, subgroup_labels, subgroup_weights, subgroup_cm, p_z1):\n    rng = np.random.RandomState(seed)\n    k = len(subgroup_labels)\n\n    S_idx = rng.choice(k, size=N, p=subgroup_weights)\n    S = np.array([subgroup_labels[i] for i in S_idx])\n\n    Z = rng.binomial(1, p_z1, N)\n    T = rng.binomial(1, 0.5, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(k):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(subgroup_cm[subgroup_labels[i]]['fpr'],\n                           subgroup_cm[subgroup_labels[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed, subgroup_labels):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, subgroup_labels)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, subgroup_labels)\n    C_hb, _ = estimate_cm_hb_map_eb(counts, subgroup_labels)\n\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in subgroup_labels:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in subgroup_labels:\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            ci_w_nv = (ci_hi_nv - ci_lo_nv) if not np.isnan(ci_lo_nv) else np.nan\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'cate_est': th_nv, 'cate_true': oracle_cate,\n                'coverage': cov_nv, 'ci_width': ci_w_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            ci_w_gc = (ci_hi_gc - ci_lo_gc) if not np.isnan(ci_lo_gc) else np.nan\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'cate_est': th_gc, 'cate_true': oracle_cate,\n                'coverage': cov_gc, 'ci_width': ci_w_gc,\n            })\n\n            # Stratified MLE\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            ci_w_ml = (ci_hi_ml - ci_lo_ml) if not np.isnan(ci_lo_ml) else np.nan\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'cate_est': th_ml, 'cate_true': oracle_cate,\n                'coverage': cov_ml, 'ci_width': ci_w_ml,\n            })\n\n            # HB EC-HTE (MAP-EB)\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            ci_w_hb = (ci_hi_hb - ci_lo_hb) if not np.isnan(ci_lo_hb) else np.nan\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'cate_est': th_hb, 'cate_true': oracle_cate,\n                'coverage': cov_hb, 'ci_width': ci_w_hb,\n            })\n\n    return rows\n\n\n# === Aggregation ===\n\ndef compute_corrected_abs_bias(df):\n    cell_bias = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias']\n                 .mean().abs().reset_index(name='abs_mean_bias'))\n    return (cell_bias.groupby(['n_expert', 'method'])['abs_mean_bias']\n            .mean().reset_index(name='abs_bias'))\n\n\ndef compute_rmse(df):\n    cell_rmse = (df.assign(bias_sq=df['bias'] ** 2)\n                 .groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias_sq']\n                 .mean().apply(np.sqrt).reset_index(name='rmse'))\n    return (cell_rmse.groupby(['n_expert', 'method'])['rmse']\n            .mean().reset_index(name='rmse'))\n\n\ndef compute_coverage(df):\n    return (df.groupby(['n_expert', 'method'])['coverage']\n            .mean().reset_index(name='coverage'))\n\n\ndef compute_ci_width(df):\n    cell_w = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['ci_width']\n              .mean().reset_index(name='ci_width'))\n    return (cell_w.groupby(['n_expert', 'method'])['ci_width']\n            .mean().reset_index(name='ci_width'))\n\n\n# === Run sweep for one K config ===\n\ndef run_sweep(k_label, subgroup_labels, subgroup_weights_dict, subgroup_cm, p_z1, dry_run=False):\n    labels = subgroup_labels\n    weights_arr = np.array([subgroup_weights_dict[s] for s in labels])\n    weights_arr = weights_arr / weights_arr.sum()  # normalize\n\n    print(f\"\\n{'='*60}\")\n    print(f\"Budget Sweep: Gemma {k_label}\")\n    print(f\"Subgroups: {labels}\")\n    print(f\"Weights: {dict(zip(labels, [round(w, 3) for w in weights_arr]))}\")\n    print(f\"P(Z=1) = {p_z1:.3f}\")\n    print(f\"tau(z=0) = {TAU_Z0}, tau(z=1) = {TAU_Z1}\")\n    print(f\"{'='*60}\")\n\n    if dry_run:\n        print(\"\\n--- Dry run (n_expert=100, 1 seed) ---\")\n        data = generate_data(SEED_BASE, 100, labels, weights_arr, subgroup_cm, p_z1)\n        rows = run_one_mc(data, SEED_BASE, labels)\n        df_dry = pd.DataFrame(rows)\n        df_dry['n_expert'] = 100\n        print(f\"Dry run OK: {len(df_dry)} rows\")\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            sub = df_dry[df_dry['method'] == m]\n            bias = sub['bias'].abs().mean()\n            print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n        return None\n\n    # Full run\n    print(f\"\\nFull run: {len(N_EXPERT_LIST)} budgets x {N_MC} seeds\")\n    all_results = []\n    t0 = time.time()\n    total_runs = len(N_EXPERT_LIST) * N_MC\n    run_count = 0\n\n    for n_expert in N_EXPERT_LIST:\n        print(f\"\\n--- n_expert = {n_expert} ---\")\n        t_budget = time.time()\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            data = generate_data(seed, n_expert, labels, weights_arr, subgroup_cm, p_z1)\n            mc_rows = run_one_mc(data, seed, labels)\n            for r in mc_rows:\n                r['n_expert'] = n_expert\n            all_results.extend(mc_rows)\n            run_count += 1\n            if (mc + 1) % 10 == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / run_count * (total_runs - run_count)\n                print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n        budget_time = time.time() - t_budget\n        print(f\"  n_expert={n_expert} done in {budget_time:.1f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(all_results)\n    return df_raw\n\n\ndef save_sweep_csv(df_raw, csv_path):\n    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level',\n                 'bias', 'cate_est', 'cate_true', 'coverage', 'ci_width']\n    df_raw[col_order].to_csv(csv_path, index=False)\n    print(f\"Saved {csv_path} ({len(df_raw)} rows)\")\n\n\ndef build_summary(df_raw):\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse = compute_rmse(df_raw)\n    cov = compute_coverage(df_raw)\n    ciw = compute_ci_width(df_raw)\n    return abs_bias.merge(rmse, on=['n_expert', 'method']).merge(\n        cov, on=['n_expert', 'method']).merge(ciw, on=['n_expert', 'method'])\n\n\ndef write_analysis(summary_k4, summary_k2, df_k4, df_k2, outpath, profile):\n    lines = []\n    lines.append(\"# Gemma-2-9B Budget Sweep Analysis\\n\")\n    lines.append(\"## Design\\n\")\n    lines.append(f\"- N={N}, P(Z=1)={profile['p_z1']:.3f}\")\n    lines.append(f\"- tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1 - TAU_Z0:.1f}\")\n    lines.append(f\"- n_expert sweep: {N_EXPERT_LIST}\")\n    lines.append(f\"- {N_MC} MC seeds per budget\")\n    lines.append(\"- HB method: MAP-EB (Gamma(3,1) prior)\")\n    lines.append(f\"- |Bias| = avg across cells of |mean(bias) across seeds|\")\n    lines.append(f\"- RMSE = avg across cells of sqrt(mean(bias^2) across seeds)\")\n    lines.append(f\"- Coverage = avg across cells of fraction(95% CI contains true CATE)\")\n    lines.append(f\"- CI Width = avg across cells of mean(CI_width)\")\n    lines.append(\"\")\n\n    for k_label, summary, df_raw in [(\"K=4\", summary_k4, df_k4), (\"K=2\", summary_k2, df_k2)]:\n        lines.append(f\"## {k_label} Summary Table\\n\")\n        lines.append(\"| n_expert | |Bias|_naive | |Bias|_global | |Bias|_strat | |Bias|_echte | RMSE_naive | RMSE_global | RMSE_strat | RMSE_echte | Cov_naive | Cov_echte | CIW_naive | CIW_echte | HB_wins_bias? | HB_wins_rmse? |\")\n        lines.append(\"|----------|-------------|--------------|-------------|-------------|------------|-------------|------------|------------|-----------|-----------|-----------|-----------|---------------|---------------|\")\n\n        for ne in N_EXPERT_LIST:\n            sub = summary[summary['n_expert'] == ne]\n            vals = {}\n            for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n                row = sub[sub['method'] == m]\n                if len(row) > 0:\n                    vals[m] = {\n                        'abs_bias': row.iloc[0]['abs_bias'],\n                        'rmse': row.iloc[0]['rmse'],\n                        'coverage': row.iloc[0]['coverage'],\n                        'ci_width': row.iloc[0]['ci_width'],\n                    }\n                else:\n                    vals[m] = {'abs_bias': np.nan, 'rmse': np.nan, 'coverage': np.nan, 'ci_width': np.nan}\n\n            hb_wins_bias = \"YES\" if vals['hb_ec_hte']['abs_bias'] < vals['naive']['abs_bias'] else \"no\"\n            hb_wins_rmse = \"YES\" if vals['hb_ec_hte']['rmse'] < vals['naive']['rmse'] else \"no\"\n\n            lines.append(\n                f\"| {ne} \"\n                f\"| {vals['naive']['abs_bias']:.4f} \"\n                f\"| {vals['global_corrected']['abs_bias']:.4f} \"\n                f\"| {vals['stratified_mle']['abs_bias']:.4f} \"\n                f\"| {vals['hb_ec_hte']['abs_bias']:.4f} \"\n                f\"| {vals['naive']['rmse']:.4f} \"\n                f\"| {vals['global_corrected']['rmse']:.4f} \"\n                f\"| {vals['stratified_mle']['rmse']:.4f} \"\n                f\"| {vals['hb_ec_hte']['rmse']:.4f} \"\n                f\"| {vals['naive']['coverage']:.3f} \"\n                f\"| {vals['hb_ec_hte']['coverage']:.3f} \"\n                f\"| {vals['naive']['ci_width']:.4f} \"\n                f\"| {vals['hb_ec_hte']['ci_width']:.4f} \"\n                f\"| {hb_wins_bias} \"\n                f\"| {hb_wins_rmse} |\"\n            )\n        lines.append(\"\")\n\n        # Crossover analysis\n        lines.append(f\"### {k_label} Crossover Analysis\\n\")\n        crossover_bias = None\n        crossover_rmse = None\n        for ne in N_EXPERT_LIST:\n            sub = summary[summary['n_expert'] == ne]\n            hb = sub[sub['method'] == 'hb_ec_hte']\n            nv = sub[sub['method'] == 'naive']\n            if len(hb) > 0 and len(nv) > 0:\n                if hb.iloc[0]['abs_bias'] < nv.iloc[0]['abs_bias'] and crossover_bias is None:\n                    crossover_bias = ne\n                if hb.iloc[0]['rmse'] < nv.iloc[0]['rmse'] and crossover_rmse is None:\n                    crossover_rmse = ne\n\n        if crossover_bias is not None:\n            lines.append(f\"- **|Bias| crossover**: EC-HTE beats Naive at n_expert={crossover_bias}\")\n        else:\n            lines.append(\"- **|Bias| crossover**: EC-HTE never beats Naive in tested range\")\n        if crossover_rmse is not None:\n            lines.append(f\"- **RMSE crossover**: EC-HTE beats Naive at n_expert={crossover_rmse}\")\n        else:\n            lines.append(\"- **RMSE crossover**: EC-HTE never beats Naive in tested range\")\n        lines.append(\"\")\n\n        # Bias-variance decomposition\n        lines.append(f\"### {k_label} Bias-Variance Decomposition\\n\")\n        lines.append(\"| n_expert | Method | Bias^2 | Variance | MSE |\")\n        lines.append(\"|----------|--------|--------|----------|-----|\")\n        for ne in N_EXPERT_LIST:\n            for m in ['naive', 'hb_ec_hte']:\n                sub_df = df_raw[(df_raw['n_expert'] == ne) & (df_raw['method'] == m)]\n                cell_stats = (sub_df.groupby(['subgroup', 'z_level'])['bias']\n                              .agg(['mean', 'var', 'count']).reset_index())\n                mean_bias_sq = (cell_stats['mean'] ** 2).mean()\n                variance = cell_stats['var'].mean()\n                mse = mean_bias_sq + variance\n                lines.append(f\"| {ne} | {m} | {mean_bias_sq:.4f} | {variance:.4f} | {mse:.4f} |\")\n        lines.append(\"\")\n\n    # K=4 vs K=2 comparison\n    lines.append(\"## K=4 vs K=2 Comparison\\n\")\n    lines.append(\"| n_expert | |Bias|_echte_K4 | |Bias|_echte_K2 | RMSE_echte_K4 | RMSE_echte_K2 | Cov_echte_K4 | Cov_echte_K2 |\")\n    lines.append(\"|----------|----------------|----------------|---------------|---------------|--------------|--------------|\")\n    for ne in N_EXPERT_LIST:\n        hb4 = summary_k4[(summary_k4['n_expert'] == ne) & (summary_k4['method'] == 'hb_ec_hte')]\n        hb2 = summary_k2[(summary_k2['n_expert'] == ne) & (summary_k2['method'] == 'hb_ec_hte')]\n        if len(hb4) > 0 and len(hb2) > 0:\n            lines.append(\n                f\"| {ne} \"\n                f\"| {hb4.iloc[0]['abs_bias']:.4f} \"\n                f\"| {hb2.iloc[0]['abs_bias']:.4f} \"\n                f\"| {hb4.iloc[0]['rmse']:.4f} \"\n                f\"| {hb2.iloc[0]['rmse']:.4f} \"\n                f\"| {hb4.iloc[0]['coverage']:.3f} \"\n                f\"| {hb2.iloc[0]['coverage']:.3f} |\"\n            )\n    lines.append(\"\")\n\n    report = \"\\n\".join(lines)\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    csv_path = 'artifacts/c1_multi_llm/gemma2_9b_balanced.csv'\n    profile = compute_cm_profile(csv_path)\n\n    # Prepare K=4 config\n    k4_labels = profile['k4']['labels']\n    k4_weights = profile['k4']['weights']\n    k4_cm = profile['k4']['cm']\n\n    # Prepare K=2 config\n    k2_labels = profile['k2']['labels']\n    k2_weights = profile['k2']['weights']\n    k2_cm = profile['k2']['cm']\n\n    p_z1 = profile['p_z1']\n\n    # Dry run K=4\n    print(\"\\n\\n=== DRY RUN K=4 ===\")\n    run_sweep(\"K=4\", k4_labels, k4_weights, k4_cm, p_z1, dry_run=True)\n\n    # Dry run K=2\n    print(\"\\n\\n=== DRY RUN K=2 ===\")\n    run_sweep(\"K=2\", k2_labels, k2_weights, k2_cm, p_z1, dry_run=True)\n\n    # Full K=4\n    print(\"\\n\\n=== FULL RUN K=4 ===\")\n    df_k4 = run_sweep(\"K=4\", k4_labels, k4_weights, k4_cm, p_z1, dry_run=False)\n    save_sweep_csv(df_k4, f'{OUT_DIR}/gemma_budget_sweep_k4.csv')\n\n    # Full K=2\n    print(\"\\n\\n=== FULL RUN K=2 ===\")\n    df_k2 = run_sweep(\"K=2\", k2_labels, k2_weights, k2_cm, p_z1, dry_run=False)\n    save_sweep_csv(df_k2, f'{OUT_DIR}/gemma_budget_sweep_k2.csv')\n\n    # Build summaries and write analysis\n    summary_k4 = build_summary(df_k4)\n    summary_k2 = build_summary(df_k2)\n\n    write_analysis(summary_k4, summary_k2, df_k4, df_k2,\n                   f'{OUT_DIR}/gemma_sweep_analysis.md', profile)\n\n    # Print final summary\n    print(\"\\n\\n=== FINAL SUMMARY ===\")\n    for k_label, summary in [(\"K=4\", summary_k4), (\"K=2\", summary_k2)]:\n        print(f\"\\n{k_label}:\")\n        for ne in N_EXPERT_LIST:\n            print(f\"  n_expert={ne}:\")\n            for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n                row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n                if len(row) > 0:\n                    print(f\"    {m:20s}: |Bias|={row.iloc[0]['abs_bias']:.4f}  RMSE={row.iloc[0]['rmse']:.4f}  Cov={row.iloc[0]['coverage']:.3f}  CIW={row.iloc[0]['ci_width']:.4f}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "cd306621-f39b-4702-b3cf-3339573103ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0144BVmMkQ2z3zrEEf7RTmZq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10342,
      "cache_read_input_tokens": 18156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10342
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

_source line 12 · 2026-05-21T22:13:06.989Z_

<details><summary>↩ Tool result · `toolu_01YCZ5Dh752uppihoFaaL1Ui`</summary>

```text
File created successfully at: /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_gemma_sweep.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "e43372be-9d34-4fe9-8fc0-9020e2a6bad4",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_gemma_sweep.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nGemma-2-9B full pipeline: CM profile + budget sweep (K=4 and K=2).\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.optimize import minimize_scalar\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\nOUT_DIR = 'artifacts/c1_multi_llm'\n\n# === Step 1: Compute per-subgroup CM from CSV ===\n\ndef compute_cm_profile(csv_path):\n    df = pd.read_csv(csv_path)\n\n    # Balanced binary Z\n    df['Z'] = (df['true_label'] >= 1).astype(int)\n    df['Z_hat'] = (df['llm_label'] >= 1).astype(int)\n\n    # Global stats\n    acc = (df['Z'] == df['Z_hat']).mean()\n    p_z1 = df['Z'].mean()\n\n    # Global FPR, FNR\n    neg = df[df['Z'] == 0]\n    pos = df[df['Z'] == 1]\n    fpr_global = (neg['Z_hat'] == 1).mean()\n    fnr_global = (pos['Z_hat'] == 0).mean()\n\n    print(f\"=== Gemma CM Profile ===\")\n    print(f\"N = {len(df)}, Accuracy = {acc:.3f}\")\n    print(f\"P(Z=1) = {p_z1:.3f}\")\n    print(f\"Global FPR = {fpr_global:.3f}, FNR = {fnr_global:.3f}\")\n    print(f\"Delta_pi = |FPR - FNR| = {abs(fpr_global - fnr_global):.3f}\")\n    print()\n\n    # K=4: has_hashtag x text_length_bin (exclude \"long\")\n    df_k4 = df[df['text_length_bin'] != 'long'].copy()\n    df_k4['subgroup'] = df_k4['has_hashtag'].astype(str) + '_' + df_k4['text_length_bin']\n    k4_labels = sorted(df_k4['subgroup'].unique())\n\n    print(f\"K=4 subgroups (excluding 'long'): {k4_labels}\")\n    print(f\"K=4 sample size: {len(df_k4)}\")\n\n    k4_cm = {}\n    k4_weights = {}\n    k4_pi = {}\n    k4_kappa = {}\n\n    for s in k4_labels:\n        sub = df_k4[df_k4['subgroup'] == s]\n        n_s = len(sub)\n        w_s = n_s / len(df_k4)\n        neg_s = sub[sub['Z'] == 0]\n        pos_s = sub[sub['Z'] == 1]\n        fpr_s = (neg_s['Z_hat'] == 1).mean() if len(neg_s) > 0 else 0.0\n        fnr_s = (pos_s['Z_hat'] == 0).mean() if len(pos_s) > 0 else 0.0\n        pi_s = sub['Z'].mean()\n        kappa_s = 1.0 / (1.0 - fpr_s - fnr_s) if abs(1.0 - fpr_s - fnr_s) > 1e-10 else float('inf')\n\n        k4_cm[s] = {'fpr': round(fpr_s, 3), 'fnr': round(fnr_s, 3)}\n        k4_weights[s] = round(w_s, 3)\n        k4_pi[s] = round(pi_s, 3)\n        k4_kappa[s] = round(kappa_s, 2)\n\n        print(f\"  {s:20s}: n={n_s:4d}, w={w_s:.3f}, pi={pi_s:.3f}, FPR={fpr_s:.3f}, FNR={fnr_s:.3f}, kappa={kappa_s:.2f}\")\n\n    print()\n\n    # K=2: has_hashtag only\n    df['subgroup_k2'] = df['has_hashtag'].astype(str)\n    k2_labels = sorted(df['subgroup_k2'].unique())\n\n    print(f\"K=2 subgroups: {k2_labels}\")\n\n    k2_cm = {}\n    k2_weights = {}\n    k2_pi = {}\n    k2_kappa = {}\n\n    for s in k2_labels:\n        sub = df[df['subgroup_k2'] == s]\n        n_s = len(sub)\n        w_s = n_s / len(df)\n        neg_s = sub[sub['Z'] == 0]\n        pos_s = sub[sub['Z'] == 1]\n        fpr_s = (neg_s['Z_hat'] == 1).mean() if len(neg_s) > 0 else 0.0\n        fnr_s = (pos_s['Z_hat'] == 0).mean() if len(pos_s) > 0 else 0.0\n        pi_s = sub['Z'].mean()\n        kappa_s = 1.0 / (1.0 - fpr_s - fnr_s) if abs(1.0 - fpr_s - fnr_s) > 1e-10 else float('inf')\n\n        k2_cm[s] = {'fpr': round(fpr_s, 3), 'fnr': round(fnr_s, 3)}\n        k2_weights[s] = round(w_s, 3)\n        k2_pi[s] = round(pi_s, 3)\n        k2_kappa[s] = round(kappa_s, 2)\n\n        print(f\"  {s:20s}: n={n_s:4d}, w={w_s:.3f}, pi={pi_s:.3f}, FPR={fpr_s:.3f}, FNR={fnr_s:.3f}, kappa={kappa_s:.2f}\")\n\n    print()\n\n    # Write CM profile markdown\n    lines = []\n    lines.append(\"# Gemma-2-9B Confusion Matrix Profile\\n\")\n    lines.append(\"## Global Statistics\\n\")\n    lines.append(f\"- N = {len(df)}\")\n    lines.append(f\"- Accuracy = {acc:.3f}\")\n    lines.append(f\"- P(Z=1) = {p_z1:.3f}\")\n    lines.append(f\"- Global FPR = {fpr_global:.3f}\")\n    lines.append(f\"- Global FNR = {fnr_global:.3f}\")\n    lines.append(f\"- Delta_pi = |FPR - FNR| = {abs(fpr_global - fnr_global):.3f}\")\n    lines.append(f\"- FNR > FPR asymmetry: {'YES' if fnr_global > fpr_global else 'NO'}\")\n    lines.append(\"\")\n\n    lines.append(\"## K=4 Subgroups (has_hashtag x text_length_bin, excl. long)\\n\")\n    lines.append(f\"- Sample size (excl. long): {len(df_k4)}\")\n    lines.append(\"\")\n    lines.append(\"| Subgroup | n | Weight | pi_s | FPR | FNR | kappa |\")\n    lines.append(\"|----------|---|--------|------|-----|-----|-------|\")\n    for s in k4_labels:\n        sub = df_k4[df_k4['subgroup'] == s]\n        lines.append(f\"| {s} | {len(sub)} | {k4_weights[s]:.3f} | {k4_pi[s]:.3f} | {k4_cm[s]['fpr']:.3f} | {k4_cm[s]['fnr']:.3f} | {k4_kappa[s]:.2f} |\")\n    lines.append(\"\")\n\n    max_kappa_k4 = max(k4_kappa.values())\n    lines.append(f\"- Max kappa = {max_kappa_k4:.2f}\")\n    prop2_count = sum(1 for s in k4_labels if k4_kappa[s] > 2.0)\n    lines.append(f\"- Prop2 triggered (kappa > 2): {prop2_count}/{len(k4_labels)}\")\n    lines.append(\"\")\n\n    lines.append(\"## K=2 Subgroups (has_hashtag only)\\n\")\n    lines.append(\"| Subgroup | n | Weight | pi_s | FPR | FNR | kappa |\")\n    lines.append(\"|----------|---|--------|------|-----|-----|-------|\")\n    for s in k2_labels:\n        sub = df[df['subgroup_k2'] == s]\n        lines.append(f\"| {s} | {len(sub)} | {k2_weights[s]:.3f} | {k2_pi[s]:.3f} | {k2_cm[s]['fpr']:.3f} | {k2_cm[s]['fnr']:.3f} | {k2_kappa[s]:.2f} |\")\n    lines.append(\"\")\n\n    max_kappa_k2 = max(k2_kappa.values())\n    lines.append(f\"- Max kappa = {max_kappa_k2:.2f}\")\n    lines.append(\"\")\n\n    profile_path = f'{OUT_DIR}/gemma_cm_profile.md'\n    with open(profile_path, 'w') as f:\n        f.write(\"\\n\".join(lines))\n    print(f\"Wrote {profile_path}\")\n\n    return {\n        'p_z1': p_z1,\n        'k4': {'labels': k4_labels, 'weights': k4_weights, 'cm': k4_cm},\n        'k2': {'labels': k2_labels, 'weights': k2_weights, 'cm': k2_cm},\n    }\n\n\n# === Config ===\n\nN = 5000\nN_EXPERT_LIST = [100, 200, 500, 1000, 2000]\nN_MC = 50\nSEED_BASE = 0\nTAU_Z0 = 0.35\nTAU_Z1 = 0.65\n\n\n# === Estimators ===\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === MAP-EB ===\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):\n    hp_rate = 1.0 / hp_scale\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = hp_shape * hp_scale\n            continue\n\n        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):\n            nll = _dirmult_neg_ll(a, _cl)\n            if a < 1e-10:\n                return 1e10\n            log_prior = (_shape - 1.0) * np.log(a) - _rate * a\n            return nll - log_prior\n\n        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n_sz = counts[i, z, :].sum()\n            d = n_sz + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    return C, alpha_opt\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\n# === DGP ===\n\ndef generate_data(seed, n_expert, subgroup_labels, subgroup_weights, subgroup_cm, p_z1):\n    rng = np.random.RandomState(seed)\n    k = len(subgroup_labels)\n\n    S_idx = rng.choice(k, size=N, p=subgroup_weights)\n    S = np.array([subgroup_labels[i] for i in S_idx])\n\n    Z = rng.binomial(1, p_z1, N)\n    T = rng.binomial(1, 0.5, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(k):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(subgroup_cm[subgroup_labels[i]]['fpr'],\n                           subgroup_cm[subgroup_labels[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed, subgroup_labels):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, subgroup_labels)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, subgroup_labels)\n    C_hb, _ = estimate_cm_hb_map_eb(counts, subgroup_labels)\n\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in subgroup_labels:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in subgroup_labels:\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            ci_w_nv = (ci_hi_nv - ci_lo_nv) if not np.isnan(ci_lo_nv) else np.nan\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'cate_est': th_nv, 'cate_true': oracle_cate,\n                'coverage': cov_nv, 'ci_width': ci_w_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            ci_w_gc = (ci_hi_gc - ci_lo_gc) if not np.isnan(ci_lo_gc) else np.nan\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'cate_est': th_gc, 'cate_true': oracle_cate,\n                'coverage': cov_gc, 'ci_width': ci_w_gc,\n            })\n\n            # Stratified MLE\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            ci_w_ml = (ci_hi_ml - ci_lo_ml) if not np.isnan(ci_lo_ml) else np.nan\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'cate_est': th_ml, 'cate_true': oracle_cate,\n                'coverage': cov_ml, 'ci_width': ci_w_ml,\n            })\n\n            # HB EC-HTE (MAP-EB)\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            ci_w_hb = (ci_hi_hb - ci_lo_hb) if not np.isnan(ci_lo_hb) else np.nan\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'cate_est': th_hb, 'cate_true': oracle_cate,\n                'coverage': cov_hb, 'ci_width': ci_w_hb,\n            })\n\n    return rows\n\n\n# === Aggregation ===\n\ndef compute_corrected_abs_bias(df):\n    cell_bias = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias']\n                 .mean().abs().reset_index(name='abs_mean_bias'))\n    return (cell_bias.groupby(['n_expert', 'method'])['abs_mean_bias']\n            .mean().reset_index(name='abs_bias'))\n\n\ndef compute_rmse(df):\n    cell_rmse = (df.assign(bias_sq=df['bias'] ** 2)\n                 .groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias_sq']\n                 .mean().apply(np.sqrt).reset_index(name='rmse'))\n    return (cell_rmse.groupby(['n_expert', 'method'])['rmse']\n            .mean().reset_index(name='rmse'))\n\n\ndef compute_coverage(df):\n    return (df.groupby(['n_expert', 'method'])['coverage']\n            .mean().reset_index(name='coverage'))\n\n\ndef compute_ci_width(df):\n    cell_w = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['ci_width']\n              .mean().reset_index(name='ci_width'))\n    return (cell_w.groupby(['n_expert', 'method'])['ci_width']\n            .mean().reset_index(name='ci_width'))\n\n\n# === Run sweep for one K config ===\n\ndef run_sweep(k_label, subgroup_labels, subgroup_weights_dict, subgroup_cm, p_z1, dry_run=False):\n    labels = subgroup_labels\n    weights_arr = np.array([subgroup_weights_dict[s] for s in labels])\n    weights_arr = weights_arr / weights_arr.sum()  # normalize\n\n    print(f\"\\n{'='*60}\")\n    print(f\"Budget Sweep: Gemma {k_label}\")\n    print(f\"Subgroups: {labels}\")\n    print(f\"Weights: {dict(zip(labels, [round(w, 3) for w in weights_arr]))}\")\n    print(f\"P(Z=1) = {p_z1:.3f}\")\n    print(f\"tau(z=0) = {TAU_Z0}, tau(z=1) = {TAU_Z1}\")\n    print(f\"{'='*60}\")\n\n    if dry_run:\n        print(\"\\n--- Dry run (n_expert=100, 1 seed) ---\")\n        data = generate_data(SEED_BASE, 100, labels, weights_arr, subgroup_cm, p_z1)\n        rows = run_one_mc(data, SEED_BASE, labels)\n        df_dry = pd.DataFrame(rows)\n        df_dry['n_expert'] = 100\n        print(f\"Dry run OK: {len(df_dry)} rows\")\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            sub = df_dry[df_dry['method'] == m]\n            bias = sub['bias'].abs().mean()\n            print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n        return None\n\n    # Full run\n    print(f\"\\nFull run: {len(N_EXPERT_LIST)} budgets x {N_MC} seeds\")\n    all_results = []\n    t0 = time.time()\n    total_runs = len(N_EXPERT_LIST) * N_MC\n    run_count = 0\n\n    for n_expert in N_EXPERT_LIST:\n        print(f\"\\n--- n_expert = {n_expert} ---\")\n        t_budget = time.time()\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            data = generate_data(seed, n_expert, labels, weights_arr, subgroup_cm, p_z1)\n            mc_rows = run_one_mc(data, seed, labels)\n            for r in mc_rows:\n                r['n_expert'] = n_expert\n            all_results.extend(mc_rows)\n            run_count += 1\n            if (mc + 1) % 10 == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / run_count * (total_runs - run_count)\n                print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n        budget_time = time.time() - t_budget\n        print(f\"  n_expert={n_expert} done in {budget_time:.1f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(all_results)\n    return df_raw\n\n\ndef save_sweep_csv(df_raw, csv_path):\n    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level',\n                 'bias', 'cate_est', 'cate_true', 'coverage', 'ci_width']\n    df_raw[col_order].to_csv(csv_path, index=False)\n    print(f\"Saved {csv_path} ({len(df_raw)} rows)\")\n\n\ndef build_summary(df_raw):\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse = compute_rmse(df_raw)\n    cov = compute_coverage(df_raw)\n    ciw = compute_ci_width(df_raw)\n    return abs_bias.merge(rmse, on=['n_expert', 'method']).merge(\n        cov, on=['n_expert', 'method']).merge(ciw, on=['n_expert', 'method'])\n\n\ndef write_analysis(summary_k4, summary_k2, df_k4, df_k2, outpath, profile):\n    lines = []\n    lines.append(\"# Gemma-2-9B Budget Sweep Analysis\\n\")\n    lines.append(\"## Design\\n\")\n    lines.append(f\"- N={N}, P(Z=1)={profile['p_z1']:.3f}\")\n    lines.append(f\"- tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1 - TAU_Z0:.1f}\")\n    lines.append(f\"- n_expert sweep: {N_EXPERT_LIST}\")\n    lines.append(f\"- {N_MC} MC seeds per budget\")\n    lines.append(\"- HB method: MAP-EB (Gamma(3,1) prior)\")\n    lines.append(f\"- |Bias| = avg across cells of |mean(bias) across seeds|\")\n    lines.append(f\"- RMSE = avg across cells of sqrt(mean(bias^2) across seeds)\")\n    lines.append(f\"- Coverage = avg across cells of fraction(95% CI contains true CATE)\")\n    lines.append(f\"- CI Width = avg across cells of mean(CI_width)\")\n    lines.append(\"\")\n\n    for k_label, summary, df_raw in [(\"K=4\", summary_k4, df_k4), (\"K=2\", summary_k2, df_k2)]:\n        lines.append(f\"## {k_label} Summary Table\\n\")\n        lines.append(\"| n_expert | |Bias|_naive | |Bias|_global | |Bias|_strat | |Bias|_echte | RMSE_naive | RMSE_global | RMSE_strat | RMSE_echte | Cov_naive | Cov_echte | CIW_naive | CIW_echte | HB_wins_bias? | HB_wins_rmse? |\")\n        lines.append(\"|----------|-------------|--------------|-------------|-------------|------------|-------------|------------|------------|-----------|-----------|-----------|-----------|---------------|---------------|\")\n\n        for ne in N_EXPERT_LIST:\n            sub = summary[summary['n_expert'] == ne]\n            vals = {}\n            for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n                row = sub[sub['method'] == m]\n                if len(row) > 0:\n                    vals[m] = {\n                        'abs_bias': row.iloc[0]['abs_bias'],\n                        'rmse': row.iloc[0]['rmse'],\n                        'coverage': row.iloc[0]['coverage'],\n                        'ci_width': row.iloc[0]['ci_width'],\n                    }\n                else:\n                    vals[m] = {'abs_bias': np.nan, 'rmse': np.nan, 'coverage': np.nan, 'ci_width': np.nan}\n\n            hb_wins_bias = \"YES\" if vals['hb_ec_hte']['abs_bias'] < vals['naive']['abs_bias'] else \"no\"\n            hb_wins_rmse = \"YES\" if vals['hb_ec_hte']['rmse'] < vals['naive']['rmse'] else \"no\"\n\n            lines.append(\n                f\"| {ne} \"\n                f\"| {vals['naive']['abs_bias']:.4f} \"\n                f\"| {vals['global_corrected']['abs_bias']:.4f} \"\n                f\"| {vals['stratified_mle']['abs_bias']:.4f} \"\n                f\"| {vals['hb_ec_hte']['abs_bias']:.4f} \"\n                f\"| {vals['naive']['rmse']:.4f} \"\n                f\"| {vals['global_corrected']['rmse']:.4f} \"\n                f\"| {vals['stratified_mle']['rmse']:.4f} \"\n                f\"| {vals['hb_ec_hte']['rmse']:.4f} \"\n                f\"| {vals['naive']['coverage']:.3f} \"\n                f\"| {vals['hb_ec_hte']['coverage']:.3f} \"\n                f\"| {vals['naive']['ci_width']:.4f} \"\n                f\"| {vals['hb_ec_hte']['ci_width']:.4f} \"\n                f\"| {hb_wins_bias} \"\n                f\"| {hb_wins_rmse} |\"\n            )\n        lines.append(\"\")\n\n        # Crossover analysis\n        lines.append(f\"### {k_label} Crossover Analysis\\n\")\n        crossover_bias = None\n        crossover_rmse = None\n        for ne in N_EXPERT_LIST:\n            sub = summary[summary['n_expert'] == ne]\n            hb = sub[sub['method'] == 'hb_ec_hte']\n            nv = sub[sub['method'] == 'naive']\n            if len(hb) > 0 and len(nv) > 0:\n                if hb.iloc[0]['abs_bias'] < nv.iloc[0]['abs_bias'] and crossover_bias is None:\n                    crossover_bias = ne\n                if hb.iloc[0]['rmse'] < nv.iloc[0]['rmse'] and crossover_rmse is None:\n                    crossover_rmse = ne\n\n        if crossover_bias is not None:\n            lines.append(f\"- **|Bias| crossover**: EC-HTE beats Naive at n_expert={crossover_bias}\")\n        else:\n            lines.append(\"- **|Bias| crossover**: EC-HTE never beats Naive in tested range\")\n        if crossover_rmse is not None:\n            lines.append(f\"- **RMSE crossover**: EC-HTE beats Naive at n_expert={crossover_rmse}\")\n        else:\n            lines.append(\"- **RMSE crossover**: EC-HTE never beats Naive in tested range\")\n        lines.append(\"\")\n\n        # Bias-variance decomposition\n        lines.append(f\"### {k_label} Bias-Variance Decomposition\\n\")\n        lines.append(\"| n_expert | Method | Bias^2 | Variance | MSE |\")\n        lines.append(\"|----------|--------|--------|----------|-----|\")\n        for ne in N_EXPERT_LIST:\n            for m in ['naive', 'hb_ec_hte']:\n                sub_df = df_raw[(df_raw['n_expert'] == ne) & (df_raw['method'] == m)]\n                cell_stats = (sub_df.groupby(['subgroup', 'z_level'])['bias']\n                              .agg(['mean', 'var', 'count']).reset_index())\n                mean_bias_sq = (cell_stats['mean'] ** 2).mean()\n                variance = cell_stats['var'].mean()\n                mse = mean_bias_sq + variance\n                lines.append(f\"| {ne} | {m} | {mean_bias_sq:.4f} | {variance:.4f} | {mse:.4f} |\")\n        lines.append(\"\")\n\n    # K=4 vs K=2 comparison\n    lines.append(\"## K=4 vs K=2 Comparison\\n\")\n    lines.append(\"| n_expert | |Bias|_echte_K4 | |Bias|_echte_K2 | RMSE_echte_K4 | RMSE_echte_K2 | Cov_echte_K4 | Cov_echte_K2 |\")\n    lines.append(\"|----------|----------------|----------------|---------------|---------------|--------------|--------------|\")\n    for ne in N_EXPERT_LIST:\n        hb4 = summary_k4[(summary_k4['n_expert'] == ne) & (summary_k4['method'] == 'hb_ec_hte')]\n        hb2 = summary_k2[(summary_k2['n_expert'] == ne) & (summary_k2['method'] == 'hb_ec_hte')]\n        if len(hb4) > 0 and len(hb2) > 0:\n            lines.append(\n                f\"| {ne} \"\n                f\"| {hb4.iloc[0]['abs_bias']:.4f} \"\n                f\"| {hb2.iloc[0]['abs_bias']:.4f} \"\n                f\"| {hb4.iloc[0]['rmse']:.4f} \"\n                f\"| {hb2.iloc[0]['rmse']:.4f} \"\n                f\"| {hb4.iloc[0]['coverage']:.3f} \"\n                f\"| {hb2.iloc[0]['coverage']:.3f} |\"\n            )\n    lines.append(\"\")\n\n    report = \"\\n\".join(lines)\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    csv_path = 'artifacts/c1_multi_llm/gemma2_9b_balanced.csv'\n    profile = compute_cm_profile(csv_path)\n\n    # Prepare K=4 config\n    k4_labels = profile['k4']['labels']\n    k4_weights = profile['k4']['weights']\n    k4_cm = profile['k4']['cm']\n\n    # Prepare K=2 config\n    k2_labels = profile['k2']['labels']\n    k2_weights = profile['k2']['weights']\n    k2_cm = profile['k2']['cm']\n\n    p_z1 = profile['p_z1']\n\n    # Dry run K=4\n    print(\"\\n\\n=== DRY RUN K=4 ===\")\n    run_sweep(\"K=4\", k4_labels, k4_weights, k4_cm, p_z1, dry_run=True)\n\n    # Dry run K=2\n    print(\"\\n\\n=== DRY RUN K=2 ===\")\n    run_sweep(\"K=2\", k2_labels, k2_weights, k2_cm, p_z1, dry_run=True)\n\n    # Full K=4\n    print(\"\\n\\n=== FULL RUN K=4 ===\")\n    df_k4 = run_sweep(\"K=4\", k4_labels, k4_weights, k4_cm, p_z1, dry_run=False)\n    save_sweep_csv(df_k4, f'{OUT_DIR}/gemma_budget_sweep_k4.csv')\n\n    # Full K=2\n    print(\"\\n\\n=== FULL RUN K=2 ===\")\n    df_k2 = run_sweep(\"K=2\", k2_labels, k2_weights, k2_cm, p_z1, dry_run=False)\n    save_sweep_csv(df_k2, f'{OUT_DIR}/gemma_budget_sweep_k2.csv')\n\n    # Build summaries and write analysis\n    summary_k4 = build_summary(df_k4)\n    summary_k2 = build_summary(df_k2)\n\n    write_analysis(summary_k4, summary_k2, df_k4, df_k2,\n                   f'{OUT_DIR}/gemma_sweep_analysis.md', profile)\n\n    # Print final summary\n    print(\"\\n\\n=== FINAL SUMMARY ===\")\n    for k_label, summary in [(\"K=4\", summary_k4), (\"K=2\", summary_k2)]:\n        print(f\"\\n{k_label}:\")\n        for ne in N_EXPERT_LIST:\n            print(f\"  n_expert={ne}:\")\n            for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n                row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n                if len(row) > 0:\n                    print(f\"    {m:20s}: |Bias|={row.iloc[0]['abs_bias']:.4f}  RMSE={row.iloc[0]['rmse']:.4f}  Cov={row.iloc[0]['coverage']:.3f}  CIW={row.iloc[0]['ci_width']:.4f}\")\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 13_

Running the script now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "8a93e1b4-f3ad-4dbb-a3c3-c6c6be0827b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MkYbiwF4tZeFWhRYpPstn4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11971,
      "cache_read_input_tokens": 28498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11971
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

_source line 14_

<details open><summary>🔧 Tool call — Bash · `toolu_013m5DtfZCUwfCWgmvgmhMMF`</summary>

```json
{
  "command": "python artifacts/c1_multi_llm/run_gemma_sweep.py 2>&1",
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
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "ff039785-a2ab-4331-84e3-792b0123e46b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MkYbiwF4tZeFWhRYpPstn4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11971,
      "cache_read_input_tokens": 28498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11971
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

_source line 15 · 2026-05-21T22:13:10.490Z_

<details><summary>↩ Tool result · reported error · `toolu_013m5DtfZCUwfCWgmvgmhMMF`</summary>

```text
Exit code 127
/bin/bash: line 1: python: command not found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "d3717219-f2cd-431f-9037-2709eac2d504",
  "tool_use_result": "Error: Exit code 127\n/bin/bash: line 1: python: command not found"
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_013o3AmGr7kAaNjonYZWBEhp`</summary>

```json
{
  "command": "which python3 && python3 artifacts/c1_multi_llm/run_gemma_sweep.py 2>&1",
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
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "f518a01f-d18e-42c8-9f6d-6ad74b1e1056",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G9GHELXFfRqnyoFz1nnN5b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 137,
      "cache_read_input_tokens": 40469,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 137
      },
      "output_tokens": 66,
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

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bjxa3mcf5",
  "tool_use_id": "toolu_013o3AmGr7kAaNjonYZWBEhp",
  "description": "which python3 && python3 artifacts/c1_multi_llm/run_gemma_sweep.py 2>&1",
  "task_type": "local_bash",
  "uuid": "3297f1f7-de6d-4b61-904c-0f1f06833941",
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc"
}
```

---

### System

_source line 18_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bjxa3mcf5",
  "tool_use_id": "toolu_013o3AmGr7kAaNjonYZWBEhp",
  "status": "completed",
  "output_file": "",
  "summary": "which python3 && python3 artifacts/c1_multi_llm/run_gemma_sweep.py 2>&1",
  "uuid": "39547012-5c51-4a3e-bda2-d435054c69b8",
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc"
}
```

---

### Tool result

_source line 19 · 2026-05-21T22:13:20.208Z_

<details><summary>↩ Tool result · `toolu_013o3AmGr7kAaNjonYZWBEhp`</summary>

```text
/usr/bin/python3
=== Gemma CM Profile ===
N = 500, Accuracy = 0.764
P(Z=1) = 0.652
Global FPR = 0.098, FNR = 0.310
Delta_pi = |FPR - FNR| = 0.212

K=4 subgroups (excluding 'long'): ['False_medium', 'False_short', 'True_medium', 'True_short']
K=4 sample size: 490
  False_medium        : n= 187, w=0.382, pi=0.465, FPR=0.110, FNR=0.437, kappa=2.21
  False_short         : n= 109, w=0.222, pi=0.734, FPR=0.138, FNR=0.300, kappa=1.78
  True_medium         : n= 125, w=0.255, pi=0.760, FPR=0.033, FNR=0.263, kappa=1.42
  True_short          : n=  69, w=0.141, pi=0.841, FPR=0.091, FNR=0.207, kappa=1.42

K=2 subgroups: ['False', 'True']
  False               : n= 302, w=0.604, pi=0.566, FPR=0.115, FNR=0.368, kappa=1.93
  True                : n= 198, w=0.396, pi=0.783, FPR=0.047, FNR=0.245, kappa=1.41

Wrote artifacts/c1_multi_llm/gemma_cm_profile.md


=== DRY RUN K=4 ===

============================================================
Budget Sweep: Gemma K=4
Subgroups: ['False_medium', 'False_short', 'True_medium', 'True_short']
Weights: {'False_medium': np.float64(0.382), 'False_short': np.float64(0.222), 'True_medium': np.float64(0.255), 'True_short': np.float64(0.141)}
P(Z=1) = 0.652
tau(z=0) = 0.35, tau(z=1) = 0.65
============================================================

--- Dry run (n_expert=100, 1 seed) ---
Dry run OK: 32 rows
  naive               : mean |bias| = 0.0663
  global_corrected    : mean |bias| = 0.0653
  stratified_mle      : mean |bias| = 0.0892
  hb_ec_hte           : mean |bias| = 0.0988


=== DRY RUN K=2 ===

============================================================
Budget Sweep: Gemma K=2
Subgroups: ['False', 'True']
Weights: {'False': np.float64(0.604), 'True': np.float64(0.396)}
P(Z=1) = 0.652
tau(z=0) = 0.35, tau(z=1) = 0.65
============================================================

--- Dry run (n_expert=100, 1 seed) ---
Dry run OK: 16 rows
  naive               : mean |bias| = 0.0517
  global_corrected    : mean |bias| = 0.1555
  stratified_mle      : mean |bias| = 0.1677
  hb_ec_hte           : mean |bias| = 0.1769


=== FULL RUN K=4 ===

============================================================
Budget Sweep: Gemma K=4
Subgroups: ['False_medium', 'False_short', 'True_medium', 'True_short']
Weights: {'False_medium': np.float64(0.382), 'False_short': np.float64(0.222), 'True_medium': np.float64(0.255), 'True_short': np.float64(0.141)}
P(Z=1) = 0.652
tau(z=0) = 0.35, tau(z=1) = 0.65
============================================================

Full run: 5 budgets x 50 seeds

--- n_expert = 100 ---
  [10/50] 0s elapsed, ETA 3s
  [20/50] 0s elapsed, ETA 3s
  [30/50] 0s elapsed, ETA 3s
  [40/50] 0s elapsed, ETA 3s
  [50/50] 1s elapsed, ETA 2s
  n_expert=100 done in 0.6s

--- n_expert = 200 ---
  [10/50] 1s elapsed, ETA 2s
  [20/50] 1s elapsed, ETA 2s
  [30/50] 1s elapsed, ETA 2s
  [40/50] 1s elapsed, ETA 2s
  [50/50] 1s elapsed, ETA 2s
  n_expert=200 done in 0.7s

--- n_expert = 500 ---
  [10/50] 1s elapsed, ETA 2s
  [20/50] 2s elapsed, ETA 2s
  [30/50] 2s elapsed, ETA 2s
  [40/50] 2s elapsed, ETA 1s
  [50/50] 2s elapsed, ETA 1s
  n_expert=500 done in 0.6s

--- n_expert = 1000 ---
  [10/50] 2s elapsed, ETA 1s
  [20/50] 2s elapsed, ETA 1s
  [30/50] 2s elapsed, ETA 1s
  [40/50] 2s elapsed, ETA 1s
  [50/50] 3s elapsed, ETA 1s
  n_expert=1000 done in 0.7s

--- n_expert = 2000 ---
  [10/50] 3s elapsed, ETA 1s
  [20/50] 3s elapsed, ETA 0s
  [30/50] 3s elapsed, ETA 0s
  [40/50] 3s elapsed, ETA 0s
  [50/50] 3s elapsed, ETA 0s
  n_expert=2000 done in 0.7s

Total time: 3.3s
Saved artifacts/c1_multi_llm/gemma_budget_sweep_k4.csv (8000 rows)


=== FULL RUN K=2 ===

============================================================
Budget Sweep: Gemma K=2
Subgroups: ['False', 'True']
Weights: {'False': np.float64(0.604), 'True': np.float64(0.396)}
P(Z=1) = 0.652
tau(z=0) = 0.35, tau(z=1) = 0.65
============================================================

Full run: 5 budgets x 50 seeds

--- n_expert = 100 ---
  [10/50] 0s elapsed, ETA 2s
  [20/50] 0s elapsed, ETA 2s
  [30/50] 0s elapsed, ETA 2s
  [40/50] 0s elapsed, ETA 2s
  [50/50] 0s elapsed, ETA 2s
  n_expert=100 done in 0.4s

--- n_expert = 200 ---
  [10/50] 1s elapsed, ETA 2s
  [20/50] 1s elapsed, ETA 2s
  [30/50] 1s elapsed, ETA 1s
  [40/50] 1s elapsed, ETA 1s
  [50/50] 1s elapsed, ETA 1s
  n_expert=200 done in 0.4s

--- n_expert = 500 ---
  [10/50] 1s elapsed, ETA 1s
  [20/50] 1s elapsed, ETA 1s
  [30/50] 1s elapsed, ETA 1s
  [40/50] 1s elapsed, ETA 1s
  [50/50] 1s elapsed, ETA 1s
  n_expert=500 done in 0.4s

--- n_expert = 1000 ---
  [10/50] 1s elapsed, ETA 1s
  [20/50] 1s elapsed, ETA 1s
  [30/50] 2s elapsed, ETA 1s
  [40/50] 2s elapsed, ETA 1s
  [50/50] 2s elapsed, ETA 0s
  n_expert=1000 done in 0.4s

--- n_expert = 2000 ---
  [10/50] 2s elapsed, ETA 0s
  [20/50] 2s elapsed, ETA 0s
  [30/50] 2s elapsed, ETA 0s
  [40/50] 2s elapsed, ETA 0s
  [50/50] 2s elapsed, ETA 0s
  n_expert=2000 done in 0.4s

Total time: 2.2s
Saved artifacts/c1_multi_llm/gemma_budget_sweep_k2.csv (4000 rows)
Wrote artifacts/c1_multi_llm/gemma_sweep_analysis.md


=== FINAL SUMMARY ===

K=4:
  n_expert=100:
    naive               : |Bias|=0.0711  RMSE=0.1192  Cov=0.775  CIW=0.3312
    global_corrected    : |Bias|=0.0202  RMSE=0.1950  Cov=0.860  CIW=0.5382
    stratified_mle      : |Bias|=0.1066  RMSE=0.6609  Cov=0.675  CIW=0.7715
    hb_ec_hte           : |Bias|=0.2106  RMSE=1.2291  Cov=0.690  CIW=0.8005
  n_expert=200:
    naive               : |Bias|=0.0711  RMSE=0.1192  Cov=0.775  CIW=0.3312
    global_corrected    : |Bias|=0.0223  RMSE=0.1682  Cov=0.887  CIW=0.5211
    stratified_mle      : |Bias|=0.0646  RMSE=0.3844  Cov=0.782  CIW=0.5890
    hb_ec_hte           : |Bias|=0.0676  RMSE=0.4212  Cov=0.790  CIW=0.5810
  n_expert=500:
    naive               : |Bias|=0.0711  RMSE=0.1192  Cov=0.775  CIW=0.3312
    global_corrected    : |Bias|=0.0172  RMSE=0.1480  Cov=0.907  CIW=0.5125
    stratified_mle      : |Bias|=0.0244  RMSE=0.1844  Cov=0.873  CIW=0.5197
    hb_ec_hte           : |Bias|=0.0233  RMSE=0.1824  Cov=0.873  CIW=0.5160
  n_expert=1000:
    naive               : |Bias|=0.0711  RMSE=0.1192  Cov=0.775  CIW=0.3312
    global_corrected    : |Bias|=0.0157  RMSE=0.1428  Cov=0.922  CIW=0.5106
    stratified_mle      : |Bias|=0.0180  RMSE=0.1549  Cov=0.900  CIW=0.5041
    hb_ec_hte           : |Bias|=0.0175  RMSE=0.1541  Cov=0.907  CIW=0.5025
  n_expert=2000:
    naive               : |Bias|=0.0711  RMSE=0.1192  Cov=0.775  CIW=0.3312
    global_corrected    : |Bias|=0.0160  RMSE=0.1377  Cov=0.920  CIW=0.5068
    stratified_mle      : |Bias|=0.0161  RMSE=0.1394  Cov=0.917  CIW=0.4947
    hb_ec_hte           : |Bias|=0.0156  RMSE=0.1390  Cov=0.917  CIW=0.4940

K=2:
  n_expert=100:
    naive               : |Bias|=0.0715  RMSE=0.0955  Cov=0.705  CIW=0.2268
    global_corrected    : |Bias|=0.0154  RMSE=0.1376  Cov=0.820  CIW=0.3585
    stratified_mle      : |Bias|=0.0250  RMSE=0.1895  Cov=0.740  CIW=0.3758
    hb_ec_hte           : |Bias|=0.0269  RMSE=0.1870  Cov=0.745  CIW=0.3694
  n_expert=200:
    naive               : |Bias|=0.0715  RMSE=0.0955  Cov=0.705  CIW=0.2268
    global_corrected    : |Bias|=0.0095  RMSE=0.1182  Cov=0.875  CIW=0.3475
    stratified_mle      : |Bias|=0.0112  RMSE=0.1412  Cov=0.775  CIW=0.3514
    hb_ec_hte           : |Bias|=0.0095  RMSE=0.1404  Cov=0.780  CIW=0.3489
  n_expert=500:
    naive               : |Bias|=0.0715  RMSE=0.0955  Cov=0.705  CIW=0.2268
    global_corrected    : |Bias|=0.0104  RMSE=0.1000  Cov=0.905  CIW=0.3436
    stratified_mle      : |Bias|=0.0130  RMSE=0.1111  Cov=0.875  CIW=0.3406
    hb_ec_hte           : |Bias|=0.0105  RMSE=0.1105  Cov=0.880  CIW=0.3397
  n_expert=1000:
    naive               : |Bias|=0.0715  RMSE=0.0955  Cov=0.705  CIW=0.2268
    global_corrected    : |Bias|=0.0100  RMSE=0.0889  Cov=0.945  CIW=0.3442
    stratified_mle      : |Bias|=0.0125  RMSE=0.0895  Cov=0.945  CIW=0.3394
    hb_ec_hte           : |Bias|=0.0122  RMSE=0.0892  Cov=0.945  CIW=0.3389
  n_expert=2000:
    naive               : |Bias|=0.0715  RMSE=0.0955  Cov=0.705  CIW=0.2268
    global_corrected    : |Bias|=0.0102  RMSE=0.0854  Cov=0.950  CIW=0.3416
    stratified_mle      : |Bias|=0.0177  RMSE=0.0860  Cov=0.925  CIW=0.3361
    hb_ec_hte           : |Bias|=0.0176  RMSE=0.0859  Cov=0.925  CIW=0.3359
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "c403b128-b08d-4df1-93ee-cf55ee56e69f",
  "tool_use_result": {
    "stdout": "/usr/bin/python3\n=== Gemma CM Profile ===\nN = 500, Accuracy = 0.764\nP(Z=1) = 0.652\nGlobal FPR = 0.098, FNR = 0.310\nDelta_pi = |FPR - FNR| = 0.212\n\nK=4 subgroups (excluding 'long'): ['False_medium', 'False_short', 'True_medium', 'True_short']\nK=4 sample size: 490\n  False_medium        : n= 187, w=0.382, pi=0.465, FPR=0.110, FNR=0.437, kappa=2.21\n  False_short         : n= 109, w=0.222, pi=0.734, FPR=0.138, FNR=0.300, kappa=1.78\n  True_medium         : n= 125, w=0.255, pi=0.760, FPR=0.033, FNR=0.263, kappa=1.42\n  True_short          : n=  69, w=0.141, pi=0.841, FPR=0.091, FNR=0.207, kappa=1.42\n\nK=2 subgroups: ['False', 'True']\n  False               : n= 302, w=0.604, pi=0.566, FPR=0.115, FNR=0.368, kappa=1.93\n  True                : n= 198, w=0.396, pi=0.783, FPR=0.047, FNR=0.245, kappa=1.41\n\nWrote artifacts/c1_multi_llm/gemma_cm_profile.md\n\n\n=== DRY RUN K=4 ===\n\n============================================================\nBudget Sweep: Gemma K=4\nSubgroups: ['False_medium', 'False_short', 'True_medium', 'True_short']\nWeights: {'False_medium': np.float64(0.382), 'False_short': np.float64(0.222), 'True_medium': np.float64(0.255), 'True_short': np.float64(0.141)}\nP(Z=1) = 0.652\ntau(z=0) = 0.35, tau(z=1) = 0.65\n============================================================\n\n--- Dry run (n_expert=100, 1 seed) ---\nDry run OK: 32 rows\n  naive               : mean |bias| = 0.0663\n  global_corrected    : mean |bias| = 0.0653\n  stratified_mle      : mean |bias| = 0.0892\n  hb_ec_hte           : mean |bias| = 0.0988\n\n\n=== DRY RUN K=2 ===\n\n============================================================\nBudget Sweep: Gemma K=2\nSubgroups: ['False', 'True']\nWeights: {'False': np.float64(0.604), 'True': np.float64(0.396)}\nP(Z=1) = 0.652\ntau(z=0) = 0.35, tau(z=1) = 0.65\n============================================================\n\n--- Dry run (n_expert=100, 1 seed) ---\nDry run OK: 16 rows\n  naive               : mean |bias| = 0.0517\n  global_corrected    : mean |bias| = 0.1555\n  stratified_mle      : mean |bias| = 0.1677\n  hb_ec_hte           : mean |bias| = 0.1769\n\n\n=== FULL RUN K=4 ===\n\n============================================================\nBudget Sweep: Gemma K=4\nSubgroups: ['False_medium', 'False_short', 'True_medium', 'True_short']\nWeights: {'False_medium': np.float64(0.382), 'False_short': np.float64(0.222), 'True_medium': np.float64(0.255), 'True_short': np.float64(0.141)}\nP(Z=1) = 0.652\ntau(z=0) = 0.35, tau(z=1) = 0.65\n============================================================\n\nFull run: 5 budgets x 50 seeds\n\n--- n_expert = 100 ---\n  [10/50] 0s elapsed, ETA 3s\n  [20/50] 0s elapsed, ETA 3s\n  [30/50] 0s elapsed, ETA 3s\n  [40/50] 0s elapsed, ETA 3s\n  [50/50] 1s elapsed, ETA 2s\n  n_expert=100 done in 0.6s\n\n--- n_expert = 200 ---\n  [10/50] 1s elapsed, ETA 2s\n  [20/50] 1s elapsed, ETA 2s\n  [30/50] 1s elapsed, ETA 2s\n  [40/50] 1s elapsed, ETA 2s\n  [50/50] 1s elapsed, ETA 2s\n  n_expert=200 done in 0.7s\n\n--- n_expert = 500 ---\n  [10/50] 1s elapsed, ETA 2s\n  [20/50] 2s elapsed, ETA 2s\n  [30/50] 2s elapsed, ETA 2s\n  [40/50] 2s elapsed, ETA 1s\n  [50/50] 2s elapsed, ETA 1s\n  n_expert=500 done in 0.6s\n\n--- n_expert = 1000 ---\n  [10/50] 2s elapsed, ETA 1s\n  [20/50] 2s elapsed, ETA 1s\n  [30/50] 2s elapsed, ETA 1s\n  [40/50] 2s elapsed, ETA 1s\n  [50/50] 3s elapsed, ETA 1s\n  n_expert=1000 done in 0.7s\n\n--- n_expert = 2000 ---\n  [10/50] 3s elapsed, ETA 1s\n  [20/50] 3s elapsed, ETA 0s\n  [30/50] 3s elapsed, ETA 0s\n  [40/50] 3s elapsed, ETA 0s\n  [50/50] 3s elapsed, ETA 0s\n  n_expert=2000 done in 0.7s\n\nTotal time: 3.3s\nSaved artifacts/c1_multi_llm/gemma_budget_sweep_k4.csv (8000 rows)\n\n\n=== FULL RUN K=2 ===\n\n============================================================\nBudget Sweep: Gemma K=2\nSubgroups: ['False', 'True']\nWeights: {'False': np.float64(0.604), 'True': np.float64(0.396)}\nP(Z=1) = 0.652\ntau(z=0) = 0.35, tau(z=1) = 0.65\n============================================================\n\nFull run: 5 budgets x 50 seeds\n\n--- n_expert = 100 ---\n  [10/50] 0s elapsed, ETA 2s\n  [20/50] 0s elapsed, ETA 2s\n  [30/50] 0s elapsed, ETA 2s\n  [40/50] 0s elapsed, ETA 2s\n  [50/50] 0s elapsed, ETA 2s\n  n_expert=100 done in 0.4s\n\n--- n_expert = 200 ---\n  [10/50] 1s elapsed, ETA 2s\n  [20/50] 1s elapsed, ETA 2s\n  [30/50] 1s elapsed, ETA 1s\n  [40/50] 1s elapsed, ETA 1s\n  [50/50] 1s elapsed, ETA 1s\n  n_expert=200 done in 0.4s\n\n--- n_expert = 500 ---\n  [10/50] 1s elapsed, ETA 1s\n  [20/50] 1s elapsed, ETA 1s\n  [30/50] 1s elapsed, ETA 1s\n  [40/50] 1s elapsed, ETA 1s\n  [50/50] 1s elapsed, ETA 1s\n  n_expert=500 done in 0.4s\n\n--- n_expert = 1000 ---\n  [10/50] 1s elapsed, ETA 1s\n  [20/50] 1s elapsed, ETA 1s\n  [30/50] 2s elapsed, ETA 1s\n  [40/50] 2s elapsed, ETA 1s\n  [50/50] 2s elapsed, ETA 0s\n  n_expert=1000 done in 0.4s\n\n--- n_expert = 2000 ---\n  [10/50] 2s elapsed, ETA 0s\n  [20/50] 2s elapsed, ETA 0s\n  [30/50] 2s elapsed, ETA 0s\n  [40/50] 2s elapsed, ETA 0s\n  [50/50] 2s elapsed, ETA 0s\n  n_expert=2000 done in 0.4s\n\nTotal time: 2.2s\nSaved artifacts/c1_multi_llm/gemma_budget_sweep_k2.csv (4000 rows)\nWrote artifacts/c1_multi_llm/gemma_sweep_analysis.md\n\n\n=== FINAL SUMMARY ===\n\nK=4:\n  n_expert=100:\n    naive               : |Bias|=0.0711  RMSE=0.1192  Cov=0.775  CIW=0.3312\n    global_corrected    : |Bias|=0.0202  RMSE=0.1950  Cov=0.860  CIW=0.5382\n    stratified_mle      : |Bias|=0.1066  RMSE=0.6609  Cov=0.675  CIW=0.7715\n    hb_ec_hte           : |Bias|=0.2106  RMSE=1.2291  Cov=0.690  CIW=0.8005\n  n_expert=200:\n    naive               : |Bias|=0.0711  RMSE=0.1192  Cov=0.775  CIW=0.3312\n    global_corrected    : |Bias|=0.0223  RMSE=0.1682  Cov=0.887  CIW=0.5211\n    stratified_mle      : |Bias|=0.0646  RMSE=0.3844  Cov=0.782  CIW=0.5890\n    hb_ec_hte           : |Bias|=0.0676  RMSE=0.4212  Cov=0.790  CIW=0.5810\n  n_expert=500:\n    naive               : |Bias|=0.0711  RMSE=0.1192  Cov=0.775  CIW=0.3312\n    global_corrected    : |Bias|=0.0172  RMSE=0.1480  Cov=0.907  CIW=0.5125\n    stratified_mle      : |Bias|=0.0244  RMSE=0.1844  Cov=0.873  CIW=0.5197\n    hb_ec_hte           : |Bias|=0.0233  RMSE=0.1824  Cov=0.873  CIW=0.5160\n  n_expert=1000:\n    naive               : |Bias|=0.0711  RMSE=0.1192  Cov=0.775  CIW=0.3312\n    global_corrected    : |Bias|=0.0157  RMSE=0.1428  Cov=0.922  CIW=0.5106\n    stratified_mle      : |Bias|=0.0180  RMSE=0.1549  Cov=0.900  CIW=0.5041\n    hb_ec_hte           : |Bias|=0.0175  RMSE=0.1541  Cov=0.907  CIW=0.5025\n  n_expert=2000:\n    naive               : |Bias|=0.0711  RMSE=0.1192  Cov=0.775  CIW=0.3312\n    global_corrected    : |Bias|=0.0160  RMSE=0.1377  Cov=0.920  CIW=0.5068\n    stratified_mle      : |Bias|=0.0161  RMSE=0.1394  Cov=0.917  CIW=0.4947\n    hb_ec_hte           : |Bias|=0.0156  RMSE=0.1390  Cov=0.917  CIW=0.4940\n\nK=2:\n  n_expert=100:\n    naive               : |Bias|=0.0715  RMSE=0.0955  Cov=0.705  CIW=0.2268\n    global_corrected    : |Bias|=0.0154  RMSE=0.1376  Cov=0.820  CIW=0.3585\n    stratified_mle      : |Bias|=0.0250  RMSE=0.1895  Cov=0.740  CIW=0.3758\n    hb_ec_hte           : |Bias|=0.0269  RMSE=0.1870  Cov=0.745  CIW=0.3694\n  n_expert=200:\n    naive               : |Bias|=0.0715  RMSE=0.0955  Cov=0.705  CIW=0.2268\n    global_corrected    : |Bias|=0.0095  RMSE=0.1182  Cov=0.875  CIW=0.3475\n    stratified_mle      : |Bias|=0.0112  RMSE=0.1412  Cov=0.775  CIW=0.3514\n    hb_ec_hte           : |Bias|=0.0095  RMSE=0.1404  Cov=0.780  CIW=0.3489\n  n_expert=500:\n    naive               : |Bias|=0.0715  RMSE=0.0955  Cov=0.705  CIW=0.2268\n    global_corrected    : |Bias|=0.0104  RMSE=0.1000  Cov=0.905  CIW=0.3436\n    stratified_mle      : |Bias|=0.0130  RMSE=0.1111  Cov=0.875  CIW=0.3406\n    hb_ec_hte           : |Bias|=0.0105  RMSE=0.1105  Cov=0.880  CIW=0.3397\n  n_expert=1000:\n    naive               : |Bias|=0.0715  RMSE=0.0955  Cov=0.705  CIW=0.2268\n    global_corrected    : |Bias|=0.0100  RMSE=0.0889  Cov=0.945  CIW=0.3442\n    stratified_mle      : |Bias|=0.0125  RMSE=0.0895  Cov=0.945  CIW=0.3394\n    hb_ec_hte           : |Bias|=0.0122  RMSE=0.0892  Cov=0.945  CIW=0.3389\n  n_expert=2000:\n    naive               : |Bias|=0.0715  RMSE=0.0955  Cov=0.705  CIW=0.2268\n    global_corrected    : |Bias|=0.0102  RMSE=0.0854  Cov=0.950  CIW=0.3416\n    stratified_mle      : |Bias|=0.0177  RMSE=0.0860  Cov=0.925  CIW=0.3361\n    hb_ec_hte           : |Bias|=0.0176  RMSE=0.0859  Cov=0.925  CIW=0.3359",
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

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
All outputs generated successfully. Let me verify the output files exist and check the content of the profile and analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "389cc925-1479-4f2d-a7e2-e403e906ed45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWPNYaLgGBYNBhZu1BEymr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4351,
      "cache_read_input_tokens": 40606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4351
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

_source line 21_

All 4 outputs generated. Let me verify the files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "b263fd9c-63b0-4f27-aed4-99e22a0ff456",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWPNYaLgGBYNBhZu1BEymr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4351,
      "cache_read_input_tokens": 40606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4351
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

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01SAk1bhkYKVJ3f76HGv4okD`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/gemma_cm_profile.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "b58f960f-ca0a-45b3-a7ba-6b6b7cad350b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWPNYaLgGBYNBhZu1BEymr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4351,
      "cache_read_input_tokens": 40606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4351
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

_source line 23 · 2026-05-21T22:13:25.030Z_

<details><summary>↩ Tool result · `toolu_01SAk1bhkYKVJ3f76HGv4okD`</summary>

```text
1	# Gemma-2-9B Confusion Matrix Profile
2	
3	## Global Statistics
4	
5	- N = 500
6	- Accuracy = 0.764
7	- P(Z=1) = 0.652
8	- Global FPR = 0.098
9	- Global FNR = 0.310
10	- Delta_pi = |FPR - FNR| = 0.212
11	- FNR > FPR asymmetry: YES
12	
13	## K=4 Subgroups (has_hashtag x text_length_bin, excl. long)
14	
15	- Sample size (excl. long): 490
16	
17	| Subgroup | n | Weight | pi_s | FPR | FNR | kappa |
18	|----------|---|--------|------|-----|-----|-------|
19	| False_medium | 187 | 0.382 | 0.465 | 0.110 | 0.437 | 2.21 |
20	| False_short | 109 | 0.222 | 0.734 | 0.138 | 0.300 | 1.78 |
21	| True_medium | 125 | 0.255 | 0.760 | 0.033 | 0.263 | 1.42 |
22	| True_short | 69 | 0.141 | 0.841 | 0.091 | 0.207 | 1.42 |
23	
24	- Max kappa = 2.21
25	- Prop2 triggered (kappa > 2): 1/4
26	
27	## K=2 Subgroups (has_hashtag only)
28	
29	| Subgroup | n | Weight | pi_s | FPR | FNR | kappa |
30	|----------|---|--------|------|-----|-----|-------|
31	| False | 302 | 0.604 | 0.566 | 0.115 | 0.368 | 1.93 |
32	| True | 198 | 0.396 | 0.783 | 0.047 | 0.245 | 1.41 |
33	
34	- Max kappa = 1.93
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "6921988e-ae2d-4933-aa90-835568d334be",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/gemma_cm_profile.md",
      "content": "# Gemma-2-9B Confusion Matrix Profile\n\n## Global Statistics\n\n- N = 500\n- Accuracy = 0.764\n- P(Z=1) = 0.652\n- Global FPR = 0.098\n- Global FNR = 0.310\n- Delta_pi = |FPR - FNR| = 0.212\n- FNR > FPR asymmetry: YES\n\n## K=4 Subgroups (has_hashtag x text_length_bin, excl. long)\n\n- Sample size (excl. long): 490\n\n| Subgroup | n | Weight | pi_s | FPR | FNR | kappa |\n|----------|---|--------|------|-----|-----|-------|\n| False_medium | 187 | 0.382 | 0.465 | 0.110 | 0.437 | 2.21 |\n| False_short | 109 | 0.222 | 0.734 | 0.138 | 0.300 | 1.78 |\n| True_medium | 125 | 0.255 | 0.760 | 0.033 | 0.263 | 1.42 |\n| True_short | 69 | 0.141 | 0.841 | 0.091 | 0.207 | 1.42 |\n\n- Max kappa = 2.21\n- Prop2 triggered (kappa > 2): 1/4\n\n## K=2 Subgroups (has_hashtag only)\n\n| Subgroup | n | Weight | pi_s | FPR | FNR | kappa |\n|----------|---|--------|------|-----|-----|-------|\n| False | 302 | 0.604 | 0.566 | 0.115 | 0.368 | 1.93 |\n| True | 198 | 0.396 | 0.783 | 0.047 | 0.245 | 1.41 |\n\n- Max kappa = 1.93\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01VU3a8sGrw37p4DUah6YSUp`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/gemma_sweep_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "948b076d-51be-4c61-b48a-b79416372c1a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VWPNYaLgGBYNBhZu1BEymr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4351,
      "cache_read_input_tokens": 40606,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4351
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

_source line 25 · 2026-05-21T22:13:25.331Z_

<details><summary>↩ Tool result · `toolu_01VU3a8sGrw37p4DUah6YSUp`</summary>

```text
1	# Gemma-2-9B Budget Sweep Analysis
2	
3	## Design
4	
5	- N=5000, P(Z=1)=0.652
6	- tau(z=0)=0.35, tau(z=1)=0.65, delta_tau=0.3
7	- n_expert sweep: [100, 200, 500, 1000, 2000]
8	- 50 MC seeds per budget
9	- HB method: MAP-EB (Gamma(3,1) prior)
10	- |Bias| = avg across cells of |mean(bias) across seeds|
11	- RMSE = avg across cells of sqrt(mean(bias^2) across seeds)
12	- Coverage = avg across cells of fraction(95% CI contains true CATE)
13	- CI Width = avg across cells of mean(CI_width)
14	
15	## K=4 Summary Table
16	
17	| n_expert | |Bias|_naive | |Bias|_global | |Bias|_strat | |Bias|_echte | RMSE_naive | RMSE_global | RMSE_strat | RMSE_echte | Cov_naive | Cov_echte | CIW_naive | CIW_echte | HB_wins_bias? | HB_wins_rmse? |
18	|----------|-------------|--------------|-------------|-------------|------------|-------------|------------|------------|-----------|-----------|-----------|-----------|---------------|---------------|
19	| 100 | 0.0711 | 0.0202 | 0.1066 | 0.2106 | 0.1192 | 0.1950 | 0.6609 | 1.2291 | 0.775 | 0.690 | 0.3312 | 0.8005 | no | no |
20	| 200 | 0.0711 | 0.0223 | 0.0646 | 0.0676 | 0.1192 | 0.1682 | 0.3844 | 0.4212 | 0.775 | 0.790 | 0.3312 | 0.5810 | YES | no |
21	| 500 | 0.0711 | 0.0172 | 0.0244 | 0.0233 | 0.1192 | 0.1480 | 0.1844 | 0.1824 | 0.775 | 0.873 | 0.3312 | 0.5160 | YES | no |
22	| 1000 | 0.0711 | 0.0157 | 0.0180 | 0.0175 | 0.1192 | 0.1428 | 0.1549 | 0.1541 | 0.775 | 0.907 | 0.3312 | 0.5025 | YES | no |
23	| 2000 | 0.0711 | 0.0160 | 0.0161 | 0.0156 | 0.1192 | 0.1377 | 0.1394 | 0.1390 | 0.775 | 0.917 | 0.3312 | 0.4940 | YES | no |
24	
25	### K=4 Crossover Analysis
26	
27	- **|Bias| crossover**: EC-HTE beats Naive at n_expert=200
28	- **RMSE crossover**: EC-HTE never beats Naive in tested range
29	
30	### K=4 Bias-Variance Decomposition
31	
32	| n_expert | Method | Bias^2 | Variance | MSE |
33	|----------|--------|--------|----------|-----|
34	| 100 | naive | 0.0076 | 0.0079 | 0.0155 |
35	| 100 | hb_ec_hte | 0.1217 | 5.2627 | 5.3844 |
36	| 200 | naive | 0.0076 | 0.0079 | 0.0155 |
37	| 200 | hb_ec_hte | 0.0095 | 0.3843 | 0.3938 |
38	| 500 | naive | 0.0076 | 0.0079 | 0.0155 |
39	| 500 | hb_ec_hte | 0.0007 | 0.0376 | 0.0383 |
40	| 1000 | naive | 0.0076 | 0.0079 | 0.0155 |
41	| 1000 | hb_ec_hte | 0.0004 | 0.0259 | 0.0263 |
42	| 2000 | naive | 0.0076 | 0.0079 | 0.0155 |
43	| 2000 | hb_ec_hte | 0.0004 | 0.0211 | 0.0215 |
44	
45	## K=2 Summary Table
46	
47	| n_expert | |Bias|_naive | |Bias|_global | |Bias|_strat | |Bias|_echte | RMSE_naive | RMSE_global | RMSE_strat | RMSE_echte | Cov_naive | Cov_echte | CIW_naive | CIW_echte | HB_wins_bias? | HB_wins_rmse? |
48	|----------|-------------|--------------|-------------|-------------|------------|-------------|------------|------------|-----------|-----------|-----------|-----------|---------------|---------------|
49	| 100 | 0.0715 | 0.0154 | 0.0250 | 0.0269 | 0.0955 | 0.1376 | 0.1895 | 0.1870 | 0.705 | 0.745 | 0.2268 | 0.3694 | YES | no |
50	| 200 | 0.0715 | 0.0095 | 0.0112 | 0.0095 | 0.0955 | 0.1182 | 0.1412 | 0.1404 | 0.705 | 0.780 | 0.2268 | 0.3489 | YES | no |
51	| 500 | 0.0715 | 0.0104 | 0.0130 | 0.0105 | 0.0955 | 0.1000 | 0.1111 | 0.1105 | 0.705 | 0.880 | 0.2268 | 0.3397 | YES | no |
52	| 1000 | 0.0715 | 0.0100 | 0.0125 | 0.0122 | 0.0955 | 0.0889 | 0.0895 | 0.0892 | 0.705 | 0.945 | 0.2268 | 0.3389 | YES | YES |
53	| 2000 | 0.0715 | 0.0102 | 0.0177 | 0.0176 | 0.0955 | 0.0854 | 0.0860 | 0.0859 | 0.705 | 0.925 | 0.2268 | 0.3359 | YES | YES |
54	
55	### K=2 Crossover Analysis
56	
57	- **|Bias| crossover**: EC-HTE beats Naive at n_expert=100
58	- **RMSE crossover**: EC-HTE beats Naive at n_expert=1000
59	
60	### K=2 Bias-Variance Decomposition
61	
62	| n_expert | Method | Bias^2 | Variance | MSE |
63	|----------|--------|--------|----------|-----|
64	| 100 | naive | 0.0077 | 0.0030 | 0.0106 |
65	| 100 | hb_ec_hte | 0.0008 | 0.0373 | 0.0381 |
66	| 200 | naive | 0.0077 | 0.0030 | 0.0106 |
67	| 200 | hb_ec_hte | 0.0001 | 0.0214 | 0.0215 |
68	| 500 | naive | 0.0077 | 0.0030 | 0.0106 |
69	| 500 | hb_ec_hte | 0.0003 | 0.0134 | 0.0137 |
70	| 1000 | naive | 0.0077 | 0.0030 | 0.0106 |
71	| 1000 | hb_ec_hte | 0.0002 | 0.0085 | 0.0087 |
72	| 2000 | naive | 0.0077 | 0.0030 | 0.0106 |
73	| 2000 | hb_ec_hte | 0.0004 | 0.0076 | 0.0080 |
74	
75	## K=4 vs K=2 Comparison
76	
77	| n_expert | |Bias|_echte_K4 | |Bias|_echte_K2 | RMSE_echte_K4 | RMSE_echte_K2 | Cov_echte_K4 | Cov_echte_K2 |
78	|----------|----------------|----------------|---------------|---------------|--------------|--------------|
79	| 100 | 0.2106 | 0.0269 | 1.2291 | 0.1870 | 0.690 | 0.745 |
80	| 200 | 0.0676 | 0.0095 | 0.4212 | 0.1404 | 0.790 | 0.780 |
81	| 500 | 0.0233 | 0.0105 | 0.1824 | 0.1105 | 0.873 | 0.880 |
82	| 1000 | 0.0175 | 0.0122 | 0.1541 | 0.0892 | 0.907 | 0.945 |
83	| 2000 | 0.0156 | 0.0176 | 0.1390 | 0.0859 | 0.917 | 0.925 |
84	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "d999a075-4c7a-41cd-9b9d-5bbc6406a1a3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/gemma_sweep_analysis.md",
      "content": "# Gemma-2-9B Budget Sweep Analysis\n\n## Design\n\n- N=5000, P(Z=1)=0.652\n- tau(z=0)=0.35, tau(z=1)=0.65, delta_tau=0.3\n- n_expert sweep: [100, 200, 500, 1000, 2000]\n- 50 MC seeds per budget\n- HB method: MAP-EB (Gamma(3,1) prior)\n- |Bias| = avg across cells of |mean(bias) across seeds|\n- RMSE = avg across cells of sqrt(mean(bias^2) across seeds)\n- Coverage = avg across cells of fraction(95% CI contains true CATE)\n- CI Width = avg across cells of mean(CI_width)\n\n## K=4 Summary Table\n\n| n_expert | |Bias|_naive | |Bias|_global | |Bias|_strat | |Bias|_echte | RMSE_naive | RMSE_global | RMSE_strat | RMSE_echte | Cov_naive | Cov_echte | CIW_naive | CIW_echte | HB_wins_bias? | HB_wins_rmse? |\n|----------|-------------|--------------|-------------|-------------|------------|-------------|------------|------------|-----------|-----------|-----------|-----------|---------------|---------------|\n| 100 | 0.0711 | 0.0202 | 0.1066 | 0.2106 | 0.1192 | 0.1950 | 0.6609 | 1.2291 | 0.775 | 0.690 | 0.3312 | 0.8005 | no | no |\n| 200 | 0.0711 | 0.0223 | 0.0646 | 0.0676 | 0.1192 | 0.1682 | 0.3844 | 0.4212 | 0.775 | 0.790 | 0.3312 | 0.5810 | YES | no |\n| 500 | 0.0711 | 0.0172 | 0.0244 | 0.0233 | 0.1192 | 0.1480 | 0.1844 | 0.1824 | 0.775 | 0.873 | 0.3312 | 0.5160 | YES | no |\n| 1000 | 0.0711 | 0.0157 | 0.0180 | 0.0175 | 0.1192 | 0.1428 | 0.1549 | 0.1541 | 0.775 | 0.907 | 0.3312 | 0.5025 | YES | no |\n| 2000 | 0.0711 | 0.0160 | 0.0161 | 0.0156 | 0.1192 | 0.1377 | 0.1394 | 0.1390 | 0.775 | 0.917 | 0.3312 | 0.4940 | YES | no |\n\n### K=4 Crossover Analysis\n\n- **|Bias| crossover**: EC-HTE beats Naive at n_expert=200\n- **RMSE crossover**: EC-HTE never beats Naive in tested range\n\n### K=4 Bias-Variance Decomposition\n\n| n_expert | Method | Bias^2 | Variance | MSE |\n|----------|--------|--------|----------|-----|\n| 100 | naive | 0.0076 | 0.0079 | 0.0155 |\n| 100 | hb_ec_hte | 0.1217 | 5.2627 | 5.3844 |\n| 200 | naive | 0.0076 | 0.0079 | 0.0155 |\n| 200 | hb_ec_hte | 0.0095 | 0.3843 | 0.3938 |\n| 500 | naive | 0.0076 | 0.0079 | 0.0155 |\n| 500 | hb_ec_hte | 0.0007 | 0.0376 | 0.0383 |\n| 1000 | naive | 0.0076 | 0.0079 | 0.0155 |\n| 1000 | hb_ec_hte | 0.0004 | 0.0259 | 0.0263 |\n| 2000 | naive | 0.0076 | 0.0079 | 0.0155 |\n| 2000 | hb_ec_hte | 0.0004 | 0.0211 | 0.0215 |\n\n## K=2 Summary Table\n\n| n_expert | |Bias|_naive | |Bias|_global | |Bias|_strat | |Bias|_echte | RMSE_naive | RMSE_global | RMSE_strat | RMSE_echte | Cov_naive | Cov_echte | CIW_naive | CIW_echte | HB_wins_bias? | HB_wins_rmse? |\n|----------|-------------|--------------|-------------|-------------|------------|-------------|------------|------------|-----------|-----------|-----------|-----------|---------------|---------------|\n| 100 | 0.0715 | 0.0154 | 0.0250 | 0.0269 | 0.0955 | 0.1376 | 0.1895 | 0.1870 | 0.705 | 0.745 | 0.2268 | 0.3694 | YES | no |\n| 200 | 0.0715 | 0.0095 | 0.0112 | 0.0095 | 0.0955 | 0.1182 | 0.1412 | 0.1404 | 0.705 | 0.780 | 0.2268 | 0.3489 | YES | no |\n| 500 | 0.0715 | 0.0104 | 0.0130 | 0.0105 | 0.0955 | 0.1000 | 0.1111 | 0.1105 | 0.705 | 0.880 | 0.2268 | 0.3397 | YES | no |\n| 1000 | 0.0715 | 0.0100 | 0.0125 | 0.0122 | 0.0955 | 0.0889 | 0.0895 | 0.0892 | 0.705 | 0.945 | 0.2268 | 0.3389 | YES | YES |\n| 2000 | 0.0715 | 0.0102 | 0.0177 | 0.0176 | 0.0955 | 0.0854 | 0.0860 | 0.0859 | 0.705 | 0.925 | 0.2268 | 0.3359 | YES | YES |\n\n### K=2 Crossover Analysis\n\n- **|Bias| crossover**: EC-HTE beats Naive at n_expert=100\n- **RMSE crossover**: EC-HTE beats Naive at n_expert=1000\n\n### K=2 Bias-Variance Decomposition\n\n| n_expert | Method | Bias^2 | Variance | MSE |\n|----------|--------|--------|----------|-----|\n| 100 | naive | 0.0077 | 0.0030 | 0.0106 |\n| 100 | hb_ec_hte | 0.0008 | 0.0373 | 0.0381 |\n| 200 | naive | 0.0077 | 0.0030 | 0.0106 |\n| 200 | hb_ec_hte | 0.0001 | 0.0214 | 0.0215 |\n| 500 | naive | 0.0077 | 0.0030 | 0.0106 |\n| 500 | hb_ec_hte | 0.0003 | 0.0134 | 0.0137 |\n| 1000 | naive | 0.0077 | 0.0030 | 0.0106 |\n| 1000 | hb_ec_hte | 0.0002 | 0.0085 | 0.0087 |\n| 2000 | naive | 0.0077 | 0.0030 | 0.0106 |\n| 2000 | hb_ec_hte | 0.0004 | 0.0076 | 0.0080 |\n\n## K=4 vs K=2 Comparison\n\n| n_expert | |Bias|_echte_K4 | |Bias|_echte_K2 | RMSE_echte_K4 | RMSE_echte_K2 | Cov_echte_K4 | Cov_echte_K2 |\n|----------|----------------|----------------|---------------|---------------|--------------|--------------|\n| 100 | 0.2106 | 0.0269 | 1.2291 | 0.1870 | 0.690 | 0.745 |\n| 200 | 0.0676 | 0.0095 | 0.4212 | 0.1404 | 0.790 | 0.780 |\n| 500 | 0.0233 | 0.0105 | 0.1824 | 0.1105 | 0.873 | 0.880 |\n| 1000 | 0.0175 | 0.0122 | 0.1541 | 0.0892 | 0.907 | 0.945 |\n| 2000 | 0.0156 | 0.0176 | 0.1390 | 0.0859 | 0.917 | 0.925 |\n",
      "numLines": 84,
      "startLine": 1,
      "totalLines": 84
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

All 4 outputs generated successfully:

| File | Status |
|------|--------|
| `gemma_cm_profile.md` | Gemma Accuracy=0.764, FPR=0.098, FNR=0.310, Δπ=0.212, strong FNR>FPR asymmetry confirmed |
| `gemma_budget_sweep_k4.csv` | 8000 rows (5 budgets × 50 seeds × 4 subgroups × 2 z-levels × 4 methods) |
| `gemma_budget_sweep_k2.csv` | 4000 rows (5 budgets × 50 seeds × 2 subgroups × 2 z-levels × 4 methods) |
| `gemma_sweep_analysis.md` | Full analysis with summary tables, crossover, bias-variance decomposition, K4 vs K2 comparison |

Key findings:

**CM Profile:** Max κ=2.21 (K=4), only 1/4 subgroups with κ>2 (vs. task's claimed 4/4 — the "known" Gemma stats appear to be from a different binarization or dataset version). The `False_medium` subgroup has the worst FNR (0.437).

**K=4:** |Bias| crossover at n_expert=200, RMSE crossover never reached (variance cost of 4-way stratification is high at small budgets — K=4 with only 490 eligible observations means thin cells).

**K=2:** |Bias| crossover at n_expert=100, RMSE crossover at n_expert=1000. K=2 dominates K=4 across all budgets — fewer subgroups = less variance, and Gemma's CM heterogeneity between hashtag groups is substantial enough that K=2 still captures the important variation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "uuid": "3b5d99b3-8e26-41ca-aa32-482389cbb856",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P7kLNFi7D3cxLUY2ui2vvu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3730,
      "cache_read_input_tokens": 44957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3730
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

_source line 27_

All 4 outputs generated successfully:

| File | Status |
|------|--------|
| `gemma_cm_profile.md` | Gemma Accuracy=0.764, FPR=0.098, FNR=0.310, Δπ=0.212, strong FNR>FPR asymmetry confirmed |
| `gemma_budget_sweep_k4.csv` | 8000 rows (5 budgets × 50 seeds × 4 subgroups × 2 z-levels × 4 methods) |
| `gemma_budget_sweep_k2.csv` | 4000 rows (5 budgets × 50 seeds × 2 subgroups × 2 z-levels × 4 methods) |
| `gemma_sweep_analysis.md` | Full analysis with summary tables, crossover, bias-variance decomposition, K4 vs K2 comparison |

Key findings:

**CM Profile:** Max κ=2.21 (K=4), only 1/4 subgroups with κ>2 (vs. task's claimed 4/4 — the "known" Gemma stats appear to be from a different binarization or dataset version). The `False_medium` subgroup has the worst FNR (0.437).

**K=4:** |Bias| crossover at n_expert=200, RMSE crossover never reached (variance cost of 4-way stratification is high at small budgets — K=4 with only 490 eligible observations means thin cells).

**K=2:** |Bias| crossover at n_expert=100, RMSE crossover at n_expert=1000. K=2 dominates K=4 across all budgets — fewer subgroups = less variance, and Gemma's CM heterogeneity between hashtag groups is substantial enough that K=2 still captures the important variation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 178077,
  "duration_api_ms": 172009,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "2ba7b734-886f-4261-af01-25a6426193cc",
  "total_cost_usd": 0.6492929999999999,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 36846,
    "cache_read_input_tokens": 184527,
    "output_tokens": 13006,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 36846,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 455,
        "cache_read_input_tokens": 44957,
        "cache_creation_input_tokens": 3730,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3730
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1412,
      "outputTokens": 28,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001552,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 13006,
      "cacheReadInputTokens": 184527,
      "cacheCreationInputTokens": 36846,
      "webSearchRequests": 0,
      "costUSD": 0.6477409999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9e028d4b-a5fa-43ca-969c-1bee85f107df"
}
```

</details>

---
