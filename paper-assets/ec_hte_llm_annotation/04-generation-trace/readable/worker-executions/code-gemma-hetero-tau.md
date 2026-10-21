# code gemma hetero tau

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/workers/worker_code_gemma-hetero-tau_20260522T001443.log`
- **Structured JSON:** [`4ea2323ce951c6836cee.json`](../../sessions/4e/4ea2323ce951c6836cee.json)

## Before a recorded user message

9 recorded events

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
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
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
  "uuid": "1fe22206-335c-437c-a346-a22706f36a4b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-ec-hte-llm-annotation/memory/"
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
    "resetsAt": 1779417000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "fbd2eb79-f4fc-4aac-9650-1fbdd1319c4a",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0"
}
```

---

### Assistant

_source line 4_

I'll start by reading the template script to understand the structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "896be33f-38c4-4f51-9b0d-bdeba1207c32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVuodn9YcUtautKDR9DzW5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6556,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6556
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

<details open><summary>🔧 Tool call — Read · `toolu_016rn9V9kRNyWPvwVCsLEsgv`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_qwen_hetero_tau.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "0b1ea74d-33c2-4fe4-8472-04bcc1be28e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVuodn9YcUtautKDR9DzW5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6556,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6556
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

_source line 6 · 2026-05-22T00:14:55.290Z_

