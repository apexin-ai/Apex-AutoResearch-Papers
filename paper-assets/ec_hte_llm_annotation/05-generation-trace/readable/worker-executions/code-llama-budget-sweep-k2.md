# code llama budget sweep k2

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_code_llama-budget-sweep-k2_20260521T212758.log`
- **Structured JSON:** [`356d2eb5ec684b8a39a5.json`](../../sessions/35/356d2eb5ec684b8a39a5.json)

## Before a recorded user message

26 recorded events

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
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
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
  "uuid": "b0bb73b9-6506-404b-942f-fecc0bafbd39",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu-ec-hte-llm-annotation/memory/"
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
    "resetsAt": 1779414600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "bed14a98-00c8-4500-86e0-9f09dc280c02",
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199"
}
```

---

### Assistant

_source line 4_

I'll start by reading the base script to understand the structure, then modify it for the K=2 budget sweep.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "uuid": "ccbc2c23-9a9b-4432-96b0-e8e4a94a55ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XBg2hLV2yQ5TkNtvTax63k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6592,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6592
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

<details open><summary>🔧 Tool call — Read · `toolu_01RnH1kQu6qknmsgwMzbE8Sr`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_llama_semisynthetic.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "uuid": "376093ac-6c76-4537-bdec-10914004db74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XBg2hLV2yQ5TkNtvTax63k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6592,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6592
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

_source line 6 · 2026-05-21T21:28:10.908Z_

<details><summary>↩ Tool result · `toolu_01RnH1kQu6qknmsgwMzbE8Sr`</summary>

