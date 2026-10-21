# analysis phase diagram t15 a050 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410.jsonl`
- **Structured JSON:** [`20f2a94a932d90f25929.json`](../../sessions/20/20f2a94a932d90f25929.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

53 recorded events

### Tool call

_source line 1 · 2026-05-21T17:58:58.663520+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__update_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__update_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T17:58:58.663871+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T17:58:58.664045+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "tail -50 ~/runs/distrib_canary_collapse/phase_diagram_t15_a050_s42_fp32.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "tail -50 ~/runs/distrib_canary_collapse/phase_diagram_t15_a050_s42_fp32.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T17:58:58.664185+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t15_a050_s42_fp32/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t15_a050_s42_fp32/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T17:58:58.664429+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r 28%|██▊       | 1400/5000 [03:02<07:47,  7.69it/s]\\r 28%|██▊       | 1401/5000 [03:02<07:47,  7.69it/s]\\r 28%|██▊       | 1402/5000 [03:02<07:47,  7.69it/s]\\r 28%|██▊       | 1403/5000 [03:02<07:48,  7.69it/s]\\r 28%|██▊       | 1404/5000 [03:02<07:47,  7.68it/s]\\r 28%|██▊       | 1405/5000 [03:02<07:47,  7.69it/s]\\r 28%|██▊       | 1406/5000 [03:02<07:47,  7.69it/s]\\r 28%|██▊       | 1407/5000 [03:02<07:47,  7.68it/s]\\r 28%|██▊       | 1408/5000 [03:03<07:47,  7.69it/s]\\r 28%|██▊       | 1409/5000 [03:03<07:47,  7.69it/s]\\r 28%|██▊       | 1410/5000 [03:03<07:46,  7.69it/s]\\r 28%|██▊       | 1411/5000 [03:03<07:46,  7.70it/s]\\r 28%|██▊       | 1412/5000 [03:03<07:46,  7.69it/s]\\r 28%|██▊       | 1413/5000 [03:03<07:46,  7.69it/s]\\r 28%|██▊       | 1414/5000 [03:03<07:46,  7.69it/s]\\r 28%|██▊       | 1415/5000 [03:04<07:46,  7.69it/s]\\r 28%|██▊       | 1416/5000 [03:04<07:46,  7.69it/s]\\r 28%|██��       | 1417/5000 [03:04<07:45,  7.69it/s]\\r 28%|██▊       | 1418/5000 [03:04<07:45,  7.69it/s]\\r 28%|██▊       | 1419/5000 [03:04<07:45,  7.69it/s]\\r 28%|██▊       | 1420/5000 [03:04<07:45,  7.69it/s]\\r 28%|██▊       | 1421/5000 [03:04<07:45,  7.69it/s]\\r 28%|██▊       | 1422/5000 [03:04<07:45,  7.69it/s]\\r 28%|██▊       | 1423/5000 [03:05<07:44,  7.69it/s]\\r 28%|██▊       | 1424/5000 [03:05<07:44,  7.69it/s]\\r 28%|██▊       | 1425/5000 [03:05<07:45,  7.69it/s]\\r 29%|██▊       | 1426/5000 [03:05<07:44,  7.69it/s]\\r 29%|██▊       | 1427/5000 [03:05<07:45,  7.68it/s]\\r 29%|██▊       | 1428/5000 [03:05<07:44,  7.69it/s]\\r 29%|██▊       | 1429/5000 [03:05<07:44,  7.68it/s]\\r 29%|██▊       | 1430/5000 [03:05<07:44,  7.69it/s]\\r 29%|██▊       | 1431/5000 [03:06<07:44,  7.68it/s]\\r 29%|██▊       | 1432/5000 [03:06<07:44,  7.69it/s]\\r 29%|██▊       | 1433/5000 [03:06<07:44,  7.69it/s]\\r 29%|██▊       | 1434/5000 [03:06<07:44,  7.68it/s]\\r 29%|██▊       | 1435/5000 [03:06<07:43,  7.68it/s
…[truncated 6481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T17:58:58.664607+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"EXIT_CODE\\nall_metrics.json\\nconfig.json\\ngen_0\\ngen_1\\ngen_10\\ngen_11\\ngen_12\\ngen_13\\ngen_14\\ngen_15\\ngen_2\\ngen_3\\ngen_4\\ngen_5\\ngen_6\\ngen_7\\ngen_8\\ngen_9\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T17:58:58.664751+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find existing analysis template",
  "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/, I need to find an existing 5-method lead-lag analysis script (run_analysis.py) that was used for a previous phase_diagram experiment (e.g., t15_a045, t05_a050, or similar). Search in the artifacts/ directory for run_analysis.py files. I need the full path to the most relevant one so I can use it as a template. Search breadth: medium."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find existing analysis template",
    "prompt": "In the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/, I need to find an existing 5-method lead-lag analysis script (run_analysis.py) that was used for a previous phase_diagram experiment (e.g., t15_a045, t05_a050, or similar). Search in the artifacts/ directory for run_analysis.py files. I need the full path to the most relevant one so I can use it as a template. Search breadth: medium."
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T17:58:58.664908+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/**/run_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/**/run_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T17:58:58.665028+00:00_

artifacts/alpha_sweep_a060_s42_fp32_v4/run_analysis.py
artifacts/phase_diagram_t05_a045_s42_fp32/run_analysis.py
artifacts/phase_diagram_t05_a050_s42_fp32/run_analysis.py
artifacts/alpha_sweep_a000_s48_fp32/run_analysis.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T17:58:58.665157+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts -name \"run_analysis.py\" -type f 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts -name \"run_analysis.py\" -type f 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T17:58:58.665295+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a000_s48_fp32/run_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t05_a050_s42_fp32/run_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/alpha_sweep_a060_s42_fp32_v4/run_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t05_a045_s42_fp32/run_analysis.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T17:58:58.665432+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t05_a050_s42_fp32/run_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t05_a050_s42_fp32/run_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T17:58:58.665641+00:00_

1	"""5-method lead-lag analysis for phase_diagram_t05_a050_s42_fp32.
2	T=5 generations, alpha=0.50, seed=42, fp32, Pythia-410m.
3	Adapted from canonical run_analysis.py methodology.
4	"""
5	import json
6	import numpy as np
7	from scipy import stats
8	from statsmodels.tsa.stattools import adfuller
9	from statsmodels.tsa.vector_ar.var_model import VAR
10	
11	N_PERM = 5000
12	ALPHA_SIG = 0.05
13	
14	CANARIES = ["token_entropy", "ece"]
15	DOWNSTREAMS = ["distinct_1", "distinct_2", "distinct_3", "mauve"]
16	
17	HIGHER_IS_WORSE = {"ece"}
18	LOWER_IS_WORSE = {"token_entropy", "distinct_1", "distinct_2", "distinct_3", "mauve"}
19	
20	ALL_METRICS = [
21	  {"token_entropy": 3.23419483150593, "self_bleu": 0.011078699301381554, "ece": 0.010804557477709054, "effective_rank": 46.612774691899155, "perplexity": 26.948958972544652, "distinct_1": 0.0979600146585773, "distinct_2": 0.5141374985748489, "distinct_3": 0.8127010497341054, "mauve": 0.031110582626136873, "generation": 0, "effective_alpha": 0.5},
22	  {"token_entropy": 2.500745799007679, "self_bleu": 0.01181542928801186, "ece": 0.06923721421227194, "effective_rank": 58.664278351426624, "perplexity": 22.906680552682573, "distinct_1": 0.09759209446336131, "distinct_2": 0.5124500211292787, "distinct_3": 0.8121673127402459, "mauve": 0.0314065242440103, "generation": 1, "effective_alpha": 0.5},
23	  {"token_entropy": 2.5279709900041323, "self_bleu": 0.011853806854457662, "ece": 0.0814817014521384, "effective_rank": 63.1498418789002, "perplexity": 25.913836211243243, "distinct_1": 0.0839296875, "distinct_2": 0.4421597043726904, "distinct_3": 0.7366443225675401, "mauve": 0.03198531125622274, "generation": 2, "effective_alpha": 0.5},
24	  {"token_entropy": 2.5705517679931194, "self_bleu": 0.01206434172162393, "ece": 0.08541292666745874, "effective_rank": 64.57902052385074, "perplexity": 27.20622452107867, "distinct_1": 0.0768828125, "distinct_2": 0.397964046594114, "distinct_3": 0.6739089673276145, "mauve": 0.0325659067423255, "gener
…[truncated 19663 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T17:58:58.665807+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t05_a045_s42_fp32/run_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t05_a045_s42_fp32/run_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T17:58:58.666014+00:00_

1	"""5-method lead-lag analysis for phase_diagram_t05_a045_s42_fp32.
2	T=5 generations, alpha=0.45, seed=42, fp32, Pythia-410m.
3	Adapted from canonical run_analysis.py methodology.
4	"""
5	import json
6	import numpy as np
7	from scipy import stats
8	from statsmodels.tsa.stattools import adfuller
9	from statsmodels.tsa.vector_ar.var_model import VAR
10	
11	N_PERM = 5000
12	ALPHA_SIG = 0.05
13	
14	CANARIES = ["token_entropy", "ece"]
15	DOWNSTREAMS = ["distinct_1", "distinct_2", "distinct_3", "mauve"]
16	
17	HIGHER_IS_WORSE = {"ece"}
18	LOWER_IS_WORSE = {"token_entropy", "distinct_1", "distinct_2", "distinct_3", "mauve"}
19	
20	ALL_METRICS = [
21	  {"token_entropy": 3.23419483150593, "self_bleu": 0.011078699301381554, "ece": 0.010804557477709054, "effective_rank": 46.612774691899155, "perplexity": 26.948958972544652, "distinct_1": 0.0979600146585773, "distinct_2": 0.5141374985748489, "distinct_3": 0.8127010497341054, "mauve": 0.031110582626136873, "generation": 0, "effective_alpha": 0.45},
22	  {"token_entropy": 2.494058441616721, "self_bleu": 0.01181542928801186, "ece": 0.06666987054815446, "effective_rank": 58.30666526113631, "perplexity": 22.538010937788044, "distinct_1": 0.09759209446336131, "distinct_2": 0.5124500211292787, "distinct_3": 0.8121673127402459, "mauve": 0.0314065242440103, "generation": 1, "effective_alpha": 0.45},
23	  {"token_entropy": 2.534136101724104, "self_bleu": 0.012035022098091467, "ece": 0.0776851344230731, "effective_rank": 62.23149385795327, "perplexity": 25.144345507719237, "distinct_1": 0.0839296875, "distinct_2": 0.4432612754787147, "distinct_3": 0.7360505632900514, "mauve": 0.03256302608932375, "generation": 2, "effective_alpha": 0.45},
24	  {"token_entropy": 2.5901672458724554, "self_bleu": 0.01229421686114261, "ece": 0.07674335772304731, "effective_rank": 63.461815189636326, "perplexity": 26.117359098847647, "distinct_1": 0.0783828125, "distinct_2": 0.40030781490480394, "distinct_3": 0.671760496257754, "mauve": 0.03222753095848002, 
…[truncated 19367 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T17:58:58.666198+00:00_

Perfect! I found the 5-method lead-lag analysis scripts. Both files contain the exact same five analysis methods. Let me verify the completeness and provide you with the most relevant path.

Based on my search, I've found the existing 5-method lead-lag analysis scripts in your project. Both phase_diagram experiments implement the identical methodology with these five analysis methods:

1. **naive_xcorr** - Cross-correlation on raw series with lag detection
2. **diff_xcorr** - Cross-correlation on differenced series with FDR adjustment
3. **threshold_onset** - 3-sigma threshold-based onset detection
4. **perm_granger** - Permutation-based Granger causality test
5. **ty_granger** - Toda-Yamamoto VAR-based Granger causality

The most relevant template file is:

**/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t05_a050_s42_fp32/run_analysis.py**

This script:
- Uses a 2x4 canary-downstream pair matrix (token_entropy + ece vs distinct_1/2/3 + mauve)
- Implements bidirectional testing (forward and reverse)
- Applies Benjamini-Hochberg FDR correction
- Generates consensus voting across methods
- Outputs detailed JSON results with metadata
- Tests both individual p-values and FDR-adjusted significance
- Handles edge cases (small sample size T=5, NaN values)

All four run_analysis.py files found follow this same pattern, with the main differences being the specific metric values from their respective experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Agent",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T17:58:58.666397+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t15_a050_s42_fp32/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t15_a050_s42_fp32/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T17:58:58.666527+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t05_a050_s42_fp32/run_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t05_a050_s42_fp32/run_analysis.py"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T17:58:58.666773+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"token_entropy\\\": 3.23419483150593,\\n    \\\"self_bleu\\\": 0.011078699301381554,\\n    \\\"ece\\\": 0.010804557477709054,\\n    \\\"effective_rank\\\": 46.612774691899155,\\n    \\\"perplexity\\\": 26.948958972544652,\\n    \\\"distinct_1\\\": 0.0979600146585773,\\n    \\\"distinct_2\\\": 0.5141374985748489,\\n    \\\"distinct_3\\\": 0.8127010497341054,\\n    \\\"mauve\\\": 0.031110582626136873,\\n    \\\"generation\\\": 0,\\n    \\\"intervention_triggered\\\": false,\\n    \\\"trigger_gen\\\": null,\\n    \\\"effective_alpha\\\": 0.5\\n  },\\n  {\\n    \\\"token_entropy\\\": 2.500745799007679,\\n    \\\"self_bleu\\\": 0.01181542928801186,\\n    \\\"ece\\\": 0.06923721421227194,\\n    \\\"effective_rank\\\": 58.664278351426624,\\n    \\\"perplexity\\\": 22.906680552682573,\\n    \\\"distinct_1\\\": 0.09759209446336131,\\n    \\\"distinct_2\\\": 0.5124500211292787,\\n    \\\"distinct_3\\\": 0.8121673127402459,\\n    \\\"mauve\\\": 0.0314065242440103,\\n    \\\"generation\\\": 1,\\n    \\\"intervention_triggered\\\": false,\\n    \\\"trigger_gen\\\": null,\\n    \\\"effective_alpha\\\": 0.5\\n  },\\n  {\\n    \\\"token_entropy\\\": 2.5279709900041323,\\n    \\\"self_bleu\\\": 0.011853806854457662,\\n    \\\"ece\\\": 0.0814817014521384,\\n    \\\"effective_rank\\\": 63.1498418789002,\\n    \\\"perplexity\\\": 25.913836211243243,\\n    \\\"distinct_1\\\": 0.0839296875,\\n    \\\"distinct_2\\\": 0.4421597043726904,\\n    \\\"distinct_3\\\": 0.7366443225675401,\\n    \\\"mauve\\\": 0.03198531125622274,\\n    \\\"generation\\\": 2,\\n    \\\"intervention_triggered\\\": false,\\n    \\\"trigger_gen\\\": null,\\n    \\\"effective_alpha\\\": 0.5\\n  },\\n  {\\n    \\\"token_entropy\\\": 2.5705517679931194,\\n    \\\"self_bleu\\\": 0.01206434172162393,\\n    \\\"ece\\\": 0.08541292666745874,\\n    \\\"effective_rank\\\": 64.57902052385074,\\n    \\\"perplexity\\\": 27.20622452107867,\\n    \\\"distinc
…[truncated 7128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T17:58:58.667096+00:00_

1	"""5-method lead-lag analysis for phase_diagram_t05_a050_s42_fp32.
2	T=5 generations, alpha=0.50, seed=42, fp32, Pythia-410m.
3	Adapted from canonical run_analysis.py methodology.
4	"""
5	import json
6	import numpy as np
7	from scipy import stats
8	from statsmodels.tsa.stattools import adfuller
9	from statsmodels.tsa.vector_ar.var_model import VAR
10	
11	N_PERM = 5000
12	ALPHA_SIG = 0.05
13	
14	CANARIES = ["token_entropy", "ece"]
15	DOWNSTREAMS = ["distinct_1", "distinct_2", "distinct_3", "mauve"]
16	
17	HIGHER_IS_WORSE = {"ece"}
18	LOWER_IS_WORSE = {"token_entropy", "distinct_1", "distinct_2", "distinct_3", "mauve"}
19	
20	ALL_METRICS = [
21	  {"token_entropy": 3.23419483150593, "self_bleu": 0.011078699301381554, "ece": 0.010804557477709054, "effective_rank": 46.612774691899155, "perplexity": 26.948958972544652, "distinct_1": 0.0979600146585773, "distinct_2": 0.5141374985748489, "distinct_3": 0.8127010497341054, "mauve": 0.031110582626136873, "generation": 0, "effective_alpha": 0.5},
22	  {"token_entropy": 2.500745799007679, "self_bleu": 0.01181542928801186, "ece": 0.06923721421227194, "effective_rank": 58.664278351426624, "perplexity": 22.906680552682573, "distinct_1": 0.09759209446336131, "distinct_2": 0.5124500211292787, "distinct_3": 0.8121673127402459, "mauve": 0.0314065242440103, "generation": 1, "effective_alpha": 0.5},
23	  {"token_entropy": 2.5279709900041323, "self_bleu": 0.011853806854457662, "ece": 0.0814817014521384, "effective_rank": 63.1498418789002, "perplexity": 25.913836211243243, "distinct_1": 0.0839296875, "distinct_2": 0.4421597043726904, "distinct_3": 0.7366443225675401, "mauve": 0.03198531125622274, "generation": 2, "effective_alpha": 0.5},
24	  {"token_entropy": 2.5705517679931194, "self_bleu": 0.01206434172162393, "ece": 0.08541292666745874, "effective_rank": 64.57902052385074, "perplexity": 27.20622452107867, "distinct_1": 0.0768828125, "distinct_2": 0.397964046594114, "distinct_3": 0.6739089673276145, "mauve": 0.0325659067423255, "gener
…[truncated 19663 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T17:58:58.667306+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32/data",
  "description": "Create output directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32/data",
    "description": "Create output directories"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T17:58:58.667450+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T17:58:58.667653+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32/run_analysis.py",
  "content": "\"\"\"5-method lead-lag analysis for phase_diagram_t15_a050_s42_fp32.\nT=15 generations, alpha=0.50, seed=42, fp32, Pythia-410m.\n\"\"\"\nimport json\nimport numpy as np\nfrom scipy import stats\nfrom statsmodels.tsa.stattools import adfuller\nfrom statsmodels.tsa.vector_ar.var_model import VAR\n\nN_PERM = 5000\nALPHA_SIG = 0.05\n\nCANARIES = [\"token_entropy\", \"ece\"]\nDOWNSTREAMS = [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"]\n\nHIGHER_IS_WORSE = {\"ece\"}\nLOWER_IS_WORSE = {\"token_entropy\", \"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"}\n\nALL_METRICS = [\n  {\"token_entropy\": 3.23419483150593, \"self_bleu\": 0.011078699301381554, \"ece\": 0.010804557477709054, \"effective_rank\": 46.612774691899155, \"perplexity\": 26.948958972544652, \"distinct_1\": 0.0979600146585773, \"distinct_2\": 0.5141374985748489, \"distinct_3\": 0.8127010497341054, \"mauve\": 0.031110582626136873, \"generation\": 0, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.500745799007679, \"self_bleu\": 0.01181542928801186, \"ece\": 0.06923721421227194, \"effective_rank\": 58.664278351426624, \"perplexity\": 22.906680552682573, \"distinct_1\": 0.09759209446336131, \"distinct_2\": 0.5124500211292787, \"distinct_3\": 0.8121673127402459, \"mauve\": 0.0314065242440103, \"generation\": 1, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.5279709900041323, \"self_bleu\": 0.011853806854457662, \"ece\": 0.0814817014521384, \"effective_rank\": 63.1498418789002, \"perplexity\": 25.913836211243243, \"distinct_1\": 0.0839296875, \"distinct_2\": 0.4421597043726904, \"distinct_3\": 0.7366443225675401, \"mauve\": 0.03198531125622274, \"generation\": 2, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.5705517679931194, \"self_bleu\": 0.01206434172162393, \"ece\": 0.08541292666745874, \"effective_rank\": 64.57902052385074, \"perplexity\": 27.20622452107867, \"distinct_1\": 0.0768828125, \"distinct_2\": 0.397964046594114, \"distinct_3\": 0.6739089673276145, \"mauve\": 0.0325659067423255, \"generation\": 3, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.5547223568996094, \"self_bleu\": 0.012242930650399822, \"ece\": 0.09349395109952266, \"effective_rank\": 65.14919303940499, \"perplexity\": 28.386376019698663, \"distinct_1\": 0.0728046875, \"distinct_2\": 0.362682520957195, \"distinct_3\": 0.6109548586696667, \"mauve\": 0.03118548395894347, \"generation\": 4, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.580346416130023, \"self_bleu\": 0.012304872677139776, \"ece\": 0.09296360416233349, \"effective_rank\": 63.564618303082256, \"perplexity\": 29.28162815993609, \"distinct_1\": 0.0696484375, \"distinct_2\": 0.3320025937702638, \"distinct_3\": 0.554360224378506, \"mauve\": 0.030921812037617825, \"generation\": 5, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.564262702211209, \"self_bleu\": 0.01193750680915104, \"ece\": 0.09837506712438573, \"effective_rank\": 63.561151240123266, \"perplexity\": 30.08017169949993, \"distinct_1\": 0.0679609375, \"distinct_2\": 0.31463527058805146, \"distinct_3\": 0.5193753027391053, \"mauve\": 0.031182692535056976, \"generation\": 6, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.6040152154444067, \"self_bleu\": 0.011591511348067306, \"ece\": 0.09373151194072746, \"effective_rank\": 62.434320178241194, \"perplexity\": 30.26975149237044, \"distinct_1\": 0.0662421875, \"distinct_2\": 0.29762732521347823, \"distinct_3\": 0.48460132189565464, \"mauve\": 0.027181014352647016, \"generation\": 7, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.58627940470919, \"self_bleu\": 0.011975516384963573, \"ece\": 0.10233863935392483, \"effective_rank\": 62.02057606199564, \"perplexity\": 31.561025257090403, \"distinct_1\": 0.0656796875, \"distinct_2\": 0.2907678966241924, \"distinct_3\": 0.4698589040453757, \"mauve\": 0.02690886449692288, \"generation\": 8, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.6018234955777535, \"self_bleu\": 0.0121229985496681, \"ece\": 0.10367290267111146, \"effective_rank\": 60.94696017365545, \"perplexity\": 32.278724816873655, \"distinct_1\": 0.0646796875, \"distinct_2\": 0.2830725240040938, \"distinct_3\": 0.4537414647103861, \"mauve\": 0.02727185115386438, \"generation\": 9, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.620642818896644, \"self_bleu\": 0.012225398003610086, \"ece\": 0.10212884563219399, \"effective_rank\": 59.743030844903664, \"perplexity\": 32.615784133669905, \"distinct_1\": 0.064203125, \"distinct_2\": 0.2784787381151415, \"distinct_3\": 0.44216315879935625, \"mauve\": 0.024453051534418697, \"generation\": 10, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.6372860365386708, \"self_bleu\": 0.012176168939241304, \"ece\": 0.10406294349108942, \"effective_rank\": 59.497715517955875, \"perplexity\": 33.178300587754556, \"distinct_1\": 0.0643359375, \"distinct_2\": 0.27711935249494135, \"distinct_3\": 0.43867091673307396, \"mauve\": 0.026187539380385434, \"generation\": 11, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.649274517690487, \"self_bleu\": 0.01211159905301402, \"ece\": 0.10485252263545924, \"effective_rank\": 60.00612616162178, \"perplexity\": 33.718560533593745, \"distinct_1\": 0.064234375, \"distinct_2\": 0.2756037156540285, \"distinct_3\": 0.43513961155643055, \"mauve\": 0.02711185259199654, \"generation\": 12, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.6691765213944105, \"self_bleu\": 0.01234131584794922, \"ece\": 0.1038628399649267, \"effective_rank\": 59.30921577186063, \"perplexity\": 33.67533110543885, \"distinct_1\": 0.0639609375, \"distinct_2\": 0.2740568285689732, \"distinct_3\": 0.4319442491288926, \"mauve\": 0.024969167666139103, \"generation\": 13, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.650109134228356, \"self_bleu\": 0.01228111626962466, \"ece\": 0.1090129944620413, \"effective_rank\": 59.627950190233996, \"perplexity\": 34.604176016757435, \"distinct_1\": 0.06384375, \"distinct_2\": 0.272697442948773, \"distinct_3\": 0.42962390037344333, \"mauve\": 0.02621373520173196, \"generation\": 14, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.69464270902633, \"self_bleu\": 0.012265766691581312, \"ece\": 0.10333076799124105, \"effective_rank\": 59.6681909643878, \"perplexity\": 34.322892091319574, \"distinct_1\": 0.0637734375, \"distinct_2\": 0.2715255587934281, \"distinct_3\": 0.42750667979187174, \"mauve\": 0.02641633548512619, \"generation\": 15, \"effective_alpha\": 0.5},\n]\n\n\ndef orient(series, name):\n    return -series.copy() if name in LOWER_IS_WORSE else series.copy()\n\n\ndef _build_lag_matrix(y, x, max_lag):\n    T = len(y)\n    n = T - max_lag\n    Y = y[max_lag:]\n    cols_r = [np.ones(n)]\n    for lag in range(1, max_lag + 1):\n        cols_r.append(y[max_lag - lag: T - lag])\n    cols_u = list(cols_r)\n    for lag in range(1, max_lag + 1):\n        cols_u.append(x[max_lag - lag: T - lag])\n    return Y, np.column_stack(cols_r), np.column_stack(cols_u)\n\n\ndef _granger_f_stat(y, x, max_lag):\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\n    n = len(Y)\n    q = max_lag\n    try:\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\n    except np.linalg.LinAlgError:\n        return np.nan\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\n    k_u = X_u.shape[1]\n    df_resid = n - k_u\n    if df_resid <= 0 or rss_u < 1e-15:\n        return np.nan\n    return ((rss_r - rss_u) / q) / (rss_u / df_resid)\n\n\ndef permutation_granger_test(x, y, max_lag=1, n_perm=1000, seed=42, difference=True):\n    x = np.asarray(x, dtype=float)\n    y = np.asarray(y, dtype=float)\n    if difference:\n        x = np.diff(x)\n        y = np.diff(y)\n    f_obs = _granger_f_stat(y, x, max_lag)\n    if np.isnan(f_obs):\n        return {\"f_stat\": None, \"p_value\": None, \"significant\": False}\n    rng = np.random.default_rng(seed)\n    null_f = np.empty(n_perm)\n    for i in range(n_perm):\n        null_f[i] = _granger_f_stat(y, rng.permutation(x), max_lag)\n    valid_null = null_f[~np.isnan(null_f)]\n    if len(valid_null) == 0:\n        return {\"f_stat\": round(float(f_obs), 4), \"p_value\": None, \"significant\": False}\n    p_value = (np.sum(valid_null >= f_obs) + 1) / (len(valid_null) + 1)\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\n    rss_r = np.sum((Y - X_r @ np.linalg.lstsq(X_r, Y, rcond=None)[0]) ** 2)\n    rss_u = np.sum((Y - X_u @ np.linalg.lstsq(X_u, Y, rcond=None)[0]) ** 2)\n    f2 = (rss_r - rss_u) / rss_u if rss_u > 1e-15 else None\n    return {\n        \"f_stat\": round(float(f_obs), 4),\n        \"p_value\": round(float(p_value), 6),\n        \"null_mean\": round(float(np.mean(valid_null)), 4),\n        \"null_std\": round(float(np.std(valid_null)), 4),\n        \"effect_size_f2\": round(float(f2), 4) if f2 is not None else None,\n        \"significant\": bool(p_value < 0.05),\n    }\n\n\ndef bh_fdr(p_values, alpha=0.05):\n    pv = np.array(p_values, dtype=float)\n    n = len(pv)\n    valid = ~np.isnan(pv)\n    adjusted = np.full(n, np.nan)\n    if valid.sum() == 0:\n        return adjusted.tolist(), [False] * n\n    idx = np.where(valid)[0]\n    p_valid = pv[idx]\n    sorted_idx = np.argsort(p_valid)\n    ranks = np.empty_like(sorted_idx)\n    ranks[sorted_idx] = np.arange(1, len(p_valid) + 1)\n    m = len(p_valid)\n    adj = p_valid * m / ranks\n    adj_sorted = adj[sorted_idx].copy()\n    for i in range(m - 2, -1, -1):\n        adj_sorted[i] = min(adj_sorted[i], adj_sorted[i + 1])\n    adj_sorted = np.minimum(adj_sorted, 1.0)\n    adj_final = np.empty(m)\n    adj_final[sorted_idx] = adj_sorted\n    for i, ix in enumerate(idx):\n        adjusted[ix] = adj_final[i]\n    significant = [(adjusted[i] < alpha if not np.isnan(adjusted[i]) else False) for i in range(n)]\n    return adjusted.tolist(), significant\n\n\ndef naive_xcorr(c, d, cn, dn, max_lag=5):\n    x, y = orient(c, cn), orient(d, dn)\n    n = len(x)\n    best_lag, best_r, best_p = 0, 0.0, 1.0\n    all_lags = []\n    for lag in range(-max_lag, max_lag + 1):\n        if lag >= 0:\n            a, b = x[lag:], y[:n - lag]\n        else:\n            a, b = x[:n + lag], y[-lag:]\n        if len(a) < 4:\n            continue\n        r, p = stats.pearsonr(a, b)\n        all_lags.append({\"lag\": int(lag), \"r\": round(float(r), 4), \"p\": round(float(p), 6)})\n        if abs(r) > abs(best_r):\n            best_lag, best_r, best_p = lag, r, p\n    return {\n        \"method\": \"naive_xcorr\",\n        \"peak_lag\": int(best_lag),\n        \"r\": round(float(best_r), 4),\n        \"p_value\": round(float(best_p), 6),\n        \"significant\": bool(best_p < ALPHA_SIG),\n        \"all_lags\": all_lags,\n    }\n\n\ndef diff_xcorr(c, d, cn, dn, max_lag=5):\n    dx, dy = np.diff(orient(c, cn)), np.diff(orient(d, dn))\n    n = len(dx)\n    best_lag, best_r, best_p = 0, 0.0, 1.0\n    all_lags = []\n    for lag in range(-max_lag, max_lag + 1):\n        if lag >= 0:\n            a, b = dx[lag:], dy[:n - lag]\n        else:\n            a, b = dx[:n + lag], dy[-lag:]\n        if len(a) < 4:\n            continue\n        if np.std(a) < 1e-12 or np.std(b) < 1e-12:\n            continue\n        r, p = stats.pearsonr(a, b)\n        all_lags.append({\"lag\": int(lag), \"r\": round(float(r), 4), \"p\": round(float(p), 6)})\n        if abs(r) > abs(best_r):\n            best_lag, best_r, best_p = lag, r, p\n    return {\n        \"method\": \"diff_xcorr\",\n        \"peak_lag\": int(best_lag),\n        \"r\": round(float(best_r), 4),\n        \"p_value\": round(float(best_p), 6),\n        \"significant\": bool(best_p < ALPHA_SIG),\n        \"all_lags\": all_lags,\n    }\n\n\ndef _onset_gen(series, name):\n    s = orient(series, name)\n    base, sigma = s[0], np.std(s)\n    if sigma < 1e-12:\n        return None\n    thresh = base + 3.0 * sigma\n    for i in range(1, len(s)):\n        if s[i] > thresh:\n            return i\n    return None\n\n\ndef threshold_onset(c, d, cn, dn):\n    c_onset = _onset_gen(c, cn)\n    d_onset = _onset_gen(d, dn)\n    if c_onset is not None and d_onset is not None:\n        lead_time = d_onset - c_onset\n        significant = lead_time > 0\n    else:\n        lead_time = None\n        significant = False\n    return {\n        \"method\": \"threshold_onset\",\n        \"canary_onset\": c_onset,\n        \"downstream_onset\": d_onset,\n        \"lead_time\": lead_time,\n        \"significant\": significant,\n        \"threshold\": \"true_3sigma_d105\",\n    }\n\n\ndef perm_granger(c, d, cn, dn, seed):\n    x = orient(c, cn)\n    y = orient(d, dn)\n    result = permutation_granger_test(x, y, max_lag=1, n_perm=N_PERM, seed=seed, difference=True)\n    return {\n        \"method\": \"perm_granger\",\n        \"f_stat\": result[\"f_stat\"],\n        \"p_value\": result[\"p_value\"],\n        \"null_mean\": result.get(\"null_mean\"),\n        \"null_std\": result.get(\"null_std\"),\n        \"effect_size_f2\": result.get(\"effect_size_f2\"),\n        \"significant\": bool(result[\"p_value\"] < ALPHA_SIG) if result[\"p_value\"] is not None else False,\n    }\n\n\ndef ty_granger(c, d, cn, dn, max_order=2):\n    x = orient(c, cn)\n    y = orient(d, dn)\n    n = len(x)\n    d_max = 0\n    for series in [x, y]:\n        try:\n            result = adfuller(series, maxlag=min(3, n // 3 - 1))\n            if result[1] > 0.05:\n                d_max = max(d_max, 1)\n        except:\n            d_max = max(d_max, 1)\n    best_k, best_aic = 1, np.inf\n    data = np.column_stack([x, y])\n    for k in range(1, max_order + 1):\n        try:\n            model = VAR(data)\n            result = model.fit(k)\n            if result.aic < best_aic:\n                best_k, best_aic = k, result.aic\n        except:\n            continue\n    total_order = best_k + d_max\n    if total_order >= n // 2:\n        total_order = max(1, n // 2 - 1)\n    try:\n        model = VAR(data)\n        result = model.fit(total_order)\n        test_result = result.test_causality(causing=1, caused=0, kind=\"f\")\n        f_stat = float(test_result.test_statistic)\n        p_value = float(test_result.pvalue)\n        return {\n            \"method\": \"ty_granger\",\n            \"f_stat\": round(f_stat, 4),\n            \"p_value\": round(p_value, 4),\n            \"significant\": bool(p_value < ALPHA_SIG),\n            \"order\": total_order,\n            \"k_opt\": best_k,\n            \"d_max\": d_max,\n        }\n    except Exception as e:\n        return {\n            \"method\": \"ty_granger\",\n            \"f_stat\": None,\n            \"p_value\": None,\n            \"significant\": False,\n            \"error\": str(e),\n            \"order\": total_order,\n            \"k_opt\": best_k,\n            \"d_max\": d_max,\n        }\n\n\ndef main():\n    data = sorted(ALL_METRICS, key=lambda x: x[\"generation\"])\n    series = {}\n    for k in CANARIES + DOWNSTREAMS:\n        series[k] = np.array([d[k] for d in data])\n\n    n_gens = len(data)\n    seed = 42\n\n    pairs = [{\"canary\": c, \"downstream\": d} for c in CANARIES for d in DOWNSTREAMS]\n\n    pair_results = []\n    perm_pval_fwd, perm_pval_rev = [], []\n    diff_pval_fwd, diff_pval_rev = [], []\n\n    for pair in pairs:\n        cn, dn = pair[\"canary\"], pair[\"downstream\"]\n        c, d = series[cn], series[dn]\n\n        fwd_naive = naive_xcorr(c, d, cn, dn)\n        fwd_diff = diff_xcorr(c, d, cn, dn)\n        fwd_onset = threshold_onset(c, d, cn, dn)\n        fwd_perm = perm_granger(c, d, cn, dn, seed)\n        fwd_ty = ty_granger(c, d, cn, dn)\n\n        rev_naive = naive_xcorr(d, c, dn, cn)\n        rev_diff = diff_xcorr(d, c, dn, cn)\n        rev_onset = threshold_onset(d, c, dn, cn)\n        rev_perm = perm_granger(d, c, dn, cn, seed)\n        rev_ty = ty_granger(d, c, dn, cn)\n\n        result = {\n            \"canary\": cn, \"downstream\": dn,\n            \"forward\": {\n                \"naive_xcorr\": fwd_naive, \"diff_xcorr\": fwd_diff,\n                \"threshold_onset\": fwd_onset, \"perm_granger\": fwd_perm,\n                \"ty_granger\": fwd_ty,\n            },\n            \"reverse\": {\n                \"naive_xcorr\": rev_naive, \"diff_xcorr\": rev_diff,\n                \"threshold_onset\": rev_onset, \"perm_granger\": rev_perm,\n                \"ty_granger\": rev_ty,\n            },\n        }\n\n        perm_pval_fwd.append(fwd_perm[\"p_value\"] if fwd_perm[\"p_value\"] is not None else np.nan)\n        perm_pval_rev.append(rev_perm[\"p_value\"] if rev_perm[\"p_value\"] is not None else np.nan)\n        diff_pval_fwd.append(fwd_diff[\"p_value\"] if fwd_diff[\"p_value\"] is not None else np.nan)\n        diff_pval_rev.append(rev_diff[\"p_value\"] if rev_diff[\"p_value\"] is not None else np.nan)\n        pair_results.append(result)\n\n    perm_adj_fwd, perm_sig_fwd = bh_fdr(perm_pval_fwd)\n    perm_adj_rev, perm_sig_rev = bh_fdr(perm_pval_rev)\n    diff_adj_fwd, diff_sig_fwd = bh_fdr(diff_pval_fwd)\n    diff_adj_rev, diff_sig_rev = bh_fdr(diff_pval_rev)\n\n    for i, r in enumerate(pair_results):\n        r[\"forward\"][\"perm_granger\"][\"p_fdr\"] = round(perm_adj_fwd[i], 6) if not np.isnan(perm_adj_fwd[i]) else None\n        r[\"forward\"][\"perm_granger\"][\"significant_fdr\"] = perm_sig_fwd[i]\n        r[\"reverse\"][\"perm_granger\"][\"p_fdr\"] = round(perm_adj_rev[i], 6) if not np.isnan(perm_adj_rev[i]) else None\n        r[\"reverse\"][\"perm_granger\"][\"significant_fdr\"] = perm_sig_rev[i]\n        r[\"forward\"][\"diff_xcorr\"][\"p_fdr\"] = round(diff_adj_fwd[i], 6) if not np.isnan(diff_adj_fwd[i]) else None\n        r[\"forward\"][\"diff_xcorr\"][\"significant_fdr\"] = diff_sig_fwd[i]\n        r[\"reverse\"][\"diff_xcorr\"][\"p_fdr\"] = round(diff_adj_rev[i], 6) if not np.isnan(diff_adj_rev[i]) else None\n        r[\"reverse\"][\"diff_xcorr\"][\"significant_fdr\"] = diff_sig_rev[i]\n\n    print(\"=\" * 100)\n    print(\"5-METHOD LEAD-LAG ANALYSIS | T=15 | alpha=0.50 | seed=42 | phase_diagram_t15_a050_s42_fp32\")\n    print(\"=\" * 100)\n    print(f\"Loaded {n_gens} generations (T=15, 16 data points)\\n\")\n\n    for direction in [\"forward\", \"reverse\"]:\n        dir_label = \"FORWARD (canary -> downstream)\" if direction == \"forward\" else \"REVERSE (downstream -> canary)\"\n        print(f\"\\n{'=' * 100}\")\n        print(f\"  {dir_label}\")\n        print(f\"{'=' * 100}\")\n        print(f\"  {'Pair':<30} {'Naive XCorr':<20} {'Diff XCorr(FDR)':<20} {'Threshold':<18} {'PermG(FDR)':<20} {'TY Granger':<15}\")\n        print(\"-\" * 130)\n        for r in pair_results:\n            label = f\"{r['canary']}<{r['downstream']}\"\n            d = r[direction]\n\n            naive_str = f\"lag={d['naive_xcorr']['peak_lag']} r={d['naive_xcorr']['r']:.3f} {'*' if d['naive_xcorr']['significant'] else ''}\"\n            diff_p = d['diff_xcorr'].get('p_value')\n            diff_str = f\"lag={d['diff_xcorr']['peak_lag']} r={d['diff_xcorr']['r']:.3f} {'*' if d['diff_xcorr'].get('significant_fdr', False) else ''}\" if diff_p is not None else \"N/A\"\n            onset_str = f\"c={d['threshold_onset']['canary_onset']} d={d['threshold_onset']['downstream_onset']} {'*' if d['threshold_onset']['significant'] else ''}\"\n            perm_str = f\"F={d['perm_granger']['f_stat']:.2f} p={d['perm_granger']['p_value']:.4f} {'*' if d['perm_granger'].get('significant_fdr', False) else ''}\" if d['perm_granger']['f_stat'] else \"N/A\"\n            ty_str = f\"F={d['ty_granger']['f_stat']:.2f} p={d['ty_granger']['p_value']:.4f} {'*' if d['ty_granger']['significant'] else ''}\" if d['ty_granger']['f_stat'] else \"N/A\"\n            print(f\"  {label:<30} {naive_str:<20} {diff_str:<20} {onset_str:<18} {perm_str:<20} {ty_str:<15}\")\n\n    print(f\"\\n{'=' * 100}\")\n    print(\"  CONSENSUS (forward, D111 direction filter: peak_lag < 0 for xcorr)\")\n    print(f\"{'=' * 100}\")\n    consensus = []\n    for r in pair_results:\n        f = r[\"forward\"]\n        votes = 0\n        methods_sig = []\n        if f[\"naive_xcorr\"][\"significant\"] and f[\"naive_xcorr\"][\"peak_lag\"] < 0:\n            votes += 1; methods_sig.append(\"naive\")\n        if f[\"diff_xcorr\"].get(\"significant_fdr\", False) and f[\"diff_xcorr\"][\"peak_lag\"] < 0:\n            votes += 1; methods_sig.append(\"diff\")\n        if f[\"threshold_onset\"][\"significant\"]:\n            votes += 1; methods_sig.append(\"threshold\")\n        if f[\"perm_granger\"].get(\"significant_fdr\", False):\n            votes += 1; methods_sig.append(\"perm\")\n        if f[\"ty_granger\"][\"significant\"]:\n            votes += 1; methods_sig.append(\"ty\")\n        label = f\"{r['canary']}<{r['downstream']}\"\n        consensus.append({\"pair\": label, \"votes\": votes, \"methods\": methods_sig})\n        print(f\"  {label:<30} {votes}/5  [{', '.join(methods_sig) if methods_sig else 'none'}]\")\n\n    summary = {\n        \"PermG_fwd\": f\"{sum(perm_sig_fwd)}/8\",\n        \"PermG_rev\": f\"{sum(perm_sig_rev)}/8\",\n        \"diff_xcorr_fdr_fwd\": f\"{sum(diff_sig_fwd)}/8\",\n        \"diff_xcorr_fdr_rev\": f\"{sum(diff_sig_rev)}/8\",\n        \"naive_xcorr_fwd_D111\": f\"{sum(1 for r in pair_results if r['forward']['naive_xcorr']['significant'] and r['forward']['naive_xcorr']['peak_lag'] < 0)}/8\",\n        \"threshold_onset_3sigma\": f\"{sum(1 for r in pair_results if r['forward']['threshold_onset']['significant'])}/8\",\n        \"TY_granger\": f\"{sum(1 for r in pair_results if r['forward']['ty_granger']['significant'])}/8\",\n        \"K_ge_3\": f\"{sum(1 for c in consensus if c['votes'] >= 3)}/8\",\n        \"K_ge_4\": f\"{sum(1 for c in consensus if c['votes'] >= 4)}/8\",\n        \"robust_pairs\": f\"{sum(1 for c in consensus if c['votes'] >= 3)}/8\",\n    }\n\n    print(f\"\\n{'=' * 100}\")\n    print(\"  SUMMARY\")\n    print(f\"{'=' * 100}\")\n    for k, v in summary.items():\n        print(f\"  {k:<30} {v}\")\n\n    print(f\"\\n{'=' * 100}\")\n    print(\"  DRIFT STATISTICS (gen0 -> gen15)\")\n    print(f\"{'=' * 100}\")\n    g0, gN = data[0], data[-1]\n    for metric in [\"token_entropy\", \"ece\", \"perplexity\", \"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\", \"effective_rank\"]:\n        v0, vN = g0[metric], gN[metric]\n        drift = (vN - v0) / abs(v0) * 100 if abs(v0) > 1e-12 else float('inf')\n        print(f\"  {metric:<20} {v0:.4f} -> {vN:.4f}  ({drift:+.2f}%)\")\n\n    full_results = {\n        \"meta\": {\n            \"exp_id\": \"phase_diagram_t15_a050_s42_fp32\",\n            \"alpha\": 0.50,\n            \"seed\": 42,\n            \"T\": 15,\n            \"n_gens\": n_gens,\n            \"n_perm\": N_PERM,\n            \"canaries\": CANARIES,\n            \"downstreams\": DOWNSTREAMS,\n            \"threshold_criterion\": \"true_3sigma_d105\",\n            \"D111_direction\": \"peak_lag < 0 (C009 corrected)\",\n            \"D105_3sigma\": \"true 3sigma (std of full series)\",\n        },\n        \"summary\": summary,\n        \"consensus\": consensus,\n        \"pairs\": [],\n    }\n\n    def clean(obj):\n        if isinstance(obj, (np.floating, np.float64)):\n            return float(obj)\n        if isinstance(obj, (np.integer,)):\n            return int(obj)\n        if isinstance(obj, np.bool_):\n            return bool(obj)\n        if isinstance(obj, dict):\n            return {k: clean(v) for k, v in obj.items()}\n        if isinstance(obj, list):\n            return [clean(v) for v in obj]\n        return obj\n\n    for r in pair_results:\n        pr = clean(r)\n        for d in [\"forward\", \"reverse\"]:\n            for m in [\"naive_xcorr\", \"diff_xcorr\"]:\n                if \"all_lags\" in pr[d][m]:\n                    del pr[d][m][\"all_lags\"]\n        full_results[\"pairs\"].append(pr)\n\n    out_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32/data/5method_leadlag.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(full_results, f, indent=2)\n    print(f\"\\nSaved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32/run_analysis.py",
    "content": "\"\"\"5-method lead-lag analysis for phase_diagram_t15_a050_s42_fp32.\nT=15 generations, alpha=0.50, seed=42, fp32, Pythia-410m.\n\"\"\"\nimport json\nimport numpy as np\nfrom scipy import stats\nfrom statsmodels.tsa.stattools import adfuller\nfrom statsmodels.tsa.vector_ar.var_model import VAR\n\nN_PERM = 5000\nALPHA_SIG = 0.05\n\nCANARIES = [\"token_entropy\", \"ece\"]\nDOWNSTREAMS = [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"]\n\nHIGHER_IS_WORSE = {\"ece\"}\nLOWER_IS_WORSE = {\"token_entropy\", \"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"}\n\nALL_METRICS = [\n  {\"token_entropy\": 3.23419483150593, \"self_bleu\": 0.011078699301381554, \"ece\": 0.010804557477709054, \"effective_rank\": 46.612774691899155, \"perplexity\": 26.948958972544652, \"distinct_1\": 0.0979600146585773, \"distinct_2\": 0.5141374985748489, \"distinct_3\": 0.8127010497341054, \"mauve\": 0.031110582626136873, \"generation\": 0, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.500745799007679, \"self_bleu\": 0.01181542928801186, \"ece\": 0.06923721421227194, \"effective_rank\": 58.664278351426624, \"perplexity\": 22.906680552682573, \"distinct_1\": 0.09759209446336131, \"distinct_2\": 0.5124500211292787, \"distinct_3\": 0.8121673127402459, \"mauve\": 0.0314065242440103, \"generation\": 1, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.5279709900041323, \"self_bleu\": 0.011853806854457662, \"ece\": 0.0814817014521384, \"effective_rank\": 63.1498418789002, \"perplexity\": 25.913836211243243, \"distinct_1\": 0.0839296875, \"distinct_2\": 0.4421597043726904, \"distinct_3\": 0.7366443225675401, \"mauve\": 0.03198531125622274, \"generation\": 2, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.5705517679931194, \"self_bleu\": 0.01206434172162393, \"ece\": 0.08541292666745874, \"effective_rank\": 64.57902052385074, \"perplexity\": 27.20622452107867, \"distinct_1\": 0.0768828125, \"distinct_2\": 0.397964046594114, \"distinct_3\": 0.6739089673276145, \"mauve\": 0.0325659067423255, \"generation\": 3, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.5547223568996094, \"self_bleu\": 0.012242930650399822, \"ece\": 0.09349395109952266, \"effective_rank\": 65.14919303940499, \"perplexity\": 28.386376019698663, \"distinct_1\": 0.0728046875, \"distinct_2\": 0.362682520957195, \"distinct_3\": 0.6109548586696667, \"mauve\": 0.03118548395894347, \"generation\": 4, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.580346416130023, \"self_bleu\": 0.012304872677139776, \"ece\": 0.09296360416233349, \"effective_rank\": 63.564618303082256, \"perplexity\": 29.28162815993609, \"distinct_1\": 0.0696484375, \"distinct_2\": 0.3320025937702638, \"distinct_3\": 0.554360224378506, \"mauve\": 0.030921812037617825, \"generation\": 5, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.564262702211209, \"self_bleu\": 0.01193750680915104, \"ece\": 0.09837506712438573, \"effective_rank\": 63.561151240123266, \"perplexity\": 30.08017169949993, \"distinct_1\": 0.0679609375, \"distinct_2\": 0.31463527058805146, \"distinct_3\": 0.5193753027391053, \"mauve\": 0.031182692535056976, \"generation\": 6, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.6040152154444067, \"self_bleu\": 0.011591511348067306, \"ece\": 0.09373151194072746, \"effective_rank\": 62.434320178241194, \"perplexity\": 30.26975149237044, \"distinct_1\": 0.0662421875, \"distinct_2\": 0.29762732521347823, \"distinct_3\": 0.48460132189565464, \"mauve\": 0.027181014352647016, \"generation\": 7, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.58627940470919, \"self_bleu\": 0.011975516384963573, \"ece\": 0.10233863935392483, \"effective_rank\": 62.02057606199564, \"perplexity\": 31.561025257090403, \"distinct_1\": 0.0656796875, \"distinct_2\": 0.2907678966241924, \"distinct_3\": 0.4698589040453757, \"mauve\": 0.02690886449692288, \"generation\": 8, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.6018234955777535, \"self_bleu\": 0.0121229985496681, \"ece\": 0.10367290267111146, \"effective_rank\": 60.94696017365545, \"perplexity\": 32.278724816873655, \"distinct_1\": 0.0646796875, \"distinct_2\": 0.2830725240040938, \"distinct_3\": 0.4537414647103861, \"mauve\": 0.02727185115386438, \"generation\": 9, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.620642818896644, \"self_bleu\": 0.012225398003610086, \"ece\": 0.10212884563219399, \"effective_rank\": 59.743030844903664, \"perplexity\": 32.615784133669905, \"distinct_1\": 0.064203125, \"distinct_2\": 0.2784787381151415, \"distinct_3\": 0.44216315879935625, \"mauve\": 0.024453051534418697, \"generation\": 10, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.6372860365386708, \"self_bleu\": 0.012176168939241304, \"ece\": 0.10406294349108942, \"effective_rank\": 59.497715517955875, \"perplexity\": 33.178300587754556, \"distinct_1\": 0.0643359375, \"distinct_2\": 0.27711935249494135, \"distinct_3\": 0.43867091673307396, \"mauve\": 0.026187539380385434, \"generation\": 11, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.649274517690487, \"self_bleu\": 0.01211159905301402, \"ece\": 0.10485252263545924, \"effective_rank\": 60.00612616162178, \"perplexity\": 33.718560533593745, \"distinct_1\": 0.064234375, \"distinct_2\": 0.2756037156540285, \"distinct_3\": 0.43513961155643055, \"mauve\": 0.02711185259199654, \"generation\": 12, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.6691765213944105, \"self_bleu\": 0.01234131584794922, \"ece\": 0.1038628399649267, \"effective_rank\": 59.30921577186063, \"perplexity\": 33.67533110543885, \"distinct_1\": 0.0639609375, \"distinct_2\": 0.2740568285689732, \"distinct_3\": 0.4319442491288926, \"mauve\": 0.024969167666139103, \"generation\": 13, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.650109134228356, \"self_bleu\": 0.01228111626962466, \"ece\": 0.1090129944620413, \"effective_rank\": 59.627950190233996, \"perplexity\": 34.604176016757435, \"distinct_1\": 0.06384375, \"distinct_2\": 0.272697442948773, \"distinct_3\": 0.42962390037344333, \"mauve\": 0.02621373520173196, \"generation\": 14, \"effective_alpha\": 0.5},\n  {\"token_entropy\": 2.69464270902633, \"self_bleu\": 0.012265766691581312, \"ece\": 0.10333076799124105, \"effective_rank\": 59.6681909643878, \"perplexity\": 34.322892091319574, \"distinct_1\": 0.0637734375, \"distinct_2\": 0.2715255587934281, \"distinct_3\": 0.42750667979187174, \"mauve\": 0.02641633548512619, \"generation\": 15, \"effective_alpha\": 0.5},\n]\n\n\ndef orient(series, name):\n    return -series.copy() if name in LOWER_IS_WORSE else series.copy()\n\n\ndef _build_lag_matrix(y, x, max_lag):\n    T = len(y)\n    n = T - max_lag\n    Y = y[max_lag:]\n    cols_r = [np.ones(n)]\n    for lag in range(1, max_lag + 1):\n        cols_r.append(y[max_lag - lag: T - lag])\n    cols_u = list(cols_r)\n    for lag in range(1, max_lag + 1):\n        cols_u.append(x[max_lag - lag: T - lag])\n    return Y, np.column_stack(cols_r), np.column_stack(cols_u)\n\n\ndef _granger_f_stat(y, x, max_lag):\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\n    n = len(Y)\n    q = max_lag\n    try:\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\n    except np.linalg.LinAlgError:\n        return np.nan\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\n    k_u = X_u.shape[1]\n    df_resid = n - k_u\n    if df_resid <= 0 or rss_u < 1e-15:\n        return np.nan\n    return ((rss_r - rss_u) / q) / (rss_u / df_resid)\n\n\ndef permutation_granger_test(x, y, max_lag=1, n_perm=1000, seed=42, difference=True):\n    x = np.asarray(x, dtype=float)\n    y = np.asarray(y, dtype=float)\n    if difference:\n        x = np.diff(x)\n        y = np.diff(y)\n    f_obs = _granger_f_stat(y, x, max_lag)\n    if np.isnan(f_obs):\n        return {\"f_stat\": None, \"p_value\": None, \"significant\": False}\n    rng = np.random.default_rng(seed)\n    null_f = np.empty(n_perm)\n    for i in range(n_perm):\n        null_f[i] = _granger_f_stat(y, rng.permutation(x), max_lag)\n    valid_null = null_f[~np.isnan(null_f)]\n    if len(valid_null) == 0:\n        return {\"f_stat\": round(float(f_obs), 4), \"p_value\": None, \"significant\": False}\n    p_value = (np.sum(valid_null >= f_obs) + 1) / (len(valid_null) + 1)\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\n    rss_r = np.sum((Y - X_r @ np.linalg.lstsq(X_r, Y, rcond=None)[0]) ** 2)\n    rss_u = np.sum((Y - X_u @ np.linalg.lstsq(X_u, Y, rcond=None)[0]) ** 2)\n    f2 = (rss_r - rss_u) / rss_u if rss_u > 1e-15 else None\n    return {\n        \"f_stat\": round(float(f_obs), 4),\n        \"p_value\": round(float(p_value), 6),\n        \"null_mean\": round(float(np.mean(valid_null)), 4),\n        \"null_std\": round(float(np.std(valid_null)), 4),\n        \"effect_size_f2\": round(float(f2), 4) if f2 is not None else None,\n        \"significant\": bool(p_value < 0.05),\n    }\n\n\ndef bh_fdr(p_values, alpha=0.05):\n    pv = np.array(p_values, dtype=float)\n    n = len(pv)\n    valid = ~np.isnan(pv)\n    adjusted = np.full(n, np.nan)\n    if valid.sum() == 0:\n        return adjusted.tolist(), [False] * n\n    idx = np.where(valid)[0]\n    p_valid = pv[idx]\n    sorted_idx = np.argsort(p_valid)\n    ranks = np.empty_like(sorted_idx)\n    ranks[sorted_idx] = np.arange(1, len(p_valid) + 1)\n    m = len(p_valid)\n    adj = p_valid * m / ranks\n    adj_sorted = adj[sorted_idx].copy()\n    for i in range(m - 2, -1, -1):\n        adj_sorted[i] = min(adj_sorted[i], adj_sorted[i + 1])\n    adj_sorted = np.minimum(adj_sorted, 1.0)\n    adj_final = np.empty(m)\n    adj_final[sorted_idx] = adj_sorted\n    for i, ix in enumerate(idx):\n        adjusted[ix] = adj_final[i]\n    significant = [(adjusted[i] < alpha if not np.isnan(adjusted[i]) else False) for i in range(n)]\n    return adjusted.tolist(), significant\n\n\ndef naive_xcorr(c, d, cn, dn, max_lag=5):\n    x, y = orient(c, cn), orient(d, dn)\n    n = len(x)\n    best_lag, best_r, best_p = 0, 0.0, 1.0\n    all_lags = []\n    for lag in range(-max_lag, max_lag + 1):\n        if lag >= 0:\n            a, b = x[lag:], y[:n - lag]\n        else:\n            a, b = x[:n + lag], y[-lag:]\n        if len(a) < 4:\n            continue\n        r, p = stats.pearsonr(a, b)\n        all_lags.append({\"lag\": int(lag), \"r\": round(float(r), 4), \"p\": round(float(p), 6)})\n        if abs(r) > abs(best_r):\n            best_lag, best_r, best_p = lag, r, p\n    return {\n        \"method\": \"naive_xcorr\",\n        \"peak_lag\": int(best_lag),\n        \"r\": round(float(best_r), 4),\n        \"p_value\": round(float(best_p), 6),\n        \"significant\": bool(best_p < ALPHA_SIG),\n        \"all_lags\": all_lags,\n    }\n\n\ndef diff_xcorr(c, d, cn, dn, max_lag=5):\n    dx, dy = np.diff(orient(c, cn)), np.diff(orient(d, dn))\n    n = len(dx)\n    best_lag, best_r, best_p = 0, 0.0, 1.0\n    all_lags = []\n    for lag in range(-max_lag, max_lag + 1):\n        if lag >= 0:\n            a, b = dx[lag:], dy[:n - lag]\n        else:\n            a, b = dx[:n + lag], dy[-lag:]\n        if len(a) < 4:\n            continue\n        if np.std(a) < 1e-12 or np.std(b) < 1e-12:\n            continue\n        r, p = stats.pearsonr(a, b)\n        all_lags.append({\"lag\": int(lag), \"r\": round(float(r), 4), \"p\": round(float(p), 6)})\n        if abs(r) > abs(best_r):\n            best_lag, best_r, best_p = lag, r, p\n    return {\n        \"method\": \"diff_xcorr\",\n        \"peak_lag\": int(best_lag),\n        \"r\": round(float(best_r), 4),\n        \"p_value\": round(float(best_p), 6),\n        \"significant\": bool(best_p < ALPHA_SIG),\n        \"all_lags\": all_lags,\n    }\n\n\ndef _onset_gen(series, name):\n    s = orient(series, name)\n    base, sigma = s[0], np.std(s)\n    if sigma < 1e-12:\n        return None\n    thresh = base + 3.0 * sigma\n    for i in range(1, len(s)):\n        if s[i] > thresh:\n            return i\n    return None\n\n\ndef threshold_onset(c, d, cn, dn):\n    c_onset = _onset_gen(c, cn)\n    d_onset = _onset_gen(d, dn)\n    if c_onset is not None and d_onset is not None:\n        lead_time = d_onset - c_onset\n        significant = lead_time > 0\n    else:\n        lead_time = None\n        significant = False\n    return {\n        \"method\": \"threshold_onset\",\n        \"canary_onset\": c_onset,\n        \"downstream_onset\": d_onset,\n        \"lead_time\": lead_time,\n        \"significant\": significant,\n        \"threshold\": \"true_3sigma_d105\",\n    }\n\n\ndef perm_granger(c, d, cn, dn, seed):\n    x = orient(c, cn)\n    y = orient(d, dn)\n    result = permutation_granger_test(x, y, max_lag=1, n_perm=N_PERM, seed=seed, difference=True)\n    return {\n        \"method\": \"perm_granger\",\n        \"f_stat\": result[\"f_stat\"],\n        \"p_value\": result[\"p_value\"],\n        \"null_mean\": result.get(\"null_mean\"),\n        \"null_std\": result.get(\"null_std\"),\n        \"effect_size_f2\": result.get(\"effect_size_f2\"),\n        \"significant\": bool(result[\"p_value\"] < ALPHA_SIG) if result[\"p_value\"] is not None else False,\n    }\n\n\ndef ty_granger(c, d, cn, dn, max_order=2):\n    x = orient(c, cn)\n    y = orient(d, dn)\n    n = len(x)\n    d_max = 0\n    for series in [x, y]:\n        try:\n            result = adfuller(series, maxlag=min(3, n // 3 - 1))\n            if result[1] > 0.05:\n                d_max = max(d_max, 1)\n        except:\n            d_max = max(d_max, 1)\n    best_k, best_aic = 1, np.inf\n    data = np.column_stack([x, y])\n    for k in range(1, max_order + 1):\n        try:\n            model = VAR(data)\n            result = model.fit(k)\n            if result.aic < best_aic:\n                best_k, best_aic = k, result.aic\n        except:\n            continue\n    total_order = best_k + d_max\n    if total_order >= n // 2:\n        total_order = max(1, n // 2 - 1)\n    try:\n        model = VAR(data)\n        result = model.fit(total_order)\n        test_result = result.test_causality(causing=1, caused=0, kind=\"f\")\n        f_stat = float(test_result.test_statistic)\n        p_value = float(test_result.pvalue)\n        return {\n            \"method\": \"ty_granger\",\n            \"f_stat\": round(f_stat, 4),\n            \"p_value\": round(p_value, 4),\n            \"significant\": bool(p_value < ALPHA_SIG),\n            \"order\": total_order,\n            \"k_opt\": best_k,\n            \"d_max\": d_max,\n        }\n    except Exception as e:\n        return {\n            \"method\": \"ty_granger\",\n            \"f_stat\": None,\n            \"p_value\": None,\n            \"significant\": False,\n            \"error\": str(e),\n            \"order\": total_order,\n            \"k_opt\": best_k,\n            \"d_max\": d_max,\n        }\n\n\ndef main():\n    data = sorted(ALL_METRICS, key=lambda x: x[\"generation\"])\n    series = {}\n    for k in CANARIES + DOWNSTREAMS:\n        series[k] = np.array([d[k] for d in data])\n\n    n_gens = len(data)\n    seed = 42\n\n    pairs = [{\"canary\": c, \"downstream\": d} for c in CANARIES for d in DOWNSTREAMS]\n\n    pair_results = []\n    perm_pval_fwd, perm_pval_rev = [], []\n    diff_pval_fwd, diff_pval_rev = [], []\n\n    for pair in pairs:\n        cn, dn = pair[\"canary\"], pair[\"downstream\"]\n        c, d = series[cn], series[dn]\n\n        fwd_naive = naive_xcorr(c, d, cn, dn)\n        fwd_diff = diff_xcorr(c, d, cn, dn)\n        fwd_onset = threshold_onset(c, d, cn, dn)\n        fwd_perm = perm_granger(c, d, cn, dn, seed)\n        fwd_ty = ty_granger(c, d, cn, dn)\n\n        rev_naive = naive_xcorr(d, c, dn, cn)\n        rev_diff = diff_xcorr(d, c, dn, cn)\n        rev_onset = threshold_onset(d, c, dn, cn)\n        rev_perm = perm_granger(d, c, dn, cn, seed)\n        rev_ty = ty_granger(d, c, dn, cn)\n\n        result = {\n            \"canary\": cn, \"downstream\": dn,\n            \"forward\": {\n                \"naive_xcorr\": fwd_naive, \"diff_xcorr\": fwd_diff,\n                \"threshold_onset\": fwd_onset, \"perm_granger\": fwd_perm,\n                \"ty_granger\": fwd_ty,\n            },\n            \"reverse\": {\n                \"naive_xcorr\": rev_naive, \"diff_xcorr\": rev_diff,\n                \"threshold_onset\": rev_onset, \"perm_granger\": rev_perm,\n                \"ty_granger\": rev_ty,\n            },\n        }\n\n        perm_pval_fwd.append(fwd_perm[\"p_value\"] if fwd_perm[\"p_value\"] is not None else np.nan)\n        perm_pval_rev.append(rev_perm[\"p_value\"] if rev_perm[\"p_value\"] is not None else np.nan)\n        diff_pval_fwd.append(fwd_diff[\"p_value\"] if fwd_diff[\"p_value\"] is not None else np.nan)\n        diff_pval_rev.append(rev_diff[\"p_value\"] if rev_diff[\"p_value\"] is not None else np.nan)\n        pair_results.append(result)\n\n    perm_adj_fwd, perm_sig_fwd = bh_fdr(perm_pval_fwd)\n    perm_adj_rev, perm_sig_rev = bh_fdr(perm_pval_rev)\n    diff_adj_fwd, diff_sig_fwd = bh_fdr(diff_pval_fwd)\n    diff_adj_rev, diff_sig_rev = bh_fdr(diff_pval_rev)\n\n    for i, r in enumerate(pair_results):\n        r[\"forward\"][\"perm_granger\"][\"p_fdr\"] = round(perm_adj_fwd[i], 6) if not np.isnan(perm_adj_fwd[i]) else None\n        r[\"forward\"][\"perm_granger\"][\"significant_fdr\"] = perm_sig_fwd[i]\n        r[\"reverse\"][\"perm_granger\"][\"p_fdr\"] = round(perm_adj_rev[i], 6) if not np.isnan(perm_adj_rev[i]) else None\n        r[\"reverse\"][\"perm_granger\"][\"significant_fdr\"] = perm_sig_rev[i]\n        r[\"forward\"][\"diff_xcorr\"][\"p_fdr\"] = round(diff_adj_fwd[i], 6) if not np.isnan(diff_adj_fwd[i]) else None\n        r[\"forward\"][\"diff_xcorr\"][\"significant_fdr\"] = diff_sig_fwd[i]\n        r[\"reverse\"][\"diff_xcorr\"][\"p_fdr\"] = round(diff_adj_rev[i], 6) if not np.isnan(diff_adj_rev[i]) else None\n        r[\"reverse\"][\"diff_xcorr\"][\"significant_fdr\"] = diff_sig_rev[i]\n\n    print(\"=\" * 100)\n    print(\"5-METHOD LEAD-LAG ANALYSIS | T=15 | alpha=0.50 | seed=42 | phase_diagram_t15_a050_s42_fp32\")\n    print(\"=\" * 100)\n    print(f\"Loaded {n_gens} generations (T=15, 16 data points)\\n\")\n\n    for direction in [\"forward\", \"reverse\"]:\n        dir_label = \"FORWARD (canary -> downstream)\" if direction == \"forward\" else \"REVERSE (downstream -> canary)\"\n        print(f\"\\n{'=' * 100}\")\n        print(f\"  {dir_label}\")\n        print(f\"{'=' * 100}\")\n        print(f\"  {'Pair':<30} {'Naive XCorr':<20} {'Diff XCorr(FDR)':<20} {'Threshold':<18} {'PermG(FDR)':<20} {'TY Granger':<15}\")\n        print(\"-\" * 130)\n        for r in pair_results:\n            label = f\"{r['canary']}<{r['downstream']}\"\n            d = r[direction]\n\n            naive_str = f\"lag={d['naive_xcorr']['peak_lag']} r={d['naive_xcorr']['r']:.3f} {'*' if d['naive_xcorr']['significant'] else ''}\"\n            diff_p = d['diff_xcorr'].get('p_value')\n            diff_str = f\"lag={d['diff_xcorr']['peak_lag']} r={d['diff_xcorr']['r']:.3f} {'*' if d['diff_xcorr'].get('significant_fdr', False) else ''}\" if diff_p is not None else \"N/A\"\n            onset_str = f\"c={d['threshold_onset']['canary_onset']} d={d['threshold_onset']['downstream_onset']} {'*' if d['threshold_onset']['significant'] else ''}\"\n            perm_str = f\"F={d['perm_granger']['f_stat']:.2f} p={d['perm_granger']['p_value']:.4f} {'*' if d['perm_granger'].get('significant_fdr', False) else ''}\" if d['perm_granger']['f_stat'] else \"N/A\"\n            ty_str = f\"F={d['ty_granger']['f_stat']:.2f} p={d['ty_granger']['p_value']:.4f} {'*' if d['ty_granger']['significant'] else ''}\" if d['ty_granger']['f_stat'] else \"N/A\"\n            print(f\"  {label:<30} {naive_str:<20} {diff_str:<20} {onset_str:<18} {perm_str:<20} {ty_str:<15}\")\n\n    print(f\"\\n{'=' * 100}\")\n    print(\"  CONSENSUS (forward, D111 direction filter: peak_lag < 0 for xcorr)\")\n    print(f\"{'=' * 100}\")\n    consensus = []\n    for r in pair_results:\n        f = r[\"forward\"]\n        votes = 0\n        methods_sig = []\n        if f[\"naive_xcorr\"][\"significant\"] and f[\"naive_xcorr\"][\"peak_lag\"] < 0:\n            votes += 1; methods_sig.append(\"naive\")\n        if f[\"diff_xcorr\"].get(\"significant_fdr\", False) and f[\"diff_xcorr\"][\"peak_lag\"] < 0:\n            votes += 1; methods_sig.append(\"diff\")\n        if f[\"threshold_onset\"][\"significant\"]:\n            votes += 1; methods_sig.append(\"threshold\")\n        if f[\"perm_granger\"].get(\"significant_fdr\", False):\n            votes += 1; methods_sig.append(\"perm\")\n        if f[\"ty_granger\"][\"significant\"]:\n            votes += 1; methods_sig.append(\"ty\")\n        label = f\"{r['canary']}<{r['downstream']}\"\n        consensus.append({\"pair\": label, \"votes\": votes, \"methods\": methods_sig})\n        print(f\"  {label:<30} {votes}/5  [{', '.join(methods_sig) if methods_sig else 'none'}]\")\n\n    summary = {\n        \"PermG_fwd\": f\"{sum(perm_sig_fwd)}/8\",\n        \"PermG_rev\": f\"{sum(perm_sig_rev)}/8\",\n        \"diff_xcorr_fdr_fwd\": f\"{sum(diff_sig_fwd)}/8\",\n        \"diff_xcorr_fdr_rev\": f\"{sum(diff_sig_rev)}/8\",\n        \"naive_xcorr_fwd_D111\": f\"{sum(1 for r in pair_results if r['forward']['naive_xcorr']['significant'] and r['forward']['naive_xcorr']['peak_lag'] < 0)}/8\",\n        \"threshold_onset_3sigma\": f\"{sum(1 for r in pair_results if r['forward']['threshold_onset']['significant'])}/8\",\n        \"TY_granger\": f\"{sum(1 for r in pair_results if r['forward']['ty_granger']['significant'])}/8\",\n        \"K_ge_3\": f\"{sum(1 for c in consensus if c['votes'] >= 3)}/8\",\n        \"K_ge_4\": f\"{sum(1 for c in consensus if c['votes'] >= 4)}/8\",\n        \"robust_pairs\": f\"{sum(1 for c in consensus if c['votes'] >= 3)}/8\",\n    }\n\n    print(f\"\\n{'=' * 100}\")\n    print(\"  SUMMARY\")\n    print(f\"{'=' * 100}\")\n    for k, v in summary.items():\n        print(f\"  {k:<30} {v}\")\n\n    print(f\"\\n{'=' * 100}\")\n    print(\"  DRIFT STATISTICS (gen0 -> gen15)\")\n    print(f\"{'=' * 100}\")\n    g0, gN = data[0], data[-1]\n    for metric in [\"token_entropy\", \"ece\", \"perplexity\", \"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\", \"effective_rank\"]:\n        v0, vN = g0[metric], gN[metric]\n        drift = (vN - v0) / abs(v0) * 100 if abs(v0) > 1e-12 else float('inf')\n        print(f\"  {metric:<20} {v0:.4f} -> {vN:.4f}  ({drift:+.2f}%)\")\n\n    full_results = {\n        \"meta\": {\n            \"exp_id\": \"phase_diagram_t15_a050_s42_fp32\",\n            \"alpha\": 0.50,\n            \"seed\": 42,\n            \"T\": 15,\n            \"n_gens\": n_gens,\n            \"n_perm\": N_PERM,\n            \"canaries\": CANARIES,\n            \"downstreams\": DOWNSTREAMS,\n            \"threshold_criterion\": \"true_3sigma_d105\",\n            \"D111_direction\": \"peak_lag < 0 (C009 corrected)\",\n            \"D105_3sigma\": \"true 3sigma (std of full series)\",\n        },\n        \"summary\": summary,\n        \"consensus\": consensus,\n        \"pairs\": [],\n    }\n\n    def clean(obj):\n        if isinstance(obj, (np.floating, np.float64)):\n            return float(obj)\n        if isinstance(obj, (np.integer,)):\n            return int(obj)\n        if isinstance(obj, np.bool_):\n            return bool(obj)\n        if isinstance(obj, dict):\n            return {k: clean(v) for k, v in obj.items()}\n        if isinstance(obj, list):\n            return [clean(v) for v in obj]\n        return obj\n\n    for r in pair_results:\n        pr = clean(r)\n        for d in [\"forward\", \"reverse\"]:\n            for m in [\"naive_xcorr\", \"diff_xcorr\"]:\n                if \"all_lags\" in pr[d][m]:\n                    del pr[d][m][\"all_lags\"]\n        full_results[\"pairs\"].append(pr)\n\n    out_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32/data/5method_leadlag.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(full_results, f, indent=2)\n    print(f\"\\nSaved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T17:58:58.668061+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32/run_analysis.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T17:58:58.668221+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32 && python run_analysis.py 2>&1",
  "description": "Run 5-method lead-lag analysis",
  "timeout": "300000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32 && python run_analysis.py 2>&1",
    "description": "Run 5-method lead-lag analysis",
    "timeout": "300000"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T17:58:58.668372+00:00_

Exit code 127
/bin/bash: line 1: python: command not found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T17:58:58.668496+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32 && python3 run_analysis.py 2>&1",
  "description": "Run 5-method lead-lag analysis with python3",
  "timeout": "300000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32 && python3 run_analysis.py 2>&1",
    "description": "Run 5-method lead-lag analysis with python3",
    "timeout": "300000"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T17:58:58.668617+00:00_

Exit code 1
Traceback (most recent call last):
  File "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32/run_analysis.py", line 7, in &lt;module>
    from statsmodels.tsa.stattools import adfuller
ModuleNotFoundError: No module named 'statsmodels'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T17:58:58.668735+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pip3 install statsmodels 2>&1 | tail -3",
  "description": "Install statsmodels",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Bash",
  "tool_args": {
    "command": "pip3 install statsmodels 2>&1 | tail -3",
    "description": "Install statsmodels",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T17:58:58.668850+00:00_

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T17:58:58.668965+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pip3 install --user statsmodels 2>&1 | tail -3",
  "description": "Install statsmodels with --user flag",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Bash",
  "tool_args": {
    "command": "pip3 install --user statsmodels 2>&1 | tail -3",
    "description": "Install statsmodels with --user flag",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T17:58:58.669080+00:00_

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T17:58:58.669196+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -m venv /tmp/analysis_venv && source /tmp/analysis_venv/bin/activate && pip install numpy scipy statsmodels 2>&1 | tail -5",
  "description": "Create venv and install dependencies",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -m venv /tmp/analysis_venv && source /tmp/analysis_venv/bin/activate && pip install numpy scipy statsmodels 2>&1 | tail -5",
    "description": "Create venv and install dependencies",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T17:58:58.669355+00:00_

Requirement already satisfied: pandas!=2.1.0,>=1.4 in /tmp/analysis_venv/lib/python3.14/site-packages (from statsmodels) (3.0.3)
Requirement already satisfied: patsy>=0.5.6 in /tmp/analysis_venv/lib/python3.14/site-packages (from statsmodels) (1.0.2)
Requirement already satisfied: packaging>=21.3 in /tmp/analysis_venv/lib/python3.14/site-packages (from statsmodels) (26.2)
Requirement already satisfied: python-dateutil>=2.8.2 in /tmp/analysis_venv/lib/python3.14/site-packages (from pandas!=2.1.0,>=1.4->statsmodels) (2.9.0.post0)
Requirement already satisfied: six>=1.5 in /tmp/analysis_venv/lib/python3.14/site-packages (from python-dateutil>=2.8.2->pandas!=2.1.0,>=1.4->statsmodels) (1.17.0)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T17:58:58.669480+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "source /tmp/analysis_venv/bin/activate && cd /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32 && python run_analysis.py 2>&1",
  "description": "Run analysis with venv",
  "timeout": "300000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Bash",
  "tool_args": {
    "command": "source /tmp/analysis_venv/bin/activate && cd /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32 && python run_analysis.py 2>&1",
    "description": "Run analysis with venv",
    "timeout": "300000"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T17:58:58.669634+00:00_

====================================================================================================
5-METHOD LEAD-LAG ANALYSIS | T=15 | alpha=0.50 | seed=42 | phase_diagram_t15_a050_s42_fp32
====================================================================================================
Loaded 16 generations (T=15, 16 data points)


====================================================================================================
  FORWARD (canary -> downstream)
====================================================================================================
  Pair                           Naive XCorr          Diff XCorr(FDR)      Threshold          PermG(FDR)           TY Granger     
----------------------------------------------------------------------------------------------------------------------------------
  token_entropy<distinct_1       lag=5 r=-0.844 *     lag=-1 r=0.833 *     c=1 d=10 *         F=1412.51 p=0.0002 * F=0.49 p=0.6962 
  token_entropy<distinct_2       lag=5 r=-0.889 *     lag=-4 r=0.751 *     c=1 d=None         F=438.24 p=0.0012 *  F=0.37 p=0.7772 
  token_entropy<distinct_3       lag=5 r=-0.918 *     lag=-4 r=0.711 *     c=1 d=None         F=119.40 p=0.0042 *  F=0.77 p=0.5343 
  token_entropy<mauve            lag=5 r=-0.886 *     lag=4 r=0.487        c=1 d=None         F=0.44 p=0.6029      F=2.50 p=0.1096 
  ece<distinct_1                 lag=-1 r=0.972 *     lag=-1 r=0.919 *     c=2 d=10 *         F=334.56 p=0.0002 *  F=3.03 p=0.0731 
  ece<distinct_2                 lag=1 r=0.952 *      lag=-4 r=0.838 *     c=2 d=None         F=222.87 p=0.0006 *  F=6.52 p=0.0074 *
  ece<distinct_3                 lag=2 r=0.944 *      lag=-4 r=0.807 *     c=2 d=None         F=177.82 p=0.0002 *  F=8.89 p=0.0021 *
  ece<mauve                      lag=-5 r=0.788 *     lag=4 r=0.567        c=2 d=None         F=0.61 p=0.4667      F=3.33 p=0.0565 

====================================================================================================
  R
…[truncated 3549 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T17:58:58.669819+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32/data/phase_diagram_t15_a050_s42_fp32_5method.txt",
  "content": "5-Method Lead-Lag Analysis: phase_diagram_t15_a050_s42_fp32\nalpha=0.50, seed=42, T=15 (16 generations), fp32, Pythia-410m\n\n=== SUMMARY ===\nPermG FDR forward significant:   6/8\nPermG FDR reverse significant:   0/8\ndiff_xcorr FDR forward:          6/8\ndiff_xcorr FDR reverse:          6/8\nnaive_xcorr fwd (D111 lag<0):    2/8\nthreshold_onset (3sigma):        2/8\nTY Granger:                      2/8\nK>=3 (consensus):                4/8\nK>=4:                            1/8\n\n=== FORWARD DIRECTION ASYMMETRY ===\nPermG: 6/8 forward vs 0/8 reverse — strong directional signal (canary leads downstream).\nThe 6 significant pairs: token_entropy→{distinct_1,2,3}, ece→{distinct_1,2,3}.\nOnly mauve pairs fail (both canaries), consistent with mauve's known noise floor.\n\n=== CONSENSUS BREAKDOWN ===\ntoken_entropy→distinct_1:  3/5  [diff, threshold, perm]\ntoken_entropy→distinct_2:  2/5  [diff, perm]\ntoken_entropy→distinct_3:  2/5  [diff, perm]\ntoken_entropy→mauve:       0/5\nece→distinct_1:            4/5  [naive, diff, threshold, perm]\nece→distinct_2:            3/5  [diff, perm, ty]\nece→distinct_3:            3/5  [diff, perm, ty]\nece→mauve:                 1/5  [naive]\n\n=== DRIFT STATISTICS (gen0 → gen15) ===\ntoken_entropy:  3.2342 → 2.6946  (-16.68%)\nece:            0.0108 → 0.1033  (+856.36%)\ndistinct_1:     0.0980 → 0.0638  (-34.90%)\ndistinct_2:     0.5141 → 0.2715  (-47.19%)\ndistinct_3:     0.8127 → 0.4275  (-47.40%)\nmauve:          0.0311 → 0.0264  (-15.09%)\n\n=== KEY OBSERVATION: CROSS-T COMPARISON ===\nTheory: alpha_c(T) = c_0 / sqrt(T), c_0 ≈ 1.176\n  alpha_c(5)  ≈ 0.526  → alpha=0.50 is near threshold\n  alpha_c(10) ≈ 0.372  → alpha=0.50 is above threshold\n  alpha_c(15) ≈ 0.304  → alpha=0.50 is well above threshold\n  alpha_c(20) ≈ 0.263  → alpha=0.50 is well above threshold\n\nPermG results at alpha=0.50 across T:\n  T=5:   PermG=1/8  (near alpha_c, low power due to 6 data points)\n  T=10:  PermG=6/8  (known)\n  T=15:  PermG=6/8  (this experiment)\n  T=20:  PermG=6/8  (M062)\n\nAt T=15, alpha=0.50 gives the same PermG=6/8 as T=10 and T=20.\nThis is consistent: once alpha > alpha_c(T), PermG stabilizes at ~6/8.\nThe 2 missing pairs are always the mauve pairs, which is a mauve-specific limitation.\n\nCross-comparison with T=15 alpha=0.45 (D178):\n  T=15, alpha=0.45: PermG=8/8\n  T=15, alpha=0.50: PermG=6/8\n\nalpha=0.45 outperforms alpha=0.50 at T=15, which is surprising but consistent\nwith the pattern seen at T=10 where alpha=0.45 also showed stronger signal than alpha=0.50.\nThis suggests the optimal alpha for lead-lag detection may be slightly below 0.50,\nnot at the maximum mixing ratio.\n\n=== CONCLUSION ===\nalpha=0.50 at T=15 produces robust forward causation signal (PermG=6/8, 0/8 reverse).\nResult confirms alpha=0.50 >> alpha_c(15)≈0.304. Phase diagram prediction validated.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32/data/phase_diagram_t15_a050_s42_fp32_5method.txt",
    "content": "5-Method Lead-Lag Analysis: phase_diagram_t15_a050_s42_fp32\nalpha=0.50, seed=42, T=15 (16 generations), fp32, Pythia-410m\n\n=== SUMMARY ===\nPermG FDR forward significant:   6/8\nPermG FDR reverse significant:   0/8\ndiff_xcorr FDR forward:          6/8\ndiff_xcorr FDR reverse:          6/8\nnaive_xcorr fwd (D111 lag<0):    2/8\nthreshold_onset (3sigma):        2/8\nTY Granger:                      2/8\nK>=3 (consensus):                4/8\nK>=4:                            1/8\n\n=== FORWARD DIRECTION ASYMMETRY ===\nPermG: 6/8 forward vs 0/8 reverse — strong directional signal (canary leads downstream).\nThe 6 significant pairs: token_entropy→{distinct_1,2,3}, ece→{distinct_1,2,3}.\nOnly mauve pairs fail (both canaries), consistent with mauve's known noise floor.\n\n=== CONSENSUS BREAKDOWN ===\ntoken_entropy→distinct_1:  3/5  [diff, threshold, perm]\ntoken_entropy→distinct_2:  2/5  [diff, perm]\ntoken_entropy→distinct_3:  2/5  [diff, perm]\ntoken_entropy→mauve:       0/5\nece→distinct_1:            4/5  [naive, diff, threshold, perm]\nece→distinct_2:            3/5  [diff, perm, ty]\nece→distinct_3:            3/5  [diff, perm, ty]\nece→mauve:                 1/5  [naive]\n\n=== DRIFT STATISTICS (gen0 → gen15) ===\ntoken_entropy:  3.2342 → 2.6946  (-16.68%)\nece:            0.0108 → 0.1033  (+856.36%)\ndistinct_1:     0.0980 → 0.0638  (-34.90%)\ndistinct_2:     0.5141 → 0.2715  (-47.19%)\ndistinct_3:     0.8127 → 0.4275  (-47.40%)\nmauve:          0.0311 → 0.0264  (-15.09%)\n\n=== KEY OBSERVATION: CROSS-T COMPARISON ===\nTheory: alpha_c(T) = c_0 / sqrt(T), c_0 ≈ 1.176\n  alpha_c(5)  ≈ 0.526  → alpha=0.50 is near threshold\n  alpha_c(10) ≈ 0.372  → alpha=0.50 is above threshold\n  alpha_c(15) ≈ 0.304  → alpha=0.50 is well above threshold\n  alpha_c(20) ≈ 0.263  → alpha=0.50 is well above threshold\n\nPermG results at alpha=0.50 across T:\n  T=5:   PermG=1/8  (near alpha_c, low power due to 6 data points)\n  T=10:  PermG=6/8  (known)\n  T=15:  PermG=6/8  (this experiment)\n  T=20:  PermG=6/8  (M062)\n\nAt T=15, alpha=0.50 gives the same PermG=6/8 as T=10 and T=20.\nThis is consistent: once alpha > alpha_c(T), PermG stabilizes at ~6/8.\nThe 2 missing pairs are always the mauve pairs, which is a mauve-specific limitation.\n\nCross-comparison with T=15 alpha=0.45 (D178):\n  T=15, alpha=0.45: PermG=8/8\n  T=15, alpha=0.50: PermG=6/8\n\nalpha=0.45 outperforms alpha=0.50 at T=15, which is surprising but consistent\nwith the pattern seen at T=10 where alpha=0.45 also showed stronger signal than alpha=0.50.\nThis suggests the optimal alpha for lead-lag detection may be slightly below 0.50,\nnot at the maximum mixing ratio.\n\n=== CONCLUSION ===\nalpha=0.50 at T=15 produces robust forward causation signal (PermG=6/8, 0/8 reverse).\nResult confirms alpha=0.50 >> alpha_c(15)≈0.304. Phase diagram prediction validated.\n"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T17:58:58.669990+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32/data/phase_diagram_t15_a050_s42_fp32_5method.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T17:58:58.670133+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "phase_diagram_t15_a050_s42_fp32_5method_leadlag",
  "type": "data",
  "description": "5-method lead-lag analysis JSON for T=15 alpha=0.50 s42 fp32. PermG=6/8 fwd, 0/8 rev. K>=3: 4/8.",
  "project": "distrib_canary_collapse",
  "exp_id": "phase_diagram_t15_a050_s42_fp32",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32/data/5method_leadlag.json",
  "tags": "['phase_diagram', '5method', 'T15', 'alpha050', 'lead-lag']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "phase_diagram_t15_a050_s42_fp32_5method_leadlag",
    "type": "data",
    "description": "5-method lead-lag analysis JSON for T=15 alpha=0.50 s42 fp32. PermG=6/8 fwd, 0/8 rev. K>=3: 4/8.",
    "project": "distrib_canary_collapse",
    "exp_id": "phase_diagram_t15_a050_s42_fp32",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32/data/5method_leadlag.json",
    "tags": "['phase_diagram', '5method', 'T15', 'alpha050', 'lead-lag']"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T17:58:58.670296+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_4bba5c\", \"name\": \"phase_diagram_t15_a050_s42_fp32_5method_leadlag\", \"type\": \"data\", \"description\": \"5-method lead-lag analysis JSON for T=15 alpha=0.50 s42 fp32. PermG=6/8 fwd, 0/8 rev. K>=3: 4/8.\", \"path\": \"projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32/data/5method_leadlag_4bba5c.json\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": \"phase_diagram_t15_a050_s42_fp32\", \"skill\": \"\", \"created_at\": \"2026-05-21T17:58:18.082865+00:00\", \"tags\": [\"phase_diagram\", \"5method\", \"T15\", \"alpha050\", \"lead-lag\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T17:58:58.670442+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "phase_diagram_t15_a050_s42_fp32_5method_summary",
  "type": "report",
  "description": "Text summary of 5-method analysis for T=15 alpha=0.50 with cross-T comparison. PermG=6/8, consistent with T=10 and T=20.",
  "project": "distrib_canary_collapse",
  "exp_id": "phase_diagram_t15_a050_s42_fp32",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32/data/phase_diagram_t15_a050_s42_fp32_5method.txt",
  "tags": "['phase_diagram', 'summary', 'T15', 'alpha050']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "phase_diagram_t15_a050_s42_fp32_5method_summary",
    "type": "report",
    "description": "Text summary of 5-method analysis for T=15 alpha=0.50 with cross-T comparison. PermG=6/8, consistent with T=10 and T=20.",
    "project": "distrib_canary_collapse",
    "exp_id": "phase_diagram_t15_a050_s42_fp32",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32/data/phase_diagram_t15_a050_s42_fp32_5method.txt",
    "tags": "['phase_diagram', 'summary', 'T15', 'alpha050']"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T17:58:58.670588+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_bebec7\", \"name\": \"phase_diagram_t15_a050_s42_fp32_5method_summary\", \"type\": \"report\", \"description\": \"Text summary of 5-method analysis for T=15 alpha=0.50 with cross-T comparison. PermG=6/8, consistent with T=10 and T=20.\", \"path\": \"projects/distrib_canary_collapse/artifacts/phase_diagram_t15_a050_s42_fp32/report/phase_diagram_t15_a050_s42_fp32_5method.txt\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": \"phase_diagram_t15_a050_s42_fp32\", \"skill\": \"\", \"created_at\": \"2026-05-21T17:58:20.898454+00:00\", \"tags\": [\"phase_diagram\", \"summary\", \"T15\", \"alpha050\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T17:58:58.670715+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "phase_diagram_t15_a050_s42_fp32",
  "field": "status",
  "value": "DONE",
  "project": "distrib_canary_collapse",
  "spec": "{'checkpoint_path': '/root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t15_a050_s42_fp32/', 'log_path': '~/runs/distrib_canary_collapse/phase_diagram_t15_a050_s42_fp32.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "phase_diagram_t15_a050_s42_fp32",
    "field": "status",
    "value": "DONE",
    "project": "distrib_canary_collapse",
    "spec": "{'checkpoint_path': '/root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t15_a050_s42_fp32/', 'log_path': '~/runs/distrib_canary_collapse/phase_diagram_t15_a050_s42_fp32.log'}"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T17:58:58.670842+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.5143}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T17:58:58.670965+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "phase_diagram_t15_a050_s42_fp32",
  "field": "conclusion",
  "value": "success",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "phase_diagram_t15_a050_s42_fp32",
    "field": "conclusion",
    "value": "success",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T17:58:58.671132+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"phase_diagram_t15_a050_s42_fp32\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T11:27:36.126Z\", \"updated_at\": \"2026-05-21T17:58:27.042Z\", \"hypothesis\": \"Phase Diagram T=15 α=0.50: theory predicts α_c(15)≈0.304, so α=0.50 is well above threshold. PermG should detect contamination at T=15. If PermG>0/8, confirms theory and maps T=15 row of detection phase diagram. Combined with T=15 α=0.45 result, establishes detection power at intermediate generation counts.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --data_dir data/wikitext103_5k --synthetic_ratio 0.50 --num_generations 15 --steps_per_gen 5000 --output_dir results/phase_diagram/t15_a050_s42_fp32 --seed 42\\\"\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:4\"], \"pid\": \"505241\", \"log_path\": \"~/runs/distrib_canary_collapse/phase_diagram_t15_a050_s42_fp32.log\", \"submitted_at\": \"2026-05-21T11:32:11.160Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-21T17:51:42.833Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T17:51:48.625852+00:00\"}]}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8956}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T17:58:58.671291+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "phase_diagram_t15_a050_s42_fp32",
  "field": "status",
  "value": "DONE",
  "project": "distrib_canary_collapse",
  "spec": "{'checkpoint_path': '/root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t15_a050_s42_fp32/', 'log_path': '~/runs/distrib_canary_collapse/phase_diagram_t15_a050_s42_fp32.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "phase_diagram_t15_a050_s42_fp32",
    "field": "status",
    "value": "DONE",
    "project": "distrib_canary_collapse",
    "spec": "{'checkpoint_path': '/root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t15_a050_s42_fp32/', 'log_path': '~/runs/distrib_canary_collapse/phase_diagram_t15_a050_s42_fp32.log'}"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T17:58:58.671433+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition ANALYZING → DONE(success) without metrics. Set metrics first, or use conclusion=negative/failed.\", \"metadata\": {\"elapsed_seconds\": 0.5376}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T17:58:58.671564+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "phase_diagram_t15_a050_s42_fp32",
  "field": "metrics",
  "value": "{'PermG_fwd': '6/8', 'PermG_rev': '0/8', 'diff_xcorr_fdr_fwd': '6/8', 'K_ge_3': '4/8', 'threshold_onset_3sigma': '2/8', 'TY_granger': '2/8', 'token_entropy_drift_pct': -16.68, 'ece_drift_pct': 856.36, 'distinct_2_drift_pct': -47.19, 'mauve_drift_pct': -15.09}",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "phase_diagram_t15_a050_s42_fp32",
    "field": "metrics",
    "value": "{'PermG_fwd': '6/8', 'PermG_rev': '0/8', 'diff_xcorr_fdr_fwd': '6/8', 'K_ge_3': '4/8', 'threshold_onset_3sigma': '2/8', 'TY_granger': '2/8', 'token_entropy_drift_pct': -16.68, 'ece_drift_pct': 856.36, 'distinct_2_drift_pct': -47.19, 'mauve_drift_pct': -15.09}",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T17:58:58.671742+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"phase_diagram_t15_a050_s42_fp32\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T11:27:36.126Z\", \"updated_at\": \"2026-05-21T17:58:38.125Z\", \"hypothesis\": \"Phase Diagram T=15 α=0.50: theory predicts α_c(15)≈0.304, so α=0.50 is well above threshold. PermG should detect contamination at T=15. If PermG>0/8, confirms theory and maps T=15 row of detection phase diagram. Combined with T=15 α=0.45 result, establishes detection power at intermediate generation counts.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --data_dir data/wikitext103_5k --synthetic_ratio 0.50 --num_generations 15 --steps_per_gen 5000 --output_dir results/phase_diagram/t15_a050_s42_fp32 --seed 42\\\"\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:4\"], \"pid\": \"505241\", \"log_path\": \"~/runs/distrib_canary_collapse/phase_diagram_t15_a050_s42_fp32.log\", \"submitted_at\": \"2026-05-21T11:32:11.160Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-21T17:51:42.833Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T17:51:48.625852+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"PermG_fwd\": \"6/8\", \"PermG_rev\": \"0/8\", \"diff_xcorr_fdr_fwd\": \"6/8\", \"K_ge_3\": \"4/8\", \"threshold_onset_3sigma\": \"2/8\", \"TY_granger\": \"2/8\", \"token_entropy_drift_pct\": -16.68, \"ece_drift_pct\": 856.36, \"distinct_2_drift_pct\": -47.19, \"mauve_drift_pct\": -15.09}}}, \"error\": null, \"metadata\": {\"elapsed_s
…[truncated 20 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T17:58:58.671890+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "phase_diagram_t15_a050_s42_fp32",
  "field": "status",
  "value": "DONE",
  "project": "distrib_canary_collapse",
  "spec": "{'checkpoint_path': '/root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t15_a050_s42_fp32/', 'log_path': '~/runs/distrib_canary_collapse/phase_diagram_t15_a050_s42_fp32.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "phase_diagram_t15_a050_s42_fp32",
    "field": "status",
    "value": "DONE",
    "project": "distrib_canary_collapse",
    "spec": "{'checkpoint_path': '/root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t15_a050_s42_fp32/', 'log_path': '~/runs/distrib_canary_collapse/phase_diagram_t15_a050_s42_fp32.log'}"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T17:58:58.672082+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"phase_diagram_t15_a050_s42_fp32\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T11:27:36.126Z\", \"updated_at\": \"2026-05-21T17:58:47.960Z\", \"hypothesis\": \"Phase Diagram T=15 α=0.50: theory predicts α_c(15)≈0.304, so α=0.50 is well above threshold. PermG should detect contamination at T=15. If PermG>0/8, confirms theory and maps T=15 row of detection phase diagram. Combined with T=15 α=0.45 result, establishes detection power at intermediate generation counts.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python -u iterative_train.py --model_name EleutherAI/pythia-410m --data_dir data/wikitext103_5k --synthetic_ratio 0.50 --num_generations 15 --steps_per_gen 5000 --output_dir results/phase_diagram/t15_a050_s42_fp32 --seed 42\\\"\", \"server\": \"westd-17855\", \"gpu\": [\"cuda:4\"], \"pid\": \"505241\", \"log_path\": \"~/runs/distrib_canary_collapse/phase_diagram_t15_a050_s42_fp32.log\", \"submitted_at\": \"2026-05-21T11:32:11.160Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"model_name\": \"EleutherAI/pythia-410m\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t15_a050_s42_fp32/\", \"wall_clock_seconds\": 23196.8, \"gpu_hours\": 6.44}, \"reproduce\": {\"finished_at\": \"2026-05-21T17:51:42.833Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T17:51:48.625852+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"PermG_fwd\": \"6/8\", \"PermG_rev\": \"0/8\", \"diff_xcorr_fdr_fwd\": \"6/8\", \"K_ge_3\": \"4/8\", \"threshold_onset_3sigma\": \"2/8\", \"TY_granger\": \"2/8\", \"token_entropy_
…[truncated 276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-21T17:58:58.672294+00:00_

分析完成，registry 已更新为 DONE(success)。

**结果摘要：**

| 指标 | 值 |
|------|-----|
| PermG FDR forward | **6/8** |
| PermG FDR reverse | 0/8 |
| diff_xcorr FDR fwd | 6/8 |
| K≥3 consensus | 4/8 |
| threshold_onset | 2/8 |
| TY Granger | 2/8 |

**跨 T 对比（α=0.50）：**
- T=5: PermG=1/8（近 α_c≈0.526）
- T=10: PermG=6/8
- T=15: PermG=**6/8**（本实验）
- T=20: PermG=6/8

α=0.50 在 T≥10 后 PermG 稳定在 6/8，缺失的 2 对始终是 mauve 配对。α=0.50 >> α_c(15)≈0.304，理论预测验证通过。

值得注意：T=15 α=0.45 (D178) 给出 PermG=8/8，优于 α=0.50 的 6/8，说明最优检测 α 可能略低于 0.50。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410"
}
```

</details>

---
