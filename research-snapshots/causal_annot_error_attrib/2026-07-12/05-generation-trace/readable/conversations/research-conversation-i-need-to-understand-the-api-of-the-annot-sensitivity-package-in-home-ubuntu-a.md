# Research conversation: I need to understand the API of the `annot_sensitivity` package in `/home/ubuntu/.agent-ml-research-prod_0510/projects/c

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a57cdec08a0b4a571.jsonl`
- **Structured JSON:** [`6d2648a0e7052c92cabb.json`](../../sessions/6d/6d2648a0e7052c92cabb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-23T14:34:55.639Z_

I need to understand the API of the `annot_sensitivity` package in `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/`. 

Read the following files fully:
1. `annot_sensitivity/correction.py` — especially `correct_ppi`, `correct_naive_plugin`, `correct_mcsimex`, `correct_mla` signatures and docstrings
2. `annot_sensitivity/asv.py` — all functions, especially how ASV is computed
3. `annot_sensitivity/utils.py` — `misclassify`, `make_dummies`, `ols`, `ols_with_se`
4. `annot_sensitivity/bias.py` — plim functions

For each function, report its full signature (all parameters with defaults) and a one-line description. Also note any imports or dependencies between them.

Also check `annot_sensitivity/__init__.py` for any re-exports.

Be very thorough — read each file completely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "931f36b2-6e79-486e-89c9-9074426aeee2",
  "agentId": "a57cdec08a0b4a571",
  "type": "user",
  "uuid": "fed70d79-96f2-458e-87a3-612012297bee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-23T14:34:56.900Z_

I'll thoroughly read the `annot_sensitivity` package to understand its API. Let me start by reading the key files you mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fed70d79-96f2-458e-87a3-612012297bee",
  "isSidechain": true,
  "agentId": "a57cdec08a0b4a571",
  "requestId": "req_011CbKfdrptJxH12sXz8T7rw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6ee245c0-db7d-492d-a50e-8f7d93869b01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CBeWS1M74oDQRoHzsiVvPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17997,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17997,
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

_source line 3 · 2026-05-23T14:34:57.150Z_

<details open><summary>🔧 Tool call — Read · `toolu_0155AMeew8JPzmvqoDV4DhJH`</summary>

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
  "parentUuid": "6ee245c0-db7d-492d-a50e-8f7d93869b01",
  "isSidechain": true,
  "agentId": "a57cdec08a0b4a571",
  "requestId": "req_011CbKfdrptJxH12sXz8T7rw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1bb1edf2-d15a-4a6d-8616-7df6ad73f05c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CBeWS1M74oDQRoHzsiVvPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17997,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17997,
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

_source line 4 · 2026-05-23T14:34:57.168Z_

<details><summary>↩ Tool result · `toolu_0155AMeew8JPzmvqoDV4DhJH`</summary>

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
  "parentUuid": "1bb1edf2-d15a-4a6d-8616-7df6ad73f05c",
  "isSidechain": true,
  "promptId": "931f36b2-6e79-486e-89c9-9074426aeee2",
  "agentId": "a57cdec08a0b4a571",
  "type": "user",
  "uuid": "8d1a501c-571c-4804-a839-a605bcae1527",
  "sourceToolAssistantUUID": "1bb1edf2-d15a-4a6d-8616-7df6ad73f05c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T14:34:57.355Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G9qgXSpEi6rdQT7ZCY3aP3`</summary>

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
  "parentUuid": "8d1a501c-571c-4804-a839-a605bcae1527",
  "isSidechain": true,
  "agentId": "a57cdec08a0b4a571",
  "requestId": "req_011CbKfdrptJxH12sXz8T7rw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b273f8ce-2843-4e2a-bf8b-bf3c511befde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CBeWS1M74oDQRoHzsiVvPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17997,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17997,
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

_source line 6 · 2026-05-23T14:34:57.364Z_

