# code llama budget sweep k4

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_code_llama-budget-sweep-k4_20260521T210604.jsonl`
- **Structured JSON:** [`ce2a460bb1ce426cd230.json`](../../sessions/ce/ce2a460bb1ce426cd230.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-21T21:09:11.379129+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_llama_semisynthetic.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_llama_semisynthetic.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T21:09:11.379598+00:00_

1	"""
2	Llama-3.1-8B Semi-Synthetic DGP: EC-HTE vs Global vs Naive RMSE comparison.
3	
4	Uses real per-subgroup confusion matrices from Llama-3.1-8B balanced annotations.
5	Ground truth CATE is synthetic; confusion matrices are empirical.
6	
7	4 subgroups with real asymmetric CMs:
8	  False_medium: FPR=0.235, FNR=0.319, weight=193/500
9	  False_short:  FPR=0.310, FNR=0.212, weight=109/500
10	  True_medium:  FPR=0.219, FNR=0.258, weight=129/500
11	  True_short:   FPR=0.091, FNR=0.190, weight=69/500
12	
13	P(Z=1) = 0.652, delta_tau = 0.3, tau(z=0)=0.35, tau(z=1)=0.65
14	Methods: Naive, Global, Stratified MLE, HB EC-HTE
15	n_expert=200, 20 MC seeds
16	
17	Usage: python3 artifacts/c1_multi_llm/run_llama_semisynthetic.py
18	"""
19	
20	import time
21	import warnings
22	import numpy as np
23	import pandas as pd
24	from scipy.special import gammaln
25	
26	warnings.filterwarnings('ignore')
27	
28	# === Config ===
29	
30	N = 5000
31	N_EXPERT = 200
32	N_MC = 20
33	SEED_BASE = 0
34	
35	SUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']
36	SUBGROUP_WEIGHTS = np.array([193, 109, 129, 69], dtype=float)
37	SUBGROUP_WEIGHTS /= SUBGROUP_WEIGHTS.sum()
38	
39	SUBGROUP_CM = {
40	    'False_medium': {'fpr': 0.235, 'fnr': 0.319},
41	    'False_short':  {'fpr': 0.310, 'fnr': 0.212},
42	    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},
43	    'True_short':   {'fpr': 0.091, 'fnr': 0.190},
44	}
45	
46	P_Z1 = 0.652
47	P_T1 = 0.5
48	TAU_Z0 = 0.35
49	TAU_Z1 = 0.65
50	
51	
52	def get_cm_matrix(fpr, fnr):
53	    """Build 2x2 confusion matrix: C[z_true, z_obs]."""
54	    return np.array([[1 - fpr, fpr],
55	                     [fnr, 1 - fnr]])
56	
57	
58	# === Core Estimators ===
59	
60	def diff_in_means(Y, T, mask):
61	    t1 = mask & (T == 1)
62	    t0 = mask & (T == 0)
63	    n1, n0 = t1.sum(), t0.sum()
64	    if n1 < 2 or n0 < 2:
65	        return np.nan, np.nan
66	    y1, y0 = Y[t1], Y[t0]
67	    tau_hat = y1.mean() - y0.mean()
68	    se = np.sqrt(y1.var(ddof=1) / n
…[truncated 24032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T21:09:11.379878+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find MAP-EB implementation",
  "prompt": "Find any file under /home/ubuntu/ec_hte_llm_annotation that contains a MAP-EB or empirical Bayes implementation for confusion matrix estimation. Look for files matching \"gamma_sensitivity\" or \"map_eb\" or \"empirical_bayes\" patterns. Also grep for \"MAP\" or \"map_eb\" or \"empirical_bayes\" in Python files under the artifacts directory. Return the file path and the relevant function code. Search breadth: medium."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find MAP-EB implementation",
    "prompt": "Find any file under /home/ubuntu/ec_hte_llm_annotation that contains a MAP-EB or empirical Bayes implementation for confusion matrix estimation. Look for files matching \"gamma_sensitivity\" or \"map_eb\" or \"empirical_bayes\" patterns. Also grep for \"MAP\" or \"map_eb\" or \"empirical_bayes\" in Python files under the artifacts directory. Return the file path and the relevant function code. Search breadth: medium."
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T21:09:11.380076+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*gamma_sensitivity*",
  "path": "/home/ubuntu/ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*gamma_sensitivity*",
    "path": "/home/ubuntu/ec_hte_llm_annotation"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T21:09:11.380211+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T21:09:11.380337+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*map_eb*",
  "path": "/home/ubuntu/ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*map_eb*",
    "path": "/home/ubuntu/ec_hte_llm_annotation"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T21:09:11.380450+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T21:09:11.380578+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*empirical_bayes*",
  "path": "/home/ubuntu/ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*empirical_bayes*",
    "path": "/home/ubuntu/ec_hte_llm_annotation"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T21:09:11.380693+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T21:09:11.380828+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/ec_hte_llm_annotation/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.py",
    "path": "/home/ubuntu/ec_hte_llm_annotation/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T21:09:11.380947+00:00_

artifacts/failure_analysis/part1_error_patterns.py
artifacts/failure_analysis/part2_regression.py
artifacts/failure_analysis/part3_shrinkage_analysis.py
artifacts/diagnostic_revision/compute_auc.py
artifacts/exp-008/scripts/llama31_8b_annotate.py
artifacts/exp-008/scripts/qwen25_7b_annotate.py
artifacts/exp-008/scripts/mistral7b_annotate.py
artifacts/exp-008/scripts/gemma2_9b_annotate.py
artifacts/diagnostic_revision/gen_fig4_roc.py
artifacts/diagnostic_revision/compute_loocv_auc.py
artifacts/balanced_z_annotation/analyze_ec_hte.py
artifacts/balanced_z_annotation/analyze_results.py
artifacts/gamma_sensitivity/run_gamma_sweep.py
artifacts/c1_multi_llm/analyze_llama.py
artifacts/c1_multi_llm/run_llama_semisynthetic.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T21:09:11.381077+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/ec_hte_llm_annotation -type f -name \"*.py\" | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/ec_hte_llm_annotation -type f -name \"*.py\" | head -50"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T21:09:11.381203+00:00_

/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py
/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py
/home/ubuntu/ec_hte_llm_annotation/scripts/explore_tweeteval.py
/home/ubuntu/ec_hte_llm_annotation/scripts/fig1_bias_mechanism.py
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py
/home/ubuntu/ec_hte_llm_annotation/exp004_hate_speech.py
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/utils.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/impl.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/_staggered.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/__init__.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/types.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/_multiprocess/__init__.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/annotated_doc/main.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/annotated_doc/__init__.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plot_collection.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/utils.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/bf_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/ess_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/forest_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/utils_plot_types.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/convergence_dist_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plo
…[truncated 2870 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T21:09:11.381349+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "MAP|map_eb|empirical_bayes",
  "path": "/home/ubuntu/ec_hte_llm_annotation",
  "type": "py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Grep",
  "tool_args": {
    "pattern": "MAP|map_eb|empirical_bayes",
    "path": "/home/ubuntu/ec_hte_llm_annotation",
    "type": "py",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T21:09:11.381474+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/ec_hte_llm_annotation/artifacts/gamma_sensitivity/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/ec_hte_llm_annotation/artifacts/gamma_sensitivity/*.py"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T21:09:11.381581+00:00_

artifacts/gamma_sensitivity/run_gamma_sweep.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T21:09:11.381705+00:00_

Found 120 files
artifacts/gamma_sensitivity/run_gamma_sweep.py
artifacts/exp-008/scripts/gemma2_9b_annotate.py
artifacts/exp-008/scripts/mistral7b_annotate.py
artifacts/exp-008/scripts/qwen25_7b_annotate.py
artifacts/exp-008/scripts/llama31_8b_annotate.py
exp008_multi_llm.py
.venv/lib/python3.14/site-packages/datasets/formatting/jax_formatter.py
.venv/lib/python3.14/site-packages/datasets/iterable_dataset.py
.venv/lib/python3.14/site-packages/datasets/config.py
.venv/lib/python3.14/site-packages/datasets/arrow_dataset.py
.venv/lib/python3.14/site-packages/huggingface_hub/utils/_terminal.py
.venv/lib/python3.14/site-packages/huggingface_hub/utils/_http.py
.venv/lib/python3.14/site-packages/huggingface_hub/inference/_providers/_common.py
.venv/lib/python3.14/site-packages/huggingface_hub/cli/_errors.py
.venv/lib/python3.14/site-packages/huggingface_hub/cli/_cli_utils.py
.venv/lib/python3.14/site-packages/huggingface_hub/hf_file_system.py
.venv/lib/python3.14/site-packages/huggingface_hub/hf_api.py
.venv/lib/python3.14/site-packages/huggingface_hub/constants.py
.venv/lib/python3.14/site-packages/aiohttp/web_log.py
.venv/lib/python3.14/site-packages/httpx/_transports/default.py
.venv/lib/python3.14/site-packages/multiprocess/synchronize.py
.venv/lib/python3.14/site-packages/multiprocess/shared_memory.py
.venv/lib/python3.14/site-packages/click/core.py
.venv/lib/python3.14/site-packages/dill/tests/test_dictviews.py
.venv/lib/python3.14/site-packages/dill/logger.py
.venv/lib/python3.14/site-packages/dill/_dill.py
.venv/lib/python3.14/site-packages/fsspec/implementations/ftp.py
.venv/lib/python3.14/site-packages/pyarrow/parquet/core.py
.venv/lib/python3.14/site-packages/pyarrow/types.py
.venv/lib/python3.14/site-packages/yaml/scanner.py
.venv/lib/python3.14/site-packages/yaml/resolver.py
.venv/lib/python3.14/site-packages/yaml/parser.py
.venv/lib/python3.14/site-packages/yaml/emitter.py
.venv/lib/python3.14/site-packages/urllib3/util/ssl_.py
pilot_llm_annotation.py
.venv/l
…[truncated 5425 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T21:09:11.381857+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/gamma_sensitivity/run_gamma_sweep.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/gamma_sensitivity/run_gamma_sweep.py"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T21:09:11.382020+00:00_

1	#!/usr/bin/env python3
2	"""
3	Gamma prior sensitivity analysis (RD2-M5).
4	Sweeps Gamma(shape, rate=1/scale) hyperprior on alpha_0 for HB confusion matrix estimation.
5	15 configs x 20 seeds, with MLE and global baselines.
6	"""
7	
8	import argparse
9	import os
10	import sys
11	import time
12	import numpy as np
13	import pandas as pd
14	from scipy.optimize import minimize_scalar
15	from scipy.special import gammaln
16	
17	sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
18	from exp001_hb_synthetic import (
19	    N, SUBGROUP_LABELS, generate_data, get_counts,
20	    estimate_cm_mle, _dirmult_neg_ll,
21	    build_mixing_matrix, invert_mixing, diff_in_means,
22	)
23	
24	REGIME_PARAMS = {
25	    'misclass': [0.05, 0.15],
26	    'tau_z1': 0.4,
27	    'tau_z0': 0.1,
28	}
29	K = 2
30	N_EXPERT = 200
31	LABELS = SUBGROUP_LABELS[K]
32	
33	SHAPES = [1, 2, 3, 5, 10]
34	SCALES = [0.5, 1, 2]
35	N_SEEDS = 20
36	
37	
38	def estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):
39	    """MAP-EB: penalized marginal likelihood with Gamma(shape, scale) prior on alpha_0."""
40	    hp_rate = 1.0 / hp_scale
41	    k = len(labels)
42	    alpha_opt = np.zeros(2)
43	
44	    for z in [0, 1]:
45	        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]
46	        total = sum(c0 + c1 for c0, c1 in cl)
47	        if total == 0:
48	            alpha_opt[z] = hp_shape * hp_scale
49	            continue
50	
51	        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):
52	            nll = _dirmult_neg_ll(a, _cl)
53	            if a < 1e-10:
54	                return 1e10
55	            log_prior = (_shape - 1.0) * np.log(a) - _rate * a
56	            return nll - log_prior
57	
58	        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')
59	        alpha_opt[z] = res.x
60	
61	    C = {}
62	    for i, s in enumerate(labels):
63	        C_s = np.zeros((2, 2))
64	        for z in [0, 1]:
65	            a = alp
…[truncated 10919 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T21:09:11.382177+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "def.*map|def.*empirical|def.*bayes|class.*MAP|class.*EB",
  "path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/gamma_sensitivity",
  "type": "py",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Grep",
  "tool_args": {
    "pattern": "def.*map|def.*empirical|def.*bayes|class.*MAP|class.*EB",
    "path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/gamma_sensitivity",
    "type": "py",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T21:09:11.382294+00:00_

artifacts/gamma_sensitivity/run_gamma_sweep.py:38:def estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T21:09:11.382415+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "estimate_cm_hb_map_eb|MAP.*EB|empirical.*bayes|map_eb",
  "path": "/home/ubuntu/ec_hte_llm_annotation",
  "type": "py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Grep",
  "tool_args": {
    "pattern": "estimate_cm_hb_map_eb|MAP.*EB|empirical.*bayes|map_eb",
    "path": "/home/ubuntu/ec_hte_llm_annotation",
    "type": "py",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T21:09:11.382531+00:00_

Found 1 file
artifacts/gamma_sensitivity/run_gamma_sweep.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T21:09:11.382653+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/ec_hte_llm_annotation -maxdepth 1 -name \"*.py\" -type f | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/ec_hte_llm_annotation -maxdepth 1 -name \"*.py\" -type f | head -20"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T21:09:11.382766+00:00_

/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py
/home/ubuntu/ec_hte_llm_annotation/exp004_hate_speech.py
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py
/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py
/home/ubuntu/ec_hte_llm_annotation/mvp_simulation.py
/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py
/home/ubuntu/ec_hte_llm_annotation/pilot_llm_annotation.py
/home/ubuntu/ec_hte_llm_annotation/exp005_diagnostic_criterion.py
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py
/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py
/home/ubuntu/ec_hte_llm_annotation/exp021_seeds_supplement.py
/home/ubuntu/ec_hte_llm_annotation/exp008_multi_llm.py
/home/ubuntu/ec_hte_llm_annotation/exp008_filter_analysis.py
/home/ubuntu/ec_hte_llm_annotation/exp002_bias_bound.py
/home/ubuntu/ec_hte_llm_annotation/exp008_gpt55_annotate.py
/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py
/home/ubuntu/ec_hte_llm_annotation/exp019_pz1_sweep.py
/home/ubuntu/ec_hte_llm_annotation/exp008_gpt5x_annotate.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T21:09:11.382918+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T21:09:11.383058+00:00_

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
…[truncated 1611 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T21:09:11.383205+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "def.*map|def.*empirical|def.*bayes|class.*MAP",
  "path": "/home/ubuntu/ec_hte_llm_annotation",
  "type": "py",
  "output_mode": "content",
  "head_limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Grep",
  "tool_args": {
    "pattern": "def.*map|def.*empirical|def.*bayes|class.*MAP",
    "path": "/home/ubuntu/ec_hte_llm_annotation",
    "type": "py",
    "output_mode": "content",
    "head_limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-21T21:09:11.383333+00:00_

artifacts/gamma_sensitivity/run_gamma_sweep.py:38:def estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):
.venv/lib/python3.14/site-packages/arviz_stats/bayes_factor.py:10:def bayes_factor(data, var_names, ref_vals=0, return_ref_vals=False, prior=None):
.venv/lib/python3.14/site-packages/arviz_stats/base/array.py:738:    def bayesian_r2(self, mu_pred, scale=None, scale_kind="sd", circular=False):
.venv/lib/python3.14/site-packages/arviz_stats/base/diagnostics.py:1512:    def _bayesian_r2(mu_pred, scale, scale_kind, circular):
.venv/lib/python3.14/site-packages/arviz_stats/metrics.py:14:def bayesian_r2(
.venv/lib/python3.14/site-packages/toolz/sandbox/parallel.py:13:def fold(binop, seq, default=no_default, map=map, chunksize=128, combine=None):
.venv/lib/python3.14/site-packages/toolz/dicttoolz.py:73:def valmap(func, d, factory=dict):
.venv/lib/python3.14/site-packages/toolz/dicttoolz.py:89:def keymap(func, d, factory=dict):
.venv/lib/python3.14/site-packages/toolz/dicttoolz.py:105:def itemmap(func, d, factory=dict):
.venv/lib/python3.14/site-packages/patsy/mgcv_cubic_splines.py:61:def _map_cyclic(x, lbound, ubound):
.venv/lib/python3.14/site-packages/patsy/mgcv_cubic_splines.py:84:def test__map_cyclic():
.venv/lib/python3.14/site-packages/patsy/mgcv_cubic_splines.py:93:def test__map_cyclic_errors():
.venv/lib/python3.14/site-packages/toolz/tests/test_itertoolz.py:223:def test_mapcat():
.venv/lib/python3.14/site-packages/toolz/tests/test_dicttoolz.py:56:    def test_valmap(self):
.venv/lib/python3.14/site-packages/toolz/tests/test_dicttoolz.py:60:    def test_keymap(self):
.venv/lib/python3.14/site-packages/toolz/tests/test_dicttoolz.py:64:    def test_itemmap(self):
.venv/lib/python3.14/site-packages/toolz/tests/test_dicttoolz.py:253:def test_merge_with_non_dict_mappings():
.venv/lib/python3.14/site-packages/toolz/itertoolz.py:501:def mapcat(func, seqs):
.venv/lib/python3.14/site-packages/anyio/_core/_synchronization.py:409:    async def __aenter__(se
…[truncated 3704 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T21:09:11.383475+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
  "limit": "300",
  "offset": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
    "limit": "300",
    "offset": "100"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T21:09:11.383635+00:00_

100	
101	    NOTE: This assumes P(Z=0)=P(Z=1)=0.5, which is correct for this experiment's
102	    DGP. For general P(Z), use the version in exp007 that takes p_z and p_z_hat.
103	    """
104	    M = np.zeros((2, 2))
105	    for zh in [0, 1]:
106	        cs = C[0, zh] + C[1, zh]
107	        if cs > 0:
108	            M[zh, 0] = C[0, zh] / cs
109	            M[zh, 1] = C[1, zh] / cs
110	        else:
111	            M[zh, :] = 0.5
112	    return M
113	
114	
115	def invert_mixing(M, tau_obs, se_obs):
116	    det = np.linalg.det(M)
117	    if abs(det) < 1e-10:
118	        return tau_obs.copy(), se_obs.copy()
119	    Mi = np.linalg.inv(M)
120	    tau_c = Mi @ tau_obs
121	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
122	    return tau_c, se_c
123	
124	
125	def safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):
126	    """Invert mixing matrix with condition number guard.
127	
128	    When cond(M_s) > threshold, matrix inversion is numerically unstable.
129	    Falls back to naive (no correction) to avoid catastrophic amplification.
130	    """
131	    cond = np.linalg.cond(M_s)
132	    if cond > cond_threshold:
133	        return tau_obs.copy()
134	    return np.linalg.solve(M_s, tau_obs)
135	
136	
137	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
138	    """Like invert_mixing but with condition number guard."""
139	    cond = np.linalg.cond(M)
140	    if cond > cond_threshold:
141	        return tau_obs.copy(), se_obs.copy()
142	    det = np.linalg.det(M)
143	    if abs(det) < 1e-10:
144	        return tau_obs.copy(), se_obs.copy()
145	    Mi = np.linalg.inv(M)
146	    tau_c = Mi @ tau_obs
147	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
148	    return tau_c, se_c
149	
150	
151	# ── Confusion Matrix Estimators ───────────────────────────────────────────────
152	
153	def estimate_cm_mle(counts, labels):
154	    """Per-subgroup MLE with Laplace smoothing (add-1)."""
15
…[truncated 9481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T21:09:11.383823+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "estimate_cm_hb_eb|estimate_cm_hb_gibbs|estimate_cm_hb_mcmc|estimate_cm_mle",
  "path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Grep",
  "tool_args": {
    "pattern": "estimate_cm_hb_eb|estimate_cm_hb_gibbs|estimate_cm_hb_mcmc|estimate_cm_mle",
    "path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-21T21:09:11.383979+00:00_

153:def estimate_cm_mle(counts, labels):
181:def estimate_cm_hb_eb(counts, labels):
280:def estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=4000, n_warmup=2000, n_chains=4,
357:def estimate_cm_hb_mcmc(counts, labels, seed=42, draws=1000, tune=500, chains=2):
418:    C_mle = estimate_cm_mle(counts, labels)
421:        C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed)
424:            C_hb, hb_diag = estimate_cm_hb_mcmc(counts, labels, seed=seed)
426:            C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)
429:        C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)
626:        _, dg = estimate_cm_hb_gibbs(tc, ['A', 'B'], seed=9999)
640:            _, dg = estimate_cm_hb_mcmc(tc, ['A', 'B'], seed=9999)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T21:09:11.384115+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"estimate_cm_hb_map_eb\\|MAP.*EB\\|map_eb\" /home/ubuntu/ec_hte_llm_annotation --include=\"*.py\" | grep -v \".venv\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"estimate_cm_hb_map_eb\\|MAP.*EB\\|map_eb\" /home/ubuntu/ec_hte_llm_annotation --include=\"*.py\" | grep -v \".venv\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-21T21:09:11.384231+00:00_

/home/ubuntu/ec_hte_llm_annotation/artifacts/gamma_sensitivity/run_gamma_sweep.py:def estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):
/home/ubuntu/ec_hte_llm_annotation/artifacts/gamma_sensitivity/run_gamma_sweep.py:    """MAP-EB: penalized marginal likelihood with Gamma(shape, scale) prior on alpha_0."""
/home/ubuntu/ec_hte_llm_annotation/artifacts/gamma_sensitivity/run_gamma_sweep.py:    C_hb, _ = estimate_cm_hb_map_eb(counts, LABELS, hp_shape, hp_scale)
/home/ubuntu/ec_hte_llm_annotation/artifacts/gamma_sensitivity/run_gamma_sweep.py:        rows.append(make_row('hb_map_eb', thb[0], thb[1], shb[0], shb[1], pi_hat_hb))
/home/ubuntu/ec_hte_llm_annotation/artifacts/gamma_sensitivity/run_gamma_sweep.py:    hb = df[df['method'] == 'hb_map_eb']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T21:09:11.384356+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
  "limit": "30",
  "offset": "181"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
    "limit": "30",
    "offset": "181"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-21T21:09:11.384475+00:00_

181	def estimate_cm_hb_eb(counts, labels):
182	    """Empirical Bayes HB: optimize shared Dirichlet concentration, posterior mean."""
183	    k = len(labels)
184	    alpha_opt = np.zeros(2)
185	    for z in [0, 1]:
186	        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]
187	        total = sum(c0 + c1 for c0, c1 in cl)
188	        if total == 0:
189	            alpha_opt[z] = 2.0
190	            continue
191	        res = minimize_scalar(
192	            lambda a: _dirmult_neg_ll(a, cl), bounds=(0.01, 500), method='bounded')
193	        alpha_opt[z] = res.x
194	
195	    C = {}
196	    for i, s in enumerate(labels):
197	        C_s = np.zeros((2, 2))
198	        for z in [0, 1]:
199	            a = alpha_opt[z] / 2.0
200	            n = counts[i, z, :].sum()
201	            d = n + 2 * a
202	            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5
203	            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5
204	        C[s] = C_s
205	
206	    diag = {'rhat_max': np.nan, 'ess_min': np.nan, 'divergent_count': 0,
207	            'runtime_seconds': 0.0, 'hb_method': 'eb',
208	            'alpha_0_z0': alpha_opt[0], 'alpha_0_z1': alpha_opt[1]}
209	    return C, diag
210	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T21:09:11.384669+00:00_

Excellent! Now I have all the information needed. Let me provide the final comprehensive report.

## Summary

I found **MAP-EB (Maximum A Posteriori Empirical Bayes) implementations for confusion matrix estimation** in your repository. Here are the key findings:

### Files Found

**Primary File:**
- `/home/ubuntu/ec_hte_llm_annotation/artifacts/gamma_sensitivity/run_gamma_sweep.py` - Contains the main MAP-EB implementation with Gamma prior sensitivity analysis

**Supporting File:**
- `/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py` - Contains the baseline empirical Bayes implementation and helper functions

### Relevant Functions

#### 1. MAP-EB with Gamma Prior (Main Implementation)
**File:** `/home/ubuntu/ec_hte_llm_annotation/artifacts/gamma_sensitivity/run_gamma_sweep.py` (lines 38-72)

```python
def estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):
    """MAP-EB: penalized marginal likelihood with Gamma(shape, scale) prior on alpha_0."""
    hp_rate = 1.0 / hp_scale
    k = len(labels)
    alpha_opt = np.zeros(2)

    for z in [0, 1]:
        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]
        total = sum(c0 + c1 for c0, c1 in cl)
        if total == 0:
            alpha_opt[z] = hp_shape * hp_scale
            continue

        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):
            nll = _dirmult_neg_ll(a, _cl)
            if a < 1e-10:
                return 1e10
            log_prior = (_shape - 1.0) * np.log(a) - _rate * a
            return nll - log_prior

        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')
        alpha_opt[z] = res.x

    C = {}
    for i, s in enumerate(labels):
        C_s = np.zeros((2, 2))
        for z in [0, 1]:
            a = alpha_opt[z] / 2.0
            n_sz = counts[i, z, :].sum()
            d = n_sz + 2 * a
            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5
            C_s[z, 1] = (counts[i, z, 1] + a) / d
