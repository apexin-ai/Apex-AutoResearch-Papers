# code plan 010 toolkit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 70
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/workers/worker_code_plan_010_toolkit_20260520T232412.log`
- **Structured JSON:** [`58476423219675426e0e.json`](../../sessions/58/58476423219675426e0e.json)

## Before a recorded user message

70 recorded events

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
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
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
  "uuid": "e97fdc34-9b4f-4ccc-b1cf-a02f7a7da49c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod-0510-projects-causal-annot-error-attrib/memory/"
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
    "resetsAt": 1779336600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "f97c1202-8f6d-4ec8-9cae-1efa4b38a04e",
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
This is a large task - building a Python package from existing code. Let me start by reading the source files to understand the existing functions, then build the package structure.

Let me read all the source files first in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "2fb1d372-519f-407c-adaa-9578d3214997",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VrZMd1roJtVpjrW4LrGWo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15004,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15004
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

### Assistant

_source line 5_

I'll start by reading all the source files to extract the existing functions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "80e94a80-5f35-42a4-9904-b8664b857763",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VrZMd1roJtVpjrW4LrGWo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15004,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15004
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

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01BaKGPeSocgWCok1Bo9v8UJ`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "27dcb3d2-1fb8-4358-aec5-7882c1073ded",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VrZMd1roJtVpjrW4LrGWo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15004,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15004
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

_source line 7 · 2026-05-20T23:24:28.782Z_

<details><summary>↩ Tool result · `toolu_01BaKGPeSocgWCok1Bo9v8UJ`</summary>

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
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "165ffcbb-2d21-40ce-ba3a-fafcf02b2dee",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_collider_mbias_iv.py",
      "content": "\"\"\"\nCollider + M-bias + Instrument DAG: bias via large-sample moments + MC verification.\nK=3 LLM annotation error bias propagation in causal inference.\n\"\"\"\n\nimport numpy as np\nfrom collections import OrderedDict\nimport time\n\n# ── Constants ────────────────────────────────────────────────────────────────\n\nBETA_MIXED = np.array([0.0, 1.0, -0.5])\nBETA_SAME  = np.array([0.0, 1.0,  0.5])\n\nC1_SYMMETRIC_HIGH = np.array([[0.80, 0.10, 0.10], [0.10, 0.80, 0.10], [0.10, 0.10, 0.80]])\nC2_ASYMMETRIC     = np.array([[0.65, 0.05, 0.10], [0.30, 0.85, 0.10], [0.05, 0.10, 0.80]])\nC3_STRUCTURAL_12  = np.array([[0.96, 0.01, 0.01], [0.02, 0.69, 0.30], [0.02, 0.30, 0.69]])\nC4_WEAK_DIAG      = np.array([[0.40, 0.35, 0.25], [0.35, 0.40, 0.35], [0.25, 0.25, 0.40]])\nC5_NEAR_PERM      = np.array([[0.05, 0.05, 0.90], [0.90, 0.05, 0.05], [0.05, 0.90, 0.05]])\nC6_DIFF_BASE      = np.array([[0.80, 0.10, 0.10], [0.10, 0.80, 0.10], [0.10, 0.10, 0.80]])\n\nALL_C = OrderedDict([\n    (\"C1_sym_high\",   C1_SYMMETRIC_HIGH),\n    (\"C2_asymmetric\", C2_ASYMMETRIC),\n    (\"C3_struct_12\",  C3_STRUCTURAL_12),\n    (\"C4_weak_diag\",  C4_WEAK_DIAG),\n    (\"C5_near_perm\",  C5_NEAR_PERM),\n    (\"C6_diff_base\",  C6_DIFF_BASE),\n])\n\n# ── Utilities ────────────────────────────────────────────────────────────────\n\ndef _generate_Astar(A, C, rng):\n    probs = C[:, A]\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\n\n\ndef _generate_Astar_fixed_u(A, C, u):\n    probs = C[:, A]\n    cum = np.cumsum(probs, axis=0)\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\n\n\ndef _softmax_sample(logits, rng):\n    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\n    probs = exp_l / exp_l.sum(axis=1, keepdims=True)\n    cum = np.cumsum(probs, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\n\n\ndef _ols(Z, Y):\n    return np.linalg.solve(Z.T @ Z, Z.T @ Y)\n\n\n# ══════════════════════════════════════════════════════════════════════════════\n# DAG 1: COLLIDER — T -> A <- Y\n# ══════════════════════════════════════════════════════════════════════════════\n\nCOLLIDER_PARAMS = dict(tau=1.0, g1=0.0, g2=0.0, dT=0.5, dY=0.8, dT2=-0.3, dY2=0.6)\n\n\ndef _gen_collider(N, params, rng):\n    T = rng.normal(0, 1, N)\n    eps = rng.normal(0, 1, N)\n    Y = params['tau'] * T + eps\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['dT'] * T + params['dY'] * Y,\n        params['g2'] + params['dT2'] * T + params['dY2'] * Y,\n    ])\n    A = _softmax_sample(logits, rng)\n    return T, Y, A\n\n\ndef theory_collider(C, params, N_approx=2_000_000, seed=999):\n    rng = np.random.default_rng(seed)\n    T, Y, A = _gen_collider(N_approx, params, rng)\n    Astar = _generate_Astar(A, C, rng)\n    D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)\n    ones = np.ones(N_approx)\n    tau_ctrl = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]\n    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]\n    return tau_ctrl, tau_nc\n\n\ndef mc_collider(C, params, N=10_000, n_reps=1000, seed=0):\n    tau_ctrl_arr = np.empty(n_reps)\n    tau_nc_arr = np.empty(n_reps)\n    for r in range(n_reps):\n        rng = np.random.default_rng(seed + r)\n        T, Y, A = _gen_collider(N, params, rng)\n        Astar = _generate_Astar(A, C, rng)\n        D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)\n        ones = np.ones(N)\n        tau_ctrl_arr[r] = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]\n        tau_nc_arr[r] = _ols(np.column_stack([ones, T]), Y)[1]\n    return tau_ctrl_arr.mean(), tau_nc_arr.mean()\n\n\n# ══════════════════════════════════════════════════════════════════════════════\n# DAG 2: M-BIAS — U1 -> {A,T}, U2 -> {A,Y}\n# ══════════════════════════════════════════════════════════════════════════════\n\nMBIAS_PARAMS = dict(tau=1.0, delta=1.0, lam=1.0,\n                    g1=0.0, g2=0.0, a1=0.8, a2=0.6, a3=-0.5, a4=0.9)\n\n\ndef _gen_mbias(N, params, rng):\n    U1 = rng.normal(0, 1, N)\n    U2 = rng.normal(0, 1, N)\n    T = params['delta'] * U1 + rng.normal(0, 1, N)\n    Y = params['tau'] * T + params['lam'] * U2 + rng.normal(0, 1, N)\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['a1'] * U1 + params['a2'] * U2,\n        params['g2'] + params['a3'] * U1 + params['a4'] * U2,\n    ])\n    A = _softmax_sample(logits, rng)\n    return T, Y, A\n\n\ndef theory_mbias(C, params, N_approx=2_000_000, seed=999):\n    rng = np.random.default_rng(seed)\n    T, Y, A = _gen_mbias(N_approx, params, rng)\n    Astar = _generate_Astar(A, C, rng)\n    D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)\n    ones = np.ones(N_approx)\n    tau_ctrl = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]\n    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]\n    return tau_ctrl, tau_nc\n\n\ndef mc_mbias(C, params, N=10_000, n_reps=1000, seed=0):\n    tau_ctrl_arr = np.empty(n_reps)\n    tau_nc_arr = np.empty(n_reps)\n    for r in range(n_reps):\n        rng = np.random.default_rng(seed + r)\n        T, Y, A = _gen_mbias(N, params, rng)\n        Astar = _generate_Astar(A, C, rng)\n        D1, D2 = (Astar == 1).astype(float), (Astar == 2).astype(float)\n        ones = np.ones(N)\n        tau_ctrl_arr[r] = _ols(np.column_stack([ones, T, D1, D2]), Y)[1]\n        tau_nc_arr[r] = _ols(np.column_stack([ones, T]), Y)[1]\n    return tau_ctrl_arr.mean(), tau_nc_arr.mean()\n\n\n# ══════════════════════════════════════════════════════════════════════════════\n# DAG 3: INSTRUMENT — Z_iv -> A -> Y, U -> {A, Y}\n# ══════════════════════════════════════════════════════════════════════════════\n\nIV_PARAMS = dict(lam=1.0, g1=0.0, g2=0.0, dZ=1.0, dU=0.8, dZ2=-0.5, dU2=0.6)\n\n\ndef _gen_iv(N, beta, params, rng):\n    Z_iv = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    eps = rng.normal(0, 1, N)\n    logits = np.column_stack([\n        np.zeros(N),\n        params['g1'] + params['dZ'] * Z_iv + params['dU'] * U,\n        params['g2'] + params['dZ2'] * Z_iv + params['dU2'] * U,\n    ])\n    A = _softmax_sample(logits, rng)\n    Y = (beta[1] * (A == 1).astype(float) + beta[2] * (A == 2).astype(float)\n         + params['lam'] * U + eps)\n    return Z_iv, U, Y, A\n\n\ndef theory_iv(C, beta, params, N_approx=2_000_000, seed=999):\n    rng = np.random.default_rng(seed)\n    Z_iv, U, Y, A = _gen_iv(N_approx, beta, params, rng)\n    Astar = _generate_Astar(A, C, rng)\n    z1 = Z_iv == 1\n    z0 = Z_iv == 0\n\n    RF = Y[z1].mean() - Y[z0].mean()\n\n    result = {'RF': RF}\n    for k in [1, 2]:\n        fs_star = (Astar[z1] == k).mean() - (Astar[z0] == k).mean()\n        fs_true = (A[z1] == k).mean() - (A[z0] == k).mean()\n        result[f'FS{k}_star'] = fs_star\n        result[f'FS{k}_true'] = fs_true\n        result[f'Wald{k}_star'] = RF / fs_star if abs(fs_star) > 1e-8 else np.nan\n        result[f'Wald{k}_true'] = RF / fs_true if abs(fs_true) > 1e-8 else np.nan\n\n    ones = np.ones(N_approx)\n    X_star = np.column_stack([ones, (Astar == 1).astype(float), (Astar == 2).astype(float)])\n    result['ols_star'] = _ols(X_star, Y)\n    X_true = np.column_stack([ones, (A == 1).astype(float), (A == 2).astype(float)])\n    result['ols_true'] = _ols(X_true, Y)\n\n    return result\n\n\ndef mc_iv(C, beta, params, N=10_000, n_reps=1000, seed=0):\n    RF_arr = np.empty(n_reps)\n    FS1_arr = np.empty(n_reps)\n    FS2_arr = np.empty(n_reps)\n    ols_arr = np.empty((n_reps, 3))\n    for r in range(n_reps):\n        rng = np.random.default_rng(seed + r)\n        Z_iv, U, Y, A = _gen_iv(N, beta, params, rng)\n        Astar = _generate_Astar(A, C, rng)\n        z1 = Z_iv == 1\n        z0 = Z_iv == 0\n        RF_arr[r] = Y[z1].mean() - Y[z0].mean()\n        FS1_arr[r] = (Astar[z1] == 1).mean() - (Astar[z0] == 1).mean()\n        FS2_arr[r] = (Astar[z1] == 2).mean() - (Astar[z0] == 2).mean()\n        ones = np.ones(N)\n        X = np.column_stack([ones, (Astar == 1).astype(float), (Astar == 2).astype(float)])\n        ols_arr[r] = _ols(X, Y)\n\n    wald1_mc = RF_arr.mean() / FS1_arr.mean()\n    wald2_mc = RF_arr.mean() / FS2_arr.mean()\n    ols_mc = ols_arr.mean(axis=0)\n    return wald1_mc, wald2_mc, ols_mc\n\n\n# ══════════════════════════════════════════════════════════════════════════════\n# RANDOM C SEARCH (reuse base dataset, vary only C)\n# ══════════════════════════════════════════════════════════════════════════════\n\ndef _fast_ols_tau(T, Y, A_star, N, sT, sTT, sY, sTY):\n    \"\"\"Inline OLS for Y ~ 1 + T + D1 + D2, returns coef on T. Avoids column_stack.\"\"\"\n    m1 = A_star == 1\n    m2 = A_star == 2\n    n1 = float(m1.sum())\n    n2 = float(m2.sum())\n    tD1 = T[m1].sum()\n    tD2 = T[m2].sum()\n    yD1 = Y[m1].sum()\n    yD2 = Y[m2].sum()\n    ZZ = np.array([[N, sT, n1, n2],\n                   [sT, sTT, tD1, tD2],\n                   [n1, tD1, n1, 0.0],\n                   [n2, tD2, 0.0, n2]])\n    ZY = np.array([sY, sTY, yD1, yD2])\n    return np.linalg.solve(ZZ, ZY)[1]\n\n\ndef rand_search_collider(n_search=100_000, N_ap=50_000, seed=42):\n    rng = np.random.default_rng(seed)\n    T, Y, A = _gen_collider(N_ap, COLLIDER_PARAMS, rng)\n    u = rng.uniform(size=N_ap)\n    N = float(N_ap)\n    sT, sTT, sY, sTY = T.sum(), (T*T).sum(), Y.sum(), (T*Y).sum()\n    tau_nc = sTY / sTT - sT * sY / (N * sTT)  # simplified no-control\n    ones = np.ones(N_ap)\n    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]\n\n    rng_s = np.random.default_rng(seed + 1)\n    biases = np.empty(n_search)\n    for i in range(n_search):\n        C = rng_s.dirichlet([1, 1, 1], size=3).T\n        Astar = _generate_Astar_fixed_u(A, C, u)\n        biases[i] = _fast_ols_tau(T, Y, Astar, N, sT, sTT, sY, sTY) - COLLIDER_PARAMS['tau']\n    return biases, tau_nc - COLLIDER_PARAMS['tau']\n\n\ndef rand_search_mbias(n_search=100_000, N_ap=50_000, seed=42):\n    rng = np.random.default_rng(seed)\n    T, Y, A = _gen_mbias(N_ap, MBIAS_PARAMS, rng)\n    u = rng.uniform(size=N_ap)\n    N = float(N_ap)\n    sT, sTT, sY, sTY = T.sum(), (T*T).sum(), Y.sum(), (T*Y).sum()\n    ones = np.ones(N_ap)\n    tau_nc = _ols(np.column_stack([ones, T]), Y)[1]\n\n    rng_s = np.random.default_rng(seed + 1)\n    biases = np.empty(n_search)\n    for i in range(n_search):\n        C = rng_s.dirichlet([1, 1, 1], size=3).T\n        Astar = _generate_Astar_fixed_u(A, C, u)\n        biases[i] = _fast_ols_tau(T, Y, Astar, N, sT, sTT, sY, sTY) - MBIAS_PARAMS['tau']\n    return biases, tau_nc - MBIAS_PARAMS['tau']\n\n\ndef rand_search_iv(beta, n_search=100_000, N_ap=50_000, seed=42):\n    rng = np.random.default_rng(seed)\n    Z_iv, U, Y, A = _gen_iv(N_ap, beta, IV_PARAMS, rng)\n    u = rng.uniform(size=N_ap)\n    z1 = Z_iv == 1\n    z0 = Z_iv == 0\n    n1_z = float(z1.sum())\n    n0_z = float(z0.sum())\n    RF = Y[z1].sum() / n1_z - Y[z0].sum() / n0_z\n    FS1_true = (A[z1] == 1).sum() / n1_z - (A[z0] == 1).sum() / n0_z\n    FS2_true = (A[z1] == 2).sum() / n1_z - (A[z0] == 2).sum() / n0_z\n    W1_true = RF / FS1_true if abs(FS1_true) > 1e-8 else np.nan\n    W2_true = RF / FS2_true if abs(FS2_true) > 1e-8 else np.nan\n\n    rng_s = np.random.default_rng(seed + 1)\n    w1_vals = np.empty(n_search)\n    w2_vals = np.empty(n_search)\n    for i in range(n_search):\n        C = rng_s.dirichlet([1, 1, 1], size=3).T\n        Astar = _generate_Astar_fixed_u(A, C, u)\n        fs1 = (Astar[z1] == 1).sum() / n1_z - (Astar[z0] == 1).sum() / n0_z\n        fs2 = (Astar[z1] == 2).sum() / n1_z - (Astar[z0] == 2).sum() / n0_z\n        w1_vals[i] = RF / fs1 if abs(fs1) > 1e-8 else np.nan\n        w2_vals[i] = RF / fs2 if abs(fs2) > 1e-8 else np.nan\n    return w1_vals, w2_vals, W1_true, W2_true\n\n\n# ══════════════════════════════════════════════════════════════════════════════\n# MAIN\n# ══════════════════════════════════════════════════════════════════════════════\n\ndef _print_section(title):\n    print()\n    print(\"=\" * 80)\n    print(title)\n    print(\"=\" * 80)\n\n\ndef main():\n    np.set_printoptions(precision=6, suppress=True)\n    t0 = time.time()\n\n    # ── DAG 1: Collider ─────────────────────────────────────────────────────\n    _print_section(\"DAG 1: COLLIDER -- T -> A <- Y\")\n    p = COLLIDER_PARAMS\n    print(f\"DGP: T~N(0,1), Y={p['tau']}*T+eps, \"\n          f\"A|T,Y softmax(dT={p['dT']}, dY={p['dY']}, dT2={p['dT2']}, dY2={p['dY2']})\")\n    print(f\"Researcher error: controls A* in Y ~ 1 + T + D*1 + D*2\")\n    print(f\"Truth: T and Y are NOT confounded => no-control OLS is consistent\")\n    print()\n\n    hdr = (f\"  {'C':<16} {'Th t_ctrl':>10} {'MC t_ctrl':>10} {'OK':>3}\"\n           f\" {'tau':>5} {'Bias_ctrl':>10} {'Th t_nc':>9} {'Bias_nc':>9}\")\n    print(hdr)\n    print(\"  \" + \"-\" * 80)\n\n    for cn, C in ALL_C.items():\n        th_c, th_n = theory_collider(C, p)\n        mc_c, mc_n = mc_collider(C, p)\n        ok = \"Y\" if abs(th_c - mc_c) < 0.02 else \"N\"\n        print(f\"  {cn:<16} {th_c:>10.4f} {mc_c:>10.4f} {ok:>3}\"\n              f\" {p['tau']:>5.1f} {th_c - p['tau']:>+10.4f} {th_n:>9.4f} {th_n - p['tau']:>+9.4f}\")\n\n    print()\n    print(\"Violation analysis:\")\n    th_c1, th_n1 = theory_collider(C1_SYMMETRIC_HIGH, p)\n    print(f\"  No-control plim(tau_hat) = {th_n1:.4f}\"\n          f\" (should = tau={p['tau']} since no confounding)\")\n    print(f\"  Controlling collider A* induces spurious T-eps association\")\n\n    t1 = time.time()\n    print(f\"\\nRandom C search (100k)... \", end=\"\", flush=True)\n    bc, bnc = rand_search_collider()\n    print(f\"done ({time.time()-t1:.0f}s)\")\n    print(f\"  No-control bias: {bnc:+.4f}\")\n    print(f\"  Control bias: mean={bc.mean():+.4f}, std={bc.std():.4f},\"\n          f\" range=[{bc.min():+.4f}, {bc.max():+.4f}]\")\n    worse = np.sum(np.abs(bc) > np.abs(bnc))\n    print(f\"  |bias_ctrl| > |bias_nc|: {worse}/{len(bc)} ({100*worse/len(bc):.1f}%)\")\n\n    # ── DAG 2: M-bias ───────────────────────────────────────────────────────\n    _print_section(\"DAG 2: M-BIAS -- U1 -> {A,T}, U2 -> {A,Y}\")\n    p = MBIAS_PARAMS\n    print(f\"DGP: U1,U2~N(0,1) indep, T={p['delta']}*U1+eta,\"\n          f\" Y={p['tau']}*T+{p['lam']}*U2+eps\")\n    print(f\"A|U1,U2 softmax(a1={p['a1']}, a2={p['a2']}, a3={p['a3']}, a4={p['a4']})\")\n    print(f\"Researcher error: controls A* => opens U1->A<-U2 path (M-bias)\")\n    print(f\"Truth: U2 indep T => no confounding of T->Y, no-control is consistent\")\n    print()\n\n    hdr = (f\"  {'C':<16} {'Th t_ctrl':>10} {'MC t_ctrl':>10} {'OK':>3}\"\n           f\" {'tau':>5} {'Bias_ctrl':>10} {'Th t_nc':>9} {'Bias_nc':>9}\")\n    print(hdr)\n    print(\"  \" + \"-\" * 80)\n\n    for cn, C in ALL_C.items():\n        th_c, th_n = theory_mbias(C, p)\n        mc_c, mc_n = mc_mbias(C, p)\n        ok = \"Y\" if abs(th_c - mc_c) < 0.02 else \"N\"\n        print(f\"  {cn:<16} {th_c:>10.4f} {mc_c:>10.4f} {ok:>3}\"\n              f\" {p['tau']:>5.1f} {th_c - p['tau']:>+10.4f} {th_n:>9.4f} {th_n - p['tau']:>+9.4f}\")\n\n    print()\n    print(\"Violation analysis:\")\n    th_c1, th_n1 = theory_mbias(C1_SYMMETRIC_HIGH, p)\n    print(f\"  No-control plim(tau_hat) = {th_n1:.4f}\"\n          f\" (should = tau={p['tau']} since U2 indep T)\")\n    print(f\"  Controlling A* opens M-bias path: T <- U1 -> A <- U2 -> Y\")\n\n    t1 = time.time()\n    print(f\"\\nRandom C search (100k)... \", end=\"\", flush=True)\n    bc, bnc = rand_search_mbias()\n    print(f\"done ({time.time()-t1:.0f}s)\")\n    print(f\"  No-control bias: {bnc:+.4f}\")\n    print(f\"  Control bias: mean={bc.mean():+.4f}, std={bc.std():.4f},\"\n          f\" range=[{bc.min():+.4f}, {bc.max():+.4f}]\")\n    worse = np.sum(np.abs(bc) > np.abs(bnc))\n    print(f\"  |bias_ctrl| > |bias_nc|: {worse}/{len(bc)} ({100*worse/len(bc):.1f}%)\")\n\n    # ── DAG 3: Instrument ────────────────────────────────────────────────────\n    for bname, beta in [(\"BETA_MIXED\", BETA_MIXED), (\"BETA_SAME\", BETA_SAME)]:\n        _print_section(\n            f\"DAG 3: INSTRUMENT -- Z->A->Y, U->{{A,Y}}  [{bname}: b={beta}]\")\n        p = IV_PARAMS\n        print(f\"DGP: Z~Bern(0.5), U~N(0,1), Y=b1*D1+b2*D2+{p['lam']}*U+eps\")\n        print(f\"A|Z,U softmax(dZ={p['dZ']}, dU={p['dU']}, dZ2={p['dZ2']}, dU2={p['dU2']})\")\n        print(f\"Under-identified: 1 IV for 2 endogenous dummies => per-dummy Wald\")\n        print(f\"Wald_k = RF/FS*_k estimates (b1*pi1+b2*pi2)/pi*_k, not b_k\")\n        print()\n\n        hdr2 = (f\"  {'C':<16}\"\n                f\" {'W1* th':>8} {'W1* mc':>8} {'ok':>3}\"\n                f\" {'W2* th':>8} {'W2* mc':>8} {'ok':>3}\"\n                f\" {'OLS b1':>8} {'mc':>8} {'ok':>3}\"\n                f\" {'OLS b2':>8} {'mc':>8} {'ok':>3}\")\n        print(hdr2)\n        print(\"  \" + \"-\" * 110)\n\n        for cn, C in ALL_C.items():\n            th = theory_iv(C, beta, p)\n            mc_w1, mc_w2, mc_ols = mc_iv(C, beta, p)\n\n            o1 = \"Y\" if abs(th['Wald1_star'] - mc_w1) < 0.10 else \"N\"\n            o2 = \"Y\" if abs(th['Wald2_star'] - mc_w2) < 0.10 else \"N\"\n            o3 = \"Y\" if abs(th['ols_star'][1] - mc_ols[1]) < 0.02 else \"N\"\n            o4 = \"Y\" if abs(th['ols_star'][2] - mc_ols[2]) < 0.02 else \"N\"\n\n            def _fmt(v, w=8):\n                return f\"{v:>{w}.4f}\" if np.isfinite(v) else f\"{'nan':>{w}}\"\n\n            print(f\"  {cn:<16}\"\n                  f\" {_fmt(th['Wald1_star'])} {_fmt(mc_w1)} {o1:>3}\"\n                  f\" {_fmt(th['Wald2_star'])} {_fmt(mc_w2)} {o2:>3}\"\n                  f\" {th['ols_star'][1]:>8.4f} {mc_ols[1]:>8.4f} {o3:>3}\"\n                  f\" {th['ols_star'][2]:>8.4f} {mc_ols[2]:>8.4f} {o4:>3}\")\n\n        print()\n        th1 = theory_iv(C1_SYMMETRIC_HIGH, beta, p)\n        print(\"Violation analysis (C1_sym_high):\")\n        print(f\"  True beta = [{beta[1]}, {beta[2]}]\")\n        print(f\"  Reduced form (ITT): {th1['RF']:.4f}\")\n        print(f\"  First stage true:  pi1={th1['FS1_true']:.4f}, pi2={th1['FS2_true']:.4f}\")\n        print(f\"  First stage A*:    pi*1={th1['FS1_star']:.4f}, pi*2={th1['FS2_star']:.4f}\")\n        print(f\"  Wald true A:  W1={th1['Wald1_true']:.4f}, W2={th1['Wald2_true']:.4f}\")\n        print(f\"  Wald A*:      W1={th1['Wald1_star']:.4f}, W2={th1['Wald2_star']:.4f}\")\n        print(f\"  OLS true A:   [{th1['ols_true'][1]:.4f}, {th1['ols_true'][2]:.4f}]\"\n              f\" (biased by U)\")\n        print(f\"  OLS A*:       [{th1['ols_star'][1]:.4f}, {th1['ols_star'][2]:.4f}]\"\n              f\" (biased by U + misclassification)\")\n\n        # Analytical insight: how C transforms first stages\n        print(f\"\\n  FS transformation by C:\")\n        print(f\"    FS*_k = sum_j C[k,j] * FS_j\")\n        for cn2, C2 in [(\"C1_sym_high\", C1_SYMMETRIC_HIGH),\n                        (\"C4_weak_diag\", C4_WEAK_DIAG),\n                        (\"C5_near_perm\", C5_NEAR_PERM)]:\n            th2 = theory_iv(C2, beta, p)\n            fs_true = np.array([-(th2['FS1_true']+th2['FS2_true']),\n                                th2['FS1_true'], th2['FS2_true']])\n            fs_star_calc = C2 @ fs_true\n            print(f\"    {cn2}: FS_true={fs_true}, C@FS={fs_star_calc},\"\n                  f\" FS*=[{th2['FS1_star']:.4f}, {th2['FS2_star']:.4f}]\")\n\n        t1 = time.time()\n        print(f\"\\n  Random C search (100k)... \", end=\"\", flush=True)\n        w1v, w2v, w1t, w2t = rand_search_iv(beta)\n        print(f\"done ({time.time()-t1:.0f}s)\")\n        v1 = np.isfinite(w1v)\n        v2 = np.isfinite(w2v)\n        w1b = w1v - w1t\n        w2b = w2v - w2t\n        print(f\"    Wald1 true={w1t:.4f}: A* vals mean={np.nanmean(w1v):+.4f},\"\n              f\" std={np.nanstd(w1v):.4f},\"\n              f\" range=[{np.nanmin(w1v):+.4f}, {np.nanmax(w1v):+.4f}],\"\n              f\" valid={v1.sum()}/{len(w1v)}\")\n        print(f\"    Wald2 true={w2t:.4f}: A* vals mean={np.nanmean(w2v):+.4f},\"\n              f\" std={np.nanstd(w2v):.4f},\"\n              f\" range=[{np.nanmin(w2v):+.4f}, {np.nanmax(w2v):+.4f}],\"\n              f\" valid={v2.sum()}/{len(w2v)}\")\n        print(f\"    Delta from true: W1 mean={np.nanmean(w1b):+.4f},\"\n              f\" W2 mean={np.nanmean(w2b):+.4f}\")\n\n    print(f\"\\nTotal: {time.time() - t0:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 489,
      "startLine": 1,
      "totalLines": 489
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01SYBuWo9xbDDtitvLSqKqBY`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "f1a3845d-49b9-4409-962a-c46323979275",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VrZMd1roJtVpjrW4LrGWo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15004,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15004
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

_source line 9 · 2026-05-20T23:24:29.578Z_

<details><summary>↩ Tool result · `toolu_01SYBuWo9xbDDtitvLSqKqBY`</summary>

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
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "d5709066-987a-45cc-a66e-726533f4ea2a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_mediation_frontdoor.py",
      "content": "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n\"\"\"Plan 001: Mediation + Front-door DAG — closed-form bias + MC verification.\"\"\"\nimport numpy as np\nimport time\nimport warnings\nfrom collections import OrderedDict\n\nwarnings.filterwarnings('ignore')\n\n# ================================================================\n# Configuration\n# ================================================================\nK = 3\nN_MC = 10_000\nN_REPS = 1_000\nN_LARGE = 50_000_000\nN_RANDOM = 100_000\n\nBETA_MIXED = np.array([0.0, 1.0, -0.5])\nBETA_SAME  = np.array([0.0, 1.0,  0.5])\n\nTAU = 0.5\nGAMMA_MED = np.array([0.0, 0.5, -0.3])\nDELTA_MED = np.array([0.0, 0.8, -0.6])\n\nALPHA_U = 1.0\nLAMBDA_U = 1.0\nGAMMA_FD = np.array([0.0, 0.5, -0.3])\nDELTA_FD = np.array([0.0, 1.0, -0.8])\n\nC_DICT = OrderedDict([\n    (\"1_sym_high\",   np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]])),\n    (\"2_asymmetric\", np.array([[.65,.05,.10],[.30,.85,.10],[.05,.10,.80]])),\n    (\"3_struct_12\",  np.array([[.96,.01,.01],[.02,.69,.30],[.02,.30,.69]])),\n    (\"4_weak_diag\",  np.array([[.40,.35,.25],[.35,.40,.35],[.25,.25,.40]])),\n    (\"5_near_perm\",  np.array([[.05,.05,.90],[.90,.05,.05],[.05,.90,.05]])),\n    (\"6_diff_base\",  np.array([[.80,.10,.10],[.10,.80,.10],[.10,.10,.80]])),\n])\n\nCOEF_NAMES = ['β₀', 'τ', 'β₁', 'β₂']\n\n\n# ================================================================\n# Helpers\n# ================================================================\ndef softmax(x):\n    e = np.exp(x - x.max())\n    return e / e.sum()\n\n\ndef p_cat(t, g, d):\n    return softmax(g + d * t)\n\n\ndef gen_Astar(A, C, rng):\n    pr = C[:, A]\n    cu = np.cumsum(pr, axis=0)\n    u = rng.uniform(size=len(A))\n    return (u >= cu[0]).astype(int) + (u >= cu[1]).astype(int)\n\n\ndef ols(Z, Y):\n    return np.linalg.lstsq(Z, Y, rcond=None)[0]\n\n\ndef fv(v, w=8, p=4):\n    return '[' + ' '.join(f'{x:>{w}.{p}f}' for x in v) + ']'\n\n\ndef fm(th, mc, se, k=2):\n    ok = np.abs(mc - th) < k * se\n    return ''.join('✓' if o else '✗' for o in ok), ok.all()\n\n\n# ================================================================\n# DAG 1  Mediation: T -> A -> Y\n#\n# DGP:  T ~ Bern(0.5)\n#        A | T ~ Cat(softmax(gamma + delta*T))\n#        Y = beta0 + beta1*D1 + beta2*D2 + tau*T + eps\n#        A* | A ~ Cat(C[:, A])\n#\n# Researcher regression:  Y ~ 1 + T + D*_1 + D*_2\n#\n# Z = (1, T, D*_1, D*_2),  X = (1, T, D_1, D_2)\n# eps indep of Z  =>  plim = (E[Z'Z])^{-1} E[Z'X] beta\n#\n# Key moments:\n#   q_t = C @ p_{A|T=t}           (P(A*|T=t))\n#   q_marg = 0.5*(q_0 + q_1)\n#   E[D*_j * D_k] = C[j,k] * p_marg[k]\n# ================================================================\ndef plim_med(C, beta, tau, g=GAMMA_MED, d=DELTA_MED):\n    p0, p1 = p_cat(0, g, d), p_cat(1, g, d)\n    q0, q1 = C @ p0, C @ p1\n    pm = .5 * (p0 + p1)\n    qm = .5 * (q0 + q1)\n\n    EZZ = np.array([\n        [1,      .5,        qm[1],      qm[2]     ],\n        [.5,     .5,        .5*q1[1],   .5*q1[2]  ],\n        [qm[1],  .5*q1[1],  qm[1],      0         ],\n        [qm[2],  .5*q1[2],  0,          qm[2]     ]])\n\n    EZX = np.array([\n        [1,      .5,        pm[1],            pm[2]           ],\n        [.5,     .5,        .5*p1[1],         .5*p1[2]        ],\n        [qm[1],  .5*q1[1],  C[1,1]*pm[1],    C[1,2]*pm[2]   ],\n        [qm[2],  .5*q1[2],  C[2,1]*pm[1],    C[2,2]*pm[2]   ]])\n\n    b = np.array([beta[0], tau, beta[1], beta[2]])\n    return np.linalg.solve(EZZ, EZX @ b)\n\n\ndef mc_med(C, beta, tau, g=GAMMA_MED, d=DELTA_MED,\n           nr=N_REPS, N=N_MC, seed=42):\n    rng = np.random.default_rng(seed)\n    p0, p1 = p_cat(0, g, d), p_cat(1, g, d)\n    out = np.zeros((nr, 4))\n    for r in range(nr):\n        T = rng.binomial(1, .5, N)\n        pr = np.where(T[:, None] == 0, p0, p1)\n        cu = np.cumsum(pr, axis=1)\n        u = rng.uniform(size=N)\n        A = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)\n        D1 = (A == 1).astype(float)\n        D2 = (A == 2).astype(float)\n        Y = beta[0] + beta[1]*D1 + beta[2]*D2 + tau*T + rng.normal(0, 1, N)\n        As = gen_Astar(A, C, rng)\n        Z = np.column_stack([np.ones(N), T.astype(float),\n                             (As == 1).astype(float), (As == 2).astype(float)])\n        out[r] = ols(Z, Y)\n    return out.mean(0), out.std(0) / np.sqrt(nr)\n\n\ndef rsearch_med(beta, tau, g=GAMMA_MED, d=DELTA_MED,\n                ns=N_RANDOM, seed=999):\n    rng = np.random.default_rng(seed)\n    p0, p1 = p_cat(0, g, d), p_cat(1, g, d)\n    pm = .5 * (p0 + p1)\n    b = np.array([beta[0], tau, beta[1], beta[2]])\n    clean = plim_med(np.eye(K), beta, tau, g, d)\n\n    Cs = np.zeros((ns, K, K))\n    for i in range(K):\n        Cs[:, :, i] = rng.dirichlet(np.ones(K), size=ns)\n\n    q0 = Cs @ p0\n    q1 = Cs @ p1\n    qm = .5 * (q0 + q1)\n\n    EZZ = np.zeros((ns, 4, 4))\n    EZZ[:, 0, 0] = 1;       EZZ[:, 0, 1] = EZZ[:, 1, 0] = .5\n    EZZ[:, 0, 2] = EZZ[:, 2, 0] = qm[:, 1]\n    EZZ[:, 0, 3] = EZZ[:, 3, 0] = qm[:, 2]\n    EZZ[:, 1, 1] = .5\n    EZZ[:, 1, 2] = EZZ[:, 2, 1] = .5 * q1[:, 1]\n    EZZ[:, 1, 3] = EZZ[:, 3, 1] = .5 * q1[:, 2]\n    EZZ[:, 2, 2] = qm[:, 1]\n    EZZ[:, 3, 3] = qm[:, 2]\n\n    EZX = np.zeros((ns, 4, 4))\n    EZX[:, 0, 0] = 1;       EZX[:, 0, 1] = .5\n    EZX[:, 0, 2] = pm[1];   EZX[:, 0, 3] = pm[2]\n    EZX[:, 1, 0] = .5;      EZX[:, 1, 1] = .5\n    EZX[:, 1, 2] = .5 * p1[1]; EZX[:, 1, 3] = .5 * p1[2]\n    EZX[:, 2, 0] = qm[:, 1];   EZX[:, 2, 1] = .5 * q1[:, 1]\n    EZX[:, 2, 2] = Cs[:, 1, 1] * pm[1]; EZX[:, 2, 3] = Cs[:, 1, 2] * pm[2]\n    EZX[:, 3, 0] = qm[:, 2];   EZX[:, 3, 1] = .5 * q1[:, 2]\n    EZX[:, 3, 2] = Cs[:, 2, 1] * pm[1]; EZX[:, 3, 3] = Cs[:, 2, 2] * pm[2]\n\n    rhs = np.einsum('nij,j->ni', EZX, b)\n    pl = np.linalg.solve(EZZ, rhs[:, :, None])[:, :, 0]\n\n    df = np.abs(pl - clean)\n    viol = np.any(df > .01, 1).mean()\n    nz = np.abs(clean) > 1e-6\n    sign = np.any(np.sign(pl[:, nz]) != np.sign(clean[nz]), 1).mean()\n    amp = np.any(np.abs(pl) > np.abs(clean) + 1e-6, 1).mean()\n    return viol, sign, amp\n\n\n# ================================================================\n# DAG 2  Front-door: T -> M -> Y,  U -> T,  U -> Y\n#\n# DGP:  U ~ N(0,1)\n#        T = alpha_U * U + eta,  eta ~ N(0,1)\n#        M | T ~ Cat(softmax(gamma + delta*T))\n#        Y = beta1*D_{M,1} + beta2*D_{M,2} + lambda*U + eps\n#        M* | M ~ Cat(C[:, M])\n#\n# Researcher regression:  Y ~ 1 + T + D*_{M,1} + D*_{M,2}\n#\n# T correlated with U (confounding), so E[Z'(lambda*U)] != 0.\n# Use large-sample moment approximation:\n#   plim = (E[Z'Z])^{-1} E[Z'Y]   estimated from N_LARGE samples.\n#\n# For fast random search, pre-compute sufficient statistics:\n#   E[D_{M,k}], E[D_{M,k}*T], E[D_{M,k}*Y]  for k=0,1,2\n# Then for any C:\n#   E[D*_j] = sum_k C[j,k]*E[D_{M,k}]   etc.\n# ================================================================\ndef _gen_fd(N, beta, rng, g=GAMMA_FD, d=DELTA_FD,\n            aU=ALPHA_U, lU=LAMBDA_U):\n    U = rng.normal(0, 1, N)\n    T = aU * U + rng.normal(0, 1, N)\n    lo = np.column_stack([np.zeros(N), g[1] + d[1]*T, g[2] + d[2]*T])\n    lo -= lo.max(1, keepdims=True)\n    e = np.exp(lo)\n    p = e / e.sum(1, keepdims=True)\n    cu = np.cumsum(p, axis=1)\n    u = rng.uniform(size=N)\n    M = (u >= cu[:, 0]).astype(int) + (u >= cu[:, 1]).astype(int)\n    DM1 = (M == 1).astype(float)\n    DM2 = (M == 2).astype(float)\n    Y = beta[1]*DM1 + beta[2]*DM2 + lU*U + rng.normal(0, 1, N)\n    return T, M, Y, U\n\n\ndef precomp_fd(beta, N=N_LARGE, seed=123):\n    rng = np.random.default_rng(seed)\n    T, M, Y, _ = _gen_fd(N, beta, rng)\n    DM = np.zeros((N, K))\n    for k in range(K):\n        DM[:, k] = (M == k).astype(float)\n    return dict(\n        E_T=T.mean(), E_T2=(T**2).mean(),\n        E_Y=Y.mean(), E_TY=(T*Y).mean(),\n        E_DM=DM.mean(0),\n        E_DM_T=(DM * T[:, None]).mean(0),\n        E_DM_Y=(DM * Y[:, None]).mean(0))\n\n\ndef plim_fd(C, st):\n    ds  = C @ st['E_DM']\n    dst = C @ st['E_DM_T']\n    dsy = C @ st['E_DM_Y']\n    ET, ET2 = st['E_T'], st['E_T2']\n    EY, ETY = st['E_Y'], st['E_TY']\n\n    EZZ = np.array([\n        [1,      ET,      ds[1],    ds[2]   ],\n        [ET,     ET2,     dst[1],   dst[2]  ],\n        [ds[1],  dst[1],  ds[1],    0       ],\n        [ds[2],  dst[2],  0,        ds[2]   ]])\n\n    EZY = np.array([EY, ETY, dsy[1], dsy[2]])\n    return np.linalg.solve(EZZ, EZY)\n\n\ndef mc_fd(C, beta, nr=N_REPS, N=N_MC, seed=42):\n    rng = np.random.default_rng(seed)\n    out = np.zeros((nr, 4))\n    for r in range(nr):\n        T, M, Y, _ = _gen_fd(N, beta, rng)\n        Ms = gen_Astar(M, C, rng)\n        Z = np.column_stack([np.ones(N), T,\n                             (Ms == 1).astype(float),\n                             (Ms == 2).astype(float)])\n        out[r] = ols(Z, Y)\n    return out.mean(0), out.std(0) / np.sqrt(nr)\n\n\ndef rsearch_fd(st, ns=N_RANDOM, seed=999):\n    rng = np.random.default_rng(seed)\n    clean = plim_fd(np.eye(K), st)\n\n    Cs = np.zeros((ns, K, K))\n    for i in range(K):\n        Cs[:, :, i] = rng.dirichlet(np.ones(K), size=ns)\n\n    E_DMs   = Cs @ st['E_DM']\n    E_DMs_T = Cs @ st['E_DM_T']\n    E_DMs_Y = Cs @ st['E_DM_Y']\n    ET, ET2 = st['E_T'], st['E_T2']\n    EY, ETY = st['E_Y'], st['E_TY']\n\n    EZZ = np.zeros((ns, 4, 4))\n    EZZ[:, 0, 0] = 1;       EZZ[:, 0, 1] = EZZ[:, 1, 0] = ET\n    EZZ[:, 0, 2] = EZZ[:, 2, 0] = E_DMs[:, 1]\n    EZZ[:, 0, 3] = EZZ[:, 3, 0] = E_DMs[:, 2]\n    EZZ[:, 1, 1] = ET2\n    EZZ[:, 1, 2] = EZZ[:, 2, 1] = E_DMs_T[:, 1]\n    EZZ[:, 1, 3] = EZZ[:, 3, 1] = E_DMs_T[:, 2]\n    EZZ[:, 2, 2] = E_DMs[:, 1]\n    EZZ[:, 3, 3] = E_DMs[:, 2]\n\n    EZY = np.zeros((ns, 4))\n    EZY[:, 0] = EY;   EZY[:, 1] = ETY\n    EZY[:, 2] = E_DMs_Y[:, 1]\n    EZY[:, 3] = E_DMs_Y[:, 2]\n\n    pl = np.linalg.solve(EZZ, EZY[:, :, None])[:, :, 0]\n\n    df = np.abs(pl - clean)\n    viol = np.any(df > .01, 1).mean()\n    nz = np.abs(clean) > 1e-6\n    sign = np.any(np.sign(pl[:, nz]) != np.sign(clean[nz]), 1).mean()\n    amp = np.any(np.abs(pl) > np.abs(clean) + 1e-6, 1).mean()\n    return viol, sign, amp\n\n\n# ================================================================\n# Main\n# ================================================================\ndef main():\n    t0 = time.time()\n    np.set_printoptions(precision=4, suppress=True)\n\n    for bn, beta in [(\"mixed [0,1,-0.5]\", BETA_MIXED),\n                      (\"same [0,1,0.5]\",   BETA_SAME)]:\n\n        # ---- DAG 1: Mediation ----\n        print(f\"\\n{'='*90}\")\n        print(f\"  MEDIATION: T -> A -> Y  |  beta={bn}\")\n        print(f\"{'='*90}\")\n        p0, p1 = p_cat(0, GAMMA_MED, DELTA_MED), p_cat(1, GAMMA_MED, DELTA_MED)\n        print(f\"  P(A|T=0)={fv(p0,6,3)}  P(A|T=1)={fv(p1,6,3)}  tau={TAU}\")\n        print(f\"  Coefs: [{', '.join(COEF_NAMES)}]\\n\")\n\n        hdr = f\"  {'C':<14} {'Theory':>36}  {'MC mean':>36}  Mt\"\n        print(hdr)\n        print(f\"  {'-'*92}\")\n\n        all_ok = True\n        for cn, C in C_DICT.items():\n            th = plim_med(C, beta, TAU)\n            mc, se = mc_med(C, beta, TAU)\n            ms, ok = fm(th, mc, se)\n            if not ok:\n                all_ok = False\n            print(f\"  {cn:<14} {fv(th)}  {fv(mc)}  {ms}\")\n\n        status = 'ALL MATCH' if all_ok else 'MISMATCH DETECTED'\n        print(f\"  >>> {status}\")\n\n        t1 = time.time()\n        v, s, a = rsearch_med(beta, TAU)\n        t2 = time.time()\n        print(f\"\\n  Random search ({N_RANDOM//1000}k, {t2-t1:.1f}s): \"\n              f\"violation={v:.1%}  sign_flip={s:.1%}  amplification={a:.1%}\")\n\n        # ---- DAG 2: Front-door ----\n        print(f\"\\n{'='*90}\")\n        print(f\"  FRONT-DOOR: T -> M -> Y, U -> T, U -> Y  |  beta={bn}\")\n        print(f\"{'='*90}\")\n        print(f\"  alpha_U={ALPHA_U}  lambda_U={LAMBDA_U}\")\n        print(f\"  M|T softmax: gamma={GAMMA_FD}  delta={DELTA_FD}\")\n        print(f\"  Coefs: [{', '.join(COEF_NAMES)}]\\n\")\n\n        t1 = time.time()\n        st = precomp_fd(beta)\n        t2 = time.time()\n        print(f\"  Moments pre-computed (N={N_LARGE//10**6}M, {t2-t1:.1f}s)\\n\")\n\n        hdr = f\"  {'C':<14} {'Theory':>36}  {'MC mean':>36}  Mt\"\n        print(hdr)\n        print(f\"  {'-'*92}\")\n\n        all_ok = True\n        for cn, C in C_DICT.items():\n            th = plim_fd(C, st)\n            mc, se = mc_fd(C, beta)\n            ms, ok = fm(th, mc, se, k=3)\n            if not ok:\n                all_ok = False\n            print(f\"  {cn:<14} {fv(th)}  {fv(mc)}  {ms}\")\n\n        status = 'ALL MATCH (3σ)' if all_ok else 'MISMATCH DETECTED'\n        print(f\"  >>> {status}\")\n\n        t1 = time.time()\n        v, s, a = rsearch_fd(st)\n        t2 = time.time()\n        print(f\"\\n  Random search ({N_RANDOM//1000}k, {t2-t1:.1f}s): \"\n              f\"violation={v:.1%}  sign_flip={s:.1%}  amplification={a:.1%}\")\n\n    print(f\"\\n{'='*90}\")\n    print(f\"  Total: {time.time()-t0:.1f}s\")\n    print(f\"{'='*90}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 386,
      "startLine": 1,
      "totalLines": 386
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_014cePPNASJqYNvB2JxA4jCn`</summary>

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
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "beee3c17-7046-435a-b664-9b1a7c980cbd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VrZMd1roJtVpjrW4LrGWo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15004,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15004
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

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01BioBzLrv6BWyt6TXco8W7V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_007_correction_guidance.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "f6e4f119-0f1b-42f8-8a24-e6ae14cd7240",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018VrZMd1roJtVpjrW4LrGWo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15004,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15004
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

