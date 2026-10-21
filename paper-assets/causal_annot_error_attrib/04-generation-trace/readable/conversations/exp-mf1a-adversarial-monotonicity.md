# exp mf1a adversarial monotonicity

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_exp_mf1a_adversarial_monotonicity_20260523T173639.jsonl`
- **Structured JSON:** [`a368cd778b392bd62c5b.json`](../../sessions/a3/a368cd778b392bd62c5b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-23T17:47:09.935094+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_mf1a_adversarial_monotonicity_20260523T173639",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/annot_sensitivity/bias.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T17:47:09.935457+00:00_

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

…[truncated 4195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_mf1a_adversarial_monotonicity_20260523T173639",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T17:47:09.935642+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture_dgp_sensitivity.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_mf1a_adversarial_monotonicity_20260523T173639",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/conjecture_dgp_sensitivity.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T17:47:09.935936+00:00_

1	#!/usr/bin/env python3
2	"""
3	Conjecture 1 robustness to DGP parameters (β, σ²).
4	
5	Reviewer concern: "Only default DGP tested" in Conjecture 1 verification.
6	This sweeps a (β, σ²) × topology grid and reports per-cell ε-approximate
7	monotonicity statistics.
8	
9	Grid:
10	  - β (coefficient magnitude scale) ∈ {0.1, 0.5, 1.0, 2.0, 5.0}
11	  - σ² (T-equation noise variance, where applicable) ∈ {0.5, 1.0, 2.0}
12	  - topology ∈ {confounding, mediation, collider, exposure, mbias, frontdoor, iv}
13	  - K = 3, N_C0 = 10,000 Dirichlet(1,1,1) per cell, δ step = 0.01
14	
15	For each (β, σ², topology, C₀), build C(δ) = (1-δ)·I + δ·C₀ for δ ∈ [0, δ_max]
16	and compute the analytic plim curve |B(δ)| = |τ̂(C(δ)) - τ_true|.
17	The wrong-direction step is the largest single-δ violation against the
18	expected direction (non-decreasing for confounding/mediation/exposure/
19	frontdoor/iv; non-increasing for collider/mbias).
20	
21	Outputs:
22	  artifacts/conjecture_dgp_sensitivity_results.json
23	  artifacts/conjecture_dgp_sensitivity_table.tex
24	"""
25	
26	import json
27	import os
28	import sys
29	import time
30	
31	import numpy as np
32	
33	sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
34	from exp_d_conjecture_verify_v2 import (
35	    ALL_TOPOS, NON_DECREASING,
36	    GH_X, GH_W, GH_X2_a_flat, GH_X2_b_flat, GH_W2_flat,
37	    _softmax,
38	    AnalyticSuffStats, AnalyticIVSuffStats,
39	    compute_confounding_ss as _ss_conf_v2,
40	    compute_mediation_ss as _ss_med_v2,
41	    compute_exposure_ss as _ss_exp_v2,
42	    compute_iv_ss as _ss_iv_v2,
43	    compute_bias_curve, check_monotonicity,
44	    get_tau_at_C, make_p_A,
45	    _ALPHA_POOL, _BETA_A_POOL, _BETA_POOL,
46	    _GAMMA_POOL, _DELTA_POOL, _DT_POOL, _DY_POOL,
47	    _MBIAS_A1_POOL, _MBIAS_A2_POOL,
48	    _IV_DZ_POOL, _IV_DU_POOL,
49	    _FD_GAMMA_POOL, _FD_DELTA_POOL,
50	)
51	
52	# ====================================================================
53	# Configuration
54	# ========================
…[truncated 21746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_mf1a_adversarial_monotonicity_20260523T173639",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T17:47:09.936100+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_mf1a_adversarial_monotonicity_20260523T173639",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test.py"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T17:47:09.936337+00:00_

1	#!/usr/bin/env python3
2	"""
3	Exp-A: Non-differential Misclassification Stress Test Expansion
4	
5	Tests sign flip rate and bias ratio under increasing differential
6	misclassification departure ε.
7	
8	4 topologies × 2 K × 3 CM qualities × 4 ε = 96 configs
9	N=10,000 × 100 MC reps per config
10	"""
11	import numpy as np
12	import json
13	import time
14	import os
15	
16	TOPOLOGIES = ['confounding', 'mediation', 'exposure', 'iv']
17	K_VALUES = [3, 10]
18	EPSILONS = [0.0, 0.01, 0.05, 0.10]
19	CM_QUALS = {'high': 0.8, 'medium': 0.6, 'low': 0.4}
20	N_SAMPLES = 10_000
21	N_REPS = 100
22	N_LARGE = 2_000_000
23	SEED = 42
24	
25	_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]
26	_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
27	_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
28	_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
29	_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]
30	
31	
32	def softmax_rows(x):
33	    e = np.exp(x - x.max(axis=1, keepdims=True))
34	    return e / e.sum(axis=1, keepdims=True)
35	
36	
37	def sample_cat(probs, rng):
38	    cum = np.cumsum(probs, axis=1)
39	    u = rng.uniform(size=probs.shape[0])[:, None]
40	    return (u >= cum[:, :-1]).sum(axis=1).astype(int)
41	
42	
43	def make_p_A(K):
44	    if K == 3:
45	        return np.array([0.40, 0.35, 0.25])
46	    raw = np.array([1.0 / (i + 1) for i in range(K)])
47	    return raw / raw.sum()
48	
49	
50	def make_dgp_params(K):
51	    p_A = make_p_A(K)
52	    params = {
53	        'confounding': {
54	            'p_A': p_A, 'alpha': np.array(_ALPHA_POOL[:K-1]),
55	            'beta_A': np.array(_BETA_A_POOL[:K-1]),
56	            'beta_T': 2.0, 'sigma_T': 1.0,
57	        },
58	        'mediation': {
59	            'tau': 0.5, 'gamma': np.array(_GAMMA_POOL[:K]),
60	            'delta': np.array(_DELTA_POOL[:K]),
61	            'beta': np.array(_BETA_POOL[:K]),
62	        },
63	        'exposure': {'beta
…[truncated 14396 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_mf1a_adversarial_monotonicity_20260523T173639",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T17:47:09.936504+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify_v2.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_mf1a_adversarial_monotonicity_20260523T173639",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify_v2.py"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T17:47:09.936823+00:00_

1	#!/usr/bin/env python3
2	"""
3	Exp-D v2: Conjecture 1 verification with ANALYTIC plim (zero sampling noise).
4	
5	The original exp_d_conjecture_verify.py computed plim via sufficient statistics
6	estimated from N=5M Monte Carlo simulation, introducing O(1/sqrt(N)) ~ 0.0004
7	sampling noise. At MONO_TOL=1e-8, this generated ~141k false monotonicity
8	violations.
9	
10	This v2 computes ALL sufficient statistics analytically (closed-form for
11	confounding/mediation/exposure, Gauss-Hermite quadrature for collider/mbias/
12	frontdoor/iv), eliminating sampling noise entirely.
13	
14	Topology-specific analytics:
15	  - confounding: fully analytic (categorical A, linear T and Y)
16	  - exposure:    fully analytic (categorical A, linear Y)
17	  - mediation:   fully analytic (binary T, softmax A|T, linear Y)
18	  - collider:    2D Gauss-Hermite over (T, eps_Y), both N(0,1)
19	  - mbias:       2D Gauss-Hermite over (U1, U2), both N(0,1)
20	  - frontdoor:   1D Gauss-Hermite over T ~ N(0, alpha_U^2 + 1)
21	  - iv:          1D Gauss-Hermite over U ~ N(0,1), with binary Z
22	
23	Output: exp_d_conjecture_results_v2.json (same structure as v1)
24	"""
25	
26	import numpy as np
27	import json
28	import time
29	import sys
30	import os
31	from scipy.special import roots_hermite, softmax as scipy_softmax
32	from scipy.optimize import minimize as scipy_minimize
33	
34	# ====================================================================
35	# Gauss-Hermite quadrature setup
36	# ====================================================================
37	N_GH = 100  # points per dimension -- machine precision for smooth integrands
38	
39	# roots_hermite: physicist's convention, weight = exp(-x^2)
40	# integral f(x) exp(-x^2) dx ~ sum w_i f(x_i)
41	# For N(0,1) expectation: E[f(X)] = (1/sqrt(pi)) sum w_i f(x_i * sqrt(2))
42	_gh_x_raw, _gh_w_raw = roots_hermite(N_GH)
43	GH_X = _gh_x_raw * np.sqrt(2)   # rescaled nodes for N(0,1)
44	GH_W = _gh_w_raw / np.sqrt(np.pi)  # rescaled weights: sum w_i
…[truncated 40527 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_mf1a_adversarial_monotonicity_20260523T173639",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T17:47:09.937284+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_test.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nMF-1a: Adversarial Monotonicity Test for Conjecture 1.\n\nVerifies ε-approximate envelope monotonicity of |B(C(δ))| along\nC(δ)=(1-δ)I+δC₀ for δ∈[0,1] under 4 adversarial confusion matrix structures.\n\nGrid: 4 adversarial C₀ types × ~9 param configs × 3 K × 7 topologies × 3 β × 100 C₀\n\"\"\"\n\nimport json\nimport os\nimport sys\nimport time\nimport numpy as np\n\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\nfrom exp_d_conjecture_verify_v2 import (\n    ALL_TOPOS, NON_DECREASING, NON_INCREASING,\n    _COMPUTE_SS, make_all_params, get_tau_true,\n    compute_bias_curve,\n)\n\nK_VALUES = [3, 5, 7]\nN_DELTA = 101\nDELTA_STEP = 0.01\nN_C0 = 100\nSEED = 2024\nEPS_THRESHOLD = 0.001\n\nBETA_CONFIGS = ['alternating_large', 'same_sign', 'alternating_small']\nADV_TYPES = ['near_perm', 'block_diag', 'sparse', 'near_uniform']\nADV_PARAMS = {\n    'near_perm': [{'eps': 0.05}, {'eps': 0.1}, {'eps': 0.2}],\n    'block_diag': [{}],\n    'sparse': [{'p_diag': 0.3}, {'p_diag': 0.5}, {'p_diag': 0.7}],\n    'near_uniform': [{'eps': 0.01}, {'eps': 0.05}],\n}\n\nOUT_DIR = os.path.dirname(os.path.abspath(__file__))\n\n\ndef make_beta_vec(name, K):\n    pools = {\n        'alternating_large': [0, 1, -0.5, 0.3, -0.2, 0.1, -0.08],\n        'same_sign':         [0, 0.5, 0.3, 0.2, 0.1, 0.08, 0.05],\n        'alternating_small': [0, 0.2, -0.1, 0.05, -0.03, 0.02, -0.01],\n    }\n    return np.array(pools[name][:K])\n\n\ndef make_params_with_beta(K, beta_name):\n    params = make_all_params(K)\n    bv = make_beta_vec(beta_name, K)\n    params['exposure']['beta'] = bv.copy()\n    params['iv']['beta'] = bv.copy()\n    params['mediation']['beta'] = bv.copy()\n    params['frontdoor']['beta'] = bv.copy()\n    params['confounding']['beta_A'] = bv[1:].copy()\n    params['collider']['dY'] = bv.copy()\n    params['mbias']['a1'] = bv.copy()\n    return params\n\n\ndef gen_C0(adv_type, cfg, K, rng):\n    if adv_type == 'near_perm':\n        perm = rng.permutation(K)\n        P = np.zeros((K, K))\n        P[perm, np.arange(K)] = 1.0\n        e = cfg['eps']\n        return (1 - e) * P + e / K\n\n    if adv_type == 'block_diag':\n        split = max(1, K // 2)\n        C0 = np.zeros((K, K))\n        for j in range(K):\n            if j < split:\n                C0[:split, j] = 1.0 / split\n            else:\n                C0[split:, j] = 1.0 / (K - split)\n        return C0\n\n    if adv_type == 'sparse':\n        pd = cfg['p_diag']\n        C0 = np.zeros((K, K))\n        for k in range(K):\n            C0[k, k] = pd\n            off = [i for i in range(K) if i != k]\n            C0[rng.choice(off), k] = 1 - pd\n        return C0\n\n    if adv_type == 'near_uniform':\n        e = cfg['eps']\n        dv = 1.0 / K + e\n        ov = (1 - dv) / (K - 1)\n        C0 = np.full((K, K), ov)\n        np.fill_diagonal(C0, dv)\n        return C0\n\n\ndef compute_fixed_curve(topo, C0, ss, tau_true):\n    \"\"\"Compute |B(C(δ))| for δ∈[0,1]. Returns (bias_abs[0:101], weak_iv).\"\"\"\n    if topo == 'iv':\n        FS = ss.FS\n        a = float(FS[1])\n        b = float((C0 @ FS)[1])\n        if abs(a) < 1e-15:\n            return None, True\n        if abs(a - b) > 1e-15:\n            d_cross = a / (a - b)\n            if 0 < d_cross < 1:\n                return None, True\n\n    deltas_full, bias_full = compute_bias_curve(\n        topo, C0, ss, tau_true, delta_step=DELTA_STEP)\n    n = min(N_DELTA, len(bias_full))\n    if n < N_DELTA:\n        return None, False\n    return bias_full[:N_DELTA], False\n\n\ndef measure_violation(bias_abs, topo):\n    \"\"\"Return max single-step violation magnitude.\"\"\"\n    valid = ~np.isnan(bias_abs)\n    ba = bias_abs[valid]\n    if len(ba) < 2:\n        return 0.0\n    diffs = np.diff(ba)\n    if topo in NON_DECREASING:\n        drops = -diffs[diffs < 0]\n    else:\n        drops = diffs[diffs > 0]\n    return float(drops.max()) if len(drops) > 0 else 0.0\n\n\ndef main():\n    t0 = time.time()\n    rng = np.random.default_rng(SEED)\n\n    print(\"=\" * 78)\n    print(\"MF-1a: Adversarial Monotonicity Test\")\n    print(f\"  K={K_VALUES}  β={BETA_CONFIGS}\")\n    print(f\"  Adversarial: {ADV_TYPES}\")\n    print(f\"  N_C0={N_C0}  δ steps={N_DELTA}  ε threshold={EPS_THRESHOLD}\")\n    print(\"=\" * 78)\n    sys.stdout.flush()\n\n    all_eps = []\n    by_adv = {a: {'n': 0, 'nm': 0, 'mx': 0.0} for a in ADV_TYPES}\n    by_topo = {t: {'n': 0, 'nm': 0, 'mx': 0.0} for t in ALL_TOPOS}\n    by_K = {str(k): {'n': 0, 'nm': 0, 'mx': 0.0} for k in K_VALUES}\n    worst = []\n    total_weak_iv = 0\n    total_skipped = 0\n\n    n_adv_cfgs = sum(len(v) for v in ADV_PARAMS.values())\n    n_cells = len(K_VALUES) * len(BETA_CONFIGS) * len(ALL_TOPOS) * n_adv_cfgs\n    cell_i = 0\n\n    for K in K_VALUES:\n        for beta_name in BETA_CONFIGS:\n            params = make_params_with_beta(K, beta_name)\n\n            for topo in ALL_TOPOS:\n                ss = _COMPUTE_SS[topo](K, params[topo])\n                tau_true = get_tau_true(topo, K, params, ss)\n\n                if np.isnan(tau_true) or abs(tau_true) < 1e-12:\n                    cell_i += n_adv_cfgs\n                    total_skipped += n_adv_cfgs * N_C0\n                    continue\n\n                for adv_type in ADV_TYPES:\n                    for adv_cfg in ADV_PARAMS[adv_type]:\n                        cell_i += 1\n                        cell_eps = []\n                        cell_nm = 0\n                        cell_weak = 0\n\n                        for _ in range(N_C0):\n                            C0 = gen_C0(adv_type, adv_cfg, K, rng)\n                            curve, weak = compute_fixed_curve(\n                                topo, C0, ss, tau_true)\n\n                            if weak:\n                                cell_weak += 1\n                                continue\n                            if curve is None:\n                                continue\n\n                            eps = measure_violation(curve, topo)\n                            cell_eps.append(eps)\n                            if eps > EPS_THRESHOLD:\n                                cell_nm += 1\n\n                        n_valid = len(cell_eps)\n                        if n_valid == 0:\n                            total_weak_iv += cell_weak\n                            continue\n\n                        mx = max(cell_eps)\n                        total_weak_iv += cell_weak\n                        all_eps.extend(cell_eps)\n\n                        for acc, key in [(by_adv, adv_type),\n                                         (by_topo, topo),\n                                         (by_K, str(K))]:\n                            acc[key]['n'] += n_valid\n                            acc[key]['nm'] += cell_nm\n                            acc[key]['mx'] = max(acc[key]['mx'], mx)\n\n                        if mx > EPS_THRESHOLD:\n                            worst.append({\n                                'topology': topo, 'K': K,\n                                'adversarial': adv_type,\n                                'adv_config': json.dumps(adv_cfg)\n                                              if adv_cfg else \"{}\",\n                                'beta': beta_name,\n                                'eps_abs': mx,\n                                'non_mono_frac': cell_nm / n_valid,\n                                'n_valid': n_valid,\n                                'weak_iv': cell_weak,\n                            })\n\n                        if cell_i % 63 == 0 or cell_i == n_cells:\n                            print(\n                                f\"  [{cell_i:>4}/{n_cells}] K={K} \"\n                                f\"{topo:<12} {adv_type:<14} \"\n                                f\"β={beta_name:<18} max_ε={mx:.6f} \"\n                                f\"nm={cell_nm}/{n_valid}  \"\n                                f\"({time.time()-t0:.1f}s)\")\n                            sys.stdout.flush()\n\n    eps_arr = np.array(all_eps) if all_eps else np.array([0.0])\n    total_curves = len(all_eps)\n    total_nm = sum(1 for e in all_eps if e > EPS_THRESHOLD)\n\n    safe_topos = {'confounding', 'mediation', 'exposure', 'frontdoor'}\n    fragile_topos = {'collider', 'mbias', 'iv'}\n\n    def fmt_acc(d):\n        return {k: {\n            'total_curves': v['n'],\n            'non_monotone_count': v['nm'],\n            'non_monotone_fraction': v['nm'] / max(v['n'], 1),\n            'max_eps_abs': v['mx'],\n        } for k, v in d.items()}\n\n    worst.sort(key=lambda x: -x['eps_abs'])\n    worst = worst[:20]\n\n    output = {\n        'description':\n            'Adversarial envelope monotonicity test for Conjecture 1',\n        'config': {\n            'K_values': K_VALUES,\n            'adversarial_types': ADV_TYPES,\n            'adversarial_params': ADV_PARAMS,\n            'topologies': ALL_TOPOS,\n            'beta_configs': BETA_CONFIGS,\n            'n_C0_per_cell': N_C0,\n            'n_delta_steps': N_DELTA,\n            'delta_step': DELTA_STEP,\n            'eps_threshold': EPS_THRESHOLD,\n            'seed': SEED,\n        },\n        'summary': {\n            'total_curves': total_curves,\n            'non_monotone_fraction':\n                total_nm / max(total_curves, 1),\n            'max_eps_abs': float(eps_arr.max()),\n            'median_eps_abs': float(np.median(eps_arr)),\n            'mean_eps_abs': float(np.mean(eps_arr)),\n            'p95_eps_abs': float(np.percentile(eps_arr, 95)),\n            'p99_eps_abs': float(np.percentile(eps_arr, 99)),\n            'safe_topo_max_eps': float(\n                max(by_topo[t]['mx'] for t in safe_topos)),\n            'fragile_topo_max_eps': float(\n                max(by_topo[t]['mx'] for t in fragile_topos)),\n            'total_weak_iv_filtered': total_weak_iv,\n            'total_skipped_zero_tau': total_skipped,\n        },\n        'by_adversarial_type': fmt_acc(by_adv),\n        'by_topology': fmt_acc(by_topo),\n        'by_K': fmt_acc(by_K),\n        'worst_cases': worst,\n        'elapsed_seconds': time.time() - t0,\n    }\n\n    out_path = os.path.join(OUT_DIR, 'adversarial_monotonicity_results.json')\n    with open(out_path, 'w') as f:\n        json.dump(output, f, indent=2, default=str)\n\n    print(f\"\\nJSON -> {out_path}\")\n    print(f\"\\n{'='*60}\")\n    print(f\"Total curves: {total_curves:,}  \"\n          f\"Non-monotone: {total_nm} \"\n          f\"({total_nm/max(total_curves,1)*100:.3f}%)\")\n    print(f\"Max ε_abs: {eps_arr.max():.6f}  \"\n          f\"Median: {np.median(eps_arr):.6f}\")\n    print(f\"Safe max ε: \"\n          f\"{max(by_topo[t]['mx'] for t in safe_topos):.6f}  \"\n          f\"Fragile max ε: \"\n          f\"{max(by_topo[t]['mx'] for t in fragile_topos):.6f}\")\n    print(f\"Weak-IV filtered: {total_weak_iv}\")\n\n    print(f\"\\nBy topology:\")\n    for t in ALL_TOPOS:\n        d = by_topo[t]\n        dr = 'non-dec' if t in NON_DECREASING else 'non-inc'\n        print(f\"  {t:<14} [{dr}]  n={d['n']:>6}  nm={d['nm']:>5}  \"\n              f\"({d['nm']/max(d['n'],1)*100:.2f}%)  \"\n              f\"max_ε={d['mx']:.6f}\")\n\n    print(f\"\\nBy adversarial type:\")\n    for a in ADV_TYPES:\n        d = by_adv[a]\n        print(f\"  {a:<14}  n={d['n']:>6}  nm={d['nm']:>5}  \"\n              f\"({d['nm']/max(d['n'],1)*100:.2f}%)  \"\n              f\"max_ε={d['mx']:.6f}\")\n\n    print(f\"\\nBy K:\")\n    for k in K_VALUES:\n        d = by_K[str(k)]\n        print(f\"  K={k}  n={d['n']:>6}  nm={d['nm']:>5}  \"\n              f\"({d['nm']/max(d['n'],1)*100:.2f}%)  \"\n              f\"max_ε={d['mx']:.6f}\")\n\n    if worst:\n        print(f\"\\nWorst cases (top 5):\")\n        for w in worst[:5]:\n            print(f\"  {w['topology']:<14} K={w['K']} \"\n                  f\"{w['adversarial']:<14} \"\n                  f\"β={w['beta']:<18} ε={w['eps_abs']:.6f}\")\n\n    print(f\"\\nElapsed: {time.time()-t0:.1f}s\")\n    print('=' * 60)\n\n\nif __name__ == '__main__':\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_mf1a_adversarial_monotonicity_20260523T173639",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_test.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nMF-1a: Adversarial Monotonicity Test for Conjecture 1.\n\nVerifies ε-approximate envelope monotonicity of |B(C(δ))| along\nC(δ)=(1-δ)I+δC₀ for δ∈[0,1] under 4 adversarial confusion matrix structures.\n\nGrid: 4 adversarial C₀ types × ~9 param configs × 3 K × 7 topologies × 3 β × 100 C₀\n\"\"\"\n\nimport json\nimport os\nimport sys\nimport time\nimport numpy as np\n\nsys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\nfrom exp_d_conjecture_verify_v2 import (\n    ALL_TOPOS, NON_DECREASING, NON_INCREASING,\n    _COMPUTE_SS, make_all_params, get_tau_true,\n    compute_bias_curve,\n)\n\nK_VALUES = [3, 5, 7]\nN_DELTA = 101\nDELTA_STEP = 0.01\nN_C0 = 100\nSEED = 2024\nEPS_THRESHOLD = 0.001\n\nBETA_CONFIGS = ['alternating_large', 'same_sign', 'alternating_small']\nADV_TYPES = ['near_perm', 'block_diag', 'sparse', 'near_uniform']\nADV_PARAMS = {\n    'near_perm': [{'eps': 0.05}, {'eps': 0.1}, {'eps': 0.2}],\n    'block_diag': [{}],\n    'sparse': [{'p_diag': 0.3}, {'p_diag': 0.5}, {'p_diag': 0.7}],\n    'near_uniform': [{'eps': 0.01}, {'eps': 0.05}],\n}\n\nOUT_DIR = os.path.dirname(os.path.abspath(__file__))\n\n\ndef make_beta_vec(name, K):\n    pools = {\n        'alternating_large': [0, 1, -0.5, 0.3, -0.2, 0.1, -0.08],\n        'same_sign':         [0, 0.5, 0.3, 0.2, 0.1, 0.08, 0.05],\n        'alternating_small': [0, 0.2, -0.1, 0.05, -0.03, 0.02, -0.01],\n    }\n    return np.array(pools[name][:K])\n\n\ndef make_params_with_beta(K, beta_name):\n    params = make_all_params(K)\n    bv = make_beta_vec(beta_name, K)\n    params['exposure']['beta'] = bv.copy()\n    params['iv']['beta'] = bv.copy()\n    params['mediation']['beta'] = bv.copy()\n    params['frontdoor']['beta'] = bv.copy()\n    params['confounding']['beta_A'] = bv[1:].copy()\n    params['collider']['dY'] = bv.copy()\n    params['mbias']['a1'] = bv.copy()\n    return params\n\n\ndef gen_C0(adv_type, cfg, K, rng):\n    if adv_type == 'near_perm':\n        perm = rng.permutation(K)\n        P = np.zeros((K, K))\n        P[perm, np.arange(K)] = 1.0\n        e = cfg['eps']\n        return (1 - e) * P + e / K\n\n    if adv_type == 'block_diag':\n        split = max(1, K // 2)\n        C0 = np.zeros((K, K))\n        for j in range(K):\n            if j < split:\n                C0[:split, j] = 1.0 / split\n            else:\n                C0[split:, j] = 1.0 / (K - split)\n        return C0\n\n    if adv_type == 'sparse':\n        pd = cfg['p_diag']\n        C0 = np.zeros((K, K))\n        for k in range(K):\n            C0[k, k] = pd\n            off = [i for i in range(K) if i != k]\n            C0[rng.choice(off), k] = 1 - pd\n        return C0\n\n    if adv_type == 'near_uniform':\n        e = cfg['eps']\n        dv = 1.0 / K + e\n        ov = (1 - dv) / (K - 1)\n        C0 = np.full((K, K), ov)\n        np.fill_diagonal(C0, dv)\n        return C0\n\n\ndef compute_fixed_curve(topo, C0, ss, tau_true):\n    \"\"\"Compute |B(C(δ))| for δ∈[0,1]. Returns (bias_abs[0:101], weak_iv).\"\"\"\n    if topo == 'iv':\n        FS = ss.FS\n        a = float(FS[1])\n        b = float((C0 @ FS)[1])\n        if abs(a) < 1e-15:\n            return None, True\n        if abs(a - b) > 1e-15:\n            d_cross = a / (a - b)\n            if 0 < d_cross < 1:\n                return None, True\n\n    deltas_full, bias_full = compute_bias_curve(\n        topo, C0, ss, tau_true, delta_step=DELTA_STEP)\n    n = min(N_DELTA, len(bias_full))\n    if n < N_DELTA:\n        return None, False\n    return bias_full[:N_DELTA], False\n\n\ndef measure_violation(bias_abs, topo):\n    \"\"\"Return max single-step violation magnitude.\"\"\"\n    valid = ~np.isnan(bias_abs)\n    ba = bias_abs[valid]\n    if len(ba) < 2:\n        return 0.0\n    diffs = np.diff(ba)\n    if topo in NON_DECREASING:\n        drops = -diffs[diffs < 0]\n    else:\n        drops = diffs[diffs > 0]\n    return float(drops.max()) if len(drops) > 0 else 0.0\n\n\ndef main():\n    t0 = time.time()\n    rng = np.random.default_rng(SEED)\n\n    print(\"=\" * 78)\n    print(\"MF-1a: Adversarial Monotonicity Test\")\n    print(f\"  K={K_VALUES}  β={BETA_CONFIGS}\")\n    print(f\"  Adversarial: {ADV_TYPES}\")\n    print(f\"  N_C0={N_C0}  δ steps={N_DELTA}  ε threshold={EPS_THRESHOLD}\")\n    print(\"=\" * 78)\n    sys.stdout.flush()\n\n    all_eps = []\n    by_adv = {a: {'n': 0, 'nm': 0, 'mx': 0.0} for a in ADV_TYPES}\n    by_topo = {t: {'n': 0, 'nm': 0, 'mx': 0.0} for t in ALL_TOPOS}\n    by_K = {str(k): {'n': 0, 'nm': 0, 'mx': 0.0} for k in K_VALUES}\n    worst = []\n    total_weak_iv = 0\n    total_skipped = 0\n\n    n_adv_cfgs = sum(len(v) for v in ADV_PARAMS.values())\n    n_cells = len(K_VALUES) * len(BETA_CONFIGS) * len(ALL_TOPOS) * n_adv_cfgs\n    cell_i = 0\n\n    for K in K_VALUES:\n        for beta_name in BETA_CONFIGS:\n            params = make_params_with_beta(K, beta_name)\n\n            for topo in ALL_TOPOS:\n                ss = _COMPUTE_SS[topo](K, params[topo])\n                tau_true = get_tau_true(topo, K, params, ss)\n\n                if np.isnan(tau_true) or abs(tau_true) < 1e-12:\n                    cell_i += n_adv_cfgs\n                    total_skipped += n_adv_cfgs * N_C0\n                    continue\n\n                for adv_type in ADV_TYPES:\n                    for adv_cfg in ADV_PARAMS[adv_type]:\n                        cell_i += 1\n                        cell_eps = []\n                        cell_nm = 0\n                        cell_weak = 0\n\n                        for _ in range(N_C0):\n                            C0 = gen_C0(adv_type, adv_cfg, K, rng)\n                            curve, weak = compute_fixed_curve(\n                                topo, C0, ss, tau_true)\n\n                            if weak:\n                                cell_weak += 1\n                                continue\n                            if curve is None:\n                                continue\n\n                            eps = measure_violation(curve, topo)\n                            cell_eps.append(eps)\n                            if eps > EPS_THRESHOLD:\n                                cell_nm += 1\n\n                        n_valid = len(cell_eps)\n                        if n_valid == 0:\n                            total_weak_iv += cell_weak\n                            continue\n\n                        mx = max(cell_eps)\n                        total_weak_iv += cell_weak\n                        all_eps.extend(cell_eps)\n\n                        for acc, key in [(by_adv, adv_type),\n                                         (by_topo, topo),\n                                         (by_K, str(K))]:\n                            acc[key]['n'] += n_valid\n                            acc[key]['nm'] += cell_nm\n                            acc[key]['mx'] = max(acc[key]['mx'], mx)\n\n                        if mx > EPS_THRESHOLD:\n                            worst.append({\n                                'topology': topo, 'K': K,\n                                'adversarial': adv_type,\n                                'adv_config': json.dumps(adv_cfg)\n                                              if adv_cfg else \"{}\",\n                                'beta': beta_name,\n                                'eps_abs': mx,\n                                'non_mono_frac': cell_nm / n_valid,\n                                'n_valid': n_valid,\n                                'weak_iv': cell_weak,\n                            })\n\n                        if cell_i % 63 == 0 or cell_i == n_cells:\n                            print(\n                                f\"  [{cell_i:>4}/{n_cells}] K={K} \"\n                                f\"{topo:<12} {adv_type:<14} \"\n                                f\"β={beta_name:<18} max_ε={mx:.6f} \"\n                                f\"nm={cell_nm}/{n_valid}  \"\n                                f\"({time.time()-t0:.1f}s)\")\n                            sys.stdout.flush()\n\n    eps_arr = np.array(all_eps) if all_eps else np.array([0.0])\n    total_curves = len(all_eps)\n    total_nm = sum(1 for e in all_eps if e > EPS_THRESHOLD)\n\n    safe_topos = {'confounding', 'mediation', 'exposure', 'frontdoor'}\n    fragile_topos = {'collider', 'mbias', 'iv'}\n\n    def fmt_acc(d):\n        return {k: {\n            'total_curves': v['n'],\n            'non_monotone_count': v['nm'],\n            'non_monotone_fraction': v['nm'] / max(v['n'], 1),\n            'max_eps_abs': v['mx'],\n        } for k, v in d.items()}\n\n    worst.sort(key=lambda x: -x['eps_abs'])\n    worst = worst[:20]\n\n    output = {\n        'description':\n            'Adversarial envelope monotonicity test for Conjecture 1',\n        'config': {\n            'K_values': K_VALUES,\n            'adversarial_types': ADV_TYPES,\n            'adversarial_params': ADV_PARAMS,\n            'topologies': ALL_TOPOS,\n            'beta_configs': BETA_CONFIGS,\n            'n_C0_per_cell': N_C0,\n            'n_delta_steps': N_DELTA,\n            'delta_step': DELTA_STEP,\n            'eps_threshold': EPS_THRESHOLD,\n            'seed': SEED,\n        },\n        'summary': {\n            'total_curves': total_curves,\n            'non_monotone_fraction':\n                total_nm / max(total_curves, 1),\n            'max_eps_abs': float(eps_arr.max()),\n            'median_eps_abs': float(np.median(eps_arr)),\n            'mean_eps_abs': float(np.mean(eps_arr)),\n            'p95_eps_abs': float(np.percentile(eps_arr, 95)),\n            'p99_eps_abs': float(np.percentile(eps_arr, 99)),\n            'safe_topo_max_eps': float(\n                max(by_topo[t]['mx'] for t in safe_topos)),\n            'fragile_topo_max_eps': float(\n                max(by_topo[t]['mx'] for t in fragile_topos)),\n            'total_weak_iv_filtered': total_weak_iv,\n            'total_skipped_zero_tau': total_skipped,\n        },\n        'by_adversarial_type': fmt_acc(by_adv),\n        'by_topology': fmt_acc(by_topo),\n        'by_K': fmt_acc(by_K),\n        'worst_cases': worst,\n        'elapsed_seconds': time.time() - t0,\n    }\n\n    out_path = os.path.join(OUT_DIR, 'adversarial_monotonicity_results.json')\n    with open(out_path, 'w') as f:\n        json.dump(output, f, indent=2, default=str)\n\n    print(f\"\\nJSON -> {out_path}\")\n    print(f\"\\n{'='*60}\")\n    print(f\"Total curves: {total_curves:,}  \"\n          f\"Non-monotone: {total_nm} \"\n          f\"({total_nm/max(total_curves,1)*100:.3f}%)\")\n    print(f\"Max ε_abs: {eps_arr.max():.6f}  \"\n          f\"Median: {np.median(eps_arr):.6f}\")\n    print(f\"Safe max ε: \"\n          f\"{max(by_topo[t]['mx'] for t in safe_topos):.6f}  \"\n          f\"Fragile max ε: \"\n          f\"{max(by_topo[t]['mx'] for t in fragile_topos):.6f}\")\n    print(f\"Weak-IV filtered: {total_weak_iv}\")\n\n    print(f\"\\nBy topology:\")\n    for t in ALL_TOPOS:\n        d = by_topo[t]\n        dr = 'non-dec' if t in NON_DECREASING else 'non-inc'\n        print(f\"  {t:<14} [{dr}]  n={d['n']:>6}  nm={d['nm']:>5}  \"\n              f\"({d['nm']/max(d['n'],1)*100:.2f}%)  \"\n              f\"max_ε={d['mx']:.6f}\")\n\n    print(f\"\\nBy adversarial type:\")\n    for a in ADV_TYPES:\n        d = by_adv[a]\n        print(f\"  {a:<14}  n={d['n']:>6}  nm={d['nm']:>5}  \"\n              f\"({d['nm']/max(d['n'],1)*100:.2f}%)  \"\n              f\"max_ε={d['mx']:.6f}\")\n\n    print(f\"\\nBy K:\")\n    for k in K_VALUES:\n        d = by_K[str(k)]\n        print(f\"  K={k}  n={d['n']:>6}  nm={d['nm']:>5}  \"\n              f\"({d['nm']/max(d['n'],1)*100:.2f}%)  \"\n              f\"max_ε={d['mx']:.6f}\")\n\n    if worst:\n        print(f\"\\nWorst cases (top 5):\")\n        for w in worst[:5]:\n            print(f\"  {w['topology']:<14} K={w['K']} \"\n                  f\"{w['adversarial']:<14} \"\n                  f\"β={w['beta']:<18} ε={w['eps_abs']:.6f}\")\n\n    print(f\"\\nElapsed: {time.time()-t0:.1f}s\")\n    print('=' * 60)\n\n\nif __name__ == '__main__':\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T17:47:09.937571+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_test.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_mf1a_adversarial_monotonicity_20260523T173639",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T17:47:09.937706+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts && python3 adversarial_monotonicity_test.py 2>&1",
  "timeout": "600000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_mf1a_adversarial_monotonicity_20260523T173639",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts && python3 adversarial_monotonicity_test.py 2>&1",
    "timeout": "600000"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T17:47:09.937850+00:00_

==============================================================================
MF-1a: Adversarial Monotonicity Test
  K=[3, 5, 7]  β=['alternating_large', 'same_sign', 'alternating_small']
  Adversarial: ['near_perm', 'block_diag', 'sparse', 'near_uniform']
  N_C0=100  δ steps=101  ε threshold=0.001
==============================================================================
/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_d_conjecture_verify_v2.py:682: RuntimeWarning: divide by zero encountered in divide
  taus = np.where(np.abs(denom) < 1e-15, np.nan, ss.RF / denom)
  [  63/567] K=3 frontdoor    near_uniform   β=alternating_large  max_ε=0.000000 nm=0/100  (1.3s)
  [ 126/567] K=3 frontdoor    near_uniform   β=same_sign          max_ε=0.000000 nm=0/100  (2.5s)
  [ 189/567] K=3 frontdoor    near_uniform   β=alternating_small  max_ε=0.000000 nm=0/100  (3.8s)
  [ 252/567] K=5 frontdoor    near_uniform   β=alternating_large  max_ε=0.000000 nm=0/100  (5.2s)
  [ 315/567] K=5 frontdoor    near_uniform   β=same_sign          max_ε=0.000000 nm=0/100  (6.7s)
  [ 378/567] K=5 frontdoor    near_uniform   β=alternating_small  max_ε=0.000000 nm=0/100  (8.1s)
  [ 441/567] K=7 frontdoor    near_uniform   β=alternating_large  max_ε=0.000000 nm=0/100  (10.8s)
  [ 504/567] K=7 frontdoor    near_uniform   β=same_sign          max_ε=0.000000 nm=0/100  (12.6s)
  [ 567/567] K=7 frontdoor    near_uniform   β=alternating_small  max_ε=0.000000 nm=0/100  (14.3s)

JSON -> /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_results.json

============================================================
Total curves: 54,611  Non-monotone: 6517 (11.933%)
Max ε_abs: 0.016365  Median: 0.000000
Safe max ε: 0.016365  Fragile max ε: 0.013177
Weak-IV filtered: 2089

By topology:
  confounding    [non-dec]  n=  8100  nm= 1706  (21.06%)  max_ε=0.016365
  mediation      [non-dec]  n=  8100  nm= 1612  (19.90%
…[truncated 1251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_mf1a_adversarial_monotonicity_20260523T173639",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T17:47:09.938015+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_mf1a_adversarial_monotonicity_20260523T173639",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T17:47:09.938130+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_mf1a_adversarial_monotonicity_20260523T173639",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T17:47:09.938263+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "MF-1a Adversarial Monotonicity Test Results",
  "type": "data",
  "description": "Conjecture 1 adversarial monotonicity test: 54,611 curves across 4 adversarial C₀ structures × 3 K × 7 topologies × 3 β configs × 100 C₀. Max ε_abs=0.016, confirming ε-approximate envelope monotonicity under adversarial conditions.",
  "project": "causal_annot_error_attrib",
  "source_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_results.json",
  "tags": "['conjecture1', 'monotonicity', 'adversarial', 'MF-1a']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_exp_mf1a_adversarial_monotonicity_20260523T173639",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "MF-1a Adversarial Monotonicity Test Results",
    "type": "data",
    "description": "Conjecture 1 adversarial monotonicity test: 54,611 curves across 4 adversarial C₀ structures × 3 K × 7 topologies × 3 β configs × 100 C₀. Max ε_abs=0.016, confirming ε-approximate envelope monotonicity under adversarial conditions.",
    "project": "causal_annot_error_attrib",
    "source_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/adversarial_monotonicity_results.json",
    "tags": "['conjecture1', 'monotonicity', 'adversarial', 'MF-1a']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T17:47:09.938400+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260523_877baa\", \"name\": \"MF-1a Adversarial Monotonicity Test Results\", \"type\": \"data\", \"description\": \"Conjecture 1 adversarial monotonicity test: 54,611 curves across 4 adversarial C₀ structures × 3 K × 7 topologies × 3 β configs × 100 C₀. Max ε_abs=0.016, confirming ε-approximate envelope monotonicity under adversarial conditions.\", \"path\": \"projects/causal_annot_error_attrib/artifacts/_project/data/adversarial_monotonicity_results.json\", \"url\": null, \"project\": \"causal_annot_error_attrib\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-23T17:46:56.702531+00:00\", \"tags\": [\"conjecture1\", \"monotonicity\", \"adversarial\", \"MF-1a\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_exp_mf1a_adversarial_monotonicity_20260523T173639",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-23T17:47:09.938559+00:00_

**MF-1a 完成。** 54,611 条曲线，14.3s 运行。

核心发现：

| 维度 | max ε_abs | 非单调率 |
|------|-----------|----------|
| **总体** | **0.0164** | 11.9% |
| safe topos (conf/med/exp/fd) | 0.0164 | — |
| fragile topos (col/mbias/iv) | 0.0132 | — |

**按 adversarial 类型：**
- **near_perm**: 最具对抗性，35.3% 非单调，max ε=0.016
- **block_diag**: 0% 非单调（确定性结构，无违反）
- **sparse**: 2.3% 非单调，max ε=0.003
- **near_uniform**: 0% 非单调

**按 topology：**
- confounding/mediation/frontdoor 约 20% 曲线有微小违反（ε < 0.017）
- exposure 仅 0.68%，mbias 1.44%
- IV: 0 违反（过滤掉 2,089 条 weak-IV 曲线后）

**结论：** 所有 adversarial 结构下 max ε_abs = 0.016，远低于论文声称的 0.06 bound。Conjecture 1 的 ε-approximate envelope monotonicity 在 adversarial 条件下成立。违反集中在 near-permutation 矩阵 + alternating_large β + 小 K 的组合。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_exp_mf1a_adversarial_monotonicity_20260523T173639"
}
```

</details>

---
