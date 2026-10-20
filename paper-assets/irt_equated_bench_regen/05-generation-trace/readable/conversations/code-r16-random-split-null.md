# code r16 random split null

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/chats/worker_code_r16_random_split_null_20260523T104440.jsonl`
- **Structured JSON:** [`a2c42b2034eaa07f1d99.json`](../../sessions/a2/a2c42b2034eaa07f1d99.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

55 recorded events

### Tool call

_source line 1 · 2026-05-23T10:49:07.543182+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix*.npz 2>/dev/null && ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv 2>/dev/null",
  "description": "Check data files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix*.npz 2>/dev/null && ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv 2>/dev/null",
    "description": "Check data files exist"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T10:49:07.543570+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix.npz
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix_index.npz
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T10:49:07.543786+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find MH-DIF implementation",
  "prompt": "Search the project at /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen for existing Mantel-Haenszel DIF implementations. Look in:\n1. artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py\n2. artifacts/r22_within_arch_temporal/within_arch_temporal.py\n3. Any other Python files that implement MH statistics or delta_MH\n\nI need to understand how they compute MH-DIF with stratified total-score matching. Report the key function signatures and the core MH computation logic (the numpy/scipy code that computes the MH odds ratio and delta_MH). Be thorough - search for \"mantel\" \"haenszel\" \"delta_mh\" \"mh_stat\" patterns across all .py files."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find MH-DIF implementation",
    "prompt": "Search the project at /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen for existing Mantel-Haenszel DIF implementations. Look in:\n1. artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py\n2. artifacts/r22_within_arch_temporal/within_arch_temporal.py\n3. Any other Python files that implement MH statistics or delta_MH\n\nI need to understand how they compute MH-DIF with stratified total-score matching. Report the key function signatures and the core MH computation logic (the numpy/scipy code that computes the MH odds ratio and delta_MH). Be thorough - search for \"mantel\" \"haenszel\" \"delta_mh\" \"mh_stat\" patterns across all .py files."
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-23T10:49:07.543975+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen -type f -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen -type f -name \"*.py\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-23T10:49:07.544198+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_A1_subject_heatmap.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_2_dose_response.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_4_downstream_impact.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_3_within_subject_matching.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_A3_rho_degradation.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_A2_q3_distribution.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_1_global_vs_differential.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/scripts/r16_dif_union.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/scripts/r14_cooks_d_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/scripts/r14_domain_profile.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_simulation.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/mf2_deff_estimation.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_004_step3_gsm1k_dif_correlation.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/dif_power_simulation.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_024_within_family.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/
…[truncated 587 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-23T10:49:07.544389+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport numpy as np\nrm = np.load('artifacts/response_matrix.npz', allow_pickle=True)\nprint('Response matrix keys:', list(rm.keys()))\nfor k in rm.keys():\n    print(f'  {k}: shape={rm[k].shape}, dtype={rm[k].dtype}')\nidx = np.load('artifacts/response_matrix_index.npz', allow_pickle=True)\nprint('Index keys:', list(idx.keys()))\nfor k in idx.keys():\n    print(f'  {k}: shape={idx[k].shape}, dtype={idx[k].dtype}')\n    if idx[k].ndim == 1 and len(idx[k]) < 10:\n        print(f'    values: {idx[k]}')\n    elif idx[k].ndim == 1:\n        print(f'    first 5: {idx[k][:5]}')\n\"\n",
  "description": "Inspect response matrix structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport numpy as np\nrm = np.load('artifacts/response_matrix.npz', allow_pickle=True)\nprint('Response matrix keys:', list(rm.keys()))\nfor k in rm.keys():\n    print(f'  {k}: shape={rm[k].shape}, dtype={rm[k].dtype}')\nidx = np.load('artifacts/response_matrix_index.npz', allow_pickle=True)\nprint('Index keys:', list(idx.keys()))\nfor k in idx.keys():\n    print(f'  {k}: shape={idx[k].shape}, dtype={idx[k].dtype}')\n    if idx[k].ndim == 1 and len(idx[k]) < 10:\n        print(f'    values: {idx[k]}')\n    elif idx[k].ndim == 1:\n        print(f'    first 5: {idx[k][:5]}')\n\"\n",
    "description": "Inspect response matrix structure"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T10:49:07.544547+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "mantel|haenszel|delta_mh|mh_stat",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "type": "py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Grep",
  "tool_args": {
    "pattern": "mantel|haenszel|delta_mh|mh_stat",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
    "type": "py",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T10:49:07.544687+00:00_

Found 63 files
artifacts/difficulty_modeltype_interaction/interaction_analysis.py
artifacts/k3_power_simulation/k3_power_simulation.py
artifacts/r20_size_stratified_deff/size_stratified_deff.py
artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py
artifacts/r19_open_closed_dif/open_closed_dif_analysis.py
artifacts/r19_temporal_granularity/temporal_granularity_analysis.py
artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py
artifacts/r18_restricted_range_rho/restricted_rho_analysis.py
artifacts/mf2_deff_estimation/mf2_deff_estimation_v3.py
artifacts/_project/intermediate/mf2_deff_estimation.py
artifacts/mf2_deff_estimation/mf2_deff_estimation.py
artifacts/predictive_model/phase2_train.py
artifacts/mf2_rho_degradation/run_simulation.py
artifacts/sf1_cluster_bootstrap/run_bootstrap.py
artifacts/sf8_power_sensitivity/sf8_power_sensitivity.py
artifacts/plan_034_multi_subject_injection/plan_034_multi_subject_injection.py
artifacts/plan_034/intermediate/plan_034_multi_subject_injection.py
artifacts/plan_033_subject_dif_concentration/plan_033_subject_dif_concentration.py
artifacts/plan_031_temporal_granularity/plan_031_temporal_granularity.py
artifacts/plan_031_temporal_granularity/intermediate/plan_031_temporal_granularity.py
artifacts/plan_028_multi_bench_dif/plan_028_multi_bench_dif.py
artifacts/plan_028_multi_bench_dif/intermediate/plan_028_multi_bench_dif.py
artifacts/plan_027_temporal_overlap/plan_027_temporal_overlap.py
artifacts/plan_026/intermediate/plan_026_constat_dif_comparison.py
artifacts/plan_026/plan_026_constat_dif_comparison.py
artifacts/_project/intermediate/plan_024_within_family.py
artifacts/plan_024/plan_024_within_family.py
artifacts/plan_022/intermediate/plan_022_model_independence.py
artifacts/plan_022/plan_022_model_independence.py
artifacts/plan_023/intermediate/plan_023_item_characterization.py
artifacts/plan_023/plan_023_item_characterization.py
artifacts/plan_010/plan_010_arch_stratified_dif.py
artifacts/_project/data/plan_020_circu
…[truncated 1712 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T10:49:07.544881+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T10:49:07.545015+00:00_

artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T10:49:07.545139+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_within_arch_temporal/within_arch_temporal.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_within_arch_temporal/within_arch_temporal.py"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T10:49:07.545255+00:00_

artifacts/r22_within_arch_temporal/within_arch_temporal.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T10:49:07.545372+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -5 artifacts/model_metadata.csv && echo \"---\" && python3 -c \"\nimport pandas as pd\ndf = pd.read_csv('artifacts/model_metadata.csv')\nprint('Columns:', list(df.columns))\nprint('cohort_temporal values:', df['cohort_temporal'].value_counts().to_dict())\nprint('2023 count:', (df['cohort_temporal']==2023).sum())\n\"\n",
  "description": "Check model metadata structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Bash",
  "tool_args": {
    "command": "head -5 artifacts/model_metadata.csv && echo \"---\" && python3 -c \"\nimport pandas as pd\ndf = pd.read_csv('artifacts/model_metadata.csv')\nprint('Columns:', list(df.columns))\nprint('cohort_temporal values:', df['cohort_temporal'].value_counts().to_dict())\nprint('2023 count:', (df['cohort_temporal']==2023).sum())\n\"\n",
    "description": "Check model metadata structure"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-23T10:49:07.545499+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-23T10:49:07.545692+00:00_

1	#!/usr/bin/env python3
2	"""
3	mmlu_bootstrap_ci.py — MMLU bootstrap 95% CI for MH-DIF C%.
4	
5	Vectorized total-score stratification (~100x faster than per-item rest-score).
6	For J=12508, total-score ≈ rest-score (diff < 0.3pp); validated at startup.
7	"""
8	
9	import numpy as np
10	import pandas as pd
11	from scipy.stats import chi2 as chi2_dist
12	from scipy.sparse import load_npz
13	from pathlib import Path
14	from multiprocessing import Pool
15	import time
16	import warnings
17	
18	warnings.filterwarnings("ignore", category=RuntimeWarning)
19	
20	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/"
21	            "projects/irt_equated_bench_regen/artifacts")
22	OUT = BASE / "plan_028_bootstrap_ci"
23	OUT.mkdir(exist_ok=True)
24	
25	N_BOOTSTRAP = 1000
26	N_CONTROL = 20
27	SEED = 42
28	N_STRATA = 5
29	
30	
31	# ════════════════════════════════════════════════════════════════════════
32	#  VECTORIZED MH-DIF (total-score stratification)
33	# ════════════════════════════════════════════════════════════════════════
34	def mh_dif_c_pct_vec(X_ref, X_foc, n_strata=N_STRATA):
35	    """Fully vectorized MH-DIF → C%. Stratifies on total score (not rest)."""
36	    n_ref, J = X_ref.shape
37	    n_foc = X_foc.shape[0]
38	
39	    tot_ref = X_ref.sum(axis=1).astype(np.float64)
40	    tot_foc = X_foc.sum(axis=1).astype(np.float64)
41	    s_all = np.concatenate([tot_ref, tot_foc])
42	
43	    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
44	    n_bins = len(edges) - 1
45	    if n_bins < 1:
46	        return 0.0
47	
48	    k_ref = np.digitize(tot_ref, edges[1:-1])
49	    k_foc = np.digitize(tot_foc, edges[1:-1])
50	
51	    n1 = np.zeros(n_bins, dtype=np.float64)
52	    n0 = np.zeros(n_bins, dtype=np.float64)
53	    A = np.zeros((n_bins, J), dtype=np.float64)
54	    C = np.zeros((n_bins, J), dtype=np.float64)
55	
56	    for k in range(n_bins):
57	        mr = (k_ref == k)
58	        mf = (k_foc == k)
59	        n1[k] = mr.sum()
60	        n0[k]
…[truncated 11568 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-23T10:49:07.545889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_within_arch_temporal/within_arch_temporal.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r22_within_arch_temporal/within_arch_temporal.py"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-23T10:49:07.546060+00:00_

1	#!/usr/bin/env python3
2	"""R22: Within-architecture temporal DIF analysis.
3	
4	Groups fine-grained families into architecture lineages (e.g., llama-2 + llama-3 → Llama),
5	then runs MH-DIF within each lineage (2023 vs 2024) to rule out the confound that
6	overall temporal DIF is driven by cross-architecture differences.
7	"""
8	
9	import numpy as np
10	import pandas as pd
11	from scipy import sparse
12	from scipy.stats import chi2 as chi2_dist
13	
14	ROOT = "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts"
15	OUT = f"{ROOT}/r22_within_arch_temporal"
16	
17	N_STRATA = 5
18	ALPHA = 0.05
19	DELTA_THRESH = 1.5
20	MIN_PER_COHORT = 10
21	
22	# ── Architecture lineage mapping ────────────────────────────────────────────
23	# Maps fine-grained family → broad architecture lineage.
24	# Only families that appear in model_metadata.csv and have a cross-year counterpart.
25	ARCH_LINEAGE = {
26	    "llama-2":    "Llama",
27	    "codellama":  "Llama",
28	    "llama-3":    "Llama",
29	    "qwen":       "Qwen",
30	    "qwen-1.5":   "Qwen",
31	    "qwen-2":     "Qwen",
32	    "yi":         "Yi",
33	    "yi-1.5":     "Yi",
34	    "phi-2":      "Phi",
35	    "phi-3":      "Phi",
36	}
37	
38	
39	# ── MH-DIF (vectorized, from r18) ──────────────────────────────────────────
40	
41	def mh_dif_full(X_ref, X_foc, n_strata=N_STRATA):
42	    n_ref, J = X_ref.shape
43	    n_foc = X_foc.shape[0]
44	
45	    tot_ref = np.asarray(X_ref.sum(axis=1), dtype=np.float64).ravel()
46	    tot_foc = np.asarray(X_foc.sum(axis=1), dtype=np.float64).ravel()
47	    s_all = np.concatenate([tot_ref, tot_foc])
48	
49	    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
50	    n_bins = len(edges) - 1
51	    if n_bins < 1:
52	        return 0.0, np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)
53	
54	    k_ref = np.digitize(tot_ref, edges[1:-1])
55	    k_foc = np.digitize(tot_foc, edges[1:-1])
56	
57	    n1 = np.zeros(n_bins, dtype=np.float64)
58	 
…[truncated 7885 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-23T10:49:07.546218+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "def.*mantel|def.*haenszel|def.*delta_mh|def.*mh_stat",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
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
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Grep",
  "tool_args": {
    "pattern": "def.*mantel|def.*haenszel|def.*delta_mh|def.*mh_stat",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
    "type": "py",
    "output_mode": "content",
    "head_limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-23T10:49:07.546345+00:00_

artifacts/mf2_deff_estimation/mf2_deff_estimation.py:204:    out_cols = ['item_id', 'subject', 'icc', 'deff', 'delta_mh', 'se',
artifacts/_project/intermediate/dif_phase2_simulation.py:58:    def mantel_haenszel_dif(responses, group, n_strata=N_STRATA):
artifacts/dif_phase2_simulation.py:58:    def mantel_haenszel_dif(responses, group, n_strata=N_STRATA):
artifacts/_project/intermediate/dif_power_simulation.py:57:def mantel_haenszel_dif(responses, group, n_strata=N_STRATA):
artifacts/_project/intermediate/mf2_deff_estimation.py:204:    out_cols = ['item_id', 'subject', 'icc', 'deff', 'delta_mh', 'se',
artifacts/k3_power_simulation/k3_power_simulation.py:56:def mantel_haenszel_dif(responses, group, n_strata):
artifacts/dif_power_simulation.py:57:def mantel_haenszel_dif(responses, group, n_strata=N_STRATA):
artifacts/sf8_power_sensitivity/sf8_power_sensitivity.py:82:def mantel_haenszel_dif(responses, group):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-23T10:49:07.546481+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_phase2_simulation.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_phase2_simulation.py"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-23T10:49:07.546729+00:00_

1	"""
2	Phase 2: Semi-synthetic DIF power simulation using real MMLU IRT parameters
3	from PSN-IRT (4PL → 2PL: take a, b only).
4	
5	Validates Phase 1 findings (synthetic params) with real parameter distributions.
6	Each replication samples 200 items (w/o replacement) from the 14042-item MMLU pool.
7	"""
8	
9	import os
10	import sys
11	import time
12	import warnings
13	import numpy as np
14	import pandas as pd
15	from scipy import stats
16	from scipy.special import expit
17	from sklearn.metrics import roc_auc_score
18	from statsmodels.stats.multitest import multipletests
19	import matplotlib
20	matplotlib.use("Agg")
21	import matplotlib.pyplot as plt
22	from itertools import product
23	
24	warnings.filterwarnings("ignore", category=RuntimeWarning)
25	warnings.filterwarnings("ignore", category=FutureWarning)
26	
27	ARTIFACTS_DIR = os.path.dirname(os.path.abspath(__file__))
28	N_ITEMS = 200
29	N_CONTAMINATED = 20
30	N_STRATA = 5
31	ALPHA = 0.05
32	SEED = 42
33	
34	# Benchmark item counts (alphabetical order in PSN-IRT combine.csv)
35	BENCHMARK_SIZES = [
36	    ("ARC-C", 295), ("BBH", 6511), ("Chinese SimpleQA", 3000),
37	    ("GPQA Diamond", 198), ("GSM8K", 1319), ("HellaSwag", 10042),
38	    ("HumanEval", 164), ("MATH", 5000), ("MBPP", 500),
39	    ("MMLU", 14042), ("TheoremQA", 800),
40	]
41	
42	sys.path.insert(0, ARTIFACTS_DIR)
43	try:
44	    from dif_power_simulation import (
45	        generate_responses, mantel_haenszel_dif,
46	        logistic_regression_dif, _batched_logistic_ll,
47	    )
48	except ImportError:
49	    print("WARNING: Could not import from dif_power_simulation.py, using inline copies")
50	    def generate_responses(theta, a, b, delta=None, contaminated_mask=None):
51	        b_adj = b.copy()
52	        if delta is not None and contaminated_mask is not None:
53	            b_adj[contaminated_mask] = b[contaminated_mask] - delta
54	        logit = a[np.newaxis, :] * (theta[:, np.newaxis] - b_adj[np.newaxis, :])
55	        prob = expit(logit)
56	 
…[truncated 23241 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-23T10:49:07.546912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_power_simulation.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_power_simulation.py"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-23T10:49:07.547117+00:00_

1	"""
2	DIF Power Monte Carlo Simulation for Benchmark Contamination Detection.
3	
4	Simulates 2PL IRT response data with injected contamination (DIF) on a subset
5	of items, then evaluates whether Mantel-Haenszel and Logistic Regression DIF
6	methods can detect the contaminated items with sufficient statistical power.
7	
8	v2: BH correction, FPR>0.15 kill, GRAY zone, verdict column.
9	    Vectorized MH (no item loop) + batched IRLS LR for speed.
10	"""
11	
12	import os
13	import sys
14	import time
15	import warnings
16	import numpy as np
17	import pandas as pd
18	from scipy import stats
19	from scipy.special import expit
20	from sklearn.metrics import roc_auc_score
21	from statsmodels.stats.multitest import multipletests
22	import matplotlib
23	matplotlib.use("Agg")
24	import matplotlib.pyplot as plt
25	from itertools import product
26	
27	warnings.filterwarnings("ignore", category=RuntimeWarning)
28	warnings.filterwarnings("ignore", category=FutureWarning)
29	
30	ARTIFACTS_DIR = os.path.dirname(os.path.abspath(__file__))
31	N_ITEMS = 200
32	N_CONTAMINATED = 20
33	N_STRATA = 5
34	ALPHA = 0.05
35	SEED = 42
36	
37	# ─── Data Generation ────────────────────────────────────────────────────────
38	
39	def generate_item_params(n_items, rng):
40	    a = rng.lognormal(mean=0.0, sigma=0.5, size=n_items)
41	    a = np.clip(a, 0.3, 2.5)
42	    b = rng.normal(0.0, 1.0, size=n_items)
43	    return a, b
44	
45	
46	def generate_responses(theta, a, b, delta=None, contaminated_mask=None):
47	    b_adj = b.copy()
48	    if delta is not None and contaminated_mask is not None:
49	        b_adj[contaminated_mask] = b[contaminated_mask] - delta
50	    logit = a[np.newaxis, :] * (theta[:, np.newaxis] - b_adj[np.newaxis, :])
51	    prob = expit(logit)
52	    return (np.random.random(prob.shape) < prob).astype(np.int8)
53	
54	
55	# ─── Mantel-Haenszel DIF (vectorized across items) ────────────────────────
56	
57	def mantel_haenszel_dif(responses, group, n_strata=N_STRATA):
58	    n_total, 
…[truncated 16312 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-23T10:49:07.547280+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_simulation.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/k3_power_simulation/k3_power_simulation.py"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-23T10:49:07.547461+00:00_

1	"""
2	K=3 vs K=5 Strata Power Simulation for MH-DIF Detection.
3	
4	Tests whether K=3 strata provides adequate power for contamination detection,
5	supporting the paper claim "smaller corpora may suffice with K=3".
6	
7	PSN-IRT empirical parameters: ā=1.2, b̄=-0.84
8	Grid: K∈{3,5} × N∈{40,60,80,100,200,500} × δ∈{0.6,0.8,1.0,1.2,1.4}
9	1000 replications per condition, MH-DIF only.
10	"""
11	
12	import os, sys, time, warnings
13	import numpy as np
14	import pandas as pd
15	from scipy import stats
16	from scipy.special import expit
17	from sklearn.metrics import roc_auc_score
18	from statsmodels.stats.multitest import multipletests
19	from itertools import product
20	
21	warnings.filterwarnings("ignore", category=RuntimeWarning)
22	
23	OUT_DIR = os.path.dirname(os.path.abspath(__file__))
24	
25	N_ITEMS = 200
26	N_CONTAMINATED = 20
27	ALPHA = 0.05
28	SEED = 42
29	
30	A_MEAN = 1.2
31	B_MEAN = -0.84
32	
33	K_VALUES = [3, 5]
34	N_VALUES = [40, 60, 80, 100, 200, 500]
35	DELTA_VALUES = [0.6, 0.8, 1.0, 1.2, 1.4]
36	
37	
38	def generate_item_params(n_items, rng):
39	    sigma_a = 0.4
40	    mu_a = np.log(A_MEAN) - sigma_a**2 / 2
41	    a = rng.lognormal(mean=mu_a, sigma=sigma_a, size=n_items)
42	    a = np.clip(a, 0.3, 2.5)
43	    b = rng.normal(B_MEAN, 1.0, size=n_items)
44	    return a, b
45	
46	
47	def generate_responses(theta, a, b, delta=None, contaminated_mask=None, rng=None):
48	    b_adj = b.copy()
49	    if delta is not None and contaminated_mask is not None:
50	        b_adj[contaminated_mask] = b[contaminated_mask] - delta
51	    logit = a[np.newaxis, :] * (theta[:, np.newaxis] - b_adj[np.newaxis, :])
52	    prob = expit(logit)
53	    return (rng.random(prob.shape) < prob).astype(np.int8)
54	
55	
56	def mantel_haenszel_dif(responses, group, n_strata):
57	    n_total, n_items = responses.shape
58	    total_score = responses.sum(axis=1).astype(float)
59	
60	    try:
61	        _, bin_edges = pd.qcut(total_score, q=n_strata, retbins=True, duplicates="drop")
62	    ex
…[truncated 11145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-23T10:49:07.547622+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "def mantel_haenszel_dif|def mh_dif_full",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf8_power_sensitivity/sf8_power_sensitivity.py",
  "output_mode": "content",
  "context": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Grep",
  "tool_args": {
    "pattern": "def mantel_haenszel_dif|def mh_dif_full",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/sf8_power_sensitivity/sf8_power_sensitivity.py",
    "output_mode": "content",
    "context": "50"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-23T10:49:07.547783+00:00_

32-    ("MMLU", 14042), ("TheoremQA", 800),
33-]
34-
35-
36-def load_mmlu_params():
37-    csv_path = os.path.join(PROJECT_ARTIFACTS, "psn_irt_item_parameters.csv")
38-    df = pd.read_csv(csv_path)
39-    cumulative = np.cumsum([s for _, s in BENCHMARK_SIZES])
40-    mmlu_idx = [name for name, _ in BENCHMARK_SIZES].index("MMLU")
41-    start = cumulative[mmlu_idx - 1] if mmlu_idx > 0 else 0
42-    end = cumulative[mmlu_idx]
43-    mmlu = df.iloc[start:end]
44-    a = mmlu["discrimination"].values.astype(np.float64)
45-    b = mmlu["difficulty"].values.astype(np.float64)
46-    valid = (a > 0) & np.isfinite(a) & np.isfinite(b)
47-    return a[valid], b[valid]
48-
49-
50-def load_metabench_params():
51-    csv_path = os.path.join(PROJECT_ARTIFACTS, "_project/data/metabench_irt_params.csv")
52-    df = pd.read_csv(csv_path)
53-    df = df[df["exclude"] == False].copy()
54-    a = df["disc"].values.astype(np.float64)
55-    b = df["diff"].values.astype(np.float64)
56-    valid = np.isfinite(a) & np.isfinite(b)
57-    return a[valid], b[valid], len(df)
58-
59-
60-def compute_descriptives(values, name):
61-    return {
62-        "parameter": name,
63-        "n": len(values),
64-        "mean": np.mean(values),
65-        "sd": np.std(values, ddof=1),
66-        "min": np.min(values),
67-        "q1": np.percentile(values, 25),
68-        "median": np.percentile(values, 50),
69-        "q3": np.percentile(values, 75),
70-        "max": np.max(values),
71-        "skewness": stats.skew(values),
72-        "kurtosis": stats.kurtosis(values),
73-    }
74-
75-
76-def generate_responses(theta, a, b):
77-    logit = a[np.newaxis, :] * (theta[:, np.newaxis] - b[np.newaxis, :])
78-    prob = expit(logit)
79-    return (np.random.random(prob.shape) < prob).astype(np.int8)
80-
81-
82:def mantel_haenszel_dif(responses, group):
83-    n_total, n_items = responses.shape
84-    total_score = responses.sum(axis=1).astype(float)
85-    try:
86-        _, bin_edges = pd.qcut(total_score
…[truncated 1836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-23T10:49:07.547937+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_deff_estimation/mf2_deff_estimation.py",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mf2_deff_estimation/mf2_deff_estimation.py",
    "limit": "250"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-23T10:49:07.548124+00:00_

1	"""
2	MF2: Design Effect (DEFF) Estimation
3	Quantifies non-independence within model families and adjusts DIF chi-squared.
4	"""
5	import numpy as np
6	import pandas as pd
7	from scipy import sparse
8	from scipy.stats import chi2
9	from pathlib import Path
10	import time
11	
12	ROOT = Path(__file__).resolve().parent.parent.parent
13	ARTIFACTS = ROOT / "artifacts"
14	OUT = ARTIFACTS / "mf2_deff_estimation"
15	OUT.mkdir(parents=True, exist_ok=True)
16	
17	
18	def load_data():
19	    f = np.load(ARTIFACTS / "response_matrix.npz")
20	    X = sparse.csr_matrix((f['data'], f['indices'], f['indptr']), shape=tuple(f['shape']))
21	    idx = np.load(ARTIFACTS / "response_matrix_index.npz", allow_pickle=True)
22	    model_names = idx['model_names']
23	    item_ids = idx['item_ids']
24	
25	    meta = pd.read_csv(ARTIFACTS / "plan_032_dif_cleaned_mmlu" / "cleaned_mmlu_analysis.csv")
26	    dif = pd.read_csv(ARTIFACTS / "plan_001" / "dif_results_temporal.csv")
27	    return X, model_names, item_ids, meta, dif
28	
29	
30	def filter_valid_models(meta, model_names):
31	    """Exclude NaN family, 'unknown', and families with size < 2."""
32	    fc = meta['family'].value_counts()
33	    valid_families = [f for f in fc[fc >= 2].index if f != 'unknown' and pd.notna(f)]
34	
35	    mask = meta['family'].isin(valid_families)
36	    valid_meta = meta.loc[mask].copy()
37	
38	    model_name_to_idx = {name: i for i, name in enumerate(model_names)}
39	    valid_indices = []
40	    valid_families_list = []
41	    valid_model_names_list = []
42	    for _, row in valid_meta.iterrows():
43	        m = row['model_name']
44	        if m in model_name_to_idx:
45	            valid_indices.append(model_name_to_idx[m])
46	            valid_families_list.append(row['family'])
47	            valid_model_names_list.append(m)
48	
49	    return (np.array(valid_indices), np.array(valid_families_list),
50	            valid_model_names_list, valid_families)
51	
52	
53	def compute_icc_vectorized(X_valid, famil
…[truncated 7803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T10:49:07.548378+00:00_

Excellent! Now I have a comprehensive view. Let me create a final summary report of all the MH-DIF implementations I've found:

## Summary: Mantel-Haenszel DIF Implementations

I've thoroughly searched the project and found **multiple complete MH-DIF implementations** using stratified total-score matching. Here are the key implementations:

### 1. **Vectorized Bootstrap CI (mmlu_bootstrap_ci.py)**
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_bootstrap_ci/mmlu_bootstrap_ci.py`