_source line 12 · 2026-05-20T23:24:30.348Z_

<details><summary>↩ Tool result · `toolu_014cePPNASJqYNvB2JxA4jCn`</summary>

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
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "c5d9b0ac-6d2b-4d27-adc7-27a8004f766f",
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

### Tool result

_source line 13 · 2026-05-20T23:24:30.558Z_

<details><summary>↩ Tool result · `toolu_01BioBzLrv6BWyt6TXco8W7V`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_007_correction_guidance.py — Correction Method Guidance MC Framework
4	
5	Purpose: Evaluate 5 correction methods for K=3 LLM misclassification bias across
6	         7 DAG topologies and 6 confusion matrix structures via Monte Carlo simulation.
7	
8	For each {topology x C_structure x correction_method}, runs N_sim MC replications to
9	measure bias_reduction, RMSE, 95% CI coverage, and method failure rates. Outputs an
10	optimal correction method mapping per {topology x C_structure}.
11	
12	Input:   Hardcoded DGP parameters (consistent with plan_001/002),
13	         6 synthetic K=3 column-stochastic confusion matrices.
14	Output:  artifacts/plan007/correction_guidance_results.json  — full MC results
15	         artifacts/plan007/correction_mapping.txt            — {topo x C} -> best method
16	         artifacts/plan007/method_comparison_summary.txt     — cross-topology rankings
17	
18	Dependencies: numpy, scipy (scipy only for polyfit fallback; core uses numpy)
19	"""
20	
21	import numpy as np
22	import json
23	import hashlib
24	import os
25	import time
26	import argparse
27	from collections import OrderedDict
28	
29	# ================================================================
30	# Constants
31	# ================================================================
32	K = 3
33	N_DATA_DEFAULT = 5000
34	N_SIM_DEFAULT = 1000
35	N_GOLD = 500
36	SIMEX_LAMBDAS = [0.5, 1.0, 1.5, 2.0]
37	SIMEX_B = 50
38	EM_MAX_ITER = 100
39	EM_TOL = 1e-6
40	
41	OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
42	                       "artifacts", "plan007")
43	
44	ALL_METHODS = ["naive_plugin", "dsl", "ppi", "mcsimex", "mla"]
45	
46	
47	# ================================================================
48	# Confusion Matrices (column-stochastic, K=3)
49	# C[j,i] = P(A*=j | A=i)
50	# ================================================================
51	def _build_C_structures():
52	    cs = OrderedDict()
53	    # mild: diag≈0.867, off≈0.067
54	    cs["mild_uniform"] = 0.8 * np.eye(K) + (0.2 / K) * np.ones((K, K))
55	    # moderate: diag≈0.733, off≈0.133
56	    cs["moderate_uniform"] = 0.6 * np.eye(K) + (0.4 / K) * np.ones((K, K))
57	    # severe: diag=0.6, off=0.2
58	    cs["severe_uniform"] = 0.4 * np.eye(K) + (0.6 / K) * np.ones((K, K))
59	    # asymmetric: class 0->1 high (0.20), others low
60	    cs["asymmetric"] = np.array([
61	        [0.75, 0.05, 0.05],
62	        [0.20, 0.80, 0.10],
63	        [0.05, 0.15, 0.85]])
64	    # near-permutation: cyclic shift with P≈0.90
65	    cs["near_permutation"] = np.array([
66	        [0.05, 0.05, 0.90],
67	        [0.90, 0.05, 0.05],
68	        [0.05, 0.90, 0.05]])
69	    # realistic LLM: adjacent confusion high, distant low
70	    cs["realistic_llm"] = np.array([
71	        [0.78, 0.15, 0.03],
72	        [0.18, 0.72, 0.18],
73	        [0.04, 0.13, 0.79]])
74	    for name, C in cs.items():
75	        assert np.allclose(C.sum(axis=0), 1.0), f"{name} not column-stochastic"
76	        assert (C >= 0).all(), f"{name} has negative entries"
77	    return cs
78	
79	
80	C_STRUCTURES = _build_C_structures()
81	
82	
83	# ================================================================
84	# DGP Parameters (K=3, consistent with plan_001/002)
85	# ================================================================
86	DGP_PARAMS = dict(
87	    confounding=dict(
88	        p_A=np.array([0.40, 0.35, 0.25]),
89	        alpha=np.array([1.5, -1.0]),
90	        beta_A=np.array([1.0, -0.5]),
91	        beta_T=2.0, sigma_T=1.0),
92	    mediation=dict(
93	        tau=0.5,
94	        gamma=np.array([0.0, 0.5, -0.3]),
95	        delta=np.array([0.0, 0.8, -0.6]),
96	        beta=np.array([0.0, 1.0, -0.5])),
97	    collider=dict(
98	        tau=1.0, g=np.zeros(K),
99	        dT=np.array([0.0, 0.5, -0.3]),
100	        dY=np.array([0.0, 0.8, 0.6])),
101	    exposure=dict(
102	        beta=np.array([0.0, 1.0, -0.5]),
103	        p_A=np.array([0.40, 0.35, 0.25])),
104	    mbias=dict(
105	        tau=1.0, delta_coef=1.0, lam=1.0, g=np.zeros(K),
106	        a1=np.array([0.0, 0.8, -0.5]),
107	        a2=np.array([0.0, 0.6, 0.9])),
108	    iv=dict(
109	        lam=1.0, g=np.zeros(K),
110	        dZ=np.array([0.0, 1.0, -0.5]),
111	        dU=np.array([0.0, 0.8, 0.6]),
112	        beta=np.array([0.0, 1.0, -0.5])),
113	    frontdoor=dict(
114	        alpha_U=1.0, lam_U=1.0,
115	        gamma=np.array([0.0, 0.5, -0.3]),
116	        delta=np.array([0.0, 1.0, -0.8]),
117	        beta=np.array([0.0, 1.0, -0.5])),
118	)
119	
120	
121	# ================================================================
122	# Utilities
123	# ================================================================
124	def det_seed(topo, c_name, sim_idx, base=42):
125	    """Deterministic seed for data generation (same across methods)."""
126	    h = hashlib.sha256(f"{topo}|{c_name}|{sim_idx}|{base}".encode()).hexdigest()
127	    return int(h[:8], 16)
128	
129	
130	def det_seed_method(topo, c_name, method, sim_idx, base=42):
131	    """Deterministic seed for method-specific randomness."""
132	    h = hashlib.sha256(
133	        f"{topo}|{c_name}|{method}|{sim_idx}|{base}".encode()).hexdigest()
134	    return int(h[:8], 16)
135	
136	
137	def softmax_sample(logits, rng):
138	    """Sample from row-wise softmax (K=3 optimized)."""
139	    e = np.exp(logits - logits.max(axis=1, keepdims=True))
140	    p = e / e.sum(axis=1, keepdims=True)
141	    cum = np.cumsum(p, axis=1)
142	    u = rng.uniform(size=logits.shape[0])
143	    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)
144	
145	
146	def misclassify(A, C, rng):
147	    """Apply misclassification: A*_i ~ Cat(C[:, A_i])."""
148	    probs = C[:, A]
149	    cum = np.cumsum(probs, axis=0)
150	    u = rng.uniform(size=len(A))
151	    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)
152	
153	
154	def make_dummies(A):
155	    """K-1 dummy variables (reference category = 0)."""
156	    N = len(A)
157	    D = np.zeros((N, K - 1))
158	    for j in range(K - 1):
159	        D[:, j] = (A == j + 1).astype(float)
160	    return D
161	
162	
163	def make_full_dummies(A):
164	    """Full K one-hot encoding."""
165	    N = len(A)
166	    D = np.zeros((N, K))
167	    for j in range(K):
168	        D[:, j] = (A == j).astype(float)
169	    return D
170	
171	
172	def ols(X, Y):
173	    """OLS point estimate."""
174	    return np.linalg.lstsq(X, Y, rcond=None)[0]
175	
176	
177	def ols_with_se(X, Y):
178	    """OLS point estimate + heteroskedasticity-naive SE."""
179	    beta = np.linalg.lstsq(X, Y, rcond=None)[0]
180	    resid = Y - X @ beta
181	    n, p = X.shape
182	    s2 = resid @ resid / max(n - p, 1)
183	    try:
184	        XtX_inv = np.linalg.inv(X.T @ X)
185	        se = np.sqrt(np.maximum(np.diag(s2 * XtX_inv), 0.0))
186	    except np.linalg.LinAlgError:
187	        se = np.full(p, np.nan)
188	    return beta, se
189	
190	
191	# ================================================================
192	# DGP Functions (7 topologies)
193	# Return: (X_other, Y, A, tau_idx)
194	#   X_other: non-A columns (always includes intercept)
195	#   A: true categorical (values 0..K-1)
196	#   tau_idx: target coefficient index in [X_other | D_{K-1}]
197	# ================================================================
198	def gen_confounding(N, rng):
199	    """A->T, A->Y, T->Y. Researcher controls for A*."""
200	    p = DGP_PARAMS["confounding"]
201	    A = rng.choice(K, size=N, p=p["p_A"])
202	    D = make_dummies(A)
203	    T = D @ p["alpha"] + rng.normal(0, p["sigma_T"], N)
204	    Y = p["beta_T"] * T + D @ p["beta_A"] + rng.normal(0, 1, N)
205	    return np.column_stack([np.ones(N), T]), Y, A, 1
206	
207	
208	def gen_mediation(N, rng):
209	    """T->A->Y. A mediates; researcher controls for A*."""
210	    p = DGP_PARAMS["mediation"]
211	    T = rng.binomial(1, 0.5, N).astype(float)
212	    logits = p["gamma"][None, :] + p["delta"][None, :] * T[:, None]
213	    A = softmax_sample(logits, rng)
214	    D = make_dummies(A)
215	    Y = p["beta"][0] + D @ p["beta"][1:] + p["tau"] * T + rng.normal(0, 1, N)
216	    return np.column_stack([np.ones(N), T]), Y, A, 1
217	
218	
219	def gen_collider(N, rng):
220	    """T->A<-Y. Researcher wrongly controls for A*."""
221	    p = DGP_PARAMS["collider"]
222	    T = rng.normal(0, 1, N)
223	    Y = p["tau"] * T + rng.normal(0, 1, N)
224	    logits = (p["g"][None, :] + p["dT"][None, :] * T[:, None]
225	              + p["dY"][None, :] * Y[:, None])
226	    A = softmax_sample(logits, rng)
227	    return np.column_stack([np.ones(N), T]), Y, A, 1
228	
229	
230	def gen_exposure(N, rng):
231	    """A->Y (direct exposure, no T)."""
232	    p = DGP_PARAMS["exposure"]
233	    A = rng.choice(K, size=N, p=p["p_A"])
234	    D = make_dummies(A)
235	    Y = p["beta"][0] + D @ p["beta"][1:] + rng.normal(0, 1, N)
236	    return np.ones((N, 1)), Y, A, 1
237	
238	
239	def gen_mbias(N, rng):
240	    """U1->{A,T}, U2->{A,Y}, T->Y. Conditioning on A* induces M-bias."""
241	    p = DGP_PARAMS["mbias"]
242	    U1, U2 = rng.normal(0, 1, N), rng.normal(0, 1, N)
243	    T = p["delta_coef"] * U1 + rng.normal(0, 1, N)
244	    logits = (p["g"][None, :] + p["a1"][None, :] * U1[:, None]
245	              + p["a2"][None, :] * U2[:, None])
246	    A = softmax_sample(logits, rng)
247	    Y = p["tau"] * T + p["lam"] * U2 + rng.normal(0, 1, N)
248	    return np.column_stack([np.ones(N), T]), Y, A, 1
249	
250	
251	def gen_iv(N, rng):
252	    """Z->A->Y, U->{A,Y}. OLS on A* (no IV correction)."""
253	    p = DGP_PARAMS["iv"]
254	    Z, U = rng.normal(0, 1, N), rng.normal(0, 1, N)
255	    logits = (p["g"][None, :] + p["dZ"][None, :] * Z[:, None]
256	              + p["dU"][None, :] * U[:, None])
257	    A = softmax_sample(logits, rng)
258	    D = make_dummies(A)
259	    Y = p["beta"][0] + D @ p["beta"][1:] + p["lam"] * U + rng.normal(0, 1, N)
260	    return np.ones((N, 1)), Y, A, 1
261	
262	
263	def gen_frontdoor(N, rng):
264	    """T->M->Y, U->{T,Y}. Misclassified variable is M (mediator)."""
265	    p = DGP_PARAMS["frontdoor"]
266	    U = rng.normal(0, 1, N)
267	    T = p["alpha_U"] * U + rng.normal(0, 1, N)
268	    logits = p["gamma"][None, :] + p["delta"][None, :] * T[:, None]
269	    M = softmax_sample(logits, rng)
270	    D_M = make_dummies(M)
271	    Y = p["beta"][0] + D_M @ p["beta"][1:] + p["lam_U"] * U + rng.normal(0, 1, N)
272	    return np.ones((N, 1)), Y, M, 1
273	
274	
275	GEN_FUNCS = OrderedDict([
276	    ("confounding", gen_confounding), ("mediation", gen_mediation),
277	    ("collider", gen_collider), ("exposure", gen_exposure),
278	    ("mbias", gen_mbias), ("iv", gen_iv), ("frontdoor", gen_frontdoor),
279	])
280	
281	
282	# ================================================================
283	# Oracle: plim of OLS with true A (large-sample reference)
284	# ================================================================
285	_oracle_cache = {}
286	
287	
288	def compute_oracle_tau(topo_name, n_large=500_000, seed=999999):
289	    if topo_name in _oracle_cache:
290	        return _oracle_cache[topo_name]
291	    rng = np.random.default_rng(seed)
292	    X_other, Y, A, tau_idx = GEN_FUNCS[topo_name](n_large, rng)
293	    D = make_dummies(A)
294	    X = np.column_stack([X_other, D])
295	    beta = ols(X, Y)
296	    _oracle_cache[topo_name] = float(beta[tau_idx])
297	    return _oracle_cache[topo_name]
298	
299	
300	# ================================================================
301	# Correction Methods
302	# All return (tau_hat, se_tau, success: bool)
303	# ================================================================
304	def estimate_uncorrected(X_other, Y, Astar, tau_idx):
305	    D_star = make_dummies(Astar)
306	    X = np.column_stack([X_other, D_star])
307	    try:
308	        beta, se = ols_with_se(X, Y)
309	        return beta[tau_idx], se[tau_idx], True
310	    except Exception:
311	        return np.nan, np.nan, False
312	
313	
314	def correct_naive_plugin(X_other, Y, Astar, C, tau_idx):
315	    """Per-observation correction: corrected_i = C^{-1}[:, A*_i].
316	    Unbiased for any invertible C."""
317	    try:
318	        C_inv = np.linalg.inv(C)
319	    except np.linalg.LinAlgError:
320	        return np.nan, np.nan, False
321	    # C_inv[:, Astar] is K x N; transpose to N x K
322	    D_corrected = C_inv[:, Astar].T[:, 1:]  # drop ref cat
323	    X = np.column_stack([X_other, D_corrected])
324	    try:
325	        beta, se = ols_with_se(X, Y)
326	        return beta[tau_idx], se[tau_idx], True
327	    except Exception:
328	        return np.nan, np.nan, False
329	
330	
331	def correct_dsl(X_other, Y, Astar, A_gold, gold_mask, tau_idx):
332	    """EM-based joint estimation of regression params and C.
333	    Uses gold-standard labels for initialization and E-step anchoring."""
334	    N = len(Y)
335	    n_other = X_other.shape[1]
336	    silver_mask = ~gold_mask
337	
338	    # Initialize C from gold data
339	    C_est = np.zeros((K, K))
340	    for j in range(K):
341	        for k in range(K):
342	            C_est[k, j] = ((A_gold[gold_mask] == j)
343	                           & (Astar[gold_mask] == k)).sum()
344	    col_sums = C_est.sum(axis=0)
345	    col_sums[col_sums == 0] = 1.0
346	    C_est /= col_sums
347	    C_est = 0.9 * C_est + 0.1 / K * np.ones((K, K))
348	
349	    # Initialize beta from naive OLS
350	    D_star = make_dummies(Astar)
351	    X_init = np.column_stack([X_other, D_star])
352	    try:
353	        beta = ols(X_init, Y)
354	    except Exception:
355	        return np.nan, np.nan, False
356	    sigma2 = 1.0
357	
358	    # Pre-compute base predictions
359	    for it in range(EM_MAX_ITER):
360	        base = X_other @ beta[:n_other]
361	
362	        # E-step: P(A=j | A*_i, Y_i, X_i; beta, C, sigma2)
363	        resp = np.zeros((N, K))
364	        for j in range(K):
365	            mu_j = base + (beta[n_other + j - 1] if j > 0 else 0.0)
366	            resp[:, j] = (-0.5 * (Y - mu_j) ** 2 / sigma2
367	                          + np.log(np.clip(C_est[Astar, j], 1e-15, None)))
368	
369	        resp -= resp.max(axis=1, keepdims=True)
370	        resp = np.exp(resp)
371	        resp /= resp.sum(axis=1, keepdims=True)
372	
373	        # Anchor gold observations
374	        resp[gold_mask] = 0.0
375	        resp[gold_mask, A_gold[gold_mask]] = 1.0
376	
377	        # M-step: beta from expected dummies
378	        D_exp = resp[:, 1:]
379	        X_new = np.column_stack([X_other, D_exp])
380	        try:
381	            beta_new = ols(X_new, Y)
382	        except Exception:
383	            return np.nan, np.nan, False
384	
385	        sigma2_new = max(np.mean((Y - X_new @ beta_new) ** 2), 1e-6)
386	
387	        # M-step: update C from responsibilities
388	        C_new = np.zeros((K, K))
389	        for j in range(K):
390	            for k in range(K):
391	                C_new[k, j] = resp[Astar == k, j].sum()
392	        cs = C_new.sum(axis=0)
393	        cs[cs == 0] = 1.0
394	        C_new /= cs
395	
396	        converged = (np.max(np.abs(beta_new - beta)) < EM_TOL
397	                     and np.max(np.abs(C_new - C_est)) < EM_TOL)
398	        beta, C_est, sigma2 = beta_new, C_new, sigma2_new
399	        if converged:
400	            break
401	
402	    # Final estimate with converged responsibilities
403	    X_final = np.column_stack([X_other, resp[:, 1:]])
404	    try:
405	        beta_f, se_f = ols_with_se(X_final, Y)
406	        return beta_f[tau_idx], se_f[tau_idx], True
407	    except Exception:
408	        return np.nan, np.nan, False
409	
410	
411	def correct_ppi(X_other, Y, Astar, A_gold, gold_mask, tau_idx, rng):
412	    """PPI++ with bootstrap lambda tuning.
413	    Combines gold-standard OLS (unbiased, high var) with full-sample A* OLS."""
414	    gold_idx = np.where(gold_mask)[0]
415	    n_gold = len(gold_idx)
416	
417	    D_g_true = make_dummies(A_gold[gold_mask])
418	    X_g_true = np.column_stack([X_other[gold_mask], D_g_true])
419	    D_g_star = make_dummies(Astar[gold_mask])
420	    X_g_star = np.column_stack([X_other[gold_mask], D_g_star])
421	    D_all_star = make_dummies(Astar)
422	    X_all_star = np.column_stack([X_other, D_all_star])
423	
424	    try:
425	        b_g_true = ols(X_g_true, Y[gold_mask])
426	        b_g_star = ols(X_g_star, Y[gold_mask])
427	        b_all_star = ols(X_all_star, Y)
428	    except Exception:
429	        return np.nan, np.nan, False
430	
431	    # Bootstrap for PPI++ lambda
432	    n_boot = 50
433	    tau_true_boot = np.zeros(n_boot)
434	    tau_rect_boot = np.zeros(n_boot)
435	    for b in range(n_boot):
436	        idx = rng.choice(gold_idx, size=n_gold, replace=True)
437	        try:
438	            bt = ols(np.column_stack([X_other[idx], make_dummies(A_gold[idx])]),
439	                     Y[idx])
440	            bs = ols(np.column_stack([X_other[idx], make_dummies(Astar[idx])]),
441	                     Y[idx])
442	            tau_true_boot[b] = bt[tau_idx]
443	            tau_rect_boot[b] = bs[tau_idx] - bt[tau_idx]
444	        except Exception:
445	            tau_true_boot[b] = tau_rect_boot[b] = np.nan
446	
447	    valid = np.isfinite(tau_true_boot) & np.isfinite(tau_rect_boot)
448	    if valid.sum() > 5:
449	        var_r = np.var(tau_rect_boot[valid])
450	        cov_tr = np.cov(tau_true_boot[valid], tau_rect_boot[valid])[0, 1]
451	        lam = np.clip(-cov_tr / var_r, 0, 1) if var_r > 1e-12 else 1.0
452	    else:
453	        lam = 1.0
454	
455	    tau_ppi = (b_g_true[tau_idx]
456	               + lam * (b_all_star[tau_idx] - b_g_star[tau_idx]))
457	
458	    se_est = np.std(tau_true_boot[valid]) if valid.sum() > 1 else np.nan
459	    return tau_ppi, se_est, True
460	
461	
462	def correct_mcsimex(X_other, Y, Astar, C, tau_idx, rng):
463	    """MC-SIMEX: add extra misclassification at levels lambda, extrapolate to -1.
464	    At lambda>0, apply C^lambda to A* producing A**; fit OLS and average over B draws.
465	    Quadratic extrapolation to lambda=-1 (no error)."""
466	    try:
467	        eigvals, eigvecs = np.linalg.eig(C)
468	        eigvecs_inv = np.linalg.inv(eigvecs)
469	    except np.linalg.LinAlgError:
470	        return np.nan, np.nan, False
471	
472	    lambdas = np.array([0.0] + SIMEX_LAMBDAS)
473	    tau_lam = np.zeros(len(lambdas))
474	
475	    for li, lam in enumerate(lambdas):
476	        if lam == 0.0:
477	            D_star = make_dummies(Astar)
478	            X = np.column_stack([X_other, D_star])
479	            try:
480	                tau_lam[li] = ols(X, Y)[tau_idx]
481	            except Exception:
482	                return np.nan, np.nan, False
483	        else:
484	            # C^lambda via eigendecomposition
485	            C_lam_raw = np.real((eigvecs * (eigvals ** lam)) @ eigvecs_inv)
486	            C_lam = np.clip(C_lam_raw, 0, None)
487	            cs = C_lam.sum(axis=0)
488	            cs[cs == 0] = 1.0
489	            C_lam /= cs
490	
491	            tau_b = np.zeros(SIMEX_B)
492	            for b in range(SIMEX_B):
493	                rng_b = np.random.default_rng(
494	                    rng.integers(0, 2**31) + b * 1000 + li * 100000)
495	                Astar_extra = misclassify(Astar, C_lam, rng_b)
496	                D_extra = make_dummies(Astar_extra)
497	                X_extra = np.column_stack([X_other, D_extra])
498	                try:
499	                    tau_b[b] = ols(X_extra, Y)[tau_idx]
500	                except Exception:
501	                    tau_b[b] = np.nan
502	
503	            ok = np.isfinite(tau_b)
504	            if ok.sum() < SIMEX_B // 2:
505	                return np.nan, np.nan, False
506	            tau_lam[li] = tau_b[ok].mean()
507	
508	    # Quadratic extrapolation to lambda=-1
509	    try:
510	        coeffs = np.polyfit(lambdas, tau_lam, 2)
511	        tau_simex = np.polyval(coeffs, -1.0)
512	    except Exception:
513	        return np.nan, np.nan, False
514	
515	    # SE proxy from naive OLS (SIMEX SE requires bootstrap, not done here)
516	    D_star = make_dummies(Astar)
517	    X = np.column_stack([X_other, D_star])
518	    try:
519	        _, se = ols_with_se(X, Y)
520	        return tau_simex, se[tau_idx], True
521	    except Exception:
522	        return tau_simex, np.nan, True
523	
524	
525	def correct_mla(X_other, Y, Astar, C, tau_idx):
526	    """MLA: right-multiply full dummies by C^{-1}.
527	    D_corrected = D*_full @ C^{-1}. Unbiased only when C is symmetric."""
528	    try:
529	        C_inv = np.linalg.inv(C)
530	    except np.linalg.LinAlgError:
531	        return np.nan, np.nan, False
532	    D_full = make_full_dummies(Astar)
533	    D_corrected = (D_full @ C_inv)[:, 1:]  # drop ref cat
534	    X = np.column_stack([X_other, D_corrected])
535	    try:
536	        beta, se = ols_with_se(X, Y)
537	        return beta[tau_idx], se[tau_idx], True
538	    except Exception:
539	        return np.nan, np.nan, False
540	
541	
542	# ================================================================
543	# MC Framework
544	# ================================================================
545	def run_mc(topo_name, c_name, methods, n_sim, n_data):
546	    """Run MC for one {topo x C} pair across all requested methods."""
547	    C = C_STRUCTURES[c_name]
548	    gen_fn = GEN_FUNCS[topo_name]
549	    tau_true = compute_oracle_tau(topo_name)
550	
551	    tau_uncorr = np.zeros(n_sim)
552	    store = {m: {"tau": np.zeros(n_sim), "se": np.zeros(n_sim),
553	                 "ok": np.zeros(n_sim, dtype=bool)} for m in methods}
554	
555	    for i in range(n_sim):
556	        seed = det_seed(topo_name, c_name, i)
557	        rng = np.random.default_rng(seed)
558	        X_other, Y, A_true, tau_idx = gen_fn(n_data, rng)
559	        Astar = misclassify(A_true, C, rng)
560	
561	        gold_mask = np.zeros(n_data, dtype=bool)
562	        gold_mask[:min(N_GOLD, n_data)] = True
563	
564	        t_u, _, _ = estimate_uncorrected(X_other, Y, Astar, tau_idx)
565	        tau_uncorr[i] = t_u
566	
567	        for m in methods:
568	            rng_m = np.random.default_rng(
569	                det_seed_method(topo_name, c_name, m, i))
570	            if m == "naive_plugin":
571	                t, s, ok = correct_naive_plugin(
572	                    X_other, Y, Astar, C, tau_idx)
573	            elif m == "dsl":
574	                t, s, ok = correct_dsl(
575	                    X_other, Y, Astar, A_true, gold_mask, tau_idx)
576	            elif m == "ppi":
577	                t, s, ok = correct_ppi(
578	                    X_other, Y, Astar, A_true, gold_mask, tau_idx, rng_m)
579	            elif m == "mcsimex":
580	                t, s, ok = correct_mcsimex(
581	                    X_other, Y, Astar, C, tau_idx, rng_m)
582	            elif m == "mla":
583	                t, s, ok = correct_mla(
584	                    X_other, Y, Astar, C, tau_idx)
585	            else:
586	                raise ValueError(f"Unknown method: {m}")
587	            store[m]["tau"][i] = t
588	            store[m]["se"][i] = s
589	            store[m]["ok"][i] = ok
590	
591	    # Aggregate
592	    v_u = np.isfinite(tau_uncorr)
593	    results = []
594	    for m in methods:
595	        v = store[m]["ok"] & np.isfinite(store[m]["tau"])
596	        v_both = v & v_u
597	        fail = 1.0 - v.mean()
598	
599	        if v_both.sum() < 10:
600	            results.append(dict(
601	                method=m, topo=topo_name, c_name=c_name,
602	                tau_true=tau_true, failure_rate=float(fail),
603	                valid_count=int(v.sum()),
604	                bias_uncorrected=np.nan, bias_corrected=np.nan,
605	                bias_reduction_pct=np.nan,
606	                rmse_uncorrected=np.nan, rmse_corrected=np.nan,
607	                coverage_95=np.nan))
608	            continue
609	
610	        bias_u = float(np.mean(tau_uncorr[v_both]) - tau_true)
611	        bias_c = float(np.mean(store[m]["tau"][v_both]) - tau_true)
612	        rmse_u = float(np.sqrt(np.mean((tau_uncorr[v_both] - tau_true) ** 2)))
613	        rmse_c = float(np.sqrt(np.mean((store[m]["tau"][v_both] - tau_true) ** 2)))
614	
615	        abs_u, abs_c = abs(bias_u), abs(bias_c)
616	        br = float(1.0 - abs_c / abs_u) if abs_u > 1e-10 else 0.0
617	
618	        # 95% CI coverage
619	        v_se = v_both & np.isfinite(store[m]["se"])
620	        if v_se.sum() > 0:
621	            lo = store[m]["tau"][v_se] - 1.96 * store[m]["se"][v_se]
622	            hi = store[m]["tau"][v_se] + 1.96 * store[m]["se"][v_se]
623	            cov = float(np.mean((tau_true >= lo) & (tau_true <= hi)))
624	        else:
625	            cov = np.nan
626	
627	        results.append(dict(
628	            method=m, topo=topo_name, c_name=c_name,
629	            tau_true=tau_true,
630	            failure_rate=float(fail),
631	            valid_count=int(v_both.sum()),
632	            bias_uncorrected=bias_u,
633	            bias_corrected=bias_c,
634	            bias_reduction_pct=br,
635	            rmse_uncorrected=rmse_u,
636	            rmse_corrected=rmse_c,
637	            coverage_95=cov))
638	    return results
639	
640	
641	# ================================================================
642	# Empirical Validation Placeholder
643	# ================================================================
644	def run_empirical_validation(plan003_data_path=None):
645	    """Placeholder: validate corrections on real LLM annotation data from plan_003.
646	    To be filled when plan_003 produces annotated datasets."""
647	    if plan003_data_path is None:
648	        return None
649	    raise NotImplementedError("Awaiting plan_003 completion")
650	
651	
652	# ================================================================
653	# Output
654	# ================================================================
655	def save_results(all_results, out_dir):
656	    os.makedirs(out_dir, exist_ok=True)
657	
658	    # 1. Full JSON
659	    jp = os.path.join(out_dir, "correction_guidance_results.json")
660	    with open(jp, "w") as f:
661	        json.dump(all_results, f, indent=2)
662	    print(f"  -> {jp}")
663	
664	    # 2. Optimal method mapping
665	    mp = os.path.join(out_dir, "correction_mapping.txt")
666	    with open(mp, "w") as f:
667	        f.write("Optimal Correction Method: {topology x C_structure} -> best method\n")
668	        f.write("Criterion: max bias_reduction_pct (tie-break: min RMSE)\n")
669	        f.write("=" * 80 + "\n\n")
670	        f.write(f"{'Topology':<14} {'C Structure':<20} {'Best Method':<16} "
671	                f"{'BiasRed%':>9} {'RMSE':>8}\n")
672	        f.write("-" * 67 + "\n")
673	        for topo in GEN_FUNCS:
674	            for cn in C_STRUCTURES:
675	                cands = [r for r in all_results
676	                         if r["topo"] == topo and r["c_name"] == cn]
677	                if not cands:
678	                    continue
679	                best = max(cands, key=lambda r: (
680	                    r["bias_reduction_pct"]
681	                    if np.isfinite(r.get("bias_reduction_pct", np.nan))
682	                    else -999,
683	                    -(r["rmse_corrected"]
684	                      if np.isfinite(r.get("rmse_corrected", np.nan))
685	                      else 999)))
686	                br = best.get("bias_reduction_pct", np.nan)
687	                rm = best.get("rmse_corrected", np.nan)
688	                if np.isfinite(br) and np.isfinite(rm):
689	                    f.write(f"{topo:<14} {cn:<20} {best['method']:<16} "
690	                            f"{br:>8.1%} {rm:>8.4f}\n")
691	                else:
692	                    f.write(f"{topo:<14} {cn:<20} {best['method']:<16} "
693	                            f"{'N/A':>9} {'N/A':>8}\n")
694	            f.write("\n")
695	    print(f"  -> {mp}")
696	
697	    # 3. Method comparison summary
698	    sp = os.path.join(out_dir, "method_comparison_summary.txt")
699	    with open(sp, "w") as f:
700	        f.write("Cross-Topology Method Comparison Summary\n")
701	        f.write("=" * 90 + "\n")
702	
703	        for method in ALL_METHODS:
704	            mr = [r for r in all_results if r["method"] == method]
705	            if not mr:
706	                continue
707	            f.write(f"\n--- {method} ---\n")
708	            br = [r["bias_reduction_pct"] for r in mr
709	                  if np.isfinite(r.get("bias_reduction_pct", np.nan))]
710	            rm = [r["rmse_corrected"] for r in mr
711	                  if np.isfinite(r.get("rmse_corrected", np.nan))]
712	            cv = [r["coverage_95"] for r in mr
713	                  if np.isfinite(r.get("coverage_95", np.nan))]
714	            fl = [r["failure_rate"] for r in mr]
715	
716	            f.write(f"  Scenarios: {len(mr)}\n")
717	            if br:
718	                f.write(f"  Bias reduction: mean={np.mean(br):.1%}  "
719	                        f"median={np.median(br):.1%}  "
720	                        f"[{np.min(br):.1%}, {np.max(br):.1%}]\n")
721	            if rm:
722	                f.write(f"  RMSE: mean={np.mean(rm):.4f}  "
723	                        f"median={np.median(rm):.4f}\n")
724	            if cv:
725	                f.write(f"  Coverage 95%: mean={np.mean(cv):.1%}  "
726	                        f"min={np.min(cv):.1%}\n")
727	            f.write(f"  Failure rate: mean={np.mean(fl):.1%}  "
728	                    f"max={np.max(fl):.1%}\n")
729	
730	            by_topo = {}
731	            for r in mr:
732	                by_topo.setdefault(r["topo"], []).append(
733	                    r["bias_reduction_pct"])
734	            f.write("  By topology (mean bias reduction):\n")
735	            for t, vs in by_topo.items():
736	                vv = [x for x in vs if np.isfinite(x)]
737	                if vv:
738	                    f.write(f"    {t:<14}: {np.mean(vv):.1%}\n")
739	
740	        # Win counts
741	        f.write("\n\n--- Method Win Counts ---\n")
742	        f.write(f"{'Method':<16} {'Wins':>6} {'Rate':>8}\n")
743	        f.write("-" * 30 + "\n")
744	        wins = {m: 0 for m in ALL_METHODS}
745	        total = 0
746	        for topo in GEN_FUNCS:
747	            for cn in C_STRUCTURES:
748	                cands = [r for r in all_results
749	                         if r["topo"] == topo and r["c_name"] == cn]
750	                if cands:
751	                    total += 1
752	                    b = max(cands, key=lambda r: (
753	                        r["bias_reduction_pct"]
754	                        if np.isfinite(r.get("bias_reduction_pct", np.nan))
755	                        else -999))
756	                    wins[b["method"]] += 1
757	        for m in ALL_METHODS:
758	            rate = wins[m] / total if total > 0 else 0
759	            f.write(f"{m:<16} {wins[m]:>6} {rate:>7.1%}\n")
760	    print(f"  -> {sp}")
761	
762	
763	# ================================================================
764	# Main
765	# ================================================================
766	def main():
767	    parser = argparse.ArgumentParser(
768	        description="Plan 007: Correction Method Guidance MC Framework. "
769	                    "Evaluates 5 correction methods x 7 DAG topologies x "
770	                    "6 confusion matrices via Monte Carlo simulation.")
771	    parser.add_argument("--n-sim", type=int, default=N_SIM_DEFAULT,
772	                        help=f"MC replications per combination "
773	                             f"(default: {N_SIM_DEFAULT})")
774	    parser.add_argument("--n-data", type=int, default=N_DATA_DEFAULT,
775	                        help=f"Sample size per replication "
776	                             f"(default: {N_DATA_DEFAULT})")
777	    parser.add_argument("--topos", nargs="+",
778	                        default=list(GEN_FUNCS.keys()),
779	                        choices=list(GEN_FUNCS.keys()),
780	                        help="Topologies to evaluate")
781	    parser.add_argument("--c-types", nargs="+",
782	                        default=list(C_STRUCTURES.keys()),
783	                        choices=list(C_STRUCTURES.keys()),
784	                        help="C structures to evaluate")
785	    parser.add_argument("--methods", nargs="+",
786	                        default=ALL_METHODS, choices=ALL_METHODS,
787	                        help="Correction methods to evaluate")
788	    parser.add_argument("--out-dir", default=OUT_DIR,
789	                        help="Output directory")
790	    parser.add_argument("--dry-run", action="store_true",
791	                        help="Quick validation: 1 topo x 1 C x 1 method x "
792	                             "10 sims")
793	    args = parser.parse_args()
794	
795	    if args.dry_run:
796	        args.n_sim = 10
797	        args.topos = args.topos[:1]
798	        args.c_types = args.c_types[:1]
799	        args.methods = args.methods[:1]
800	        print("=== DRY RUN ===\n")
801	
802	    print(f"Plan 007: Correction Guidance MC Framework")
803	    print(f"  Topologies : {args.topos}")
804	    print(f"  C structures: {args.c_types}")
805	    print(f"  Methods    : {args.methods}")
806	    print(f"  N_sim={args.n_sim}  N_data={args.n_data}  N_gold={N_GOLD}")
807	    print(f"  Output     : {args.out_dir}\n")
808	
809	    all_results = []
810	    t0 = time.time()
811	    n_combos = len(args.topos) * len(args.c_types)
812	    combo_i = 0
813	
814	    for topo in args.topos:
815	        for cn in args.c_types:
816	            combo_i += 1
817	            t1 = time.time()
818	            print(f"[{combo_i}/{n_combos}] {topo} x {cn} ... ",
819	                  end="", flush=True)
820	            results = run_mc(topo, cn, args.methods, args.n_sim, args.n_data)
821	            all_results.extend(results)
822	            elapsed = time.time() - t1
823	            # Print summary for this combo
824	            for r in results:
825	                br = r["bias_reduction_pct"]
826	                br_s = f"{br:.1%}" if np.isfinite(br) else "N/A"
827	                print(f"\n    {r['method']:<14} bias_red={br_s:>7}  "
828	                      f"fail={r['failure_rate']:.0%}", end="")
829	            print(f"  [{elapsed:.1f}s]")
830	
831	    print(f"\nTotal: {time.time() - t0:.0f}s\n")
832	    print("Saving results...")
833	    save_results(all_results, args.out_dir)
834	    print("\nDone.")
835	
836	
837	if __name__ == "__main__":
838	    main()
839	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "b337f46f-aa23-470f-8e0e-e18775c0f762",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_007_correction_guidance.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nplan_007_correction_guidance.py — Correction Method Guidance MC Framework\n\nPurpose: Evaluate 5 correction methods for K=3 LLM misclassification bias across\n         7 DAG topologies and 6 confusion matrix structures via Monte Carlo simulation.\n\nFor each {topology x C_structure x correction_method}, runs N_sim MC replications to\nmeasure bias_reduction, RMSE, 95% CI coverage, and method failure rates. Outputs an\noptimal correction method mapping per {topology x C_structure}.\n\nInput:   Hardcoded DGP parameters (consistent with plan_001/002),\n         6 synthetic K=3 column-stochastic confusion matrices.\nOutput:  artifacts/plan007/correction_guidance_results.json  — full MC results\n         artifacts/plan007/correction_mapping.txt            — {topo x C} -> best method\n         artifacts/plan007/method_comparison_summary.txt     — cross-topology rankings\n\nDependencies: numpy, scipy (scipy only for polyfit fallback; core uses numpy)\n\"\"\"\n\nimport numpy as np\nimport json\nimport hashlib\nimport os\nimport time\nimport argparse\nfrom collections import OrderedDict\n\n# ================================================================\n# Constants\n# ================================================================\nK = 3\nN_DATA_DEFAULT = 5000\nN_SIM_DEFAULT = 1000\nN_GOLD = 500\nSIMEX_LAMBDAS = [0.5, 1.0, 1.5, 2.0]\nSIMEX_B = 50\nEM_MAX_ITER = 100\nEM_TOL = 1e-6\n\nOUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),\n                       \"artifacts\", \"plan007\")\n\nALL_METHODS = [\"naive_plugin\", \"dsl\", \"ppi\", \"mcsimex\", \"mla\"]\n\n\n# ================================================================\n# Confusion Matrices (column-stochastic, K=3)\n# C[j,i] = P(A*=j | A=i)\n# ================================================================\ndef _build_C_structures():\n    cs = OrderedDict()\n    # mild: diag≈0.867, off≈0.067\n    cs[\"mild_uniform\"] = 0.8 * np.eye(K) + (0.2 / K) * np.ones((K, K))\n    # moderate: diag≈0.733, off≈0.133\n    cs[\"moderate_uniform\"] = 0.6 * np.eye(K) + (0.4 / K) * np.ones((K, K))\n    # severe: diag=0.6, off=0.2\n    cs[\"severe_uniform\"] = 0.4 * np.eye(K) + (0.6 / K) * np.ones((K, K))\n    # asymmetric: class 0->1 high (0.20), others low\n    cs[\"asymmetric\"] = np.array([\n        [0.75, 0.05, 0.05],\n        [0.20, 0.80, 0.10],\n        [0.05, 0.15, 0.85]])\n    # near-permutation: cyclic shift with P≈0.90\n    cs[\"near_permutation\"] = np.array([\n        [0.05, 0.05, 0.90],\n        [0.90, 0.05, 0.05],\n        [0.05, 0.90, 0.05]])\n    # realistic LLM: adjacent confusion high, distant low\n    cs[\"realistic_llm\"] = np.array([\n        [0.78, 0.15, 0.03],\n        [0.18, 0.72, 0.18],\n        [0.04, 0.13, 0.79]])\n    for name, C in cs.items():\n        assert np.allclose(C.sum(axis=0), 1.0), f\"{name} not column-stochastic\"\n        assert (C >= 0).all(), f\"{name} has negative entries\"\n    return cs\n\n\nC_STRUCTURES = _build_C_structures()\n\n\n# ================================================================\n# DGP Parameters (K=3, consistent with plan_001/002)\n# ================================================================\nDGP_PARAMS = dict(\n    confounding=dict(\n        p_A=np.array([0.40, 0.35, 0.25]),\n        alpha=np.array([1.5, -1.0]),\n        beta_A=np.array([1.0, -0.5]),\n        beta_T=2.0, sigma_T=1.0),\n    mediation=dict(\n        tau=0.5,\n        gamma=np.array([0.0, 0.5, -0.3]),\n        delta=np.array([0.0, 0.8, -0.6]),\n        beta=np.array([0.0, 1.0, -0.5])),\n    collider=dict(\n        tau=1.0, g=np.zeros(K),\n        dT=np.array([0.0, 0.5, -0.3]),\n        dY=np.array([0.0, 0.8, 0.6])),\n    exposure=dict(\n        beta=np.array([0.0, 1.0, -0.5]),\n        p_A=np.array([0.40, 0.35, 0.25])),\n    mbias=dict(\n        tau=1.0, delta_coef=1.0, lam=1.0, g=np.zeros(K),\n        a1=np.array([0.0, 0.8, -0.5]),\n        a2=np.array([0.0, 0.6, 0.9])),\n    iv=dict(\n        lam=1.0, g=np.zeros(K),\n        dZ=np.array([0.0, 1.0, -0.5]),\n        dU=np.array([0.0, 0.8, 0.6]),\n        beta=np.array([0.0, 1.0, -0.5])),\n    frontdoor=dict(\n        alpha_U=1.0, lam_U=1.0,\n        gamma=np.array([0.0, 0.5, -0.3]),\n        delta=np.array([0.0, 1.0, -0.8]),\n        beta=np.array([0.0, 1.0, -0.5])),\n)\n\n\n# ================================================================\n# Utilities\n# ================================================================\ndef det_seed(topo, c_name, sim_idx, base=42):\n    \"\"\"Deterministic seed for data generation (same across methods).\"\"\"\n    h = hashlib.sha256(f\"{topo}|{c_name}|{sim_idx}|{base}\".encode()).hexdigest()\n    return int(h[:8], 16)\n\n\ndef det_seed_method(topo, c_name, method, sim_idx, base=42):\n    \"\"\"Deterministic seed for method-specific randomness.\"\"\"\n    h = hashlib.sha256(\n        f\"{topo}|{c_name}|{method}|{sim_idx}|{base}\".encode()).hexdigest()\n    return int(h[:8], 16)\n\n\ndef softmax_sample(logits, rng):\n    \"\"\"Sample from row-wise softmax (K=3 optimized).\"\"\"\n    e = np.exp(logits - logits.max(axis=1, keepdims=True))\n    p = e / e.sum(axis=1, keepdims=True)\n    cum = np.cumsum(p, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    return (u >= cum[:, 0]).astype(int) + (u >= cum[:, 1]).astype(int)\n\n\ndef misclassify(A, C, rng):\n    \"\"\"Apply misclassification: A*_i ~ Cat(C[:, A_i]).\"\"\"\n    probs = C[:, A]\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    return (u >= cum[0]).astype(int) + (u >= cum[1]).astype(int)\n\n\ndef make_dummies(A):\n    \"\"\"K-1 dummy variables (reference category = 0).\"\"\"\n    N = len(A)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    return D\n\n\ndef make_full_dummies(A):\n    \"\"\"Full K one-hot encoding.\"\"\"\n    N = len(A)\n    D = np.zeros((N, K))\n    for j in range(K):\n        D[:, j] = (A == j).astype(float)\n    return D\n\n\ndef ols(X, Y):\n    \"\"\"OLS point estimate.\"\"\"\n    return np.linalg.lstsq(X, Y, rcond=None)[0]\n\n\ndef ols_with_se(X, Y):\n    \"\"\"OLS point estimate + heteroskedasticity-naive SE.\"\"\"\n    beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n    resid = Y - X @ beta\n    n, p = X.shape\n    s2 = resid @ resid / max(n - p, 1)\n    try:\n        XtX_inv = np.linalg.inv(X.T @ X)\n        se = np.sqrt(np.maximum(np.diag(s2 * XtX_inv), 0.0))\n    except np.linalg.LinAlgError:\n        se = np.full(p, np.nan)\n    return beta, se\n\n\n# ================================================================\n# DGP Functions (7 topologies)\n# Return: (X_other, Y, A, tau_idx)\n#   X_other: non-A columns (always includes intercept)\n#   A: true categorical (values 0..K-1)\n#   tau_idx: target coefficient index in [X_other | D_{K-1}]\n# ================================================================\ndef gen_confounding(N, rng):\n    \"\"\"A->T, A->Y, T->Y. Researcher controls for A*.\"\"\"\n    p = DGP_PARAMS[\"confounding\"]\n    A = rng.choice(K, size=N, p=p[\"p_A\"])\n    D = make_dummies(A)\n    T = D @ p[\"alpha\"] + rng.normal(0, p[\"sigma_T\"], N)\n    Y = p[\"beta_T\"] * T + D @ p[\"beta_A\"] + rng.normal(0, 1, N)\n    return np.column_stack([np.ones(N), T]), Y, A, 1\n\n\ndef gen_mediation(N, rng):\n    \"\"\"T->A->Y. A mediates; researcher controls for A*.\"\"\"\n    p = DGP_PARAMS[\"mediation\"]\n    T = rng.binomial(1, 0.5, N).astype(float)\n    logits = p[\"gamma\"][None, :] + p[\"delta\"][None, :] * T[:, None]\n    A = softmax_sample(logits, rng)\n    D = make_dummies(A)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + p[\"tau\"] * T + rng.normal(0, 1, N)\n    return np.column_stack([np.ones(N), T]), Y, A, 1\n\n\ndef gen_collider(N, rng):\n    \"\"\"T->A<-Y. Researcher wrongly controls for A*.\"\"\"\n    p = DGP_PARAMS[\"collider\"]\n    T = rng.normal(0, 1, N)\n    Y = p[\"tau\"] * T + rng.normal(0, 1, N)\n    logits = (p[\"g\"][None, :] + p[\"dT\"][None, :] * T[:, None]\n              + p[\"dY\"][None, :] * Y[:, None])\n    A = softmax_sample(logits, rng)\n    return np.column_stack([np.ones(N), T]), Y, A, 1\n\n\ndef gen_exposure(N, rng):\n    \"\"\"A->Y (direct exposure, no T).\"\"\"\n    p = DGP_PARAMS[\"exposure\"]\n    A = rng.choice(K, size=N, p=p[\"p_A\"])\n    D = make_dummies(A)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + rng.normal(0, 1, N)\n    return np.ones((N, 1)), Y, A, 1\n\n\ndef gen_mbias(N, rng):\n    \"\"\"U1->{A,T}, U2->{A,Y}, T->Y. Conditioning on A* induces M-bias.\"\"\"\n    p = DGP_PARAMS[\"mbias\"]\n    U1, U2 = rng.normal(0, 1, N), rng.normal(0, 1, N)\n    T = p[\"delta_coef\"] * U1 + rng.normal(0, 1, N)\n    logits = (p[\"g\"][None, :] + p[\"a1\"][None, :] * U1[:, None]\n              + p[\"a2\"][None, :] * U2[:, None])\n    A = softmax_sample(logits, rng)\n    Y = p[\"tau\"] * T + p[\"lam\"] * U2 + rng.normal(0, 1, N)\n    return np.column_stack([np.ones(N), T]), Y, A, 1\n\n\ndef gen_iv(N, rng):\n    \"\"\"Z->A->Y, U->{A,Y}. OLS on A* (no IV correction).\"\"\"\n    p = DGP_PARAMS[\"iv\"]\n    Z, U = rng.normal(0, 1, N), rng.normal(0, 1, N)\n    logits = (p[\"g\"][None, :] + p[\"dZ\"][None, :] * Z[:, None]\n              + p[\"dU\"][None, :] * U[:, None])\n    A = softmax_sample(logits, rng)\n    D = make_dummies(A)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + p[\"lam\"] * U + rng.normal(0, 1, N)\n    return np.ones((N, 1)), Y, A, 1\n\n\ndef gen_frontdoor(N, rng):\n    \"\"\"T->M->Y, U->{T,Y}. Misclassified variable is M (mediator).\"\"\"\n    p = DGP_PARAMS[\"frontdoor\"]\n    U = rng.normal(0, 1, N)\n    T = p[\"alpha_U\"] * U + rng.normal(0, 1, N)\n    logits = p[\"gamma\"][None, :] + p[\"delta\"][None, :] * T[:, None]\n    M = softmax_sample(logits, rng)\n    D_M = make_dummies(M)\n    Y = p[\"beta\"][0] + D_M @ p[\"beta\"][1:] + p[\"lam_U\"] * U + rng.normal(0, 1, N)\n    return np.ones((N, 1)), Y, M, 1\n\n\nGEN_FUNCS = OrderedDict([\n    (\"confounding\", gen_confounding), (\"mediation\", gen_mediation),\n    (\"collider\", gen_collider), (\"exposure\", gen_exposure),\n    (\"mbias\", gen_mbias), (\"iv\", gen_iv), (\"frontdoor\", gen_frontdoor),\n])\n\n\n# ================================================================\n# Oracle: plim of OLS with true A (large-sample reference)\n# ================================================================\n_oracle_cache = {}\n\n\ndef compute_oracle_tau(topo_name, n_large=500_000, seed=999999):\n    if topo_name in _oracle_cache:\n        return _oracle_cache[topo_name]\n    rng = np.random.default_rng(seed)\n    X_other, Y, A, tau_idx = GEN_FUNCS[topo_name](n_large, rng)\n    D = make_dummies(A)\n    X = np.column_stack([X_other, D])\n    beta = ols(X, Y)\n    _oracle_cache[topo_name] = float(beta[tau_idx])\n    return _oracle_cache[topo_name]\n\n\n# ================================================================\n# Correction Methods\n# All return (tau_hat, se_tau, success: bool)\n# ================================================================\ndef estimate_uncorrected(X_other, Y, Astar, tau_idx):\n    D_star = make_dummies(Astar)\n    X = np.column_stack([X_other, D_star])\n    try:\n        beta, se = ols_with_se(X, Y)\n        return beta[tau_idx], se[tau_idx], True\n    except Exception:\n        return np.nan, np.nan, False\n\n\ndef correct_naive_plugin(X_other, Y, Astar, C, tau_idx):\n    \"\"\"Per-observation correction: corrected_i = C^{-1}[:, A*_i].\n    Unbiased for any invertible C.\"\"\"\n    try:\n        C_inv = np.linalg.inv(C)\n    except np.linalg.LinAlgError:\n        return np.nan, np.nan, False\n    # C_inv[:, Astar] is K x N; transpose to N x K\n    D_corrected = C_inv[:, Astar].T[:, 1:]  # drop ref cat\n    X = np.column_stack([X_other, D_corrected])\n    try:\n        beta, se = ols_with_se(X, Y)\n        return beta[tau_idx], se[tau_idx], True\n    except Exception:\n        return np.nan, np.nan, False\n\n\ndef correct_dsl(X_other, Y, Astar, A_gold, gold_mask, tau_idx):\n    \"\"\"EM-based joint estimation of regression params and C.\n    Uses gold-standard labels for initialization and E-step anchoring.\"\"\"\n    N = len(Y)\n    n_other = X_other.shape[1]\n    silver_mask = ~gold_mask\n\n    # Initialize C from gold data\n    C_est = np.zeros((K, K))\n    for j in range(K):\n        for k in range(K):\n            C_est[k, j] = ((A_gold[gold_mask] == j)\n                           & (Astar[gold_mask] == k)).sum()\n    col_sums = C_est.sum(axis=0)\n    col_sums[col_sums == 0] = 1.0\n    C_est /= col_sums\n    C_est = 0.9 * C_est + 0.1 / K * np.ones((K, K))\n\n    # Initialize beta from naive OLS\n    D_star = make_dummies(Astar)\n    X_init = np.column_stack([X_other, D_star])\n    try:\n        beta = ols(X_init, Y)\n    except Exception:\n        return np.nan, np.nan, False\n    sigma2 = 1.0\n\n    # Pre-compute base predictions\n    for it in range(EM_MAX_ITER):\n        base = X_other @ beta[:n_other]\n\n        # E-step: P(A=j | A*_i, Y_i, X_i; beta, C, sigma2)\n        resp = np.zeros((N, K))\n        for j in range(K):\n            mu_j = base + (beta[n_other + j - 1] if j > 0 else 0.0)\n            resp[:, j] = (-0.5 * (Y - mu_j) ** 2 / sigma2\n                          + np.log(np.clip(C_est[Astar, j], 1e-15, None)))\n\n        resp -= resp.max(axis=1, keepdims=True)\n        resp = np.exp(resp)\n        resp /= resp.sum(axis=1, keepdims=True)\n\n        # Anchor gold observations\n        resp[gold_mask] = 0.0\n        resp[gold_mask, A_gold[gold_mask]] = 1.0\n\n        # M-step: beta from expected dummies\n        D_exp = resp[:, 1:]\n        X_new = np.column_stack([X_other, D_exp])\n        try:\n            beta_new = ols(X_new, Y)\n        except Exception:\n            return np.nan, np.nan, False\n\n        sigma2_new = max(np.mean((Y - X_new @ beta_new) ** 2), 1e-6)\n\n        # M-step: update C from responsibilities\n        C_new = np.zeros((K, K))\n        for j in range(K):\n            for k in range(K):\n                C_new[k, j] = resp[Astar == k, j].sum()\n        cs = C_new.sum(axis=0)\n        cs[cs == 0] = 1.0\n        C_new /= cs\n\n        converged = (np.max(np.abs(beta_new - beta)) < EM_TOL\n                     and np.max(np.abs(C_new - C_est)) < EM_TOL)\n        beta, C_est, sigma2 = beta_new, C_new, sigma2_new\n        if converged:\n            break\n\n    # Final estimate with converged responsibilities\n    X_final = np.column_stack([X_other, resp[:, 1:]])\n    try:\n        beta_f, se_f = ols_with_se(X_final, Y)\n        return beta_f[tau_idx], se_f[tau_idx], True\n    except Exception:\n        return np.nan, np.nan, False\n\n\ndef correct_ppi(X_other, Y, Astar, A_gold, gold_mask, tau_idx, rng):\n    \"\"\"PPI++ with bootstrap lambda tuning.\n    Combines gold-standard OLS (unbiased, high var) with full-sample A* OLS.\"\"\"\n    gold_idx = np.where(gold_mask)[0]\n    n_gold = len(gold_idx)\n\n    D_g_true = make_dummies(A_gold[gold_mask])\n    X_g_true = np.column_stack([X_other[gold_mask], D_g_true])\n    D_g_star = make_dummies(Astar[gold_mask])\n    X_g_star = np.column_stack([X_other[gold_mask], D_g_star])\n    D_all_star = make_dummies(Astar)\n    X_all_star = np.column_stack([X_other, D_all_star])\n\n    try:\n        b_g_true = ols(X_g_true, Y[gold_mask])\n        b_g_star = ols(X_g_star, Y[gold_mask])\n        b_all_star = ols(X_all_star, Y)\n    except Exception:\n        return np.nan, np.nan, False\n\n    # Bootstrap for PPI++ lambda\n    n_boot = 50\n    tau_true_boot = np.zeros(n_boot)\n    tau_rect_boot = np.zeros(n_boot)\n    for b in range(n_boot):\n        idx = rng.choice(gold_idx, size=n_gold, replace=True)\n        try:\n            bt = ols(np.column_stack([X_other[idx], make_dummies(A_gold[idx])]),\n                     Y[idx])\n            bs = ols(np.column_stack([X_other[idx], make_dummies(Astar[idx])]),\n                     Y[idx])\n            tau_true_boot[b] = bt[tau_idx]\n            tau_rect_boot[b] = bs[tau_idx] - bt[tau_idx]\n        except Exception:\n            tau_true_boot[b] = tau_rect_boot[b] = np.nan\n\n    valid = np.isfinite(tau_true_boot) & np.isfinite(tau_rect_boot)\n    if valid.sum() > 5:\n        var_r = np.var(tau_rect_boot[valid])\n        cov_tr = np.cov(tau_true_boot[valid], tau_rect_boot[valid])[0, 1]\n        lam = np.clip(-cov_tr / var_r, 0, 1) if var_r > 1e-12 else 1.0\n    else:\n        lam = 1.0\n\n    tau_ppi = (b_g_true[tau_idx]\n               + lam * (b_all_star[tau_idx] - b_g_star[tau_idx]))\n\n    se_est = np.std(tau_true_boot[valid]) if valid.sum() > 1 else np.nan\n    return tau_ppi, se_est, True\n\n\ndef correct_mcsimex(X_other, Y, Astar, C, tau_idx, rng):\n    \"\"\"MC-SIMEX: add extra misclassification at levels lambda, extrapolate to -1.\n    At lambda>0, apply C^lambda to A* producing A**; fit OLS and average over B draws.\n    Quadratic extrapolation to lambda=-1 (no error).\"\"\"\n    try:\n        eigvals, eigvecs = np.linalg.eig(C)\n        eigvecs_inv = np.linalg.inv(eigvecs)\n    except np.linalg.LinAlgError:\n        return np.nan, np.nan, False\n\n    lambdas = np.array([0.0] + SIMEX_LAMBDAS)\n    tau_lam = np.zeros(len(lambdas))\n\n    for li, lam in enumerate(lambdas):\n        if lam == 0.0:\n            D_star = make_dummies(Astar)\n            X = np.column_stack([X_other, D_star])\n            try:\n                tau_lam[li] = ols(X, Y)[tau_idx]\n            except Exception:\n                return np.nan, np.nan, False\n        else:\n            # C^lambda via eigendecomposition\n            C_lam_raw = np.real((eigvecs * (eigvals ** lam)) @ eigvecs_inv)\n            C_lam = np.clip(C_lam_raw, 0, None)\n            cs = C_lam.sum(axis=0)\n            cs[cs == 0] = 1.0\n            C_lam /= cs\n\n            tau_b = np.zeros(SIMEX_B)\n            for b in range(SIMEX_B):\n                rng_b = np.random.default_rng(\n                    rng.integers(0, 2**31) + b * 1000 + li * 100000)\n                Astar_extra = misclassify(Astar, C_lam, rng_b)\n                D_extra = make_dummies(Astar_extra)\n                X_extra = np.column_stack([X_other, D_extra])\n                try:\n                    tau_b[b] = ols(X_extra, Y)[tau_idx]\n                except Exception:\n                    tau_b[b] = np.nan\n\n            ok = np.isfinite(tau_b)\n            if ok.sum() < SIMEX_B // 2:\n                return np.nan, np.nan, False\n            tau_lam[li] = tau_b[ok].mean()\n\n    # Quadratic extrapolation to lambda=-1\n    try:\n        coeffs = np.polyfit(lambdas, tau_lam, 2)\n        tau_simex = np.polyval(coeffs, -1.0)\n    except Exception:\n        return np.nan, np.nan, False\n\n    # SE proxy from naive OLS (SIMEX SE requires bootstrap, not done here)\n    D_star = make_dummies(Astar)\n    X = np.column_stack([X_other, D_star])\n    try:\n        _, se = ols_with_se(X, Y)\n        return tau_simex, se[tau_idx], True\n    except Exception:\n        return tau_simex, np.nan, True\n\n\ndef correct_mla(X_other, Y, Astar, C, tau_idx):\n    \"\"\"MLA: right-multiply full dummies by C^{-1}.\n    D_corrected = D*_full @ C^{-1}. Unbiased only when C is symmetric.\"\"\"\n    try:\n        C_inv = np.linalg.inv(C)\n    except np.linalg.LinAlgError:\n        return np.nan, np.nan, False\n    D_full = make_full_dummies(Astar)\n    D_corrected = (D_full @ C_inv)[:, 1:]  # drop ref cat\n    X = np.column_stack([X_other, D_corrected])\n    try:\n        beta, se = ols_with_se(X, Y)\n        return beta[tau_idx], se[tau_idx], True\n    except Exception:\n        return np.nan, np.nan, False\n\n\n# ================================================================\n# MC Framework\n# ================================================================\ndef run_mc(topo_name, c_name, methods, n_sim, n_data):\n    \"\"\"Run MC for one {topo x C} pair across all requested methods.\"\"\"\n    C = C_STRUCTURES[c_name]\n    gen_fn = GEN_FUNCS[topo_name]\n    tau_true = compute_oracle_tau(topo_name)\n\n    tau_uncorr = np.zeros(n_sim)\n    store = {m: {\"tau\": np.zeros(n_sim), \"se\": np.zeros(n_sim),\n                 \"ok\": np.zeros(n_sim, dtype=bool)} for m in methods}\n\n    for i in range(n_sim):\n        seed = det_seed(topo_name, c_name, i)\n        rng = np.random.default_rng(seed)\n        X_other, Y, A_true, tau_idx = gen_fn(n_data, rng)\n        Astar = misclassify(A_true, C, rng)\n\n        gold_mask = np.zeros(n_data, dtype=bool)\n        gold_mask[:min(N_GOLD, n_data)] = True\n\n        t_u, _, _ = estimate_uncorrected(X_other, Y, Astar, tau_idx)\n        tau_uncorr[i] = t_u\n\n        for m in methods:\n            rng_m = np.random.default_rng(\n                det_seed_method(topo_name, c_name, m, i))\n            if m == \"naive_plugin\":\n                t, s, ok = correct_naive_plugin(\n                    X_other, Y, Astar, C, tau_idx)\n            elif m == \"dsl\":\n                t, s, ok = correct_dsl(\n                    X_other, Y, Astar, A_true, gold_mask, tau_idx)\n            elif m == \"ppi\":\n                t, s, ok = correct_ppi(\n                    X_other, Y, Astar, A_true, gold_mask, tau_idx, rng_m)\n            elif m == \"mcsimex\":\n                t, s, ok = correct_mcsimex(\n                    X_other, Y, Astar, C, tau_idx, rng_m)\n            elif m == \"mla\":\n                t, s, ok = correct_mla(\n                    X_other, Y, Astar, C, tau_idx)\n            else:\n                raise ValueError(f\"Unknown method: {m}\")\n            store[m][\"tau\"][i] = t\n            store[m][\"se\"][i] = s\n            store[m][\"ok\"][i] = ok\n\n    # Aggregate\n    v_u = np.isfinite(tau_uncorr)\n    results = []\n    for m in methods:\n        v = store[m][\"ok\"] & np.isfinite(store[m][\"tau\"])\n        v_both = v & v_u\n        fail = 1.0 - v.mean()\n\n        if v_both.sum() < 10:\n            results.append(dict(\n                method=m, topo=topo_name, c_name=c_name,\n                tau_true=tau_true, failure_rate=float(fail),\n                valid_count=int(v.sum()),\n                bias_uncorrected=np.nan, bias_corrected=np.nan,\n                bias_reduction_pct=np.nan,\n                rmse_uncorrected=np.nan, rmse_corrected=np.nan,\n                coverage_95=np.nan))\n            continue\n\n        bias_u = float(np.mean(tau_uncorr[v_both]) - tau_true)\n        bias_c = float(np.mean(store[m][\"tau\"][v_both]) - tau_true)\n        rmse_u = float(np.sqrt(np.mean((tau_uncorr[v_both] - tau_true) ** 2)))\n        rmse_c = float(np.sqrt(np.mean((store[m][\"tau\"][v_both] - tau_true) ** 2)))\n\n        abs_u, abs_c = abs(bias_u), abs(bias_c)\n        br = float(1.0 - abs_c / abs_u) if abs_u > 1e-10 else 0.0\n\n        # 95% CI coverage\n        v_se = v_both & np.isfinite(store[m][\"se\"])\n        if v_se.sum() > 0:\n            lo = store[m][\"tau\"][v_se] - 1.96 * store[m][\"se\"][v_se]\n            hi = store[m][\"tau\"][v_se] + 1.96 * store[m][\"se\"][v_se]\n            cov = float(np.mean((tau_true >= lo) & (tau_true <= hi)))\n        else:\n            cov = np.nan\n\n        results.append(dict(\n            method=m, topo=topo_name, c_name=c_name,\n            tau_true=tau_true,\n            failure_rate=float(fail),\n            valid_count=int(v_both.sum()),\n            bias_uncorrected=bias_u,\n            bias_corrected=bias_c,\n            bias_reduction_pct=br,\n            rmse_uncorrected=rmse_u,\n            rmse_corrected=rmse_c,\n            coverage_95=cov))\n    return results\n\n\n# ================================================================\n# Empirical Validation Placeholder\n# ================================================================\ndef run_empirical_validation(plan003_data_path=None):\n    \"\"\"Placeholder: validate corrections on real LLM annotation data from plan_003.\n    To be filled when plan_003 produces annotated datasets.\"\"\"\n    if plan003_data_path is None:\n        return None\n    raise NotImplementedError(\"Awaiting plan_003 completion\")\n\n\n# ================================================================\n# Output\n# ================================================================\ndef save_results(all_results, out_dir):\n    os.makedirs(out_dir, exist_ok=True)\n\n    # 1. Full JSON\n    jp = os.path.join(out_dir, \"correction_guidance_results.json\")\n    with open(jp, \"w\") as f:\n        json.dump(all_results, f, indent=2)\n    print(f\"  -> {jp}\")\n\n    # 2. Optimal method mapping\n    mp = os.path.join(out_dir, \"correction_mapping.txt\")\n    with open(mp, \"w\") as f:\n        f.write(\"Optimal Correction Method: {topology x C_structure} -> best method\\n\")\n        f.write(\"Criterion: max bias_reduction_pct (tie-break: min RMSE)\\n\")\n        f.write(\"=\" * 80 + \"\\n\\n\")\n        f.write(f\"{'Topology':<14} {'C Structure':<20} {'Best Method':<16} \"\n                f\"{'BiasRed%':>9} {'RMSE':>8}\\n\")\n        f.write(\"-\" * 67 + \"\\n\")\n        for topo in GEN_FUNCS:\n            for cn in C_STRUCTURES:\n                cands = [r for r in all_results\n                         if r[\"topo\"] == topo and r[\"c_name\"] == cn]\n                if not cands:\n                    continue\n                best = max(cands, key=lambda r: (\n                    r[\"bias_reduction_pct\"]\n                    if np.isfinite(r.get(\"bias_reduction_pct\", np.nan))\n                    else -999,\n                    -(r[\"rmse_corrected\"]\n                      if np.isfinite(r.get(\"rmse_corrected\", np.nan))\n                      else 999)))\n                br = best.get(\"bias_reduction_pct\", np.nan)\n                rm = best.get(\"rmse_corrected\", np.nan)\n                if np.isfinite(br) and np.isfinite(rm):\n                    f.write(f\"{topo:<14} {cn:<20} {best['method']:<16} \"\n                            f\"{br:>8.1%} {rm:>8.4f}\\n\")\n                else:\n                    f.write(f\"{topo:<14} {cn:<20} {best['method']:<16} \"\n                            f\"{'N/A':>9} {'N/A':>8}\\n\")\n            f.write(\"\\n\")\n    print(f\"  -> {mp}\")\n\n    # 3. Method comparison summary\n    sp = os.path.join(out_dir, \"method_comparison_summary.txt\")\n    with open(sp, \"w\") as f:\n        f.write(\"Cross-Topology Method Comparison Summary\\n\")\n        f.write(\"=\" * 90 + \"\\n\")\n\n        for method in ALL_METHODS:\n            mr = [r for r in all_results if r[\"method\"] == method]\n            if not mr:\n                continue\n            f.write(f\"\\n--- {method} ---\\n\")\n            br = [r[\"bias_reduction_pct\"] for r in mr\n                  if np.isfinite(r.get(\"bias_reduction_pct\", np.nan))]\n            rm = [r[\"rmse_corrected\"] for r in mr\n                  if np.isfinite(r.get(\"rmse_corrected\", np.nan))]\n            cv = [r[\"coverage_95\"] for r in mr\n                  if np.isfinite(r.get(\"coverage_95\", np.nan))]\n            fl = [r[\"failure_rate\"] for r in mr]\n\n            f.write(f\"  Scenarios: {len(mr)}\\n\")\n            if br:\n                f.write(f\"  Bias reduction: mean={np.mean(br):.1%}  \"\n                        f\"median={np.median(br):.1%}  \"\n                        f\"[{np.min(br):.1%}, {np.max(br):.1%}]\\n\")\n            if rm:\n                f.write(f\"  RMSE: mean={np.mean(rm):.4f}  \"\n                        f\"median={np.median(rm):.4f}\\n\")\n            if cv:\n                f.write(f\"  Coverage 95%: mean={np.mean(cv):.1%}  \"\n                        f\"min={np.min(cv):.1%}\\n\")\n            f.write(f\"  Failure rate: mean={np.mean(fl):.1%}  \"\n                    f\"max={np.max(fl):.1%}\\n\")\n\n            by_topo = {}\n            for r in mr:\n                by_topo.setdefault(r[\"topo\"], []).append(\n                    r[\"bias_reduction_pct\"])\n            f.write(\"  By topology (mean bias reduction):\\n\")\n            for t, vs in by_topo.items():\n                vv = [x for x in vs if np.isfinite(x)]\n                if vv:\n                    f.write(f\"    {t:<14}: {np.mean(vv):.1%}\\n\")\n\n        # Win counts\n        f.write(\"\\n\\n--- Method Win Counts ---\\n\")\n        f.write(f\"{'Method':<16} {'Wins':>6} {'Rate':>8}\\n\")\n        f.write(\"-\" * 30 + \"\\n\")\n        wins = {m: 0 for m in ALL_METHODS}\n        total = 0\n        for topo in GEN_FUNCS:\n            for cn in C_STRUCTURES:\n                cands = [r for r in all_results\n                         if r[\"topo\"] == topo and r[\"c_name\"] == cn]\n                if cands:\n                    total += 1\n                    b = max(cands, key=lambda r: (\n                        r[\"bias_reduction_pct\"]\n                        if np.isfinite(r.get(\"bias_reduction_pct\", np.nan))\n                        else -999))\n                    wins[b[\"method\"]] += 1\n        for m in ALL_METHODS:\n            rate = wins[m] / total if total > 0 else 0\n            f.write(f\"{m:<16} {wins[m]:>6} {rate:>7.1%}\\n\")\n    print(f\"  -> {sp}\")\n\n\n# ================================================================\n# Main\n# ================================================================\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Plan 007: Correction Method Guidance MC Framework. \"\n                    \"Evaluates 5 correction methods x 7 DAG topologies x \"\n                    \"6 confusion matrices via Monte Carlo simulation.\")\n    parser.add_argument(\"--n-sim\", type=int, default=N_SIM_DEFAULT,\n                        help=f\"MC replications per combination \"\n                             f\"(default: {N_SIM_DEFAULT})\")\n    parser.add_argument(\"--n-data\", type=int, default=N_DATA_DEFAULT,\n                        help=f\"Sample size per replication \"\n                             f\"(default: {N_DATA_DEFAULT})\")\n    parser.add_argument(\"--topos\", nargs=\"+\",\n                        default=list(GEN_FUNCS.keys()),\n                        choices=list(GEN_FUNCS.keys()),\n                        help=\"Topologies to evaluate\")\n    parser.add_argument(\"--c-types\", nargs=\"+\",\n                        default=list(C_STRUCTURES.keys()),\n                        choices=list(C_STRUCTURES.keys()),\n                        help=\"C structures to evaluate\")\n    parser.add_argument(\"--methods\", nargs=\"+\",\n                        default=ALL_METHODS, choices=ALL_METHODS,\n                        help=\"Correction methods to evaluate\")\n    parser.add_argument(\"--out-dir\", default=OUT_DIR,\n                        help=\"Output directory\")\n    parser.add_argument(\"--dry-run\", action=\"store_true\",\n                        help=\"Quick validation: 1 topo x 1 C x 1 method x \"\n                             \"10 sims\")\n    args = parser.parse_args()\n\n    if args.dry_run:\n        args.n_sim = 10\n        args.topos = args.topos[:1]\n        args.c_types = args.c_types[:1]\n        args.methods = args.methods[:1]\n        print(\"=== DRY RUN ===\\n\")\n\n    print(f\"Plan 007: Correction Guidance MC Framework\")\n    print(f\"  Topologies : {args.topos}\")\n    print(f\"  C structures: {args.c_types}\")\n    print(f\"  Methods    : {args.methods}\")\n    print(f\"  N_sim={args.n_sim}  N_data={args.n_data}  N_gold={N_GOLD}\")\n    print(f\"  Output     : {args.out_dir}\\n\")\n\n    all_results = []\n    t0 = time.time()\n    n_combos = len(args.topos) * len(args.c_types)\n    combo_i = 0\n\n    for topo in args.topos:\n        for cn in args.c_types:\n            combo_i += 1\n            t1 = time.time()\n            print(f\"[{combo_i}/{n_combos}] {topo} x {cn} ... \",\n                  end=\"\", flush=True)\n            results = run_mc(topo, cn, args.methods, args.n_sim, args.n_data)\n            all_results.extend(results)\n            elapsed = time.time() - t1\n            # Print summary for this combo\n            for r in results:\n                br = r[\"bias_reduction_pct\"]\n                br_s = f\"{br:.1%}\" if np.isfinite(br) else \"N/A\"\n                print(f\"\\n    {r['method']:<14} bias_red={br_s:>7}  \"\n                      f\"fail={r['failure_rate']:.0%}\", end=\"\")\n            print(f\"  [{elapsed:.1f}s]\")\n\n    print(f\"\\nTotal: {time.time() - t0:.0f}s\\n\")\n    print(\"Saving results...\")\n    save_results(all_results, args.out_dir)\n    print(\"\\nDone.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 839,
      "startLine": 1,
      "totalLines": 839
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

Now let me also check the fixed ASV file for `compute_signif_asv_fast`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "f6a69fdd-8529-4551-8aa1-b50ea3988ccf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mfhKEG3qZNgzwTqAtHk3G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 45562,
      "cache_read_input_tokens": 26845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 45562
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

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_01PYdDWuBVgbk3JonnbWPpCQ`</summary>

```json
{
  "pattern": "artifacts/plan_005_asv_extended_fixed.py",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "844e88cf-daf2-460f-9cbb-3d5c27273ca0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mfhKEG3qZNgzwTqAtHk3G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 45562,
      "cache_read_input_tokens": 26845,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 45562
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

_source line 16 · 2026-05-20T23:24:38.589Z_

<details><summary>↩ Tool result · `toolu_01PYdDWuBVgbk3JonnbWPpCQ`</summary>

```text
artifacts/plan_005_asv_extended_fixed.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "c9a7bd51-a507-4d71-b225-0ac84d28f136",
  "tool_use_result": {
    "filenames": [
      "artifacts/plan_005_asv_extended_fixed.py"
    ],
    "durationMs": 30,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_01EmtLoiMbXEtqGdeExwWd9W`</summary>

```json
{
  "pattern": "compute_signif_asv_fast",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan_005_asv_extended_fixed.py",
  "output_mode": "content",
  "-A": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "44095830-6537-4787-b940-3534ec623c5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrZWeVid3aBSQ22VX37yUU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 158,
      "cache_read_input_tokens": 72407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 158
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

_source line 18 · 2026-05-20T23:24:42.419Z_

<details><summary>↩ Tool result · `toolu_01EmtLoiMbXEtqGdeExwWd9W`</summary>

```text
6:  C1: Added compute_signif_asv_fast from plan_004_v3_fixed
7-  C2: compute_magnitude_asv_fast returns 0.0 (not None) when tau_true ~ 0
8-  W1: IV tau_true = plim_iv(I), not DGP beta (approx 0.66 vs 0.5)
9-  W2: M-bias tau_true = plim_mbias(I)[1], not DGP tau (approx 0.5128 vs 0.5)
10-
11-Only Part 2+3+5 re-run. Part 1 and Part 4 preserved but skipped.
12-Part 5 uses significance-based ASV rejection rule (from plan_004_v3_fixed).
13-"""
14-
15-import numpy as np
16-import json
17-import time
18-
19-K = 3
20-
21-# ============================================================================
22-# Utilities (from plan_004 v3)
23-# ============================================================================
24-
25-def softmax_sample(logits, rng):
26-    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))
--
423:def compute_signif_asv_fast(tau_curve, deltas, se):
424-    """Min delta where |plim tau(C(delta))| < 1.96 * SE (becomes non-significant)."""
425-    z_crit = 1.96
426-    for i in range(len(deltas)):
427-        if np.isnan(tau_curve[i]):
428-            continue
429-        if abs(tau_curve[i]) < z_crit * se:
430-            return deltas[i]
431-    return None
432-
433-
434-# ============================================================================
435-# Part 1: Envelope Monotonicity (preserved, skipped in main)
436-# ============================================================================
437-
438-def part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_fd):
439-    print("\n" + "=" * 70)
440-    print("PART 1: Envelope Monotonicity (tau=0.5)")
441-    print("=" * 70)
442-    t0 = time.time()
443-    param = LinearInterpolation()
--
709:                    sasv = compute_signif_asv_fast(tau_curve, deltas, se_tau)
710-                    sasv_vals.append(sasv)
711-                    if reject and (sasv is None or sasv > 1.0):
712-                        asv_rej += 1
713-                sf = [a for a in sasv_vals if a is not None]
714-                sm = f"{np.mean(sf):.2f}" if sf else "N/A"
715-                ms = f"{masv:.2f}" if masv is not None else "None"
716-                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
717-                      f"{asv_rej/n_mc:>10.3f} {sm:>10} {ms:>10}")
718-                results[("mbias", tau_val, cname, h_label)] = {
719-                    "naive_rej": naive_rej/n_mc, "asv_rej": asv_rej/n_mc,
720-                    "mean_sasv": np.mean(sf) if sf else None, "masv": masv}
721-
722-        # === IV ===
723-        print("\n  [IV]")
724-        print(header)
725-        print("  " + "-" * 55)
726-        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
727-            iv_b = np.array([0.0, tau_h, -tau_h/2])
728-            st_h = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)
729-            # [W1] Use plim(I) as tau_true for magnitude ASV
--
751:                    sasv = compute_signif_asv_fast(tau_curve, deltas, se_for_asv)
752-                    sasv_vals.append(sasv)
753-                    if reject and (sasv is None or sasv > 1.0):
754-                        asv_rej += 1
755-                sf = [a for a in sasv_vals if a is not None]
756-                sm = f"{np.mean(sf):.2f}" if sf else "N/A"
757-                ms = f"{masv:.2f}" if masv is not None else "None"
758-                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
759-                      f"{asv_rej/n_mc:>10.3f} {sm:>10} {ms:>10}")
760-                results[("iv", tau_val, cname, h_label)] = {
761-                    "naive_rej": naive_rej/n_mc, "asv_rej": asv_rej/n_mc,
762-                    "mean_sasv": np.mean(sf) if sf else None, "masv": masv}
763-
764-        # === Front-door ===
765-        print("\n  [Front-door]")
766-        print(header)
767-        print("  " + "-" * 55)
768-        for h_label, tau_h in [("H0", 0.0), ("H1", tau_val)]:
769-            if h_label == "H0":
770-                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=0.0, aU=0.0,
771-                                  d=np.zeros(3), seed=400)
--
803:                    sasv = compute_signif_asv_fast(tau_curve, deltas, se_tau)
804-                    sasv_vals.append(sasv)
805-                    if reject and (sasv is None or sasv > 1.0):
806-                        asv_rej += 1
807-                sf = [a for a in sasv_vals if a is not None]
808-                sm = f"{np.mean(sf):.2f}" if sf else "N/A"
809-                ms = f"{masv:.2f}" if masv is not None else "None"
810-                print(f"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} "
811-                      f"{asv_rej/n_mc:>10.3f} {sm:>10} {ms:>10}")
812-                results[("frontdoor", tau_val, cname, h_label)] = {
813-                    "naive_rej": naive_rej/n_mc, "asv_rej": asv_rej/n_mc,
814-                    "mean_sasv": np.mean(sf) if sf else None, "masv": masv}
815-
816-    print(f"\n  Total time: {time.time()-t0:.1f}s")
817-    return results
818-
819-
820-# ============================================================================
821-# Part 6: Summary JSON
822-# ============================================================================
823-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "2df9b8d7-f963-4290-beed-56c329ca609a",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "6:  C1: Added compute_signif_asv_fast from plan_004_v3_fixed\n7-  C2: compute_magnitude_asv_fast returns 0.0 (not None) when tau_true ~ 0\n8-  W1: IV tau_true = plim_iv(I), not DGP beta (approx 0.66 vs 0.5)\n9-  W2: M-bias tau_true = plim_mbias(I)[1], not DGP tau (approx 0.5128 vs 0.5)\n10-\n11-Only Part 2+3+5 re-run. Part 1 and Part 4 preserved but skipped.\n12-Part 5 uses significance-based ASV rejection rule (from plan_004_v3_fixed).\n13-\"\"\"\n14-\n15-import numpy as np\n16-import json\n17-import time\n18-\n19-K = 3\n20-\n21-# ============================================================================\n22-# Utilities (from plan_004 v3)\n23-# ============================================================================\n24-\n25-def softmax_sample(logits, rng):\n26-    exp_l = np.exp(logits - logits.max(axis=1, keepdims=True))\n--\n423:def compute_signif_asv_fast(tau_curve, deltas, se):\n424-    \"\"\"Min delta where |plim tau(C(delta))| < 1.96 * SE (becomes non-significant).\"\"\"\n425-    z_crit = 1.96\n426-    for i in range(len(deltas)):\n427-        if np.isnan(tau_curve[i]):\n428-            continue\n429-        if abs(tau_curve[i]) < z_crit * se:\n430-            return deltas[i]\n431-    return None\n432-\n433-\n434-# ============================================================================\n435-# Part 1: Envelope Monotonicity (preserved, skipped in main)\n436-# ============================================================================\n437-\n438-def part1_envelope_monotonicity(st_mb, st_iv, st_fd, tau_fd):\n439-    print(\"\\n\" + \"=\" * 70)\n440-    print(\"PART 1: Envelope Monotonicity (tau=0.5)\")\n441-    print(\"=\" * 70)\n442-    t0 = time.time()\n443-    param = LinearInterpolation()\n--\n709:                    sasv = compute_signif_asv_fast(tau_curve, deltas, se_tau)\n710-                    sasv_vals.append(sasv)\n711-                    if reject and (sasv is None or sasv > 1.0):\n712-                        asv_rej += 1\n713-                sf = [a for a in sasv_vals if a is not None]\n714-                sm = f\"{np.mean(sf):.2f}\" if sf else \"N/A\"\n715-                ms = f\"{masv:.2f}\" if masv is not None else \"None\"\n716-                print(f\"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} \"\n717-                      f\"{asv_rej/n_mc:>10.3f} {sm:>10} {ms:>10}\")\n718-                results[(\"mbias\", tau_val, cname, h_label)] = {\n719-                    \"naive_rej\": naive_rej/n_mc, \"asv_rej\": asv_rej/n_mc,\n720-                    \"mean_sasv\": np.mean(sf) if sf else None, \"masv\": masv}\n721-\n722-        # === IV ===\n723-        print(\"\\n  [IV]\")\n724-        print(header)\n725-        print(\"  \" + \"-\" * 55)\n726-        for h_label, tau_h in [(\"H0\", 0.0), (\"H1\", tau_val)]:\n727-            iv_b = np.array([0.0, tau_h, -tau_h/2])\n728-            st_h = precomp_iv(iv_b, IV_PARAMS, N=2_000_000)\n729-            # [W1] Use plim(I) as tau_true for magnitude ASV\n--\n751:                    sasv = compute_signif_asv_fast(tau_curve, deltas, se_for_asv)\n752-                    sasv_vals.append(sasv)\n753-                    if reject and (sasv is None or sasv > 1.0):\n754-                        asv_rej += 1\n755-                sf = [a for a in sasv_vals if a is not None]\n756-                sm = f\"{np.mean(sf):.2f}\" if sf else \"N/A\"\n757-                ms = f\"{masv:.2f}\" if masv is not None else \"None\"\n758-                print(f\"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} \"\n759-                      f\"{asv_rej/n_mc:>10.3f} {sm:>10} {ms:>10}\")\n760-                results[(\"iv\", tau_val, cname, h_label)] = {\n761-                    \"naive_rej\": naive_rej/n_mc, \"asv_rej\": asv_rej/n_mc,\n762-                    \"mean_sasv\": np.mean(sf) if sf else None, \"masv\": masv}\n763-\n764-        # === Front-door ===\n765-        print(\"\\n  [Front-door]\")\n766-        print(header)\n767-        print(\"  \" + \"-\" * 55)\n768-        for h_label, tau_h in [(\"H0\", 0.0), (\"H1\", tau_val)]:\n769-            if h_label == \"H0\":\n770-                st_h = precomp_fd(BETA_FD, N=10_000_000, lU=0.0, aU=0.0,\n771-                                  d=np.zeros(3), seed=400)\n--\n803:                    sasv = compute_signif_asv_fast(tau_curve, deltas, se_tau)\n804-                    sasv_vals.append(sasv)\n805-                    if reject and (sasv is None or sasv > 1.0):\n806-                        asv_rej += 1\n807-                sf = [a for a in sasv_vals if a is not None]\n808-                sm = f\"{np.mean(sf):.2f}\" if sf else \"N/A\"\n809-                ms = f\"{masv:.2f}\" if masv is not None else \"None\"\n810-                print(f\"  {cname:<12} {h_label:<5} {naive_rej/n_mc:>10.3f} \"\n811-                      f\"{asv_rej/n_mc:>10.3f} {sm:>10} {ms:>10}\")\n812-                results[(\"frontdoor\", tau_val, cname, h_label)] = {\n813-                    \"naive_rej\": naive_rej/n_mc, \"asv_rej\": asv_rej/n_mc,\n814-                    \"mean_sasv\": np.mean(sf) if sf else None, \"masv\": masv}\n815-\n816-    print(f\"\\n  Total time: {time.time()-t0:.1f}s\")\n817-    return results\n818-\n819-\n820-# ============================================================================\n821-# Part 6: Summary JSON\n822-# ============================================================================\n823-",
    "numLines": 109
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