…[truncated 2781 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Agent",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T21:09:11.384863+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/gamma_sensitivity/run_gamma_sweep.py",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/gamma_sensitivity/run_gamma_sweep.py",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T21:09:11.385015+00:00_

1	#!/usr/bin/env python3
2	"""
3	Gamma prior sensitivity analysis (RD2-M5).
4	Sweeps Gamma(shape, rate=1/scale) hyperprior on alpha_0 for HB confusion matrix estimation.
5	15 configs x 20 seeds, with MLE and global baselines.
6	"""
7	
8	import argparse
9	import os
10	import sys
11	import time
12	import numpy as np
13	import pandas as pd
14	from scipy.optimize import minimize_scalar
15	from scipy.special import gammaln
16	
17	sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
18	from exp001_hb_synthetic import (
19	    N, SUBGROUP_LABELS, generate_data, get_counts,
20	    estimate_cm_mle, _dirmult_neg_ll,
21	    build_mixing_matrix, invert_mixing, diff_in_means,
22	)
23	
24	REGIME_PARAMS = {
25	    'misclass': [0.05, 0.15],
26	    'tau_z1': 0.4,
27	    'tau_z0': 0.1,
28	}
29	K = 2
30	N_EXPERT = 200
31	LABELS = SUBGROUP_LABELS[K]
32	
33	SHAPES = [1, 2, 3, 5, 10]
34	SCALES = [0.5, 1, 2]
35	N_SEEDS = 20
36	
37	
38	def estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):
39	    """MAP-EB: penalized marginal likelihood with Gamma(shape, scale) prior on alpha_0."""
40	    hp_rate = 1.0 / hp_scale
41	    k = len(labels)
42	    alpha_opt = np.zeros(2)
43	
44	    for z in [0, 1]:
45	        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]
46	        total = sum(c0 + c1 for c0, c1 in cl)
47	        if total == 0:
48	            alpha_opt[z] = hp_shape * hp_scale
49	            continue
50	
51	        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):
52	            nll = _dirmult_neg_ll(a, _cl)
53	            if a < 1e-10:
54	                return 1e10
55	            log_prior = (_shape - 1.0) * np.log(a) - _rate * a
56	            return nll - log_prior
57	
58	        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')
59	        alpha_opt[z] = res.x
60	
61	    C = {}
62	    for i, s in enumerate(labels):
63	        C_s = np.zeros((2, 2))
64	        for z in [0, 1]:
65	            a = alp
…[truncated 579 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T21:09:11.385225+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_budget_sweep_k4.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nBudget sensitivity sweep for Llama K=4 real confusion matrices.\n\nSweeps n_expert in {100, 200, 500, 1000, 2000} with 50 MC seeds each.\nUses MAP-EB instead of Gibbs for speed (250 total runs).\n\n|Bias| metric: |mean(estimate - truth) across seeds| averaged across cells.\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.optimize import minimize_scalar\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT_LIST = [100, 200, 500, 1000, 2000]\nN_MC = 50\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']\nSUBGROUP_WEIGHTS = np.array([0.386, 0.218, 0.258, 0.138])\n\nSUBGROUP_CM = {\n    'False_medium': {'fpr': 0.235, 'fnr': 0.319},\n    'False_short':  {'fpr': 0.310, 'fnr': 0.212},\n    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},\n    'True_short':   {'fpr': 0.091, 'fnr': 0.190},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\nTAU_Z0 = 0.35\nTAU_Z1 = 0.65\n\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === MAP-EB ===\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):\n    hp_rate = 1.0 / hp_scale\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = hp_shape * hp_scale\n            continue\n\n        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):\n            nll = _dirmult_neg_ll(a, _cl)\n            if a < 1e-10:\n                return 1e10\n            log_prior = (_shape - 1.0) * np.log(a) - _rate * a\n            return nll - log_prior\n\n        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n_sz = counts[i, z, :].sum()\n            d = n_sz + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    return C, alpha_opt\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\n# === DGP ===\n\ndef generate_data(seed, n_expert):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(4):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb, _ = estimate_cm_hb_map_eb(counts, SUBGROUP_LABELS)\n\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'cate_est': th_nv, 'cate_true': oracle_cate,\n                'coverage': cov_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'cate_est': th_gc, 'cate_true': oracle_cate,\n                'coverage': cov_gc,\n            })\n\n            # Stratified MLE\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'cate_est': th_ml, 'cate_true': oracle_cate,\n                'coverage': cov_ml,\n            })\n\n            # HB EC-HTE (MAP-EB)\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'cate_est': th_hb, 'cate_true': oracle_cate,\n                'coverage': cov_hb,\n            })\n\n    return rows\n\n\n# === Corrected |Bias| aggregation ===\n\ndef compute_corrected_abs_bias(df):\n    \"\"\"\n    |Bias| = average across cells of |mean(estimate - truth) across seeds|.\n    For each (method, n_expert): average over (subgroup, z_level) cells of |mean bias|.\n    \"\"\"\n    cell_bias = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias']\n                 .mean().abs().reset_index(name='abs_mean_bias'))\n    return (cell_bias.groupby(['n_expert', 'method'])['abs_mean_bias']\n            .mean().reset_index(name='abs_bias'))\n\n\ndef compute_rmse(df):\n    \"\"\"RMSE = sqrt(mean(bias^2)) averaged across cells.\"\"\"\n    cell_rmse = (df.assign(bias_sq=df['bias'] ** 2)\n                 .groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias_sq']\n                 .mean().apply(np.sqrt).reset_index(name='rmse'))\n    return (cell_rmse.groupby(['n_expert', 'method'])['rmse']\n            .mean().reset_index(name='rmse'))\n\n\ndef compute_coverage(df):\n    return (df.groupby(['n_expert', 'method'])['coverage']\n            .mean().reset_index(name='coverage'))\n\n\n# === Analysis Report ===\n\ndef write_analysis(df_raw, outpath):\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse = compute_rmse(df_raw)\n    cov = compute_coverage(df_raw)\n\n    summary = abs_bias.merge(rmse, on=['n_expert', 'method']).merge(cov, on=['n_expert', 'method'])\n\n    lines = []\n    lines.append(\"# Budget Sensitivity Sweep: Llama K=4 Real CM\\n\")\n    lines.append(\"## Design\\n\")\n    lines.append(f\"- N={N}, P(Z=1)={P_Z1}, K=4 subgroups\")\n    lines.append(f\"- tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1 - TAU_Z0:.1f}\")\n    lines.append(f\"- n_expert sweep: {N_EXPERT_LIST}\")\n    lines.append(f\"- {N_MC} MC seeds per budget\")\n    lines.append(\"- HB method: MAP-EB (Gamma(3,1) prior)\")\n    lines.append(f\"- |Bias| = avg across cells of |mean(bias) across seeds|\")\n    lines.append(\"\")\n\n    lines.append(\"## Summary Table\\n\")\n    lines.append(\"| n_expert | |Bias|_naive | |Bias|_global | |Bias|_strat | |Bias|_echte | RMSE_naive | RMSE_global | RMSE_strat | RMSE_echte | Cov_echte | HB_wins_bias? | HB_wins_rmse? |\")\n    lines.append(\"|----------|-------------|--------------|-------------|-------------|------------|-------------|------------|------------|-----------|---------------|---------------|\")\n\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        vals = {}\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            row = sub[sub['method'] == m]\n            if len(row) > 0:\n                vals[m] = {\n                    'abs_bias': row.iloc[0]['abs_bias'],\n                    'rmse': row.iloc[0]['rmse'],\n                    'coverage': row.iloc[0]['coverage'],\n                }\n            else:\n                vals[m] = {'abs_bias': np.nan, 'rmse': np.nan, 'coverage': np.nan}\n\n        hb_wins_bias = \"YES\" if vals['hb_ec_hte']['abs_bias'] < vals['naive']['abs_bias'] else \"no\"\n        hb_wins_rmse = \"YES\" if vals['hb_ec_hte']['rmse'] < vals['naive']['rmse'] else \"no\"\n\n        lines.append(\n            f\"| {ne} \"\n            f\"| {vals['naive']['abs_bias']:.4f} \"\n            f\"| {vals['global_corrected']['abs_bias']:.4f} \"\n            f\"| {vals['stratified_mle']['abs_bias']:.4f} \"\n            f\"| {vals['hb_ec_hte']['abs_bias']:.4f} \"\n            f\"| {vals['naive']['rmse']:.4f} \"\n            f\"| {vals['global_corrected']['rmse']:.4f} \"\n            f\"| {vals['stratified_mle']['rmse']:.4f} \"\n            f\"| {vals['hb_ec_hte']['rmse']:.4f} \"\n            f\"| {vals['hb_ec_hte']['coverage']:.3f} \"\n            f\"| {hb_wins_bias} \"\n            f\"| {hb_wins_rmse} |\"\n        )\n    lines.append(\"\")\n\n    # Crossover analysis\n    lines.append(\"## Crossover Analysis\\n\")\n    crossover_bias = None\n    crossover_rmse = None\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        hb = sub[sub['method'] == 'hb_ec_hte']\n        nv = sub[sub['method'] == 'naive']\n        if len(hb) > 0 and len(nv) > 0:\n            if hb.iloc[0]['abs_bias'] < nv.iloc[0]['abs_bias'] and crossover_bias is None:\n                crossover_bias = ne\n            if hb.iloc[0]['rmse'] < nv.iloc[0]['rmse'] and crossover_rmse is None:\n                crossover_rmse = ne\n\n    if crossover_bias is not None:\n        lines.append(f\"- **|Bias| crossover**: EC-HTE beats Naive at n_expert={crossover_bias}\")\n    else:\n        lines.append(\"- **|Bias| crossover**: EC-HTE never beats Naive in tested range\")\n    if crossover_rmse is not None:\n        lines.append(f\"- **RMSE crossover**: EC-HTE beats Naive at n_expert={crossover_rmse}\")\n    else:\n        lines.append(\"- **RMSE crossover**: EC-HTE never beats Naive in tested range\")\n    lines.append(\"\")\n\n    # Bias-variance decomposition per budget\n    lines.append(\"## Bias-Variance Decomposition (per budget)\\n\")\n    lines.append(\"| n_expert | Method | Bias^2 | Variance | MSE |\")\n    lines.append(\"|----------|--------|--------|----------|-----|\")\n    for ne in N_EXPERT_LIST:\n        for m in ['naive', 'hb_ec_hte']:\n            sub_df = df_raw[(df_raw['n_expert'] == ne) & (df_raw['method'] == m)]\n            cell_stats = (sub_df.groupby(['subgroup', 'z_level'])['bias']\n                          .agg(['mean', 'var', 'count']).reset_index())\n            mean_bias_sq = (cell_stats['mean'] ** 2).mean()\n            variance = cell_stats['var'].mean()\n            mse = mean_bias_sq + variance\n            lines.append(f\"| {ne} | {m} | {mean_bias_sq:.4f} | {variance:.4f} | {mse:.4f} |\")\n    lines.append(\"\")\n\n    report = \"\\n\".join(lines)\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"Budget Sensitivity Sweep: Llama K=4 Real CM\")\n    print(f\"N={N}, budgets={N_EXPERT_LIST}, seeds={N_MC}\")\n    print(f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}\")\n    print()\n\n    out_dir = 'artifacts/c1_multi_llm'\n\n    # Dry run: 1 budget, 1 seed\n    print(\"=== Dry run (n_expert=100, 1 seed) ===\")\n    data = generate_data(SEED_BASE, 100)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    df_dry['n_expert'] = 100\n    print(f\"Dry run OK: {len(df_dry)} rows, columns: {list(df_dry.columns)}\")\n    for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n    print()\n\n    # Full run\n    print(f\"=== Full run ({len(N_EXPERT_LIST)} budgets x {N_MC} seeds) ===\")\n    all_results = []\n    t0 = time.time()\n    total_runs = len(N_EXPERT_LIST) * N_MC\n    run_count = 0\n\n    for n_expert in N_EXPERT_LIST:\n        print(f\"\\n--- n_expert = {n_expert} ---\")\n        t_budget = time.time()\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            data = generate_data(seed, n_expert)\n            mc_rows = run_one_mc(data, seed)\n            for r in mc_rows:\n                r['n_expert'] = n_expert\n            all_results.extend(mc_rows)\n            run_count += 1\n            if (mc + 1) % 10 == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / run_count * (total_runs - run_count)\n                print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n        budget_time = time.time() - t_budget\n        print(f\"  n_expert={n_expert} done in {budget_time:.1f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(all_results)\n\n    # Save results CSV\n    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage']\n    df_raw[col_order].to_csv(f'{out_dir}/budget_sweep_k4_results.csv', index=False)\n    print(f\"Saved budget_sweep_k4_results.csv ({len(df_raw)} rows)\")\n\n    # Write analysis\n    write_analysis(df_raw, f'{out_dir}/budget_sweep_k4_analysis.md')\n\n    # Print summary\n    print(\"\\n=== Summary ===\")\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse_df = compute_rmse(df_raw)\n    summary = abs_bias.merge(rmse_df, on=['n_expert', 'method'])\n    for ne in N_EXPERT_LIST:\n        print(f\"\\n  n_expert={ne}:\")\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n            if len(row) > 0:\n                print(f\"    {m:20s}: |Bias|={row.iloc[0]['abs_bias']:.4f}  RMSE={row.iloc[0]['rmse']:.4f}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_budget_sweep_k4.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nBudget sensitivity sweep for Llama K=4 real confusion matrices.\n\nSweeps n_expert in {100, 200, 500, 1000, 2000} with 50 MC seeds each.\nUses MAP-EB instead of Gibbs for speed (250 total runs).\n\n|Bias| metric: |mean(estimate - truth) across seeds| averaged across cells.\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.optimize import minimize_scalar\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT_LIST = [100, 200, 500, 1000, 2000]\nN_MC = 50\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']\nSUBGROUP_WEIGHTS = np.array([0.386, 0.218, 0.258, 0.138])\n\nSUBGROUP_CM = {\n    'False_medium': {'fpr': 0.235, 'fnr': 0.319},\n    'False_short':  {'fpr': 0.310, 'fnr': 0.212},\n    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},\n    'True_short':   {'fpr': 0.091, 'fnr': 0.190},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\nTAU_Z0 = 0.35\nTAU_Z1 = 0.65\n\n\ndef get_cm_matrix(fpr, fnr):\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === MAP-EB ===\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_map_eb(counts, labels, hp_shape=3.0, hp_scale=1.0):\n    hp_rate = 1.0 / hp_scale\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = hp_shape * hp_scale\n            continue\n\n        def neg_log_post(a, _cl=cl, _shape=hp_shape, _rate=hp_rate):\n            nll = _dirmult_neg_ll(a, _cl)\n            if a < 1e-10:\n                return 1e10\n            log_prior = (_shape - 1.0) * np.log(a) - _rate * a\n            return nll - log_prior\n\n        res = minimize_scalar(neg_log_post, bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n_sz = counts[i, z, :].sum()\n            d = n_sz + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    return C, alpha_opt\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\n# === DGP ===\n\ndef generate_data(seed, n_expert):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(4):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb, _ = estimate_cm_hb_map_eb(counts, SUBGROUP_LABELS)\n\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'cate_est': th_nv, 'cate_true': oracle_cate,\n                'coverage': cov_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'cate_est': th_gc, 'cate_true': oracle_cate,\n                'coverage': cov_gc,\n            })\n\n            # Stratified MLE\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'cate_est': th_ml, 'cate_true': oracle_cate,\n                'coverage': cov_ml,\n            })\n\n            # HB EC-HTE (MAP-EB)\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'cate_est': th_hb, 'cate_true': oracle_cate,\n                'coverage': cov_hb,\n            })\n\n    return rows\n\n\n# === Corrected |Bias| aggregation ===\n\ndef compute_corrected_abs_bias(df):\n    \"\"\"\n    |Bias| = average across cells of |mean(estimate - truth) across seeds|.\n    For each (method, n_expert): average over (subgroup, z_level) cells of |mean bias|.\n    \"\"\"\n    cell_bias = (df.groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias']\n                 .mean().abs().reset_index(name='abs_mean_bias'))\n    return (cell_bias.groupby(['n_expert', 'method'])['abs_mean_bias']\n            .mean().reset_index(name='abs_bias'))\n\n\ndef compute_rmse(df):\n    \"\"\"RMSE = sqrt(mean(bias^2)) averaged across cells.\"\"\"\n    cell_rmse = (df.assign(bias_sq=df['bias'] ** 2)\n                 .groupby(['n_expert', 'method', 'subgroup', 'z_level'])['bias_sq']\n                 .mean().apply(np.sqrt).reset_index(name='rmse'))\n    return (cell_rmse.groupby(['n_expert', 'method'])['rmse']\n            .mean().reset_index(name='rmse'))\n\n\ndef compute_coverage(df):\n    return (df.groupby(['n_expert', 'method'])['coverage']\n            .mean().reset_index(name='coverage'))\n\n\n# === Analysis Report ===\n\ndef write_analysis(df_raw, outpath):\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse = compute_rmse(df_raw)\n    cov = compute_coverage(df_raw)\n\n    summary = abs_bias.merge(rmse, on=['n_expert', 'method']).merge(cov, on=['n_expert', 'method'])\n\n    lines = []\n    lines.append(\"# Budget Sensitivity Sweep: Llama K=4 Real CM\\n\")\n    lines.append(\"## Design\\n\")\n    lines.append(f\"- N={N}, P(Z=1)={P_Z1}, K=4 subgroups\")\n    lines.append(f\"- tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1 - TAU_Z0:.1f}\")\n    lines.append(f\"- n_expert sweep: {N_EXPERT_LIST}\")\n    lines.append(f\"- {N_MC} MC seeds per budget\")\n    lines.append(\"- HB method: MAP-EB (Gamma(3,1) prior)\")\n    lines.append(f\"- |Bias| = avg across cells of |mean(bias) across seeds|\")\n    lines.append(\"\")\n\n    lines.append(\"## Summary Table\\n\")\n    lines.append(\"| n_expert | |Bias|_naive | |Bias|_global | |Bias|_strat | |Bias|_echte | RMSE_naive | RMSE_global | RMSE_strat | RMSE_echte | Cov_echte | HB_wins_bias? | HB_wins_rmse? |\")\n    lines.append(\"|----------|-------------|--------------|-------------|-------------|------------|-------------|------------|------------|-----------|---------------|---------------|\")\n\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        vals = {}\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            row = sub[sub['method'] == m]\n            if len(row) > 0:\n                vals[m] = {\n                    'abs_bias': row.iloc[0]['abs_bias'],\n                    'rmse': row.iloc[0]['rmse'],\n                    'coverage': row.iloc[0]['coverage'],\n                }\n            else:\n                vals[m] = {'abs_bias': np.nan, 'rmse': np.nan, 'coverage': np.nan}\n\n        hb_wins_bias = \"YES\" if vals['hb_ec_hte']['abs_bias'] < vals['naive']['abs_bias'] else \"no\"\n        hb_wins_rmse = \"YES\" if vals['hb_ec_hte']['rmse'] < vals['naive']['rmse'] else \"no\"\n\n        lines.append(\n            f\"| {ne} \"\n            f\"| {vals['naive']['abs_bias']:.4f} \"\n            f\"| {vals['global_corrected']['abs_bias']:.4f} \"\n            f\"| {vals['stratified_mle']['abs_bias']:.4f} \"\n            f\"| {vals['hb_ec_hte']['abs_bias']:.4f} \"\n            f\"| {vals['naive']['rmse']:.4f} \"\n            f\"| {vals['global_corrected']['rmse']:.4f} \"\n            f\"| {vals['stratified_mle']['rmse']:.4f} \"\n            f\"| {vals['hb_ec_hte']['rmse']:.4f} \"\n            f\"| {vals['hb_ec_hte']['coverage']:.3f} \"\n            f\"| {hb_wins_bias} \"\n            f\"| {hb_wins_rmse} |\"\n        )\n    lines.append(\"\")\n\n    # Crossover analysis\n    lines.append(\"## Crossover Analysis\\n\")\n    crossover_bias = None\n    crossover_rmse = None\n    for ne in N_EXPERT_LIST:\n        sub = summary[summary['n_expert'] == ne]\n        hb = sub[sub['method'] == 'hb_ec_hte']\n        nv = sub[sub['method'] == 'naive']\n        if len(hb) > 0 and len(nv) > 0:\n            if hb.iloc[0]['abs_bias'] < nv.iloc[0]['abs_bias'] and crossover_bias is None:\n                crossover_bias = ne\n            if hb.iloc[0]['rmse'] < nv.iloc[0]['rmse'] and crossover_rmse is None:\n                crossover_rmse = ne\n\n    if crossover_bias is not None:\n        lines.append(f\"- **|Bias| crossover**: EC-HTE beats Naive at n_expert={crossover_bias}\")\n    else:\n        lines.append(\"- **|Bias| crossover**: EC-HTE never beats Naive in tested range\")\n    if crossover_rmse is not None:\n        lines.append(f\"- **RMSE crossover**: EC-HTE beats Naive at n_expert={crossover_rmse}\")\n    else:\n        lines.append(\"- **RMSE crossover**: EC-HTE never beats Naive in tested range\")\n    lines.append(\"\")\n\n    # Bias-variance decomposition per budget\n    lines.append(\"## Bias-Variance Decomposition (per budget)\\n\")\n    lines.append(\"| n_expert | Method | Bias^2 | Variance | MSE |\")\n    lines.append(\"|----------|--------|--------|----------|-----|\")\n    for ne in N_EXPERT_LIST:\n        for m in ['naive', 'hb_ec_hte']:\n            sub_df = df_raw[(df_raw['n_expert'] == ne) & (df_raw['method'] == m)]\n            cell_stats = (sub_df.groupby(['subgroup', 'z_level'])['bias']\n                          .agg(['mean', 'var', 'count']).reset_index())\n            mean_bias_sq = (cell_stats['mean'] ** 2).mean()\n            variance = cell_stats['var'].mean()\n            mse = mean_bias_sq + variance\n            lines.append(f\"| {ne} | {m} | {mean_bias_sq:.4f} | {variance:.4f} | {mse:.4f} |\")\n    lines.append(\"\")\n\n    report = \"\\n\".join(lines)\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"Budget Sensitivity Sweep: Llama K=4 Real CM\")\n    print(f\"N={N}, budgets={N_EXPERT_LIST}, seeds={N_MC}\")\n    print(f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}\")\n    print()\n\n    out_dir = 'artifacts/c1_multi_llm'\n\n    # Dry run: 1 budget, 1 seed\n    print(\"=== Dry run (n_expert=100, 1 seed) ===\")\n    data = generate_data(SEED_BASE, 100)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    df_dry['n_expert'] = 100\n    print(f\"Dry run OK: {len(df_dry)} rows, columns: {list(df_dry.columns)}\")\n    for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n    print()\n\n    # Full run\n    print(f\"=== Full run ({len(N_EXPERT_LIST)} budgets x {N_MC} seeds) ===\")\n    all_results = []\n    t0 = time.time()\n    total_runs = len(N_EXPERT_LIST) * N_MC\n    run_count = 0\n\n    for n_expert in N_EXPERT_LIST:\n        print(f\"\\n--- n_expert = {n_expert} ---\")\n        t_budget = time.time()\n        for mc in range(N_MC):\n            seed = SEED_BASE + mc\n            data = generate_data(seed, n_expert)\n            mc_rows = run_one_mc(data, seed)\n            for r in mc_rows:\n                r['n_expert'] = n_expert\n            all_results.extend(mc_rows)\n            run_count += 1\n            if (mc + 1) % 10 == 0:\n                elapsed = time.time() - t0\n                eta = elapsed / run_count * (total_runs - run_count)\n                print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n        budget_time = time.time() - t_budget\n        print(f\"  n_expert={n_expert} done in {budget_time:.1f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(all_results)\n\n    # Save results CSV\n    col_order = ['n_expert', 'seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage']\n    df_raw[col_order].to_csv(f'{out_dir}/budget_sweep_k4_results.csv', index=False)\n    print(f\"Saved budget_sweep_k4_results.csv ({len(df_raw)} rows)\")\n\n    # Write analysis\n    write_analysis(df_raw, f'{out_dir}/budget_sweep_k4_analysis.md')\n\n    # Print summary\n    print(\"\\n=== Summary ===\")\n    abs_bias = compute_corrected_abs_bias(df_raw)\n    rmse_df = compute_rmse(df_raw)\n    summary = abs_bias.merge(rmse_df, on=['n_expert', 'method'])\n    for ne in N_EXPERT_LIST:\n        print(f\"\\n  n_expert={ne}:\")\n        for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n            row = summary[(summary['n_expert'] == ne) & (summary['method'] == m)]\n            if len(row) > 0:\n                print(f\"    {m:20s}: |Bias|={row.iloc[0]['abs_bias']:.4f}  RMSE={row.iloc[0]['rmse']:.4f}\")\n"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T21:09:11.385576+00:00_

