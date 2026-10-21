# analyze exp027 bootstrap ci

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 122
- **Recorded user turns:** 0
- **Tool calls:** 60
- **Original source:** `logs/chats/worker_analyze_exp027-bootstrap-ci_20260518T112149.jsonl`
- **Structured JSON:** [`d5f5465137511d0692ca.json`](../../sessions/d5/d5f5465137511d0692ca.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

122 recorded events

### Tool call

_source line 1 · 2026-05-18T11:32:25.908128+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Find bootstrap CI scripts",
  "subagent_type": "Explore",
  "prompt": "Find bootstrap CI scripts in /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ — specifically look for `crossscorer_bootstrap_ci.py`, `c4_power_curve.py`, or any script with \"bootstrap\" in the name under the `scripts/` directory. Also check for any Python files that contain \"bootstrap\" as a keyword. I need to understand the bootstrap resampling logic used in this project. Search breadth: medium."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Agent",
  "tool_args": {
    "description": "Find bootstrap CI scripts",
    "subagent_type": "Explore",
    "prompt": "Find bootstrap CI scripts in /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ — specifically look for `crossscorer_bootstrap_ci.py`, `c4_power_curve.py`, or any script with \"bootstrap\" in the name under the `scripts/` directory. Also check for any Python files that contain \"bootstrap\" as a keyword. I need to understand the bootstrap resampling logic used in this project. Search breadth: medium."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-18T11:32:25.908501+00:00_

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
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
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

_source line 3 · 2026-05-18T11:32:25.908681+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T11:32:25.908854+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/bootstrap*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/bootstrap*.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-18T11:32:25.909002+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T11:32:25.909133+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/scripts/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/scripts/*.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-18T11:32:25.909255+00:00_

scripts/run_pipeline.py
scripts/run_cross_transfer.py
scripts/run_exp013_cross_transfer.py
scripts/plot_exp003_decoding_ablation.py
scripts/run_exp009_dose_response.py
scripts/run_exp015_neural_probe.py
scripts/exp006_analyze_results.py
scripts/exp006_fill_discussion.py
scripts/analyze_exp006.py
scripts/exp_B_14d_ablation.py
scripts/exp_D_obd_n500_v2.py
scripts/exp_D_mcnemar.py
scripts/exp_E_paired_stats.py
artifacts/scripts/plot_summary_auc_decay.py
scripts/draw_kstar_theta.py
artifacts/scripts/transfer_heatmap.py
artifacts/scripts/plot_auc_decay_ci.py
artifacts/scripts/plot_filtering_strategies.py
scripts/draw_pipeline_figure.py
scripts/exp025_pythia_filtering.py
scripts/plot_fig_jsd_decay.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T11:32:25.909391+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "bootstrap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "type": "py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Grep",
  "tool_args": {
    "pattern": "bootstrap",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
    "type": "py",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T11:32:25.909520+00:00_

Found 18 files
artifacts/exp008_retrain_chain.py
artifacts/scripts/plot_auc_decay_ci.py
scripts/draw_kstar_theta.py
scripts/exp_D_mcnemar.py
scripts/exp_D_obd_n500_v2.py
.venv/lib/python3.14/site-packages/matplotlib/tests/test_cbook.py
.venv/lib/python3.14/site-packages/matplotlib/tests/test_backend_tk.py
.venv/lib/python3.14/site-packages/matplotlib/tests/test_axes.py
.venv/lib/python3.14/site-packages/matplotlib/axes/_axes.pyi
.venv/lib/python3.14/site-packages/matplotlib/axes/_axes.py
.venv/lib/python3.14/site-packages/matplotlib/rcsetup.py
.venv/lib/python3.14/site-packages/matplotlib/pyplot.py
.venv/lib/python3.14/site-packages/matplotlib/cbook.pyi
.venv/lib/python3.14/site-packages/matplotlib/cbook.py
.venv/lib/python3.14/site-packages/matplotlib/_animation_data.py
.venv/lib/python3.14/site-packages/pip/_vendor/distlib/util.py
.venv/lib/python3.14/site-packages/pip/_vendor/distlib/compat.py
scripts/run_exp015_neural_probe.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T11:32:25.909661+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/scripts/plot_auc_decay_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/scripts/plot_auc_decay_ci.py"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T11:32:25.909859+00:00_

1	#!/usr/bin/env python3
2	"""AUC decay curves with bootstrap confidence interval bands.
3	
4	Input:  artifacts/exp*_bootstrap_ci.json, results_*/bootstrap_ci.json,
5	        results_*/pairwise_auc.json (per_fold → approximate CI)
6	Output: artifacts/figures/fig_s1_auc_decay_ci.pdf
7	Deps:   matplotlib, numpy
8	"""
9	
10	import argparse
11	import json
12	import re
13	import matplotlib
14	matplotlib.use("Agg")
15	import matplotlib.pyplot as plt
16	import numpy as np
17	from pathlib import Path
18	
19	TABLEAU_COLORS = [
20	    "#4e79a7", "#e15759", "#76b7b2", "#59a14f",
21	    "#b07aa1", "#ff9da7", "#9c755f", "#bab0ac",
22	    "#edc948", "#f28e2b",
23	]
24	MARKERS = ["o", "s", "^", "D", "v", "P", "X", "*", "h", "<"]
25	PAIR_KEYS = ["0v1", "1v2", "2v3", "3v4", "4v5"]
26	X_LABELS = ["0 vs 1", "1 vs 2", "2 vs 3", "3 vs 4", "4 vs 5"]
27	
28	
29	def infer_label(source_path, metadata=None):
30	    """Infer model label from file path or JSON metadata."""
31	    if metadata and "experiment" in metadata:
32	        exp = metadata["experiment"].lower()
33	    else:
34	        exp = str(source_path).lower()
35	    patterns = [
36	        (r"qwen.*rw|qwen.*rewrite", "Qwen-rw"),
37	        (r"qwen.*base", "Qwen-base"),
38	        (r"qwen.*7b", "Qwen-7B"),
39	        (r"qwen.*cont|qwen(?!.*rw|.*rewrite|.*base|.*7b)", "Qwen-cont"),
40	        (r"pythia.*greedy", "Pythia-greedy"),
41	        (r"pythia.*nuc", "Pythia-nuc0.9"),
42	        (r"pythia.*t07|pythia.*t0\.7", "Pythia-T0.7"),
43	        (r"pythia.*t12|pythia.*t1\.2", "Pythia-T1.2"),
44	        (r"pythia", "Pythia"),
45	        (r"olmo", "OLMo"),
46	        (r"mistral", "Mistral-7B"),
47	        (r"llama.*8b", "LLaMA-8B"),
48	        (r"length.?128", "Length-128"),
49	        (r"length.?256", "Length-256"),
50	        (r"length.?512", "Length-512"),
51	    ]
52	    for pat, label in patterns:
53	        if re.search(pat, exp, re.IGNORECASE):
54	            return label
55	    name = source_path.stem if source_path.is_file() els
…[truncated 7060 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T11:32:25.910042+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/exp_D_mcnemar.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/exp_D_mcnemar.py"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T11:32:25.910205+00:00_

1	"""EXP-D McNemar paired test + Bootstrap difference CI: OBD vs LLMs.
2	
3	Re-runs OBD out-of-fold predictions on the same 500 samples as exp-011,
4	then performs McNemar exact test and bootstrap CI on accuracy differences.
5	"""
6	import csv
7	import json
8	import re
9	from pathlib import Path
10	
11	import numpy as np
12	
13	PROJECT = Path("/root/autodl-tmp/gen-depth-contamination")
14	DATA_DIR = PROJECT / "data_exp001_pythia"
15	SAMPLES_PATH = PROJECT / "artifacts" / "exp011_samples.jsonl"
16	GPT_PATH = PROJECT / "artifacts" / "exp011_results_gpt_5_5.jsonl"
17	CLAUDE_PATH = PROJECT / "artifacts" / "exp011_results_claude_opus_4_6.jsonl"
18	OUT_PATH = PROJECT / "artifacts" / "exp_D_mcnemar.json"
19	
20	FEAT_COLS = [
21	    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
22	    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
23	    "surp_d2_mean", "surp_d2_std",
24	    "ttr", "hapax_ratio", "self_bleu",
25	    "freq_kurtosis", "freq_entropy", "low_freq_ratio",
26	]
27	
28	MAX_DEPTH = 5
29	N_SPLITS = 5
30	N_BOOTSTRAP = 10000
31	SEED = 42
32	
33	
34	def load_features():
35	    feat_path = DATA_DIR / "features.csv"
36	    with open(feat_path) as f:
37	        reader = csv.DictReader(f)
38	        rows = list(reader)
39	    depths = np.array([int(r["depth"]) for r in rows])
40	    doc_ids = np.array([int(r["doc_id"]) for r in rows])
41	    X = np.array([
42	        [float(r[c]) if r[c] not in ("", "nan") else np.nan for c in FEAT_COLS]
43	        for r in rows
44	    ])
45	    col_means = np.nanmean(X, axis=0)
46	    for j in range(X.shape[1]):
47	        mask = np.isnan(X[:, j])
48	        X[mask, j] = col_means[j]
49	    return X, depths, doc_ids
50	
51	
52	def run_obd_oof(X, y, groups, max_depth, n_splits):
53	    import lightgbm as lgb
54	    from sklearn.model_selection import GroupKFold
55	
56	    n = len(y)
57	    cum_probs = np.zeros((n, max_depth))
58	    gkf = GroupKFold(n_splits=n_splits)
59	    fold_indices = list(gkf.split(X, y, groups=groups))
60	
61	  
…[truncated 6703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T11:32:25.910367+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/exp_D_obd_n500_v2.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/exp_D_obd_n500_v2.py"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T11:32:25.910524+00:00_

1	"""EXP-D v2: OBD-LightGBM accuracy on the SAME N=500 samples as exp-011 LLM baselines.
2	
3	Corrects exp_D v1 which used plain multiclass LightGBM instead of true OBD.
4	
5	Method:
6	  - True Ordinal Binary Decomposition: K-1 binary LightGBM classifiers for P(Y > k)
7	  - Hyperparameters from exp-010 (paper-consistent): n_estimators=200, max_depth=6, lr=0.05, num_leaves=31
8	  - 5-fold GroupKFold CV on full Pythia data (depths 0-5, N=30000)
9	  - Extract OOF predictions for the specific 500 samples from exp011_samples.jsonl
10	  - Report 5-class accuracy (depths 0-4) + bootstrap CI
11	"""
12	import csv
13	import json
14	import re
15	from pathlib import Path
16	
17	import numpy as np
18	
19	PROJECT = Path("/root/autodl-tmp/gen-depth-contamination")
20	DATA_DIR = PROJECT / "data_exp001_pythia"
21	SAMPLES_PATH = PROJECT / "artifacts" / "exp011_samples.jsonl"
22	OUT_PATH = PROJECT / "artifacts" / "exp_D_obd_n500_v2.json"
23	
24	FEAT_COLS = [
25	    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
26	    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
27	    "surp_d2_mean", "surp_d2_std",
28	    "ttr", "hapax_ratio", "self_bleu",
29	    "freq_kurtosis", "freq_entropy", "low_freq_ratio",
30	]
31	
32	MAX_DEPTH = 5  # depths 0-5, 6 classes (matching exp-010 / paper)
33	N_SPLITS = 5
34	N_BOOTSTRAP = 1000
35	
36	
37	def load_features():
38	    feat_path = DATA_DIR / "features.csv"
39	    with open(feat_path) as f:
40	        reader = csv.DictReader(f)
41	        rows = list(reader)
42	
43	    depths = np.array([int(r["depth"]) for r in rows])
44	    doc_ids = np.array([int(r["doc_id"]) for r in rows])
45	    X = np.array([
46	        [float(r[c]) if r[c] not in ("", "nan") else np.nan for c in FEAT_COLS]
47	        for r in rows
48	    ])
49	    col_means = np.nanmean(X, axis=0)
50	    for j in range(X.shape[1]):
51	        mask = np.isnan(X[:, j])
52	        X[mask, j] = col_means[j]
53	
54	    return X, depths, doc_ids
55	
56	
57	def run_obd_oof(X, y, groups, max_depth, 
…[truncated 6295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T11:32:25.910681+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/draw_kstar_theta.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/draw_kstar_theta.py"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T11:32:25.910861+00:00_

1	#!/usr/bin/env python3
2	"""K* as a function of theta: auto-discovers bootstrap CI JSONs.
3	
4	Input:  artifacts/exp*_bootstrap_ci.json, results_*/bootstrap_ci.json
5	Output: docs/paper/figures/fig_kstar_theta.pdf
6	Deps:   matplotlib, numpy
7	"""
8	
9	import argparse
10	import json
11	import re
12	import matplotlib
13	matplotlib.use("Agg")
14	import matplotlib.pyplot as plt
15	import numpy as np
16	from pathlib import Path
17	
18	TABLEAU_COLORS = [
19	    "#4e79a7", "#e15759", "#76b7b2", "#59a14f",
20	    "#b07aa1", "#ff9da7", "#9c755f", "#bab0ac",
21	    "#edc948", "#f28e2b",
22	]
23	MARKERS = ["o", "s", "^", "D", "v", "P", "X", "*", "h", "<"]
24	LINESTYLES = ["-", "--", "-.", ":", "-", "--", "-.", ":"]
25	
26	
27	def infer_label(source_path: Path, metadata: dict | None = None) -> str:
28	    """Infer model label from file path or JSON metadata."""
29	    if metadata and "experiment" in metadata:
30	        exp = metadata["experiment"].lower()
31	        patterns = [
32	            (r"qwen.*rw|qwen.*rewrite", "Qwen-rw"),
33	            (r"qwen.*base", "Qwen-base"),
34	            (r"qwen.*7b", "Qwen-7B"),
35	            (r"qwen.*cont|qwen.*1\.5", "Qwen-cont"),
36	            (r"pythia", "Pythia"),
37	            (r"olmo", "OLMo"),
38	            (r"mistral", "Mistral-7B"),
39	            (r"llama.*8b", "LLaMA-8B"),
40	        ]
41	        for pat, label in patterns:
42	            if re.search(pat, exp, re.IGNORECASE):
43	                return label
44	
45	    name = source_path.stem if source_path.is_file() else source_path.name
46	    name = re.sub(r"^exp\d+_", "", name).replace("bootstrap_ci", "").strip("_")
47	    patterns = [
48	        (r"qwen.*rw|qwen.*rewrite", "Qwen-rw"),
49	        (r"qwen.*base", "Qwen-base"),
50	        (r"qwen.*7b", "Qwen-7B"),
51	        (r"qwen.*cont|qwen(?!.*rw|.*rewrite|.*base|.*7b)", "Qwen-cont"),
52	        (r"pythia", "Pythia"),
53	        (r"olmo", "OLMo"),
54	        (r"mistral", "Mistral-7B"),
55	        (r"llama", "LLaMA
…[truncated 5352 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T11:32:25.911023+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp008_retrain_chain.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp008_retrain_chain.py"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T11:32:25.911292+00:00_

1	# exp-008: Retrain-chain ecological validity experiment
2	# Each generation: LoRA fine-tune Pythia-1.4B on depth_d → generate depth_{d+1}
3	# Independent LoRA per generation (no accumulation), simulating real-world model collapse scenario
4	
5	import argparse
6	import gc
7	import json
8	import logging
9	import math
10	import os
11	import shutil
12	import sys
13	from collections import Counter
14	from pathlib import Path
15	
16	import numpy as np
17	import torch
18	from scipy import stats
19	from tqdm import tqdm
20	
21	logging.basicConfig(
22	    level=logging.INFO,
23	    format="%(asctime)s [%(levelname)s] %(message)s",
24	    datefmt="%H:%M:%S",
25	    handlers=[logging.StreamHandler(sys.stdout)],
26	)
27	log = logging.getLogger(__name__)
28	
29	
30	# ---------------------------------------------------------------------------
31	# Config
32	# ---------------------------------------------------------------------------
33	
34	PYTHIA_PATH = "/root/autodl-tmp/.hf_cache/models--EleutherAI--pythia-1.4b/snapshots/fedc38a16eea3bd36a96b906d78d11d2ce18ed79"
35	SCORER_PATH = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B"
36	SEED_DATA = "/root/autodl-tmp/gen-depth-contamination/data_exp020_pythia_greedy/depth_0.jsonl"
37	
38	LORA_RANK = 16
39	LORA_ALPHA = 32
40	LORA_TARGET_MODULES = ["query_key_value"]
41	TRAIN_LR = 2e-4
42	TRAIN_BATCH_SIZE = 4
43	GRADIENT_ACCUMULATION = 4
44	TRAIN_EPOCHS = 1
45	
46	GEN_TOP_P = 0.95
47	GEN_TEMPERATURE = 1.0
48	GEN_MAX_NEW_TOKENS = 256
49	GEN_BATCH_SIZE = 8
50	
51	MAX_DEPTH = 4
52	NUM_SAMPLES = 5000
53	
54	
55	# ---------------------------------------------------------------------------
56	# Utilities
57	# ---------------------------------------------------------------------------
58	
59	def load_jsonl(path):
60	    with open(path) as f:
61	        return [json.loads(line) for line in f]
62	
63	
64	def save_jsonl(records, path):
65	    Path(path).parent.mkdir(parents=True, exist_ok=True)
66	    with open(path, "w") as f:
67	        for 
…[truncated 25859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T11:32:25.911508+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts -name \"*.py\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T11:32:25.911648+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_cross_transfer.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp013_cross_transfer.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/draw_pipeline_figure.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/exp_D_obd_n500_v2.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/analyze_exp006.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/draw_kstar_theta.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_pipeline.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/plot_fig_jsd_decay.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp009_dose_response.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/exp025_pythia_filtering.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/exp_B_14d_ablation.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/exp_E_paired_stats.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/exp006_fill_discussion.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/plot_exp003_decoding_ablation.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/exp006_analyze_results.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp015_neural_probe.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/exp_D_mcnemar.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T11:32:25.911810+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "def.*bootstrap|N_BOOTSTRAP|rng\\.(choice|randint)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "type": "py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Grep",
  "tool_args": {
    "pattern": "def.*bootstrap|N_BOOTSTRAP|rng\\.(choice|randint)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
    "type": "py",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-18T11:32:25.911947+00:00_

Found 19 files
artifacts/exp008_retrain_chain.py
artifacts/scripts/plot_auc_decay_ci.py
artifacts/exp-004/intermediate/run_exp004_qwen7b_depth.py
artifacts/run_exp004_qwen7b_depth.py
scripts/exp_D_mcnemar.py
scripts/exp_D_obd_n500_v2.py
artifacts/exp006_filtering_strategies.py
.venv/lib/python3.14/site-packages/matplotlib/tests/test_cbook.py
.venv/lib/python3.14/site-packages/matplotlib/cbook.py
.venv/lib/python3.14/site-packages/numpy/random/tests/test_randomstate_regression.py
.venv/lib/python3.14/site-packages/numpy/random/tests/test_randomstate.py
.venv/lib/python3.14/site-packages/numpy/random/tests/test_random.py
.venv/lib/python3.14/site-packages/numpy/ma/tests/test_arrayobject.py
.venv/lib/python3.14/site-packages/numpy/_core/tests/test_numeric.py
.venv/lib/python3.14/site-packages/numpy/_core/tests/test_multithreading.py
.venv/lib/python3.14/site-packages/numpy/_core/tests/test_mem_overlap.py
scripts/run_exp015_neural_probe.py
scripts/run_exp009_dose_response.py
scripts/run_pipeline.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-18T11:32:25.912084+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/exp_E_paired_stats.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/exp_E_paired_stats.py"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-18T11:32:25.912239+00:00_

1	"""EXP-E: Pairwise paired t-tests for 6 strategies × 5 seeds (MMLU & HellaSwag)."""
2	
3	import json
4	import os
5	import sys
6	from itertools import combinations
7	import numpy as np
8	from scipy import stats
9	
10	BASE_DIR = "/root/autodl-tmp/gen-depth-contamination/outputs/exp006"
11	OUT_PATH = "/root/autodl-tmp/gen-depth-contamination/artifacts/exp_E_paired_stats.json"
12	
13	MAIN_STRATEGIES = ["binary-ours", "binary-drayson", "surprisal", "graduated_a0.9", "dsir", "no-filter"]
14	GRADUATED_ALPHAS = ["graduated_a0.1", "graduated_a0.3", "graduated_a0.5", "graduated_a0.7"]
15	ALL_STRATEGIES = MAIN_STRATEGIES + GRADUATED_ALPHAS
16	SEEDS = [42, 123, 456, 789, 1024]
17	
18	
19	def load_scores():
20	    data = {}
21	    for strat in ALL_STRATEGIES:
22	        data[strat] = {"mmlu": [], "hellaswag": []}
23	        for seed in SEEDS:
24	            path = os.path.join(BASE_DIR, f"{strat}_s{seed}", "eval_results.json")
25	            with open(path) as f:
26	                res = json.load(f)
27	            data[strat]["mmlu"].append(res["scores"]["mmlu"]["acc,none"])
28	            data[strat]["hellaswag"].append(res["scores"]["hellaswag"]["acc_norm,none"])
29	    return data
30	
31	
32	def cohens_d_paired(x, y):
33	    x, y = np.array(x), np.array(y)
34	    pooled_sd = np.sqrt((np.var(x, ddof=1) + np.var(y, ddof=1)) / 2)
35	    return float(np.mean(x - y) / pooled_sd) if pooled_sd > 0 else 0.0
36	
37	
38	def holm_bonferroni(p_values):
39	    n = len(p_values)
40	    indexed = sorted(enumerate(p_values), key=lambda x: x[1])
41	    corrected = [None] * n
42	    cummax = 0.0
43	    for rank, (orig_idx, p) in enumerate(indexed):
44	        adjusted = p * (n - rank)
45	        adjusted = max(adjusted, cummax)
46	        adjusted = min(adjusted, 1.0)
47	        cummax = adjusted
48	        corrected[orig_idx] = adjusted
49	    return corrected
50	
51	
52	def run_pairwise(data, metric, strategies):
53	    pairs = list(combinations(strategies, 2))
54	    raw_ps = []
55	    r
…[truncated 5517 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-18T11:32:25.912399+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp009_dose_response.py",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp009_dose_response.py",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-18T11:32:25.912550+00:00_

1	"""exp009 Dose-Response — graduated vs binary filtering at varying synthetic injection ratios.
2	
3	Measures downstream LM quality (MMLU/HellaSwag) after continued pretraining on data
4	with 10%/30%/50% synthetic injection, filtered by graduated vs binary-ours strategies.
5	Fixed dataset size (default 5000) across all ratios ensures training cost parity.
6	
7	Input:  data/ directory (features.csv + depth_*.jsonl, same as exp-006)
8	        Qwen2.5-1.5B-Instruct base model (local path or HF hub)
9	Output: outputs/exp009/r&lt;ratio>_&lt;strategy>_s&lt;seed>/eval_results.json  (per-run)
10	        outputs/exp009/analysis.json                                   (paired t-tests)
11	
12	Usage:
13	    # Dry-run: 1 seed, 200 samples, 10 training steps, hellaswag-only eval (limit=20)
14	    python run_exp009_dose_response.py --dry-run
15	
16	    # Full experiment (30 runs)
17	    python run_exp009_dose_response.py
18	
19	    # Single config
20	    python run_exp009_dose_response.py --ratios 0.3 --strategies graduated --seeds 42
21	
22	    # Analyze existing results only
23	    python run_exp009_dose_response.py --analyze-only
24	
25	Dependencies: torch, transformers, peft, lightgbm, lm_eval, numpy, pandas, scipy
26	"""
27	
28	import argparse
29	import json
30	import os
31	import sys
32	import time
33	import traceback
34	from collections import defaultdict
35	
36	import numpy as np
37	import pandas as pd
38	import torch
39	from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
40	from transformers import (
41	    AutoModelForCausalLM,
42	    AutoTokenizer,
43	    DataCollatorForLanguageModeling,
44	    Trainer,
45	    TrainingArguments,
46	    set_seed,
47	)
48	from peft import LoraConfig, get_peft_model, TaskType
49	from scipy import stats
50	
51	sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
52	from exp006_filtering_strategies import STRATEGIES, FEATURE_COLS, load_data
53	
54	
55	def prepare_dose_data(df, texts, ratio, seed, total_n):
56	    """Subs
…[truncated 3633 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-18T11:32:25.912758+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp006_filtering_strategies.py",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp006_filtering_strategies.py",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-18T11:32:25.913023+00:00_

1	"""exp006 Filtering Strategies — 6 data quality filters for depth chain data.
2	
3	Input:  features.csv (30000 rows: doc_id, depth, 15 features)
4	        depth_*.jsonl (text data, needed for DSIR)
5	Output: per-sample weights [0,1] via get_weights(), boolean mask via get_mask()
6	
7	Strategies:
8	  1. no-filter      — uniform weights (baseline)
9	  2. binary-ours    — LightGBM binary (human vs synthetic), threshold=0.5
10	  3. binary-drayson — SIR resampling (Drayson et al. 2025), b=1, k=1.5
11	  4. graduated      — OBD-LightGBM ordinal + exp(-alpha*d) weighting
12	  5. surprisal      — surp_mean median threshold
13	  6. dsir           — n-gram importance resampling (Xie et al. 2023)
14	"""
15	
16	import argparse
17	import json
18	import os
19	from abc import ABC, abstractmethod
20	from collections import Counter
21	from hashlib import md5
22	
23	import numpy as np
24	import pandas as pd
25	
26	FEATURE_COLS = [
27	    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
28	    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
29	    "surp_d2_mean", "surp_d2_std",
30	    "ttr", "hapax_ratio", "self_bleu",
31	    "freq_kurtosis", "freq_entropy", "low_freq_ratio",
32	]
33	
34	
35	class FilterStrategy(ABC):
36	    @abstractmethod
37	    def fit(self, features: np.ndarray, depths: np.ndarray, texts: list = None):
38	        ...
39	
40	    @abstractmethod
41	    def get_weights(self, features: np.ndarray, texts: list = None) -> np.ndarray:
42	        ...
43	
44	    def get_mask(self, features: np.ndarray, texts: list = None, threshold: float = 0.0) -> np.ndarray:
45	        return self.get_weights(features, texts) > threshold
46	
47	
48	class NoFilter(FilterStrategy):
49	    def fit(self, features, depths, texts=None):
50	        pass
51	
52	    def get_weights(self, features, texts=None):
53	        return np.ones(len(features))
54	
55	
56	class BinaryOurs(FilterStrategy):
57	    """LightGBM binary: human (depth=0) vs synthetic (depth>=1).
58	    Weight = 1 - P(synthetic).
…[truncated 3583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-18T11:32:25.913210+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_pipeline.py",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_pipeline.py",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-18T11:32:25.913362+00:00_

1	"""
2	MVP Pilot Saturation Study — Complete Pipeline (Steps 2-5)
3	
4	Generates recursive depth chains from C4 seed data using Qwen2.5-1.5B,
5	extracts statistical features, and runs distinguishability analysis.
6	
7	Input:  C4 validation split (streamed from HuggingFace)
8	Output: data/depth_{0..K}.jsonl, data/features.csv, results/*.json + summary.txt
9	
10	Key deps: torch, transformers, datasets, scipy, lightgbm, sklearn, tqdm
11	"""
12	
13	import argparse
14	import json
15	import logging
16	import math
17	import os
18	import sys
19	from collections import Counter
20	from pathlib import Path
21	
22	import numpy as np
23	import torch
24	from scipy import stats
25	from tqdm import tqdm
26	
27	logging.basicConfig(
28	    level=logging.INFO,
29	    format="%(asctime)s [%(levelname)s] %(message)s",
30	    datefmt="%H:%M:%S",
31	)
32	log = logging.getLogger(__name__)
33	
34	
35	# ---------------------------------------------------------------------------
36	# Utility: simple 4-gram BLEU (no nltk dependency)
37	# ---------------------------------------------------------------------------
38	
39	def ngrams(tokens, n):
40	    return [tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)]
41	
42	
43	def simple_bleu(candidate_tokens, reference_tokens, max_n=4):
44	    """Compute sentence-level BLEU up to max_n grams with brevity penalty."""
45	    if len(candidate_tokens) == 0:
46	        return 0.0
47	    precisions = []
48	    for n in range(1, max_n + 1):
49	        cand_ngrams = ngrams(candidate_tokens, n)
50	        ref_ngrams = ngrams(reference_tokens, n)
51	        if not cand_ngrams:
52	            precisions.append(0.0)
53	            continue
54	        ref_counts = Counter(ref_ngrams)
55	        clipped = 0
56	        cand_counts = Counter(cand_ngrams)
57	        for ng, cnt in cand_counts.items():
58	            clipped += min(cnt, ref_counts.get(ng, 0))
59	        precisions.append(clipped / len(cand_ngrams))
60	    if any(p == 0 for p in precisions):

…[truncated 2035 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T11:32:25.913570+00:00_

Perfect! Now I have a comprehensive understanding of the bootstrap CI implementation. Let me compile the findings:

## Bootstrap CI Scripts Summary

I've successfully located and analyzed the bootstrap resampling logic used in this project. Here are the key findings:

### Primary Bootstrap CI Implementation Files

**1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/exp_D_mcnemar.py`** (Lines 120-129)
   - Implements `bootstrap_diff_ci()` function for bootstrap difference confidence intervals
   - **Logic**: Resamples data with replacement (n=10,000 bootstrap samples), computes accuracy differences between two methods per sample
   - **CI Calculation**: Uses 2.5th and 97.5th percentiles of the bootstrap distribution
   - Used for McNemar paired test + bootstrap CI comparing OBD vs LLM predictions

**2. `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/exp_D_obd_n500_v2.py`** (Lines 101-108)
   - Implements `bootstrap_ci()` function
   - **Logic**: Bootstrap resamples N=1,000 times, computing accuracy on each resample
   - **CI Calculation**: Percentile method (2.5th/97.5th percentiles)
   - Used for single-model bootstrap CI on OBD LightGBM classifier

**3. `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp008_retrain_chain.py`** (Lines 485-522)
   - Implements bootstrap CI within `run_analysis()` function
   - **Logic**: 10,000 bootstrap resamples with replacement, trains classifier on each resample
   - **Model Fitting**: LightGBM trained fresh on each bootstrap sample
   - **CI Calculation**: Percentile method on bootstrap AUC distributions
   - Comprehensive pipeline with pairwise AUC, JSD, K*, permutation tests

**4. `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/scripts/plot_auc_decay_ci.py`** (Lines 85-125)
   - **Data Loading**: Reads pre-computed bootstrap CI JSON files
   - **Two Methods
…[truncated 1712 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Agent",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T11:32:25.913757+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls -la /root/autodl-tmp/gen-depth-contamination/data/exp_027_latex_ablation/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls -la /root/autodl-tmp/gen-depth-contamination/data/exp_027_latex_ablation/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T11:32:25.913928+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 17292\\ndrwxr-xr-x  2 root root     184 May 18 18:34 .\\ndrwxr-xr-x 27 root root    4096 May 18 18:23 ..\\n-rw-r--r--  1 root root 3133386 May 18 18:23 depth_0.jsonl\\n-rw-r--r--  1 root root 2032215 May 18 18:23 depth_1.jsonl\\n-rw-r--r--  1 root root 2211102 May 18 18:23 depth_2.jsonl\\n-rw-r--r--  1 root root 2246339 May 18 18:23 depth_3.jsonl\\n-rw-r--r--  1 root root 2205612 May 18 18:23 depth_4.jsonl\\n-rw-r--r--  1 root root 2118176 May 18 18:23 depth_5.jsonl\\n-rw-r--r--  1 root root 3741498 May 18 18:34 features.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.86}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-18T11:32:25.914059+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls -la /root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls -la /root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T11:32:25.914189+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 24\\ndrwxr-xr-x  2 root root  149 May 18 18:35 .\\ndrwxr-xr-x 33 root root 4096 May 18 18:26 ..\\n-rw-r--r--  1 root root  639 May 18 18:35 feature_importance.json\\n-rw-r--r--  1 root root   96 May 18 18:34 jsd.json\\n-rw-r--r--  1 root root   56 May 18 18:35 ordinal_results.json\\n-rw-r--r--  1 root root  575 May 18 18:34 pairwise_auc.json\\n-rw-r--r--  1 root root 1326 May 18 18:35 summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T11:32:25.914319+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp008_retrain_chain.py",
  "limit": "100",
  "offset": "470"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp008_retrain_chain.py",
    "limit": "100",
    "offset": "470"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T11:32:25.914475+00:00_

470	            jsd = 0.5 * np.sum(p * np.log2(p / m)) + 0.5 * np.sum(q * np.log2(q / m))
471	            jsds.append(float(jsd))
472	        pairwise_jsd[f"{k-1}v{k}"] = round(float(np.mean(jsds)), 6)
473	        log.info(f"  JSD({k-1} vs {k}) = {np.mean(jsds):.6f}")
474	
475	    with open(results_dir / "jsd.json", "w") as f:
476	        json.dump(pairwise_jsd, f, indent=2)
477	
478	    # K*
479	    k_star = 0
480	    for k in range(1, max_depth + 1):
481	        if pairwise_auc.get(f"{k-1}v{k}", 0) > 0.60:
482	            k_star = k
483	    log.info(f"K* = {k_star}")
484	
485	    # Bootstrap CI
486	    log.info("Bootstrap CI (10000 resamples)...")
487	    bootstrap_results = {}
488	    rng = np.random.RandomState(42)
489	    for k in range(1, max_depth + 1):
490	        mask = (depths == k - 1) | (depths == k)
491	        X = feat_matrix[mask]
492	        y = (depths[mask] == k).astype(int)
493	        groups = doc_ids[mask]
494	        if len(np.unique(y)) < 2:
495	            continue
496	
497	        n = len(X)
498	        boot_aucs = []
499	        for _ in range(10000):
500	            idx = rng.choice(n, n, replace=True)
501	            X_b, y_b = X[idx], y[idx]
502	            if len(np.unique(y_b)) < 2:
503	                continue
504	            clf = lgb.LGBMClassifier(
505	                n_estimators=100, max_depth=6, learning_rate=0.05,
506	                num_leaves=31, verbose=-1, n_jobs=-1,
507	            )
508	            clf.fit(X_b, y_b)
509	            proba = clf.predict_proba(X_b)[:, 1]
510	            boot_aucs.append(roc_auc_score(y_b, proba))
511	
512	        if boot_aucs:
513	            ci_lo = float(np.percentile(boot_aucs, 2.5))
514	            ci_hi = float(np.percentile(boot_aucs, 97.5))
515	            bootstrap_results[f"{k-1}v{k}"] = {
516	                "mean": round(float(np.mean(boot_aucs)), 4),
517	                "ci_95": [round(ci_lo, 4), round(ci_hi, 4)],
518	            }
519	            log.info(f"  Bootstrap AUC({k-1}
…[truncated 2208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-18T11:32:25.914642+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "head -3 /root/autodl-tmp/gen-depth-contamination/data/exp_027_latex_ablation/features.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "head -3 /root/autodl-tmp/gen-depth-contamination/data/exp_027_latex_ablation/features.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T11:32:25.914792+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"doc_id,depth,surp_mean,surp_std,surp_skew,surp_kurt,surp_d1_mean,surp_d1_std,surp_d1_skew,surp_d2_mean,surp_d2_std,ttr,hapax_ratio,self_bleu,freq_kurtosis,freq_entropy,low_freq_ratio\\r\\n0,0,3.2880189076383064,3.0792762398852567,1.0022333493853872,0.21667259078267787,-0.014234875444839857,4.021983532992029,0.10126073360253228,0.047920460786138264,6.8147699031169005,0.7371134020618557,0.8391608391608392,0.0,17.058097793268516,6.885246847578275,0.9300699300699301\\r\\n1,0,3.2794168031821815,2.833895853612952,0.9374791895368758,0.44950793517850096,-0.021321614583333332,3.7925839759708673,-0.1340113795964952,0.01903463630546075,6.440128629716455,0.7316017316017316,0.834319526627219,0.0009856785965805328,16.14255093488592,7.129627829265425,0.9171597633136095\\r\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-18T11:32:25.914935+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/pairwise_auc.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/pairwise_auc.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T11:32:25.915077+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"mean\\\": {\\n    \\\"0v1\\\": 0.9948,\\n    \\\"1v2\\\": 0.8297,\\n    \\\"2v3\\\": 0.6229,\\n    \\\"3v4\\\": 0.5468,\\n    \\\"4v5\\\": 0.5476\\n  },\\n  \\\"per_fold\\\": {\\n    \\\"0v1\\\": [\\n      0.9905,\\n      0.9979,\\n      0.9937,\\n      0.9974,\\n      0.9943\\n    ],\\n    \\\"1v2\\\": [\\n      0.8085,\\n      0.8529,\\n      0.8198,\\n      0.8292,\\n      0.8381\\n    ],\\n    \\\"2v3\\\": [\\n      0.6429,\\n      0.6196,\\n      0.6258,\\n      0.5986,\\n      0.6275\\n    ],\\n    \\\"3v4\\\": [\\n      0.5515,\\n      0.572,\\n      0.5373,\\n      0.5589,\\n      0.5142\\n    ],\\n    \\\"4v5\\\": [\\n      0.537,\\n      0.5757,\\n      0.5458,\\n      0.5527,\\n      0.527\\n    ]\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-18T11:32:25.915203+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/summary.txt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/summary.txt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-18T11:32:25.915380+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"============================================================\\nMVP Pilot Saturation Study — Results Summary\\n============================================================\\n\\nPairwise AUC (adjacent depths):\\n  depth 0 vs 1: AUC = 0.9948 ± 0.0027  folds=[0.9905, 0.9979, 0.9937, 0.9974, 0.9943]\\n  depth 1 vs 2: AUC = 0.8297 ± 0.0152  folds=[0.8085, 0.8529, 0.8198, 0.8292, 0.8381]\\n  depth 2 vs 3: AUC = 0.6229 ± 0.0144  folds=[0.6429, 0.6196, 0.6258, 0.5986, 0.6275]\\n  depth 3 vs 4: AUC = 0.5468 ± 0.0198  folds=[0.5515, 0.572, 0.5373, 0.5589, 0.5142]\\n  depth 4 vs 5: AUC = 0.5476 ± 0.0165  folds=[0.537, 0.5757, 0.5458, 0.5527, 0.527]\\n\\nPairwise JSD (adjacent depths):\\n  depth 0 vs 1: JSD = 0.201513\\n  depth 1 vs 2: JSD = 0.062547\\n  depth 2 vs 3: JSD = 0.01612\\n  depth 3 vs 4: JSD = 0.007644\\n  depth 4 vs 5: JSD = 0.007585\\n\\nK* (max depth with AUC > 0.60): 3\\n\\nOrdinal Classification (6-class, 5-fold CV):\\n  MAE = 0.8817\\n  Accuracy = 0.4589\\n\\nTop-10 Feature Importance:\\n  freq_entropy         9922.6\\n  surp_std             7667.0\\n  surp_d1_skew         7578.2\\n  surp_d1_mean         7132.6\\n  surp_mean            7072.0\\n  surp_d2_mean         6947.4\\n  freq_kurtosis        6818.0\\n  surp_kurt            6704.4\\n  surp_d1_std          6664.8\\n  surp_skew            6071.2\\n\\n============================================================\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-18T11:32:25.915535+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "wc -l /root/autodl-tmp/gen-depth-contamination/data/exp_027_latex_ablation/features.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "wc -l /root/autodl-tmp/gen-depth-contamination/data/exp_027_latex_ablation/features.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-18T11:32:25.915700+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"13201 /root/autodl-tmp/gen-depth-contamination/data/exp_027_latex_ablation/features.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-18T11:32:25.916040+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-18T11:32:25.916186+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-18T11:32:25.916337+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "account": "root",
  "command": "cat > /root/autodl-tmp/gen-depth-contamination/scripts/exp027_bootstrap_ci.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"exp_027 Bootstrap CI: doc-level bootstrap on OOF predictions + permutation test.\"\"\"\n\nimport json\nimport time\nimport numpy as np\nimport pandas as pd\nimport lightgbm as lgb\nfrom pathlib import Path\nfrom sklearn.model_selection import GroupKFold\nfrom sklearn.metrics import roc_auc_score\n\nDATA_DIR = Path(\"/root/autodl-tmp/gen-depth-contamination/data/exp_027_latex_ablation\")\nRESULTS_DIR = Path(\"/root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation\")\nN_BOOT = 10_000\nN_PERM = 1_000\nSEED = 42\nTHETA = 0.60\n\nLGB_PARAMS = dict(\n    n_estimators=200, max_depth=6, learning_rate=0.05,\n    num_leaves=31, verbose=-1, n_jobs=-1,\n)\n\n\ndef main():\n    t0 = time.time()\n    df = pd.read_csv(DATA_DIR / \"features.csv\")\n    feat_cols = [c for c in df.columns if c not in (\"doc_id\", \"depth\")]\n    print(f\"Data: {len(df)} rows, {len(feat_cols)} features, depths {sorted(df.depth.unique())}\")\n\n    pairs = [\"0v1\", \"1v2\", \"2v3\", \"3v4\", \"4v5\"]\n    results = {}\n\n    for pair in pairs:\n        lo, hi = int(pair[0]), int(pair[2])\n        sub = df[df[\"depth\"].isin([lo, hi])].copy().reset_index(drop=True)\n        X = sub[feat_cols].values\n        y = (sub[\"depth\"] == hi).astype(int).values\n        doc_ids = sub[\"doc_id\"].values\n        unique_docs = np.unique(doc_ids)\n\n        print(f\"\\n--- {pair}: {len(sub)} samples, {len(unique_docs)} docs ---\")\n\n        # Step 1: GroupKFold(5) OOF predictions\n        oof = np.zeros(len(X))\n        fold_aucs = []\n        gkf = GroupKFold(n_splits=5)\n        for tr, te in gkf.split(X, y, groups=doc_ids):\n            clf = lgb.LGBMClassifier(**LGB_PARAMS)\n            clf.fit(X[tr], y[tr])\n            oof[te] = clf.predict_proba(X[te])[:, 1]\n            fold_aucs.append(roc_auc_score(y[te], oof[te]))\n\n        point_est = roc_auc_score(y, oof)\n        print(f\"  OOF AUC = {point_est:.4f}  folds={[round(a,4) for a in fold_aucs]}\")\n\n        # Step 2: Doc-level bootstrap CI on OOF predictions\n        doc_to_idx = {d: np.where(doc_ids == d)[0] for d in unique_docs}\n        rng = np.random.RandomState(SEED)\n        boot_aucs = []\n        for _ in range(N_BOOT):\n            bd = rng.choice(unique_docs, len(unique_docs), replace=True)\n            bi = np.concatenate([doc_to_idx[d] for d in bd])\n            yb, pb = y[bi], oof[bi]\n            if len(np.unique(yb)) < 2:\n                continue\n            boot_aucs.append(roc_auc_score(yb, pb))\n\n        ci_lo = float(np.percentile(boot_aucs, 2.5))\n        ci_hi = float(np.percentile(boot_aucs, 97.5))\n        print(f\"  CI95 = [{ci_lo:.4f}, {ci_hi:.4f}]  boot_mean={np.mean(boot_aucs):.4f}  ({len(boot_aucs)}/{N_BOOT} valid)\")\n\n        result = {\n            \"point_estimate\": round(point_est, 4),\n            \"boot_mean\": round(float(np.mean(boot_aucs)), 4),\n            \"ci_lower\": round(ci_lo, 4),\n            \"ci_upper\": round(ci_hi, 4),\n            \"per_fold\": [round(a, 4) for a in fold_aucs],\n            \"n_boot_valid\": len(boot_aucs),\n        }\n\n        # Step 3: Permutation test (2v3 only)\n        # Permute labels against fixed OOF predictions; under H0 labels are\n        # independent of predictions so AUC ~ 0.5\n        if pair == \"2v3\":\n            rng_p = np.random.RandomState(SEED + 1)\n            perm_aucs = []\n            for _ in range(N_PERM):\n                y_perm = rng_p.permutation(y)\n                if len(np.unique(y_perm)) < 2:\n                    continue\n                perm_aucs.append(roc_auc_score(y_perm, oof))\n\n            p_val = float(np.mean([a >= point_est for a in perm_aucs]))\n            result[\"p_value\"] = round(p_val, 6)\n            result[\"perm_null_mean\"] = round(float(np.mean(perm_aucs)), 4)\n            result[\"perm_null_std\"] = round(float(np.std(perm_aucs)), 4)\n            result[\"n_perm\"] = len(perm_aucs)\n            print(f\"  Perm test: p={p_val:.6f}  null={np.mean(perm_aucs):.4f}+/-{np.std(perm_aucs):.4f}\")\n\n        results[pair] = result\n\n    # Summary\n    print(f\"\\n{'='*60}\")\n    print(\"RESULTS SUMMARY\")\n    print(f\"{'='*60}\")\n    for pair, r in results.items():\n        s = f\"  {pair}: AUC={r['point_estimate']:.4f} [{r['ci_lower']:.4f}, {r['ci_upper']:.4f}]\"\n        if \"p_value\" in r:\n            s += f\"  p={r['p_value']:.6f}\"\n        s += f\"  ci_lo {'>' if r['ci_lower'] > THETA else '<='} theta={THETA}\"\n        print(s)\n\n    r23 = results[\"2v3\"]\n    verdict = r23[\"ci_lower\"] > THETA\n    print(f\"\\n*** 2v3 CI lower = {r23['ci_lower']:.4f} {'>' if verdict else '<='} theta={THETA}\")\n    print(f\"    -> {'CONFIRMED: signal above threshold' if verdict else 'BELOW threshold'}\")\n    print(f\"\\nTotal: {time.time()-t0:.1f}s\")\n\n    RESULTS_DIR.mkdir(parents=True, exist_ok=True)\n    out = RESULTS_DIR / \"bootstrap_ci_results.json\"\n    with open(out, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"Saved: {out}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "account": "root",
    "command": "cat > /root/autodl-tmp/gen-depth-contamination/scripts/exp027_bootstrap_ci.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"exp_027 Bootstrap CI: doc-level bootstrap on OOF predictions + permutation test.\"\"\"\n\nimport json\nimport time\nimport numpy as np\nimport pandas as pd\nimport lightgbm as lgb\nfrom pathlib import Path\nfrom sklearn.model_selection import GroupKFold\nfrom sklearn.metrics import roc_auc_score\n\nDATA_DIR = Path(\"/root/autodl-tmp/gen-depth-contamination/data/exp_027_latex_ablation\")\nRESULTS_DIR = Path(\"/root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation\")\nN_BOOT = 10_000\nN_PERM = 1_000\nSEED = 42\nTHETA = 0.60\n\nLGB_PARAMS = dict(\n    n_estimators=200, max_depth=6, learning_rate=0.05,\n    num_leaves=31, verbose=-1, n_jobs=-1,\n)\n\n\ndef main():\n    t0 = time.time()\n    df = pd.read_csv(DATA_DIR / \"features.csv\")\n    feat_cols = [c for c in df.columns if c not in (\"doc_id\", \"depth\")]\n    print(f\"Data: {len(df)} rows, {len(feat_cols)} features, depths {sorted(df.depth.unique())}\")\n\n    pairs = [\"0v1\", \"1v2\", \"2v3\", \"3v4\", \"4v5\"]\n    results = {}\n\n    for pair in pairs:\n        lo, hi = int(pair[0]), int(pair[2])\n        sub = df[df[\"depth\"].isin([lo, hi])].copy().reset_index(drop=True)\n        X = sub[feat_cols].values\n        y = (sub[\"depth\"] == hi).astype(int).values\n        doc_ids = sub[\"doc_id\"].values\n        unique_docs = np.unique(doc_ids)\n\n        print(f\"\\n--- {pair}: {len(sub)} samples, {len(unique_docs)} docs ---\")\n\n        # Step 1: GroupKFold(5) OOF predictions\n        oof = np.zeros(len(X))\n        fold_aucs = []\n        gkf = GroupKFold(n_splits=5)\n        for tr, te in gkf.split(X, y, groups=doc_ids):\n            clf = lgb.LGBMClassifier(**LGB_PARAMS)\n            clf.fit(X[tr], y[tr])\n            oof[te] = clf.predict_proba(X[te])[:, 1]\n            fold_aucs.append(roc_auc_score(y[te], oof[te]))\n\n        point_est = roc_auc_score(y, oof)\n        print(f\"  OOF AUC = {point_est:.4f}  folds={[round(a,4) for a in fold_aucs]}\")\n\n        # Step 2: Doc-level bootstrap CI on OOF predictions\n        doc_to_idx = {d: np.where(doc_ids == d)[0] for d in unique_docs}\n        rng = np.random.RandomState(SEED)\n        boot_aucs = []\n        for _ in range(N_BOOT):\n            bd = rng.choice(unique_docs, len(unique_docs), replace=True)\n            bi = np.concatenate([doc_to_idx[d] for d in bd])\n            yb, pb = y[bi], oof[bi]\n            if len(np.unique(yb)) < 2:\n                continue\n            boot_aucs.append(roc_auc_score(yb, pb))\n\n        ci_lo = float(np.percentile(boot_aucs, 2.5))\n        ci_hi = float(np.percentile(boot_aucs, 97.5))\n        print(f\"  CI95 = [{ci_lo:.4f}, {ci_hi:.4f}]  boot_mean={np.mean(boot_aucs):.4f}  ({len(boot_aucs)}/{N_BOOT} valid)\")\n\n        result = {\n            \"point_estimate\": round(point_est, 4),\n            \"boot_mean\": round(float(np.mean(boot_aucs)), 4),\n            \"ci_lower\": round(ci_lo, 4),\n            \"ci_upper\": round(ci_hi, 4),\n            \"per_fold\": [round(a, 4) for a in fold_aucs],\n            \"n_boot_valid\": len(boot_aucs),\n        }\n\n        # Step 3: Permutation test (2v3 only)\n        # Permute labels against fixed OOF predictions; under H0 labels are\n        # independent of predictions so AUC ~ 0.5\n        if pair == \"2v3\":\n            rng_p = np.random.RandomState(SEED + 1)\n            perm_aucs = []\n            for _ in range(N_PERM):\n                y_perm = rng_p.permutation(y)\n                if len(np.unique(y_perm)) < 2:\n                    continue\n                perm_aucs.append(roc_auc_score(y_perm, oof))\n\n            p_val = float(np.mean([a >= point_est for a in perm_aucs]))\n            result[\"p_value\"] = round(p_val, 6)\n            result[\"perm_null_mean\"] = round(float(np.mean(perm_aucs)), 4)\n            result[\"perm_null_std\"] = round(float(np.std(perm_aucs)), 4)\n            result[\"n_perm\"] = len(perm_aucs)\n            print(f\"  Perm test: p={p_val:.6f}  null={np.mean(perm_aucs):.4f}+/-{np.std(perm_aucs):.4f}\")\n\n        results[pair] = result\n\n    # Summary\n    print(f\"\\n{'='*60}\")\n    print(\"RESULTS SUMMARY\")\n    print(f\"{'='*60}\")\n    for pair, r in results.items():\n        s = f\"  {pair}: AUC={r['point_estimate']:.4f} [{r['ci_lower']:.4f}, {r['ci_upper']:.4f}]\"\n        if \"p_value\" in r:\n            s += f\"  p={r['p_value']:.6f}\"\n        s += f\"  ci_lo {'>' if r['ci_lower'] > THETA else '<='} theta={THETA}\"\n        print(s)\n\n    r23 = results[\"2v3\"]\n    verdict = r23[\"ci_lower\"] > THETA\n    print(f\"\\n*** 2v3 CI lower = {r23['ci_lower']:.4f} {'>' if verdict else '<='} theta={THETA}\")\n    print(f\"    -> {'CONFIRMED: signal above threshold' if verdict else 'BELOW threshold'}\")\n    print(f\"\\nTotal: {time.time()-t0:.1f}s\")\n\n    RESULTS_DIR.mkdir(parents=True, exist_ok=True)\n    out = RESULTS_DIR / \"bootstrap_ci_results.json\"\n    with open(out, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"Saved: {out}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written.\""
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-18T11:32:25.916517+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-18T11:32:25.916646+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "account": "root",
  "command": "cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp027_bootstrap_ci.py 2>&1",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "account": "root",
    "command": "cd /root/autodl-tmp/gen-depth-contamination && python scripts/exp027_bootstrap_ci.py 2>&1",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-18T11:32:25.916798+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"bash: line 1: python: command not found\\n\", \"stderr\": \"\", \"return_code\": 127}, \"error\": \"exit code 127\", \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-18T11:32:25.916930+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "account": "root",
  "command": "cd /root/autodl-tmp/gen-depth-contamination && python3 scripts/exp027_bootstrap_ci.py 2>&1",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "account": "root",
    "command": "cd /root/autodl-tmp/gen-depth-contamination && python3 scripts/exp027_bootstrap_ci.py 2>&1",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-18T11:32:25.917058+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"Traceback (most recent call last):\\n  File \\\"/root/autodl-tmp/gen-depth-contamination/scripts/exp027_bootstrap_ci.py\\\", line 7, in &lt;module>\\n    import pandas as pd\\nModuleNotFoundError: No module named 'pandas'\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-18T11:32:25.917179+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__detect_image",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__detect_image",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-18T11:32:25.917294+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-18T11:32:25.917405+00:00_

called mcp__agent-ml-research__detect_image

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image</summary>

```json
{
  "server": "cqa1-22115",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__detect_image",
  "tool_args": {
    "server": "cqa1-22115",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-18T11:32:25.917627+00:00_

{"result":"{\n  \"detected\": false,\n  \"status\": \"ssh_error\",\n  \"skip_base_setup\": false,\n  \"message\": \"SSH error: exit code 1\"\n}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__detect_image",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-18T11:32:25.917837+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "which python3",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "which python3",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-18T11:32:25.918039+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'which' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-18T11:32:25.918225+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls /root/miniconda3/envs/ /root/anaconda3/envs/ /opt/conda/envs/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls /root/miniconda3/envs/ /root/anaconda3/envs/ /opt/conda/envs/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-18T11:32:25.918408+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-18T11:32:25.918598+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "ls /root/miniconda3/envs/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "ls /root/miniconda3/envs/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-18T11:32:25.918799+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-18T11:32:25.918985+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "account": "root",
  "command": "which python3 && python3 -c \"import sys; print(sys.executable, sys.version)\"",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "account": "root",
    "command": "which python3 && python3 -c \"import sys; print(sys.executable, sys.version)\"",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-18T11:32:25.919168+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/usr/bin/python3\\n/usr/bin/python3 3.10.12 (main, Mar  3 2026, 11:56:32) [GCC 11.4.0]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-18T11:32:25.919365+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "account": "root",
  "command": "pip3 install pandas numpy scikit-learn lightgbm 2>&1 | tail -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "account": "root",
    "command": "pip3 install pandas numpy scikit-learn lightgbm 2>&1 | tail -5"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-18T11:32:25.919554+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Requirement already satisfied: scipy>=1.8.0 in /usr/local/lib/python3.10/dist-packages (from scikit-learn) (1.15.3)\\nRequirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\\nInstalling collected packages: pytz, tzdata, pandas\\nSuccessfully installed pandas-2.3.3 pytz-2026.2 tzdata-2026.2\\nWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 10.23}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-18T11:32:25.919763+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "account": "root",
  "command": "cd /root/autodl-tmp/gen-depth-contamination && python3 scripts/exp027_bootstrap_ci.py 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "account": "root",
    "command": "cd /root/autodl-tmp/gen-depth-contamination && python3 scripts/exp027_bootstrap_ci.py 2>&1"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-18T11:32:25.920002+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cd /root/autodl-tmp/gen-depth-contamination && python3 scripts/exp027_bootstrap_ci.py 2>&1'\\n\\nStdout:\\n\\n/usr/local/lib/python3.10/dist-packages/sklearn/utils/validation.py:2749: UserWarning: X does not have valid feature names, but LGBMClassifier was fitted with feature names\\n  warnings.warn(\\n/usr/local/lib/python3.10/dist-packages/sklearn/utils/validation.py:2749: UserWarning: X does not have valid feature names, but LGBMClassifier was fitted with feature names\\n  warnings.warn(\\n/usr/local/lib/python3.10/dist-packages/sklearn/utils/validation.py:2749: UserWarning: X does not have valid feature names, but LGBMClassifier was fitted with feature names\\n  warnings.warn(\\n/usr/local/lib/python3.10/dist-packages/sklearn/utils/validation.py:2749: UserWarning: X does not have valid feature names, but LGBMClassifier was fitted with feature names\\n  warnings.warn(\\n/usr/local/lib/python3.10/dist-packages/sklearn/utils/validation.py:2749: UserWarning: X does not have valid feature names, but LGBMClassifier was fitted with feature names\\n  warnings.warn(\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-18T11:32:25.920243+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "account": "root",
  "command": "cd /root/autodl-tmp/gen-depth-contamination && nohup python3 scripts/exp027_bootstrap_ci.py > /tmp/exp027_bootstrap.log 2>&1 & echo \"PID=$!\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "account": "root",
    "command": "cd /root/autodl-tmp/gen-depth-contamination && nohup python3 scripts/exp027_bootstrap_ci.py > /tmp/exp027_bootstrap.log 2>&1 & echo \"PID=$!\""
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-18T11:32:25.920391+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cd /root/autodl-tmp/gen-depth-contamination && nohup python3 scripts/exp027_bootstrap_ci.py > /tmp/exp027_bootstrap.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=51173\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.68}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-18T11:32:25.920543+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "account": "root",
  "command": "ps aux | grep exp027 | grep -v grep",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "account": "root",
    "command": "ps aux | grep exp027 | grep -v grep",
    "warn": "True"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-18T11:32:25.920668+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -20 /tmp/exp027_bootstrap.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -20 /tmp/exp027_bootstrap.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-18T11:32:25.920835+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root      50945  0.0  0.0   4364  1448 ?        Ss   19:27   0:00 bash -c cd /root/autodl-tmp/gen-depth-contamination && python3 scripts/exp027_bootstrap_ci.py 2>&1\\nroot      50946  622  0.0 10155740 180336 ?     Rl   19:27   7:28 python3 scripts/exp027_bootstrap_ci.py\\nroot      51173  0.0  0.0   4364   240 ?        S    19:28   0:00 bash -c cd /root/autodl-tmp/gen-depth-contamination && nohup python3 scripts/exp027_bootstrap_ci.py > /tmp/exp027_bootstrap.log 2>&1 & echo \\\"PID=$!\\\"\\nroot      51174  761  0.0 10155248 173816 ?     Rl   19:28   4:34 python3 scripts/exp027_bootstrap_ci.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-18T11:32:25.921044+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/usr/local/lib/python3.10/dist-packages/sklearn/utils/validation.py:2749: UserWarning: X does not have valid feature names, but LGBMClassifier was fitted with feature names\\n  warnings.warn(\\n/usr/local/lib/python3.10/dist-packages/sklearn/utils/validation.py:2749: UserWarning: X does not have valid feature names, but LGBMClassifier was fitted with feature names\\n  warnings.warn(\\n/usr/local/lib/python3.10/dist-packages/sklearn/utils/validation.py:2749: UserWarning: X does not have valid feature names, but LGBMClassifier was fitted with feature names\\n  warnings.warn(\\n/usr/local/lib/python3.10/dist-packages/sklearn/utils/validation.py:2749: UserWarning: X does not have valid feature names, but LGBMClassifier was fitted with feature names\\n  warnings.warn(\\n/usr/local/lib/python3.10/dist-packages/sklearn/utils/validation.py:2749: UserWarning: X does not have valid feature names, but LGBMClassifier was fitted with feature names\\n  warnings.warn(\\n/usr/local/lib/python3.10/dist-packages/sklearn/utils/validation.py:2749: UserWarning: X does not have valid feature names, but LGBMClassifier was fitted with feature names\\n  warnings.warn(\\n/usr/local/lib/python3.10/dist-packages/sklearn/utils/validation.py:2749: UserWarning: X does not have valid feature names, but LGBMClassifier was fitted with feature names\\n  warnings.warn(\\n/usr/local/lib/python3.10/dist-packages/sklearn/utils/validation.py:2749: UserWarning: X does not have valid feature names, but LGBMClassifier was fitted with feature names\\n  warnings.warn(\\n/usr/local/lib/python3.10/dist-packages/sklearn/utils/validation.py:2749: UserWarning: X does not have valid feature names, but LGBMClassifier was fitted with feature names\\n  warnings.warn(\\n/usr/local/lib/python3.10/dist-packages/sklearn/utils/validation.py:2749: UserWarning: X does not have valid feature names, but LGBMClassifier was fitted with feature names\\n  warnings.warn(\\n\", 
…[truncated 100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-18T11:32:25.921234+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "account": "root",
  "command": "kill 50946 50945 51173 51174 2>/dev/null; sleep 1; ps aux | grep exp027 | grep -v grep || echo \"All killed\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "account": "root",
    "command": "kill 50946 50945 51173 51174 2>/dev/null; sleep 1; ps aux | grep exp027 | grep -v grep || echo \"All killed\""
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-18T11:32:25.921369+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"All killed\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.64}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-18T11:32:25.921511+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "account": "root",
  "command": "cat > /root/autodl-tmp/gen-depth-contamination/scripts/exp027_bootstrap_ci.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"exp_027 Bootstrap CI: doc-level bootstrap on OOF predictions + permutation test.\"\"\"\n\nimport json, time, warnings\nimport numpy as np\nimport pandas as pd\nimport lightgbm as lgb\nfrom pathlib import Path\nfrom sklearn.model_selection import GroupKFold\nfrom sklearn.metrics import roc_auc_score\n\nwarnings.filterwarnings(\"ignore\")\n\nDATA_DIR = Path(\"/root/autodl-tmp/gen-depth-contamination/data/exp_027_latex_ablation\")\nRESULTS_DIR = Path(\"/root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation\")\nN_BOOT = 10_000\nN_PERM = 1_000\nSEED = 42\nTHETA = 0.60\n\nLGB_PARAMS = dict(\n    n_estimators=200, max_depth=6, learning_rate=0.05,\n    num_leaves=31, verbose=-1, n_jobs=-1,\n)\n\n\ndef main():\n    t0 = time.time()\n    df = pd.read_csv(DATA_DIR / \"features.csv\")\n    feat_cols = [c for c in df.columns if c not in (\"doc_id\", \"depth\")]\n    print(f\"Data: {len(df)} rows, {len(feat_cols)} features, depths {sorted(df.depth.unique())}\", flush=True)\n\n    pairs = [\"0v1\", \"1v2\", \"2v3\", \"3v4\", \"4v5\"]\n    results = {}\n\n    for pair in pairs:\n        lo, hi = int(pair[0]), int(pair[2])\n        sub = df[df[\"depth\"].isin([lo, hi])].copy().reset_index(drop=True)\n        X = sub[feat_cols].values\n        y = (sub[\"depth\"] == hi).astype(int).values\n        doc_ids = sub[\"doc_id\"].values\n        unique_docs = np.unique(doc_ids)\n\n        print(f\"\\n--- {pair}: {len(sub)} samples, {len(unique_docs)} docs ---\", flush=True)\n\n        # Step 1: GroupKFold(5) OOF predictions\n        oof = np.zeros(len(X))\n        fold_aucs = []\n        gkf = GroupKFold(n_splits=5)\n        for fold_i, (tr, te) in enumerate(gkf.split(X, y, groups=doc_ids)):\n            clf = lgb.LGBMClassifier(**LGB_PARAMS)\n            clf.fit(X[tr], y[tr])\n            oof[te] = clf.predict_proba(X[te])[:, 1]\n            fold_aucs.append(roc_auc_score(y[te], oof[te]))\n\n        point_est = roc_auc_score(y, oof)\n        print(f\"  OOF AUC = {point_est:.4f}  folds={[round(a,4) for a in fold_aucs]}\", flush=True)\n\n        # Step 2: Doc-level bootstrap CI on OOF predictions\n        doc_to_idx = {d: np.where(doc_ids == d)[0] for d in unique_docs}\n        rng = np.random.RandomState(SEED)\n        boot_aucs = []\n        t1 = time.time()\n        for bi in range(N_BOOT):\n            bd = rng.choice(unique_docs, len(unique_docs), replace=True)\n            idx = np.concatenate([doc_to_idx[d] for d in bd])\n            yb, pb = y[idx], oof[idx]\n            if len(np.unique(yb)) < 2:\n                continue\n            boot_aucs.append(roc_auc_score(yb, pb))\n            if (bi + 1) % 2000 == 0:\n                print(f\"    bootstrap {bi+1}/{N_BOOT} ({time.time()-t1:.1f}s)\", flush=True)\n\n        ci_lo = float(np.percentile(boot_aucs, 2.5))\n        ci_hi = float(np.percentile(boot_aucs, 97.5))\n        print(f\"  CI95 = [{ci_lo:.4f}, {ci_hi:.4f}]  boot_mean={np.mean(boot_aucs):.4f}  ({len(boot_aucs)}/{N_BOOT} valid, {time.time()-t1:.1f}s)\", flush=True)\n\n        result = {\n            \"point_estimate\": round(point_est, 4),\n            \"boot_mean\": round(float(np.mean(boot_aucs)), 4),\n            \"ci_lower\": round(ci_lo, 4),\n            \"ci_upper\": round(ci_hi, 4),\n            \"per_fold\": [round(a, 4) for a in fold_aucs],\n            \"n_boot_valid\": len(boot_aucs),\n        }\n\n        # Step 3: Permutation test (2v3 only)\n        if pair == \"2v3\":\n            print(f\"  Permutation test ({N_PERM} perms)...\", flush=True)\n            rng_p = np.random.RandomState(SEED + 1)\n            perm_aucs = []\n            for pi in range(N_PERM):\n                y_perm = rng_p.permutation(y)\n                if len(np.unique(y_perm)) < 2:\n                    continue\n                perm_aucs.append(roc_auc_score(y_perm, oof))\n\n            p_val = float(np.mean([a >= point_est for a in perm_aucs]))\n            result[\"p_value\"] = round(p_val, 6)\n            result[\"perm_null_mean\"] = round(float(np.mean(perm_aucs)), 4)\n            result[\"perm_null_std\"] = round(float(np.std(perm_aucs)), 4)\n            result[\"n_perm\"] = len(perm_aucs)\n            print(f\"  Perm: p={p_val:.6f}  null={np.mean(perm_aucs):.4f}+/-{np.std(perm_aucs):.4f}\", flush=True)\n\n        results[pair] = result\n\n    # Summary\n    print(f\"\\n{'='*60}\", flush=True)\n    print(\"RESULTS SUMMARY\", flush=True)\n    print(f\"{'='*60}\", flush=True)\n    for pair, r in results.items():\n        s = f\"  {pair}: AUC={r['point_estimate']:.4f} [{r['ci_lower']:.4f}, {r['ci_upper']:.4f}]\"\n        if \"p_value\" in r:\n            s += f\"  p={r['p_value']:.6f}\"\n        s += f\"  ci_lo {'>' if r['ci_lower'] > THETA else '<='} theta={THETA}\"\n        print(s, flush=True)\n\n    r23 = results[\"2v3\"]\n    verdict = r23[\"ci_lower\"] > THETA\n    print(f\"\\n*** 2v3 CI lower = {r23['ci_lower']:.4f} {'>' if verdict else '<='} theta={THETA}\", flush=True)\n    print(f\"    -> {'CONFIRMED: signal above threshold' if verdict else 'BELOW threshold'}\", flush=True)\n    print(f\"\\nTotal: {time.time()-t0:.1f}s\", flush=True)\n\n    RESULTS_DIR.mkdir(parents=True, exist_ok=True)\n    out = RESULTS_DIR / \"bootstrap_ci_results.json\"\n    with open(out, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"Saved: {out}\", flush=True)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Updated.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "account": "root",
    "command": "cat > /root/autodl-tmp/gen-depth-contamination/scripts/exp027_bootstrap_ci.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"exp_027 Bootstrap CI: doc-level bootstrap on OOF predictions + permutation test.\"\"\"\n\nimport json, time, warnings\nimport numpy as np\nimport pandas as pd\nimport lightgbm as lgb\nfrom pathlib import Path\nfrom sklearn.model_selection import GroupKFold\nfrom sklearn.metrics import roc_auc_score\n\nwarnings.filterwarnings(\"ignore\")\n\nDATA_DIR = Path(\"/root/autodl-tmp/gen-depth-contamination/data/exp_027_latex_ablation\")\nRESULTS_DIR = Path(\"/root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation\")\nN_BOOT = 10_000\nN_PERM = 1_000\nSEED = 42\nTHETA = 0.60\n\nLGB_PARAMS = dict(\n    n_estimators=200, max_depth=6, learning_rate=0.05,\n    num_leaves=31, verbose=-1, n_jobs=-1,\n)\n\n\ndef main():\n    t0 = time.time()\n    df = pd.read_csv(DATA_DIR / \"features.csv\")\n    feat_cols = [c for c in df.columns if c not in (\"doc_id\", \"depth\")]\n    print(f\"Data: {len(df)} rows, {len(feat_cols)} features, depths {sorted(df.depth.unique())}\", flush=True)\n\n    pairs = [\"0v1\", \"1v2\", \"2v3\", \"3v4\", \"4v5\"]\n    results = {}\n\n    for pair in pairs:\n        lo, hi = int(pair[0]), int(pair[2])\n        sub = df[df[\"depth\"].isin([lo, hi])].copy().reset_index(drop=True)\n        X = sub[feat_cols].values\n        y = (sub[\"depth\"] == hi).astype(int).values\n        doc_ids = sub[\"doc_id\"].values\n        unique_docs = np.unique(doc_ids)\n\n        print(f\"\\n--- {pair}: {len(sub)} samples, {len(unique_docs)} docs ---\", flush=True)\n\n        # Step 1: GroupKFold(5) OOF predictions\n        oof = np.zeros(len(X))\n        fold_aucs = []\n        gkf = GroupKFold(n_splits=5)\n        for fold_i, (tr, te) in enumerate(gkf.split(X, y, groups=doc_ids)):\n            clf = lgb.LGBMClassifier(**LGB_PARAMS)\n            clf.fit(X[tr], y[tr])\n            oof[te] = clf.predict_proba(X[te])[:, 1]\n            fold_aucs.append(roc_auc_score(y[te], oof[te]))\n\n        point_est = roc_auc_score(y, oof)\n        print(f\"  OOF AUC = {point_est:.4f}  folds={[round(a,4) for a in fold_aucs]}\", flush=True)\n\n        # Step 2: Doc-level bootstrap CI on OOF predictions\n        doc_to_idx = {d: np.where(doc_ids == d)[0] for d in unique_docs}\n        rng = np.random.RandomState(SEED)\n        boot_aucs = []\n        t1 = time.time()\n        for bi in range(N_BOOT):\n            bd = rng.choice(unique_docs, len(unique_docs), replace=True)\n            idx = np.concatenate([doc_to_idx[d] for d in bd])\n            yb, pb = y[idx], oof[idx]\n            if len(np.unique(yb)) < 2:\n                continue\n            boot_aucs.append(roc_auc_score(yb, pb))\n            if (bi + 1) % 2000 == 0:\n                print(f\"    bootstrap {bi+1}/{N_BOOT} ({time.time()-t1:.1f}s)\", flush=True)\n\n        ci_lo = float(np.percentile(boot_aucs, 2.5))\n        ci_hi = float(np.percentile(boot_aucs, 97.5))\n        print(f\"  CI95 = [{ci_lo:.4f}, {ci_hi:.4f}]  boot_mean={np.mean(boot_aucs):.4f}  ({len(boot_aucs)}/{N_BOOT} valid, {time.time()-t1:.1f}s)\", flush=True)\n\n        result = {\n            \"point_estimate\": round(point_est, 4),\n            \"boot_mean\": round(float(np.mean(boot_aucs)), 4),\n            \"ci_lower\": round(ci_lo, 4),\n            \"ci_upper\": round(ci_hi, 4),\n            \"per_fold\": [round(a, 4) for a in fold_aucs],\n            \"n_boot_valid\": len(boot_aucs),\n        }\n\n        # Step 3: Permutation test (2v3 only)\n        if pair == \"2v3\":\n            print(f\"  Permutation test ({N_PERM} perms)...\", flush=True)\n            rng_p = np.random.RandomState(SEED + 1)\n            perm_aucs = []\n            for pi in range(N_PERM):\n                y_perm = rng_p.permutation(y)\n                if len(np.unique(y_perm)) < 2:\n                    continue\n                perm_aucs.append(roc_auc_score(y_perm, oof))\n\n            p_val = float(np.mean([a >= point_est for a in perm_aucs]))\n            result[\"p_value\"] = round(p_val, 6)\n            result[\"perm_null_mean\"] = round(float(np.mean(perm_aucs)), 4)\n            result[\"perm_null_std\"] = round(float(np.std(perm_aucs)), 4)\n            result[\"n_perm\"] = len(perm_aucs)\n            print(f\"  Perm: p={p_val:.6f}  null={np.mean(perm_aucs):.4f}+/-{np.std(perm_aucs):.4f}\", flush=True)\n\n        results[pair] = result\n\n    # Summary\n    print(f\"\\n{'='*60}\", flush=True)\n    print(\"RESULTS SUMMARY\", flush=True)\n    print(f\"{'='*60}\", flush=True)\n    for pair, r in results.items():\n        s = f\"  {pair}: AUC={r['point_estimate']:.4f} [{r['ci_lower']:.4f}, {r['ci_upper']:.4f}]\"\n        if \"p_value\" in r:\n            s += f\"  p={r['p_value']:.6f}\"\n        s += f\"  ci_lo {'>' if r['ci_lower'] > THETA else '<='} theta={THETA}\"\n        print(s, flush=True)\n\n    r23 = results[\"2v3\"]\n    verdict = r23[\"ci_lower\"] > THETA\n    print(f\"\\n*** 2v3 CI lower = {r23['ci_lower']:.4f} {'>' if verdict else '<='} theta={THETA}\", flush=True)\n    print(f\"    -> {'CONFIRMED: signal above threshold' if verdict else 'BELOW threshold'}\", flush=True)\n    print(f\"\\nTotal: {time.time()-t0:.1f}s\", flush=True)\n\n    RESULTS_DIR.mkdir(parents=True, exist_ok=True)\n    out = RESULTS_DIR / \"bootstrap_ci_results.json\"\n    with open(out, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"Saved: {out}\", flush=True)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Updated.\""
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-18T11:32:25.921687+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Updated.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-18T11:32:25.921853+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-22115",
  "account": "root",
  "command": "cd /root/autodl-tmp/gen-depth-contamination && nohup python3 -u scripts/exp027_bootstrap_ci.py > /tmp/exp027_bootstrap.log 2>&1 &\ndisown\necho \"STARTED\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-22115",
    "account": "root",
    "command": "cd /root/autodl-tmp/gen-depth-contamination && nohup python3 -u scripts/exp027_bootstrap_ci.py > /tmp/exp027_bootstrap.log 2>&1 &\ndisown\necho \"STARTED\""
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-18T11:32:25.922032+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cd /root/autodl-tmp/gen-depth-contamination && nohup python3 -u scripts/exp027_bootstrap_ci.py > /tmp/exp027_bootstrap.log 2>&1 &\\\\ndisown\\\\necho \\\"STARTED\\\"'\\n\\nStdout:\\n\\nSTARTED\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-18T11:32:25.922188+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -30 /tmp/exp027_bootstrap.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -30 /tmp/exp027_bootstrap.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-18T11:32:25.922323+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Data: 13200 rows, 15 features, depths [np.int64(0), np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5)]\\n\\n--- 0v1: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.9944  folds=[0.9912, 0.9978, 0.9934, 0.9976, 0.994]\\n    bootstrap 2000/10000 (4.5s)\\n    bootstrap 4000/10000 (8.7s)\\n    bootstrap 6000/10000 (13.1s)\\n    bootstrap 8000/10000 (16.7s)\\n    bootstrap 10000/10000 (20.3s)\\n  CI95 = [0.9925, 0.9960]  boot_mean=0.9944  (10000/10000 valid, 20.3s)\\n\\n--- 1v2: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.8315  folds=[0.8125, 0.8563, 0.8227, 0.8285, 0.8373]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (7.1s)\\n    bootstrap 6000/10000 (10.6s)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.77}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-18T11:32:25.922462+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "sleep 120 && echo \"done waiting\"",
  "description": "Wait 2 minutes for bootstrap to complete",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Bash",
  "tool_args": {
    "command": "sleep 120 && echo \"done waiting\"",
    "description": "Wait 2 minutes for bootstrap to complete",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-18T11:32:25.922587+00:00_

Command running in background with ID: bg1avxqdz. Output is being written to: /tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/0eb0119c-751b-4ee4-862f-7c124e4aa0a0/tasks/bg1avxqdz.output

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-18T11:32:25.922709+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -40 /tmp/exp027_bootstrap.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -40 /tmp/exp027_bootstrap.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-18T11:32:25.922868+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Data: 13200 rows, 15 features, depths [np.int64(0), np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5)]\\n\\n--- 0v1: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.9944  folds=[0.9912, 0.9978, 0.9934, 0.9976, 0.994]\\n    bootstrap 2000/10000 (4.5s)\\n    bootstrap 4000/10000 (8.7s)\\n    bootstrap 6000/10000 (13.1s)\\n    bootstrap 8000/10000 (16.7s)\\n    bootstrap 10000/10000 (20.3s)\\n  CI95 = [0.9925, 0.9960]  boot_mean=0.9944  (10000/10000 valid, 20.3s)\\n\\n--- 1v2: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.8315  folds=[0.8125, 0.8563, 0.8227, 0.8285, 0.8373]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (7.1s)\\n    bootstrap 6000/10000 (10.6s)\\n    bootstrap 8000/10000 (14.1s)\\n    bootstrap 10000/10000 (17.6s)\\n  CI95 = [0.8205, 0.8426]  boot_mean=0.8316  (10000/10000 valid, 17.6s)\\n\\n--- 2v3: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.6248  folds=[0.6512, 0.6178, 0.6157, 0.6054, 0.6351]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.92}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-18T11:32:25.923023+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -50 /tmp/exp027_bootstrap.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -50 /tmp/exp027_bootstrap.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-18T11:32:25.923170+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Data: 13200 rows, 15 features, depths [np.int64(0), np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5)]\\n\\n--- 0v1: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.9944  folds=[0.9912, 0.9978, 0.9934, 0.9976, 0.994]\\n    bootstrap 2000/10000 (4.5s)\\n    bootstrap 4000/10000 (8.7s)\\n    bootstrap 6000/10000 (13.1s)\\n    bootstrap 8000/10000 (16.7s)\\n    bootstrap 10000/10000 (20.3s)\\n  CI95 = [0.9925, 0.9960]  boot_mean=0.9944  (10000/10000 valid, 20.3s)\\n\\n--- 1v2: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.8315  folds=[0.8125, 0.8563, 0.8227, 0.8285, 0.8373]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (7.1s)\\n    bootstrap 6000/10000 (10.6s)\\n    bootstrap 8000/10000 (14.1s)\\n    bootstrap 10000/10000 (17.6s)\\n  CI95 = [0.8205, 0.8426]  boot_mean=0.8316  (10000/10000 valid, 17.6s)\\n\\n--- 2v3: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.6248  folds=[0.6512, 0.6178, 0.6157, 0.6054, 0.6351]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (6.9s)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-18T11:32:25.923338+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -30 /tmp/exp027_bootstrap.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -30 /tmp/exp027_bootstrap.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-18T11:32:25.923489+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Data: 13200 rows, 15 features, depths [np.int64(0), np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5)]\\n\\n--- 0v1: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.9944  folds=[0.9912, 0.9978, 0.9934, 0.9976, 0.994]\\n    bootstrap 2000/10000 (4.5s)\\n    bootstrap 4000/10000 (8.7s)\\n    bootstrap 6000/10000 (13.1s)\\n    bootstrap 8000/10000 (16.7s)\\n    bootstrap 10000/10000 (20.3s)\\n  CI95 = [0.9925, 0.9960]  boot_mean=0.9944  (10000/10000 valid, 20.3s)\\n\\n--- 1v2: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.8315  folds=[0.8125, 0.8563, 0.8227, 0.8285, 0.8373]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (7.1s)\\n    bootstrap 6000/10000 (10.6s)\\n    bootstrap 8000/10000 (14.1s)\\n    bootstrap 10000/10000 (17.6s)\\n  CI95 = [0.8205, 0.8426]  boot_mean=0.8316  (10000/10000 valid, 17.6s)\\n\\n--- 2v3: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.6248  folds=[0.6512, 0.6178, 0.6157, 0.6054, 0.6351]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (6.9s)\\n    bootstrap 6000/10000 (10.3s)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-18T11:32:25.923621+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -20 /tmp/exp027_bootstrap.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -20 /tmp/exp027_bootstrap.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-18T11:32:25.923752+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    bootstrap 6000/10000 (13.1s)\\n    bootstrap 8000/10000 (16.7s)\\n    bootstrap 10000/10000 (20.3s)\\n  CI95 = [0.9925, 0.9960]  boot_mean=0.9944  (10000/10000 valid, 20.3s)\\n\\n--- 1v2: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.8315  folds=[0.8125, 0.8563, 0.8227, 0.8285, 0.8373]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (7.1s)\\n    bootstrap 6000/10000 (10.6s)\\n    bootstrap 8000/10000 (14.1s)\\n    bootstrap 10000/10000 (17.6s)\\n  CI95 = [0.8205, 0.8426]  boot_mean=0.8316  (10000/10000 valid, 17.6s)\\n\\n--- 2v3: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.6248  folds=[0.6512, 0.6178, 0.6157, 0.6054, 0.6351]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (6.9s)\\n    bootstrap 6000/10000 (10.3s)\\n    bootstrap 8000/10000 (13.7s)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-18T11:32:25.923908+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -15 /tmp/exp027_bootstrap.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -15 /tmp/exp027_bootstrap.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-18T11:32:25.924036+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    bootstrap 10000/10000 (17.6s)\\n  CI95 = [0.8205, 0.8426]  boot_mean=0.8316  (10000/10000 valid, 17.6s)\\n\\n--- 2v3: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.6248  folds=[0.6512, 0.6178, 0.6157, 0.6054, 0.6351]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (6.9s)\\n    bootstrap 6000/10000 (10.3s)\\n    bootstrap 8000/10000 (13.7s)\\n    bootstrap 10000/10000 (17.2s)\\n  CI95 = [0.6098, 0.6402]  boot_mean=0.6248  (10000/10000 valid, 17.2s)\\n  Permutation test (1000 perms)...\\n  Perm: p=0.000000  null=0.5000+/-0.0087\\n\\n--- 3v4: 4400 samples, 2200 docs ---\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-18T11:32:25.924183+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -30 /tmp/exp027_bootstrap.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -30 /tmp/exp027_bootstrap.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-18T11:32:25.924319+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    bootstrap 2000/10000 (4.5s)\\n    bootstrap 4000/10000 (8.7s)\\n    bootstrap 6000/10000 (13.1s)\\n    bootstrap 8000/10000 (16.7s)\\n    bootstrap 10000/10000 (20.3s)\\n  CI95 = [0.9925, 0.9960]  boot_mean=0.9944  (10000/10000 valid, 20.3s)\\n\\n--- 1v2: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.8315  folds=[0.8125, 0.8563, 0.8227, 0.8285, 0.8373]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (7.1s)\\n    bootstrap 6000/10000 (10.6s)\\n    bootstrap 8000/10000 (14.1s)\\n    bootstrap 10000/10000 (17.6s)\\n  CI95 = [0.8205, 0.8426]  boot_mean=0.8316  (10000/10000 valid, 17.6s)\\n\\n--- 2v3: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.6248  folds=[0.6512, 0.6178, 0.6157, 0.6054, 0.6351]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (6.9s)\\n    bootstrap 6000/10000 (10.3s)\\n    bootstrap 8000/10000 (13.7s)\\n    bootstrap 10000/10000 (17.2s)\\n  CI95 = [0.6098, 0.6402]  boot_mean=0.6248  (10000/10000 valid, 17.2s)\\n  Permutation test (1000 perms)...\\n  Perm: p=0.000000  null=0.5000+/-0.0087\\n\\n--- 3v4: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.5440  folds=[0.5501, 0.5691, 0.5507, 0.5379, 0.5131]\\n    bootstrap 2000/10000 (3.5s)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-18T11:32:25.924444+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -20 /tmp/exp027_bootstrap.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -20 /tmp/exp027_bootstrap.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-18T11:32:25.924571+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    bootstrap 6000/10000 (10.6s)\\n    bootstrap 8000/10000 (14.1s)\\n    bootstrap 10000/10000 (17.6s)\\n  CI95 = [0.8205, 0.8426]  boot_mean=0.8316  (10000/10000 valid, 17.6s)\\n\\n--- 2v3: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.6248  folds=[0.6512, 0.6178, 0.6157, 0.6054, 0.6351]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (6.9s)\\n    bootstrap 6000/10000 (10.3s)\\n    bootstrap 8000/10000 (13.7s)\\n    bootstrap 10000/10000 (17.2s)\\n  CI95 = [0.6098, 0.6402]  boot_mean=0.6248  (10000/10000 valid, 17.2s)\\n  Permutation test (1000 perms)...\\n  Perm: p=0.000000  null=0.5000+/-0.0087\\n\\n--- 3v4: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.5440  folds=[0.5501, 0.5691, 0.5507, 0.5379, 0.5131]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (7.0s)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-18T11:32:25.924693+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -25 /tmp/exp027_bootstrap.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -25 /tmp/exp027_bootstrap.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-18T11:32:25.924849+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"--- 1v2: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.8315  folds=[0.8125, 0.8563, 0.8227, 0.8285, 0.8373]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (7.1s)\\n    bootstrap 6000/10000 (10.6s)\\n    bootstrap 8000/10000 (14.1s)\\n    bootstrap 10000/10000 (17.6s)\\n  CI95 = [0.8205, 0.8426]  boot_mean=0.8316  (10000/10000 valid, 17.6s)\\n\\n--- 2v3: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.6248  folds=[0.6512, 0.6178, 0.6157, 0.6054, 0.6351]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (6.9s)\\n    bootstrap 6000/10000 (10.3s)\\n    bootstrap 8000/10000 (13.7s)\\n    bootstrap 10000/10000 (17.2s)\\n  CI95 = [0.6098, 0.6402]  boot_mean=0.6248  (10000/10000 valid, 17.2s)\\n  Permutation test (1000 perms)...\\n  Perm: p=0.000000  null=0.5000+/-0.0087\\n\\n--- 3v4: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.5440  folds=[0.5501, 0.5691, 0.5507, 0.5379, 0.5131]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (7.0s)\\n    bootstrap 6000/10000 (10.5s)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-18T11:32:25.924983+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -15 /tmp/exp027_bootstrap.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -15 /tmp/exp027_bootstrap.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-18T11:32:25.925111+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (6.9s)\\n    bootstrap 6000/10000 (10.3s)\\n    bootstrap 8000/10000 (13.7s)\\n    bootstrap 10000/10000 (17.2s)\\n  CI95 = [0.6098, 0.6402]  boot_mean=0.6248  (10000/10000 valid, 17.2s)\\n  Permutation test (1000 perms)...\\n  Perm: p=0.000000  null=0.5000+/-0.0087\\n\\n--- 3v4: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.5440  folds=[0.5501, 0.5691, 0.5507, 0.5379, 0.5131]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (7.0s)\\n    bootstrap 6000/10000 (10.5s)\\n    bootstrap 8000/10000 (13.9s)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-18T11:32:25.925232+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -20 /tmp/exp027_bootstrap.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -20 /tmp/exp027_bootstrap.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-18T11:32:25.925359+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  OOF AUC = 0.6248  folds=[0.6512, 0.6178, 0.6157, 0.6054, 0.6351]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (6.9s)\\n    bootstrap 6000/10000 (10.3s)\\n    bootstrap 8000/10000 (13.7s)\\n    bootstrap 10000/10000 (17.2s)\\n  CI95 = [0.6098, 0.6402]  boot_mean=0.6248  (10000/10000 valid, 17.2s)\\n  Permutation test (1000 perms)...\\n  Perm: p=0.000000  null=0.5000+/-0.0087\\n\\n--- 3v4: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.5440  folds=[0.5501, 0.5691, 0.5507, 0.5379, 0.5131]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (7.0s)\\n    bootstrap 6000/10000 (10.5s)\\n    bootstrap 8000/10000 (13.9s)\\n    bootstrap 10000/10000 (17.5s)\\n  CI95 = [0.5277, 0.5598]  boot_mean=0.5439  (10000/10000 valid, 17.5s)\\n\\n--- 4v5: 4400 samples, 2200 docs ---\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-18T11:32:25.925501+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -25 /tmp/exp027_bootstrap.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -25 /tmp/exp027_bootstrap.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-18T11:32:25.925634+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n--- 2v3: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.6248  folds=[0.6512, 0.6178, 0.6157, 0.6054, 0.6351]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (6.9s)\\n    bootstrap 6000/10000 (10.3s)\\n    bootstrap 8000/10000 (13.7s)\\n    bootstrap 10000/10000 (17.2s)\\n  CI95 = [0.6098, 0.6402]  boot_mean=0.6248  (10000/10000 valid, 17.2s)\\n  Permutation test (1000 perms)...\\n  Perm: p=0.000000  null=0.5000+/-0.0087\\n\\n--- 3v4: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.5440  folds=[0.5501, 0.5691, 0.5507, 0.5379, 0.5131]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (7.0s)\\n    bootstrap 6000/10000 (10.5s)\\n    bootstrap 8000/10000 (13.9s)\\n    bootstrap 10000/10000 (17.5s)\\n  CI95 = [0.5277, 0.5598]  boot_mean=0.5439  (10000/10000 valid, 17.5s)\\n\\n--- 4v5: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.5425  folds=[0.5253, 0.5664, 0.547, 0.5423, 0.5292]\\n    bootstrap 2000/10000 (3.4s)\\n    bootstrap 4000/10000 (6.8s)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-18T11:32:25.925760+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -20 /tmp/exp027_bootstrap.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -20 /tmp/exp027_bootstrap.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-18T11:32:25.925986+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    bootstrap 6000/10000 (10.3s)\\n    bootstrap 8000/10000 (13.7s)\\n    bootstrap 10000/10000 (17.2s)\\n  CI95 = [0.6098, 0.6402]  boot_mean=0.6248  (10000/10000 valid, 17.2s)\\n  Permutation test (1000 perms)...\\n  Perm: p=0.000000  null=0.5000+/-0.0087\\n\\n--- 3v4: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.5440  folds=[0.5501, 0.5691, 0.5507, 0.5379, 0.5131]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (7.0s)\\n    bootstrap 6000/10000 (10.5s)\\n    bootstrap 8000/10000 (13.9s)\\n    bootstrap 10000/10000 (17.5s)\\n  CI95 = [0.5277, 0.5598]  boot_mean=0.5439  (10000/10000 valid, 17.5s)\\n\\n--- 4v5: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.5425  folds=[0.5253, 0.5664, 0.547, 0.5423, 0.5292]\\n    bootstrap 2000/10000 (3.4s)\\n    bootstrap 4000/10000 (6.8s)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-18T11:32:25.926132+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -15 /tmp/exp027_bootstrap.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -15 /tmp/exp027_bootstrap.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-18T11:32:25.926279+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"--- 3v4: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.5440  folds=[0.5501, 0.5691, 0.5507, 0.5379, 0.5131]\\n    bootstrap 2000/10000 (3.5s)\\n    bootstrap 4000/10000 (7.0s)\\n    bootstrap 6000/10000 (10.5s)\\n    bootstrap 8000/10000 (13.9s)\\n    bootstrap 10000/10000 (17.5s)\\n  CI95 = [0.5277, 0.5598]  boot_mean=0.5439  (10000/10000 valid, 17.5s)\\n\\n--- 4v5: 4400 samples, 2200 docs ---\\n  OOF AUC = 0.5425  folds=[0.5253, 0.5664, 0.547, 0.5423, 0.5292]\\n    bootstrap 2000/10000 (3.4s)\\n    bootstrap 4000/10000 (6.8s)\\n    bootstrap 6000/10000 (10.3s)\\n    bootstrap 8000/10000 (13.8s)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.65}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-18T11:32:25.926406+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "tail -20 /tmp/exp027_bootstrap.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "tail -20 /tmp/exp027_bootstrap.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-18T11:32:25.926537+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    bootstrap 4000/10000 (6.8s)\\n    bootstrap 6000/10000 (10.3s)\\n    bootstrap 8000/10000 (13.8s)\\n    bootstrap 10000/10000 (17.3s)\\n  CI95 = [0.5265, 0.5584]  boot_mean=0.5425  (10000/10000 valid, 17.3s)\\n\\n============================================================\\nRESULTS SUMMARY\\n============================================================\\n  0v1: AUC=0.9944 [0.9925, 0.9960]  ci_lo > theta=0.6\\n  1v2: AUC=0.8315 [0.8205, 0.8426]  ci_lo > theta=0.6\\n  2v3: AUC=0.6248 [0.6098, 0.6402]  p=0.000000  ci_lo > theta=0.6\\n  3v4: AUC=0.5440 [0.5277, 0.5598]  ci_lo <= theta=0.6\\n  4v5: AUC=0.5425 [0.5265, 0.5584]  ci_lo <= theta=0.6\\n\\n*** 2v3 CI lower = 0.6098 > theta=0.6\\n    -> CONFIRMED: signal above threshold\\n\\nTotal: 98.1s\\nSaved: /root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/bootstrap_ci_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-18T11:32:25.926674+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-22115",
  "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/bootstrap_ci_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-22115",
    "command": "cat /root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/bootstrap_ci_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-18T11:32:25.926848+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"0v1\\\": {\\n    \\\"point_estimate\\\": 0.9944,\\n    \\\"boot_mean\\\": 0.9944,\\n    \\\"ci_lower\\\": 0.9925,\\n    \\\"ci_upper\\\": 0.996,\\n    \\\"per_fold\\\": [\\n      0.9912,\\n      0.9978,\\n      0.9934,\\n      0.9976,\\n      0.994\\n    ],\\n    \\\"n_boot_valid\\\": 10000\\n  },\\n  \\\"1v2\\\": {\\n    \\\"point_estimate\\\": 0.8315,\\n    \\\"boot_mean\\\": 0.8316,\\n    \\\"ci_lower\\\": 0.8205,\\n    \\\"ci_upper\\\": 0.8426,\\n    \\\"per_fold\\\": [\\n      0.8125,\\n      0.8563,\\n      0.8227,\\n      0.8285,\\n      0.8373\\n    ],\\n    \\\"n_boot_valid\\\": 10000\\n  },\\n  \\\"2v3\\\": {\\n    \\\"point_estimate\\\": 0.6248,\\n    \\\"boot_mean\\\": 0.6248,\\n    \\\"ci_lower\\\": 0.6098,\\n    \\\"ci_upper\\\": 0.6402,\\n    \\\"per_fold\\\": [\\n      0.6512,\\n      0.6178,\\n      0.6157,\\n      0.6054,\\n      0.6351\\n    ],\\n    \\\"n_boot_valid\\\": 10000,\\n    \\\"p_value\\\": 0.0,\\n    \\\"perm_null_mean\\\": 0.5,\\n    \\\"perm_null_std\\\": 0.0087,\\n    \\\"n_perm\\\": 1000\\n  },\\n  \\\"3v4\\\": {\\n    \\\"point_estimate\\\": 0.544,\\n    \\\"boot_mean\\\": 0.5439,\\n    \\\"ci_lower\\\": 0.5277,\\n    \\\"ci_upper\\\": 0.5598,\\n    \\\"per_fold\\\": [\\n      0.5501,\\n      0.5691,\\n      0.5507,\\n      0.5379,\\n      0.5131\\n    ],\\n    \\\"n_boot_valid\\\": 10000\\n  },\\n  \\\"4v5\\\": {\\n    \\\"point_estimate\\\": 0.5425,\\n    \\\"boot_mean\\\": 0.5425,\\n    \\\"ci_lower\\\": 0.5265,\\n    \\\"ci_upper\\\": 0.5584,\\n    \\\"per_fold\\\": [\\n      0.5253,\\n      0.5664,\\n      0.547,\\n      0.5423,\\n      0.5292\\n    ],\\n    \\\"n_boot_valid\\\": 10000\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-18T11:32:25.927012+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp_027_bootstrap_ci",
  "description": "Create artifact directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp_027_bootstrap_ci",
    "description": "Create artifact directory"
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-18T11:32:25.927138+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-18T11:32:25.927276+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp_027_bootstrap_ci/results_summary.md",
  "content": "# exp_027 Bootstrap CI Results (LaTeX Ablation)\n\n## Method\n- **Data**: exp_027_latex_ablation features.csv (13,200 rows, 15 features, depths 0-5)\n- **Classifier**: LightGBM (200 trees, max_depth=6, lr=0.05)\n- **OOF**: GroupKFold(5), grouped by doc_id\n- **Bootstrap**: 10,000 doc-level resamples on OOF predictions, percentile CI\n- **Permutation test** (2v3 only): 1,000 label permutations against fixed OOF predictions\n\n## Results\n\n| Pair | Point Est | CI Lower | CI Upper | Per-fold AUCs | CI lower > 0.60? |\n|------|-----------|----------|----------|---------------|-------------------|\n| 0v1  | 0.9944    | 0.9925   | 0.9960   | 0.9912, 0.9978, 0.9934, 0.9976, 0.9940 | Yes |\n| 1v2  | 0.8315    | 0.8205   | 0.8426   | 0.8125, 0.8563, 0.8227, 0.8285, 0.8373 | Yes |\n| **2v3** | **0.6248** | **0.6098** | **0.6402** | 0.6512, 0.6178, 0.6157, 0.6054, 0.6351 | **Yes** |\n| 3v4  | 0.5440    | 0.5277   | 0.5598   | 0.5501, 0.5691, 0.5507, 0.5379, 0.5131 | No |\n| 4v5  | 0.5425    | 0.5265   | 0.5584   | 0.5253, 0.5664, 0.5470, 0.5423, 0.5292 | No |\n\n## 2v3 Permutation Test\n- p-value: 0.000 (0/1000 permutations exceeded observed AUC)\n- Null distribution: mean=0.5000, std=0.0087\n\n## Conclusion\n**2v3 CI lower = 0.6098 > theta = 0.60: CONFIRMED.**\n\nK*=3 holds under bootstrap CI even after LaTeX removal. The 2v3 signal is statistically significant (p < 0.001) and the 95% CI lower bound clears the theta=0.60 threshold, though with only 0.0098 margin. The drop from the original 0.6436 to 0.6248 is notable but does not invalidate the K*=3 finding.\n\n## Artifacts\n- Server JSON: `/root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/bootstrap_ci_results.json`\n- Script: `/root/autodl-tmp/gen-depth-contamination/scripts/exp027_bootstrap_ci.py`\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp_027_bootstrap_ci/results_summary.md",
    "content": "# exp_027 Bootstrap CI Results (LaTeX Ablation)\n\n## Method\n- **Data**: exp_027_latex_ablation features.csv (13,200 rows, 15 features, depths 0-5)\n- **Classifier**: LightGBM (200 trees, max_depth=6, lr=0.05)\n- **OOF**: GroupKFold(5), grouped by doc_id\n- **Bootstrap**: 10,000 doc-level resamples on OOF predictions, percentile CI\n- **Permutation test** (2v3 only): 1,000 label permutations against fixed OOF predictions\n\n## Results\n\n| Pair | Point Est | CI Lower | CI Upper | Per-fold AUCs | CI lower > 0.60? |\n|------|-----------|----------|----------|---------------|-------------------|\n| 0v1  | 0.9944    | 0.9925   | 0.9960   | 0.9912, 0.9978, 0.9934, 0.9976, 0.9940 | Yes |\n| 1v2  | 0.8315    | 0.8205   | 0.8426   | 0.8125, 0.8563, 0.8227, 0.8285, 0.8373 | Yes |\n| **2v3** | **0.6248** | **0.6098** | **0.6402** | 0.6512, 0.6178, 0.6157, 0.6054, 0.6351 | **Yes** |\n| 3v4  | 0.5440    | 0.5277   | 0.5598   | 0.5501, 0.5691, 0.5507, 0.5379, 0.5131 | No |\n| 4v5  | 0.5425    | 0.5265   | 0.5584   | 0.5253, 0.5664, 0.5470, 0.5423, 0.5292 | No |\n\n## 2v3 Permutation Test\n- p-value: 0.000 (0/1000 permutations exceeded observed AUC)\n- Null distribution: mean=0.5000, std=0.0087\n\n## Conclusion\n**2v3 CI lower = 0.6098 > theta = 0.60: CONFIRMED.**\n\nK*=3 holds under bootstrap CI even after LaTeX removal. The 2v3 signal is statistically significant (p < 0.001) and the 95% CI lower bound clears the theta=0.60 threshold, though with only 0.0098 margin. The drop from the original 0.6436 to 0.6248 is notable but does not invalidate the K*=3 finding.\n\n## Artifacts\n- Server JSON: `/root/autodl-tmp/gen-depth-contamination/results/exp_027_latex_ablation/bootstrap_ci_results.json`\n- Script: `/root/autodl-tmp/gen-depth-contamination/scripts/exp027_bootstrap_ci.py`\n"
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-18T11:32:25.927440+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp_027_bootstrap_ci/results_summary.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 121 · 2026-05-18T11:32:25.927607+00:00_

完成。结果：

**2v3 CI lower = 0.6098 > θ = 0.60: CONFIRMED.** K*=3 在去除 LaTeX 后依然成立。

| Pair | AUC | 95% CI | > θ? |
|------|-----|--------|------|
| 0v1 | 0.9944 | [0.9925, 0.9960] | Yes |
| 1v2 | 0.8315 | [0.8205, 0.8426] | Yes |
| **2v3** | **0.6248** | **[0.6098, 0.6402]** | **Yes** |
| 3v4 | 0.5440 | [0.5277, 0.5598] | No |
| 4v5 | 0.5425 | [0.5265, 0.5584] | No |

2v3 permutation test p=0.000 (null mean=0.50). CI lower bound 超过阈值 0.0098，margin 很小但统计上成立。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149"
}
```

</details>

---

### Assistant

_source line 122 · 2026-05-18T11:32:25.927819+00:00_

(Background wait task completed — bootstrap already finished before it, results reported above.)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_exp027-bootstrap-ci_20260518T112149"
}
```

</details>

---
