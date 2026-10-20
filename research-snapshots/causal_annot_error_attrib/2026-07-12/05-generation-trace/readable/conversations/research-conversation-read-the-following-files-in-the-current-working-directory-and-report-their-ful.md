# Research conversation: Read the following files in the current working directory and report their full contents (or as much as possible): 1. /h

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a2e40a43448a018a4.jsonl`
- **Structured JSON:** [`a456048120dbc7867268.json`](../../sessions/a4/a456048120dbc7867268.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

15 recorded events

### User

_source line 1 · 2026-05-20T21:00:39.091Z_

Read the following files in the current working directory and report their full contents (or as much as possible):

1. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_collider_mbias_iv.py
2. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_mediation_frontdoor.py
3. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_005_asv_extended.py
4. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_004_asv_framework.py (if it exists)
5. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_002_k57_extension.py (if it exists)
6. /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/memory.md

Report the full content of each file. I need to understand:
- The plim bias computation functions for each topology
- The ASV computation functions (magnitude, significance, sign_flip)
- DGP parameter conventions
- How confusion matrices are constructed and used
- The topologies list and their parameter structures

Be very thorough - read each file completely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "61d74a93-5a71-4e46-b233-0f41972ac7d7",
  "agentId": "a2e40a43448a018a4",
  "type": "user",
  "uuid": "7fecfdc2-7a2a-4484-8729-df9b63beb811",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-20T21:00:40.479Z_

I'll read all the specified files in the project directory. Let me start by reading each one.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fecfdc2-7a2a-4484-8729-df9b63beb811",
  "isSidechain": true,
  "agentId": "a2e40a43448a018a4",
  "requestId": "req_011CbEVd7vXE3TKTexjP11kn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1a16350d-6394-4a7d-a042-4b37974b1a22",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RQ1FLWennpE9fQL7iZAEwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15897,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15897,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 3 · 2026-05-20T21:00:40.697Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Up1jUceWPTD2NNFPfubW7g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_collider_mbias_iv.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a16350d-6394-4a7d-a042-4b37974b1a22",
  "isSidechain": true,
  "agentId": "a2e40a43448a018a4",
  "requestId": "req_011CbEVd7vXE3TKTexjP11kn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "077e0097-60dd-4bb3-85c8-9c28b66a9fc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RQ1FLWennpE9fQL7iZAEwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15897,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15897,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T21:00:40.710Z_

<details><summary>↩ Tool result · `toolu_01Up1jUceWPTD2NNFPfubW7g`</summary>

```text
1	"""
2	Collider + M-bias + Instrument DAG: bias via large-sample moments + MC verification.
3	K=3 LLM annotation error bias propagation in causal inference.
4	"""
5	
6	import numpy as np
7	from collections import OrderedDict
8	import time
9	
10	# ── Constants ────────────────────────────────────────────────────────────────
11	
12	BETA_MIXED = np.array([0.0, 1.0, -0.5])
13	BETA_SAME  = np.array([0.0, 1.0,  0.5])
14	
15	C1_SYMMETRIC_HIGH = np.array([[0.80, 0.10, 0.10], [0.10, 0.80, 0.10], [0.10, 0.10, 0.80]])
16	C2_ASYMMETRIC     = np.array([[0.65, 0.05, 0.10], [0.30, 0.85, 0.10], [0.05, 0.10, 0.80]])
17	C3_STRUCTURAL_12  = np.array([[0.96, 0.01, 0.01], [0.02, 0.69, 0.30], [0.02, 0.30, 0.69]])
18	C4_WEAK_DIAG      = np.array([[0.40, 0.35, 0.25], [0.35, 0.40, 0.35], [0.25, 0.25, 0.40]])
19	C5_NEAR_PERM      = np.array([[0.05, 0.05, 0.90], [0.90, 0.05, 0.05], [0.05, 0.90, 0.05]])
20	C6_DIFF_BASE      = np.array([[0.80, 0.10, 0.10], [0.10, 0.80, 0.10], [0.10, 0.10, 0.80]])
21	
22	ALL_C = OrderedDict([
23	    ("C1_sym_high",   C1_SYMMETRIC_HIGH),
24	    ("C2_asymmetric", C2_ASYMMETRIC),
25	    ("C3_struct_12",  C3_STRUCTURAL_12),
26	    ("C4_weak_diag",  C4_WEAK_DIAG),
27	    ("C5_near_perm",  C5_NEAR_PERM),
28	    ("C6_diff_base",  C6_DIFF_BASE),
29	])
30	
31	# ── Utilities ────────────────────────────────────────────────────────────────
32	
33	def _generate_Astar(A, C, rng):
34	    probs = C[:, A]
35	    cum = np.cumsum(probs, axis=0)
36	    u = rng.uniform(size=len(A))
37	    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)
38	
39	
40	def _generate_Astar_fixed_u(A, C, u):
41	    probs = C[:, A]
42	    cum = np.cumsum(probs, axis=0)
43	    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)
44	
45	
46	def _softmax_sample(logits, rng):
47	    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))
48	    probs = exp_l / exp_l.sum(axis=1, keepdims=True)
49	    cum = np.cumsum(probs, axis=1)
50	    u = rng.uniform(size=logits.shape[0])
51	    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)
52	
53	
54	def _ols(Z, Y):
55	    return np.linalg.solve(Z.T @ Z, Z.T @ Y)
56	
57	
58	# ══════════════════════════════════════════════════════════════════════════════
59	# DAG 1: COLLIDER — T -> A <- Y
60	# ══════════════════════════════════════════════════════════════════════════════
61	
62	COLLIDER_PARAMS = dict(tau=1.0, g1=0.0, g2=0.0, dT=0.5, dY=0.8, dT2=-0.3, dY2=0.6)
63	
64	
65	def _gen_collider(N, params, rng):
66	    T = rng.normal(0, 1, N)
67	    eps = rng.normal(0, 1, N)
68	    Y = params['tau'] * T + eps
69	    logits = np.column_stack([
70	        np.zeros(N),
71	        params['g1'] + params['dT'] * T + params['dY'] * Y,
72	        params['g2'] + params['dT2'] * T + params['dY2'] * Y,
73	    ])
74	    A = _softmax_sample(logits, rng)
75	    return T, Y, A
76	
77	
78	def theory_collider(C, params, N_approx=2_000_000, seed=999):
79	    rng = np.random.default_rng(seed)
80	    T, Y, A = _gen_collider(N_approx, params, rng)
81	    Astar = _generate_Astar(A, C, rng)
82	    D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)
83	    ones = np.ones(N_approx)
84	    tau_ctrl = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]
85	    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]
86	    return tau_ctrl, tau_nc
87	
88	
89	def mc_collider(C, params, N=10_000, n_reps=1000, seed=0):
90	    tau_ctrl_arr = np.empty(n_reps)
91	    tau_nc_arr = np.empty(n_reps)
92	    for r in range(n_reps):
93	        rng = np.random.default_rng(seed + r)
94	        T, Y, A = _gen_collider(N, params, rng)
95	        Astar = _generate_Astar(A, C, rng)
96	        D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)
97	        ones = np.ones(N)
98	        tau_ctrl_arr[r] = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]
99	        tau_nc_arr[r] = _ols(np.column_stack([ones, T]), Y)[1]
100	    return tau_ctrl_arr.mean(), tau_nc_arr.mean()
101	
102	
103	# ══════════════════════════════════════════════════════════════════════════════
104	# DAG 2: M-BIAS — U1 -> {A,T}, U2 -> {A,Y}
105	# ══════════════════════════════════════════════════════════════════════════════
106	
107	MBIAS_PARAMS = dict(tau=1.0, delta=1.0, lam=1.0,
108	                    g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9)
109	
110	
111	def _gen_mbias(N, params, rng):
112	    U1 = rng.normal(0, 1, N)
113	    U2 = rng.normal(0, 1, N)
114	    T = params['delta'] * U1 + rng.normal(0, 1, N)
115	    Y = params['tau'] * T + params['lam'] * U2 + rng.normal(0, 1, N)
116	    logits = np.column_stack([
117	        np.zeros(N),
118	        params['g1'] + params['a1'] * U1 + params['a2'] * U2,
119	        params['g2'] + params['a3'] * U1 + params['a4'] * U2,
120	    ])
121	    A = _softmax_sample(logits, rng)
122	    return T, Y, A
123	
124	
125	def theory_mbias(C, params, N_approx=2_000_000, seed=999):
126	    rng = np.random.default_rng(seed)
127	    T, Y, A = _gen_mbias(N_approx, params, rng)
128	    Astar = _generate_Astar(A, C, rng)
129	    D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)
130	    ones = np.ones(N_approx)
131	    tau_ctrl = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]
132	    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]
133	    return tau_ctrl, tau_nc
134	
135	
136	def mc_mbias(C, params, N=10_000, n_reps=1000, seed=0):
137	    tau_ctrl_arr = np.empty(n_reps)
138	    tau_nc_arr = np.empty(n_reps)
139	    for r in range(n_reps):
140	        rng = np.random.default_rng(seed + r)
141	        T, Y, A = _gen_mbias(N, params, rng)
142	        Astar = _generate_Astar(A, C, rng)
143	        D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)
144	        ones = np.ones(N)
145	        tau_ctrl_arr[r] = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]
146	        tau_nc_arr[r] = _ols(np.column_stack([ones, T]), Y)[1]
147	    return tau_ctrl_arr.mean(), tau_nc_arr.mean()
148	
149	
150	# ══════════════════════════════════════════════════════════════════════════════
151	# DAG 3: INSTRUMENT — Z_iv -> A -> Y, U -> {A, Y}
152	# ══════════════════════════════════════════════════════════════════════════════
153	
154	IV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)
155	
156	
157	def _gen_iv(N, beta, params, rng):
158	    Z_iv = rng.binomial(1, 0.5, N).astype(float)
159	    U = rng.normal(0, 1, N)
160	    eps = rng.normal(0, 1, N)
161	    logits = np.column_stack([
162	        np.zeros(N),
163	        params['g1'] + params['dZ'] * Z_iv + params['dU'] * U,
164	        params['g2'] + params['dZ2'] * Z_iv + params['dU2'] * U,
165	    ])
166	    A = _softmax_sample(logits, rng)
167	    Y = (beta[1] * (A == 1).astype(float) + beta[2] * (A == 2).astype(float)
168	         + params['lam'] * U + eps)
169	    return Z_iv, U, Y, A
170	
171	
172	def theory_iv(C, beta, params, N_approx=2_000_000, seed=999):
173	    rng = np.random.default_rng(seed)
174	    Z_iv, U, Y, A = _gen_iv(N_approx, beta, params, rng)
175	    Astar = _generate_Astar(A, C, rng)
176	    z1 = Z_iv == 1
177	    z0 = Z_iv == 0
178	
179	    RF = Y[z1].mean() - Y[z0].mean()
180	
181	    result = {'RF': RF}
182	    for k in [1, 2]:
183	        fs_star = (Astar[z1] == k).mean() - (Astar[z0] == k).mean()
184	        fs_true = (A[z1] == k).mean() - (A[z0] == k).mean()
185	        result[f'FS{k}_star'] = fs_star
186	        result[f'FS{k}_true'] = fs_true
187	        result[f'Wald{k}_star'] = RF / fs_star if abs(fs_star) > 1e-8 else np.nan
188	        result[f'Wald{k}_true'] = RF / fs_true if abs(fs_true) > 1e-8 else np.nan
189	
190	    ones = np.ones(N_approx)
191	    X_star = np.column_stack([ones, (Astar == 1).astype(float), (Astar == 2).astype(float)])
192	    result['ols_star'] = _ols(X_star, Y)
193	    X_true = np.column_stack([ones, (A == 1).astype(float), (A == 2).astype(float)])
194	    result['ols_true'] = _ols(X_true, Y)
195	
196	    return result
197	
198	
199	def mc_iv(C, beta, params, N=10_000, n_reps=1000, seed=0):
200	    RF_arr = np.empty(n_reps)
201	    FS1_arr = np.empty(n_reps)
202	    FS2_arr = np.empty(n_reps)
203	    ols_arr = np.empty((n_reps, 3))
204	    for r in range(n_reps):
205	        rng = np.random.default_rng(seed + r)
206	        Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)
207	        Astar = _generate_Astar(A, C, rng)
208	        z1 = Z_iv == 1
209	        z0 = Z_iv == 0
210	        RF_arr[r] = Y[z1].mean() - Y[z0].mean()
211	        FS1_arr[r] = (Astar[z1] == 1).mean() - (Astar[z0] == 1).mean()
212	        FS2_arr[r] = (Astar[z1] == 2).mean() - (Astar[z0] == 2).mean()
213	        ones = np.ones(N)
214	        X = np.column_stack([ones, (Astar == 1).astype(float), (Astar == 2).astype(float)])
215	        ols_arr[r] = _ols(X, Y)
216	
217	    wald1_mc = RF_arr.mean() / FS1_arr.mean()
218	    wald2_mc = RF_arr.mean() / FS2_arr.mean()
219	    ols_mc = ols_arr.mean(axis=0)
220	    return wald1_mc, wald2_mc, ols_mc
221	
222	
223	# ══════════════════════════════════════════════════════════════════════════════
224	# RANDOM C SEARCH (reuse base dataset, vary only C)
225	# ══════════════════════════════════════════════════════════════════════════════
226	
227	def _fast_ols_tau(T, Y, A_star, N, sT, sTT, sY, sTY):
228	    """Inline OLS for Y ~ 1 + T + D1 + D2, returns coef on T. Avoids column_stack."""
229	    m1 = A_star == 1
230	    m2 = A_star == 2
231	    n1 = float(m1.sum())
232	    n2 = float(m2.sum())
233	    tD1 = T[m1].sum()
234	    tD2 = T[m2].sum()
235	    yD1 = Y[m1].sum()
236	    yD2 = Y[m2].sum()
237	    ZZ = np.array([[N, sT, n1, n2],
238	                   [sT, sTT, tD1, tD2],
239	                   [n1, tD1, n1, 0.0],
240	                   [n2, tD2, 0.0, n2]])
241	    ZY = np.array([sY, sTY, yD1, yD2])
242	    return np.linalg.solve(ZZ, ZY)[1]
243	
244	
245	def rand_search_collider(n_search=100_000, N_ap=50_000, seed=42):
246	    rng = np.random.default_rng(seed)
247	    T, Y, A = _gen_collider(N_ap, COLLIDER_PARAMS, rng)
248	    u = rng.uniform(size=N_ap)
249	    N = float(N_ap)
250	    sT, sTT, sY, sTY = T.sum(), (T*T).sum(), Y.sum(), (T*Y).sum()
251	    tau_nc = sTY / sTT - sT * sY / (N * sTT)  # simplified no-control
252	    ones = np.ones(N_ap)
253	    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]
254	
255	    rng_s = np.random.default_rng(seed + 1)
256	    biases = np.empty(n_search)
257	    for i in range(n_search):
258	        C = rng_s.dirichlet([1, 1, 1], size=3).T
259	        Astar = _generate_Astar_fixed_u(A, C, u)
260	        biases[i] = _fast_ols_tau(T, Y, Astar, N, sT, sTT, sY, sTY) - COLLIDER_PARAMS['tau']
261	    return biases, tau_nc - COLLIDER_PARAMS['tau']
262	
263	
264	def rand_search_mbias(n_search=100_000, N_ap=50_000, seed=42):
265	    rng = np.random.default_rng(seed)
266	    T, Y, A = _gen_mbias(N_ap, MBIAS_PARAMS, rng)
267	    u = rng.uniform(size=N_ap)
268	    N = float(N_ap)
269	    sT, sTT, sY, sTY = T.sum(), (T*T).sum(), Y.sum(), (T*Y).sum()
270	    ones = np.ones(N_ap)
271	    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]
272	
273	    rng_s = np.random.default_rng(seed + 1)
274	    biases = np.empty(n_search)
275	    for i in range(n_search):
276	        C = rng_s.dirichlet([1, 1, 1], size=3).T
277	        Astar = _generate_Astar_fixed_u(A, C, u)
278	        biases[i] = _fast_ols_tau(T, Y, Astar, N, sT, sTT, sY, sTY) - MBIAS_PARAMS['tau']
279	    return biases, tau_nc - MBIAS_PARAMS['tau']
280	
281	
282	def rand_search_iv(beta, n_search=100_000, N_ap=50_000, seed=42):
283	    rng = np.random.default_rng(seed)
284	    Z_iv, U, Y, A = _gen_iv(N_ap, beta, IV_PARAMS, rng)
285	    u = rng.uniform(size=N_ap)
286	    z1 = Z_iv == 1
287	    z0 = Z_iv == 0
288	    n1_z = float(z1.sum())
289	    n0_z = float(z0.sum())
290	    RF = Y[z1].sum() / n1_z - Y[z0].sum() / n0_z
291	    FS1_true = (A[z1] == 1).sum() / n1_z - (A[z0] == 1).sum() / n0_z
292	    FS2_true = (A[z1] == 2).sum() / n1_z - (A[z0] == 2).sum() / n0_z
293	    W1_true = RF / FS1_true if abs(FS1_true) > 1e-8 else np.nan
294	    W2_true = RF / FS2_true if abs(FS2_true) > 1e-8 else np.nan
295	
296	    rng_s = np.random.default_rng(seed + 1)
297	    w1_vals = np.empty(n_search)
298	    w2_vals = np.empty(n_search)
299	    for i in range(n_search):
300	        C = rng_s.dirichlet([1, 1, 1], size=3).T
301	        Astar = _generate_Astar_fixed_u(A, C, u)
302	        fs1 = (Astar[z1] == 1).sum() / n1_z - (Astar[z0] == 1).sum() / n0_z
303	        fs2 = (Astar[z1] == 2).sum() / n1_z - (Astar[z0] == 2).sum() / n0_z
304	        w1_vals[i] = RF / fs1 if abs(fs1) > 1e-8 else np.nan
305	        w2_vals[i] = RF / fs2 if abs(fs2) > 1e-8 else np.nan
306	    return w1_vals, w2_vals, W1_true, W2_true
307	
308	
309	# ══════════════════════════════════════════════════════════════════════════════
310	# MAIN
311	# ══════════════════════════════════════════════════════════════════════════════
312	
313	def _print_section(title):
314	    print()
315	    print("=" * 80)
316	    print(title)
317	    print("=" * 80)
318	
319	
320	def main():
321	    np.set_printoptions(precision=6, suppress=True)
322	    t0 = time.time()
323	
324	    # ── DAG 1: Collider ─────────────────────────────────────────────────────
325	    _print_section("DAG 1: COLLIDER -- T -> A <- Y")
326	    p = COLLIDER_PARAMS
327	    print(f"DGP: T~N(0,1), Y={p['tau']}*T+eps, "
328	          f"A|T,Y softmax(dT={p['dT']}, dY={p['dY']}, dT2={p['dT2']}, dY2={p['dY2']})")
329	    print(f"Researcher error: controls A* in Y ~ 1 + T + D*1 + D*2")
330	    print(f"Truth: T and Y are NOT confounded => no-control OLS is consistent")
331	    print()
332	
333	    hdr = (f"  {'C':<16} {'Th t_ctrl':>10} {'MC t_ctrl':>10} {'OK':>3}"
334	           f" {'tau':>5} {'Bias_ctrl':>10} {'Th t_nc':>9} {'Bias_nc':>9}")
335	    print(hdr)
336	    print("  " + "-" * 80)
337	
338	    for cn, C in ALL_C.items():
339	        th_c, th_n = theory_collider(C, p)
340	        mc_c, mc_n = mc_collider(C, p)
341	        ok = "Y" if abs(th_c - mc_c) < 0.02 else "N"
342	        print(f"  {cn:<16} {th_c:>10.4f} {mc_c:>10.4f} {ok:>3}"
343	              f" {p['tau']:>5.1f} {th_c - p['tau']:>+10.4f} {th_n:>9.4f} {th_n - p['tau']:>+9.4f}")
344	
345	    print()
346	    print("Violation analysis:")
347	    th_c1, th_n1 = theory_collider(C1_SYMMETRIC_HIGH, p)
348	    print(f"  No-control plim(tau_hat) = {th_n1:.4f}"
349	          f" (should = tau={p['tau']} since no confounding)")
350	    print(f"  Controlling collider A* induces spurious T-eps association")
351	
352	    t1 = time.time()
353	    print(f"\nRandom C search (100k)... ", end="", flush=True)
354	    bc, bnc = rand_search_collider()
355	    print(f"done ({time.time()-t1:.0f}s)")
356	    print(f"  No-control bias: {bnc:+.4f}")
357	    print(f"  Control bias: mean={bc.mean():+.4f}, std={bc.std():.4f},"
358	          f" range=[{bc.min():+.4f}, {bc.max():+.4f}]")
359	    worse = np.sum(np.abs(bc) > np.abs(bnc))
360	    print(f"  |bias_ctrl| > |bias_nc|: {worse}/{len(bc)} ({100*worse/len(bc):.1f}%)")
361	
362	    # ── DAG 2: M-bias ───────────────────────────────────────────────────────
363	    _print_section("DAG 2: M-BIAS -- U1 -> {A,T}, U2 -> {A,Y}")
364	    p = MBIAS_PARAMS
365	    print(f"DGP: U1,U2~N(0,1) indep, T={p['delta']}*U1+eta,"
366	          f" Y={p['tau']}*T+{p['lam']}*U2+eps")
367	    print(f"A|U1,U2 softmax(a1={p['a1']}, a2={p['a2']}, a3={p['a3']}, a4={p['a4']})")
368	    print(f"Researcher error: controls A* => opens U1->A<-U2 path (M-bias)")
369	    print(f"Truth: U2 indep T => no confounding of T->Y, no-control is consistent")
370	    print()
371	
372	    hdr = (f"  {'C':<16} {'Th t_ctrl':>10} {'MC t_ctrl':>10} {'OK':>3}"
373	           f" {'tau':>5} {'Bias_ctrl':>10} {'Th t_nc':>9} {'Bias_nc':>9}")
374	    print(hdr)
375	    print("  " + "-" * 80)
376	
377	    for cn, C in ALL_C.items():
378	        th_c, th_n = theory_mbias(C, p)
379	        mc_c, mc_n = mc_mbias(C, p)
380	        ok = "Y" if abs(th_c - mc_c) < 0.02 else "N"
381	        print(f"  {cn:<16} {th_c:>10.4f} {mc_c:>10.4f} {ok:>3}"
382	              f" {p['tau']:>5.1f} {th_c - p['tau']:>+10.4f} {th_n:>9.4f} {th_n - p['tau']:>+9.4f}")
383	
384	    print()
385	    print("Violation analysis:")
386	    th_c1, th_n1 = theory_mbias(C1_SYMMETRIC_HIGH, p)
387	    print(f"  No-control plim(tau_hat) = {th_n1:.4f}"
388	          f" (should = tau={p['tau']} since U2 indep T)")
389	    print(f"  Controlling A* opens M-bias path: T <- U1 -> A <- U2 -> Y")
390	
391	    t1 = time.time()
392	    print(f"\nRandom C search (100k)... ", end="", flush=True)
393	    bc, bnc = rand_search_mbias()
394	    print(f"done ({time.time()-t1:.0f}s)")
395	    print(f"  No-control bias: {bnc:+.4f}")
396	    print(f"  Control bias: mean={bc.mean():+.4f}, std={bc.std():.4f},"
397	          f" range=[{bc.min():+.4f}, {bc.max():+.4f}]")
398	    worse = np.sum(np.abs(bc) > np.abs(bnc))
399	    print(f"  |bias_ctrl| > |bias_nc|: {worse}/{len(bc)} ({100*worse/len(bc):.1f}%)")
400	
401	    # ── DAG 3: Instrument ────────────────────────────────────────────────────
402	    for bname, beta in [("BETA_MIXED", BETA_MIXED), ("BETA_SAME", BETA_SAME)]:
403	        _print_section(
404	            f"DAG 3: INSTRUMENT -- Z->A->Y, U->{{A,Y}}  [{bname}: b={beta}]")
405	        p = IV_PARAMS
406	        print(f"DGP: Z~Bern(0.5), U~N(0,1), Y=b1*D1+b2*D2+{p['lam']}*U+eps")
407	        print(f"A|Z,U softmax(dZ={p['dZ']}, dU={p['dU']}, dZ2={p['dZ2']}, dU2={p['dU2']})")
408	        print(f"Under-identified: 1 IV for 2 endogenous dummies => per-dummy Wald")
409	        print(f"Wald_k = RF/FS*_k estimates (b1*pi1+b2*pi2)/pi*_k, not b_k")
410	        print()
411	
412	        hdr2 = (f"  {'C':<16}"
413	                f" {'W1* th':>8} {'W1* mc':>8} {'ok':>3}"
414	                f" {'W2* th':>8} {'W2* mc':>8} {'ok':>3}"
415	                f" {'OLS b1':>8} {'mc':>8} {'ok':>3}"
416	                f" {'OLS b2':>8} {'mc':>8} {'ok':>3}")
417	        print(hdr2)
418	        print("  " + "-" * 110)
419	
420	        for cn, C in ALL_C.items():
421	            th = theory_iv(C, beta, p)
422	            mc_w1, mc_w2, mc_ols = mc_iv(C, beta, p)
423	
424	            o1 = "Y" if abs(th['Wald1_star'] - mc_w1) < 0.10 else "N"
425	            o2 = "Y" if abs(th['Wald2_star'] - mc_w2) < 0.10 else "N"
426	            o3 = "Y" if abs(th['ols_star'][1] - mc_ols[1]) < 0.02 else "N"
427	            o4 = "Y" if abs(th['ols_star'][2] - mc_ols[2]) < 0.02 else "N"
428	
429	            def _fmt(v, w=8):
430	                return f"{v:>{w}.4f}" if np.isfinite(v) else f"{'nan':>{w}}"
431	
432	            print(f"  {cn:<16}"
433	                  f" {_fmt(th['Wald1_star'])} {_fmt(mc_w1)} {o1:>3}"
434	                  f" {_fmt(th['Wald2_star'])} {_fmt(mc_w2)} {o2:>3}"
435	                  f" {th['ols_star'][1]:>8.4f} {mc_ols[1]:>8.4f} {o3:>3}"
436	                  f" {th['ols_star'][2]:>8.4f} {mc_ols[2]:>8.4f} {o4:>3}")
437	
438	        print()
439	        th1 = theory_iv(C1_SYMMETRIC_HIGH, beta, p)
440	        print("Violation analysis (C1_sym_high):")
441	        print(f"  True beta = [{beta[1]}, {beta[2]}]")
442	        print(f"  Reduced form (ITT): {th1['RF']:.4f}")
443	        print(f"  First stage true:  pi1={th1['FS1_true']:.4f}, pi2={th1['FS2_true']:.4f}")
444	        print(f"  First stage A*:    pi*1={th1['FS1_star']:.4f}, pi*2={th1['FS2_star']:.4f}")
445	        print(f"  Wald true A:  W1={th1['Wald1_true']:.4f}, W2={th1['Wald2_true']:.4f}")
446	        print(f"  Wald A*:      W1={th1['Wald1_star']:.4f}, W2={th1['Wald2_star']:.4f}")
447	        print(f"  OLS true A:   [{th1['ols_true'][1]:.4f}, {th1['ols_true'][2]:.4f}]"
448	              f" (biased by U)")
449	        print(f"  OLS A*:       [{th1['ols_star'][1]:.4f}, {th1['ols_star'][2]:.4f}]"
450	              f" (biased by U + misclassification)")
451	
452	        # Analytical insight: how C transforms first stages
453	        print(f"\n  FS transformation by C:")
454	        print(f"    FS*_k = sum_j C[k,j] * FS_j")
455	        for cn2, C2 in [("C1_sym_high", C1_SYMMETRIC_HIGH),
456	                        ("C4_weak_diag", C4_WEAK_DIAG),
457	                        ("C5_near_perm", C5_NEAR_PERM)]:
458	            th2 = theory_iv(C2, beta, p)
459	            fs_true = np.array([-(th2['FS1_true']+th2['FS2_true']),
460	                                th2['FS1_true'], th2['FS2_true']])
461	            fs_star_calc = C2 @ fs_true
462	            print(f"    {cn2}: FS_true={fs_true}, C@FS={fs_star_calc},"
463	                  f" FS*=[{th2['FS1_star']:.4f}, {th2['FS2_star']:.4f}]")
464	
465	        t1 = time.time()
466	        print(f"\n  Random C search (100k)... ", end="", flush=True)
467	        w1v, w2v, w1t, w2t = rand_search_iv(beta)
468	        print(f"done ({time.time()-t1:.0f}s)")
469	        v1 = np.isfinite(w1v)
470	        v2 = np.isfinite(w2v)
471	        w1b = w1v - w1t
472	        w2b = w2v - w2t
473	        print(f"    Wald1 true={w1t:.4f}: A* vals mean={np.nanmean(w1v):+.4f},"
474	              f" std={np.nanstd(w1v):.4f},"
475	              f" range=[{np.nanmin(w1v):+.4f}, {np.nanmax(w1v):+.4f}],"
476	              f" valid={v1.sum()}/{len(w1v)}")
477	        print(f"    Wald2 true={w2t:.4f}: A* vals mean={np.nanmean(w2v):+.4f},"
478	              f" std={np.nanstd(w2v):.4f},"
479	              f" range=[{np.nanmin(w2v):+.4f}, {np.nanmax(w2v):+.4f}],"
480	              f" valid={v2.sum()}/{len(w2v)}")
481	        print(f"    Delta from true: W1 mean={np.nanmean(w1b):+.4f},"
482	              f" W2 mean={np.nanmean(w2b):+.4f}")
483	
484	    print(f"\nTotal: {time.time() - t0:.1f}s")
485	
486	
487	if __name__ == "__main__":
488	    main()
489	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "077e0097-60dd-4bb3-85c8-9c28b66a9fc2",
  "isSidechain": true,
  "promptId": "61d74a93-5a71-4e46-b233-0f41972ac7d7",
  "agentId": "a2e40a43448a018a4",
  "type": "user",
  "uuid": "4905d61d-481b-4208-b9e0-be167bf81e2c",
  "sourceToolAssistantUUID": "077e0097-60dd-4bb3-85c8-9c28b66a9fc2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T21:00:40.911Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LzwoUJu5qNDZULnSH5ffL8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_mediation_frontdoor.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4905d61d-481b-4208-b9e0-be167bf81e2c",
  "isSidechain": true,
  "agentId": "a2e40a43448a018a4",
  "requestId": "req_011CbEVd7vXE3TKTexjP11kn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9a464f9a-ef0b-436c-b148-f64e776e2b1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RQ1FLWennpE9fQL7iZAEwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15897,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15897,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T21:00:40.918Z_