File created successfully at: /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_budget_sweep_k4.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T21:09:11.385723+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport sys\nsys.path.insert(0, '.')\nexec(open('artifacts/c1_multi_llm/run_budget_sweep_k4.py').read().split('# Full run')[0])\nprint('Dry run passed')\nprint(df_dry[['method','subgroup','z_level','bias','cate_est','cate_true','coverage']].head(16).to_string())\n\"\n",
  "description": "Dry-run budget sweep: 1 budget, 1 seed",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport sys\nsys.path.insert(0, '.')\nexec(open('artifacts/c1_multi_llm/run_budget_sweep_k4.py').read().split('# Full run')[0])\nprint('Dry run passed')\nprint(df_dry[['method','subgroup','z_level','bias','cate_est','cate_true','coverage']].head(16).to_string())\n\"\n",
    "description": "Dry-run budget sweep: 1 budget, 1 seed",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T21:09:11.385879+00:00_

Budget Sensitivity Sweep: Llama K=4 Real CM
N=5000, budgets=[100, 200, 500, 1000, 2000], seeds=50
tau(z=0)=0.35, tau(z=1)=0.65

=== Dry run (n_expert=100, 1 seed) ===
Dry run OK: 32 rows, columns: ['seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage', 'n_expert']
  naive               : mean |bias| = 0.0796
  global_corrected    : mean |bias| = 0.0962
  stratified_mle      : mean |bias| = 0.2730
  hb_ec_hte           : mean |bias| = 0.2810