**Key Function:**
```python
def mh_dif_c_pct_vec(X_ref, X_foc, n_strata=N_STRATA):
    """Fully vectorized MH-DIF → C%. Stratifies on total score (not rest)."""
```

**Core MH Computation Logic (lines 34-101):**
- **Stratification:** Uses `np.digitize()` to partition reference and focal groups by total score quantiles
- **Contingency accumulation:** For each stratum k:
  - `A[k]` = correct answers in reference group
  - `C[k]` = correct answers in focal group  
  - `B[k]` = n1 - A[k]` (incorrect in reference)
  - `D[k]` = n0 - C[k]` (incorrect in focal)
- **Odds ratio computation:**
  ```python
  Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)  # Sum over strata
  Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)
  ```
- **Delta_MH calculation:**
  ```python
  delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)
  ```
  (The constant 2.35 = LN(8) is the ETS scaling factor)

- **Chi-squared test statistic:**
  ```python
  EA = np.where(valid, n1[:, None] * m1 / Nk, 0)  # Expected A
  sum_diff = np.where(valid, A - EA, 0).sum(axis=0)
  sum_var = np.where(valid, n1[:, None] * n0[:, None] * m1 * m0 / (Nk**2 * Nk_m1), 0).sum(axis=0)
  chi2_j = np.where(sum_var > 0, np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30), 0)
  pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)
  ```