```text
1	"""
2	Llama-3.1-8B Semi-Synthetic DGP: EC-HTE vs Global vs Naive RMSE comparison.
3	
4	Uses real per-subgroup confusion matrices from Llama-3.1-8B balanced annotations.
5	Ground truth CATE is synthetic; confusion matrices are empirical.
6	
7	4 subgroups with real asymmetric CMs:
8	  False_medium: FPR=0.235, FNR=0.319, weight=193/500
9	  False_short:  FPR=0.310, FNR=0.212, weight=109/500
10	  True_medium:  FPR=0.219, FNR=0.258, weight=129/500
11	  True_short:   FPR=0.091, FNR=0.190, weight=69/500
12	
13	P(Z=1) = 0.652, delta_tau = 0.3, tau(z=0)=0.35, tau(z=1)=0.65
14	Methods: Naive, Global, Stratified MLE, HB EC-HTE
15	n_expert=200, 20 MC seeds
16	
17	Usage: python3 artifacts/c1_multi_llm/run_llama_semisynthetic.py
18	"""
19	
20	import time
21	import warnings
22	import numpy as np
23	import pandas as pd
24	from scipy.special import gammaln
25	
26	warnings.filterwarnings('ignore')
27	
28	# === Config ===
29	
30	N = 5000
31	N_EXPERT = 200
32	N_MC = 20
33	SEED_BASE = 0
34	
35	SUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']
36	SUBGROUP_WEIGHTS = np.array([193, 109, 129, 69], dtype=float)
37	SUBGROUP_WEIGHTS /= SUBGROUP_WEIGHTS.sum()
38	
39	SUBGROUP_CM = {
40	    'False_medium': {'fpr': 0.235, 'fnr': 0.319},
41	    'False_short':  {'fpr': 0.310, 'fnr': 0.212},
42	    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},
43	    'True_short':   {'fpr': 0.091, 'fnr': 0.190},
44	}
45	
46	P_Z1 = 0.652
47	P_T1 = 0.5
48	TAU_Z0 = 0.35
49	TAU_Z1 = 0.65
50	
51	
52	def get_cm_matrix(fpr, fnr):
53	    """Build 2x2 confusion matrix: C[z_true, z_obs]."""
54	    return np.array([[1 - fpr, fpr],
55	                     [fnr, 1 - fnr]])
56	
57	
58	# === Core Estimators ===
59	
60	def diff_in_means(Y, T, mask):
61	    t1 = mask & (T == 1)
62	    t0 = mask & (T == 0)
63	    n1, n0 = t1.sum(), t0.sum()
64	    if n1 < 2 or n0 < 2:
65	        return np.nan, np.nan
66	    y1, y0 = Y[t1], Y[t0]
67	    tau_hat = y1.mean() - y0.mean()
68	    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
69	    return tau_hat, se
70	
71	
72	def estimate_confusion_matrix(z_true, z_hat):
73	    """Global CM with Laplace smoothing."""
74	    C = np.zeros((2, 2))
75	    for zt in [0, 1]:
76	        mask = z_true == zt
77	        n = mask.sum()
78	        for zh in [0, 1]:
79	            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
80	    return C
81	
82	
83	def estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):
84	    """Per-subgroup MLE with Laplace smoothing."""
85	    C = {}
86	    for s in labels:
87	        ms = subgroups == s
88	        C_s = np.zeros((2, 2))
89	        for zt in [0, 1]:
90	            mask = ms & (z_true == zt)
91	            n = mask.sum()
92	            for zh in [0, 1]:
93	                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
94	        C[s] = C_s
95	    return C
96	
97	
98	def build_mixing_matrix(C, p_z, p_z_hat):
99	    """M[z_hat, z] = P(Z=z | Z_hat=z_hat) via Bayes' rule."""
100	    M = np.zeros((2, 2))
101	    for zh in [0, 1]:
102	        for z in [0, 1]:
103	            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5
104	    return M
105	
106	
107	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
108	    cond = np.linalg.cond(M)
109	    if cond > cond_threshold:
110	        return tau_obs.copy(), se_obs.copy()
111	    det = np.linalg.det(M)
112	    if abs(det) < 1e-10:
113	        return tau_obs.copy(), se_obs.copy()
114	    Mi = np.linalg.inv(M)
115	    tau_c = Mi @ tau_obs
116	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
117	    return tau_c, se_c
118	
119	
120	# === HB Gibbs Sampler ===
121	
122	def get_counts(z_true, z_hat, subgroups, labels):
123	    k = len(labels)
124	    counts = np.zeros((k, 2, 2), dtype=int)
125	    for i, s in enumerate(labels):
126	        ms = subgroups == s
127	        for z in [0, 1]:
128	            mz = ms & (z_true == z)
129	            counts[i, z, 0] = (z_hat[mz] == 0).sum()
130	            counts[i, z, 1] = (z_hat[mz] == 1).sum()
131	    return counts
132	
133	
134	def _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):
135	    if alpha < 1e-10:
136	        return -1e10
137	    a = alpha / 2.0
138	    k = theta_z.shape[0]
139	    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha
140	    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))
141	    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))
142	    return lp
143	
144	
145	def estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=1000, n_warmup=500, n_chains=4,
146	                         hp_a0=3.0, hp_b0=1.0):
147	    k = len(labels)
148	    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),
149	                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]
150	    chain_inits = chain_inits_pool[:n_chains]
151	    all_theta = []
152	    t0 = time.time()
153	
154	    for chain in range(n_chains):
155	        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)
156	        alpha = chain_inits[chain].copy()
157	        theta = np.ones((k, 2, 2)) * 0.5
158	        mh_scale = np.array([0.3, 0.3])
159	        accept_ct = np.array([0, 0])
160	        attempt_ct = np.array([0, 0])
161	
162	        theta_samples = np.zeros((n_iter, k, 2, 2))
163	
164	        for it in range(n_warmup + n_iter):
165	            for z in [0, 1]:
166	                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0
167	                post_a = np.maximum(post_a, 1e-6)
168	                g = rng.gamma(post_a)
169	                g_sum = g.sum(axis=1, keepdims=True)
170	                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)
171	
172	            for z in [0, 1]:
173	                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])
174	                a_prop = np.exp(x_prop)
175	                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -
176	                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))
177	                accepted = np.log(rng.rand()) < log_r
178	                if accepted:
179	                    alpha[z] = a_prop
180	                if it < n_warmup:
181	                    accept_ct[z] += int(accepted)
182	                    attempt_ct[z] += 1
183	
184	            if it < n_warmup and it > 0 and it % 100 == 0:
185	                for z in [0, 1]:
186	                    rate = accept_ct[z] / max(attempt_ct[z], 1)
187	                    if rate < 0.2:
188	                        mh_scale[z] *= 0.7
189	                    elif rate > 0.5:
190	                        mh_scale[z] *= 1.3
191	                    accept_ct[z] = 0
192	                    attempt_ct[z] = 0
193	
194	            if it >= n_warmup:
195	                theta_samples[it - n_warmup] = theta.copy()
196	
197	        all_theta.append(theta_samples)
198	
199	    runtime = time.time() - t0
200	    theta_arr = np.stack(all_theta)
201	
202	    C = {}
203	    for i, s in enumerate(labels):
204	        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))
205	
206	    return C, {'runtime_seconds': runtime}
207	
208	
209	# === DGP ===
210	
211	def generate_data(seed):
212	    rng = np.random.RandomState(seed)
213	
214	    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)
215	    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])
216	
217	    Z = rng.binomial(1, P_Z1, N)
218	    T = rng.binomial(1, P_T1, N)
219	
220	    Z_hat = np.empty(N, dtype=int)
221	    for i in range(4):
222	        s_mask = S_idx == i
223	        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],
224	                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])
225	        z_s = Z[s_mask]
226	        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])
227	        Z_hat[s_mask] = rng.binomial(1, p_obs1)
228	
229	    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)
230	    eps = rng.randn(N)
231	    Y = 1.0 + tau_vals * T + eps
232	
233	    expert_idx = rng.choice(N, N_EXPERT, replace=False)
234	    expert_mask = np.zeros(N, dtype=bool)
235	    expert_mask[expert_idx] = True
236	
237	    return {
238	        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,
239	        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,
240	    }
241	
242	
243	# === MC Runner ===
244	
245	def run_one_mc(data, seed):
246	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
247	    expert_mask = data['expert_mask']
248	
249	    z_exp = Z[expert_mask]
250	    zh_exp = Z_hat[expert_mask]
251	    s_exp = S[expert_mask]
252	
253	    # Global CM from experts
254	    C_global = estimate_confusion_matrix(z_exp, zh_exp)
255	    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])
256	    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])
257	    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)
258	
259	    # Stratified MLE per-subgroup
260	    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)
261	
262	    # HB Gibbs
263	    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)
264	    C_hb, _ = estimate_cm_hb_gibbs(counts, SUBGROUP_LABELS, seed=seed)
265	
266	    # Build per-subgroup mixing matrices
267	    M_mle_sub = {}
268	    M_hb_sub = {}
269	    for s_val in SUBGROUP_LABELS:
270	        sm_exp = (s_exp == s_val)
271	        sm_all = (S == s_val)
272	        if sm_exp.sum() >= 4:
273	            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])
274	        else:
275	            p_z_s = p_z_global
276	        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])
277	        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)
278	        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)
279	
280	    rows = []
281	
282	    for s_val in SUBGROUP_LABELS:
283	        s_mask = S == s_val
284	
285	        for z_level in [0, 1]:
286	            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0
287	
288	            # Oracle
289	            th_or, se_or = diff_in_means(Y, T, s_mask & (Z == z_level))
290	            ci_lo_or = th_or - 1.96 * se_or if not np.isnan(se_or) else np.nan
291	            ci_hi_or = th_or + 1.96 * se_or if not np.isnan(se_or) else np.nan
292	            cov_or = 1 if (not np.isnan(ci_lo_or) and ci_lo_or <= oracle_cate <= ci_hi_or) else 0
293	            rows.append({
294	                'seed': seed, 'method': 'oracle', 'subgroup': s_val,
295	                'z_level': z_level,
296	                'bias': th_or - oracle_cate if not np.isnan(th_or) else np.nan,
297	                'rmse': abs(th_or - oracle_cate) if not np.isnan(th_or) else np.nan,
298	                'coverage': cov_or,
299	                'cate_true': oracle_cate, 'cate_est': th_or,
300	            })
301	
302	            # Naive
303	            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))
304	            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan
305	            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan
306	            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0
307	            rows.append({
308	                'seed': seed, 'method': 'naive', 'subgroup': s_val,
309	                'z_level': z_level,
310	                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,
311	                'rmse': abs(th_nv - oracle_cate) if not np.isnan(th_nv) else np.nan,
312	                'coverage': cov_nv,
313	                'cate_true': oracle_cate, 'cate_est': th_nv,
314	            })
315	
316	            # Observed CATE in Z_hat=0 and Z_hat=1 cells for this subgroup
317	            tau_obs = np.array([
318	                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],
319	                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],
320	            ])
321	            se_obs = np.array([
322	                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],
323	                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],
324	            ])
325	
326	            if not np.any(np.isnan(tau_obs)):
327	                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)
328	                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]
329	
330	                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)
331	                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]
332	
333	                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)
334	                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]
335	            else:
336	                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan
337	
338	            # Global corrected
339	            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan
340	            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan
341	            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0
342	            rows.append({
343	                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,
344	                'z_level': z_level,
345	                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,
346	                'rmse': abs(th_gc - oracle_cate) if not np.isnan(th_gc) else np.nan,
347	                'coverage': cov_gc,
348	                'cate_true': oracle_cate, 'cate_est': th_gc,
349	            })
350	
351	            # Stratified MLE
352	            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan
353	            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan
354	            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0
355	            rows.append({
356	                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,
357	                'z_level': z_level,
358	                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,
359	                'rmse': abs(th_ml - oracle_cate) if not np.isnan(th_ml) else np.nan,
360	                'coverage': cov_ml,
361	                'cate_true': oracle_cate, 'cate_est': th_ml,
362	            })
363	
364	            # HB EC-HTE
365	            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan
366	            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan
367	            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0
368	            rows.append({
369	                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,
370	                'z_level': z_level,
371	                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,
372	                'rmse': abs(th_hb - oracle_cate) if not np.isnan(th_hb) else np.nan,
373	                'coverage': cov_hb,
374	                'cate_true': oracle_cate, 'cate_est': th_hb,
375	            })
376	
377	    return rows
378	
379	
380	# === Aggregation ===
381	
382	def aggregate_results(df_raw):
383	    group_cols = ['subgroup', 'z_level', 'method']
384	    rows = []
385	    for keys, grp in df_raw.groupby(group_cols):
386	        row = dict(zip(group_cols, keys))
387	        valid = grp['bias'].dropna()
388	        if len(valid) == 0:
389	            continue
390	        row['mean_bias'] = valid.mean()
391	        row['mean_abs_bias'] = valid.abs().mean()
392	        row['rmse'] = np.sqrt((valid ** 2).mean())
393	        row['coverage'] = grp['coverage'].mean()
394	        row['n_mc'] = len(valid)
395	        rows.append(row)
396	    return pd.DataFrame(rows)
397	
398	
399	# === Analysis Report ===
400	
401	def write_analysis(df_raw, df_summary):
402	    lines = []
403	    lines.append("# Llama-3.1-8B Semi-Synthetic EC-HTE Experiment\n")
404	
405	    lines.append("## Design\n")
406	    lines.append("Uses **real asymmetric confusion matrices** from Llama-3.1-8B balanced annotations.")
407	    lines.append("Ground truth CATE is synthetic; confusion matrices are empirical.\n")
408	
409	    lines.append("| Subgroup | Weight | FPR | FNR | pi_s |")
410	    lines.append("|----------|--------|-----|-----|------|")
411	    for i, s in enumerate(SUBGROUP_LABELS):
412	        cm = SUBGROUP_CM[s]
413	        lines.append(f"| {s} | {SUBGROUP_WEIGHTS[i]:.3f} | {cm['fpr']:.3f} | {cm['fnr']:.3f} | {(cm['fpr'] + cm['fnr'])/2:.3f} |")
414	    lines.append("")
415	
416	    lines.append(f"**Parameters**: N={N}, P(Z=1)={P_Z1}, n_expert={N_EXPERT}, "
417	                 f"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1-TAU_Z0:.1f}")
418	    lines.append(f"**MC seeds**: {N_MC}\n")
419	
420	    # Overall summary
421	    lines.append("## Summary (averaged across subgroups and z-levels)\n")
422	    lines.append("| Method | Mean |Bias| | RMSE | Coverage |")
423	    lines.append("|--------|-------------|------|----------|")
424	    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:
425	        sub = df_summary[df_summary['method'] == m]
426	        if len(sub) > 0:
427	            lines.append(f"| {m} | {sub['mean_abs_bias'].mean():.4f} | "
428	                         f"{sub['rmse'].mean():.4f} | {sub['coverage'].mean():.3f} |")
429	    lines.append("")
430	
431	    # Per-subgroup breakdown
432	    lines.append("## Per-Subgroup Breakdown\n")
433	    lines.append("| Subgroup | Z | Method | Mean Bias | |Bias| | RMSE | Coverage |")
434	    lines.append("|----------|---|--------|-----------|-------|------|----------|")
435	    for s in SUBGROUP_LABELS:
436	        for z in [0, 1]:
437	            for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:
438	                row = df_summary[(df_summary['subgroup'] == s) &
439	                                 (df_summary['z_level'] == z) &
440	                                 (df_summary['method'] == m)]
441	                if len(row) > 0:
442	                    r = row.iloc[0]
443	                    lines.append(f"| {s} | {z} | {m} | {r['mean_bias']:+.4f} | "
444	                                 f"{r['mean_abs_bias']:.4f} | {r['rmse']:.4f} | {r['coverage']:.3f} |")
445	    lines.append("")
446	
447	    # EC-HTE vs Global bias reduction
448	    lines.append("## EC-HTE vs Global: Bias Reduction Ratio\n")
449	    lines.append("| Subgroup | Z | HB |Bias| | Global |Bias| | Reduction |")
450	    lines.append("|----------|---|-----------|-------------|-----------|")
451	    total_hb, total_gc = 0.0, 0.0
452	    n_cells = 0
453	    for s in SUBGROUP_LABELS:
454	        for z in [0, 1]:
455	            hb = df_summary[(df_summary['subgroup'] == s) & (df_summary['z_level'] == z) &
456	                            (df_summary['method'] == 'hb_ec_hte')]
457	            gc = df_summary[(df_summary['subgroup'] == s) & (df_summary['z_level'] == z) &
458	                            (df_summary['method'] == 'global_corrected')]
459	            if len(hb) > 0 and len(gc) > 0:
460	                hb_b = hb.iloc[0]['mean_abs_bias']
461	                gc_b = gc.iloc[0]['mean_abs_bias']
462	                red = (gc_b - hb_b) / gc_b * 100 if gc_b > 1e-6 else 0
463	                lines.append(f"| {s} | {z} | {hb_b:.4f} | {gc_b:.4f} | {red:+.1f}% |")
464	                total_hb += hb_b
465	                total_gc += gc_b
466	                n_cells += 1
467	    if n_cells > 0:
468	        avg_red = (total_gc / n_cells - total_hb / n_cells) / (total_gc / n_cells) * 100
469	        lines.append(f"| **Average** | | {total_hb/n_cells:.4f} | {total_gc/n_cells:.4f} | {avg_red:+.1f}% |")
470	    lines.append("")
471	
472	    # Conclusion
473	    lines.append("## Conclusion\n")
474	
475	    hb_all = df_summary[df_summary['method'] == 'hb_ec_hte']
476	    gc_all = df_summary[df_summary['method'] == 'global_corrected']
477	    nv_all = df_summary[df_summary['method'] == 'naive']
478	    ml_all = df_summary[df_summary['method'] == 'stratified_mle']
479	
480	    if len(hb_all) > 0:
481	        lines.append(f"- **Naive**: RMSE={nv_all['rmse'].mean():.4f}, |Bias|={nv_all['mean_abs_bias'].mean():.4f}, Coverage={nv_all['coverage'].mean():.3f}")
482	        lines.append(f"- **Global**: RMSE={gc_all['rmse'].mean():.4f}, |Bias|={gc_all['mean_abs_bias'].mean():.4f}, Coverage={gc_all['coverage'].mean():.3f}")
483	        lines.append(f"- **Stratified MLE**: RMSE={ml_all['rmse'].mean():.4f}, |Bias|={ml_all['mean_abs_bias'].mean():.4f}, Coverage={ml_all['coverage'].mean():.3f}")
484	        lines.append(f"- **HB EC-HTE**: RMSE={hb_all['rmse'].mean():.4f}, |Bias|={hb_all['mean_abs_bias'].mean():.4f}, Coverage={hb_all['coverage'].mean():.3f}")
485	
486	        naive_rmse = nv_all['rmse'].mean()
487	        gc_rmse = gc_all['rmse'].mean()
488	        hb_rmse = hb_all['rmse'].mean()
489	
490	        lines.append("")
491	        gc_bias = gc_all['mean_abs_bias'].mean()
492	        hb_bias = hb_all['mean_abs_bias'].mean()
493	        nv_bias = nv_all['mean_abs_bias'].mean()
494	
495	        hb_cov = hb_all['coverage'].mean()
496	        gc_cov = gc_all['coverage'].mean()
497	        nv_cov = nv_all['coverage'].mean()
498	
499	        lines.append("### RMSE comparison")
500	        for label, r in [('HB vs Naive', (naive_rmse - hb_rmse) / naive_rmse * 100),
501	                         ('HB vs Global', (gc_rmse - hb_rmse) / gc_rmse * 100),
502	                         ('Global vs Naive', (naive_rmse - gc_rmse) / naive_rmse * 100)]:
503	            direction = "improves" if r > 0 else "worsens"
504	            lines.append(f"- {label}: {direction} by {abs(r):.1f}%")
505	
506	        lines.append(f"\nCoverage: Naive={nv_cov:.3f}, Global={gc_cov:.3f}, HB={hb_cov:.3f} (target=0.95)")
507	
508	        # Bias-variance decomposition insight
509	        hb_mean_bias_sq = (hb_all['mean_bias'] ** 2).mean()
510	        hb_var = hb_all['rmse'].apply(lambda x: x**2).mean() - hb_mean_bias_sq
511	        nv_mean_bias_sq = (nv_all['mean_bias'] ** 2).mean()
512	        nv_var = nv_all['rmse'].apply(lambda x: x**2).mean() - nv_mean_bias_sq
513	
514	        lines.append("\n### Bias-Variance Decomposition (MSE = Bias^2 + Var)")
515	        lines.append(f"- Naive:   Bias^2={nv_mean_bias_sq:.4f}, Var={nv_var:.4f}, MSE={nv_mean_bias_sq+nv_var:.4f}")
516	        lines.append(f"- HB:     Bias^2={hb_mean_bias_sq:.4f}, Var={hb_var:.4f}, MSE={hb_mean_bias_sq+hb_var:.4f}")
517	
518	        lines.append("\n### Interpretation\n")
519	        if hb_bias >= nv_bias:
520	            lines.append("EC-HTE correction **increases** total error under these conditions. "
521	                         "The per-subgroup CM estimates (from ~28-77 expert labels per subgroup) "
522	                         "are too noisy: the variance inflation from inverting estimated mixing matrices "
523	                         "exceeds the bias reduction from stratified correction.")
524	            lines.append(f"\nWith delta_pi={0.137:.3f} (moderate CM heterogeneity) and n_expert={N_EXPERT}, "
525	                         "the Naive estimator's attenuation bias is smaller than the correction's variance cost. "
526	                         "EC-HTE would improve with larger expert budgets or greater CM heterogeneity.")
527	        else:
528	            lines.append("**EC-HTE improves bias over Global under real Llama CMs.**")
529	
530	    report = "\n".join(lines)
531	    outpath = 'artifacts/c1_multi_llm/llama_semisynthetic_analysis.md'
532	    with open(outpath, 'w') as f:
533	        f.write(report)
534	    print(f"Wrote {outpath}")
535	
536	
537	# === Main ===
538	
539	if __name__ == '__main__':
540	    print("Llama-3.1-8B Semi-Synthetic EC-HTE Experiment")
541	    print(f"N={N}, n_expert={N_EXPERT}, n_mc={N_MC}, P(Z=1)={P_Z1}")
542	    print(f"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1-TAU_Z0:.1f}")
543	    print("Subgroup CMs:")
544	    for s in SUBGROUP_LABELS:
545	        cm = SUBGROUP_CM[s]
546	        print(f"  {s}: FPR={cm['fpr']:.3f}, FNR={cm['fnr']:.3f}")
547	    print()
548	
549	    # Dry run: 1 seed
550	    print("=== Dry run (1 seed) ===")
551	    data = generate_data(SEED_BASE)
552	    rows = run_one_mc(data, SEED_BASE)
553	    df_dry = pd.DataFrame(rows)
554	    print(f"Dry run OK: {len(df_dry)} rows")
555	    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:
556	        sub = df_dry[df_dry['method'] == m]
557	        bias = sub['bias'].abs().mean()
558	        print(f"  {m:20s}: mean |bias| = {bias:.4f}")
559	    print()
560	
561	    # Full run
562	    print(f"=== Full run ({N_MC} seeds) ===")
563	    results = []
564	    t0 = time.time()
565	    for mc in range(N_MC):
566	        seed = SEED_BASE + mc
567	        data = generate_data(seed)
568	        mc_rows = run_one_mc(data, seed)
569	        results.extend(mc_rows)
570	        elapsed = time.time() - t0
571	        eta = elapsed / (mc + 1) * (N_MC - mc - 1)
572	        print(f"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s")
573	
574	    total_time = time.time() - t0
575	    print(f"\nTotal time: {total_time:.1f}s")
576	
577	    df_raw = pd.DataFrame(results)
578	    df_summary = aggregate_results(df_raw)
579	
580	    # Save results CSV
581	    col_order = ['seed', 'method', 'subgroup', 'z_level', 'bias', 'rmse', 'coverage', 'cate_true', 'cate_est']
582	    df_raw[col_order].to_csv('artifacts/c1_multi_llm/llama_semisynthetic_results.csv', index=False)
583	    print(f"Saved llama_semisynthetic_results.csv ({len(df_raw)} rows)")
584	
585	    # Write analysis
586	    write_analysis(df_raw, df_summary)
587	
588	    # Print summary
589	    print("\n=== Summary ===\n")
590	    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:
591	        sub = df_summary[df_summary['method'] == m]
592	        if len(sub) > 0:
593	            print(f"  {m:20s}: |bias|={sub['mean_abs_bias'].mean():.4f}  "
594	                  f"rmse={sub['rmse'].mean():.4f}  cov={sub['coverage'].mean():.3f}")
595	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "uuid": "147e2904-3e82-49da-9264-c21691f49434",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_llama_semisynthetic.py",
      "content": "\"\"\"\nLlama-3.1-8B Semi-Synthetic DGP: EC-HTE vs Global vs Naive RMSE comparison.\n\nUses real per-subgroup confusion matrices from Llama-3.1-8B balanced annotations.\nGround truth CATE is synthetic; confusion matrices are empirical.\n\n4 subgroups with real asymmetric CMs:\n  False_medium: FPR=0.235, FNR=0.319, weight=193/500\n  False_short:  FPR=0.310, FNR=0.212, weight=109/500\n  True_medium:  FPR=0.219, FNR=0.258, weight=129/500\n  True_short:   FPR=0.091, FNR=0.190, weight=69/500\n\nP(Z=1) = 0.652, delta_tau = 0.3, tau(z=0)=0.35, tau(z=1)=0.65\nMethods: Naive, Global, Stratified MLE, HB EC-HTE\nn_expert=200, 20 MC seeds\n\nUsage: python3 artifacts/c1_multi_llm/run_llama_semisynthetic.py\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT = 200\nN_MC = 20\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']\nSUBGROUP_WEIGHTS = np.array([193, 109, 129, 69], dtype=float)\nSUBGROUP_WEIGHTS /= SUBGROUP_WEIGHTS.sum()\n\nSUBGROUP_CM = {\n    'False_medium': {'fpr': 0.235, 'fnr': 0.319},\n    'False_short':  {'fpr': 0.310, 'fnr': 0.212},\n    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},\n    'True_short':   {'fpr': 0.091, 'fnr': 0.190},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\nTAU_Z0 = 0.35\nTAU_Z1 = 0.65\n\n\ndef get_cm_matrix(fpr, fnr):\n    \"\"\"Build 2x2 confusion matrix: C[z_true, z_obs].\"\"\"\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Core Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    \"\"\"Global CM with Laplace smoothing.\"\"\"\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    \"\"\"Per-subgroup MLE with Laplace smoothing.\"\"\"\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    \"\"\"M[z_hat, z] = P(Z=z | Z_hat=z_hat) via Bayes' rule.\"\"\"\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === HB Gibbs Sampler ===\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=1000, n_warmup=500, n_chains=4,\n                         hp_a0=3.0, hp_b0=1.0):\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_theta = []\n    t0 = time.time()\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))\n                accepted = np.log(rng.rand()) < log_r\n                if accepted:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(accepted)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                theta_samples[it - n_warmup] = theta.copy()\n\n        all_theta.append(theta_samples)\n\n    runtime = time.time() - t0\n    theta_arr = np.stack(all_theta)\n\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n\n    return C, {'runtime_seconds': runtime}\n\n\n# === DGP ===\n\ndef generate_data(seed):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(4):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, N_EXPERT, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    # Global CM from experts\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    # Stratified MLE per-subgroup\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    # HB Gibbs\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb, _ = estimate_cm_hb_gibbs(counts, SUBGROUP_LABELS, seed=seed)\n\n    # Build per-subgroup mixing matrices\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0\n\n            # Oracle\n            th_or, se_or = diff_in_means(Y, T, s_mask & (Z == z_level))\n            ci_lo_or = th_or - 1.96 * se_or if not np.isnan(se_or) else np.nan\n            ci_hi_or = th_or + 1.96 * se_or if not np.isnan(se_or) else np.nan\n            cov_or = 1 if (not np.isnan(ci_lo_or) and ci_lo_or <= oracle_cate <= ci_hi_or) else 0\n            rows.append({\n                'seed': seed, 'method': 'oracle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_or - oracle_cate if not np.isnan(th_or) else np.nan,\n                'rmse': abs(th_or - oracle_cate) if not np.isnan(th_or) else np.nan,\n                'coverage': cov_or,\n                'cate_true': oracle_cate, 'cate_est': th_or,\n            })\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'rmse': abs(th_nv - oracle_cate) if not np.isnan(th_nv) else np.nan,\n                'coverage': cov_nv,\n                'cate_true': oracle_cate, 'cate_est': th_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells for this subgroup\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'rmse': abs(th_gc - oracle_cate) if not np.isnan(th_gc) else np.nan,\n                'coverage': cov_gc,\n                'cate_true': oracle_cate, 'cate_est': th_gc,\n            })\n\n            # Stratified MLE\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'rmse': abs(th_ml - oracle_cate) if not np.isnan(th_ml) else np.nan,\n                'coverage': cov_ml,\n                'cate_true': oracle_cate, 'cate_est': th_ml,\n            })\n\n            # HB EC-HTE\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'rmse': abs(th_hb - oracle_cate) if not np.isnan(th_hb) else np.nan,\n                'coverage': cov_hb,\n                'cate_true': oracle_cate, 'cate_est': th_hb,\n            })\n\n    return rows\n\n\n# === Aggregation ===\n\ndef aggregate_results(df_raw):\n    group_cols = ['subgroup', 'z_level', 'method']\n    rows = []\n    for keys, grp in df_raw.groupby(group_cols):\n        row = dict(zip(group_cols, keys))\n        valid = grp['bias'].dropna()\n        if len(valid) == 0:\n            continue\n        row['mean_bias'] = valid.mean()\n        row['mean_abs_bias'] = valid.abs().mean()\n        row['rmse'] = np.sqrt((valid ** 2).mean())\n        row['coverage'] = grp['coverage'].mean()\n        row['n_mc'] = len(valid)\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# === Analysis Report ===\n\ndef write_analysis(df_raw, df_summary):\n    lines = []\n    lines.append(\"# Llama-3.1-8B Semi-Synthetic EC-HTE Experiment\\n\")\n\n    lines.append(\"## Design\\n\")\n    lines.append(\"Uses **real asymmetric confusion matrices** from Llama-3.1-8B balanced annotations.\")\n    lines.append(\"Ground truth CATE is synthetic; confusion matrices are empirical.\\n\")\n\n    lines.append(\"| Subgroup | Weight | FPR | FNR | pi_s |\")\n    lines.append(\"|----------|--------|-----|-----|------|\")\n    for i, s in enumerate(SUBGROUP_LABELS):\n        cm = SUBGROUP_CM[s]\n        lines.append(f\"| {s} | {SUBGROUP_WEIGHTS[i]:.3f} | {cm['fpr']:.3f} | {cm['fnr']:.3f} | {(cm['fpr'] + cm['fnr'])/2:.3f} |\")\n    lines.append(\"\")\n\n    lines.append(f\"**Parameters**: N={N}, P(Z=1)={P_Z1}, n_expert={N_EXPERT}, \"\n                 f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1-TAU_Z0:.1f}\")\n    lines.append(f\"**MC seeds**: {N_MC}\\n\")\n\n    # Overall summary\n    lines.append(\"## Summary (averaged across subgroups and z-levels)\\n\")\n    lines.append(\"| Method | Mean |Bias| | RMSE | Coverage |\")\n    lines.append(\"|--------|-------------|------|----------|\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_summary[df_summary['method'] == m]\n        if len(sub) > 0:\n            lines.append(f\"| {m} | {sub['mean_abs_bias'].mean():.4f} | \"\n                         f\"{sub['rmse'].mean():.4f} | {sub['coverage'].mean():.3f} |\")\n    lines.append(\"\")\n\n    # Per-subgroup breakdown\n    lines.append(\"## Per-Subgroup Breakdown\\n\")\n    lines.append(\"| Subgroup | Z | Method | Mean Bias | |Bias| | RMSE | Coverage |\")\n    lines.append(\"|----------|---|--------|-----------|-------|------|----------|\")\n    for s in SUBGROUP_LABELS:\n        for z in [0, 1]:\n            for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n                row = df_summary[(df_summary['subgroup'] == s) &\n                                 (df_summary['z_level'] == z) &\n                                 (df_summary['method'] == m)]\n                if len(row) > 0:\n                    r = row.iloc[0]\n                    lines.append(f\"| {s} | {z} | {m} | {r['mean_bias']:+.4f} | \"\n                                 f\"{r['mean_abs_bias']:.4f} | {r['rmse']:.4f} | {r['coverage']:.3f} |\")\n    lines.append(\"\")\n\n    # EC-HTE vs Global bias reduction\n    lines.append(\"## EC-HTE vs Global: Bias Reduction Ratio\\n\")\n    lines.append(\"| Subgroup | Z | HB |Bias| | Global |Bias| | Reduction |\")\n    lines.append(\"|----------|---|-----------|-------------|-----------|\")\n    total_hb, total_gc = 0.0, 0.0\n    n_cells = 0\n    for s in SUBGROUP_LABELS:\n        for z in [0, 1]:\n            hb = df_summary[(df_summary['subgroup'] == s) & (df_summary['z_level'] == z) &\n                            (df_summary['method'] == 'hb_ec_hte')]\n            gc = df_summary[(df_summary['subgroup'] == s) & (df_summary['z_level'] == z) &\n                            (df_summary['method'] == 'global_corrected')]\n            if len(hb) > 0 and len(gc) > 0:\n                hb_b = hb.iloc[0]['mean_abs_bias']\n                gc_b = gc.iloc[0]['mean_abs_bias']\n                red = (gc_b - hb_b) / gc_b * 100 if gc_b > 1e-6 else 0\n                lines.append(f\"| {s} | {z} | {hb_b:.4f} | {gc_b:.4f} | {red:+.1f}% |\")\n                total_hb += hb_b\n                total_gc += gc_b\n                n_cells += 1\n    if n_cells > 0:\n        avg_red = (total_gc / n_cells - total_hb / n_cells) / (total_gc / n_cells) * 100\n        lines.append(f\"| **Average** | | {total_hb/n_cells:.4f} | {total_gc/n_cells:.4f} | {avg_red:+.1f}% |\")\n    lines.append(\"\")\n\n    # Conclusion\n    lines.append(\"## Conclusion\\n\")\n\n    hb_all = df_summary[df_summary['method'] == 'hb_ec_hte']\n    gc_all = df_summary[df_summary['method'] == 'global_corrected']\n    nv_all = df_summary[df_summary['method'] == 'naive']\n    ml_all = df_summary[df_summary['method'] == 'stratified_mle']\n\n    if len(hb_all) > 0:\n        lines.append(f\"- **Naive**: RMSE={nv_all['rmse'].mean():.4f}, |Bias|={nv_all['mean_abs_bias'].mean():.4f}, Coverage={nv_all['coverage'].mean():.3f}\")\n        lines.append(f\"- **Global**: RMSE={gc_all['rmse'].mean():.4f}, |Bias|={gc_all['mean_abs_bias'].mean():.4f}, Coverage={gc_all['coverage'].mean():.3f}\")\n        lines.append(f\"- **Stratified MLE**: RMSE={ml_all['rmse'].mean():.4f}, |Bias|={ml_all['mean_abs_bias'].mean():.4f}, Coverage={ml_all['coverage'].mean():.3f}\")\n        lines.append(f\"- **HB EC-HTE**: RMSE={hb_all['rmse'].mean():.4f}, |Bias|={hb_all['mean_abs_bias'].mean():.4f}, Coverage={hb_all['coverage'].mean():.3f}\")\n\n        naive_rmse = nv_all['rmse'].mean()\n        gc_rmse = gc_all['rmse'].mean()\n        hb_rmse = hb_all['rmse'].mean()\n\n        lines.append(\"\")\n        gc_bias = gc_all['mean_abs_bias'].mean()\n        hb_bias = hb_all['mean_abs_bias'].mean()\n        nv_bias = nv_all['mean_abs_bias'].mean()\n\n        hb_cov = hb_all['coverage'].mean()\n        gc_cov = gc_all['coverage'].mean()\n        nv_cov = nv_all['coverage'].mean()\n\n        lines.append(\"### RMSE comparison\")\n        for label, r in [('HB vs Naive', (naive_rmse - hb_rmse) / naive_rmse * 100),\n                         ('HB vs Global', (gc_rmse - hb_rmse) / gc_rmse * 100),\n                         ('Global vs Naive', (naive_rmse - gc_rmse) / naive_rmse * 100)]:\n            direction = \"improves\" if r > 0 else \"worsens\"\n            lines.append(f\"- {label}: {direction} by {abs(r):.1f}%\")\n\n        lines.append(f\"\\nCoverage: Naive={nv_cov:.3f}, Global={gc_cov:.3f}, HB={hb_cov:.3f} (target=0.95)\")\n\n        # Bias-variance decomposition insight\n        hb_mean_bias_sq = (hb_all['mean_bias'] ** 2).mean()\n        hb_var = hb_all['rmse'].apply(lambda x: x**2).mean() - hb_mean_bias_sq\n        nv_mean_bias_sq = (nv_all['mean_bias'] ** 2).mean()\n        nv_var = nv_all['rmse'].apply(lambda x: x**2).mean() - nv_mean_bias_sq\n\n        lines.append(\"\\n### Bias-Variance Decomposition (MSE = Bias^2 + Var)\")\n        lines.append(f\"- Naive:   Bias^2={nv_mean_bias_sq:.4f}, Var={nv_var:.4f}, MSE={nv_mean_bias_sq+nv_var:.4f}\")\n        lines.append(f\"- HB:     Bias^2={hb_mean_bias_sq:.4f}, Var={hb_var:.4f}, MSE={hb_mean_bias_sq+hb_var:.4f}\")\n\n        lines.append(\"\\n### Interpretation\\n\")\n        if hb_bias >= nv_bias:\n            lines.append(\"EC-HTE correction **increases** total error under these conditions. \"\n                         \"The per-subgroup CM estimates (from ~28-77 expert labels per subgroup) \"\n                         \"are too noisy: the variance inflation from inverting estimated mixing matrices \"\n                         \"exceeds the bias reduction from stratified correction.\")\n            lines.append(f\"\\nWith delta_pi={0.137:.3f} (moderate CM heterogeneity) and n_expert={N_EXPERT}, \"\n                         \"the Naive estimator's attenuation bias is smaller than the correction's variance cost. \"\n                         \"EC-HTE would improve with larger expert budgets or greater CM heterogeneity.\")\n        else:\n            lines.append(\"**EC-HTE improves bias over Global under real Llama CMs.**\")\n\n    report = \"\\n\".join(lines)\n    outpath = 'artifacts/c1_multi_llm/llama_semisynthetic_analysis.md'\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"Llama-3.1-8B Semi-Synthetic EC-HTE Experiment\")\n    print(f\"N={N}, n_expert={N_EXPERT}, n_mc={N_MC}, P(Z=1)={P_Z1}\")\n    print(f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1-TAU_Z0:.1f}\")\n    print(\"Subgroup CMs:\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.3f}, FNR={cm['fnr']:.3f}\")\n    print()\n\n    # Dry run: 1 seed\n    print(\"=== Dry run (1 seed) ===\")\n    data = generate_data(SEED_BASE)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    print(f\"Dry run OK: {len(df_dry)} rows\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n    print()\n\n    # Full run\n    print(f\"=== Full run ({N_MC} seeds) ===\")\n    results = []\n    t0 = time.time()\n    for mc in range(N_MC):\n        seed = SEED_BASE + mc\n        data = generate_data(seed)\n        mc_rows = run_one_mc(data, seed)\n        results.extend(mc_rows)\n        elapsed = time.time() - t0\n        eta = elapsed / (mc + 1) * (N_MC - mc - 1)\n        print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(results)\n    df_summary = aggregate_results(df_raw)\n\n    # Save results CSV\n    col_order = ['seed', 'method', 'subgroup', 'z_level', 'bias', 'rmse', 'coverage', 'cate_true', 'cate_est']\n    df_raw[col_order].to_csv('artifacts/c1_multi_llm/llama_semisynthetic_results.csv', index=False)\n    print(f\"Saved llama_semisynthetic_results.csv ({len(df_raw)} rows)\")\n\n    # Write analysis\n    write_analysis(df_raw, df_summary)\n\n    # Print summary\n    print(\"\\n=== Summary ===\\n\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_summary[df_summary['method'] == m]\n        if len(sub) > 0:\n            print(f\"  {m:20s}: |bias|={sub['mean_abs_bias'].mean():.4f}  \"\n                  f\"rmse={sub['rmse'].mean():.4f}  cov={sub['coverage'].mean():.3f}\")\n",
      "numLines": 595,
      "startLine": 1,
      "totalLines": 595
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
Now I understand the base script. I need to create a K=2 budget sweep version with:

1. K=2 subgroups: 'False' and 'True' (merged by has_hashtag)
2. n_expert ∈ {100, 200, 500, 1000, 2000}
3. 50 MC seeds
4. Corrected |Bias| metric: |mean(bias)| not mean(|bias|)
5. Output CSV and analysis MD

Let me write the script.

Key changes:


- Setting up the subgroup labels and their population weights
- Merging the confusion matrices across subgroups with the corrected bias calculation
- Iterating through the expert budget values with 50 random seeds
- Analyzing where the fairness-accuracy tradeoff crosses over

Writing the script...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "uuid": "fa0fefc6-3225-44b4-b4a5-4d31a202c62e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VATEsvTgy2qnvdtuYuhPQF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10980,
      "cache_read_input_tokens": 18433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10980
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

_source line 8_

Now I'll create the K=2 budget sweep script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "uuid": "91131e34-06c1-4ba5-8df3-2b5b097fe882",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VATEsvTgy2qnvdtuYuhPQF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10980,
      "cache_read_input_tokens": 18433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10980
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

_source line 9_

<details open><summary>🔧 Tool call — Write · `toolu_01V7uScxqFTdBahCmQUQc9u3`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_budget_sweep_k2.py",
  "content": "\"\"\"\nK=2 Budget Sensitivity Sweep: Llama-3.1-8B Semi-Synthetic EC-HTE.\n\nMerged subgroups by has_hashtag:\n  False (no hashtag): FPR=0.252, FNR=0.269, weight=0.604\n  True (has hashtag):  FPR=0.186, FNR=0.233, weight=0.396\n\nΔπ = |0.261 - 0.210| = 0.051\n\nn_expert ∈ {100, 200, 500, 1000, 2000}, 50 MC seeds per budget.\nMethods: Naive, Global, Stratified MLE, HB EC-HTE\n\nUsage: python3 artifacts/c1_multi_llm/run_budget_sweep_k2.py\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT_LIST = [100, 200, 500, 1000, 2000]\nN_MC = 50\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False', 'True']\nSUBGROUP_WEIGHTS = np.array([0.604, 0.396])\n\nSUBGROUP_CM = {\n    'False': {'fpr': 0.252, 'fnr': 0.269},\n    'True':  {'fpr': 0.186, 'fnr': 0.233},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\nTAU_Z0 = 0.35\nTAU_Z1 = 0.65\n\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Core Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === HB Gibbs Sampler (MAP-EB accelerated) ===\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=800, n_warmup=400, n_chains=2,\n                         hp_a0=3.0, hp_b0=1.0):\n    k = len(labels)\n    chain_inits = [np.array([1.0, 1.0]), np.array([5.0, 5.0])][:n_chains]\n    all_theta = []\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))\n                if np.log(rng.rand()) < log_r:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(np.log(rng.rand()) < log_r)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                theta_samples[it - n_warmup] = theta.copy()\n\n        all_theta.append(theta_samples)\n\n    theta_arr = np.stack(all_theta)\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n    return C\n\n\n# === DGP ===\n\ndef generate_data(seed, n_expert):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(2, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(2):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb = estimate_cm_hb_gibbs(counts, SUBGROUP_LABELS, seed=seed)\n\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0\n\n            th_or, se_or = diff_in_means(Y, T, s_mask & (Z == z_level))\n            ci_lo_or = th_or - 1.96 * se_or if not np.isnan(se_or) else np.nan\n            ci_hi_or = th_or + 1.96 * se_or if not np.isnan(se_or) else np.nan\n            cov_or = 1 if (not np.isnan(ci_lo_or) and ci_lo_or <= oracle_cate <= ci_hi_or) else 0\n            rows.append({\n                'seed': seed, 'method': 'oracle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_or - oracle_cate if not np.isnan(th_or) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_or,\n                'coverage': cov_or,\n            })\n\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_nv,\n                'coverage': cov_nv,\n            })\n\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_gc,\n                'coverage': cov_gc,\n            })\n\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_ml,\n                'coverage': cov_ml,\n            })\n\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_hb,\n                'coverage': cov_hb,\n            })\n\n    return rows\n\n\n# === Aggregation (corrected |Bias| = |mean(bias)|) ===\n\ndef aggregate_results(df_raw):\n    group_cols = ['n_expert', 'subgroup', 'z_level', 'method']\n    rows = []\n    for keys, grp in df_raw.groupby(group_cols):\n        row = dict(zip(group_cols, keys))\n        valid = grp['bias'].dropna()\n        if len(valid) == 0:\n            continue\n        row['mean_bias'] = valid.mean()\n        row['abs_mean_bias'] = abs(valid.mean())\n        row['rmse'] = np.sqrt((valid ** 2).mean())\n        row['coverage'] = grp['coverage'].mean()\n        row['n_mc'] = len(valid)\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# === Analysis Report ===\n\ndef write_analysis(df_summary):\n    lines = []\n    lines.append(\"# K=2 Budget Sensitivity Sweep: Llama-3.1-8B Real CMs\\n\")\n\n    lines.append(\"## Design\\n\")\n    lines.append(\"Merged subgroups by `has_hashtag` (K=2).\\n\")\n    lines.append(\"| Subgroup | Weight | FPR | FNR | π_s |\")\n    lines.append(\"|----------|--------|-----|-----|-----|\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        pi = (cm['fpr'] + cm['fnr']) / 2\n        lines.append(f\"| {s} | {SUBGROUP_WEIGHTS[SUBGROUP_LABELS.index(s)]:.3f} | {cm['fpr']:.3f} | {cm['fnr']:.3f} | {pi:.3f} |\")\n    lines.append(\"\")\n    lines.append(\"Δπ = |π_False - π_True| = |0.261 - 0.210| = 0.051\")\n    lines.append(f\"\\nN={N}, P(Z=1)={P_Z1}, τ(z=0)={TAU_Z0}, τ(z=1)={TAU_Z1}, Δτ={TAU_Z1-TAU_Z0:.1f}\")\n    lines.append(f\"n_expert ∈ {N_EXPERT_LIST}, {N_MC} MC seeds per budget\\n\")\n\n    lines.append(\"## Summary by n_expert\\n\")\n    lines.append(\"| n_expert | Method | |Bias| | RMSE | Coverage |\")\n    lines.append(\"|----------|--------|-------|------|----------|\")\n    for ne in N_EXPERT_LIST:\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                lines.append(f\"| {ne} | {m} | {sub['abs_mean_bias'].mean():.4f} | \"\n                             f\"{sub['rmse'].mean():.4f} | {sub['coverage'].mean():.3f} |\")\n        lines.append(\"|---|---|---|---|---|\")\n    lines.append(\"\")\n\n    lines.append(\"## RMSE Ratio: EC-HTE / Naive\\n\")\n    lines.append(\"| n_expert | Naive RMSE | HB RMSE | Ratio | HB wins? |\")\n    lines.append(\"|----------|-----------|---------|-------|----------|\")\n    crossover = None\n    for ne in N_EXPERT_LIST:\n        nv = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'naive')]\n        hb = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'hb_ec_hte')]\n        if len(nv) > 0 and len(hb) > 0:\n            nv_rmse = nv['rmse'].mean()\n            hb_rmse = hb['rmse'].mean()\n            ratio = hb_rmse / nv_rmse\n            wins = \"YES\" if ratio < 1.0 else \"no\"\n            lines.append(f\"| {ne} | {nv_rmse:.4f} | {hb_rmse:.4f} | {ratio:.3f} | {wins} |\")\n            if ratio < 1.0 and crossover is None:\n                crossover = ne\n    lines.append(\"\")\n\n    lines.append(\"## |Bias| Ratio: EC-HTE / Naive\\n\")\n    lines.append(\"| n_expert | Naive |Bias| | HB |Bias| | Ratio | HB wins? |\")\n    lines.append(\"|----------|-----------|---------|-------|----------|\")\n    bias_crossover = None\n    for ne in N_EXPERT_LIST:\n        nv = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'naive')]\n        hb = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'hb_ec_hte')]\n        if len(nv) > 0 and len(hb) > 0:\n            nv_b = nv['abs_mean_bias'].mean()\n            hb_b = hb['abs_mean_bias'].mean()\n            ratio = hb_b / nv_b if nv_b > 1e-8 else float('inf')\n            wins = \"YES\" if ratio < 1.0 else \"no\"\n            lines.append(f\"| {ne} | {nv_b:.4f} | {hb_b:.4f} | {ratio:.3f} | {wins} |\")\n            if ratio < 1.0 and bias_crossover is None:\n                bias_crossover = ne\n    lines.append(\"\")\n\n    lines.append(\"## Bias-Variance Decomposition\\n\")\n    lines.append(\"| n_expert | Method | Bias² | Var | MSE |\")\n    lines.append(\"|----------|--------|-------|-----|-----|\")\n    for ne in N_EXPERT_LIST:\n        for m in ['naive', 'global_corrected', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                bias_sq = (sub['mean_bias'] ** 2).mean()\n                mse = (sub['rmse'] ** 2).mean()\n                var = mse - bias_sq\n                lines.append(f\"| {ne} | {m} | {bias_sq:.4f} | {var:.4f} | {mse:.4f} |\")\n        lines.append(\"|---|---|---|---|---|\")\n    lines.append(\"\")\n\n    lines.append(\"## Crossover Analysis\\n\")\n    if crossover:\n        lines.append(f\"**RMSE crossover**: EC-HTE first beats Naive at n_expert={crossover}\")\n    else:\n        lines.append(\"**RMSE crossover**: EC-HTE never beats Naive in tested range\")\n    if bias_crossover:\n        lines.append(f\"**|Bias| crossover**: EC-HTE first beats Naive at n_expert={bias_crossover}\")\n    else:\n        lines.append(\"**|Bias| crossover**: EC-HTE never beats Naive in tested range\")\n\n    lines.append(\"\")\n    lines.append(\"## Conclusion\\n\")\n    lines.append(f\"With K=2 and Δπ=0.051, the CM heterogeneity is small.\")\n    lines.append(\"The bias reduction from stratified correction is limited, \"\n                 \"so the variance cost of estimating per-subgroup CMs must be overcome by larger n_expert.\")\n    if crossover:\n        lines.append(f\"\\nAt n_expert≥{crossover}, HB EC-HTE achieves lower RMSE than Naive, \"\n                     \"indicating the variance cost is amortized.\")\n    else:\n        lines.append(\"\\nEven at n_expert=2000, the variance cost exceeds the bias reduction. \"\n                     \"K=2 with Δπ=0.051 may be too homogeneous for EC-HTE to help.\")\n\n    report = \"\\n\".join(lines)\n    outpath = 'artifacts/c1_multi_llm/budget_sweep_k2_analysis.md'\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"K=2 Budget Sensitivity Sweep\")\n    print(f\"N={N}, n_expert_list={N_EXPERT_LIST}, n_mc={N_MC}\")\n    print(f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, Δτ={TAU_Z1-TAU_Z0:.1f}\")\n    print(\"K=2 Subgroup CMs:\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.3f}, FNR={cm['fnr']:.3f}, π={(cm['fpr']+cm['fnr'])/2:.3f}\")\n    print()\n\n    # Dry run: 1 seed, smallest budget\n    print(\"=== Dry run (1 seed, n_expert=100) ===\")\n    data = generate_data(SEED_BASE, 100)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    df_dry['n_expert'] = 100\n    print(f\"Dry run OK: {len(df_dry)} rows\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n    print()\n\n    proceed = input(\"Proceed with full run? [y/N] \").strip().lower()\n    if proceed != 'y':\n        print(\"Aborted.\")\n        exit(0)\n\n    # Full run\n    all_results = []\n    t0_total = time.time()\n\n    for ne in N_EXPERT_LIST:\n        print(f\"\\n=== n_expert={ne} ({N_MC} seeds) ===\")\n        t0 = time.time()\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            data = generate_data(seed, ne)\n            mc_rows = run_one_mc(data, seed)\n            for r in mc_rows:\n                r['n_expert'] = ne\n            all_results.extend(mc_rows)\n\n            if (mc + 1) % 10 == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / (mc + 1) * (N_MC - mc - 1)\n                print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n\n        elapsed = time.time() - t0\n        print(f\"  n_expert={ne} done in {elapsed:.1f}s\")\n\n    total_time = time.time() - t0_total\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(all_results)\n    df_summary = aggregate_results(df_raw)\n\n    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_true', 'cate_est', 'coverage']\n    df_raw[col_order].to_csv('artifacts/c1_multi_llm/budget_sweep_k2_results.csv', index=False)\n    print(f\"Saved budget_sweep_k2_results.csv ({len(df_raw)} rows)\")\n\n    write_analysis(df_summary)\n\n    print(\"\\n=== Summary ===\")\n    for ne in N_EXPERT_LIST:\n        print(f\"\\n  n_expert={ne}:\")\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                print(f\"    {m:20s}: |bias|={sub['abs_mean_bias'].mean():.4f}  \"\n                      f\"rmse={sub['rmse'].mean():.4f}  cov={sub['coverage'].mean():.3f}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "uuid": "7fcb9681-8096-40c8-926b-def2f1a663c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VATEsvTgy2qnvdtuYuhPQF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10980,
      "cache_read_input_tokens": 18433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10980
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

_source line 10 · 2026-05-21T21:30:08.703Z_

<details><summary>↩ Tool result · `toolu_01V7uScxqFTdBahCmQUQc9u3`</summary>

```text
File created successfully at: /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_budget_sweep_k2.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "uuid": "8d38d1ff-fb00-436d-a185-8257c36fa346",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_budget_sweep_k2.py",
    "content": "\"\"\"\nK=2 Budget Sensitivity Sweep: Llama-3.1-8B Semi-Synthetic EC-HTE.\n\nMerged subgroups by has_hashtag:\n  False (no hashtag): FPR=0.252, FNR=0.269, weight=0.604\n  True (has hashtag):  FPR=0.186, FNR=0.233, weight=0.396\n\nΔπ = |0.261 - 0.210| = 0.051\n\nn_expert ∈ {100, 200, 500, 1000, 2000}, 50 MC seeds per budget.\nMethods: Naive, Global, Stratified MLE, HB EC-HTE\n\nUsage: python3 artifacts/c1_multi_llm/run_budget_sweep_k2.py\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT_LIST = [100, 200, 500, 1000, 2000]\nN_MC = 50\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False', 'True']\nSUBGROUP_WEIGHTS = np.array([0.604, 0.396])\n\nSUBGROUP_CM = {\n    'False': {'fpr': 0.252, 'fnr': 0.269},\n    'True':  {'fpr': 0.186, 'fnr': 0.233},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\nTAU_Z0 = 0.35\nTAU_Z1 = 0.65\n\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Core Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === HB Gibbs Sampler (MAP-EB accelerated) ===\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=800, n_warmup=400, n_chains=2,\n                         hp_a0=3.0, hp_b0=1.0):\n    k = len(labels)\n    chain_inits = [np.array([1.0, 1.0]), np.array([5.0, 5.0])][:n_chains]\n    all_theta = []\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))\n                if np.log(rng.rand()) < log_r:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(np.log(rng.rand()) < log_r)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                theta_samples[it - n_warmup] = theta.copy()\n\n        all_theta.append(theta_samples)\n\n    theta_arr = np.stack(all_theta)\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n    return C\n\n\n# === DGP ===\n\ndef generate_data(seed, n_expert):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(2, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(2):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb = estimate_cm_hb_gibbs(counts, SUBGROUP_LABELS, seed=seed)\n\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0\n\n            th_or, se_or = diff_in_means(Y, T, s_mask & (Z == z_level))\n            ci_lo_or = th_or - 1.96 * se_or if not np.isnan(se_or) else np.nan\n            ci_hi_or = th_or + 1.96 * se_or if not np.isnan(se_or) else np.nan\n            cov_or = 1 if (not np.isnan(ci_lo_or) and ci_lo_or <= oracle_cate <= ci_hi_or) else 0\n            rows.append({\n                'seed': seed, 'method': 'oracle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_or - oracle_cate if not np.isnan(th_or) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_or,\n                'coverage': cov_or,\n            })\n\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_nv,\n                'coverage': cov_nv,\n            })\n\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_gc,\n                'coverage': cov_gc,\n            })\n\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_ml,\n                'coverage': cov_ml,\n            })\n\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'cate_true': oracle_cate, 'cate_est': th_hb,\n                'coverage': cov_hb,\n            })\n\n    return rows\n\n\n# === Aggregation (corrected |Bias| = |mean(bias)|) ===\n\ndef aggregate_results(df_raw):\n    group_cols = ['n_expert', 'subgroup', 'z_level', 'method']\n    rows = []\n    for keys, grp in df_raw.groupby(group_cols):\n        row = dict(zip(group_cols, keys))\n        valid = grp['bias'].dropna()\n        if len(valid) == 0:\n            continue\n        row['mean_bias'] = valid.mean()\n        row['abs_mean_bias'] = abs(valid.mean())\n        row['rmse'] = np.sqrt((valid ** 2).mean())\n        row['coverage'] = grp['coverage'].mean()\n        row['n_mc'] = len(valid)\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# === Analysis Report ===\n\ndef write_analysis(df_summary):\n    lines = []\n    lines.append(\"# K=2 Budget Sensitivity Sweep: Llama-3.1-8B Real CMs\\n\")\n\n    lines.append(\"## Design\\n\")\n    lines.append(\"Merged subgroups by `has_hashtag` (K=2).\\n\")\n    lines.append(\"| Subgroup | Weight | FPR | FNR | π_s |\")\n    lines.append(\"|----------|--------|-----|-----|-----|\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        pi = (cm['fpr'] + cm['fnr']) / 2\n        lines.append(f\"| {s} | {SUBGROUP_WEIGHTS[SUBGROUP_LABELS.index(s)]:.3f} | {cm['fpr']:.3f} | {cm['fnr']:.3f} | {pi:.3f} |\")\n    lines.append(\"\")\n    lines.append(\"Δπ = |π_False - π_True| = |0.261 - 0.210| = 0.051\")\n    lines.append(f\"\\nN={N}, P(Z=1)={P_Z1}, τ(z=0)={TAU_Z0}, τ(z=1)={TAU_Z1}, Δτ={TAU_Z1-TAU_Z0:.1f}\")\n    lines.append(f\"n_expert ∈ {N_EXPERT_LIST}, {N_MC} MC seeds per budget\\n\")\n\n    lines.append(\"## Summary by n_expert\\n\")\n    lines.append(\"| n_expert | Method | |Bias| | RMSE | Coverage |\")\n    lines.append(\"|----------|--------|-------|------|----------|\")\n    for ne in N_EXPERT_LIST:\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                lines.append(f\"| {ne} | {m} | {sub['abs_mean_bias'].mean():.4f} | \"\n                             f\"{sub['rmse'].mean():.4f} | {sub['coverage'].mean():.3f} |\")\n        lines.append(\"|---|---|---|---|---|\")\n    lines.append(\"\")\n\n    lines.append(\"## RMSE Ratio: EC-HTE / Naive\\n\")\n    lines.append(\"| n_expert | Naive RMSE | HB RMSE | Ratio | HB wins? |\")\n    lines.append(\"|----------|-----------|---------|-------|----------|\")\n    crossover = None\n    for ne in N_EXPERT_LIST:\n        nv = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'naive')]\n        hb = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'hb_ec_hte')]\n        if len(nv) > 0 and len(hb) > 0:\n            nv_rmse = nv['rmse'].mean()\n            hb_rmse = hb['rmse'].mean()\n            ratio = hb_rmse / nv_rmse\n            wins = \"YES\" if ratio < 1.0 else \"no\"\n            lines.append(f\"| {ne} | {nv_rmse:.4f} | {hb_rmse:.4f} | {ratio:.3f} | {wins} |\")\n            if ratio < 1.0 and crossover is None:\n                crossover = ne\n    lines.append(\"\")\n\n    lines.append(\"## |Bias| Ratio: EC-HTE / Naive\\n\")\n    lines.append(\"| n_expert | Naive |Bias| | HB |Bias| | Ratio | HB wins? |\")\n    lines.append(\"|----------|-----------|---------|-------|----------|\")\n    bias_crossover = None\n    for ne in N_EXPERT_LIST:\n        nv = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'naive')]\n        hb = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'hb_ec_hte')]\n        if len(nv) > 0 and len(hb) > 0:\n            nv_b = nv['abs_mean_bias'].mean()\n            hb_b = hb['abs_mean_bias'].mean()\n            ratio = hb_b / nv_b if nv_b > 1e-8 else float('inf')\n            wins = \"YES\" if ratio < 1.0 else \"no\"\n            lines.append(f\"| {ne} | {nv_b:.4f} | {hb_b:.4f} | {ratio:.3f} | {wins} |\")\n            if ratio < 1.0 and bias_crossover is None:\n                bias_crossover = ne\n    lines.append(\"\")\n\n    lines.append(\"## Bias-Variance Decomposition\\n\")\n    lines.append(\"| n_expert | Method | Bias² | Var | MSE |\")\n    lines.append(\"|----------|--------|-------|-----|-----|\")\n    for ne in N_EXPERT_LIST:\n        for m in ['naive', 'global_corrected', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                bias_sq = (sub['mean_bias'] ** 2).mean()\n                mse = (sub['rmse'] ** 2).mean()\n                var = mse - bias_sq\n                lines.append(f\"| {ne} | {m} | {bias_sq:.4f} | {var:.4f} | {mse:.4f} |\")\n        lines.append(\"|---|---|---|---|---|\")\n    lines.append(\"\")\n\n    lines.append(\"## Crossover Analysis\\n\")\n    if crossover:\n        lines.append(f\"**RMSE crossover**: EC-HTE first beats Naive at n_expert={crossover}\")\n    else:\n        lines.append(\"**RMSE crossover**: EC-HTE never beats Naive in tested range\")\n    if bias_crossover:\n        lines.append(f\"**|Bias| crossover**: EC-HTE first beats Naive at n_expert={bias_crossover}\")\n    else:\n        lines.append(\"**|Bias| crossover**: EC-HTE never beats Naive in tested range\")\n\n    lines.append(\"\")\n    lines.append(\"## Conclusion\\n\")\n    lines.append(f\"With K=2 and Δπ=0.051, the CM heterogeneity is small.\")\n    lines.append(\"The bias reduction from stratified correction is limited, \"\n                 \"so the variance cost of estimating per-subgroup CMs must be overcome by larger n_expert.\")\n    if crossover:\n        lines.append(f\"\\nAt n_expert≥{crossover}, HB EC-HTE achieves lower RMSE than Naive, \"\n                     \"indicating the variance cost is amortized.\")\n    else:\n        lines.append(\"\\nEven at n_expert=2000, the variance cost exceeds the bias reduction. \"\n                     \"K=2 with Δπ=0.051 may be too homogeneous for EC-HTE to help.\")\n\n    report = \"\\n\".join(lines)\n    outpath = 'artifacts/c1_multi_llm/budget_sweep_k2_analysis.md'\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"K=2 Budget Sensitivity Sweep\")\n    print(f\"N={N}, n_expert_list={N_EXPERT_LIST}, n_mc={N_MC}\")\n    print(f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, Δτ={TAU_Z1-TAU_Z0:.1f}\")\n    print(\"K=2 Subgroup CMs:\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.3f}, FNR={cm['fnr']:.3f}, π={(cm['fpr']+cm['fnr'])/2:.3f}\")\n    print()\n\n    # Dry run: 1 seed, smallest budget\n    print(\"=== Dry run (1 seed, n_expert=100) ===\")\n    data = generate_data(SEED_BASE, 100)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    df_dry['n_expert'] = 100\n    print(f\"Dry run OK: {len(df_dry)} rows\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n    print()\n\n    proceed = input(\"Proceed with full run? [y/N] \").strip().lower()\n    if proceed != 'y':\n        print(\"Aborted.\")\n        exit(0)\n\n    # Full run\n    all_results = []\n    t0_total = time.time()\n\n    for ne in N_EXPERT_LIST:\n        print(f\"\\n=== n_expert={ne} ({N_MC} seeds) ===\")\n        t0 = time.time()\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            data = generate_data(seed, ne)\n            mc_rows = run_one_mc(data, seed)\n            for r in mc_rows:\n                r['n_expert'] = ne\n            all_results.extend(mc_rows)\n\n            if (mc + 1) % 10 == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / (mc + 1) * (N_MC - mc - 1)\n                print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n\n        elapsed = time.time() - t0\n        print(f\"  n_expert={ne} done in {elapsed:.1f}s\")\n\n    total_time = time.time() - t0_total\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(all_results)\n    df_summary = aggregate_results(df_raw)\n\n    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_true', 'cate_est', 'coverage']\n    df_raw[col_order].to_csv('artifacts/c1_multi_llm/budget_sweep_k2_results.csv', index=False)\n    print(f\"Saved budget_sweep_k2_results.csv ({len(df_raw)} rows)\")\n\n    write_analysis(df_summary)\n\n    print(\"\\n=== Summary ===\")\n    for ne in N_EXPERT_LIST:\n        print(f\"\\n  n_expert={ne}:\")\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                print(f\"    {m:20s}: |bias|={sub['abs_mean_bias'].mean():.4f}  \"\n                      f\"rmse={sub['rmse'].mean():.4f}  cov={sub['coverage'].mean():.3f}\")\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 11_