<details><summary>↩ Tool result · `toolu_01G9qgXSpEi6rdQT7ZCY3aP3`</summary>

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
  "parentUuid": "b273f8ce-2843-4e2a-bf8b-bf3c511befde",
  "isSidechain": true,
  "promptId": "931f36b2-6e79-486e-89c9-9074426aeee2",
  "agentId": "a57cdec08a0b4a571",
  "type": "user",
  "uuid": "ab35aaf1-e32e-41eb-9c9a-54eae16099bf",
  "sourceToolAssistantUUID": "b273f8ce-2843-4e2a-bf8b-bf3c511befde",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T14:34:57.566Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MZTZ37eubk2LSHor4rK9un`</summary>

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
  "parentUuid": "ab35aaf1-e32e-41eb-9c9a-54eae16099bf",
  "isSidechain": true,
  "agentId": "a57cdec08a0b4a571",
  "requestId": "req_011CbKfdrptJxH12sXz8T7rw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fd11a8e6-3ab3-4e58-b427-c5706a057ecf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CBeWS1M74oDQRoHzsiVvPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17997,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17997,
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

_source line 8 · 2026-05-23T14:34:57.575Z_

<details><summary>↩ Tool result · `toolu_01MZTZ37eubk2LSHor4rK9un`</summary>

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
  "parentUuid": "fd11a8e6-3ab3-4e58-b427-c5706a057ecf",
  "isSidechain": true,
  "promptId": "931f36b2-6e79-486e-89c9-9074426aeee2",
  "agentId": "a57cdec08a0b4a571",
  "type": "user",
  "uuid": "f5a4a771-cdb6-444f-bf66-2d6ded3ab836",
  "sourceToolAssistantUUID": "fd11a8e6-3ab3-4e58-b427-c5706a057ecf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T14:34:57.777Z_

<details open><summary>🔧 Tool call — Read · `toolu_015yYE2MjTErfLA93MKVGZYU`</summary>

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
  "parentUuid": "f5a4a771-cdb6-444f-bf66-2d6ded3ab836",
  "isSidechain": true,
  "agentId": "a57cdec08a0b4a571",
  "requestId": "req_011CbKfdrptJxH12sXz8T7rw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "47cb6c6d-2a3e-4932-b201-4bc4ee7f13d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CBeWS1M74oDQRoHzsiVvPe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17997,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17997,
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

_source line 10 · 2026-05-23T14:34:57.783Z_

<details><summary>↩ Tool result · `toolu_015yYE2MjTErfLA93MKVGZYU`</summary>

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
  "parentUuid": "47cb6c6d-2a3e-4932-b201-4bc4ee7f13d2",
  "isSidechain": true,
  "promptId": "931f36b2-6e79-486e-89c9-9074426aeee2",
  "agentId": "a57cdec08a0b4a571",
  "type": "user",
  "uuid": "5770734b-3ed9-492b-a280-e265ec6d333b",
  "sourceToolAssistantUUID": "47cb6c6d-2a3e-4932-b201-4bc4ee7f13d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T14:34:57.981Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G5bT6wjGxDHky7Qvxdpskb`</summary>

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
  "parentUuid": "5770734b-3ed9-492b-a280-e265ec6d333b",
  "isSidechain": true,
  "agentId": "a57cdec08a0b4a571",
  "requestId": "req_011CbKfdrptJxH12sXz8T7rw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b4369e32-f524-4663-b742-926458e6cf38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CBeWS1M74oDQRoHzsiVvPe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17997,
      "cache_read_input_tokens": 0,
      "output_tokens": 407,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17997
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 407,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17997,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17997,
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

_source line 12 · 2026-05-23T14:34:57.987Z_