<details><summary>↩ Tool result · `toolu_01LzwoUJu5qNDZULnSH5ffL8`</summary>

```text
1	#!/usr/bin/env python3
2	# -*- coding: utf-8 -*-
3	"""Plan 001: Mediation + Front-door DAG — closed-form bias + MC verification."""
4	import numpy as np
5	import time
6	import warnings
7	from collections import OrderedDict
8	
9	warnings.filterwarnings('ignore')
10	
11	# ================================================================
12	# Configuration
13	# ================================================================
14	K = 3
15	N_MC = 10_000
16	N_REPS = 1_000
17	N_LARGE = 50_000_000
18	N_RANDOM = 100_000
19	
20	BETA_MIXED = np.array([0.0, 1.0, -0.5])
21	BETA_SAME  = np.array([0.0, 1.0,  0.5])
22	
23	TAU = 0.5
24	GAMMA_MED = np.array([0.0, 0.5, -0.3])
25	DELTA_MED = np.array([0.0, 0.8, -0.6])
26	
27	ALPHA_U = 1.0
28	LAMBDA_U = 1.0
29	GAMMA_FD = np.array([0.0, 0.5, -0.3])
30	DELTA_FD = np.array([0.0, 1.0, -0.8])
31	
32	C_DICT = OrderedDict([
33	    ("1_sym_high",   np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]])),
34	    ("2_asymmetric", np.array([[.65,.05,.10],[.30,.85,.10],[.05,.10,.80]])),
35	    ("3_struct_12",  np.array([[.96,.01,.01],[.02,.69,.30],[.02,.30,.69]])),
36	    ("4_weak_diag",  np.array([[.40,.35,.25],[.35,.40,.35],[.25,.25,.40]])),
37	    ("5_near_perm",  np.array([[.05,.05,.90],[.90,.05,.05],[.05,.90,.05]])),
38	    ("6_diff_base",  np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]])),
39	])
40	
41	COEF_NAMES = ['β₀', 'τ', 'β₁', 'β₂']
42	
43	
44	# ================================================================
45	# Helpers
46	# ================================================================
47	def softmax(x):
48	    e = np.exp(x - x.max())
49	    return e / e.sum()
50	
51	
52	def p_cat(t, g, d):
53	    return softmax(g + d * t)
54	
55	
56	def gen_Astar(A, C, rng):
57	    pr = C[:, A]
58	    cu = np.cumsum(pr, axis=0)
59	    u = rng.uniform(size=len(A))
60	    return (u >= cu[0]).astype(int) + (u >= cu[1]).astype(int)
61	
62	
63	def ols(Z, Y):
64	    return np.linalg.lstsq(Z, Y, rcond=None)[0]
65	
66	
67	def fv(v, w=8, p=4):
68	    return '[' + ' '.join(f'{x:>{w}.{p}f}' for x in v) + ']'
69	
70	
71	def fm(th, mc, se, k=2):
72	    ok = np.abs(mc - th) < k * se
73	    return ''.join('✓' if o else '✗' for o in ok), ok.all()
74	
75	
76	# ================================================================
77	# DAG 1  Mediation: T -> A -> Y
78	#
79	# DGP:  T ~ Bern(0.5)
80	#        A | T ~ Cat(softmax(gamma + delta*T))
81	#        Y = beta0 + beta1*D1 + beta2*D2 + tau*T + eps
82	#        A* | A ~ Cat(C[:, A])
83	#
84	# Researcher regression:  Y ~ 1 + T + D*_1 + D*_2
85	#
86	# Z = (1, T, D*_1, D*_2),  X = (1, T, D_1, D_2)
87	# eps indep of Z  =>  plim = (E[Z'Z])^{-1} E[Z'X] beta
88	#
89	# Key moments:
90	#   q_t = C @ p_{A|T=t}           (P(A*|T=t))
91	#   q_marg = 0.5*(q_0 + q_1)
92	#   E[D*_j * D_k] = C[j,k] * p_marg[k]
93	# ================================================================
94	def plim_med(C, beta, tau, g=GAMMA_MED, d=DELTA_MED):
95	    p0, p1 = p_cat(0, g, d), p_cat(1, g, d)
96	    q0, q1 = C @ p0, C @ p1
97	    pm = .5 * (p0 + p1)
98	    qm = .5 * (q0 + q1)
99	
100	    EZZ = np.array([
101	        [1,      .5,        qm[1],      qm[2]     ],
102	        [.5,     .5,        .5*q1[1],   .5*q1[2]  ],
103	        [qm[1],  .5*q1[1],  qm[1],      0         ],
104	        [qm[2],  .5*q1[2],  0,          qm[2]     ]])
105	
106	    EZX = np.array([
107	        [1,      .5,        pm[1],            pm[2]           ],
108	        [.5,     .5,        .5*p1[1],         .5*p1[2]        ],
109	        [qm[1],  .5*q1[1],  C[1,1]*pm[1],    C[1,2]*pm[2]   ],
110	        [qm[2],  .5*q1[2],  C[2,1]*pm[1],    C[2,2]*pm[2]   ]])
111	
112	    b = np.array([beta[0], tau, beta[1], beta[2]])
113	    return np.linalg.solve(EZZ, EZX @ b)
114	
115	
116	def mc_med(C, beta, tau, g=GAMMA_MED, d=DELTA_MED,
117	           nr=N_REPS, N=N_MC, seed=42):
118	    rng = np.random.default_rng(seed)
119	    p0, p1 = p_cat(0, g, d), p_cat(1, g, d)
120	    out = np.zeros((nr, 4))
121	    for r in range(nr):
122	        T = rng.binomial(1, .5, N)
123	        pr = np.where(T[:, None] == 0, p0, p1)
124	        cu = np.cumsum(pr, axis=1)
125	        u = rng.uniform(size=N)
126	        A = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)
127	        D1 = (A == 1).astype(float)
128	        D2 = (A == 2).astype(float)
129	        Y = beta[0] + beta[1]*D1 + beta[2]*D2 + tau*T + rng.normal(0, 1, N)
130	        As = gen_Astar(A, C, rng)
131	        Z = np.column_stack([np.ones(N), T.astype(float),
132	                             (As == 1).astype(float), (As == 2).astype(float)])
133	        out[r] = ols(Z, Y)
134	    return out.mean(0), out.std(0) / np.sqrt(nr)
135	
136	
137	def rsearch_med(beta, tau, g=GAMMA_MED, d=DELTA_MED,
138	                ns=N_RANDOM, seed=999):
139	    rng = np.random.default_rng(seed)
140	    p0, p1 = p_cat(0, g, d), p_cat(1, g, d)
141	    pm = .5 * (p0 + p1)
142	    b = np.array([beta[0], tau, beta[1], beta[2]])
143	    clean = plim_med(np.eye(K), beta, tau, g, d)
144	
145	    Cs = np.zeros((ns, K, K))
146	    for i in range(K):
147	        Cs[:, :, i] = rng.dirichlet(np.ones(K), size=ns)
148	
149	    q0 = Cs @ p0
150	    q1 = Cs @ p1
151	    qm = .5 * (q0 + q1)
152	
153	    EZZ = np.zeros((ns, 4, 4))
154	    EZZ[:, 0, 0] = 1;       EZZ[:, 0, 1] = EZZ[:, 1, 0] = .5
155	    EZZ[:, 0, 2] = EZZ[:, 2, 0] = qm[:, 1]
156	    EZZ[:, 0, 3] = EZZ[:, 3, 0] = qm[:, 2]
157	    EZZ[:, 1, 1] = .5
158	    EZZ[:, 1, 2] = EZZ[:, 2, 1] = .5 * q1[:, 1]
159	    EZZ[:, 1, 3] = EZZ[:, 3, 1] = .5 * q1[:, 2]
160	    EZZ[:, 2, 2] = qm[:, 1]
161	    EZZ[:, 3, 3] = qm[:, 2]
162	
163	    EZX = np.zeros((ns, 4, 4))
164	    EZX[:, 0, 0] = 1;       EZX[:, 0, 1] = .5
165	    EZX[:, 0, 2] = pm[1];   EZX[:, 0, 3] = pm[2]
166	    EZX[:, 1, 0] = .5;      EZX[:, 1, 1] = .5
167	    EZX[:, 1, 2] = .5 * p1[1]; EZX[:, 1, 3] = .5 * p1[2]
168	    EZX[:, 2, 0] = qm[:, 1];   EZX[:, 2, 1] = .5 * q1[:, 1]
169	    EZX[:, 2, 2] = Cs[:, 1, 1] * pm[1]; EZX[:, 2, 3] = Cs[:, 1, 2] * pm[2]
170	    EZX[:, 3, 0] = qm[:, 2];   EZX[:, 3, 1] = .5 * q1[:, 2]
171	    EZX[:, 3, 2] = Cs[:, 2, 1] * pm[1]; EZX[:, 3, 3] = Cs[:, 2, 2] * pm[2]
172	
173	    rhs = np.einsum('nij,j->ni', EZX, b)
174	    pl = np.linalg.solve(EZZ, rhs[:, :, None])[:, :, 0]
175	
176	    df = np.abs(pl - clean)
177	    viol = np.any(df > .01, 1).mean()
178	    nz = np.abs(clean) > 1e-6
179	    sign = np.any(np.sign(pl[:, nz]) != np.sign(clean[nz]), 1).mean()
180	    amp = np.any(np.abs(pl) > np.abs(clean) + 1e-6, 1).mean()
181	    return viol, sign, amp
182	
183	
184	# ================================================================
185	# DAG 2  Front-door: T -> M -> Y,  U -> T,  U -> Y
186	#
187	# DGP:  U ~ N(0,1)
188	#        T = alpha_U * U + eta,  eta ~ N(0,1)
189	#        M | T ~ Cat(softmax(gamma + delta*T))
190	#        Y = beta1*D_{M,1} + beta2*D_{M,2} + lambda*U + eps
191	#        M* | M ~ Cat(C[:, M])
192	#
193	# Researcher regression:  Y ~ 1 + T + D*_{M,1} + D*_{M,2}
194	#
195	# T correlated with U (confounding), so E[Z'(lambda*U)] != 0.
196	# Use large-sample moment approximation:
197	#   plim = (E[Z'Z])^{-1} E[Z'Y]   estimated from N_LARGE samples.
198	#
199	# For fast random search, pre-compute sufficient statistics:
200	#   E[D_{M,k}], E[D_{M,k}*T], E[D_{M,k}*Y]  for k=0,1,2
201	# Then for any C:
202	#   E[D*_j] = sum_k C[j,k]*E[D_{M,k}]   etc.
203	# ================================================================
204	def _gen_fd(N, beta, rng, g=GAMMA_FD, d=DELTA_FD,
205	            aU=ALPHA_U, lU=LAMBDA_U):
206	    U = rng.normal(0, 1, N)
207	    T = aU * U + rng.normal(0, 1, N)
208	    lo = np.column_stack([np.zeros(N), g[1] + d[1]*T, g[2] + d[2]*T])
209	    lo -= lo.max(1, keepdims=True)
210	    e = np.exp(lo)
211	    p = e / e.sum(1, keepdims=True)
212	    cu = np.cumsum(p, axis=1)
213	    u = rng.uniform(size=N)
214	    M = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)
215	    DM1 = (M == 1).astype(float)
216	    DM2 = (M == 2).astype(float)
217	    Y = beta[1]*DM1 + beta[2]*DM2 + lU*U + rng.normal(0, 1, N)
218	    return T, M, Y, U
219	
220	
221	def precomp_fd(beta, N=N_LARGE, seed=123):
222	    rng = np.random.default_rng(seed)
223	    T, M, Y, _ = _gen_fd(N, beta, rng)
224	    DM = np.zeros((N, K))
225	    for k in range(K):
226	        DM[:, k] = (M == k).astype(float)
227	    return dict(
228	        E_T=T.mean(), E_T2=(T**2).mean(),
229	        E_Y=Y.mean(), E_TY=(T*Y).mean(),
230	        E_DM=DM.mean(0),
231	        E_DM_T=(DM * T[:, None]).mean(0),
232	        E_DM_Y=(DM * Y[:, None]).mean(0))
233	
234	
235	def plim_fd(C, st):
236	    ds  = C @ st['E_DM']
237	    dst = C @ st['E_DM_T']
238	    dsy = C @ st['E_DM_Y']
239	    ET, ET2 = st['E_T'], st['E_T2']
240	    EY, ETY = st['E_Y'], st['E_TY']
241	
242	    EZZ = np.array([
243	        [1,      ET,      ds[1],    ds[2]   ],
244	        [ET,     ET2,     dst[1],   dst[2]  ],
245	        [ds[1],  dst[1],  ds[1],    0       ],
246	        [ds[2],  dst[2],  0,        ds[2]   ]])
247	
248	    EZY = np.array([EY, ETY, dsy[1], dsy[2]])
249	    return np.linalg.solve(EZZ, EZY)
250	
251	
252	def mc_fd(C, beta, nr=N_REPS, N=N_MC, seed=42):
253	    rng = np.random.default_rng(seed)
254	    out = np.zeros((nr, 4))
255	    for r in range(nr):
256	        T, M, Y, _ = _gen_fd(N, beta, rng)
257	        Ms = gen_Astar(M, C, rng)
258	        Z = np.column_stack([np.ones(N), T,
259	                             (Ms == 1).astype(float),
260	                             (Ms == 2).astype(float)])
261	        out[r] = ols(Z, Y)
262	    return out.mean(0), out.std(0) / np.sqrt(nr)
263	
264	
265	def rsearch_fd(st, ns=N_RANDOM, seed=999):
266	    rng = np.random.default_rng(seed)
267	    clean = plim_fd(np.eye(K), st)
268	
269	    Cs = np.zeros((ns, K, K))
270	    for i in range(K):
271	        Cs[:, :, i] = rng.dirichlet(np.ones(K), size=ns)
272	
273	    E_DMs   = Cs @ st['E_DM']
274	    E_DMs_T = Cs @ st['E_DM_T']
275	    E_DMs_Y = Cs @ st['E_DM_Y']
276	    ET, ET2 = st['E_T'], st['E_T2']
277	    EY, ETY = st['E_Y'], st['E_TY']
278	
279	    EZZ = np.zeros((ns, 4, 4))
280	    EZZ[:, 0, 0] = 1;       EZZ[:, 0, 1] = EZZ[:, 1, 0] = ET
281	    EZZ[:, 0, 2] = EZZ[:, 2, 0] = E_DMs[:, 1]
282	    EZZ[:, 0, 3] = EZZ[:, 3, 0] = E_DMs[:, 2]
283	    EZZ[:, 1, 1] = ET2
284	    EZZ[:, 1, 2] = EZZ[:, 2, 1] = E_DMs_T[:, 1]
285	    EZZ[:, 1, 3] = EZZ[:, 3, 1] = E_DMs_T[:, 2]
286	    EZZ[:, 2, 2] = E_DMs[:, 1]
287	    EZZ[:, 3, 3] = E_DMs[:, 2]
288	
289	    EZY = np.zeros((ns, 4))
290	    EZY[:, 0] = EY;   EZY[:, 1] = ETY
291	    EZY[:, 2] = E_DMs_Y[:, 1]
292	    EZY[:, 3] = E_DMs_Y[:, 2]
293	
294	    pl = np.linalg.solve(EZZ, EZY[:, :, None])[:, :, 0]
295	
296	    df = np.abs(pl - clean)
297	    viol = np.any(df > .01, 1).mean()
298	    nz = np.abs(clean) > 1e-6
299	    sign = np.any(np.sign(pl[:, nz]) != np.sign(clean[nz]), 1).mean()
300	    amp = np.any(np.abs(pl) > np.abs(clean) + 1e-6, 1).mean()
301	    return viol, sign, amp
302	
303	
304	# ================================================================
305	# Main
306	# ================================================================
307	def main():
308	    t0 = time.time()
309	    np.set_printoptions(precision=4, suppress=True)
310	
311	    for bn, beta in [("mixed [0,1,-0.5]", BETA_MIXED),
312	                      ("same [0,1,0.5]",   BETA_SAME)]:
313	
314	        # ---- DAG 1: Mediation ----
315	        print(f"\n{'='*90}")
316	        print(f"  MEDIATION: T -> A -> Y  |  beta={bn}")
317	        print(f"{'='*90}")
318	        p0, p1 = p_cat(0, GAMMA_MED, DELTA_MED), p_cat(1, GAMMA_MED, DELTA_MED)
319	        print(f"  P(A|T=0)={fv(p0,6,3)}  P(A|T=1)={fv(p1,6,3)}  tau={TAU}")
320	        print(f"  Coefs: [{', '.join(COEF_NAMES)}]\n")
321	
322	        hdr = f"  {'C':<14} {'Theory':>36}  {'MC mean':>36}  Mt"
323	        print(hdr)
324	        print(f"  {'-'*92}")
325	
326	        all_ok = True
327	        for cn, C in C_DICT.items():
328	            th = plim_med(C, beta, TAU)
329	            mc, se = mc_med(C, beta, TAU)
330	            ms, ok = fm(th, mc, se)
331	            if not ok:
332	                all_ok = False
333	            print(f"  {cn:<14} {fv(th)}  {fv(mc)}  {ms}")
334	
335	        status = 'ALL MATCH' if all_ok else 'MISMATCH DETECTED'
336	        print(f"  >>> {status}")
337	
338	        t1 = time.time()
339	        v, s, a = rsearch_med(beta, TAU)
340	        t2 = time.time()
341	        print(f"\n  Random search ({N_RANDOM//1000}k, {t2-t1:.1f}s): "
342	              f"violation={v:.1%}  sign_flip={s:.1%}  amplification={a:.1%}")
343	
344	        # ---- DAG 2: Front-door ----
345	        print(f"\n{'='*90}")
346	        print(f"  FRONT-DOOR: T -> M -> Y, U -> T, U -> Y  |  beta={bn}")
347	        print(f"{'='*90}")
348	        print(f"  alpha_U={ALPHA_U}  lambda_U={LAMBDA_U}")
349	        print(f"  M|T softmax: gamma={GAMMA_FD}  delta={DELTA_FD}")
350	        print(f"  Coefs: [{', '.join(COEF_NAMES)}]\n")
351	
352	        t1 = time.time()
353	        st = precomp_fd(beta)
354	        t2 = time.time()
355	        print(f"  Moments pre-computed (N={N_LARGE//10**6}M, {t2-t1:.1f}s)\n")
356	
357	        hdr = f"  {'C':<14} {'Theory':>36}  {'MC mean':>36}  Mt"
358	        print(hdr)
359	        print(f"  {'-'*92}")
360	
361	        all_ok = True
362	        for cn, C in C_DICT.items():
363	            th = plim_fd(C, st)
364	            mc, se = mc_fd(C, beta)
365	            ms, ok = fm(th, mc, se, k=3)
366	            if not ok:
367	                all_ok = False
368	            print(f"  {cn:<14} {fv(th)}  {fv(mc)}  {ms}")
369	
370	        status = 'ALL MATCH (3σ)' if all_ok else 'MISMATCH DETECTED'
371	        print(f"  >>> {status}")
372	
373	        t1 = time.time()
374	        v, s, a = rsearch_fd(st)
375	        t2 = time.time()
376	        print(f"\n  Random search ({N_RANDOM//1000}k, {t2-t1:.1f}s): "
377	              f"violation={v:.1%}  sign_flip={s:.1%}  amplification={a:.1%}")
378	
379	    print(f"\n{'='*90}")
380	    print(f"  Total: {time.time()-t0:.1f}s")
381	    print(f"{'='*90}")
382	
383	
384	if __name__ == "__main__":
385	    main()
386	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9a464f9a-ef0b-436c-b148-f64e776e2b1f",
  "isSidechain": true,
  "promptId": "61d74a93-5a71-4e46-b233-0f41972ac7d7",
  "agentId": "a2e40a43448a018a4",
  "type": "user",
  "uuid": "5befa87e-5522-48ee-945d-cb79ff048f21",
  "sourceToolAssistantUUID": "9a464f9a-ef0b-436c-b148-f64e776e2b1f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T21:00:41.101Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NUYhNAfwGG4JMXp1gCswPV`</summary>

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
  "parentUuid": "5befa87e-5522-48ee-945d-cb79ff048f21",
  "isSidechain": true,
  "agentId": "a2e40a43448a018a4",
  "requestId": "req_011CbEVd7vXE3TKTexjP11kn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f140327b-9dcb-43bf-923e-cf4b5fd00787",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RQ1FLWennpE9fQL7iZAEwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15897,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15897,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T21:00:41.375Z_