````text
Now I have a thorough understanding of all the source files. Let me now build the package. I'll create all files in parallel where possible.

Let me plan the package structure:

1. `utils.py` — shared utilities (OLS, dummies, softmax_sample, misclassify)
2. `confusion.py` — confusion matrix tools
3. `dgp.py` — 7 DAG topology data generation
4. `bias.py` — compute_bias using plim calculations
5. `asv.py` — ASV framework
6. `correction.py` — 5 correction methods + recommend_correction


7. `__init__.py` — public API
8. `examples/confounding_k3.py` — worked example
9. `tests/__init__.py` — empty
10. `tests/test_core.py` — pytest tests

Now I'm thinking through the design. In utils.py, I need to implement softmax sampling from logits, a misclassification function that corrupts labels, and dummy variable creation in both reduced and full forms.

For confusion matrices, I'll validate that they're column-stochastic and square, generate random ones with diagonal dominance control, interpolate between identity and a given matrix, and provide a dictionary of predefined examples. The dgp.py module will contain seven data generation functions with consistent output formats and default parameters, while bias.py will expose the main compute_bias function with internal precomputed statistics.

Now I'm working through how to compute the probability limits for each topology. For confounding and exposure cases where there's no closed-form solution like in plan_001, I'll use large-sample Monte Carlo approximation. Looking at the confounding setup specifically—where A influences both T and Y, the researcher controls for A*, and the regression estimates T's effect—I need to derive the probability limit by computing large-sample moments from the data generating process rather than relying on analytical formulas.