<details><summary>↩ Tool result · `toolu_01G5bT6wjGxDHky7Qvxdpskb`</summary>

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
56	    if topology == "iv":
57	        Z = data["Z"]
58	        Zc = Z - Z.mean()
59	        var_Z = (Zc ** 2).mean()
60	        stats["RF"] = (Zc * (Y - Y.mean())).mean() / var_Z
61	        FS = np.zeros(K)
62	        for k in range(K):
63	            FS[k] = (Zc * (DA[:, k] - DA[:, k].mean())).mean() / var_Z
64	        stats["FS"] = FS
65	
66	    _precomp_cache[cache_key] = stats
67	    return stats
68	
69	
70	def _plim_with_T(C, stats, K):
71	    """OLS plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}."""
72	    ds = C @ stats["E_DA"]
73	    dst = C @ stats["E_DA_T"]
74	    dsy = C @ stats["E_DA_Y"]
75	    ET, ET2 = stats["E_T"], stats["E_T2"]
76	    EY, ETY = stats["E_Y"], stats["E_TY"]
77	
78	    dim = 1 + K  # intercept + T + (K-1) dummies
79	    EZZ = np.zeros((dim, dim))
80	    EZZ[0, 0] = 1.0
81	    EZZ[0, 1] = EZZ[1, 0] = ET
82	    EZZ[1, 1] = ET2
83	    for j in range(1, K):
84	        idx = j + 1
85	        EZZ[0, idx] = EZZ[idx, 0] = ds[j]
86	        EZZ[1, idx] = EZZ[idx, 1] = dst[j]
87	        EZZ[idx, idx] = ds[j]
88	
89	    EZY = np.zeros(dim)
90	    EZY[0] = EY
91	    EZY[1] = ETY
92	    for j in range(1, K):
93	        EZY[j + 1] = dsy[j]
94	
95	    cond = np.linalg.cond(EZZ)
96	    if cond > 1e12:
97	        warnings.warn(
98	            f"EZZ condition number {cond:.1e} — plim may be numerically unstable"
99	        )
100	
101	    return np.linalg.solve(EZZ, EZY)
102	
103	
104	def _plim_no_T(C, stats, K):
105	    """OLS plim for Y ~ 1 + D*_1 + ... + D*_{K-1}."""
106	    ds = C @ stats["E_DA"]
107	    dsy = C @ stats["E_DA_Y"]
108	    EY = stats["E_Y"]
109	
110	    dim = K  # intercept + (K-1) dummies
111	    EZZ = np.zeros((dim, dim))
112	    EZZ[0, 0] = 1.0
113	    for j in range(1, K):
114	        EZZ[0, j] = EZZ[j, 0] = ds[j]
115	        EZZ[j, j] = ds[j]
116	
117	    EZY = np.zeros(dim)
118	    EZY[0] = EY
119	    for j in range(1, K):
120	        EZY[j] = dsy[j]
121	
122	    cond = np.linalg.cond(EZZ)
123	    if cond > 1e12:
124	        warnings.warn(
125	            f"EZZ condition number {cond:.1e} — plim may be numerically unstable"
126	        )
127	
128	    return np.linalg.solve(EZZ, EZY)
129	
130	
131	def _plim_iv(C, stats, K):
132	    """Wald estimator plim: RF / (C @ FS)[1]."""
133	    FS_star = C @ stats["FS"]
134	    denom = FS_star[1]
135	    if abs(denom) < 1e-15:
136	        return np.nan
137	    return stats["RF"] / denom
138	
139	
140	def _get_tau(topology, C, stats, K):
141	    """Extract target coefficient from plim vector.
142	
143	    For IV: Wald estimator RF / (C @ FS)[1].
144	    For topologies with T: OLS coefficient index 1 (treatment effect).
145	    For topologies without T: OLS coefficient index 1 (first dummy).
146	    """
147	    if topology == "iv":
148	        return _plim_iv(C, stats, K)
149	    if topology in HAS_TREATMENT:
150	        coefs = _plim_with_T(C, stats, K)
151	    else:
152	        coefs = _plim_no_T(C, stats, K)
153	    return coefs[1]
154	
155	
156	def compute_bias(topology, C, params=None):
157	    """Compute annotation-error bias for a given topology and confusion matrix.
158	
159	    Args:
160	        topology: one of "confounding", "mediation", "collider", "exposure",
161	                  "mbias", "iv", "frontdoor"
162	        C: (K, K) column-stochastic confusion matrix, C[j,i] = P(A*=j|A=i)
163	        params: optional DGP parameters dict, None uses defaults
164	
165	    Returns:
166	        dict with tau_true, tau_biased, bias, bias_pct, topology
167	    """
168	    if topology not in TOPOLOGIES:
169	        raise ValueError(f"Unknown topology: {topology}. Choose from {TOPOLOGIES}")
170	    if not validate_confusion_matrix(C):
171	        raise ValueError("C must be a square, non-negative, column-stochastic matrix")
172	
173	    K = C.shape[0]
174	    merged = dict(DEFAULT_PARAMS[topology])
175	    if params is not None:
176	        merged.update(params)
177	
178	    stats = _precompute(topology, merged, K)
179	    tau_true = _get_tau(topology, np.eye(K), stats, K)
180	    tau_biased = _get_tau(topology, C, stats, K)
181	    bias = tau_biased - tau_true
182	    bias_pct = 100.0 * bias / tau_true if abs(tau_true) > 1e-12 else float("nan")
183	
184	    return {
185	        "tau_true": float(tau_true),
186	        "tau_biased": float(tau_biased),
187	        "bias": float(bias),
188	        "bias_pct": float(bias_pct),
189	        "topology": topology,
190	    }
191	
192	
193	def clear_cache():
194	    """Clear the precomputed statistics cache."""
195	    _precomp_cache.clear()
196	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b4369e32-f524-4663-b742-926458e6cf38",
  "isSidechain": true,
  "promptId": "931f36b2-6e79-486e-89c9-9074426aeee2",
  "agentId": "a57cdec08a0b4a571",
  "type": "user",
  "uuid": "7eb15c92-28ba-4507-bf9a-1493dcbd460f",
  "sourceToolAssistantUUID": "b4369e32-f524-4663-b742-926458e6cf38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-23T14:35:26.131Z_

