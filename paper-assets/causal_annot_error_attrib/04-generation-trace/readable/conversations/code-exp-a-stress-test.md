# code exp a stress test

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/chats/worker_code_exp_a_stress_test_20260522T110940.jsonl`
- **Structured JSON:** [`f336c00b94d4b727e197.json`](../../sessions/f3/f336c00b94d4b727e197.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

45 recorded events

### Tool call

_source line 1 · 2026-05-22T11:24:24.985437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan006_asv_empirical.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/plan006_asv_empirical.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T11:24:24.985755+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib. Did you mean plan006_asv_empirical?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T11:24:24.985911+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_exposure_dag.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/mvp_exposure_dag.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T11:24:24.986252+00:00_

1	#!/usr/bin/env python3
2	"""
3	MVP Validation: Exposure Misclassification DAG — K=3 vs K=2
4	
5	Tests whether the binary "bias toward null" guarantee for non-differential
6	exposure misclassification breaks in the multiclass (K>=3) setting.
7	
8	== Technical Setting ==
9	A is the EXPOSURE/TREATMENT variable, measured with error via LLM annotation.
10	No confounders. Simplest possible misclassification scenario.
11	
12	  DAG: A -> Y, A -> A*
13	  DGP: Y = beta_0 + beta_1*1[A=1] + beta_2*1[A=2] + eps
14	  Misclassification: P(A*=j|A=i) = C[j,i], C column-stochastic
15	
16	Researcher regresses Y ~ 1 + 1[A*=1] + 1[A*=2] instead of Y ~ 1 + 1[A=1] + 1[A=2].
17	
18	== Binary Guarantee (K=2) ==
19	Non-differential misclassification of binary exposure guarantees bias toward
20	null: the estimated effect is attenuated (|gamma_hat| <= |beta|). This is
21	a classical result in measurement error literature.
22	
23	== Key Question ==
24	Does this guarantee extend to K=3? Or can certain confusion matrix structures
25	produce:
26	  - SIGN REVERSAL: sign(gamma_hat_k) != sign(beta_k)
27	  - AMPLIFICATION: |gamma_hat_k| > |beta_k|
28	
29	== Distinction from Lee & Wood-Doughty (2024) ==
30	We study OBSERVED exposure with noisy measurement (A observable, A* used at
31	scale). LWD study UNOBSERVED confounding with proxy (different identifiability).
32	
33	Dependencies: numpy
34	"""
35	
36	import numpy as np
37	from collections import OrderedDict
38	import time
39	
40	
41	# ============================================================
42	# DGP Parameters
43	# ============================================================
44	N_SAMPLES = 10_000
45	M_REPS = 1_000
46	N_RANDOM_SEARCH = 100_000
47	SEED = 42
48	
49	P_A = np.array([0.4, 0.35, 0.25])
50	BETA = np.array([0.0, 1.0, -0.5])    # beta_0, beta_1, beta_2
51	SIGMA_Y = 1.0
52	
53	
54	# ============================================================
55	# Confusion Matrix Structures (reused from confounding DAG MVP)
56	# ========================
…[truncated 19310 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T11:24:24.986461+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/plan006_asv_empirical*",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/plan006_asv_empirical*",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T11:24:24.986591+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T11:24:24.986725+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/plan006_asv_empirical/**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/plan006_asv_empirical/**/*.py",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T11:24:24.986839+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T11:24:24.986958+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/**/*asv*",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/**/*asv*",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T11:24:24.987074+00:00_

artifacts/plan004_asv_framework/report/plan_004_asv_v3_summary.txt
artifacts/plan_004_asv_v3_fixed/report/plan_004_asv_v3_fixed_results.txt
artifacts/plan_005_asv_extended_fixed.py
artifacts/_project/chart/fig3_asv_ranking.pdf
artifacts/_project/chart/fig3_asv_ranking_d3fbb2.pdf
artifacts/_project/chart/fig3_asv_ranking_8051a6.pdf
artifacts/plan006/asv_empirical_results.json
artifacts/plan006_mock/asv_empirical_results.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T11:24:24.987206+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/**/*empirical*",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/**/*empirical*",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T11:24:24.987339+00:00_

artifacts/_project/data/plan006_empirical_data.txt
artifacts/plan006/asv_empirical_results.json
artifacts/plan006_mock/asv_empirical_results.json
artifacts/_project/data/plan006_empirical_data_505323.txt
artifacts/plan006_empirical_data.txt
artifacts/compute_theory_empirical_mape.py
artifacts/ppi_empirical_validation_appendix.tex
artifacts/theory_empirical_mape.json
artifacts/theory_empirical_mape_table.tex
artifacts/ppi_empirical_validation_table.tex
artifacts/compute_ppi_empirical.py
artifacts/_project/data/ppi_empirical_validation.json
artifacts/ppi_empirical_validation.json
artifacts/_project/data/updated_empirical_results.json
artifacts/compute_updated_empirical.py
artifacts/updated_empirical_results.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T11:24:24.987485+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find plan006 DGP code",
  "prompt": "In the directory /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib, find the Python file(s) that contain the functions `make_dgp_params` and `compute_plim`. Also find `_BETA_POOL`. These are referenced as being in plan006_asv_empirical.py but the file may be at a different location. Search broadly across artifacts/ and the project root."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find plan006 DGP code",
    "prompt": "In the directory /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib, find the Python file(s) that contain the functions `make_dgp_params` and `compute_plim`. Also find `_BETA_POOL`. These are referenced as being in plan006_asv_empirical.py but the file may be at a different location. Search broadly across artifacts/ and the project root."
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-22T11:24:24.987614+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.py",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-22T11:24:24.987724+00:00_

artifacts/_project/data/mvp_confounding_dag.py
artifacts/mvp_confounding_dag.py
artifacts/_project/data/mvp_exposure_dag.py
artifacts/mvp_exposure_dag.py
artifacts/_project/report/mvp_exposure_dirichlet_subspace.py
artifacts/mvp_exposure_dirichlet_subspace.py
artifacts/preprocess.py
plan_001_collider_mbias_iv.py
plan_001_mediation_frontdoor.py
patch_metrics.py
plan_008_binarization_collapse.py
artifacts/plan008_binarization_collapse/report/plan_008_binarization_collapse.py
plan_005_asv_extended.py
artifacts/plan_005_asv_extended_fixed.py
plan_002_k57_extension.py
artifacts/plan_002_k57_extended_7topo.py
figures/paper/gen_fig4.py
artifacts/plan_009_pathological_matrices.py
figures/paper/gen_fig1.py
plan_009_pathological_matrices.py
plan_007_correction_guidance.py
figures/paper/gen_fig3.py
figures/paper/gen_fig2.py
plan_006_asv_empirical.py
annot_sensitivity/utils.py
annot_sensitivity/confusion.py
annot_sensitivity/dgp.py
annot_sensitivity/asv.py
annot_sensitivity/correction.py
annot_sensitivity/__init__.py
annot_sensitivity/examples/confounding_k3.py
annot_sensitivity/tests/__init__.py
annot_sensitivity/bias.py
annot_sensitivity/tests/test_core.py
artifacts/mvp_iv_dirichlet_subspace.py
artifacts/nondiff_stress_test.py
figures/paper/gen_diagnostic_plots.py
artifacts/compute_theory_empirical_mape.py
figures/paper/gen_fig7.py
plan_010_ppi_empirical_validation.py
artifacts/compute_all_tasks.py
artifacts/compute_ppi_empirical.py
artifacts/plan011_frontier_annotations/scripts/prepare_data.py
artifacts/plan011_frontier_annotations/scripts/annotate_frontier.py
artifacts/_project/intermediate/case_study_analysis.py
artifacts/plan012_case_study/case_study_analysis.py
artifacts/plan011_frontier_annotations/scripts/compute_results.py
artifacts/compute_delta_max.py
artifacts/annotate.py
artifacts/compute_updated_empirical.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-22T11:24:24.987852+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "def make_dgp_params",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "type": "py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Grep",
  "tool_args": {
    "pattern": "def make_dgp_params",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
    "type": "py"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-22T11:24:24.987958+00:00_

Found 2 files
artifacts/compute_ppi_empirical.py
plan_006_asv_empirical.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T11:24:24.988067+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "def compute_plim",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "type": "py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Grep",
  "tool_args": {
    "pattern": "def compute_plim",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
    "type": "py"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T11:24:24.988183+00:00_

Found 1 file
plan_006_asv_empirical.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-22T11:24:24.988300+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "_BETA_POOL",
  "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
  "type": "py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Grep",
  "tool_args": {
    "pattern": "_BETA_POOL",
    "path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib",
    "type": "py"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-22T11:24:24.988402+00:00_

Found 7 files
artifacts/compute_ppi_empirical.py
plan_010_ppi_empirical_validation.py
plan_006_asv_empirical.py
plan_009_pathological_matrices.py
artifacts/plan_009_pathological_matrices.py
artifacts/plan_002_k57_extended_7topo.py
plan_002_k57_extension.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-22T11:24:24.988513+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T11:24:24.988623+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_ppi_empirical.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_ppi_empirical.py"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T11:24:24.988808+00:00_

1	#!/usr/bin/env python3
2	"""
3	Empirical Correction Validation — HumAID K=10
4	
5	Loads 8 valid HumAID confusion matrices from asv_empirical_results.json,
6	generates synthetic MC data using plan_006's K=10 DGP for each of 7 topologies,
7	runs all 5 correction methods (PPI++, naive plug-in, DSL, MC-SIMEX, MLA),
8	and reports empirical bias reduction per topology × method.
9	
10	Input:  artifacts/plan006/asv_empirical_results.json
11	Output: artifacts/ppi_empirical_validation.json
12	
13	Dependencies: numpy, annot_sensitivity (local package)
14	"""
15	
16	import sys
17	import os
18	import json
19	import time
20	import numpy as np
21	
22	PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
23	sys.path.insert(0, PROJECT_ROOT)
24	
25	from annot_sensitivity.correction import (
26	    correct_ppi, correct_naive_plugin, correct_dsl, correct_mcsimex, correct_mla
27	)
28	from annot_sensitivity.utils import misclassify, make_dummies, ols, ols_with_se
29	
30	# ── Plan 006 DGP Infrastructure (K-general) ────────────────────────
31	
32	_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]
33	_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
34	_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
35	_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
36	_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]
37	_DT_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
38	_DY_POOL = [0.0, 0.8, 0.6, -0.5, 0.4, -0.3, 0.2, 0.15, -0.1, 0.05]
39	
40	
41	def softmax_rows(logits):
42	    e = np.exp(logits - logits.max(axis=1, keepdims=True))
43	    return e / e.sum(axis=1, keepdims=True)
44	
45	
46	def sample_cat(probs, rng):
47	    cum = np.cumsum(probs, axis=1)
48	    u = rng.uniform(size=probs.shape[0])[:, None]
49	    return (u >= cum[:, :-1]).sum(axis=1).astype(int)
50	
51	
52	def make_p_A(K):
53	    if K == 2:
54	        return np.array([0.55, 0.45])
55	    elif K == 3:
56	  
…[truncated 21905 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-22T11:24:24.989158+00:00_

1	#!/usr/bin/env python3
2	"""
3	plan_006: Empirical ASV Calibration with LLM Annotation Confusion Matrices
4	
5	Uses empirical confusion matrices from LLM annotations (3 LLMs × 3 datasets × 3 prompts
6	= 27 C matrices) to compute:
7	  1. Downstream causal bias across 7 DAG topologies
8	  2. ASV sensitivity metrics (magnitude, significance, sign-flip)
9	  3. F1 vs bias disconnect analysis (Baumann 2025 verification)
10	  4. Type I/II error rates before/after ASV filtering
11	  5. Inter-model error correlation
12	
13	Input:  data/{dataset}/{model}_{prompt}_annotations.jsonl
14	        Each line: {"true_label": int, "predicted_label": int}
15	
16	Output: artifacts/plan006/asv_empirical_results.json
17	
18	Dependencies: numpy (required), matplotlib (optional for plots)
19	"""
20	
21	import numpy as np
22	import json
23	import argparse
24	import os
25	import time
26	from collections import OrderedDict
27	
28	try:
29	    import matplotlib
30	    matplotlib.use('Agg')
31	    import matplotlib.pyplot as plt
32	    HAS_MPL = True
33	except ImportError:
34	    HAS_MPL = False
35	
36	# ============================================================================
37	# Constants
38	# ============================================================================
39	
40	DATASETS = OrderedDict([
41	    ('civil_comments', {'K': 2}),
42	    ('vast', {'K': 3}),
43	    ('humaid', {'K': 10}),
44	])
45	
46	MODELS = ['llama4', 'qwen3', 'deepseek']
47	PROMPTS = ['zero-shot', 'few-shot-3', 'few-shot-5']
48	
49	TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
50	              'mbias', 'iv', 'frontdoor']
51	
52	N_PRECOMP = 2_000_000
53	
54	# Parameter pools — K=3 values match plan_001/plan_005
55	_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]
56	_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
57	_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
58	_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
59	_DELT
…[truncated 42691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T11:24:24.989376+00:00_

Perfect! I've found all three items. Here's a summary of my findings:

## Summary

All three items you're looking for are located in **two main files**:

### 1. **Primary Location: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py`**

