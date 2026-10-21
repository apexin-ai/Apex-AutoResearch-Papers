# analysis gpt2m s43 bf16 leadlag

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 189
- **Recorded user turns:** 0
- **Tool calls:** 94
- **Original source:** `logs/chats/worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603.jsonl`
- **Structured JSON:** [`ff27667fc97a9dfe681c.json`](../../sessions/ff/ff27667fc97a9dfe681c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

189 recorded events

### Tool call

_source line 1 · 2026-05-18T21:27:49.829545+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T21:27:49.829836+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T21:27:49.830014+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'gen_wiki_gpt2m_a100_s42_v4'}",
  "project": "distrib_canary_collapse",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'gen_wiki_gpt2m_a100_s42_v4'}",
    "project": "distrib_canary_collapse",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T21:27:49.830150+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.3199}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T21:27:49.830300+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T21:27:49.830439+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-18T21:27:49.830563+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"detrending_utils.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.06}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T21:27:49.830682+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"EXIT_CODE\\nall_metrics.json\\nconfig.json\\ngen_0\\ngen_1\\ngen_10\\ngen_2\\ngen_3\\ngen_4\\ngen_5\\ngen_6\\ngen_7\\ngen_8\\ngen_9\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T21:27:49.830827+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "project": "distrib_canary_collapse",
  "fields": "['*']",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "project": "distrib_canary_collapse",
    "fields": "['*']",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T21:27:49.831068+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"gen_gpt2m_a100_s43_bf16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:25:55.336Z\", \"updated_at\": \"2026-05-18T21:14:52.266Z\", \"spec\": {\"command\": \"python -u iterative_train.py --model_name openai-community/gpt2-medium --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 1.0 --bf16 --output_dir results/generalize/gpt2m_wiki_a100_s43_bf16\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:1\"], \"pid\": \"16116\", \"log_path\": \"~/runs/distrib_canary_collapse/gen_gpt2m_a100_s43_bf16.log\", \"submitted_at\": \"2026-05-18T17:25:55.193Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"openai-community/gpt2-medium\", \"seed\": 43, \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"wall_clock_seconds\": 12444.6, \"gpu_hours\": 3.46, \"checkpoint_path\": \"results/generalize/gpt2m_wiki_a100_s43_bf16\"}, \"hypothesis\": \"GPT-2-medium multi-seed s43: GPT-2-medium × WikiText-103 × α=1.0 × seed=43. Validates s42 cross-architecture results (K≥4=6/8) are reproducible.\", \"reproduce\": {\"finished_at\": \"2026-05-18T20:53:18.007Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T20:53:19.746Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:53:22.622800+00:00\"}]}}, \"alpha_sweep_a060_s42_bf16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:26:43.407Z\", \"updated_at\": \"2026-05-18T21:14:50.289Z\", \"spec\": {\"command\": \"python -u iterative_train.py --model_name EleutherAI/pythia-410m --seed 42 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 0.60 --bf16 --output_dir results/alpha_sweep/a060_s42_bf16\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:3\"], \"pid\": 