Perfect! I have read all the key files. Let me compile a comprehensive API reference for the `annot_sensitivity` package.

## API Reference: `annot_sensitivity` Package

### File: `annot_sensitivity/__init__.py`
**Re-exports (Public API):**
- `compute_bias` (from `.bias`)
- `compute_asv` (from `.asv`)
- `recommend_correction` (from `.correction`)
- `correct_naive_plugin`, `correct_dsl`, `correct_ppi`, `correct_mcsimex`, `correct_mla` (from `.correction`)
- `clear_cache` (from `.bias`)
- `METHODS` (from `.correction`)
- `validate_confusion_matrix`, `random_confusion_matrix`, `interpolate_confusion`, `predefined_matrices`, `delta_range` (from `.confusion`)
- `generate_data`, `TOPOLOGIES`, `DEFAULT_PARAMS`, `GEN_FUNCS` (from `.dgp`)
- `ols`, `ols_with_se`, `make_dummies`, `softmax_sample`, `misclassify` (from `.utils`)

---

### File: `annot_sensitivity/correction.py`

**Module Constants:**
- `METHODS = ["naive_plugin", "dsl", "ppi", "mcsimex", "mla"]`

**Functions:**

1. **`correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1)`**
   - Correct using C^{-1} applied per-observation to dummy indicators (reference category dropped)
   - Returns: `(tau_hat, se, success)` tuple of floats and bool

2. **`correct_dsl(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1)`**
   - EM-based joint estimation of regression parameters and confusion matrix C
   - Returns: `(tau_hat, se, success)` tuple

3. **`correct_ppi(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1, rng=None)`**
   - PPI++ with bootstrap lambda tuning using gold-standard labels
   - Returns: `(tau_hat, se, success)` tuple

4. **`correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=None)`**
   - MC-SIMEX: add extra misclassification at levels [0.5, 1.0, 1.5, 2.0], extrapolate quadratically to lambda=-1
   - Returns: `(tau_hat, se, success)` tuple

5. **`correct_mla(X_other, Y, Astar, C, tau_idx=1)`**
   - Matrix-based label adjustment: D_corrected = D_full @ C^{-1}, drop reference category
   - Returns: `(tau_hat, se, success)` tuple

6. **`recommend_correction(topology, C, has_gold=False, gold_fraction=0.1)`**
   - Recommend the best correction method based on topology and data availability
   - Returns: dict with keys `{"recommended", "ranking", "notes"}`

