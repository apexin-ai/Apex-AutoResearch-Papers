# code exp 001 hyperprior

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_code_exp-001-hyperprior_20260520T220653.log`
- **Structured JSON:** [`347737dea5241391ca63.json`](../../sessions/34/347737dea5241391ca63.json)

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
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
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
    "mcp__agent-ml-research__allocate_and_submit",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__approve_worker",
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__backup_project_to_s3",
    "mcp__agent-ml-research__cancel_worker",
    "mcp__agent-ml-research__check_job_status",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__distill_papers",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__feishu_read_tum_pending_key",
    "mcp__agent-ml-research__feishu_send_alert",
    "mcp__agent-ml-research__feishu_send_approval_card",
    "mcp__agent-ml-research__feishu_send_result_card",
    "mcp__agent-ml-research__feishu_send_tum_key_request_card",
    "mcp__agent-ml-research__fetch_wandb_metrics",
    "mcp__agent-ml-research__get_baseline_metrics",
    "mcp__agent-ml-research__get_distill_status",
    "mcp__agent-ml-research__get_gpu_health",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_matrix_value",
    "mcp__agent-ml-research__get_project_resource_usage",
    "mcp__agent-ml-research__get_tum_config",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__impact_analysis",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_available_gpus",
    "mcp__agent-ml-research__list_constraints",
    "mcp__agent-ml-research__list_s3_backups",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__main_agent_post_to_director",
    "mcp__agent-ml-research__matrix_gap_analysis",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__poll_cron",
    "mcp__agent-ml-research__poll_secret_request",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_matrix",
    "mcp__agent-ml-research__read_mistakes",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__reconcile_crons",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__register_cron",
    "mcp__agent-ml-research__request_secret",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__submit_on_allocated",
    "mcp__agent-ml-research__submit_training_job",
    "mcp__agent-ml-research__sync_matrix_status",
    "mcp__agent-ml-research__tail_training_logs",
    "mcp__agent-ml-research__update_baseline",
    "mcp__agent-ml-research__update_matrix",
    "mcp__agent-ml-research__update_registry",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
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
  "uuid": "0061da1b-689d-4e77-aead-e50ece071182",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-ec-hte-llm-annotation/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Assistant

_source line 3_

I'll start by reading the current Gibbs sampler code to understand the hyperprior setup.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "ac53a54d-3702-4cd1-a1f2-3995df59c8e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzU9JFJyD6MGjfRuCYzLVe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7370,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7370
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

_source line 4_

<details open><summary>🔧 Tool call — Read · `toolu_018WX6SPEiNPxNWiKFaC9yCB`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "121d5e43-fdeb-4053-9055-40e824e60dac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NzU9JFJyD6MGjfRuCYzLVe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7370,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7370
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

### Runtime record

_source line 5_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779326400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "24e5a196-f8d8-46e1-a3e2-77a34b0bb4b1",
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92"
}
```

---

### Tool result

_source line 6 · 2026-05-20T22:07:05.236Z_

