# code plan 004 step2 gsm8k semi synthetic

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157.jsonl`
- **Structured JSON:** [`3fc9cc0bd94fdc428e47.json`](../../sessions/3f/3fc9cc0bd94fdc428e47.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-21T00:58:29.837959+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore plan_011 semi-synthetic code",
  "prompt": "Find and read the semi-synthetic injection scripts in /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/. I need to understand:\n1. The full injection mechanism (how contaminated items are selected, how ability-overlapping models are identified, how incorrect→correct flipping works)\n2. The MH-DIF implementation\n3. The dose-response evaluation (TPR, FPR, Fisher exact test)\n4. The matching variable computation (standard vs external)\n5. How results are summarized\n\nRead ALL python files in that directory thoroughly. Return the complete code of the main semi-synthetic script."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Explore plan_011 semi-synthetic code",
    "prompt": "Find and read the semi-synthetic injection scripts in /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/. I need to understand:\n1. The full injection mechanism (how contaminated items are selected, how ability-overlapping models are identified, how incorrect→correct flipping works)\n2. The MH-DIF implementation\n3. The dose-response evaluation (TPR, FPR, Fisher exact test)\n4. The matching variable computation (standard vs external)\n5. How results are summarized\n\nRead ALL python files in that directory thoroughly. Return the complete code of the main semi-synthetic script."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-21T00:58:29.838342+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011 -type f -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011 -type f -name \"*.py\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-21T00:58:29.838522+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T00:58:29.838660+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T00:58:29.838843+00:00_

total 2096
drwxr-xr-x  2 ubuntu ubuntu    4096 May 20 21:48 .
drwxr-xr-x 23 ubuntu ubuntu    4096 May 21 00:32 ..
-rw-r--r--  1 ubuntu ubuntu    3587 May 20 21:48 dose_response_summary.csv
-rw-r--r--  1 ubuntu ubuntu   19217 May 20 21:48 injection_results.csv
-rw-r--r--  1 ubuntu ubuntu 2076592 May 20 21:48 per_item_results.csv
-rw-r--r--  1 ubuntu ubuntu   25953 May 20 21:48 plan_011_analysis.py
-rw-r--r--  1 ubuntu ubuntu    7000 May 20 21:48 plan_011_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T00:58:29.838981+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011/plan_011_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T00:58:29.839289+00:00_

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
…[truncated 24070 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T00:58:29.839725+00:00_

Perfect! I have the complete semi-synthetic injection script. Let me now provide you with a comprehensive analysis of the code:

## Complete Analysis of plan_011_analysis.py

### 1. **Full Injection Mechanism** (Lines 307-330)

The injection process works as follows:

- **Contaminated item selection**: For each seed, `N_CONTAMINATED=100` items are randomly selected from the `N_BASELINE=500` baseline items using `np.random.choice()` without replacement (line 311).
- **Ability-overlapping model identification**: The script identifies focal models that fall within the ability (or temporal) overlap range:
  - For ability cohort: models in Q4-5 (highest accuracy) whose accuracy falls within [min(Q1-2 accuracy), min(Q4-5 accuracy)] (lines 237-242)
  - This ensures contamination is injected into models with similar base abilities as reference models, creating a "differential" contamination scenario
- **Incorrect→Correct flipping** (lines 318-324):
  - For each contaminated item and each focal model to inject into
  - Only flip if current response is 0 (incorrect), with probability `p` (the injection strength)
  - Only incorrect responses can be flipped to correct (never the reverse)
  - Count total flips via `n_flipped`

### 2. **MH-DIF Implementation** (Lines 46-167)

The `mh_dif_subset()` function implements Mantel-Haenszel DIF testing with three matching variable modes:

**Stratification priority**:
1. **External**: Pre-computed ability scores from full 12,508-item matrix (lines 71-73)
2. **Anchor**: Sum of known-clean items only (lines 74-80)
3. **Standard**: Total score minus current item (lines 81-83) - purified approach

**Core MH computation** (lines 101-149):
- Stratifies both reference and focal groups into `n_strata=5` bins based on matching variable (lines 85-93)
- For each stratum k, computes 2×2 contingency table (A, B, C, D) for item j (lines 109-115)
- Accumulates Mantel-Haenszel statistics across strata:
  - R and S: numerator/denominator of alpha (lines 1
…[truncated 27590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "Agent",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T00:58:29.839905+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step1_gsm8k_temporal_dif.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step1_gsm8k_temporal_dif.py"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T00:58:29.840222+00:00_

1	#!/usr/bin/env python3
2	"""
3	plan_004_step1 — GSM8K Temporal MH-DIF Analysis
4	
5	Replicates plan_001 methodology on GSM8K data from METABENCH.
6	Two matching strategies:
7	  - standard: purified GSM8K total score
8	  - external: total scores from ARC + HellaSwag + TruthfulQA + Winogrande
9	
10	Inputs:
11	  metabench_data/benchmark-data/gsm8k.csv  — (source, item, correct) long format
12	  model_metadata.csv                        — cohort_temporal, etc.
13	  metabench_data/benchmark-data/{arc,hellaswag,truthfulqa,winogrande}.csv
14	
15	Outputs (in plan_004/):
16	  gsm8k_dif_results.csv, gsm8k_ets_summary.csv, plan_004_step1_report.md
17	"""
18	
19	import numpy as np
20	import pandas as pd
21	from scipy.stats import chi2 as chi2_dist
22	from pathlib import Path
23	import time
24	import warnings
25	import csv
26	
27	warnings.filterwarnings("ignore", category=RuntimeWarning)
28	
29	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
30	BENCH_DIR = BASE / "metabench_data" / "benchmark-data"
31	OUT = BASE / "plan_004"
32	OUT.mkdir(exist_ok=True)
33	
34	
35	# ════════════════════════════════════════════════════════════════════════════
36	#  DATA LOADING
37	# ════════════════════════════════════════════════════════════════════════════
38	print("=== Loading GSM8K data ===")
39	t0_load = time.time()
40	gsm = pd.read_csv(BENCH_DIR / "gsm8k.csv")
41	print(f"  Raw rows: {len(gsm):,}")
42	
43	gsm["correct"] = gsm["correct"].map({"True": 1, "False": 0, True: 1, False: 0}).astype(np.int8)
44	gsm_pivot = gsm.pivot(index="source", columns="item", values="correct")
45	gsm_pivot = gsm_pivot.fillna(0).astype(np.int8)
46	
47	MODEL_NAMES = np.array(gsm_pivot.index.tolist())
48	ITEM_IDS = np.array(gsm_pivot.columns.tolist())
49	X = gsm_pivot.values  # (N_models, J)
50	N_MODELS, J = X.shape
51	print(f"  Response matrix: {N_MODELS} models × {J} items")
52	del gsm, gsm_pivot
53	
54	NAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}
…[truncated 19822 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T00:58:29.840453+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/",
  "description": "List existing plan_004 artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/",
    "description": "List existing plan_004 artifacts"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T00:58:29.840589+00:00_

gsm8k_dif_results.csv
gsm8k_ets_summary.csv
plan_004_step1_gsm8k_temporal_dif.py
plan_004_step1_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T00:58:29.840820+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py",
  "content": "#!/usr/bin/env python3\n\"\"\"\nplan_004_step2 — GSM8K Semi-Synthetic DIF Injection\n\nReplicates plan_011 methodology on GSM8K: inject known differential contamination\ninto real response data and test whether MH-DIF detects it.\n\nTwo matching variants:\n  - standard: purified GSM8K total score (contaminated by injection)\n  - external: average proportion correct on ARC+HellaSwag+TruthfulQA+Winogrande\n\nCohort: temporal, ref=2023, foc=2024\nInjection: 20% of GSM8K items, p ∈ {0.0, 0.3, 0.5, 0.7, 1.0}, 5 seeds\n\nInputs:\n  metabench_data/benchmark-data/gsm8k.csv\n  model_metadata.csv\n  metabench_data/benchmark-data/{arc,hellaswag,truthfulqa,winogrande}.csv\n\nOutputs (in plan_004/):\n  gsm8k_dose_response.csv, gsm8k_dose_response_summary.csv,\n  plan_004_step2_report.md\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.stats import chi2 as chi2_dist, fisher_exact\nfrom pathlib import Path\nimport time\nimport warnings\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nBENCH_DIR = BASE / \"metabench_data\" / \"benchmark-data\"\nOUT = BASE / \"plan_004\"\nOUT.mkdir(exist_ok=True)\n\nINJECTION_PS = [0.0, 0.3, 0.5, 0.7, 1.0]\nN_SEEDS = 5\nCONTAM_FRAC = 0.20\n\nMH_VARIANTS = [\"standard\", \"external\"]\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE\n# ════════════════════════════════════════════════════════════════════════════\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\")\n\n\ndef mh_dif(X_ref, X_foc, n_strata=5,\n           external_scores_ref=None, external_scores_foc=None):\n    \"\"\"Purified Mantel-Haenszel DIF for all columns.\"\"\"\n    J = X_ref.shape[1]\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n\n    rows = []\n    for j in range(J):\n        if use_external:\n            s_ref = external_scores_ref.astype(np.float64)\n            s_foc = external_scores_foc.astype(np.float64)\n        else:\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n        n_bins = len(edges) - 1\n\n        k_ref = np.digitize(s_ref, edges[1:-1])\n        k_foc = np.digitize(s_foc, edges[1:-1])\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        for k in range(n_bins):\n            mr = (k_ref == k)\n            mf = (k_foc == k)\n            n1 = int(mr.sum())\n            n0 = int(mf.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(X_ref[mr, j].sum())\n            B = float(n1 - A)\n            C = float(X_foc[mf, j].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else 999.0\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets))\n\n    return pd.DataFrame(rows)\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"=== Loading GSM8K data ===\")\nt0 = time.time()\ngsm = pd.read_csv(BENCH_DIR / \"gsm8k.csv\")\ngsm[\"correct\"] = gsm[\"correct\"].map({\"True\": 1, \"False\": 0, True: 1, False: 0}).astype(np.int8)\ngsm_pivot = gsm.pivot(index=\"source\", columns=\"item\", values=\"correct\")\ngsm_pivot = gsm_pivot.fillna(0).astype(np.int8)\n\nMODEL_NAMES = np.array(gsm_pivot.index.tolist())\nITEM_IDS = np.array(gsm_pivot.columns.tolist())\nX_full = gsm_pivot.values\nN_MODELS, J_TOTAL = X_full.shape\nprint(f\"  Response matrix: {N_MODELS} × {J_TOTAL}\")\ndel gsm, gsm_pivot\n\nNAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}\nN_CONTAMINATED = int(round(J_TOTAL * CONTAM_FRAC))\nN_CLEAN = J_TOTAL - N_CONTAMINATED\nprint(f\"  Contaminated items: {N_CONTAMINATED} ({CONTAM_FRAC*100:.0f}%), clean: {N_CLEAN}\")\n\n# Model metadata\nmodel_meta = pd.read_csv(BASE / \"model_metadata.csv\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  EXTERNAL MATCHING SCORES\n# ════════════════════════════════════════════════════════════════════════════\ndef compute_benchmark_scores(filepath, benchmark_name):\n    \"\"\"Compute per-model proportion correct from a benchmark CSV.\"\"\"\n    print(f\"  Loading {benchmark_name}...\")\n    t0b = time.time()\n    scores = {}\n    counts = {}\n    for chunk in pd.read_csv(filepath, chunksize=500_000):\n        chunk[\"correct\"] = chunk[\"correct\"].map({\"True\": 1, \"False\": 0, True: 1, False: 0})\n        grouped = chunk.groupby(\"source\")[\"correct\"].agg([\"sum\", \"count\"])\n        for model, row in grouped.iterrows():\n            if model in scores:\n                scores[model] += row[\"sum\"]\n                counts[model] += row[\"count\"]\n            else:\n                scores[model] = row[\"sum\"]\n                counts[model] = row[\"count\"]\n    result = {m: scores[m] / counts[m] for m in scores if counts[m] > 0}\n    print(f\"    {benchmark_name}: {len(result)} models, {time.time()-t0b:.1f}s\")\n    return result\n\n\nprint(\"\\n=== Computing external matching scores ===\")\next_benchmarks = [\"arc\", \"hellaswag\", \"truthfulqa\", \"winogrande\"]\next_scores_raw = {}\nfor bm in ext_benchmarks:\n    ext_scores_raw[bm] = compute_benchmark_scores(BENCH_DIR / f\"{bm}.csv\", bm)\n\next_combined = {}\nfor model in MODEL_NAMES:\n    bm_scores = [ext_scores_raw[bm][model] for bm in ext_benchmarks if model in ext_scores_raw[bm]]\n    if len(bm_scores) >= 2:\n        ext_combined[model] = np.mean(bm_scores)\nprint(f\"  Models with external scores (≥2 benchmarks): {len(ext_combined)}\")\ndel ext_scores_raw\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  COHORT CONSTRUCTION\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Cohort construction ===\")\n\n\ndef rows_for(col, values):\n    names = model_meta.loc[model_meta[col].isin(values), \"model_name\"]\n    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])\n\n\nref_idx = rows_for(\"cohort_temporal\", [\"2023\"])\nfoc_idx = rows_for(\"cohort_temporal\", [\"2024\"])\nprint(f\"  Temporal: ref=2023 (N={len(ref_idx)}), foc=2024 (N={len(foc_idx)})\")\n\n# External subset: models with external scores\nref_names_ext = [MODEL_NAMES[i] for i in ref_idx if MODEL_NAMES[i] in ext_combined]\nfoc_names_ext = [MODEL_NAMES[i] for i in foc_idx if MODEL_NAMES[i] in ext_combined]\nref_idx_ext = np.array([NAME2ROW[n] for n in ref_names_ext])\nfoc_idx_ext = np.array([NAME2ROW[n] for n in foc_names_ext])\nprint(f\"  External subset: ref (N={len(ref_idx_ext)}), foc (N={len(foc_idx_ext)})\")\n\n# Focal injection subset: models with accuracy overlap with ref\ngsm8k_acc = X_full.mean(axis=1)\nref_acc = gsm8k_acc[ref_idx]\nfoc_acc = gsm8k_acc[foc_idx]\noverlap_min = max(ref_acc.min(), foc_acc.min())\noverlap_max = min(ref_acc.max(), foc_acc.max())\n\nif overlap_min <= overlap_max:\n    foc_inject_mask = np.array([(gsm8k_acc[i] >= overlap_min) and (gsm8k_acc[i] <= overlap_max)\n                                 for i in foc_idx])\n    foc_inject_idx = foc_idx[foc_inject_mask]\nelse:\n    foc_inject_idx = foc_idx.copy()\n\n# Same for external subset\nif overlap_min <= overlap_max:\n    foc_inject_ext_mask = np.array([(gsm8k_acc[i] >= overlap_min) and (gsm8k_acc[i] <= overlap_max)\n                                     for i in foc_idx_ext])\n    foc_inject_idx_ext = foc_idx_ext[foc_inject_ext_mask]\nelse:\n    foc_inject_idx_ext = foc_idx_ext.copy()\n\nprint(f\"  Accuracy overlap: [{overlap_min:.4f}, {overlap_max:.4f}]\")\nprint(f\"  Focal inject (standard): {len(foc_inject_idx)} models\")\nprint(f\"  Focal inject (external): {len(foc_inject_idx_ext)} models\")\n\n# Precompute external scores arrays\next_ref_scores = np.array([ext_combined[MODEL_NAMES[i]] for i in ref_idx_ext])\next_foc_scores = np.array([ext_combined[MODEL_NAMES[i]] for i in foc_idx_ext])\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  INJECTION + MH-DIF\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Injection + MH-DIF ===\")\n\ntotal_runs = len(INJECTION_PS) * N_SEEDS * len(MH_VARIANTS)\nrun_count = 0\nt_start = time.time()\n\ninjection_rows = []\n\nfor p in INJECTION_PS:\n    for seed in range(1, N_SEEDS + 1):\n        rng = np.random.RandomState(seed)\n\n        contam_local_idx = rng.choice(J_TOTAL, N_CONTAMINATED, replace=False)\n        contam_set = set(contam_local_idx.tolist())\n        clean_local_idx = np.array([i for i in range(J_TOTAL) if i not in contam_set])\n\n        X_inj = X_full.copy()\n        n_flipped = 0\n\n        if p > 0:\n            for local_j in contam_local_idx:\n                for model_row in foc_inject_idx:\n                    if X_inj[model_row, local_j] == 0:\n                        if rng.random() < p:\n                            X_inj[model_row, local_j] = 1\n                            n_flipped += 1\n\n        orig_density = X_full[np.ix_(foc_inject_idx, contam_local_idx)].mean()\n        new_density = X_inj[np.ix_(foc_inject_idx, contam_local_idx)].mean()\n\n        for variant in MH_VARIANTS:\n            run_count += 1\n\n            if variant == \"standard\":\n                X_ref_v = X_inj[ref_idx]\n                X_foc_v = X_inj[foc_idx]\n                dif_results = mh_dif(X_ref_v, X_foc_v, n_strata=5)\n            else:\n                X_ref_v = X_inj[ref_idx_ext]\n                X_foc_v = X_inj[foc_idx_ext]\n                dif_results = mh_dif(X_ref_v, X_foc_v, n_strata=5,\n                                     external_scores_ref=ext_ref_scores,\n                                     external_scores_foc=ext_foc_scores)\n\n            contam_mask = dif_results[\"col_idx\"].isin(contam_set)\n            contam_results = dif_results[contam_mask]\n            clean_results = dif_results[~contam_mask]\n\n            n_c_contam = (contam_results[\"ets_class\"] == \"C\").sum()\n            n_c_clean = (clean_results[\"ets_class\"] == \"C\").sum()\n            tpr = n_c_contam / N_CONTAMINATED\n            fpr = n_c_clean / N_CLEAN\n\n            table = [[n_c_contam, N_CONTAMINATED - n_c_contam],\n                     [n_c_clean, N_CLEAN - n_c_clean]]\n            fisher_or, fisher_p = fisher_exact(table)\n\n            injection_rows.append(dict(\n                p=p, seed=seed, matching_type=variant,\n                n_items=J_TOTAL, n_contaminated=N_CONTAMINATED, n_clean=N_CLEAN,\n                n_ref=len(ref_idx) if variant == \"standard\" else len(ref_idx_ext),\n                n_foc=len(foc_idx) if variant == \"standard\" else len(foc_idx_ext),\n                n_foc_inject=len(foc_inject_idx) if variant == \"standard\" else len(foc_inject_idx_ext),\n                tpr=tpr, fpr=fpr,\n                n_c_contam=n_c_contam, n_c_clean=n_c_clean,\n                fisher_or=fisher_or, fisher_p=fisher_p,\n                n_responses_flipped=n_flipped,\n                orig_density=orig_density, new_density=new_density,\n            ))\n\n            elapsed = time.time() - t_start\n            print(f\"  [{run_count}/{total_runs}] {variant:8s} p={p} seed={seed}: \"\n                  f\"TPR={tpr:.3f} FPR={fpr:.3f} flipped={n_flipped} ({elapsed:.0f}s)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  AGGREGATE & SAVE\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Aggregating results ===\")\n\ninj_df = pd.DataFrame(injection_rows)\ninj_df.to_csv(OUT / \"gsm8k_dose_response.csv\", index=False)\nprint(f\"  Saved gsm8k_dose_response.csv ({len(inj_df)} rows)\")\n\nsummary_rows = []\nfor (p_val, variant), grp in inj_df.groupby([\"p\", \"matching_type\"]):\n    base_grp = inj_df[(inj_df[\"p\"] == 0.0) & (inj_df[\"matching_type\"] == variant)]\n    base_tpr = base_grp[\"tpr\"].mean()\n    summary_rows.append(dict(\n        p=p_val, matching_type=variant,\n        tpr_mean=grp[\"tpr\"].mean(), tpr_std=grp[\"tpr\"].std(),\n        fpr_mean=grp[\"fpr\"].mean(), fpr_std=grp[\"fpr\"].std(),\n        delta_tpr=grp[\"tpr\"].mean() - base_tpr,\n        fisher_or_mean=grp[\"fisher_or\"].mean(),\n        fisher_p_median=grp[\"fisher_p\"].median(),\n        n_flipped_mean=grp[\"n_responses_flipped\"].mean(),\n    ))\nsummary_df = pd.DataFrame(summary_rows)\nsummary_df.to_csv(OUT / \"gsm8k_dose_response_summary.csv\", index=False)\nprint(f\"  Saved gsm8k_dose_response_summary.csv ({len(summary_df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  REPORT\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Generating report ===\")\n\nL = []\ndef w(s=\"\"):\n    L.append(s)\n\nw(\"# Plan 004 Step 2: GSM8K Semi-Synthetic DIF Injection\")\nw()\nw(\"## 1. Objective\")\nw()\nw(\"Inject known differential contamination into GSM8K response data and test whether\")\nw(\"MH-DIF detects it. Validates that the DIF methodology works on GSM8K (single-domain,\")\nw(\"math benchmark) and enables comparison with MMLU results from plan_011.\")\nw()\n\nw(\"## 2. Setup\")\nw()\nw(f\"- **Benchmark**: GSM8K ({J_TOTAL} items)\")\nw(f\"- **Contaminated items**: {N_CONTAMINATED} ({CONTAM_FRAC*100:.0f}% of {J_TOTAL})\")\nw(f\"- **Injection probabilities**: {INJECTION_PS}\")\nw(f\"- **Seeds per p-level**: {N_SEEDS}\")\nw(f\"- **Cohort**: temporal, ref=2023 (N={len(ref_idx)}), foc=2024 (N={len(foc_idx)})\")\nw(f\"- **External cohort**: ref (N={len(ref_idx_ext)}), foc (N={len(foc_idx_ext)})\")\nw(f\"- **Focal inject (standard)**: {len(foc_inject_idx)} models in accuracy overlap [{overlap_min:.4f}, {overlap_max:.4f}]\")\nw(f\"- **Focal inject (external)**: {len(foc_inject_idx_ext)} models\")\nw()\n\nw(\"### Matching variants\")\nw()\nw(\"| Variant | Matching variable | Properties |\")\nw(\"|---------|-------------------|------------|\")\nw(\"| standard | purified GSM8K total score | Contaminated by injection (20% items affected) |\")\nw(\"| external | avg proportion correct on ARC+HellaSwag+TruthfulQA+Winogrande | Immune to GSM8K injection |\")\nw()\n\nw(\"## 3. Dose-Response Results\")\nw()\nfor variant in MH_VARIANTS:\n    w(f\"### {variant.capitalize()} matching\")\n    w()\n    w(\"| p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |\")\n    w(\"|---|----------------|----------------|------|-----------|----------|\")\n    sub = summary_df[summary_df[\"matching_type\"] == variant].sort_values(\"p\")\n    for _, r in sub.iterrows():\n        w(f\"| {r.p} | {r.tpr_mean:.3f}±{r.tpr_std:.3f} | \"\n          f\"{r.fpr_mean:.3f}±{r.fpr_std:.3f} | {r.delta_tpr:+.3f} | \"\n          f\"{r.fisher_or_mean:.2f} | {r.fisher_p_median:.4f} |\")\n    w()\n\nw(\"## 4. Comparison with MMLU (plan_011)\")\nw()\nw(\"| Metric | MMLU plan_011 (external) | GSM8K (external) |\")\nw(\"|--------|--------------------------|------------------|\")\n\next_sub = summary_df[summary_df[\"matching_type\"] == \"external\"]\next_p0 = ext_sub[ext_sub[\"p\"] == 0.0]\next_p05 = ext_sub[ext_sub[\"p\"] == 0.5]\next_p1 = ext_sub[ext_sub[\"p\"] == 1.0]\n\nmmlu_baseline_fpr = 0.314\nmmlu_dtpr_05 = 0.508\nmmlu_dtpr_10 = 0.674\n\ngsm_fpr0 = ext_p0.iloc[0][\"fpr_mean\"] if len(ext_p0) > 0 else np.nan\ngsm_dtpr05 = ext_p05.iloc[0][\"delta_tpr\"] if len(ext_p05) > 0 else np.nan\ngsm_dtpr10 = ext_p1.iloc[0][\"delta_tpr\"] if len(ext_p1) > 0 else np.nan\n\nw(f\"| Baseline FPR (p=0) | {mmlu_baseline_fpr:.3f} | {gsm_fpr0:.3f} |\")\nw(f\"| ΔTPR at p=0.5 | +{mmlu_dtpr_05:.3f} | {gsm_dtpr05:+.3f} |\")\nw(f\"| ΔTPR at p=1.0 | +{mmlu_dtpr_10:.3f} | {gsm_dtpr10:+.3f} |\")\nw(f\"| Items | 500 (subset) | {J_TOTAL} (all) |\")\nw(f\"| Contaminated | 100 (20%) | {N_CONTAMINATED} (~20%) |\")\nw()\n\nw(\"## 5. Standard vs External Matching\")\nw()\nw(\"| p | Standard TPR | External TPR | Standard FPR | External FPR |\")\nw(\"|---|-------------|-------------|-------------|-------------|\")\nfor p_val in INJECTION_PS:\n    std_r = summary_df[(summary_df[\"p\"] == p_val) & (summary_df[\"matching_type\"] == \"standard\")]\n    ext_r = summary_df[(summary_df[\"p\"] == p_val) & (summary_df[\"matching_type\"] == \"external\")]\n    if len(std_r) > 0 and len(ext_r) > 0:\n        w(f\"| {p_val} | {std_r.iloc[0].tpr_mean:.3f} | {ext_r.iloc[0].tpr_mean:.3f} | \"\n          f\"{std_r.iloc[0].fpr_mean:.3f} | {ext_r.iloc[0].fpr_mean:.3f} |\")\nw()\n\nw(\"## 6. Density Changes\")\nw()\nw(\"| p | Orig density | Post density | Responses flipped |\")\nw(\"|---|-------------|-------------|-------------------|\")\nfor p_val in INJECTION_PS:\n    if p_val == 0:\n        continue\n    sub = inj_df[(inj_df[\"p\"] == p_val) & (inj_df[\"matching_type\"] == \"standard\")]\n    if len(sub) > 0:\n        w(f\"| {p_val} | {sub.orig_density.mean():.4f} | {sub.new_density.mean():.4f} | \"\n          f\"{sub.n_responses_flipped.mean():.0f} |\")\nw()\n\nw(\"## 7. Verdict\")\nw()\n\nfor variant in MH_VARIANTS:\n    sub = summary_df[summary_df[\"matching_type\"] == variant]\n    p0 = sub[sub[\"p\"] == 0.0]\n    p1 = sub[sub[\"p\"] == 1.0]\n    if len(p0) == 0 or len(p1) == 0:\n        continue\n    tpr0 = p0.iloc[0][\"tpr_mean\"]\n    fpr0 = p0.iloc[0][\"fpr_mean\"]\n    tpr1 = p1.iloc[0][\"tpr_mean\"]\n    fpr1 = p1.iloc[0][\"fpr_mean\"]\n    d_tpr = tpr1 - tpr0\n\n    w(f\"### {variant.capitalize()} matching\")\n    w()\n    w(f\"- Baseline (p=0): TPR={tpr0:.3f}, FPR={fpr0:.3f}\")\n    w(f\"- Full injection (p=1): TPR={tpr1:.3f}, FPR={fpr1:.3f}\")\n    w(f\"- ΔTPR = {d_tpr:+.3f}\")\n    w()\n\n    if d_tpr > 0.3 and tpr1 > 0.5:\n        w(f\"**SUCCESS**: injection raises TPR by {d_tpr:.3f} with clear dose-response.\")\n    elif d_tpr > 0.1:\n        w(f\"**PARTIAL**: detectable signal (ΔTPR={d_tpr:.3f}) but modest.\")\n    else:\n        w(f\"**FAIL**: ΔTPR={d_tpr:.3f} too small to indicate reliable detection.\")\n    w()\n\nw(\"## 8. Implications\")\nw()\nw(\"### Cross-benchmark generalization\")\nw()\nw(\"If GSM8K semi-synthetic results are comparable to MMLU plan_011, this confirms\")\nw(\"MH-DIF methodology generalizes beyond MMLU to single-domain math benchmarks.\")\nw()\nw(\"### Matching variable contamination\")\nw()\nw(\"Standard matching uses GSM8K total score, which is corrupted when 20% of items\")\nw(\"are injected. This should inflate FPR compared to external matching.\")\nw(\"External matching (other benchmarks) is immune to GSM8K injection and should\")\nw(\"provide cleaner separation between contaminated and clean items.\")\nw()\n\nreport_text = \"\\n\".join(L) + \"\\n\"\n(OUT / \"plan_004_step2_report.md\").write_text(report_text)\nprint(\"  Report written.\")\n\n# Console summary\nprint(\"\\n\" + \"=\" * 60)\nprint(\"SUMMARY\")\nprint(\"=\" * 60)\nfor variant in MH_VARIANTS:\n    print(f\"\\n--- {variant} matching ---\")\n    sub = summary_df[summary_df[\"matching_type\"] == variant].sort_values(\"p\")\n    for _, r in sub.iterrows():\n        print(f\"  p={r.p}: TPR={r.tpr_mean:.3f}±{r.tpr_std:.3f}  \"\n              f\"FPR={r.fpr_mean:.3f}±{r.fpr_std:.3f}  ΔTPR={r.delta_tpr:+.3f}\")\n\ntotal_elapsed = time.time() - t_start\nprint(f\"\\nTotal time: {total_elapsed:.0f}s\")\nprint(f\"All outputs saved to {OUT}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py",
    "content": "#!/usr/bin/env python3\n\"\"\"\nplan_004_step2 — GSM8K Semi-Synthetic DIF Injection\n\nReplicates plan_011 methodology on GSM8K: inject known differential contamination\ninto real response data and test whether MH-DIF detects it.\n\nTwo matching variants:\n  - standard: purified GSM8K total score (contaminated by injection)\n  - external: average proportion correct on ARC+HellaSwag+TruthfulQA+Winogrande\n\nCohort: temporal, ref=2023, foc=2024\nInjection: 20% of GSM8K items, p ∈ {0.0, 0.3, 0.5, 0.7, 1.0}, 5 seeds\n\nInputs:\n  metabench_data/benchmark-data/gsm8k.csv\n  model_metadata.csv\n  metabench_data/benchmark-data/{arc,hellaswag,truthfulqa,winogrande}.csv\n\nOutputs (in plan_004/):\n  gsm8k_dose_response.csv, gsm8k_dose_response_summary.csv,\n  plan_004_step2_report.md\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy.stats import chi2 as chi2_dist, fisher_exact\nfrom pathlib import Path\nimport time\nimport warnings\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nBASE = Path(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\")\nBENCH_DIR = BASE / \"metabench_data\" / \"benchmark-data\"\nOUT = BASE / \"plan_004\"\nOUT.mkdir(exist_ok=True)\n\nINJECTION_PS = [0.0, 0.3, 0.5, 0.7, 1.0]\nN_SEEDS = 5\nCONTAM_FRAC = 0.20\n\nMH_VARIANTS = [\"standard\", \"external\"]\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MH-DIF CORE\n# ════════════════════════════════════════════════════════════════════════════\ndef _nan_row(j):\n    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,\n                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class=\"A\")\n\n\ndef mh_dif(X_ref, X_foc, n_strata=5,\n           external_scores_ref=None, external_scores_foc=None):\n    \"\"\"Purified Mantel-Haenszel DIF for all columns.\"\"\"\n    J = X_ref.shape[1]\n    use_external = external_scores_ref is not None\n\n    if not use_external:\n        tot_ref = X_ref.sum(axis=1).astype(np.float64)\n        tot_foc = X_foc.sum(axis=1).astype(np.float64)\n\n    rows = []\n    for j in range(J):\n        if use_external:\n            s_ref = external_scores_ref.astype(np.float64)\n            s_foc = external_scores_foc.astype(np.float64)\n        else:\n            s_ref = tot_ref - X_ref[:, j].astype(np.float64)\n            s_foc = tot_foc - X_foc[:, j].astype(np.float64)\n\n        s_all = np.concatenate([s_ref, s_foc])\n        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n        if len(edges) < 2:\n            rows.append(_nan_row(j))\n            continue\n        n_bins = len(edges) - 1\n\n        k_ref = np.digitize(s_ref, edges[1:-1])\n        k_foc = np.digitize(s_foc, edges[1:-1])\n\n        R = S = 0.0\n        sum_diff = 0.0\n        sum_var = 0.0\n        pr = ps_qr = qs = 0.0\n        n_ok = 0\n\n        for k in range(n_bins):\n            mr = (k_ref == k)\n            mf = (k_foc == k)\n            n1 = int(mr.sum())\n            n0 = int(mf.sum())\n            if n1 == 0 or n0 == 0:\n                continue\n\n            A = float(X_ref[mr, j].sum())\n            B = float(n1 - A)\n            C = float(X_foc[mf, j].sum())\n            D = float(n0 - C)\n            Nk = float(n1 + n0)\n            m1 = A + C\n            m0 = B + D\n\n            if m1 == 0 or m0 == 0 or Nk <= 1:\n                continue\n            n_ok += 1\n\n            Rk = A * D / Nk\n            Sk = B * C / Nk\n            R += Rk\n            S += Sk\n\n            EA = n1 * m1 / Nk\n            sum_diff += A - EA\n            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))\n\n            Pk = (A + D) / Nk\n            Qk = (B + C) / Nk\n            pr += Pk * Rk\n            ps_qr += Pk * Sk + Qk * Rk\n            qs += Qk * Sk\n\n        if n_ok == 0 or (R == 0 and S == 0):\n            rows.append(_nan_row(j))\n            continue\n\n        if S == 0:\n            alpha, delta, se = np.inf, -np.inf, np.nan\n        elif R == 0:\n            alpha, delta, se = 0.0, np.inf, np.nan\n        else:\n            alpha = R / S\n            delta = -2.35 * np.log(alpha)\n            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)\n            se = 2.35 * np.sqrt(v) if v > 0 else np.nan\n\n        if sum_var > 0:\n            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var\n            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)\n        else:\n            chi2_stat = pval = np.nan\n\n        ad = abs(delta) if np.isfinite(delta) else 999.0\n        if ad < 1.0:\n            ets = \"A\"\n        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:\n            ets = \"C\"\n        else:\n            ets = \"B\"\n\n        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,\n                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets))\n\n    return pd.DataFrame(rows)\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DATA LOADING\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"=== Loading GSM8K data ===\")\nt0 = time.time()\ngsm = pd.read_csv(BENCH_DIR / \"gsm8k.csv\")\ngsm[\"correct\"] = gsm[\"correct\"].map({\"True\": 1, \"False\": 0, True: 1, False: 0}).astype(np.int8)\ngsm_pivot = gsm.pivot(index=\"source\", columns=\"item\", values=\"correct\")\ngsm_pivot = gsm_pivot.fillna(0).astype(np.int8)\n\nMODEL_NAMES = np.array(gsm_pivot.index.tolist())\nITEM_IDS = np.array(gsm_pivot.columns.tolist())\nX_full = gsm_pivot.values\nN_MODELS, J_TOTAL = X_full.shape\nprint(f\"  Response matrix: {N_MODELS} × {J_TOTAL}\")\ndel gsm, gsm_pivot\n\nNAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}\nN_CONTAMINATED = int(round(J_TOTAL * CONTAM_FRAC))\nN_CLEAN = J_TOTAL - N_CONTAMINATED\nprint(f\"  Contaminated items: {N_CONTAMINATED} ({CONTAM_FRAC*100:.0f}%), clean: {N_CLEAN}\")\n\n# Model metadata\nmodel_meta = pd.read_csv(BASE / \"model_metadata.csv\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  EXTERNAL MATCHING SCORES\n# ════════════════════════════════════════════════════════════════════════════\ndef compute_benchmark_scores(filepath, benchmark_name):\n    \"\"\"Compute per-model proportion correct from a benchmark CSV.\"\"\"\n    print(f\"  Loading {benchmark_name}...\")\n    t0b = time.time()\n    scores = {}\n    counts = {}\n    for chunk in pd.read_csv(filepath, chunksize=500_000):\n        chunk[\"correct\"] = chunk[\"correct\"].map({\"True\": 1, \"False\": 0, True: 1, False: 0})\n        grouped = chunk.groupby(\"source\")[\"correct\"].agg([\"sum\", \"count\"])\n        for model, row in grouped.iterrows():\n            if model in scores:\n                scores[model] += row[\"sum\"]\n                counts[model] += row[\"count\"]\n            else:\n                scores[model] = row[\"sum\"]\n                counts[model] = row[\"count\"]\n    result = {m: scores[m] / counts[m] for m in scores if counts[m] > 0}\n    print(f\"    {benchmark_name}: {len(result)} models, {time.time()-t0b:.1f}s\")\n    return result\n\n\nprint(\"\\n=== Computing external matching scores ===\")\next_benchmarks = [\"arc\", \"hellaswag\", \"truthfulqa\", \"winogrande\"]\next_scores_raw = {}\nfor bm in ext_benchmarks:\n    ext_scores_raw[bm] = compute_benchmark_scores(BENCH_DIR / f\"{bm}.csv\", bm)\n\next_combined = {}\nfor model in MODEL_NAMES:\n    bm_scores = [ext_scores_raw[bm][model] for bm in ext_benchmarks if model in ext_scores_raw[bm]]\n    if len(bm_scores) >= 2:\n        ext_combined[model] = np.mean(bm_scores)\nprint(f\"  Models with external scores (≥2 benchmarks): {len(ext_combined)}\")\ndel ext_scores_raw\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  COHORT CONSTRUCTION\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Cohort construction ===\")\n\n\ndef rows_for(col, values):\n    names = model_meta.loc[model_meta[col].isin(values), \"model_name\"]\n    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])\n\n\nref_idx = rows_for(\"cohort_temporal\", [\"2023\"])\nfoc_idx = rows_for(\"cohort_temporal\", [\"2024\"])\nprint(f\"  Temporal: ref=2023 (N={len(ref_idx)}), foc=2024 (N={len(foc_idx)})\")\n\n# External subset: models with external scores\nref_names_ext = [MODEL_NAMES[i] for i in ref_idx if MODEL_NAMES[i] in ext_combined]\nfoc_names_ext = [MODEL_NAMES[i] for i in foc_idx if MODEL_NAMES[i] in ext_combined]\nref_idx_ext = np.array([NAME2ROW[n] for n in ref_names_ext])\nfoc_idx_ext = np.array([NAME2ROW[n] for n in foc_names_ext])\nprint(f\"  External subset: ref (N={len(ref_idx_ext)}), foc (N={len(foc_idx_ext)})\")\n\n# Focal injection subset: models with accuracy overlap with ref\ngsm8k_acc = X_full.mean(axis=1)\nref_acc = gsm8k_acc[ref_idx]\nfoc_acc = gsm8k_acc[foc_idx]\noverlap_min = max(ref_acc.min(), foc_acc.min())\noverlap_max = min(ref_acc.max(), foc_acc.max())\n\nif overlap_min <= overlap_max:\n    foc_inject_mask = np.array([(gsm8k_acc[i] >= overlap_min) and (gsm8k_acc[i] <= overlap_max)\n                                 for i in foc_idx])\n    foc_inject_idx = foc_idx[foc_inject_mask]\nelse:\n    foc_inject_idx = foc_idx.copy()\n\n# Same for external subset\nif overlap_min <= overlap_max:\n    foc_inject_ext_mask = np.array([(gsm8k_acc[i] >= overlap_min) and (gsm8k_acc[i] <= overlap_max)\n                                     for i in foc_idx_ext])\n    foc_inject_idx_ext = foc_idx_ext[foc_inject_ext_mask]\nelse:\n    foc_inject_idx_ext = foc_idx_ext.copy()\n\nprint(f\"  Accuracy overlap: [{overlap_min:.4f}, {overlap_max:.4f}]\")\nprint(f\"  Focal inject (standard): {len(foc_inject_idx)} models\")\nprint(f\"  Focal inject (external): {len(foc_inject_idx_ext)} models\")\n\n# Precompute external scores arrays\next_ref_scores = np.array([ext_combined[MODEL_NAMES[i]] for i in ref_idx_ext])\next_foc_scores = np.array([ext_combined[MODEL_NAMES[i]] for i in foc_idx_ext])\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  INJECTION + MH-DIF\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Injection + MH-DIF ===\")\n\ntotal_runs = len(INJECTION_PS) * N_SEEDS * len(MH_VARIANTS)\nrun_count = 0\nt_start = time.time()\n\ninjection_rows = []\n\nfor p in INJECTION_PS:\n    for seed in range(1, N_SEEDS + 1):\n        rng = np.random.RandomState(seed)\n\n        contam_local_idx = rng.choice(J_TOTAL, N_CONTAMINATED, replace=False)\n        contam_set = set(contam_local_idx.tolist())\n        clean_local_idx = np.array([i for i in range(J_TOTAL) if i not in contam_set])\n\n        X_inj = X_full.copy()\n        n_flipped = 0\n\n        if p > 0:\n            for local_j in contam_local_idx:\n                for model_row in foc_inject_idx:\n                    if X_inj[model_row, local_j] == 0:\n                        if rng.random() < p:\n                            X_inj[model_row, local_j] = 1\n                            n_flipped += 1\n\n        orig_density = X_full[np.ix_(foc_inject_idx, contam_local_idx)].mean()\n        new_density = X_inj[np.ix_(foc_inject_idx, contam_local_idx)].mean()\n\n        for variant in MH_VARIANTS:\n            run_count += 1\n\n            if variant == \"standard\":\n                X_ref_v = X_inj[ref_idx]\n                X_foc_v = X_inj[foc_idx]\n                dif_results = mh_dif(X_ref_v, X_foc_v, n_strata=5)\n            else:\n                X_ref_v = X_inj[ref_idx_ext]\n                X_foc_v = X_inj[foc_idx_ext]\n                dif_results = mh_dif(X_ref_v, X_foc_v, n_strata=5,\n                                     external_scores_ref=ext_ref_scores,\n                                     external_scores_foc=ext_foc_scores)\n\n            contam_mask = dif_results[\"col_idx\"].isin(contam_set)\n            contam_results = dif_results[contam_mask]\n            clean_results = dif_results[~contam_mask]\n\n            n_c_contam = (contam_results[\"ets_class\"] == \"C\").sum()\n            n_c_clean = (clean_results[\"ets_class\"] == \"C\").sum()\n            tpr = n_c_contam / N_CONTAMINATED\n            fpr = n_c_clean / N_CLEAN\n\n            table = [[n_c_contam, N_CONTAMINATED - n_c_contam],\n                     [n_c_clean, N_CLEAN - n_c_clean]]\n            fisher_or, fisher_p = fisher_exact(table)\n\n            injection_rows.append(dict(\n                p=p, seed=seed, matching_type=variant,\n                n_items=J_TOTAL, n_contaminated=N_CONTAMINATED, n_clean=N_CLEAN,\n                n_ref=len(ref_idx) if variant == \"standard\" else len(ref_idx_ext),\n                n_foc=len(foc_idx) if variant == \"standard\" else len(foc_idx_ext),\n                n_foc_inject=len(foc_inject_idx) if variant == \"standard\" else len(foc_inject_idx_ext),\n                tpr=tpr, fpr=fpr,\n                n_c_contam=n_c_contam, n_c_clean=n_c_clean,\n                fisher_or=fisher_or, fisher_p=fisher_p,\n                n_responses_flipped=n_flipped,\n                orig_density=orig_density, new_density=new_density,\n            ))\n\n            elapsed = time.time() - t_start\n            print(f\"  [{run_count}/{total_runs}] {variant:8s} p={p} seed={seed}: \"\n                  f\"TPR={tpr:.3f} FPR={fpr:.3f} flipped={n_flipped} ({elapsed:.0f}s)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  AGGREGATE & SAVE\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Aggregating results ===\")\n\ninj_df = pd.DataFrame(injection_rows)\ninj_df.to_csv(OUT / \"gsm8k_dose_response.csv\", index=False)\nprint(f\"  Saved gsm8k_dose_response.csv ({len(inj_df)} rows)\")\n\nsummary_rows = []\nfor (p_val, variant), grp in inj_df.groupby([\"p\", \"matching_type\"]):\n    base_grp = inj_df[(inj_df[\"p\"] == 0.0) & (inj_df[\"matching_type\"] == variant)]\n    base_tpr = base_grp[\"tpr\"].mean()\n    summary_rows.append(dict(\n        p=p_val, matching_type=variant,\n        tpr_mean=grp[\"tpr\"].mean(), tpr_std=grp[\"tpr\"].std(),\n        fpr_mean=grp[\"fpr\"].mean(), fpr_std=grp[\"fpr\"].std(),\n        delta_tpr=grp[\"tpr\"].mean() - base_tpr,\n        fisher_or_mean=grp[\"fisher_or\"].mean(),\n        fisher_p_median=grp[\"fisher_p\"].median(),\n        n_flipped_mean=grp[\"n_responses_flipped\"].mean(),\n    ))\nsummary_df = pd.DataFrame(summary_rows)\nsummary_df.to_csv(OUT / \"gsm8k_dose_response_summary.csv\", index=False)\nprint(f\"  Saved gsm8k_dose_response_summary.csv ({len(summary_df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  REPORT\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Generating report ===\")\n\nL = []\ndef w(s=\"\"):\n    L.append(s)\n\nw(\"# Plan 004 Step 2: GSM8K Semi-Synthetic DIF Injection\")\nw()\nw(\"## 1. Objective\")\nw()\nw(\"Inject known differential contamination into GSM8K response data and test whether\")\nw(\"MH-DIF detects it. Validates that the DIF methodology works on GSM8K (single-domain,\")\nw(\"math benchmark) and enables comparison with MMLU results from plan_011.\")\nw()\n\nw(\"## 2. Setup\")\nw()\nw(f\"- **Benchmark**: GSM8K ({J_TOTAL} items)\")\nw(f\"- **Contaminated items**: {N_CONTAMINATED} ({CONTAM_FRAC*100:.0f}% of {J_TOTAL})\")\nw(f\"- **Injection probabilities**: {INJECTION_PS}\")\nw(f\"- **Seeds per p-level**: {N_SEEDS}\")\nw(f\"- **Cohort**: temporal, ref=2023 (N={len(ref_idx)}), foc=2024 (N={len(foc_idx)})\")\nw(f\"- **External cohort**: ref (N={len(ref_idx_ext)}), foc (N={len(foc_idx_ext)})\")\nw(f\"- **Focal inject (standard)**: {len(foc_inject_idx)} models in accuracy overlap [{overlap_min:.4f}, {overlap_max:.4f}]\")\nw(f\"- **Focal inject (external)**: {len(foc_inject_idx_ext)} models\")\nw()\n\nw(\"### Matching variants\")\nw()\nw(\"| Variant | Matching variable | Properties |\")\nw(\"|---------|-------------------|------------|\")\nw(\"| standard | purified GSM8K total score | Contaminated by injection (20% items affected) |\")\nw(\"| external | avg proportion correct on ARC+HellaSwag+TruthfulQA+Winogrande | Immune to GSM8K injection |\")\nw()\n\nw(\"## 3. Dose-Response Results\")\nw()\nfor variant in MH_VARIANTS:\n    w(f\"### {variant.capitalize()} matching\")\n    w()\n    w(\"| p | TPR (mean±std) | FPR (mean±std) | ΔTPR | Fisher OR | Fisher p |\")\n    w(\"|---|----------------|----------------|------|-----------|----------|\")\n    sub = summary_df[summary_df[\"matching_type\"] == variant].sort_values(\"p\")\n    for _, r in sub.iterrows():\n        w(f\"| {r.p} | {r.tpr_mean:.3f}±{r.tpr_std:.3f} | \"\n          f\"{r.fpr_mean:.3f}±{r.fpr_std:.3f} | {r.delta_tpr:+.3f} | \"\n          f\"{r.fisher_or_mean:.2f} | {r.fisher_p_median:.4f} |\")\n    w()\n\nw(\"## 4. Comparison with MMLU (plan_011)\")\nw()\nw(\"| Metric | MMLU plan_011 (external) | GSM8K (external) |\")\nw(\"|--------|--------------------------|------------------|\")\n\next_sub = summary_df[summary_df[\"matching_type\"] == \"external\"]\next_p0 = ext_sub[ext_sub[\"p\"] == 0.0]\next_p05 = ext_sub[ext_sub[\"p\"] == 0.5]\next_p1 = ext_sub[ext_sub[\"p\"] == 1.0]\n\nmmlu_baseline_fpr = 0.314\nmmlu_dtpr_05 = 0.508\nmmlu_dtpr_10 = 0.674\n\ngsm_fpr0 = ext_p0.iloc[0][\"fpr_mean\"] if len(ext_p0) > 0 else np.nan\ngsm_dtpr05 = ext_p05.iloc[0][\"delta_tpr\"] if len(ext_p05) > 0 else np.nan\ngsm_dtpr10 = ext_p1.iloc[0][\"delta_tpr\"] if len(ext_p1) > 0 else np.nan\n\nw(f\"| Baseline FPR (p=0) | {mmlu_baseline_fpr:.3f} | {gsm_fpr0:.3f} |\")\nw(f\"| ΔTPR at p=0.5 | +{mmlu_dtpr_05:.3f} | {gsm_dtpr05:+.3f} |\")\nw(f\"| ΔTPR at p=1.0 | +{mmlu_dtpr_10:.3f} | {gsm_dtpr10:+.3f} |\")\nw(f\"| Items | 500 (subset) | {J_TOTAL} (all) |\")\nw(f\"| Contaminated | 100 (20%) | {N_CONTAMINATED} (~20%) |\")\nw()\n\nw(\"## 5. Standard vs External Matching\")\nw()\nw(\"| p | Standard TPR | External TPR | Standard FPR | External FPR |\")\nw(\"|---|-------------|-------------|-------------|-------------|\")\nfor p_val in INJECTION_PS:\n    std_r = summary_df[(summary_df[\"p\"] == p_val) & (summary_df[\"matching_type\"] == \"standard\")]\n    ext_r = summary_df[(summary_df[\"p\"] == p_val) & (summary_df[\"matching_type\"] == \"external\")]\n    if len(std_r) > 0 and len(ext_r) > 0:\n        w(f\"| {p_val} | {std_r.iloc[0].tpr_mean:.3f} | {ext_r.iloc[0].tpr_mean:.3f} | \"\n          f\"{std_r.iloc[0].fpr_mean:.3f} | {ext_r.iloc[0].fpr_mean:.3f} |\")\nw()\n\nw(\"## 6. Density Changes\")\nw()\nw(\"| p | Orig density | Post density | Responses flipped |\")\nw(\"|---|-------------|-------------|-------------------|\")\nfor p_val in INJECTION_PS:\n    if p_val == 0:\n        continue\n    sub = inj_df[(inj_df[\"p\"] == p_val) & (inj_df[\"matching_type\"] == \"standard\")]\n    if len(sub) > 0:\n        w(f\"| {p_val} | {sub.orig_density.mean():.4f} | {sub.new_density.mean():.4f} | \"\n          f\"{sub.n_responses_flipped.mean():.0f} |\")\nw()\n\nw(\"## 7. Verdict\")\nw()\n\nfor variant in MH_VARIANTS:\n    sub = summary_df[summary_df[\"matching_type\"] == variant]\n    p0 = sub[sub[\"p\"] == 0.0]\n    p1 = sub[sub[\"p\"] == 1.0]\n    if len(p0) == 0 or len(p1) == 0:\n        continue\n    tpr0 = p0.iloc[0][\"tpr_mean\"]\n    fpr0 = p0.iloc[0][\"fpr_mean\"]\n    tpr1 = p1.iloc[0][\"tpr_mean\"]\n    fpr1 = p1.iloc[0][\"fpr_mean\"]\n    d_tpr = tpr1 - tpr0\n\n    w(f\"### {variant.capitalize()} matching\")\n    w()\n    w(f\"- Baseline (p=0): TPR={tpr0:.3f}, FPR={fpr0:.3f}\")\n    w(f\"- Full injection (p=1): TPR={tpr1:.3f}, FPR={fpr1:.3f}\")\n    w(f\"- ΔTPR = {d_tpr:+.3f}\")\n    w()\n\n    if d_tpr > 0.3 and tpr1 > 0.5:\n        w(f\"**SUCCESS**: injection raises TPR by {d_tpr:.3f} with clear dose-response.\")\n    elif d_tpr > 0.1:\n        w(f\"**PARTIAL**: detectable signal (ΔTPR={d_tpr:.3f}) but modest.\")\n    else:\n        w(f\"**FAIL**: ΔTPR={d_tpr:.3f} too small to indicate reliable detection.\")\n    w()\n\nw(\"## 8. Implications\")\nw()\nw(\"### Cross-benchmark generalization\")\nw()\nw(\"If GSM8K semi-synthetic results are comparable to MMLU plan_011, this confirms\")\nw(\"MH-DIF methodology generalizes beyond MMLU to single-domain math benchmarks.\")\nw()\nw(\"### Matching variable contamination\")\nw()\nw(\"Standard matching uses GSM8K total score, which is corrupted when 20% of items\")\nw(\"are injected. This should inflate FPR compared to external matching.\")\nw(\"External matching (other benchmarks) is immune to GSM8K injection and should\")\nw(\"provide cleaner separation between contaminated and clean items.\")\nw()\n\nreport_text = \"\\n\".join(L) + \"\\n\"\n(OUT / \"plan_004_step2_report.md\").write_text(report_text)\nprint(\"  Report written.\")\n\n# Console summary\nprint(\"\\n\" + \"=\" * 60)\nprint(\"SUMMARY\")\nprint(\"=\" * 60)\nfor variant in MH_VARIANTS:\n    print(f\"\\n--- {variant} matching ---\")\n    sub = summary_df[summary_df[\"matching_type\"] == variant].sort_values(\"p\")\n    for _, r in sub.iterrows():\n        print(f\"  p={r.p}: TPR={r.tpr_mean:.3f}±{r.tpr_std:.3f}  \"\n              f\"FPR={r.fpr_mean:.3f}±{r.fpr_std:.3f}  ΔTPR={r.delta_tpr:+.3f}\")\n\ntotal_elapsed = time.time() - t_start\nprint(f\"\\nTotal time: {total_elapsed:.0f}s\")\nprint(f\"All outputs saved to {OUT}\")\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T00:58:29.841257+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T00:58:29.841412+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py 2>&1",
  "description": "Run GSM8K semi-synthetic injection script",
  "timeout": "600000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "Bash",
  "tool_args": {
    "command": "python artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py 2>&1",
    "description": "Run GSM8K semi-synthetic injection script",
    "timeout": "600000"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T00:58:29.841535+00:00_

Exit code 127
/bin/bash: line 1: python: command not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T00:58:29.841650+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "which python3 && python3 artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py 2>&1",
  "description": "Run GSM8K semi-synthetic injection script with python3",
  "timeout": "600000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "Bash",
  "tool_args": {
    "command": "which python3 && python3 artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py 2>&1",
    "description": "Run GSM8K semi-synthetic injection script with python3",
    "timeout": "600000"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T00:58:29.841843+00:00_

/usr/bin/python3
=== Loading GSM8K data ===
  Response matrix: 6702 × 1319
  Contaminated items: 264 (20%), clean: 1055

=== Computing external matching scores ===
  Loading arc...
    arc: 5227 models, 4.3s
  Loading hellaswag...
    hellaswag: 5227 models, 34.3s
  Loading truthfulqa...
    truthfulqa: 5228 models, 2.7s
  Loading winogrande...
    winogrande: 6558 models, 4.8s
  Models with external scores (≥2 benchmarks): 5057

=== Cohort construction ===
  Temporal: ref=2023 (N=1017), foc=2024 (N=804)
  External subset: ref (N=1017), foc (N=804)
  Accuracy overlap: [0.0000, 0.7589]
  Focal inject (standard): 779 models
  Focal inject (external): 779 models

=== Injection + MH-DIF ===
  [1/50] standard p=0.0 seed=1: TPR=0.227 FPR=0.179 flipped=0 (1s)
  [2/50] external p=0.0 seed=1: TPR=0.470 FPR=0.475 flipped=0 (2s)
  [3/50] standard p=0.0 seed=2: TPR=0.155 FPR=0.197 flipped=0 (2s)
  [4/50] external p=0.0 seed=2: TPR=0.492 FPR=0.469 flipped=0 (3s)
  [5/50] standard p=0.0 seed=3: TPR=0.163 FPR=0.195 flipped=0 (4s)
  [6/50] external p=0.0 seed=3: TPR=0.455 FPR=0.479 flipped=0 (5s)
  [7/50] standard p=0.0 seed=4: TPR=0.220 FPR=0.181 flipped=0 (5s)
  [8/50] external p=0.0 seed=4: TPR=0.527 FPR=0.461 flipped=0 (6s)
  [9/50] standard p=0.0 seed=5: TPR=0.144 FPR=0.200 flipped=0 (7s)
  [10/50] external p=0.0 seed=5: TPR=0.473 FPR=0.474 flipped=0 (8s)
  [11/50] standard p=0.3 seed=1: TPR=0.739 FPR=0.262 flipped=37260 (9s)
  [12/50] external p=0.3 seed=1: TPR=0.951 FPR=0.475 flipped=37260 (9s)
  [13/50] standard p=0.3 seed=2: TPR=0.750 FPR=0.264 flipped=36402 (10s)
  [14/50] external p=0.3 seed=2: TPR=0.973 FPR=0.469 flipped=36402 (11s)
  [15/50] standard p=0.3 seed=3: TPR=0.750 FPR=0.259 flipped=35947 (12s)
  [16/50] external p=0.3 seed=3: TPR=0.981 FPR=0.479 flipped=35947 (13s)
  [17/50] standard p=0.3 seed=4: TPR=0.754 FPR=0.250 flipped=36437 (14s)
  [18/50] external p=0.3 seed=4: TPR=0.958 FPR=0.461 flipped=36437 (15s)
  [19/50] standard p=0.3 seed=5: TPR=0.712 FPR=0.24
…[truncated 3333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T00:58:29.842035+00:00_

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
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
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

_source line 20 · 2026-05-21T00:58:29.842161+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T00:58:29.842282+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "plan_004_step2_gsm8k_semi_synthetic",
  "type": "intermediate",
  "description": "GSM8K semi-synthetic DIF injection script — injects known differential contamination and tests MH-DIF detection with standard/external matching",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py",
  "tags": "['plan_004', 'gsm8k', 'semi-synthetic', 'dif', 'injection']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "plan_004_step2_gsm8k_semi_synthetic",
    "type": "intermediate",
    "description": "GSM8K semi-synthetic DIF injection script — injects known differential contamination and tests MH-DIF detection with standard/external matching",
    "project": "irt_equated_bench_regen",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step2_gsm8k_semi_synthetic.py",
    "tags": "['plan_004', 'gsm8k', 'semi-synthetic', 'dif', 'injection']"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T00:58:29.842427+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_3f68a2\", \"name\": \"plan_004_step2_gsm8k_semi_synthetic\", \"type\": \"intermediate\", \"description\": \"GSM8K semi-synthetic DIF injection script — injects known differential contamination and tests MH-DIF detection with standard/external matching\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_004_step2_gsm8k_semi_synthetic.py\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T00:58:09.035640+00:00\", \"tags\": [\"plan_004\", \"gsm8k\", \"semi-synthetic\", \"dif\", \"injection\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T00:58:29.842565+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "gsm8k_dose_response",
  "type": "data",
  "description": "GSM8K dose-response raw results: TPR/FPR/Fisher for each p × matching_type × seed (50 rows)",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/gsm8k_dose_response.csv",
  "tags": "['plan_004', 'gsm8k', 'dose-response']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "gsm8k_dose_response",
    "type": "data",
    "description": "GSM8K dose-response raw results: TPR/FPR/Fisher for each p × matching_type × seed (50 rows)",
    "project": "irt_equated_bench_regen",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/gsm8k_dose_response.csv",
    "tags": "['plan_004', 'gsm8k', 'dose-response']"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T00:58:29.842728+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_36bb27\", \"name\": \"gsm8k_dose_response\", \"type\": \"data\", \"description\": \"GSM8K dose-response raw results: TPR/FPR/Fisher for each p × matching_type × seed (50 rows)\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/data/gsm8k_dose_response.csv\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T00:58:11.905186+00:00\", \"tags\": [\"plan_004\", \"gsm8k\", \"dose-response\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T00:58:29.842864+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "gsm8k_dose_response_summary",
  "type": "data",
  "description": "GSM8K dose-response summary: mean TPR/FPR/ΔTPR aggregated across 5 seeds per p × matching_type (10 rows)",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/gsm8k_dose_response_summary.csv",
  "tags": "['plan_004', 'gsm8k', 'dose-response', 'summary']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "gsm8k_dose_response_summary",
    "type": "data",
    "description": "GSM8K dose-response summary: mean TPR/FPR/ΔTPR aggregated across 5 seeds per p × matching_type (10 rows)",
    "project": "irt_equated_bench_regen",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/gsm8k_dose_response_summary.csv",
    "tags": "['plan_004', 'gsm8k', 'dose-response', 'summary']"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T00:58:29.843008+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_ab8247\", \"name\": \"gsm8k_dose_response_summary\", \"type\": \"data\", \"description\": \"GSM8K dose-response summary: mean TPR/FPR/ΔTPR aggregated across 5 seeds per p × matching_type (10 rows)\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/data/gsm8k_dose_response_summary.csv\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T00:58:14.383381+00:00\", \"tags\": [\"plan_004\", \"gsm8k\", \"dose-response\", \"summary\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T00:58:29.843134+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "plan_004_step2_report",
  "type": "report",
  "description": "Plan 004 Step 2 report: GSM8K semi-synthetic DIF injection results, comparison with MMLU plan_011",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step2_report.md",
  "tags": "['plan_004', 'gsm8k', 'report']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "plan_004_step2_report",
    "type": "report",
    "description": "Plan 004 Step 2 report: GSM8K semi-synthetic DIF injection results, comparison with MMLU plan_011",
    "project": "irt_equated_bench_regen",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step2_report.md",
    "tags": "['plan_004', 'gsm8k', 'report']"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T00:58:29.843314+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_42613e\", \"name\": \"plan_004_step2_report\", \"type\": \"report\", \"description\": \"Plan 004 Step 2 report: GSM8K semi-synthetic DIF injection results, comparison with MMLU plan_011\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/report/plan_004_step2_report.md\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T00:58:16.451993+00:00\", \"tags\": [\"plan_004\", \"gsm8k\", \"report\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-21T00:58:29.843481+00:00_

全部完成。核心结果：

### GSM8K vs MMLU 对比

| 指标 | MMLU plan_011 (external) | GSM8K (external) | GSM8K (standard) |
|------|--------------------------|------------------|-------------------|
| Baseline FPR | 0.314 | **0.471** | 0.191 |
| ΔTPR p=0.5 | +0.508 | **+0.514** | **+0.749** |
| ΔTPR p=1.0 | +0.674 | +0.517 | **+0.818** |

### 关键发现

1. **Standard matching 表现优于预期**：baseline FPR 仅 19.1%，ΔTPR 在 p=0.5 就达到 +0.749，p=0.7 时 TPR 已饱和至 1.000。比 MMLU 的 external matching 更强。

2. **External matching 灵敏度极高但 FPR 太高**：p=0.3 时 TPR 已达 0.970，但 baseline FPR 高达 47.1%（与 Step 1 的 47.4% C-rate 一致）。FPR 不随 p 变化（预期行为——外部分数不受 GSM8K 注入影响），但这意味着 external matching 在 GSM8K 上无法区分真实 temporal DIF 和注入污染。

3. **Standard matching 的 FPR 膨胀**：从 p=0 的 0.191 升至 p=1.0 的 0.645，符合预期——20% items 被注入时 matching variable 被污染。

4. **方法论在 GSM8K 上验证成功**：standard matching 展现清晰的 dose-response，ΔTPR 单调递增，Fisher exact test 显著。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157"
}
```

</details>

---