Dry run passed
              method      subgroup  z_level      bias  cate_est  cate_true  coverage
0              naive  False_medium        0  0.127430  0.477430       0.35         0
1   global_corrected  False_medium        0 -0.028211  0.321789       0.35         1
2     stratified_mle  False_medium        0  0.274864  0.624864       0.35         1
3          hb_ec_hte  False_medium        0  0.271445  0.621445       0.35         1
4              naive  False_medium        1  0.006981  0.656981       0.65         1
5   global_corrected  False_medium        1  0.041153  0.691153       0.65         1
6     stratified_mle  False_medium        1 -0.100547  0.549453       0.65         1
7          hb_ec_hte  False_medium        1 -0.099122  0.550878       0.65         1
8              naive   False_short        0  0.085692  0.435692       0.35         1
9   global_corrected   False_short        0  0.070684  0.420684       0.35         1
10    stratified_mle   False_short        0 -0.104317  0.245683       0.35         1
11         hb_ec_hte   False_short        0 -0.128769  0.221231       0.35         1
12             naive   False_short        1 -0.154415  0.495585       0.65         0
13  global_corrected   False_short        1 -0.159599  0.490401       0.65         1
14    stratified_mle   False_short        1 -0.080812  0.569188       0.65         1
15         hb_ec_hte   False_short        1 -0.070332  0.579668       0.65         1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T21:09:11.386034+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 artifacts/c1_multi_llm/run_budget_sweep_k4.py",
  "description": "Full budget sweep: 5 budgets x 50 seeds",
  "timeout": "600000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 artifacts/c1_multi_llm/run_budget_sweep_k4.py",
    "description": "Full budget sweep: 5 budgets x 50 seeds",
    "timeout": "600000"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T21:09:11.386190+00:00_