<details><summary>↩ Tool result · `toolu_01NUYhNAfwGG4JMXp1gCswPV`</summary>

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
  "parentUuid": "f140327b-9dcb-43bf-923e-cf4b5fd00787",
  "isSidechain": true,
  "promptId": "61d74a93-5a71-4e46-b233-0f41972ac7d7",
  "agentId": "a2e40a43448a018a4",
  "type": "user",
  "uuid": "05becd05-1232-4dbc-8669-9b1cd926e699",
  "sourceToolAssistantUUID": "f140327b-9dcb-43bf-923e-cf4b5fd00787",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T21:00:41.536Z_

<details open><summary>🔧 Tool call — Read · `toolu_012yu7juCyXWcCDKoyp7xSgs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_004_asv_framework.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05becd05-1232-4dbc-8669-9b1cd926e699",
  "isSidechain": true,
  "agentId": "a2e40a43448a018a4",
  "requestId": "req_011CbEVd7vXE3TKTexjP11kn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "336cf65b-97b4-4315-b1c1-8fab9f627801",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RQ1FLWennpE9fQL7iZAEwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15897,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15897,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T21:00:41.545Z_

<details><summary>↩ Tool result · reported error · `toolu_012yu7juCyXWcCDKoyp7xSgs`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "336cf65b-97b4-4315-b1c1-8fab9f627801",
  "isSidechain": true,
  "promptId": "61d74a93-5a71-4e46-b233-0f41972ac7d7",
  "agentId": "a2e40a43448a018a4",
  "type": "user",
  "uuid": "2f18da17-506d-427f-bd2b-ebf702102c14",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib.",
  "sourceToolAssistantUUID": "336cf65b-97b4-4315-b1c1-8fab9f627801",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T21:00:41.754Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PP7wXHYYG8F9czyLxqk5jt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_002_k57_extension.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f18da17-506d-427f-bd2b-ebf702102c14",
  "isSidechain": true,
  "agentId": "a2e40a43448a018a4",
  "requestId": "req_011CbEVd7vXE3TKTexjP11kn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "18a0f93a-3248-44ca-88ec-2577f8bf0b2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RQ1FLWennpE9fQL7iZAEwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15897,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15897,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T21:00:41.761Z_

<details><summary>↩ Tool result · `toolu_01PP7wXHYYG8F9czyLxqk5jt`</summary>

```text
1	#!/usr/bin/env python3
2	# -*- coding: utf-8 -*-
3	"""
4	Plan 002: K={3,5,7} Bias Taxonomy Extension
5	
6	Extends plan_001's K=3 bias analysis to general K across 4 core DAG topologies.
7	For each topology x K, generates 100k random K×K confusion matrices (Dirichlet),
8	computes plim via pre-computed sufficient statistics, and reports violation/sign-flip/
9	amplification rates. Includes eigendecomposition, worst-case bounds, and sensitivity
10	heatmaps as interpretability tools.
11	
12	Input:  DGP parameters per topology (auto-generated for each K)
13	Output: Cross-K comparison tables, sensitivity heatmaps (PNG)
14	
15	Dependencies: torch (GPU), numpy, matplotlib
16	"""
17	
18	import torch
19	import numpy as np
20	import matplotlib
21	matplotlib.use('Agg')
22	import matplotlib.pyplot as plt
23	import time
24	import os
25	import sys
26	
27	# ================================================================
28	# Configuration
29	# ================================================================
30	K_VALUES = [3, 5, 7]
31	N_RANDOM = 100_000
32	N_LARGE = 5_000_000
33	SEED = 42
34	DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
35	DTYPE = torch.float64
36	OUT_DIR = os.path.dirname(os.path.abspath(__file__))
37	
38	
39	# ================================================================
40	# DGP Parameters for general K
41	# ================================================================
42	# Base coefficient pools — K=3 values match plan_001 exactly,
43	# K=5,7 extend with alternating-sign decreasing magnitudes.
44	_ALPHA_POOL  = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]
45	_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
46	_BETA_POOL   = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2]
47	_GAMMA_POOL  = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
48	_DELTA_POOL  = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]
49	_DT_POOL     = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
50	_DY_POOL     = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2]
51	
52	
53	def make_p_A(K):
54	    """Slightly imbalanced category probabilities."""
55	    if K == 3:
56	        return np.array([0.40, 0.35, 0.25])
57	    raw = np.array([1.0 / i for i in range(1, K + 1)])
58	    return raw / raw.sum()
59	
60	
61	def make_params(K):
62	    """DGP parameters for all topologies at given K."""
63	    p_A = make_p_A(K)
64	
65	    conf = dict(
66	        p_A=p_A,
67	        alpha=np.array(_ALPHA_POOL[:K-1]),
68	        beta_A=np.array(_BETA_A_POOL[:K-1]),
69	        beta_T=2.0,
70	        sigma_T=1.0,
71	    )
72	
73	    med = dict(
74	        tau=0.5,
75	        gamma=np.array(_GAMMA_POOL[:K]),
76	        delta=np.array(_DELTA_POOL[:K]),
77	        beta=np.array(_BETA_POOL[:K]),
78	    )
79	
80	    coll = dict(
81	        tau=1.0,
82	        g=np.zeros(K),
83	        dT=np.array(_DT_POOL[:K]),
84	        dY=np.array(_DY_POOL[:K]),
85	    )
86	
87	    exp = dict(
88	        beta=np.array(_BETA_POOL[:K]),
89	        p_A=p_A,
90	    )
91	
92	    return dict(confounding=conf, mediation=med, collider=coll, exposure=exp)
93	
94	
95	# ================================================================
96	# DGP Generators
97	# ================================================================
98	def _softmax_rows(logits):
99	    e = np.exp(logits - logits.max(axis=-1, keepdims=True))
100	    return e / e.sum(axis=-1, keepdims=True)
101	
102	
103	def _sample_cat(probs, rng):
104	    """Sample from row-wise categorical probabilities [N, K]."""
105	    cum = np.cumsum(probs, axis=1)
106	    u = rng.uniform(size=probs.shape[0])[:, None]
107	    return (u >= cum).sum(axis=1).astype(int)
108	
109	
110	def gen_confounding(K, N, p, rng):
111	    """A→T, A→Y, T→Y. Researcher omits true A, uses A*."""
112	    A = rng.choice(K, size=N, p=p['p_A'])
113	    D = np.zeros((N, K - 1))
114	    for j in range(K - 1):
115	        D[:, j] = (A == j + 1).astype(float)
116	    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)
117	    Y = p['beta_T'] * T + D @ p['beta_A'] + rng.normal(0, 1, N)
118	    return T, Y, A
119	
120	
121	def gen_mediation(K, N, p, rng):
122	    """T→A→Y. A mediates T's effect; researcher controls for A*."""
123	    T = rng.binomial(1, 0.5, N).astype(float)
124	    logits = p['gamma'][None, :] + p['delta'][None, :] * T[:, None]
125	    probs = _softmax_rows(logits)
126	    A = _sample_cat(probs, rng)
127	    D = np.zeros((N, K - 1))
128	    for j in range(K - 1):
129	        D[:, j] = (A == j + 1).astype(float)
130	    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau'] * T + rng.normal(0, 1, N)
131	    return T, Y, A
132	
133	
134	def gen_collider(K, N, p, rng):
135	    """T→A←Y. Controlling for collider A* opens a backdoor path."""
136	    T = rng.normal(0, 1, N)
137	    Y = p['tau'] * T + rng.normal(0, 1, N)
138	    logits = (p['g'][None, :]
139	              + p['dT'][None, :] * T[:, None]
140	              + p['dY'][None, :] * Y[:, None])
141	    probs = _softmax_rows(logits)
142	    A = _sample_cat(probs, rng)
143	    return T, Y, A
144	
145	
146	def gen_exposure(K, N, p, rng):
147	    """A→Y. A is the treatment of interest."""
148	    A = rng.choice(K, size=N, p=p['p_A'])
149	    D = np.zeros((N, K - 1))
150	    for j in range(K - 1):
151	        D[:, j] = (A == j + 1).astype(float)
152	    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)
153	    return None, Y, A
154	
155	
156	_GEN = dict(confounding=gen_confounding, mediation=gen_mediation,
157	            collider=gen_collider, exposure=gen_exposure)
158	
159	
160	# ================================================================
161	# Sufficient Statistics
162	# ================================================================
163	class SuffStats:
164	    """Pre-compute population moments from a large DGP sample.
165	
166	    Stores:
167	      p_A[k]   = P(A=k)
168	      E_Y      = E[Y]
169	      E_YD[k]  = E[Y · 1(A=k)]
170	    For topologies with T:
171	      E_T, E_T2, E_TY, E_TD[k] = E[T · 1(A=k)]
172	    """
173	
174	    def __init__(self, T, Y, A, K):
175	        self.K = K
176	        self.has_T = T is not None
177	
178	        self.p_A = np.array([(A == k).mean() for k in range(K)])
179	        self.E_Y = Y.mean()
180	        self.E_YD = np.array([(Y * (A == k)).mean() for k in range(K)])
181	
182	        if self.has_T:
183	            self.E_T = T.mean()
184	            self.E_T2 = (T ** 2).mean()
185	            self.E_TY = (T * Y).mean()
186	            self.E_TD = np.array([(T * (A == k)).mean() for k in range(K)])
187	
188	    def to_device(self, dev):
189	        self.t_p_A = torch.tensor(self.p_A, dtype=DTYPE, device=dev)
190	        self.t_E_Y = torch.tensor(self.E_Y, dtype=DTYPE, device=dev)
191	        self.t_E_YD = torch.tensor(self.E_YD, dtype=DTYPE, device=dev)
192	        if self.has_T:
193	            self.t_E_T = torch.tensor(self.E_T, dtype=DTYPE, device=dev)
194	            self.t_E_T2 = torch.tensor(self.E_T2, dtype=DTYPE, device=dev)
195	            self.t_E_TY = torch.tensor(self.E_TY, dtype=DTYPE, device=dev)
196	            self.t_E_TD = torch.tensor(self.E_TD, dtype=DTYPE, device=dev)
197	        return self
198	
199	
200	# ================================================================
201	# GPU-Batched Plim
202	# ================================================================
203	def plim_with_T(ss, C):
204	    """Batched plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}.
205	
206	    Generalizes K=3 plan_001 formula. Z* = (1, T, D*_1,...,D*_{K-1}).
207	    plim = (E[Z*'Z*])^{-1} E[Z*'Y].
208	
209	    E[Z*'Z*] and E[Z*'Y] depend on C through:
210	      q = C @ p_A              (marginal of A*)
211	      E[T·D*_j] = (C @ E_TD)[j]
212	      E[Y·D*_j] = (C @ E_YD)[j]
213	      E[D*_i·D*_j] = q[i] δ_{ij}  (A* is categorical)
214	
215	    Args:
216	        ss: SuffStats on device
217	        C:  [B, K, K] confusion matrices
218	    Returns:
219	        [B, K+1] plim coefficients
220	    """
221	    B, K = C.shape[0], ss.K
222	    dim = K + 1
223	
224	    q = C @ ss.t_p_A                   # [B, K]
225	    ct = C @ ss.t_E_TD                 # [B, K]
226	    cy = C @ ss.t_E_YD                 # [B, K]
227	
228	    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)
229	    EZZ[:, 0, 0] = 1.0
230	    EZZ[:, 0, 1] = ss.t_E_T
231	    EZZ[:, 1, 0] = ss.t_E_T
232	    EZZ[:, 1, 1] = ss.t_E_T2
233	    EZZ[:, 0, 2:] = q[:, 1:]
234	    EZZ[:, 2:, 0] = q[:, 1:]
235	    EZZ[:, 1, 2:] = ct[:, 1:]
236	    EZZ[:, 2:, 1] = ct[:, 1:]
237	    idx = torch.arange(K - 1, device=C.device)
238	    EZZ[:, idx + 2, idx + 2] = q[:, 1:]
239	
240	    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)
241	    EZY[:, 0] = ss.t_E_Y
242	    EZY[:, 1] = ss.t_E_TY
243	    EZY[:, 2:] = cy[:, 1:]
244	
245	    return torch.linalg.solve(EZZ, EZY)
246	
247	
248	def plim_exposure(ss, C):
249	    """Batched plim for Y ~ 1 + D*_1 + ... + D*_{K-1} (no T).
250	
251	    Same moment algebra as plim_with_T but without the T row/column.
252	    """
253	    B, K = C.shape[0], ss.K
254	    dim = K
255	
256	    q = C @ ss.t_p_A
257	    cy = C @ ss.t_E_YD
258	
259	    EZZ = torch.zeros(B, dim, dim, dtype=DTYPE, device=C.device)
260	    EZZ[:, 0, 0] = 1.0
261	    EZZ[:, 0, 1:] = q[:, 1:]
262	    EZZ[:, 1:, 0] = q[:, 1:]
263	    idx = torch.arange(K - 1, device=C.device)
264	    EZZ[:, idx + 1, idx + 1] = q[:, 1:]
265	
266	    EZY = torch.zeros(B, dim, dtype=DTYPE, device=C.device)
267	    EZY[:, 0] = ss.t_E_Y
268	    EZY[:, 1:] = cy[:, 1:]
269	
270	    return torch.linalg.solve(EZZ, EZY)
271	
272	
273	# ================================================================
274	# Random C Generation
275	# ================================================================
276	def gen_random_C(K, N, device, seed=SEED, min_diag=None):
277	    """Sample N column-stochastic K×K matrices via Dirichlet(1,...,1).
278	
279	    Each column independently drawn. If min_diag is set, each diagonal
280	    element is drawn from U[min_diag, 1] and the remaining mass is
281	    distributed Dirichlet among off-diagonal entries.
282	    """
283	    rng = np.random.default_rng(seed)
284	    C = np.zeros((N, K, K))
285	
286	    if min_diag is not None and min_diag > 0:
287	        for j in range(K):
288	            diag = rng.uniform(min_diag, 1.0, N)
289	            offdiag = rng.dirichlet(np.ones(K - 1), N) * (1.0 - diag)[:, None]
290	            col = np.zeros((N, K))
291	            col[:, j] = diag
292	            idx = 0
293	            for i in range(K):
294	                if i != j:
295	                    col[:, i] = offdiag[:, idx]
296	                    idx += 1
297	            C[:, :, j] = col
298	    else:
299	        for j in range(K):
300	            C[:, :, j] = rng.dirichlet(np.ones(K), N)
301	
302	    return torch.tensor(C, dtype=DTYPE, device=device)
303	
304	
305	# ================================================================
306	# Metrics
307	# ================================================================
308	def compute_metrics(plim_batch, plim_true, tau_idx=None):
309	    """Violation / sign-flip / amplification rates.
310	
311	    tau_idx: index of τ coefficient (1 for topologies with T, None for exposure).
312	    """
313	    diff = plim_batch - plim_true.unsqueeze(0)
314	
315	    violation = (diff.abs() > 1e-8).any(dim=1).float().mean().item()
316	
317	    s0 = torch.sign(plim_true).unsqueeze(0)
318	    s1 = torch.sign(plim_batch)
319	    sign_flip = ((s0 != s1) & (s0 != 0) & (s1 != 0)).any(dim=1).float().mean().item()
320	
321	    amplification = (plim_batch.abs() > plim_true.abs().unsqueeze(0) + 1e-10
322	                     ).any(dim=1).float().mean().item()
323	
324	    m = dict(violation=violation, sign_flip=sign_flip, amplification=amplification)
325	
326	    if tau_idx is not None:
327	        tb = plim_batch[:, tau_idx]
328	        tt = plim_true[tau_idx]
329	        td = tb - tt
330	        m['tau_violation'] = (td.abs() > 1e-8).float().mean().item()
331	        m['tau_sign_flip'] = ((torch.sign(tb) != torch.sign(tt)) &
332	                              (torch.sign(tt) != 0) &
333	                              (torch.sign(tb) != 0)).float().mean().item()
334	        m['tau_amplification'] = (tb.abs() > tt.abs() + 1e-10).float().mean().item()
335	        m['tau_bias_mean'] = td.mean().item()
336	        m['tau_bias_std'] = td.std().item()
337	        m['tau_bias_max'] = td.abs().max().item()
338	    return m
339	
340	
341	# ================================================================
342	# MC Verification (small-scale, a few named C matrices)
343	# ================================================================
344	def mc_verify(K, topo, params, C_np, n_reps=500, n_mc=10_000, seed=0):
345	    """Monte Carlo OLS estimate of plim for a single C, as validation."""
346	    gen_fn = _GEN[topo]
347	    coefs = []
348	    for r in range(n_reps):
349	        rng = np.random.default_rng(seed + r)
350	        T, Y, A = gen_fn(K, n_mc, params, rng)
351	
352	        # Misclassify
353	        probs = C_np[:, A]       # [K, N]
354	        cum = np.cumsum(probs, axis=0)
355	        u = rng.uniform(size=n_mc)
356	        Astar = np.zeros(n_mc, dtype=int)
357	        for k in range(K - 1):
358	            Astar += (u >= cum[k]).astype(int)
359	
360	        Dstar = np.zeros((n_mc, K - 1))
361	        for j in range(K - 1):
362	            Dstar[:, j] = (Astar == j + 1).astype(float)
363	
364	        ones = np.ones((n_mc, 1))
365	        if T is not None:
366	            Z = np.hstack([ones, T[:, None], Dstar])
367	        else:
368	            Z = np.hstack([ones, Dstar])
369	        b = np.linalg.lstsq(Z, Y, rcond=None)[0]
370	        coefs.append(b)
371	    return np.mean(coefs, axis=0), np.std(coefs, axis=0) / np.sqrt(n_reps)
372	
373	
374	# ================================================================
375	# Interpretability (a): Eigendecomposition of bias vectors
376	# ================================================================
377	def eigen_analysis(plim_batch, plim_true):
378	    """PCA on bias = plim(C) - plim(I). Returns top-3 variance ratios.
379	
380	    The bias vectors live in R^{K+1} (or R^K for exposure).
381	    Eigendecomposition of bias covariance identifies which linear
382	    combinations of coefficients carry most of the bias variance.
383	    """
384	    bias = (plim_batch - plim_true.unsqueeze(0)).cpu().numpy()
385	    bias_c = bias - bias.mean(axis=0)
386	    _, S, Vt = np.linalg.svd(bias_c, full_matrices=False)
387	    var = S ** 2
388	    ratios = var / var.sum()
389	    return ratios[:min(3, len(ratios))]
390	
391	
392	# ================================================================
393	# Interpretability (b): Worst-case bounds under diagonal constraint
394	# ================================================================
395	def worst_case_bounds(ss, plim_fn, K, device, thresholds=(0.5, 0.7, 0.9)):
396	    """max|τ̂ − τ_true| over column-stochastic C with min diag(C) ≥ thr.
397	
398	    For each threshold, sample 50k constrained C matrices and report
399	    the maximum, mean, and 95th-percentile |bias|.
400	    """
401	    I_batch = torch.eye(K, dtype=DTYPE, device=device).unsqueeze(0)
402	    plim_I = plim_fn(ss, I_batch).squeeze(0)
403	    has_T = plim_I.shape[0] > K
404	    idx = 1 if has_T else 1
405	
406	    results = {}
407	    for thr in thresholds:
408	        Cb = gen_random_C(K, 50_000, device, seed=SEED + int(thr * 1000), min_diag=thr)
409	        pb = plim_fn(ss, Cb)
410	        valid = torch.isfinite(pb).all(dim=1)
411	        pb = pb[valid]
412	        if has_T:
413	            bias = (pb[:, idx] - plim_I[idx]).abs()
414	        else:
415	            bias = (pb[:, 1:] - plim_I[1:].unsqueeze(0)).abs().max(dim=1).values
416	        results[thr] = dict(
417	            max_bias=bias.max().item(),
418	            mean_bias=bias.mean().item(),
419	            p95_bias=torch.quantile(bias, 0.95).item(),
420	        )
421	    return results
422	
423	
424	# ================================================================
425	# Interpretability (c): Sensitivity heatmap via finite differences
426	# ================================================================
427	def sensitivity_heatmap(ss, plim_fn, K, device, out_path, topo_name):
428	    """∂|bias(τ)|/∂C_ij evaluated at C = I via finite differences.
429	
430	    For off-diagonal (i,j): perturb C[i,j] += δ and C[j,j] -= δ to keep
431	    column j stochastic. Measures which misclassification patterns most
432	    affect the τ estimate.
433	    """
434	    delta = 0.01
435	    I_batch = torch.eye(K, dtype=DTYPE, device=device).unsqueeze(0)
436	    plim_I = plim_fn(ss, I_batch).squeeze(0)
437	    has_T = plim_I.shape[0] > K
438	    tau_idx = 1 if has_T else 1
439	    tau_I = plim_I[tau_idx].item()
440	
441	    sens = np.zeros((K, K))
442	    for i in range(K):
443	        for j in range(K):
444	            if i == j:
445	                continue
446	            C = torch.eye(K, dtype=DTYPE, device=device)
447	            C[i, j] += delta
448	            C[j, j] -= delta
449	            p = plim_fn(ss, C.unsqueeze(0)).squeeze(0)
450	            sens[i, j] = abs(p[tau_idx].item() - tau_I) / delta
451	
452	    fig, ax = plt.subplots(figsize=(max(3.5, K * 0.7), max(3.5, K * 0.7)))
453	    im = ax.imshow(sens, cmap='YlOrRd', aspect='equal')
454	    ax.set_xlabel('True category j')
455	    ax.set_ylabel('Observed category i')
456	    ax.set_title(f'{topo_name} K={K}: |∂bias(τ)/∂C_ij|')
457	    ax.set_xticks(range(K))
458	    ax.set_yticks(range(K))
459	    for i in range(K):
460	        for j in range(K):
461	            color = 'w' if sens[i, j] > sens.max() * 0.6 else 'k'
462	            ax.text(j, i, f'{sens[i,j]:.3f}', ha='center', va='center',
463	                    fontsize=max(5, 8 - K), color=color)
464	    plt.colorbar(im, ax=ax, shrink=0.8)
465	    fig.tight_layout()
466	    fig.savefig(out_path, dpi=150, bbox_inches='tight')
467	    plt.close(fig)
468	    return sens
469	
470	
471	# ================================================================
472	# Main
473	# ================================================================
474	def main():
475	    t0 = time.time()
476	    print("=" * 90)
477	    print("  Plan 002: K={3,5,7} Bias Taxonomy Extension")
478	    print("=" * 90)
479	    print(f"Device: {DEVICE}")
480	    if torch.cuda.is_available():
481	        gp = torch.cuda.get_device_properties(0)
482	        print(f"GPU: {gp.name}  ({gp.total_memory / 1024**3:.1f} GB)")
483	    print(f"N_RANDOM={N_RANDOM:,}  N_LARGE={N_LARGE:,}")
484	
485	    topologies = ['confounding', 'mediation', 'collider', 'exposure']
486	    all_results = {}
487	
488	    # ------------------------------------------------------------------
489	    # Named C matrices for MC verification (K=3 only, matching plan_001)
490	    # ------------------------------------------------------------------
491	    C_named_3 = {
492	        'sym_high': np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]]),
493	        'weak_diag': np.array([[.40,.35,.25],[.35,.40,.35],[.25,.25,.40]]),
494	    }
495	
496	    for topo in topologies:
497	        print(f"\n{'=' * 90}")
498	        print(f"  TOPOLOGY: {topo.upper()}")
499	        print(f"{'=' * 90}")
500	
501	        plim_fn = plim_exposure if topo == 'exposure' else plim_with_T
502	        tau_idx = None if topo == 'exposure' else 1
503	
504	        for K in K_VALUES:
505	            print(f"\n  --- K={K} ---")
506	            tk = time.time()
507	
508	            params = make_params(K)
509	            p = params[topo]
510	            rng = np.random.default_rng(SEED)
511	
512	            # 1. Large DGP → sufficient statistics
513	            T, Y, A = _GEN[topo](K, N_LARGE, p, rng)
514	            ss = SuffStats(T, Y, A, K).to_device(DEVICE)
515	            print(f"  p_A = {ss.p_A}")
516	            if ss.has_T:
517	                print(f"  E[T]={ss.E_T:.4f}  E[T²]={ss.E_T2:.4f}  E[TY]={ss.E_TY:.4f}")
518	
519	            # 2. plim(I) = τ_true
520	            I_batch = torch.eye(K, dtype=DTYPE, device=DEVICE).unsqueeze(0)
521	            plim_true = plim_fn(ss, I_batch).squeeze(0)
522	            print(f"  plim(I) = {plim_true.cpu().numpy()}")
523	
524	            # 3. MC verification for K=3
525	            if K == 3:
526	                print(f"\n  MC Verification (K=3, 500 reps × 10k samples):")
527	                for cn, Cnp in C_named_3.items():
528	                    Ct = torch.tensor(Cnp, dtype=DTYPE, device=DEVICE).unsqueeze(0)
529	                    th = plim_fn(ss, Ct).squeeze(0).cpu().numpy()
530	                    mc, se = mc_verify(K, topo, p, Cnp)
531	                    match = np.abs(th - mc) < 2.5 * se
532	                    tag = ''.join('✓' if m else '✗' for m in match)
533	                    print(f"    {cn:<10}  theory={th}  MC={mc}  {tag}")
534	
535	            # 4. Random C search
536	            C_batch = gen_random_C(K, N_RANDOM, DEVICE)
537	            plim_all = plim_fn(ss, C_batch)
538	
539	            valid = torch.isfinite(plim_all).all(dim=1)
540	            n_valid = valid.sum().item()
541	            if n_valid < N_RANDOM:
542	                print(f"  WARNING: {N_RANDOM - n_valid} singular, using {n_valid}")
543	                plim_all = plim_all[valid]
544	
545	            metrics = compute_metrics(plim_all, plim_true, tau_idx=tau_idx)
546	            key = f"{topo}_K{K}"
547	            all_results[key] = metrics
548	
549	            print(f"\n  Overall: violation={metrics['violation']:.1%}  "
550	                  f"sign_flip={metrics['sign_flip']:.1%}  "
551	                  f"amplification={metrics['amplification']:.1%}")
552	            if tau_idx is not None:
553	                print(f"  τ-specific: violation={metrics['tau_violation']:.1%}  "
554	                      f"sign_flip={metrics['tau_sign_flip']:.1%}  "
555	                      f"amplification={metrics['tau_amplification']:.1%}")
556	                print(f"  τ bias: mean={metrics['tau_bias_mean']:+.6f}  "
557	                      f"std={metrics['tau_bias_std']:.6f}  "
558	                      f"max={metrics['tau_bias_max']:.6f}")
559	
560	            # 5. Eigendecomposition
561	            top3 = eigen_analysis(plim_all, plim_true)
562	            print(f"  Eigen top-{len(top3)} var explained: "
563	                  + '  '.join(f'{v:.1%}' for v in top3))
564	
565	            # 6. Worst-case bounds
566	            wc = worst_case_bounds(ss, plim_fn, K, DEVICE)
567	            for thr, v in wc.items():
568	                print(f"  Worst-case (diag≥{thr}): "
569	                      f"max|Δτ|={v['max_bias']:.6f}  "
570	                      f"mean={v['mean_bias']:.6f}  "
571	                      f"P95={v['p95_bias']:.6f}")
572	
573	            # 7. Sensitivity heatmap
574	            hm_path = os.path.join(OUT_DIR, f"plan002_sensitivity_{topo}_K{K}.png")
575	            sensitivity_heatmap(ss, plim_fn, K, DEVICE, hm_path, topo)
576	            print(f"  Heatmap → {os.path.basename(hm_path)}")
577	
578	            print(f"  [{time.time() - tk:.1f}s]")
579	
580	    # ==================================================================
581	    # Cross-K Summary
582	    # ==================================================================
583	    print(f"\n{'=' * 90}")
584	    print("  CROSS-K COMPARISON")
585	    print(f"{'=' * 90}")
586	
587	    hdr = (f"  {'Topology':<14} {'K':>3}"
588	           f" {'violat':>8} {'sflip':>8} {'amplif':>8}"
589	           f" {'τ_viol':>8} {'τ_sflip':>8} {'τ_amp':>8}")
590	    print(hdr)
591	    print(f"  {'-' * 73}")
592	
593	    for topo in topologies:
594	        for K in K_VALUES:
595	            m = all_results[f"{topo}_K{K}"]
596	            tv = m.get('tau_violation', None)
597	            ts = m.get('tau_sign_flip', None)
598	            ta = m.get('tau_amplification', None)
599	            tvs = f"{tv:.1%}" if tv is not None else "  —"
600	            tss = f"{ts:.1%}" if ts is not None else "  —"
601	            tas = f"{ta:.1%}" if ta is not None else "  —"
602	            print(f"  {topo:<14} {K:>3}"
603	                  f" {m['violation']:>8.1%} {m['sign_flip']:>8.1%}"
604	                  f" {m['amplification']:>8.1%}"
605	                  f" {tvs:>8} {tss:>8} {tas:>8}")
606	        print()
607	
608	    # Trend analysis
609	    print("  K-TREND ANALYSIS (does bias worsen with K?)")
610	    for topo in topologies:
611	        if topo == 'exposure':
612	            vals = [all_results[f"{topo}_K{K}"]['violation'] for K in K_VALUES]
613	            label = 'violation'
614	        else:
615	            vals = [all_results[f"{topo}_K{K}"]['tau_violation'] for K in K_VALUES]
616	            label = 'τ_violation'
617	        d = vals[-1] - vals[0]
618	        trend = "WORSENS" if d > 0.01 else ("STABLE" if abs(d) <= 0.01 else "IMPROVES")
619	        print(f"  {topo:<14} ({label}): "
620	              f"K=3 {vals[0]:.1%} → K=5 {vals[1]:.1%} → K=7 {vals[2]:.1%}  [{trend}]")
621	
622	    # ==================================================================
623	    # Combined sensitivity figure (K=5 and K=7 side by side per topology)
624	    # ==================================================================
625	    fig, axes = plt.subplots(len(topologies), 2, figsize=(12, 4 * len(topologies)))
626	    for row, topo in enumerate(topologies):
627	        for col, K in enumerate([5, 7]):
628	            ax = axes[row, col]
629	            hm_path = os.path.join(OUT_DIR, f"plan002_sensitivity_{topo}_K{K}.png")
630	            if os.path.exists(hm_path):
631	                img = plt.imread(hm_path)
632	                ax.imshow(img)
633	                ax.axis('off')
634	                ax.set_title(f'{topo} K={K}', fontsize=10)
635	            else:
636	                ax.text(0.5, 0.5, 'N/A', ha='center', va='center', transform=ax.transAxes)
637	                ax.set_title(f'{topo} K={K}', fontsize=10)
638	    fig.suptitle('Sensitivity Heatmaps: |∂bias(τ)/∂C_ij|', fontsize=13)
639	    fig.tight_layout(rect=[0, 0, 1, 0.97])
640	    combined_path = os.path.join(OUT_DIR, 'plan002_sensitivity_combined.png')
641	    fig.savefig(combined_path, dpi=150, bbox_inches='tight')
642	    plt.close(fig)
643	    print(f"\n  Combined heatmap → {os.path.basename(combined_path)}")
644	
645	    print(f"\nTotal: {time.time() - t0:.0f}s")
646	
647	
648	if __name__ == "__main__":
649	    main()
650	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18a0f93a-3248-44ca-88ec-2577f8bf0b2e",
  "isSidechain": true,
  "promptId": "61d74a93-5a71-4e46-b233-0f41972ac7d7",
  "agentId": "a2e40a43448a018a4",
  "type": "user",
  "uuid": "702da1e2-08cb-46a3-888b-a2438215eb3c",
  "sourceToolAssistantUUID": "18a0f93a-3248-44ca-88ec-2577f8bf0b2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T21:00:41.834Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VV3Fgz1NV3uurvmxCS3s1J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "702da1e2-08cb-46a3-888b-a2438215eb3c",
  "isSidechain": true,
  "agentId": "a2e40a43448a018a4",
  "requestId": "req_011CbEVd7vXE3TKTexjP11kn",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "921a2481-c30e-49f0-8586-2265e541fe78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RQ1FLWennpE9fQL7iZAEwh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15897,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15897,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T21:00:41.840Z_

