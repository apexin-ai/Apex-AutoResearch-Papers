# code llama semisynthetic rmse

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_code_llama-semisynthetic-rmse_20260521T204338.jsonl`
- **Structured JSON:** [`3e90c9037e7784e35ee3.json`](../../sessions/3e/3e90c9037e7784e35ee3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-21T20:51:29.486349+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/src/experiment_runner.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/src/experiment_runner.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T20:51:29.486660+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/ec_hte_llm_annotation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T20:51:29.486847+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/src/hb_confusion.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/src/hb_confusion.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T20:51:29.486994+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/ec_hte_llm_annotation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T20:51:29.487118+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/src/dgp.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/src/dgp.py"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T20:51:29.487235+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/ec_hte_llm_annotation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T20:51:29.487350+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "src/correction*.py",
  "path": "/home/ubuntu/ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Glob",
  "tool_args": {
    "pattern": "src/correction*.py",
    "path": "/home/ubuntu/ec_hte_llm_annotation"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T20:51:29.487463+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T20:51:29.487598+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/ec_hte_llm_annotation -type f | head -80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/ec_hte_llm_annotation -type f | head -80"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T20:51:29.487744+00:00_

/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py
/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py
/home/ubuntu/ec_hte_llm_annotation/scripts/explore_tweeteval.py
/home/ubuntu/ec_hte_llm_annotation/scripts/fig1_bias_mechanism.py
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py
/home/ubuntu/ec_hte_llm_annotation/exp004_hate_speech.py
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py
/home/ubuntu/ec_hte_llm_annotation/.venv/.gitignore
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/get_objgraph
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/undill
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/pip3.14
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/activate.fish
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/httpx
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/activate
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/datasets-cli
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/hf
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/get_gprof
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/normalizer
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/tiny-agents
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/Activate.ps1
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/typer
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/numba
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/pytensor-cache
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/f2py
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/pygmentize
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/pip
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/activate.csh
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/huggingface-cli
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/pip3
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/markdown-it
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/tqdm
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/numpy-config
/home/ubuntu/ec_hte_llm_annotation/.venv/pyvenv.cfg
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/utils.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-
…[truncated 4939 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T20:51:29.487944+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/ec_hte_llm_annotation -maxdepth 1 -type f -name \"*.py\" | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/ec_hte_llm_annotation -maxdepth 1 -type f -name \"*.py\" | sort"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T20:51:29.488081+00:00_

/home/ubuntu/ec_hte_llm_annotation/draw_fig2.py
/home/ubuntu/ec_hte_llm_annotation/draw_fig3.py
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py
/home/ubuntu/ec_hte_llm_annotation/exp002_bias_bound.py
/home/ubuntu/ec_hte_llm_annotation/exp003_tweeteval.py
/home/ubuntu/ec_hte_llm_annotation/exp004_hate_speech.py
/home/ubuntu/ec_hte_llm_annotation/exp005_diagnostic_criterion.py
/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py
/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py
/home/ubuntu/ec_hte_llm_annotation/exp008_filter_analysis.py
/home/ubuntu/ec_hte_llm_annotation/exp008_gpt55_annotate.py
/home/ubuntu/ec_hte_llm_annotation/exp008_gpt5x_annotate.py
/home/ubuntu/ec_hte_llm_annotation/exp008_multi_llm.py
/home/ubuntu/ec_hte_llm_annotation/exp010_misspecified_subgroups.py
/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py
/home/ubuntu/ec_hte_llm_annotation/exp013_boundary_condition.py
/home/ubuntu/ec_hte_llm_annotation/exp014_asymmetric.py
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py
/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py
/home/ubuntu/ec_hte_llm_annotation/exp018_multiplicative_dgp.py
/home/ubuntu/ec_hte_llm_annotation/exp019_pz1_sweep.py
/home/ubuntu/ec_hte_llm_annotation/exp020_kappa_sweep.py
/home/ubuntu/ec_hte_llm_annotation/exp021_seeds_supplement.py
/home/ubuntu/ec_hte_llm_annotation/mvp_simulation.py
/home/ubuntu/ec_hte_llm_annotation/pilot_gemini_annotation.py
/home/ubuntu/ec_hte_llm_annotation/pilot_llm_annotation.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T20:51:29.488209+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/ 2>/dev/null || echo \"directory does not exist\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/ 2>/dev/null || echo \"directory does not exist\""
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T20:51:29.488371+00:00_

total 156
drwxr-xr-x  2 ubuntu ubuntu  4096 May 21 20:40 .
drwxr-xr-x 14 ubuntu ubuntu  4096 May 21 20:38 ..
-rw-r--r--  1 ubuntu ubuntu 15564 May 21 20:40 analyze_llama.py
-rw-r--r--  1 ubuntu ubuntu 61636 May 21 20:38 llama31_8b_balanced.csv
-rw-r--r--  1 ubuntu ubuntu  3096 May 21 20:40 llama_analysis.md
-rw-r--r--  1 ubuntu ubuntu   256 May 21 20:40 llama_metrics.csv
-rw-r--r--  1 ubuntu ubuntu 60634 May 21 20:38 pilot_gemini_annotations.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T20:51:29.488547+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T20:51:29.488848+00:00_

1	"""
2	exp-015: Semi-Real Confusion Matrix EC-HTE Experiment.
3	
4	Uses real asymmetric confusion matrices from GPT-4.1 TweetEval pilot annotations.
5	Ground truth CATE is synthetic, but CMs come from real LLM pilot data.
6	
7	4 subgroups with real asymmetric CMs (from pilot GPT-4.1 annotations, n>=10 only):
8	  S0 (False_medium): FPR=0.054, FNR=0.526, weight=0.38
9	  S1 (False_short):  FPR=0.101, FNR=0.300, weight=0.22
10	  S2 (True_short):   FPR=0.143, FNR=0.308, weight=0.14
11	  S3 (True_medium):  FPR=0.194, FNR=0.222, weight=0.25
12	
13	Output:
14	  results/exp015_semi_real_raw.csv
15	  results/exp015_semi_real_summary.csv
16	  results/exp015_semi_real_analysis.md
17	
18	Usage: python3 exp015_semi_real_cm.py --n-mc 100
19	"""
20	
21	import argparse
22	import time
23	import warnings
24	import numpy as np
25	import pandas as pd
26	from scipy.special import gammaln
27	
28	warnings.filterwarnings('ignore')
29	
30	# === Config ===
31	
32	N = 5000
33	N_EXPERTS = [100, 250, 500]
34	SEED_BASE = 0
35	
36	SUBGROUP_LABELS = ['S0', 'S1', 'S2', 'S3']
37	SUBGROUP_WEIGHTS = np.array([0.38, 0.22, 0.14, 0.25])
38	SUBGROUP_WEIGHTS = SUBGROUP_WEIGHTS / SUBGROUP_WEIGHTS.sum()
39	
40	# Real asymmetric CMs from GPT-4.1 pilot (FPR, FNR per subgroup)
41	SUBGROUP_CM = {
42	    'S0': {'fpr': 0.054, 'fnr': 0.526},
43	    'S1': {'fpr': 0.101, 'fnr': 0.300},
44	    'S2': {'fpr': 0.143, 'fnr': 0.308},
45	    'S3': {'fpr': 0.194, 'fnr': 0.222},
46	}
47	
48	P_Z1 = 0.18  # P(Z=1) from pilot overall
49	P_T1 = 0.5
50	
51	
52	def get_cm_matrix(fpr, fnr):
53	    """Build 2x2 confusion matrix: M[z_true, z_obs]."""
54	    return np.array([[1 - fpr, fpr],
55	                     [fnr, 1 - fnr]])
56	
57	
58	# True CATE by (z, subgroup)
59	def true_tau(z, s_idx):
60	    if z == 0:
61	        return 0.3 + 0.1 * s_idx
62	    else:
63	        return 0.8 - 0.15 * s_idx
64	
65	
66	# === Core Estimators ===
67	
68	def diff_in_means(Y, T, mask):
69	    t1 = mask & (T == 1)
70	    t0 = mask & (T == 0)
71	    n
…[truncated 21934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T20:51:29.489028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp014_asymmetric.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp014_asymmetric.py"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T20:51:29.489331+00:00_

1	"""
2	exp014_asymmetric.py — Asymmetric Misclassification Verification (exp-014)
3	
4	Verifies the bias product structure under FPR != FNR and demonstrates
5	EC-HTE effectiveness in asymmetric scenarios.
6	
7	Key identity: bias(z, s) = delta_tau * [B_s]_{z,1}
8	where B_s = M_global^{-1} M_s - I.
9	"""
10	
11	import numpy as np
12	import pandas as pd
13	import time
14	import os
15	import sys
16	
17	# ============================================================
18	# Parameters
19	# ============================================================
20	
21	N = 50000
22	N_MC = 100
23	N_EXPERT = 250
24	TAU_Z0 = 0.1
25	RESULTS_DIR = 'results'
26	os.makedirs(RESULTS_DIR, exist_ok=True)
27	
28	CONFIGS = {
29	    'config1': {'name': 'Cross-asymmetric',
30	                'fpr': [0.10, 0.25], 'fnr': [0.20, 0.10]},
31	    'config2': {'name': 'Co-directional',
32	                'fpr': [0.05, 0.20], 'fnr': [0.15, 0.30]},
33	    'config3': {'name': 'Extreme asymmetric',
34	                'fpr': [0.03, 0.30], 'fnr': [0.25, 0.05]},
35	}
36	
37	DELTA_TAUS = [0.1, 0.2, 0.3, 0.4, 0.5]
38	
39	
40	# ============================================================
41	# Core: mixing matrix and analytic bias
42	# ============================================================
43	
44	def mixing_matrix(fpr, fnr):
45	    """M[zhat,z] = P(Z=z|Zhat=zhat,S=s) under P(Z=0)=P(Z=1)=0.5."""
46	    d0 = (1.0 - fpr) + fnr
47	    d1 = fpr + (1.0 - fnr)
48	    return np.array([[(1.0 - fpr) / d0, fnr / d0],
49	                     [fpr / d1, (1.0 - fnr) / d1]])
50	
51	
52	def analytic_bias_asym(fpr_list, fnr_list, weights, tau):
53	    """Compute B_s = M_global^{-1} M_s - I and bias = B_s @ tau."""
54	    K = len(fpr_list)
55	    Ms = [mixing_matrix(fpr_list[s], fnr_list[s]) for s in range(K)]
56	    M_global = sum(weights[s] * Ms[s] for s in range(K))
57	    M_inv = np.linalg.inv(M_global)
58	    biases, Bs = {}, {}
59	    for s in range(K):
60	        B = M_inv @ Ms[s] - np.eye(2)
61	        Bs[s] = B
62	       
…[truncated 20694 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T20:51:29.489496+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T20:51:29.489793+00:00_

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
60	    S = rng.cho
…[truncated 26142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T20:51:29.490152+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_llama_semisynthetic.py",
  "content": "\"\"\"\nLlama-3.1-8B Semi-Synthetic DGP: EC-HTE vs Global vs Naive RMSE comparison.\n\nUses real per-subgroup confusion matrices from Llama-3.1-8B balanced annotations.\nGround truth CATE is synthetic; confusion matrices are empirical.\n\n4 subgroups with real asymmetric CMs:\n  False_medium: FPR=0.235, FNR=0.319, weight=193/500\n  False_short:  FPR=0.310, FNR=0.212, weight=109/500\n  True_medium:  FPR=0.219, FNR=0.258, weight=129/500\n  True_short:   FPR=0.091, FNR=0.190, weight=69/500\n\nP(Z=1) = 0.652, delta_tau = 0.3, tau(z=0)=0.35, tau(z=1)=0.65\nMethods: Naive, Global, Stratified MLE, HB EC-HTE\nn_expert=200, 20 MC seeds\n\nUsage: python3 artifacts/c1_multi_llm/run_llama_semisynthetic.py\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT = 200\nN_MC = 20\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']\nSUBGROUP_WEIGHTS = np.array([193, 109, 129, 69], dtype=float)\nSUBGROUP_WEIGHTS /= SUBGROUP_WEIGHTS.sum()\n\nSUBGROUP_CM = {\n    'False_medium': {'fpr': 0.235, 'fnr': 0.319},\n    'False_short':  {'fpr': 0.310, 'fnr': 0.212},\n    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},\n    'True_short':   {'fpr': 0.091, 'fnr': 0.190},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\nTAU_Z0 = 0.35\nTAU_Z1 = 0.65\n\n\ndef get_cm_matrix(fpr, fnr):\n    \"\"\"Build 2x2 confusion matrix: C[z_true, z_obs].\"\"\"\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Core Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    \"\"\"Global CM with Laplace smoothing.\"\"\"\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    \"\"\"Per-subgroup MLE with Laplace smoothing.\"\"\"\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    \"\"\"M[z_hat, z] = P(Z=z | Z_hat=z_hat) via Bayes' rule.\"\"\"\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === HB Gibbs Sampler ===\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=1000, n_warmup=500, n_chains=4,\n                         hp_a0=3.0, hp_b0=1.0):\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_theta = []\n    t0 = time.time()\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))\n                accepted = np.log(rng.rand()) < log_r\n                if accepted:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(accepted)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                theta_samples[it - n_warmup] = theta.copy()\n\n        all_theta.append(theta_samples)\n\n    runtime = time.time() - t0\n    theta_arr = np.stack(all_theta)\n\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n\n    return C, {'runtime_seconds': runtime}\n\n\n# === DGP ===\n\ndef generate_data(seed):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(4):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, N_EXPERT, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    # Global CM from experts\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    # Stratified MLE per-subgroup\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    # HB Gibbs\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb, _ = estimate_cm_hb_gibbs(counts, SUBGROUP_LABELS, seed=seed)\n\n    # Build per-subgroup mixing matrices\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0\n\n            # Oracle\n            th_or, se_or = diff_in_means(Y, T, s_mask & (Z == z_level))\n            ci_lo_or = th_or - 1.96 * se_or if not np.isnan(se_or) else np.nan\n            ci_hi_or = th_or + 1.96 * se_or if not np.isnan(se_or) else np.nan\n            cov_or = 1 if (not np.isnan(ci_lo_or) and ci_lo_or <= oracle_cate <= ci_hi_or) else 0\n            rows.append({\n                'seed': seed, 'method': 'oracle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_or - oracle_cate if not np.isnan(th_or) else np.nan,\n                'rmse': abs(th_or - oracle_cate) if not np.isnan(th_or) else np.nan,\n                'coverage': cov_or,\n                'cate_true': oracle_cate, 'cate_est': th_or,\n            })\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'rmse': abs(th_nv - oracle_cate) if not np.isnan(th_nv) else np.nan,\n                'coverage': cov_nv,\n                'cate_true': oracle_cate, 'cate_est': th_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells for this subgroup\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'rmse': abs(th_gc - oracle_cate) if not np.isnan(th_gc) else np.nan,\n                'coverage': cov_gc,\n                'cate_true': oracle_cate, 'cate_est': th_gc,\n            })\n\n            # Stratified MLE\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'rmse': abs(th_ml - oracle_cate) if not np.isnan(th_ml) else np.nan,\n                'coverage': cov_ml,\n                'cate_true': oracle_cate, 'cate_est': th_ml,\n            })\n\n            # HB EC-HTE\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'rmse': abs(th_hb - oracle_cate) if not np.isnan(th_hb) else np.nan,\n                'coverage': cov_hb,\n                'cate_true': oracle_cate, 'cate_est': th_hb,\n            })\n\n    return rows\n\n\n# === Aggregation ===\n\ndef aggregate_results(df_raw):\n    group_cols = ['subgroup', 'z_level', 'method']\n    rows = []\n    for keys, grp in df_raw.groupby(group_cols):\n        row = dict(zip(group_cols, keys))\n        valid = grp['bias'].dropna()\n        if len(valid) == 0:\n            continue\n        row['mean_bias'] = valid.mean()\n        row['mean_abs_bias'] = valid.abs().mean()\n        row['rmse'] = np.sqrt((valid ** 2).mean())\n        row['coverage'] = grp['coverage'].mean()\n        row['n_mc'] = len(valid)\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# === Analysis Report ===\n\ndef write_analysis(df_raw, df_summary):\n    lines = []\n    lines.append(\"# Llama-3.1-8B Semi-Synthetic EC-HTE Experiment\\n\")\n\n    lines.append(\"## Design\\n\")\n    lines.append(\"Uses **real asymmetric confusion matrices** from Llama-3.1-8B balanced annotations.\")\n    lines.append(\"Ground truth CATE is synthetic; confusion matrices are empirical.\\n\")\n\n    lines.append(\"| Subgroup | Weight | FPR | FNR | pi_s |\")\n    lines.append(\"|----------|--------|-----|-----|------|\")\n    for i, s in enumerate(SUBGROUP_LABELS):\n        cm = SUBGROUP_CM[s]\n        lines.append(f\"| {s} | {SUBGROUP_WEIGHTS[i]:.3f} | {cm['fpr']:.3f} | {cm['fnr']:.3f} | {(cm['fpr'] + cm['fnr'])/2:.3f} |\")\n    lines.append(\"\")\n\n    lines.append(f\"**Parameters**: N={N}, P(Z=1)={P_Z1}, n_expert={N_EXPERT}, \"\n                 f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1-TAU_Z0:.1f}\")\n    lines.append(f\"**MC seeds**: {N_MC}\\n\")\n\n    # Overall summary\n    lines.append(\"## Summary (averaged across subgroups and z-levels)\\n\")\n    lines.append(\"| Method | Mean |Bias| | RMSE | Coverage |\")\n    lines.append(\"|--------|-------------|------|----------|\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_summary[df_summary['method'] == m]\n        if len(sub) > 0:\n            lines.append(f\"| {m} | {sub['mean_abs_bias'].mean():.4f} | \"\n                         f\"{sub['rmse'].mean():.4f} | {sub['coverage'].mean():.3f} |\")\n    lines.append(\"\")\n\n    # Per-subgroup breakdown\n    lines.append(\"## Per-Subgroup Breakdown\\n\")\n    lines.append(\"| Subgroup | Z | Method | Mean Bias | |Bias| | RMSE | Coverage |\")\n    lines.append(\"|----------|---|--------|-----------|-------|------|----------|\")\n    for s in SUBGROUP_LABELS:\n        for z in [0, 1]:\n            for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n                row = df_summary[(df_summary['subgroup'] == s) &\n                                 (df_summary['z_level'] == z) &\n                                 (df_summary['method'] == m)]\n                if len(row) > 0:\n                    r = row.iloc[0]\n                    lines.append(f\"| {s} | {z} | {m} | {r['mean_bias']:+.4f} | \"\n                                 f\"{r['mean_abs_bias']:.4f} | {r['rmse']:.4f} | {r['coverage']:.3f} |\")\n    lines.append(\"\")\n\n    # EC-HTE vs Global bias reduction\n    lines.append(\"## EC-HTE vs Global: Bias Reduction Ratio\\n\")\n    lines.append(\"| Subgroup | Z | HB |Bias| | Global |Bias| | Reduction |\")\n    lines.append(\"|----------|---|-----------|-------------|-----------|\")\n    total_hb, total_gc = 0.0, 0.0\n    n_cells = 0\n    for s in SUBGROUP_LABELS:\n        for z in [0, 1]:\n            hb = df_summary[(df_summary['subgroup'] == s) & (df_summary['z_level'] == z) &\n                            (df_summary['method'] == 'hb_ec_hte')]\n            gc = df_summary[(df_summary['subgroup'] == s) & (df_summary['z_level'] == z) &\n                            (df_summary['method'] == 'global_corrected')]\n            if len(hb) > 0 and len(gc) > 0:\n                hb_b = hb.iloc[0]['mean_abs_bias']\n                gc_b = gc.iloc[0]['mean_abs_bias']\n                red = (gc_b - hb_b) / gc_b * 100 if gc_b > 1e-6 else 0\n                lines.append(f\"| {s} | {z} | {hb_b:.4f} | {gc_b:.4f} | {red:+.1f}% |\")\n                total_hb += hb_b\n                total_gc += gc_b\n                n_cells += 1\n    if n_cells > 0:\n        avg_red = (total_gc / n_cells - total_hb / n_cells) / (total_gc / n_cells) * 100\n        lines.append(f\"| **Average** | | {total_hb/n_cells:.4f} | {total_gc/n_cells:.4f} | {avg_red:+.1f}% |\")\n    lines.append(\"\")\n\n    # Conclusion\n    lines.append(\"## Conclusion\\n\")\n\n    hb_all = df_summary[df_summary['method'] == 'hb_ec_hte']\n    gc_all = df_summary[df_summary['method'] == 'global_corrected']\n    nv_all = df_summary[df_summary['method'] == 'naive']\n    ml_all = df_summary[df_summary['method'] == 'stratified_mle']\n\n    if len(hb_all) > 0:\n        lines.append(f\"- **Naive**: RMSE={nv_all['rmse'].mean():.4f}, |Bias|={nv_all['mean_abs_bias'].mean():.4f}, Coverage={nv_all['coverage'].mean():.3f}\")\n        lines.append(f\"- **Global**: RMSE={gc_all['rmse'].mean():.4f}, |Bias|={gc_all['mean_abs_bias'].mean():.4f}, Coverage={gc_all['coverage'].mean():.3f}\")\n        lines.append(f\"- **Stratified MLE**: RMSE={ml_all['rmse'].mean():.4f}, |Bias|={ml_all['mean_abs_bias'].mean():.4f}, Coverage={ml_all['coverage'].mean():.3f}\")\n        lines.append(f\"- **HB EC-HTE**: RMSE={hb_all['rmse'].mean():.4f}, |Bias|={hb_all['mean_abs_bias'].mean():.4f}, Coverage={hb_all['coverage'].mean():.3f}\")\n\n        naive_rmse = nv_all['rmse'].mean()\n        gc_rmse = gc_all['rmse'].mean()\n        hb_rmse = hb_all['rmse'].mean()\n\n        lines.append(f\"\\nEC-HTE reduces RMSE by {(gc_rmse - hb_rmse)/gc_rmse*100:+.1f}% vs Global, \"\n                     f\"{(naive_rmse - hb_rmse)/naive_rmse*100:+.1f}% vs Naive.\")\n\n        gc_bias = gc_all['mean_abs_bias'].mean()\n        hb_bias = hb_all['mean_abs_bias'].mean()\n        nv_bias = nv_all['mean_abs_bias'].mean()\n        lines.append(f\"EC-HTE reduces |Bias| by {(gc_bias - hb_bias)/gc_bias*100:+.1f}% vs Global, \"\n                     f\"{(nv_bias - hb_bias)/nv_bias*100:+.1f}% vs Naive.\")\n\n        hb_cov = hb_all['coverage'].mean()\n        gc_cov = gc_all['coverage'].mean()\n        nv_cov = nv_all['coverage'].mean()\n        lines.append(f\"\\nCoverage: Naive={nv_cov:.3f}, Global={gc_cov:.3f}, HB={hb_cov:.3f} (target=0.95)\")\n\n        if hb_bias < gc_bias:\n            lines.append(\"\\n**EC-HTE improves bias over Global under real Llama CMs.**\")\n        else:\n            lines.append(\"\\n**EC-HTE does NOT improve bias over Global under real Llama CMs.**\")\n\n    report = \"\\n\".join(lines)\n    outpath = 'artifacts/c1_multi_llm/llama_semisynthetic_analysis.md'\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"Llama-3.1-8B Semi-Synthetic EC-HTE Experiment\")\n    print(f\"N={N}, n_expert={N_EXPERT}, n_mc={N_MC}, P(Z=1)={P_Z1}\")\n    print(f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1-TAU_Z0:.1f}\")\n    print(\"Subgroup CMs:\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.3f}, FNR={cm['fnr']:.3f}\")\n    print()\n\n    # Dry run: 1 seed\n    print(\"=== Dry run (1 seed) ===\")\n    data = generate_data(SEED_BASE)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    print(f\"Dry run OK: {len(df_dry)} rows\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n    print()\n\n    # Full run\n    print(f\"=== Full run ({N_MC} seeds) ===\")\n    results = []\n    t0 = time.time()\n    for mc in range(N_MC):\n        seed = SEED_BASE + mc\n        data = generate_data(seed)\n        mc_rows = run_one_mc(data, seed)\n        results.extend(mc_rows)\n        elapsed = time.time() - t0\n        eta = elapsed / (mc + 1) * (N_MC - mc - 1)\n        print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(results)\n    df_summary = aggregate_results(df_raw)\n\n    # Save results CSV\n    col_order = ['seed', 'method', 'subgroup', 'z_level', 'bias', 'rmse', 'coverage', 'cate_true', 'cate_est']\n    df_raw[col_order].to_csv('artifacts/c1_multi_llm/llama_semisynthetic_results.csv', index=False)\n    print(f\"Saved llama_semisynthetic_results.csv ({len(df_raw)} rows)\")\n\n    # Write analysis\n    write_analysis(df_raw, df_summary)\n\n    # Print summary\n    print(\"\\n=== Summary ===\\n\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_summary[df_summary['method'] == m]\n        if len(sub) > 0:\n            print(f\"  {m:20s}: |bias|={sub['mean_abs_bias'].mean():.4f}  \"\n                  f\"rmse={sub['rmse'].mean():.4f}  cov={sub['coverage'].mean():.3f}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_llama_semisynthetic.py",
    "content": "\"\"\"\nLlama-3.1-8B Semi-Synthetic DGP: EC-HTE vs Global vs Naive RMSE comparison.\n\nUses real per-subgroup confusion matrices from Llama-3.1-8B balanced annotations.\nGround truth CATE is synthetic; confusion matrices are empirical.\n\n4 subgroups with real asymmetric CMs:\n  False_medium: FPR=0.235, FNR=0.319, weight=193/500\n  False_short:  FPR=0.310, FNR=0.212, weight=109/500\n  True_medium:  FPR=0.219, FNR=0.258, weight=129/500\n  True_short:   FPR=0.091, FNR=0.190, weight=69/500\n\nP(Z=1) = 0.652, delta_tau = 0.3, tau(z=0)=0.35, tau(z=1)=0.65\nMethods: Naive, Global, Stratified MLE, HB EC-HTE\nn_expert=200, 20 MC seeds\n\nUsage: python3 artifacts/c1_multi_llm/run_llama_semisynthetic.py\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT = 200\nN_MC = 20\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']\nSUBGROUP_WEIGHTS = np.array([193, 109, 129, 69], dtype=float)\nSUBGROUP_WEIGHTS /= SUBGROUP_WEIGHTS.sum()\n\nSUBGROUP_CM = {\n    'False_medium': {'fpr': 0.235, 'fnr': 0.319},\n    'False_short':  {'fpr': 0.310, 'fnr': 0.212},\n    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},\n    'True_short':   {'fpr': 0.091, 'fnr': 0.190},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\nTAU_Z0 = 0.35\nTAU_Z1 = 0.65\n\n\ndef get_cm_matrix(fpr, fnr):\n    \"\"\"Build 2x2 confusion matrix: C[z_true, z_obs].\"\"\"\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Core Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    \"\"\"Global CM with Laplace smoothing.\"\"\"\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    \"\"\"Per-subgroup MLE with Laplace smoothing.\"\"\"\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    \"\"\"M[z_hat, z] = P(Z=z | Z_hat=z_hat) via Bayes' rule.\"\"\"\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === HB Gibbs Sampler ===\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=1000, n_warmup=500, n_chains=4,\n                         hp_a0=3.0, hp_b0=1.0):\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_theta = []\n    t0 = time.time()\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))\n                accepted = np.log(rng.rand()) < log_r\n                if accepted:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(accepted)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                theta_samples[it - n_warmup] = theta.copy()\n\n        all_theta.append(theta_samples)\n\n    runtime = time.time() - t0\n    theta_arr = np.stack(all_theta)\n\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n\n    return C, {'runtime_seconds': runtime}\n\n\n# === DGP ===\n\ndef generate_data(seed):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(4):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, N_EXPERT, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    # Global CM from experts\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    # Stratified MLE per-subgroup\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    # HB Gibbs\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb, _ = estimate_cm_hb_gibbs(counts, SUBGROUP_LABELS, seed=seed)\n\n    # Build per-subgroup mixing matrices\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0\n\n            # Oracle\n            th_or, se_or = diff_in_means(Y, T, s_mask & (Z == z_level))\n            ci_lo_or = th_or - 1.96 * se_or if not np.isnan(se_or) else np.nan\n            ci_hi_or = th_or + 1.96 * se_or if not np.isnan(se_or) else np.nan\n            cov_or = 1 if (not np.isnan(ci_lo_or) and ci_lo_or <= oracle_cate <= ci_hi_or) else 0\n            rows.append({\n                'seed': seed, 'method': 'oracle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_or - oracle_cate if not np.isnan(th_or) else np.nan,\n                'rmse': abs(th_or - oracle_cate) if not np.isnan(th_or) else np.nan,\n                'coverage': cov_or,\n                'cate_true': oracle_cate, 'cate_est': th_or,\n            })\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'rmse': abs(th_nv - oracle_cate) if not np.isnan(th_nv) else np.nan,\n                'coverage': cov_nv,\n                'cate_true': oracle_cate, 'cate_est': th_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells for this subgroup\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'rmse': abs(th_gc - oracle_cate) if not np.isnan(th_gc) else np.nan,\n                'coverage': cov_gc,\n                'cate_true': oracle_cate, 'cate_est': th_gc,\n            })\n\n            # Stratified MLE\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'rmse': abs(th_ml - oracle_cate) if not np.isnan(th_ml) else np.nan,\n                'coverage': cov_ml,\n                'cate_true': oracle_cate, 'cate_est': th_ml,\n            })\n\n            # HB EC-HTE\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'rmse': abs(th_hb - oracle_cate) if not np.isnan(th_hb) else np.nan,\n                'coverage': cov_hb,\n                'cate_true': oracle_cate, 'cate_est': th_hb,\n            })\n\n    return rows\n\n\n# === Aggregation ===\n\ndef aggregate_results(df_raw):\n    group_cols = ['subgroup', 'z_level', 'method']\n    rows = []\n    for keys, grp in df_raw.groupby(group_cols):\n        row = dict(zip(group_cols, keys))\n        valid = grp['bias'].dropna()\n        if len(valid) == 0:\n            continue\n        row['mean_bias'] = valid.mean()\n        row['mean_abs_bias'] = valid.abs().mean()\n        row['rmse'] = np.sqrt((valid ** 2).mean())\n        row['coverage'] = grp['coverage'].mean()\n        row['n_mc'] = len(valid)\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# === Analysis Report ===\n\ndef write_analysis(df_raw, df_summary):\n    lines = []\n    lines.append(\"# Llama-3.1-8B Semi-Synthetic EC-HTE Experiment\\n\")\n\n    lines.append(\"## Design\\n\")\n    lines.append(\"Uses **real asymmetric confusion matrices** from Llama-3.1-8B balanced annotations.\")\n    lines.append(\"Ground truth CATE is synthetic; confusion matrices are empirical.\\n\")\n\n    lines.append(\"| Subgroup | Weight | FPR | FNR | pi_s |\")\n    lines.append(\"|----------|--------|-----|-----|------|\")\n    for i, s in enumerate(SUBGROUP_LABELS):\n        cm = SUBGROUP_CM[s]\n        lines.append(f\"| {s} | {SUBGROUP_WEIGHTS[i]:.3f} | {cm['fpr']:.3f} | {cm['fnr']:.3f} | {(cm['fpr'] + cm['fnr'])/2:.3f} |\")\n    lines.append(\"\")\n\n    lines.append(f\"**Parameters**: N={N}, P(Z=1)={P_Z1}, n_expert={N_EXPERT}, \"\n                 f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1-TAU_Z0:.1f}\")\n    lines.append(f\"**MC seeds**: {N_MC}\\n\")\n\n    # Overall summary\n    lines.append(\"## Summary (averaged across subgroups and z-levels)\\n\")\n    lines.append(\"| Method | Mean |Bias| | RMSE | Coverage |\")\n    lines.append(\"|--------|-------------|------|----------|\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_summary[df_summary['method'] == m]\n        if len(sub) > 0:\n            lines.append(f\"| {m} | {sub['mean_abs_bias'].mean():.4f} | \"\n                         f\"{sub['rmse'].mean():.4f} | {sub['coverage'].mean():.3f} |\")\n    lines.append(\"\")\n\n    # Per-subgroup breakdown\n    lines.append(\"## Per-Subgroup Breakdown\\n\")\n    lines.append(\"| Subgroup | Z | Method | Mean Bias | |Bias| | RMSE | Coverage |\")\n    lines.append(\"|----------|---|--------|-----------|-------|------|----------|\")\n    for s in SUBGROUP_LABELS:\n        for z in [0, 1]:\n            for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n                row = df_summary[(df_summary['subgroup'] == s) &\n                                 (df_summary['z_level'] == z) &\n                                 (df_summary['method'] == m)]\n                if len(row) > 0:\n                    r = row.iloc[0]\n                    lines.append(f\"| {s} | {z} | {m} | {r['mean_bias']:+.4f} | \"\n                                 f\"{r['mean_abs_bias']:.4f} | {r['rmse']:.4f} | {r['coverage']:.3f} |\")\n    lines.append(\"\")\n\n    # EC-HTE vs Global bias reduction\n    lines.append(\"## EC-HTE vs Global: Bias Reduction Ratio\\n\")\n    lines.append(\"| Subgroup | Z | HB |Bias| | Global |Bias| | Reduction |\")\n    lines.append(\"|----------|---|-----------|-------------|-----------|\")\n    total_hb, total_gc = 0.0, 0.0\n    n_cells = 0\n    for s in SUBGROUP_LABELS:\n        for z in [0, 1]:\n            hb = df_summary[(df_summary['subgroup'] == s) & (df_summary['z_level'] == z) &\n                            (df_summary['method'] == 'hb_ec_hte')]\n            gc = df_summary[(df_summary['subgroup'] == s) & (df_summary['z_level'] == z) &\n                            (df_summary['method'] == 'global_corrected')]\n            if len(hb) > 0 and len(gc) > 0:\n                hb_b = hb.iloc[0]['mean_abs_bias']\n                gc_b = gc.iloc[0]['mean_abs_bias']\n                red = (gc_b - hb_b) / gc_b * 100 if gc_b > 1e-6 else 0\n                lines.append(f\"| {s} | {z} | {hb_b:.4f} | {gc_b:.4f} | {red:+.1f}% |\")\n                total_hb += hb_b\n                total_gc += gc_b\n                n_cells += 1\n    if n_cells > 0:\n        avg_red = (total_gc / n_cells - total_hb / n_cells) / (total_gc / n_cells) * 100\n        lines.append(f\"| **Average** | | {total_hb/n_cells:.4f} | {total_gc/n_cells:.4f} | {avg_red:+.1f}% |\")\n    lines.append(\"\")\n\n    # Conclusion\n    lines.append(\"## Conclusion\\n\")\n\n    hb_all = df_summary[df_summary['method'] == 'hb_ec_hte']\n    gc_all = df_summary[df_summary['method'] == 'global_corrected']\n    nv_all = df_summary[df_summary['method'] == 'naive']\n    ml_all = df_summary[df_summary['method'] == 'stratified_mle']\n\n    if len(hb_all) > 0:\n        lines.append(f\"- **Naive**: RMSE={nv_all['rmse'].mean():.4f}, |Bias|={nv_all['mean_abs_bias'].mean():.4f}, Coverage={nv_all['coverage'].mean():.3f}\")\n        lines.append(f\"- **Global**: RMSE={gc_all['rmse'].mean():.4f}, |Bias|={gc_all['mean_abs_bias'].mean():.4f}, Coverage={gc_all['coverage'].mean():.3f}\")\n        lines.append(f\"- **Stratified MLE**: RMSE={ml_all['rmse'].mean():.4f}, |Bias|={ml_all['mean_abs_bias'].mean():.4f}, Coverage={ml_all['coverage'].mean():.3f}\")\n        lines.append(f\"- **HB EC-HTE**: RMSE={hb_all['rmse'].mean():.4f}, |Bias|={hb_all['mean_abs_bias'].mean():.4f}, Coverage={hb_all['coverage'].mean():.3f}\")\n\n        naive_rmse = nv_all['rmse'].mean()\n        gc_rmse = gc_all['rmse'].mean()\n        hb_rmse = hb_all['rmse'].mean()\n\n        lines.append(f\"\\nEC-HTE reduces RMSE by {(gc_rmse - hb_rmse)/gc_rmse*100:+.1f}% vs Global, \"\n                     f\"{(naive_rmse - hb_rmse)/naive_rmse*100:+.1f}% vs Naive.\")\n\n        gc_bias = gc_all['mean_abs_bias'].mean()\n        hb_bias = hb_all['mean_abs_bias'].mean()\n        nv_bias = nv_all['mean_abs_bias'].mean()\n        lines.append(f\"EC-HTE reduces |Bias| by {(gc_bias - hb_bias)/gc_bias*100:+.1f}% vs Global, \"\n                     f\"{(nv_bias - hb_bias)/nv_bias*100:+.1f}% vs Naive.\")\n\n        hb_cov = hb_all['coverage'].mean()\n        gc_cov = gc_all['coverage'].mean()\n        nv_cov = nv_all['coverage'].mean()\n        lines.append(f\"\\nCoverage: Naive={nv_cov:.3f}, Global={gc_cov:.3f}, HB={hb_cov:.3f} (target=0.95)\")\n\n        if hb_bias < gc_bias:\n            lines.append(\"\\n**EC-HTE improves bias over Global under real Llama CMs.**\")\n        else:\n            lines.append(\"\\n**EC-HTE does NOT improve bias over Global under real Llama CMs.**\")\n\n    report = \"\\n\".join(lines)\n    outpath = 'artifacts/c1_multi_llm/llama_semisynthetic_analysis.md'\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"Llama-3.1-8B Semi-Synthetic EC-HTE Experiment\")\n    print(f\"N={N}, n_expert={N_EXPERT}, n_mc={N_MC}, P(Z=1)={P_Z1}\")\n    print(f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1-TAU_Z0:.1f}\")\n    print(\"Subgroup CMs:\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.3f}, FNR={cm['fnr']:.3f}\")\n    print()\n\n    # Dry run: 1 seed\n    print(\"=== Dry run (1 seed) ===\")\n    data = generate_data(SEED_BASE)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    print(f\"Dry run OK: {len(df_dry)} rows\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n    print()\n\n    # Full run\n    print(f\"=== Full run ({N_MC} seeds) ===\")\n    results = []\n    t0 = time.time()\n    for mc in range(N_MC):\n        seed = SEED_BASE + mc\n        data = generate_data(seed)\n        mc_rows = run_one_mc(data, seed)\n        results.extend(mc_rows)\n        elapsed = time.time() - t0\n        eta = elapsed / (mc + 1) * (N_MC - mc - 1)\n        print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(results)\n    df_summary = aggregate_results(df_raw)\n\n    # Save results CSV\n    col_order = ['seed', 'method', 'subgroup', 'z_level', 'bias', 'rmse', 'coverage', 'cate_true', 'cate_est']\n    df_raw[col_order].to_csv('artifacts/c1_multi_llm/llama_semisynthetic_results.csv', index=False)\n    print(f\"Saved llama_semisynthetic_results.csv ({len(df_raw)} rows)\")\n\n    # Write analysis\n    write_analysis(df_raw, df_summary)\n\n    # Print summary\n    print(\"\\n=== Summary ===\\n\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_summary[df_summary['method'] == m]\n        if len(sub) > 0:\n            print(f\"  {m:20s}: |bias|={sub['mean_abs_bias'].mean():.4f}  \"\n                  f\"rmse={sub['rmse'].mean():.4f}  cov={sub['coverage'].mean():.3f}\")\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T20:51:29.490544+00:00_

File created successfully at: /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_llama_semisynthetic.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T20:51:29.490693+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": ".venv/bin/python artifacts/c1_multi_llm/run_llama_semisynthetic.py 2>&1",
  "timeout": "600000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Bash",
  "tool_args": {
    "command": ".venv/bin/python artifacts/c1_multi_llm/run_llama_semisynthetic.py 2>&1",
    "timeout": "600000"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T20:51:29.490855+00:00_

Llama-3.1-8B Semi-Synthetic EC-HTE Experiment
N=5000, n_expert=200, n_mc=20, P(Z=1)=0.652
tau(z=0)=0.35, tau(z=1)=0.65, delta_tau=0.3
Subgroup CMs:
  False_medium: FPR=0.235, FNR=0.319
  False_short: FPR=0.310, FNR=0.212
  True_medium: FPR=0.219, FNR=0.258
  True_short: FPR=0.091, FNR=0.190

=== Dry run (1 seed) ===
Dry run OK: 40 rows
  oracle              : mean |bias| = 0.0705
  naive               : mean |bias| = 0.0796
  global_corrected    : mean |bias| = 0.1348
  stratified_mle      : mean |bias| = 0.3423
  hb_ec_hte           : mean |bias| = 0.3354

=== Full run (20 seeds) ===
  [1/20] 1s elapsed, ETA 16s
  [2/20] 2s elapsed, ETA 16s
  [3/20] 3s elapsed, ETA 15s
  [4/20] 3s elapsed, ETA 14s
  [5/20] 4s elapsed, ETA 13s
  [6/20] 5s elapsed, ETA 12s
  [7/20] 6s elapsed, ETA 11s
  [8/20] 7s elapsed, ETA 10s
  [9/20] 8s elapsed, ETA 9s
  [10/20] 9s elapsed, ETA 9s
  [11/20] 9s elapsed, ETA 8s
  [12/20] 10s elapsed, ETA 7s
  [13/20] 11s elapsed, ETA 6s
  [14/20] 12s elapsed, ETA 5s
  [15/20] 13s elapsed, ETA 4s
  [16/20] 14s elapsed, ETA 3s
  [17/20] 15s elapsed, ETA 3s
  [18/20] 16s elapsed, ETA 2s
  [19/20] 17s elapsed, ETA 1s
  [20/20] 18s elapsed, ETA 0s

Total time: 17.6s
Saved llama_semisynthetic_results.csv (800 rows)
Wrote artifacts/c1_multi_llm/llama_semisynthetic_analysis.md

=== Summary ===

  oracle              : |bias|=0.0742  rmse=0.0896  cov=0.950
  naive               : |bias|=0.1031  rmse=0.1246  cov=0.750
  global_corrected    : |bias|=0.1525  rmse=0.1892  cov=0.856
  stratified_mle      : |bias|=0.2158  rmse=0.2808  cov=0.744
  hb_ec_hte           : |bias|=0.2183  rmse=0.2851  cov=0.750

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T20:51:29.491082+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_semisynthetic_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_semisynthetic_analysis.md"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T20:51:29.491242+00:00_

1	# Llama-3.1-8B Semi-Synthetic EC-HTE Experiment
2	
3	## Design
4	
5	Uses **real asymmetric confusion matrices** from Llama-3.1-8B balanced annotations.
6	Ground truth CATE is synthetic; confusion matrices are empirical.
7	
8	| Subgroup | Weight | FPR | FNR | pi_s |
9	|----------|--------|-----|-----|------|
10	| False_medium | 0.386 | 0.235 | 0.319 | 0.277 |
11	| False_short | 0.218 | 0.310 | 0.212 | 0.261 |
12	| True_medium | 0.258 | 0.219 | 0.258 | 0.238 |
13	| True_short | 0.138 | 0.091 | 0.190 | 0.141 |
14	
15	**Parameters**: N=5000, P(Z=1)=0.652, n_expert=200, tau(z=0)=0.35, tau(z=1)=0.65, delta_tau=0.3
16	**MC seeds**: 20
17	
18	## Summary (averaged across subgroups and z-levels)
19	
20	| Method | Mean |Bias| | RMSE | Coverage |
21	|--------|-------------|------|----------|
22	| oracle | 0.0742 | 0.0896 | 0.950 |
23	| naive | 0.1031 | 0.1246 | 0.750 |
24	| global_corrected | 0.1525 | 0.1892 | 0.856 |
25	| stratified_mle | 0.2158 | 0.2808 | 0.744 |
26	| hb_ec_hte | 0.2183 | 0.2851 | 0.750 |
27	
28	## Per-Subgroup Breakdown
29	
30	| Subgroup | Z | Method | Mean Bias | |Bias| | RMSE | Coverage |
31	|----------|---|--------|-----------|-------|------|----------|
32	| False_medium | 0 | naive | +0.1506 | 0.1506 | 0.1607 | 0.300 |
33	| False_medium | 0 | global_corrected | +0.0560 | 0.1589 | 0.1849 | 0.900 |
34	| False_medium | 0 | stratified_mle | +0.0213 | 0.2766 | 0.3654 | 0.700 |
35	| False_medium | 0 | hb_ec_hte | +0.0194 | 0.2783 | 0.3668 | 0.700 |
36	| False_medium | 1 | naive | -0.0563 | 0.0670 | 0.0815 | 0.800 |
37	| False_medium | 1 | global_corrected | -0.0067 | 0.0956 | 0.1189 | 0.850 |
38	| False_medium | 1 | stratified_mle | +0.0390 | 0.1686 | 0.2197 | 0.650 |
39	| False_medium | 1 | hb_ec_hte | +0.0401 | 0.1698 | 0.2212 | 0.650 |
40	| False_short | 0 | naive | +0.0853 | 0.1058 | 0.1388 | 0.750 |
41	| False_short | 0 | global_corrected | -0.0618 | 0.1633 | 0.2381 | 0.850 |
42	| False_short | 0 | stratified_mle | -0.0308 | 0.2819 | 0.3473 | 0.850 |
43
…[truncated 2683 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T20:51:29.491387+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -5 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_semisynthetic_results.csv && echo \"---\" && wc -l /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_semisynthetic_results.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Bash",
  "tool_args": {
    "command": "head -5 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_semisynthetic_results.csv && echo \"---\" && wc -l /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_semisynthetic_results.csv"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T20:51:29.491512+00:00_

seed,method,subgroup,z_level,bias,rmse,coverage,cate_true,cate_est
0,oracle,False_medium,0,-0.12429089725631359,0.12429089725631359,1,0.35,0.22570910274368639
0,naive,False_medium,0,0.1274304394672402,0.1274304394672402,0,0.35,0.4774304394672402
0,global_corrected,False_medium,0,-0.1444315549348372,0.1444315549348372,1,0.35,0.20556844506516278
0,stratified_mle,False_medium,0,-0.19096345128834807,0.19096345128834807,1,0.35,0.1590365487116519
---
801 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_semisynthetic_results.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T20:51:29.491695+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_llama_semisynthetic.py",
  "old_string": "        lines.append(f\"\\nEC-HTE reduces RMSE by {(gc_rmse - hb_rmse)/gc_rmse*100:+.1f}% vs Global, \"\n                     f\"{(naive_rmse - hb_rmse)/naive_rmse*100:+.1f}% vs Naive.\")\n\n        gc_bias = gc_all['mean_abs_bias'].mean()\n        hb_bias = hb_all['mean_abs_bias'].mean()\n        nv_bias = nv_all['mean_abs_bias'].mean()\n        lines.append(f\"EC-HTE reduces |Bias| by {(gc_bias - hb_bias)/gc_bias*100:+.1f}% vs Global, \"\n                     f\"{(nv_bias - hb_bias)/nv_bias*100:+.1f}% vs Naive.\")\n\n        hb_cov = hb_all['coverage'].mean()\n        gc_cov = gc_all['coverage'].mean()\n        nv_cov = nv_all['coverage'].mean()\n        lines.append(f\"\\nCoverage: Naive={nv_cov:.3f}, Global={gc_cov:.3f}, HB={hb_cov:.3f} (target=0.95)\")\n\n        if hb_bias < gc_bias:\n            lines.append(\"\\n**EC-HTE improves bias over Global under real Llama CMs.**\")\n        else:\n            lines.append(\"\\n**EC-HTE does NOT improve bias over Global under real Llama CMs.**\")",
  "new_string": "        lines.append(\"\")\n        gc_bias = gc_all['mean_abs_bias'].mean()\n        hb_bias = hb_all['mean_abs_bias'].mean()\n        nv_bias = nv_all['mean_abs_bias'].mean()\n\n        hb_cov = hb_all['coverage'].mean()\n        gc_cov = gc_all['coverage'].mean()\n        nv_cov = nv_all['coverage'].mean()\n\n        lines.append(\"### RMSE comparison\")\n        for label, r in [('HB vs Naive', (naive_rmse - hb_rmse) / naive_rmse * 100),\n                         ('HB vs Global', (gc_rmse - hb_rmse) / gc_rmse * 100),\n                         ('Global vs Naive', (naive_rmse - gc_rmse) / naive_rmse * 100)]:\n            direction = \"improves\" if r > 0 else \"worsens\"\n            lines.append(f\"- {label}: {direction} by {abs(r):.1f}%\")\n\n        lines.append(f\"\\nCoverage: Naive={nv_cov:.3f}, Global={gc_cov:.3f}, HB={hb_cov:.3f} (target=0.95)\")\n\n        # Bias-variance decomposition insight\n        hb_mean_bias_sq = (hb_all['mean_bias'] ** 2).mean()\n        hb_var = hb_all['rmse'].apply(lambda x: x**2).mean() - hb_mean_bias_sq\n        nv_mean_bias_sq = (nv_all['mean_bias'] ** 2).mean()\n        nv_var = nv_all['rmse'].apply(lambda x: x**2).mean() - nv_mean_bias_sq\n\n        lines.append(\"\\n### Bias-Variance Decomposition (MSE = Bias^2 + Var)\")\n        lines.append(f\"- Naive:   Bias^2={nv_mean_bias_sq:.4f}, Var={nv_var:.4f}, MSE={nv_mean_bias_sq+nv_var:.4f}\")\n        lines.append(f\"- HB:     Bias^2={hb_mean_bias_sq:.4f}, Var={hb_var:.4f}, MSE={hb_mean_bias_sq+hb_var:.4f}\")\n\n        lines.append(\"\\n### Interpretation\\n\")\n        if hb_bias >= nv_bias:\n            lines.append(\"EC-HTE correction **increases** total error under these conditions. \"\n                         \"The per-subgroup CM estimates (from ~28-77 expert labels per subgroup) \"\n                         \"are too noisy: the variance inflation from inverting estimated mixing matrices \"\n                         \"exceeds the bias reduction from stratified correction.\")\n            lines.append(f\"\\nWith delta_pi={0.137:.3f} (moderate CM heterogeneity) and n_expert={N_EXPERT}, \"\n                         \"the Naive estimator's attenuation bias is smaller than the correction's variance cost. \"\n                         \"EC-HTE would improve with larger expert budgets or greater CM heterogeneity.\")\n        else:\n            lines.append(\"**EC-HTE improves bias over Global under real Llama CMs.**\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_llama_semisynthetic.py",
    "old_string": "        lines.append(f\"\\nEC-HTE reduces RMSE by {(gc_rmse - hb_rmse)/gc_rmse*100:+.1f}% vs Global, \"\n                     f\"{(naive_rmse - hb_rmse)/naive_rmse*100:+.1f}% vs Naive.\")\n\n        gc_bias = gc_all['mean_abs_bias'].mean()\n        hb_bias = hb_all['mean_abs_bias'].mean()\n        nv_bias = nv_all['mean_abs_bias'].mean()\n        lines.append(f\"EC-HTE reduces |Bias| by {(gc_bias - hb_bias)/gc_bias*100:+.1f}% vs Global, \"\n                     f\"{(nv_bias - hb_bias)/nv_bias*100:+.1f}% vs Naive.\")\n\n        hb_cov = hb_all['coverage'].mean()\n        gc_cov = gc_all['coverage'].mean()\n        nv_cov = nv_all['coverage'].mean()\n        lines.append(f\"\\nCoverage: Naive={nv_cov:.3f}, Global={gc_cov:.3f}, HB={hb_cov:.3f} (target=0.95)\")\n\n        if hb_bias < gc_bias:\n            lines.append(\"\\n**EC-HTE improves bias over Global under real Llama CMs.**\")\n        else:\n            lines.append(\"\\n**EC-HTE does NOT improve bias over Global under real Llama CMs.**\")",
    "new_string": "        lines.append(\"\")\n        gc_bias = gc_all['mean_abs_bias'].mean()\n        hb_bias = hb_all['mean_abs_bias'].mean()\n        nv_bias = nv_all['mean_abs_bias'].mean()\n\n        hb_cov = hb_all['coverage'].mean()\n        gc_cov = gc_all['coverage'].mean()\n        nv_cov = nv_all['coverage'].mean()\n\n        lines.append(\"### RMSE comparison\")\n        for label, r in [('HB vs Naive', (naive_rmse - hb_rmse) / naive_rmse * 100),\n                         ('HB vs Global', (gc_rmse - hb_rmse) / gc_rmse * 100),\n                         ('Global vs Naive', (naive_rmse - gc_rmse) / naive_rmse * 100)]:\n            direction = \"improves\" if r > 0 else \"worsens\"\n            lines.append(f\"- {label}: {direction} by {abs(r):.1f}%\")\n\n        lines.append(f\"\\nCoverage: Naive={nv_cov:.3f}, Global={gc_cov:.3f}, HB={hb_cov:.3f} (target=0.95)\")\n\n        # Bias-variance decomposition insight\n        hb_mean_bias_sq = (hb_all['mean_bias'] ** 2).mean()\n        hb_var = hb_all['rmse'].apply(lambda x: x**2).mean() - hb_mean_bias_sq\n        nv_mean_bias_sq = (nv_all['mean_bias'] ** 2).mean()\n        nv_var = nv_all['rmse'].apply(lambda x: x**2).mean() - nv_mean_bias_sq\n\n        lines.append(\"\\n### Bias-Variance Decomposition (MSE = Bias^2 + Var)\")\n        lines.append(f\"- Naive:   Bias^2={nv_mean_bias_sq:.4f}, Var={nv_var:.4f}, MSE={nv_mean_bias_sq+nv_var:.4f}\")\n        lines.append(f\"- HB:     Bias^2={hb_mean_bias_sq:.4f}, Var={hb_var:.4f}, MSE={hb_mean_bias_sq+hb_var:.4f}\")\n\n        lines.append(\"\\n### Interpretation\\n\")\n        if hb_bias >= nv_bias:\n            lines.append(\"EC-HTE correction **increases** total error under these conditions. \"\n                         \"The per-subgroup CM estimates (from ~28-77 expert labels per subgroup) \"\n                         \"are too noisy: the variance inflation from inverting estimated mixing matrices \"\n                         \"exceeds the bias reduction from stratified correction.\")\n            lines.append(f\"\\nWith delta_pi={0.137:.3f} (moderate CM heterogeneity) and n_expert={N_EXPERT}, \"\n                         \"the Naive estimator's attenuation bias is smaller than the correction's variance cost. \"\n                         \"EC-HTE would improve with larger expert budgets or greater CM heterogeneity.\")\n        else:\n            lines.append(\"**EC-HTE improves bias over Global under real Llama CMs.**\")"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T20:51:29.491981+00:00_

The file /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_llama_semisynthetic.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T20:51:29.492138+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": ".venv/bin/python artifacts/c1_multi_llm/run_llama_semisynthetic.py 2>&1",
  "timeout": "600000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Bash",
  "tool_args": {
    "command": ".venv/bin/python artifacts/c1_multi_llm/run_llama_semisynthetic.py 2>&1",
    "timeout": "600000"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T20:51:29.492286+00:00_

Llama-3.1-8B Semi-Synthetic EC-HTE Experiment
N=5000, n_expert=200, n_mc=20, P(Z=1)=0.652
tau(z=0)=0.35, tau(z=1)=0.65, delta_tau=0.3
Subgroup CMs:
  False_medium: FPR=0.235, FNR=0.319
  False_short: FPR=0.310, FNR=0.212
  True_medium: FPR=0.219, FNR=0.258
  True_short: FPR=0.091, FNR=0.190

=== Dry run (1 seed) ===
Dry run OK: 40 rows
  oracle              : mean |bias| = 0.0705
  naive               : mean |bias| = 0.0796
  global_corrected    : mean |bias| = 0.1348
  stratified_mle      : mean |bias| = 0.3423
  hb_ec_hte           : mean |bias| = 0.3354

=== Full run (20 seeds) ===
  [1/20] 1s elapsed, ETA 17s
  [2/20] 2s elapsed, ETA 16s
  [3/20] 3s elapsed, ETA 15s
  [4/20] 3s elapsed, ETA 14s
  [5/20] 4s elapsed, ETA 13s
  [6/20] 5s elapsed, ETA 12s
  [7/20] 6s elapsed, ETA 11s
  [8/20] 7s elapsed, ETA 10s
  [9/20] 8s elapsed, ETA 10s
  [10/20] 9s elapsed, ETA 9s
  [11/20] 10s elapsed, ETA 8s
  [12/20] 10s elapsed, ETA 7s
  [13/20] 11s elapsed, ETA 6s
  [14/20] 12s elapsed, ETA 5s
  [15/20] 13s elapsed, ETA 4s
  [16/20] 14s elapsed, ETA 4s
  [17/20] 15s elapsed, ETA 3s
  [18/20] 16s elapsed, ETA 2s
  [19/20] 17s elapsed, ETA 1s
  [20/20] 18s elapsed, ETA 0s

Total time: 17.7s
Saved llama_semisynthetic_results.csv (800 rows)
Wrote artifacts/c1_multi_llm/llama_semisynthetic_analysis.md

=== Summary ===

  oracle              : |bias|=0.0742  rmse=0.0896  cov=0.950
  naive               : |bias|=0.1031  rmse=0.1246  cov=0.750
  global_corrected    : |bias|=0.1525  rmse=0.1892  cov=0.856
  stratified_mle      : |bias|=0.2158  rmse=0.2808  cov=0.744
  hb_ec_hte           : |bias|=0.2183  rmse=0.2851  cov=0.750

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T20:51:29.492419+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_semisynthetic_analysis.md",
  "offset": "75"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_semisynthetic_analysis.md",
    "offset": "75"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T20:51:29.492547+00:00_

75	| True_short | 0 | 0.2496 | 0.1483 | -68.3% |
76	| True_short | 1 | 0.1678 | 0.1535 | -9.3% |
77	| **Average** | | 0.2183 | 0.1525 | -43.1% |
78	
79	## Conclusion
80	
81	- **Naive**: RMSE=0.1246, |Bias|=0.1031, Coverage=0.750
82	- **Global**: RMSE=0.1892, |Bias|=0.1525, Coverage=0.856
83	- **Stratified MLE**: RMSE=0.2808, |Bias|=0.2158, Coverage=0.744
84	- **HB EC-HTE**: RMSE=0.2851, |Bias|=0.2183, Coverage=0.750
85	
86	### RMSE comparison
87	- HB vs Naive: worsens by 128.8%
88	- HB vs Global: worsens by 50.7%
89	- Global vs Naive: worsens by 51.8%
90	
91	Coverage: Naive=0.750, Global=0.856, HB=0.750 (target=0.95)
92	
93	### Bias-Variance Decomposition (MSE = Bias^2 + Var)
94	- Naive:   Bias^2=0.0079, Var=0.0087, MSE=0.0165
95	- HB:     Bias^2=0.0039, Var=0.0824, MSE=0.0863
96	
97	### Interpretation
98	
99	EC-HTE correction **increases** total error under these conditions. The per-subgroup CM estimates (from ~28-77 expert labels per subgroup) are too noisy: the variance inflation from inverting estimated mixing matrices exceeds the bias reduction from stratified correction.
100	
101	With delta_pi=0.137 (moderate CM heterogeneity) and n_expert=200, the Naive estimator's attenuation bias is smaller than the correction's variance cost. EC-HTE would improve with larger expert budgets or greater CM heterogeneity.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-21T20:51:29.492721+00:00_

The analysis is complete and the bias-variance decomposition confirms the story clearly:

- **Naive**: Bias^2=0.0079, Var=0.0087, MSE=0.0165
- **HB EC-HTE**: Bias^2=0.0039, Var=0.0824, MSE=0.0863

EC-HTE halves the systematic bias (0.0039 vs 0.0079) but inflates variance by ~10x (0.0824 vs 0.0087), so total MSE is 5x worse.

All outputs produced:
- `artifacts/c1_multi_llm/llama_semisynthetic_results.csv` — 800 rows (20 seeds x 4 subgroups x 2 z-levels x 5 methods)
- `artifacts/c1_multi_llm/llama_semisynthetic_analysis.md` — full analysis with summary tables, per-subgroup breakdown, bias reduction ratios, bias-variance decomposition, and interpretation

**Key finding**: Under Llama's real CMs (Δπ=0.137, moderate heterogeneity) with n_expert=200, EC-HTE correction does NOT improve over Naive. The per-subgroup CM estimates (~28-77 expert labels per subgroup) are too noisy — the variance cost from inverting estimated mixing matrices exceeds the bias reduction benefit. EC-HTE would need larger expert budgets or greater CM heterogeneity to be beneficial.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_llama-semisynthetic-rmse_20260521T204338"
}
```

</details>

---