Running dry-run first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "uuid": "90501f2f-1567-4d9f-8e57-aa4c53e9fcc4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWo4nEqGC7a6zVgGfHauBb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8847,
      "cache_read_input_tokens": 29413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8847
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

_source line 12_

<details open><summary>🔧 Tool call — Bash · `toolu_01Qgc3a2rbhYpYNwKohH7R6x`</summary>

```json
{
  "command": "echo 'y' | python3 artifacts/c1_multi_llm/run_budget_sweep_k2.py 2>&1 | head -30",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "uuid": "e8ff6c8f-33b4-4537-b5eb-5344b6f7b5bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EWo4nEqGC7a6zVgGfHauBb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8847,
      "cache_read_input_tokens": 29413,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8847
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

_source line 13_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bd9b80sr2",
  "tool_use_id": "toolu_01Qgc3a2rbhYpYNwKohH7R6x",
  "description": "echo 'y' | python3 artifacts/c1_multi_llm/run_budget_sweep_k2.py 2>&1 | head -30",
  "task_type": "local_bash",
  "uuid": "5ed64cf0-45a6-4556-92ec-9f936555a495",
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199"
}
```

---

### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bd9b80sr2",
  "tool_use_id": "toolu_01Qgc3a2rbhYpYNwKohH7R6x",
  "status": "completed",
  "output_file": "",
  "summary": "echo 'y' | python3 artifacts/c1_multi_llm/run_budget_sweep_k2.py 2>&1 | head -30",
  "uuid": "cb3418ea-f356-488f-995c-853e562fe0e6",
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199"
}
```

---

### Tool result

_source line 15 · 2026-05-21T21:31:45.973Z_

<details><summary>↩ Tool result · `toolu_01Qgc3a2rbhYpYNwKohH7R6x`</summary>

```text
K=2 Budget Sensitivity Sweep
N=5000, n_expert_list=[100, 200, 500, 1000, 2000], n_mc=50
tau(z=0)=0.35, tau(z=1)=0.65, Δτ=0.3
K=2 Subgroup CMs:
  False: FPR=0.252, FNR=0.269, π=0.261
  True: FPR=0.186, FNR=0.233, π=0.210