<details><summary>↩ Tool result · `toolu_01VV3Fgz1NV3uurvmxCS3s1J`</summary>

```text
1	# Project Memory
2	
3	## MVP 验证发现 (2026-05-20)
4	
5	### Exposure DAG: bias-toward-null 保证在 K=3 下失效（核心发现）
6	**100k 随机 C 搜索：85% 违反 bias-toward-null，83.4% 产生符号反转。** 二分类 K=2 下全部满足 toward null 保证。
7	
8	具体 named structure 结果：
9	- C3_STRUCTURAL_12: β_2=-0.5 → γ̂_2=+0.06（符号反转）
10	- C4_WEAK_DIAG: β_1=1.0 → γ̂_1≈0（近消失）
11	- C5_NEAR_PERM: β_2=-0.5 → γ̂_2=+1.25（符号反转 + 2.5x 放大，最极端）
12	
13	**关键洞察**：exposure 误分类场景下，多分类 C 矩阵的交叉污染使得回归将某类的 Y 值归因到错误标签，产生符号反转。
14	
15	### Dirichlet 子空间分析：高精度 LLM 仍有显著违反
16	即使 min(diag(C))≥0.9，amplification 违反率仍达 11.9%。符号反转随精度提高消失，但 amplification 稳定在 ~12%。
17	
18	### Confounding DAG: 偏差方向性质
19	100k 随机 C 搜索均未发现负偏差。K=3 误分类偏差始终与 OVB 同向。
20	
21	### DGP 参数
22	- Confounding DAG: P(A)=[0.4, 0.35, 0.25], alpha=[1.5, -1.0], beta_T=2.0, beta_A=[1.0, -0.5], sigma=1.0
23	- Exposure DAG: P(A)=[0.4, 0.35, 0.25], beta=[0, 1.0, -0.5], sigma_Y=1.0
24	
25	## plan_001 完整 Taxonomy 结果 (2026-05-20)
26	
27	### 结构性保证：τ sign_flip = 0% 跨所有拓扑和所有 τ 大小
28	**这是论文 Claim 1 的核心 positive result**。K=3 非差异性误分类改变 treatment effect 幅度但不翻转方向。小 τ (0.05, 0.1) 确认是结构性的。Exposure DAG 是唯一例外（83.4% sign reversal）。
29	
30	### 拓扑行为分层
31	- **Mediation/Front-door**: violation ≈100%, amplification ≈100%, misclass_amplifies ≈100% — 最受影响
32	- **Collider**: misclass_amplifies = 0% — 误分类减弱 collider bias（独特）
33	- **M-bias**: violation 53.2%, amplification 10.4% — 最鲁棒
34	- **Exposure**: sign_flip 83.4% — 唯一翻转拓扑（C 直接作用于 design matrix）
35	
36	## plan_002 K=5,7 扩展结果 (2026-05-20)
37	
38	### Sign_flip 随 K 恶化（核心发现）
39	**K 增大引入更多错分模式，符号反转概率系统性上升**：
40	- Mediation: 83.8%(K=3) → 96.6%(K=5) → **100%(K=7)**
41	- Collider: 66.6%(K=3) → 95.5%(K=5) → **99.2%(K=7)**
42	- Confounding/Exposure: K=3 已近饱和，K=5,7 达 100%
43	
44	### 但 worst-case bound 和 bias 均值反而下降（除 exposure）
45	**反直觉的 nuance**：高精度约束(diag≥0.9)下，K 增大每个 off-diagonal 元素分摊更小 → confounding worst-case 从 0.162(K=3) 降至 0.092(K=7)。**唯一例外是 exposure**（0.253→0.282），因为 exposure 的 bias 来自 design matrix 的交叉污染，不受对角占优约束的同样保护。
46	
47	### Eigendecomposition：bias 方差随 K 分散
48	Top-1 PC 解释 bias 方差的比例：78%(K=3) → 67%(K=5) → 61%(K=7)。K 增大后 bias 不再集中在单一方向，增加了诊断和校正难度。
49	
50	### 对论文 story 的影响
51	Claim 1 证据链完整：plan_001(K=3 taxonomy) + plan_002(K scaling) + plan_008(binarization collapse)。可 claim "K 增大使符号反转风险恶化，practitioners 处理高 K 分类任务时风险更大"。
52	
53	## plan_008 Binarization Collapse 结果 (2026-05-20)
54	
55	### 拓扑依赖性：折叠偏差跨度 150 倍
56	IV (Δ_mean=0.926) > Exposure (0.516) >> Mediation (0.045) > Confounding (0.025) > Collider (0.017) > M-bias (0.006)。Sign flip 只在 IV (17.5%) 和 Exposure (14.0%)。plan_001 和 plan_008 的拓扑危险性排序一致。
57	
58	## plan_004 ASV 框架结果 (2026-05-20)
59	
60	### v2 发现 + v3 修正
61	v2 问题：(1) 单调性 75% 违反 (2) sign-flip ASV 对 confounding/mediation 返回 None
62	
63	v3 修正（D007 + Director magnitude 阈值修正）：
64	- **Envelope monotonicity**: violations = 0（构造性保证）
65	- **Magnitude ASV (10% relative threshold)**: 对所有拓扑有信息
66	  - τ=0.5: 0.076–0.487（部分 C₀ 下安全）
67	  - τ=0.1: 0.014–0.093（不安全）
68	  - τ=0.05: 0.008–0.047（极不安全）
69	- **关键洞察**：小 τ ASV << 1 = LLM 标注误差对小效应因果推断不安全 → 连接 Claim 3 correction 需求
70	- **Type I/II (小 τ)**: ASV-informed 正确保守（H₁ 下 0% 拒绝，因为 ASV<1 → 标记不安全）
71	
72	### ASV 三类定义（最终版）
73	1. **Sign-flip ASV**: min δ 使 sign 翻转（Exposure 专用，其他拓扑 = None）
74	2. **Magnitude ASV**: min δ 使 |bias| > 0.1×|τ̂|（通用，所有拓扑有信息）
75	3. **Significance ASV**: min δ 使 |plim τ̂(C(δ))| < 1.96×SE（假设检验 filter）
76	
77	## plan_005 ASV 扩展结果 (2026-05-20, fixed)
78	
79	### 6 拓扑 ASV 全覆盖（Reviewer CRITICAL 修复后）
80	修复 4 点：C1 significance ASV 函数 + C2 magnitude τ≈0→0.0 + W1 IV τ_true=plim(I)=0.6598 + W2 M-bias τ_true=plim(I)=0.5128
81	
82	### τ_true 必须用 plim(I) 而非 DGP 参数
83	**设计决策**：ASV 衡量 annotation error **额外引入**的 bias，不含估计量固有的多类别污染。因此 τ_true = plim(C=I)，不是 DGP 直接参数。IV plim(I)=0.6598≠β₁=0.5；M-bias plim(I)=0.5128≠τ=0.5。Front-door 已正确。
84	
85	### Significance filter Type I/II（修复后）
86	| 拓扑 | Type I | Power τ=0.05 | Power τ=0.1 |
87	|------|--------|-------------|-------------|
88	| M-bias | 0% | 95.8-99.2% | 100% |
89	| IV | 0% | 0% | 0% |
90	| Front-door | 0% | 100% | 100% |
91	
92	- **IV power=0% 是正确的**：Wald 估计量极脆弱，signif_ASV≈0（annotation error 立即摧毁 significance），ASV filter 保守阻止所有拒绝。对 IV，应改用 magnitude ASV 报告脆弱性
93	- **M-bias 高 power**：误分类减弱 spurious bias，不影响真实效应的检测
94	- 与 plan_004 confounding/mediation/collider 结果合并 → 6 拓扑 significance filter 完整验证
95	
96	## plan_007 Correction Guidance 结果 (2026-05-20)
97	
98	### PPI++ 全面碾压（Claim 3 核心支撑）
99	Grand mean: bias_red 93.8%, coverage 96.8%, win rate 95.2% (40/42 scenarios)。唯一满足名义 95% coverage 的方法。
100	
101	### Frisch-Waugh 不变性：理论到实证完全验证
102	naive_plugin 和 MLA 在 OLS 拓扑（confounding/mediation/collider/mbias）下 bias_red 精确 0.0%。原因：C⁻¹ 变换 dummy matrix 不改变 [intercept, D*] 的列空间，T 系数 OLS 估计不变。
103	但在 exposure/iv/frontdoor 下两者显著恶化（-40% ~ -113%），因为这些拓扑的估计量不是简单 OLS on T → FWL 不适用。
104	
105	### DSL 拓扑敏感性（新发现，可作为 contribution）
106	DSL 仅在 confounding (49.8%) 和 mediation (70.3%) 有效——这两种拓扑 misclassification error 主要通过 dummy 系数传播，DSL 的 EM 迭代能捕获。其余 5 拓扑系统性失败，最差 mbias -768%。**失败原因是结构性的，非个别 C 问题。**
107	
108	### PPI++ 的阿喀琉斯之踵
109	mbias + realistic_llm: bias_red = -25.1%（恶化），但 coverage 99%。说明 PPI 的置信区间正确反映了增大的不确定性，bias 校正本身失效。论文应诚实报告此弱点。
110	
111	### MC-SIMEX 不稳定
112	Grand mean 20.9%，在 iv (64.7%) 尚可但 frontdoor (-55.7%) 崩溃。不适合作为通用推荐。
113	
114	## plan_009 Pathological Matrices 结果 (2026-05-20)
115	
116	### 3 风险层级
117	- **Low risk**: mbias (mean_bias 0.006-0.039)
118	- **Medium risk**: confounding/mediation/collider/frontdoor (R²=0.70-0.77, condition_number 最一致预测因子)
119	- **High risk**: exposure/IV (不可预测，R²低)
120	
121	### IV 过滤问题
122	3000/28000 (10.7%) non-finite Wald estimates 被静默排除。regression 仅基于 89.3% 的样本。
123	
124	## Director 决策记录 (2026-05-20)
125	
126	### 数据集决策（最终确认）
127	- HumAID (K=10), VAST (K=3), Civil Comments (K=2)
128	- 数据位置：`/home/sonny/causal_annot_error_attrib/data/`
129	
130	### API 模型决策
131	- Llama 4 Maverick, Qwen 3 235B, DeepSeek Chat V3
132	- API endpoint: `http://47.94.22.126/v1`，全部用 OPENROUTER_API_KEY
133	
134	### home-1x5090 服务器
135	- account: sonny, Python 3.10.12, Ubuntu 22.04
136	- 项目目录 `/home/sonny/causal_annot_error_attrib/`
137	
138	### ASV 框架决策 (D005-D008)
139	- D005: C(δ) 参数化选定方案 A 线性插值
140	- D006: 区分 Vulnerability/Protection 双方向 ASV
141	- D007: Envelope monotonicity 替代 raw monotonicity
142	- D008: ASV 阈值从 sign-flip 改为 magnitude-based（0.1×|τ̂|），sign-flip ASV 保留给 Exposure
143	
144	### Lee & Wood-Doughty (2024) 技术区分
145	本项目：observed exposure/confounder with noisy LLM annotation。LWD：unobserved confounding with proxy。关键区别：我们的 C 可从 validation data 估计。
146	
147	## ASV C(δ) 参数化调研 (2026-05-20)
148	
149	### 关键文献
150	- VanderWeele & Ding (2017): E-value 框架——单标量参数化 + 单调 + 可解释
151	- VanderWeele & Li (2019): 测量误差灵敏度分析——Se/Sp ratio 参数化
152	- Lash, Fox & Fink (2009): QBA 框架——(Se, Sp) 对参数化
153	- Brenner (1993): 多分类混杂误分类偏差方向可反转
154	
155	### 与 E-value 的对应
156	方案 A 在 K=2 时精确退化到 VanderWeele & Li (2019) 框架。
157	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "921a2481-c30e-49f0-8586-2265e541fe78",
  "isSidechain": true,
  "promptId": "61d74a93-5a71-4e46-b233-0f41972ac7d7",
  "agentId": "a2e40a43448a018a4",
  "type": "user",
  "uuid": "5b1982d2-f809-4651-b05c-416e5d9f74e3",
  "sourceToolAssistantUUID": "921a2481-c30e-49f0-8586-2265e541fe78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-20T21:01:24.538Z_

