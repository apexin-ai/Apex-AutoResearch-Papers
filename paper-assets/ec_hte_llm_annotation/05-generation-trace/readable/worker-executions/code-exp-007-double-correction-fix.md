# code exp 007 double correction fix

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_code_exp-007-double-correction-fix_20260520T223135.log`
- **Structured JSON:** [`348ee7bea83836f5b4a0.json`](../../sessions/34/348ee7bea83836f5b4a0.json)

## Before a recorded user message

30 recorded events

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
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
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
  "uuid": "dd77159c-37f2-41e4-bf9b-8b25518769cf",
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
    "resetsAt": 1779326400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ab504cce-db6a-433c-b6c0-a7a29cba947e",
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903"
}
```

---

### Assistant

_source line 4_

I'll start by reading the file to understand the current code structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "b7357849-daf7-424c-a60e-e6f7a8885bf1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0188NiRRCeGQv1HEAUsaDvFw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7573,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7573
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

<details open><summary>🔧 Tool call — Read · `toolu_01SHgni1KH7mHPCA15HaaH8M`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "ad2ff798-d386-4025-a107-51b0734b1f2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0188NiRRCeGQv1HEAUsaDvFw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 7573,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7573
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

_source line 6 · 2026-05-20T22:31:54.309Z_

<details><summary>↩ Tool result · `toolu_01SHgni1KH7mHPCA15HaaH8M`</summary>