**Key Module Notes:**
- `_EM_MAX_ITER = 100`, `_EM_TOL = 1e-6` (DSL parameters)
- `_SIMEX_LAMBDAS = [0.5, 1.0, 1.5, 2.0]`, `_SIMEX_B = 50` (MC-SIMEX parameters)
- All correction functions follow pattern: (X_other, Y, Astar, ...) → (float, float, bool)
- FWL theorem note: `naive_plugin` and `mla` only correct dummy coefficients, NOT treatment coefficient when treatment is separate
- Imports: `numpy`, `ols`, `ols_with_se`, `make_dummies`, `make_full_dummies`, `misclassify` from utils

---

### File: `annot_sensitivity/asv.py`

**Functions:**

1. **`_compute_bias_curve(topology, C0, stats, K, tau_true, n_grid=1500)`**
   - Compute absolute bias along C(delta) interpolation path
   - Returns: `(deltas, bias_abs, tau_curve)` arrays

2. **`_compute_envelope(bias_abs)`**
   - Running maximum of absolute bias (for threshold crossing detection)
   - Returns: `(n_grid,)` envelope array

3. **`_find_threshold_crossing(envelope, deltas, tau_curve, tau_true, threshold_type, threshold_value)`**
   - Find delta where bias envelope crosses threshold
   - `threshold_type` in `{"magnitude", "significance", "sign_flip"}`
   - Returns: `float` delta or `None`

4. **`compute_asv(topology, C0, params=None, threshold_type="magnitude", threshold_value=0.1, n_grid=1500)`**
   - Compute Annotation Sensitivity Value: minimum delta at which bias threshold is crossed
   - Returns: dict with keys `{"asv", "bias_curve", "envelope", "deltas", "tau_true"}`

**Key Module Notes:**
- ASV measures robustness of causal inference to annotation error
- Uses interpolation path: C(delta) = (1-delta)*I + delta*C0
- Imports: `_precompute`, `_get_tau` from bias; `validate_confusion_matrix`, `interpolate_confusion`, `delta_range` from confusion; DEFAULT_PARAMS, TOPOLOGIES from dgp

---

### File: `annot_sensitivity/utils.py`

**Functions:**

1. **`softmax_sample(logits, rng)`**
   - Sample categorical variable from row-wise softmax probabilities
   - Args: `logits` (N, K), `rng` numpy Generator
   - Returns: `(N,)` integer array in {0, ..., K-1}

2. **`misclassify(A, C, rng)`**
   - Apply misclassification: A*_i ~ Cat(C[:, A_i]) using confusion matrix C
   - Args: `A` (N,) true labels, `C` (K, K) column-stochastic, `rng` Generator
   - Returns: `(N,)` misclassified labels

3. **`make_dummies(A, K=None)`**
   - Create K-1 dummy variables with reference category 0
   - Args: `A` (N,) labels in {0, ..., K-1}, `K` inferred from A.max()+1 if None
   - Returns: `(N, K-1)` dummy matrix

4. **`make_full_dummies(A, K=None)`**
   - Create full K one-hot encoding (all K categories)
   - Args: `A` (N,) labels, `K` optional
   - Returns: `(N, K)` one-hot matrix

5. **`ols(X, Y)`**
   - OLS point estimate via least-squares (numpy.linalg.lstsq)
   - Args: `X` (N, p) design matrix, `Y` (N,) response
   - Returns: `(p,)` coefficient vector

6. **`ols_with_se(X, Y)`**
   - OLS point estimate with homoskedastic standard errors
   - Args: `X` (N, p), `Y` (N,)
   - Returns: `(beta, se)` tuple of (p,) arrays

**Key Module Notes:**
- All sampling uses numpy random Generator (RNG) interface
- No imports beyond numpy

---

### File: `annot_sensitivity/bias.py`

**Module Constants:**
- `_N_PRECOMP = 2_000_000` (sample size for precomputation)
- `_precomp_cache = {}` (global cache for sufficient statistics)

**Functions:**

1. **`_params_key(params)`**
   - Convert parameter dict to hashable tuple key for caching
   - Returns: `tuple`

