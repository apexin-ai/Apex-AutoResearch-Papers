# code dfpr bootstrap ci

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/chats/worker_code_dfpr_bootstrap_ci_20260521T074450.jsonl`
- **Structured JSON:** [`214bf081e7f7301dfc9c.json`](../../sessions/21/214bf081e7f7301dfc9c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

67 recorded events

### Tool call

_source line 1 · 2026-05-21T07:58:12.996158+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore plan_016 code structure",
  "prompt": "I need to understand the cross-subject matching logic in plan_016. \n\n1. List all files in `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/`\n2. Read the main Python files to understand:\n   - How cross-subject matching works\n   - How semi-synthetic injection is done\n   - How MH-DIF is computed\n   - How FPR is calculated (especially at p=0 baseline)\n   - What the \"focal cohort\" and \"reference cohort\" are\n   - How models are selected/grouped\n3. Also check what data files exist: `artifacts/response_matrix.npz`, `artifacts/model_metadata.csv`, `artifacts/item_metadata.csv`\n\nSearch breadth: very thorough. Report back all the key details I need to reimplement the bootstrap."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Explore plan_016 code structure",
    "prompt": "I need to understand the cross-subject matching logic in plan_016. \n\n1. List all files in `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/`\n2. Read the main Python files to understand:\n   - How cross-subject matching works\n   - How semi-synthetic injection is done\n   - How MH-DIF is computed\n   - How FPR is calculated (especially at p=0 baseline)\n   - What the \"focal cohort\" and \"reference cohort\" are\n   - How models are selected/grouped\n3. Also check what data files exist: `artifacts/response_matrix.npz`, `artifacts/model_metadata.csv`, `artifacts/item_metadata.csv`\n\nSearch breadth: very thorough. Report back all the key details I need to reimplement the bootstrap."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-21T07:58:12.996558+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/ -type f | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/ -type f | head -50"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-21T07:58:12.996930+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/within_subject_dose_response.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/within_subject_injection_results.csv
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_within_subject_injection.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T07:58:12.997087+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T07:58:12.997278+00:00_

total 72
drwxr-xr-x  2 ubuntu ubuntu  4096 May 20 22:46 .
drwxr-xr-x 30 ubuntu ubuntu  4096 May 21 07:25 ..
-rw-r--r--  1 ubuntu ubuntu  8524 May 20 22:47 plan_016_report.md
-rw-r--r--  1 ubuntu ubuntu 23768 May 20 22:46 plan_016_within_subject_injection.py
-rw-r--r--  1 ubuntu ubuntu  4285 May 20 22:47 within_subject_dose_response.csv
-rw-r--r--  1 ubuntu ubuntu 17107 May 20 22:47 within_subject_injection_results.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T07:58:12.997444+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep -E \"response_matrix|model_metadata|item_metadata\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ | grep -E \"response_matrix|model_metadata|item_metadata\""
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T07:58:12.997571+00:00_

-rw-r--r--  1 ubuntu ubuntu    20975 May 20 20:48 build_response_matrix.py
-rw-r--r--  1 ubuntu ubuntu  1528143 May 20 20:57 item_metadata.csv
-rw-r--r--  1 ubuntu ubuntu   399283 May 20 20:51 model_metadata.csv
-rw-r--r--  1 ubuntu ubuntu 50638630 May 20 20:51 response_matrix.npz
-rw-r--r--  1 ubuntu ubuntu    87445 May 20 20:51 response_matrix_index.npz

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T07:58:12.997738+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_within_subject_injection.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_within_subject_injection.py"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T07:58:12.998020+00:00_

1	#!/usr/bin/env python3
2	"""
3	plan_016: Within-Subject Semi-Synthetic Injection
4	
5	For each of 5 selected MMLU subjects, inject differential contamination into
6	the temporal focal group (2024 models) and test whether within-subject MH-DIF
7	detects the injected signal.
8	
9	Subjects: business_ethics (93), human_aging (203), professional_medicine (248),
10	          formal_logic (109), high_school_statistics (181)
11	Injection: 20% items contaminated, p ∈ {0.0, 0.5, 1.0}, 5 seeds
12	Matching: within-subject purified total score + cross-subject total score
13	"""
14	
15	import numpy as np
16	import pandas as pd
17	from scipy.sparse import load_npz
18	from scipy.stats import chi2 as chi2_dist, fisher_exact
19	from pathlib import Path
20	import time
21	import warnings
22	
23	warnings.filterwarnings("ignore", category=RuntimeWarning)
24	
25	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
26	OUT = BASE / "plan_016"
27	OUT.mkdir(exist_ok=True)
28	
29	SUBJECTS = ["business_ethics", "human_aging", "professional_medicine",
30	            "formal_logic", "high_school_statistics"]
31	INJECTION_PS = [0.0, 0.5, 1.0]
32	N_SEEDS = 5
33	CONTAM_FRAC = 0.20
34	N_STRATA = 5
35	MIN_PER_STRATUM = 5
36	
37	
38	# ════════════════════════════════════════════════════════════════════════════
39	#  MH-DIF CORE (from plan_014 with strata merging + external score support)
40	# ════════════════════════════════════════════════════════════════════════════
41	def purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,
42	                    external_scores_foc=None, min_per_stratum=5):
43	    J = X_ref.shape[1]
44	    use_external = external_scores_ref is not None
45	
46	    if not use_external:
47	        tot_ref = X_ref.sum(axis=1).astype(np.float64)
48	        tot_foc = X_foc.sum(axis=1).astype(np.float64)
49	
50	    rows = []
51	    for j in range(J):
52	        if use_external:
53	            s_ref = external_scores_ref
…[truncated 22291 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T07:58:12.998194+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_report.md"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T07:58:12.998354+00:00_

1	# Plan 016: Within-Subject Semi-Synthetic Injection
2	
3	## Objective
4	
5	Verify that MH-DIF detects differential contamination **within individual subjects**,
6	not just globally. This validates plan_014's finding that within-subject temporal
7	C% = 38.1% reflects real signal, not method failure.
8	
9	## Setup
10	
11	- **Temporal cohort**: ref=2023 (1080 models), foc=2024 (807 models)
12	- **Focal injection subset**: 787 models (ability overlap with ref)
13	- **Contamination fraction**: 20% of items per subject
14	- **Injection probabilities**: [0.0, 0.5, 1.0]
15	- **Seeds per p**: 5
16	- **Matching**: within-subject purified total score + cross-subject total score
17	
18	### Subjects
19	
20	| Subject | N items | N contaminated | N baseline | Strata |
21	|---------|---------|----------------|------------|--------|
22	| business_ethics | 93 | 18 | 75 | 3 |
23	| human_aging | 203 | 40 | 163 | 5 |
24	| professional_medicine | 248 | 49 | 199 | 5 |
25	| formal_logic | 109 | 21 | 88 | 5 |
26	| high_school_statistics | 181 | 36 | 145 | 5 |
27	
28	## Results: Within-Subject Matching
29	
30	Matching variable = purified total score on current subject's items (minus studied item).
31	
32	### Per-Subject Dose-Response (Within)
33	
34	| Subject | p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |
35	|---------|---|----------------|----------------|------|-----------|----------|
36	| business_ethics | 0.0 | 0.600±0.072 | 0.563±0.017 | +0.000 | 1.24 | 0.5990 |
37	| business_ethics | 0.5 | 0.522±0.084 | 0.603±0.017 | -0.078 | 0.78 | 0.5957 |
38	| business_ethics | 1.0 | 1.000±0.000 | 0.629±0.017 | +0.400 | inf | 0.0012 |
39	| formal_logic | 0.0 | 0.333±0.158 | 0.409±0.038 | +0.000 | 0.92 | 0.2169 |
40	| formal_logic | 0.5 | 0.790±0.080 | 0.500±0.033 | +0.457 | 4.21 | 0.0254 |
41	| formal_logic | 1.0 | 1.000±0.000 | 0.584±0.019 | +0.667 | inf | 0.0001 |
42	| high_school_statistics | 0.0 | 0.472±0.059 | 0.407±0.015 | +0.000 | 1.35 | 0.5720 |
43	| high_school_stat
…[truncated 6962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T07:58:12.998518+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -5 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "tool_args": {
    "command": "head -5 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T07:58:12.998641+00:00_

model_name,family,release_year,release_half,training_method,accuracy,cohort_temporal,cohort_accuracy_quintile
0-hero/Matter-0.1-7B,unknown,unknown,unknown,unknown,0.661225,other,3
0-hero/Matter-0.1-7B-DPO-preview,,unknown,unknown,DPO,0.661337,other,3
0-hero/Matter-0.1-7B-boost,unknown,unknown,unknown,unknown,0.653422,other,3
0-hero/Matter-0.1-7B-boost-DPO,,unknown,unknown,DPO,0.654941,other,3

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T07:58:12.998814+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -5 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/item_metadata.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "tool_args": {
    "command": "head -5 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/item_metadata.csv"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T07:58:12.998944+00:00_

item_id,subject,ctt_difficulty,ctt_discrimination,sd,is_negative_disc,empirical_p
abstract_algebra.1,abstract_algebra,0.1415501053841732,-0.2833678806673642,0.391334247107756,True,0.18867202449292
abstract_algebra.10,abstract_algebra,0.0829181835600689,0.1905805323705553,0.313613528527619,False,0.11040949100650593
abstract_algebra.100,abstract_algebra,0.0485725234719294,0.0603451356931113,0.2461314261708401,False,0.06467661691542288
abstract_algebra.11,abstract_algebra,0.5031136232994826,0.0842828755338663,0.4699611407645028,False,0.6701109835438194

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T07:58:12.999075+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -10 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/within_subject_injection_results.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "tool_args": {
    "command": "head -10 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/within_subject_injection_results.csv"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T07:58:12.999194+00:00_

subject,p,seed,matching_type,n_items,n_baseline,n_contaminated,n_flipped,tpr,fpr,n_c_contam,n_c_clean,fisher_or,fisher_p
business_ethics,0.0,1,within,93,75,18,0,0.6666666666666666,0.5466666666666666,12,41,1.6585365853658536,0.4325726597644446
business_ethics,0.0,1,cross,93,75,18,0,0.5555555555555556,0.5333333333333333,10,40,1.09375,1.0
business_ethics,0.0,2,within,93,75,18,0,0.5,0.5866666666666667,9,44,0.7045454545454546,0.5989625496035944
business_ethics,0.0,2,cross,93,75,18,0,0.3333333333333333,0.5866666666666667,6,44,0.3522727272727273,0.06742122723354463
business_ethics,0.0,3,within,93,75,18,0,0.5555555555555556,0.5733333333333334,10,43,0.9302325581395349,1.0
business_ethics,0.0,3,cross,93,75,18,0,0.5555555555555556,0.5333333333333333,10,40,1.09375,1.0
business_ethics,0.0,4,within,93,75,18,0,0.6666666666666666,0.5466666666666666,12,41,1.6585365853658536,0.4325726597644446
business_ethics,0.0,4,cross,93,75,18,0,0.6666666666666666,0.5066666666666667,12,38,1.9473684210526316,0.294839665891075
business_ethics,0.0,5,within,93,75,18,0,0.6111111111111112,0.56,11,42,1.2346938775510203,0.794092511324052

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T07:58:12.999335+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ -name \"*.py\" | grep -E \"(plan|bootstrap)\" | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ -name \"*.py\" | grep -E \"(plan|bootstrap)\" | sort"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T07:58:12.999470+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/plan_004_step1_gsm8k_temporal_dif.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/plan_020_circularity_ablation.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_004_step2_gsm8k_semi_synthetic.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_004_step3_gsm1k_dif_correlation.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_012_irt_theta_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_013_q3_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_014_within_subject_dif.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_016_within_subject_injection.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_021_nonuniform_dif.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/data/plan_001_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu/intermediate/plan_001_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/data/plan_001b_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b/plan_001b_analysis.py
/home/ubuntu/.agent-ml-researc
…[truncated 3852 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T07:58:12.999613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_014/plan_014_within_subject_dif.py",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_014/plan_014_within_subject_dif.py",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T07:58:12.999813+00:00_

1	#!/usr/bin/env python3
2	"""
3	plan_014: Within-Subject Temporal DIF + Cross-Subject Matching + SIBTEST Check
4	
5	Part 1: For 5 high-C% subjects, run purified MH-DIF using within-subject total score
6	Part 2: Re-run with cross-subject total score (all other subjects) as matching variable
7	Part 3: Check SIBTEST availability (R packages + Python)
8	"""
9	
10	import numpy as np
11	import pandas as pd
12	from scipy.sparse import load_npz
13	from scipy.stats import chi2 as chi2_dist
14	from pathlib import Path
15	import subprocess
16	import time
17	import warnings
18	
19	warnings.filterwarnings("ignore", category=RuntimeWarning)
20	
21	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
22	OUT = BASE / "plan_014"
23	OUT.mkdir(exist_ok=True)
24	
25	SUBJECTS = [
26	    ("business_ethics", 93, 48.4),
27	    ("human_aging", 203, 41.9),
28	    ("formal_logic", 109, 40.4),
29	    ("professional_medicine", 248, 37.9),
30	    ("high_school_statistics", 181, 35.4),
31	]
32	
33	N_STRATA = 5
34	MIN_PER_STRATUM = 5
35	
36	
37	# ════════════════════════════════════════════════════════════════════════════
38	#  MH-DIF CORE (adapted from plan_011)
39	# ════════════════════════════════════════════════════════════════════════════
40	def purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,
41	                    external_scores_foc=None, min_per_stratum=5):
42	    """
43	    Purified MH-DIF for all columns in X_ref/X_foc.
44	    If external_scores provided, use those for stratification.
45	    Otherwise use purified within-subject total (sum minus current item).
46	    Merges adjacent strata if any stratum has < min_per_stratum in either group.
47	    """
48	    J = X_ref.shape[1]
49	    use_external = external_scores_ref is not None
50	
51	    if not use_external:
52	        tot_ref = X_ref.sum(axis=1).astype(np.float64)
53	        tot_foc = X_foc.sum(axis=1).astype(np.float64)
54	
55	    rows = []
56	    for j in r
…[truncated 5131 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T07:58:12.999988+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_bootstrap_ci.py",
  "limit": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_bootstrap_ci.py",
    "limit": "300"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T07:58:13.000187+00:00_

1	"""BCa bootstrap confidence intervals for GSM1K contamination gap correlations."""
2	
3	import numpy as np
4	import pandas as pd
5	from scipy import stats
6	from pathlib import Path
7	
8	BASE = Path(__file__).parent
9	DATA_PATH = BASE / "gsm1k_dif_correlation.csv"
10	DOMAIN_PATH = BASE.parent / "plan_001" / "domain_specificity.csv"
11	OUTPUT_PATH = BASE / "bootstrap_ci_report.md"
12	N_BOOT = 10_000
13	ALPHA = 0.05
14	SEED = 42
15	
16	
17	def bca_bootstrap_ci(arrays, stat_func, n_boot=N_BOOT, alpha=ALPHA, seed=SEED):
18	    """BCa bootstrap CI for a statistic computed from multiple aligned arrays."""
19	    rng = np.random.RandomState(seed)
20	    n = len(arrays[0])
21	
22	    theta_hat = stat_func(*arrays)
23	
24	    theta_boot = np.empty(n_boot)
25	    for i in range(n_boot):
26	        idx = rng.choice(n, size=n, replace=True)
27	        theta_boot[i] = stat_func(*(a[idx] for a in arrays))
28	
29	    z0 = stats.norm.ppf(np.mean(theta_boot < theta_hat))
30	
31	    theta_jack = np.empty(n)
32	    for i in range(n):
33	        idx = np.concatenate([np.arange(i), np.arange(i + 1, n)])
34	        theta_jack[i] = stat_func(*(a[idx] for a in arrays))
35	
36	    theta_dot = np.mean(theta_jack)
37	    diff = theta_dot - theta_jack
38	    a_hat = np.sum(diff ** 3) / (6.0 * np.sum(diff ** 2) ** 1.5 + 1e-15)
39	
40	    z_lo = stats.norm.ppf(alpha / 2)
41	    z_hi = stats.norm.ppf(1 - alpha / 2)
42	
43	    def adj(z_a):
44	        num = z0 + z_a
45	        return stats.norm.cdf(z0 + num / (1 - a_hat * num))
46	
47	    p_lo = np.clip(adj(z_lo), 0.5 / n_boot, 1 - 0.5 / n_boot)
48	    p_hi = np.clip(adj(z_hi), 0.5 / n_boot, 1 - 0.5 / n_boot)
49	
50	    ci_lo = np.percentile(theta_boot, 100 * p_lo)
51	    ci_hi = np.percentile(theta_boot, 100 * p_hi)
52	    boot_se = np.std(theta_boot, ddof=1)
53	
54	    return theta_hat, ci_lo, ci_hi, boot_se
55	
56	
57	def pearson_r(x, y):
58	    return stats.pearsonr(x, y)[0]
59	
60	
61	def spearman_rho(x, y):
62	    return stats.spearmanr(x,
…[truncated 5552 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T07:58:13.000367+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ -name \"memory.md\" -o -name \"ROADMAP.md\" -o -name \"CLAUDE.md\" 2>/dev/null | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/ -name \"memory.md\" -o -name \"ROADMAP.md\" -o -name \"CLAUDE.md\" 2>/dev/null | head -5"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T07:58:13.000684+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/memory.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/review_director_870d8ac6/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/agent_9c4a2fd1/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/director_af61c18a/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/paper_agent_3035e659/CLAUDE.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T07:58:13.000866+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T07:58:13.001027+00:00_

1	## MVP 验证关键经验 (2026-05-20)
2	
3	### D001 决策：ETS C 分类 > p-value 检验
4	- **p-value based DIF 检测在 200-item benchmark 上严重 underpowered**：BH 校正后 TPR 仅 0.04-0.07（N=50, δ=1.0）
5	- **ETS C 分类（|Δ_MH|≥1.5 + 显著性）是可行的替代**：TPR=0.68-0.85 at N≥80, δ≥1.4
6	- **AUC 一直很好（0.91-0.96）**
7	
8	### 关键操作参数
9	- N≥80/group 最低要求，N≥100 显著改善
10	- δ≥1.4 logits 可靠检测区间
11	- MH 5 层 quantile + ETS C 阈值是最佳组合
12	- Subject ≥200 items 才有足够 matching precision（<100 items baseline FPR 膨胀至 ~56%）
13	
14	## D006: plan_011 Semi-Synthetic 验证成功 ✅
15	
16	### DIF 检测差异性污染有效
17	- **External MH**: temporal ΔTPR=+0.674 (0.326→1.000), FPR 恒定 0.314
18	- **Matching variable contamination**: 20% items 注入时 standard MH FPR 0.298→0.616, anchor/external 免疫
19	- **Li et al. enrichment≈1.0 原因**: web-overlap = 全局性污染，不产生 DIF
20	
21	## D007-D010: 降低 FPR 路线全部穷尽 ⚠️
22	
23	### plan_012 θ-Conditioning 失败
24	- logit θ 与 total score 相关性 0.9986 → 单维 θ 分层 ≡ 总分分层
25	
26	### plan_014 Within-Subject 前置检查：C% = 38.1% (>25%)
27	- 5 个高 C% subjects 的 within-subject temporal C% 均 >25%（31-45%）
28	- Within vs cross-subject matching 差异仅 -2.4pp → 信号对 matching 不敏感
29	- **结论**：temporal DIF 渗透到每个 subject 内部，不是 between-subject 能力差异的伪影
30	- Bifactor 方向因此否定（D010）
31	
32	### plan_013 Q3 局部独立性：温和但存在
33	- Within-subject mean Q3 = 0.009（低于 0.20 阈值）
34	- 但 11.3% within-subject pairs |Q3|>0.20（vs 2.2% cross-subject，5x）
35	- 最严重: moral_scenarios 34.2%, world_religions 18%, marketing 17.5%
36	- 不太可能单独解释 31% FPR
37	
38	### plan_016 Within-Subject Semi-Synthetic：DIF 在 subject 内也有效 ✅
39	- Cross-subject matching FPR 完全稳定（ΔFPR=0.000），4/5 subjects ΔTPR>0.3
40	- Within-subject matching FPR 膨胀 +0.067 to +0.281（matching variable 包含注入 items）
41	- **结论**：within-subject 38% C% 是真实 temporal DIF，方法论有效
42	
43	### 综合推导：31% temporal FPR 不是 artifact
44	证伪链完整：1D θ 无效 → within-subject 仍高 → bifactor 否定 → Q3 不是主因 → **这是 genuine temporal DIF**（2023→2024 模型在特定 items 上的真实差异性表现变化）。DIF 方法有效但无法区分 contamination-DIF 和 capability-DIF。
45	
46	## D012: plan_017 Downstream Impact — DIF Items ≠ 噪声 ⚠
…[truncated 2789 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T07:58:13.001289+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py",
    "limit": "250"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-21T07:58:13.001501+00:00_

1	#!/usr/bin/env python3
2	"""
3	plan_011_analysis.py — Semi-Synthetic DIF Validation
4	
5	Injects known differential contamination into real MMLU response data and tests
6	whether MH-DIF can detect it. Validates the DIF methodology used in plan_001.
7	
8	Three MH variants:
9	  (1) standard  — total score on 500 items minus current (same as plan_001)
10	  (2) anchor    — total score on 400 known-clean items only
11	  (3) external  — total score on full 12508-item original matrix (best matching)
12	
13	Inputs:
14	  response_matrix.npz, response_matrix_index.npz, model_metadata.csv,
15	  item_metadata.csv, mmlu_li2024_proxy_labels.csv,
16	  plan_001/dif_results_ability.csv
17	
18	Outputs (all in plan_011/):
19	  injection_results.csv, dose_response_summary.csv, per_item_results.csv,
20	  plan_011_report.md
21	"""
22	
23	import numpy as np
24	import pandas as pd
25	from scipy.sparse import load_npz
26	from scipy.stats import chi2 as chi2_dist, fisher_exact
27	from pathlib import Path
28	import time
29	import warnings
30	
31	warnings.filterwarnings("ignore", category=RuntimeWarning)
32	
33	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
34	OUT = BASE / "plan_011"
35	OUT.mkdir(exist_ok=True)
36	
37	INJECTION_PS = [0.0, 0.3, 0.5, 0.7, 1.0]
38	N_SEEDS = 5
39	N_BASELINE = 500
40	N_CONTAMINATED = 100
41	
42	
43	# ════════════════════════════════════════════════════════════════════════════
44	#  MH-DIF CORE
45	# ════════════════════════════════════════════════════════════════════════════
46	def mh_dif_subset(X_ref, X_foc, n_strata=5, anchor_cols=None,
47	                  external_scores_ref=None, external_scores_foc=None):
48	    """
49	    Purified MH-DIF for all columns.
50	
51	    Stratification source (in priority order):
52	      1. external_scores_ref/foc — precomputed ability scores (e.g. full-matrix total)
53	      2. anchor_cols — total score from specified columns only
54	      3. None — standard purified (a
…[truncated 7898 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T07:58:13.002055+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -20 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/within_subject_dose_response.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "tool_args": {
    "command": "head -20 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/within_subject_dose_response.csv"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T07:58:13.002230+00:00_

subject,p,matching_type,tpr_mean,tpr_std,fpr_mean,fpr_std,delta_tpr,fisher_or_mean,fisher_p_median
business_ethics,0.0,cross,0.5555555555555556,0.13608276348795434,0.5333333333333334,0.032659863237109024,0.0,1.2869019138755982,0.294839665891075
business_ethics,0.0,within,0.6,0.0724355822800294,0.5626666666666666,0.017384539747207082,0.0,1.2373090121935433,0.5989625496035944
business_ethics,0.5,cross,0.6111111111111112,0.055555555555555525,0.5333333333333334,0.032659863237109024,0.05555555555555558,1.4255724538619277,0.44637304853594856
business_ethics,0.5,within,0.5222222222222223,0.08425417160057277,0.6026666666666667,0.017384539747207068,-0.07777777777777772,0.7760791074482102,0.5956725676908661
business_ethics,1.0,cross,1.0,0.0,0.5333333333333334,0.032659863237109024,0.4444444444444444,inf,7.650538099771612e-05
business_ethics,1.0,within,1.0,0.0,0.6293333333333334,0.01738453974720708,0.4,inf,0.0011840274522551643
formal_logic,0.0,cross,0.3619047619047619,0.13718914562750412,0.4022727272727272,0.03273831884292712,0.0,1.0018702062819709,0.3242857143685039
formal_logic,0.0,within,0.3333333333333333,0.1579345138264476,0.40909090909090906,0.03768891807222045,0.0,0.9165509503744798,0.21690431559178033
formal_logic,0.5,cross,0.9047619047619048,0.08908708063747481,0.4022727272727272,0.03273831884292712,0.5428571428571429,inf,4.729088163088643e-05
formal_logic,0.5,within,0.7904761904761906,0.07968190728895957,0.5,0.0331304084934392,0.45714285714285724,4.209665551839465,0.02541389125536241
formal_logic,1.0,cross,1.0,0.0,0.4022727272727272,0.03273831884292712,0.638095238095238,inf,1.5255546300936283e-07
formal_logic,1.0,within,1.0,0.0,0.5840909090909092,0.019015000603047155,0.6666666666666667,inf,6.368425177331953e-05
high_school_statistics,0.0,cross,0.4,0.046481112585226414,0.3351724137931035,0.011540138297021734,0.0,1.352732201056,0.5638963166592237
high_school_statistics,0.0,within,0.4722222222222222,0.05892556509887897,0.4068965517241379,0.01462979547282513,0.0,1.350218
…[truncated 744 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T07:58:13.002388+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"bootstrap\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"bootstrap\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/ 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-21T07:58:13.002512+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T07:58:13.002646+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'EOF'\nimport numpy as np\nidx = np.load(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix_index.npz\", allow_pickle=True)\nprint(\"Keys:\", list(idx.files))\nprint(\"\\nmodel_names shape:\", idx['model_names'].shape)\nprint(\"item_ids shape:\", idx['item_ids'].shape)\nprint(\"\\nFirst 5 model names:\", idx['model_names'][:5])\nprint(\"First 5 item ids:\", idx['item_ids'][:5])\nEOF\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'EOF'\nimport numpy as np\nidx = np.load(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix_index.npz\", allow_pickle=True)\nprint(\"Keys:\", list(idx.files))\nprint(\"\\nmodel_names shape:\", idx['model_names'].shape)\nprint(\"item_ids shape:\", idx['item_ids'].shape)\nprint(\"\\nFirst 5 model names:\", idx['model_names'][:5])\nprint(\"First 5 item ids:\", idx['item_ids'][:5])\nEOF\n"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-21T07:58:13.002797+00:00_

Keys: ['model_names', 'item_ids']

model_names shape: (5227,)
item_ids shape: (12508,)

First 5 model names: ['0-hero/Matter-0.1-7B' '0-hero/Matter-0.1-7B-DPO-preview'
 '0-hero/Matter-0.1-7B-boost' '0-hero/Matter-0.1-7B-boost-DPO'
 '0-hero/Matter-0.1-7B-boost-DPO-preview']
First 5 item ids: ['abstract_algebra.1' 'abstract_algebra.10' 'abstract_algebra.100'
 'abstract_algebra.11' 'abstract_algebra.12']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T07:58:13.002992+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A 5 \"def purified_mh_dif\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_within_subject_injection.py | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A 5 \"def purified_mh_dif\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_within_subject_injection.py | head -20"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-21T07:58:13.003176+00:00_

def purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,
                    external_scores_foc=None, min_per_stratum=5):
    J = X_ref.shape[1]
    use_external = external_scores_ref is not None

    if not use_external:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T07:58:13.003412+00:00_

Perfect. I have all the information I need. Let me compile a comprehensive summary.

## Comprehensive Plan 016 Analysis: Cross-Subject Matching Logic & Bootstrap Implementation

Based on my thorough exploration of the plan_016 artifacts and related code, here's everything you need to reimplement the bootstrap:

### **FILES IN /artifacts/plan_016/**
- `plan_016_within_subject_injection.py` — Main execution script
- `plan_016_report.md` — Results and interpretation
- `within_subject_injection_results.csv` — Per-run results (750 rows: 5 subjects × 3 p values × 5 seeds × 2 matching types)
- `within_subject_dose_response.csv` — Aggregated by subject × p × matching_type (30 rows)

### **DATA FILES REFERENCED**
- `/artifacts/response_matrix.npz` (50.6 MB) — Sparse 5227×12508 binary response matrix
- `/artifacts/response_matrix_index.npz` — model_names (5227,) and item_ids (12508,)
- `/artifacts/model_metadata.csv` — model_name, cohort_temporal (2023 or 2024), accuracy, etc.
- `/artifacts/item_metadata.csv` — item_id, subject, ctt_difficulty, ctt_discrimination, empirical_p

---

## **CROSS-SUBJECT MATCHING LOGIC**

### **Key Concept: Two Matching Strategies Compared**

1. **Within-Subject Matching** (lines 279-281):
   - Stratification variable = purified total score on **current subject's items only** (minus the item being tested)
   - Formula: `s = sum(X_subj) - X_subj[:, j]` for item j
   - Contamination-prone: matching variable contains injected items

2. **Cross-Subject Matching** (lines 282-286):
   - Stratification variable = total score on **all other subjects' items** (never touched by injection)
   - Formula: precomputed as `cross_ref_base = sum(mat[ref_rows][:, other_cols])` and similar for focal
   - Contamination-immune: matching variable unaffected by injection in current subject
   - These are external scores passed to `purified_mh_dif()` as `external_scores_ref/foc`

### **How Cross-Subject Scores Are Computed (lines 241-248)**

```python
# For each subject
…[truncated 11077 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Agent",
  "elapsed_ms": 7
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T07:58:13.003605+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/within_subject_dose_response.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/within_subject_dose_response.csv"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T07:58:13.003781+00:00_

1	subject,p,matching_type,tpr_mean,tpr_std,fpr_mean,fpr_std,delta_tpr,fisher_or_mean,fisher_p_median
2	business_ethics,0.0,cross,0.5555555555555556,0.13608276348795434,0.5333333333333334,0.032659863237109024,0.0,1.2869019138755982,0.294839665891075
3	business_ethics,0.0,within,0.6,0.0724355822800294,0.5626666666666666,0.017384539747207082,0.0,1.2373090121935433,0.5989625496035944
4	business_ethics,0.5,cross,0.6111111111111112,0.055555555555555525,0.5333333333333334,0.032659863237109024,0.05555555555555558,1.4255724538619277,0.44637304853594856
5	business_ethics,0.5,within,0.5222222222222223,0.08425417160057277,0.6026666666666667,0.017384539747207068,-0.07777777777777772,0.7760791074482102,0.5956725676908661
6	business_ethics,1.0,cross,1.0,0.0,0.5333333333333334,0.032659863237109024,0.4444444444444444,inf,7.650538099771612e-05
7	business_ethics,1.0,within,1.0,0.0,0.6293333333333334,0.01738453974720708,0.4,inf,0.0011840274522551643
8	formal_logic,0.0,cross,0.3619047619047619,0.13718914562750412,0.4022727272727272,0.03273831884292712,0.0,1.0018702062819709,0.3242857143685039
9	formal_logic,0.0,within,0.3333333333333333,0.1579345138264476,0.40909090909090906,0.03768891807222045,0.0,0.9165509503744798,0.21690431559178033
10	formal_logic,0.5,cross,0.9047619047619048,0.08908708063747481,0.4022727272727272,0.03273831884292712,0.5428571428571429,inf,4.729088163088643e-05
11	formal_logic,0.5,within,0.7904761904761906,0.07968190728895957,0.5,0.0331304084934392,0.45714285714285724,4.209665551839465,0.02541389125536241
12	formal_logic,1.0,cross,1.0,0.0,0.4022727272727272,0.03273831884292712,0.638095238095238,inf,1.5255546300936283e-07
13	formal_logic,1.0,within,1.0,0.0,0.5840909090909092,0.019015000603047155,0.6666666666666667,inf,6.368425177331953e-05
14	high_school_statistics,0.0,cross,0.4,0.046481112585226414,0.3351724137931035,0.011540138297021734,0.0,1.352732201056,0.5638963166592237
15	high_school_statistics,0.0,within,0.4722222222222222,0.05892556509887897,0.4068965517241
…[truncated 2372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T07:58:13.003936+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_within_subject_injection.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016/plan_016_within_subject_injection.py"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T07:58:13.004257+00:00_

1	#!/usr/bin/env python3
2	"""
3	plan_016: Within-Subject Semi-Synthetic Injection
4	
5	For each of 5 selected MMLU subjects, inject differential contamination into
6	the temporal focal group (2024 models) and test whether within-subject MH-DIF
7	detects the injected signal.
8	
9	Subjects: business_ethics (93), human_aging (203), professional_medicine (248),
10	          formal_logic (109), high_school_statistics (181)
11	Injection: 20% items contaminated, p ∈ {0.0, 0.5, 1.0}, 5 seeds
12	Matching: within-subject purified total score + cross-subject total score
13	"""
14	
15	import numpy as np
16	import pandas as pd
17	from scipy.sparse import load_npz
18	from scipy.stats import chi2 as chi2_dist, fisher_exact
19	from pathlib import Path
20	import time
21	import warnings
22	
23	warnings.filterwarnings("ignore", category=RuntimeWarning)
24	
25	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
26	OUT = BASE / "plan_016"
27	OUT.mkdir(exist_ok=True)
28	
29	SUBJECTS = ["business_ethics", "human_aging", "professional_medicine",
30	            "formal_logic", "high_school_statistics"]
31	INJECTION_PS = [0.0, 0.5, 1.0]
32	N_SEEDS = 5
33	CONTAM_FRAC = 0.20
34	N_STRATA = 5
35	MIN_PER_STRATUM = 5
36	
37	
38	# ════════════════════════════════════════════════════════════════════════════
39	#  MH-DIF CORE (from plan_014 with strata merging + external score support)
40	# ════════════════════════════════════════════════════════════════════════════
41	def purified_mh_dif(X_ref, X_foc, n_strata=5, external_scores_ref=None,
42	                    external_scores_foc=None, min_per_stratum=5):
43	    J = X_ref.shape[1]
44	    use_external = external_scores_ref is not None
45	
46	    if not use_external:
47	        tot_ref = X_ref.sum(axis=1).astype(np.float64)
48	        tot_foc = X_foc.sum(axis=1).astype(np.float64)
49	
50	    rows = []
51	    for j in range(J):
52	        if use_external:
53	            s_ref = external_scores_ref
…[truncated 22291 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T07:58:13.004610+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement",
    "description": "Create output directory"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T07:58:13.004821+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T07:58:13.005016+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement/bootstrap_dfpr.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nplan_016_supplement: Bootstrap CI for ΔFPR in Cross-Subject Matching\n\nAddresses reviewer concern that ΔFPR = 0.000 across all 5 subjects is \"too\nperfect\". Resamples focal cohort models (with replacement) 1000 times per\nsubject, re-running cross-subject MH-DIF at p=0 (baseline) and p=1 (max\ninjection) to quantify the sampling distribution of ΔFPR.\n\nAlgebraic note: For cross-subject matching, ΔFPR = 0 is guaranteed because\n(1) clean item responses are unchanged by injection, and (2) cross-subject\nstratification scores are independent of injected items. The bootstrap\nconfirms this algebraic invariant empirically.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist\nfrom pathlib import Path\nimport time\nimport warnings\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/\"\n            \"irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_016_supplement\"\nOUT.mkdir(exist_ok=True)\n\nSUBJECTS = [\"business_ethics\", \"human_aging\", \"professional_medicine\",\n            \"formal_logic\", \"high_school_statistics\"]\nN_BOOT = 1000\nCONTAM_FRAC = 0.20\nCONTAM_SEED = 1\nN_STRATA_DEFAULT = 5\nMIN_PER_STRATUM = 5\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  MH-DIF helpers (from plan_016, optimised for cross-subject matching)\n# ═══════════════════════════════════════════════════════════════════════\n\ndef _merge_small_strata(k_all, groups_all, n_bins, min_n):\n    labels = k_all.copy()\n    merged = True\n    while merged:\n        merged = False\n        unique_strata = sorted(np.unique(labels))\n        for i, k in enumerate(unique_strata):\n            mask_k = (labels == k)\n            n_ref = int((mask_k & (groups_all == 0)).sum())\n            n_foc = int((mask_k & (groups_all == 1)).sum())\n            if n_ref < min_n or n_foc < min_n:\n                if i + 1 < len(unique_strata):\n                    labels[labels == unique_strata[i + 1]] = k\n                elif i > 0:\n                    labels[labels == k] = unique_strata[i - 1]\n                merged = True\n                break\n    return labels\n\n\ndef cross_mh_ets(X_ref, X_foc, scores_ref, scores_foc,\n                 n_strata=5, min_per_stratum=5):\n    \"\"\"Cross-subject MH-DIF returning ETS class per item.\n\n    Optimised: strata are computed once (external scores are item-invariant).\n    \"\"\"\n    J = X_ref.shape[1]\n    n_ref_models = len(scores_ref)\n\n    s_all = np.concatenate([scores_ref, scores_foc])\n    groups_all = np.concatenate([np.zeros(n_ref_models),\n                                 np.ones(len(scores_foc))])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    if len(edges) < 2:\n        return np.array([\"A\"] * J)\n\n    k_all = np.digitize(s_all, edges[1:-1])\n    strata = _merge_small_strata(k_all, groups_all,\n                                 len(edges) - 1, min_per_stratum)\n\n    stratum_info = []\n    for k in np.unique(strata):\n        mask_k = (strata == k)\n        mask_ref = mask_k[:n_ref_models]\n        mask_foc = mask_k[n_ref_models:]\n        n1 = int(mask_ref.sum())\n        n0 = int(mask_foc.sum())\n        if n1 > 0 and n0 > 0:\n            stratum_info.append((mask_ref, mask_foc, float(n1), float(n0)))\n\n    ets_classes = np.empty(J, dtype=\"U1\")\n\n    for j in range(J):\n        x_ref_j = X_ref[:, j].astype(np.float64)\n        x_foc_j = X_foc[:, j].astype(np.float64)\n\n        R = S = sum_diff = sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        for mask_ref, mask_foc, n1, n0 in stratum_info:\n            A = float(x_ref_j[mask_ref].sum())\n            B = n1 - A\n            C = float(x_foc_j[mask_foc].sum())\n            D = n0 - C\n            Nk = n1 + n0\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            ets_classes[j] = \"A\"\n            continue\n\n        if S == 0:\n            delta = -np.inf\n        elif R == 0:\n            delta = np.inf\n        else:\n            delta = -2.35 * np.log(R / S)\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else np.inf\n        if ad < 1.0:\n            ets_classes[j] = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets_classes[j] = \"C\"\n        else:\n            ets_classes[j] = \"B\"\n\n    return ets_classes\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ═══════════════════════════════════════════════════════════════════════\nprint(\"=== Loading data ===\")\nt0 = time.time()\n\nmat = load_npz(BASE / \"response_matrix.npz\")\nidx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\nMODEL_NAMES = idx[\"model_names\"]\nITEM_IDS = idx[\"item_ids\"]\nITEM2COL = {iid: i for i, iid in enumerate(ITEM_IDS)}\n\nmodel_meta = pd.read_csv(BASE / \"model_metadata.csv\")\nitem_meta = pd.read_csv(BASE / \"item_metadata.csv\")\nNAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}\n\nref_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"model_name\"]\nfoc_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"model_name\"]\nref_rows = np.array([NAME2ROW[n] for n in ref_names if n in NAME2ROW])\nfoc_rows = np.array([NAME2ROW[n] for n in foc_names if n in NAME2ROW])\n\nref_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\nfoc_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"accuracy\"]\nt_overlap_min = max(ref_acc.min(), foc_acc.min())\nt_overlap_max = min(ref_acc.max(), foc_acc.max())\n\nfoc_inject_mask_global = (\n    (model_meta[\"cohort_temporal\"] == \"2024\")\n    & (model_meta[\"accuracy\"] >= t_overlap_min)\n    & (model_meta[\"accuracy\"] <= t_overlap_max)\n)\nfoc_inject_rows_set = set(\n    NAME2ROW[n]\n    for n in model_meta.loc[foc_inject_mask_global, \"model_name\"]\n    if n in NAME2ROW\n)\n\nfoc_is_injectable = np.array([r in foc_inject_rows_set for r in foc_rows])\n\nprint(f\"  ref={len(ref_rows)}, foc={len(foc_rows)}, \"\n      f\"foc_inject={foc_is_injectable.sum()}\")\nprint(f\"  Load time: {time.time()-t0:.1f}s\")\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  BOOTSTRAP\n# ═══════════════════════════════════════════════════════════════════════\nprint(f\"\\n=== Bootstrap ΔFPR ({N_BOOT} resamples per subject) ===\")\n\nall_results = []\nall_boot_rows = []\n\nfor subj_name in SUBJECTS:\n    t_subj = time.time()\n\n    subj_items = item_meta[item_meta[\"subject\"] == subj_name][\"item_id\"].values\n    subj_cols = np.array([ITEM2COL[iid] for iid in subj_items\n                          if iid in ITEM2COL])\n    n_items = len(subj_cols)\n    n_contam = max(1, int(n_items * CONTAM_FRAC))\n    n_baseline = n_items - n_contam\n    n_strata = 3 if n_items < 100 else N_STRATA_DEFAULT\n\n    X_subj = mat[:, subj_cols].toarray().astype(np.int8)\n    X_ref = X_subj[ref_rows]\n    X_foc_all = X_subj[foc_rows]\n\n    subj_items_set = set(subj_items.tolist())\n    other_cols = np.array([ITEM2COL[iid] for iid in ITEM_IDS\n                           if iid in ITEM2COL and iid not in subj_items_set])\n    cross_ref = np.asarray(\n        mat[ref_rows][:, other_cols].sum(axis=1)\n    ).ravel().astype(np.float64)\n    cross_foc_all = np.asarray(\n        mat[foc_rows][:, other_cols].sum(axis=1)\n    ).ravel().astype(np.float64)\n\n    rng_contam = np.random.RandomState(CONTAM_SEED)\n    contam_local_idx = rng_contam.choice(n_items, n_contam, replace=False)\n    contam_set = set(contam_local_idx.tolist())\n    clean_idx = np.array([j for j in range(n_items) if j not in contam_set])\n\n    print(f\"\\n  {subj_name}: {n_items} items, {n_contam} contam, \"\n          f\"{n_baseline} clean, {n_strata} strata\")\n\n    fpr_p0_arr = np.empty(N_BOOT)\n    fpr_p1_arr = np.empty(N_BOOT)\n    delta_fpr_arr = np.empty(N_BOOT)\n\n    for b in range(N_BOOT):\n        rng_boot = np.random.RandomState(10000 + b)\n        boot_idx = rng_boot.choice(len(foc_rows), len(foc_rows), replace=True)\n\n        X_foc_b = X_foc_all[boot_idx]\n        cross_foc_b = cross_foc_all[boot_idx]\n        injectable_b = foc_is_injectable[boot_idx]\n\n        # p = 0 (baseline, no injection)\n        ets_0 = cross_mh_ets(X_ref, X_foc_b, cross_ref, cross_foc_b,\n                             n_strata=n_strata,\n                             min_per_stratum=MIN_PER_STRATUM)\n        fpr_0 = (ets_0[clean_idx] == \"C\").sum() / n_baseline\n\n        # p = 1 (maximum injection on contaminated items)\n        X_foc_b_inj = X_foc_b.copy()\n        for local_j in contam_local_idx:\n            mask = injectable_b & (X_foc_b_inj[:, local_j] == 0)\n            X_foc_b_inj[mask, local_j] = 1\n\n        ets_1 = cross_mh_ets(X_ref, X_foc_b_inj, cross_ref, cross_foc_b,\n                             n_strata=n_strata,\n                             min_per_stratum=MIN_PER_STRATUM)\n        fpr_1 = (ets_1[clean_idx] == \"C\").sum() / n_baseline\n\n        fpr_p0_arr[b] = fpr_0\n        fpr_p1_arr[b] = fpr_1\n        delta_fpr_arr[b] = fpr_1 - fpr_0\n\n        all_boot_rows.append(dict(\n            subject=subj_name, boot_id=b,\n            fpr_p0=fpr_0, fpr_p1=fpr_1,\n            delta_fpr=fpr_1 - fpr_0,\n        ))\n\n        if (b + 1) % 250 == 0:\n            elapsed = time.time() - t_subj\n            print(f\"    [{b+1}/{N_BOOT}] elapsed {elapsed:.0f}s\")\n\n    elapsed = time.time() - t_subj\n    n_nonzero = int((delta_fpr_arr != 0.0).sum())\n\n    result = dict(\n        subject=subj_name,\n        n_items=n_items,\n        n_contam=n_contam,\n        n_baseline=n_baseline,\n        n_boot=N_BOOT,\n        fpr_p0_mean=float(fpr_p0_arr.mean()),\n        fpr_p0_se=float(fpr_p0_arr.std()),\n        fpr_p0_ci_lo=float(np.percentile(fpr_p0_arr, 2.5)),\n        fpr_p0_ci_hi=float(np.percentile(fpr_p0_arr, 97.5)),\n        fpr_p1_mean=float(fpr_p1_arr.mean()),\n        fpr_p1_se=float(fpr_p1_arr.std()),\n        fpr_p1_ci_lo=float(np.percentile(fpr_p1_arr, 2.5)),\n        fpr_p1_ci_hi=float(np.percentile(fpr_p1_arr, 97.5)),\n        delta_fpr_point=0.000,\n        delta_fpr_mean=float(delta_fpr_arr.mean()),\n        delta_fpr_se=float(delta_fpr_arr.std()),\n        delta_fpr_ci_lo=float(np.percentile(delta_fpr_arr, 2.5)),\n        delta_fpr_ci_hi=float(np.percentile(delta_fpr_arr, 97.5)),\n        n_nonzero_delta=n_nonzero,\n        elapsed_s=elapsed,\n    )\n    all_results.append(result)\n\n    print(f\"  {subj_name} done ({elapsed:.0f}s)\")\n    print(f\"    FPR(p=0): {result['fpr_p0_mean']:.4f} \"\n          f\"[{result['fpr_p0_ci_lo']:.4f}, {result['fpr_p0_ci_hi']:.4f}]\")\n    print(f\"    FPR(p=1): {result['fpr_p1_mean']:.4f} \"\n          f\"[{result['fpr_p1_ci_lo']:.4f}, {result['fpr_p1_ci_hi']:.4f}]\")\n    print(f\"    ΔFPR:     {result['delta_fpr_mean']:.6f} \"\n          f\"[{result['delta_fpr_ci_lo']:.6f}, {result['delta_fpr_ci_hi']:.6f}] \"\n          f\"SE={result['delta_fpr_se']:.6f}  nonzero={n_nonzero}/{N_BOOT}\")\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  SAVE\n# ═══════════════════════════════════════════════════════════════════════\nresults_df = pd.DataFrame(all_results)\nresults_df.to_csv(OUT / \"bootstrap_dfpr_results.csv\", index=False)\n\nboot_df = pd.DataFrame(all_boot_rows)\nboot_df.to_csv(OUT / \"bootstrap_dfpr_samples.csv\", index=False)\n\nprint(f\"\\n=== Saved results to {OUT} ===\")\nprint(f\"  bootstrap_dfpr_results.csv  ({len(results_df)} rows)\")\nprint(f\"  bootstrap_dfpr_samples.csv  ({len(boot_df)} rows)\")\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  REPORT\n# ═══════════════════════════════════════════════════════════════════════\nL = []\n\n\ndef w(s=\"\"):\n    L.append(s)\n\n\nw(\"# Bootstrap CI for ΔFPR: Cross-Subject Matching\")\nw()\nw(\"## Motivation\")\nw()\nw(\"Plan 016 found ΔFPR = 0.000 for cross-subject matching across all 5\")\nw(\"subjects—the false positive rate on clean items was perfectly stable\")\nw(\"regardless of injection intensity (p = 0 vs p = 1). A reviewer flagged\")\nw(\"this as suspiciously perfect. This supplement provides bootstrap\")\nw(\"confidence intervals to demonstrate that the zero is not a statistical\")\nw(\"fluke but a structural invariant of cross-subject matching.\")\nw()\nw(\"## Method\")\nw()\nw(f\"- **Bootstrap resamples**: B = {N_BOOT} per subject\")\nw(f\"- **Resampling unit**: focal cohort models (2024, N = {len(foc_rows)}), \"\n  \"with replacement\")\nw(\"- **Reference cohort**: held fixed (2023 models)\")\nw(f\"- **Contamination**: 20% of items, fixed seed = {CONTAM_SEED}, \"\n  \"p ∈ {0.0, 1.0}\")\nw(\"- **Matching**: cross-subject total score (items from all other subjects)\")\nw(\"- **Metric**: FPR = proportion of clean (non-contaminated) items \"\n  \"classified ETS-C\")\nw(\"- **ΔFPR** = FPR(p = 1) − FPR(p = 0)\")\nw()\n\nw(\"## Results\")\nw()\nw(\"### ΔFPR Bootstrap Distribution\")\nw()\nw(\"| Subject | ΔFPR point | ΔFPR mean | Bootstrap SE | \"\n  \"95% CI | Non-zero |\")\nw(\"|---------|-----------|-----------|-------------|\"\n  \"-------|----------|\")\nfor r in all_results:\n    w(f\"| {r['subject']} | {r['delta_fpr_point']:.3f} | \"\n      f\"{r['delta_fpr_mean']:.4f} | {r['delta_fpr_se']:.4f} | \"\n      f\"[{r['delta_fpr_ci_lo']:.4f}, {r['delta_fpr_ci_hi']:.4f}] | \"\n      f\"{r['n_nonzero_delta']}/{r['n_boot']} |\")\nw()\n\nw(\"### Baseline FPR (p = 0) Bootstrap Distribution\")\nw()\nw(\"| Subject | N clean | FPR mean | Bootstrap SE | 95% CI |\")\nw(\"|---------|---------|----------|-------------|--------|\")\nfor r in all_results:\n    w(f\"| {r['subject']} | {r['n_baseline']} | \"\n      f\"{r['fpr_p0_mean']:.4f} | {r['fpr_p0_se']:.4f} | \"\n      f\"[{r['fpr_p0_ci_lo']:.4f}, {r['fpr_p0_ci_hi']:.4f}] |\")\nw()\n\nw(\"### FPR Under Injection (p = 1) Bootstrap Distribution\")\nw()\nw(\"| Subject | FPR mean | Bootstrap SE | 95% CI |\")\nw(\"|---------|----------|-------------|--------|\")\nfor r in all_results:\n    w(f\"| {r['subject']} | {r['fpr_p1_mean']:.4f} | \"\n      f\"{r['fpr_p1_se']:.4f} | \"\n      f\"[{r['fpr_p1_ci_lo']:.4f}, {r['fpr_p1_ci_hi']:.4f}] |\")\nw()\n\nw(\"## Why ΔFPR = 0 Is Algebraically Guaranteed\")\nw()\nw(\"The zero is not a coincidence. It follows from the design of\")\nw(\"cross-subject matching by a simple algebraic argument:\")\nw()\nw(\"1. **Injection scope**: only contaminated items in the current subject\")\nw(\"   have responses flipped (incorrect → correct for focal inject models).\")\nw(\"2. **Clean item responses are invariant**: FPR is computed on clean\")\nw(\"   (non-contaminated) items. Their responses are identical at p = 0 and\")\nw(\"   p = 1 because injection never touches them.\")\nw(\"3. **Cross-subject scores are invariant**: the stratification variable\")\nw(\"   sums responses over all *other* subjects' items. Since injection only\")\nw(\"   modifies the *current* subject, these scores are identical at p = 0\")\nw(\"   and p = 1.\")\nw(\"4. **Identical inputs ⇒ identical outputs**: with the same item\")\nw(\"   responses and the same stratification, MH statistics for each clean\")\nw(\"   item are numerically identical. Therefore ETS classifications are\")\nw(\"   identical, and FPR(p = 1) = FPR(p = 0) exactly.\")\nw()\nw(\"This holds for *any* bootstrap sample of models, not just the original\")\nw(\"sample. The bootstrap confirms: across 1000 resamples per subject,\")\nw(\"ΔFPR = 0.000 in every single iteration.\")\nw()\nw(\"By contrast, within-subject matching uses a purified total on the\")\nw(\"*current* subject's items. When contaminated items are flipped, the\")\nw(\"purified total changes for focal models, shifting stratum assignments\")\nw(\"and causing FPR inflation on clean items. This is why within-subject\")\nw(\"ΔFPR > 0 under injection.\")\nw()\n\nw(\"## Conclusion\")\nw()\nw(\"The ΔFPR = 0.000 finding is a structural property of cross-subject\")\nw(\"matching, confirmed by B = 1000 bootstrap resamples with SE = 0.000\")\nw(\"and 95% CI = [0.000, 0.000] for all 5 subjects. The baseline FPR\")\nw(\"itself varies across bootstrap samples (reflecting model sampling\")\nw(\"variability), but ΔFPR remains exactly zero because injection cannot\")\nw(\"affect the inputs to the DIF computation for clean items under\")\nw(\"cross-subject stratification.\")\nw()\n\ntotal_time = time.time() - t0\nw(f\"*Generated: {N_BOOT} bootstrap resamples × 5 subjects, \"\n  f\"total runtime {total_time:.0f}s*\")\n\nreport_text = \"\\n\".join(L) + \"\\n\"\n(OUT / \"bootstrap_dfpr_report.md\").write_text(report_text)\n\nprint(f\"\\n  bootstrap_dfpr_report.md written\")\nprint(f\"\\nTotal time: {time.time()-t0:.0f}s\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement/bootstrap_dfpr.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nplan_016_supplement: Bootstrap CI for ΔFPR in Cross-Subject Matching\n\nAddresses reviewer concern that ΔFPR = 0.000 across all 5 subjects is \"too\nperfect\". Resamples focal cohort models (with replacement) 1000 times per\nsubject, re-running cross-subject MH-DIF at p=0 (baseline) and p=1 (max\ninjection) to quantify the sampling distribution of ΔFPR.\n\nAlgebraic note: For cross-subject matching, ΔFPR = 0 is guaranteed because\n(1) clean item responses are unchanged by injection, and (2) cross-subject\nstratification scores are independent of injected items. The bootstrap\nconfirms this algebraic invariant empirically.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.sparse import load_npz\nfrom scipy.stats import chi2 as chi2_dist\nfrom pathlib import Path\nimport time\nimport warnings\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/\"\n            \"irt_equated_bench_regen/artifacts\")\nOUT = BASE / \"plan_016_supplement\"\nOUT.mkdir(exist_ok=True)\n\nSUBJECTS = [\"business_ethics\", \"human_aging\", \"professional_medicine\",\n            \"formal_logic\", \"high_school_statistics\"]\nN_BOOT = 1000\nCONTAM_FRAC = 0.20\nCONTAM_SEED = 1\nN_STRATA_DEFAULT = 5\nMIN_PER_STRATUM = 5\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  MH-DIF helpers (from plan_016, optimised for cross-subject matching)\n# ═══════════════════════════════════════════════════════════════════════\n\ndef _merge_small_strata(k_all, groups_all, n_bins, min_n):\n    labels = k_all.copy()\n    merged = True\n    while merged:\n        merged = False\n        unique_strata = sorted(np.unique(labels))\n        for i, k in enumerate(unique_strata):\n            mask_k = (labels == k)\n            n_ref = int((mask_k & (groups_all == 0)).sum())\n            n_foc = int((mask_k & (groups_all == 1)).sum())\n            if n_ref < min_n or n_foc < min_n:\n                if i + 1 < len(unique_strata):\n                    labels[labels == unique_strata[i + 1]] = k\n                elif i > 0:\n                    labels[labels == k] = unique_strata[i - 1]\n                merged = True\n                break\n    return labels\n\n\ndef cross_mh_ets(X_ref, X_foc, scores_ref, scores_foc,\n                 n_strata=5, min_per_stratum=5):\n    \"\"\"Cross-subject MH-DIF returning ETS class per item.\n\n    Optimised: strata are computed once (external scores are item-invariant).\n    \"\"\"\n    J = X_ref.shape[1]\n    n_ref_models = len(scores_ref)\n\n    s_all = np.concatenate([scores_ref, scores_foc])\n    groups_all = np.concatenate([np.zeros(n_ref_models),\n                                 np.ones(len(scores_foc))])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    if len(edges) < 2:\n        return np.array([\"A\"] * J)\n\n    k_all = np.digitize(s_all, edges[1:-1])\n    strata = _merge_small_strata(k_all, groups_all,\n                                 len(edges) - 1, min_per_stratum)\n\n    stratum_info = []\n    for k in np.unique(strata):\n        mask_k = (strata == k)\n        mask_ref = mask_k[:n_ref_models]\n        mask_foc = mask_k[n_ref_models:]\n        n1 = int(mask_ref.sum())\n        n0 = int(mask_foc.sum())\n        if n1 > 0 and n0 > 0:\n            stratum_info.append((mask_ref, mask_foc, float(n1), float(n0)))\n\n    ets_classes = np.empty(J, dtype=\"U1\")\n\n    for j in range(J):\n        x_ref_j = X_ref[:, j].astype(np.float64)\n        x_foc_j = X_foc[:, j].astype(np.float64)\n\n        R = S = sum_diff = sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        for mask_ref, mask_foc, n1, n0 in stratum_info:\n            A = float(x_ref_j[mask_ref].sum())\n            B = n1 - A\n            C = float(x_foc_j[mask_foc].sum())\n            D = n0 - C\n            Nk = n1 + n0\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            ets_classes[j] = \"A\"\n            continue\n\n        if S == 0:\n            delta = -np.inf\n        elif R == 0:\n            delta = np.inf\n        else:\n            delta = -2.35 * np.log(R / S)\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else np.inf\n        if ad < 1.0:\n            ets_classes[j] = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets_classes[j] = \"C\"\n        else:\n            ets_classes[j] = \"B\"\n\n    return ets_classes\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ═══════════════════════════════════════════════════════════════════════\nprint(\"=== Loading data ===\")\nt0 = time.time()\n\nmat = load_npz(BASE / \"response_matrix.npz\")\nidx = np.load(BASE / \"response_matrix_index.npz\", allow_pickle=True)\nMODEL_NAMES = idx[\"model_names\"]\nITEM_IDS = idx[\"item_ids\"]\nITEM2COL = {iid: i for i, iid in enumerate(ITEM_IDS)}\n\nmodel_meta = pd.read_csv(BASE / \"model_metadata.csv\")\nitem_meta = pd.read_csv(BASE / \"item_metadata.csv\")\nNAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}\n\nref_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"model_name\"]\nfoc_names = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"model_name\"]\nref_rows = np.array([NAME2ROW[n] for n in ref_names if n in NAME2ROW])\nfoc_rows = np.array([NAME2ROW[n] for n in foc_names if n in NAME2ROW])\n\nref_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2023\", \"accuracy\"]\nfoc_acc = model_meta.loc[model_meta[\"cohort_temporal\"] == \"2024\", \"accuracy\"]\nt_overlap_min = max(ref_acc.min(), foc_acc.min())\nt_overlap_max = min(ref_acc.max(), foc_acc.max())\n\nfoc_inject_mask_global = (\n    (model_meta[\"cohort_temporal\"] == \"2024\")\n    & (model_meta[\"accuracy\"] >= t_overlap_min)\n    & (model_meta[\"accuracy\"] <= t_overlap_max)\n)\nfoc_inject_rows_set = set(\n    NAME2ROW[n]\n    for n in model_meta.loc[foc_inject_mask_global, \"model_name\"]\n    if n in NAME2ROW\n)\n\nfoc_is_injectable = np.array([r in foc_inject_rows_set for r in foc_rows])\n\nprint(f\"  ref={len(ref_rows)}, foc={len(foc_rows)}, \"\n      f\"foc_inject={foc_is_injectable.sum()}\")\nprint(f\"  Load time: {time.time()-t0:.1f}s\")\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  BOOTSTRAP\n# ═══════════════════════════════════════════════════════════════════════\nprint(f\"\\n=== Bootstrap ΔFPR ({N_BOOT} resamples per subject) ===\")\n\nall_results = []\nall_boot_rows = []\n\nfor subj_name in SUBJECTS:\n    t_subj = time.time()\n\n    subj_items = item_meta[item_meta[\"subject\"] == subj_name][\"item_id\"].values\n    subj_cols = np.array([ITEM2COL[iid] for iid in subj_items\n                          if iid in ITEM2COL])\n    n_items = len(subj_cols)\n    n_contam = max(1, int(n_items * CONTAM_FRAC))\n    n_baseline = n_items - n_contam\n    n_strata = 3 if n_items < 100 else N_STRATA_DEFAULT\n\n    X_subj = mat[:, subj_cols].toarray().astype(np.int8)\n    X_ref = X_subj[ref_rows]\n    X_foc_all = X_subj[foc_rows]\n\n    subj_items_set = set(subj_items.tolist())\n    other_cols = np.array([ITEM2COL[iid] for iid in ITEM_IDS\n                           if iid in ITEM2COL and iid not in subj_items_set])\n    cross_ref = np.asarray(\n        mat[ref_rows][:, other_cols].sum(axis=1)\n    ).ravel().astype(np.float64)\n    cross_foc_all = np.asarray(\n        mat[foc_rows][:, other_cols].sum(axis=1)\n    ).ravel().astype(np.float64)\n\n    rng_contam = np.random.RandomState(CONTAM_SEED)\n    contam_local_idx = rng_contam.choice(n_items, n_contam, replace=False)\n    contam_set = set(contam_local_idx.tolist())\n    clean_idx = np.array([j for j in range(n_items) if j not in contam_set])\n\n    print(f\"\\n  {subj_name}: {n_items} items, {n_contam} contam, \"\n          f\"{n_baseline} clean, {n_strata} strata\")\n\n    fpr_p0_arr = np.empty(N_BOOT)\n    fpr_p1_arr = np.empty(N_BOOT)\n    delta_fpr_arr = np.empty(N_BOOT)\n\n    for b in range(N_BOOT):\n        rng_boot = np.random.RandomState(10000 + b)\n        boot_idx = rng_boot.choice(len(foc_rows), len(foc_rows), replace=True)\n\n        X_foc_b = X_foc_all[boot_idx]\n        cross_foc_b = cross_foc_all[boot_idx]\n        injectable_b = foc_is_injectable[boot_idx]\n\n        # p = 0 (baseline, no injection)\n        ets_0 = cross_mh_ets(X_ref, X_foc_b, cross_ref, cross_foc_b,\n                             n_strata=n_strata,\n                             min_per_stratum=MIN_PER_STRATUM)\n        fpr_0 = (ets_0[clean_idx] == \"C\").sum() / n_baseline\n\n        # p = 1 (maximum injection on contaminated items)\n        X_foc_b_inj = X_foc_b.copy()\n        for local_j in contam_local_idx:\n            mask = injectable_b & (X_foc_b_inj[:, local_j] == 0)\n            X_foc_b_inj[mask, local_j] = 1\n\n        ets_1 = cross_mh_ets(X_ref, X_foc_b_inj, cross_ref, cross_foc_b,\n                             n_strata=n_strata,\n                             min_per_stratum=MIN_PER_STRATUM)\n        fpr_1 = (ets_1[clean_idx] == \"C\").sum() / n_baseline\n\n        fpr_p0_arr[b] = fpr_0\n        fpr_p1_arr[b] = fpr_1\n        delta_fpr_arr[b] = fpr_1 - fpr_0\n\n        all_boot_rows.append(dict(\n            subject=subj_name, boot_id=b,\n            fpr_p0=fpr_0, fpr_p1=fpr_1,\n            delta_fpr=fpr_1 - fpr_0,\n        ))\n\n        if (b + 1) % 250 == 0:\n            elapsed = time.time() - t_subj\n            print(f\"    [{b+1}/{N_BOOT}] elapsed {elapsed:.0f}s\")\n\n    elapsed = time.time() - t_subj\n    n_nonzero = int((delta_fpr_arr != 0.0).sum())\n\n    result = dict(\n        subject=subj_name,\n        n_items=n_items,\n        n_contam=n_contam,\n        n_baseline=n_baseline,\n        n_boot=N_BOOT,\n        fpr_p0_mean=float(fpr_p0_arr.mean()),\n        fpr_p0_se=float(fpr_p0_arr.std()),\n        fpr_p0_ci_lo=float(np.percentile(fpr_p0_arr, 2.5)),\n        fpr_p0_ci_hi=float(np.percentile(fpr_p0_arr, 97.5)),\n        fpr_p1_mean=float(fpr_p1_arr.mean()),\n        fpr_p1_se=float(fpr_p1_arr.std()),\n        fpr_p1_ci_lo=float(np.percentile(fpr_p1_arr, 2.5)),\n        fpr_p1_ci_hi=float(np.percentile(fpr_p1_arr, 97.5)),\n        delta_fpr_point=0.000,\n        delta_fpr_mean=float(delta_fpr_arr.mean()),\n        delta_fpr_se=float(delta_fpr_arr.std()),\n        delta_fpr_ci_lo=float(np.percentile(delta_fpr_arr, 2.5)),\n        delta_fpr_ci_hi=float(np.percentile(delta_fpr_arr, 97.5)),\n        n_nonzero_delta=n_nonzero,\n        elapsed_s=elapsed,\n    )\n    all_results.append(result)\n\n    print(f\"  {subj_name} done ({elapsed:.0f}s)\")\n    print(f\"    FPR(p=0): {result['fpr_p0_mean']:.4f} \"\n          f\"[{result['fpr_p0_ci_lo']:.4f}, {result['fpr_p0_ci_hi']:.4f}]\")\n    print(f\"    FPR(p=1): {result['fpr_p1_mean']:.4f} \"\n          f\"[{result['fpr_p1_ci_lo']:.4f}, {result['fpr_p1_ci_hi']:.4f}]\")\n    print(f\"    ΔFPR:     {result['delta_fpr_mean']:.6f} \"\n          f\"[{result['delta_fpr_ci_lo']:.6f}, {result['delta_fpr_ci_hi']:.6f}] \"\n          f\"SE={result['delta_fpr_se']:.6f}  nonzero={n_nonzero}/{N_BOOT}\")\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  SAVE\n# ═══════════════════════════════════════════════════════════════════════\nresults_df = pd.DataFrame(all_results)\nresults_df.to_csv(OUT / \"bootstrap_dfpr_results.csv\", index=False)\n\nboot_df = pd.DataFrame(all_boot_rows)\nboot_df.to_csv(OUT / \"bootstrap_dfpr_samples.csv\", index=False)\n\nprint(f\"\\n=== Saved results to {OUT} ===\")\nprint(f\"  bootstrap_dfpr_results.csv  ({len(results_df)} rows)\")\nprint(f\"  bootstrap_dfpr_samples.csv  ({len(boot_df)} rows)\")\n\n\n# ═══════════════════════════════════════════════════════════════════════\n#  REPORT\n# ═══════════════════════════════════════════════════════════════════════\nL = []\n\n\ndef w(s=\"\"):\n    L.append(s)\n\n\nw(\"# Bootstrap CI for ΔFPR: Cross-Subject Matching\")\nw()\nw(\"## Motivation\")\nw()\nw(\"Plan 016 found ΔFPR = 0.000 for cross-subject matching across all 5\")\nw(\"subjects—the false positive rate on clean items was perfectly stable\")\nw(\"regardless of injection intensity (p = 0 vs p = 1). A reviewer flagged\")\nw(\"this as suspiciously perfect. This supplement provides bootstrap\")\nw(\"confidence intervals to demonstrate that the zero is not a statistical\")\nw(\"fluke but a structural invariant of cross-subject matching.\")\nw()\nw(\"## Method\")\nw()\nw(f\"- **Bootstrap resamples**: B = {N_BOOT} per subject\")\nw(f\"- **Resampling unit**: focal cohort models (2024, N = {len(foc_rows)}), \"\n  \"with replacement\")\nw(\"- **Reference cohort**: held fixed (2023 models)\")\nw(f\"- **Contamination**: 20% of items, fixed seed = {CONTAM_SEED}, \"\n  \"p ∈ {0.0, 1.0}\")\nw(\"- **Matching**: cross-subject total score (items from all other subjects)\")\nw(\"- **Metric**: FPR = proportion of clean (non-contaminated) items \"\n  \"classified ETS-C\")\nw(\"- **ΔFPR** = FPR(p = 1) − FPR(p = 0)\")\nw()\n\nw(\"## Results\")\nw()\nw(\"### ΔFPR Bootstrap Distribution\")\nw()\nw(\"| Subject | ΔFPR point | ΔFPR mean | Bootstrap SE | \"\n  \"95% CI | Non-zero |\")\nw(\"|---------|-----------|-----------|-------------|\"\n  \"-------|----------|\")\nfor r in all_results:\n    w(f\"| {r['subject']} | {r['delta_fpr_point']:.3f} | \"\n      f\"{r['delta_fpr_mean']:.4f} | {r['delta_fpr_se']:.4f} | \"\n      f\"[{r['delta_fpr_ci_lo']:.4f}, {r['delta_fpr_ci_hi']:.4f}] | \"\n      f\"{r['n_nonzero_delta']}/{r['n_boot']} |\")\nw()\n\nw(\"### Baseline FPR (p = 0) Bootstrap Distribution\")\nw()\nw(\"| Subject | N clean | FPR mean | Bootstrap SE | 95% CI |\")\nw(\"|---------|---------|----------|-------------|--------|\")\nfor r in all_results:\n    w(f\"| {r['subject']} | {r['n_baseline']} | \"\n      f\"{r['fpr_p0_mean']:.4f} | {r['fpr_p0_se']:.4f} | \"\n      f\"[{r['fpr_p0_ci_lo']:.4f}, {r['fpr_p0_ci_hi']:.4f}] |\")\nw()\n\nw(\"### FPR Under Injection (p = 1) Bootstrap Distribution\")\nw()\nw(\"| Subject | FPR mean | Bootstrap SE | 95% CI |\")\nw(\"|---------|----------|-------------|--------|\")\nfor r in all_results:\n    w(f\"| {r['subject']} | {r['fpr_p1_mean']:.4f} | \"\n      f\"{r['fpr_p1_se']:.4f} | \"\n      f\"[{r['fpr_p1_ci_lo']:.4f}, {r['fpr_p1_ci_hi']:.4f}] |\")\nw()\n\nw(\"## Why ΔFPR = 0 Is Algebraically Guaranteed\")\nw()\nw(\"The zero is not a coincidence. It follows from the design of\")\nw(\"cross-subject matching by a simple algebraic argument:\")\nw()\nw(\"1. **Injection scope**: only contaminated items in the current subject\")\nw(\"   have responses flipped (incorrect → correct for focal inject models).\")\nw(\"2. **Clean item responses are invariant**: FPR is computed on clean\")\nw(\"   (non-contaminated) items. Their responses are identical at p = 0 and\")\nw(\"   p = 1 because injection never touches them.\")\nw(\"3. **Cross-subject scores are invariant**: the stratification variable\")\nw(\"   sums responses over all *other* subjects' items. Since injection only\")\nw(\"   modifies the *current* subject, these scores are identical at p = 0\")\nw(\"   and p = 1.\")\nw(\"4. **Identical inputs ⇒ identical outputs**: with the same item\")\nw(\"   responses and the same stratification, MH statistics for each clean\")\nw(\"   item are numerically identical. Therefore ETS classifications are\")\nw(\"   identical, and FPR(p = 1) = FPR(p = 0) exactly.\")\nw()\nw(\"This holds for *any* bootstrap sample of models, not just the original\")\nw(\"sample. The bootstrap confirms: across 1000 resamples per subject,\")\nw(\"ΔFPR = 0.000 in every single iteration.\")\nw()\nw(\"By contrast, within-subject matching uses a purified total on the\")\nw(\"*current* subject's items. When contaminated items are flipped, the\")\nw(\"purified total changes for focal models, shifting stratum assignments\")\nw(\"and causing FPR inflation on clean items. This is why within-subject\")\nw(\"ΔFPR > 0 under injection.\")\nw()\n\nw(\"## Conclusion\")\nw()\nw(\"The ΔFPR = 0.000 finding is a structural property of cross-subject\")\nw(\"matching, confirmed by B = 1000 bootstrap resamples with SE = 0.000\")\nw(\"and 95% CI = [0.000, 0.000] for all 5 subjects. The baseline FPR\")\nw(\"itself varies across bootstrap samples (reflecting model sampling\")\nw(\"variability), but ΔFPR remains exactly zero because injection cannot\")\nw(\"affect the inputs to the DIF computation for clean items under\")\nw(\"cross-subject stratification.\")\nw()\n\ntotal_time = time.time() - t0\nw(f\"*Generated: {N_BOOT} bootstrap resamples × 5 subjects, \"\n  f\"total runtime {total_time:.0f}s*\")\n\nreport_text = \"\\n\".join(L) + \"\\n\"\n(OUT / \"bootstrap_dfpr_report.md\").write_text(report_text)\n\nprint(f\"\\n  bootstrap_dfpr_report.md written\")\nprint(f\"\\nTotal time: {time.time()-t0:.0f}s\")\n"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T07:58:13.005394+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement/bootstrap_dfpr.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T07:58:13.005559+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python artifacts/plan_016_supplement/bootstrap_dfpr.py 2>&1",
  "description": "Run bootstrap ΔFPR analysis (1000 resamples × 5 subjects)",
  "timeout": "600000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "tool_args": {
    "command": "python artifacts/plan_016_supplement/bootstrap_dfpr.py 2>&1",
    "description": "Run bootstrap ΔFPR analysis (1000 resamples × 5 subjects)",
    "timeout": "600000"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T07:58:13.005695+00:00_

Exit code 127
/bin/bash: line 1: python: command not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T07:58:13.005870+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "which python3 && python3 --version",
  "description": "Find python3 path"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "tool_args": {
    "command": "which python3 && python3 --version",
    "description": "Find python3 path"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T07:58:13.005995+00:00_

/usr/bin/python3
Python 3.14.4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T07:58:13.006116+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 artifacts/plan_016_supplement/bootstrap_dfpr.py 2>&1",
  "description": "Run bootstrap ΔFPR analysis",
  "timeout": "600000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 artifacts/plan_016_supplement/bootstrap_dfpr.py 2>&1",
    "description": "Run bootstrap ΔFPR analysis",
    "timeout": "600000"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T07:58:13.006271+00:00_

=== Loading data ===
  ref=1080, foc=807, foc_inject=787
  Load time: 0.9s

=== Bootstrap ΔFPR (1000 resamples per subject) ===

  business_ethics: 93 items, 18 contam, 75 clean, 3 strata
    [250/1000] elapsed 9s
    [500/1000] elapsed 17s
    [750/1000] elapsed 24s
    [1000/1000] elapsed 32s
  business_ethics done (32s)
    FPR(p=0): 0.5282 [0.4667, 0.6000]
    FPR(p=1): 0.5282 [0.4667, 0.6000]
    ΔFPR:     0.000000 [0.000000, 0.000000] SE=0.000000  nonzero=0/1000

  human_aging: 203 items, 40 contam, 163 clean, 5 strata
    [250/1000] elapsed 20s
    [500/1000] elapsed 41s
    [750/1000] elapsed 59s
    [1000/1000] elapsed 78s
  human_aging done (78s)
    FPR(p=0): 0.4165 [0.3497, 0.4785]
    FPR(p=1): 0.4165 [0.3497, 0.4785]
    ΔFPR:     0.000000 [0.000000, 0.000000] SE=0.000000  nonzero=0/1000

  professional_medicine: 248 items, 49 contam, 199 clean, 5 strata
    [250/1000] elapsed 24s
    [500/1000] elapsed 49s
    [750/1000] elapsed 74s
    [1000/1000] elapsed 98s
  professional_medicine done (98s)
    FPR(p=0): 0.3992 [0.3417, 0.4523]
    FPR(p=1): 0.3992 [0.3417, 0.4523]
    ΔFPR:     0.000000 [0.000000, 0.000000] SE=0.000000  nonzero=0/1000

  formal_logic: 109 items, 21 contam, 88 clean, 5 strata
    [250/1000] elapsed 12s
    [500/1000] elapsed 23s
    [750/1000] elapsed 34s
    [1000/1000] elapsed 46s
  formal_logic done (46s)
    FPR(p=0): 0.3617 [0.3182, 0.3977]
    FPR(p=1): 0.3617 [0.3182, 0.3977]
    ΔFPR:     0.000000 [0.000000, 0.000000] SE=0.000000  nonzero=0/1000

  high_school_statistics: 181 items, 36 contam, 145 clean, 5 strata
    [250/1000] elapsed 18s
    [500/1000] elapsed 36s
    [750/1000] elapsed 53s
    [1000/1000] elapsed 70s
  high_school_statistics done (70s)
    FPR(p=0): 0.3491 [0.3034, 0.3931]
    FPR(p=1): 0.3491 [0.3034, 0.3931]
    ΔFPR:     0.000000 [0.000000, 0.000000] SE=0.000000  nonzero=0/1000

=== Saved results to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_su
…[truncated 147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T07:58:13.006430+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement/",
  "description": "Verify output files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement/",
    "description": "Verify output files"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-21T07:58:13.006556+00:00_

total 340
drwxr-xr-x  2 ubuntu ubuntu   4096 May 21 07:57 .
drwxr-xr-x 32 ubuntu ubuntu   4096 May 21 07:50 ..
-rw-r--r--  1 ubuntu ubuntu  18307 May 21 07:52 bootstrap_dfpr.py
-rw-r--r--  1 ubuntu ubuntu   4394 May 21 07:57 bootstrap_dfpr_report.md
-rw-r--r--  1 ubuntu ubuntu   1336 May 21 07:57 bootstrap_dfpr_results.csv
-rw-r--r--  1 ubuntu ubuntu 304334 May 21 07:57 bootstrap_dfpr_samples.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-21T07:58:13.006681+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement/bootstrap_dfpr_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement/bootstrap_dfpr_report.md"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-21T07:58:13.006882+00:00_

1	# Bootstrap CI for ΔFPR: Cross-Subject Matching
2	
3	## Motivation
4	
5	Plan 016 found ΔFPR = 0.000 for cross-subject matching across all 5
6	subjects—the false positive rate on clean items was perfectly stable
7	regardless of injection intensity (p = 0 vs p = 1). A reviewer flagged
8	this as suspiciously perfect. This supplement provides bootstrap
9	confidence intervals to demonstrate that the zero is not a statistical
10	fluke but a structural invariant of cross-subject matching.
11	
12	## Method
13	
14	- **Bootstrap resamples**: B = 1000 per subject
15	- **Resampling unit**: focal cohort models (2024, N = 807), with replacement
16	- **Reference cohort**: held fixed (2023 models)
17	- **Contamination**: 20% of items, fixed seed = 1, p ∈ {0.0, 1.0}
18	- **Matching**: cross-subject total score (items from all other subjects)
19	- **Metric**: FPR = proportion of clean (non-contaminated) items classified ETS-C
20	- **ΔFPR** = FPR(p = 1) − FPR(p = 0)
21	
22	## Results
23	
24	### ΔFPR Bootstrap Distribution
25	
26	| Subject | ΔFPR point | ΔFPR mean | Bootstrap SE | 95% CI | Non-zero |
27	|---------|-----------|-----------|-------------|-------|----------|
28	| business_ethics | 0.000 | 0.0000 | 0.0000 | [0.0000, 0.0000] | 0/1000 |
29	| human_aging | 0.000 | 0.0000 | 0.0000 | [0.0000, 0.0000] | 0/1000 |
30	| professional_medicine | 0.000 | 0.0000 | 0.0000 | [0.0000, 0.0000] | 0/1000 |
31	| formal_logic | 0.000 | 0.0000 | 0.0000 | [0.0000, 0.0000] | 0/1000 |
32	| high_school_statistics | 0.000 | 0.0000 | 0.0000 | [0.0000, 0.0000] | 0/1000 |
33	
34	### Baseline FPR (p = 0) Bootstrap Distribution
35	
36	| Subject | N clean | FPR mean | Bootstrap SE | 95% CI |
37	|---------|---------|----------|-------------|--------|
38	| business_ethics | 75 | 0.5282 | 0.0372 | [0.4667, 0.6000] |
39	| human_aging | 163 | 0.4165 | 0.0328 | [0.3497, 0.4785] |
40	| professional_medicine | 199 | 0.3992 | 0.0287 | [0.3417, 0.4523] |
41	| formal_logic | 88 | 0.3617 | 0.0218 | [0.3182, 0.3977] 
…[truncated 2645 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-21T07:58:13.007048+00:00_

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
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
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

_source line 58 · 2026-05-21T07:58:13.007173+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-21T07:58:13.007298+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "plan_016_supplement_bootstrap_dfpr_code",
  "type": "intermediate",
  "description": "Bootstrap CI script for ΔFPR in cross-subject matching (1000 resamples × 5 subjects)",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement/bootstrap_dfpr.py",
  "tags": "['plan_016', 'bootstrap', 'ΔFPR', 'cross-subject-matching']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "plan_016_supplement_bootstrap_dfpr_code",
    "type": "intermediate",
    "description": "Bootstrap CI script for ΔFPR in cross-subject matching (1000 resamples × 5 subjects)",
    "project": "irt_equated_bench_regen",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement/bootstrap_dfpr.py",
    "tags": "['plan_016', 'bootstrap', 'ΔFPR', 'cross-subject-matching']"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-21T07:58:13.007641+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_fec8b2\", \"name\": \"plan_016_supplement_bootstrap_dfpr_code\", \"type\": \"intermediate\", \"description\": \"Bootstrap CI script for ΔFPR in cross-subject matching (1000 resamples × 5 subjects)\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/intermediate/bootstrap_dfpr.py\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T07:57:56.560796+00:00\", \"tags\": [\"plan_016\", \"bootstrap\", \"ΔFPR\", \"cross-subject-matching\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-21T07:58:13.007839+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "plan_016_supplement_bootstrap_dfpr_report",
  "type": "report",
  "description": "Bootstrap CI results for ΔFPR: confirms ΔFPR=0.000 with SE=0 and CI=[0,0] across all 5 subjects (structural invariant, not fluke)",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement/bootstrap_dfpr_report.md",
  "tags": "['plan_016', 'bootstrap', 'ΔFPR', 'cross-subject-matching', 'reviewer-response']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "plan_016_supplement_bootstrap_dfpr_report",
    "type": "report",
    "description": "Bootstrap CI results for ΔFPR: confirms ΔFPR=0.000 with SE=0 and CI=[0,0] across all 5 subjects (structural invariant, not fluke)",
    "project": "irt_equated_bench_regen",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement/bootstrap_dfpr_report.md",
    "tags": "['plan_016', 'bootstrap', 'ΔFPR', 'cross-subject-matching', 'reviewer-response']"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-21T07:58:13.008004+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_65e0f2\", \"name\": \"plan_016_supplement_bootstrap_dfpr_report\", \"type\": \"report\", \"description\": \"Bootstrap CI results for ΔFPR: confirms ΔFPR=0.000 with SE=0 and CI=[0,0] across all 5 subjects (structural invariant, not fluke)\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/report/bootstrap_dfpr_report.md\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T07:57:59.094507+00:00\", \"tags\": [\"plan_016\", \"bootstrap\", \"ΔFPR\", \"cross-subject-matching\", \"reviewer-response\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-21T07:58:13.008171+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "plan_016_supplement_bootstrap_dfpr_results",
  "type": "data",
  "description": "Per-subject bootstrap summary: ΔFPR point/mean/SE/CI, baseline FPR distribution stats",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement/bootstrap_dfpr_results.csv",
  "tags": "['plan_016', 'bootstrap', 'ΔFPR']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "plan_016_supplement_bootstrap_dfpr_results",
    "type": "data",
    "description": "Per-subject bootstrap summary: ΔFPR point/mean/SE/CI, baseline FPR distribution stats",
    "project": "irt_equated_bench_regen",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement/bootstrap_dfpr_results.csv",
    "tags": "['plan_016', 'bootstrap', 'ΔFPR']"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-21T07:58:13.008336+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_5e25e6\", \"name\": \"plan_016_supplement_bootstrap_dfpr_results\", \"type\": \"data\", \"description\": \"Per-subject bootstrap summary: ΔFPR point/mean/SE/CI, baseline FPR distribution stats\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/data/bootstrap_dfpr_results.csv\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T07:58:01.353128+00:00\", \"tags\": [\"plan_016\", \"bootstrap\", \"ΔFPR\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-21T07:58:13.008479+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "plan_016_supplement_bootstrap_dfpr_samples",
  "type": "data",
  "description": "Raw bootstrap samples: 5000 rows (1000 per subject) with per-iteration FPR(p=0), FPR(p=1), ΔFPR",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement/bootstrap_dfpr_samples.csv",
  "tags": "['plan_016', 'bootstrap', 'ΔFPR']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "plan_016_supplement_bootstrap_dfpr_samples",
    "type": "data",
    "description": "Raw bootstrap samples: 5000 rows (1000 per subject) with per-iteration FPR(p=0), FPR(p=1), ΔFPR",
    "project": "irt_equated_bench_regen",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement/bootstrap_dfpr_samples.csv",
    "tags": "['plan_016', 'bootstrap', 'ΔFPR']"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-21T07:58:13.008747+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_2aa86a\", \"name\": \"plan_016_supplement_bootstrap_dfpr_samples\", \"type\": \"data\", \"description\": \"Raw bootstrap samples: 5000 rows (1000 per subject) with per-iteration FPR(p=0), FPR(p=1), ΔFPR\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/data/bootstrap_dfpr_samples.csv\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T07:58:03.270137+00:00\", \"tags\": [\"plan_016\", \"bootstrap\", \"ΔFPR\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-21T07:58:13.008956+00:00_

All artifacts registered. Summary:

**Bootstrap ΔFPR analysis complete** (1000 resamples × 5 subjects, 325s total).

Results per subject:

| Subject | ΔFPR | 95% CI | SE | Baseline FPR 95% CI |
|---------|------|--------|-----|---------------------|
| business_ethics | 0.000 | [0.000, 0.000] | 0.000 | [0.467, 0.600] |
| human_aging | 0.000 | [0.000, 0.000] | 0.000 | [0.350, 0.479] |
| professional_medicine | 0.000 | [0.000, 0.000] | 0.000 | [0.342, 0.452] |
| formal_logic | 0.000 | [0.000, 0.000] | 0.000 | [0.318, 0.398] |
| high_school_statistics | 0.000 | [0.000, 0.000] | 0.000 | [0.303, 0.393] |

0 non-zero ΔFPR iterations out of 5000 total. The zero is not a coincidence — it's algebraically guaranteed: cross-subject stratification scores and clean item responses are both invariant to within-subject injection, so the MH-DIF inputs for clean items are numerically identical at p=0 and p=1 regardless of which models are sampled. The report includes this proof.

Output files in `artifacts/plan_016_supplement/`:
- `bootstrap_dfpr.py` — code
- `bootstrap_dfpr_report.md` — report with method, results, algebraic proof
- `bootstrap_dfpr_results.csv` — per-subject summary
- `bootstrap_dfpr_samples.csv` — 5000 raw bootstrap iterations

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_dfpr_bootstrap_ci_20260521T074450"
}
```

</details>

---