…[truncated 5849 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T21:27:49.831229+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T21:27:49.831465+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"token_entropy\\\": 3.6020808767427344,\\n    \\\"self_bleu\\\": 0.009580845530412248,\\n    \\\"distinct_1\\\": 0.10922127457560528,\\n    \\\"distinct_2\\\": 0.5664917780524339,\\n    \\\"distinct_3\\\": 0.8652146154601709,\\n    \\\"ece\\\": 0.011054360637091282,\\n    \\\"effective_rank\\\": 2.3594859133162567,\\n    \\\"perplexity\\\": 32.907320786093294,\\n    \\\"mauve\\\": 0.03180325466092311,\\n    \\\"generation\\\": 0,\\n    \\\"intervention_triggered\\\": false,\\n    \\\"trigger_gen\\\": null,\\n    \\\"effective_alpha\\\": 1.0\\n  },\\n  {\\n    \\\"token_entropy\\\": 3.0175825482178156,\\n    \\\"self_bleu\\\": 0.009223467529265237,\\n    \\\"distinct_1\\\": 0.11012468337309102,\\n    \\\"distinct_2\\\": 0.5688756271108634,\\n    \\\"distinct_3\\\": 0.863862542729963,\\n    \\\"ece\\\": 0.013150979689605163,\\n    \\\"effective_rank\\\": 2.5295110287101337,\\n    \\\"perplexity\\\": 25.13798337696562,\\n    \\\"mauve\\\": 0.035410410872493706,\\n    \\\"generation\\\": 1,\\n    \\\"intervention_triggered\\\": false,\\n    \\\"trigger_gen\\\": null,\\n    \\\"effective_alpha\\\": 1.0\\n  },\\n  {\\n    \\\"token_entropy\\\": 2.9256155300464513,\\n    \\\"self_bleu\\\": 0.010028909654000284,\\n    \\\"distinct_1\\\": 0.09890144505256526,\\n    \\\"distinct_2\\\": 0.5311062811062811,\\n    \\\"distinct_3\\\": 0.8396399518045723,\\n    \\\"ece\\\": 0.02608590842847843,\\n    \\\"effective_rank\\\": 2.6133973392601515,\\n    \\\"perplexity\\\": 26.779638876026645,\\n    \\\"mauve\\\": 0.0353651678158546,\\n    \\\"generation\\\": 2,\\n    \\\"intervention_triggered\\\": false,\\n    \\\"trigger_gen\\\": null,\\n    \\\"effective_alpha\\\": 1.0\\n  },\\n  {\\n    \\\"token_entropy\\\": 2.9861721710101357,\\n    \\\"self_bleu\\\": 0.010222916018421688,\\n    \\\"distinct_1\\\": 0.09195276195252686,\\n    \\\"distinct_2\\\": 0.49496113096357597,\\n    \\\"distinct_3\\\": 0.81385033736393
…[truncated 4382 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T21:27:49.831618+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"*.py\" -path \"*/analysis/*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"*.py\" -path \"*/analysis/*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T21:27:49.831739+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16/EXIT_CODE",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16/EXIT_CODE",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T21:27:49.831858+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/analysis/detrending_utils.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T21:27:49.831992+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T21:27:49.832107+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/analysis/**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/analysis/**/*.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T21:27:49.832217+00:00_

artifacts/analysis/cross_alpha/cross_alpha_analysis_v4.py
artifacts/analysis/consensus_framework/consensus_framework.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T21:27:49.832384+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/consensus_framework/consensus_framework.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/consensus_framework/consensus_framework.py"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T21:27:49.832689+00:00_

1	"""
2	Multi-method consensus framework for canary→downstream association robustness.
3	
4	Formalizes "robust association": a pair is robust only when ≥method_threshold
5	independent statistical methods agree (each requiring ≥seed_threshold seeds
6	significant). Two-stage aggregation: seed→method verdict, then method→consensus.
7	
8	Input:  results/mvp/analysis/method_ablation.json
9	Output: consensus classification, sensitivity heatmap, FPR/FNR table (JSON)
10	
11	Dependencies: numpy, json (stdlib)
12	"""
13	
14	import json
15	import os
16	
17	import numpy as np
18	
19	METHOD_NAMES = [
20	    "naive_pearson",
21	    "differenced_xcorr",
22	    "threshold_onset",
23	    "toda_yamamoto",
24	    "permutation_granger",
25	]
26	
27	# Primary FPR ground truth: alpha=0.0 null control; differenced_xcorr retained for legacy
28	DIFF_INDEX = 1
29	
30	
31	def _to_native(obj):
32	    """Convert numpy types to Python native for JSON serialization."""
33	    if isinstance(obj, (np.integer,)):
34	        return int(obj)
35	    if isinstance(obj, (np.floating,)):
36	        return float(obj)
37	    if isinstance(obj, (np.bool_,)):
38	        return bool(obj)
39	    if isinstance(obj, np.ndarray):
40	        return obj.tolist()
41	    return obj
42	
43	
44	class NumpyEncoder(json.JSONEncoder):
45	    """JSON encoder that handles numpy types."""
46	    def default(self, obj):
47	        native = _to_native(obj)
48	        if native is not obj:
49	            return native
50	        return super().default(obj)
51	
52	
53	def load_sig_matrix(ablation_path, apply_fdr=True):
54	    """
55	    Load method_ablation.json into a boolean significance tensor.
56	
57	    Args:
58	        ablation_path: path to method_ablation.json
59	
60	    Returns:
61	        sig_matrix: np.ndarray, shape (5, 16, 4), dtype bool
62	                    axes = (method, pair, seed)
63	        pair_names: list of (canary, downstream) tuples, len 16
64	        method_names: list of str, len 5
65	        seeds: li
…[truncated 24654 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T21:27:49.832849+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/cross_alpha/cross_alpha_analysis_v4.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/cross_alpha/cross_alpha_analysis_v4.py"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T21:27:49.833306+00:00_

1	"""Cross-alpha analysis v4 with per-alpha consensus classification.
2	
3	Extends v3 with:
4	  5. Per-alpha multi-method consensus classification (regime-dependent validity)
5	  6. Markdown report output
6	
7	Handles mixed data paths:
8	  - alpha-sweep: results/alpha_sweep/a{NNN}_s42/all_metrics.json (single seed)
9	  - alpha=1.0:   results/mvp/rep_{42..45}/all_metrics.json (4 seeds)
10	  - alpha=1.0 consensus loads existing method_ablation.json
11	  - Single-seed alpha points: seed_threshold=1, method agreement only
12	
13	Dependencies: numpy, scipy, statsmodels
14	"""
15	
16	import argparse
17	import glob
18	import json
19	import os
20	import re
21	import sys
22	import warnings
23	from datetime import datetime
24	
25	import numpy as np
26	from statsmodels.stats.multitest import multipletests
27	
28	warnings.filterwarnings("ignore")
29	
30	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
31	sys.path.insert(0, BASE_DIR)
32	
33	from method_ablation import (
34	    CANARY, DOWNSTREAM,
35	    extract as ma_extract,
36	    naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto, perm_granger,
37	)
38	from consensus_framework import classify_robust, load_sig_matrix, NumpyEncoder
39	
40	SWEEP_DIR = os.path.join(BASE_DIR, "results", "alpha_sweep")
41	MVP_DIR = os.path.join(BASE_DIR, "results", "mvp")
42	ANALYSIS_DIR = os.path.join(BASE_DIR, "results", "analysis")
43	
44	METRICS = ["distinct_1", "distinct_2", "distinct_3", "token_entropy", "ece", "perplexity"]
45	
46	GRANGER_PAIRS = [
47	    ("token_entropy", "distinct_1", "entropy->d1"),
48	    ("ece",           "distinct_1", "ECE->d1"),
49	    ("token_entropy", "distinct_2", "entropy->d2"),
50	    ("ece",           "distinct_2", "ECE->d2"),
51	    ("distinct_1", "token_entropy", "d1->entropy"),
52	    ("distinct_1", "ece",           "d1->ECE"),
53	    ("distinct_2", "token_entropy", "d2->entropy"),
54	    ("distinct_2", "ece",           "d2->ECE"),
55	]
56	
57	XCORR_PAIRS = [
58	    ("token_entropy", "distinct_1", 
…[truncated 36084 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T21:27:49.833485+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'gen_wiki_gpt2m_a100_s42_v4'}",
  "project": "distrib_canary_collapse",
  "fields": "['*']",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'gen_wiki_gpt2m_a100_s42_v4'}",
    "project": "distrib_canary_collapse",
    "fields": "['*']",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T21:27:49.833616+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1944}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T21:27:49.833767+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"method_ablation.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"method_ablation.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T21:27:49.833900+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T21:27:49.834011+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/generalize/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/generalize/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-18T21:27:49.834120+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "distrib_canary_collapse",
  "fields": "['*']",
  "limit": "57"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "fields": "['*']",
    "limit": "57"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-18T21:27:49.834234+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"gpt2m_wiki_a100_s43\\ngpt2m_wiki_a100_s43_bf16\\nopt13b_wiki_a100_s43_bf16\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T21:27:49.834729+00:00_

Error: result (105,234 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/6c5856df-7e7e-4732-a15b-77014fe6cce0/tool-results/mcp-agent-ml-research-read_registry-1779139028668.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/6c5856df-7e7e-4732-a15b-77014fe6cce0/tool-results/mcp-agent-ml-research-read_registry-1779139028668.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-18T21:27:49.834914+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/6c5856df-7e7e-4732-a15b-77014fe6cce0/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779139028668.txt') as f:\n    data = json.loads(json.loads(f.read())['result'])\nexps = data['data']['experiments']\n# Find s42 gpt2m entries\nfor k, v in exps.items():\n    if 'gpt2m' in k.lower():\n        print(f'=== {k} ===')\n        print(json.dumps(v, indent=2)[:3000])\n        print()\n\"\n",
  "description": "Search registry for GPT-2m experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/6c5856df-7e7e-4732-a15b-77014fe6cce0/tool-results && python3 -c \"\nimport json\nwith open('mcp-agent-ml-research-read_registry-1779139028668.txt') as f:\n    data = json.loads(json.loads(f.read())['result'])\nexps = data['data']['experiments']\n# Find s42 gpt2m entries\nfor k, v in exps.items():\n    if 'gpt2m' in k.lower():\n        print(f'=== {k} ===')\n        print(json.dumps(v, indent=2)[:3000])\n        print()\n\"\n",
    "description": "Search registry for GPT-2m experiments"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T21:27:49.835147+00:00_

=== gen_gpt2m_a100_s43_bf16 ===
{
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-18T17:25:55.336Z",
  "updated_at": "2026-05-18T21:14:52.266Z",
  "spec": {
    "command": "python -u iterative_train.py --model_name openai-community/gpt2-medium --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 1.0 --bf16 --output_dir results/generalize/gpt2m_wiki_a100_s43_bf16",
    "server": "westd-17855",
    "gpu": [
      "cuda:1"
    ],
    "pid": "16116",
    "log_path": "~/runs/distrib_canary_collapse/gen_gpt2m_a100_s43_bf16.log",
    "submitted_at": "2026-05-18T17:25:55.193Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "model_name": "openai-community/gpt2-medium",
    "seed": 43,
    "data_path": "data/wikitext103_5k",
    "data_count": 5000,
    "wall_clock_seconds": 12444.6,
    "gpu_hours": 3.46,
    "checkpoint_path": "results/generalize/gpt2m_wiki_a100_s43_bf16"
  },
  "hypothesis": "GPT-2-medium multi-seed s43: GPT-2-medium \u00d7 WikiText-103 \u00d7 \u03b1=1.0 \u00d7 seed=43. Validates s42 cross-architecture results (K\u22654=6/8) are reproducible.",
  "reproduce": {
    "finished_at": "2026-05-18T20:53:18.007Z"
  },
  "failure_reason": "EXIT_CODE=129 (non-zero)",
  "conclusion": "success",
  "completed_at": "2026-05-18T20:53:19.746Z",
  "extra": {
    "hook_events": [
      {
        "event": "on_failed",
        "action": "agent",
        "ts": "2026-05-18T20:53:22.622800+00:00"
      }
    ]
  }
}

=== gen_gpt2m_a100_s43 ===
{
  "status": "PREPARING",
  "retry_count": 0,
  "created_at": "2026-05-18T16:58:48.288Z",
  "updated_at": "2026-05-18T17:22:47.135Z",
  "spec": {
    "command": "bash -c \"cd /root/autodl-tmp/distrib_canary_collapse && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_DISABLE_XET=1 && export HF_ENDPOINT=https://hf-mirror.com && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICE
…[truncated 10226 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T21:27:49.835312+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Find Table 7 format",
  "subagent_type": "Explore",
  "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse, find the definition/template for \"Table 7\" in the paper. Check docs/paper/*.tex files and any artifact files. I need to know the exact columns and format of Table 7. Search for \"Table 7\", \"table7\", \"cross-architecture\", \"generalize\" in tex files. Report what columns Table 7 has and what format each row should be in."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Agent",
  "tool_args": {
    "description": "Find Table 7 format",
    "subagent_type": "Explore",
    "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse, find the definition/template for \"Table 7\" in the paper. Check docs/paper/*.tex files and any artifact files. I need to know the exact columns and format of Table 7. Search for \"Table 7\", \"table7\", \"cross-architecture\", \"generalize\" in tex files. Report what columns Table 7 has and what format each row should be in."
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-18T21:27:49.835472+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.tex\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.tex\" 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-18T21:27:49.835597+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/single_method_errors.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/discussion.
…[truncated 262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-18T21:27:49.835736+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Table\\s+7|table7|cross-architecture|generalize",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "type": "tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Table\\s+7|table7|cross-architecture|generalize",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
    "type": "tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-18T21:27:49.835850+00:00_

Found 5 files
docs/paper/limitations.tex
docs/paper/discussion.tex
docs/paper/introduction.tex
docs/paper/experiments.tex
docs/paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-18T21:27:49.835990+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Table\\s+7|table7|cross-architecture|generalize",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts",
  "type": "tex",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Table\\s+7|table7|cross-architecture|generalize",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts",
    "type": "tex",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-18T21:27:49.836114+00:00_

Found 1 file
artifacts/_project/paper/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-18T21:27:49.836231+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Table 7",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Table 7",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
    "type": "tex",
    "output_mode": "content",
    "context": "5"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-18T21:27:49.836359+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-18T21:27:49.836482+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\begin\\{table\\}|\\\\begin\\{tabular\\}|\\\\label\\{table:7\\}|\\\\label\\{table:seven\\}|cross-architecture",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
  "output_mode": "content",
  "context": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\begin\\{table\\}|\\\\begin\\{tabular\\}|\\\\label\\{table:7\\}|\\\\label\\{table:seven\\}|cross-architecture",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
    "output_mode": "content",
    "context": "3"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-18T21:27:49.836620+00:00_

27-Cross-correlation analysis uses a maximum lag of 5 generations.
28-Table~\ref{tab:drift_summary} summarizes raw metric drift from generation~0 to generation~10 across all six contamination levels.
29-
30:\begin{table}[t]
31-\centering
32-\small
33-[Omitted long context line]
34-\label{tab:drift_summary}
35:\begin{tabular}{lccccc}
36-\toprule
37-$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
38-\midrule
--
101-\label{fig:consensus_heatmap}
102-\end{figure}
103-
104:\begin{table}[t]
105-\centering
106-\small
107-[Omitted long context line]
108-\label{tab:method_comparison}
109:\begin{tabular}{lcccccc}
110-\toprule
111-Method & $\alpha{=}0.0$ & $\alpha{=}0.25$ & $\alpha{=}0.50$ & $\alpha{=}0.75$ & $\alpha{=}1.0$ & FPR$_\text{null}$ \\
112-\midrule
--
156-Table~\ref{tab:cross_arch_regime} summarizes the regime map across both architectures.
157-At $\alpha{=}0.25$, GPT-2-medium yields 1/8 pairs at Tier~3 ($K{\geq}4/5$) and 7/8 at Tier~2 ($K{\geq}3/5$), consistent with Pythia's 0/8 Tier~3, 0/8 Tier~2 result at the same contamination level, placing both architectures in the null/low-detectability regime.
158-
159:\begin{table}[t]
160-\centering
161-\small
162-\caption{Cross-architecture regime map: lead-lag consensus tier and metric drift at $\alpha{=}0.25$ and $\alpha{=}1.0$. Tier~3: $K{\geq}4/5$ methods; Tier~2: $K{\geq}3/5$. Drift is generation~0$\to$10. GPT-2-medium $\alpha{=}0.25$: single seed (seed=42); Pythia $\alpha{=}0.25$: 3-seed mean${\pm}$std. The onset boundary ($\alpha{\approx}0.25$--$0.50$) is consistent across two transformer decoder-only model families of similar scale.}
163-\label{tab:cross_arch_regime}
164:\begin{tabular}{llcccccc}
165-\toprule
166-$\alpha$ & Model & Entropy & ECE & Distinct-1 & Distinct-2 & Perm.\ Granger & Tier~3 \\
167-\midrule
--
190-We scope this claim precisely: canary metrics predict \emph{diversity collapse} (declining distinct-$n$), not model collapse broadly.
191-
192-\paragraph{Full synthetic replacement
…[truncated 3971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-18T21:27:49.836806+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-18T21:27:49.837039+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \cite{biderman2023pythia}, a 410M-parameter decoder-only language model.
8	Pythia provides a controlled setting: small enough for multi-seed experiments across six contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.
9	Cross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \S\ref{sec:method_sensitivity}, \S\ref{sec:regime}, and \S\ref{sec:discussion}.
10	Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
11	
12	Our protocol follows the replace paradigm of \citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\alpha{<}1.0$.
13	Each generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.
14	We run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\alpha \in \{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\}$.
15	The $\alpha{=}1.0$ condition uses four random seeds $\{42, 43, 44, 45\}$; $\alpha \in \{0.00, 0.25, 0.50, 0.75\}$ each use three seeds $\{42, 43, 44\}$; $\alpha{=}0.10$ uses a single seed (42, preliminary).
16	
17	We track two \emph{canary metrics} (cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical s
…[truncated 39105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-18T21:27:49.837198+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts -name \"*generalization*\" -o -name \"*table7*\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts -name \"*generalization*\" -o -name \"*table7*\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-18T21:27:49.837355+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/generalization_draft.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/intermediate/generalization_prep.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/generalization_prep.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/gen_wiki_gpt2m_a100_s42_v4/report/gpt2m_wiki_8pair_table7_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/generalization_draft.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-18T21:27:49.837489+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/generalization_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/generalization_draft.tex"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-18T21:27:49.837656+00:00_

1	% ============================================================
2	% generalization_draft.tex
3	% Pre-drafted paragraphs and table structure for §5.5
4	% (Cross-Architecture and Cross-Domain Generalization)
5	%
6	% STATUS: Draft with placeholders. Awaiting Phase 2 results.
7	%
8	% PLACEHOLDERS:
9	%   \textbf{XX}  — numeric value to fill from experiment
10	%   \textbf{[TBD]}  — entire row/cell pending experiment completion
11	%   VERSION A / VERSION B — pick one after results are in
12	%
13	% USAGE: Copy relevant pieces into docs/paper/experiments.tex §5.5
14	%        after results arrive. Do NOT edit this file as ground truth.
15	% ============================================================
16	
17	
18	% ============================================================
19	% TABLE: Generalization summary (replaces skeleton in experiments.tex)
20	% ============================================================
21	
22	\begin{table}[t]
23	\centering
24	\small
25	\caption{Generalization of lead-lag detectability across model scale,
26	architecture family, and training domain ($\alpha{=}1.0$, single seed
27	per condition). Each cell reports the fraction of 8 canary$\to$downstream
28	pairs (token entropy and ECE $\times$ 4 downstream metrics) reaching
29	BH-corrected FDR significance ($q{=}0.05$). Direction asymmetry shows
30	forward vs.\ reverse permutation Granger significance. The baseline row
31	reproduces the single-seed Pythia-410M result for comparison; 4-seed
32	pooled rates are reported in Table~\ref{tab:method_comparison}.
33	``Key canary'' identifies the metric with the strongest consensus
34	signal in each condition.}
35	\label{tab:generalization}
36	\begin{tabular}{llcccccc}
37	\toprule
38	Variation & Model / Dataset
39	  & \rotatebox{70}{Naive XCorr}
40	  & \rotatebox{70}{Diff.\ XCorr}
41	  & \rotatebox{70}{Threshold}
42	  & \rotatebox{70}{PermG (fwd/rev)}
43	  & \rotatebox{70}{TY}
44	  & \rotatebox{70}{$K{\geq}4/5$} \\
45	\midrule
46	Baseline
47	  & Pythia-410M / W
…[truncated 13150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-18T21:27:49.837808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/gen_wiki_gpt2m_a100_s42_v4/report/gpt2m_wiki_8pair_table7_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/gen_wiki_gpt2m_a100_s42_v4/report/gpt2m_wiki_8pair_table7_report.md"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-18T21:27:49.837936+00:00_

1	# GPT-2-medium WikiText-103 8-Pair Table 7 Analysis
2	
3	**Experiment**: gen_wiki_gpt2m_a100_s42_v4
4	**Model**: gpt2-medium (355M)
5	**Dataset**: wikitext103_5k, alpha=1.0, seed=42
6	**Generations**: 11 (gen0-gen10), 5000 steps/gen
7	**Parameters**: n_perm=5000, xcorr_lag=5, granger_lag=1
8	
9	## Table 7 Row
10	
11	| Naive | Diff | Thresh | PG_fwd | PG_rev | TY | K>=4 |
12	|-------|------|--------|--------|--------|-----|------|
13	| 8/8 | 8/8 | 8/8 | 6/8 | 3/8 | 5/8 | 6/8 |
14	
15	## Per-Pair Detail
16	
17	| Pair | Naive | Diff(FDR) | Thresh | TY | PG_fwd | PG_rev | K |
18	|------|-------|-----------|--------|-----|--------|--------|---|
19	| ent->ppl | Y (p=0.0199) | Y (q=0.0016) | Y (L=7) | N (p=0.9998) | N (p=0.4989) | N (p=0.1820) | 3/5 |
20	| ent->d1 | Y (p=0.0000) | Y (q=0.0000) | Y (L=2) | N (p=0.1160) | Y (p=0.0006) | N (p=0.0964) | 4/5 |
21	| ent->d2 | Y (p=0.0000) | Y (q=0.0000) | Y (L=2) | Y (p=0.0017) | Y (p=0.0020) | N (p=0.1052) | 5/5 |
22	| ent->d3 | Y (p=0.0000) | Y (q=0.0000) | Y (L=2) | Y (p=0.0000) | Y (p=0.0024) | N (p=0.1062) | 5/5 |
23	| ece->ppl | Y (p=0.0076) | Y (q=0.0029) | Y (L=6) | N (p=0.2254) | N (p=0.8796) | N (p=0.6107) | 3/5 |
24	| ece->d1 | Y (p=0.0000) | Y (q=0.0007) | Y (L=1) | Y (p=0.0000) | Y (p=0.0006) | Y (p=0.0032) | 5/5 |
25	| ece->d2 | Y (p=0.0000) | Y (q=0.0000) | Y (L=1) | Y (p=0.0000) | Y (p=0.0010) | Y (p=0.0160) | 5/5 |
26	| ece->d3 | Y (p=0.0000) | Y (q=0.0000) | Y (L=1) | Y (p=0.0000) | Y (p=0.0010) | Y (p=0.0084) | 5/5 |
27	
28	## Drift Analysis (gen0 -> gen10)
29	
30	| Metric | Gen0 | Gen10 | Change% |
31	|--------|------|-------|---------|
32	| token_entropy | 3.5714 | 0.4794 | -86.6% |
33	| ece | 0.0112 | 0.5216 | +4571.9% |
34	| perplexity | 32.63 | 16520.55 | +50527.6% |
35	| distinct_1 | 0.1044 | 0.0918 | -12.1% |
36	| distinct_2 | 0.5483 | 0.4717 | -14.0% |
37	| distinct_3 | 0.8441 | 0.7394 | -12.4% |
38	| self_bleu | 0.0094 | 0.0119 | +25.9% |
39	| effective_rank | 2.3722 | 25.0018 | +953.9% |
40	| mauve
…[truncated 1736 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-18T21:27:49.838123+00:00_

Perfect! Now I have a complete picture of Table 7. Let me provide a comprehensive report.

## Summary: Table 7 Definition and Format

**Table 7 Title**: "Generalization of lead-lag detectability across architecture, scale, and domain"

**Location**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex` (lines 342-365)

### Table 7 Exact Columns:

The table has **9 columns**:

1. **Variation** - Row category (Baseline, Architecture, Scale, Domain)
2. **Model / Dataset** - Specific model name and training dataset (e.g., "Pythia-410M / Wiki", "GPT-2-medium / Wiki", "OPT-1.3B / Wiki", "Pythia-1.4B / Wiki", "Pythia-1B / C4")
3. **Naive** - Naive cross-correlation significance (fraction out of 8 pairs)
4. **Diff. XCorr** - Differenced cross-correlation FDR significance (fraction out of 8)
5. **Threshold** - Threshold onset detection significance (fraction out of 8)
6. **PermG (fwd)** - Permutation Granger forward direction significance (fraction out of 8)
7. **PermG (rev)** - Permutation Granger reverse direction significance (fraction out of 8)
8. **TY** - Toda-Yamamoto Granger significance (fraction out of 8)
9. **$K{\geq}4/5$** - Consensus threshold (K≥4/5 methods) significance (fraction out of 8)

### Row Format:

Each row contains:
- **Variation type** (Architecture | Scale | Domain)
- **Model/Dataset combination**
- **8 numeric cells** in format: **X/8** representing "number of 8 canary→downstream pairs" reaching BH-corrected FDR significance at q=0.05

### Key Details:

**Row Structure** (from the actual data in experiments.tex lines 352-360):
- Baseline: Pythia-410M / Wiki
- Architecture: GPT-2-medium / Wiki, OPT-1.3B / Wiki  
- Scale: Pythia-1.4B / Wiki (two seeds: s42, s43)
- Domain: Pythia-1B / C4 (two seeds: s42, s43)

**Data Format Per Cell**: Each cell reports the count of canary→downstream pairs (out of 8 total pairs: 2 canaries × 4 downstream metrics) that reach BH-corrected FDR significance (q=0.05).
…[truncated 1100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Agent",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-18T21:27:49.838324+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
  "offset": "330",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex",
    "offset": "330",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-18T21:27:49.838493+00:00_

330	\bottomrule
331	\end{tabular}
332	\end{table}
333	
334	
335	\subsection{Cross-Architecture, Cross-Scale, and Cross-Domain Generalization}
336	\label{sec:generalization}
337	
338	The methodological pitfalls and consensus framework developed above are calibrated on a single model family (Pythia-410M, WikiText-103).
339	To test whether these findings transfer, we evaluate the consensus pipeline along three generalization axes: architecture family (GPT-2-medium 345M, OPT-1.3B), model scale (Pythia-1.4B, $3.4\times$ parameters within the same family), and training domain (Pythia-1B trained on C4 rather than WikiText-103).
340	All conditions use $\alpha{=}1.0$; architecture conditions use a single seed, while scale and domain conditions use two seeds (s42, s43) to assess replicability.
341	
342	\begin{table}[t]
343	\centering
344	\small
345	\caption{Generalization of lead-lag detectability across architecture, scale, and domain ($\alpha{=}1.0$, $n_{\text{perm}}{=}5{,}000$). Each cell reports the fraction of 8~canary$\to$downstream pairs per condition reaching BH-corrected FDR significance ($q{=}0.05$), with two seeds (s42, s43) to assess replicability for scale and domain conditions. MMCT: weighted forward consensus (\S\ref{sec:mmct}).}
346	\label{tab:generalization}
347	\resizebox{\columnwidth}{!}{%
348	\begin{tabular}{llcccccccc}
349	\toprule
350	Variation & Model / Dataset & \rotatebox{70}{Naive} & \rotatebox{70}{Diff.\ XCorr} & \rotatebox{70}{Threshold} & \rotatebox{70}{PermG (fwd)} & \rotatebox{70}{PermG (rev)} & \rotatebox{70}{TY} & \rotatebox{70}{$K{\geq}4/5$} & \rotatebox{70}{MMCT} \\
351	\midrule
352	Baseline & Pythia-410M / Wiki & 8/8 & 8/8 & 8/8 & 6/8 & 3/8 & 4/8 & 6/8 & 5/8 \\
353	Architecture & GPT-2-medium / Wiki & 8/8 & 8/8 & 8/8 & 6/8 & 3/8 & 5/8 & 6/8 & \textbf{8/8} \\
354	Architecture & OPT-1.3B / Wiki & 8/8 & 6/8 & 8/8 & 6/8 & 2/8 & 6/8 & 6/8 & 5/8 \\
355	Scale ($3.4\times$) & Pythia-1.4B / Wiki (s42) & 7/8 & 6/8 & 8/8 & 5/8 & 0/8 & 0/8 & 5/8 & 4/8 
…[truncated 3997 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-18T21:27:49.838639+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "python3 -c \"import numpy, scipy, statsmodels; print('numpy', numpy.__version__); print('scipy', scipy.__version__); print('statsmodels', statsmodels.__version__)\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "python3 -c \"import numpy, scipy, statsmodels; print('numpy', numpy.__version__); print('scipy', scipy.__version__); print('statsmodels', statsmodels.__version__)\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-18T21:27:49.838761+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-18T21:27:49.838899+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "python3 -c \"import numpy; print('numpy', numpy.__version__)\" && python3 -c \"import scipy; print('scipy', scipy.__version__)\" && python3 -c \"import statsmodels; print('statsmodels', statsmodels.__version__)\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "python3 -c \"import numpy; print('numpy', numpy.__version__)\" && python3 -c \"import scipy; print('scipy', scipy.__version__)\" && python3 -c \"import statsmodels; print('statsmodels', statsmodels.__version__)\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-18T21:27:49.839025+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'python3 -c \\\"import numpy; print(\\\\'numpy\\\\', numpy.__version__)\\\" && python3 -c \\\"import scipy; print(\\\\'scipy\\\\', scipy.__version__)\\\" && python3 -c \\\"import statsmodels; print(\\\\'statsmodels\\\\', statsmodels.__version__)\\\"'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-18T21:27:49.839143+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"import numpy; print('numpy', numpy.__version__)\" && python -c \"import scipy; print('scipy', scipy.__version__)\" && python -c \"import statsmodels; print('statsmodels', statsmodels.__version__)\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"import numpy; print('numpy', numpy.__version__)\" && python -c \"import scipy; print('scipy', scipy.__version__)\" && python -c \"import statsmodels; print('statsmodels', statsmodels.__version__)\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-18T21:27:49.839282+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"numpy 2.3.2\\nscipy 1.17.1\\nstatsmodels 0.14.6\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-18T21:27:49.839426+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/analysis/detrending_utils.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/analysis/detrending_utils.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-18T21:27:49.839638+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Detrending utilities for canary→downstream lead-lag validation.\\n\\nProvides first-differencing and HP filter detrending, plus detrended\\ncross-correlation to verify lead-lag relationships survive trend removal\\n(Dream D014 reviewer concern: ruling out spurious correlation from\\nshared monotonic trends).\\n\\nInput:  all_metrics.json — list of dicts, one per generation.\\nOutput: JSON comparing raw vs. detrended cross-correlation per pair.\\n\\nDependencies: numpy, scipy, statsmodels\\n\\\"\\\"\\\"\\n\\nimport json\\nimport argparse\\nimport os\\nfrom pathlib import Path\\nfrom typing import Literal\\n\\nimport numpy as np\\nfrom statsmodels.tsa.filters.hp_filter import hpfilter\\n\\n\\nCANARY_METRICS = [\\\"token_entropy\\\", \\\"ece\\\"]\\nDOWNSTREAM_METRICS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"perplexity\\\"]\\n\\nHIGHER_IS_WORSE = {\\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\n\\ndef first_difference(series: np.ndarray) -> np.ndarray:\\n    \\\"\\\"\\\"First differences: y[t] - y[t-1].\\n\\n    Args:\\n        series: Time series of shape (T,).\\n\\n    Returns:\\n        Differenced series of shape (T-1,).\\n    \\\"\\\"\\\"\\n    return np.diff(series)\\n\\n\\ndef hp_filter(series: np.ndarray, lamb: float = 6.25) -> tuple[np.ndarray, np.ndarray]:\\n    \\\"\\\"\\\"Hodrick-Prescott filter decomposition.\\n\\n    Args:\\n        series: Time series of shape (T,).\\n        lamb: Smoothing parameter. 6.25 is Ravn-Uhlig for annual data.\\n              With T~10, results are sensitive to lambda choice; consider\\n              values in [1, 10] and check robustness.\\n\\n    Returns:\\n        (trend, cycle) tuple, both of shape (T,).\\n    \\\"\\\"\\\"\\n    cycle, trend = hpfilter(series, lamb=lamb)\\n    return np.asarray(trend), np.asarray(cycle)\\n\\n\\ndef _normali
…[truncated 6977 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-18T21:27:49.839784+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"lead_lag*\" -o -name \"method_ablation*\" -o -name \"run_analysis*\" -o -name \"mmct*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"lead_lag*\" -o -name \"method_ablation*\" -o -name \"run_analysis*\" -o -name \"mmct*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-18T21:27:49.839919+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/mmct\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-18T21:27:49.840062+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/mmct -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/mmct -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-18T21:27:49.840189+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/mmct/__init__.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/methods.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/null_distribution.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/consensus_test.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/run_mmct.py\\n/root/autodl-tmp/distrib_canary_collapse/mmct/__pycache__/__init__.cpython-312.pyc\\n/root/autodl-tmp/distrib_canary_collapse/mmct/__pycache__/consensus_test.cpython-312.pyc\\n/root/autodl-tmp/distrib_canary_collapse/mmct/__pycache__/methods.cpython-312.pyc\\n/root/autodl-tmp/distrib_canary_collapse/mmct/__pycache__/null_distribution.cpython-312.pyc\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-18T21:27:49.840327+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"gen_analysis*.py\" -o -name \"run_gen*.py\" -o -name \"generalize*.py\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"gen_analysis*.py\" -o -name \"run_gen*.py\" -o -name \"generalize*.py\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-18T21:27:49.840446+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-18T21:27:49.840584+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/mmct/run_mmct.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/mmct/run_mmct.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-18T21:27:49.840855+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Run MMCT across all available alpha-sweep conditions.\\n\\nScans results/alpha_sweep/ for conditions with 5method_leadlag.json,\\nruns MMCT in 4 modes (uniform/weighted x forward/bidirectional),\\noutputs JSON results and markdown reports.\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\nimport sys\\nfrom datetime import datetime\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/distrib_canary_collapse\\\")\\n\\nfrom mmct.methods import METRIC_PAIRS, METHOD_NAMES\\nfrom mmct.null_distribution import NullDistribution\\nfrom mmct.consensus_test import MMCT\\n\\nBASE_DIR = \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep\\\"\\nOUTPUT_DIR = \\\"/root/autodl-tmp/distrib_canary_collapse/artifacts/mmct_results\\\"\\n\\nNULL_DIRS = [\\n    os.path.join(BASE_DIR, \\\"a000_s42\\\"),\\n    os.path.join(BASE_DIR, \\\"a000_s43\\\"),\\n    os.path.join(BASE_DIR, \\\"a000_s44\\\"),\\n]\\n\\nMODES = [\\n    {\\\"weighted\\\": False, \\\"bidirectional\\\": False, \\\"name\\\": \\\"uniform_forward\\\"},\\n    {\\\"weighted\\\": False, \\\"bidirectional\\\": True,  \\\"name\\\": \\\"uniform_bidirectional\\\"},\\n    {\\\"weighted\\\": True,  \\\"bidirectional\\\": False, \\\"name\\\": \\\"weighted_forward\\\"},\\n    {\\\"weighted\\\": True,  \\\"bidirectional\\\": True,  \\\"name\\\": \\\"weighted_bidirectional\\\"},\\n]\\n\\n\\ndef discover_conditions():\\n    \\\"\\\"\\\"Scan alpha_sweep directory for conditions with 5method analysis.\\\"\\\"\\\"\\n    conditions = {}\\n    for entry in sorted(os.listdir(BASE_DIR)):\\n        if not entry.startswith(\\\"a\\\") or \\\"_s\\\" not in entry:\\n            continue\\n        analysis = os.path.join(BASE_DIR, entry, \\\"analysis\\\",\\n                                \\\"5method_leadlag.json\\\")\\n        if not os.path.exists(analysis):\\n            continue\\n        parts = entry.split(\\\"_\\\")\\n        alpha_str = parts[0]\\n        seed = int(parts[1][1
…[truncated 7584 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-18T21:27:49.841010+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/mmct/methods.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/mmct/methods.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-18T21:27:49.841172+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Unified wrapper for 5 lead-lag detection methods.\\n\\nReads pre-computed results from 5method_leadlag.json rather than\\nre-running statistical tests. Handles two JSON layouts:\\n  Format A (a000): pair has top-level canary/downstream + forward/reverse dicts\\n  Format B (a025+): pair has forward/reverse dicts with canary/downstream inside\\n\\\"\\\"\\\"\\n\\nimport json\\nfrom pathlib import Path\\n\\nMETHOD_NAMES = [\\\"naive_xcorr\\\", \\\"diff_xcorr\\\", \\\"threshold_onset\\\",\\n                \\\"perm_granger\\\", \\\"ty_granger\\\"]\\n\\nCANARY_METRICS = [\\\"token_entropy\\\", \\\"ece\\\"]\\nDOWNSTREAM_METRICS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"perplexity\\\"]\\n\\nMETRIC_PAIRS = [(c, d) for c in CANARY_METRICS for d in DOWNSTREAM_METRICS]\\n\\n\\ndef load_5method_results(data_dir):\\n    \\\"\\\"\\\"Load pre-computed 5-method lead-lag results for one condition.\\\"\\\"\\\"\\n    path = Path(data_dir) / \\\"analysis\\\" / \\\"5method_leadlag.json\\\"\\n    with open(path) as f:\\n        return json.load(f)\\n\\n\\ndef _find_pair(results, canary, downstream):\\n    \\\"\\\"\\\"Find the pair dict, handling both JSON formats.\\\"\\\"\\\"\\n    for pair in results[\\\"pairs\\\"]:\\n        # Format A: canary/downstream at pair level\\n        if pair.get(\\\"canary\\\") == canary and pair.get(\\\"downstream\\\") == downstream:\\n            return pair\\n        # Format B: canary/downstream inside forward\\n        fwd = pair.get(\\\"forward\\\", {})\\n        if fwd.get(\\\"canary\\\") == canary and fwd.get(\\\"downstream\\\") == downstream:\\n            return pair\\n    return None\\n\\n\\ndef extract_method_significance(results, canary, downstream,\\n                                 direction=\\\"forward\\\"):\\n    \\\"\\\"\\\"Extract per-method significance for one pair.\\n\\n    Returns dict mapping method name to bool (significant or not).\\n    \\\"
…[truncated 947 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-18T21:27:49.841336+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/mmct/consensus_test.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/mmct/consensus_test.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-18T21:27:49.841508+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Multi-Method Consensus Test (MMCT) core implementation.\\n\\nSingle methods have uncontrolled FPR on short time series (T~11).\\nMMCT aggregates K=5 methods into a consensus score calibrated against\\nalpha=0.00 null data to control false positive rate.\\n\\nModes:\\n  - uniform: consensus = count of significant methods\\n  - weighted: consensus = inverse-FPR-weighted sum (down-weights noisy methods)\\n  - forward-only: test canary -> downstream direction only\\n  - bidirectional: require forward significant AND reverse non-significant\\n\\\"\\\"\\\"\\n\\nfrom dataclasses import dataclass, field, asdict\\nfrom typing import Optional\\n\\nfrom .methods import METHOD_NAMES, extract_method_significance, load_5method_results\\nfrom .null_distribution import NullDistribution\\n\\n\\n@dataclass\\nclass MMCTResult:\\n    canary: str\\n    downstream: str\\n    consensus_score: float\\n    p_value: float\\n    ci_lower: float\\n    ci_upper: float\\n    method_results: dict\\n    significant: bool\\n    alpha: float = 0.05\\n    mode: str = \\\"uniform_forward\\\"\\n    weights: Optional[dict] = None\\n    reverse_p_value: Optional[float] = None\\n    reverse_consensus_score: Optional[float] = None\\n    reverse_method_results: Optional[dict] = None\\n\\n    def to_dict(self):\\n        d = asdict(self)\\n        if d[\\\"weights\\\"]:\\n            d[\\\"weights\\\"] = {k: round(v, 4) for k, v in d[\\\"weights\\\"].items()}\\n        return d\\n\\n\\nclass MMCT:\\n    \\\"\\\"\\\"Multi-Method Consensus Test.\\\"\\\"\\\"\\n\\n    def __init__(self, null_distribution, weighted=False,\\n                 bidirectional=False, alpha=0.05):\\n        self.null = null_distribution\\n        self.weighted = weighted\\n        self.bidirectional = bidirectional\\n        self.alpha = alpha\\n\\n    @property\\n    def mode_name(self):\\n        w = \\\"weighted\\\" if self.weighted else \\\"uniform\\\"\\n        d =
…[truncated 2770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-18T21:27:49.841664+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/mmct/null_distribution.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/mmct/null_distribution.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-18T21:27:49.841861+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Null distribution construction from alpha=0.00 data.\\n\\nUses alpha=0.00 runs (no synthetic contamination) to build the empirical\\ndistribution of consensus scores under H0. Supports both uniform and\\nweighted consensus modes. Per-method FPR profiles are computed for\\ninverse-FPR weighting.\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\nfrom pathlib import Path\\n\\nfrom .methods import (METHOD_NAMES, METRIC_PAIRS, load_5method_results,\\n                      extract_method_significance)\\n\\n\\nclass NullDistribution:\\n    \\\"\\\"\\\"Empirical null distribution for MMCT consensus scores.\\\"\\\"\\\"\\n\\n    def __init__(self, null_dirs, n_bootstrap=10000, seed=42):\\n        \\\"\\\"\\\"\\n        Args:\\n            null_dirs: list of paths to alpha=0.00 experiment directories\\n            n_bootstrap: bootstrap resamples for p-value CI\\n            seed: random seed for reproducibility\\n        \\\"\\\"\\\"\\n        self.null_dirs = null_dirs\\n        self.n_bootstrap = n_bootstrap\\n        self.seed = seed\\n\\n        self._per_pair_sigs = {}\\n        self._load_null_data()\\n        self._compute_fpr_profile()\\n        self._build_distributions()\\n\\n    def _load_null_data(self):\\n        for d in self.null_dirs:\\n            results = load_5method_results(d)\\n            for canary, downstream in METRIC_PAIRS:\\n                key = (canary, downstream)\\n                if key not in self._per_pair_sigs:\\n                    self._per_pair_sigs[key] = {\\\"forward\\\": [], \\\"reverse\\\": []}\\n\\n                fwd = extract_method_significance(\\n                    results, canary, downstream, \\\"forward\\\")\\n                rev = extract_method_significance(\\n                    results, canary, downstream, \\\"reverse\\\")\\n                self._per_pair_sigs[key][\\\"forward\\\"].append(fwd)\\n                self._per_pair_sigs[key][\\\"reverse\\\"].append(rev)
…[truncated 6125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-18T21:27:49.842010+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Find method_ablation.py",
  "subagent_type": "Explore",
  "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse, find the file \"method_ablation.py\" which contains the 5 statistical methods: naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto, perm_granger. Also look for any script that generates \"5method_leadlag.json\". Check in artifacts/, docs/, or any other directories. Also search for these function names to find where they're defined."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Agent",
  "tool_args": {
    "description": "Find method_ablation.py",
    "subagent_type": "Explore",
    "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse, find the file \"method_ablation.py\" which contains the 5 statistical methods: naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto, perm_granger. Also look for any script that generates \"5method_leadlag.json\". Check in artifacts/, docs/, or any other directories. Also search for these function names to find where they're defined."
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-18T21:27:49.842157+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"*.py\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-18T21:27:49.842295+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/figures/paper/gen_fig_differencing_dmax.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/plot_consensus_workflow.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/plot_regime_map.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/bootstrap_ty_validation.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_mvp.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/intermediate/iterative_train.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/cross_alpha_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/consensus_framework.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/permutation_granger.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures/plot_regime_map.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/metrics.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/test_alpha_sweep.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/iterative_train.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_extended.py
/home/ubuntu/.agent-ml-researc
…[truncated 301 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-18T21:27:49.842468+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"method_ablation.py\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"method_ablation.py\""
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-18T21:27:49.842602+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-18T21:27:49.842726+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"*5method*\" -o -name \"*leadlag*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"*5method*\" -o -name \"*leadlag*\""
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-18T21:27:49.842875+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_a050_s42_5method_urgent_20260516T203706.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_ssh_a100_5method_and_table_update_20260517T094159.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_plan006_20gen_leadlag_20260515T052204.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_gpt2m_metrics_and_leadlag_20260515T221815_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_ssh_a050_s44_5method_20260517T063654_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_c4_5method_full_20260517T173731.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_ssh_a050_s44_5method_20260517T063654.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_gpt2m_full_5method_leadlag_20260515T222426_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_a075_s44_5method_leadlag_20260516T141651_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_gpt2m_a025_5method_b3_20260516T083010_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_a075_s43_5method_leadlag_20260516T142157_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_gpt2m_full_5method_leadlag_20260515T222426.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_analysis_gpt2m_s43_bf16_lead
…[truncated 5163 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-18T21:27:49.843043+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "naive_pearson|diff_xcorr|threshold_lead|toda_yamamoto|perm_granger",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Grep",
  "tool_args": {
    "pattern": "naive_pearson|diff_xcorr|threshold_lead|toda_yamamoto|perm_granger",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-18T21:27:49.843199+00:00_

Found 250 files limit: 250
logs/workers/worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603.log
logs/workers/worker_analysis_a060_bf16_leadlag_20260518T211552.log
logs/chats/feishu_group_oc_1f489e32588225ae3672d716b94662a8_reviewer.jsonl
artifacts/manifest.yaml
logs/chats/feishu_group_oc_1f489e32588225ae3672d716b94662a8.jsonl
registry.yaml
logs/chats/feishu_group_oc_150c7ce908e05d7932315e0288cf5bfb_director.jsonl
experiment_plan.yaml
decisions.yaml
mistakes.yaml
logs/workers/worker_analyze_c4_a050_bf16_results_20260518T202848.log
memory.md
logs/chats/feishu_group_oc_1f489e32588225ae3672d716b94662a8_paper_agent.jsonl
logs/workers/worker_analyze_alpha_sweep_a010_s42_v2_20260518T193614.log
logs/workers/worker_analysis_mmct_unified_data_v4_20260518T161826.log
logs/workers/worker_infra_env_setup_westd17855_20260518T154535.log
logs/workers/worker_code_csmp_implementation_20260518T161544.log
logs/chats/worker_analysis_mmct_bugfix_expand_v3_20260518T155459.jsonl
logs/workers/worker_analysis_mmct_bugfix_expand_v3_20260518T155459.log
logs/workers/worker_analysis_mmct_alpha100_fix_20260518T155251.log
logs/workers/worker_code_mmct_implementation_v2_20260518T153850_result.json
logs/workers/worker_code_mmct_implementation_v2_20260518T153850.log
logs/workers/worker_analysis_intervention_reactive_s42_20260518T145214.log
logs/workers/worker_analysis_change_point_supplement_20260518T142018.log
logs/workers/worker_analysis_transfer_entropy_20260518T140339.log
logs/workers/worker_analysis_change_point_20260518T140428.log
logs/chats/worker_check_intervention_progress_20260518T131904.jsonl
logs/workers/worker_check_intervention_progress_20260518T131904.log
logs/workers/worker_analysis_gpt2m_v4_table7_20260518T113128.log
logs/workers/worker_analysis_gen_wiki_gpt2m_a100_s42_v4_20260518T113124.log
logs/chats/cron_hook_gen_wiki_gpt2m_a100_s42_v4.jsonl
logs/workers/worker_analysis_m004_persist_batch1_20260518T111739_result.json
logs/workers/worker_analysis_m004_persist_batch1_20260518T1117
…[truncated 15161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-18T21:27:49.843379+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "def (naive_pearson|diff_xcorr|threshold_lead|toda_yamamoto|perm_granger)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "type": "py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Grep",
  "tool_args": {
    "pattern": "def (naive_pearson|diff_xcorr|threshold_lead|toda_yamamoto|perm_granger)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
    "type": "py",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-18T21:27:49.843500+00:00_

Found 1 file
artifacts/analyze_extended.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-18T21:27:49.843622+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"*.py\" | xargs grep -l \"5method_leadlag.json\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"*.py\" | xargs grep -l \"5method_leadlag.json\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-18T21:27:49.843732+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-18T21:27:49.843847+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_extended.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_extended.py"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-18T21:27:49.844079+00:00_

1	# analyze_extended.py — Plan-006 extended 20-gen analysis
2	# Input:  results/extended_20gen/s{seed}/all_metrics.json
3	# Output: results/extended_20gen/analysis/{extended_analysis.json, summary.txt, mvp_comparison.json}
4	
5	import argparse
6	import json
7	import os
8	import sys
9	import warnings
10	from datetime import datetime
11	
12	import numpy as np
13	from scipy import stats
14	from statsmodels.stats.multitest import multipletests
15	from statsmodels.tsa.stattools import adfuller
16	
17	from permutation_granger import permutation_granger_test
18	from detrending_utils import detrend, cross_correlate, detrend_and_crosscorr
19	
20	warnings.filterwarnings("ignore")
21	
22	CANARY_METRICS = ["token_entropy", "ece"]
23	DOWNSTREAM_METRICS = ["distinct_1", "distinct_2", "distinct_3", "perplexity"]
24	HIGHER_IS_WORSE = {"self_bleu", "ece", "perplexity"}
25	LOWER_IS_WORSE = {"token_entropy", "effective_rank", "distinct_1", "distinct_2",
26	                   "distinct_3", "mauve"}
27	ALPHA_SIG = 0.05
28	N_PERM = 5000
29	
30	
31	# ── helpers ──────────────────────────────────────────────────────────────
32	
33	def load_metrics(path):
34	    """Load all_metrics.json, return sorted list of dicts."""
35	    with open(path) as f:
36	        data = json.load(f)
37	    return sorted(data, key=lambda m: m["generation"])
38	
39	
40	def extract(metrics_list, name):
41	    return np.array([m[name] for m in metrics_list])
42	
43	
44	def orient(series, name):
45	    return -series.copy() if name in LOWER_IS_WORSE else series.copy()
46	
47	
48	def cohen_r_label(r):
49	    r = abs(r)
50	    if r >= 0.5:   return "large"
51	    if r >= 0.3:   return "medium"
52	    if r >= 0.1:   return "small"
53	    return "negligible"
54	
55	
56	def cohen_f2_label(f2):
57	    if f2 is None: return "N/A"
58	    if f2 >= 0.35: return "large"
59	    if f2 >= 0.15: return "medium"
60	    if f2 >= 0.02: return "small"
61	    return "negligible"
62	
63	
64	def adf_order(series, max_d=2):
65	    for d in
…[truncated 22744 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-18T21:27:49.844235+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py"
  }
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-18T21:27:49.844407+00:00_

1	"""Generate Single-Method Error Consequence table from 5method_leadlag.json files."""
2	import json
3	import os
4	import glob
5	
6	BASE = "/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep"
7	
8	files = sorted(glob.glob(os.path.join(BASE, "a*_s*/analysis/5method_leadlag.json")))
9	
10	METHOD_KEYS = ["naive_xcorr", "diff_xcorr", "threshold_onset", "perm_granger", "ty_granger"]
11	METHOD_LABELS = {
12	    "naive_xcorr": "Naive XCorr",
13	    "diff_xcorr": "Diff XCorr (FDR)",
14	    "threshold_onset": "Threshold Onset",
15	    "perm_granger": "Perm Granger (FDR)",
16	    "ty_granger": "TY Granger",
17	}
18	
19	def get_sig(method_data, method_key):
20	    if method_key in ("diff_xcorr", "perm_granger"):
21	        return method_data.get("significant_fdr", method_data.get("significant", False))
22	    return method_data.get("significant", False)
23	
24	results = {}
25	data_sources = {}
26	
27	for f in files:
28	    with open(f) as fh:
29	        d = json.load(fh)
30	    if "meta" in d:
31	        alpha = d["meta"]["alpha"]
32	        seed = d["meta"]["seed"]
33	    else:
34	        alpha = d["alpha"]
35	        seed = d["seed"]
36	    alpha_str = f"a{int(alpha*100):03d}"
37	    key = (alpha_str, seed)
38	    data_sources[key] = f
39	
40	    method_sig = {m: 0 for m in METHOD_KEYS}
41	    n_pairs = len(d["pairs"])
42	
43	    for pair in d["pairs"]:
44	        fwd = pair["forward"]
45	        for m in METHOD_KEYS:
46	            if m in fwd and isinstance(fwd[m], dict) and get_sig(fwd[m], m):
47	                method_sig[m] += 1
48	
49	    results[key] = {"method_sig": method_sig, "n_pairs": n_pairs}
50	
51	ALPHAS = ["a000", "a025", "a050", "a075", "a100"]
52	ALPHA_LABELS = {"a000": "0.00", "a025": "0.25", "a050": "0.50", "a075": "0.75", "a100": "1.00"}
53	
54	print("=" * 80)
55	print("Per-seed, per-method forward significant pair counts (out of 8)")
56	print("=" * 80)
57	
58	for alpha in ALPHAS:
59	    seeds = sorted([k[1] for k in results if k[0] == alpha])
…[truncated 4095 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-18T21:27:49.844566+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"*.py\" | xargs grep -l \"5method_leadlag\\|naive_xcorr\\|diff_xcorr\\|threshold_onset\" 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"*.py\" | xargs grep -l \"5method_leadlag\\|naive_xcorr\\|diff_xcorr\\|threshold_onset\" 2>/dev/null | head -10"
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-18T21:27:49.844687+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/consensus_framework.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/cross_alpha/cross_alpha_analysis_v4.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/consensus_framework/consensus_framework.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/consensus_framework.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-18T21:27:49.844810+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/consensus_framework.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/consensus_framework.py"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-18T21:27:49.845020+00:00_

1	"""
2	Multi-method consensus framework for canary→downstream association robustness.
3	
4	Formalizes "robust association": a pair is robust only when ≥method_threshold
5	independent statistical methods agree (each requiring ≥seed_threshold seeds
6	significant). Two-stage aggregation: seed→method verdict, then method→consensus.
7	
8	Input:  results/mvp/analysis/method_ablation.json
9	Output: consensus classification, sensitivity heatmap, FPR/FNR table (JSON)
10	
11	Dependencies: numpy, json (stdlib)
12	"""
13	
14	import json
15	import os
16	
17	import numpy as np
18	
19	METHOD_NAMES = [
20	    "naive_pearson",
21	    "differenced_xcorr",
22	    "threshold_onset",
23	    "toda_yamamoto",
24	    "permutation_granger",
25	]
26	
27	# differenced_xcorr is the FP ground truth (index 1)
28	DIFF_INDEX = 1
29	
30	
31	def _to_native(obj):
32	    """Convert numpy types to Python native for JSON serialization."""
33	    if isinstance(obj, (np.integer,)):
34	        return int(obj)
35	    if isinstance(obj, (np.floating,)):
36	        return float(obj)
37	    if isinstance(obj, (np.bool_,)):
38	        return bool(obj)
39	    if isinstance(obj, np.ndarray):
40	        return obj.tolist()
41	    return obj
42	
43	
44	class NumpyEncoder(json.JSONEncoder):
45	    """JSON encoder that handles numpy types."""
46	    def default(self, obj):
47	        native = _to_native(obj)
48	        if native is not obj:
49	            return native
50	        return super().default(obj)
51	
52	
53	def load_sig_matrix(ablation_path, apply_fdr=True):
54	    """
55	    Load method_ablation.json into a boolean significance tensor.
56	
57	    Args:
58	        ablation_path: path to method_ablation.json
59	
60	    Returns:
61	        sig_matrix: np.ndarray, shape (5, 16, 4), dtype bool
62	                    axes = (method, pair, seed)
63	        pair_names: list of (canary, downstream) tuples, len 16
64	        method_names: list of str, len 5
65	        seeds: list of int, e.g. [42, 43, 44, 45]
66	 
…[truncated 23590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-18T21:27:49.845177+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-18T21:27:49.845333+00:00_

1	"""Cross-alpha analysis v4 with per-alpha consensus classification.
2	
3	Extends v3 with:
4	  5. Per-alpha multi-method consensus classification (regime-dependent validity)
5	  6. Markdown report output
6	
7	Handles mixed data paths:
8	  - alpha-sweep: results/alpha_sweep/a{NNN}_s42/all_metrics.json (single seed)
9	  - alpha=1.0:   results/mvp/rep_{42..45}/all_metrics.json (4 seeds)
10	  - alpha=1.0 consensus loads existing method_ablation.json
11	  - Single-seed alpha points: seed_threshold=1, method agreement only
12	
13	Dependencies: numpy, scipy, statsmodels
14	"""
15	
16	import argparse
17	import glob
18	import json
19	import os
20	import re
21	import sys
22	import warnings
23	from datetime import datetime
24	
25	import numpy as np
26	from statsmodels.stats.multitest import multipletests
27	
28	warnings.filterwarnings("ignore")
29	
30	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
31	sys.path.insert(0, BASE_DIR)
32	
33	from method_ablation import (
34	    CANARY, DOWNSTREAM,
35	    extract as ma_extract,
36	    naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto, perm_granger,
37	)
38	from consensus_framework import classify_robust, load_sig_matrix, NumpyEncoder
39	
40	SWEEP_DIR = os.path.join(BASE_DIR, "results", "alpha_sweep")
41	MVP_DIR = os.path.join(BASE_DIR, "results", "mvp")
42	ANALYSIS_DIR = os.path.join(BASE_DIR, "results", "analysis")
43	
44	METRICS = ["distinct_1", "distinct_2", "distinct_3", "token_entropy", "ece", "perplexity"]
45	
46	GRANGER_PAIRS = [
47	    ("token_entropy", "distinct_1", "entropy->d1"),
48	    ("ece",           "distinct_1", "ECE->d1"),
49	    ("token_entropy", "distinct_2", "entropy->d2"),
50	    ("ece",           "distinct_2", "ECE->d2"),
51	    ("distinct_1", "token_entropy", "d1->entropy"),
52	    ("distinct_1", "ece",           "d1->ECE"),
53	    ("distinct_2", "token_entropy", "d2->entropy"),
54	    ("distinct_2", "ece",           "d2->ECE"),
55	]
56	
57	XCORR_PAIRS = [
58	    ("token_entropy", "distinct_1", 
…[truncated 1496 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-18T21:27:49.845487+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"method_ablation.py\" -o -name \"*ablation*\" | grep -v \".lock\\|.log\\|.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"method_ablation.py\" -o -name \"*ablation*\" | grep -v \".lock\\|.log\\|.json\""
  }
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-18T21:27:49.845611+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/report/method_ablation_phase2_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/report/subset_ablation_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/method_ablation
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/method_ablation/subset_ablation_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/method_ablation_phase2
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/method_ablation_phase2/report/method_ablation_phase2_summary.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/configs/sprint_day1/plan_008_ablation_accum.sh

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-18T21:27:49.845740+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts -name \"method_ablation.py\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts -name \"method_ablation.py\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-18T21:27:49.845851+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-18T21:27:49.845971+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"from method_ablation import\\|from.*import.*naive_pearson\\|from.*import.*diff_xcorr\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse --include=\"*.py\" | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"from method_ablation import\\|from.*import.*naive_pearson\\|from.*import.*diff_xcorr\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse --include=\"*.py\" | head -5"
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-18T21:27:49.846083+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py:from method_ablation import (
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/cross_alpha/cross_alpha_analysis_v4.py:from method_ablation import (

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-18T21:27:49.846203+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ | grep \"method_ablation\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ | grep \"method_ablation\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-18T21:27:49.846328+00:00_

drwxr-xr-x  2 ubuntu ubuntu   4096 May 15 23:13 method_ablation
drwxr-xr-x  3 ubuntu ubuntu   4096 May 15 09:51 method_ablation_phase2

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-18T21:27:49.846448+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/*.py | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/*.py | head -20"
  }
}
```

</details>

---

### Tool result

_source line 109 · 2026-05-18T21:27:49.846558+00:00_

-rw-r--r-- 1 ubuntu ubuntu 23422 May 14 21:55 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_extended.py
-rw-r--r-- 1 ubuntu ubuntu 19888 May 14 08:34 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_mvp.py
-rw-r--r-- 1 ubuntu ubuntu 34169 May 15 08:58 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py
-rw-r--r-- 1 ubuntu ubuntu  4541 May 14 21:40 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/detrending_utils.py
-rw-r--r-- 1 ubuntu ubuntu 11276 May 14 19:05 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/iterative_train.py
-rw-r--r-- 1 ubuntu ubuntu 12171 May 14 07:26 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/metrics.py
-rw-r--r-- 1 ubuntu ubuntu  6974 May 14 21:51 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/permutation_granger.py
-rw-r--r-- 1 ubuntu ubuntu  2407 May 14 05:41 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/prepare_data.py
-rw-r--r-- 1 ubuntu ubuntu 12812 May 14 19:05 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/test_alpha_sweep.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-18T21:27:49.846688+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/*.py 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/*.py 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-18T21:27:49.846841+00:00_

-rw-r--r-- 1 ubuntu ubuntu  8465 May 14 21:29 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/bootstrap_ty_validation.py
-rw-r--r-- 1 ubuntu ubuntu 23204 May 15 10:06 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/consensus_framework.py
-rw-r--r-- 1 ubuntu ubuntu 18765 May 15 06:43 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-18T21:27:49.846984+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "def naive_pearson|def diff_xcorr|def threshold_lead|def toda_yamamoto|def perm_granger",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "type": "py",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Grep",
  "tool_args": {
    "pattern": "def naive_pearson|def diff_xcorr|def threshold_lead|def toda_yamamoto|def perm_granger",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
    "type": "py",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-18T21:27:49.847099+00:00_

artifacts/analyze_extended.py:151:def toda_yamamoto(metrics_list, cn, dn, d_max_mode="adaptive"):

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-18T21:27:49.847216+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-18T21:27:49.847383+00:00_

1	"""Cross-alpha analysis for distributional canary collapse experiments.
2	
3	Scans results/alpha_sweep/a*_s42/ directories, computes:
4	  1. Dose-response table (gen0→genN drift% per metric per α)
5	  2. Bidirectional permutation Granger causality with BH FDR correction
6	  3. Cross-correlation lead-lag analysis (Δmetric pairs)
7	  4. Per-generation velocity analysis for distinct_1
8	
9	Input:  results/alpha_sweep/a{NNN}_s42/all_metrics.json
10	Output: results/analysis/cross_alpha_v{VERSION}.json + terminal summary
11	
12	Dependencies: numpy, scipy, pandas, statsmodels
13	"""
14	
15	import argparse
16	import glob
17	import json
18	import os
19	import re
20	import sys
21	from datetime import datetime
22	
23	import numpy as np
24	from statsmodels.stats.multitest import multipletests
25	
26	
27	# ---------------------------------------------------------------------------
28	# Data loading
29	# ---------------------------------------------------------------------------
30	
31	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
32	SWEEP_DIR = os.path.join(BASE_DIR, "results", "alpha_sweep")
33	ANALYSIS_DIR = os.path.join(BASE_DIR, "results", "analysis")
34	
35	METRICS = ["distinct_1", "distinct_2", "distinct_3", "token_entropy", "ece", "perplexity"]
36	
37	# Granger test pairs: (cause, effect, label)
38	GRANGER_PAIRS = [
39	    ("token_entropy", "distinct_1", "entropy→d1"),
40	    ("ece",           "distinct_1", "ECE→d1"),
41	    ("token_entropy", "distinct_2", "entropy→d2"),
42	    ("ece",           "distinct_2", "ECE→d2"),
43	    ("distinct_1", "token_entropy", "d1→entropy"),
44	    ("distinct_1", "ece",           "d1→ECE"),
45	    ("distinct_2", "token_entropy", "d2→entropy"),
46	    ("distinct_2", "ece",           "d2→ECE"),
47	]
48	
49	XCORR_PAIRS = [
50	    ("token_entropy", "distinct_1", "entropy_vs_d1"),
51	    ("ece",           "distinct_1", "ece_vs_d1"),
52	]
53	
54	
55	def discover_alpha_dirs(explicit=None):
56	    """Find alpha experiment directories. Ret
…[truncated 965 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-18T21:27:49.847541+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep* -name \"*.json\" | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep* -name \"*.json\" | head -5"
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-18T21:27:49.847657+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a000_s43/data/a000_s43_5method_results_616865.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a000_s43/data/a000_s43_5method_results.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a075_s43/data/a075_s43_5method_results.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a075_s44/data/a075_s44_5method_results.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-18T21:27:49.847779+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a000_s43/data/a000_s43_5method_results.json",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a000_s43/data/a000_s43_5method_results.json",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-18T21:27:49.847907+00:00_

1	{
2	  "experiment": "alpha_sweep_a000_s43",
3	  "alpha": 0.0,
4	  "seed": 43,
5	  "n_generations": 11,
6	  "status": "completed",
7	  "metrics": {
8	    "gen0": {
9	      "token_entropy": 3.2342,
10	      "ece": 0.01080,
11	      "perplexity": 26.949,
12	      "distinct_1": 0.09833,
13	      "distinct_2": 0.51318,
14	      "distinct_3": 0.80567,
15	      "effective_rank": 46.613,
16	      "mauve": 0.03351
17	    },
18	    "gen10": {
19	      "token_entropy": 3.0907,
20	      "ece": 0.01482,
21	      "perplexity": 21.469,
22	      "distinct_1": 0.08465,
23	      "distinct_2": 0.46312,
24	      "distinct_3": 0.76723,
25	      "effective_rank": 43.720,
26	      "mauve": 0.02646
27	    },
28	    "drift_pct": {
29	      "token_entropy": -4.44,
30	      "ece": 37.16,
31	      "perplexity": -20.34,
32	      "distinct_1": -13.91,
33	      "distinct_2": -9.75,
34	      "distinct_3": -4.77,
35	      "effective_rank": -6.21,
36	      "mauve": -21.05
37	    }
38	  },
39	  "five_method_analysis": {
40	    "config": {
41	      "n_perm": 5000,
42	      "fdr_alpha": 0.05,
43	      "threshold_criterion": "3x_sigma_drift"
44	    },
45	    "summary": {
46	      "perm_granger_fdr_forward_sig": 0,
47	      "perm_granger_fdr_reverse_sig": 0,
48	      "diff_xcorr_fdr_forward_sig": 3,
49	      "diff_xcorr_fdr_reverse_sig": 3,
50	      "threshold_forward_sig": 1,

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-18T21:27:49.848048+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"method_ablation.py\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"method_ablation.py\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-18T21:27:49.848160+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-18T21:27:49.848291+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project -name \"*.py\" -type f | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project -name \"*.py\" -type f | head -10"
  }
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-18T21:27:49.848407+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/intermediate/iterative_train.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/cross_alpha_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/consensus_framework.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/permutation_granger.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-18T21:27:49.848531+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"5method_leadlag\\|naive_xcorr\\|diff_xcorr\\|threshold_onset\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs --include=\"*.log\" | head -3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"5method_leadlag\\|naive_xcorr\\|diff_xcorr\\|threshold_onset\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs --include=\"*.log\" | head -3"
  }
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-18T21:27:49.848653+00:00_

&lt;persisted-output>
Output too large (62.8KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/6c5856df-7e7e-4732-a15b-77014fe6cce0/tool-results/bncdb9ilw.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/logs/workers/worker_paper_writing_method_20260515T185754.log:{"type":"user","message":{"role":"user","content":[{"tool_use_id":"toolu_01G8RpYhChDhYPYMYjeQzna9","type":"tool_result","content":"1\t# Paper Framing — distrib_canary_collapse\n2\t\n3\t## Target Venue\n4\t- Primary: **EMNLP 2026 Main Track** (D043, 用户指定)\n5\t- ARR cycle: June 2026 (deadline ~June 15, 待确认具体日期)\n6\t- 格式: ACL 系列模板 (acl.sty), 8 页正文 + unlimited appendix\n7\t- Note: ARR May cycle 已过；June cycle 对齐 EMNLP 2026 commitment deadline\n8\t\n9\t## Narrative Structure (D027: Option B reframe)\n10\t\n11\t**主线**：方法论陷阱 + 多方法共识框架。Canary prediction 为系统性 case study。\n12\t**Claim 呈现顺序**：论文中 Claim 3 领衔 → Claim 2 (regime map) → Claim 1 (case study)。\n13\t**内部编号保持不变**（避免引用混乱），论文呈现时重排。\n14\t\n15\t## Core Claims (3 条，内部编号不变)\n16\t\n17\t1. **Canary→Diversity Granger-Causal Precedence (论文中作为 Case Study Finding)**: token_entropy 对 diversity 退化（distinct_1/2）具有 Granger-causal precedence——领先 1-2 代，差分后仍显著，证据来自多方法一致性：cross-correlation（lag=-1, std=0.0, |r|>0.99, p<0.004, 4/4 seed）、差分交叉相关（显著）、threshold onset（canary gen 1-2, diversity gen 3-4）、**permutation Granger（差分后仍 4/4 seed 显著，F=612-2615）**。论文可用措辞 (D037 更新)：*\"We demonstrate Granger-causal precedence of canary metrics at α≥0.75: α=1.0 achieves 24/24 FDR-sig (4 seeds), α=0.75 achieves 3/4 FDR-sig with the fourth borderline (p_fdr=0.054; single seed, pending multi-seed confirmation C001). Consistent temporal precedence (cross-correlation lag=+1, r=0.80–0.94) is observed across all contamination levels, though formal Granger tests at α≤0.50 do not reach FDR-corrected significance at T=11 (power analysis: §X).\"*升级上限：Granger ≠ 
…[truncated 299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-18T21:27:49.848801+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"*analysis*.py\" -type f | grep -v \"__pycache__\" | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -name \"*analysis*.py\" -type f | grep -v \"__pycache__\" | sort"
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-18T21:27:49.848914+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/data/cross_alpha_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/cross_alpha/cross_alpha_analysis_v4.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/cross_alpha_analysis.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 128 · 2026-05-18T21:27:49.849032+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-18T21:27:49.849173+00:00_

1	"""Cross-alpha analysis v4 with per-alpha consensus classification.
2	
3	Extends v3 with:
4	  5. Per-alpha multi-method consensus classification (regime-dependent validity)
5	  6. Markdown report output
6	
7	Handles mixed data paths:
8	  - alpha-sweep: results/alpha_sweep/a{NNN}_s42/all_metrics.json (single seed)
9	  - alpha=1.0:   results/mvp/rep_{42..45}/all_metrics.json (4 seeds)
10	  - alpha=1.0 consensus loads existing method_ablation.json
11	  - Single-seed alpha points: seed_threshold=1, method agreement only
12	
13	Dependencies: numpy, scipy, statsmodels
14	"""
15	
16	import argparse
17	import glob
18	import json
19	import os
20	import re
21	import sys
22	import warnings
23	from datetime import datetime
24	
25	import numpy as np
26	from statsmodels.stats.multitest import multipletests
27	
28	warnings.filterwarnings("ignore")
29	
30	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
31	sys.path.insert(0, BASE_DIR)
32	
33	from method_ablation import (
34	    CANARY, DOWNSTREAM,
35	    extract as ma_extract,
36	    naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto, perm_granger,
37	)
38	from consensus_framework import classify_robust, load_sig_matrix, NumpyEncoder
39	
40	SWEEP_DIR = os.path.join(BASE_DIR, "results", "alpha_sweep")
41	MVP_DIR = os.path.join(BASE_DIR, "results", "mvp")
42	ANALYSIS_DIR = os.path.join(BASE_DIR, "results", "analysis")
43	
44	METRICS = ["distinct_1", "distinct_2", "distinct_3", "token_entropy", "ece", "perplexity"]
45	
46	GRANGER_PAIRS = [
47	    ("token_entropy", "distinct_1", "entropy->d1"),
48	    ("ece",           "distinct_1", "ECE->d1"),
49	    ("token_entropy", "distinct_2", "entropy->d2"),
50	    ("ece",           "distinct_2", "ECE->d2"),
51	    ("distinct_1", "token_entropy", "d1->entropy"),
52	    ("distinct_1", "ece",           "d1->ECE"),
53	    ("distinct_2", "token_entropy", "d2->entropy"),
54	    ("distinct_2", "ece",           "d2->ECE"),
55	]
56	
57	XCORR_PAIRS = [
58	    ("token_entropy", "distinct_1", 
…[truncated 5452 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 130 · 2026-05-18T21:27:49.849341+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"method_ablation.py\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse -type f -name \"method_ablation.py\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-18T21:27:49.849457+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 132 · 2026-05-18T21:27:49.849576+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ | head -40"
  }
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-18T21:27:49.849693+00:00_

total 808
drwxr-xr-x 42 ubuntu ubuntu   4096 May 18 21:17 .
drwxr-xr-x 11 ubuntu ubuntu   4096 May 18 21:16 ..
drwxr-xr-x  3 ubuntu ubuntu   4096 May 15 15:41 D040
drwxr-xr-x  7 ubuntu ubuntu   4096 May 15 18:45 _project
-rw-r--r--  1 ubuntu ubuntu   2457 May 17 03:32 a050_s44_draft_versions.tex
-rw-r--r--  1 ubuntu ubuntu   1682 May 15 07:58 a075_analysis_prep.md
drwxr-xr-x  3 ubuntu ubuntu   4096 May 15 05:49 alpha_sweep
drwxr-xr-x  4 ubuntu ubuntu   4096 May 16 18:47 alpha_sweep_a000_s43
drwxr-xr-x  4 ubuntu ubuntu   4096 May 16 18:53 alpha_sweep_a000_s44
drwxr-xr-x  3 ubuntu ubuntu   4096 May 18 19:40 alpha_sweep_a010_s42_v2
drwxr-xr-x  3 ubuntu ubuntu   4096 May 15 05:47 alpha_sweep_a050_s42
drwxr-xr-x  3 ubuntu ubuntu   4096 May 15 22:02 alpha_sweep_a050_s43
drwxr-xr-x  3 ubuntu ubuntu   4096 May 17 06:38 alpha_sweep_a050_s44
drwxr-xr-x  2 ubuntu ubuntu   4096 May 18 20:53 alpha_sweep_a060_s42_bf16
drwxr-xr-x  3 ubuntu ubuntu   4096 May 15 13:31 alpha_sweep_a075_s42
drwxr-xr-x  4 ubuntu ubuntu   4096 May 16 14:27 alpha_sweep_a075_s43
drwxr-xr-x  4 ubuntu ubuntu   4096 May 16 14:23 alpha_sweep_a075_s44
drwxr-xr-x  3 ubuntu ubuntu   4096 May 18 20:27 alpha_sweep_c4_a050_s42_bf16
drwxr-xr-x  4 ubuntu ubuntu   4096 May 15 11:28 analysis
-rw-r--r--  1 ubuntu ubuntu   8542 May 18 19:40 analysis_alpha_sweep_a010_s42_v2.md
-rw-r--r--  1 ubuntu ubuntu  23422 May 14 21:55 analyze_extended.py
-rw-r--r--  1 ubuntu ubuntu  19888 May 14 08:34 analyze_mvp.py
-rw-r--r--  1 ubuntu ubuntu   5193 May 18 21:17 c4_vs_wikitext_a050_collapse.md
-rw-r--r--  1 ubuntu ubuntu   3422 May 14 19:04 ccf_maxlag7_report.md
-rwxr-xr-x  1 ubuntu ubuntu   6649 May 14 08:27 check_progress.sh
drwxr-xr-x  2 ubuntu ubuntu   4096 May 15 11:20 consensus_framework
drwxr-xr-x  2 ubuntu ubuntu   4096 May 15 21:04 cross_alpha_aggregation
-rw-r--r--  1 ubuntu ubuntu  34169 May 15 08:58 cross_alpha_analysis_v4.py
-rw-r--r--  1 ubuntu ubuntu   2405 May 15 09:01 cross_alpha_v4_ready.md
-rw-r--r--  1 ubuntu ub
…[truncated 697 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-18T21:27:49.849830+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-18T21:27:49.849945+00:00_

total 28
drwxr-xr-x  4 ubuntu ubuntu 4096 May 15 11:28 .
drwxr-xr-x 42 ubuntu ubuntu 4096 May 18 21:17 ..
drwxr-xr-x  2 ubuntu ubuntu 4096 May 15 11:23 consensus_framework
drwxr-xr-x  2 ubuntu ubuntu 4096 May 15 09:17 cross_alpha
-rw-r--r--  1 ubuntu ubuntu 8818 May 15 11:28 cross_alpha_fdr_4point.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-18T21:27:49.850067+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/cross_alpha/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analysis/cross_alpha/"
  }
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-18T21:27:49.850173+00:00_

total 44
drwxr-xr-x 2 ubuntu ubuntu  4096 May 15 09:17 .
drwxr-xr-x 4 ubuntu ubuntu  4096 May 15 11:28 ..
-rw-r--r-- 1 ubuntu ubuntu 34714 May 15 09:17 cross_alpha_analysis_v4.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-18T21:27:49.850304+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4 -name \"method_ablation.py\" -type f 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4 -name \"method_ablation.py\" -type f 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-18T21:27:49.850417+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-18T21:27:49.850561+00:00_

The method_ablation.py file doesn't exist yet in the project. Based on what I found, let me now compile a comprehensive report of my findings:

## Summary

I've thoroughly explored the project structure and found the following:

### Key Finding: Method Names Mismatch

The project uses **different method names** depending on context:

**In `consensus_framework.py` (lines 19-25):**
The 5 statistical methods are:
1. `naive_pearson`
2. `differenced_xcorr`
3. `threshold_onset`
4. `toda_yamamoto`
5. `permutation_granger`

**In the actual analysis scripts** (like `scripts/gen_single_method_table.py`):
The methods are referenced as:
1. `naive_xcorr`
2. `diff_xcorr`
3. `threshold_onset`
4. `perm_granger`
5. `ty_granger`

### Files Found

**1. Core Framework Files:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/consensus_framework.py` - Contains the multi-method consensus classification framework with the 5 METHOD_NAMES defined (lines 19-25)
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py` - Attempts to import from `method_ablation` module (lines 33-37), which includes the 5 methods

**2. Scripts that Generate JSON Results:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py` - Generates analysis from `5method_leadlag.json` files (line 8 references the file pattern: `a*_s*/analysis/5method_leadlag.json`)

**3. Related Implementation Files:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/analyze_extended.py` - Contains `toda_yamamoto()` implementation (line 151) and related methods
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/permutation_granger.py` - Likely contains permutation Granger implementation
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/detrending
…[truncated 1363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Agent",
  "elapsed_ms": 8
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-18T21:27:49.850710+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/**/5method*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/**/5method*.json",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-18T21:27:49.850828+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-18T21:27:49.850938+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "scripts/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Glob",
  "tool_args": {
    "pattern": "scripts/*.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-18T21:27:49.851046+00:00_

scripts/plot_regime_map.py
scripts/plot_consensus_workflow.py
scripts/gen_single_method_table.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-18T21:27:49.851152+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/scripts/gen_single_method_table.py"
  }
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-18T21:27:49.851345+00:00_

1	"""Generate Single-Method Error Consequence table from 5method_leadlag.json files."""
2	import json
3	import os
4	import glob
5	
6	BASE = "/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep"
7	
8	files = sorted(glob.glob(os.path.join(BASE, "a*_s*/analysis/5method_leadlag.json")))
9	
10	METHOD_KEYS = ["naive_xcorr", "diff_xcorr", "threshold_onset", "perm_granger", "ty_granger"]
11	METHOD_LABELS = {
12	    "naive_xcorr": "Naive XCorr",
13	    "diff_xcorr": "Diff XCorr (FDR)",
14	    "threshold_onset": "Threshold Onset",
15	    "perm_granger": "Perm Granger (FDR)",
16	    "ty_granger": "TY Granger",
17	}
18	
19	def get_sig(method_data, method_key):
20	    if method_key in ("diff_xcorr", "perm_granger"):
21	        return method_data.get("significant_fdr", method_data.get("significant", False))
22	    return method_data.get("significant", False)
23	
24	results = {}
25	data_sources = {}
26	
27	for f in files:
28	    with open(f) as fh:
29	        d = json.load(fh)
30	    if "meta" in d:
31	        alpha = d["meta"]["alpha"]
32	        seed = d["meta"]["seed"]
33	    else:
34	        alpha = d["alpha"]
35	        seed = d["seed"]
36	    alpha_str = f"a{int(alpha*100):03d}"
37	    key = (alpha_str, seed)
38	    data_sources[key] = f
39	
40	    method_sig = {m: 0 for m in METHOD_KEYS}
41	    n_pairs = len(d["pairs"])
42	
43	    for pair in d["pairs"]:
44	        fwd = pair["forward"]
45	        for m in METHOD_KEYS:
46	            if m in fwd and isinstance(fwd[m], dict) and get_sig(fwd[m], m):
47	                method_sig[m] += 1
48	
49	    results[key] = {"method_sig": method_sig, "n_pairs": n_pairs}
50	
51	ALPHAS = ["a000", "a025", "a050", "a075", "a100"]
52	ALPHA_LABELS = {"a000": "0.00", "a025": "0.25", "a050": "0.50", "a075": "0.75", "a100": "1.00"}
53	
54	print("=" * 80)
55	print("Per-seed, per-method forward significant pair counts (out of 8)")
56	print("=" * 80)
57	
58	for alpha in ALPHAS:
59	    seeds = sorted([k[1] for k in results if k[0] == alpha])
…[truncated 4095 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-18T21:27:49.851521+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results -name \"5method_leadlag.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results -name \"5method_leadlag.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-18T21:27:49.851651+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-18T21:27:49.851767+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"5method*\" -o -name \"five_method*\" -o -name \"lead_lag*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"5method*\" -o -name \"five_method*\" -o -name \"lead_lag*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-18T21:27:49.851892+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-18T21:27:49.852024+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"5method_leadlag.json\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"5method_leadlag.json\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-18T21:27:49.852157+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s43/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s44/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s43/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s44/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s43/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s44/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s44/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s42_bf16/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s42/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/opt1b_wiki_a100_s42/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia1b_c4_a100_s42/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s42/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia1b_c4_a100_s43/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s42/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_
…[truncated 188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-18T21:27:49.852335+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"run_5method*\" -o -name \"gen_5method*\" -o -name \"analyze_5method*\" -o -name \"method_ablation*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"run_5method*\" -o -name \"gen_5method*\" -o -name \"analyze_5method*\" -o -name \"method_ablation*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 154 · 2026-05-18T21:27:49.852466+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -100 /root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s42/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -100 /root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s42/analysis/5method_leadlag.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-18T21:27:49.852592+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/__pycache__/method_ablation.cpython-312.pyc\\n/root/autodl-tmp/distrib_canary_collapse/__pycache__/method_ablation.cpython-310.pyc\\n/root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_panel.json\\n/root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_report.md\\n/root/autodl-tmp/distrib_canary_collapse/method_ablation.py\\n/root/autodl-tmp/distrib_canary_collapse/method_ablation_phase2.py\\n/root/autodl-tmp/distrib_canary_collapse/run_5method_analysis.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-18T21:27:49.852760+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"alpha\\\": 1.0,\\n  \\\"seed\\\": 42,\\n  \\\"n_generations\\\": 11,\\n  \\\"data_dir\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s42\\\",\\n  \\\"methods\\\": [\\n    \\\"naive_xcorr\\\",\\n    \\\"diff_xcorr\\\",\\n    \\\"threshold_onset\\\",\\n    \\\"perm_granger\\\",\\n    \\\"ty_granger\\\"\\n  ],\\n  \\\"config\\\": {\\n    \\\"n_perm\\\": 5000,\\n    \\\"fdr_alpha\\\": 0.05,\\n    \\\"threshold_criterion\\\": \\\"3x_sigma_drift\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": -1,\\n          \\\"r\\\": 0.9976,\\n          \\\"p_value\\\": 0.0,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.9395,\\n              \\\"p\\\": 0.005384\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.9728,\\n              \\\"p\\\": 0.00023\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.9894,\\n              \\\"p\\\": 3e-06\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.994,\\n              \\\"p\\\": 0.0\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.9976,\\n              \\\"p\\\": 0.0\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.8876,\\n              \\\"p\\\": 0.000265\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.8882,\\n              \\\"p\\\": 0.000597\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\": 0.9244,\\n           
…[truncated 1014 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-18T21:27:49.852938+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-18T21:27:49.853061+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-18T21:27:49.853336+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"5-method lead-lag analysis: generalized CLI version.\\n\\nUsage:\\n    python run_5method_analysis.py --data_dir results/alpha_sweep/a000_s43 --alpha 0.0 --seed 43\\n    python run_5method_analysis.py --data_dir results/alpha_sweep/a000_s43 --alpha 0.0 --seed 43 --dry-run\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport glob as glob_module\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.tsa.stattools import adfuller\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/distrib_canary_collapse\\\")\\nfrom permutation_granger import permutation_granger_test\\n\\nN_PERM = 5000\\nALPHA = 0.05\\n\\nCANARIES = [\\\"token_entropy\\\", \\\"ece\\\"]\\nDOWNSTREAMS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"perplexity\\\"]\\n\\nHIGHER_IS_WORSE = {\\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\n\\ndef load_series(data_dir):\\n    \\\"\\\"\\\"Load metrics - from all_metrics.json if available, else aggregate gen_X/metrics.json.\\\"\\\"\\\"\\n    all_path = os.path.join(data_dir, \\\"all_metrics.json\\\")\\n    if os.path.exists(all_path):\\n        with open(all_path) as f:\\n            data = json.load(f)\\n    else:\\n        # Aggregate from per-generation metrics\\n        gen_dirs = sorted(glob_module.glob(os.path.join(data_dir, \\\"gen_*\\\")),\\n                         key=lambda x: int(os.path.basename(x).split(\\\"_\\\")[1]))\\n        data = []\\n        for gd in gen_dirs:\\n            mp = os.path.join(gd, \\\"metrics.json\\\")\\n            if os.path.exists(mp):\\n                with open(mp) as f:\\n                    data.append(json.load(f))\\n        if not data:\\n            raise FileNotFoundError(f\\\"No metrics found in {data_dir}\\\")\\n    data.sort(key=lambda x: x[\\\"generation\\\"])\\n    out = {}\\n    for k in CANARIES +
…[truncated 7282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-18T21:27:49.853632+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Method ablation: compare four lead-lag estimation methods.\\n\\nCompares naive vs robust approaches to detect canary->downstream lead-lag,\\nquantifying the spurious regression rate when non-stationary series are\\ncorrelated without proper detrending.\\n\\nInput:  results/mvp/rep_{seed}/all_metrics.json (seeds 42-45)\\nOutput: results/mvp/analysis/method_ablation.json\\n        (with BH FDR correction and effect sizes)\\n\\nMethods:\\n  1. Naive Pearson lag-correlation (raw levels)\\n  2. Differenced cross-correlation (first-differenced series)\\n  3. Threshold-based lead time (2-sigma onset detection)\\n  4. Toda-Yamamoto augmented-lag Granger causality\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport warnings\\nfrom itertools import product\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.stats.multitest import multipletests\\nfrom statsmodels.tsa.stattools import adfuller\\nfrom permutation_granger import permutation_granger_test\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nCANARY = [\\\"token_entropy\\\", \\\"self_bleu\\\", \\\"ece\\\", \\\"effective_rank\\\"]\\nDOWNSTREAM = [\\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"]\\n\\n# Sign conventions: \\\"higher is worse\\\" kept as-is; \\\"lower is worse\\\" negated\\n# so that degradation = positive direction in all analyses.\\nHIGHER_IS_WORSE = {\\\"self_bleu\\\", \\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"effective_rank\\\",\\n                   \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\nALPHA = 0.05\\n\\n\\ndef load_metrics(data_dir, seeds):\\n    \\\"\\\"\\\"Load all_metrics.json for each seed.\\\"\\\"\\\"\\n    data = {}\\n    for s in seeds:\\n        path = os.path.join(data_dir, f\\\"rep_{s}\\\", \\\"all_metrics.json\\\")\\n        with open(path) as f:\\n            data[s] = json.load(f)\\n    return 
…[truncated 7427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-18T21:27:49.853822+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/permutation_granger.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/permutation_granger.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-18T21:27:49.854097+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Permutation-based Granger causality test.\\n\\nUses permutation to build a null distribution of the Granger F-statistic,\\navoiding asymptotic assumptions that fail on short series (T<20).\\nFirst-differences the series to handle non-stationarity, then uses random\\nshuffle (not circular shift) since differencing removes autocorrelation.\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\n\\n\\ndef _build_lag_matrix(y, x, max_lag):\\n    \\\"\\\"\\\"Build design matrices for restricted and unrestricted Granger models.\\\"\\\"\\\"\\n    T = len(y)\\n    n = T - max_lag\\n    Y = y[max_lag:]\\n\\n    cols_r = [np.ones(n)]\\n    for lag in range(1, max_lag + 1):\\n        cols_r.append(y[max_lag - lag: T - lag])\\n\\n    cols_u = list(cols_r)\\n    for lag in range(1, max_lag + 1):\\n        cols_u.append(x[max_lag - lag: T - lag])\\n\\n    X_r = np.column_stack(cols_r)\\n    X_u = np.column_stack(cols_u)\\n    return Y, X_r, X_u\\n\\n\\ndef _granger_f_stat(y, x, max_lag):\\n    \\\"\\\"\\\"Compute Granger F-statistic: does x help predict y beyond y's own lags?\\\"\\\"\\\"\\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\\n    n = len(Y)\\n    q = max_lag\\n\\n    try:\\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\\n    except np.linalg.LinAlgError:\\n        return np.nan\\n\\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\\n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\\n\\n    k_u = X_u.shape[1]\\n    df_resid = n - k_u\\n\\n    if df_resid <= 0 or rss_u < 1e-15:\\n        return np.nan\\n\\n    F = ((rss_r - rss_u) / q) / (rss_u / df_resid)\\n    return F\\n\\n\\ndef permutation_granger_test(x, y, max_lag=1, n_perm=1000, seed=42,\\n                              difference=True):\\n    \\\"\\\"\\\"Permutation-based Granger causality test.\\n\\n    Tests whether x Granger-causes y using permutation null distribution.\\n    First-differences se
…[truncated 7406 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 163 · 2026-05-18T21:27:49.854359+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "cat << 'PYEOF' > /root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py\n\"\"\"Self-contained 5-method lead-lag analysis for GPT-2m s43.\"\"\"\nimport json\nimport os\nimport sys\nimport numpy as np\nfrom scipy import stats\nfrom statsmodels.tsa.stattools import adfuller\n\nN_PERM = 5000\nALPHA = 0.05\n\nCANARIES = [\"token_entropy\", \"ece\"]\nDOWNSTREAMS = [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"perplexity\"]\n\nHIGHER_IS_WORSE = {\"ece\", \"perplexity\"}\nLOWER_IS_WORSE = {\"token_entropy\", \"distinct_1\", \"distinct_2\", \"distinct_3\"}\n\nDATA_DIR = \"/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16\"\n\n\ndef load_series(data_dir):\n    with open(os.path.join(data_dir, \"all_metrics.json\")) as f:\n        data = json.load(f)\n    data.sort(key=lambda x: x[\"generation\"])\n    out = {}\n    for k in CANARIES + DOWNSTREAMS:\n        out[k] = np.array([d[k] for d in data])\n    return out, len(data)\n\n\ndef orient(series, name):\n    return -series.copy() if name in LOWER_IS_WORSE else series.copy()\n\n\ndef bh_fdr(p_values, alpha=0.05):\n    pv = np.array(p_values, dtype=float)\n    n = len(pv)\n    valid = ~np.isnan(pv)\n    adjusted = np.full(n, np.nan)\n    if valid.sum() == 0:\n        return adjusted.tolist(), [False] * n\n    idx = np.where(valid)[0]\n    p_valid = pv[idx]\n    sorted_idx = np.argsort(p_valid)\n    ranks = np.empty_like(sorted_idx)\n    ranks[sorted_idx] = np.arange(1, len(p_valid) + 1)\n    m = len(p_valid)\n    adj = p_valid * m / ranks\n    adj_sorted = adj[sorted_idx].copy()\n    for i in range(m - 2, -1, -1):\n        adj_sorted[i] = min(adj_sorted[i], adj_sorted[i + 1])\n    adj_sorted = np.minimum(adj_sorted, 1.0)\n    adj_final = np.empty(m)\n    adj_final[sorted_idx] = adj_sorted\n    for i, ix in enumerate(idx):\n        adjusted[ix] = adj_final[i]\n    significant = [(adjusted[i] < alpha if not np.isnan(adjusted[i]) else False) for i in range(n)]\n    return adjusted.tolist(), significant\n\n\n# Method 1: Naive cross-correlation\ndef naive_xcorr(c, d, cn, dn, max_lag=5):\n    x, y = orient(c, cn), orient(d, dn)\n    n = len(x)\n    best_lag, best_r, best_p = 0, 0.0, 1.0\n    all_lags = []\n    for lag in range(-max_lag, max_lag + 1):\n        if lag >= 0:\n            a, b = x[lag:], y[:n - lag]\n        else:\n            a, b = x[:n + lag], y[-lag:]\n        if len(a) < 4:\n            continue\n        r, p = stats.pearsonr(a, b)\n        all_lags.append({\"lag\": int(lag), \"r\": round(float(r), 4), \"p\": round(float(p), 6)})\n        if abs(r) > abs(best_r):\n            best_lag, best_r, best_p = lag, r, p\n    return {\n        \"method\": \"naive_xcorr\",\n        \"peak_lag\": int(best_lag),\n        \"r\": round(float(best_r), 4),\n        \"p_value\": round(float(best_p), 6),\n        \"significant\": bool(best_p < ALPHA),\n        \"all_lags\": all_lags,\n    }\n\n\n# Method 2: Differenced cross-correlation\ndef diff_xcorr(c, d, cn, dn, max_lag=5):\n    dx, dy = np.diff(orient(c, cn)), np.diff(orient(d, dn))\n    n = len(dx)\n    best_lag, best_r, best_p = 0, 0.0, 1.0\n    all_lags = []\n    for lag in range(-max_lag, max_lag + 1):\n        if lag >= 0:\n            a, b = dx[lag:], dy[:n - lag]\n        else:\n            a, b = dx[:n + lag], dy[-lag:]\n        if len(a) < 4:\n            continue\n        if np.std(a) < 1e-12 or np.std(b) < 1e-12:\n            continue\n        r, p = stats.pearsonr(a, b)\n        all_lags.append({\"lag\": int(lag), \"r\": round(float(r), 4), \"p\": round(float(p), 6)})\n        if abs(r) > abs(best_r):\n            best_lag, best_r, best_p = lag, r, p\n    return {\n        \"method\": \"diff_xcorr\",\n        \"peak_lag\": int(best_lag),\n        \"r\": round(float(best_r), 4),\n        \"p_value\": round(float(best_p), 6),\n        \"significant\": bool(best_p < ALPHA),\n        \"all_lags\": all_lags,\n    }\n\n\n# Method 3: Threshold onset detection\ndef threshold_onset(c, d, cn, dn, sigma_mult=3):\n    x, y = orient(c, cn), orient(d, dn)\n    gen0_c, gen0_d = x[0], y[0]\n    std_c = np.std(np.diff(x)) if len(x) > 1 else 1e-12\n    std_d = np.std(np.diff(y)) if len(y) > 1 else 1e-12\n    if std_c < 1e-12:\n        std_c = abs(gen0_c) * 0.01 if abs(gen0_c) > 1e-12 else 1e-6\n    if std_d < 1e-12:\n        std_d = abs(gen0_d) * 0.01 if abs(gen0_d) > 1e-12 else 1e-6\n    thresh_c = gen0_c + sigma_mult * std_c\n    thresh_d = gen0_d + sigma_mult * std_d\n    onset_c, onset_d = None, None\n    for i in range(1, len(x)):\n        if onset_c is None and x[i] > thresh_c:\n            onset_c = i\n        if onset_d is None and y[i] > thresh_d:\n            onset_d = i\n    if onset_c is not None and onset_d is not None:\n        lead = onset_d - onset_c\n        significant = lead > 0\n    elif onset_c is not None and onset_d is None:\n        lead = len(x) - onset_c\n        significant = True\n    else:\n        lead = 0\n        significant = False\n    return {\n        \"method\": \"threshold_onset\",\n        \"onset_canary\": onset_c,\n        \"onset_downstream\": onset_d,\n        \"lead_time\": int(lead) if lead is not None else None,\n        \"threshold_canary\": round(float(thresh_c), 6),\n        \"threshold_downstream\": round(float(thresh_d), 6),\n        \"significant\": significant,\n    }\n\n\n# Method 4: Permutation Granger\ndef _build_lag_matrix(y, x, max_lag):\n    T = len(y)\n    n = T - max_lag\n    Y = y[max_lag:]\n    cols_r = [np.ones(n)]\n    for lag in range(1, max_lag + 1):\n        cols_r.append(y[max_lag - lag: T - lag])\n    cols_u = list(cols_r)\n    for lag in range(1, max_lag + 1):\n        cols_u.append(x[max_lag - lag: T - lag])\n    return Y, np.column_stack(cols_r), np.column_stack(cols_u)\n\n\ndef _granger_f_stat(y, x, max_lag):\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\n    n = len(Y)\n    q = max_lag\n    try:\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\n    except np.linalg.LinAlgError:\n        return np.nan\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\n    k_u = X_u.shape[1]\n    df_resid = n - k_u\n    if df_resid <= 0 or rss_u < 1e-15:\n        return np.nan\n    return ((rss_r - rss_u) / q) / (rss_u / df_resid)\n\n\ndef perm_granger(x, y, max_lag=1, n_perm=5000, seed=42, difference=True):\n    x = np.asarray(x, dtype=float)\n    y = np.asarray(y, dtype=float)\n    if difference:\n        x, y = np.diff(x), np.diff(y)\n    T = len(x)\n    if T <= max_lag + 2:\n        return {\"f_stat\": None, \"p_value\": None, \"significant\": False, \"note\": f\"T={T} too short\"}\n    f_obs = _granger_f_stat(y, x, max_lag)\n    if np.isnan(f_obs):\n        return {\"f_stat\": None, \"p_value\": None, \"significant\": False, \"note\": \"F-stat failed\"}\n    rng = np.random.default_rng(seed)\n    null_f = np.empty(n_perm)\n    for i in range(n_perm):\n        null_f[i] = _granger_f_stat(y, rng.permutation(x), max_lag)\n    valid = null_f[~np.isnan(null_f)]\n    if len(valid) == 0:\n        return {\"f_stat\": round(float(f_obs), 4), \"p_value\": None, \"significant\": False}\n    p = (np.sum(valid >= f_obs) + 1) / (len(valid) + 1)\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\n    rss_r = np.sum((Y - X_r @ np.linalg.lstsq(X_r, Y, rcond=None)[0]) ** 2)\n    rss_u = np.sum((Y - X_u @ np.linalg.lstsq(X_u, Y, rcond=None)[0]) ** 2)\n    f2 = (rss_r - rss_u) / rss_u if rss_u > 1e-15 else None\n    return {\n        \"method\": \"perm_granger\",\n        \"f_stat\": round(float(f_obs), 4),\n        \"p_value\": round(float(p), 6),\n        \"significant\": bool(p < ALPHA),\n        \"n_perm\": n_perm,\n        \"effect_size_f2\": round(float(f2), 4) if f2 is not None else None,\n    }\n\n\n# Method 5: Toda-Yamamoto\ndef ty_granger(c, d, cn, dn, max_lag_search=2):\n    x, y = orient(c, cn), orient(d, dn)\n    T = len(x)\n    try:\n        adf_x = adfuller(x, maxlag=min(2, T // 3 - 1))\n        adf_y = adfuller(y, maxlag=min(2, T // 3 - 1))\n    except Exception:\n        return {\"method\": \"ty_granger\", \"significant\": False, \"note\": \"ADF failed\"}\n    d_max = 0\n    if adf_x[1] > 0.05:\n        d_max = max(d_max, 1)\n    if adf_y[1] > 0.05:\n        d_max = max(d_max, 1)\n    p_opt = 1\n    best_aic = np.inf\n    for p_try in range(1, max_lag_search + 1):\n        n_fit = T - p_try\n        if n_fit < 5:\n            continue\n        Y_fit = y[p_try:]\n        cols = [np.ones(n_fit)]\n        for lag in range(1, p_try + 1):\n            cols.append(y[p_try - lag: T - lag])\n            cols.append(x[p_try - lag: T - lag])\n        X_fit = np.column_stack(cols)\n        try:\n            beta = np.linalg.lstsq(X_fit, Y_fit, rcond=None)[0]\n            rss = np.sum((Y_fit - X_fit @ beta) ** 2)\n            k = X_fit.shape[1]\n            aic = n_fit * np.log(rss / n_fit + 1e-15) + 2 * k\n            if aic < best_aic:\n                best_aic = aic\n                p_opt = p_try\n        except Exception:\n            continue\n    p_aug = p_opt + d_max\n    n = T - p_aug\n    if n < 4:\n        return {\"method\": \"ty_granger\", \"significant\": False, \"note\": f\"n={n} too small\",\n                \"d_max\": d_max, \"p_opt\": p_opt, \"p_aug\": p_aug}\n    Y = y[p_aug:]\n    cols_r = [np.ones(n)]\n    for lag in range(1, p_aug + 1):\n        cols_r.append(y[p_aug - lag: T - lag])\n    for lag in range(p_opt + 1, p_aug + 1):\n        cols_r.append(x[p_aug - lag: T - lag])\n    X_r = np.column_stack(cols_r)\n    cols_u = list(cols_r)\n    for lag in range(1, p_opt + 1):\n        cols_u.append(x[p_aug - lag: T - lag])\n    X_u = np.column_stack(cols_u)\n    try:\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\n    except Exception:\n        return {\"method\": \"ty_granger\", \"significant\": False, \"note\": \"lstsq failed\"}\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\n    q = p_opt\n    df_resid = n - X_u.shape[1]\n    if df_resid <= 0 or rss_u < 1e-15:\n        return {\"method\": \"ty_granger\", \"significant\": False, \"note\": f\"df_resid={df_resid}\",\n                \"d_max\": d_max, \"p_opt\": p_opt, \"df_resid\": df_resid}\n    F = ((rss_r - rss_u) / q) / (rss_u / df_resid)\n    p_val = 1 - stats.f.cdf(F, q, df_resid)\n    f2 = (rss_r - rss_u) / rss_u if rss_u > 1e-15 else None\n    return {\n        \"method\": \"ty_granger\",\n        \"wald_F\": round(float(F), 4),\n        \"p_raw\": round(float(p_val), 6),\n        \"significant\": bool(p_val < ALPHA),\n        \"d_max\": int(d_max),\n        \"p_opt\": int(p_opt),\n        \"p_aug\": int(p_aug),\n        \"df_resid\": int(df_resid),\n        \"effect_size_f2\": round(float(f2), 4) if f2 is not None else None,\n    }\n\n\ndef run():\n    series, n_gens = load_series(DATA_DIR)\n    print(f\"Loaded {n_gens} generations from {DATA_DIR}\")\n    pair_results = []\n    for cn in CANARIES:\n        for dn in DOWNSTREAMS:\n            c, d = series[cn], series[dn]\n            fwd = {\n                \"naive_xcorr\": naive_xcorr(c, d, cn, dn),\n                \"diff_xcorr\": diff_xcorr(c, d, cn, dn),\n                \"threshold_onset\": threshold_onset(c, d, cn, dn),\n                \"perm_granger\": perm_granger(orient(c, cn), orient(d, dn), n_perm=N_PERM, seed=42),\n                \"ty_granger\": ty_granger(c, d, cn, dn),\n            }\n            rev = {\n                \"naive_xcorr\": naive_xcorr(d, c, dn, cn),\n                \"diff_xcorr\": diff_xcorr(d, c, dn, cn),\n                \"threshold_onset\": threshold_onset(d, c, dn, cn),\n                \"perm_granger\": perm_granger(orient(d, dn), orient(c, cn), n_perm=N_PERM, seed=42),\n                \"ty_granger\": ty_granger(d, c, dn, cn),\n            }\n            pair_results.append({\"canary\": cn, \"downstream\": dn, \"forward\": fwd, \"reverse\": rev})\n            print(f\"  {cn} -> {dn}: done\")\n\n    # BH FDR for diff_xcorr and perm_granger (forward)\n    for method_key in [\"diff_xcorr\", \"perm_granger\"]:\n        p_key = \"p_value\"\n        fwd_pvals = [p[\"forward\"][method_key].get(p_key) for p in pair_results]\n        fwd_pvals_clean = [p if p is not None else np.nan for p in fwd_pvals]\n        adj, sig = bh_fdr(fwd_pvals_clean)\n        for i, p in enumerate(pair_results):\n            p[\"forward\"][method_key][\"p_fdr\"] = round(adj[i], 6) if not np.isnan(adj[i]) else None\n            p[\"forward\"][method_key][\"significant_fdr\"] = sig[i]\n\n        rev_pvals = [p[\"reverse\"][method_key].get(p_key) for p in pair_results]\n        rev_pvals_clean = [p if p is not None else np.nan for p in rev_pvals]\n        adj_r, sig_r = bh_fdr(rev_pvals_clean)\n        for i, p in enumerate(pair_results):\n            p[\"reverse\"][method_key][\"p_fdr\"] = round(adj_r[i], 6) if not np.isnan(adj_r[i]) else None\n            p[\"reverse\"][method_key][\"significant_fdr\"] = sig_r[i]\n\n    all_results = {\n        \"alpha\": 1.0, \"seed\": 43, \"n_generations\": n_gens,\n        \"data_dir\": DATA_DIR,\n        \"methods\": [\"naive_xcorr\", \"diff_xcorr\", \"threshold_onset\", \"perm_granger\", \"ty_granger\"],\n        \"config\": {\"n_perm\": N_PERM, \"fdr_alpha\": 0.05, \"threshold_criterion\": \"3x_sigma_drift\"},\n        \"pairs\": pair_results,\n    }\n\n    # Count Table 7 columns\n    naive_sig = diff_sig = thresh_sig = pg_fwd_sig = pg_rev_sig = ty_sig = 0\n    consensus_list = []\n    for p in pair_results:\n        f = p[\"forward\"]\n        naive_ok = f[\"naive_xcorr\"][\"significant\"]\n        diff_ok = f[\"diff_xcorr\"].get(\"significant_fdr\", False)\n        thresh_ok = f[\"threshold_onset\"][\"significant\"]\n        pg_fwd_ok = f[\"perm_granger\"].get(\"significant_fdr\", False)\n        ty_ok = f[\"ty_granger\"][\"significant\"]\n        naive_sig += naive_ok\n        diff_sig += diff_ok\n        thresh_sig += thresh_ok\n        pg_fwd_sig += pg_fwd_ok\n        ty_sig += ty_ok\n        # Reverse perm granger\n        pg_rev_ok = p[\"reverse\"][\"perm_granger\"].get(\"significant_fdr\", False)\n        pg_rev_sig += pg_rev_ok\n        # K>=4 consensus\n        votes = sum([naive_ok, diff_ok, thresh_ok, pg_fwd_ok, ty_ok])\n        methods_sig = []\n        if naive_ok: methods_sig.append(\"naive\")\n        if diff_ok: methods_sig.append(\"diff\")\n        if thresh_ok: methods_sig.append(\"thresh\")\n        if pg_fwd_ok: methods_sig.append(\"pg\")\n        if ty_ok: methods_sig.append(\"ty\")\n        consensus_list.append({\"pair\": f\"{p['canary']}->{p['downstream']}\", \"votes\": votes, \"methods\": methods_sig})\n\n    k_gte4 = sum(1 for c in consensus_list if c[\"votes\"] >= 4)\n\n    all_results[\"consensus\"] = consensus_list\n    all_results[\"table7_row\"] = {\n        \"naive\": f\"{naive_sig}/8\",\n        \"diff_xcorr\": f\"{diff_sig}/8\",\n        \"threshold\": f\"{thresh_sig}/8\",\n        \"pg_fwd\": f\"{pg_fwd_sig}/8\",\n        \"pg_rev\": f\"{pg_rev_sig}/8\",\n        \"ty\": f\"{ty_sig}/8\",\n        \"k_gte4\": f\"{k_gte4}/8\",\n    }\n\n    print(f\"\\n{'='*60}\")\n    print(\"TABLE 7 ROW: GPT-2-medium / Wiki (s43)\")\n    print(f\"{'='*60}\")\n    t = all_results[\"table7_row\"]\n    print(f\"  Naive:      {t['naive']}\")\n    print(f\"  Diff XCorr: {t['diff_xcorr']}\")\n    print(f\"  Threshold:  {t['threshold']}\")\n    print(f\"  PermG fwd:  {t['pg_fwd']}\")\n    print(f\"  PermG rev:  {t['pg_rev']}\")\n    print(f\"  TY:         {t['ty']}\")\n    print(f\"  K>=4/5:     {t['k_gte4']}\")\n\n    print(f\"\\nConsensus detail:\")\n    for c in consensus_list:\n        print(f\"  {c['pair']:<30} {c['votes']}/5  [{', '.join(c['methods'])}]\")\n\n    # Save\n    out_dir = os.path.join(DATA_DIR, \"analysis\")\n    os.makedirs(out_dir, exist_ok=True)\n\n    def clean(obj):\n        if isinstance(obj, (np.floating, np.float64)):\n            return float(obj)\n        if isinstance(obj, (np.integer,)):\n            return int(obj)\n        if isinstance(obj, np.bool_):\n            return bool(obj)\n        if isinstance(obj, dict):\n            return {k: clean(v) for k, v in obj.items()}\n        if isinstance(obj, list):\n            return [clean(v) for v in obj]\n        return obj\n\n    json_path = os.path.join(out_dir, \"5method_leadlag.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(clean(all_results), f, indent=2)\n    print(f\"\\nSaved: {json_path}\")\n    return all_results\n\n\nif __name__ == \"__main__\":\n    run()\nPYEOF\necho \"Script written successfully\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat << 'PYEOF' > /root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py\n\"\"\"Self-contained 5-method lead-lag analysis for GPT-2m s43.\"\"\"\nimport json\nimport os\nimport sys\nimport numpy as np\nfrom scipy import stats\nfrom statsmodels.tsa.stattools import adfuller\n\nN_PERM = 5000\nALPHA = 0.05\n\nCANARIES = [\"token_entropy\", \"ece\"]\nDOWNSTREAMS = [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"perplexity\"]\n\nHIGHER_IS_WORSE = {\"ece\", \"perplexity\"}\nLOWER_IS_WORSE = {\"token_entropy\", \"distinct_1\", \"distinct_2\", \"distinct_3\"}\n\nDATA_DIR = \"/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16\"\n\n\ndef load_series(data_dir):\n    with open(os.path.join(data_dir, \"all_metrics.json\")) as f:\n        data = json.load(f)\n    data.sort(key=lambda x: x[\"generation\"])\n    out = {}\n    for k in CANARIES + DOWNSTREAMS:\n        out[k] = np.array([d[k] for d in data])\n    return out, len(data)\n\n\ndef orient(series, name):\n    return -series.copy() if name in LOWER_IS_WORSE else series.copy()\n\n\ndef bh_fdr(p_values, alpha=0.05):\n    pv = np.array(p_values, dtype=float)\n    n = len(pv)\n    valid = ~np.isnan(pv)\n    adjusted = np.full(n, np.nan)\n    if valid.sum() == 0:\n        return adjusted.tolist(), [False] * n\n    idx = np.where(valid)[0]\n    p_valid = pv[idx]\n    sorted_idx = np.argsort(p_valid)\n    ranks = np.empty_like(sorted_idx)\n    ranks[sorted_idx] = np.arange(1, len(p_valid) + 1)\n    m = len(p_valid)\n    adj = p_valid * m / ranks\n    adj_sorted = adj[sorted_idx].copy()\n    for i in range(m - 2, -1, -1):\n        adj_sorted[i] = min(adj_sorted[i], adj_sorted[i + 1])\n    adj_sorted = np.minimum(adj_sorted, 1.0)\n    adj_final = np.empty(m)\n    adj_final[sorted_idx] = adj_sorted\n    for i, ix in enumerate(idx):\n        adjusted[ix] = adj_final[i]\n    significant = [(adjusted[i] < alpha if not np.isnan(adjusted[i]) else False) for i in range(n)]\n    return adjusted.tolist(), significant\n\n\n# Method 1: Naive cross-correlation\ndef naive_xcorr(c, d, cn, dn, max_lag=5):\n    x, y = orient(c, cn), orient(d, dn)\n    n = len(x)\n    best_lag, best_r, best_p = 0, 0.0, 1.0\n    all_lags = []\n    for lag in range(-max_lag, max_lag + 1):\n        if lag >= 0:\n            a, b = x[lag:], y[:n - lag]\n        else:\n            a, b = x[:n + lag], y[-lag:]\n        if len(a) < 4:\n            continue\n        r, p = stats.pearsonr(a, b)\n        all_lags.append({\"lag\": int(lag), \"r\": round(float(r), 4), \"p\": round(float(p), 6)})\n        if abs(r) > abs(best_r):\n            best_lag, best_r, best_p = lag, r, p\n    return {\n        \"method\": \"naive_xcorr\",\n        \"peak_lag\": int(best_lag),\n        \"r\": round(float(best_r), 4),\n        \"p_value\": round(float(best_p), 6),\n        \"significant\": bool(best_p < ALPHA),\n        \"all_lags\": all_lags,\n    }\n\n\n# Method 2: Differenced cross-correlation\ndef diff_xcorr(c, d, cn, dn, max_lag=5):\n    dx, dy = np.diff(orient(c, cn)), np.diff(orient(d, dn))\n    n = len(dx)\n    best_lag, best_r, best_p = 0, 0.0, 1.0\n    all_lags = []\n    for lag in range(-max_lag, max_lag + 1):\n        if lag >= 0:\n            a, b = dx[lag:], dy[:n - lag]\n        else:\n            a, b = dx[:n + lag], dy[-lag:]\n        if len(a) < 4:\n            continue\n        if np.std(a) < 1e-12 or np.std(b) < 1e-12:\n            continue\n        r, p = stats.pearsonr(a, b)\n        all_lags.append({\"lag\": int(lag), \"r\": round(float(r), 4), \"p\": round(float(p), 6)})\n        if abs(r) > abs(best_r):\n            best_lag, best_r, best_p = lag, r, p\n    return {\n        \"method\": \"diff_xcorr\",\n        \"peak_lag\": int(best_lag),\n        \"r\": round(float(best_r), 4),\n        \"p_value\": round(float(best_p), 6),\n        \"significant\": bool(best_p < ALPHA),\n        \"all_lags\": all_lags,\n    }\n\n\n# Method 3: Threshold onset detection\ndef threshold_onset(c, d, cn, dn, sigma_mult=3):\n    x, y = orient(c, cn), orient(d, dn)\n    gen0_c, gen0_d = x[0], y[0]\n    std_c = np.std(np.diff(x)) if len(x) > 1 else 1e-12\n    std_d = np.std(np.diff(y)) if len(y) > 1 else 1e-12\n    if std_c < 1e-12:\n        std_c = abs(gen0_c) * 0.01 if abs(gen0_c) > 1e-12 else 1e-6\n    if std_d < 1e-12:\n        std_d = abs(gen0_d) * 0.01 if abs(gen0_d) > 1e-12 else 1e-6\n    thresh_c = gen0_c + sigma_mult * std_c\n    thresh_d = gen0_d + sigma_mult * std_d\n    onset_c, onset_d = None, None\n    for i in range(1, len(x)):\n        if onset_c is None and x[i] > thresh_c:\n            onset_c = i\n        if onset_d is None and y[i] > thresh_d:\n            onset_d = i\n    if onset_c is not None and onset_d is not None:\n        lead = onset_d - onset_c\n        significant = lead > 0\n    elif onset_c is not None and onset_d is None:\n        lead = len(x) - onset_c\n        significant = True\n    else:\n        lead = 0\n        significant = False\n    return {\n        \"method\": \"threshold_onset\",\n        \"onset_canary\": onset_c,\n        \"onset_downstream\": onset_d,\n        \"lead_time\": int(lead) if lead is not None else None,\n        \"threshold_canary\": round(float(thresh_c), 6),\n        \"threshold_downstream\": round(float(thresh_d), 6),\n        \"significant\": significant,\n    }\n\n\n# Method 4: Permutation Granger\ndef _build_lag_matrix(y, x, max_lag):\n    T = len(y)\n    n = T - max_lag\n    Y = y[max_lag:]\n    cols_r = [np.ones(n)]\n    for lag in range(1, max_lag + 1):\n        cols_r.append(y[max_lag - lag: T - lag])\n    cols_u = list(cols_r)\n    for lag in range(1, max_lag + 1):\n        cols_u.append(x[max_lag - lag: T - lag])\n    return Y, np.column_stack(cols_r), np.column_stack(cols_u)\n\n\ndef _granger_f_stat(y, x, max_lag):\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\n    n = len(Y)\n    q = max_lag\n    try:\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\n    except np.linalg.LinAlgError:\n        return np.nan\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\n    k_u = X_u.shape[1]\n    df_resid = n - k_u\n    if df_resid <= 0 or rss_u < 1e-15:\n        return np.nan\n    return ((rss_r - rss_u) / q) / (rss_u / df_resid)\n\n\ndef perm_granger(x, y, max_lag=1, n_perm=5000, seed=42, difference=True):\n    x = np.asarray(x, dtype=float)\n    y = np.asarray(y, dtype=float)\n    if difference:\n        x, y = np.diff(x), np.diff(y)\n    T = len(x)\n    if T <= max_lag + 2:\n        return {\"f_stat\": None, \"p_value\": None, \"significant\": False, \"note\": f\"T={T} too short\"}\n    f_obs = _granger_f_stat(y, x, max_lag)\n    if np.isnan(f_obs):\n        return {\"f_stat\": None, \"p_value\": None, \"significant\": False, \"note\": \"F-stat failed\"}\n    rng = np.random.default_rng(seed)\n    null_f = np.empty(n_perm)\n    for i in range(n_perm):\n        null_f[i] = _granger_f_stat(y, rng.permutation(x), max_lag)\n    valid = null_f[~np.isnan(null_f)]\n    if len(valid) == 0:\n        return {\"f_stat\": round(float(f_obs), 4), \"p_value\": None, \"significant\": False}\n    p = (np.sum(valid >= f_obs) + 1) / (len(valid) + 1)\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\n    rss_r = np.sum((Y - X_r @ np.linalg.lstsq(X_r, Y, rcond=None)[0]) ** 2)\n    rss_u = np.sum((Y - X_u @ np.linalg.lstsq(X_u, Y, rcond=None)[0]) ** 2)\n    f2 = (rss_r - rss_u) / rss_u if rss_u > 1e-15 else None\n    return {\n        \"method\": \"perm_granger\",\n        \"f_stat\": round(float(f_obs), 4),\n        \"p_value\": round(float(p), 6),\n        \"significant\": bool(p < ALPHA),\n        \"n_perm\": n_perm,\n        \"effect_size_f2\": round(float(f2), 4) if f2 is not None else None,\n    }\n\n\n# Method 5: Toda-Yamamoto\ndef ty_granger(c, d, cn, dn, max_lag_search=2):\n    x, y = orient(c, cn), orient(d, dn)\n    T = len(x)\n    try:\n        adf_x = adfuller(x, maxlag=min(2, T // 3 - 1))\n        adf_y = adfuller(y, maxlag=min(2, T // 3 - 1))\n    except Exception:\n        return {\"method\": \"ty_granger\", \"significant\": False, \"note\": \"ADF failed\"}\n    d_max = 0\n    if adf_x[1] > 0.05:\n        d_max = max(d_max, 1)\n    if adf_y[1] > 0.05:\n        d_max = max(d_max, 1)\n    p_opt = 1\n    best_aic = np.inf\n    for p_try in range(1, max_lag_search + 1):\n        n_fit = T - p_try\n        if n_fit < 5:\n            continue\n        Y_fit = y[p_try:]\n        cols = [np.ones(n_fit)]\n        for lag in range(1, p_try + 1):\n            cols.append(y[p_try - lag: T - lag])\n            cols.append(x[p_try - lag: T - lag])\n        X_fit = np.column_stack(cols)\n        try:\n            beta = np.linalg.lstsq(X_fit, Y_fit, rcond=None)[0]\n            rss = np.sum((Y_fit - X_fit @ beta) ** 2)\n            k = X_fit.shape[1]\n            aic = n_fit * np.log(rss / n_fit + 1e-15) + 2 * k\n            if aic < best_aic:\n                best_aic = aic\n                p_opt = p_try\n        except Exception:\n            continue\n    p_aug = p_opt + d_max\n    n = T - p_aug\n    if n < 4:\n        return {\"method\": \"ty_granger\", \"significant\": False, \"note\": f\"n={n} too small\",\n                \"d_max\": d_max, \"p_opt\": p_opt, \"p_aug\": p_aug}\n    Y = y[p_aug:]\n    cols_r = [np.ones(n)]\n    for lag in range(1, p_aug + 1):\n        cols_r.append(y[p_aug - lag: T - lag])\n    for lag in range(p_opt + 1, p_aug + 1):\n        cols_r.append(x[p_aug - lag: T - lag])\n    X_r = np.column_stack(cols_r)\n    cols_u = list(cols_r)\n    for lag in range(1, p_opt + 1):\n        cols_u.append(x[p_aug - lag: T - lag])\n    X_u = np.column_stack(cols_u)\n    try:\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\n    except Exception:\n        return {\"method\": \"ty_granger\", \"significant\": False, \"note\": \"lstsq failed\"}\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\n    q = p_opt\n    df_resid = n - X_u.shape[1]\n    if df_resid <= 0 or rss_u < 1e-15:\n        return {\"method\": \"ty_granger\", \"significant\": False, \"note\": f\"df_resid={df_resid}\",\n                \"d_max\": d_max, \"p_opt\": p_opt, \"df_resid\": df_resid}\n    F = ((rss_r - rss_u) / q) / (rss_u / df_resid)\n    p_val = 1 - stats.f.cdf(F, q, df_resid)\n    f2 = (rss_r - rss_u) / rss_u if rss_u > 1e-15 else None\n    return {\n        \"method\": \"ty_granger\",\n        \"wald_F\": round(float(F), 4),\n        \"p_raw\": round(float(p_val), 6),\n        \"significant\": bool(p_val < ALPHA),\n        \"d_max\": int(d_max),\n        \"p_opt\": int(p_opt),\n        \"p_aug\": int(p_aug),\n        \"df_resid\": int(df_resid),\n        \"effect_size_f2\": round(float(f2), 4) if f2 is not None else None,\n    }\n\n\ndef run():\n    series, n_gens = load_series(DATA_DIR)\n    print(f\"Loaded {n_gens} generations from {DATA_DIR}\")\n    pair_results = []\n    for cn in CANARIES:\n        for dn in DOWNSTREAMS:\n            c, d = series[cn], series[dn]\n            fwd = {\n                \"naive_xcorr\": naive_xcorr(c, d, cn, dn),\n                \"diff_xcorr\": diff_xcorr(c, d, cn, dn),\n                \"threshold_onset\": threshold_onset(c, d, cn, dn),\n                \"perm_granger\": perm_granger(orient(c, cn), orient(d, dn), n_perm=N_PERM, seed=42),\n                \"ty_granger\": ty_granger(c, d, cn, dn),\n            }\n            rev = {\n                \"naive_xcorr\": naive_xcorr(d, c, dn, cn),\n                \"diff_xcorr\": diff_xcorr(d, c, dn, cn),\n                \"threshold_onset\": threshold_onset(d, c, dn, cn),\n                \"perm_granger\": perm_granger(orient(d, dn), orient(c, cn), n_perm=N_PERM, seed=42),\n                \"ty_granger\": ty_granger(d, c, dn, cn),\n            }\n            pair_results.append({\"canary\": cn, \"downstream\": dn, \"forward\": fwd, \"reverse\": rev})\n            print(f\"  {cn} -> {dn}: done\")\n\n    # BH FDR for diff_xcorr and perm_granger (forward)\n    for method_key in [\"diff_xcorr\", \"perm_granger\"]:\n        p_key = \"p_value\"\n        fwd_pvals = [p[\"forward\"][method_key].get(p_key) for p in pair_results]\n        fwd_pvals_clean = [p if p is not None else np.nan for p in fwd_pvals]\n        adj, sig = bh_fdr(fwd_pvals_clean)\n        for i, p in enumerate(pair_results):\n            p[\"forward\"][method_key][\"p_fdr\"] = round(adj[i], 6) if not np.isnan(adj[i]) else None\n            p[\"forward\"][method_key][\"significant_fdr\"] = sig[i]\n\n        rev_pvals = [p[\"reverse\"][method_key].get(p_key) for p in pair_results]\n        rev_pvals_clean = [p if p is not None else np.nan for p in rev_pvals]\n        adj_r, sig_r = bh_fdr(rev_pvals_clean)\n        for i, p in enumerate(pair_results):\n            p[\"reverse\"][method_key][\"p_fdr\"] = round(adj_r[i], 6) if not np.isnan(adj_r[i]) else None\n            p[\"reverse\"][method_key][\"significant_fdr\"] = sig_r[i]\n\n    all_results = {\n        \"alpha\": 1.0, \"seed\": 43, \"n_generations\": n_gens,\n        \"data_dir\": DATA_DIR,\n        \"methods\": [\"naive_xcorr\", \"diff_xcorr\", \"threshold_onset\", \"perm_granger\", \"ty_granger\"],\n        \"config\": {\"n_perm\": N_PERM, \"fdr_alpha\": 0.05, \"threshold_criterion\": \"3x_sigma_drift\"},\n        \"pairs\": pair_results,\n    }\n\n    # Count Table 7 columns\n    naive_sig = diff_sig = thresh_sig = pg_fwd_sig = pg_rev_sig = ty_sig = 0\n    consensus_list = []\n    for p in pair_results:\n        f = p[\"forward\"]\n        naive_ok = f[\"naive_xcorr\"][\"significant\"]\n        diff_ok = f[\"diff_xcorr\"].get(\"significant_fdr\", False)\n        thresh_ok = f[\"threshold_onset\"][\"significant\"]\n        pg_fwd_ok = f[\"perm_granger\"].get(\"significant_fdr\", False)\n        ty_ok = f[\"ty_granger\"][\"significant\"]\n        naive_sig += naive_ok\n        diff_sig += diff_ok\n        thresh_sig += thresh_ok\n        pg_fwd_sig += pg_fwd_ok\n        ty_sig += ty_ok\n        # Reverse perm granger\n        pg_rev_ok = p[\"reverse\"][\"perm_granger\"].get(\"significant_fdr\", False)\n        pg_rev_sig += pg_rev_ok\n        # K>=4 consensus\n        votes = sum([naive_ok, diff_ok, thresh_ok, pg_fwd_ok, ty_ok])\n        methods_sig = []\n        if naive_ok: methods_sig.append(\"naive\")\n        if diff_ok: methods_sig.append(\"diff\")\n        if thresh_ok: methods_sig.append(\"thresh\")\n        if pg_fwd_ok: methods_sig.append(\"pg\")\n        if ty_ok: methods_sig.append(\"ty\")\n        consensus_list.append({\"pair\": f\"{p['canary']}->{p['downstream']}\", \"votes\": votes, \"methods\": methods_sig})\n\n    k_gte4 = sum(1 for c in consensus_list if c[\"votes\"] >= 4)\n\n    all_results[\"consensus\"] = consensus_list\n    all_results[\"table7_row\"] = {\n        \"naive\": f\"{naive_sig}/8\",\n        \"diff_xcorr\": f\"{diff_sig}/8\",\n        \"threshold\": f\"{thresh_sig}/8\",\n        \"pg_fwd\": f\"{pg_fwd_sig}/8\",\n        \"pg_rev\": f\"{pg_rev_sig}/8\",\n        \"ty\": f\"{ty_sig}/8\",\n        \"k_gte4\": f\"{k_gte4}/8\",\n    }\n\n    print(f\"\\n{'='*60}\")\n    print(\"TABLE 7 ROW: GPT-2-medium / Wiki (s43)\")\n    print(f\"{'='*60}\")\n    t = all_results[\"table7_row\"]\n    print(f\"  Naive:      {t['naive']}\")\n    print(f\"  Diff XCorr: {t['diff_xcorr']}\")\n    print(f\"  Threshold:  {t['threshold']}\")\n    print(f\"  PermG fwd:  {t['pg_fwd']}\")\n    print(f\"  PermG rev:  {t['pg_rev']}\")\n    print(f\"  TY:         {t['ty']}\")\n    print(f\"  K>=4/5:     {t['k_gte4']}\")\n\n    print(f\"\\nConsensus detail:\")\n    for c in consensus_list:\n        print(f\"  {c['pair']:<30} {c['votes']}/5  [{', '.join(c['methods'])}]\")\n\n    # Save\n    out_dir = os.path.join(DATA_DIR, \"analysis\")\n    os.makedirs(out_dir, exist_ok=True)\n\n    def clean(obj):\n        if isinstance(obj, (np.floating, np.float64)):\n            return float(obj)\n        if isinstance(obj, (np.integer,)):\n            return int(obj)\n        if isinstance(obj, np.bool_):\n            return bool(obj)\n        if isinstance(obj, dict):\n            return {k: clean(v) for k, v in obj.items()}\n        if isinstance(obj, list):\n            return [clean(v) for v in obj]\n        return obj\n\n    json_path = os.path.join(out_dir, \"5method_leadlag.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(clean(all_results), f, indent=2)\n    print(f\"\\nSaved: {json_path}\")\n    return all_results\n\n\nif __name__ == \"__main__\":\n    run()\nPYEOF\necho \"Script written successfully\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-18T21:27:49.854643+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written successfully\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-18T21:27:49.854791+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python run_5method_s43.py",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python run_5method_s43.py",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-18T21:27:49.854930+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loaded 11 generations from /root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16\\n  token_entropy -> distinct_1: done\\n  token_entropy -> distinct_2: done\\n  token_entropy -> distinct_3: done\\n  token_entropy -> perplexity: done\\n  ece -> distinct_1: done\\n  ece -> distinct_2: done\\n  ece -> distinct_3: done\\n  ece -> perplexity: done\\n\\n============================================================\\nTABLE 7 ROW: GPT-2-medium / Wiki (s43)\\n============================================================\\n  Naive:      8/8\\n  Diff XCorr: 7/8\\n  Threshold:  8/8\\n  PermG fwd:  1/8\\n  PermG rev:  0/8\\n  TY:         0/8\\n  K>=4/5:     1/8\\n\\nConsensus detail:\\n  token_entropy->distinct_1      3/5  [naive, diff, thresh]\\n  token_entropy->distinct_2      3/5  [naive, diff, thresh]\\n  token_entropy->distinct_3      3/5  [naive, diff, thresh]\\n  token_entropy->perplexity      3/5  [naive, diff, thresh]\\n  ece->distinct_1                3/5  [naive, diff, thresh]\\n  ece->distinct_2                3/5  [naive, diff, thresh]\\n  ece->distinct_3                2/5  [naive, thresh]\\n  ece->perplexity                4/5  [naive, diff, thresh, pg]\\n\\nSaved: /root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16/analysis/5method_leadlag.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.84}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-18T21:27:49.855113+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "python3 -c \"\nimport json\nwith open('/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16/analysis/5method_leadlag.json') as f:\n    d = json.load(f)\nfor p in d['pairs']:\n    cn, dn = p['canary'], p['downstream']\n    fwd = p['forward']\n    pg_p = fwd['perm_granger'].get('p_value', 'N/A')\n    pg_fdr = fwd['perm_granger'].get('p_fdr', 'N/A')\n    pg_f = fwd['perm_granger'].get('f_stat', 'N/A')\n    ty_p = fwd['ty_granger'].get('p_raw', 'N/A')\n    ty_f = fwd['ty_granger'].get('wald_F', 'N/A')\n    ty_df = fwd['ty_granger'].get('df_resid', 'N/A')\n    ty_d = fwd['ty_granger'].get('d_max', 'N/A')\n    diff_p = fwd['diff_xcorr'].get('p_value', 'N/A')\n    diff_fdr = fwd['diff_xcorr'].get('p_fdr', 'N/A')\n    diff_lag = fwd['diff_xcorr'].get('peak_lag', 'N/A')\n    print(f'{cn}->{dn}: PG p={pg_p} fdr={pg_fdr} F={pg_f} | TY p={ty_p} F={ty_f} df={ty_df} d={ty_d} | diff lag={diff_lag} p={diff_p} fdr={diff_fdr}')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "python3 -c \"\nimport json\nwith open('/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16/analysis/5method_leadlag.json') as f:\n    d = json.load(f)\nfor p in d['pairs']:\n    cn, dn = p['canary'], p['downstream']\n    fwd = p['forward']\n    pg_p = fwd['perm_granger'].get('p_value', 'N/A')\n    pg_fdr = fwd['perm_granger'].get('p_fdr', 'N/A')\n    pg_f = fwd['perm_granger'].get('f_stat', 'N/A')\n    ty_p = fwd['ty_granger'].get('p_raw', 'N/A')\n    ty_f = fwd['ty_granger'].get('wald_F', 'N/A')\n    ty_df = fwd['ty_granger'].get('df_resid', 'N/A')\n    ty_d = fwd['ty_granger'].get('d_max', 'N/A')\n    diff_p = fwd['diff_xcorr'].get('p_value', 'N/A')\n    diff_fdr = fwd['diff_xcorr'].get('p_fdr', 'N/A')\n    diff_lag = fwd['diff_xcorr'].get('peak_lag', 'N/A')\n    print(f'{cn}->{dn}: PG p={pg_p} fdr={pg_fdr} F={pg_f} | TY p={ty_p} F={ty_f} df={ty_df} d={ty_d} | diff lag={diff_lag} p={diff_p} fdr={diff_fdr}')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 168 · 2026-05-18T21:27:49.855247+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-18T21:27:49.855391+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nimport json\nwith open('/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16/analysis/5method_leadlag.json') as f:\n    d = json.load(f)\nfor p in d['pairs']:\n    cn, dn = p['canary'], p['downstream']\n    fwd = p['forward']\n    pg_p = fwd['perm_granger'].get('p_value', 'N/A')\n    pg_fdr = fwd['perm_granger'].get('p_fdr', 'N/A')\n    pg_f = fwd['perm_granger'].get('f_stat', 'N/A')\n    ty_p = fwd['ty_granger'].get('p_raw', 'N/A')\n    ty_f = fwd['ty_granger'].get('wald_F', 'N/A')\n    ty_df = fwd['ty_granger'].get('df_resid', 'N/A')\n    ty_d = fwd['ty_granger'].get('d_max', 'N/A')\n    diff_p = fwd['diff_xcorr'].get('p_value', 'N/A')\n    diff_fdr = fwd['diff_xcorr'].get('p_fdr', 'N/A')\n    diff_lag = fwd['diff_xcorr'].get('peak_lag', 'N/A')\n    print(f'{cn}->{dn}: PG p={pg_p} fdr={pg_fdr} F={pg_f}')\n    print(f'  TY p={ty_p} F={ty_f} df={ty_df} d={ty_d}')\n    print(f'  diff lag={diff_lag} p={diff_p} fdr={diff_fdr}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nimport json\nwith open('/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16/analysis/5method_leadlag.json') as f:\n    d = json.load(f)\nfor p in d['pairs']:\n    cn, dn = p['canary'], p['downstream']\n    fwd = p['forward']\n    pg_p = fwd['perm_granger'].get('p_value', 'N/A')\n    pg_fdr = fwd['perm_granger'].get('p_fdr', 'N/A')\n    pg_f = fwd['perm_granger'].get('f_stat', 'N/A')\n    ty_p = fwd['ty_granger'].get('p_raw', 'N/A')\n    ty_f = fwd['ty_granger'].get('wald_F', 'N/A')\n    ty_df = fwd['ty_granger'].get('df_resid', 'N/A')\n    ty_d = fwd['ty_granger'].get('d_max', 'N/A')\n    diff_p = fwd['diff_xcorr'].get('p_value', 'N/A')\n    diff_fdr = fwd['diff_xcorr'].get('p_fdr', 'N/A')\n    diff_lag = fwd['diff_xcorr'].get('peak_lag', 'N/A')\n    print(f'{cn}->{dn}: PG p={pg_p} fdr={pg_fdr} F={pg_f}')\n    print(f'  TY p={ty_p} F={ty_f} df={ty_df} d={ty_d}')\n    print(f'  diff lag={diff_lag} p={diff_p} fdr={diff_fdr}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-18T21:27:49.855529+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"token_entropy->distinct_1: PG p=0.082184 fdr=0.187163 F=19.5137\\n  TY p=0.950735 F=0.0043 df=4 d=1\\n  diff lag=-3 p=0.000954 fdr=0.001526\\ntoken_entropy->distinct_2: PG p=0.107978 fdr=0.187163 F=4.464\\n  TY p=0.167723 F=2.8315 df=4 d=1\\n  diff lag=-3 p=0.004493 fdr=0.005991\\ntoken_entropy->distinct_3: PG p=0.140372 fdr=0.187163 F=1.8387\\n  TY p=0.107717 F=4.2684 df=4 d=1\\n  diff lag=3 p=0.013336 fdr=0.015241\\ntoken_entropy->perplexity: PG p=0.136973 fdr=0.187163 F=2.6574\\n  TY p=0.152048 F=21.1275 df=1 d=1\\n  diff lag=0 p=3e-06 fdr=2.4e-05\\nece->distinct_1: PG p=0.841032 fdr=0.841032 F=0.051\\n  TY p=0.838857 F=0.1837 df=4 d=0\\n  diff lag=0 p=9e-06 fdr=3.6e-05\\nece->distinct_2: PG p=0.118376 fdr=0.187163 F=3.4018\\n  TY p=0.160888 F=18.8162 df=1 d=1\\n  diff lag=0 p=0.000797 fdr=0.001526\\nece->distinct_3: PG p=0.525095 fdr=0.600109 F=0.4865\\n  TY p=0.333524 F=1.2075 df=4 d=1\\n  diff lag=5 p=0.062846 fdr=0.062846\\nece->perplexity: PG p=0.0016 fdr=0.0128 F=41.9202\\n  TY p=0.402385 F=1.1529 df=4 d=0\\n  diff lag=-1 p=8.5e-05 fdr=0.000227\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 171 · 2026-05-18T21:27:49.855700+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nimport json\nwith open('/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s42/analysis/5method_leadlag.json') as f:\n    d = json.load(f)\nprint('s42 table7:', d.get('table7_row', 'N/A'))\nprint()\nfor p in d['pairs']:\n    cn, dn = p['canary'], p['downstream']\n    fwd = p['forward']\n    pg_p = fwd['perm_granger'].get('p_value', 'N/A')\n    pg_fdr = fwd['perm_granger'].get('p_fdr', 'N/A')\n    ty_p = fwd['ty_granger'].get('p_raw', 'N/A')\n    ty_df = fwd['ty_granger'].get('df_resid', 'N/A')\n    ty_d = fwd['ty_granger'].get('d_max', 'N/A')\n    print(f'{cn}->{dn}: PG p={pg_p} fdr={pg_fdr} TY p={ty_p} df={ty_df} d={ty_d}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nimport json\nwith open('/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s42/analysis/5method_leadlag.json') as f:\n    d = json.load(f)\nprint('s42 table7:', d.get('table7_row', 'N/A'))\nprint()\nfor p in d['pairs']:\n    cn, dn = p['canary'], p['downstream']\n    fwd = p['forward']\n    pg_p = fwd['perm_granger'].get('p_value', 'N/A')\n    pg_fdr = fwd['perm_granger'].get('p_fdr', 'N/A')\n    ty_p = fwd['ty_granger'].get('p_raw', 'N/A')\n    ty_df = fwd['ty_granger'].get('df_resid', 'N/A')\n    ty_d = fwd['ty_granger'].get('d_max', 'N/A')\n    print(f'{cn}->{dn}: PG p={pg_p} fdr={pg_fdr} TY p={ty_p} df={ty_df} d={ty_d}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-18T21:27:49.855836+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"s42 table7: N/A\\n\\ntoken_entropy->distinct_1: PG p=0.0006 fdr=N/A TY p=N/A df=1 d=2\\ntoken_entropy->distinct_2: PG p=0.002 fdr=N/A TY p=N/A df=7 d=0\\ntoken_entropy->distinct_3: PG p=0.0024 fdr=N/A TY p=N/A df=7 d=0\\ntoken_entropy->perplexity: PG p=0.4989 fdr=N/A TY p=N/A df=1 d=2\\nece->distinct_1: PG p=0.0006 fdr=N/A TY p=N/A df=1 d=2\\nece->distinct_2: PG p=0.001 fdr=N/A TY p=N/A df=1 d=2\\nece->distinct_3: PG p=0.001 fdr=N/A TY p=N/A df=1 d=2\\nece->perplexity: PG p=0.879624 fdr=N/A TY p=N/A df=1 d=2\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 173 · 2026-05-18T21:27:49.856011+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16/analysis/5method_leadlag.json",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16/analysis/5method_leadlag.json",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-18T21:27:49.856360+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"alpha\\\": 1.0,\\n  \\\"seed\\\": 43,\\n  \\\"n_generations\\\": 11,\\n  \\\"data_dir\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16\\\",\\n  \\\"methods\\\": [\\n    \\\"naive_xcorr\\\",\\n    \\\"diff_xcorr\\\",\\n    \\\"threshold_onset\\\",\\n    \\\"perm_granger\\\",\\n    \\\"ty_granger\\\"\\n  ],\\n  \\\"config\\\": {\\n    \\\"n_perm\\\": 5000,\\n    \\\"fdr_alpha\\\": 0.05,\\n    \\\"threshold_criterion\\\": \\\"3x_sigma_drift\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": 5,\\n          \\\"r\\\": 0.9351,\\n          \\\"p_value\\\": 0.006178,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.7029,\\n              \\\"p\\\": 0.119276\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.6577,\\n              \\\"p\\\": 0.10834\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.7471,\\n              \\\"p\\\": 0.033173\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.694,\\n              \\\"p\\\": 0.038075\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.6819,\\n              \\\"p\\\": 0.029843\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.4833,\\n              \\\"p\\\": 0.132086\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": -0.5597,\\n              \\\"p\\\": 0.092482\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\"
…[truncated 8626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-18T21:27:49.856590+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cat << 'PYEOF' > /root/autodl-tmp/distrib_canary_collapse/run_mmct_s43.py\n\"\"\"MMCT analysis for GPT-2m s43 bf16 using null from alpha=0.00.\"\"\"\nimport sys\nsys.path.insert(0, \"/root/autodl-tmp/distrib_canary_collapse\")\n\nfrom mmct.methods import METRIC_PAIRS, METHOD_NAMES\nfrom mmct.null_distribution import NullDistribution\nfrom mmct.consensus_test import MMCT\n\nNULL_DIRS = [\n    \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42\",\n    \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s43\",\n    \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s44\",\n]\n\n# s43 bf16 forward significance (from 5method analysis)\nS43_FWD = {\n    (\"token_entropy\", \"distinct_1\"): {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": True, \"perm_granger\": False, \"ty_granger\": False},\n    (\"token_entropy\", \"distinct_2\"): {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": True, \"perm_granger\": False, \"ty_granger\": False},\n    (\"token_entropy\", \"distinct_3\"): {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": True, \"perm_granger\": False, \"ty_granger\": False},\n    (\"token_entropy\", \"perplexity\"):  {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": True, \"perm_granger\": False, \"ty_granger\": False},\n    (\"ece\", \"distinct_1\"):            {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": True, \"perm_granger\": False, \"ty_granger\": False},\n    (\"ece\", \"distinct_2\"):            {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": True, \"perm_granger\": False, \"ty_granger\": False},\n    (\"ece\", \"distinct_3\"):            {\"naive_xcorr\": True, \"diff_xcorr\": False, \"threshold_onset\": True, \"perm_granger\": False, \"ty_granger\": False},\n    (\"ece\", \"perplexity\"):            {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": False, \"perm_granger\": True, \"ty_granger\": False},\n}\n\n# s43 bf16 reverse significance\nS43_REV = {\n    (\"token_entropy\", \"distinct_1\"): {\"naive_xcorr\": True, \"diff_xcorr\": False, \"threshold_onset\": False, \"perm_granger\": False, \"ty_granger\": False},\n    (\"token_entropy\", \"distinct_2\"): {\"naive_xcorr\": True, \"diff_xcorr\": False, \"threshold_onset\": False, \"perm_granger\": False, \"ty_granger\": False},\n    (\"token_entropy\", \"distinct_3\"): {\"naive_xcorr\": True, \"diff_xcorr\": False, \"threshold_onset\": False, \"perm_granger\": False, \"ty_granger\": False},\n    (\"token_entropy\", \"perplexity\"):  {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": True, \"perm_granger\": False, \"ty_granger\": False},\n    (\"ece\", \"distinct_1\"):            {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": False, \"perm_granger\": False, \"ty_granger\": False},\n    (\"ece\", \"distinct_2\"):            {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": False, \"perm_granger\": False, \"ty_granger\": False},\n    (\"ece\", \"distinct_3\"):            {\"naive_xcorr\": True, \"diff_xcorr\": False, \"threshold_onset\": False, \"perm_granger\": False, \"ty_granger\": False},\n    (\"ece\", \"perplexity\"):            {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": False, \"perm_granger\": False, \"ty_granger\": False},\n}\n\nprint(\"Building null distribution...\")\nnull_dist = NullDistribution(NULL_DIRS, n_bootstrap=10000, seed=42)\nprint(f\"  Null observations: {len(null_dist.null_uniform_fwd)}\")\nprint(f\"  Global FPR: {null_dist.global_fpr}\")\n\nfor mode_name, weighted, bidirectional in [\n    (\"weighted_forward\", True, False),\n]:\n    print(f\"\\n--- Mode: {mode_name} ---\")\n    mmct = MMCT(null_dist, weighted=weighted, bidirectional=bidirectional)\n    n_sig = 0\n    for canary, downstream in METRIC_PAIRS:\n        fwd_sig = S43_FWD[(canary, downstream)]\n        pair_key = (canary, downstream)\n        if weighted:\n            weights = null_dist.get_weights(pair_key)\n            score = null_dist.consensus_score_weighted(fwd_sig, weights)\n        else:\n            score = null_dist.consensus_score_uniform(fwd_sig)\n        p, ci_lo, ci_hi = null_dist.p_value(score, weighted=weighted, direction=\"forward\")\n        sig = p < 0.05\n        n_sig += sig\n        print(f\"  {canary}->{downstream}: score={score:.4f} p={p:.4f} [{ci_lo:.4f},{ci_hi:.4f}] {'SIG' if sig else ''}\")\n    print(f\"\\n  MMCT {mode_name}: {n_sig}/8 significant\")\n\nPYEOF\necho \"Script written\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat << 'PYEOF' > /root/autodl-tmp/distrib_canary_collapse/run_mmct_s43.py\n\"\"\"MMCT analysis for GPT-2m s43 bf16 using null from alpha=0.00.\"\"\"\nimport sys\nsys.path.insert(0, \"/root/autodl-tmp/distrib_canary_collapse\")\n\nfrom mmct.methods import METRIC_PAIRS, METHOD_NAMES\nfrom mmct.null_distribution import NullDistribution\nfrom mmct.consensus_test import MMCT\n\nNULL_DIRS = [\n    \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42\",\n    \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s43\",\n    \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s44\",\n]\n\n# s43 bf16 forward significance (from 5method analysis)\nS43_FWD = {\n    (\"token_entropy\", \"distinct_1\"): {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": True, \"perm_granger\": False, \"ty_granger\": False},\n    (\"token_entropy\", \"distinct_2\"): {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": True, \"perm_granger\": False, \"ty_granger\": False},\n    (\"token_entropy\", \"distinct_3\"): {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": True, \"perm_granger\": False, \"ty_granger\": False},\n    (\"token_entropy\", \"perplexity\"):  {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": True, \"perm_granger\": False, \"ty_granger\": False},\n    (\"ece\", \"distinct_1\"):            {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": True, \"perm_granger\": False, \"ty_granger\": False},\n    (\"ece\", \"distinct_2\"):            {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": True, \"perm_granger\": False, \"ty_granger\": False},\n    (\"ece\", \"distinct_3\"):            {\"naive_xcorr\": True, \"diff_xcorr\": False, \"threshold_onset\": True, \"perm_granger\": False, \"ty_granger\": False},\n    (\"ece\", \"perplexity\"):            {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": False, \"perm_granger\": True, \"ty_granger\": False},\n}\n\n# s43 bf16 reverse significance\nS43_REV = {\n    (\"token_entropy\", \"distinct_1\"): {\"naive_xcorr\": True, \"diff_xcorr\": False, \"threshold_onset\": False, \"perm_granger\": False, \"ty_granger\": False},\n    (\"token_entropy\", \"distinct_2\"): {\"naive_xcorr\": True, \"diff_xcorr\": False, \"threshold_onset\": False, \"perm_granger\": False, \"ty_granger\": False},\n    (\"token_entropy\", \"distinct_3\"): {\"naive_xcorr\": True, \"diff_xcorr\": False, \"threshold_onset\": False, \"perm_granger\": False, \"ty_granger\": False},\n    (\"token_entropy\", \"perplexity\"):  {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": True, \"perm_granger\": False, \"ty_granger\": False},\n    (\"ece\", \"distinct_1\"):            {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": False, \"perm_granger\": False, \"ty_granger\": False},\n    (\"ece\", \"distinct_2\"):            {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": False, \"perm_granger\": False, \"ty_granger\": False},\n    (\"ece\", \"distinct_3\"):            {\"naive_xcorr\": True, \"diff_xcorr\": False, \"threshold_onset\": False, \"perm_granger\": False, \"ty_granger\": False},\n    (\"ece\", \"perplexity\"):            {\"naive_xcorr\": True, \"diff_xcorr\": True, \"threshold_onset\": False, \"perm_granger\": False, \"ty_granger\": False},\n}\n\nprint(\"Building null distribution...\")\nnull_dist = NullDistribution(NULL_DIRS, n_bootstrap=10000, seed=42)\nprint(f\"  Null observations: {len(null_dist.null_uniform_fwd)}\")\nprint(f\"  Global FPR: {null_dist.global_fpr}\")\n\nfor mode_name, weighted, bidirectional in [\n    (\"weighted_forward\", True, False),\n]:\n    print(f\"\\n--- Mode: {mode_name} ---\")\n    mmct = MMCT(null_dist, weighted=weighted, bidirectional=bidirectional)\n    n_sig = 0\n    for canary, downstream in METRIC_PAIRS:\n        fwd_sig = S43_FWD[(canary, downstream)]\n        pair_key = (canary, downstream)\n        if weighted:\n            weights = null_dist.get_weights(pair_key)\n            score = null_dist.consensus_score_weighted(fwd_sig, weights)\n        else:\n            score = null_dist.consensus_score_uniform(fwd_sig)\n        p, ci_lo, ci_hi = null_dist.p_value(score, weighted=weighted, direction=\"forward\")\n        sig = p < 0.05\n        n_sig += sig\n        print(f\"  {canary}->{downstream}: score={score:.4f} p={p:.4f} [{ci_lo:.4f},{ci_hi:.4f}] {'SIG' if sig else ''}\")\n    print(f\"\\n  MMCT {mode_name}: {n_sig}/8 significant\")\n\nPYEOF\necho \"Script written\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-18T21:27:49.856763+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 177 · 2026-05-18T21:27:49.856976+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && sed -i 's/\"threshold_onset\": False, \"perm_granger\": True/\"threshold_onset\": True, \"perm_granger\": True/' run_mmct_s43.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && sed -i 's/\"threshold_onset\": False, \"perm_granger\": True/\"threshold_onset\": True, \"perm_granger\": True/' run_mmct_s43.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 178 · 2026-05-18T21:27:49.857122+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 179 · 2026-05-18T21:27:49.857293+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python run_mmct_s43.py",
  "account": "root",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python run_mmct_s43.py",
    "account": "root",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 180 · 2026-05-18T21:27:49.857447+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Building null distribution...\\n  Null observations: 24\\n  Global FPR: {'naive_xcorr': 0.9583333333333334, 'diff_xcorr': 0.5, 'threshold_onset': 0.20833333333333334, 'perm_granger': 0.125, 'ty_granger': 0.08333333333333333}\\n\\n--- Mode: weighted_forward ---\\n  token_entropy->distinct_1: score=0.4988 p=0.0400 [0.0400,0.0400] SIG\\n  token_entropy->distinct_2: score=0.4976 p=0.0400 [0.0400,0.0400] SIG\\n  token_entropy->distinct_3: score=0.5012 p=0.0400 [0.0400,0.0400] SIG\\n  token_entropy->perplexity: score=0.3377 p=0.0400 [0.0400,0.0400] SIG\\n  ece->distinct_1: score=0.0244 p=0.1600 [0.0400,0.2800] \\n  ece->distinct_2: score=0.3421 p=0.0400 [0.0400,0.0400] SIG\\n  ece->distinct_3: score=0.0193 p=0.2000 [0.0800,0.3600] \\n  ece->perplexity: score=0.7509 p=0.0400 [0.0400,0.0400] SIG\\n\\n  MMCT weighted_forward: 6/8 significant\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 181 · 2026-05-18T21:27:49.857633+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "gen_gpt2m_a100_s43_bf16",
  "field": "metrics",
  "value": "{'token_entropy_gen0': 3.6021, 'token_entropy_gen10': 3.0035, 'token_entropy_delta_pct': -16.6, 'distinct_1_gen0': 0.1092, 'distinct_1_gen10': 0.0724, 'distinct_1_delta_pct': -33.7, 'distinct_2_gen0': 0.5665, 'distinct_2_gen10': 0.3422, 'distinct_2_delta_pct': -39.6, 'distinct_3_gen0': 0.8652, 'distinct_3_gen10': 0.5756, 'distinct_3_delta_pct': -33.5, 'ece_gen0': 0.0111, 'ece_gen10': 0.0716, 'ece_delta_pct': 547.9, 'perplexity_gen0': 32.91, 'perplexity_gen10': 55.49, 'perplexity_delta_pct': 68.6, 'mauve_gen0': 0.0318, 'mauve_gen10': 0.0227, 'mauve_delta_pct': -28.7, 'naive': '8/8', 'diff': '7/8', 'thresh': '8/8', 'pg_fwd': '1/8', 'pg_rev': '0/8', 'ty': '0/8', 'k_gte4': '1/8', 'mmct_weighted_fwd': '6/8', 'n_perm': 5000, 'xcorr_lag': 5, 'granger_lag': 1, 'cross_seed_note': 'CAUTION: s42 was fp32 (entropy drift -86.6%), s43 is bf16 (entropy drift -16.6%). NOT a fair cross-seed comparison. bf16 dramatically reduces collapse severity, causing PG/TY to lose power (PG_fwd 1/8 vs 6/8, TY 0/8 vs 5/8). MMCT partially recovers signal (6/8) via FPR-inverse weighting of naive+diff+thresh consensus. K>=4 drops to 1/8 (ece->ppl only, a spurious channel).', 'precision_note': 'bf16 mixed precision; collapse trajectory is qualitatively similar but quantitatively much milder than fp32 s42'}",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "gen_gpt2m_a100_s43_bf16",
    "field": "metrics",
    "value": "{'token_entropy_gen0': 3.6021, 'token_entropy_gen10': 3.0035, 'token_entropy_delta_pct': -16.6, 'distinct_1_gen0': 0.1092, 'distinct_1_gen10': 0.0724, 'distinct_1_delta_pct': -33.7, 'distinct_2_gen0': 0.5665, 'distinct_2_gen10': 0.3422, 'distinct_2_delta_pct': -39.6, 'distinct_3_gen0': 0.8652, 'distinct_3_gen10': 0.5756, 'distinct_3_delta_pct': -33.5, 'ece_gen0': 0.0111, 'ece_gen10': 0.0716, 'ece_delta_pct': 547.9, 'perplexity_gen0': 32.91, 'perplexity_gen10': 55.49, 'perplexity_delta_pct': 68.6, 'mauve_gen0': 0.0318, 'mauve_gen10': 0.0227, 'mauve_delta_pct': -28.7, 'naive': '8/8', 'diff': '7/8', 'thresh': '8/8', 'pg_fwd': '1/8', 'pg_rev': '0/8', 'ty': '0/8', 'k_gte4': '1/8', 'mmct_weighted_fwd': '6/8', 'n_perm': 5000, 'xcorr_lag': 5, 'granger_lag': 1, 'cross_seed_note': 'CAUTION: s42 was fp32 (entropy drift -86.6%), s43 is bf16 (entropy drift -16.6%). NOT a fair cross-seed comparison. bf16 dramatically reduces collapse severity, causing PG/TY to lose power (PG_fwd 1/8 vs 6/8, TY 0/8 vs 5/8). MMCT partially recovers signal (6/8) via FPR-inverse weighting of naive+diff+thresh consensus. K>=4 drops to 1/8 (ece->ppl only, a spurious channel).', 'precision_note': 'bf16 mixed precision; collapse trajectory is qualitatively similar but quantitatively much milder than fp32 s42'}",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 182 · 2026-05-18T21:27:49.857847+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"gen_gpt2m_a100_s43_bf16\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:25:55.336Z\", \"updated_at\": \"2026-05-18T21:27:02.861Z\", \"spec\": {\"command\": \"python -u iterative_train.py --model_name openai-community/gpt2-medium --seed 43 --data_dir data/wikitext103_5k --steps_per_gen 5000 --num_generations 10 --synthetic_ratio 1.0 --bf16 --output_dir results/generalize/gpt2m_wiki_a100_s43_bf16\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:1\"], \"pid\": \"16116\", \"log_path\": \"~/runs/distrib_canary_collapse/gen_gpt2m_a100_s43_bf16.log\", \"submitted_at\": \"2026-05-18T17:25:55.193Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"openai-community/gpt2-medium\", \"seed\": 43, \"data_path\": \"data/wikitext103_5k\", \"data_count\": 5000, \"wall_clock_seconds\": 12444.6, \"gpu_hours\": 3.46, \"checkpoint_path\": \"results/generalize/gpt2m_wiki_a100_s43_bf16\"}, \"hypothesis\": \"GPT-2-medium multi-seed s43: GPT-2-medium × WikiText-103 × α=1.0 × seed=43. Validates s42 cross-architecture results (K≥4=6/8) are reproducible.\", \"reproduce\": {\"finished_at\": \"2026-05-18T20:53:18.007Z\"}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T20:53:19.746Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-18T20:53:22.622800+00:00\"}]}, \"metrics\": {\"token_entropy_gen0\": 3.6021, \"token_entropy_gen10\": 3.0035, \"token_entropy_delta_pct\": -16.6, \"distinct_1_gen0\": 0.1092, \"distinct_1_gen10\": 0.0724, \"distinct_1_delta_pct\": -33.7, \"distinct_2_gen0\": 0.5665, \"distinct_2_gen10\": 0.3422, \"distinct_2_delta_pct\": -39.6, \"distinct_3_gen0\": 0.8652, \"distinct_3_gen10\": 0.5756, \"distinct_3_delta_pct\": -33.5, \"ece_gen0\": 0.0111, \"ece_gen10\": 0.0716, \"ece_delta_pct\": 547.9, \"perplexi
…[truncated 988 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 183 · 2026-05-18T21:27:49.858095+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "gpt2m_s43_bf16_5method_leadlag",
  "type": "data",
  "description": "5-method lead-lag analysis for GPT-2-medium s43 bf16: Table 7 row data. Naive=8/8, Diff=7/8, Thresh=8/8, PG_fwd=1/8, PG_rev=0/8, TY=0/8, K≥4=1/8, MMCT=6/8. Remote path: westd-17855:/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16/analysis/5method_leadlag.json",
  "project": "distrib_canary_collapse",
  "exp_id": "gen_gpt2m_a100_s43_bf16",
  "content": "{\n  \"table7_row\": {\n    \"variation\": \"Architecture\",\n    \"model_dataset\": \"GPT-2-medium / Wiki (s43, bf16)\",\n    \"naive\": \"8/8\",\n    \"diff_xcorr\": \"7/8\",\n    \"threshold\": \"8/8\",\n    \"pg_fwd\": \"1/8\",\n    \"pg_rev\": \"0/8\",\n    \"ty\": \"0/8\",\n    \"k_gte4\": \"1/8\",\n    \"mmct\": \"6/8\"\n  },\n  \"cross_seed_comparison\": {\n    \"s42_fp32\": {\"naive\": \"8/8\", \"diff\": \"8/8\", \"thresh\": \"8/8\", \"pg_fwd\": \"6/8\", \"pg_rev\": \"3/8\", \"ty\": \"5/8\", \"k_gte4\": \"6/8\", \"mmct\": \"8/8\"},\n    \"s43_bf16\": {\"naive\": \"8/8\", \"diff\": \"7/8\", \"thresh\": \"8/8\", \"pg_fwd\": \"1/8\", \"pg_rev\": \"0/8\", \"ty\": \"0/8\", \"k_gte4\": \"1/8\", \"mmct\": \"6/8\"},\n    \"confound\": \"s42=fp32 vs s43=bf16, not a fair cross-seed comparison\",\n    \"entropy_drift_s42\": \"-86.6%\",\n    \"entropy_drift_s43\": \"-16.6%\",\n    \"conclusion\": \"bf16 reduces collapse severity ~5x, PG/TY lose statistical power. MMCT recovers 6/8 via FPR-inverse weighting.\"\n  },\n  \"mmct_detail\": {\n    \"mode\": \"weighted_forward\",\n    \"significant_pairs\": [\"token_entropy->distinct_1\", \"token_entropy->distinct_2\", \"token_entropy->distinct_3\", \"token_entropy->perplexity\", \"ece->distinct_2\", \"ece->perplexity\"],\n    \"non_significant_pairs\": [\"ece->distinct_1\", \"ece->distinct_3\"],\n    \"null_source\": \"a000_s42/s43/s44 (3 seeds x 8 pairs = 24 null obs)\"\n  },\n  \"metrics_summary\": {\n    \"gen0\": {\"token_entropy\": 3.6021, \"distinct_1\": 0.1092, \"ece\": 0.0111, \"perplexity\": 32.91},\n    \"gen10\": {\"token_entropy\": 3.0035, \"distinct_1\": 0.0724, \"ece\": 0.0716, \"perplexity\": 55.49},\n    \"drift_pct\": {\"token_entropy\": -16.6, \"distinct_1\": -33.7, \"distinct_2\": -39.6, \"distinct_3\": -33.5, \"ece\": 547.9, \"perplexity\": 68.6}\n  }\n}",
  "content_filename": "gpt2m_s43_bf16_table7_analysis.json",
  "tags": "['table7', 'lead-lag', 'mmct', 'gpt2m', 's43', 'bf16', 'cross-seed']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "gpt2m_s43_bf16_5method_leadlag",
    "type": "data",
    "description": "5-method lead-lag analysis for GPT-2-medium s43 bf16: Table 7 row data. Naive=8/8, Diff=7/8, Thresh=8/8, PG_fwd=1/8, PG_rev=0/8, TY=0/8, K≥4=1/8, MMCT=6/8. Remote path: westd-17855:/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16/analysis/5method_leadlag.json",
    "project": "distrib_canary_collapse",
    "exp_id": "gen_gpt2m_a100_s43_bf16",
    "content": "{\n  \"table7_row\": {\n    \"variation\": \"Architecture\",\n    \"model_dataset\": \"GPT-2-medium / Wiki (s43, bf16)\",\n    \"naive\": \"8/8\",\n    \"diff_xcorr\": \"7/8\",\n    \"threshold\": \"8/8\",\n    \"pg_fwd\": \"1/8\",\n    \"pg_rev\": \"0/8\",\n    \"ty\": \"0/8\",\n    \"k_gte4\": \"1/8\",\n    \"mmct\": \"6/8\"\n  },\n  \"cross_seed_comparison\": {\n    \"s42_fp32\": {\"naive\": \"8/8\", \"diff\": \"8/8\", \"thresh\": \"8/8\", \"pg_fwd\": \"6/8\", \"pg_rev\": \"3/8\", \"ty\": \"5/8\", \"k_gte4\": \"6/8\", \"mmct\": \"8/8\"},\n    \"s43_bf16\": {\"naive\": \"8/8\", \"diff\": \"7/8\", \"thresh\": \"8/8\", \"pg_fwd\": \"1/8\", \"pg_rev\": \"0/8\", \"ty\": \"0/8\", \"k_gte4\": \"1/8\", \"mmct\": \"6/8\"},\n    \"confound\": \"s42=fp32 vs s43=bf16, not a fair cross-seed comparison\",\n    \"entropy_drift_s42\": \"-86.6%\",\n    \"entropy_drift_s43\": \"-16.6%\",\n    \"conclusion\": \"bf16 reduces collapse severity ~5x, PG/TY lose statistical power. MMCT recovers 6/8 via FPR-inverse weighting.\"\n  },\n  \"mmct_detail\": {\n    \"mode\": \"weighted_forward\",\n    \"significant_pairs\": [\"token_entropy->distinct_1\", \"token_entropy->distinct_2\", \"token_entropy->distinct_3\", \"token_entropy->perplexity\", \"ece->distinct_2\", \"ece->perplexity\"],\n    \"non_significant_pairs\": [\"ece->distinct_1\", \"ece->distinct_3\"],\n    \"null_source\": \"a000_s42/s43/s44 (3 seeds x 8 pairs = 24 null obs)\"\n  },\n  \"metrics_summary\": {\n    \"gen0\": {\"token_entropy\": 3.6021, \"distinct_1\": 0.1092, \"ece\": 0.0111, \"perplexity\": 32.91},\n    \"gen10\": {\"token_entropy\": 3.0035, \"distinct_1\": 0.0724, \"ece\": 0.0716, \"perplexity\": 55.49},\n    \"drift_pct\": {\"token_entropy\": -16.6, \"distinct_1\": -33.7, \"distinct_2\": -39.6, \"distinct_3\": -33.5, \"ece\": 547.9, \"perplexity\": 68.6}\n  }\n}",
    "content_filename": "gpt2m_s43_bf16_table7_analysis.json",
    "tags": "['table7', 'lead-lag', 'mmct', 'gpt2m', 's43', 'bf16', 'cross-seed']"
  }
}
```

</details>

---

### Tool result

_source line 184 · 2026-05-18T21:27:49.858300+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'table7_row': {'variatio...9, 'perplexity': 68.6}}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 185 · 2026-05-18T21:27:49.858459+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "gpt2m_s43_bf16_5method_leadlag",
  "type": "data",
  "description": "5-method lead-lag + MMCT analysis for GPT-2-medium s43 bf16: Table 7 row. Naive=8/8, Diff=7/8, Thresh=8/8, PG_fwd=1/8, PG_rev=0/8, TY=0/8, K≥4=1/8, MMCT=6/8.",
  "project": "distrib_canary_collapse",
  "exp_id": "gen_gpt2m_a100_s43_bf16",
  "content": "{\"table7_row\":{\"variation\":\"Architecture\",\"model_dataset\":\"GPT-2-medium / Wiki (s43, bf16)\",\"naive\":\"8/8\",\"diff_xcorr\":\"7/8\",\"threshold\":\"8/8\",\"pg_fwd\":\"1/8\",\"pg_rev\":\"0/8\",\"ty\":\"0/8\",\"k_gte4\":\"1/8\",\"mmct\":\"6/8\"},\"cross_seed_comparison\":{\"s42_fp32\":{\"naive\":\"8/8\",\"diff\":\"8/8\",\"thresh\":\"8/8\",\"pg_fwd\":\"6/8\",\"pg_rev\":\"3/8\",\"ty\":\"5/8\",\"k_gte4\":\"6/8\",\"mmct\":\"8/8\"},\"s43_bf16\":{\"naive\":\"8/8\",\"diff\":\"7/8\",\"thresh\":\"8/8\",\"pg_fwd\":\"1/8\",\"pg_rev\":\"0/8\",\"ty\":\"0/8\",\"k_gte4\":\"1/8\",\"mmct\":\"6/8\"},\"confound\":\"s42=fp32 vs s43=bf16\",\"entropy_drift_s42\":\"-86.6%\",\"entropy_drift_s43\":\"-16.6%\"},\"mmct_detail\":{\"mode\":\"weighted_forward\",\"sig_pairs\":[\"te->d1\",\"te->d2\",\"te->d3\",\"te->ppl\",\"ece->d2\",\"ece->ppl\"],\"non_sig_pairs\":[\"ece->d1\",\"ece->d3\"]}}",
  "content_filename": "gpt2m_s43_bf16_table7_analysis.json",
  "tags": "['table7', 'lead-lag', 'mmct', 'gpt2m', 's43', 'bf16']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "gpt2m_s43_bf16_5method_leadlag",
    "type": "data",
    "description": "5-method lead-lag + MMCT analysis for GPT-2-medium s43 bf16: Table 7 row. Naive=8/8, Diff=7/8, Thresh=8/8, PG_fwd=1/8, PG_rev=0/8, TY=0/8, K≥4=1/8, MMCT=6/8.",
    "project": "distrib_canary_collapse",
    "exp_id": "gen_gpt2m_a100_s43_bf16",
    "content": "{\"table7_row\":{\"variation\":\"Architecture\",\"model_dataset\":\"GPT-2-medium / Wiki (s43, bf16)\",\"naive\":\"8/8\",\"diff_xcorr\":\"7/8\",\"threshold\":\"8/8\",\"pg_fwd\":\"1/8\",\"pg_rev\":\"0/8\",\"ty\":\"0/8\",\"k_gte4\":\"1/8\",\"mmct\":\"6/8\"},\"cross_seed_comparison\":{\"s42_fp32\":{\"naive\":\"8/8\",\"diff\":\"8/8\",\"thresh\":\"8/8\",\"pg_fwd\":\"6/8\",\"pg_rev\":\"3/8\",\"ty\":\"5/8\",\"k_gte4\":\"6/8\",\"mmct\":\"8/8\"},\"s43_bf16\":{\"naive\":\"8/8\",\"diff\":\"7/8\",\"thresh\":\"8/8\",\"pg_fwd\":\"1/8\",\"pg_rev\":\"0/8\",\"ty\":\"0/8\",\"k_gte4\":\"1/8\",\"mmct\":\"6/8\"},\"confound\":\"s42=fp32 vs s43=bf16\",\"entropy_drift_s42\":\"-86.6%\",\"entropy_drift_s43\":\"-16.6%\"},\"mmct_detail\":{\"mode\":\"weighted_forward\",\"sig_pairs\":[\"te->d1\",\"te->d2\",\"te->d3\",\"te->ppl\",\"ece->d2\",\"ece->ppl\"],\"non_sig_pairs\":[\"ece->d1\",\"ece->d3\"]}}",
    "content_filename": "gpt2m_s43_bf16_table7_analysis.json",
    "tags": "['table7', 'lead-lag', 'mmct', 'gpt2m', 's43', 'bf16']"
  }
}
```

</details>

---

### Tool result

_source line 186 · 2026-05-18T21:27:49.858601+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'table7_row': {'variatio...['ece->d1', 'ece->d3']}}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 187 · 2026-05-18T21:27:49.858727+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "gpt2m_s43_bf16_table7_analysis",
  "type": "data",
  "description": "5-method lead-lag + MMCT analysis for GPT-2-medium s43 bf16: Table 7 row. Naive=8/8, Diff=7/8, Thresh=8/8, PG_fwd=1/8, PG_rev=0/8, TY=0/8, K>=4=1/8, MMCT=6/8.",
  "project": "distrib_canary_collapse",
  "exp_id": "gen_gpt2m_a100_s43_bf16",
  "content": "Table 7 Row: GPT-2-medium / Wiki (s43, bf16)\n\nNaive=8/8 | Diff.XCorr=7/8 | Threshold=8/8 | PermG(fwd)=1/8 | PermG(rev)=0/8 | TY=0/8 | K>=4/5=1/8 | MMCT=6/8\n\nCross-seed comparison (s42 fp32 vs s43 bf16):\n  s42 fp32: 8/8 | 8/8 | 8/8 | 6/8 | 3/8 | 5/8 | 6/8 | 8/8\n  s43 bf16: 8/8 | 7/8 | 8/8 | 1/8 | 0/8 | 0/8 | 1/8 | 6/8\n  CONFOUND: s42=fp32, s43=bf16 (not fair cross-seed)\n  Entropy drift: s42=-86.6%, s43=-16.6%\n\nMMCT detail (weighted_forward, 6/8 sig):\n  SIG: te->d1, te->d2, te->d3, te->ppl, ece->d2, ece->ppl\n  non-sig: ece->d1 (p=0.16), ece->d3 (p=0.20)\n\nMetrics:\n  gen0:  entropy=3.602, d1=0.1092, ece=0.0111, ppl=32.91\n  gen10: entropy=3.004, d1=0.0724, ece=0.0716, ppl=55.49\n  Drift: entropy=-16.6%, d1=-33.7%, d2=-39.6%, d3=-33.5%, ece=+548%, ppl=+68.6%\n\nSource: westd-17855:/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16/analysis/5method_leadlag.json",
  "content_filename": "gpt2m_s43_bf16_table7_analysis.txt",
  "tags": "['table7', 'lead-lag', 'mmct', 'gpt2m', 's43', 'bf16']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "gpt2m_s43_bf16_table7_analysis",
    "type": "data",
    "description": "5-method lead-lag + MMCT analysis for GPT-2-medium s43 bf16: Table 7 row. Naive=8/8, Diff=7/8, Thresh=8/8, PG_fwd=1/8, PG_rev=0/8, TY=0/8, K>=4=1/8, MMCT=6/8.",
    "project": "distrib_canary_collapse",
    "exp_id": "gen_gpt2m_a100_s43_bf16",
    "content": "Table 7 Row: GPT-2-medium / Wiki (s43, bf16)\n\nNaive=8/8 | Diff.XCorr=7/8 | Threshold=8/8 | PermG(fwd)=1/8 | PermG(rev)=0/8 | TY=0/8 | K>=4/5=1/8 | MMCT=6/8\n\nCross-seed comparison (s42 fp32 vs s43 bf16):\n  s42 fp32: 8/8 | 8/8 | 8/8 | 6/8 | 3/8 | 5/8 | 6/8 | 8/8\n  s43 bf16: 8/8 | 7/8 | 8/8 | 1/8 | 0/8 | 0/8 | 1/8 | 6/8\n  CONFOUND: s42=fp32, s43=bf16 (not fair cross-seed)\n  Entropy drift: s42=-86.6%, s43=-16.6%\n\nMMCT detail (weighted_forward, 6/8 sig):\n  SIG: te->d1, te->d2, te->d3, te->ppl, ece->d2, ece->ppl\n  non-sig: ece->d1 (p=0.16), ece->d3 (p=0.20)\n\nMetrics:\n  gen0:  entropy=3.602, d1=0.1092, ece=0.0111, ppl=32.91\n  gen10: entropy=3.004, d1=0.0724, ece=0.0716, ppl=55.49\n  Drift: entropy=-16.6%, d1=-33.7%, d2=-39.6%, d3=-33.5%, ece=+548%, ppl=+68.6%\n\nSource: westd-17855:/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16/analysis/5method_leadlag.json",
    "content_filename": "gpt2m_s43_bf16_table7_analysis.txt",
    "tags": "['table7', 'lead-lag', 'mmct', 'gpt2m', 's43', 'bf16']"
  }
}
```

</details>

---

### Tool result

_source line 188 · 2026-05-18T21:27:49.858877+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260518_3e2473\", \"name\": \"gpt2m_s43_bf16_table7_analysis\", \"type\": \"data\", \"description\": \"5-method lead-lag + MMCT analysis for GPT-2-medium s43 bf16: Table 7 row. Naive=8/8, Diff=7/8, Thresh=8/8, PG_fwd=1/8, PG_rev=0/8, TY=0/8, K>=4=1/8, MMCT=6/8.\", \"path\": \"projects/distrib_canary_collapse/artifacts/gen_gpt2m_a100_s43_bf16/data/gpt2m_s43_bf16_table7_analysis.txt\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": \"gen_gpt2m_a100_s43_bf16\", \"skill\": \"\", \"created_at\": \"2026-05-18T21:27:38.155401+00:00\", \"tags\": [\"table7\", \"lead-lag\", \"mmct\", \"gpt2m\", \"s43\", \"bf16\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 189 · 2026-05-18T21:27:49.859036+00:00_

完成。汇总：

## Table 7 Row: GPT-2-medium / Wiki (s43, bf16)

| | Naive | Diff. XCorr | Threshold | PermG (fwd) | PermG (rev) | TY | K≥4/5 | MMCT |
|---|---|---|---|---|---|---|---|---|
| **s43 bf16** | 8/8 | 7/8 | 8/8 | 1/8 | 0/8 | 0/8 | 1/8 | **6/8** |
| s42 fp32 | 8/8 | 8/8 | 8/8 | 6/8 | 3/8 | 5/8 | 6/8 | 8/8 |

**关键发现：**

1. **K≥4 共识从 6/8 暴跌到 1/8**（唯一通过的是 ece→perplexity，属于 spurious channel）
2. **MMCT 恢复到 6/8**，因为 FPR-inverse weighting 给予 naive+diff+thresh 三法共识足够权重
3. **根因是 fp32 vs bf16 混淆因子**：s42(fp32) entropy drift=-86.6%, s43(bf16) entropy drift=-16.6%。bf16 将 collapse 严重程度降低约 5 倍，PG/TY 在弱信号下失去检验力
4. 非 parametric 方法（naive, threshold）对信号强度不敏感，8/8 保持稳定
5. **不建议直接纳入 Table 7 作为 cross-seed 行**，因为 fp32/bf16 是实验条件差异而非 seed variance

数据已写入 registry（metrics 字段）并注册为 artifact。5method_leadlag.json 保存在 westd-17855 上。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_gpt2m_s43_bf16_leadlag_20260518T211603"
}
```

</details>

---