Perfect! I've successfully read all the requested files. Let me provide you with a comprehensive report of the critical information you need.

## COMPREHENSIVE FILE REPORT

### FILE 1: plan_001_collider_mbias_iv.py
**Location:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_collider_mbias_iv.py`

**PLIM BIAS COMPUTATION FUNCTIONS:**

1. **Collider (T → A ← Y):**
   - `theory_collider(C, params, N_approx, seed)`: Large-sample approximation using 2M samples
   - Returns `(tau_ctrl, tau_nc)` - OLS estimate with and without controlling for A*
   - DGP: `Y = tau*T + eps`, `A|T,Y ~ softmax(...)`
   - Regression: `Y ~ 1 + T + D1 + D2` where D1, D2 are dummy variables for A*
   
2. **M-bias (U1→{A,T}, U2→{A,Y}):**
   - `theory_mbias(C, params, N_approx, seed)`: Similar large-sample approach
   - DGP: `T = delta*U1 + eta`, `Y = tau*T + lam*U2 + eps`
   - Computes plim via OLS with control for misclassified A*
   
3. **Instrument (Z→A→Y, U→{A,Y}):**
   - `theory_iv(C, beta, params, N_approx, seed)`: Computes Wald estimators
   - Returns dict with: `RF`, `FS1_star`, `FS2_star`, `FS1_true`, `FS2_true`, `Wald1_star`, `Wald2_star`, `ols_star`, `ols_true`
   - First stage: `FS*_k = (Astar[Z=1]==k).mean() - (Astar[Z=0]==k).mean()`

**CONFUSION MATRIX USAGE:**
- C is K×K (here K=3): confusion matrix where `C[i,j] = P(A*=i | A=j)`
- Generation via `_generate_Astar(A, C, rng)`: Sample from categorical using column probabilities
- Example matrices: C1_SYMMETRIC_HIGH (0.80 diag), C2_ASYMMETRIC, C3_STRUCTURAL_12, etc.

**NAMED C MATRICES:**
```python
C1_SYMMETRIC_HIGH = [[.80, .10, .10], [.10, .80, .10], [.10, .10, .80]]
C2_ASYMMETRIC = [[.65, .05, .10], [.30, .85, .10], [.05, .10, .80]]
C3_STRUCTURAL_12 = [[.96, .01, .01], [.02, .69, .30], [.02, .30, .69]]
C4_WEAK_DIAG = [[.40, .35, .25], [.35, .40, .35], [.25, .25, .40]]
C5_NEAR_PERM = [[.05, .05, .90], [.90, .05, .05], [.05, .90, .05]]
C6_DIFF_BASE = [[.80, .10, .10], [.10, .80, .10], [.10, .10, .80]]
```

**DGP PARAMETER CONVENTIONS:**
- `COLLIDER_PARAMS = {tau=1.0, g1=0.0, g2=0.0, dT=0.5, dY=0.8, dT2=-0.3, dY2=0.6}`
- `MBIAS_PARAMS = {tau=1.0, delta=1.0, lam=1.0, g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9}`
- `IV_PARAMS = {lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6}`
- `BETA_MIXED = [0.0, 1.0, -0.5]`, `BETA_SAME = [0.0, 1.0, 0.5]`

---

### FILE 2: plan_001_mediation_frontdoor.py
**Location:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_mediation_frontdoor.py`

