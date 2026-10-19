# code plan 010 w1w2 fix

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_code_plan_010_w1w2_fix_20260520T235049.log`
- **Structured JSON:** [`92072c422bb1799c339f.json`](../../sessions/92/92072c422bb1799c339f.json)

## Before a recorded user message

52 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
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
  "uuid": "55bdba68-df5a-4388-aa6d-a5232903ad90",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1779415200,
    "rateLimitType": "seven_day",
    "utilization": 0.99,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "1c81c875-5469-418a-8cf2-12a015dad5d7",
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the key files to understand the current implementation before making changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "ae647683-782a-44a1-a1c5-ebd44d72cdde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Byz4Q64JNAbiejma3RxERa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15010,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15010
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

_source line 5_

I'll read the reference implementation and current source files in parallel to understand the codebase.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "ecfb5119-aff6-44b7-b254-790330061713",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Byz4Q64JNAbiejma3RxERa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15010,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15010
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_013V1VMehP34ZRZ1SKg6a76w`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_005_asv_extended.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "4dddc5d5-b249-4c27-ac7f-848994b062ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Byz4Q64JNAbiejma3RxERa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15010,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15010
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

### Tool result

_source line 7 · 2026-05-20T23:51:06.847Z_

<details><summary>↩ Tool result · `toolu_013V1VMehP34ZRZ1SKg6a76w`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_005: ASV framework extension to M-bias, IV, front-door topologies.
4	Extends plan_004 v3 (envelope monotonicity + magnitude/sign-flip dual reporting)
5	to complete Claim 2 coverage across all 6 DAG topologies.
6	"""
7	
8	import numpy as np
9	import json
10	import time
11	
12	K = 3
13	
14	# ============================================================================
15	# Utilities (from plan_004 v3)
16	# ============================================================================
17	
18	def softmax_sample(logits, rng):
19	    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))
20	    probs = exp_l / exp_l.sum(axis=1, keepdims=True)
21	    cum = np.cumsum(probs, axis=1)
22	    u = rng.uniform(size=logits.shape[0])
23	    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)
24	
25	
26	def generate_Astar(A, C, rng):
27	    probs = C[:, A]
28	    cum = np.cumsum(probs, axis=0)
29	    u = rng.uniform(size=len(A))
30	    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)
31	
32	
33	def ols_with_dummies(Y, T, Astar, K=3):
34	    N = len(Y)
35	    D = np.zeros((N, K - 1))
36	    for k in range(1, K):
37	        D[:, k - 1] = (Astar == k).astype(float)
38	    X = np.column_stack([np.ones(N), T, D])
39	    try:
40	        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
41	        resid = Y - X @ beta
42	        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)
43	        XtX_inv = np.linalg.inv(X.T @ X)
44	        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))
45	    except np.linalg.LinAlgError:
46	        beta = np.full(X.shape[1], np.nan)
47	        se = np.full(X.shape[1], np.nan)
48	    return beta, se
49	
50	
51	# ============================================================================
52	# C(delta) Parameterization (from plan_004 v3)
53	# ============================================================================
54	
55	class LinearInterpolation:
56	    def __call__(self, C0, delta):
57	        K = C0.shape[0]
58	        C_d = (1 - delta) * np.eye(K) + delta * C0
59	        C_d = np.maximum(C_d, 0.0)
60	        col_sums = C_d.sum(axis=0)
61	        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)
62	        C_d = C_d / col_sums
63	        return C_d
64	
65	    def delta_range(self, C0=None):
66	        if C0 is None:
67	            return (0.0, 5.0)
68	        min_diag = np.diag(C0).min()
69	        if min_diag >= 1.0:
70	            return (0.0, 10.0)
71	        delta_max = min(1.0 / (1.0 - min_diag), 10.0)
72	        return (0.0, delta_max)
73	
74	
75	# ============================================================================
76	# C matrices (from plan_004 v3)
77	# ============================================================================
78	
79	def make_C_list():
80	    return {
81	        "C1_sym": np.array([[0.80, 0.10, 0.10],
82	                            [0.10, 0.80, 0.10],
83	                            [0.10, 0.10, 0.80]]),
84	        "C2_high": np.array([[0.90, 0.05, 0.05],
85	                             [0.05, 0.90, 0.05],
86	                             [0.05, 0.05, 0.90]]),
87	        "C3_asym": np.array([[0.70, 0.20, 0.10],
88	                             [0.15, 0.70, 0.15],
89	                             [0.10, 0.15, 0.75]]),
90	        "C4_weak": np.array([[0.60, 0.20, 0.20],
91	                             [0.20, 0.60, 0.20],
92	                             [0.15, 0.15, 0.70]]),
93	        "C5_perm": np.array([[0.40, 0.30, 0.30],
94	                             [0.30, 0.40, 0.30],
95	                             [0.30, 0.30, 0.40]]),
96	        "C6_diff": np.array([[0.85, 0.075, 0.075],
97	                             [0.15, 0.70, 0.15],
98	                             [0.05, 0.05, 0.90]]),
99	    }
100	
101	
102	def normalize_C_list(C_dict):
103	    out = {}
104	    for name, C in C_dict.items():
105	        C = np.maximum(C, 0.0)
106	        cs = C.sum(axis=0)
107	        cs = np.where(cs < 1e-10, 1.0, cs)
108	        out[name] = C / cs
109	    return out
110	
111	
112	def random_C0(K, rng, diag_alpha=5.0, offdiag_alpha=1.0):
113	    C = np.zeros((K, K))
114	    for k in range(K):
115	        alphas = np.full(K, offdiag_alpha)
116	        alphas[k] = diag_alpha
117	        C[:, k] = rng.dirichlet(alphas)
118	    return C
119	
120	
121	# ============================================================================
122	# Topology 1: M-BIAS — U1->{A,T}, U2->{A,Y}, T->Y
123	# ============================================================================
124	
125	MBIAS_PARAMS = dict(tau=0.5, delta=1.0, lam=1.0,
126	                    g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9)
127	
128	
129	def _gen_mbias(N, params, rng):
130	    U1 = rng.normal(0, 1, N)
131	    U2 = rng.normal(0, 1, N)
132	    T = params['delta'] * U1 + rng.normal(0, 1, N)
133	    Y = params['tau'] * T + params['lam'] * U2 + rng.normal(0, 1, N)
134	    logits = np.column_stack([
135	        np.zeros(N),
136	        params['g1'] + params['a1'] * U1 + params['a2'] * U2,
137	        params['g2'] + params['a3'] * U1 + params['a4'] * U2,
138	    ])
139	    A = softmax_sample(logits, rng)
140	    return T, Y, A
141	
142	
143	def gen_mbias_data(N, params, C0, rng):
144	    T, Y, A = _gen_mbias(N, params, rng)
145	    Astar = generate_Astar(A, C0, rng)
146	    return T, Y, A, Astar
147	
148	
149	def precomp_mbias(params, N=2_000_000, seed=999):
150	    rng = np.random.default_rng(seed)
151	    T, Y, A = _gen_mbias(N, params, rng)
152	    DA = np.zeros((N, K))
153	    for k in range(K):
154	        DA[:, k] = (A == k).astype(float)
155	    return dict(
156	        E_T=T.mean(), E_T2=(T**2).mean(),
157	        E_Y=Y.mean(), E_TY=(T*Y).mean(),
158	        E_DA=DA.mean(0),
159	        E_DA_T=(DA * T[:, None]).mean(0),
160	        E_DA_Y=(DA * Y[:, None]).mean(0))
161	
162	
163	def plim_mbias(C, st):
164	    """OLS plim for Y ~ 1 + T + D1_A* + D2_A*."""
165	    ds  = C @ st['E_DA']
166	    dst = C @ st['E_DA_T']
167	    dsy = C @ st['E_DA_Y']
168	    ET, ET2 = st['E_T'], st['E_T2']
169	    EY, ETY = st['E_Y'], st['E_TY']
170	    EZZ = np.array([
171	        [1,      ET,      ds[1],    ds[2]   ],
172	        [ET,     ET2,     dst[1],   dst[2]  ],
173	        [ds[1],  dst[1],  ds[1],    0       ],
174	        [ds[2],  dst[2],  0,        ds[2]   ]])
175	    EZY = np.array([EY, ETY, dsy[1], dsy[2]])
176	    return np.linalg.solve(EZZ, EZY)
177	
178	
179	# ============================================================================
180	# Topology 2: IV — Z->A->Y, U->{A,Y}
181	# ============================================================================
182	
183	IV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)
184	IV_BETA = np.array([0.0, 0.5, -0.25])
185	
186	
187	def _gen_iv(N, beta, params, rng):
188	    Z_iv = rng.binomial(1, 0.5, N).astype(float)
189	    U = rng.normal(0, 1, N)
190	    eps = rng.normal(0, 1, N)
191	    logits = np.column_stack([
192	        np.zeros(N),
193	        params['g1'] + params['dZ'] * Z_iv + params['dU'] * U,
194	        params['g2'] + params['dZ2'] * Z_iv + params['dU2'] * U,
195	    ])
196	    A = softmax_sample(logits, rng)
197	    Y = (beta[1] * (A == 1).astype(float) + beta[2] * (A == 2).astype(float)
198	         + params['lam'] * U + eps)
199	    return Z_iv, U, Y, A
200	
201	
202	def gen_iv_data(N, beta, params, C0, rng):
203	    Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)
204	    Astar = generate_Astar(A, C0, rng)
205	    return Z_iv, Y, A, Astar
206	
207	
208	def precomp_iv(beta, params, N=2_000_000, seed=999):
209	    """Precompute reduced form and first stage for Wald estimator."""
210	    rng = np.random.default_rng(seed)
211	    Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)
212	    z1 = Z_iv == 1; z0 = Z_iv == 0
213	    RF = Y[z1].mean() - Y[z0].mean()
214	    FS = np.zeros(K)
215	    for k in range(K):
216	        FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()
217	    return dict(RF=RF, FS=FS)
218	
219	
220	def plim_iv(C, st):
221	    """Wald estimator: RF / FS*_1 where FS* = C @ FS."""
222	    FS_star = C @ st['FS']
223	    if abs(FS_star[1]) < 1e-8:
224	        return np.nan
225	    return st['RF'] / FS_star[1]
226	
227	
228	def wald_with_se(Z, Y, Astar, k=1):
229	    """Finite-sample Wald estimator with delta-method SE."""
230	    z1 = Z == 1; z0 = Z == 0
231	    n1 = float(z1.sum()); n0 = float(z0.sum())
232	    if n1 < 2 or n0 < 2:
233	        return np.nan, np.nan
234	    RF = Y[z1].mean() - Y[z0].mean()
235	    var_RF = Y[z1].var() / n1 + Y[z0].var() / n0
236	    Dk_z1 = (Astar[z1] == k).astype(float).mean()
237	    Dk_z0 = (Astar[z0] == k).astype(float).mean()
238	    FS = Dk_z1 - Dk_z0
239	    var_FS = Dk_z1 * (1 - Dk_z1) / n1 + Dk_z0 * (1 - Dk_z0) / n0
240	    if abs(FS) < 1e-8:
241	        return np.nan, np.nan
242	    Wald = RF / FS
243	    var_Wald = var_RF / FS**2 + RF**2 * var_FS / FS**4
244	    SE = np.sqrt(max(var_Wald, 0))
245	    return Wald, SE
246	
247	
248	# ============================================================================
249	# Topology 3: FRONT-DOOR — T->M->Y, U->{T,Y}
250	# ============================================================================
251	
252	ALPHA_U = 1.0
253	LAMBDA_U = 1.0
254	GAMMA_FD = np.array([0.0, 0.5, -0.3])
255	DELTA_FD = np.array([0.0, 1.0, -0.8])
256	BETA_FD = np.array([0.0, 1.0, -0.5])
257	
258	
259	def _gen_fd(N, beta, rng, g=None, d=None, aU=None, lU=None):
260	    if g is None: g = GAMMA_FD
261	    if d is None: d = DELTA_FD
262	    if aU is None: aU = ALPHA_U
263	    if lU is None: lU = LAMBDA_U
264	    U = rng.normal(0, 1, N)
265	    T = aU * U + rng.normal(0, 1, N)
266	    lo = np.column_stack([np.zeros(N), g[1] + d[1]*T, g[2] + d[2]*T])
267	    lo -= lo.max(1, keepdims=True)
268	    e = np.exp(lo)
269	    p = e / e.sum(1, keepdims=True)
270	    cu = np.cumsum(p, axis=1)
271	    u = rng.uniform(size=N)
272	    M = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)
273	    DM1 = (M == 1).astype(float)
274	    DM2 = (M == 2).astype(float)
275	    Y = beta[1]*DM1 + beta[2]*DM2 + lU*U + rng.normal(0, 1, N)
276	    return T, M, Y, U
277	
278	
279	def gen_fd_data(N, beta, C0, rng, lU=None, aU=None, d=None):
280	    T, M, Y, U = _gen_fd(N, beta, rng, d=d, aU=aU, lU=lU)
281	    Mstar = generate_Astar(M, C0, rng)
282	    return T, Y, M, Mstar
283	
284	
285	def precomp_fd(beta, N=10_000_000, seed=123, lU=None, aU=None, d=None):
286	    rng = np.random.default_rng(seed)
287	    T, M, Y, _ = _gen_fd(N, beta, rng, d=d, aU=aU, lU=lU)
288	    DM = np.zeros((N, K))
289	    for k in range(K):
290	        DM[:, k] = (M == k).astype(float)
291	    return dict(
292	        E_T=T.mean(), E_T2=(T**2).mean(),
293	        E_Y=Y.mean(), E_TY=(T*Y).mean(),
294	        E_DM=DM.mean(0),
295	        E_DM_T=(DM * T[:, None]).mean(0),
296	        E_DM_Y=(DM * Y[:, None]).mean(0))
297	
298	
299	def plim_fd(C, st):
300	    """OLS plim for Y ~ 1 + T + D1_M* + D2_M*."""
301	    ds  = C @ st['E_DM']
302	    dst = C @ st['E_DM_T']
303	    dsy = C @ st['E_DM_Y']
304	    ET, ET2 = st['E_T'], st['E_T2']
305	    EY, ETY = st['E_Y'], st['E_TY']
306	    EZZ = np.array([
307	        [1,      ET,      ds[1],    ds[2]   ],
308	        [ET,     ET2,     dst[1],   dst[2]  ],
309	        [ds[1],  dst[1],  ds[1],    0       ],
310	        [ds[2],  dst[2],  0,        ds[2]   ]])
311	    EZY = np.array([EY, ETY, dsy[1], dsy[2]])
312	    return np.linalg.solve(EZZ, EZY)
313	
314	
315	# ============================================================================
316	# ASV Framework
317	# ============================================================================
318	
319	def compute_bias_curve(topology, C0, param, tau_true, st, n_grid=1500):
320	    dmin, dmax = param.delta_range(C0)
321	    deltas = np.linspace(dmin, dmax, n_grid)
322	    tau_curve = np.zeros(n_grid)
323	    for i, d in enumerate(deltas):
324	        C_d = param(C0, d)
325	        if topology == "mbias":
326	            tau_curve[i] = plim_mbias(C_d, st)[1]
327	        elif topology == "iv":
328	            tau_curve[i] = plim_iv(C_d, st)
329	        elif topology == "frontdoor":
330	            tau_curve[i] = plim_fd(C_d, st)[1]
331	    bias_abs = np.abs(tau_curve - tau_true)
332	    return deltas, bias_abs, tau_curve
333	
334	
335	def compute_envelope(bias_abs):
336	    env = np.zeros_like(bias_abs)
337	    running_max = 0.0
338	    for i in range(len(bias_abs)):
339	        v = bias_abs[i]
340	        if not np.isnan(v):
341	            running_max = max(running_max, v)
342	        env[i] = running_max
343	    return env
344	
345	
346	def verify_envelope_monotonicity(envelope):
347	    diffs = np.diff(envelope)
348	    return int(np.sum(diffs < -1e-12))
349	
350	
351	def compute_asv_envelope(topology, C0, tau_true, param, threshold_type,
352	                         threshold_value=0.1, st=None, n_grid=1500):
353	    deltas, bias_abs, tau_curve = compute_bias_curve(
354	        topology, C0, param, tau_true, st, n_grid)
355	    envelope = compute_envelope(bias_abs)
356	
357	    valid_ba = bias_abs[~np.isnan(bias_abs)]
358	    raw_violations = int(np.sum(np.diff(valid_ba) < -1e-12)) if len(valid_ba) > 1 else 0
359	    env_violations = verify_envelope_monotonicity(envelope)
360	
361	    asv = None
362	    if threshold_type == "sign_flip":
363	        if abs(tau_true) < 1e-12:
364	            asv = None
365	        else:
366	            baseline_sign = np.sign(tau_true)
367	            for i, d in enumerate(deltas):
368	                if np.isnan(tau_curve[i]):
369	                    continue
370	                if np.sign(tau_curve[i]) != baseline_sign:
371	                    asv = d
372	                    break
373	    elif threshold_type == "magnitude_relative":
374	        if abs(tau_true) < 1e-12:
375	            asv = None
376	        else:
377	            thresh = threshold_value * abs(tau_true)
378	            for i, d in enumerate(deltas):
379	                if envelope[i] > thresh:
380	                    asv = d
381	                    break
382	    elif threshold_type == "magnitude_absolute":
383	        thresh = threshold_value
384	        for i, d in enumerate(deltas):
385	            if envelope[i] > thresh:
386	                asv = d
387	                break
388	
389	    return {
390	        "asv": asv,
391	        "raw_violations": raw_violations,
392	        "envelope_violations": env_violations,
393	        "deltas": deltas,
394	        "tau_curve": tau_curve,
395	        "envelope": envelope,
396	    }
397	
398	
399	def compute_magnitude_asv_fast(tau_curve, deltas, tau_true, rel_thresh=0.1):
400	    if abs(tau_true) < 1e-12:
401	        return None
402	    thresh = rel_thresh * abs(tau_true)
403	    running_max = 0.0
404	    for i in range(len(deltas)):
405	        b = abs(tau_curve[i] - tau_true)
406	        if np.isnan(b):
407	            continue
408	        running_max = max(running_max, b)
409	        if running_max > thresh:
410	            return deltas[i]
411	    return None
412	
413	
414	# ============================================================================
415	# Part 1: Envelope Monotonicity
416	# ============================================================================
417	
418	def part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_fd):
419	    print("\n" + "=" * 70)
420	    print("PART 1: Envelope Monotonicity (tau=0.5)")
421	    print("=" * 70)
422	    t0 = time.time()
423	    param = LinearInterpolation()
424	    C_list = normalize_C_list(make_C_list())
425	
426	    for topo, st, tau_true, label in [
427	        ("mbias", st_mb, 0.5, "M-bias"),
428	        ("iv", st_iv, 0.5, "IV"),
429	        ("frontdoor", st_fd, tau_fd, "Front-door"),
430	    ]:
431	        print(f"\n  {label} (tau_true={tau_true:.4f}):")
432	        for cname, C0 in C_list.items():
433	            r = compute_asv_envelope(topo, C0, tau_true, param,
434	                                     "magnitude_relative", 0.1, st=st)
435	            print(f"    {cname}: raw_violations={r['raw_violations']}/1500, "
436	                  f"envelope_violations={r['envelope_violations']}/1500")
437	    print(f"\n  Time: {time.time()-t0:.1f}s")
438	
439	
440	# ============================================================================
441	# Part 2: ASV Values (tau=0.5)
442	# ============================================================================
443	
444	def part2_asv_values(st_mb, st_iv, st_fd, tau_fd):
445	    print("\n" + "=" * 70)
446	    print("PART 2: ASV Values (tau=0.5)")
447	    print("=" * 70)
448	    t0 = time.time()
449	    param = LinearInterpolation()
450	    C_list = normalize_C_list(make_C_list())
451	    results = {}
452	
453	    print(f"\n  {'Topology':<12} {'C0':<10} {'SignFlip':>10} {'Mag10%':>10}")
454	    print("  " + "-" * 45)
455	
456	    for topo, st, tau_true, label in [
457	        ("mbias", st_mb, 0.5, "M-bias"),
458	        ("iv", st_iv, 0.5, "IV"),
459	        ("frontdoor", st_fd, tau_fd, "Front-door"),
460	    ]:
461	        for cname, C0 in C_list.items():
462	            r_sf = compute_asv_envelope(topo, C0, tau_true, param,
463	                                        "sign_flip", st=st)
464	            r_mag = compute_asv_envelope(topo, C0, tau_true, param,
465	                                         "magnitude_relative", 0.1, st=st)
466	            sf_s = f"{r_sf['asv']:.3f}" if r_sf['asv'] is not None else "None"
467	            mg_s = f"{r_mag['asv']:.3f}" if r_mag['asv'] is not None else "None"
468	            print(f"  {label:<12} {cname:<10} {sf_s:>10} {mg_s:>10}")
469	            results[(label, cname)] = {
470	                "sign_flip": r_sf['asv'], "magnitude_10pct": r_mag['asv']}
471	    print(f"\n  Time: {time.time()-t0:.1f}s")
472	    return results
473	
474	
475	# ============================================================================
476	# Part 3: Small-tau ASV
477	# ============================================================================
478	
479	def part3_small_tau_asv():
480	    print("\n" + "=" * 70)
481	    print("PART 3: Small-tau ASV (tau=0.05, 0.1)")
482	    print("=" * 70)
483	    t0 = time.time()
484	    param = LinearInterpolation()
485	    C_list = normalize_C_list(make_C_list())
486	    results = {}
487	
488	    for tau_val in [0.05, 0.1]:
489	        print(f"\n  --- tau = {tau_val} ---")
490	        mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_val
491	        st_mb = precomp_mbias(mb_p, N=2_000_000)
492	        iv_b = np.array([0.0, tau_val, -tau_val/2])
493	        st_iv = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
494	        lU = tau_val * 2
495	        st_fd = precomp_fd(BETA_FD, N=10_000_000, lU=lU, seed=200+int(tau_val*100))
496	        tau_fd = plim_fd(np.eye(K), st_fd)[1]
497	        print(f"  Front-door tau_I = {tau_fd:.6f}")
498	
499	        hdr = f"  {'Topology':<12} {'C0':<10} {'SignFlip':>10} {'Mag10%':>10} {'MagAbs.05':>10}"
500	        print(hdr)
501	        print("  " + "-" * 55)
502	
503	        for topo, st, tau_true, label in [
504	            ("mbias", st_mb, tau_val, "M-bias"),
505	            ("iv", st_iv, tau_val, "IV"),
506	            ("frontdoor", st_fd, tau_fd, "Front-door"),
507	        ]:
508	            for cname, C0 in C_list.items():
509	                r_sf = compute_asv_envelope(topo, C0, tau_true, param,
510	                                            "sign_flip", st=st)
511	                r_mg = compute_asv_envelope(topo, C0, tau_true, param,
512	                                            "magnitude_relative", 0.1, st=st)
513	                r_ab = compute_asv_envelope(topo, C0, tau_true, param,
514	                                            "magnitude_absolute", 0.05, st=st)
515	                sf_s = f"{r_sf['asv']:.3f}" if r_sf['asv'] is not None else "None"
516	                mg_s = f"{r_mg['asv']:.3f}" if r_mg['asv'] is not None else "None"
517	                ab_s = f"{r_ab['asv']:.3f}" if r_ab['asv'] is not None else "None"
518	                print(f"  {label:<12} {cname:<10} {sf_s:>10} {mg_s:>10} {ab_s:>10}")
519	                results[(tau_val, label, cname)] = {
520	                    "sign_flip": r_sf['asv'],
521	                    "magnitude_10pct": r_mg['asv'],
522	                    "magnitude_abs05": r_ab['asv']}
523	    print(f"\n  Time: {time.time()-t0:.1f}s")
524	    return results
525	
526	
527	# ============================================================================
528	# Part 4: MC Coverage
529	# ============================================================================
530	
531	def part4_mc_coverage(n_scenarios=500, N_mc=10000, reps=100):
532	    print("\n" + "=" * 70)
533	    print(f"PART 4: MC Coverage ({n_scenarios} scenarios x {reps} reps x N={N_mc})")
534	    print("=" * 70)
535	    t0 = time.time()
536	    rng = np.random.default_rng(42)
537	    results = {}
538	
539	    for tau_val in [0.05, 0.1]:
540	        print(f"\n  --- tau = {tau_val} ---")
541	
542	        # --- M-bias ---
543	        print("  [M-bias]")
544	        mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_val
545	        st_mb = precomp_mbias(mb_p, N=2_000_000)
546	        plim_ok = 0; bias_ok = 0
547	        for s in range(n_scenarios):
548	            C0 = random_C0(K, rng)
549	            tau_plim = plim_mbias(C0, st_mb)[1]
550	            bias_theory = abs(tau_plim - tau_val)
551	            tau_mc = np.zeros(reps)
552	            for r in range(reps):
553	                Td, Yd, _, Asd = gen_mbias_data(N_mc, mb_p, C0, rng)
554	                bh, _ = ols_with_dummies(Yd, Td, Asd, K)
555	                tau_mc[r] = bh[1]
556	            mc_mean = tau_mc.mean()
557	            mc_se = tau_mc.std() / np.sqrt(reps)
558	            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:
559	                plim_ok += 1
560	            if abs(mc_mean - tau_val) <= bias_theory + 3 * mc_se + 0.02:
561	                bias_ok += 1
562	            if (s + 1) % 100 == 0:
563	                print(f"    ... {s+1}/{n_scenarios}")
564	        print(f"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%")
565	        print(f"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%")
566	        results[("mbias", tau_val)] = {
567	            "plim_acc": plim_ok/n_scenarios, "bias_bounded": bias_ok/n_scenarios}
568	
569	        # --- IV ---
570	        print("  [IV]")
571	        iv_b = np.array([0.0, tau_val, -tau_val/2])
572	        st_iv = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
573	        plim_ok = 0; bias_ok = 0
574	        for s in range(n_scenarios):
575	            C0 = random_C0(K, rng)
576	            tau_plim = plim_iv(C0, st_iv)
577	            if np.isnan(tau_plim):
578	                plim_ok += 1; bias_ok += 1; continue
579	            bias_theory = abs(tau_plim - tau_val)
580	            tau_mc = np.zeros(reps)
581	            for r in range(reps):
582	                Zd, Yd, _, Asd = gen_iv_data(N_mc, iv_b, IV_PARAMS, C0, rng)
583	                w, _ = wald_with_se(Zd, Yd, Asd)
584	                tau_mc[r] = w
585	            valid = ~np.isnan(tau_mc)
586	            if valid.sum() < reps * 0.5:
587	                plim_ok += 1; bias_ok += 1; continue
588	            mc_mean = tau_mc[valid].mean()
589	            mc_se = tau_mc[valid].std() / np.sqrt(valid.sum())
590	            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.05:
591	                plim_ok += 1
592	            if abs(mc_mean - tau_val) <= bias_theory + 3 * mc_se + 0.05:
593	                bias_ok += 1
594	            if (s + 1) % 100 == 0:
595	                print(f"    ... {s+1}/{n_scenarios}")
596	        print(f"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%")
597	        print(f"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%")
598	        results[("iv", tau_val)] = {
599	            "plim_acc": plim_ok/n_scenarios, "bias_bounded": bias_ok/n_scenarios}
600	
601	        # --- Front-door ---
602	        print("  [Front-door]")
603	        lU = tau_val * 2
604	        st_fd = precomp_fd(BETA_FD, N=10_000_000, lU=lU,
605	                           seed=300+int(tau_val*100))
606	        tau_I_fd = plim_fd(np.eye(K), st_fd)[1]
607	        plim_ok = 0; bias_ok = 0
608	        for s in range(n_scenarios):
609	            C0 = random_C0(K, rng)
610	            tau_plim = plim_fd(C0, st_fd)[1]
611	            bias_theory = abs(tau_plim - tau_I_fd)
612	            tau_mc = np.zeros(reps)
613	            for r in range(reps):
614	                Td, Yd, _, Msd = gen_fd_data(N_mc, BETA_FD, C0, rng, lU=lU)
615	                bh, _ = ols_with_dummies(Yd, Td, Msd, K)
616	                tau_mc[r] = bh[1]
617	            mc_mean = tau_mc.mean()
618	            mc_se = tau_mc.std() / np.sqrt(reps)
619	            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:
620	                plim_ok += 1
621	            if abs(mc_mean - tau_I_fd) <= bias_theory + 3 * mc_se + 0.02:
622	                bias_ok += 1
623	            if (s + 1) % 100 == 0:
624	                print(f"    ... {s+1}/{n_scenarios}")
625	        print(f"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%")
626	        print(f"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%")
627	        results[("frontdoor", tau_val)] = {
628	            "plim_acc": plim_ok/n_scenarios, "bias_bounded": bias_ok/n_scenarios}
629	
630	    print(f"\n  Total time: {time.time()-t0:.1f}s")
631	    return results
632	
633	
634	# ============================================================================
635	# Part 5: Type I/II
636	# ============================================================================
637	
638	def part5_type_errors(n_mc=500, N_sample=5000):
639	    print("\n" + "=" * 70)
640	    print(f"PART 5: Type I/II ({n_mc} MC x N={N_sample})")
641	    print("  Decision: reject if |tau_hat/SE|>1.96 AND magnitude_ASV > 1")
642	    print("=" * 70)
643	    t0 = time.time()
644	    param = LinearInterpolation()
645	    C_list = normalize_C_list(make_C_list())
646	    results = {}
647	    seed_ctr = 3000
648	
649	    for tau_val in [0.05, 0.1]:
650	        print(f"\n  --- tau = {tau_val} ---")
651	        header = (f"  {'C_struct':<12} {'H':<5} {'naive_rej':>10} "
652	                  f"{'mag_rej':>10} {'mean_masv':>10}")
653	
654	        # === M-bias ===
655	        print("\n  [M-bias]")
656	        print(header)
657	        print("  " + "-" * 52)
658	        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
659	            mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_h
660	            st_h = precomp_mbias(mb_p, N=2_000_000)
661	            for cname, C0 in C_list.items():
662	                seed_ctr += 1
663	                dmin, dmax = param.delta_range(C0)
664	                deltas = np.linspace(dmin, dmax, 1500)
665	                tau_curve = np.array([
666	                    plim_mbias(param(C0, d), st_h)[1] for d in deltas])
667	                rng_mc = np.random.default_rng(seed_ctr)
668	                naive_rej = 0; mag_rej = 0; masv_vals = []
669	                for mc in range(n_mc):
670	                    Td, Yd, _, Asd = gen_mbias_data(
671	                        N_sample, mb_p, C0, rng_mc)
672	                    bh, seh = ols_with_dummies(Yd, Td, Asd, K)
673	                    tau_hat, se_tau = bh[1], seh[1]
674	                    reject = (abs(tau_hat / se_tau) > 1.96
675	                              if se_tau > 1e-10 else False)
676	                    if reject:
677	                        naive_rej += 1
678	                    masv = compute_magnitude_asv_fast(
679	                        tau_curve, deltas, tau_h, 0.1)
680	                    masv_vals.append(masv)
681	                    if reject and (masv is None or masv > 1.0):
682	                        mag_rej += 1
683	                mf = [a for a in masv_vals if a is not None]
684	                mm = f"{np.mean(mf):.2f}" if mf else "N/A"
685	                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
686	                      f"{mag_rej/n_mc:>10.3f} {mm:>10}")
687	                results[("mbias", tau_val, cname, h_label)] = {
688	                    "naive_rej": naive_rej/n_mc, "mag_rej": mag_rej/n_mc}
689	
690	        # === IV ===
691	        print("\n  [IV]")
692	        print(header)
693	        print("  " + "-" * 52)
694	        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
695	            iv_b = np.array([0.0, tau_h, -tau_h/2])
696	            st_h = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
697	            for cname, C0 in C_list.items():
698	                seed_ctr += 1
699	                dmin, dmax = param.delta_range(C0)
700	                deltas = np.linspace(dmin, dmax, 1500)
701	                tau_curve = np.array([
702	                    plim_iv(param(C0, d), st_h) for d in deltas])
703	                rng_mc = np.random.default_rng(seed_ctr)
704	                naive_rej = 0; mag_rej = 0; masv_vals = []
705	                for mc in range(n_mc):
706	                    Zd, Yd, _, Asd = gen_iv_data(
707	                        N_sample, iv_b, IV_PARAMS, C0, rng_mc)
708	                    w, se_w = wald_with_se(Zd, Yd, Asd)
709	                    reject = False
710	                    if not np.isnan(w) and se_w > 1e-10:
711	                        reject = abs(w / se_w) > 1.96
712	                    if reject:
713	                        naive_rej += 1
714	                    masv = compute_magnitude_asv_fast(
715	                        tau_curve, deltas, tau_h, 0.1)
716	                    masv_vals.append(masv)
717	                    if reject and (masv is None or masv > 1.0):
718	                        mag_rej += 1
719	                mf = [a for a in masv_vals if a is not None]
720	                mm = f"{np.mean(mf):.2f}" if mf else "N/A"
721	                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
722	                      f"{mag_rej/n_mc:>10.3f} {mm:>10}")
723	                results[("iv", tau_val, cname, h_label)] = {
724	                    "naive_rej": naive_rej/n_mc, "mag_rej": mag_rej/n_mc}
725	
726	        # === Front-door ===
727	        print("\n  [Front-door]")
728	        print(header)
729	        print("  " + "-" * 52)
730	        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
731	            if h_label == "H0":
732	                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=0.0, aU=0.0,
733	                                  d=np.zeros(3), seed=400)
734	                tau_ref = 0.0
735	            else:
736	                lU = tau_val * 2
737	                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=lU,
738	                                  seed=401+int(tau_val*100))
739	                tau_ref = plim_fd(np.eye(K), st_h)[1]
740	            print(f"    ({h_label}: tau_ref={tau_ref:.4f})")
741	            for cname, C0 in C_list.items():
742	                seed_ctr += 1
743	                dmin, dmax = param.delta_range(C0)
744	                deltas = np.linspace(dmin, dmax, 1500)
745	                tau_curve = np.array([
746	                    plim_fd(param(C0, d), st_h)[1] for d in deltas])
747	                rng_mc = np.random.default_rng(seed_ctr)
748	                naive_rej = 0; mag_rej = 0; masv_vals = []
749	                for mc in range(n_mc):
750	                    if h_label == "H0":
751	                        Td, Yd, _, Msd = gen_fd_data(
752	                            N_sample, BETA_FD, C0, rng_mc,
753	                            lU=0.0, aU=0.0, d=np.zeros(3))
754	                    else:
755	                        Td, Yd, _, Msd = gen_fd_data(
756	                            N_sample, BETA_FD, C0, rng_mc, lU=lU)
757	                    bh, seh = ols_with_dummies(Yd, Td, Msd, K)
758	                    tau_hat, se_tau = bh[1], seh[1]
759	                    reject = (abs(tau_hat / se_tau) > 1.96
760	                              if se_tau > 1e-10 else False)
761	                    if reject:
762	                        naive_rej += 1
763	                    masv = compute_magnitude_asv_fast(
764	                        tau_curve, deltas, tau_ref, 0.1)
765	                    masv_vals.append(masv)
766	                    if reject and (masv is None or masv > 1.0):
767	                        mag_rej += 1
768	                mf = [a for a in masv_vals if a is not None]
769	                mm = f"{np.mean(mf):.2f}" if mf else "N/A"
770	                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
771	                      f"{mag_rej/n_mc:>10.3f} {mm:>10}")
772	                results[("frontdoor", tau_val, cname, h_label)] = {
773	                    "naive_rej": naive_rej/n_mc, "mag_rej": mag_rej/n_mc}
774	
775	    print(f"\n  Total time: {time.time()-t0:.1f}s")
776	    return results
777	
778	
779	# ============================================================================
780	# Part 6: Summary JSON
781	# ============================================================================
782	
783	def collect_summary(asv_res, small_tau_res, cov_res, te_res):
784	    def _f(v):
785	        if v is None:
786	            return None
787	        return float(v)
788	
789	    summary = {
790	        "experiment": "plan_005_asv_extended",
791	        "topologies": ["mbias", "iv", "frontdoor"],
792	        "asv_values_tau05": {},
793	        "small_tau_asv": {},
794	        "coverage": {},
795	        "type_errors": {},
796	    }
797	    for (label, cname), vals in asv_res.items():
798	        summary["asv_values_tau05"][f"{label}_{cname}"] = {
799	            k: _f(v) for k, v in vals.items()}
800	    for (tv, label, cname), vals in small_tau_res.items():
801	        summary["small_tau_asv"][f"tau{tv}_{label}_{cname}"] = {
802	            k: _f(v) for k, v in vals.items()}
803	    for (topo, tv), vals in cov_res.items():
804	        summary["coverage"][f"{topo}_tau{tv}"] = vals
805	    for key, vals in te_res.items():
806	        summary["type_errors"]["_".join(str(x) for x in key)] = vals
807	    return summary
808	
809	
810	# ============================================================================
811	# Main
812	# ============================================================================
813	
814	if __name__ == "__main__":
815	    np.set_printoptions(precision=6, suppress=True)
816	    print("plan_005: ASV Framework Extension to M-bias/IV/Front-door")
817	    print("=" * 70)
818	    t_total = time.time()
819	
820	    print("\nPrecomputing sufficient statistics (tau=0.5)...")
821	    t0 = time.time()
822	    st_mb = precomp_mbias(MBIAS_PARAMS, N=2_000_000)
823	    tau_I_mb = plim_mbias(np.eye(K), st_mb)[1]
824	    print(f"  M-bias:     tau_DGP=0.5, plim(I)={tau_I_mb:.6f}")
825	
826	    st_iv = precomp_iv(IV_BETA, IV_PARAMS, N=2_000_000)
827	    tau_I_iv = plim_iv(np.eye(K), st_iv)
828	    print(f"  IV:         beta[1]=0.5, Wald(I)={tau_I_iv:.6f}")
829	
830	    st_fd = precomp_fd(BETA_FD, N=10_000_000)
831	    tau_I_fd = plim_fd(np.eye(K), st_fd)[1]
832	    print(f"  Front-door: plim(I)={tau_I_fd:.6f}")
833	    print(f"  Done ({time.time()-t0:.1f}s)")
834	
835	    part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_I_fd)
836	    asv_res = part2_asv_values(st_mb, st_iv, st_fd, tau_I_fd)
837	    small_tau_res = part3_small_tau_asv()
838	    cov_res = part4_mc_coverage(n_scenarios=500, N_mc=10000, reps=100)
839	    te_res = part5_type_errors(n_mc=500, N_sample=5000)
840	
841	    print("\n" + "=" * 70)
842	    print("PART 6: Summary JSON")
843	    print("=" * 70)
844	    summary = collect_summary(asv_res, small_tau_res, cov_res, te_res)
845	    print(json.dumps(summary, indent=2, default=str))
846	
847	    print("\n" + "=" * 70)
848	    elapsed = time.time() - t_total
849	    print(f"ALL PARTS COMPLETE. Total time: {elapsed:.1f}s ({elapsed/60:.1f}min)")
850	    print("=" * 70)
851	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "6b676f9c-42cc-42ce-9dc0-a0cf52740c58",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_005_asv_extended.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nplan_005: ASV framework extension to M-bias, IV, front-door topologies.\nExtends plan_004 v3 (envelope monotonicity + magnitude/sign-flip dual reporting)\nto complete Claim 2 coverage across all 6 DAG topologies.\n\"\"\"\n\nimport numpy as np\nimport json\nimport time\n\nK = 3\n\n# ============================================================================\n# Utilities (from plan_004 v3)\n# ============================================================================\n\ndef softmax_sample(logits, rng):\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\n    cum = np.cumsum(probs, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\n\n\ndef generate_Astar(A, C, rng):\n    probs = C[:, A]\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\n\n\ndef ols_with_dummies(Y, T, Astar, K=3):\n    N = len(Y)\n    D = np.zeros((N, K - 1))\n    for k in range(1, K):\n        D[:, k - 1] = (Astar == k).astype(float)\n    X = np.column_stack([np.ones(N), T, D])\n    try:\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n        resid = Y - X @ beta\n        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)\n        XtX_inv = np.linalg.inv(X.T @ X)\n        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))\n    except np.linalg.LinAlgError:\n        beta = np.full(X.shape[1], np.nan)\n        se = np.full(X.shape[1], np.nan)\n    return beta, se\n\n\n# ============================================================================\n# C(delta) Parameterization (from plan_004 v3)\n# ============================================================================\n\nclass LinearInterpolation:\n    def __call__(self, C0, delta):\n        K = C0.shape[0]\n        C_d = (1 - delta) * np.eye(K) + delta * C0\n        C_d = np.maximum(C_d, 0.0)\n        col_sums = C_d.sum(axis=0)\n        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\n        C_d = C_d / col_sums\n        return C_d\n\n    def delta_range(self, C0=None):\n        if C0 is None:\n            return (0.0, 5.0)\n        min_diag = np.diag(C0).min()\n        if min_diag >= 1.0:\n            return (0.0, 10.0)\n        delta_max = min(1.0 / (1.0 - min_diag), 10.0)\n        return (0.0, delta_max)\n\n\n# ============================================================================\n# C matrices (from plan_004 v3)\n# ============================================================================\n\ndef make_C_list():\n    return {\n        \"C1_sym\": np.array([[0.80, 0.10, 0.10],\n                            [0.10, 0.80, 0.10],\n                            [0.10, 0.10, 0.80]]),\n        \"C2_high\": np.array([[0.90, 0.05, 0.05],\n                             [0.05, 0.90, 0.05],\n                             [0.05, 0.05, 0.90]]),\n        \"C3_asym\": np.array([[0.70, 0.20, 0.10],\n                             [0.15, 0.70, 0.15],\n                             [0.10, 0.15, 0.75]]),\n        \"C4_weak\": np.array([[0.60, 0.20, 0.20],\n                             [0.20, 0.60, 0.20],\n                             [0.15, 0.15, 0.70]]),\n        \"C5_perm\": np.array([[0.40, 0.30, 0.30],\n                             [0.30, 0.40, 0.30],\n                             [0.30, 0.30, 0.40]]),\n        \"C6_diff\": np.array([[0.85, 0.075, 0.075],\n                             [0.15, 0.70, 0.15],\n                             [0.05, 0.05, 0.90]]),\n    }\n\n\ndef normalize_C_list(C_dict):\n    out = {}\n    for name, C in C_dict.items():\n        C = np.maximum(C, 0.0)\n        cs = C.sum(axis=0)\n        cs = np.where(cs < 1e-10, 1.0, cs)\n        out[name] = C / cs\n    return out\n\n\ndef random_C0(K, rng, diag_alpha=5.0, offdiag_alpha=1.0):\n    C = np.zeros((K, K))\n    for k in range(K):\n        alphas = np.full(K, offdiag_alpha)\n        alphas[k] = diag_alpha\n        C[:, k] = rng.dirichlet(alphas)\n    return C\n\n\n# ============================================================================\n# Topology 1: M-BIAS — U1->{A,T}, U2->{A,Y}, T->Y\n# ============================================================================\n\nMBIAS_PARAMS = dict(tau=0.5, delta=1.0, lam=1.0,\n                    g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9)\n\n\ndef _gen_mbias(N, params, rng):\n    U1 = rng.normal(0, 1, N)\n    U2 = rng.normal(0, 1, N)\n    T = params['delta'] * U1 + rng.normal(0, 1, N)\n    Y = params['tau'] * T + params['lam'] * U2 + rng.normal(0, 1, N)\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['a1'] * U1 + params['a2'] * U2,\n        params['g2'] + params['a3'] * U1 + params['a4'] * U2,\n    ])\n    A = softmax_sample(logits, rng)\n    return T, Y, A\n\n\ndef gen_mbias_data(N, params, C0, rng):\n    T, Y, A = _gen_mbias(N, params, rng)\n    Astar = generate_Astar(A, C0, rng)\n    return T, Y, A, Astar\n\n\ndef precomp_mbias(params, N=2_000_000, seed=999):\n    rng = np.random.default_rng(seed)\n    T, Y, A = _gen_mbias(N, params, rng)\n    DA = np.zeros((N, K))\n    for k in range(K):\n        DA[:, k] = (A == k).astype(float)\n    return dict(\n        E_T=T.mean(), E_T2=(T**2).mean(),\n        E_Y=Y.mean(), E_TY=(T*Y).mean(),\n        E_DA=DA.mean(0),\n        E_DA_T=(DA * T[:, None]).mean(0),\n        E_DA_Y=(DA * Y[:, None]).mean(0))\n\n\ndef plim_mbias(C, st):\n    \"\"\"OLS plim for Y ~ 1 + T + D1_A* + D2_A*.\"\"\"\n    ds  = C @ st['E_DA']\n    dst = C @ st['E_DA_T']\n    dsy = C @ st['E_DA_Y']\n    ET, ET2 = st['E_T'], st['E_T2']\n    EY, ETY = st['E_Y'], st['E_TY']\n    EZZ = np.array([\n        [1,      ET,      ds[1],    ds[2]   ],\n        [ET,     ET2,     dst[1],   dst[2]  ],\n        [ds[1],  dst[1],  ds[1],    0       ],\n        [ds[2],  dst[2],  0,        ds[2]   ]])\n    EZY = np.array([EY, ETY, dsy[1], dsy[2]])\n    return np.linalg.solve(EZZ, EZY)\n\n\n# ============================================================================\n# Topology 2: IV — Z->A->Y, U->{A,Y}\n# ============================================================================\n\nIV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)\nIV_BETA = np.array([0.0, 0.5, -0.25])\n\n\ndef _gen_iv(N, beta, params, rng):\n    Z_iv = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    eps = rng.normal(0, 1, N)\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['dZ'] * Z_iv + params['dU'] * U,\n        params['g2'] + params['dZ2'] * Z_iv + params['dU2'] * U,\n    ])\n    A = softmax_sample(logits, rng)\n    Y = (beta[1] * (A == 1).astype(float) + beta[2] * (A == 2).astype(float)\n         + params['lam'] * U + eps)\n    return Z_iv, U, Y, A\n\n\ndef gen_iv_data(N, beta, params, C0, rng):\n    Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)\n    Astar = generate_Astar(A, C0, rng)\n    return Z_iv, Y, A, Astar\n\n\ndef precomp_iv(beta, params, N=2_000_000, seed=999):\n    \"\"\"Precompute reduced form and first stage for Wald estimator.\"\"\"\n    rng = np.random.default_rng(seed)\n    Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)\n    z1 = Z_iv == 1; z0 = Z_iv == 0\n    RF = Y[z1].mean() - Y[z0].mean()\n    FS = np.zeros(K)\n    for k in range(K):\n        FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()\n    return dict(RF=RF, FS=FS)\n\n\ndef plim_iv(C, st):\n    \"\"\"Wald estimator: RF / FS*_1 where FS* = C @ FS.\"\"\"\n    FS_star = C @ st['FS']\n    if abs(FS_star[1]) < 1e-8:\n        return np.nan\n    return st['RF'] / FS_star[1]\n\n\ndef wald_with_se(Z, Y, Astar, k=1):\n    \"\"\"Finite-sample Wald estimator with delta-method SE.\"\"\"\n    z1 = Z == 1; z0 = Z == 0\n    n1 = float(z1.sum()); n0 = float(z0.sum())\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    RF = Y[z1].mean() - Y[z0].mean()\n    var_RF = Y[z1].var() / n1 + Y[z0].var() / n0\n    Dk_z1 = (Astar[z1] == k).astype(float).mean()\n    Dk_z0 = (Astar[z0] == k).astype(float).mean()\n    FS = Dk_z1 - Dk_z0\n    var_FS = Dk_z1 * (1 - Dk_z1) / n1 + Dk_z0 * (1 - Dk_z0) / n0\n    if abs(FS) < 1e-8:\n        return np.nan, np.nan\n    Wald = RF / FS\n    var_Wald = var_RF / FS**2 + RF**2 * var_FS / FS**4\n    SE = np.sqrt(max(var_Wald, 0))\n    return Wald, SE\n\n\n# ============================================================================\n# Topology 3: FRONT-DOOR — T->M->Y, U->{T,Y}\n# ============================================================================\n\nALPHA_U = 1.0\nLAMBDA_U = 1.0\nGAMMA_FD = np.array([0.0, 0.5, -0.3])\nDELTA_FD = np.array([0.0, 1.0, -0.8])\nBETA_FD = np.array([0.0, 1.0, -0.5])\n\n\ndef _gen_fd(N, beta, rng, g=None, d=None, aU=None, lU=None):\n    if g is None: g = GAMMA_FD\n    if d is None: d = DELTA_FD\n    if aU is None: aU = ALPHA_U\n    if lU is None: lU = LAMBDA_U\n    U = rng.normal(0, 1, N)\n    T = aU * U + rng.normal(0, 1, N)\n    lo = np.column_stack([np.zeros(N), g[1] + d[1]*T, g[2] + d[2]*T])\n    lo -= lo.max(1, keepdims=True)\n    e = np.exp(lo)\n    p = e / e.sum(1, keepdims=True)\n    cu = np.cumsum(p, axis=1)\n    u = rng.uniform(size=N)\n    M = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)\n    DM1 = (M == 1).astype(float)\n    DM2 = (M == 2).astype(float)\n    Y = beta[1]*DM1 + beta[2]*DM2 + lU*U + rng.normal(0, 1, N)\n    return T, M, Y, U\n\n\ndef gen_fd_data(N, beta, C0, rng, lU=None, aU=None, d=None):\n    T, M, Y, U = _gen_fd(N, beta, rng, d=d, aU=aU, lU=lU)\n    Mstar = generate_Astar(M, C0, rng)\n    return T, Y, M, Mstar\n\n\ndef precomp_fd(beta, N=10_000_000, seed=123, lU=None, aU=None, d=None):\n    rng = np.random.default_rng(seed)\n    T, M, Y, _ = _gen_fd(N, beta, rng, d=d, aU=aU, lU=lU)\n    DM = np.zeros((N, K))\n    for k in range(K):\n        DM[:, k] = (M == k).astype(float)\n    return dict(\n        E_T=T.mean(), E_T2=(T**2).mean(),\n        E_Y=Y.mean(), E_TY=(T*Y).mean(),\n        E_DM=DM.mean(0),\n        E_DM_T=(DM * T[:, None]).mean(0),\n        E_DM_Y=(DM * Y[:, None]).mean(0))\n\n\ndef plim_fd(C, st):\n    \"\"\"OLS plim for Y ~ 1 + T + D1_M* + D2_M*.\"\"\"\n    ds  = C @ st['E_DM']\n    dst = C @ st['E_DM_T']\n    dsy = C @ st['E_DM_Y']\n    ET, ET2 = st['E_T'], st['E_T2']\n    EY, ETY = st['E_Y'], st['E_TY']\n    EZZ = np.array([\n        [1,      ET,      ds[1],    ds[2]   ],\n        [ET,     ET2,     dst[1],   dst[2]  ],\n        [ds[1],  dst[1],  ds[1],    0       ],\n        [ds[2],  dst[2],  0,        ds[2]   ]])\n    EZY = np.array([EY, ETY, dsy[1], dsy[2]])\n    return np.linalg.solve(EZZ, EZY)\n\n\n# ============================================================================\n# ASV Framework\n# ============================================================================\n\ndef compute_bias_curve(topology, C0, param, tau_true, st, n_grid=1500):\n    dmin, dmax = param.delta_range(C0)\n    deltas = np.linspace(dmin, dmax, n_grid)\n    tau_curve = np.zeros(n_grid)\n    for i, d in enumerate(deltas):\n        C_d = param(C0, d)\n        if topology == \"mbias\":\n            tau_curve[i] = plim_mbias(C_d, st)[1]\n        elif topology == \"iv\":\n            tau_curve[i] = plim_iv(C_d, st)\n        elif topology == \"frontdoor\":\n            tau_curve[i] = plim_fd(C_d, st)[1]\n    bias_abs = np.abs(tau_curve - tau_true)\n    return deltas, bias_abs, tau_curve\n\n\ndef compute_envelope(bias_abs):\n    env = np.zeros_like(bias_abs)\n    running_max = 0.0\n    for i in range(len(bias_abs)):\n        v = bias_abs[i]\n        if not np.isnan(v):\n            running_max = max(running_max, v)\n        env[i] = running_max\n    return env\n\n\ndef verify_envelope_monotonicity(envelope):\n    diffs = np.diff(envelope)\n    return int(np.sum(diffs < -1e-12))\n\n\ndef compute_asv_envelope(topology, C0, tau_true, param, threshold_type,\n                         threshold_value=0.1, st=None, n_grid=1500):\n    deltas, bias_abs, tau_curve = compute_bias_curve(\n        topology, C0, param, tau_true, st, n_grid)\n    envelope = compute_envelope(bias_abs)\n\n    valid_ba = bias_abs[~np.isnan(bias_abs)]\n    raw_violations = int(np.sum(np.diff(valid_ba) < -1e-12)) if len(valid_ba) > 1 else 0\n    env_violations = verify_envelope_monotonicity(envelope)\n\n    asv = None\n    if threshold_type == \"sign_flip\":\n        if abs(tau_true) < 1e-12:\n            asv = None\n        else:\n            baseline_sign = np.sign(tau_true)\n            for i, d in enumerate(deltas):\n                if np.isnan(tau_curve[i]):\n                    continue\n                if np.sign(tau_curve[i]) != baseline_sign:\n                    asv = d\n                    break\n    elif threshold_type == \"magnitude_relative\":\n        if abs(tau_true) < 1e-12:\n            asv = None\n        else:\n            thresh = threshold_value * abs(tau_true)\n            for i, d in enumerate(deltas):\n                if envelope[i] > thresh:\n                    asv = d\n                    break\n    elif threshold_type == \"magnitude_absolute\":\n        thresh = threshold_value\n        for i, d in enumerate(deltas):\n            if envelope[i] > thresh:\n                asv = d\n                break\n\n    return {\n        \"asv\": asv,\n        \"raw_violations\": raw_violations,\n        \"envelope_violations\": env_violations,\n        \"deltas\": deltas,\n        \"tau_curve\": tau_curve,\n        \"envelope\": envelope,\n    }\n\n\ndef compute_magnitude_asv_fast(tau_curve, deltas, tau_true, rel_thresh=0.1):\n    if abs(tau_true) < 1e-12:\n        return None\n    thresh = rel_thresh * abs(tau_true)\n    running_max = 0.0\n    for i in range(len(deltas)):\n        b = abs(tau_curve[i] - tau_true)\n        if np.isnan(b):\n            continue\n        running_max = max(running_max, b)\n        if running_max > thresh:\n            return deltas[i]\n    return None\n\n\n# ============================================================================\n# Part 1: Envelope Monotonicity\n# ============================================================================\n\ndef part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_fd):\n    print(\"\\n\" + \"=\" * 70)\n    print(\"PART 1: Envelope Monotonicity (tau=0.5)\")\n    print(\"=\" * 70)\n    t0 = time.time()\n    param = LinearInterpolation()\n    C_list = normalize_C_list(make_C_list())\n\n    for topo, st, tau_true, label in [\n        (\"mbias\", st_mb, 0.5, \"M-bias\"),\n        (\"iv\", st_iv, 0.5, \"IV\"),\n        (\"frontdoor\", st_fd, tau_fd, \"Front-door\"),\n    ]:\n        print(f\"\\n  {label} (tau_true={tau_true:.4f}):\")\n        for cname, C0 in C_list.items():\n            r = compute_asv_envelope(topo, C0, tau_true, param,\n                                     \"magnitude_relative\", 0.1, st=st)\n            print(f\"    {cname}: raw_violations={r['raw_violations']}/1500, \"\n                  f\"envelope_violations={r['envelope_violations']}/1500\")\n    print(f\"\\n  Time: {time.time()-t0:.1f}s\")\n\n\n# ============================================================================\n# Part 2: ASV Values (tau=0.5)\n# ============================================================================\n\ndef part2_asv_values(st_mb, st_iv, st_fd, tau_fd):\n    print(\"\\n\" + \"=\" * 70)\n    print(\"PART 2: ASV Values (tau=0.5)\")\n    print(\"=\" * 70)\n    t0 = time.time()\n    param = LinearInterpolation()\n    C_list = normalize_C_list(make_C_list())\n    results = {}\n\n    print(f\"\\n  {'Topology':<12} {'C0':<10} {'SignFlip':>10} {'Mag10%':>10}\")\n    print(\"  \" + \"-\" * 45)\n\n    for topo, st, tau_true, label in [\n        (\"mbias\", st_mb, 0.5, \"M-bias\"),\n        (\"iv\", st_iv, 0.5, \"IV\"),\n        (\"frontdoor\", st_fd, tau_fd, \"Front-door\"),\n    ]:\n        for cname, C0 in C_list.items():\n            r_sf = compute_asv_envelope(topo, C0, tau_true, param,\n                                        \"sign_flip\", st=st)\n            r_mag = compute_asv_envelope(topo, C0, tau_true, param,\n                                         \"magnitude_relative\", 0.1, st=st)\n            sf_s = f\"{r_sf['asv']:.3f}\" if r_sf['asv'] is not None else \"None\"\n            mg_s = f\"{r_mag['asv']:.3f}\" if r_mag['asv'] is not None else \"None\"\n            print(f\"  {label:<12} {cname:<10} {sf_s:>10} {mg_s:>10}\")\n            results[(label, cname)] = {\n                \"sign_flip\": r_sf['asv'], \"magnitude_10pct\": r_mag['asv']}\n    print(f\"\\n  Time: {time.time()-t0:.1f}s\")\n    return results\n\n\n# ============================================================================\n# Part 3: Small-tau ASV\n# ============================================================================\n\ndef part3_small_tau_asv():\n    print(\"\\n\" + \"=\" * 70)\n    print(\"PART 3: Small-tau ASV (tau=0.05, 0.1)\")\n    print(\"=\" * 70)\n    t0 = time.time()\n    param = LinearInterpolation()\n    C_list = normalize_C_list(make_C_list())\n    results = {}\n\n    for tau_val in [0.05, 0.1]:\n        print(f\"\\n  --- tau = {tau_val} ---\")\n        mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_val\n        st_mb = precomp_mbias(mb_p, N=2_000_000)\n        iv_b = np.array([0.0, tau_val, -tau_val/2])\n        st_iv = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)\n        lU = tau_val * 2\n        st_fd = precomp_fd(BETA_FD, N=10_000_000, lU=lU, seed=200+int(tau_val*100))\n        tau_fd = plim_fd(np.eye(K), st_fd)[1]\n        print(f\"  Front-door tau_I = {tau_fd:.6f}\")\n\n        hdr = f\"  {'Topology':<12} {'C0':<10} {'SignFlip':>10} {'Mag10%':>10} {'MagAbs.05':>10}\"\n        print(hdr)\n        print(\"  \" + \"-\" * 55)\n\n        for topo, st, tau_true, label in [\n            (\"mbias\", st_mb, tau_val, \"M-bias\"),\n            (\"iv\", st_iv, tau_val, \"IV\"),\n            (\"frontdoor\", st_fd, tau_fd, \"Front-door\"),\n        ]:\n            for cname, C0 in C_list.items():\n                r_sf = compute_asv_envelope(topo, C0, tau_true, param,\n                                            \"sign_flip\", st=st)\n                r_mg = compute_asv_envelope(topo, C0, tau_true, param,\n                                            \"magnitude_relative\", 0.1, st=st)\n                r_ab = compute_asv_envelope(topo, C0, tau_true, param,\n                                            \"magnitude_absolute\", 0.05, st=st)\n                sf_s = f\"{r_sf['asv']:.3f}\" if r_sf['asv'] is not None else \"None\"\n                mg_s = f\"{r_mg['asv']:.3f}\" if r_mg['asv'] is not None else \"None\"\n                ab_s = f\"{r_ab['asv']:.3f}\" if r_ab['asv'] is not None else \"None\"\n                print(f\"  {label:<12} {cname:<10} {sf_s:>10} {mg_s:>10} {ab_s:>10}\")\n                results[(tau_val, label, cname)] = {\n                    \"sign_flip\": r_sf['asv'],\n                    \"magnitude_10pct\": r_mg['asv'],\n                    \"magnitude_abs05\": r_ab['asv']}\n    print(f\"\\n  Time: {time.time()-t0:.1f}s\")\n    return results\n\n\n# ============================================================================\n# Part 4: MC Coverage\n# ============================================================================\n\ndef part4_mc_coverage(n_scenarios=500, N_mc=10000, reps=100):\n    print(\"\\n\" + \"=\" * 70)\n    print(f\"PART 4: MC Coverage ({n_scenarios} scenarios x {reps} reps x N={N_mc})\")\n    print(\"=\" * 70)\n    t0 = time.time()\n    rng = np.random.default_rng(42)\n    results = {}\n\n    for tau_val in [0.05, 0.1]:\n        print(f\"\\n  --- tau = {tau_val} ---\")\n\n        # --- M-bias ---\n        print(\"  [M-bias]\")\n        mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_val\n        st_mb = precomp_mbias(mb_p, N=2_000_000)\n        plim_ok = 0; bias_ok = 0\n        for s in range(n_scenarios):\n            C0 = random_C0(K, rng)\n            tau_plim = plim_mbias(C0, st_mb)[1]\n            bias_theory = abs(tau_plim - tau_val)\n            tau_mc = np.zeros(reps)\n            for r in range(reps):\n                Td, Yd, _, Asd = gen_mbias_data(N_mc, mb_p, C0, rng)\n                bh, _ = ols_with_dummies(Yd, Td, Asd, K)\n                tau_mc[r] = bh[1]\n            mc_mean = tau_mc.mean()\n            mc_se = tau_mc.std() / np.sqrt(reps)\n            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:\n                plim_ok += 1\n            if abs(mc_mean - tau_val) <= bias_theory + 3 * mc_se + 0.02:\n                bias_ok += 1\n            if (s + 1) % 100 == 0:\n                print(f\"    ... {s+1}/{n_scenarios}\")\n        print(f\"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%\")\n        print(f\"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%\")\n        results[(\"mbias\", tau_val)] = {\n            \"plim_acc\": plim_ok/n_scenarios, \"bias_bounded\": bias_ok/n_scenarios}\n\n        # --- IV ---\n        print(\"  [IV]\")\n        iv_b = np.array([0.0, tau_val, -tau_val/2])\n        st_iv = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)\n        plim_ok = 0; bias_ok = 0\n        for s in range(n_scenarios):\n            C0 = random_C0(K, rng)\n            tau_plim = plim_iv(C0, st_iv)\n            if np.isnan(tau_plim):\n                plim_ok += 1; bias_ok += 1; continue\n            bias_theory = abs(tau_plim - tau_val)\n            tau_mc = np.zeros(reps)\n            for r in range(reps):\n                Zd, Yd, _, Asd = gen_iv_data(N_mc, iv_b, IV_PARAMS, C0, rng)\n                w, _ = wald_with_se(Zd, Yd, Asd)\n                tau_mc[r] = w\n            valid = ~np.isnan(tau_mc)\n            if valid.sum() < reps * 0.5:\n                plim_ok += 1; bias_ok += 1; continue\n            mc_mean = tau_mc[valid].mean()\n            mc_se = tau_mc[valid].std() / np.sqrt(valid.sum())\n            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.05:\n                plim_ok += 1\n            if abs(mc_mean - tau_val) <= bias_theory + 3 * mc_se + 0.05:\n                bias_ok += 1\n            if (s + 1) % 100 == 0:\n                print(f\"    ... {s+1}/{n_scenarios}\")\n        print(f\"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%\")\n        print(f\"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%\")\n        results[(\"iv\", tau_val)] = {\n            \"plim_acc\": plim_ok/n_scenarios, \"bias_bounded\": bias_ok/n_scenarios}\n\n        # --- Front-door ---\n        print(\"  [Front-door]\")\n        lU = tau_val * 2\n        st_fd = precomp_fd(BETA_FD, N=10_000_000, lU=lU,\n                           seed=300+int(tau_val*100))\n        tau_I_fd = plim_fd(np.eye(K), st_fd)[1]\n        plim_ok = 0; bias_ok = 0\n        for s in range(n_scenarios):\n            C0 = random_C0(K, rng)\n            tau_plim = plim_fd(C0, st_fd)[1]\n            bias_theory = abs(tau_plim - tau_I_fd)\n            tau_mc = np.zeros(reps)\n            for r in range(reps):\n                Td, Yd, _, Msd = gen_fd_data(N_mc, BETA_FD, C0, rng, lU=lU)\n                bh, _ = ols_with_dummies(Yd, Td, Msd, K)\n                tau_mc[r] = bh[1]\n            mc_mean = tau_mc.mean()\n            mc_se = tau_mc.std() / np.sqrt(reps)\n            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:\n                plim_ok += 1\n            if abs(mc_mean - tau_I_fd) <= bias_theory + 3 * mc_se + 0.02:\n                bias_ok += 1\n            if (s + 1) % 100 == 0:\n                print(f\"    ... {s+1}/{n_scenarios}\")\n        print(f\"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%\")\n        print(f\"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%\")\n        results[(\"frontdoor\", tau_val)] = {\n            \"plim_acc\": plim_ok/n_scenarios, \"bias_bounded\": bias_ok/n_scenarios}\n\n    print(f\"\\n  Total time: {time.time()-t0:.1f}s\")\n    return results\n\n\n# ============================================================================\n# Part 5: Type I/II\n# ============================================================================\n\ndef part5_type_errors(n_mc=500, N_sample=5000):\n    print(\"\\n\" + \"=\" * 70)\n    print(f\"PART 5: Type I/II ({n_mc} MC x N={N_sample})\")\n    print(\"  Decision: reject if |tau_hat/SE|>1.96 AND magnitude_ASV > 1\")\n    print(\"=\" * 70)\n    t0 = time.time()\n    param = LinearInterpolation()\n    C_list = normalize_C_list(make_C_list())\n    results = {}\n    seed_ctr = 3000\n\n    for tau_val in [0.05, 0.1]:\n        print(f\"\\n  --- tau = {tau_val} ---\")\n        header = (f\"  {'C_struct':<12} {'H':<5} {'naive_rej':>10} \"\n                  f\"{'mag_rej':>10} {'mean_masv':>10}\")\n\n        # === M-bias ===\n        print(\"\\n  [M-bias]\")\n        print(header)\n        print(\"  \" + \"-\" * 52)\n        for h_label, tau_h in [(\"H0\", 0.0), (\"H1\", tau_val)]:\n            mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_h\n            st_h = precomp_mbias(mb_p, N=2_000_000)\n            for cname, C0 in C_list.items():\n                seed_ctr += 1\n                dmin, dmax = param.delta_range(C0)\n                deltas = np.linspace(dmin, dmax, 1500)\n                tau_curve = np.array([\n                    plim_mbias(param(C0, d), st_h)[1] for d in deltas])\n                rng_mc = np.random.default_rng(seed_ctr)\n                naive_rej = 0; mag_rej = 0; masv_vals = []\n                for mc in range(n_mc):\n                    Td, Yd, _, Asd = gen_mbias_data(\n                        N_sample, mb_p, C0, rng_mc)\n                    bh, seh = ols_with_dummies(Yd, Td, Asd, K)\n                    tau_hat, se_tau = bh[1], seh[1]\n                    reject = (abs(tau_hat / se_tau) > 1.96\n                              if se_tau > 1e-10 else False)\n                    if reject:\n                        naive_rej += 1\n                    masv = compute_magnitude_asv_fast(\n                        tau_curve, deltas, tau_h, 0.1)\n                    masv_vals.append(masv)\n                    if reject and (masv is None or masv > 1.0):\n                        mag_rej += 1\n                mf = [a for a in masv_vals if a is not None]\n                mm = f\"{np.mean(mf):.2f}\" if mf else \"N/A\"\n                print(f\"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} \"\n                      f\"{mag_rej/n_mc:>10.3f} {mm:>10}\")\n                results[(\"mbias\", tau_val, cname, h_label)] = {\n                    \"naive_rej\": naive_rej/n_mc, \"mag_rej\": mag_rej/n_mc}\n\n        # === IV ===\n        print(\"\\n  [IV]\")\n        print(header)\n        print(\"  \" + \"-\" * 52)\n        for h_label, tau_h in [(\"H0\", 0.0), (\"H1\", tau_val)]:\n            iv_b = np.array([0.0, tau_h, -tau_h/2])\n            st_h = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)\n            for cname, C0 in C_list.items():\n                seed_ctr += 1\n                dmin, dmax = param.delta_range(C0)\n                deltas = np.linspace(dmin, dmax, 1500)\n                tau_curve = np.array([\n                    plim_iv(param(C0, d), st_h) for d in deltas])\n                rng_mc = np.random.default_rng(seed_ctr)\n                naive_rej = 0; mag_rej = 0; masv_vals = []\n                for mc in range(n_mc):\n                    Zd, Yd, _, Asd = gen_iv_data(\n                        N_sample, iv_b, IV_PARAMS, C0, rng_mc)\n                    w, se_w = wald_with_se(Zd, Yd, Asd)\n                    reject = False\n                    if not np.isnan(w) and se_w > 1e-10:\n                        reject = abs(w / se_w) > 1.96\n                    if reject:\n                        naive_rej += 1\n                    masv = compute_magnitude_asv_fast(\n                        tau_curve, deltas, tau_h, 0.1)\n                    masv_vals.append(masv)\n                    if reject and (masv is None or masv > 1.0):\n                        mag_rej += 1\n                mf = [a for a in masv_vals if a is not None]\n                mm = f\"{np.mean(mf):.2f}\" if mf else \"N/A\"\n                print(f\"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} \"\n                      f\"{mag_rej/n_mc:>10.3f} {mm:>10}\")\n                results[(\"iv\", tau_val, cname, h_label)] = {\n                    \"naive_rej\": naive_rej/n_mc, \"mag_rej\": mag_rej/n_mc}\n\n        # === Front-door ===\n        print(\"\\n  [Front-door]\")\n        print(header)\n        print(\"  \" + \"-\" * 52)\n        for h_label, tau_h in [(\"H0\", 0.0), (\"H1\", tau_val)]:\n            if h_label == \"H0\":\n                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=0.0, aU=0.0,\n                                  d=np.zeros(3), seed=400)\n                tau_ref = 0.0\n            else:\n                lU = tau_val * 2\n                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=lU,\n                                  seed=401+int(tau_val*100))\n                tau_ref = plim_fd(np.eye(K), st_h)[1]\n            print(f\"    ({h_label}: tau_ref={tau_ref:.4f})\")\n            for cname, C0 in C_list.items():\n                seed_ctr += 1\n                dmin, dmax = param.delta_range(C0)\n                deltas = np.linspace(dmin, dmax, 1500)\n                tau_curve = np.array([\n                    plim_fd(param(C0, d), st_h)[1] for d in deltas])\n                rng_mc = np.random.default_rng(seed_ctr)\n                naive_rej = 0; mag_rej = 0; masv_vals = []\n                for mc in range(n_mc):\n                    if h_label == \"H0\":\n                        Td, Yd, _, Msd = gen_fd_data(\n                            N_sample, BETA_FD, C0, rng_mc,\n                            lU=0.0, aU=0.0, d=np.zeros(3))\n                    else:\n                        Td, Yd, _, Msd = gen_fd_data(\n                            N_sample, BETA_FD, C0, rng_mc, lU=lU)\n                    bh, seh = ols_with_dummies(Yd, Td, Msd, K)\n                    tau_hat, se_tau = bh[1], seh[1]\n                    reject = (abs(tau_hat / se_tau) > 1.96\n                              if se_tau > 1e-10 else False)\n                    if reject:\n                        naive_rej += 1\n                    masv = compute_magnitude_asv_fast(\n                        tau_curve, deltas, tau_ref, 0.1)\n                    masv_vals.append(masv)\n                    if reject and (masv is None or masv > 1.0):\n                        mag_rej += 1\n                mf = [a for a in masv_vals if a is not None]\n                mm = f\"{np.mean(mf):.2f}\" if mf else \"N/A\"\n                print(f\"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} \"\n                      f\"{mag_rej/n_mc:>10.3f} {mm:>10}\")\n                results[(\"frontdoor\", tau_val, cname, h_label)] = {\n                    \"naive_rej\": naive_rej/n_mc, \"mag_rej\": mag_rej/n_mc}\n\n    print(f\"\\n  Total time: {time.time()-t0:.1f}s\")\n    return results\n\n\n# ============================================================================\n# Part 6: Summary JSON\n# ============================================================================\n\ndef collect_summary(asv_res, small_tau_res, cov_res, te_res):\n    def _f(v):\n        if v is None:\n            return None\n        return float(v)\n\n    summary = {\n        \"experiment\": \"plan_005_asv_extended\",\n        \"topologies\": [\"mbias\", \"iv\", \"frontdoor\"],\n        \"asv_values_tau05\": {},\n        \"small_tau_asv\": {},\n        \"coverage\": {},\n        \"type_errors\": {},\n    }\n    for (label, cname), vals in asv_res.items():\n        summary[\"asv_values_tau05\"][f\"{label}_{cname}\"] = {\n            k: _f(v) for k, v in vals.items()}\n    for (tv, label, cname), vals in small_tau_res.items():\n        summary[\"small_tau_asv\"][f\"tau{tv}_{label}_{cname}\"] = {\n            k: _f(v) for k, v in vals.items()}\n    for (topo, tv), vals in cov_res.items():\n        summary[\"coverage\"][f\"{topo}_tau{tv}\"] = vals\n    for key, vals in te_res.items():\n        summary[\"type_errors\"][\"_\".join(str(x) for x in key)] = vals\n    return summary\n\n\n# ============================================================================\n# Main\n# ============================================================================\n\nif __name__ == \"__main__\":\n    np.set_printoptions(precision=6, suppress=True)\n    print(\"plan_005: ASV Framework Extension to M-bias/IV/Front-door\")\n    print(\"=\" * 70)\n    t_total = time.time()\n\n    print(\"\\nPrecomputing sufficient statistics (tau=0.5)...\")\n    t0 = time.time()\n    st_mb = precomp_mbias(MBIAS_PARAMS, N=2_000_000)\n    tau_I_mb = plim_mbias(np.eye(K), st_mb)[1]\n    print(f\"  M-bias:     tau_DGP=0.5, plim(I)={tau_I_mb:.6f}\")\n\n    st_iv = precomp_iv(IV_BETA, IV_PARAMS, N=2_000_000)\n    tau_I_iv = plim_iv(np.eye(K), st_iv)\n    print(f\"  IV:         beta[1]=0.5, Wald(I)={tau_I_iv:.6f}\")\n\n    st_fd = precomp_fd(BETA_FD, N=10_000_000)\n    tau_I_fd = plim_fd(np.eye(K), st_fd)[1]\n    print(f\"  Front-door: plim(I)={tau_I_fd:.6f}\")\n    print(f\"  Done ({time.time()-t0:.1f}s)\")\n\n    part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_I_fd)\n    asv_res = part2_asv_values(st_mb, st_iv, st_fd, tau_I_fd)\n    small_tau_res = part3_small_tau_asv()\n    cov_res = part4_mc_coverage(n_scenarios=500, N_mc=10000, reps=100)\n    te_res = part5_type_errors(n_mc=500, N_sample=5000)\n\n    print(\"\\n\" + \"=\" * 70)\n    print(\"PART 6: Summary JSON\")\n    print(\"=\" * 70)\n    summary = collect_summary(asv_res, small_tau_res, cov_res, te_res)\n    print(json.dumps(summary, indent=2, default=str))\n\n    print(\"\\n\" + \"=\" * 70)\n    elapsed = time.time() - t_total\n    print(f\"ALL PARTS COMPLETE. Total time: {elapsed:.1f}s ({elapsed/60:.1f}min)\")\n    print(\"=\" * 70)\n",
      "numLines": 851,
      "startLine": 1,
      "totalLines": 851
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01MGqtgcq5JHY1kKExM9HrKj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "8d54da3c-5c03-4e4e-ad84-0151ff93881f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Byz4Q64JNAbiejma3RxERa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15010,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15010
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

### Tool result

_source line 9 · 2026-05-20T23:51:07.091Z_

<details><summary>↩ Tool result · `toolu_01MGqtgcq5JHY1kKExM9HrKj`</summary>

```text
1	"""Compute annotation-error bias via probability limit calculations.
2	
3	Uses precomputed sufficient statistics from large-sample DGP simulations
4	to compute OLS plim as a function of confusion matrix C, avoiding MC.
5	"""
6	
7	import warnings
8	import numpy as np
9	from .dgp import DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES
10	from .confusion import validate_confusion_matrix
11	
12	_N_PRECOMP = 2_000_000
13	_precomp_cache = {}
14	
15	
16	def _params_key(params):
17	    items = []
18	    for k, v in sorted(params.items()):
19	        if isinstance(v, np.ndarray):
20	            items.append((k, tuple(v.flat)))
21	        else:
22	            items.append((k, v))
23	    return tuple(items)
24	
25	
26	def _precompute(topology, params, K, seed=999):
27	    """Precompute sufficient statistics for plim calculation."""
28	    cache_key = (topology, _params_key(params), K)
29	    if cache_key in _precomp_cache:
30	        return _precomp_cache[cache_key]
31	
32	    rng = np.random.default_rng(seed)
33	    data = GEN_FUNCS[topology](_N_PRECOMP, params=params, rng=rng)
34	    Y = data["Y"]
35	    A = data["A"]
36	
37	    DA = np.zeros((_N_PRECOMP, K))
38	    for k in range(K):
39	        DA[:, k] = (A == k).astype(float)
40	
41	    stats = {
42	        "E_Y": Y.mean(),
43	        "E_DA": DA.mean(0),
44	        "E_DA_Y": (DA * Y[:, None]).mean(0),
45	    }
46	
47	    if topology in HAS_TREATMENT:
48	        T = data["T"]
49	        stats.update({
50	            "E_T": T.mean(),
51	            "E_T2": (T ** 2).mean(),
52	            "E_TY": (T * Y).mean(),
53	            "E_DA_T": (DA * T[:, None]).mean(0),
54	        })
55	
56	    _precomp_cache[cache_key] = stats
57	    return stats
58	
59	
60	def _plim_with_T(C, stats, K):
61	    """OLS plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}."""
62	    ds = C @ stats["E_DA"]
63	    dst = C @ stats["E_DA_T"]
64	    dsy = C @ stats["E_DA_Y"]
65	    ET, ET2 = stats["E_T"], stats["E_T2"]
66	    EY, ETY = stats["E_Y"], stats["E_TY"]
67	
68	    dim = 1 + K  # intercept + T + (K-1) dummies
69	    EZZ = np.zeros((dim, dim))
70	    EZZ[0, 0] = 1.0
71	    EZZ[0, 1] = EZZ[1, 0] = ET
72	    EZZ[1, 1] = ET2
73	    for j in range(1, K):
74	        idx = j + 1
75	        EZZ[0, idx] = EZZ[idx, 0] = ds[j]
76	        EZZ[1, idx] = EZZ[idx, 1] = dst[j]
77	        EZZ[idx, idx] = ds[j]
78	
79	    EZY = np.zeros(dim)
80	    EZY[0] = EY
81	    EZY[1] = ETY
82	    for j in range(1, K):
83	        EZY[j + 1] = dsy[j]
84	
85	    cond = np.linalg.cond(EZZ)
86	    if cond > 1e12:
87	        warnings.warn(
88	            f"EZZ condition number {cond:.1e} — plim may be numerically unstable"
89	        )
90	
91	    return np.linalg.solve(EZZ, EZY)
92	
93	
94	def _plim_no_T(C, stats, K):
95	    """OLS plim for Y ~ 1 + D*_1 + ... + D*_{K-1}."""
96	    ds = C @ stats["E_DA"]
97	    dsy = C @ stats["E_DA_Y"]
98	    EY = stats["E_Y"]
99	
100	    dim = K  # intercept + (K-1) dummies
101	    EZZ = np.zeros((dim, dim))
102	    EZZ[0, 0] = 1.0
103	    for j in range(1, K):
104	        EZZ[0, j] = EZZ[j, 0] = ds[j]
105	        EZZ[j, j] = ds[j]
106	
107	    EZY = np.zeros(dim)
108	    EZY[0] = EY
109	    for j in range(1, K):
110	        EZY[j] = dsy[j]
111	
112	    cond = np.linalg.cond(EZZ)
113	    if cond > 1e12:
114	        warnings.warn(
115	            f"EZZ condition number {cond:.1e} — plim may be numerically unstable"
116	        )
117	
118	    return np.linalg.solve(EZZ, EZY)
119	
120	
121	def _get_tau(topology, C, stats, K):
122	    """Extract target coefficient from plim vector.
123	
124	    For topologies with T: coefficient index 1 (treatment effect).
125	    For topologies without T: coefficient index 1 (first dummy).
126	    """
127	    if topology in HAS_TREATMENT:
128	        coefs = _plim_with_T(C, stats, K)
129	    else:
130	        coefs = _plim_no_T(C, stats, K)
131	    return coefs[1]
132	
133	
134	def compute_bias(topology, C, params=None):
135	    """Compute annotation-error bias for a given topology and confusion matrix.
136	
137	    Args:
138	        topology: one of "confounding", "mediation", "collider", "exposure",
139	                  "mbias", "iv", "frontdoor"
140	        C: (K, K) column-stochastic confusion matrix, C[j,i] = P(A*=j|A=i)
141	        params: optional DGP parameters dict, None uses defaults
142	
143	    Returns:
144	        dict with tau_true, tau_biased, bias, bias_pct, topology
145	    """
146	    if topology not in TOPOLOGIES:
147	        raise ValueError(f"Unknown topology: {topology}. Choose from {TOPOLOGIES}")
148	    if not validate_confusion_matrix(C):
149	        raise ValueError("C must be a square, non-negative, column-stochastic matrix")
150	
151	    K = C.shape[0]
152	    merged = dict(DEFAULT_PARAMS[topology])
153	    if params is not None:
154	        merged.update(params)
155	
156	    stats = _precompute(topology, merged, K)
157	    tau_true = _get_tau(topology, np.eye(K), stats, K)
158	    tau_biased = _get_tau(topology, C, stats, K)
159	    bias = tau_biased - tau_true
160	    bias_pct = 100.0 * bias / tau_true if abs(tau_true) > 1e-12 else float("nan")
161	
162	    return {
163	        "tau_true": float(tau_true),
164	        "tau_biased": float(tau_biased),
165	        "bias": float(bias),
166	        "bias_pct": float(bias_pct),
167	        "topology": topology,
168	    }
169	
170	
171	def clear_cache():
172	    """Clear the precomputed statistics cache."""
173	    _precomp_cache.clear()
174	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "317a2ae1-d179-4ba3-9d39-fb6b9daab660",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py",
      "content": "\"\"\"Compute annotation-error bias via probability limit calculations.\n\nUses precomputed sufficient statistics from large-sample DGP simulations\nto compute OLS plim as a function of confusion matrix C, avoiding MC.\n\"\"\"\n\nimport warnings\nimport numpy as np\nfrom .dgp import DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES\nfrom .confusion import validate_confusion_matrix\n\n_N_PRECOMP = 2_000_000\n_precomp_cache = {}\n\n\ndef _params_key(params):\n    items = []\n    for k, v in sorted(params.items()):\n        if isinstance(v, np.ndarray):\n            items.append((k, tuple(v.flat)))\n        else:\n            items.append((k, v))\n    return tuple(items)\n\n\ndef _precompute(topology, params, K, seed=999):\n    \"\"\"Precompute sufficient statistics for plim calculation.\"\"\"\n    cache_key = (topology, _params_key(params), K)\n    if cache_key in _precomp_cache:\n        return _precomp_cache[cache_key]\n\n    rng = np.random.default_rng(seed)\n    data = GEN_FUNCS[topology](_N_PRECOMP, params=params, rng=rng)\n    Y = data[\"Y\"]\n    A = data[\"A\"]\n\n    DA = np.zeros((_N_PRECOMP, K))\n    for k in range(K):\n        DA[:, k] = (A == k).astype(float)\n\n    stats = {\n        \"E_Y\": Y.mean(),\n        \"E_DA\": DA.mean(0),\n        \"E_DA_Y\": (DA * Y[:, None]).mean(0),\n    }\n\n    if topology in HAS_TREATMENT:\n        T = data[\"T\"]\n        stats.update({\n            \"E_T\": T.mean(),\n            \"E_T2\": (T ** 2).mean(),\n            \"E_TY\": (T * Y).mean(),\n            \"E_DA_T\": (DA * T[:, None]).mean(0),\n        })\n\n    _precomp_cache[cache_key] = stats\n    return stats\n\n\ndef _plim_with_T(C, stats, K):\n    \"\"\"OLS plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}.\"\"\"\n    ds = C @ stats[\"E_DA\"]\n    dst = C @ stats[\"E_DA_T\"]\n    dsy = C @ stats[\"E_DA_Y\"]\n    ET, ET2 = stats[\"E_T\"], stats[\"E_T2\"]\n    EY, ETY = stats[\"E_Y\"], stats[\"E_TY\"]\n\n    dim = 1 + K  # intercept + T + (K-1) dummies\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    EZZ[0, 1] = EZZ[1, 0] = ET\n    EZZ[1, 1] = ET2\n    for j in range(1, K):\n        idx = j + 1\n        EZZ[0, idx] = EZZ[idx, 0] = ds[j]\n        EZZ[1, idx] = EZZ[idx, 1] = dst[j]\n        EZZ[idx, idx] = ds[j]\n\n    EZY = np.zeros(dim)\n    EZY[0] = EY\n    EZY[1] = ETY\n    for j in range(1, K):\n        EZY[j + 1] = dsy[j]\n\n    cond = np.linalg.cond(EZZ)\n    if cond > 1e12:\n        warnings.warn(\n            f\"EZZ condition number {cond:.1e} — plim may be numerically unstable\"\n        )\n\n    return np.linalg.solve(EZZ, EZY)\n\n\ndef _plim_no_T(C, stats, K):\n    \"\"\"OLS plim for Y ~ 1 + D*_1 + ... + D*_{K-1}.\"\"\"\n    ds = C @ stats[\"E_DA\"]\n    dsy = C @ stats[\"E_DA_Y\"]\n    EY = stats[\"E_Y\"]\n\n    dim = K  # intercept + (K-1) dummies\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    for j in range(1, K):\n        EZZ[0, j] = EZZ[j, 0] = ds[j]\n        EZZ[j, j] = ds[j]\n\n    EZY = np.zeros(dim)\n    EZY[0] = EY\n    for j in range(1, K):\n        EZY[j] = dsy[j]\n\n    cond = np.linalg.cond(EZZ)\n    if cond > 1e12:\n        warnings.warn(\n            f\"EZZ condition number {cond:.1e} — plim may be numerically unstable\"\n        )\n\n    return np.linalg.solve(EZZ, EZY)\n\n\ndef _get_tau(topology, C, stats, K):\n    \"\"\"Extract target coefficient from plim vector.\n\n    For topologies with T: coefficient index 1 (treatment effect).\n    For topologies without T: coefficient index 1 (first dummy).\n    \"\"\"\n    if topology in HAS_TREATMENT:\n        coefs = _plim_with_T(C, stats, K)\n    else:\n        coefs = _plim_no_T(C, stats, K)\n    return coefs[1]\n\n\ndef compute_bias(topology, C, params=None):\n    \"\"\"Compute annotation-error bias for a given topology and confusion matrix.\n\n    Args:\n        topology: one of \"confounding\", \"mediation\", \"collider\", \"exposure\",\n                  \"mbias\", \"iv\", \"frontdoor\"\n        C: (K, K) column-stochastic confusion matrix, C[j,i] = P(A*=j|A=i)\n        params: optional DGP parameters dict, None uses defaults\n\n    Returns:\n        dict with tau_true, tau_biased, bias, bias_pct, topology\n    \"\"\"\n    if topology not in TOPOLOGIES:\n        raise ValueError(f\"Unknown topology: {topology}. Choose from {TOPOLOGIES}\")\n    if not validate_confusion_matrix(C):\n        raise ValueError(\"C must be a square, non-negative, column-stochastic matrix\")\n\n    K = C.shape[0]\n    merged = dict(DEFAULT_PARAMS[topology])\n    if params is not None:\n        merged.update(params)\n\n    stats = _precompute(topology, merged, K)\n    tau_true = _get_tau(topology, np.eye(K), stats, K)\n    tau_biased = _get_tau(topology, C, stats, K)\n    bias = tau_biased - tau_true\n    bias_pct = 100.0 * bias / tau_true if abs(tau_true) > 1e-12 else float(\"nan\")\n\n    return {\n        \"tau_true\": float(tau_true),\n        \"tau_biased\": float(tau_biased),\n        \"bias\": float(bias),\n        \"bias_pct\": float(bias_pct),\n        \"topology\": topology,\n    }\n\n\ndef clear_cache():\n    \"\"\"Clear the precomputed statistics cache.\"\"\"\n    _precomp_cache.clear()\n",
      "numLines": 174,
      "startLine": 1,
      "totalLines": 174
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01MQpxZKPVczFB9PBqvNUbLr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/dgp.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "b7fd0a1f-fbee-4378-9660-93c06aaabf80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Byz4Q64JNAbiejma3RxERa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15010,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15010
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

### Tool result

_source line 11 · 2026-05-20T23:51:07.530Z_

<details><summary>↩ Tool result · `toolu_01MQpxZKPVczFB9PBqvNUbLr`</summary>

```text
1	"""Data generation processes for 7 DAG topologies.
2	
3	Each topology generates synthetic data with a known causal structure.
4	The variable A (or M for frontdoor) is the one subject to misclassification.
5	"""
6	
7	import numpy as np
8	from .utils import softmax_sample, make_dummies
9	
10	DEFAULT_PARAMS = {
11	    "confounding": dict(
12	        p_A=np.array([0.40, 0.35, 0.25]),
13	        alpha=np.array([1.5, -1.0]),
14	        beta_A=np.array([1.0, -0.5]),
15	        beta_T=2.0, sigma_T=1.0),
16	    "mediation": dict(
17	        tau=0.5,
18	        gamma=np.array([0.0, 0.5, -0.3]),
19	        delta=np.array([0.0, 0.8, -0.6]),
20	        beta=np.array([0.0, 1.0, -0.5])),
21	    "collider": dict(
22	        tau=1.0,
23	        g=np.array([0.0, 0.0, 0.0]),
24	        dT=np.array([0.0, 0.5, -0.3]),
25	        dY=np.array([0.0, 0.8, 0.6])),
26	    "exposure": dict(
27	        beta=np.array([0.0, 1.0, -0.5]),
28	        p_A=np.array([0.40, 0.35, 0.25])),
29	    "mbias": dict(
30	        tau=1.0, delta_coef=1.0, lam=1.0,
31	        g=np.array([0.0, 0.0, 0.0]),
32	        a1=np.array([0.0, 0.8, -0.5]),
33	        a2=np.array([0.0, 0.6, 0.9])),
34	    "iv": dict(
35	        lam=1.0,
36	        g=np.array([0.0, 0.0, 0.0]),
37	        dZ=np.array([0.0, 1.0, -0.5]),
38	        dU=np.array([0.0, 0.8, 0.6]),
39	        beta=np.array([0.0, 1.0, -0.5])),
40	    "frontdoor": dict(
41	        alpha_U=1.0, lam_U=1.0,
42	        gamma=np.array([0.0, 0.5, -0.3]),
43	        delta=np.array([0.0, 1.0, -0.8]),
44	        beta=np.array([0.0, 1.0, -0.5])),
45	}
46	
47	TOPOLOGIES = list(DEFAULT_PARAMS.keys())
48	
49	HAS_TREATMENT = {"confounding", "mediation", "collider", "mbias", "frontdoor"}
50	NO_TREATMENT = {"exposure", "iv"}
51	
52	
53	def _get_rng(rng, seed):
54	    if rng is not None:
55	        return rng
56	    return np.random.default_rng(seed)
57	
58	
59	def _get_params(topology, params):
60	    p = dict(DEFAULT_PARAMS[topology])
61	    if params is not None:
62	        p.update(params)
63	    return p
64	
65	
66	def gen_confounding(N, params=None, rng=None, seed=None):
67	    """A->T, A->Y, T->Y. Researcher controls for A*.
68	
69	    Returns:
70	        dict with keys T, Y, A
71	    """
72	    rng = _get_rng(rng, seed)
73	    p = _get_params("confounding", params)
74	    K = len(p["p_A"])
75	    A = rng.choice(K, size=N, p=p["p_A"])
76	    D = make_dummies(A, K)
77	    T = D @ p["alpha"] + rng.normal(0, p["sigma_T"], N)
78	    Y = p["beta_T"] * T + D @ p["beta_A"] + rng.normal(0, 1, N)
79	    return {"T": T, "Y": Y, "A": A}
80	
81	
82	def gen_mediation(N, params=None, rng=None, seed=None):
83	    """T->A->Y. A mediates; researcher controls for A*.
84	
85	    Returns:
86	        dict with keys T, Y, A
87	    """
88	    rng = _get_rng(rng, seed)
89	    p = _get_params("mediation", params)
90	    T = rng.binomial(1, 0.5, N).astype(float)
91	    K = len(p["gamma"])
92	    logits = p["gamma"][None, :] + p["delta"][None, :] * T[:, None]
93	    A = softmax_sample(logits, rng)
94	    D = make_dummies(A, K)
95	    Y = p["beta"][0] + D @ p["beta"][1:] + p["tau"] * T + rng.normal(0, 1, N)
96	    return {"T": T, "Y": Y, "A": A}
97	
98	
99	def gen_collider(N, params=None, rng=None, seed=None):
100	    """T->A<-Y. Researcher wrongly controls for A*.
101	
102	    Returns:
103	        dict with keys T, Y, A
104	    """
105	    rng = _get_rng(rng, seed)
106	    p = _get_params("collider", params)
107	    T = rng.normal(0, 1, N)
108	    Y = p["tau"] * T + rng.normal(0, 1, N)
109	    logits = (p["g"][None, :] + p["dT"][None, :] * T[:, None]
110	              + p["dY"][None, :] * Y[:, None])
111	    A = softmax_sample(logits, rng)
112	    return {"T": T, "Y": Y, "A": A}
113	
114	
115	def gen_exposure(N, params=None, rng=None, seed=None):
116	    """A->Y (direct exposure, no treatment T).
117	
118	    Returns:
119	        dict with keys Y, A
120	    """
121	    rng = _get_rng(rng, seed)
122	    p = _get_params("exposure", params)
123	    K = len(p["p_A"])
124	    A = rng.choice(K, size=N, p=p["p_A"])
125	    D = make_dummies(A, K)
126	    Y = p["beta"][0] + D @ p["beta"][1:] + rng.normal(0, 1, N)
127	    return {"Y": Y, "A": A}
128	
129	
130	def gen_mbias(N, params=None, rng=None, seed=None):
131	    """U1->{A,T}, U2->{A,Y}, T->Y. Conditioning on A* induces M-bias.
132	
133	    Returns:
134	        dict with keys T, Y, A
135	    """
136	    rng = _get_rng(rng, seed)
137	    p = _get_params("mbias", params)
138	    N_out = N
139	    U1, U2 = rng.normal(0, 1, N_out), rng.normal(0, 1, N_out)
140	    T = p["delta_coef"] * U1 + rng.normal(0, 1, N_out)
141	    logits = (p["g"][None, :] + p["a1"][None, :] * U1[:, None]
142	              + p["a2"][None, :] * U2[:, None])
143	    A = softmax_sample(logits, rng)
144	    Y = p["tau"] * T + p["lam"] * U2 + rng.normal(0, 1, N_out)
145	    return {"T": T, "Y": Y, "A": A}
146	
147	
148	def gen_iv(N, params=None, rng=None, seed=None):
149	    """Z->A->Y, U->{A,Y}. IV topology with endogenous A.
150	
151	    Returns:
152	        dict with keys Z, Y, A
153	    """
154	    rng = _get_rng(rng, seed)
155	    p = _get_params("iv", params)
156	    K = len(p["g"])
157	    Z = rng.normal(0, 1, N)
158	    U = rng.normal(0, 1, N)
159	    logits = (p["g"][None, :] + p["dZ"][None, :] * Z[:, None]
160	              + p["dU"][None, :] * U[:, None])
161	    A = softmax_sample(logits, rng)
162	    D = make_dummies(A, K)
163	    Y = p["beta"][0] + D @ p["beta"][1:] + p["lam"] * U + rng.normal(0, 1, N)
164	    return {"Z": Z, "Y": Y, "A": A}
165	
166	
167	def gen_frontdoor(N, params=None, rng=None, seed=None):
168	    """T->M->Y, U->{T,Y}. Misclassified variable is M (mediator, stored as A).
169	
170	    Returns:
171	        dict with keys T, Y, A (A is the mediator M)
172	    """
173	    rng = _get_rng(rng, seed)
174	    p = _get_params("frontdoor", params)
175	    U = rng.normal(0, 1, N)
176	    T = p["alpha_U"] * U + rng.normal(0, 1, N)
177	    K = len(p["gamma"])
178	    logits = p["gamma"][None, :] + p["delta"][None, :] * T[:, None]
179	    A = softmax_sample(logits, rng)
180	    D = make_dummies(A, K)
181	    Y = p["beta"][0] + D @ p["beta"][1:] + p["lam_U"] * U + rng.normal(0, 1, N)
182	    return {"T": T, "Y": Y, "A": A}
183	
184	
185	GEN_FUNCS = {
186	    "confounding": gen_confounding,
187	    "mediation": gen_mediation,
188	    "collider": gen_collider,
189	    "exposure": gen_exposure,
190	    "mbias": gen_mbias,
191	    "iv": gen_iv,
192	    "frontdoor": gen_frontdoor,
193	}
194	
195	
196	def generate_data(topology, N, params=None, rng=None, seed=None):
197	    """Generate synthetic data for a given topology.
198	
199	    Args:
200	        topology: one of "confounding", "mediation", "collider", "exposure",
201	                  "mbias", "iv", "frontdoor"
202	        N: sample size
203	        params: optional DGP parameter overrides
204	        rng: numpy random Generator
205	        seed: random seed (used if rng is None)
206	
207	    Returns:
208	        dict with generated variables (topology-dependent keys)
209	    """
210	    if topology not in GEN_FUNCS:
211	        raise ValueError(f"Unknown topology: {topology}. Choose from {TOPOLOGIES}")
212	    return GEN_FUNCS[topology](N, params=params, rng=rng, seed=seed)
213	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "06a3db00-8247-474d-9cfe-bdcb1b5c51dd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/dgp.py",
      "content": "\"\"\"Data generation processes for 7 DAG topologies.\n\nEach topology generates synthetic data with a known causal structure.\nThe variable A (or M for frontdoor) is the one subject to misclassification.\n\"\"\"\n\nimport numpy as np\nfrom .utils import softmax_sample, make_dummies\n\nDEFAULT_PARAMS = {\n    \"confounding\": dict(\n        p_A=np.array([0.40, 0.35, 0.25]),\n        alpha=np.array([1.5, -1.0]),\n        beta_A=np.array([1.0, -0.5]),\n        beta_T=2.0, sigma_T=1.0),\n    \"mediation\": dict(\n        tau=0.5,\n        gamma=np.array([0.0, 0.5, -0.3]),\n        delta=np.array([0.0, 0.8, -0.6]),\n        beta=np.array([0.0, 1.0, -0.5])),\n    \"collider\": dict(\n        tau=1.0,\n        g=np.array([0.0, 0.0, 0.0]),\n        dT=np.array([0.0, 0.5, -0.3]),\n        dY=np.array([0.0, 0.8, 0.6])),\n    \"exposure\": dict(\n        beta=np.array([0.0, 1.0, -0.5]),\n        p_A=np.array([0.40, 0.35, 0.25])),\n    \"mbias\": dict(\n        tau=1.0, delta_coef=1.0, lam=1.0,\n        g=np.array([0.0, 0.0, 0.0]),\n        a1=np.array([0.0, 0.8, -0.5]),\n        a2=np.array([0.0, 0.6, 0.9])),\n    \"iv\": dict(\n        lam=1.0,\n        g=np.array([0.0, 0.0, 0.0]),\n        dZ=np.array([0.0, 1.0, -0.5]),\n        dU=np.array([0.0, 0.8, 0.6]),\n        beta=np.array([0.0, 1.0, -0.5])),\n    \"frontdoor\": dict(\n        alpha_U=1.0, lam_U=1.0,\n        gamma=np.array([0.0, 0.5, -0.3]),\n        delta=np.array([0.0, 1.0, -0.8]),\n        beta=np.array([0.0, 1.0, -0.5])),\n}\n\nTOPOLOGIES = list(DEFAULT_PARAMS.keys())\n\nHAS_TREATMENT = {\"confounding\", \"mediation\", \"collider\", \"mbias\", \"frontdoor\"}\nNO_TREATMENT = {\"exposure\", \"iv\"}\n\n\ndef _get_rng(rng, seed):\n    if rng is not None:\n        return rng\n    return np.random.default_rng(seed)\n\n\ndef _get_params(topology, params):\n    p = dict(DEFAULT_PARAMS[topology])\n    if params is not None:\n        p.update(params)\n    return p\n\n\ndef gen_confounding(N, params=None, rng=None, seed=None):\n    \"\"\"A->T, A->Y, T->Y. Researcher controls for A*.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"confounding\", params)\n    K = len(p[\"p_A\"])\n    A = rng.choice(K, size=N, p=p[\"p_A\"])\n    D = make_dummies(A, K)\n    T = D @ p[\"alpha\"] + rng.normal(0, p[\"sigma_T\"], N)\n    Y = p[\"beta_T\"] * T + D @ p[\"beta_A\"] + rng.normal(0, 1, N)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_mediation(N, params=None, rng=None, seed=None):\n    \"\"\"T->A->Y. A mediates; researcher controls for A*.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"mediation\", params)\n    T = rng.binomial(1, 0.5, N).astype(float)\n    K = len(p[\"gamma\"])\n    logits = p[\"gamma\"][None, :] + p[\"delta\"][None, :] * T[:, None]\n    A = softmax_sample(logits, rng)\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + p[\"tau\"] * T + rng.normal(0, 1, N)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_collider(N, params=None, rng=None, seed=None):\n    \"\"\"T->A<-Y. Researcher wrongly controls for A*.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"collider\", params)\n    T = rng.normal(0, 1, N)\n    Y = p[\"tau\"] * T + rng.normal(0, 1, N)\n    logits = (p[\"g\"][None, :] + p[\"dT\"][None, :] * T[:, None]\n              + p[\"dY\"][None, :] * Y[:, None])\n    A = softmax_sample(logits, rng)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_exposure(N, params=None, rng=None, seed=None):\n    \"\"\"A->Y (direct exposure, no treatment T).\n\n    Returns:\n        dict with keys Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"exposure\", params)\n    K = len(p[\"p_A\"])\n    A = rng.choice(K, size=N, p=p[\"p_A\"])\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + rng.normal(0, 1, N)\n    return {\"Y\": Y, \"A\": A}\n\n\ndef gen_mbias(N, params=None, rng=None, seed=None):\n    \"\"\"U1->{A,T}, U2->{A,Y}, T->Y. Conditioning on A* induces M-bias.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"mbias\", params)\n    N_out = N\n    U1, U2 = rng.normal(0, 1, N_out), rng.normal(0, 1, N_out)\n    T = p[\"delta_coef\"] * U1 + rng.normal(0, 1, N_out)\n    logits = (p[\"g\"][None, :] + p[\"a1\"][None, :] * U1[:, None]\n              + p[\"a2\"][None, :] * U2[:, None])\n    A = softmax_sample(logits, rng)\n    Y = p[\"tau\"] * T + p[\"lam\"] * U2 + rng.normal(0, 1, N_out)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_iv(N, params=None, rng=None, seed=None):\n    \"\"\"Z->A->Y, U->{A,Y}. IV topology with endogenous A.\n\n    Returns:\n        dict with keys Z, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"iv\", params)\n    K = len(p[\"g\"])\n    Z = rng.normal(0, 1, N)\n    U = rng.normal(0, 1, N)\n    logits = (p[\"g\"][None, :] + p[\"dZ\"][None, :] * Z[:, None]\n              + p[\"dU\"][None, :] * U[:, None])\n    A = softmax_sample(logits, rng)\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + p[\"lam\"] * U + rng.normal(0, 1, N)\n    return {\"Z\": Z, \"Y\": Y, \"A\": A}\n\n\ndef gen_frontdoor(N, params=None, rng=None, seed=None):\n    \"\"\"T->M->Y, U->{T,Y}. Misclassified variable is M (mediator, stored as A).\n\n    Returns:\n        dict with keys T, Y, A (A is the mediator M)\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"frontdoor\", params)\n    U = rng.normal(0, 1, N)\n    T = p[\"alpha_U\"] * U + rng.normal(0, 1, N)\n    K = len(p[\"gamma\"])\n    logits = p[\"gamma\"][None, :] + p[\"delta\"][None, :] * T[:, None]\n    A = softmax_sample(logits, rng)\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + p[\"lam_U\"] * U + rng.normal(0, 1, N)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\nGEN_FUNCS = {\n    \"confounding\": gen_confounding,\n    \"mediation\": gen_mediation,\n    \"collider\": gen_collider,\n    \"exposure\": gen_exposure,\n    \"mbias\": gen_mbias,\n    \"iv\": gen_iv,\n    \"frontdoor\": gen_frontdoor,\n}\n\n\ndef generate_data(topology, N, params=None, rng=None, seed=None):\n    \"\"\"Generate synthetic data for a given topology.\n\n    Args:\n        topology: one of \"confounding\", \"mediation\", \"collider\", \"exposure\",\n                  \"mbias\", \"iv\", \"frontdoor\"\n        N: sample size\n        params: optional DGP parameter overrides\n        rng: numpy random Generator\n        seed: random seed (used if rng is None)\n\n    Returns:\n        dict with generated variables (topology-dependent keys)\n    \"\"\"\n    if topology not in GEN_FUNCS:\n        raise ValueError(f\"Unknown topology: {topology}. Choose from {TOPOLOGIES}\")\n    return GEN_FUNCS[topology](N, params=params, rng=rng, seed=seed)\n",
      "numLines": 213,
      "startLine": 1,
      "totalLines": 213
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01DRcBktzPZMuTi4kBNFTuiF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/__init__.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "87abc8e2-dd05-4502-8fec-19d88b94a813",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Byz4Q64JNAbiejma3RxERa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15010,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15010
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

### Tool result

_source line 13 · 2026-05-20T23:51:07.832Z_

<details><summary>↩ Tool result · `toolu_01DRcBktzPZMuTi4kBNFTuiF`</summary>

```text
1	"""annot_sensitivity: Annotation-error sensitivity analysis for causal inference.
2	
3	Computes how LLM annotation misclassification propagates bias through
4	7 DAG topologies, with ASV sensitivity measures and 5 correction methods.
5	"""
6	
7	from .bias import compute_bias, clear_cache
8	from .asv import compute_asv
9	from .correction import (
10	    recommend_correction,
11	    correct_naive_plugin,
12	    correct_dsl,
13	    correct_ppi,
14	    correct_mcsimex,
15	    correct_mla,
16	    METHODS,
17	)
18	from .confusion import (
19	    validate_confusion_matrix,
20	    random_confusion_matrix,
21	    interpolate_confusion,
22	    predefined_matrices,
23	    delta_range,
24	)
25	from .dgp import generate_data, TOPOLOGIES, DEFAULT_PARAMS, GEN_FUNCS
26	from .utils import ols, ols_with_se, make_dummies, softmax_sample, misclassify
27	
28	__all__ = [
29	    "compute_bias",
30	    "compute_asv",
31	    "recommend_correction",
32	    "correct_naive_plugin",
33	    "correct_dsl",
34	    "correct_ppi",
35	    "correct_mcsimex",
36	    "correct_mla",
37	    "validate_confusion_matrix",
38	    "random_confusion_matrix",
39	    "interpolate_confusion",
40	    "predefined_matrices",
41	    "delta_range",
42	    "generate_data",
43	    "clear_cache",
44	    "TOPOLOGIES",
45	    "DEFAULT_PARAMS",
46	    "METHODS",
47	    "GEN_FUNCS",
48	    "ols",
49	    "ols_with_se",
50	    "make_dummies",
51	    "softmax_sample",
52	    "misclassify",
53	]
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "a8d5b198-4ccf-4cd1-8527-72c29f9877c7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/__init__.py",
      "content": "\"\"\"annot_sensitivity: Annotation-error sensitivity analysis for causal inference.\n\nComputes how LLM annotation misclassification propagates bias through\n7 DAG topologies, with ASV sensitivity measures and 5 correction methods.\n\"\"\"\n\nfrom .bias import compute_bias, clear_cache\nfrom .asv import compute_asv\nfrom .correction import (\n    recommend_correction,\n    correct_naive_plugin,\n    correct_dsl,\n    correct_ppi,\n    correct_mcsimex,\n    correct_mla,\n    METHODS,\n)\nfrom .confusion import (\n    validate_confusion_matrix,\n    random_confusion_matrix,\n    interpolate_confusion,\n    predefined_matrices,\n    delta_range,\n)\nfrom .dgp import generate_data, TOPOLOGIES, DEFAULT_PARAMS, GEN_FUNCS\nfrom .utils import ols, ols_with_se, make_dummies, softmax_sample, misclassify\n\n__all__ = [\n    \"compute_bias\",\n    \"compute_asv\",\n    \"recommend_correction\",\n    \"correct_naive_plugin\",\n    \"correct_dsl\",\n    \"correct_ppi\",\n    \"correct_mcsimex\",\n    \"correct_mla\",\n    \"validate_confusion_matrix\",\n    \"random_confusion_matrix\",\n    \"interpolate_confusion\",\n    \"predefined_matrices\",\n    \"delta_range\",\n    \"generate_data\",\n    \"clear_cache\",\n    \"TOPOLOGIES\",\n    \"DEFAULT_PARAMS\",\n    \"METHODS\",\n    \"GEN_FUNCS\",\n    \"ols\",\n    \"ols_with_se\",\n    \"make_dummies\",\n    \"softmax_sample\",\n    \"misclassify\",\n]\n",
      "numLines": 54,
      "startLine": 1,
      "totalLines": 54
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the remaining files I need: the ASV module, the correction module, and the existing tests.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "903477e1-ed03-4ea4-b770-db61935c8cf2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQbEmFPpg3WkXvGvZH8S1P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21029,
      "cache_read_input_tokens": 26851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21029
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

_source line 15_

Now let me read the ASV module, correction module, and existing tests.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "c968d7af-7463-4800-93d4-13c3c8e90495",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQbEmFPpg3WkXvGvZH8S1P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21029,
      "cache_read_input_tokens": 26851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21029
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

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01M3cm7UqNosS7SVaE5RSzLJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/asv.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "2f70b3e1-e22f-4797-ba22-8e93709eca3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQbEmFPpg3WkXvGvZH8S1P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21029,
      "cache_read_input_tokens": 26851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21029
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

_source line 17 · 2026-05-20T23:51:13.097Z_

<details><summary>↩ Tool result · `toolu_01M3cm7UqNosS7SVaE5RSzLJ`</summary>

```text
1	"""Annotation Sensitivity Value (ASV) computation.
2	
3	ASV measures how much misclassification is needed to cross a bias threshold,
4	using the C(delta) = (1-delta)*I + delta*C0 interpolation path.
5	"""
6	
7	import numpy as np
8	from .bias import _precompute, _get_tau
9	from .confusion import validate_confusion_matrix, interpolate_confusion, delta_range
10	from .dgp import DEFAULT_PARAMS, TOPOLOGIES
11	
12	
13	def _compute_bias_curve(topology, C0, stats, K, tau_true, n_grid=1500):
14	    dmin, dmax = delta_range(C0)
15	    deltas = np.linspace(dmin, dmax, n_grid)
16	    tau_curve = np.zeros(n_grid)
17	    for i, d in enumerate(deltas):
18	        C_d = interpolate_confusion(C0, d)
19	        tau_curve[i] = _get_tau(topology, C_d, stats, K)
20	    bias_abs = np.abs(tau_curve - tau_true)
21	    return deltas, bias_abs, tau_curve
22	
23	
24	def _compute_envelope(bias_abs):
25	    env = np.zeros_like(bias_abs)
26	    running_max = 0.0
27	    for i in range(len(bias_abs)):
28	        v = bias_abs[i]
29	        if not np.isnan(v):
30	            running_max = max(running_max, v)
31	        env[i] = running_max
32	    return env
33	
34	
35	def _find_threshold_crossing(envelope, deltas, tau_curve, tau_true,
36	                             threshold_type, threshold_value):
37	    if threshold_type == "magnitude":
38	        if abs(tau_true) < 1e-12:
39	            return None
40	        thresh = threshold_value * abs(tau_true)
41	        for i in range(len(deltas)):
42	            if envelope[i] > thresh:
43	                return float(deltas[i])
44	        return None
45	    elif threshold_type == "sign_flip":
46	        if abs(tau_true) < 1e-12:
47	            return None
48	        baseline_sign = np.sign(tau_true)
49	        for i in range(len(deltas)):
50	            if np.isnan(tau_curve[i]):
51	                continue
52	            if np.sign(tau_curve[i]) != baseline_sign:
53	                return float(deltas[i])
54	        return None
55	    elif threshold_type == "significance":
56	        z_crit = 1.96
57	        for i in range(len(deltas)):
58	            if np.isnan(tau_curve[i]):
59	                continue
60	            if abs(tau_curve[i]) < z_crit * threshold_value:
61	                return float(deltas[i])
62	        return None
63	    else:
64	        raise ValueError(
65	            f"Unknown threshold_type: {threshold_type}. "
66	            f"Choose from 'magnitude', 'significance', 'sign_flip'"
67	        )
68	
69	
70	def compute_asv(topology, C0, params=None, threshold_type="magnitude",
71	                threshold_value=0.1, n_grid=1500):
72	    """Compute Annotation Sensitivity Value for a topology and base confusion matrix.
73	
74	    ASV is the minimum interpolation delta at which a bias threshold is crossed
75	    along the path C(delta) = (1-delta)*I + delta*C0.
76	
77	    Args:
78	        topology: one of 7 DAG types
79	        C0: (K, K) base confusion matrix
80	        params: optional DGP parameters dict
81	        threshold_type: "magnitude" (relative to tau_true),
82	                        "significance" (threshold_value = SE),
83	                        "sign_flip" (sign of tau changes)
84	        threshold_value: threshold parameter (meaning depends on threshold_type)
85	        n_grid: number of delta grid points
86	
87	    Returns:
88	        dict with asv, bias_curve, envelope, deltas, tau_true
89	    """
90	    if topology not in TOPOLOGIES:
91	        raise ValueError(f"Unknown topology: {topology}. Choose from {TOPOLOGIES}")
92	    if not validate_confusion_matrix(C0):
93	        raise ValueError("C0 must be a valid column-stochastic matrix")
94	
95	    K = C0.shape[0]
96	    merged = dict(DEFAULT_PARAMS[topology])
97	    if params is not None:
98	        merged.update(params)
99	
100	    stats = _precompute(topology, merged, K)
101	    tau_true = _get_tau(topology, np.eye(K), stats, K)
102	
103	    deltas, bias_abs, tau_curve = _compute_bias_curve(
104	        topology, C0, stats, K, tau_true, n_grid
105	    )
106	    envelope = _compute_envelope(bias_abs)
107	
108	    asv = _find_threshold_crossing(
109	        envelope, deltas, tau_curve, tau_true, threshold_type, threshold_value
110	    )
111	
112	    return {
113	        "asv": asv,
114	        "bias_curve": bias_abs,
115	        "envelope": envelope,
116	        "deltas": deltas,
117	        "tau_true": float(tau_true),
118	    }
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "18d09de1-aaec-4fc6-a359-94162c586885",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/asv.py",
      "content": "\"\"\"Annotation Sensitivity Value (ASV) computation.\n\nASV measures how much misclassification is needed to cross a bias threshold,\nusing the C(delta) = (1-delta)*I + delta*C0 interpolation path.\n\"\"\"\n\nimport numpy as np\nfrom .bias import _precompute, _get_tau\nfrom .confusion import validate_confusion_matrix, interpolate_confusion, delta_range\nfrom .dgp import DEFAULT_PARAMS, TOPOLOGIES\n\n\ndef _compute_bias_curve(topology, C0, stats, K, tau_true, n_grid=1500):\n    dmin, dmax = delta_range(C0)\n    deltas = np.linspace(dmin, dmax, n_grid)\n    tau_curve = np.zeros(n_grid)\n    for i, d in enumerate(deltas):\n        C_d = interpolate_confusion(C0, d)\n        tau_curve[i] = _get_tau(topology, C_d, stats, K)\n    bias_abs = np.abs(tau_curve - tau_true)\n    return deltas, bias_abs, tau_curve\n\n\ndef _compute_envelope(bias_abs):\n    env = np.zeros_like(bias_abs)\n    running_max = 0.0\n    for i in range(len(bias_abs)):\n        v = bias_abs[i]\n        if not np.isnan(v):\n            running_max = max(running_max, v)\n        env[i] = running_max\n    return env\n\n\ndef _find_threshold_crossing(envelope, deltas, tau_curve, tau_true,\n                             threshold_type, threshold_value):\n    if threshold_type == \"magnitude\":\n        if abs(tau_true) < 1e-12:\n            return None\n        thresh = threshold_value * abs(tau_true)\n        for i in range(len(deltas)):\n            if envelope[i] > thresh:\n                return float(deltas[i])\n        return None\n    elif threshold_type == \"sign_flip\":\n        if abs(tau_true) < 1e-12:\n            return None\n        baseline_sign = np.sign(tau_true)\n        for i in range(len(deltas)):\n            if np.isnan(tau_curve[i]):\n                continue\n            if np.sign(tau_curve[i]) != baseline_sign:\n                return float(deltas[i])\n        return None\n    elif threshold_type == \"significance\":\n        z_crit = 1.96\n        for i in range(len(deltas)):\n            if np.isnan(tau_curve[i]):\n                continue\n            if abs(tau_curve[i]) < z_crit * threshold_value:\n                return float(deltas[i])\n        return None\n    else:\n        raise ValueError(\n            f\"Unknown threshold_type: {threshold_type}. \"\n            f\"Choose from 'magnitude', 'significance', 'sign_flip'\"\n        )\n\n\ndef compute_asv(topology, C0, params=None, threshold_type=\"magnitude\",\n                threshold_value=0.1, n_grid=1500):\n    \"\"\"Compute Annotation Sensitivity Value for a topology and base confusion matrix.\n\n    ASV is the minimum interpolation delta at which a bias threshold is crossed\n    along the path C(delta) = (1-delta)*I + delta*C0.\n\n    Args:\n        topology: one of 7 DAG types\n        C0: (K, K) base confusion matrix\n        params: optional DGP parameters dict\n        threshold_type: \"magnitude\" (relative to tau_true),\n                        \"significance\" (threshold_value = SE),\n                        \"sign_flip\" (sign of tau changes)\n        threshold_value: threshold parameter (meaning depends on threshold_type)\n        n_grid: number of delta grid points\n\n    Returns:\n        dict with asv, bias_curve, envelope, deltas, tau_true\n    \"\"\"\n    if topology not in TOPOLOGIES:\n        raise ValueError(f\"Unknown topology: {topology}. Choose from {TOPOLOGIES}\")\n    if not validate_confusion_matrix(C0):\n        raise ValueError(\"C0 must be a valid column-stochastic matrix\")\n\n    K = C0.shape[0]\n    merged = dict(DEFAULT_PARAMS[topology])\n    if params is not None:\n        merged.update(params)\n\n    stats = _precompute(topology, merged, K)\n    tau_true = _get_tau(topology, np.eye(K), stats, K)\n\n    deltas, bias_abs, tau_curve = _compute_bias_curve(\n        topology, C0, stats, K, tau_true, n_grid\n    )\n    envelope = _compute_envelope(bias_abs)\n\n    asv = _find_threshold_crossing(\n        envelope, deltas, tau_curve, tau_true, threshold_type, threshold_value\n    )\n\n    return {\n        \"asv\": asv,\n        \"bias_curve\": bias_abs,\n        \"envelope\": envelope,\n        \"deltas\": deltas,\n        \"tau_true\": float(tau_true),\n    }\n",
      "numLines": 119,
      "startLine": 1,
      "totalLines": 119
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_018DTr7bTyahPuWCPBaYT1gx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/correction.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "8f139451-972a-4cd3-ba94-0bbb3c4b3619",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQbEmFPpg3WkXvGvZH8S1P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21029,
      "cache_read_input_tokens": 26851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21029
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

_source line 19 · 2026-05-20T23:51:13.553Z_

<details><summary>↩ Tool result · `toolu_018DTr7bTyahPuWCPBaYT1gx`</summary>

```text
1	"""Correction methods and recommendation engine for annotation-error bias.
2	
3	Five correction methods:
4	  - naive_plugin: C^{-1} correction of dummy indicators
5	  - dsl: EM-based joint estimation of regression params and C
6	  - ppi: PPI++ combining gold-standard and full-sample estimates
7	  - mcsimex: MC-SIMEX extrapolation to lambda=-1
8	  - mla: Matrix-based label adjustment via D*_full @ C^{-1}
9	
10	Key finding (FWL theorem): naive_plugin and mla correct dummy coefficients
11	but NOT the treatment coefficient in regressions with a separate treatment T.
12	"""
13	
14	import numpy as np
15	from .utils import ols, ols_with_se, make_dummies, make_full_dummies, misclassify
16	
17	METHODS = ["naive_plugin", "dsl", "ppi", "mcsimex", "mla"]
18	
19	_EM_MAX_ITER = 100
20	_EM_TOL = 1e-6
21	_SIMEX_LAMBDAS = [0.5, 1.0, 1.5, 2.0]
22	_SIMEX_B = 50
23	
24	
25	def correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1):
26	    """Correct using C^{-1} applied per-observation to dummy indicators.
27	
28	    Args:
29	        X_other: (N, p) non-A regressors (includes intercept)
30	        Y: (N,) outcome
31	        Astar: (N,) misclassified labels
32	        C: (K, K) confusion matrix
33	        tau_idx: index of target coefficient in full design
34	
35	    Returns:
36	        (tau_hat, se, success) tuple
37	    """
38	    cond = np.linalg.cond(C)
39	    if cond > 1e12:
40	        return np.nan, np.nan, False
41	    try:
42	        C_inv = np.linalg.inv(C)
43	    except np.linalg.LinAlgError:
44	        return np.nan, np.nan, False
45	    D_corrected = C_inv[:, Astar].T[:, 1:]
46	    X = np.column_stack([X_other, D_corrected])
47	    try:
48	        beta, se = ols_with_se(X, Y)
49	        return float(beta[tau_idx]), float(se[tau_idx]), True
50	    except Exception:
51	        return np.nan, np.nan, False
52	
53	
54	def correct_dsl(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1):
55	    """EM-based joint estimation of regression params and C.
56	
57	    Args:
58	        X_other: (N, p) non-A regressors (includes intercept)
59	        Y: (N,) outcome
60	        Astar: (N,) misclassified labels
61	        A_gold: (N,) gold-standard labels (only gold_mask positions used)
62	        gold_mask: (N,) boolean mask for gold-standard observations
63	        tau_idx: index of target coefficient
64	
65	    Returns:
66	        (tau_hat, se, success) tuple
67	    """
68	    N = len(Y)
69	    K = int(max(Astar.max(), A_gold[gold_mask].max())) + 1
70	    n_other = X_other.shape[1]
71	
72	    C_est = np.zeros((K, K))
73	    for j in range(K):
74	        for k in range(K):
75	            C_est[k, j] = (
76	                (A_gold[gold_mask] == j) & (Astar[gold_mask] == k)
77	            ).sum()
78	    col_sums = C_est.sum(axis=0)
79	    col_sums[col_sums == 0] = 1.0
80	    C_est /= col_sums
81	    C_est = 0.9 * C_est + 0.1 / K * np.ones((K, K))
82	
83	    D_star = make_dummies(Astar, K)
84	    X_init = np.column_stack([X_other, D_star])
85	    try:
86	        beta = ols(X_init, Y)
87	    except Exception:
88	        return np.nan, np.nan, False
89	    sigma2 = 1.0
90	
91	    for _ in range(_EM_MAX_ITER):
92	        base = X_other @ beta[:n_other]
93	        resp = np.zeros((N, K))
94	        for j in range(K):
95	            mu_j = base + (beta[n_other + j - 1] if j > 0 else 0.0)
96	            resp[:, j] = (
97	                -0.5 * (Y - mu_j) ** 2 / sigma2
98	                + np.log(np.clip(C_est[Astar, j], 1e-15, None))
99	            )
100	        resp -= resp.max(axis=1, keepdims=True)
101	        resp = np.exp(resp)
102	        resp /= resp.sum(axis=1, keepdims=True)
103	        resp[gold_mask] = 0.0
104	        resp[gold_mask, A_gold[gold_mask]] = 1.0
105	
106	        D_exp = resp[:, 1:]
107	        X_new = np.column_stack([X_other, D_exp])
108	        try:
109	            beta_new = ols(X_new, Y)
110	        except Exception:
111	            return np.nan, np.nan, False
112	        sigma2_new = max(np.mean((Y - X_new @ beta_new) ** 2), 1e-6)
113	
114	        C_new = np.zeros((K, K))
115	        for j in range(K):
116	            for k in range(K):
117	                C_new[k, j] = resp[Astar == k, j].sum()
118	        cs = C_new.sum(axis=0)
119	        cs[cs == 0] = 1.0
120	        C_new /= cs
121	
122	        converged = (
123	            np.max(np.abs(beta_new - beta)) < _EM_TOL
124	            and np.max(np.abs(C_new - C_est)) < _EM_TOL
125	        )
126	        beta, C_est, sigma2 = beta_new, C_new, sigma2_new
127	        if converged:
128	            break
129	
130	    X_final = np.column_stack([X_other, resp[:, 1:]])
131	    try:
132	        beta_f, se_f = ols_with_se(X_final, Y)
133	        return float(beta_f[tau_idx]), float(se_f[tau_idx]), True
134	    except Exception:
135	        return np.nan, np.nan, False
136	
137	
138	def correct_ppi(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1, rng=None):
139	    """PPI++ with bootstrap lambda tuning.
140	
141	    Args:
142	        X_other: (N, p) non-A regressors (includes intercept)
143	        Y: (N,) outcome
144	        Astar: (N,) misclassified labels
145	        A_gold: (N,) gold-standard labels
146	        gold_mask: (N,) boolean mask for gold-standard observations
147	        tau_idx: index of target coefficient
148	        rng: numpy random Generator
149	
150	    Returns:
151	        (tau_hat, se, success) tuple
152	    """
153	    if rng is None:
154	        rng = np.random.default_rng()
155	    K = int(max(Astar.max(), A_gold[gold_mask].max())) + 1
156	    gold_idx = np.where(gold_mask)[0]
157	    n_gold = len(gold_idx)
158	
159	    D_g_true = make_dummies(A_gold[gold_mask], K)
160	    X_g_true = np.column_stack([X_other[gold_mask], D_g_true])
161	    D_g_star = make_dummies(Astar[gold_mask], K)
162	    X_g_star = np.column_stack([X_other[gold_mask], D_g_star])
163	    D_all_star = make_dummies(Astar, K)
164	    X_all_star = np.column_stack([X_other, D_all_star])
165	
166	    try:
167	        b_g_true = ols(X_g_true, Y[gold_mask])
168	        b_g_star = ols(X_g_star, Y[gold_mask])
169	        b_all_star = ols(X_all_star, Y)
170	    except Exception:
171	        return np.nan, np.nan, False
172	
173	    n_boot = 50
174	    tau_true_boot = np.zeros(n_boot)
175	    tau_rect_boot = np.zeros(n_boot)
176	    for b in range(n_boot):
177	        idx = rng.choice(gold_idx, size=n_gold, replace=True)
178	        try:
179	            bt = ols(
180	                np.column_stack([X_other[idx], make_dummies(A_gold[idx], K)]),
181	                Y[idx],
182	            )
183	            bs = ols(
184	                np.column_stack([X_other[idx], make_dummies(Astar[idx], K)]),
185	                Y[idx],
186	            )
187	            tau_true_boot[b] = bt[tau_idx]
188	            tau_rect_boot[b] = bs[tau_idx] - bt[tau_idx]
189	        except Exception:
190	            tau_true_boot[b] = tau_rect_boot[b] = np.nan
191	
192	    valid = np.isfinite(tau_true_boot) & np.isfinite(tau_rect_boot)
193	    if valid.sum() > 5:
194	        var_r = np.var(tau_rect_boot[valid])
195	        cov_tr = np.cov(tau_true_boot[valid], tau_rect_boot[valid])[0, 1]
196	        lam = np.clip(-cov_tr / var_r, 0, 1) if var_r > 1e-12 else 1.0
197	    else:
198	        lam = 1.0
199	
200	    tau_ppi = b_g_true[tau_idx] + lam * (b_all_star[tau_idx] - b_g_star[tau_idx])
201	    se_est = float(np.std(tau_true_boot[valid])) if valid.sum() > 1 else np.nan
202	    return float(tau_ppi), se_est, True
203	
204	
205	def correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=None):
206	    """MC-SIMEX: add extra misclassification at levels lambda, extrapolate to -1.
207	
208	    Args:
209	        X_other: (N, p) non-A regressors (includes intercept)
210	        Y: (N,) outcome
211	        Astar: (N,) misclassified labels
212	        C: (K, K) confusion matrix
213	        tau_idx: index of target coefficient
214	        rng: numpy random Generator
215	
216	    Returns:
217	        (tau_hat, se, success) tuple
218	    """
219	    if rng is None:
220	        rng = np.random.default_rng()
221	    K = C.shape[0]
222	    try:
223	        eigvals, eigvecs = np.linalg.eig(C)
224	        eigvecs_inv = np.linalg.inv(eigvecs)
225	    except np.linalg.LinAlgError:
226	        return np.nan, np.nan, False
227	
228	    lambdas = np.array([0.0] + _SIMEX_LAMBDAS)
229	    tau_lam = np.zeros(len(lambdas))
230	
231	    for li, lam_val in enumerate(lambdas):
232	        if lam_val == 0.0:
233	            D_star = make_dummies(Astar, K)
234	            X = np.column_stack([X_other, D_star])
235	            try:
236	                tau_lam[li] = ols(X, Y)[tau_idx]
237	            except Exception:
238	                return np.nan, np.nan, False
239	        else:
240	            C_lam_raw = np.real((eigvecs * (eigvals ** lam_val)) @ eigvecs_inv)
241	            C_lam = np.clip(C_lam_raw, 0, None)
242	            cs = C_lam.sum(axis=0)
243	            cs[cs == 0] = 1.0
244	            C_lam /= cs
245	
246	            tau_b = np.zeros(_SIMEX_B)
247	            for b in range(_SIMEX_B):
248	                rng_b = np.random.default_rng(
249	                    rng.integers(0, 2 ** 31) + b * 1000 + li * 100000
250	                )
251	                A_extra = misclassify(Astar, C_lam, rng_b)
252	                D_extra = make_dummies(A_extra, K)
253	                X_extra = np.column_stack([X_other, D_extra])
254	                try:
255	                    tau_b[b] = ols(X_extra, Y)[tau_idx]
256	                except Exception:
257	                    tau_b[b] = np.nan
258	            ok = np.isfinite(tau_b)
259	            if ok.sum() < _SIMEX_B // 2:
260	                return np.nan, np.nan, False
261	            tau_lam[li] = tau_b[ok].mean()
262	
263	    try:
264	        coeffs = np.polyfit(lambdas, tau_lam, 2)
265	        tau_simex = float(np.polyval(coeffs, -1.0))
266	    except Exception:
267	        return np.nan, np.nan, False
268	
269	    D_star = make_dummies(Astar, K)
270	    X = np.column_stack([X_other, D_star])
271	    try:
272	        _, se = ols_with_se(X, Y)
273	        return tau_simex, float(se[tau_idx]), True
274	    except Exception:
275	        return tau_simex, np.nan, True
276	
277	
278	def correct_mla(X_other, Y, Astar, C, tau_idx=1):
279	    """MLA: D_corrected = D*_full @ C^{-1}, drop reference category.
280	
281	    Args:
282	        X_other: (N, p) non-A regressors (includes intercept)
283	        Y: (N,) outcome
284	        Astar: (N,) misclassified labels
285	        C: (K, K) confusion matrix
286	        tau_idx: index of target coefficient
287	
288	    Returns:
289	        (tau_hat, se, success) tuple
290	    """
291	    cond = np.linalg.cond(C)
292	    if cond > 1e12:
293	        return np.nan, np.nan, False
294	    try:
295	        C_inv = np.linalg.inv(C)
296	    except np.linalg.LinAlgError:
297	        return np.nan, np.nan, False
298	    K = C.shape[0]
299	    D_full = make_full_dummies(Astar, K)
300	    D_corrected = (D_full @ C_inv)[:, 1:]
301	    X = np.column_stack([X_other, D_corrected])
302	    try:
303	        beta, se = ols_with_se(X, Y)
304	        return float(beta[tau_idx]), float(se[tau_idx]), True
305	    except Exception:
306	        return np.nan, np.nan, False
307	
308	
309	def recommend_correction(topology, C, has_gold=False, gold_fraction=0.1):
310	    """Recommend the best correction method based on topology and data availability.
311	
312	    Rules (from plan_007 conclusions):
313	      - has_gold=True  -> PPI++ (93.8% bias reduction, 96.8% coverage)
314	      - has_gold=False + confounding/mediation -> DSL
315	      - has_gold=False + other topologies -> MC-SIMEX
316	      - naive_plugin/MLA: only correct dummy coefficients (FWL theorem)
317	
318	    Args:
319	        topology: one of 7 DAG types
320	        C: (K, K) confusion matrix (used for diagnostics)
321	        has_gold: whether gold-standard labels are available
322	        gold_fraction: fraction of data with gold labels
323	
324	    Returns:
325	        dict with recommended, ranking, notes
326	    """
327	    dsl_safe = topology in ("confounding", "mediation")
328	
329	    if has_gold:
330	        recommended = "ppi"
331	    elif dsl_safe:
332	        recommended = "dsl"
333	    else:
334	        recommended = "mcsimex"
335	
336	    ranking = []
337	
338	    # PPI++
339	    if has_gold:
340	        ranking.append({
341	            "method": "ppi",
342	            "applicable": True,
343	            "expected_bias_reduction": 0.938,
344	            "notes": "Best with gold labels (93.8% bias reduction, 96.8% coverage)",
345	        })
346	    else:
347	        ranking.append({
348	            "method": "ppi",
349	            "applicable": False,
350	            "expected_bias_reduction": 0.0,
351	            "notes": "Requires gold-standard labels",
352	        })
353	
354	    # DSL
355	    if dsl_safe:
356	        ranking.append({
357	            "method": "dsl",
358	            "applicable": True,
359	            "expected_bias_reduction": 0.75,
360	            "notes": "Good for confounding/mediation"
361	                     + (" (best with gold for initialization)" if not has_gold else ""),
362	        })
363	    else:
364	        ranking.append({
365	            "method": "dsl",
366	            "applicable": False,
367	            "expected_bias_reduction": -5.0,
368	            "notes": f"Catastrophic for {topology} (e.g., mbias yields -768%)",
369	        })
370	
371	    # MC-SIMEX
372	    ranking.append({
373	        "method": "mcsimex",
374	        "applicable": True,
375	        "expected_bias_reduction": 0.209,
376	        "notes": "Moderate (20.9%) but broadly applicable; requires known C",
377	    })
378	
379	    # Naive Plugin
380	    ranking.append({
381	        "method": "naive_plugin",
382	        "applicable": True,
383	        "expected_bias_reduction": 0.0,
384	        "notes": "Only corrects dummy coefficients, NOT treatment coefficient (FWL theorem)",
385	    })
386	
387	    # MLA
388	    ranking.append({
389	        "method": "mla",
390	        "applicable": True,
391	        "expected_bias_reduction": 0.0,
392	        "notes": "Only corrects dummy coefficients, NOT treatment coefficient (FWL theorem)",
393	    })
394	
395	    ranking.sort(key=lambda m: -m["expected_bias_reduction"])
396	
397	    notes = []
398	    if has_gold:
399	        notes.append(f"Gold labels available ({gold_fraction:.0%} of data)")
400	        notes.append("PPI++ recommended: highest bias reduction with valid coverage")
401	    else:
402	        notes.append("No gold labels available")
403	        if dsl_safe:
404	            notes.append(f"DSL recommended for {topology} (EM-based, works with known C)")
405	        else:
406	            notes.append(
407	                f"MC-SIMEX recommended; DSL is catastrophic for {topology}"
408	            )
409	
410	    cond = np.linalg.cond(C)
411	    if cond > 100:
412	        notes.append(
413	            f"WARNING: C condition number = {cond:.0f}, "
414	            f"inverse-based methods may be unstable"
415	        )
416	
417	    return {
418	        "recommended": recommended,
419	        "ranking": ranking,
420	        "notes": notes,
421	    }
422	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "da0cb6f5-3446-4fcf-9579-fed543297c55",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/correction.py",
      "content": "\"\"\"Correction methods and recommendation engine for annotation-error bias.\n\nFive correction methods:\n  - naive_plugin: C^{-1} correction of dummy indicators\n  - dsl: EM-based joint estimation of regression params and C\n  - ppi: PPI++ combining gold-standard and full-sample estimates\n  - mcsimex: MC-SIMEX extrapolation to lambda=-1\n  - mla: Matrix-based label adjustment via D*_full @ C^{-1}\n\nKey finding (FWL theorem): naive_plugin and mla correct dummy coefficients\nbut NOT the treatment coefficient in regressions with a separate treatment T.\n\"\"\"\n\nimport numpy as np\nfrom .utils import ols, ols_with_se, make_dummies, make_full_dummies, misclassify\n\nMETHODS = [\"naive_plugin\", \"dsl\", \"ppi\", \"mcsimex\", \"mla\"]\n\n_EM_MAX_ITER = 100\n_EM_TOL = 1e-6\n_SIMEX_LAMBDAS = [0.5, 1.0, 1.5, 2.0]\n_SIMEX_B = 50\n\n\ndef correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1):\n    \"\"\"Correct using C^{-1} applied per-observation to dummy indicators.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        C: (K, K) confusion matrix\n        tau_idx: index of target coefficient in full design\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    cond = np.linalg.cond(C)\n    if cond > 1e12:\n        return np.nan, np.nan, False\n    try:\n        C_inv = np.linalg.inv(C)\n    except np.linalg.LinAlgError:\n        return np.nan, np.nan, False\n    D_corrected = C_inv[:, Astar].T[:, 1:]\n    X = np.column_stack([X_other, D_corrected])\n    try:\n        beta, se = ols_with_se(X, Y)\n        return float(beta[tau_idx]), float(se[tau_idx]), True\n    except Exception:\n        return np.nan, np.nan, False\n\n\ndef correct_dsl(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1):\n    \"\"\"EM-based joint estimation of regression params and C.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        A_gold: (N,) gold-standard labels (only gold_mask positions used)\n        gold_mask: (N,) boolean mask for gold-standard observations\n        tau_idx: index of target coefficient\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    N = len(Y)\n    K = int(max(Astar.max(), A_gold[gold_mask].max())) + 1\n    n_other = X_other.shape[1]\n\n    C_est = np.zeros((K, K))\n    for j in range(K):\n        for k in range(K):\n            C_est[k, j] = (\n                (A_gold[gold_mask] == j) & (Astar[gold_mask] == k)\n            ).sum()\n    col_sums = C_est.sum(axis=0)\n    col_sums[col_sums == 0] = 1.0\n    C_est /= col_sums\n    C_est = 0.9 * C_est + 0.1 / K * np.ones((K, K))\n\n    D_star = make_dummies(Astar, K)\n    X_init = np.column_stack([X_other, D_star])\n    try:\n        beta = ols(X_init, Y)\n    except Exception:\n        return np.nan, np.nan, False\n    sigma2 = 1.0\n\n    for _ in range(_EM_MAX_ITER):\n        base = X_other @ beta[:n_other]\n        resp = np.zeros((N, K))\n        for j in range(K):\n            mu_j = base + (beta[n_other + j - 1] if j > 0 else 0.0)\n            resp[:, j] = (\n                -0.5 * (Y - mu_j) ** 2 / sigma2\n                + np.log(np.clip(C_est[Astar, j], 1e-15, None))\n            )\n        resp -= resp.max(axis=1, keepdims=True)\n        resp = np.exp(resp)\n        resp /= resp.sum(axis=1, keepdims=True)\n        resp[gold_mask] = 0.0\n        resp[gold_mask, A_gold[gold_mask]] = 1.0\n\n        D_exp = resp[:, 1:]\n        X_new = np.column_stack([X_other, D_exp])\n        try:\n            beta_new = ols(X_new, Y)\n        except Exception:\n            return np.nan, np.nan, False\n        sigma2_new = max(np.mean((Y - X_new @ beta_new) ** 2), 1e-6)\n\n        C_new = np.zeros((K, K))\n        for j in range(K):\n            for k in range(K):\n                C_new[k, j] = resp[Astar == k, j].sum()\n        cs = C_new.sum(axis=0)\n        cs[cs == 0] = 1.0\n        C_new /= cs\n\n        converged = (\n            np.max(np.abs(beta_new - beta)) < _EM_TOL\n            and np.max(np.abs(C_new - C_est)) < _EM_TOL\n        )\n        beta, C_est, sigma2 = beta_new, C_new, sigma2_new\n        if converged:\n            break\n\n    X_final = np.column_stack([X_other, resp[:, 1:]])\n    try:\n        beta_f, se_f = ols_with_se(X_final, Y)\n        return float(beta_f[tau_idx]), float(se_f[tau_idx]), True\n    except Exception:\n        return np.nan, np.nan, False\n\n\ndef correct_ppi(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1, rng=None):\n    \"\"\"PPI++ with bootstrap lambda tuning.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        A_gold: (N,) gold-standard labels\n        gold_mask: (N,) boolean mask for gold-standard observations\n        tau_idx: index of target coefficient\n        rng: numpy random Generator\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    if rng is None:\n        rng = np.random.default_rng()\n    K = int(max(Astar.max(), A_gold[gold_mask].max())) + 1\n    gold_idx = np.where(gold_mask)[0]\n    n_gold = len(gold_idx)\n\n    D_g_true = make_dummies(A_gold[gold_mask], K)\n    X_g_true = np.column_stack([X_other[gold_mask], D_g_true])\n    D_g_star = make_dummies(Astar[gold_mask], K)\n    X_g_star = np.column_stack([X_other[gold_mask], D_g_star])\n    D_all_star = make_dummies(Astar, K)\n    X_all_star = np.column_stack([X_other, D_all_star])\n\n    try:\n        b_g_true = ols(X_g_true, Y[gold_mask])\n        b_g_star = ols(X_g_star, Y[gold_mask])\n        b_all_star = ols(X_all_star, Y)\n    except Exception:\n        return np.nan, np.nan, False\n\n    n_boot = 50\n    tau_true_boot = np.zeros(n_boot)\n    tau_rect_boot = np.zeros(n_boot)\n    for b in range(n_boot):\n        idx = rng.choice(gold_idx, size=n_gold, replace=True)\n        try:\n            bt = ols(\n                np.column_stack([X_other[idx], make_dummies(A_gold[idx], K)]),\n                Y[idx],\n            )\n            bs = ols(\n                np.column_stack([X_other[idx], make_dummies(Astar[idx], K)]),\n                Y[idx],\n            )\n            tau_true_boot[b] = bt[tau_idx]\n            tau_rect_boot[b] = bs[tau_idx] - bt[tau_idx]\n        except Exception:\n            tau_true_boot[b] = tau_rect_boot[b] = np.nan\n\n    valid = np.isfinite(tau_true_boot) & np.isfinite(tau_rect_boot)\n    if valid.sum() > 5:\n        var_r = np.var(tau_rect_boot[valid])\n        cov_tr = np.cov(tau_true_boot[valid], tau_rect_boot[valid])[0, 1]\n        lam = np.clip(-cov_tr / var_r, 0, 1) if var_r > 1e-12 else 1.0\n    else:\n        lam = 1.0\n\n    tau_ppi = b_g_true[tau_idx] + lam * (b_all_star[tau_idx] - b_g_star[tau_idx])\n    se_est = float(np.std(tau_true_boot[valid])) if valid.sum() > 1 else np.nan\n    return float(tau_ppi), se_est, True\n\n\ndef correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=None):\n    \"\"\"MC-SIMEX: add extra misclassification at levels lambda, extrapolate to -1.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        C: (K, K) confusion matrix\n        tau_idx: index of target coefficient\n        rng: numpy random Generator\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    if rng is None:\n        rng = np.random.default_rng()\n    K = C.shape[0]\n    try:\n        eigvals, eigvecs = np.linalg.eig(C)\n        eigvecs_inv = np.linalg.inv(eigvecs)\n    except np.linalg.LinAlgError:\n        return np.nan, np.nan, False\n\n    lambdas = np.array([0.0] + _SIMEX_LAMBDAS)\n    tau_lam = np.zeros(len(lambdas))\n\n    for li, lam_val in enumerate(lambdas):\n        if lam_val == 0.0:\n            D_star = make_dummies(Astar, K)\n            X = np.column_stack([X_other, D_star])\n            try:\n                tau_lam[li] = ols(X, Y)[tau_idx]\n            except Exception:\n                return np.nan, np.nan, False\n        else:\n            C_lam_raw = np.real((eigvecs * (eigvals ** lam_val)) @ eigvecs_inv)\n            C_lam = np.clip(C_lam_raw, 0, None)\n            cs = C_lam.sum(axis=0)\n            cs[cs == 0] = 1.0\n            C_lam /= cs\n\n            tau_b = np.zeros(_SIMEX_B)\n            for b in range(_SIMEX_B):\n                rng_b = np.random.default_rng(\n                    rng.integers(0, 2 ** 31) + b * 1000 + li * 100000\n                )\n                A_extra = misclassify(Astar, C_lam, rng_b)\n                D_extra = make_dummies(A_extra, K)\n                X_extra = np.column_stack([X_other, D_extra])\n                try:\n                    tau_b[b] = ols(X_extra, Y)[tau_idx]\n                except Exception:\n                    tau_b[b] = np.nan\n            ok = np.isfinite(tau_b)\n            if ok.sum() < _SIMEX_B // 2:\n                return np.nan, np.nan, False\n            tau_lam[li] = tau_b[ok].mean()\n\n    try:\n        coeffs = np.polyfit(lambdas, tau_lam, 2)\n        tau_simex = float(np.polyval(coeffs, -1.0))\n    except Exception:\n        return np.nan, np.nan, False\n\n    D_star = make_dummies(Astar, K)\n    X = np.column_stack([X_other, D_star])\n    try:\n        _, se = ols_with_se(X, Y)\n        return tau_simex, float(se[tau_idx]), True\n    except Exception:\n        return tau_simex, np.nan, True\n\n\ndef correct_mla(X_other, Y, Astar, C, tau_idx=1):\n    \"\"\"MLA: D_corrected = D*_full @ C^{-1}, drop reference category.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        C: (K, K) confusion matrix\n        tau_idx: index of target coefficient\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    cond = np.linalg.cond(C)\n    if cond > 1e12:\n        return np.nan, np.nan, False\n    try:\n        C_inv = np.linalg.inv(C)\n    except np.linalg.LinAlgError:\n        return np.nan, np.nan, False\n    K = C.shape[0]\n    D_full = make_full_dummies(Astar, K)\n    D_corrected = (D_full @ C_inv)[:, 1:]\n    X = np.column_stack([X_other, D_corrected])\n    try:\n        beta, se = ols_with_se(X, Y)\n        return float(beta[tau_idx]), float(se[tau_idx]), True\n    except Exception:\n        return np.nan, np.nan, False\n\n\ndef recommend_correction(topology, C, has_gold=False, gold_fraction=0.1):\n    \"\"\"Recommend the best correction method based on topology and data availability.\n\n    Rules (from plan_007 conclusions):\n      - has_gold=True  -> PPI++ (93.8% bias reduction, 96.8% coverage)\n      - has_gold=False + confounding/mediation -> DSL\n      - has_gold=False + other topologies -> MC-SIMEX\n      - naive_plugin/MLA: only correct dummy coefficients (FWL theorem)\n\n    Args:\n        topology: one of 7 DAG types\n        C: (K, K) confusion matrix (used for diagnostics)\n        has_gold: whether gold-standard labels are available\n        gold_fraction: fraction of data with gold labels\n\n    Returns:\n        dict with recommended, ranking, notes\n    \"\"\"\n    dsl_safe = topology in (\"confounding\", \"mediation\")\n\n    if has_gold:\n        recommended = \"ppi\"\n    elif dsl_safe:\n        recommended = \"dsl\"\n    else:\n        recommended = \"mcsimex\"\n\n    ranking = []\n\n    # PPI++\n    if has_gold:\n        ranking.append({\n            \"method\": \"ppi\",\n            \"applicable\": True,\n            \"expected_bias_reduction\": 0.938,\n            \"notes\": \"Best with gold labels (93.8% bias reduction, 96.8% coverage)\",\n        })\n    else:\n        ranking.append({\n            \"method\": \"ppi\",\n            \"applicable\": False,\n            \"expected_bias_reduction\": 0.0,\n            \"notes\": \"Requires gold-standard labels\",\n        })\n\n    # DSL\n    if dsl_safe:\n        ranking.append({\n            \"method\": \"dsl\",\n            \"applicable\": True,\n            \"expected_bias_reduction\": 0.75,\n            \"notes\": \"Good for confounding/mediation\"\n                     + (\" (best with gold for initialization)\" if not has_gold else \"\"),\n        })\n    else:\n        ranking.append({\n            \"method\": \"dsl\",\n            \"applicable\": False,\n            \"expected_bias_reduction\": -5.0,\n            \"notes\": f\"Catastrophic for {topology} (e.g., mbias yields -768%)\",\n        })\n\n    # MC-SIMEX\n    ranking.append({\n        \"method\": \"mcsimex\",\n        \"applicable\": True,\n        \"expected_bias_reduction\": 0.209,\n        \"notes\": \"Moderate (20.9%) but broadly applicable; requires known C\",\n    })\n\n    # Naive Plugin\n    ranking.append({\n        \"method\": \"naive_plugin\",\n        \"applicable\": True,\n        \"expected_bias_reduction\": 0.0,\n        \"notes\": \"Only corrects dummy coefficients, NOT treatment coefficient (FWL theorem)\",\n    })\n\n    # MLA\n    ranking.append({\n        \"method\": \"mla\",\n        \"applicable\": True,\n        \"expected_bias_reduction\": 0.0,\n        \"notes\": \"Only corrects dummy coefficients, NOT treatment coefficient (FWL theorem)\",\n    })\n\n    ranking.sort(key=lambda m: -m[\"expected_bias_reduction\"])\n\n    notes = []\n    if has_gold:\n        notes.append(f\"Gold labels available ({gold_fraction:.0%} of data)\")\n        notes.append(\"PPI++ recommended: highest bias reduction with valid coverage\")\n    else:\n        notes.append(\"No gold labels available\")\n        if dsl_safe:\n            notes.append(f\"DSL recommended for {topology} (EM-based, works with known C)\")\n        else:\n            notes.append(\n                f\"MC-SIMEX recommended; DSL is catastrophic for {topology}\"\n            )\n\n    cond = np.linalg.cond(C)\n    if cond > 100:\n        notes.append(\n            f\"WARNING: C condition number = {cond:.0f}, \"\n            f\"inverse-based methods may be unstable\"\n        )\n\n    return {\n        \"recommended\": recommended,\n        \"ranking\": ranking,\n        \"notes\": notes,\n    }\n",
      "numLines": 422,
      "startLine": 1,
      "totalLines": 422
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01EkUggzFUUjDfr7ZpvSjGE8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/test_core.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "b8ead37e-ef7b-429f-afea-df0adc53e3c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQbEmFPpg3WkXvGvZH8S1P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21029,
      "cache_read_input_tokens": 26851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21029
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

_source line 21 · 2026-05-20T23:51:14.555Z_

<details><summary>↩ Tool result · `toolu_01EkUggzFUUjDfr7ZpvSjGE8`</summary>

```text
1	"""Core tests for the annot_sensitivity package."""
2	
3	import numpy as np
4	import pytest
5	from annot_sensitivity import (
6	    compute_bias,
7	    compute_asv,
8	    recommend_correction,
9	    validate_confusion_matrix,
10	    interpolate_confusion,
11	    random_confusion_matrix,
12	    predefined_matrices,
13	    generate_data,
14	    TOPOLOGIES,
15	)
16	
17	
18	class TestValidateConfusionMatrix:
19	    def test_identity_valid(self):
20	        assert validate_confusion_matrix(np.eye(3)) is True
21	
22	    def test_predefined_valid(self):
23	        for name, C in predefined_matrices().items():
24	            assert validate_confusion_matrix(C) is True, f"{name} failed"
25	
26	    def test_non_square(self):
27	        assert validate_confusion_matrix(np.ones((2, 3))) is False
28	
29	    def test_negative_entries(self):
30	        C = np.array([[1.1, -0.1], [-0.1, 1.1]])
31	        assert validate_confusion_matrix(C) is False
32	
33	    def test_not_column_stochastic(self):
34	        C = np.array([[0.5, 0.5], [0.3, 0.3]])
35	        assert validate_confusion_matrix(C) is False
36	
37	    def test_not_array(self):
38	        assert validate_confusion_matrix([[1, 0], [0, 1]]) is False
39	
40	    def test_1x1(self):
41	        assert validate_confusion_matrix(np.array([[1.0]])) is False
42	
43	    def test_random_valid(self):
44	        C = random_confusion_matrix(4, diag_dominance=0.7, rng=np.random.default_rng(42))
45	        assert validate_confusion_matrix(C) is True
46	        assert C.shape == (4, 4)
47	
48	
49	class TestInterpolateConfusion:
50	    def test_delta_zero_is_identity(self):
51	        C0 = predefined_matrices()["symmetric_high"]
52	        C = interpolate_confusion(C0, 0.0)
53	        np.testing.assert_allclose(C, np.eye(3), atol=1e-12)
54	
55	    def test_delta_one_is_C0(self):
56	        C0 = predefined_matrices()["symmetric_high"]
57	        C = interpolate_confusion(C0, 1.0)
58	        np.testing.assert_allclose(C, C0, atol=1e-12)
59	
60	    def test_intermediate_column_stochastic(self):
61	        C0 = predefined_matrices()["asymmetric"]
62	        C = interpolate_confusion(C0, 0.5)
63	        assert validate_confusion_matrix(C)
64	
65	    def test_small_delta(self):
66	        C0 = predefined_matrices()["severe_uniform"]
67	        C = interpolate_confusion(C0, 0.01)
68	        assert np.allclose(np.diag(C), np.ones(3) * (1 - 0.01) + 0.01 * np.diag(C0),
69	                           atol=1e-6)
70	
71	
72	class TestComputeBias:
73	    def test_identity_zero_bias(self):
74	        result = compute_bias("confounding", np.eye(3))
75	        assert abs(result["bias"]) < 1e-3
76	        assert abs(result["bias_pct"]) < 0.1
77	
78	    def test_confounding_nonzero_bias(self):
79	        C = predefined_matrices()["symmetric_high"]
80	        result = compute_bias("confounding", C)
81	        assert abs(result["bias"]) > 0.01
82	        assert result["topology"] == "confounding"
83	        assert np.isfinite(result["tau_true"])
84	        assert np.isfinite(result["tau_biased"])
85	
86	    def test_all_topologies_run(self):
87	        C = predefined_matrices()["mild_uniform"]
88	        for topo in TOPOLOGIES:
89	            result = compute_bias(topo, C)
90	            assert result["topology"] == topo
91	            assert np.isfinite(result["tau_true"])
92	            assert np.isfinite(result["tau_biased"])
93	
94	    def test_invalid_topology(self):
95	        with pytest.raises(ValueError, match="Unknown topology"):
96	            compute_bias("nonexistent", np.eye(3))
97	
98	    def test_invalid_C(self):
99	        with pytest.raises(ValueError, match="column-stochastic"):
100	            compute_bias("confounding", np.ones((3, 3)))
101	
102	    def test_worse_C_more_bias(self):
103	        C_mild = predefined_matrices()["mild_uniform"]
104	        C_severe = predefined_matrices()["severe_uniform"]
105	        r_mild = compute_bias("confounding", C_mild)
106	        r_severe = compute_bias("confounding", C_severe)
107	        assert abs(r_severe["bias"]) > abs(r_mild["bias"])
108	
109	
110	class TestComputeASV:
111	    def test_returns_valid_structure(self):
112	        C0 = predefined_matrices()["symmetric_high"]
113	        result = compute_asv("confounding", C0, n_grid=200)
114	        assert "asv" in result
115	        assert "bias_curve" in result
116	        assert "envelope" in result
117	        assert "deltas" in result
118	        assert "tau_true" in result
119	        assert len(result["deltas"]) == 200
120	        assert len(result["bias_curve"]) == 200
121	        assert len(result["envelope"]) == 200
122	
123	    def test_asv_is_positive_or_none(self):
124	        C0 = predefined_matrices()["symmetric_high"]
125	        result = compute_asv("confounding", C0, threshold_type="magnitude",
126	                             threshold_value=0.1, n_grid=200)
127	        if result["asv"] is not None:
128	            assert result["asv"] > 0
129	
130	    def test_envelope_monotone(self):
131	        C0 = predefined_matrices()["asymmetric"]
132	        result = compute_asv("mediation", C0, n_grid=200)
133	        diffs = np.diff(result["envelope"])
134	        assert np.all(diffs >= -1e-12)
135	
136	    def test_sign_flip_threshold(self):
137	        C0 = predefined_matrices()["symmetric_high"]
138	        result = compute_asv("confounding", C0, threshold_type="sign_flip",
139	                             n_grid=200)
140	        assert "asv" in result
141	
142	    def test_invalid_threshold_type(self):
143	        C0 = predefined_matrices()["symmetric_high"]
144	        with pytest.raises(ValueError, match="Unknown threshold_type"):
145	            compute_asv("confounding", C0, threshold_type="invalid", n_grid=50)
146	
147	
148	class TestRecommendCorrection:
149	    def test_with_gold_recommends_ppi(self):
150	        C = predefined_matrices()["symmetric_high"]
151	        result = recommend_correction("confounding", C, has_gold=True)
152	        assert result["recommended"] == "ppi"
153	
154	    def test_without_gold_confounding_recommends_dsl(self):
155	        C = predefined_matrices()["symmetric_high"]
156	        result = recommend_correction("confounding", C, has_gold=False)
157	        assert result["recommended"] == "dsl"
158	
159	    def test_without_gold_mediation_recommends_dsl(self):
160	        C = predefined_matrices()["symmetric_high"]
161	        result = recommend_correction("mediation", C, has_gold=False)
162	        assert result["recommended"] == "dsl"
163	
164	    def test_without_gold_collider_recommends_mcsimex(self):
165	        C = predefined_matrices()["symmetric_high"]
166	        result = recommend_correction("collider", C, has_gold=False)
167	        assert result["recommended"] == "mcsimex"
168	
169	    def test_without_gold_mbias_recommends_mcsimex(self):
170	        C = predefined_matrices()["symmetric_high"]
171	        result = recommend_correction("mbias", C, has_gold=False)
172	        assert result["recommended"] == "mcsimex"
173	
174	    def test_ranking_has_all_methods(self):
175	        C = predefined_matrices()["symmetric_high"]
176	        result = recommend_correction("confounding", C, has_gold=True)
177	        methods = {m["method"] for m in result["ranking"]}
178	        assert methods == {"ppi", "dsl", "mcsimex", "naive_plugin", "mla"}
179	
180	    def test_notes_nonempty(self):
181	        C = predefined_matrices()["symmetric_high"]
182	        result = recommend_correction("collider", C, has_gold=False)
183	        assert len(result["notes"]) > 0
184	
185	
186	class TestDGP:
187	    def test_generate_all_topologies(self):
188	        for topo in TOPOLOGIES:
189	            data = generate_data(topo, 100, seed=42)
190	            assert "Y" in data
191	            assert "A" in data
192	            assert len(data["Y"]) == 100
193	
194	    def test_confounding_has_treatment(self):
195	        data = generate_data("confounding", 100, seed=42)
196	        assert "T" in data
197	
198	    def test_exposure_no_treatment(self):
199	        data = generate_data("exposure", 100, seed=42)
200	        assert "T" not in data
201	
202	    def test_iv_has_instrument(self):
203	        data = generate_data("iv", 100, seed=42)
204	        assert "Z" in data
205	
206	    def test_invalid_topology(self):
207	        with pytest.raises(ValueError):
208	            generate_data("invalid", 100)
209	
210	
211	if __name__ == "__main__":
212	    pytest.main([__file__, "-v"])
213	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "3bad90d5-cfcd-4082-929e-74afa1298e51",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/test_core.py",
      "content": "\"\"\"Core tests for the annot_sensitivity package.\"\"\"\n\nimport numpy as np\nimport pytest\nfrom annot_sensitivity import (\n    compute_bias,\n    compute_asv,\n    recommend_correction,\n    validate_confusion_matrix,\n    interpolate_confusion,\n    random_confusion_matrix,\n    predefined_matrices,\n    generate_data,\n    TOPOLOGIES,\n)\n\n\nclass TestValidateConfusionMatrix:\n    def test_identity_valid(self):\n        assert validate_confusion_matrix(np.eye(3)) is True\n\n    def test_predefined_valid(self):\n        for name, C in predefined_matrices().items():\n            assert validate_confusion_matrix(C) is True, f\"{name} failed\"\n\n    def test_non_square(self):\n        assert validate_confusion_matrix(np.ones((2, 3))) is False\n\n    def test_negative_entries(self):\n        C = np.array([[1.1, -0.1], [-0.1, 1.1]])\n        assert validate_confusion_matrix(C) is False\n\n    def test_not_column_stochastic(self):\n        C = np.array([[0.5, 0.5], [0.3, 0.3]])\n        assert validate_confusion_matrix(C) is False\n\n    def test_not_array(self):\n        assert validate_confusion_matrix([[1, 0], [0, 1]]) is False\n\n    def test_1x1(self):\n        assert validate_confusion_matrix(np.array([[1.0]])) is False\n\n    def test_random_valid(self):\n        C = random_confusion_matrix(4, diag_dominance=0.7, rng=np.random.default_rng(42))\n        assert validate_confusion_matrix(C) is True\n        assert C.shape == (4, 4)\n\n\nclass TestInterpolateConfusion:\n    def test_delta_zero_is_identity(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        C = interpolate_confusion(C0, 0.0)\n        np.testing.assert_allclose(C, np.eye(3), atol=1e-12)\n\n    def test_delta_one_is_C0(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        C = interpolate_confusion(C0, 1.0)\n        np.testing.assert_allclose(C, C0, atol=1e-12)\n\n    def test_intermediate_column_stochastic(self):\n        C0 = predefined_matrices()[\"asymmetric\"]\n        C = interpolate_confusion(C0, 0.5)\n        assert validate_confusion_matrix(C)\n\n    def test_small_delta(self):\n        C0 = predefined_matrices()[\"severe_uniform\"]\n        C = interpolate_confusion(C0, 0.01)\n        assert np.allclose(np.diag(C), np.ones(3) * (1 - 0.01) + 0.01 * np.diag(C0),\n                           atol=1e-6)\n\n\nclass TestComputeBias:\n    def test_identity_zero_bias(self):\n        result = compute_bias(\"confounding\", np.eye(3))\n        assert abs(result[\"bias\"]) < 1e-3\n        assert abs(result[\"bias_pct\"]) < 0.1\n\n    def test_confounding_nonzero_bias(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = compute_bias(\"confounding\", C)\n        assert abs(result[\"bias\"]) > 0.01\n        assert result[\"topology\"] == \"confounding\"\n        assert np.isfinite(result[\"tau_true\"])\n        assert np.isfinite(result[\"tau_biased\"])\n\n    def test_all_topologies_run(self):\n        C = predefined_matrices()[\"mild_uniform\"]\n        for topo in TOPOLOGIES:\n            result = compute_bias(topo, C)\n            assert result[\"topology\"] == topo\n            assert np.isfinite(result[\"tau_true\"])\n            assert np.isfinite(result[\"tau_biased\"])\n\n    def test_invalid_topology(self):\n        with pytest.raises(ValueError, match=\"Unknown topology\"):\n            compute_bias(\"nonexistent\", np.eye(3))\n\n    def test_invalid_C(self):\n        with pytest.raises(ValueError, match=\"column-stochastic\"):\n            compute_bias(\"confounding\", np.ones((3, 3)))\n\n    def test_worse_C_more_bias(self):\n        C_mild = predefined_matrices()[\"mild_uniform\"]\n        C_severe = predefined_matrices()[\"severe_uniform\"]\n        r_mild = compute_bias(\"confounding\", C_mild)\n        r_severe = compute_bias(\"confounding\", C_severe)\n        assert abs(r_severe[\"bias\"]) > abs(r_mild[\"bias\"])\n\n\nclass TestComputeASV:\n    def test_returns_valid_structure(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        result = compute_asv(\"confounding\", C0, n_grid=200)\n        assert \"asv\" in result\n        assert \"bias_curve\" in result\n        assert \"envelope\" in result\n        assert \"deltas\" in result\n        assert \"tau_true\" in result\n        assert len(result[\"deltas\"]) == 200\n        assert len(result[\"bias_curve\"]) == 200\n        assert len(result[\"envelope\"]) == 200\n\n    def test_asv_is_positive_or_none(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        result = compute_asv(\"confounding\", C0, threshold_type=\"magnitude\",\n                             threshold_value=0.1, n_grid=200)\n        if result[\"asv\"] is not None:\n            assert result[\"asv\"] > 0\n\n    def test_envelope_monotone(self):\n        C0 = predefined_matrices()[\"asymmetric\"]\n        result = compute_asv(\"mediation\", C0, n_grid=200)\n        diffs = np.diff(result[\"envelope\"])\n        assert np.all(diffs >= -1e-12)\n\n    def test_sign_flip_threshold(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        result = compute_asv(\"confounding\", C0, threshold_type=\"sign_flip\",\n                             n_grid=200)\n        assert \"asv\" in result\n\n    def test_invalid_threshold_type(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        with pytest.raises(ValueError, match=\"Unknown threshold_type\"):\n            compute_asv(\"confounding\", C0, threshold_type=\"invalid\", n_grid=50)\n\n\nclass TestRecommendCorrection:\n    def test_with_gold_recommends_ppi(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"confounding\", C, has_gold=True)\n        assert result[\"recommended\"] == \"ppi\"\n\n    def test_without_gold_confounding_recommends_dsl(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"confounding\", C, has_gold=False)\n        assert result[\"recommended\"] == \"dsl\"\n\n    def test_without_gold_mediation_recommends_dsl(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"mediation\", C, has_gold=False)\n        assert result[\"recommended\"] == \"dsl\"\n\n    def test_without_gold_collider_recommends_mcsimex(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"collider\", C, has_gold=False)\n        assert result[\"recommended\"] == \"mcsimex\"\n\n    def test_without_gold_mbias_recommends_mcsimex(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"mbias\", C, has_gold=False)\n        assert result[\"recommended\"] == \"mcsimex\"\n\n    def test_ranking_has_all_methods(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"confounding\", C, has_gold=True)\n        methods = {m[\"method\"] for m in result[\"ranking\"]}\n        assert methods == {\"ppi\", \"dsl\", \"mcsimex\", \"naive_plugin\", \"mla\"}\n\n    def test_notes_nonempty(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"collider\", C, has_gold=False)\n        assert len(result[\"notes\"]) > 0\n\n\nclass TestDGP:\n    def test_generate_all_topologies(self):\n        for topo in TOPOLOGIES:\n            data = generate_data(topo, 100, seed=42)\n            assert \"Y\" in data\n            assert \"A\" in data\n            assert len(data[\"Y\"]) == 100\n\n    def test_confounding_has_treatment(self):\n        data = generate_data(\"confounding\", 100, seed=42)\n        assert \"T\" in data\n\n    def test_exposure_no_treatment(self):\n        data = generate_data(\"exposure\", 100, seed=42)\n        assert \"T\" not in data\n\n    def test_iv_has_instrument(self):\n        data = generate_data(\"iv\", 100, seed=42)\n        assert \"Z\" in data\n\n    def test_invalid_topology(self):\n        with pytest.raises(ValueError):\n            generate_data(\"invalid\", 100)\n\n\nif __name__ == \"__main__\":\n    pytest.main([__file__, \"-v\"])\n",
      "numLines": 213,
      "startLine": 1,
      "totalLines": 213
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01Aaq9aY8NWMSQFBXpRGouyt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/confusion.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "96100bab-f8bf-4cb4-8f62-b34a8518a869",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQbEmFPpg3WkXvGvZH8S1P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21029,
      "cache_read_input_tokens": 26851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21029
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

_source line 23 · 2026-05-20T23:51:15.095Z_

<details><summary>↩ Tool result · `toolu_01Aaq9aY8NWMSQFBXpRGouyt`</summary>

```text
1	"""Confusion matrix utilities: validation, generation, interpolation.
2	
3	Convention: C[j, i] = P(A*=j | A=i), columns sum to 1 (column-stochastic).
4	"""
5	
6	import numpy as np
7	
8	
9	def validate_confusion_matrix(C):
10	    """Check if C is a valid column-stochastic confusion matrix.
11	
12	    Args:
13	        C: array to validate
14	
15	    Returns:
16	        True if valid, False otherwise
17	    """
18	    if not isinstance(C, np.ndarray):
19	        return False
20	    if C.ndim != 2 or C.shape[0] != C.shape[1]:
21	        return False
22	    if C.shape[0] < 2:
23	        return False
24	    if (C < -1e-10).any():
25	        return False
26	    if not np.allclose(C.sum(axis=0), 1.0, atol=1e-6):
27	        return False
28	    return True
29	
30	
31	def random_confusion_matrix(K, diag_dominance=0.8, rng=None):
32	    """Generate a random column-stochastic confusion matrix.
33	
34	    Args:
35	        K: number of categories
36	        diag_dominance: controls diagonal strength (0 to 1)
37	        rng: numpy random Generator (created if None)
38	
39	    Returns:
40	        (K, K) column-stochastic matrix
41	    """
42	    if rng is None:
43	        rng = np.random.default_rng()
44	    diag_alpha = diag_dominance * 10
45	    offdiag_alpha = max((1 - diag_dominance) * 10 / max(K - 1, 1), 0.1)
46	    C = np.zeros((K, K))
47	    for k in range(K):
48	        alphas = np.full(K, offdiag_alpha)
49	        alphas[k] = diag_alpha
50	        C[:, k] = rng.dirichlet(alphas)
51	    return C
52	
53	
54	def interpolate_confusion(C0, delta):
55	    """Interpolate between identity and C0: C(delta) = (1-delta)*I + delta*C0.
56	
57	    Args:
58	        C0: (K, K) base confusion matrix
59	        delta: interpolation parameter (0 = identity, 1 = C0)
60	
61	    Returns:
62	        (K, K) interpolated column-stochastic matrix
63	    """
64	    K = C0.shape[0]
65	    C = (1 - delta) * np.eye(K) + delta * C0
66	    C = np.maximum(C, 0.0)
67	    col_sums = C.sum(axis=0)
68	    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)
69	    return C / col_sums
70	
71	
72	def delta_range(C0):
73	    """Compute valid delta range for interpolation.
74	
75	    Args:
76	        C0: (K, K) base confusion matrix
77	
78	    Returns:
79	        (delta_min, delta_max) tuple
80	    """
81	    min_diag = np.diag(C0).min()
82	    if min_diag >= 1.0:
83	        return (0.0, 10.0)
84	    delta_max = min(1.0 / (1.0 - min_diag), 10.0)
85	    return (0.0, delta_max)
86	
87	
88	def predefined_matrices(K=3):
89	    """Return a dict of predefined K x K confusion matrices.
90	
91	    Args:
92	        K: number of categories (only K=3 supported)
93	
94	    Returns:
95	        dict mapping name to (K, K) confusion matrix
96	    """
97	    if K != 3:
98	        raise ValueError(f"Predefined matrices only available for K=3, got K={K}")
99	    return {
100	        "symmetric_high": np.array([
101	            [0.80, 0.10, 0.10],
102	            [0.10, 0.80, 0.10],
103	            [0.10, 0.10, 0.80]]),
104	        "mild_uniform": np.array([
105	            [0.8 + 0.2 / 3, 0.2 / 3, 0.2 / 3],
106	            [0.2 / 3, 0.8 + 0.2 / 3, 0.2 / 3],
107	            [0.2 / 3, 0.2 / 3, 0.8 + 0.2 / 3]]),
108	        "moderate_uniform": np.array([
109	            [0.6 + 0.4 / 3, 0.4 / 3, 0.4 / 3],
110	            [0.4 / 3, 0.6 + 0.4 / 3, 0.4 / 3],
111	            [0.4 / 3, 0.4 / 3, 0.6 + 0.4 / 3]]),
112	        "severe_uniform": np.array([
113	            [0.4 + 0.6 / 3, 0.6 / 3, 0.6 / 3],
114	            [0.6 / 3, 0.4 + 0.6 / 3, 0.6 / 3],
115	            [0.6 / 3, 0.6 / 3, 0.4 + 0.6 / 3]]),
116	        "asymmetric": np.array([
117	            [0.75, 0.05, 0.05],
118	            [0.20, 0.80, 0.10],
119	            [0.05, 0.15, 0.85]]),
120	        "near_permutation": np.array([
121	            [0.05, 0.05, 0.90],
122	            [0.90, 0.05, 0.05],
123	            [0.05, 0.90, 0.05]]),
124	        "realistic_llm": np.array([
125	            [0.78, 0.15, 0.03],
126	            [0.18, 0.72, 0.18],
127	            [0.04, 0.13, 0.79]]),
128	    }
129	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "25aa9873-952f-421e-bd1a-fcc7886d96ea",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/confusion.py",
      "content": "\"\"\"Confusion matrix utilities: validation, generation, interpolation.\n\nConvention: C[j, i] = P(A*=j | A=i), columns sum to 1 (column-stochastic).\n\"\"\"\n\nimport numpy as np\n\n\ndef validate_confusion_matrix(C):\n    \"\"\"Check if C is a valid column-stochastic confusion matrix.\n\n    Args:\n        C: array to validate\n\n    Returns:\n        True if valid, False otherwise\n    \"\"\"\n    if not isinstance(C, np.ndarray):\n        return False\n    if C.ndim != 2 or C.shape[0] != C.shape[1]:\n        return False\n    if C.shape[0] < 2:\n        return False\n    if (C < -1e-10).any():\n        return False\n    if not np.allclose(C.sum(axis=0), 1.0, atol=1e-6):\n        return False\n    return True\n\n\ndef random_confusion_matrix(K, diag_dominance=0.8, rng=None):\n    \"\"\"Generate a random column-stochastic confusion matrix.\n\n    Args:\n        K: number of categories\n        diag_dominance: controls diagonal strength (0 to 1)\n        rng: numpy random Generator (created if None)\n\n    Returns:\n        (K, K) column-stochastic matrix\n    \"\"\"\n    if rng is None:\n        rng = np.random.default_rng()\n    diag_alpha = diag_dominance * 10\n    offdiag_alpha = max((1 - diag_dominance) * 10 / max(K - 1, 1), 0.1)\n    C = np.zeros((K, K))\n    for k in range(K):\n        alphas = np.full(K, offdiag_alpha)\n        alphas[k] = diag_alpha\n        C[:, k] = rng.dirichlet(alphas)\n    return C\n\n\ndef interpolate_confusion(C0, delta):\n    \"\"\"Interpolate between identity and C0: C(delta) = (1-delta)*I + delta*C0.\n\n    Args:\n        C0: (K, K) base confusion matrix\n        delta: interpolation parameter (0 = identity, 1 = C0)\n\n    Returns:\n        (K, K) interpolated column-stochastic matrix\n    \"\"\"\n    K = C0.shape[0]\n    C = (1 - delta) * np.eye(K) + delta * C0\n    C = np.maximum(C, 0.0)\n    col_sums = C.sum(axis=0)\n    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\n    return C / col_sums\n\n\ndef delta_range(C0):\n    \"\"\"Compute valid delta range for interpolation.\n\n    Args:\n        C0: (K, K) base confusion matrix\n\n    Returns:\n        (delta_min, delta_max) tuple\n    \"\"\"\n    min_diag = np.diag(C0).min()\n    if min_diag >= 1.0:\n        return (0.0, 10.0)\n    delta_max = min(1.0 / (1.0 - min_diag), 10.0)\n    return (0.0, delta_max)\n\n\ndef predefined_matrices(K=3):\n    \"\"\"Return a dict of predefined K x K confusion matrices.\n\n    Args:\n        K: number of categories (only K=3 supported)\n\n    Returns:\n        dict mapping name to (K, K) confusion matrix\n    \"\"\"\n    if K != 3:\n        raise ValueError(f\"Predefined matrices only available for K=3, got K={K}\")\n    return {\n        \"symmetric_high\": np.array([\n            [0.80, 0.10, 0.10],\n            [0.10, 0.80, 0.10],\n            [0.10, 0.10, 0.80]]),\n        \"mild_uniform\": np.array([\n            [0.8 + 0.2 / 3, 0.2 / 3, 0.2 / 3],\n            [0.2 / 3, 0.8 + 0.2 / 3, 0.2 / 3],\n            [0.2 / 3, 0.2 / 3, 0.8 + 0.2 / 3]]),\n        \"moderate_uniform\": np.array([\n            [0.6 + 0.4 / 3, 0.4 / 3, 0.4 / 3],\n            [0.4 / 3, 0.6 + 0.4 / 3, 0.4 / 3],\n            [0.4 / 3, 0.4 / 3, 0.6 + 0.4 / 3]]),\n        \"severe_uniform\": np.array([\n            [0.4 + 0.6 / 3, 0.6 / 3, 0.6 / 3],\n            [0.6 / 3, 0.4 + 0.6 / 3, 0.6 / 3],\n            [0.6 / 3, 0.6 / 3, 0.4 + 0.6 / 3]]),\n        \"asymmetric\": np.array([\n            [0.75, 0.05, 0.05],\n            [0.20, 0.80, 0.10],\n            [0.05, 0.15, 0.85]]),\n        \"near_permutation\": np.array([\n            [0.05, 0.05, 0.90],\n            [0.90, 0.05, 0.05],\n            [0.05, 0.90, 0.05]]),\n        \"realistic_llm\": np.array([\n            [0.78, 0.15, 0.03],\n            [0.18, 0.72, 0.18],\n            [0.04, 0.13, 0.79]]),\n    }\n",
      "numLines": 129,
      "startLine": 1,
      "totalLines": 129
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_0182DffEQeVjo2ZXtDxZz4gv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/utils.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "f7eb589b-b6e4-40a5-92c4-c69fdaf89267",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HQbEmFPpg3WkXvGvZH8S1P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21029,
      "cache_read_input_tokens": 26851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21029
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

_source line 25 · 2026-05-20T23:51:15.351Z_

<details><summary>↩ Tool result · `toolu_0182DffEQeVjo2ZXtDxZz4gv`</summary>

```text
1	"""Shared utilities: OLS, dummy encoding, softmax sampling."""
2	
3	import numpy as np
4	
5	
6	def softmax_sample(logits, rng):
7	    """Sample categorical variable from row-wise softmax probabilities.
8	
9	    Args:
10	        logits: (N, K) array of logits
11	        rng: numpy random Generator
12	
13	    Returns:
14	        (N,) integer array with values in {0, ..., K-1}
15	    """
16	    e = np.exp(logits - logits.max(axis=1, keepdims=True))
17	    p = e / e.sum(axis=1, keepdims=True)
18	    cum = np.cumsum(p, axis=1)
19	    u = rng.uniform(size=logits.shape[0])
20	    K = logits.shape[1]
21	    result = np.zeros(logits.shape[0], dtype=int)
22	    for k in range(K - 1):
23	        result += (u >= cum[:, k]).astype(int)
24	    return result
25	
26	
27	def misclassify(A, C, rng):
28	    """Apply misclassification: A*_i ~ Cat(C[:, A_i]).
29	
30	    Args:
31	        A: (N,) true labels in {0, ..., K-1}
32	        C: (K, K) column-stochastic confusion matrix
33	        rng: numpy random Generator
34	
35	    Returns:
36	        (N,) misclassified labels
37	    """
38	    K = C.shape[0]
39	    probs = C[:, A]
40	    cum = np.cumsum(probs, axis=0)
41	    u = rng.uniform(size=len(A))
42	    result = np.zeros(len(A), dtype=int)
43	    for k in range(K - 1):
44	        result += (u >= cum[k]).astype(int)
45	    return result
46	
47	
48	def make_dummies(A, K=None):
49	    """Create K-1 dummy variables (reference category 0).
50	
51	    Args:
52	        A: (N,) categorical labels in {0, ..., K-1}
53	        K: number of categories (inferred from A if None)
54	
55	    Returns:
56	        (N, K-1) dummy matrix
57	    """
58	    if K is None:
59	        K = int(A.max()) + 1
60	    N = len(A)
61	    D = np.zeros((N, K - 1))
62	    for j in range(K - 1):
63	        D[:, j] = (A == j + 1).astype(float)
64	    return D
65	
66	
67	def make_full_dummies(A, K=None):
68	    """Create full K one-hot encoding.
69	
70	    Args:
71	        A: (N,) categorical labels in {0, ..., K-1}
72	        K: number of categories (inferred from A if None)
73	
74	    Returns:
75	        (N, K) one-hot matrix
76	    """
77	    if K is None:
78	        K = int(A.max()) + 1
79	    N = len(A)
80	    D = np.zeros((N, K))
81	    for j in range(K):
82	        D[:, j] = (A == j).astype(float)
83	    return D
84	
85	
86	def ols(X, Y):
87	    """OLS point estimate via least-squares.
88	
89	    Args:
90	        X: (N, p) design matrix
91	        Y: (N,) response
92	
93	    Returns:
94	        (p,) coefficient vector
95	    """
96	    return np.linalg.lstsq(X, Y, rcond=None)[0]
97	
98	
99	def ols_with_se(X, Y):
100	    """OLS point estimate with homoskedastic standard errors.
101	
102	    Args:
103	        X: (N, p) design matrix
104	        Y: (N,) response
105	
106	    Returns:
107	        (beta, se) tuple of (p,) arrays
108	    """
109	    beta = np.linalg.lstsq(X, Y, rcond=None)[0]
110	    resid = Y - X @ beta
111	    n, p = X.shape
112	    s2 = resid @ resid / max(n - p, 1)
113	    try:
114	        XtX_inv = np.linalg.inv(X.T @ X)
115	        se = np.sqrt(np.maximum(np.diag(s2 * XtX_inv), 0.0))
116	    except np.linalg.LinAlgError:
117	        se = np.full(p, np.nan)
118	    return beta, se
119	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "9c4569f6-fe0c-4fc6-a7e1-be812f279429",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/utils.py",
      "content": "\"\"\"Shared utilities: OLS, dummy encoding, softmax sampling.\"\"\"\n\nimport numpy as np\n\n\ndef softmax_sample(logits, rng):\n    \"\"\"Sample categorical variable from row-wise softmax probabilities.\n\n    Args:\n        logits: (N, K) array of logits\n        rng: numpy random Generator\n\n    Returns:\n        (N,) integer array with values in {0, ..., K-1}\n    \"\"\"\n    e = np.exp(logits - logits.max(axis=1, keepdims=True))\n    p = e / e.sum(axis=1, keepdims=True)\n    cum = np.cumsum(p, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    K = logits.shape[1]\n    result = np.zeros(logits.shape[0], dtype=int)\n    for k in range(K - 1):\n        result += (u >= cum[:, k]).astype(int)\n    return result\n\n\ndef misclassify(A, C, rng):\n    \"\"\"Apply misclassification: A*_i ~ Cat(C[:, A_i]).\n\n    Args:\n        A: (N,) true labels in {0, ..., K-1}\n        C: (K, K) column-stochastic confusion matrix\n        rng: numpy random Generator\n\n    Returns:\n        (N,) misclassified labels\n    \"\"\"\n    K = C.shape[0]\n    probs = C[:, A]\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    result = np.zeros(len(A), dtype=int)\n    for k in range(K - 1):\n        result += (u >= cum[k]).astype(int)\n    return result\n\n\ndef make_dummies(A, K=None):\n    \"\"\"Create K-1 dummy variables (reference category 0).\n\n    Args:\n        A: (N,) categorical labels in {0, ..., K-1}\n        K: number of categories (inferred from A if None)\n\n    Returns:\n        (N, K-1) dummy matrix\n    \"\"\"\n    if K is None:\n        K = int(A.max()) + 1\n    N = len(A)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    return D\n\n\ndef make_full_dummies(A, K=None):\n    \"\"\"Create full K one-hot encoding.\n\n    Args:\n        A: (N,) categorical labels in {0, ..., K-1}\n        K: number of categories (inferred from A if None)\n\n    Returns:\n        (N, K) one-hot matrix\n    \"\"\"\n    if K is None:\n        K = int(A.max()) + 1\n    N = len(A)\n    D = np.zeros((N, K))\n    for j in range(K):\n        D[:, j] = (A == j).astype(float)\n    return D\n\n\ndef ols(X, Y):\n    \"\"\"OLS point estimate via least-squares.\n\n    Args:\n        X: (N, p) design matrix\n        Y: (N,) response\n\n    Returns:\n        (p,) coefficient vector\n    \"\"\"\n    return np.linalg.lstsq(X, Y, rcond=None)[0]\n\n\ndef ols_with_se(X, Y):\n    \"\"\"OLS point estimate with homoskedastic standard errors.\n\n    Args:\n        X: (N, p) design matrix\n        Y: (N,) response\n\n    Returns:\n        (beta, se) tuple of (p,) arrays\n    \"\"\"\n    beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n    resid = Y - X @ beta\n    n, p = X.shape\n    s2 = resid @ resid / max(n - p, 1)\n    try:\n        XtX_inv = np.linalg.inv(X.T @ X)\n        se = np.sqrt(np.maximum(np.diag(s2 * XtX_inv), 0.0))\n    except np.linalg.LinAlgError:\n        se = np.full(p, np.nan)\n    return beta, se\n",
      "numLines": 119,
      "startLine": 1,
      "totalLines": 119
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Now I have a full picture. Let me summarize what needs to happen:

### W1: Fix IV topology to use Wald estimator instead of OLS

Current state in `bias.py`:
- `_precompute()` computes stats for OLS (E_Y, E_DA, E_DA_Y, and if HAS_TREATMENT: E_T, E_T2, E_TY, E_DA_T)
- `_get_tau()` dispatches to `_plim_with_T()` or `_plim_no_T()` based on HAS_TREATMENT


- IV is in the `NO_TREATMENT` set, so it incorrectly uses the OLS path: Y ~ 1 + D*_1 + ... + D*_{K-1}, when it should instead compute the Wald estimator as tau = RF / FS*_1

The reference implementation shows how to properly handle IV by generating data with a binary instrument Z, then computing the reduced form effect (RF) and first stage effects (FS) for each treatment variable.

The package uses a continuous normal instrument Z ~ N(0,1) instead of binary, so I need to adapt the approach: RF becomes the covariance between Z and Y divided by the variance of Z, and each first stage coefficient FS[k] is the covariance between Z and the k-th treatment divided by the variance of Z. Writing IV implementation... Computing covariance and variance directly from the simulated data is cleaner—I'll calculate the first-stage F-statistic and reduced-form coefficient by dividing the covariance of Z with each variable by Z's variance, avoiding unnecessary allocations. I'm defining the IV estimator function that computes the probability limit using the reduced form coefficient divided by the first element of the transformed first stage coefficients, with a check for near-zero denominators. Then I'm refactoring `_get_tau` to dispatch to the appropriate probability limit function based on the topology type.

I'm thinking through the edge cases: when the transformation matrix is identity, the first stage should be nonzero since the instrument affects treatment assignment; when it's a near-permutation, the first stage element could approach zero or flip sign, which captures the sign reversal phenomenon I'm investigating.

Now I'm ready to implement these changes and write the test class for the correction methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "ccdfd5e6-b240-4dd6-8b8a-03564121fe6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018TreD2GgfaTyCnR7KXBPYD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13983,
      "cache_read_input_tokens": 47880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13983
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

_source line 27_

I now have a complete picture of the codebase. Let me implement both fixes.

**W1**: IV topology currently falls through to `_plim_no_T` (OLS), but needs Wald estimator `RF / (C @ FS)[1]`. The key insight: `gen_iv` uses continuous Z ~ N(0,1), so I'll use covariance-based RF and FS.

**W2**: Add correction method tests.

Let me start with the W1 core fix in `bias.py`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "6b3b4012-eefd-43a9-892a-2dbcba755fee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018TreD2GgfaTyCnR7KXBPYD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13983,
      "cache_read_input_tokens": 47880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13983
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

_source line 28_

<details open><summary>🔧 Tool call — Edit · `toolu_01UbmCHK5MPAPGUX9UFUVTTZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py",
  "old_string": "    if topology in HAS_TREATMENT:\n        T = data[\"T\"]\n        stats.update({\n            \"E_T\": T.mean(),\n            \"E_T2\": (T ** 2).mean(),\n            \"E_TY\": (T * Y).mean(),\n            \"E_DA_T\": (DA * T[:, None]).mean(0),\n        })\n\n    _precomp_cache[cache_key] = stats\n    return stats",
  "new_string": "    if topology in HAS_TREATMENT:\n        T = data[\"T\"]\n        stats.update({\n            \"E_T\": T.mean(),\n            \"E_T2\": (T ** 2).mean(),\n            \"E_TY\": (T * Y).mean(),\n            \"E_DA_T\": (DA * T[:, None]).mean(0),\n        })\n\n    if topology == \"iv\":\n        Z = data[\"Z\"]\n        Zc = Z - Z.mean()\n        var_Z = (Zc ** 2).mean()\n        stats[\"RF\"] = (Zc * (Y - Y.mean())).mean() / var_Z\n        FS = np.zeros(K)\n        for k in range(K):\n            FS[k] = (Zc * (DA[:, k] - DA[:, k].mean())).mean() / var_Z\n        stats[\"FS\"] = FS\n\n    _precomp_cache[cache_key] = stats\n    return stats"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "e39c271b-b73f-4f0f-b3ff-3404e0e3fcea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018TreD2GgfaTyCnR7KXBPYD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13983,
      "cache_read_input_tokens": 47880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13983
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

_source line 29 · 2026-05-20T23:52:02.313Z_

<details><summary>↩ Tool result · `toolu_01UbmCHK5MPAPGUX9UFUVTTZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "967352ae-f0c4-43e5-8b33-832accaf3f6f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py",
    "oldString": "    if topology in HAS_TREATMENT:\n        T = data[\"T\"]\n        stats.update({\n            \"E_T\": T.mean(),\n            \"E_T2\": (T ** 2).mean(),\n            \"E_TY\": (T * Y).mean(),\n            \"E_DA_T\": (DA * T[:, None]).mean(0),\n        })\n\n    _precomp_cache[cache_key] = stats\n    return stats",
    "newString": "    if topology in HAS_TREATMENT:\n        T = data[\"T\"]\n        stats.update({\n            \"E_T\": T.mean(),\n            \"E_T2\": (T ** 2).mean(),\n            \"E_TY\": (T * Y).mean(),\n            \"E_DA_T\": (DA * T[:, None]).mean(0),\n        })\n\n    if topology == \"iv\":\n        Z = data[\"Z\"]\n        Zc = Z - Z.mean()\n        var_Z = (Zc ** 2).mean()\n        stats[\"RF\"] = (Zc * (Y - Y.mean())).mean() / var_Z\n        FS = np.zeros(K)\n        for k in range(K):\n            FS[k] = (Zc * (DA[:, k] - DA[:, k].mean())).mean() / var_Z\n        stats[\"FS\"] = FS\n\n    _precomp_cache[cache_key] = stats\n    return stats",
    "originalFile": "\"\"\"Compute annotation-error bias via probability limit calculations.\n\nUses precomputed sufficient statistics from large-sample DGP simulations\nto compute OLS plim as a function of confusion matrix C, avoiding MC.\n\"\"\"\n\nimport warnings\nimport numpy as np\nfrom .dgp import DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES\nfrom .confusion import validate_confusion_matrix\n\n_N_PRECOMP = 2_000_000\n_precomp_cache = {}\n\n\ndef _params_key(params):\n    items = []\n    for k, v in sorted(params.items()):\n        if isinstance(v, np.ndarray):\n            items.append((k, tuple(v.flat)))\n        else:\n            items.append((k, v))\n    return tuple(items)\n\n\ndef _precompute(topology, params, K, seed=999):\n    \"\"\"Precompute sufficient statistics for plim calculation.\"\"\"\n    cache_key = (topology, _params_key(params), K)\n    if cache_key in _precomp_cache:\n        return _precomp_cache[cache_key]\n\n    rng = np.random.default_rng(seed)\n    data = GEN_FUNCS[topology](_N_PRECOMP, params=params, rng=rng)\n    Y = data[\"Y\"]\n    A = data[\"A\"]\n\n    DA = np.zeros((_N_PRECOMP, K))\n    for k in range(K):\n        DA[:, k] = (A == k).astype(float)\n\n    stats = {\n        \"E_Y\": Y.mean(),\n        \"E_DA\": DA.mean(0),\n        \"E_DA_Y\": (DA * Y[:, None]).mean(0),\n    }\n\n    if topology in HAS_TREATMENT:\n        T = data[\"T\"]\n        stats.update({\n            \"E_T\": T.mean(),\n            \"E_T2\": (T ** 2).mean(),\n            \"E_TY\": (T * Y).mean(),\n            \"E_DA_T\": (DA * T[:, None]).mean(0),\n        })\n\n    _precomp_cache[cache_key] = stats\n    return stats\n\n\ndef _plim_with_T(C, stats, K):\n    \"\"\"OLS plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}.\"\"\"\n    ds = C @ stats[\"E_DA\"]\n    dst = C @ stats[\"E_DA_T\"]\n    dsy = C @ stats[\"E_DA_Y\"]\n    ET, ET2 = stats[\"E_T\"], stats[\"E_T2\"]\n    EY, ETY = stats[\"E_Y\"], stats[\"E_TY\"]\n\n    dim = 1 + K  # intercept + T + (K-1) dummies\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    EZZ[0, 1] = EZZ[1, 0] = ET\n    EZZ[1, 1] = ET2\n    for j in range(1, K):\n        idx = j + 1\n        EZZ[0, idx] = EZZ[idx, 0] = ds[j]\n        EZZ[1, idx] = EZZ[idx, 1] = dst[j]\n        EZZ[idx, idx] = ds[j]\n\n    EZY = np.zeros(dim)\n    EZY[0] = EY\n    EZY[1] = ETY\n    for j in range(1, K):\n        EZY[j + 1] = dsy[j]\n\n    cond = np.linalg.cond(EZZ)\n    if cond > 1e12:\n        warnings.warn(\n            f\"EZZ condition number {cond:.1e} — plim may be numerically unstable\"\n        )\n\n    return np.linalg.solve(EZZ, EZY)\n\n\ndef _plim_no_T(C, stats, K):\n    \"\"\"OLS plim for Y ~ 1 + D*_1 + ... + D*_{K-1}.\"\"\"\n    ds = C @ stats[\"E_DA\"]\n    dsy = C @ stats[\"E_DA_Y\"]\n    EY = stats[\"E_Y\"]\n\n    dim = K  # intercept + (K-1) dummies\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    for j in range(1, K):\n        EZZ[0, j] = EZZ[j, 0] = ds[j]\n        EZZ[j, j] = ds[j]\n\n    EZY = np.zeros(dim)\n    EZY[0] = EY\n    for j in range(1, K):\n        EZY[j] = dsy[j]\n\n    cond = np.linalg.cond(EZZ)\n    if cond > 1e12:\n        warnings.warn(\n            f\"EZZ condition number {cond:.1e} — plim may be numerically unstable\"\n        )\n\n    return np.linalg.solve(EZZ, EZY)\n\n\ndef _get_tau(topology, C, stats, K):\n    \"\"\"Extract target coefficient from plim vector.\n\n    For topologies with T: coefficient index 1 (treatment effect).\n    For topologies without T: coefficient index 1 (first dummy).\n    \"\"\"\n    if topology in HAS_TREATMENT:\n        coefs = _plim_with_T(C, stats, K)\n    else:\n        coefs = _plim_no_T(C, stats, K)\n    return coefs[1]\n\n\ndef compute_bias(topology, C, params=None):\n    \"\"\"Compute annotation-error bias for a given topology and confusion matrix.\n\n    Args:\n        topology: one of \"confounding\", \"mediation\", \"collider\", \"exposure\",\n                  \"mbias\", \"iv\", \"frontdoor\"\n        C: (K, K) column-stochastic confusion matrix, C[j,i] = P(A*=j|A=i)\n        params: optional DGP parameters dict, None uses defaults\n\n    Returns:\n        dict with tau_true, tau_biased, bias, bias_pct, topology\n    \"\"\"\n    if topology not in TOPOLOGIES:\n        raise ValueError(f\"Unknown topology: {topology}. Choose from {TOPOLOGIES}\")\n    if not validate_confusion_matrix(C):\n        raise ValueError(\"C must be a square, non-negative, column-stochastic matrix\")\n\n    K = C.shape[0]\n    merged = dict(DEFAULT_PARAMS[topology])\n    if params is not None:\n        merged.update(params)\n\n    stats = _precompute(topology, merged, K)\n    tau_true = _get_tau(topology, np.eye(K), stats, K)\n    tau_biased = _get_tau(topology, C, stats, K)\n    bias = tau_biased - tau_true\n    bias_pct = 100.0 * bias / tau_true if abs(tau_true) > 1e-12 else float(\"nan\")\n\n    return {\n        \"tau_true\": float(tau_true),\n        \"tau_biased\": float(tau_biased),\n        \"bias\": float(bias),\n        \"bias_pct\": float(bias_pct),\n        \"topology\": topology,\n    }\n\n\ndef clear_cache():\n    \"\"\"Clear the precomputed statistics cache.\"\"\"\n    _precomp_cache.clear()\n",
    "structuredPatch": [
      {
        "oldStart": 53,
        "oldLines": 6,
        "newStart": 53,
        "newLines": 16,
        "lines": [
          "             \"E_DA_T\": (DA * T[:, None]).mean(0),",
          "         })",
          " ",
          "+    if topology == \"iv\":",
          "+        Z = data[\"Z\"]",
          "+        Zc = Z - Z.mean()",
          "+        var_Z = (Zc ** 2).mean()",
          "+        stats[\"RF\"] = (Zc * (Y - Y.mean())).mean() / var_Z",
          "+        FS = np.zeros(K)",
          "+        for k in range(K):",
          "+            FS[k] = (Zc * (DA[:, k] - DA[:, k].mean())).mean() / var_Z",
          "+        stats[\"FS\"] = FS",
          "+",
          "     _precomp_cache[cache_key] = stats",
          "     return stats",
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

_source line 30_

<details open><summary>🔧 Tool call — Edit · `toolu_01RsVFpq5yoE4QWUgXi5eQqm`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py",
  "old_string": "def _get_tau(topology, C, stats, K):\n    \"\"\"Extract target coefficient from plim vector.\n\n    For topologies with T: coefficient index 1 (treatment effect).\n    For topologies without T: coefficient index 1 (first dummy).\n    \"\"\"\n    if topology in HAS_TREATMENT:\n        coefs = _plim_with_T(C, stats, K)\n    else:\n        coefs = _plim_no_T(C, stats, K)\n    return coefs[1]",
  "new_string": "def _plim_iv(C, stats, K):\n    \"\"\"Wald estimator plim: RF / (C @ FS)[1].\"\"\"\n    FS_star = C @ stats[\"FS\"]\n    denom = FS_star[1]\n    if abs(denom) < 1e-15:\n        return np.nan\n    return stats[\"RF\"] / denom\n\n\ndef _get_tau(topology, C, stats, K):\n    \"\"\"Extract target coefficient from plim vector.\n\n    For IV: Wald estimator RF / (C @ FS)[1].\n    For topologies with T: OLS coefficient index 1 (treatment effect).\n    For topologies without T: OLS coefficient index 1 (first dummy).\n    \"\"\"\n    if topology == \"iv\":\n        return _plim_iv(C, stats, K)\n    if topology in HAS_TREATMENT:\n        coefs = _plim_with_T(C, stats, K)\n    else:\n        coefs = _plim_no_T(C, stats, K)\n    return coefs[1]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "63df7fb4-69e2-4966-9956-0a575c5744b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XSr1a4gHydkKAWYncbtsgM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2719,
      "cache_read_input_tokens": 61863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2719
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

_source line 31 · 2026-05-20T23:52:09.896Z_

<details><summary>↩ Tool result · `toolu_01RsVFpq5yoE4QWUgXi5eQqm`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "935290b7-e478-408e-aa63-f803cae5c9ab",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py",
    "oldString": "def _get_tau(topology, C, stats, K):\n    \"\"\"Extract target coefficient from plim vector.\n\n    For topologies with T: coefficient index 1 (treatment effect).\n    For topologies without T: coefficient index 1 (first dummy).\n    \"\"\"\n    if topology in HAS_TREATMENT:\n        coefs = _plim_with_T(C, stats, K)\n    else:\n        coefs = _plim_no_T(C, stats, K)\n    return coefs[1]",
    "newString": "def _plim_iv(C, stats, K):\n    \"\"\"Wald estimator plim: RF / (C @ FS)[1].\"\"\"\n    FS_star = C @ stats[\"FS\"]\n    denom = FS_star[1]\n    if abs(denom) < 1e-15:\n        return np.nan\n    return stats[\"RF\"] / denom\n\n\ndef _get_tau(topology, C, stats, K):\n    \"\"\"Extract target coefficient from plim vector.\n\n    For IV: Wald estimator RF / (C @ FS)[1].\n    For topologies with T: OLS coefficient index 1 (treatment effect).\n    For topologies without T: OLS coefficient index 1 (first dummy).\n    \"\"\"\n    if topology == \"iv\":\n        return _plim_iv(C, stats, K)\n    if topology in HAS_TREATMENT:\n        coefs = _plim_with_T(C, stats, K)\n    else:\n        coefs = _plim_no_T(C, stats, K)\n    return coefs[1]",
    "originalFile": "\"\"\"Compute annotation-error bias via probability limit calculations.\n\nUses precomputed sufficient statistics from large-sample DGP simulations\nto compute OLS plim as a function of confusion matrix C, avoiding MC.\n\"\"\"\n\nimport warnings\nimport numpy as np\nfrom .dgp import DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES\nfrom .confusion import validate_confusion_matrix\n\n_N_PRECOMP = 2_000_000\n_precomp_cache = {}\n\n\ndef _params_key(params):\n    items = []\n    for k, v in sorted(params.items()):\n        if isinstance(v, np.ndarray):\n            items.append((k, tuple(v.flat)))\n        else:\n            items.append((k, v))\n    return tuple(items)\n\n\ndef _precompute(topology, params, K, seed=999):\n    \"\"\"Precompute sufficient statistics for plim calculation.\"\"\"\n    cache_key = (topology, _params_key(params), K)\n    if cache_key in _precomp_cache:\n        return _precomp_cache[cache_key]\n\n    rng = np.random.default_rng(seed)\n    data = GEN_FUNCS[topology](_N_PRECOMP, params=params, rng=rng)\n    Y = data[\"Y\"]\n    A = data[\"A\"]\n\n    DA = np.zeros((_N_PRECOMP, K))\n    for k in range(K):\n        DA[:, k] = (A == k).astype(float)\n\n    stats = {\n        \"E_Y\": Y.mean(),\n        \"E_DA\": DA.mean(0),\n        \"E_DA_Y\": (DA * Y[:, None]).mean(0),\n    }\n\n    if topology in HAS_TREATMENT:\n        T = data[\"T\"]\n        stats.update({\n            \"E_T\": T.mean(),\n            \"E_T2\": (T ** 2).mean(),\n            \"E_TY\": (T * Y).mean(),\n            \"E_DA_T\": (DA * T[:, None]).mean(0),\n        })\n\n    if topology == \"iv\":\n        Z = data[\"Z\"]\n        Zc = Z - Z.mean()\n        var_Z = (Zc ** 2).mean()\n        stats[\"RF\"] = (Zc * (Y - Y.mean())).mean() / var_Z\n        FS = np.zeros(K)\n        for k in range(K):\n            FS[k] = (Zc * (DA[:, k] - DA[:, k].mean())).mean() / var_Z\n        stats[\"FS\"] = FS\n\n    _precomp_cache[cache_key] = stats\n    return stats\n\n\ndef _plim_with_T(C, stats, K):\n    \"\"\"OLS plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}.\"\"\"\n    ds = C @ stats[\"E_DA\"]\n    dst = C @ stats[\"E_DA_T\"]\n    dsy = C @ stats[\"E_DA_Y\"]\n    ET, ET2 = stats[\"E_T\"], stats[\"E_T2\"]\n    EY, ETY = stats[\"E_Y\"], stats[\"E_TY\"]\n\n    dim = 1 + K  # intercept + T + (K-1) dummies\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    EZZ[0, 1] = EZZ[1, 0] = ET\n    EZZ[1, 1] = ET2\n    for j in range(1, K):\n        idx = j + 1\n        EZZ[0, idx] = EZZ[idx, 0] = ds[j]\n        EZZ[1, idx] = EZZ[idx, 1] = dst[j]\n        EZZ[idx, idx] = ds[j]\n\n    EZY = np.zeros(dim)\n    EZY[0] = EY\n    EZY[1] = ETY\n    for j in range(1, K):\n        EZY[j + 1] = dsy[j]\n\n    cond = np.linalg.cond(EZZ)\n    if cond > 1e12:\n        warnings.warn(\n            f\"EZZ condition number {cond:.1e} — plim may be numerically unstable\"\n        )\n\n    return np.linalg.solve(EZZ, EZY)\n\n\ndef _plim_no_T(C, stats, K):\n    \"\"\"OLS plim for Y ~ 1 + D*_1 + ... + D*_{K-1}.\"\"\"\n    ds = C @ stats[\"E_DA\"]\n    dsy = C @ stats[\"E_DA_Y\"]\n    EY = stats[\"E_Y\"]\n\n    dim = K  # intercept + (K-1) dummies\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    for j in range(1, K):\n        EZZ[0, j] = EZZ[j, 0] = ds[j]\n        EZZ[j, j] = ds[j]\n\n    EZY = np.zeros(dim)\n    EZY[0] = EY\n    for j in range(1, K):\n        EZY[j] = dsy[j]\n\n    cond = np.linalg.cond(EZZ)\n    if cond > 1e12:\n        warnings.warn(\n            f\"EZZ condition number {cond:.1e} — plim may be numerically unstable\"\n        )\n\n    return np.linalg.solve(EZZ, EZY)\n\n\ndef _get_tau(topology, C, stats, K):\n    \"\"\"Extract target coefficient from plim vector.\n\n    For topologies with T: coefficient index 1 (treatment effect).\n    For topologies without T: coefficient index 1 (first dummy).\n    \"\"\"\n    if topology in HAS_TREATMENT:\n        coefs = _plim_with_T(C, stats, K)\n    else:\n        coefs = _plim_no_T(C, stats, K)\n    return coefs[1]\n\n\ndef compute_bias(topology, C, params=None):\n    \"\"\"Compute annotation-error bias for a given topology and confusion matrix.\n\n    Args:\n        topology: one of \"confounding\", \"mediation\", \"collider\", \"exposure\",\n                  \"mbias\", \"iv\", \"frontdoor\"\n        C: (K, K) column-stochastic confusion matrix, C[j,i] = P(A*=j|A=i)\n        params: optional DGP parameters dict, None uses defaults\n\n    Returns:\n        dict with tau_true, tau_biased, bias, bias_pct, topology\n    \"\"\"\n    if topology not in TOPOLOGIES:\n        raise ValueError(f\"Unknown topology: {topology}. Choose from {TOPOLOGIES}\")\n    if not validate_confusion_matrix(C):\n        raise ValueError(\"C must be a square, non-negative, column-stochastic matrix\")\n\n    K = C.shape[0]\n    merged = dict(DEFAULT_PARAMS[topology])\n    if params is not None:\n        merged.update(params)\n\n    stats = _precompute(topology, merged, K)\n    tau_true = _get_tau(topology, np.eye(K), stats, K)\n    tau_biased = _get_tau(topology, C, stats, K)\n    bias = tau_biased - tau_true\n    bias_pct = 100.0 * bias / tau_true if abs(tau_true) > 1e-12 else float(\"nan\")\n\n    return {\n        \"tau_true\": float(tau_true),\n        \"tau_biased\": float(tau_biased),\n        \"bias\": float(bias),\n        \"bias_pct\": float(bias_pct),\n        \"topology\": topology,\n    }\n\n\ndef clear_cache():\n    \"\"\"Clear the precomputed statistics cache.\"\"\"\n    _precomp_cache.clear()\n",
    "structuredPatch": [
      {
        "oldStart": 128,
        "oldLines": 12,
        "newStart": 128,
        "newLines": 24,
        "lines": [
          "     return np.linalg.solve(EZZ, EZY)",
          " ",
          " ",
          "+def _plim_iv(C, stats, K):",
          "+    \"\"\"Wald estimator plim: RF / (C @ FS)[1].\"\"\"",
          "+    FS_star = C @ stats[\"FS\"]",
          "+    denom = FS_star[1]",
          "+    if abs(denom) < 1e-15:",
          "+        return np.nan",
          "+    return stats[\"RF\"] / denom",
          "+",
          "+",
          " def _get_tau(topology, C, stats, K):",
          "     \"\"\"Extract target coefficient from plim vector.",
          " ",
          "-    For topologies with T: coefficient index 1 (treatment effect).",
          "-    For topologies without T: coefficient index 1 (first dummy).",
          "+    For IV: Wald estimator RF / (C @ FS)[1].",
          "+    For topologies with T: OLS coefficient index 1 (treatment effect).",
          "+    For topologies without T: OLS coefficient index 1 (first dummy).",
          "     \"\"\"",
          "+    if topology == \"iv\":",
          "+        return _plim_iv(C, stats, K)",
          "     if topology in HAS_TREATMENT:",
          "         coefs = _plim_with_T(C, stats, K)",
          "     else:"
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

_source line 32_

Now run the existing 35 tests to confirm nothing breaks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "c93a4242-78ed-4af3-8c83-79f22cce179f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQeD5qZr9VU1nZs4nqV2Cs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 64582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 585
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

_source line 33_

<details open><summary>🔧 Tool call — Bash · `toolu_015SmzDfecfNYii5ZmJqCGrb`</summary>

```json
{
  "command": "python3 -m pytest annot_sensitivity/tests/test_core.py -v 2>&1",
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
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "77743d41-1671-490a-bd60-818221e3df45",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQeD5qZr9VU1nZs4nqV2Cs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 585,
      "cache_read_input_tokens": 64582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 585
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

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bnlwa2dps",
  "tool_use_id": "toolu_015SmzDfecfNYii5ZmJqCGrb",
  "description": "python3 -m pytest annot_sensitivity/tests/test_core.py -v 2>&1",
  "task_type": "local_bash",
  "uuid": "5407920a-ae71-4764-929e-b2f5edef9315",
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020"
}
```

---

### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bnlwa2dps",
  "tool_use_id": "toolu_015SmzDfecfNYii5ZmJqCGrb",
  "status": "completed",
  "output_file": "",
  "summary": "python3 -m pytest annot_sensitivity/tests/test_core.py -v 2>&1",
  "uuid": "8e3585f9-d262-4924-b4a2-f37f92691387",
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020"
}
```

---

### Tool result

_source line 36 · 2026-05-20T23:52:24.506Z_

<details><summary>↩ Tool result · `toolu_015SmzDfecfNYii5ZmJqCGrb`</summary>

```text
============================= test session starts ==============================
platform linux -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib
plugins: anyio-4.13.0, typeguard-4.4.4
collecting ... collected 35 items

annot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_identity_valid PASSED [  2%]
annot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_predefined_valid PASSED [  5%]
annot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_non_square PASSED [  8%]
annot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_negative_entries PASSED [ 11%]
annot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_not_column_stochastic PASSED [ 14%]
annot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_not_array PASSED [ 17%]
annot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_1x1 PASSED [ 20%]
annot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_random_valid PASSED [ 22%]
annot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_delta_zero_is_identity PASSED [ 25%]
annot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_delta_one_is_C0 PASSED [ 28%]
annot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_intermediate_column_stochastic PASSED [ 31%]
annot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_small_delta PASSED [ 34%]
annot_sensitivity/tests/test_core.py::TestComputeBias::test_identity_zero_bias PASSED [ 37%]
annot_sensitivity/tests/test_core.py::TestComputeBias::test_confounding_nonzero_bias PASSED [ 40%]
annot_sensitivity/tests/test_core.py::TestComputeBias::test_all_topologies_run PASSED [ 42%]
annot_sensitivity/tests/test_core.py::TestComputeBias::test_invalid_topology PASSED [ 45%]
annot_sensitivity/tests/test_core.py::TestComputeBias::test_invalid_C PASSED [ 48%]
annot_sensitivity/tests/test_core.py::TestComputeBias::test_worse_C_more_bias PASSED [ 51%]
annot_sensitivity/tests/test_core.py::TestComputeASV::test_returns_valid_structure PASSED [ 54%]
annot_sensitivity/tests/test_core.py::TestComputeASV::test_asv_is_positive_or_none PASSED [ 57%]
annot_sensitivity/tests/test_core.py::TestComputeASV::test_envelope_monotone PASSED [ 60%]
annot_sensitivity/tests/test_core.py::TestComputeASV::test_sign_flip_threshold PASSED [ 62%]
annot_sensitivity/tests/test_core.py::TestComputeASV::test_invalid_threshold_type PASSED [ 65%]
annot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_with_gold_recommends_ppi PASSED [ 68%]
annot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_confounding_recommends_dsl PASSED [ 71%]
annot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_mediation_recommends_dsl PASSED [ 74%]
annot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_collider_recommends_mcsimex PASSED [ 77%]
annot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_mbias_recommends_mcsimex PASSED [ 80%]
annot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_ranking_has_all_methods PASSED [ 82%]
annot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_notes_nonempty PASSED [ 85%]
annot_sensitivity/tests/test_core.py::TestDGP::test_generate_all_topologies PASSED [ 88%]
annot_sensitivity/tests/test_core.py::TestDGP::test_confounding_has_treatment PASSED [ 91%]
annot_sensitivity/tests/test_core.py::TestDGP::test_exposure_no_treatment PASSED [ 94%]
annot_sensitivity/tests/test_core.py::TestDGP::test_iv_has_instrument PASSED [ 97%]
annot_sensitivity/tests/test_core.py::TestDGP::test_invalid_topology PASSED [100%]

============================== 35 passed in 9.53s ==============================
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "36ba4f61-5837-47f3-81ee-dcad13bbf2de",
  "tool_use_result": {
    "stdout": "============================= test session starts ==============================\nplatform linux -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- /usr/bin/python3\ncachedir: .pytest_cache\nrootdir: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib\nplugins: anyio-4.13.0, typeguard-4.4.4\ncollecting ... collected 35 items\n\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_identity_valid PASSED [  2%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_predefined_valid PASSED [  5%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_non_square PASSED [  8%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_negative_entries PASSED [ 11%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_not_column_stochastic PASSED [ 14%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_not_array PASSED [ 17%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_1x1 PASSED [ 20%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_random_valid PASSED [ 22%]\nannot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_delta_zero_is_identity PASSED [ 25%]\nannot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_delta_one_is_C0 PASSED [ 28%]\nannot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_intermediate_column_stochastic PASSED [ 31%]\nannot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_small_delta PASSED [ 34%]\nannot_sensitivity/tests/test_core.py::TestComputeBias::test_identity_zero_bias PASSED [ 37%]\nannot_sensitivity/tests/test_core.py::TestComputeBias::test_confounding_nonzero_bias PASSED [ 40%]\nannot_sensitivity/tests/test_core.py::TestComputeBias::test_all_topologies_run PASSED [ 42%]\nannot_sensitivity/tests/test_core.py::TestComputeBias::test_invalid_topology PASSED [ 45%]\nannot_sensitivity/tests/test_core.py::TestComputeBias::test_invalid_C PASSED [ 48%]\nannot_sensitivity/tests/test_core.py::TestComputeBias::test_worse_C_more_bias PASSED [ 51%]\nannot_sensitivity/tests/test_core.py::TestComputeASV::test_returns_valid_structure PASSED [ 54%]\nannot_sensitivity/tests/test_core.py::TestComputeASV::test_asv_is_positive_or_none PASSED [ 57%]\nannot_sensitivity/tests/test_core.py::TestComputeASV::test_envelope_monotone PASSED [ 60%]\nannot_sensitivity/tests/test_core.py::TestComputeASV::test_sign_flip_threshold PASSED [ 62%]\nannot_sensitivity/tests/test_core.py::TestComputeASV::test_invalid_threshold_type PASSED [ 65%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_with_gold_recommends_ppi PASSED [ 68%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_confounding_recommends_dsl PASSED [ 71%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_mediation_recommends_dsl PASSED [ 74%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_collider_recommends_mcsimex PASSED [ 77%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_mbias_recommends_mcsimex PASSED [ 80%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_ranking_has_all_methods PASSED [ 82%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_notes_nonempty PASSED [ 85%]\nannot_sensitivity/tests/test_core.py::TestDGP::test_generate_all_topologies PASSED [ 88%]\nannot_sensitivity/tests/test_core.py::TestDGP::test_confounding_has_treatment PASSED [ 91%]\nannot_sensitivity/tests/test_core.py::TestDGP::test_exposure_no_treatment PASSED [ 94%]\nannot_sensitivity/tests/test_core.py::TestDGP::test_iv_has_instrument PASSED [ 97%]\nannot_sensitivity/tests/test_core.py::TestDGP::test_invalid_topology PASSED [100%]\n\n============================== 35 passed in 9.53s ==============================",
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

_source line 37_

35/35 pass. Now let me verify the IV sign-flip behavior with the near-permutation C.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "ac24d22c-eb05-41d9-bfd0-d9cd7eddf32c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LsY7QkV4uZyxBYUM3HfL9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1507,
      "cache_read_input_tokens": 65167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1507
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

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_01APAizZLhvDWGkXAHqjgGsH`</summary>

```json
{
  "command": "python3 -c \"\nfrom annot_sensitivity import compute_bias, compute_asv\nfrom annot_sensitivity.confusion import predefined_matrices\nimport numpy as np\n\n# Test 1: identity -> zero bias\nr = compute_bias('iv', np.eye(3))\nprint(f'Identity: tau_true={r[\\\"tau_true\\\"]:.4f}, tau_biased={r[\\\"tau_biased\\\"]:.4f}, bias={r[\\\"bias\\\"]:.4f}')\n\n# Test 2: near-permutation -> should show sign flip\nC_perm = predefined_matrices()['near_permutation']\nr2 = compute_bias('iv', C_perm)\nprint(f'Near-perm: tau_true={r2[\\\"tau_true\\\"]:.4f}, tau_biased={r2[\\\"tau_biased\\\"]:.4f}, bias={r2[\\\"bias\\\"]:.4f}, bias_pct={r2[\\\"bias_pct\\\"]:.1f}%')\n\n# Test 3: custom near-permutation from task description\nC_custom = np.array([[0.1, 0.8, 0.1], [0.8, 0.1, 0.1], [0.1, 0.1, 0.8]])\nr3 = compute_bias('iv', C_custom)\nprint(f'Custom perm: tau_true={r3[\\\"tau_true\\\"]:.4f}, tau_biased={r3[\\\"tau_biased\\\"]:.4f}, bias={r3[\\\"bias\\\"]:.4f}, bias_pct={r3[\\\"bias_pct\\\"]:.1f}%')\n\n# Test 4: ASV sign_flip\nr4 = compute_asv('iv', predefined_matrices()['symmetric_high'], threshold_type='sign_flip', n_grid=500)\nprint(f'ASV sign_flip (symmetric_high): {r4[\\\"asv\\\"]}')\n\nr5 = compute_asv('iv', C_perm, threshold_type='sign_flip', n_grid=500)\nprint(f'ASV sign_flip (near_perm): {r5[\\\"asv\\\"]}')\n\"\n",
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
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "748cdb8b-32d8-4e2e-b19d-de67409c1bff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LsY7QkV4uZyxBYUM3HfL9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1507,
      "cache_read_input_tokens": 65167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1507
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

_source line 39 · 2026-05-20T23:52:37.878Z_

<details><summary>↩ Tool result · `toolu_01APAizZLhvDWGkXAHqjgGsH`</summary>

```text
Identity: tau_true=1.4114, tau_biased=1.4114, bias=0.0000
Near-perm: tau_true=1.4114, tau_biased=-9.3551, bias=-10.7666, bias_pct=-762.8%
Custom perm: tau_true=1.4114, tau_biased=-11.3598, bias=-12.7712, bias_pct=-904.8%
ASV sign_flip (symmetric_high): 3.336673346693387
ASV sign_flip (near_perm): 0.8691066343212741
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "3c0edae0-43f5-40aa-988a-9aa0f72d78c3",
  "tool_use_result": {
    "stdout": "Identity: tau_true=1.4114, tau_biased=1.4114, bias=0.0000\nNear-perm: tau_true=1.4114, tau_biased=-9.3551, bias=-10.7666, bias_pct=-762.8%\nCustom perm: tau_true=1.4114, tau_biased=-11.3598, bias=-12.7712, bias_pct=-904.8%\nASV sign_flip (symmetric_high): 3.336673346693387\nASV sign_flip (near_perm): 0.8691066343212741",
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

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
The IV Wald estimator is working correctly:
- Identity C → zero bias
- Near-permutation C → massive sign flip (-762.8%, -904.8%)
- ASV sign_flip gives meaningful values

Now let me note the tau_true for IV is 1.4114, not 1.0 (beta[1] = 1.0). This is because the Wald estimator with clean data (C=I) gives RF/FS[1], and since Z is continuous and A is categorical via softmax, the true Wald plim depends on the DGP parameters. 

The Wald estimator's true value is the reduced form effect divided by the first-stage coefficient—essentially the local average treatment effect. With beta[1] = 1.0 in the default setup, the reduced form captures Z's total effect on Y through both treatment categories, while the first-stage only measures how Z influences the first treatment category, which is why they don't align perfectly.

This makes sense—the Wald estimator for categorical treatments behaves differently than individual coefficients. The key validation points are holding up: identity covariance gives zero bias, near-permutation matrices produce massive bias and sign flips, and ASV produces sensible estimates. Now I'm moving on to add the W2 tests.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "0284a515-4fdf-4dc8-9a48-c07b1d79e548",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013m6QQ2Vtb7x2PSLtPv4uxR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 793,
      "cache_read_input_tokens": 66674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 793
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

_source line 41_

IV Wald estimator working correctly: identity gives zero bias, near-permutation gives -762.8% bias (sign flip). ASV returns meaningful values.

Now adding W2 correction method tests.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "68c25abe-d475-47e2-9b7f-d386b1b6304f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013m6QQ2Vtb7x2PSLtPv4uxR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 793,
      "cache_read_input_tokens": 66674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 793
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

_source line 42_

<details open><summary>🔧 Tool call — Edit · `toolu_01FYNvZtC3iDXJvod5KyKhif`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/test_core.py",
  "old_string": "\"\"\"Core tests for the annot_sensitivity package.\"\"\"\n\nimport numpy as np\nimport pytest\nfrom annot_sensitivity import (\n    compute_bias,\n    compute_asv,\n    recommend_correction,\n    validate_confusion_matrix,\n    interpolate_confusion,\n    random_confusion_matrix,\n    predefined_matrices,\n    generate_data,\n    TOPOLOGIES,\n)",
  "new_string": "\"\"\"Core tests for the annot_sensitivity package.\"\"\"\n\nimport numpy as np\nimport pytest\nfrom annot_sensitivity import (\n    compute_bias,\n    compute_asv,\n    recommend_correction,\n    correct_naive_plugin,\n    correct_dsl,\n    correct_ppi,\n    correct_mcsimex,\n    correct_mla,\n    validate_confusion_matrix,\n    interpolate_confusion,\n    random_confusion_matrix,\n    predefined_matrices,\n    generate_data,\n    make_dummies,\n    misclassify,\n    ols_with_se,\n    TOPOLOGIES,\n)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "5bba7d55-2dcc-4cbf-9706-23def644b9b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013m6QQ2Vtb7x2PSLtPv4uxR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 793,
      "cache_read_input_tokens": 66674,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 793
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

_source line 43 · 2026-05-20T23:52:57.607Z_

<details><summary>↩ Tool result · `toolu_01FYNvZtC3iDXJvod5KyKhif`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/test_core.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "482155db-4c4f-4197-b2d2-24e9caf4913e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/test_core.py",
    "oldString": "\"\"\"Core tests for the annot_sensitivity package.\"\"\"\n\nimport numpy as np\nimport pytest\nfrom annot_sensitivity import (\n    compute_bias,\n    compute_asv,\n    recommend_correction,\n    validate_confusion_matrix,\n    interpolate_confusion,\n    random_confusion_matrix,\n    predefined_matrices,\n    generate_data,\n    TOPOLOGIES,\n)",
    "newString": "\"\"\"Core tests for the annot_sensitivity package.\"\"\"\n\nimport numpy as np\nimport pytest\nfrom annot_sensitivity import (\n    compute_bias,\n    compute_asv,\n    recommend_correction,\n    correct_naive_plugin,\n    correct_dsl,\n    correct_ppi,\n    correct_mcsimex,\n    correct_mla,\n    validate_confusion_matrix,\n    interpolate_confusion,\n    random_confusion_matrix,\n    predefined_matrices,\n    generate_data,\n    make_dummies,\n    misclassify,\n    ols_with_se,\n    TOPOLOGIES,\n)",
    "originalFile": "\"\"\"Core tests for the annot_sensitivity package.\"\"\"\n\nimport numpy as np\nimport pytest\nfrom annot_sensitivity import (\n    compute_bias,\n    compute_asv,\n    recommend_correction,\n    validate_confusion_matrix,\n    interpolate_confusion,\n    random_confusion_matrix,\n    predefined_matrices,\n    generate_data,\n    TOPOLOGIES,\n)\n\n\nclass TestValidateConfusionMatrix:\n    def test_identity_valid(self):\n        assert validate_confusion_matrix(np.eye(3)) is True\n\n    def test_predefined_valid(self):\n        for name, C in predefined_matrices().items():\n            assert validate_confusion_matrix(C) is True, f\"{name} failed\"\n\n    def test_non_square(self):\n        assert validate_confusion_matrix(np.ones((2, 3))) is False\n\n    def test_negative_entries(self):\n        C = np.array([[1.1, -0.1], [-0.1, 1.1]])\n        assert validate_confusion_matrix(C) is False\n\n    def test_not_column_stochastic(self):\n        C = np.array([[0.5, 0.5], [0.3, 0.3]])\n        assert validate_confusion_matrix(C) is False\n\n    def test_not_array(self):\n        assert validate_confusion_matrix([[1, 0], [0, 1]]) is False\n\n    def test_1x1(self):\n        assert validate_confusion_matrix(np.array([[1.0]])) is False\n\n    def test_random_valid(self):\n        C = random_confusion_matrix(4, diag_dominance=0.7, rng=np.random.default_rng(42))\n        assert validate_confusion_matrix(C) is True\n        assert C.shape == (4, 4)\n\n\nclass TestInterpolateConfusion:\n    def test_delta_zero_is_identity(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        C = interpolate_confusion(C0, 0.0)\n        np.testing.assert_allclose(C, np.eye(3), atol=1e-12)\n\n    def test_delta_one_is_C0(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        C = interpolate_confusion(C0, 1.0)\n        np.testing.assert_allclose(C, C0, atol=1e-12)\n\n    def test_intermediate_column_stochastic(self):\n        C0 = predefined_matrices()[\"asymmetric\"]\n        C = interpolate_confusion(C0, 0.5)\n        assert validate_confusion_matrix(C)\n\n    def test_small_delta(self):\n        C0 = predefined_matrices()[\"severe_uniform\"]\n        C = interpolate_confusion(C0, 0.01)\n        assert np.allclose(np.diag(C), np.ones(3) * (1 - 0.01) + 0.01 * np.diag(C0),\n                           atol=1e-6)\n\n\nclass TestComputeBias:\n    def test_identity_zero_bias(self):\n        result = compute_bias(\"confounding\", np.eye(3))\n        assert abs(result[\"bias\"]) < 1e-3\n        assert abs(result[\"bias_pct\"]) < 0.1\n\n    def test_confounding_nonzero_bias(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = compute_bias(\"confounding\", C)\n        assert abs(result[\"bias\"]) > 0.01\n        assert result[\"topology\"] == \"confounding\"\n        assert np.isfinite(result[\"tau_true\"])\n        assert np.isfinite(result[\"tau_biased\"])\n\n    def test_all_topologies_run(self):\n        C = predefined_matrices()[\"mild_uniform\"]\n        for topo in TOPOLOGIES:\n            result = compute_bias(topo, C)\n            assert result[\"topology\"] == topo\n            assert np.isfinite(result[\"tau_true\"])\n            assert np.isfinite(result[\"tau_biased\"])\n\n    def test_invalid_topology(self):\n        with pytest.raises(ValueError, match=\"Unknown topology\"):\n            compute_bias(\"nonexistent\", np.eye(3))\n\n    def test_invalid_C(self):\n        with pytest.raises(ValueError, match=\"column-stochastic\"):\n            compute_bias(\"confounding\", np.ones((3, 3)))\n\n    def test_worse_C_more_bias(self):\n        C_mild = predefined_matrices()[\"mild_uniform\"]\n        C_severe = predefined_matrices()[\"severe_uniform\"]\n        r_mild = compute_bias(\"confounding\", C_mild)\n        r_severe = compute_bias(\"confounding\", C_severe)\n        assert abs(r_severe[\"bias\"]) > abs(r_mild[\"bias\"])\n\n\nclass TestComputeASV:\n    def test_returns_valid_structure(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        result = compute_asv(\"confounding\", C0, n_grid=200)\n        assert \"asv\" in result\n        assert \"bias_curve\" in result\n        assert \"envelope\" in result\n        assert \"deltas\" in result\n        assert \"tau_true\" in result\n        assert len(result[\"deltas\"]) == 200\n        assert len(result[\"bias_curve\"]) == 200\n        assert len(result[\"envelope\"]) == 200\n\n    def test_asv_is_positive_or_none(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        result = compute_asv(\"confounding\", C0, threshold_type=\"magnitude\",\n                             threshold_value=0.1, n_grid=200)\n        if result[\"asv\"] is not None:\n            assert result[\"asv\"] > 0\n\n    def test_envelope_monotone(self):\n        C0 = predefined_matrices()[\"asymmetric\"]\n        result = compute_asv(\"mediation\", C0, n_grid=200)\n        diffs = np.diff(result[\"envelope\"])\n        assert np.all(diffs >= -1e-12)\n\n    def test_sign_flip_threshold(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        result = compute_asv(\"confounding\", C0, threshold_type=\"sign_flip\",\n                             n_grid=200)\n        assert \"asv\" in result\n\n    def test_invalid_threshold_type(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        with pytest.raises(ValueError, match=\"Unknown threshold_type\"):\n            compute_asv(\"confounding\", C0, threshold_type=\"invalid\", n_grid=50)\n\n\nclass TestRecommendCorrection:\n    def test_with_gold_recommends_ppi(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"confounding\", C, has_gold=True)\n        assert result[\"recommended\"] == \"ppi\"\n\n    def test_without_gold_confounding_recommends_dsl(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"confounding\", C, has_gold=False)\n        assert result[\"recommended\"] == \"dsl\"\n\n    def test_without_gold_mediation_recommends_dsl(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"mediation\", C, has_gold=False)\n        assert result[\"recommended\"] == \"dsl\"\n\n    def test_without_gold_collider_recommends_mcsimex(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"collider\", C, has_gold=False)\n        assert result[\"recommended\"] == \"mcsimex\"\n\n    def test_without_gold_mbias_recommends_mcsimex(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"mbias\", C, has_gold=False)\n        assert result[\"recommended\"] == \"mcsimex\"\n\n    def test_ranking_has_all_methods(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"confounding\", C, has_gold=True)\n        methods = {m[\"method\"] for m in result[\"ranking\"]}\n        assert methods == {\"ppi\", \"dsl\", \"mcsimex\", \"naive_plugin\", \"mla\"}\n\n    def test_notes_nonempty(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"collider\", C, has_gold=False)\n        assert len(result[\"notes\"]) > 0\n\n\nclass TestDGP:\n    def test_generate_all_topologies(self):\n        for topo in TOPOLOGIES:\n            data = generate_data(topo, 100, seed=42)\n            assert \"Y\" in data\n            assert \"A\" in data\n            assert len(data[\"Y\"]) == 100\n\n    def test_confounding_has_treatment(self):\n        data = generate_data(\"confounding\", 100, seed=42)\n        assert \"T\" in data\n\n    def test_exposure_no_treatment(self):\n        data = generate_data(\"exposure\", 100, seed=42)\n        assert \"T\" not in data\n\n    def test_iv_has_instrument(self):\n        data = generate_data(\"iv\", 100, seed=42)\n        assert \"Z\" in data\n\n    def test_invalid_topology(self):\n        with pytest.raises(ValueError):\n            generate_data(\"invalid\", 100)\n\n\nif __name__ == \"__main__\":\n    pytest.main([__file__, \"-v\"])\n",
    "structuredPatch": [
      {
        "oldStart": 6,
        "oldLines": 11,
        "newStart": 6,
        "newLines": 19,
        "lines": [
          "     compute_bias,",
          "     compute_asv,",
          "     recommend_correction,",
          "+    correct_naive_plugin,",
          "+    correct_dsl,",
          "+    correct_ppi,",
          "+    correct_mcsimex,",
          "+    correct_mla,",
          "     validate_confusion_matrix,",
          "     interpolate_confusion,",
          "     random_confusion_matrix,",
          "     predefined_matrices,",
          "     generate_data,",
          "+    make_dummies,",
          "+    misclassify,",
          "+    ols_with_se,",
          "     TOPOLOGIES,",
          " )",
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

_source line 44_

<details open><summary>🔧 Tool call — Edit · `toolu_01HBDpdmP7rzpF4D9Y24LDmg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/test_core.py",
  "old_string": "if __name__ == \"__main__\":\n    pytest.main([__file__, \"-v\"])",
  "new_string": "class TestIVWald:\n    \"\"\"Tests for IV Wald estimator (W1 fix).\"\"\"\n\n    def test_identity_zero_bias(self):\n        result = compute_bias(\"iv\", np.eye(3))\n        assert abs(result[\"bias\"]) < 1e-3\n\n    def test_near_permutation_sign_flip(self):\n        C = predefined_matrices()[\"near_permutation\"]\n        result = compute_bias(\"iv\", C)\n        assert np.sign(result[\"tau_biased\"]) != np.sign(result[\"tau_true\"])\n\n    def test_asv_sign_flip_finite(self):\n        C0 = predefined_matrices()[\"near_permutation\"]\n        result = compute_asv(\"iv\", C0, threshold_type=\"sign_flip\", n_grid=300)\n        assert result[\"asv\"] is not None\n        assert result[\"asv\"] > 0\n\n    def test_symmetric_high_moderate_bias(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = compute_bias(\"iv\", C)\n        assert abs(result[\"bias\"]) > 0.01\n\n\ndef _make_confounding_data(N, K, C, rng, gold_frac=0.1):\n    \"\"\"Helper: generate confounding data, misclassify, return test inputs.\"\"\"\n    data = generate_data(\"confounding\", N, seed=int(rng.integers(0, 2**31)))\n    T, Y, A = data[\"T\"], data[\"Y\"], data[\"A\"]\n    Astar = misclassify(A, C, rng)\n    X_other = np.column_stack([np.ones(N), T])\n    gold_mask = np.zeros(N, dtype=bool)\n    gold_mask[: int(gold_frac * N)] = True\n    return X_other, Y, A, Astar, gold_mask\n\n\nclass TestCorrectionMethods:\n    \"\"\"Smoke tests + property tests for 5 correction methods.\"\"\"\n\n    @pytest.fixture\n    def confounding_data(self):\n        rng = np.random.default_rng(42)\n        K = 3\n        C = predefined_matrices(K)[\"symmetric_high\"]\n        X_other, Y, A, Astar, gold_mask = _make_confounding_data(\n            2000, K, C, rng\n        )\n        return dict(\n            X_other=X_other, Y=Y, A=A, Astar=Astar,\n            gold_mask=gold_mask, C=C, K=K, rng=rng,\n        )\n\n    def test_naive_plugin_smoke(self, confounding_data):\n        d = confounding_data\n        tau, se, ok = correct_naive_plugin(d[\"X_other\"], d[\"Y\"], d[\"Astar\"],\n                                           d[\"C\"], tau_idx=1)\n        assert ok is True\n        assert np.isfinite(tau)\n        assert np.isfinite(se)\n\n    def test_dsl_smoke(self, confounding_data):\n        d = confounding_data\n        tau, se, ok = correct_dsl(d[\"X_other\"], d[\"Y\"], d[\"Astar\"],\n                                  d[\"A\"], d[\"gold_mask\"], tau_idx=1)\n        assert ok is True\n        assert np.isfinite(tau)\n        assert np.isfinite(se)\n\n    def test_ppi_smoke(self, confounding_data):\n        d = confounding_data\n        tau, se, ok = correct_ppi(d[\"X_other\"], d[\"Y\"], d[\"Astar\"],\n                                  d[\"A\"], d[\"gold_mask\"], tau_idx=1,\n                                  rng=d[\"rng\"])\n        assert ok is True\n        assert np.isfinite(tau)\n        assert np.isfinite(se)\n\n    def test_mcsimex_smoke(self, confounding_data):\n        d = confounding_data\n        tau, se, ok = correct_mcsimex(d[\"X_other\"], d[\"Y\"], d[\"Astar\"],\n                                      d[\"C\"], tau_idx=1, rng=d[\"rng\"])\n        assert ok is True\n        assert np.isfinite(tau)\n\n    def test_mla_smoke(self, confounding_data):\n        d = confounding_data\n        tau, se, ok = correct_mla(d[\"X_other\"], d[\"Y\"], d[\"Astar\"],\n                                  d[\"C\"], tau_idx=1)\n        assert ok is True\n        assert np.isfinite(tau)\n        assert np.isfinite(se)\n\n    def test_ppi_bias_reduction(self):\n        rng = np.random.default_rng(123)\n        K = 3\n        C = predefined_matrices(K)[\"symmetric_high\"]\n        n_reps = 20\n        N = 5000\n        uncorrected = np.zeros(n_reps)\n        corrected = np.zeros(n_reps)\n        tau_true_vals = np.zeros(n_reps)\n\n        for r in range(n_reps):\n            data = generate_data(\"confounding\", N,\n                                 seed=int(rng.integers(0, 2**31)))\n            T, Y, A = data[\"T\"], data[\"Y\"], data[\"A\"]\n            Astar = misclassify(A, C, rng)\n            X_other = np.column_stack([np.ones(N), T])\n            D_star = make_dummies(Astar, K)\n            X_unc = np.column_stack([X_other, D_star])\n            beta_unc, _ = ols_with_se(X_unc, Y)\n            D_true = make_dummies(A, K)\n            X_true = np.column_stack([X_other, D_true])\n            beta_true, _ = ols_with_se(X_true, Y)\n            tau_true_vals[r] = beta_true[1]\n            uncorrected[r] = beta_unc[1]\n\n            gold_mask = np.zeros(N, dtype=bool)\n            gold_mask[: int(0.1 * N)] = True\n            tau_ppi, _, _ = correct_ppi(X_other, Y, Astar, A, gold_mask,\n                                        tau_idx=1, rng=rng)\n            corrected[r] = tau_ppi\n\n        tau_true_mean = tau_true_vals.mean()\n        bias_unc = abs(uncorrected.mean() - tau_true_mean)\n        bias_ppi = abs(corrected.mean() - tau_true_mean)\n        assert bias_ppi < 0.5 * bias_unc, (\n            f\"PPI bias {bias_ppi:.4f} not < 50% of uncorrected {bias_unc:.4f}\"\n        )\n\n    def test_dsl_catastrophic_on_mbias(self):\n        rng = np.random.default_rng(77)\n        K = 3\n        C = predefined_matrices(K)[\"symmetric_high\"]\n        N = 3000\n        data = generate_data(\"mbias\", N, seed=77)\n        T, Y, A = data[\"T\"], data[\"Y\"], data[\"A\"]\n        Astar = misclassify(A, C, rng)\n        X_other = np.column_stack([np.ones(N), T])\n        gold_mask = np.zeros(N, dtype=bool)\n        gold_mask[:int(0.1 * N)] = True\n\n        D_star = make_dummies(Astar, K)\n        X_unc = np.column_stack([X_other, D_star])\n        beta_unc, _ = ols_with_se(X_unc, Y)\n\n        D_true = make_dummies(A, K)\n        X_true = np.column_stack([X_other, D_true])\n        beta_true, _ = ols_with_se(X_true, Y)\n        tau_true = beta_true[1]\n\n        tau_dsl, _, ok = correct_dsl(X_other, Y, Astar, A, gold_mask,\n                                     tau_idx=1)\n        bias_unc = abs(beta_unc[1] - tau_true)\n        bias_dsl = abs(tau_dsl - tau_true)\n        assert bias_dsl > bias_unc * 0.8, (\n            f\"DSL bias {bias_dsl:.4f} not worse than uncorrected {bias_unc:.4f}\"\n        )\n\n    def test_end_to_end_pipeline(self):\n        rng = np.random.default_rng(99)\n        K = 3\n        C = predefined_matrices(K)[\"symmetric_high\"]\n        N = 2000\n        data = generate_data(\"confounding\", N, seed=99)\n        T, Y, A = data[\"T\"], data[\"Y\"], data[\"A\"]\n\n        r_bias = compute_bias(\"confounding\", C)\n        assert abs(r_bias[\"bias\"]) > 0.01\n\n        Astar = misclassify(A, C, rng)\n        X_other = np.column_stack([np.ones(N), T])\n        gold_mask = np.zeros(N, dtype=bool)\n        gold_mask[:int(0.1 * N)] = True\n\n        tau_ppi, se_ppi, ok = correct_ppi(X_other, Y, Astar, A, gold_mask,\n                                          tau_idx=1, rng=rng)\n        assert ok is True\n        assert np.isfinite(tau_ppi)\n\n\nif __name__ == \"__main__\":\n    pytest.main([__file__, \"-v\"])"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "c7a8b168-4ddf-4222-b2ba-87ee3e956ec8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KXdj9c57zvCoM8qf7jKvFJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 921,
      "cache_read_input_tokens": 67467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 921
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

_source line 45 · 2026-05-20T23:53:29.862Z_

<details><summary>↩ Tool result · `toolu_01HBDpdmP7rzpF4D9Y24LDmg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/test_core.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "a8908ff3-f71a-4907-b400-3560e6bcfb27",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/test_core.py",
    "oldString": "if __name__ == \"__main__\":\n    pytest.main([__file__, \"-v\"])",
    "newString": "class TestIVWald:\n    \"\"\"Tests for IV Wald estimator (W1 fix).\"\"\"\n\n    def test_identity_zero_bias(self):\n        result = compute_bias(\"iv\", np.eye(3))\n        assert abs(result[\"bias\"]) < 1e-3\n\n    def test_near_permutation_sign_flip(self):\n        C = predefined_matrices()[\"near_permutation\"]\n        result = compute_bias(\"iv\", C)\n        assert np.sign(result[\"tau_biased\"]) != np.sign(result[\"tau_true\"])\n\n    def test_asv_sign_flip_finite(self):\n        C0 = predefined_matrices()[\"near_permutation\"]\n        result = compute_asv(\"iv\", C0, threshold_type=\"sign_flip\", n_grid=300)\n        assert result[\"asv\"] is not None\n        assert result[\"asv\"] > 0\n\n    def test_symmetric_high_moderate_bias(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = compute_bias(\"iv\", C)\n        assert abs(result[\"bias\"]) > 0.01\n\n\ndef _make_confounding_data(N, K, C, rng, gold_frac=0.1):\n    \"\"\"Helper: generate confounding data, misclassify, return test inputs.\"\"\"\n    data = generate_data(\"confounding\", N, seed=int(rng.integers(0, 2**31)))\n    T, Y, A = data[\"T\"], data[\"Y\"], data[\"A\"]\n    Astar = misclassify(A, C, rng)\n    X_other = np.column_stack([np.ones(N), T])\n    gold_mask = np.zeros(N, dtype=bool)\n    gold_mask[: int(gold_frac * N)] = True\n    return X_other, Y, A, Astar, gold_mask\n\n\nclass TestCorrectionMethods:\n    \"\"\"Smoke tests + property tests for 5 correction methods.\"\"\"\n\n    @pytest.fixture\n    def confounding_data(self):\n        rng = np.random.default_rng(42)\n        K = 3\n        C = predefined_matrices(K)[\"symmetric_high\"]\n        X_other, Y, A, Astar, gold_mask = _make_confounding_data(\n            2000, K, C, rng\n        )\n        return dict(\n            X_other=X_other, Y=Y, A=A, Astar=Astar,\n            gold_mask=gold_mask, C=C, K=K, rng=rng,\n        )\n\n    def test_naive_plugin_smoke(self, confounding_data):\n        d = confounding_data\n        tau, se, ok = correct_naive_plugin(d[\"X_other\"], d[\"Y\"], d[\"Astar\"],\n                                           d[\"C\"], tau_idx=1)\n        assert ok is True\n        assert np.isfinite(tau)\n        assert np.isfinite(se)\n\n    def test_dsl_smoke(self, confounding_data):\n        d = confounding_data\n        tau, se, ok = correct_dsl(d[\"X_other\"], d[\"Y\"], d[\"Astar\"],\n                                  d[\"A\"], d[\"gold_mask\"], tau_idx=1)\n        assert ok is True\n        assert np.isfinite(tau)\n        assert np.isfinite(se)\n\n    def test_ppi_smoke(self, confounding_data):\n        d = confounding_data\n        tau, se, ok = correct_ppi(d[\"X_other\"], d[\"Y\"], d[\"Astar\"],\n                                  d[\"A\"], d[\"gold_mask\"], tau_idx=1,\n                                  rng=d[\"rng\"])\n        assert ok is True\n        assert np.isfinite(tau)\n        assert np.isfinite(se)\n\n    def test_mcsimex_smoke(self, confounding_data):\n        d = confounding_data\n        tau, se, ok = correct_mcsimex(d[\"X_other\"], d[\"Y\"], d[\"Astar\"],\n                                      d[\"C\"], tau_idx=1, rng=d[\"rng\"])\n        assert ok is True\n        assert np.isfinite(tau)\n\n    def test_mla_smoke(self, confounding_data):\n        d = confounding_data\n        tau, se, ok = correct_mla(d[\"X_other\"], d[\"Y\"], d[\"Astar\"],\n                                  d[\"C\"], tau_idx=1)\n        assert ok is True\n        assert np.isfinite(tau)\n        assert np.isfinite(se)\n\n    def test_ppi_bias_reduction(self):\n        rng = np.random.default_rng(123)\n        K = 3\n        C = predefined_matrices(K)[\"symmetric_high\"]\n        n_reps = 20\n        N = 5000\n        uncorrected = np.zeros(n_reps)\n        corrected = np.zeros(n_reps)\n        tau_true_vals = np.zeros(n_reps)\n\n        for r in range(n_reps):\n            data = generate_data(\"confounding\", N,\n                                 seed=int(rng.integers(0, 2**31)))\n            T, Y, A = data[\"T\"], data[\"Y\"], data[\"A\"]\n            Astar = misclassify(A, C, rng)\n            X_other = np.column_stack([np.ones(N), T])\n            D_star = make_dummies(Astar, K)\n            X_unc = np.column_stack([X_other, D_star])\n            beta_unc, _ = ols_with_se(X_unc, Y)\n            D_true = make_dummies(A, K)\n            X_true = np.column_stack([X_other, D_true])\n            beta_true, _ = ols_with_se(X_true, Y)\n            tau_true_vals[r] = beta_true[1]\n            uncorrected[r] = beta_unc[1]\n\n            gold_mask = np.zeros(N, dtype=bool)\n            gold_mask[: int(0.1 * N)] = True\n            tau_ppi, _, _ = correct_ppi(X_other, Y, Astar, A, gold_mask,\n                                        tau_idx=1, rng=rng)\n            corrected[r] = tau_ppi\n\n        tau_true_mean = tau_true_vals.mean()\n        bias_unc = abs(uncorrected.mean() - tau_true_mean)\n        bias_ppi = abs(corrected.mean() - tau_true_mean)\n        assert bias_ppi < 0.5 * bias_unc, (\n            f\"PPI bias {bias_ppi:.4f} not < 50% of uncorrected {bias_unc:.4f}\"\n        )\n\n    def test_dsl_catastrophic_on_mbias(self):\n        rng = np.random.default_rng(77)\n        K = 3\n        C = predefined_matrices(K)[\"symmetric_high\"]\n        N = 3000\n        data = generate_data(\"mbias\", N, seed=77)\n        T, Y, A = data[\"T\"], data[\"Y\"], data[\"A\"]\n        Astar = misclassify(A, C, rng)\n        X_other = np.column_stack([np.ones(N), T])\n        gold_mask = np.zeros(N, dtype=bool)\n        gold_mask[:int(0.1 * N)] = True\n\n        D_star = make_dummies(Astar, K)\n        X_unc = np.column_stack([X_other, D_star])\n        beta_unc, _ = ols_with_se(X_unc, Y)\n\n        D_true = make_dummies(A, K)\n        X_true = np.column_stack([X_other, D_true])\n        beta_true, _ = ols_with_se(X_true, Y)\n        tau_true = beta_true[1]\n\n        tau_dsl, _, ok = correct_dsl(X_other, Y, Astar, A, gold_mask,\n                                     tau_idx=1)\n        bias_unc = abs(beta_unc[1] - tau_true)\n        bias_dsl = abs(tau_dsl - tau_true)\n        assert bias_dsl > bias_unc * 0.8, (\n            f\"DSL bias {bias_dsl:.4f} not worse than uncorrected {bias_unc:.4f}\"\n        )\n\n    def test_end_to_end_pipeline(self):\n        rng = np.random.default_rng(99)\n        K = 3\n        C = predefined_matrices(K)[\"symmetric_high\"]\n        N = 2000\n        data = generate_data(\"confounding\", N, seed=99)\n        T, Y, A = data[\"T\"], data[\"Y\"], data[\"A\"]\n\n        r_bias = compute_bias(\"confounding\", C)\n        assert abs(r_bias[\"bias\"]) > 0.01\n\n        Astar = misclassify(A, C, rng)\n        X_other = np.column_stack([np.ones(N), T])\n        gold_mask = np.zeros(N, dtype=bool)\n        gold_mask[:int(0.1 * N)] = True\n\n        tau_ppi, se_ppi, ok = correct_ppi(X_other, Y, Astar, A, gold_mask,\n                                          tau_idx=1, rng=rng)\n        assert ok is True\n        assert np.isfinite(tau_ppi)\n\n\nif __name__ == \"__main__\":\n    pytest.main([__file__, \"-v\"])",
    "originalFile": "\"\"\"Core tests for the annot_sensitivity package.\"\"\"\n\nimport numpy as np\nimport pytest\nfrom annot_sensitivity import (\n    compute_bias,\n    compute_asv,\n    recommend_correction,\n    correct_naive_plugin,\n    correct_dsl,\n    correct_ppi,\n    correct_mcsimex,\n    correct_mla,\n    validate_confusion_matrix,\n    interpolate_confusion,\n    random_confusion_matrix,\n    predefined_matrices,\n    generate_data,\n    make_dummies,\n    misclassify,\n    ols_with_se,\n    TOPOLOGIES,\n)\n\n\nclass TestValidateConfusionMatrix:\n    def test_identity_valid(self):\n        assert validate_confusion_matrix(np.eye(3)) is True\n\n    def test_predefined_valid(self):\n        for name, C in predefined_matrices().items():\n            assert validate_confusion_matrix(C) is True, f\"{name} failed\"\n\n    def test_non_square(self):\n        assert validate_confusion_matrix(np.ones((2, 3))) is False\n\n    def test_negative_entries(self):\n        C = np.array([[1.1, -0.1], [-0.1, 1.1]])\n        assert validate_confusion_matrix(C) is False\n\n    def test_not_column_stochastic(self):\n        C = np.array([[0.5, 0.5], [0.3, 0.3]])\n        assert validate_confusion_matrix(C) is False\n\n    def test_not_array(self):\n        assert validate_confusion_matrix([[1, 0], [0, 1]]) is False\n\n    def test_1x1(self):\n        assert validate_confusion_matrix(np.array([[1.0]])) is False\n\n    def test_random_valid(self):\n        C = random_confusion_matrix(4, diag_dominance=0.7, rng=np.random.default_rng(42))\n        assert validate_confusion_matrix(C) is True\n        assert C.shape == (4, 4)\n\n\nclass TestInterpolateConfusion:\n    def test_delta_zero_is_identity(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        C = interpolate_confusion(C0, 0.0)\n        np.testing.assert_allclose(C, np.eye(3), atol=1e-12)\n\n    def test_delta_one_is_C0(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        C = interpolate_confusion(C0, 1.0)\n        np.testing.assert_allclose(C, C0, atol=1e-12)\n\n    def test_intermediate_column_stochastic(self):\n        C0 = predefined_matrices()[\"asymmetric\"]\n        C = interpolate_confusion(C0, 0.5)\n        assert validate_confusion_matrix(C)\n\n    def test_small_delta(self):\n        C0 = predefined_matrices()[\"severe_uniform\"]\n        C = interpolate_confusion(C0, 0.01)\n        assert np.allclose(np.diag(C), np.ones(3) * (1 - 0.01) + 0.01 * np.diag(C0),\n                           atol=1e-6)\n\n\nclass TestComputeBias:\n    def test_identity_zero_bias(self):\n        result = compute_bias(\"confounding\", np.eye(3))\n        assert abs(result[\"bias\"]) < 1e-3\n        assert abs(result[\"bias_pct\"]) < 0.1\n\n    def test_confounding_nonzero_bias(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = compute_bias(\"confounding\", C)\n        assert abs(result[\"bias\"]) > 0.01\n        assert result[\"topology\"] == \"confounding\"\n        assert np.isfinite(result[\"tau_true\"])\n        assert np.isfinite(result[\"tau_biased\"])\n\n    def test_all_topologies_run(self):\n        C = predefined_matrices()[\"mild_uniform\"]\n        for topo in TOPOLOGIES:\n            result = compute_bias(topo, C)\n            assert result[\"topology\"] == topo\n            assert np.isfinite(result[\"tau_true\"])\n            assert np.isfinite(result[\"tau_biased\"])\n\n    def test_invalid_topology(self):\n        with pytest.raises(ValueError, match=\"Unknown topology\"):\n            compute_bias(\"nonexistent\", np.eye(3))\n\n    def test_invalid_C(self):\n        with pytest.raises(ValueError, match=\"column-stochastic\"):\n            compute_bias(\"confounding\", np.ones((3, 3)))\n\n    def test_worse_C_more_bias(self):\n        C_mild = predefined_matrices()[\"mild_uniform\"]\n        C_severe = predefined_matrices()[\"severe_uniform\"]\n        r_mild = compute_bias(\"confounding\", C_mild)\n        r_severe = compute_bias(\"confounding\", C_severe)\n        assert abs(r_severe[\"bias\"]) > abs(r_mild[\"bias\"])\n\n\nclass TestComputeASV:\n    def test_returns_valid_structure(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        result = compute_asv(\"confounding\", C0, n_grid=200)\n        assert \"asv\" in result\n        assert \"bias_curve\" in result\n        assert \"envelope\" in result\n        assert \"deltas\" in result\n        assert \"tau_true\" in result\n        assert len(result[\"deltas\"]) == 200\n        assert len(result[\"bias_curve\"]) == 200\n        assert len(result[\"envelope\"]) == 200\n\n    def test_asv_is_positive_or_none(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        result = compute_asv(\"confounding\", C0, threshold_type=\"magnitude\",\n                             threshold_value=0.1, n_grid=200)\n        if result[\"asv\"] is not None:\n            assert result[\"asv\"] > 0\n\n    def test_envelope_monotone(self):\n        C0 = predefined_matrices()[\"asymmetric\"]\n        result = compute_asv(\"mediation\", C0, n_grid=200)\n        diffs = np.diff(result[\"envelope\"])\n        assert np.all(diffs >= -1e-12)\n\n    def test_sign_flip_threshold(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        result = compute_asv(\"confounding\", C0, threshold_type=\"sign_flip\",\n                             n_grid=200)\n        assert \"asv\" in result\n\n    def test_invalid_threshold_type(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        with pytest.raises(ValueError, match=\"Unknown threshold_type\"):\n            compute_asv(\"confounding\", C0, threshold_type=\"invalid\", n_grid=50)\n\n\nclass TestRecommendCorrection:\n    def test_with_gold_recommends_ppi(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"confounding\", C, has_gold=True)\n        assert result[\"recommended\"] == \"ppi\"\n\n    def test_without_gold_confounding_recommends_dsl(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"confounding\", C, has_gold=False)\n        assert result[\"recommended\"] == \"dsl\"\n\n    def test_without_gold_mediation_recommends_dsl(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"mediation\", C, has_gold=False)\n        assert result[\"recommended\"] == \"dsl\"\n\n    def test_without_gold_collider_recommends_mcsimex(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"collider\", C, has_gold=False)\n        assert result[\"recommended\"] == \"mcsimex\"\n\n    def test_without_gold_mbias_recommends_mcsimex(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"mbias\", C, has_gold=False)\n        assert result[\"recommended\"] == \"mcsimex\"\n\n    def test_ranking_has_all_methods(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"confounding\", C, has_gold=True)\n        methods = {m[\"method\"] for m in result[\"ranking\"]}\n        assert methods == {\"ppi\", \"dsl\", \"mcsimex\", \"naive_plugin\", \"mla\"}\n\n    def test_notes_nonempty(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"collider\", C, has_gold=False)\n        assert len(result[\"notes\"]) > 0\n\n\nclass TestDGP:\n    def test_generate_all_topologies(self):\n        for topo in TOPOLOGIES:\n            data = generate_data(topo, 100, seed=42)\n            assert \"Y\" in data\n            assert \"A\" in data\n            assert len(data[\"Y\"]) == 100\n\n    def test_confounding_has_treatment(self):\n        data = generate_data(\"confounding\", 100, seed=42)\n        assert \"T\" in data\n\n    def test_exposure_no_treatment(self):\n        data = generate_data(\"exposure\", 100, seed=42)\n        assert \"T\" not in data\n\n    def test_iv_has_instrument(self):\n        data = generate_data(\"iv\", 100, seed=42)\n        assert \"Z\" in data\n\n    def test_invalid_topology(self):\n        with pytest.raises(ValueError):\n            generate_data(\"invalid\", 100)\n\n\nif __name__ == \"__main__\":\n    pytest.main([__file__, \"-v\"])\n",
    "structuredPatch": [
      {
        "oldStart": 216,
        "oldLines": 5,
        "newStart": 216,
        "newLines": 185,
        "lines": [
          "             generate_data(\"invalid\", 100)",
          " ",
          " ",
          "+class TestIVWald:",
          "+    \"\"\"Tests for IV Wald estimator (W1 fix).\"\"\"",
          "+",
          "+    def test_identity_zero_bias(self):",
          "+        result = compute_bias(\"iv\", np.eye(3))",
          "+        assert abs(result[\"bias\"]) < 1e-3",
          "+",
          "+    def test_near_permutation_sign_flip(self):",
          "+        C = predefined_matrices()[\"near_permutation\"]",
          "+        result = compute_bias(\"iv\", C)",
          "+        assert np.sign(result[\"tau_biased\"]) != np.sign(result[\"tau_true\"])",
          "+",
          "+    def test_asv_sign_flip_finite(self):",
          "+        C0 = predefined_matrices()[\"near_permutation\"]",
          "+        result = compute_asv(\"iv\", C0, threshold_type=\"sign_flip\", n_grid=300)",
          "+        assert result[\"asv\"] is not None",
          "+        assert result[\"asv\"] > 0",
          "+",
          "+    def test_symmetric_high_moderate_bias(self):",
          "+        C = predefined_matrices()[\"symmetric_high\"]",
          "+        result = compute_bias(\"iv\", C)",
          "+        assert abs(result[\"bias\"]) > 0.01",
          "+",
          "+",
          "+def _make_confounding_data(N, K, C, rng, gold_frac=0.1):",
          "+    \"\"\"Helper: generate confounding data, misclassify, return test inputs.\"\"\"",
          "+    data = generate_data(\"confounding\", N, seed=int(rng.integers(0, 2**31)))",
          "+    T, Y, A = data[\"T\"], data[\"Y\"], data[\"A\"]",
          "+    Astar = misclassify(A, C, rng)",
          "+    X_other = np.column_stack([np.ones(N), T])",
          "+    gold_mask = np.zeros(N, dtype=bool)",
          "+    gold_mask[: int(gold_frac * N)] = True",
          "+    return X_other, Y, A, Astar, gold_mask",
          "+",
          "+",
          "+class TestCorrectionMethods:",
          "+    \"\"\"Smoke tests + property tests for 5 correction methods.\"\"\"",
          "+",
          "+    @pytest.fixture",
          "+    def confounding_data(self):",
          "+        rng = np.random.default_rng(42)",
          "+        K = 3",
          "+        C = predefined_matrices(K)[\"symmetric_high\"]",
          "+        X_other, Y, A, Astar, gold_mask = _make_confounding_data(",
          "+            2000, K, C, rng",
          "+        )",
          "+        return dict(",
          "+            X_other=X_other, Y=Y, A=A, Astar=Astar,",
          "+            gold_mask=gold_mask, C=C, K=K, rng=rng,",
          "+        )",
          "+",
          "+    def test_naive_plugin_smoke(self, confounding_data):",
          "+        d = confounding_data",
          "+        tau, se, ok = correct_naive_plugin(d[\"X_other\"], d[\"Y\"], d[\"Astar\"],",
          "+                                           d[\"C\"], tau_idx=1)",
          "+        assert ok is True",
          "+        assert np.isfinite(tau)",
          "+        assert np.isfinite(se)",
          "+",
          "+    def test_dsl_smoke(self, confounding_data):",
          "+        d = confounding_data",
          "+        tau, se, ok = correct_dsl(d[\"X_other\"], d[\"Y\"], d[\"Astar\"],",
          "+                                  d[\"A\"], d[\"gold_mask\"], tau_idx=1)",
          "+        assert ok is True",
          "+        assert np.isfinite(tau)",
          "+        assert np.isfinite(se)",
          "+",
          "+    def test_ppi_smoke(self, confounding_data):",
          "+        d = confounding_data",
          "+        tau, se, ok = correct_ppi(d[\"X_other\"], d[\"Y\"], d[\"Astar\"],",
          "+                                  d[\"A\"], d[\"gold_mask\"], tau_idx=1,",
          "+                                  rng=d[\"rng\"])",
          "+        assert ok is True",
          "+        assert np.isfinite(tau)",
          "+        assert np.isfinite(se)",
          "+",
          "+    def test_mcsimex_smoke(self, confounding_data):",
          "+        d = confounding_data",
          "+        tau, se, ok = correct_mcsimex(d[\"X_other\"], d[\"Y\"], d[\"Astar\"],",
          "+                                      d[\"C\"], tau_idx=1, rng=d[\"rng\"])",
          "+        assert ok is True",
          "+        assert np.isfinite(tau)",
          "+",
          "+    def test_mla_smoke(self, confounding_data):",
          "+        d = confounding_data",
          "+        tau, se, ok = correct_mla(d[\"X_other\"], d[\"Y\"], d[\"Astar\"],",
          "+                                  d[\"C\"], tau_idx=1)",
          "+        assert ok is True",
          "+        assert np.isfinite(tau)",
          "+        assert np.isfinite(se)",
          "+",
          "+    def test_ppi_bias_reduction(self):",
          "+        rng = np.random.default_rng(123)",
          "+        K = 3",
          "+        C = predefined_matrices(K)[\"symmetric_high\"]",
          "+        n_reps = 20",
          "+        N = 5000",
          "+        uncorrected = np.zeros(n_reps)",
          "+        corrected = np.zeros(n_reps)",
          "+        tau_true_vals = np.zeros(n_reps)",
          "+",
          "+        for r in range(n_reps):",
          "+            data = generate_data(\"confounding\", N,",
          "+                                 seed=int(rng.integers(0, 2**31)))",
          "+            T, Y, A = data[\"T\"], data[\"Y\"], data[\"A\"]",
          "+            Astar = misclassify(A, C, rng)",
          "+            X_other = np.column_stack([np.ones(N), T])",
          "+            D_star = make_dummies(Astar, K)",
          "+            X_unc = np.column_stack([X_other, D_star])",
          "+            beta_unc, _ = ols_with_se(X_unc, Y)",
          "+            D_true = make_dummies(A, K)",
          "+            X_true = np.column_stack([X_other, D_true])",
          "+            beta_true, _ = ols_with_se(X_true, Y)",
          "+            tau_true_vals[r] = beta_true[1]",
          "+            uncorrected[r] = beta_unc[1]",
          "+",
          "+            gold_mask = np.zeros(N, dtype=bool)",
          "+            gold_mask[: int(0.1 * N)] = True",
          "+            tau_ppi, _, _ = correct_ppi(X_other, Y, Astar, A, gold_mask,",
          "+                                        tau_idx=1, rng=rng)",
          "+            corrected[r] = tau_ppi",
          "+",
          "+        tau_true_mean = tau_true_vals.mean()",
          "+        bias_unc = abs(uncorrected.mean() - tau_true_mean)",
          "+        bias_ppi = abs(corrected.mean() - tau_true_mean)",
          "+        assert bias_ppi < 0.5 * bias_unc, (",
          "+            f\"PPI bias {bias_ppi:.4f} not < 50% of uncorrected {bias_unc:.4f}\"",
          "+        )",
          "+",
          "+    def test_dsl_catastrophic_on_mbias(self):",
          "+        rng = np.random.default_rng(77)",
          "+        K = 3",
          "+        C = predefined_matrices(K)[\"symmetric_high\"]",
          "+        N = 3000",
          "+        data = generate_data(\"mbias\", N, seed=77)",
          "+        T, Y, A = data[\"T\"], data[\"Y\"], data[\"A\"]",
          "+        Astar = misclassify(A, C, rng)",
          "+        X_other = np.column_stack([np.ones(N), T])",
          "+        gold_mask = np.zeros(N, dtype=bool)",
          "+        gold_mask[:int(0.1 * N)] = True",
          "+",
          "+        D_star = make_dummies(Astar, K)",
          "+        X_unc = np.column_stack([X_other, D_star])",
          "+        beta_unc, _ = ols_with_se(X_unc, Y)",
          "+",
          "+        D_true = make_dummies(A, K)",
          "+        X_true = np.column_stack([X_other, D_true])",
          "+        beta_true, _ = ols_with_se(X_true, Y)",
          "+        tau_true = beta_true[1]",
          "+",
          "+        tau_dsl, _, ok = correct_dsl(X_other, Y, Astar, A, gold_mask,",
          "+                                     tau_idx=1)",
          "+        bias_unc = abs(beta_unc[1] - tau_true)",
          "+        bias_dsl = abs(tau_dsl - tau_true)",
          "+        assert bias_dsl > bias_unc * 0.8, (",
          "+            f\"DSL bias {bias_dsl:.4f} not worse than uncorrected {bias_unc:.4f}\"",
          "+        )",
          "+",
          "+    def test_end_to_end_pipeline(self):",
          "+        rng = np.random.default_rng(99)",
          "+        K = 3",
          "+        C = predefined_matrices(K)[\"symmetric_high\"]",
          "+        N = 2000",
          "+        data = generate_data(\"confounding\", N, seed=99)",
          "+        T, Y, A = data[\"T\"], data[\"Y\"], data[\"A\"]",
          "+",
          "+        r_bias = compute_bias(\"confounding\", C)",
          "+        assert abs(r_bias[\"bias\"]) > 0.01",
          "+",
          "+        Astar = misclassify(A, C, rng)",
          "+        X_other = np.column_stack([np.ones(N), T])",
          "+        gold_mask = np.zeros(N, dtype=bool)",
          "+        gold_mask[:int(0.1 * N)] = True",
          "+",
          "+        tau_ppi, se_ppi, ok = correct_ppi(X_other, Y, Astar, A, gold_mask,",
          "+                                          tau_idx=1, rng=rng)",
          "+        assert ok is True",
          "+        assert np.isfinite(tau_ppi)",
          "+",
          "+",
          " if __name__ == \"__main__\":",
          "     pytest.main([__file__, \"-v\"])"
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

_source line 46_

Now run the full test suite.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "47235480-7982-4bf3-8936-76e5e7ad2984",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0195oU2M3x7JCvp7CaK8GzFZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2782,
      "cache_read_input_tokens": 68388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2782
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

_source line 47_

<details open><summary>🔧 Tool call — Bash · `toolu_01Pg7Zq5d7oDGL7iBYpz6jKX`</summary>

```json
{
  "command": "python3 -m pytest annot_sensitivity/tests/test_core.py -v 2>&1",
  "timeout": 300000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "33529b4b-f3f1-4be3-94ec-2d1c1becea88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0195oU2M3x7JCvp7CaK8GzFZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2782,
      "cache_read_input_tokens": 68388,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2782
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

_source line 48_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bap9mr3ku",
  "tool_use_id": "toolu_01Pg7Zq5d7oDGL7iBYpz6jKX",
  "description": "python3 -m pytest annot_sensitivity/tests/test_core.py -v 2>&1",
  "task_type": "local_bash",
  "uuid": "2fe24442-37b0-47b2-9a6a-9eb6d1c5ac5f",
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020"
}
```

---

### System

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bap9mr3ku",
  "tool_use_id": "toolu_01Pg7Zq5d7oDGL7iBYpz6jKX",
  "status": "completed",
  "output_file": "",
  "summary": "python3 -m pytest annot_sensitivity/tests/test_core.py -v 2>&1",
  "uuid": "abd96dba-e525-414b-b5b2-6868db5d6e6b",
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020"
}
```

---

### Tool result

_source line 50 · 2026-05-20T23:53:44.879Z_

<details><summary>↩ Tool result · `toolu_01Pg7Zq5d7oDGL7iBYpz6jKX`</summary>

```text
============================= test session starts ==============================
platform linux -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib
plugins: anyio-4.13.0, typeguard-4.4.4
collecting ... collected 47 items

annot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_identity_valid PASSED [  2%]
annot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_predefined_valid PASSED [  4%]
annot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_non_square PASSED [  6%]
annot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_negative_entries PASSED [  8%]
annot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_not_column_stochastic PASSED [ 10%]
annot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_not_array PASSED [ 12%]
annot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_1x1 PASSED [ 14%]
annot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_random_valid PASSED [ 17%]
annot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_delta_zero_is_identity PASSED [ 19%]
annot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_delta_one_is_C0 PASSED [ 21%]
annot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_intermediate_column_stochastic PASSED [ 23%]
annot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_small_delta PASSED [ 25%]
annot_sensitivity/tests/test_core.py::TestComputeBias::test_identity_zero_bias PASSED [ 27%]
annot_sensitivity/tests/test_core.py::TestComputeBias::test_confounding_nonzero_bias PASSED [ 29%]
annot_sensitivity/tests/test_core.py::TestComputeBias::test_all_topologies_run PASSED [ 31%]
annot_sensitivity/tests/test_core.py::TestComputeBias::test_invalid_topology PASSED [ 34%]
annot_sensitivity/tests/test_core.py::TestComputeBias::test_invalid_C PASSED [ 36%]
annot_sensitivity/tests/test_core.py::TestComputeBias::test_worse_C_more_bias PASSED [ 38%]
annot_sensitivity/tests/test_core.py::TestComputeASV::test_returns_valid_structure PASSED [ 40%]
annot_sensitivity/tests/test_core.py::TestComputeASV::test_asv_is_positive_or_none PASSED [ 42%]
annot_sensitivity/tests/test_core.py::TestComputeASV::test_envelope_monotone PASSED [ 44%]
annot_sensitivity/tests/test_core.py::TestComputeASV::test_sign_flip_threshold PASSED [ 46%]
annot_sensitivity/tests/test_core.py::TestComputeASV::test_invalid_threshold_type PASSED [ 48%]
annot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_with_gold_recommends_ppi PASSED [ 51%]
annot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_confounding_recommends_dsl PASSED [ 53%]
annot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_mediation_recommends_dsl PASSED [ 55%]
annot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_collider_recommends_mcsimex PASSED [ 57%]
annot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_mbias_recommends_mcsimex PASSED [ 59%]
annot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_ranking_has_all_methods PASSED [ 61%]
annot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_notes_nonempty PASSED [ 63%]
annot_sensitivity/tests/test_core.py::TestDGP::test_generate_all_topologies PASSED [ 65%]
annot_sensitivity/tests/test_core.py::TestDGP::test_confounding_has_treatment PASSED [ 68%]
annot_sensitivity/tests/test_core.py::TestDGP::test_exposure_no_treatment PASSED [ 70%]
annot_sensitivity/tests/test_core.py::TestDGP::test_iv_has_instrument PASSED [ 72%]
annot_sensitivity/tests/test_core.py::TestDGP::test_invalid_topology PASSED [ 74%]
annot_sensitivity/tests/test_core.py::TestIVWald::test_identity_zero_bias PASSED [ 76%]
annot_sensitivity/tests/test_core.py::TestIVWald::test_near_permutation_sign_flip PASSED [ 78%]
annot_sensitivity/tests/test_core.py::TestIVWald::test_asv_sign_flip_finite PASSED [ 80%]
annot_sensitivity/tests/test_core.py::TestIVWald::test_symmetric_high_moderate_bias PASSED [ 82%]
annot_sensitivity/tests/test_core.py::TestCorrectionMethods::test_naive_plugin_smoke PASSED [ 85%]
annot_sensitivity/tests/test_core.py::TestCorrectionMethods::test_dsl_smoke PASSED [ 87%]
annot_sensitivity/tests/test_core.py::TestCorrectionMethods::test_ppi_smoke PASSED [ 89%]
annot_sensitivity/tests/test_core.py::TestCorrectionMethods::test_mcsimex_smoke PASSED [ 91%]
annot_sensitivity/tests/test_core.py::TestCorrectionMethods::test_mla_smoke PASSED [ 93%]
annot_sensitivity/tests/test_core.py::TestCorrectionMethods::test_ppi_bias_reduction PASSED [ 95%]
annot_sensitivity/tests/test_core.py::TestCorrectionMethods::test_dsl_catastrophic_on_mbias PASSED [ 97%]
annot_sensitivity/tests/test_core.py::TestCorrectionMethods::test_end_to_end_pipeline PASSED [100%]

============================= 47 passed in 10.76s ==============================
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "bef044c3-3832-4c23-a7a5-ac253f80ca54",
  "tool_use_result": {
    "stdout": "============================= test session starts ==============================\nplatform linux -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- /usr/bin/python3\ncachedir: .pytest_cache\nrootdir: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib\nplugins: anyio-4.13.0, typeguard-4.4.4\ncollecting ... collected 47 items\n\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_identity_valid PASSED [  2%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_predefined_valid PASSED [  4%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_non_square PASSED [  6%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_negative_entries PASSED [  8%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_not_column_stochastic PASSED [ 10%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_not_array PASSED [ 12%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_1x1 PASSED [ 14%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_random_valid PASSED [ 17%]\nannot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_delta_zero_is_identity PASSED [ 19%]\nannot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_delta_one_is_C0 PASSED [ 21%]\nannot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_intermediate_column_stochastic PASSED [ 23%]\nannot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_small_delta PASSED [ 25%]\nannot_sensitivity/tests/test_core.py::TestComputeBias::test_identity_zero_bias PASSED [ 27%]\nannot_sensitivity/tests/test_core.py::TestComputeBias::test_confounding_nonzero_bias PASSED [ 29%]\nannot_sensitivity/tests/test_core.py::TestComputeBias::test_all_topologies_run PASSED [ 31%]\nannot_sensitivity/tests/test_core.py::TestComputeBias::test_invalid_topology PASSED [ 34%]\nannot_sensitivity/tests/test_core.py::TestComputeBias::test_invalid_C PASSED [ 36%]\nannot_sensitivity/tests/test_core.py::TestComputeBias::test_worse_C_more_bias PASSED [ 38%]\nannot_sensitivity/tests/test_core.py::TestComputeASV::test_returns_valid_structure PASSED [ 40%]\nannot_sensitivity/tests/test_core.py::TestComputeASV::test_asv_is_positive_or_none PASSED [ 42%]\nannot_sensitivity/tests/test_core.py::TestComputeASV::test_envelope_monotone PASSED [ 44%]\nannot_sensitivity/tests/test_core.py::TestComputeASV::test_sign_flip_threshold PASSED [ 46%]\nannot_sensitivity/tests/test_core.py::TestComputeASV::test_invalid_threshold_type PASSED [ 48%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_with_gold_recommends_ppi PASSED [ 51%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_confounding_recommends_dsl PASSED [ 53%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_mediation_recommends_dsl PASSED [ 55%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_collider_recommends_mcsimex PASSED [ 57%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_mbias_recommends_mcsimex PASSED [ 59%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_ranking_has_all_methods PASSED [ 61%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_notes_nonempty PASSED [ 63%]\nannot_sensitivity/tests/test_core.py::TestDGP::test_generate_all_topologies PASSED [ 65%]\nannot_sensitivity/tests/test_core.py::TestDGP::test_confounding_has_treatment PASSED [ 68%]\nannot_sensitivity/tests/test_core.py::TestDGP::test_exposure_no_treatment PASSED [ 70%]\nannot_sensitivity/tests/test_core.py::TestDGP::test_iv_has_instrument PASSED [ 72%]\nannot_sensitivity/tests/test_core.py::TestDGP::test_invalid_topology PASSED [ 74%]\nannot_sensitivity/tests/test_core.py::TestIVWald::test_identity_zero_bias PASSED [ 76%]\nannot_sensitivity/tests/test_core.py::TestIVWald::test_near_permutation_sign_flip PASSED [ 78%]\nannot_sensitivity/tests/test_core.py::TestIVWald::test_asv_sign_flip_finite PASSED [ 80%]\nannot_sensitivity/tests/test_core.py::TestIVWald::test_symmetric_high_moderate_bias PASSED [ 82%]\nannot_sensitivity/tests/test_core.py::TestCorrectionMethods::test_naive_plugin_smoke PASSED [ 85%]\nannot_sensitivity/tests/test_core.py::TestCorrectionMethods::test_dsl_smoke PASSED [ 87%]\nannot_sensitivity/tests/test_core.py::TestCorrectionMethods::test_ppi_smoke PASSED [ 89%]\nannot_sensitivity/tests/test_core.py::TestCorrectionMethods::test_mcsimex_smoke PASSED [ 91%]\nannot_sensitivity/tests/test_core.py::TestCorrectionMethods::test_mla_smoke PASSED [ 93%]\nannot_sensitivity/tests/test_core.py::TestCorrectionMethods::test_ppi_bias_reduction PASSED [ 95%]\nannot_sensitivity/tests/test_core.py::TestCorrectionMethods::test_dsl_catastrophic_on_mbias PASSED [ 97%]\nannot_sensitivity/tests/test_core.py::TestCorrectionMethods::test_end_to_end_pipeline PASSED [100%]\n\n============================= 47 passed in 10.76s ==============================",
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

_source line 51_

47/47 pass. Summary:

**W1 (IV Wald fix)**: Added `_plim_iv()` and IV-specific precomputation (RF, FS) to `bias.py`. IV topology now uses Wald estimator `RF / (C @ FS)[1]` instead of OLS. Near-permutation C produces -762.8% bias with sign flip, matching the paper's finding.

**W2 (Correction tests)**: Added 12 new tests in two classes:
- `TestIVWald` (4 tests): identity zero bias, near-permutation sign flip, ASV sign_flip finite, symmetric_high moderate bias
- `TestCorrectionMethods` (8 tests): 5 smoke tests, PPI++ bias reduction >50%, DSL catastrophic on mbias, end-to-end pipeline

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "uuid": "7f9bdc07-8fa1-49ff-aa5c-a1804aa6829d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXSMT6Zipt2RnCZUVmLoCY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1931,
      "cache_read_input_tokens": 71170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1931
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

_source line 52_

47/47 pass. Summary:

**W1 (IV Wald fix)**: Added `_plim_iv()` and IV-specific precomputation (RF, FS) to `bias.py`. IV topology now uses Wald estimator `RF / (C @ FS)[1]` instead of OLS. Near-permutation C produces -762.8% bias with sign flip, matching the paper's finding.

**W2 (Correction tests)**: Added 12 new tests in two classes:
- `TestIVWald` (4 tests): identity zero bias, near-permutation sign flip, ASV sign_flip finite, symmetric_high moderate bias
- `TestCorrectionMethods` (8 tests): 5 smoke tests, PPI++ bias reduction >50%, DSL catastrophic on mbias, end-to-end pipeline

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 171039,
  "duration_api_ms": 147316,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "7af88b0a-5af8-4480-8e3f-ff9155a17020",
  "total_cost_usd": 0.8769405000000002,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 61260,
    "cache_read_input_tokens": 551883,
    "output_tokens": 8588,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 61260,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 201,
        "cache_read_input_tokens": 71170,
        "cache_creation_input_tokens": 1931,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1931
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3269,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0033640000000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 8588,
      "cacheReadInputTokens": 551883,
      "cacheCreationInputTokens": 61260,
      "webSearchRequests": 0,
      "costUSD": 0.8735765000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f42e9060-8ef7-485d-9e9e-b79e76ba0ac2"
}
```

</details>

---