=== Dry run (1 seed, n_expert=100) ===
Dry run OK: 20 rows
  oracle              : mean |bias| = 0.0465
  naive               : mean |bias| = 0.0626
  global_corrected    : mean |bias| = 0.2893
  stratified_mle      : mean |bias| = 0.3114
  hb_ec_hte           : mean |bias| = 0.3143

Proceed with full run? [y/N] 
=== n_expert=100 (50 seeds) ===
  [10/50] 4s elapsed, ETA 16s
  [20/50] 8s elapsed, ETA 11s
  [30/50] 12s elapsed, ETA 8s
  [40/50] 15s elapsed, ETA 4s
  [50/50] 19s elapsed, ETA 0s
  n_expert=100 done in 18.8s

=== n_expert=200 (50 seeds) ===
  [10/50] 3s elapsed, ETA 14s
  [20/50] 7s elapsed, ETA 11s
  [30/50] 11s elapsed, ETA 7s
  [40/50] 14s elapsed, ETA 4s
  [50/50] 18s elapsed, ETA 0s
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "uuid": "d181a2cd-c673-4612-a430-7bdc6978bf4d",
  "tool_use_result": {
    "stdout": "K=2 Budget Sensitivity Sweep\nN=5000, n_expert_list=[100, 200, 500, 1000, 2000], n_mc=50\ntau(z=0)=0.35, tau(z=1)=0.65, Δτ=0.3\nK=2 Subgroup CMs:\n  False: FPR=0.252, FNR=0.269, π=0.261\n  True: FPR=0.186, FNR=0.233, π=0.210\n\n=== Dry run (1 seed, n_expert=100) ===\nDry run OK: 20 rows\n  oracle              : mean |bias| = 0.0465\n  naive               : mean |bias| = 0.0626\n  global_corrected    : mean |bias| = 0.2893\n  stratified_mle      : mean |bias| = 0.3114\n  hb_ec_hte           : mean |bias| = 0.3143\n\nProceed with full run? [y/N] \n=== n_expert=100 (50 seeds) ===\n  [10/50] 4s elapsed, ETA 16s\n  [20/50] 8s elapsed, ETA 11s\n  [30/50] 12s elapsed, ETA 8s\n  [40/50] 15s elapsed, ETA 4s\n  [50/50] 19s elapsed, ETA 0s\n  n_expert=100 done in 18.8s\n\n=== n_expert=200 (50 seeds) ===\n  [10/50] 3s elapsed, ETA 14s\n  [20/50] 7s elapsed, ETA 11s\n  [30/50] 11s elapsed, ETA 7s\n  [40/50] 14s elapsed, ETA 4s\n  [50/50] 18s elapsed, ETA 0s",
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

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Dry run looks good. Let me wait for the full run to complete.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "uuid": "a445e685-47be-4b67-9eb1-37c9a84a0066",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpyxVZTpkkuq7hvS2j96Zw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 607,
      "cache_read_input_tokens": 38260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 607
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

### Assistant

_source line 17_

Dry run passed. Waiting for full run to complete.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "uuid": "a39b05c5-fa5f-451e-aabb-975c630ae20b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpyxVZTpkkuq7hvS2j96Zw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 607,
      "cache_read_input_tokens": 38260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 607
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

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01KKJy5Xh7obVksf9rKzJb95`</summary>

```json
{
  "command": "echo 'y' | python3 artifacts/c1_multi_llm/run_budget_sweep_k2.py 2>&1 | tail -50",
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
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "uuid": "ad05276f-c806-4ef7-9ce4-87085624bf50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BpyxVZTpkkuq7hvS2j96Zw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 607,
      "cache_read_input_tokens": 38260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 607
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

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bsswx2k4j",
  "tool_use_id": "toolu_01KKJy5Xh7obVksf9rKzJb95",
  "description": "echo 'y' | python3 artifacts/c1_multi_llm/run_budget_sweep_k2.py 2>&1 | tail -50",
  "task_type": "local_bash",
  "uuid": "66e2d48f-6c32-4561-8654-3d052733ad7a",
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199"
}
```

---

### System

_source line 20_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bsswx2k4j",
  "tool_use_id": "toolu_01KKJy5Xh7obVksf9rKzJb95",
  "status": "completed",
  "output_file": "",
  "summary": "echo 'y' | python3 artifacts/c1_multi_llm/run_budget_sweep_k2.py 2>&1 | tail -50",
  "uuid": "bfb360f8-f077-4fa9-b801-6cafa7ee3b72",
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199"
}
```

---

### Tool result

_source line 21 · 2026-05-21T21:33:25.150Z_

<details><summary>↩ Tool result · `toolu_01KKJy5Xh7obVksf9rKzJb95`</summary>

```text
  [10/50] 4s elapsed, ETA 15s
  [20/50] 7s elapsed, ETA 11s
  [30/50] 11s elapsed, ETA 7s
  [40/50] 15s elapsed, ETA 4s
  [50/50] 18s elapsed, ETA 0s
  n_expert=1000 done in 18.2s

=== n_expert=2000 (50 seeds) ===
  [10/50] 4s elapsed, ETA 15s
  [20/50] 8s elapsed, ETA 11s
  [30/50] 11s elapsed, ETA 7s
  [40/50] 15s elapsed, ETA 4s
  [50/50] 18s elapsed, ETA 0s
  n_expert=2000 done in 18.5s

Total time: 92.2s
Saved budget_sweep_k2_results.csv (5000 rows)
Wrote artifacts/c1_multi_llm/budget_sweep_k2_analysis.md

=== Summary ===

  n_expert=100:
    naive               : |bias|=0.0819  rmse=0.1000  cov=0.675
    global_corrected    : |bias|=0.0094  rmse=0.1456  cov=0.840
    stratified_mle      : |bias|=0.0128  rmse=0.1905  cov=0.745
    hb_ec_hte           : |bias|=0.0116  rmse=0.1927  cov=0.745

  n_expert=200:
    naive               : |bias|=0.0819  rmse=0.1000  cov=0.675
    global_corrected    : |bias|=0.0161  rmse=0.1223  cov=0.860
    stratified_mle      : |bias|=0.0179  rmse=0.1540  cov=0.775
    hb_ec_hte           : |bias|=0.0168  rmse=0.1557  cov=0.780

  n_expert=500:
    naive               : |bias|=0.0819  rmse=0.1000  cov=0.675
    global_corrected    : |bias|=0.0132  rmse=0.1070  cov=0.925
    stratified_mle      : |bias|=0.0128  rmse=0.1239  cov=0.900
    hb_ec_hte           : |bias|=0.0125  rmse=0.1242  cov=0.905

  n_expert=1000:
    naive               : |bias|=0.0819  rmse=0.1000  cov=0.675
    global_corrected    : |bias|=0.0073  rmse=0.0952  cov=0.960
    stratified_mle      : |bias|=0.0065  rmse=0.0999  cov=0.940
    hb_ec_hte           : |bias|=0.0065  rmse=0.0997  cov=0.940

  n_expert=2000:
    naive               : |bias|=0.0819  rmse=0.1000  cov=0.675
    global_corrected    : |bias|=0.0069  rmse=0.0908  cov=0.955
    stratified_mle      : |bias|=0.0137  rmse=0.0921  cov=0.950
    hb_ec_hte           : |bias|=0.0137  rmse=0.0920  cov=0.950
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "uuid": "1dfa07c3-5351-4e1e-8836-76a52c9d3d4c",
  "tool_use_result": {
    "stdout": "  [10/50] 4s elapsed, ETA 15s\n  [20/50] 7s elapsed, ETA 11s\n  [30/50] 11s elapsed, ETA 7s\n  [40/50] 15s elapsed, ETA 4s\n  [50/50] 18s elapsed, ETA 0s\n  n_expert=1000 done in 18.2s\n\n=== n_expert=2000 (50 seeds) ===\n  [10/50] 4s elapsed, ETA 15s\n  [20/50] 8s elapsed, ETA 11s\n  [30/50] 11s elapsed, ETA 7s\n  [40/50] 15s elapsed, ETA 4s\n  [50/50] 18s elapsed, ETA 0s\n  n_expert=2000 done in 18.5s\n\nTotal time: 92.2s\nSaved budget_sweep_k2_results.csv (5000 rows)\nWrote artifacts/c1_multi_llm/budget_sweep_k2_analysis.md\n\n=== Summary ===\n\n  n_expert=100:\n    naive               : |bias|=0.0819  rmse=0.1000  cov=0.675\n    global_corrected    : |bias|=0.0094  rmse=0.1456  cov=0.840\n    stratified_mle      : |bias|=0.0128  rmse=0.1905  cov=0.745\n    hb_ec_hte           : |bias|=0.0116  rmse=0.1927  cov=0.745\n\n  n_expert=200:\n    naive               : |bias|=0.0819  rmse=0.1000  cov=0.675\n    global_corrected    : |bias|=0.0161  rmse=0.1223  cov=0.860\n    stratified_mle      : |bias|=0.0179  rmse=0.1540  cov=0.775\n    hb_ec_hte           : |bias|=0.0168  rmse=0.1557  cov=0.780\n\n  n_expert=500:\n    naive               : |bias|=0.0819  rmse=0.1000  cov=0.675\n    global_corrected    : |bias|=0.0132  rmse=0.1070  cov=0.925\n    stratified_mle      : |bias|=0.0128  rmse=0.1239  cov=0.900\n    hb_ec_hte           : |bias|=0.0125  rmse=0.1242  cov=0.905\n\n  n_expert=1000:\n    naive               : |bias|=0.0819  rmse=0.1000  cov=0.675\n    global_corrected    : |bias|=0.0073  rmse=0.0952  cov=0.960\n    stratified_mle      : |bias|=0.0065  rmse=0.0999  cov=0.940\n    hb_ec_hte           : |bias|=0.0065  rmse=0.0997  cov=0.940\n\n  n_expert=2000:\n    naive               : |bias|=0.0819  rmse=0.1000  cov=0.675\n    global_corrected    : |bias|=0.0069  rmse=0.0908  cov=0.955\n    stratified_mle      : |bias|=0.0137  rmse=0.0921  cov=0.950\n    hb_ec_hte           : |bias|=0.0137  rmse=0.0920  cov=0.950",
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

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01MYwtsJfGSw1CCxSDZJL59C`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/budget_sweep_k2_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "uuid": "9f7cb5ba-225f-4f52-8a83-8f3f3559235e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EZ9jVNixoMg6vUoJj8eqcS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1106,
      "cache_read_input_tokens": 38867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1106
      },
      "output_tokens": 34,
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