**PLIM BIAS COMPUTATION - CLOSED FORM:**

1. **Mediation (T → A → Y):**
   - `plim_med(C, beta, tau, g=GAMMA_MED, d=DELTA_MED)`: Closed-form plim computation
   - Key moments: `p0 = softmax(g + d*0)`, `p1 = softmax(g + d*1)`
   - Transformed: `q0 = C @ p0`, `q1 = C @ p1` (P(A*|T))
   - Constructs EZZ, EZX matrices explicitly:
     ```python
     EZZ[0,0] = 1, EZZ[0,1] = 0.5, EZZ[0,2:] = qm[1:]
     EZZ[1,1] = 0.5, EZZ[1,2:] = 0.5*q1[1:]
     EZZ[2:,2:] = diag(qm[1:])
     ```
   - Returns: `np.linalg.solve(EZZ, EZX @ b)`

2. **Front-door (T → M → Y, U → {T,Y}):**
   - `plim_fd(C, st)`: Uses pre-computed sufficient statistics dict
   - Requires: `E_T, E_T2, E_Y, E_TY, E_DM[k], E_DM_T[k], E_DM_Y[k]`
   - Transforms: `E_D* = C @ E_D`, then constructs 4×4 EZZ and EZY

**SUFFICIENT STATISTICS COMPUTATION:**
- `precomp_fd(beta, N=50M, seed=123)`: Generates DGP, computes population moments
- For mediation: uses direct conditional probabilities `softmax(gamma + delta*T)`
- Returns dict of means: `E_T, E_T2, E_Y, E_TY, E_DM, E_DM_T, E_DM_Y`