Budget Sensitivity Sweep: Llama K=4 Real CM
N=5000, budgets=[100, 200, 500, 1000, 2000], seeds=50
tau(z=0)=0.35, tau(z=1)=0.65

=== Dry run (n_expert=100, 1 seed) ===
Dry run OK: 32 rows, columns: ['seed', 'method', 'subgroup', 'z_level', 'bias', 'cate_est', 'cate_true', 'coverage', 'n_expert']
  naive               : mean |bias| = 0.0796
  global_corrected    : mean |bias| = 0.0962
  stratified_mle      : mean |bias| = 0.2730
  hb_ec_hte           : mean |bias| = 0.2810

=== Full run (5 budgets x 50 seeds) ===

--- n_expert = 100 ---
  [10/50] 0s elapsed, ETA 3s
  [20/50] 0s elapsed, ETA 3s
  [30/50] 0s elapsed, ETA 3s
  [40/50] 0s elapsed, ETA 3s
  [50/50] 1s elapsed, ETA 2s
  n_expert=100 done in 0.6s

--- n_expert = 200 ---
  [10/50] 1s elapsed, ETA 2s
  [20/50] 1s elapsed, ETA 2s
  [30/50] 1s elapsed, ETA 2s
  [40/50] 1s elapsed, ETA 2s
  [50/50] 1s elapsed, ETA 2s
  n_expert=200 done in 0.6s