_source line 23 · 2026-05-21T21:33:28.418Z_

<details><summary>↩ Tool result · `toolu_01MYwtsJfGSw1CCxSDZJL59C`</summary>

```text
1	# K=2 Budget Sensitivity Sweep: Llama-3.1-8B Real CMs
2	
3	## Design
4	
5	Merged subgroups by `has_hashtag` (K=2).
6	
7	| Subgroup | Weight | FPR | FNR | π_s |
8	|----------|--------|-----|-----|-----|
9	| False | 0.604 | 0.252 | 0.269 | 0.261 |
10	| True | 0.396 | 0.186 | 0.233 | 0.210 |
11	
12	Δπ = |π_False - π_True| = |0.261 - 0.210| = 0.051
13	
14	N=5000, P(Z=1)=0.652, τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3
15	n_expert ∈ [100, 200, 500, 1000, 2000], 50 MC seeds per budget
16	
17	## Summary by n_expert
18	
19	| n_expert | Method | |Bias| | RMSE | Coverage |
20	|----------|--------|-------|------|----------|
21	| 100 | naive | 0.0819 | 0.1000 | 0.675 |
22	| 100 | global_corrected | 0.0094 | 0.1456 | 0.840 |
23	| 100 | stratified_mle | 0.0128 | 0.1905 | 0.745 |
24	| 100 | hb_ec_hte | 0.0116 | 0.1927 | 0.745 |
25	|---|---|---|---|---|
26	| 200 | naive | 0.0819 | 0.1000 | 0.675 |
27	| 200 | global_corrected | 0.0161 | 0.1223 | 0.860 |
28	| 200 | stratified_mle | 0.0179 | 0.1540 | 0.775 |
29	| 200 | hb_ec_hte | 0.0168 | 0.1557 | 0.780 |
30	|---|---|---|---|---|
31	| 500 | naive | 0.0819 | 0.1000 | 0.675 |
32	| 500 | global_corrected | 0.0132 | 0.1070 | 0.925 |
33	| 500 | stratified_mle | 0.0128 | 0.1239 | 0.900 |
34	| 500 | hb_ec_hte | 0.0125 | 0.1242 | 0.905 |
35	|---|---|---|---|---|
36	| 1000 | naive | 0.0819 | 0.1000 | 0.675 |
37	| 1000 | global_corrected | 0.0073 | 0.0952 | 0.960 |
38	| 1000 | stratified_mle | 0.0065 | 0.0999 | 0.940 |
39	| 1000 | hb_ec_hte | 0.0065 | 0.0997 | 0.940 |
40	|---|---|---|---|---|
41	| 2000 | naive | 0.0819 | 0.1000 | 0.675 |
42	| 2000 | global_corrected | 0.0069 | 0.0908 | 0.955 |
43	| 2000 | stratified_mle | 0.0137 | 0.0921 | 0.950 |
44	| 2000 | hb_ec_hte | 0.0137 | 0.0920 | 0.950 |
45	|---|---|---|---|---|
46	
47	## RMSE Ratio: EC-HTE / Naive
48	
49	| n_expert | Naive RMSE | HB RMSE | Ratio | HB wins? |
50	|----------|-----------|---------|-------|----------|
51	| 100 | 0.1000 | 0.1927 | 1.928 | no |
52	| 200 | 0.1000 | 0.1557 | 1.557 | no |
53	| 500 | 0.1000 | 0.1242 | 1.243 | no |
54	| 1000 | 0.1000 | 0.0997 | 0.998 | YES |
55	| 2000 | 0.1000 | 0.0920 | 0.921 | YES |
56	
57	## |Bias| Ratio: EC-HTE / Naive
58	
59	| n_expert | Naive |Bias| | HB |Bias| | Ratio | HB wins? |
60	|----------|-----------|---------|-------|----------|
61	| 100 | 0.0819 | 0.0116 | 0.141 | YES |
62	| 200 | 0.0819 | 0.0168 | 0.206 | YES |
63	| 500 | 0.0819 | 0.0125 | 0.152 | YES |
64	| 1000 | 0.0819 | 0.0065 | 0.080 | YES |
65	| 2000 | 0.0819 | 0.0137 | 0.167 | YES |
66	
67	## Bias-Variance Decomposition
68	
69	| n_expert | Method | Bias² | Var | MSE |
70	|----------|--------|-------|-----|-----|
71	| 100 | naive | 0.0082 | 0.0029 | 0.0111 |
72	| 100 | global_corrected | 0.0001 | 0.0227 | 0.0228 |
73	| 100 | hb_ec_hte | 0.0002 | 0.0410 | 0.0412 |
74	|---|---|---|---|---|
75	| 200 | naive | 0.0082 | 0.0029 | 0.0111 |
76	| 200 | global_corrected | 0.0004 | 0.0158 | 0.0161 |
77	| 200 | hb_ec_hte | 0.0003 | 0.0261 | 0.0264 |
78	|---|---|---|---|---|
79	| 500 | naive | 0.0082 | 0.0029 | 0.0111 |
80	| 500 | global_corrected | 0.0002 | 0.0121 | 0.0123 |
81	| 500 | hb_ec_hte | 0.0003 | 0.0165 | 0.0168 |
82	|---|---|---|---|---|
83	| 1000 | naive | 0.0082 | 0.0029 | 0.0111 |
84	| 1000 | global_corrected | 0.0001 | 0.0096 | 0.0097 |
85	| 1000 | hb_ec_hte | 0.0001 | 0.0105 | 0.0106 |
86	|---|---|---|---|---|
87	| 2000 | naive | 0.0082 | 0.0029 | 0.0111 |
88	| 2000 | global_corrected | 0.0001 | 0.0088 | 0.0088 |
89	| 2000 | hb_ec_hte | 0.0003 | 0.0087 | 0.0090 |
90	|---|---|---|---|---|
91	
92	## Crossover Analysis
93	
94	**RMSE crossover**: EC-HTE first beats Naive at n_expert=1000
95	**|Bias| crossover**: EC-HTE first beats Naive at n_expert=100
96	
97	## Conclusion
98	
99	With K=2 and Δπ=0.051, the CM heterogeneity is small.
100	The bias reduction from stratified correction is limited, so the variance cost of estimating per-subgroup CMs must be overcome by larger n_expert.
101	
102	At n_expert≥1000, HB EC-HTE achieves lower RMSE than Naive, indicating the variance cost is amortized.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "uuid": "9f0077f1-aaa5-4119-b21c-27a15a4d5902",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/budget_sweep_k2_analysis.md",
      "content": "# K=2 Budget Sensitivity Sweep: Llama-3.1-8B Real CMs\n\n## Design\n\nMerged subgroups by `has_hashtag` (K=2).\n\n| Subgroup | Weight | FPR | FNR | π_s |\n|----------|--------|-----|-----|-----|\n| False | 0.604 | 0.252 | 0.269 | 0.261 |\n| True | 0.396 | 0.186 | 0.233 | 0.210 |\n\nΔπ = |π_False - π_True| = |0.261 - 0.210| = 0.051\n\nN=5000, P(Z=1)=0.652, τ(z=0)=0.35, τ(z=1)=0.65, Δτ=0.3\nn_expert ∈ [100, 200, 500, 1000, 2000], 50 MC seeds per budget\n\n## Summary by n_expert\n\n| n_expert | Method | |Bias| | RMSE | Coverage |\n|----------|--------|-------|------|----------|\n| 100 | naive | 0.0819 | 0.1000 | 0.675 |\n| 100 | global_corrected | 0.0094 | 0.1456 | 0.840 |\n| 100 | stratified_mle | 0.0128 | 0.1905 | 0.745 |\n| 100 | hb_ec_hte | 0.0116 | 0.1927 | 0.745 |\n|---|---|---|---|---|\n| 200 | naive | 0.0819 | 0.1000 | 0.675 |\n| 200 | global_corrected | 0.0161 | 0.1223 | 0.860 |\n| 200 | stratified_mle | 0.0179 | 0.1540 | 0.775 |\n| 200 | hb_ec_hte | 0.0168 | 0.1557 | 0.780 |\n|---|---|---|---|---|\n| 500 | naive | 0.0819 | 0.1000 | 0.675 |\n| 500 | global_corrected | 0.0132 | 0.1070 | 0.925 |\n| 500 | stratified_mle | 0.0128 | 0.1239 | 0.900 |\n| 500 | hb_ec_hte | 0.0125 | 0.1242 | 0.905 |\n|---|---|---|---|---|\n| 1000 | naive | 0.0819 | 0.1000 | 0.675 |\n| 1000 | global_corrected | 0.0073 | 0.0952 | 0.960 |\n| 1000 | stratified_mle | 0.0065 | 0.0999 | 0.940 |\n| 1000 | hb_ec_hte | 0.0065 | 0.0997 | 0.940 |\n|---|---|---|---|---|\n| 2000 | naive | 0.0819 | 0.1000 | 0.675 |\n| 2000 | global_corrected | 0.0069 | 0.0908 | 0.955 |\n| 2000 | stratified_mle | 0.0137 | 0.0921 | 0.950 |\n| 2000 | hb_ec_hte | 0.0137 | 0.0920 | 0.950 |\n|---|---|---|---|---|\n\n## RMSE Ratio: EC-HTE / Naive\n\n| n_expert | Naive RMSE | HB RMSE | Ratio | HB wins? |\n|----------|-----------|---------|-------|----------|\n| 100 | 0.1000 | 0.1927 | 1.928 | no |\n| 200 | 0.1000 | 0.1557 | 1.557 | no |\n| 500 | 0.1000 | 0.1242 | 1.243 | no |\n| 1000 | 0.1000 | 0.0997 | 0.998 | YES |\n| 2000 | 0.1000 | 0.0920 | 0.921 | YES |\n\n## |Bias| Ratio: EC-HTE / Naive\n\n| n_expert | Naive |Bias| | HB |Bias| | Ratio | HB wins? |\n|----------|-----------|---------|-------|----------|\n| 100 | 0.0819 | 0.0116 | 0.141 | YES |\n| 200 | 0.0819 | 0.0168 | 0.206 | YES |\n| 500 | 0.0819 | 0.0125 | 0.152 | YES |\n| 1000 | 0.0819 | 0.0065 | 0.080 | YES |\n| 2000 | 0.0819 | 0.0137 | 0.167 | YES |\n\n## Bias-Variance Decomposition\n\n| n_expert | Method | Bias² | Var | MSE |\n|----------|--------|-------|-----|-----|\n| 100 | naive | 0.0082 | 0.0029 | 0.0111 |\n| 100 | global_corrected | 0.0001 | 0.0227 | 0.0228 |\n| 100 | hb_ec_hte | 0.0002 | 0.0410 | 0.0412 |\n|---|---|---|---|---|\n| 200 | naive | 0.0082 | 0.0029 | 0.0111 |\n| 200 | global_corrected | 0.0004 | 0.0158 | 0.0161 |\n| 200 | hb_ec_hte | 0.0003 | 0.0261 | 0.0264 |\n|---|---|---|---|---|\n| 500 | naive | 0.0082 | 0.0029 | 0.0111 |\n| 500 | global_corrected | 0.0002 | 0.0121 | 0.0123 |\n| 500 | hb_ec_hte | 0.0003 | 0.0165 | 0.0168 |\n|---|---|---|---|---|\n| 1000 | naive | 0.0082 | 0.0029 | 0.0111 |\n| 1000 | global_corrected | 0.0001 | 0.0096 | 0.0097 |\n| 1000 | hb_ec_hte | 0.0001 | 0.0105 | 0.0106 |\n|---|---|---|---|---|\n| 2000 | naive | 0.0082 | 0.0029 | 0.0111 |\n| 2000 | global_corrected | 0.0001 | 0.0088 | 0.0088 |\n| 2000 | hb_ec_hte | 0.0003 | 0.0087 | 0.0090 |\n|---|---|---|---|---|\n\n## Crossover Analysis\n\n**RMSE crossover**: EC-HTE first beats Naive at n_expert=1000\n**|Bias| crossover**: EC-HTE first beats Naive at n_expert=100\n\n## Conclusion\n\nWith K=2 and Δπ=0.051, the CM heterogeneity is small.\nThe bias reduction from stratified correction is limited, so the variance cost of estimating per-subgroup CMs must be overcome by larger n_expert.\n\nAt n_expert≥1000, HB EC-HTE achieves lower RMSE than Naive, indicating the variance cost is amortized.",
      "numLines": 102,
      "startLine": 1,
      "totalLines": 102
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
The results are interesting. Let me also note that the Global corrected method actually beats HB EC-HTE at every budget level in terms of RMSE. This makes sense because with K=2 and Δπ=0.051, the heterogeneity is so small that a single global CM is more efficient than per-subgroup CMs.

Key findings:
- RMSE crossover for HB EC-HTE vs Naive: n_expert=1000
- Global corrected beats Naive starting at n_expert=1000 (RMSE 0.0952 vs 0.1000)


- At n_expert=500, Global corrected is close but still slightly higher than Naive, and HB EC-HTE never outperforms Global corrected since the minimal heterogeneity doesn't justify the added variance from per-subgroup estimation

The results are complete and saved, so I should verify the CSV file exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "uuid": "d7e29486-4921-413c-970b-ab30cd455d8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U36KUobit4gAJ3B1zizdGh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2375,
      "cache_read_input_tokens": 39973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2375
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

Run complete (92s). Both outputs saved.

**Key results:**

| n_expert | Naive RMSE | Global RMSE | HB EC-HTE RMSE | HB/Naive |
|----------|-----------|-------------|----------------|----------|
| 100 | 0.1000 | 0.1456 | 0.1927 | 1.93 |
| 200 | 0.1000 | 0.1223 | 0.1557 | 1.56 |
| 500 | 0.1000 | 0.1070 | 0.1242 | 1.24 |
| **1000** | **0.1000** | **0.0952** | **0.0997** | **1.00** |
| 2000 | 0.1000 | 0.0908 | 0.0920 | 0.92 |

**Findings:**
- **RMSE crossover at n_expert=1000** — HB EC-HTE just barely beats Naive (ratio=0.998)
- **|Bias| is always lower for HB** (5-8x reduction over Naive at all budgets), but variance inflation dominates until n_expert≈1000
- **Global corrected dominates HB EC-HTE at every budget** — with Δπ=0.051, the per-subgroup CM heterogeneity is too small to justify the extra variance from stratified estimation
- Bias-variance decomposition confirms: Naive has Bias²=0.0082 (stable), HB trades this for Var that shrinks from 0.041→0.009 as n_expert grows

**Bottom line:** K=2 merging reduced Δπ from 0.137 (K=4) to 0.051, pushing the crossover from ~200 to ~1000. The global corrected estimator (single CM) is the best choice here since CM heterogeneity is negligible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "uuid": "00da803f-7e1f-45b6-860a-39d08715e440",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U36KUobit4gAJ3B1zizdGh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2375,
      "cache_read_input_tokens": 39973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2375
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

_source line 26_

Run complete (92s). Both outputs saved.

**Key results:**

| n_expert | Naive RMSE | Global RMSE | HB EC-HTE RMSE | HB/Naive |
|----------|-----------|-------------|----------------|----------|
| 100 | 0.1000 | 0.1456 | 0.1927 | 1.93 |
| 200 | 0.1000 | 0.1223 | 0.1557 | 1.56 |
| 500 | 0.1000 | 0.1070 | 0.1242 | 1.24 |
| **1000** | **0.1000** | **0.0952** | **0.0997** | **1.00** |
| 2000 | 0.1000 | 0.0908 | 0.0920 | 0.92 |

**Findings:**
- **RMSE crossover at n_expert=1000** — HB EC-HTE just barely beats Naive (ratio=0.998)
- **|Bias| is always lower for HB** (5-8x reduction over Naive at all budgets), but variance inflation dominates until n_expert≈1000
- **Global corrected dominates HB EC-HTE at every budget** — with Δπ=0.051, the per-subgroup CM heterogeneity is too small to justify the extra variance from stratified estimation
- Bias-variance decomposition confirms: Naive has Bias²=0.0082 (stable), HB trades this for Var that shrinks from 0.041→0.009 as n_expert grows

**Bottom line:** K=2 merging reduced Δπ from 0.137 (K=4) to 0.051, pushing the crossover from ~200 to ~1000. The global corrected estimator (single CM) is the best choice here since CM heterogeneity is negligible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 338017,
  "duration_api_ms": 152673,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "abb9cd85-6e8d-4bd2-8854-ae066bab6199",
  "total_cost_usd": 0.5316112500000001,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 30507,
    "cache_read_input_tokens": 176787,
    "output_tokens": 10028,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 30507,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 749,
        "cache_read_input_tokens": 39973,
        "cache_creation_input_tokens": 2375,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2375
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1694,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001809,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 10028,
      "cacheReadInputTokens": 176787,
      "cacheCreationInputTokens": 30507,
      "webSearchRequests": 0,
      "costUSD": 0.52980225,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3e60e80e-a9ef-4d67-93e2-452a1d58f39b"
}
```

</details>

---