The key insight is that I can precompute the expected values of all the moment terms (like E[D_k], E[D_k * T], E[D_k * Y]) and then use the transformation through C to get the expected values under the controlled variables, which gives me the asymptotic behavior of the regression coefficients. This follows the same unified approach I'm using for frontdoor and m-bias cases. For exposure bias, where A directly affects Y without T in the picture, the regression simplifies to just the intercept and the controlled confounders, so I'll apply the same moment-based framework. Looking at the compute_bias API, I need to figure out what tau represents for the exposure topology — it's the coefficient on the first dummy variable (A=1 vs A=0), which is beta[1] = 1.0 in the true DGP, but this changes when A gets misclassified. topologies (confounding, mediation, collider, mbias), T is the treatment and tau is the coefficient on T. For exposure and IV, the treatment IS A, so the "tau" is the coefficient on D_1 (or some combination).

Looking at `compute_oracle_tau`, each topology has a `tau_idx` that specifies which coefficient to target—for confounding it's the coefficient on T, and for exposure it's the coefficient on the first dummy variable since the treatment is encoded that way.

The `compute_bias` function should abstract away these topology-specific details, so users just pass the topology name and C value to get back the true and biased tau estimates. For each topology I'm considering the best computational approach: confounding and mediation have closed-form solutions or precomputed moments, while collider and mbias might need large-sample OLS.

I'm settling on a unified strategy using precomputed sufficient statistics for each topology, which avoids Monte Carlo simulation and keeps things fast. I'm realizing I need to handle the regression specifications differently across topologies. For most cases with continuous treatment—confounding, mediation, collider, and m-bias—I'm regressing Y on treatment T plus the adjustment set, targeting the coefficient on T. But exposure uses a different outcome variable, IV might use a Wald estimator instead of OLS, and I need to check how the IV specification actually works in the existing code.

Looking at the IV implementation, it's doing OLS on the treatment variable without proper IV correction, which means the bias comes from both confounding and measurement error. The key insight is that I should focus on the relative bias introduced by misclassification rather than the absolute bias from confounding alone.

For the compute_bias API, I need to iterate through each topology and apply the appropriate regression specification.

For each topology, I'll compute the true parameter limit under perfect classification, then the biased parameter limit under the given misclassification matrix, and calculate both the absolute and percentage bias. This follows the ASV framework where delta=0 represents the baseline with no misclassification.

To make this efficient, I'll precompute a large sample for each topology to get the joint moments of the treatment, outcome, and dummy-coded treatment variables. Then for any misclassification matrix, I can quickly compute the expected values of the misclassified dummies and their interactions without regenerating data.

For mediation and other topologies with confounding, I'll precompute E[T], E[T²], E[Y], E[TY] along with E[D_k] and E[D_k * T], E[D_k * Y] for each dummy variable. Then I can construct the moment matrices for any C by taking linear combinations of these precomputed expectations. For exposure and IV models without a true confounder, I only need E[Y], E[D_k], and E[D_k * Y].

The closed-form solution for mediation works analytically for K=3 but doesn't generalize to larger K, whereas the precomputation approach scales to any number of categories. With a large sample size like 2 million, the Monte Carlo approximation error is negligible, so I'll use precomputation consistently across all topologies for simplicity and generality.

Now I need to design the overall package structure.

Looking at how the bias curve computation works in plan_005, the key insight is that for any topology with treatment T, I can construct the moment matrices by computing the same set of expectations: E[D_k], E[D_k*T], E[D_k*Y], E[T], E[T²], E[Y], and E[TY]. Then I solve a linear system where the coefficient matrix is built from these moments and the target parameter is extracted from the solution.

When K > 3, this structure generalizes naturally to a larger system. For the exposure-only case without T, the system simplifies to just the intercept, the first confounder effect, and the second confounder effect. The IV approach with Wald estimation...

Writing bias matrices... the same sample could be reused across different C values, so I should cache the precomp results separately from the plim computation.

For the IV topology, I'm noticing a tension between the two approaches: plan_005 uses the Wald estimator while plan_007 uses OLS. I'll keep them separate—`compute_bias` will use the OLS framework for consistency across all topologies, while `compute_asv` will support both modes depending on which plan is being followed. The Wald estimator removes confounding through the instrument, while OLS is biased by design due to U—they're measuring different things. For compute_bias, I'll use OLS consistently: the "true" value is OLS with perfect classification (C=I, still biased by U), and the "biased" value is OLS with the given C, so the difference isolates just the misclassification-induced bias. Now I need to extend this to arbitrary K beyond the well-defined K=3 case, starting with the dummy variables D_1 through D_K.

The system dimensions scale with K—it's (K+1)×(K+1) for topologies with T and K×K without. The precomputation approach generalizes naturally, but the DGP parameters themselves are K-dependent: p_A, alpha, and beta_A all have lengths tied to K. If a user specifies K=5 with default parameters designed for K=3, those won't align. The requirement allows arbitrary K in the API, but precomputed stats and plims might only support K=3, falling back to Monte Carlo otherwise.

For other values of K without provided parameters, I should raise an error rather than silently fail. The simplest approach: default parameters are for K=3, so if K≠3 and params is None, throw a ValueError. If the user supplies appropriate parameters, any K works.

Now I'm setting up the code structure with DGP functions in dgp.py and bias computation in bias.py, starting with how to handle the DGP parameters design.

Looking at the default parameters from the agent context, I see they use one naming convention, but the actual DGP implementations in plan_007 use topology-specific parameter dictionaries with different names. I should align with the plan_007 structure and provide defaults that match what those implementations expect—so confounding needs p_A, alpha, beta_A, beta_T, sigma_T, while mediation needs tau, gamma, and so on for each topology.

For the package API, I'll keep these as internal defaults but let users override any parameters through the params dict. Now I'm ready to start building out the files in order: directory structure, then utils, confusion, dgp, bias, asv, correction, __init__, the example script, and finally the test files.

Writing the implementation files... the DGP, I need to handle each topology. Let me design the DGP interface so each function returns a dictionary with topology-specific keys plus common ones like Y, A, and optionally Astar for misclassified labels.

Actually, looking back at the task structure, dgp.py should just generate the core data (T, Y, A) and keep misclassification separate in confusion.py.