<details><summary>↩ Tool result · `toolu_016rn9V9kRNyWPvwVCsLEsgv`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Heterogeneous-τ DGP experiment with Qwen2.5-7B confusion matrices.
4	Mirrors run_hetero_tau.py (Llama) but uses Qwen per-subgroup FPR/FNR.
5	"""
6	
7	import time
8	import warnings
9	import numpy as np
10	import pandas as pd
11	from scipy.optimize import minimize_scalar
12	from scipy.special import gammaln
13	
14	warnings.filterwarnings('ignore')
15	
16	# === Config ===
17	
18	N = 5000
19	N_EXPERT_LIST = [200, 500, 1000]
20	N_MC = 50
21	SEED_BASE = 0
22	
23	SUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']
24	SUBGROUP_WEIGHTS = np.array([0.3816, 0.2224, 0.2551, 0.1408])
25	SUBGROUP_WEIGHTS = SUBGROUP_WEIGHTS / SUBGROUP_WEIGHTS.sum()
26	
27	SUBGROUP_CM = {
28	    'False_medium': {'fpr': 0.1800, 'fnr': 0.2874},
29	    'False_short':  {'fpr': 0.2414, 'fnr': 0.1750},
30	    'True_medium':  {'fpr': 0.2333, 'fnr': 0.2105},
31	    'True_short':   {'fpr': 0.0000, 'fnr': 0.1379},
32	}
33	
34	SUBGROUP_TAU = {
35	    'True_short':   {'tau_z0': 0.2,  'tau_z1': 0.8},
36	    'True_medium':  {'tau_z0': 0.35, 'tau_z1': 0.65},
37	    'False_short':  {'tau_z0': 0.4,  'tau_z1': 0.5},
38	    'False_medium': {'tau_z0': 0.45, 'tau_z1': 0.55},
39	}
40	
41	P_Z1 = 0.652
42	P_T1 = 0.5
43	
44	
45	def get_cm_matrix(fpr, fnr):
46	    return np.array([[1 - fpr, fpr],
47	                     [fnr, 1 - fnr]])
48	
49	
50	# === Estimators ===
51	
52	def diff_in_means(Y, T, mask):
53	    t1 = mask & (T == 1)
54	    t0 = mask & (T == 0)
55	    n1, n0 = t1.sum(), t0.sum()
56	    if n1 < 2 or n0 < 2:
57	        return np.nan, np.nan
58	    y1, y0 = Y[t1], Y[t0]
59	    tau_hat = y1.mean() - y0.mean()
60	    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
61	    return tau_hat, se
62	
63	
64	def estimate_confusion_matrix(z_true, z_hat):
65	    C = np.zeros((2, 2))
66	    for zt in [0, 1]:
67	        mask = z_true == zt
68	        n = mask.sum()
69	        for zh in [0, 1]:
70	            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
71	    return C
72	
73	
74	def estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):
75	    C = {}
76	    for s in labels:
77	        ms = subgroups == s
78	        C_s = np.zeros((2, 2))
79	        for zt in [0, 1]:
80	            mask = ms & (z_true == zt)
81	            n = mask.sum()
82	            for zh in [0, 1]:
83	                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
84	        C[s] = C_s
85	    return C
86	
87	
88	def build_mixing_matrix(C, p_z, p_z_hat):
89	    M = np.zeros((2, 2))
90	    for zh in [0, 1]:
91	        for z in [0, 1]:
92	            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5
93	    return M
94	
95	
96	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
97	    cond = np.linalg.cond(M)
98	    if cond > cond_threshold:
99	        return tau_obs.copy(), se_obs.copy()
100	    det = np.linalg.det(M)
101	    if abs(det) < 1e-10:
102	        return tau_obs.copy(), se_obs.copy()
103	    Mi = np.linalg.inv(M)
104	    tau_c = Mi @ tau_obs
105	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
106	    return tau_c, se_c
107	
108	
109	# === MAP-EB ===
110	
111	def _dirmult_neg_ll(alpha, counts_z):
112	    a = alpha / 2.0
113	    if a < 1e-10:
114	        return 1e10
115	    ll = 0.0
116	    for c0, c1 in counts_z:
117	        n = c0 + c1
118	        if n == 0:
119	            continue
120	        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)
121	        ll -= 2 * gammaln(a) - gammaln(2 * a)
122	    return -ll
123	
124	
125	def estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):
126	    hp_rate = 1.0 / hp_scale
127	    k = len(labels)
128	    alpha_opt = np.zeros(2)
129	
130	    for z in [0, 1]:
131	        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]
132	        total = sum(c0 + c1 for c0, c1 in cl)
133	        if total == 0:
134	            alpha_opt[z] = hp_shape * hp_scale
135	            continue
136	
137	        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):
138	            nll = _dirmult_neg_ll(a, _cl)
139	            if a < 1e-10:
140	                return 1e10
141	            log_prior = (_shape - 1.0) * np.log(a) - _rate * a
142	            return nll - log_prior
143	
144	        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')
145	        alpha_opt[z] = res.x
146	
147	    C = {}
148	    for i, s in enumerate(labels):
149	        C_s = np.zeros((2, 2))
150	        for z in [0, 1]:
151	            a = alpha_opt[z] / 2.0
152	            n_sz = counts[i, z, :].sum()
153	            d = n_sz + 2 * a
154	            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5
155	            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5
156	        C[s] = C_s
157	
158	    return C, alpha_opt
159	
160	
161	def get_counts(z_true, z_hat, subgroups, labels):
162	    k = len(labels)
163	    counts = np.zeros((k, 2, 2), dtype=int)
164	    for i, s in enumerate(labels):
165	        ms = subgroups == s
166	        for z in [0, 1]:
167	            mz = ms & (z_true == z)
168	            counts[i, z, 0] = (z_hat[mz] == 0).sum()
169	            counts[i, z, 1] = (z_hat[mz] == 1).sum()
170	    return counts
171	
172	
173	# === DGP (heterogeneous tau) ===
174	
175	def generate_data(seed, n_expert):
176	    rng = np.random.RandomState(seed)
177	
178	    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)
179	    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])
180	
181	    Z = rng.binomial(1, P_Z1, N)
182	    T = rng.binomial(1, P_T1, N)
183	
184	    Z_hat = np.empty(N, dtype=int)
185	    for i in range(4):
186	        s_mask = S_idx == i
187	        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],
188	                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])
189	        z_s = Z[s_mask]
190	        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])
191	        Z_hat[s_mask] = rng.binomial(1, p_obs1)
192	
193	    tau_vals = np.zeros(N)
194	    for i, s in enumerate(SUBGROUP_LABELS):
195	        s_mask = S_idx == i
196	        tau_s = SUBGROUP_TAU[s]
197	        tau_vals[s_mask] = np.where(Z[s_mask] == 1, tau_s['tau_z1'], tau_s['tau_z0'])
198	
199	    eps = rng.randn(N)
200	    Y = 1.0 + tau_vals * T + eps
201	
202	    expert_idx = rng.choice(N, n_expert, replace=False)
203	    expert_mask = np.zeros(N, dtype=bool)
204	    expert_mask[expert_idx] = True
205	
206	    return {
207	        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,
208	        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,
209	    }
210	
211	
212	# === MC Runner ===
213	
214	def run_one_mc(data, seed):
215	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
216	    expert_mask = data['expert_mask']
217	
218	    z_exp = Z[expert_mask]
219	    zh_exp = Z_hat[expert_mask]
220	    s_exp = S[expert_mask]
221	
222	    C_global = estimate_confusion_matrix(z_exp, zh_exp)
223	    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])
224	    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])
225	    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)
226	
227	    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)
228	
229	    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)
230	    C_hb, _ = estimate_cm_hb_map_eb(counts, SUBGROUP_LABELS)
231	
232	    M_mle_sub = {}
233	    M_hb_sub = {}
234	    for s_val in SUBGROUP_LABELS:
235	        sm_exp = (s_exp == s_val)
236	        sm_all = (S == s_val)
237	        if sm_exp.sum() >= 4:
238	            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])
239	        else:
240	            p_z_s = p_z_global
241	        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])
242	        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)
243	        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)
244	
245	    rows = []
246	
247	    for s_val in SUBGROUP_LABELS:
248	        s_mask = S == s_val
249	        tau_s = SUBGROUP_TAU[s_val]
250	
251	        for z_level in [0, 1]:
252	            oracle_cate = tau_s['tau_z1'] if z_level == 1 else tau_s['tau_z0']
253	
254	            # Naive
255	            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))
256	            ci_w_nv = 2 * 1.96 * se_nv if not np.isnan(se_nv) else np.nan
257	            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan
258	            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan
259	            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0
260	            rows.append({
261	                'seed': seed, 'method': 'naive', 'subgroup': s_val,
262	                'z_level': z_level,
263	                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,
264	                'cate_est': th_nv, 'cate_true': oracle_cate,
265	                'coverage': cov_nv, 'ci_width': ci_w_nv,
266	            })
267	
268	            # Observed CATE in Z_hat=0 and Z_hat=1 cells
269	            tau_obs = np.array([
270	                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],
271	                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],
272	            ])
273	            se_obs = np.array([
274	                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],
275	                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],
276	            ])
277	
278	            if not np.any(np.isnan(tau_obs)):
279	                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)
280	                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]
281	
282	                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)
283	                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]
284	
285	                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)
286	                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]
287	            else:
288	                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan
289	
290	            # Global corrected
291	            ci_w_gc = 2 * 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan
292	            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan
293	            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan
294	            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0
295	            rows.append({
296	                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,
297	                'z_level': z_level,
298	                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,
299	                'cate_est': th_gc, 'cate_true': oracle_cate,
300	                'coverage': cov_gc, 'ci_width': ci_w_gc,
301	            })
302	
303	            # Stratified MLE
304	            ci_w_ml = 2 * 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan
305	            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan
306	            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan
307	            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0
308	            rows.append({
309	                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,
310	                'z_level': z_level,
311	                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,
312	                'cate_est': th_ml, 'cate_true': oracle_cate,
313	                'coverage': cov_ml, 'ci_width': ci_w_ml,
314	            })
315	
316	            # HB EC-HTE (MAP-EB)
317	            ci_w_hb = 2 * 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan
318	            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan
319	            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan
320	            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0
321	            rows.append({
322	                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,
323	                'z_level': z_level,
324	                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,
325	                'cate_est': th_hb, 'cate_true': oracle_cate,
326	                'coverage': cov_hb, 'ci_width': ci_w_hb,
327	            })
328	
329	    return rows
330	
331	
332	# === Aggregation ===
333	
334	def compute_corrected_abs_bias(df):
335	    cell_bias = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias']
336	                 .mean().abs().reset_index(name='abs_mean_bias'))
337	    return (cell_bias.groupby(['n_expert', 'method'])['abs_mean_bias']
338	            .mean().reset_index(name='abs_bias'))
339	
340	
341	def compute_rmse(df):
342	    cell_rmse = (df.assign(bias_sq=df['bias'] ** 2)
343	                 .groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias_sq']
344	                 .mean().apply(np.sqrt).reset_index(name='rmse'))
345	    return (cell_rmse.groupby(['n_expert', 'method'])['rmse']
346	            .mean().reset_index(name='rmse'))
347	
348	
349	def compute_coverage(df):
350	    return (df.groupby(['n_expert', 'method'])['coverage']
351	            .mean().reset_index(name='coverage'))
352	
353	
354	def compute_ci_width(df):
355	    return (df.groupby(['n_expert', 'method'])['ci_width']
356	            .mean().reset_index(name='ci_width'))
357	
358	
359	# === Analysis Report ===
360	
361	LLAMA_RESULTS = {
362	    200:  {'global_bias': 0.0365, 'echte_bias': 0.0248, 'global_rmse': 0.1780, 'echte_rmse': 0.2606},
363	    500:  {'global_bias': 0.0314, 'echte_bias': 0.0099, 'global_rmse': 0.1580, 'echte_rmse': 0.1760},
364	    1000: {'global_bias': 0.0286, 'echte_bias': 0.0130, 'global_rmse': 0.1554, 'echte_rmse': 0.1602},
365	}
366	
367	LLAMA_CM = {
368	    'False_medium': {'fpr': 0.235, 'fnr': 0.319},
369	    'False_short':  {'fpr': 0.310, 'fnr': 0.212},
370	    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},
371	    'True_short':   {'fpr': 0.091, 'fnr': 0.190},
372	}
373	
374	
375	def write_analysis(df_raw, outpath):
376	    abs_bias = compute_corrected_abs_bias(df_raw)
377	    rmse = compute_rmse(df_raw)
378	    cov = compute_coverage(df_raw)
379	    ciw = compute_ci_width(df_raw)
380	
381	    summary = abs_bias.merge(rmse, on=['n_expert', 'method']).merge(
382	        cov, on=['n_expert', 'method']).merge(ciw, on=['n_expert', 'method'])
383	
384	    lines = []
385	    lines.append("# Qwen2.5-7B Heterogeneous-τ DGP: EC-HTE vs Global Correction\n")
386	    lines.append("## Design\n")
387	    lines.append(f"- N={N}, P(Z=1)={P_Z1}, K=4 subgroups")
388	    lines.append("- **LLM**: Qwen2.5-7B (balanced binarization)")
389	    lines.append("- **Heterogeneous τ(z) across subgroups:**")
390	    for s in SUBGROUP_LABELS:
391	        t = SUBGROUP_TAU[s]
392	        lines.append(f"  - {s}: τ(z=0)={t['tau_z0']}, τ(z=1)={t['tau_z1']}, Δτ={t['tau_z1']-t['tau_z0']:.1f}")
393	    lines.append(f"- n_expert sweep: {N_EXPERT_LIST}")
394	    lines.append(f"- {N_MC} MC seeds per budget")
395	    lines.append("- HB method: MAP-EB (Gamma(3,1) prior)")
396	    lines.append(f"- |Bias| = avg across cells of |mean(bias) across seeds|")
397	    lines.append(f"- RMSE = avg across cells of sqrt(mean(bias²) across seeds)")
398	    lines.append("")
399	
400	    # Qwen CM table
401	    lines.append("## Qwen2.5-7B Per-Subgroup Confusion Matrix\n")
402	    lines.append("| Subgroup | π_s | FPR | FNR | 1-FPR-FNR |")
403	    lines.append("|----------|-----|-----|-----|-----------|")
404	    for s in SUBGROUP_LABELS:
405	        cm = SUBGROUP_CM[s]
406	        w = SUBGROUP_WEIGHTS[SUBGROUP_LABELS.index(s)]
407	        lines.append(f"| {s} | {w:.4f} | {cm['fpr']:.4f} | {cm['fnr']:.4f} | {1-cm['fpr']-cm['fnr']:.4f} |")
408	    lines.append("")
409	    qwen_fpr_range = max(cm['fpr'] for cm in SUBGROUP_CM.values()) - min(cm['fpr'] for cm in SUBGROUP_CM.values())
410	    qwen_fnr_range = max(cm['fnr'] for cm in SUBGROUP_CM.values()) - min(cm['fnr'] for cm in SUBGROUP_CM.values())
411	    llama_fpr_range = max(cm['fpr'] for cm in LLAMA_CM.values()) - min(cm['fpr'] for cm in LLAMA_CM.values())
412	    llama_fnr_range = max(cm['fnr'] for cm in LLAMA_CM.values()) - min(cm['fnr'] for cm in LLAMA_CM.values())
413	    lines.append(f"- Qwen Δ_FPR = {qwen_fpr_range:.4f}, Δ_FNR = {qwen_fnr_range:.4f}")
414	    lines.append(f"- Llama Δ_FPR = {llama_fpr_range:.4f}, Δ_FNR = {llama_fnr_range:.4f}")
415	    lines.append(f"- Qwen has {'larger' if qwen_fpr_range > llama_fpr_range else 'smaller'} FPR heterogeneity "
416	                 f"and {'larger' if qwen_fnr_range > llama_fnr_range else 'smaller'} FNR heterogeneity than Llama")
417	    lines.append("")
418	
419	    # Summary table
420	    lines.append("## Summary Table (averaged across all cells)\n")
421	    lines.append("| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |")
422	    lines.append("|----------|--------|-------|------|----------|----------|")
423	
424	    method_order = ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']
425	    method_labels = {'naive': 'Naive', 'global_corrected': 'Global', 'stratified_mle': 'Strat MLE', 'hb_ec_hte': 'HB EC-HTE'}
426	
427	    for ne in N_EXPERT_LIST:
428	        for m in method_order:
429	            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]
430	            if len(row) > 0:
431	                r = row.iloc[0]
432	                lines.append(f"| {ne} | {method_labels[m]} | {r['abs_bias']:.4f} | {r['rmse']:.4f} | {r['coverage']:.3f} | {r['ci_width']:.3f} |")
433	        lines.append("|----------|--------|-------|------|----------|----------|")
434	    lines.append("")
435	
436	    # EC-HTE vs Global comparison
437	    lines.append("## EC-HTE vs Global Comparison\n")
438	    lines.append("| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |")
439	    lines.append("|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|")
440	    for ne in N_EXPERT_LIST:
441	        sub = summary[summary['n_expert'] == ne]
442	        gc = sub[sub['method'] == 'global_corrected'].iloc[0]
443	        hb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]
444	        d_bias = gc['abs_bias'] - hb['abs_bias']
445	        d_rmse = gc['rmse'] - hb['rmse']
446	        wb = "**YES**" if hb['abs_bias'] < gc['abs_bias'] else "no"
447	        wr = "**YES**" if hb['rmse'] < gc['rmse'] else "no"
448	        lines.append(f"| {ne} | {gc['abs_bias']:.4f} | {hb['abs_bias']:.4f} | {d_bias:+.4f} | {gc['rmse']:.4f} | {hb['rmse']:.4f} | {d_rmse:+.4f} | {wb} | {wr} |")
449	    lines.append("")
450	
451	    # Per-subgroup breakdown
452	    lines.append("## Per-Subgroup Breakdown\n")
453	    for ne in N_EXPERT_LIST:
454	        lines.append(f"### n_expert = {ne}\n")
455	        lines.append("| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |")
456	        lines.append("|----------|-----|---|-------------|-------------|-------------|-------------|------------|")
457	        sub_df = df_raw[df_raw['n_expert'] == ne]
458	        for s_val in SUBGROUP_LABELS:
459	            dt = SUBGROUP_TAU[s_val]['tau_z1'] - SUBGROUP_TAU[s_val]['tau_z0']
460	            for z_level in [0, 1]:
461	                cell_gc = sub_df[(sub_df['method'] == 'global_corrected') & (sub_df['subgroup'] == s_val) & (sub_df['z_level'] == z_level)]
462	                cell_hb = sub_df[(sub_df['method'] == 'hb_ec_hte') & (sub_df['subgroup'] == s_val) & (sub_df['z_level'] == z_level)]
463	                bias_gc = abs(cell_gc['bias'].mean())
464	                bias_hb = abs(cell_hb['bias'].mean())
465	                rmse_gc = np.sqrt((cell_gc['bias'] ** 2).mean())
466	                rmse_hb = np.sqrt((cell_hb['bias'] ** 2).mean())
467	                imp = bias_gc - bias_hb
468	                lines.append(f"| {s_val} | {dt:.1f} | {z_level} | {bias_gc:.4f} | {bias_hb:.4f} | {imp:+.4f} | {rmse_gc:.4f} | {rmse_hb:.4f} |")
469	        lines.append("")
470	
471	    # Bias-variance decomposition
472	    lines.append("## Bias-Variance Decomposition\n")
473	    lines.append("| n_expert | Method | Bias² | Variance | MSE |")
474	    lines.append("|----------|--------|-------|----------|-----|")
475	    for ne in N_EXPERT_LIST:
476	        for m in method_order:
477	            sub_df = df_raw[(df_raw['n_expert'] == ne) & (df_raw['method'] == m)]
478	            cell_stats = (sub_df.groupby(['subgroup', 'z_level'])['bias']
479	                          .agg(['mean', 'var', 'count']).reset_index())
480	            mean_bias_sq = (cell_stats['mean'] ** 2).mean()
481	            variance = cell_stats['var'].mean()
482	            mse = mean_bias_sq + variance
483	            lines.append(f"| {ne} | {method_labels[m]} | {mean_bias_sq:.4f} | {variance:.4f} | {mse:.4f} |")
484	    lines.append("")
485	
486	    # Cross-model comparison with Llama
487	    lines.append("## Cross-Model Comparison: Qwen vs Llama (exp-023)\n")
488	    lines.append("### CM Heterogeneity\n")
489	    lines.append("| Metric | Qwen2.5-7B | Llama3.1-8B |")
490	    lines.append("|--------|-----------|------------|")
491	    lines.append(f"| Δ_FPR (max-min) | {qwen_fpr_range:.4f} | {llama_fpr_range:.4f} |")
492	    lines.append(f"| Δ_FNR (max-min) | {qwen_fnr_range:.4f} | {llama_fnr_range:.4f} |")
493	    lines.append(f"| Mean Δ_error | {(qwen_fpr_range+qwen_fnr_range)/2:.4f} | {(llama_fpr_range+llama_fnr_range)/2:.4f} |")
494	    lines.append("")
495	
496	    lines.append("### Bias Comparison\n")
497	    lines.append("| n_expert | Qwen |Bias|_Global | Qwen |Bias|_ECHTE | Qwen Δ|Bias| | Llama |Bias|_Global | Llama |Bias|_ECHTE | Llama Δ|Bias| |")
498	    lines.append("|----------|------------------|--------------------|--------------|--------------------|--------------------|---------------|")
499	    for ne in N_EXPERT_LIST:
500	        sub = summary[summary['n_expert'] == ne]
501	        qgc = sub[sub['method'] == 'global_corrected'].iloc[0]
502	        qhb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]
503	        qd = qgc['abs_bias'] - qhb['abs_bias']
504	        lr = LLAMA_RESULTS[ne]
505	        ld = lr['global_bias'] - lr['echte_bias']
506	        lines.append(f"| {ne} | {qgc['abs_bias']:.4f} | {qhb['abs_bias']:.4f} | {qd:+.4f} | {lr['global_bias']:.4f} | {lr['echte_bias']:.4f} | {ld:+.4f} |")
507	    lines.append("")
508	
509	    lines.append("### RMSE Comparison\n")
510	    lines.append("| n_expert | Qwen RMSE_Global | Qwen RMSE_ECHTE | Llama RMSE_Global | Llama RMSE_ECHTE |")
511	    lines.append("|----------|-----------------|----------------|------------------|-----------------|")
512	    for ne in N_EXPERT_LIST:
513	        sub = summary[summary['n_expert'] == ne]
514	        qgc = sub[sub['method'] == 'global_corrected'].iloc[0]
515	        qhb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]
516	        lr = LLAMA_RESULTS[ne]
517	        lines.append(f"| {ne} | {qgc['rmse']:.4f} | {qhb['rmse']:.4f} | {lr['global_rmse']:.4f} | {lr['echte_rmse']:.4f} |")
518	    lines.append("")
519	
520	    # Conclusion
521	    lines.append("## Conclusion\n")
522	    gc_all = summary[summary['method'] == 'global_corrected']
523	    hb_all = summary[summary['method'] == 'hb_ec_hte']
524	    n_bias_wins = 0
525	    n_rmse_wins = 0
526	    for ne in N_EXPERT_LIST:
527	        gc_row = gc_all[gc_all['n_expert'] == ne].iloc[0]
528	        hb_row = hb_all[hb_all['n_expert'] == ne].iloc[0]
529	        if hb_row['abs_bias'] < gc_row['abs_bias']:
530	            n_bias_wins += 1
531	        if hb_row['rmse'] < gc_row['rmse']:
532	            n_rmse_wins += 1
533	
534	    lines.append(f"EC-HTE wins on |Bias| in {n_bias_wins}/{len(N_EXPERT_LIST)} budget levels.")
535	    lines.append(f"EC-HTE wins on RMSE in {n_rmse_wins}/{len(N_EXPERT_LIST)} budget levels.\n")
536	
537	    if n_bias_wins == len(N_EXPERT_LIST):
538	        lines.append("**Result: Under heterogeneous-τ DGP with Qwen2.5-7B CMs, EC-HTE consistently outperforms Global correction in bias.**\n")
539	    elif n_bias_wins > 0:
540	        lines.append(f"**Result: Under heterogeneous-τ DGP with Qwen2.5-7B CMs, EC-HTE outperforms Global in bias at {n_bias_wins} of {len(N_EXPERT_LIST)} budget levels.**\n")
541	    else:
542	        lines.append("**Result: EC-HTE does not outperform Global in bias under this DGP configuration with Qwen CMs.**\n")
543	
544	    # Cross-model conclusion
545	    llama_bias_wins = sum(1 for ne in N_EXPERT_LIST if LLAMA_RESULTS[ne]['echte_bias'] < LLAMA_RESULTS[ne]['global_bias'])
546	    lines.append(f"**Cross-model consistency**: Llama EC-HTE wins on bias in {llama_bias_wins}/3 budgets; "
547	                 f"Qwen EC-HTE wins in {n_bias_wins}/3 budgets.")
548	    if n_bias_wins == len(N_EXPERT_LIST) and llama_bias_wins == len(N_EXPERT_LIST):
549	        lines.append("EC-HTE's bias advantage is consistent across both Llama and Qwen models.")
550	    lines.append("")
551	
552	    avg_qwen_improvement = np.mean([
553	        (summary[(summary['n_expert']==ne) & (summary['method']=='global_corrected')].iloc[0]['abs_bias'] -
554	         summary[(summary['n_expert']==ne) & (summary['method']=='hb_ec_hte')].iloc[0]['abs_bias'])
555	        for ne in N_EXPERT_LIST
556	    ])
557	    avg_llama_improvement = np.mean([
558	        LLAMA_RESULTS[ne]['global_bias'] - LLAMA_RESULTS[ne]['echte_bias']
559	        for ne in N_EXPERT_LIST
560	    ])
561	    lines.append(f"Average Δ|Bias| (Global - EC-HTE): Qwen = {avg_qwen_improvement:+.4f}, Llama = {avg_llama_improvement:+.4f}")
562	    if avg_qwen_improvement > avg_llama_improvement:
563	        lines.append(f"Qwen shows larger EC-HTE improvement, consistent with its greater CM heterogeneity "
564	                     f"(Δ_FPR={qwen_fpr_range:.3f} vs {llama_fpr_range:.3f}).")
565	    else:
566	        lines.append(f"Llama shows larger EC-HTE improvement despite smaller CM heterogeneity.")
567	    lines.append("")
568	
569	    report = "\n".join(lines)
570	    with open(outpath, 'w') as f:
571	        f.write(report)
572	    print(f"Wrote {outpath}")
573	
574	
575	# === Main ===
576	
577	if __name__ == '__main__':
578	    print("Qwen2.5-7B Heterogeneous-τ DGP: EC-HTE vs Global")
579	    print(f"N={N}, budgets={N_EXPERT_LIST}, seeds={N_MC}")
580	    print("Qwen per-subgroup CM:")
581	    for s in SUBGROUP_LABELS:
582	        cm = SUBGROUP_CM[s]
583	        print(f"  {s}: FPR={cm['fpr']:.4f}, FNR={cm['fnr']:.4f}")
584	    print("Subgroup τ values:")
585	    for s in SUBGROUP_LABELS:
586	        t = SUBGROUP_TAU[s]
587	        print(f"  {s}: τ(z=0)={t['tau_z0']}, τ(z=1)={t['tau_z1']}, Δτ={t['tau_z1']-t['tau_z0']:.1f}")
588	    print()
589	
590	    out_dir = 'artifacts/c1_multi_llm'
591	
592	    # Dry run: 1 budget, 1 seed
593	    print("=== Dry run (n_expert=200, 1 seed) ===")
594	    data = generate_data(SEED_BASE, 200)
595	    rows = run_one_mc(data, SEED_BASE)
596	    df_dry = pd.DataFrame(rows)
597	    df_dry['n_expert'] = 200
598	    print(f"Dry run OK: {len(df_dry)} rows, columns: {list(df_dry.columns)}")
599	    for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:
600	        sub = df_dry[df_dry['method'] == m]
601	        bias = sub['bias'].abs().mean()
602	        print(f"  {m:20s}: mean |bias| = {bias:.4f}")
603	
604	    # Verify oracle CATE values
605	    print("\n  Oracle CATE check:")
606	    for s_val in SUBGROUP_LABELS:
607	        for zl in [0, 1]:
608	            cell = df_dry[(df_dry['subgroup'] == s_val) & (df_dry['z_level'] == zl)]
609	            true_val = cell['cate_true'].iloc[0]
610	            expected = SUBGROUP_TAU[s_val]['tau_z1'] if zl == 1 else SUBGROUP_TAU[s_val]['tau_z0']
611	            ok = "OK" if abs(true_val - expected) < 1e-10 else "MISMATCH"
612	            print(f"    {s_val} z={zl}: cate_true={true_val:.2f} expected={expected:.2f} [{ok}]")
613	    print()
614	
615	    # Full run
616	    print(f"=== Full run ({len(N_EXPERT_LIST)} budgets x {N_MC} seeds) ===")
617	    all_results = []
618	    t0 = time.time()
619	    total_runs = len(N_EXPERT_LIST) * N_MC
620	    run_count = 0
621	
622	    for n_expert in N_EXPERT_LIST:
623	        print(f"\n--- n_expert = {n_expert} ---")
624	        t_budget = time.time()
625	        for mc in range(N_MC):
626	            seed = SEED_BASE + mc
627	            data = generate_data(seed, n_expert)
628	            mc_rows = run_one_mc(data, seed)
629	            for r in mc_rows:
630	                r['n_expert'] = n_expert
631	            all_results.extend(mc_rows)
632	            run_count += 1
633	            if (mc + 1) % 10 == 0:
634	                elapsed = time.time() - t0
635	                eta = elapsed / run_count * (total_runs - run_count)
636	                print(f"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s")
637	        budget_time = time.time() - t_budget
638	        print(f"  n_expert={n_expert} done in {budget_time:.1f}s")
639	
640	    total_time = time.time() - t0
641	    print(f"\nTotal time: {total_time:.1f}s")
642	
643	    df_raw = pd.DataFrame(all_results)
644	
645	    # Save results CSV
646	    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage', 'ci_width']
647	    df_raw[col_order].to_csv(f'{out_dir}/qwen_hetero_tau_results.csv', index=False)
648	    print(f"Saved qwen_hetero_tau_results.csv ({len(df_raw)} rows)")
649	
650	    # Write analysis
651	    write_analysis(df_raw, f'{out_dir}/qwen_hetero_tau_analysis.md')
652	
653	    # Print summary
654	    print("\n=== Summary ===")
655	    abs_bias = compute_corrected_abs_bias(df_raw)
656	    rmse_df = compute_rmse(df_raw)
657	    summary = abs_bias.merge(rmse_df, on=['n_expert', 'method'])
658	    for ne in N_EXPERT_LIST:
659	        print(f"\n  n_expert={ne}:")
660	        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:
661	            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]
662	            if len(row) > 0:
663	                print(f"    {m:20s}: |Bias|={row.iloc[0]['abs_bias']:.4f}  RMSE={row.iloc[0]['rmse']:.4f}")
664	    print()
665	
666	    # EC-HTE vs Global
667	    print("=== EC-HTE vs Global (Qwen) ===")
668	    for ne in N_EXPERT_LIST:
669	        gc = summary[(summary['n_expert'] == ne) & (summary['method'] == 'global_corrected')].iloc[0]
670	        hb = summary[(summary['n_expert'] == ne) & (summary['method'] == 'hb_ec_hte')].iloc[0]
671	        print(f"  n_expert={ne}: |Bias| Global={gc['abs_bias']:.4f} vs ECHTE={hb['abs_bias']:.4f} "
672	              f"({'ECHTE wins' if hb['abs_bias'] < gc['abs_bias'] else 'Global wins'})")
673	        print(f"              RMSE  Global={gc['rmse']:.4f} vs ECHTE={hb['rmse']:.4f} "
674	              f"({'ECHTE wins' if hb['rmse'] < gc['rmse'] else 'Global wins'})")
675	
676	    # Cross-model comparison
677	    print("\n=== Cross-Model: Qwen vs Llama ===")
678	    for ne in N_EXPERT_LIST:
679	        qgc = summary[(summary['n_expert'] == ne) & (summary['method'] == 'global_corrected')].iloc[0]
680	        qhb = summary[(summary['n_expert'] == ne) & (summary['method'] == 'hb_ec_hte')].iloc[0]
681	        lr = LLAMA_RESULTS[ne]
682	        print(f"  n_expert={ne}:")
683	        print(f"    Qwen  Δ|Bias| = {qgc['abs_bias'] - qhb['abs_bias']:+.4f}")
684	        print(f"    Llama Δ|Bias| = {lr['global_bias'] - lr['echte_bias']:+.4f}")
685	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "94af7560-c032-455a-82b6-70d91d329d77",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_qwen_hetero_tau.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nHeterogeneous-τ DGP experiment with Qwen2.5-7B confusion matrices.\nMirrors run_hetero_tau.py (Llama) but uses Qwen per-subgroup FPR/FNR.\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.optimize import minimize_scalar\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT_LIST = [200, 500, 1000]\nN_MC = 50\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']\nSUBGROUP_WEIGHTS = np.array([0.3816, 0.2224, 0.2551, 0.1408])\nSUBGROUP_WEIGHTS = SUBGROUP_WEIGHTS / SUBGROUP_WEIGHTS.sum()\n\nSUBGROUP_CM = {\n    'False_medium': {'fpr': 0.1800, 'fnr': 0.2874},\n    'False_short':  {'fpr': 0.2414, 'fnr': 0.1750},\n    'True_medium':  {'fpr': 0.2333, 'fnr': 0.2105},\n    'True_short':   {'fpr': 0.0000, 'fnr': 0.1379},\n}\n\nSUBGROUP_TAU = {\n    'True_short':   {'tau_z0': 0.2,  'tau_z1': 0.8},\n    'True_medium':  {'tau_z0': 0.35, 'tau_z1': 0.65},\n    'False_short':  {'tau_z0': 0.4,  'tau_z1': 0.5},\n    'False_medium': {'tau_z0': 0.45, 'tau_z1': 0.55},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\n\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === MAP-EB ===\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):\n    hp_rate = 1.0 / hp_scale\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = hp_shape * hp_scale\n            continue\n\n        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):\n            nll = _dirmult_neg_ll(a, _cl)\n            if a < 1e-10:\n                return 1e10\n            log_prior = (_shape - 1.0) * np.log(a) - _rate * a\n            return nll - log_prior\n\n        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n_sz = counts[i, z, :].sum()\n            d = n_sz + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    return C, alpha_opt\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\n# === DGP (heterogeneous tau) ===\n\ndef generate_data(seed, n_expert):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(4):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.zeros(N)\n    for i, s in enumerate(SUBGROUP_LABELS):\n        s_mask = S_idx == i\n        tau_s = SUBGROUP_TAU[s]\n        tau_vals[s_mask] = np.where(Z[s_mask] == 1, tau_s['tau_z1'], tau_s['tau_z0'])\n\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb, _ = estimate_cm_hb_map_eb(counts, SUBGROUP_LABELS)\n\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n        tau_s = SUBGROUP_TAU[s_val]\n\n        for z_level in [0, 1]:\n            oracle_cate = tau_s['tau_z1'] if z_level == 1 else tau_s['tau_z0']\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_w_nv = 2 * 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'cate_est': th_nv, 'cate_true': oracle_cate,\n                'coverage': cov_nv, 'ci_width': ci_w_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_w_gc = 2 * 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'cate_est': th_gc, 'cate_true': oracle_cate,\n                'coverage': cov_gc, 'ci_width': ci_w_gc,\n            })\n\n            # Stratified MLE\n            ci_w_ml = 2 * 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'cate_est': th_ml, 'cate_true': oracle_cate,\n                'coverage': cov_ml, 'ci_width': ci_w_ml,\n            })\n\n            # HB EC-HTE (MAP-EB)\n            ci_w_hb = 2 * 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'cate_est': th_hb, 'cate_true': oracle_cate,\n                'coverage': cov_hb, 'ci_width': ci_w_hb,\n            })\n\n    return rows\n\n\n# === Aggregation ===\n\ndef compute_corrected_abs_bias(df):\n    cell_bias = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias']\n                 .mean().abs().reset_index(name='abs_mean_bias'))\n    return (cell_bias.groupby(['n_expert', 'method'])['abs_mean_bias']\n            .mean().reset_index(name='abs_bias'))\n\n\ndef compute_rmse(df):\n    cell_rmse = (df.assign(bias_sq=df['bias'] ** 2)\n                 .groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias_sq']\n                 .mean().apply(np.sqrt).reset_index(name='rmse'))\n    return (cell_rmse.groupby(['n_expert', 'method'])['rmse']\n            .mean().reset_index(name='rmse'))\n\n\ndef compute_coverage(df):\n    return (df.groupby(['n_expert', 'method'])['coverage']\n            .mean().reset_index(name='coverage'))\n\n\ndef compute_ci_width(df):\n    return (df.groupby(['n_expert', 'method'])['ci_width']\n            .mean().reset_index(name='ci_width'))\n\n\n# === Analysis Report ===\n\nLLAMA_RESULTS = {\n    200:  {'global_bias': 0.0365, 'echte_bias': 0.0248, 'global_rmse': 0.1780, 'echte_rmse': 0.2606},\n    500:  {'global_bias': 0.0314, 'echte_bias': 0.0099, 'global_rmse': 0.1580, 'echte_rmse': 0.1760},\n    1000: {'global_bias': 0.0286, 'echte_bias': 0.0130, 'global_rmse': 0.1554, 'echte_rmse': 0.1602},\n}\n\nLLAMA_CM = {\n    'False_medium': {'fpr': 0.235, 'fnr': 0.319},\n    'False_short':  {'fpr': 0.310, 'fnr': 0.212},\n    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},\n    'True_short':   {'fpr': 0.091, 'fnr': 0.190},\n}\n\n\ndef write_analysis(df_raw, outpath):\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse = compute_rmse(df_raw)\n    cov = compute_coverage(df_raw)\n    ciw = compute_ci_width(df_raw)\n\n    summary = abs_bias.merge(rmse, on=['n_expert', 'method']).merge(\n        cov, on=['n_expert', 'method']).merge(ciw, on=['n_expert', 'method'])\n\n    lines = []\n    lines.append(\"# Qwen2.5-7B Heterogeneous-τ DGP: EC-HTE vs Global Correction\\n\")\n    lines.append(\"## Design\\n\")\n    lines.append(f\"- N={N}, P(Z=1)={P_Z1}, K=4 subgroups\")\n    lines.append(\"- **LLM**: Qwen2.5-7B (balanced binarization)\")\n    lines.append(\"- **Heterogeneous τ(z) across subgroups:**\")\n    for s in SUBGROUP_LABELS:\n        t = SUBGROUP_TAU[s]\n        lines.append(f\"  - {s}: τ(z=0)={t['tau_z0']}, τ(z=1)={t['tau_z1']}, Δτ={t['tau_z1']-t['tau_z0']:.1f}\")\n    lines.append(f\"- n_expert sweep: {N_EXPERT_LIST}\")\n    lines.append(f\"- {N_MC} MC seeds per budget\")\n    lines.append(\"- HB method: MAP-EB (Gamma(3,1) prior)\")\n    lines.append(f\"- |Bias| = avg across cells of |mean(bias) across seeds|\")\n    lines.append(f\"- RMSE = avg across cells of sqrt(mean(bias²) across seeds)\")\n    lines.append(\"\")\n\n    # Qwen CM table\n    lines.append(\"## Qwen2.5-7B Per-Subgroup Confusion Matrix\\n\")\n    lines.append(\"| Subgroup | π_s | FPR | FNR | 1-FPR-FNR |\")\n    lines.append(\"|----------|-----|-----|-----|-----------|\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        w = SUBGROUP_WEIGHTS[SUBGROUP_LABELS.index(s)]\n        lines.append(f\"| {s} | {w:.4f} | {cm['fpr']:.4f} | {cm['fnr']:.4f} | {1-cm['fpr']-cm['fnr']:.4f} |\")\n    lines.append(\"\")\n    qwen_fpr_range = max(cm['fpr'] for cm in SUBGROUP_CM.values()) - min(cm['fpr'] for cm in SUBGROUP_CM.values())\n    qwen_fnr_range = max(cm['fnr'] for cm in SUBGROUP_CM.values()) - min(cm['fnr'] for cm in SUBGROUP_CM.values())\n    llama_fpr_range = max(cm['fpr'] for cm in LLAMA_CM.values()) - min(cm['fpr'] for cm in LLAMA_CM.values())\n    llama_fnr_range = max(cm['fnr'] for cm in LLAMA_CM.values()) - min(cm['fnr'] for cm in LLAMA_CM.values())\n    lines.append(f\"- Qwen Δ_FPR = {qwen_fpr_range:.4f}, Δ_FNR = {qwen_fnr_range:.4f}\")\n    lines.append(f\"- Llama Δ_FPR = {llama_fpr_range:.4f}, Δ_FNR = {llama_fnr_range:.4f}\")\n    lines.append(f\"- Qwen has {'larger' if qwen_fpr_range > llama_fpr_range else 'smaller'} FPR heterogeneity \"\n                 f\"and {'larger' if qwen_fnr_range > llama_fnr_range else 'smaller'} FNR heterogeneity than Llama\")\n    lines.append(\"\")\n\n    # Summary table\n    lines.append(\"## Summary Table (averaged across all cells)\\n\")\n    lines.append(\"| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |\")\n    lines.append(\"|----------|--------|-------|------|----------|----------|\")\n\n    method_order = ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']\n    method_labels = {'naive': 'Naive', 'global_corrected': 'Global', 'stratified_mle': 'Strat MLE', 'hb_ec_hte': 'HB EC-HTE'}\n\n    for ne in N_EXPERT_LIST:\n        for m in method_order:\n            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n            if len(row) > 0:\n                r = row.iloc[0]\n                lines.append(f\"| {ne} | {method_labels[m]} | {r['abs_bias']:.4f} | {r['rmse']:.4f} | {r['coverage']:.3f} | {r['ci_width']:.3f} |\")\n        lines.append(\"|----------|--------|-------|------|----------|----------|\")\n    lines.append(\"\")\n\n    # EC-HTE vs Global comparison\n    lines.append(\"## EC-HTE vs Global Comparison\\n\")\n    lines.append(\"| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |\")\n    lines.append(\"|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|\")\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        gc = sub[sub['method'] == 'global_corrected'].iloc[0]\n        hb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]\n        d_bias = gc['abs_bias'] - hb['abs_bias']\n        d_rmse = gc['rmse'] - hb['rmse']\n        wb = \"**YES**\" if hb['abs_bias'] < gc['abs_bias'] else \"no\"\n        wr = \"**YES**\" if hb['rmse'] < gc['rmse'] else \"no\"\n        lines.append(f\"| {ne} | {gc['abs_bias']:.4f} | {hb['abs_bias']:.4f} | {d_bias:+.4f} | {gc['rmse']:.4f} | {hb['rmse']:.4f} | {d_rmse:+.4f} | {wb} | {wr} |\")\n    lines.append(\"\")\n\n    # Per-subgroup breakdown\n    lines.append(\"## Per-Subgroup Breakdown\\n\")\n    for ne in N_EXPERT_LIST:\n        lines.append(f\"### n_expert = {ne}\\n\")\n        lines.append(\"| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |\")\n        lines.append(\"|----------|-----|---|-------------|-------------|-------------|-------------|------------|\")\n        sub_df = df_raw[df_raw['n_expert'] == ne]\n        for s_val in SUBGROUP_LABELS:\n            dt = SUBGROUP_TAU[s_val]['tau_z1'] - SUBGROUP_TAU[s_val]['tau_z0']\n            for z_level in [0, 1]:\n                cell_gc = sub_df[(sub_df['method'] == 'global_corrected') & (sub_df['subgroup'] == s_val) & (sub_df['z_level'] == z_level)]\n                cell_hb = sub_df[(sub_df['method'] == 'hb_ec_hte') & (sub_df['subgroup'] == s_val) & (sub_df['z_level'] == z_level)]\n                bias_gc = abs(cell_gc['bias'].mean())\n                bias_hb = abs(cell_hb['bias'].mean())\n                rmse_gc = np.sqrt((cell_gc['bias'] ** 2).mean())\n                rmse_hb = np.sqrt((cell_hb['bias'] ** 2).mean())\n                imp = bias_gc - bias_hb\n                lines.append(f\"| {s_val} | {dt:.1f} | {z_level} | {bias_gc:.4f} | {bias_hb:.4f} | {imp:+.4f} | {rmse_gc:.4f} | {rmse_hb:.4f} |\")\n        lines.append(\"\")\n\n    # Bias-variance decomposition\n    lines.append(\"## Bias-Variance Decomposition\\n\")\n    lines.append(\"| n_expert | Method | Bias² | Variance | MSE |\")\n    lines.append(\"|----------|--------|-------|----------|-----|\")\n    for ne in N_EXPERT_LIST:\n        for m in method_order:\n            sub_df = df_raw[(df_raw['n_expert'] == ne) & (df_raw['method'] == m)]\n            cell_stats = (sub_df.groupby(['subgroup', 'z_level'])['bias']\n                          .agg(['mean', 'var', 'count']).reset_index())\n            mean_bias_sq = (cell_stats['mean'] ** 2).mean()\n            variance = cell_stats['var'].mean()\n            mse = mean_bias_sq + variance\n            lines.append(f\"| {ne} | {method_labels[m]} | {mean_bias_sq:.4f} | {variance:.4f} | {mse:.4f} |\")\n    lines.append(\"\")\n\n    # Cross-model comparison with Llama\n    lines.append(\"## Cross-Model Comparison: Qwen vs Llama (exp-023)\\n\")\n    lines.append(\"### CM Heterogeneity\\n\")\n    lines.append(\"| Metric | Qwen2.5-7B | Llama3.1-8B |\")\n    lines.append(\"|--------|-----------|------------|\")\n    lines.append(f\"| Δ_FPR (max-min) | {qwen_fpr_range:.4f} | {llama_fpr_range:.4f} |\")\n    lines.append(f\"| Δ_FNR (max-min) | {qwen_fnr_range:.4f} | {llama_fnr_range:.4f} |\")\n    lines.append(f\"| Mean Δ_error | {(qwen_fpr_range+qwen_fnr_range)/2:.4f} | {(llama_fpr_range+llama_fnr_range)/2:.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Bias Comparison\\n\")\n    lines.append(\"| n_expert | Qwen |Bias|_Global | Qwen |Bias|_ECHTE | Qwen Δ|Bias| | Llama |Bias|_Global | Llama |Bias|_ECHTE | Llama Δ|Bias| |\")\n    lines.append(\"|----------|------------------|--------------------|--------------|--------------------|--------------------|---------------|\")\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        qgc = sub[sub['method'] == 'global_corrected'].iloc[0]\n        qhb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]\n        qd = qgc['abs_bias'] - qhb['abs_bias']\n        lr = LLAMA_RESULTS[ne]\n        ld = lr['global_bias'] - lr['echte_bias']\n        lines.append(f\"| {ne} | {qgc['abs_bias']:.4f} | {qhb['abs_bias']:.4f} | {qd:+.4f} | {lr['global_bias']:.4f} | {lr['echte_bias']:.4f} | {ld:+.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### RMSE Comparison\\n\")\n    lines.append(\"| n_expert | Qwen RMSE_Global | Qwen RMSE_ECHTE | Llama RMSE_Global | Llama RMSE_ECHTE |\")\n    lines.append(\"|----------|-----------------|----------------|------------------|-----------------|\")\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        qgc = sub[sub['method'] == 'global_corrected'].iloc[0]\n        qhb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]\n        lr = LLAMA_RESULTS[ne]\n        lines.append(f\"| {ne} | {qgc['rmse']:.4f} | {qhb['rmse']:.4f} | {lr['global_rmse']:.4f} | {lr['echte_rmse']:.4f} |\")\n    lines.append(\"\")\n\n    # Conclusion\n    lines.append(\"## Conclusion\\n\")\n    gc_all = summary[summary['method'] == 'global_corrected']\n    hb_all = summary[summary['method'] == 'hb_ec_hte']\n    n_bias_wins = 0\n    n_rmse_wins = 0\n    for ne in N_EXPERT_LIST:\n        gc_row = gc_all[gc_all['n_expert'] == ne].iloc[0]\n        hb_row = hb_all[hb_all['n_expert'] == ne].iloc[0]\n        if hb_row['abs_bias'] < gc_row['abs_bias']:\n            n_bias_wins += 1\n        if hb_row['rmse'] < gc_row['rmse']:\n            n_rmse_wins += 1\n\n    lines.append(f\"EC-HTE wins on |Bias| in {n_bias_wins}/{len(N_EXPERT_LIST)} budget levels.\")\n    lines.append(f\"EC-HTE wins on RMSE in {n_rmse_wins}/{len(N_EXPERT_LIST)} budget levels.\\n\")\n\n    if n_bias_wins == len(N_EXPERT_LIST):\n        lines.append(\"**Result: Under heterogeneous-τ DGP with Qwen2.5-7B CMs, EC-HTE consistently outperforms Global correction in bias.**\\n\")\n    elif n_bias_wins > 0:\n        lines.append(f\"**Result: Under heterogeneous-τ DGP with Qwen2.5-7B CMs, EC-HTE outperforms Global in bias at {n_bias_wins} of {len(N_EXPERT_LIST)} budget levels.**\\n\")\n    else:\n        lines.append(\"**Result: EC-HTE does not outperform Global in bias under this DGP configuration with Qwen CMs.**\\n\")\n\n    # Cross-model conclusion\n    llama_bias_wins = sum(1 for ne in N_EXPERT_LIST if LLAMA_RESULTS[ne]['echte_bias'] < LLAMA_RESULTS[ne]['global_bias'])\n    lines.append(f\"**Cross-model consistency**: Llama EC-HTE wins on bias in {llama_bias_wins}/3 budgets; \"\n                 f\"Qwen EC-HTE wins in {n_bias_wins}/3 budgets.\")\n    if n_bias_wins == len(N_EXPERT_LIST) and llama_bias_wins == len(N_EXPERT_LIST):\n        lines.append(\"EC-HTE's bias advantage is consistent across both Llama and Qwen models.\")\n    lines.append(\"\")\n\n    avg_qwen_improvement = np.mean([\n        (summary[(summary['n_expert']==ne) & (summary['method']=='global_corrected')].iloc[0]['abs_bias'] -\n         summary[(summary['n_expert']==ne) & (summary['method']=='hb_ec_hte')].iloc[0]['abs_bias'])\n        for ne in N_EXPERT_LIST\n    ])\n    avg_llama_improvement = np.mean([\n        LLAMA_RESULTS[ne]['global_bias'] - LLAMA_RESULTS[ne]['echte_bias']\n        for ne in N_EXPERT_LIST\n    ])\n    lines.append(f\"Average Δ|Bias| (Global - EC-HTE): Qwen = {avg_qwen_improvement:+.4f}, Llama = {avg_llama_improvement:+.4f}\")\n    if avg_qwen_improvement > avg_llama_improvement:\n        lines.append(f\"Qwen shows larger EC-HTE improvement, consistent with its greater CM heterogeneity \"\n                     f\"(Δ_FPR={qwen_fpr_range:.3f} vs {llama_fpr_range:.3f}).\")\n    else:\n        lines.append(f\"Llama shows larger EC-HTE improvement despite smaller CM heterogeneity.\")\n    lines.append(\"\")\n\n    report = \"\\n\".join(lines)\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"Qwen2.5-7B Heterogeneous-τ DGP: EC-HTE vs Global\")\n    print(f\"N={N}, budgets={N_EXPERT_LIST}, seeds={N_MC}\")\n    print(\"Qwen per-subgroup CM:\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.4f}, FNR={cm['fnr']:.4f}\")\n    print(\"Subgroup τ values:\")\n    for s in SUBGROUP_LABELS:\n        t = SUBGROUP_TAU[s]\n        print(f\"  {s}: τ(z=0)={t['tau_z0']}, τ(z=1)={t['tau_z1']}, Δτ={t['tau_z1']-t['tau_z0']:.1f}\")\n    print()\n\n    out_dir = 'artifacts/c1_multi_llm'\n\n    # Dry run: 1 budget, 1 seed\n    print(\"=== Dry run (n_expert=200, 1 seed) ===\")\n    data = generate_data(SEED_BASE, 200)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    df_dry['n_expert'] = 200\n    print(f\"Dry run OK: {len(df_dry)} rows, columns: {list(df_dry.columns)}\")\n    for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n\n    # Verify oracle CATE values\n    print(\"\\n  Oracle CATE check:\")\n    for s_val in SUBGROUP_LABELS:\n        for zl in [0, 1]:\n            cell = df_dry[(df_dry['subgroup'] == s_val) & (df_dry['z_level'] == zl)]\n            true_val = cell['cate_true'].iloc[0]\n            expected = SUBGROUP_TAU[s_val]['tau_z1'] if zl == 1 else SUBGROUP_TAU[s_val]['tau_z0']\n            ok = \"OK\" if abs(true_val - expected) < 1e-10 else \"MISMATCH\"\n            print(f\"    {s_val} z={zl}: cate_true={true_val:.2f} expected={expected:.2f} [{ok}]\")\n    print()\n\n    # Full run\n    print(f\"=== Full run ({len(N_EXPERT_LIST)} budgets x {N_MC} seeds) ===\")\n    all_results = []\n    t0 = time.time()\n    total_runs = len(N_EXPERT_LIST) * N_MC\n    run_count = 0\n\n    for n_expert in N_EXPERT_LIST:\n        print(f\"\\n--- n_expert = {n_expert} ---\")\n        t_budget = time.time()\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            data = generate_data(seed, n_expert)\n            mc_rows = run_one_mc(data, seed)\n            for r in mc_rows:\n                r['n_expert'] = n_expert\n            all_results.extend(mc_rows)\n            run_count += 1\n            if (mc + 1) % 10 == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / run_count * (total_runs - run_count)\n                print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n        budget_time = time.time() - t_budget\n        print(f\"  n_expert={n_expert} done in {budget_time:.1f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(all_results)\n\n    # Save results CSV\n    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage', 'ci_width']\n    df_raw[col_order].to_csv(f'{out_dir}/qwen_hetero_tau_results.csv', index=False)\n    print(f\"Saved qwen_hetero_tau_results.csv ({len(df_raw)} rows)\")\n\n    # Write analysis\n    write_analysis(df_raw, f'{out_dir}/qwen_hetero_tau_analysis.md')\n\n    # Print summary\n    print(\"\\n=== Summary ===\")\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse_df = compute_rmse(df_raw)\n    summary = abs_bias.merge(rmse_df, on=['n_expert', 'method'])\n    for ne in N_EXPERT_LIST:\n        print(f\"\\n  n_expert={ne}:\")\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n            if len(row) > 0:\n                print(f\"    {m:20s}: |Bias|={row.iloc[0]['abs_bias']:.4f}  RMSE={row.iloc[0]['rmse']:.4f}\")\n    print()\n\n    # EC-HTE vs Global\n    print(\"=== EC-HTE vs Global (Qwen) ===\")\n    for ne in N_EXPERT_LIST:\n        gc = summary[(summary['n_expert'] == ne) & (summary['method'] == 'global_corrected')].iloc[0]\n        hb = summary[(summary['n_expert'] == ne) & (summary['method'] == 'hb_ec_hte')].iloc[0]\n        print(f\"  n_expert={ne}: |Bias| Global={gc['abs_bias']:.4f} vs ECHTE={hb['abs_bias']:.4f} \"\n              f\"({'ECHTE wins' if hb['abs_bias'] < gc['abs_bias'] else 'Global wins'})\")\n        print(f\"              RMSE  Global={gc['rmse']:.4f} vs ECHTE={hb['rmse']:.4f} \"\n              f\"({'ECHTE wins' if hb['rmse'] < gc['rmse'] else 'Global wins'})\")\n\n    # Cross-model comparison\n    print(\"\\n=== Cross-Model: Qwen vs Llama ===\")\n    for ne in N_EXPERT_LIST:\n        qgc = summary[(summary['n_expert'] == ne) & (summary['method'] == 'global_corrected')].iloc[0]\n        qhb = summary[(summary['n_expert'] == ne) & (summary['method'] == 'hb_ec_hte')].iloc[0]\n        lr = LLAMA_RESULTS[ne]\n        print(f\"  n_expert={ne}:\")\n        print(f\"    Qwen  Δ|Bias| = {qgc['abs_bias'] - qhb['abs_bias']:+.4f}\")\n        print(f\"    Llama Δ|Bias| = {lr['global_bias'] - lr['echte_bias']:+.4f}\")\n",
      "numLines": 685,
      "startLine": 1,
      "totalLines": 685
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

Now I'll also read the Qwen analysis file for reference on the report format, and check the existing Llama hetero_tau_analysis for cross-model comparison data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "f0bafd70-2335-4213-add8-4d36b90803b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JFxnpnHiTzpUi7tEPofdS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13636,
      "cache_read_input_tokens": 18397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13636
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

_source line 8_

<details open><summary>🔧 Tool call — Agent · `toolu_01WubYAsQYWHZYfDxaXfpR4a`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find Qwen analysis and Llama results",
  "prompt": "Find the Qwen hetero_tau_analysis.md and Llama hetero_tau_analysis.md files used in the cross-model comparison. Look in:\n1. /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/qwen_hetero_tau_analysis.md\n2. /home/ubuntu/ec_hte_llm_annotation/artifacts/exp-023/ or similar directories for Llama hetero_tau_analysis.md\n\nRead both files and report back their full contents so I can use them for the Gemma cross-model comparison section."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "e77cef56-c915-4522-9aa4-364f2b5cf420",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JFxnpnHiTzpUi7tEPofdS8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13636,
      "cache_read_input_tokens": 18397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13636
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

_source line 9_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a3ce3846bb26060b4",
  "tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "description": "Find Qwen analysis and Llama results",
  "task_type": "local_agent",
  "prompt": "Find the Qwen hetero_tau_analysis.md and Llama hetero_tau_analysis.md files used in the cross-model comparison. Look in:\n1. /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/qwen_hetero_tau_analysis.md\n2. /home/ubuntu/ec_hte_llm_annotation/artifacts/exp-023/ or similar directories for Llama hetero_tau_analysis.md\n\nRead both files and report back their full contents so I can use them for the Gemma cross-model comparison section.",
  "uuid": "ce3b32a0-54ba-4237-8435-0e9afe59f2f7",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0"
}
```

---

## Round 1

39 recorded events

### User

_source line 10 · 2026-05-22T00:15:02.733Z_

Find the Qwen hetero_tau_analysis.md and Llama hetero_tau_analysis.md files used in the cross-model comparison. Look in:
1. /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/qwen_hetero_tau_analysis.md
2. /home/ubuntu/ec_hte_llm_annotation/artifacts/exp-023/ or similar directories for Llama hetero_tau_analysis.md

Read both files and report back their full contents so I can use them for the Gemma cross-model comparison section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "614c957c-6cf2-4a66-94d5-acac9f913b30"
}
```

</details>

---

### System

_source line 11_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3ce3846bb26060b4",
  "tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "description": "Reading artifacts/c1_multi_llm/qwen_hetero_tau_analysis.md",
  "usage": {
    "total_tokens": 17895,
    "tool_uses": 1,
    "duration_ms": 1616
  },
  "last_tool_name": "Read",
  "uuid": "84c5a499-c2c6-43a9-8c40-df42e8f6606a",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0"
}
```

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_013Ue2jueX8Qryz85WEUSzWB`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/qwen_hetero_tau_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "310751e5-96ab-48db-af72-7a8cfae93b66",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E89GwEV9GajiFjkLTDCX7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17878,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17878,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 13 · 2026-05-22T00:15:04.357Z_

<details><summary>↩ Tool result · `toolu_013Ue2jueX8Qryz85WEUSzWB`</summary>

```text
1	# Qwen2.5-7B Heterogeneous-τ DGP: EC-HTE vs Global Correction
2	
3	## Design
4	
5	- N=5000, P(Z=1)=0.652, K=4 subgroups
6	- **LLM**: Qwen2.5-7B (balanced binarization)
7	- **Heterogeneous τ(z) across subgroups:**
8	  - False_medium: τ(z=0)=0.45, τ(z=1)=0.55, Δτ=0.1
9	  - False_short: τ(z=0)=0.4, τ(z=1)=0.5, Δτ=0.1
10	  - True_medium: τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3
11	  - True_short: τ(z=0)=0.2, τ(z=1)=0.8, Δτ=0.6
12	- n_expert sweep: [200, 500, 1000]
13	- 50 MC seeds per budget
14	- HB method: MAP-EB (Gamma(3,1) prior)
15	- |Bias| = avg across cells of |mean(bias) across seeds|
16	- RMSE = avg across cells of sqrt(mean(bias²) across seeds)
17	
18	## Qwen2.5-7B Per-Subgroup Confusion Matrix
19	
20	| Subgroup | π_s | FPR | FNR | 1-FPR-FNR |
21	|----------|-----|-----|-----|-----------|
22	| False_medium | 0.3816 | 0.1800 | 0.2874 | 0.5326 |
23	| False_short | 0.2224 | 0.2414 | 0.1750 | 0.5836 |
24	| True_medium | 0.2551 | 0.2333 | 0.2105 | 0.5562 |
25	| True_short | 0.1408 | 0.0000 | 0.1379 | 0.8621 |
26	
27	- Qwen Δ_FPR = 0.2414, Δ_FNR = 0.1495
28	- Llama Δ_FPR = 0.2190, Δ_FNR = 0.1290
29	- Qwen has larger FPR heterogeneity and larger FNR heterogeneity than Llama
30	
31	## Summary Table (averaged across all cells)
32	
33	| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |
34	|----------|--------|-------|------|----------|----------|
35	| 200 | Naive | 0.0575 | 0.1060 | 0.900 | 0.334 |
36	| 200 | Global | 0.0368 | 0.1546 | 0.907 | 0.512 |
37	| 200 | Strat MLE | 0.0282 | 0.2288 | 0.800 | 0.548 |
38	| 200 | HB EC-HTE | 0.0275 | 0.2293 | 0.802 | 0.546 |
39	|----------|--------|-------|------|----------|----------|
40	| 500 | Naive | 0.0575 | 0.1060 | 0.900 | 0.334 |
41	| 500 | Global | 0.0336 | 0.1362 | 0.938 | 0.501 |
42	| 500 | Strat MLE | 0.0215 | 0.1639 | 0.875 | 0.498 |
43	| 500 | HB EC-HTE | 0.0196 | 0.1631 | 0.873 | 0.495 |
44	|----------|--------|-------|------|----------|----------|
45	| 1000 | Naive | 0.0575 | 0.1060 | 0.900 | 0.334 |
46	| 1000 | Global | 0.0328 | 0.1314 | 0.940 | 0.496 |
47	| 1000 | Strat MLE | 0.0181 | 0.1399 | 0.905 | 0.481 |
48	| 1000 | HB EC-HTE | 0.0165 | 0.1393 | 0.902 | 0.480 |
49	|----------|--------|-------|------|----------|----------|
50	
51	## EC-HTE vs Global Comparison
52	
53	| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |
54	|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|
55	| 200 | 0.0368 | 0.0275 | +0.0093 | 0.1546 | 0.2293 | -0.0747 | **YES** | no |
56	| 500 | 0.0336 | 0.0196 | +0.0141 | 0.1362 | 0.1631 | -0.0269 | **YES** | no |
57	| 1000 | 0.0328 | 0.0165 | +0.0162 | 0.1314 | 0.1393 | -0.0079 | **YES** | no |
58	
59	## Per-Subgroup Breakdown
60	
61	### n_expert = 200
62	
63	| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
64	|----------|-----|---|-------------|-------------|-------------|-------------|------------|
65	| False_medium | 0.1 | 0 | 0.0175 | 0.0252 | -0.0077 | 0.1639 | 0.2191 |
66	| False_medium | 0.1 | 1 | 0.0082 | 0.0284 | -0.0202 | 0.0905 | 0.1183 |
67	| False_short | 0.1 | 0 | 0.0032 | 0.0225 | -0.0193 | 0.2131 | 0.3422 |
68	| False_short | 0.1 | 1 | 0.0069 | 0.0063 | +0.0007 | 0.1158 | 0.1807 |
69	| True_medium | 0.3 | 0 | 0.0545 | 0.0669 | -0.0124 | 0.1786 | 0.2636 |
70	| True_medium | 0.3 | 1 | 0.0106 | 0.0033 | +0.0073 | 0.0934 | 0.1514 |
71	| True_short | 0.6 | 0 | 0.1156 | 0.0406 | +0.0750 | 0.2193 | 0.3421 |
72	| True_short | 0.6 | 1 | 0.0780 | 0.0268 | +0.0512 | 0.1619 | 0.2168 |
73	
74	### n_expert = 500
75	
76	| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
77	|----------|-----|---|-------------|-------------|-------------|-------------|------------|
78	| False_medium | 0.1 | 0 | 0.0156 | 0.0074 | +0.0082 | 0.1348 | 0.1767 |
79	| False_medium | 0.1 | 1 | 0.0031 | 0.0141 | -0.0110 | 0.0777 | 0.0945 |
80	| False_short | 0.1 | 0 | 0.0002 | 0.0201 | -0.0199 | 0.1854 | 0.2451 |
81	| False_short | 0.1 | 1 | 0.0114 | 0.0050 | +0.0064 | 0.1034 | 0.1353 |
82	| True_medium | 0.3 | 0 | 0.0580 | 0.0509 | +0.0070 | 0.1528 | 0.1938 |
83	| True_medium | 0.3 | 1 | 0.0177 | 0.0045 | +0.0132 | 0.0837 | 0.1091 |
84	| True_short | 0.6 | 0 | 0.1012 | 0.0395 | +0.0617 | 0.2031 | 0.2016 |
85	| True_short | 0.6 | 1 | 0.0621 | 0.0152 | +0.0469 | 0.1483 | 0.1486 |
86	
87	### n_expert = 1000
88	
89	| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
90	|----------|-----|---|-------------|-------------|-------------|-------------|------------|
91	| False_medium | 0.1 | 0 | 0.0151 | 0.0087 | +0.0064 | 0.1299 | 0.1746 |
92	| False_medium | 0.1 | 1 | 0.0017 | 0.0024 | -0.0007 | 0.0715 | 0.0836 |
93	| False_short | 0.1 | 0 | 0.0019 | 0.0004 | +0.0015 | 0.1758 | 0.1900 |
94	| False_short | 0.1 | 1 | 0.0123 | 0.0053 | +0.0070 | 0.1020 | 0.1139 |
95	| True_medium | 0.3 | 0 | 0.0576 | 0.0395 | +0.0181 | 0.1480 | 0.1621 |
96	| True_medium | 0.3 | 1 | 0.0195 | 0.0001 | +0.0194 | 0.0814 | 0.0896 |
97	| True_short | 0.6 | 0 | 0.0971 | 0.0497 | +0.0474 | 0.1980 | 0.1679 |
98	| True_short | 0.6 | 1 | 0.0571 | 0.0262 | +0.0309 | 0.1443 | 0.1325 |
99	
100	## Bias-Variance Decomposition
101	
102	| n_expert | Method | Bias² | Variance | MSE |
103	|----------|--------|-------|----------|-----|
104	| 200 | Naive | 0.0059 | 0.0072 | 0.0131 |
105	| 200 | Global | 0.0029 | 0.0237 | 0.0266 |
106	| 200 | Strat MLE | 0.0013 | 0.0582 | 0.0595 |
107	| 200 | HB EC-HTE | 0.0011 | 0.0586 | 0.0597 |
108	| 500 | Naive | 0.0059 | 0.0072 | 0.0131 |
109	| 500 | Global | 0.0023 | 0.0185 | 0.0207 |
110	| 500 | Strat MLE | 0.0008 | 0.0290 | 0.0298 |
111	| 500 | HB EC-HTE | 0.0006 | 0.0288 | 0.0294 |
112	| 1000 | Naive | 0.0059 | 0.0072 | 0.0131 |
113	| 1000 | Global | 0.0021 | 0.0172 | 0.0193 |
114	| 1000 | Strat MLE | 0.0007 | 0.0208 | 0.0214 |
115	| 1000 | HB EC-HTE | 0.0006 | 0.0206 | 0.0212 |
116	
117	## Cross-Model Comparison: Qwen vs Llama (exp-023)
118	
119	### CM Heterogeneity
120	
121	| Metric | Qwen2.5-7B | Llama3.1-8B |
122	|--------|-----------|------------|
123	| Δ_FPR (max-min) | 0.2414 | 0.2190 |
124	| Δ_FNR (max-min) | 0.1495 | 0.1290 |
125	| Mean Δ_error | 0.1955 | 0.1740 |
126	
127	### Bias Comparison
128	
129	| n_expert | Qwen |Bias|_Global | Qwen |Bias|_ECHTE | Qwen Δ|Bias| | Llama |Bias|_Global | Llama |Bias|_ECHTE | Llama Δ|Bias| |
130	|----------|------------------|--------------------|--------------|--------------------|--------------------|---------------|
131	| 200 | 0.0368 | 0.0275 | +0.0093 | 0.0365 | 0.0248 | +0.0117 |
132	| 500 | 0.0336 | 0.0196 | +0.0141 | 0.0314 | 0.0099 | +0.0215 |
133	| 1000 | 0.0328 | 0.0165 | +0.0162 | 0.0286 | 0.0130 | +0.0156 |
134	
135	### RMSE Comparison
136	
137	| n_expert | Qwen RMSE_Global | Qwen RMSE_ECHTE | Llama RMSE_Global | Llama RMSE_ECHTE |
138	|----------|-----------------|----------------|------------------|-----------------|
139	| 200 | 0.1546 | 0.2293 | 0.1780 | 0.2606 |
140	| 500 | 0.1362 | 0.1631 | 0.1580 | 0.1760 |
141	| 1000 | 0.1314 | 0.1393 | 0.1554 | 0.1602 |
142	
143	## Conclusion
144	
145	EC-HTE wins on |Bias| in 3/3 budget levels.
146	EC-HTE wins on RMSE in 0/3 budget levels.
147	
148	**Result: Under heterogeneous-τ DGP with Qwen2.5-7B CMs, EC-HTE consistently outperforms Global correction in bias.**
149	
150	**Cross-model consistency**: Llama EC-HTE wins on bias in 3/3 budgets; Qwen EC-HTE wins in 3/3 budgets.
151	EC-HTE's bias advantage is consistent across both Llama and Qwen models.
152	
153	Average Δ|Bias| (Global - EC-HTE): Qwen = +0.0132, Llama = +0.0163
154	Llama shows larger EC-HTE improvement despite smaller CM heterogeneity.
155	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "b1d94537-61a9-40a4-b4e9-e5a5ba8c3ec4"
}
```

</details>

---

### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3ce3846bb26060b4",
  "tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "description": "Finding /home/ubuntu/ec_hte_llm_annotation/artifacts/**/h…",
  "usage": {
    "total_tokens": 17902,
    "tool_uses": 2,
    "duration_ms": 2028
  },
  "last_tool_name": "Glob",
  "uuid": "52f7fe2f-2c85-45de-8a69-38d29cfe4426",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0"
}
```

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_01Bws39HK6CC2aDZ3ya8CRoh`</summary>

```json
{
  "pattern": "/home/ubuntu/ec_hte_llm_annotation/artifacts/**/hetero_tau_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "b7532d74-c159-43bf-91bf-399060d6ce67",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01E89GwEV9GajiFjkLTDCX7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17878,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17878,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 16 · 2026-05-22T00:15:04.777Z_

<details><summary>↩ Tool result · `toolu_01Bws39HK6CC2aDZ3ya8CRoh`</summary>

```text
artifacts/c1_multi_llm/hetero_tau_analysis.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "edcdea4e-2c50-4e51-b053-186a7991c6f7"
}
```

</details>

---

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3ce3846bb26060b4",
  "tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "description": "Running find /home/ubuntu/ec_hte_llm_annotation/artifacts…",
  "usage": {
    "total_tokens": 23368,
    "tool_uses": 3,
    "duration_ms": 4120
  },
  "last_tool_name": "Bash",
  "uuid": "32cd421b-1034-4202-be82-6916ee18f929",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0"
}
```

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01KQPMWNPZ3yHAwTMrASAn2T`</summary>

```json
{
  "command": "find /home/ubuntu/ec_hte_llm_annotation/artifacts -name \"*hetero_tau*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "30c592a0-bdb4-4594-825b-845ff2138348",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Co3ACpwtBaJCwfT7wj57g1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5460,
      "cache_read_input_tokens": 17878,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5460,
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

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3ce3846bb26060b4",
  "tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "description": "Running ls -la /home/ubuntu/ec_hte_llm_annotation/artifac…",
  "usage": {
    "total_tokens": 23369,
    "tool_uses": 4,
    "duration_ms": 4312
  },
  "last_tool_name": "Bash",
  "uuid": "7fdc1aa0-1462-4d80-80f1-0e504bae25b7",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_01UpnE81bjMPNLqDxo93CrmU`</summary>

```json
{
  "command": "ls -la /home/ubuntu/ec_hte_llm_annotation/artifacts/exp-023/ 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "7b92d5d2-ac2e-418c-9be1-30d1fca00f65",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Co3ACpwtBaJCwfT7wj57g1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5460,
      "cache_read_input_tokens": 17878,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5460,
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

_source line 21 · 2026-05-22T00:15:07.081Z_

<details><summary>↩ Tool result · `toolu_01KQPMWNPZ3yHAwTMrASAn2T`</summary>

```text
/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/qwen_hetero_tau_results.csv
/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_hetero_tau.py
/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/qwen_hetero_tau_analysis.md
/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_qwen_hetero_tau.py
/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/hetero_tau_results.csv
/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/hetero_tau_analysis.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "09bc1871-131c-41be-8f76-cf36e24fe602"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T00:15:07.126Z_

<details><summary>↩ Tool result · `toolu_01UpnE81bjMPNLqDxo93CrmU`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "c7039926-8bb2-4b7b-9e28-fe128bd4e6d7"
}
```

</details>

---

### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3ce3846bb26060b4",
  "tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "description": "Reading artifacts/c1_multi_llm/hetero_tau_analysis.md",
  "usage": {
    "total_tokens": 23834,
    "tool_uses": 5,
    "duration_ms": 5883
  },
  "last_tool_name": "Read",
  "uuid": "4fb818c6-564d-47da-b93a-df10783629c7",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0"
}
```

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01XUZf5qbvGKVGcJKSoMxU1W`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/hetero_tau_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "0106da07-4f62-4fc1-b018-97ca7aed213d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VMMDDepcs31Cb3f4zRby64",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 23338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 463,
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

_source line 25 · 2026-05-22T00:15:08.624Z_

<details><summary>↩ Tool result · `toolu_01XUZf5qbvGKVGcJKSoMxU1W`</summary>

```text
1	# Heterogeneous-τ DGP: EC-HTE vs Global Correction
2	
3	## Design
4	
5	- N=5000, P(Z=1)=0.652, K=4 subgroups
6	- **Heterogeneous τ(z) across subgroups:**
7	  - False_medium: τ(z=0)=0.45, τ(z=1)=0.55, Δτ=0.1
8	  - False_short: τ(z=0)=0.4, τ(z=1)=0.5, Δτ=0.1
9	  - True_medium: τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3
10	  - True_short: τ(z=0)=0.2, τ(z=1)=0.8, Δτ=0.6
11	- n_expert sweep: [200, 500, 1000]
12	- 50 MC seeds per budget
13	- HB method: MAP-EB (Gamma(3,1) prior)
14	- |Bias| = avg across cells of |mean(bias) across seeds|
15	- RMSE = avg across cells of sqrt(mean(bias²) across seeds)
16	
17	## Summary Table (averaged across all cells)
18	
19	| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |
20	|----------|--------|-------|------|----------|----------|
21	| 200 | Naive | 0.0643 | 0.1141 | 0.858 | 0.335 |
22	| 200 | Global | 0.0365 | 0.1780 | 0.887 | 0.590 |
23	| 200 | Strat MLE | 0.0179 | 0.2561 | 0.800 | 0.646 |
24	| 200 | HB EC-HTE | 0.0248 | 0.2606 | 0.795 | 0.655 |
25	|----------|--------|-------|------|----------|----------|
26	| 500 | Naive | 0.0643 | 0.1141 | 0.858 | 0.335 |
27	| 500 | Global | 0.0314 | 0.1580 | 0.915 | 0.574 |
28	| 500 | Strat MLE | 0.0085 | 0.1750 | 0.900 | 0.576 |
29	| 500 | HB EC-HTE | 0.0099 | 0.1760 | 0.895 | 0.579 |
30	|----------|--------|-------|------|----------|----------|
31	| 1000 | Naive | 0.0643 | 0.1141 | 0.858 | 0.335 |
32	| 1000 | Global | 0.0286 | 0.1554 | 0.927 | 0.566 |
33	| 1000 | Strat MLE | 0.0131 | 0.1597 | 0.912 | 0.553 |
34	| 1000 | HB EC-HTE | 0.0130 | 0.1602 | 0.912 | 0.554 |
35	|----------|--------|-------|------|----------|----------|
36	
37	## EC-HTE vs Global Comparison
38	
39	| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |
40	|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|
41	| 200 | 0.0365 | 0.0248 | +0.0117 | 0.1780 | 0.2606 | -0.0826 | **YES** | no |
42	| 500 | 0.0314 | 0.0099 | +0.0215 | 0.1580 | 0.1760 | -0.0180 | **YES** | no |
43	| 1000 | 0.0286 | 0.0130 | +0.0156 | 0.1554 | 0.1602 | -0.0048 | **YES** | no |
44	
45	## Per-Subgroup Breakdown
46	
47	### n_expert = 200
48	
49	| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
50	|----------|-----|---|-------------|-------------|-------------|-------------|------------|
51	| False_medium | 0.1 | 0 | 0.0135 | 0.0119 | +0.0016 | 0.1837 | 0.3011 |
52	| False_medium | 0.1 | 1 | 0.0083 | 0.0165 | -0.0082 | 0.0966 | 0.1544 |
53	| False_short | 0.1 | 0 | 0.0390 | 0.0090 | +0.0301 | 0.1996 | 0.3353 |
54	| False_short | 0.1 | 1 | 0.0104 | 0.0163 | -0.0059 | 0.1239 | 0.1937 |
55	| True_medium | 0.3 | 0 | 0.0044 | 0.0228 | -0.0185 | 0.2260 | 0.3332 |
56	| True_medium | 0.3 | 1 | 0.0218 | 0.0531 | -0.0313 | 0.1418 | 0.2161 |
57	| True_short | 0.6 | 0 | 0.1177 | 0.0351 | +0.0826 | 0.2691 | 0.3307 |
58	| True_short | 0.6 | 1 | 0.0771 | 0.0340 | +0.0431 | 0.1832 | 0.2204 |
59	
60	### n_expert = 500
61	
62	| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
63	|----------|-----|---|-------------|-------------|-------------|-------------|------------|
64	| False_medium | 0.1 | 0 | 0.0089 | 0.0058 | +0.0031 | 0.1407 | 0.2082 |
65	| False_medium | 0.1 | 1 | 0.0043 | 0.0103 | -0.0060 | 0.0807 | 0.1062 |
66	| False_short | 0.1 | 0 | 0.0417 | 0.0138 | +0.0279 | 0.1978 | 0.2307 |
67	| False_short | 0.1 | 1 | 0.0062 | 0.0031 | +0.0030 | 0.1137 | 0.1359 |
68	| True_medium | 0.3 | 0 | 0.0006 | 0.0131 | -0.0124 | 0.1893 | 0.2035 |
69	| True_medium | 0.3 | 1 | 0.0144 | 0.0245 | -0.0101 | 0.1131 | 0.1235 |
70	| True_short | 0.6 | 0 | 0.1117 | 0.0022 | +0.1095 | 0.2567 | 0.2253 |
71	| True_short | 0.6 | 1 | 0.0636 | 0.0063 | +0.0574 | 0.1717 | 0.1745 |
72	
73	### n_expert = 1000
74	
75	| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
76	|----------|-----|---|-------------|-------------|-------------|-------------|------------|
77	| False_medium | 0.1 | 0 | 0.0138 | 0.0054 | +0.0084 | 0.1278 | 0.1601 |
78	| False_medium | 0.1 | 1 | 0.0002 | 0.0017 | -0.0015 | 0.0750 | 0.0827 |
79	| False_short | 0.1 | 0 | 0.0358 | 0.0260 | +0.0098 | 0.1974 | 0.2054 |
80	| False_short | 0.1 | 1 | 0.0028 | 0.0049 | -0.0021 | 0.1101 | 0.1262 |
81	| True_medium | 0.3 | 0 | 0.0094 | 0.0059 | +0.0035 | 0.1902 | 0.2032 |
82	| True_medium | 0.3 | 1 | 0.0093 | 0.0224 | -0.0132 | 0.1154 | 0.1281 |
83	| True_short | 0.6 | 0 | 0.1020 | 0.0274 | +0.0745 | 0.2577 | 0.2117 |
84	| True_short | 0.6 | 1 | 0.0554 | 0.0103 | +0.0452 | 0.1693 | 0.1637 |
85	
86	## Bias-Variance Decomposition
87	
88	| n_expert | Method | Bias² | Variance | MSE |
89	|----------|--------|-------|----------|-----|
90	| 200 | Naive | 0.0077 | 0.0081 | 0.0158 |
91	| 200 | Global | 0.0028 | 0.0323 | 0.0351 |
92	| 200 | Strat MLE | 0.0005 | 0.0709 | 0.0714 |
93	| 200 | HB EC-HTE | 0.0008 | 0.0732 | 0.0740 |
94	| 500 | Naive | 0.0077 | 0.0081 | 0.0158 |
95	| 500 | Global | 0.0023 | 0.0260 | 0.0283 |
96	| 500 | Strat MLE | 0.0001 | 0.0332 | 0.0333 |
97	| 500 | HB EC-HTE | 0.0001 | 0.0336 | 0.0337 |
98	| 1000 | Naive | 0.0077 | 0.0081 | 0.0158 |
99	| 1000 | Global | 0.0019 | 0.0258 | 0.0277 |
100	| 1000 | Strat MLE | 0.0003 | 0.0276 | 0.0279 |
101	| 1000 | HB EC-HTE | 0.0003 | 0.0278 | 0.0280 |
102	
103	## Comparison with Constant-τ DGP
104	
105	Under **constant τ** (τ(z=0)=0.35, τ(z=1)=0.65 for all subgroups),
106	Global correction uses a pooled CM that is correct *on average*.
107	Since all subgroups share the same Δτ, Global's pooled correction is unbiased.
108	
109	Under **heterogeneous τ**, Global's pooled CM applies a single correction
110	factor to all subgroups, but the true Δτ varies from 0.1 (False_medium/short)
111	to 0.6 (True_short). The correction's bias = δ_s × Δτ_s / (1−2π̄),
112	and since Global uses pooled δ instead of subgroup-specific δ_s,
113	it over-corrects subgroups with small Δτ and under-corrects those with large Δτ.
114	
115	## Conclusion
116	
117	EC-HTE wins on |Bias| in 3/3 budget levels.
118	EC-HTE wins on RMSE in 0/3 budget levels.
119	
120	**Result: Under heterogeneous-τ DGP, EC-HTE consistently outperforms Global correction in bias.**
121	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "9a286a67-eb7e-4622-ae4e-f759d9b13915"
}
```

</details>

---

### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3ce3846bb26060b4",
  "tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "description": "Running ls -lh /home/ubuntu/ec_hte_llm_annotation/artifac…",
  "usage": {
    "total_tokens": 27512,
    "tool_uses": 6,
    "duration_ms": 8821
  },
  "last_tool_name": "Bash",
  "uuid": "90cab36d-ba6f-48db-802e-88ff2e47f481",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0"
}
```

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_016Jm2YvYu57gPfoP3oKoSbk`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/*.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "8070fee8-41c0-4f79-9fae-42cf04683708",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0158zq9ydC7QxEBbxbDd7ydY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3677,
      "cache_read_input_tokens": 23801,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3677,
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

_source line 28 · 2026-05-22T00:15:11.638Z_

<details><summary>↩ Tool result · `toolu_016Jm2YvYu57gPfoP3oKoSbk`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 6.1K May 21 21:50 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/all_models_analysis.md
-rw-r--r-- 1 ubuntu ubuntu 3.7K May 21 21:33 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/budget_sweep_k2_analysis.md
-rw-r--r-- 1 ubuntu ubuntu 1.9K May 21 21:08 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/budget_sweep_k4_analysis.md
-rw-r--r-- 1 ubuntu ubuntu  982 May 21 22:13 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/gemma_cm_profile.md
-rw-r--r-- 1 ubuntu ubuntu 4.5K May 21 22:13 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/gemma_sweep_analysis.md
-rw-r--r-- 1 ubuntu ubuntu 5.9K May 21 23:06 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/hetero_tau_analysis.md
-rw-r--r-- 1 ubuntu ubuntu 3.1K May 21 20:40 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_analysis.md
-rw-r--r-- 1 ubuntu ubuntu 5.0K May 21 20:51 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_semisynthetic_analysis.md
-rw-r--r-- 1 ubuntu ubuntu 1.2K May 21 22:13 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/mistral_cm_profile.md
-rw-r--r-- 1 ubuntu ubuntu 4.6K May 21 22:13 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/mistral_sweep_analysis.md
-rw-r--r-- 1 ubuntu ubuntu 1.5K May 21 21:54 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/qwen_cm_profile.md
-rw-r--r-- 1 ubuntu ubuntu 7.2K May 22 00:05 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/qwen_hetero_tau_analysis.md
-rw-r--r-- 1 ubuntu ubuntu 4.3K May 21 21:54 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/qwen_sweep_analysis.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "73862572-c58f-4fdd-803b-59d12ddb4dc8"
}
```

</details>

---

### System

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a3ce3846bb26060b4",
  "tool_use_id": "toolu_01WubYAsQYWHZYfDxaXfpR4a",
  "status": "completed",
  "output_file": "",
  "summary": "Find Qwen analysis and Llama results",
  "usage": {
    "total_tokens": 28535,
    "tool_uses": 6,
    "duration_ms": 51630
  },
  "uuid": "cc2b1e5a-7ccc-4d38-bb19-87ea29a6955e",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0"
}
```

---

### Tool result

_source line 30 · 2026-05-22T00:15:54.366Z_

<details><summary>↩ Tool result · `toolu_01WubYAsQYWHZYfDxaXfpR4a`</summary>

````text
I can see the naming pattern now. The `hetero_tau_analysis.md` appears to be the Llama analysis (since the Qwen one is specifically named `qwen_hetero_tau_analysis.md`). Let me verify this by checking the content of the generic hetero_tau_analysis.md file to confirm it mentions Llama.

Looking at the file I already read, I can see in the "Cross-Model Comparison" section (lines 117-154) of `qwen_hetero_tau_analysis.md` that it references both Qwen and Llama. This confirms that:

1. **`/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/qwen_hetero_tau_analysis.md`** - Qwen2.5-7B Heterogeneous-τ DGP analysis
2. **`/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/hetero_tau_analysis.md`** - Llama3.1-8B Heterogeneous-τ DGP analysis (this is the one used for cross-model comparison)

Here are the complete contents of both files:

---

## **File 1: Qwen Hetero-Tau Analysis**
**Path:** `/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/qwen_hetero_tau_analysis.md`

```markdown
# Qwen2.5-7B Heterogeneous-τ DGP: EC-HTE vs Global Correction

## Design

- N=5000, P(Z=1)=0.652, K=4 subgroups
- **LLM**: Qwen2.5-7B (balanced binarization)
- **Heterogeneous τ(z) across subgroups:**
  - False_medium: τ(z=0)=0.45, τ(z=1)=0.55, Δτ=0.1
  - False_short: τ(z=0)=0.4, τ(z=1)=0.5, Δτ=0.1
  - True_medium: τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3
  - True_short: τ(z=0)=0.2, τ(z=1)=0.8, Δτ=0.6
- n_expert sweep: [200, 500, 1000]
- 50 MC seeds per budget
- HB method: MAP-EB (Gamma(3,1) prior)
- |Bias| = avg across cells of |mean(bias) across seeds|
- RMSE = avg across cells of sqrt(mean(bias²) across seeds)

## Qwen2.5-7B Per-Subgroup Confusion Matrix

| Subgroup | π_s | FPR | FNR | 1-FPR-FNR |
|----------|-----|-----|-----|-----------|
| False_medium | 0.3816 | 0.1800 | 0.2874 | 0.5326 |
| False_short | 0.2224 | 0.2414 | 0.1750 | 0.5836 |
| True_medium | 0.2551 | 0.2333 | 0.2105 | 0.5562 |
| True_short | 0.1408 | 0.0000 | 0.1379 | 0.8621 |

- Qwen Δ_FPR = 0.2414, Δ_FNR = 0.1495
- Llama Δ_FPR = 0.2190, Δ_FNR = 0.1290
- Qwen has larger FPR heterogeneity and larger FNR heterogeneity than Llama

## Summary Table (averaged across all cells)

| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |
|----------|--------|-------|------|----------|----------|
| 200 | Naive | 0.0575 | 0.1060 | 0.900 | 0.334 |
| 200 | Global | 0.0368 | 0.1546 | 0.907 | 0.512 |
| 200 | Strat MLE | 0.0282 | 0.2288 | 0.800 | 0.548 |
| 200 | HB EC-HTE | 0.0275 | 0.2293 | 0.802 | 0.546 |
| 500 | Naive | 0.0575 | 0.1060 | 0.900 | 0.334 |
| 500 | Global | 0.0336 | 0.1362 | 0.938 | 0.501 |
| 500 | Strat MLE | 0.0215 | 0.1639 | 0.875 | 0.498 |
| 500 | HB EC-HTE | 0.0196 | 0.1631 | 0.873 | 0.495 |
| 1000 | Naive | 0.0575 | 0.1060 | 0.900 | 0.334 |
| 1000 | Global | 0.0328 | 0.1314 | 0.940 | 0.496 |
| 1000 | Strat MLE | 0.0181 | 0.1399 | 0.905 | 0.481 |
| 1000 | HB EC-HTE | 0.0165 | 0.1393 | 0.902 | 0.480 |

## EC-HTE vs Global Comparison

| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |
|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|
| 200 | 0.0368 | 0.0275 | +0.0093 | 0.1546 | 0.2293 | -0.0747 | **YES** | no |
| 500 | 0.0336 | 0.0196 | +0.0141 | 0.1362 | 0.1631 | -0.0269 | **YES** | no |
| 1000 | 0.0328 | 0.0165 | +0.0162 | 0.1314 | 0.1393 | -0.0079 | **YES** | no |

## Per-Subgroup Breakdown

### n_expert = 200

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| False_medium | 0.1 | 0 | 0.0175 | 0.0252 | -0.0077 | 0.1639 | 0.2191 |
| False_medium | 0.1 | 1 | 0.0082 | 0.0284 | -0.0202 | 0.0905 | 0.1183 |
| False_short | 0.1 | 0 | 0.0032 | 0.0225 | -0.0193 | 0.2131 | 0.3422 |
| False_short | 0.1 | 1 | 0.0069 | 0.0063 | +0.0007 | 0.1158 | 0.1807 |
| True_medium | 0.3 | 0 | 0.0545 | 0.0669 | -0.0124 | 0.1786 | 0.2636 |
| True_medium | 0.3 | 1 | 0.0106 | 0.0033 | +0.0073 | 0.0934 | 0.1514 |
| True_short | 0.6 | 0 | 0.1156 | 0.0406 | +0.0750 | 0.2193 | 0.3421 |
| True_short | 0.6 | 1 | 0.0780 | 0.0268 | +0.0512 | 0.1619 | 0.2168 |

### n_expert = 500

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| False_medium | 0.1 | 0 | 0.0156 | 0.0074 | +0.0082 | 0.1348 | 0.1767 |
| False_medium | 0.1 | 1 | 0.0031 | 0.0141 | -0.0110 | 0.0777 | 0.0945 |
| False_short | 0.1 | 0 | 0.0002 | 0.0201 | -0.0199 | 0.1854 | 0.2451 |
| False_short | 0.1 | 1 | 0.0114 | 0.0050 | +0.0064 | 0.1034 | 0.1353 |
| True_medium | 0.3 | 0 | 0.0580 | 0.0509 | +0.0070 | 0.1528 | 0.1938 |
| True_medium | 0.3 | 1 | 0.0177 | 0.0045 | +0.0132 | 0.0837 | 0.1091 |
| True_short | 0.6 | 0 | 0.1012 | 0.0395 | +0.0617 | 0.2031 | 0.2016 |
| True_short | 0.6 | 1 | 0.0621 | 0.0152 | +0.0469 | 0.1483 | 0.1486 |

### n_expert = 1000

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| False_medium | 0.1 | 0 | 0.0151 | 0.0087 | +0.0064 | 0.1299 | 0.1746 |
| False_medium | 0.1 | 1 | 0.0017 | 0.0024 | -0.0007 | 0.0715 | 0.0836 |
| False_short | 0.1 | 0 | 0.0019 | 0.0004 | +0.0015 | 0.1758 | 0.1900 |
| False_short | 0.1 | 1 | 0.0123 | 0.0053 | +0.0070 | 0.1020 | 0.1139 |
| True_medium | 0.3 | 0 | 0.0576 | 0.0395 | +0.0181 | 0.1480 | 0.1621 |
| True_medium | 0.3 | 1 | 0.0195 | 0.0001 | +0.0194 | 0.0814 | 0.0896 |
| True_short | 0.6 | 0 | 0.0971 | 0.0497 | +0.0474 | 0.1980 | 0.1679 |
| True_short | 0.6 | 1 | 0.0571 | 0.0262 | +0.0309 | 0.1443 | 0.1325 |

## Bias-Variance Decomposition

| n_expert | Method | Bias² | Variance | MSE |
|----------|--------|-------|----------|-----|
| 200 | Naive | 0.0059 | 0.0072 | 0.0131 |
| 200 | Global | 0.0029 | 0.0237 | 0.0266 |
| 200 | Strat MLE | 0.0013 | 0.0582 | 0.0595 |
| 200 | HB EC-HTE | 0.0011 | 0.0586 | 0.0597 |
| 500 | Naive | 0.0059 | 0.0072 | 0.0131 |
| 500 | Global | 0.0023 | 0.0185 | 0.0207 |
| 500 | Strat MLE | 0.0008 | 0.0290 | 0.0298 |
| 500 | HB EC-HTE | 0.0006 | 0.0288 | 0.0294 |
| 1000 | Naive | 0.0059 | 0.0072 | 0.0131 |
| 1000 | Global | 0.0021 | 0.0172 | 0.0193 |
| 1000 | Strat MLE | 0.0007 | 0.0208 | 0.0214 |
| 1000 | HB EC-HTE | 0.0006 | 0.0206 | 0.0212 |

## Cross-Model Comparison: Qwen vs Llama (exp-023)

### CM Heterogeneity

| Metric | Qwen2.5-7B | Llama3.1-8B |
|--------|-----------|------------|
| Δ_FPR (max-min) | 0.2414 | 0.2190 |
| Δ_FNR (max-min) | 0.1495 | 0.1290 |
| Mean Δ_error | 0.1955 | 0.1740 |

### Bias Comparison

| n_expert | Qwen |Bias|_Global | Qwen |Bias|_ECHTE | Qwen Δ|Bias| | Llama |Bias|_Global | Llama |Bias|_ECHTE | Llama Δ|Bias| |
|----------|------------------|--------------------|--------------|--------------------|--------------------|---------------|
| 200 | 0.0368 | 0.0275 | +0.0093 | 0.0365 | 0.0248 | +0.0117 |
| 500 | 0.0336 | 0.0196 | +0.0141 | 0.0314 | 0.0099 | +0.0215 |
| 1000 | 0.0328 | 0.0165 | +0.0162 | 0.0286 | 0.0130 | +0.0156 |

### RMSE Comparison

| n_expert | Qwen RMSE_Global | Qwen RMSE_ECHTE | Llama RMSE_Global | Llama RMSE_ECHTE |
|----------|-----------------|----------------|------------------|-----------------|
| 200 | 0.1546 | 0.2293 | 0.1780 | 0.2606 |
| 500 | 0.1362 | 0.1631 | 0.1580 | 0.1760 |
| 1000 | 0.1314 | 0.1393 | 0.1554 | 0.1602 |

## Conclusion

EC-HTE wins on |Bias| in 3/3 budget levels.
EC-HTE wins on RMSE in 0/3 budget levels.

**Result: Under heterogeneous-τ DGP with Qwen2.5-7B CMs, EC-HTE consistently outperforms Global correction in bias.**

**Cross-model consistency**: Llama EC-HTE wins on bias in 3/3 budgets; Qwen EC-HTE wins in 3/3 budgets.
EC-HTE's bias advantage is consistent across both Llama and Qwen models.

Average Δ|Bias| (Global - EC-HTE): Qwen = +0.0132, Llama = +0.0163
Llama shows larger EC-HTE improvement despite smaller CM heterogeneity.
```

---

## **File 2: Llama Hetero-Tau Analysis**
**Path:** `/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/hetero_tau_analysis.md`

```markdown
# Heterogeneous-τ DGP: EC-HTE vs Global Correction

## Design

- N=5000, P(Z=1)=0.652, K=4 subgroups
- **Heterogeneous τ(z) across subgroups:**
  - False_medium: τ(z=0)=0.45, τ(z=1)=0.55, Δτ=0.1
  - False_short: τ(z=0)=0.4, τ(z=1)=0.5, Δτ=0.1
  - True_medium: τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3
  - True_short: τ(z=0)=0.2, τ(z=1)=0.8, Δτ=0.6
- n_expert sweep: [200, 500, 1000]
- 50 MC seeds per budget
- HB method: MAP-EB (Gamma(3,1) prior)
- |Bias| = avg across cells of |mean(bias) across seeds|
- RMSE = avg across cells of sqrt(mean(bias²) across seeds)

## Summary Table (averaged across all cells)

| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |
|----------|--------|-------|------|----------|----------|
| 200 | Naive | 0.0643 | 0.1141 | 0.858 | 0.335 |
| 200 | Global | 0.0365 | 0.1780 | 0.887 | 0.590 |
| 200 | Strat MLE | 0.0179 | 0.2561 | 0.800 | 0.646 |
| 200 | HB EC-HTE | 0.0248 | 0.2606 | 0.795 | 0.655 |
| 500 | Naive | 0.0643 | 0.1141 | 0.858 | 0.335 |
| 500 | Global | 0.0314 | 0.1580 | 0.915 | 0.574 |
| 500 | Strat MLE | 0.0085 | 0.1750 | 0.900 | 0.576 |
| 500 | HB EC-HTE | 0.0099 | 0.1760 | 0.895 | 0.579 |
| 1000 | Naive | 0.0643 | 0.1141 | 0.858 | 0.335 |
| 1000 | Global | 0.0286 | 0.1554 | 0.927 | 0.566 |
| 1000 | Strat MLE | 0.0131 | 0.1597 | 0.912 | 0.553 |
| 1000 | HB EC-HTE | 0.0130 | 0.1602 | 0.912 | 0.554 |

## EC-HTE vs Global Comparison

| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |
|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|
| 200 | 0.0365 | 0.0248 | +0.0117 | 0.1780 | 0.2606 | -0.0826 | **YES** | no |
| 500 | 0.0314 | 0.0099 | +0.0215 | 0.1580 | 0.1760 | -0.0180 | **YES** | no |
| 1000 | 0.0286 | 0.0130 | +0.0156 | 0.1554 | 0.1602 | -0.0048 | **YES** | no |

## Per-Subgroup Breakdown

### n_expert = 200

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| False_medium | 0.1 | 0 | 0.0135 | 0.0119 | +0.0016 | 0.1837 | 0.3011 |
| False_medium | 0.1 | 1 | 0.0083 | 0.0165 | -0.0082 | 0.0966 | 0.1544 |
| False_short | 0.1 | 0 | 0.0390 | 0.0090 | +0.0301 | 0.1996 | 0.3353 |
| False_short | 0.1 | 1 | 0.0104 | 0.0163 | -0.0059 | 0.1239 | 0.1937 |
| True_medium | 0.3 | 0 | 0.0044 | 0.0228 | -0.0185 | 0.2260 | 0.3332 |
| True_medium | 0.3 | 1 | 0.0218 | 0.0531 | -0.0313 | 0.1418 | 0.2161 |
| True_short | 0.6 | 0 | 0.1177 | 0.0351 | +0.0826 | 0.2691 | 0.3307 |
| True_short | 0.6 | 1 | 0.0771 | 0.0340 | +0.0431 | 0.1832 | 0.2204 |

### n_expert = 500

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| False_medium | 0.1 | 0 | 0.0089 | 0.0058 | +0.0031 | 0.1407 | 0.2082 |
| False_medium | 0.1 | 1 | 0.0043 | 0.0103 | -0.0060 | 0.0807 | 0.1062 |
| False_short | 0.1 | 0 | 0.0417 | 0.0138 | +0.0279 | 0.1978 | 0.2307 |
| False_short | 0.1 | 1 | 0.0062 | 0.0031 | +0.0030 | 0.1137 | 0.1359 |
| True_medium | 0.3 | 0 | 0.0006 | 0.0131 | -0.0124 | 0.1893 | 0.2035 |
| True_medium | 0.3 | 1 | 0.0144 | 0.0245 | -0.0101 | 0.1131 | 0.1235 |
| True_short | 0.6 | 0 | 0.1117 | 0.0022 | +0.1095 | 0.2567 | 0.2253 |
| True_short | 0.6 | 1 | 0.0636 | 0.0063 | +0.0574 | 0.1717 | 0.1745 |

### n_expert = 1000

| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
|----------|-----|---|-------------|-------------|-------------|-------------|------------|
| False_medium | 0.1 | 0 | 0.0138 | 0.0054 | +0.0084 | 0.1278 | 0.1601 |
| False_medium | 0.1 | 1 | 0.0002 | 0.0017 | -0.0015 | 0.0750 | 0.0827 |
| False_short | 0.1 | 0 | 0.0358 | 0.0260 | +0.0098 | 0.1974 | 0.2054 |
| False_short | 0.1 | 1 | 0.0028 | 0.0049 | -0.0021 | 0.1101 | 0.1262 |
| True_medium | 0.3 | 0 | 0.0094 | 0.0059 | +0.0035 | 0.1902 | 0.2032 |
| True_medium | 0.3 | 1 | 0.0093 | 0.0224 | -0.0132 | 0.1154 | 0.1281 |
| True_short | 0.6 | 0 | 0.1020 | 0.0274 | +0.0745 | 0.2577 | 0.2117 |
| True_short | 0.6 | 1 | 0.0554 | 0.0103 | +0.0452 | 0.1693 | 0.1637 |

## Bias-Variance Decomposition

| n_expert | Method | Bias² | Variance | MSE |
|----------|--------|-------|----------|-----|
| 200 | Naive | 0.0077 | 0.0081 | 0.0158 |
| 200 | Global | 0.0028 | 0.0323 | 0.0351 |
| 200 | Strat MLE | 0.0005 | 0.0709 | 0.0714 |
| 200 | HB EC-HTE | 0.0008 | 0.0732 | 0.0740 |
| 500 | Naive | 0.0077 | 0.0081 | 0.0158 |
| 500 | Global | 0.0023 | 0.0260 | 0.0283 |
| 500 | Strat MLE | 0.0001 | 0.0332 | 0.0333 |
| 500 | HB EC-HTE | 0.0001 | 0.0336 | 0.0337 |
| 1000 | Naive | 0.0077 | 0.0081 | 0.0158 |
| 1000 | Global | 0.0019 | 0.0258 | 0.0277 |
| 1000 | Strat MLE | 0.0003 | 0.0276 | 0.0279 |
| 1000 | HB EC-HTE | 0.0003 | 0.0278 | 0.0280 |

## Comparison with Constant-τ DGP

Under **constant τ** (τ(z=0)=0.35, τ(z=1)=0.65 for all subgroups),
Global correction uses a pooled CM that is correct *on average*.
Since all subgroups share the same Δτ, Global's pooled correction is unbiased.

Under **heterogeneous τ**, Global's pooled CM applies a single correction
factor to all subgroups, but the true Δτ varies from 0.1 (False_medium/short)
to 0.6 (True_short). The correction's bias = δ_s × Δτ_s / (1−2π̄),
and since Global uses pooled δ instead of subgroup-specific δ_s,
it over-corrects subgroups with small Δτ and under-corrects those with large Δτ.

## Conclusion

EC-HTE wins on |Bias| in 3/3 budget levels.
EC-HTE wins on RMSE in 0/3 budget levels.

**Result: Under heterogeneous-τ DGP, EC-HTE consistently outperforms Global correction in bias.**
```

---

## Summary

I've located and retrieved both hetero_tau_analysis.md files for the cross-model comparison:

1. **Qwen analysis**: `/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/qwen_hetero_tau_analysis.md` (7.2 KB) - Includes explicit Qwen2.5-7B confusion matrix and cross-model comparison tables showing Qwen vs Llama performance.

2. **Llama analysis**: `/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/hetero_tau_analysis.md` (5.9 KB) - Base heterogeneous-τ DGP analysis (Llama3.1-8B).

Both files are ready for your Gemma cross-model comparison section. The Qwen file already includes a "Cross-Model Comparison: Qwen vs Llama" section with side-by-side bias and RMSE comparisons that you can use as a template for structuring the Gemma comparison.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "dae998a3-7220-4a31-81f8-e2567a116456",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Find the Qwen hetero_tau_analysis.md and Llama hetero_tau_analysis.md files used in the cross-model comparison. Look in:\n1. /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/qwen_hetero_tau_analysis.md\n2. /home/ubuntu/ec_hte_llm_annotation/artifacts/exp-023/ or similar directories for Llama hetero_tau_analysis.md\n\nRead both files and report back their full contents so I can use them for the Gemma cross-model comparison section.",
    "agentId": "a3ce3846bb26060b4",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "I can see the naming pattern now. The `hetero_tau_analysis.md` appears to be the Llama analysis (since the Qwen one is specifically named `qwen_hetero_tau_analysis.md`). Let me verify this by checking the content of the generic hetero_tau_analysis.md file to confirm it mentions Llama.\n\nLooking at the file I already read, I can see in the \"Cross-Model Comparison\" section (lines 117-154) of `qwen_hetero_tau_analysis.md` that it references both Qwen and Llama. This confirms that:\n\n1. **`/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/qwen_hetero_tau_analysis.md`** - Qwen2.5-7B Heterogeneous-τ DGP analysis\n2. **`/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/hetero_tau_analysis.md`** - Llama3.1-8B Heterogeneous-τ DGP analysis (this is the one used for cross-model comparison)\n\nHere are the complete contents of both files:\n\n---\n\n## **File 1: Qwen Hetero-Tau Analysis**\n**Path:** `/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/qwen_hetero_tau_analysis.md`\n\n```markdown\n# Qwen2.5-7B Heterogeneous-τ DGP: EC-HTE vs Global Correction\n\n## Design\n\n- N=5000, P(Z=1)=0.652, K=4 subgroups\n- **LLM**: Qwen2.5-7B (balanced binarization)\n- **Heterogeneous τ(z) across subgroups:**\n  - False_medium: τ(z=0)=0.45, τ(z=1)=0.55, Δτ=0.1\n  - False_short: τ(z=0)=0.4, τ(z=1)=0.5, Δτ=0.1\n  - True_medium: τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3\n  - True_short: τ(z=0)=0.2, τ(z=1)=0.8, Δτ=0.6\n- n_expert sweep: [200, 500, 1000]\n- 50 MC seeds per budget\n- HB method: MAP-EB (Gamma(3,1) prior)\n- |Bias| = avg across cells of |mean(bias) across seeds|\n- RMSE = avg across cells of sqrt(mean(bias²) across seeds)\n\n## Qwen2.5-7B Per-Subgroup Confusion Matrix\n\n| Subgroup | π_s | FPR | FNR | 1-FPR-FNR |\n|----------|-----|-----|-----|-----------|\n| False_medium | 0.3816 | 0.1800 | 0.2874 | 0.5326 |\n| False_short | 0.2224 | 0.2414 | 0.1750 | 0.5836 |\n| True_medium | 0.2551 | 0.2333 | 0.2105 | 0.5562 |\n| True_short | 0.1408 | 0.0000 | 0.1379 | 0.8621 |\n\n- Qwen Δ_FPR = 0.2414, Δ_FNR = 0.1495\n- Llama Δ_FPR = 0.2190, Δ_FNR = 0.1290\n- Qwen has larger FPR heterogeneity and larger FNR heterogeneity than Llama\n\n## Summary Table (averaged across all cells)\n\n| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |\n|----------|--------|-------|------|----------|----------|\n| 200 | Naive | 0.0575 | 0.1060 | 0.900 | 0.334 |\n| 200 | Global | 0.0368 | 0.1546 | 0.907 | 0.512 |\n| 200 | Strat MLE | 0.0282 | 0.2288 | 0.800 | 0.548 |\n| 200 | HB EC-HTE | 0.0275 | 0.2293 | 0.802 | 0.546 |\n| 500 | Naive | 0.0575 | 0.1060 | 0.900 | 0.334 |\n| 500 | Global | 0.0336 | 0.1362 | 0.938 | 0.501 |\n| 500 | Strat MLE | 0.0215 | 0.1639 | 0.875 | 0.498 |\n| 500 | HB EC-HTE | 0.0196 | 0.1631 | 0.873 | 0.495 |\n| 1000 | Naive | 0.0575 | 0.1060 | 0.900 | 0.334 |\n| 1000 | Global | 0.0328 | 0.1314 | 0.940 | 0.496 |\n| 1000 | Strat MLE | 0.0181 | 0.1399 | 0.905 | 0.481 |\n| 1000 | HB EC-HTE | 0.0165 | 0.1393 | 0.902 | 0.480 |\n\n## EC-HTE vs Global Comparison\n\n| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |\n|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|\n| 200 | 0.0368 | 0.0275 | +0.0093 | 0.1546 | 0.2293 | -0.0747 | **YES** | no |\n| 500 | 0.0336 | 0.0196 | +0.0141 | 0.1362 | 0.1631 | -0.0269 | **YES** | no |\n| 1000 | 0.0328 | 0.0165 | +0.0162 | 0.1314 | 0.1393 | -0.0079 | **YES** | no |\n\n## Per-Subgroup Breakdown\n\n### n_expert = 200\n\n| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |\n|----------|-----|---|-------------|-------------|-------------|-------------|------------|\n| False_medium | 0.1 | 0 | 0.0175 | 0.0252 | -0.0077 | 0.1639 | 0.2191 |\n| False_medium | 0.1 | 1 | 0.0082 | 0.0284 | -0.0202 | 0.0905 | 0.1183 |\n| False_short | 0.1 | 0 | 0.0032 | 0.0225 | -0.0193 | 0.2131 | 0.3422 |\n| False_short | 0.1 | 1 | 0.0069 | 0.0063 | +0.0007 | 0.1158 | 0.1807 |\n| True_medium | 0.3 | 0 | 0.0545 | 0.0669 | -0.0124 | 0.1786 | 0.2636 |\n| True_medium | 0.3 | 1 | 0.0106 | 0.0033 | +0.0073 | 0.0934 | 0.1514 |\n| True_short | 0.6 | 0 | 0.1156 | 0.0406 | +0.0750 | 0.2193 | 0.3421 |\n| True_short | 0.6 | 1 | 0.0780 | 0.0268 | +0.0512 | 0.1619 | 0.2168 |\n\n### n_expert = 500\n\n| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |\n|----------|-----|---|-------------|-------------|-------------|-------------|------------|\n| False_medium | 0.1 | 0 | 0.0156 | 0.0074 | +0.0082 | 0.1348 | 0.1767 |\n| False_medium | 0.1 | 1 | 0.0031 | 0.0141 | -0.0110 | 0.0777 | 0.0945 |\n| False_short | 0.1 | 0 | 0.0002 | 0.0201 | -0.0199 | 0.1854 | 0.2451 |\n| False_short | 0.1 | 1 | 0.0114 | 0.0050 | +0.0064 | 0.1034 | 0.1353 |\n| True_medium | 0.3 | 0 | 0.0580 | 0.0509 | +0.0070 | 0.1528 | 0.1938 |\n| True_medium | 0.3 | 1 | 0.0177 | 0.0045 | +0.0132 | 0.0837 | 0.1091 |\n| True_short | 0.6 | 0 | 0.1012 | 0.0395 | +0.0617 | 0.2031 | 0.2016 |\n| True_short | 0.6 | 1 | 0.0621 | 0.0152 | +0.0469 | 0.1483 | 0.1486 |\n\n### n_expert = 1000\n\n| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |\n|----------|-----|---|-------------|-------------|-------------|-------------|------------|\n| False_medium | 0.1 | 0 | 0.0151 | 0.0087 | +0.0064 | 0.1299 | 0.1746 |\n| False_medium | 0.1 | 1 | 0.0017 | 0.0024 | -0.0007 | 0.0715 | 0.0836 |\n| False_short | 0.1 | 0 | 0.0019 | 0.0004 | +0.0015 | 0.1758 | 0.1900 |\n| False_short | 0.1 | 1 | 0.0123 | 0.0053 | +0.0070 | 0.1020 | 0.1139 |\n| True_medium | 0.3 | 0 | 0.0576 | 0.0395 | +0.0181 | 0.1480 | 0.1621 |\n| True_medium | 0.3 | 1 | 0.0195 | 0.0001 | +0.0194 | 0.0814 | 0.0896 |\n| True_short | 0.6 | 0 | 0.0971 | 0.0497 | +0.0474 | 0.1980 | 0.1679 |\n| True_short | 0.6 | 1 | 0.0571 | 0.0262 | +0.0309 | 0.1443 | 0.1325 |\n\n## Bias-Variance Decomposition\n\n| n_expert | Method | Bias² | Variance | MSE |\n|----------|--------|-------|----------|-----|\n| 200 | Naive | 0.0059 | 0.0072 | 0.0131 |\n| 200 | Global | 0.0029 | 0.0237 | 0.0266 |\n| 200 | Strat MLE | 0.0013 | 0.0582 | 0.0595 |\n| 200 | HB EC-HTE | 0.0011 | 0.0586 | 0.0597 |\n| 500 | Naive | 0.0059 | 0.0072 | 0.0131 |\n| 500 | Global | 0.0023 | 0.0185 | 0.0207 |\n| 500 | Strat MLE | 0.0008 | 0.0290 | 0.0298 |\n| 500 | HB EC-HTE | 0.0006 | 0.0288 | 0.0294 |\n| 1000 | Naive | 0.0059 | 0.0072 | 0.0131 |\n| 1000 | Global | 0.0021 | 0.0172 | 0.0193 |\n| 1000 | Strat MLE | 0.0007 | 0.0208 | 0.0214 |\n| 1000 | HB EC-HTE | 0.0006 | 0.0206 | 0.0212 |\n\n## Cross-Model Comparison: Qwen vs Llama (exp-023)\n\n### CM Heterogeneity\n\n| Metric | Qwen2.5-7B | Llama3.1-8B |\n|--------|-----------|------------|\n| Δ_FPR (max-min) | 0.2414 | 0.2190 |\n| Δ_FNR (max-min) | 0.1495 | 0.1290 |\n| Mean Δ_error | 0.1955 | 0.1740 |\n\n### Bias Comparison\n\n| n_expert | Qwen |Bias|_Global | Qwen |Bias|_ECHTE | Qwen Δ|Bias| | Llama |Bias|_Global | Llama |Bias|_ECHTE | Llama Δ|Bias| |\n|----------|------------------|--------------------|--------------|--------------------|--------------------|---------------|\n| 200 | 0.0368 | 0.0275 | +0.0093 | 0.0365 | 0.0248 | +0.0117 |\n| 500 | 0.0336 | 0.0196 | +0.0141 | 0.0314 | 0.0099 | +0.0215 |\n| 1000 | 0.0328 | 0.0165 | +0.0162 | 0.0286 | 0.0130 | +0.0156 |\n\n### RMSE Comparison\n\n| n_expert | Qwen RMSE_Global | Qwen RMSE_ECHTE | Llama RMSE_Global | Llama RMSE_ECHTE |\n|----------|-----------------|----------------|------------------|-----------------|\n| 200 | 0.1546 | 0.2293 | 0.1780 | 0.2606 |\n| 500 | 0.1362 | 0.1631 | 0.1580 | 0.1760 |\n| 1000 | 0.1314 | 0.1393 | 0.1554 | 0.1602 |\n\n## Conclusion\n\nEC-HTE wins on |Bias| in 3/3 budget levels.\nEC-HTE wins on RMSE in 0/3 budget levels.\n\n**Result: Under heterogeneous-τ DGP with Qwen2.5-7B CMs, EC-HTE consistently outperforms Global correction in bias.**\n\n**Cross-model consistency**: Llama EC-HTE wins on bias in 3/3 budgets; Qwen EC-HTE wins in 3/3 budgets.\nEC-HTE's bias advantage is consistent across both Llama and Qwen models.\n\nAverage Δ|Bias| (Global - EC-HTE): Qwen = +0.0132, Llama = +0.0163\nLlama shows larger EC-HTE improvement despite smaller CM heterogeneity.\n```\n\n---\n\n## **File 2: Llama Hetero-Tau Analysis**\n**Path:** `/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/hetero_tau_analysis.md`\n\n```markdown\n# Heterogeneous-τ DGP: EC-HTE vs Global Correction\n\n## Design\n\n- N=5000, P(Z=1)=0.652, K=4 subgroups\n- **Heterogeneous τ(z) across subgroups:**\n  - False_medium: τ(z=0)=0.45, τ(z=1)=0.55, Δτ=0.1\n  - False_short: τ(z=0)=0.4, τ(z=1)=0.5, Δτ=0.1\n  - True_medium: τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3\n  - True_short: τ(z=0)=0.2, τ(z=1)=0.8, Δτ=0.6\n- n_expert sweep: [200, 500, 1000]\n- 50 MC seeds per budget\n- HB method: MAP-EB (Gamma(3,1) prior)\n- |Bias| = avg across cells of |mean(bias) across seeds|\n- RMSE = avg across cells of sqrt(mean(bias²) across seeds)\n\n## Summary Table (averaged across all cells)\n\n| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |\n|----------|--------|-------|------|----------|----------|\n| 200 | Naive | 0.0643 | 0.1141 | 0.858 | 0.335 |\n| 200 | Global | 0.0365 | 0.1780 | 0.887 | 0.590 |\n| 200 | Strat MLE | 0.0179 | 0.2561 | 0.800 | 0.646 |\n| 200 | HB EC-HTE | 0.0248 | 0.2606 | 0.795 | 0.655 |\n| 500 | Naive | 0.0643 | 0.1141 | 0.858 | 0.335 |\n| 500 | Global | 0.0314 | 0.1580 | 0.915 | 0.574 |\n| 500 | Strat MLE | 0.0085 | 0.1750 | 0.900 | 0.576 |\n| 500 | HB EC-HTE | 0.0099 | 0.1760 | 0.895 | 0.579 |\n| 1000 | Naive | 0.0643 | 0.1141 | 0.858 | 0.335 |\n| 1000 | Global | 0.0286 | 0.1554 | 0.927 | 0.566 |\n| 1000 | Strat MLE | 0.0131 | 0.1597 | 0.912 | 0.553 |\n| 1000 | HB EC-HTE | 0.0130 | 0.1602 | 0.912 | 0.554 |\n\n## EC-HTE vs Global Comparison\n\n| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |\n|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|\n| 200 | 0.0365 | 0.0248 | +0.0117 | 0.1780 | 0.2606 | -0.0826 | **YES** | no |\n| 500 | 0.0314 | 0.0099 | +0.0215 | 0.1580 | 0.1760 | -0.0180 | **YES** | no |\n| 1000 | 0.0286 | 0.0130 | +0.0156 | 0.1554 | 0.1602 | -0.0048 | **YES** | no |\n\n## Per-Subgroup Breakdown\n\n### n_expert = 200\n\n| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |\n|----------|-----|---|-------------|-------------|-------------|-------------|------------|\n| False_medium | 0.1 | 0 | 0.0135 | 0.0119 | +0.0016 | 0.1837 | 0.3011 |\n| False_medium | 0.1 | 1 | 0.0083 | 0.0165 | -0.0082 | 0.0966 | 0.1544 |\n| False_short | 0.1 | 0 | 0.0390 | 0.0090 | +0.0301 | 0.1996 | 0.3353 |\n| False_short | 0.1 | 1 | 0.0104 | 0.0163 | -0.0059 | 0.1239 | 0.1937 |\n| True_medium | 0.3 | 0 | 0.0044 | 0.0228 | -0.0185 | 0.2260 | 0.3332 |\n| True_medium | 0.3 | 1 | 0.0218 | 0.0531 | -0.0313 | 0.1418 | 0.2161 |\n| True_short | 0.6 | 0 | 0.1177 | 0.0351 | +0.0826 | 0.2691 | 0.3307 |\n| True_short | 0.6 | 1 | 0.0771 | 0.0340 | +0.0431 | 0.1832 | 0.2204 |\n\n### n_expert = 500\n\n| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |\n|----------|-----|---|-------------|-------------|-------------|-------------|------------|\n| False_medium | 0.1 | 0 | 0.0089 | 0.0058 | +0.0031 | 0.1407 | 0.2082 |\n| False_medium | 0.1 | 1 | 0.0043 | 0.0103 | -0.0060 | 0.0807 | 0.1062 |\n| False_short | 0.1 | 0 | 0.0417 | 0.0138 | +0.0279 | 0.1978 | 0.2307 |\n| False_short | 0.1 | 1 | 0.0062 | 0.0031 | +0.0030 | 0.1137 | 0.1359 |\n| True_medium | 0.3 | 0 | 0.0006 | 0.0131 | -0.0124 | 0.1893 | 0.2035 |\n| True_medium | 0.3 | 1 | 0.0144 | 0.0245 | -0.0101 | 0.1131 | 0.1235 |\n| True_short | 0.6 | 0 | 0.1117 | 0.0022 | +0.1095 | 0.2567 | 0.2253 |\n| True_short | 0.6 | 1 | 0.0636 | 0.0063 | +0.0574 | 0.1717 | 0.1745 |\n\n### n_expert = 1000\n\n| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |\n|----------|-----|---|-------------|-------------|-------------|-------------|------------|\n| False_medium | 0.1 | 0 | 0.0138 | 0.0054 | +0.0084 | 0.1278 | 0.1601 |\n| False_medium | 0.1 | 1 | 0.0002 | 0.0017 | -0.0015 | 0.0750 | 0.0827 |\n| False_short | 0.1 | 0 | 0.0358 | 0.0260 | +0.0098 | 0.1974 | 0.2054 |\n| False_short | 0.1 | 1 | 0.0028 | 0.0049 | -0.0021 | 0.1101 | 0.1262 |\n| True_medium | 0.3 | 0 | 0.0094 | 0.0059 | +0.0035 | 0.1902 | 0.2032 |\n| True_medium | 0.3 | 1 | 0.0093 | 0.0224 | -0.0132 | 0.1154 | 0.1281 |\n| True_short | 0.6 | 0 | 0.1020 | 0.0274 | +0.0745 | 0.2577 | 0.2117 |\n| True_short | 0.6 | 1 | 0.0554 | 0.0103 | +0.0452 | 0.1693 | 0.1637 |\n\n## Bias-Variance Decomposition\n\n| n_expert | Method | Bias² | Variance | MSE |\n|----------|--------|-------|----------|-----|\n| 200 | Naive | 0.0077 | 0.0081 | 0.0158 |\n| 200 | Global | 0.0028 | 0.0323 | 0.0351 |\n| 200 | Strat MLE | 0.0005 | 0.0709 | 0.0714 |\n| 200 | HB EC-HTE | 0.0008 | 0.0732 | 0.0740 |\n| 500 | Naive | 0.0077 | 0.0081 | 0.0158 |\n| 500 | Global | 0.0023 | 0.0260 | 0.0283 |\n| 500 | Strat MLE | 0.0001 | 0.0332 | 0.0333 |\n| 500 | HB EC-HTE | 0.0001 | 0.0336 | 0.0337 |\n| 1000 | Naive | 0.0077 | 0.0081 | 0.0158 |\n| 1000 | Global | 0.0019 | 0.0258 | 0.0277 |\n| 1000 | Strat MLE | 0.0003 | 0.0276 | 0.0279 |\n| 1000 | HB EC-HTE | 0.0003 | 0.0278 | 0.0280 |\n\n## Comparison with Constant-τ DGP\n\nUnder **constant τ** (τ(z=0)=0.35, τ(z=1)=0.65 for all subgroups),\nGlobal correction uses a pooled CM that is correct *on average*.\nSince all subgroups share the same Δτ, Global's pooled correction is unbiased.\n\nUnder **heterogeneous τ**, Global's pooled CM applies a single correction\nfactor to all subgroups, but the true Δτ varies from 0.1 (False_medium/short)\nto 0.6 (True_short). The correction's bias = δ_s × Δτ_s / (1−2π̄),\nand since Global uses pooled δ instead of subgroup-specific δ_s,\nit over-corrects subgroups with small Δτ and under-corrects those with large Δτ.\n\n## Conclusion\n\nEC-HTE wins on |Bias| in 3/3 budget levels.\nEC-HTE wins on RMSE in 0/3 budget levels.\n\n**Result: Under heterogeneous-τ DGP, EC-HTE consistently outperforms Global correction in bias.**\n```\n\n---\n\n## Summary\n\nI've located and retrieved both hetero_tau_analysis.md files for the cross-model comparison:\n\n1. **Qwen analysis**: `/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/qwen_hetero_tau_analysis.md` (7.2 KB) - Includes explicit Qwen2.5-7B confusion matrix and cross-model comparison tables showing Qwen vs Llama performance.\n\n2. **Llama analysis**: `/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/hetero_tau_analysis.md` (5.9 KB) - Base heterogeneous-τ DGP analysis (Llama3.1-8B).\n\nBoth files are ready for your Gemma cross-model comparison section. The Qwen file already includes a \"Cross-Model Comparison: Qwen vs Llama\" section with side-by-side bias and RMSE comparisons that you can use as a template for structuring the Gemma comparison."
      }
    ],
    "totalDurationMs": 51632,
    "totalTokens": 36386,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1022,
      "cache_read_input_tokens": 27478,
      "output_tokens": 7881,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1022
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 7881,
          "cache_read_input_tokens": 27478,
          "cache_creation_input_tokens": 1022,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1022,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 1,
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

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me create the Gemma version of the script. The key changes are:

1. Replace SUBGROUP_CM with Gemma's values
2. Update all text references from "Qwen" to "Gemma"
3. Add Qwen results to the cross-model comparison (alongside Llama)
4. Keep everything else identical

Let me create the Gemma script now.

Gemma-2-9B CM values:
- False_medium: FPR=0.1100, FNR=0.4368


- False_short: FPR=0.1379, FNR=0.3000
- True_medium: FPR=0.0333, FNR=0.2632
- True_short: FPR=0.0909, FNR=0.2069

I also need to add Qwen results for the cross-model comparison, similar to how the Qwen script includes Llama results. I'll set up both LLAMA_RESULTS and QWEN_RESULTS in the Gemma script, pulling the relevant metrics from the Qwen analysis.

Looking at the Qwen performance across different sample sizes, I can see the bias and RMSE metrics improve as n increases, with the echte variants showing better performance than the global measures. Now I'm ready to write out the full script with both model comparisons integrated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "d47e846a-cfd6-4c2b-96a0-ce63a24039f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NvLSZRTh5wPnNtwRsppASe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8166,
      "cache_read_input_tokens": 32033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8166
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

_source line 32_

Now I have all the context. Creating the Gemma script with only the CM parameters changed, plus updated cross-model comparison sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "d52e97c8-535a-434f-b58e-bcbf490a7efb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NvLSZRTh5wPnNtwRsppASe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8166,
      "cache_read_input_tokens": 32033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8166
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

_source line 33_

<details open><summary>🔧 Tool call — Write · `toolu_012VQvXdwvucyujcHiD3oRQf`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_gemma_hetero_tau.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nHeterogeneous-τ DGP experiment with Gemma-2-9B confusion matrices.\nMirrors run_hetero_tau.py (Llama) but uses Gemma per-subgroup FPR/FNR.\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.optimize import minimize_scalar\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT_LIST = [200, 500, 1000]\nN_MC = 50\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']\nSUBGROUP_WEIGHTS = np.array([0.3816, 0.2224, 0.2551, 0.1408])\nSUBGROUP_WEIGHTS = SUBGROUP_WEIGHTS / SUBGROUP_WEIGHTS.sum()\n\nSUBGROUP_CM = {\n    'False_medium': {'fpr': 0.1100, 'fnr': 0.4368},\n    'False_short':  {'fpr': 0.1379, 'fnr': 0.3000},\n    'True_medium':  {'fpr': 0.0333, 'fnr': 0.2632},\n    'True_short':   {'fpr': 0.0909, 'fnr': 0.2069},\n}\n\nSUBGROUP_TAU = {\n    'True_short':   {'tau_z0': 0.2,  'tau_z1': 0.8},\n    'True_medium':  {'tau_z0': 0.35, 'tau_z1': 0.65},\n    'False_short':  {'tau_z0': 0.4,  'tau_z1': 0.5},\n    'False_medium': {'tau_z0': 0.45, 'tau_z1': 0.55},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\n\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === MAP-EB ===\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):\n    hp_rate = 1.0 / hp_scale\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = hp_shape * hp_scale\n            continue\n\n        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):\n            nll = _dirmult_neg_ll(a, _cl)\n            if a < 1e-10:\n                return 1e10\n            log_prior = (_shape - 1.0) * np.log(a) - _rate * a\n            return nll - log_prior\n\n        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n_sz = counts[i, z, :].sum()\n            d = n_sz + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    return C, alpha_opt\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\n# === DGP (heterogeneous tau) ===\n\ndef generate_data(seed, n_expert):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(4):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.zeros(N)\n    for i, s in enumerate(SUBGROUP_LABELS):\n        s_mask = S_idx == i\n        tau_s = SUBGROUP_TAU[s]\n        tau_vals[s_mask] = np.where(Z[s_mask] == 1, tau_s['tau_z1'], tau_s['tau_z0'])\n\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb, _ = estimate_cm_hb_map_eb(counts, SUBGROUP_LABELS)\n\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n        tau_s = SUBGROUP_TAU[s_val]\n\n        for z_level in [0, 1]:\n            oracle_cate = tau_s['tau_z1'] if z_level == 1 else tau_s['tau_z0']\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_w_nv = 2 * 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'cate_est': th_nv, 'cate_true': oracle_cate,\n                'coverage': cov_nv, 'ci_width': ci_w_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_w_gc = 2 * 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'cate_est': th_gc, 'cate_true': oracle_cate,\n                'coverage': cov_gc, 'ci_width': ci_w_gc,\n            })\n\n            # Stratified MLE\n            ci_w_ml = 2 * 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'cate_est': th_ml, 'cate_true': oracle_cate,\n                'coverage': cov_ml, 'ci_width': ci_w_ml,\n            })\n\n            # HB EC-HTE (MAP-EB)\n            ci_w_hb = 2 * 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'cate_est': th_hb, 'cate_true': oracle_cate,\n                'coverage': cov_hb, 'ci_width': ci_w_hb,\n            })\n\n    return rows\n\n\n# === Aggregation ===\n\ndef compute_corrected_abs_bias(df):\n    cell_bias = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias']\n                 .mean().abs().reset_index(name='abs_mean_bias'))\n    return (cell_bias.groupby(['n_expert', 'method'])['abs_mean_bias']\n            .mean().reset_index(name='abs_bias'))\n\n\ndef compute_rmse(df):\n    cell_rmse = (df.assign(bias_sq=df['bias'] ** 2)\n                 .groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias_sq']\n                 .mean().apply(np.sqrt).reset_index(name='rmse'))\n    return (cell_rmse.groupby(['n_expert', 'method'])['rmse']\n            .mean().reset_index(name='rmse'))\n\n\ndef compute_coverage(df):\n    return (df.groupby(['n_expert', 'method'])['coverage']\n            .mean().reset_index(name='coverage'))\n\n\ndef compute_ci_width(df):\n    return (df.groupby(['n_expert', 'method'])['ci_width']\n            .mean().reset_index(name='ci_width'))\n\n\n# === Analysis Report ===\n\nLLAMA_RESULTS = {\n    200:  {'global_bias': 0.0365, 'echte_bias': 0.0248, 'global_rmse': 0.1780, 'echte_rmse': 0.2606},\n    500:  {'global_bias': 0.0314, 'echte_bias': 0.0099, 'global_rmse': 0.1580, 'echte_rmse': 0.1760},\n    1000: {'global_bias': 0.0286, 'echte_bias': 0.0130, 'global_rmse': 0.1554, 'echte_rmse': 0.1602},\n}\n\nLLAMA_CM = {\n    'False_medium': {'fpr': 0.235, 'fnr': 0.319},\n    'False_short':  {'fpr': 0.310, 'fnr': 0.212},\n    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},\n    'True_short':   {'fpr': 0.091, 'fnr': 0.190},\n}\n\nQWEN_RESULTS = {\n    200:  {'global_bias': 0.0368, 'echte_bias': 0.0275, 'global_rmse': 0.1546, 'echte_rmse': 0.2293},\n    500:  {'global_bias': 0.0336, 'echte_bias': 0.0196, 'global_rmse': 0.1362, 'echte_rmse': 0.1631},\n    1000: {'global_bias': 0.0328, 'echte_bias': 0.0165, 'global_rmse': 0.1314, 'echte_rmse': 0.1393},\n}\n\nQWEN_CM = {\n    'False_medium': {'fpr': 0.180, 'fnr': 0.287},\n    'False_short':  {'fpr': 0.241, 'fnr': 0.175},\n    'True_medium':  {'fpr': 0.233, 'fnr': 0.211},\n    'True_short':   {'fpr': 0.000, 'fnr': 0.138},\n}\n\n\ndef write_analysis(df_raw, outpath):\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse = compute_rmse(df_raw)\n    cov = compute_coverage(df_raw)\n    ciw = compute_ci_width(df_raw)\n\n    summary = abs_bias.merge(rmse, on=['n_expert', 'method']).merge(\n        cov, on=['n_expert', 'method']).merge(ciw, on=['n_expert', 'method'])\n\n    lines = []\n    lines.append(\"# Gemma-2-9B Heterogeneous-τ DGP: EC-HTE vs Global Correction\\n\")\n    lines.append(\"## Design\\n\")\n    lines.append(f\"- N={N}, P(Z=1)={P_Z1}, K=4 subgroups\")\n    lines.append(\"- **LLM**: Gemma-2-9B (balanced binarization)\")\n    lines.append(\"- **Heterogeneous τ(z) across subgroups:**\")\n    for s in SUBGROUP_LABELS:\n        t = SUBGROUP_TAU[s]\n        lines.append(f\"  - {s}: τ(z=0)={t['tau_z0']}, τ(z=1)={t['tau_z1']}, Δτ={t['tau_z1']-t['tau_z0']:.1f}\")\n    lines.append(f\"- n_expert sweep: {N_EXPERT_LIST}\")\n    lines.append(f\"- {N_MC} MC seeds per budget\")\n    lines.append(\"- HB method: MAP-EB (Gamma(3,1) prior)\")\n    lines.append(f\"- |Bias| = avg across cells of |mean(bias) across seeds|\")\n    lines.append(f\"- RMSE = avg across cells of sqrt(mean(bias²) across seeds)\")\n    lines.append(\"\")\n\n    # Gemma CM table\n    lines.append(\"## Gemma-2-9B Per-Subgroup Confusion Matrix\\n\")\n    lines.append(\"| Subgroup | π_s | FPR | FNR | 1-FPR-FNR |\")\n    lines.append(\"|----------|-----|-----|-----|-----------|\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        w = SUBGROUP_WEIGHTS[SUBGROUP_LABELS.index(s)]\n        lines.append(f\"| {s} | {w:.4f} | {cm['fpr']:.4f} | {cm['fnr']:.4f} | {1-cm['fpr']-cm['fnr']:.4f} |\")\n    lines.append(\"\")\n    gemma_fpr_range = max(cm['fpr'] for cm in SUBGROUP_CM.values()) - min(cm['fpr'] for cm in SUBGROUP_CM.values())\n    gemma_fnr_range = max(cm['fnr'] for cm in SUBGROUP_CM.values()) - min(cm['fnr'] for cm in SUBGROUP_CM.values())\n    llama_fpr_range = max(cm['fpr'] for cm in LLAMA_CM.values()) - min(cm['fpr'] for cm in LLAMA_CM.values())\n    llama_fnr_range = max(cm['fnr'] for cm in LLAMA_CM.values()) - min(cm['fnr'] for cm in LLAMA_CM.values())\n    qwen_fpr_range = max(cm['fpr'] for cm in QWEN_CM.values()) - min(cm['fpr'] for cm in QWEN_CM.values())\n    qwen_fnr_range = max(cm['fnr'] for cm in QWEN_CM.values()) - min(cm['fnr'] for cm in QWEN_CM.values())\n    lines.append(f\"- Gemma Δ_FPR = {gemma_fpr_range:.4f}, Δ_FNR = {gemma_fnr_range:.4f}\")\n    lines.append(f\"- Qwen Δ_FPR = {qwen_fpr_range:.4f}, Δ_FNR = {qwen_fnr_range:.4f}\")\n    lines.append(f\"- Llama Δ_FPR = {llama_fpr_range:.4f}, Δ_FNR = {llama_fnr_range:.4f}\")\n    lines.append(f\"- **Note**: Gemma has strong FNR>FPR asymmetry (False_medium FNR=0.437 most extreme)\")\n    lines.append(\"\")\n\n    # Summary table\n    lines.append(\"## Summary Table (averaged across all cells)\\n\")\n    lines.append(\"| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |\")\n    lines.append(\"|----------|--------|-------|------|----------|----------|\")\n\n    method_order = ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']\n    method_labels = {'naive': 'Naive', 'global_corrected': 'Global', 'stratified_mle': 'Strat MLE', 'hb_ec_hte': 'HB EC-HTE'}\n\n    for ne in N_EXPERT_LIST:\n        for m in method_order:\n            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n            if len(row) > 0:\n                r = row.iloc[0]\n                lines.append(f\"| {ne} | {method_labels[m]} | {r['abs_bias']:.4f} | {r['rmse']:.4f} | {r['coverage']:.3f} | {r['ci_width']:.3f} |\")\n        lines.append(\"|----------|--------|-------|------|----------|----------|\")\n    lines.append(\"\")\n\n    # EC-HTE vs Global comparison\n    lines.append(\"## EC-HTE vs Global Comparison\\n\")\n    lines.append(\"| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |\")\n    lines.append(\"|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|\")\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        gc = sub[sub['method'] == 'global_corrected'].iloc[0]\n        hb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]\n        d_bias = gc['abs_bias'] - hb['abs_bias']\n        d_rmse = gc['rmse'] - hb['rmse']\n        wb = \"**YES**\" if hb['abs_bias'] < gc['abs_bias'] else \"no\"\n        wr = \"**YES**\" if hb['rmse'] < gc['rmse'] else \"no\"\n        lines.append(f\"| {ne} | {gc['abs_bias']:.4f} | {hb['abs_bias']:.4f} | {d_bias:+.4f} | {gc['rmse']:.4f} | {hb['rmse']:.4f} | {d_rmse:+.4f} | {wb} | {wr} |\")\n    lines.append(\"\")\n\n    # Per-subgroup breakdown\n    lines.append(\"## Per-Subgroup Breakdown\\n\")\n    for ne in N_EXPERT_LIST:\n        lines.append(f\"### n_expert = {ne}\\n\")\n        lines.append(\"| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |\")\n        lines.append(\"|----------|-----|---|-------------|-------------|-------------|-------------|------------|\")\n        sub_df = df_raw[df_raw['n_expert'] == ne]\n        for s_val in SUBGROUP_LABELS:\n            dt = SUBGROUP_TAU[s_val]['tau_z1'] - SUBGROUP_TAU[s_val]['tau_z0']\n            for z_level in [0, 1]:\n                cell_gc = sub_df[(sub_df['method'] == 'global_corrected') & (sub_df['subgroup'] == s_val) & (sub_df['z_level'] == z_level)]\n                cell_hb = sub_df[(sub_df['method'] == 'hb_ec_hte') & (sub_df['subgroup'] == s_val) & (sub_df['z_level'] == z_level)]\n                bias_gc = abs(cell_gc['bias'].mean())\n                bias_hb = abs(cell_hb['bias'].mean())\n                rmse_gc = np.sqrt((cell_gc['bias'] ** 2).mean())\n                rmse_hb = np.sqrt((cell_hb['bias'] ** 2).mean())\n                imp = bias_gc - bias_hb\n                lines.append(f\"| {s_val} | {dt:.1f} | {z_level} | {bias_gc:.4f} | {bias_hb:.4f} | {imp:+.4f} | {rmse_gc:.4f} | {rmse_hb:.4f} |\")\n        lines.append(\"\")\n\n    # Bias-variance decomposition\n    lines.append(\"## Bias-Variance Decomposition\\n\")\n    lines.append(\"| n_expert | Method | Bias² | Variance | MSE |\")\n    lines.append(\"|----------|--------|-------|----------|-----|\")\n    for ne in N_EXPERT_LIST:\n        for m in method_order:\n            sub_df = df_raw[(df_raw['n_expert'] == ne) & (df_raw['method'] == m)]\n            cell_stats = (sub_df.groupby(['subgroup', 'z_level'])['bias']\n                          .agg(['mean', 'var', 'count']).reset_index())\n            mean_bias_sq = (cell_stats['mean'] ** 2).mean()\n            variance = cell_stats['var'].mean()\n            mse = mean_bias_sq + variance\n            lines.append(f\"| {ne} | {method_labels[m]} | {mean_bias_sq:.4f} | {variance:.4f} | {mse:.4f} |\")\n    lines.append(\"\")\n\n    # Cross-model comparison with Llama and Qwen\n    lines.append(\"## Cross-Model Comparison: Gemma vs Qwen vs Llama\\n\")\n    lines.append(\"### CM Heterogeneity\\n\")\n    lines.append(\"| Metric | Gemma-2-9B | Qwen2.5-7B | Llama3.1-8B |\")\n    lines.append(\"|--------|-----------|-----------|------------|\")\n    lines.append(f\"| Δ_FPR (max-min) | {gemma_fpr_range:.4f} | {qwen_fpr_range:.4f} | {llama_fpr_range:.4f} |\")\n    lines.append(f\"| Δ_FNR (max-min) | {gemma_fnr_range:.4f} | {qwen_fnr_range:.4f} | {llama_fnr_range:.4f} |\")\n    lines.append(f\"| Mean Δ_error | {(gemma_fpr_range+gemma_fnr_range)/2:.4f} | {(qwen_fpr_range+qwen_fnr_range)/2:.4f} | {(llama_fpr_range+llama_fnr_range)/2:.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Bias Comparison\\n\")\n    lines.append(\"| n_expert | Gemma |Bias|_Global | Gemma |Bias|_ECHTE | Gemma Δ|Bias| | Qwen |Bias|_Global | Qwen |Bias|_ECHTE | Qwen Δ|Bias| | Llama |Bias|_Global | Llama |Bias|_ECHTE | Llama Δ|Bias| |\")\n    lines.append(\"|----------|------------------|--------------------|--------------|--------------------|--------------------|--------------|--------------------|--------------------|--------------| \")\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        ggc = sub[sub['method'] == 'global_corrected'].iloc[0]\n        ghb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]\n        gd = ggc['abs_bias'] - ghb['abs_bias']\n        qr = QWEN_RESULTS[ne]\n        qd = qr['global_bias'] - qr['echte_bias']\n        lr = LLAMA_RESULTS[ne]\n        ld = lr['global_bias'] - lr['echte_bias']\n        lines.append(f\"| {ne} | {ggc['abs_bias']:.4f} | {ghb['abs_bias']:.4f} | {gd:+.4f} | {qr['global_bias']:.4f} | {qr['echte_bias']:.4f} | {qd:+.4f} | {lr['global_bias']:.4f} | {lr['echte_bias']:.4f} | {ld:+.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### RMSE Comparison\\n\")\n    lines.append(\"| n_expert | Gemma RMSE_Global | Gemma RMSE_ECHTE | Qwen RMSE_Global | Qwen RMSE_ECHTE | Llama RMSE_Global | Llama RMSE_ECHTE |\")\n    lines.append(\"|----------|-----------------|----------------|-----------------|----------------|------------------|-----------------|\")\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        ggc = sub[sub['method'] == 'global_corrected'].iloc[0]\n        ghb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]\n        qr = QWEN_RESULTS[ne]\n        lr = LLAMA_RESULTS[ne]\n        lines.append(f\"| {ne} | {ggc['rmse']:.4f} | {ghb['rmse']:.4f} | {qr['global_rmse']:.4f} | {qr['echte_rmse']:.4f} | {lr['global_rmse']:.4f} | {lr['echte_rmse']:.4f} |\")\n    lines.append(\"\")\n\n    # Conclusion\n    lines.append(\"## Conclusion\\n\")\n    gc_all = summary[summary['method'] == 'global_corrected']\n    hb_all = summary[summary['method'] == 'hb_ec_hte']\n    n_bias_wins = 0\n    n_rmse_wins = 0\n    for ne in N_EXPERT_LIST:\n        gc_row = gc_all[gc_all['n_expert'] == ne].iloc[0]\n        hb_row = hb_all[hb_all['n_expert'] == ne].iloc[0]\n        if hb_row['abs_bias'] < gc_row['abs_bias']:\n            n_bias_wins += 1\n        if hb_row['rmse'] < gc_row['rmse']:\n            n_rmse_wins += 1\n\n    lines.append(f\"EC-HTE wins on |Bias| in {n_bias_wins}/{len(N_EXPERT_LIST)} budget levels.\")\n    lines.append(f\"EC-HTE wins on RMSE in {n_rmse_wins}/{len(N_EXPERT_LIST)} budget levels.\\n\")\n\n    if n_bias_wins == len(N_EXPERT_LIST):\n        lines.append(\"**Result: Under heterogeneous-τ DGP with Gemma-2-9B CMs, EC-HTE consistently outperforms Global correction in bias.**\\n\")\n    elif n_bias_wins > 0:\n        lines.append(f\"**Result: Under heterogeneous-τ DGP with Gemma-2-9B CMs, EC-HTE outperforms Global in bias at {n_bias_wins} of {len(N_EXPERT_LIST)} budget levels.**\\n\")\n    else:\n        lines.append(\"**Result: EC-HTE does not outperform Global in bias under this DGP configuration with Gemma CMs.**\\n\")\n\n    # Cross-model conclusion\n    llama_bias_wins = sum(1 for ne in N_EXPERT_LIST if LLAMA_RESULTS[ne]['echte_bias'] < LLAMA_RESULTS[ne]['global_bias'])\n    qwen_bias_wins = sum(1 for ne in N_EXPERT_LIST if QWEN_RESULTS[ne]['echte_bias'] < QWEN_RESULTS[ne]['global_bias'])\n    lines.append(f\"**Cross-model consistency**: Llama EC-HTE wins on bias in {llama_bias_wins}/3 budgets; \"\n                 f\"Qwen EC-HTE wins in {qwen_bias_wins}/3 budgets; \"\n                 f\"Gemma EC-HTE wins in {n_bias_wins}/3 budgets.\")\n    all_win = (n_bias_wins == len(N_EXPERT_LIST) and llama_bias_wins == len(N_EXPERT_LIST)\n               and qwen_bias_wins == len(N_EXPERT_LIST))\n    if all_win:\n        lines.append(\"EC-HTE's bias advantage is consistent across all three models (Llama, Qwen, Gemma).\")\n    lines.append(\"\")\n\n    avg_gemma_improvement = np.mean([\n        (summary[(summary['n_expert']==ne) & (summary['method']=='global_corrected')].iloc[0]['abs_bias'] -\n         summary[(summary['n_expert']==ne) & (summary['method']=='hb_ec_hte')].iloc[0]['abs_bias'])\n        for ne in N_EXPERT_LIST\n    ])\n    avg_qwen_improvement = np.mean([\n        QWEN_RESULTS[ne]['global_bias'] - QWEN_RESULTS[ne]['echte_bias']\n        for ne in N_EXPERT_LIST\n    ])\n    avg_llama_improvement = np.mean([\n        LLAMA_RESULTS[ne]['global_bias'] - LLAMA_RESULTS[ne]['echte_bias']\n        for ne in N_EXPERT_LIST\n    ])\n    lines.append(f\"Average Δ|Bias| (Global - EC-HTE): Gemma = {avg_gemma_improvement:+.4f}, Qwen = {avg_qwen_improvement:+.4f}, Llama = {avg_llama_improvement:+.4f}\")\n\n    improvements = [('Gemma', avg_gemma_improvement, gemma_fnr_range),\n                    ('Qwen', avg_qwen_improvement, qwen_fnr_range),\n                    ('Llama', avg_llama_improvement, llama_fnr_range)]\n    improvements.sort(key=lambda x: x[1], reverse=True)\n    lines.append(f\"Ranking by EC-HTE improvement: {improvements[0][0]} > {improvements[1][0]} > {improvements[2][0]}\")\n    lines.append(\"\")\n\n    report = \"\\n\".join(lines)\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"Gemma-2-9B Heterogeneous-τ DGP: EC-HTE vs Global\")\n    print(f\"N={N}, budgets={N_EXPERT_LIST}, seeds={N_MC}\")\n    print(\"Gemma per-subgroup CM:\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.4f}, FNR={cm['fnr']:.4f}\")\n    print(\"Subgroup τ values:\")\n    for s in SUBGROUP_LABELS:\n        t = SUBGROUP_TAU[s]\n        print(f\"  {s}: τ(z=0)={t['tau_z0']}, τ(z=1)={t['tau_z1']}, Δτ={t['tau_z1']-t['tau_z0']:.1f}\")\n    print()\n\n    out_dir = 'artifacts/c1_multi_llm'\n\n    # Dry run: 1 budget, 1 seed\n    print(\"=== Dry run (n_expert=200, 1 seed) ===\")\n    data = generate_data(SEED_BASE, 200)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    df_dry['n_expert'] = 200\n    print(f\"Dry run OK: {len(df_dry)} rows, columns: {list(df_dry.columns)}\")\n    for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n\n    # Verify oracle CATE values\n    print(\"\\n  Oracle CATE check:\")\n    for s_val in SUBGROUP_LABELS:\n        for zl in [0, 1]:\n            cell = df_dry[(df_dry['subgroup'] == s_val) & (df_dry['z_level'] == zl)]\n            true_val = cell['cate_true'].iloc[0]\n            expected = SUBGROUP_TAU[s_val]['tau_z1'] if zl == 1 else SUBGROUP_TAU[s_val]['tau_z0']\n            ok = \"OK\" if abs(true_val - expected) < 1e-10 else \"MISMATCH\"\n            print(f\"    {s_val} z={zl}: cate_true={true_val:.2f} expected={expected:.2f} [{ok}]\")\n    print()\n\n    # Full run\n    print(f\"=== Full run ({len(N_EXPERT_LIST)} budgets x {N_MC} seeds) ===\")\n    all_results = []\n    t0 = time.time()\n    total_runs = len(N_EXPERT_LIST) * N_MC\n    run_count = 0\n\n    for n_expert in N_EXPERT_LIST:\n        print(f\"\\n--- n_expert = {n_expert} ---\")\n        t_budget = time.time()\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            data = generate_data(seed, n_expert)\n            mc_rows = run_one_mc(data, seed)\n            for r in mc_rows:\n                r['n_expert'] = n_expert\n            all_results.extend(mc_rows)\n            run_count += 1\n            if (mc + 1) % 10 == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / run_count * (total_runs - run_count)\n                print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n        budget_time = time.time() - t_budget\n        print(f\"  n_expert={n_expert} done in {budget_time:.1f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(all_results)\n\n    # Save results CSV\n    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage', 'ci_width']\n    df_raw[col_order].to_csv(f'{out_dir}/gemma_hetero_tau_results.csv', index=False)\n    print(f\"Saved gemma_hetero_tau_results.csv ({len(df_raw)} rows)\")\n\n    # Write analysis\n    write_analysis(df_raw, f'{out_dir}/gemma_hetero_tau_analysis.md')\n\n    # Print summary\n    print(\"\\n=== Summary ===\")\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse_df = compute_rmse(df_raw)\n    summary = abs_bias.merge(rmse_df, on=['n_expert', 'method'])\n    for ne in N_EXPERT_LIST:\n        print(f\"\\n  n_expert={ne}:\")\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n            if len(row) > 0:\n                print(f\"    {m:20s}: |Bias|={row.iloc[0]['abs_bias']:.4f}  RMSE={row.iloc[0]['rmse']:.4f}\")\n    print()\n\n    # EC-HTE vs Global\n    print(\"=== EC-HTE vs Global (Gemma) ===\")\n    for ne in N_EXPERT_LIST:\n        gc = summary[(summary['n_expert'] == ne) & (summary['method'] == 'global_corrected')].iloc[0]\n        hb = summary[(summary['n_expert'] == ne) & (summary['method'] == 'hb_ec_hte')].iloc[0]\n        print(f\"  n_expert={ne}: |Bias| Global={gc['abs_bias']:.4f} vs ECHTE={hb['abs_bias']:.4f} \"\n              f\"({'ECHTE wins' if hb['abs_bias'] < gc['abs_bias'] else 'Global wins'})\")\n        print(f\"              RMSE  Global={gc['rmse']:.4f} vs ECHTE={hb['rmse']:.4f} \"\n              f\"({'ECHTE wins' if hb['rmse'] < gc['rmse'] else 'Global wins'})\")\n\n    # Cross-model comparison\n    print(\"\\n=== Cross-Model: Gemma vs Qwen vs Llama ===\")\n    for ne in N_EXPERT_LIST:\n        ggc = summary[(summary['n_expert'] == ne) & (summary['method'] == 'global_corrected')].iloc[0]\n        ghb = summary[(summary['n_expert'] == ne) & (summary['method'] == 'hb_ec_hte')].iloc[0]\n        qr = QWEN_RESULTS[ne]\n        lr = LLAMA_RESULTS[ne]\n        print(f\"  n_expert={ne}:\")\n        print(f\"    Gemma Δ|Bias| = {ggc['abs_bias'] - ghb['abs_bias']:+.4f}\")\n        print(f\"    Qwen  Δ|Bias| = {qr['global_bias'] - qr['echte_bias']:+.4f}\")\n        print(f\"    Llama Δ|Bias| = {lr['global_bias'] - lr['echte_bias']:+.4f}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "4628951f-89a7-4c1b-9d51-e084d31422fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NvLSZRTh5wPnNtwRsppASe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8166,
      "cache_read_input_tokens": 32033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8166
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

_source line 34 · 2026-05-22T00:18:47.772Z_

<details><summary>↩ Tool result · `toolu_012VQvXdwvucyujcHiD3oRQf`</summary>

```text
File created successfully at: /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_gemma_hetero_tau.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "cb7a36cb-fc35-400f-8dbe-85cae1bc4525",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_gemma_hetero_tau.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nHeterogeneous-τ DGP experiment with Gemma-2-9B confusion matrices.\nMirrors run_hetero_tau.py (Llama) but uses Gemma per-subgroup FPR/FNR.\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.optimize import minimize_scalar\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT_LIST = [200, 500, 1000]\nN_MC = 50\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']\nSUBGROUP_WEIGHTS = np.array([0.3816, 0.2224, 0.2551, 0.1408])\nSUBGROUP_WEIGHTS = SUBGROUP_WEIGHTS / SUBGROUP_WEIGHTS.sum()\n\nSUBGROUP_CM = {\n    'False_medium': {'fpr': 0.1100, 'fnr': 0.4368},\n    'False_short':  {'fpr': 0.1379, 'fnr': 0.3000},\n    'True_medium':  {'fpr': 0.0333, 'fnr': 0.2632},\n    'True_short':   {'fpr': 0.0909, 'fnr': 0.2069},\n}\n\nSUBGROUP_TAU = {\n    'True_short':   {'tau_z0': 0.2,  'tau_z1': 0.8},\n    'True_medium':  {'tau_z0': 0.35, 'tau_z1': 0.65},\n    'False_short':  {'tau_z0': 0.4,  'tau_z1': 0.5},\n    'False_medium': {'tau_z0': 0.45, 'tau_z1': 0.55},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\n\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === MAP-EB ===\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):\n    hp_rate = 1.0 / hp_scale\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = hp_shape * hp_scale\n            continue\n\n        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):\n            nll = _dirmult_neg_ll(a, _cl)\n            if a < 1e-10:\n                return 1e10\n            log_prior = (_shape - 1.0) * np.log(a) - _rate * a\n            return nll - log_prior\n\n        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n_sz = counts[i, z, :].sum()\n            d = n_sz + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    return C, alpha_opt\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\n# === DGP (heterogeneous tau) ===\n\ndef generate_data(seed, n_expert):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(4):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.zeros(N)\n    for i, s in enumerate(SUBGROUP_LABELS):\n        s_mask = S_idx == i\n        tau_s = SUBGROUP_TAU[s]\n        tau_vals[s_mask] = np.where(Z[s_mask] == 1, tau_s['tau_z1'], tau_s['tau_z0'])\n\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb, _ = estimate_cm_hb_map_eb(counts, SUBGROUP_LABELS)\n\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n        tau_s = SUBGROUP_TAU[s_val]\n\n        for z_level in [0, 1]:\n            oracle_cate = tau_s['tau_z1'] if z_level == 1 else tau_s['tau_z0']\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_w_nv = 2 * 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'cate_est': th_nv, 'cate_true': oracle_cate,\n                'coverage': cov_nv, 'ci_width': ci_w_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_w_gc = 2 * 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'cate_est': th_gc, 'cate_true': oracle_cate,\n                'coverage': cov_gc, 'ci_width': ci_w_gc,\n            })\n\n            # Stratified MLE\n            ci_w_ml = 2 * 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'cate_est': th_ml, 'cate_true': oracle_cate,\n                'coverage': cov_ml, 'ci_width': ci_w_ml,\n            })\n\n            # HB EC-HTE (MAP-EB)\n            ci_w_hb = 2 * 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'cate_est': th_hb, 'cate_true': oracle_cate,\n                'coverage': cov_hb, 'ci_width': ci_w_hb,\n            })\n\n    return rows\n\n\n# === Aggregation ===\n\ndef compute_corrected_abs_bias(df):\n    cell_bias = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias']\n                 .mean().abs().reset_index(name='abs_mean_bias'))\n    return (cell_bias.groupby(['n_expert', 'method'])['abs_mean_bias']\n            .mean().reset_index(name='abs_bias'))\n\n\ndef compute_rmse(df):\n    cell_rmse = (df.assign(bias_sq=df['bias'] ** 2)\n                 .groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias_sq']\n                 .mean().apply(np.sqrt).reset_index(name='rmse'))\n    return (cell_rmse.groupby(['n_expert', 'method'])['rmse']\n            .mean().reset_index(name='rmse'))\n\n\ndef compute_coverage(df):\n    return (df.groupby(['n_expert', 'method'])['coverage']\n            .mean().reset_index(name='coverage'))\n\n\ndef compute_ci_width(df):\n    return (df.groupby(['n_expert', 'method'])['ci_width']\n            .mean().reset_index(name='ci_width'))\n\n\n# === Analysis Report ===\n\nLLAMA_RESULTS = {\n    200:  {'global_bias': 0.0365, 'echte_bias': 0.0248, 'global_rmse': 0.1780, 'echte_rmse': 0.2606},\n    500:  {'global_bias': 0.0314, 'echte_bias': 0.0099, 'global_rmse': 0.1580, 'echte_rmse': 0.1760},\n    1000: {'global_bias': 0.0286, 'echte_bias': 0.0130, 'global_rmse': 0.1554, 'echte_rmse': 0.1602},\n}\n\nLLAMA_CM = {\n    'False_medium': {'fpr': 0.235, 'fnr': 0.319},\n    'False_short':  {'fpr': 0.310, 'fnr': 0.212},\n    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},\n    'True_short':   {'fpr': 0.091, 'fnr': 0.190},\n}\n\nQWEN_RESULTS = {\n    200:  {'global_bias': 0.0368, 'echte_bias': 0.0275, 'global_rmse': 0.1546, 'echte_rmse': 0.2293},\n    500:  {'global_bias': 0.0336, 'echte_bias': 0.0196, 'global_rmse': 0.1362, 'echte_rmse': 0.1631},\n    1000: {'global_bias': 0.0328, 'echte_bias': 0.0165, 'global_rmse': 0.1314, 'echte_rmse': 0.1393},\n}\n\nQWEN_CM = {\n    'False_medium': {'fpr': 0.180, 'fnr': 0.287},\n    'False_short':  {'fpr': 0.241, 'fnr': 0.175},\n    'True_medium':  {'fpr': 0.233, 'fnr': 0.211},\n    'True_short':   {'fpr': 0.000, 'fnr': 0.138},\n}\n\n\ndef write_analysis(df_raw, outpath):\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse = compute_rmse(df_raw)\n    cov = compute_coverage(df_raw)\n    ciw = compute_ci_width(df_raw)\n\n    summary = abs_bias.merge(rmse, on=['n_expert', 'method']).merge(\n        cov, on=['n_expert', 'method']).merge(ciw, on=['n_expert', 'method'])\n\n    lines = []\n    lines.append(\"# Gemma-2-9B Heterogeneous-τ DGP: EC-HTE vs Global Correction\\n\")\n    lines.append(\"## Design\\n\")\n    lines.append(f\"- N={N}, P(Z=1)={P_Z1}, K=4 subgroups\")\n    lines.append(\"- **LLM**: Gemma-2-9B (balanced binarization)\")\n    lines.append(\"- **Heterogeneous τ(z) across subgroups:**\")\n    for s in SUBGROUP_LABELS:\n        t = SUBGROUP_TAU[s]\n        lines.append(f\"  - {s}: τ(z=0)={t['tau_z0']}, τ(z=1)={t['tau_z1']}, Δτ={t['tau_z1']-t['tau_z0']:.1f}\")\n    lines.append(f\"- n_expert sweep: {N_EXPERT_LIST}\")\n    lines.append(f\"- {N_MC} MC seeds per budget\")\n    lines.append(\"- HB method: MAP-EB (Gamma(3,1) prior)\")\n    lines.append(f\"- |Bias| = avg across cells of |mean(bias) across seeds|\")\n    lines.append(f\"- RMSE = avg across cells of sqrt(mean(bias²) across seeds)\")\n    lines.append(\"\")\n\n    # Gemma CM table\n    lines.append(\"## Gemma-2-9B Per-Subgroup Confusion Matrix\\n\")\n    lines.append(\"| Subgroup | π_s | FPR | FNR | 1-FPR-FNR |\")\n    lines.append(\"|----------|-----|-----|-----|-----------|\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        w = SUBGROUP_WEIGHTS[SUBGROUP_LABELS.index(s)]\n        lines.append(f\"| {s} | {w:.4f} | {cm['fpr']:.4f} | {cm['fnr']:.4f} | {1-cm['fpr']-cm['fnr']:.4f} |\")\n    lines.append(\"\")\n    gemma_fpr_range = max(cm['fpr'] for cm in SUBGROUP_CM.values()) - min(cm['fpr'] for cm in SUBGROUP_CM.values())\n    gemma_fnr_range = max(cm['fnr'] for cm in SUBGROUP_CM.values()) - min(cm['fnr'] for cm in SUBGROUP_CM.values())\n    llama_fpr_range = max(cm['fpr'] for cm in LLAMA_CM.values()) - min(cm['fpr'] for cm in LLAMA_CM.values())\n    llama_fnr_range = max(cm['fnr'] for cm in LLAMA_CM.values()) - min(cm['fnr'] for cm in LLAMA_CM.values())\n    qwen_fpr_range = max(cm['fpr'] for cm in QWEN_CM.values()) - min(cm['fpr'] for cm in QWEN_CM.values())\n    qwen_fnr_range = max(cm['fnr'] for cm in QWEN_CM.values()) - min(cm['fnr'] for cm in QWEN_CM.values())\n    lines.append(f\"- Gemma Δ_FPR = {gemma_fpr_range:.4f}, Δ_FNR = {gemma_fnr_range:.4f}\")\n    lines.append(f\"- Qwen Δ_FPR = {qwen_fpr_range:.4f}, Δ_FNR = {qwen_fnr_range:.4f}\")\n    lines.append(f\"- Llama Δ_FPR = {llama_fpr_range:.4f}, Δ_FNR = {llama_fnr_range:.4f}\")\n    lines.append(f\"- **Note**: Gemma has strong FNR>FPR asymmetry (False_medium FNR=0.437 most extreme)\")\n    lines.append(\"\")\n\n    # Summary table\n    lines.append(\"## Summary Table (averaged across all cells)\\n\")\n    lines.append(\"| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |\")\n    lines.append(\"|----------|--------|-------|------|----------|----------|\")\n\n    method_order = ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']\n    method_labels = {'naive': 'Naive', 'global_corrected': 'Global', 'stratified_mle': 'Strat MLE', 'hb_ec_hte': 'HB EC-HTE'}\n\n    for ne in N_EXPERT_LIST:\n        for m in method_order:\n            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n            if len(row) > 0:\n                r = row.iloc[0]\n                lines.append(f\"| {ne} | {method_labels[m]} | {r['abs_bias']:.4f} | {r['rmse']:.4f} | {r['coverage']:.3f} | {r['ci_width']:.3f} |\")\n        lines.append(\"|----------|--------|-------|------|----------|----------|\")\n    lines.append(\"\")\n\n    # EC-HTE vs Global comparison\n    lines.append(\"## EC-HTE vs Global Comparison\\n\")\n    lines.append(\"| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |\")\n    lines.append(\"|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|\")\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        gc = sub[sub['method'] == 'global_corrected'].iloc[0]\n        hb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]\n        d_bias = gc['abs_bias'] - hb['abs_bias']\n        d_rmse = gc['rmse'] - hb['rmse']\n        wb = \"**YES**\" if hb['abs_bias'] < gc['abs_bias'] else \"no\"\n        wr = \"**YES**\" if hb['rmse'] < gc['rmse'] else \"no\"\n        lines.append(f\"| {ne} | {gc['abs_bias']:.4f} | {hb['abs_bias']:.4f} | {d_bias:+.4f} | {gc['rmse']:.4f} | {hb['rmse']:.4f} | {d_rmse:+.4f} | {wb} | {wr} |\")\n    lines.append(\"\")\n\n    # Per-subgroup breakdown\n    lines.append(\"## Per-Subgroup Breakdown\\n\")\n    for ne in N_EXPERT_LIST:\n        lines.append(f\"### n_expert = {ne}\\n\")\n        lines.append(\"| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |\")\n        lines.append(\"|----------|-----|---|-------------|-------------|-------------|-------------|------------|\")\n        sub_df = df_raw[df_raw['n_expert'] == ne]\n        for s_val in SUBGROUP_LABELS:\n            dt = SUBGROUP_TAU[s_val]['tau_z1'] - SUBGROUP_TAU[s_val]['tau_z0']\n            for z_level in [0, 1]:\n                cell_gc = sub_df[(sub_df['method'] == 'global_corrected') & (sub_df['subgroup'] == s_val) & (sub_df['z_level'] == z_level)]\n                cell_hb = sub_df[(sub_df['method'] == 'hb_ec_hte') & (sub_df['subgroup'] == s_val) & (sub_df['z_level'] == z_level)]\n                bias_gc = abs(cell_gc['bias'].mean())\n                bias_hb = abs(cell_hb['bias'].mean())\n                rmse_gc = np.sqrt((cell_gc['bias'] ** 2).mean())\n                rmse_hb = np.sqrt((cell_hb['bias'] ** 2).mean())\n                imp = bias_gc - bias_hb\n                lines.append(f\"| {s_val} | {dt:.1f} | {z_level} | {bias_gc:.4f} | {bias_hb:.4f} | {imp:+.4f} | {rmse_gc:.4f} | {rmse_hb:.4f} |\")\n        lines.append(\"\")\n\n    # Bias-variance decomposition\n    lines.append(\"## Bias-Variance Decomposition\\n\")\n    lines.append(\"| n_expert | Method | Bias² | Variance | MSE |\")\n    lines.append(\"|----------|--------|-------|----------|-----|\")\n    for ne in N_EXPERT_LIST:\n        for m in method_order:\n            sub_df = df_raw[(df_raw['n_expert'] == ne) & (df_raw['method'] == m)]\n            cell_stats = (sub_df.groupby(['subgroup', 'z_level'])['bias']\n                          .agg(['mean', 'var', 'count']).reset_index())\n            mean_bias_sq = (cell_stats['mean'] ** 2).mean()\n            variance = cell_stats['var'].mean()\n            mse = mean_bias_sq + variance\n            lines.append(f\"| {ne} | {method_labels[m]} | {mean_bias_sq:.4f} | {variance:.4f} | {mse:.4f} |\")\n    lines.append(\"\")\n\n    # Cross-model comparison with Llama and Qwen\n    lines.append(\"## Cross-Model Comparison: Gemma vs Qwen vs Llama\\n\")\n    lines.append(\"### CM Heterogeneity\\n\")\n    lines.append(\"| Metric | Gemma-2-9B | Qwen2.5-7B | Llama3.1-8B |\")\n    lines.append(\"|--------|-----------|-----------|------------|\")\n    lines.append(f\"| Δ_FPR (max-min) | {gemma_fpr_range:.4f} | {qwen_fpr_range:.4f} | {llama_fpr_range:.4f} |\")\n    lines.append(f\"| Δ_FNR (max-min) | {gemma_fnr_range:.4f} | {qwen_fnr_range:.4f} | {llama_fnr_range:.4f} |\")\n    lines.append(f\"| Mean Δ_error | {(gemma_fpr_range+gemma_fnr_range)/2:.4f} | {(qwen_fpr_range+qwen_fnr_range)/2:.4f} | {(llama_fpr_range+llama_fnr_range)/2:.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### Bias Comparison\\n\")\n    lines.append(\"| n_expert | Gemma |Bias|_Global | Gemma |Bias|_ECHTE | Gemma Δ|Bias| | Qwen |Bias|_Global | Qwen |Bias|_ECHTE | Qwen Δ|Bias| | Llama |Bias|_Global | Llama |Bias|_ECHTE | Llama Δ|Bias| |\")\n    lines.append(\"|----------|------------------|--------------------|--------------|--------------------|--------------------|--------------|--------------------|--------------------|--------------| \")\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        ggc = sub[sub['method'] == 'global_corrected'].iloc[0]\n        ghb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]\n        gd = ggc['abs_bias'] - ghb['abs_bias']\n        qr = QWEN_RESULTS[ne]\n        qd = qr['global_bias'] - qr['echte_bias']\n        lr = LLAMA_RESULTS[ne]\n        ld = lr['global_bias'] - lr['echte_bias']\n        lines.append(f\"| {ne} | {ggc['abs_bias']:.4f} | {ghb['abs_bias']:.4f} | {gd:+.4f} | {qr['global_bias']:.4f} | {qr['echte_bias']:.4f} | {qd:+.4f} | {lr['global_bias']:.4f} | {lr['echte_bias']:.4f} | {ld:+.4f} |\")\n    lines.append(\"\")\n\n    lines.append(\"### RMSE Comparison\\n\")\n    lines.append(\"| n_expert | Gemma RMSE_Global | Gemma RMSE_ECHTE | Qwen RMSE_Global | Qwen RMSE_ECHTE | Llama RMSE_Global | Llama RMSE_ECHTE |\")\n    lines.append(\"|----------|-----------------|----------------|-----------------|----------------|------------------|-----------------|\")\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        ggc = sub[sub['method'] == 'global_corrected'].iloc[0]\n        ghb = sub[sub['method'] == 'hb_ec_hte'].iloc[0]\n        qr = QWEN_RESULTS[ne]\n        lr = LLAMA_RESULTS[ne]\n        lines.append(f\"| {ne} | {ggc['rmse']:.4f} | {ghb['rmse']:.4f} | {qr['global_rmse']:.4f} | {qr['echte_rmse']:.4f} | {lr['global_rmse']:.4f} | {lr['echte_rmse']:.4f} |\")\n    lines.append(\"\")\n\n    # Conclusion\n    lines.append(\"## Conclusion\\n\")\n    gc_all = summary[summary['method'] == 'global_corrected']\n    hb_all = summary[summary['method'] == 'hb_ec_hte']\n    n_bias_wins = 0\n    n_rmse_wins = 0\n    for ne in N_EXPERT_LIST:\n        gc_row = gc_all[gc_all['n_expert'] == ne].iloc[0]\n        hb_row = hb_all[hb_all['n_expert'] == ne].iloc[0]\n        if hb_row['abs_bias'] < gc_row['abs_bias']:\n            n_bias_wins += 1\n        if hb_row['rmse'] < gc_row['rmse']:\n            n_rmse_wins += 1\n\n    lines.append(f\"EC-HTE wins on |Bias| in {n_bias_wins}/{len(N_EXPERT_LIST)} budget levels.\")\n    lines.append(f\"EC-HTE wins on RMSE in {n_rmse_wins}/{len(N_EXPERT_LIST)} budget levels.\\n\")\n\n    if n_bias_wins == len(N_EXPERT_LIST):\n        lines.append(\"**Result: Under heterogeneous-τ DGP with Gemma-2-9B CMs, EC-HTE consistently outperforms Global correction in bias.**\\n\")\n    elif n_bias_wins > 0:\n        lines.append(f\"**Result: Under heterogeneous-τ DGP with Gemma-2-9B CMs, EC-HTE outperforms Global in bias at {n_bias_wins} of {len(N_EXPERT_LIST)} budget levels.**\\n\")\n    else:\n        lines.append(\"**Result: EC-HTE does not outperform Global in bias under this DGP configuration with Gemma CMs.**\\n\")\n\n    # Cross-model conclusion\n    llama_bias_wins = sum(1 for ne in N_EXPERT_LIST if LLAMA_RESULTS[ne]['echte_bias'] < LLAMA_RESULTS[ne]['global_bias'])\n    qwen_bias_wins = sum(1 for ne in N_EXPERT_LIST if QWEN_RESULTS[ne]['echte_bias'] < QWEN_RESULTS[ne]['global_bias'])\n    lines.append(f\"**Cross-model consistency**: Llama EC-HTE wins on bias in {llama_bias_wins}/3 budgets; \"\n                 f\"Qwen EC-HTE wins in {qwen_bias_wins}/3 budgets; \"\n                 f\"Gemma EC-HTE wins in {n_bias_wins}/3 budgets.\")\n    all_win = (n_bias_wins == len(N_EXPERT_LIST) and llama_bias_wins == len(N_EXPERT_LIST)\n               and qwen_bias_wins == len(N_EXPERT_LIST))\n    if all_win:\n        lines.append(\"EC-HTE's bias advantage is consistent across all three models (Llama, Qwen, Gemma).\")\n    lines.append(\"\")\n\n    avg_gemma_improvement = np.mean([\n        (summary[(summary['n_expert']==ne) & (summary['method']=='global_corrected')].iloc[0]['abs_bias'] -\n         summary[(summary['n_expert']==ne) & (summary['method']=='hb_ec_hte')].iloc[0]['abs_bias'])\n        for ne in N_EXPERT_LIST\n    ])\n    avg_qwen_improvement = np.mean([\n        QWEN_RESULTS[ne]['global_bias'] - QWEN_RESULTS[ne]['echte_bias']\n        for ne in N_EXPERT_LIST\n    ])\n    avg_llama_improvement = np.mean([\n        LLAMA_RESULTS[ne]['global_bias'] - LLAMA_RESULTS[ne]['echte_bias']\n        for ne in N_EXPERT_LIST\n    ])\n    lines.append(f\"Average Δ|Bias| (Global - EC-HTE): Gemma = {avg_gemma_improvement:+.4f}, Qwen = {avg_qwen_improvement:+.4f}, Llama = {avg_llama_improvement:+.4f}\")\n\n    improvements = [('Gemma', avg_gemma_improvement, gemma_fnr_range),\n                    ('Qwen', avg_qwen_improvement, qwen_fnr_range),\n                    ('Llama', avg_llama_improvement, llama_fnr_range)]\n    improvements.sort(key=lambda x: x[1], reverse=True)\n    lines.append(f\"Ranking by EC-HTE improvement: {improvements[0][0]} > {improvements[1][0]} > {improvements[2][0]}\")\n    lines.append(\"\")\n\n    report = \"\\n\".join(lines)\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"Gemma-2-9B Heterogeneous-τ DGP: EC-HTE vs Global\")\n    print(f\"N={N}, budgets={N_EXPERT_LIST}, seeds={N_MC}\")\n    print(\"Gemma per-subgroup CM:\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.4f}, FNR={cm['fnr']:.4f}\")\n    print(\"Subgroup τ values:\")\n    for s in SUBGROUP_LABELS:\n        t = SUBGROUP_TAU[s]\n        print(f\"  {s}: τ(z=0)={t['tau_z0']}, τ(z=1)={t['tau_z1']}, Δτ={t['tau_z1']-t['tau_z0']:.1f}\")\n    print()\n\n    out_dir = 'artifacts/c1_multi_llm'\n\n    # Dry run: 1 budget, 1 seed\n    print(\"=== Dry run (n_expert=200, 1 seed) ===\")\n    data = generate_data(SEED_BASE, 200)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    df_dry['n_expert'] = 200\n    print(f\"Dry run OK: {len(df_dry)} rows, columns: {list(df_dry.columns)}\")\n    for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n\n    # Verify oracle CATE values\n    print(\"\\n  Oracle CATE check:\")\n    for s_val in SUBGROUP_LABELS:\n        for zl in [0, 1]:\n            cell = df_dry[(df_dry['subgroup'] == s_val) & (df_dry['z_level'] == zl)]\n            true_val = cell['cate_true'].iloc[0]\n            expected = SUBGROUP_TAU[s_val]['tau_z1'] if zl == 1 else SUBGROUP_TAU[s_val]['tau_z0']\n            ok = \"OK\" if abs(true_val - expected) < 1e-10 else \"MISMATCH\"\n            print(f\"    {s_val} z={zl}: cate_true={true_val:.2f} expected={expected:.2f} [{ok}]\")\n    print()\n\n    # Full run\n    print(f\"=== Full run ({len(N_EXPERT_LIST)} budgets x {N_MC} seeds) ===\")\n    all_results = []\n    t0 = time.time()\n    total_runs = len(N_EXPERT_LIST) * N_MC\n    run_count = 0\n\n    for n_expert in N_EXPERT_LIST:\n        print(f\"\\n--- n_expert = {n_expert} ---\")\n        t_budget = time.time()\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            data = generate_data(seed, n_expert)\n            mc_rows = run_one_mc(data, seed)\n            for r in mc_rows:\n                r['n_expert'] = n_expert\n            all_results.extend(mc_rows)\n            run_count += 1\n            if (mc + 1) % 10 == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / run_count * (total_runs - run_count)\n                print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n        budget_time = time.time() - t_budget\n        print(f\"  n_expert={n_expert} done in {budget_time:.1f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(all_results)\n\n    # Save results CSV\n    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage', 'ci_width']\n    df_raw[col_order].to_csv(f'{out_dir}/gemma_hetero_tau_results.csv', index=False)\n    print(f\"Saved gemma_hetero_tau_results.csv ({len(df_raw)} rows)\")\n\n    # Write analysis\n    write_analysis(df_raw, f'{out_dir}/gemma_hetero_tau_analysis.md')\n\n    # Print summary\n    print(\"\\n=== Summary ===\")\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse_df = compute_rmse(df_raw)\n    summary = abs_bias.merge(rmse_df, on=['n_expert', 'method'])\n    for ne in N_EXPERT_LIST:\n        print(f\"\\n  n_expert={ne}:\")\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n            if len(row) > 0:\n                print(f\"    {m:20s}: |Bias|={row.iloc[0]['abs_bias']:.4f}  RMSE={row.iloc[0]['rmse']:.4f}\")\n    print()\n\n    # EC-HTE vs Global\n    print(\"=== EC-HTE vs Global (Gemma) ===\")\n    for ne in N_EXPERT_LIST:\n        gc = summary[(summary['n_expert'] == ne) & (summary['method'] == 'global_corrected')].iloc[0]\n        hb = summary[(summary['n_expert'] == ne) & (summary['method'] == 'hb_ec_hte')].iloc[0]\n        print(f\"  n_expert={ne}: |Bias| Global={gc['abs_bias']:.4f} vs ECHTE={hb['abs_bias']:.4f} \"\n              f\"({'ECHTE wins' if hb['abs_bias'] < gc['abs_bias'] else 'Global wins'})\")\n        print(f\"              RMSE  Global={gc['rmse']:.4f} vs ECHTE={hb['rmse']:.4f} \"\n              f\"({'ECHTE wins' if hb['rmse'] < gc['rmse'] else 'Global wins'})\")\n\n    # Cross-model comparison\n    print(\"\\n=== Cross-Model: Gemma vs Qwen vs Llama ===\")\n    for ne in N_EXPERT_LIST:\n        ggc = summary[(summary['n_expert'] == ne) & (summary['method'] == 'global_corrected')].iloc[0]\n        ghb = summary[(summary['n_expert'] == ne) & (summary['method'] == 'hb_ec_hte')].iloc[0]\n        qr = QWEN_RESULTS[ne]\n        lr = LLAMA_RESULTS[ne]\n        print(f\"  n_expert={ne}:\")\n        print(f\"    Gemma Δ|Bias| = {ggc['abs_bias'] - ghb['abs_bias']:+.4f}\")\n        print(f\"    Qwen  Δ|Bias| = {qr['global_bias'] - qr['echte_bias']:+.4f}\")\n        print(f\"    Llama Δ|Bias| = {lr['global_bias'] - lr['echte_bias']:+.4f}\")\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 35_

Script created. Running it now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "c268fe4e-8c81-4a00-9004-d6a2966b6fc1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bxWtPtJVZ4qTA9udDQWYS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13531,
      "cache_read_input_tokens": 40199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13531
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

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_017hkmvC3E5wHRihJBnFrK9V`</summary>

```json
{
  "command": "python artifacts/c1_multi_llm/run_gemma_hetero_tau.py 2>&1",
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
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "5101fbf6-d78e-4f03-a35a-757d86ff2c61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bxWtPtJVZ4qTA9udDQWYS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13531,
      "cache_read_input_tokens": 40199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13531
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

_source line 37 · 2026-05-22T00:18:52.978Z_

<details><summary>↩ Tool result · reported error · `toolu_017hkmvC3E5wHRihJBnFrK9V`</summary>

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
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "b46f7e7a-7662-416d-8c7e-e3bcf632ae97",
  "tool_use_result": "Error: Exit code 127\n/bin/bash: line 1: python: command not found"
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_01M8kjX1QdbbxpigmMjjoxfv`</summary>

```json
{
  "command": "python3 artifacts/c1_multi_llm/run_gemma_hetero_tau.py 2>&1",
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
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "64278c8c-db9d-4b14-8dd8-111305dbadcd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013q5iHpPuwRxhei6QC8X1Qz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 142,
      "cache_read_input_tokens": 53730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 142
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

### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bcuzx8tgj",
  "tool_use_id": "toolu_01M8kjX1QdbbxpigmMjjoxfv",
  "description": "python3 artifacts/c1_multi_llm/run_gemma_hetero_tau.py 2>&1",
  "task_type": "local_bash",
  "uuid": "2689ccaf-eefb-4f5f-ac0b-ef75b4b5970c",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0"
}
```

---

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bcuzx8tgj",
  "tool_use_id": "toolu_01M8kjX1QdbbxpigmMjjoxfv",
  "status": "completed",
  "output_file": "",
  "summary": "python3 artifacts/c1_multi_llm/run_gemma_hetero_tau.py 2>&1",
  "uuid": "e20040fe-163c-46a0-8e8f-43a05d340002",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0"
}
```

---

### Tool result

_source line 41 · 2026-05-22T00:18:59.292Z_

<details><summary>↩ Tool result · `toolu_01M8kjX1QdbbxpigmMjjoxfv`</summary>

```text
Gemma-2-9B Heterogeneous-τ DGP: EC-HTE vs Global
N=5000, budgets=[200, 500, 1000], seeds=50
Gemma per-subgroup CM:
  False_medium: FPR=0.1100, FNR=0.4368
  False_short: FPR=0.1379, FNR=0.3000
  True_medium: FPR=0.0333, FNR=0.2632
  True_short: FPR=0.0909, FNR=0.2069
Subgroup τ values:
  False_medium: τ(z=0)=0.45, τ(z=1)=0.55, Δτ=0.1
  False_short: τ(z=0)=0.4, τ(z=1)=0.5, Δτ=0.1
  True_medium: τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3
  True_short: τ(z=0)=0.2, τ(z=1)=0.8, Δτ=0.6

=== Dry run (n_expert=200, 1 seed) ===
Dry run OK: 32 rows, columns: ['seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage', 'ci_width', 'n_expert']
  naive               : mean |bias| = 0.0752
  global_corrected    : mean |bias| = 0.1193
  stratified_mle      : mean |bias| = 0.1197
  hb_ec_hte           : mean |bias| = 0.1267

  Oracle CATE check:
    False_medium z=0: cate_true=0.45 expected=0.45 [OK]
    False_medium z=1: cate_true=0.55 expected=0.55 [OK]
    False_short z=0: cate_true=0.40 expected=0.40 [OK]
    False_short z=1: cate_true=0.50 expected=0.50 [OK]
    True_medium z=0: cate_true=0.35 expected=0.35 [OK]
    True_medium z=1: cate_true=0.65 expected=0.65 [OK]
    True_short z=0: cate_true=0.20 expected=0.20 [OK]
    True_short z=1: cate_true=0.80 expected=0.80 [OK]

=== Full run (3 budgets x 50 seeds) ===

--- n_expert = 200 ---
  [10/50] 0s elapsed, ETA 2s
  [20/50] 0s elapsed, ETA 2s
  [30/50] 0s elapsed, ETA 2s
  [40/50] 1s elapsed, ETA 1s
  [50/50] 1s elapsed, ETA 1s
  n_expert=200 done in 0.7s

--- n_expert = 500 ---
  [10/50] 1s elapsed, ETA 1s
  [20/50] 1s elapsed, ETA 1s
  [30/50] 1s elapsed, ETA 1s
  [40/50] 1s elapsed, ETA 1s
  [50/50] 1s elapsed, ETA 1s
  n_expert=500 done in 0.8s

--- n_expert = 1000 ---
  [10/50] 2s elapsed, ETA 1s
  [20/50] 2s elapsed, ETA 0s
  [30/50] 2s elapsed, ETA 0s
  [40/50] 2s elapsed, ETA 0s
  [50/50] 2s elapsed, ETA 0s
  n_expert=1000 done in 0.7s

Total time: 2.1s
Saved gemma_hetero_tau_results.csv (4800 rows)
Wrote artifacts/c1_multi_llm/gemma_hetero_tau_analysis.md

=== Summary ===

  n_expert=200:
    naive               : |Bias|=0.0598  RMSE=0.1101
    global_corrected    : |Bias|=0.0261  RMSE=0.1498
    stratified_mle      : |Bias|=0.0263  RMSE=0.2708
    hb_ec_hte           : |Bias|=0.0269  RMSE=0.2614

  n_expert=500:
    naive               : |Bias|=0.0598  RMSE=0.1101
    global_corrected    : |Bias|=0.0153  RMSE=0.1353
    stratified_mle      : |Bias|=0.0156  RMSE=0.1760
    hb_ec_hte           : |Bias|=0.0117  RMSE=0.1741

  n_expert=1000:
    naive               : |Bias|=0.0598  RMSE=0.1101
    global_corrected    : |Bias|=0.0155  RMSE=0.1310
    stratified_mle      : |Bias|=0.0169  RMSE=0.1444
    hb_ec_hte           : |Bias|=0.0157  RMSE=0.1435

=== EC-HTE vs Global (Gemma) ===
  n_expert=200: |Bias| Global=0.0261 vs ECHTE=0.0269 (Global wins)
              RMSE  Global=0.1498 vs ECHTE=0.2614 (Global wins)
  n_expert=500: |Bias| Global=0.0153 vs ECHTE=0.0117 (ECHTE wins)
              RMSE  Global=0.1353 vs ECHTE=0.1741 (Global wins)
  n_expert=1000: |Bias| Global=0.0155 vs ECHTE=0.0157 (Global wins)
              RMSE  Global=0.1310 vs ECHTE=0.1435 (Global wins)

=== Cross-Model: Gemma vs Qwen vs Llama ===
  n_expert=200:
    Gemma Δ|Bias| = -0.0008
    Qwen  Δ|Bias| = +0.0093
    Llama Δ|Bias| = +0.0117
  n_expert=500:
    Gemma Δ|Bias| = +0.0036
    Qwen  Δ|Bias| = +0.0140
    Llama Δ|Bias| = +0.0215
  n_expert=1000:
    Gemma Δ|Bias| = -0.0002
    Qwen  Δ|Bias| = +0.0163
    Llama Δ|Bias| = +0.0156
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "c33aa703-4afe-4640-8c03-7e720e56f0a5",
  "tool_use_result": {
    "stdout": "Gemma-2-9B Heterogeneous-τ DGP: EC-HTE vs Global\nN=5000, budgets=[200, 500, 1000], seeds=50\nGemma per-subgroup CM:\n  False_medium: FPR=0.1100, FNR=0.4368\n  False_short: FPR=0.1379, FNR=0.3000\n  True_medium: FPR=0.0333, FNR=0.2632\n  True_short: FPR=0.0909, FNR=0.2069\nSubgroup τ values:\n  False_medium: τ(z=0)=0.45, τ(z=1)=0.55, Δτ=0.1\n  False_short: τ(z=0)=0.4, τ(z=1)=0.5, Δτ=0.1\n  True_medium: τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3\n  True_short: τ(z=0)=0.2, τ(z=1)=0.8, Δτ=0.6\n\n=== Dry run (n_expert=200, 1 seed) ===\nDry run OK: 32 rows, columns: ['seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage', 'ci_width', 'n_expert']\n  naive               : mean |bias| = 0.0752\n  global_corrected    : mean |bias| = 0.1193\n  stratified_mle      : mean |bias| = 0.1197\n  hb_ec_hte           : mean |bias| = 0.1267\n\n  Oracle CATE check:\n    False_medium z=0: cate_true=0.45 expected=0.45 [OK]\n    False_medium z=1: cate_true=0.55 expected=0.55 [OK]\n    False_short z=0: cate_true=0.40 expected=0.40 [OK]\n    False_short z=1: cate_true=0.50 expected=0.50 [OK]\n    True_medium z=0: cate_true=0.35 expected=0.35 [OK]\n    True_medium z=1: cate_true=0.65 expected=0.65 [OK]\n    True_short z=0: cate_true=0.20 expected=0.20 [OK]\n    True_short z=1: cate_true=0.80 expected=0.80 [OK]\n\n=== Full run (3 budgets x 50 seeds) ===\n\n--- n_expert = 200 ---\n  [10/50] 0s elapsed, ETA 2s\n  [20/50] 0s elapsed, ETA 2s\n  [30/50] 0s elapsed, ETA 2s\n  [40/50] 1s elapsed, ETA 1s\n  [50/50] 1s elapsed, ETA 1s\n  n_expert=200 done in 0.7s\n\n--- n_expert = 500 ---\n  [10/50] 1s elapsed, ETA 1s\n  [20/50] 1s elapsed, ETA 1s\n  [30/50] 1s elapsed, ETA 1s\n  [40/50] 1s elapsed, ETA 1s\n  [50/50] 1s elapsed, ETA 1s\n  n_expert=500 done in 0.8s\n\n--- n_expert = 1000 ---\n  [10/50] 2s elapsed, ETA 1s\n  [20/50] 2s elapsed, ETA 0s\n  [30/50] 2s elapsed, ETA 0s\n  [40/50] 2s elapsed, ETA 0s\n  [50/50] 2s elapsed, ETA 0s\n  n_expert=1000 done in 0.7s\n\nTotal time: 2.1s\nSaved gemma_hetero_tau_results.csv (4800 rows)\nWrote artifacts/c1_multi_llm/gemma_hetero_tau_analysis.md\n\n=== Summary ===\n\n  n_expert=200:\n    naive               : |Bias|=0.0598  RMSE=0.1101\n    global_corrected    : |Bias|=0.0261  RMSE=0.1498\n    stratified_mle      : |Bias|=0.0263  RMSE=0.2708\n    hb_ec_hte           : |Bias|=0.0269  RMSE=0.2614\n\n  n_expert=500:\n    naive               : |Bias|=0.0598  RMSE=0.1101\n    global_corrected    : |Bias|=0.0153  RMSE=0.1353\n    stratified_mle      : |Bias|=0.0156  RMSE=0.1760\n    hb_ec_hte           : |Bias|=0.0117  RMSE=0.1741\n\n  n_expert=1000:\n    naive               : |Bias|=0.0598  RMSE=0.1101\n    global_corrected    : |Bias|=0.0155  RMSE=0.1310\n    stratified_mle      : |Bias|=0.0169  RMSE=0.1444\n    hb_ec_hte           : |Bias|=0.0157  RMSE=0.1435\n\n=== EC-HTE vs Global (Gemma) ===\n  n_expert=200: |Bias| Global=0.0261 vs ECHTE=0.0269 (Global wins)\n              RMSE  Global=0.1498 vs ECHTE=0.2614 (Global wins)\n  n_expert=500: |Bias| Global=0.0153 vs ECHTE=0.0117 (ECHTE wins)\n              RMSE  Global=0.1353 vs ECHTE=0.1741 (Global wins)\n  n_expert=1000: |Bias| Global=0.0155 vs ECHTE=0.0157 (Global wins)\n              RMSE  Global=0.1310 vs ECHTE=0.1435 (Global wins)\n\n=== Cross-Model: Gemma vs Qwen vs Llama ===\n  n_expert=200:\n    Gemma Δ|Bias| = -0.0008\n    Qwen  Δ|Bias| = +0.0093\n    Llama Δ|Bias| = +0.0117\n  n_expert=500:\n    Gemma Δ|Bias| = +0.0036\n    Qwen  Δ|Bias| = +0.0140\n    Llama Δ|Bias| = +0.0215\n  n_expert=1000:\n    Gemma Δ|Bias| = -0.0002\n    Qwen  Δ|Bias| = +0.0163\n    Llama Δ|Bias| = +0.0156",
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

_source line 42_

Now let me verify the CSV row count and check the output files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "c80e108b-3804-49a7-bcab-22adc06f611e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Qfnd5eErSWDU59N3ibR1V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1957,
      "cache_read_input_tokens": 53872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1957
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

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_018SRNT7JLFbWU5eu999Psfc`</summary>

```json
{
  "command": "wc -l artifacts/c1_multi_llm/gemma_hetero_tau_results.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "348a268b-9910-4d5a-8106-2b0e4789dfff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Qfnd5eErSWDU59N3ibR1V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1957,
      "cache_read_input_tokens": 53872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1957
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

_source line 44 · 2026-05-22T00:19:02.656Z_

<details><summary>↩ Tool result · `toolu_018SRNT7JLFbWU5eu999Psfc`</summary>

```text
4801 artifacts/c1_multi_llm/gemma_hetero_tau_results.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "51137d4f-0849-4f6d-9841-4781bacd8405",
  "tool_use_result": {
    "stdout": "4801 artifacts/c1_multi_llm/gemma_hetero_tau_results.csv",
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

_source line 45_

<details open><summary>🔧 Tool call — Read · `toolu_011paky8AdSEqjU7Uo8F3i6c`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/gemma_hetero_tau_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "32903dc2-513e-4879-808f-de0f00488a16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Qfnd5eErSWDU59N3ibR1V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1957,
      "cache_read_input_tokens": 53872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1957
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

_source line 46 · 2026-05-22T00:19:03.373Z_

<details><summary>↩ Tool result · `toolu_011paky8AdSEqjU7Uo8F3i6c`</summary>

```text
1	# Gemma-2-9B Heterogeneous-τ DGP: EC-HTE vs Global Correction
2	
3	## Design
4	
5	- N=5000, P(Z=1)=0.652, K=4 subgroups
6	- **LLM**: Gemma-2-9B (balanced binarization)
7	- **Heterogeneous τ(z) across subgroups:**
8	  - False_medium: τ(z=0)=0.45, τ(z=1)=0.55, Δτ=0.1
9	  - False_short: τ(z=0)=0.4, τ(z=1)=0.5, Δτ=0.1
10	  - True_medium: τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3
11	  - True_short: τ(z=0)=0.2, τ(z=1)=0.8, Δτ=0.6
12	- n_expert sweep: [200, 500, 1000]
13	- 50 MC seeds per budget
14	- HB method: MAP-EB (Gamma(3,1) prior)
15	- |Bias| = avg across cells of |mean(bias) across seeds|
16	- RMSE = avg across cells of sqrt(mean(bias²) across seeds)
17	
18	## Gemma-2-9B Per-Subgroup Confusion Matrix
19	
20	| Subgroup | π_s | FPR | FNR | 1-FPR-FNR |
21	|----------|-----|-----|-----|-----------|
22	| False_medium | 0.3816 | 0.1100 | 0.4368 | 0.4532 |
23	| False_short | 0.2224 | 0.1379 | 0.3000 | 0.5621 |
24	| True_medium | 0.2551 | 0.0333 | 0.2632 | 0.7035 |
25	| True_short | 0.1408 | 0.0909 | 0.2069 | 0.7022 |
26	
27	- Gemma Δ_FPR = 0.1046, Δ_FNR = 0.2299
28	- Qwen Δ_FPR = 0.2410, Δ_FNR = 0.1490
29	- Llama Δ_FPR = 0.2190, Δ_FNR = 0.1290
30	- **Note**: Gemma has strong FNR>FPR asymmetry (False_medium FNR=0.437 most extreme)
31	
32	## Summary Table (averaged across all cells)
33	
34	| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |
35	|----------|--------|-------|------|----------|----------|
36	| 200 | Naive | 0.0598 | 0.1101 | 0.873 | 0.332 |
37	| 200 | Global | 0.0261 | 0.1498 | 0.927 | 0.525 |
38	| 200 | Strat MLE | 0.0263 | 0.2708 | 0.802 | 0.575 |
39	| 200 | HB EC-HTE | 0.0269 | 0.2614 | 0.807 | 0.562 |
40	|----------|--------|-------|------|----------|----------|
41	| 500 | Naive | 0.0598 | 0.1101 | 0.873 | 0.332 |
42	| 500 | Global | 0.0153 | 0.1353 | 0.948 | 0.514 |
43	| 500 | Strat MLE | 0.0156 | 0.1760 | 0.877 | 0.519 |
44	| 500 | HB EC-HTE | 0.0117 | 0.1741 | 0.873 | 0.515 |
45	|----------|--------|-------|------|----------|----------|
46	| 1000 | Naive | 0.0598 | 0.1101 | 0.873 | 0.332 |
47	| 1000 | Global | 0.0155 | 0.1310 | 0.950 | 0.513 |
48	| 1000 | Strat MLE | 0.0169 | 0.1444 | 0.910 | 0.505 |
49	| 1000 | HB EC-HTE | 0.0157 | 0.1435 | 0.915 | 0.503 |
50	|----------|--------|-------|------|----------|----------|
51	
52	## EC-HTE vs Global Comparison
53	
54	| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |
55	|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|
56	| 200 | 0.0261 | 0.0269 | -0.0008 | 0.1498 | 0.2614 | -0.1116 | no | no |
57	| 500 | 0.0153 | 0.0117 | +0.0036 | 0.1353 | 0.1741 | -0.0388 | **YES** | no |
58	| 1000 | 0.0155 | 0.0157 | -0.0002 | 0.1310 | 0.1435 | -0.0125 | no | no |
59	
60	## Per-Subgroup Breakdown
61	
62	### n_expert = 200
63	
64	| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
65	|----------|-----|---|-------------|-------------|-------------|-------------|------------|
66	| False_medium | 0.1 | 0 | 0.0049 | 0.0374 | -0.0325 | 0.1549 | 0.2857 |
67	| False_medium | 0.1 | 1 | 0.0158 | 0.0342 | -0.0185 | 0.0974 | 0.1584 |
68	| False_short | 0.1 | 0 | 0.0299 | 0.0112 | +0.0186 | 0.2069 | 0.3273 |
69	| False_short | 0.1 | 1 | 0.0094 | 0.0158 | -0.0064 | 0.1176 | 0.1720 |
70	| True_medium | 0.3 | 0 | 0.0213 | 0.0034 | +0.0178 | 0.1556 | 0.1811 |
71	| True_medium | 0.3 | 1 | 0.0297 | 0.0430 | -0.0133 | 0.0945 | 0.1278 |
72	| True_short | 0.6 | 0 | 0.0827 | 0.0011 | +0.0815 | 0.2345 | 0.5282 |
73	| True_short | 0.6 | 1 | 0.0151 | 0.0688 | -0.0538 | 0.1368 | 0.3107 |
74	
75	### n_expert = 500
76	
77	| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
78	|----------|-----|---|-------------|-------------|-------------|-------------|------------|
79	| False_medium | 0.1 | 0 | 0.0186 | 0.0031 | +0.0155 | 0.1369 | 0.2157 |
80	| False_medium | 0.1 | 1 | 0.0036 | 0.0125 | -0.0089 | 0.0870 | 0.1200 |
81	| False_short | 0.1 | 0 | 0.0194 | 0.0023 | +0.0171 | 0.1809 | 0.2303 |
82	| False_short | 0.1 | 1 | 0.0026 | 0.0008 | +0.0018 | 0.1087 | 0.1344 |
83	| True_medium | 0.3 | 0 | 0.0009 | 0.0247 | -0.0238 | 0.1341 | 0.1490 |
84	| True_medium | 0.3 | 1 | 0.0134 | 0.0113 | +0.0021 | 0.0824 | 0.0931 |
85	| True_short | 0.6 | 0 | 0.0583 | 0.0332 | +0.0251 | 0.2253 | 0.2858 |
86	| True_short | 0.6 | 1 | 0.0057 | 0.0059 | -0.0002 | 0.1273 | 0.1650 |
87	
88	### n_expert = 1000
89	
90	| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |
91	|----------|-----|---|-------------|-------------|-------------|-------------|------------|
92	| False_medium | 0.1 | 0 | 0.0185 | 0.0072 | +0.0113 | 0.1266 | 0.1819 |
93	| False_medium | 0.1 | 1 | 0.0025 | 0.0045 | -0.0020 | 0.0804 | 0.0948 |
94	| False_short | 0.1 | 0 | 0.0199 | 0.0183 | +0.0017 | 0.1743 | 0.1971 |
95	| False_short | 0.1 | 1 | 0.0032 | 0.0022 | +0.0011 | 0.1098 | 0.1216 |
96	| True_medium | 0.3 | 0 | 0.0009 | 0.0318 | -0.0309 | 0.1343 | 0.1349 |
97	| True_medium | 0.3 | 1 | 0.0116 | 0.0045 | +0.0071 | 0.0807 | 0.0749 |
98	| True_short | 0.6 | 0 | 0.0592 | 0.0384 | +0.0208 | 0.2181 | 0.2055 |
99	| True_short | 0.6 | 1 | 0.0081 | 0.0186 | -0.0105 | 0.1237 | 0.1372 |
100	
101	## Bias-Variance Decomposition
102	
103	| n_expert | Method | Bias² | Variance | MSE |
104	|----------|--------|-------|----------|-----|
105	| 200 | Naive | 0.0078 | 0.0072 | 0.0150 |
106	| 200 | Global | 0.0012 | 0.0239 | 0.0251 |
107	| 200 | Strat MLE | 0.0009 | 0.0919 | 0.0928 |
108	| 200 | HB EC-HTE | 0.0012 | 0.0840 | 0.0852 |
109	| 500 | Naive | 0.0078 | 0.0072 | 0.0150 |
110	| 500 | Global | 0.0005 | 0.0202 | 0.0207 |
111	| 500 | Strat MLE | 0.0005 | 0.0350 | 0.0355 |
112	| 500 | HB EC-HTE | 0.0003 | 0.0344 | 0.0347 |
113	| 1000 | Naive | 0.0078 | 0.0072 | 0.0150 |
114	| 1000 | Global | 0.0006 | 0.0189 | 0.0194 |
115	| 1000 | Strat MLE | 0.0005 | 0.0228 | 0.0233 |
116	| 1000 | HB EC-HTE | 0.0004 | 0.0226 | 0.0230 |
117	
118	## Cross-Model Comparison: Gemma vs Qwen vs Llama
119	
120	### CM Heterogeneity
121	
122	| Metric | Gemma-2-9B | Qwen2.5-7B | Llama3.1-8B |
123	|--------|-----------|-----------|------------|
124	| Δ_FPR (max-min) | 0.1046 | 0.2410 | 0.2190 |
125	| Δ_FNR (max-min) | 0.2299 | 0.1490 | 0.1290 |
126	| Mean Δ_error | 0.1673 | 0.1950 | 0.1740 |
127	
128	### Bias Comparison
129	
130	| n_expert | Gemma |Bias|_Global | Gemma |Bias|_ECHTE | Gemma Δ|Bias| | Qwen |Bias|_Global | Qwen |Bias|_ECHTE | Qwen Δ|Bias| | Llama |Bias|_Global | Llama |Bias|_ECHTE | Llama Δ|Bias| |
131	|----------|------------------|--------------------|--------------|--------------------|--------------------|--------------|--------------------|--------------------|--------------| 
132	| 200 | 0.0261 | 0.0269 | -0.0008 | 0.0368 | 0.0275 | +0.0093 | 0.0365 | 0.0248 | +0.0117 |
133	| 500 | 0.0153 | 0.0117 | +0.0036 | 0.0336 | 0.0196 | +0.0140 | 0.0314 | 0.0099 | +0.0215 |
134	| 1000 | 0.0155 | 0.0157 | -0.0002 | 0.0328 | 0.0165 | +0.0163 | 0.0286 | 0.0130 | +0.0156 |
135	
136	### RMSE Comparison
137	
138	| n_expert | Gemma RMSE_Global | Gemma RMSE_ECHTE | Qwen RMSE_Global | Qwen RMSE_ECHTE | Llama RMSE_Global | Llama RMSE_ECHTE |
139	|----------|-----------------|----------------|-----------------|----------------|------------------|-----------------|
140	| 200 | 0.1498 | 0.2614 | 0.1546 | 0.2293 | 0.1780 | 0.2606 |
141	| 500 | 0.1353 | 0.1741 | 0.1362 | 0.1631 | 0.1580 | 0.1760 |
142	| 1000 | 0.1310 | 0.1435 | 0.1314 | 0.1393 | 0.1554 | 0.1602 |
143	
144	## Conclusion
145	
146	EC-HTE wins on |Bias| in 1/3 budget levels.
147	EC-HTE wins on RMSE in 0/3 budget levels.
148	
149	**Result: Under heterogeneous-τ DGP with Gemma-2-9B CMs, EC-HTE outperforms Global in bias at 1 of 3 budget levels.**
150	
151	**Cross-model consistency**: Llama EC-HTE wins on bias in 3/3 budgets; Qwen EC-HTE wins in 3/3 budgets; Gemma EC-HTE wins in 1/3 budgets.
152	
153	Average Δ|Bias| (Global - EC-HTE): Gemma = +0.0009, Qwen = +0.0132, Llama = +0.0163
154	Ranking by EC-HTE improvement: Llama > Qwen > Gemma
155	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "ddbd20d2-77c7-4761-a7a7-57d111e97727",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/gemma_hetero_tau_analysis.md",
      "content": "# Gemma-2-9B Heterogeneous-τ DGP: EC-HTE vs Global Correction\n\n## Design\n\n- N=5000, P(Z=1)=0.652, K=4 subgroups\n- **LLM**: Gemma-2-9B (balanced binarization)\n- **Heterogeneous τ(z) across subgroups:**\n  - False_medium: τ(z=0)=0.45, τ(z=1)=0.55, Δτ=0.1\n  - False_short: τ(z=0)=0.4, τ(z=1)=0.5, Δτ=0.1\n  - True_medium: τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3\n  - True_short: τ(z=0)=0.2, τ(z=1)=0.8, Δτ=0.6\n- n_expert sweep: [200, 500, 1000]\n- 50 MC seeds per budget\n- HB method: MAP-EB (Gamma(3,1) prior)\n- |Bias| = avg across cells of |mean(bias) across seeds|\n- RMSE = avg across cells of sqrt(mean(bias²) across seeds)\n\n## Gemma-2-9B Per-Subgroup Confusion Matrix\n\n| Subgroup | π_s | FPR | FNR | 1-FPR-FNR |\n|----------|-----|-----|-----|-----------|\n| False_medium | 0.3816 | 0.1100 | 0.4368 | 0.4532 |\n| False_short | 0.2224 | 0.1379 | 0.3000 | 0.5621 |\n| True_medium | 0.2551 | 0.0333 | 0.2632 | 0.7035 |\n| True_short | 0.1408 | 0.0909 | 0.2069 | 0.7022 |\n\n- Gemma Δ_FPR = 0.1046, Δ_FNR = 0.2299\n- Qwen Δ_FPR = 0.2410, Δ_FNR = 0.1490\n- Llama Δ_FPR = 0.2190, Δ_FNR = 0.1290\n- **Note**: Gemma has strong FNR>FPR asymmetry (False_medium FNR=0.437 most extreme)\n\n## Summary Table (averaged across all cells)\n\n| n_expert | Method | |Bias| | RMSE | Coverage | CI Width |\n|----------|--------|-------|------|----------|----------|\n| 200 | Naive | 0.0598 | 0.1101 | 0.873 | 0.332 |\n| 200 | Global | 0.0261 | 0.1498 | 0.927 | 0.525 |\n| 200 | Strat MLE | 0.0263 | 0.2708 | 0.802 | 0.575 |\n| 200 | HB EC-HTE | 0.0269 | 0.2614 | 0.807 | 0.562 |\n|----------|--------|-------|------|----------|----------|\n| 500 | Naive | 0.0598 | 0.1101 | 0.873 | 0.332 |\n| 500 | Global | 0.0153 | 0.1353 | 0.948 | 0.514 |\n| 500 | Strat MLE | 0.0156 | 0.1760 | 0.877 | 0.519 |\n| 500 | HB EC-HTE | 0.0117 | 0.1741 | 0.873 | 0.515 |\n|----------|--------|-------|------|----------|----------|\n| 1000 | Naive | 0.0598 | 0.1101 | 0.873 | 0.332 |\n| 1000 | Global | 0.0155 | 0.1310 | 0.950 | 0.513 |\n| 1000 | Strat MLE | 0.0169 | 0.1444 | 0.910 | 0.505 |\n| 1000 | HB EC-HTE | 0.0157 | 0.1435 | 0.915 | 0.503 |\n|----------|--------|-------|------|----------|----------|\n\n## EC-HTE vs Global Comparison\n\n| n_expert | |Bias|_Global | |Bias|_ECHTE | Δ|Bias| | RMSE_Global | RMSE_ECHTE | ΔRMSE | HB_wins_bias? | HB_wins_rmse? |\n|----------|-------------|-------------|---------|-------------|------------|-------|---------------|---------------|\n| 200 | 0.0261 | 0.0269 | -0.0008 | 0.1498 | 0.2614 | -0.1116 | no | no |\n| 500 | 0.0153 | 0.0117 | +0.0036 | 0.1353 | 0.1741 | -0.0388 | **YES** | no |\n| 1000 | 0.0155 | 0.0157 | -0.0002 | 0.1310 | 0.1435 | -0.0125 | no | no |\n\n## Per-Subgroup Breakdown\n\n### n_expert = 200\n\n| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |\n|----------|-----|---|-------------|-------------|-------------|-------------|------------|\n| False_medium | 0.1 | 0 | 0.0049 | 0.0374 | -0.0325 | 0.1549 | 0.2857 |\n| False_medium | 0.1 | 1 | 0.0158 | 0.0342 | -0.0185 | 0.0974 | 0.1584 |\n| False_short | 0.1 | 0 | 0.0299 | 0.0112 | +0.0186 | 0.2069 | 0.3273 |\n| False_short | 0.1 | 1 | 0.0094 | 0.0158 | -0.0064 | 0.1176 | 0.1720 |\n| True_medium | 0.3 | 0 | 0.0213 | 0.0034 | +0.0178 | 0.1556 | 0.1811 |\n| True_medium | 0.3 | 1 | 0.0297 | 0.0430 | -0.0133 | 0.0945 | 0.1278 |\n| True_short | 0.6 | 0 | 0.0827 | 0.0011 | +0.0815 | 0.2345 | 0.5282 |\n| True_short | 0.6 | 1 | 0.0151 | 0.0688 | -0.0538 | 0.1368 | 0.3107 |\n\n### n_expert = 500\n\n| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |\n|----------|-----|---|-------------|-------------|-------------|-------------|------------|\n| False_medium | 0.1 | 0 | 0.0186 | 0.0031 | +0.0155 | 0.1369 | 0.2157 |\n| False_medium | 0.1 | 1 | 0.0036 | 0.0125 | -0.0089 | 0.0870 | 0.1200 |\n| False_short | 0.1 | 0 | 0.0194 | 0.0023 | +0.0171 | 0.1809 | 0.2303 |\n| False_short | 0.1 | 1 | 0.0026 | 0.0008 | +0.0018 | 0.1087 | 0.1344 |\n| True_medium | 0.3 | 0 | 0.0009 | 0.0247 | -0.0238 | 0.1341 | 0.1490 |\n| True_medium | 0.3 | 1 | 0.0134 | 0.0113 | +0.0021 | 0.0824 | 0.0931 |\n| True_short | 0.6 | 0 | 0.0583 | 0.0332 | +0.0251 | 0.2253 | 0.2858 |\n| True_short | 0.6 | 1 | 0.0057 | 0.0059 | -0.0002 | 0.1273 | 0.1650 |\n\n### n_expert = 1000\n\n| Subgroup | Δτ | z | |Bias|_Global | |Bias|_ECHTE | Improvement | RMSE_Global | RMSE_ECHTE |\n|----------|-----|---|-------------|-------------|-------------|-------------|------------|\n| False_medium | 0.1 | 0 | 0.0185 | 0.0072 | +0.0113 | 0.1266 | 0.1819 |\n| False_medium | 0.1 | 1 | 0.0025 | 0.0045 | -0.0020 | 0.0804 | 0.0948 |\n| False_short | 0.1 | 0 | 0.0199 | 0.0183 | +0.0017 | 0.1743 | 0.1971 |\n| False_short | 0.1 | 1 | 0.0032 | 0.0022 | +0.0011 | 0.1098 | 0.1216 |\n| True_medium | 0.3 | 0 | 0.0009 | 0.0318 | -0.0309 | 0.1343 | 0.1349 |\n| True_medium | 0.3 | 1 | 0.0116 | 0.0045 | +0.0071 | 0.0807 | 0.0749 |\n| True_short | 0.6 | 0 | 0.0592 | 0.0384 | +0.0208 | 0.2181 | 0.2055 |\n| True_short | 0.6 | 1 | 0.0081 | 0.0186 | -0.0105 | 0.1237 | 0.1372 |\n\n## Bias-Variance Decomposition\n\n| n_expert | Method | Bias² | Variance | MSE |\n|----------|--------|-------|----------|-----|\n| 200 | Naive | 0.0078 | 0.0072 | 0.0150 |\n| 200 | Global | 0.0012 | 0.0239 | 0.0251 |\n| 200 | Strat MLE | 0.0009 | 0.0919 | 0.0928 |\n| 200 | HB EC-HTE | 0.0012 | 0.0840 | 0.0852 |\n| 500 | Naive | 0.0078 | 0.0072 | 0.0150 |\n| 500 | Global | 0.0005 | 0.0202 | 0.0207 |\n| 500 | Strat MLE | 0.0005 | 0.0350 | 0.0355 |\n| 500 | HB EC-HTE | 0.0003 | 0.0344 | 0.0347 |\n| 1000 | Naive | 0.0078 | 0.0072 | 0.0150 |\n| 1000 | Global | 0.0006 | 0.0189 | 0.0194 |\n| 1000 | Strat MLE | 0.0005 | 0.0228 | 0.0233 |\n| 1000 | HB EC-HTE | 0.0004 | 0.0226 | 0.0230 |\n\n## Cross-Model Comparison: Gemma vs Qwen vs Llama\n\n### CM Heterogeneity\n\n| Metric | Gemma-2-9B | Qwen2.5-7B | Llama3.1-8B |\n|--------|-----------|-----------|------------|\n| Δ_FPR (max-min) | 0.1046 | 0.2410 | 0.2190 |\n| Δ_FNR (max-min) | 0.2299 | 0.1490 | 0.1290 |\n| Mean Δ_error | 0.1673 | 0.1950 | 0.1740 |\n\n### Bias Comparison\n\n| n_expert | Gemma |Bias|_Global | Gemma |Bias|_ECHTE | Gemma Δ|Bias| | Qwen |Bias|_Global | Qwen |Bias|_ECHTE | Qwen Δ|Bias| | Llama |Bias|_Global | Llama |Bias|_ECHTE | Llama Δ|Bias| |\n|----------|------------------|--------------------|--------------|--------------------|--------------------|--------------|--------------------|--------------------|--------------| \n| 200 | 0.0261 | 0.0269 | -0.0008 | 0.0368 | 0.0275 | +0.0093 | 0.0365 | 0.0248 | +0.0117 |\n| 500 | 0.0153 | 0.0117 | +0.0036 | 0.0336 | 0.0196 | +0.0140 | 0.0314 | 0.0099 | +0.0215 |\n| 1000 | 0.0155 | 0.0157 | -0.0002 | 0.0328 | 0.0165 | +0.0163 | 0.0286 | 0.0130 | +0.0156 |\n\n### RMSE Comparison\n\n| n_expert | Gemma RMSE_Global | Gemma RMSE_ECHTE | Qwen RMSE_Global | Qwen RMSE_ECHTE | Llama RMSE_Global | Llama RMSE_ECHTE |\n|----------|-----------------|----------------|-----------------|----------------|------------------|-----------------|\n| 200 | 0.1498 | 0.2614 | 0.1546 | 0.2293 | 0.1780 | 0.2606 |\n| 500 | 0.1353 | 0.1741 | 0.1362 | 0.1631 | 0.1580 | 0.1760 |\n| 1000 | 0.1310 | 0.1435 | 0.1314 | 0.1393 | 0.1554 | 0.1602 |\n\n## Conclusion\n\nEC-HTE wins on |Bias| in 1/3 budget levels.\nEC-HTE wins on RMSE in 0/3 budget levels.\n\n**Result: Under heterogeneous-τ DGP with Gemma-2-9B CMs, EC-HTE outperforms Global in bias at 1 of 3 budget levels.**\n\n**Cross-model consistency**: Llama EC-HTE wins on bias in 3/3 budgets; Qwen EC-HTE wins in 3/3 budgets; Gemma EC-HTE wins in 1/3 budgets.\n\nAverage Δ|Bias| (Global - EC-HTE): Gemma = +0.0009, Qwen = +0.0132, Llama = +0.0163\nRanking by EC-HTE improvement: Llama > Qwen > Gemma\n",
      "numLines": 155,
      "startLine": 1,
      "totalLines": 155
    }
  }
}
```

</details>

---

### Assistant

_source line 47_

All done. Results:

- **CSV**: `gemma_hetero_tau_results.csv` — 4801 lines (4800 data + 1 header), matches expected count
- **Analysis**: `gemma_hetero_tau_analysis.md` — full report with all sections

**Key findings for Gemma-2-9B**:

| n_expert | |Bias| Global | |Bias| EC-HTE | Winner |
|----------|-------------|-------------|--------|
| 200 | 0.0261 | 0.0269 | Global |
| 500 | 0.0153 | 0.0117 | **EC-HTE** |
| 1000 | 0.0155 | 0.0157 | Global |

EC-HTE wins bias in only **1/3** budgets (n=500), vs 3/3 for both Llama and Qwen. Gemma's CM profile is quite different — small FPR heterogeneity (Δ_FPR=0.10) but large FNR heterogeneity (Δ_FNR=0.23), with strong FNR>FPR asymmetry. This means Global correction is already relatively accurate for Gemma, leaving less room for EC-HTE's subgroup-specific correction to improve on. Average Δ|Bias| improvement ranking: Llama (+0.016) > Qwen (+0.013) > Gemma (+0.001).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "uuid": "b926099d-77f4-4bba-b74b-917ee37a53f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017jLSxKZVuZyC3P8bD2AMgk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4973,
      "cache_read_input_tokens": 55829,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4973
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

_source line 48_

All done. Results:

- **CSV**: `gemma_hetero_tau_results.csv` — 4801 lines (4800 data + 1 header), matches expected count
- **Analysis**: `gemma_hetero_tau_analysis.md` — full report with all sections

**Key findings for Gemma-2-9B**:

| n_expert | |Bias| Global | |Bias| EC-HTE | Winner |
|----------|-------------|-------------|--------|
| 200 | 0.0261 | 0.0269 | Global |
| 500 | 0.0153 | 0.0117 | **EC-HTE** |
| 1000 | 0.0155 | 0.0157 | Global |

EC-HTE wins bias in only **1/3** budgets (n=500), vs 3/3 for both Llama and Qwen. Gemma's CM profile is quite different — small FPR heterogeneity (Δ_FPR=0.10) but large FNR heterogeneity (Δ_FNR=0.23), with strong FNR>FPR asymmetry. This means Global correction is already relatively accurate for Gemma, leaving less room for EC-HTE's subgroup-specific correction to improve on. Average Δ|Bias| improvement ranking: Llama (+0.016) > Qwen (+0.013) > Gemma (+0.001).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 261999,
  "duration_api_ms": 258972,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "265369f3-c779-4bbc-a398-b2ef39f644e0",
  "total_cost_usd": 0.89533325,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 48961,
    "cache_read_input_tokens": 265901,
    "output_tokens": 14685,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 48961,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 361,
        "cache_read_input_tokens": 55829,
        "cache_creation_input_tokens": 4973,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4973
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1677,
      "outputTokens": 8531,
      "cacheReadInputTokens": 92495,
      "cacheCreationInputTokens": 28500,
      "webSearchRequests": 0,
      "costUSD": 0.0892065,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 14685,
      "cacheReadInputTokens": 265901,
      "cacheCreationInputTokens": 48961,
      "webSearchRequests": 0,
      "costUSD": 0.80612675,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f167b797-ce3a-487b-926c-9a0e2094ab4c"
}
```

</details>

---