- **ETS Classification:** Items flagged as "C" if `|delta_j| >= 1.5 AND p < 0.05`

---

### 2. **Full Output MH-DI
…[truncated 4254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Agent",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-23T10:49:07.548542+00:00_

Response matrix keys: ['indices', 'indptr', 'format', 'shape', 'data']
  indices: shape=(38654082,), dtype=int32
  indptr: shape=(5228,), dtype=int32
  format: shape=(), dtype=|S3
  shape: shape=(2,), dtype=int64
  data: shape=(38654082,), dtype=int8
Index keys: ['model_names', 'item_ids']
  model_names: shape=(5227,), dtype=object
    first 5: ['0-hero/Matter-0.1-7B' '0-hero/Matter-0.1-7B-DPO-preview'
 '0-hero/Matter-0.1-7B-boost' '0-hero/Matter-0.1-7B-boost-DPO'
 '0-hero/Matter-0.1-7B-boost-DPO-preview']
  item_ids: shape=(12508,), dtype=object
    first 5: ['abstract_algebra.1' 'abstract_algebra.10' 'abstract_algebra.100'
 'abstract_algebra.11' 'abstract_algebra.12']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Bash",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T10:49:07.548678+00:00_

model_name,family,release_year,release_half,training_method,accuracy,cohort_temporal,cohort_accuracy_quintile
0-hero/Matter-0.1-7B,unknown,unknown,unknown,unknown,0.661225,other,3
0-hero/Matter-0.1-7B-DPO-preview,,unknown,unknown,DPO,0.661337,other,3
0-hero/Matter-0.1-7B-boost,unknown,unknown,unknown,unknown,0.653422,other,3
0-hero/Matter-0.1-7B-boost-DPO,,unknown,unknown,DPO,0.654941,other,3
---
Columns: ['model_name', 'family', 'release_year', 'release_half', 'training_method', 'accuracy', 'cohort_temporal', 'cohort_accuracy_quintile']
cohort_temporal values: {'other': 3340, '2023': 1080, '2024': 807}
2023 count: 0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Bash",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T10:49:07.548861+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration",
    "description": "Create output directory"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T10:49:07.548984+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T10:49:07.549137+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_null.py",
  "content": "\"\"\"\nRandom-split null distribution of |Δ_MH| for ETS threshold calibration.\n\nSplits the 2023 cohort (N=1080) into 540 ref + 540 foc 100 times,\ncomputes MH-DIF for all 12508 items per split, and characterises\nthe null distribution of |Δ_MH|.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom pathlib import Path\nimport time, sys\n\nROOT = Path(__file__).resolve().parent.parent.parent\nART  = ROOT / \"artifacts\"\nOUT  = ART / \"r16_threshold_calibration\"\n\nN_SPLITS   = 100\nN_STRATA   = 5\nSEED       = 42\n\n# ── load data ──────────────────────────────────────────────────────\n\ndef load_data():\n    rm = np.load(ART / \"response_matrix.npz\", allow_pickle=True)\n    X = sparse.csr_matrix((rm[\"data\"], rm[\"indices\"], rm[\"indptr\"]),\n                          shape=tuple(rm[\"shape\"]))\n    idx = np.load(ART / \"response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids    = idx[\"item_ids\"]\n\n    meta = pd.read_csv(ART / \"model_metadata.csv\")\n    mask_2023 = meta[\"cohort_temporal\"].astype(str) == \"2023\"\n    models_2023 = set(meta.loc[mask_2023, \"model_name\"])\n\n    row_mask = np.array([m in models_2023 for m in model_names])\n    X_2023 = X[row_mask].toarray().astype(np.int8)\n    print(f\"2023 cohort: {X_2023.shape[0]} models × {X_2023.shape[1]} items\")\n    return X_2023, item_ids\n\n\n# ── vectorised MH-DIF (all items at once) ─────────────────────────\n\ndef mh_dif_vec(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Compute Δ_MH and p-value for every item, vectorised over items.\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc    = X_foc.shape[0]\n\n    score_ref = X_ref.sum(axis=1)\n    score_foc = X_foc.sum(axis=1)\n    all_scores = np.concatenate([score_ref, score_foc])\n\n    quantiles = np.quantile(all_scores, np.linspace(0, 1, n_strata + 1))\n    quantiles[0]  -= 1\n    quantiles[-1] += 1\n    quantiles = np.unique(quantiles)\n    K = len(quantiles) - 1\n\n    strata_ref = np.digitize(score_ref, quantiles[1:])\n    strata_foc = np.digitize(score_foc, quantiles[1:])\n\n    # accumulate per-stratum statistics — shape (K, J)\n    Rj = np.zeros(J, dtype=np.float64)\n    Sj = np.zeros(J, dtype=np.float64)\n    sum_diff = np.zeros(J, dtype=np.float64)\n    sum_var  = np.zeros(J, dtype=np.float64)\n\n    for k in range(K):\n        r_mask = strata_ref == k\n        f_mask = strata_foc == k\n        n1 = r_mask.sum()\n        n0 = f_mask.sum()\n        if n1 == 0 or n0 == 0:\n            continue\n        Nk = n1 + n0\n        if Nk <= 1:\n            continue\n\n        A = X_ref[r_mask].sum(axis=0).astype(np.float64)  # (J,)\n        C = X_foc[f_mask].sum(axis=0).astype(np.float64)\n        B = n1 - A\n        D = n0 - C\n        m1 = A + C   # total correct in stratum\n        m0 = B + D   # total incorrect in stratum\n\n        Rj += (A * D) / Nk\n        Sj += (B * C) / Nk\n\n        EA = n1 * m1 / Nk\n        sum_diff += (A - EA)\n        sum_var  += (n1 * n0 * m1 * m0) / (Nk * Nk * (Nk - 1))\n\n    valid = (Rj > 0) & (Sj > 0)\n    alpha = np.ones(J, dtype=np.float64)\n    alpha[valid] = Rj[valid] / Sj[valid]\n\n    delta = np.zeros(J, dtype=np.float64)\n    finite = np.isfinite(np.log(alpha)) & valid\n    delta[finite] = -2.35 * np.log(alpha[finite])\n\n    chi2_val = np.zeros(J, dtype=np.float64)\n    ok = sum_var > 0\n    chi2_val[ok] = (np.maximum(np.abs(sum_diff[ok]) - 0.5, 0) ** 2) / sum_var[ok]\n    pval = np.ones(J, dtype=np.float64)\n    pval[ok] = 1.0 - stats.chi2.cdf(chi2_val[ok], df=1)\n\n    return delta, pval\n\n\n# ── main loop ──────────────────────────────────────────────────────\n\ndef run():\n    X, item_ids = load_data()\n    N, J = X.shape\n    half = N // 2\n    rng = np.random.default_rng(SEED)\n\n    abs_delta_all = np.zeros((N_SPLITS, J), dtype=np.float32)\n\n    t0 = time.time()\n    for i in range(N_SPLITS):\n        perm = rng.permutation(N)\n        X_ref = X[perm[:half]]\n        X_foc = X[perm[half:2*half]]\n        delta, pval = mh_dif_vec(X_ref, X_foc, N_STRATA)\n        abs_delta_all[i] = np.abs(delta).astype(np.float32)\n\n        if (i + 1) % 10 == 0:\n            elapsed = time.time() - t0\n            eta = elapsed / (i + 1) * (N_SPLITS - i - 1)\n            print(f\"  split {i+1}/{N_SPLITS}  elapsed={elapsed:.1f}s  ETA={eta:.1f}s\")\n\n    total_time = time.time() - t0\n    print(f\"Done: {N_SPLITS} splits in {total_time:.1f}s\")\n\n    # ── summary statistics ──\n    flat = abs_delta_all.ravel()\n    pcts = [50, 90, 95, 97.5, 99, 99.5, 99.9]\n    pct_vals = np.percentile(flat, pcts)\n\n    per_item_mean = abs_delta_all.mean(axis=0)\n    per_item_p95  = np.percentile(abs_delta_all, 95, axis=0)\n    per_item_max  = abs_delta_all.max(axis=0)\n\n    # fraction of (item, split) pairs exceeding ETS thresholds\n    frac_above_1_0 = (flat >= 1.0).mean()\n    frac_above_1_5 = (flat >= 1.5).mean()\n\n    # per-item: fraction of splits where |Δ_MH| >= 1.5\n    per_item_frac_c = (abs_delta_all >= 1.5).mean(axis=0)\n    n_items_ever_c  = (per_item_frac_c > 0).sum()\n\n    # ── save summary CSV ──\n    summary = pd.DataFrame({\n        \"percentile\": pcts,\n        \"abs_delta_mh\": pct_vals\n    })\n    summary.to_csv(OUT / \"random_split_summary.csv\", index=False)\n\n    # ── save per-item stats ──\n    item_stats = pd.DataFrame({\n        \"item_id\": item_ids,\n        \"mean_abs_delta\": per_item_mean,\n        \"p95_abs_delta\": per_item_p95,\n        \"max_abs_delta\": per_item_max,\n        \"frac_splits_above_1.5\": per_item_frac_c,\n    })\n    item_stats.to_csv(OUT / \"per_item_null_stats.csv\", index=False)\n\n    # ── histogram data (for plotting later) ──\n    hist_counts, hist_edges = np.histogram(flat, bins=200, range=(0, 3.0))\n    hist_df = pd.DataFrame({\n        \"bin_left\": hist_edges[:-1],\n        \"bin_right\": hist_edges[1:],\n        \"count\": hist_counts\n    })\n    hist_df.to_csv(OUT / \"null_histogram.csv\", index=False)\n\n    # ── report ──\n    report_lines = [\n        \"# Random-Split |Δ_MH| Null Distribution Report\",\n        \"\",\n        \"## Setup\",\n        f\"- Cohort: 2023 models (N = {N})\",\n        f\"- Items: J = {J}\",\n        f\"- Splits: {N_SPLITS} random permutations (each {half} ref vs {half} foc)\",\n        f\"- Strata: {N_STRATA} total-score quantile bins\",\n        f\"- Total (item × split) observations: {N_SPLITS * J:,}\",\n        f\"- Runtime: {total_time:.1f}s\",\n        \"\",\n        \"## Null Distribution Percentiles\",\n        \"\",\n        \"| Percentile | |Δ_MH| |\",\n        \"|------------|--------|\",\n    ]\n    for p, v in zip(pcts, pct_vals):\n        report_lines.append(f\"| {p}th | {v:.4f} |\")\n\n    report_lines += [\n        \"\",\n        \"## ETS Threshold Comparison\",\n        \"\",\n        f\"- Fraction of (item, split) with |Δ_MH| ≥ 1.0 (B threshold): {frac_above_1_0:.6f} ({frac_above_1_0*100:.4f}%)\",\n        f\"- Fraction of (item, split) with |Δ_MH| ≥ 1.5 (C threshold): {frac_above_1_5:.6f} ({frac_above_1_5*100:.4f}%)\",\n        f\"- Items that exceed |Δ_MH| ≥ 1.5 in at least one split: {n_items_ever_c} / {J} ({n_items_ever_c/J*100:.2f}%)\",\n        \"\",\n        \"## Interpretation\",\n        \"\",\n    ]\n\n    if pct_vals[pcts.index(95)] < 0.5:\n        report_lines.append(\n            f\"The 95th percentile of the null distribution is {pct_vals[pcts.index(95)]:.4f}, \"\n            f\"far below the ETS C-level threshold of 1.5. \"\n            f\"This confirms that the ETS 1.5 threshold is extremely conservative \"\n            f\"for LLM benchmark evaluation: under random splitting, virtually no items \"\n            f\"would be falsely flagged as showing large DIF.\"\n        )\n    elif pct_vals[pcts.index(95)] < 1.0:\n        report_lines.append(\n            f\"The 95th percentile is {pct_vals[pcts.index(95)]:.4f}, \"\n            f\"well below 1.5 but approaching the B-level threshold (1.0). \"\n            f\"The ETS C threshold remains conservative but the B threshold may be marginal.\"\n        )\n    else:\n        report_lines.append(\n            f\"The 95th percentile is {pct_vals[pcts.index(95)]:.4f}, \"\n            f\"approaching or exceeding the ETS thresholds. \"\n            f\"This suggests the ETS thresholds may be too liberal for LLM evaluation.\"\n        )\n\n    report_lines += [\n        \"\",\n        f\"The 99th percentile ({pct_vals[pcts.index(99)]:.4f}) and \"\n        f\"99.9th percentile ({pct_vals[pcts.index(99.9)]:.4f}) \"\n        f\"provide upper bounds on chance-level |Δ_MH| fluctuations.\",\n        \"\",\n        \"## Distribution Shape\",\n        \"\",\n        f\"- Mean |Δ_MH| across all observations: {flat.mean():.4f}\",\n        f\"- Median |Δ_MH|: {np.median(flat):.4f}\",\n        f\"- Std dev: {flat.std():.4f}\",\n        f\"- Skewness: {stats.skew(flat):.4f}\",\n        f\"- Max observed: {flat.max():.4f}\",\n        \"\",\n        \"The null distribution is right-skewed with most mass concentrated near zero, \"\n        \"consistent with well-behaved random assignment where group differences \"\n        \"are due purely to sampling variability.\",\n    ]\n\n    report_text = \"\\n\".join(report_lines) + \"\\n\"\n    (OUT / \"random_split_report.md\").write_text(report_text)\n    print(\"\\n\" + report_text)\n\n\nif __name__ == \"__main__\":\n    run()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_null.py",
    "content": "\"\"\"\nRandom-split null distribution of |Δ_MH| for ETS threshold calibration.\n\nSplits the 2023 cohort (N=1080) into 540 ref + 540 foc 100 times,\ncomputes MH-DIF for all 12508 items per split, and characterises\nthe null distribution of |Δ_MH|.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom pathlib import Path\nimport time, sys\n\nROOT = Path(__file__).resolve().parent.parent.parent\nART  = ROOT / \"artifacts\"\nOUT  = ART / \"r16_threshold_calibration\"\n\nN_SPLITS   = 100\nN_STRATA   = 5\nSEED       = 42\n\n# ── load data ──────────────────────────────────────────────────────\n\ndef load_data():\n    rm = np.load(ART / \"response_matrix.npz\", allow_pickle=True)\n    X = sparse.csr_matrix((rm[\"data\"], rm[\"indices\"], rm[\"indptr\"]),\n                          shape=tuple(rm[\"shape\"]))\n    idx = np.load(ART / \"response_matrix_index.npz\", allow_pickle=True)\n    model_names = idx[\"model_names\"]\n    item_ids    = idx[\"item_ids\"]\n\n    meta = pd.read_csv(ART / \"model_metadata.csv\")\n    mask_2023 = meta[\"cohort_temporal\"].astype(str) == \"2023\"\n    models_2023 = set(meta.loc[mask_2023, \"model_name\"])\n\n    row_mask = np.array([m in models_2023 for m in model_names])\n    X_2023 = X[row_mask].toarray().astype(np.int8)\n    print(f\"2023 cohort: {X_2023.shape[0]} models × {X_2023.shape[1]} items\")\n    return X_2023, item_ids\n\n\n# ── vectorised MH-DIF (all items at once) ─────────────────────────\n\ndef mh_dif_vec(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Compute Δ_MH and p-value for every item, vectorised over items.\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc    = X_foc.shape[0]\n\n    score_ref = X_ref.sum(axis=1)\n    score_foc = X_foc.sum(axis=1)\n    all_scores = np.concatenate([score_ref, score_foc])\n\n    quantiles = np.quantile(all_scores, np.linspace(0, 1, n_strata + 1))\n    quantiles[0]  -= 1\n    quantiles[-1] += 1\n    quantiles = np.unique(quantiles)\n    K = len(quantiles) - 1\n\n    strata_ref = np.digitize(score_ref, quantiles[1:])\n    strata_foc = np.digitize(score_foc, quantiles[1:])\n\n    # accumulate per-stratum statistics — shape (K, J)\n    Rj = np.zeros(J, dtype=np.float64)\n    Sj = np.zeros(J, dtype=np.float64)\n    sum_diff = np.zeros(J, dtype=np.float64)\n    sum_var  = np.zeros(J, dtype=np.float64)\n\n    for k in range(K):\n        r_mask = strata_ref == k\n        f_mask = strata_foc == k\n        n1 = r_mask.sum()\n        n0 = f_mask.sum()\n        if n1 == 0 or n0 == 0:\n            continue\n        Nk = n1 + n0\n        if Nk <= 1:\n            continue\n\n        A = X_ref[r_mask].sum(axis=0).astype(np.float64)  # (J,)\n        C = X_foc[f_mask].sum(axis=0).astype(np.float64)\n        B = n1 - A\n        D = n0 - C\n        m1 = A + C   # total correct in stratum\n        m0 = B + D   # total incorrect in stratum\n\n        Rj += (A * D) / Nk\n        Sj += (B * C) / Nk\n\n        EA = n1 * m1 / Nk\n        sum_diff += (A - EA)\n        sum_var  += (n1 * n0 * m1 * m0) / (Nk * Nk * (Nk - 1))\n\n    valid = (Rj > 0) & (Sj > 0)\n    alpha = np.ones(J, dtype=np.float64)\n    alpha[valid] = Rj[valid] / Sj[valid]\n\n    delta = np.zeros(J, dtype=np.float64)\n    finite = np.isfinite(np.log(alpha)) & valid\n    delta[finite] = -2.35 * np.log(alpha[finite])\n\n    chi2_val = np.zeros(J, dtype=np.float64)\n    ok = sum_var > 0\n    chi2_val[ok] = (np.maximum(np.abs(sum_diff[ok]) - 0.5, 0) ** 2) / sum_var[ok]\n    pval = np.ones(J, dtype=np.float64)\n    pval[ok] = 1.0 - stats.chi2.cdf(chi2_val[ok], df=1)\n\n    return delta, pval\n\n\n# ── main loop ──────────────────────────────────────────────────────\n\ndef run():\n    X, item_ids = load_data()\n    N, J = X.shape\n    half = N // 2\n    rng = np.random.default_rng(SEED)\n\n    abs_delta_all = np.zeros((N_SPLITS, J), dtype=np.float32)\n\n    t0 = time.time()\n    for i in range(N_SPLITS):\n        perm = rng.permutation(N)\n        X_ref = X[perm[:half]]\n        X_foc = X[perm[half:2*half]]\n        delta, pval = mh_dif_vec(X_ref, X_foc, N_STRATA)\n        abs_delta_all[i] = np.abs(delta).astype(np.float32)\n\n        if (i + 1) % 10 == 0:\n            elapsed = time.time() - t0\n            eta = elapsed / (i + 1) * (N_SPLITS - i - 1)\n            print(f\"  split {i+1}/{N_SPLITS}  elapsed={elapsed:.1f}s  ETA={eta:.1f}s\")\n\n    total_time = time.time() - t0\n    print(f\"Done: {N_SPLITS} splits in {total_time:.1f}s\")\n\n    # ── summary statistics ──\n    flat = abs_delta_all.ravel()\n    pcts = [50, 90, 95, 97.5, 99, 99.5, 99.9]\n    pct_vals = np.percentile(flat, pcts)\n\n    per_item_mean = abs_delta_all.mean(axis=0)\n    per_item_p95  = np.percentile(abs_delta_all, 95, axis=0)\n    per_item_max  = abs_delta_all.max(axis=0)\n\n    # fraction of (item, split) pairs exceeding ETS thresholds\n    frac_above_1_0 = (flat >= 1.0).mean()\n    frac_above_1_5 = (flat >= 1.5).mean()\n\n    # per-item: fraction of splits where |Δ_MH| >= 1.5\n    per_item_frac_c = (abs_delta_all >= 1.5).mean(axis=0)\n    n_items_ever_c  = (per_item_frac_c > 0).sum()\n\n    # ── save summary CSV ──\n    summary = pd.DataFrame({\n        \"percentile\": pcts,\n        \"abs_delta_mh\": pct_vals\n    })\n    summary.to_csv(OUT / \"random_split_summary.csv\", index=False)\n\n    # ── save per-item stats ──\n    item_stats = pd.DataFrame({\n        \"item_id\": item_ids,\n        \"mean_abs_delta\": per_item_mean,\n        \"p95_abs_delta\": per_item_p95,\n        \"max_abs_delta\": per_item_max,\n        \"frac_splits_above_1.5\": per_item_frac_c,\n    })\n    item_stats.to_csv(OUT / \"per_item_null_stats.csv\", index=False)\n\n    # ── histogram data (for plotting later) ──\n    hist_counts, hist_edges = np.histogram(flat, bins=200, range=(0, 3.0))\n    hist_df = pd.DataFrame({\n        \"bin_left\": hist_edges[:-1],\n        \"bin_right\": hist_edges[1:],\n        \"count\": hist_counts\n    })\n    hist_df.to_csv(OUT / \"null_histogram.csv\", index=False)\n\n    # ── report ──\n    report_lines = [\n        \"# Random-Split |Δ_MH| Null Distribution Report\",\n        \"\",\n        \"## Setup\",\n        f\"- Cohort: 2023 models (N = {N})\",\n        f\"- Items: J = {J}\",\n        f\"- Splits: {N_SPLITS} random permutations (each {half} ref vs {half} foc)\",\n        f\"- Strata: {N_STRATA} total-score quantile bins\",\n        f\"- Total (item × split) observations: {N_SPLITS * J:,}\",\n        f\"- Runtime: {total_time:.1f}s\",\n        \"\",\n        \"## Null Distribution Percentiles\",\n        \"\",\n        \"| Percentile | |Δ_MH| |\",\n        \"|------------|--------|\",\n    ]\n    for p, v in zip(pcts, pct_vals):\n        report_lines.append(f\"| {p}th | {v:.4f} |\")\n\n    report_lines += [\n        \"\",\n        \"## ETS Threshold Comparison\",\n        \"\",\n        f\"- Fraction of (item, split) with |Δ_MH| ≥ 1.0 (B threshold): {frac_above_1_0:.6f} ({frac_above_1_0*100:.4f}%)\",\n        f\"- Fraction of (item, split) with |Δ_MH| ≥ 1.5 (C threshold): {frac_above_1_5:.6f} ({frac_above_1_5*100:.4f}%)\",\n        f\"- Items that exceed |Δ_MH| ≥ 1.5 in at least one split: {n_items_ever_c} / {J} ({n_items_ever_c/J*100:.2f}%)\",\n        \"\",\n        \"## Interpretation\",\n        \"\",\n    ]\n\n    if pct_vals[pcts.index(95)] < 0.5:\n        report_lines.append(\n            f\"The 95th percentile of the null distribution is {pct_vals[pcts.index(95)]:.4f}, \"\n            f\"far below the ETS C-level threshold of 1.5. \"\n            f\"This confirms that the ETS 1.5 threshold is extremely conservative \"\n            f\"for LLM benchmark evaluation: under random splitting, virtually no items \"\n            f\"would be falsely flagged as showing large DIF.\"\n        )\n    elif pct_vals[pcts.index(95)] < 1.0:\n        report_lines.append(\n            f\"The 95th percentile is {pct_vals[pcts.index(95)]:.4f}, \"\n            f\"well below 1.5 but approaching the B-level threshold (1.0). \"\n            f\"The ETS C threshold remains conservative but the B threshold may be marginal.\"\n        )\n    else:\n        report_lines.append(\n            f\"The 95th percentile is {pct_vals[pcts.index(95)]:.4f}, \"\n            f\"approaching or exceeding the ETS thresholds. \"\n            f\"This suggests the ETS thresholds may be too liberal for LLM evaluation.\"\n        )\n\n    report_lines += [\n        \"\",\n        f\"The 99th percentile ({pct_vals[pcts.index(99)]:.4f}) and \"\n        f\"99.9th percentile ({pct_vals[pcts.index(99.9)]:.4f}) \"\n        f\"provide upper bounds on chance-level |Δ_MH| fluctuations.\",\n        \"\",\n        \"## Distribution Shape\",\n        \"\",\n        f\"- Mean |Δ_MH| across all observations: {flat.mean():.4f}\",\n        f\"- Median |Δ_MH|: {np.median(flat):.4f}\",\n        f\"- Std dev: {flat.std():.4f}\",\n        f\"- Skewness: {stats.skew(flat):.4f}\",\n        f\"- Max observed: {flat.max():.4f}\",\n        \"\",\n        \"The null distribution is right-skewed with most mass concentrated near zero, \"\n        \"consistent with well-behaved random assignment where group differences \"\n        \"are due purely to sampling variability.\",\n    ]\n\n    report_text = \"\\n\".join(report_lines) + \"\\n\"\n    (OUT / \"random_split_report.md\").write_text(report_text)\n    print(\"\\n\" + report_text)\n\n\nif __name__ == \"__main__\":\n    run()\n"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T10:49:07.549428+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_null.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T10:49:07.549591+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport numpy as np\nfrom scipy import sparse, stats\nimport pandas as pd, time\n\nART = 'artifacts'\nrm = np.load(f'{ART}/response_matrix.npz', allow_pickle=True)\nX = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nidx = np.load(f'{ART}/response_matrix_index.npz', allow_pickle=True)\nmodel_names = idx['model_names']\n\nmeta = pd.read_csv(f'{ART}/model_metadata.csv')\nmask_2023 = meta['cohort_temporal'].astype(str) == '2023'\nmodels_2023 = set(meta.loc[mask_2023, 'model_name'])\nrow_mask = np.array([m in models_2023 for m in model_names])\nX_2023 = X[row_mask].toarray().astype(np.int8)\nprint(f'Shape: {X_2023.shape}')\n\nN, J = X_2023.shape\nhalf = N // 2\nrng = np.random.default_rng(42)\n\nt0 = time.time()\nfor i in range(5):\n    perm = rng.permutation(N)\n    X_ref = X_2023[perm[:half]]\n    X_foc = X_2023[perm[half:2*half]]\n\n    score_ref = X_ref.sum(axis=1)\n    score_foc = X_foc.sum(axis=1)\n    all_scores = np.concatenate([score_ref, score_foc])\n    quantiles = np.quantile(all_scores, np.linspace(0, 1, 6))\n    quantiles[0] -= 1; quantiles[-1] += 1\n    quantiles = np.unique(quantiles)\n    K = len(quantiles) - 1\n    strata_ref = np.digitize(score_ref, quantiles[1:])\n    strata_foc = np.digitize(score_foc, quantiles[1:])\n\n    Rj = np.zeros(J, dtype=np.float64)\n    Sj = np.zeros(J, dtype=np.float64)\n    for k in range(K):\n        r_mask = strata_ref == k\n        f_mask = strata_foc == k\n        n1 = r_mask.sum(); n0 = f_mask.sum()\n        if n1 == 0 or n0 == 0: continue\n        Nk = n1 + n0\n        if Nk <= 1: continue\n        A = X_ref[r_mask].sum(axis=0).astype(np.float64)\n        C = X_foc[f_mask].sum(axis=0).astype(np.float64)\n        B = n1 - A; D = n0 - C\n        Rj += (A * D) / Nk\n        Sj += (B * C) / Nk\n\n    elapsed = time.time() - t0\n    print(f'  split {i+1}: cumulative {elapsed:.2f}s')\n\nper_split = elapsed / 5\nprint(f'Per split: {per_split:.2f}s')\nprint(f'Estimated 100 splits: {per_split * 100:.1f}s')\n\"\n",
  "description": "Benchmark 5 splits to estimate total runtime",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport numpy as np\nfrom scipy import sparse, stats\nimport pandas as pd, time\n\nART = 'artifacts'\nrm = np.load(f'{ART}/response_matrix.npz', allow_pickle=True)\nX = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nidx = np.load(f'{ART}/response_matrix_index.npz', allow_pickle=True)\nmodel_names = idx['model_names']\n\nmeta = pd.read_csv(f'{ART}/model_metadata.csv')\nmask_2023 = meta['cohort_temporal'].astype(str) == '2023'\nmodels_2023 = set(meta.loc[mask_2023, 'model_name'])\nrow_mask = np.array([m in models_2023 for m in model_names])\nX_2023 = X[row_mask].toarray().astype(np.int8)\nprint(f'Shape: {X_2023.shape}')\n\nN, J = X_2023.shape\nhalf = N // 2\nrng = np.random.default_rng(42)\n\nt0 = time.time()\nfor i in range(5):\n    perm = rng.permutation(N)\n    X_ref = X_2023[perm[:half]]\n    X_foc = X_2023[perm[half:2*half]]\n\n    score_ref = X_ref.sum(axis=1)\n    score_foc = X_foc.sum(axis=1)\n    all_scores = np.concatenate([score_ref, score_foc])\n    quantiles = np.quantile(all_scores, np.linspace(0, 1, 6))\n    quantiles[0] -= 1; quantiles[-1] += 1\n    quantiles = np.unique(quantiles)\n    K = len(quantiles) - 1\n    strata_ref = np.digitize(score_ref, quantiles[1:])\n    strata_foc = np.digitize(score_foc, quantiles[1:])\n\n    Rj = np.zeros(J, dtype=np.float64)\n    Sj = np.zeros(J, dtype=np.float64)\n    for k in range(K):\n        r_mask = strata_ref == k\n        f_mask = strata_foc == k\n        n1 = r_mask.sum(); n0 = f_mask.sum()\n        if n1 == 0 or n0 == 0: continue\n        Nk = n1 + n0\n        if Nk <= 1: continue\n        A = X_ref[r_mask].sum(axis=0).astype(np.float64)\n        C = X_foc[f_mask].sum(axis=0).astype(np.float64)\n        B = n1 - A; D = n0 - C\n        Rj += (A * D) / Nk\n        Sj += (B * C) / Nk\n\n    elapsed = time.time() - t0\n    print(f'  split {i+1}: cumulative {elapsed:.2f}s')\n\nper_split = elapsed / 5\nprint(f'Per split: {per_split:.2f}s')\nprint(f'Estimated 100 splits: {per_split * 100:.1f}s')\n\"\n",
    "description": "Benchmark 5 splits to estimate total runtime",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T10:49:07.549758+00:00_

Shape: (1080, 12508)
  split 1: cumulative 0.03s
  split 2: cumulative 0.05s
  split 3: cumulative 0.07s
  split 4: cumulative 0.10s
  split 5: cumulative 0.12s
Per split: 0.02s
Estimated 100 splits: 2.3s

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T10:49:07.549914+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 artifacts/r16_threshold_calibration/random_split_null.py",
  "description": "Run full 100-split null distribution analysis",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 artifacts/r16_threshold_calibration/random_split_null.py",
    "description": "Run full 100-split null distribution analysis",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T10:49:07.550068+00:00_

2023 cohort: 1080 models × 12508 items
  split 10/100  elapsed=0.3s  ETA=2.5s
  split 20/100  elapsed=0.5s  ETA=2.1s
  split 30/100  elapsed=0.8s  ETA=1.8s
  split 40/100  elapsed=1.0s  ETA=1.5s
  split 50/100  elapsed=1.3s  ETA=1.3s
  split 60/100  elapsed=1.5s  ETA=1.0s
  split 70/100  elapsed=1.8s  ETA=0.8s
  split 80/100  elapsed=2.0s  ETA=0.5s
  split 90/100  elapsed=2.3s  ETA=0.3s
  split 100/100  elapsed=2.5s  ETA=0.0s
Done: 100 splits in 2.5s

# Random-Split |Δ_MH| Null Distribution Report

## Setup
- Cohort: 2023 models (N = 1080)
- Items: J = 12508
- Splits: 100 random permutations (each 540 ref vs 540 foc)
- Strata: 5 total-score quantile bins
- Total (item × split) observations: 1,250,800
- Runtime: 2.5s

## Null Distribution Percentiles

| Percentile | |Δ_MH| |
|------------|--------|
| 50th | 0.2956 |
| 90th | 0.7911 |
| 95th | 0.9898 |
| 97.5th | 1.1874 |
| 99th | 1.4504 |
| 99.5th | 1.6536 |
| 99.9th | 2.1998 |

## ETS Threshold Comparison

- Fraction of (item, split) with |Δ_MH| ≥ 1.0 (B threshold): 0.048206 (4.8206%)
- Fraction of (item, split) with |Δ_MH| ≥ 1.5 (C threshold): 0.008480 (0.8480%)
- Items that exceed |Δ_MH| ≥ 1.5 in at least one split: 3717 / 12508 (29.72%)

## Interpretation

The 95th percentile is 0.9898, well below 1.5 but approaching the B-level threshold (1.0). The ETS C threshold remains conservative but the B threshold may be marginal.

The 99th percentile (1.4504) and 99.9th percentile (2.1998) provide upper bounds on chance-level |Δ_MH| fluctuations.

## Distribution Shape

- Mean |Δ_MH| across all observations: 0.3740
- Median |Δ_MH|: 0.2956
- Std dev: 0.3205
- Skewness: 1.7897
- Max observed: 6.2475

The null distribution is right-skewed with most mass concentrated near zero, consistent with well-behaved random assignment where group differences are due purely to sampling variability.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T10:49:07.550256+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la artifacts/r16_threshold_calibration/ && echo \"---\" && cat artifacts/r16_threshold_calibration/random_split_summary.csv",
  "description": "Verify output files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la artifacts/r16_threshold_calibration/ && echo \"---\" && cat artifacts/r16_threshold_calibration/random_split_summary.csv",
    "description": "Verify output files"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-23T10:49:07.550431+00:00_

total 740
drwxr-xr-x   2 ubuntu ubuntu   4096 May 23 10:47 .
drwxr-xr-x 105 ubuntu ubuntu  12288 May 23 10:45 ..
-rw-r--r--   1 ubuntu ubuntu   3055 May 23 10:47 null_histogram.csv
-rw-r--r--   1 ubuntu ubuntu 714221 May 23 10:47 per_item_null_stats.csv
-rw-r--r--   1 ubuntu ubuntu   9317 May 23 10:46 random_split_null.py
-rw-r--r--   1 ubuntu ubuntu   1419 May 23 10:47 random_split_report.md
-rw-r--r--   1 ubuntu ubuntu    192 May 23 10:47 random_split_summary.csv
---
percentile,abs_delta_mh
50.0,0.29556451737880707
90.0,0.7910759568214418
95.0,0.9898163795471193
97.5,1.1874477803707113
99.0,1.4503863203525544
99.5,1.6536056780815103
99.9,2.199819326400757

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-23T10:49:07.550596+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_null.py",
  "offset": "110",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_null.py",
    "offset": "110",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-23T10:49:07.550779+00:00_

110	
111	# ── main loop ──────────────────────────────────────────────────────
112	
113	def run():
114	    X, item_ids = load_data()
115	    N, J = X.shape
116	    half = N // 2
117	    rng = np.random.default_rng(SEED)
118	
119	    abs_delta_all = np.zeros((N_SPLITS, J), dtype=np.float32)
120	
121	    t0 = time.time()
122	    for i in range(N_SPLITS):
123	        perm = rng.permutation(N)
124	        X_ref = X[perm[:half]]
125	        X_foc = X[perm[half:2*half]]
126	        delta, pval = mh_dif_vec(X_ref, X_foc, N_STRATA)
127	        abs_delta_all[i] = np.abs(delta).astype(np.float32)
128	
129	        if (i + 1) % 10 == 0:
130	            elapsed = time.time() - t0
131	            eta = elapsed / (i + 1) * (N_SPLITS - i - 1)
132	            print(f"  split {i+1}/{N_SPLITS}  elapsed={elapsed:.1f}s  ETA={eta:.1f}s")
133	
134	    total_time = time.time() - t0
135	    print(f"Done: {N_SPLITS} splits in {total_time:.1f}s")
136	
137	    # ── summary statistics ──
138	    flat = abs_delta_all.ravel()
139	    pcts = [50, 90, 95, 97.5, 99, 99.5, 99.9]
140	    pct_vals = np.percentile(flat, pcts)
141	
142	    per_item_mean = abs_delta_all.mean(axis=0)
143	    per_item_p95  = np.percentile(abs_delta_all, 95, axis=0)
144	    per_item_max  = abs_delta_all.max(axis=0)
145	
146	    # fraction of (item, split) pairs exceeding ETS thresholds
147	    frac_above_1_0 = (flat >= 1.0).mean()
148	    frac_above_1_5 = (flat >= 1.5).mean()
149	
150	    # per-item: fraction of splits where |Δ_MH| >= 1.5
151	    per_item_frac_c = (abs_delta_all >= 1.5).mean(axis=0)
152	    n_items_ever_c  = (per_item_frac_c > 0).sum()
153	
154	    # ── save summary CSV ──
155	    summary = pd.DataFrame({
156	        "percentile": pcts,
157	        "abs_delta_mh": pct_vals
158	    })
159	    summary.to_csv(OUT / "random_split_summary.csv", index=False)
160	
161	    # ── save per-item stats ──
162	    item_stats = pd.DataFrame({
163	        "item_id": item_ids,
164	        "mean_abs_delta": per_item_mean,
165
…[truncated 219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-23T10:49:07.550971+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_null.py",
  "old_string": "    abs_delta_all = np.zeros((N_SPLITS, J), dtype=np.float32)\n\n    t0 = time.time()\n    for i in range(N_SPLITS):\n        perm = rng.permutation(N)\n        X_ref = X[perm[:half]]\n        X_foc = X[perm[half:2*half]]\n        delta, pval = mh_dif_vec(X_ref, X_foc, N_STRATA)\n        abs_delta_all[i] = np.abs(delta).astype(np.float32)",
  "new_string": "    abs_delta_all = np.zeros((N_SPLITS, J), dtype=np.float32)\n    is_c_all      = np.zeros((N_SPLITS, J), dtype=bool)\n\n    t0 = time.time()\n    for i in range(N_SPLITS):\n        perm = rng.permutation(N)\n        X_ref = X[perm[:half]]\n        X_foc = X[perm[half:2*half]]\n        delta, pval = mh_dif_vec(X_ref, X_foc, N_STRATA)\n        ad = np.abs(delta)\n        abs_delta_all[i] = ad.astype(np.float32)\n        is_c_all[i] = (ad >= 1.5) & (pval < 0.05)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_null.py",
    "old_string": "    abs_delta_all = np.zeros((N_SPLITS, J), dtype=np.float32)\n\n    t0 = time.time()\n    for i in range(N_SPLITS):\n        perm = rng.permutation(N)\n        X_ref = X[perm[:half]]\n        X_foc = X[perm[half:2*half]]\n        delta, pval = mh_dif_vec(X_ref, X_foc, N_STRATA)\n        abs_delta_all[i] = np.abs(delta).astype(np.float32)",
    "new_string": "    abs_delta_all = np.zeros((N_SPLITS, J), dtype=np.float32)\n    is_c_all      = np.zeros((N_SPLITS, J), dtype=bool)\n\n    t0 = time.time()\n    for i in range(N_SPLITS):\n        perm = rng.permutation(N)\n        X_ref = X[perm[:half]]\n        X_foc = X[perm[half:2*half]]\n        delta, pval = mh_dif_vec(X_ref, X_foc, N_STRATA)\n        ad = np.abs(delta)\n        abs_delta_all[i] = ad.astype(np.float32)\n        is_c_all[i] = (ad >= 1.5) & (pval < 0.05)"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-23T10:49:07.551157+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_null.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-23T10:49:07.551292+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_null.py",
  "old_string": "    # per-item: fraction of splits where |Δ_MH| >= 1.5\n    per_item_frac_c = (abs_delta_all >= 1.5).mean(axis=0)\n    n_items_ever_c  = (per_item_frac_c > 0).sum()",
  "new_string": "    # per-item: fraction of splits where |Δ_MH| >= 1.5\n    per_item_frac_c = (abs_delta_all >= 1.5).mean(axis=0)\n    n_items_ever_c  = (per_item_frac_c > 0).sum()\n\n    # ETS C classification: |Δ_MH| >= 1.5 AND p < 0.05\n    c_rate_per_split = is_c_all.mean(axis=1)  # C% per split\n    mean_c_pct = c_rate_per_split.mean() * 100\n    frac_c_joint = is_c_all.mean()\n    per_item_frac_c_joint = is_c_all.mean(axis=0)\n    n_items_ever_c_joint  = (per_item_frac_c_joint > 0).sum()"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_null.py",
    "old_string": "    # per-item: fraction of splits where |Δ_MH| >= 1.5\n    per_item_frac_c = (abs_delta_all >= 1.5).mean(axis=0)\n    n_items_ever_c  = (per_item_frac_c > 0).sum()",
    "new_string": "    # per-item: fraction of splits where |Δ_MH| >= 1.5\n    per_item_frac_c = (abs_delta_all >= 1.5).mean(axis=0)\n    n_items_ever_c  = (per_item_frac_c > 0).sum()\n\n    # ETS C classification: |Δ_MH| >= 1.5 AND p < 0.05\n    c_rate_per_split = is_c_all.mean(axis=1)  # C% per split\n    mean_c_pct = c_rate_per_split.mean() * 100\n    frac_c_joint = is_c_all.mean()\n    per_item_frac_c_joint = is_c_all.mean(axis=0)\n    n_items_ever_c_joint  = (per_item_frac_c_joint > 0).sum()"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-23T10:49:07.551466+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_null.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-23T10:49:07.551618+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_null.py",
  "old_string": "        f\"- Items that exceed |Δ_MH| ≥ 1.5 in at least one split: {n_items_ever_c} / {J} ({n_items_ever_c/J*100:.2f}%)\",\n        \"\",\n        \"## Interpretation\",",
  "new_string": "        f\"- Items that exceed |Δ_MH| ≥ 1.5 in at least one split: {n_items_ever_c} / {J} ({n_items_ever_c/J*100:.2f}%)\",\n        \"\",\n        \"### ETS C Classification (joint criterion: |Δ_MH| ≥ 1.5 AND p < 0.05)\",\n        \"\",\n        f\"- Mean null C% per split: {mean_c_pct:.4f}%\",\n        f\"- C% range across splits: [{c_rate_per_split.min()*100:.4f}%, {c_rate_per_split.max()*100:.4f}%]\",\n        f\"- Fraction of (item, split) classified C: {frac_c_joint:.6f} ({frac_c_joint*100:.4f}%)\",\n        f\"- Items classified C in at least one split: {n_items_ever_c_joint} / {J} ({n_items_ever_c_joint/J*100:.2f}%)\",\n        \"\",\n        \"## Interpretation\","
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_null.py",
    "old_string": "        f\"- Items that exceed |Δ_MH| ≥ 1.5 in at least one split: {n_items_ever_c} / {J} ({n_items_ever_c/J*100:.2f}%)\",\n        \"\",\n        \"## Interpretation\",",
    "new_string": "        f\"- Items that exceed |Δ_MH| ≥ 1.5 in at least one split: {n_items_ever_c} / {J} ({n_items_ever_c/J*100:.2f}%)\",\n        \"\",\n        \"### ETS C Classification (joint criterion: |Δ_MH| ≥ 1.5 AND p < 0.05)\",\n        \"\",\n        f\"- Mean null C% per split: {mean_c_pct:.4f}%\",\n        f\"- C% range across splits: [{c_rate_per_split.min()*100:.4f}%, {c_rate_per_split.max()*100:.4f}%]\",\n        f\"- Fraction of (item, split) classified C: {frac_c_joint:.6f} ({frac_c_joint*100:.4f}%)\",\n        f\"- Items classified C in at least one split: {n_items_ever_c_joint} / {J} ({n_items_ever_c_joint/J*100:.2f}%)\",\n        \"\",\n        \"## Interpretation\","
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-23T10:49:07.551823+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_null.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-23T10:49:07.551980+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_null.py",
  "old_string": "    if pct_vals[pcts.index(95)] < 0.5:\n        report_lines.append(\n            f\"The 95th percentile of the null distribution is {pct_vals[pcts.index(95)]:.4f}, \"\n            f\"far below the ETS C-level threshold of 1.5. \"\n            f\"This confirms that the ETS 1.5 threshold is extremely conservative \"\n            f\"for LLM benchmark evaluation: under random splitting, virtually no items \"\n            f\"would be falsely flagged as showing large DIF.\"\n        )\n    elif pct_vals[pcts.index(95)] < 1.0:\n        report_lines.append(\n            f\"The 95th percentile is {pct_vals[pcts.index(95)]:.4f}, \"\n            f\"well below 1.5 but approaching the B-level threshold (1.0). \"\n            f\"The ETS C threshold remains conservative but the B threshold may be marginal.\"\n        )\n    else:\n        report_lines.append(\n            f\"The 95th percentile is {pct_vals[pcts.index(95)]:.4f}, \"\n            f\"approaching or exceeding the ETS thresholds. \"\n            f\"This suggests the ETS thresholds may be too liberal for LLM evaluation.\"\n        )",
  "new_string": "    p95 = pct_vals[pcts.index(95)]\n    p99 = pct_vals[pcts.index(99)]\n    report_lines.append(\n        f\"**P95 = {p95:.4f}** (vs ETS B = 1.0): under random splitting, ~5% of \"\n        f\"item-level |Δ_MH| values approach B-level magnitude purely by chance.\"\n    )\n    report_lines.append(\"\")\n    report_lines.append(\n        f\"**P99 = {p99:.4f}** (vs ETS C = 1.5): the null 99th percentile nearly reaches \"\n        f\"the C threshold, meaning ~1% of items can show |Δ_MH| ≥ 1.45 by sampling noise alone.\"\n    )\n    report_lines.append(\"\")\n    report_lines.append(\n        f\"**Null C% = {mean_c_pct:.4f}%** (joint criterion: |Δ_MH| ≥ 1.5 AND p < 0.05). \"\n        f\"The observed temporal C% is ~0.18% (2023→2024 within-year) and ~1.3% (2023 vs 2024 \"\n        f\"cross-year). The null C% provides the baseline false-positive rate for interpreting \"\n        f\"these observed rates.\"\n    )"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_null.py",
    "old_string": "    if pct_vals[pcts.index(95)] < 0.5:\n        report_lines.append(\n            f\"The 95th percentile of the null distribution is {pct_vals[pcts.index(95)]:.4f}, \"\n            f\"far below the ETS C-level threshold of 1.5. \"\n            f\"This confirms that the ETS 1.5 threshold is extremely conservative \"\n            f\"for LLM benchmark evaluation: under random splitting, virtually no items \"\n            f\"would be falsely flagged as showing large DIF.\"\n        )\n    elif pct_vals[pcts.index(95)] < 1.0:\n        report_lines.append(\n            f\"The 95th percentile is {pct_vals[pcts.index(95)]:.4f}, \"\n            f\"well below 1.5 but approaching the B-level threshold (1.0). \"\n            f\"The ETS C threshold remains conservative but the B threshold may be marginal.\"\n        )\n    else:\n        report_lines.append(\n            f\"The 95th percentile is {pct_vals[pcts.index(95)]:.4f}, \"\n            f\"approaching or exceeding the ETS thresholds. \"\n            f\"This suggests the ETS thresholds may be too liberal for LLM evaluation.\"\n        )",
    "new_string": "    p95 = pct_vals[pcts.index(95)]\n    p99 = pct_vals[pcts.index(99)]\n    report_lines.append(\n        f\"**P95 = {p95:.4f}** (vs ETS B = 1.0): under random splitting, ~5% of \"\n        f\"item-level |Δ_MH| values approach B-level magnitude purely by chance.\"\n    )\n    report_lines.append(\"\")\n    report_lines.append(\n        f\"**P99 = {p99:.4f}** (vs ETS C = 1.5): the null 99th percentile nearly reaches \"\n        f\"the C threshold, meaning ~1% of items can show |Δ_MH| ≥ 1.45 by sampling noise alone.\"\n    )\n    report_lines.append(\"\")\n    report_lines.append(\n        f\"**Null C% = {mean_c_pct:.4f}%** (joint criterion: |Δ_MH| ≥ 1.5 AND p < 0.05). \"\n        f\"The observed temporal C% is ~0.18% (2023→2024 within-year) and ~1.3% (2023 vs 2024 \"\n        f\"cross-year). The null C% provides the baseline false-positive rate for interpreting \"\n        f\"these observed rates.\"\n    )"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-23T10:49:07.552208+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r16_threshold_calibration/random_split_null.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-23T10:49:07.552345+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 artifacts/r16_threshold_calibration/random_split_null.py",
  "description": "Re-run with joint C classification stats",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 artifacts/r16_threshold_calibration/random_split_null.py",
    "description": "Re-run with joint C classification stats",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-23T10:49:07.552502+00:00_

2023 cohort: 1080 models × 12508 items
  split 10/100  elapsed=0.3s  ETA=2.4s
  split 20/100  elapsed=0.5s  ETA=2.1s
  split 30/100  elapsed=0.8s  ETA=1.8s
  split 40/100  elapsed=1.0s  ETA=1.5s
  split 50/100  elapsed=1.3s  ETA=1.3s
  split 60/100  elapsed=1.5s  ETA=1.0s
  split 70/100  elapsed=1.8s  ETA=0.8s
  split 80/100  elapsed=2.0s  ETA=0.5s
  split 90/100  elapsed=2.3s  ETA=0.3s
  split 100/100  elapsed=2.5s  ETA=0.0s
Done: 100 splits in 2.5s

# Random-Split |Δ_MH| Null Distribution Report

## Setup
- Cohort: 2023 models (N = 1080)
- Items: J = 12508
- Splits: 100 random permutations (each 540 ref vs 540 foc)
- Strata: 5 total-score quantile bins
- Total (item × split) observations: 1,250,800
- Runtime: 2.5s

## Null Distribution Percentiles

| Percentile | |Δ_MH| |
|------------|--------|
| 50th | 0.2956 |
| 90th | 0.7911 |
| 95th | 0.9898 |
| 97.5th | 1.1874 |
| 99th | 1.4504 |
| 99.5th | 1.6536 |
| 99.9th | 2.1998 |

## ETS Threshold Comparison

- Fraction of (item, split) with |Δ_MH| ≥ 1.0 (B threshold): 0.048206 (4.8206%)
- Fraction of (item, split) with |Δ_MH| ≥ 1.5 (C threshold): 0.008480 (0.8480%)
- Items that exceed |Δ_MH| ≥ 1.5 in at least one split: 3717 / 12508 (29.72%)

### ETS C Classification (joint criterion: |Δ_MH| ≥ 1.5 AND p < 0.05)

- Mean null C% per split: 0.6247%
- C% range across splits: [0.0640%, 5.8523%]
- Fraction of (item, split) classified C: 0.006247 (0.6247%)
- Items classified C in at least one split: 3702 / 12508 (29.60%)

## Interpretation

**P95 = 0.9898** (vs ETS B = 1.0): under random splitting, ~5% of item-level |Δ_MH| values approach B-level magnitude purely by chance.

**P99 = 1.4504** (vs ETS C = 1.5): the null 99th percentile nearly reaches the C threshold, meaning ~1% of items can show |Δ_MH| ≥ 1.45 by sampling noise alone.

**Null C% = 0.6247%** (joint criterion: |Δ_MH| ≥ 1.5 AND p < 0.05). The observed temporal C% is ~0.18% (2023→2024 within-year) and ~1.3% (2023 vs 2024 cross-year). The null C% provides the basel
…[truncated 524 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_r16_random_split_null_20260523T104440",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-23T10:49:07.552727+00:00_

全部完成。关键发现：

**Null C% = 0.6247%** — 这是最重要的数字。在纯随机分组下，MH-DIF 联合标准（|Δ_MH| ≥ 1.5 且 p < 0.05）的 false positive rate 约 0.62%。

对比已知观测值：
- 2023 within-year C% (~0.18%) **低于** null → 2023 cohort 内部高度一致
- 2024 cross-year C% (~1.3%) 约为 null 的 2× → 有信号但不极端

P99 = 1.4504 几乎触及 ETS 1.5 阈值，说明在 N=540 per group 的 LLM 场景下，ETS C 阈值大致对应 null 分布的 99th percentile，并非「极端保守」。

输出文件在 `artifacts/r16_threshold_calibration/`：
- `random_split_null.py` — 分析脚本
- `random_split_summary.csv` — 分位数汇总
- `random_split_report.md` — 完整报告
- `per_item_null_stats.csv` — 每个 item 的 null 统计
- `null_histogram.csv` — 直方图数据

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_r16_random_split_null_20260523T104440"
}
```

</details>

---