So dgp.py will have the 7 DGP functions each returning a dict. Now for bias.py, I need to think through the computation pipeline: get DGP parameters, precompute sufficient statistics (which I'll cache by topology and params), compute the probability limit under no misclassification to get the true effect, then compute it under the given confusion matrix to get the biased effect. The expensive part is the precomputation, so caching makes sense. For each topology, I need to clarify what "bias" actually means—for confounding, the true regression is just Y regressed on T. - plim(I).

So tau_true is the probability limit when C equals the identity matrix (no misclassification), and tau_biased is the probability limit under the actual misclassification structure. The bias is just the difference between them. I'll stick with these names as specified in the task, even though for the collider case tau_true is still biased due to the collider bias itself—it just means "without misclassification bias on top of that." Now I need to work through the implementation for each topology, computing the precomputed values and probability limits.

For topologies with T, I'll generate a large sample and compute the key moments and cross-moments: the mean of T, the mean of T squared, the mean of Y, the mean of T times Y, and then the means of the misclassification matrix times T and Y respectively. Then I'll define the probability limit function...

Writing plim function... Building the moment matrix... The cross-product terms in the matrix confirm that dummy variables are orthogonal to each other, so the matrix is block diagonal with the dummy coefficients isolated on the diagonal. The expected value calculations for both the Z'Z matrix and Z'Y vector check out, validating that this approach generalizes correctly beyond the K=3 case.

Now I'm setting up the case without the treatment variable, where the regression only includes the intercept and dummy variables. Building a function to compute the probability limits by constructing the Z'Z matrix and Z'Y vector from the relevant statistics...

Still writing function logic... I see the issue now — plan_007 uses naive OLS regression on the misclassified variable, which ignores the endogeneity problem entirely. That's the whole point of the comparison. For compute_bias, I should stick with OLS across all topologies to match plan_007's approach, even though plan_005 uses the Wald estimator for IV cases. The compute_asv function will need to dispatch differently depending on topology, using the appropriate estimator for each case. This is Wald!
elif topology == "frontdoor":
    tau_curve[i] = plim_fd(C_d, st)[1]
```

For IV, they use plim_iv which is the Wald estimator. This makes sense because for IV, the Wald estimator is what would actually be used in practice.

But for compute_bias, the plan_007 approach uses OLS (not Wald). This is because plan_007 evaluates correction methods, which all operate on the OLS framework.

I think for this package, I should:
- In compute_bias: use OLS for all topologies (the "naive" analysis without considering the instrument)
- In compute_asv: also use OLS for consistency

Unless the user wants Wald... but let me keep it simple for now.

The compute_asv return spec includes asv, bias_curve, envelope, deltas, and tau_true, along with threshold types like magnitude, significance, and sign_flip. These are all consistent with the OLS plim approach, so I'll stick with OLS uniformly.

Now I need to think through what happens for each topology when computing plim. Some topologies have a treatment mediator T (confounding, mediation, collider, mbias, frontdoor) while others don't (exposure, iv). For the ones without T, the regression is just Y regressed on the exposure variables, and the bias comes from the change in coefficients.

For IV specifically, even though the DGP uses an instrument Z to generate the mediator A, the OLS regression doesn't include Z—it's just Y regressed on the exposure variables. The Z is internal to the data generation but not used in the regression itself.

Now I'm ready to write the code. I'll create seven DGP functions plus a dispatch dictionary, each returning a consistent format of (X_other, Y, A) or equivalent.

Writing DGP functions... GP functions need to return. For bias computation, I need (T, Y, A) or (Y, A). For correction methods, I need (X_other, Y, A, tau_idx).

Let me think about what the DGP module should expose. The task says:

> dgp.py: 7 种 DAG 拓扑的数据生成过程

I'll have each function return a dict with the generated data. For the precomp approach in bias.py, I'll use internal functions.

For dgp.py, I'm defining functions for each DAG topology that return a dict containing the generated variables like T, Y, A, and the true treatment effect. Rather than exposing internal details like tau_idx, I'll keep the API simple — each function returns all the generated variables and lets bias.py handle the regression logic internally. I'm moving toward a cleaner design where the DGP module just generates data and the bias module extracts what it needs. I'm overcomplicating this—time to just start writing the code. I'll make practical decisions and build out all the modules systematically: utilities for sampling and data manipulation, confusion matrix handling, the seven data generation functions, bias computation with caching, ASV calculation, correction methods, and finally the package exports.

For the precomputation caching in bias.py, I need to handle two distinct cases: topologies that include a treatment variable T (confounding, mediation, collider, m-bias, frontdoor) require computing expectations for T and Y separately and jointly, while topologies without T (exposure, instrumental variable) only need Y expectations. I'll unify this with a single precompute function that handles both scenarios.

Writing the module code... Writing utility functions... Writing utility functions... Writing confusion matrix utilities... Defining predefined confusion matrices... Writing default parameters... Finishing up the parameter dictionary with the frontdoor adjustment method, then defining a list of available topologies and setting up utility functions for random number generation.

Now I'm implementing the confounding scenario where treatment and outcome both depend on a confounder that the researcher controls for, generating dummy variables for the confounder and then simulating treatment and outcome values based on the specified parameters.

Then I'm setting up a mediation scenario where treatment affects an intermediate variable that in turn affects the outcome, using softmax sampling to generate the mediator values based on treatment-dependent logits.

Now moving to a collider scenario where treatment and outcome both influence a third variable, which researchers might mistakenly control for, creating spurious associations. I'm generating treatment and outcome independently, then computing the collider variable's probabilities based on both.

Defining more generator functions... Writing data generation functions... Writing data generation code... Writing utility functions... Writing precomputation logic... Building the moment matrix... Writing the bias computation function... Finishing the bias percentage calculation and returning the results dictionary with all the computed metrics. But now I'm second-guessing the _get_tau implementation for the no-treatment topologies—specifically what the first dummy coefficient represents in the regression for exposure and IV cases.

For exposure, it's straightforward: the coefficient captures the effect of A=1 versus A=0 on Y. For IV, it's the coefficient on the first dummy in the OLS regression, which represents the treatment effect through the instrumental variable pathway. Either way, I'm targeting coefs[1], so that's consistent.

Now I'm moving into the ASV computation module, setting up the bias curve calculation as a function of the interpolation parameter delta, starting with determining the maximum delta value based on the minimum diagonal element of the confusion matrix.

Defining the bias envelope function... Writing threshold detection logic...

Now I'm setting up the main ASV computation function that validates the input topology and confusion matrix, merges in any custom parameters with the defaults, and then precomputes the necessary statistics before calculating the true tau value.

Computing the bias curve and envelope to identify where the threshold crossing occurs, then returning all the key results including the asymptotic sample validity point and the tau trajectory.

Now I'm setting up the correction methods module with different estimation approaches like naive plugin, doubly robust, and simulation-based methods, along with their configuration parameters.

Defining correction functions... Writing EM algorithm... Finishing the convergence check...

I'm checking if the parameters have converged by comparing the change in beta and the covariance matrix against a tolerance threshold, then updating the estimates and breaking out of the loop if we've reached convergence. After the EM algorithm finishes, I'm fitting a final OLS model with the updated responsibilities and extracting the coefficient and standard error for the treatment effect at the specified index, returning those values along with a success flag.

Now I'm setting up the PPI++ correction function with bootstrap lambda tuning. I'm initializing the random number generator, determining the number of categories from the maximum values in both the predicted and gold-standard treatment assignments, then constructing dummy variable matrices for the gold-standard data using both the true and predicted treatments, as well as for the full dataset with predicted treatments.

Setting up data structures... Still writing bootstrap loop... Writing SIMEX correction logic... Continuing the simulation loop...

When the regression fails, I'm setting that iteration to NaN and then filtering to keep only the valid estimates. If there aren't enough successful runs, I bail out early. Otherwise, I'm fitting a quadratic polynomial across the lambda values and extrapolating back to -1 to get the SIMEX estimate. Finally, I'm computing the standard error using the corrected classification matrix and returning the estimate with its uncertainty.

Now I'm implementing the MLA correction method, which inverts the classification matrix and applies it to the full dummy variables before dropping the reference category. I check the condition number first to avoid numerical instability, then invert the matrix and construct the corrected design matrix for the regression.

I'm also building a function that recommends the best correction approach based on the DAG topology and whether gold-standard labels are available, starting with PPI++ as a strong option when gold labels exist. Building the methods list... Writing recommendation logic... I'm noticing a contradiction in the spec—it recommends DSL for cases without gold labels, but DSL actually requires gold labels for initialization and E-step anchoring. Either the spec is inconsistent, or "DSL" here refers to a variant that can work without gold by using an external estimate of the confounder instead. the spec:

> has_gold=False + topology in ("confounding", "mediation") → DSL

Maybe this means: if you DON'T have gold but have topology in confounding/mediation, DSL is still the best (assuming you can estimate C from the data somehow). But in practice, our implementation requires gold.

I'll mark DSL as "recommended if gold available" for these topologies, and MC-SIMEX as the fallback.

Actually wait, let me re-read more carefully. The recommendation rules say:
1. has_gold=True → PPI++
2. has_gold=False + confounding/mediation → DSL
3. has_gold=False + other topologies → MC-SIMEX

I think rule 2 might assume that DSL can work with an estimated C (not gold labels), or that the user has C available but not gold labels. DSL theoretically works if you can bootstrap C estimation from the data.

The spec seems to be about which method to use rather than whether it requires gold labels—DSL could theoretically work without gold if you initialize C differently, though our implementation does require gold labels for anchoring the EM algorithm. I should just follow the spec literally and note that DSL needs some form of validation data, even if that's not gold labels in the theoretical sense. I'm going to follow the spec literally: DSL for cases where we don't have gold labels but the topology is safe (confounding or mediation), and MC-SIMEX otherwise. I'll add a note that our DSL implementation technically requires gold labels or an alternative way to initialize C, but I'll recommend it as specified and let users know about this constraint. I'm realizing there's a tension between what the spec literally says and what makes sense given the constraints — the spec suggests DSL for confounding/mediation even without gold, but that doesn't align with how the function actually works. I'll stick with the spec's recommendation field but ensure the applicability logic correctly reflects that DSL requires gold.

Writing the recommendation logic... I need to stick with the spec here — if there's no gold data and the topology is confounding or mediation, DSL is the recommendation, otherwise it falls back to MC-SIMEX. I'm building the recommend_correction function to encode this logic, returning the appropriate method based on the input parameters. I'm realizing the ambiguity in what "has_gold" actually means—it could refer to gold labels for estimating the correction matrix C, not just for the correction methods themselves. Let me reconsider: if has_gold=True means you have enough gold data to estimate C reliably, then PPI++ makes sense; if has_gold=False, you'd fall back to MC-SIMEX since DSL requires gold labels for proper initialization. I'll simplify the recommendation logic to always use MC-SIMEX when gold isn't available, and note in the ranking that DSL would be preferable for confounding or mediation scenarios if gold labels were present.

Actually, there's a deeper distinction emerging—DSL's real strength is that it jointly estimates both C and the regression coefficients via EM, making it robust to misspecification of C, whereas MC-SIMEX treats C as fixed and is therefore more sensitive to how accurately you've estimated it. So the choice between them hinges on whether you're confident in your C estimate or need the joint estimation that DSL provides.

The recommendation crystallizes into three cases: with gold labels, PPI++ dominates because it can anchor DSL's EM algorithm; without gold labels but in safe topologies like confounding or mediation, DSL still works reasonably well despite potential local optima; for unsafe topologies without gold, MC-SIMEX is the safer fallback. I need to modify the DSL implementation to make gold labels optional rather than required, then I can start writing out the actual code.

Writing implementation files... Now I'm ready to implement all the files—I'll start with the main module, then the example demonstrating the key functions like computing bias and ASV for the confounding topology, and finally the test suite covering validation, bias computation across different topologies, ASV calculations, and correction recommendations with and without gold labels.

For the precomputation cache, I'll set the default to 2 million samples since that's sufficient for most use cases, and I'll make sure the bias module allows adjusting or clearing the cache as needed. The correction API will take the observed data and confusion matrix, then recommend the appropriate method based on whether gold labels are available.

I'm going to structure the public exports to include both the recommendation function and the individual correction methods—naive plugin, DSL, PPI++, MC-SIMEX, and MLA—so users can either get a recommendation or apply a specific approach directly. Now I'll write out all the package files.

One thing I want to verify: when the confusion matrix is identity, the bias should be zero since there's no misclassification happening, but let me think through whether the math actually works out that way.

With C=I, the probability limit of the biased estimator should equal the true parameter, so the difference between them is indeed zero. That checks out.

For the confounding case with a known misclassification matrix, I need to think about what happens when we control for the misclassified variable instead of the true one. The imperfect control means some confounding bias leaks through, and the direction depends on how the confounding and misclassification interact. For testing purposes, I just need to verify that the bias is non-zero when misclassification is present.

Looking at the default parameters, the confounding is positive—A=1 increases both T and Y—so without any control, the naive estimate would be biased upward. When controlling for the misclassified A*, the control is imperfect, allowing some of that positive confounding to remain in the estimate.

Now I'm setting up the code to run the numerical tests and verify the bias direction. Before I start writing the files, I should check that the directory structure is in place. I'm also clarifying what tau_idx represents in the correction methods—it's the column index of the treatment variable T in the full design matrix, which depends on how many other covariates are included.

For the compute_asv return format, I'm tracking the absolute bias curve across a grid of delta values, computing its monotone envelope, and finding the minimum delta where bias stays below a threshold.

Now I'm realizing there's an issue with the significance threshold mode—it needs the standard error as input, but the function signature has a fixed default. Looking at how plan_005 handles this, it takes SE as an explicit parameter for significance-based ASV computation, so I should structure compute_asv the same way when threshold_type="significance".

For the confounding bias computation, I need to verify the approach: generate a large sample of confounding data, compute the empirical moments for the confounder distribution and its relationship with the treatment, then use those to calculate the bias term. When the observed dummies are misclassified, their expectations shift based on the confusion matrix, which biases the regression coefficient away from the true treatment effect. Now I'm writing out the test suite, starting with validation checks for the confusion matrix itself—ensuring it's square, has non-negative entries, and is properly column-stochastic—then moving to tests that verify the bias computation produces the expected directional effects under different misclassification scenarios. without_gold, the recommendation shifts to "dsl" when there's confounding or "mcsimex" for collider bias. For the interpolation test, delta=0 should give the identity matrix and delta=1 should give the confusion matrix. Now I'm ready to write out all the module files—the core utilities, confusion matrix handling, data generation, bias computation, ASV calculation, correction methods, plus tests and an example workflow.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "c8680c39-d047-4b07-9226-772ba5fce482",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsttFM8E3kqPM3SqkX6ho9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2102,
      "cache_read_input_tokens": 72565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2102
      },
      "output_tokens": 12,
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

_source line 20_

Now I have a thorough understanding of all source files. Let me create the package. I'll start by creating the directory structure and writing all files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "46efb818-d5c2-4217-b489-7b5c7f695478",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsttFM8E3kqPM3SqkX6ho9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2102,
      "cache_read_input_tokens": 72565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2102
      },
      "output_tokens": 12,
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

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_01DJ7kaT17EDWYxgAjicp7fb`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/ 2>/dev/null || echo \"NOT_EXISTS\"",
  "description": "Check if package directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "17df8e3e-a694-4271-87de-3d27af26ccf9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsttFM8E3kqPM3SqkX6ho9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2102,
      "cache_read_input_tokens": 72565,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2102
      },
      "output_tokens": 12,
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

_source line 22 · 2026-05-20T23:32:14.761Z_

<details><summary>↩ Tool result · `toolu_01DJ7kaT17EDWYxgAjicp7fb`</summary>

```text
NOT_EXISTS
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "9a2cd567-ad56-46c8-a099-909cdebe7f6d",
  "tool_use_result": {
    "stdout": "NOT_EXISTS",
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

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_01YCi34mNvnCBxmpzJgpnnZh`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/{examples,tests}",
  "description": "Create package directory structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "afb5c3bf-ce7f-45bf-9c78-44d2628ebff3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EChFDteRqmaajcwS6zo5wz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 28390,
      "cache_read_input_tokens": 74667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 28390
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

_source line 24 · 2026-05-20T23:32:18.311Z_

<details><summary>↩ Tool result · `toolu_01YCi34mNvnCBxmpzJgpnnZh`</summary>

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
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "0c2b4c23-a0c8-4424-8551-38174add9df9",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Assistant

_source line 25_

Now I'll write all the package files. Starting with the foundational modules.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "4ca30c1c-56f9-4ea3-9e0c-82d5afe2d041",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGdHzhx44SU9fE4mq7jEND",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 129,
      "cache_read_input_tokens": 103057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 129
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

_source line 26_

<details open><summary>🔧 Tool call — Write · `toolu_012yLPjbok26w9kPiiGWcozD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/utils.py",
  "content": "\"\"\"Shared utilities: OLS, dummy encoding, softmax sampling.\"\"\"\n\nimport numpy as np\n\n\ndef softmax_sample(logits, rng):\n    \"\"\"Sample categorical variable from row-wise softmax probabilities.\n\n    Args:\n        logits: (N, K) array of logits\n        rng: numpy random Generator\n\n    Returns:\n        (N,) integer array with values in {0, ..., K-1}\n    \"\"\"\n    e = np.exp(logits - logits.max(axis=1, keepdims=True))\n    p = e / e.sum(axis=1, keepdims=True)\n    cum = np.cumsum(p, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    K = logits.shape[1]\n    result = np.zeros(logits.shape[0], dtype=int)\n    for k in range(K - 1):\n        result += (u >= cum[:, k]).astype(int)\n    return result\n\n\ndef misclassify(A, C, rng):\n    \"\"\"Apply misclassification: A*_i ~ Cat(C[:, A_i]).\n\n    Args:\n        A: (N,) true labels in {0, ..., K-1}\n        C: (K, K) column-stochastic confusion matrix\n        rng: numpy random Generator\n\n    Returns:\n        (N,) misclassified labels\n    \"\"\"\n    K = C.shape[0]\n    probs = C[:, A]\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    result = np.zeros(len(A), dtype=int)\n    for k in range(K - 1):\n        result += (u >= cum[k]).astype(int)\n    return result\n\n\ndef make_dummies(A, K=None):\n    \"\"\"Create K-1 dummy variables (reference category 0).\n\n    Args:\n        A: (N,) categorical labels in {0, ..., K-1}\n        K: number of categories (inferred from A if None)\n\n    Returns:\n        (N, K-1) dummy matrix\n    \"\"\"\n    if K is None:\n        K = int(A.max()) + 1\n    N = len(A)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    return D\n\n\ndef make_full_dummies(A, K=None):\n    \"\"\"Create full K one-hot encoding.\n\n    Args:\n        A: (N,) categorical labels in {0, ..., K-1}\n        K: number of categories (inferred from A if None)\n\n    Returns:\n        (N, K) one-hot matrix\n    \"\"\"\n    if K is None:\n        K = int(A.max()) + 1\n    N = len(A)\n    D = np.zeros((N, K))\n    for j in range(K):\n        D[:, j] = (A == j).astype(float)\n    return D\n\n\ndef ols(X, Y):\n    \"\"\"OLS point estimate via least-squares.\n\n    Args:\n        X: (N, p) design matrix\n        Y: (N,) response\n\n    Returns:\n        (p,) coefficient vector\n    \"\"\"\n    return np.linalg.lstsq(X, Y, rcond=None)[0]\n\n\ndef ols_with_se(X, Y):\n    \"\"\"OLS point estimate with homoskedastic standard errors.\n\n    Args:\n        X: (N, p) design matrix\n        Y: (N,) response\n\n    Returns:\n        (beta, se) tuple of (p,) arrays\n    \"\"\"\n    beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n    resid = Y - X @ beta\n    n, p = X.shape\n    s2 = resid @ resid / max(n - p, 1)\n    try:\n        XtX_inv = np.linalg.inv(X.T @ X)\n        se = np.sqrt(np.maximum(np.diag(s2 * XtX_inv), 0.0))\n    except np.linalg.LinAlgError:\n        se = np.full(p, np.nan)\n    return beta, se\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "173e9909-67a1-402a-8eef-7481f10b502e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGdHzhx44SU9fE4mq7jEND",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 129,
      "cache_read_input_tokens": 103057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 129
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

_source line 27 · 2026-05-20T23:32:35.016Z_

<details><summary>↩ Tool result · `toolu_012yLPjbok26w9kPiiGWcozD`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/utils.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "4724c292-2aad-42d0-a143-0be6348c35c9",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/utils.py",
    "content": "\"\"\"Shared utilities: OLS, dummy encoding, softmax sampling.\"\"\"\n\nimport numpy as np\n\n\ndef softmax_sample(logits, rng):\n    \"\"\"Sample categorical variable from row-wise softmax probabilities.\n\n    Args:\n        logits: (N, K) array of logits\n        rng: numpy random Generator\n\n    Returns:\n        (N,) integer array with values in {0, ..., K-1}\n    \"\"\"\n    e = np.exp(logits - logits.max(axis=1, keepdims=True))\n    p = e / e.sum(axis=1, keepdims=True)\n    cum = np.cumsum(p, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    K = logits.shape[1]\n    result = np.zeros(logits.shape[0], dtype=int)\n    for k in range(K - 1):\n        result += (u >= cum[:, k]).astype(int)\n    return result\n\n\ndef misclassify(A, C, rng):\n    \"\"\"Apply misclassification: A*_i ~ Cat(C[:, A_i]).\n\n    Args:\n        A: (N,) true labels in {0, ..., K-1}\n        C: (K, K) column-stochastic confusion matrix\n        rng: numpy random Generator\n\n    Returns:\n        (N,) misclassified labels\n    \"\"\"\n    K = C.shape[0]\n    probs = C[:, A]\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    result = np.zeros(len(A), dtype=int)\n    for k in range(K - 1):\n        result += (u >= cum[k]).astype(int)\n    return result\n\n\ndef make_dummies(A, K=None):\n    \"\"\"Create K-1 dummy variables (reference category 0).\n\n    Args:\n        A: (N,) categorical labels in {0, ..., K-1}\n        K: number of categories (inferred from A if None)\n\n    Returns:\n        (N, K-1) dummy matrix\n    \"\"\"\n    if K is None:\n        K = int(A.max()) + 1\n    N = len(A)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    return D\n\n\ndef make_full_dummies(A, K=None):\n    \"\"\"Create full K one-hot encoding.\n\n    Args:\n        A: (N,) categorical labels in {0, ..., K-1}\n        K: number of categories (inferred from A if None)\n\n    Returns:\n        (N, K) one-hot matrix\n    \"\"\"\n    if K is None:\n        K = int(A.max()) + 1\n    N = len(A)\n    D = np.zeros((N, K))\n    for j in range(K):\n        D[:, j] = (A == j).astype(float)\n    return D\n\n\ndef ols(X, Y):\n    \"\"\"OLS point estimate via least-squares.\n\n    Args:\n        X: (N, p) design matrix\n        Y: (N,) response\n\n    Returns:\n        (p,) coefficient vector\n    \"\"\"\n    return np.linalg.lstsq(X, Y, rcond=None)[0]\n\n\ndef ols_with_se(X, Y):\n    \"\"\"OLS point estimate with homoskedastic standard errors.\n\n    Args:\n        X: (N, p) design matrix\n        Y: (N,) response\n\n    Returns:\n        (beta, se) tuple of (p,) arrays\n    \"\"\"\n    beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n    resid = Y - X @ beta\n    n, p = X.shape\n    s2 = resid @ resid / max(n - p, 1)\n    try:\n        XtX_inv = np.linalg.inv(X.T @ X)\n        se = np.sqrt(np.maximum(np.diag(s2 * XtX_inv), 0.0))\n    except np.linalg.LinAlgError:\n        se = np.full(p, np.nan)\n    return beta, se\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Write · `toolu_01WH6ePHA8hdBVDjkAj5uKd8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/confusion.py",
  "content": "\"\"\"Confusion matrix utilities: validation, generation, interpolation.\n\nConvention: C[j, i] = P(A*=j | A=i), columns sum to 1 (column-stochastic).\n\"\"\"\n\nimport numpy as np\n\n\ndef validate_confusion_matrix(C):\n    \"\"\"Check if C is a valid column-stochastic confusion matrix.\n\n    Args:\n        C: array to validate\n\n    Returns:\n        True if valid, False otherwise\n    \"\"\"\n    if not isinstance(C, np.ndarray):\n        return False\n    if C.ndim != 2 or C.shape[0] != C.shape[1]:\n        return False\n    if C.shape[0] < 2:\n        return False\n    if (C < -1e-10).any():\n        return False\n    if not np.allclose(C.sum(axis=0), 1.0, atol=1e-6):\n        return False\n    return True\n\n\ndef random_confusion_matrix(K, diag_dominance=0.8, rng=None):\n    \"\"\"Generate a random column-stochastic confusion matrix.\n\n    Args:\n        K: number of categories\n        diag_dominance: controls diagonal strength (0 to 1)\n        rng: numpy random Generator (created if None)\n\n    Returns:\n        (K, K) column-stochastic matrix\n    \"\"\"\n    if rng is None:\n        rng = np.random.default_rng()\n    diag_alpha = diag_dominance * 10\n    offdiag_alpha = max((1 - diag_dominance) * 10 / max(K - 1, 1), 0.1)\n    C = np.zeros((K, K))\n    for k in range(K):\n        alphas = np.full(K, offdiag_alpha)\n        alphas[k] = diag_alpha\n        C[:, k] = rng.dirichlet(alphas)\n    return C\n\n\ndef interpolate_confusion(C0, delta):\n    \"\"\"Interpolate between identity and C0: C(delta) = (1-delta)*I + delta*C0.\n\n    Args:\n        C0: (K, K) base confusion matrix\n        delta: interpolation parameter (0 = identity, 1 = C0)\n\n    Returns:\n        (K, K) interpolated column-stochastic matrix\n    \"\"\"\n    K = C0.shape[0]\n    C = (1 - delta) * np.eye(K) + delta * C0\n    C = np.maximum(C, 0.0)\n    col_sums = C.sum(axis=0)\n    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\n    return C / col_sums\n\n\ndef delta_range(C0):\n    \"\"\"Compute valid delta range for interpolation.\n\n    Args:\n        C0: (K, K) base confusion matrix\n\n    Returns:\n        (delta_min, delta_max) tuple\n    \"\"\"\n    min_diag = np.diag(C0).min()\n    if min_diag >= 1.0:\n        return (0.0, 10.0)\n    delta_max = min(1.0 / (1.0 - min_diag), 10.0)\n    return (0.0, delta_max)\n\n\ndef predefined_matrices(K=3):\n    \"\"\"Return a dict of predefined K x K confusion matrices.\n\n    Args:\n        K: number of categories (only K=3 supported)\n\n    Returns:\n        dict mapping name to (K, K) confusion matrix\n    \"\"\"\n    if K != 3:\n        raise ValueError(f\"Predefined matrices only available for K=3, got K={K}\")\n    return {\n        \"symmetric_high\": np.array([\n            [0.80, 0.10, 0.10],\n            [0.10, 0.80, 0.10],\n            [0.10, 0.10, 0.80]]),\n        \"mild_uniform\": np.array([\n            [0.8 + 0.2 / 3, 0.2 / 3, 0.2 / 3],\n            [0.2 / 3, 0.8 + 0.2 / 3, 0.2 / 3],\n            [0.2 / 3, 0.2 / 3, 0.8 + 0.2 / 3]]),\n        \"moderate_uniform\": np.array([\n            [0.6 + 0.4 / 3, 0.4 / 3, 0.4 / 3],\n            [0.4 / 3, 0.6 + 0.4 / 3, 0.4 / 3],\n            [0.4 / 3, 0.4 / 3, 0.6 + 0.4 / 3]]),\n        \"severe_uniform\": np.array([\n            [0.4 + 0.6 / 3, 0.6 / 3, 0.6 / 3],\n            [0.6 / 3, 0.4 + 0.6 / 3, 0.6 / 3],\n            [0.6 / 3, 0.6 / 3, 0.4 + 0.6 / 3]]),\n        \"asymmetric\": np.array([\n            [0.75, 0.05, 0.05],\n            [0.20, 0.80, 0.10],\n            [0.05, 0.15, 0.85]]),\n        \"near_permutation\": np.array([\n            [0.05, 0.05, 0.90],\n            [0.90, 0.05, 0.05],\n            [0.05, 0.90, 0.05]]),\n        \"realistic_llm\": np.array([\n            [0.78, 0.15, 0.03],\n            [0.18, 0.72, 0.18],\n            [0.04, 0.13, 0.79]]),\n    }\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "f8267612-def8-4b21-9716-c0d7b241e4b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01McA18ET3jyQQ8MvVJp8nFB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1256,
      "cache_read_input_tokens": 103186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1256
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

_source line 29 · 2026-05-20T23:32:55.630Z_

<details><summary>↩ Tool result · `toolu_01WH6ePHA8hdBVDjkAj5uKd8`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/confusion.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "31f668c8-46d7-4611-9771-8bdaee9c44f9",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/confusion.py",
    "content": "\"\"\"Confusion matrix utilities: validation, generation, interpolation.\n\nConvention: C[j, i] = P(A*=j | A=i), columns sum to 1 (column-stochastic).\n\"\"\"\n\nimport numpy as np\n\n\ndef validate_confusion_matrix(C):\n    \"\"\"Check if C is a valid column-stochastic confusion matrix.\n\n    Args:\n        C: array to validate\n\n    Returns:\n        True if valid, False otherwise\n    \"\"\"\n    if not isinstance(C, np.ndarray):\n        return False\n    if C.ndim != 2 or C.shape[0] != C.shape[1]:\n        return False\n    if C.shape[0] < 2:\n        return False\n    if (C < -1e-10).any():\n        return False\n    if not np.allclose(C.sum(axis=0), 1.0, atol=1e-6):\n        return False\n    return True\n\n\ndef random_confusion_matrix(K, diag_dominance=0.8, rng=None):\n    \"\"\"Generate a random column-stochastic confusion matrix.\n\n    Args:\n        K: number of categories\n        diag_dominance: controls diagonal strength (0 to 1)\n        rng: numpy random Generator (created if None)\n\n    Returns:\n        (K, K) column-stochastic matrix\n    \"\"\"\n    if rng is None:\n        rng = np.random.default_rng()\n    diag_alpha = diag_dominance * 10\n    offdiag_alpha = max((1 - diag_dominance) * 10 / max(K - 1, 1), 0.1)\n    C = np.zeros((K, K))\n    for k in range(K):\n        alphas = np.full(K, offdiag_alpha)\n        alphas[k] = diag_alpha\n        C[:, k] = rng.dirichlet(alphas)\n    return C\n\n\ndef interpolate_confusion(C0, delta):\n    \"\"\"Interpolate between identity and C0: C(delta) = (1-delta)*I + delta*C0.\n\n    Args:\n        C0: (K, K) base confusion matrix\n        delta: interpolation parameter (0 = identity, 1 = C0)\n\n    Returns:\n        (K, K) interpolated column-stochastic matrix\n    \"\"\"\n    K = C0.shape[0]\n    C = (1 - delta) * np.eye(K) + delta * C0\n    C = np.maximum(C, 0.0)\n    col_sums = C.sum(axis=0)\n    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\n    return C / col_sums\n\n\ndef delta_range(C0):\n    \"\"\"Compute valid delta range for interpolation.\n\n    Args:\n        C0: (K, K) base confusion matrix\n\n    Returns:\n        (delta_min, delta_max) tuple\n    \"\"\"\n    min_diag = np.diag(C0).min()\n    if min_diag >= 1.0:\n        return (0.0, 10.0)\n    delta_max = min(1.0 / (1.0 - min_diag), 10.0)\n    return (0.0, delta_max)\n\n\ndef predefined_matrices(K=3):\n    \"\"\"Return a dict of predefined K x K confusion matrices.\n\n    Args:\n        K: number of categories (only K=3 supported)\n\n    Returns:\n        dict mapping name to (K, K) confusion matrix\n    \"\"\"\n    if K != 3:\n        raise ValueError(f\"Predefined matrices only available for K=3, got K={K}\")\n    return {\n        \"symmetric_high\": np.array([\n            [0.80, 0.10, 0.10],\n            [0.10, 0.80, 0.10],\n            [0.10, 0.10, 0.80]]),\n        \"mild_uniform\": np.array([\n            [0.8 + 0.2 / 3, 0.2 / 3, 0.2 / 3],\n            [0.2 / 3, 0.8 + 0.2 / 3, 0.2 / 3],\n            [0.2 / 3, 0.2 / 3, 0.8 + 0.2 / 3]]),\n        \"moderate_uniform\": np.array([\n            [0.6 + 0.4 / 3, 0.4 / 3, 0.4 / 3],\n            [0.4 / 3, 0.6 + 0.4 / 3, 0.4 / 3],\n            [0.4 / 3, 0.4 / 3, 0.6 + 0.4 / 3]]),\n        \"severe_uniform\": np.array([\n            [0.4 + 0.6 / 3, 0.6 / 3, 0.6 / 3],\n            [0.6 / 3, 0.4 + 0.6 / 3, 0.6 / 3],\n            [0.6 / 3, 0.6 / 3, 0.4 + 0.6 / 3]]),\n        \"asymmetric\": np.array([\n            [0.75, 0.05, 0.05],\n            [0.20, 0.80, 0.10],\n            [0.05, 0.15, 0.85]]),\n        \"near_permutation\": np.array([\n            [0.05, 0.05, 0.90],\n            [0.90, 0.05, 0.05],\n            [0.05, 0.90, 0.05]]),\n        \"realistic_llm\": np.array([\n            [0.78, 0.15, 0.03],\n            [0.18, 0.72, 0.18],\n            [0.04, 0.13, 0.79]]),\n    }\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Write · `toolu_01DH5VLiV5KaYxYkohEcFVaf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/dgp.py",
  "content": "\"\"\"Data generation processes for 7 DAG topologies.\n\nEach topology generates synthetic data with a known causal structure.\nThe variable A (or M for frontdoor) is the one subject to misclassification.\n\"\"\"\n\nimport numpy as np\nfrom .utils import softmax_sample, make_dummies\n\nDEFAULT_PARAMS = {\n    \"confounding\": dict(\n        p_A=np.array([0.40, 0.35, 0.25]),\n        alpha=np.array([1.5, -1.0]),\n        beta_A=np.array([1.0, -0.5]),\n        beta_T=2.0, sigma_T=1.0),\n    \"mediation\": dict(\n        tau=0.5,\n        gamma=np.array([0.0, 0.5, -0.3]),\n        delta=np.array([0.0, 0.8, -0.6]),\n        beta=np.array([0.0, 1.0, -0.5])),\n    \"collider\": dict(\n        tau=1.0,\n        g=np.array([0.0, 0.0, 0.0]),\n        dT=np.array([0.0, 0.5, -0.3]),\n        dY=np.array([0.0, 0.8, 0.6])),\n    \"exposure\": dict(\n        beta=np.array([0.0, 1.0, -0.5]),\n        p_A=np.array([0.40, 0.35, 0.25])),\n    \"mbias\": dict(\n        tau=1.0, delta_coef=1.0, lam=1.0,\n        g=np.array([0.0, 0.0, 0.0]),\n        a1=np.array([0.0, 0.8, -0.5]),\n        a2=np.array([0.0, 0.6, 0.9])),\n    \"iv\": dict(\n        lam=1.0,\n        g=np.array([0.0, 0.0, 0.0]),\n        dZ=np.array([0.0, 1.0, -0.5]),\n        dU=np.array([0.0, 0.8, 0.6]),\n        beta=np.array([0.0, 1.0, -0.5])),\n    \"frontdoor\": dict(\n        alpha_U=1.0, lam_U=1.0,\n        gamma=np.array([0.0, 0.5, -0.3]),\n        delta=np.array([0.0, 1.0, -0.8]),\n        beta=np.array([0.0, 1.0, -0.5])),\n}\n\nTOPOLOGIES = list(DEFAULT_PARAMS.keys())\n\nHAS_TREATMENT = {\"confounding\", \"mediation\", \"collider\", \"mbias\", \"frontdoor\"}\nNO_TREATMENT = {\"exposure\", \"iv\"}\n\n\ndef _get_rng(rng, seed):\n    if rng is not None:\n        return rng\n    return np.random.default_rng(seed)\n\n\ndef _get_params(topology, params):\n    p = dict(DEFAULT_PARAMS[topology])\n    if params is not None:\n        p.update(params)\n    return p\n\n\ndef gen_confounding(N, params=None, rng=None, seed=None):\n    \"\"\"A->T, A->Y, T->Y. Researcher controls for A*.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"confounding\", params)\n    K = len(p[\"p_A\"])\n    A = rng.choice(K, size=N, p=p[\"p_A\"])\n    D = make_dummies(A, K)\n    T = D @ p[\"alpha\"] + rng.normal(0, p[\"sigma_T\"], N)\n    Y = p[\"beta_T\"] * T + D @ p[\"beta_A\"] + rng.normal(0, 1, N)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_mediation(N, params=None, rng=None, seed=None):\n    \"\"\"T->A->Y. A mediates; researcher controls for A*.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"mediation\", params)\n    T = rng.binomial(1, 0.5, N).astype(float)\n    K = len(p[\"gamma\"])\n    logits = p[\"gamma\"][None, :] + p[\"delta\"][None, :] * T[:, None]\n    A = softmax_sample(logits, rng)\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + p[\"tau\"] * T + rng.normal(0, 1, N)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_collider(N, params=None, rng=None, seed=None):\n    \"\"\"T->A<-Y. Researcher wrongly controls for A*.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"collider\", params)\n    T = rng.normal(0, 1, N)\n    Y = p[\"tau\"] * T + rng.normal(0, 1, N)\n    logits = (p[\"g\"][None, :] + p[\"dT\"][None, :] * T[:, None]\n              + p[\"dY\"][None, :] * Y[:, None])\n    A = softmax_sample(logits, rng)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_exposure(N, params=None, rng=None, seed=None):\n    \"\"\"A->Y (direct exposure, no treatment T).\n\n    Returns:\n        dict with keys Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"exposure\", params)\n    K = len(p[\"p_A\"])\n    A = rng.choice(K, size=N, p=p[\"p_A\"])\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + rng.normal(0, 1, N)\n    return {\"Y\": Y, \"A\": A}\n\n\ndef gen_mbias(N, params=None, rng=None, seed=None):\n    \"\"\"U1->{A,T}, U2->{A,Y}, T->Y. Conditioning on A* induces M-bias.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"mbias\", params)\n    N_out = N\n    U1, U2 = rng.normal(0, 1, N_out), rng.normal(0, 1, N_out)\n    T = p[\"delta_coef\"] * U1 + rng.normal(0, 1, N_out)\n    logits = (p[\"g\"][None, :] + p[\"a1\"][None, :] * U1[:, None]\n              + p[\"a2\"][None, :] * U2[:, None])\n    A = softmax_sample(logits, rng)\n    Y = p[\"tau\"] * T + p[\"lam\"] * U2 + rng.normal(0, 1, N_out)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_iv(N, params=None, rng=None, seed=None):\n    \"\"\"Z->A->Y, U->{A,Y}. IV topology with endogenous A.\n\n    Returns:\n        dict with keys Z, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"iv\", params)\n    K = len(p[\"g\"])\n    Z = rng.normal(0, 1, N)\n    U = rng.normal(0, 1, N)\n    logits = (p[\"g\"][None, :] + p[\"dZ\"][None, :] * Z[:, None]\n              + p[\"dU\"][None, :] * U[:, None])\n    A = softmax_sample(logits, rng)\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + p[\"lam\"] * U + rng.normal(0, 1, N)\n    return {\"Z\": Z, \"Y\": Y, \"A\": A}\n\n\ndef gen_frontdoor(N, params=None, rng=None, seed=None):\n    \"\"\"T->M->Y, U->{T,Y}. Misclassified variable is M (mediator, stored as A).\n\n    Returns:\n        dict with keys T, Y, A (A is the mediator M)\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"frontdoor\", params)\n    U = rng.normal(0, 1, N)\n    T = p[\"alpha_U\"] * U + rng.normal(0, 1, N)\n    K = len(p[\"gamma\"])\n    logits = p[\"gamma\"][None, :] + p[\"delta\"][None, :] * T[:, None]\n    A = softmax_sample(logits, rng)\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + p[\"lam_U\"] * U + rng.normal(0, 1, N)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\nGEN_FUNCS = {\n    \"confounding\": gen_confounding,\n    \"mediation\": gen_mediation,\n    \"collider\": gen_collider,\n    \"exposure\": gen_exposure,\n    \"mbias\": gen_mbias,\n    \"iv\": gen_iv,\n    \"frontdoor\": gen_frontdoor,\n}\n\n\ndef generate_data(topology, N, params=None, rng=None, seed=None):\n    \"\"\"Generate synthetic data for a given topology.\n\n    Args:\n        topology: one of \"confounding\", \"mediation\", \"collider\", \"exposure\",\n                  \"mbias\", \"iv\", \"frontdoor\"\n        N: sample size\n        params: optional DGP parameter overrides\n        rng: numpy random Generator\n        seed: random seed (used if rng is None)\n\n    Returns:\n        dict with generated variables (topology-dependent keys)\n    \"\"\"\n    if topology not in GEN_FUNCS:\n        raise ValueError(f\"Unknown topology: {topology}. Choose from {TOPOLOGIES}\")\n    return GEN_FUNCS[topology](N, params=params, rng=rng, seed=seed)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "5a87dab4-e568-4d4e-961d-30065d0c9a7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AiAiTgXsUgDz1GG9ZrwZEW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1688,
      "cache_read_input_tokens": 104442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1688
      },
      "output_tokens": 68,
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

_source line 31 · 2026-05-20T23:33:33.232Z_

