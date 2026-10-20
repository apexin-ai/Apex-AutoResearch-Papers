# Research conversation: Read the full file at /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan_005_as

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-ac15b957449628c9b.jsonl`
- **Structured JSON:** [`4d8ecd1c16586f467ce3.json`](../../sessions/4d/4d8ecd1c16586f467ce3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

5 recorded events

### User

_source line 1 · 2026-05-20T16:10:20.098Z_

Read the full file at /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan_005_asv_extended_fixed.py and report back the entire contents. I need to understand:
1. The M-bias, IV, and front-door plim functions - their signatures, parameters, and return values
2. Any additional plim functions not in plan_002
3. How the GPU framework differs from plan_002
4. The overall script structure

Read the complete file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ef981d00-655a-40ab-b613-a59407a7199d",
  "agentId": "ac15b957449628c9b",
  "type": "user",
  "uuid": "82254aa0-06c5-4eab-9e2f-ff1a206ddf85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "8336aaef-aca4-4681-aaf5-922c1ee2b72e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-20T16:10:21.234Z_

I'll read the complete file for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82254aa0-06c5-4eab-9e2f-ff1a206ddf85",
  "isSidechain": true,
  "agentId": "ac15b957449628c9b",
  "requestId": "req_011CbE7V6Fmz96ysdTqHQyeY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7cfb041e-501a-4c41-894b-12304bd4d390",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "8336aaef-aca4-4681-aaf5-922c1ee2b72e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0122pmaHB1Wnz98FsDSPNAqQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 550,
      "cache_read_input_tokens": 15112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 550,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T16:10:21.676Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Np6WosCYZpDjFYqgdomMR8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan_005_asv_extended_fixed.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cfb041e-501a-4c41-894b-12304bd4d390",
  "isSidechain": true,
  "agentId": "ac15b957449628c9b",
  "requestId": "req_011CbE7V6Fmz96ysdTqHQyeY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "71858df7-3cc0-4ff2-9c0a-5541db3cfa44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "8336aaef-aca4-4681-aaf5-922c1ee2b72e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0122pmaHB1Wnz98FsDSPNAqQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 550,
      "cache_read_input_tokens": 15112,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 550
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 105,
          "cache_read_input_tokens": 15112,
          "cache_creation_input_tokens": 550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 550,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T16:10:21.958Z_

<details><summary>↩ Tool result · `toolu_01Np6WosCYZpDjFYqgdomMR8`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_005_fixed: ASV Framework Extension (C1/C2/W1/W2 fixes)
4	
5	Fixes applied (Reviewer CRITICAL):
6	  C1: Added compute_signif_asv_fast from plan_004_v3_fixed
7	  C2: compute_magnitude_asv_fast returns 0.0 (not None) when tau_true ~ 0
8	  W1: IV tau_true = plim_iv(I), not DGP beta (approx 0.66 vs 0.5)
9	  W2: M-bias tau_true = plim_mbias(I)[1], not DGP tau (approx 0.5128 vs 0.5)
10	
11	Only Part 2+3+5 re-run. Part 1 and Part 4 preserved but skipped.
12	Part 5 uses significance-based ASV rejection rule (from plan_004_v3_fixed).
13	"""
14	
15	import numpy as np
16	import json
17	import time
18	
19	K = 3
20	
21	# ============================================================================
22	# Utilities (from plan_004 v3)
23	# ============================================================================
24	
25	def softmax_sample(logits, rng):
26	    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))
27	    probs = exp_l / exp_l.sum(axis=1, keepdims=True)
28	    cum = np.cumsum(probs, axis=1)
29	    u = rng.uniform(size=logits.shape[0])
30	    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)
31	
32	
33	def generate_Astar(A, C, rng):
34	    probs = C[:, A]
35	    cum = np.cumsum(probs, axis=0)
36	    u = rng.uniform(size=len(A))
37	    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)
38	
39	
40	def ols_with_dummies(Y, T, Astar, K=3):
41	    N = len(Y)
42	    D = np.zeros((N, K - 1))
43	    for k in range(1, K):
44	        D[:, k - 1] = (Astar == k).astype(float)
45	    X = np.column_stack([np.ones(N), T, D])
46	    try:
47	        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
48	        resid = Y - X @ beta
49	        sigma2 = np.sum(resid**2) / max(N - X.shape[1], 1)
50	        XtX_inv = np.linalg.inv(X.T @ X)
51	        se = np.sqrt(np.maximum(sigma2 * np.diag(XtX_inv), 0))
52	    except np.linalg.LinAlgError:
53	        beta = np.full(X.shape[1], np.nan)
54	        se = np.full(X.shape[1], np.nan)
55	    return beta, se
56	
57	
58	# ============================================================================
59	# C(delta) Parameterization (from plan_004 v3)
60	# ============================================================================
61	
62	class LinearInterpolation:
63	    def __call__(self, C0, delta):
64	        K = C0.shape[0]
65	        C_d = (1 - delta) * np.eye(K) + delta * C0
66	        C_d = np.maximum(C_d, 0.0)
67	        col_sums = C_d.sum(axis=0)
68	        col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)
69	        C_d = C_d / col_sums
70	        return C_d
71	
72	    def delta_range(self, C0=None):
73	        if C0 is None:
74	            return (0.0, 5.0)
75	        min_diag = np.diag(C0).min()
76	        if min_diag >= 1.0:
77	            return (0.0, 10.0)
78	        delta_max = min(1.0 / (1.0 - min_diag), 10.0)
79	        return (0.0, delta_max)
80	
81	
82	# ============================================================================
83	# C matrices (from plan_004 v3)
84	# ============================================================================
85	
86	def make_C_list():
87	    return {
88	        "C1_sym": np.array([[0.80, 0.10, 0.10],
89	                            [0.10, 0.80, 0.10],
90	                            [0.10, 0.10, 0.80]]),
91	        "C2_high": np.array([[0.90, 0.05, 0.05],
92	                             [0.05, 0.90, 0.05],
93	                             [0.05, 0.05, 0.90]]),
94	        "C3_asym": np.array([[0.70, 0.20, 0.10],
95	                             [0.15, 0.70, 0.15],
96	                             [0.10, 0.15, 0.75]]),
97	        "C4_weak": np.array([[0.60, 0.20, 0.20],
98	                             [0.20, 0.60, 0.20],
99	                             [0.15, 0.15, 0.70]]),
100	        "C5_perm": np.array([[0.40, 0.30, 0.30],
101	                             [0.30, 0.40, 0.30],
102	                             [0.30, 0.30, 0.40]]),
103	        "C6_diff": np.array([[0.85, 0.075, 0.075],
104	                             [0.15, 0.70, 0.15],
105	                             [0.05, 0.05, 0.90]]),
106	    }
107	
108	
109	def normalize_C_list(C_dict):
110	    out = {}
111	    for name, C in C_dict.items():
112	        C = np.maximum(C, 0.0)
113	        cs = C.sum(axis=0)
114	        cs = np.where(cs < 1e-10, 1.0, cs)
115	        out[name] = C / cs
116	    return out
117	
118	
119	def random_C0(K, rng, diag_alpha=5.0, offdiag_alpha=1.0):
120	    C = np.zeros((K, K))
121	    for k in range(K):
122	        alphas = np.full(K, offdiag_alpha)
123	        alphas[k] = diag_alpha
124	        C[:, k] = rng.dirichlet(alphas)
125	    return C
126	
127	
128	# ============================================================================
129	# Topology 1: M-BIAS — U1->{A,T}, U2->{A,Y}, T->Y
130	# ============================================================================
131	
132	MBIAS_PARAMS = dict(tau=0.5, delta=1.0, lam=1.0,
133	                    g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9)
134	
135	
136	def _gen_mbias(N, params, rng):
137	    U1 = rng.normal(0, 1, N)
138	    U2 = rng.normal(0, 1, N)
139	    T = params['delta'] * U1 + rng.normal(0, 1, N)
140	    Y = params['tau'] * T + params['lam'] * U2 + rng.normal(0, 1, N)
141	    logits = np.column_stack([
142	        np.zeros(N),
143	        params['g1'] + params['a1'] * U1 + params['a2'] * U2,
144	        params['g2'] + params['a3'] * U1 + params['a4'] * U2,
145	    ])
146	    A = softmax_sample(logits, rng)
147	    return T, Y, A
148	
149	
150	def gen_mbias_data(N, params, C0, rng):
151	    T, Y, A = _gen_mbias(N, params, rng)
152	    Astar = generate_Astar(A, C0, rng)
153	    return T, Y, A, Astar
154	
155	
156	def precomp_mbias(params, N=2_000_000, seed=999):
157	    rng = np.random.default_rng(seed)
158	    T, Y, A = _gen_mbias(N, params, rng)
159	    DA = np.zeros((N, K))
160	    for k in range(K):
161	        DA[:, k] = (A == k).astype(float)
162	    return dict(
163	        E_T=T.mean(), E_T2=(T**2).mean(),
164	        E_Y=Y.mean(), E_TY=(T*Y).mean(),
165	        E_DA=DA.mean(0),
166	        E_DA_T=(DA * T[:, None]).mean(0),
167	        E_DA_Y=(DA * Y[:, None]).mean(0))
168	
169	
170	def plim_mbias(C, st):
171	    """OLS plim for Y ~ 1 + T + D1_A* + D2_A*."""
172	    ds  = C @ st['E_DA']
173	    dst = C @ st['E_DA_T']
174	    dsy = C @ st['E_DA_Y']
175	    ET, ET2 = st['E_T'], st['E_T2']
176	    EY, ETY = st['E_Y'], st['E_TY']
177	    EZZ = np.array([
178	        [1,      ET,      ds[1],    ds[2]   ],
179	        [ET,     ET2,     dst[1],   dst[2]  ],
180	        [ds[1],  dst[1],  ds[1],    0       ],
181	        [ds[2],  dst[2],  0,        ds[2]   ]])
182	    EZY = np.array([EY, ETY, dsy[1], dsy[2]])
183	    return np.linalg.solve(EZZ, EZY)
184	
185	
186	# ============================================================================
187	# Topology 2: IV — Z->A->Y, U->{A,Y}
188	# ============================================================================
189	
190	IV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)
191	IV_BETA = np.array([0.0, 0.5, -0.25])
192	
193	
194	def _gen_iv(N, beta, params, rng):
195	    Z_iv = rng.binomial(1, 0.5, N).astype(float)
196	    U = rng.normal(0, 1, N)
197	    eps = rng.normal(0, 1, N)
198	    logits = np.column_stack([
199	        np.zeros(N),
200	        params['g1'] + params['dZ'] * Z_iv + params['dU'] * U,
201	        params['g2'] + params['dZ2'] * Z_iv + params['dU2'] * U,
202	    ])
203	    A = softmax_sample(logits, rng)
204	    Y = (beta[1] * (A == 1).astype(float) + beta[2] * (A == 2).astype(float)
205	         + params['lam'] * U + eps)
206	    return Z_iv, U, Y, A
207	
208	
209	def gen_iv_data(N, beta, params, C0, rng):
210	    Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)
211	    Astar = generate_Astar(A, C0, rng)
212	    return Z_iv, Y, A, Astar
213	
214	
215	def precomp_iv(beta, params, N=2_000_000, seed=999):
216	    """Precompute reduced form and first stage for Wald estimator."""
217	    rng = np.random.default_rng(seed)
218	    Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)
219	    z1 = Z_iv == 1; z0 = Z_iv == 0
220	    RF = Y[z1].mean() - Y[z0].mean()
221	    FS = np.zeros(K)
222	    for k in range(K):
223	        FS[k] = (A[z1] == k).mean() - (A[z0] == k).mean()
224	    return dict(RF=RF, FS=FS)
225	
226	
227	def plim_iv(C, st):
228	    """Wald estimator: RF / FS*_1 where FS* = C @ FS."""
229	    FS_star = C @ st['FS']
230	    if abs(FS_star[1]) < 1e-8:
231	        return np.nan
232	    return st['RF'] / FS_star[1]
233	
234	
235	def wald_with_se(Z, Y, Astar, k=1):
236	    """Finite-sample Wald estimator with delta-method SE."""
237	    z1 = Z == 1; z0 = Z == 0
238	    n1 = float(z1.sum()); n0 = float(z0.sum())
239	    if n1 < 2 or n0 < 2:
240	        return np.nan, np.nan
241	    RF = Y[z1].mean() - Y[z0].mean()
242	    var_RF = Y[z1].var() / n1 + Y[z0].var() / n0
243	    Dk_z1 = (Astar[z1] == k).astype(float).mean()
244	    Dk_z0 = (Astar[z0] == k).astype(float).mean()
245	    FS = Dk_z1 - Dk_z0
246	    var_FS = Dk_z1 * (1 - Dk_z1) / n1 + Dk_z0 * (1 - Dk_z0) / n0
247	    if abs(FS) < 1e-8:
248	        return np.nan, np.nan
249	    Wald = RF / FS
250	    var_Wald = var_RF / FS**2 + RF**2 * var_FS / FS**4
251	    SE = np.sqrt(max(var_Wald, 0))
252	    return Wald, SE
253	
254	
255	# ============================================================================
256	# Topology 3: FRONT-DOOR — T->M->Y, U->{T,Y}
257	# ============================================================================
258	
259	ALPHA_U = 1.0
260	LAMBDA_U = 1.0
261	GAMMA_FD = np.array([0.0, 0.5, -0.3])
262	DELTA_FD = np.array([0.0, 1.0, -0.8])
263	BETA_FD = np.array([0.0, 1.0, -0.5])
264	
265	
266	def _gen_fd(N, beta, rng, g=None, d=None, aU=None, lU=None):
267	    if g is None: g = GAMMA_FD
268	    if d is None: d = DELTA_FD
269	    if aU is None: aU = ALPHA_U
270	    if lU is None: lU = LAMBDA_U
271	    U = rng.normal(0, 1, N)
272	    T = aU * U + rng.normal(0, 1, N)
273	    lo = np.column_stack([np.zeros(N), g[1] + d[1]*T, g[2] + d[2]*T])
274	    lo -= lo.max(1, keepdims=True)
275	    e = np.exp(lo)
276	    p = e / e.sum(1, keepdims=True)
277	    cu = np.cumsum(p, axis=1)
278	    u = rng.uniform(size=N)
279	    M = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)
280	    DM1 = (M == 1).astype(float)
281	    DM2 = (M == 2).astype(float)
282	    Y = beta[1]*DM1 + beta[2]*DM2 + lU*U + rng.normal(0, 1, N)
283	    return T, M, Y, U
284	
285	
286	def gen_fd_data(N, beta, C0, rng, lU=None, aU=None, d=None):
287	    T, M, Y, U = _gen_fd(N, beta, rng, d=d, aU=aU, lU=lU)
288	    Mstar = generate_Astar(M, C0, rng)
289	    return T, Y, M, Mstar
290	
291	
292	def precomp_fd(beta, N=10_000_000, seed=123, lU=None, aU=None, d=None):
293	    rng = np.random.default_rng(seed)
294	    T, M, Y, _ = _gen_fd(N, beta, rng, d=d, aU=aU, lU=lU)
295	    DM = np.zeros((N, K))
296	    for k in range(K):
297	        DM[:, k] = (M == k).astype(float)
298	    return dict(
299	        E_T=T.mean(), E_T2=(T**2).mean(),
300	        E_Y=Y.mean(), E_TY=(T*Y).mean(),
301	        E_DM=DM.mean(0),
302	        E_DM_T=(DM * T[:, None]).mean(0),
303	        E_DM_Y=(DM * Y[:, None]).mean(0))
304	
305	
306	def plim_fd(C, st):
307	    """OLS plim for Y ~ 1 + T + D1_M* + D2_M*."""
308	    ds  = C @ st['E_DM']
309	    dst = C @ st['E_DM_T']
310	    dsy = C @ st['E_DM_Y']
311	    ET, ET2 = st['E_T'], st['E_T2']
312	    EY, ETY = st['E_Y'], st['E_TY']
313	    EZZ = np.array([
314	        [1,      ET,      ds[1],    ds[2]   ],
315	        [ET,     ET2,     dst[1],   dst[2]  ],
316	        [ds[1],  dst[1],  ds[1],    0       ],
317	        [ds[2],  dst[2],  0,        ds[2]   ]])
318	    EZY = np.array([EY, ETY, dsy[1], dsy[2]])
319	    return np.linalg.solve(EZZ, EZY)
320	
321	
322	# ============================================================================
323	# ASV Framework
324	# ============================================================================
325	
326	def compute_bias_curve(topology, C0, param, tau_true, st, n_grid=1500):
327	    dmin, dmax = param.delta_range(C0)
328	    deltas = np.linspace(dmin, dmax, n_grid)
329	    tau_curve = np.zeros(n_grid)
330	    for i, d in enumerate(deltas):
331	        C_d = param(C0, d)
332	        if topology == "mbias":
333	            tau_curve[i] = plim_mbias(C_d, st)[1]
334	        elif topology == "iv":
335	            tau_curve[i] = plim_iv(C_d, st)
336	        elif topology == "frontdoor":
337	            tau_curve[i] = plim_fd(C_d, st)[1]
338	    bias_abs = np.abs(tau_curve - tau_true)
339	    return deltas, bias_abs, tau_curve
340	
341	
342	def compute_envelope(bias_abs):
343	    env = np.zeros_like(bias_abs)
344	    running_max = 0.0
345	    for i in range(len(bias_abs)):
346	        v = bias_abs[i]
347	        if not np.isnan(v):
348	            running_max = max(running_max, v)
349	        env[i] = running_max
350	    return env
351	
352	
353	def verify_envelope_monotonicity(envelope):
354	    diffs = np.diff(envelope)
355	    return int(np.sum(diffs < -1e-12))
356	
357	
358	def compute_asv_envelope(topology, C0, tau_true, param, threshold_type,
359	                         threshold_value=0.1, st=None, n_grid=1500):
360	    deltas, bias_abs, tau_curve = compute_bias_curve(
361	        topology, C0, param, tau_true, st, n_grid)
362	    envelope = compute_envelope(bias_abs)
363	
364	    valid_ba = bias_abs[~np.isnan(bias_abs)]
365	    raw_violations = int(np.sum(np.diff(valid_ba) < -1e-12)) if len(valid_ba) > 1 else 0
366	    env_violations = verify_envelope_monotonicity(envelope)
367	
368	    asv = None
369	    if threshold_type == "sign_flip":
370	        if abs(tau_true) < 1e-12:
371	            asv = None
372	        else:
373	            baseline_sign = np.sign(tau_true)
374	            for i, d in enumerate(deltas):
375	                if np.isnan(tau_curve[i]):
376	                    continue
377	                if np.sign(tau_curve[i]) != baseline_sign:
378	                    asv = d
379	                    break
380	    elif threshold_type == "magnitude_relative":
381	        if abs(tau_true) < 1e-12:
382	            asv = None
383	        else:
384	            thresh = threshold_value * abs(tau_true)
385	            for i, d in enumerate(deltas):
386	                if envelope[i] > thresh:
387	                    asv = d
388	                    break
389	    elif threshold_type == "magnitude_absolute":
390	        thresh = threshold_value
391	        for i, d in enumerate(deltas):
392	            if envelope[i] > thresh:
393	                asv = d
394	                break
395	
396	    return {
397	        "asv": asv,
398	        "raw_violations": raw_violations,
399	        "envelope_violations": env_violations,
400	        "deltas": deltas,
401	        "tau_curve": tau_curve,
402	        "envelope": envelope,
403	    }
404	
405	
406	def compute_magnitude_asv_fast(tau_curve, deltas, tau_true, rel_thresh=0.1):
407	    # [C2] tau~0 means maximally fragile — any annotation error changes the result
408	    if abs(tau_true) < 1e-12:
409	        return 0.0
410	    thresh = rel_thresh * abs(tau_true)
411	    running_max = 0.0
412	    for i in range(len(deltas)):
413	        b = abs(tau_curve[i] - tau_true)
414	        if np.isnan(b):
415	            continue
416	        running_max = max(running_max, b)
417	        if running_max > thresh:
418	            return deltas[i]
419	    return None
420	
421	
422	# [C1] Significance-based ASV from plan_004_v3_fixed
423	def compute_signif_asv_fast(tau_curve, deltas, se):
424	    """Min delta where |plim tau(C(delta))| < 1.96 * SE (becomes non-significant)."""
425	    z_crit = 1.96
426	    for i in range(len(deltas)):
427	        if np.isnan(tau_curve[i]):
428	            continue
429	        if abs(tau_curve[i]) < z_crit * se:
430	            return deltas[i]
431	    return None
432	
433	
434	# ============================================================================
435	# Part 1: Envelope Monotonicity (preserved, skipped in main)
436	# ============================================================================
437	
438	def part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_fd):
439	    print("\n" + "=" * 70)
440	    print("PART 1: Envelope Monotonicity (tau=0.5)")
441	    print("=" * 70)
442	    t0 = time.time()
443	    param = LinearInterpolation()
444	    C_list = normalize_C_list(make_C_list())
445	
446	    for topo, st, tau_true, label in [
447	        ("mbias", st_mb, 0.5, "M-bias"),
448	        ("iv", st_iv, 0.5, "IV"),
449	        ("frontdoor", st_fd, tau_fd, "Front-door"),
450	    ]:
451	        print(f"\n  {label} (tau_true={tau_true:.4f}):")
452	        for cname, C0 in C_list.items():
453	            r = compute_asv_envelope(topo, C0, tau_true, param,
454	                                     "magnitude_relative", 0.1, st=st)
455	            print(f"    {cname}: raw_violations={r['raw_violations']}/1500, "
456	                  f"envelope_violations={r['envelope_violations']}/1500")
457	    print(f"\n  Time: {time.time()-t0:.1f}s")
458	
459	
460	# ============================================================================
461	# Part 2: ASV Values (tau=0.5) — [W1/W2] fixed tau_true
462	# ============================================================================
463	
464	def part2_asv_values(st_mb, st_iv, st_fd, tau_I_mb, tau_I_iv, tau_I_fd):
465	    print("\n" + "=" * 70)
466	    print("PART 2: ASV Values (tau=0.5)")
467	    print("=" * 70)
468	    t0 = time.time()
469	    param = LinearInterpolation()
470	    C_list = normalize_C_list(make_C_list())
471	    results = {}
472	
473	    print(f"\n  {'Topology':<12} {'C0':<10} {'SignFlip':>10} {'Mag10%':>10}")
474	    print("  " + "-" * 45)
475	
476	    # [W1/W2] Use plim(I) as tau_true — ASV measures ADDITIONAL bias from annotation error
477	    for topo, st, tau_true, label in [
478	        ("mbias", st_mb, tau_I_mb, "M-bias"),
479	        ("iv", st_iv, tau_I_iv, "IV"),
480	        ("frontdoor", st_fd, tau_I_fd, "Front-door"),
481	    ]:
482	        for cname, C0 in C_list.items():
483	            r_sf = compute_asv_envelope(topo, C0, tau_true, param,
484	                                        "sign_flip", st=st)
485	            r_mag = compute_asv_envelope(topo, C0, tau_true, param,
486	                                         "magnitude_relative", 0.1, st=st)
487	            sf_s = f"{r_sf['asv']:.3f}" if r_sf['asv'] is not None else "None"
488	            mg_s = f"{r_mag['asv']:.3f}" if r_mag['asv'] is not None else "None"
489	            print(f"  {label:<12} {cname:<10} {sf_s:>10} {mg_s:>10}")
490	            results[(label, cname)] = {
491	                "sign_flip": r_sf['asv'], "magnitude_10pct": r_mag['asv']}
492	    print(f"\n  Time: {time.time()-t0:.1f}s")
493	    return results
494	
495	
496	# ============================================================================
497	# Part 3: Small-tau ASV — [W1/W2] fixed tau_true
498	# ============================================================================
499	
500	def part3_small_tau_asv():
501	    print("\n" + "=" * 70)
502	    print("PART 3: Small-tau ASV (tau=0.05, 0.1)")
503	    print("=" * 70)
504	    t0 = time.time()
505	    param = LinearInterpolation()
506	    C_list = normalize_C_list(make_C_list())
507	    results = {}
508	
509	    for tau_val in [0.05, 0.1]:
510	        print(f"\n  --- tau = {tau_val} ---")
511	        mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_val
512	        st_mb = precomp_mbias(mb_p, N=2_000_000)
513	        iv_b = np.array([0.0, tau_val, -tau_val/2])
514	        st_iv = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
515	        lU = tau_val * 2
516	        st_fd = precomp_fd(BETA_FD, N=10_000_000, lU=lU, seed=200+int(tau_val*100))
517	        tau_fd = plim_fd(np.eye(K), st_fd)[1]
518	        print(f"  Front-door tau_I = {tau_fd:.6f}")
519	
520	        # [W1/W2] Use plim(I) as tau_true, not DGP parameter
521	        tau_I_mb = plim_mbias(np.eye(K), st_mb)[1]
522	        tau_I_iv = plim_iv(np.eye(K), st_iv)
523	        print(f"  M-bias tau_I = {tau_I_mb:.6f}, IV tau_I = {tau_I_iv:.6f}")
524	
525	        hdr = f"  {'Topology':<12} {'C0':<10} {'SignFlip':>10} {'Mag10%':>10} {'MagAbs.05':>10}"
526	        print(hdr)
527	        print("  " + "-" * 55)
528	
529	        for topo, st, tau_true, label in [
530	            ("mbias", st_mb, tau_I_mb, "M-bias"),
531	            ("iv", st_iv, tau_I_iv, "IV"),
532	            ("frontdoor", st_fd, tau_fd, "Front-door"),
533	        ]:
534	            for cname, C0 in C_list.items():
535	                r_sf = compute_asv_envelope(topo, C0, tau_true, param,
536	                                            "sign_flip", st=st)
537	                r_mg = compute_asv_envelope(topo, C0, tau_true, param,
538	                                            "magnitude_relative", 0.1, st=st)
539	                r_ab = compute_asv_envelope(topo, C0, tau_true, param,
540	                                            "magnitude_absolute", 0.05, st=st)
541	                sf_s = f"{r_sf['asv']:.3f}" if r_sf['asv'] is not None else "None"
542	                mg_s = f"{r_mg['asv']:.3f}" if r_mg['asv'] is not None else "None"
543	                ab_s = f"{r_ab['asv']:.3f}" if r_ab['asv'] is not None else "None"
544	                print(f"  {label:<12} {cname:<10} {sf_s:>10} {mg_s:>10} {ab_s:>10}")
545	                results[(tau_val, label, cname)] = {
546	                    "sign_flip": r_sf['asv'],
547	                    "magnitude_10pct": r_mg['asv'],
548	                    "magnitude_abs05": r_ab['asv']}
549	    print(f"\n  Time: {time.time()-t0:.1f}s")
550	    return results
551	
552	
553	# ============================================================================
554	# Part 4: MC Coverage (preserved, skipped in main)
555	# ============================================================================
556	
557	def part4_mc_coverage(n_scenarios=500, N_mc=10000, reps=100):
558	    print("\n" + "=" * 70)
559	    print(f"PART 4: MC Coverage ({n_scenarios} scenarios x {reps} reps x N={N_mc})")
560	    print("=" * 70)
561	    t0 = time.time()
562	    rng = np.random.default_rng(42)
563	    results = {}
564	
565	    for tau_val in [0.05, 0.1]:
566	        print(f"\n  --- tau = {tau_val} ---")
567	
568	        # --- M-bias ---
569	        print("  [M-bias]")
570	        mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_val
571	        st_mb = precomp_mbias(mb_p, N=2_000_000)
572	        plim_ok = 0; bias_ok = 0
573	        for s in range(n_scenarios):
574	            C0 = random_C0(K, rng)
575	            tau_plim = plim_mbias(C0, st_mb)[1]
576	            bias_theory = abs(tau_plim - tau_val)
577	            tau_mc = np.zeros(reps)
578	            for r in range(reps):
579	                Td, Yd, _, Asd = gen_mbias_data(N_mc, mb_p, C0, rng)
580	                bh, _ = ols_with_dummies(Yd, Td, Asd, K)
581	                tau_mc[r] = bh[1]
582	            mc_mean = tau_mc.mean()
583	            mc_se = tau_mc.std() / np.sqrt(reps)
584	            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:
585	                plim_ok += 1
586	            if abs(mc_mean - tau_val) <= bias_theory + 3 * mc_se + 0.02:
587	                bias_ok += 1
588	            if (s + 1) % 100 == 0:
589	                print(f"    ... {s+1}/{n_scenarios}")
590	        print(f"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%")
591	        print(f"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%")
592	        results[("mbias", tau_val)] = {
593	            "plim_acc": plim_ok/n_scenarios, "bias_bounded": bias_ok/n_scenarios}
594	
595	        # --- IV ---
596	        print("  [IV]")
597	        iv_b = np.array([0.0, tau_val, -tau_val/2])
598	        st_iv = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
599	        plim_ok = 0; bias_ok = 0
600	        for s in range(n_scenarios):
601	            C0 = random_C0(K, rng)
602	            tau_plim = plim_iv(C0, st_iv)
603	            if np.isnan(tau_plim):
604	                plim_ok += 1; bias_ok += 1; continue
605	            bias_theory = abs(tau_plim - tau_val)
606	            tau_mc = np.zeros(reps)
607	            for r in range(reps):
608	                Zd, Yd, _, Asd = gen_iv_data(N_mc, iv_b, IV_PARAMS, C0, rng)
609	                w, _ = wald_with_se(Zd, Yd, Asd)
610	                tau_mc[r] = w
611	            valid = ~np.isnan(tau_mc)
612	            if valid.sum() < reps * 0.5:
613	                plim_ok += 1; bias_ok += 1; continue
614	            mc_mean = tau_mc[valid].mean()
615	            mc_se = tau_mc[valid].std() / np.sqrt(valid.sum())
616	            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.05:
617	                plim_ok += 1
618	            if abs(mc_mean - tau_val) <= bias_theory + 3 * mc_se + 0.05:
619	                bias_ok += 1
620	            if (s + 1) % 100 == 0:
621	                print(f"    ... {s+1}/{n_scenarios}")
622	        print(f"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%")
623	        print(f"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%")
624	        results[("iv", tau_val)] = {
625	            "plim_acc": plim_ok/n_scenarios, "bias_bounded": bias_ok/n_scenarios}
626	
627	        # --- Front-door ---
628	        print("  [Front-door]")
629	        lU = tau_val * 2
630	        st_fd = precomp_fd(BETA_FD, N=10_000_000, lU=lU,
631	                           seed=300+int(tau_val*100))
632	        tau_I_fd = plim_fd(np.eye(K), st_fd)[1]
633	        plim_ok = 0; bias_ok = 0
634	        for s in range(n_scenarios):
635	            C0 = random_C0(K, rng)
636	            tau_plim = plim_fd(C0, st_fd)[1]
637	            bias_theory = abs(tau_plim - tau_I_fd)
638	            tau_mc = np.zeros(reps)
639	            for r in range(reps):
640	                Td, Yd, _, Msd = gen_fd_data(N_mc, BETA_FD, C0, rng, lU=lU)
641	                bh, _ = ols_with_dummies(Yd, Td, Msd, K)
642	                tau_mc[r] = bh[1]
643	            mc_mean = tau_mc.mean()
644	            mc_se = tau_mc.std() / np.sqrt(reps)
645	            if abs(mc_mean - tau_plim) < 3 * mc_se + 0.02:
646	                plim_ok += 1
647	            if abs(mc_mean - tau_I_fd) <= bias_theory + 3 * mc_se + 0.02:
648	                bias_ok += 1
649	            if (s + 1) % 100 == 0:
650	                print(f"    ... {s+1}/{n_scenarios}")
651	        print(f"    plim accuracy: {plim_ok}/{n_scenarios} = {plim_ok/n_scenarios*100:.1f}%")
652	        print(f"    bias bounded:  {bias_ok}/{n_scenarios} = {bias_ok/n_scenarios*100:.1f}%")
653	        results[("frontdoor", tau_val)] = {
654	            "plim_acc": plim_ok/n_scenarios, "bias_bounded": bias_ok/n_scenarios}
655	
656	    print(f"\n  Total time: {time.time()-t0:.1f}s")
657	    return results
658	
659	
660	# ============================================================================
661	# Part 5: Type I/II (Significance-Based ASV Filter) — REWRITTEN
662	# ============================================================================
663	
664	def part5_type_errors(n_mc=500, N_sample=5000):
665	    print("\n" + "=" * 70)
666	    print(f"PART 5: Type I/II ({n_mc} MC x N={N_sample})")
667	    print("  Filter: significance-based ASV")
668	    print("  reject if |tau_hat/SE|>1.96 AND (signif_ASV is None OR signif_ASV > 1)")
669	    print("=" * 70)
670	    t0 = time.time()
671	    param = LinearInterpolation()
672	    C_list = normalize_C_list(make_C_list())
673	    results = {}
674	    seed_ctr = 3000
675	
676	    for tau_val in [0.05, 0.1]:
677	        print(f"\n  --- tau = {tau_val} ---")
678	        header = (f"  {'C_struct':<12} {'H':<5} {'naive_rej':>10} "
679	                  f"{'asv_rej':>10} {'mean_sasv':>10} {'mag_asv':>10}")
680	
681	        # === M-bias ===
682	        print("\n  [M-bias]")
683	        print(header)
684	        print("  " + "-" * 55)
685	        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
686	            mb_p = dict(MBIAS_PARAMS); mb_p['tau'] = tau_h
687	            st_h = precomp_mbias(mb_p, N=2_000_000)
688	            # [W2] Use plim(I) as tau_true for magnitude ASV
689	            tau_I_h = plim_mbias(np.eye(K), st_h)[1]
690	            for cname, C0 in C_list.items():
691	                seed_ctr += 1
692	                dmin, dmax = param.delta_range(C0)
693	                deltas = np.linspace(dmin, dmax, 1500)
694	                tau_curve = np.array([
695	                    plim_mbias(param(C0, d), st_h)[1] for d in deltas])
696	                masv = compute_magnitude_asv_fast(
697	                    tau_curve, deltas, tau_I_h, 0.1)
698	                rng_mc = np.random.default_rng(seed_ctr)
699	                naive_rej = 0; asv_rej = 0; sasv_vals = []
700	                for mc in range(n_mc):
701	                    Td, Yd, _, Asd = gen_mbias_data(
702	                        N_sample, mb_p, C0, rng_mc)
703	                    bh, seh = ols_with_dummies(Yd, Td, Asd, K)
704	                    tau_hat, se_tau = bh[1], seh[1]
705	                    reject = (abs(tau_hat / se_tau) > 1.96
706	                              if se_tau > 1e-10 else False)
707	                    if reject:
708	                        naive_rej += 1
709	                    sasv = compute_signif_asv_fast(tau_curve, deltas, se_tau)
710	                    sasv_vals.append(sasv)
711	                    if reject and (sasv is None or sasv > 1.0):
712	                        asv_rej += 1
713	                sf = [a for a in sasv_vals if a is not None]
714	                sm = f"{np.mean(sf):.2f}" if sf else "N/A"
715	                ms = f"{masv:.2f}" if masv is not None else "None"
716	                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
717	                      f"{asv_rej/n_mc:>10.3f} {sm:>10} {ms:>10}")
718	                results[("mbias", tau_val, cname, h_label)] = {
719	                    "naive_rej": naive_rej/n_mc, "asv_rej": asv_rej/n_mc,
720	                    "mean_sasv": np.mean(sf) if sf else None, "masv": masv}
721	
722	        # === IV ===
723	        print("\n  [IV]")
724	        print(header)
725	        print("  " + "-" * 55)
726	        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
727	            iv_b = np.array([0.0, tau_h, -tau_h/2])
728	            st_h = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
729	            # [W1] Use plim(I) as tau_true for magnitude ASV
730	            tau_I_h = plim_iv(np.eye(K), st_h)
731	            for cname, C0 in C_list.items():
732	                seed_ctr += 1
733	                dmin, dmax = param.delta_range(C0)
734	                deltas = np.linspace(dmin, dmax, 1500)
735	                tau_curve = np.array([
736	                    plim_iv(param(C0, d), st_h) for d in deltas])
737	                masv = compute_magnitude_asv_fast(
738	                    tau_curve, deltas, tau_I_h, 0.1)
739	                rng_mc = np.random.default_rng(seed_ctr)
740	                naive_rej = 0; asv_rej = 0; sasv_vals = []
741	                for mc in range(n_mc):
742	                    Zd, Yd, _, Asd = gen_iv_data(
743	                        N_sample, iv_b, IV_PARAMS, C0, rng_mc)
744	                    w, se_w = wald_with_se(Zd, Yd, Asd)
745	                    reject = False
746	                    if not np.isnan(w) and se_w > 1e-10:
747	                        reject = abs(w / se_w) > 1.96
748	                    if reject:
749	                        naive_rej += 1
750	                    se_for_asv = se_w if (not np.isnan(se_w) and se_w > 1e-10) else 1e10
751	                    sasv = compute_signif_asv_fast(tau_curve, deltas, se_for_asv)
752	                    sasv_vals.append(sasv)
753	                    if reject and (sasv is None or sasv > 1.0):
754	                        asv_rej += 1
755	                sf = [a for a in sasv_vals if a is not None]
756	                sm = f"{np.mean(sf):.2f}" if sf else "N/A"
757	                ms = f"{masv:.2f}" if masv is not None else "None"
758	                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
759	                      f"{asv_rej/n_mc:>10.3f} {sm:>10} {ms:>10}")
760	                results[("iv", tau_val, cname, h_label)] = {
761	                    "naive_rej": naive_rej/n_mc, "asv_rej": asv_rej/n_mc,
762	                    "mean_sasv": np.mean(sf) if sf else None, "masv": masv}
763	
764	        # === Front-door ===
765	        print("\n  [Front-door]")
766	        print(header)
767	        print("  " + "-" * 55)
768	        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
769	            if h_label == "H0":
770	                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=0.0, aU=0.0,
771	                                  d=np.zeros(3), seed=400)
772	                tau_ref = 0.0
773	            else:
774	                lU = tau_val * 2
775	                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=lU,
776	                                  seed=401+int(tau_val*100))
777	                tau_ref = plim_fd(np.eye(K), st_h)[1]
778	            print(f"    ({h_label}: tau_ref={tau_ref:.4f})")
779	            for cname, C0 in C_list.items():
780	                seed_ctr += 1
781	                dmin, dmax = param.delta_range(C0)
782	                deltas = np.linspace(dmin, dmax, 1500)
783	                tau_curve = np.array([
784	                    plim_fd(param(C0, d), st_h)[1] for d in deltas])
785	                masv = compute_magnitude_asv_fast(
786	                    tau_curve, deltas, tau_ref, 0.1)
787	                rng_mc = np.random.default_rng(seed_ctr)
788	                naive_rej = 0; asv_rej = 0; sasv_vals = []
789	                for mc in range(n_mc):
790	                    if h_label == "H0":
791	                        Td, Yd, _, Msd = gen_fd_data(
792	                            N_sample, BETA_FD, C0, rng_mc,
793	                            lU=0.0, aU=0.0, d=np.zeros(3))
794	                    else:
795	                        Td, Yd, _, Msd = gen_fd_data(
796	                            N_sample, BETA_FD, C0, rng_mc, lU=lU)
797	                    bh, seh = ols_with_dummies(Yd, Td, Msd, K)
798	                    tau_hat, se_tau = bh[1], seh[1]
799	                    reject = (abs(tau_hat / se_tau) > 1.96
800	                              if se_tau > 1e-10 else False)
801	                    if reject:
802	                        naive_rej += 1
803	                    sasv = compute_signif_asv_fast(tau_curve, deltas, se_tau)
804	                    sasv_vals.append(sasv)
805	                    if reject and (sasv is None or sasv > 1.0):
806	                        asv_rej += 1
807	                sf = [a for a in sasv_vals if a is not None]
808	                sm = f"{np.mean(sf):.2f}" if sf else "N/A"
809	                ms = f"{masv:.2f}" if masv is not None else "None"
810	                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
811	                      f"{asv_rej/n_mc:>10.3f} {sm:>10} {ms:>10}")
812	                results[("frontdoor", tau_val, cname, h_label)] = {
813	                    "naive_rej": naive_rej/n_mc, "asv_rej": asv_rej/n_mc,
814	                    "mean_sasv": np.mean(sf) if sf else None, "masv": masv}
815	
816	    print(f"\n  Total time: {time.time()-t0:.1f}s")
817	    return results
818	
819	
820	# ============================================================================
821	# Part 6: Summary JSON
822	# ============================================================================
823	
824	def collect_summary(asv_res, small_tau_res, cov_res, te_res):
825	    def _f(v):
826	        if v is None:
827	            return None
828	        return float(v)
829	
830	    summary = {
831	        "experiment": "plan_005_asv_extended_fixed",
832	        "topologies": ["mbias", "iv", "frontdoor"],
833	        "asv_values_tau05": {},
834	        "small_tau_asv": {},
835	        "coverage": {},
836	        "type_errors": {},
837	    }
838	    for (label, cname), vals in asv_res.items():
839	        summary["asv_values_tau05"][f"{label}_{cname}"] = {
840	            k: _f(v) for k, v in vals.items()}
841	    for (tv, label, cname), vals in small_tau_res.items():
842	        summary["small_tau_asv"][f"tau{tv}_{label}_{cname}"] = {
843	            k: _f(v) for k, v in vals.items()}
844	    for (topo, tv), vals in cov_res.items():
845	        summary["coverage"][f"{topo}_tau{tv}"] = vals
846	    for key, vals in te_res.items():
847	        summary["type_errors"]["_".join(str(x) for x in key)] = vals
848	    return summary
849	
850	
851	# ============================================================================
852	# Main
853	# ============================================================================
854	
855	if __name__ == "__main__":
856	    np.set_printoptions(precision=6, suppress=True)
857	    print("plan_005_fixed: ASV Framework Extension (C1/C2/W1/W2 fixes)")
858	    print("=" * 70)
859	    t_total = time.time()
860	
861	    print("\nPrecomputing sufficient statistics (tau=0.5)...")
862	    t0 = time.time()
863	    st_mb = precomp_mbias(MBIAS_PARAMS, N=2_000_000)
864	    tau_I_mb = plim_mbias(np.eye(K), st_mb)[1]
865	    print(f"  M-bias:     tau_DGP=0.5, plim(I)={tau_I_mb:.6f}")
866	
867	    st_iv = precomp_iv(IV_BETA, IV_PARAMS, N=2_000_000)
868	    tau_I_iv = plim_iv(np.eye(K), st_iv)
869	    print(f"  IV:         beta[1]=0.5, Wald(I)={tau_I_iv:.6f}")
870	
871	    st_fd = precomp_fd(BETA_FD, N=10_000_000)
872	    tau_I_fd = plim_fd(np.eye(K), st_fd)[1]
873	    print(f"  Front-door: plim(I)={tau_I_fd:.6f}")
874	    print(f"  Done ({time.time()-t0:.1f}s)")
875	
876	    # Part 1 skipped (passed review)
877	    # part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_I_fd)
878	
879	    # [W1/W2] Part 2 now uses plim(I) as tau_true
880	    asv_res = part2_asv_values(st_mb, st_iv, st_fd, tau_I_mb, tau_I_iv, tau_I_fd)
881	
882	    small_tau_res = part3_small_tau_asv()
883	
884	    # Part 4 skipped (passed review)
885	    cov_res = {}
886	
887	    te_res = part5_type_errors(n_mc=500, N_sample=5000)
888	
889	    print("\n" + "=" * 70)
890	    print("PART 6: Summary JSON")
891	    print("=" * 70)
892	    summary = collect_summary(asv_res, small_tau_res, cov_res, te_res)
893	    print(json.dumps(summary, indent=2, default=str))
894	
895	    print("\n" + "=" * 70)
896	    elapsed = time.time() - t_total
897	    print(f"ALL PARTS COMPLETE. Total time: {elapsed:.1f}s ({elapsed/60:.1f}min)")
898	    print("=" * 70)
899	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71858df7-3cc0-4ff2-9c0a-5541db3cfa44",
  "isSidechain": true,
  "promptId": "ef981d00-655a-40ab-b613-a59407a7199d",
  "agentId": "ac15b957449628c9b",
  "type": "user",
  "uuid": "2225b5d7-a5a1-41b2-ad39-8336c7b497da",
  "sourceToolAssistantUUID": "71858df7-3cc0-4ff2-9c0a-5541db3cfa44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "8336aaef-aca4-4681-aaf5-922c1ee2b72e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-20T16:10:41.842Z_

I've read the complete file. Here's a detailed breakdown of the key components you requested:

## 1. M-bias, IV, and Front-door plim Functions

### **plim_mbias** (lines 170-183)
- **Signature**: `plim_mbias(C, st)`
- **Parameters**: 
  - `C`: K×K confounding matrix
  - `st`: Dictionary with precomputed sufficient statistics (E_T, E_T2, E_Y, E_TY, E_DA, E_DA_T, E_DA_Y)
- **Return**: Numpy array of 4 coefficients from OLS: `[const, tau, D1_coeff, D2_coeff]`
- **Purpose**: Probability limit of OLS regression `Y ~ 1 + T + D1_A* + D2_A*` under M-bias topology

### **plim_iv** (lines 227-232)
- **Signature**: `plim_iv(C, st)`
- **Parameters**:
  - `C`: K×K confounding matrix
  - `st`: Dictionary with reduced form (RF) and first stage (FS) from precomputed data
- **Return**: Scalar float (Wald estimator) or `np.nan` if denominator is near-zero
- **Purpose**: Wald estimator = RF / FS*[1], where FS* = C @ FS. Scalar return (not array like mbias/fd)

### **plim_fd** (lines 306-319)
- **Signature**: `plim_fd(C, st)`
- **Parameters**:
  - `C`: K×K confounding matrix
  - `st`: Dictionary with E_T, E_T2, E_Y, E_TY, E_DM, E_DM_T, E_DM_Y
- **Return**: Numpy array of 4 coefficients from OLS: `[const, tau, D1_coeff, D2_coeff]`
- **Purpose**: Probability limit of OLS `Y ~ 1 + T + D1_M* + D2_M*` under front-door topology

---

## 2. Additional plim Functions Not in plan_002

**None identified.** Only these three plim functions exist. However, there are two new **fast ASV computation functions**:

### **compute_magnitude_asv_fast** (lines 406-419)
- **Signature**: `compute_magnitude_asv_fast(tau_curve, deltas, tau_true, rel_thresh=0.1)`
- **Parameters**:
  - `tau_curve`: Array of tau estimates across delta grid
  - `deltas`: Delta grid points
  - `tau_true`: Ground truth tau (from plim(I))
  - `rel_thresh`: Relative threshold (default 0.1 = 10%)
- **Return**: First delta where running max bias exceeds threshold, or `None`
- **Key Fix [C2]**: Returns `0.0` when `tau_true ~ 0` (not `None`), marking maximally fragile results

### **compute_signif_asv_fast** (lines 423-431)
- **Signature**: `compute_signif_asv_fast(tau_curve, deltas, se)`
- **Parameters**:
  - `tau_curve`: Array of plim tau values across delta grid
  - `deltas`: Delta grid points
  - `se`: Standard error from finite sample
- **Return**: First delta where `|plim_tau(delta)| < 1.96 * SE`, or `None`
- **Purpose**: Significance-based ASV rejection rule (from plan_004_v3_fixed)

---

## 3. GPU Framework Differences from plan_002

**No GPU framework is present in this script.** The script is **pure NumPy CPU-based**:
- No CUDA, PyTorch, JAX, or GPU libraries imported
- No `.to(device)`, `.cuda()`, or GPU memory management
- Uses only standard NumPy operations and `np.linalg` for linear algebra
- Precomputation uses large sample sizes (2M-10M) but on CPU via standard `np.random`

This appears to be a **CPU-only, pure-Python statistical simulation** framework.

---

## 4. Overall Script Structure

**6 Parts** (lines 438-817):

1. **Part 1: Envelope Monotonicity** (lines 438-457) — *Skipped in main, verifies monotonicity of bias curves*
2. **Part 2: ASV Values** (lines 464-493) — *Computes sign-flip and magnitude-relative ASV for tau=0.5 across C matrices [W1/W2 fix: uses plim(I) as tau_true]*
3. **Part 3: Small-tau ASV** (lines 500-550) — *Extends ASV analysis to tau=0.05, 0.1 with three thresholds (sign_flip, mag10%, mag_abs0.05)*
4. **Part 4: MC Coverage** (lines 557-657) — *Skipped in main, validates plim accuracy via finite-sample MC*
5. **Part 5: Type I/II Errors** (lines 664-817) — *Rewritten with significance-based ASV rejection rule [C1]: `reject if |tau_hat/SE|>1.96 AND (signif_ASV is None OR signif_ASV > 1)`*
6. **Part 6: Summary JSON** (lines 824-848) — *Aggregates results into JSON*

**Main Execution Flow** (lines 855-898):
- Precomputes sufficient statistics for all three topologies at tau=0.5
- **Key Fix [W1/W2]**: Extracts `tau_I = plim(I)[1]` for M-bias/front-door or `Wald(I)` for IV (these become the "true" reference for ASV, not DGP parameters)
- Runs Parts 2, 3, 5 sequentially
- Outputs JSON summary with all results

---

## Key Reviewer Fixes Applied

- **C1**: Significance-based ASV from plan_004_v3_fixed incorporated into Part 5
- **C2**: Returns 0.0 (not None) when tau_true ≈ 0 in magnitude ASV
- **W1**: IV tau_true = plim_iv(I) ≈ 0.66, not beta=0.5
- **W2**: M-bias tau_true = plim_mbias(I)[1] ≈ 0.5128, not DGP tau=0.5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2225b5d7-a5a1-41b2-ad39-8336c7b497da",
  "isSidechain": true,
  "agentId": "ac15b957449628c9b",
  "requestId": "req_011CbE7VE1MrYxr5zopBZV1y",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6de89680-4134-4425-b028-dcd5d6e67b3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "8336aaef-aca4-4681-aaf5-922c1ee2b72e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C8zCouzXEZdzE3uDPdY4DH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 16574,
      "cache_read_input_tokens": 15662,
      "output_tokens": 1622,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16574
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1622,
          "cache_read_input_tokens": 15662,
          "cache_creation_input_tokens": 16574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16574,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