<details><summary>↩ Tool result · `toolu_018WX6SPEiNPxNWiKFaC9yCB`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	exp001_hb_synthetic.py - Hierarchical Bayesian EC-HTE Synthetic Validation (exp-001)
4	
5	Compares confusion matrix estimators for CATE correction under heterogeneous
6	misclassification across subgroups:
7	  Oracle, Naive, Global-corrected, MLE (Laplace), HB Dirichlet (partial pooling)
8	
9	Input: Synthetic DGP parameters (regimes, expert budgets, subgroup counts)
10	Output: results/exp001_hb_results.csv, results/exp001_hb_diagnostics.csv
11	"""
12	
13	import argparse
14	import os
15	import sys
16	import time
17	import warnings
18	import numpy as np
19	import pandas as pd
20	from scipy.special import gammaln
21	from scipy.optimize import minimize_scalar
22	
23	warnings.filterwarnings('ignore')
24	
25	try:
26	    import pymc as pm
27	    import pytensor.tensor as pt
28	    import arviz as az
29	    HAS_PYMC = True
30	except ImportError:
31	    HAS_PYMC = False
32	
33	N = 5000
34	SUBGROUP_LABELS = {2: ['A', 'B'], 4: ['A', 'B', 'C', 'D']}
35	
36	REGIMES = {
37	    2: {
38	        'extreme':     {'misclass': [0.25, 0.05], 'tau_z1': 0.5, 'tau_z0': 0.1},
39	        'moderate':    {'misclass': [0.15, 0.10], 'tau_z1': 0.3, 'tau_z0': 0.15},
40	        'homogeneous': {'misclass': [0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
41	    },
42	    4: {
43	        'extreme':     {'misclass': [0.30, 0.20, 0.10, 0.03], 'tau_z1': 0.5, 'tau_z0': 0.1},
44	        'moderate':    {'misclass': [0.20, 0.15, 0.10, 0.05], 'tau_z1': 0.3, 'tau_z0': 0.15},
45	        'homogeneous': {'misclass': [0.12, 0.12, 0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
46	    },
47	}
48	
49	DEFAULT_N_EXPERTS = [50, 100, 250, 500, 1000, 2000]
50	DEFAULT_K_LIST = [2, 4]
51	
52	
53	# ── DGP ───────────────────────────────────────────────────────────────────────
54	
55	def generate_data(regime_params, n_expert, k, seed):
56	    rng = np.random.RandomState(seed)
57	    labels = SUBGROUP_LABELS[k]
58	    T = rng.binomial(1, 0.5, N)
59	    Z = rng.binomial(1, 0.5, N)
60	    S = rng.choice(labels, N, p=[1.0 / k] * k)
61	    X = rng.randn(N, 5)
62	    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])
63	    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)
64	    mc_rates = np.zeros(N)
65	    for i, s in enumerate(labels):
66	        mc_rates[S == s] = regime_params['misclass'][i]
67	    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)
68	    idx = rng.choice(N, min(n_expert, N), replace=False)
69	    expert_mask = np.zeros(N, dtype=bool)
70	    expert_mask[idx] = True
71	    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, X=X, Y=Y, tau=tau, expert_mask=expert_mask)
72	
73	
74	# ── Helpers ───────────────────────────────────────────────────────────────────
75	
76	def diff_in_means(Y, T, mask):
77	    t1, t0 = mask & (T == 1), mask & (T == 0)
78	    n1, n0 = t1.sum(), t0.sum()
79	    if n1 < 2 or n0 < 2:
80	        return np.nan, np.nan
81	    y1, y0 = Y[t1], Y[t0]
82	    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
83	
84	
85	def get_counts(z_true, z_hat, subgroups, labels):
86	    """Confusion matrix counts per subgroup: (k, 2, 2) = [subgroup, true_z, z_hat]."""
87	    k = len(labels)
88	    counts = np.zeros((k, 2, 2), dtype=int)
89	    for i, s in enumerate(labels):
90	        ms = subgroups == s
91	        for z in [0, 1]:
92	            mz = ms & (z_true == z)
93	            counts[i, z, 0] = (z_hat[mz] == 0).sum()
94	            counts[i, z, 1] = (z_hat[mz] == 1).sum()
95	    return counts
96	
97	
98	def build_mixing_matrix(C):
99	    """C[z, z_hat] → M[z_hat, z] via Bayes rule (assuming P(Z=0)=P(Z=1)=0.5)."""
100	    M = np.zeros((2, 2))
101	    for zh in [0, 1]:
102	        cs = C[0, zh] + C[1, zh]
103	        if cs > 0:
104	            M[zh, 0] = C[0, zh] / cs
105	            M[zh, 1] = C[1, zh] / cs
106	        else:
107	            M[zh, :] = 0.5
108	    return M
109	
110	
111	def invert_mixing(M, tau_obs, se_obs):
112	    det = np.linalg.det(M)
113	    if abs(det) < 1e-10:
114	        return tau_obs.copy(), se_obs.copy()
115	    Mi = np.linalg.inv(M)
116	    tau_c = Mi @ tau_obs
117	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
118	    return tau_c, se_c
119	
120	
121	def safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):
122	    """Invert mixing matrix with condition number guard.
123	
124	    When cond(M_s) > threshold, matrix inversion is numerically unstable.
125	    Falls back to naive (no correction) to avoid catastrophic amplification.
126	    """
127	    cond = np.linalg.cond(M_s)
128	    if cond > cond_threshold:
129	        return tau_obs.copy()
130	    return np.linalg.solve(M_s, tau_obs)
131	
132	
133	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
134	    """Like invert_mixing but with condition number guard."""
135	    cond = np.linalg.cond(M)
136	    if cond > cond_threshold:
137	        return tau_obs.copy(), se_obs.copy()
138	    det = np.linalg.det(M)
139	    if abs(det) < 1e-10:
140	        return tau_obs.copy(), se_obs.copy()
141	    Mi = np.linalg.inv(M)
142	    tau_c = Mi @ tau_obs
143	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
144	    return tau_c, se_c
145	
146	
147	# ── Confusion Matrix Estimators ───────────────────────────────────────────────
148	
149	def estimate_cm_mle(counts, labels):
150	    """Per-subgroup MLE with Laplace smoothing (add-1)."""
151	    C = {}
152	    for i, s in enumerate(labels):
153	        C_s = np.zeros((2, 2))
154	        for z in [0, 1]:
155	            n = counts[i, z, :].sum()
156	            for zh in [0, 1]:
157	                C_s[z, zh] = (counts[i, z, zh] + 1) / (n + 2) if n > 0 else 0.5
158	        C[s] = C_s
159	    return C
160	
161	
162	def _dirmult_neg_ll(alpha, counts_z):
163	    """Negative log marginal likelihood for Dirichlet-Multinomial."""
164	    a = alpha / 2.0
165	    if a < 1e-10:
166	        return 1e10
167	    ll = 0.0
168	    for c0, c1 in counts_z:
169	        n = c0 + c1
170	        if n == 0:
171	            continue
172	        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)
173	        ll -= 2 * gammaln(a) - gammaln(2 * a)
174	    return -ll
175	
176	
177	def estimate_cm_hb_eb(counts, labels):
178	    """Empirical Bayes HB: optimize shared Dirichlet concentration, posterior mean."""
179	    k = len(labels)
180	    alpha_opt = np.zeros(2)
181	    for z in [0, 1]:
182	        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]
183	        total = sum(c0 + c1 for c0, c1 in cl)
184	        if total == 0:
185	            alpha_opt[z] = 2.0
186	            continue
187	        res = minimize_scalar(
188	            lambda a: _dirmult_neg_ll(a, cl), bounds=(0.01, 500), method='bounded')
189	        alpha_opt[z] = res.x
190	
191	    C = {}
192	    for i, s in enumerate(labels):
193	        C_s = np.zeros((2, 2))
194	        for z in [0, 1]:
195	            a = alpha_opt[z] / 2.0
196	            n = counts[i, z, :].sum()
197	            d = n + 2 * a
198	            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5
199	            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5
200	        C[s] = C_s
201	
202	    diag = {'rhat_max': np.nan, 'ess_min': np.nan, 'divergent_count': 0,
203	            'runtime_seconds': 0.0, 'hb_method': 'eb',
204	            'alpha_0_z0': alpha_opt[0], 'alpha_0_z1': alpha_opt[1]}
205	    return C, diag
206	
207	
208	def _split_rhat(chains):
209	    """Split R-hat for a scalar parameter. chains: (n_chains, n_draws)."""
210	    parts = []
211	    for c in range(chains.shape[0]):
212	        half = chains.shape[1] // 2
213	        parts.append(chains[c, :half])
214	        parts.append(chains[c, half:2 * half])
215	    parts = np.array(parts)
216	    m = parts.shape[0]
217	    n = parts.shape[1]
218	    chain_means = parts.mean(axis=1)
219	    W = np.mean(np.var(parts, axis=1, ddof=1))
220	    B = n * np.var(chain_means, ddof=1)
221	    if W < 1e-20:
222	        return 1.0
223	    var_hat = (1 - 1.0 / n) * W + B / n
224	    return float(np.sqrt(var_hat / W))
225	
226	
227	def _bulk_ess(chains):
228	    """Approximate bulk ESS via initial positive sequence. chains: (n_chains, n_draws)."""
229	    x = chains.ravel()
230	    n = len(x)
231	    mu = x.mean()
232	    xc = x - mu
233	    max_lag = min(n // 2, 300)
234	    c0 = np.dot(xc, xc)
235	    if c0 < 1e-20:
236	        return float(n)
237	    tau = 1.0
238	    for lag in range(1, max_lag - 1, 2):
239	        r1 = np.dot(xc[:n - lag], xc[lag:]) / c0
240	        r2 = np.dot(xc[:n - lag - 1], xc[lag + 1:]) / c0 if lag + 1 < n else 0
241	        pair = r1 + r2
242	        if pair < 0:
243	            break
244	        tau += 2 * pair
245	    return float(n / tau)
246	
247	
248	def _fast_diagnostics(alpha_arr, theta_arr, labels):
249	    """Compute R-hat and ESS over all parameters without arviz."""
250	    rhats, esss = [], []
251	    for d in range(alpha_arr.shape[2]):
252	        rhats.append(_split_rhat(alpha_arr[:, :, d]))
253	        esss.append(_bulk_ess(alpha_arr[:, :, d]))
254	    k = len(labels)
255	    for i in range(k):
256	        for z in [0, 1]:
257	            for zh in range(theta_arr.shape[4]):
258	                ch = theta_arr[:, :, i, z, zh]
259	                rhats.append(_split_rhat(ch))
260	                esss.append(_bulk_ess(ch))
261	    return max(rhats), min(esss)
262	
263	
264	def _log_target_alpha(alpha, theta_z):
265	    """Log posterior for alpha_0[z] in log-alpha space (includes Jacobian)."""
266	    if alpha < 1e-10:
267	        return -1e10
268	    a = alpha / 2.0
269	    k = theta_z.shape[0]
270	    lp = 2.0 * np.log(alpha) - alpha
271	    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))
272	    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))
273	    return lp
274	
275	
276	def estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=2000, n_warmup=1000, n_chains=2):
277	    """Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0)."""
278	    k = len(labels)
279	    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),
280	                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]
281	    chain_inits = chain_inits_pool[:n_chains]
282	    all_alpha, all_theta = [], []
283	    t0 = time.time()
284	
285	    for chain in range(n_chains):
286	        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)
287	        alpha = chain_inits[chain].copy()
288	        theta = np.ones((k, 2, 2)) * 0.5
289	        mh_scale = np.array([0.3, 0.3])
290	        accept_ct = np.array([0, 0])
291	        attempt_ct = np.array([0, 0])
292	
293	        alpha_samples = np.zeros((n_iter, 2))
294	        theta_samples = np.zeros((n_iter, k, 2, 2))
295	
296	        for it in range(n_warmup + n_iter):
297	            for z in [0, 1]:
298	                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0
299	                post_a = np.maximum(post_a, 1e-6)
300	                g = rng.gamma(post_a)
301	                g_sum = g.sum(axis=1, keepdims=True)
302	                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)
303	
304	            for z in [0, 1]:
305	                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])
306	                a_prop = np.exp(x_prop)
307	                log_r = (_log_target_alpha(a_prop, theta[:, z, :]) -
308	                         _log_target_alpha(alpha[z], theta[:, z, :]))
309	                accepted = np.log(rng.rand()) < log_r
310	                if accepted:
311	                    alpha[z] = a_prop
312	                if it < n_warmup:
313	                    accept_ct[z] += int(accepted)
314	                    attempt_ct[z] += 1
315	
316	            if it < n_warmup and it > 0 and it % 100 == 0:
317	                for z in [0, 1]:
318	                    rate = accept_ct[z] / max(attempt_ct[z], 1)
319	                    if rate < 0.2:
320	                        mh_scale[z] *= 0.7
321	                    elif rate > 0.5:
322	                        mh_scale[z] *= 1.3
323	                    accept_ct[z] = 0
324	                    attempt_ct[z] = 0
325	
326	            if it >= n_warmup:
327	                idx = it - n_warmup
328	                alpha_samples[idx] = alpha.copy()
329	                theta_samples[idx] = theta.copy()
330	
331	        all_alpha.append(alpha_samples)
332	        all_theta.append(theta_samples)
333	
334	    runtime = time.time() - t0
335	    alpha_arr = np.stack(all_alpha)
336	    theta_arr = np.stack(all_theta)
337	
338	    C = {}
339	    for i, s in enumerate(labels):
340	        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))
341	
342	    rhat_max, ess_min = _fast_diagnostics(alpha_arr, theta_arr, labels)
343	
344	    diag = {'rhat_max': rhat_max, 'ess_min': ess_min, 'divergent_count': 0,
345	            'runtime_seconds': runtime, 'hb_method': 'gibbs'}
346	    return C, diag
347	
348	
349	def estimate_cm_hb_mcmc(counts, labels, seed=42, draws=1000, tune=500, chains=2):
350	    """Full Bayesian HB with PyMC MCMC."""
351	    k = len(labels)
352	    n_per_sz = counts.sum(axis=2)
353	
354	    with pm.Model():
355	        alpha_0 = pm.Gamma('alpha_0', alpha=2, beta=1, shape=2)
356	        for z in [0, 1]:
357	            for i, s in enumerate(labels):
358	                nsz = int(n_per_sz[i, z])
359	                if nsz == 0:
360	                    continue
361	                a = pt.stack([alpha_0[z] / 2, alpha_0[z] / 2])
362	                theta = pm.Dirichlet(f'theta_{s}_z{z}', a=a)
363	                pm.Multinomial(f'obs_{s}_z{z}', n=nsz, p=theta,
364	                               observed=counts[i, z, :].astype('int32'))
365	        t0 = time.time()
366	        trace = pm.sample(draws=draws, tune=tune, chains=chains,
367	                          random_seed=seed, progressbar=False)
368	        runtime = time.time() - t0
369	
370	    C = {}
371	    for i, s in enumerate(labels):
372	        C_s = np.zeros((2, 2))
373	        for z in [0, 1]:
374	            vn = f'theta_{s}_z{z}'
375	            if vn in trace.posterior:
376	                C_s[z, :] = trace.posterior[vn].values.mean(axis=(0, 1))
377	            else:
378	                C_s[z, :] = 0.5
379	        C[s] = C_s
380	
381	    all_vars = list(trace.posterior.data_vars)
382	    try:
383	        summ = az.summary(trace, var_names=all_vars)
384	        rhat_max = float(summ['r_hat'].max())
385	        ess_min = float(summ['ess_bulk'].min())
386	    except Exception:
387	        rhat_max = ess_min = np.nan
388	    try:
389	        divergent = int(trace.sample_stats['diverging'].values.sum())
390	    except Exception:
391	        divergent = -1
392	
393	    diag = {'rhat_max': rhat_max, 'ess_min': ess_min,
394	            'divergent_count': divergent, 'runtime_seconds': runtime,
395	            'hb_method': 'mcmc'}
396	    return C, diag
397	
398	
399	# ── Single MC Run ─────────────────────────────────────────────────────────────
400	
401	def run_one_mc(regime_name, regime_params, n_expert, k, seed, hb_method='eb'):
402	    data = generate_data(regime_params, n_expert, k, seed)
403	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
404	    em = data['expert_mask']
405	    labels = SUBGROUP_LABELS[k]
406	    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']
407	
408	    counts = get_counts(Z[em], Z_hat[em], S[em], labels)
409	
410	    C_mle = estimate_cm_mle(counts, labels)
411	
412	    if hb_method == 'gibbs':
413	        C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed)
414	    elif hb_method == 'mcmc' and HAS_PYMC:
415	        try:
416	            C_hb, hb_diag = estimate_cm_hb_mcmc(counts, labels, seed=seed)
417	        except Exception:
418	            C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)
419	            hb_diag['hb_method'] = 'eb_fallback'
420	    else:
421	        C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)
422	
423	    # Global CM (pool all expert labels, Laplace)
424	    cg = counts.sum(axis=0)
425	    C_gl = np.zeros((2, 2))
426	    for z in [0, 1]:
427	        n = cg[z, :].sum()
428	        for zh in [0, 1]:
429	            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5
430	
431	    M_gl = build_mixing_matrix(C_gl)
432	    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}
433	    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}
434	
435	    base = {'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k, 'mc_run': seed}
436	    rows = []
437	
438	    for s in labels:
439	        sm = S == s
440	        th0_or, se0_or = diff_in_means(Y, T, sm & (Z == 0))
441	        th1_or, se1_or = diff_in_means(Y, T, sm & (Z == 1))
442	        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))
443	        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))
444	
445	        tau_obs = np.array([th0_n, th1_n])
446	        se_obs = np.array([se0_n, se1_n])
447	        if np.any(np.isnan(tau_obs)):
448	            continue
449	
450	        tgc, sgc = invert_mixing(M_gl, tau_obs, se_obs)
451	        tml, sml = invert_mixing(M_mle[s], tau_obs, se_obs)
452	        thb, shb = invert_mixing(M_hb[s], tau_obs, se_obs)
453	
454	        def mr(method, th0, th1, se0, se1):
455	            return {**base, 'subgroup': s, 'method': method,
456	                    'tau_hat_z0': th0, 'tau_hat_z1': th1,
457	                    'se_z0': se0, 'se_z1': se1,
458	                    'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}
459	
460	        rows.append(mr('oracle', th0_or, th1_or, se0_or, se1_or))
461	        rows.append(mr('naive', th0_n, th1_n, se0_n, se1_n))
462	        rows.append(mr('global_corrected', tgc[0], tgc[1], sgc[0], sgc[1]))
463	        rows.append(mr('mle_laplace', tml[0], tml[1], sml[0], sml[1]))
464	        rows.append(mr('hb_dirichlet', thb[0], thb[1], shb[0], shb[1]))
465	
466	    return rows, {**base, **hb_diag}
467	
468	
469	# ── Aggregation ───────────────────────────────────────────────────────────────
470	
471	def aggregate_results(df):
472	    rows = []
473	    grp_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method']
474	    for keys, grp in df.groupby(grp_cols):
475	        regime, n_expert, k, subgroup, method = keys
476	        row = {'regime': regime, 'n_expert': int(n_expert), 'k_subgroups': int(k),
477	               'subgroup': subgroup, 'method': method}
478	        n_mc = len(grp)
479	        for z in ['z0', 'z1']:
480	            err = grp[f'tau_hat_{z}'].values - grp[f'tau_true_{z}'].values
481	            bias = err.mean()
482	            mse = (err ** 2).mean()
483	            rmse = np.sqrt(mse)
484	            ci_lo = grp[f'tau_hat_{z}'].values - 1.96 * grp[f'se_{z}'].values
485	            ci_hi = grp[f'tau_hat_{z}'].values + 1.96 * grp[f'se_{z}'].values
486	            cov = ((ci_lo <= grp[f'tau_true_{z}'].values) &
487	                   (grp[f'tau_true_{z}'].values <= ci_hi)).mean()
488	            row[f'bias_{z}'] = bias
489	            row[f'rmse_{z}'] = rmse
490	            row[f'coverage_{z}'] = cov
491	            row[f'bias_{z}_se'] = err.std() / np.sqrt(n_mc)
492	            mse_se = (err ** 2).std() / np.sqrt(n_mc)
493	            row[f'rmse_{z}_se'] = mse_se / (2 * rmse) if rmse > 1e-10 else np.nan
494	        rows.append(row)
495	    return pd.DataFrame(rows)
496	
497	
498	# ── Output ────────────────────────────────────────────────────────────────────
499	
500	def print_summary(df_agg, df_diag):
501	    pd.set_option('display.float_format', '{:.4f}'.format)
502	
503	    # MCMC / Gibbs diagnostics
504	    if 'hb_method' in df_diag.columns:
505	        for method_label in ['gibbs', 'mcmc']:
506	            mrows = df_diag[df_diag['hb_method'] == method_label]
507	            if mrows.empty:
508	                continue
509	            print(f"\n── {method_label.upper()} Diagnostics ──────────────────────────────")
510	            print(f"  Runs:           {len(mrows)}")
511	            rh = mrows['rhat_max'].dropna()
512	            es = mrows['ess_min'].dropna()
513	            if not rh.empty:
514	                print(f"  R-hat max:      {rh.max():.4f} (target < 1.01)")
515	            if not es.empty:
516	                print(f"  ESS min:        {es.min():.0f} (target > 200)")
517	            print(f"  Divergent total:{int(mrows['divergent_count'].sum())}")
518	            print(f"  Runtime median: {mrows['runtime_seconds'].median():.2f}s")
519	
520	    # Per-config HB vs MLE comparison
521	    print("\n── HB vs MLE RMSE Comparison (subgroup-level, averaged) ──")
522	    for k in sorted(df_agg['k_subgroups'].unique()):
523	        print(f"\n  K = {int(k)} subgroups")
524	        for regime in ['extreme', 'moderate', 'homogeneous']:
525	            sub = df_agg[(df_agg['k_subgroups'] == k) & (df_agg['regime'] == regime)]
526	            if sub.empty:
527	                continue
528	            print(f"    {regime}:")
529	            print(f"    {'n_exp':>6s}  {'oracle':>8s}  {'naive':>8s}  {'global':>8s}  "
530	                  f"{'mle':>8s}  {'hb':>8s}  {'HB vs MLE':>10s}")
531	            for ne in sorted(sub['n_expert'].unique()):
532	                vals = {}
533	                for m in ['oracle', 'naive', 'global_corrected', 'mle_laplace', 'hb_dirichlet']:
534	                    ms = sub[(sub['method'] == m) & (sub['n_expert'] == ne)]
535	                    if ms.empty:
536	                        vals[m] = np.nan
537	                    else:
538	                        vals[m] = np.sqrt((ms['rmse_z0'].values ** 2 +
539	                                           ms['rmse_z1'].values ** 2).mean())
540	                mle_v, hb_v = vals['mle_laplace'], vals['hb_dirichlet']
541	                pct = (mle_v - hb_v) / mle_v * 100 if mle_v > 1e-10 else 0
542	                tag = f"{pct:+.1f}%"
543	                print(f"    {int(ne):6d}  {vals['oracle']:8.4f}  {vals['naive']:8.4f}  "
544	                      f"{vals['global_corrected']:8.4f}  {mle_v:8.4f}  {hb_v:8.4f}  {tag:>10s}")
545	
546	
547	# ── Sweep ─────────────────────────────────────────────────────────────────────
548	
549	def run_sweep(regime_names, n_experts, k_list, n_mc,
550	              hb_method='eb', mcmc_diag_runs=5, verbose=True):
551	    all_rows, all_diag = [], []
552	    total = sum(1 for k in k_list for r in regime_names if r in REGIMES[k]) * len(n_experts) * n_mc
553	    count = 0
554	    t0 = time.time()
555	
556	    for k in k_list:
557	        for rn in regime_names:
558	            if rn not in REGIMES[k]:
559	                continue
560	            rp = REGIMES[k][rn]
561	            for ne in n_experts:
562	                for mc in range(n_mc):
563	                    use = hb_method
564	                    if hb_method == 'auto':
565	                        use = 'mcmc' if mc < mcmc_diag_runs else 'eb'
566	                    try:
567	                        rows, diag = run_one_mc(rn, rp, ne, k, seed=mc, hb_method=use)
568	                        all_rows.extend(rows)
569	                        all_diag.append(diag)
570	                    except Exception as e:
571	                        if verbose:
572	                            print(f"  WARN: k={k} {rn} ne={ne} mc={mc} failed: {e}")
573	                        all_diag.append({
574	                            'regime': rn, 'n_expert': ne, 'k_subgroups': k,
575	                            'mc_run': mc, 'hb_method': 'error',
576	                            'rhat_max': np.nan, 'ess_min': np.nan,
577	                            'divergent_count': -1, 'runtime_seconds': 0.0})
578	                    count += 1
579	                    if verbose and count % max(1, total // 20) == 0:
580	                        el = time.time() - t0
581	                        eta = el / count * (total - count)
582	                        print(f"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s | "
583	                              f"k={k} {rn} ne={ne} mc={mc}")
584	
585	    if verbose:
586	        print(f"  Sweep done: {time.time() - t0:.1f}s ({count} runs)")
587	    return pd.DataFrame(all_rows), pd.DataFrame(all_diag)
588	
589	
590	# ── Main ──────────────────────────────────────────────────────────────────────
591	
592	if __name__ == '__main__':
593	    parser = argparse.ArgumentParser()
594	    parser.add_argument('--n-mc', type=int, default=100)
595	    parser.add_argument('--dry-run', action='store_true')
596	    parser.add_argument('--hb-method', choices=['auto', 'mcmc', 'gibbs', 'eb'], default='auto')
597	    parser.add_argument('--mcmc-diag-runs', type=int, default=5)
598	    args = parser.parse_args()
599	
600	    n_mc = 5 if args.dry_run else args.n_mc
601	    regime_names = ['moderate'] if args.dry_run else ['extreme', 'moderate', 'homogeneous']
602	    n_experts = [100] if args.dry_run else DEFAULT_N_EXPERTS
603	    k_list = [2] if args.dry_run else DEFAULT_K_LIST
604	
605	    print(f"exp-001 HB Synthetic Validation | PyMC={HAS_PYMC}")
606	    print(f"N={N} n_mc={n_mc} hb={args.hb_method}")
607	    print(f"Regimes={regime_names} n_experts={n_experts} K={k_list}\n")
608	
609	    # Timing test
610	    effective_method = args.hb_method
611	    d = generate_data(REGIMES[2]['moderate'], 100, 2, seed=9999)
612	    em = d['expert_mask']
613	    tc = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], ['A', 'B'])
614	
615	    if args.hb_method == 'auto':
616	        print("Timing Gibbs sampler...")
617	        t0 = time.time()
618	        _, dg = estimate_cm_hb_gibbs(tc, ['A', 'B'], seed=9999)
619	        gt = time.time() - t0
620	        print(f"  Gibbs: {gt:.2f}s | rhat={dg['rhat_max']:.3f} "
621	              f"ess={dg['ess_min']:.0f}")
622	        if gt < 5:
623	            effective_method = 'gibbs'
624	            print(f"  Fast enough → using Gibbs for all runs")
625	        else:
626	            effective_method = 'eb'
627	            print(f"  Slow → using EB")
628	    elif args.hb_method == 'mcmc' and HAS_PYMC:
629	        print("Timing PyMC MCMC...")
630	        t0 = time.time()
631	        try:
632	            _, dg = estimate_cm_hb_mcmc(tc, ['A', 'B'], seed=9999)
633	            mt = time.time() - t0
634	            print(f"  MCMC: {mt:.1f}s | rhat={dg['rhat_max']:.3f} "
635	                  f"ess={dg['ess_min']:.0f} div={dg['divergent_count']}")
636	        except Exception as e:
637	            print(f"  MCMC failed: {e} → falling back to Gibbs")
638	            effective_method = 'gibbs'
639	
640	    print(f"\nEffective method: {effective_method}\n")
641	
642	    df_raw, df_diag = run_sweep(
643	        regime_names, n_experts, k_list, n_mc,
644	        hb_method=effective_method, mcmc_diag_runs=args.mcmc_diag_runs)
645	
646	    df_agg = aggregate_results(df_raw)
647	
648	    os.makedirs('results', exist_ok=True)
649	    agg_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method',
650	                'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1',
651	                'bias_z0_se', 'rmse_z0_se', 'bias_z1_se', 'rmse_z1_se']
652	    df_agg[agg_cols].to_csv('results/exp001_hb_results.csv', index=False)
653	
654	    diag_cols = ['regime', 'n_expert', 'k_subgroups', 'mc_run',
655	                 'rhat_max', 'ess_min', 'divergent_count', 'runtime_seconds']
656	    save_cols = [c for c in diag_cols if c in df_diag.columns]
657	    if 'hb_method' in df_diag.columns:
658	        save_cols.insert(4, 'hb_method')
659	    df_diag[save_cols].to_csv('results/exp001_hb_diagnostics.csv', index=False)
660	
661	    print_summary(df_agg, df_diag)
662	
663	    print(f"\nSaved: results/exp001_hb_results.csv ({len(df_agg)} rows)")
664	    print(f"Saved: results/exp001_hb_diagnostics.csv ({len(df_diag)} rows)")
665	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "3b76e18c-f6f1-412c-89cb-a7cffc3dc989",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nexp001_hb_synthetic.py - Hierarchical Bayesian EC-HTE Synthetic Validation (exp-001)\n\nCompares confusion matrix estimators for CATE correction under heterogeneous\nmisclassification across subgroups:\n  Oracle, Naive, Global-corrected, MLE (Laplace), HB Dirichlet (partial pooling)\n\nInput: Synthetic DGP parameters (regimes, expert budgets, subgroup counts)\nOutput: results/exp001_hb_results.csv, results/exp001_hb_diagnostics.csv\n\"\"\"\n\nimport argparse\nimport os\nimport sys\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\nfrom scipy.optimize import minimize_scalar\n\nwarnings.filterwarnings('ignore')\n\ntry:\n    import pymc as pm\n    import pytensor.tensor as pt\n    import arviz as az\n    HAS_PYMC = True\nexcept ImportError:\n    HAS_PYMC = False\n\nN = 5000\nSUBGROUP_LABELS = {2: ['A', 'B'], 4: ['A', 'B', 'C', 'D']}\n\nREGIMES = {\n    2: {\n        'extreme':     {'misclass': [0.25, 0.05], 'tau_z1': 0.5, 'tau_z0': 0.1},\n        'moderate':    {'misclass': [0.15, 0.10], 'tau_z1': 0.3, 'tau_z0': 0.15},\n        'homogeneous': {'misclass': [0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},\n    },\n    4: {\n        'extreme':     {'misclass': [0.30, 0.20, 0.10, 0.03], 'tau_z1': 0.5, 'tau_z0': 0.1},\n        'moderate':    {'misclass': [0.20, 0.15, 0.10, 0.05], 'tau_z1': 0.3, 'tau_z0': 0.15},\n        'homogeneous': {'misclass': [0.12, 0.12, 0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},\n    },\n}\n\nDEFAULT_N_EXPERTS = [50, 100, 250, 500, 1000, 2000]\nDEFAULT_K_LIST = [2, 4]\n\n\n# ── DGP ───────────────────────────────────────────────────────────────────────\n\ndef generate_data(regime_params, n_expert, k, seed):\n    rng = np.random.RandomState(seed)\n    labels = SUBGROUP_LABELS[k]\n    T = rng.binomial(1, 0.5, N)\n    Z = rng.binomial(1, 0.5, N)\n    S = rng.choice(labels, N, p=[1.0 / k] * k)\n    X = rng.randn(N, 5)\n    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])\n    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)\n    mc_rates = np.zeros(N)\n    for i, s in enumerate(labels):\n        mc_rates[S == s] = regime_params['misclass'][i]\n    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)\n    idx = rng.choice(N, min(n_expert, N), replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[idx] = True\n    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, X=X, Y=Y, tau=tau, expert_mask=expert_mask)\n\n\n# ── Helpers ───────────────────────────────────────────────────────────────────\n\ndef diff_in_means(Y, T, mask):\n    t1, t0 = mask & (T == 1), mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    \"\"\"Confusion matrix counts per subgroup: (k, 2, 2) = [subgroup, true_z, z_hat].\"\"\"\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef build_mixing_matrix(C):\n    \"\"\"C[z, z_hat] → M[z_hat, z] via Bayes rule (assuming P(Z=0)=P(Z=1)=0.5).\"\"\"\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        cs = C[0, zh] + C[1, zh]\n        if cs > 0:\n            M[zh, 0] = C[0, zh] / cs\n            M[zh, 1] = C[1, zh] / cs\n        else:\n            M[zh, :] = 0.5\n    return M\n\n\ndef invert_mixing(M, tau_obs, se_obs):\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\ndef safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):\n    \"\"\"Invert mixing matrix with condition number guard.\n\n    When cond(M_s) > threshold, matrix inversion is numerically unstable.\n    Falls back to naive (no correction) to avoid catastrophic amplification.\n    \"\"\"\n    cond = np.linalg.cond(M_s)\n    if cond > cond_threshold:\n        return tau_obs.copy()\n    return np.linalg.solve(M_s, tau_obs)\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    \"\"\"Like invert_mixing but with condition number guard.\"\"\"\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# ── Confusion Matrix Estimators ───────────────────────────────────────────────\n\ndef estimate_cm_mle(counts, labels):\n    \"\"\"Per-subgroup MLE with Laplace smoothing (add-1).\"\"\"\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            n = counts[i, z, :].sum()\n            for zh in [0, 1]:\n                C_s[z, zh] = (counts[i, z, zh] + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    \"\"\"Negative log marginal likelihood for Dirichlet-Multinomial.\"\"\"\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_eb(counts, labels):\n    \"\"\"Empirical Bayes HB: optimize shared Dirichlet concentration, posterior mean.\"\"\"\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = 2.0\n            continue\n        res = minimize_scalar(\n            lambda a: _dirmult_neg_ll(a, cl), bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n = counts[i, z, :].sum()\n            d = n + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    diag = {'rhat_max': np.nan, 'ess_min': np.nan, 'divergent_count': 0,\n            'runtime_seconds': 0.0, 'hb_method': 'eb',\n            'alpha_0_z0': alpha_opt[0], 'alpha_0_z1': alpha_opt[1]}\n    return C, diag\n\n\ndef _split_rhat(chains):\n    \"\"\"Split R-hat for a scalar parameter. chains: (n_chains, n_draws).\"\"\"\n    parts = []\n    for c in range(chains.shape[0]):\n        half = chains.shape[1] // 2\n        parts.append(chains[c, :half])\n        parts.append(chains[c, half:2 * half])\n    parts = np.array(parts)\n    m = parts.shape[0]\n    n = parts.shape[1]\n    chain_means = parts.mean(axis=1)\n    W = np.mean(np.var(parts, axis=1, ddof=1))\n    B = n * np.var(chain_means, ddof=1)\n    if W < 1e-20:\n        return 1.0\n    var_hat = (1 - 1.0 / n) * W + B / n\n    return float(np.sqrt(var_hat / W))\n\n\ndef _bulk_ess(chains):\n    \"\"\"Approximate bulk ESS via initial positive sequence. chains: (n_chains, n_draws).\"\"\"\n    x = chains.ravel()\n    n = len(x)\n    mu = x.mean()\n    xc = x - mu\n    max_lag = min(n // 2, 300)\n    c0 = np.dot(xc, xc)\n    if c0 < 1e-20:\n        return float(n)\n    tau = 1.0\n    for lag in range(1, max_lag - 1, 2):\n        r1 = np.dot(xc[:n - lag], xc[lag:]) / c0\n        r2 = np.dot(xc[:n - lag - 1], xc[lag + 1:]) / c0 if lag + 1 < n else 0\n        pair = r1 + r2\n        if pair < 0:\n            break\n        tau += 2 * pair\n    return float(n / tau)\n\n\ndef _fast_diagnostics(alpha_arr, theta_arr, labels):\n    \"\"\"Compute R-hat and ESS over all parameters without arviz.\"\"\"\n    rhats, esss = [], []\n    for d in range(alpha_arr.shape[2]):\n        rhats.append(_split_rhat(alpha_arr[:, :, d]))\n        esss.append(_bulk_ess(alpha_arr[:, :, d]))\n    k = len(labels)\n    for i in range(k):\n        for z in [0, 1]:\n            for zh in range(theta_arr.shape[4]):\n                ch = theta_arr[:, :, i, z, zh]\n                rhats.append(_split_rhat(ch))\n                esss.append(_bulk_ess(ch))\n    return max(rhats), min(esss)\n\n\ndef _log_target_alpha(alpha, theta_z):\n    \"\"\"Log posterior for alpha_0[z] in log-alpha space (includes Jacobian).\"\"\"\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = 2.0 * np.log(alpha) - alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=2000, n_warmup=1000, n_chains=2):\n    \"\"\"Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).\"\"\"\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_alpha, all_theta = [], []\n    t0 = time.time()\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        alpha_samples = np.zeros((n_iter, 2))\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :]) -\n                         _log_target_alpha(alpha[z], theta[:, z, :]))\n                accepted = np.log(rng.rand()) < log_r\n                if accepted:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(accepted)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                idx = it - n_warmup\n                alpha_samples[idx] = alpha.copy()\n                theta_samples[idx] = theta.copy()\n\n        all_alpha.append(alpha_samples)\n        all_theta.append(theta_samples)\n\n    runtime = time.time() - t0\n    alpha_arr = np.stack(all_alpha)\n    theta_arr = np.stack(all_theta)\n\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n\n    rhat_max, ess_min = _fast_diagnostics(alpha_arr, theta_arr, labels)\n\n    diag = {'rhat_max': rhat_max, 'ess_min': ess_min, 'divergent_count': 0,\n            'runtime_seconds': runtime, 'hb_method': 'gibbs'}\n    return C, diag\n\n\ndef estimate_cm_hb_mcmc(counts, labels, seed=42, draws=1000, tune=500, chains=2):\n    \"\"\"Full Bayesian HB with PyMC MCMC.\"\"\"\n    k = len(labels)\n    n_per_sz = counts.sum(axis=2)\n\n    with pm.Model():\n        alpha_0 = pm.Gamma('alpha_0', alpha=2, beta=1, shape=2)\n        for z in [0, 1]:\n            for i, s in enumerate(labels):\n                nsz = int(n_per_sz[i, z])\n                if nsz == 0:\n                    continue\n                a = pt.stack([alpha_0[z] / 2, alpha_0[z] / 2])\n                theta = pm.Dirichlet(f'theta_{s}_z{z}', a=a)\n                pm.Multinomial(f'obs_{s}_z{z}', n=nsz, p=theta,\n                               observed=counts[i, z, :].astype('int32'))\n        t0 = time.time()\n        trace = pm.sample(draws=draws, tune=tune, chains=chains,\n                          random_seed=seed, progressbar=False)\n        runtime = time.time() - t0\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            vn = f'theta_{s}_z{z}'\n            if vn in trace.posterior:\n                C_s[z, :] = trace.posterior[vn].values.mean(axis=(0, 1))\n            else:\n                C_s[z, :] = 0.5\n        C[s] = C_s\n\n    all_vars = list(trace.posterior.data_vars)\n    try:\n        summ = az.summary(trace, var_names=all_vars)\n        rhat_max = float(summ['r_hat'].max())\n        ess_min = float(summ['ess_bulk'].min())\n    except Exception:\n        rhat_max = ess_min = np.nan\n    try:\n        divergent = int(trace.sample_stats['diverging'].values.sum())\n    except Exception:\n        divergent = -1\n\n    diag = {'rhat_max': rhat_max, 'ess_min': ess_min,\n            'divergent_count': divergent, 'runtime_seconds': runtime,\n            'hb_method': 'mcmc'}\n    return C, diag\n\n\n# ── Single MC Run ─────────────────────────────────────────────────────────────\n\ndef run_one_mc(regime_name, regime_params, n_expert, k, seed, hb_method='eb'):\n    data = generate_data(regime_params, n_expert, k, seed)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    em = data['expert_mask']\n    labels = SUBGROUP_LABELS[k]\n    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']\n\n    counts = get_counts(Z[em], Z_hat[em], S[em], labels)\n\n    C_mle = estimate_cm_mle(counts, labels)\n\n    if hb_method == 'gibbs':\n        C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed)\n    elif hb_method == 'mcmc' and HAS_PYMC:\n        try:\n            C_hb, hb_diag = estimate_cm_hb_mcmc(counts, labels, seed=seed)\n        except Exception:\n            C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)\n            hb_diag['hb_method'] = 'eb_fallback'\n    else:\n        C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)\n\n    # Global CM (pool all expert labels, Laplace)\n    cg = counts.sum(axis=0)\n    C_gl = np.zeros((2, 2))\n    for z in [0, 1]:\n        n = cg[z, :].sum()\n        for zh in [0, 1]:\n            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5\n\n    M_gl = build_mixing_matrix(C_gl)\n    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}\n    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}\n\n    base = {'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k, 'mc_run': seed}\n    rows = []\n\n    for s in labels:\n        sm = S == s\n        th0_or, se0_or = diff_in_means(Y, T, sm & (Z == 0))\n        th1_or, se1_or = diff_in_means(Y, T, sm & (Z == 1))\n        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))\n        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))\n\n        tau_obs = np.array([th0_n, th1_n])\n        se_obs = np.array([se0_n, se1_n])\n        if np.any(np.isnan(tau_obs)):\n            continue\n\n        tgc, sgc = invert_mixing(M_gl, tau_obs, se_obs)\n        tml, sml = invert_mixing(M_mle[s], tau_obs, se_obs)\n        thb, shb = invert_mixing(M_hb[s], tau_obs, se_obs)\n\n        def mr(method, th0, th1, se0, se1):\n            return {**base, 'subgroup': s, 'method': method,\n                    'tau_hat_z0': th0, 'tau_hat_z1': th1,\n                    'se_z0': se0, 'se_z1': se1,\n                    'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}\n\n        rows.append(mr('oracle', th0_or, th1_or, se0_or, se1_or))\n        rows.append(mr('naive', th0_n, th1_n, se0_n, se1_n))\n        rows.append(mr('global_corrected', tgc[0], tgc[1], sgc[0], sgc[1]))\n        rows.append(mr('mle_laplace', tml[0], tml[1], sml[0], sml[1]))\n        rows.append(mr('hb_dirichlet', thb[0], thb[1], shb[0], shb[1]))\n\n    return rows, {**base, **hb_diag}\n\n\n# ── Aggregation ───────────────────────────────────────────────────────────────\n\ndef aggregate_results(df):\n    rows = []\n    grp_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method']\n    for keys, grp in df.groupby(grp_cols):\n        regime, n_expert, k, subgroup, method = keys\n        row = {'regime': regime, 'n_expert': int(n_expert), 'k_subgroups': int(k),\n               'subgroup': subgroup, 'method': method}\n        n_mc = len(grp)\n        for z in ['z0', 'z1']:\n            err = grp[f'tau_hat_{z}'].values - grp[f'tau_true_{z}'].values\n            bias = err.mean()\n            mse = (err ** 2).mean()\n            rmse = np.sqrt(mse)\n            ci_lo = grp[f'tau_hat_{z}'].values - 1.96 * grp[f'se_{z}'].values\n            ci_hi = grp[f'tau_hat_{z}'].values + 1.96 * grp[f'se_{z}'].values\n            cov = ((ci_lo <= grp[f'tau_true_{z}'].values) &\n                   (grp[f'tau_true_{z}'].values <= ci_hi)).mean()\n            row[f'bias_{z}'] = bias\n            row[f'rmse_{z}'] = rmse\n            row[f'coverage_{z}'] = cov\n            row[f'bias_{z}_se'] = err.std() / np.sqrt(n_mc)\n            mse_se = (err ** 2).std() / np.sqrt(n_mc)\n            row[f'rmse_{z}_se'] = mse_se / (2 * rmse) if rmse > 1e-10 else np.nan\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# ── Output ────────────────────────────────────────────────────────────────────\n\ndef print_summary(df_agg, df_diag):\n    pd.set_option('display.float_format', '{:.4f}'.format)\n\n    # MCMC / Gibbs diagnostics\n    if 'hb_method' in df_diag.columns:\n        for method_label in ['gibbs', 'mcmc']:\n            mrows = df_diag[df_diag['hb_method'] == method_label]\n            if mrows.empty:\n                continue\n            print(f\"\\n── {method_label.upper()} Diagnostics ──────────────────────────────\")\n            print(f\"  Runs:           {len(mrows)}\")\n            rh = mrows['rhat_max'].dropna()\n            es = mrows['ess_min'].dropna()\n            if not rh.empty:\n                print(f\"  R-hat max:      {rh.max():.4f} (target < 1.01)\")\n            if not es.empty:\n                print(f\"  ESS min:        {es.min():.0f} (target > 200)\")\n            print(f\"  Divergent total:{int(mrows['divergent_count'].sum())}\")\n            print(f\"  Runtime median: {mrows['runtime_seconds'].median():.2f}s\")\n\n    # Per-config HB vs MLE comparison\n    print(\"\\n── HB vs MLE RMSE Comparison (subgroup-level, averaged) ──\")\n    for k in sorted(df_agg['k_subgroups'].unique()):\n        print(f\"\\n  K = {int(k)} subgroups\")\n        for regime in ['extreme', 'moderate', 'homogeneous']:\n            sub = df_agg[(df_agg['k_subgroups'] == k) & (df_agg['regime'] == regime)]\n            if sub.empty:\n                continue\n            print(f\"    {regime}:\")\n            print(f\"    {'n_exp':>6s}  {'oracle':>8s}  {'naive':>8s}  {'global':>8s}  \"\n                  f\"{'mle':>8s}  {'hb':>8s}  {'HB vs MLE':>10s}\")\n            for ne in sorted(sub['n_expert'].unique()):\n                vals = {}\n                for m in ['oracle', 'naive', 'global_corrected', 'mle_laplace', 'hb_dirichlet']:\n                    ms = sub[(sub['method'] == m) & (sub['n_expert'] == ne)]\n                    if ms.empty:\n                        vals[m] = np.nan\n                    else:\n                        vals[m] = np.sqrt((ms['rmse_z0'].values ** 2 +\n                                           ms['rmse_z1'].values ** 2).mean())\n                mle_v, hb_v = vals['mle_laplace'], vals['hb_dirichlet']\n                pct = (mle_v - hb_v) / mle_v * 100 if mle_v > 1e-10 else 0\n                tag = f\"{pct:+.1f}%\"\n                print(f\"    {int(ne):6d}  {vals['oracle']:8.4f}  {vals['naive']:8.4f}  \"\n                      f\"{vals['global_corrected']:8.4f}  {mle_v:8.4f}  {hb_v:8.4f}  {tag:>10s}\")\n\n\n# ── Sweep ─────────────────────────────────────────────────────────────────────\n\ndef run_sweep(regime_names, n_experts, k_list, n_mc,\n              hb_method='eb', mcmc_diag_runs=5, verbose=True):\n    all_rows, all_diag = [], []\n    total = sum(1 for k in k_list for r in regime_names if r in REGIMES[k]) * len(n_experts) * n_mc\n    count = 0\n    t0 = time.time()\n\n    for k in k_list:\n        for rn in regime_names:\n            if rn not in REGIMES[k]:\n                continue\n            rp = REGIMES[k][rn]\n            for ne in n_experts:\n                for mc in range(n_mc):\n                    use = hb_method\n                    if hb_method == 'auto':\n                        use = 'mcmc' if mc < mcmc_diag_runs else 'eb'\n                    try:\n                        rows, diag = run_one_mc(rn, rp, ne, k, seed=mc, hb_method=use)\n                        all_rows.extend(rows)\n                        all_diag.append(diag)\n                    except Exception as e:\n                        if verbose:\n                            print(f\"  WARN: k={k} {rn} ne={ne} mc={mc} failed: {e}\")\n                        all_diag.append({\n                            'regime': rn, 'n_expert': ne, 'k_subgroups': k,\n                            'mc_run': mc, 'hb_method': 'error',\n                            'rhat_max': np.nan, 'ess_min': np.nan,\n                            'divergent_count': -1, 'runtime_seconds': 0.0})\n                    count += 1\n                    if verbose and count % max(1, total // 20) == 0:\n                        el = time.time() - t0\n                        eta = el / count * (total - count)\n                        print(f\"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s | \"\n                              f\"k={k} {rn} ne={ne} mc={mc}\")\n\n    if verbose:\n        print(f\"  Sweep done: {time.time() - t0:.1f}s ({count} runs)\")\n    return pd.DataFrame(all_rows), pd.DataFrame(all_diag)\n\n\n# ── Main ──────────────────────────────────────────────────────────────────────\n\nif __name__ == '__main__':\n    parser = argparse.ArgumentParser()\n    parser.add_argument('--n-mc', type=int, default=100)\n    parser.add_argument('--dry-run', action='store_true')\n    parser.add_argument('--hb-method', choices=['auto', 'mcmc', 'gibbs', 'eb'], default='auto')\n    parser.add_argument('--mcmc-diag-runs', type=int, default=5)\n    args = parser.parse_args()\n\n    n_mc = 5 if args.dry_run else args.n_mc\n    regime_names = ['moderate'] if args.dry_run else ['extreme', 'moderate', 'homogeneous']\n    n_experts = [100] if args.dry_run else DEFAULT_N_EXPERTS\n    k_list = [2] if args.dry_run else DEFAULT_K_LIST\n\n    print(f\"exp-001 HB Synthetic Validation | PyMC={HAS_PYMC}\")\n    print(f\"N={N} n_mc={n_mc} hb={args.hb_method}\")\n    print(f\"Regimes={regime_names} n_experts={n_experts} K={k_list}\\n\")\n\n    # Timing test\n    effective_method = args.hb_method\n    d = generate_data(REGIMES[2]['moderate'], 100, 2, seed=9999)\n    em = d['expert_mask']\n    tc = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], ['A', 'B'])\n\n    if args.hb_method == 'auto':\n        print(\"Timing Gibbs sampler...\")\n        t0 = time.time()\n        _, dg = estimate_cm_hb_gibbs(tc, ['A', 'B'], seed=9999)\n        gt = time.time() - t0\n        print(f\"  Gibbs: {gt:.2f}s | rhat={dg['rhat_max']:.3f} \"\n              f\"ess={dg['ess_min']:.0f}\")\n        if gt < 5:\n            effective_method = 'gibbs'\n            print(f\"  Fast enough → using Gibbs for all runs\")\n        else:\n            effective_method = 'eb'\n            print(f\"  Slow → using EB\")\n    elif args.hb_method == 'mcmc' and HAS_PYMC:\n        print(\"Timing PyMC MCMC...\")\n        t0 = time.time()\n        try:\n            _, dg = estimate_cm_hb_mcmc(tc, ['A', 'B'], seed=9999)\n            mt = time.time() - t0\n            print(f\"  MCMC: {mt:.1f}s | rhat={dg['rhat_max']:.3f} \"\n                  f\"ess={dg['ess_min']:.0f} div={dg['divergent_count']}\")\n        except Exception as e:\n            print(f\"  MCMC failed: {e} → falling back to Gibbs\")\n            effective_method = 'gibbs'\n\n    print(f\"\\nEffective method: {effective_method}\\n\")\n\n    df_raw, df_diag = run_sweep(\n        regime_names, n_experts, k_list, n_mc,\n        hb_method=effective_method, mcmc_diag_runs=args.mcmc_diag_runs)\n\n    df_agg = aggregate_results(df_raw)\n\n    os.makedirs('results', exist_ok=True)\n    agg_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method',\n                'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1',\n                'bias_z0_se', 'rmse_z0_se', 'bias_z1_se', 'rmse_z1_se']\n    df_agg[agg_cols].to_csv('results/exp001_hb_results.csv', index=False)\n\n    diag_cols = ['regime', 'n_expert', 'k_subgroups', 'mc_run',\n                 'rhat_max', 'ess_min', 'divergent_count', 'runtime_seconds']\n    save_cols = [c for c in diag_cols if c in df_diag.columns]\n    if 'hb_method' in df_diag.columns:\n        save_cols.insert(4, 'hb_method')\n    df_diag[save_cols].to_csv('results/exp001_hb_diagnostics.csv', index=False)\n\n    print_summary(df_agg, df_diag)\n\n    print(f\"\\nSaved: results/exp001_hb_results.csv ({len(df_agg)} rows)\")\n    print(f\"Saved: results/exp001_hb_diagnostics.csv ({len(df_diag)} rows)\")\n",
      "numLines": 665,
      "startLine": 1,
      "totalLines": 665
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
Let me understand the hyperprior structure:

1. In `estimate_cm_hb_gibbs` (line 276), the Gibbs sampler uses:
   - `_log_target_alpha` (line 264) which computes the log posterior for `alpha_0[z]`
   - The prior on `alpha_0` is: `lp = 2.0 * np.log(alpha) - alpha` (line 271)
   - This is `log(alpha^2 * exp(-alpha))` which means `p(alpha) ∝ alpha^2 * exp(-alpha)`
   - This corresponds to a Gamma(3, 1) distribution with shape=3 and rate=1

2. In `estimate_cm_hb_mcmc` (line 349), PyMC uses:
   - `alpha_0 = pm.Gamma('alpha_0', alpha=2, beta=1, shape=2)` (line 355)
   - This is Gamma(alpha=2, beta=1) → shape=2, rate=1

There's a mismatch here: the Gibbs sampler is using Gamma(3, 1) but the PyMC version is using Gamma(2, 1), so I need to figure out where this discrepancy comes from.

Looking at the log-probability in `_log_target_alpha`, the expression `alpha^2 * exp(-alpha)` matches the Gamma(3, 1) kernel, but the PyMC prior is specified differently. For the sensitivity analysis, I'll stick with the Gibbs sampler version since that's what's actually being used in practice.

Now I'm considering how to scale the hyperprior for sensitivity testing—I could scale both shape and rate parameters together to preserve the mean while changing variance, or scale them independently to explore different prior configurations. I see the issue now—the task description and the hint are contradictory. According to the hint, scaling both parameters by s gives Gamma(a*s, b*s), which keeps the mean constant but reduces variance as s increases. That would make s=2.0 tighter and s=0.5 wider, the opposite of what the task states. Let me reconsider whether they might mean scaling just one parameter instead. means increasing both a₀ and b₀ proportionally to tighten the prior, but the task description seems to suggest scale=0.5 should produce a tighter distribution. Let me reconsider whether "scale" should adjust the variance directly rather than the parameters—if I scale the variance by a factor while keeping the mean constant, I can reparameterize using Gamma(a/s, b/s) to achieve this effect.

With this approach, scale=0.5 gives half the variance (tighter), and scale=2.0 doubles it (wider), which aligns with the intended semantics. So I'd adjust the original Gamma(3, 1) parameters by dividing both by the scale factor, and then update the log probability calculation accordingly. sense! Let me implement this.

I need to modify the log target function and the Gibbs sampler to accept hyperprior parameters, then write a script to test sensitivity across different scaling factors. For the log target function, I'll replace the hardcoded coefficients with parameterized versions that use the hyperprior shape and rate parameters. The Gibbs sampler will accept these hyperprior parameters and pass them through to the log target function. I need to pass the hyperprior parameters through the entire chain and then write a sensitivity analysis script that tests different hyperprior values.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "e6c51ffd-9794-4872-afab-26e09f3c658c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSmbWLdu7tUCMUrYL1JLjj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11493,
      "cache_read_input_tokens": 19211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11493
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

Now I understand the code. The hyperprior is in `_log_target_alpha` (line 270-271):

```python
lp = 2.0 * np.log(alpha) - alpha  # ∝ Gamma(shape=3, rate=1)
```

This is Gamma(a₀=3, b₀=1) on `alpha_0[z]`. I need to:
1. Make the hyperprior parameters configurable in the Gibbs sampler
2. Write the sensitivity script

Scaling approach: to keep the mean fixed (a₀/b₀=3) while varying informativeness, I'll use Gamma(a₀/scale, b₀/scale). scale=0.5 → tighter (var halved), scale=2.0 → wider (var doubled).

Let me modify the Gibbs sampler first, then write the sensitivity script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "dd7262c3-537d-4e93-b0fa-a8e48f12217c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSmbWLdu7tUCMUrYL1JLjj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11493,
      "cache_read_input_tokens": 19211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11493
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

<details open><summary>🔧 Tool call — Edit · `toolu_01XmRHa2svWjLMbdfrZK9DNh`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
  "old_string": "def _log_target_alpha(alpha, theta_z):\n    \"\"\"Log posterior for alpha_0[z] in log-alpha space (includes Jacobian).\"\"\"\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = 2.0 * np.log(alpha) - alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp",
  "new_string": "def _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    \"\"\"Log posterior for alpha_0[z] in log-alpha space (includes Jacobian).\"\"\"\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "12256562-c0fd-44b6-b0ba-03fc7cf8158a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSmbWLdu7tUCMUrYL1JLjj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11493,
      "cache_read_input_tokens": 19211,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11493
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

_source line 10 · 2026-05-20T22:08:02.328Z_

<details><summary>↩ Tool result · `toolu_01XmRHa2svWjLMbdfrZK9DNh`</summary>

```text
The file /home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "a159b0c1-2786-45bf-be08-6457cd340147",
  "tool_use_result": {
    "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
    "oldString": "def _log_target_alpha(alpha, theta_z):\n    \"\"\"Log posterior for alpha_0[z] in log-alpha space (includes Jacobian).\"\"\"\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = 2.0 * np.log(alpha) - alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp",
    "newString": "def _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    \"\"\"Log posterior for alpha_0[z] in log-alpha space (includes Jacobian).\"\"\"\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nexp001_hb_synthetic.py - Hierarchical Bayesian EC-HTE Synthetic Validation (exp-001)\n\nCompares confusion matrix estimators for CATE correction under heterogeneous\nmisclassification across subgroups:\n  Oracle, Naive, Global-corrected, MLE (Laplace), HB Dirichlet (partial pooling)\n\nInput: Synthetic DGP parameters (regimes, expert budgets, subgroup counts)\nOutput: results/exp001_hb_results.csv, results/exp001_hb_diagnostics.csv\n\"\"\"\n\nimport argparse\nimport os\nimport sys\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\nfrom scipy.optimize import minimize_scalar\n\nwarnings.filterwarnings('ignore')\n\ntry:\n    import pymc as pm\n    import pytensor.tensor as pt\n    import arviz as az\n    HAS_PYMC = True\nexcept ImportError:\n    HAS_PYMC = False\n\nN = 5000\nSUBGROUP_LABELS = {2: ['A', 'B'], 4: ['A', 'B', 'C', 'D']}\n\nREGIMES = {\n    2: {\n        'extreme':     {'misclass': [0.25, 0.05], 'tau_z1': 0.5, 'tau_z0': 0.1},\n        'moderate':    {'misclass': [0.15, 0.10], 'tau_z1': 0.3, 'tau_z0': 0.15},\n        'homogeneous': {'misclass': [0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},\n    },\n    4: {\n        'extreme':     {'misclass': [0.30, 0.20, 0.10, 0.03], 'tau_z1': 0.5, 'tau_z0': 0.1},\n        'moderate':    {'misclass': [0.20, 0.15, 0.10, 0.05], 'tau_z1': 0.3, 'tau_z0': 0.15},\n        'homogeneous': {'misclass': [0.12, 0.12, 0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},\n    },\n}\n\nDEFAULT_N_EXPERTS = [50, 100, 250, 500, 1000, 2000]\nDEFAULT_K_LIST = [2, 4]\n\n\n# ── DGP ───────────────────────────────────────────────────────────────────────\n\ndef generate_data(regime_params, n_expert, k, seed):\n    rng = np.random.RandomState(seed)\n    labels = SUBGROUP_LABELS[k]\n    T = rng.binomial(1, 0.5, N)\n    Z = rng.binomial(1, 0.5, N)\n    S = rng.choice(labels, N, p=[1.0 / k] * k)\n    X = rng.randn(N, 5)\n    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])\n    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)\n    mc_rates = np.zeros(N)\n    for i, s in enumerate(labels):\n        mc_rates[S == s] = regime_params['misclass'][i]\n    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)\n    idx = rng.choice(N, min(n_expert, N), replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[idx] = True\n    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, X=X, Y=Y, tau=tau, expert_mask=expert_mask)\n\n\n# ── Helpers ───────────────────────────────────────────────────────────────────\n\ndef diff_in_means(Y, T, mask):\n    t1, t0 = mask & (T == 1), mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    \"\"\"Confusion matrix counts per subgroup: (k, 2, 2) = [subgroup, true_z, z_hat].\"\"\"\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef build_mixing_matrix(C):\n    \"\"\"C[z, z_hat] → M[z_hat, z] via Bayes rule (assuming P(Z=0)=P(Z=1)=0.5).\"\"\"\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        cs = C[0, zh] + C[1, zh]\n        if cs > 0:\n            M[zh, 0] = C[0, zh] / cs\n            M[zh, 1] = C[1, zh] / cs\n        else:\n            M[zh, :] = 0.5\n    return M\n\n\ndef invert_mixing(M, tau_obs, se_obs):\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\ndef safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):\n    \"\"\"Invert mixing matrix with condition number guard.\n\n    When cond(M_s) > threshold, matrix inversion is numerically unstable.\n    Falls back to naive (no correction) to avoid catastrophic amplification.\n    \"\"\"\n    cond = np.linalg.cond(M_s)\n    if cond > cond_threshold:\n        return tau_obs.copy()\n    return np.linalg.solve(M_s, tau_obs)\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    \"\"\"Like invert_mixing but with condition number guard.\"\"\"\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# ── Confusion Matrix Estimators ───────────────────────────────────────────────\n\ndef estimate_cm_mle(counts, labels):\n    \"\"\"Per-subgroup MLE with Laplace smoothing (add-1).\"\"\"\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            n = counts[i, z, :].sum()\n            for zh in [0, 1]:\n                C_s[z, zh] = (counts[i, z, zh] + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    \"\"\"Negative log marginal likelihood for Dirichlet-Multinomial.\"\"\"\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_eb(counts, labels):\n    \"\"\"Empirical Bayes HB: optimize shared Dirichlet concentration, posterior mean.\"\"\"\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = 2.0\n            continue\n        res = minimize_scalar(\n            lambda a: _dirmult_neg_ll(a, cl), bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n = counts[i, z, :].sum()\n            d = n + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    diag = {'rhat_max': np.nan, 'ess_min': np.nan, 'divergent_count': 0,\n            'runtime_seconds': 0.0, 'hb_method': 'eb',\n            'alpha_0_z0': alpha_opt[0], 'alpha_0_z1': alpha_opt[1]}\n    return C, diag\n\n\ndef _split_rhat(chains):\n    \"\"\"Split R-hat for a scalar parameter. chains: (n_chains, n_draws).\"\"\"\n    parts = []\n    for c in range(chains.shape[0]):\n        half = chains.shape[1] // 2\n        parts.append(chains[c, :half])\n        parts.append(chains[c, half:2 * half])\n    parts = np.array(parts)\n    m = parts.shape[0]\n    n = parts.shape[1]\n    chain_means = parts.mean(axis=1)\n    W = np.mean(np.var(parts, axis=1, ddof=1))\n    B = n * np.var(chain_means, ddof=1)\n    if W < 1e-20:\n        return 1.0\n    var_hat = (1 - 1.0 / n) * W + B / n\n    return float(np.sqrt(var_hat / W))\n\n\ndef _bulk_ess(chains):\n    \"\"\"Approximate bulk ESS via initial positive sequence. chains: (n_chains, n_draws).\"\"\"\n    x = chains.ravel()\n    n = len(x)\n    mu = x.mean()\n    xc = x - mu\n    max_lag = min(n // 2, 300)\n    c0 = np.dot(xc, xc)\n    if c0 < 1e-20:\n        return float(n)\n    tau = 1.0\n    for lag in range(1, max_lag - 1, 2):\n        r1 = np.dot(xc[:n - lag], xc[lag:]) / c0\n        r2 = np.dot(xc[:n - lag - 1], xc[lag + 1:]) / c0 if lag + 1 < n else 0\n        pair = r1 + r2\n        if pair < 0:\n            break\n        tau += 2 * pair\n    return float(n / tau)\n\n\ndef _fast_diagnostics(alpha_arr, theta_arr, labels):\n    \"\"\"Compute R-hat and ESS over all parameters without arviz.\"\"\"\n    rhats, esss = [], []\n    for d in range(alpha_arr.shape[2]):\n        rhats.append(_split_rhat(alpha_arr[:, :, d]))\n        esss.append(_bulk_ess(alpha_arr[:, :, d]))\n    k = len(labels)\n    for i in range(k):\n        for z in [0, 1]:\n            for zh in range(theta_arr.shape[4]):\n                ch = theta_arr[:, :, i, z, zh]\n                rhats.append(_split_rhat(ch))\n                esss.append(_bulk_ess(ch))\n    return max(rhats), min(esss)\n\n\ndef _log_target_alpha(alpha, theta_z):\n    \"\"\"Log posterior for alpha_0[z] in log-alpha space (includes Jacobian).\"\"\"\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = 2.0 * np.log(alpha) - alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=2000, n_warmup=1000, n_chains=2):\n    \"\"\"Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).\"\"\"\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_alpha, all_theta = [], []\n    t0 = time.time()\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        alpha_samples = np.zeros((n_iter, 2))\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :]) -\n                         _log_target_alpha(alpha[z], theta[:, z, :]))\n                accepted = np.log(rng.rand()) < log_r\n                if accepted:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(accepted)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                idx = it - n_warmup\n                alpha_samples[idx] = alpha.copy()\n                theta_samples[idx] = theta.copy()\n\n        all_alpha.append(alpha_samples)\n        all_theta.append(theta_samples)\n\n    runtime = time.time() - t0\n    alpha_arr = np.stack(all_alpha)\n    theta_arr = np.stack(all_theta)\n\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n\n    rhat_max, ess_min = _fast_diagnostics(alpha_arr, theta_arr, labels)\n\n    diag = {'rhat_max': rhat_max, 'ess_min': ess_min, 'divergent_count': 0,\n            'runtime_seconds': runtime, 'hb_method': 'gibbs'}\n    return C, diag\n\n\ndef estimate_cm_hb_mcmc(counts, labels, seed=42, draws=1000, tune=500, chains=2):\n    \"\"\"Full Bayesian HB with PyMC MCMC.\"\"\"\n    k = len(labels)\n    n_per_sz = counts.sum(axis=2)\n\n    with pm.Model():\n        alpha_0 = pm.Gamma('alpha_0', alpha=2, beta=1, shape=2)\n        for z in [0, 1]:\n            for i, s in enumerate(labels):\n                nsz = int(n_per_sz[i, z])\n                if nsz == 0:\n                    continue\n                a = pt.stack([alpha_0[z] / 2, alpha_0[z] / 2])\n                theta = pm.Dirichlet(f'theta_{s}_z{z}', a=a)\n                pm.Multinomial(f'obs_{s}_z{z}', n=nsz, p=theta,\n                               observed=counts[i, z, :].astype('int32'))\n        t0 = time.time()\n        trace = pm.sample(draws=draws, tune=tune, chains=chains,\n                          random_seed=seed, progressbar=False)\n        runtime = time.time() - t0\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            vn = f'theta_{s}_z{z}'\n            if vn in trace.posterior:\n                C_s[z, :] = trace.posterior[vn].values.mean(axis=(0, 1))\n            else:\n                C_s[z, :] = 0.5\n        C[s] = C_s\n\n    all_vars = list(trace.posterior.data_vars)\n    try:\n        summ = az.summary(trace, var_names=all_vars)\n        rhat_max = float(summ['r_hat'].max())\n        ess_min = float(summ['ess_bulk'].min())\n    except Exception:\n        rhat_max = ess_min = np.nan\n    try:\n        divergent = int(trace.sample_stats['diverging'].values.sum())\n    except Exception:\n        divergent = -1\n\n    diag = {'rhat_max': rhat_max, 'ess_min': ess_min,\n            'divergent_count': divergent, 'runtime_seconds': runtime,\n            'hb_method': 'mcmc'}\n    return C, diag\n\n\n# ── Single MC Run ─────────────────────────────────────────────────────────────\n\ndef run_one_mc(regime_name, regime_params, n_expert, k, seed, hb_method='eb'):\n    data = generate_data(regime_params, n_expert, k, seed)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    em = data['expert_mask']\n    labels = SUBGROUP_LABELS[k]\n    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']\n\n    counts = get_counts(Z[em], Z_hat[em], S[em], labels)\n\n    C_mle = estimate_cm_mle(counts, labels)\n\n    if hb_method == 'gibbs':\n        C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed)\n    elif hb_method == 'mcmc' and HAS_PYMC:\n        try:\n            C_hb, hb_diag = estimate_cm_hb_mcmc(counts, labels, seed=seed)\n        except Exception:\n            C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)\n            hb_diag['hb_method'] = 'eb_fallback'\n    else:\n        C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)\n\n    # Global CM (pool all expert labels, Laplace)\n    cg = counts.sum(axis=0)\n    C_gl = np.zeros((2, 2))\n    for z in [0, 1]:\n        n = cg[z, :].sum()\n        for zh in [0, 1]:\n            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5\n\n    M_gl = build_mixing_matrix(C_gl)\n    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}\n    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}\n\n    base = {'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k, 'mc_run': seed}\n    rows = []\n\n    for s in labels:\n        sm = S == s\n        th0_or, se0_or = diff_in_means(Y, T, sm & (Z == 0))\n        th1_or, se1_or = diff_in_means(Y, T, sm & (Z == 1))\n        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))\n        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))\n\n        tau_obs = np.array([th0_n, th1_n])\n        se_obs = np.array([se0_n, se1_n])\n        if np.any(np.isnan(tau_obs)):\n            continue\n\n        tgc, sgc = invert_mixing(M_gl, tau_obs, se_obs)\n        tml, sml = invert_mixing(M_mle[s], tau_obs, se_obs)\n        thb, shb = invert_mixing(M_hb[s], tau_obs, se_obs)\n\n        def mr(method, th0, th1, se0, se1):\n            return {**base, 'subgroup': s, 'method': method,\n                    'tau_hat_z0': th0, 'tau_hat_z1': th1,\n                    'se_z0': se0, 'se_z1': se1,\n                    'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}\n\n        rows.append(mr('oracle', th0_or, th1_or, se0_or, se1_or))\n        rows.append(mr('naive', th0_n, th1_n, se0_n, se1_n))\n        rows.append(mr('global_corrected', tgc[0], tgc[1], sgc[0], sgc[1]))\n        rows.append(mr('mle_laplace', tml[0], tml[1], sml[0], sml[1]))\n        rows.append(mr('hb_dirichlet', thb[0], thb[1], shb[0], shb[1]))\n\n    return rows, {**base, **hb_diag}\n\n\n# ── Aggregation ───────────────────────────────────────────────────────────────\n\ndef aggregate_results(df):\n    rows = []\n    grp_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method']\n    for keys, grp in df.groupby(grp_cols):\n        regime, n_expert, k, subgroup, method = keys\n        row = {'regime': regime, 'n_expert': int(n_expert), 'k_subgroups': int(k),\n               'subgroup': subgroup, 'method': method}\n        n_mc = len(grp)\n        for z in ['z0', 'z1']:\n            err = grp[f'tau_hat_{z}'].values - grp[f'tau_true_{z}'].values\n            bias = err.mean()\n            mse = (err ** 2).mean()\n            rmse = np.sqrt(mse)\n            ci_lo = grp[f'tau_hat_{z}'].values - 1.96 * grp[f'se_{z}'].values\n            ci_hi = grp[f'tau_hat_{z}'].values + 1.96 * grp[f'se_{z}'].values\n            cov = ((ci_lo <= grp[f'tau_true_{z}'].values) &\n                   (grp[f'tau_true_{z}'].values <= ci_hi)).mean()\n            row[f'bias_{z}'] = bias\n            row[f'rmse_{z}'] = rmse\n            row[f'coverage_{z}'] = cov\n            row[f'bias_{z}_se'] = err.std() / np.sqrt(n_mc)\n            mse_se = (err ** 2).std() / np.sqrt(n_mc)\n            row[f'rmse_{z}_se'] = mse_se / (2 * rmse) if rmse > 1e-10 else np.nan\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# ── Output ────────────────────────────────────────────────────────────────────\n\ndef print_summary(df_agg, df_diag):\n    pd.set_option('display.float_format', '{:.4f}'.format)\n\n    # MCMC / Gibbs diagnostics\n    if 'hb_method' in df_diag.columns:\n        for method_label in ['gibbs', 'mcmc']:\n            mrows = df_diag[df_diag['hb_method'] == method_label]\n            if mrows.empty:\n                continue\n            print(f\"\\n── {method_label.upper()} Diagnostics ──────────────────────────────\")\n            print(f\"  Runs:           {len(mrows)}\")\n            rh = mrows['rhat_max'].dropna()\n            es = mrows['ess_min'].dropna()\n            if not rh.empty:\n                print(f\"  R-hat max:      {rh.max():.4f} (target < 1.01)\")\n            if not es.empty:\n                print(f\"  ESS min:        {es.min():.0f} (target > 200)\")\n            print(f\"  Divergent total:{int(mrows['divergent_count'].sum())}\")\n            print(f\"  Runtime median: {mrows['runtime_seconds'].median():.2f}s\")\n\n    # Per-config HB vs MLE comparison\n    print(\"\\n── HB vs MLE RMSE Comparison (subgroup-level, averaged) ──\")\n    for k in sorted(df_agg['k_subgroups'].unique()):\n        print(f\"\\n  K = {int(k)} subgroups\")\n        for regime in ['extreme', 'moderate', 'homogeneous']:\n            sub = df_agg[(df_agg['k_subgroups'] == k) & (df_agg['regime'] == regime)]\n            if sub.empty:\n                continue\n            print(f\"    {regime}:\")\n            print(f\"    {'n_exp':>6s}  {'oracle':>8s}  {'naive':>8s}  {'global':>8s}  \"\n                  f\"{'mle':>8s}  {'hb':>8s}  {'HB vs MLE':>10s}\")\n            for ne in sorted(sub['n_expert'].unique()):\n                vals = {}\n                for m in ['oracle', 'naive', 'global_corrected', 'mle_laplace', 'hb_dirichlet']:\n                    ms = sub[(sub['method'] == m) & (sub['n_expert'] == ne)]\n                    if ms.empty:\n                        vals[m] = np.nan\n                    else:\n                        vals[m] = np.sqrt((ms['rmse_z0'].values ** 2 +\n                                           ms['rmse_z1'].values ** 2).mean())\n                mle_v, hb_v = vals['mle_laplace'], vals['hb_dirichlet']\n                pct = (mle_v - hb_v) / mle_v * 100 if mle_v > 1e-10 else 0\n                tag = f\"{pct:+.1f}%\"\n                print(f\"    {int(ne):6d}  {vals['oracle']:8.4f}  {vals['naive']:8.4f}  \"\n                      f\"{vals['global_corrected']:8.4f}  {mle_v:8.4f}  {hb_v:8.4f}  {tag:>10s}\")\n\n\n# ── Sweep ─────────────────────────────────────────────────────────────────────\n\ndef run_sweep(regime_names, n_experts, k_list, n_mc,\n              hb_method='eb', mcmc_diag_runs=5, verbose=True):\n    all_rows, all_diag = [], []\n    total = sum(1 for k in k_list for r in regime_names if r in REGIMES[k]) * len(n_experts) * n_mc\n    count = 0\n    t0 = time.time()\n\n    for k in k_list:\n        for rn in regime_names:\n            if rn not in REGIMES[k]:\n                continue\n            rp = REGIMES[k][rn]\n            for ne in n_experts:\n                for mc in range(n_mc):\n                    use = hb_method\n                    if hb_method == 'auto':\n                        use = 'mcmc' if mc < mcmc_diag_runs else 'eb'\n                    try:\n                        rows, diag = run_one_mc(rn, rp, ne, k, seed=mc, hb_method=use)\n                        all_rows.extend(rows)\n                        all_diag.append(diag)\n                    except Exception as e:\n                        if verbose:\n                            print(f\"  WARN: k={k} {rn} ne={ne} mc={mc} failed: {e}\")\n                        all_diag.append({\n                            'regime': rn, 'n_expert': ne, 'k_subgroups': k,\n                            'mc_run': mc, 'hb_method': 'error',\n                            'rhat_max': np.nan, 'ess_min': np.nan,\n                            'divergent_count': -1, 'runtime_seconds': 0.0})\n                    count += 1\n                    if verbose and count % max(1, total // 20) == 0:\n                        el = time.time() - t0\n                        eta = el / count * (total - count)\n                        print(f\"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s | \"\n                              f\"k={k} {rn} ne={ne} mc={mc}\")\n\n    if verbose:\n        print(f\"  Sweep done: {time.time() - t0:.1f}s ({count} runs)\")\n    return pd.DataFrame(all_rows), pd.DataFrame(all_diag)\n\n\n# ── Main ──────────────────────────────────────────────────────────────────────\n\nif __name__ == '__main__':\n    parser = argparse.ArgumentParser()\n    parser.add_argument('--n-mc', type=int, default=100)\n    parser.add_argument('--dry-run', action='store_true')\n    parser.add_argument('--hb-method', choices=['auto', 'mcmc', 'gibbs', 'eb'], default='auto')\n    parser.add_argument('--mcmc-diag-runs', type=int, default=5)\n    args = parser.parse_args()\n\n    n_mc = 5 if args.dry_run else args.n_mc\n    regime_names = ['moderate'] if args.dry_run else ['extreme', 'moderate', 'homogeneous']\n    n_experts = [100] if args.dry_run else DEFAULT_N_EXPERTS\n    k_list = [2] if args.dry_run else DEFAULT_K_LIST\n\n    print(f\"exp-001 HB Synthetic Validation | PyMC={HAS_PYMC}\")\n    print(f\"N={N} n_mc={n_mc} hb={args.hb_method}\")\n    print(f\"Regimes={regime_names} n_experts={n_experts} K={k_list}\\n\")\n\n    # Timing test\n    effective_method = args.hb_method\n    d = generate_data(REGIMES[2]['moderate'], 100, 2, seed=9999)\n    em = d['expert_mask']\n    tc = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], ['A', 'B'])\n\n    if args.hb_method == 'auto':\n        print(\"Timing Gibbs sampler...\")\n        t0 = time.time()\n        _, dg = estimate_cm_hb_gibbs(tc, ['A', 'B'], seed=9999)\n        gt = time.time() - t0\n        print(f\"  Gibbs: {gt:.2f}s | rhat={dg['rhat_max']:.3f} \"\n              f\"ess={dg['ess_min']:.0f}\")\n        if gt < 5:\n            effective_method = 'gibbs'\n            print(f\"  Fast enough → using Gibbs for all runs\")\n        else:\n            effective_method = 'eb'\n            print(f\"  Slow → using EB\")\n    elif args.hb_method == 'mcmc' and HAS_PYMC:\n        print(\"Timing PyMC MCMC...\")\n        t0 = time.time()\n        try:\n            _, dg = estimate_cm_hb_mcmc(tc, ['A', 'B'], seed=9999)\n            mt = time.time() - t0\n            print(f\"  MCMC: {mt:.1f}s | rhat={dg['rhat_max']:.3f} \"\n                  f\"ess={dg['ess_min']:.0f} div={dg['divergent_count']}\")\n        except Exception as e:\n            print(f\"  MCMC failed: {e} → falling back to Gibbs\")\n            effective_method = 'gibbs'\n\n    print(f\"\\nEffective method: {effective_method}\\n\")\n\n    df_raw, df_diag = run_sweep(\n        regime_names, n_experts, k_list, n_mc,\n        hb_method=effective_method, mcmc_diag_runs=args.mcmc_diag_runs)\n\n    df_agg = aggregate_results(df_raw)\n\n    os.makedirs('results', exist_ok=True)\n    agg_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method',\n                'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1',\n                'bias_z0_se', 'rmse_z0_se', 'bias_z1_se', 'rmse_z1_se']\n    df_agg[agg_cols].to_csv('results/exp001_hb_results.csv', index=False)\n\n    diag_cols = ['regime', 'n_expert', 'k_subgroups', 'mc_run',\n                 'rhat_max', 'ess_min', 'divergent_count', 'runtime_seconds']\n    save_cols = [c for c in diag_cols if c in df_diag.columns]\n    if 'hb_method' in df_diag.columns:\n        save_cols.insert(4, 'hb_method')\n    df_diag[save_cols].to_csv('results/exp001_hb_diagnostics.csv', index=False)\n\n    print_summary(df_agg, df_diag)\n\n    print(f\"\\nSaved: results/exp001_hb_results.csv ({len(df_agg)} rows)\")\n    print(f\"Saved: results/exp001_hb_diagnostics.csv ({len(df_diag)} rows)\")\n",
    "structuredPatch": [
      {
        "oldStart": 261,
        "oldLines": 13,
        "newStart": 261,
        "newLines": 13,
        "lines": [
          "     return max(rhats), min(esss)",
          " ",
          " ",
          "-def _log_target_alpha(alpha, theta_z):",
          "+def _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):",
          "     \"\"\"Log posterior for alpha_0[z] in log-alpha space (includes Jacobian).\"\"\"",
          "     if alpha < 1e-10:",
          "         return -1e10",
          "     a = alpha / 2.0",
          "     k = theta_z.shape[0]",
          "-    lp = 2.0 * np.log(alpha) - alpha",
          "+    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha",
          "     lp += k * (gammaln(alpha) - 2.0 * gammaln(a))",
          "     lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))",
          "     return lp"
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

<details open><summary>🔧 Tool call — Edit · `toolu_01LNYoNzKmbzHjvHXwejSQZK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
  "old_string": "def estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=2000, n_warmup=1000, n_chains=2):\n    \"\"\"Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).\"\"\"\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_alpha, all_theta = [], []\n    t0 = time.time()\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        alpha_samples = np.zeros((n_iter, 2))\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :]) -\n                         _log_target_alpha(alpha[z], theta[:, z, :]))",
  "new_string": "def estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=2000, n_warmup=1000, n_chains=2,\n                         hp_a0=3.0, hp_b0=1.0):\n    \"\"\"Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).\n\n    hp_a0, hp_b0: Gamma hyperprior shape/rate on alpha_0 (default Gamma(3,1)).\n    \"\"\"\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_alpha, all_theta = [], []\n    t0 = time.time()\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        alpha_samples = np.zeros((n_iter, 2))\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "b37164f4-2d17-4f2a-b37a-a9d825368e58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LiQ3JPCKFhPGndEkDhBXeq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3225,
      "cache_read_input_tokens": 30704,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3225
      },
      "output_tokens": 69,
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

_source line 12 · 2026-05-20T22:08:20.987Z_

<details><summary>↩ Tool result · `toolu_01LNYoNzKmbzHjvHXwejSQZK`</summary>

```text
The file /home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "2e3543e5-19ff-4ea0-9e3f-ea9d2856d1a7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
    "oldString": "def estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=2000, n_warmup=1000, n_chains=2):\n    \"\"\"Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).\"\"\"\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_alpha, all_theta = [], []\n    t0 = time.time()\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        alpha_samples = np.zeros((n_iter, 2))\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :]) -\n                         _log_target_alpha(alpha[z], theta[:, z, :]))",
    "newString": "def estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=2000, n_warmup=1000, n_chains=2,\n                         hp_a0=3.0, hp_b0=1.0):\n    \"\"\"Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).\n\n    hp_a0, hp_b0: Gamma hyperprior shape/rate on alpha_0 (default Gamma(3,1)).\n    \"\"\"\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_alpha, all_theta = [], []\n    t0 = time.time()\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        alpha_samples = np.zeros((n_iter, 2))\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"\nexp001_hb_synthetic.py - Hierarchical Bayesian EC-HTE Synthetic Validation (exp-001)\n\nCompares confusion matrix estimators for CATE correction under heterogeneous\nmisclassification across subgroups:\n  Oracle, Naive, Global-corrected, MLE (Laplace), HB Dirichlet (partial pooling)\n\nInput: Synthetic DGP parameters (regimes, expert budgets, subgroup counts)\nOutput: results/exp001_hb_results.csv, results/exp001_hb_diagnostics.csv\n\"\"\"\n\nimport argparse\nimport os\nimport sys\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\nfrom scipy.optimize import minimize_scalar\n\nwarnings.filterwarnings('ignore')\n\ntry:\n    import pymc as pm\n    import pytensor.tensor as pt\n    import arviz as az\n    HAS_PYMC = True\nexcept ImportError:\n    HAS_PYMC = False\n\nN = 5000\nSUBGROUP_LABELS = {2: ['A', 'B'], 4: ['A', 'B', 'C', 'D']}\n\nREGIMES = {\n    2: {\n        'extreme':     {'misclass': [0.25, 0.05], 'tau_z1': 0.5, 'tau_z0': 0.1},\n        'moderate':    {'misclass': [0.15, 0.10], 'tau_z1': 0.3, 'tau_z0': 0.15},\n        'homogeneous': {'misclass': [0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},\n    },\n    4: {\n        'extreme':     {'misclass': [0.30, 0.20, 0.10, 0.03], 'tau_z1': 0.5, 'tau_z0': 0.1},\n        'moderate':    {'misclass': [0.20, 0.15, 0.10, 0.05], 'tau_z1': 0.3, 'tau_z0': 0.15},\n        'homogeneous': {'misclass': [0.12, 0.12, 0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},\n    },\n}\n\nDEFAULT_N_EXPERTS = [50, 100, 250, 500, 1000, 2000]\nDEFAULT_K_LIST = [2, 4]\n\n\n# ── DGP ───────────────────────────────────────────────────────────────────────\n\ndef generate_data(regime_params, n_expert, k, seed):\n    rng = np.random.RandomState(seed)\n    labels = SUBGROUP_LABELS[k]\n    T = rng.binomial(1, 0.5, N)\n    Z = rng.binomial(1, 0.5, N)\n    S = rng.choice(labels, N, p=[1.0 / k] * k)\n    X = rng.randn(N, 5)\n    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])\n    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)\n    mc_rates = np.zeros(N)\n    for i, s in enumerate(labels):\n        mc_rates[S == s] = regime_params['misclass'][i]\n    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)\n    idx = rng.choice(N, min(n_expert, N), replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[idx] = True\n    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, X=X, Y=Y, tau=tau, expert_mask=expert_mask)\n\n\n# ── Helpers ───────────────────────────────────────────────────────────────────\n\ndef diff_in_means(Y, T, mask):\n    t1, t0 = mask & (T == 1), mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    \"\"\"Confusion matrix counts per subgroup: (k, 2, 2) = [subgroup, true_z, z_hat].\"\"\"\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef build_mixing_matrix(C):\n    \"\"\"C[z, z_hat] → M[z_hat, z] via Bayes rule (assuming P(Z=0)=P(Z=1)=0.5).\"\"\"\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        cs = C[0, zh] + C[1, zh]\n        if cs > 0:\n            M[zh, 0] = C[0, zh] / cs\n            M[zh, 1] = C[1, zh] / cs\n        else:\n            M[zh, :] = 0.5\n    return M\n\n\ndef invert_mixing(M, tau_obs, se_obs):\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\ndef safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):\n    \"\"\"Invert mixing matrix with condition number guard.\n\n    When cond(M_s) > threshold, matrix inversion is numerically unstable.\n    Falls back to naive (no correction) to avoid catastrophic amplification.\n    \"\"\"\n    cond = np.linalg.cond(M_s)\n    if cond > cond_threshold:\n        return tau_obs.copy()\n    return np.linalg.solve(M_s, tau_obs)\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    \"\"\"Like invert_mixing but with condition number guard.\"\"\"\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# ── Confusion Matrix Estimators ───────────────────────────────────────────────\n\ndef estimate_cm_mle(counts, labels):\n    \"\"\"Per-subgroup MLE with Laplace smoothing (add-1).\"\"\"\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            n = counts[i, z, :].sum()\n            for zh in [0, 1]:\n                C_s[z, zh] = (counts[i, z, zh] + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    \"\"\"Negative log marginal likelihood for Dirichlet-Multinomial.\"\"\"\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_eb(counts, labels):\n    \"\"\"Empirical Bayes HB: optimize shared Dirichlet concentration, posterior mean.\"\"\"\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = 2.0\n            continue\n        res = minimize_scalar(\n            lambda a: _dirmult_neg_ll(a, cl), bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n = counts[i, z, :].sum()\n            d = n + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    diag = {'rhat_max': np.nan, 'ess_min': np.nan, 'divergent_count': 0,\n            'runtime_seconds': 0.0, 'hb_method': 'eb',\n            'alpha_0_z0': alpha_opt[0], 'alpha_0_z1': alpha_opt[1]}\n    return C, diag\n\n\ndef _split_rhat(chains):\n    \"\"\"Split R-hat for a scalar parameter. chains: (n_chains, n_draws).\"\"\"\n    parts = []\n    for c in range(chains.shape[0]):\n        half = chains.shape[1] // 2\n        parts.append(chains[c, :half])\n        parts.append(chains[c, half:2 * half])\n    parts = np.array(parts)\n    m = parts.shape[0]\n    n = parts.shape[1]\n    chain_means = parts.mean(axis=1)\n    W = np.mean(np.var(parts, axis=1, ddof=1))\n    B = n * np.var(chain_means, ddof=1)\n    if W < 1e-20:\n        return 1.0\n    var_hat = (1 - 1.0 / n) * W + B / n\n    return float(np.sqrt(var_hat / W))\n\n\ndef _bulk_ess(chains):\n    \"\"\"Approximate bulk ESS via initial positive sequence. chains: (n_chains, n_draws).\"\"\"\n    x = chains.ravel()\n    n = len(x)\n    mu = x.mean()\n    xc = x - mu\n    max_lag = min(n // 2, 300)\n    c0 = np.dot(xc, xc)\n    if c0 < 1e-20:\n        return float(n)\n    tau = 1.0\n    for lag in range(1, max_lag - 1, 2):\n        r1 = np.dot(xc[:n - lag], xc[lag:]) / c0\n        r2 = np.dot(xc[:n - lag - 1], xc[lag + 1:]) / c0 if lag + 1 < n else 0\n        pair = r1 + r2\n        if pair < 0:\n            break\n        tau += 2 * pair\n    return float(n / tau)\n\n\ndef _fast_diagnostics(alpha_arr, theta_arr, labels):\n    \"\"\"Compute R-hat and ESS over all parameters without arviz.\"\"\"\n    rhats, esss = [], []\n    for d in range(alpha_arr.shape[2]):\n        rhats.append(_split_rhat(alpha_arr[:, :, d]))\n        esss.append(_bulk_ess(alpha_arr[:, :, d]))\n    k = len(labels)\n    for i in range(k):\n        for z in [0, 1]:\n            for zh in range(theta_arr.shape[4]):\n                ch = theta_arr[:, :, i, z, zh]\n                rhats.append(_split_rhat(ch))\n                esss.append(_bulk_ess(ch))\n    return max(rhats), min(esss)\n\n\ndef _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    \"\"\"Log posterior for alpha_0[z] in log-alpha space (includes Jacobian).\"\"\"\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=2000, n_warmup=1000, n_chains=2):\n    \"\"\"Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).\"\"\"\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_alpha, all_theta = [], []\n    t0 = time.time()\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        alpha_samples = np.zeros((n_iter, 2))\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :]) -\n                         _log_target_alpha(alpha[z], theta[:, z, :]))\n                accepted = np.log(rng.rand()) < log_r\n                if accepted:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(accepted)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                idx = it - n_warmup\n                alpha_samples[idx] = alpha.copy()\n                theta_samples[idx] = theta.copy()\n\n        all_alpha.append(alpha_samples)\n        all_theta.append(theta_samples)\n\n    runtime = time.time() - t0\n    alpha_arr = np.stack(all_alpha)\n    theta_arr = np.stack(all_theta)\n\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n\n    rhat_max, ess_min = _fast_diagnostics(alpha_arr, theta_arr, labels)\n\n    diag = {'rhat_max': rhat_max, 'ess_min': ess_min, 'divergent_count': 0,\n            'runtime_seconds': runtime, 'hb_method': 'gibbs'}\n    return C, diag\n\n\ndef estimate_cm_hb_mcmc(counts, labels, seed=42, draws=1000, tune=500, chains=2):\n    \"\"\"Full Bayesian HB with PyMC MCMC.\"\"\"\n    k = len(labels)\n    n_per_sz = counts.sum(axis=2)\n\n    with pm.Model():\n        alpha_0 = pm.Gamma('alpha_0', alpha=2, beta=1, shape=2)\n        for z in [0, 1]:\n            for i, s in enumerate(labels):\n                nsz = int(n_per_sz[i, z])\n                if nsz == 0:\n                    continue\n                a = pt.stack([alpha_0[z] / 2, alpha_0[z] / 2])\n                theta = pm.Dirichlet(f'theta_{s}_z{z}', a=a)\n                pm.Multinomial(f'obs_{s}_z{z}', n=nsz, p=theta,\n                               observed=counts[i, z, :].astype('int32'))\n        t0 = time.time()\n        trace = pm.sample(draws=draws, tune=tune, chains=chains,\n                          random_seed=seed, progressbar=False)\n        runtime = time.time() - t0\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            vn = f'theta_{s}_z{z}'\n            if vn in trace.posterior:\n                C_s[z, :] = trace.posterior[vn].values.mean(axis=(0, 1))\n            else:\n                C_s[z, :] = 0.5\n        C[s] = C_s\n\n    all_vars = list(trace.posterior.data_vars)\n    try:\n        summ = az.summary(trace, var_names=all_vars)\n        rhat_max = float(summ['r_hat'].max())\n        ess_min = float(summ['ess_bulk'].min())\n    except Exception:\n        rhat_max = ess_min = np.nan\n    try:\n        divergent = int(trace.sample_stats['diverging'].values.sum())\n    except Exception:\n        divergent = -1\n\n    diag = {'rhat_max': rhat_max, 'ess_min': ess_min,\n            'divergent_count': divergent, 'runtime_seconds': runtime,\n            'hb_method': 'mcmc'}\n    return C, diag\n\n\n# ── Single MC Run ─────────────────────────────────────────────────────────────\n\ndef run_one_mc(regime_name, regime_params, n_expert, k, seed, hb_method='eb'):\n    data = generate_data(regime_params, n_expert, k, seed)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    em = data['expert_mask']\n    labels = SUBGROUP_LABELS[k]\n    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']\n\n    counts = get_counts(Z[em], Z_hat[em], S[em], labels)\n\n    C_mle = estimate_cm_mle(counts, labels)\n\n    if hb_method == 'gibbs':\n        C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed)\n    elif hb_method == 'mcmc' and HAS_PYMC:\n        try:\n            C_hb, hb_diag = estimate_cm_hb_mcmc(counts, labels, seed=seed)\n        except Exception:\n            C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)\n            hb_diag['hb_method'] = 'eb_fallback'\n    else:\n        C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)\n\n    # Global CM (pool all expert labels, Laplace)\n    cg = counts.sum(axis=0)\n    C_gl = np.zeros((2, 2))\n    for z in [0, 1]:\n        n = cg[z, :].sum()\n        for zh in [0, 1]:\n            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5\n\n    M_gl = build_mixing_matrix(C_gl)\n    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}\n    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}\n\n    base = {'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k, 'mc_run': seed}\n    rows = []\n\n    for s in labels:\n        sm = S == s\n        th0_or, se0_or = diff_in_means(Y, T, sm & (Z == 0))\n        th1_or, se1_or = diff_in_means(Y, T, sm & (Z == 1))\n        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))\n        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))\n\n        tau_obs = np.array([th0_n, th1_n])\n        se_obs = np.array([se0_n, se1_n])\n        if np.any(np.isnan(tau_obs)):\n            continue\n\n        tgc, sgc = invert_mixing(M_gl, tau_obs, se_obs)\n        tml, sml = invert_mixing(M_mle[s], tau_obs, se_obs)\n        thb, shb = invert_mixing(M_hb[s], tau_obs, se_obs)\n\n        def mr(method, th0, th1, se0, se1):\n            return {**base, 'subgroup': s, 'method': method,\n                    'tau_hat_z0': th0, 'tau_hat_z1': th1,\n                    'se_z0': se0, 'se_z1': se1,\n                    'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}\n\n        rows.append(mr('oracle', th0_or, th1_or, se0_or, se1_or))\n        rows.append(mr('naive', th0_n, th1_n, se0_n, se1_n))\n        rows.append(mr('global_corrected', tgc[0], tgc[1], sgc[0], sgc[1]))\n        rows.append(mr('mle_laplace', tml[0], tml[1], sml[0], sml[1]))\n        rows.append(mr('hb_dirichlet', thb[0], thb[1], shb[0], shb[1]))\n\n    return rows, {**base, **hb_diag}\n\n\n# ── Aggregation ───────────────────────────────────────────────────────────────\n\ndef aggregate_results(df):\n    rows = []\n    grp_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method']\n    for keys, grp in df.groupby(grp_cols):\n        regime, n_expert, k, subgroup, method = keys\n        row = {'regime': regime, 'n_expert': int(n_expert), 'k_subgroups': int(k),\n               'subgroup': subgroup, 'method': method}\n        n_mc = len(grp)\n        for z in ['z0', 'z1']:\n            err = grp[f'tau_hat_{z}'].values - grp[f'tau_true_{z}'].values\n            bias = err.mean()\n            mse = (err ** 2).mean()\n            rmse = np.sqrt(mse)\n            ci_lo = grp[f'tau_hat_{z}'].values - 1.96 * grp[f'se_{z}'].values\n            ci_hi = grp[f'tau_hat_{z}'].values + 1.96 * grp[f'se_{z}'].values\n            cov = ((ci_lo <= grp[f'tau_true_{z}'].values) &\n                   (grp[f'tau_true_{z}'].values <= ci_hi)).mean()\n            row[f'bias_{z}'] = bias\n            row[f'rmse_{z}'] = rmse\n            row[f'coverage_{z}'] = cov\n            row[f'bias_{z}_se'] = err.std() / np.sqrt(n_mc)\n            mse_se = (err ** 2).std() / np.sqrt(n_mc)\n            row[f'rmse_{z}_se'] = mse_se / (2 * rmse) if rmse > 1e-10 else np.nan\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# ── Output ────────────────────────────────────────────────────────────────────\n\ndef print_summary(df_agg, df_diag):\n    pd.set_option('display.float_format', '{:.4f}'.format)\n\n    # MCMC / Gibbs diagnostics\n    if 'hb_method' in df_diag.columns:\n        for method_label in ['gibbs', 'mcmc']:\n            mrows = df_diag[df_diag['hb_method'] == method_label]\n            if mrows.empty:\n                continue\n            print(f\"\\n── {method_label.upper()} Diagnostics ──────────────────────────────\")\n            print(f\"  Runs:           {len(mrows)}\")\n            rh = mrows['rhat_max'].dropna()\n            es = mrows['ess_min'].dropna()\n            if not rh.empty:\n                print(f\"  R-hat max:      {rh.max():.4f} (target < 1.01)\")\n            if not es.empty:\n                print(f\"  ESS min:        {es.min():.0f} (target > 200)\")\n            print(f\"  Divergent total:{int(mrows['divergent_count'].sum())}\")\n            print(f\"  Runtime median: {mrows['runtime_seconds'].median():.2f}s\")\n\n    # Per-config HB vs MLE comparison\n    print(\"\\n── HB vs MLE RMSE Comparison (subgroup-level, averaged) ──\")\n    for k in sorted(df_agg['k_subgroups'].unique()):\n        print(f\"\\n  K = {int(k)} subgroups\")\n        for regime in ['extreme', 'moderate', 'homogeneous']:\n            sub = df_agg[(df_agg['k_subgroups'] == k) & (df_agg['regime'] == regime)]\n            if sub.empty:\n                continue\n            print(f\"    {regime}:\")\n            print(f\"    {'n_exp':>6s}  {'oracle':>8s}  {'naive':>8s}  {'global':>8s}  \"\n                  f\"{'mle':>8s}  {'hb':>8s}  {'HB vs MLE':>10s}\")\n            for ne in sorted(sub['n_expert'].unique()):\n                vals = {}\n                for m in ['oracle', 'naive', 'global_corrected', 'mle_laplace', 'hb_dirichlet']:\n                    ms = sub[(sub['method'] == m) & (sub['n_expert'] == ne)]\n                    if ms.empty:\n                        vals[m] = np.nan\n                    else:\n                        vals[m] = np.sqrt((ms['rmse_z0'].values ** 2 +\n                                           ms['rmse_z1'].values ** 2).mean())\n                mle_v, hb_v = vals['mle_laplace'], vals['hb_dirichlet']\n                pct = (mle_v - hb_v) / mle_v * 100 if mle_v > 1e-10 else 0\n                tag = f\"{pct:+.1f}%\"\n                print(f\"    {int(ne):6d}  {vals['oracle']:8.4f}  {vals['naive']:8.4f}  \"\n                      f\"{vals['global_corrected']:8.4f}  {mle_v:8.4f}  {hb_v:8.4f}  {tag:>10s}\")\n\n\n# ── Sweep ─────────────────────────────────────────────────────────────────────\n\ndef run_sweep(regime_names, n_experts, k_list, n_mc,\n              hb_method='eb', mcmc_diag_runs=5, verbose=True):\n    all_rows, all_diag = [], []\n    total = sum(1 for k in k_list for r in regime_names if r in REGIMES[k]) * len(n_experts) * n_mc\n    count = 0\n    t0 = time.time()\n\n    for k in k_list:\n        for rn in regime_names:\n            if rn not in REGIMES[k]:\n                continue\n            rp = REGIMES[k][rn]\n            for ne in n_experts:\n                for mc in range(n_mc):\n                    use = hb_method\n                    if hb_method == 'auto':\n                        use = 'mcmc' if mc < mcmc_diag_runs else 'eb'\n                    try:\n                        rows, diag = run_one_mc(rn, rp, ne, k, seed=mc, hb_method=use)\n                        all_rows.extend(rows)\n                        all_diag.append(diag)\n                    except Exception as e:\n                        if verbose:\n                            print(f\"  WARN: k={k} {rn} ne={ne} mc={mc} failed: {e}\")\n                        all_diag.append({\n                            'regime': rn, 'n_expert': ne, 'k_subgroups': k,\n                            'mc_run': mc, 'hb_method': 'error',\n                            'rhat_max': np.nan, 'ess_min': np.nan,\n                            'divergent_count': -1, 'runtime_seconds': 0.0})\n                    count += 1\n                    if verbose and count % max(1, total // 20) == 0:\n                        el = time.time() - t0\n                        eta = el / count * (total - count)\n                        print(f\"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s | \"\n                              f\"k={k} {rn} ne={ne} mc={mc}\")\n\n    if verbose:\n        print(f\"  Sweep done: {time.time() - t0:.1f}s ({count} runs)\")\n    return pd.DataFrame(all_rows), pd.DataFrame(all_diag)\n\n\n# ── Main ──────────────────────────────────────────────────────────────────────\n\nif __name__ == '__main__':\n    parser = argparse.ArgumentParser()\n    parser.add_argument('--n-mc', type=int, default=100)\n    parser.add_argument('--dry-run', action='store_true')\n    parser.add_argument('--hb-method', choices=['auto', 'mcmc', 'gibbs', 'eb'], default='auto')\n    parser.add_argument('--mcmc-diag-runs', type=int, default=5)\n    args = parser.parse_args()\n\n    n_mc = 5 if args.dry_run else args.n_mc\n    regime_names = ['moderate'] if args.dry_run else ['extreme', 'moderate', 'homogeneous']\n    n_experts = [100] if args.dry_run else DEFAULT_N_EXPERTS\n    k_list = [2] if args.dry_run else DEFAULT_K_LIST\n\n    print(f\"exp-001 HB Synthetic Validation | PyMC={HAS_PYMC}\")\n    print(f\"N={N} n_mc={n_mc} hb={args.hb_method}\")\n    print(f\"Regimes={regime_names} n_experts={n_experts} K={k_list}\\n\")\n\n    # Timing test\n    effective_method = args.hb_method\n    d = generate_data(REGIMES[2]['moderate'], 100, 2, seed=9999)\n    em = d['expert_mask']\n    tc = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], ['A', 'B'])\n\n    if args.hb_method == 'auto':\n        print(\"Timing Gibbs sampler...\")\n        t0 = time.time()\n        _, dg = estimate_cm_hb_gibbs(tc, ['A', 'B'], seed=9999)\n        gt = time.time() - t0\n        print(f\"  Gibbs: {gt:.2f}s | rhat={dg['rhat_max']:.3f} \"\n              f\"ess={dg['ess_min']:.0f}\")\n        if gt < 5:\n            effective_method = 'gibbs'\n            print(f\"  Fast enough → using Gibbs for all runs\")\n        else:\n            effective_method = 'eb'\n            print(f\"  Slow → using EB\")\n    elif args.hb_method == 'mcmc' and HAS_PYMC:\n        print(\"Timing PyMC MCMC...\")\n        t0 = time.time()\n        try:\n            _, dg = estimate_cm_hb_mcmc(tc, ['A', 'B'], seed=9999)\n            mt = time.time() - t0\n            print(f\"  MCMC: {mt:.1f}s | rhat={dg['rhat_max']:.3f} \"\n                  f\"ess={dg['ess_min']:.0f} div={dg['divergent_count']}\")\n        except Exception as e:\n            print(f\"  MCMC failed: {e} → falling back to Gibbs\")\n            effective_method = 'gibbs'\n\n    print(f\"\\nEffective method: {effective_method}\\n\")\n\n    df_raw, df_diag = run_sweep(\n        regime_names, n_experts, k_list, n_mc,\n        hb_method=effective_method, mcmc_diag_runs=args.mcmc_diag_runs)\n\n    df_agg = aggregate_results(df_raw)\n\n    os.makedirs('results', exist_ok=True)\n    agg_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method',\n                'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1',\n                'bias_z0_se', 'rmse_z0_se', 'bias_z1_se', 'rmse_z1_se']\n    df_agg[agg_cols].to_csv('results/exp001_hb_results.csv', index=False)\n\n    diag_cols = ['regime', 'n_expert', 'k_subgroups', 'mc_run',\n                 'rhat_max', 'ess_min', 'divergent_count', 'runtime_seconds']\n    save_cols = [c for c in diag_cols if c in df_diag.columns]\n    if 'hb_method' in df_diag.columns:\n        save_cols.insert(4, 'hb_method')\n    df_diag[save_cols].to_csv('results/exp001_hb_diagnostics.csv', index=False)\n\n    print_summary(df_agg, df_diag)\n\n    print(f\"\\nSaved: results/exp001_hb_results.csv ({len(df_agg)} rows)\")\n    print(f\"Saved: results/exp001_hb_diagnostics.csv ({len(df_diag)} rows)\")\n",
    "structuredPatch": [
      {
        "oldStart": 273,
        "oldLines": 8,
        "newStart": 273,
        "newLines": 12,
        "lines": [
          "     return lp",
          " ",
          " ",
          "-def estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=2000, n_warmup=1000, n_chains=2):",
          "-    \"\"\"Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).\"\"\"",
          "+def estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=2000, n_warmup=1000, n_chains=2,",
          "+                         hp_a0=3.0, hp_b0=1.0):",
          "+    \"\"\"Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).",
          "+",
          "+    hp_a0, hp_b0: Gamma hyperprior shape/rate on alpha_0 (default Gamma(3,1)).",
          "+    \"\"\"",
          "     k = len(labels)",
          "     chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),",
          "                         np.array([0.5, 0.5]), np.array([10.0, 10.0])]"
        ]
      },
      {
        "oldStart": 304,
        "oldLines": 8,
        "newStart": 308,
        "newLines": 8,
        "lines": [
          "             for z in [0, 1]:",
          "                 x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])",
          "                 a_prop = np.exp(x_prop)",
          "-                log_r = (_log_target_alpha(a_prop, theta[:, z, :]) -",
          "-                         _log_target_alpha(alpha[z], theta[:, z, :]))",
          "+                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -",
          "+                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))",
          "                 accepted = np.log(rng.rand()) < log_r",
          "                 if accepted:",
          "                     alpha[z] = a_prop"
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

_source line 13_

Now write the sensitivity script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "25230d40-6c29-46c0-8de7-50e0429216da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbQ1N9pFDufQqXnZAFatgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1414,
      "cache_read_input_tokens": 33929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1414
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

<details open><summary>🔧 Tool call — Write · `toolu_01GBke7NjtmsN3CcLkjPrHNQ`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nexp-001 hyperprior sensitivity analysis.\nTests robustness of HB Dirichlet confusion matrix estimator\nto hyperprior specification.\n\nSweeps over hyperprior scale factors on a single well-conditioned\nconfiguration (K=2/moderate/n=250) with 100 MC runs.\n\nOutput: results/exp001_hyperprior_sensitivity.csv\n\"\"\"\n\nimport argparse\nimport os\nimport time\nimport numpy as np\nimport pandas as pd\n\nfrom exp001_hb_synthetic import (\n    REGIMES, SUBGROUP_LABELS, generate_data, get_counts,\n    estimate_cm_mle, estimate_cm_hb_gibbs,\n    build_mixing_matrix, invert_mixing, diff_in_means,\n)\n\n# Default Gamma hyperprior on alpha_0: Gamma(a0=3, b0=1), mean=3, var=3.\n# Scaling: Gamma(a0/s, b0/s) keeps mean fixed, scales variance by s.\n#   s=0.5 → Gamma(6, 2), var=1.5  (tighter, more shrinkage)\n#   s=1.0 → Gamma(3, 1), var=3    (baseline)\n#   s=2.0 → Gamma(1.5, 0.5), var=6 (wider, closer to MLE)\nDEFAULT_HP_A0 = 3.0\nDEFAULT_HP_B0 = 1.0\nHYPERPRIOR_SCALES = [0.5, 1.0, 2.0]\n\nK = 2\nREGIME_NAME = 'moderate'\nN_EXPERT = 250\n\n\ndef run_one_sensitivity(regime_params, n_expert, k, seed, hp_a0, hp_b0):\n    data = generate_data(regime_params, n_expert, k, seed)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    em = data['expert_mask']\n    labels = SUBGROUP_LABELS[k]\n    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']\n\n    counts = get_counts(Z[em], Z_hat[em], S[em], labels)\n\n    C_mle = estimate_cm_mle(counts, labels)\n    C_hb, _ = estimate_cm_hb_gibbs(counts, labels, seed=seed, hp_a0=hp_a0, hp_b0=hp_b0)\n\n    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}\n    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}\n\n    rows = []\n    for s in labels:\n        sm = S == s\n        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))\n        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))\n        tau_obs = np.array([th0_n, th1_n])\n        se_obs = np.array([se0_n, se1_n])\n        if np.any(np.isnan(tau_obs)):\n            continue\n\n        tml, sml = invert_mixing(M_mle[s], tau_obs, se_obs)\n        thb, shb = invert_mixing(M_hb[s], tau_obs, se_obs)\n\n        base = {'subgroup': s, 'mc_run': seed, 'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}\n        rows.append({**base, 'method': 'mle_laplace',\n                     'tau_hat_z0': tml[0], 'tau_hat_z1': tml[1],\n                     'se_z0': sml[0], 'se_z1': sml[1]})\n        rows.append({**base, 'method': 'hb_dirichlet',\n                     'tau_hat_z0': thb[0], 'tau_hat_z1': thb[1],\n                     'se_z0': shb[0], 'se_z1': shb[1]})\n    return rows\n\n\ndef aggregate(df):\n    rows = []\n    for (scale, method, subgroup), grp in df.groupby(['hyperprior_scale', 'method', 'subgroup']):\n        row = {'hyperprior_scale': scale, 'method': method, 'subgroup': subgroup}\n        for z in ['z0', 'z1']:\n            err = grp[f'tau_hat_{z}'].values - grp[f'tau_true_{z}'].values\n            bias = err.mean()\n            rmse = np.sqrt((err ** 2).mean())\n            ci_lo = grp[f'tau_hat_{z}'].values - 1.96 * grp[f'se_{z}'].values\n            ci_hi = grp[f'tau_hat_{z}'].values + 1.96 * grp[f'se_{z}'].values\n            cov = ((ci_lo <= grp[f'tau_true_{z}'].values) &\n                   (grp[f'tau_true_{z}'].values <= ci_hi)).mean()\n            row[f'bias_{z}'] = bias\n            row[f'rmse_{z}'] = rmse\n            row[f'coverage_{z}'] = cov\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description='exp-001 hyperprior sensitivity')\n    parser.add_argument('--n-mc', type=int, default=100)\n    parser.add_argument('--dry-run', action='store_true')\n    args = parser.parse_args()\n\n    n_mc = 2 if args.dry_run else args.n_mc\n    regime_params = REGIMES[K][REGIME_NAME]\n\n    print(f\"Hyperprior sensitivity: K={K} {REGIME_NAME} n_expert={N_EXPERT} n_mc={n_mc}\")\n    print(f\"Scales: {HYPERPRIOR_SCALES}\")\n    print(f\"Default hyperprior: Gamma({DEFAULT_HP_A0}, {DEFAULT_HP_B0})\\n\")\n\n    all_rows = []\n    total = len(HYPERPRIOR_SCALES) * n_mc\n    count = 0\n    t0 = time.time()\n\n    for scale in HYPERPRIOR_SCALES:\n        hp_a0 = DEFAULT_HP_A0 / scale\n        hp_b0 = DEFAULT_HP_B0 / scale\n        print(f\"  scale={scale:.1f} → Gamma({hp_a0:.1f}, {hp_b0:.1f})\")\n\n        for mc in range(n_mc):\n            rows = run_one_sensitivity(regime_params, N_EXPERT, K, seed=mc,\n                                       hp_a0=hp_a0, hp_b0=hp_b0)\n            for r in rows:\n                r['hyperprior_scale'] = scale\n            all_rows.extend(rows)\n            count += 1\n            if count % max(1, total // 10) == 0:\n                el = time.time() - t0\n                eta = el / count * (total - count)\n                print(f\"    [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s\")\n\n    df_raw = pd.DataFrame(all_rows)\n    df_agg = aggregate(df_raw)\n\n    os.makedirs('results', exist_ok=True)\n    out_cols = ['hyperprior_scale', 'method', 'subgroup',\n                'bias_z0', 'rmse_z0', 'coverage_z0',\n                'bias_z1', 'rmse_z1', 'coverage_z1']\n    df_agg[out_cols].to_csv('results/exp001_hyperprior_sensitivity.csv', index=False)\n\n    print(f\"\\nDone: {time.time() - t0:.1f}s ({count} runs)\\n\")\n\n    # Summary table\n    print(\"hyperprior_scale | method       | RMSE_z0 | RMSE_z1 | Cov_z0 | Cov_z1\")\n    print(\"-\" * 75)\n    for _, row in df_agg.sort_values(['hyperprior_scale', 'method']).iterrows():\n        sg = row['subgroup']\n        print(f\"  {row['hyperprior_scale']:4.1f}  {sg}       | {row['method']:<12s} | \"\n              f\"{row['rmse_z0']:.4f}  | {row['rmse_z1']:.4f}  | \"\n              f\"{row['coverage_z0']:.3f}  | {row['coverage_z1']:.3f}\")\n\n    # Condensed: average over subgroups\n    print(\"\\n── Averaged over subgroups ──\")\n    print(f\"{'scale':>5s} | {'HB RMSE_z0':>10s} | {'HB RMSE_z1':>10s} | \"\n          f\"{'HB Cov_z0':>9s} | {'HB Cov_z1':>9s} | {'MLE RMSE_z0 (ref)':>18s}\")\n    print(\"-\" * 80)\n    for scale in HYPERPRIOR_SCALES:\n        sub = df_agg[df_agg['hyperprior_scale'] == scale]\n        hb = sub[sub['method'] == 'hb_dirichlet']\n        mle = sub[sub['method'] == 'mle_laplace']\n        print(f\"{scale:5.1f} | {hb['rmse_z0'].mean():10.4f} | {hb['rmse_z1'].mean():10.4f} | \"\n              f\"{hb['coverage_z0'].mean():9.3f} | {hb['coverage_z1'].mean():9.3f} | \"\n              f\"{mle['rmse_z0'].mean():18.4f}\")\n\n    print(f\"\\nSaved: results/exp001_hyperprior_sensitivity.csv ({len(df_agg)} rows)\")\n\n\nif __name__ == '__main__':\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "360264bf-c83f-4cdb-975e-2065aac08a58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MbQ1N9pFDufQqXnZAFatgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1414,
      "cache_read_input_tokens": 33929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1414
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

_source line 15 · 2026-05-20T22:09:00.129Z_

<details><summary>↩ Tool result · `toolu_01GBke7NjtmsN3CcLkjPrHNQ`</summary>

```text
File created successfully at: /home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "88bec413-789f-42a4-9520-0063c7edac74",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nexp-001 hyperprior sensitivity analysis.\nTests robustness of HB Dirichlet confusion matrix estimator\nto hyperprior specification.\n\nSweeps over hyperprior scale factors on a single well-conditioned\nconfiguration (K=2/moderate/n=250) with 100 MC runs.\n\nOutput: results/exp001_hyperprior_sensitivity.csv\n\"\"\"\n\nimport argparse\nimport os\nimport time\nimport numpy as np\nimport pandas as pd\n\nfrom exp001_hb_synthetic import (\n    REGIMES, SUBGROUP_LABELS, generate_data, get_counts,\n    estimate_cm_mle, estimate_cm_hb_gibbs,\n    build_mixing_matrix, invert_mixing, diff_in_means,\n)\n\n# Default Gamma hyperprior on alpha_0: Gamma(a0=3, b0=1), mean=3, var=3.\n# Scaling: Gamma(a0/s, b0/s) keeps mean fixed, scales variance by s.\n#   s=0.5 → Gamma(6, 2), var=1.5  (tighter, more shrinkage)\n#   s=1.0 → Gamma(3, 1), var=3    (baseline)\n#   s=2.0 → Gamma(1.5, 0.5), var=6 (wider, closer to MLE)\nDEFAULT_HP_A0 = 3.0\nDEFAULT_HP_B0 = 1.0\nHYPERPRIOR_SCALES = [0.5, 1.0, 2.0]\n\nK = 2\nREGIME_NAME = 'moderate'\nN_EXPERT = 250\n\n\ndef run_one_sensitivity(regime_params, n_expert, k, seed, hp_a0, hp_b0):\n    data = generate_data(regime_params, n_expert, k, seed)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    em = data['expert_mask']\n    labels = SUBGROUP_LABELS[k]\n    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']\n\n    counts = get_counts(Z[em], Z_hat[em], S[em], labels)\n\n    C_mle = estimate_cm_mle(counts, labels)\n    C_hb, _ = estimate_cm_hb_gibbs(counts, labels, seed=seed, hp_a0=hp_a0, hp_b0=hp_b0)\n\n    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}\n    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}\n\n    rows = []\n    for s in labels:\n        sm = S == s\n        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))\n        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))\n        tau_obs = np.array([th0_n, th1_n])\n        se_obs = np.array([se0_n, se1_n])\n        if np.any(np.isnan(tau_obs)):\n            continue\n\n        tml, sml = invert_mixing(M_mle[s], tau_obs, se_obs)\n        thb, shb = invert_mixing(M_hb[s], tau_obs, se_obs)\n\n        base = {'subgroup': s, 'mc_run': seed, 'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}\n        rows.append({**base, 'method': 'mle_laplace',\n                     'tau_hat_z0': tml[0], 'tau_hat_z1': tml[1],\n                     'se_z0': sml[0], 'se_z1': sml[1]})\n        rows.append({**base, 'method': 'hb_dirichlet',\n                     'tau_hat_z0': thb[0], 'tau_hat_z1': thb[1],\n                     'se_z0': shb[0], 'se_z1': shb[1]})\n    return rows\n\n\ndef aggregate(df):\n    rows = []\n    for (scale, method, subgroup), grp in df.groupby(['hyperprior_scale', 'method', 'subgroup']):\n        row = {'hyperprior_scale': scale, 'method': method, 'subgroup': subgroup}\n        for z in ['z0', 'z1']:\n            err = grp[f'tau_hat_{z}'].values - grp[f'tau_true_{z}'].values\n            bias = err.mean()\n            rmse = np.sqrt((err ** 2).mean())\n            ci_lo = grp[f'tau_hat_{z}'].values - 1.96 * grp[f'se_{z}'].values\n            ci_hi = grp[f'tau_hat_{z}'].values + 1.96 * grp[f'se_{z}'].values\n            cov = ((ci_lo <= grp[f'tau_true_{z}'].values) &\n                   (grp[f'tau_true_{z}'].values <= ci_hi)).mean()\n            row[f'bias_{z}'] = bias\n            row[f'rmse_{z}'] = rmse\n            row[f'coverage_{z}'] = cov\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description='exp-001 hyperprior sensitivity')\n    parser.add_argument('--n-mc', type=int, default=100)\n    parser.add_argument('--dry-run', action='store_true')\n    args = parser.parse_args()\n\n    n_mc = 2 if args.dry_run else args.n_mc\n    regime_params = REGIMES[K][REGIME_NAME]\n\n    print(f\"Hyperprior sensitivity: K={K} {REGIME_NAME} n_expert={N_EXPERT} n_mc={n_mc}\")\n    print(f\"Scales: {HYPERPRIOR_SCALES}\")\n    print(f\"Default hyperprior: Gamma({DEFAULT_HP_A0}, {DEFAULT_HP_B0})\\n\")\n\n    all_rows = []\n    total = len(HYPERPRIOR_SCALES) * n_mc\n    count = 0\n    t0 = time.time()\n\n    for scale in HYPERPRIOR_SCALES:\n        hp_a0 = DEFAULT_HP_A0 / scale\n        hp_b0 = DEFAULT_HP_B0 / scale\n        print(f\"  scale={scale:.1f} → Gamma({hp_a0:.1f}, {hp_b0:.1f})\")\n\n        for mc in range(n_mc):\n            rows = run_one_sensitivity(regime_params, N_EXPERT, K, seed=mc,\n                                       hp_a0=hp_a0, hp_b0=hp_b0)\n            for r in rows:\n                r['hyperprior_scale'] = scale\n            all_rows.extend(rows)\n            count += 1\n            if count % max(1, total // 10) == 0:\n                el = time.time() - t0\n                eta = el / count * (total - count)\n                print(f\"    [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s\")\n\n    df_raw = pd.DataFrame(all_rows)\n    df_agg = aggregate(df_raw)\n\n    os.makedirs('results', exist_ok=True)\n    out_cols = ['hyperprior_scale', 'method', 'subgroup',\n                'bias_z0', 'rmse_z0', 'coverage_z0',\n                'bias_z1', 'rmse_z1', 'coverage_z1']\n    df_agg[out_cols].to_csv('results/exp001_hyperprior_sensitivity.csv', index=False)\n\n    print(f\"\\nDone: {time.time() - t0:.1f}s ({count} runs)\\n\")\n\n    # Summary table\n    print(\"hyperprior_scale | method       | RMSE_z0 | RMSE_z1 | Cov_z0 | Cov_z1\")\n    print(\"-\" * 75)\n    for _, row in df_agg.sort_values(['hyperprior_scale', 'method']).iterrows():\n        sg = row['subgroup']\n        print(f\"  {row['hyperprior_scale']:4.1f}  {sg}       | {row['method']:<12s} | \"\n              f\"{row['rmse_z0']:.4f}  | {row['rmse_z1']:.4f}  | \"\n              f\"{row['coverage_z0']:.3f}  | {row['coverage_z1']:.3f}\")\n\n    # Condensed: average over subgroups\n    print(\"\\n── Averaged over subgroups ──\")\n    print(f\"{'scale':>5s} | {'HB RMSE_z0':>10s} | {'HB RMSE_z1':>10s} | \"\n          f\"{'HB Cov_z0':>9s} | {'HB Cov_z1':>9s} | {'MLE RMSE_z0 (ref)':>18s}\")\n    print(\"-\" * 80)\n    for scale in HYPERPRIOR_SCALES:\n        sub = df_agg[df_agg['hyperprior_scale'] == scale]\n        hb = sub[sub['method'] == 'hb_dirichlet']\n        mle = sub[sub['method'] == 'mle_laplace']\n        print(f\"{scale:5.1f} | {hb['rmse_z0'].mean():10.4f} | {hb['rmse_z1'].mean():10.4f} | \"\n              f\"{hb['coverage_z0'].mean():9.3f} | {hb['coverage_z1'].mean():9.3f} | \"\n              f\"{mle['rmse_z0'].mean():18.4f}\")\n\n    print(f\"\\nSaved: results/exp001_hyperprior_sensitivity.csv ({len(df_agg)} rows)\")\n\n\nif __name__ == '__main__':\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 16_

Now let me verify the import works and do a dry-run (2 MC runs).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "047912b0-028e-40e7-aa7f-215d27d20e69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpN15mAZWC4Ra9DVXvpyj5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2802,
      "cache_read_input_tokens": 35343,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2802
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

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_01Xk2hgomjpdai4B7PF4WbJQ`</summary>

```json
{
  "command": "python exp001_hyperprior_sensitivity.py --dry-run 2>&1",
  "description": "Dry-run sensitivity script with 2 MC runs",
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
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "c9ef495e-0f16-4115-a13c-1177477395e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpN15mAZWC4Ra9DVXvpyj5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2802,
      "cache_read_input_tokens": 35343,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2802
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

_source line 18 · 2026-05-20T22:09:04.278Z_

<details><summary>↩ Tool result · reported error · `toolu_01Xk2hgomjpdai4B7PF4WbJQ`</summary>

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
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "0c67438d-a48c-4856-bd75-ad2b957e9d2b",
  "tool_use_result": "Error: Exit code 127\n/bin/bash: line 1: python: command not found"
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_01TkUrwGqF94t2saQiVRao2E`</summary>

```json
{
  "command": "which python3 && python3 /home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py --dry-run 2>&1",
  "description": "Dry-run sensitivity script with python3",
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
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "251b5505-eff4-49be-8620-a13d9feb0521",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0138ahEwggZj6pTGPto2uRCg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 175,
      "cache_read_input_tokens": 38145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 175
      },
      "output_tokens": 70,
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

_source line 20_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bwuxlst61",
  "tool_use_id": "toolu_01TkUrwGqF94t2saQiVRao2E",
  "description": "Dry-run sensitivity script with python3",
  "task_type": "local_bash",
  "uuid": "63a2b89c-dfc3-4ac5-a5ac-c144981b9f4a",
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92"
}
```

---

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bwuxlst61",
  "tool_use_id": "toolu_01TkUrwGqF94t2saQiVRao2E",
  "status": "completed",
  "output_file": "",
  "summary": "Dry-run sensitivity script with python3",
  "uuid": "93c3058f-803d-461a-b760-aa7bed693353",
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92"
}
```

---

### Tool result

_source line 22 · 2026-05-20T22:09:19.991Z_

<details><summary>↩ Tool result · `toolu_01TkUrwGqF94t2saQiVRao2E`</summary>

```text
/usr/bin/python3
Hyperprior sensitivity: K=2 moderate n_expert=250 n_mc=2
Scales: [0.5, 1.0, 2.0]
Default hyperprior: Gamma(3.0, 1.0)

  scale=0.5 → Gamma(6.0, 2.0)
    [1/6] 2s elapsed, ETA 9s
    [2/6] 4s elapsed, ETA 7s
  scale=1.0 → Gamma(3.0, 1.0)
    [3/6] 5s elapsed, ETA 5s
    [4/6] 7s elapsed, ETA 4s
  scale=2.0 → Gamma(1.5, 0.5)
    [5/6] 9s elapsed, ETA 2s
    [6/6] 11s elapsed, ETA 0s

Done: 10.9s (6 runs)

hyperprior_scale | method       | RMSE_z0 | RMSE_z1 | Cov_z0 | Cov_z1
---------------------------------------------------------------------------
   0.5  A       | hb_dirichlet | 0.0293  | 0.0681  | 1.000  | 1.000
   0.5  B       | hb_dirichlet | 0.0448  | 0.0587  | 1.000  | 1.000
   0.5  A       | mle_laplace  | 0.0292  | 0.0681  | 1.000  | 1.000
   0.5  B       | mle_laplace  | 0.0447  | 0.0588  | 1.000  | 1.000
   1.0  A       | hb_dirichlet | 0.0291  | 0.0680  | 1.000  | 1.000
   1.0  B       | hb_dirichlet | 0.0442  | 0.0589  | 1.000  | 1.000
   1.0  A       | mle_laplace  | 0.0292  | 0.0681  | 1.000  | 1.000
   1.0  B       | mle_laplace  | 0.0447  | 0.0588  | 1.000  | 1.000
   2.0  A       | hb_dirichlet | 0.0289  | 0.0678  | 1.000  | 1.000
   2.0  B       | hb_dirichlet | 0.0438  | 0.0591  | 1.000  | 1.000
   2.0  A       | mle_laplace  | 0.0292  | 0.0681  | 1.000  | 1.000
   2.0  B       | mle_laplace  | 0.0447  | 0.0588  | 1.000  | 1.000

── Averaged over subgroups ──
scale | HB RMSE_z0 | HB RMSE_z1 | HB Cov_z0 | HB Cov_z1 |  MLE RMSE_z0 (ref)
--------------------------------------------------------------------------------
  0.5 |     0.0370 |     0.0634 |     1.000 |     1.000 |             0.0369
  1.0 |     0.0366 |     0.0634 |     1.000 |     1.000 |             0.0369
  2.0 |     0.0363 |     0.0635 |     1.000 |     1.000 |             0.0369

Saved: results/exp001_hyperprior_sensitivity.csv (12 rows)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "789906f3-4e46-4006-b6e7-689d702a4623",
  "tool_use_result": {
    "stdout": "/usr/bin/python3\nHyperprior sensitivity: K=2 moderate n_expert=250 n_mc=2\nScales: [0.5, 1.0, 2.0]\nDefault hyperprior: Gamma(3.0, 1.0)\n\n  scale=0.5 → Gamma(6.0, 2.0)\n    [1/6] 2s elapsed, ETA 9s\n    [2/6] 4s elapsed, ETA 7s\n  scale=1.0 → Gamma(3.0, 1.0)\n    [3/6] 5s elapsed, ETA 5s\n    [4/6] 7s elapsed, ETA 4s\n  scale=2.0 → Gamma(1.5, 0.5)\n    [5/6] 9s elapsed, ETA 2s\n    [6/6] 11s elapsed, ETA 0s\n\nDone: 10.9s (6 runs)\n\nhyperprior_scale | method       | RMSE_z0 | RMSE_z1 | Cov_z0 | Cov_z1\n---------------------------------------------------------------------------\n   0.5  A       | hb_dirichlet | 0.0293  | 0.0681  | 1.000  | 1.000\n   0.5  B       | hb_dirichlet | 0.0448  | 0.0587  | 1.000  | 1.000\n   0.5  A       | mle_laplace  | 0.0292  | 0.0681  | 1.000  | 1.000\n   0.5  B       | mle_laplace  | 0.0447  | 0.0588  | 1.000  | 1.000\n   1.0  A       | hb_dirichlet | 0.0291  | 0.0680  | 1.000  | 1.000\n   1.0  B       | hb_dirichlet | 0.0442  | 0.0589  | 1.000  | 1.000\n   1.0  A       | mle_laplace  | 0.0292  | 0.0681  | 1.000  | 1.000\n   1.0  B       | mle_laplace  | 0.0447  | 0.0588  | 1.000  | 1.000\n   2.0  A       | hb_dirichlet | 0.0289  | 0.0678  | 1.000  | 1.000\n   2.0  B       | hb_dirichlet | 0.0438  | 0.0591  | 1.000  | 1.000\n   2.0  A       | mle_laplace  | 0.0292  | 0.0681  | 1.000  | 1.000\n   2.0  B       | mle_laplace  | 0.0447  | 0.0588  | 1.000  | 1.000\n\n── Averaged over subgroups ──\nscale | HB RMSE_z0 | HB RMSE_z1 | HB Cov_z0 | HB Cov_z1 |  MLE RMSE_z0 (ref)\n--------------------------------------------------------------------------------\n  0.5 |     0.0370 |     0.0634 |     1.000 |     1.000 |             0.0369\n  1.0 |     0.0366 |     0.0634 |     1.000 |     1.000 |             0.0369\n  2.0 |     0.0363 |     0.0635 |     1.000 |     1.000 |             0.0369\n\nSaved: results/exp001_hyperprior_sensitivity.csv (12 rows)",
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

_source line 23_

Dry-run passes. Let me also verify the original script's default behavior is unchanged.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "26f7ff7e-7bfd-47af-95c8-800d7ba759ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016277fwpdd3miNLcuG9PYTN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1222,
      "cache_read_input_tokens": 38320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1222
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

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_01Hqakx8yFNo182FcdYGHxke`</summary>

```json
{
  "command": "python3 -c \"\nfrom exp001_hb_synthetic import estimate_cm_hb_gibbs, generate_data, get_counts, REGIMES\nimport numpy as np\n\nd = generate_data(REGIMES[2]['moderate'], 100, 2, seed=42)\nem = d['expert_mask']\ncounts = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], ['A', 'B'])\n\n# Default call (no hp args) should match explicit defaults\nC1, _ = estimate_cm_hb_gibbs(counts, ['A', 'B'], seed=42)\nC2, _ = estimate_cm_hb_gibbs(counts, ['A', 'B'], seed=42, hp_a0=3.0, hp_b0=1.0)\n\nfor s in ['A', 'B']:\n    assert np.allclose(C1[s], C2[s]), f'Mismatch for subgroup {s}'\nprint('Default behavior preserved ✓')\n\" 2>&1",
  "description": "Verify default behavior unchanged",
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
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "ffcb739b-5171-420e-bb3e-fef7d48c6a4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016277fwpdd3miNLcuG9PYTN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1222,
      "cache_read_input_tokens": 38320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1222
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

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b8wy6f2m2",
  "tool_use_id": "toolu_01Hqakx8yFNo182FcdYGHxke",
  "description": "Verify default behavior unchanged",
  "task_type": "local_bash",
  "uuid": "6aeda6bd-b914-42aa-b081-059fc737e77e",
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92"
}
```

---

### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b8wy6f2m2",
  "tool_use_id": "toolu_01Hqakx8yFNo182FcdYGHxke",
  "status": "completed",
  "output_file": "",
  "summary": "Verify default behavior unchanged",
  "uuid": "14a73625-886f-4d0c-9711-7c5f7dcc6bff",
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92"
}
```

---

### Tool result

_source line 27 · 2026-05-20T22:09:31.957Z_

<details><summary>↩ Tool result · `toolu_01Hqakx8yFNo182FcdYGHxke`</summary>

```text
Default behavior preserved ✓
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "6ee19b48-89d8-4596-97f6-ef9213b99cf7",
  "tool_use_result": {
    "stdout": "Default behavior preserved ✓",
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

Done. Summary of changes:

1. **`exp001_hb_synthetic.py`** — Added `hp_a0=3.0, hp_b0=1.0` parameters to `_log_target_alpha` and `estimate_cm_hb_gibbs`. Defaults match the original Gamma(3,1) behavior, so no existing code is affected.

2. **`exp001_hyperprior_sensitivity.py`** — New script that sweeps `hyperprior_scale ∈ {0.5, 1.0, 2.0}` over K=2/moderate/n=250 with 100 MC runs. Scaling uses Gamma(a₀/s, b₀/s) to keep the prior mean fixed at 3 while varying variance (s=0.5 → tighter/more shrinkage, s=2.0 → wider/closer to MLE). Each run computes both HB and MLE baseline. Outputs `results/exp001_hyperprior_sensitivity.csv` and prints a condensed summary table.

Dry-run (2 MC) completed successfully in ~11s. Full 100 MC run is deferred per instructions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "uuid": "df81ba0f-3171-469a-a31b-73d072354bad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FgMPL1kmXR3VA69r2jwyVP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 384,
      "cache_read_input_tokens": 39542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 384
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

_source line 29_

Done. Summary of changes:

1. **`exp001_hb_synthetic.py`** — Added `hp_a0=3.0, hp_b0=1.0` parameters to `_log_target_alpha` and `estimate_cm_hb_gibbs`. Defaults match the original Gamma(3,1) behavior, so no existing code is affected.

2. **`exp001_hyperprior_sensitivity.py`** — New script that sweeps `hyperprior_scale ∈ {0.5, 1.0, 2.0}` over K=2/moderate/n=250 with 100 MC runs. Scaling uses Gamma(a₀/s, b₀/s) to keep the prior mean fixed at 3 while varying variance (s=0.5 → tighter/more shrinkage, s=2.0 → wider/closer to MLE). Each run computes both HB and MLE baseline. Outputs `results/exp001_hyperprior_sensitivity.csv` and prints a condensed summary table.

Dry-run (2 MC) completed successfully in ~11s. Full 100 MC run is deferred per instructions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 158811,
  "duration_api_ms": 144385,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "91f4cbf1-67e9-4e4e-bc27-b5108cfcbb92",
  "total_cost_usd": 0.50911875,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 28085,
    "cache_read_input_tokens": 247035,
    "output_tokens": 8335,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 28085,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 282,
        "cache_read_input_tokens": 39542,
        "cache_creation_input_tokens": 384,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 384
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 8335,
      "cacheReadInputTokens": 247035,
      "cacheCreationInputTokens": 28085,
      "webSearchRequests": 0,
      "costUSD": 0.50746875,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    },
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1555,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00165,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "db819bf3-2d56-427d-9ed7-e1a713be837e"
}
```

</details>

---