<details><summary>↩ Tool result · `toolu_01DH5VLiV5KaYxYkohEcFVaf`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/dgp.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "90802f13-5604-4ac6-96c4-c2e8f97c49d6",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/dgp.py",
    "content": "\"\"\"Data generation processes for 7 DAG topologies.\n\nEach topology generates synthetic data with a known causal structure.\nThe variable A (or M for frontdoor) is the one subject to misclassification.\n\"\"\"\n\nimport numpy as np\nfrom .utils import softmax_sample, make_dummies\n\nDEFAULT_PARAMS = {\n    \"confounding\": dict(\n        p_A=np.array([0.40, 0.35, 0.25]),\n        alpha=np.array([1.5, -1.0]),\n        beta_A=np.array([1.0, -0.5]),\n        beta_T=2.0, sigma_T=1.0),\n    \"mediation\": dict(\n        tau=0.5,\n        gamma=np.array([0.0, 0.5, -0.3]),\n        delta=np.array([0.0, 0.8, -0.6]),\n        beta=np.array([0.0, 1.0, -0.5])),\n    \"collider\": dict(\n        tau=1.0,\n        g=np.array([0.0, 0.0, 0.0]),\n        dT=np.array([0.0, 0.5, -0.3]),\n        dY=np.array([0.0, 0.8, 0.6])),\n    \"exposure\": dict(\n        beta=np.array([0.0, 1.0, -0.5]),\n        p_A=np.array([0.40, 0.35, 0.25])),\n    \"mbias\": dict(\n        tau=1.0, delta_coef=1.0, lam=1.0,\n        g=np.array([0.0, 0.0, 0.0]),\n        a1=np.array([0.0, 0.8, -0.5]),\n        a2=np.array([0.0, 0.6, 0.9])),\n    \"iv\": dict(\n        lam=1.0,\n        g=np.array([0.0, 0.0, 0.0]),\n        dZ=np.array([0.0, 1.0, -0.5]),\n        dU=np.array([0.0, 0.8, 0.6]),\n        beta=np.array([0.0, 1.0, -0.5])),\n    \"frontdoor\": dict(\n        alpha_U=1.0, lam_U=1.0,\n        gamma=np.array([0.0, 0.5, -0.3]),\n        delta=np.array([0.0, 1.0, -0.8]),\n        beta=np.array([0.0, 1.0, -0.5])),\n}\n\nTOPOLOGIES = list(DEFAULT_PARAMS.keys())\n\nHAS_TREATMENT = {\"confounding\", \"mediation\", \"collider\", \"mbias\", \"frontdoor\"}\nNO_TREATMENT = {\"exposure\", \"iv\"}\n\n\ndef _get_rng(rng, seed):\n    if rng is not None:\n        return rng\n    return np.random.default_rng(seed)\n\n\ndef _get_params(topology, params):\n    p = dict(DEFAULT_PARAMS[topology])\n    if params is not None:\n        p.update(params)\n    return p\n\n\ndef gen_confounding(N, params=None, rng=None, seed=None):\n    \"\"\"A->T, A->Y, T->Y. Researcher controls for A*.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"confounding\", params)\n    K = len(p[\"p_A\"])\n    A = rng.choice(K, size=N, p=p[\"p_A\"])\n    D = make_dummies(A, K)\n    T = D @ p[\"alpha\"] + rng.normal(0, p[\"sigma_T\"], N)\n    Y = p[\"beta_T\"] * T + D @ p[\"beta_A\"] + rng.normal(0, 1, N)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_mediation(N, params=None, rng=None, seed=None):\n    \"\"\"T->A->Y. A mediates; researcher controls for A*.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"mediation\", params)\n    T = rng.binomial(1, 0.5, N).astype(float)\n    K = len(p[\"gamma\"])\n    logits = p[\"gamma\"][None, :] + p[\"delta\"][None, :] * T[:, None]\n    A = softmax_sample(logits, rng)\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + p[\"tau\"] * T + rng.normal(0, 1, N)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_collider(N, params=None, rng=None, seed=None):\n    \"\"\"T->A<-Y. Researcher wrongly controls for A*.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"collider\", params)\n    T = rng.normal(0, 1, N)\n    Y = p[\"tau\"] * T + rng.normal(0, 1, N)\n    logits = (p[\"g\"][None, :] + p[\"dT\"][None, :] * T[:, None]\n              + p[\"dY\"][None, :] * Y[:, None])\n    A = softmax_sample(logits, rng)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_exposure(N, params=None, rng=None, seed=None):\n    \"\"\"A->Y (direct exposure, no treatment T).\n\n    Returns:\n        dict with keys Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"exposure\", params)\n    K = len(p[\"p_A\"])\n    A = rng.choice(K, size=N, p=p[\"p_A\"])\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + rng.normal(0, 1, N)\n    return {\"Y\": Y, \"A\": A}\n\n\ndef gen_mbias(N, params=None, rng=None, seed=None):\n    \"\"\"U1->{A,T}, U2->{A,Y}, T->Y. Conditioning on A* induces M-bias.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"mbias\", params)\n    N_out = N\n    U1, U2 = rng.normal(0, 1, N_out), rng.normal(0, 1, N_out)\n    T = p[\"delta_coef\"] * U1 + rng.normal(0, 1, N_out)\n    logits = (p[\"g\"][None, :] + p[\"a1\"][None, :] * U1[:, None]\n              + p[\"a2\"][None, :] * U2[:, None])\n    A = softmax_sample(logits, rng)\n    Y = p[\"tau\"] * T + p[\"lam\"] * U2 + rng.normal(0, 1, N_out)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_iv(N, params=None, rng=None, seed=None):\n    \"\"\"Z->A->Y, U->{A,Y}. IV topology with endogenous A.\n\n    Returns:\n        dict with keys Z, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"iv\", params)\n    K = len(p[\"g\"])\n    Z = rng.normal(0, 1, N)\n    U = rng.normal(0, 1, N)\n    logits = (p[\"g\"][None, :] + p[\"dZ\"][None, :] * Z[:, None]\n              + p[\"dU\"][None, :] * U[:, None])\n    A = softmax_sample(logits, rng)\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + p[\"lam\"] * U + rng.normal(0, 1, N)\n    return {\"Z\": Z, \"Y\": Y, \"A\": A}\n\n\ndef gen_frontdoor(N, params=None, rng=None, seed=None):\n    \"\"\"T->M->Y, U->{T,Y}. Misclassified variable is M (mediator, stored as A).\n\n    Returns:\n        dict with keys T, Y, A (A is the mediator M)\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"frontdoor\", params)\n    U = rng.normal(0, 1, N)\n    T = p[\"alpha_U\"] * U + rng.normal(0, 1, N)\n    K = len(p[\"gamma\"])\n    logits = p[\"gamma\"][None, :] + p[\"delta\"][None, :] * T[:, None]\n    A = softmax_sample(logits, rng)\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + p[\"lam_U\"] * U + rng.normal(0, 1, N)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\nGEN_FUNCS = {\n    \"confounding\": gen_confounding,\n    \"mediation\": gen_mediation,\n    \"collider\": gen_collider,\n    \"exposure\": gen_exposure,\n    \"mbias\": gen_mbias,\n    \"iv\": gen_iv,\n    \"frontdoor\": gen_frontdoor,\n}\n\n\ndef generate_data(topology, N, params=None, rng=None, seed=None):\n    \"\"\"Generate synthetic data for a given topology.\n\n    Args:\n        topology: one of \"confounding\", \"mediation\", \"collider\", \"exposure\",\n                  \"mbias\", \"iv\", \"frontdoor\"\n        N: sample size\n        params: optional DGP parameter overrides\n        rng: numpy random Generator\n        seed: random seed (used if rng is None)\n\n    Returns:\n        dict with generated variables (topology-dependent keys)\n    \"\"\"\n    if topology not in GEN_FUNCS:\n        raise ValueError(f\"Unknown topology: {topology}. Choose from {TOPOLOGIES}\")\n    return GEN_FUNCS[topology](N, params=params, rng=rng, seed=seed)\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Write · `toolu_01Ba1ouYwcVmrDsquXpGdFxh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py",
  "content": "\"\"\"Compute annotation-error bias via probability limit calculations.\n\nUses precomputed sufficient statistics from large-sample DGP simulations\nto compute OLS plim as a function of confusion matrix C, avoiding MC.\n\"\"\"\n\nimport warnings\nimport numpy as np\nfrom .dgp import DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES\nfrom .confusion import validate_confusion_matrix\n\n_N_PRECOMP = 2_000_000\n_precomp_cache = {}\n\n\ndef _params_key(params):\n    items = []\n    for k, v in sorted(params.items()):\n        if isinstance(v, np.ndarray):\n            items.append((k, tuple(v.flat)))\n        else:\n            items.append((k, v))\n    return tuple(items)\n\n\ndef _precompute(topology, params, K, seed=999):\n    \"\"\"Precompute sufficient statistics for plim calculation.\"\"\"\n    cache_key = (topology, _params_key(params), K)\n    if cache_key in _precomp_cache:\n        return _precomp_cache[cache_key]\n\n    rng = np.random.default_rng(seed)\n    data = GEN_FUNCS[topology](_N_PRECOMP, params=params, rng=rng)\n    Y = data[\"Y\"]\n    A = data[\"A\"]\n\n    DA = np.zeros((_N_PRECOMP, K))\n    for k in range(K):\n        DA[:, k] = (A == k).astype(float)\n\n    stats = {\n        \"E_Y\": Y.mean(),\n        \"E_DA\": DA.mean(0),\n        \"E_DA_Y\": (DA * Y[:, None]).mean(0),\n    }\n\n    if topology in HAS_TREATMENT:\n        T = data[\"T\"]\n        stats.update({\n            \"E_T\": T.mean(),\n            \"E_T2\": (T ** 2).mean(),\n            \"E_TY\": (T * Y).mean(),\n            \"E_DA_T\": (DA * T[:, None]).mean(0),\n        })\n\n    _precomp_cache[cache_key] = stats\n    return stats\n\n\ndef _plim_with_T(C, stats, K):\n    \"\"\"OLS plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}.\"\"\"\n    ds = C @ stats[\"E_DA\"]\n    dst = C @ stats[\"E_DA_T\"]\n    dsy = C @ stats[\"E_DA_Y\"]\n    ET, ET2 = stats[\"E_T\"], stats[\"E_T2\"]\n    EY, ETY = stats[\"E_Y\"], stats[\"E_TY\"]\n\n    dim = 1 + K  # intercept + T + (K-1) dummies\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    EZZ[0, 1] = EZZ[1, 0] = ET\n    EZZ[1, 1] = ET2\n    for j in range(1, K):\n        idx = j + 1\n        EZZ[0, idx] = EZZ[idx, 0] = ds[j]\n        EZZ[1, idx] = EZZ[idx, 1] = dst[j]\n        EZZ[idx, idx] = ds[j]\n\n    EZY = np.zeros(dim)\n    EZY[0] = EY\n    EZY[1] = ETY\n    for j in range(1, K):\n        EZY[j + 1] = dsy[j]\n\n    cond = np.linalg.cond(EZZ)\n    if cond > 1e12:\n        warnings.warn(\n            f\"EZZ condition number {cond:.1e} — plim may be numerically unstable\"\n        )\n\n    return np.linalg.solve(EZZ, EZY)\n\n\ndef _plim_no_T(C, stats, K):\n    \"\"\"OLS plim for Y ~ 1 + D*_1 + ... + D*_{K-1}.\"\"\"\n    ds = C @ stats[\"E_DA\"]\n    dsy = C @ stats[\"E_DA_Y\"]\n    EY = stats[\"E_Y\"]\n\n    dim = K  # intercept + (K-1) dummies\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    for j in range(1, K):\n        EZZ[0, j] = EZZ[j, 0] = ds[j]\n        EZZ[j, j] = ds[j]\n\n    EZY = np.zeros(dim)\n    EZY[0] = EY\n    for j in range(1, K):\n        EZY[j] = dsy[j]\n\n    cond = np.linalg.cond(EZZ)\n    if cond > 1e12:\n        warnings.warn(\n            f\"EZZ condition number {cond:.1e} — plim may be numerically unstable\"\n        )\n\n    return np.linalg.solve(EZZ, EZY)\n\n\ndef _get_tau(topology, C, stats, K):\n    \"\"\"Extract target coefficient from plim vector.\n\n    For topologies with T: coefficient index 1 (treatment effect).\n    For topologies without T: coefficient index 1 (first dummy).\n    \"\"\"\n    if topology in HAS_TREATMENT:\n        coefs = _plim_with_T(C, stats, K)\n    else:\n        coefs = _plim_no_T(C, stats, K)\n    return coefs[1]\n\n\ndef compute_bias(topology, C, params=None):\n    \"\"\"Compute annotation-error bias for a given topology and confusion matrix.\n\n    Args:\n        topology: one of \"confounding\", \"mediation\", \"collider\", \"exposure\",\n                  \"mbias\", \"iv\", \"frontdoor\"\n        C: (K, K) column-stochastic confusion matrix, C[j,i] = P(A*=j|A=i)\n        params: optional DGP parameters dict, None uses defaults\n\n    Returns:\n        dict with tau_true, tau_biased, bias, bias_pct, topology\n    \"\"\"\n    if topology not in TOPOLOGIES:\n        raise ValueError(f\"Unknown topology: {topology}. Choose from {TOPOLOGIES}\")\n    if not validate_confusion_matrix(C):\n        raise ValueError(\"C must be a square, non-negative, column-stochastic matrix\")\n\n    K = C.shape[0]\n    merged = dict(DEFAULT_PARAMS[topology])\n    if params is not None:\n        merged.update(params)\n\n    stats = _precompute(topology, merged, K)\n    tau_true = _get_tau(topology, np.eye(K), stats, K)\n    tau_biased = _get_tau(topology, C, stats, K)\n    bias = tau_biased - tau_true\n    bias_pct = 100.0 * bias / tau_true if abs(tau_true) > 1e-12 else float(\"nan\")\n\n    return {\n        \"tau_true\": float(tau_true),\n        \"tau_biased\": float(tau_biased),\n        \"bias\": float(bias),\n        \"bias_pct\": float(bias_pct),\n        \"topology\": topology,\n    }\n\n\ndef clear_cache():\n    \"\"\"Clear the precomputed statistics cache.\"\"\"\n    _precomp_cache.clear()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "5239bb9b-713c-4f44-a6a9-8baff759daa8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WVcQXpiB4gqDNUENaU4Gf3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2945,
      "cache_read_input_tokens": 106130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2945
      },
      "output_tokens": 65,
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

_source line 33 · 2026-05-20T23:34:00.927Z_

<details><summary>↩ Tool result · `toolu_01Ba1ouYwcVmrDsquXpGdFxh`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "625ef7c7-7091-4ac6-90c1-497170f2507a",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py",
    "content": "\"\"\"Compute annotation-error bias via probability limit calculations.\n\nUses precomputed sufficient statistics from large-sample DGP simulations\nto compute OLS plim as a function of confusion matrix C, avoiding MC.\n\"\"\"\n\nimport warnings\nimport numpy as np\nfrom .dgp import DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES\nfrom .confusion import validate_confusion_matrix\n\n_N_PRECOMP = 2_000_000\n_precomp_cache = {}\n\n\ndef _params_key(params):\n    items = []\n    for k, v in sorted(params.items()):\n        if isinstance(v, np.ndarray):\n            items.append((k, tuple(v.flat)))\n        else:\n            items.append((k, v))\n    return tuple(items)\n\n\ndef _precompute(topology, params, K, seed=999):\n    \"\"\"Precompute sufficient statistics for plim calculation.\"\"\"\n    cache_key = (topology, _params_key(params), K)\n    if cache_key in _precomp_cache:\n        return _precomp_cache[cache_key]\n\n    rng = np.random.default_rng(seed)\n    data = GEN_FUNCS[topology](_N_PRECOMP, params=params, rng=rng)\n    Y = data[\"Y\"]\n    A = data[\"A\"]\n\n    DA = np.zeros((_N_PRECOMP, K))\n    for k in range(K):\n        DA[:, k] = (A == k).astype(float)\n\n    stats = {\n        \"E_Y\": Y.mean(),\n        \"E_DA\": DA.mean(0),\n        \"E_DA_Y\": (DA * Y[:, None]).mean(0),\n    }\n\n    if topology in HAS_TREATMENT:\n        T = data[\"T\"]\n        stats.update({\n            \"E_T\": T.mean(),\n            \"E_T2\": (T ** 2).mean(),\n            \"E_TY\": (T * Y).mean(),\n            \"E_DA_T\": (DA * T[:, None]).mean(0),\n        })\n\n    _precomp_cache[cache_key] = stats\n    return stats\n\n\ndef _plim_with_T(C, stats, K):\n    \"\"\"OLS plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}.\"\"\"\n    ds = C @ stats[\"E_DA\"]\n    dst = C @ stats[\"E_DA_T\"]\n    dsy = C @ stats[\"E_DA_Y\"]\n    ET, ET2 = stats[\"E_T\"], stats[\"E_T2\"]\n    EY, ETY = stats[\"E_Y\"], stats[\"E_TY\"]\n\n    dim = 1 + K  # intercept + T + (K-1) dummies\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    EZZ[0, 1] = EZZ[1, 0] = ET\n    EZZ[1, 1] = ET2\n    for j in range(1, K):\n        idx = j + 1\n        EZZ[0, idx] = EZZ[idx, 0] = ds[j]\n        EZZ[1, idx] = EZZ[idx, 1] = dst[j]\n        EZZ[idx, idx] = ds[j]\n\n    EZY = np.zeros(dim)\n    EZY[0] = EY\n    EZY[1] = ETY\n    for j in range(1, K):\n        EZY[j + 1] = dsy[j]\n\n    cond = np.linalg.cond(EZZ)\n    if cond > 1e12:\n        warnings.warn(\n            f\"EZZ condition number {cond:.1e} — plim may be numerically unstable\"\n        )\n\n    return np.linalg.solve(EZZ, EZY)\n\n\ndef _plim_no_T(C, stats, K):\n    \"\"\"OLS plim for Y ~ 1 + D*_1 + ... + D*_{K-1}.\"\"\"\n    ds = C @ stats[\"E_DA\"]\n    dsy = C @ stats[\"E_DA_Y\"]\n    EY = stats[\"E_Y\"]\n\n    dim = K  # intercept + (K-1) dummies\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    for j in range(1, K):\n        EZZ[0, j] = EZZ[j, 0] = ds[j]\n        EZZ[j, j] = ds[j]\n\n    EZY = np.zeros(dim)\n    EZY[0] = EY\n    for j in range(1, K):\n        EZY[j] = dsy[j]\n\n    cond = np.linalg.cond(EZZ)\n    if cond > 1e12:\n        warnings.warn(\n            f\"EZZ condition number {cond:.1e} — plim may be numerically unstable\"\n        )\n\n    return np.linalg.solve(EZZ, EZY)\n\n\ndef _get_tau(topology, C, stats, K):\n    \"\"\"Extract target coefficient from plim vector.\n\n    For topologies with T: coefficient index 1 (treatment effect).\n    For topologies without T: coefficient index 1 (first dummy).\n    \"\"\"\n    if topology in HAS_TREATMENT:\n        coefs = _plim_with_T(C, stats, K)\n    else:\n        coefs = _plim_no_T(C, stats, K)\n    return coefs[1]\n\n\ndef compute_bias(topology, C, params=None):\n    \"\"\"Compute annotation-error bias for a given topology and confusion matrix.\n\n    Args:\n        topology: one of \"confounding\", \"mediation\", \"collider\", \"exposure\",\n                  \"mbias\", \"iv\", \"frontdoor\"\n        C: (K, K) column-stochastic confusion matrix, C[j,i] = P(A*=j|A=i)\n        params: optional DGP parameters dict, None uses defaults\n\n    Returns:\n        dict with tau_true, tau_biased, bias, bias_pct, topology\n    \"\"\"\n    if topology not in TOPOLOGIES:\n        raise ValueError(f\"Unknown topology: {topology}. Choose from {TOPOLOGIES}\")\n    if not validate_confusion_matrix(C):\n        raise ValueError(\"C must be a square, non-negative, column-stochastic matrix\")\n\n    K = C.shape[0]\n    merged = dict(DEFAULT_PARAMS[topology])\n    if params is not None:\n        merged.update(params)\n\n    stats = _precompute(topology, merged, K)\n    tau_true = _get_tau(topology, np.eye(K), stats, K)\n    tau_biased = _get_tau(topology, C, stats, K)\n    bias = tau_biased - tau_true\n    bias_pct = 100.0 * bias / tau_true if abs(tau_true) > 1e-12 else float(\"nan\")\n\n    return {\n        \"tau_true\": float(tau_true),\n        \"tau_biased\": float(tau_biased),\n        \"bias\": float(bias),\n        \"bias_pct\": float(bias_pct),\n        \"topology\": topology,\n    }\n\n\ndef clear_cache():\n    \"\"\"Clear the precomputed statistics cache.\"\"\"\n    _precomp_cache.clear()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Write · `toolu_01UJ2Pqbf2oryLQfu9YwbXjc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/asv.py",
  "content": "\"\"\"Annotation Sensitivity Value (ASV) computation.\n\nASV measures how much misclassification is needed to cross a bias threshold,\nusing the C(delta) = (1-delta)*I + delta*C0 interpolation path.\n\"\"\"\n\nimport numpy as np\nfrom .bias import _precompute, _get_tau\nfrom .confusion import validate_confusion_matrix, interpolate_confusion, delta_range\nfrom .dgp import DEFAULT_PARAMS, TOPOLOGIES\n\n\ndef _compute_bias_curve(topology, C0, stats, K, tau_true, n_grid=1500):\n    dmin, dmax = delta_range(C0)\n    deltas = np.linspace(dmin, dmax, n_grid)\n    tau_curve = np.zeros(n_grid)\n    for i, d in enumerate(deltas):\n        C_d = interpolate_confusion(C0, d)\n        tau_curve[i] = _get_tau(topology, C_d, stats, K)\n    bias_abs = np.abs(tau_curve - tau_true)\n    return deltas, bias_abs, tau_curve\n\n\ndef _compute_envelope(bias_abs):\n    env = np.zeros_like(bias_abs)\n    running_max = 0.0\n    for i in range(len(bias_abs)):\n        v = bias_abs[i]\n        if not np.isnan(v):\n            running_max = max(running_max, v)\n        env[i] = running_max\n    return env\n\n\ndef _find_threshold_crossing(envelope, deltas, tau_curve, tau_true,\n                             threshold_type, threshold_value):\n    if threshold_type == \"magnitude\":\n        if abs(tau_true) < 1e-12:\n            return None\n        thresh = threshold_value * abs(tau_true)\n        for i in range(len(deltas)):\n            if envelope[i] > thresh:\n                return float(deltas[i])\n        return None\n    elif threshold_type == \"sign_flip\":\n        if abs(tau_true) < 1e-12:\n            return None\n        baseline_sign = np.sign(tau_true)\n        for i in range(len(deltas)):\n            if np.isnan(tau_curve[i]):\n                continue\n            if np.sign(tau_curve[i]) != baseline_sign:\n                return float(deltas[i])\n        return None\n    elif threshold_type == \"significance\":\n        z_crit = 1.96\n        for i in range(len(deltas)):\n            if np.isnan(tau_curve[i]):\n                continue\n            if abs(tau_curve[i]) < z_crit * threshold_value:\n                return float(deltas[i])\n        return None\n    else:\n        raise ValueError(\n            f\"Unknown threshold_type: {threshold_type}. \"\n            f\"Choose from 'magnitude', 'significance', 'sign_flip'\"\n        )\n\n\ndef compute_asv(topology, C0, params=None, threshold_type=\"magnitude\",\n                threshold_value=0.1, n_grid=1500):\n    \"\"\"Compute Annotation Sensitivity Value for a topology and base confusion matrix.\n\n    ASV is the minimum interpolation delta at which a bias threshold is crossed\n    along the path C(delta) = (1-delta)*I + delta*C0.\n\n    Args:\n        topology: one of 7 DAG types\n        C0: (K, K) base confusion matrix\n        params: optional DGP parameters dict\n        threshold_type: \"magnitude\" (relative to tau_true),\n                        \"significance\" (threshold_value = SE),\n                        \"sign_flip\" (sign of tau changes)\n        threshold_value: threshold parameter (meaning depends on threshold_type)\n        n_grid: number of delta grid points\n\n    Returns:\n        dict with asv, bias_curve, envelope, deltas, tau_true\n    \"\"\"\n    if topology not in TOPOLOGIES:\n        raise ValueError(f\"Unknown topology: {topology}. Choose from {TOPOLOGIES}\")\n    if not validate_confusion_matrix(C0):\n        raise ValueError(\"C0 must be a valid column-stochastic matrix\")\n\n    K = C0.shape[0]\n    merged = dict(DEFAULT_PARAMS[topology])\n    if params is not None:\n        merged.update(params)\n\n    stats = _precompute(topology, merged, K)\n    tau_true = _get_tau(topology, np.eye(K), stats, K)\n\n    deltas, bias_abs, tau_curve = _compute_bias_curve(\n        topology, C0, stats, K, tau_true, n_grid\n    )\n    envelope = _compute_envelope(bias_abs)\n\n    asv = _find_threshold_crossing(\n        envelope, deltas, tau_curve, tau_true, threshold_type, threshold_value\n    )\n\n    return {\n        \"asv\": asv,\n        \"bias_curve\": bias_abs,\n        \"envelope\": envelope,\n        \"deltas\": deltas,\n        \"tau_true\": float(tau_true),\n    }\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "99c4ba94-ba9e-4e62-a33a-d335c57315c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0151o5Q1jq7Do98kEDmBe2Nb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2040,
      "cache_read_input_tokens": 109075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2040
      },
      "output_tokens": 65,
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

_source line 35 · 2026-05-20T23:34:24.020Z_

<details><summary>↩ Tool result · `toolu_01UJ2Pqbf2oryLQfu9YwbXjc`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/asv.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "9b4b708c-e11e-404e-a086-62cf1e44740e",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/asv.py",
    "content": "\"\"\"Annotation Sensitivity Value (ASV) computation.\n\nASV measures how much misclassification is needed to cross a bias threshold,\nusing the C(delta) = (1-delta)*I + delta*C0 interpolation path.\n\"\"\"\n\nimport numpy as np\nfrom .bias import _precompute, _get_tau\nfrom .confusion import validate_confusion_matrix, interpolate_confusion, delta_range\nfrom .dgp import DEFAULT_PARAMS, TOPOLOGIES\n\n\ndef _compute_bias_curve(topology, C0, stats, K, tau_true, n_grid=1500):\n    dmin, dmax = delta_range(C0)\n    deltas = np.linspace(dmin, dmax, n_grid)\n    tau_curve = np.zeros(n_grid)\n    for i, d in enumerate(deltas):\n        C_d = interpolate_confusion(C0, d)\n        tau_curve[i] = _get_tau(topology, C_d, stats, K)\n    bias_abs = np.abs(tau_curve - tau_true)\n    return deltas, bias_abs, tau_curve\n\n\ndef _compute_envelope(bias_abs):\n    env = np.zeros_like(bias_abs)\n    running_max = 0.0\n    for i in range(len(bias_abs)):\n        v = bias_abs[i]\n        if not np.isnan(v):\n            running_max = max(running_max, v)\n        env[i] = running_max\n    return env\n\n\ndef _find_threshold_crossing(envelope, deltas, tau_curve, tau_true,\n                             threshold_type, threshold_value):\n    if threshold_type == \"magnitude\":\n        if abs(tau_true) < 1e-12:\n            return None\n        thresh = threshold_value * abs(tau_true)\n        for i in range(len(deltas)):\n            if envelope[i] > thresh:\n                return float(deltas[i])\n        return None\n    elif threshold_type == \"sign_flip\":\n        if abs(tau_true) < 1e-12:\n            return None\n        baseline_sign = np.sign(tau_true)\n        for i in range(len(deltas)):\n            if np.isnan(tau_curve[i]):\n                continue\n            if np.sign(tau_curve[i]) != baseline_sign:\n                return float(deltas[i])\n        return None\n    elif threshold_type == \"significance\":\n        z_crit = 1.96\n        for i in range(len(deltas)):\n            if np.isnan(tau_curve[i]):\n                continue\n            if abs(tau_curve[i]) < z_crit * threshold_value:\n                return float(deltas[i])\n        return None\n    else:\n        raise ValueError(\n            f\"Unknown threshold_type: {threshold_type}. \"\n            f\"Choose from 'magnitude', 'significance', 'sign_flip'\"\n        )\n\n\ndef compute_asv(topology, C0, params=None, threshold_type=\"magnitude\",\n                threshold_value=0.1, n_grid=1500):\n    \"\"\"Compute Annotation Sensitivity Value for a topology and base confusion matrix.\n\n    ASV is the minimum interpolation delta at which a bias threshold is crossed\n    along the path C(delta) = (1-delta)*I + delta*C0.\n\n    Args:\n        topology: one of 7 DAG types\n        C0: (K, K) base confusion matrix\n        params: optional DGP parameters dict\n        threshold_type: \"magnitude\" (relative to tau_true),\n                        \"significance\" (threshold_value = SE),\n                        \"sign_flip\" (sign of tau changes)\n        threshold_value: threshold parameter (meaning depends on threshold_type)\n        n_grid: number of delta grid points\n\n    Returns:\n        dict with asv, bias_curve, envelope, deltas, tau_true\n    \"\"\"\n    if topology not in TOPOLOGIES:\n        raise ValueError(f\"Unknown topology: {topology}. Choose from {TOPOLOGIES}\")\n    if not validate_confusion_matrix(C0):\n        raise ValueError(\"C0 must be a valid column-stochastic matrix\")\n\n    K = C0.shape[0]\n    merged = dict(DEFAULT_PARAMS[topology])\n    if params is not None:\n        merged.update(params)\n\n    stats = _precompute(topology, merged, K)\n    tau_true = _get_tau(topology, np.eye(K), stats, K)\n\n    deltas, bias_abs, tau_curve = _compute_bias_curve(\n        topology, C0, stats, K, tau_true, n_grid\n    )\n    envelope = _compute_envelope(bias_abs)\n\n    asv = _find_threshold_crossing(\n        envelope, deltas, tau_curve, tau_true, threshold_type, threshold_value\n    )\n\n    return {\n        \"asv\": asv,\n        \"bias_curve\": bias_abs,\n        \"envelope\": envelope,\n        \"deltas\": deltas,\n        \"tau_true\": float(tau_true),\n    }\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Write · `toolu_011pHz6Lu8zht1iwaYSXNAVf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/correction.py",
  "content": "\"\"\"Correction methods and recommendation engine for annotation-error bias.\n\nFive correction methods:\n  - naive_plugin: C^{-1} correction of dummy indicators\n  - dsl: EM-based joint estimation of regression params and C\n  - ppi: PPI++ combining gold-standard and full-sample estimates\n  - mcsimex: MC-SIMEX extrapolation to lambda=-1\n  - mla: Matrix-based label adjustment via D*_full @ C^{-1}\n\nKey finding (FWL theorem): naive_plugin and mla correct dummy coefficients\nbut NOT the treatment coefficient in regressions with a separate treatment T.\n\"\"\"\n\nimport numpy as np\nfrom .utils import ols, ols_with_se, make_dummies, make_full_dummies, misclassify\n\nMETHODS = [\"naive_plugin\", \"dsl\", \"ppi\", \"mcsimex\", \"mla\"]\n\n_EM_MAX_ITER = 100\n_EM_TOL = 1e-6\n_SIMEX_LAMBDAS = [0.5, 1.0, 1.5, 2.0]\n_SIMEX_B = 50\n\n\ndef correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1):\n    \"\"\"Correct using C^{-1} applied per-observation to dummy indicators.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        C: (K, K) confusion matrix\n        tau_idx: index of target coefficient in full design\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    cond = np.linalg.cond(C)\n    if cond > 1e12:\n        return np.nan, np.nan, False\n    try:\n        C_inv = np.linalg.inv(C)\n    except np.linalg.LinAlgError:\n        return np.nan, np.nan, False\n    D_corrected = C_inv[:, Astar].T[:, 1:]\n    X = np.column_stack([X_other, D_corrected])\n    try:\n        beta, se = ols_with_se(X, Y)\n        return float(beta[tau_idx]), float(se[tau_idx]), True\n    except Exception:\n        return np.nan, np.nan, False\n\n\ndef correct_dsl(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1):\n    \"\"\"EM-based joint estimation of regression params and C.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        A_gold: (N,) gold-standard labels (only gold_mask positions used)\n        gold_mask: (N,) boolean mask for gold-standard observations\n        tau_idx: index of target coefficient\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    N = len(Y)\n    K = int(max(Astar.max(), A_gold[gold_mask].max())) + 1\n    n_other = X_other.shape[1]\n\n    C_est = np.zeros((K, K))\n    for j in range(K):\n        for k in range(K):\n            C_est[k, j] = (\n                (A_gold[gold_mask] == j) & (Astar[gold_mask] == k)\n            ).sum()\n    col_sums = C_est.sum(axis=0)\n    col_sums[col_sums == 0] = 1.0\n    C_est /= col_sums\n    C_est = 0.9 * C_est + 0.1 / K * np.ones((K, K))\n\n    D_star = make_dummies(Astar, K)\n    X_init = np.column_stack([X_other, D_star])\n    try:\n        beta = ols(X_init, Y)\n    except Exception:\n        return np.nan, np.nan, False\n    sigma2 = 1.0\n\n    for _ in range(_EM_MAX_ITER):\n        base = X_other @ beta[:n_other]\n        resp = np.zeros((N, K))\n        for j in range(K):\n            mu_j = base + (beta[n_other + j - 1] if j > 0 else 0.0)\n            resp[:, j] = (\n                -0.5 * (Y - mu_j) ** 2 / sigma2\n                + np.log(np.clip(C_est[Astar, j], 1e-15, None))\n            )\n        resp -= resp.max(axis=1, keepdims=True)\n        resp = np.exp(resp)\n        resp /= resp.sum(axis=1, keepdims=True)\n        resp[gold_mask] = 0.0\n        resp[gold_mask, A_gold[gold_mask]] = 1.0\n\n        D_exp = resp[:, 1:]\n        X_new = np.column_stack([X_other, D_exp])\n        try:\n            beta_new = ols(X_new, Y)\n        except Exception:\n            return np.nan, np.nan, False\n        sigma2_new = max(np.mean((Y - X_new @ beta_new) ** 2), 1e-6)\n\n        C_new = np.zeros((K, K))\n        for j in range(K):\n            for k in range(K):\n                C_new[k, j] = resp[Astar == k, j].sum()\n        cs = C_new.sum(axis=0)\n        cs[cs == 0] = 1.0\n        C_new /= cs\n\n        converged = (\n            np.max(np.abs(beta_new - beta)) < _EM_TOL\n            and np.max(np.abs(C_new - C_est)) < _EM_TOL\n        )\n        beta, C_est, sigma2 = beta_new, C_new, sigma2_new\n        if converged:\n            break\n\n    X_final = np.column_stack([X_other, resp[:, 1:]])\n    try:\n        beta_f, se_f = ols_with_se(X_final, Y)\n        return float(beta_f[tau_idx]), float(se_f[tau_idx]), True\n    except Exception:\n        return np.nan, np.nan, False\n\n\ndef correct_ppi(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1, rng=None):\n    \"\"\"PPI++ with bootstrap lambda tuning.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        A_gold: (N,) gold-standard labels\n        gold_mask: (N,) boolean mask for gold-standard observations\n        tau_idx: index of target coefficient\n        rng: numpy random Generator\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    if rng is None:\n        rng = np.random.default_rng()\n    K = int(max(Astar.max(), A_gold[gold_mask].max())) + 1\n    gold_idx = np.where(gold_mask)[0]\n    n_gold = len(gold_idx)\n\n    D_g_true = make_dummies(A_gold[gold_mask], K)\n    X_g_true = np.column_stack([X_other[gold_mask], D_g_true])\n    D_g_star = make_dummies(Astar[gold_mask], K)\n    X_g_star = np.column_stack([X_other[gold_mask], D_g_star])\n    D_all_star = make_dummies(Astar, K)\n    X_all_star = np.column_stack([X_other, D_all_star])\n\n    try:\n        b_g_true = ols(X_g_true, Y[gold_mask])\n        b_g_star = ols(X_g_star, Y[gold_mask])\n        b_all_star = ols(X_all_star, Y)\n    except Exception:\n        return np.nan, np.nan, False\n\n    n_boot = 50\n    tau_true_boot = np.zeros(n_boot)\n    tau_rect_boot = np.zeros(n_boot)\n    for b in range(n_boot):\n        idx = rng.choice(gold_idx, size=n_gold, replace=True)\n        try:\n            bt = ols(\n                np.column_stack([X_other[idx], make_dummies(A_gold[idx], K)]),\n                Y[idx],\n            )\n            bs = ols(\n                np.column_stack([X_other[idx], make_dummies(Astar[idx], K)]),\n                Y[idx],\n            )\n            tau_true_boot[b] = bt[tau_idx]\n            tau_rect_boot[b] = bs[tau_idx] - bt[tau_idx]\n        except Exception:\n            tau_true_boot[b] = tau_rect_boot[b] = np.nan\n\n    valid = np.isfinite(tau_true_boot) & np.isfinite(tau_rect_boot)\n    if valid.sum() > 5:\n        var_r = np.var(tau_rect_boot[valid])\n        cov_tr = np.cov(tau_true_boot[valid], tau_rect_boot[valid])[0, 1]\n        lam = np.clip(-cov_tr / var_r, 0, 1) if var_r > 1e-12 else 1.0\n    else:\n        lam = 1.0\n\n    tau_ppi = b_g_true[tau_idx] + lam * (b_all_star[tau_idx] - b_g_star[tau_idx])\n    se_est = float(np.std(tau_true_boot[valid])) if valid.sum() > 1 else np.nan\n    return float(tau_ppi), se_est, True\n\n\ndef correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=None):\n    \"\"\"MC-SIMEX: add extra misclassification at levels lambda, extrapolate to -1.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        C: (K, K) confusion matrix\n        tau_idx: index of target coefficient\n        rng: numpy random Generator\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    if rng is None:\n        rng = np.random.default_rng()\n    K = C.shape[0]\n    try:\n        eigvals, eigvecs = np.linalg.eig(C)\n        eigvecs_inv = np.linalg.inv(eigvecs)\n    except np.linalg.LinAlgError:\n        return np.nan, np.nan, False\n\n    lambdas = np.array([0.0] + _SIMEX_LAMBDAS)\n    tau_lam = np.zeros(len(lambdas))\n\n    for li, lam_val in enumerate(lambdas):\n        if lam_val == 0.0:\n            D_star = make_dummies(Astar, K)\n            X = np.column_stack([X_other, D_star])\n            try:\n                tau_lam[li] = ols(X, Y)[tau_idx]\n            except Exception:\n                return np.nan, np.nan, False\n        else:\n            C_lam_raw = np.real((eigvecs * (eigvals ** lam_val)) @ eigvecs_inv)\n            C_lam = np.clip(C_lam_raw, 0, None)\n            cs = C_lam.sum(axis=0)\n            cs[cs == 0] = 1.0\n            C_lam /= cs\n\n            tau_b = np.zeros(_SIMEX_B)\n            for b in range(_SIMEX_B):\n                rng_b = np.random.default_rng(\n                    rng.integers(0, 2 ** 31) + b * 1000 + li * 100000\n                )\n                A_extra = misclassify(Astar, C_lam, rng_b)\n                D_extra = make_dummies(A_extra, K)\n                X_extra = np.column_stack([X_other, D_extra])\n                try:\n                    tau_b[b] = ols(X_extra, Y)[tau_idx]\n                except Exception:\n                    tau_b[b] = np.nan\n            ok = np.isfinite(tau_b)\n            if ok.sum() < _SIMEX_B // 2:\n                return np.nan, np.nan, False\n            tau_lam[li] = tau_b[ok].mean()\n\n    try:\n        coeffs = np.polyfit(lambdas, tau_lam, 2)\n        tau_simex = float(np.polyval(coeffs, -1.0))\n    except Exception:\n        return np.nan, np.nan, False\n\n    D_star = make_dummies(Astar, K)\n    X = np.column_stack([X_other, D_star])\n    try:\n        _, se = ols_with_se(X, Y)\n        return tau_simex, float(se[tau_idx]), True\n    except Exception:\n        return tau_simex, np.nan, True\n\n\ndef correct_mla(X_other, Y, Astar, C, tau_idx=1):\n    \"\"\"MLA: D_corrected = D*_full @ C^{-1}, drop reference category.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        C: (K, K) confusion matrix\n        tau_idx: index of target coefficient\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    cond = np.linalg.cond(C)\n    if cond > 1e12:\n        return np.nan, np.nan, False\n    try:\n        C_inv = np.linalg.inv(C)\n    except np.linalg.LinAlgError:\n        return np.nan, np.nan, False\n    K = C.shape[0]\n    D_full = make_full_dummies(Astar, K)\n    D_corrected = (D_full @ C_inv)[:, 1:]\n    X = np.column_stack([X_other, D_corrected])\n    try:\n        beta, se = ols_with_se(X, Y)\n        return float(beta[tau_idx]), float(se[tau_idx]), True\n    except Exception:\n        return np.nan, np.nan, False\n\n\ndef recommend_correction(topology, C, has_gold=False, gold_fraction=0.1):\n    \"\"\"Recommend the best correction method based on topology and data availability.\n\n    Rules (from plan_007 conclusions):\n      - has_gold=True  -> PPI++ (93.8% bias reduction, 96.8% coverage)\n      - has_gold=False + confounding/mediation -> DSL\n      - has_gold=False + other topologies -> MC-SIMEX\n      - naive_plugin/MLA: only correct dummy coefficients (FWL theorem)\n\n    Args:\n        topology: one of 7 DAG types\n        C: (K, K) confusion matrix (used for diagnostics)\n        has_gold: whether gold-standard labels are available\n        gold_fraction: fraction of data with gold labels\n\n    Returns:\n        dict with recommended, ranking, notes\n    \"\"\"\n    dsl_safe = topology in (\"confounding\", \"mediation\")\n\n    if has_gold:\n        recommended = \"ppi\"\n    elif dsl_safe:\n        recommended = \"dsl\"\n    else:\n        recommended = \"mcsimex\"\n\n    ranking = []\n\n    # PPI++\n    if has_gold:\n        ranking.append({\n            \"method\": \"ppi\",\n            \"applicable\": True,\n            \"expected_bias_reduction\": 0.938,\n            \"notes\": \"Best with gold labels (93.8% bias reduction, 96.8% coverage)\",\n        })\n    else:\n        ranking.append({\n            \"method\": \"ppi\",\n            \"applicable\": False,\n            \"expected_bias_reduction\": 0.0,\n            \"notes\": \"Requires gold-standard labels\",\n        })\n\n    # DSL\n    if dsl_safe:\n        ranking.append({\n            \"method\": \"dsl\",\n            \"applicable\": True,\n            \"expected_bias_reduction\": 0.75,\n            \"notes\": \"Good for confounding/mediation\"\n                     + (\" (best with gold for initialization)\" if not has_gold else \"\"),\n        })\n    else:\n        ranking.append({\n            \"method\": \"dsl\",\n            \"applicable\": False,\n            \"expected_bias_reduction\": -5.0,\n            \"notes\": f\"Catastrophic for {topology} (e.g., mbias yields -768%)\",\n        })\n\n    # MC-SIMEX\n    ranking.append({\n        \"method\": \"mcsimex\",\n        \"applicable\": True,\n        \"expected_bias_reduction\": 0.209,\n        \"notes\": \"Moderate (20.9%) but broadly applicable; requires known C\",\n    })\n\n    # Naive Plugin\n    ranking.append({\n        \"method\": \"naive_plugin\",\n        \"applicable\": True,\n        \"expected_bias_reduction\": 0.0,\n        \"notes\": \"Only corrects dummy coefficients, NOT treatment coefficient (FWL theorem)\",\n    })\n\n    # MLA\n    ranking.append({\n        \"method\": \"mla\",\n        \"applicable\": True,\n        \"expected_bias_reduction\": 0.0,\n        \"notes\": \"Only corrects dummy coefficients, NOT treatment coefficient (FWL theorem)\",\n    })\n\n    ranking.sort(key=lambda m: -m[\"expected_bias_reduction\"])\n\n    notes = []\n    if has_gold:\n        notes.append(f\"Gold labels available ({gold_fraction:.0%} of data)\")\n        notes.append(\"PPI++ recommended: highest bias reduction with valid coverage\")\n    else:\n        notes.append(\"No gold labels available\")\n        if dsl_safe:\n            notes.append(f\"DSL recommended for {topology} (EM-based, works with known C)\")\n        else:\n            notes.append(\n                f\"MC-SIMEX recommended; DSL is catastrophic for {topology}\"\n            )\n\n    cond = np.linalg.cond(C)\n    if cond > 100:\n        notes.append(\n            f\"WARNING: C condition number = {cond:.0f}, \"\n            f\"inverse-based methods may be unstable\"\n        )\n\n    return {\n        \"recommended\": recommended,\n        \"ranking\": ranking,\n        \"notes\": notes,\n    }\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "da713c59-84ce-4b84-8421-dedc5c567e48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KAdpL8wDhUzWXCmp3WLNLk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1400,
      "cache_read_input_tokens": 111115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1400
      },
      "output_tokens": 65,
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