**DGP PARAMETERS:**
```python
TAU = 0.5
GAMMA_MED = [0.0, 0.5, -0.3]
DELTA_MED = [0.0, 0.8, -0.6]
ALPHA_U = 1.0
LAMBDA_U = 1.0
GAMMA_FD = [0.0, 0.5, -0.3]
DELTA_FD = [0.0, 1.0, -0.8]
BETA_MIXED = [0.0, 1.0, -0.5]
BETA_SAME = [0.0, 1.0, 0.5]
```

**C DICTIONARY (6 matrices):**
```python
C_DICT = {
    "1_sym_high":   [[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]],
    "2_asymmetric": [[.65,.05,.10],[.30,.85,.10],[.05,.10,.80]],
    "3_struct_12":  [[.96,.01,.01],[.02,.69,.30],[.02,.30,.69]],
    "4_weak_diag":  [[.40,.35,.25],[.35,.40,.35],[.25,.25,.40]],
    "5_near_perm":  [[.05,.05,.90],[.90,.05,.05],[.05,.90,.05]],
    "6_diff_base":  [[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]],
}
```

---

### FILE 3: plan_005_asv_extended.py
**Location:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_005_asv_extended.py`

**ASV FRAMEWORK IMPLEMENTATION:**

1. **ASV COMPUTATION FUNCTIONS:**

   - `compute_bias_curve(topology, C0, param, tau_true, st, n_grid=1500)`:
     - Generates delta range, computes tau curve via C(delta) parameterization
     - Returns: `(deltas, bias_abs, tau_curve)` where `bias_abs = |tau_curve - tau_true|`

   - `compute_envelope(bias_abs)`: Computes envelope via running maximum
     - Returns monotone upper bound on absolute bias

   - `compute_asv_envelope(topology, C0, tau_true, param, threshold_type, threshold_value, st, n_grid)`:
     - Supports three threshold types:
       1. **"sign_flip"**: First delta where sign changes (if tau_true ≠ 0)
       2. **"magnitude_relative"**: First delta where envelope > 0.1×|tau_true|
       3. **"magnitude_absolute"**: First delta where envelope > threshold_value
     - Returns dict with `asv`, violations counts, deltas, tau_curve, envelope

   - `compute_magnitude_asv_fast(tau_curve, deltas, tau_true, rel_thresh=0.1)`:
     - Returns first delta where running max bias exceeds threshold

2. **C(delta) PARAMETERIZATION (LinearInterpolation):**
   - `C(delta) = (1-delta)*I + delta*C0` normalized by column sums
   - `delta_range(C0)`: Returns (0, delta_max) where delta_max depends on diag(C0)
   - If min_diag ≥ 1: max_delta = 10
   - Else: max_delta = min(1/(1-min_diag), 10)

3. **TOPOLOGIES STRUCTURE:**

   **M-bias:**
   - `MBIAS_PARAMS = {tau=0.5, delta=1.0, lam=1.0, g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9}`
   - `precomp_mbias(params, N=2M, seed=999)`: Returns sufficient stats dict
   - `plim_mbias(C, st)`: OLS plim for Y ~ 1 + T + D1_A* + D2_A*

   **IV:**
   - `IV_PARAMS = {lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6}`
   - `IV_BETA = [0.0, 0.5, -0.25]`
   - `precomp_iv(beta, params, N=2M, seed=999)`: RF and FS
   - `plim_iv(C, st)`: Wald estimator RF/FS*_1

   **Front-door:**
   - `ALPHA_U=1.0, LAMBDA_U=1.0, BETA_FD=[0.0, 1.0, -0.5]`
   - `GAMMA_FD = [0.0, 0.5, -0.3], DELTA_FD = [0.0, 1.0, -0.8]`
   - `precomp_fd(beta, N=10M, seed=123, lU=None, aU=None, d=None)`: Sufficient stats
   - `plim_fd(C, st)`: OLS plim for Y ~ 1 + T + D1_M* + D2_M*

4. **C MATRIX LIST (6 matrices):**
   ```python
   def make_C_list():
       return {
           "C1_sym": [[0.80, 0.10, 0.10], ...],
           "C2_high": [[0.90, 0.05, 0.05], ...],
           "C3_asym": [[0.70, 0.20, 0.10], ...],
           "C4_weak": [[0.60, 0.20, 0.20], ...],
           "C5_perm": [[0.40, 0.30, 0.30], ...],
           "C6_diff": [[0.85, 0.075, 0.075], ...],
       }
   ```

5. **FIVE ANALYSIS PARTS:**
   - Part 1: Envelope monotonicity verification (0 violations expected)
   - Part 2: ASV values (sign_flip, magnitude_relative 10%)
   - Part 3: Small-tau ASV (tau=0.05, 0.1)
   - Part 4: MC coverage (500 scenarios, 100 reps each)
   - Part 5: Type I/II errors with significance filter

---

### FILE 4: plan_002_k57_extension.py
**Location:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_002_k57_extension.py`