```text
1	"""
2	exp-007: PPCI + Stratified MLE Baseline Comparison for EC-HTE
3	Compares measurement-model-level correction (EC-HTE) vs estimand-level correction (Stratified MLE)
4	vs standard PPCI approach. DGP uses pure covariate-error: only Z has LLM misclassification.
5	Outcome Y can optionally have measurement error (sigma_outcome > 0).
6	"""
7	
8	import numpy as np
9	import pandas as pd
10	import sys
11	import time
12	import warnings
13	warnings.filterwarnings('ignore')
14	
15	# === DGP ===
16	
17	REGIMES = {
18	    'extreme':     {'tau_z1': 0.5, 'tau_z0': 0.1},
19	    'moderate':    {'tau_z1': 0.3, 'tau_z0': 0.15},
20	    'homogeneous': {'tau_z1': 0.25, 'tau_z0': 0.20},
21	}
22	
23	MISCLASS_K2 = {
24	    'extreme':     [0.25, 0.05],
25	    'moderate':    [0.15, 0.10],
26	    'homogeneous': [0.12, 0.12],
27	}
28	
29	MISCLASS_K4 = {
30	    'extreme':     [0.30, 0.20, 0.10, 0.03],
31	    'moderate':    [0.20, 0.15, 0.10, 0.05],
32	    'homogeneous': [0.12, 0.12, 0.12, 0.12],
33	}
34	
35	OUTCOME_BIAS = {
36	    'extreme':     [0.3, 0.1, 0.5, 0.2],
37	    'moderate':    [0.15, 0.05, 0.25, 0.10],
38	    'homogeneous': [0.1, 0.1, 0.1, 0.1],
39	}
40	
41	DGP_CONFIGS = {
42	    'A_covariate_only':  {'has_covariate_error': True,  'has_outcome_error': False},
43	    'B_outcome_only':    {'has_covariate_error': False, 'has_outcome_error': True},
44	    'C_both_errors':     {'has_covariate_error': True,  'has_outcome_error': True},
45	    'D_no_error':        {'has_covariate_error': False, 'has_outcome_error': False},
46	}
47	
48	N = 5000
49	N_EXPERTS = [50, 100, 250, 500]
50	N_MC = 100
51	OUTCOME_NOISE_LEVELS = [0.0, 0.5, 1.0]
52	
53	
54	def generate_data(regime_params, misclass_rates, n_expert, k_subgroups, seed,
55	                  sigma_outcome=0.0, outcome_noise_heterogeneous=True,
56	                  has_covariate_error=True, has_outcome_error=False,
57	                  outcome_bias_per_subgroup=None):
58	    """Generate synthetic data with configurable covariate and outcome error.
59	
60	    DGP A (covariate only): Z_hat has misclassification, Y = Y_true
61	    DGP B (outcome only): Z_hat = Z, Y has treatment-differential bias
62	    DGP C (both): Z_hat has misclassification AND Y has bias
63	    DGP D (no error): Z_hat = Z, Y = Y_true
64	    """
65	    rng = np.random.RandomState(seed)
66	    k = k_subgroups
67	
68	    T = rng.binomial(1, 0.5, N)
69	    Z = rng.binomial(1, 0.5, N)
70	    S = rng.choice(k, N, p=[1/k]*k)
71	    X = rng.randn(N, 5)
72	
73	    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])
74	    eps = rng.randn(N)
75	    Y_true = 1 + tau * T + 0.5 * X[:, 0] + eps
76	    Y = Y_true.copy()
77	
78	    if has_outcome_error:
79	        if outcome_bias_per_subgroup is not None:
80	            for i in range(k):
81	                s_mask = (S == i)
82	                bias_i = outcome_bias_per_subgroup[i] if i < len(outcome_bias_per_subgroup) else outcome_bias_per_subgroup[-1]
83	                Y[s_mask] += bias_i * T[s_mask]
84	        if sigma_outcome > 0:
85	            for i in range(k):
86	                s_mask = (S == i)
87	                noise_scale = sigma_outcome * (1 + 0.5 * i / max(k - 1, 1))
88	                Y[s_mask] += rng.normal(0, noise_scale, s_mask.sum())
89	
90	    if has_covariate_error:
91	        mc_rates = np.array([misclass_rates[s] for s in S])
92	        flip = rng.rand(N) < mc_rates
93	        Z_hat = np.where(flip, 1 - Z, Z)
94	    else:
95	        Z_hat = Z.copy()
96	
97	    expert_idx = rng.choice(N, n_expert, replace=False)
98	    expert_mask = np.zeros(N, dtype=bool)
99	    expert_mask[expert_idx] = True
100	
101	    return {
102	        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'X': X, 'Y': Y,
103	        'Y_true': Y_true, 'tau': tau, 'expert_mask': expert_mask,
104	    }
105	
106	
107	# === Confusion Matrix Estimators ===
108	
109	def estimate_cm_mle(z_true, z_hat):
110	    """MLE confusion matrix with Laplace smoothing. C[z, z_hat] = P(Z_hat=z_hat | Z=z)."""
111	    C = np.zeros((2, 2))
112	    for zt in [0, 1]:
113	        mask = z_true == zt
114	        for zh in [0, 1]:
115	            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (mask.sum() + 2)
116	    return C
117	
118	
119	def estimate_cm_hb(z_true, z_hat, all_subgroup_data):
120	    """Hierarchical Bayesian confusion matrix estimator (placeholder).
121	
122	    # TODO: integrate HB from exp001 after MCMC fix
123	    Uses Dirichlet-Multinomial hierarchical model with partial pooling across subgroups.
124	    """
125	    return estimate_cm_mle(z_true, z_hat)
126	
127	
128	# === Correction Methods ===
129	
130	def diff_in_means(Y, T, mask):
131	    """Difference-in-means estimator for subpopulation defined by mask."""
132	    t1 = mask & (T == 1)
133	    t0 = mask & (T == 0)
134	    n1, n0 = t1.sum(), t0.sum()
135	    if n1 < 2 or n0 < 2:
136	        return np.nan, np.nan
137	    y1, y0 = Y[t1], Y[t0]
138	    tau_hat = y1.mean() - y0.mean()
139	    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
140	    return tau_hat, se
141	
142	
143	def build_mixing_matrix(C, p_z, p_z_hat):
144	    """M[z_hat, z] = P(Z=z | Z_hat=z_hat) via Bayes' rule."""
145	    M = np.zeros((2, 2))
146	    for zh in [0, 1]:
147	        for z in [0, 1]:
148	            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh]
149	    return M
150	
151	
152	def invert_mixing(M, tau_obs, se_obs):
153	    """Apply M^{-1} correction. Returns (tau_corrected, se_corrected)."""
154	    det = np.linalg.det(M)
155	    if abs(det) < 1e-10:
156	        return tau_obs.copy(), se_obs.copy()
157	    M_inv = np.linalg.inv(M)
158	    tau_corrected = M_inv @ tau_obs
159	    sigma_obs = np.diag(se_obs ** 2)
160	    sigma_corrected = M_inv @ sigma_obs @ M_inv.T
161	    se_corrected = np.sqrt(np.diag(sigma_corrected))
162	    return tau_corrected, se_corrected
163	
164	
165	def method_oracle(data, s_val):
166	    """Oracle: use true Z within subgroup s."""
167	    Y, T, Z, S = data['Y'], data['T'], data['Z'], data['S']
168	    s_mask = S == s_val
169	    th0, se0 = diff_in_means(Y, T, s_mask & (Z == 0))
170	    th1, se1 = diff_in_means(Y, T, s_mask & (Z == 1))
171	    return th0, th1, se0, se1
172	
173	
174	def method_naive(data, s_val):
175	    """Naive: use Z_hat within subgroup s, no correction."""
176	    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']
177	    s_mask = S == s_val
178	    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))
179	    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))
180	    return th0, th1, se0, se1
181	
182	
183	def method_global_corrected(data, s_val, C_global, p_z_global, p_zh_global):
184	    """Global-corrected: use global M_global^{-1} on subgroup-level observed CATEs."""
185	    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']
186	    s_mask = S == s_val
187	
188	    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))
189	    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))
190	    if np.isnan(th0) or np.isnan(th1):
191	        return np.nan, np.nan, np.nan, np.nan
192	
193	    M = build_mixing_matrix(C_global, p_z_global, p_zh_global)
194	    tau_corr, se_corr = invert_mixing(M, np.array([th0, th1]), np.array([se0, se1]))
195	    return tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]
196	
197	
198	def method_stratified_mle(data, s_val, C_s, p_z_s, p_zh_s):
199	    """Stratified MLE: per-subgroup independent correction.
200	
201	    Each subgroup estimates its own confusion matrix independently (no pooling).
202	    This is estimand-level correction -- correct the CATE estimate directly
203	    using the subgroup's own confusion matrix.
204	
205	    Key difference from EC-HTE: no cross-subgroup shrinkage.
206	    When n_expert is small per subgroup, Stratified MLE has high variance.
207	    """
208	    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']
209	    s_mask = S == s_val
210	
211	    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))
212	    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))
213	    if np.isnan(th0) or np.isnan(th1):
214	        return np.nan, np.nan, np.nan, np.nan
215	
216	    M_s = build_mixing_matrix(C_s, p_z_s, p_zh_s)
217	    tau_corr, se_corr = invert_mixing(M_s, np.array([th0, th1]), np.array([se0, se1]))
218	    return tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]
219	
220	
221	def method_ec_hte(data, s_val, C_s_hb, p_z_s, p_zh_s):
222	    """EC-HTE: hierarchical Bayesian confusion matrix + subgroup correction.
223	
224	    Uses HB estimator (partial pooling) for confusion matrix, then applies
225	    subgroup-level correction. The key advantage over Stratified MLE is that the
226	    confusion matrix estimate borrows strength across subgroups.
227	
228	    # TODO: integrate HB from exp001 after MCMC fix
229	    Currently falls back to MLE (same as Stratified MLE) until HB is integrated.
230	    """
231	    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']
232	    s_mask = S == s_val
233	
234	    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))
235	    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))
236	    if np.isnan(th0) or np.isnan(th1):
237	        return np.nan, np.nan, np.nan, np.nan
238	
239	    M_s = build_mixing_matrix(C_s_hb, p_z_s, p_zh_s)
240	    tau_corr, se_corr = invert_mixing(M_s, np.array([th0, th1]), np.array([se0, se1]))
241	    return tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]
242	
243	
244	def method_mi_rubin(data, s_val, M=20, seed=0):
245	    """Multiple Imputation with Rubin's rules (formerly called PPCI).
246	
247	    For each non-expert observation, impute Z from P(Z|Z_hat, S) estimated
248	    on expert data. Repeat M times, compute CATE on each imputed dataset,
249	    then combine estimates using Rubin's rules.
250	    """
251	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
252	    expert_mask = data['expert_mask']
253	    rng = np.random.RandomState(seed)
254	
255	    s_mask = S == s_val
256	    expert_s = expert_mask & s_mask
257	
258	    if expert_s.sum() < 4:
259	        return np.nan, np.nan, np.nan, np.nan
260	
261	    p_z1_given_zhat = {}
262	    for z_hat_val in [0, 1]:
263	        expert_zhat = expert_s & (Z_hat == z_hat_val)
264	        if expert_zhat.sum() > 0:
265	            p_z1_given_zhat[z_hat_val] = np.clip(Z[expert_zhat].mean(), 0.01, 0.99)
266	        else:
267	            p_z1_given_zhat[z_hat_val] = float(z_hat_val)
268	
269	    Y_s = Y[s_mask]
270	    T_s = T[s_mask]
271	    Z_hat_s = Z_hat[s_mask]
272	    is_expert_s = expert_mask[s_mask]
273	    Z_true_s = Z[s_mask]
274	    non_expert_s = ~is_expert_s
275	
276	    tau_z0_list, tau_z1_list = [], []
277	    var_z0_list, var_z1_list = [], []
278	
279	    for m_iter in range(M):
280	        Z_imp = Z_hat_s.copy().astype(float)
281	        Z_imp[is_expert_s] = Z_true_s[is_expert_s]
282	        if non_expert_s.any():
283	            probs = np.array([p_z1_given_zhat[zh] for zh in Z_hat_s[non_expert_s]])
284	            Z_imp[non_expert_s] = rng.binomial(1, probs).astype(float)
285	
286	        for z_val, tau_list, var_list in [(0, tau_z0_list, var_z0_list),
287	                                          (1, tau_z1_list, var_z1_list)]:
288	            z_mask = Z_imp == z_val
289	            t1 = z_mask & (T_s == 1)
290	            t0 = z_mask & (T_s == 0)
291	            n1, n0 = t1.sum(), t0.sum()
292	            if n1 < 2 or n0 < 2:
293	                tau_list.append(np.nan)
294	                var_list.append(np.nan)
295	            else:
296	                y1, y0 = Y_s[t1], Y_s[t0]
297	                tau_hat = y1.mean() - y0.mean()
298	                v = y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0
299	                tau_list.append(tau_hat)
300	                var_list.append(v)
301	
302	    def rubins_combine(tau_list, var_list):
303	        valid = [(t, v) for t, v in zip(tau_list, var_list)
304	                 if not np.isnan(t) and not np.isnan(v)]
305	        if len(valid) < 2:
306	            return np.nan, np.nan
307	        taus = np.array([t for t, v in valid])
308	        vars_ = np.array([v for t, v in valid])
309	        m_eff = len(valid)
310	        tau_bar = taus.mean()
311	        W = vars_.mean()
312	        B = taus.var(ddof=1)
313	        V_total = W + (1 + 1.0 / m_eff) * B
314	        return tau_bar, np.sqrt(max(V_total, 0))
315	
316	    th0, se0 = rubins_combine(tau_z0_list, var_z0_list)
317	    th1, se1 = rubins_combine(tau_z1_list, var_z1_list)
318	    return th0, th1, se0, se1
319	
320	
321	def method_ppci(data, s_val):
322	    """PPI rectifier for CATE estimation.
323	
324	    Corrects outcome-side bias using a gold-standard expert subset.
325	    Gold subset has access to BOTH true Z and true Y (Y_true).
326	    For each subgroup s and Z-level z:
327	      1. tau_hat_all(z,s) = CATE from ALL data using Z_hat and observed Y
328	      2. tau_gold(z,s) = CATE from GOLD subset using true Z and true Y
329	      3. tau_hat_gold(z,s) = CATE from GOLD subset using Z_hat and observed Y
330	      4. rectifier = tau_gold - tau_hat_gold
331	      5. tau_ppci = tau_hat_all + rectifier
332	    """
333	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
334	    Y_true = data['Y_true']
335	    expert_mask = data['expert_mask']
336	
337	    s_mask = S == s_val
338	    expert_s = expert_mask & s_mask
339	    n_expert_s = expert_s.sum()
340	
341	    if n_expert_s < 10:
342	        th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))
343	        th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))
344	        return th0, th1, se0, se1
345	
346	    expert_s_indices = np.where(expert_s)[0]
347	    Z_true_s = Z[expert_s_indices]
348	
349	    results_z = {}
350	    for z_val in [0, 1]:
351	        all_mask = s_mask & (Z_hat == z_val)
352	        tau_hat_all, se_hat_all = diff_in_means(Y, T, all_mask)
353	
354	        gold_mask_z = (Z_true_s == z_val)
355	        gold_indices = expert_s_indices[gold_mask_z]
356	
357	        if len(gold_indices) < 4:
358	            results_z[z_val] = (tau_hat_all, se_hat_all)
359	            continue
360	
361	        # tau_gold: use true Z and true Y on gold subset
362	        gold_bool = np.zeros(len(Y), dtype=bool)
363	        gold_bool[gold_indices] = True
364	        tau_gold, se_gold = diff_in_means(Y_true, T, gold_bool)
365	
366	        # tau_hat_gold: use Z_hat and observed Y on gold subset (same people)
367	        gold_zhat_mask = (Z_hat[expert_s_indices] == z_val)
368	        gold_zhat_indices = expert_s_indices[gold_zhat_mask]
369	        gold_zhat_bool = np.zeros(len(Y), dtype=bool)
370	        gold_zhat_bool[gold_zhat_indices] = True
371	        tau_hat_gold, se_hat_gold = diff_in_means(Y, T, gold_zhat_bool)
372	
373	        if np.isnan(tau_gold) or np.isnan(tau_hat_gold) or np.isnan(tau_hat_all):
374	            results_z[z_val] = (tau_hat_all, se_hat_all)
375	            continue
376	
377	        rectifier = tau_gold - tau_hat_gold
378	        tau_ppci = tau_hat_all + rectifier
379	        se_ppci = np.sqrt(se_hat_all**2 + se_gold**2 + se_hat_gold**2)
380	        results_z[z_val] = (tau_ppci, se_ppci)
381	
382	    th0, se0 = results_z.get(0, (np.nan, np.nan))
383	    th1, se1 = results_z.get(1, (np.nan, np.nan))
384	    return th0, th1, se0, se1
385	
386	
387	def method_ec_hte_ppci(data, s_val, C_s, p_z_s, p_zh_s):
388	    """EC-HTE + PPCI: correct covariate error via M^{-1}, then apply PPI rectifier for outcome error."""
389	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
390	    Y_true = data['Y_true']
391	    expert_mask = data['expert_mask']
392	
393	    s_mask = S == s_val
394	    expert_s = expert_mask & s_mask
395	
396	    th0_obs, se0_obs = diff_in_means(Y, T, s_mask & (Z_hat == 0))
397	    th1_obs, se1_obs = diff_in_means(Y, T, s_mask & (Z_hat == 1))
398	    if np.isnan(th0_obs) or np.isnan(th1_obs):
399	        return np.nan, np.nan, np.nan, np.nan
400	
401	    M_s = build_mixing_matrix(C_s, p_z_s, p_zh_s)
402	    tau_ec, se_ec = invert_mixing(M_s, np.array([th0_obs, th1_obs]),
403	                                  np.array([se0_obs, se1_obs]))
404	
405	    n_expert_s = expert_s.sum()
406	    if n_expert_s < 10:
407	        return tau_ec[0], tau_ec[1], se_ec[0], se_ec[1]
408	
409	    expert_s_indices = np.where(expert_s)[0]
410	    Z_true_s = Z[expert_s_indices]
411	
412	    results_z = {}
413	    for idx, z_val in enumerate([0, 1]):
414	        gold_z_mask = (Z_true_s == z_val)
415	        gold_indices = expert_s_indices[gold_z_mask]
416	
417	        if len(gold_indices) < 4:
418	            results_z[z_val] = (tau_ec[idx], se_ec[idx])
419	            continue
420	
421	        # tau_gold: true Z + true Y on gold subset
422	        gold_bool = np.zeros(len(Y), dtype=bool)
423	        gold_bool[gold_indices] = True
424	        tau_gold, se_gold = diff_in_means(Y_true, T, gold_bool)
425	
426	        # tau_hat_gold: Z_hat + observed Y on gold subset
427	        gold_zhat_mask = (Z_hat[expert_s_indices] == z_val)
428	        gold_zhat_indices = expert_s_indices[gold_zhat_mask]
429	        gold_zhat_bool = np.zeros(len(Y), dtype=bool)
430	        gold_zhat_bool[gold_zhat_indices] = True
431	        tau_hat_gold, se_hat_gold = diff_in_means(Y, T, gold_zhat_bool)
432	
433	        if np.isnan(tau_gold) or np.isnan(tau_hat_gold):
434	            results_z[z_val] = (tau_ec[idx], se_ec[idx])
435	            continue
436	
437	        rectifier = tau_gold - tau_hat_gold
438	        tau_combined = tau_ec[idx] + rectifier
439	        se_combined = np.sqrt(se_ec[idx]**2 + se_gold**2 + se_hat_gold**2)
440	        results_z[z_val] = (tau_combined, se_combined)
441	
442	    th0, se0 = results_z.get(0, (np.nan, np.nan))
443	    th1, se1 = results_z.get(1, (np.nan, np.nan))
444	    return th0, th1, se0, se1
445	
446	
447	# === Main Simulation Loop ===
448	
449	def run_one_mc(regime_name, regime_params, misclass_rates, n_expert, k_subgroups, seed,
450	               sigma_outcome=0.0, dgp_name='A_covariate_only', dgp_cfg=None,
451	               outcome_bias_per_subgroup=None):
452	    """Run one MC iteration for all methods."""
453	    if dgp_cfg is None:
454	        dgp_cfg = DGP_CONFIGS[dgp_name]
455	
456	    data = generate_data(regime_params, misclass_rates, n_expert, k_subgroups, seed,
457	                         sigma_outcome=sigma_outcome,
458	                         has_covariate_error=dgp_cfg['has_covariate_error'],
459	                         has_outcome_error=dgp_cfg['has_outcome_error'],
460	                         outcome_bias_per_subgroup=outcome_bias_per_subgroup)
461	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
462	    expert_mask = data['expert_mask']
463	    tau_true_z0, tau_true_z1 = regime_params['tau_z0'], regime_params['tau_z1']
464	
465	    C_global = estimate_cm_mle(Z[expert_mask], Z_hat[expert_mask])
466	    p_z_global = np.clip(np.array([(Z[expert_mask]==0).mean(), (Z[expert_mask]==1).mean()]), 0.01, 0.99)
467	    p_zh_global = np.clip(np.array([(Z_hat==0).mean(), (Z_hat==1).mean()]), 0.01, 0.99)
468	
469	    C_mle = {}
470	    C_hb = {}
471	    all_subgroup_expert_data = []
472	
473	    for s in range(k_subgroups):
474	        s_mask = S == s
475	        expert_s = expert_mask & s_mask
476	        if expert_s.sum() >= 4:
477	            C_mle[s] = estimate_cm_mle(Z[expert_s], Z_hat[expert_s])
478	            all_subgroup_expert_data.append((Z[expert_s], Z_hat[expert_s]))
479	        else:
480	            C_mle[s] = C_global
481	            all_subgroup_expert_data.append((Z[expert_mask], Z_hat[expert_mask]))
482	
483	    for s in range(k_subgroups):
484	        s_mask = S == s
485	        expert_s = expert_mask & s_mask
486	        if expert_s.sum() >= 4:
487	            C_hb[s] = estimate_cm_hb(Z[expert_s], Z_hat[expert_s], all_subgroup_expert_data)
488	        else:
489	            C_hb[s] = C_global
490	
491	    rows = []
492	    base = {
493	        'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k_subgroups,
494	        'sigma_outcome': sigma_outcome, 'dgp': dgp_name,
495	        'mc_run': seed, 'tau_true_z0': tau_true_z0, 'tau_true_z1': tau_true_z1,
496	    }
497	
498	    def make_row(method, subgroup, th0, th1, se0, se1):
499	        return {**base, 'method': method, 'subgroup': subgroup,
500	                'tau_hat_z0': th0, 'tau_hat_z1': th1,
501	                'ci_lower_z0': th0 - 1.96*se0 if not np.isnan(se0) else np.nan,
502	                'ci_upper_z0': th0 + 1.96*se0 if not np.isnan(se0) else np.nan,
503	                'ci_lower_z1': th1 - 1.96*se1 if not np.isnan(se1) else np.nan,
504	                'ci_upper_z1': th1 + 1.96*se1 if not np.isnan(se1) else np.nan}
505	
506	    for s in range(k_subgroups):
507	        s_mask = S == s
508	        expert_s = expert_mask & s_mask
509	        if expert_s.sum() >= 4:
510	            p_z_s = np.clip(np.array([(Z[expert_s]==0).mean(), (Z[expert_s]==1).mean()]), 0.01, 0.99)
511	        else:
512	            p_z_s = p_z_global
513	        p_zh_s = np.clip(np.array([(Z_hat[s_mask]==0).mean(), (Z_hat[s_mask]==1).mean()]), 0.01, 0.99)
514	
515	        th0, th1, se0, se1 = method_oracle(data, s)
516	        rows.append(make_row('oracle', s, th0, th1, se0, se1))
517	
518	        th0, th1, se0, se1 = method_naive(data, s)
519	        rows.append(make_row('naive', s, th0, th1, se0, se1))
520	
521	        th0, th1, se0, se1 = method_global_corrected(data, s, C_global, p_z_global, p_zh_global)
522	        rows.append(make_row('global_corrected', s, th0, th1, se0, se1))
523	
524	        th0, th1, se0, se1 = method_stratified_mle(data, s, C_mle[s], p_z_s, p_zh_s)
525	        rows.append(make_row('stratified_mle', s, th0, th1, se0, se1))
526	
527	        th0, th1, se0, se1 = method_ec_hte(data, s, C_hb[s], p_z_s, p_zh_s)
528	        rows.append(make_row('ec_hte', s, th0, th1, se0, se1))
529	
530	        th0, th1, se0, se1 = method_mi_rubin(data, s, M=20, seed=seed * 1000 + s)
531	        rows.append(make_row('mi_rubin', s, th0, th1, se0, se1))
532	
533	        th0, th1, se0, se1 = method_ppci(data, s)
534	        rows.append(make_row('ppci', s, th0, th1, se0, se1))
535	
536	        th0, th1, se0, se1 = method_ec_hte_ppci(data, s, C_hb[s], p_z_s, p_zh_s)
537	        rows.append(make_row('ec_hte_ppci', s, th0, th1, se0, se1))
538	
539	    return rows
540	
541	
542	def aggregate_results(df):
543	    """Aggregate per-run results into summary statistics."""
544	    rows = []
545	    group_cols = ['regime', 'n_expert', 'k_subgroups', 'sigma_outcome', 'dgp', 'subgroup', 'method']
546	    for keys, grp in df.groupby(group_cols):
547	        row = dict(zip(group_cols, keys))
548	        for z in ['z0', 'z1']:
549	            err = grp[f'tau_hat_{z}'] - grp[f'tau_true_{z}']
550	            valid = err.dropna()
551	            if len(valid) == 0:
552	                row.update({f'bias_{z}': np.nan, f'rmse_{z}': np.nan, f'coverage_{z}': np.nan})
553	                continue
554	            row[f'bias_{z}'] = valid.mean()
555	            row[f'rmse_{z}'] = np.sqrt((valid**2).mean())
556	            covered = ((grp[f'ci_lower_{z}'] <= grp[f'tau_true_{z}']) &
557	                       (grp[f'tau_true_{z}'] <= grp[f'ci_upper_{z}'])).mean()
558	            row[f'coverage_{z}'] = covered
559	            row[f'bias_{z}_se'] = valid.std() / np.sqrt(len(valid))
560	        rows.append(row)
561	    return pd.DataFrame(rows)
562	
563	
564	def run_simulation(n_mc, k_list=[2, 4], sigma_list=None, dgp_list=None, verbose=True):
565	    """Run full simulation sweep over DGP configs."""
566	    if sigma_list is None:
567	        sigma_list = OUTCOME_NOISE_LEVELS
568	    if dgp_list is None:
569	        dgp_list = list(DGP_CONFIGS.keys())
570	    results = []
571	    configs = []
572	    for regime_name in REGIMES:
573	        for k in k_list:
574	            misclass = MISCLASS_K2[regime_name] if k == 2 else MISCLASS_K4[regime_name]
575	            for ne in N_EXPERTS:
576	                for sigma in sigma_list:
577	                    for dgp_name in dgp_list:
578	                        configs.append((regime_name, k, misclass, ne, sigma, dgp_name))
579	
580	    total = len(configs) * n_mc
581	    count = 0
582	    t0 = time.time()
583	
584	    for regime_name, k, misclass, ne, sigma, dgp_name in configs:
585	        dgp_cfg = DGP_CONFIGS[dgp_name]
586	        outcome_bias = OUTCOME_BIAS[regime_name]
587	        if k == 2:
588	            outcome_bias_k = outcome_bias[:2]
589	        else:
590	            outcome_bias_k = outcome_bias[:k]
591	
592	        for mc in range(n_mc):
593	            rows = run_one_mc(regime_name, REGIMES[regime_name], misclass, ne, k, seed=mc,
594	                              sigma_outcome=sigma, dgp_name=dgp_name, dgp_cfg=dgp_cfg,
595	                              outcome_bias_per_subgroup=outcome_bias_k)
596	            results.extend(rows)
597	            count += 1
598	            if verbose and count % max(1, total // 20) == 0:
599	                elapsed = time.time() - t0
600	                eta = elapsed / count * (total - count)
601	                print(f"  [{count}/{total}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s | {dgp_name} k={k} {regime_name} ne={ne} sigma={sigma} mc={mc}")
602	
603	    return pd.DataFrame(results), time.time() - t0
604	
605	
606	if __name__ == '__main__':
607	    dry_run = '--dry-run' in sys.argv
608	    args = [a for a in sys.argv[1:] if a != '--dry-run']
609	    n_mc = int(args[0]) if args else N_MC
610	
611	    if dry_run:
612	        n_mc = 1
613	        sigma_list = [0.5]
614	        k_list = [2]
615	        dgp_list = list(DGP_CONFIGS.keys())
616	    else:
617	        sigma_list = None
618	        k_list = [2, 4]
619	        dgp_list = None
620	
621	    methods_str = 'oracle, naive, global_corrected, stratified_mle, ec_hte, mi_rubin, ppci, ec_hte_ppci'
622	    print(f"exp-007: PPCI + EC-HTE 4-DGP Matrix")
623	    print(f"N={N}, N_MC={n_mc}")
624	    print(f"Methods: {methods_str}")
625	    print(f"DGPs: {dgp_list if dgp_list else list(DGP_CONFIGS.keys())}")
626	    print(f"Outcome noise levels: {sigma_list if sigma_list else OUTCOME_NOISE_LEVELS}")
627	    print(f"Note: ec_hte currently uses MLE fallback (HB placeholder)")
628	    if dry_run:
629	        print(f"** DRY RUN: 1 MC, k=[2], sigma=[0.5], all 4 DGPs **")
630	    print()
631	
632	    df_raw, elapsed = run_simulation(n_mc, k_list=k_list, sigma_list=sigma_list,
633	                                     dgp_list=dgp_list)
634	    df_agg = aggregate_results(df_raw)
635	
636	    raw_path = 'results/exp007_ppci_dsl_raw.csv'
637	    agg_path = 'results/exp007_ppci_dsl.csv'
638	    df_raw.to_csv(raw_path, index=False)
639	    df_agg.to_csv(agg_path, index=False)
640	
641	    print(f"\nTotal time: {elapsed:.1f}s")
642	    print(f"Saved: {raw_path}, {agg_path}")
643	
644	    pd.set_option('display.max_columns', 20)
645	    pd.set_option('display.width', 240)
646	    pd.set_option('display.float_format', '{:.4f}'.format)
647	
648	    for dgp in (dgp_list or list(DGP_CONFIGS.keys())):
649	        for regime in REGIMES:
650	            print(f"\n{'='*140}")
651	            print(f"DGP: {dgp} | Regime: {regime}")
652	            print(f"{'='*140}")
653	            sub = df_agg[(df_agg['regime'] == regime) & (df_agg['dgp'] == dgp)]
654	            if sub.empty:
655	                continue
656	            cols = ['n_expert', 'k_subgroups', 'sigma_outcome', 'subgroup', 'method',
657	                    'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1']
658	            print(sub[cols].to_string(index=False))
659	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "c933f00c-f922-4b7a-a9f2-6f7da3d7b1e3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py",
      "content": "\"\"\"\nexp-007: PPCI + Stratified MLE Baseline Comparison for EC-HTE\nCompares measurement-model-level correction (EC-HTE) vs estimand-level correction (Stratified MLE)\nvs standard PPCI approach. DGP uses pure covariate-error: only Z has LLM misclassification.\nOutcome Y can optionally have measurement error (sigma_outcome > 0).\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nimport sys\nimport time\nimport warnings\nwarnings.filterwarnings('ignore')\n\n# === DGP ===\n\nREGIMES = {\n    'extreme':     {'tau_z1': 0.5, 'tau_z0': 0.1},\n    'moderate':    {'tau_z1': 0.3, 'tau_z0': 0.15},\n    'homogeneous': {'tau_z1': 0.25, 'tau_z0': 0.20},\n}\n\nMISCLASS_K2 = {\n    'extreme':     [0.25, 0.05],\n    'moderate':    [0.15, 0.10],\n    'homogeneous': [0.12, 0.12],\n}\n\nMISCLASS_K4 = {\n    'extreme':     [0.30, 0.20, 0.10, 0.03],\n    'moderate':    [0.20, 0.15, 0.10, 0.05],\n    'homogeneous': [0.12, 0.12, 0.12, 0.12],\n}\n\nOUTCOME_BIAS = {\n    'extreme':     [0.3, 0.1, 0.5, 0.2],\n    'moderate':    [0.15, 0.05, 0.25, 0.10],\n    'homogeneous': [0.1, 0.1, 0.1, 0.1],\n}\n\nDGP_CONFIGS = {\n    'A_covariate_only':  {'has_covariate_error': True,  'has_outcome_error': False},\n    'B_outcome_only':    {'has_covariate_error': False, 'has_outcome_error': True},\n    'C_both_errors':     {'has_covariate_error': True,  'has_outcome_error': True},\n    'D_no_error':        {'has_covariate_error': False, 'has_outcome_error': False},\n}\n\nN = 5000\nN_EXPERTS = [50, 100, 250, 500]\nN_MC = 100\nOUTCOME_NOISE_LEVELS = [0.0, 0.5, 1.0]\n\n\ndef generate_data(regime_params, misclass_rates, n_expert, k_subgroups, seed,\n                  sigma_outcome=0.0, outcome_noise_heterogeneous=True,\n                  has_covariate_error=True, has_outcome_error=False,\n                  outcome_bias_per_subgroup=None):\n    \"\"\"Generate synthetic data with configurable covariate and outcome error.\n\n    DGP A (covariate only): Z_hat has misclassification, Y = Y_true\n    DGP B (outcome only): Z_hat = Z, Y has treatment-differential bias\n    DGP C (both): Z_hat has misclassification AND Y has bias\n    DGP D (no error): Z_hat = Z, Y = Y_true\n    \"\"\"\n    rng = np.random.RandomState(seed)\n    k = k_subgroups\n\n    T = rng.binomial(1, 0.5, N)\n    Z = rng.binomial(1, 0.5, N)\n    S = rng.choice(k, N, p=[1/k]*k)\n    X = rng.randn(N, 5)\n\n    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])\n    eps = rng.randn(N)\n    Y_true = 1 + tau * T + 0.5 * X[:, 0] + eps\n    Y = Y_true.copy()\n\n    if has_outcome_error:\n        if outcome_bias_per_subgroup is not None:\n            for i in range(k):\n                s_mask = (S == i)\n                bias_i = outcome_bias_per_subgroup[i] if i < len(outcome_bias_per_subgroup) else outcome_bias_per_subgroup[-1]\n                Y[s_mask] += bias_i * T[s_mask]\n        if sigma_outcome > 0:\n            for i in range(k):\n                s_mask = (S == i)\n                noise_scale = sigma_outcome * (1 + 0.5 * i / max(k - 1, 1))\n                Y[s_mask] += rng.normal(0, noise_scale, s_mask.sum())\n\n    if has_covariate_error:\n        mc_rates = np.array([misclass_rates[s] for s in S])\n        flip = rng.rand(N) < mc_rates\n        Z_hat = np.where(flip, 1 - Z, Z)\n    else:\n        Z_hat = Z.copy()\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'X': X, 'Y': Y,\n        'Y_true': Y_true, 'tau': tau, 'expert_mask': expert_mask,\n    }\n\n\n# === Confusion Matrix Estimators ===\n\ndef estimate_cm_mle(z_true, z_hat):\n    \"\"\"MLE confusion matrix with Laplace smoothing. C[z, z_hat] = P(Z_hat=z_hat | Z=z).\"\"\"\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (mask.sum() + 2)\n    return C\n\n\ndef estimate_cm_hb(z_true, z_hat, all_subgroup_data):\n    \"\"\"Hierarchical Bayesian confusion matrix estimator (placeholder).\n\n    # TODO: integrate HB from exp001 after MCMC fix\n    Uses Dirichlet-Multinomial hierarchical model with partial pooling across subgroups.\n    \"\"\"\n    return estimate_cm_mle(z_true, z_hat)\n\n\n# === Correction Methods ===\n\ndef diff_in_means(Y, T, mask):\n    \"\"\"Difference-in-means estimator for subpopulation defined by mask.\"\"\"\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    \"\"\"M[z_hat, z] = P(Z=z | Z_hat=z_hat) via Bayes' rule.\"\"\"\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh]\n    return M\n\n\ndef invert_mixing(M, tau_obs, se_obs):\n    \"\"\"Apply M^{-1} correction. Returns (tau_corrected, se_corrected).\"\"\"\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    M_inv = np.linalg.inv(M)\n    tau_corrected = M_inv @ tau_obs\n    sigma_obs = np.diag(se_obs ** 2)\n    sigma_corrected = M_inv @ sigma_obs @ M_inv.T\n    se_corrected = np.sqrt(np.diag(sigma_corrected))\n    return tau_corrected, se_corrected\n\n\ndef method_oracle(data, s_val):\n    \"\"\"Oracle: use true Z within subgroup s.\"\"\"\n    Y, T, Z, S = data['Y'], data['T'], data['Z'], data['S']\n    s_mask = S == s_val\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z == 1))\n    return th0, th1, se0, se1\n\n\ndef method_naive(data, s_val):\n    \"\"\"Naive: use Z_hat within subgroup s, no correction.\"\"\"\n    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']\n    s_mask = S == s_val\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    return th0, th1, se0, se1\n\n\ndef method_global_corrected(data, s_val, C_global, p_z_global, p_zh_global):\n    \"\"\"Global-corrected: use global M_global^{-1} on subgroup-level observed CATEs.\"\"\"\n    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']\n    s_mask = S == s_val\n\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    if np.isnan(th0) or np.isnan(th1):\n        return np.nan, np.nan, np.nan, np.nan\n\n    M = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n    tau_corr, se_corr = invert_mixing(M, np.array([th0, th1]), np.array([se0, se1]))\n    return tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]\n\n\ndef method_stratified_mle(data, s_val, C_s, p_z_s, p_zh_s):\n    \"\"\"Stratified MLE: per-subgroup independent correction.\n\n    Each subgroup estimates its own confusion matrix independently (no pooling).\n    This is estimand-level correction -- correct the CATE estimate directly\n    using the subgroup's own confusion matrix.\n\n    Key difference from EC-HTE: no cross-subgroup shrinkage.\n    When n_expert is small per subgroup, Stratified MLE has high variance.\n    \"\"\"\n    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']\n    s_mask = S == s_val\n\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    if np.isnan(th0) or np.isnan(th1):\n        return np.nan, np.nan, np.nan, np.nan\n\n    M_s = build_mixing_matrix(C_s, p_z_s, p_zh_s)\n    tau_corr, se_corr = invert_mixing(M_s, np.array([th0, th1]), np.array([se0, se1]))\n    return tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]\n\n\ndef method_ec_hte(data, s_val, C_s_hb, p_z_s, p_zh_s):\n    \"\"\"EC-HTE: hierarchical Bayesian confusion matrix + subgroup correction.\n\n    Uses HB estimator (partial pooling) for confusion matrix, then applies\n    subgroup-level correction. The key advantage over Stratified MLE is that the\n    confusion matrix estimate borrows strength across subgroups.\n\n    # TODO: integrate HB from exp001 after MCMC fix\n    Currently falls back to MLE (same as Stratified MLE) until HB is integrated.\n    \"\"\"\n    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']\n    s_mask = S == s_val\n\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    if np.isnan(th0) or np.isnan(th1):\n        return np.nan, np.nan, np.nan, np.nan\n\n    M_s = build_mixing_matrix(C_s_hb, p_z_s, p_zh_s)\n    tau_corr, se_corr = invert_mixing(M_s, np.array([th0, th1]), np.array([se0, se1]))\n    return tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]\n\n\ndef method_mi_rubin(data, s_val, M=20, seed=0):\n    \"\"\"Multiple Imputation with Rubin's rules (formerly called PPCI).\n\n    For each non-expert observation, impute Z from P(Z|Z_hat, S) estimated\n    on expert data. Repeat M times, compute CATE on each imputed dataset,\n    then combine estimates using Rubin's rules.\n    \"\"\"\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n    rng = np.random.RandomState(seed)\n\n    s_mask = S == s_val\n    expert_s = expert_mask & s_mask\n\n    if expert_s.sum() < 4:\n        return np.nan, np.nan, np.nan, np.nan\n\n    p_z1_given_zhat = {}\n    for z_hat_val in [0, 1]:\n        expert_zhat = expert_s & (Z_hat == z_hat_val)\n        if expert_zhat.sum() > 0:\n            p_z1_given_zhat[z_hat_val] = np.clip(Z[expert_zhat].mean(), 0.01, 0.99)\n        else:\n            p_z1_given_zhat[z_hat_val] = float(z_hat_val)\n\n    Y_s = Y[s_mask]\n    T_s = T[s_mask]\n    Z_hat_s = Z_hat[s_mask]\n    is_expert_s = expert_mask[s_mask]\n    Z_true_s = Z[s_mask]\n    non_expert_s = ~is_expert_s\n\n    tau_z0_list, tau_z1_list = [], []\n    var_z0_list, var_z1_list = [], []\n\n    for m_iter in range(M):\n        Z_imp = Z_hat_s.copy().astype(float)\n        Z_imp[is_expert_s] = Z_true_s[is_expert_s]\n        if non_expert_s.any():\n            probs = np.array([p_z1_given_zhat[zh] for zh in Z_hat_s[non_expert_s]])\n            Z_imp[non_expert_s] = rng.binomial(1, probs).astype(float)\n\n        for z_val, tau_list, var_list in [(0, tau_z0_list, var_z0_list),\n                                          (1, tau_z1_list, var_z1_list)]:\n            z_mask = Z_imp == z_val\n            t1 = z_mask & (T_s == 1)\n            t0 = z_mask & (T_s == 0)\n            n1, n0 = t1.sum(), t0.sum()\n            if n1 < 2 or n0 < 2:\n                tau_list.append(np.nan)\n                var_list.append(np.nan)\n            else:\n                y1, y0 = Y_s[t1], Y_s[t0]\n                tau_hat = y1.mean() - y0.mean()\n                v = y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0\n                tau_list.append(tau_hat)\n                var_list.append(v)\n\n    def rubins_combine(tau_list, var_list):\n        valid = [(t, v) for t, v in zip(tau_list, var_list)\n                 if not np.isnan(t) and not np.isnan(v)]\n        if len(valid) < 2:\n            return np.nan, np.nan\n        taus = np.array([t for t, v in valid])\n        vars_ = np.array([v for t, v in valid])\n        m_eff = len(valid)\n        tau_bar = taus.mean()\n        W = vars_.mean()\n        B = taus.var(ddof=1)\n        V_total = W + (1 + 1.0 / m_eff) * B\n        return tau_bar, np.sqrt(max(V_total, 0))\n\n    th0, se0 = rubins_combine(tau_z0_list, var_z0_list)\n    th1, se1 = rubins_combine(tau_z1_list, var_z1_list)\n    return th0, th1, se0, se1\n\n\ndef method_ppci(data, s_val):\n    \"\"\"PPI rectifier for CATE estimation.\n\n    Corrects outcome-side bias using a gold-standard expert subset.\n    Gold subset has access to BOTH true Z and true Y (Y_true).\n    For each subgroup s and Z-level z:\n      1. tau_hat_all(z,s) = CATE from ALL data using Z_hat and observed Y\n      2. tau_gold(z,s) = CATE from GOLD subset using true Z and true Y\n      3. tau_hat_gold(z,s) = CATE from GOLD subset using Z_hat and observed Y\n      4. rectifier = tau_gold - tau_hat_gold\n      5. tau_ppci = tau_hat_all + rectifier\n    \"\"\"\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    Y_true = data['Y_true']\n    expert_mask = data['expert_mask']\n\n    s_mask = S == s_val\n    expert_s = expert_mask & s_mask\n    n_expert_s = expert_s.sum()\n\n    if n_expert_s < 10:\n        th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n        th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n        return th0, th1, se0, se1\n\n    expert_s_indices = np.where(expert_s)[0]\n    Z_true_s = Z[expert_s_indices]\n\n    results_z = {}\n    for z_val in [0, 1]:\n        all_mask = s_mask & (Z_hat == z_val)\n        tau_hat_all, se_hat_all = diff_in_means(Y, T, all_mask)\n\n        gold_mask_z = (Z_true_s == z_val)\n        gold_indices = expert_s_indices[gold_mask_z]\n\n        if len(gold_indices) < 4:\n            results_z[z_val] = (tau_hat_all, se_hat_all)\n            continue\n\n        # tau_gold: use true Z and true Y on gold subset\n        gold_bool = np.zeros(len(Y), dtype=bool)\n        gold_bool[gold_indices] = True\n        tau_gold, se_gold = diff_in_means(Y_true, T, gold_bool)\n\n        # tau_hat_gold: use Z_hat and observed Y on gold subset (same people)\n        gold_zhat_mask = (Z_hat[expert_s_indices] == z_val)\n        gold_zhat_indices = expert_s_indices[gold_zhat_mask]\n        gold_zhat_bool = np.zeros(len(Y), dtype=bool)\n        gold_zhat_bool[gold_zhat_indices] = True\n        tau_hat_gold, se_hat_gold = diff_in_means(Y, T, gold_zhat_bool)\n\n        if np.isnan(tau_gold) or np.isnan(tau_hat_gold) or np.isnan(tau_hat_all):\n            results_z[z_val] = (tau_hat_all, se_hat_all)\n            continue\n\n        rectifier = tau_gold - tau_hat_gold\n        tau_ppci = tau_hat_all + rectifier\n        se_ppci = np.sqrt(se_hat_all**2 + se_gold**2 + se_hat_gold**2)\n        results_z[z_val] = (tau_ppci, se_ppci)\n\n    th0, se0 = results_z.get(0, (np.nan, np.nan))\n    th1, se1 = results_z.get(1, (np.nan, np.nan))\n    return th0, th1, se0, se1\n\n\ndef method_ec_hte_ppci(data, s_val, C_s, p_z_s, p_zh_s):\n    \"\"\"EC-HTE + PPCI: correct covariate error via M^{-1}, then apply PPI rectifier for outcome error.\"\"\"\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    Y_true = data['Y_true']\n    expert_mask = data['expert_mask']\n\n    s_mask = S == s_val\n    expert_s = expert_mask & s_mask\n\n    th0_obs, se0_obs = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1_obs, se1_obs = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    if np.isnan(th0_obs) or np.isnan(th1_obs):\n        return np.nan, np.nan, np.nan, np.nan\n\n    M_s = build_mixing_matrix(C_s, p_z_s, p_zh_s)\n    tau_ec, se_ec = invert_mixing(M_s, np.array([th0_obs, th1_obs]),\n                                  np.array([se0_obs, se1_obs]))\n\n    n_expert_s = expert_s.sum()\n    if n_expert_s < 10:\n        return tau_ec[0], tau_ec[1], se_ec[0], se_ec[1]\n\n    expert_s_indices = np.where(expert_s)[0]\n    Z_true_s = Z[expert_s_indices]\n\n    results_z = {}\n    for idx, z_val in enumerate([0, 1]):\n        gold_z_mask = (Z_true_s == z_val)\n        gold_indices = expert_s_indices[gold_z_mask]\n\n        if len(gold_indices) < 4:\n            results_z[z_val] = (tau_ec[idx], se_ec[idx])\n            continue\n\n        # tau_gold: true Z + true Y on gold subset\n        gold_bool = np.zeros(len(Y), dtype=bool)\n        gold_bool[gold_indices] = True\n        tau_gold, se_gold = diff_in_means(Y_true, T, gold_bool)\n\n        # tau_hat_gold: Z_hat + observed Y on gold subset\n        gold_zhat_mask = (Z_hat[expert_s_indices] == z_val)\n        gold_zhat_indices = expert_s_indices[gold_zhat_mask]\n        gold_zhat_bool = np.zeros(len(Y), dtype=bool)\n        gold_zhat_bool[gold_zhat_indices] = True\n        tau_hat_gold, se_hat_gold = diff_in_means(Y, T, gold_zhat_bool)\n\n        if np.isnan(tau_gold) or np.isnan(tau_hat_gold):\n            results_z[z_val] = (tau_ec[idx], se_ec[idx])\n            continue\n\n        rectifier = tau_gold - tau_hat_gold\n        tau_combined = tau_ec[idx] + rectifier\n        se_combined = np.sqrt(se_ec[idx]**2 + se_gold**2 + se_hat_gold**2)\n        results_z[z_val] = (tau_combined, se_combined)\n\n    th0, se0 = results_z.get(0, (np.nan, np.nan))\n    th1, se1 = results_z.get(1, (np.nan, np.nan))\n    return th0, th1, se0, se1\n\n\n# === Main Simulation Loop ===\n\ndef run_one_mc(regime_name, regime_params, misclass_rates, n_expert, k_subgroups, seed,\n               sigma_outcome=0.0, dgp_name='A_covariate_only', dgp_cfg=None,\n               outcome_bias_per_subgroup=None):\n    \"\"\"Run one MC iteration for all methods.\"\"\"\n    if dgp_cfg is None:\n        dgp_cfg = DGP_CONFIGS[dgp_name]\n\n    data = generate_data(regime_params, misclass_rates, n_expert, k_subgroups, seed,\n                         sigma_outcome=sigma_outcome,\n                         has_covariate_error=dgp_cfg['has_covariate_error'],\n                         has_outcome_error=dgp_cfg['has_outcome_error'],\n                         outcome_bias_per_subgroup=outcome_bias_per_subgroup)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n    tau_true_z0, tau_true_z1 = regime_params['tau_z0'], regime_params['tau_z1']\n\n    C_global = estimate_cm_mle(Z[expert_mask], Z_hat[expert_mask])\n    p_z_global = np.clip(np.array([(Z[expert_mask]==0).mean(), (Z[expert_mask]==1).mean()]), 0.01, 0.99)\n    p_zh_global = np.clip(np.array([(Z_hat==0).mean(), (Z_hat==1).mean()]), 0.01, 0.99)\n\n    C_mle = {}\n    C_hb = {}\n    all_subgroup_expert_data = []\n\n    for s in range(k_subgroups):\n        s_mask = S == s\n        expert_s = expert_mask & s_mask\n        if expert_s.sum() >= 4:\n            C_mle[s] = estimate_cm_mle(Z[expert_s], Z_hat[expert_s])\n            all_subgroup_expert_data.append((Z[expert_s], Z_hat[expert_s]))\n        else:\n            C_mle[s] = C_global\n            all_subgroup_expert_data.append((Z[expert_mask], Z_hat[expert_mask]))\n\n    for s in range(k_subgroups):\n        s_mask = S == s\n        expert_s = expert_mask & s_mask\n        if expert_s.sum() >= 4:\n            C_hb[s] = estimate_cm_hb(Z[expert_s], Z_hat[expert_s], all_subgroup_expert_data)\n        else:\n            C_hb[s] = C_global\n\n    rows = []\n    base = {\n        'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k_subgroups,\n        'sigma_outcome': sigma_outcome, 'dgp': dgp_name,\n        'mc_run': seed, 'tau_true_z0': tau_true_z0, 'tau_true_z1': tau_true_z1,\n    }\n\n    def make_row(method, subgroup, th0, th1, se0, se1):\n        return {**base, 'method': method, 'subgroup': subgroup,\n                'tau_hat_z0': th0, 'tau_hat_z1': th1,\n                'ci_lower_z0': th0 - 1.96*se0 if not np.isnan(se0) else np.nan,\n                'ci_upper_z0': th0 + 1.96*se0 if not np.isnan(se0) else np.nan,\n                'ci_lower_z1': th1 - 1.96*se1 if not np.isnan(se1) else np.nan,\n                'ci_upper_z1': th1 + 1.96*se1 if not np.isnan(se1) else np.nan}\n\n    for s in range(k_subgroups):\n        s_mask = S == s\n        expert_s = expert_mask & s_mask\n        if expert_s.sum() >= 4:\n            p_z_s = np.clip(np.array([(Z[expert_s]==0).mean(), (Z[expert_s]==1).mean()]), 0.01, 0.99)\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.clip(np.array([(Z_hat[s_mask]==0).mean(), (Z_hat[s_mask]==1).mean()]), 0.01, 0.99)\n\n        th0, th1, se0, se1 = method_oracle(data, s)\n        rows.append(make_row('oracle', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_naive(data, s)\n        rows.append(make_row('naive', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_global_corrected(data, s, C_global, p_z_global, p_zh_global)\n        rows.append(make_row('global_corrected', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_stratified_mle(data, s, C_mle[s], p_z_s, p_zh_s)\n        rows.append(make_row('stratified_mle', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_ec_hte(data, s, C_hb[s], p_z_s, p_zh_s)\n        rows.append(make_row('ec_hte', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_mi_rubin(data, s, M=20, seed=seed * 1000 + s)\n        rows.append(make_row('mi_rubin', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_ppci(data, s)\n        rows.append(make_row('ppci', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_ec_hte_ppci(data, s, C_hb[s], p_z_s, p_zh_s)\n        rows.append(make_row('ec_hte_ppci', s, th0, th1, se0, se1))\n\n    return rows\n\n\ndef aggregate_results(df):\n    \"\"\"Aggregate per-run results into summary statistics.\"\"\"\n    rows = []\n    group_cols = ['regime', 'n_expert', 'k_subgroups', 'sigma_outcome', 'dgp', 'subgroup', 'method']\n    for keys, grp in df.groupby(group_cols):\n        row = dict(zip(group_cols, keys))\n        for z in ['z0', 'z1']:\n            err = grp[f'tau_hat_{z}'] - grp[f'tau_true_{z}']\n            valid = err.dropna()\n            if len(valid) == 0:\n                row.update({f'bias_{z}': np.nan, f'rmse_{z}': np.nan, f'coverage_{z}': np.nan})\n                continue\n            row[f'bias_{z}'] = valid.mean()\n            row[f'rmse_{z}'] = np.sqrt((valid**2).mean())\n            covered = ((grp[f'ci_lower_{z}'] <= grp[f'tau_true_{z}']) &\n                       (grp[f'tau_true_{z}'] <= grp[f'ci_upper_{z}'])).mean()\n            row[f'coverage_{z}'] = covered\n            row[f'bias_{z}_se'] = valid.std() / np.sqrt(len(valid))\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\ndef run_simulation(n_mc, k_list=[2, 4], sigma_list=None, dgp_list=None, verbose=True):\n    \"\"\"Run full simulation sweep over DGP configs.\"\"\"\n    if sigma_list is None:\n        sigma_list = OUTCOME_NOISE_LEVELS\n    if dgp_list is None:\n        dgp_list = list(DGP_CONFIGS.keys())\n    results = []\n    configs = []\n    for regime_name in REGIMES:\n        for k in k_list:\n            misclass = MISCLASS_K2[regime_name] if k == 2 else MISCLASS_K4[regime_name]\n            for ne in N_EXPERTS:\n                for sigma in sigma_list:\n                    for dgp_name in dgp_list:\n                        configs.append((regime_name, k, misclass, ne, sigma, dgp_name))\n\n    total = len(configs) * n_mc\n    count = 0\n    t0 = time.time()\n\n    for regime_name, k, misclass, ne, sigma, dgp_name in configs:\n        dgp_cfg = DGP_CONFIGS[dgp_name]\n        outcome_bias = OUTCOME_BIAS[regime_name]\n        if k == 2:\n            outcome_bias_k = outcome_bias[:2]\n        else:\n            outcome_bias_k = outcome_bias[:k]\n\n        for mc in range(n_mc):\n            rows = run_one_mc(regime_name, REGIMES[regime_name], misclass, ne, k, seed=mc,\n                              sigma_outcome=sigma, dgp_name=dgp_name, dgp_cfg=dgp_cfg,\n                              outcome_bias_per_subgroup=outcome_bias_k)\n            results.extend(rows)\n            count += 1\n            if verbose and count % max(1, total // 20) == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / count * (total - count)\n                print(f\"  [{count}/{total}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s | {dgp_name} k={k} {regime_name} ne={ne} sigma={sigma} mc={mc}\")\n\n    return pd.DataFrame(results), time.time() - t0\n\n\nif __name__ == '__main__':\n    dry_run = '--dry-run' in sys.argv\n    args = [a for a in sys.argv[1:] if a != '--dry-run']\n    n_mc = int(args[0]) if args else N_MC\n\n    if dry_run:\n        n_mc = 1\n        sigma_list = [0.5]\n        k_list = [2]\n        dgp_list = list(DGP_CONFIGS.keys())\n    else:\n        sigma_list = None\n        k_list = [2, 4]\n        dgp_list = None\n\n    methods_str = 'oracle, naive, global_corrected, stratified_mle, ec_hte, mi_rubin, ppci, ec_hte_ppci'\n    print(f\"exp-007: PPCI + EC-HTE 4-DGP Matrix\")\n    print(f\"N={N}, N_MC={n_mc}\")\n    print(f\"Methods: {methods_str}\")\n    print(f\"DGPs: {dgp_list if dgp_list else list(DGP_CONFIGS.keys())}\")\n    print(f\"Outcome noise levels: {sigma_list if sigma_list else OUTCOME_NOISE_LEVELS}\")\n    print(f\"Note: ec_hte currently uses MLE fallback (HB placeholder)\")\n    if dry_run:\n        print(f\"** DRY RUN: 1 MC, k=[2], sigma=[0.5], all 4 DGPs **\")\n    print()\n\n    df_raw, elapsed = run_simulation(n_mc, k_list=k_list, sigma_list=sigma_list,\n                                     dgp_list=dgp_list)\n    df_agg = aggregate_results(df_raw)\n\n    raw_path = 'results/exp007_ppci_dsl_raw.csv'\n    agg_path = 'results/exp007_ppci_dsl.csv'\n    df_raw.to_csv(raw_path, index=False)\n    df_agg.to_csv(agg_path, index=False)\n\n    print(f\"\\nTotal time: {elapsed:.1f}s\")\n    print(f\"Saved: {raw_path}, {agg_path}\")\n\n    pd.set_option('display.max_columns', 20)\n    pd.set_option('display.width', 240)\n    pd.set_option('display.float_format', '{:.4f}'.format)\n\n    for dgp in (dgp_list or list(DGP_CONFIGS.keys())):\n        for regime in REGIMES:\n            print(f\"\\n{'='*140}\")\n            print(f\"DGP: {dgp} | Regime: {regime}\")\n            print(f\"{'='*140}\")\n            sub = df_agg[(df_agg['regime'] == regime) & (df_agg['dgp'] == dgp)]\n            if sub.empty:\n                continue\n            cols = ['n_expert', 'k_subgroups', 'sigma_outcome', 'subgroup', 'method',\n                    'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1']\n            print(sub[cols].to_string(index=False))\n",
      "numLines": 659,
      "startLine": 1,
      "totalLines": 659
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
Now I understand the code fully. Let me analyze the bug in `method_ec_hte_ppci` (lines 387-444):

**The Bug:**
In the current `method_ec_hte_ppci`:
1. Step 1: EC-HTE uses M⁻¹ to correct covariate error → `tau_ec`
2. Step 2: Rectifier is computed as `tau_gold - tau_hat_gold` where:
   - `tau_gold` = diff_in_means(Y_true, T, gold_bool) — uses true Z grouping, true Y
   - `tau_hat_gold` = diff_in_means(Y, T, gold_zhat_bool) — uses Z_hat grouping, observed Y
   
   So the rectifier captures both covariate error and outcome error simultaneously.

3. Step 3: `tau_combined = tau_ec + rectifier`

The problem is that `tau_ec` already corrected for covariate error through the M⁻¹ adjustment, but the rectifier also includes covariate error, resulting in double correction.

**The Fix:**
The rectifier should isolate only outcome error. To do this, I need to compute `tau_hat_gold` using the true Z grouping instead of Z_hat grouping, so it only differs from `tau_gold` in the outcome measurement, not the covariate assignment.

Examining the current code more carefully...

I'm filtering the gold subset by the true Z value, then computing two estimates: one using true Y and true Z grouping for a clean baseline, and another using observed Y with Z_hat grouping to capture the outcome error while keeping the covariate structure consistent. Implementing the fix now. I need to update the docstring for `method_ppci` to clarify it captures all systematic error, verify that `generate_data` provides true Z values in the gold subset, and add a note at the top of the file explaining the correction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "0fd5a571-cfa2-48d2-8215-9a54cc743446",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018xQzAudfpuRH6pkLAraWYX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11664,
      "cache_read_input_tokens": 19414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11664
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

I see the bug. In `method_ec_hte_ppci`, the rectifier computes `tau_gold - tau_hat_gold` where `tau_hat_gold` uses Z_hat grouping + observed Y, so it captures both covariate and outcome error. Since M⁻¹ already corrected covariate error, this double-corrects it.

The fix: compute `tau_hat_gold` using true Z (same `gold_bool` mask) but observed Y, so the rectifier only captures outcome error.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "dcd6a080-57c7-4ae7-8eef-00049c5b214f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018xQzAudfpuRH6pkLAraWYX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11664,
      "cache_read_input_tokens": 19414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11664
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

<details open><summary>🔧 Tool call — Edit · `toolu_01HU21xv9LQYEopHnBkQQbhb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py",
  "old_string": "\"\"\"\nexp-007: PPCI + Stratified MLE Baseline Comparison for EC-HTE\nCompares measurement-model-level correction (EC-HTE) vs estimand-level correction (Stratified MLE)\nvs standard PPCI approach. DGP uses pure covariate-error: only Z has LLM misclassification.\nOutcome Y can optionally have measurement error (sigma_outcome > 0).\n\"\"\"",
  "new_string": "\"\"\"\nexp-007: PPCI + Stratified MLE Baseline Comparison for EC-HTE\nCompares measurement-model-level correction (EC-HTE) vs estimand-level correction (Stratified MLE)\nvs standard PPCI approach. DGP uses pure covariate-error: only Z has LLM misclassification.\nOutcome Y can optionally have measurement error (sigma_outcome > 0).\n\nFix (2026-05-20): method_ec_hte_ppci double-correction bug.\n  Rectifier was using Z_hat grouping on gold subset, capturing both covariate and outcome error.\n  Since M^{-1} already corrects covariate error, this caused double correction under DGP A/C.\n  Fixed: rectifier now uses true Z grouping on gold subset so it only captures outcome error.\n\"\"\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "65e1697a-595f-4241-b86f-c76b9bc260ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018xQzAudfpuRH6pkLAraWYX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11664,
      "cache_read_input_tokens": 19414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11664
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

