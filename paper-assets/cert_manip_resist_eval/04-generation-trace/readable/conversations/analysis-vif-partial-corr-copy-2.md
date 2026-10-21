# analysis vif partial corr

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analysis_vif-partial-corr_20260522T233637.jsonl`
- **Structured JSON:** [`f103e3a7ab457b5c3bc0.json`](../../sessions/f1/f103e3a7ab457b5c3bc0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-22T23:38:37.684946+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find K_eff calculation",
  "prompt": "Find and read the file `run_condition_dominance.py` in `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/` or any subdirectory. I need to understand exactly how K_eff is computed — what formula, what data is used, and how log transforms are applied. Also find and read `src/unified_data_loader.py` to understand the data loading functions (load_all_scores, load_mi_data, ALL_MODELS, DATASETS, ATTACKS). Report the full relevant code sections."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find K_eff calculation",
    "prompt": "Find and read the file `run_condition_dominance.py` in `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/` or any subdirectory. I need to understand exactly how K_eff is computed — what formula, what data is used, and how log transforms are applied. Also find and read `src/unified_data_loader.py` to understand the data loading functions (load_all_scores, load_mi_data, ALL_MODELS, DATASETS, ATTACKS). Report the full relevant code sections."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-22T23:38:37.685285+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/**/run_condition_dominance.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/**/run_condition_dominance.py"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-22T23:38:37.685456+00:00_

scripts/run_condition_dominance.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-22T23:38:37.685592+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/**/unified_data_loader.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/**/unified_data_loader.py"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-22T23:38:37.685739+00:00_

src/unified_data_loader.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-22T23:38:37.685867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_condition_dominance.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_condition_dominance.py"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-22T23:38:37.686078+00:00_

1	#!/usr/bin/env python3
2	"""Condition-Dependent Dominance Analysis.
3	
4	For each of 12 conditions (2 datasets x 6 attacks), determines whether
5	K_eff_resid or η_max dominates panel ASR via standardized β comparison
6	and FDR-corrected significance testing.
7	
8	Output:
9	  - artifacts/results/plan001/condition_dominance_15model.json
10	"""
11	
12	import os
13	os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
14	
15	import sys
16	sys.path.insert(0, "/root/cert_manip_resist_eval")
17	
18	import json
19	import itertools
20	import numpy as np
21	import statsmodels.api as sm
22	from pathlib import Path
23	from scipy import stats
24	from statsmodels.stats.multitest import multipletests
25	from statsmodels.stats.outliers_influence import variance_inflation_factor
26	
27	from src.utils import setup_logging
28	from src.unified_data_loader import (
29	    ALL_MODELS, DATASETS, ATTACKS,
30	    load_all_scores, load_pairs, load_mi_data,
31	)
32	
33	logger = setup_logging("condition_dominance")
34	
35	EPS = 1e-6
36	FDR_ALPHA = 0.05
37	
38	MODEL_FAMILIES = {
39	    "qwen2.5-72b": "qwen", "qwen2.5-32b": "qwen", "qwen2.5-14b": "qwen",
40	    "llama3.1-70b": "meta", "llama3.1-8b": "meta",
41	    "mistral-large": "mistral",
42	    "claude-opus-4": "anthropic", "claude-sonnet-4": "anthropic",
43	    "claude-3-haiku": "anthropic",
44	    "gpt-5.5": "openai", "gpt-4.1": "openai",
45	    "gpt-4o": "openai", "gpt-4o-mini": "openai",
46	    "gemini-2.5-pro": "google", "gemini-2.5-flash": "google",
47	}
48	
49	
50	def _json_default(obj):
51	    if isinstance(obj, np.floating):
52	        v = float(obj)
53	        return None if (np.isnan(v) or np.isinf(v)) else v
54	    if isinstance(obj, np.integer):
55	        return int(obj)
56	    if isinstance(obj, np.ndarray):
57	        return obj.tolist()
58	    if isinstance(obj, np.bool_):
59	        return bool(obj)
60	    raise TypeError(f"Not JSON serializable: {type(obj)}")
61	
62	
63	def majority_vote(votes):
64	    counts = {"A": 0, "
…[truncated 16615 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T23:38:37.686247+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/src/unified_data_loader.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/src/unified_data_loader.py"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-22T23:38:37.686418+00:00_

1	#!/usr/bin/env python3
2	"""Unified data loader for 15-model cert_manip_resist_eval pipeline.
3	
4	Handles two data formats:
5	  - Checkpoint files (local 6 models): nested {clean_scores: {ds: {model: [...]}}}
6	  - Individual JSON files (API 9 models): flat {scores: [...], asr, accuracy, ...}
7	"""
8	
9	import json
10	import logging
11	from pathlib import Path
12	
13	logger = logging.getLogger(__name__)
14	
15	# ── Model lists ──────────────────────────────────────────────────────
16	LOCAL_MODELS = [
17	    "qwen2.5-72b", "llama3.1-70b", "mistral-large",
18	    "qwen2.5-32b", "qwen2.5-14b", "llama3.1-8b",
19	]
20	API_MODELS = [
21	    "claude-opus-4", "gpt-5.5", "gemini-2.5-pro", "gpt-4.1",
22	    "claude-sonnet-4", "gpt-4o", "gemini-2.5-flash",
23	    "gpt-4o-mini", "claude-3-haiku",
24	]
25	ALL_MODELS = LOCAL_MODELS + API_MODELS
26	DATASETS = ["mmlu", "arc_challenge"]
27	ATTACKS = [
28	    "prompt_injection", "sycophancy", "score_manipulation",
29	    "verbosity_bias", "position_bias", "authority_bias",
30	]
31	
32	# ── Default paths ────────────────────────────────────────────────────
33	RESULTS_DIR = Path("/root/cert_manip_resist_eval/artifacts/results")
34	PLAN001_DIR = RESULTS_DIR / "plan001"
35	SCORES_DIR = PLAN001_DIR / "individual_scores"
36	MI_PATH = PLAN001_DIR / "mi_matrix" / "mi_matrix_15models.json"
37	CKPT_FILES = [
38	    RESULTS_DIR / "_taxonomy_checkpoint.json",
39	    RESULTS_DIR / "_step2v3_checkpoint.json",
40	]
41	OUTPUT_DIR = PLAN001_DIR / "panel_regression"
42	
43	
44	def _invert_winners(scores):
45	    swap = {"A": "B", "B": "A", "tie": "tie"}
46	    return [{**s, "winner": swap.get(s.get("winner", "tie"), "tie")} for s in scores]
47	
48	
49	def load_all_scores(
50	    checkpoint_files=None,
51	    individual_dir=None,
52	    datasets=None,
53	    attacks=None,
54	    all_models=None,
55	):
56	    """Load sample-level clean + attacked scores for all 15 models.
57	
58	    Returns:
59	        clean:    {ds: {model_id: [score_dicts]}}
60	   
…[truncated 7107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T23:38:37.686634+00:00_

Perfect! I have both files. Let me now provide you with a comprehensive report on the key sections you requested.

## Summary of K_eff Computation and Data Loading

### K_eff Computation (run_condition_dominance.py)

**Location:** Lines 183-207 in `run_condition_dominance.py`

The K_eff computation uses a **standardized regression approach in log-space**:

```python
# Log transformation of variables
log_keff = np.log(p_keffs)
log_eta = np.log(p_etas + EPS)
y = np.log(p_asrs + EPS)

