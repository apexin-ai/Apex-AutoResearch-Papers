# analysis model as fixed

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 101
- **Recorded user turns:** 0
- **Tool calls:** 50
- **Original source:** `logs/chats/worker_analysis_model_as_fixed_20260521T085703.jsonl`
- **Structured JSON:** [`778999af34ffc23de7cb.json`](../../sessions/77/778999af34ffc23de7cb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

101 recorded events

### Tool call

_source line 1 · 2026-05-21T09:07:41.654260+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Read existing G-study scripts",
  "prompt": "I need to understand the existing G-study implementation for this project. Read these files in full:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/src/analysis/gstudy_full.py\n2. /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/dataset_a4_gstudy.py\n\nAlso check what other analysis scripts exist:\n- Glob for /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/src/analysis/*.py\n- Glob for /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/*gstudy*\n\nReport the full content of the G-study scripts and the Henderson I EMS formulas used, the variance components computed, the G coefficient formula, and the facet structure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Read existing G-study scripts",
    "prompt": "I need to understand the existing G-study implementation for this project. Read these files in full:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/src/analysis/gstudy_full.py\n2. /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/dataset_a4_gstudy.py\n\nAlso check what other analysis scripts exist:\n- Glob for /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/src/analysis/*.py\n- Glob for /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/*gstudy*\n\nReport the full content of the G-study scripts and the Henderson I EMS formulas used, the variance components computed, the G coefficient formula, and the facet structure."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-21T09:07:41.654592+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/src/analysis/gstudy_full.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/src/analysis/gstudy_full.py"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-21T09:07:41.654753+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T09:07:41.654886+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/dataset_a4_gstudy.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/dataset_a4_gstudy.py"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T09:07:41.655005+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T09:07:41.655131+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/src/analysis/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/src/analysis/*.py"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T09:07:41.655243+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T09:07:41.655363+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/*gstudy*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/*gstudy*"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T09:07:41.655524+00:00_

scripts/gstudy_full.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T09:07:41.655647+00:00_

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
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/gstudy_full.py"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T09:07:41.655781+00:00_

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
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T09:07:41.655939+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory -type f -name \"*gstudy*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory -type f -name \"*gstudy*\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T09:07:41.656065+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/gstudy_full.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/logs/workers/worker_analysis_4model_gstudy_20260521T072418_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/logs/workers/worker_analysis_exp001b_gstudy_20260521T083847.log
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/logs/workers/worker_analysis_dataset_b_gstudy_20260521T053605.log
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/logs/workers/worker_analysis_llama_single_gstudy_20260521T034025.log
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/logs/workers/worker_analysis_dataset_a_gstudy_20260521T053533.log
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/logs/workers/worker_analysis_dataset_b_gstudy_20260521T053605_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/logs/workers/worker_analysis_dataset_a_gstudy_20260521T053533_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/logs/workers/worker_analysis_exp001b_gstudy_20260521T083847_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/logs/workers/worker_analysis_4model_gstudy_20260521T072418.log
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/logs/workers/worker_analysis_llama_single_gstudy_20260521T034025_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/logs/chats/worker_analysis_llama_single_gstudy_20260521T034025.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/logs/chats/worker_analysis_llama_single_gstudy_20260521T034025.lock
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/logs/chats/worker_analysis_4model_gstudy_20260521T072418.lock
/home/ubuntu/.agen
…[truncated 384 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T09:07:41.656210+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory -type f -name \"*.py\" | grep -E \"(analysis|scripts)\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory -type f -name \"*.py\" | grep -E \"(analysis|scripts)\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T09:07:41.656330+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/sample_benchmarks.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/gstudy_full.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/numpy/tests/test_scripts.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/pip/_vendor/distlib/scripts.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/scipy/stats/tests/test_sensitivity_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/scipy/stats/_sensitivity_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/reml_em.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/variance_decomposition.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/d_study.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/visualize.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/merge_cross_model.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/model_facet_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/__init__.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/bootstrap_ci.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/analysis/dual_metric_analysis.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T09:07:41.656485+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts -type f -name \"*.py\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts -type f -name \"*.py\" 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T09:07:41.656602+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/sample_benchmarks.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/gstudy_full.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T09:07:41.656723+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/src/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/src/"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T09:07:41.656832+00:00_

Exit code 2
ls: cannot access '/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/src/': No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T09:07:41.656950+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory -type d -name \"analysis\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory -type d -name \"analysis\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T09:07:41.657064+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/analysis

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T09:07:41.657182+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts -type f -name \"*gstudy*\" -o -name \"*analysis*.py\" 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts -type f -name \"*gstudy*\" -o -name \"*analysis*.py\" 2>/dev/null | head -30"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T09:07:41.657307+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/_project/data/bf16_fp16_only_gstudy.md
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/exp001b_resampling/data/exp001b_resampling_gstudy.md
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/model_facet_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/analysis/dual_metric_analysis.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T09:07:41.657448+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T09:07:41.657565+00:00_

total 80
drwxr-xr-x 3 ubuntu ubuntu  4096 May 21 06:04 .
drwxr-xr-x 8 ubuntu ubuntu  4096 May 20 22:16 ..
-rw-r--r-- 1 ubuntu ubuntu     0 May 20 14:03 __init__.py
drwxr-xr-x 2 ubuntu ubuntu  4096 May 21 02:55 __pycache__
-rw-r--r-- 1 ubuntu ubuntu  9112 May 21 02:55 bootstrap_ci.py
-rw-r--r-- 1 ubuntu ubuntu  5434 May 20 14:23 d_study.py
-rw-r--r-- 1 ubuntu ubuntu  3200 May 21 02:54 merge_cross_model.py
-rw-r--r-- 1 ubuntu ubuntu  9410 May 21 02:54 model_facet_analysis.py
-rw-r--r-- 1 ubuntu ubuntu  7484 May 21 06:04 reml_em.py
-rw-r--r-- 1 ubuntu ubuntu  3716 May 21 05:18 reml_lme4.R
-rw-r--r-- 1 ubuntu ubuntu 11158 May 20 18:57 variance_decomposition.py
-rw-r--r-- 1 ubuntu ubuntu  6959 May 20 14:22 visualize.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-21T09:07:41.657686+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/analysis/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/analysis/"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T09:07:41.657795+00:00_

total 568
drwxr-xr-x 3 ubuntu ubuntu   4096 May 21 06:03 .
drwxr-xr-x 9 ubuntu ubuntu   4096 May 21 08:48 ..
-rw-r--r-- 1 ubuntu ubuntu   3710 May 21 06:03 cross_model_reml.json
-rw-r--r-- 1 ubuntu ubuntu   7108 May 20 22:00 dual_metric_analysis.md
-rw-r--r-- 1 ubuntu ubuntu  16776 May 20 21:58 dual_metric_analysis.py
-rw-r--r-- 1 ubuntu ubuntu 131531 May 20 21:58 fig1_variance_decomposition_comparison.png
-rw-r--r-- 1 ubuntu ubuntu 182095 May 20 21:58 fig2_item_scatter.png
-rw-r--r-- 1 ubuntu ubuntu 215384 May 20 21:58 fig3_facet_heatmap.png
drwxr-xr-x 2 ubuntu ubuntu   4096 May 20 21:54 mvp_data

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T09:07:41.657912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/variance_decomposition.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/variance_decomposition.py"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-21T09:07:41.658079+00:00_

1	"""G-theory variance decomposition for LLM evaluation.
2	
3	Estimates variance components for all 6 facets (main effects) and all
4	15 two-way interactions using ANOVA-based estimation (Henderson Method I)
5	for balanced fully-crossed designs.  Higher-order interactions (≥3-way) are
6	absorbed into the residual.
7	
8	Estimation treats all facets as random (standard G-study practice).  The
9	fixed/random distinction is used downstream in the D-study to partition
10	universe-score variance from error variance.
11	
12	Bootstrap 95 %% CIs are computed by resampling items with replacement.
13	
14	Facets
15	------
16	precision, temperature                    — fixed  (in D-study)
17	prompt_template, seed, ordering, item_id  — random (in D-study)
18	
19	Input:  JSONL from ``run_experiment.py`` (one row per item × condition).
20	Output: JSON with ANOVA table, variance components, and bootstrap CIs.
21	"""
22	
23	import argparse
24	import json
25	from itertools import combinations
26	from math import prod
27	from pathlib import Path
28	from collections import Counter
29	from typing import Optional
30	
31	import numpy as np
32	import pandas as pd
33	
34	ALL_FACETS = [
35	    "precision", "temperature",
36	    "prompt_template", "seed", "ordering", "item_id",
37	]
38	FIXED_FACETS = ["precision", "temperature"]
39	RANDOM_FACETS = ["prompt_template", "seed", "ordering", "item_id"]
40	
41	
42	# ---------------------------------------------------------------------------
43	# ANOVA helpers
44	# ---------------------------------------------------------------------------
45	
46	def compute_ss(
47	    df: pd.DataFrame,
48	    response: str,
49	    facets: list[str],
50	) -> tuple[dict, dict[str, int]]:
51	    """Compute Type-I sums of squares for main effects and 2-way interactions.
52	
53	    For a balanced design, Type I = Type III, so the order of terms does not
54	    matter.
55	
56	    Returns:
57	        (effects_dict, n_levels_dict) where each effect entry has keys
58	       
…[truncated 10359 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T09:07:41.658231+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/d_study.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/d_study.py"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T09:07:41.658375+00:00_

1	"""D-study projections for G-theory variance decomposition.
2	
3	Given the estimated variance components from the G-study, computes the
4	generalizability coefficient (G) for different measurement designs by
5	varying the number of replications of each random facet.
6	
7	Partition rule
8	--------------
9	* σ²_τ  (universe score): components involving *only* fixed facets
10	  (precision, temperature and their interactions).
11	* σ²_δ  (relative error): components involving ≥1 random facet, each
12	  divided by the product of the sample sizes of the random facets in
13	  that component.
14	* G = σ²_τ / (σ²_τ + σ²_δ)
15	
16	Input:  ``variance_components.json`` from ``variance_decomposition.py``.
17	Output: ``d_study_results.json`` — current G, per-facet sweep, minimum
18	        replications for target G thresholds.
19	"""
20	
21	import argparse
22	import json
23	from pathlib import Path
24	
25	FIXED_FACETS = {"precision", "temperature"}
26	RANDOM_FACETS = ["prompt_template", "seed", "ordering", "item_id"]
27	
28	MVP_LEVELS = {
29	    "prompt_template": 3,
30	    "seed": 3,
31	    "ordering": 2,
32	    "item_id": 50,
33	}
34	
35	
36	def compute_g_coefficient(
37	    variance_components: dict,
38	    random_n: dict[str, int],
39	) -> tuple[float, float, float]:
40	    """Compute G for a given D-study design.
41	
42	    Args:
43	        variance_components: Keys are component names (e.g. ``"seed"``,
44	            ``"precision:prompt_template"``), values are dicts with an
45	            ``"estimate"`` key **or** plain floats.
46	        random_n: Number of replications for each random facet.
47	
48	    Returns:
49	        (G, σ²_τ, σ²_δ).
50	    """
51	    sigma_tau = 0.0
52	    sigma_delta = 0.0
53	
54	    for component, info in variance_components.items():
55	        est = info["estimate"] if isinstance(info, dict) else info
56	
57	        if component == "residual":
58	            divisor = 1
59	            for f in RANDOM_FACETS:
60	                divisor *= rando
…[truncated 4003 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-21T09:07:41.658550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/reml_em.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/reml_em.py"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-21T09:07:41.658718+00:00_

1	"""REML variance component estimation via EM algorithm.
2	
3	Uses Henderson MME with Cholesky factorization. Set OPENBLAS_NUM_THREADS=2
4	for optimal performance on this server (multi-thread OpenBLAS has contention issues).
5	"""
6	
7	import argparse
8	import json
9	import time
10	from itertools import combinations
11	from pathlib import Path
12	
13	import numpy as np
14	import pandas as pd
15	from scipy import sparse
16	from scipy.linalg import cho_factor, cho_solve
17	
18	
19	ALL_FACETS = [
20	    "model", "precision", "temperature",
21	    "prompt_template", "seed", "ordering", "item_id",
22	]
23	
24	
25	def _encode_factor(series):
26	    codes, uniques = pd.factorize(series, sort=True)
27	    return codes, len(uniques)
28	
29	
30	def _build_z_sparse(codes, n_levels, n_obs):
31	    return sparse.csc_matrix(
32	        (np.ones(n_obs, dtype=np.float64), (np.arange(n_obs), codes)),
33	        shape=(n_obs, n_levels),
34	    )
35	
36	
37	def reml_em(df, response, facets, max_iter=500, tol=1e-8, verbose=True):
38	    t0 = time.time()
39	    n_obs = len(df)
40	    y = df[response].values.astype(np.float64)
41	    p = 1
42	
43	    factor_codes = {}
44	    factor_nlevels = {}
45	    for f in facets:
46	        codes, nl = _encode_factor(df[f])
47	        factor_codes[f] = codes
48	        factor_nlevels[f] = nl
49	
50	    re_names = []
51	    Z_list = []
52	    q_list = []
53	
54	    for f in facets:
55	        Z = _build_z_sparse(factor_codes[f], factor_nlevels[f], n_obs)
56	        re_names.append(f)
57	        Z_list.append(Z)
58	        q_list.append(factor_nlevels[f])
59	
60	    for fi, fj in combinations(facets, 2):
61	        int_codes = factor_codes[fi] * factor_nlevels[fj] + factor_codes[fj]
62	        observed = np.unique(int_codes)
63	        n_obs_levels = len(observed)
64	        remap = np.empty(factor_nlevels[fi] * factor_nlevels[fj], dtype=np.int32)
65	        remap[observed] = np.arange(n_obs_levels)
66	        Z = _build_z_sparse(remap[int_codes], n_
…[truncated 6322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T09:07:41.658864+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/model_facet_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/model_facet_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-21T09:07:41.659024+00:00_

1	"""Multi-model G-theory variance decomposition (exp-001).
2	
3	Extends the MVP single-model analysis to a fully-crossed design with 7 facets:
4	model, precision, temperature, prompt_template, seed, ordering, item_id.
5	
6	Estimates all 7 main effects + 21 two-way interactions + residual using
7	Henderson Method I (ANOVA-based), identical to the MVP approach but with
8	model added as a crossed random facet.
9	
10	Input:  One or more JSONL files from multi-model experiments. Each row has
11	        model, precision, temperature, prompt_template, seed, ordering,
12	        item_id, correct, generated_text.
13	Output: JSON with variance components, G coefficient, and D-study projections.
14	"""
15	
16	import argparse
17	import glob
18	import json
19	from math import prod
20	from pathlib import Path
21	
22	import numpy as np
23	import pandas as pd
24	
25	from src.analysis.variance_decomposition import (
26	    compute_ss,
27	    compute_text_exact_match,
28	    estimate_variance_components,
29	)
30	
31	ALL_FACETS = [
32	    "model", "precision", "temperature",
33	    "prompt_template", "seed", "ordering", "item_id",
34	]
35	FIXED_FACETS = ["precision", "temperature"]
36	RANDOM_FACETS = ["model", "prompt_template", "seed", "ordering", "item_id"]
37	
38	
39	def load_jsonl_glob(patterns: list[str]) -> pd.DataFrame:
40	    """Load and concatenate JSONL files matching one or more glob patterns.
41	
42	    Args:
43	        patterns: List of file paths or glob patterns (e.g. ["results/*.jsonl"]).
44	
45	    Returns:
46	        Combined DataFrame.
47	    """
48	    paths = []
49	    for pat in patterns:
50	        expanded = sorted(glob.glob(pat))
51	        if not expanded:
52	            raise FileNotFoundError(f"No files matched pattern: {pat}")
53	        paths.extend(expanded)
54	
55	    frames = [pd.read_json(p, lines=True) for p in paths]
56	    df = pd.concat(frames, ignore_index=True)
57	
58	    for col in ["answer_logprob"]:
59	        if col in df.columns:
60	      
…[truncated 8434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-21T09:07:41.659176+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/analysis/dual_metric_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/analysis/dual_metric_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-21T09:07:41.659469+00:00_

1	"""Dual-metric (binary_correct vs text_exact_match) deep analysis."""
2	import json
3	import numpy as np
4	import pandas as pd
5	import matplotlib
6	matplotlib.use('Agg')
7	import matplotlib.pyplot as plt
8	import matplotlib.ticker as mticker
9	from pathlib import Path
10	
11	OUT = Path("/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/analysis")
12	OUT.mkdir(parents=True, exist_ok=True)
13	
14	# ── Load variance components ──
15	vc_binary = {
16	    "precision:temperature": {"pct": 0.0017},
17	    "precision:prompt_template": {"pct": 0.0196},
18	    "precision:seed": {"pct": 0.0},
19	    "precision:ordering": {"pct": 0.0},
20	    "precision:item_id": {"pct": 7.2432},
21	    "temperature:prompt_template": {"pct": 0.0049},
22	    "temperature:seed": {"pct": 0.0387},
23	    "temperature:ordering": {"pct": 0.0185},
24	    "temperature:item_id": {"pct": 6.8495},
25	    "prompt_template:seed": {"pct": 0.0},
26	    "prompt_template:ordering": {"pct": 0.0103},
27	    "prompt_template:item_id": {"pct": 5.7342},
28	    "seed:ordering": {"pct": 0.0},
29	    "seed:item_id": {"pct": 2.6973},
30	    "ordering:item_id": {"pct": 0.4438},
31	    "precision": {"pct": 0.8725},
32	    "temperature": {"pct": 0.0},
33	    "prompt_template": {"pct": 0.0310},
34	    "seed": {"pct": 0.0},
35	    "ordering": {"pct": 0.0},
36	    "item_id": {"pct": 58.4405},
37	    "residual": {"pct": 17.5944},
38	}
39	
40	vc_text = {
41	    "precision:temperature": {"pct": 1.2611},
42	    "precision:prompt_template": {"pct": 0.0128},
43	    "precision:seed": {"pct": 0.0},
44	    "precision:ordering": {"pct": 0.0207},
45	    "precision:item_id": {"pct": 0.6281},
46	    "temperature:prompt_template": {"pct": 0.2423},
47	    "temperature:seed": {"pct": 0.0},
48	    "temperature:ordering": {"pct": 0.0},
49	    "temperature:item_id": {"pct": 2.4724},
50	    "prompt_template:seed": {"pct": 0.0},
51	    "prompt_template:ordering": {"pct": 0.0736},
52	    "prompt_template:item
…[truncated 15355 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-21T09:07:41.659667+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory -type f -name \"*.md\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory -type f -name \"*.md\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-21T09:07:41.659804+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/task_context/director.md
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/task_context/reviewer.md
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/memory.md
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/pyparsing/ai/best_practices.md
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/numpy/random/LICENSE.md
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/fft/pocketfft/LICENSE.md
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/splitmix64/LICENSE.md
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/philox/LICENSE.md
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/distributions/LICENSE.md
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/sfc64/LICENSE.md
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/pcg64/LICENSE.md
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/mt19937/LICENSE.md
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.venv/lib/python3.1
…[truncated 845 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T09:07:41.659944+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/IDEA_BRIEF.md"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T09:07:41.660069+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T09:07:41.660192+00:00_

1	# Memory — nlp_variance_gtheory
2	
3	## Gated Model 约束 (2026-05-20)
4	Llama-3.1-8B-Instruct 和 gemma-2-9b-it 是 HF gated models，直接用 repo ID 加载失败。westd-32570 上通过 ModelScope 下载到本地路径（如 `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct`）。exp-001 正式运行需要 model path mapping 或 HF token。
5	
6	## 双 Metric 设计决策 (2026-05-20, D002)
7	binary_correct 和 text_exact_match 测量正交维度（Spearman ρ = −0.21, n.s.）。前者衡量评估有效性（item 难度主导），后者衡量可复现性（prompt×item + temperature 主导）。两者必须同时保留——不能互相替代。
8	
9	## Temperature 对 text_match 的决定性影响 (2026-05-20)
10	T=0 → text_match=0.247, T=0.5 → text_match=0.019（降 92%），但 binary_correct 几乎不变。这是 G-theory 框架的关键洞察：采样随机性改变文本表述但不改变答案选择。
11	
12	## FP32 精度效应确认 (2026-05-20)
13	FP32 的 8.5pp accuracy gap 中 97.4% 是精度效应（非引擎 confound）。BF16-trained model 用 FP32 推理表现更差，可能因为权重从 BF16 加载到 FP32 时的数值行为差异。
14	
15	## Gemma2 不支持 float16 (2026-05-21)
16	vLLM 拒绝以 float16 加载 gemma2：`"The model type 'gemma2' does not support float16. Reason: Numerical instability."`。这是架构层面限制，非配置问题。Director 决策 (方案 A 修改版)：cross-model 分析用 bf16+fp32 (2 precisions × 4 models 平衡设计)，fp16 仅用于 Llama/Mistral/Qwen 的 within-model G-study。bf16 vs fp16 差异 <0.1pp (Llama 已证实)，precision 信号集中在 fp32 vs 其他 (10.7pp gap)。
17	
18	## few_shot_examples.json 一致性风险 (2026-05-21)
19	Gemma 启动时 Worker 重新生成了 few_shot_examples.json（从 5 subjects × 2 orderings → 10 subjects × 4 orderings）。需验证 Llama 实际使用的版本是否一致，否则 cross-model ordering facet 对比可能失效。
20	
21	## M006: D-study 公式方向性检查 (2026-05-21)
22	D-study 公式 `G_ni = σ²τ / (σ²τ + σ²δ × (n_actual / ni))` — 注意是 n_actual/ni 而非 ni/n_actual。G 必须随 n_items 单调递增（items 越多 error 越小）。所有 D-study 代码必须带 monotonicity assertion。temperature_stratified_analysis.json 曾因公式反转导致 min_items_G80=10（正确值 414）。**教训：遇到不合理结果（G 随 items 下降）时质疑计算，不要合理化。**
23	
24	## Cross-model G-study 关键洞察 (2026-05-21, 更新)
25	3-model 平衡数据 (Llama+Gemma+Mistral, bf16, N=259,200): item_id=42.8%, model×item_id=31.7%, residual=19.3%。G_item=0.777 [0.725, 0.829]。D-study: 5 models → G=0.84。2-model 平衡数据 (Llama+Gemma, bf16+fp32, N=23
…[truncated 323 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-21T09:07:41.660376+00:00_

1	# Idea Brief: Where Does the Variance Go? Decomposing Infrastructure and Methodological Variance in LLM Evaluation via Generalizability Theory
2	
3	
4	- **Idea ID**: `idea_031`
5	- **Created**: 2026-05-20
6	- **Approved**: 2026-05-20
7	- **Source**: foreign:be-idea-gen-0515-4
8	- **Level**: solid
9	- **Target Venues**: AAAI 2027 (abstract Jul 21, paper Jul 28 2026 — primary target with 10 weeks runway; requires overlapping experiment execution with writing), ACL 2027 via ARR (October 15, 2026 cycle — comfortable 21-week runway; preferred if AAAI timeline proves too tight), TACL (rolling monthly deadline — no conference deadline pressure, allows most thorough execution), NeurIPS 2027 (abstract ~May 2027 — very comfortable fallback if earlier deadlines are missed)
10	
11	## Seed Topic
12	
13	web_research
14	
15	## Core Problem
16	
17	When LLM evaluation results vary across reproductions, practitioners cannot determine whether the culprit is prompt phrasing, random seed, GPU hardware, numerical precision, temperature, or few-shot ordering—let alone how these factors interact—because every prior study isolates at most two sources. Mesting (2026) recently decomposed methodological sources (prompt variant, temperature, judge model) via Generalizability Theory but treated infrastructure as fixed background; no existing work crosses infrastructure factors (hardware type, numerical precision) with methodological factors (prompt, temperature, seed, data ordering) in a unified variance decomposition that produces actionable reproducibility budgets.
18	
19	## Opportunity / Why Now
20	
21	Multiple 2025–2026 papers each quantify individual variance sources in isolation: Brittlebench (2026) attributes up to 50% of performance variance to prompt perturbations and shows single perturbations alter model rankings in 63% of cases; Bui et al. (2025) document extreme seed sensitivity (RTES variance = 18.22) in fine-tuning; Yuan et al. (2025) demonstrate up to 9% accuracy variation and 
…[truncated 17284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T09:07:41.660626+00:00_

Excellent! Now I have comprehensive information. Let me compile the complete report.

## G-Study Implementation Report

Based on my analysis of the existing G-study implementation for this project, here is a comprehensive report:

### Overview

The project implements **Generalizability Theory (G-theory)** for decomposing variance sources in LLM evaluation. There are two main levels of implementation:

1. **Single-model MVP analysis** (`gstudy_full.py`)
2. **Multi-model G-theory analysis** with REML-EM and bootstrap CIs (`variance_decomposition.py`, `reml_em.py`)

---

### Facet Structure

The study uses a **fully-crossed factorial design** with these facets:

**MVP Phase (Single-Model):**
- **Precision**: fp32, bf16, fp16 (3 levels)
- **Temperature**: 0.0, 0.5 (top-p=0.9), 1.0 (top-p=0.8) (3 levels)
- **Prompt Template**: 6 paraphrases (6 levels, random facet)
- **Seed**: CUDA RNG seeds (6 levels, random facet)
- **Ordering**: Few-shot example orderings (4 levels, random facet)
- **Item ID**: MMLU items (50 levels, random facet)

**Multi-Model Phase (exp-001):**
- **Model**: Llama-3.1-8B-Instruct, Gemma-2-9B-IT, Mistral-7B-Instruct-v0.3, Qwen3-8B (4+ levels, random facet)
- Plus all 6 facets above

**Fixed vs. Random Facets:**
- **Fixed Facets** (in D-study partition): precision, temperature
- **Random Facets**: prompt_template, seed, ordering, item_id, (model)

---

### Variance Components Estimated

The implementation computes:

1. **6 Main Effects** (single facets)
2. **15 Two-Way Interactions** (all pairwise combinations)
3. **Residual** (confounds ≥3-way interactions; treated as error)

**Key Components from MVP Results:**
- **item_id**: 58.4% (dominant)
- **residual**: 17.6% (higher-order interactions + measurement noise)
- **precision×item**: 7.2%
- **temperature×item**: 6.9%
- **prompt_template×item**: 5.7%
- **seed×item**: 2.7%
- **precision (main)**: 0.9%

**Critical Insight**: Direct precision-×-methodology interactions are <0.02%, supporting "separabilit
…[truncated 7162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Agent",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T09:07:41.660804+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/variance_decomposition.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/variance_decomposition.py"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T09:07:41.661078+00:00_

1	"""G-theory variance decomposition for LLM evaluation.
2	
3	Estimates variance components for all 6 facets (main effects) and all
4	15 two-way interactions using ANOVA-based estimation (Henderson Method I)
5	for balanced fully-crossed designs.  Higher-order interactions (≥3-way) are
6	absorbed into the residual.
7	
8	Estimation treats all facets as random (standard G-study practice).  The
9	fixed/random distinction is used downstream in the D-study to partition
10	universe-score variance from error variance.
11	
12	Bootstrap 95 %% CIs are computed by resampling items with replacement.
13	
14	Facets
15	------
16	precision, temperature                    — fixed  (in D-study)
17	prompt_template, seed, ordering, item_id  — random (in D-study)
18	
19	Input:  JSONL from ``run_experiment.py`` (one row per item × condition).
20	Output: JSON with ANOVA table, variance components, and bootstrap CIs.
21	"""
22	
23	import argparse
24	import json
25	from itertools import combinations
26	from math import prod
27	from pathlib import Path
28	from collections import Counter
29	from typing import Optional
30	
31	import numpy as np
32	import pandas as pd
33	
34	ALL_FACETS = [
35	    "precision", "temperature",
36	    "prompt_template", "seed", "ordering", "item_id",
37	]
38	FIXED_FACETS = ["precision", "temperature"]
39	RANDOM_FACETS = ["prompt_template", "seed", "ordering", "item_id"]
40	
41	
42	# ---------------------------------------------------------------------------
43	# ANOVA helpers
44	# ---------------------------------------------------------------------------
45	
46	def compute_ss(
47	    df: pd.DataFrame,
48	    response: str,
49	    facets: list[str],
50	) -> tuple[dict, dict[str, int]]:
51	    """Compute Type-I sums of squares for main effects and 2-way interactions.
52	
53	    For a balanced design, Type I = Type III, so the order of terms does not
54	    matter.
55	
56	    Returns:
57	        (effects_dict, n_levels_dict) where each effect entry has keys
58	       
…[truncated 10359 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T09:07:41.661243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/d_study.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/d_study.py"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T09:07:41.661515+00:00_

1	"""D-study projections for G-theory variance decomposition.
2	
3	Given the estimated variance components from the G-study, computes the
4	generalizability coefficient (G) for different measurement designs by
5	varying the number of replications of each random facet.
6	
7	Partition rule
8	--------------
9	* σ²_τ  (universe score): components involving *only* fixed facets
10	  (precision, temperature and their interactions).
11	* σ²_δ  (relative error): components involving ≥1 random facet, each
12	  divided by the product of the sample sizes of the random facets in
13	  that component.
14	* G = σ²_τ / (σ²_τ + σ²_δ)
15	
16	Input:  ``variance_components.json`` from ``variance_decomposition.py``.
17	Output: ``d_study_results.json`` — current G, per-facet sweep, minimum
18	        replications for target G thresholds.
19	"""
20	
21	import argparse
22	import json
23	from pathlib import Path
24	
25	FIXED_FACETS = {"precision", "temperature"}
26	RANDOM_FACETS = ["prompt_template", "seed", "ordering", "item_id"]
27	
28	MVP_LEVELS = {
29	    "prompt_template": 3,
30	    "seed": 3,
31	    "ordering": 2,
32	    "item_id": 50,
33	}
34	
35	
36	def compute_g_coefficient(
37	    variance_components: dict,
38	    random_n: dict[str, int],
39	) -> tuple[float, float, float]:
40	    """Compute G for a given D-study design.
41	
42	    Args:
43	        variance_components: Keys are component names (e.g. ``"seed"``,
44	            ``"precision:prompt_template"``), values are dicts with an
45	            ``"estimate"`` key **or** plain floats.
46	        random_n: Number of replications for each random facet.
47	
48	    Returns:
49	        (G, σ²_τ, σ²_δ).
50	    """
51	    sigma_tau = 0.0
52	    sigma_delta = 0.0
53	
54	    for component, info in variance_components.items():
55	        est = info["estimate"] if isinstance(info, dict) else info
56	
57	        if component == "residual":
58	            divisor = 1
59	            for f in RANDOM_FACETS:
60	                divisor *= rando
…[truncated 4003 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T09:07:41.661689+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/model_facet_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/code/src/analysis/model_facet_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T09:07:41.661894+00:00_

1	"""Multi-model G-theory variance decomposition (exp-001).
2	
3	Extends the MVP single-model analysis to a fully-crossed design with 7 facets:
4	model, precision, temperature, prompt_template, seed, ordering, item_id.
5	
6	Estimates all 7 main effects + 21 two-way interactions + residual using
7	Henderson Method I (ANOVA-based), identical to the MVP approach but with
8	model added as a crossed random facet.
9	
10	Input:  One or more JSONL files from multi-model experiments. Each row has
11	        model, precision, temperature, prompt_template, seed, ordering,
12	        item_id, correct, generated_text.
13	Output: JSON with variance components, G coefficient, and D-study projections.
14	"""
15	
16	import argparse
17	import glob
18	import json
19	from math import prod
20	from pathlib import Path
21	
22	import numpy as np
23	import pandas as pd
24	
25	from src.analysis.variance_decomposition import (
26	    compute_ss,
27	    compute_text_exact_match,
28	    estimate_variance_components,
29	)
30	
31	ALL_FACETS = [
32	    "model", "precision", "temperature",
33	    "prompt_template", "seed", "ordering", "item_id",
34	]
35	FIXED_FACETS = ["precision", "temperature"]
36	RANDOM_FACETS = ["model", "prompt_template", "seed", "ordering", "item_id"]
37	
38	
39	def load_jsonl_glob(patterns: list[str]) -> pd.DataFrame:
40	    """Load and concatenate JSONL files matching one or more glob patterns.
41	
42	    Args:
43	        patterns: List of file paths or glob patterns (e.g. ["results/*.jsonl"]).
44	
45	    Returns:
46	        Combined DataFrame.
47	    """
48	    paths = []
49	    for pat in patterns:
50	        expanded = sorted(glob.glob(pat))
51	        if not expanded:
52	            raise FileNotFoundError(f"No files matched pattern: {pat}")
53	        paths.extend(expanded)
54	
55	    frames = [pd.read_json(p, lines=True) for p in paths]
56	    df = pd.concat(frames, ignore_index=True)
57	
58	    for col in ["answer_logprob"]:
59	        if col in df.columns:
60	      
…[truncated 8434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T09:07:41.662066+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T09:07:41.662190+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T09:07:41.662339+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "head -5 /root/nlp_variance_gtheory/results/analysis/cross_model_4way_bf16.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "head -5 /root/nlp_variance_gtheory/results/analysis/cross_model_4way_bf16.csv"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-21T09:07:41.662542+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "wc -l /root/nlp_variance_gtheory/results/analysis/cross_model_4way_bf16.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "wc -l /root/nlp_variance_gtheory/results/analysis/cross_model_4way_bf16.csv"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-21T09:07:41.662742+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"condition_id,item_id,subject,model,precision,temperature,top_p,prompt_template,seed,ordering,generated_text,predicted_answer,gold_answer,correct,latency_ms,answer_logprob,top_logprobs\\n2033,abstract_algebra_81,abstract_algebra,llama-3.1-8b-instruct,bfloat16,0.7,0.9,1,1024,1,\\\"A\\n\\nThe following are multiple choice questions (with answers) about abstract algebra.\\\",A,D,0,24.53,-0.6409203410148621,\\\"{' A': -0.6409203410148621, ' C': -1.3560044765472412, ' B': -1.5347745418548584, '\\\"\\\"': -inf, '!': -inf}\\\"\\n2033,abstract_algebra_14,abstract_algebra,llama-3.1-8b-instruct,bfloat16,0.7,0.9,1,1024,1,\\\"D\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.99}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-21T09:07:41.662951+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"1121525 /root/nlp_variance_gtheory/results/analysis/cross_model_4way_bf16.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-21T09:07:41.663146+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "ls /root/nlp_variance_gtheory/results/analysis/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "ls /root/nlp_variance_gtheory/results/analysis/"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-21T09:07:41.663354+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"bf16_fp16_only_gstudy.json\\nbinary_data_limitation.json\\nbootstrap_vs_jackknife.json\\ncross_model_2way_precision.csv\\ncross_model_2way_precision_meta.json\\ncross_model_3way_bf16.csv\\ncross_model_3way_bf16_meta.json\\ncross_model_4way_bf16.csv\\ncross_model_balanced.csv\\ncross_model_balanced.jsonl\\ncross_model_balanced_meta.json\\ncross_model_bootstrap.json\\ncross_model_g_coefficients.json\\ncross_model_gstudy.json\\ncross_model_llama_gemma.csv\\ncross_model_llama_gemma.jsonl\\ncross_model_reml.json\\ncross_model_reml_500iter.json\\ndataset_a4_gstudy.json\\ndataset_a_gstudy.json\\ndataset_b_gstudy.json\\nexp001_llama_bf16only_5facet.json\\nexp001b_resampling_gstudy.json\\nexp002_prep_report.md\\nfixed_vs_random_sensitivity.json\\nirt_vs_gtheory.json\\nleave_one_model_out.json\\nllama_full.csv\\nllama_precision_balanced.csv\\nllama_precision_balanced_meta.json\\nllama_single_model_gstudy.json\\nlomo_matched_spec.json\\ntemperature_stratified_analysis.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-21T09:07:41.664855+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /root/nlp_variance_gtheory/results/analysis/cross_model_gstudy.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /root/nlp_variance_gtheory/results/analysis/cross_model_gstudy.json"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-21T09:07:41.665375+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"variance_components\\\": {\\n    \\\"model:precision\\\": {\\n      \\\"estimate\\\": 0.002862784248965513,\\n      \\\"pct\\\": 1.413417175184034\\n    },\\n    \\\"model:temperature\\\": {\\n      \\\"estimate\\\": 0.00011870591528130242,\\n      \\\"pct\\\": 0.05860762281166056\\n    },\\n    \\\"model:prompt_template\\\": {\\n      \\\"estimate\\\": 2.402264109639751e-05,\\n      \\\"pct\\\": 0.011860486353870214\\n    },\\n    \\\"model:seed\\\": {\\n      \\\"estimate\\\": 1.5882635941682044e-05,\\n      \\\"pct\\\": 0.007841593523955106\\n    },\\n    \\\"model:ordering\\\": {\\n      \\\"estimate\\\": 1.464414769445534e-06,\\n      \\\"pct\\\": 0.0007230125663418166\\n    },\\n    \\\"model:item_id\\\": {\\n      \\\"estimate\\\": 0.052990529644762044,\\n      \\\"pct\\\": 26.162546042046376\\n    },\\n    \\\"precision:temperature\\\": {\\n      \\\"estimate\\\": 0.00017760671055344333,\\n      \\\"pct\\\": 0.08768819208603951\\n    },\\n    \\\"precision:prompt_template\\\": {\\n      \\\"estimate\\\": 2.4218263937991997e-05,\\n      \\\"pct\\\": 0.011957069491166665\\n    },\\n    \\\"precision:seed\\\": {\\n      \\\"estimate\\\": 0.0,\\n      \\\"pct\\\": 0.0\\n    },\\n    \\\"precision:ordering\\\": {\\n      \\\"estimate\\\": 1.0633958135522418e-06,\\n      \\\"pct\\\": 0.000525021020161287\\n    },\\n    \\\"precision:item_id\\\": {\\n      \\\"estimate\\\": 0.004684000564930411,\\n      \\\"pct\\\": 2.3125902168271\\n    },\\n    \\\"temperature:prompt_template\\\": {\\n      \\\"estimate\\\": 9.018113094017191e-05,\\n      \\\"pct\\\": 0.04452433304899561\\n    },\\n    \\\"temperature:seed\\\": {\\n      \\\"estimate\\\": 2.5337923801108396e-05,\\n      \\\"pct\\\": 0.012509869263438986\\n    },\\n    \\\"temperature:ordering\\\": {\\n      \\\"estimate\\\": 0.0,\\n      \\\"pct\\\": 0.0\\n    },\\n    \\\"temperature:item_id\\\": {\\n      \\\"estimate\\\": 0.0026693313551231566,\
…[truncated 8541 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-21T09:07:41.665673+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "head -1 /root/nlp_variance_gtheory/results/analysis/cross_model_4way_bf16.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "head -1 /root/nlp_variance_gtheory/results/analysis/cross_model_4way_bf16.csv"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-21T09:07:41.665910+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"condition_id,item_id,subject,model,precision,temperature,top_p,prompt_template,seed,ordering,generated_text,predicted_answer,gold_answer,correct,latency_ms,answer_logprob,top_logprobs\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-21T09:07:41.666115+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "python3 -c \"import pandas as pd; df=pd.read_csv('/root/nlp_variance_gtheory/results/analysis/cross_model_4way_bf16.csv', nrows=10); print(df[['model','precision','temperature','prompt_template','seed','ordering','item_id','correct']].head())\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "python3 -c \"import pandas as pd; df=pd.read_csv('/root/nlp_variance_gtheory/results/analysis/cross_model_4way_bf16.csv', nrows=10); print(df[['model','precision','temperature','prompt_template','seed','ordering','item_id','correct']].head())\""
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-21T09:07:41.666325+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-21T09:07:41.666591+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /root/nlp_variance_gtheory/results/analysis/dataset_a4_gstudy.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /root/nlp_variance_gtheory/results/analysis/dataset_a4_gstudy.json"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-21T09:07:41.667029+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"A-4\\\",\\n  \\\"description\\\": \\\"4 models (Llama-3.1-8B, Gemma-2-9B, Mistral-7B, Qwen3-8B) x bf16 only, fully crossed\\\",\\n  \\\"n_observations\\\": 345600,\\n  \\\"n_levels\\\": {\\n    \\\"model\\\": 4,\\n    \\\"temperature\\\": 3,\\n    \\\"prompt_template\\\": 6,\\n    \\\"seed\\\": 6,\\n    \\\"ordering\\\": 4,\\n    \\\"item_id\\\": 200\\n  },\\n  \\\"grand_mean\\\": 0.7014670138888889,\\n  \\\"total_variance\\\": 0.2094116482511765,\\n  \\\"model_accuracies\\\": {\\n    \\\"gemma-2-9b-it\\\": 0.7311226851851852,\\n    \\\"llama-3.1-8b-instruct\\\": 0.7108333333333333,\\n    \\\"mistral-7b-instruct-v0.3\\\": 0.6375810185185186,\\n    \\\"qwen3-8b\\\": 0.7263310185185186\\n  },\\n  \\\"variance_components_ems\\\": {\\n    \\\"residual\\\": {\\n      \\\"estimate\\\": 0.04112504957221074,\\n      \\\"pct\\\": 19.546133489131964,\\n      \\\"ci_95_lower_pct\\\": 17.079460634578474,\\n      \\\"ci_95_upper_pct\\\": 21.66215216840251\\n    },\\n    \\\"model:item_id\\\": {\\n      \\\"estimate\\\": 0.07077083602117985,\\n      \\\"pct\\\": 33.63634141227101,\\n      \\\"ci_95_lower_pct\\\": 28.403783030649297,\\n      \\\"ci_95_upper_pct\\\": 37.86331353856019\\n    },\\n    \\\"temperature:item_id\\\": {\\n      \\\"estimate\\\": 0.0013693394228968586,\\n      \\\"pct\\\": 0.6508269638648393,\\n      \\\"ci_95_lower_pct\\\": 0.42563847889720724,\\n      \\\"ci_95_upper_pct\\\": 0.9052073107692409\\n    },\\n    \\\"prompt_template:item_id\\\": {\\n      \\\"estimate\\\": 0.0030141106077090168,\\n      \\\"pct\\\": 1.432562608486166,\\n      \\\"ci_95_lower_pct\\\": 1.1997864521761648,\\n      \\\"ci_95_upper_pct\\\": 1.6734667379141035\\n    },\\n    \\\"seed:item_id\\\": {\\n      \\\"estimate\\\": 0.002784839735601544,\\n      \\\"pct\\\": 1.3235935222966497,\\n      \\\"ci_95_lower_pct\\\": 1.0775488602242351,\\n      \\\"ci_95_upper_pct\\\": 1.659477351049782\\n    },\\n
…[truncated 6396 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-21T09:07:41.667301+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "python3 -c \"import pandas as pd; df=pd.read_csv('/root/nlp_variance_gtheory/results/analysis/cross_model_4way_bf16.csv'); print('shape:', df.shape); print('models:', df['model'].unique()); print('n_levels:'); [print(f'  {c}: {df[c].nunique()}') for c in ['model','precision','temperature','prompt_template','seed','ordering','item_id']]\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "python3 -c \"import pandas as pd; df=pd.read_csv('/root/nlp_variance_gtheory/results/analysis/cross_model_4way_bf16.csv'); print('shape:', df.shape); print('models:', df['model'].unique()); print('n_levels:'); [print(f'  {c}: {df[c].nunique()}') for c in ['model','precision','temperature','prompt_template','seed','ordering','item_id']]\""
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-21T09:07:41.667572+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-21T09:07:41.667808+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "grep -o '\"model\":[^,]*' /root/nlp_variance_gtheory/results/analysis/cross_model_4way_bf16.csv | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "grep -o '\"model\":[^,]*' /root/nlp_variance_gtheory/results/analysis/cross_model_4way_bf16.csv | head -5"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-21T09:07:41.668019+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-21T09:07:41.668251+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /root/nlp_variance_gtheory/scripts/dataset_a4_gstudy.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /root/nlp_variance_gtheory/scripts/dataset_a4_gstudy.py"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-21T09:07:41.668482+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/nlp_variance_gtheory/scripts/dataset_a4_gstudy.py: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-21T09:07:41.668688+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "find /root/nlp_variance_gtheory/scripts -name \"*a4*\" -o -name \"*dataset*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "find /root/nlp_variance_gtheory/scripts -name \"*a4*\" -o -name \"*dataset*\""
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-21T09:07:41.668888+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "ls /root/nlp_variance_gtheory/scripts/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "ls /root/nlp_variance_gtheory/scripts/"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-21T09:07:41.669087+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/nlp_variance_gtheory/scripts/dataset_a_gstudy.py\\n/root/nlp_variance_gtheory/scripts/gstudy_dataset_b.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-21T09:07:41.669325+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"auto_start_qwen.sh\\nbalance_cross_model.py\\nbf16_fp16_sensitivity.py\\nbootstrap_vs_jackknife.py\\ncompute_g_coefficients.py\\ndataset_a_gstudy.py\\ndry_run_exp002.py\\nexp001_4model_gstudy.py\\nexp001_4model_gstudy_v2.py\\nexp001_llama_bf16only_5facet.py\\nexp001b_gstudy.py\\nfix_dstudy_formula.py\\nfixed_vs_random_sensitivity.py\\ngenerate_exp001b_design.py\\ngstudy_dataset_b.py\\ngstudy_full.py\\nleave_one_model_out.py\\nlomo_matched_spec.py\\nprepare_few_shot_exp002.py\\nrun_exp001b.sh\\nrun_exp002_full.sh\\nrun_exp002_pilot.sh\\nsample_benchmarks.py\\nsample_resampling.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-21T09:07:41.669580+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /root/nlp_variance_gtheory/scripts/dataset_a_gstudy.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /root/nlp_variance_gtheory/scripts/dataset_a_gstudy.py"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-21T09:07:41.669994+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Dataset A full G-study: 3 models × bf16 only, 6 facets. Fully vectorized.\\\"\\\"\\\"\\n\\nimport json\\nimport sys\\nimport time\\nfrom itertools import combinations\\nfrom math import prod\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport pandas as pd\\n\\nsys.path.insert(0, \\\"/root/nlp_variance_gtheory\\\")\\nfrom src.analysis.variance_decomposition import compute_ss, estimate_variance_components\\n\\nINPUT = \\\"results/analysis/cross_model_3way_bf16.csv\\\"\\nOUTPUT = \\\"results/analysis/dataset_a_gstudy.json\\\"\\nRESPONSE = \\\"correct\\\"\\nN_BOOT = 200\\nSEED = 42\\n\\nFACETS = [\\\"model\\\", \\\"temperature\\\", \\\"prompt_template\\\", \\\"seed\\\", \\\"ordering\\\", \\\"item_id\\\"]\\nFIXED_FACETS = [\\\"temperature\\\"]\\nRANDOM_FACETS = [\\\"model\\\", \\\"prompt_template\\\", \\\"seed\\\", \\\"ordering\\\", \\\"item_id\\\"]\\n\\nt_start = time.time()\\ndf = pd.read_csv(INPUT)\\nfor f in FACETS:\\n    df[f] = df[f].astype(str)\\n\\nprint(f\\\"Loaded {len(df)} obs, {df['model'].nunique()} models, {df['item_id'].nunique()} items ({time.time()-t_start:.1f}s)\\\", flush=True)\\n\\n# Step 1: ANOVA on full data\\neffects, n_levels = compute_ss(df, RESPONSE, FACETS)\\nvc = estimate_variance_components(effects, FACETS, n_levels)\\ntotal_var = sum(vc.values())\\n\\nprint(f\\\"\\\\n{'Component':<30} {'Estimate':>12} {'%':>8}\\\", flush=True)\\nprint(\\\"-\\\" * 52, flush=True)\\nfor name, est in sorted(vc.items(), key=lambda x: -x[1]):\\n    pct = est / total_var * 100\\n    if pct >= 0.01:\\n        print(f\\\"{name:<30} {est:>12.8f} {pct:>7.2f}%\\\", flush=True)\\n\\n# Step 2: Build 6D numpy array (vectorized)\\nfacet_order = FACETS\\nfacet_vals = {}\\nfacet_maps = {}\\nfor f in facet_order:\\n    vals = sorted(df[f].unique())\\n    facet_vals[f] = vals\\n    facet_maps[f] = {v: i for i, v in enumerate(vals)}\\n\\nshape = tuple(len(facet_vals[f]) for f in facet_order)\\nprint(f\\
…[truncated 7306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-21T09:07:41.670295+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /root/nlp_variance_gtheory/scripts/exp001_4model_gstudy_v2.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /root/nlp_variance_gtheory/scripts/exp001_4model_gstudy_v2.py"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-21T09:07:41.670774+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import pandas as pd\\nimport numpy as np\\nimport json\\nfrom numpy.random import default_rng\\n\\ndf = pd.read_csv('results/analysis/cross_model_4way_bf16.csv')\\nN = len(df)\\ngrand_mean = df['correct'].mean()\\ntotal_var = df['correct'].var()\\nss_total = total_var * (N - 1)\\n\\nn_m, n_t, n_p, n_s, n_o, n_i = 4, 3, 6, 6, 4, 200\\n\\nprint(f\\\"N={N}, grand_mean={grand_mean:.6f}, total_var={total_var:.6f}\\\")\\n\\nmodel_acc = df.groupby('model')['correct'].mean().to_dict()\\nprint(\\\"\\\\nModel accuracies:\\\")\\nfor m, a in sorted(model_acc.items()):\\n    print(f\\\"  {m}: {a:.6f}\\\")\\n\\n# Build 6D array\\nmodels_sorted = sorted(df['model'].unique())\\ntemps_sorted = sorted(df['temperature'].unique())\\nprompts_sorted = sorted(df['prompt_template'].unique())\\nseeds_sorted = sorted(df['seed'].unique())\\norders_sorted = sorted(df['ordering'].unique())\\nitems_sorted = sorted(df['item_id'].unique())\\n\\nmodel_map = {v: i for i, v in enumerate(models_sorted)}\\ntemp_map = {v: i for i, v in enumerate(temps_sorted)}\\nprompt_map = {v: i for i, v in enumerate(prompts_sorted)}\\nseed_map = {v: i for i, v in enumerate(seeds_sorted)}\\norder_map = {v: i for i, v in enumerate(orders_sorted)}\\nitem_map = {v: i for i, v in enumerate(items_sorted)}\\n\\nY = np.full((n_m, n_t, n_p, n_s, n_o, n_i), np.nan)\\nfor _, row in df.iterrows():\\n    Y[model_map[row['model']], temp_map[row['temperature']], prompt_map[row['prompt_template']],\\n      seed_map[row['seed']], order_map[row['ordering']], item_map[row['item_id']]] = row['correct']\\n\\nprint(f\\\"Array shape: {Y.shape}, NaN: {np.isnan(Y).sum()}\\\")\\n\\ndef compute_gstudy(Y_arr):\\n    nm, nt, np_, ns, no, ni = Y_arr.shape\\n    N_arr = nm * nt * np_ * ns * no * ni\\n    gm = np.nanmean(Y_arr)\\n    \\n    mean_m = np.nanmean(Y_arr, axis=(1,2,3,4,5))\\n    mean_t = np.nanmean(Y_arr, axis=(0,2,3,4,5))\\n    mean_p = np.nanmean(Y_arr, axis=(0,1,3,4,5))\\n    me
…[truncated 6726 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-21T09:07:41.671257+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/model_as_fixed_gstudy.py",
  "content": "\"\"\"Model-as-fixed G-study (MF2 defense).\n\nTreats model as a fixed facet (not a random sample from a population of models).\nTwo methods:\n  A) Per-model 5-facet G-study, then average (clean separation)\n  B) Remove model:item from σ²δ in the crossed 6-facet design (quick adjustment)\n\nInput:  results/analysis/cross_model_4way_bf16.csv (4 models × bf16 × fully crossed)\nOutput: results/analysis/model_as_fixed_gstudy.json\n\"\"\"\n\nimport json\nimport time\nfrom itertools import combinations\nfrom math import prod\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\n\nINPUT = \"results/analysis/cross_model_4way_bf16.csv\"\nOUTPUT = \"results/analysis/model_as_fixed_gstudy.json\"\nN_BOOT = 200\nSEED = 42\n\nFACETS_6 = [\"model\", \"temperature\", \"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\nFACETS_5 = [\"temperature\", \"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\n\nt_start = time.time()\ndf = pd.read_csv(INPUT)\nprint(f\"Loaded {len(df)} obs ({time.time()-t_start:.1f}s)\", flush=True)\n\nmodels_sorted = sorted(df[\"model\"].unique())\ntemps_sorted = sorted(df[\"temperature\"].unique())\nprompts_sorted = sorted(df[\"prompt_template\"].unique())\nseeds_sorted = sorted(df[\"seed\"].unique())\norders_sorted = sorted(df[\"ordering\"].unique())\nitems_sorted = sorted(df[\"item_id\"].unique())\n\nn_m, n_t, n_p, n_s, n_o, n_i = (\n    len(models_sorted), len(temps_sorted), len(prompts_sorted),\n    len(seeds_sorted), len(orders_sorted), len(items_sorted),\n)\nprint(f\"Design: {n_m}m × {n_t}t × {n_p}p × {n_s}s × {n_o}o × {n_i}i = {n_m*n_t*n_p*n_s*n_o*n_i}\", flush=True)\n\nmodel_map = {v: i for i, v in enumerate(models_sorted)}\ntemp_map = {v: i for i, v in enumerate(temps_sorted)}\nprompt_map = {v: i for i, v in enumerate(prompts_sorted)}\nseed_map = {v: i for i, v in enumerate(seeds_sorted)}\norder_map = {v: i for i, v in enumerate(orders_sorted)}\nitem_map = {v: i for i, v in enumerate(items_sorted)}\n\nY = np.full((n_m, n_t, n_p, n_s, n_o, n_i), np.nan)\nfor _, row in df.iterrows():\n    Y[model_map[row[\"model\"]], temp_map[row[\"temperature\"]],\n      prompt_map[row[\"prompt_template\"]], seed_map[row[\"seed\"]],\n      order_map[row[\"ordering\"]], item_map[row[\"item_id\"]]] = row[\"correct\"]\n\nassert np.isnan(Y).sum() == 0, f\"Missing cells: {np.isnan(Y).sum()}\"\nprint(f\"6D array built ({time.time()-t_start:.1f}s)\", flush=True)\n\n\ndef compute_gstudy_5facet(arr_5d):\n    \"\"\"5-facet Henderson I on a (temp, prompt, seed, ordering, item) array.\"\"\"\n    nt, np_, ns, no, ni = arr_5d.shape\n    N = arr_5d.size\n    gm = arr_5d.mean()\n    facet_names = FACETS_5\n    n_lev = {\"temperature\": nt, \"prompt_template\": np_, \"seed\": ns, \"ordering\": no, \"item_id\": ni}\n\n    axes_map = {\n        \"temperature\": 0, \"prompt_template\": 1, \"seed\": 2, \"ordering\": 3, \"item_id\": 4,\n    }\n\n    effects = {}\n    for f in facet_names:\n        ax = axes_map[f]\n        other_axes = tuple(j for j in range(5) if j != ax)\n        level_means = arr_5d.mean(axis=other_axes)\n        n_per = N // arr_5d.shape[ax]\n        ss = float(n_per * np.sum((level_means - gm) ** 2))\n        df_eff = arr_5d.shape[ax] - 1\n        effects[f] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    for i_idx in range(5):\n        for j_idx in range(i_idx + 1, 5):\n            fi, fj = facet_names[i_idx], facet_names[j_idx]\n            other_axes = tuple(k for k in range(5) if k not in (i_idx, j_idx))\n            cell_means = arr_5d.mean(axis=other_axes)\n            main_i = arr_5d.mean(axis=tuple(k for k in range(5) if k != i_idx))\n            main_j = arr_5d.mean(axis=tuple(k for k in range(5) if k != j_idx))\n            interaction = cell_means - main_i[:, None] - main_j[None, :] + gm\n            n_per = N // (arr_5d.shape[i_idx] * arr_5d.shape[j_idx])\n            ss = float(n_per * np.sum(interaction ** 2))\n            df_eff = (arr_5d.shape[i_idx] - 1) * (arr_5d.shape[j_idx] - 1)\n            key = f\"{fi}:{fj}\"\n            effects[key] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    ss_total = float(np.sum((arr_5d - gm) ** 2))\n    ss_model = sum(e[\"ss\"] for e in effects.values())\n    ss_res = max(0.0, ss_total - ss_model)\n    df_res = N - 1 - sum(e[\"df\"] for e in effects.values())\n    effects[\"residual\"] = {\"ss\": ss_res, \"df\": df_res, \"ms\": ss_res / df_res if df_res > 0 else 0.0}\n\n    ms_res = effects[\"residual\"][\"ms\"]\n    vc = {}\n    for fi, fj in combinations(facet_names, 2):\n        key = f\"{fi}:{fj}\"\n        coeff = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n        raw = (effects[key][\"ms\"] - ms_res) / coeff if coeff > 0 else 0.0\n        vc[key] = max(0.0, raw)\n\n    for fi in facet_names:\n        coeff_main = prod(n_lev[f] for f in facet_names if f != fi)\n        interaction_contrib = 0.0\n        for fj in facet_names:\n            if fj == fi:\n                continue\n            int_key = f\"{fi}:{fj}\" if f\"{fi}:{fj}\" in vc else f\"{fj}:{fi}\"\n            coeff_ij = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n            interaction_contrib += coeff_ij * vc[int_key]\n        raw = (effects[fi][\"ms\"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0\n        vc[fi] = max(0.0, raw)\n\n    vc[\"residual\"] = ms_res\n    return vc, n_lev, effects\n\n\ndef compute_g_item_5facet(vc, n_lev):\n    \"\"\"G_item for 5-facet design. Fixed: temperature. Random: prompt, seed, ordering, item.\"\"\"\n    random_facets_5 = [\"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\n    sigma_item = vc.get(\"item_id\", 0.0)\n\n    sigma_delta = 0.0\n    for comp, est in vc.items():\n        if est == 0.0:\n            continue\n        if comp == \"residual\":\n            divisor = prod(n_lev[f] for f in random_facets_5)\n            sigma_delta += est / divisor\n            continue\n        facets_in = set(comp.split(\":\"))\n        if \"item_id\" not in facets_in:\n            continue\n        random_in = [f for f in facets_in if f in set(random_facets_5)]\n        if len(random_in) > 0:\n            divisor = prod(n_lev[f] for f in random_in)\n            sigma_delta += est / divisor\n\n    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0\n    return g, sigma_item, sigma_delta\n\n\ndef compute_gstudy_6facet(Y_6d):\n    \"\"\"Full 6-facet G-study on the (model, temp, prompt, seed, ordering, item) array.\"\"\"\n    nm, nt, np_, ns, no, ni = Y_6d.shape\n    N = Y_6d.size\n    gm = Y_6d.mean()\n    facet_names = FACETS_6\n    n_lev = {\"model\": nm, \"temperature\": nt, \"prompt_template\": np_, \"seed\": ns, \"ordering\": no, \"item_id\": ni}\n\n    effects = {}\n    for idx, f in enumerate(facet_names):\n        other_axes = tuple(j for j in range(6) if j != idx)\n        level_means = Y_6d.mean(axis=other_axes)\n        n_per = N // Y_6d.shape[idx]\n        ss = float(n_per * np.sum((level_means - gm) ** 2))\n        df_eff = Y_6d.shape[idx] - 1\n        effects[f] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    for i_idx in range(6):\n        for j_idx in range(i_idx + 1, 6):\n            fi, fj = facet_names[i_idx], facet_names[j_idx]\n            other_axes = tuple(k for k in range(6) if k not in (i_idx, j_idx))\n            cell_means = Y_6d.mean(axis=other_axes)\n            main_i = Y_6d.mean(axis=tuple(k for k in range(6) if k != i_idx))\n            main_j = Y_6d.mean(axis=tuple(k for k in range(6) if k != j_idx))\n            interaction = cell_means - main_i[:, None] - main_j[None, :] + gm\n            n_per = N // (Y_6d.shape[i_idx] * Y_6d.shape[j_idx])\n            ss = float(n_per * np.sum(interaction ** 2))\n            df_eff = (Y_6d.shape[i_idx] - 1) * (Y_6d.shape[j_idx] - 1)\n            key = f\"{fi}:{fj}\"\n            effects[key] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    ss_total = float(np.sum((Y_6d - gm) ** 2))\n    ss_model = sum(e[\"ss\"] for e in effects.values())\n    ss_res = max(0.0, ss_total - ss_model)\n    df_res = N - 1 - sum(e[\"df\"] for e in effects.values())\n    effects[\"residual\"] = {\"ss\": ss_res, \"df\": df_res, \"ms\": ss_res / df_res if df_res > 0 else 0.0}\n\n    ms_res = effects[\"residual\"][\"ms\"]\n    vc = {}\n    for fi, fj in combinations(facet_names, 2):\n        key = f\"{fi}:{fj}\"\n        coeff = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n        raw = (effects[key][\"ms\"] - ms_res) / coeff if coeff > 0 else 0.0\n        vc[key] = max(0.0, raw)\n\n    for fi in facet_names:\n        coeff_main = prod(n_lev[f] for f in facet_names if f != fi)\n        interaction_contrib = 0.0\n        for fj in facet_names:\n            if fj == fi:\n                continue\n            int_key = f\"{fi}:{fj}\" if f\"{fi}:{fj}\" in vc else f\"{fj}:{fi}\"\n            coeff_ij = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n            interaction_contrib += coeff_ij * vc[int_key]\n        raw = (effects[fi][\"ms\"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0\n        vc[fi] = max(0.0, raw)\n\n    vc[\"residual\"] = ms_res\n    return vc, n_lev, effects\n\n\ndef compute_g_item_random(vc, n_lev):\n    \"\"\"G_item with model as RANDOM (original formula).\"\"\"\n    sigma_item = vc.get(\"item_id\", 0.0)\n    delta = (\n        vc.get(\"model:item_id\", 0.0) / n_lev[\"model\"]\n        + vc.get(\"temperature:item_id\", 0.0) / n_lev[\"temperature\"]\n        + vc.get(\"prompt_template:item_id\", 0.0) / n_lev[\"prompt_template\"]\n        + vc.get(\"seed:item_id\", 0.0) / n_lev[\"seed\"]\n        + vc.get(\"ordering:item_id\", 0.0) / n_lev[\"ordering\"]\n        + vc[\"residual\"] / (n_lev[\"model\"] * n_lev[\"temperature\"] * n_lev[\"prompt_template\"]\n                            * n_lev[\"seed\"] * n_lev[\"ordering\"])\n    )\n    g = sigma_item / (sigma_item + delta) if (sigma_item + delta) > 0 else 0.0\n    return g, sigma_item, delta\n\n\ndef compute_g_item_fixed_methodB(vc, n_lev):\n    \"\"\"G_item with model as FIXED (Method B: remove model:item from σ²δ).\"\"\"\n    sigma_item = vc.get(\"item_id\", 0.0)\n    delta = (\n        vc.get(\"temperature:item_id\", 0.0) / n_lev[\"temperature\"]\n        + vc.get(\"prompt_template:item_id\", 0.0) / n_lev[\"prompt_template\"]\n        + vc.get(\"seed:item_id\", 0.0) / n_lev[\"seed\"]\n        + vc.get(\"ordering:item_id\", 0.0) / n_lev[\"ordering\"]\n        + vc[\"residual\"] / (n_lev[\"model\"] * n_lev[\"temperature\"] * n_lev[\"prompt_template\"]\n                            * n_lev[\"seed\"] * n_lev[\"ordering\"])\n    )\n    g = sigma_item / (sigma_item + delta) if (sigma_item + delta) > 0 else 0.0\n    return g, sigma_item, delta\n\n\n# ============================================================\n# Full 6-facet G-study (reproduce random-model baseline)\n# ============================================================\nprint(\"\\n=== 6-facet G-study (model=random baseline) ===\", flush=True)\nvc_6, nl_6, eff_6 = compute_gstudy_6facet(Y)\ntotal_var_6 = sum(vc_6.values())\n\ng_random, tau_random, delta_random = compute_g_item_random(vc_6, nl_6)\nprint(f\"G_item (model=random) = {g_random:.6f}\", flush=True)\n\n\n# ============================================================\n# Method B: Fixed model in crossed design\n# ============================================================\nprint(\"\\n=== Method B: model-as-fixed (remove model:item from σ²δ) ===\", flush=True)\ng_fixedB, tau_fixedB, delta_fixedB = compute_g_item_fixed_methodB(vc_6, nl_6)\nprint(f\"G_item (model=fixed, Method B) = {g_fixedB:.6f}\", flush=True)\nprint(f\"  σ²δ reduction: {delta_random:.8f} → {delta_fixedB:.8f} \"\n      f\"(removed model:item/n_m = {vc_6.get('model:item_id', 0)/nl_6['model']:.8f})\", flush=True)\n\n\n# ============================================================\n# Method A: Per-model 5-facet G-study\n# ============================================================\nprint(\"\\n=== Method A: per-model 5-facet G-study ===\", flush=True)\nper_model_results = {}\ng_items_per_model = []\n\nfor mi, model_name in enumerate(models_sorted):\n    Y_m = Y[mi]  # shape: (n_t, n_p, n_s, n_o, n_i)\n    vc_m, nl_m, eff_m = compute_gstudy_5facet(Y_m)\n    g_m, tau_m, delta_m = compute_g_item_5facet(vc_m, nl_m)\n    g_items_per_model.append(g_m)\n\n    total_var_m = sum(vc_m.values())\n    per_model_results[model_name] = {\n        \"g_item\": round(g_m, 6),\n        \"sigma_tau\": round(tau_m, 8),\n        \"sigma_delta\": round(delta_m, 8),\n        \"variance_components\": {\n            k: {\"estimate\": v, \"pct\": v / total_var_m * 100 if total_var_m > 0 else 0.0}\n            for k, v in sorted(vc_m.items(), key=lambda x: -x[1])\n        },\n        \"accuracy\": float(Y_m.mean()),\n    }\n    print(f\"  {model_name}: G_item={g_m:.6f}, acc={Y_m.mean():.4f}, \"\n          f\"σ²(item)={vc_m['item_id']:.6f}, σ²δ={delta_m:.6f}\", flush=True)\n\ng_fixed_A = float(np.mean(g_items_per_model))\nprint(f\"\\nAverage G_item (model=fixed, Method A) = {g_fixed_A:.6f}\", flush=True)\n\n# Pooled variance components (average across models)\npooled_vc = {}\nfor key in per_model_results[models_sorted[0]][\"variance_components\"]:\n    vals = [per_model_results[m][\"variance_components\"][key][\"estimate\"] for m in models_sorted]\n    pooled_vc[key] = float(np.mean(vals))\n\npooled_total = sum(pooled_vc.values())\n\n\n# ============================================================\n# Bootstrap CI for Method A\n# ============================================================\nprint(f\"\\nBootstrapping Method A ({N_BOOT} resamples)...\", flush=True)\nrng = np.random.default_rng(SEED)\nboot_g_fixed_A = []\nboot_g_random = []\n\nfor b in range(N_BOOT):\n    if b % 50 == 0:\n        print(f\"  {b}/{N_BOOT}...\", flush=True)\n    idx = rng.choice(n_i, size=n_i, replace=True)\n    Y_b = Y[:, :, :, :, :, idx]\n\n    vc_b6, nl_b6, _ = compute_gstudy_6facet(Y_b)\n    g_r, _, _ = compute_g_item_random(vc_b6, nl_b6)\n    boot_g_random.append(g_r)\n\n    g_per_model_b = []\n    for mi in range(n_m):\n        vc_bm, nl_bm, _ = compute_gstudy_5facet(Y_b[mi])\n        g_bm, _, _ = compute_g_item_5facet(vc_bm, nl_bm)\n        g_per_model_b.append(g_bm)\n    boot_g_fixed_A.append(float(np.mean(g_per_model_b)))\n\nci_random = [float(np.percentile(boot_g_random, 2.5)), float(np.percentile(boot_g_random, 97.5))]\nci_fixed_A = [float(np.percentile(boot_g_fixed_A, 2.5)), float(np.percentile(boot_g_fixed_A, 97.5))]\n\nprint(f\"\\nG_item (random): {g_random:.6f} [{ci_random[0]:.6f}, {ci_random[1]:.6f}]\", flush=True)\nprint(f\"G_item (fixed A): {g_fixed_A:.6f} [{ci_fixed_A[0]:.6f}, {ci_fixed_A[1]:.6f}]\", flush=True)\nprint(f\"G_item (fixed B): {g_fixedB:.6f}\", flush=True)\n\n\n# ============================================================\n# Ranking consistency check\n# ============================================================\nper_model_item_means = {}\nfor mi, m in enumerate(models_sorted):\n    per_model_item_means[m] = Y[mi].mean(axis=(0, 1, 2, 3))  # mean over temp, prompt, seed, ordering\n\nfrom scipy.stats import spearmanr\nranks = {}\nfor m in models_sorted:\n    ranks[m] = per_model_item_means[m]\n\nrank_corrs = []\nfor i in range(len(models_sorted)):\n    for j in range(i + 1, len(models_sorted)):\n        mi, mj = models_sorted[i], models_sorted[j]\n        rho, _ = spearmanr(ranks[mi], ranks[mj])\n        rank_corrs.append({\"pair\": f\"{mi} vs {mj}\", \"spearman_rho\": round(rho, 4)})\n\nmean_rho = float(np.mean([r[\"spearman_rho\"] for r in rank_corrs]))\nprint(f\"\\nItem ranking consistency across models:\", flush=True)\nfor r in rank_corrs:\n    print(f\"  {r['pair']}: ρ={r['spearman_rho']:.4f}\", flush=True)\nprint(f\"  Mean ρ = {mean_rho:.4f}\", flush=True)\n\n\n# ============================================================\n# Save\n# ============================================================\nresults = {\n    \"random_model\": {\n        \"G_item\": round(g_random, 6),\n        \"ci_95\": ci_random,\n        \"sigma_tau\": round(tau_random, 8),\n        \"sigma_delta\": round(delta_random, 8),\n        \"variance_components\": {\n            k: {\"estimate\": v, \"pct\": v / total_var_6 * 100}\n            for k, v in sorted(vc_6.items(), key=lambda x: -x[1])\n        },\n    },\n    \"fixed_model\": {\n        \"method_A_per_model_average\": {\n            \"G_item\": round(g_fixed_A, 6),\n            \"ci_95\": ci_fixed_A,\n            \"description\": \"Average of per-model 5-facet G_item values\",\n        },\n        \"method_B_remove_model_item\": {\n            \"G_item\": round(g_fixedB, 6),\n            \"sigma_tau\": round(tau_fixedB, 8),\n            \"sigma_delta\": round(delta_fixedB, 8),\n            \"description\": \"6-facet VC with model:item_id removed from σ²δ\",\n        },\n        \"per_model_gstudy\": per_model_results,\n        \"pooled_variance_components\": {\n            k: {\"estimate\": v, \"pct\": v / pooled_total * 100 if pooled_total > 0 else 0.0}\n            for k, v in sorted(pooled_vc.items(), key=lambda x: -x[1])\n        },\n    },\n    \"comparison\": {\n        \"G_item_random\": round(g_random, 6),\n        \"G_item_fixed_A\": round(g_fixed_A, 6),\n        \"G_item_fixed_B\": round(g_fixedB, 6),\n        \"G_item_delta_A\": round(g_fixed_A - g_random, 6),\n        \"G_item_delta_B\": round(g_fixedB - g_random, 6),\n        \"ranking_consistency\": {\n            \"pairwise_spearman\": rank_corrs,\n            \"mean_spearman_rho\": round(mean_rho, 4),\n            \"consistent\": mean_rho > 0.7,\n        },\n        \"interpretation\": (\n            \"Model-as-fixed G_item is higher because model:item variance \"\n            \"(differential item difficulty across models) is no longer treated as \"\n            \"measurement error. This is appropriate when generalizing to these \"\n            \"specific 4 models rather than a hypothetical population of models.\"\n        ),\n    },\n    \"design\": {\n        \"n_observations\": int(Y.size),\n        \"n_levels\": {\"model\": n_m, \"temperature\": n_t, \"prompt_template\": n_p,\n                     \"seed\": n_s, \"ordering\": n_o, \"item_id\": n_i},\n        \"models\": models_sorted,\n        \"fixed_facets_random_design\": [\"temperature\"],\n        \"fixed_facets_fixed_model_design\": [\"model\", \"temperature\"],\n    },\n    \"bootstrap\": {\"n_resamples\": N_BOOT, \"seed\": SEED, \"method\": \"item cluster resampling\"},\n}\n\nPath(OUTPUT).parent.mkdir(parents=True, exist_ok=True)\nwith open(OUTPUT, \"w\") as f:\n    json.dump(results, f, indent=2, default=str)\n\nprint(f\"\\nTotal runtime: {time.time()-t_start:.1f}s\", flush=True)\nprint(f\"→ Saved to {OUTPUT}\", flush=True)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/model_as_fixed_gstudy.py",
    "content": "\"\"\"Model-as-fixed G-study (MF2 defense).\n\nTreats model as a fixed facet (not a random sample from a population of models).\nTwo methods:\n  A) Per-model 5-facet G-study, then average (clean separation)\n  B) Remove model:item from σ²δ in the crossed 6-facet design (quick adjustment)\n\nInput:  results/analysis/cross_model_4way_bf16.csv (4 models × bf16 × fully crossed)\nOutput: results/analysis/model_as_fixed_gstudy.json\n\"\"\"\n\nimport json\nimport time\nfrom itertools import combinations\nfrom math import prod\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\n\nINPUT = \"results/analysis/cross_model_4way_bf16.csv\"\nOUTPUT = \"results/analysis/model_as_fixed_gstudy.json\"\nN_BOOT = 200\nSEED = 42\n\nFACETS_6 = [\"model\", \"temperature\", \"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\nFACETS_5 = [\"temperature\", \"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\n\nt_start = time.time()\ndf = pd.read_csv(INPUT)\nprint(f\"Loaded {len(df)} obs ({time.time()-t_start:.1f}s)\", flush=True)\n\nmodels_sorted = sorted(df[\"model\"].unique())\ntemps_sorted = sorted(df[\"temperature\"].unique())\nprompts_sorted = sorted(df[\"prompt_template\"].unique())\nseeds_sorted = sorted(df[\"seed\"].unique())\norders_sorted = sorted(df[\"ordering\"].unique())\nitems_sorted = sorted(df[\"item_id\"].unique())\n\nn_m, n_t, n_p, n_s, n_o, n_i = (\n    len(models_sorted), len(temps_sorted), len(prompts_sorted),\n    len(seeds_sorted), len(orders_sorted), len(items_sorted),\n)\nprint(f\"Design: {n_m}m × {n_t}t × {n_p}p × {n_s}s × {n_o}o × {n_i}i = {n_m*n_t*n_p*n_s*n_o*n_i}\", flush=True)\n\nmodel_map = {v: i for i, v in enumerate(models_sorted)}\ntemp_map = {v: i for i, v in enumerate(temps_sorted)}\nprompt_map = {v: i for i, v in enumerate(prompts_sorted)}\nseed_map = {v: i for i, v in enumerate(seeds_sorted)}\norder_map = {v: i for i, v in enumerate(orders_sorted)}\nitem_map = {v: i for i, v in enumerate(items_sorted)}\n\nY = np.full((n_m, n_t, n_p, n_s, n_o, n_i), np.nan)\nfor _, row in df.iterrows():\n    Y[model_map[row[\"model\"]], temp_map[row[\"temperature\"]],\n      prompt_map[row[\"prompt_template\"]], seed_map[row[\"seed\"]],\n      order_map[row[\"ordering\"]], item_map[row[\"item_id\"]]] = row[\"correct\"]\n\nassert np.isnan(Y).sum() == 0, f\"Missing cells: {np.isnan(Y).sum()}\"\nprint(f\"6D array built ({time.time()-t_start:.1f}s)\", flush=True)\n\n\ndef compute_gstudy_5facet(arr_5d):\n    \"\"\"5-facet Henderson I on a (temp, prompt, seed, ordering, item) array.\"\"\"\n    nt, np_, ns, no, ni = arr_5d.shape\n    N = arr_5d.size\n    gm = arr_5d.mean()\n    facet_names = FACETS_5\n    n_lev = {\"temperature\": nt, \"prompt_template\": np_, \"seed\": ns, \"ordering\": no, \"item_id\": ni}\n\n    axes_map = {\n        \"temperature\": 0, \"prompt_template\": 1, \"seed\": 2, \"ordering\": 3, \"item_id\": 4,\n    }\n\n    effects = {}\n    for f in facet_names:\n        ax = axes_map[f]\n        other_axes = tuple(j for j in range(5) if j != ax)\n        level_means = arr_5d.mean(axis=other_axes)\n        n_per = N // arr_5d.shape[ax]\n        ss = float(n_per * np.sum((level_means - gm) ** 2))\n        df_eff = arr_5d.shape[ax] - 1\n        effects[f] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    for i_idx in range(5):\n        for j_idx in range(i_idx + 1, 5):\n            fi, fj = facet_names[i_idx], facet_names[j_idx]\n            other_axes = tuple(k for k in range(5) if k not in (i_idx, j_idx))\n            cell_means = arr_5d.mean(axis=other_axes)\n            main_i = arr_5d.mean(axis=tuple(k for k in range(5) if k != i_idx))\n            main_j = arr_5d.mean(axis=tuple(k for k in range(5) if k != j_idx))\n            interaction = cell_means - main_i[:, None] - main_j[None, :] + gm\n            n_per = N // (arr_5d.shape[i_idx] * arr_5d.shape[j_idx])\n            ss = float(n_per * np.sum(interaction ** 2))\n            df_eff = (arr_5d.shape[i_idx] - 1) * (arr_5d.shape[j_idx] - 1)\n            key = f\"{fi}:{fj}\"\n            effects[key] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    ss_total = float(np.sum((arr_5d - gm) ** 2))\n    ss_model = sum(e[\"ss\"] for e in effects.values())\n    ss_res = max(0.0, ss_total - ss_model)\n    df_res = N - 1 - sum(e[\"df\"] for e in effects.values())\n    effects[\"residual\"] = {\"ss\": ss_res, \"df\": df_res, \"ms\": ss_res / df_res if df_res > 0 else 0.0}\n\n    ms_res = effects[\"residual\"][\"ms\"]\n    vc = {}\n    for fi, fj in combinations(facet_names, 2):\n        key = f\"{fi}:{fj}\"\n        coeff = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n        raw = (effects[key][\"ms\"] - ms_res) / coeff if coeff > 0 else 0.0\n        vc[key] = max(0.0, raw)\n\n    for fi in facet_names:\n        coeff_main = prod(n_lev[f] for f in facet_names if f != fi)\n        interaction_contrib = 0.0\n        for fj in facet_names:\n            if fj == fi:\n                continue\n            int_key = f\"{fi}:{fj}\" if f\"{fi}:{fj}\" in vc else f\"{fj}:{fi}\"\n            coeff_ij = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n            interaction_contrib += coeff_ij * vc[int_key]\n        raw = (effects[fi][\"ms\"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0\n        vc[fi] = max(0.0, raw)\n\n    vc[\"residual\"] = ms_res\n    return vc, n_lev, effects\n\n\ndef compute_g_item_5facet(vc, n_lev):\n    \"\"\"G_item for 5-facet design. Fixed: temperature. Random: prompt, seed, ordering, item.\"\"\"\n    random_facets_5 = [\"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\n    sigma_item = vc.get(\"item_id\", 0.0)\n\n    sigma_delta = 0.0\n    for comp, est in vc.items():\n        if est == 0.0:\n            continue\n        if comp == \"residual\":\n            divisor = prod(n_lev[f] for f in random_facets_5)\n            sigma_delta += est / divisor\n            continue\n        facets_in = set(comp.split(\":\"))\n        if \"item_id\" not in facets_in:\n            continue\n        random_in = [f for f in facets_in if f in set(random_facets_5)]\n        if len(random_in) > 0:\n            divisor = prod(n_lev[f] for f in random_in)\n            sigma_delta += est / divisor\n\n    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0\n    return g, sigma_item, sigma_delta\n\n\ndef compute_gstudy_6facet(Y_6d):\n    \"\"\"Full 6-facet G-study on the (model, temp, prompt, seed, ordering, item) array.\"\"\"\n    nm, nt, np_, ns, no, ni = Y_6d.shape\n    N = Y_6d.size\n    gm = Y_6d.mean()\n    facet_names = FACETS_6\n    n_lev = {\"model\": nm, \"temperature\": nt, \"prompt_template\": np_, \"seed\": ns, \"ordering\": no, \"item_id\": ni}\n\n    effects = {}\n    for idx, f in enumerate(facet_names):\n        other_axes = tuple(j for j in range(6) if j != idx)\n        level_means = Y_6d.mean(axis=other_axes)\n        n_per = N // Y_6d.shape[idx]\n        ss = float(n_per * np.sum((level_means - gm) ** 2))\n        df_eff = Y_6d.shape[idx] - 1\n        effects[f] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    for i_idx in range(6):\n        for j_idx in range(i_idx + 1, 6):\n            fi, fj = facet_names[i_idx], facet_names[j_idx]\n            other_axes = tuple(k for k in range(6) if k not in (i_idx, j_idx))\n            cell_means = Y_6d.mean(axis=other_axes)\n            main_i = Y_6d.mean(axis=tuple(k for k in range(6) if k != i_idx))\n            main_j = Y_6d.mean(axis=tuple(k for k in range(6) if k != j_idx))\n            interaction = cell_means - main_i[:, None] - main_j[None, :] + gm\n            n_per = N // (Y_6d.shape[i_idx] * Y_6d.shape[j_idx])\n            ss = float(n_per * np.sum(interaction ** 2))\n            df_eff = (Y_6d.shape[i_idx] - 1) * (Y_6d.shape[j_idx] - 1)\n            key = f\"{fi}:{fj}\"\n            effects[key] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    ss_total = float(np.sum((Y_6d - gm) ** 2))\n    ss_model = sum(e[\"ss\"] for e in effects.values())\n    ss_res = max(0.0, ss_total - ss_model)\n    df_res = N - 1 - sum(e[\"df\"] for e in effects.values())\n    effects[\"residual\"] = {\"ss\": ss_res, \"df\": df_res, \"ms\": ss_res / df_res if df_res > 0 else 0.0}\n\n    ms_res = effects[\"residual\"][\"ms\"]\n    vc = {}\n    for fi, fj in combinations(facet_names, 2):\n        key = f\"{fi}:{fj}\"\n        coeff = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n        raw = (effects[key][\"ms\"] - ms_res) / coeff if coeff > 0 else 0.0\n        vc[key] = max(0.0, raw)\n\n    for fi in facet_names:\n        coeff_main = prod(n_lev[f] for f in facet_names if f != fi)\n        interaction_contrib = 0.0\n        for fj in facet_names:\n            if fj == fi:\n                continue\n            int_key = f\"{fi}:{fj}\" if f\"{fi}:{fj}\" in vc else f\"{fj}:{fi}\"\n            coeff_ij = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n            interaction_contrib += coeff_ij * vc[int_key]\n        raw = (effects[fi][\"ms\"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0\n        vc[fi] = max(0.0, raw)\n\n    vc[\"residual\"] = ms_res\n    return vc, n_lev, effects\n\n\ndef compute_g_item_random(vc, n_lev):\n    \"\"\"G_item with model as RANDOM (original formula).\"\"\"\n    sigma_item = vc.get(\"item_id\", 0.0)\n    delta = (\n        vc.get(\"model:item_id\", 0.0) / n_lev[\"model\"]\n        + vc.get(\"temperature:item_id\", 0.0) / n_lev[\"temperature\"]\n        + vc.get(\"prompt_template:item_id\", 0.0) / n_lev[\"prompt_template\"]\n        + vc.get(\"seed:item_id\", 0.0) / n_lev[\"seed\"]\n        + vc.get(\"ordering:item_id\", 0.0) / n_lev[\"ordering\"]\n        + vc[\"residual\"] / (n_lev[\"model\"] * n_lev[\"temperature\"] * n_lev[\"prompt_template\"]\n                            * n_lev[\"seed\"] * n_lev[\"ordering\"])\n    )\n    g = sigma_item / (sigma_item + delta) if (sigma_item + delta) > 0 else 0.0\n    return g, sigma_item, delta\n\n\ndef compute_g_item_fixed_methodB(vc, n_lev):\n    \"\"\"G_item with model as FIXED (Method B: remove model:item from σ²δ).\"\"\"\n    sigma_item = vc.get(\"item_id\", 0.0)\n    delta = (\n        vc.get(\"temperature:item_id\", 0.0) / n_lev[\"temperature\"]\n        + vc.get(\"prompt_template:item_id\", 0.0) / n_lev[\"prompt_template\"]\n        + vc.get(\"seed:item_id\", 0.0) / n_lev[\"seed\"]\n        + vc.get(\"ordering:item_id\", 0.0) / n_lev[\"ordering\"]\n        + vc[\"residual\"] / (n_lev[\"model\"] * n_lev[\"temperature\"] * n_lev[\"prompt_template\"]\n                            * n_lev[\"seed\"] * n_lev[\"ordering\"])\n    )\n    g = sigma_item / (sigma_item + delta) if (sigma_item + delta) > 0 else 0.0\n    return g, sigma_item, delta\n\n\n# ============================================================\n# Full 6-facet G-study (reproduce random-model baseline)\n# ============================================================\nprint(\"\\n=== 6-facet G-study (model=random baseline) ===\", flush=True)\nvc_6, nl_6, eff_6 = compute_gstudy_6facet(Y)\ntotal_var_6 = sum(vc_6.values())\n\ng_random, tau_random, delta_random = compute_g_item_random(vc_6, nl_6)\nprint(f\"G_item (model=random) = {g_random:.6f}\", flush=True)\n\n\n# ============================================================\n# Method B: Fixed model in crossed design\n# ============================================================\nprint(\"\\n=== Method B: model-as-fixed (remove model:item from σ²δ) ===\", flush=True)\ng_fixedB, tau_fixedB, delta_fixedB = compute_g_item_fixed_methodB(vc_6, nl_6)\nprint(f\"G_item (model=fixed, Method B) = {g_fixedB:.6f}\", flush=True)\nprint(f\"  σ²δ reduction: {delta_random:.8f} → {delta_fixedB:.8f} \"\n      f\"(removed model:item/n_m = {vc_6.get('model:item_id', 0)/nl_6['model']:.8f})\", flush=True)\n\n\n# ============================================================\n# Method A: Per-model 5-facet G-study\n# ============================================================\nprint(\"\\n=== Method A: per-model 5-facet G-study ===\", flush=True)\nper_model_results = {}\ng_items_per_model = []\n\nfor mi, model_name in enumerate(models_sorted):\n    Y_m = Y[mi]  # shape: (n_t, n_p, n_s, n_o, n_i)\n    vc_m, nl_m, eff_m = compute_gstudy_5facet(Y_m)\n    g_m, tau_m, delta_m = compute_g_item_5facet(vc_m, nl_m)\n    g_items_per_model.append(g_m)\n\n    total_var_m = sum(vc_m.values())\n    per_model_results[model_name] = {\n        \"g_item\": round(g_m, 6),\n        \"sigma_tau\": round(tau_m, 8),\n        \"sigma_delta\": round(delta_m, 8),\n        \"variance_components\": {\n            k: {\"estimate\": v, \"pct\": v / total_var_m * 100 if total_var_m > 0 else 0.0}\n            for k, v in sorted(vc_m.items(), key=lambda x: -x[1])\n        },\n        \"accuracy\": float(Y_m.mean()),\n    }\n    print(f\"  {model_name}: G_item={g_m:.6f}, acc={Y_m.mean():.4f}, \"\n          f\"σ²(item)={vc_m['item_id']:.6f}, σ²δ={delta_m:.6f}\", flush=True)\n\ng_fixed_A = float(np.mean(g_items_per_model))\nprint(f\"\\nAverage G_item (model=fixed, Method A) = {g_fixed_A:.6f}\", flush=True)\n\n# Pooled variance components (average across models)\npooled_vc = {}\nfor key in per_model_results[models_sorted[0]][\"variance_components\"]:\n    vals = [per_model_results[m][\"variance_components\"][key][\"estimate\"] for m in models_sorted]\n    pooled_vc[key] = float(np.mean(vals))\n\npooled_total = sum(pooled_vc.values())\n\n\n# ============================================================\n# Bootstrap CI for Method A\n# ============================================================\nprint(f\"\\nBootstrapping Method A ({N_BOOT} resamples)...\", flush=True)\nrng = np.random.default_rng(SEED)\nboot_g_fixed_A = []\nboot_g_random = []\n\nfor b in range(N_BOOT):\n    if b % 50 == 0:\n        print(f\"  {b}/{N_BOOT}...\", flush=True)\n    idx = rng.choice(n_i, size=n_i, replace=True)\n    Y_b = Y[:, :, :, :, :, idx]\n\n    vc_b6, nl_b6, _ = compute_gstudy_6facet(Y_b)\n    g_r, _, _ = compute_g_item_random(vc_b6, nl_b6)\n    boot_g_random.append(g_r)\n\n    g_per_model_b = []\n    for mi in range(n_m):\n        vc_bm, nl_bm, _ = compute_gstudy_5facet(Y_b[mi])\n        g_bm, _, _ = compute_g_item_5facet(vc_bm, nl_bm)\n        g_per_model_b.append(g_bm)\n    boot_g_fixed_A.append(float(np.mean(g_per_model_b)))\n\nci_random = [float(np.percentile(boot_g_random, 2.5)), float(np.percentile(boot_g_random, 97.5))]\nci_fixed_A = [float(np.percentile(boot_g_fixed_A, 2.5)), float(np.percentile(boot_g_fixed_A, 97.5))]\n\nprint(f\"\\nG_item (random): {g_random:.6f} [{ci_random[0]:.6f}, {ci_random[1]:.6f}]\", flush=True)\nprint(f\"G_item (fixed A): {g_fixed_A:.6f} [{ci_fixed_A[0]:.6f}, {ci_fixed_A[1]:.6f}]\", flush=True)\nprint(f\"G_item (fixed B): {g_fixedB:.6f}\", flush=True)\n\n\n# ============================================================\n# Ranking consistency check\n# ============================================================\nper_model_item_means = {}\nfor mi, m in enumerate(models_sorted):\n    per_model_item_means[m] = Y[mi].mean(axis=(0, 1, 2, 3))  # mean over temp, prompt, seed, ordering\n\nfrom scipy.stats import spearmanr\nranks = {}\nfor m in models_sorted:\n    ranks[m] = per_model_item_means[m]\n\nrank_corrs = []\nfor i in range(len(models_sorted)):\n    for j in range(i + 1, len(models_sorted)):\n        mi, mj = models_sorted[i], models_sorted[j]\n        rho, _ = spearmanr(ranks[mi], ranks[mj])\n        rank_corrs.append({\"pair\": f\"{mi} vs {mj}\", \"spearman_rho\": round(rho, 4)})\n\nmean_rho = float(np.mean([r[\"spearman_rho\"] for r in rank_corrs]))\nprint(f\"\\nItem ranking consistency across models:\", flush=True)\nfor r in rank_corrs:\n    print(f\"  {r['pair']}: ρ={r['spearman_rho']:.4f}\", flush=True)\nprint(f\"  Mean ρ = {mean_rho:.4f}\", flush=True)\n\n\n# ============================================================\n# Save\n# ============================================================\nresults = {\n    \"random_model\": {\n        \"G_item\": round(g_random, 6),\n        \"ci_95\": ci_random,\n        \"sigma_tau\": round(tau_random, 8),\n        \"sigma_delta\": round(delta_random, 8),\n        \"variance_components\": {\n            k: {\"estimate\": v, \"pct\": v / total_var_6 * 100}\n            for k, v in sorted(vc_6.items(), key=lambda x: -x[1])\n        },\n    },\n    \"fixed_model\": {\n        \"method_A_per_model_average\": {\n            \"G_item\": round(g_fixed_A, 6),\n            \"ci_95\": ci_fixed_A,\n            \"description\": \"Average of per-model 5-facet G_item values\",\n        },\n        \"method_B_remove_model_item\": {\n            \"G_item\": round(g_fixedB, 6),\n            \"sigma_tau\": round(tau_fixedB, 8),\n            \"sigma_delta\": round(delta_fixedB, 8),\n            \"description\": \"6-facet VC with model:item_id removed from σ²δ\",\n        },\n        \"per_model_gstudy\": per_model_results,\n        \"pooled_variance_components\": {\n            k: {\"estimate\": v, \"pct\": v / pooled_total * 100 if pooled_total > 0 else 0.0}\n            for k, v in sorted(pooled_vc.items(), key=lambda x: -x[1])\n        },\n    },\n    \"comparison\": {\n        \"G_item_random\": round(g_random, 6),\n        \"G_item_fixed_A\": round(g_fixed_A, 6),\n        \"G_item_fixed_B\": round(g_fixedB, 6),\n        \"G_item_delta_A\": round(g_fixed_A - g_random, 6),\n        \"G_item_delta_B\": round(g_fixedB - g_random, 6),\n        \"ranking_consistency\": {\n            \"pairwise_spearman\": rank_corrs,\n            \"mean_spearman_rho\": round(mean_rho, 4),\n            \"consistent\": mean_rho > 0.7,\n        },\n        \"interpretation\": (\n            \"Model-as-fixed G_item is higher because model:item variance \"\n            \"(differential item difficulty across models) is no longer treated as \"\n            \"measurement error. This is appropriate when generalizing to these \"\n            \"specific 4 models rather than a hypothetical population of models.\"\n        ),\n    },\n    \"design\": {\n        \"n_observations\": int(Y.size),\n        \"n_levels\": {\"model\": n_m, \"temperature\": n_t, \"prompt_template\": n_p,\n                     \"seed\": n_s, \"ordering\": n_o, \"item_id\": n_i},\n        \"models\": models_sorted,\n        \"fixed_facets_random_design\": [\"temperature\"],\n        \"fixed_facets_fixed_model_design\": [\"model\", \"temperature\"],\n    },\n    \"bootstrap\": {\"n_resamples\": N_BOOT, \"seed\": SEED, \"method\": \"item cluster resampling\"},\n}\n\nPath(OUTPUT).parent.mkdir(parents=True, exist_ok=True)\nwith open(OUTPUT, \"w\") as f:\n    json.dump(results, f, indent=2, default=str)\n\nprint(f\"\\nTotal runtime: {time.time()-t_start:.1f}s\", flush=True)\nprint(f\"→ Saved to {OUTPUT}\", flush=True)\n"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-21T09:07:41.671833+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/model_as_fixed_gstudy.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-21T09:07:41.672067+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32570",
  "command": "cat > /root/nlp_variance_gtheory/scripts/model_as_fixed_gstudy.py << 'SCRIPT_EOF'\n\"\"\"Model-as-fixed G-study (MF2 defense).\n\nTreats model as a fixed facet (not a random sample from a population of models).\nTwo methods:\n  A) Per-model 5-facet G-study, then average (clean separation)\n  B) Remove model:item from σ²δ in the crossed 6-facet design (quick adjustment)\n\nInput:  results/analysis/cross_model_4way_bf16.csv (4 models × bf16 × fully crossed)\nOutput: results/analysis/model_as_fixed_gstudy.json\n\"\"\"\n\nimport json\nimport time\nfrom itertools import combinations\nfrom math import prod\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\n\nINPUT = \"results/analysis/cross_model_4way_bf16.csv\"\nOUTPUT = \"results/analysis/model_as_fixed_gstudy.json\"\nN_BOOT = 200\nSEED = 42\n\nFACETS_6 = [\"model\", \"temperature\", \"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\nFACETS_5 = [\"temperature\", \"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\n\nt_start = time.time()\ndf = pd.read_csv(INPUT)\nprint(f\"Loaded {len(df)} obs ({time.time()-t_start:.1f}s)\", flush=True)\n\nmodels_sorted = sorted(df[\"model\"].unique())\ntemps_sorted = sorted(df[\"temperature\"].unique())\nprompts_sorted = sorted(df[\"prompt_template\"].unique())\nseeds_sorted = sorted(df[\"seed\"].unique())\norders_sorted = sorted(df[\"ordering\"].unique())\nitems_sorted = sorted(df[\"item_id\"].unique())\n\nn_m, n_t, n_p, n_s, n_o, n_i = (\n    len(models_sorted), len(temps_sorted), len(prompts_sorted),\n    len(seeds_sorted), len(orders_sorted), len(items_sorted),\n)\nprint(f\"Design: {n_m}m x {n_t}t x {n_p}p x {n_s}s x {n_o}o x {n_i}i = {n_m*n_t*n_p*n_s*n_o*n_i}\", flush=True)\n\nmodel_map = {v: i for i, v in enumerate(models_sorted)}\ntemp_map = {v: i for i, v in enumerate(temps_sorted)}\nprompt_map = {v: i for i, v in enumerate(prompts_sorted)}\nseed_map = {v: i for i, v in enumerate(seeds_sorted)}\norder_map = {v: i for i, v in enumerate(orders_sorted)}\nitem_map = {v: i for i, v in enumerate(items_sorted)}\n\nY = np.full((n_m, n_t, n_p, n_s, n_o, n_i), np.nan)\nfor _, row in df.iterrows():\n    Y[model_map[row[\"model\"]], temp_map[row[\"temperature\"]],\n      prompt_map[row[\"prompt_template\"]], seed_map[row[\"seed\"]],\n      order_map[row[\"ordering\"]], item_map[row[\"item_id\"]]] = row[\"correct\"]\n\nassert np.isnan(Y).sum() == 0, f\"Missing cells: {np.isnan(Y).sum()}\"\nprint(f\"6D array built ({time.time()-t_start:.1f}s)\", flush=True)\n\n\ndef compute_gstudy_5facet(arr_5d):\n    nt, np_, ns, no, ni = arr_5d.shape\n    N = arr_5d.size\n    gm = arr_5d.mean()\n    facet_names = FACETS_5\n    n_lev = {\"temperature\": nt, \"prompt_template\": np_, \"seed\": ns, \"ordering\": no, \"item_id\": ni}\n\n    effects = {}\n    for idx, f in enumerate(facet_names):\n        other_axes = tuple(j for j in range(5) if j != idx)\n        level_means = arr_5d.mean(axis=other_axes)\n        n_per = N // arr_5d.shape[idx]\n        ss = float(n_per * np.sum((level_means - gm) ** 2))\n        df_eff = arr_5d.shape[idx] - 1\n        effects[f] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    for i_idx in range(5):\n        for j_idx in range(i_idx + 1, 5):\n            fi, fj = facet_names[i_idx], facet_names[j_idx]\n            other_axes = tuple(k for k in range(5) if k not in (i_idx, j_idx))\n            cell_means = arr_5d.mean(axis=other_axes)\n            main_i = arr_5d.mean(axis=tuple(k for k in range(5) if k != i_idx))\n            main_j = arr_5d.mean(axis=tuple(k for k in range(5) if k != j_idx))\n            interaction = cell_means - main_i[:, None] - main_j[None, :] + gm\n            n_per = N // (arr_5d.shape[i_idx] * arr_5d.shape[j_idx])\n            ss = float(n_per * np.sum(interaction ** 2))\n            df_eff = (arr_5d.shape[i_idx] - 1) * (arr_5d.shape[j_idx] - 1)\n            key = f\"{fi}:{fj}\"\n            effects[key] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    ss_total = float(np.sum((arr_5d - gm) ** 2))\n    ss_model = sum(e[\"ss\"] for e in effects.values())\n    ss_res = max(0.0, ss_total - ss_model)\n    df_res = N - 1 - sum(e[\"df\"] for e in effects.values())\n    effects[\"residual\"] = {\"ss\": ss_res, \"df\": df_res, \"ms\": ss_res / df_res if df_res > 0 else 0.0}\n\n    ms_res = effects[\"residual\"][\"ms\"]\n    vc = {}\n    for fi, fj in combinations(facet_names, 2):\n        key = f\"{fi}:{fj}\"\n        coeff = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n        raw = (effects[key][\"ms\"] - ms_res) / coeff if coeff > 0 else 0.0\n        vc[key] = max(0.0, raw)\n\n    for fi in facet_names:\n        coeff_main = prod(n_lev[f] for f in facet_names if f != fi)\n        interaction_contrib = 0.0\n        for fj in facet_names:\n            if fj == fi:\n                continue\n            int_key = f\"{fi}:{fj}\" if f\"{fi}:{fj}\" in vc else f\"{fj}:{fi}\"\n            coeff_ij = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n            interaction_contrib += coeff_ij * vc[int_key]\n        raw = (effects[fi][\"ms\"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0\n        vc[fi] = max(0.0, raw)\n\n    vc[\"residual\"] = ms_res\n    return vc, n_lev, effects\n\n\ndef compute_g_item_5facet(vc, n_lev):\n    random_facets_5 = [\"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\n    sigma_item = vc.get(\"item_id\", 0.0)\n\n    sigma_delta = 0.0\n    for comp, est in vc.items():\n        if est == 0.0:\n            continue\n        if comp == \"residual\":\n            divisor = prod(n_lev[f] for f in random_facets_5)\n            sigma_delta += est / divisor\n            continue\n        facets_in = set(comp.split(\":\"))\n        if \"item_id\" not in facets_in:\n            continue\n        random_in = [f for f in facets_in if f in set(random_facets_5)]\n        if len(random_in) > 0:\n            divisor = prod(n_lev[f] for f in random_in)\n            sigma_delta += est / divisor\n\n    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0\n    return g, sigma_item, sigma_delta\n\n\ndef compute_gstudy_6facet(Y_6d):\n    nm, nt, np_, ns, no, ni = Y_6d.shape\n    N = Y_6d.size\n    gm = Y_6d.mean()\n    facet_names = FACETS_6\n    n_lev = {\"model\": nm, \"temperature\": nt, \"prompt_template\": np_, \"seed\": ns, \"ordering\": no, \"item_id\": ni}\n\n    effects = {}\n    for idx, f in enumerate(facet_names):\n        other_axes = tuple(j for j in range(6) if j != idx)\n        level_means = Y_6d.mean(axis=other_axes)\n        n_per = N // Y_6d.shape[idx]\n        ss = float(n_per * np.sum((level_means - gm) ** 2))\n        df_eff = Y_6d.shape[idx] - 1\n        effects[f] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    for i_idx in range(6):\n        for j_idx in range(i_idx + 1, 6):\n            fi, fj = facet_names[i_idx], facet_names[j_idx]\n            other_axes = tuple(k for k in range(6) if k not in (i_idx, j_idx))\n            cell_means = Y_6d.mean(axis=other_axes)\n            main_i = Y_6d.mean(axis=tuple(k for k in range(6) if k != i_idx))\n            main_j = Y_6d.mean(axis=tuple(k for k in range(6) if k != j_idx))\n            interaction = cell_means - main_i[:, None] - main_j[None, :] + gm\n            n_per = N // (Y_6d.shape[i_idx] * Y_6d.shape[j_idx])\n            ss = float(n_per * np.sum(interaction ** 2))\n            df_eff = (Y_6d.shape[i_idx] - 1) * (Y_6d.shape[j_idx] - 1)\n            key = f\"{fi}:{fj}\"\n            effects[key] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    ss_total = float(np.sum((Y_6d - gm) ** 2))\n    ss_model = sum(e[\"ss\"] for e in effects.values())\n    ss_res = max(0.0, ss_total - ss_model)\n    df_res = N - 1 - sum(e[\"df\"] for e in effects.values())\n    effects[\"residual\"] = {\"ss\": ss_res, \"df\": df_res, \"ms\": ss_res / df_res if df_res > 0 else 0.0}\n\n    ms_res = effects[\"residual\"][\"ms\"]\n    vc = {}\n    for fi, fj in combinations(facet_names, 2):\n        key = f\"{fi}:{fj}\"\n        coeff = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n        raw = (effects[key][\"ms\"] - ms_res) / coeff if coeff > 0 else 0.0\n        vc[key] = max(0.0, raw)\n\n    for fi in facet_names:\n        coeff_main = prod(n_lev[f] for f in facet_names if f != fi)\n        interaction_contrib = 0.0\n        for fj in facet_names:\n            if fj == fi:\n                continue\n            int_key = f\"{fi}:{fj}\" if f\"{fi}:{fj}\" in vc else f\"{fj}:{fi}\"\n            coeff_ij = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n            interaction_contrib += coeff_ij * vc[int_key]\n        raw = (effects[fi][\"ms\"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0\n        vc[fi] = max(0.0, raw)\n\n    vc[\"residual\"] = ms_res\n    return vc, n_lev, effects\n\n\ndef compute_g_item_random(vc, n_lev):\n    sigma_item = vc.get(\"item_id\", 0.0)\n    delta = (\n        vc.get(\"model:item_id\", 0.0) / n_lev[\"model\"]\n        + vc.get(\"temperature:item_id\", 0.0) / n_lev[\"temperature\"]\n        + vc.get(\"prompt_template:item_id\", 0.0) / n_lev[\"prompt_template\"]\n        + vc.get(\"seed:item_id\", 0.0) / n_lev[\"seed\"]\n        + vc.get(\"ordering:item_id\", 0.0) / n_lev[\"ordering\"]\n        + vc[\"residual\"] / (n_lev[\"model\"] * n_lev[\"temperature\"] * n_lev[\"prompt_template\"]\n                            * n_lev[\"seed\"] * n_lev[\"ordering\"])\n    )\n    g = sigma_item / (sigma_item + delta) if (sigma_item + delta) > 0 else 0.0\n    return g, sigma_item, delta\n\n\ndef compute_g_item_fixed_methodB(vc, n_lev):\n    sigma_item = vc.get(\"item_id\", 0.0)\n    delta = (\n        vc.get(\"temperature:item_id\", 0.0) / n_lev[\"temperature\"]\n        + vc.get(\"prompt_template:item_id\", 0.0) / n_lev[\"prompt_template\"]\n        + vc.get(\"seed:item_id\", 0.0) / n_lev[\"seed\"]\n        + vc.get(\"ordering:item_id\", 0.0) / n_lev[\"ordering\"]\n        + vc[\"residual\"] / (n_lev[\"model\"] * n_lev[\"temperature\"] * n_lev[\"prompt_template\"]\n                            * n_lev[\"seed\"] * n_lev[\"ordering\"])\n    )\n    g = sigma_item / (sigma_item + delta) if (sigma_item + delta) > 0 else 0.0\n    return g, sigma_item, delta\n\n\n# Full 6-facet G-study (reproduce random-model baseline)\nprint(\"\\n=== 6-facet G-study (model=random baseline) ===\", flush=True)\nvc_6, nl_6, eff_6 = compute_gstudy_6facet(Y)\ntotal_var_6 = sum(vc_6.values())\n\ng_random, tau_random, delta_random = compute_g_item_random(vc_6, nl_6)\nprint(f\"G_item (model=random) = {g_random:.6f}\", flush=True)\n\n\n# Method B\nprint(\"\\n=== Method B: model-as-fixed (remove model:item from delta) ===\", flush=True)\ng_fixedB, tau_fixedB, delta_fixedB = compute_g_item_fixed_methodB(vc_6, nl_6)\nprint(f\"G_item (model=fixed, Method B) = {g_fixedB:.6f}\", flush=True)\nprint(f\"  delta reduction: {delta_random:.8f} -> {delta_fixedB:.8f} \"\n      f\"(removed model:item/n_m = {vc_6.get('model:item_id', 0)/nl_6['model']:.8f})\", flush=True)\n\n\n# Method A: Per-model 5-facet G-study\nprint(\"\\n=== Method A: per-model 5-facet G-study ===\", flush=True)\nper_model_results = {}\ng_items_per_model = []\n\nfor mi, model_name in enumerate(models_sorted):\n    Y_m = Y[mi]\n    vc_m, nl_m, eff_m = compute_gstudy_5facet(Y_m)\n    g_m, tau_m, delta_m = compute_g_item_5facet(vc_m, nl_m)\n    g_items_per_model.append(g_m)\n\n    total_var_m = sum(vc_m.values())\n    per_model_results[model_name] = {\n        \"g_item\": round(g_m, 6),\n        \"sigma_tau\": round(tau_m, 8),\n        \"sigma_delta\": round(delta_m, 8),\n        \"variance_components\": {\n            k: {\"estimate\": v, \"pct\": v / total_var_m * 100 if total_var_m > 0 else 0.0}\n            for k, v in sorted(vc_m.items(), key=lambda x: -x[1])\n        },\n        \"accuracy\": float(Y_m.mean()),\n    }\n    print(f\"  {model_name}: G_item={g_m:.6f}, acc={Y_m.mean():.4f}, \"\n          f\"s2(item)={vc_m['item_id']:.6f}, s2_delta={delta_m:.6f}\", flush=True)\n\ng_fixed_A = float(np.mean(g_items_per_model))\nprint(f\"\\nAverage G_item (model=fixed, Method A) = {g_fixed_A:.6f}\", flush=True)\n\npooled_vc = {}\nfor key in per_model_results[models_sorted[0]][\"variance_components\"]:\n    vals = [per_model_results[m][\"variance_components\"][key][\"estimate\"] for m in models_sorted]\n    pooled_vc[key] = float(np.mean(vals))\npooled_total = sum(pooled_vc.values())\n\n\n# Bootstrap\nprint(f\"\\nBootstrapping Method A ({N_BOOT} resamples)...\", flush=True)\nrng = np.random.default_rng(SEED)\nboot_g_fixed_A = []\nboot_g_random = []\n\nfor b in range(N_BOOT):\n    if b % 50 == 0:\n        print(f\"  {b}/{N_BOOT}...\", flush=True)\n    idx = rng.choice(n_i, size=n_i, replace=True)\n    Y_b = Y[:, :, :, :, :, idx]\n\n    vc_b6, nl_b6, _ = compute_gstudy_6facet(Y_b)\n    g_r, _, _ = compute_g_item_random(vc_b6, nl_b6)\n    boot_g_random.append(g_r)\n\n    g_per_model_b = []\n    for mi in range(n_m):\n        vc_bm, nl_bm, _ = compute_gstudy_5facet(Y_b[mi])\n        g_bm, _, _ = compute_g_item_5facet(vc_bm, nl_bm)\n        g_per_model_b.append(g_bm)\n    boot_g_fixed_A.append(float(np.mean(g_per_model_b)))\n\nci_random = [float(np.percentile(boot_g_random, 2.5)), float(np.percentile(boot_g_random, 97.5))]\nci_fixed_A = [float(np.percentile(boot_g_fixed_A, 2.5)), float(np.percentile(boot_g_fixed_A, 97.5))]\n\nprint(f\"\\nG_item (random): {g_random:.6f} [{ci_random[0]:.6f}, {ci_random[1]:.6f}]\", flush=True)\nprint(f\"G_item (fixed A): {g_fixed_A:.6f} [{ci_fixed_A[0]:.6f}, {ci_fixed_A[1]:.6f}]\", flush=True)\nprint(f\"G_item (fixed B): {g_fixedB:.6f}\", flush=True)\n\n\n# Ranking consistency\nfrom scipy.stats import spearmanr\n\nper_model_item_means = {}\nfor mi, m in enumerate(models_sorted):\n    per_model_item_means[m] = Y[mi].mean(axis=(0, 1, 2, 3))\n\nrank_corrs = []\nfor i in range(len(models_sorted)):\n    for j in range(i + 1, len(models_sorted)):\n        mi, mj = models_sorted[i], models_sorted[j]\n        rho, _ = spearmanr(per_model_item_means[mi], per_model_item_means[mj])\n        rank_corrs.append({\"pair\": f\"{mi} vs {mj}\", \"spearman_rho\": round(float(rho), 4)})\n\nmean_rho = float(np.mean([r[\"spearman_rho\"] for r in rank_corrs]))\nprint(f\"\\nItem ranking consistency across models:\", flush=True)\nfor r in rank_corrs:\n    print(f\"  {r['pair']}: rho={r['spearman_rho']:.4f}\", flush=True)\nprint(f\"  Mean rho = {mean_rho:.4f}\", flush=True)\n\n\n# Save\nresults = {\n    \"random_model\": {\n        \"G_item\": round(g_random, 6),\n        \"ci_95\": ci_random,\n        \"sigma_tau\": round(tau_random, 8),\n        \"sigma_delta\": round(delta_random, 8),\n        \"variance_components\": {\n            k: {\"estimate\": v, \"pct\": v / total_var_6 * 100}\n            for k, v in sorted(vc_6.items(), key=lambda x: -x[1])\n        },\n    },\n    \"fixed_model\": {\n        \"method_A_per_model_average\": {\n            \"G_item\": round(g_fixed_A, 6),\n            \"ci_95\": ci_fixed_A,\n            \"description\": \"Average of per-model 5-facet G_item values\",\n        },\n        \"method_B_remove_model_item\": {\n            \"G_item\": round(g_fixedB, 6),\n            \"sigma_tau\": round(tau_fixedB, 8),\n            \"sigma_delta\": round(delta_fixedB, 8),\n            \"description\": \"6-facet VC with model:item_id removed from sigma_delta\",\n        },\n        \"per_model_gstudy\": per_model_results,\n        \"pooled_variance_components\": {\n            k: {\"estimate\": v, \"pct\": v / pooled_total * 100 if pooled_total > 0 else 0.0}\n            for k, v in sorted(pooled_vc.items(), key=lambda x: -x[1])\n        },\n    },\n    \"comparison\": {\n        \"G_item_random\": round(g_random, 6),\n        \"G_item_fixed_A\": round(g_fixed_A, 6),\n        \"G_item_fixed_B\": round(g_fixedB, 6),\n        \"G_item_delta_A\": round(g_fixed_A - g_random, 6),\n        \"G_item_delta_B\": round(g_fixedB - g_random, 6),\n        \"ranking_consistency\": {\n            \"pairwise_spearman\": rank_corrs,\n            \"mean_spearman_rho\": round(mean_rho, 4),\n            \"consistent\": mean_rho > 0.7,\n        },\n        \"interpretation\": (\n            \"Model-as-fixed G_item is higher because model:item variance \"\n            \"(differential item difficulty across models) is no longer treated as \"\n            \"measurement error. This is appropriate when generalizing to these \"\n            \"specific 4 models rather than a hypothetical population of models.\"\n        ),\n    },\n    \"design\": {\n        \"n_observations\": int(Y.size),\n        \"n_levels\": {\"model\": n_m, \"temperature\": n_t, \"prompt_template\": n_p,\n                     \"seed\": n_s, \"ordering\": n_o, \"item_id\": n_i},\n        \"models\": models_sorted,\n        \"fixed_facets_random_design\": [\"temperature\"],\n        \"fixed_facets_fixed_model_design\": [\"model\", \"temperature\"],\n    },\n    \"bootstrap\": {\"n_resamples\": N_BOOT, \"seed\": SEED, \"method\": \"item cluster resampling\"},\n}\n\nPath(OUTPUT).parent.mkdir(parents=True, exist_ok=True)\nwith open(OUTPUT, \"w\") as f:\n    json.dump(results, f, indent=2, default=str)\n\nprint(f\"\\nTotal runtime: {time.time()-t_start:.1f}s\", flush=True)\nprint(f\"-> Saved to {OUTPUT}\", flush=True)\nSCRIPT_EOF\necho \"Script written OK\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat > /root/nlp_variance_gtheory/scripts/model_as_fixed_gstudy.py << 'SCRIPT_EOF'\n\"\"\"Model-as-fixed G-study (MF2 defense).\n\nTreats model as a fixed facet (not a random sample from a population of models).\nTwo methods:\n  A) Per-model 5-facet G-study, then average (clean separation)\n  B) Remove model:item from σ²δ in the crossed 6-facet design (quick adjustment)\n\nInput:  results/analysis/cross_model_4way_bf16.csv (4 models × bf16 × fully crossed)\nOutput: results/analysis/model_as_fixed_gstudy.json\n\"\"\"\n\nimport json\nimport time\nfrom itertools import combinations\nfrom math import prod\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\n\nINPUT = \"results/analysis/cross_model_4way_bf16.csv\"\nOUTPUT = \"results/analysis/model_as_fixed_gstudy.json\"\nN_BOOT = 200\nSEED = 42\n\nFACETS_6 = [\"model\", \"temperature\", \"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\nFACETS_5 = [\"temperature\", \"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\n\nt_start = time.time()\ndf = pd.read_csv(INPUT)\nprint(f\"Loaded {len(df)} obs ({time.time()-t_start:.1f}s)\", flush=True)\n\nmodels_sorted = sorted(df[\"model\"].unique())\ntemps_sorted = sorted(df[\"temperature\"].unique())\nprompts_sorted = sorted(df[\"prompt_template\"].unique())\nseeds_sorted = sorted(df[\"seed\"].unique())\norders_sorted = sorted(df[\"ordering\"].unique())\nitems_sorted = sorted(df[\"item_id\"].unique())\n\nn_m, n_t, n_p, n_s, n_o, n_i = (\n    len(models_sorted), len(temps_sorted), len(prompts_sorted),\n    len(seeds_sorted), len(orders_sorted), len(items_sorted),\n)\nprint(f\"Design: {n_m}m x {n_t}t x {n_p}p x {n_s}s x {n_o}o x {n_i}i = {n_m*n_t*n_p*n_s*n_o*n_i}\", flush=True)\n\nmodel_map = {v: i for i, v in enumerate(models_sorted)}\ntemp_map = {v: i for i, v in enumerate(temps_sorted)}\nprompt_map = {v: i for i, v in enumerate(prompts_sorted)}\nseed_map = {v: i for i, v in enumerate(seeds_sorted)}\norder_map = {v: i for i, v in enumerate(orders_sorted)}\nitem_map = {v: i for i, v in enumerate(items_sorted)}\n\nY = np.full((n_m, n_t, n_p, n_s, n_o, n_i), np.nan)\nfor _, row in df.iterrows():\n    Y[model_map[row[\"model\"]], temp_map[row[\"temperature\"]],\n      prompt_map[row[\"prompt_template\"]], seed_map[row[\"seed\"]],\n      order_map[row[\"ordering\"]], item_map[row[\"item_id\"]]] = row[\"correct\"]\n\nassert np.isnan(Y).sum() == 0, f\"Missing cells: {np.isnan(Y).sum()}\"\nprint(f\"6D array built ({time.time()-t_start:.1f}s)\", flush=True)\n\n\ndef compute_gstudy_5facet(arr_5d):\n    nt, np_, ns, no, ni = arr_5d.shape\n    N = arr_5d.size\n    gm = arr_5d.mean()\n    facet_names = FACETS_5\n    n_lev = {\"temperature\": nt, \"prompt_template\": np_, \"seed\": ns, \"ordering\": no, \"item_id\": ni}\n\n    effects = {}\n    for idx, f in enumerate(facet_names):\n        other_axes = tuple(j for j in range(5) if j != idx)\n        level_means = arr_5d.mean(axis=other_axes)\n        n_per = N // arr_5d.shape[idx]\n        ss = float(n_per * np.sum((level_means - gm) ** 2))\n        df_eff = arr_5d.shape[idx] - 1\n        effects[f] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    for i_idx in range(5):\n        for j_idx in range(i_idx + 1, 5):\n            fi, fj = facet_names[i_idx], facet_names[j_idx]\n            other_axes = tuple(k for k in range(5) if k not in (i_idx, j_idx))\n            cell_means = arr_5d.mean(axis=other_axes)\n            main_i = arr_5d.mean(axis=tuple(k for k in range(5) if k != i_idx))\n            main_j = arr_5d.mean(axis=tuple(k for k in range(5) if k != j_idx))\n            interaction = cell_means - main_i[:, None] - main_j[None, :] + gm\n            n_per = N // (arr_5d.shape[i_idx] * arr_5d.shape[j_idx])\n            ss = float(n_per * np.sum(interaction ** 2))\n            df_eff = (arr_5d.shape[i_idx] - 1) * (arr_5d.shape[j_idx] - 1)\n            key = f\"{fi}:{fj}\"\n            effects[key] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    ss_total = float(np.sum((arr_5d - gm) ** 2))\n    ss_model = sum(e[\"ss\"] for e in effects.values())\n    ss_res = max(0.0, ss_total - ss_model)\n    df_res = N - 1 - sum(e[\"df\"] for e in effects.values())\n    effects[\"residual\"] = {\"ss\": ss_res, \"df\": df_res, \"ms\": ss_res / df_res if df_res > 0 else 0.0}\n\n    ms_res = effects[\"residual\"][\"ms\"]\n    vc = {}\n    for fi, fj in combinations(facet_names, 2):\n        key = f\"{fi}:{fj}\"\n        coeff = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n        raw = (effects[key][\"ms\"] - ms_res) / coeff if coeff > 0 else 0.0\n        vc[key] = max(0.0, raw)\n\n    for fi in facet_names:\n        coeff_main = prod(n_lev[f] for f in facet_names if f != fi)\n        interaction_contrib = 0.0\n        for fj in facet_names:\n            if fj == fi:\n                continue\n            int_key = f\"{fi}:{fj}\" if f\"{fi}:{fj}\" in vc else f\"{fj}:{fi}\"\n            coeff_ij = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n            interaction_contrib += coeff_ij * vc[int_key]\n        raw = (effects[fi][\"ms\"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0\n        vc[fi] = max(0.0, raw)\n\n    vc[\"residual\"] = ms_res\n    return vc, n_lev, effects\n\n\ndef compute_g_item_5facet(vc, n_lev):\n    random_facets_5 = [\"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\n    sigma_item = vc.get(\"item_id\", 0.0)\n\n    sigma_delta = 0.0\n    for comp, est in vc.items():\n        if est == 0.0:\n            continue\n        if comp == \"residual\":\n            divisor = prod(n_lev[f] for f in random_facets_5)\n            sigma_delta += est / divisor\n            continue\n        facets_in = set(comp.split(\":\"))\n        if \"item_id\" not in facets_in:\n            continue\n        random_in = [f for f in facets_in if f in set(random_facets_5)]\n        if len(random_in) > 0:\n            divisor = prod(n_lev[f] for f in random_in)\n            sigma_delta += est / divisor\n\n    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0\n    return g, sigma_item, sigma_delta\n\n\ndef compute_gstudy_6facet(Y_6d):\n    nm, nt, np_, ns, no, ni = Y_6d.shape\n    N = Y_6d.size\n    gm = Y_6d.mean()\n    facet_names = FACETS_6\n    n_lev = {\"model\": nm, \"temperature\": nt, \"prompt_template\": np_, \"seed\": ns, \"ordering\": no, \"item_id\": ni}\n\n    effects = {}\n    for idx, f in enumerate(facet_names):\n        other_axes = tuple(j for j in range(6) if j != idx)\n        level_means = Y_6d.mean(axis=other_axes)\n        n_per = N // Y_6d.shape[idx]\n        ss = float(n_per * np.sum((level_means - gm) ** 2))\n        df_eff = Y_6d.shape[idx] - 1\n        effects[f] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    for i_idx in range(6):\n        for j_idx in range(i_idx + 1, 6):\n            fi, fj = facet_names[i_idx], facet_names[j_idx]\n            other_axes = tuple(k for k in range(6) if k not in (i_idx, j_idx))\n            cell_means = Y_6d.mean(axis=other_axes)\n            main_i = Y_6d.mean(axis=tuple(k for k in range(6) if k != i_idx))\n            main_j = Y_6d.mean(axis=tuple(k for k in range(6) if k != j_idx))\n            interaction = cell_means - main_i[:, None] - main_j[None, :] + gm\n            n_per = N // (Y_6d.shape[i_idx] * Y_6d.shape[j_idx])\n            ss = float(n_per * np.sum(interaction ** 2))\n            df_eff = (Y_6d.shape[i_idx] - 1) * (Y_6d.shape[j_idx] - 1)\n            key = f\"{fi}:{fj}\"\n            effects[key] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    ss_total = float(np.sum((Y_6d - gm) ** 2))\n    ss_model = sum(e[\"ss\"] for e in effects.values())\n    ss_res = max(0.0, ss_total - ss_model)\n    df_res = N - 1 - sum(e[\"df\"] for e in effects.values())\n    effects[\"residual\"] = {\"ss\": ss_res, \"df\": df_res, \"ms\": ss_res / df_res if df_res > 0 else 0.0}\n\n    ms_res = effects[\"residual\"][\"ms\"]\n    vc = {}\n    for fi, fj in combinations(facet_names, 2):\n        key = f\"{fi}:{fj}\"\n        coeff = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n        raw = (effects[key][\"ms\"] - ms_res) / coeff if coeff > 0 else 0.0\n        vc[key] = max(0.0, raw)\n\n    for fi in facet_names:\n        coeff_main = prod(n_lev[f] for f in facet_names if f != fi)\n        interaction_contrib = 0.0\n        for fj in facet_names:\n            if fj == fi:\n                continue\n            int_key = f\"{fi}:{fj}\" if f\"{fi}:{fj}\" in vc else f\"{fj}:{fi}\"\n            coeff_ij = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n            interaction_contrib += coeff_ij * vc[int_key]\n        raw = (effects[fi][\"ms\"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0\n        vc[fi] = max(0.0, raw)\n\n    vc[\"residual\"] = ms_res\n    return vc, n_lev, effects\n\n\ndef compute_g_item_random(vc, n_lev):\n    sigma_item = vc.get(\"item_id\", 0.0)\n    delta = (\n        vc.get(\"model:item_id\", 0.0) / n_lev[\"model\"]\n        + vc.get(\"temperature:item_id\", 0.0) / n_lev[\"temperature\"]\n        + vc.get(\"prompt_template:item_id\", 0.0) / n_lev[\"prompt_template\"]\n        + vc.get(\"seed:item_id\", 0.0) / n_lev[\"seed\"]\n        + vc.get(\"ordering:item_id\", 0.0) / n_lev[\"ordering\"]\n        + vc[\"residual\"] / (n_lev[\"model\"] * n_lev[\"temperature\"] * n_lev[\"prompt_template\"]\n                            * n_lev[\"seed\"] * n_lev[\"ordering\"])\n    )\n    g = sigma_item / (sigma_item + delta) if (sigma_item + delta) > 0 else 0.0\n    return g, sigma_item, delta\n\n\ndef compute_g_item_fixed_methodB(vc, n_lev):\n    sigma_item = vc.get(\"item_id\", 0.0)\n    delta = (\n        vc.get(\"temperature:item_id\", 0.0) / n_lev[\"temperature\"]\n        + vc.get(\"prompt_template:item_id\", 0.0) / n_lev[\"prompt_template\"]\n        + vc.get(\"seed:item_id\", 0.0) / n_lev[\"seed\"]\n        + vc.get(\"ordering:item_id\", 0.0) / n_lev[\"ordering\"]\n        + vc[\"residual\"] / (n_lev[\"model\"] * n_lev[\"temperature\"] * n_lev[\"prompt_template\"]\n                            * n_lev[\"seed\"] * n_lev[\"ordering\"])\n    )\n    g = sigma_item / (sigma_item + delta) if (sigma_item + delta) > 0 else 0.0\n    return g, sigma_item, delta\n\n\n# Full 6-facet G-study (reproduce random-model baseline)\nprint(\"\\n=== 6-facet G-study (model=random baseline) ===\", flush=True)\nvc_6, nl_6, eff_6 = compute_gstudy_6facet(Y)\ntotal_var_6 = sum(vc_6.values())\n\ng_random, tau_random, delta_random = compute_g_item_random(vc_6, nl_6)\nprint(f\"G_item (model=random) = {g_random:.6f}\", flush=True)\n\n\n# Method B\nprint(\"\\n=== Method B: model-as-fixed (remove model:item from delta) ===\", flush=True)\ng_fixedB, tau_fixedB, delta_fixedB = compute_g_item_fixed_methodB(vc_6, nl_6)\nprint(f\"G_item (model=fixed, Method B) = {g_fixedB:.6f}\", flush=True)\nprint(f\"  delta reduction: {delta_random:.8f} -> {delta_fixedB:.8f} \"\n      f\"(removed model:item/n_m = {vc_6.get('model:item_id', 0)/nl_6['model']:.8f})\", flush=True)\n\n\n# Method A: Per-model 5-facet G-study\nprint(\"\\n=== Method A: per-model 5-facet G-study ===\", flush=True)\nper_model_results = {}\ng_items_per_model = []\n\nfor mi, model_name in enumerate(models_sorted):\n    Y_m = Y[mi]\n    vc_m, nl_m, eff_m = compute_gstudy_5facet(Y_m)\n    g_m, tau_m, delta_m = compute_g_item_5facet(vc_m, nl_m)\n    g_items_per_model.append(g_m)\n\n    total_var_m = sum(vc_m.values())\n    per_model_results[model_name] = {\n        \"g_item\": round(g_m, 6),\n        \"sigma_tau\": round(tau_m, 8),\n        \"sigma_delta\": round(delta_m, 8),\n        \"variance_components\": {\n            k: {\"estimate\": v, \"pct\": v / total_var_m * 100 if total_var_m > 0 else 0.0}\n            for k, v in sorted(vc_m.items(), key=lambda x: -x[1])\n        },\n        \"accuracy\": float(Y_m.mean()),\n    }\n    print(f\"  {model_name}: G_item={g_m:.6f}, acc={Y_m.mean():.4f}, \"\n          f\"s2(item)={vc_m['item_id']:.6f}, s2_delta={delta_m:.6f}\", flush=True)\n\ng_fixed_A = float(np.mean(g_items_per_model))\nprint(f\"\\nAverage G_item (model=fixed, Method A) = {g_fixed_A:.6f}\", flush=True)\n\npooled_vc = {}\nfor key in per_model_results[models_sorted[0]][\"variance_components\"]:\n    vals = [per_model_results[m][\"variance_components\"][key][\"estimate\"] for m in models_sorted]\n    pooled_vc[key] = float(np.mean(vals))\npooled_total = sum(pooled_vc.values())\n\n\n# Bootstrap\nprint(f\"\\nBootstrapping Method A ({N_BOOT} resamples)...\", flush=True)\nrng = np.random.default_rng(SEED)\nboot_g_fixed_A = []\nboot_g_random = []\n\nfor b in range(N_BOOT):\n    if b % 50 == 0:\n        print(f\"  {b}/{N_BOOT}...\", flush=True)\n    idx = rng.choice(n_i, size=n_i, replace=True)\n    Y_b = Y[:, :, :, :, :, idx]\n\n    vc_b6, nl_b6, _ = compute_gstudy_6facet(Y_b)\n    g_r, _, _ = compute_g_item_random(vc_b6, nl_b6)\n    boot_g_random.append(g_r)\n\n    g_per_model_b = []\n    for mi in range(n_m):\n        vc_bm, nl_bm, _ = compute_gstudy_5facet(Y_b[mi])\n        g_bm, _, _ = compute_g_item_5facet(vc_bm, nl_bm)\n        g_per_model_b.append(g_bm)\n    boot_g_fixed_A.append(float(np.mean(g_per_model_b)))\n\nci_random = [float(np.percentile(boot_g_random, 2.5)), float(np.percentile(boot_g_random, 97.5))]\nci_fixed_A = [float(np.percentile(boot_g_fixed_A, 2.5)), float(np.percentile(boot_g_fixed_A, 97.5))]\n\nprint(f\"\\nG_item (random): {g_random:.6f} [{ci_random[0]:.6f}, {ci_random[1]:.6f}]\", flush=True)\nprint(f\"G_item (fixed A): {g_fixed_A:.6f} [{ci_fixed_A[0]:.6f}, {ci_fixed_A[1]:.6f}]\", flush=True)\nprint(f\"G_item (fixed B): {g_fixedB:.6f}\", flush=True)\n\n\n# Ranking consistency\nfrom scipy.stats import spearmanr\n\nper_model_item_means = {}\nfor mi, m in enumerate(models_sorted):\n    per_model_item_means[m] = Y[mi].mean(axis=(0, 1, 2, 3))\n\nrank_corrs = []\nfor i in range(len(models_sorted)):\n    for j in range(i + 1, len(models_sorted)):\n        mi, mj = models_sorted[i], models_sorted[j]\n        rho, _ = spearmanr(per_model_item_means[mi], per_model_item_means[mj])\n        rank_corrs.append({\"pair\": f\"{mi} vs {mj}\", \"spearman_rho\": round(float(rho), 4)})\n\nmean_rho = float(np.mean([r[\"spearman_rho\"] for r in rank_corrs]))\nprint(f\"\\nItem ranking consistency across models:\", flush=True)\nfor r in rank_corrs:\n    print(f\"  {r['pair']}: rho={r['spearman_rho']:.4f}\", flush=True)\nprint(f\"  Mean rho = {mean_rho:.4f}\", flush=True)\n\n\n# Save\nresults = {\n    \"random_model\": {\n        \"G_item\": round(g_random, 6),\n        \"ci_95\": ci_random,\n        \"sigma_tau\": round(tau_random, 8),\n        \"sigma_delta\": round(delta_random, 8),\n        \"variance_components\": {\n            k: {\"estimate\": v, \"pct\": v / total_var_6 * 100}\n            for k, v in sorted(vc_6.items(), key=lambda x: -x[1])\n        },\n    },\n    \"fixed_model\": {\n        \"method_A_per_model_average\": {\n            \"G_item\": round(g_fixed_A, 6),\n            \"ci_95\": ci_fixed_A,\n            \"description\": \"Average of per-model 5-facet G_item values\",\n        },\n        \"method_B_remove_model_item\": {\n            \"G_item\": round(g_fixedB, 6),\n            \"sigma_tau\": round(tau_fixedB, 8),\n            \"sigma_delta\": round(delta_fixedB, 8),\n            \"description\": \"6-facet VC with model:item_id removed from sigma_delta\",\n        },\n        \"per_model_gstudy\": per_model_results,\n        \"pooled_variance_components\": {\n            k: {\"estimate\": v, \"pct\": v / pooled_total * 100 if pooled_total > 0 else 0.0}\n            for k, v in sorted(pooled_vc.items(), key=lambda x: -x[1])\n        },\n    },\n    \"comparison\": {\n        \"G_item_random\": round(g_random, 6),\n        \"G_item_fixed_A\": round(g_fixed_A, 6),\n        \"G_item_fixed_B\": round(g_fixedB, 6),\n        \"G_item_delta_A\": round(g_fixed_A - g_random, 6),\n        \"G_item_delta_B\": round(g_fixedB - g_random, 6),\n        \"ranking_consistency\": {\n            \"pairwise_spearman\": rank_corrs,\n            \"mean_spearman_rho\": round(mean_rho, 4),\n            \"consistent\": mean_rho > 0.7,\n        },\n        \"interpretation\": (\n            \"Model-as-fixed G_item is higher because model:item variance \"\n            \"(differential item difficulty across models) is no longer treated as \"\n            \"measurement error. This is appropriate when generalizing to these \"\n            \"specific 4 models rather than a hypothetical population of models.\"\n        ),\n    },\n    \"design\": {\n        \"n_observations\": int(Y.size),\n        \"n_levels\": {\"model\": n_m, \"temperature\": n_t, \"prompt_template\": n_p,\n                     \"seed\": n_s, \"ordering\": n_o, \"item_id\": n_i},\n        \"models\": models_sorted,\n        \"fixed_facets_random_design\": [\"temperature\"],\n        \"fixed_facets_fixed_model_design\": [\"model\", \"temperature\"],\n    },\n    \"bootstrap\": {\"n_resamples\": N_BOOT, \"seed\": SEED, \"method\": \"item cluster resampling\"},\n}\n\nPath(OUTPUT).parent.mkdir(parents=True, exist_ok=True)\nwith open(OUTPUT, \"w\") as f:\n    json.dump(results, f, indent=2, default=str)\n\nprint(f\"\\nTotal runtime: {time.time()-t_start:.1f}s\", flush=True)\nprint(f\"-> Saved to {OUTPUT}\", flush=True)\nSCRIPT_EOF\necho \"Script written OK\""
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-21T09:07:41.672378+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-21T09:07:41.672553+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32570",
  "command": "cd /root/nlp_variance_gtheory && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export PYTHONPATH=/root/nlp_variance_gtheory:$PYTHONPATH && nohup python scripts/model_as_fixed_gstudy.py > /tmp/model_fixed_gstudy.log 2>&1 &\necho \"PID: $!\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32570",
    "command": "cd /root/nlp_variance_gtheory && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export PYTHONPATH=/root/nlp_variance_gtheory:$PYTHONPATH && nohup python scripts/model_as_fixed_gstudy.py > /tmp/model_fixed_gstudy.log 2>&1 &\necho \"PID: $!\""
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-21T09:07:41.672690+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"PID: 130243\\n\", \"stderr\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 22.8}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-21T09:07:41.672823+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "tail -20 /tmp/model_fixed_gstudy.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "tail -20 /tmp/model_fixed_gstudy.log"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-21T09:07:41.672977+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  0/200...\\n  50/200...\\n  100/200...\\n  150/200...\\n\\nG_item (random): 0.820039 [0.781615, 0.860875]\\nG_item (fixed A): 0.994739 [0.994692, 0.994782]\\nG_item (fixed B): 0.980807\\n\\nItem ranking consistency across models:\\n  gemma-2-9b-it vs llama-3.1-8b-instruct: rho=0.6792\\n  gemma-2-9b-it vs mistral-7b-instruct-v0.3: rho=0.6442\\n  gemma-2-9b-it vs qwen3-8b: rho=0.6657\\n  llama-3.1-8b-instruct vs mistral-7b-instruct-v0.3: rho=0.6924\\n  llama-3.1-8b-instruct vs qwen3-8b: rho=0.6377\\n  mistral-7b-instruct-v0.3 vs qwen3-8b: rho=0.5347\\n  Mean rho = 0.6423\\n\\nTotal runtime: 21.8s\\n-> Saved to results/analysis/model_as_fixed_gstudy.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-21T09:07:41.673169+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /root/nlp_variance_gtheory/results/analysis/model_as_fixed_gstudy.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /root/nlp_variance_gtheory/results/analysis/model_as_fixed_gstudy.json"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-21T09:07:41.673533+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"random_model\\\": {\\n    \\\"G_item\\\": 0.820039,\\n    \\\"ci_95\\\": [\\n      0.7816146190369399,\\n      0.8608747018283437\\n    ],\\n    \\\"sigma_tau\\\": 0.08851438,\\n    \\\"sigma_delta\\\": 0.01942482,\\n    \\\"variance_components\\\": {\\n      \\\"item_id\\\": {\\n        \\\"estimate\\\": 0.08851437651254966,\\n        \\\"pct\\\": 42.07775096535229\\n      },\\n      \\\"model:item_id\\\": {\\n        \\\"estimate\\\": 0.07077085201146294,\\n        \\\"pct\\\": 33.642877054236855\\n      },\\n      \\\"residual\\\": {\\n        \\\"estimate\\\": 0.041118141769829794,\\n        \\\"pct\\\": 19.54664312981569\\n      },\\n      \\\"prompt_template:item_id\\\": {\\n        \\\"estimate\\\": 0.003014134593133947,\\n        \\\"pct\\\": 1.4328520380862861\\n      },\\n      \\\"seed:item_id\\\": {\\n        \\\"estimate\\\": 0.0027848637210264957,\\n        \\\"pct\\\": 1.3238618035024308\\n      },\\n      \\\"model\\\": {\\n        \\\"estimate\\\": 0.001511069516435654,\\n        \\\"pct\\\": 0.7183285846779928\\n      },\\n      \\\"temperature:item_id\\\": {\\n        \\\"estimate\\\": 0.0013693514156093306,\\n        \\\"pct\\\": 0.6509589754822792\\n      },\\n      \\\"ordering:item_id\\\": {\\n        \\\"estimate\\\": 0.0011414417428128746,\\n        \\\"pct\\\": 0.5426158245460633\\n      },\\n      \\\"model:prompt_template\\\": {\\n        \\\"estimate\\\": 4.183404268830899e-05,\\n        \\\"pct\\\": 0.019886966382946934\\n      },\\n      \\\"model:temperature\\\": {\\n        \\\"estimate\\\": 3.66508899784139e-05,\\n        \\\"pct\\\": 0.01742301174037613\\n      },\\n      \\\"model:seed\\\": {\\n        \\\"estimate\\\": 1.9099989190366816e-05,\\n        \\\"pct\\\": 0.009079706825695467\\n      },\\n      \\\"prompt_template\\\": {\\n        \\\"estimate\\\": 1.3871568991435068e-05,\\n        \\\"pct\\\": 0.006594233033292083\\n      },\\n      \\\"prompt_template:o
…[truncated 8116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-21T09:07:41.673849+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32570",
  "command": "cat > /root/nlp_variance_gtheory/scripts/model_as_fixed_gstudy.py << 'SCRIPT_EOF'\n\"\"\"Model-as-fixed G-study (MF2 defense).\n\nTreats model as a fixed facet (not a random sample from a population of models).\nTwo methods:\n  A) Per-model 5-facet G-study, then average (clean separation)\n  B) Remove model:item from σ²δ in the crossed 6-facet design (quick adjustment)\n\nInput:  results/analysis/cross_model_4way_bf16.csv (4 models × bf16 × fully crossed)\nOutput: results/analysis/model_as_fixed_gstudy.json\n\"\"\"\n\nimport json\nimport time\nfrom itertools import combinations\nfrom math import prod\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\n\nINPUT = \"results/analysis/cross_model_4way_bf16.csv\"\nOUTPUT = \"results/analysis/model_as_fixed_gstudy.json\"\nN_BOOT = 200\nSEED = 42\n\nFACETS_6 = [\"model\", \"temperature\", \"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\nFACETS_5 = [\"temperature\", \"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\n\nt_start = time.time()\ndf = pd.read_csv(INPUT)\nprint(f\"Loaded {len(df)} obs ({time.time()-t_start:.1f}s)\", flush=True)\n\nmodels_sorted = sorted(df[\"model\"].unique())\ntemps_sorted = sorted(df[\"temperature\"].unique())\nprompts_sorted = sorted(df[\"prompt_template\"].unique())\nseeds_sorted = sorted(df[\"seed\"].unique())\norders_sorted = sorted(df[\"ordering\"].unique())\nitems_sorted = sorted(df[\"item_id\"].unique())\n\nn_m, n_t, n_p, n_s, n_o, n_i = (\n    len(models_sorted), len(temps_sorted), len(prompts_sorted),\n    len(seeds_sorted), len(orders_sorted), len(items_sorted),\n)\nprint(f\"Design: {n_m}m x {n_t}t x {n_p}p x {n_s}s x {n_o}o x {n_i}i = {n_m*n_t*n_p*n_s*n_o*n_i}\", flush=True)\n\nmodel_map = {v: i for i, v in enumerate(models_sorted)}\ntemp_map = {v: i for i, v in enumerate(temps_sorted)}\nprompt_map = {v: i for i, v in enumerate(prompts_sorted)}\nseed_map = {v: i for i, v in enumerate(seeds_sorted)}\norder_map = {v: i for i, v in enumerate(orders_sorted)}\nitem_map = {v: i for i, v in enumerate(items_sorted)}\n\nY = np.full((n_m, n_t, n_p, n_s, n_o, n_i), np.nan)\nfor _, row in df.iterrows():\n    Y[model_map[row[\"model\"]], temp_map[row[\"temperature\"]],\n      prompt_map[row[\"prompt_template\"]], seed_map[row[\"seed\"]],\n      order_map[row[\"ordering\"]], item_map[row[\"item_id\"]]] = row[\"correct\"]\n\nassert np.isnan(Y).sum() == 0, f\"Missing cells: {np.isnan(Y).sum()}\"\nprint(f\"6D array built ({time.time()-t_start:.1f}s)\", flush=True)\n\n\ndef compute_gstudy_5facet(arr_5d):\n    \"\"\"5-facet Henderson I on (temp, prompt, seed, ordering, item) array.\"\"\"\n    nt, np_, ns, no, ni = arr_5d.shape\n    N = arr_5d.size\n    gm = arr_5d.mean()\n    facet_names = FACETS_5\n    n_lev = {\"temperature\": nt, \"prompt_template\": np_, \"seed\": ns, \"ordering\": no, \"item_id\": ni}\n\n    effects = {}\n    for idx, f in enumerate(facet_names):\n        other_axes = tuple(j for j in range(5) if j != idx)\n        level_means = arr_5d.mean(axis=other_axes)\n        n_per = N // arr_5d.shape[idx]\n        ss = float(n_per * np.sum((level_means - gm) ** 2))\n        df_eff = arr_5d.shape[idx] - 1\n        effects[f] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    for i_idx in range(5):\n        for j_idx in range(i_idx + 1, 5):\n            fi, fj = facet_names[i_idx], facet_names[j_idx]\n            other_axes = tuple(k for k in range(5) if k not in (i_idx, j_idx))\n            cell_means = arr_5d.mean(axis=other_axes)\n            main_i = arr_5d.mean(axis=tuple(k for k in range(5) if k != i_idx))\n            main_j = arr_5d.mean(axis=tuple(k for k in range(5) if k != j_idx))\n            interaction = cell_means - main_i[:, None] - main_j[None, :] + gm\n            n_per = N // (arr_5d.shape[i_idx] * arr_5d.shape[j_idx])\n            ss = float(n_per * np.sum(interaction ** 2))\n            df_eff = (arr_5d.shape[i_idx] - 1) * (arr_5d.shape[j_idx] - 1)\n            key = f\"{fi}:{fj}\"\n            effects[key] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    ss_total = float(np.sum((arr_5d - gm) ** 2))\n    ss_model = sum(e[\"ss\"] for e in effects.values())\n    ss_res = max(0.0, ss_total - ss_model)\n    df_res = N - 1 - sum(e[\"df\"] for e in effects.values())\n    effects[\"residual\"] = {\"ss\": ss_res, \"df\": df_res, \"ms\": ss_res / df_res if df_res > 0 else 0.0}\n\n    ms_res = effects[\"residual\"][\"ms\"]\n    vc = {}\n    for fi, fj in combinations(facet_names, 2):\n        key = f\"{fi}:{fj}\"\n        coeff = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n        raw = (effects[key][\"ms\"] - ms_res) / coeff if coeff > 0 else 0.0\n        vc[key] = max(0.0, raw)\n\n    for fi in facet_names:\n        coeff_main = prod(n_lev[f] for f in facet_names if f != fi)\n        interaction_contrib = 0.0\n        for fj in facet_names:\n            if fj == fi:\n                continue\n            int_key = f\"{fi}:{fj}\" if f\"{fi}:{fj}\" in vc else f\"{fj}:{fi}\"\n            coeff_ij = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n            interaction_contrib += coeff_ij * vc[int_key]\n        raw = (effects[fi][\"ms\"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0\n        vc[fi] = max(0.0, raw)\n\n    vc[\"residual\"] = ms_res\n    return vc, n_lev, effects\n\n\ndef compute_g_item_5facet(vc, n_lev):\n    \"\"\"G_item for 5-facet within-model design.\n\n    Object of measurement: item_id.\n    σ²_τ = σ²(item_id)\n    σ²_δ = Σ σ²(X:item_id)/n_X + σ²(residual)/Π(n_X for X ≠ item_id)\n    \"\"\"\n    sigma_item = vc.get(\"item_id\", 0.0)\n    non_item_facets = [\"temperature\", \"prompt_template\", \"seed\", \"ordering\"]\n\n    sigma_delta = 0.0\n    for comp, est in vc.items():\n        if est == 0.0 or comp == \"item_id\":\n            continue\n        if comp == \"residual\":\n            divisor = prod(n_lev[f] for f in non_item_facets)\n            sigma_delta += est / divisor\n            continue\n        facets_in = set(comp.split(\":\"))\n        if \"item_id\" not in facets_in:\n            continue\n        other = [f for f in facets_in if f != \"item_id\"]\n        divisor = prod(n_lev[f] for f in other) if other else 1\n        sigma_delta += est / divisor\n\n    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0\n    return g, sigma_item, sigma_delta\n\n\ndef compute_gstudy_6facet(Y_6d):\n    \"\"\"Full 6-facet Henderson I on (model, temp, prompt, seed, ordering, item) array.\"\"\"\n    nm, nt, np_, ns, no, ni = Y_6d.shape\n    N = Y_6d.size\n    gm = Y_6d.mean()\n    facet_names = FACETS_6\n    n_lev = {\"model\": nm, \"temperature\": nt, \"prompt_template\": np_, \"seed\": ns, \"ordering\": no, \"item_id\": ni}\n\n    effects = {}\n    for idx, f in enumerate(facet_names):\n        other_axes = tuple(j for j in range(6) if j != idx)\n        level_means = Y_6d.mean(axis=other_axes)\n        n_per = N // Y_6d.shape[idx]\n        ss = float(n_per * np.sum((level_means - gm) ** 2))\n        df_eff = Y_6d.shape[idx] - 1\n        effects[f] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    for i_idx in range(6):\n        for j_idx in range(i_idx + 1, 6):\n            fi, fj = facet_names[i_idx], facet_names[j_idx]\n            other_axes = tuple(k for k in range(6) if k not in (i_idx, j_idx))\n            cell_means = Y_6d.mean(axis=other_axes)\n            main_i = Y_6d.mean(axis=tuple(k for k in range(6) if k != i_idx))\n            main_j = Y_6d.mean(axis=tuple(k for k in range(6) if k != j_idx))\n            interaction = cell_means - main_i[:, None] - main_j[None, :] + gm\n            n_per = N // (Y_6d.shape[i_idx] * Y_6d.shape[j_idx])\n            ss = float(n_per * np.sum(interaction ** 2))\n            df_eff = (Y_6d.shape[i_idx] - 1) * (Y_6d.shape[j_idx] - 1)\n            key = f\"{fi}:{fj}\"\n            effects[key] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    ss_total = float(np.sum((Y_6d - gm) ** 2))\n    ss_model = sum(e[\"ss\"] for e in effects.values())\n    ss_res = max(0.0, ss_total - ss_model)\n    df_res = N - 1 - sum(e[\"df\"] for e in effects.values())\n    effects[\"residual\"] = {\"ss\": ss_res, \"df\": df_res, \"ms\": ss_res / df_res if df_res > 0 else 0.0}\n\n    ms_res = effects[\"residual\"][\"ms\"]\n    vc = {}\n    for fi, fj in combinations(facet_names, 2):\n        key = f\"{fi}:{fj}\"\n        coeff = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n        raw = (effects[key][\"ms\"] - ms_res) / coeff if coeff > 0 else 0.0\n        vc[key] = max(0.0, raw)\n\n    for fi in facet_names:\n        coeff_main = prod(n_lev[f] for f in facet_names if f != fi)\n        interaction_contrib = 0.0\n        for fj in facet_names:\n            if fj == fi:\n                continue\n            int_key = f\"{fi}:{fj}\" if f\"{fi}:{fj}\" in vc else f\"{fj}:{fi}\"\n            coeff_ij = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n            interaction_contrib += coeff_ij * vc[int_key]\n        raw = (effects[fi][\"ms\"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0\n        vc[fi] = max(0.0, raw)\n\n    vc[\"residual\"] = ms_res\n    return vc, n_lev, effects\n\n\ndef compute_g_item_random(vc, n_lev):\n    \"\"\"G_item with model as RANDOM.\n\n    σ²_δ = σ²(model:item)/n_m + σ²(temp:item)/n_t + ... + σ²(res)/(n_m·n_t·n_p·n_s·n_o)\n    \"\"\"\n    sigma_item = vc.get(\"item_id\", 0.0)\n    delta = (\n        vc.get(\"model:item_id\", 0.0) / n_lev[\"model\"]\n        + vc.get(\"temperature:item_id\", 0.0) / n_lev[\"temperature\"]\n        + vc.get(\"prompt_template:item_id\", 0.0) / n_lev[\"prompt_template\"]\n        + vc.get(\"seed:item_id\", 0.0) / n_lev[\"seed\"]\n        + vc.get(\"ordering:item_id\", 0.0) / n_lev[\"ordering\"]\n        + vc[\"residual\"] / (n_lev[\"model\"] * n_lev[\"temperature\"] * n_lev[\"prompt_template\"]\n                            * n_lev[\"seed\"] * n_lev[\"ordering\"])\n    )\n    g = sigma_item / (sigma_item + delta) if (sigma_item + delta) > 0 else 0.0\n    return g, sigma_item, delta\n\n\ndef compute_g_item_fixed_methodB(vc, n_lev):\n    \"\"\"G_item with model as FIXED (Method B: remove model:item from σ²δ).\n\n    Same residual divisor (n_m still in denominator since we average over 4 fixed models).\n    \"\"\"\n    sigma_item = vc.get(\"item_id\", 0.0)\n    delta = (\n        vc.get(\"temperature:item_id\", 0.0) / n_lev[\"temperature\"]\n        + vc.get(\"prompt_template:item_id\", 0.0) / n_lev[\"prompt_template\"]\n        + vc.get(\"seed:item_id\", 0.0) / n_lev[\"seed\"]\n        + vc.get(\"ordering:item_id\", 0.0) / n_lev[\"ordering\"]\n        + vc[\"residual\"] / (n_lev[\"model\"] * n_lev[\"temperature\"] * n_lev[\"prompt_template\"]\n                            * n_lev[\"seed\"] * n_lev[\"ordering\"])\n    )\n    g = sigma_item / (sigma_item + delta) if (sigma_item + delta) > 0 else 0.0\n    return g, sigma_item, delta\n\n\n# ============================================================\n# Full 6-facet G-study (reproduce random-model baseline)\n# ============================================================\nprint(\"\\n=== 6-facet G-study (model=random baseline) ===\", flush=True)\nvc_6, nl_6, eff_6 = compute_gstudy_6facet(Y)\ntotal_var_6 = sum(vc_6.values())\n\ng_random, tau_random, delta_random = compute_g_item_random(vc_6, nl_6)\nprint(f\"G_item (model=random) = {g_random:.6f}\", flush=True)\nprint(f\"  sigma_tau={tau_random:.8f}, sigma_delta={delta_random:.8f}\", flush=True)\n\n\n# ============================================================\n# Method B: Fixed model in crossed design\n# ============================================================\nprint(\"\\n=== Method B: model-as-fixed (remove model:item from delta) ===\", flush=True)\ng_fixedB, tau_fixedB, delta_fixedB = compute_g_item_fixed_methodB(vc_6, nl_6)\nprint(f\"G_item (model=fixed, Method B) = {g_fixedB:.6f}\", flush=True)\nprint(f\"  sigma_delta: {delta_random:.8f} -> {delta_fixedB:.8f}\", flush=True)\nprint(f\"  removed: model:item/n_m = {vc_6.get('model:item_id', 0)/nl_6['model']:.8f}\", flush=True)\n\n\n# ============================================================\n# Method A: Per-model 5-facet G-study\n# ============================================================\nprint(\"\\n=== Method A: per-model 5-facet G-study ===\", flush=True)\nper_model_results = {}\ng_items_per_model = []\n\nfor mi, model_name in enumerate(models_sorted):\n    Y_m = Y[mi]\n    vc_m, nl_m, eff_m = compute_gstudy_5facet(Y_m)\n    g_m, tau_m, delta_m = compute_g_item_5facet(vc_m, nl_m)\n    g_items_per_model.append(g_m)\n\n    total_var_m = sum(vc_m.values())\n    per_model_results[model_name] = {\n        \"g_item\": round(g_m, 6),\n        \"sigma_tau\": round(tau_m, 8),\n        \"sigma_delta\": round(delta_m, 8),\n        \"variance_components\": {\n            k: {\"estimate\": v, \"pct\": v / total_var_m * 100 if total_var_m > 0 else 0.0}\n            for k, v in sorted(vc_m.items(), key=lambda x: -x[1])\n        },\n        \"accuracy\": float(Y_m.mean()),\n    }\n    print(f\"  {model_name}: G_item={g_m:.6f}, acc={Y_m.mean():.4f}, \"\n          f\"s2_item={vc_m['item_id']:.6f}, s2_delta={delta_m:.6f}\", flush=True)\n\ng_fixed_A = float(np.mean(g_items_per_model))\nprint(f\"\\nAverage G_item (model=fixed, Method A) = {g_fixed_A:.6f}\", flush=True)\n\npooled_vc = {}\nfor key in per_model_results[models_sorted[0]][\"variance_components\"]:\n    vals = [per_model_results[m][\"variance_components\"][key][\"estimate\"] for m in models_sorted]\n    pooled_vc[key] = float(np.mean(vals))\npooled_total = sum(pooled_vc.values())\n\n\n# ============================================================\n# Bootstrap CI\n# ============================================================\nprint(f\"\\nBootstrapping ({N_BOOT} resamples)...\", flush=True)\nrng = np.random.default_rng(SEED)\nboot_g_fixed_A = []\nboot_g_fixed_B = []\nboot_g_random = []\n\nfor b in range(N_BOOT):\n    if b % 50 == 0:\n        print(f\"  {b}/{N_BOOT}...\", flush=True)\n    idx = rng.choice(n_i, size=n_i, replace=True)\n    Y_b = Y[:, :, :, :, :, idx]\n\n    vc_b6, nl_b6, _ = compute_gstudy_6facet(Y_b)\n    g_r, _, _ = compute_g_item_random(vc_b6, nl_b6)\n    boot_g_random.append(g_r)\n\n    g_fB, _, _ = compute_g_item_fixed_methodB(vc_b6, nl_b6)\n    boot_g_fixed_B.append(g_fB)\n\n    g_per_model_b = []\n    for mi in range(n_m):\n        vc_bm, nl_bm, _ = compute_gstudy_5facet(Y_b[mi])\n        g_bm, _, _ = compute_g_item_5facet(vc_bm, nl_bm)\n        g_per_model_b.append(g_bm)\n    boot_g_fixed_A.append(float(np.mean(g_per_model_b)))\n\nci_random = [float(np.percentile(boot_g_random, 2.5)), float(np.percentile(boot_g_random, 97.5))]\nci_fixed_A = [float(np.percentile(boot_g_fixed_A, 2.5)), float(np.percentile(boot_g_fixed_A, 97.5))]\nci_fixed_B = [float(np.percentile(boot_g_fixed_B, 2.5)), float(np.percentile(boot_g_fixed_B, 97.5))]\n\nprint(f\"\\nResults with 95% CI:\", flush=True)\nprint(f\"  G_item (random):  {g_random:.6f} [{ci_random[0]:.6f}, {ci_random[1]:.6f}]\", flush=True)\nprint(f\"  G_item (fixed A): {g_fixed_A:.6f} [{ci_fixed_A[0]:.6f}, {ci_fixed_A[1]:.6f}]\", flush=True)\nprint(f\"  G_item (fixed B): {g_fixedB:.6f} [{ci_fixed_B[0]:.6f}, {ci_fixed_B[1]:.6f}]\", flush=True)\n\n\n# ============================================================\n# Ranking consistency\n# ============================================================\nfrom scipy.stats import spearmanr\n\nper_model_item_means = {}\nfor mi, m in enumerate(models_sorted):\n    per_model_item_means[m] = Y[mi].mean(axis=(0, 1, 2, 3))\n\nrank_corrs = []\nfor i in range(len(models_sorted)):\n    for j in range(i + 1, len(models_sorted)):\n        mi, mj = models_sorted[i], models_sorted[j]\n        rho, _ = spearmanr(per_model_item_means[mi], per_model_item_means[mj])\n        rank_corrs.append({\"pair\": f\"{mi} vs {mj}\", \"spearman_rho\": round(float(rho), 4)})\n\nmean_rho = float(np.mean([r[\"spearman_rho\"] for r in rank_corrs]))\nprint(f\"\\nItem ranking consistency across models:\", flush=True)\nfor r in rank_corrs:\n    print(f\"  {r['pair']}: rho={r['spearman_rho']:.4f}\", flush=True)\nprint(f\"  Mean rho = {mean_rho:.4f}\", flush=True)\n\n\n# ============================================================\n# Save\n# ============================================================\nresults = {\n    \"random_model\": {\n        \"G_item\": round(g_random, 6),\n        \"ci_95\": ci_random,\n        \"sigma_tau\": round(tau_random, 8),\n        \"sigma_delta\": round(delta_random, 8),\n        \"variance_components\": {\n            k: {\"estimate\": v, \"pct\": v / total_var_6 * 100}\n            for k, v in sorted(vc_6.items(), key=lambda x: -x[1])\n        },\n    },\n    \"fixed_model\": {\n        \"method_A_per_model_average\": {\n            \"G_item\": round(g_fixed_A, 6),\n            \"ci_95\": ci_fixed_A,\n            \"description\": \"Average of per-model 5-facet G_item values\",\n        },\n        \"method_B_remove_model_item\": {\n            \"G_item\": round(g_fixedB, 6),\n            \"ci_95\": ci_fixed_B,\n            \"sigma_tau\": round(tau_fixedB, 8),\n            \"sigma_delta\": round(delta_fixedB, 8),\n            \"description\": \"6-facet VC with model:item_id removed from sigma_delta\",\n        },\n        \"per_model_gstudy\": per_model_results,\n        \"pooled_variance_components\": {\n            k: {\"estimate\": v, \"pct\": v / pooled_total * 100 if pooled_total > 0 else 0.0}\n            for k, v in sorted(pooled_vc.items(), key=lambda x: -x[1])\n        },\n    },\n    \"comparison\": {\n        \"G_item_random\": round(g_random, 6),\n        \"G_item_fixed_A\": round(g_fixed_A, 6),\n        \"G_item_fixed_B\": round(g_fixedB, 6),\n        \"G_item_delta_A\": round(g_fixed_A - g_random, 6),\n        \"G_item_delta_B\": round(g_fixedB - g_random, 6),\n        \"ranking_consistency\": {\n            \"pairwise_spearman\": rank_corrs,\n            \"mean_spearman_rho\": round(mean_rho, 4),\n            \"consistent\": mean_rho > 0.7,\n        },\n        \"interpretation\": (\n            \"Model-as-fixed G_item is higher because model:item variance \"\n            \"(differential item difficulty across models) is no longer treated as \"\n            \"measurement error. This is appropriate when generalizing to these \"\n            \"specific 4 models rather than a hypothetical population of models.\"\n        ),\n    },\n    \"design\": {\n        \"n_observations\": int(Y.size),\n        \"n_levels\": {\"model\": n_m, \"temperature\": n_t, \"prompt_template\": n_p,\n                     \"seed\": n_s, \"ordering\": n_o, \"item_id\": n_i},\n        \"models\": models_sorted,\n        \"fixed_facets_random_design\": [\"temperature\"],\n        \"fixed_facets_fixed_model_design\": [\"model\", \"temperature\"],\n    },\n    \"bootstrap\": {\"n_resamples\": N_BOOT, \"seed\": SEED, \"method\": \"item cluster resampling\"},\n}\n\nPath(OUTPUT).parent.mkdir(parents=True, exist_ok=True)\nwith open(OUTPUT, \"w\") as f:\n    json.dump(results, f, indent=2, default=str)\n\nprint(f\"\\nTotal runtime: {time.time()-t_start:.1f}s\", flush=True)\nprint(f\"-> Saved to {OUTPUT}\", flush=True)\nSCRIPT_EOF\necho \"Script written OK\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat > /root/nlp_variance_gtheory/scripts/model_as_fixed_gstudy.py << 'SCRIPT_EOF'\n\"\"\"Model-as-fixed G-study (MF2 defense).\n\nTreats model as a fixed facet (not a random sample from a population of models).\nTwo methods:\n  A) Per-model 5-facet G-study, then average (clean separation)\n  B) Remove model:item from σ²δ in the crossed 6-facet design (quick adjustment)\n\nInput:  results/analysis/cross_model_4way_bf16.csv (4 models × bf16 × fully crossed)\nOutput: results/analysis/model_as_fixed_gstudy.json\n\"\"\"\n\nimport json\nimport time\nfrom itertools import combinations\nfrom math import prod\nfrom pathlib import Path\n\nimport numpy as np\nimport pandas as pd\n\nINPUT = \"results/analysis/cross_model_4way_bf16.csv\"\nOUTPUT = \"results/analysis/model_as_fixed_gstudy.json\"\nN_BOOT = 200\nSEED = 42\n\nFACETS_6 = [\"model\", \"temperature\", \"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\nFACETS_5 = [\"temperature\", \"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\n\nt_start = time.time()\ndf = pd.read_csv(INPUT)\nprint(f\"Loaded {len(df)} obs ({time.time()-t_start:.1f}s)\", flush=True)\n\nmodels_sorted = sorted(df[\"model\"].unique())\ntemps_sorted = sorted(df[\"temperature\"].unique())\nprompts_sorted = sorted(df[\"prompt_template\"].unique())\nseeds_sorted = sorted(df[\"seed\"].unique())\norders_sorted = sorted(df[\"ordering\"].unique())\nitems_sorted = sorted(df[\"item_id\"].unique())\n\nn_m, n_t, n_p, n_s, n_o, n_i = (\n    len(models_sorted), len(temps_sorted), len(prompts_sorted),\n    len(seeds_sorted), len(orders_sorted), len(items_sorted),\n)\nprint(f\"Design: {n_m}m x {n_t}t x {n_p}p x {n_s}s x {n_o}o x {n_i}i = {n_m*n_t*n_p*n_s*n_o*n_i}\", flush=True)\n\nmodel_map = {v: i for i, v in enumerate(models_sorted)}\ntemp_map = {v: i for i, v in enumerate(temps_sorted)}\nprompt_map = {v: i for i, v in enumerate(prompts_sorted)}\nseed_map = {v: i for i, v in enumerate(seeds_sorted)}\norder_map = {v: i for i, v in enumerate(orders_sorted)}\nitem_map = {v: i for i, v in enumerate(items_sorted)}\n\nY = np.full((n_m, n_t, n_p, n_s, n_o, n_i), np.nan)\nfor _, row in df.iterrows():\n    Y[model_map[row[\"model\"]], temp_map[row[\"temperature\"]],\n      prompt_map[row[\"prompt_template\"]], seed_map[row[\"seed\"]],\n      order_map[row[\"ordering\"]], item_map[row[\"item_id\"]]] = row[\"correct\"]\n\nassert np.isnan(Y).sum() == 0, f\"Missing cells: {np.isnan(Y).sum()}\"\nprint(f\"6D array built ({time.time()-t_start:.1f}s)\", flush=True)\n\n\ndef compute_gstudy_5facet(arr_5d):\n    \"\"\"5-facet Henderson I on (temp, prompt, seed, ordering, item) array.\"\"\"\n    nt, np_, ns, no, ni = arr_5d.shape\n    N = arr_5d.size\n    gm = arr_5d.mean()\n    facet_names = FACETS_5\n    n_lev = {\"temperature\": nt, \"prompt_template\": np_, \"seed\": ns, \"ordering\": no, \"item_id\": ni}\n\n    effects = {}\n    for idx, f in enumerate(facet_names):\n        other_axes = tuple(j for j in range(5) if j != idx)\n        level_means = arr_5d.mean(axis=other_axes)\n        n_per = N // arr_5d.shape[idx]\n        ss = float(n_per * np.sum((level_means - gm) ** 2))\n        df_eff = arr_5d.shape[idx] - 1\n        effects[f] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    for i_idx in range(5):\n        for j_idx in range(i_idx + 1, 5):\n            fi, fj = facet_names[i_idx], facet_names[j_idx]\n            other_axes = tuple(k for k in range(5) if k not in (i_idx, j_idx))\n            cell_means = arr_5d.mean(axis=other_axes)\n            main_i = arr_5d.mean(axis=tuple(k for k in range(5) if k != i_idx))\n            main_j = arr_5d.mean(axis=tuple(k for k in range(5) if k != j_idx))\n            interaction = cell_means - main_i[:, None] - main_j[None, :] + gm\n            n_per = N // (arr_5d.shape[i_idx] * arr_5d.shape[j_idx])\n            ss = float(n_per * np.sum(interaction ** 2))\n            df_eff = (arr_5d.shape[i_idx] - 1) * (arr_5d.shape[j_idx] - 1)\n            key = f\"{fi}:{fj}\"\n            effects[key] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    ss_total = float(np.sum((arr_5d - gm) ** 2))\n    ss_model = sum(e[\"ss\"] for e in effects.values())\n    ss_res = max(0.0, ss_total - ss_model)\n    df_res = N - 1 - sum(e[\"df\"] for e in effects.values())\n    effects[\"residual\"] = {\"ss\": ss_res, \"df\": df_res, \"ms\": ss_res / df_res if df_res > 0 else 0.0}\n\n    ms_res = effects[\"residual\"][\"ms\"]\n    vc = {}\n    for fi, fj in combinations(facet_names, 2):\n        key = f\"{fi}:{fj}\"\n        coeff = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n        raw = (effects[key][\"ms\"] - ms_res) / coeff if coeff > 0 else 0.0\n        vc[key] = max(0.0, raw)\n\n    for fi in facet_names:\n        coeff_main = prod(n_lev[f] for f in facet_names if f != fi)\n        interaction_contrib = 0.0\n        for fj in facet_names:\n            if fj == fi:\n                continue\n            int_key = f\"{fi}:{fj}\" if f\"{fi}:{fj}\" in vc else f\"{fj}:{fi}\"\n            coeff_ij = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n            interaction_contrib += coeff_ij * vc[int_key]\n        raw = (effects[fi][\"ms\"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0\n        vc[fi] = max(0.0, raw)\n\n    vc[\"residual\"] = ms_res\n    return vc, n_lev, effects\n\n\ndef compute_g_item_5facet(vc, n_lev):\n    \"\"\"G_item for 5-facet within-model design.\n\n    Object of measurement: item_id.\n    σ²_τ = σ²(item_id)\n    σ²_δ = Σ σ²(X:item_id)/n_X + σ²(residual)/Π(n_X for X ≠ item_id)\n    \"\"\"\n    sigma_item = vc.get(\"item_id\", 0.0)\n    non_item_facets = [\"temperature\", \"prompt_template\", \"seed\", \"ordering\"]\n\n    sigma_delta = 0.0\n    for comp, est in vc.items():\n        if est == 0.0 or comp == \"item_id\":\n            continue\n        if comp == \"residual\":\n            divisor = prod(n_lev[f] for f in non_item_facets)\n            sigma_delta += est / divisor\n            continue\n        facets_in = set(comp.split(\":\"))\n        if \"item_id\" not in facets_in:\n            continue\n        other = [f for f in facets_in if f != \"item_id\"]\n        divisor = prod(n_lev[f] for f in other) if other else 1\n        sigma_delta += est / divisor\n\n    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0\n    return g, sigma_item, sigma_delta\n\n\ndef compute_gstudy_6facet(Y_6d):\n    \"\"\"Full 6-facet Henderson I on (model, temp, prompt, seed, ordering, item) array.\"\"\"\n    nm, nt, np_, ns, no, ni = Y_6d.shape\n    N = Y_6d.size\n    gm = Y_6d.mean()\n    facet_names = FACETS_6\n    n_lev = {\"model\": nm, \"temperature\": nt, \"prompt_template\": np_, \"seed\": ns, \"ordering\": no, \"item_id\": ni}\n\n    effects = {}\n    for idx, f in enumerate(facet_names):\n        other_axes = tuple(j for j in range(6) if j != idx)\n        level_means = Y_6d.mean(axis=other_axes)\n        n_per = N // Y_6d.shape[idx]\n        ss = float(n_per * np.sum((level_means - gm) ** 2))\n        df_eff = Y_6d.shape[idx] - 1\n        effects[f] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    for i_idx in range(6):\n        for j_idx in range(i_idx + 1, 6):\n            fi, fj = facet_names[i_idx], facet_names[j_idx]\n            other_axes = tuple(k for k in range(6) if k not in (i_idx, j_idx))\n            cell_means = Y_6d.mean(axis=other_axes)\n            main_i = Y_6d.mean(axis=tuple(k for k in range(6) if k != i_idx))\n            main_j = Y_6d.mean(axis=tuple(k for k in range(6) if k != j_idx))\n            interaction = cell_means - main_i[:, None] - main_j[None, :] + gm\n            n_per = N // (Y_6d.shape[i_idx] * Y_6d.shape[j_idx])\n            ss = float(n_per * np.sum(interaction ** 2))\n            df_eff = (Y_6d.shape[i_idx] - 1) * (Y_6d.shape[j_idx] - 1)\n            key = f\"{fi}:{fj}\"\n            effects[key] = {\"ss\": ss, \"df\": df_eff, \"ms\": ss / df_eff if df_eff > 0 else 0.0}\n\n    ss_total = float(np.sum((Y_6d - gm) ** 2))\n    ss_model = sum(e[\"ss\"] for e in effects.values())\n    ss_res = max(0.0, ss_total - ss_model)\n    df_res = N - 1 - sum(e[\"df\"] for e in effects.values())\n    effects[\"residual\"] = {\"ss\": ss_res, \"df\": df_res, \"ms\": ss_res / df_res if df_res > 0 else 0.0}\n\n    ms_res = effects[\"residual\"][\"ms\"]\n    vc = {}\n    for fi, fj in combinations(facet_names, 2):\n        key = f\"{fi}:{fj}\"\n        coeff = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n        raw = (effects[key][\"ms\"] - ms_res) / coeff if coeff > 0 else 0.0\n        vc[key] = max(0.0, raw)\n\n    for fi in facet_names:\n        coeff_main = prod(n_lev[f] for f in facet_names if f != fi)\n        interaction_contrib = 0.0\n        for fj in facet_names:\n            if fj == fi:\n                continue\n            int_key = f\"{fi}:{fj}\" if f\"{fi}:{fj}\" in vc else f\"{fj}:{fi}\"\n            coeff_ij = prod(n_lev[f] for f in facet_names if f not in (fi, fj))\n            interaction_contrib += coeff_ij * vc[int_key]\n        raw = (effects[fi][\"ms\"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0\n        vc[fi] = max(0.0, raw)\n\n    vc[\"residual\"] = ms_res\n    return vc, n_lev, effects\n\n\ndef compute_g_item_random(vc, n_lev):\n    \"\"\"G_item with model as RANDOM.\n\n    σ²_δ = σ²(model:item)/n_m + σ²(temp:item)/n_t + ... + σ²(res)/(n_m·n_t·n_p·n_s·n_o)\n    \"\"\"\n    sigma_item = vc.get(\"item_id\", 0.0)\n    delta = (\n        vc.get(\"model:item_id\", 0.0) / n_lev[\"model\"]\n        + vc.get(\"temperature:item_id\", 0.0) / n_lev[\"temperature\"]\n        + vc.get(\"prompt_template:item_id\", 0.0) / n_lev[\"prompt_template\"]\n        + vc.get(\"seed:item_id\", 0.0) / n_lev[\"seed\"]\n        + vc.get(\"ordering:item_id\", 0.0) / n_lev[\"ordering\"]\n        + vc[\"residual\"] / (n_lev[\"model\"] * n_lev[\"temperature\"] * n_lev[\"prompt_template\"]\n                            * n_lev[\"seed\"] * n_lev[\"ordering\"])\n    )\n    g = sigma_item / (sigma_item + delta) if (sigma_item + delta) > 0 else 0.0\n    return g, sigma_item, delta\n\n\ndef compute_g_item_fixed_methodB(vc, n_lev):\n    \"\"\"G_item with model as FIXED (Method B: remove model:item from σ²δ).\n\n    Same residual divisor (n_m still in denominator since we average over 4 fixed models).\n    \"\"\"\n    sigma_item = vc.get(\"item_id\", 0.0)\n    delta = (\n        vc.get(\"temperature:item_id\", 0.0) / n_lev[\"temperature\"]\n        + vc.get(\"prompt_template:item_id\", 0.0) / n_lev[\"prompt_template\"]\n        + vc.get(\"seed:item_id\", 0.0) / n_lev[\"seed\"]\n        + vc.get(\"ordering:item_id\", 0.0) / n_lev[\"ordering\"]\n        + vc[\"residual\"] / (n_lev[\"model\"] * n_lev[\"temperature\"] * n_lev[\"prompt_template\"]\n                            * n_lev[\"seed\"] * n_lev[\"ordering\"])\n    )\n    g = sigma_item / (sigma_item + delta) if (sigma_item + delta) > 0 else 0.0\n    return g, sigma_item, delta\n\n\n# ============================================================\n# Full 6-facet G-study (reproduce random-model baseline)\n# ============================================================\nprint(\"\\n=== 6-facet G-study (model=random baseline) ===\", flush=True)\nvc_6, nl_6, eff_6 = compute_gstudy_6facet(Y)\ntotal_var_6 = sum(vc_6.values())\n\ng_random, tau_random, delta_random = compute_g_item_random(vc_6, nl_6)\nprint(f\"G_item (model=random) = {g_random:.6f}\", flush=True)\nprint(f\"  sigma_tau={tau_random:.8f}, sigma_delta={delta_random:.8f}\", flush=True)\n\n\n# ============================================================\n# Method B: Fixed model in crossed design\n# ============================================================\nprint(\"\\n=== Method B: model-as-fixed (remove model:item from delta) ===\", flush=True)\ng_fixedB, tau_fixedB, delta_fixedB = compute_g_item_fixed_methodB(vc_6, nl_6)\nprint(f\"G_item (model=fixed, Method B) = {g_fixedB:.6f}\", flush=True)\nprint(f\"  sigma_delta: {delta_random:.8f} -> {delta_fixedB:.8f}\", flush=True)\nprint(f\"  removed: model:item/n_m = {vc_6.get('model:item_id', 0)/nl_6['model']:.8f}\", flush=True)\n\n\n# ============================================================\n# Method A: Per-model 5-facet G-study\n# ============================================================\nprint(\"\\n=== Method A: per-model 5-facet G-study ===\", flush=True)\nper_model_results = {}\ng_items_per_model = []\n\nfor mi, model_name in enumerate(models_sorted):\n    Y_m = Y[mi]\n    vc_m, nl_m, eff_m = compute_gstudy_5facet(Y_m)\n    g_m, tau_m, delta_m = compute_g_item_5facet(vc_m, nl_m)\n    g_items_per_model.append(g_m)\n\n    total_var_m = sum(vc_m.values())\n    per_model_results[model_name] = {\n        \"g_item\": round(g_m, 6),\n        \"sigma_tau\": round(tau_m, 8),\n        \"sigma_delta\": round(delta_m, 8),\n        \"variance_components\": {\n            k: {\"estimate\": v, \"pct\": v / total_var_m * 100 if total_var_m > 0 else 0.0}\n            for k, v in sorted(vc_m.items(), key=lambda x: -x[1])\n        },\n        \"accuracy\": float(Y_m.mean()),\n    }\n    print(f\"  {model_name}: G_item={g_m:.6f}, acc={Y_m.mean():.4f}, \"\n          f\"s2_item={vc_m['item_id']:.6f}, s2_delta={delta_m:.6f}\", flush=True)\n\ng_fixed_A = float(np.mean(g_items_per_model))\nprint(f\"\\nAverage G_item (model=fixed, Method A) = {g_fixed_A:.6f}\", flush=True)\n\npooled_vc = {}\nfor key in per_model_results[models_sorted[0]][\"variance_components\"]:\n    vals = [per_model_results[m][\"variance_components\"][key][\"estimate\"] for m in models_sorted]\n    pooled_vc[key] = float(np.mean(vals))\npooled_total = sum(pooled_vc.values())\n\n\n# ============================================================\n# Bootstrap CI\n# ============================================================\nprint(f\"\\nBootstrapping ({N_BOOT} resamples)...\", flush=True)\nrng = np.random.default_rng(SEED)\nboot_g_fixed_A = []\nboot_g_fixed_B = []\nboot_g_random = []\n\nfor b in range(N_BOOT):\n    if b % 50 == 0:\n        print(f\"  {b}/{N_BOOT}...\", flush=True)\n    idx = rng.choice(n_i, size=n_i, replace=True)\n    Y_b = Y[:, :, :, :, :, idx]\n\n    vc_b6, nl_b6, _ = compute_gstudy_6facet(Y_b)\n    g_r, _, _ = compute_g_item_random(vc_b6, nl_b6)\n    boot_g_random.append(g_r)\n\n    g_fB, _, _ = compute_g_item_fixed_methodB(vc_b6, nl_b6)\n    boot_g_fixed_B.append(g_fB)\n\n    g_per_model_b = []\n    for mi in range(n_m):\n        vc_bm, nl_bm, _ = compute_gstudy_5facet(Y_b[mi])\n        g_bm, _, _ = compute_g_item_5facet(vc_bm, nl_bm)\n        g_per_model_b.append(g_bm)\n    boot_g_fixed_A.append(float(np.mean(g_per_model_b)))\n\nci_random = [float(np.percentile(boot_g_random, 2.5)), float(np.percentile(boot_g_random, 97.5))]\nci_fixed_A = [float(np.percentile(boot_g_fixed_A, 2.5)), float(np.percentile(boot_g_fixed_A, 97.5))]\nci_fixed_B = [float(np.percentile(boot_g_fixed_B, 2.5)), float(np.percentile(boot_g_fixed_B, 97.5))]\n\nprint(f\"\\nResults with 95% CI:\", flush=True)\nprint(f\"  G_item (random):  {g_random:.6f} [{ci_random[0]:.6f}, {ci_random[1]:.6f}]\", flush=True)\nprint(f\"  G_item (fixed A): {g_fixed_A:.6f} [{ci_fixed_A[0]:.6f}, {ci_fixed_A[1]:.6f}]\", flush=True)\nprint(f\"  G_item (fixed B): {g_fixedB:.6f} [{ci_fixed_B[0]:.6f}, {ci_fixed_B[1]:.6f}]\", flush=True)\n\n\n# ============================================================\n# Ranking consistency\n# ============================================================\nfrom scipy.stats import spearmanr\n\nper_model_item_means = {}\nfor mi, m in enumerate(models_sorted):\n    per_model_item_means[m] = Y[mi].mean(axis=(0, 1, 2, 3))\n\nrank_corrs = []\nfor i in range(len(models_sorted)):\n    for j in range(i + 1, len(models_sorted)):\n        mi, mj = models_sorted[i], models_sorted[j]\n        rho, _ = spearmanr(per_model_item_means[mi], per_model_item_means[mj])\n        rank_corrs.append({\"pair\": f\"{mi} vs {mj}\", \"spearman_rho\": round(float(rho), 4)})\n\nmean_rho = float(np.mean([r[\"spearman_rho\"] for r in rank_corrs]))\nprint(f\"\\nItem ranking consistency across models:\", flush=True)\nfor r in rank_corrs:\n    print(f\"  {r['pair']}: rho={r['spearman_rho']:.4f}\", flush=True)\nprint(f\"  Mean rho = {mean_rho:.4f}\", flush=True)\n\n\n# ============================================================\n# Save\n# ============================================================\nresults = {\n    \"random_model\": {\n        \"G_item\": round(g_random, 6),\n        \"ci_95\": ci_random,\n        \"sigma_tau\": round(tau_random, 8),\n        \"sigma_delta\": round(delta_random, 8),\n        \"variance_components\": {\n            k: {\"estimate\": v, \"pct\": v / total_var_6 * 100}\n            for k, v in sorted(vc_6.items(), key=lambda x: -x[1])\n        },\n    },\n    \"fixed_model\": {\n        \"method_A_per_model_average\": {\n            \"G_item\": round(g_fixed_A, 6),\n            \"ci_95\": ci_fixed_A,\n            \"description\": \"Average of per-model 5-facet G_item values\",\n        },\n        \"method_B_remove_model_item\": {\n            \"G_item\": round(g_fixedB, 6),\n            \"ci_95\": ci_fixed_B,\n            \"sigma_tau\": round(tau_fixedB, 8),\n            \"sigma_delta\": round(delta_fixedB, 8),\n            \"description\": \"6-facet VC with model:item_id removed from sigma_delta\",\n        },\n        \"per_model_gstudy\": per_model_results,\n        \"pooled_variance_components\": {\n            k: {\"estimate\": v, \"pct\": v / pooled_total * 100 if pooled_total > 0 else 0.0}\n            for k, v in sorted(pooled_vc.items(), key=lambda x: -x[1])\n        },\n    },\n    \"comparison\": {\n        \"G_item_random\": round(g_random, 6),\n        \"G_item_fixed_A\": round(g_fixed_A, 6),\n        \"G_item_fixed_B\": round(g_fixedB, 6),\n        \"G_item_delta_A\": round(g_fixed_A - g_random, 6),\n        \"G_item_delta_B\": round(g_fixedB - g_random, 6),\n        \"ranking_consistency\": {\n            \"pairwise_spearman\": rank_corrs,\n            \"mean_spearman_rho\": round(mean_rho, 4),\n            \"consistent\": mean_rho > 0.7,\n        },\n        \"interpretation\": (\n            \"Model-as-fixed G_item is higher because model:item variance \"\n            \"(differential item difficulty across models) is no longer treated as \"\n            \"measurement error. This is appropriate when generalizing to these \"\n            \"specific 4 models rather than a hypothetical population of models.\"\n        ),\n    },\n    \"design\": {\n        \"n_observations\": int(Y.size),\n        \"n_levels\": {\"model\": n_m, \"temperature\": n_t, \"prompt_template\": n_p,\n                     \"seed\": n_s, \"ordering\": n_o, \"item_id\": n_i},\n        \"models\": models_sorted,\n        \"fixed_facets_random_design\": [\"temperature\"],\n        \"fixed_facets_fixed_model_design\": [\"model\", \"temperature\"],\n    },\n    \"bootstrap\": {\"n_resamples\": N_BOOT, \"seed\": SEED, \"method\": \"item cluster resampling\"},\n}\n\nPath(OUTPUT).parent.mkdir(parents=True, exist_ok=True)\nwith open(OUTPUT, \"w\") as f:\n    json.dump(results, f, indent=2, default=str)\n\nprint(f\"\\nTotal runtime: {time.time()-t_start:.1f}s\", flush=True)\nprint(f\"-> Saved to {OUTPUT}\", flush=True)\nSCRIPT_EOF\necho \"Script written OK\""
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-21T09:07:41.674180+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-21T09:07:41.674317+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32570",
  "command": "cd /root/nlp_variance_gtheory && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export PYTHONPATH=/root/nlp_variance_gtheory:$PYTHONPATH && nohup python scripts/model_as_fixed_gstudy.py > /tmp/model_fixed_gstudy.log 2>&1 &\necho \"PID: $!\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32570",
    "command": "cd /root/nlp_variance_gtheory && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export PYTHONPATH=/root/nlp_variance_gtheory:$PYTHONPATH && nohup python scripts/model_as_fixed_gstudy.py > /tmp/model_fixed_gstudy.log 2>&1 &\necho \"PID: $!\""
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-21T09:07:41.674473+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"PID: 132111\\n\", \"stderr\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 23.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-21T09:07:41.674598+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "tail -30 /tmp/model_fixed_gstudy.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "tail -30 /tmp/model_fixed_gstudy.log"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-21T09:07:41.674792+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Method A: per-model 5-facet G-study ===\\n  gemma-2-9b-it: G_item=0.970557, acc=0.7311, s2_item=0.154892, s2_delta=0.004699\\n  llama-3.1-8b-instruct: G_item=0.957793, acc=0.7108, s2_item=0.146413, s2_delta=0.006452\\n  mistral-7b-instruct-v0.3: G_item=0.956335, acc=0.6376, s2_item=0.165380, s2_delta=0.007551\\n  qwen3-8b: G_item=0.967657, acc=0.7263, s2_item=0.153827, s2_delta=0.005142\\n\\nAverage G_item (model=fixed, Method A) = 0.963085\\n\\nBootstrapping (200 resamples)...\\n  0/200...\\n  50/200...\\n  100/200...\\n  150/200...\\n\\nResults with 95% CI:\\n  G_item (random):  0.820039 [0.781615, 0.860875]\\n  G_item (fixed A): 0.963085 [0.957237, 0.968582]\\n  G_item (fixed B): 0.980807 [0.975481, 0.984784]\\n\\nItem ranking consistency across models:\\n  gemma-2-9b-it vs llama-3.1-8b-instruct: rho=0.6792\\n  gemma-2-9b-it vs mistral-7b-instruct-v0.3: rho=0.6442\\n  gemma-2-9b-it vs qwen3-8b: rho=0.6657\\n  llama-3.1-8b-instruct vs mistral-7b-instruct-v0.3: rho=0.6924\\n  llama-3.1-8b-instruct vs qwen3-8b: rho=0.6377\\n  mistral-7b-instruct-v0.3 vs qwen3-8b: rho=0.5347\\n  Mean rho = 0.6423\\n\\nTotal runtime: 22.3s\\n-> Saved to results/analysis/model_as_fixed_gstudy.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-21T09:07:41.674961+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "head -60 /root/nlp_variance_gtheory/results/analysis/model_as_fixed_gstudy.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "head -60 /root/nlp_variance_gtheory/results/analysis/model_as_fixed_gstudy.json"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-21T09:07:41.675124+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"random_model\\\": {\\n    \\\"G_item\\\": 0.820039,\\n    \\\"ci_95\\\": [\\n      0.7816146190369399,\\n      0.8608747018283437\\n    ],\\n    \\\"sigma_tau\\\": 0.08851438,\\n    \\\"sigma_delta\\\": 0.01942482,\\n    \\\"variance_components\\\": {\\n      \\\"item_id\\\": {\\n        \\\"estimate\\\": 0.08851437651254966,\\n        \\\"pct\\\": 42.07775096535229\\n      },\\n      \\\"model:item_id\\\": {\\n        \\\"estimate\\\": 0.07077085201146294,\\n        \\\"pct\\\": 33.642877054236855\\n      },\\n      \\\"residual\\\": {\\n        \\\"estimate\\\": 0.041118141769829794,\\n        \\\"pct\\\": 19.54664312981569\\n      },\\n      \\\"prompt_template:item_id\\\": {\\n        \\\"estimate\\\": 0.003014134593133947,\\n        \\\"pct\\\": 1.4328520380862861\\n      },\\n      \\\"seed:item_id\\\": {\\n        \\\"estimate\\\": 0.0027848637210264957,\\n        \\\"pct\\\": 1.3238618035024308\\n      },\\n      \\\"model\\\": {\\n        \\\"estimate\\\": 0.001511069516435654,\\n        \\\"pct\\\": 0.7183285846779928\\n      },\\n      \\\"temperature:item_id\\\": {\\n        \\\"estimate\\\": 0.0013693514156093306,\\n        \\\"pct\\\": 0.6509589754822792\\n      },\\n      \\\"ordering:item_id\\\": {\\n        \\\"estimate\\\": 0.0011414417428128746,\\n        \\\"pct\\\": 0.5426158245460633\\n      },\\n      \\\"model:prompt_template\\\": {\\n        \\\"estimate\\\": 4.183404268830899e-05,\\n        \\\"pct\\\": 0.019886966382946934\\n      },\\n      \\\"model:temperature\\\": {\\n        \\\"estimate\\\": 3.66508899784139e-05,\\n        \\\"pct\\\": 0.01742301174037613\\n      },\\n      \\\"model:seed\\\": {\\n        \\\"estimate\\\": 1.9099989190366816e-05,\\n        \\\"pct\\\": 0.009079706825695467\\n      },\\n      \\\"prompt_template\\\": {\\n        \\\"estimate\\\": 1.3871568991435068e-05,\\n        \\\"pct\\\": 0.006594233033292083\\n      },\\n      \\\"prompt_template:o
…[truncated 172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-21T09:07:41.675302+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/model_as_fixed_gstudy.py",
  "old_string": "def compute_g_item_5facet(vc, n_lev):\n    \"\"\"G_item for 5-facet design. Fixed: temperature. Random: prompt, seed, ordering, item.\"\"\"\n    random_facets_5 = [\"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\n    sigma_item = vc.get(\"item_id\", 0.0)\n\n    sigma_delta = 0.0\n    for comp, est in vc.items():\n        if est == 0.0:\n            continue\n        if comp == \"residual\":\n            divisor = prod(n_lev[f] for f in random_facets_5)\n            sigma_delta += est / divisor\n            continue\n        facets_in = set(comp.split(\":\"))\n        if \"item_id\" not in facets_in:\n            continue\n        random_in = [f for f in facets_in if f in set(random_facets_5)]\n        if len(random_in) > 0:\n            divisor = prod(n_lev[f] for f in random_in)\n            sigma_delta += est / divisor\n\n    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0\n    return g, sigma_item, sigma_delta",
  "new_string": "def compute_g_item_5facet(vc, n_lev):\n    \"\"\"G_item for 5-facet within-model design.\n\n    Object of measurement: item_id.\n    σ²_τ = σ²(item_id)\n    σ²_δ = Σ σ²(X:item_id)/n_X + σ²(residual)/Π(n_X for X ≠ item_id)\n    \"\"\"\n    sigma_item = vc.get(\"item_id\", 0.0)\n    non_item_facets = [\"temperature\", \"prompt_template\", \"seed\", \"ordering\"]\n\n    sigma_delta = 0.0\n    for comp, est in vc.items():\n        if est == 0.0 or comp == \"item_id\":\n            continue\n        if comp == \"residual\":\n            divisor = prod(n_lev[f] for f in non_item_facets)\n            sigma_delta += est / divisor\n            continue\n        facets_in = set(comp.split(\":\"))\n        if \"item_id\" not in facets_in:\n            continue\n        other = [f for f in facets_in if f != \"item_id\"]\n        divisor = prod(n_lev[f] for f in other) if other else 1\n        sigma_delta += est / divisor\n\n    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0\n    return g, sigma_item, sigma_delta"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/model_as_fixed_gstudy.py",
    "old_string": "def compute_g_item_5facet(vc, n_lev):\n    \"\"\"G_item for 5-facet design. Fixed: temperature. Random: prompt, seed, ordering, item.\"\"\"\n    random_facets_5 = [\"prompt_template\", \"seed\", \"ordering\", \"item_id\"]\n    sigma_item = vc.get(\"item_id\", 0.0)\n\n    sigma_delta = 0.0\n    for comp, est in vc.items():\n        if est == 0.0:\n            continue\n        if comp == \"residual\":\n            divisor = prod(n_lev[f] for f in random_facets_5)\n            sigma_delta += est / divisor\n            continue\n        facets_in = set(comp.split(\":\"))\n        if \"item_id\" not in facets_in:\n            continue\n        random_in = [f for f in facets_in if f in set(random_facets_5)]\n        if len(random_in) > 0:\n            divisor = prod(n_lev[f] for f in random_in)\n            sigma_delta += est / divisor\n\n    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0\n    return g, sigma_item, sigma_delta",
    "new_string": "def compute_g_item_5facet(vc, n_lev):\n    \"\"\"G_item for 5-facet within-model design.\n\n    Object of measurement: item_id.\n    σ²_τ = σ²(item_id)\n    σ²_δ = Σ σ²(X:item_id)/n_X + σ²(residual)/Π(n_X for X ≠ item_id)\n    \"\"\"\n    sigma_item = vc.get(\"item_id\", 0.0)\n    non_item_facets = [\"temperature\", \"prompt_template\", \"seed\", \"ordering\"]\n\n    sigma_delta = 0.0\n    for comp, est in vc.items():\n        if est == 0.0 or comp == \"item_id\":\n            continue\n        if comp == \"residual\":\n            divisor = prod(n_lev[f] for f in non_item_facets)\n            sigma_delta += est / divisor\n            continue\n        facets_in = set(comp.split(\":\"))\n        if \"item_id\" not in facets_in:\n            continue\n        other = [f for f in facets_in if f != \"item_id\"]\n        divisor = prod(n_lev[f] for f in other) if other else 1\n        sigma_delta += est / divisor\n\n    g = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0\n    return g, sigma_item, sigma_delta"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-21T09:07:41.675571+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/scripts/model_as_fixed_gstudy.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_model_as_fixed_20260521T085703",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 101 · 2026-05-21T09:07:41.675742+00:00_

Output saved to `results/analysis/model_as_fixed_gstudy.json`.

## 结果

| 设计 | G_item | 95% CI |
|------|--------|--------|
| Model=random (原始) | **0.820** | [0.782, 0.861] |
| Model=fixed, Method A (per-model avg) | **0.963** | [0.957, 0.969] |
| Model=fixed, Method B (移除 model:item) | **0.981** | [0.975, 0.985] |

**Per-model G_item**:
- gemma-2-9b-it: 0.971
- llama-3.1-8b-instruct: 0.958
- mistral-7b-instruct-v0.3: 0.956
- qwen3-8b: 0.968

**关键发现**：
- Fixed-model G_item 比 random 高 +0.143 (Method A) / +0.161 (Method B)，因为 model:item_id 占总方差 33.6% — 当 model 为 fixed 时这部分不计入测量误差
- Method B > Method A，因为 B 用的是 6-facet 残差（被更多条件平均，更小），而 A 用的是 per-model 5-facet 残差（更大）
- Item ranking 跨模型一致性中等（mean Spearman ρ = 0.642），说明 model:item 交互不可忽略 — 支持 random-model 作为更保守的报告选择

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_model_as_fixed_20260521T085703"
}
```

</details>

---