_source line 10 · 2026-05-20T22:32:25.432Z_

<details><summary>↩ Tool result · `toolu_01HU21xv9LQYEopHnBkQQbhb`</summary>

```text
The file /home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "4e93b8f8-aa0c-4219-8e65-17dec93c2f06",
  "tool_use_result": {
    "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py",
    "oldString": "\"\"\"\nexp-007: PPCI + Stratified MLE Baseline Comparison for EC-HTE\nCompares measurement-model-level correction (EC-HTE) vs estimand-level correction (Stratified MLE)\nvs standard PPCI approach. DGP uses pure covariate-error: only Z has LLM misclassification.\nOutcome Y can optionally have measurement error (sigma_outcome > 0).\n\"\"\"",
    "newString": "\"\"\"\nexp-007: PPCI + Stratified MLE Baseline Comparison for EC-HTE\nCompares measurement-model-level correction (EC-HTE) vs estimand-level correction (Stratified MLE)\nvs standard PPCI approach. DGP uses pure covariate-error: only Z has LLM misclassification.\nOutcome Y can optionally have measurement error (sigma_outcome > 0).\n\nFix (2026-05-20): method_ec_hte_ppci double-correction bug.\n  Rectifier was using Z_hat grouping on gold subset, capturing both covariate and outcome error.\n  Since M^{-1} already corrects covariate error, this caused double correction under DGP A/C.\n  Fixed: rectifier now uses true Z grouping on gold subset so it only captures outcome error.\n\"\"\"",
    "originalFile": "\"\"\"\nexp-007: PPCI + Stratified MLE Baseline Comparison for EC-HTE\nCompares measurement-model-level correction (EC-HTE) vs estimand-level correction (Stratified MLE)\nvs standard PPCI approach. DGP uses pure covariate-error: only Z has LLM misclassification.\nOutcome Y can optionally have measurement error (sigma_outcome > 0).\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nimport sys\nimport time\nimport warnings\nwarnings.filterwarnings('ignore')\n\n# === DGP ===\n\nREGIMES = {\n    'extreme':     {'tau_z1': 0.5, 'tau_z0': 0.1},\n    'moderate':    {'tau_z1': 0.3, 'tau_z0': 0.15},\n    'homogeneous': {'tau_z1': 0.25, 'tau_z0': 0.20},\n}\n\nMISCLASS_K2 = {\n    'extreme':     [0.25, 0.05],\n    'moderate':    [0.15, 0.10],\n    'homogeneous': [0.12, 0.12],\n}\n\nMISCLASS_K4 = {\n    'extreme':     [0.30, 0.20, 0.10, 0.03],\n    'moderate':    [0.20, 0.15, 0.10, 0.05],\n    'homogeneous': [0.12, 0.12, 0.12, 0.12],\n}\n\nOUTCOME_BIAS = {\n    'extreme':     [0.3, 0.1, 0.5, 0.2],\n    'moderate':    [0.15, 0.05, 0.25, 0.10],\n    'homogeneous': [0.1, 0.1, 0.1, 0.1],\n}\n\nDGP_CONFIGS = {\n    'A_covariate_only':  {'has_covariate_error': True,  'has_outcome_error': False},\n    'B_outcome_only':    {'has_covariate_error': False, 'has_outcome_error': True},\n    'C_both_errors':     {'has_covariate_error': True,  'has_outcome_error': True},\n    'D_no_error':        {'has_covariate_error': False, 'has_outcome_error': False},\n}\n\nN = 5000\nN_EXPERTS = [50, 100, 250, 500]\nN_MC = 100\nOUTCOME_NOISE_LEVELS = [0.0, 0.5, 1.0]\n\n\ndef generate_data(regime_params, misclass_rates, n_expert, k_subgroups, seed,\n                  sigma_outcome=0.0, outcome_noise_heterogeneous=True,\n                  has_covariate_error=True, has_outcome_error=False,\n                  outcome_bias_per_subgroup=None):\n    \"\"\"Generate synthetic data with configurable covariate and outcome error.\n\n    DGP A (covariate only): Z_hat has misclassification, Y = Y_true\n    DGP B (outcome only): Z_hat = Z, Y has treatment-differential bias\n    DGP C (both): Z_hat has misclassification AND Y has bias\n    DGP D (no error): Z_hat = Z, Y = Y_true\n    \"\"\"\n    rng = np.random.RandomState(seed)\n    k = k_subgroups\n\n    T = rng.binomial(1, 0.5, N)\n    Z = rng.binomial(1, 0.5, N)\n    S = rng.choice(k, N, p=[1/k]*k)\n    X = rng.randn(N, 5)\n\n    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])\n    eps = rng.randn(N)\n    Y_true = 1 + tau * T + 0.5 * X[:, 0] + eps\n    Y = Y_true.copy()\n\n    if has_outcome_error:\n        if outcome_bias_per_subgroup is not None:\n            for i in range(k):\n                s_mask = (S == i)\n                bias_i = outcome_bias_per_subgroup[i] if i < len(outcome_bias_per_subgroup) else outcome_bias_per_subgroup[-1]\n                Y[s_mask] += bias_i * T[s_mask]\n        if sigma_outcome > 0:\n            for i in range(k):\n                s_mask = (S == i)\n                noise_scale = sigma_outcome * (1 + 0.5 * i / max(k - 1, 1))\n                Y[s_mask] += rng.normal(0, noise_scale, s_mask.sum())\n\n    if has_covariate_error:\n        mc_rates = np.array([misclass_rates[s] for s in S])\n        flip = rng.rand(N) < mc_rates\n        Z_hat = np.where(flip, 1 - Z, Z)\n    else:\n        Z_hat = Z.copy()\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'X': X, 'Y': Y,\n        'Y_true': Y_true, 'tau': tau, 'expert_mask': expert_mask,\n    }\n\n\n# === Confusion Matrix Estimators ===\n\ndef estimate_cm_mle(z_true, z_hat):\n    \"\"\"MLE confusion matrix with Laplace smoothing. C[z, z_hat] = P(Z_hat=z_hat | Z=z).\"\"\"\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (mask.sum() + 2)\n    return C\n\n\ndef estimate_cm_hb(z_true, z_hat, all_subgroup_data):\n    \"\"\"Hierarchical Bayesian confusion matrix estimator (placeholder).\n\n    # TODO: integrate HB from exp001 after MCMC fix\n    Uses Dirichlet-Multinomial hierarchical model with partial pooling across subgroups.\n    \"\"\"\n    return estimate_cm_mle(z_true, z_hat)\n\n\n# === Correction Methods ===\n\ndef diff_in_means(Y, T, mask):\n    \"\"\"Difference-in-means estimator for subpopulation defined by mask.\"\"\"\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    \"\"\"M[z_hat, z] = P(Z=z | Z_hat=z_hat) via Bayes' rule.\"\"\"\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh]\n    return M\n\n\ndef invert_mixing(M, tau_obs, se_obs):\n    \"\"\"Apply M^{-1} correction. Returns (tau_corrected, se_corrected).\"\"\"\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    M_inv = np.linalg.inv(M)\n    tau_corrected = M_inv @ tau_obs\n    sigma_obs = np.diag(se_obs ** 2)\n    sigma_corrected = M_inv @ sigma_obs @ M_inv.T\n    se_corrected = np.sqrt(np.diag(sigma_corrected))\n    return tau_corrected, se_corrected\n\n\ndef method_oracle(data, s_val):\n    \"\"\"Oracle: use true Z within subgroup s.\"\"\"\n    Y, T, Z, S = data['Y'], data['T'], data['Z'], data['S']\n    s_mask = S == s_val\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z == 1))\n    return th0, th1, se0, se1\n\n\ndef method_naive(data, s_val):\n    \"\"\"Naive: use Z_hat within subgroup s, no correction.\"\"\"\n    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']\n    s_mask = S == s_val\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    return th0, th1, se0, se1\n\n\ndef method_global_corrected(data, s_val, C_global, p_z_global, p_zh_global):\n    \"\"\"Global-corrected: use global M_global^{-1} on subgroup-level observed CATEs.\"\"\"\n    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']\n    s_mask = S == s_val\n\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    if np.isnan(th0) or np.isnan(th1):\n        return np.nan, np.nan, np.nan, np.nan\n\n    M = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n    tau_corr, se_corr = invert_mixing(M, np.array([th0, th1]), np.array([se0, se1]))\n    return tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]\n\n\ndef method_stratified_mle(data, s_val, C_s, p_z_s, p_zh_s):\n    \"\"\"Stratified MLE: per-subgroup independent correction.\n\n    Each subgroup estimates its own confusion matrix independently (no pooling).\n    This is estimand-level correction -- correct the CATE estimate directly\n    using the subgroup's own confusion matrix.\n\n    Key difference from EC-HTE: no cross-subgroup shrinkage.\n    When n_expert is small per subgroup, Stratified MLE has high variance.\n    \"\"\"\n    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']\n    s_mask = S == s_val\n\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    if np.isnan(th0) or np.isnan(th1):\n        return np.nan, np.nan, np.nan, np.nan\n\n    M_s = build_mixing_matrix(C_s, p_z_s, p_zh_s)\n    tau_corr, se_corr = invert_mixing(M_s, np.array([th0, th1]), np.array([se0, se1]))\n    return tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]\n\n\ndef method_ec_hte(data, s_val, C_s_hb, p_z_s, p_zh_s):\n    \"\"\"EC-HTE: hierarchical Bayesian confusion matrix + subgroup correction.\n\n    Uses HB estimator (partial pooling) for confusion matrix, then applies\n    subgroup-level correction. The key advantage over Stratified MLE is that the\n    confusion matrix estimate borrows strength across subgroups.\n\n    # TODO: integrate HB from exp001 after MCMC fix\n    Currently falls back to MLE (same as Stratified MLE) until HB is integrated.\n    \"\"\"\n    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']\n    s_mask = S == s_val\n\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    if np.isnan(th0) or np.isnan(th1):\n        return np.nan, np.nan, np.nan, np.nan\n\n    M_s = build_mixing_matrix(C_s_hb, p_z_s, p_zh_s)\n    tau_corr, se_corr = invert_mixing(M_s, np.array([th0, th1]), np.array([se0, se1]))\n    return tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]\n\n\ndef method_mi_rubin(data, s_val, M=20, seed=0):\n    \"\"\"Multiple Imputation with Rubin's rules (formerly called PPCI).\n\n    For each non-expert observation, impute Z from P(Z|Z_hat, S) estimated\n    on expert data. Repeat M times, compute CATE on each imputed dataset,\n    then combine estimates using Rubin's rules.\n    \"\"\"\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n    rng = np.random.RandomState(seed)\n\n    s_mask = S == s_val\n    expert_s = expert_mask & s_mask\n\n    if expert_s.sum() < 4:\n        return np.nan, np.nan, np.nan, np.nan\n\n    p_z1_given_zhat = {}\n    for z_hat_val in [0, 1]:\n        expert_zhat = expert_s & (Z_hat == z_hat_val)\n        if expert_zhat.sum() > 0:\n            p_z1_given_zhat[z_hat_val] = np.clip(Z[expert_zhat].mean(), 0.01, 0.99)\n        else:\n            p_z1_given_zhat[z_hat_val] = float(z_hat_val)\n\n    Y_s = Y[s_mask]\n    T_s = T[s_mask]\n    Z_hat_s = Z_hat[s_mask]\n    is_expert_s = expert_mask[s_mask]\n    Z_true_s = Z[s_mask]\n    non_expert_s = ~is_expert_s\n\n    tau_z0_list, tau_z1_list = [], []\n    var_z0_list, var_z1_list = [], []\n\n    for m_iter in range(M):\n        Z_imp = Z_hat_s.copy().astype(float)\n        Z_imp[is_expert_s] = Z_true_s[is_expert_s]\n        if non_expert_s.any():\n            probs = np.array([p_z1_given_zhat[zh] for zh in Z_hat_s[non_expert_s]])\n            Z_imp[non_expert_s] = rng.binomial(1, probs).astype(float)\n\n        for z_val, tau_list, var_list in [(0, tau_z0_list, var_z0_list),\n                                          (1, tau_z1_list, var_z1_list)]:\n            z_mask = Z_imp == z_val\n            t1 = z_mask & (T_s == 1)\n            t0 = z_mask & (T_s == 0)\n            n1, n0 = t1.sum(), t0.sum()\n            if n1 < 2 or n0 < 2:\n                tau_list.append(np.nan)\n                var_list.append(np.nan)\n            else:\n                y1, y0 = Y_s[t1], Y_s[t0]\n                tau_hat = y1.mean() - y0.mean()\n                v = y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0\n                tau_list.append(tau_hat)\n                var_list.append(v)\n\n    def rubins_combine(tau_list, var_list):\n        valid = [(t, v) for t, v in zip(tau_list, var_list)\n                 if not np.isnan(t) and not np.isnan(v)]\n        if len(valid) < 2:\n            return np.nan, np.nan\n        taus = np.array([t for t, v in valid])\n        vars_ = np.array([v for t, v in valid])\n        m_eff = len(valid)\n        tau_bar = taus.mean()\n        W = vars_.mean()\n        B = taus.var(ddof=1)\n        V_total = W + (1 + 1.0 / m_eff) * B\n        return tau_bar, np.sqrt(max(V_total, 0))\n\n    th0, se0 = rubins_combine(tau_z0_list, var_z0_list)\n    th1, se1 = rubins_combine(tau_z1_list, var_z1_list)\n    return th0, th1, se0, se1\n\n\ndef method_ppci(data, s_val):\n    \"\"\"PPI rectifier for CATE estimation.\n\n    Corrects outcome-side bias using a gold-standard expert subset.\n    Gold subset has access to BOTH true Z and true Y (Y_true).\n    For each subgroup s and Z-level z:\n      1. tau_hat_all(z,s) = CATE from ALL data using Z_hat and observed Y\n      2. tau_gold(z,s) = CATE from GOLD subset using true Z and true Y\n      3. tau_hat_gold(z,s) = CATE from GOLD subset using Z_hat and observed Y\n      4. rectifier = tau_gold - tau_hat_gold\n      5. tau_ppci = tau_hat_all + rectifier\n    \"\"\"\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    Y_true = data['Y_true']\n    expert_mask = data['expert_mask']\n\n    s_mask = S == s_val\n    expert_s = expert_mask & s_mask\n    n_expert_s = expert_s.sum()\n\n    if n_expert_s < 10:\n        th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n        th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n        return th0, th1, se0, se1\n\n    expert_s_indices = np.where(expert_s)[0]\n    Z_true_s = Z[expert_s_indices]\n\n    results_z = {}\n    for z_val in [0, 1]:\n        all_mask = s_mask & (Z_hat == z_val)\n        tau_hat_all, se_hat_all = diff_in_means(Y, T, all_mask)\n\n        gold_mask_z = (Z_true_s == z_val)\n        gold_indices = expert_s_indices[gold_mask_z]\n\n        if len(gold_indices) < 4:\n            results_z[z_val] = (tau_hat_all, se_hat_all)\n            continue\n\n        # tau_gold: use true Z and true Y on gold subset\n        gold_bool = np.zeros(len(Y), dtype=bool)\n        gold_bool[gold_indices] = True\n        tau_gold, se_gold = diff_in_means(Y_true, T, gold_bool)\n\n        # tau_hat_gold: use Z_hat and observed Y on gold subset (same people)\n        gold_zhat_mask = (Z_hat[expert_s_indices] == z_val)\n        gold_zhat_indices = expert_s_indices[gold_zhat_mask]\n        gold_zhat_bool = np.zeros(len(Y), dtype=bool)\n        gold_zhat_bool[gold_zhat_indices] = True\n        tau_hat_gold, se_hat_gold = diff_in_means(Y, T, gold_zhat_bool)\n\n        if np.isnan(tau_gold) or np.isnan(tau_hat_gold) or np.isnan(tau_hat_all):\n            results_z[z_val] = (tau_hat_all, se_hat_all)\n            continue\n\n        rectifier = tau_gold - tau_hat_gold\n        tau_ppci = tau_hat_all + rectifier\n        se_ppci = np.sqrt(se_hat_all**2 + se_gold**2 + se_hat_gold**2)\n        results_z[z_val] = (tau_ppci, se_ppci)\n\n    th0, se0 = results_z.get(0, (np.nan, np.nan))\n    th1, se1 = results_z.get(1, (np.nan, np.nan))\n    return th0, th1, se0, se1\n\n\ndef method_ec_hte_ppci(data, s_val, C_s, p_z_s, p_zh_s):\n    \"\"\"EC-HTE + PPCI: correct covariate error via M^{-1}, then apply PPI rectifier for outcome error.\"\"\"\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    Y_true = data['Y_true']\n    expert_mask = data['expert_mask']\n\n    s_mask = S == s_val\n    expert_s = expert_mask & s_mask\n\n    th0_obs, se0_obs = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1_obs, se1_obs = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    if np.isnan(th0_obs) or np.isnan(th1_obs):\n        return np.nan, np.nan, np.nan, np.nan\n\n    M_s = build_mixing_matrix(C_s, p_z_s, p_zh_s)\n    tau_ec, se_ec = invert_mixing(M_s, np.array([th0_obs, th1_obs]),\n                                  np.array([se0_obs, se1_obs]))\n\n    n_expert_s = expert_s.sum()\n    if n_expert_s < 10:\n        return tau_ec[0], tau_ec[1], se_ec[0], se_ec[1]\n\n    expert_s_indices = np.where(expert_s)[0]\n    Z_true_s = Z[expert_s_indices]\n\n    results_z = {}\n    for idx, z_val in enumerate([0, 1]):\n        gold_z_mask = (Z_true_s == z_val)\n        gold_indices = expert_s_indices[gold_z_mask]\n\n        if len(gold_indices) < 4:\n            results_z[z_val] = (tau_ec[idx], se_ec[idx])\n            continue\n\n        # tau_gold: true Z + true Y on gold subset\n        gold_bool = np.zeros(len(Y), dtype=bool)\n        gold_bool[gold_indices] = True\n        tau_gold, se_gold = diff_in_means(Y_true, T, gold_bool)\n\n        # tau_hat_gold: Z_hat + observed Y on gold subset\n        gold_zhat_mask = (Z_hat[expert_s_indices] == z_val)\n        gold_zhat_indices = expert_s_indices[gold_zhat_mask]\n        gold_zhat_bool = np.zeros(len(Y), dtype=bool)\n        gold_zhat_bool[gold_zhat_indices] = True\n        tau_hat_gold, se_hat_gold = diff_in_means(Y, T, gold_zhat_bool)\n\n        if np.isnan(tau_gold) or np.isnan(tau_hat_gold):\n            results_z[z_val] = (tau_ec[idx], se_ec[idx])\n            continue\n\n        rectifier = tau_gold - tau_hat_gold\n        tau_combined = tau_ec[idx] + rectifier\n        se_combined = np.sqrt(se_ec[idx]**2 + se_gold**2 + se_hat_gold**2)\n        results_z[z_val] = (tau_combined, se_combined)\n\n    th0, se0 = results_z.get(0, (np.nan, np.nan))\n    th1, se1 = results_z.get(1, (np.nan, np.nan))\n    return th0, th1, se0, se1\n\n\n# === Main Simulation Loop ===\n\ndef run_one_mc(regime_name, regime_params, misclass_rates, n_expert, k_subgroups, seed,\n               sigma_outcome=0.0, dgp_name='A_covariate_only', dgp_cfg=None,\n               outcome_bias_per_subgroup=None):\n    \"\"\"Run one MC iteration for all methods.\"\"\"\n    if dgp_cfg is None:\n        dgp_cfg = DGP_CONFIGS[dgp_name]\n\n    data = generate_data(regime_params, misclass_rates, n_expert, k_subgroups, seed,\n                         sigma_outcome=sigma_outcome,\n                         has_covariate_error=dgp_cfg['has_covariate_error'],\n                         has_outcome_error=dgp_cfg['has_outcome_error'],\n                         outcome_bias_per_subgroup=outcome_bias_per_subgroup)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n    tau_true_z0, tau_true_z1 = regime_params['tau_z0'], regime_params['tau_z1']\n\n    C_global = estimate_cm_mle(Z[expert_mask], Z_hat[expert_mask])\n    p_z_global = np.clip(np.array([(Z[expert_mask]==0).mean(), (Z[expert_mask]==1).mean()]), 0.01, 0.99)\n    p_zh_global = np.clip(np.array([(Z_hat==0).mean(), (Z_hat==1).mean()]), 0.01, 0.99)\n\n    C_mle = {}\n    C_hb = {}\n    all_subgroup_expert_data = []\n\n    for s in range(k_subgroups):\n        s_mask = S == s\n        expert_s = expert_mask & s_mask\n        if expert_s.sum() >= 4:\n            C_mle[s] = estimate_cm_mle(Z[expert_s], Z_hat[expert_s])\n            all_subgroup_expert_data.append((Z[expert_s], Z_hat[expert_s]))\n        else:\n            C_mle[s] = C_global\n            all_subgroup_expert_data.append((Z[expert_mask], Z_hat[expert_mask]))\n\n    for s in range(k_subgroups):\n        s_mask = S == s\n        expert_s = expert_mask & s_mask\n        if expert_s.sum() >= 4:\n            C_hb[s] = estimate_cm_hb(Z[expert_s], Z_hat[expert_s], all_subgroup_expert_data)\n        else:\n            C_hb[s] = C_global\n\n    rows = []\n    base = {\n        'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k_subgroups,\n        'sigma_outcome': sigma_outcome, 'dgp': dgp_name,\n        'mc_run': seed, 'tau_true_z0': tau_true_z0, 'tau_true_z1': tau_true_z1,\n    }\n\n    def make_row(method, subgroup, th0, th1, se0, se1):\n        return {**base, 'method': method, 'subgroup': subgroup,\n                'tau_hat_z0': th0, 'tau_hat_z1': th1,\n                'ci_lower_z0': th0 - 1.96*se0 if not np.isnan(se0) else np.nan,\n                'ci_upper_z0': th0 + 1.96*se0 if not np.isnan(se0) else np.nan,\n                'ci_lower_z1': th1 - 1.96*se1 if not np.isnan(se1) else np.nan,\n                'ci_upper_z1': th1 + 1.96*se1 if not np.isnan(se1) else np.nan}\n\n    for s in range(k_subgroups):\n        s_mask = S == s\n        expert_s = expert_mask & s_mask\n        if expert_s.sum() >= 4:\n            p_z_s = np.clip(np.array([(Z[expert_s]==0).mean(), (Z[expert_s]==1).mean()]), 0.01, 0.99)\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.clip(np.array([(Z_hat[s_mask]==0).mean(), (Z_hat[s_mask]==1).mean()]), 0.01, 0.99)\n\n        th0, th1, se0, se1 = method_oracle(data, s)\n        rows.append(make_row('oracle', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_naive(data, s)\n        rows.append(make_row('naive', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_global_corrected(data, s, C_global, p_z_global, p_zh_global)\n        rows.append(make_row('global_corrected', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_stratified_mle(data, s, C_mle[s], p_z_s, p_zh_s)\n        rows.append(make_row('stratified_mle', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_ec_hte(data, s, C_hb[s], p_z_s, p_zh_s)\n        rows.append(make_row('ec_hte', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_mi_rubin(data, s, M=20, seed=seed * 1000 + s)\n        rows.append(make_row('mi_rubin', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_ppci(data, s)\n        rows.append(make_row('ppci', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_ec_hte_ppci(data, s, C_hb[s], p_z_s, p_zh_s)\n        rows.append(make_row('ec_hte_ppci', s, th0, th1, se0, se1))\n\n    return rows\n\n\ndef aggregate_results(df):\n    \"\"\"Aggregate per-run results into summary statistics.\"\"\"\n    rows = []\n    group_cols = ['regime', 'n_expert', 'k_subgroups', 'sigma_outcome', 'dgp', 'subgroup', 'method']\n    for keys, grp in df.groupby(group_cols):\n        row = dict(zip(group_cols, keys))\n        for z in ['z0', 'z1']:\n            err = grp[f'tau_hat_{z}'] - grp[f'tau_true_{z}']\n            valid = err.dropna()\n            if len(valid) == 0:\n                row.update({f'bias_{z}': np.nan, f'rmse_{z}': np.nan, f'coverage_{z}': np.nan})\n                continue\n            row[f'bias_{z}'] = valid.mean()\n            row[f'rmse_{z}'] = np.sqrt((valid**2).mean())\n            covered = ((grp[f'ci_lower_{z}'] <= grp[f'tau_true_{z}']) &\n                       (grp[f'tau_true_{z}'] <= grp[f'ci_upper_{z}'])).mean()\n            row[f'coverage_{z}'] = covered\n            row[f'bias_{z}_se'] = valid.std() / np.sqrt(len(valid))\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\ndef run_simulation(n_mc, k_list=[2, 4], sigma_list=None, dgp_list=None, verbose=True):\n    \"\"\"Run full simulation sweep over DGP configs.\"\"\"\n    if sigma_list is None:\n        sigma_list = OUTCOME_NOISE_LEVELS\n    if dgp_list is None:\n        dgp_list = list(DGP_CONFIGS.keys())\n    results = []\n    configs = []\n    for regime_name in REGIMES:\n        for k in k_list:\n            misclass = MISCLASS_K2[regime_name] if k == 2 else MISCLASS_K4[regime_name]\n            for ne in N_EXPERTS:\n                for sigma in sigma_list:\n                    for dgp_name in dgp_list:\n                        configs.append((regime_name, k, misclass, ne, sigma, dgp_name))\n\n    total = len(configs) * n_mc\n    count = 0\n    t0 = time.time()\n\n    for regime_name, k, misclass, ne, sigma, dgp_name in configs:\n        dgp_cfg = DGP_CONFIGS[dgp_name]\n        outcome_bias = OUTCOME_BIAS[regime_name]\n        if k == 2:\n            outcome_bias_k = outcome_bias[:2]\n        else:\n            outcome_bias_k = outcome_bias[:k]\n\n        for mc in range(n_mc):\n            rows = run_one_mc(regime_name, REGIMES[regime_name], misclass, ne, k, seed=mc,\n                              sigma_outcome=sigma, dgp_name=dgp_name, dgp_cfg=dgp_cfg,\n                              outcome_bias_per_subgroup=outcome_bias_k)\n            results.extend(rows)\n            count += 1\n            if verbose and count % max(1, total // 20) == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / count * (total - count)\n                print(f\"  [{count}/{total}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s | {dgp_name} k={k} {regime_name} ne={ne} sigma={sigma} mc={mc}\")\n\n    return pd.DataFrame(results), time.time() - t0\n\n\nif __name__ == '__main__':\n    dry_run = '--dry-run' in sys.argv\n    args = [a for a in sys.argv[1:] if a != '--dry-run']\n    n_mc = int(args[0]) if args else N_MC\n\n    if dry_run:\n        n_mc = 1\n        sigma_list = [0.5]\n        k_list = [2]\n        dgp_list = list(DGP_CONFIGS.keys())\n    else:\n        sigma_list = None\n        k_list = [2, 4]\n        dgp_list = None\n\n    methods_str = 'oracle, naive, global_corrected, stratified_mle, ec_hte, mi_rubin, ppci, ec_hte_ppci'\n    print(f\"exp-007: PPCI + EC-HTE 4-DGP Matrix\")\n    print(f\"N={N}, N_MC={n_mc}\")\n    print(f\"Methods: {methods_str}\")\n    print(f\"DGPs: {dgp_list if dgp_list else list(DGP_CONFIGS.keys())}\")\n    print(f\"Outcome noise levels: {sigma_list if sigma_list else OUTCOME_NOISE_LEVELS}\")\n    print(f\"Note: ec_hte currently uses MLE fallback (HB placeholder)\")\n    if dry_run:\n        print(f\"** DRY RUN: 1 MC, k=[2], sigma=[0.5], all 4 DGPs **\")\n    print()\n\n    df_raw, elapsed = run_simulation(n_mc, k_list=k_list, sigma_list=sigma_list,\n                                     dgp_list=dgp_list)\n    df_agg = aggregate_results(df_raw)\n\n    raw_path = 'results/exp007_ppci_dsl_raw.csv'\n    agg_path = 'results/exp007_ppci_dsl.csv'\n    df_raw.to_csv(raw_path, index=False)\n    df_agg.to_csv(agg_path, index=False)\n\n    print(f\"\\nTotal time: {elapsed:.1f}s\")\n    print(f\"Saved: {raw_path}, {agg_path}\")\n\n    pd.set_option('display.max_columns', 20)\n    pd.set_option('display.width', 240)\n    pd.set_option('display.float_format', '{:.4f}'.format)\n\n    for dgp in (dgp_list or list(DGP_CONFIGS.keys())):\n        for regime in REGIMES:\n            print(f\"\\n{'='*140}\")\n            print(f\"DGP: {dgp} | Regime: {regime}\")\n            print(f\"{'='*140}\")\n            sub = df_agg[(df_agg['regime'] == regime) & (df_agg['dgp'] == dgp)]\n            if sub.empty:\n                continue\n            cols = ['n_expert', 'k_subgroups', 'sigma_outcome', 'subgroup', 'method',\n                    'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1']\n            print(sub[cols].to_string(index=False))\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 6,
        "newStart": 3,
        "newLines": 11,
        "lines": [
          " Compares measurement-model-level correction (EC-HTE) vs estimand-level correction (Stratified MLE)",
          " vs standard PPCI approach. DGP uses pure covariate-error: only Z has LLM misclassification.",
          " Outcome Y can optionally have measurement error (sigma_outcome > 0).",
          "+",
          "+Fix (2026-05-20): method_ec_hte_ppci double-correction bug.",
          "+  Rectifier was using Z_hat grouping on gold subset, capturing both covariate and outcome error.",
          "+  Since M^{-1} already corrects covariate error, this caused double correction under DGP A/C.",
          "+  Fixed: rectifier now uses true Z grouping on gold subset so it only captures outcome error.",
          " \"\"\"",
          " ",
          " import numpy as np"
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

<details open><summary>🔧 Tool call — Edit · `toolu_01QPiEpfCqoYgq3XqrnGCKgx`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py",
  "old_string": "def method_ppci(data, s_val):\n    \"\"\"PPI rectifier for CATE estimation.\n\n    Corrects outcome-side bias using a gold-standard expert subset.\n    Gold subset has access to BOTH true Z and true Y (Y_true).\n    For each subgroup s and Z-level z:\n      1. tau_hat_all(z,s) = CATE from ALL data using Z_hat and observed Y\n      2. tau_gold(z,s) = CATE from GOLD subset using true Z and true Y\n      3. tau_hat_gold(z,s) = CATE from GOLD subset using Z_hat and observed Y\n      4. rectifier = tau_gold - tau_hat_gold\n      5. tau_ppci = tau_hat_all + rectifier\n    \"\"\"",
  "new_string": "def method_ppci(data, s_val):\n    \"\"\"PPI rectifier for CATE estimation.\n\n    General-purpose correction using a gold-standard expert subset.\n    The rectifier captures ALL systematic error (covariate + outcome) between\n    the gold estimate (true Z, true Y) and the noisy estimate (Z_hat, observed Y).\n    This is complementary to EC-HTE's structured covariate-only correction via M^{-1}.\n\n    For each subgroup s and Z-level z:\n      1. tau_hat_all(z,s) = CATE from ALL data using Z_hat and observed Y\n      2. tau_gold(z,s) = CATE from GOLD subset using true Z and true Y\n      3. tau_hat_gold(z,s) = CATE from GOLD subset using Z_hat and observed Y\n      4. rectifier = tau_gold - tau_hat_gold  (captures covariate + outcome error)\n      5. tau_ppci = tau_hat_all + rectifier\n    \"\"\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "0e4ff438-e3fe-4d05-8598-179b50da40bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JYnExopoxHwyGaYPgyHHX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1704,
      "cache_read_input_tokens": 31078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1704
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

_source line 12 · 2026-05-20T22:32:35.370Z_

<details><summary>↩ Tool result · `toolu_01QPiEpfCqoYgq3XqrnGCKgx`</summary>

```text
The file /home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "ffc67c60-d44d-4594-9104-477abedd7d1d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py",
    "oldString": "def method_ppci(data, s_val):\n    \"\"\"PPI rectifier for CATE estimation.\n\n    Corrects outcome-side bias using a gold-standard expert subset.\n    Gold subset has access to BOTH true Z and true Y (Y_true).\n    For each subgroup s and Z-level z:\n      1. tau_hat_all(z,s) = CATE from ALL data using Z_hat and observed Y\n      2. tau_gold(z,s) = CATE from GOLD subset using true Z and true Y\n      3. tau_hat_gold(z,s) = CATE from GOLD subset using Z_hat and observed Y\n      4. rectifier = tau_gold - tau_hat_gold\n      5. tau_ppci = tau_hat_all + rectifier\n    \"\"\"",
    "newString": "def method_ppci(data, s_val):\n    \"\"\"PPI rectifier for CATE estimation.\n\n    General-purpose correction using a gold-standard expert subset.\n    The rectifier captures ALL systematic error (covariate + outcome) between\n    the gold estimate (true Z, true Y) and the noisy estimate (Z_hat, observed Y).\n    This is complementary to EC-HTE's structured covariate-only correction via M^{-1}.\n\n    For each subgroup s and Z-level z:\n      1. tau_hat_all(z,s) = CATE from ALL data using Z_hat and observed Y\n      2. tau_gold(z,s) = CATE from GOLD subset using true Z and true Y\n      3. tau_hat_gold(z,s) = CATE from GOLD subset using Z_hat and observed Y\n      4. rectifier = tau_gold - tau_hat_gold  (captures covariate + outcome error)\n      5. tau_ppci = tau_hat_all + rectifier\n    \"\"\"",
    "originalFile": "\"\"\"\nexp-007: PPCI + Stratified MLE Baseline Comparison for EC-HTE\nCompares measurement-model-level correction (EC-HTE) vs estimand-level correction (Stratified MLE)\nvs standard PPCI approach. DGP uses pure covariate-error: only Z has LLM misclassification.\nOutcome Y can optionally have measurement error (sigma_outcome > 0).\n\nFix (2026-05-20): method_ec_hte_ppci double-correction bug.\n  Rectifier was using Z_hat grouping on gold subset, capturing both covariate and outcome error.\n  Since M^{-1} already corrects covariate error, this caused double correction under DGP A/C.\n  Fixed: rectifier now uses true Z grouping on gold subset so it only captures outcome error.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nimport sys\nimport time\nimport warnings\nwarnings.filterwarnings('ignore')\n\n# === DGP ===\n\nREGIMES = {\n    'extreme':     {'tau_z1': 0.5, 'tau_z0': 0.1},\n    'moderate':    {'tau_z1': 0.3, 'tau_z0': 0.15},\n    'homogeneous': {'tau_z1': 0.25, 'tau_z0': 0.20},\n}\n\nMISCLASS_K2 = {\n    'extreme':     [0.25, 0.05],\n    'moderate':    [0.15, 0.10],\n    'homogeneous': [0.12, 0.12],\n}\n\nMISCLASS_K4 = {\n    'extreme':     [0.30, 0.20, 0.10, 0.03],\n    'moderate':    [0.20, 0.15, 0.10, 0.05],\n    'homogeneous': [0.12, 0.12, 0.12, 0.12],\n}\n\nOUTCOME_BIAS = {\n    'extreme':     [0.3, 0.1, 0.5, 0.2],\n    'moderate':    [0.15, 0.05, 0.25, 0.10],\n    'homogeneous': [0.1, 0.1, 0.1, 0.1],\n}\n\nDGP_CONFIGS = {\n    'A_covariate_only':  {'has_covariate_error': True,  'has_outcome_error': False},\n    'B_outcome_only':    {'has_covariate_error': False, 'has_outcome_error': True},\n    'C_both_errors':     {'has_covariate_error': True,  'has_outcome_error': True},\n    'D_no_error':        {'has_covariate_error': False, 'has_outcome_error': False},\n}\n\nN = 5000\nN_EXPERTS = [50, 100, 250, 500]\nN_MC = 100\nOUTCOME_NOISE_LEVELS = [0.0, 0.5, 1.0]\n\n\ndef generate_data(regime_params, misclass_rates, n_expert, k_subgroups, seed,\n                  sigma_outcome=0.0, outcome_noise_heterogeneous=True,\n                  has_covariate_error=True, has_outcome_error=False,\n                  outcome_bias_per_subgroup=None):\n    \"\"\"Generate synthetic data with configurable covariate and outcome error.\n\n    DGP A (covariate only): Z_hat has misclassification, Y = Y_true\n    DGP B (outcome only): Z_hat = Z, Y has treatment-differential bias\n    DGP C (both): Z_hat has misclassification AND Y has bias\n    DGP D (no error): Z_hat = Z, Y = Y_true\n    \"\"\"\n    rng = np.random.RandomState(seed)\n    k = k_subgroups\n\n    T = rng.binomial(1, 0.5, N)\n    Z = rng.binomial(1, 0.5, N)\n    S = rng.choice(k, N, p=[1/k]*k)\n    X = rng.randn(N, 5)\n\n    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])\n    eps = rng.randn(N)\n    Y_true = 1 + tau * T + 0.5 * X[:, 0] + eps\n    Y = Y_true.copy()\n\n    if has_outcome_error:\n        if outcome_bias_per_subgroup is not None:\n            for i in range(k):\n                s_mask = (S == i)\n                bias_i = outcome_bias_per_subgroup[i] if i < len(outcome_bias_per_subgroup) else outcome_bias_per_subgroup[-1]\n                Y[s_mask] += bias_i * T[s_mask]\n        if sigma_outcome > 0:\n            for i in range(k):\n                s_mask = (S == i)\n                noise_scale = sigma_outcome * (1 + 0.5 * i / max(k - 1, 1))\n                Y[s_mask] += rng.normal(0, noise_scale, s_mask.sum())\n\n    if has_covariate_error:\n        mc_rates = np.array([misclass_rates[s] for s in S])\n        flip = rng.rand(N) < mc_rates\n        Z_hat = np.where(flip, 1 - Z, Z)\n    else:\n        Z_hat = Z.copy()\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'X': X, 'Y': Y,\n        'Y_true': Y_true, 'tau': tau, 'expert_mask': expert_mask,\n    }\n\n\n# === Confusion Matrix Estimators ===\n\ndef estimate_cm_mle(z_true, z_hat):\n    \"\"\"MLE confusion matrix with Laplace smoothing. C[z, z_hat] = P(Z_hat=z_hat | Z=z).\"\"\"\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (mask.sum() + 2)\n    return C\n\n\ndef estimate_cm_hb(z_true, z_hat, all_subgroup_data):\n    \"\"\"Hierarchical Bayesian confusion matrix estimator (placeholder).\n\n    # TODO: integrate HB from exp001 after MCMC fix\n    Uses Dirichlet-Multinomial hierarchical model with partial pooling across subgroups.\n    \"\"\"\n    return estimate_cm_mle(z_true, z_hat)\n\n\n# === Correction Methods ===\n\ndef diff_in_means(Y, T, mask):\n    \"\"\"Difference-in-means estimator for subpopulation defined by mask.\"\"\"\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    \"\"\"M[z_hat, z] = P(Z=z | Z_hat=z_hat) via Bayes' rule.\"\"\"\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh]\n    return M\n\n\ndef invert_mixing(M, tau_obs, se_obs):\n    \"\"\"Apply M^{-1} correction. Returns (tau_corrected, se_corrected).\"\"\"\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    M_inv = np.linalg.inv(M)\n    tau_corrected = M_inv @ tau_obs\n    sigma_obs = np.diag(se_obs ** 2)\n    sigma_corrected = M_inv @ sigma_obs @ M_inv.T\n    se_corrected = np.sqrt(np.diag(sigma_corrected))\n    return tau_corrected, se_corrected\n\n\ndef method_oracle(data, s_val):\n    \"\"\"Oracle: use true Z within subgroup s.\"\"\"\n    Y, T, Z, S = data['Y'], data['T'], data['Z'], data['S']\n    s_mask = S == s_val\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z == 1))\n    return th0, th1, se0, se1\n\n\ndef method_naive(data, s_val):\n    \"\"\"Naive: use Z_hat within subgroup s, no correction.\"\"\"\n    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']\n    s_mask = S == s_val\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    return th0, th1, se0, se1\n\n\ndef method_global_corrected(data, s_val, C_global, p_z_global, p_zh_global):\n    \"\"\"Global-corrected: use global M_global^{-1} on subgroup-level observed CATEs.\"\"\"\n    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']\n    s_mask = S == s_val\n\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    if np.isnan(th0) or np.isnan(th1):\n        return np.nan, np.nan, np.nan, np.nan\n\n    M = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n    tau_corr, se_corr = invert_mixing(M, np.array([th0, th1]), np.array([se0, se1]))\n    return tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]\n\n\ndef method_stratified_mle(data, s_val, C_s, p_z_s, p_zh_s):\n    \"\"\"Stratified MLE: per-subgroup independent correction.\n\n    Each subgroup estimates its own confusion matrix independently (no pooling).\n    This is estimand-level correction -- correct the CATE estimate directly\n    using the subgroup's own confusion matrix.\n\n    Key difference from EC-HTE: no cross-subgroup shrinkage.\n    When n_expert is small per subgroup, Stratified MLE has high variance.\n    \"\"\"\n    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']\n    s_mask = S == s_val\n\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    if np.isnan(th0) or np.isnan(th1):\n        return np.nan, np.nan, np.nan, np.nan\n\n    M_s = build_mixing_matrix(C_s, p_z_s, p_zh_s)\n    tau_corr, se_corr = invert_mixing(M_s, np.array([th0, th1]), np.array([se0, se1]))\n    return tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]\n\n\ndef method_ec_hte(data, s_val, C_s_hb, p_z_s, p_zh_s):\n    \"\"\"EC-HTE: hierarchical Bayesian confusion matrix + subgroup correction.\n\n    Uses HB estimator (partial pooling) for confusion matrix, then applies\n    subgroup-level correction. The key advantage over Stratified MLE is that the\n    confusion matrix estimate borrows strength across subgroups.\n\n    # TODO: integrate HB from exp001 after MCMC fix\n    Currently falls back to MLE (same as Stratified MLE) until HB is integrated.\n    \"\"\"\n    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']\n    s_mask = S == s_val\n\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    if np.isnan(th0) or np.isnan(th1):\n        return np.nan, np.nan, np.nan, np.nan\n\n    M_s = build_mixing_matrix(C_s_hb, p_z_s, p_zh_s)\n    tau_corr, se_corr = invert_mixing(M_s, np.array([th0, th1]), np.array([se0, se1]))\n    return tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]\n\n\ndef method_mi_rubin(data, s_val, M=20, seed=0):\n    \"\"\"Multiple Imputation with Rubin's rules (formerly called PPCI).\n\n    For each non-expert observation, impute Z from P(Z|Z_hat, S) estimated\n    on expert data. Repeat M times, compute CATE on each imputed dataset,\n    then combine estimates using Rubin's rules.\n    \"\"\"\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n    rng = np.random.RandomState(seed)\n\n    s_mask = S == s_val\n    expert_s = expert_mask & s_mask\n\n    if expert_s.sum() < 4:\n        return np.nan, np.nan, np.nan, np.nan\n\n    p_z1_given_zhat = {}\n    for z_hat_val in [0, 1]:\n        expert_zhat = expert_s & (Z_hat == z_hat_val)\n        if expert_zhat.sum() > 0:\n            p_z1_given_zhat[z_hat_val] = np.clip(Z[expert_zhat].mean(), 0.01, 0.99)\n        else:\n            p_z1_given_zhat[z_hat_val] = float(z_hat_val)\n\n    Y_s = Y[s_mask]\n    T_s = T[s_mask]\n    Z_hat_s = Z_hat[s_mask]\n    is_expert_s = expert_mask[s_mask]\n    Z_true_s = Z[s_mask]\n    non_expert_s = ~is_expert_s\n\n    tau_z0_list, tau_z1_list = [], []\n    var_z0_list, var_z1_list = [], []\n\n    for m_iter in range(M):\n        Z_imp = Z_hat_s.copy().astype(float)\n        Z_imp[is_expert_s] = Z_true_s[is_expert_s]\n        if non_expert_s.any():\n            probs = np.array([p_z1_given_zhat[zh] for zh in Z_hat_s[non_expert_s]])\n            Z_imp[non_expert_s] = rng.binomial(1, probs).astype(float)\n\n        for z_val, tau_list, var_list in [(0, tau_z0_list, var_z0_list),\n                                          (1, tau_z1_list, var_z1_list)]:\n            z_mask = Z_imp == z_val\n            t1 = z_mask & (T_s == 1)\n            t0 = z_mask & (T_s == 0)\n            n1, n0 = t1.sum(), t0.sum()\n            if n1 < 2 or n0 < 2:\n                tau_list.append(np.nan)\n                var_list.append(np.nan)\n            else:\n                y1, y0 = Y_s[t1], Y_s[t0]\n                tau_hat = y1.mean() - y0.mean()\n                v = y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0\n                tau_list.append(tau_hat)\n                var_list.append(v)\n\n    def rubins_combine(tau_list, var_list):\n        valid = [(t, v) for t, v in zip(tau_list, var_list)\n                 if not np.isnan(t) and not np.isnan(v)]\n        if len(valid) < 2:\n            return np.nan, np.nan\n        taus = np.array([t for t, v in valid])\n        vars_ = np.array([v for t, v in valid])\n        m_eff = len(valid)\n        tau_bar = taus.mean()\n        W = vars_.mean()\n        B = taus.var(ddof=1)\n        V_total = W + (1 + 1.0 / m_eff) * B\n        return tau_bar, np.sqrt(max(V_total, 0))\n\n    th0, se0 = rubins_combine(tau_z0_list, var_z0_list)\n    th1, se1 = rubins_combine(tau_z1_list, var_z1_list)\n    return th0, th1, se0, se1\n\n\ndef method_ppci(data, s_val):\n    \"\"\"PPI rectifier for CATE estimation.\n\n    Corrects outcome-side bias using a gold-standard expert subset.\n    Gold subset has access to BOTH true Z and true Y (Y_true).\n    For each subgroup s and Z-level z:\n      1. tau_hat_all(z,s) = CATE from ALL data using Z_hat and observed Y\n      2. tau_gold(z,s) = CATE from GOLD subset using true Z and true Y\n      3. tau_hat_gold(z,s) = CATE from GOLD subset using Z_hat and observed Y\n      4. rectifier = tau_gold - tau_hat_gold\n      5. tau_ppci = tau_hat_all + rectifier\n    \"\"\"\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    Y_true = data['Y_true']\n    expert_mask = data['expert_mask']\n\n    s_mask = S == s_val\n    expert_s = expert_mask & s_mask\n    n_expert_s = expert_s.sum()\n\n    if n_expert_s < 10:\n        th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n        th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n        return th0, th1, se0, se1\n\n    expert_s_indices = np.where(expert_s)[0]\n    Z_true_s = Z[expert_s_indices]\n\n    results_z = {}\n    for z_val in [0, 1]:\n        all_mask = s_mask & (Z_hat == z_val)\n        tau_hat_all, se_hat_all = diff_in_means(Y, T, all_mask)\n\n        gold_mask_z = (Z_true_s == z_val)\n        gold_indices = expert_s_indices[gold_mask_z]\n\n        if len(gold_indices) < 4:\n            results_z[z_val] = (tau_hat_all, se_hat_all)\n            continue\n\n        # tau_gold: use true Z and true Y on gold subset\n        gold_bool = np.zeros(len(Y), dtype=bool)\n        gold_bool[gold_indices] = True\n        tau_gold, se_gold = diff_in_means(Y_true, T, gold_bool)\n\n        # tau_hat_gold: use Z_hat and observed Y on gold subset (same people)\n        gold_zhat_mask = (Z_hat[expert_s_indices] == z_val)\n        gold_zhat_indices = expert_s_indices[gold_zhat_mask]\n        gold_zhat_bool = np.zeros(len(Y), dtype=bool)\n        gold_zhat_bool[gold_zhat_indices] = True\n        tau_hat_gold, se_hat_gold = diff_in_means(Y, T, gold_zhat_bool)\n\n        if np.isnan(tau_gold) or np.isnan(tau_hat_gold) or np.isnan(tau_hat_all):\n            results_z[z_val] = (tau_hat_all, se_hat_all)\n            continue\n\n        rectifier = tau_gold - tau_hat_gold\n        tau_ppci = tau_hat_all + rectifier\n        se_ppci = np.sqrt(se_hat_all**2 + se_gold**2 + se_hat_gold**2)\n        results_z[z_val] = (tau_ppci, se_ppci)\n\n    th0, se0 = results_z.get(0, (np.nan, np.nan))\n    th1, se1 = results_z.get(1, (np.nan, np.nan))\n    return th0, th1, se0, se1\n\n\ndef method_ec_hte_ppci(data, s_val, C_s, p_z_s, p_zh_s):\n    \"\"\"EC-HTE + PPCI: correct covariate error via M^{-1}, then apply PPI rectifier for outcome error.\"\"\"\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    Y_true = data['Y_true']\n    expert_mask = data['expert_mask']\n\n    s_mask = S == s_val\n    expert_s = expert_mask & s_mask\n\n    th0_obs, se0_obs = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1_obs, se1_obs = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    if np.isnan(th0_obs) or np.isnan(th1_obs):\n        return np.nan, np.nan, np.nan, np.nan\n\n    M_s = build_mixing_matrix(C_s, p_z_s, p_zh_s)\n    tau_ec, se_ec = invert_mixing(M_s, np.array([th0_obs, th1_obs]),\n                                  np.array([se0_obs, se1_obs]))\n\n    n_expert_s = expert_s.sum()\n    if n_expert_s < 10:\n        return tau_ec[0], tau_ec[1], se_ec[0], se_ec[1]\n\n    expert_s_indices = np.where(expert_s)[0]\n    Z_true_s = Z[expert_s_indices]\n\n    results_z = {}\n    for idx, z_val in enumerate([0, 1]):\n        gold_z_mask = (Z_true_s == z_val)\n        gold_indices = expert_s_indices[gold_z_mask]\n\n        if len(gold_indices) < 4:\n            results_z[z_val] = (tau_ec[idx], se_ec[idx])\n            continue\n\n        # tau_gold: true Z + true Y on gold subset\n        gold_bool = np.zeros(len(Y), dtype=bool)\n        gold_bool[gold_indices] = True\n        tau_gold, se_gold = diff_in_means(Y_true, T, gold_bool)\n\n        # tau_hat_gold: Z_hat + observed Y on gold subset\n        gold_zhat_mask = (Z_hat[expert_s_indices] == z_val)\n        gold_zhat_indices = expert_s_indices[gold_zhat_mask]\n        gold_zhat_bool = np.zeros(len(Y), dtype=bool)\n        gold_zhat_bool[gold_zhat_indices] = True\n        tau_hat_gold, se_hat_gold = diff_in_means(Y, T, gold_zhat_bool)\n\n        if np.isnan(tau_gold) or np.isnan(tau_hat_gold):\n            results_z[z_val] = (tau_ec[idx], se_ec[idx])\n            continue\n\n        rectifier = tau_gold - tau_hat_gold\n        tau_combined = tau_ec[idx] + rectifier\n        se_combined = np.sqrt(se_ec[idx]**2 + se_gold**2 + se_hat_gold**2)\n        results_z[z_val] = (tau_combined, se_combined)\n\n    th0, se0 = results_z.get(0, (np.nan, np.nan))\n    th1, se1 = results_z.get(1, (np.nan, np.nan))\n    return th0, th1, se0, se1\n\n\n# === Main Simulation Loop ===\n\ndef run_one_mc(regime_name, regime_params, misclass_rates, n_expert, k_subgroups, seed,\n               sigma_outcome=0.0, dgp_name='A_covariate_only', dgp_cfg=None,\n               outcome_bias_per_subgroup=None):\n    \"\"\"Run one MC iteration for all methods.\"\"\"\n    if dgp_cfg is None:\n        dgp_cfg = DGP_CONFIGS[dgp_name]\n\n    data = generate_data(regime_params, misclass_rates, n_expert, k_subgroups, seed,\n                         sigma_outcome=sigma_outcome,\n                         has_covariate_error=dgp_cfg['has_covariate_error'],\n                         has_outcome_error=dgp_cfg['has_outcome_error'],\n                         outcome_bias_per_subgroup=outcome_bias_per_subgroup)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n    tau_true_z0, tau_true_z1 = regime_params['tau_z0'], regime_params['tau_z1']\n\n    C_global = estimate_cm_mle(Z[expert_mask], Z_hat[expert_mask])\n    p_z_global = np.clip(np.array([(Z[expert_mask]==0).mean(), (Z[expert_mask]==1).mean()]), 0.01, 0.99)\n    p_zh_global = np.clip(np.array([(Z_hat==0).mean(), (Z_hat==1).mean()]), 0.01, 0.99)\n\n    C_mle = {}\n    C_hb = {}\n    all_subgroup_expert_data = []\n\n    for s in range(k_subgroups):\n        s_mask = S == s\n        expert_s = expert_mask & s_mask\n        if expert_s.sum() >= 4:\n            C_mle[s] = estimate_cm_mle(Z[expert_s], Z_hat[expert_s])\n            all_subgroup_expert_data.append((Z[expert_s], Z_hat[expert_s]))\n        else:\n            C_mle[s] = C_global\n            all_subgroup_expert_data.append((Z[expert_mask], Z_hat[expert_mask]))\n\n    for s in range(k_subgroups):\n        s_mask = S == s\n        expert_s = expert_mask & s_mask\n        if expert_s.sum() >= 4:\n            C_hb[s] = estimate_cm_hb(Z[expert_s], Z_hat[expert_s], all_subgroup_expert_data)\n        else:\n            C_hb[s] = C_global\n\n    rows = []\n    base = {\n        'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k_subgroups,\n        'sigma_outcome': sigma_outcome, 'dgp': dgp_name,\n        'mc_run': seed, 'tau_true_z0': tau_true_z0, 'tau_true_z1': tau_true_z1,\n    }\n\n    def make_row(method, subgroup, th0, th1, se0, se1):\n        return {**base, 'method': method, 'subgroup': subgroup,\n                'tau_hat_z0': th0, 'tau_hat_z1': th1,\n                'ci_lower_z0': th0 - 1.96*se0 if not np.isnan(se0) else np.nan,\n                'ci_upper_z0': th0 + 1.96*se0 if not np.isnan(se0) else np.nan,\n                'ci_lower_z1': th1 - 1.96*se1 if not np.isnan(se1) else np.nan,\n                'ci_upper_z1': th1 + 1.96*se1 if not np.isnan(se1) else np.nan}\n\n    for s in range(k_subgroups):\n        s_mask = S == s\n        expert_s = expert_mask & s_mask\n        if expert_s.sum() >= 4:\n            p_z_s = np.clip(np.array([(Z[expert_s]==0).mean(), (Z[expert_s]==1).mean()]), 0.01, 0.99)\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.clip(np.array([(Z_hat[s_mask]==0).mean(), (Z_hat[s_mask]==1).mean()]), 0.01, 0.99)\n\n        th0, th1, se0, se1 = method_oracle(data, s)\n        rows.append(make_row('oracle', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_naive(data, s)\n        rows.append(make_row('naive', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_global_corrected(data, s, C_global, p_z_global, p_zh_global)\n        rows.append(make_row('global_corrected', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_stratified_mle(data, s, C_mle[s], p_z_s, p_zh_s)\n        rows.append(make_row('stratified_mle', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_ec_hte(data, s, C_hb[s], p_z_s, p_zh_s)\n        rows.append(make_row('ec_hte', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_mi_rubin(data, s, M=20, seed=seed * 1000 + s)\n        rows.append(make_row('mi_rubin', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_ppci(data, s)\n        rows.append(make_row('ppci', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_ec_hte_ppci(data, s, C_hb[s], p_z_s, p_zh_s)\n        rows.append(make_row('ec_hte_ppci', s, th0, th1, se0, se1))\n\n    return rows\n\n\ndef aggregate_results(df):\n    \"\"\"Aggregate per-run results into summary statistics.\"\"\"\n    rows = []\n    group_cols = ['regime', 'n_expert', 'k_subgroups', 'sigma_outcome', 'dgp', 'subgroup', 'method']\n    for keys, grp in df.groupby(group_cols):\n        row = dict(zip(group_cols, keys))\n        for z in ['z0', 'z1']:\n            err = grp[f'tau_hat_{z}'] - grp[f'tau_true_{z}']\n            valid = err.dropna()\n            if len(valid) == 0:\n                row.update({f'bias_{z}': np.nan, f'rmse_{z}': np.nan, f'coverage_{z}': np.nan})\n                continue\n            row[f'bias_{z}'] = valid.mean()\n            row[f'rmse_{z}'] = np.sqrt((valid**2).mean())\n            covered = ((grp[f'ci_lower_{z}'] <= grp[f'tau_true_{z}']) &\n                       (grp[f'tau_true_{z}'] <= grp[f'ci_upper_{z}'])).mean()\n            row[f'coverage_{z}'] = covered\n            row[f'bias_{z}_se'] = valid.std() / np.sqrt(len(valid))\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\ndef run_simulation(n_mc, k_list=[2, 4], sigma_list=None, dgp_list=None, verbose=True):\n    \"\"\"Run full simulation sweep over DGP configs.\"\"\"\n    if sigma_list is None:\n        sigma_list = OUTCOME_NOISE_LEVELS\n    if dgp_list is None:\n        dgp_list = list(DGP_CONFIGS.keys())\n    results = []\n    configs = []\n    for regime_name in REGIMES:\n        for k in k_list:\n            misclass = MISCLASS_K2[regime_name] if k == 2 else MISCLASS_K4[regime_name]\n            for ne in N_EXPERTS:\n                for sigma in sigma_list:\n                    for dgp_name in dgp_list:\n                        configs.append((regime_name, k, misclass, ne, sigma, dgp_name))\n\n    total = len(configs) * n_mc\n    count = 0\n    t0 = time.time()\n\n    for regime_name, k, misclass, ne, sigma, dgp_name in configs:\n        dgp_cfg = DGP_CONFIGS[dgp_name]\n        outcome_bias = OUTCOME_BIAS[regime_name]\n        if k == 2:\n            outcome_bias_k = outcome_bias[:2]\n        else:\n            outcome_bias_k = outcome_bias[:k]\n\n        for mc in range(n_mc):\n            rows = run_one_mc(regime_name, REGIMES[regime_name], misclass, ne, k, seed=mc,\n                              sigma_outcome=sigma, dgp_name=dgp_name, dgp_cfg=dgp_cfg,\n                              outcome_bias_per_subgroup=outcome_bias_k)\n            results.extend(rows)\n            count += 1\n            if verbose and count % max(1, total // 20) == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / count * (total - count)\n                print(f\"  [{count}/{total}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s | {dgp_name} k={k} {regime_name} ne={ne} sigma={sigma} mc={mc}\")\n\n    return pd.DataFrame(results), time.time() - t0\n\n\nif __name__ == '__main__':\n    dry_run = '--dry-run' in sys.argv\n    args = [a for a in sys.argv[1:] if a != '--dry-run']\n    n_mc = int(args[0]) if args else N_MC\n\n    if dry_run:\n        n_mc = 1\n        sigma_list = [0.5]\n        k_list = [2]\n        dgp_list = list(DGP_CONFIGS.keys())\n    else:\n        sigma_list = None\n        k_list = [2, 4]\n        dgp_list = None\n\n    methods_str = 'oracle, naive, global_corrected, stratified_mle, ec_hte, mi_rubin, ppci, ec_hte_ppci'\n    print(f\"exp-007: PPCI + EC-HTE 4-DGP Matrix\")\n    print(f\"N={N}, N_MC={n_mc}\")\n    print(f\"Methods: {methods_str}\")\n    print(f\"DGPs: {dgp_list if dgp_list else list(DGP_CONFIGS.keys())}\")\n    print(f\"Outcome noise levels: {sigma_list if sigma_list else OUTCOME_NOISE_LEVELS}\")\n    print(f\"Note: ec_hte currently uses MLE fallback (HB placeholder)\")\n    if dry_run:\n        print(f\"** DRY RUN: 1 MC, k=[2], sigma=[0.5], all 4 DGPs **\")\n    print()\n\n    df_raw, elapsed = run_simulation(n_mc, k_list=k_list, sigma_list=sigma_list,\n                                     dgp_list=dgp_list)\n    df_agg = aggregate_results(df_raw)\n\n    raw_path = 'results/exp007_ppci_dsl_raw.csv'\n    agg_path = 'results/exp007_ppci_dsl.csv'\n    df_raw.to_csv(raw_path, index=False)\n    df_agg.to_csv(agg_path, index=False)\n\n    print(f\"\\nTotal time: {elapsed:.1f}s\")\n    print(f\"Saved: {raw_path}, {agg_path}\")\n\n    pd.set_option('display.max_columns', 20)\n    pd.set_option('display.width', 240)\n    pd.set_option('display.float_format', '{:.4f}'.format)\n\n    for dgp in (dgp_list or list(DGP_CONFIGS.keys())):\n        for regime in REGIMES:\n            print(f\"\\n{'='*140}\")\n            print(f\"DGP: {dgp} | Regime: {regime}\")\n            print(f\"{'='*140}\")\n            sub = df_agg[(df_agg['regime'] == regime) & (df_agg['dgp'] == dgp)]\n            if sub.empty:\n                continue\n            cols = ['n_expert', 'k_subgroups', 'sigma_outcome', 'subgroup', 'method',\n                    'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1']\n            print(sub[cols].to_string(index=False))\n",
    "structuredPatch": [
      {
        "oldStart": 326,
        "oldLines": 13,
        "newStart": 326,
        "newLines": 16,
        "lines": [
          " def method_ppci(data, s_val):",
          "     \"\"\"PPI rectifier for CATE estimation.",
          " ",
          "-    Corrects outcome-side bias using a gold-standard expert subset.",
          "-    Gold subset has access to BOTH true Z and true Y (Y_true).",
          "+    General-purpose correction using a gold-standard expert subset.",
          "+    The rectifier captures ALL systematic error (covariate + outcome) between",
          "+    the gold estimate (true Z, true Y) and the noisy estimate (Z_hat, observed Y).",
          "+    This is complementary to EC-HTE's structured covariate-only correction via M^{-1}.",
          "+",
          "     For each subgroup s and Z-level z:",
          "       1. tau_hat_all(z,s) = CATE from ALL data using Z_hat and observed Y",
          "       2. tau_gold(z,s) = CATE from GOLD subset using true Z and true Y",
          "       3. tau_hat_gold(z,s) = CATE from GOLD subset using Z_hat and observed Y",
          "-      4. rectifier = tau_gold - tau_hat_gold",
          "+      4. rectifier = tau_gold - tau_hat_gold  (captures covariate + outcome error)",
          "       5. tau_ppci = tau_hat_all + rectifier",
          "     \"\"\"",
          "     Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']"
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

Now the main fix — change the rectifier in `method_ec_hte_ppci` to use true Z grouping:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "be63d119-8b78-462a-8ab9-6c186a96371e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoUGo5UgqPVfzDjVioddiQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 32782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 617
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

<details open><summary>🔧 Tool call — Edit · `toolu_01Wk7G3jshfPi9wo5wQRoFcd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py",
  "old_string": "    results_z = {}\n    for idx, z_val in enumerate([0, 1]):\n        gold_z_mask = (Z_true_s == z_val)\n        gold_indices = expert_s_indices[gold_z_mask]\n\n        if len(gold_indices) < 4:\n            results_z[z_val] = (tau_ec[idx], se_ec[idx])\n            continue\n\n        # tau_gold: true Z + true Y on gold subset\n        gold_bool = np.zeros(len(Y), dtype=bool)\n        gold_bool[gold_indices] = True\n        tau_gold, se_gold = diff_in_means(Y_true, T, gold_bool)\n\n        # tau_hat_gold: Z_hat + observed Y on gold subset\n        gold_zhat_mask = (Z_hat[expert_s_indices] == z_val)\n        gold_zhat_indices = expert_s_indices[gold_zhat_mask]\n        gold_zhat_bool = np.zeros(len(Y), dtype=bool)\n        gold_zhat_bool[gold_zhat_indices] = True\n        tau_hat_gold, se_hat_gold = diff_in_means(Y, T, gold_zhat_bool)\n\n        if np.isnan(tau_gold) or np.isnan(tau_hat_gold):\n            results_z[z_val] = (tau_ec[idx], se_ec[idx])\n            continue\n\n        rectifier = tau_gold - tau_hat_gold\n        tau_combined = tau_ec[idx] + rectifier\n        se_combined = np.sqrt(se_ec[idx]**2 + se_gold**2 + se_hat_gold**2)\n        results_z[z_val] = (tau_combined, se_combined)",
  "new_string": "    results_z = {}\n    for idx, z_val in enumerate([0, 1]):\n        gold_z_mask = (Z_true_s == z_val)\n        gold_indices = expert_s_indices[gold_z_mask]\n\n        if len(gold_indices) < 4:\n            results_z[z_val] = (tau_ec[idx], se_ec[idx])\n            continue\n\n        gold_bool = np.zeros(len(Y), dtype=bool)\n        gold_bool[gold_indices] = True\n\n        # tau_gold: true Z + true Y → no error\n        tau_gold, se_gold = diff_in_means(Y_true, T, gold_bool)\n\n        # tau_hat_gold_true_z: true Z + observed Y → only outcome error remains\n        tau_hat_gold_true_z, se_hat_gold = diff_in_means(Y, T, gold_bool)\n\n        if np.isnan(tau_gold) or np.isnan(tau_hat_gold_true_z):\n            results_z[z_val] = (tau_ec[idx], se_ec[idx])\n            continue\n\n        # rectifier captures outcome error only (covariate error already handled by M^{-1})\n        rectifier = tau_gold - tau_hat_gold_true_z\n        tau_combined = tau_ec[idx] + rectifier\n        se_combined = np.sqrt(se_ec[idx]**2 + se_gold**2 + se_hat_gold**2)\n        results_z[z_val] = (tau_combined, se_combined)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "725c41f9-d36e-4b8e-8143-1b3e03c04b06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JoUGo5UgqPVfzDjVioddiQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 32782,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 617
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

_source line 15 · 2026-05-20T22:32:46.372Z_

<details><summary>↩ Tool result · `toolu_01Wk7G3jshfPi9wo5wQRoFcd`</summary>

```text
The file /home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "64779f38-3a5d-4588-9dd5-6eee3ca9bebd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py",
    "oldString": "    results_z = {}\n    for idx, z_val in enumerate([0, 1]):\n        gold_z_mask = (Z_true_s == z_val)\n        gold_indices = expert_s_indices[gold_z_mask]\n\n        if len(gold_indices) < 4:\n            results_z[z_val] = (tau_ec[idx], se_ec[idx])\n            continue\n\n        # tau_gold: true Z + true Y on gold subset\n        gold_bool = np.zeros(len(Y), dtype=bool)\n        gold_bool[gold_indices] = True\n        tau_gold, se_gold = diff_in_means(Y_true, T, gold_bool)\n\n        # tau_hat_gold: Z_hat + observed Y on gold subset\n        gold_zhat_mask = (Z_hat[expert_s_indices] == z_val)\n        gold_zhat_indices = expert_s_indices[gold_zhat_mask]\n        gold_zhat_bool = np.zeros(len(Y), dtype=bool)\n        gold_zhat_bool[gold_zhat_indices] = True\n        tau_hat_gold, se_hat_gold = diff_in_means(Y, T, gold_zhat_bool)\n\n        if np.isnan(tau_gold) or np.isnan(tau_hat_gold):\n            results_z[z_val] = (tau_ec[idx], se_ec[idx])\n            continue\n\n        rectifier = tau_gold - tau_hat_gold\n        tau_combined = tau_ec[idx] + rectifier\n        se_combined = np.sqrt(se_ec[idx]**2 + se_gold**2 + se_hat_gold**2)\n        results_z[z_val] = (tau_combined, se_combined)",
    "newString": "    results_z = {}\n    for idx, z_val in enumerate([0, 1]):\n        gold_z_mask = (Z_true_s == z_val)\n        gold_indices = expert_s_indices[gold_z_mask]\n\n        if len(gold_indices) < 4:\n            results_z[z_val] = (tau_ec[idx], se_ec[idx])\n            continue\n\n        gold_bool = np.zeros(len(Y), dtype=bool)\n        gold_bool[gold_indices] = True\n\n        # tau_gold: true Z + true Y → no error\n        tau_gold, se_gold = diff_in_means(Y_true, T, gold_bool)\n\n        # tau_hat_gold_true_z: true Z + observed Y → only outcome error remains\n        tau_hat_gold_true_z, se_hat_gold = diff_in_means(Y, T, gold_bool)\n\n        if np.isnan(tau_gold) or np.isnan(tau_hat_gold_true_z):\n            results_z[z_val] = (tau_ec[idx], se_ec[idx])\n            continue\n\n        # rectifier captures outcome error only (covariate error already handled by M^{-1})\n        rectifier = tau_gold - tau_hat_gold_true_z\n        tau_combined = tau_ec[idx] + rectifier\n        se_combined = np.sqrt(se_ec[idx]**2 + se_gold**2 + se_hat_gold**2)\n        results_z[z_val] = (tau_combined, se_combined)",
    "originalFile": "\"\"\"\nexp-007: PPCI + Stratified MLE Baseline Comparison for EC-HTE\nCompares measurement-model-level correction (EC-HTE) vs estimand-level correction (Stratified MLE)\nvs standard PPCI approach. DGP uses pure covariate-error: only Z has LLM misclassification.\nOutcome Y can optionally have measurement error (sigma_outcome > 0).\n\nFix (2026-05-20): method_ec_hte_ppci double-correction bug.\n  Rectifier was using Z_hat grouping on gold subset, capturing both covariate and outcome error.\n  Since M^{-1} already corrects covariate error, this caused double correction under DGP A/C.\n  Fixed: rectifier now uses true Z grouping on gold subset so it only captures outcome error.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nimport sys\nimport time\nimport warnings\nwarnings.filterwarnings('ignore')\n\n# === DGP ===\n\nREGIMES = {\n    'extreme':     {'tau_z1': 0.5, 'tau_z0': 0.1},\n    'moderate':    {'tau_z1': 0.3, 'tau_z0': 0.15},\n    'homogeneous': {'tau_z1': 0.25, 'tau_z0': 0.20},\n}\n\nMISCLASS_K2 = {\n    'extreme':     [0.25, 0.05],\n    'moderate':    [0.15, 0.10],\n    'homogeneous': [0.12, 0.12],\n}\n\nMISCLASS_K4 = {\n    'extreme':     [0.30, 0.20, 0.10, 0.03],\n    'moderate':    [0.20, 0.15, 0.10, 0.05],\n    'homogeneous': [0.12, 0.12, 0.12, 0.12],\n}\n\nOUTCOME_BIAS = {\n    'extreme':     [0.3, 0.1, 0.5, 0.2],\n    'moderate':    [0.15, 0.05, 0.25, 0.10],\n    'homogeneous': [0.1, 0.1, 0.1, 0.1],\n}\n\nDGP_CONFIGS = {\n    'A_covariate_only':  {'has_covariate_error': True,  'has_outcome_error': False},\n    'B_outcome_only':    {'has_covariate_error': False, 'has_outcome_error': True},\n    'C_both_errors':     {'has_covariate_error': True,  'has_outcome_error': True},\n    'D_no_error':        {'has_covariate_error': False, 'has_outcome_error': False},\n}\n\nN = 5000\nN_EXPERTS = [50, 100, 250, 500]\nN_MC = 100\nOUTCOME_NOISE_LEVELS = [0.0, 0.5, 1.0]\n\n\ndef generate_data(regime_params, misclass_rates, n_expert, k_subgroups, seed,\n                  sigma_outcome=0.0, outcome_noise_heterogeneous=True,\n                  has_covariate_error=True, has_outcome_error=False,\n                  outcome_bias_per_subgroup=None):\n    \"\"\"Generate synthetic data with configurable covariate and outcome error.\n\n    DGP A (covariate only): Z_hat has misclassification, Y = Y_true\n    DGP B (outcome only): Z_hat = Z, Y has treatment-differential bias\n    DGP C (both): Z_hat has misclassification AND Y has bias\n    DGP D (no error): Z_hat = Z, Y = Y_true\n    \"\"\"\n    rng = np.random.RandomState(seed)\n    k = k_subgroups\n\n    T = rng.binomial(1, 0.5, N)\n    Z = rng.binomial(1, 0.5, N)\n    S = rng.choice(k, N, p=[1/k]*k)\n    X = rng.randn(N, 5)\n\n    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])\n    eps = rng.randn(N)\n    Y_true = 1 + tau * T + 0.5 * X[:, 0] + eps\n    Y = Y_true.copy()\n\n    if has_outcome_error:\n        if outcome_bias_per_subgroup is not None:\n            for i in range(k):\n                s_mask = (S == i)\n                bias_i = outcome_bias_per_subgroup[i] if i < len(outcome_bias_per_subgroup) else outcome_bias_per_subgroup[-1]\n                Y[s_mask] += bias_i * T[s_mask]\n        if sigma_outcome > 0:\n            for i in range(k):\n                s_mask = (S == i)\n                noise_scale = sigma_outcome * (1 + 0.5 * i / max(k - 1, 1))\n                Y[s_mask] += rng.normal(0, noise_scale, s_mask.sum())\n\n    if has_covariate_error:\n        mc_rates = np.array([misclass_rates[s] for s in S])\n        flip = rng.rand(N) < mc_rates\n        Z_hat = np.where(flip, 1 - Z, Z)\n    else:\n        Z_hat = Z.copy()\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'X': X, 'Y': Y,\n        'Y_true': Y_true, 'tau': tau, 'expert_mask': expert_mask,\n    }\n\n\n# === Confusion Matrix Estimators ===\n\ndef estimate_cm_mle(z_true, z_hat):\n    \"\"\"MLE confusion matrix with Laplace smoothing. C[z, z_hat] = P(Z_hat=z_hat | Z=z).\"\"\"\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (mask.sum() + 2)\n    return C\n\n\ndef estimate_cm_hb(z_true, z_hat, all_subgroup_data):\n    \"\"\"Hierarchical Bayesian confusion matrix estimator (placeholder).\n\n    # TODO: integrate HB from exp001 after MCMC fix\n    Uses Dirichlet-Multinomial hierarchical model with partial pooling across subgroups.\n    \"\"\"\n    return estimate_cm_mle(z_true, z_hat)\n\n\n# === Correction Methods ===\n\ndef diff_in_means(Y, T, mask):\n    \"\"\"Difference-in-means estimator for subpopulation defined by mask.\"\"\"\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    \"\"\"M[z_hat, z] = P(Z=z | Z_hat=z_hat) via Bayes' rule.\"\"\"\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh]\n    return M\n\n\ndef invert_mixing(M, tau_obs, se_obs):\n    \"\"\"Apply M^{-1} correction. Returns (tau_corrected, se_corrected).\"\"\"\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    M_inv = np.linalg.inv(M)\n    tau_corrected = M_inv @ tau_obs\n    sigma_obs = np.diag(se_obs ** 2)\n    sigma_corrected = M_inv @ sigma_obs @ M_inv.T\n    se_corrected = np.sqrt(np.diag(sigma_corrected))\n    return tau_corrected, se_corrected\n\n\ndef method_oracle(data, s_val):\n    \"\"\"Oracle: use true Z within subgroup s.\"\"\"\n    Y, T, Z, S = data['Y'], data['T'], data['Z'], data['S']\n    s_mask = S == s_val\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z == 1))\n    return th0, th1, se0, se1\n\n\ndef method_naive(data, s_val):\n    \"\"\"Naive: use Z_hat within subgroup s, no correction.\"\"\"\n    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']\n    s_mask = S == s_val\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    return th0, th1, se0, se1\n\n\ndef method_global_corrected(data, s_val, C_global, p_z_global, p_zh_global):\n    \"\"\"Global-corrected: use global M_global^{-1} on subgroup-level observed CATEs.\"\"\"\n    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']\n    s_mask = S == s_val\n\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    if np.isnan(th0) or np.isnan(th1):\n        return np.nan, np.nan, np.nan, np.nan\n\n    M = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n    tau_corr, se_corr = invert_mixing(M, np.array([th0, th1]), np.array([se0, se1]))\n    return tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]\n\n\ndef method_stratified_mle(data, s_val, C_s, p_z_s, p_zh_s):\n    \"\"\"Stratified MLE: per-subgroup independent correction.\n\n    Each subgroup estimates its own confusion matrix independently (no pooling).\n    This is estimand-level correction -- correct the CATE estimate directly\n    using the subgroup's own confusion matrix.\n\n    Key difference from EC-HTE: no cross-subgroup shrinkage.\n    When n_expert is small per subgroup, Stratified MLE has high variance.\n    \"\"\"\n    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']\n    s_mask = S == s_val\n\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    if np.isnan(th0) or np.isnan(th1):\n        return np.nan, np.nan, np.nan, np.nan\n\n    M_s = build_mixing_matrix(C_s, p_z_s, p_zh_s)\n    tau_corr, se_corr = invert_mixing(M_s, np.array([th0, th1]), np.array([se0, se1]))\n    return tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]\n\n\ndef method_ec_hte(data, s_val, C_s_hb, p_z_s, p_zh_s):\n    \"\"\"EC-HTE: hierarchical Bayesian confusion matrix + subgroup correction.\n\n    Uses HB estimator (partial pooling) for confusion matrix, then applies\n    subgroup-level correction. The key advantage over Stratified MLE is that the\n    confusion matrix estimate borrows strength across subgroups.\n\n    # TODO: integrate HB from exp001 after MCMC fix\n    Currently falls back to MLE (same as Stratified MLE) until HB is integrated.\n    \"\"\"\n    Y, T, Z_hat, S = data['Y'], data['T'], data['Z_hat'], data['S']\n    s_mask = S == s_val\n\n    th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    if np.isnan(th0) or np.isnan(th1):\n        return np.nan, np.nan, np.nan, np.nan\n\n    M_s = build_mixing_matrix(C_s_hb, p_z_s, p_zh_s)\n    tau_corr, se_corr = invert_mixing(M_s, np.array([th0, th1]), np.array([se0, se1]))\n    return tau_corr[0], tau_corr[1], se_corr[0], se_corr[1]\n\n\ndef method_mi_rubin(data, s_val, M=20, seed=0):\n    \"\"\"Multiple Imputation with Rubin's rules (formerly called PPCI).\n\n    For each non-expert observation, impute Z from P(Z|Z_hat, S) estimated\n    on expert data. Repeat M times, compute CATE on each imputed dataset,\n    then combine estimates using Rubin's rules.\n    \"\"\"\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n    rng = np.random.RandomState(seed)\n\n    s_mask = S == s_val\n    expert_s = expert_mask & s_mask\n\n    if expert_s.sum() < 4:\n        return np.nan, np.nan, np.nan, np.nan\n\n    p_z1_given_zhat = {}\n    for z_hat_val in [0, 1]:\n        expert_zhat = expert_s & (Z_hat == z_hat_val)\n        if expert_zhat.sum() > 0:\n            p_z1_given_zhat[z_hat_val] = np.clip(Z[expert_zhat].mean(), 0.01, 0.99)\n        else:\n            p_z1_given_zhat[z_hat_val] = float(z_hat_val)\n\n    Y_s = Y[s_mask]\n    T_s = T[s_mask]\n    Z_hat_s = Z_hat[s_mask]\n    is_expert_s = expert_mask[s_mask]\n    Z_true_s = Z[s_mask]\n    non_expert_s = ~is_expert_s\n\n    tau_z0_list, tau_z1_list = [], []\n    var_z0_list, var_z1_list = [], []\n\n    for m_iter in range(M):\n        Z_imp = Z_hat_s.copy().astype(float)\n        Z_imp[is_expert_s] = Z_true_s[is_expert_s]\n        if non_expert_s.any():\n            probs = np.array([p_z1_given_zhat[zh] for zh in Z_hat_s[non_expert_s]])\n            Z_imp[non_expert_s] = rng.binomial(1, probs).astype(float)\n\n        for z_val, tau_list, var_list in [(0, tau_z0_list, var_z0_list),\n                                          (1, tau_z1_list, var_z1_list)]:\n            z_mask = Z_imp == z_val\n            t1 = z_mask & (T_s == 1)\n            t0 = z_mask & (T_s == 0)\n            n1, n0 = t1.sum(), t0.sum()\n            if n1 < 2 or n0 < 2:\n                tau_list.append(np.nan)\n                var_list.append(np.nan)\n            else:\n                y1, y0 = Y_s[t1], Y_s[t0]\n                tau_hat = y1.mean() - y0.mean()\n                v = y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0\n                tau_list.append(tau_hat)\n                var_list.append(v)\n\n    def rubins_combine(tau_list, var_list):\n        valid = [(t, v) for t, v in zip(tau_list, var_list)\n                 if not np.isnan(t) and not np.isnan(v)]\n        if len(valid) < 2:\n            return np.nan, np.nan\n        taus = np.array([t for t, v in valid])\n        vars_ = np.array([v for t, v in valid])\n        m_eff = len(valid)\n        tau_bar = taus.mean()\n        W = vars_.mean()\n        B = taus.var(ddof=1)\n        V_total = W + (1 + 1.0 / m_eff) * B\n        return tau_bar, np.sqrt(max(V_total, 0))\n\n    th0, se0 = rubins_combine(tau_z0_list, var_z0_list)\n    th1, se1 = rubins_combine(tau_z1_list, var_z1_list)\n    return th0, th1, se0, se1\n\n\ndef method_ppci(data, s_val):\n    \"\"\"PPI rectifier for CATE estimation.\n\n    General-purpose correction using a gold-standard expert subset.\n    The rectifier captures ALL systematic error (covariate + outcome) between\n    the gold estimate (true Z, true Y) and the noisy estimate (Z_hat, observed Y).\n    This is complementary to EC-HTE's structured covariate-only correction via M^{-1}.\n\n    For each subgroup s and Z-level z:\n      1. tau_hat_all(z,s) = CATE from ALL data using Z_hat and observed Y\n      2. tau_gold(z,s) = CATE from GOLD subset using true Z and true Y\n      3. tau_hat_gold(z,s) = CATE from GOLD subset using Z_hat and observed Y\n      4. rectifier = tau_gold - tau_hat_gold  (captures covariate + outcome error)\n      5. tau_ppci = tau_hat_all + rectifier\n    \"\"\"\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    Y_true = data['Y_true']\n    expert_mask = data['expert_mask']\n\n    s_mask = S == s_val\n    expert_s = expert_mask & s_mask\n    n_expert_s = expert_s.sum()\n\n    if n_expert_s < 10:\n        th0, se0 = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n        th1, se1 = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n        return th0, th1, se0, se1\n\n    expert_s_indices = np.where(expert_s)[0]\n    Z_true_s = Z[expert_s_indices]\n\n    results_z = {}\n    for z_val in [0, 1]:\n        all_mask = s_mask & (Z_hat == z_val)\n        tau_hat_all, se_hat_all = diff_in_means(Y, T, all_mask)\n\n        gold_mask_z = (Z_true_s == z_val)\n        gold_indices = expert_s_indices[gold_mask_z]\n\n        if len(gold_indices) < 4:\n            results_z[z_val] = (tau_hat_all, se_hat_all)\n            continue\n\n        # tau_gold: use true Z and true Y on gold subset\n        gold_bool = np.zeros(len(Y), dtype=bool)\n        gold_bool[gold_indices] = True\n        tau_gold, se_gold = diff_in_means(Y_true, T, gold_bool)\n\n        # tau_hat_gold: use Z_hat and observed Y on gold subset (same people)\n        gold_zhat_mask = (Z_hat[expert_s_indices] == z_val)\n        gold_zhat_indices = expert_s_indices[gold_zhat_mask]\n        gold_zhat_bool = np.zeros(len(Y), dtype=bool)\n        gold_zhat_bool[gold_zhat_indices] = True\n        tau_hat_gold, se_hat_gold = diff_in_means(Y, T, gold_zhat_bool)\n\n        if np.isnan(tau_gold) or np.isnan(tau_hat_gold) or np.isnan(tau_hat_all):\n            results_z[z_val] = (tau_hat_all, se_hat_all)\n            continue\n\n        rectifier = tau_gold - tau_hat_gold\n        tau_ppci = tau_hat_all + rectifier\n        se_ppci = np.sqrt(se_hat_all**2 + se_gold**2 + se_hat_gold**2)\n        results_z[z_val] = (tau_ppci, se_ppci)\n\n    th0, se0 = results_z.get(0, (np.nan, np.nan))\n    th1, se1 = results_z.get(1, (np.nan, np.nan))\n    return th0, th1, se0, se1\n\n\ndef method_ec_hte_ppci(data, s_val, C_s, p_z_s, p_zh_s):\n    \"\"\"EC-HTE + PPCI: correct covariate error via M^{-1}, then apply PPI rectifier for outcome error.\"\"\"\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    Y_true = data['Y_true']\n    expert_mask = data['expert_mask']\n\n    s_mask = S == s_val\n    expert_s = expert_mask & s_mask\n\n    th0_obs, se0_obs = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1_obs, se1_obs = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    if np.isnan(th0_obs) or np.isnan(th1_obs):\n        return np.nan, np.nan, np.nan, np.nan\n\n    M_s = build_mixing_matrix(C_s, p_z_s, p_zh_s)\n    tau_ec, se_ec = invert_mixing(M_s, np.array([th0_obs, th1_obs]),\n                                  np.array([se0_obs, se1_obs]))\n\n    n_expert_s = expert_s.sum()\n    if n_expert_s < 10:\n        return tau_ec[0], tau_ec[1], se_ec[0], se_ec[1]\n\n    expert_s_indices = np.where(expert_s)[0]\n    Z_true_s = Z[expert_s_indices]\n\n    results_z = {}\n    for idx, z_val in enumerate([0, 1]):\n        gold_z_mask = (Z_true_s == z_val)\n        gold_indices = expert_s_indices[gold_z_mask]\n\n        if len(gold_indices) < 4:\n            results_z[z_val] = (tau_ec[idx], se_ec[idx])\n            continue\n\n        # tau_gold: true Z + true Y on gold subset\n        gold_bool = np.zeros(len(Y), dtype=bool)\n        gold_bool[gold_indices] = True\n        tau_gold, se_gold = diff_in_means(Y_true, T, gold_bool)\n\n        # tau_hat_gold: Z_hat + observed Y on gold subset\n        gold_zhat_mask = (Z_hat[expert_s_indices] == z_val)\n        gold_zhat_indices = expert_s_indices[gold_zhat_mask]\n        gold_zhat_bool = np.zeros(len(Y), dtype=bool)\n        gold_zhat_bool[gold_zhat_indices] = True\n        tau_hat_gold, se_hat_gold = diff_in_means(Y, T, gold_zhat_bool)\n\n        if np.isnan(tau_gold) or np.isnan(tau_hat_gold):\n            results_z[z_val] = (tau_ec[idx], se_ec[idx])\n            continue\n\n        rectifier = tau_gold - tau_hat_gold\n        tau_combined = tau_ec[idx] + rectifier\n        se_combined = np.sqrt(se_ec[idx]**2 + se_gold**2 + se_hat_gold**2)\n        results_z[z_val] = (tau_combined, se_combined)\n\n    th0, se0 = results_z.get(0, (np.nan, np.nan))\n    th1, se1 = results_z.get(1, (np.nan, np.nan))\n    return th0, th1, se0, se1\n\n\n# === Main Simulation Loop ===\n\ndef run_one_mc(regime_name, regime_params, misclass_rates, n_expert, k_subgroups, seed,\n               sigma_outcome=0.0, dgp_name='A_covariate_only', dgp_cfg=None,\n               outcome_bias_per_subgroup=None):\n    \"\"\"Run one MC iteration for all methods.\"\"\"\n    if dgp_cfg is None:\n        dgp_cfg = DGP_CONFIGS[dgp_name]\n\n    data = generate_data(regime_params, misclass_rates, n_expert, k_subgroups, seed,\n                         sigma_outcome=sigma_outcome,\n                         has_covariate_error=dgp_cfg['has_covariate_error'],\n                         has_outcome_error=dgp_cfg['has_outcome_error'],\n                         outcome_bias_per_subgroup=outcome_bias_per_subgroup)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n    tau_true_z0, tau_true_z1 = regime_params['tau_z0'], regime_params['tau_z1']\n\n    C_global = estimate_cm_mle(Z[expert_mask], Z_hat[expert_mask])\n    p_z_global = np.clip(np.array([(Z[expert_mask]==0).mean(), (Z[expert_mask]==1).mean()]), 0.01, 0.99)\n    p_zh_global = np.clip(np.array([(Z_hat==0).mean(), (Z_hat==1).mean()]), 0.01, 0.99)\n\n    C_mle = {}\n    C_hb = {}\n    all_subgroup_expert_data = []\n\n    for s in range(k_subgroups):\n        s_mask = S == s\n        expert_s = expert_mask & s_mask\n        if expert_s.sum() >= 4:\n            C_mle[s] = estimate_cm_mle(Z[expert_s], Z_hat[expert_s])\n            all_subgroup_expert_data.append((Z[expert_s], Z_hat[expert_s]))\n        else:\n            C_mle[s] = C_global\n            all_subgroup_expert_data.append((Z[expert_mask], Z_hat[expert_mask]))\n\n    for s in range(k_subgroups):\n        s_mask = S == s\n        expert_s = expert_mask & s_mask\n        if expert_s.sum() >= 4:\n            C_hb[s] = estimate_cm_hb(Z[expert_s], Z_hat[expert_s], all_subgroup_expert_data)\n        else:\n            C_hb[s] = C_global\n\n    rows = []\n    base = {\n        'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k_subgroups,\n        'sigma_outcome': sigma_outcome, 'dgp': dgp_name,\n        'mc_run': seed, 'tau_true_z0': tau_true_z0, 'tau_true_z1': tau_true_z1,\n    }\n\n    def make_row(method, subgroup, th0, th1, se0, se1):\n        return {**base, 'method': method, 'subgroup': subgroup,\n                'tau_hat_z0': th0, 'tau_hat_z1': th1,\n                'ci_lower_z0': th0 - 1.96*se0 if not np.isnan(se0) else np.nan,\n                'ci_upper_z0': th0 + 1.96*se0 if not np.isnan(se0) else np.nan,\n                'ci_lower_z1': th1 - 1.96*se1 if not np.isnan(se1) else np.nan,\n                'ci_upper_z1': th1 + 1.96*se1 if not np.isnan(se1) else np.nan}\n\n    for s in range(k_subgroups):\n        s_mask = S == s\n        expert_s = expert_mask & s_mask\n        if expert_s.sum() >= 4:\n            p_z_s = np.clip(np.array([(Z[expert_s]==0).mean(), (Z[expert_s]==1).mean()]), 0.01, 0.99)\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.clip(np.array([(Z_hat[s_mask]==0).mean(), (Z_hat[s_mask]==1).mean()]), 0.01, 0.99)\n\n        th0, th1, se0, se1 = method_oracle(data, s)\n        rows.append(make_row('oracle', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_naive(data, s)\n        rows.append(make_row('naive', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_global_corrected(data, s, C_global, p_z_global, p_zh_global)\n        rows.append(make_row('global_corrected', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_stratified_mle(data, s, C_mle[s], p_z_s, p_zh_s)\n        rows.append(make_row('stratified_mle', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_ec_hte(data, s, C_hb[s], p_z_s, p_zh_s)\n        rows.append(make_row('ec_hte', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_mi_rubin(data, s, M=20, seed=seed * 1000 + s)\n        rows.append(make_row('mi_rubin', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_ppci(data, s)\n        rows.append(make_row('ppci', s, th0, th1, se0, se1))\n\n        th0, th1, se0, se1 = method_ec_hte_ppci(data, s, C_hb[s], p_z_s, p_zh_s)\n        rows.append(make_row('ec_hte_ppci', s, th0, th1, se0, se1))\n\n    return rows\n\n\ndef aggregate_results(df):\n    \"\"\"Aggregate per-run results into summary statistics.\"\"\"\n    rows = []\n    group_cols = ['regime', 'n_expert', 'k_subgroups', 'sigma_outcome', 'dgp', 'subgroup', 'method']\n    for keys, grp in df.groupby(group_cols):\n        row = dict(zip(group_cols, keys))\n        for z in ['z0', 'z1']:\n            err = grp[f'tau_hat_{z}'] - grp[f'tau_true_{z}']\n            valid = err.dropna()\n            if len(valid) == 0:\n                row.update({f'bias_{z}': np.nan, f'rmse_{z}': np.nan, f'coverage_{z}': np.nan})\n                continue\n            row[f'bias_{z}'] = valid.mean()\n            row[f'rmse_{z}'] = np.sqrt((valid**2).mean())\n            covered = ((grp[f'ci_lower_{z}'] <= grp[f'tau_true_{z}']) &\n                       (grp[f'tau_true_{z}'] <= grp[f'ci_upper_{z}'])).mean()\n            row[f'coverage_{z}'] = covered\n            row[f'bias_{z}_se'] = valid.std() / np.sqrt(len(valid))\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\ndef run_simulation(n_mc, k_list=[2, 4], sigma_list=None, dgp_list=None, verbose=True):\n    \"\"\"Run full simulation sweep over DGP configs.\"\"\"\n    if sigma_list is None:\n        sigma_list = OUTCOME_NOISE_LEVELS\n    if dgp_list is None:\n        dgp_list = list(DGP_CONFIGS.keys())\n    results = []\n    configs = []\n    for regime_name in REGIMES:\n        for k in k_list:\n            misclass = MISCLASS_K2[regime_name] if k == 2 else MISCLASS_K4[regime_name]\n            for ne in N_EXPERTS:\n                for sigma in sigma_list:\n                    for dgp_name in dgp_list:\n                        configs.append((regime_name, k, misclass, ne, sigma, dgp_name))\n\n    total = len(configs) * n_mc\n    count = 0\n    t0 = time.time()\n\n    for regime_name, k, misclass, ne, sigma, dgp_name in configs:\n        dgp_cfg = DGP_CONFIGS[dgp_name]\n        outcome_bias = OUTCOME_BIAS[regime_name]\n        if k == 2:\n            outcome_bias_k = outcome_bias[:2]\n        else:\n            outcome_bias_k = outcome_bias[:k]\n\n        for mc in range(n_mc):\n            rows = run_one_mc(regime_name, REGIMES[regime_name], misclass, ne, k, seed=mc,\n                              sigma_outcome=sigma, dgp_name=dgp_name, dgp_cfg=dgp_cfg,\n                              outcome_bias_per_subgroup=outcome_bias_k)\n            results.extend(rows)\n            count += 1\n            if verbose and count % max(1, total // 20) == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / count * (total - count)\n                print(f\"  [{count}/{total}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s | {dgp_name} k={k} {regime_name} ne={ne} sigma={sigma} mc={mc}\")\n\n    return pd.DataFrame(results), time.time() - t0\n\n\nif __name__ == '__main__':\n    dry_run = '--dry-run' in sys.argv\n    args = [a for a in sys.argv[1:] if a != '--dry-run']\n    n_mc = int(args[0]) if args else N_MC\n\n    if dry_run:\n        n_mc = 1\n        sigma_list = [0.5]\n        k_list = [2]\n        dgp_list = list(DGP_CONFIGS.keys())\n    else:\n        sigma_list = None\n        k_list = [2, 4]\n        dgp_list = None\n\n    methods_str = 'oracle, naive, global_corrected, stratified_mle, ec_hte, mi_rubin, ppci, ec_hte_ppci'\n    print(f\"exp-007: PPCI + EC-HTE 4-DGP Matrix\")\n    print(f\"N={N}, N_MC={n_mc}\")\n    print(f\"Methods: {methods_str}\")\n    print(f\"DGPs: {dgp_list if dgp_list else list(DGP_CONFIGS.keys())}\")\n    print(f\"Outcome noise levels: {sigma_list if sigma_list else OUTCOME_NOISE_LEVELS}\")\n    print(f\"Note: ec_hte currently uses MLE fallback (HB placeholder)\")\n    if dry_run:\n        print(f\"** DRY RUN: 1 MC, k=[2], sigma=[0.5], all 4 DGPs **\")\n    print()\n\n    df_raw, elapsed = run_simulation(n_mc, k_list=k_list, sigma_list=sigma_list,\n                                     dgp_list=dgp_list)\n    df_agg = aggregate_results(df_raw)\n\n    raw_path = 'results/exp007_ppci_dsl_raw.csv'\n    agg_path = 'results/exp007_ppci_dsl.csv'\n    df_raw.to_csv(raw_path, index=False)\n    df_agg.to_csv(agg_path, index=False)\n\n    print(f\"\\nTotal time: {elapsed:.1f}s\")\n    print(f\"Saved: {raw_path}, {agg_path}\")\n\n    pd.set_option('display.max_columns', 20)\n    pd.set_option('display.width', 240)\n    pd.set_option('display.float_format', '{:.4f}'.format)\n\n    for dgp in (dgp_list or list(DGP_CONFIGS.keys())):\n        for regime in REGIMES:\n            print(f\"\\n{'='*140}\")\n            print(f\"DGP: {dgp} | Regime: {regime}\")\n            print(f\"{'='*140}\")\n            sub = df_agg[(df_agg['regime'] == regime) & (df_agg['dgp'] == dgp)]\n            if sub.empty:\n                continue\n            cols = ['n_expert', 'k_subgroups', 'sigma_outcome', 'subgroup', 'method',\n                    'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1']\n            print(sub[cols].to_string(index=False))\n",
    "structuredPatch": [
      {
        "oldStart": 426,
        "oldLines": 23,
        "newStart": 426,
        "newLines": 21,
        "lines": [
          "             results_z[z_val] = (tau_ec[idx], se_ec[idx])",
          "             continue",
          " ",
          "-        # tau_gold: true Z + true Y on gold subset",
          "         gold_bool = np.zeros(len(Y), dtype=bool)",
          "         gold_bool[gold_indices] = True",
          "+",
          "+        # tau_gold: true Z + true Y → no error",
          "         tau_gold, se_gold = diff_in_means(Y_true, T, gold_bool)",
          " ",
          "-        # tau_hat_gold: Z_hat + observed Y on gold subset",
          "-        gold_zhat_mask = (Z_hat[expert_s_indices] == z_val)",
          "-        gold_zhat_indices = expert_s_indices[gold_zhat_mask]",
          "-        gold_zhat_bool = np.zeros(len(Y), dtype=bool)",
          "-        gold_zhat_bool[gold_zhat_indices] = True",
          "-        tau_hat_gold, se_hat_gold = diff_in_means(Y, T, gold_zhat_bool)",
          "+        # tau_hat_gold_true_z: true Z + observed Y → only outcome error remains",
          "+        tau_hat_gold_true_z, se_hat_gold = diff_in_means(Y, T, gold_bool)",
          " ",
          "-        if np.isnan(tau_gold) or np.isnan(tau_hat_gold):",
          "+        if np.isnan(tau_gold) or np.isnan(tau_hat_gold_true_z):",
          "             results_z[z_val] = (tau_ec[idx], se_ec[idx])",
          "             continue",
          " ",
          "-        rectifier = tau_gold - tau_hat_gold",
          "+        # rectifier captures outcome error only (covariate error already handled by M^{-1})",
          "+        rectifier = tau_gold - tau_hat_gold_true_z",
          "         tau_combined = tau_ec[idx] + rectifier",
          "         se_combined = np.sqrt(se_ec[idx]**2 + se_gold**2 + se_hat_gold**2)",
          "         results_z[z_val] = (tau_combined, se_combined)"
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

_source line 16_

Now let me verify the fix looks correct and run the validation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "e53dc8a1-122f-44dd-8cfe-37a3e95c5ffa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PpNYUWat8rooqZPnJawncF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1033,
      "cache_read_input_tokens": 33399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1033
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

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_014su5EnMzTk1Y1Wmsq8NCVc`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py",
  "offset": 390,
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "b45e746d-e177-4021-bbb5-fbabc51b9daa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PpNYUWat8rooqZPnJawncF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1033,
      "cache_read_input_tokens": 33399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1033
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

_source line 18 · 2026-05-20T22:32:49.929Z_

<details><summary>↩ Tool result · `toolu_014su5EnMzTk1Y1Wmsq8NCVc`</summary>

```text
390	    th0, se0 = results_z.get(0, (np.nan, np.nan))
391	    th1, se1 = results_z.get(1, (np.nan, np.nan))
392	    return th0, th1, se0, se1
393	
394	
395	def method_ec_hte_ppci(data, s_val, C_s, p_z_s, p_zh_s):
396	    """EC-HTE + PPCI: correct covariate error via M^{-1}, then apply PPI rectifier for outcome error."""
397	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
398	    Y_true = data['Y_true']
399	    expert_mask = data['expert_mask']
400	
401	    s_mask = S == s_val
402	    expert_s = expert_mask & s_mask
403	
404	    th0_obs, se0_obs = diff_in_means(Y, T, s_mask & (Z_hat == 0))
405	    th1_obs, se1_obs = diff_in_means(Y, T, s_mask & (Z_hat == 1))
406	    if np.isnan(th0_obs) or np.isnan(th1_obs):
407	        return np.nan, np.nan, np.nan, np.nan
408	
409	    M_s = build_mixing_matrix(C_s, p_z_s, p_zh_s)
410	    tau_ec, se_ec = invert_mixing(M_s, np.array([th0_obs, th1_obs]),
411	                                  np.array([se0_obs, se1_obs]))
412	
413	    n_expert_s = expert_s.sum()
414	    if n_expert_s < 10:
415	        return tau_ec[0], tau_ec[1], se_ec[0], se_ec[1]
416	
417	    expert_s_indices = np.where(expert_s)[0]
418	    Z_true_s = Z[expert_s_indices]
419	
420	    results_z = {}
421	    for idx, z_val in enumerate([0, 1]):
422	        gold_z_mask = (Z_true_s == z_val)
423	        gold_indices = expert_s_indices[gold_z_mask]
424	
425	        if len(gold_indices) < 4:
426	            results_z[z_val] = (tau_ec[idx], se_ec[idx])
427	            continue
428	
429	        gold_bool = np.zeros(len(Y), dtype=bool)
430	        gold_bool[gold_indices] = True
431	
432	        # tau_gold: true Z + true Y → no error
433	        tau_gold, se_gold = diff_in_means(Y_true, T, gold_bool)
434	
435	        # tau_hat_gold_true_z: true Z + observed Y → only outcome error remains
436	        tau_hat_gold_true_z, se_hat_gold = diff_in_means(Y, T, gold_bool)
437	
438	        if np.isnan(tau_gold) or np.isnan(tau_hat_gold_true_z):
439	            results_z[z_val] = (tau_ec[idx], se_ec[idx])
440	            continue
441	
442	        # rectifier captures outcome error only (covariate error already handled by M^{-1})
443	        rectifier = tau_gold - tau_hat_gold_true_z
444	        tau_combined = tau_ec[idx] + rectifier
445	        se_combined = np.sqrt(se_ec[idx]**2 + se_gold**2 + se_hat_gold**2)
446	        results_z[z_val] = (tau_combined, se_combined)
447	
448	    th0, se0 = results_z.get(0, (np.nan, np.nan))
449	    th1, se1 = results_z.get(1, (np.nan, np.nan))
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "5e380062-80f4-45c6-85ea-11397ac95b2d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py",
      "content": "    th0, se0 = results_z.get(0, (np.nan, np.nan))\n    th1, se1 = results_z.get(1, (np.nan, np.nan))\n    return th0, th1, se0, se1\n\n\ndef method_ec_hte_ppci(data, s_val, C_s, p_z_s, p_zh_s):\n    \"\"\"EC-HTE + PPCI: correct covariate error via M^{-1}, then apply PPI rectifier for outcome error.\"\"\"\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    Y_true = data['Y_true']\n    expert_mask = data['expert_mask']\n\n    s_mask = S == s_val\n    expert_s = expert_mask & s_mask\n\n    th0_obs, se0_obs = diff_in_means(Y, T, s_mask & (Z_hat == 0))\n    th1_obs, se1_obs = diff_in_means(Y, T, s_mask & (Z_hat == 1))\n    if np.isnan(th0_obs) or np.isnan(th1_obs):\n        return np.nan, np.nan, np.nan, np.nan\n\n    M_s = build_mixing_matrix(C_s, p_z_s, p_zh_s)\n    tau_ec, se_ec = invert_mixing(M_s, np.array([th0_obs, th1_obs]),\n                                  np.array([se0_obs, se1_obs]))\n\n    n_expert_s = expert_s.sum()\n    if n_expert_s < 10:\n        return tau_ec[0], tau_ec[1], se_ec[0], se_ec[1]\n\n    expert_s_indices = np.where(expert_s)[0]\n    Z_true_s = Z[expert_s_indices]\n\n    results_z = {}\n    for idx, z_val in enumerate([0, 1]):\n        gold_z_mask = (Z_true_s == z_val)\n        gold_indices = expert_s_indices[gold_z_mask]\n\n        if len(gold_indices) < 4:\n            results_z[z_val] = (tau_ec[idx], se_ec[idx])\n            continue\n\n        gold_bool = np.zeros(len(Y), dtype=bool)\n        gold_bool[gold_indices] = True\n\n        # tau_gold: true Z + true Y → no error\n        tau_gold, se_gold = diff_in_means(Y_true, T, gold_bool)\n\n        # tau_hat_gold_true_z: true Z + observed Y → only outcome error remains\n        tau_hat_gold_true_z, se_hat_gold = diff_in_means(Y, T, gold_bool)\n\n        if np.isnan(tau_gold) or np.isnan(tau_hat_gold_true_z):\n            results_z[z_val] = (tau_ec[idx], se_ec[idx])\n            continue\n\n        # rectifier captures outcome error only (covariate error already handled by M^{-1})\n        rectifier = tau_gold - tau_hat_gold_true_z\n        tau_combined = tau_ec[idx] + rectifier\n        se_combined = np.sqrt(se_ec[idx]**2 + se_gold**2 + se_hat_gold**2)\n        results_z[z_val] = (tau_combined, se_combined)\n\n    th0, se0 = results_z.get(0, (np.nan, np.nan))\n    th1, se1 = results_z.get(1, (np.nan, np.nan))",
      "numLines": 60,
      "startLine": 390,
      "totalLines": 665
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

Code looks correct. Running the validation — DGP A (covariate-only error), comparing `ec_hte` vs `ec_hte_ppci` bias across 5 MC runs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "bcc47d94-d51e-4e09-babe-c604654455bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012a1QGEmafeXkbpZwZ7yNdz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1209,
      "cache_read_input_tokens": 34432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1209
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

<details open><summary>🔧 Tool call — Bash · `toolu_01SJDwibtC5tGdtFRxM9q9yZ`</summary>

```json
{
  "command": "python -c \"\nimport exp007_ppci_dsl as m\nimport numpy as np\nimport pandas as pd\n\nnp.random.seed(42)\nregime = 'extreme'\nk = 2\nn_expert = 250\nsigma = 0.0\nn_mc = 5\n\nrows = []\nfor mc in range(n_mc):\n    r = m.run_one_mc(regime, m.REGIMES[regime], m.MISCLASS_K2[regime], n_expert, k, seed=mc,\n                     sigma_outcome=sigma, dgp_name='A_covariate_only',\n                     outcome_bias_per_subgroup=m.OUTCOME_BIAS[regime][:k])\n    rows.extend(r)\n\ndf = pd.DataFrame(rows)\ndf['bias_z0'] = df['tau_hat_z0'] - df['tau_true_z0']\ndf['bias_z1'] = df['tau_hat_z1'] - df['tau_true_z1']\n\nprint('DGP A (covariate-only error), extreme regime, n_expert=250, k=2, 5 MC runs')\nprint('Rectifier should be ~0 under DGP A (no outcome error)')\nprint()\nfor method in ['oracle', 'naive', 'ec_hte', 'ec_hte_ppci', 'ppci']:\n    sub = df[df['method'] == method]\n    b0 = sub['bias_z0'].mean()\n    b1 = sub['bias_z1'].mean()\n    print(f'{method:20s}  bias_z0={b0:+.4f}  bias_z1={b1:+.4f}')\n\"\n",
  "description": "Validate fix: compare ec_hte vs ec_hte_ppci bias under DGP A",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "7ea9d239-8574-4f8f-83eb-f27e3100083c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012a1QGEmafeXkbpZwZ7yNdz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1209,
      "cache_read_input_tokens": 34432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1209
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

_source line 21 · 2026-05-20T22:33:01.613Z_

<details><summary>↩ Tool result · reported error · `toolu_01SJDwibtC5tGdtFRxM9q9yZ`</summary>

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
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "d7b6aad2-ba78-49f8-b69c-92998e0bfb1a",
  "tool_use_result": "Error: Exit code 127\n/bin/bash: line 1: python: command not found"
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01WMbzR2LmFsvntj5wzdNwvj`</summary>

```json
{
  "command": "which python3 && python3 --version",
  "description": "Check python3 availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "c2322162-c7fb-4c3f-ac2d-e69752b9b515",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Btz5uKCU1HpmreunDCijAj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 35641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 718
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

### Tool result

_source line 23 · 2026-05-20T22:33:04.212Z_

<details><summary>↩ Tool result · `toolu_01WMbzR2LmFsvntj5wzdNwvj`</summary>

```text
/usr/bin/python3
Python 3.14.4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "604f5ec2-1369-43b7-97af-ab5df52951ae",
  "tool_use_result": {
    "stdout": "/usr/bin/python3\nPython 3.14.4",
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

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_01S8LtSNmU4ogPU4RgfiZM7x`</summary>

```json
{
  "command": "python3 -c \"\nimport exp007_ppci_dsl as m\nimport numpy as np\nimport pandas as pd\n\nnp.random.seed(42)\nregime = 'extreme'\nk = 2\nn_expert = 250\nsigma = 0.0\nn_mc = 5\n\nrows = []\nfor mc in range(n_mc):\n    r = m.run_one_mc(regime, m.REGIMES[regime], m.MISCLASS_K2[regime], n_expert, k, seed=mc,\n                     sigma_outcome=sigma, dgp_name='A_covariate_only',\n                     outcome_bias_per_subgroup=m.OUTCOME_BIAS[regime][:k])\n    rows.extend(r)\n\ndf = pd.DataFrame(rows)\ndf['bias_z0'] = df['tau_hat_z0'] - df['tau_true_z0']\ndf['bias_z1'] = df['tau_hat_z1'] - df['tau_true_z1']\n\nprint('DGP A (covariate-only error), extreme regime, n_expert=250, k=2, 5 MC runs')\nprint('Rectifier should be ~0 under DGP A (no outcome error)')\nprint()\nfor method in ['oracle', 'naive', 'ec_hte', 'ec_hte_ppci', 'ppci']:\n    sub = df[df['method'] == method]\n    b0 = sub['bias_z0'].mean()\n    b1 = sub['bias_z1'].mean()\n    print(f'{method:20s}  bias_z0={b0:+.4f}  bias_z1={b1:+.4f}')\n\"\n",
  "description": "Validate fix: compare ec_hte vs ec_hte_ppci bias under DGP A",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "26065bec-62b8-4777-a699-3bbbb81c6ecb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NnExyUpN617t1tsK5CKCv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 108,
      "cache_read_input_tokens": 36359,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 108
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

_source line 25 · 2026-05-20T22:33:11.635Z_

<details><summary>↩ Tool result · `toolu_01S8LtSNmU4ogPU4RgfiZM7x`</summary>

```text
DGP A (covariate-only error), extreme regime, n_expert=250, k=2, 5 MC runs
Rectifier should be ~0 under DGP A (no outcome error)

oracle                bias_z0=-0.0256  bias_z1=-0.0212
naive                 bias_z0=+0.0244  bias_z1=-0.0719
ec_hte                bias_z0=-0.0505  bias_z1=-0.0042
ec_hte_ppci           bias_z0=-0.0505  bias_z1=-0.0042
ppci                  bias_z0=-0.0372  bias_z1=-0.0263
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "b3ba88a8-6dec-4a50-b4f4-9e92bce0c6a3",
  "tool_use_result": {
    "stdout": "DGP A (covariate-only error), extreme regime, n_expert=250, k=2, 5 MC runs\nRectifier should be ~0 under DGP A (no outcome error)\n\noracle                bias_z0=-0.0256  bias_z1=-0.0212\nnaive                 bias_z0=+0.0244  bias_z1=-0.0719\nec_hte                bias_z0=-0.0505  bias_z1=-0.0042\nec_hte_ppci           bias_z0=-0.0505  bias_z1=-0.0042\nppci                  bias_z0=-0.0372  bias_z1=-0.0263",
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

_source line 26_

`ec_hte_ppci` now matches `ec_hte` exactly under DGP A — the rectifier is effectively 0 when there's no outcome error, confirming the fix eliminates double correction.

Let me also verify DGP C (both errors) still works — the rectifier should add value there:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "12acac4d-b579-4bee-9aab-59ce59c0ed77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dJTbQ7aqyjeu7wwbGDjLJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 36467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 716
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

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_01ByMnsfoqSjSAz12DEHTVPZ`</summary>

```json
{
  "command": "python3 -c \"\nimport exp007_ppci_dsl as m\nimport numpy as np\nimport pandas as pd\n\nregime = 'extreme'\nk = 2\nn_expert = 250\nsigma = 0.5\nn_mc = 5\n\nrows = []\nfor mc in range(n_mc):\n    r = m.run_one_mc(regime, m.REGIMES[regime], m.MISCLASS_K2[regime], n_expert, k, seed=mc,\n                     sigma_outcome=sigma, dgp_name='C_both_errors',\n                     outcome_bias_per_subgroup=m.OUTCOME_BIAS[regime][:k])\n    rows.extend(r)\n\ndf = pd.DataFrame(rows)\ndf['bias_z0'] = df['tau_hat_z0'] - df['tau_true_z0']\ndf['bias_z1'] = df['tau_hat_z1'] - df['tau_true_z1']\n\nprint('DGP C (both errors), extreme regime, n_expert=250, k=2, sigma=0.5, 5 MC runs')\nprint()\nfor method in ['oracle', 'naive', 'ec_hte', 'ec_hte_ppci', 'ppci']:\n    sub = df[df['method'] == method]\n    b0 = sub['bias_z0'].mean()\n    b1 = sub['bias_z1'].mean()\n    print(f'{method:20s}  bias_z0={b0:+.4f}  bias_z1={b1:+.4f}')\n\"\n",
  "description": "Validate DGP C: ec_hte_ppci should improve over ec_hte",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "6699856a-4e0c-4f20-bb72-7425858b114e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dJTbQ7aqyjeu7wwbGDjLJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 716,
      "cache_read_input_tokens": 36467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 716
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

_source line 28 · 2026-05-20T22:33:20.446Z_

<details><summary>↩ Tool result · `toolu_01ByMnsfoqSjSAz12DEHTVPZ`</summary>

```text
DGP C (both errors), extreme regime, n_expert=250, k=2, sigma=0.5, 5 MC runs

oracle                bias_z0=+0.1594  bias_z1=+0.1475
naive                 bias_z0=+0.2238  bias_z1=+0.0792
ec_hte                bias_z0=+0.1475  bias_z1=+0.1844
ec_hte_ppci           bias_z0=-0.0411  bias_z1=-0.0163
ppci                  bias_z0=-0.0238  bias_z1=-0.0511
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "e67fd772-ba0b-4a66-8a48-c3e005e9823c",
  "tool_use_result": {
    "stdout": "DGP C (both errors), extreme regime, n_expert=250, k=2, sigma=0.5, 5 MC runs\n\noracle                bias_z0=+0.1594  bias_z1=+0.1475\nnaive                 bias_z0=+0.2238  bias_z1=+0.0792\nec_hte                bias_z0=+0.1475  bias_z1=+0.1844\nec_hte_ppci           bias_z0=-0.0411  bias_z1=-0.0163\nppci                  bias_z0=-0.0238  bias_z1=-0.0511",
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

_source line 29_

Results look correct:

- **DGP A** (covariate-only): `ec_hte_ppci` = `ec_hte` exactly (rectifier ≈ 0, no double correction)
- **DGP C** (both errors): `ec_hte_ppci` substantially improves over `ec_hte` by correcting the remaining outcome error

Changes made:
1. **`method_ec_hte_ppci`** (line 420-446): Rectifier now uses `gold_bool` (true Z grouping) for both `tau_gold` and `tau_hat_gold_true_z`, so it only captures outcome error. Previously it used Z_hat grouping for `tau_hat_gold`, causing double correction of covariate error.
2. **`method_ppci` docstring** (line 325-338): Clarified that the PPCI rectifier captures all systematic error (covariate + outcome), complementary to EC-HTE's structured covariate-only correction.
3. **File header** (line 7-10): Documented the fix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "uuid": "469621ff-f2c0-437b-977f-ee28186f8389",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T4x4B7kDPX3vcnUwuGTFH2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 745,
      "cache_read_input_tokens": 37183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 745
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

_source line 30_

Results look correct:

- **DGP A** (covariate-only): `ec_hte_ppci` = `ec_hte` exactly (rectifier ≈ 0, no double correction)
- **DGP C** (both errors): `ec_hte_ppci` substantially improves over `ec_hte` by correcting the remaining outcome error

Changes made:
1. **`method_ec_hte_ppci`** (line 420-446): Rectifier now uses `gold_bool` (true Z grouping) for both `tau_gold` and `tau_hat_gold_true_z`, so it only captures outcome error. Previously it used Z_hat grouping for `tau_hat_gold`, causing double correction of covariate error.
2. **`method_ppci` docstring** (line 325-338): Clarified that the PPCI rectifier captures all systematic error (covariate + outcome), complementary to EC-HTE's structured covariate-only correction.
3. **File header** (line 7-10): Documented the fix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 100449,
  "duration_api_ms": 98972,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "909d7cad-6a48-4849-9ac9-63c991919903",
  "total_cost_usd": 0.45628975,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 26087,
    "cache_read_input_tokens": 308596,
    "output_tokens": 5481,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 26087,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 261,
        "cache_read_input_tokens": 37183,
        "cache_creation_input_tokens": 745,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 745
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1758,
      "outputTokens": 22,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001868,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 5481,
      "cacheReadInputTokens": 308596,
      "cacheCreationInputTokens": 26087,
      "webSearchRequests": 0,
      "costUSD": 0.45442175,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "71515f25-1d0c-442d-a9c5-31f07c9d8c32"
}
```

</details>

---