--- n_expert = 500 ---
  [10/50] 1s elapsed, ETA 2s
  [20/50] 1s elapsed, ETA 2s
  [30/50] 2s elapsed, ETA 1s
  [40/50] 2s elapsed, ETA 1s
  [50/50] 2s elapsed, ETA 1s
  n_expert=500 done in 0.6s

--- n_expert = 1000 ---
  [10/50] 2s elapsed, ETA 1s
  [20/50] 2s elapsed, ETA 1s
  [30/50] 2s elapsed, ETA 1s
  [40/50] 2s elapsed, ETA 1s
  [50/50] 2s elapsed, ETA 1s
  n_expert=1000 done in 0.6s

--- n_expert = 2000 ---
  [10/50] 3s elapsed, ETA 0s
  [20/50] 3s elapsed, ETA 0s
  [30/50] 3s elapsed, ETA 0s
  [40/50] 3s elapsed, ETA 0s
  [50/50] 3s elapsed, ETA 0s
  n_expert=2000 done in 0.6s

Total time: 3.1s
Saved budget_sweep_k4_results.csv (8000 rows)
Wrote artifacts/c1_multi_llm/budget_sweep_k4_analysis.md

=== Summary ===

  n_expert=100:
    naive               : |Bias|=0.0803  RMSE=0.1219
    global_corrected    : |Bias|=0.0214  RMSE=0.1895
    stratified_mle      : |Bias|=0.0520  RMSE=0.3937
    hb_ec_hte           : |Bias|=0.0578  RMSE=0.4020

  n_expert=200:
    naive               : |Bias|=0.0803  RMSE=0.1219
    global_corrected    : |Bias|=0.0208  RMSE=0.1747
    