2. **`_precompute(topology, params, K, seed=999)`**
   - Precompute sufficient statistics from large-sample DGP simulations
   - Returns: dict with keys `E_Y`, `E_DA`, `E_DA_Y`, and optionally `E_T`, `E_T2`, `E_TY`, `E_DA_T`, `RF`, `FS`

3. **`_plim_with_T(C, stats, K)`**
   - OLS plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}
   - Returns: `(1+K,)` coefficient vector

4. **`_plim_no_T(C, stats, K)`**
   - OLS plim for Y ~ 1 + D*_1 + ... + D*_{K-1}
   - Returns: `(K,)` coefficient vector

5. **`_plim_iv(C, stats, K)`**
   - Wald estimator plim: RF / (C @ FS)[1]
   - Returns: `float` or `np.nan`

6. **`_get_tau(topology, C, stats, K)`**
   - Extract target coefficient from plim vector
   - For IV: Wald estimator; for others: coefficient at index 1
   - Returns: `float`

7. **`compute_bias(topology, C, params=None)`**
   - Compute annotation-error bias for a given topology and confusion matrix C
   - Returns: dict with keys `{"tau_true", "tau_biased", "bias", "bias_pct", "topology"}` (all floats)

8. **`clear_cache()`**
   - Clear the precomputed statistics cache
   - Returns: `None`

**Key Module Notes:**
- Plim calculations avoid Monte Carlo by using precomputed sufficient statistics from N=2M samples
- Condition number warnings logged if EZZ is poorly conditioned (cond > 1e12)
- Imports: `warnings`, `numpy`, DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES from dgp; `validate_confusion_matrix` from confusion

---

### Cross-Function Dependencies

```
correction.py
  ↓ uses
  ├─ utils: ols, ols_with_se, make_dummies, make_full_dummies, misclassify
  └─ (returns tau_hat, se, success tuples)

asv.py
  ↓ uses
  ├─ bias: _precompute, _get_tau
  ├─ confusion: validate_confusion_matrix, interpolate_confusion, delta_range
  ├─ dgp: DEFAULT_PARAMS, TOPOLOGIES
  └─ (returns asv dict with bias_curve, envelope, deltas, tau_true)

bias.py
  ↓ uses
  ├─ dgp: DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES
  ├─ confusion: validate_confusion_matrix
  └─ (returns tau_true, tau_biased, bias, bias_pct as floats)

utils.py
  ↓ standalone
  └─ (no dependencies on other annot_sensitivity modules)
```

---

### Summary: Function Signatures at a Glance

**Correction Methods** (all return `(tau_hat: float, se: float, success: bool)`)
- `correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1)`
- `correct_dsl(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1)`
- `correct_ppi(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1, rng=None)`
- `correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=None)`
- `correct_mla(X_other, Y, Astar, C, tau_idx=1)`

**Main API Functions**
- `compute_bias(topology, C, params=None)` → dict
- `compute_asv(topology, C0, params=None, threshold_type="magnitude", threshold_value=0.1, n_grid=1500)` → dict
- `recommend_correction(topology, C, has_gold=False, gold_fraction=0.1)` → dict

**Utilities**
- `ols(X, Y)` → (p,) coefficients
- `ols_with_se(X, Y)` → ((p,), (p,)) coefficients and standard errors
- `make_dummies(A, K=None)` → (N, K-1) dummies
- `make_full_dummies(A, K=None)` → (N, K) one-hot
- `misclassify(A, C, rng)` → (N,) misclassified labels
- `softmax_sample(logits, rng)` → (N,) sampled categories

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7eb15c92-28ba-4507-bf9a-1493dcbd460f",
  "isSidechain": true,
  "agentId": "a57cdec08a0b4a571",
  "requestId": "req_011CbKfe2x6NduV5ahWJt5Rk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5b5cff34-955d-424d-b063-69afa2f7b6a0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "sessionId": "a1e14e23-41f7-42b4-ac49-b035326a4af4",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ku4MocxtVwL7TpqirLMgr6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 13113,
      "cache_read_input_tokens": 17997,
      "output_tokens": 3238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13113
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3238,
          "cache_read_input_tokens": 17997,
          "cache_creation_input_tokens": 13113,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13113,
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