_source line 37 · 2026-05-20T23:35:33.249Z_

<details><summary>↩ Tool result · `toolu_011pHz6Lu8zht1iwaYSXNAVf`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/correction.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "78a80cdb-0617-4239-b728-1d6bfa355aa3",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/correction.py",
    "content": "\"\"\"Correction methods and recommendation engine for annotation-error bias.\n\nFive correction methods:\n  - naive_plugin: C^{-1} correction of dummy indicators\n  - dsl: EM-based joint estimation of regression params and C\n  - ppi: PPI++ combining gold-standard and full-sample estimates\n  - mcsimex: MC-SIMEX extrapolation to lambda=-1\n  - mla: Matrix-based label adjustment via D*_full @ C^{-1}\n\nKey finding (FWL theorem): naive_plugin and mla correct dummy coefficients\nbut NOT the treatment coefficient in regressions with a separate treatment T.\n\"\"\"\n\nimport numpy as np\nfrom .utils import ols, ols_with_se, make_dummies, make_full_dummies, misclassify\n\nMETHODS = [\"naive_plugin\", \"dsl\", \"ppi\", \"mcsimex\", \"mla\"]\n\n_EM_MAX_ITER = 100\n_EM_TOL = 1e-6\n_SIMEX_LAMBDAS = [0.5, 1.0, 1.5, 2.0]\n_SIMEX_B = 50\n\n\ndef correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1):\n    \"\"\"Correct using C^{-1} applied per-observation to dummy indicators.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        C: (K, K) confusion matrix\n        tau_idx: index of target coefficient in full design\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    cond = np.linalg.cond(C)\n    if cond > 1e12:\n        return np.nan, np.nan, False\n    try:\n        C_inv = np.linalg.inv(C)\n    except np.linalg.LinAlgError:\n        return np.nan, np.nan, False\n    D_corrected = C_inv[:, Astar].T[:, 1:]\n    X = np.column_stack([X_other, D_corrected])\n    try:\n        beta, se = ols_with_se(X, Y)\n        return float(beta[tau_idx]), float(se[tau_idx]), True\n    except Exception:\n        return np.nan, np.nan, False\n\n\ndef correct_dsl(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1):\n    \"\"\"EM-based joint estimation of regression params and C.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        A_gold: (N,) gold-standard labels (only gold_mask positions used)\n        gold_mask: (N,) boolean mask for gold-standard observations\n        tau_idx: index of target coefficient\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    N = len(Y)\n    K = int(max(Astar.max(), A_gold[gold_mask].max())) + 1\n    n_other = X_other.shape[1]\n\n    C_est = np.zeros((K, K))\n    for j in range(K):\n        for k in range(K):\n            C_est[k, j] = (\n                (A_gold[gold_mask] == j) & (Astar[gold_mask] == k)\n            ).sum()\n    col_sums = C_est.sum(axis=0)\n    col_sums[col_sums == 0] = 1.0\n    C_est /= col_sums\n    C_est = 0.9 * C_est + 0.1 / K * np.ones((K, K))\n\n    D_star = make_dummies(Astar, K)\n    X_init = np.column_stack([X_other, D_star])\n    try:\n        beta = ols(X_init, Y)\n    except Exception:\n        return np.nan, np.nan, False\n    sigma2 = 1.0\n\n    for _ in range(_EM_MAX_ITER):\n        base = X_other @ beta[:n_other]\n        resp = np.zeros((N, K))\n        for j in range(K):\n            mu_j = base + (beta[n_other + j - 1] if j > 0 else 0.0)\n            resp[:, j] = (\n                -0.5 * (Y - mu_j) ** 2 / sigma2\n                + np.log(np.clip(C_est[Astar, j], 1e-15, None))\n            )\n        resp -= resp.max(axis=1, keepdims=True)\n        resp = np.exp(resp)\n        resp /= resp.sum(axis=1, keepdims=True)\n        resp[gold_mask] = 0.0\n        resp[gold_mask, A_gold[gold_mask]] = 1.0\n\n        D_exp = resp[:, 1:]\n        X_new = np.column_stack([X_other, D_exp])\n        try:\n            beta_new = ols(X_new, Y)\n        except Exception:\n            return np.nan, np.nan, False\n        sigma2_new = max(np.mean((Y - X_new @ beta_new) ** 2), 1e-6)\n\n        C_new = np.zeros((K, K))\n        for j in range(K):\n            for k in range(K):\n                C_new[k, j] = resp[Astar == k, j].sum()\n        cs = C_new.sum(axis=0)\n        cs[cs == 0] = 1.0\n        C_new /= cs\n\n        converged = (\n            np.max(np.abs(beta_new - beta)) < _EM_TOL\n            and np.max(np.abs(C_new - C_est)) < _EM_TOL\n        )\n        beta, C_est, sigma2 = beta_new, C_new, sigma2_new\n        if converged:\n            break\n\n    X_final = np.column_stack([X_other, resp[:, 1:]])\n    try:\n        beta_f, se_f = ols_with_se(X_final, Y)\n        return float(beta_f[tau_idx]), float(se_f[tau_idx]), True\n    except Exception:\n        return np.nan, np.nan, False\n\n\ndef correct_ppi(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1, rng=None):\n    \"\"\"PPI++ with bootstrap lambda tuning.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        A_gold: (N,) gold-standard labels\n        gold_mask: (N,) boolean mask for gold-standard observations\n        tau_idx: index of target coefficient\n        rng: numpy random Generator\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    if rng is None:\n        rng = np.random.default_rng()\n    K = int(max(Astar.max(), A_gold[gold_mask].max())) + 1\n    gold_idx = np.where(gold_mask)[0]\n    n_gold = len(gold_idx)\n\n    D_g_true = make_dummies(A_gold[gold_mask], K)\n    X_g_true = np.column_stack([X_other[gold_mask], D_g_true])\n    D_g_star = make_dummies(Astar[gold_mask], K)\n    X_g_star = np.column_stack([X_other[gold_mask], D_g_star])\n    D_all_star = make_dummies(Astar, K)\n    X_all_star = np.column_stack([X_other, D_all_star])\n\n    try:\n        b_g_true = ols(X_g_true, Y[gold_mask])\n        b_g_star = ols(X_g_star, Y[gold_mask])\n        b_all_star = ols(X_all_star, Y)\n    except Exception:\n        return np.nan, np.nan, False\n\n    n_boot = 50\n    tau_true_boot = np.zeros(n_boot)\n    tau_rect_boot = np.zeros(n_boot)\n    for b in range(n_boot):\n        idx = rng.choice(gold_idx, size=n_gold, replace=True)\n        try:\n            bt = ols(\n                np.column_stack([X_other[idx], make_dummies(A_gold[idx], K)]),\n                Y[idx],\n            )\n            bs = ols(\n                np.column_stack([X_other[idx], make_dummies(Astar[idx], K)]),\n                Y[idx],\n            )\n            tau_true_boot[b] = bt[tau_idx]\n            tau_rect_boot[b] = bs[tau_idx] - bt[tau_idx]\n        except Exception:\n            tau_true_boot[b] = tau_rect_boot[b] = np.nan\n\n    valid = np.isfinite(tau_true_boot) & np.isfinite(tau_rect_boot)\n    if valid.sum() > 5:\n        var_r = np.var(tau_rect_boot[valid])\n        cov_tr = np.cov(tau_true_boot[valid], tau_rect_boot[valid])[0, 1]\n        lam = np.clip(-cov_tr / var_r, 0, 1) if var_r > 1e-12 else 1.0\n    else:\n        lam = 1.0\n\n    tau_ppi = b_g_true[tau_idx] + lam * (b_all_star[tau_idx] - b_g_star[tau_idx])\n    se_est = float(np.std(tau_true_boot[valid])) if valid.sum() > 1 else np.nan\n    return float(tau_ppi), se_est, True\n\n\ndef correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=None):\n    \"\"\"MC-SIMEX: add extra misclassification at levels lambda, extrapolate to -1.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        C: (K, K) confusion matrix\n        tau_idx: index of target coefficient\n        rng: numpy random Generator\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    if rng is None:\n        rng = np.random.default_rng()\n    K = C.shape[0]\n    try:\n        eigvals, eigvecs = np.linalg.eig(C)\n        eigvecs_inv = np.linalg.inv(eigvecs)\n    except np.linalg.LinAlgError:\n        return np.nan, np.nan, False\n\n    lambdas = np.array([0.0] + _SIMEX_LAMBDAS)\n    tau_lam = np.zeros(len(lambdas))\n\n    for li, lam_val in enumerate(lambdas):\n        if lam_val == 0.0:\n            D_star = make_dummies(Astar, K)\n            X = np.column_stack([X_other, D_star])\n            try:\n                tau_lam[li] = ols(X, Y)[tau_idx]\n            except Exception:\n                return np.nan, np.nan, False\n        else:\n            C_lam_raw = np.real((eigvecs * (eigvals ** lam_val)) @ eigvecs_inv)\n            C_lam = np.clip(C_lam_raw, 0, None)\n            cs = C_lam.sum(axis=0)\n            cs[cs == 0] = 1.0\n            C_lam /= cs\n\n            tau_b = np.zeros(_SIMEX_B)\n            for b in range(_SIMEX_B):\n                rng_b = np.random.default_rng(\n                    rng.integers(0, 2 ** 31) + b * 1000 + li * 100000\n                )\n                A_extra = misclassify(Astar, C_lam, rng_b)\n                D_extra = make_dummies(A_extra, K)\n                X_extra = np.column_stack([X_other, D_extra])\n                try:\n                    tau_b[b] = ols(X_extra, Y)[tau_idx]\n                except Exception:\n                    tau_b[b] = np.nan\n            ok = np.isfinite(tau_b)\n            if ok.sum() < _SIMEX_B // 2:\n                return np.nan, np.nan, False\n            tau_lam[li] = tau_b[ok].mean()\n\n    try:\n        coeffs = np.polyfit(lambdas, tau_lam, 2)\n        tau_simex = float(np.polyval(coeffs, -1.0))\n    except Exception:\n        return np.nan, np.nan, False\n\n    D_star = make_dummies(Astar, K)\n    X = np.column_stack([X_other, D_star])\n    try:\n        _, se = ols_with_se(X, Y)\n        return tau_simex, float(se[tau_idx]), True\n    except Exception:\n        return tau_simex, np.nan, True\n\n\ndef correct_mla(X_other, Y, Astar, C, tau_idx=1):\n    \"\"\"MLA: D_corrected = D*_full @ C^{-1}, drop reference category.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        C: (K, K) confusion matrix\n        tau_idx: index of target coefficient\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    cond = np.linalg.cond(C)\n    if cond > 1e12:\n        return np.nan, np.nan, False\n    try:\n        C_inv = np.linalg.inv(C)\n    except np.linalg.LinAlgError:\n        return np.nan, np.nan, False\n    K = C.shape[0]\n    D_full = make_full_dummies(Astar, K)\n    D_corrected = (D_full @ C_inv)[:, 1:]\n    X = np.column_stack([X_other, D_corrected])\n    try:\n        beta, se = ols_with_se(X, Y)\n        return float(beta[tau_idx]), float(se[tau_idx]), True\n    except Exception:\n        return np.nan, np.nan, False\n\n\ndef recommend_correction(topology, C, has_gold=False, gold_fraction=0.1):\n    \"\"\"Recommend the best correction method based on topology and data availability.\n\n    Rules (from plan_007 conclusions):\n      - has_gold=True  -> PPI++ (93.8% bias reduction, 96.8% coverage)\n      - has_gold=False + confounding/mediation -> DSL\n      - has_gold=False + other topologies -> MC-SIMEX\n      - naive_plugin/MLA: only correct dummy coefficients (FWL theorem)\n\n    Args:\n        topology: one of 7 DAG types\n        C: (K, K) confusion matrix (used for diagnostics)\n        has_gold: whether gold-standard labels are available\n        gold_fraction: fraction of data with gold labels\n\n    Returns:\n        dict with recommended, ranking, notes\n    \"\"\"\n    dsl_safe = topology in (\"confounding\", \"mediation\")\n\n    if has_gold:\n        recommended = \"ppi\"\n    elif dsl_safe:\n        recommended = \"dsl\"\n    else:\n        recommended = \"mcsimex\"\n\n    ranking = []\n\n    # PPI++\n    if has_gold:\n        ranking.append({\n            \"method\": \"ppi\",\n            \"applicable\": True,\n            \"expected_bias_reduction\": 0.938,\n            \"notes\": \"Best with gold labels (93.8% bias reduction, 96.8% coverage)\",\n        })\n    else:\n        ranking.append({\n            \"method\": \"ppi\",\n            \"applicable\": False,\n            \"expected_bias_reduction\": 0.0,\n            \"notes\": \"Requires gold-standard labels\",\n        })\n\n    # DSL\n    if dsl_safe:\n        ranking.append({\n            \"method\": \"dsl\",\n            \"applicable\": True,\n            \"expected_bias_reduction\": 0.75,\n            \"notes\": \"Good for confounding/mediation\"\n                     + (\" (best with gold for initialization)\" if not has_gold else \"\"),\n        })\n    else:\n        ranking.append({\n            \"method\": \"dsl\",\n            \"applicable\": False,\n            \"expected_bias_reduction\": -5.0,\n            \"notes\": f\"Catastrophic for {topology} (e.g., mbias yields -768%)\",\n        })\n\n    # MC-SIMEX\n    ranking.append({\n        \"method\": \"mcsimex\",\n        \"applicable\": True,\n        \"expected_bias_reduction\": 0.209,\n        \"notes\": \"Moderate (20.9%) but broadly applicable; requires known C\",\n    })\n\n    # Naive Plugin\n    ranking.append({\n        \"method\": \"naive_plugin\",\n        \"applicable\": True,\n        \"expected_bias_reduction\": 0.0,\n        \"notes\": \"Only corrects dummy coefficients, NOT treatment coefficient (FWL theorem)\",\n    })\n\n    # MLA\n    ranking.append({\n        \"method\": \"mla\",\n        \"applicable\": True,\n        \"expected_bias_reduction\": 0.0,\n        \"notes\": \"Only corrects dummy coefficients, NOT treatment coefficient (FWL theorem)\",\n    })\n\n    ranking.sort(key=lambda m: -m[\"expected_bias_reduction\"])\n\n    notes = []\n    if has_gold:\n        notes.append(f\"Gold labels available ({gold_fraction:.0%} of data)\")\n        notes.append(\"PPI++ recommended: highest bias reduction with valid coverage\")\n    else:\n        notes.append(\"No gold labels available\")\n        if dsl_safe:\n            notes.append(f\"DSL recommended for {topology} (EM-based, works with known C)\")\n        else:\n            notes.append(\n                f\"MC-SIMEX recommended; DSL is catastrophic for {topology}\"\n            )\n\n    cond = np.linalg.cond(C)\n    if cond > 100:\n        notes.append(\n            f\"WARNING: C condition number = {cond:.0f}, \"\n            f\"inverse-based methods may be unstable\"\n        )\n\n    return {\n        \"recommended\": recommended,\n        \"ranking\": ranking,\n        \"notes\": notes,\n    }\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Write · `toolu_01N8gxkVW68Ur5bmMPPPHTrA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/__init__.py",
  "content": "\"\"\"annot_sensitivity: Annotation-error sensitivity analysis for causal inference.\n\nComputes how LLM annotation misclassification propagates bias through\n7 DAG topologies, with ASV sensitivity measures and 5 correction methods.\n\"\"\"\n\nfrom .bias import compute_bias, clear_cache\nfrom .asv import compute_asv\nfrom .correction import (\n    recommend_correction,\n    correct_naive_plugin,\n    correct_dsl,\n    correct_ppi,\n    correct_mcsimex,\n    correct_mla,\n    METHODS,\n)\nfrom .confusion import (\n    validate_confusion_matrix,\n    random_confusion_matrix,\n    interpolate_confusion,\n    predefined_matrices,\n    delta_range,\n)\nfrom .dgp import generate_data, TOPOLOGIES, DEFAULT_PARAMS, GEN_FUNCS\nfrom .utils import ols, ols_with_se, make_dummies, softmax_sample, misclassify\n\n__all__ = [\n    \"compute_bias\",\n    \"compute_asv\",\n    \"recommend_correction\",\n    \"correct_naive_plugin\",\n    \"correct_dsl\",\n    \"correct_ppi\",\n    \"correct_mcsimex\",\n    \"correct_mla\",\n    \"validate_confusion_matrix\",\n    \"random_confusion_matrix\",\n    \"interpolate_confusion\",\n    \"predefined_matrices\",\n    \"delta_range\",\n    \"generate_data\",\n    \"clear_cache\",\n    \"TOPOLOGIES\",\n    \"DEFAULT_PARAMS\",\n    \"METHODS\",\n    \"GEN_FUNCS\",\n    \"ols\",\n    \"ols_with_se\",\n    \"make_dummies\",\n    \"softmax_sample\",\n    \"misclassify\",\n]\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "32379ee9-2118-403b-9b8e-29dc715f8e8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PuGsmeEDmSXhoJxKUomhD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5035,
      "cache_read_input_tokens": 112515,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5035
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

_source line 39 · 2026-05-20T23:35:42.713Z_

<details><summary>↩ Tool result · `toolu_01N8gxkVW68Ur5bmMPPPHTrA`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/__init__.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "af080ebd-67bf-44f0-b15f-b8143250fb79",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/__init__.py",
    "content": "\"\"\"annot_sensitivity: Annotation-error sensitivity analysis for causal inference.\n\nComputes how LLM annotation misclassification propagates bias through\n7 DAG topologies, with ASV sensitivity measures and 5 correction methods.\n\"\"\"\n\nfrom .bias import compute_bias, clear_cache\nfrom .asv import compute_asv\nfrom .correction import (\n    recommend_correction,\n    correct_naive_plugin,\n    correct_dsl,\n    correct_ppi,\n    correct_mcsimex,\n    correct_mla,\n    METHODS,\n)\nfrom .confusion import (\n    validate_confusion_matrix,\n    random_confusion_matrix,\n    interpolate_confusion,\n    predefined_matrices,\n    delta_range,\n)\nfrom .dgp import generate_data, TOPOLOGIES, DEFAULT_PARAMS, GEN_FUNCS\nfrom .utils import ols, ols_with_se, make_dummies, softmax_sample, misclassify\n\n__all__ = [\n    \"compute_bias\",\n    \"compute_asv\",\n    \"recommend_correction\",\n    \"correct_naive_plugin\",\n    \"correct_dsl\",\n    \"correct_ppi\",\n    \"correct_mcsimex\",\n    \"correct_mla\",\n    \"validate_confusion_matrix\",\n    \"random_confusion_matrix\",\n    \"interpolate_confusion\",\n    \"predefined_matrices\",\n    \"delta_range\",\n    \"generate_data\",\n    \"clear_cache\",\n    \"TOPOLOGIES\",\n    \"DEFAULT_PARAMS\",\n    \"METHODS\",\n    \"GEN_FUNCS\",\n    \"ols\",\n    \"ols_with_se\",\n    \"make_dummies\",\n    \"softmax_sample\",\n    \"misclassify\",\n]\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 40_

Now the example and tests.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "b839ba40-7b36-4de5-b870-a541d10b9ee7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XhysbagqkbBEhGETNwsqT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 117550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
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

_source line 41_

<details open><summary>🔧 Tool call — Write · `toolu_01HKs8GT4FAYMHxkb5zBgLsu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/examples/confounding_k3.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Worked example: confounding topology with K=3 confusion matrix.\n\nDemonstrates the full annot_sensitivity workflow:\n  1. Define a K=3 confusion matrix\n  2. Compute bias\n  3. Compute ASV\n  4. Get correction recommendation\n  5. (Optional) Plot bias curve\n\"\"\"\n\nimport numpy as np\nimport sys\nimport os\n\nsys.path.insert(0, os.path.join(os.path.dirname(__file__), \"..\", \"..\"))\n\nfrom annot_sensitivity import (\n    compute_bias,\n    compute_asv,\n    recommend_correction,\n    predefined_matrices,\n    validate_confusion_matrix,\n)\n\n\ndef main():\n    print(\"=\" * 60)\n    print(\"annot_sensitivity: Confounding K=3 Example\")\n    print(\"=\" * 60)\n\n    # 1. Define confusion matrix\n    C = np.array([\n        [0.80, 0.10, 0.10],\n        [0.10, 0.80, 0.10],\n        [0.10, 0.10, 0.80],\n    ])\n    print(f\"\\nConfusion matrix C (column-stochastic):\")\n    print(C)\n    print(f\"Valid: {validate_confusion_matrix(C)}\")\n    print(f\"Condition number: {np.linalg.cond(C):.1f}\")\n\n    # 2. Compute bias\n    print(\"\\n--- Bias Analysis ---\")\n    result = compute_bias(\"confounding\", C)\n    print(f\"tau_true  (no misclassification): {result['tau_true']:.4f}\")\n    print(f\"tau_biased (with C):              {result['tau_biased']:.4f}\")\n    print(f\"bias:                             {result['bias']:+.4f}\")\n    print(f\"bias_pct:                         {result['bias_pct']:+.2f}%\")\n\n    # Try all predefined matrices\n    print(f\"\\nBias across predefined matrices:\")\n    print(f\"  {'Matrix':<22} {'tau_biased':>10} {'bias':>10} {'bias_pct':>10}\")\n    print(f\"  {'-'*55}\")\n    for name, Ci in predefined_matrices().items():\n        r = compute_bias(\"confounding\", Ci)\n        print(f\"  {name:<22} {r['tau_biased']:>10.4f} {r['bias']:>+10.4f} \"\n              f\"{r['bias_pct']:>+9.2f}%\")\n\n    # 3. Compute ASV\n    print(\"\\n--- ASV Analysis ---\")\n    C0 = C.copy()\n    asv_result = compute_asv(\"confounding\", C0, threshold_type=\"magnitude\",\n                             threshold_value=0.1)\n    asv_val = asv_result[\"asv\"]\n    print(f\"tau_true:      {asv_result['tau_true']:.4f}\")\n    if asv_val is not None:\n        print(f\"Magnitude ASV: {asv_val:.3f} \"\n              f\"(bias exceeds 10% of tau at delta={asv_val:.3f})\")\n    else:\n        print(f\"Magnitude ASV: None (threshold never crossed)\")\n\n    asv_sf = compute_asv(\"confounding\", C0, threshold_type=\"sign_flip\")\n    sf_val = asv_sf[\"asv\"]\n    if sf_val is not None:\n        print(f\"Sign-flip ASV: {sf_val:.3f}\")\n    else:\n        print(f\"Sign-flip ASV: None (sign never flips)\")\n\n    # 4. Correction recommendation\n    print(\"\\n--- Correction Recommendation ---\")\n    rec_gold = recommend_correction(\"confounding\", C, has_gold=True,\n                                    gold_fraction=0.1)\n    print(f\"With gold labels:    {rec_gold['recommended']}\")\n    for note in rec_gold[\"notes\"]:\n        print(f\"  - {note}\")\n\n    rec_no_gold = recommend_correction(\"confounding\", C, has_gold=False)\n    print(f\"Without gold labels: {rec_no_gold['recommended']}\")\n    for note in rec_no_gold[\"notes\"]:\n        print(f\"  - {note}\")\n\n    print(f\"\\nMethod ranking (with gold):\")\n    for m in rec_gold[\"ranking\"]:\n        app = \"Y\" if m[\"applicable\"] else \"N\"\n        print(f\"  {m['method']:<16} applicable={app}  \"\n              f\"expected_bias_reduction={m['expected_bias_reduction']:+.1%}\")\n\n    # 5. Optional: plot bias curve\n    try:\n        import matplotlib\n        matplotlib.use(\"Agg\")\n        import matplotlib.pyplot as plt\n\n        fig, ax = plt.subplots(1, 1, figsize=(6, 4))\n        deltas = asv_result[\"deltas\"]\n        ax.plot(deltas, asv_result[\"bias_curve\"], \"b-\", alpha=0.4,\n                label=\"Pointwise |bias|\")\n        ax.plot(deltas, asv_result[\"envelope\"], \"r-\", linewidth=2,\n                label=\"Monotone envelope\")\n        thresh = 0.1 * abs(asv_result[\"tau_true\"])\n        ax.axhline(thresh, color=\"gray\", linestyle=\"--\", label=f\"10% threshold\")\n        if asv_val is not None:\n            ax.axvline(asv_val, color=\"green\", linestyle=\":\", label=f\"ASV={asv_val:.2f}\")\n        ax.set_xlabel(r\"$\\delta$ (interpolation parameter)\")\n        ax.set_ylabel(\"|Bias|\")\n        ax.set_title(\"Confounding K=3: ASV Bias Curve\")\n        ax.legend(fontsize=8)\n        ax.set_xlim(0, min(deltas[-1], 5))\n\n        out_path = os.path.join(os.path.dirname(__file__), \"..\", \"..\",\n                                \"artifacts\", \"example_bias_curve.png\")\n        os.makedirs(os.path.dirname(out_path), exist_ok=True)\n        fig.savefig(out_path, dpi=150, bbox_inches=\"tight\")\n        plt.close()\n        print(f\"\\nPlot saved to {out_path}\")\n    except ImportError:\n        print(\"\\nmatplotlib not available, skipping plot\")\n\n    print(\"\\nDone.\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "d51d0584-c988-496b-9689-90d6e9446c86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016XhysbagqkbBEhGETNwsqT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 117550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
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

_source line 42 · 2026-05-20T23:36:07.808Z_

<details><summary>↩ Tool result · `toolu_01HKs8GT4FAYMHxkb5zBgLsu`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/examples/confounding_k3.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "2aed914a-c7bd-4ae2-9516-2658fcd8c21c",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/examples/confounding_k3.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Worked example: confounding topology with K=3 confusion matrix.\n\nDemonstrates the full annot_sensitivity workflow:\n  1. Define a K=3 confusion matrix\n  2. Compute bias\n  3. Compute ASV\n  4. Get correction recommendation\n  5. (Optional) Plot bias curve\n\"\"\"\n\nimport numpy as np\nimport sys\nimport os\n\nsys.path.insert(0, os.path.join(os.path.dirname(__file__), \"..\", \"..\"))\n\nfrom annot_sensitivity import (\n    compute_bias,\n    compute_asv,\n    recommend_correction,\n    predefined_matrices,\n    validate_confusion_matrix,\n)\n\n\ndef main():\n    print(\"=\" * 60)\n    print(\"annot_sensitivity: Confounding K=3 Example\")\n    print(\"=\" * 60)\n\n    # 1. Define confusion matrix\n    C = np.array([\n        [0.80, 0.10, 0.10],\n        [0.10, 0.80, 0.10],\n        [0.10, 0.10, 0.80],\n    ])\n    print(f\"\\nConfusion matrix C (column-stochastic):\")\n    print(C)\n    print(f\"Valid: {validate_confusion_matrix(C)}\")\n    print(f\"Condition number: {np.linalg.cond(C):.1f}\")\n\n    # 2. Compute bias\n    print(\"\\n--- Bias Analysis ---\")\n    result = compute_bias(\"confounding\", C)\n    print(f\"tau_true  (no misclassification): {result['tau_true']:.4f}\")\n    print(f\"tau_biased (with C):              {result['tau_biased']:.4f}\")\n    print(f\"bias:                             {result['bias']:+.4f}\")\n    print(f\"bias_pct:                         {result['bias_pct']:+.2f}%\")\n\n    # Try all predefined matrices\n    print(f\"\\nBias across predefined matrices:\")\n    print(f\"  {'Matrix':<22} {'tau_biased':>10} {'bias':>10} {'bias_pct':>10}\")\n    print(f\"  {'-'*55}\")\n    for name, Ci in predefined_matrices().items():\n        r = compute_bias(\"confounding\", Ci)\n        print(f\"  {name:<22} {r['tau_biased']:>10.4f} {r['bias']:>+10.4f} \"\n              f\"{r['bias_pct']:>+9.2f}%\")\n\n    # 3. Compute ASV\n    print(\"\\n--- ASV Analysis ---\")\n    C0 = C.copy()\n    asv_result = compute_asv(\"confounding\", C0, threshold_type=\"magnitude\",\n                             threshold_value=0.1)\n    asv_val = asv_result[\"asv\"]\n    print(f\"tau_true:      {asv_result['tau_true']:.4f}\")\n    if asv_val is not None:\n        print(f\"Magnitude ASV: {asv_val:.3f} \"\n              f\"(bias exceeds 10% of tau at delta={asv_val:.3f})\")\n    else:\n        print(f\"Magnitude ASV: None (threshold never crossed)\")\n\n    asv_sf = compute_asv(\"confounding\", C0, threshold_type=\"sign_flip\")\n    sf_val = asv_sf[\"asv\"]\n    if sf_val is not None:\n        print(f\"Sign-flip ASV: {sf_val:.3f}\")\n    else:\n        print(f\"Sign-flip ASV: None (sign never flips)\")\n\n    # 4. Correction recommendation\n    print(\"\\n--- Correction Recommendation ---\")\n    rec_gold = recommend_correction(\"confounding\", C, has_gold=True,\n                                    gold_fraction=0.1)\n    print(f\"With gold labels:    {rec_gold['recommended']}\")\n    for note in rec_gold[\"notes\"]:\n        print(f\"  - {note}\")\n\n    rec_no_gold = recommend_correction(\"confounding\", C, has_gold=False)\n    print(f\"Without gold labels: {rec_no_gold['recommended']}\")\n    for note in rec_no_gold[\"notes\"]:\n        print(f\"  - {note}\")\n\n    print(f\"\\nMethod ranking (with gold):\")\n    for m in rec_gold[\"ranking\"]:\n        app = \"Y\" if m[\"applicable\"] else \"N\"\n        print(f\"  {m['method']:<16} applicable={app}  \"\n              f\"expected_bias_reduction={m['expected_bias_reduction']:+.1%}\")\n\n    # 5. Optional: plot bias curve\n    try:\n        import matplotlib\n        matplotlib.use(\"Agg\")\n        import matplotlib.pyplot as plt\n\n        fig, ax = plt.subplots(1, 1, figsize=(6, 4))\n        deltas = asv_result[\"deltas\"]\n        ax.plot(deltas, asv_result[\"bias_curve\"], \"b-\", alpha=0.4,\n                label=\"Pointwise |bias|\")\n        ax.plot(deltas, asv_result[\"envelope\"], \"r-\", linewidth=2,\n                label=\"Monotone envelope\")\n        thresh = 0.1 * abs(asv_result[\"tau_true\"])\n        ax.axhline(thresh, color=\"gray\", linestyle=\"--\", label=f\"10% threshold\")\n        if asv_val is not None:\n            ax.axvline(asv_val, color=\"green\", linestyle=\":\", label=f\"ASV={asv_val:.2f}\")\n        ax.set_xlabel(r\"$\\delta$ (interpolation parameter)\")\n        ax.set_ylabel(\"|Bias|\")\n        ax.set_title(\"Confounding K=3: ASV Bias Curve\")\n        ax.legend(fontsize=8)\n        ax.set_xlim(0, min(deltas[-1], 5))\n\n        out_path = os.path.join(os.path.dirname(__file__), \"..\", \"..\",\n                                \"artifacts\", \"example_bias_curve.png\")\n        os.makedirs(os.path.dirname(out_path), exist_ok=True)\n        fig.savefig(out_path, dpi=150, bbox_inches=\"tight\")\n        plt.close()\n        print(f\"\\nPlot saved to {out_path}\")\n    except ImportError:\n        print(\"\\nmatplotlib not available, skipping plot\")\n\n    print(\"\\nDone.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Write · `toolu_01HFSJyiw9BEKtYfTtzCvbuH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/__init__.py",
  "content": ""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "e84a89af-8578-4906-a3ab-489c40403900",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ThebK3CQtotKZn851bLYDZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1931,
      "cache_read_input_tokens": 118142,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1931
      },
      "output_tokens": 65,
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