# Full OLS regression in log space
X = np.column_stack([log_keff, log_eta])
Xc = sm.add_constant(X)
fit_full = sm.OLS(y, Xc).fit()

# Extract standardized beta coefficients
# Standardized β = raw_β × SD(x) / SD(y)
sd_y = np.std(y)
keff_std_beta = float(fit_full.params[1] * np.std(log_keff) / sd_y)
eta_std_beta = float(fit_full.params[2] * np.std(log_eta) / sd_y)
```

**Key details:**
- **Data sources:** For each panel (3-model combination) on a given (dataset, attack) condition:
  - `p_asrs`: Panel Attack Success Rate (computed via majority-vote across 3 models)
  - `p_keffs`: K_eff value from MI matrix (loaded from `mi_data["keff_per_panel"]`)
  - `p_etas`: η_max (maximum individual ASR across the 3 models in the panel)
  
- **Log transforms applied:**
  - All three variables log-transformed: `log(ASR + eps)`, `log(K_eff)`, `log(η_max + eps)`
  - EPS = 1e-6 (constant to avoid log(0))

- **Standardized regression:**
  - Raw β coefficients from OLS
  - Standardized β = raw_β × SD(log_x) / SD(log_y)
  - This makes coefficients comparable across variables with different scales

- **Residualization check (Line 203-205):**
  ```python
  keff_resid = sm.OLS(log_keff, sm.add_constant(log_eta)).fit().resid
  fit_resid = sm.OLS(y, sm.add_constant(keff_resid)).fit()
  kresid_p_check = float(fit_resid.pvalues[1])
  ```
  Computes K_eff residualized against η_max as a verification metric.

- **Dominance determination (Lines 281-289):**
  - Uses FDR-corrected p-values (Benjamini-Hochberg, α=0.05)
  - 
…[truncated 2467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "Agent",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T23:38:37.686848+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_condition_dominance.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_condition_dominance.py"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T23:38:37.687125+00:00_

1	#!/usr/bin/env python3
2	"""Condition-Dependent Dominance Analysis.
3	
4	For each of 12 conditions (2 datasets x 6 attacks), determines whether
5	K_eff_resid or η_max dominates panel ASR via standardized β comparison
6	and FDR-corrected significance testing.
7	
8	Output:
9	  - artifacts/results/plan001/condition_dominance_15model.json
10	"""
11	
12	import os
13	os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
14	
15	import sys
16	sys.path.insert(0, "/root/cert_manip_resist_eval")
17	
18	import json
19	import itertools
20	import numpy as np
21	import statsmodels.api as sm
22	from pathlib import Path
23	from scipy import stats
24	from statsmodels.stats.multitest import multipletests
25	from statsmodels.stats.outliers_influence import variance_inflation_factor
26	
27	from src.utils import setup_logging
28	from src.unified_data_loader import (
29	    ALL_MODELS, DATASETS, ATTACKS,
30	    load_all_scores, load_pairs, load_mi_data,
31	)
32	
33	logger = setup_logging("condition_dominance")
34	
35	EPS = 1e-6
36	FDR_ALPHA = 0.05
37	
38	MODEL_FAMILIES = {
39	    "qwen2.5-72b": "qwen", "qwen2.5-32b": "qwen", "qwen2.5-14b": "qwen",
40	    "llama3.1-70b": "meta", "llama3.1-8b": "meta",
41	    "mistral-large": "mistral",
42	    "claude-opus-4": "anthropic", "claude-sonnet-4": "anthropic",
43	    "claude-3-haiku": "anthropic",
44	    "gpt-5.5": "openai", "gpt-4.1": "openai",
45	    "gpt-4o": "openai", "gpt-4o-mini": "openai",
46	    "gemini-2.5-pro": "google", "gemini-2.5-flash": "google",
47	}
48	
49	
50	def _json_default(obj):
51	    if isinstance(obj, np.floating):
52	        v = float(obj)
53	        return None if (np.isnan(v) or np.isinf(v)) else v
54	    if isinstance(obj, np.integer):
55	        return int(obj)
56	    if isinstance(obj, np.ndarray):
57	        return obj.tolist()
58	    if isinstance(obj, np.bool_):
59	        return bool(obj)
60	    raise TypeError(f"Not JSON serializable: {type(obj)}")
61	
62	
63	def majority_vote(votes):
64	    counts = {"A": 0, "
…[truncated 16615 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T23:38:37.687323+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T23:38:37.687453+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T23:38:37.687717+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat > /root/cert_manip_resist_eval/scripts/run_vif_partial_corr.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"VIF + Partial Correlation analysis for K_eff and η_max.\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nimport statsmodels.api as sm\nfrom pathlib import Path\nfrom scipy import stats\n\nfrom src.unified_data_loader import (\n    ALL_MODELS, DATASETS, ATTACKS,\n    load_all_scores, load_pairs, load_mi_data,\n)\n\nEPS = 1e-6\n\nMODEL_FAMILIES = {\n    \"qwen2.5-72b\": \"qwen\", \"qwen2.5-32b\": \"qwen\", \"qwen2.5-14b\": \"qwen\",\n    \"llama3.1-70b\": \"meta\", \"llama3.1-8b\": \"meta\",\n    \"mistral-large\": \"mistral\",\n    \"claude-opus-4\": \"anthropic\", \"claude-sonnet-4\": \"anthropic\",\n    \"claude-3-haiku\": \"anthropic\",\n    \"gpt-5.5\": \"openai\", \"gpt-4.1\": \"openai\",\n    \"gpt-4o\": \"openai\", \"gpt-4o-mini\": \"openai\",\n    \"gemini-2.5-pro\": \"google\", \"gemini-2.5-flash\": \"google\",\n}\n\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i].get(\"winner\", \"tie\") == gt:\n            n_correct += 1\n            if attacked_list[i].get(\"winner\", \"tie\") != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef compute_panel_asr(jids, clean, attacked, pairs):\n    n = min(len(pairs), *(len(clean[j]) for j in jids),\n            *(len(attacked[j]) for j in jids))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean[j][i].get(\"winner\", \"tie\") for j in jids])\n        if cv != gt:\n            continue\n        n_correct += 1\n        av = majority_vote([attacked[j][i].get(\"winner\", \"tie\") for j in jids])\n        if av != gt:\n            n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef partial_corr(x, y, z):\n    \"\"\"Partial correlation r(x, y | z) via residualization.\"\"\"\n    resid_x = sm.OLS(x, sm.add_constant(z)).fit().resid\n    resid_y = sm.OLS(y, sm.add_constant(z)).fit().resid\n    r, p = stats.pearsonr(resid_x, resid_y)\n    return float(r), float(p)\n\n\ndef compute_vif_two_predictors(x1, x2):\n    \"\"\"VIF for two predictors = 1/(1-R^2) where R^2 from regressing x1 on x2.\"\"\"\n    fit = sm.OLS(x1, sm.add_constant(x2)).fit()\n    return 1.0 / (1.0 - fit.rsquared)\n\n\ndef main():\n    print(\"Loading data...\")\n    mi_data = load_mi_data()\n    pairs = load_pairs()\n    clean, attacked = load_all_scores()\n\n    # Individual ASR\n    ind_asr = {}\n    for ds in DATASETS:\n        for atk in ATTACKS:\n            for mid in ALL_MODELS:\n                if mid in clean[ds] and mid in attacked[ds][atk]:\n                    ind_asr[(ds, atk, mid)] = compute_individual_asr(\n                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]\n                    )\n\n    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))\n\n    vif_per_condition = {}\n    partial_per_condition = {}\n\n    for ds in DATASETS:\n        keff_data = mi_data[\"keff_per_panel\"].get(ds, {})\n        for atk in ATTACKS:\n            cond = f\"{ds}x{atk}\"\n\n            p_asrs, p_keffs, p_etas = [], [], []\n            for combo in all_combos:\n                jids = [ALL_MODELS[i] for i in combo]\n                if not all((ds, atk, j) in ind_asr for j in jids):\n                    continue\n                pk = \"|\".join(jids)\n                if pk not in keff_data:\n                    continue\n\n                keff = keff_data[pk][\"keff\"]\n                etas = [ind_asr[(ds, atk, j)] for j in jids]\n                eta_max = max(etas)\n\n                cs = {j: clean[ds][j] for j in jids}\n                ats = {j: attacked[ds][atk][j] for j in jids}\n                p_asr = compute_panel_asr(jids, cs, ats, pairs[ds])\n\n                p_asrs.append(p_asr)\n                p_keffs.append(keff)\n                p_etas.append(eta_max)\n\n            n_panels = len(p_asrs)\n            if n_panels < 10:\n                continue\n\n            p_asrs = np.array(p_asrs)\n            p_keffs = np.array(p_keffs)\n            p_etas = np.array(p_etas)\n\n            if np.std(p_asrs) < 1e-10:\n                continue\n\n            log_keff = np.log(p_keffs)\n            log_eta = np.log(p_etas + EPS)\n            log_asr = np.log(p_asrs + EPS)\n\n            # VIF between the two predictors\n            vif = compute_vif_two_predictors(log_keff, log_eta)\n            vif_per_condition[cond] = round(vif, 4)\n\n            # Partial correlations\n            r_eta_given_keff, p_eta_given_keff = partial_corr(log_eta, log_asr, log_keff)\n            r_keff_given_eta, p_keff_given_eta = partial_corr(log_keff, log_asr, log_eta)\n\n            partial_per_condition[cond] = {\n                \"eta_given_keff\": {\"r\": round(r_eta_given_keff, 4), \"p\": float(f\"{p_eta_given_keff:.6e}\")},\n                \"keff_given_eta\": {\"r\": round(r_keff_given_eta, 4), \"p\": float(f\"{p_keff_given_eta:.6e}\")},\n            }\n\n            print(f\"{cond}: VIF={vif:.4f}  \"\n                  f\"r(η|K)={r_eta_given_keff:+.4f} p={p_eta_given_keff:.2e}  \"\n                  f\"r(K|η)={r_keff_given_eta:+.4f} p={p_keff_given_eta:.2e}\")\n\n    # Summary\n    vif_vals = list(vif_per_condition.values())\n    vif_summary = {\n        \"mean\": round(float(np.mean(vif_vals)), 4),\n        \"min\": round(float(np.min(vif_vals)), 4),\n        \"max\": round(float(np.max(vif_vals)), 4),\n    }\n\n    eta_rs = [v[\"eta_given_keff\"][\"r\"] for v in partial_per_condition.values()]\n    keff_rs = [v[\"keff_given_eta\"][\"r\"] for v in partial_per_condition.values()]\n    eta_ps = [v[\"eta_given_keff\"][\"p\"] for v in partial_per_condition.values()]\n    keff_ps = [v[\"keff_given_eta\"][\"p\"] for v in partial_per_condition.values()]\n\n    eta_sig = sum(1 for p in eta_ps if p < 0.05)\n    keff_sig = sum(1 for p in keff_ps if p < 0.05)\n\n    partial_summary = {\n        \"eta_given_keff_mean_r\": round(float(np.mean(eta_rs)), 4),\n        \"keff_given_eta_mean_r\": round(float(np.mean(keff_rs)), 4),\n        \"eta_sig_count\": f\"{eta_sig}/{len(eta_rs)}\",\n        \"keff_sig_count\": f\"{keff_sig}/{len(keff_rs)}\",\n    }\n\n    output = {\n        \"vif\": {\n            \"per_condition\": vif_per_condition,\n            **vif_summary,\n        },\n        \"partial_correlation\": {\n            \"per_condition\": partial_per_condition,\n            \"summary\": partial_summary,\n        },\n    }\n\n    out_path = Path(\"/root/cert_manip_resist_eval/artifacts/results/plan001/vif_partial_corr.json\")\n    out_path.parent.mkdir(parents=True, exist_ok=True)\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n\n    print(f\"\\nVIF: mean={vif_summary['mean']}, min={vif_summary['min']}, max={vif_summary['max']}\")\n    print(f\"Partial r(η|K): mean={partial_summary['eta_given_keff_mean_r']}, sig={partial_summary['eta_sig_count']}\")\n    print(f\"Partial r(K|η): mean={partial_summary['keff_given_eta_mean_r']}, sig={partial_summary['keff_sig_count']}\")\n    print(f\"\\nSaved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cat > /root/cert_manip_resist_eval/scripts/run_vif_partial_corr.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"VIF + Partial Correlation analysis for K_eff and η_max.\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nimport statsmodels.api as sm\nfrom pathlib import Path\nfrom scipy import stats\n\nfrom src.unified_data_loader import (\n    ALL_MODELS, DATASETS, ATTACKS,\n    load_all_scores, load_pairs, load_mi_data,\n)\n\nEPS = 1e-6\n\nMODEL_FAMILIES = {\n    \"qwen2.5-72b\": \"qwen\", \"qwen2.5-32b\": \"qwen\", \"qwen2.5-14b\": \"qwen\",\n    \"llama3.1-70b\": \"meta\", \"llama3.1-8b\": \"meta\",\n    \"mistral-large\": \"mistral\",\n    \"claude-opus-4\": \"anthropic\", \"claude-sonnet-4\": \"anthropic\",\n    \"claude-3-haiku\": \"anthropic\",\n    \"gpt-5.5\": \"openai\", \"gpt-4.1\": \"openai\",\n    \"gpt-4o\": \"openai\", \"gpt-4o-mini\": \"openai\",\n    \"gemini-2.5-pro\": \"google\", \"gemini-2.5-flash\": \"google\",\n}\n\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i].get(\"winner\", \"tie\") == gt:\n            n_correct += 1\n            if attacked_list[i].get(\"winner\", \"tie\") != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef compute_panel_asr(jids, clean, attacked, pairs):\n    n = min(len(pairs), *(len(clean[j]) for j in jids),\n            *(len(attacked[j]) for j in jids))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean[j][i].get(\"winner\", \"tie\") for j in jids])\n        if cv != gt:\n            continue\n        n_correct += 1\n        av = majority_vote([attacked[j][i].get(\"winner\", \"tie\") for j in jids])\n        if av != gt:\n            n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef partial_corr(x, y, z):\n    \"\"\"Partial correlation r(x, y | z) via residualization.\"\"\"\n    resid_x = sm.OLS(x, sm.add_constant(z)).fit().resid\n    resid_y = sm.OLS(y, sm.add_constant(z)).fit().resid\n    r, p = stats.pearsonr(resid_x, resid_y)\n    return float(r), float(p)\n\n\ndef compute_vif_two_predictors(x1, x2):\n    \"\"\"VIF for two predictors = 1/(1-R^2) where R^2 from regressing x1 on x2.\"\"\"\n    fit = sm.OLS(x1, sm.add_constant(x2)).fit()\n    return 1.0 / (1.0 - fit.rsquared)\n\n\ndef main():\n    print(\"Loading data...\")\n    mi_data = load_mi_data()\n    pairs = load_pairs()\n    clean, attacked = load_all_scores()\n\n    # Individual ASR\n    ind_asr = {}\n    for ds in DATASETS:\n        for atk in ATTACKS:\n            for mid in ALL_MODELS:\n                if mid in clean[ds] and mid in attacked[ds][atk]:\n                    ind_asr[(ds, atk, mid)] = compute_individual_asr(\n                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]\n                    )\n\n    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))\n\n    vif_per_condition = {}\n    partial_per_condition = {}\n\n    for ds in DATASETS:\n        keff_data = mi_data[\"keff_per_panel\"].get(ds, {})\n        for atk in ATTACKS:\n            cond = f\"{ds}x{atk}\"\n\n            p_asrs, p_keffs, p_etas = [], [], []\n            for combo in all_combos:\n                jids = [ALL_MODELS[i] for i in combo]\n                if not all((ds, atk, j) in ind_asr for j in jids):\n                    continue\n                pk = \"|\".join(jids)\n                if pk not in keff_data:\n                    continue\n\n                keff = keff_data[pk][\"keff\"]\n                etas = [ind_asr[(ds, atk, j)] for j in jids]\n                eta_max = max(etas)\n\n                cs = {j: clean[ds][j] for j in jids}\n                ats = {j: attacked[ds][atk][j] for j in jids}\n                p_asr = compute_panel_asr(jids, cs, ats, pairs[ds])\n\n                p_asrs.append(p_asr)\n                p_keffs.append(keff)\n                p_etas.append(eta_max)\n\n            n_panels = len(p_asrs)\n            if n_panels < 10:\n                continue\n\n            p_asrs = np.array(p_asrs)\n            p_keffs = np.array(p_keffs)\n            p_etas = np.array(p_etas)\n\n            if np.std(p_asrs) < 1e-10:\n                continue\n\n            log_keff = np.log(p_keffs)\n            log_eta = np.log(p_etas + EPS)\n            log_asr = np.log(p_asrs + EPS)\n\n            # VIF between the two predictors\n            vif = compute_vif_two_predictors(log_keff, log_eta)\n            vif_per_condition[cond] = round(vif, 4)\n\n            # Partial correlations\n            r_eta_given_keff, p_eta_given_keff = partial_corr(log_eta, log_asr, log_keff)\n            r_keff_given_eta, p_keff_given_eta = partial_corr(log_keff, log_asr, log_eta)\n\n            partial_per_condition[cond] = {\n                \"eta_given_keff\": {\"r\": round(r_eta_given_keff, 4), \"p\": float(f\"{p_eta_given_keff:.6e}\")},\n                \"keff_given_eta\": {\"r\": round(r_keff_given_eta, 4), \"p\": float(f\"{p_keff_given_eta:.6e}\")},\n            }\n\n            print(f\"{cond}: VIF={vif:.4f}  \"\n                  f\"r(η|K)={r_eta_given_keff:+.4f} p={p_eta_given_keff:.2e}  \"\n                  f\"r(K|η)={r_keff_given_eta:+.4f} p={p_keff_given_eta:.2e}\")\n\n    # Summary\n    vif_vals = list(vif_per_condition.values())\n    vif_summary = {\n        \"mean\": round(float(np.mean(vif_vals)), 4),\n        \"min\": round(float(np.min(vif_vals)), 4),\n        \"max\": round(float(np.max(vif_vals)), 4),\n    }\n\n    eta_rs = [v[\"eta_given_keff\"][\"r\"] for v in partial_per_condition.values()]\n    keff_rs = [v[\"keff_given_eta\"][\"r\"] for v in partial_per_condition.values()]\n    eta_ps = [v[\"eta_given_keff\"][\"p\"] for v in partial_per_condition.values()]\n    keff_ps = [v[\"keff_given_eta\"][\"p\"] for v in partial_per_condition.values()]\n\n    eta_sig = sum(1 for p in eta_ps if p < 0.05)\n    keff_sig = sum(1 for p in keff_ps if p < 0.05)\n\n    partial_summary = {\n        \"eta_given_keff_mean_r\": round(float(np.mean(eta_rs)), 4),\n        \"keff_given_eta_mean_r\": round(float(np.mean(keff_rs)), 4),\n        \"eta_sig_count\": f\"{eta_sig}/{len(eta_rs)}\",\n        \"keff_sig_count\": f\"{keff_sig}/{len(keff_rs)}\",\n    }\n\n    output = {\n        \"vif\": {\n            \"per_condition\": vif_per_condition,\n            **vif_summary,\n        },\n        \"partial_correlation\": {\n            \"per_condition\": partial_per_condition,\n            \"summary\": partial_summary,\n        },\n    }\n\n    out_path = Path(\"/root/cert_manip_resist_eval/artifacts/results/plan001/vif_partial_corr.json\")\n    out_path.parent.mkdir(parents=True, exist_ok=True)\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n\n    print(f\"\\nVIF: mean={vif_summary['mean']}, min={vif_summary['min']}, max={vif_summary['max']}\")\n    print(f\"Partial r(η|K): mean={partial_summary['eta_given_keff_mean_r']}, sig={partial_summary['eta_sig_count']}\")\n    print(f\"Partial r(K|η): mean={partial_summary['keff_given_eta_mean_r']}, sig={partial_summary['keff_sig_count']}\")\n    print(f\"\\nSaved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\""
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T23:38:37.687964+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T23:38:37.688094+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cert_manip_resist_eval && python scripts/run_vif_partial_corr.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cert_manip_resist_eval && python scripts/run_vif_partial_corr.py"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T23:38:37.688237+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading data...\\nmmluxprompt_injection: VIF=1.9923  r(η|K)=+0.6006 p=5.95e-46  r(K|η)=+0.2943 p=1.53e-10\\nmmluxsycophancy: VIF=1.2349  r(η|K)=+0.4727 p=1.05e-26  r(K|η)=+0.1797 p=1.16e-04\\nmmluxscore_manipulation: VIF=3.0201  r(η|K)=+0.4031 p=3.31e-19  r(K|η)=+0.0242 p=6.07e-01\\nmmluxverbosity_bias: VIF=1.2456  r(η|K)=+0.5679 p=3.25e-40  r(K|η)=+0.1045 p=2.58e-02\\nmmluxposition_bias: VIF=1.7790  r(η|K)=+0.3390 p=1.07e-13  r(K|η)=+0.0893 p=5.71e-02\\nmmluxauthority_bias: VIF=1.6270  r(η|K)=+0.3046 p=3.20e-11  r(K|η)=+0.0088 p=8.52e-01\\narc_challengexprompt_injection: VIF=3.3828  r(η|K)=+0.1569 p=7.86e-04  r(K|η)=+0.2100 p=6.27e-06\\narc_challengexsycophancy: VIF=2.5402  r(η|K)=+0.3148 p=6.35e-12  r(K|η)=-0.1280 p=6.24e-03\\narc_challengexscore_manipulation: VIF=7.0271  r(η|K)=+0.0952 p=4.23e-02  r(K|η)=+0.1070 p=2.24e-02\\narc_challengexverbosity_bias: VIF=3.2007  r(η|K)=+0.2125 p=4.83e-06  r(K|η)=+0.0918 p=5.03e-02\\narc_challengexposition_bias: VIF=6.5318  r(η|K)=-0.0054 p=9.09e-01  r(K|η)=+0.2688 p=5.67e-09\\narc_challengexauthority_bias: VIF=2.1595  r(η|K)=+0.1927 p=3.49e-05  r(K|η)=+0.1447 p=1.97e-03\\n\\nVIF: mean=2.9784, min=1.2349, max=7.0271\\nPartial r(η|K): mean=0.3046, sig=11/12\\nPartial r(K|η): mean=0.1163, sig=8/12\\n\\nSaved: /root/cert_manip_resist_eval/artifacts/results/plan001/vif_partial_corr.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.12}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T23:38:37.688387+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat /root/cert_manip_resist_eval/artifacts/results/plan001/vif_partial_corr.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cat /root/cert_manip_resist_eval/artifacts/results/plan001/vif_partial_corr.json"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T23:38:37.688587+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"vif\\\": {\\n    \\\"per_condition\\\": {\\n      \\\"mmluxprompt_injection\\\": 1.9923,\\n      \\\"mmluxsycophancy\\\": 1.2349,\\n      \\\"mmluxscore_manipulation\\\": 3.0201,\\n      \\\"mmluxverbosity_bias\\\": 1.2456,\\n      \\\"mmluxposition_bias\\\": 1.779,\\n      \\\"mmluxauthority_bias\\\": 1.627,\\n      \\\"arc_challengexprompt_injection\\\": 3.3828,\\n      \\\"arc_challengexsycophancy\\\": 2.5402,\\n      \\\"arc_challengexscore_manipulation\\\": 7.0271,\\n      \\\"arc_challengexverbosity_bias\\\": 3.2007,\\n      \\\"arc_challengexposition_bias\\\": 6.5318,\\n      \\\"arc_challengexauthority_bias\\\": 2.1595\\n    },\\n    \\\"mean\\\": 2.9784,\\n    \\\"min\\\": 1.2349,\\n    \\\"max\\\": 7.0271\\n  },\\n  \\\"partial_correlation\\\": {\\n    \\\"per_condition\\\": {\\n      \\\"mmluxprompt_injection\\\": {\\n        \\\"eta_given_keff\\\": {\\n          \\\"r\\\": 0.6006,\\n          \\\"p\\\": 5.948303e-46\\n        },\\n        \\\"keff_given_eta\\\": {\\n          \\\"r\\\": 0.2943,\\n          \\\"p\\\": 1.533901e-10\\n        }\\n      },\\n      \\\"mmluxsycophancy\\\": {\\n        \\\"eta_given_keff\\\": {\\n          \\\"r\\\": 0.4727,\\n          \\\"p\\\": 1.050395e-26\\n        },\\n        \\\"keff_given_eta\\\": {\\n          \\\"r\\\": 0.1797,\\n          \\\"p\\\": 0.0001164105\\n        }\\n      },\\n      \\\"mmluxscore_manipulation\\\": {\\n        \\\"eta_given_keff\\\": {\\n          \\\"r\\\": 0.4031,\\n          \\\"p\\\": 3.313542e-19\\n        },\\n        \\\"keff_given_eta\\\": {\\n          \\\"r\\\": 0.0242,\\n          \\\"p\\\": 0.606678\\n        }\\n      },\\n      \\\"mmluxverbosity_bias\\\": {\\n        \\\"eta_given_keff\\\": {\\n          \\\"r\\\": 0.5679,\\n          \\\"p\\\": 3.251142e-40\\n        },\\n        \\\"keff_given_eta\\\": {\\n          \\\"r\\\": 0.1045,\\n          \\\"p\\\": 0.02582004\\n        }\\n      },\\n      \\\"mmlu
…[truncated 2606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_vif-partial-corr_20260522T233637",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-22T23:38:37.688800+00:00_

完成。结果已保存到 `/root/cert_manip_resist_eval/artifacts/results/plan001/vif_partial_corr.json`。

**VIF 结果：**
- Mean = 2.98, Min = 1.23 (mmlu×sycophancy), Max = 7.03 (arc_challenge×score_manipulation)
- 高于预期的 ~1.96，arc_challenge 上几个条件 VIF 较高（score_manipulation 7.03, position_bias 6.53），说明这些条件下 log(K_eff) 和 log(η_max) 共线性较强

**Partial Correlation 结果：**
- η_max → ASR | K_eff: mean r = 0.305, 11/12 conditions 显著 (p < 0.05)
- K_eff → ASR | η_max: mean r = 0.116, 8/12 conditions 显著 (p < 0.05)
- η_max 控制 K_eff 后仍有较强独立解释力；K_eff 控制 η_max 后效应较弱但多数条件仍显著

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_vif-partial-corr_20260522T233637"
}
```

</details>

---