**GENERAL K PARAMETERIZATION:**

1. **DGP PARAMETER GENERATION FOR K={3,5,7}:**
   ```python
   K_VALUES = [3, 5, 7]
   _ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7]  # For alpha
   _BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2]  # For beta_A
   _GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1]
   _DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2]
   ```

   - `make_params(K)`: Generates all topology parameters for given K
   - Parameters for each topology: confounding, mediation, collider, exposure

2. **SUFFICIENT STATISTICS CLASS:**
   ```python
   class SuffStats:
       def __init__(self, T, Y, A, K):
           self.p_A = P(A=k) for each k
           self.E_Y, self.E_YD[k]  # Marginal Y and Y given category k
           if has_T:
               self.E_T, self.E_T2, self.E_TY, self.E_TD[k]
   ```

3. **PLIM COMPUTATION (GPU-BATCHED):**
   - `plim_with_T(ss, C)`: For topologies with treatment T
     - Constructs EZZ, EZY matrices in batched form
     - Returns `torch.linalg.solve(EZZ, EZY)` - shape [B, K+1]
   - `plim_exposure(ss, C)`: For pure exposure outcome (no T)
     - Similar but dimension is K, not K+1

4. **CONFUSION MATRIX GENERATION:**
   - `gen_random_C(K, N, device, seed, min_diag=None)`: Sample N column-stochastic K×K matrices
   - Uses Dirichlet(1,...,1) per column
   - Optional constraint: min_diag specifies minimum diagonal elements

5. **METRICS COMPUTATION:**
   - `compute_metrics(plim_batch, plim_true, tau_idx)`:
     - violation: Any coefficient changes
     - sign_flip: Any non-zero coefficient flips sign
     - amplification: Any |coef| > |coef_true|
     - tau-specific versions if tau_idx provided

---

### FILE 5: plan_002_k57_extension.py (NOT plan_004)
**Note:** plan_004_asv_framework.py does NOT exist. plan_002_k57_extension.py was file 5.

---

### FILE 6: memory.md
**Location:** `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/memory.md`

**KEY FINDINGS:**

1. **Exposure DAG Paradox (MVP Finding):**
   - 85% violate bias-toward-null with K=3
   - 83.4% sign flip rate
   - K=2 maintains toward-null guarantee

2. **Sign-flip Worsening with K:**
   - Mediation: 83.8%(K=3) → 96.6%(K=5) → 100%(K=7)
   - Collider: 66.6%(K=3) → 95.5%(K=5) → 99.2%(K=7)

3. **Topology Risk Hierarchy:**
   - Low risk: M-bias
   - Medium risk: confounding/mediation/collider/front-door
   - High risk: exposure/IV

4. **ASV Definition (Final v3):**
   1. Sign-flip ASV: min δ where sign flips
   2. Magnitude ASV: min δ where |bias| > 0.1×|τ̂|
   3. Significance ASV: min δ where |τ̂| < 1.96×SE

5. **Plan 005 Significance Filter Results:**
   - M-bias: Type I=0%, Power(τ=0.05)=95.8-99.2%
   - IV: Type I=0%, Power=0% (Wald estimator too fragile)
   - Front-door: Type I=0%, Power(τ=0.05)=100%

6. **Plan 007 Correction (Claim 3):**
   - PPI++ grand mean: 93.8% bias reduction, 96.8% coverage, 95.2% win rate
   - Only method achieving nominal 95% coverage
   - Naive plugin: 0% bias reduction (Frisch-Waugh invariance for OLS)

---

## SUMMARY TABLE: KEY FUNCTIONS

| File | Topology | Plim Function | Parameters | C Matrix |
|------|----------|---------------|-----------|----------|
| plan_001_collider_mbias_iv.py | Collider | `theory_collider` | COLLIDER_PARAMS | C1-C6 |
| plan_001_collider_mbias_iv.py | M-bias | `theory_mbias` | MBIAS_PARAMS | C1-C6 |
| plan_001_collider_mbias_iv.py | IV | `theory_iv` | IV_PARAMS, BETA_MIXED/SAME | C1-C6 |
| plan_001_mediation_frontdoor.py | Mediation | `plim_med` | GAMMA_MED, DELTA_MED, TAU | C_DICT (6) |
| plan_001_mediation_frontdoor.py | Front-door | `plim_fd` | ALPHA_U, LAMBDA_U, GAMMA_FD, DELTA_FD | C_DICT (6) |
| plan_005_asv_extended.py | M-bias/IV/FD | `compute_asv_envelope` | Per-topology | C1-C6 |
| plan_002_k57_extension.py | All 4 | `plim_with_T`/`plim_exposure` | Generated per K | Random Dirichlet |

This comprehensive report captures all the critical implementation details, parameter conventions, and ASV framework specifications across all files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b1982d2-f809-4651-b05c-416e5d9f74e3",
  "isSidechain": true,
  "agentId": "a2e40a43448a018a4",
  "requestId": "req_011CbEVdKiCCdh8BAXx4MtDo",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5357e471-f52c-4940-bc56-ed7feded0534",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "fb66a23b-ab7a-49cf-9609-9cc0b887dde7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015TbGWxbM8Y95TrmutKERYN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 47908,
      "cache_read_input_tokens": 15897,
      "output_tokens": 5069,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 47908
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 5069,
          "cache_read_input_tokens": 15897,
          "cache_creation_input_tokens": 47908,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 47908,
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
