# analysis phase2 gitem consistency check

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 73
- **Recorded user turns:** 0
- **Tool calls:** 36
- **Original source:** `logs/chats/worker_analysis_phase2_gitem_consistency_check_20260521T230320.jsonl`
- **Structured JSON:** [`7edcbcbe32b138ef9de0.json`](../../sessions/7e/7edcbcbe32b138ef9de0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

73 recorded events

### Tool call

_source line 1 · 2026-05-21T23:10:45.913982+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read facet structures from both scripts",
  "subagent_type": "Explore",
  "prompt": "I need to compare the facet structures used in two G-study implementations for a research project.\n\nRead these files in full:\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp002_analysis/per_benchmark_gstudy.py` - the 4-model G-study script\n2. `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/compute_g_coefficients.py` - possibly used by 8-model FF worker\n\nFor each file, I need to know:\n- What facets are used in the G-study (e.g., model, item, ordering, precision)?\n- How is G_item computed? What goes into σ²(item) and σ²(δ)?\n- How is the data structured (what columns, what scoring)?\n- Henderson Type I method details\n\nAlso check if there are any files in `scripts/` that contain \"exp004\" or \"8model\" or \"ff\" that might be the actual 8-model script.\n\nSearch broadly - check `scripts/` directory structure first."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Agent",
  "tool_args": {
    "description": "Read facet structures from both scripts",
    "subagent_type": "Explore",
    "prompt": "I need to compare the facet structures used in two G-study implementations for a research project.\n\nRead these files in full:\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp002_analysis/per_benchmark_gstudy.py` - the 4-model G-study script\n2. `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/compute_g_coefficients.py` - possibly used by 8-model FF worker\n\nFor each file, I need to know:\n- What facets are used in the G-study (e.g., model, item, ordering, precision)?\n- How is G_item computed? What goes into σ²(item) and σ²(δ)?\n- How is the data structured (what columns, what scoring)?\n- Henderson Type I method details\n\nAlso check if there are any files in `scripts/` that contain \"exp004\" or \"8model\" or \"ff\" that might be the actual 8-model script.\n\nSearch broadly - check `scripts/` directory structure first."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-21T23:10:45.914316+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts -type f -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts -type f -name \"*.py\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-21T23:10:45.914517+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/sample_benchmarks.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp002_analysis/cross_benchmark_dstudy.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp002_analysis/gsm8k_answer_reextract.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp002_analysis/per_benchmark_gstudy.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp002_analysis/leave_one_benchmark_out.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp002_analysis/within_format_gradient.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp002_analysis/gradient_permutation_test.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/gstudy_full.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp001_analysis/dstudy_henderson_i.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/model_as_fixed_gstudy.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp004_defensive_analyses.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T23:10:45.914668+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts -type f -name \"*exp004*\" -o -name \"*8model*\" -o -name \"*ff*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts -type f -name \"*exp004*\" -o -name \"*8model*\" -o -name \"*ff*\""
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T23:10:45.914794+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp004_defensive_analyses.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T23:10:45.914922+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory -type f -name \"*compute*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory -type f -name \"*compute*\""
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T23:10:45.915039+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/logs/workers/worker_fix_qwen_accuracy_recompute_20260521T074236.log
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/logs/workers/worker_fix_qwen_accuracy_recompute_20260521T074236_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/scipy/special/tests/__pycache__/test_precompute_expn_asy.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/scipy/special/tests/__pycache__/test_precompute_utils.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/scipy/special/tests/__pycache__/test_precompute_gammainc.cpython-314.pyc
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/scipy/special/tests/test_precompute_expn_asy.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/scipy/special/tests/test_precompute_utils.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/scipy/special/tests/test_precompute_gammainc.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T23:10:45.915177+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory -type f -name \"compute_g*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory -type f -name \"compute_g*\""
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T23:10:45.915291+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T23:10:45.915423+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp002_analysis/per_benchmark_gstudy.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp002_analysis/per_benchmark_gstudy.py"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T23:10:45.915595+00:00_

1	"""Per-benchmark Henderson I variance decomposition for exp-002.
2	
3	Input:  Merged exp-002 JSONL (4 models x 4 benchmarks x bf16 x 2 temps x 6 prompts x 6 seeds x 4 orderings).
4	Output: results/analysis/exp002_per_benchmark_gstudy.json
5	        — per-benchmark variance components, G_item, D-study projections.
6	
7	Facets (7, within each benchmark):
8	  model, temperature, prompt_template, seed, ordering, item_id
9	  + all 2-way interactions. Residual absorbs >=3-way.
10	
11	Usage:
12	  python scripts/exp002_analysis/per_benchmark_gstudy.py --data-dir results/exp002
13	"""
14	
15	import argparse
16	import json
17	import sys
18	import time
19	from itertools import combinations
20	from math import prod
21	from pathlib import Path
22	
23	import numpy as np
24	import pandas as pd
25	
26	sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
27	from src.config.model_paths import normalize_model_name
28	
29	FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
30	BENCHMARKS = ["mmlu", "gsm8k", "arc", "hellaswag"]
31	
32	
33	def load_exp002_data(data_dir: str) -> pd.DataFrame:
34	    data_path = Path(data_dir)
35	    jsonl_files = sorted(data_path.glob("*.jsonl"))
36	    if not jsonl_files:
37	        raise FileNotFoundError(f"No JSONL files in {data_dir}")
38	    frames = [pd.read_json(f, lines=True) for f in jsonl_files]
39	    df = pd.concat(frames, ignore_index=True)
40	    if "top_logprobs" in df.columns:
41	        df.drop(columns=["top_logprobs"], inplace=True)
42	    df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
43	    for f in FACETS:
44	        df[f] = df[f].astype(str)
45	    return df
46	
47	
48	def compute_henderson_i(df: pd.DataFrame, response: str, facets: list[str]):
49	    """Henderson Method I: SS -> EMS -> variance components."""
50	    grand_mean = df[response].mean()
51	    N = len(df)
52	    n_levels = {f: df[f].nunique() for f in facets}
53	
54	    effects = {}
55	
56	    for f in fac
…[truncated 9883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T23:10:45.915748+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp004_defensive_analyses.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp004_defensive_analyses.py"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T23:10:45.915955+00:00_

1	#!/usr/bin/env python3
2	"""Phase 2 defensive analyses: Bernoulli baseline + MMLU subsampling + LOBO stability.
3	
4	Produces: results/exp004_8model_analysis/defensive_analyses.json
5	
6	Usage:
7	  source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
8	  export PYTHONPATH=/root/nlp_variance_gtheory:$PYTHONPATH
9	  cd /root/nlp_variance_gtheory
10	  python scripts/exp004_defensive_analyses.py
11	"""
12	
13	import json
14	import sys
15	import time
16	from itertools import combinations
17	from math import prod
18	from pathlib import Path
19	
20	import numpy as np
21	import pandas as pd
22	
23	sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
24	from src.config.model_paths import normalize_model_name
25	
26	FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
27	DATA_DIR = Path("results/exp002")
28	OUTPUT_DIR = Path("results/exp004_8model_analysis")
29	
30	BENCHMARK_FILES = {
31	    "mmlu": ["llama_mmlu", "mistral_mmlu", "gemma_mmlu", "qwen_mmlu",
32	             "internlm_mmlu", "deepseek_mmlu", "olmo_mmlu", "yi_mmlu"],
33	    "arc": ["llama_arc", "mistral_arc", "gemma_arc", "qwen_arc",
34	            "internlm_arc", "deepseek_arc", "olmo_arc", "yi_arc"],
35	    "hellaswag": ["llama_hellaswag", "mistral_hellaswag", "gemma_hellaswag",
36	                  "qwen_hellaswag", "internlm_hellaswag", "deepseek_hellaswag"],
37	    "gsm8k": ["llama_gsm8k", "mistral_gsm8k", "gemma_gsm8k", "qwen_gsm8k",
38	              "internlm_gsm8k", "deepseek_gsm8k", "olmo_gsm8k", "yi_gsm8k"],
39	    "math": ["llama_math", "mistral_math", "gemma_math", "qwen_math",
40	             "internlm_math", "olmo_math", "yi_math"],
41	}
42	
43	FORMAT_GROUP = {"mmlu": "MC", "arc": "MC", "hellaswag": "MC", "gsm8k": "FF", "math": "FF"}
44	KEEP_COLS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id", "correct"]
45	
46	
47	def load_benchmark(benchmark):
48	    frames = []
49	    for fname in BENCHMARK_FILES[benchmark]:
50
…[truncated 14305 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T23:10:45.916114+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts -type f -name \"*.py\" | xargs grep -l \"8.*model\\|8model\\|ff.*worker\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts -type f -name \"*.py\" | xargs grep -l \"8.*model\\|8model\\|ff.*worker\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T23:10:45.916231+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp004_defensive_analyses.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T23:10:45.916352+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -lah /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -lah /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/*.py"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T23:10:45.916493+00:00_

-rw-r--r-- 1 ubuntu ubuntu  16K May 21 22:52 /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp004_defensive_analyses.py
-rw-r--r-- 1 ubuntu ubuntu 3.3K May 21 03:44 /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/gstudy_full.py
-rw-r--r-- 1 ubuntu ubuntu  18K May 21 09:07 /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/model_as_fixed_gstudy.py
-rw-r--r-- 1 ubuntu ubuntu 7.1K May 21 07:55 /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/sample_benchmarks.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T23:10:45.916619+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/gstudy_full.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/gstudy_full.py"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T23:10:45.916747+00:00_

1	import json
2	import numpy as np
3	import pandas as pd
4	from pathlib import Path
5	from itertools import combinations
6	
7	df = pd.read_csv("results/analysis/llama_full.csv")
8	print("Loaded %d records" % len(df), flush=True)
9	
10	facets = ["precision", "temperature", "prompt_template", "seed", "ordering", "item_id"]
11	levels = {f: sorted(df[f].unique()) for f in facets}
12	n = {f: len(v) for f, v in levels.items()}
13	N = len(df)
14	print("Facet levels:", n, flush=True)
15	
16	results = {}
17	for metric in ["correct", "text_exact_match"]:
18	    print("\n" + "=" * 60, flush=True)
19	    print("METRIC: " + metric, flush=True)
20	
21	    y = df[metric].values.astype(np.float64)
22	    grand_mean = y.mean()
23	    SS_total = ((y - grand_mean) ** 2).sum()
24	    print("Grand mean: %.4f, SS_total: %.4f" % (grand_mean, SS_total), flush=True)
25	
26	    components = {}
27	    main_means = {}
28	    for f in facets:
29	        means = df.groupby(f)[metric].mean()
30	        main_means[f] = means
31	        n_per = N // n[f]
32	        ss = n_per * ((means.values - grand_mean) ** 2).sum()
33	        components[f] = ss
34	        print("  main %s: %.2f%%" % (f, ss / SS_total * 100), flush=True)
35	
36	    for f1, f2 in combinations(facets, 2):
37	        cell_means = df.groupby([f1, f2])[metric].mean().reset_index()
38	        cell_means.columns = [f1, f2, "cell_mean"]
39	        cell_means["f1_mean"] = cell_means[f1].map(main_means[f1])
40	        cell_means["f2_mean"] = cell_means[f2].map(main_means[f2])
41	        n_per = N // (n[f1] * n[f2])
42	        deviations = cell_means["cell_mean"] - cell_means["f1_mean"] - cell_means["f2_mean"] + grand_mean
43	        ss = n_per * (deviations ** 2).sum()
44	        key = "%s:%s" % (f1, f2)
45	        components[key] = ss
46	
47	    ss_explained = sum(components.values())
48	    components["residual"] = SS_total - ss_explained
49	    total_var = sum(components.values())
50	    pct = {k: v / total_var * 100 for k, v in compone
…[truncated 1603 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T23:10:45.916896+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0theory/scripts/model_as_fixed_gstudy.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0theory/scripts/model_as_fixed_gstudy.py"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T23:10:45.917006+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T23:10:45.917126+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/model_as_fixed_gstudy.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/model_as_fixed_gstudy.py"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T23:10:45.917322+00:00_

1	"""Model-as-fixed G-study (MF2 defense).
2	
3	Treats model as a fixed facet (not a random sample from a population of models).
4	Two methods:
5	  A) Per-model 5-facet G-study, then average (clean separation)
6	  B) Remove model:item from σ²δ in the crossed 6-facet design (quick adjustment)
7	
8	Input:  results/analysis/cross_model_4way_bf16.csv (4 models × bf16 × fully crossed)
9	Output: results/analysis/model_as_fixed_gstudy.json
10	"""
11	
12	import json
13	import time
14	from itertools import combinations
15	from math import prod
16	from pathlib import Path
17	
18	import numpy as np
19	import pandas as pd
20	
21	INPUT = "results/analysis/cross_model_4way_bf16.csv"
22	OUTPUT = "results/analysis/model_as_fixed_gstudy.json"
23	N_BOOT = 200
24	SEED = 42
25	
26	FACETS_6 = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
27	FACETS_5 = ["temperature", "prompt_template", "seed", "ordering", "item_id"]
28	
29	t_start = time.time()
30	df = pd.read_csv(INPUT)
31	print(f"Loaded {len(df)} obs ({time.time()-t_start:.1f}s)", flush=True)
32	
33	models_sorted = sorted(df["model"].unique())
34	temps_sorted = sorted(df["temperature"].unique())
35	prompts_sorted = sorted(df["prompt_template"].unique())
36	seeds_sorted = sorted(df["seed"].unique())
37	orders_sorted = sorted(df["ordering"].unique())
38	items_sorted = sorted(df["item_id"].unique())
39	
40	n_m, n_t, n_p, n_s, n_o, n_i = (
41	    len(models_sorted), len(temps_sorted), len(prompts_sorted),
42	    len(seeds_sorted), len(orders_sorted), len(items_sorted),
43	)
44	print(f"Design: {n_m}m × {n_t}t × {n_p}p × {n_s}s × {n_o}o × {n_i}i = {n_m*n_t*n_p*n_s*n_o*n_i}", flush=True)
45	
46	model_map = {v: i for i, v in enumerate(models_sorted)}
47	temp_map = {v: i for i, v in enumerate(temps_sorted)}
48	prompt_map = {v: i for i, v in enumerate(prompts_sorted)}
49	seed_map = {v: i for i, v in enumerate(seeds_sorted)}
50	order_map = {v: i for i, v in enumerate(orders_sorted)}
51	item_map = {v: i for i, v in en
…[truncated 17744 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T23:10:45.917523+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory -type f \\( -name \"*coefficient*\" -o -name \"*compute*g*\" \\) 2>/dev/null | grep -v \".venv\" | grep -v \"__pycache__\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory -type f \\( -name \"*coefficient*\" -o -name \"*compute*g*\" \\) 2>/dev/null | grep -v \".venv\" | grep -v \"__pycache__\""
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T23:10:45.917649+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/logs/workers/worker_fix_qwen_accuracy_recompute_20260521T074236.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T23:10:45.917772+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp001_analysis/dstudy_henderson_i.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp001_analysis/dstudy_henderson_i.py"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T23:10:45.917919+00:00_

1	"""D-study projection using Henderson Method I on exp-001 balanced data (259,200 records).
2	
3	Two analyses:
4	  1. Six-facet (precision × temperature × prompt_template × seed × ordering × item_id)
5	  2. BF16-only five-facet (drop precision, keep bf16 subset: 86,400 records)
6	
7	Output: results/exp001_analysis/dstudy_henderson_i_259k.json
8	"""
9	
10	import json
11	import time
12	from itertools import combinations
13	from math import prod
14	from pathlib import Path
15	
16	import numpy as np
17	import pandas as pd
18	
19	
20	def compute_henderson_i(df: pd.DataFrame, response: str, facets: list[str]):
21	    grand_mean = df[response].mean()
22	    N = len(df)
23	    n_levels = {f: df[f].nunique() for f in facets}
24	
25	    effects = {}
26	
27	    for f in facets:
28	        group_means = df.groupby(f, observed=True)[response].mean()
29	        n_per = N // n_levels[f]
30	        ss = float(n_per * ((group_means - grand_mean) ** 2).sum())
31	        df_eff = n_levels[f] - 1
32	        effects[f] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}
33	
34	    for fi, fj in combinations(facets, 2):
35	        cell_means = df.groupby([fi, fj], observed=True)[response].mean()
36	        main_fi = df.groupby(fi, observed=True)[response].mean()
37	        main_fj = df.groupby(fj, observed=True)[response].mean()
38	        n_per = N // (n_levels[fi] * n_levels[fj])
39	        ss = 0.0
40	        for (li, lj), cm in cell_means.items():
41	            interaction = cm - main_fi[li] - main_fj[lj] + grand_mean
42	            ss += n_per * interaction ** 2
43	        df_eff = (n_levels[fi] - 1) * (n_levels[fj] - 1)
44	        effects[f"{fi}:{fj}"] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}
45	
46	    ss_total = float(((df[response] - grand_mean) ** 2).sum())
47	    ss_model = sum(e["ss"] for e in effects.values())
48	    ss_res = max(0.0, ss_total - ss_model)
49	    df_res = N - 1 - sum(e["df"] for e in effects.values())
50	    effe
…[truncated 5919 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T23:10:45.918133+00:00_

Perfect! Now I have all the information I need. Let me compile a comprehensive comparison report.

## Facet Structure Comparison Report

I found **three main G-study implementations** in your project (not a separate 8-model file yet). Here's the detailed comparison:

### **1. Per-Benchmark 4-Model G-Study** 
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/exp002_analysis/per_benchmark_gstudy.py`

**Facets (6 total):**
- model
- temperature
- prompt_template
- seed
- ordering
- item_id

**Data Structure:**
- Input: Merged exp-002 JSONL files (4 models × 4 benchmarks × bf16 × 2 temps × 6 prompts × 6 seeds × 4 orderings)
- Scoring column: `correct` (binary)
- All 2-way interactions computed; residual absorbs ≥3-way interactions
- Processed per benchmark separately

**G_item Computation (lines 105-130):**
```
σ²(item) = vc["item_id"]
σ²δ = Σ[all X:item_id interactions / n_X] + residual / Π(n_X where X ≠ item_id)
G_item = σ²(item) / (σ²(item) + σ²δ)
```

**Henderson Type I Details (lines 48-102):**
- Main effects: SS = n_per × Σ(level_means - grand_mean)²
- 2-way interactions: SS computed via cell means with orthogonal decomposition
- Residual: SS_total - SS_model, df_res = N - 1 - Σ(df_effects)
- Variance components extracted via MS differences: VC[f] = (MS[f] - Σ(interaction_contrib) - MS_res) / coeff
- Coefficients: prod(n_levels[f] for f in facets if f ∉ {fi, fj})

---

### **2. Single-Model/LLaMA G-Study** 
**File:** `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/gstudy_full.py`

**Facets (6 total):**
- precision (replaces model)
- temperature
- prompt_template
- seed
- ordering
- item_id

**Data Structure:**
- Input: CSV file (llama_full.csv)
- Scoring columns: `correct`, `text_exact_match` (binary/continuous)
- Both metrics analyzed separately

**G_item Computation (lines 58-60):**
```
τ = σ²(item_id) / total_var
G_coefficient = τ  (simplified - assumes item is only source of vari
…[truncated 4571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "Agent",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T23:10:45.918327+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T23:10:45.918478+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T23:10:45.918610+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "ls /root/nlp_variance_gtheory/results/exp004_8model_analysis/per_benchmark_gstudy_ff.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "ls /root/nlp_variance_gtheory/results/exp004_8model_analysis/per_benchmark_gstudy_ff.json"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T23:10:45.918726+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "ls /root/nlp_variance_gtheory/results/exp002/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "ls /root/nlp_variance_gtheory/results/exp002/"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T23:10:45.918837+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /root/nlp_variance_gtheory/results/exp004_8model_analysis/per_benchmark_gstudy_ff.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /root/nlp_variance_gtheory/results/exp004_8model_analysis/per_benchmark_gstudy_ff.json"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T23:10:45.918951+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/nlp_variance_gtheory/results/exp004_8model_analysis/per_benchmark_gstudy_ff.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-21T23:10:45.919092+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"chain_deepseek.log\\nchain_internlm.log\\ndeepseek_arc.jsonl\\ndeepseek_gsm8k.jsonl\\ndeepseek_hellaswag.jsonl\\ndeepseek_math.jsonl\\ndeepseek_math_gpu2.jsonl\\ndeepseek_mmlu.jsonl\\ndesign_matrix_exp002_full.csv\\ndesign_matrix_new_models.csv\\nfull_run.log\\ngemma_arc.jsonl\\ngemma_gsm8k.jsonl\\ngemma_hellaswag.jsonl\\ngemma_math.jsonl\\ngemma_mmlu.jsonl\\ngpu0_internlm_math.log\\ngpu0_qwen.log\\ngpu1_internlm_arc.log\\ngpu1_internlm_gsm8k.log\\ngpu1_internlm_hellaswag.log\\ngpu1_internlm_mmlu.log\\ngpu1_llama.log\\ngpu2_deepseek_math.log\\ngpu2_gemma.log\\ngpu3_deepseek_arc.log\\ngpu3_deepseek_gsm8k.log\\ngpu3_deepseek_hellaswag.log\\ngpu3_deepseek_mmlu.log\\ngpu3_mistral.log\\ninternlm_arc.jsonl\\ninternlm_gsm8k.jsonl\\ninternlm_hellaswag.jsonl\\ninternlm_math.jsonl\\ninternlm_mmlu.jsonl\\nllama_arc.jsonl\\nllama_gsm8k.jsonl\\nllama_hellaswag.jsonl\\nllama_math.jsonl\\nllama_mmlu.jsonl\\nmath_then_new_models.log\\nmistral_arc.jsonl\\nmistral_gsm8k.jsonl\\nmistral_hellaswag.jsonl\\nmistral_math.jsonl\\nmistral_mmlu.jsonl\\nolmo_arc.jsonl\\nolmo_gsm8k.jsonl\\nolmo_math.jsonl\\nolmo_mmlu.jsonl\\nqwen_arc.jsonl\\nqwen_gsm8k.jsonl\\nqwen_hellaswag.jsonl\\nqwen_math.jsonl\\nqwen_mmlu.jsonl\\nshard_0_qwen.csv\\nshard_1_llama.csv\\nshard_2_gemma.csv\\nshard_3_mistral.csv\\nshard_deepseek_arc.csv\\nshard_deepseek_gsm8k.csv\\nshard_deepseek_hellaswag.csv\\nshard_deepseek_math.csv\\nshard_deepseek_mmlu.csv\\nshard_gemma_arc.csv\\nshard_gemma_gsm8k.csv\\nshard_gemma_hellaswag.csv\\nshard_gemma_math.csv\\nshard_gemma_mmlu.csv\\nshard_internlm_arc.csv\\nshard_internlm_gsm8k.csv\\nshard_internlm_hellaswag.csv\\nshard_internlm_math.csv\\nshard_internlm_mmlu.csv\\nshard_llama_arc.csv\\nshard_llama_gsm8k.csv\\nshard_llama_hellaswag.csv\\nshard_llama_math.csv\\nshard_llama_mmlu.csv\\nshard_mistral_arc.csv\\nshard_mistral_gsm8k.csv\\nshard_mistral_hellaswag.csv\\nshard_mistral_math.csv\\nshard_mistral_mmlu.csv\\nshard_qwen_ar
…[truncated 270 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T23:10:45.919455+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-004\\\",\\n  \\\"analysis\\\": \\\"per_benchmark_henderson_i_gstudy_freeform\\\",\\n  \\\"facets\\\": [\\n    \\\"model\\\",\\n    \\\"temperature\\\",\\n    \\\"prompt_template\\\",\\n    \\\"seed\\\",\\n    \\\"ordering\\\",\\n    \\\"item_id\\\"\\n  ],\\n  \\\"note_math\\\": \\\"DeepSeek excluded from MATH (incomplete data: 37400/57600 lines)\\\",\\n  \\\"benchmarks\\\": {\\n    \\\"gsm8k\\\": {\\n      \\\"benchmark\\\": \\\"gsm8k\\\",\\n      \\\"n_observations\\\": 460800,\\n      \\\"n_models\\\": 8,\\n      \\\"models\\\": [\\n        \\\"DeepSeek-7B\\\",\\n        \\\"Gemma-2-9B\\\",\\n        \\\"InternLM2.5-7B\\\",\\n        \\\"Llama-3.1-8B\\\",\\n        \\\"Mistral-7B-v0.3\\\",\\n        \\\"OLMo-2-7B\\\",\\n        \\\"Qwen3-8B\\\",\\n        \\\"Yi-1.5-9B\\\"\\n      ],\\n      \\\"n_levels\\\": {\\n        \\\"model\\\": 8,\\n        \\\"temperature\\\": 2,\\n        \\\"prompt_template\\\": 6,\\n        \\\"seed\\\": 6,\\n        \\\"ordering\\\": 4,\\n        \\\"item_id\\\": 200\\n      },\\n      \\\"grand_mean_accuracy\\\": 0.581923,\\n      \\\"variance_components\\\": {\\n        \\\"residual\\\": {\\n          \\\"estimate\\\": 0.0996441838,\\n          \\\"pct\\\": 39.8941\\n        },\\n        \\\"item_id\\\": {\\n          \\\"estimate\\\": 0.0421014063,\\n          \\\"pct\\\": 16.8559\\n        },\\n        \\\"model:item_id\\\": {\\n          \\\"estimate\\\": 0.036345528,\\n          \\\"pct\\\": 14.5515\\n        },\\n        \\\"model\\\": {\\n          \\\"estimate\\\": 0.0268400916,\\n          \\\"pct\\\": 10.7458\\n        },\\n        \\\"model:prompt_template\\\": {\\n          \\\"estimate\\\": 0.021308241,\\n          \\\"pct\\\": 8.5311\\n        },\\n        \\\"prompt_template\\\": {\\n          \\\"estimate\\\": 0.0135210714,\\n          \\\"pct\\\": 5.4134\\n        },\\n        \\\"prompt_template:item_id\\\": {\\n          \\\"e
…[truncated 8553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T23:10:45.919660+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "find /root/nlp_variance_gtheory/results -name \"*per_benchmark*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "find /root/nlp_variance_gtheory/results -name \"*per_benchmark*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T23:10:45.919803+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json\\n/root/nlp_variance_gtheory/results/exp004_8model_analysis/per_benchmark_gstudy_mc.json\\n/root/nlp_variance_gtheory/results/exp004_8model_analysis/per_benchmark_gstudy_ff.json\\n/root/nlp_variance_gtheory/results/exp004_8model_analysis/per_benchmark_gstudy_mmlu.json\\n/root/nlp_variance_gtheory/results/exp004_8model_analysis/per_benchmark_gstudy_hellaswag.json\\n/root/nlp_variance_gtheory/results/exp004_8model_analysis/per_benchmark_gstudy_arc.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T23:10:45.919929+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /root/nlp_variance_gtheory/scripts/exp004_defensive_analyses.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /root/nlp_variance_gtheory/scripts/exp004_defensive_analyses.py"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T23:10:45.920208+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Phase 2 defensive analyses: Bernoulli baseline + MMLU subsampling + LOBO stability.\\n\\nProduces: results/exp004_8model_analysis/defensive_analyses.json\\n\\\"\\\"\\\"\\n\\nimport json\\nimport sys\\nimport time\\nfrom itertools import combinations\\nfrom math import prod\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport pandas as pd\\n\\nsys.path.insert(0, str(Path(__file__).resolve().parents[1]))\\nfrom src.config.model_paths import normalize_model_name\\n\\nFACETS = [\\\"model\\\", \\\"temperature\\\", \\\"prompt_template\\\", \\\"seed\\\", \\\"ordering\\\", \\\"item_id\\\"]\\nDATA_DIR = Path(\\\"results/exp002\\\")\\nOUTPUT_DIR = Path(\\\"results/exp004_8model_analysis\\\")\\n\\nBENCHMARK_FILES = {\\n    \\\"mmlu\\\": [\\\"llama_mmlu\\\", \\\"mistral_mmlu\\\", \\\"gemma_mmlu\\\", \\\"qwen_mmlu\\\",\\n             \\\"internlm_mmlu\\\", \\\"deepseek_mmlu\\\", \\\"olmo_mmlu\\\", \\\"yi_mmlu\\\"],\\n    \\\"arc\\\": [\\\"llama_arc\\\", \\\"mistral_arc\\\", \\\"gemma_arc\\\", \\\"qwen_arc\\\",\\n            \\\"internlm_arc\\\", \\\"deepseek_arc\\\", \\\"olmo_arc\\\", \\\"yi_arc\\\"],\\n    \\\"hellaswag\\\": [\\\"llama_hellaswag\\\", \\\"mistral_hellaswag\\\", \\\"gemma_hellaswag\\\",\\n                  \\\"qwen_hellaswag\\\", \\\"internlm_hellaswag\\\", \\\"deepseek_hellaswag\\\"],\\n    \\\"gsm8k\\\": [\\\"llama_gsm8k\\\", \\\"mistral_gsm8k\\\", \\\"gemma_gsm8k\\\", \\\"qwen_gsm8k\\\",\\n              \\\"internlm_gsm8k\\\", \\\"deepseek_gsm8k\\\", \\\"olmo_gsm8k\\\", \\\"yi_gsm8k\\\"],\\n    \\\"math\\\": [\\\"llama_math\\\", \\\"mistral_math\\\", \\\"gemma_math\\\", \\\"qwen_math\\\",\\n             \\\"internlm_math\\\", \\\"olmo_math\\\", \\\"yi_math\\\"],\\n}\\n\\nFORMAT_GROUP = {\\\"mmlu\\\": \\\"MC\\\", \\\"arc\\\": \\\"MC\\\", \\\"hellaswag\\\": \\\"MC\\\", \\\"gsm8k\\\": \\\"FF\\\", \\\"math\\\": \\\"FF\\\"}\\nKEEP_COLS = [\\\"model\\\", \\\"temperatu
…[truncated 7651 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T23:10:45.920398+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "python3 -c \"import json; d=json.load(open('/root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json')); gsm=d['benchmarks']['gsm8k']; print(json.dumps({k:gsm[k] for k in ['n_models','models','n_levels','G_item','sigma_tau','sigma_delta','grand_mean_accuracy']}, indent=2))\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "python3 -c \"import json; d=json.load(open('/root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json')); gsm=d['benchmarks']['gsm8k']; print(json.dumps({k:gsm[k] for k in ['n_models','models','n_levels','G_item','sigma_tau','sigma_delta','grand_mean_accuracy']}, indent=2))\""
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T23:10:45.920542+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T23:10:45.920672+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "python3 -c \"import json; d=json.load(open('/root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json')); gsm=d['benchmarks']['gsm8k']; vc=gsm['variance_components']; print(json.dumps({k:v for k,v in vc.items() if v['pct']>0.5}, indent=2))\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "python3 -c \"import json; d=json.load(open('/root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json')); gsm=d['benchmarks']['gsm8k']; vc=gsm['variance_components']; print(json.dumps({k:v for k,v in vc.items() if v['pct']>0.5}, indent=2))\""
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T23:10:45.920802+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T23:10:45.920925+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T23:10:45.921313+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-002\\\",\\n  \\\"analysis\\\": \\\"per_benchmark_henderson_i_gstudy\\\",\\n  \\\"facets\\\": [\\n    \\\"model\\\",\\n    \\\"temperature\\\",\\n    \\\"prompt_template\\\",\\n    \\\"seed\\\",\\n    \\\"ordering\\\",\\n    \\\"item_id\\\"\\n  ],\\n  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"benchmark\\\": \\\"mmlu\\\",\\n      \\\"n_observations\\\": 230400,\\n      \\\"n_levels\\\": {\\n        \\\"model\\\": 4,\\n        \\\"temperature\\\": 2,\\n        \\\"prompt_template\\\": 6,\\n        \\\"seed\\\": 6,\\n        \\\"ordering\\\": 4,\\n        \\\"item_id\\\": 200\\n      },\\n      \\\"grand_mean_accuracy\\\": 0.700247,\\n      \\\"variance_components\\\": {\\n        \\\"item_id\\\": {\\n          \\\"estimate\\\": 0.0876133124,\\n          \\\"pct\\\": 41.5471\\n        },\\n        \\\"model:item_id\\\": {\\n          \\\"estimate\\\": 0.0691895248,\\n          \\\"pct\\\": 32.8103\\n        },\\n        \\\"residual\\\": {\\n          \\\"estimate\\\": 0.043262815,\\n          \\\"pct\\\": 20.5156\\n        },\\n        \\\"prompt_template:item_id\\\": {\\n          \\\"estimate\\\": 0.0029608526,\\n          \\\"pct\\\": 1.4041\\n        },\\n        \\\"seed:item_id\\\": {\\n          \\\"estimate\\\": 0.0025039227,\\n          \\\"pct\\\": 1.1874\\n        },\\n        \\\"temperature:item_id\\\": {\\n          \\\"estimate\\\": 0.00249588,\\n          \\\"pct\\\": 1.1836\\n        },\\n        \\\"model\\\": {\\n          \\\"estimate\\\": 0.0015897059,\\n          \\\"pct\\\": 0.7539\\n        },\\n        \\\"ordering:item_id\\\": {\\n          \\\"estimate\\\": 0.0010917321,\\n          \\\"pct\\\": 0.5177\\n        },\\n        \\\"model:temperature\\\": {\\n          \\\"estimate\\\": 6.01697e-05,\\n          \\\"pct\\\": 0.0285\\n        },\\n        \\\"model:prompt_template\\\": {\\n          \\\"estimate\\\": 3.90555e-05,\\n          \\\"
…[truncated 8518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T23:10:45.921585+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /root/nlp_variance_gtheory/scripts/exp002_analysis/per_benchmark_gstudy.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /root/nlp_variance_gtheory/scripts/exp002_analysis/per_benchmark_gstudy.py"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T23:10:45.921857+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Per-benchmark Henderson I variance decomposition for exp-002.\\n\\nInput:  Merged exp-002 JSONL (4 models x 4 benchmarks x bf16 x 2 temps x 6 prompts x 6 seeds x 4 orderings).\\nOutput: results/analysis/exp002_per_benchmark_gstudy.json\\n        — per-benchmark variance components, G_item, D-study projections.\\n\\nFacets (7, within each benchmark):\\n  model, temperature, prompt_template, seed, ordering, item_id\\n  + all 2-way interactions. Residual absorbs >=3-way.\\n\\nUsage:\\n  python scripts/exp002_analysis/per_benchmark_gstudy.py --data-dir results/exp002\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport sys\\nimport time\\nfrom itertools import combinations\\nfrom math import prod\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport pandas as pd\\n\\nsys.path.insert(0, str(Path(__file__).resolve().parents[2]))\\nfrom src.config.model_paths import normalize_model_name\\n\\nFACETS = [\\\"model\\\", \\\"temperature\\\", \\\"prompt_template\\\", \\\"seed\\\", \\\"ordering\\\", \\\"item_id\\\"]\\nBENCHMARKS = [\\\"mmlu\\\", \\\"gsm8k\\\", \\\"arc\\\", \\\"hellaswag\\\"]\\n\\n\\ndef load_exp002_data(data_dir: str) -> pd.DataFrame:\\n    data_path = Path(data_dir)\\n    jsonl_files = sorted(data_path.glob(\\\"*.jsonl\\\"))\\n    if not jsonl_files:\\n        raise FileNotFoundError(f\\\"No JSONL files in {data_dir}\\\")\\n    frames = [pd.read_json(f, lines=True) for f in jsonl_files]\\n    df = pd.concat(frames, ignore_index=True)\\n    if \\\"top_logprobs\\\" in df.columns:\\n        df.drop(columns=[\\\"top_logprobs\\\"], inplace=True)\\n    df[\\\"model\\\"] = df[\\\"model\\\"].map(normalize_model_name).fillna(df[\\\"model\\\"])\\n    for f in FACETS:\\n        df[f] = df[f].astype(str)\\n    return df\\n\\n\\ndef compute_henderson_i(df: pd.DataFrame, response: str, facets: list[str]):\\n    \\\"\\\"\\\"Henderson Method I: SS -> EMS -> variance components.\\\"\\\"\\\"\\n    gra
…[truncated 7246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T23:10:45.922039+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "grep -n \"def compute_g_item\\|def d_study_curve\\|def find_min_items\" /root/nlp_variance_gtheory/scripts/exp002_analysis/per_benchmark_gstudy.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "grep -n \"def compute_g_item\\|def d_study_curve\\|def find_min_items\" /root/nlp_variance_gtheory/scripts/exp002_analysis/per_benchmark_gstudy.py"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T23:10:45.922175+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T23:10:45.922303+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "grep -n \"def \" /root/nlp_variance_gtheory/scripts/exp002_analysis/per_benchmark_gstudy.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "grep -n \"def \" /root/nlp_variance_gtheory/scripts/exp002_analysis/per_benchmark_gstudy.py"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T23:10:45.922454+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"33:def load_exp002_data(data_dir: str) -> pd.DataFrame:\\n48:def compute_henderson_i(df: pd.DataFrame, response: str, facets: list[str]):\\n105:def compute_g_item(vc: dict, n_levels: dict) -> tuple[float, float, float]:\\n133:def d_study_curve(vc: dict, n_levels: dict, item_counts: list[int]) -> dict:\\n163:def find_min_items_for_g(vc: dict, n_levels: dict, target_g: float, max_items: int = 2000) -> int | None:\\n192:def analyze_benchmark(df_bm: pd.DataFrame, benchmark: str) -> dict:\\n226:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T23:10:45.922583+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "head -195 /root/nlp_variance_gtheory/scripts/exp002_analysis/per_benchmark_gstudy.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "head -195 /root/nlp_variance_gtheory/scripts/exp002_analysis/per_benchmark_gstudy.py"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-21T23:10:45.922800+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Per-benchmark Henderson I variance decomposition for exp-002.\\n\\nInput:  Merged exp-002 JSONL (4 models x 4 benchmarks x bf16 x 2 temps x 6 prompts x 6 seeds x 4 orderings).\\nOutput: results/analysis/exp002_per_benchmark_gstudy.json\\n        — per-benchmark variance components, G_item, D-study projections.\\n\\nFacets (7, within each benchmark):\\n  model, temperature, prompt_template, seed, ordering, item_id\\n  + all 2-way interactions. Residual absorbs >=3-way.\\n\\nUsage:\\n  python scripts/exp002_analysis/per_benchmark_gstudy.py --data-dir results/exp002\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport sys\\nimport time\\nfrom itertools import combinations\\nfrom math import prod\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport pandas as pd\\n\\nsys.path.insert(0, str(Path(__file__).resolve().parents[2]))\\nfrom src.config.model_paths import normalize_model_name\\n\\nFACETS = [\\\"model\\\", \\\"temperature\\\", \\\"prompt_template\\\", \\\"seed\\\", \\\"ordering\\\", \\\"item_id\\\"]\\nBENCHMARKS = [\\\"mmlu\\\", \\\"gsm8k\\\", \\\"arc\\\", \\\"hellaswag\\\"]\\n\\n\\ndef load_exp002_data(data_dir: str) -> pd.DataFrame:\\n    data_path = Path(data_dir)\\n    jsonl_files = sorted(data_path.glob(\\\"*.jsonl\\\"))\\n    if not jsonl_files:\\n        raise FileNotFoundError(f\\\"No JSONL files in {data_dir}\\\")\\n    frames = [pd.read_json(f, lines=True) for f in jsonl_files]\\n    df = pd.concat(frames, ignore_index=True)\\n    if \\\"top_logprobs\\\" in df.columns:\\n        df.drop(columns=[\\\"top_logprobs\\\"], inplace=True)\\n    df[\\\"model\\\"] = df[\\\"model\\\"].map(normalize_model_name).fillna(df[\\\"model\\\"])\\n    for f in FACETS:\\n        df[f] = df[f].astype(str)\\n    return df\\n\\n\\ndef compute_henderson_i(df: pd.DataFrame, response: str, facets: list[str]):\\n    \\\"\\\"\\\"Henderson Method I: SS -> EMS -> variance components.\\\"\\\"\\\"\\n    gra
…[truncated 6395 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-21T23:10:45.922994+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "grep -rn \"per_benchmark_gstudy_ff\" /root/nlp_variance_gtheory/scripts/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "grep -rn \"per_benchmark_gstudy_ff\" /root/nlp_variance_gtheory/scripts/"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-21T23:10:45.923125+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/nlp_variance_gtheory/scripts/exp004_ff_gstudy.py:416:    out_path = out_dir / \\\"per_benchmark_gstudy_ff.json\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-21T23:10:45.923244+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "grep -n \"def \" /root/nlp_variance_gtheory/scripts/exp004_ff_gstudy.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "grep -n \"def \" /root/nlp_variance_gtheory/scripts/exp004_ff_gstudy.py"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-21T23:10:45.923357+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "head -160 /root/nlp_variance_gtheory/scripts/exp004_ff_gstudy.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "head -160 /root/nlp_variance_gtheory/scripts/exp004_ff_gstudy.py"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-21T23:10:45.923499+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"25:def load_data(data_dir, benchmark):\\n52:def compute_henderson_i(df, response, facets):\\n107:def compute_g_item(vc, n_levels):\\n126:def d_study_curve(vc, n_levels, item_counts):\\n151:def fast_bootstrap_ci(df, facets, n_boot=1000, seed=42):\\n332:def analyze_benchmark(df_bm, benchmark):\\n375:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-21T23:10:45.923688+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"exp-004: Per-benchmark Henderson I G-study for free-form benchmarks (GSM8K, MATH).\\n\\n8 models for GSM8K, 7 for MATH (deepseek incomplete).\\nFacets: model, temperature, prompt_template, seed, ordering, item_id\\nBootstrap CIs: 1000 resamples over items.\\nOptimized: precompute item-condition matrix for fast bootstrap.\\n\\\"\\\"\\\"\\n\\nimport json\\nimport sys\\nimport time\\nfrom itertools import combinations\\nfrom math import prod\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport pandas as pd\\n\\nsys.path.insert(0, str(Path(__file__).resolve().parents[1]))\\nfrom src.config.model_paths import normalize_model_name\\n\\nFACETS = [\\\"model\\\", \\\"temperature\\\", \\\"prompt_template\\\", \\\"seed\\\", \\\"ordering\\\", \\\"item_id\\\"]\\n\\n\\ndef load_data(data_dir, benchmark):\\n    data_path = Path(data_dir)\\n    frames = []\\n    for f in sorted(data_path.glob(\\\"*.jsonl\\\")):\\n        if benchmark not in f.name:\\n            continue\\n        if benchmark == \\\"math\\\" and f.name == \\\"deepseek_math.jsonl\\\":\\n            continue\\n        if benchmark == \\\"math\\\" and \\\"deepseek\\\" in f.name:\\n            continue\\n        df_tmp = pd.read_json(f, lines=True)\\n        if \\\"_placeholder\\\" in df_tmp.columns:\\n            df_tmp = df_tmp[df_tmp[\\\"_placeholder\\\"] != True]\\n        if \\\"benchmark\\\" in df_tmp.columns:\\n            df_tmp = df_tmp[df_tmp[\\\"benchmark\\\"] == benchmark]\\n        if len(df_tmp) > 0:\\n            frames.append(df_tmp)\\n            print(f\\\"  {f.name}: {len(df_tmp)} rows\\\", flush=True)\\n    df = pd.concat(frames, ignore_index=True)\\n    if \\\"top_logprobs\\\" in df.columns:\\n        df.drop(columns=[\\\"top_logprobs\\\"], inplace=True)\\n    df[\\\"model\\\"] = df[\\\"model\\\"].map(normalize_model_name).fillna(df[\\\"model\\\"])\\n    for f in FACETS:\\n        df[f] = df[f].astype(str)\\n    return df\\
…[truncated 4844 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-21T23:10:45.923983+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32570",
  "command": "cat > /root/nlp_variance_gtheory/scripts/gitem_consistency_check.py << 'SCRIPT'\n\"\"\"G_item consistency diagnostic: 4-model vs 8-model GSM8K.\n\nRoot cause hypothesis: exp004_ff_gstudy.py has divisor=1 for residual in compute_g_item,\nwhile per_benchmark_gstudy.py correctly divides by prod(non_item_facet_levels).\n\"\"\"\nimport json\nimport sys\nimport time\nfrom itertools import combinations\nfrom math import prod\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\n\nsys.path.insert(0, str(Path(__file__).resolve().parents[1]))\nfrom src.config.model_paths import normalize_model_name\n\nFACETS = [\"model\", \"temperature\", \"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\nDATA_DIR = Path(\"results/exp002\")\nKEEP_COLS = [\"model\", \"temperature\", \"prompt_template\", \"seed\", \"ordering\", \"item_id\", \"correct\"]\n\nMODEL_ORDER = [\"Llama-3.1-8B\", \"Mistral-7B-v0.3\", \"Qwen3-8B\", \"Gemma-2-9B\",\n               \"InternLM2.5-7B\", \"DeepSeek-7B\", \"OLMo-2-7B\", \"Yi-1.5-9B\"]\n\nGSM8K_FILES = [\"llama_gsm8k\", \"mistral_gsm8k\", \"qwen_gsm8k\", \"gemma_gsm8k\",\n               \"internlm_gsm8k\", \"deepseek_gsm8k\", \"olmo_gsm8k\", \"yi_gsm8k\"]\n\nMMLU_FILES = [\"llama_mmlu\", \"mistral_mmlu\", \"qwen_mmlu\", \"gemma_mmlu\",\n              \"internlm_mmlu\", \"deepseek_mmlu\", \"olmo_mmlu\", \"yi_mmlu\"]\n\n\ndef load_benchmark_data(benchmark_files):\n    frames = []\n    for fname in benchmark_files:\n        fpath = DATA_DIR / f\"{fname}.jsonl\"\n        if not fpath.exists():\n            print(f\"  SKIP {fpath}\")\n            continue\n        df = pd.read_json(fpath, lines=True)\n        if \"_placeholder\" in df.columns:\n            df = df[df[\"_placeholder\"] != True]\n        if \"top_logprobs\" in df.columns:\n            df.drop(columns=[\"top_logprobs\"], inplace=True)\n        df[\"model\"] = df[\"model\"].map(normalize_model_name).fillna(df[\"model\"])\n        for f in FACETS:\n            df[f] = df[f].astype(str)\n        frames.append(df[KEEP_COLS])\n    return pd.concat(frames, ignore_index=True)\n\n\ndef henderson_i(df):\n    grand_mean = df[\"correct\"].mean()\n    N = len(df)\n    n_levels = {f: df[f].nunique() for f in FACETS}\n    effects = {}\n\n    for f in FACETS:\n        gm = df.groupby(f, observed=True)[\"correct\"].mean()\n        n_per = N // n_levels[f]\n        ss = float(n_per * ((gm - grand_mean) ** 2).sum())\n        dof = n_levels[f] - 1\n        effects[f] = {\"ss\": ss, \"df\": dof, \"ms\": ss / dof if dof > 0 else 0.0}\n\n    for fi, fj in combinations(FACETS, 2):\n        cm = df.groupby([fi, fj], observed=True)[\"correct\"].mean()\n        mi = df.groupby(fi, observed=True)[\"correct\"].mean()\n        mj = df.groupby(fj, observed=True)[\"correct\"].mean()\n        n_per = N // (n_levels[fi] * n_levels[fj])\n        ss = 0.0\n        for (li, lj), val in cm.items():\n            ss += n_per * (val - mi[li] - mj[lj] + grand_mean) ** 2\n        dof = (n_levels[fi] - 1) * (n_levels[fj] - 1)\n        effects[f\"{fi}:{fj}\"] = {\"ss\": ss, \"df\": dof, \"ms\": ss / dof if dof > 0 else 0.0}\n\n    ss_total = float(((df[\"correct\"] - grand_mean) ** 2).sum())\n    ss_model_sum = sum(e[\"ss\"] for e in effects.values())\n    ss_res = max(0.0, ss_total - ss_model_sum)\n    df_res = N - 1 - sum(e[\"df\"] for e in effects.values())\n    effects[\"residual\"] = {\"ss\": ss_res, \"df\": df_res, \"ms\": ss_res / df_res if df_res > 0 else 0.0}\n\n    ms_res = effects[\"residual\"][\"ms\"]\n    vc = {}\n    for fi, fj in combinations(FACETS, 2):\n        key = f\"{fi}:{fj}\"\n        coeff = prod(n_levels[f] for f in FACETS if f not in (fi, fj))\n        vc[key] = max(0.0, (effects[key][\"ms\"] - ms_res) / coeff if coeff > 0 else 0.0)\n\n    for fi in FACETS:\n        coeff_main = prod(n_levels[f] for f in FACETS if f != fi)\n        ic = 0.0\n        for fj in FACETS:\n            if fj == fi:\n                continue\n            ik = f\"{fi}:{fj}\" if f\"{fi}:{fj}\" in vc else f\"{fj}:{fi}\"\n            cij = prod(n_levels[f] for f in FACETS if f not in (fi, fj))\n            ic += cij * vc[ik]\n        vc[fi] = max(0.0, (effects[fi][\"ms\"] - ic - ms_res) / coeff_main if coeff_main > 0 else 0.0)\n\n    vc[\"residual\"] = ms_res\n    return vc, n_levels\n\n\ndef g_item_correct(vc, n_levels):\n    \"\"\"Correct formula: residual / prod(non_item_facets).\"\"\"\n    non_item = [f for f in FACETS if f != \"item_id\"]\n    sigma_item = vc.get(\"item_id\", 0.0)\n    sigma_delta = 0.0\n    for key, est in vc.items():\n        if est == 0.0 or key == \"item_id\":\n            continue\n        if key == \"residual\":\n            sigma_delta += est / prod(n_levels[f] for f in non_item)\n            continue\n        parts = set(key.split(\":\"))\n        if \"item_id\" not in parts:\n            continue\n        other = [p for p in parts if p != \"item_id\"]\n        sigma_delta += est / (prod(n_levels[o] for o in other) if other else 1)\n    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0\n    return g, sigma_item, sigma_delta\n\n\ndef g_item_buggy(vc, n_levels):\n    \"\"\"Buggy formula from exp004_ff_gstudy.py: residual / 1.\"\"\"\n    sigma_item = vc.get(\"item_id\", 0.0)\n    sigma_delta = 0.0\n    for key, est in vc.items():\n        if key == \"item_id\":\n            continue\n        parts = key.split(\":\")\n        other = [p for p in parts if p != \"item_id\"]\n        if \"item_id\" not in parts and key != \"residual\":\n            continue\n        if key == \"residual\":\n            divisor = 1\n        else:\n            divisor = prod(n_levels[o] for o in other) if other else 1\n        sigma_delta += est / divisor\n    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0\n    return g, sigma_item, sigma_delta\n\n\ndef item_accuracy_profiles(df):\n    \"\"\"Per-model item accuracy vector (200 items).\"\"\"\n    items = sorted(df[\"item_id\"].unique())\n    models = sorted(df[\"model\"].unique())\n    profiles = {}\n    for m in models:\n        acc = df[df[\"model\"] == m].groupby(\"item_id\")[\"correct\"].mean()\n        profiles[m] = np.array([acc.get(i, np.nan) for i in items])\n    return profiles, items\n\n\ndef pairwise_correlations(profiles):\n    models = sorted(profiles.keys())\n    n = len(models)\n    corr = np.zeros((n, n))\n    for i in range(n):\n        for j in range(n):\n            mask = ~(np.isnan(profiles[models[i]]) | np.isnan(profiles[models[j]]))\n            corr[i, j] = np.corrcoef(profiles[models[i]][mask], profiles[models[j]][mask])[0, 1]\n    return corr, models\n\n\ndef main():\n    t0 = time.time()\n    results = {}\n\n    # === Step 1: Load all GSM8K data ===\n    print(\"Loading GSM8K data...\", flush=True)\n    df_gsm = load_benchmark_data(GSM8K_FILES)\n    print(f\"  {len(df_gsm)} rows, {df_gsm['model'].nunique()} models\", flush=True)\n    print(f\"  Models: {sorted(df_gsm['model'].unique())}\", flush=True)\n\n    # === Step 2: Bug confirmation ===\n    print(\"\\n=== Bug Confirmation: 8-model GSM8K ===\", flush=True)\n    vc8, nl8 = henderson_i(df_gsm)\n    g_correct, st_c, sd_c = g_item_correct(vc8, nl8)\n    g_buggy, st_b, sd_b = g_item_buggy(vc8, nl8)\n\n    non_item_prod = prod(nl8[f] for f in FACETS if f != \"item_id\")\n    print(f\"  residual = {vc8['residual']:.6f}\", flush=True)\n    print(f\"  prod(non_item) = {non_item_prod}\", flush=True)\n    print(f\"  residual/prod = {vc8['residual']/non_item_prod:.8f}\", flush=True)\n    print(f\"  residual/1    = {vc8['residual']:.8f}\", flush=True)\n    print(f\"  G_item (correct, /prod): {g_correct:.6f}  sigma_delta={sd_c:.8f}\", flush=True)\n    print(f\"  G_item (buggy, /1):      {g_buggy:.6f}  sigma_delta={sd_b:.8f}\", flush=True)\n    print(f\"  Reported 8-model G_item: 0.283713\", flush=True)\n    print(f\"  Reported 4-model G_item: 0.728948\", flush=True)\n\n    results[\"step2_bug_confirmation\"] = {\n        \"eight_model_correct_G\": round(g_correct, 6),\n        \"eight_model_buggy_G\": round(g_buggy, 6),\n        \"reported_8model_G\": 0.283713,\n        \"reported_4model_G\": 0.728948,\n        \"residual\": round(vc8[\"residual\"], 10),\n        \"prod_non_item\": non_item_prod,\n        \"bug_location\": \"exp004_ff_gstudy.py:compute_g_item line ~120, divisor=1 for residual\",\n        \"correct_divisor\": f\"prod(non_item_facets) = {non_item_prod}\",\n    }\n\n    # === Step 2b: 4-model subset verification ===\n    print(\"\\n=== 4-Model Subset Verification ===\", flush=True)\n    original_4 = [\"Llama-3.1-8B\", \"Mistral-7B-v0.3\", \"Qwen3-8B\", \"Gemma-2-9B\"]\n    df_4sub = df_gsm[df_gsm[\"model\"].isin(original_4)].reset_index(drop=True)\n    vc4, nl4 = henderson_i(df_4sub)\n    g4_correct, _, _ = g_item_correct(vc4, nl4)\n    g4_buggy, _, _ = g_item_buggy(vc4, nl4)\n    print(f\"  4-model subset G_item (correct): {g4_correct:.6f}\", flush=True)\n    print(f\"  4-model subset G_item (buggy):   {g4_buggy:.6f}\", flush=True)\n    print(f\"  Original 4-model G_item:         0.728948\", flush=True)\n\n    results[\"step2b_4model_subset\"] = {\n        \"subset_correct_G\": round(g4_correct, 6),\n        \"subset_buggy_G\": round(g4_buggy, 6),\n        \"original_4model_G\": 0.728948,\n        \"match\": abs(g4_correct - 0.728948) < 0.01,\n    }\n\n    # === Step 3: Incremental model analysis (correct formula) ===\n    print(\"\\n=== Step 3: Incremental Model Addition ===\", flush=True)\n    add_order = [\"Llama-3.1-8B\", \"Mistral-7B-v0.3\", \"Qwen3-8B\", \"Gemma-2-9B\",\n                 \"InternLM2.5-7B\", \"DeepSeek-7B\", \"OLMo-2-7B\", \"Yi-1.5-9B\"]\n    incremental = []\n    for k in range(4, len(add_order) + 1):\n        models_k = add_order[:k]\n        df_k = df_gsm[df_gsm[\"model\"].isin(models_k)].reset_index(drop=True)\n        if df_k[\"model\"].nunique() < k:\n            print(f\"  {k} models: only {df_k['model'].nunique()} found, skip\")\n            continue\n        vc_k, nl_k = henderson_i(df_k)\n        g_c, si_c, sd_c = g_item_correct(vc_k, nl_k)\n        g_b, si_b, sd_b = g_item_buggy(vc_k, nl_k)\n        added = add_order[k-1] if k > 4 else \"base-4\"\n        total_var = sum(vc_k.values())\n        item_pct = vc_k[\"item_id\"] / total_var * 100 if total_var > 0 else 0\n        mi_pct = vc_k.get(\"model:item_id\", 0) / total_var * 100 if total_var > 0 else 0\n        res_pct = vc_k[\"residual\"] / total_var * 100 if total_var > 0 else 0\n        print(f\"  {k} models (+{added:20s}): G_correct={g_c:.4f}  G_buggy={g_b:.4f}  \"\n              f\"item%={item_pct:.1f}  m:i%={mi_pct:.1f}  res%={res_pct:.1f}\", flush=True)\n        incremental.append({\n            \"n_models\": k,\n            \"added_model\": added,\n            \"G_item_correct\": round(g_c, 6),\n            \"G_item_buggy\": round(g_b, 6),\n            \"sigma_item\": round(si_c, 8),\n            \"sigma_delta_correct\": round(sd_c, 8),\n            \"sigma_delta_buggy\": round(sd_b, 8),\n            \"item_pct\": round(item_pct, 2),\n            \"model_item_pct\": round(mi_pct, 2),\n            \"residual_pct\": round(res_pct, 2),\n        })\n    results[\"step3_incremental_gsm8k\"] = incremental\n\n    # === Step 4: Pairwise item accuracy correlations ===\n    print(\"\\n=== Step 4: Pairwise Item Accuracy Correlations (GSM8K) ===\", flush=True)\n    profiles, items = item_accuracy_profiles(df_gsm)\n    corr, corr_models = pairwise_correlations(profiles)\n    print(f\"  {'':20s}\", end=\"\")\n    for m in corr_models:\n        print(f\"  {m[:8]:>8s}\", end=\"\")\n    print()\n    for i, m in enumerate(corr_models):\n        print(f\"  {m:20s}\", end=\"\")\n        for j in range(len(corr_models)):\n            print(f\"  {corr[i,j]:8.3f}\", end=\"\")\n        print()\n\n    # Mean off-diagonal correlation\n    n_m = len(corr_models)\n    off_diag = [corr[i,j] for i in range(n_m) for j in range(n_m) if i != j]\n    mean_corr = np.mean(off_diag)\n    print(f\"\\n  Mean off-diagonal r = {mean_corr:.4f}\")\n\n    # Original 4 vs new 4 comparison\n    orig_idx = [i for i, m in enumerate(corr_models) if m in original_4]\n    new_idx = [i for i, m in enumerate(corr_models) if m not in original_4]\n    orig_corrs = [corr[i,j] for i in orig_idx for j in orig_idx if i != j]\n    cross_corrs = [corr[i,j] for i in orig_idx for j in new_idx]\n    new_corrs = [corr[i,j] for i in new_idx for j in new_idx if i != j]\n    print(f\"  Mean r (orig 4x4): {np.mean(orig_corrs):.4f}\")\n    print(f\"  Mean r (cross):    {np.mean(cross_corrs):.4f}\")\n    print(f\"  Mean r (new 4x4):  {np.mean(new_corrs):.4f}\")\n\n    results[\"step4_correlations\"] = {\n        \"models\": corr_models,\n        \"correlation_matrix\": [[round(corr[i,j], 4) for j in range(n_m)] for i in range(n_m)],\n        \"mean_off_diagonal\": round(mean_corr, 4),\n        \"mean_original_4\": round(np.mean(orig_corrs), 4),\n        \"mean_cross\": round(np.mean(cross_corrs), 4),\n        \"mean_new_4\": round(np.mean(new_corrs), 4),\n    }\n\n    # === Step 5: MMLU comparison ===\n    print(\"\\n=== Step 5: MMLU Incremental (Correct Formula) ===\", flush=True)\n    df_mmlu = load_benchmark_data(MMLU_FILES)\n    print(f\"  {len(df_mmlu)} rows, {df_mmlu['model'].nunique()} models\", flush=True)\n    mmlu_incremental = []\n    for k in range(4, len(add_order) + 1):\n        models_k = add_order[:k]\n        df_k = df_mmlu[df_mmlu[\"model\"].isin(models_k)].reset_index(drop=True)\n        actual_n = df_k[\"model\"].nunique()\n        if actual_n < 4:\n            continue\n        vc_k, nl_k = henderson_i(df_k)\n        g_c, _, _ = g_item_correct(vc_k, nl_k)\n        g_b, _, _ = g_item_buggy(vc_k, nl_k)\n        added = add_order[k-1] if k > 4 else \"base-4\"\n        print(f\"  {actual_n} models (+{added:20s}): G_correct={g_c:.4f}  G_buggy={g_b:.4f}\", flush=True)\n        mmlu_incremental.append({\n            \"n_models\": actual_n,\n            \"added_model\": added,\n            \"G_item_correct\": round(g_c, 6),\n            \"G_item_buggy\": round(g_b, 6),\n        })\n    results[\"step5_mmlu_incremental\"] = mmlu_incremental\n\n    # === Summary ===\n    results[\"conclusion\"] = {\n        \"root_cause\": \"BUG in exp004_ff_gstudy.py: compute_g_item divides residual by 1 instead of prod(non_item_facet_levels)\",\n        \"impact\": \"sigma_delta inflated ~2300x for residual term, causing G_item to appear much lower than reality\",\n        \"corrected_8model_gsm8k_G\": results[\"step2_bug_confirmation\"][\"eight_model_correct_G\"],\n        \"real_phenomenon\": \"After bug fix, 4→8 model G_item change is small and should be verified in step3\",\n    }\n\n    # Save\n    out_path = Path(\"results/exp004_8model_analysis/gitem_consistency_check.json\")\n    out_path.parent.mkdir(parents=True, exist_ok=True)\n    with open(out_path, \"w\") as f:\n        json.dump(results, f, indent=2, default=str)\n    print(f\"\\nSaved -> {out_path}\")\n    print(f\"Runtime: {time.time()-t0:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT\necho \"Script written OK\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat > /root/nlp_variance_gtheory/scripts/gitem_consistency_check.py << 'SCRIPT'\n\"\"\"G_item consistency diagnostic: 4-model vs 8-model GSM8K.\n\nRoot cause hypothesis: exp004_ff_gstudy.py has divisor=1 for residual in compute_g_item,\nwhile per_benchmark_gstudy.py correctly divides by prod(non_item_facet_levels).\n\"\"\"\nimport json\nimport sys\nimport time\nfrom itertools import combinations\nfrom math import prod\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\n\nsys.path.insert(0, str(Path(__file__).resolve().parents[1]))\nfrom src.config.model_paths import normalize_model_name\n\nFACETS = [\"model\", \"temperature\", \"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\nDATA_DIR = Path(\"results/exp002\")\nKEEP_COLS = [\"model\", \"temperature\", \"prompt_template\", \"seed\", \"ordering\", \"item_id\", \"correct\"]\n\nMODEL_ORDER = [\"Llama-3.1-8B\", \"Mistral-7B-v0.3\", \"Qwen3-8B\", \"Gemma-2-9B\",\n               \"InternLM2.5-7B\", \"DeepSeek-7B\", \"OLMo-2-7B\", \"Yi-1.5-9B\"]\n\nGSM8K_FILES = [\"llama_gsm8k\", \"mistral_gsm8k\", \"qwen_gsm8k\", \"gemma_gsm8k\",\n               \"internlm_gsm8k\", \"deepseek_gsm8k\", \"olmo_gsm8k\", \"yi_gsm8k\"]\n\nMMLU_FILES = [\"llama_mmlu\", \"mistral_mmlu\", \"qwen_mmlu\", \"gemma_mmlu\",\n              \"internlm_mmlu\", \"deepseek_mmlu\", \"olmo_mmlu\", \"yi_mmlu\"]\n\n\ndef load_benchmark_data(benchmark_files):\n    frames = []\n    for fname in benchmark_files:\n        fpath = DATA_DIR / f\"{fname}.jsonl\"\n        if not fpath.exists():\n            print(f\"  SKIP {fpath}\")\n            continue\n        df = pd.read_json(fpath, lines=True)\n        if \"_placeholder\" in df.columns:\n            df = df[df[\"_placeholder\"] != True]\n        if \"top_logprobs\" in df.columns:\n            df.drop(columns=[\"top_logprobs\"], inplace=True)\n        df[\"model\"] = df[\"model\"].map(normalize_model_name).fillna(df[\"model\"])\n        for f in FACETS:\n            df[f] = df[f].astype(str)\n        frames.append(df[KEEP_COLS])\n    return pd.concat(frames, ignore_index=True)\n\n\ndef henderson_i(df):\n    grand_mean = df[\"correct\"].mean()\n    N = len(df)\n    n_levels = {f: df[f].nunique() for f in FACETS}\n    effects = {}\n\n    for f in FACETS:\n        gm = df.groupby(f, observed=True)[\"correct\"].mean()\n        n_per = N // n_levels[f]\n        ss = float(n_per * ((gm - grand_mean) ** 2).sum())\n        dof = n_levels[f] - 1\n        effects[f] = {\"ss\": ss, \"df\": dof, \"ms\": ss / dof if dof > 0 else 0.0}\n\n    for fi, fj in combinations(FACETS, 2):\n        cm = df.groupby([fi, fj], observed=True)[\"correct\"].mean()\n        mi = df.groupby(fi, observed=True)[\"correct\"].mean()\n        mj = df.groupby(fj, observed=True)[\"correct\"].mean()\n        n_per = N // (n_levels[fi] * n_levels[fj])\n        ss = 0.0\n        for (li, lj), val in cm.items():\n            ss += n_per * (val - mi[li] - mj[lj] + grand_mean) ** 2\n        dof = (n_levels[fi] - 1) * (n_levels[fj] - 1)\n        effects[f\"{fi}:{fj}\"] = {\"ss\": ss, \"df\": dof, \"ms\": ss / dof if dof > 0 else 0.0}\n\n    ss_total = float(((df[\"correct\"] - grand_mean) ** 2).sum())\n    ss_model_sum = sum(e[\"ss\"] for e in effects.values())\n    ss_res = max(0.0, ss_total - ss_model_sum)\n    df_res = N - 1 - sum(e[\"df\"] for e in effects.values())\n    effects[\"residual\"] = {\"ss\": ss_res, \"df\": df_res, \"ms\": ss_res / df_res if df_res > 0 else 0.0}\n\n    ms_res = effects[\"residual\"][\"ms\"]\n    vc = {}\n    for fi, fj in combinations(FACETS, 2):\n        key = f\"{fi}:{fj}\"\n        coeff = prod(n_levels[f] for f in FACETS if f not in (fi, fj))\n        vc[key] = max(0.0, (effects[key][\"ms\"] - ms_res) / coeff if coeff > 0 else 0.0)\n\n    for fi in FACETS:\n        coeff_main = prod(n_levels[f] for f in FACETS if f != fi)\n        ic = 0.0\n        for fj in FACETS:\n            if fj == fi:\n                continue\n            ik = f\"{fi}:{fj}\" if f\"{fi}:{fj}\" in vc else f\"{fj}:{fi}\"\n            cij = prod(n_levels[f] for f in FACETS if f not in (fi, fj))\n            ic += cij * vc[ik]\n        vc[fi] = max(0.0, (effects[fi][\"ms\"] - ic - ms_res) / coeff_main if coeff_main > 0 else 0.0)\n\n    vc[\"residual\"] = ms_res\n    return vc, n_levels\n\n\ndef g_item_correct(vc, n_levels):\n    \"\"\"Correct formula: residual / prod(non_item_facets).\"\"\"\n    non_item = [f for f in FACETS if f != \"item_id\"]\n    sigma_item = vc.get(\"item_id\", 0.0)\n    sigma_delta = 0.0\n    for key, est in vc.items():\n        if est == 0.0 or key == \"item_id\":\n            continue\n        if key == \"residual\":\n            sigma_delta += est / prod(n_levels[f] for f in non_item)\n            continue\n        parts = set(key.split(\":\"))\n        if \"item_id\" not in parts:\n            continue\n        other = [p for p in parts if p != \"item_id\"]\n        sigma_delta += est / (prod(n_levels[o] for o in other) if other else 1)\n    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0\n    return g, sigma_item, sigma_delta\n\n\ndef g_item_buggy(vc, n_levels):\n    \"\"\"Buggy formula from exp004_ff_gstudy.py: residual / 1.\"\"\"\n    sigma_item = vc.get(\"item_id\", 0.0)\n    sigma_delta = 0.0\n    for key, est in vc.items():\n        if key == \"item_id\":\n            continue\n        parts = key.split(\":\")\n        other = [p for p in parts if p != \"item_id\"]\n        if \"item_id\" not in parts and key != \"residual\":\n            continue\n        if key == \"residual\":\n            divisor = 1\n        else:\n            divisor = prod(n_levels[o] for o in other) if other else 1\n        sigma_delta += est / divisor\n    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0\n    return g, sigma_item, sigma_delta\n\n\ndef item_accuracy_profiles(df):\n    \"\"\"Per-model item accuracy vector (200 items).\"\"\"\n    items = sorted(df[\"item_id\"].unique())\n    models = sorted(df[\"model\"].unique())\n    profiles = {}\n    for m in models:\n        acc = df[df[\"model\"] == m].groupby(\"item_id\")[\"correct\"].mean()\n        profiles[m] = np.array([acc.get(i, np.nan) for i in items])\n    return profiles, items\n\n\ndef pairwise_correlations(profiles):\n    models = sorted(profiles.keys())\n    n = len(models)\n    corr = np.zeros((n, n))\n    for i in range(n):\n        for j in range(n):\n            mask = ~(np.isnan(profiles[models[i]]) | np.isnan(profiles[models[j]]))\n            corr[i, j] = np.corrcoef(profiles[models[i]][mask], profiles[models[j]][mask])[0, 1]\n    return corr, models\n\n\ndef main():\n    t0 = time.time()\n    results = {}\n\n    # === Step 1: Load all GSM8K data ===\n    print(\"Loading GSM8K data...\", flush=True)\n    df_gsm = load_benchmark_data(GSM8K_FILES)\n    print(f\"  {len(df_gsm)} rows, {df_gsm['model'].nunique()} models\", flush=True)\n    print(f\"  Models: {sorted(df_gsm['model'].unique())}\", flush=True)\n\n    # === Step 2: Bug confirmation ===\n    print(\"\\n=== Bug Confirmation: 8-model GSM8K ===\", flush=True)\n    vc8, nl8 = henderson_i(df_gsm)\n    g_correct, st_c, sd_c = g_item_correct(vc8, nl8)\n    g_buggy, st_b, sd_b = g_item_buggy(vc8, nl8)\n\n    non_item_prod = prod(nl8[f] for f in FACETS if f != \"item_id\")\n    print(f\"  residual = {vc8['residual']:.6f}\", flush=True)\n    print(f\"  prod(non_item) = {non_item_prod}\", flush=True)\n    print(f\"  residual/prod = {vc8['residual']/non_item_prod:.8f}\", flush=True)\n    print(f\"  residual/1    = {vc8['residual']:.8f}\", flush=True)\n    print(f\"  G_item (correct, /prod): {g_correct:.6f}  sigma_delta={sd_c:.8f}\", flush=True)\n    print(f\"  G_item (buggy, /1):      {g_buggy:.6f}  sigma_delta={sd_b:.8f}\", flush=True)\n    print(f\"  Reported 8-model G_item: 0.283713\", flush=True)\n    print(f\"  Reported 4-model G_item: 0.728948\", flush=True)\n\n    results[\"step2_bug_confirmation\"] = {\n        \"eight_model_correct_G\": round(g_correct, 6),\n        \"eight_model_buggy_G\": round(g_buggy, 6),\n        \"reported_8model_G\": 0.283713,\n        \"reported_4model_G\": 0.728948,\n        \"residual\": round(vc8[\"residual\"], 10),\n        \"prod_non_item\": non_item_prod,\n        \"bug_location\": \"exp004_ff_gstudy.py:compute_g_item line ~120, divisor=1 for residual\",\n        \"correct_divisor\": f\"prod(non_item_facets) = {non_item_prod}\",\n    }\n\n    # === Step 2b: 4-model subset verification ===\n    print(\"\\n=== 4-Model Subset Verification ===\", flush=True)\n    original_4 = [\"Llama-3.1-8B\", \"Mistral-7B-v0.3\", \"Qwen3-8B\", \"Gemma-2-9B\"]\n    df_4sub = df_gsm[df_gsm[\"model\"].isin(original_4)].reset_index(drop=True)\n    vc4, nl4 = henderson_i(df_4sub)\n    g4_correct, _, _ = g_item_correct(vc4, nl4)\n    g4_buggy, _, _ = g_item_buggy(vc4, nl4)\n    print(f\"  4-model subset G_item (correct): {g4_correct:.6f}\", flush=True)\n    print(f\"  4-model subset G_item (buggy):   {g4_buggy:.6f}\", flush=True)\n    print(f\"  Original 4-model G_item:         0.728948\", flush=True)\n\n    results[\"step2b_4model_subset\"] = {\n        \"subset_correct_G\": round(g4_correct, 6),\n        \"subset_buggy_G\": round(g4_buggy, 6),\n        \"original_4model_G\": 0.728948,\n        \"match\": abs(g4_correct - 0.728948) < 0.01,\n    }\n\n    # === Step 3: Incremental model analysis (correct formula) ===\n    print(\"\\n=== Step 3: Incremental Model Addition ===\", flush=True)\n    add_order = [\"Llama-3.1-8B\", \"Mistral-7B-v0.3\", \"Qwen3-8B\", \"Gemma-2-9B\",\n                 \"InternLM2.5-7B\", \"DeepSeek-7B\", \"OLMo-2-7B\", \"Yi-1.5-9B\"]\n    incremental = []\n    for k in range(4, len(add_order) + 1):\n        models_k = add_order[:k]\n        df_k = df_gsm[df_gsm[\"model\"].isin(models_k)].reset_index(drop=True)\n        if df_k[\"model\"].nunique() < k:\n            print(f\"  {k} models: only {df_k['model'].nunique()} found, skip\")\n            continue\n        vc_k, nl_k = henderson_i(df_k)\n        g_c, si_c, sd_c = g_item_correct(vc_k, nl_k)\n        g_b, si_b, sd_b = g_item_buggy(vc_k, nl_k)\n        added = add_order[k-1] if k > 4 else \"base-4\"\n        total_var = sum(vc_k.values())\n        item_pct = vc_k[\"item_id\"] / total_var * 100 if total_var > 0 else 0\n        mi_pct = vc_k.get(\"model:item_id\", 0) / total_var * 100 if total_var > 0 else 0\n        res_pct = vc_k[\"residual\"] / total_var * 100 if total_var > 0 else 0\n        print(f\"  {k} models (+{added:20s}): G_correct={g_c:.4f}  G_buggy={g_b:.4f}  \"\n              f\"item%={item_pct:.1f}  m:i%={mi_pct:.1f}  res%={res_pct:.1f}\", flush=True)\n        incremental.append({\n            \"n_models\": k,\n            \"added_model\": added,\n            \"G_item_correct\": round(g_c, 6),\n            \"G_item_buggy\": round(g_b, 6),\n            \"sigma_item\": round(si_c, 8),\n            \"sigma_delta_correct\": round(sd_c, 8),\n            \"sigma_delta_buggy\": round(sd_b, 8),\n            \"item_pct\": round(item_pct, 2),\n            \"model_item_pct\": round(mi_pct, 2),\n            \"residual_pct\": round(res_pct, 2),\n        })\n    results[\"step3_incremental_gsm8k\"] = incremental\n\n    # === Step 4: Pairwise item accuracy correlations ===\n    print(\"\\n=== Step 4: Pairwise Item Accuracy Correlations (GSM8K) ===\", flush=True)\n    profiles, items = item_accuracy_profiles(df_gsm)\n    corr, corr_models = pairwise_correlations(profiles)\n    print(f\"  {'':20s}\", end=\"\")\n    for m in corr_models:\n        print(f\"  {m[:8]:>8s}\", end=\"\")\n    print()\n    for i, m in enumerate(corr_models):\n        print(f\"  {m:20s}\", end=\"\")\n        for j in range(len(corr_models)):\n            print(f\"  {corr[i,j]:8.3f}\", end=\"\")\n        print()\n\n    # Mean off-diagonal correlation\n    n_m = len(corr_models)\n    off_diag = [corr[i,j] for i in range(n_m) for j in range(n_m) if i != j]\n    mean_corr = np.mean(off_diag)\n    print(f\"\\n  Mean off-diagonal r = {mean_corr:.4f}\")\n\n    # Original 4 vs new 4 comparison\n    orig_idx = [i for i, m in enumerate(corr_models) if m in original_4]\n    new_idx = [i for i, m in enumerate(corr_models) if m not in original_4]\n    orig_corrs = [corr[i,j] for i in orig_idx for j in orig_idx if i != j]\n    cross_corrs = [corr[i,j] for i in orig_idx for j in new_idx]\n    new_corrs = [corr[i,j] for i in new_idx for j in new_idx if i != j]\n    print(f\"  Mean r (orig 4x4): {np.mean(orig_corrs):.4f}\")\n    print(f\"  Mean r (cross):    {np.mean(cross_corrs):.4f}\")\n    print(f\"  Mean r (new 4x4):  {np.mean(new_corrs):.4f}\")\n\n    results[\"step4_correlations\"] = {\n        \"models\": corr_models,\n        \"correlation_matrix\": [[round(corr[i,j], 4) for j in range(n_m)] for i in range(n_m)],\n        \"mean_off_diagonal\": round(mean_corr, 4),\n        \"mean_original_4\": round(np.mean(orig_corrs), 4),\n        \"mean_cross\": round(np.mean(cross_corrs), 4),\n        \"mean_new_4\": round(np.mean(new_corrs), 4),\n    }\n\n    # === Step 5: MMLU comparison ===\n    print(\"\\n=== Step 5: MMLU Incremental (Correct Formula) ===\", flush=True)\n    df_mmlu = load_benchmark_data(MMLU_FILES)\n    print(f\"  {len(df_mmlu)} rows, {df_mmlu['model'].nunique()} models\", flush=True)\n    mmlu_incremental = []\n    for k in range(4, len(add_order) + 1):\n        models_k = add_order[:k]\n        df_k = df_mmlu[df_mmlu[\"model\"].isin(models_k)].reset_index(drop=True)\n        actual_n = df_k[\"model\"].nunique()\n        if actual_n < 4:\n            continue\n        vc_k, nl_k = henderson_i(df_k)\n        g_c, _, _ = g_item_correct(vc_k, nl_k)\n        g_b, _, _ = g_item_buggy(vc_k, nl_k)\n        added = add_order[k-1] if k > 4 else \"base-4\"\n        print(f\"  {actual_n} models (+{added:20s}): G_correct={g_c:.4f}  G_buggy={g_b:.4f}\", flush=True)\n        mmlu_incremental.append({\n            \"n_models\": actual_n,\n            \"added_model\": added,\n            \"G_item_correct\": round(g_c, 6),\n            \"G_item_buggy\": round(g_b, 6),\n        })\n    results[\"step5_mmlu_incremental\"] = mmlu_incremental\n\n    # === Summary ===\n    results[\"conclusion\"] = {\n        \"root_cause\": \"BUG in exp004_ff_gstudy.py: compute_g_item divides residual by 1 instead of prod(non_item_facet_levels)\",\n        \"impact\": \"sigma_delta inflated ~2300x for residual term, causing G_item to appear much lower than reality\",\n        \"corrected_8model_gsm8k_G\": results[\"step2_bug_confirmation\"][\"eight_model_correct_G\"],\n        \"real_phenomenon\": \"After bug fix, 4→8 model G_item change is small and should be verified in step3\",\n    }\n\n    # Save\n    out_path = Path(\"results/exp004_8model_analysis/gitem_consistency_check.json\")\n    out_path.parent.mkdir(parents=True, exist_ok=True)\n    with open(out_path, \"w\") as f:\n        json.dump(results, f, indent=2, default=str)\n    print(f\"\\nSaved -> {out_path}\")\n    print(f\"Runtime: {time.time()-t0:.1f}s\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT\necho \"Script written OK\""
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-21T23:10:45.924279+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-21T23:10:45.924426+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32570",
  "command": "cd /root/nlp_variance_gtheory && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export PYTHONPATH=/root/nlp_variance_gtheory:$PYTHONPATH && python scripts/gitem_consistency_check.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32570",
    "command": "cd /root/nlp_variance_gtheory && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export PYTHONPATH=/root/nlp_variance_gtheory:$PYTHONPATH && python scripts/gitem_consistency_check.py"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-21T23:10:45.924580+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading GSM8K data...\\n  460800 rows, 8 models\\n  Models: ['DeepSeek-7B', 'Gemma-2-9B', 'InternLM2.5-7B', 'Llama-3.1-8B', 'Mistral-7B-v0.3', 'OLMo-2-7B', 'Qwen3-8B', 'Yi-1.5-9B']\\n\\n=== Bug Confirmation: 8-model GSM8K ===\\n  residual = 0.099644\\n  prod(non_item) = 2304\\n  residual/prod = 0.00004325\\n  residual/1    = 0.09964418\\n  G_item (correct, /prod): 0.862852  sigma_delta=0.00669189\\n  G_item (buggy, /1):      0.283713  sigma_delta=0.10629283\\n  Reported 8-model G_item: 0.283713\\n  Reported 4-model G_item: 0.728948\\n\\n=== 4-Model Subset Verification ===\\n  4-model subset G_item (correct): 0.728948\\n  4-model subset G_item (buggy):   0.246158\\n  Original 4-model G_item:         0.728948\\n\\n=== Step 3: Incremental Model Addition ===\\n  4 models (+base-4              ): G_correct=0.7289  G_buggy=0.2462  item%=12.0  m:i%=12.1  res%=32.3\\n  5 models (+InternLM2.5-7B      ): G_correct=0.7916  G_buggy=0.2666  item%=14.3  m:i%=12.2  res%=35.7\\n  6 models (+DeepSeek-7B         ): G_correct=0.8111  G_buggy=0.2589  item%=14.6  m:i%=13.5  res%=38.4\\n  7 models (+OLMo-2-7B           ): G_correct=0.8412  G_buggy=0.2835  item%=16.5  m:i%=15.2  res%=38.5\\n  8 models (+Yi-1.5-9B           ): G_correct=0.8629  G_buggy=0.2837  item%=16.9  m:i%=14.6  res%=39.9\\n\\n=== Step 4: Pairwise Item Accuracy Correlations (GSM8K) ===\\n                        DeepSeek  Gemma-2-  InternLM  Llama-3.  Mistral-  OLMo-2-7  Qwen3-8B  Yi-1.5-9\\n  DeepSeek-7B              1.000     0.445     0.528     0.632     0.662     0.506     0.196     0.463\\n  Gemma-2-9B               0.445     1.000     0.712     0.722     0.512     0.536     0.530     0.758\\n  InternLM2.5-7B           0.528     0.712     1.000     0.697     0.534     0.608     0.488     0.723\\n  Llama-3.1-8B             0.632     0.722     0.697     1.000     0.637     0.653     0.417     0.690\\n  Mistral-7B-v0.3          0.662     0.512     0.534     0.637
…[truncated 1233 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-21T23:10:45.924767+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "G_item Consistency Diagnostic",
  "type": "data",
  "description": "G_item 4→8 model consistency check for GSM8K. Confirmed root cause is a bug in exp004_ff_gstudy.py (residual divisor=1 instead of prod(non_item_facets)=2304). Corrected 8-model G_item=0.863, not 0.284.",
  "project": "nlp_variance_gtheory",
  "exp_id": "exp004",
  "source_path": "/root/nlp_variance_gtheory/results/exp004_8model_analysis/gitem_consistency_check.json",
  "tags": "['gtheory', 'g_item', 'bug', 'diagnostic']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "G_item Consistency Diagnostic",
    "type": "data",
    "description": "G_item 4→8 model consistency check for GSM8K. Confirmed root cause is a bug in exp004_ff_gstudy.py (residual divisor=1 instead of prod(non_item_facets)=2304). Corrected 8-model G_item=0.863, not 0.284.",
    "project": "nlp_variance_gtheory",
    "exp_id": "exp004",
    "source_path": "/root/nlp_variance_gtheory/results/exp004_8model_analysis/gitem_consistency_check.json",
    "tags": "['gtheory', 'g_item', 'bug', 'diagnostic']"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-21T23:10:45.924904+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/nlp_variance_gtheory/results/exp004_8model_analysis/gitem_consistency_check.json\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-21T23:10:45.925020+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /root/nlp_variance_gtheory/results/exp004_8model_analysis/gitem_consistency_check.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /root/nlp_variance_gtheory/results/exp004_8model_analysis/gitem_consistency_check.json"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-21T23:10:45.925224+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"step2_bug_confirmation\\\": {\\n    \\\"eight_model_correct_G\\\": 0.862852,\\n    \\\"eight_model_buggy_G\\\": 0.283713,\\n    \\\"reported_8model_G\\\": 0.283713,\\n    \\\"reported_4model_G\\\": 0.728948,\\n    \\\"residual\\\": 0.0996441838,\\n    \\\"prod_non_item\\\": 2304,\\n    \\\"bug_location\\\": \\\"exp004_ff_gstudy.py:compute_g_item line ~120, divisor=1 for residual\\\",\\n    \\\"correct_divisor\\\": \\\"prod(non_item_facets) = 2304\\\"\\n  },\\n  \\\"step2b_4model_subset\\\": {\\n    \\\"subset_correct_G\\\": 0.728948,\\n    \\\"subset_buggy_G\\\": 0.246158,\\n    \\\"original_4model_G\\\": 0.728948,\\n    \\\"match\\\": \\\"True\\\"\\n  },\\n  \\\"step3_incremental_gsm8k\\\": [\\n    {\\n      \\\"n_models\\\": 4,\\n      \\\"added_model\\\": \\\"base-4\\\",\\n      \\\"G_item_correct\\\": 0.728948,\\n      \\\"G_item_buggy\\\": 0.246158,\\n      \\\"sigma_item\\\": 0.0316303,\\n      \\\"sigma_delta_correct\\\": 0.01176141,\\n      \\\"sigma_delta_buggy\\\": 0.09686541,\\n      \\\"item_pct\\\": 11.99,\\n      \\\"model_item_pct\\\": 12.09,\\n      \\\"residual_pct\\\": 32.29\\n    },\\n    {\\n      \\\"n_models\\\": 5,\\n      \\\"added_model\\\": \\\"InternLM2.5-7B\\\",\\n      \\\"G_item_correct\\\": 0.791584,\\n      \\\"G_item_buggy\\\": 0.266621,\\n      \\\"sigma_item\\\": 0.03664521,\\n      \\\"sigma_delta_correct\\\": 0.00964831,\\n      \\\"sigma_delta_buggy\\\": 0.10079792,\\n      \\\"item_pct\\\": 14.34,\\n      \\\"model_item_pct\\\": 12.16,\\n      \\\"residual_pct\\\": 35.69\\n    },\\n    {\\n      \\\"n_models\\\": 6,\\n      \\\"added_model\\\": \\\"DeepSeek-7B\\\",\\n      \\\"G_item_correct\\\": 0.811136,\\n      \\\"G_item_buggy\\\": 0.258936,\\n      \\\"sigma_item\\\": 0.037548,\\n      \\\"sigma_delta_correct\\\": 0.00874263,\\n      \\\"sigma_delta_buggy\\\": 0.10746075,\\n      \\\"item_pct\\\": 14.58,\\n      \\\"model_item_pct\\\": 13.48,\\n      \\\"res
…[truncated 4158 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-21T23:10:45.925415+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "G_item Consistency Diagnostic",
  "type": "data",
  "description": "G_item 4→8 model consistency check for GSM8K. Confirmed root cause is a bug in exp004_ff_gstudy.py (residual divisor=1 instead of prod(non_item_facets)=2304). Corrected 8-model G_item=0.863, not 0.284.",
  "project": "nlp_variance_gtheory",
  "exp_id": "exp004",
  "content_filename": "gitem_consistency_check.json",
  "content": "{\n  \"step2_bug_confirmation\": {\n    \"eight_model_correct_G\": 0.862852,\n    \"eight_model_buggy_G\": 0.283713,\n    \"reported_8model_G\": 0.283713,\n    \"reported_4model_G\": 0.728948,\n    \"residual\": 0.0996441838,\n    \"prod_non_item\": 2304,\n    \"bug_location\": \"exp004_ff_gstudy.py:compute_g_item line ~120, divisor=1 for residual\",\n    \"correct_divisor\": \"prod(non_item_facets) = 2304\"\n  },\n  \"step2b_4model_subset\": {\n    \"subset_correct_G\": 0.728948,\n    \"subset_buggy_G\": 0.246158,\n    \"original_4model_G\": 0.728948,\n    \"match\": true\n  },\n  \"conclusion\": {\n    \"root_cause\": \"BUG in exp004_ff_gstudy.py: compute_g_item divides residual by 1 instead of prod(non_item_facet_levels)\",\n    \"impact\": \"sigma_delta inflated ~2300x for residual term\",\n    \"corrected_8model_gsm8k_G\": 0.862852,\n    \"real_trend\": \"G_item INCREASES 0.729→0.863 with more models (opposite of reported drop)\"\n  }\n}",
  "tags": "['gtheory', 'g_item', 'bug', 'diagnostic']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "G_item Consistency Diagnostic",
    "type": "data",
    "description": "G_item 4→8 model consistency check for GSM8K. Confirmed root cause is a bug in exp004_ff_gstudy.py (residual divisor=1 instead of prod(non_item_facets)=2304). Corrected 8-model G_item=0.863, not 0.284.",
    "project": "nlp_variance_gtheory",
    "exp_id": "exp004",
    "content_filename": "gitem_consistency_check.json",
    "content": "{\n  \"step2_bug_confirmation\": {\n    \"eight_model_correct_G\": 0.862852,\n    \"eight_model_buggy_G\": 0.283713,\n    \"reported_8model_G\": 0.283713,\n    \"reported_4model_G\": 0.728948,\n    \"residual\": 0.0996441838,\n    \"prod_non_item\": 2304,\n    \"bug_location\": \"exp004_ff_gstudy.py:compute_g_item line ~120, divisor=1 for residual\",\n    \"correct_divisor\": \"prod(non_item_facets) = 2304\"\n  },\n  \"step2b_4model_subset\": {\n    \"subset_correct_G\": 0.728948,\n    \"subset_buggy_G\": 0.246158,\n    \"original_4model_G\": 0.728948,\n    \"match\": true\n  },\n  \"conclusion\": {\n    \"root_cause\": \"BUG in exp004_ff_gstudy.py: compute_g_item divides residual by 1 instead of prod(non_item_facet_levels)\",\n    \"impact\": \"sigma_delta inflated ~2300x for residual term\",\n    \"corrected_8model_gsm8k_G\": 0.862852,\n    \"real_trend\": \"G_item INCREASES 0.729→0.863 with more models (opposite of reported drop)\"\n  }\n}",
    "tags": "['gtheory', 'g_item', 'bug', 'diagnostic']"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-21T23:10:45.925565+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'step2_bug_confirmation'...ite of reported drop)'}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-21T23:10:45.925686+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "G_item Consistency Diagnostic",
  "type": "data",
  "description": "G_item 4-to-8 model consistency check for GSM8K. Root cause: bug in exp004_ff_gstudy.py (residual divisor=1 instead of 2304). Corrected 8-model G_item=0.863, not 0.284. G actually increases with more models.",
  "project": "nlp_variance_gtheory",
  "exp_id": "exp004",
  "content": "See server file: results/exp004_8model_analysis/gitem_consistency_check.json",
  "content_filename": "gitem_consistency_check_pointer.txt",
  "tags": "['gtheory', 'g_item', 'bug', 'diagnostic']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "G_item Consistency Diagnostic",
    "type": "data",
    "description": "G_item 4-to-8 model consistency check for GSM8K. Root cause: bug in exp004_ff_gstudy.py (residual divisor=1 instead of 2304). Corrected 8-model G_item=0.863, not 0.284. G actually increases with more models.",
    "project": "nlp_variance_gtheory",
    "exp_id": "exp004",
    "content": "See server file: results/exp004_8model_analysis/gitem_consistency_check.json",
    "content_filename": "gitem_consistency_check_pointer.txt",
    "tags": "['gtheory', 'g_item', 'bug', 'diagnostic']"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-21T23:10:45.925822+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_be3767\", \"name\": \"G_item Consistency Diagnostic\", \"type\": \"data\", \"description\": \"G_item 4-to-8 model consistency check for GSM8K. Root cause: bug in exp004_ff_gstudy.py (residual divisor=1 instead of 2304). Corrected 8-model G_item=0.863, not 0.284. G actually increases with more models.\", \"path\": \"projects/nlp_variance_gtheory/artifacts/exp004/data/gitem_consistency_check_pointer.txt\", \"url\": null, \"project\": \"nlp_variance_gtheory\", \"exp_id\": \"exp004\", \"skill\": \"\", \"created_at\": \"2026-05-21T23:10:29.438071+00:00\", \"tags\": [\"gtheory\", \"g_item\", \"bug\", \"diagnostic\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 73 · 2026-05-21T23:10:45.925990+00:00_

## 诊断结论

**根本原因：`exp004_ff_gstudy.py` 中的 bug**

`compute_g_item` 函数（约第120行）将 residual 除以 `1` 而非 `prod(non_item_facet_levels) = 2304`，导致 σ²(δ) 被膨胀约 2300 倍。

### Step 1: Facet 结构对比

| | 4-model 脚本 | 8-model FF 脚本 |
|---|---|---|
| Facets | model/temp/prompt/seed/ordering/item_id | 相同 |
| Henderson I | 相同实现 | 相同实现 |
| **residual in G_item** | **`÷ prod(non_item) = 1152`** | **`÷ 1` ← BUG** |

### Step 2: Bug 确认

| | G_item |
|---|---|
| 8-model buggy (÷1) | **0.2837** ← 匹配报告值 |
| 8-model correct (÷2304) | **0.8629** |
| 4-model subset (correct) | **0.7289** ← 精确匹配原值 |

### Step 3: 逐步加模型（correct 公式）

| Models | G_item | Δ |
|---|---|---|
| 4 (base) | 0.7289 | — |
| 5 (+InternLM) | 0.7916 | +0.063 |
| 6 (+DeepSeek) | 0.8111 | +0.020 |
| 7 (+OLMo) | 0.8412 | +0.030 |
| 8 (+Yi) | 0.8629 | +0.022 |

G_item **单调递增**，与报告的骤降完全相反。MMLU 同样趋势（0.816→0.896）。

### Step 4: Pairwise 相关

- 原4模型平均 r = 0.518
- 新4模型平均 r = 0.558
- 跨组平均 r = 0.564
- Qwen3-8B 与 DeepSeek 相关最低（r=0.196）

### 需要修复

`scripts/exp004_ff_gstudy.py` 第 ~120 行和 ~145 行，`compute_g_item` 和 `d_study_curve` 中：
```python
# 错误：
if key == "residual":
    divisor = 1
# 应改为：
if key == "residual":
    non_item = [f for f in FACETS if f != "item_id"]
    divisor = prod(n_levels[f] for f in non_item)
```

JSON 已保存到 `results/exp004_8model_analysis/gitem_consistency_check.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_phase2_gitem_consistency_check_20260521T230320"
}
```

</details>

---