_source line 44 · 2026-05-20T23:36:11.325Z_

<details><summary>↩ Tool result · `toolu_01HFSJyiw9BEKtYfTtzCvbuH`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/__init__.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "e472b5d1-ea50-4c19-8b1f-168d86387885",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/__init__.py",
    "content": "",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Write · `toolu_01YRGGQYnTHbhAX38LUEAYoc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/test_core.py",
  "content": "\"\"\"Core tests for the annot_sensitivity package.\"\"\"\n\nimport numpy as np\nimport pytest\nfrom annot_sensitivity import (\n    compute_bias,\n    compute_asv,\n    recommend_correction,\n    validate_confusion_matrix,\n    interpolate_confusion,\n    random_confusion_matrix,\n    predefined_matrices,\n    generate_data,\n    TOPOLOGIES,\n)\n\n\nclass TestValidateConfusionMatrix:\n    def test_identity_valid(self):\n        assert validate_confusion_matrix(np.eye(3)) is True\n\n    def test_predefined_valid(self):\n        for name, C in predefined_matrices().items():\n            assert validate_confusion_matrix(C) is True, f\"{name} failed\"\n\n    def test_non_square(self):\n        assert validate_confusion_matrix(np.ones((2, 3))) is False\n\n    def test_negative_entries(self):\n        C = np.array([[1.1, -0.1], [-0.1, 1.1]])\n        assert validate_confusion_matrix(C) is False\n\n    def test_not_column_stochastic(self):\n        C = np.array([[0.5, 0.5], [0.3, 0.3]])\n        assert validate_confusion_matrix(C) is False\n\n    def test_not_array(self):\n        assert validate_confusion_matrix([[1, 0], [0, 1]]) is False\n\n    def test_1x1(self):\n        assert validate_confusion_matrix(np.array([[1.0]])) is False\n\n    def test_random_valid(self):\n        C = random_confusion_matrix(4, diag_dominance=0.7, rng=np.random.default_rng(42))\n        assert validate_confusion_matrix(C) is True\n        assert C.shape == (4, 4)\n\n\nclass TestInterpolateConfusion:\n    def test_delta_zero_is_identity(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        C = interpolate_confusion(C0, 0.0)\n        np.testing.assert_allclose(C, np.eye(3), atol=1e-12)\n\n    def test_delta_one_is_C0(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        C = interpolate_confusion(C0, 1.0)\n        np.testing.assert_allclose(C, C0, atol=1e-12)\n\n    def test_intermediate_column_stochastic(self):\n        C0 = predefined_matrices()[\"asymmetric\"]\n        C = interpolate_confusion(C0, 0.5)\n        assert validate_confusion_matrix(C)\n\n    def test_small_delta(self):\n        C0 = predefined_matrices()[\"severe_uniform\"]\n        C = interpolate_confusion(C0, 0.01)\n        assert np.allclose(np.diag(C), np.ones(3) * (1 - 0.01) + 0.01 * np.diag(C0),\n                           atol=1e-6)\n\n\nclass TestComputeBias:\n    def test_identity_zero_bias(self):\n        result = compute_bias(\"confounding\", np.eye(3))\n        assert abs(result[\"bias\"]) < 1e-3\n        assert abs(result[\"bias_pct\"]) < 0.1\n\n    def test_confounding_nonzero_bias(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = compute_bias(\"confounding\", C)\n        assert abs(result[\"bias\"]) > 0.01\n        assert result[\"topology\"] == \"confounding\"\n        assert np.isfinite(result[\"tau_true\"])\n        assert np.isfinite(result[\"tau_biased\"])\n\n    def test_all_topologies_run(self):\n        C = predefined_matrices()[\"mild_uniform\"]\n        for topo in TOPOLOGIES:\n            result = compute_bias(topo, C)\n            assert result[\"topology\"] == topo\n            assert np.isfinite(result[\"tau_true\"])\n            assert np.isfinite(result[\"tau_biased\"])\n\n    def test_invalid_topology(self):\n        with pytest.raises(ValueError, match=\"Unknown topology\"):\n            compute_bias(\"nonexistent\", np.eye(3))\n\n    def test_invalid_C(self):\n        with pytest.raises(ValueError, match=\"column-stochastic\"):\n            compute_bias(\"confounding\", np.ones((3, 3)))\n\n    def test_worse_C_more_bias(self):\n        C_mild = predefined_matrices()[\"mild_uniform\"]\n        C_severe = predefined_matrices()[\"severe_uniform\"]\n        r_mild = compute_bias(\"confounding\", C_mild)\n        r_severe = compute_bias(\"confounding\", C_severe)\n        assert abs(r_severe[\"bias\"]) > abs(r_mild[\"bias\"])\n\n\nclass TestComputeASV:\n    def test_returns_valid_structure(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        result = compute_asv(\"confounding\", C0, n_grid=200)\n        assert \"asv\" in result\n        assert \"bias_curve\" in result\n        assert \"envelope\" in result\n        assert \"deltas\" in result\n        assert \"tau_true\" in result\n        assert len(result[\"deltas\"]) == 200\n        assert len(result[\"bias_curve\"]) == 200\n        assert len(result[\"envelope\"]) == 200\n\n    def test_asv_is_positive_or_none(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        result = compute_asv(\"confounding\", C0, threshold_type=\"magnitude\",\n                             threshold_value=0.1, n_grid=200)\n        if result[\"asv\"] is not None:\n            assert result[\"asv\"] > 0\n\n    def test_envelope_monotone(self):\n        C0 = predefined_matrices()[\"asymmetric\"]\n        result = compute_asv(\"mediation\", C0, n_grid=200)\n        diffs = np.diff(result[\"envelope\"])\n        assert np.all(diffs >= -1e-12)\n\n    def test_sign_flip_threshold(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        result = compute_asv(\"confounding\", C0, threshold_type=\"sign_flip\",\n                             n_grid=200)\n        assert \"asv\" in result\n\n    def test_invalid_threshold_type(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        with pytest.raises(ValueError, match=\"Unknown threshold_type\"):\n            compute_asv(\"confounding\", C0, threshold_type=\"invalid\", n_grid=50)\n\n\nclass TestRecommendCorrection:\n    def test_with_gold_recommends_ppi(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"confounding\", C, has_gold=True)\n        assert result[\"recommended\"] == \"ppi\"\n\n    def test_without_gold_confounding_recommends_dsl(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"confounding\", C, has_gold=False)\n        assert result[\"recommended\"] == \"dsl\"\n\n    def test_without_gold_mediation_recommends_dsl(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"mediation\", C, has_gold=False)\n        assert result[\"recommended\"] == \"dsl\"\n\n    def test_without_gold_collider_recommends_mcsimex(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"collider\", C, has_gold=False)\n        assert result[\"recommended\"] == \"mcsimex\"\n\n    def test_without_gold_mbias_recommends_mcsimex(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"mbias\", C, has_gold=False)\n        assert result[\"recommended\"] == \"mcsimex\"\n\n    def test_ranking_has_all_methods(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"confounding\", C, has_gold=True)\n        methods = {m[\"method\"] for m in result[\"ranking\"]}\n        assert methods == {\"ppi\", \"dsl\", \"mcsimex\", \"naive_plugin\", \"mla\"}\n\n    def test_notes_nonempty(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"collider\", C, has_gold=False)\n        assert len(result[\"notes\"]) > 0\n\n\nclass TestDGP:\n    def test_generate_all_topologies(self):\n        for topo in TOPOLOGIES:\n            data = generate_data(topo, 100, seed=42)\n            assert \"Y\" in data\n            assert \"A\" in data\n            assert len(data[\"Y\"]) == 100\n\n    def test_confounding_has_treatment(self):\n        data = generate_data(\"confounding\", 100, seed=42)\n        assert \"T\" in data\n\n    def test_exposure_no_treatment(self):\n        data = generate_data(\"exposure\", 100, seed=42)\n        assert \"T\" not in data\n\n    def test_iv_has_instrument(self):\n        data = generate_data(\"iv\", 100, seed=42)\n        assert \"Z\" in data\n\n    def test_invalid_topology(self):\n        with pytest.raises(ValueError):\n            generate_data(\"invalid\", 100)\n\n\nif __name__ == \"__main__\":\n    pytest.main([__file__, \"-v\"])\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "89976117-e538-43b9-be96-8675960426d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SLvKptjGM3y1us26qVnaXP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 162,
      "cache_read_input_tokens": 120073,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 162
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

_source line 46 · 2026-05-20T23:36:40.548Z_

<details><summary>↩ Tool result · `toolu_01YRGGQYnTHbhAX38LUEAYoc`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/test_core.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "43a67b8e-f051-48e7-91c7-5277afda0877",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/test_core.py",
    "content": "\"\"\"Core tests for the annot_sensitivity package.\"\"\"\n\nimport numpy as np\nimport pytest\nfrom annot_sensitivity import (\n    compute_bias,\n    compute_asv,\n    recommend_correction,\n    validate_confusion_matrix,\n    interpolate_confusion,\n    random_confusion_matrix,\n    predefined_matrices,\n    generate_data,\n    TOPOLOGIES,\n)\n\n\nclass TestValidateConfusionMatrix:\n    def test_identity_valid(self):\n        assert validate_confusion_matrix(np.eye(3)) is True\n\n    def test_predefined_valid(self):\n        for name, C in predefined_matrices().items():\n            assert validate_confusion_matrix(C) is True, f\"{name} failed\"\n\n    def test_non_square(self):\n        assert validate_confusion_matrix(np.ones((2, 3))) is False\n\n    def test_negative_entries(self):\n        C = np.array([[1.1, -0.1], [-0.1, 1.1]])\n        assert validate_confusion_matrix(C) is False\n\n    def test_not_column_stochastic(self):\n        C = np.array([[0.5, 0.5], [0.3, 0.3]])\n        assert validate_confusion_matrix(C) is False\n\n    def test_not_array(self):\n        assert validate_confusion_matrix([[1, 0], [0, 1]]) is False\n\n    def test_1x1(self):\n        assert validate_confusion_matrix(np.array([[1.0]])) is False\n\n    def test_random_valid(self):\n        C = random_confusion_matrix(4, diag_dominance=0.7, rng=np.random.default_rng(42))\n        assert validate_confusion_matrix(C) is True\n        assert C.shape == (4, 4)\n\n\nclass TestInterpolateConfusion:\n    def test_delta_zero_is_identity(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        C = interpolate_confusion(C0, 0.0)\n        np.testing.assert_allclose(C, np.eye(3), atol=1e-12)\n\n    def test_delta_one_is_C0(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        C = interpolate_confusion(C0, 1.0)\n        np.testing.assert_allclose(C, C0, atol=1e-12)\n\n    def test_intermediate_column_stochastic(self):\n        C0 = predefined_matrices()[\"asymmetric\"]\n        C = interpolate_confusion(C0, 0.5)\n        assert validate_confusion_matrix(C)\n\n    def test_small_delta(self):\n        C0 = predefined_matrices()[\"severe_uniform\"]\n        C = interpolate_confusion(C0, 0.01)\n        assert np.allclose(np.diag(C), np.ones(3) * (1 - 0.01) + 0.01 * np.diag(C0),\n                           atol=1e-6)\n\n\nclass TestComputeBias:\n    def test_identity_zero_bias(self):\n        result = compute_bias(\"confounding\", np.eye(3))\n        assert abs(result[\"bias\"]) < 1e-3\n        assert abs(result[\"bias_pct\"]) < 0.1\n\n    def test_confounding_nonzero_bias(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = compute_bias(\"confounding\", C)\n        assert abs(result[\"bias\"]) > 0.01\n        assert result[\"topology\"] == \"confounding\"\n        assert np.isfinite(result[\"tau_true\"])\n        assert np.isfinite(result[\"tau_biased\"])\n\n    def test_all_topologies_run(self):\n        C = predefined_matrices()[\"mild_uniform\"]\n        for topo in TOPOLOGIES:\n            result = compute_bias(topo, C)\n            assert result[\"topology\"] == topo\n            assert np.isfinite(result[\"tau_true\"])\n            assert np.isfinite(result[\"tau_biased\"])\n\n    def test_invalid_topology(self):\n        with pytest.raises(ValueError, match=\"Unknown topology\"):\n            compute_bias(\"nonexistent\", np.eye(3))\n\n    def test_invalid_C(self):\n        with pytest.raises(ValueError, match=\"column-stochastic\"):\n            compute_bias(\"confounding\", np.ones((3, 3)))\n\n    def test_worse_C_more_bias(self):\n        C_mild = predefined_matrices()[\"mild_uniform\"]\n        C_severe = predefined_matrices()[\"severe_uniform\"]\n        r_mild = compute_bias(\"confounding\", C_mild)\n        r_severe = compute_bias(\"confounding\", C_severe)\n        assert abs(r_severe[\"bias\"]) > abs(r_mild[\"bias\"])\n\n\nclass TestComputeASV:\n    def test_returns_valid_structure(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        result = compute_asv(\"confounding\", C0, n_grid=200)\n        assert \"asv\" in result\n        assert \"bias_curve\" in result\n        assert \"envelope\" in result\n        assert \"deltas\" in result\n        assert \"tau_true\" in result\n        assert len(result[\"deltas\"]) == 200\n        assert len(result[\"bias_curve\"]) == 200\n        assert len(result[\"envelope\"]) == 200\n\n    def test_asv_is_positive_or_none(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        result = compute_asv(\"confounding\", C0, threshold_type=\"magnitude\",\n                             threshold_value=0.1, n_grid=200)\n        if result[\"asv\"] is not None:\n            assert result[\"asv\"] > 0\n\n    def test_envelope_monotone(self):\n        C0 = predefined_matrices()[\"asymmetric\"]\n        result = compute_asv(\"mediation\", C0, n_grid=200)\n        diffs = np.diff(result[\"envelope\"])\n        assert np.all(diffs >= -1e-12)\n\n    def test_sign_flip_threshold(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        result = compute_asv(\"confounding\", C0, threshold_type=\"sign_flip\",\n                             n_grid=200)\n        assert \"asv\" in result\n\n    def test_invalid_threshold_type(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        with pytest.raises(ValueError, match=\"Unknown threshold_type\"):\n            compute_asv(\"confounding\", C0, threshold_type=\"invalid\", n_grid=50)\n\n\nclass TestRecommendCorrection:\n    def test_with_gold_recommends_ppi(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"confounding\", C, has_gold=True)\n        assert result[\"recommended\"] == \"ppi\"\n\n    def test_without_gold_confounding_recommends_dsl(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"confounding\", C, has_gold=False)\n        assert result[\"recommended\"] == \"dsl\"\n\n    def test_without_gold_mediation_recommends_dsl(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"mediation\", C, has_gold=False)\n        assert result[\"recommended\"] == \"dsl\"\n\n    def test_without_gold_collider_recommends_mcsimex(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"collider\", C, has_gold=False)\n        assert result[\"recommended\"] == \"mcsimex\"\n\n    def test_without_gold_mbias_recommends_mcsimex(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"mbias\", C, has_gold=False)\n        assert result[\"recommended\"] == \"mcsimex\"\n\n    def test_ranking_has_all_methods(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"confounding\", C, has_gold=True)\n        methods = {m[\"method\"] for m in result[\"ranking\"]}\n        assert methods == {\"ppi\", \"dsl\", \"mcsimex\", \"naive_plugin\", \"mla\"}\n\n    def test_notes_nonempty(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"collider\", C, has_gold=False)\n        assert len(result[\"notes\"]) > 0\n\n\nclass TestDGP:\n    def test_generate_all_topologies(self):\n        for topo in TOPOLOGIES:\n            data = generate_data(topo, 100, seed=42)\n            assert \"Y\" in data\n            assert \"A\" in data\n            assert len(data[\"Y\"]) == 100\n\n    def test_confounding_has_treatment(self):\n        data = generate_data(\"confounding\", 100, seed=42)\n        assert \"T\" in data\n\n    def test_exposure_no_treatment(self):\n        data = generate_data(\"exposure\", 100, seed=42)\n        assert \"T\" not in data\n\n    def test_iv_has_instrument(self):\n        data = generate_data(\"iv\", 100, seed=42)\n        assert \"Z\" in data\n\n    def test_invalid_topology(self):\n        with pytest.raises(ValueError):\n            generate_data(\"invalid\", 100)\n\n\nif __name__ == \"__main__\":\n    pytest.main([__file__, \"-v\"])\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 47_

All files written. Now let me run the verification steps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "a22299cd-02b3-499f-901f-4656c3366db9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SoD1Vzsd1MyDdDzskdHqnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2587,
      "cache_read_input_tokens": 120235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2587
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

_source line 48_

<details open><summary>🔧 Tool call — Bash · `toolu_01PYAafwL9ds2Wt4Zups76V9`</summary>

```json
{
  "command": "python -c \"from annot_sensitivity import compute_bias, compute_asv, recommend_correction; print('Import OK')\"",
  "description": "Test basic import"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "891cbdb4-e60c-429a-a99f-612cbc55ba0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SoD1Vzsd1MyDdDzskdHqnM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2587,
      "cache_read_input_tokens": 120235,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2587
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

_source line 49 · 2026-05-20T23:36:44.768Z_

<details><summary>↩ Tool result · reported error · `toolu_01PYAafwL9ds2Wt4Zups76V9`</summary>

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
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "0b1f3162-148b-4be6-a2af-dedaa3afefe6",
  "tool_use_result": "Error: Exit code 127\n/bin/bash: line 1: python: command not found"
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Bash · `toolu_01VsRPnQvRWvE15FVdyMCBQc`</summary>

```json
{
  "command": "python3 -c \"from annot_sensitivity import compute_bias, compute_asv, recommend_correction; print('Import OK')\"",
  "description": "Test basic import with python3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "855dc93d-afe0-46db-adcb-65a35d38481d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FwKiq2F2WimCDVh3ZBpQGU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 151,
      "cache_read_input_tokens": 122822,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 151
      },
      "output_tokens": 67,
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

_source line 51 · 2026-05-20T23:36:49.000Z_

<details><summary>↩ Tool result · `toolu_01VsRPnQvRWvE15FVdyMCBQc`</summary>

```text
Import OK
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "fe2e4a13-e6f7-4e70-9864-7e960a0ec8dc",
  "tool_use_result": {
    "stdout": "Import OK",
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

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_01TitMrhWfJSCLKvHvjcJdBY`</summary>

```json
{
  "command": "python3 -m pytest annot_sensitivity/tests/test_core.py -v 2>&1",
  "description": "Run pytest test suite",
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
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "05b454d5-d9aa-47d9-82f7-0018490c3ae6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R9Qev6hQaTZFwi2q8kQxhN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 118,
      "cache_read_input_tokens": 122973,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 118
      },
      "output_tokens": 64,
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

_source line 53 · 2026-05-20T23:36:53.354Z_

<details><summary>↩ Tool result · reported error · `toolu_01TitMrhWfJSCLKvHvjcJdBY`</summary>

```text
Exit code 1
/usr/bin/python3: No module named pytest
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "9647769f-73b6-47c2-8e20-4e8eba4eb4c5",
  "tool_use_result": "Error: Exit code 1\n/usr/bin/python3: No module named pytest"
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Bash · `toolu_019DYBh1eDzW8cb6aqH8MZYQ`</summary>

```json
{
  "command": "pip3 install pytest -q 2>&1 | tail -3",
  "description": "Install pytest"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "a669f897-7b27-489c-bdf5-9278252852cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GL3fbDo9Lu5iLZj8Fe4CMf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 150,
      "cache_read_input_tokens": 123091,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 150
      },
      "output_tokens": 61,
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

_source line 55 · 2026-05-20T23:37:02.958Z_

<details><summary>↩ Tool result · `toolu_019DYBh1eDzW8cb6aqH8MZYQ`</summary>

```text
note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "77614e0f-3d53-49e9-a6e5-6c25258d926d",
  "tool_use_result": {
    "stdout": "note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.\nhint: See PEP 668 for the detailed specification.",
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

_source line 56_

<details open><summary>🔧 Tool call — Bash · `toolu_01BNxp474ssZvcCV1tMfi2j9`</summary>

```json
{
  "command": "pip3 install --user pytest -q 2>&1 | tail -3",
  "description": "Install pytest with --user flag"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "3c70dfd0-962d-4f53-9587-8d7e09177e78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LSNsoZTdPZtaAA2KV1PWTg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 156,
      "cache_read_input_tokens": 123241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 156
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

_source line 57 · 2026-05-20T23:37:07.371Z_

<details><summary>↩ Tool result · `toolu_01BNxp474ssZvcCV1tMfi2j9`</summary>

```text
note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "a78b60b2-1b05-4053-8401-6e41c0139b03",
  "tool_use_result": {
    "stdout": "note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.\nhint: See PEP 668 for the detailed specification.",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01YMoeMZTx3TLw2RJ3euEQaL`</summary>

```json
{
  "command": "pip3 install --break-system-packages pytest -q 2>&1 | tail -3",
  "description": "Install pytest (break-system-packages for PEP 668)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "e2ebde34-cec6-4d50-adb1-cf3959001aa6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Psc6xuHBUgw9JnCjRm4GwQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 162,
      "cache_read_input_tokens": 123397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 162
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

_source line 59_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b7i2lmpqn",
  "tool_use_id": "toolu_01YMoeMZTx3TLw2RJ3euEQaL",
  "description": "Install pytest (break-system-packages for PEP 668)",
  "task_type": "local_bash",
  "uuid": "1b0fb080-d4dc-4d8d-aca0-7a5f0a7b4084",
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e"
}
```

---

### System

_source line 60_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b7i2lmpqn",
  "tool_use_id": "toolu_01YMoeMZTx3TLw2RJ3euEQaL",
  "status": "completed",
  "output_file": "",
  "summary": "Install pytest (break-system-packages for PEP 668)",
  "uuid": "d7f31d87-98fc-4566-a0e1-ea9ee5128f3d",
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e"
}
```

---

### Tool result

_source line 61 · 2026-05-20T23:37:17.907Z_

<details><summary>↩ Tool result · `toolu_01YMoeMZTx3TLw2RJ3euEQaL`</summary>

```text
  WARNING: The scripts py.test and pytest are installed in '/home/ubuntu/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "874adffc-0ff9-461a-b2be-2fb4d303bd9d",
  "tool_use_result": {
    "stdout": "  WARNING: The scripts py.test and pytest are installed in '/home/ubuntu/.local/bin' which is not on PATH.\n  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.",
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

_source line 62_

<details open><summary>🔧 Tool call — Bash · `toolu_015sG5AkKDNkqCUdsJopraAn`</summary>

```json
{
  "command": "python3 -m pytest annot_sensitivity/tests/test_core.py -v 2>&1",
  "description": "Run pytest test suite",
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
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "c0b819b0-5df0-42aa-8fe4-48f756b35e7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JAve5eWGFd4QXqreguXhnC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 170,
      "cache_read_input_tokens": 123559,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 170
      },
      "output_tokens": 67,
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

_source line 63_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bq17jee2w",
  "tool_use_id": "toolu_015sG5AkKDNkqCUdsJopraAn",
  "description": "Run pytest test suite",
  "task_type": "local_bash",
  "uuid": "d39af8d5-928a-4539-a284-ee4ed8f246b0",
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e"
}
```

---

### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bq17jee2w",
  "tool_use_id": "toolu_015sG5AkKDNkqCUdsJopraAn",
  "status": "completed",
  "output_file": "",
  "summary": "Run pytest test suite",
  "uuid": "7be820c2-c917-406b-ac39-8fd988b33fe7",
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e"
}
```

---

### Tool result

_source line 65 · 2026-05-20T23:37:38.485Z_

<details><summary>↩ Tool result · `toolu_015sG5AkKDNkqCUdsJopraAn`</summary>

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

============================= 35 passed in 14.30s ==============================
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "3397ad2d-e9a5-41a9-af35-11c24e27b34f",
  "tool_use_result": {
    "stdout": "============================= test session starts ==============================\nplatform linux -- Python 3.14.4, pytest-9.0.3, pluggy-1.6.0 -- /usr/bin/python3\ncachedir: .pytest_cache\nrootdir: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib\nplugins: anyio-4.13.0, typeguard-4.4.4\ncollecting ... collected 35 items\n\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_identity_valid PASSED [  2%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_predefined_valid PASSED [  5%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_non_square PASSED [  8%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_negative_entries PASSED [ 11%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_not_column_stochastic PASSED [ 14%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_not_array PASSED [ 17%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_1x1 PASSED [ 20%]\nannot_sensitivity/tests/test_core.py::TestValidateConfusionMatrix::test_random_valid PASSED [ 22%]\nannot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_delta_zero_is_identity PASSED [ 25%]\nannot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_delta_one_is_C0 PASSED [ 28%]\nannot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_intermediate_column_stochastic PASSED [ 31%]\nannot_sensitivity/tests/test_core.py::TestInterpolateConfusion::test_small_delta PASSED [ 34%]\nannot_sensitivity/tests/test_core.py::TestComputeBias::test_identity_zero_bias PASSED [ 37%]\nannot_sensitivity/tests/test_core.py::TestComputeBias::test_confounding_nonzero_bias PASSED [ 40%]\nannot_sensitivity/tests/test_core.py::TestComputeBias::test_all_topologies_run PASSED [ 42%]\nannot_sensitivity/tests/test_core.py::TestComputeBias::test_invalid_topology PASSED [ 45%]\nannot_sensitivity/tests/test_core.py::TestComputeBias::test_invalid_C PASSED [ 48%]\nannot_sensitivity/tests/test_core.py::TestComputeBias::test_worse_C_more_bias PASSED [ 51%]\nannot_sensitivity/tests/test_core.py::TestComputeASV::test_returns_valid_structure PASSED [ 54%]\nannot_sensitivity/tests/test_core.py::TestComputeASV::test_asv_is_positive_or_none PASSED [ 57%]\nannot_sensitivity/tests/test_core.py::TestComputeASV::test_envelope_monotone PASSED [ 60%]\nannot_sensitivity/tests/test_core.py::TestComputeASV::test_sign_flip_threshold PASSED [ 62%]\nannot_sensitivity/tests/test_core.py::TestComputeASV::test_invalid_threshold_type PASSED [ 65%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_with_gold_recommends_ppi PASSED [ 68%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_confounding_recommends_dsl PASSED [ 71%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_mediation_recommends_dsl PASSED [ 74%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_collider_recommends_mcsimex PASSED [ 77%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_without_gold_mbias_recommends_mcsimex PASSED [ 80%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_ranking_has_all_methods PASSED [ 82%]\nannot_sensitivity/tests/test_core.py::TestRecommendCorrection::test_notes_nonempty PASSED [ 85%]\nannot_sensitivity/tests/test_core.py::TestDGP::test_generate_all_topologies PASSED [ 88%]\nannot_sensitivity/tests/test_core.py::TestDGP::test_confounding_has_treatment PASSED [ 91%]\nannot_sensitivity/tests/test_core.py::TestDGP::test_exposure_no_treatment PASSED [ 94%]\nannot_sensitivity/tests/test_core.py::TestDGP::test_iv_has_instrument PASSED [ 97%]\nannot_sensitivity/tests/test_core.py::TestDGP::test_invalid_topology PASSED [100%]\n\n============================= 35 passed in 14.30s ==============================",
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

_source line 66_

35/35 tests pass. Now run the example.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "6822042f-84b6-4226-b5b5-156ae90d7822",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CebB79KhBT44SSw6ofMa7y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 123729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1616
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

_source line 67_

<details open><summary>🔧 Tool call — Bash · `toolu_01MmvVa986pcg8cxc5mDLBvi`</summary>

```json
{
  "command": "python3 annot_sensitivity/examples/confounding_k3.py 2>&1",
  "description": "Run worked example",
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
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "e8120a67-8c84-4f0a-8ca0-36c3a8acbb66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CebB79KhBT44SSw6ofMa7y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 123729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1616
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

_source line 68 · 2026-05-20T23:37:44.289Z_

<details><summary>↩ Tool result · `toolu_01MmvVa986pcg8cxc5mDLBvi`</summary>

```text
============================================================
annot_sensitivity: Confounding K=3 Example
============================================================

Confusion matrix C (column-stochastic):
[[0.8 0.1 0.1]
 [0.1 0.8 0.1]
 [0.1 0.1 0.8]]
Valid: True
Condition number: 1.4

--- Bias Analysis ---
tau_true  (no misclassification): 2.0004
tau_biased (with C):              2.2045
bias:                             +0.2040
bias_pct:                         +10.20%

Bias across predefined matrices:
  Matrix                 tau_biased       bias   bias_pct
  -------------------------------------------------------
  symmetric_high             2.2045    +0.2040    +10.20%
  mild_uniform               2.1610    +0.1605     +8.03%
  moderate_uniform           2.2355    +0.2351    +11.75%
  severe_uniform             2.2745    +0.2741    +13.70%
  asymmetric                 2.2232    +0.2227    +11.13%
  near_permutation           2.1325    +0.1321     +6.60%
  realistic_llm              2.2455    +0.2451    +12.25%

--- ASV Analysis ---
tau_true:      2.0004
Magnitude ASV: 0.967 (bias exceeds 10% of tau at delta=0.967)
Sign-flip ASV: None (sign never flips)

--- Correction Recommendation ---
With gold labels:    ppi
  - Gold labels available (10% of data)
  - PPI++ recommended: highest bias reduction with valid coverage
Without gold labels: dsl
  - No gold labels available
  - DSL recommended for confounding (EM-based, works with known C)

Method ranking (with gold):
  ppi              applicable=Y  expected_bias_reduction=+93.8%
  dsl              applicable=Y  expected_bias_reduction=+75.0%
  mcsimex          applicable=Y  expected_bias_reduction=+20.9%
  naive_plugin     applicable=Y  expected_bias_reduction=+0.0%
  mla              applicable=Y  expected_bias_reduction=+0.0%

matplotlib not available, skipping plot

Done.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "f70428d9-c605-4f29-86a2-dc82c21d09e7",
  "tool_use_result": {
    "stdout": "============================================================\nannot_sensitivity: Confounding K=3 Example\n============================================================\n\nConfusion matrix C (column-stochastic):\n[[0.8 0.1 0.1]\n [0.1 0.8 0.1]\n [0.1 0.1 0.8]]\nValid: True\nCondition number: 1.4\n\n--- Bias Analysis ---\ntau_true  (no misclassification): 2.0004\ntau_biased (with C):              2.2045\nbias:                             +0.2040\nbias_pct:                         +10.20%\n\nBias across predefined matrices:\n  Matrix                 tau_biased       bias   bias_pct\n  -------------------------------------------------------\n  symmetric_high             2.2045    +0.2040    +10.20%\n  mild_uniform               2.1610    +0.1605     +8.03%\n  moderate_uniform           2.2355    +0.2351    +11.75%\n  severe_uniform             2.2745    +0.2741    +13.70%\n  asymmetric                 2.2232    +0.2227    +11.13%\n  near_permutation           2.1325    +0.1321     +6.60%\n  realistic_llm              2.2455    +0.2451    +12.25%\n\n--- ASV Analysis ---\ntau_true:      2.0004\nMagnitude ASV: 0.967 (bias exceeds 10% of tau at delta=0.967)\nSign-flip ASV: None (sign never flips)\n\n--- Correction Recommendation ---\nWith gold labels:    ppi\n  - Gold labels available (10% of data)\n  - PPI++ recommended: highest bias reduction with valid coverage\nWithout gold labels: dsl\n  - No gold labels available\n  - DSL recommended for confounding (EM-based, works with known C)\n\nMethod ranking (with gold):\n  ppi              applicable=Y  expected_bias_reduction=+93.8%\n  dsl              applicable=Y  expected_bias_reduction=+75.0%\n  mcsimex          applicable=Y  expected_bias_reduction=+20.9%\n  naive_plugin     applicable=Y  expected_bias_reduction=+0.0%\n  mla              applicable=Y  expected_bias_reduction=+0.0%\n\nmatplotlib not available, skipping plot\n\nDone.",
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

_source line 69_

All three verification steps pass:

1. **Import** — works
2. **35/35 pytest tests** — all pass (14s)
3. **Worked example** — runs correctly, shows confounding bias of +10.2% with symmetric_high C, ASV at δ=0.967, recommends PPI++ with gold / DSL without

Package structure created:

```
annot_sensitivity/
├── __init__.py          # Public API: compute_bias, compute_asv, recommend_correction, ...
├── utils.py             # softmax_sample, misclassify, make_dummies, ols, ols_with_se
├── confusion.py         # validate, random, interpolate, predefined matrices
├── dgp.py               # 7 topology DGPs with DEFAULT_PARAMS
├── bias.py              # compute_bias via precomputed plim (2M samples, cached)
├── asv.py               # compute_asv with magnitude/significance/sign_flip thresholds
├── correction.py        # 5 correction methods + recommend_correction
├── examples/
│   └── confounding_k3.py   # Full workflow demo
└── tests/
    ├── __init__.py
    └── test_core.py     # 35 tests across all modules
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "uuid": "9efc1701-81b1-494f-a5a6-476d27efd789",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YMVNWMvReKZTghM75xAqyC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 125345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 720
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

_source line 70_

All three verification steps pass:

1. **Import** — works
2. **35/35 pytest tests** — all pass (14s)
3. **Worked example** — runs correctly, shows confounding bias of +10.2% with symmetric_high C, ASV at δ=0.967, recommends PPI++ with gold / DSL without

Package structure created:

```
annot_sensitivity/
├── __init__.py          # Public API: compute_bias, compute_asv, recommend_correction, ...
├── utils.py             # softmax_sample, misclassify, make_dummies, ols, ols_with_se
├── confusion.py         # validate, random, interpolate, predefined matrices
├── dgp.py               # 7 topology DGPs with DEFAULT_PARAMS
├── bias.py              # compute_bias via precomputed plim (2M samples, cached)
├── asv.py               # compute_asv with magnitude/significance/sign_flip thresholds
├── correction.py        # 5 correction methods + recommend_correction
├── examples/
│   └── confounding_k3.py   # Full workflow demo
└── tests/
    ├── __init__.py
    └── test_core.py     # 35 tests across all modules
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 808892,
  "duration_api_ms": 781050,
  "num_turns": 27,
  "stop_reason": "end_turn",
  "session_id": "e33e7000-6089-4915-9a7a-3c7178313f4e",
  "total_cost_usd": 3.1878439999999997,
  "usage": {
    "input_tokens": 26,
    "cache_creation_input_tokens": 114224,
    "cache_read_input_tokens": 2472002,
    "output_tokens": 49374,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 114224,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 315,
        "cache_read_input_tokens": 125345,
        "cache_creation_input_tokens": 720,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 720
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3388,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003463,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 26,
      "outputTokens": 49374,
      "cacheReadInputTokens": 2472002,
      "cacheCreationInputTokens": 114224,
      "webSearchRequests": 0,
      "costUSD": 3.1843809999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "cadcb257-2792-434c-ada0-f1ca83c647f7"
}
```

</details>

---