…[truncated 790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T21:09:11.386349+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/budget_sweep_k4_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/budget_sweep_k4_analysis.md"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T21:09:11.386486+00:00_

1	# Budget Sensitivity Sweep: Llama K=4 Real CM
2	
3	## Design
4	
5	- N=5000, P(Z=1)=0.652, K=4 subgroups
6	- tau(z=0)=0.35, tau(z=1)=0.65, delta_tau=0.3
7	- n_expert sweep: [100, 200, 500, 1000, 2000]
8	- 50 MC seeds per budget
9	- HB method: MAP-EB (Gamma(3,1) prior)
10	- |Bias| = avg across cells of |mean(bias) across seeds|
11	
12	## Summary Table
13	
14	| n_expert | |Bias|_naive | |Bias|_global | |Bias|_strat | |Bias|_echte | RMSE_naive | RMSE_global | RMSE_strat | RMSE_echte | Cov_echte | HB_wins_bias? | HB_wins_rmse? |
15	|----------|-------------|--------------|-------------|-------------|------------|-------------|------------|------------|-----------|---------------|---------------|
16	| 100 | 0.0803 | 0.0214 | 0.0520 | 0.0578 | 0.1219 | 0.1895 | 0.3937 | 0.4020 | 0.710 | YES | no |
17	| 200 | 0.0803 | 0.0208 | 0.0251 | 0.0294 | 0.1219 | 0.1747 | 0.2603 | 0.2639 | 0.800 | YES | no |
18	| 500 | 0.0803 | 0.0167 | 0.0153 | 0.0165 | 0.1219 | 0.1544 | 0.1774 | 0.1783 | 0.892 | YES | no |
19	| 1000 | 0.0803 | 0.0168 | 0.0162 | 0.0166 | 0.1219 | 0.1524 | 0.1603 | 0.1608 | 0.915 | YES | no |
20	| 2000 | 0.0803 | 0.0167 | 0.0213 | 0.0212 | 0.1219 | 0.1491 | 0.1492 | 0.1494 | 0.940 | YES | no |
21	
22	## Crossover Analysis
23	
24	- **|Bias| crossover**: EC-HTE beats Naive at n_expert=100
25	- **RMSE crossover**: EC-HTE never beats Naive in tested range
26	
27	## Bias-Variance Decomposition (per budget)
28	
29	| n_expert | Method | Bias^2 | Variance | MSE |
30	|----------|--------|--------|----------|-----|
31	| 100 | naive | 0.0079 | 0.0081 | 0.0160 |
32	| 100 | hb_ec_hte | 0.0043 | 0.1755 | 0.1798 |
33	| 200 | naive | 0.0079 | 0.0081 | 0.0160 |
34	| 200 | hb_ec_hte | 0.0011 | 0.0746 | 0.0757 |
35	| 500 | naive | 0.0079 | 0.0081 | 0.0160 |
36	| 500 | hb_ec_hte | 0.0003 | 0.0342 | 0.0345 |
37	| 1000 | naive | 0.0079 | 0.0081 | 0.0160 |
38	| 1000 | hb_ec_hte | 0.0005 | 0.0278 | 0.0283 |
39	| 2000 | naive | 0.0079 | 0.0081 | 0.0160 |
40	| 2000 | hb_ec_hte | 0.0007 | 0.
…[truncated 19 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T21:09:11.386630+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -5 artifacts/c1_multi_llm/budget_sweep_k4_results.csv && echo \"...\" && wc -l artifacts/c1_multi_llm/budget_sweep_k4_results.csv",
  "description": "Verify CSV output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Bash",
  "tool_args": {
    "command": "head -5 artifacts/c1_multi_llm/budget_sweep_k4_results.csv && echo \"...\" && wc -l artifacts/c1_multi_llm/budget_sweep_k4_results.csv",
    "description": "Verify CSV output"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T21:09:11.386751+00:00_

n_expert,seed,method,subgroup,z_level,bias,cate_est,cate_true,coverage
100,0,naive,False_medium,0,0.1274304394672402,0.4774304394672402,0.35,0
100,0,global_corrected,False_medium,0,-0.028211203261220064,0.3217887967387799,0.35,1
100,0,stratified_mle,False_medium,0,0.2748635774922591,0.6248635774922591,0.35,1
100,0,hb_ec_hte,False_medium,0,0.27144451913448076,0.6214445191344807,0.35,1
...
8001 artifacts/c1_multi_llm/budget_sweep_k4_results.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-21T21:09:11.386934+00:00_

全部完成。关键发现：

**|Bias|**: EC-HTE 在所有 budget 下都优于 Naive（crossover 在最小的 n_expert=100 就已存在）。

**RMSE**: EC-HTE 在测试范围内始终不优于 Naive。根因清晰可见于 bias-variance 分解：
- Naive 的方差恒定在 0.008（不依赖 expert budget）
- EC-HTE 的方差从 n=100 的 0.176 降至 n=2000 的 0.024，但即使在 n=2000 仍略高于 Naive 的 0.016 MSE

**结论**: 在 Llama K=4 真实 CM 下（delta_pi ≈ 0.137，中等异质性），方差膨胀始终主导 bias reduction。RMSE crossover 需要 n_expert > 2000，或更大的 CM 异质性才能实现。

输出文件：
- `budget_sweep_k4_results.csv` — 8000 行原始结果
- `budget_sweep_k4_analysis.md` — 汇总表 + crossover 分析 + bias-variance 分解

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_llama-budget-sweep-k4_20260521T210604"
}
```

</details>

---
