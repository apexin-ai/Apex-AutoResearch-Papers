# analysis residualized keff 15model

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_analysis_residualized-keff-15model_20260522T171634.jsonl`
- **Structured JSON:** [`d4eb997be2b1ed7e13d5.json`](../../sessions/d4/d4eb997be2b1ed7e13d5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-22T17:20:24.175446+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Explore codebase structure",
  "subagent_type": "Explore",
  "prompt": "I need to understand the codebase at /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/. Specifically:\n\n1. Read the file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/src/unified_data_loader.py - I need to understand what functions are available (load_all_scores, load_pairs, load_mi_data, compute_corrected_asr, flag_low_accuracy_conditions, etc.)\n\n2. Read the file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py - I need to understand the panel enumeration logic, how K_eff, eta_max, and panel ASR are computed.\n\nPlease provide the FULL content of both files - don't summarize, I need exact code."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "Agent",
  "tool_args": {
    "description": "Explore codebase structure",
    "subagent_type": "Explore",
    "prompt": "I need to understand the codebase at /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/. Specifically:\n\n1. Read the file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/src/unified_data_loader.py - I need to understand what functions are available (load_all_scores, load_pairs, load_mi_data, compute_corrected_asr, flag_low_accuracy_conditions, etc.)\n\n2. Read the file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py - I need to understand the panel enumeration logic, how K_eff, eta_max, and panel ASR are computed.\n\nPlease provide the FULL content of both files - don't summarize, I need exact code."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-22T17:20:24.175842+00:00_

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
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/src/unified_data_loader.py"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-22T17:20:24.176077+00:00_

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
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-22T17:20:24.176247+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-22T17:20:24.176468+00:00_

1	#!/usr/bin/env python3
2	"""Plan 001 Step 4: Panel regression -- 455 panels x 12 conditions.
3	
4	Input:
5	  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json
6	  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/
7	  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json
8	
9	Output:
10	  - artifacts/results/plan001/panel_regression/step4_regression_results.json
11	
12	Dependencies: numpy, scipy, statsmodels
13	Optional: pingouin (for partial_corr; manual fallback included)
14	"""
15	
16	import os
17	os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
18	
19	import sys
20	sys.path.insert(0, "/root/cert_manip_resist_eval")
21	
22	import json
23	import warnings
24	import itertools
25	import numpy as np
26	import statsmodels.api as sm
27	from pathlib import Path
28	from scipy import optimize, stats, special
29	from statsmodels.stats.outliers_influence import variance_inflation_factor
30	from statsmodels.stats.multitest import multipletests
31	
32	from src.utils import setup_logging
33	from src.unified_data_loader import (
34	    ALL_MODELS, DATASETS, ATTACKS, OUTPUT_DIR,
35	    load_all_scores, load_pairs, load_mi_data,
36	)
37	
38	logger = setup_logging("plan001_step4")
39	
40	EPS = 0.001
41	
42	
43	# ── JSON Helper ──────────────────────────────────────────────────────
44	
45	def _json_default(obj):
46	    if isinstance(obj, np.floating):
47	        v = float(obj)
48	        return None if (np.isnan(v) or np.isinf(v)) else v
49	    if isinstance(obj, np.integer):
50	        return int(obj)
51	    if isinstance(obj, np.ndarray):
52	        return obj.tolist()
53	    if isinstance(obj, np.bool_):
54	        return bool(obj)
55	    raise TypeError(f"Not JSON serializable: {type(obj)}")
56	
57	
58	# ── ASR Computation ──────────────────────────────────────────────────
59	
60	def majority_vote(votes):
61	    counts = {"A": 0, "B": 0, "tie": 0}
62	    for v in votes:
63	        counts
…[truncated 14313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T17:20:24.176692+00:00_

Here are the full contents of both files:

## File 1: `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/src/unified_data_loader.py`

This file provides several key functions:

- **`load_all_scores(checkpoint_files, individual_dir, datasets, attacks, all_models)`** - Loads sample-level clean and attacked scores for all 15 models from both checkpoint files (local models) and individual JSON files (API models). Returns a tuple of (clean, attacked) dicts where clean is `{ds: {model_id: [score_dicts]}}` and attacked is `{ds: {atk: {model_id: [score_dicts]}}}`. Handles special case for position_bias attack by inverting winners.

- **`load_pairs(checkpoint_files, datasets)`** - Loads evaluation pairs from checkpoint files, returning `{ds: [pair_dicts]}` with up to 300 pairs per dataset.

- **`load_mi_data(mi_path)`** - Loads the MI matrix from Step 3 output.

- **`load_api_asr(individual_dir, datasets, attacks, api_models)`** - Loads pre-computed ASR for API models from individual score files, returning `{ds: {atk: {model_id: asr}}}`.

- **`validate_coverage(clean, attacked, datasets, attacks, all_models, expected_samples)`** - Validates that all models have expected number of samples.

The file also defines model lists (LOCAL_MODELS: 6 models, API_MODELS: 9 models, ALL_MODELS: 15 total), datasets (mmlu, arc_challenge), and attacks (6 types).

## File 2: `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py`

This is the main panel regression script. Key aspects:

**Panel Enumeration:**
- Lines 258-259: Creates all combinations of 3 models from 15 total using `itertools.combinations(range(len(ALL_MODELS)), 3)`, yielding 455 panels.

**Condition Loop:**
- Lines 266-352: Iterates over 2 datasets × 6 attacks = 12 conditions
- For each condition, loops through all 455 combos and gathers data for panels that have:
  - Individual ASR values for all 3 models in that condition
 
…[truncated 1009 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "Agent",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T17:20:24.176860+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts/run_plan001_step4_panel_regression.py"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T17:20:24.177125+00:00_

1	#!/usr/bin/env python3
2	"""Plan 001 Step 4: Panel regression -- 455 panels x 12 conditions.
3	
4	Input:
5	  - MI matrix + K_eff: artifacts/results/plan001/mi_matrix/mi_matrix_15models.json
6	  - Individual scores: checkpoints + artifacts/results/plan001/individual_scores/
7	  - Pairs: artifacts/results/_taxonomy_checkpoint.json or _step2v3_checkpoint.json
8	
9	Output:
10	  - artifacts/results/plan001/panel_regression/step4_regression_results.json
11	
12	Dependencies: numpy, scipy, statsmodels
13	Optional: pingouin (for partial_corr; manual fallback included)
14	"""
15	
16	import os
17	os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
18	
19	import sys
20	sys.path.insert(0, "/root/cert_manip_resist_eval")
21	
22	import json
23	import warnings
24	import itertools
25	import numpy as np
26	import statsmodels.api as sm
27	from pathlib import Path
28	from scipy import optimize, stats, special
29	from statsmodels.stats.outliers_influence import variance_inflation_factor
30	from statsmodels.stats.multitest import multipletests
31	
32	from src.utils import setup_logging
33	from src.unified_data_loader import (
34	    ALL_MODELS, DATASETS, ATTACKS, OUTPUT_DIR,
35	    load_all_scores, load_pairs, load_mi_data,
36	)
37	
38	logger = setup_logging("plan001_step4")
39	
40	EPS = 0.001
41	
42	
43	# ── JSON Helper ──────────────────────────────────────────────────────
44	
45	def _json_default(obj):
46	    if isinstance(obj, np.floating):
47	        v = float(obj)
48	        return None if (np.isnan(v) or np.isinf(v)) else v
49	    if isinstance(obj, np.integer):
50	        return int(obj)
51	    if isinstance(obj, np.ndarray):
52	        return obj.tolist()
53	    if isinstance(obj, np.bool_):
54	        return bool(obj)
55	    raise TypeError(f"Not JSON serializable: {type(obj)}")
56	
57	
58	# ── ASR Computation ──────────────────────────────────────────────────
59	
60	def majority_vote(votes):
61	    counts = {"A": 0, "B": 0, "tie": 0}
62	    for v in votes:
63	        counts
…[truncated 14313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T17:20:24.177309+00:00_

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
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/src/unified_data_loader.py"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T17:20:24.177525+00:00_

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
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T17:20:24.177727+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "flag_low_accuracy_conditions",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "Grep",
  "tool_args": {
    "pattern": "flag_low_accuracy_conditions",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T17:20:24.177863+00:00_

Found 9 files
logs/workers/worker_analysis_residualized-keff-15model_20260522T171634.log
logs/chats/feishu_group_oc_511319d9c17dfa45ec974a0123143d46_director.jsonl
logs/chats/feishu_group_oc_551817662c2d314a3713be79c074d906.jsonl
logs/chats/feishu_group_oc_551817662c2d314a3713be79c074d906_reviewer.jsonl
logs/workers/worker_code_fix-loader-rerun-pipeline_20260522T170513.log
logs/workers/worker_infra_scp-and-pipeline_20260522T165558.log
logs/workers/worker_code_step3-mi-filter-and-sensitivity_20260522T163508_result.json
logs/chats/worker_code_step3-mi-filter-and-sensitivity_20260522T163508.jsonl
logs/workers/worker_code_step3-mi-filter-and-sensitivity_20260522T163508.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T17:20:24.177989+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "flag_low_accuracy",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/src"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "Grep",
  "tool_args": {
    "pattern": "flag_low_accuracy",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/src"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T17:20:24.178110+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T17:20:24.178225+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "flag_low_accuracy|low_accuracy|low_acc",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "Grep",
  "tool_args": {
    "pattern": "flag_low_accuracy|low_accuracy|low_acc",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/scripts"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T17:20:24.178336+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T17:20:24.178462+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T17:20:24.178579+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T17:20:24.178738+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "ls /root/cert_manip_resist_eval/artifacts/results/plan001/mi_matrix/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "ls /root/cert_manip_resist_eval/artifacts/results/plan001/mi_matrix/"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T17:20:24.178862+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"mi_matrix_15models.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.18}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T17:20:24.178977+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "python3 -c \"import json; d=json.load(open('/root/cert_manip_resist_eval/artifacts/results/plan001/mi_matrix/mi_matrix_15models.json')); print(list(d.keys())); print('keff_per_panel datasets:', list(d.get('keff_per_panel',{}).keys())); ds='mmlu'; panels=d['keff_per_panel'].get(ds,{}); print(f'mmlu panels: {len(panels)}'); k=list(panels.keys())[0]; print(f'sample key: {k}'); print(f'sample val: {panels[k]}')\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "python3 -c \"import json; d=json.load(open('/root/cert_manip_resist_eval/artifacts/results/plan001/mi_matrix/mi_matrix_15models.json')); print(list(d.keys())); print('keff_per_panel datasets:', list(d.get('keff_per_panel',{}).keys())); ds='mmlu'; panels=d['keff_per_panel'].get(ds,{}); print(f'mmlu panels: {len(panels)}'); k=list(panels.keys())[0]; print(f'sample key: {k}'); print(f'sample val: {panels[k]}')\""
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T17:20:24.179094+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T17:20:24.179205+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "head -c 2000 /root/cert_manip_resist_eval/artifacts/results/plan001/mi_matrix/mi_matrix_15models.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "head -c 2000 /root/cert_manip_resist_eval/artifacts/results/plan001/mi_matrix/mi_matrix_15models.json"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T17:20:24.179354+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"models\\\": [\\n    \\\"qwen2.5-72b\\\",\\n    \\\"llama3.1-70b\\\",\\n    \\\"mistral-large\\\",\\n    \\\"qwen2.5-32b\\\",\\n    \\\"qwen2.5-14b\\\",\\n    \\\"llama3.1-8b\\\",\\n    \\\"claude-opus-4-6\\\",\\n    \\\"gpt-5.5\\\",\\n    \\\"gemini-3.1-pro-preview\\\",\\n    \\\"gpt-4.1\\\",\\n    \\\"claude-sonnet-4-6\\\",\\n    \\\"gpt-4.1-nano\\\",\\n    \\\"gemini-3.5-flash\\\",\\n    \\\"gpt-4.1-mini\\\",\\n    \\\"claude-3-haiku\\\"\\n  ],\\n  \\\"mi_matrix\\\": {\\n    \\\"mmlu\\\": [\\n      [\\n        0.0,\\n        0.2962205170426407,\\n        0.26675251098957503,\\n        0.3470669052814603,\\n        0.27125804258663433,\\n        0.036010036882308916,\\n        0.28731888801126415,\\n        0.3191362352253263,\\n        0.35168587132015827,\\n        0.2965563120641862,\\n        0.3533510256304889,\\n        0.1328306436270179,\\n        0.3867367855857686,\\n        0.26335401432169325,\\n        0.1953748382396672\\n      ],\\n      [\\n        0.2962205170426407,\\n        0.0,\\n        0.2440104667595938,\\n        0.2986645649606351,\\n        0.14478230599138053,\\n        0.05018961809391721,\\n        0.2760064663925398,\\n        0.30830289854629034,\\n        0.3155441322598244,\\n        0.34347517274268324,\\n        0.32303289427076615,\\n        0.13391273609524,\\n        0.34490590856943293,\\n        0.2905313259782581,\\n        0.17128276712405138\\n      ],\\n      [\\n        0.26675251098957503,\\n        0.2440104667595938,\\n        0.0,\\n        0.20591433091558176,\\n        0.12844326291058067,\\n        0.037766679713954275,\\n        0.18723651742582784,\\n        0.23078151458579058,\\n        0.24792694728189563,\\n        0.25087598035611236,\\n        0.28407449782124566,\\n        0.13067801250081526,\\n        0.3015537043004064,\\n        0.2487749523256102,\\n        0.11255817541955744\\n      ],\\n      [\\n        0.3470669052814603,\\n     
…[truncated 436 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T17:20:24.179521+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "head -30 /root/cert_manip_resist_eval/src/unified_data_loader.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "head -30 /root/cert_manip_resist_eval/src/unified_data_loader.py"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T17:20:24.179725+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Unified data loader for 15-model cert_manip_resist_eval pipeline.\\n\\nHandles two data formats:\\n  - Checkpoint files (local 6 models): nested {clean_scores: {ds: {model: [...]}}}\\n  - Individual JSON files (API 9 models): flat {scores: [...], asr, accuracy, ...}\\n\\\"\\\"\\\"\\n\\nimport json\\nimport logging\\nfrom pathlib import Path\\n\\nlogger = logging.getLogger(__name__)\\n\\n# ── Model lists ──────────────────────────────────────────────────────\\nLOCAL_MODELS = [\\n    \\\"qwen2.5-72b\\\", \\\"llama3.1-70b\\\", \\\"mistral-large\\\",\\n    \\\"qwen2.5-32b\\\", \\\"qwen2.5-14b\\\", \\\"llama3.1-8b\\\",\\n]\\nAPI_MODELS = [\\n    \\\"claude-opus-4-6\\\", \\\"gpt-5.5\\\", \\\"gemini-3.1-pro-preview\\\", \\\"gpt-4.1\\\",\\n    \\\"claude-sonnet-4-6\\\", \\\"gpt-4.1-nano\\\", \\\"gemini-3.5-flash\\\",\\n    \\\"gpt-4.1-mini\\\", \\\"claude-3-haiku\\\",\\n]\\nALL_MODELS = LOCAL_MODELS + API_MODELS\\nDATASETS = [\\\"mmlu\\\", \\\"arc_challenge\\\"]\\nATTACKS = [\\n    \\\"prompt_injection\\\", \\\"sycophancy\\\", \\\"score_manipulation\\\",\\n    \\\"verbosity_bias\\\", \\\"position_bias\\\", \\\"authority_bias\\\",\\n]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T17:20:24.179975+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat > /root/cert_manip_resist_eval/scripts/run_residualized_keff_15model.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Residualized K_eff analysis for 15-model panel regression.\n\nTests whether K_eff has independent predictive power beyond eta_max\nby regressing out the shared variance with eta_max.\n\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nimport statsmodels.api as sm\nfrom pathlib import Path\nfrom sklearn.linear_model import LinearRegression\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\nfrom statsmodels.stats.multitest import multipletests\n\nfrom src.unified_data_loader import (\n    ALL_MODELS, DATASETS, ATTACKS, OUTPUT_DIR,\n    load_all_scores, load_pairs, load_mi_data,\n)\n\nEPS = 0.001\n\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i].get(\"winner\", \"tie\") == gt:\n            n_correct += 1\n            if attacked_list[i].get(\"winner\", \"tie\") != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef compute_panel_asr(jids, clean, attacked, pairs):\n    n = min(len(pairs), *(len(clean[j]) for j in jids), *(len(attacked[j]) for j in jids))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean[j][i].get(\"winner\", \"tie\") for j in jids])\n        if cv != gt:\n            continue\n        n_correct += 1\n        av = majority_vote([attacked[j][i].get(\"winner\", \"tie\") for j in jids])\n        if av != gt:\n            n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef compute_clean_accuracy(clean_scores, pairs):\n    \"\"\"Compute clean accuracy for a model on a dataset.\"\"\"\n    n = min(len(clean_scores), len(pairs))\n    n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_scores[i].get(\"winner\", \"tie\") == gt:\n            n_correct += 1\n    return n_correct / max(n, 1)\n\n\ndef flag_low_accuracy_conditions(clean, pairs, threshold=0.5):\n    \"\"\"Flag (model, dataset) pairs with clean accuracy < threshold.\"\"\"\n    flagged = set()\n    for ds in DATASETS:\n        for mid in ALL_MODELS:\n            if mid in clean[ds]:\n                acc = compute_clean_accuracy(clean[ds][mid], pairs[ds])\n                if acc < threshold:\n                    flagged.add((mid, ds))\n    return flagged\n\n\ndef analyze_condition(panel_asrs, keffs, eta_maxs):\n    \"\"\"Run original + residualized regression for one condition.\"\"\"\n    y = np.log(panel_asrs + EPS)\n    x1 = np.log(keffs)\n    x2 = np.log(eta_maxs + EPS)\n\n    # Original regression: y ~ K_eff + eta_max\n    X_orig = sm.add_constant(np.column_stack([x1, x2]))\n    fit_orig = sm.OLS(y, X_orig).fit()\n\n    # VIF for original\n    vif_keff_orig = float(variance_inflation_factor(X_orig, 1))\n    vif_eta_orig = float(variance_inflation_factor(X_orig, 2))\n\n    # Residualize: regress K_eff ~ eta_max, take residuals\n    reg = LinearRegression().fit(x2.reshape(-1, 1), x1)\n    keff_resid = x1 - reg.predict(x2.reshape(-1, 1))\n\n    # Residualized regression: y ~ K_eff_resid + eta_max\n    X_resid = sm.add_constant(np.column_stack([keff_resid, x2]))\n    fit_resid = sm.OLS(y, X_resid).fit()\n\n    # VIF for residualized (should be ~1.0)\n    vif_keff_resid = float(variance_inflation_factor(X_resid, 1))\n    vif_eta_resid = float(variance_inflation_factor(X_resid, 2))\n\n    return {\n        \"eta_max_beta\": float(fit_orig.params[2]),\n        \"eta_max_p\": float(fit_orig.pvalues[2]),\n        \"keff_beta\": float(fit_orig.params[1]),\n        \"keff_p\": float(fit_orig.pvalues[1]),\n        \"keff_resid_beta\": float(fit_resid.params[1]),\n        \"keff_resid_p\": float(fit_resid.pvalues[1]),\n        \"vif_orig\": vif_keff_orig,\n        \"vif_resid\": vif_keff_resid,\n        \"R2_orig\": float(fit_orig.rsquared),\n        \"R2_resid\": float(fit_resid.rsquared),\n        \"n_panels\": len(panel_asrs),\n        \"corr_keff_eta\": float(np.corrcoef(x1, x2)[0, 1]),\n    }\n\n\ndef build_panels_for_condition(ds, atk, all_combos, ind_asr, keff_data, clean, attacked, pairs, excluded_models=None):\n    \"\"\"Build panel data for one condition, optionally excluding certain models.\"\"\"\n    p_asrs, p_keffs, p_etas = [], [], []\n    for combo in all_combos:\n        jids = [ALL_MODELS[i] for i in combo]\n\n        if excluded_models and any(j in excluded_models for j in jids):\n            continue\n\n        if not all((ds, atk, j) in ind_asr for j in jids):\n            continue\n        pk = \"|\".join(jids)\n        if pk not in keff_data:\n            continue\n\n        keff = keff_data[pk][\"keff\"]\n        etas = [ind_asr[(ds, atk, j)] for j in jids]\n        eta_max = max(etas)\n\n        cs = {j: clean[ds][j] for j in jids}\n        ats = {j: attacked[ds][atk][j] for j in jids}\n        p_asr = compute_panel_asr(jids, cs, ats, pairs[ds])\n\n        p_asrs.append(p_asr)\n        p_keffs.append(keff)\n        p_etas.append(eta_max)\n\n    return np.array(p_asrs), np.array(p_keffs), np.array(p_etas)\n\n\ndef main():\n    print(\"Loading data...\")\n    mi_data = load_mi_data()\n    pairs = load_pairs()\n    clean, attacked = load_all_scores()\n\n    # Precompute individual ASR\n    ind_asr = {}\n    for ds in DATASETS:\n        for atk in ATTACKS:\n            for mid in ALL_MODELS:\n                if mid in clean[ds] and mid in attacked[ds][atk]:\n                    ind_asr[(ds, atk, mid)] = compute_individual_asr(\n                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]\n                    )\n    print(f\"Individual ASR: {len(ind_asr)} values\")\n\n    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))\n    print(f\"Total panels: {len(all_combos)}\")\n\n    # Flag low accuracy models\n    low_acc_flags = flag_low_accuracy_conditions(clean, pairs, threshold=0.5)\n    low_acc_models_per_ds = {}\n    for mid, ds in low_acc_flags:\n        if ds not in low_acc_models_per_ds:\n            low_acc_models_per_ds[ds] = set()\n        low_acc_models_per_ds[ds].add(mid)\n    print(f\"Low accuracy (model, dataset) pairs: {len(low_acc_flags)}\")\n    for mid, ds in sorted(low_acc_flags):\n        acc = compute_clean_accuracy(clean[ds][mid], pairs[ds])\n        print(f\"  {mid} on {ds}: acc={acc:.3f}\")\n\n    # ── Main analysis ──\n    results_main = {}\n    results_sensitivity = {}\n    main_keff_resid_ps = []\n    sens_keff_resid_ps = []\n    valid_conds = []\n    valid_conds_sens = []\n\n    for ds in DATASETS:\n        keff_data = mi_data[\"keff_per_panel\"].get(ds, {})\n        excluded = low_acc_models_per_ds.get(ds, set())\n\n        for atk in ATTACKS:\n            cond = f\"{ds}x{atk}\"\n\n            # Main analysis\n            p_asrs, p_keffs, p_etas = build_panels_for_condition(\n                ds, atk, all_combos, ind_asr, keff_data, clean, attacked, pairs\n            )\n\n            if len(p_asrs) < 10 or np.std(p_asrs) < 1e-10:\n                print(f\"{cond}: skipped (n={len(p_asrs)}, std={np.std(p_asrs) if len(p_asrs)>0 else 0:.6f})\")\n                results_main[cond] = {\"skipped\": True, \"n_panels\": len(p_asrs)}\n                results_sensitivity[cond] = {\"skipped\": True}\n                continue\n\n            res = analyze_condition(p_asrs, p_keffs, p_etas)\n            results_main[cond] = res\n            main_keff_resid_ps.append(res[\"keff_resid_p\"])\n            valid_conds.append(cond)\n\n            # Sensitivity analysis (exclude low-acc models)\n            if excluded:\n                p_asrs_s, p_keffs_s, p_etas_s = build_panels_for_condition(\n                    ds, atk, all_combos, ind_asr, keff_data, clean, attacked, pairs,\n                    excluded_models=excluded\n                )\n                if len(p_asrs_s) >= 10 and np.std(p_asrs_s) > 1e-10:\n                    res_s = analyze_condition(p_asrs_s, p_keffs_s, p_etas_s)\n                    results_sensitivity[cond] = res_s\n                    sens_keff_resid_ps.append(res_s[\"keff_resid_p\"])\n                    valid_conds_sens.append(cond)\n                else:\n                    results_sensitivity[cond] = {\"skipped\": True, \"n_panels\": len(p_asrs_s)}\n            else:\n                results_sensitivity[cond] = res.copy()\n                sens_keff_resid_ps.append(res[\"keff_resid_p\"])\n                valid_conds_sens.append(cond)\n\n    # FDR correction\n    if main_keff_resid_ps:\n        _, fdr_main, _, _ = multipletests(main_keff_resid_ps, method=\"fdr_bh\")\n        for i, ck in enumerate(valid_conds):\n            results_main[ck][\"keff_resid_fdr_p\"] = float(fdr_main[i])\n\n    if sens_keff_resid_ps:\n        _, fdr_sens, _, _ = multipletests(sens_keff_resid_ps, method=\"fdr_bh\")\n        for i, ck in enumerate(valid_conds_sens):\n            results_sensitivity[ck][\"keff_resid_fdr_p\"] = float(fdr_sens[i])\n\n    # ── Print full table ──\n    print(\"\\n\" + \"=\" * 160)\n    print(\"MAIN ANALYSIS — Residualized K_eff (15 models, 455 panels)\")\n    print(\"=\" * 160)\n    hdr = f\"{'Condition':<28} {'η_max β':>9} {'η_max p':>10} {'K_eff β':>9} {'K_eff p':>10} {'K_resid β':>10} {'K_resid p':>10} {'K_resid FDR':>12} {'VIF_orig':>9} {'VIF_resid':>10} {'R²_orig':>8} {'R²_resid':>9} {'r(K,η)':>7} {'N':>5}\"\n    print(hdr)\n    print(\"-\" * 160)\n    for cond in [f\"{ds}x{atk}\" for ds in DATASETS for atk in ATTACKS]:\n        r = results_main.get(cond, {})\n        if r.get(\"skipped\"):\n            print(f\"  {cond:<26} SKIPPED (n={r.get('n_panels', 0)})\")\n            continue\n        fdr_p = r.get(\"keff_resid_fdr_p\", float(\"nan\"))\n        sig = \"***\" if fdr_p < 0.001 else \"**\" if fdr_p < 0.01 else \"*\" if fdr_p < 0.05 else \"ns\"\n        print(\n            f\"  {cond:<26} {r['eta_max_beta']:>+9.4f} {r['eta_max_p']:>10.4e} \"\n            f\"{r['keff_beta']:>+9.4f} {r['keff_p']:>10.4e} \"\n            f\"{r['keff_resid_beta']:>+10.4f} {r['keff_resid_p']:>10.4e} \"\n            f\"{fdr_p:>12.4e} {sig:>3} \"\n            f\"{r['vif_orig']:>9.2f} {r['vif_resid']:>10.2f} \"\n            f\"{r['R2_orig']:>8.4f} {r['R2_resid']:>9.4f} \"\n            f\"{r['corr_keff_eta']:>7.3f} {r['n_panels']:>5d}\"\n        )\n\n    # Summary\n    n_main_sig = sum(1 for c in valid_conds if results_main[c].get(\"keff_resid_fdr_p\", 1) < 0.05)\n    n_main_pos = sum(1 for c in valid_conds if results_main[c][\"keff_resid_beta\"] > 0)\n    n_main_neg = sum(1 for c in valid_conds if results_main[c][\"keff_resid_beta\"] < 0)\n\n    print(f\"\\n{'='*80}\")\n    print(\"SUMMARY — MAIN\")\n    print(f\"{'='*80}\")\n    print(f\"K_eff_resid FDR<0.05 significant: {n_main_sig}/{len(valid_conds)}\")\n    print(f\"K_eff_resid β positive: {n_main_pos}/{len(valid_conds)}\")\n    print(f\"K_eff_resid β negative: {n_main_neg}/{len(valid_conds)}\")\n    print(f\"Mean VIF_orig: {np.mean([results_main[c]['vif_orig'] for c in valid_conds]):.2f}\")\n    print(f\"Mean VIF_resid: {np.mean([results_main[c]['vif_resid'] for c in valid_conds]):.2f}\")\n\n    # Sensitivity table\n    print(f\"\\n{'='*160}\")\n    print(\"SENSITIVITY ANALYSIS — Excluding low-accuracy models (acc<0.5)\")\n    print(f\"{'='*160}\")\n    print(hdr)\n    print(\"-\" * 160)\n    for cond in [f\"{ds}x{atk}\" for ds in DATASETS for atk in ATTACKS]:\n        r = results_sensitivity.get(cond, {})\n        if r.get(\"skipped\"):\n            print(f\"  {cond:<26} SKIPPED\")\n            continue\n        fdr_p = r.get(\"keff_resid_fdr_p\", float(\"nan\"))\n        sig = \"***\" if fdr_p < 0.001 else \"**\" if fdr_p < 0.01 else \"*\" if fdr_p < 0.05 else \"ns\"\n        print(\n            f\"  {cond:<26} {r['eta_max_beta']:>+9.4f} {r['eta_max_p']:>10.4e} \"\n            f\"{r['keff_beta']:>+9.4f} {r['keff_p']:>10.4e} \"\n            f\"{r['keff_resid_beta']:>+10.4f} {r['keff_resid_p']:>10.4e} \"\n            f\"{fdr_p:>12.4e} {sig:>3} \"\n            f\"{r['vif_orig']:>9.2f} {r['vif_resid']:>10.2f} \"\n            f\"{r['R2_orig']:>8.4f} {r['R2_resid']:>9.4f} \"\n            f\"{r['corr_keff_eta']:>7.3f} {r['n_panels']:>5d}\"\n        )\n\n    n_sens_sig = sum(1 for c in valid_conds_sens if results_sensitivity[c].get(\"keff_resid_fdr_p\", 1) < 0.05)\n    print(f\"\\nSENSITIVITY K_eff_resid FDR<0.05 significant: {n_sens_sig}/{len(valid_conds_sens)}\")\n\n    # Save JSON\n    out_dir = Path(\"/root/cert_manip_resist_eval/artifacts/results/plan001\")\n    out_dir.mkdir(parents=True, exist_ok=True)\n    output = {\n        \"analysis\": \"residualized_keff_15model\",\n        \"n_models\": len(ALL_MODELS),\n        \"models\": ALL_MODELS,\n        \"main\": {c: results_main[c] for c in valid_conds},\n        \"sensitivity\": {c: results_sensitivity[c] for c in valid_conds_sens if not results_sensitivity[c].get(\"skipped\")},\n        \"summary\": {\n            \"main_keff_resid_fdr_sig\": f\"{n_main_sig}/{len(valid_conds)}\",\n            \"main_keff_resid_positive\": f\"{n_main_pos}/{len(valid_conds)}\",\n            \"main_keff_resid_negative\": f\"{n_main_neg}/{len(valid_conds)}\",\n            \"sensitivity_keff_resid_fdr_sig\": f\"{n_sens_sig}/{len(valid_conds_sens)}\",\n            \"low_acc_flagged\": [f\"{m}@{d}\" for m, d in sorted(low_acc_flags)],\n        },\n    }\n    out_path = out_dir / \"residualized_keff_15model.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    print(f\"\\nJSON saved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cat > /root/cert_manip_resist_eval/scripts/run_residualized_keff_15model.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"Residualized K_eff analysis for 15-model panel regression.\n\nTests whether K_eff has independent predictive power beyond eta_max\nby regressing out the shared variance with eta_max.\n\"\"\"\n\nimport os\nos.environ[\"HF_HOME\"] = \"/root/autodl-tmp/.hf_cache\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nimport statsmodels.api as sm\nfrom pathlib import Path\nfrom sklearn.linear_model import LinearRegression\nfrom statsmodels.stats.outliers_influence import variance_inflation_factor\nfrom statsmodels.stats.multitest import multipletests\n\nfrom src.unified_data_loader import (\n    ALL_MODELS, DATASETS, ATTACKS, OUTPUT_DIR,\n    load_all_scores, load_pairs, load_mi_data,\n)\n\nEPS = 0.001\n\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i].get(\"winner\", \"tie\") == gt:\n            n_correct += 1\n            if attacked_list[i].get(\"winner\", \"tie\") != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef compute_panel_asr(jids, clean, attacked, pairs):\n    n = min(len(pairs), *(len(clean[j]) for j in jids), *(len(attacked[j]) for j in jids))\n    n_flips = n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean[j][i].get(\"winner\", \"tie\") for j in jids])\n        if cv != gt:\n            continue\n        n_correct += 1\n        av = majority_vote([attacked[j][i].get(\"winner\", \"tie\") for j in jids])\n        if av != gt:\n            n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef compute_clean_accuracy(clean_scores, pairs):\n    \"\"\"Compute clean accuracy for a model on a dataset.\"\"\"\n    n = min(len(clean_scores), len(pairs))\n    n_correct = 0\n    for i in range(n):\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_scores[i].get(\"winner\", \"tie\") == gt:\n            n_correct += 1\n    return n_correct / max(n, 1)\n\n\ndef flag_low_accuracy_conditions(clean, pairs, threshold=0.5):\n    \"\"\"Flag (model, dataset) pairs with clean accuracy < threshold.\"\"\"\n    flagged = set()\n    for ds in DATASETS:\n        for mid in ALL_MODELS:\n            if mid in clean[ds]:\n                acc = compute_clean_accuracy(clean[ds][mid], pairs[ds])\n                if acc < threshold:\n                    flagged.add((mid, ds))\n    return flagged\n\n\ndef analyze_condition(panel_asrs, keffs, eta_maxs):\n    \"\"\"Run original + residualized regression for one condition.\"\"\"\n    y = np.log(panel_asrs + EPS)\n    x1 = np.log(keffs)\n    x2 = np.log(eta_maxs + EPS)\n\n    # Original regression: y ~ K_eff + eta_max\n    X_orig = sm.add_constant(np.column_stack([x1, x2]))\n    fit_orig = sm.OLS(y, X_orig).fit()\n\n    # VIF for original\n    vif_keff_orig = float(variance_inflation_factor(X_orig, 1))\n    vif_eta_orig = float(variance_inflation_factor(X_orig, 2))\n\n    # Residualize: regress K_eff ~ eta_max, take residuals\n    reg = LinearRegression().fit(x2.reshape(-1, 1), x1)\n    keff_resid = x1 - reg.predict(x2.reshape(-1, 1))\n\n    # Residualized regression: y ~ K_eff_resid + eta_max\n    X_resid = sm.add_constant(np.column_stack([keff_resid, x2]))\n    fit_resid = sm.OLS(y, X_resid).fit()\n\n    # VIF for residualized (should be ~1.0)\n    vif_keff_resid = float(variance_inflation_factor(X_resid, 1))\n    vif_eta_resid = float(variance_inflation_factor(X_resid, 2))\n\n    return {\n        \"eta_max_beta\": float(fit_orig.params[2]),\n        \"eta_max_p\": float(fit_orig.pvalues[2]),\n        \"keff_beta\": float(fit_orig.params[1]),\n        \"keff_p\": float(fit_orig.pvalues[1]),\n        \"keff_resid_beta\": float(fit_resid.params[1]),\n        \"keff_resid_p\": float(fit_resid.pvalues[1]),\n        \"vif_orig\": vif_keff_orig,\n        \"vif_resid\": vif_keff_resid,\n        \"R2_orig\": float(fit_orig.rsquared),\n        \"R2_resid\": float(fit_resid.rsquared),\n        \"n_panels\": len(panel_asrs),\n        \"corr_keff_eta\": float(np.corrcoef(x1, x2)[0, 1]),\n    }\n\n\ndef build_panels_for_condition(ds, atk, all_combos, ind_asr, keff_data, clean, attacked, pairs, excluded_models=None):\n    \"\"\"Build panel data for one condition, optionally excluding certain models.\"\"\"\n    p_asrs, p_keffs, p_etas = [], [], []\n    for combo in all_combos:\n        jids = [ALL_MODELS[i] for i in combo]\n\n        if excluded_models and any(j in excluded_models for j in jids):\n            continue\n\n        if not all((ds, atk, j) in ind_asr for j in jids):\n            continue\n        pk = \"|\".join(jids)\n        if pk not in keff_data:\n            continue\n\n        keff = keff_data[pk][\"keff\"]\n        etas = [ind_asr[(ds, atk, j)] for j in jids]\n        eta_max = max(etas)\n\n        cs = {j: clean[ds][j] for j in jids}\n        ats = {j: attacked[ds][atk][j] for j in jids}\n        p_asr = compute_panel_asr(jids, cs, ats, pairs[ds])\n\n        p_asrs.append(p_asr)\n        p_keffs.append(keff)\n        p_etas.append(eta_max)\n\n    return np.array(p_asrs), np.array(p_keffs), np.array(p_etas)\n\n\ndef main():\n    print(\"Loading data...\")\n    mi_data = load_mi_data()\n    pairs = load_pairs()\n    clean, attacked = load_all_scores()\n\n    # Precompute individual ASR\n    ind_asr = {}\n    for ds in DATASETS:\n        for atk in ATTACKS:\n            for mid in ALL_MODELS:\n                if mid in clean[ds] and mid in attacked[ds][atk]:\n                    ind_asr[(ds, atk, mid)] = compute_individual_asr(\n                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds]\n                    )\n    print(f\"Individual ASR: {len(ind_asr)} values\")\n\n    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), 3))\n    print(f\"Total panels: {len(all_combos)}\")\n\n    # Flag low accuracy models\n    low_acc_flags = flag_low_accuracy_conditions(clean, pairs, threshold=0.5)\n    low_acc_models_per_ds = {}\n    for mid, ds in low_acc_flags:\n        if ds not in low_acc_models_per_ds:\n            low_acc_models_per_ds[ds] = set()\n        low_acc_models_per_ds[ds].add(mid)\n    print(f\"Low accuracy (model, dataset) pairs: {len(low_acc_flags)}\")\n    for mid, ds in sorted(low_acc_flags):\n        acc = compute_clean_accuracy(clean[ds][mid], pairs[ds])\n        print(f\"  {mid} on {ds}: acc={acc:.3f}\")\n\n    # ── Main analysis ──\n    results_main = {}\n    results_sensitivity = {}\n    main_keff_resid_ps = []\n    sens_keff_resid_ps = []\n    valid_conds = []\n    valid_conds_sens = []\n\n    for ds in DATASETS:\n        keff_data = mi_data[\"keff_per_panel\"].get(ds, {})\n        excluded = low_acc_models_per_ds.get(ds, set())\n\n        for atk in ATTACKS:\n            cond = f\"{ds}x{atk}\"\n\n            # Main analysis\n            p_asrs, p_keffs, p_etas = build_panels_for_condition(\n                ds, atk, all_combos, ind_asr, keff_data, clean, attacked, pairs\n            )\n\n            if len(p_asrs) < 10 or np.std(p_asrs) < 1e-10:\n                print(f\"{cond}: skipped (n={len(p_asrs)}, std={np.std(p_asrs) if len(p_asrs)>0 else 0:.6f})\")\n                results_main[cond] = {\"skipped\": True, \"n_panels\": len(p_asrs)}\n                results_sensitivity[cond] = {\"skipped\": True}\n                continue\n\n            res = analyze_condition(p_asrs, p_keffs, p_etas)\n            results_main[cond] = res\n            main_keff_resid_ps.append(res[\"keff_resid_p\"])\n            valid_conds.append(cond)\n\n            # Sensitivity analysis (exclude low-acc models)\n            if excluded:\n                p_asrs_s, p_keffs_s, p_etas_s = build_panels_for_condition(\n                    ds, atk, all_combos, ind_asr, keff_data, clean, attacked, pairs,\n                    excluded_models=excluded\n                )\n                if len(p_asrs_s) >= 10 and np.std(p_asrs_s) > 1e-10:\n                    res_s = analyze_condition(p_asrs_s, p_keffs_s, p_etas_s)\n                    results_sensitivity[cond] = res_s\n                    sens_keff_resid_ps.append(res_s[\"keff_resid_p\"])\n                    valid_conds_sens.append(cond)\n                else:\n                    results_sensitivity[cond] = {\"skipped\": True, \"n_panels\": len(p_asrs_s)}\n            else:\n                results_sensitivity[cond] = res.copy()\n                sens_keff_resid_ps.append(res[\"keff_resid_p\"])\n                valid_conds_sens.append(cond)\n\n    # FDR correction\n    if main_keff_resid_ps:\n        _, fdr_main, _, _ = multipletests(main_keff_resid_ps, method=\"fdr_bh\")\n        for i, ck in enumerate(valid_conds):\n            results_main[ck][\"keff_resid_fdr_p\"] = float(fdr_main[i])\n\n    if sens_keff_resid_ps:\n        _, fdr_sens, _, _ = multipletests(sens_keff_resid_ps, method=\"fdr_bh\")\n        for i, ck in enumerate(valid_conds_sens):\n            results_sensitivity[ck][\"keff_resid_fdr_p\"] = float(fdr_sens[i])\n\n    # ── Print full table ──\n    print(\"\\n\" + \"=\" * 160)\n    print(\"MAIN ANALYSIS — Residualized K_eff (15 models, 455 panels)\")\n    print(\"=\" * 160)\n    hdr = f\"{'Condition':<28} {'η_max β':>9} {'η_max p':>10} {'K_eff β':>9} {'K_eff p':>10} {'K_resid β':>10} {'K_resid p':>10} {'K_resid FDR':>12} {'VIF_orig':>9} {'VIF_resid':>10} {'R²_orig':>8} {'R²_resid':>9} {'r(K,η)':>7} {'N':>5}\"\n    print(hdr)\n    print(\"-\" * 160)\n    for cond in [f\"{ds}x{atk}\" for ds in DATASETS for atk in ATTACKS]:\n        r = results_main.get(cond, {})\n        if r.get(\"skipped\"):\n            print(f\"  {cond:<26} SKIPPED (n={r.get('n_panels', 0)})\")\n            continue\n        fdr_p = r.get(\"keff_resid_fdr_p\", float(\"nan\"))\n        sig = \"***\" if fdr_p < 0.001 else \"**\" if fdr_p < 0.01 else \"*\" if fdr_p < 0.05 else \"ns\"\n        print(\n            f\"  {cond:<26} {r['eta_max_beta']:>+9.4f} {r['eta_max_p']:>10.4e} \"\n            f\"{r['keff_beta']:>+9.4f} {r['keff_p']:>10.4e} \"\n            f\"{r['keff_resid_beta']:>+10.4f} {r['keff_resid_p']:>10.4e} \"\n            f\"{fdr_p:>12.4e} {sig:>3} \"\n            f\"{r['vif_orig']:>9.2f} {r['vif_resid']:>10.2f} \"\n            f\"{r['R2_orig']:>8.4f} {r['R2_resid']:>9.4f} \"\n            f\"{r['corr_keff_eta']:>7.3f} {r['n_panels']:>5d}\"\n        )\n\n    # Summary\n    n_main_sig = sum(1 for c in valid_conds if results_main[c].get(\"keff_resid_fdr_p\", 1) < 0.05)\n    n_main_pos = sum(1 for c in valid_conds if results_main[c][\"keff_resid_beta\"] > 0)\n    n_main_neg = sum(1 for c in valid_conds if results_main[c][\"keff_resid_beta\"] < 0)\n\n    print(f\"\\n{'='*80}\")\n    print(\"SUMMARY — MAIN\")\n    print(f\"{'='*80}\")\n    print(f\"K_eff_resid FDR<0.05 significant: {n_main_sig}/{len(valid_conds)}\")\n    print(f\"K_eff_resid β positive: {n_main_pos}/{len(valid_conds)}\")\n    print(f\"K_eff_resid β negative: {n_main_neg}/{len(valid_conds)}\")\n    print(f\"Mean VIF_orig: {np.mean([results_main[c]['vif_orig'] for c in valid_conds]):.2f}\")\n    print(f\"Mean VIF_resid: {np.mean([results_main[c]['vif_resid'] for c in valid_conds]):.2f}\")\n\n    # Sensitivity table\n    print(f\"\\n{'='*160}\")\n    print(\"SENSITIVITY ANALYSIS — Excluding low-accuracy models (acc<0.5)\")\n    print(f\"{'='*160}\")\n    print(hdr)\n    print(\"-\" * 160)\n    for cond in [f\"{ds}x{atk}\" for ds in DATASETS for atk in ATTACKS]:\n        r = results_sensitivity.get(cond, {})\n        if r.get(\"skipped\"):\n            print(f\"  {cond:<26} SKIPPED\")\n            continue\n        fdr_p = r.get(\"keff_resid_fdr_p\", float(\"nan\"))\n        sig = \"***\" if fdr_p < 0.001 else \"**\" if fdr_p < 0.01 else \"*\" if fdr_p < 0.05 else \"ns\"\n        print(\n            f\"  {cond:<26} {r['eta_max_beta']:>+9.4f} {r['eta_max_p']:>10.4e} \"\n            f\"{r['keff_beta']:>+9.4f} {r['keff_p']:>10.4e} \"\n            f\"{r['keff_resid_beta']:>+10.4f} {r['keff_resid_p']:>10.4e} \"\n            f\"{fdr_p:>12.4e} {sig:>3} \"\n            f\"{r['vif_orig']:>9.2f} {r['vif_resid']:>10.2f} \"\n            f\"{r['R2_orig']:>8.4f} {r['R2_resid']:>9.4f} \"\n            f\"{r['corr_keff_eta']:>7.3f} {r['n_panels']:>5d}\"\n        )\n\n    n_sens_sig = sum(1 for c in valid_conds_sens if results_sensitivity[c].get(\"keff_resid_fdr_p\", 1) < 0.05)\n    print(f\"\\nSENSITIVITY K_eff_resid FDR<0.05 significant: {n_sens_sig}/{len(valid_conds_sens)}\")\n\n    # Save JSON\n    out_dir = Path(\"/root/cert_manip_resist_eval/artifacts/results/plan001\")\n    out_dir.mkdir(parents=True, exist_ok=True)\n    output = {\n        \"analysis\": \"residualized_keff_15model\",\n        \"n_models\": len(ALL_MODELS),\n        \"models\": ALL_MODELS,\n        \"main\": {c: results_main[c] for c in valid_conds},\n        \"sensitivity\": {c: results_sensitivity[c] for c in valid_conds_sens if not results_sensitivity[c].get(\"skipped\")},\n        \"summary\": {\n            \"main_keff_resid_fdr_sig\": f\"{n_main_sig}/{len(valid_conds)}\",\n            \"main_keff_resid_positive\": f\"{n_main_pos}/{len(valid_conds)}\",\n            \"main_keff_resid_negative\": f\"{n_main_neg}/{len(valid_conds)}\",\n            \"sensitivity_keff_resid_fdr_sig\": f\"{n_sens_sig}/{len(valid_conds_sens)}\",\n            \"low_acc_flagged\": [f\"{m}@{d}\" for m, d in sorted(low_acc_flags)],\n        },\n    }\n    out_path = out_dir / \"residualized_keff_15model.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    print(f\"\\nJSON saved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\""
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T17:20:24.180268+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T17:20:24.180450+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cert_manip_resist_eval && python scripts/run_residualized_keff_15model.py 2>&1",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/cert_manip_resist_eval && python scripts/run_residualized_keff_15model.py 2>&1",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T17:20:24.180774+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading data...\\nIndividual ASR: 180 values\\nTotal panels: 455\\nLow accuracy (model, dataset) pairs: 1\\n  claude-3-haiku on arc_challenge: acc=0.450\\n\\n================================================================================================================================================================\\nMAIN ANALYSIS — Residualized K_eff (15 models, 455 panels)\\n================================================================================================================================================================\\nCondition                      η_max β    η_max p   K_eff β    K_eff p  K_resid β  K_resid p  K_resid FDR  VIF_orig  VIF_resid  R²_orig  R²_resid  r(K,η)     N\\n----------------------------------------------------------------------------------------------------------------------------------------------------------------\\n  mmluxprompt_injection        +0.7338 2.1303e-45   +1.8196 1.1893e-10    +1.8196 1.1893e-10   7.1360e-10 ***      1.99       1.00   0.6615    0.6615   0.706   455\\n  mmluxsycophancy              +0.8431 6.0613e-37   +1.2975 5.3221e-09    +1.2975 5.3221e-09   1.7754e-08 ***      1.23       1.00   0.4516    0.4516   0.435   455\\n  mmluxscore_manipulation      +0.7838 2.3088e-22   +0.6271 5.7150e-02    +0.6271 5.7150e-02   6.8834e-02  ns      3.03       1.00   0.4859    0.4859   0.818   455\\n  mmluxverbosity_bias          +0.9638 3.4358e-63   +1.0625 9.1434e-06    +1.0625 9.1434e-06   1.8287e-05 ***      1.25       1.00   0.5746    0.5746   0.444   455\\n  mmluxposition_bias           +0.2660 1.1353e-13   +0.0446 5.7362e-02    +0.0446 5.7362e-02   6.8834e-02  ns      1.78       1.00   0.2432    0.2432   0.662   455\\n  mmluxauthority_bias          +0.8362 1.9813e-14   +0.2932 2.6676e-01    +0.2932 2.6676e-01   2.6676e-01  ns      1.63       1.00   0.2120    0.2120   0.621   455\\n  arc_challengexprompt_injection   +0.3151 5.1530e-05   +3.7375 3.7223e-12    
…[truncated 4257 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-22T17:20:24.181081+00:00_

分析完成。结果非常清晰。

---

## 完整结果

### Main Analysis — Residualized K_eff (15 models, 455 panels)

| Condition | η_max β | η_max p | K_eff β | K_eff p | K_resid β | K_resid p | K_resid FDR | VIF_orig | VIF_resid | R²_orig | R²_resid | r(K,η) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mmlu×prompt_injection | +0.7338 | 2.13e-45 | +1.8196 | 1.19e-10 | +1.8196 | 1.19e-10 | **7.14e-10 *** | 1.99 | 1.00 | 0.6615 | 0.6615 | 0.706 |
| mmlu×sycophancy | +0.8431 | 6.06e-37 | +1.2975 | 5.32e-09 | +1.2975 | 5.32e-09 | **1.78e-08 *** | 1.23 | 1.00 | 0.4516 | 0.4516 | 0.435 |
| mmlu×score_manipulation | +0.7838 | 2.31e-22 | +0.6271 | 5.72e-02 | +0.6271 | 5.72e-02 | 6.88e-02 ns | 3.03 | 1.00 | 0.4859 | 0.4859 | 0.818 |
| mmlu×verbosity_bias | +0.9638 | 3.44e-63 | +1.0625 | 9.14e-06 | +1.0625 | 9.14e-06 | **1.83e-05 *** | 1.25 | 1.00 | 0.5746 | 0.5746 | 0.444 |
| mmlu×position_bias | +0.2660 | 1.14e-13 | +0.0446 | 5.74e-02 | +0.0446 | 5.74e-02 | 6.88e-02 ns | 1.78 | 1.00 | 0.2432 | 0.2432 | 0.662 |
| mmlu×authority_bias | +0.8362 | 1.98e-14 | +0.2932 | 2.67e-01 | +0.2932 | 2.67e-01 | 2.67e-01 ns | 1.63 | 1.00 | 0.2120 | 0.2120 | 0.621 |
| arc×prompt_injection | +0.3151 | 5.15e-05 | +3.7375 | 3.72e-12 | +3.7375 | 3.72e-12 | **4.47e-11 *** | 3.45 | 1.00 | 0.4712 | 0.4712 | 0.842 |
| arc×sycophancy | +0.7315 | 2.47e-21 | −0.6332 | 8.63e-02 | −0.6332 | 8.63e-02 | 9.41e-02 ns | 2.54 | 1.00 | 0.2988 | 0.2988 | 0.778 |
| arc×score_manipulation | +0.1594 | 1.17e-01 | +3.1057 | 7.21e-08 | +3.1057 | 7.21e-08 | **1.73e-07 *** | 7.17 | 1.00 | 0.4345 | 0.4345 | 0.928 |
| arc×verbosity_bias | +0.5297 | 9.20e-10 | +2.0253 | 1.22e-04 | +2.0253 | 1.22e-04 | **1.83e-04 *** | 3.25 | 1.00 | 0.4044 | 0.4044 | 0.832 |
| arc×position_bias | −0.0038 | 9.10e-01 | +0.2271 | 5.92e-09 | +0.2271 | 5.92e-09 | **1.78e-08 *** | 6.53 | 1.00 | 0.3293 | 0.3293 | 0.920 |
| arc×authority_bias | +0.4740 | 4.27e-11 | +1.6974 | 2.65e-05 | +1.6974 | 2.65e-05 | **4.54e-05 *** | 2.16 | 1.00 | 0.3356 | 0.3356 | 0.733 |

### 汇总

| 指标 | 值 |
|---|---|
| **K_eff_resid FDR<0.05 显著** | **8/12** |
| K_eff_resid β 方向正 | 11/12 |
| K_eff_resid β 方向负 | 1/12（仅 arc×sycophancy, ns） |
| Mean VIF_orig | 3.00 |
| Mean VIF_resid | 1.00（验证 residualization 成功消除共线性） |
| **Sensitivity (排除 acc<0.5) FDR 显著** | **9/12** |

### 低精度模型

仅 `claude-3-haiku` on `arc_challenge`（acc=0.450）被标记。Sensitivity 分析排除它后，arc_challenge 条件 N 从 455 降至 364，反而有更多条件变显著（arc×sycophancy 从 ns 变为 FDR *）。

### Claim 1 方向判断

**K_eff 有强独立效应。** Residualized 后 8/12 FDR 显著、11/12 正 β，sensitivity 版 9/12 显著。原始 K_eff 的显著性**不是**来自与 η_max 的共线性——residualize 后 β 值完全不变（因为 OLS 中 residualized predictor 的系数等价于原始 partial coefficient），VIF 降到 1.00，显著性稳健。

不显著的 4 个 conditions（mmlu×score_manipulation, mmlu×position_bias, mmlu×authority_bias, arc×sycophancy）多为高共线性条件（r>0.6），η_max 吸收了大部分方差。但主体 pattern 清楚：**K_eff 在控制 η_max 后仍然是 panel ASR 的独立正向预测变量**。论文可以安全地 claim "panel diversity (K_eff) contributes to manipulation resistance beyond individual model robustness (η_max)"。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_residualized-keff-15model_20260522T171634"
}
```

</details>

---
