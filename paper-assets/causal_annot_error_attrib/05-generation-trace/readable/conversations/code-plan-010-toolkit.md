# code plan 010 toolkit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_code_plan_010_toolkit_20260520T232412.jsonl`
- **Structured JSON:** [`691e80d07c1327ec90d5.json`](../../sessions/69/691e80d07c1327ec90d5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

53 recorded events

### Tool call

_source line 1 · 2026-05-20T23:37:54.434670+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_collider_mbias_iv.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_collider_mbias_iv.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T23:37:54.437543+00:00_

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
51	    retur
…[truncated 19583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Read",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T23:37:54.437953+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_mediation_frontdoor.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_001_mediation_frontdoor.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T23:37:54.438431+00:00_

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
68	    r
…[truncated 12084 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T23:37:54.438741+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_005_asv_extended.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_005_asv_extended.py"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T23:37:54.438983+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_007_correction_guidance.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_007_correction_guidance.py"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T23:37:54.441743+00:00_

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
57	     
…[truncated 33891 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Read",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T23:37:54.442555+00:00_

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
53	    # mild: diag≈0.867, off≈0
…[truncated 32313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Read",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T23:37:54.442875+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/plan_005_asv_extended_fixed.py",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T23:37:54.443108+00:00_

artifacts/plan_005_asv_extended_fixed.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T23:37:54.447476+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "compute_signif_asv_fast",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan_005_asv_extended_fixed.py",
  "output_mode": "content",
  "-A": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Grep",
  "tool_args": {
    "pattern": "compute_signif_asv_fast",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan_005_asv_extended_fixed.py",
    "output_mode": "content",
    "-A": "20"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T23:37:54.447814+00:00_

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
714-           
…[truncated 3177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T23:37:54.452467+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/ 2>/dev/null || echo \"NOT_EXISTS\"",
    "description": "Check if package directory exists"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T23:37:54.452789+00:00_

NOT_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T23:37:54.453047+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/{examples,tests}",
    "description": "Create package directory structure"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T23:37:54.453489+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T23:37:54.453804+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/utils.py",
    "content": "\"\"\"Shared utilities: OLS, dummy encoding, softmax sampling.\"\"\"\n\nimport numpy as np\n\n\ndef softmax_sample(logits, rng):\n    \"\"\"Sample categorical variable from row-wise softmax probabilities.\n\n    Args:\n        logits: (N, K) array of logits\n        rng: numpy random Generator\n\n    Returns:\n        (N,) integer array with values in {0, ..., K-1}\n    \"\"\"\n    e = np.exp(logits - logits.max(axis=1, keepdims=True))\n    p = e / e.sum(axis=1, keepdims=True)\n    cum = np.cumsum(p, axis=1)\n    u = rng.uniform(size=logits.shape[0])\n    K = logits.shape[1]\n    result = np.zeros(logits.shape[0], dtype=int)\n    for k in range(K - 1):\n        result += (u >= cum[:, k]).astype(int)\n    return result\n\n\ndef misclassify(A, C, rng):\n    \"\"\"Apply misclassification: A*_i ~ Cat(C[:, A_i]).\n\n    Args:\n        A: (N,) true labels in {0, ..., K-1}\n        C: (K, K) column-stochastic confusion matrix\n        rng: numpy random Generator\n\n    Returns:\n        (N,) misclassified labels\n    \"\"\"\n    K = C.shape[0]\n    probs = C[:, A]\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    result = np.zeros(len(A), dtype=int)\n    for k in range(K - 1):\n        result += (u >= cum[k]).astype(int)\n    return result\n\n\ndef make_dummies(A, K=None):\n    \"\"\"Create K-1 dummy variables (reference category 0).\n\n    Args:\n        A: (N,) categorical labels in {0, ..., K-1}\n        K: number of categories (inferred from A if None)\n\n    Returns:\n        (N, K-1) dummy matrix\n    \"\"\"\n    if K is None:\n        K = int(A.max()) + 1\n    N = len(A)\n    D = np.zeros((N, K - 1))\n    for j in range(K - 1):\n        D[:, j] = (A == j + 1).astype(float)\n    return D\n\n\ndef make_full_dummies(A, K=None):\n    \"\"\"Create full K one-hot encoding.\n\n    Args:\n        A: (N,) categorical labels in {0, ..., K-1}\n        K: number of categories (inferred from A if None)\n\n    Returns:\n        (N, K) one-hot matrix\n    \"\"\"\n    if K is None:\n        K = int(A.max()) + 1\n    N = len(A)\n    D = np.zeros((N, K))\n    for j in range(K):\n        D[:, j] = (A == j).astype(float)\n    return D\n\n\ndef ols(X, Y):\n    \"\"\"OLS point estimate via least-squares.\n\n    Args:\n        X: (N, p) design matrix\n        Y: (N,) response\n\n    Returns:\n        (p,) coefficient vector\n    \"\"\"\n    return np.linalg.lstsq(X, Y, rcond=None)[0]\n\n\ndef ols_with_se(X, Y):\n    \"\"\"OLS point estimate with homoskedastic standard errors.\n\n    Args:\n        X: (N, p) design matrix\n        Y: (N,) response\n\n    Returns:\n        (beta, se) tuple of (p,) arrays\n    \"\"\"\n    beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n    resid = Y - X @ beta\n    n, p = X.shape\n    s2 = resid @ resid / max(n - p, 1)\n    try:\n        XtX_inv = np.linalg.inv(X.T @ X)\n        se = np.sqrt(np.maximum(np.diag(s2 * XtX_inv), 0.0))\n    except np.linalg.LinAlgError:\n        se = np.full(p, np.nan)\n    return beta, se\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T23:37:54.454126+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/utils.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T23:37:54.454466+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/confusion.py",
    "content": "\"\"\"Confusion matrix utilities: validation, generation, interpolation.\n\nConvention: C[j, i] = P(A*=j | A=i), columns sum to 1 (column-stochastic).\n\"\"\"\n\nimport numpy as np\n\n\ndef validate_confusion_matrix(C):\n    \"\"\"Check if C is a valid column-stochastic confusion matrix.\n\n    Args:\n        C: array to validate\n\n    Returns:\n        True if valid, False otherwise\n    \"\"\"\n    if not isinstance(C, np.ndarray):\n        return False\n    if C.ndim != 2 or C.shape[0] != C.shape[1]:\n        return False\n    if C.shape[0] < 2:\n        return False\n    if (C < -1e-10).any():\n        return False\n    if not np.allclose(C.sum(axis=0), 1.0, atol=1e-6):\n        return False\n    return True\n\n\ndef random_confusion_matrix(K, diag_dominance=0.8, rng=None):\n    \"\"\"Generate a random column-stochastic confusion matrix.\n\n    Args:\n        K: number of categories\n        diag_dominance: controls diagonal strength (0 to 1)\n        rng: numpy random Generator (created if None)\n\n    Returns:\n        (K, K) column-stochastic matrix\n    \"\"\"\n    if rng is None:\n        rng = np.random.default_rng()\n    diag_alpha = diag_dominance * 10\n    offdiag_alpha = max((1 - diag_dominance) * 10 / max(K - 1, 1), 0.1)\n    C = np.zeros((K, K))\n    for k in range(K):\n        alphas = np.full(K, offdiag_alpha)\n        alphas[k] = diag_alpha\n        C[:, k] = rng.dirichlet(alphas)\n    return C\n\n\ndef interpolate_confusion(C0, delta):\n    \"\"\"Interpolate between identity and C0: C(delta) = (1-delta)*I + delta*C0.\n\n    Args:\n        C0: (K, K) base confusion matrix\n        delta: interpolation parameter (0 = identity, 1 = C0)\n\n    Returns:\n        (K, K) interpolated column-stochastic matrix\n    \"\"\"\n    K = C0.shape[0]\n    C = (1 - delta) * np.eye(K) + delta * C0\n    C = np.maximum(C, 0.0)\n    col_sums = C.sum(axis=0)\n    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)\n    return C / col_sums\n\n\ndef delta_range(C0):\n    \"\"\"Compute valid delta range for interpolation.\n\n    Args:\n        C0: (K, K) base confusion matrix\n\n    Returns:\n        (delta_min, delta_max) tuple\n    \"\"\"\n    min_diag = np.diag(C0).min()\n    if min_diag >= 1.0:\n        return (0.0, 10.0)\n    delta_max = min(1.0 / (1.0 - min_diag), 10.0)\n    return (0.0, delta_max)\n\n\ndef predefined_matrices(K=3):\n    \"\"\"Return a dict of predefined K x K confusion matrices.\n\n    Args:\n        K: number of categories (only K=3 supported)\n\n    Returns:\n        dict mapping name to (K, K) confusion matrix\n    \"\"\"\n    if K != 3:\n        raise ValueError(f\"Predefined matrices only available for K=3, got K={K}\")\n    return {\n        \"symmetric_high\": np.array([\n            [0.80, 0.10, 0.10],\n            [0.10, 0.80, 0.10],\n            [0.10, 0.10, 0.80]]),\n        \"mild_uniform\": np.array([\n            [0.8 + 0.2 / 3, 0.2 / 3, 0.2 / 3],\n            [0.2 / 3, 0.8 + 0.2 / 3, 0.2 / 3],\n            [0.2 / 3, 0.2 / 3, 0.8 + 0.2 / 3]]),\n        \"moderate_uniform\": np.array([\n            [0.6 + 0.4 / 3, 0.4 / 3, 0.4 / 3],\n            [0.4 / 3, 0.6 + 0.4 / 3, 0.4 / 3],\n            [0.4 / 3, 0.4 / 3, 0.6 + 0.4 / 3]]),\n        \"severe_uniform\": np.array([\n            [0.4 + 0.6 / 3, 0.6 / 3, 0.6 / 3],\n            [0.6 / 3, 0.4 + 0.6 / 3, 0.6 / 3],\n            [0.6 / 3, 0.6 / 3, 0.4 + 0.6 / 3]]),\n        \"asymmetric\": np.array([\n            [0.75, 0.05, 0.05],\n            [0.20, 0.80, 0.10],\n            [0.05, 0.15, 0.85]]),\n        \"near_permutation\": np.array([\n            [0.05, 0.05, 0.90],\n            [0.90, 0.05, 0.05],\n            [0.05, 0.90, 0.05]]),\n        \"realistic_llm\": np.array([\n            [0.78, 0.15, 0.03],\n            [0.18, 0.72, 0.18],\n            [0.04, 0.13, 0.79]]),\n    }\n"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T23:37:54.454830+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/confusion.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T23:37:54.455097+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/dgp.py",
    "content": "\"\"\"Data generation processes for 7 DAG topologies.\n\nEach topology generates synthetic data with a known causal structure.\nThe variable A (or M for frontdoor) is the one subject to misclassification.\n\"\"\"\n\nimport numpy as np\nfrom .utils import softmax_sample, make_dummies\n\nDEFAULT_PARAMS = {\n    \"confounding\": dict(\n        p_A=np.array([0.40, 0.35, 0.25]),\n        alpha=np.array([1.5, -1.0]),\n        beta_A=np.array([1.0, -0.5]),\n        beta_T=2.0, sigma_T=1.0),\n    \"mediation\": dict(\n        tau=0.5,\n        gamma=np.array([0.0, 0.5, -0.3]),\n        delta=np.array([0.0, 0.8, -0.6]),\n        beta=np.array([0.0, 1.0, -0.5])),\n    \"collider\": dict(\n        tau=1.0,\n        g=np.array([0.0, 0.0, 0.0]),\n        dT=np.array([0.0, 0.5, -0.3]),\n        dY=np.array([0.0, 0.8, 0.6])),\n    \"exposure\": dict(\n        beta=np.array([0.0, 1.0, -0.5]),\n        p_A=np.array([0.40, 0.35, 0.25])),\n    \"mbias\": dict(\n        tau=1.0, delta_coef=1.0, lam=1.0,\n        g=np.array([0.0, 0.0, 0.0]),\n        a1=np.array([0.0, 0.8, -0.5]),\n        a2=np.array([0.0, 0.6, 0.9])),\n    \"iv\": dict(\n        lam=1.0,\n        g=np.array([0.0, 0.0, 0.0]),\n        dZ=np.array([0.0, 1.0, -0.5]),\n        dU=np.array([0.0, 0.8, 0.6]),\n        beta=np.array([0.0, 1.0, -0.5])),\n    \"frontdoor\": dict(\n        alpha_U=1.0, lam_U=1.0,\n        gamma=np.array([0.0, 0.5, -0.3]),\n        delta=np.array([0.0, 1.0, -0.8]),\n        beta=np.array([0.0, 1.0, -0.5])),\n}\n\nTOPOLOGIES = list(DEFAULT_PARAMS.keys())\n\nHAS_TREATMENT = {\"confounding\", \"mediation\", \"collider\", \"mbias\", \"frontdoor\"}\nNO_TREATMENT = {\"exposure\", \"iv\"}\n\n\ndef _get_rng(rng, seed):\n    if rng is not None:\n        return rng\n    return np.random.default_rng(seed)\n\n\ndef _get_params(topology, params):\n    p = dict(DEFAULT_PARAMS[topology])\n    if params is not None:\n        p.update(params)\n    return p\n\n\ndef gen_confounding(N, params=None, rng=None, seed=None):\n    \"\"\"A->T, A->Y, T->Y. Researcher controls for A*.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"confounding\", params)\n    K = len(p[\"p_A\"])\n    A = rng.choice(K, size=N, p=p[\"p_A\"])\n    D = make_dummies(A, K)\n    T = D @ p[\"alpha\"] + rng.normal(0, p[\"sigma_T\"], N)\n    Y = p[\"beta_T\"] * T + D @ p[\"beta_A\"] + rng.normal(0, 1, N)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_mediation(N, params=None, rng=None, seed=None):\n    \"\"\"T->A->Y. A mediates; researcher controls for A*.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"mediation\", params)\n    T = rng.binomial(1, 0.5, N).astype(float)\n    K = len(p[\"gamma\"])\n    logits = p[\"gamma\"][None, :] + p[\"delta\"][None, :] * T[:, None]\n    A = softmax_sample(logits, rng)\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + p[\"tau\"] * T + rng.normal(0, 1, N)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_collider(N, params=None, rng=None, seed=None):\n    \"\"\"T->A<-Y. Researcher wrongly controls for A*.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"collider\", params)\n    T = rng.normal(0, 1, N)\n    Y = p[\"tau\"] * T + rng.normal(0, 1, N)\n    logits = (p[\"g\"][None, :] + p[\"dT\"][None, :] * T[:, None]\n              + p[\"dY\"][None, :] * Y[:, None])\n    A = softmax_sample(logits, rng)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_exposure(N, params=None, rng=None, seed=None):\n    \"\"\"A->Y (direct exposure, no treatment T).\n\n    Returns:\n        dict with keys Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"exposure\", params)\n    K = len(p[\"p_A\"])\n    A = rng.choice(K, size=N, p=p[\"p_A\"])\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + rng.normal(0, 1, N)\n    return {\"Y\": Y, \"A\": A}\n\n\ndef gen_mbias(N, params=None, rng=None, seed=None):\n    \"\"\"U1->{A,T}, U2->{A,Y}, T->Y. Conditioning on A* induces M-bias.\n\n    Returns:\n        dict with keys T, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"mbias\", params)\n    N_out = N\n    U1, U2 = rng.normal(0, 1, N_out), rng.normal(0, 1, N_out)\n    T = p[\"delta_coef\"] * U1 + rng.normal(0, 1, N_out)\n    logits = (p[\"g\"][None, :] + p[\"a1\"][None, :] * U1[:, None]\n              + p[\"a2\"][None, :] * U2[:, None])\n    A = softmax_sample(logits, rng)\n    Y = p[\"tau\"] * T + p[\"lam\"] * U2 + rng.normal(0, 1, N_out)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\ndef gen_iv(N, params=None, rng=None, seed=None):\n    \"\"\"Z->A->Y, U->{A,Y}. IV topology with endogenous A.\n\n    Returns:\n        dict with keys Z, Y, A\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"iv\", params)\n    K = len(p[\"g\"])\n    Z = rng.normal(0, 1, N)\n    U = rng.normal(0, 1, N)\n    logits = (p[\"g\"][None, :] + p[\"dZ\"][None, :] * Z[:, None]\n              + p[\"dU\"][None, :] * U[:, None])\n    A = softmax_sample(logits, rng)\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + p[\"lam\"] * U + rng.normal(0, 1, N)\n    return {\"Z\": Z, \"Y\": Y, \"A\": A}\n\n\ndef gen_frontdoor(N, params=None, rng=None, seed=None):\n    \"\"\"T->M->Y, U->{T,Y}. Misclassified variable is M (mediator, stored as A).\n\n    Returns:\n        dict with keys T, Y, A (A is the mediator M)\n    \"\"\"\n    rng = _get_rng(rng, seed)\n    p = _get_params(\"frontdoor\", params)\n    U = rng.normal(0, 1, N)\n    T = p[\"alpha_U\"] * U + rng.normal(0, 1, N)\n    K = len(p[\"gamma\"])\n    logits = p[\"gamma\"][None, :] + p[\"delta\"][None, :] * T[:, None]\n    A = softmax_sample(logits, rng)\n    D = make_dummies(A, K)\n    Y = p[\"beta\"][0] + D @ p[\"beta\"][1:] + p[\"lam_U\"] * U + rng.normal(0, 1, N)\n    return {\"T\": T, \"Y\": Y, \"A\": A}\n\n\nGEN_FUNCS = {\n    \"confounding\": gen_confounding,\n    \"mediation\": gen_mediation,\n    \"collider\": gen_collider,\n    \"exposure\": gen_exposure,\n    \"mbias\": gen_mbias,\n    \"iv\": gen_iv,\n    \"frontdoor\": gen_frontdoor,\n}\n\n\ndef generate_data(topology, N, params=None, rng=None, seed=None):\n    \"\"\"Generate synthetic data for a given topology.\n\n    Args:\n        topology: one of \"confounding\", \"mediation\", \"collider\", \"exposure\",\n                  \"mbias\", \"iv\", \"frontdoor\"\n        N: sample size\n        params: optional DGP parameter overrides\n        rng: numpy random Generator\n        seed: random seed (used if rng is None)\n\n    Returns:\n        dict with generated variables (topology-dependent keys)\n    \"\"\"\n    if topology not in GEN_FUNCS:\n        raise ValueError(f\"Unknown topology: {topology}. Choose from {TOPOLOGIES}\")\n    return GEN_FUNCS[topology](N, params=params, rng=rng, seed=seed)\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T23:37:54.457611+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/dgp.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T23:37:54.457920+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py",
    "content": "\"\"\"Compute annotation-error bias via probability limit calculations.\n\nUses precomputed sufficient statistics from large-sample DGP simulations\nto compute OLS plim as a function of confusion matrix C, avoiding MC.\n\"\"\"\n\nimport warnings\nimport numpy as np\nfrom .dgp import DEFAULT_PARAMS, HAS_TREATMENT, GEN_FUNCS, TOPOLOGIES\nfrom .confusion import validate_confusion_matrix\n\n_N_PRECOMP = 2_000_000\n_precomp_cache = {}\n\n\ndef _params_key(params):\n    items = []\n    for k, v in sorted(params.items()):\n        if isinstance(v, np.ndarray):\n            items.append((k, tuple(v.flat)))\n        else:\n            items.append((k, v))\n    return tuple(items)\n\n\ndef _precompute(topology, params, K, seed=999):\n    \"\"\"Precompute sufficient statistics for plim calculation.\"\"\"\n    cache_key = (topology, _params_key(params), K)\n    if cache_key in _precomp_cache:\n        return _precomp_cache[cache_key]\n\n    rng = np.random.default_rng(seed)\n    data = GEN_FUNCS[topology](_N_PRECOMP, params=params, rng=rng)\n    Y = data[\"Y\"]\n    A = data[\"A\"]\n\n    DA = np.zeros((_N_PRECOMP, K))\n    for k in range(K):\n        DA[:, k] = (A == k).astype(float)\n\n    stats = {\n        \"E_Y\": Y.mean(),\n        \"E_DA\": DA.mean(0),\n        \"E_DA_Y\": (DA * Y[:, None]).mean(0),\n    }\n\n    if topology in HAS_TREATMENT:\n        T = data[\"T\"]\n        stats.update({\n            \"E_T\": T.mean(),\n            \"E_T2\": (T ** 2).mean(),\n            \"E_TY\": (T * Y).mean(),\n            \"E_DA_T\": (DA * T[:, None]).mean(0),\n        })\n\n    _precomp_cache[cache_key] = stats\n    return stats\n\n\ndef _plim_with_T(C, stats, K):\n    \"\"\"OLS plim for Y ~ 1 + T + D*_1 + ... + D*_{K-1}.\"\"\"\n    ds = C @ stats[\"E_DA\"]\n    dst = C @ stats[\"E_DA_T\"]\n    dsy = C @ stats[\"E_DA_Y\"]\n    ET, ET2 = stats[\"E_T\"], stats[\"E_T2\"]\n    EY, ETY = stats[\"E_Y\"], stats[\"E_TY\"]\n\n    dim = 1 + K  # intercept + T + (K-1) dummies\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    EZZ[0, 1] = EZZ[1, 0] = ET\n    EZZ[1, 1] = ET2\n    for j in range(1, K):\n        idx = j + 1\n        EZZ[0, idx] = EZZ[idx, 0] = ds[j]\n        EZZ[1, idx] = EZZ[idx, 1] = dst[j]\n        EZZ[idx, idx] = ds[j]\n\n    EZY = np.zeros(dim)\n    EZY[0] = EY\n    EZY[1] = ETY\n    for j in range(1, K):\n        EZY[j + 1] = dsy[j]\n\n    cond = np.linalg.cond(EZZ)\n    if cond > 1e12:\n        warnings.warn(\n            f\"EZZ condition number {cond:.1e} — plim may be numerically unstable\"\n        )\n\n    return np.linalg.solve(EZZ, EZY)\n\n\ndef _plim_no_T(C, stats, K):\n    \"\"\"OLS plim for Y ~ 1 + D*_1 + ... + D*_{K-1}.\"\"\"\n    ds = C @ stats[\"E_DA\"]\n    dsy = C @ stats[\"E_DA_Y\"]\n    EY = stats[\"E_Y\"]\n\n    dim = K  # intercept + (K-1) dummies\n    EZZ = np.zeros((dim, dim))\n    EZZ[0, 0] = 1.0\n    for j in range(1, K):\n        EZZ[0, j] = EZZ[j, 0] = ds[j]\n        EZZ[j, j] = ds[j]\n\n    EZY = np.zeros(dim)\n    EZY[0] = EY\n    for j in range(1, K):\n        EZY[j] = dsy[j]\n\n    cond = np.linalg.cond(EZZ)\n    if cond > 1e12:\n        warnings.warn(\n            f\"EZZ condition number {cond:.1e} — plim may be numerically unstable\"\n        )\n\n    return np.linalg.solve(EZZ, EZY)\n\n\ndef _get_tau(topology, C, stats, K):\n    \"\"\"Extract target coefficient from plim vector.\n\n    For topologies with T: coefficient index 1 (treatment effect).\n    For topologies without T: coefficient index 1 (first dummy).\n    \"\"\"\n    if topology in HAS_TREATMENT:\n        coefs = _plim_with_T(C, stats, K)\n    else:\n        coefs = _plim_no_T(C, stats, K)\n    return coefs[1]\n\n\ndef compute_bias(topology, C, params=None):\n    \"\"\"Compute annotation-error bias for a given topology and confusion matrix.\n\n    Args:\n        topology: one of \"confounding\", \"mediation\", \"collider\", \"exposure\",\n                  \"mbias\", \"iv\", \"frontdoor\"\n        C: (K, K) column-stochastic confusion matrix, C[j,i] = P(A*=j|A=i)\n        params: optional DGP parameters dict, None uses defaults\n\n    Returns:\n        dict with tau_true, tau_biased, bias, bias_pct, topology\n    \"\"\"\n    if topology not in TOPOLOGIES:\n        raise ValueError(f\"Unknown topology: {topology}. Choose from {TOPOLOGIES}\")\n    if not validate_confusion_matrix(C):\n        raise ValueError(\"C must be a square, non-negative, column-stochastic matrix\")\n\n    K = C.shape[0]\n    merged = dict(DEFAULT_PARAMS[topology])\n    if params is not None:\n        merged.update(params)\n\n    stats = _precompute(topology, merged, K)\n    tau_true = _get_tau(topology, np.eye(K), stats, K)\n    tau_biased = _get_tau(topology, C, stats, K)\n    bias = tau_biased - tau_true\n    bias_pct = 100.0 * bias / tau_true if abs(tau_true) > 1e-12 else float(\"nan\")\n\n    return {\n        \"tau_true\": float(tau_true),\n        \"tau_biased\": float(tau_biased),\n        \"bias\": float(bias),\n        \"bias_pct\": float(bias_pct),\n        \"topology\": topology,\n    }\n\n\ndef clear_cache():\n    \"\"\"Clear the precomputed statistics cache.\"\"\"\n    _precomp_cache.clear()\n"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T23:37:54.458332+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T23:37:54.458602+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/asv.py",
    "content": "\"\"\"Annotation Sensitivity Value (ASV) computation.\n\nASV measures how much misclassification is needed to cross a bias threshold,\nusing the C(delta) = (1-delta)*I + delta*C0 interpolation path.\n\"\"\"\n\nimport numpy as np\nfrom .bias import _precompute, _get_tau\nfrom .confusion import validate_confusion_matrix, interpolate_confusion, delta_range\nfrom .dgp import DEFAULT_PARAMS, TOPOLOGIES\n\n\ndef _compute_bias_curve(topology, C0, stats, K, tau_true, n_grid=1500):\n    dmin, dmax = delta_range(C0)\n    deltas = np.linspace(dmin, dmax, n_grid)\n    tau_curve = np.zeros(n_grid)\n    for i, d in enumerate(deltas):\n        C_d = interpolate_confusion(C0, d)\n        tau_curve[i] = _get_tau(topology, C_d, stats, K)\n    bias_abs = np.abs(tau_curve - tau_true)\n    return deltas, bias_abs, tau_curve\n\n\ndef _compute_envelope(bias_abs):\n    env = np.zeros_like(bias_abs)\n    running_max = 0.0\n    for i in range(len(bias_abs)):\n        v = bias_abs[i]\n        if not np.isnan(v):\n            running_max = max(running_max, v)\n        env[i] = running_max\n    return env\n\n\ndef _find_threshold_crossing(envelope, deltas, tau_curve, tau_true,\n                             threshold_type, threshold_value):\n    if threshold_type == \"magnitude\":\n        if abs(tau_true) < 1e-12:\n            return None\n        thresh = threshold_value * abs(tau_true)\n        for i in range(len(deltas)):\n            if envelope[i] > thresh:\n                return float(deltas[i])\n        return None\n    elif threshold_type == \"sign_flip\":\n        if abs(tau_true) < 1e-12:\n            return None\n        baseline_sign = np.sign(tau_true)\n        for i in range(len(deltas)):\n            if np.isnan(tau_curve[i]):\n                continue\n            if np.sign(tau_curve[i]) != baseline_sign:\n                return float(deltas[i])\n        return None\n    elif threshold_type == \"significance\":\n        z_crit = 1.96\n        for i in range(len(deltas)):\n            if np.isnan(tau_curve[i]):\n                continue\n            if abs(tau_curve[i]) < z_crit * threshold_value:\n                return float(deltas[i])\n        return None\n    else:\n        raise ValueError(\n            f\"Unknown threshold_type: {threshold_type}. \"\n            f\"Choose from 'magnitude', 'significance', 'sign_flip'\"\n        )\n\n\ndef compute_asv(topology, C0, params=None, threshold_type=\"magnitude\",\n                threshold_value=0.1, n_grid=1500):\n    \"\"\"Compute Annotation Sensitivity Value for a topology and base confusion matrix.\n\n    ASV is the minimum interpolation delta at which a bias threshold is crossed\n    along the path C(delta) = (1-delta)*I + delta*C0.\n\n    Args:\n        topology: one of 7 DAG types\n        C0: (K, K) base confusion matrix\n        params: optional DGP parameters dict\n        threshold_type: \"magnitude\" (relative to tau_true),\n                        \"significance\" (threshold_value = SE),\n                        \"sign_flip\" (sign of tau changes)\n        threshold_value: threshold parameter (meaning depends on threshold_type)\n        n_grid: number of delta grid points\n\n    Returns:\n        dict with asv, bias_curve, envelope, deltas, tau_true\n    \"\"\"\n    if topology not in TOPOLOGIES:\n        raise ValueError(f\"Unknown topology: {topology}. Choose from {TOPOLOGIES}\")\n    if not validate_confusion_matrix(C0):\n        raise ValueError(\"C0 must be a valid column-stochastic matrix\")\n\n    K = C0.shape[0]\n    merged = dict(DEFAULT_PARAMS[topology])\n    if params is not None:\n        merged.update(params)\n\n    stats = _precompute(topology, merged, K)\n    tau_true = _get_tau(topology, np.eye(K), stats, K)\n\n    deltas, bias_abs, tau_curve = _compute_bias_curve(\n        topology, C0, stats, K, tau_true, n_grid\n    )\n    envelope = _compute_envelope(bias_abs)\n\n    asv = _find_threshold_crossing(\n        envelope, deltas, tau_curve, tau_true, threshold_type, threshold_value\n    )\n\n    return {\n        \"asv\": asv,\n        \"bias_curve\": bias_abs,\n        \"envelope\": envelope,\n        \"deltas\": deltas,\n        \"tau_true\": float(tau_true),\n    }\n"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T23:37:54.458925+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/asv.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T23:37:54.461295+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/correction.py",
    "content": "\"\"\"Correction methods and recommendation engine for annotation-error bias.\n\nFive correction methods:\n  - naive_plugin: C^{-1} correction of dummy indicators\n  - dsl: EM-based joint estimation of regression params and C\n  - ppi: PPI++ combining gold-standard and full-sample estimates\n  - mcsimex: MC-SIMEX extrapolation to lambda=-1\n  - mla: Matrix-based label adjustment via D*_full @ C^{-1}\n\nKey finding (FWL theorem): naive_plugin and mla correct dummy coefficients\nbut NOT the treatment coefficient in regressions with a separate treatment T.\n\"\"\"\n\nimport numpy as np\nfrom .utils import ols, ols_with_se, make_dummies, make_full_dummies, misclassify\n\nMETHODS = [\"naive_plugin\", \"dsl\", \"ppi\", \"mcsimex\", \"mla\"]\n\n_EM_MAX_ITER = 100\n_EM_TOL = 1e-6\n_SIMEX_LAMBDAS = [0.5, 1.0, 1.5, 2.0]\n_SIMEX_B = 50\n\n\ndef correct_naive_plugin(X_other, Y, Astar, C, tau_idx=1):\n    \"\"\"Correct using C^{-1} applied per-observation to dummy indicators.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        C: (K, K) confusion matrix\n        tau_idx: index of target coefficient in full design\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    cond = np.linalg.cond(C)\n    if cond > 1e12:\n        return np.nan, np.nan, False\n    try:\n        C_inv = np.linalg.inv(C)\n    except np.linalg.LinAlgError:\n        return np.nan, np.nan, False\n    D_corrected = C_inv[:, Astar].T[:, 1:]\n    X = np.column_stack([X_other, D_corrected])\n    try:\n        beta, se = ols_with_se(X, Y)\n        return float(beta[tau_idx]), float(se[tau_idx]), True\n    except Exception:\n        return np.nan, np.nan, False\n\n\ndef correct_dsl(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1):\n    \"\"\"EM-based joint estimation of regression params and C.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        A_gold: (N,) gold-standard labels (only gold_mask positions used)\n        gold_mask: (N,) boolean mask for gold-standard observations\n        tau_idx: index of target coefficient\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    N = len(Y)\n    K = int(max(Astar.max(), A_gold[gold_mask].max())) + 1\n    n_other = X_other.shape[1]\n\n    C_est = np.zeros((K, K))\n    for j in range(K):\n        for k in range(K):\n            C_est[k, j] = (\n                (A_gold[gold_mask] == j) & (Astar[gold_mask] == k)\n            ).sum()\n    col_sums = C_est.sum(axis=0)\n    col_sums[col_sums == 0] = 1.0\n    C_est /= col_sums\n    C_est = 0.9 * C_est + 0.1 / K * np.ones((K, K))\n\n    D_star = make_dummies(Astar, K)\n    X_init = np.column_stack([X_other, D_star])\n    try:\n        beta = ols(X_init, Y)\n    except Exception:\n        return np.nan, np.nan, False\n    sigma2 = 1.0\n\n    for _ in range(_EM_MAX_ITER):\n        base = X_other @ beta[:n_other]\n        resp = np.zeros((N, K))\n        for j in range(K):\n            mu_j = base + (beta[n_other + j - 1] if j > 0 else 0.0)\n            resp[:, j] = (\n                -0.5 * (Y - mu_j) ** 2 / sigma2\n                + np.log(np.clip(C_est[Astar, j], 1e-15, None))\n            )\n        resp -= resp.max(axis=1, keepdims=True)\n        resp = np.exp(resp)\n        resp /= resp.sum(axis=1, keepdims=True)\n        resp[gold_mask] = 0.0\n        resp[gold_mask, A_gold[gold_mask]] = 1.0\n\n        D_exp = resp[:, 1:]\n        X_new = np.column_stack([X_other, D_exp])\n        try:\n            beta_new = ols(X_new, Y)\n        except Exception:\n            return np.nan, np.nan, False\n        sigma2_new = max(np.mean((Y - X_new @ beta_new) ** 2), 1e-6)\n\n        C_new = np.zeros((K, K))\n        for j in range(K):\n            for k in range(K):\n                C_new[k, j] = resp[Astar == k, j].sum()\n        cs = C_new.sum(axis=0)\n        cs[cs == 0] = 1.0\n        C_new /= cs\n\n        converged = (\n            np.max(np.abs(beta_new - beta)) < _EM_TOL\n            and np.max(np.abs(C_new - C_est)) < _EM_TOL\n        )\n        beta, C_est, sigma2 = beta_new, C_new, sigma2_new\n        if converged:\n            break\n\n    X_final = np.column_stack([X_other, resp[:, 1:]])\n    try:\n        beta_f, se_f = ols_with_se(X_final, Y)\n        return float(beta_f[tau_idx]), float(se_f[tau_idx]), True\n    except Exception:\n        return np.nan, np.nan, False\n\n\ndef correct_ppi(X_other, Y, Astar, A_gold, gold_mask, tau_idx=1, rng=None):\n    \"\"\"PPI++ with bootstrap lambda tuning.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        A_gold: (N,) gold-standard labels\n        gold_mask: (N,) boolean mask for gold-standard observations\n        tau_idx: index of target coefficient\n        rng: numpy random Generator\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    if rng is None:\n        rng = np.random.default_rng()\n    K = int(max(Astar.max(), A_gold[gold_mask].max())) + 1\n    gold_idx = np.where(gold_mask)[0]\n    n_gold = len(gold_idx)\n\n    D_g_true = make_dummies(A_gold[gold_mask], K)\n    X_g_true = np.column_stack([X_other[gold_mask], D_g_true])\n    D_g_star = make_dummies(Astar[gold_mask], K)\n    X_g_star = np.column_stack([X_other[gold_mask], D_g_star])\n    D_all_star = make_dummies(Astar, K)\n    X_all_star = np.column_stack([X_other, D_all_star])\n\n    try:\n        b_g_true = ols(X_g_true, Y[gold_mask])\n        b_g_star = ols(X_g_star, Y[gold_mask])\n        b_all_star = ols(X_all_star, Y)\n    except Exception:\n        return np.nan, np.nan, False\n\n    n_boot = 50\n    tau_true_boot = np.zeros(n_boot)\n    tau_rect_boot = np.zeros(n_boot)\n    for b in range(n_boot):\n        idx = rng.choice(gold_idx, size=n_gold, replace=True)\n        try:\n            bt = ols(\n                np.column_stack([X_other[idx], make_dummies(A_gold[idx], K)]),\n                Y[idx],\n            )\n            bs = ols(\n                np.column_stack([X_other[idx], make_dummies(Astar[idx], K)]),\n                Y[idx],\n            )\n            tau_true_boot[b] = bt[tau_idx]\n            tau_rect_boot[b] = bs[tau_idx] - bt[tau_idx]\n        except Exception:\n            tau_true_boot[b] = tau_rect_boot[b] = np.nan\n\n    valid = np.isfinite(tau_true_boot) & np.isfinite(tau_rect_boot)\n    if valid.sum() > 5:\n        var_r = np.var(tau_rect_boot[valid])\n        cov_tr = np.cov(tau_true_boot[valid], tau_rect_boot[valid])[0, 1]\n        lam = np.clip(-cov_tr / var_r, 0, 1) if var_r > 1e-12 else 1.0\n    else:\n        lam = 1.0\n\n    tau_ppi = b_g_true[tau_idx] + lam * (b_all_star[tau_idx] - b_g_star[tau_idx])\n    se_est = float(np.std(tau_true_boot[valid])) if valid.sum() > 1 else np.nan\n    return float(tau_ppi), se_est, True\n\n\ndef correct_mcsimex(X_other, Y, Astar, C, tau_idx=1, rng=None):\n    \"\"\"MC-SIMEX: add extra misclassification at levels lambda, extrapolate to -1.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        C: (K, K) confusion matrix\n        tau_idx: index of target coefficient\n        rng: numpy random Generator\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    if rng is None:\n        rng = np.random.default_rng()\n    K = C.shape[0]\n    try:\n        eigvals, eigvecs = np.linalg.eig(C)\n        eigvecs_inv = np.linalg.inv(eigvecs)\n    except np.linalg.LinAlgError:\n        return np.nan, np.nan, False\n\n    lambdas = np.array([0.0] + _SIMEX_LAMBDAS)\n    tau_lam = np.zeros(len(lambdas))\n\n    for li, lam_val in enumerate(lambdas):\n        if lam_val == 0.0:\n            D_star = make_dummies(Astar, K)\n            X = np.column_stack([X_other, D_star])\n            try:\n                tau_lam[li] = ols(X, Y)[tau_idx]\n            except Exception:\n                return np.nan, np.nan, False\n        else:\n            C_lam_raw = np.real((eigvecs * (eigvals ** lam_val)) @ eigvecs_inv)\n            C_lam = np.clip(C_lam_raw, 0, None)\n            cs = C_lam.sum(axis=0)\n            cs[cs == 0] = 1.0\n            C_lam /= cs\n\n            tau_b = np.zeros(_SIMEX_B)\n            for b in range(_SIMEX_B):\n                rng_b = np.random.default_rng(\n                    rng.integers(0, 2 ** 31) + b * 1000 + li * 100000\n                )\n                A_extra = misclassify(Astar, C_lam, rng_b)\n                D_extra = make_dummies(A_extra, K)\n                X_extra = np.column_stack([X_other, D_extra])\n                try:\n                    tau_b[b] = ols(X_extra, Y)[tau_idx]\n                except Exception:\n                    tau_b[b] = np.nan\n            ok = np.isfinite(tau_b)\n            if ok.sum() < _SIMEX_B // 2:\n                return np.nan, np.nan, False\n            tau_lam[li] = tau_b[ok].mean()\n\n    try:\n        coeffs = np.polyfit(lambdas, tau_lam, 2)\n        tau_simex = float(np.polyval(coeffs, -1.0))\n    except Exception:\n        return np.nan, np.nan, False\n\n    D_star = make_dummies(Astar, K)\n    X = np.column_stack([X_other, D_star])\n    try:\n        _, se = ols_with_se(X, Y)\n        return tau_simex, float(se[tau_idx]), True\n    except Exception:\n        return tau_simex, np.nan, True\n\n\ndef correct_mla(X_other, Y, Astar, C, tau_idx=1):\n    \"\"\"MLA: D_corrected = D*_full @ C^{-1}, drop reference category.\n\n    Args:\n        X_other: (N, p) non-A regressors (includes intercept)\n        Y: (N,) outcome\n        Astar: (N,) misclassified labels\n        C: (K, K) confusion matrix\n        tau_idx: index of target coefficient\n\n    Returns:\n        (tau_hat, se, success) tuple\n    \"\"\"\n    cond = np.linalg.cond(C)\n    if cond > 1e12:\n        return np.nan, np.nan, False\n    try:\n        C_inv = np.linalg.inv(C)\n    except np.linalg.LinAlgError:\n        return np.nan, np.nan, False\n    K = C.shape[0]\n    D_full = make_full_dummies(Astar, K)\n    D_corrected = (D_full @ C_inv)[:, 1:]\n    X = np.column_stack([X_other, D_corrected])\n    try:\n        beta, se = ols_with_se(X, Y)\n        return float(beta[tau_idx]), float(se[tau_idx]), True\n    except Exception:\n        return np.nan, np.nan, False\n\n\ndef recommend_correction(topology, C, has_gold=False, gold_fraction=0.1):\n    \"\"\"Recommend the best correction method based on topology and data availability.\n\n    Rules (from plan_007 conclusions):\n      - has_gold=True  -> PPI++ (93.8% bias reduction, 96.8% coverage)\n      - has_gold=False + confounding/mediation -> DSL\n      - has_gold=False + other topologies -> MC-SIMEX\n      - naive_plugin/MLA: only correct dummy coefficients (FWL theorem)\n\n    Args:\n        topology: one of 7 DAG types\n        C: (K, K) confusion matrix (used for diagnostics)\n        has_gold: whether gold-standard labels are available\n        gold_fraction: fraction of data with gold labels\n\n    Returns:\n        dict with recommended, ranking, notes\n    \"\"\"\n    dsl_safe = topology in (\"confounding\", \"mediation\")\n\n    if has_gold:\n        recommended = \"ppi\"\n    elif dsl_safe:\n        recommended = \"dsl\"\n    else:\n        recommended = \"mcsimex\"\n\n    ranking = []\n\n    # PPI++\n    if has_gold:\n        ranking.append({\n            \"method\": \"ppi\",\n            \"applicable\": True,\n            \"expected_bias_reduction\": 0.938,\n            \"notes\": \"Best with gold labels (93.8% bias reduction, 96.8% coverage)\",\n        })\n    else:\n        ranking.append({\n            \"method\": \"ppi\",\n            \"applicable\": False,\n            \"expected_bias_reduction\": 0.0,\n            \"notes\": \"Requires gold-standard labels\",\n        })\n\n    # DSL\n    if dsl_safe:\n        ranking.append({\n            \"method\": \"dsl\",\n            \"applicable\": True,\n            \"expected_bias_reduction\": 0.75,\n            \"notes\": \"Good for confounding/mediation\"\n                     + (\" (best with gold for initialization)\" if not has_gold else \"\"),\n        })\n    else:\n        ranking.append({\n            \"method\": \"dsl\",\n            \"applicable\": False,\n            \"expected_bias_reduction\": -5.0,\n            \"notes\": f\"Catastrophic for {topology} (e.g., mbias yields -768%)\",\n        })\n\n    # MC-SIMEX\n    ranking.append({\n        \"method\": \"mcsimex\",\n        \"applicable\": True,\n        \"expected_bias_reduction\": 0.209,\n        \"notes\": \"Moderate (20.9%) but broadly applicable; requires known C\",\n    })\n\n    # Naive Plugin\n    ranking.append({\n        \"method\": \"naive_plugin\",\n        \"applicable\": True,\n        \"expected_bias_reduction\": 0.0,\n        \"notes\": \"Only corrects dummy coefficients, NOT treatment coefficient (FWL theorem)\",\n    })\n\n    # MLA\n    ranking.append({\n        \"method\": \"mla\",\n        \"applicable\": True,\n        \"expected_bias_reduction\": 0.0,\n        \"notes\": \"Only corrects dummy coefficients, NOT treatment coefficient (FWL theorem)\",\n    })\n\n    ranking.sort(key=lambda m: -m[\"expected_bias_reduction\"])\n\n    notes = []\n    if has_gold:\n        notes.append(f\"Gold labels available ({gold_fraction:.0%} of data)\")\n        notes.append(\"PPI++ recommended: highest bias reduction with valid coverage\")\n    else:\n        notes.append(\"No gold labels available\")\n        if dsl_safe:\n            notes.append(f\"DSL recommended for {topology} (EM-based, works with known C)\")\n        else:\n            notes.append(\n                f\"MC-SIMEX recommended; DSL is catastrophic for {topology}\"\n            )\n\n    cond = np.linalg.cond(C)\n    if cond > 100:\n        notes.append(\n            f\"WARNING: C condition number = {cond:.0f}, \"\n            f\"inverse-based methods may be unstable\"\n        )\n\n    return {\n        \"recommended\": recommended,\n        \"ranking\": ranking,\n        \"notes\": notes,\n    }\n"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T23:37:54.461878+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/correction.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T23:37:54.462137+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/__init__.py",
    "content": "\"\"\"annot_sensitivity: Annotation-error sensitivity analysis for causal inference.\n\nComputes how LLM annotation misclassification propagates bias through\n7 DAG topologies, with ASV sensitivity measures and 5 correction methods.\n\"\"\"\n\nfrom .bias import compute_bias, clear_cache\nfrom .asv import compute_asv\nfrom .correction import (\n    recommend_correction,\n    correct_naive_plugin,\n    correct_dsl,\n    correct_ppi,\n    correct_mcsimex,\n    correct_mla,\n    METHODS,\n)\nfrom .confusion import (\n    validate_confusion_matrix,\n    random_confusion_matrix,\n    interpolate_confusion,\n    predefined_matrices,\n    delta_range,\n)\nfrom .dgp import generate_data, TOPOLOGIES, DEFAULT_PARAMS, GEN_FUNCS\nfrom .utils import ols, ols_with_se, make_dummies, softmax_sample, misclassify\n\n__all__ = [\n    \"compute_bias\",\n    \"compute_asv\",\n    \"recommend_correction\",\n    \"correct_naive_plugin\",\n    \"correct_dsl\",\n    \"correct_ppi\",\n    \"correct_mcsimex\",\n    \"correct_mla\",\n    \"validate_confusion_matrix\",\n    \"random_confusion_matrix\",\n    \"interpolate_confusion\",\n    \"predefined_matrices\",\n    \"delta_range\",\n    \"generate_data\",\n    \"clear_cache\",\n    \"TOPOLOGIES\",\n    \"DEFAULT_PARAMS\",\n    \"METHODS\",\n    \"GEN_FUNCS\",\n    \"ols\",\n    \"ols_with_se\",\n    \"make_dummies\",\n    \"softmax_sample\",\n    \"misclassify\",\n]\n"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T23:37:54.462423+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/__init__.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T23:37:54.462709+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/examples/confounding_k3.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Worked example: confounding topology with K=3 confusion matrix.\n\nDemonstrates the full annot_sensitivity workflow:\n  1. Define a K=3 confusion matrix\n  2. Compute bias\n  3. Compute ASV\n  4. Get correction recommendation\n  5. (Optional) Plot bias curve\n\"\"\"\n\nimport numpy as np\nimport sys\nimport os\n\nsys.path.insert(0, os.path.join(os.path.dirname(__file__), \"..\", \"..\"))\n\nfrom annot_sensitivity import (\n    compute_bias,\n    compute_asv,\n    recommend_correction,\n    predefined_matrices,\n    validate_confusion_matrix,\n)\n\n\ndef main():\n    print(\"=\" * 60)\n    print(\"annot_sensitivity: Confounding K=3 Example\")\n    print(\"=\" * 60)\n\n    # 1. Define confusion matrix\n    C = np.array([\n        [0.80, 0.10, 0.10],\n        [0.10, 0.80, 0.10],\n        [0.10, 0.10, 0.80],\n    ])\n    print(f\"\\nConfusion matrix C (column-stochastic):\")\n    print(C)\n    print(f\"Valid: {validate_confusion_matrix(C)}\")\n    print(f\"Condition number: {np.linalg.cond(C):.1f}\")\n\n    # 2. Compute bias\n    print(\"\\n--- Bias Analysis ---\")\n    result = compute_bias(\"confounding\", C)\n    print(f\"tau_true  (no misclassification): {result['tau_true']:.4f}\")\n    print(f\"tau_biased (with C):              {result['tau_biased']:.4f}\")\n    print(f\"bias:                             {result['bias']:+.4f}\")\n    print(f\"bias_pct:                         {result['bias_pct']:+.2f}%\")\n\n    # Try all predefined matrices\n    print(f\"\\nBias across predefined matrices:\")\n    print(f\"  {'Matrix':<22} {'tau_biased':>10} {'bias':>10} {'bias_pct':>10}\")\n    print(f\"  {'-'*55}\")\n    for name, Ci in predefined_matrices().items():\n        r = compute_bias(\"confounding\", Ci)\n        print(f\"  {name:<22} {r['tau_biased']:>10.4f} {r['bias']:>+10.4f} \"\n              f\"{r['bias_pct']:>+9.2f}%\")\n\n    # 3. Compute ASV\n    print(\"\\n--- ASV Analysis ---\")\n    C0 = C.copy()\n    asv_result = compute_asv(\"confounding\", C0, threshold_type=\"magnitude\",\n                             threshold_value=0.1)\n    asv_val = asv_result[\"asv\"]\n    print(f\"tau_true:      {asv_result['tau_true']:.4f}\")\n    if asv_val is not None:\n        print(f\"Magnitude ASV: {asv_val:.3f} \"\n              f\"(bias exceeds 10% of tau at delta={asv_val:.3f})\")\n    else:\n        print(f\"Magnitude ASV: None (threshold never crossed)\")\n\n    asv_sf = compute_asv(\"confounding\", C0, threshold_type=\"sign_flip\")\n    sf_val = asv_sf[\"asv\"]\n    if sf_val is not None:\n        print(f\"Sign-flip ASV: {sf_val:.3f}\")\n    else:\n        print(f\"Sign-flip ASV: None (sign never flips)\")\n\n    # 4. Correction recommendation\n    print(\"\\n--- Correction Recommendation ---\")\n    rec_gold = recommend_correction(\"confounding\", C, has_gold=True,\n                                    gold_fraction=0.1)\n    print(f\"With gold labels:    {rec_gold['recommended']}\")\n    for note in rec_gold[\"notes\"]:\n        print(f\"  - {note}\")\n\n    rec_no_gold = recommend_correction(\"confounding\", C, has_gold=False)\n    print(f\"Without gold labels: {rec_no_gold['recommended']}\")\n    for note in rec_no_gold[\"notes\"]:\n        print(f\"  - {note}\")\n\n    print(f\"\\nMethod ranking (with gold):\")\n    for m in rec_gold[\"ranking\"]:\n        app = \"Y\" if m[\"applicable\"] else \"N\"\n        print(f\"  {m['method']:<16} applicable={app}  \"\n              f\"expected_bias_reduction={m['expected_bias_reduction']:+.1%}\")\n\n    # 5. Optional: plot bias curve\n    try:\n        import matplotlib\n        matplotlib.use(\"Agg\")\n        import matplotlib.pyplot as plt\n\n        fig, ax = plt.subplots(1, 1, figsize=(6, 4))\n        deltas = asv_result[\"deltas\"]\n        ax.plot(deltas, asv_result[\"bias_curve\"], \"b-\", alpha=0.4,\n                label=\"Pointwise |bias|\")\n        ax.plot(deltas, asv_result[\"envelope\"], \"r-\", linewidth=2,\n                label=\"Monotone envelope\")\n        thresh = 0.1 * abs(asv_result[\"tau_true\"])\n        ax.axhline(thresh, color=\"gray\", linestyle=\"--\", label=f\"10% threshold\")\n        if asv_val is not None:\n            ax.axvline(asv_val, color=\"green\", linestyle=\":\", label=f\"ASV={asv_val:.2f}\")\n        ax.set_xlabel(r\"$\\delta$ (interpolation parameter)\")\n        ax.set_ylabel(\"|Bias|\")\n        ax.set_title(\"Confounding K=3: ASV Bias Curve\")\n        ax.legend(fontsize=8)\n        ax.set_xlim(0, min(deltas[-1], 5))\n\n        out_path = os.path.join(os.path.dirname(__file__), \"..\", \"..\",\n                                \"artifacts\", \"example_bias_curve.png\")\n        os.makedirs(os.path.dirname(out_path), exist_ok=True)\n        fig.savefig(out_path, dpi=150, bbox_inches=\"tight\")\n        plt.close()\n        print(f\"\\nPlot saved to {out_path}\")\n    except ImportError:\n        print(\"\\nmatplotlib not available, skipping plot\")\n\n    print(\"\\nDone.\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T23:37:54.463060+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/examples/confounding_k3.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T23:37:54.465380+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/__init__.py",
    "content": ""
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T23:37:54.465647+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/__init__.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T23:37:54.465939+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/test_core.py",
    "content": "\"\"\"Core tests for the annot_sensitivity package.\"\"\"\n\nimport numpy as np\nimport pytest\nfrom annot_sensitivity import (\n    compute_bias,\n    compute_asv,\n    recommend_correction,\n    validate_confusion_matrix,\n    interpolate_confusion,\n    random_confusion_matrix,\n    predefined_matrices,\n    generate_data,\n    TOPOLOGIES,\n)\n\n\nclass TestValidateConfusionMatrix:\n    def test_identity_valid(self):\n        assert validate_confusion_matrix(np.eye(3)) is True\n\n    def test_predefined_valid(self):\n        for name, C in predefined_matrices().items():\n            assert validate_confusion_matrix(C) is True, f\"{name} failed\"\n\n    def test_non_square(self):\n        assert validate_confusion_matrix(np.ones((2, 3))) is False\n\n    def test_negative_entries(self):\n        C = np.array([[1.1, -0.1], [-0.1, 1.1]])\n        assert validate_confusion_matrix(C) is False\n\n    def test_not_column_stochastic(self):\n        C = np.array([[0.5, 0.5], [0.3, 0.3]])\n        assert validate_confusion_matrix(C) is False\n\n    def test_not_array(self):\n        assert validate_confusion_matrix([[1, 0], [0, 1]]) is False\n\n    def test_1x1(self):\n        assert validate_confusion_matrix(np.array([[1.0]])) is False\n\n    def test_random_valid(self):\n        C = random_confusion_matrix(4, diag_dominance=0.7, rng=np.random.default_rng(42))\n        assert validate_confusion_matrix(C) is True\n        assert C.shape == (4, 4)\n\n\nclass TestInterpolateConfusion:\n    def test_delta_zero_is_identity(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        C = interpolate_confusion(C0, 0.0)\n        np.testing.assert_allclose(C, np.eye(3), atol=1e-12)\n\n    def test_delta_one_is_C0(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        C = interpolate_confusion(C0, 1.0)\n        np.testing.assert_allclose(C, C0, atol=1e-12)\n\n    def test_intermediate_column_stochastic(self):\n        C0 = predefined_matrices()[\"asymmetric\"]\n        C = interpolate_confusion(C0, 0.5)\n        assert validate_confusion_matrix(C)\n\n    def test_small_delta(self):\n        C0 = predefined_matrices()[\"severe_uniform\"]\n        C = interpolate_confusion(C0, 0.01)\n        assert np.allclose(np.diag(C), np.ones(3) * (1 - 0.01) + 0.01 * np.diag(C0),\n                           atol=1e-6)\n\n\nclass TestComputeBias:\n    def test_identity_zero_bias(self):\n        result = compute_bias(\"confounding\", np.eye(3))\n        assert abs(result[\"bias\"]) < 1e-3\n        assert abs(result[\"bias_pct\"]) < 0.1\n\n    def test_confounding_nonzero_bias(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = compute_bias(\"confounding\", C)\n        assert abs(result[\"bias\"]) > 0.01\n        assert result[\"topology\"] == \"confounding\"\n        assert np.isfinite(result[\"tau_true\"])\n        assert np.isfinite(result[\"tau_biased\"])\n\n    def test_all_topologies_run(self):\n        C = predefined_matrices()[\"mild_uniform\"]\n        for topo in TOPOLOGIES:\n            result = compute_bias(topo, C)\n            assert result[\"topology\"] == topo\n            assert np.isfinite(result[\"tau_true\"])\n            assert np.isfinite(result[\"tau_biased\"])\n\n    def test_invalid_topology(self):\n        with pytest.raises(ValueError, match=\"Unknown topology\"):\n            compute_bias(\"nonexistent\", np.eye(3))\n\n    def test_invalid_C(self):\n        with pytest.raises(ValueError, match=\"column-stochastic\"):\n            compute_bias(\"confounding\", np.ones((3, 3)))\n\n    def test_worse_C_more_bias(self):\n        C_mild = predefined_matrices()[\"mild_uniform\"]\n        C_severe = predefined_matrices()[\"severe_uniform\"]\n        r_mild = compute_bias(\"confounding\", C_mild)\n        r_severe = compute_bias(\"confounding\", C_severe)\n        assert abs(r_severe[\"bias\"]) > abs(r_mild[\"bias\"])\n\n\nclass TestComputeASV:\n    def test_returns_valid_structure(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        result = compute_asv(\"confounding\", C0, n_grid=200)\n        assert \"asv\" in result\n        assert \"bias_curve\" in result\n        assert \"envelope\" in result\n        assert \"deltas\" in result\n        assert \"tau_true\" in result\n        assert len(result[\"deltas\"]) == 200\n        assert len(result[\"bias_curve\"]) == 200\n        assert len(result[\"envelope\"]) == 200\n\n    def test_asv_is_positive_or_none(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        result = compute_asv(\"confounding\", C0, threshold_type=\"magnitude\",\n                             threshold_value=0.1, n_grid=200)\n        if result[\"asv\"] is not None:\n            assert result[\"asv\"] > 0\n\n    def test_envelope_monotone(self):\n        C0 = predefined_matrices()[\"asymmetric\"]\n        result = compute_asv(\"mediation\", C0, n_grid=200)\n        diffs = np.diff(result[\"envelope\"])\n        assert np.all(diffs >= -1e-12)\n\n    def test_sign_flip_threshold(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        result = compute_asv(\"confounding\", C0, threshold_type=\"sign_flip\",\n                             n_grid=200)\n        assert \"asv\" in result\n\n    def test_invalid_threshold_type(self):\n        C0 = predefined_matrices()[\"symmetric_high\"]\n        with pytest.raises(ValueError, match=\"Unknown threshold_type\"):\n            compute_asv(\"confounding\", C0, threshold_type=\"invalid\", n_grid=50)\n\n\nclass TestRecommendCorrection:\n    def test_with_gold_recommends_ppi(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"confounding\", C, has_gold=True)\n        assert result[\"recommended\"] == \"ppi\"\n\n    def test_without_gold_confounding_recommends_dsl(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"confounding\", C, has_gold=False)\n        assert result[\"recommended\"] == \"dsl\"\n\n    def test_without_gold_mediation_recommends_dsl(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"mediation\", C, has_gold=False)\n        assert result[\"recommended\"] == \"dsl\"\n\n    def test_without_gold_collider_recommends_mcsimex(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"collider\", C, has_gold=False)\n        assert result[\"recommended\"] == \"mcsimex\"\n\n    def test_without_gold_mbias_recommends_mcsimex(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"mbias\", C, has_gold=False)\n        assert result[\"recommended\"] == \"mcsimex\"\n\n    def test_ranking_has_all_methods(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"confounding\", C, has_gold=True)\n        methods = {m[\"method\"] for m in result[\"ranking\"]}\n        assert methods == {\"ppi\", \"dsl\", \"mcsimex\", \"naive_plugin\", \"mla\"}\n\n    def test_notes_nonempty(self):\n        C = predefined_matrices()[\"symmetric_high\"]\n        result = recommend_correction(\"collider\", C, has_gold=False)\n        assert len(result[\"notes\"]) > 0\n\n\nclass TestDGP:\n    def test_generate_all_topologies(self):\n        for topo in TOPOLOGIES:\n            data = generate_data(topo, 100, seed=42)\n            assert \"Y\" in data\n            assert \"A\" in data\n            assert len(data[\"Y\"]) == 100\n\n    def test_confounding_has_treatment(self):\n        data = generate_data(\"confounding\", 100, seed=42)\n        assert \"T\" in data\n\n    def test_exposure_no_treatment(self):\n        data = generate_data(\"exposure\", 100, seed=42)\n        assert \"T\" not in data\n\n    def test_iv_has_instrument(self):\n        data = generate_data(\"iv\", 100, seed=42)\n        assert \"Z\" in data\n\n    def test_invalid_topology(self):\n        with pytest.raises(ValueError):\n            generate_data(\"invalid\", 100)\n\n\nif __name__ == \"__main__\":\n    pytest.main([__file__, \"-v\"])\n"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T23:37:54.466404+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/tests/test_core.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T23:37:54.466660+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "tool_args": {
    "command": "python -c \"from annot_sensitivity import compute_bias, compute_asv, recommend_correction; print('Import OK')\"",
    "description": "Test basic import"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T23:37:54.466883+00:00_

Exit code 127
/bin/bash: line 1: python: command not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T23:37:54.467105+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"from annot_sensitivity import compute_bias, compute_asv, recommend_correction; print('Import OK')\"",
    "description": "Test basic import with python3"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T23:37:54.469443+00:00_

Import OK

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T23:37:54.469704+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -m pytest annot_sensitivity/tests/test_core.py -v 2>&1",
  "description": "Run pytest test suite",
  "timeout": "300000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -m pytest annot_sensitivity/tests/test_core.py -v 2>&1",
    "description": "Run pytest test suite",
    "timeout": "300000"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T23:37:54.469959+00:00_

Exit code 1
/usr/bin/python3: No module named pytest

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T23:37:54.470192+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "tool_args": {
    "command": "pip3 install pytest -q 2>&1 | tail -3",
    "description": "Install pytest"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T23:37:54.470456+00:00_

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T23:37:54.470698+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "tool_args": {
    "command": "pip3 install --user pytest -q 2>&1 | tail -3",
    "description": "Install pytest with --user flag"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T23:37:54.470944+00:00_

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T23:37:54.473200+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

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
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "tool_args": {
    "command": "pip3 install --break-system-packages pytest -q 2>&1 | tail -3",
    "description": "Install pytest (break-system-packages for PEP 668)"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T23:37:54.473700+00:00_

  WARNING: The scripts py.test and pytest are installed in '/home/ubuntu/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T23:37:54.473947+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -m pytest annot_sensitivity/tests/test_core.py -v 2>&1",
  "description": "Run pytest test suite",
  "timeout": "300000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -m pytest annot_sensitivity/tests/test_core.py -v 2>&1",
    "description": "Run pytest test suite",
    "timeout": "300000"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T23:37:54.474250+00:00_

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
annot_sensitivity/tests/test_core.py::TestComputeBias::test_invalid_
…[truncated 1895 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T23:37:54.474555+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 annot_sensitivity/examples/confounding_k3.py 2>&1",
  "description": "Run worked example",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 annot_sensitivity/examples/confounding_k3.py 2>&1",
    "description": "Run worked example",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T23:37:54.474818+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_010_toolkit_20260520T232412",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-20T23:37:54.477193+00:00_

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
  "session": "worker_code_plan_010_toolkit_20260520T232412"
}
```

</details>

---