- **`make_dgp_params(K)`** - Function defined at **line 154**
  - Generates DGP (Data Generating Process) parameters for different causal topologies
  - Returns a dictionary of parameters keyed by topology name
  
- **`compute_plim(C, st, K)`** - Function defined at **line 369**
  - Computes the probability limit under confusion matrix C
  - Takes confusion matrix C, sufficient statistics st, and number of classes K
  
- **`_BETA_POOL`** - Variable defined at **line 57**
  - List of 10 parameter values: `[0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]`
  - Used to construct parameters for mediation and exposure topologies

### 2. **Secondary Location: `/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/compute_ppi_empirical.py`**

This file contains **duplicate implementations** of the same components:
- **`make_dgp_params(K)`** - Defined at **line 62** (identical to plan_006_asv_empirical.py)
- **`_BETA_POOL`** - Defined at **line 34** (same values)
- **`compute_plim` is NOT in this file** (only the first two items are duplicated here)

The functions in `compute_ppi_empirical.py` appear to be copied from `plan_006_asv_empirical.py` to support empirical validation work, but the original canonical implementations are in `plan_006_asv_empirical.py`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Agent",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T11:24:24.989518+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T11:24:24.989900+00:00_

1	#!/usr/bin/env python3
2	"""
3	plan_006: Empirical ASV Calibration with LLM Annotation Confusion Matrices
4	
5	Uses empirical confusion matrices from LLM annotations (3 LLMs × 3 datasets × 3 prompts
6	= 27 C matrices) to compute:
7	  1. Downstream causal bias across 7 DAG topologies
8	  2. ASV sensitivity metrics (magnitude, significance, sign-flip)
9	  3. F1 vs bias disconnect analysis (Baumann 2025 verification)
10	  4. Type I/II error rates before/after ASV filtering
11	  5. Inter-model error correlation
12	
13	Input:  data/{dataset}/{model}_{prompt}_annotations.jsonl
14	        Each line: {"true_label": int, "predicted_label": int}
15	
16	Output: artifacts/plan006/asv_empirical_results.json
17	
18	Dependencies: numpy (required), matplotlib (optional for plots)
19	"""
20	
21	import numpy as np
22	import json
23	import argparse
24	import os
25	import time
26	from collections import OrderedDict
27	
28	try:
29	    import matplotlib
30	    matplotlib.use('Agg')
31	    import matplotlib.pyplot as plt
32	    HAS_MPL = True
33	except ImportError:
34	    HAS_MPL = False
35	
36	# ============================================================================
37	# Constants
38	# ============================================================================
39	
40	DATASETS = OrderedDict([
41	    ('civil_comments', {'K': 2}),
42	    ('vast', {'K': 3}),
43	    ('humaid', {'K': 10}),
44	])
45	
46	MODELS = ['llama4', 'qwen3', 'deepseek']
47	PROMPTS = ['zero-shot', 'few-shot-3', 'few-shot-5']
48	
49	TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
50	              'mbias', 'iv', 'frontdoor']
51	
52	N_PRECOMP = 2_000_000
53	
54	# Parameter pools — K=3 values match plan_001/plan_005
55	_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]
56	_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
57	_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]
58	_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]
59	_DELT
…[truncated 42691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T11:24:24.990546+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nExp-A: Non-differential Misclassification Stress Test Expansion\n\nTests sign flip rate and bias ratio under increasing differential\nmisclassification departure ε.\n\n4 topologies × 2 K × 3 CM qualities × 4 ε = 96 configs\nN=10,000 × 100 MC reps per config\n\"\"\"\nimport numpy as np\nimport json\nimport time\nimport os\n\nTOPOLOGIES = ['confounding', 'mediation', 'exposure', 'iv']\nK_VALUES = [3, 10]\nEPSILONS = [0.0, 0.01, 0.05, 0.10]\nCM_QUALS = {'high': 0.8, 'medium': 0.6, 'low': 0.4}\nN_SAMPLES = 10_000\nN_REPS = 100\nN_LARGE = 2_000_000\nSEED = 42\n\n_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]\n_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]\n_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]\n_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]\n_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]\n\n\ndef softmax_rows(x):\n    e = np.exp(x - x.max(axis=1, keepdims=True))\n    return e / e.sum(axis=1, keepdims=True)\n\n\ndef sample_cat(probs, rng):\n    cum = np.cumsum(probs, axis=1)\n    u = rng.uniform(size=probs.shape[0])[:, None]\n    return (u >= cum[:, :-1]).sum(axis=1).astype(int)\n\n\ndef make_p_A(K):\n    if K == 3:\n        return np.array([0.40, 0.35, 0.25])\n    raw = np.array([1.0 / (i + 1) for i in range(K)])\n    return raw / raw.sum()\n\n\ndef make_dgp_params(K):\n    p_A = make_p_A(K)\n    params = {\n        'confounding': {\n            'p_A': p_A, 'alpha': np.array(_ALPHA_POOL[:K-1]),\n            'beta_A': np.array(_BETA_A_POOL[:K-1]),\n            'beta_T': 2.0, 'sigma_T': 1.0,\n        },\n        'mediation': {\n            'tau': 0.5, 'gamma': np.array(_GAMMA_POOL[:K]),\n            'delta': np.array(_DELTA_POOL[:K]),\n            'beta': np.array(_BETA_POOL[:K]),\n        },\n        'exposure': {'beta': np.array(_BETA_POOL[:K]), 'p_A': p_A},\n    }\n    if K == 3:\n        params['iv'] = {\n            'lam': 1.0, 'beta': np.array([0.0, 0.5, -0.25]),\n            'g': np.zeros(3), 'dZ': np.array([0.0, 1.0, -0.5]),\n            'dU': np.array([0.0, 0.8, 0.6]),\n        }\n    else:\n        iv_b = np.array(_BETA_POOL[:K]) * 0.5\n        iv_b[0] = 0.0\n        params['iv'] = {\n            'lam': 1.0, 'beta': iv_b, 'g': np.zeros(K),\n            'dZ': np.array([0.0] + [_ALPHA_POOL[i]*0.7 for i in range(K-1)]),\n            'dU': np.array([0.0] + [_BETA_A_POOL[i]*0.6 for i in range(K-1)]),\n        }\n    return params\n\n\n# ── DGP generators ──────────────────────────────────────────\n\ndef gen_confounding(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K-1))\n    for j in range(K-1):\n        D[:, j] = (A == j+1).astype(float)\n    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)\n    Y = p['beta_T']*T + D @ p['beta_A'] + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_mediation(K, N, p, rng):\n    T = rng.binomial(1, 0.5, N).astype(float)\n    logits = p['gamma'][None, :] + p['delta'][None, :]*T[:, None]\n    A = sample_cat(softmax_rows(logits), rng)\n    D = np.zeros((N, K-1))\n    for j in range(K-1):\n        D[:, j] = (A == j+1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau']*T + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_exposure(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K-1))\n    for j in range(K-1):\n        D[:, j] = (A == j+1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)\n    return None, Y, A\n\n\ndef gen_iv(K, N, p, rng):\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['dZ'][None, :]*Z[:, None]\n              + p['dU'][None, :]*U[:, None])\n    A = sample_cat(softmax_rows(logits), rng)\n    D = np.zeros((N, K-1))\n    for j in range(K-1):\n        D[:, j] = (A == j+1).astype(float)\n    Y = D @ p['beta'][1:] + p['lam']*U + rng.normal(0, 1, N)\n    return Z, Y, A\n\n\nGEN = {'confounding': gen_confounding, 'mediation': gen_mediation,\n       'exposure': gen_exposure, 'iv': gen_iv}\n\n\n# ── Estimators ──────────────────────────────────────────────\n\ndef est_tau(topo, fv, Y, Ak, K):\n    N = len(Y)\n    D = np.zeros((N, K-1))\n    for k in range(1, K):\n        D[:, k-1] = (Ak == k).astype(float)\n    if topo == 'iv':\n        z1, z0 = fv == 1, fv == 0\n        if z1.sum() < 2 or z0.sum() < 2:\n            return np.nan\n        RF = Y[z1].mean() - Y[z0].mean()\n        FS = D[z1, 0].mean() - D[z0, 0].mean()\n        return RF / FS if abs(FS) > 1e-8 else np.nan\n    elif topo == 'exposure':\n        X = np.column_stack([np.ones(N), D])\n    else:\n        X = np.column_stack([np.ones(N), fv, D])\n    try:\n        return np.linalg.lstsq(X, Y, rcond=None)[0][1]\n    except np.linalg.LinAlgError:\n        return np.nan\n\n\n# ── Confusion matrix construction & perturbation ────────────\n\ndef make_cm(K, diag):\n    C = np.full((K, K), (1.0 - diag) / (K - 1))\n    np.fill_diagonal(C, diag)\n    return C\n\n\ndef perturb(C, eps):\n    K = C.shape[0]\n    Cp = C.copy()\n    Cp[~np.eye(K, dtype=bool)] += eps\n    for j in range(K):\n        Cp[:, j] /= Cp[:, j].sum()\n    return Cp\n\n\ndef gen_Astar(A, Y, Cb, eps, rng):\n    if eps <= 0:\n        probs = Cb[:, A]\n    else:\n        Cp = perturb(Cb, eps)\n        high = Y > np.median(Y)\n        probs = np.where(high[None, :], Cp[:, A], Cb[:, A])\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    return (u[None, :] >= cum[:-1]).sum(axis=0).astype(int)\n\n\n# ── Main ────────────────────────────────────────────────────\n\ndef main():\n    t0 = time.time()\n    out_dir = os.path.dirname(os.path.abspath(__file__))\n    n_total = len(TOPOLOGIES) * len(K_VALUES) * len(EPSILONS) * len(CM_QUALS)\n    print(f\"Exp-A: {n_total} configs x {N_REPS} MC reps, N={N_SAMPLES}\")\n\n    # Validate CMs\n    for K in K_VALUES:\n        for dv in CM_QUALS.values():\n            C = make_cm(K, dv)\n            assert np.allclose(C.sum(axis=0), 1.0), f\"K={K} diag={dv}: bad CM\"\n            for eps in EPSILONS:\n                if eps > 0:\n                    Cp = perturb(C, eps)\n                    assert np.allclose(Cp.sum(axis=0), 1.0)\n                    assert (Cp >= -1e-12).all()\n\n    all_params = {K: make_dgp_params(K) for K in K_VALUES}\n\n    # True parameters (oracle with N=2M)\n    tau_trues = {}\n    print(\"\\nTrue parameters (N=2M oracle):\")\n    for K in K_VALUES:\n        for topo in TOPOLOGIES:\n            rng = np.random.default_rng(K*1000 + abs(hash(topo)) % 1000)\n            fv, Y, A = GEN[topo](K, N_LARGE, all_params[K][topo], rng)\n            tau_trues[(K, topo)] = est_tau(topo, fv, Y, A, K)\n            print(f\"  K={K:>2} {topo:<13} tau_true={tau_trues[(K,topo)]:>10.6f}\")\n\n    # MC simulation\n    results = []\n    idx = 0\n    print(f\"\\nMC simulation ({n_total} configs):\")\n    for topo in TOPOLOGIES:\n        for K in K_VALUES:\n            p = all_params[K][topo]\n            tt = tau_trues[(K, topo)]\n            for qn, dv in CM_QUALS.items():\n                Cb = make_cm(K, dv)\n                for eps in EPSILONS:\n                    idx += 1\n                    rng = np.random.default_rng(SEED + idx*1000)\n                    hats = np.empty(N_REPS)\n                    for m in range(N_REPS):\n                        fv, Y, A = GEN[topo](K, N_SAMPLES, p, rng)\n                        As = gen_Astar(A, Y, Cb, eps, rng)\n                        hats[m] = est_tau(topo, fv, Y, As, K)\n\n                    ok = np.isfinite(hats)\n                    nv = int(ok.sum())\n                    if nv > 0 and abs(tt) > 1e-12:\n                        vh = hats[ok]\n                        sfr = float((np.sign(vh) != np.sign(tt)).mean())\n                        ratios = np.abs(vh / tt)\n                        br = float(ratios.mean())\n                        br_std = float(ratios.std())\n                        br_med = float(np.median(ratios))\n                        mt = float(vh.mean())\n                    else:\n                        sfr = br = br_std = br_med = mt = None\n\n                    results.append({\n                        'topology': topo, 'K': K, 'epsilon': eps,\n                        'cm_quality': qn, 'cm_diag': dv,\n                        'sign_flip_rate': sfr,\n                        'mean_bias_ratio': br,\n                        'std_bias_ratio': br_std,\n                        'median_bias_ratio': br_med,\n                        'tau_true': float(tt),\n                        'mean_tau_hat': mt,\n                        'n_reps': nv,\n                    })\n\n                    if idx % 12 == 0 or idx == n_total:\n                        el = time.time() - t0\n                        eta = el / idx * (n_total - idx)\n                        s = f\"SF={sfr:.3f} BR={br:.3f}\" if sfr is not None else \"N/A\"\n                        print(f\"  [{idx:>3}/{n_total}] {topo:<13} K={K:>2} \"\n                              f\"eps={eps:.2f} {qn:<6} {s}  \"\n                              f\"({el:.0f}s, ETA {eta:.0f}s)\")\n\n    # Summaries\n    def sm(vals):\n        v = [x for x in vals if x is not None]\n        return float(np.mean(v)) if v else None\n\n    by_eps = {}\n    for eps in EPSILONS:\n        sub = [r for r in results if r['epsilon'] == eps]\n        sfs = [r['sign_flip_rate'] for r in sub if r['sign_flip_rate'] is not None]\n        brs = [r['mean_bias_ratio'] for r in sub if r['mean_bias_ratio'] is not None]\n        by_eps[str(eps)] = {\n            'mean_sign_flip_rate': float(np.mean(sfs)) if sfs else None,\n            'mean_bias_ratio': float(np.mean(brs)) if brs else None,\n            'max_sign_flip_rate': float(max(sfs)) if sfs else None,\n        }\n\n    by_topo = {}\n    for topo in TOPOLOGIES:\n        sub = [r for r in results if r['topology'] == topo]\n        sfs = [r['sign_flip_rate'] for r in sub if r['sign_flip_rate'] is not None]\n        brs = [r['mean_bias_ratio'] for r in sub if r['mean_bias_ratio'] is not None]\n        by_topo[topo] = {\n            'mean_sign_flip_rate': float(np.mean(sfs)) if sfs else None,\n            'mean_bias_ratio': float(np.mean(brs)) if brs else None,\n        }\n\n    by_K = {}\n    for K in K_VALUES:\n        sub = [r for r in results if r['K'] == K]\n        sfs = [r['sign_flip_rate'] for r in sub if r['sign_flip_rate'] is not None]\n        brs = [r['mean_bias_ratio'] for r in sub if r['mean_bias_ratio'] is not None]\n        by_K[str(K)] = {\n            'mean_sign_flip_rate': float(np.mean(sfs)) if sfs else None,\n            'mean_bias_ratio': float(np.mean(brs)) if brs else None,\n        }\n\n    output = {\n        'results': results,\n        'summary': {'by_epsilon': by_eps, 'by_topology': by_topo, 'by_K': by_K},\n    }\n\n    def clean(o):\n        if isinstance(o, (float, np.floating)):\n            v = float(o)\n            return None if (np.isnan(v) or np.isinf(v)) else v\n        if isinstance(o, np.integer):\n            return int(o)\n        if isinstance(o, dict):\n            return {k: clean(v) for k, v in o.items()}\n        if isinstance(o, list):\n            return [clean(v) for v in o]\n        return o\n\n    output = clean(output)\n    jpath = os.path.join(out_dir, 'exp_a_stress_test_results.json')\n    with open(jpath, 'w') as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nJSON -> {jpath}\")\n\n    tpath = os.path.join(out_dir, 'exp_a_stress_test_table.tex')\n    write_tex(results, tpath)\n    print(f\"TeX  -> {tpath}\")\n\n    total = time.time() - t0\n    print(f\"\\nDone in {total:.0f}s ({total/60:.1f}min)\")\n    print(\"\\nBy epsilon:\")\n    for eps, s in by_eps.items():\n        sf = s['mean_sign_flip_rate']\n        br = s['mean_bias_ratio']\n        mx = s['max_sign_flip_rate']\n        print(f\"  eps={eps}: meanSF={sf:.4f} meanBR={br:.4f} maxSF={mx:.4f}\")\n    print(\"\\nBy topology:\")\n    for topo, s in by_topo.items():\n        print(f\"  {topo:<13}: SF={s['mean_sign_flip_rate']:.4f} \"\n              f\"BR={s['mean_bias_ratio']:.4f}\")\n    print(\"\\nBy K:\")\n    for k, s in by_K.items():\n        print(f\"  K={k}: SF={s['mean_sign_flip_rate']:.4f} \"\n              f\"BR={s['mean_bias_ratio']:.4f}\")\n\n\ndef write_tex(results, path):\n    ncols = 3 + 2 * len(EPSILONS)\n    lines = [\n        r'\\begin{table*}[t]',\n        r'\\centering',\n        r'\\caption{Non-differential misclassification stress test: sign flip rate (SF) '\n        r'and mean bias ratio (BR\\,$=\\overline{|\\hat\\tau/\\tau|}$) under increasing '\n        r'differential departure $\\varepsilon$.}',\n        r'\\label{tab:stress-test}',\n        r'\\small\\setlength{\\tabcolsep}{3.5pt}',\n        r'\\begin{tabular}{llc' + 'rr' * len(EPSILONS) + '}',\n        r'\\toprule',\n    ]\n\n    h1 = r'Topology & $K$ & Q'\n    for e in EPSILONS:\n        h1 += rf' & \\multicolumn{{2}}{{c}}{{$\\varepsilon\\!=\\!{e}$}}'\n    lines.append(h1 + r' \\\\')\n\n    clines = ' '.join(\n        rf'\\cmidrule(lr){{{4+2*i}-{5+2*i}}}' for i in range(len(EPSILONS)))\n    lines.append(clines)\n\n    h2 = r' & &'\n    for _ in EPSILONS:\n        h2 += r' & {\\scriptsize SF} & {\\scriptsize BR}'\n    lines.append(h2 + r' \\\\')\n    lines.append(r'\\midrule')\n\n    for ti, topo in enumerate(TOPOLOGIES):\n        if ti > 0:\n            lines.append(r'\\midrule')\n        first_t = True\n        for ki, K in enumerate(K_VALUES):\n            if ki > 0:\n                lines.append(rf'\\cmidrule{{2-{ncols}}}')\n            first_k = True\n            for qn in CM_QUALS:\n                tl = topo.capitalize() if first_t else ''\n                kl = str(K) if first_k else ''\n                row = f'{tl} & {kl} & {qn[0].upper()}'\n                for eps in EPSILONS:\n                    r = next(x for x in results\n                             if x['topology'] == topo and x['K'] == K\n                             and x['epsilon'] == eps and x['cm_quality'] == qn)\n                    sf = r['sign_flip_rate']\n                    br = r['mean_bias_ratio']\n                    sfs = f'{sf:.2f}' if sf is not None else '--'\n                    brs = f'{br:.2f}' if br is not None else '--'\n                    row += f' & {sfs} & {brs}'\n                lines.append(row + r' \\\\')\n                first_t = False\n                first_k = False\n\n    lines += [\n        r'\\bottomrule',\n        r'\\end{tabular}',\n        r'\\vspace{1mm}',\n        r'\\parbox{\\textwidth}{\\footnotesize '\n        r'SF\\,=\\,sign flip rate; BR\\,=\\,mean $|\\hat\\tau/\\tau|$ '\n        r'(1.00 = unbiased). '\n        r'$\\varepsilon\\!=\\!0$: non-differential; $\\varepsilon\\!>\\!0$: '\n        r'outcome-dependent misclassification. '\n        r'Q: H/M/L\\,=\\,CM diagonal 0.8/0.6/0.4 with uniform off-diagonal. '\n        r'Each cell: $N\\!=\\!10{,}000\\!\\times\\!100$ MC replications.}',\n        r'\\end{table*}',\n    ]\n    with open(path, 'w') as f:\n        f.write('\\n'.join(lines) + '\\n')\n\n\nif __name__ == '__main__':\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nExp-A: Non-differential Misclassification Stress Test Expansion\n\nTests sign flip rate and bias ratio under increasing differential\nmisclassification departure ε.\n\n4 topologies × 2 K × 3 CM qualities × 4 ε = 96 configs\nN=10,000 × 100 MC reps per config\n\"\"\"\nimport numpy as np\nimport json\nimport time\nimport os\n\nTOPOLOGIES = ['confounding', 'mediation', 'exposure', 'iv']\nK_VALUES = [3, 10]\nEPSILONS = [0.0, 0.01, 0.05, 0.10]\nCM_QUALS = {'high': 0.8, 'medium': 0.6, 'low': 0.4}\nN_SAMPLES = 10_000\nN_REPS = 100\nN_LARGE = 2_000_000\nSEED = 42\n\n_ALPHA_POOL = [1.5, -1.0, 0.8, -0.5, 1.2, -0.7, 0.9, -0.4, 0.6]\n_BETA_A_POOL = [1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]\n_BETA_POOL = [0.0, 1.0, -0.5, 0.7, -0.3, 0.5, -0.2, 0.4, -0.15, 0.3]\n_GAMMA_POOL = [0.0, 0.5, -0.3, 0.4, -0.2, 0.3, -0.1, 0.2, -0.05, 0.1]\n_DELTA_POOL = [0.0, 0.8, -0.6, 0.5, -0.4, 0.3, -0.2, 0.15, -0.1, 0.05]\n\n\ndef softmax_rows(x):\n    e = np.exp(x - x.max(axis=1, keepdims=True))\n    return e / e.sum(axis=1, keepdims=True)\n\n\ndef sample_cat(probs, rng):\n    cum = np.cumsum(probs, axis=1)\n    u = rng.uniform(size=probs.shape[0])[:, None]\n    return (u >= cum[:, :-1]).sum(axis=1).astype(int)\n\n\ndef make_p_A(K):\n    if K == 3:\n        return np.array([0.40, 0.35, 0.25])\n    raw = np.array([1.0 / (i + 1) for i in range(K)])\n    return raw / raw.sum()\n\n\ndef make_dgp_params(K):\n    p_A = make_p_A(K)\n    params = {\n        'confounding': {\n            'p_A': p_A, 'alpha': np.array(_ALPHA_POOL[:K-1]),\n            'beta_A': np.array(_BETA_A_POOL[:K-1]),\n            'beta_T': 2.0, 'sigma_T': 1.0,\n        },\n        'mediation': {\n            'tau': 0.5, 'gamma': np.array(_GAMMA_POOL[:K]),\n            'delta': np.array(_DELTA_POOL[:K]),\n            'beta': np.array(_BETA_POOL[:K]),\n        },\n        'exposure': {'beta': np.array(_BETA_POOL[:K]), 'p_A': p_A},\n    }\n    if K == 3:\n        params['iv'] = {\n            'lam': 1.0, 'beta': np.array([0.0, 0.5, -0.25]),\n            'g': np.zeros(3), 'dZ': np.array([0.0, 1.0, -0.5]),\n            'dU': np.array([0.0, 0.8, 0.6]),\n        }\n    else:\n        iv_b = np.array(_BETA_POOL[:K]) * 0.5\n        iv_b[0] = 0.0\n        params['iv'] = {\n            'lam': 1.0, 'beta': iv_b, 'g': np.zeros(K),\n            'dZ': np.array([0.0] + [_ALPHA_POOL[i]*0.7 for i in range(K-1)]),\n            'dU': np.array([0.0] + [_BETA_A_POOL[i]*0.6 for i in range(K-1)]),\n        }\n    return params\n\n\n# ── DGP generators ──────────────────────────────────────────\n\ndef gen_confounding(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K-1))\n    for j in range(K-1):\n        D[:, j] = (A == j+1).astype(float)\n    T = D @ p['alpha'] + rng.normal(0, p['sigma_T'], N)\n    Y = p['beta_T']*T + D @ p['beta_A'] + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_mediation(K, N, p, rng):\n    T = rng.binomial(1, 0.5, N).astype(float)\n    logits = p['gamma'][None, :] + p['delta'][None, :]*T[:, None]\n    A = sample_cat(softmax_rows(logits), rng)\n    D = np.zeros((N, K-1))\n    for j in range(K-1):\n        D[:, j] = (A == j+1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + p['tau']*T + rng.normal(0, 1, N)\n    return T, Y, A\n\n\ndef gen_exposure(K, N, p, rng):\n    A = rng.choice(K, size=N, p=p['p_A'])\n    D = np.zeros((N, K-1))\n    for j in range(K-1):\n        D[:, j] = (A == j+1).astype(float)\n    Y = p['beta'][0] + D @ p['beta'][1:] + rng.normal(0, 1, N)\n    return None, Y, A\n\n\ndef gen_iv(K, N, p, rng):\n    Z = rng.binomial(1, 0.5, N).astype(float)\n    U = rng.normal(0, 1, N)\n    logits = (p['g'][None, :] + p['dZ'][None, :]*Z[:, None]\n              + p['dU'][None, :]*U[:, None])\n    A = sample_cat(softmax_rows(logits), rng)\n    D = np.zeros((N, K-1))\n    for j in range(K-1):\n        D[:, j] = (A == j+1).astype(float)\n    Y = D @ p['beta'][1:] + p['lam']*U + rng.normal(0, 1, N)\n    return Z, Y, A\n\n\nGEN = {'confounding': gen_confounding, 'mediation': gen_mediation,\n       'exposure': gen_exposure, 'iv': gen_iv}\n\n\n# ── Estimators ──────────────────────────────────────────────\n\ndef est_tau(topo, fv, Y, Ak, K):\n    N = len(Y)\n    D = np.zeros((N, K-1))\n    for k in range(1, K):\n        D[:, k-1] = (Ak == k).astype(float)\n    if topo == 'iv':\n        z1, z0 = fv == 1, fv == 0\n        if z1.sum() < 2 or z0.sum() < 2:\n            return np.nan\n        RF = Y[z1].mean() - Y[z0].mean()\n        FS = D[z1, 0].mean() - D[z0, 0].mean()\n        return RF / FS if abs(FS) > 1e-8 else np.nan\n    elif topo == 'exposure':\n        X = np.column_stack([np.ones(N), D])\n    else:\n        X = np.column_stack([np.ones(N), fv, D])\n    try:\n        return np.linalg.lstsq(X, Y, rcond=None)[0][1]\n    except np.linalg.LinAlgError:\n        return np.nan\n\n\n# ── Confusion matrix construction & perturbation ────────────\n\ndef make_cm(K, diag):\n    C = np.full((K, K), (1.0 - diag) / (K - 1))\n    np.fill_diagonal(C, diag)\n    return C\n\n\ndef perturb(C, eps):\n    K = C.shape[0]\n    Cp = C.copy()\n    Cp[~np.eye(K, dtype=bool)] += eps\n    for j in range(K):\n        Cp[:, j] /= Cp[:, j].sum()\n    return Cp\n\n\ndef gen_Astar(A, Y, Cb, eps, rng):\n    if eps <= 0:\n        probs = Cb[:, A]\n    else:\n        Cp = perturb(Cb, eps)\n        high = Y > np.median(Y)\n        probs = np.where(high[None, :], Cp[:, A], Cb[:, A])\n    cum = np.cumsum(probs, axis=0)\n    u = rng.uniform(size=len(A))\n    return (u[None, :] >= cum[:-1]).sum(axis=0).astype(int)\n\n\n# ── Main ────────────────────────────────────────────────────\n\ndef main():\n    t0 = time.time()\n    out_dir = os.path.dirname(os.path.abspath(__file__))\n    n_total = len(TOPOLOGIES) * len(K_VALUES) * len(EPSILONS) * len(CM_QUALS)\n    print(f\"Exp-A: {n_total} configs x {N_REPS} MC reps, N={N_SAMPLES}\")\n\n    # Validate CMs\n    for K in K_VALUES:\n        for dv in CM_QUALS.values():\n            C = make_cm(K, dv)\n            assert np.allclose(C.sum(axis=0), 1.0), f\"K={K} diag={dv}: bad CM\"\n            for eps in EPSILONS:\n                if eps > 0:\n                    Cp = perturb(C, eps)\n                    assert np.allclose(Cp.sum(axis=0), 1.0)\n                    assert (Cp >= -1e-12).all()\n\n    all_params = {K: make_dgp_params(K) for K in K_VALUES}\n\n    # True parameters (oracle with N=2M)\n    tau_trues = {}\n    print(\"\\nTrue parameters (N=2M oracle):\")\n    for K in K_VALUES:\n        for topo in TOPOLOGIES:\n            rng = np.random.default_rng(K*1000 + abs(hash(topo)) % 1000)\n            fv, Y, A = GEN[topo](K, N_LARGE, all_params[K][topo], rng)\n            tau_trues[(K, topo)] = est_tau(topo, fv, Y, A, K)\n            print(f\"  K={K:>2} {topo:<13} tau_true={tau_trues[(K,topo)]:>10.6f}\")\n\n    # MC simulation\n    results = []\n    idx = 0\n    print(f\"\\nMC simulation ({n_total} configs):\")\n    for topo in TOPOLOGIES:\n        for K in K_VALUES:\n            p = all_params[K][topo]\n            tt = tau_trues[(K, topo)]\n            for qn, dv in CM_QUALS.items():\n                Cb = make_cm(K, dv)\n                for eps in EPSILONS:\n                    idx += 1\n                    rng = np.random.default_rng(SEED + idx*1000)\n                    hats = np.empty(N_REPS)\n                    for m in range(N_REPS):\n                        fv, Y, A = GEN[topo](K, N_SAMPLES, p, rng)\n                        As = gen_Astar(A, Y, Cb, eps, rng)\n                        hats[m] = est_tau(topo, fv, Y, As, K)\n\n                    ok = np.isfinite(hats)\n                    nv = int(ok.sum())\n                    if nv > 0 and abs(tt) > 1e-12:\n                        vh = hats[ok]\n                        sfr = float((np.sign(vh) != np.sign(tt)).mean())\n                        ratios = np.abs(vh / tt)\n                        br = float(ratios.mean())\n                        br_std = float(ratios.std())\n                        br_med = float(np.median(ratios))\n                        mt = float(vh.mean())\n                    else:\n                        sfr = br = br_std = br_med = mt = None\n\n                    results.append({\n                        'topology': topo, 'K': K, 'epsilon': eps,\n                        'cm_quality': qn, 'cm_diag': dv,\n                        'sign_flip_rate': sfr,\n                        'mean_bias_ratio': br,\n                        'std_bias_ratio': br_std,\n                        'median_bias_ratio': br_med,\n                        'tau_true': float(tt),\n                        'mean_tau_hat': mt,\n                        'n_reps': nv,\n                    })\n\n                    if idx % 12 == 0 or idx == n_total:\n                        el = time.time() - t0\n                        eta = el / idx * (n_total - idx)\n                        s = f\"SF={sfr:.3f} BR={br:.3f}\" if sfr is not None else \"N/A\"\n                        print(f\"  [{idx:>3}/{n_total}] {topo:<13} K={K:>2} \"\n                              f\"eps={eps:.2f} {qn:<6} {s}  \"\n                              f\"({el:.0f}s, ETA {eta:.0f}s)\")\n\n    # Summaries\n    def sm(vals):\n        v = [x for x in vals if x is not None]\n        return float(np.mean(v)) if v else None\n\n    by_eps = {}\n    for eps in EPSILONS:\n        sub = [r for r in results if r['epsilon'] == eps]\n        sfs = [r['sign_flip_rate'] for r in sub if r['sign_flip_rate'] is not None]\n        brs = [r['mean_bias_ratio'] for r in sub if r['mean_bias_ratio'] is not None]\n        by_eps[str(eps)] = {\n            'mean_sign_flip_rate': float(np.mean(sfs)) if sfs else None,\n            'mean_bias_ratio': float(np.mean(brs)) if brs else None,\n            'max_sign_flip_rate': float(max(sfs)) if sfs else None,\n        }\n\n    by_topo = {}\n    for topo in TOPOLOGIES:\n        sub = [r for r in results if r['topology'] == topo]\n        sfs = [r['sign_flip_rate'] for r in sub if r['sign_flip_rate'] is not None]\n        brs = [r['mean_bias_ratio'] for r in sub if r['mean_bias_ratio'] is not None]\n        by_topo[topo] = {\n            'mean_sign_flip_rate': float(np.mean(sfs)) if sfs else None,\n            'mean_bias_ratio': float(np.mean(brs)) if brs else None,\n        }\n\n    by_K = {}\n    for K in K_VALUES:\n        sub = [r for r in results if r['K'] == K]\n        sfs = [r['sign_flip_rate'] for r in sub if r['sign_flip_rate'] is not None]\n        brs = [r['mean_bias_ratio'] for r in sub if r['mean_bias_ratio'] is not None]\n        by_K[str(K)] = {\n            'mean_sign_flip_rate': float(np.mean(sfs)) if sfs else None,\n            'mean_bias_ratio': float(np.mean(brs)) if brs else None,\n        }\n\n    output = {\n        'results': results,\n        'summary': {'by_epsilon': by_eps, 'by_topology': by_topo, 'by_K': by_K},\n    }\n\n    def clean(o):\n        if isinstance(o, (float, np.floating)):\n            v = float(o)\n            return None if (np.isnan(v) or np.isinf(v)) else v\n        if isinstance(o, np.integer):\n            return int(o)\n        if isinstance(o, dict):\n            return {k: clean(v) for k, v in o.items()}\n        if isinstance(o, list):\n            return [clean(v) for v in o]\n        return o\n\n    output = clean(output)\n    jpath = os.path.join(out_dir, 'exp_a_stress_test_results.json')\n    with open(jpath, 'w') as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nJSON -> {jpath}\")\n\n    tpath = os.path.join(out_dir, 'exp_a_stress_test_table.tex')\n    write_tex(results, tpath)\n    print(f\"TeX  -> {tpath}\")\n\n    total = time.time() - t0\n    print(f\"\\nDone in {total:.0f}s ({total/60:.1f}min)\")\n    print(\"\\nBy epsilon:\")\n    for eps, s in by_eps.items():\n        sf = s['mean_sign_flip_rate']\n        br = s['mean_bias_ratio']\n        mx = s['max_sign_flip_rate']\n        print(f\"  eps={eps}: meanSF={sf:.4f} meanBR={br:.4f} maxSF={mx:.4f}\")\n    print(\"\\nBy topology:\")\n    for topo, s in by_topo.items():\n        print(f\"  {topo:<13}: SF={s['mean_sign_flip_rate']:.4f} \"\n              f\"BR={s['mean_bias_ratio']:.4f}\")\n    print(\"\\nBy K:\")\n    for k, s in by_K.items():\n        print(f\"  K={k}: SF={s['mean_sign_flip_rate']:.4f} \"\n              f\"BR={s['mean_bias_ratio']:.4f}\")\n\n\ndef write_tex(results, path):\n    ncols = 3 + 2 * len(EPSILONS)\n    lines = [\n        r'\\begin{table*}[t]',\n        r'\\centering',\n        r'\\caption{Non-differential misclassification stress test: sign flip rate (SF) '\n        r'and mean bias ratio (BR\\,$=\\overline{|\\hat\\tau/\\tau|}$) under increasing '\n        r'differential departure $\\varepsilon$.}',\n        r'\\label{tab:stress-test}',\n        r'\\small\\setlength{\\tabcolsep}{3.5pt}',\n        r'\\begin{tabular}{llc' + 'rr' * len(EPSILONS) + '}',\n        r'\\toprule',\n    ]\n\n    h1 = r'Topology & $K$ & Q'\n    for e in EPSILONS:\n        h1 += rf' & \\multicolumn{{2}}{{c}}{{$\\varepsilon\\!=\\!{e}$}}'\n    lines.append(h1 + r' \\\\')\n\n    clines = ' '.join(\n        rf'\\cmidrule(lr){{{4+2*i}-{5+2*i}}}' for i in range(len(EPSILONS)))\n    lines.append(clines)\n\n    h2 = r' & &'\n    for _ in EPSILONS:\n        h2 += r' & {\\scriptsize SF} & {\\scriptsize BR}'\n    lines.append(h2 + r' \\\\')\n    lines.append(r'\\midrule')\n\n    for ti, topo in enumerate(TOPOLOGIES):\n        if ti > 0:\n            lines.append(r'\\midrule')\n        first_t = True\n        for ki, K in enumerate(K_VALUES):\n            if ki > 0:\n                lines.append(rf'\\cmidrule{{2-{ncols}}}')\n            first_k = True\n            for qn in CM_QUALS:\n                tl = topo.capitalize() if first_t else ''\n                kl = str(K) if first_k else ''\n                row = f'{tl} & {kl} & {qn[0].upper()}'\n                for eps in EPSILONS:\n                    r = next(x for x in results\n                             if x['topology'] == topo and x['K'] == K\n                             and x['epsilon'] == eps and x['cm_quality'] == qn)\n                    sf = r['sign_flip_rate']\n                    br = r['mean_bias_ratio']\n                    sfs = f'{sf:.2f}' if sf is not None else '--'\n                    brs = f'{br:.2f}' if br is not None else '--'\n                    row += f' & {sfs} & {brs}'\n                lines.append(row + r' \\\\')\n                first_t = False\n                first_k = False\n\n    lines += [\n        r'\\bottomrule',\n        r'\\end{tabular}',\n        r'\\vspace{1mm}',\n        r'\\parbox{\\textwidth}{\\footnotesize '\n        r'SF\\,=\\,sign flip rate; BR\\,=\\,mean $|\\hat\\tau/\\tau|$ '\n        r'(1.00 = unbiased). '\n        r'$\\varepsilon\\!=\\!0$: non-differential; $\\varepsilon\\!>\\!0$: '\n        r'outcome-dependent misclassification. '\n        r'Q: H/M/L\\,=\\,CM diagonal 0.8/0.6/0.4 with uniform off-diagonal. '\n        r'Each cell: $N\\!=\\!10{,}000\\!\\times\\!100$ MC replications.}',\n        r'\\end{table*}',\n    ]\n    with open(path, 'w') as f:\n        f.write('\\n'.join(lines) + '\\n')\n\n\nif __name__ == '__main__':\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T11:24:24.990892+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T11:24:24.991045+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python artifacts/exp_a_stress_test.py 2>&1",
  "description": "Run Exp-A stress test: 96 configs × 100 MC reps",
  "timeout": "600000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Bash",
  "tool_args": {
    "command": "python artifacts/exp_a_stress_test.py 2>&1",
    "description": "Run Exp-A stress test: 96 configs × 100 MC reps",
    "timeout": "600000"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T11:24:24.991183+00:00_

Exit code 127
/bin/bash: line 1: python: command not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T11:24:24.991301+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 artifacts/exp_a_stress_test.py 2>&1",
  "description": "Run Exp-A stress test with python3",
  "timeout": "600000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 artifacts/exp_a_stress_test.py 2>&1",
    "description": "Run Exp-A stress test with python3",
    "timeout": "600000"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T11:24:24.991433+00:00_

Exp-A: 96 configs x 100 MC reps, N=10000

True parameters (N=2M oracle):
  K= 3 confounding   tau_true=  2.000452
  K= 3 mediation     tau_true=  0.501208
  K= 3 exposure      tau_true=  1.001102
  K= 3 iv            tau_true=  0.658211
  K=10 confounding   tau_true=  1.999778
  K=10 mediation     tau_true=  0.500440
  K=10 exposure      tau_true=  1.001081
  K=10 iv            tau_true=  1.118235

MC simulation (96 configs):
  [ 12/96] confounding   K= 3 eps=0.10 low    SF=0.000 BR=1.150  (15s, ETA 102s)
  [ 24/96] confounding   K=10 eps=0.10 low    SF=0.000 BR=1.112  (21s, ETA 64s)
  [ 36/96] mediation     K= 3 eps=0.10 low    SF=0.000 BR=1.599  (27s, ETA 44s)
  [ 48/96] mediation     K=10 eps=0.10 low    SF=0.000 BR=1.348  (36s, ETA 36s)
  [ 60/96] exposure      K= 3 eps=0.10 low    SF=0.050 BR=0.055  (39s, ETA 24s)
  [ 72/96] exposure      K=10 eps=0.10 low    SF=0.000 BR=0.426  (45s, ETA 15s)
  [ 84/96] iv            K= 3 eps=0.10 low    SF=0.070 BR=44.004  (51s, ETA 7s)
  [ 96/96] iv            K=10 eps=0.10 low    SF=0.000 BR=9.604  (58s, ETA 0s)

JSON -> /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test_results.json
TeX  -> /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test_table.tex

Done in 58s (1.0min)

By epsilon:
  eps=0.0: meanSF=0.0000 meanBR=1.7214 maxSF=0.0000
  eps=0.01: meanSF=0.0000 meanBR=1.7260 maxSF=0.0000
  eps=0.05: meanSF=0.0013 meanBR=2.1433 maxSF=0.0200
  eps=0.1: meanSF=0.0050 meanBR=3.3959 maxSF=0.0700

By topology:
  confounding  : SF=0.0000 BR=1.1123
  mediation    : SF=0.0000 BR=1.3950
  exposure     : SF=0.0025 BR=0.5230
  iv           : SF=0.0038 BR=5.9563

By K:
  K=3: SF=0.0031 BR=2.9865
  K=10: SF=0.0000 BR=1.5068

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T11:24:24.991597+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test_table.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test_table.tex"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-22T11:24:24.991741+00:00_

1	\begin{table*}[t]
2	\centering
3	\caption{Non-differential misclassification stress test: sign flip rate (SF) and mean bias ratio (BR\,$=\overline{|\hat\tau/\tau|}$) under increasing differential departure $\varepsilon$.}
4	\label{tab:stress-test}
5	\small\setlength{\tabcolsep}{3.5pt}
6	\begin{tabular}{llcrrrrrrrr}
7	\toprule
8	Topology & $K$ & Q & \multicolumn{2}{c}{$\varepsilon\!=\!0.0$} & \multicolumn{2}{c}{$\varepsilon\!=\!0.01$} & \multicolumn{2}{c}{$\varepsilon\!=\!0.05$} & \multicolumn{2}{c}{$\varepsilon\!=\!0.1$} \\
9	\cmidrule(lr){4-5} \cmidrule(lr){6-7} \cmidrule(lr){8-9} \cmidrule(lr){10-11}
10	 & & & {\scriptsize SF} & {\scriptsize BR} & {\scriptsize SF} & {\scriptsize BR} & {\scriptsize SF} & {\scriptsize BR} & {\scriptsize SF} & {\scriptsize BR} \\
11	\midrule
12	Confounding & 3 & H & 0.00 & 1.10 & 0.00 & 1.10 & 0.00 & 1.11 & 0.00 & 1.12 \\
13	 &  & M & 0.00 & 1.14 & 0.00 & 1.14 & 0.00 & 1.14 & 0.00 & 1.14 \\
14	 &  & L & 0.00 & 1.15 & 0.00 & 1.15 & 0.00 & 1.15 & 0.00 & 1.15 \\
15	\cmidrule{2-11}
16	 & 10 & H & 0.00 & 1.06 & 0.00 & 1.06 & 0.00 & 1.08 & 0.00 & 1.09 \\
17	 &  & M & 0.00 & 1.09 & 0.00 & 1.09 & 0.00 & 1.10 & 0.00 & 1.10 \\
18	 &  & L & 0.00 & 1.11 & 0.00 & 1.11 & 0.00 & 1.11 & 0.00 & 1.11 \\
19	\midrule
20	Mediation & 3 & H & 0.00 & 1.35 & 0.00 & 1.36 & 0.00 & 1.41 & 0.00 & 1.46 \\
21	 &  & M & 0.00 & 1.51 & 0.00 & 1.53 & 0.00 & 1.55 & 0.00 & 1.57 \\
22	 &  & L & 0.00 & 1.60 & 0.00 & 1.61 & 0.00 & 1.61 & 0.00 & 1.60 \\
23	\cmidrule{2-11}
24	 & 10 & H & 0.00 & 1.15 & 0.00 & 1.18 & 0.00 & 1.25 & 0.00 & 1.29 \\
25	 &  & M & 0.00 & 1.24 & 0.00 & 1.26 & 0.00 & 1.31 & 0.00 & 1.32 \\
26	 &  & L & 0.00 & 1.31 & 0.00 & 1.32 & 0.00 & 1.33 & 0.00 & 1.35 \\
27	\midrule
28	Exposure & 3 & H & 0.00 & 0.71 & 0.00 & 0.71 & 0.00 & 0.67 & 0.00 & 0.64 \\
29	 &  & M & 0.00 & 0.42 & 0.00 & 0.41 & 0.00 & 0.38 & 0.00 & 0.35 \\
30	 &  & L & 0.00 & 0.11 & 0.00 & 0.10 & 0.01 & 0.08 & 0.05 & 0.06 \\
31	\cmidrule{2-11}
32	 & 10 & H & 0.00 & 0.87 & 0.00 & 0.86 & 0.00
…[truncated 1021 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T11:24:24.991884+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test_results.json",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test_results.json",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-22T11:24:24.992031+00:00_

1	{
2	  "results": [
3	    {
4	      "topology": "confounding",
5	      "K": 3,
6	      "epsilon": 0.0,
7	      "cm_quality": "high",
8	      "cm_diag": 0.8,
9	      "sign_flip_rate": 0.0,
10	      "mean_bias_ratio": 1.1015599464124983,
11	      "std_bias_ratio": 0.004556093015165541,
12	      "median_bias_ratio": 1.1014664420476403,
13	      "tau_true": 2.000451504038447,
14	      "mean_tau_hat": 2.2036172515893937,
15	      "n_reps": 100
16	    },
17	    {
18	      "topology": "confounding",
19	      "K": 3,
20	      "epsilon": 0.01,
21	      "cm_quality": "high",
22	      "cm_diag": 0.8,
23	      "sign_flip_rate": 0.0,
24	      "mean_bias_ratio": 1.104051267054083,
25	      "std_bias_ratio": 0.0045990842693053495,
26	      "median_bias_ratio": 1.1042079467769277,
27	      "tau_true": 2.000451504038447,
28	      "mean_tau_hat": 2.2086010177138937,
29	      "n_reps": 100
30	    },
31	    {
32	      "topology": "confounding",
33	      "K": 3,
34	      "epsilon": 0.05,
35	      "cm_quality": "high",
36	      "cm_diag": 0.8,
37	      "sign_flip_rate": 0.0,
38	      "mean_bias_ratio": 1.1114994184165408,
39	      "std_bias_ratio": 0.004100728016773654,
40	      "median_bias_ratio": 1.1112502428175057,
41	      "tau_true": 2.000451504038447,
42	      "mean_tau_hat": 2.223500683309228,
43	      "n_reps": 100
44	    },
45	    {
46	      "topology": "confounding",
47	      "K": 3,
48	      "epsilon": 0.1,
49	      "cm_quality": "high",
50	      "cm_diag": 0.8,
51	      "sign_flip_rate": 0.0,
52	      "mean_bias_ratio": 1.118489980180931,
53	      "std_bias_ratio": 0.0036399667080638342,
54	      "median_bias_ratio": 1.1184393514672841,
55	      "tau_true": 2.000451504038447,
56	      "mean_tau_hat": 2.237484963104876,
57	      "n_reps": 100
58	    },
59	    {
60	      "topology": "confounding",
61	      "K": 3,
62	      "epsilon": 0.0,
63	      "cm_quality": "medium",
64	      "cm_diag": 0.6,
65	      "sign_flip_rate": 0.0,
66	      "mean_bias_ratio": 1.136938124355988,
67
…[truncated 440 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-22T11:24:24.992232+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test.py",
  "old_string": "                tl = topo.capitalize() if first_t else ''",
  "new_string": "                TOPO_LABELS = {'confounding': 'Confounding', 'mediation': 'Mediation',\n                               'exposure': 'Exposure', 'iv': 'IV'}\n                tl = TOPO_LABELS.get(topo, topo.capitalize()) if first_t else ''"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test.py",
    "old_string": "                tl = topo.capitalize() if first_t else ''",
    "new_string": "                TOPO_LABELS = {'confounding': 'Confounding', 'mediation': 'Mediation',\n                               'exposure': 'Exposure', 'iv': 'IV'}\n                tl = TOPO_LABELS.get(topo, topo.capitalize()) if first_t else ''"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-22T11:24:24.992415+00:00_

The file /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-22T11:24:24.992545+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 artifacts/exp_a_stress_test.py 2>&1",
  "description": "Re-run with IV label fix",
  "timeout": "600000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 artifacts/exp_a_stress_test.py 2>&1",
    "description": "Re-run with IV label fix",
    "timeout": "600000"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-22T11:24:24.992679+00:00_

Exp-A: 96 configs x 100 MC reps, N=10000

True parameters (N=2M oracle):
  K= 3 confounding   tau_true=  1.999494
  K= 3 mediation     tau_true=  0.498646
  K= 3 exposure      tau_true=  0.999268
  K= 3 iv            tau_true=  0.666699
  K=10 confounding   tau_true=  2.001391
  K=10 mediation     tau_true=  0.502447
  K=10 exposure      tau_true=  1.001286
  K=10 iv            tau_true=  1.107873

MC simulation (96 configs):
  [ 12/96] confounding   K= 3 eps=0.10 low    SF=0.000 BR=1.150  (14s, ETA 98s)
  [ 24/96] confounding   K=10 eps=0.10 low    SF=0.000 BR=1.111  (21s, ETA 62s)
  [ 36/96] mediation     K= 3 eps=0.10 low    SF=0.000 BR=1.607  (27s, ETA 45s)
  [ 48/96] mediation     K=10 eps=0.10 low    SF=0.000 BR=1.342  (36s, ETA 36s)
  [ 60/96] exposure      K= 3 eps=0.10 low    SF=0.050 BR=0.055  (39s, ETA 23s)
  [ 72/96] exposure      K=10 eps=0.10 low    SF=0.000 BR=0.426  (45s, ETA 15s)
  [ 84/96] iv            K= 3 eps=0.10 low    SF=0.070 BR=43.444  (50s, ETA 7s)
  [ 96/96] iv            K=10 eps=0.10 low    SF=0.000 BR=9.694  (58s, ETA 0s)

JSON -> /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test_results.json
TeX  -> /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test_table.tex

Done in 58s (1.0min)

By epsilon:
  eps=0.0: meanSF=0.0000 meanBR=1.7152 maxSF=0.0000
  eps=0.01: meanSF=0.0000 meanBR=1.7204 maxSF=0.0000
  eps=0.05: meanSF=0.0013 meanBR=2.1339 maxSF=0.0200
  eps=0.1: meanSF=0.0050 meanBR=3.3759 maxSF=0.0700

By topology:
  confounding  : SF=0.0000 BR=1.1121
  mediation    : SF=0.0000 BR=1.3963
  exposure     : SF=0.0025 BR=0.5233
  iv           : SF=0.0038 BR=5.9135

By K:
  K=3: SF=0.0031 BR=2.9604
  K=10: SF=0.0000 BR=1.5123

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T11:24:24.992810+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"Iv \" /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test_table.tex || echo \"No 'Iv ' found — fixed\"",
  "description": "Verify IV label fix"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"Iv \" /home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/exp_a_stress_test_table.tex || echo \"No 'Iv ' found — fixed\"",
    "description": "Verify IV label fix"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-22T11:24:24.992971+00:00_

No 'Iv ' found — fixed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_a_stress_test_20260522T110940",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-22T11:24:24.993124+00:00_

All 3 outputs generated successfully. Here's the results summary:

**96 configs** (4 topologies × 2 K × 3 CM qualities × 4 ε), each with 100 MC reps at N=10,000. Completed in 58s.

**Key findings:**

| | ε=0 (non-diff) | ε=0.01 | ε=0.05 | ε=0.10 |
|---|---|---|---|---|
| Mean SF rate | 0.000 | 0.000 | 0.001 | 0.005 |
| Max SF rate | 0.000 | 0.000 | 0.020 | 0.070 |
| Mean BR | 1.72 | 1.72 | 2.13 | 3.38 |

**By topology:**
- **Confounding**: No sign flips at any ε. BR ≈ 1.10–1.15 (mild amplification due to residual confounding from misclassified confounder). Stable across ε.
- **Mediation**: No sign flips. BR ≈ 1.15–1.61 (indirect effect leakage). Increases moderately with ε.
- **Exposure**: Sign flips appear at ε≥0.05 for K=3 low-quality CM (SF=5% at ε=0.10). BR < 1 (attenuation toward null), decreasing with ε.
- **IV**: Most sensitive. Sign flips at ε=0.10 for K=3 low-quality (SF=7%). Extreme BR for low-quality CMs (up to 44× for K=3) due to weak first-stage amplification in the Wald estimator.

**Verification:**
- ε=0: zero sign flips across all configs (consistent with non-differential theory for symmetric CMs)
- Sign flips monotonically increase with ε
- All CMs validated as column-stochastic

**Output files:**
- `artifacts/exp_a_stress_test_results.json` — full results with per-config metrics
- `artifacts/exp_a_stress_test_table.tex` — LaTeX table for Appendix B.3
- `artifacts/exp_a_stress_test.py` — reproducible script

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_exp_a_stress_test_20260522T110940"
}
```

</details>

---
