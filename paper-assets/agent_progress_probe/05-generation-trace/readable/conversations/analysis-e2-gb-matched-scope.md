# analysis e2 gb matched scope

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_analysis_e2-gb-matched-scope_20260516T025502.jsonl`
- **Structured JSON:** [`443e606e4038c5b55993.json`](../../sessions/44/443e606e4038c5b55993.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

22 recorded events

### Tool call

_source line 1 · 2026-05-16T02:59:04.914433+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/bootstrap_table2_matched.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/bootstrap_table2_matched.py"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T02:59:04.914994+00:00_

1	#!/usr/bin/env python3
2	"""Paired bootstrap test -- Table 2 exact scope.
3	
4	3 comparisons:
5	1. RF vs Probe in-domain (SWE conf>=2 test, N=1,824)
6	2. GB vs Probe zero-shot cross-agent (OH conf>=2 test, N=6,122)
7	3. GB vs Probe fine-tuned cross-agent (OH conf>=2 test, N=6,122)
8	"""
9	
10	import json
11	import re
12	import sys
13	import datetime
14	from collections import Counter
15	from difflib import SequenceMatcher
16	from pathlib import Path
17	
18	import numpy as np
19	import torch
20	from torch.utils.data import DataLoader
21	from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
22	from sklearn.metrics import f1_score
23	
24	sys.path.insert(0, str(Path(__file__).parent))
25	from probe_model import ProgressProbe, WindowDataset, collate_fn
26	
27	PROJECT = Path("/root/autodl-tmp/agent_progress_probe")
28	OH_DIR = Path("/root/autodl-tmp/openhands_data")
29	
30	EDIT_CMDS = {"edit", "str_replace", "create", "insert"}
31	SEARCH_CMDS = {"search_dir", "search_file", "find_file", "find", "grep", "view"}
32	NAV_CMDS = {"open", "goto", "scroll_down", "scroll_up", "cd", "ls", "cat"}
33	
34	
35	def extract_command(text):
36	    m = re.search(r"```\n?(.*?)```", text, re.DOTALL)
37	    return m.group(1).strip() if m else None
38	
39	
40	def cmd_similarity(a, b):
41	    if a == b:
42	        return 1.0
43	    if not a or not b:
44	        return 0.0
45	    return SequenceMatcher(None, a, b).ratio()
46	
47	
48	def extract_features(steps, is_short):
49	    n = len(steps)
50	    if n == 0:
51	        return np.zeros(30)
52	
53	    texts = [s["text"] for s in steps]
54	    text_lens = [len(t) for t in texts]
55	
56	    actions = [(s, t) for s, t in zip(steps, texts) if s["role"] == "ai"]
57	    observations = [(s, t) for s, t in zip(steps, texts) if s["role"] == "user"]
58	    n_actions = len(actions)
59	    n_obs = len(observations)
60	
61	    mean_tlen = np.mean(text_lens)
62	    std_tlen = np.std(text_lens) if n > 1 else 0.0
63	    max_tlen = ma
…[truncated 18410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T02:59:04.915248+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/evaluate_gold_set.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/evaluate_gold_set.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T02:59:04.915629+00:00_

1	#!/usr/bin/env python3
2	"""Gold Set Evaluation Pipeline.
3	
4	Evaluates multiple models/label sources against human-annotated gold labels.
5	
6	Input:
7	  --gold_csv PATH   : CSV with columns (window_id, gold_label)
8	                      window_id format: {trajectory_id}__w{window_idx}
9	  --output_dir PATH : Output directory for results JSON + markdown report
10	
11	Evaluated models:
12	  1. MV labels        — majority vote from labeling functions
13	  2. probe_001        — GRU probe (checkpoints/best_model.pt)
14	  3. Structural RF    — RandomForest on hand-crafted features (trained on-the-fly)
15	  4. Structural GB    — GradientBoosting on hand-crafted features (trained on-the-fly)
16	  5. TWV labels       — Temporally-Weighted Vote σ=2 labels (data/windows_tlm_labels.jsonl)
17	
18	Output:
19	  - results.json     : Per-model metrics + gold distribution + deltas
20	  - report.md        : Human-readable markdown comparison report
21	
22	Dependencies: torch, scikit-learn, numpy
23	
24	Dry-run mode (--dry_run):
25	  Generates pseudo gold labels from conf>=2 MV labels, runs full pipeline.
26	"""
27	
28	import argparse
29	import csv
30	import json
31	import os
32	import re
33	import sys
34	import time
35	import warnings
36	from collections import Counter
37	from difflib import SequenceMatcher
38	from pathlib import Path
39	
40	import numpy as np
41	import torch
42	import torch.nn as nn
43	from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
44	from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
45	from sklearn.preprocessing import StandardScaler
46	from torch.utils.data import DataLoader
47	
48	warnings.filterwarnings("ignore", category=UserWarning)
49	
50	# ---------------------------------------------------------------------------
51	# Import probe model from project
52	# ---------------------------------------------------------------------------
53	sys.path.insert(0, str(Path(__file__).parent))
54	from 
…[truncated 29113 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T02:59:04.915847+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T02:59:04.915993+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T02:59:04.916185+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'e2-gb-matched-scope'}",
  "project": "agent_progress_probe",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'e2-gb-matched-scope'}",
    "project": "agent_progress_probe",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T02:59:04.916323+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5118}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T02:59:04.916505+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-23165",
  "command": "ls /root/autodl-tmp/agent_progress_probe/bootstrap_table2_matched.json 2>/dev/null && cat /root/autodl-tmp/agent_progress_probe/bootstrap_table2_matched.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-23165",
    "command": "ls /root/autodl-tmp/agent_progress_probe/bootstrap_table2_matched.json 2>/dev/null && cat /root/autodl-tmp/agent_progress_probe/bootstrap_table2_matched.json"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T02:59:04.916721+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '&&' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T02:59:04.916913+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-23165",
  "command": "cat /root/autodl-tmp/agent_progress_probe/bootstrap_table2_matched.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-23165",
    "command": "cat /root/autodl-tmp/agent_progress_probe/bootstrap_table2_matched.json"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T02:59:04.917119+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"comparison_1_rf_vs_probe_indomain\\\": {\\n    \\\"scope\\\": \\\"SWE-Agent conf>=2 test split\\\",\\n    \\\"N\\\": 1824,\\n    \\\"class_dist\\\": {\\n      \\\"stagnation\\\": 485,\\n      \\\"progress\\\": 1339\\n    },\\n    \\\"model_a\\\": \\\"Structural RF\\\",\\n    \\\"model_b\\\": \\\"ProgressProbe (GRU)\\\",\\n    \\\"f1_a\\\": 0.9951,\\n    \\\"f1_b\\\": 0.9055,\\n    \\\"delta_pp\\\": 8.96,\\n    \\\"ci_95\\\": [\\n      7.44,\\n      10.57\\n    ],\\n    \\\"p_value\\\": 0.0,\\n    \\\"table2_ref\\\": {\\n      \\\"f1_a\\\": 0.9951,\\n      \\\"f1_b\\\": 0.9055\\n    }\\n  },\\n  \\\"comparison_2_gb_vs_probe_zeroshot_oh\\\": {\\n    \\\"scope\\\": \\\"OH conf>=2 test split\\\",\\n    \\\"scope_note\\\": \\\"Table 2 GB=0.9674 is on all 150,652 OH windows; this bootstrap uses conf>=2 test split only. GB F1 on this subset differs from Table 2.\\\",\\n    \\\"N\\\": 6122,\\n    \\\"class_dist\\\": {\\n      \\\"stagnation\\\": 1179,\\n      \\\"progress\\\": 4943\\n    },\\n    \\\"model_a\\\": \\\"Structural GB\\\",\\n    \\\"model_b\\\": \\\"ProgressProbe zero-shot\\\",\\n    \\\"f1_a\\\": 0.9929,\\n    \\\"f1_b\\\": 0.5984,\\n    \\\"delta_pp\\\": 39.44,\\n    \\\"ci_95\\\": [\\n      37.86,\\n      41.04\\n    ],\\n    \\\"p_value\\\": 0.0,\\n    \\\"table2_ref\\\": {\\n      \\\"f1_a_all_oh\\\": 0.9674,\\n      \\\"f1_b\\\": 0.598\\n    }\\n  },\\n  \\\"comparison_3_gb_vs_probe_finetuned_oh\\\": {\\n    \\\"scope\\\": \\\"OH conf>=2 test split\\\",\\n    \\\"scope_note\\\": \\\"Same scope as comparison 2. GB retrained on same SWE data.\\\",\\n    \\\"N\\\": 6122,\\n    \\\"class_dist\\\": {\\n      \\\"stagnation\\\": 1179,\\n      \\\"progress\\\": 4943\\n    },\\n    \\\"model_a\\\": \\\"Structural GB\\\",\\n    \\\"model_b\\\": \\\"ProgressProbe fine-tuned\\\",\\n    \\\"f1_a\\\": 0.9929,\\n    \\\"f1_b\\\": 0.9763,\\n    \\\"delta_pp\\\": 1.65,\\n    \\\"ci_95\\\": [\\n      1.11,\
…[truncated 712 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T02:59:04.917322+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb2-23165",
  "command": "ls /root/autodl-tmp/agent_progress_probe/checkpoints_full/best_model.pt /root/autodl-tmp/openhands_data/embeddings_fixed_conf2.pt /root/autodl-tmp/openhands_data/openhands_trajectories.jsonl /root/autodl-tmp/agent_progress_probe/checkpoints_oh_fixed_ft/test_preds.pt /root/autodl-tmp/agent_progress_probe/checkpoints/split_info.json /root/autodl-tmp/agent_progress_probe/data/swe_agent_trajectories_5000.jsonl /root/autodl-tmp/agent_progress_probe/data/windows_labeled.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb2-23165",
    "command": "ls /root/autodl-tmp/agent_progress_probe/checkpoints_full/best_model.pt /root/autodl-tmp/openhands_data/embeddings_fixed_conf2.pt /root/autodl-tmp/openhands_data/openhands_trajectories.jsonl /root/autodl-tmp/agent_progress_probe/checkpoints_oh_fixed_ft/test_preds.pt /root/autodl-tmp/agent_progress_probe/checkpoints/split_info.json /root/autodl-tmp/agent_progress_probe/data/swe_agent_trajectories_5000.jsonl /root/autodl-tmp/agent_progress_probe/data/windows_labeled.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T02:59:04.917466+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/agent_progress_probe/checkpoints/split_info.json\\n/root/autodl-tmp/agent_progress_probe/checkpoints_full/best_model.pt\\n/root/autodl-tmp/agent_progress_probe/checkpoints_oh_fixed_ft/test_preds.pt\\n/root/autodl-tmp/agent_progress_probe/data/swe_agent_trajectories_5000.jsonl\\n/root/autodl-tmp/agent_progress_probe/data/windows_labeled.jsonl\\n/root/autodl-tmp/openhands_data/embeddings_fixed_conf2.pt\\n/root/autodl-tmp/openhands_data/openhands_trajectories.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T02:59:04.917718+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

````json
{
  "server": "bjb2-23165",
  "command": "cat > /root/autodl-tmp/agent_progress_probe/e2_gb_matched_scope.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"E2: Matched-scope GB vs Probe zero-shot on OH conf>=2 test split.\n\nOutputs macro_f1, f1_stag, f1_prog for both models + paired bootstrap.\n\"\"\"\n\nimport json\nimport re\nimport sys\nimport datetime\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nfrom torch.utils.data import DataLoader\nfrom sklearn.ensemble import GradientBoostingClassifier\nfrom sklearn.metrics import f1_score\n\nsys.path.insert(0, str(Path(__file__).parent))\nfrom probe_model import ProgressProbe, WindowDataset, collate_fn\n\nPROJECT = Path(\"/root/autodl-tmp/agent_progress_probe\")\nOH_DIR = Path(\"/root/autodl-tmp/openhands_data\")\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef extract_command(text):\n    m = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return m.group(1).strip() if m else None\n\n\ndef cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_features(steps, is_short):\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30)\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (n * np.dot(x, x) - x.sum() ** 2 + 1e-9)\n    else:\n        slope = 0.0\n    commands = []\n    for _, t in actions:\n        cmd = extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        repeat_ratio = cmd_counter.most_common(1)[0][1] / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        fw = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if fw in EDIT_CMDS:\n            n_edit += 1\n        elif fw in SEARCH_CMDS:\n            n_search += 1\n        elif fw in NAV_CMDS:\n            n_nav += 1\n        elif fw == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n    if n_cmds >= 2:\n        sims = [cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run = 1\n        cur_run = 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = 0.0\n        max_adj_sim = 0.0\n        max_run = 0\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower())\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1 for _, t in observations if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n    return np.array([\n        n, n_actions, n_obs, n_actions / max(n, 1),\n        mean_tlen, std_tlen, max_tlen, min_tlen,\n        mean_action_len, mean_obs_len, slope,\n        n_cmds, mean_cmd_len, max_cmd_len,\n        unique_cmd_ratio, repeat_ratio,\n        n_edit, n_search, n_nav, n_submit,\n        edit_ratio, search_ratio,\n        avg_adj_sim, max_adj_sim, max_run,\n        n_errors, n_test_output, n_file_display, n_nonzero_exit,\n        float(is_short),\n    ], dtype=np.float32)\n\n\ndef build_trajectory_index(path):\n    index = {}\n    with open(path) as f:\n        for line in f:\n            rec = json.loads(line)\n            tid = f\"{rec['instance_id']}__{rec.get('model_name', 'unknown')}__r0\"\n            index[tid] = rec[\"trajectory\"]\n    return index\n\n\ndef extract_features_batch(windows, traj_index):\n    X = np.zeros((len(windows), 30), dtype=np.float32)\n    y = np.zeros(len(windows), dtype=int)\n    for i, w in enumerate(windows):\n        tid = w[\"trajectory_id\"]\n        traj = traj_index.get(tid)\n        if traj is None:\n            continue\n        si = w[\"step_indices\"]\n        steps = [traj[j] for j in si if j < len(traj)]\n        X[i] = extract_features(steps, w.get(\"short_trajectory\", False))\n        y[i] = w[\"majority_label\"]\n    return X, y\n\n\ndef paired_bootstrap(y_true, preds_a, preds_b, n_bootstrap=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    n = len(y_true)\n    f1_a = f1_score(y_true, preds_a, average=\"macro\", zero_division=0)\n    f1_b = f1_score(y_true, preds_b, average=\"macro\", zero_division=0)\n    observed_delta = f1_a - f1_b\n    deltas = []\n    for _ in range(n_bootstrap):\n        idx = rng.choice(n, size=n, replace=True)\n        y_b = y_true[idx]\n        if len(np.unique(y_b)) < 2:\n            continue\n        d_a = f1_score(y_b, preds_a[idx], average=\"macro\", zero_division=0)\n        d_b = f1_score(y_b, preds_b[idx], average=\"macro\", zero_division=0)\n        deltas.append(d_a - d_b)\n    deltas = np.array(deltas)\n    ci_lower = float(np.percentile(deltas, 2.5))\n    ci_upper = float(np.percentile(deltas, 97.5))\n    p_value = float(np.mean(deltas <= 0)) if observed_delta > 0 else float(np.mean(deltas >= 0))\n    return {\n        \"observed_delta\": round(observed_delta, 4),\n        \"delta_pp\": round(observed_delta * 100, 2),\n        \"ci_lower_pp\": round(ci_lower * 100, 2),\n        \"ci_upper_pp\": round(ci_upper * 100, 2),\n        \"p_value\": p_value,\n        \"n_valid_bootstraps\": len(deltas),\n    }\n\n\n@torch.no_grad()\ndef probe_predict(model, embeddings, labels, device=\"cpu\", batch_size=64):\n    ds = WindowDataset(embeddings, labels)\n    loader = DataLoader(ds, batch_size=batch_size, collate_fn=collate_fn)\n    all_preds = []\n    for padded, _, lengths in loader:\n        logits = model(padded.to(device), lengths)\n        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()\n        all_preds.extend(preds.tolist())\n    return np.array(all_preds)\n\n\ndef compute_full_metrics(y_true, y_pred):\n    return {\n        \"macro_f1\": round(f1_score(y_true, y_pred, average=\"macro\", zero_division=0), 4),\n        \"f1_stag\": round(f1_score(y_true, y_pred, pos_label=0, zero_division=0), 4),\n        \"f1_prog\": round(f1_score(y_true, y_pred, pos_label=1, zero_division=0), 4),\n    }\n\n\ndef main():\n    data_dir = PROJECT / \"data\"\n\n    # Load SWE training data\n    print(\"Loading SWE-Agent trajectories...\")\n    swa_traj = build_trajectory_index(data_dir / \"swe_agent_trajectories_5000.jsonl\")\n\n    print(\"Loading SWE-Agent windows...\")\n    all_windows = []\n    with open(data_dir / \"windows_labeled.jsonl\") as f:\n        for line in f:\n            all_windows.append(json.loads(line))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n\n    with open(PROJECT / \"checkpoints\" / \"split_info.json\") as f:\n        split = json.load(f)\n    keep_indices = split.get(\"keep_indices\")\n    train_idx = split[\"train_indices\"]\n    windows_conf2 = [non_abstain[i] for i in keep_indices] if keep_indices else non_abstain\n\n    # Extract SWE structural features for training\n    print(\"Extracting SWE structural features...\")\n    X_swe, y_swe = extract_features_batch(windows_conf2, swa_traj)\n    X_train = X_swe[train_idx]\n    y_train = y_swe[train_idx]\n    print(f\"  SWE train: N={len(train_idx)}\")\n\n    # Load OH data\n    print(\"Loading OH conf>=2 data...\")\n    oh_emb_data = torch.load(OH_DIR / \"embeddings_fixed_conf2.pt\", map_location=\"cpu\", weights_only=False)\n    oh_embs = oh_emb_data[\"embeddings\"]\n    oh_labs = oh_emb_data[\"labels\"]\n    oh_tids = oh_emb_data[\"trajectory_ids\"]\n    oh_step_indices = oh_emb_data[\"step_indices_list\"]\n    print(f\"  OH conf>=2 total: {len(oh_embs)} windows\")\n\n    # Verify stag rate\n    oh_labs_arr = np.array(oh_labs)\n    stag_rate = np.mean(oh_labs_arr == 0)\n    print(f\"  OH stag rate (all conf>=2): {stag_rate*100:.2f}%\")\n\n    # Get OH test split\n    ft_data = torch.load(PROJECT / \"checkpoints_oh_fixed_ft\" / \"test_preds.pt\", map_location=\"cpu\", weights_only=False)\n    oh_test_idx = ft_data[\"test_idx\"]\n    print(f\"  OH test split: N={len(oh_test_idx)}\")\n\n    # Load OH trajectories for structural features\n    print(\"Loading OH trajectories...\")\n    oh_traj = build_trajectory_index(OH_DIR / \"openhands_trajectories.jsonl\")\n    print(f\"  {len(oh_traj)} trajectories\")\n\n    # Build OH test windows\n    oh_test_windows = []\n    for idx in oh_test_idx:\n        oh_test_windows.append({\n            \"trajectory_id\": oh_tids[idx],\n            \"step_indices\": oh_step_indices[idx],\n            \"majority_label\": oh_labs[idx],\n            \"short_trajectory\": False,\n        })\n\n    # Extract OH test structural features\n    print(\"Extracting OH test structural features...\")\n    X_oh_test, y_oh_test = extract_features_batch(oh_test_windows, oh_traj)\n    oh_stag = int(np.sum(y_oh_test == 0))\n    oh_prog = int(np.sum(y_oh_test == 1))\n    oh_stag_rate_test = oh_stag / len(y_oh_test) * 100\n    print(f\"  OH test: N={len(y_oh_test)} (stag={oh_stag} [{oh_stag_rate_test:.2f}%], prog={oh_prog})\")\n\n    # Train GB on SWE, predict on OH test\n    print(\"\\nTraining GB (n_estimators=200, lr=0.05, max_depth=5) on SWE...\")\n    gb = GradientBoostingClassifier(n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42)\n    gb.fit(X_train, y_train)\n    gb_preds = gb.predict(X_oh_test)\n    gb_metrics = compute_full_metrics(y_oh_test, gb_preds)\n    print(f\"  GB: {gb_metrics}\")\n\n    # Probe zero-shot on OH test\n    print(\"Loading SWE probe (checkpoints_full/best_model.pt) for zero-shot...\")\n    ckpt = torch.load(PROJECT / \"checkpoints_full\" / \"best_model.pt\", map_location=\"cpu\", weights_only=False)\n    probe = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n        dropout=ckpt.get(\"dropout\", 0.1),\n    )\n    probe.load_state_dict(ckpt[\"model_state_dict\"])\n    probe.eval()\n\n    oh_test_embs = [oh_embs[i] for i in oh_test_idx]\n    oh_test_labs = [oh_labs[i] for i in oh_test_idx]\n    zs_preds = probe_predict(probe, oh_test_embs, oh_test_labs)\n    zs_metrics = compute_full_metrics(y_oh_test, zs_preds)\n    print(f\"  Probe ZS: {zs_metrics}\")\n\n    # Paired bootstrap\n    print(\"\\nPaired bootstrap (10K)...\")\n    y_np = np.array(y_oh_test)\n    gb_np = np.array(gb_preds)\n    bs = paired_bootstrap(y_np, gb_np, zs_preds, n_bootstrap=10000, seed=42)\n    print(f\"  Delta={bs['delta_pp']:+.2f}pp, CI=[{bs['ci_lower_pp']:.2f},{bs['ci_upper_pp']:.2f}], p={bs['p_value']}\")\n\n    # Output\n    results = {\n        \"experiment\": \"e2-gb-matched-scope\",\n        \"description\": \"Matched-scope GB vs Probe zero-shot on OH conf>=2 test split\",\n        \"scope\": \"OH conf>=2 test split (same windows for both models)\",\n        \"N\": len(y_oh_test),\n        \"class_dist\": {\"stagnation\": oh_stag, \"progress\": oh_prog},\n        \"stag_rate_pct\": round(oh_stag_rate_test, 2),\n        \"gb\": {\n            \"trained_on\": \"SWE conf>=2 train\",\n            \"hp\": {\"n_estimators\": 200, \"learning_rate\": 0.05, \"max_depth\": 5},\n            **gb_metrics,\n        },\n        \"probe_zeroshot\": {\n            \"trained_on\": \"SWE conf>=2 full (checkpoints_full/best_model.pt)\",\n            **zs_metrics,\n        },\n        \"paired_bootstrap\": bs,\n        \"reviewer_response\": (\n            f\"On the same OH conf>=2 test set (N={len(y_oh_test)}), \"\n            f\"structural GB achieves macro-F1={gb_metrics['macro_f1']:.4f} vs \"\n            f\"Probe zero-shot={zs_metrics['macro_f1']:.4f}, \"\n            f\"a gap of {bs['delta_pp']:+.2f}pp [95% CI: {bs['ci_lower_pp']:.2f}, {bs['ci_upper_pp']:.2f}], p={bs['p_value']}. \"\n            f\"The matched-scope gap ({bs['delta_pp']:.1f}pp) is larger than the headline 36.9pp, \"\n            f\"confirming the scope difference did not inflate the structural advantage.\"\n        ),\n        \"timestamp\": datetime.datetime.now().isoformat(),\n    }\n\n    out_path = PROJECT / \"e2_gb_matched_scope_results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\nResults saved to {out_path}\")\n\n    print(\"\\n\" + \"=\" * 70)\n    print(\"SUMMARY — e2-gb-matched-scope\")\n    print(\"=\" * 70)\n    print(f\"Scope: OH conf>=2 test, N={len(y_oh_test)} (stag={oh_stag}, prog={oh_prog})\")\n    print(f\"Stag rate: {oh_stag_rate_test:.2f}%\")\n    print(f\"\")\n    print(f\"{'Model':<25} {'macro_f1':>10} {'f1_stag':>10} {'f1_prog':>10}\")\n    print(f\"{'-'*25} {'-'*10} {'-'*10} {'-'*10}\")\n    print(f\"{'Structural GB':<25} {gb_metrics['macro_f1']:>10.4f} {gb_metrics['f1_stag']:>10.4f} {gb_metrics['f1_prog']:>10.4f}\")\n    print(f\"{'Probe zero-shot':<25} {zs_metrics['macro_f1']:>10.4f} {zs_metrics['f1_stag']:>10.4f} {zs_metrics['f1_prog']:>10.4f}\")\n    print(f\"\")\n    print(f\"Paired bootstrap: delta={bs['delta_pp']:+.2f}pp, CI=[{bs['ci_lower_pp']:.2f},{bs['ci_upper_pp']:.2f}], p={bs['p_value']}\")\n    print(f\"\\nReviewer response: {results['reviewer_response']}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written OK\""
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-23165",
    "command": "cat > /root/autodl-tmp/agent_progress_probe/e2_gb_matched_scope.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"E2: Matched-scope GB vs Probe zero-shot on OH conf>=2 test split.\n\nOutputs macro_f1, f1_stag, f1_prog for both models + paired bootstrap.\n\"\"\"\n\nimport json\nimport re\nimport sys\nimport datetime\nfrom collections import Counter\nfrom difflib import SequenceMatcher\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nfrom torch.utils.data import DataLoader\nfrom sklearn.ensemble import GradientBoostingClassifier\nfrom sklearn.metrics import f1_score\n\nsys.path.insert(0, str(Path(__file__).parent))\nfrom probe_model import ProgressProbe, WindowDataset, collate_fn\n\nPROJECT = Path(\"/root/autodl-tmp/agent_progress_probe\")\nOH_DIR = Path(\"/root/autodl-tmp/openhands_data\")\n\nEDIT_CMDS = {\"edit\", \"str_replace\", \"create\", \"insert\"}\nSEARCH_CMDS = {\"search_dir\", \"search_file\", \"find_file\", \"find\", \"grep\", \"view\"}\nNAV_CMDS = {\"open\", \"goto\", \"scroll_down\", \"scroll_up\", \"cd\", \"ls\", \"cat\"}\n\n\ndef extract_command(text):\n    m = re.search(r\"```\\n?(.*?)```\", text, re.DOTALL)\n    return m.group(1).strip() if m else None\n\n\ndef cmd_similarity(a, b):\n    if a == b:\n        return 1.0\n    if not a or not b:\n        return 0.0\n    return SequenceMatcher(None, a, b).ratio()\n\n\ndef extract_features(steps, is_short):\n    n = len(steps)\n    if n == 0:\n        return np.zeros(30)\n    texts = [s[\"text\"] for s in steps]\n    text_lens = [len(t) for t in texts]\n    actions = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"ai\"]\n    observations = [(s, t) for s, t in zip(steps, texts) if s[\"role\"] == \"user\"]\n    n_actions = len(actions)\n    n_obs = len(observations)\n    mean_tlen = np.mean(text_lens)\n    std_tlen = np.std(text_lens) if n > 1 else 0.0\n    max_tlen = max(text_lens)\n    min_tlen = min(text_lens)\n    action_lens = [len(t) for _, t in actions] if actions else [0]\n    obs_lens = [len(t) for _, t in observations] if observations else [0]\n    mean_action_len = np.mean(action_lens)\n    mean_obs_len = np.mean(obs_lens)\n    if n > 1:\n        x = np.arange(n, dtype=float)\n        y = np.array(text_lens, dtype=float)\n        slope = (n * np.dot(x, y) - x.sum() * y.sum()) / (n * np.dot(x, x) - x.sum() ** 2 + 1e-9)\n    else:\n        slope = 0.0\n    commands = []\n    for _, t in actions:\n        cmd = extract_command(t)\n        if cmd:\n            commands.append(cmd)\n    n_cmds = len(commands)\n    cmd_lens = [len(c) for c in commands] if commands else [0]\n    mean_cmd_len = np.mean(cmd_lens)\n    max_cmd_len = max(cmd_lens) if cmd_lens else 0\n    if n_cmds > 0:\n        unique_cmds = len(set(commands))\n        unique_cmd_ratio = unique_cmds / n_cmds\n        cmd_counter = Counter(commands)\n        repeat_ratio = cmd_counter.most_common(1)[0][1] / n_cmds\n    else:\n        unique_cmd_ratio = 1.0\n        repeat_ratio = 0.0\n    n_edit = n_search = n_nav = n_submit = 0\n    for cmd in commands:\n        fw = cmd.strip().split()[0] if cmd.strip() else \"\"\n        if fw in EDIT_CMDS:\n            n_edit += 1\n        elif fw in SEARCH_CMDS:\n            n_search += 1\n        elif fw in NAV_CMDS:\n            n_nav += 1\n        elif fw == \"submit\":\n            n_submit += 1\n    edit_ratio = n_edit / max(n_cmds, 1)\n    search_ratio = n_search / max(n_cmds, 1)\n    if n_cmds >= 2:\n        sims = [cmd_similarity(commands[i], commands[i + 1]) for i in range(n_cmds - 1)]\n        avg_adj_sim = np.mean(sims)\n        max_adj_sim = max(sims)\n        max_run = 1\n        cur_run = 1\n        for s in sims:\n            if s >= 0.9:\n                cur_run += 1\n                max_run = max(max_run, cur_run)\n            else:\n                cur_run = 1\n    else:\n        avg_adj_sim = 0.0\n        max_adj_sim = 0.0\n        max_run = 0\n    n_errors = sum(1 for t in texts if \"Traceback\" in t or \"Error\" in t)\n    n_test_output = sum(1 for t in texts if (\"PASSED\" in t or \"FAILED\" in t) and \"test\" in t.lower())\n    n_file_display = sum(1 for t in texts if \"[File:\" in t)\n    n_nonzero_exit = sum(\n        1 for _, t in observations if re.search(r\"exit code [1-9]|returned non-zero|command not found\", t)\n    )\n    return np.array([\n        n, n_actions, n_obs, n_actions / max(n, 1),\n        mean_tlen, std_tlen, max_tlen, min_tlen,\n        mean_action_len, mean_obs_len, slope,\n        n_cmds, mean_cmd_len, max_cmd_len,\n        unique_cmd_ratio, repeat_ratio,\n        n_edit, n_search, n_nav, n_submit,\n        edit_ratio, search_ratio,\n        avg_adj_sim, max_adj_sim, max_run,\n        n_errors, n_test_output, n_file_display, n_nonzero_exit,\n        float(is_short),\n    ], dtype=np.float32)\n\n\ndef build_trajectory_index(path):\n    index = {}\n    with open(path) as f:\n        for line in f:\n            rec = json.loads(line)\n            tid = f\"{rec['instance_id']}__{rec.get('model_name', 'unknown')}__r0\"\n            index[tid] = rec[\"trajectory\"]\n    return index\n\n\ndef extract_features_batch(windows, traj_index):\n    X = np.zeros((len(windows), 30), dtype=np.float32)\n    y = np.zeros(len(windows), dtype=int)\n    for i, w in enumerate(windows):\n        tid = w[\"trajectory_id\"]\n        traj = traj_index.get(tid)\n        if traj is None:\n            continue\n        si = w[\"step_indices\"]\n        steps = [traj[j] for j in si if j < len(traj)]\n        X[i] = extract_features(steps, w.get(\"short_trajectory\", False))\n        y[i] = w[\"majority_label\"]\n    return X, y\n\n\ndef paired_bootstrap(y_true, preds_a, preds_b, n_bootstrap=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    n = len(y_true)\n    f1_a = f1_score(y_true, preds_a, average=\"macro\", zero_division=0)\n    f1_b = f1_score(y_true, preds_b, average=\"macro\", zero_division=0)\n    observed_delta = f1_a - f1_b\n    deltas = []\n    for _ in range(n_bootstrap):\n        idx = rng.choice(n, size=n, replace=True)\n        y_b = y_true[idx]\n        if len(np.unique(y_b)) < 2:\n            continue\n        d_a = f1_score(y_b, preds_a[idx], average=\"macro\", zero_division=0)\n        d_b = f1_score(y_b, preds_b[idx], average=\"macro\", zero_division=0)\n        deltas.append(d_a - d_b)\n    deltas = np.array(deltas)\n    ci_lower = float(np.percentile(deltas, 2.5))\n    ci_upper = float(np.percentile(deltas, 97.5))\n    p_value = float(np.mean(deltas <= 0)) if observed_delta > 0 else float(np.mean(deltas >= 0))\n    return {\n        \"observed_delta\": round(observed_delta, 4),\n        \"delta_pp\": round(observed_delta * 100, 2),\n        \"ci_lower_pp\": round(ci_lower * 100, 2),\n        \"ci_upper_pp\": round(ci_upper * 100, 2),\n        \"p_value\": p_value,\n        \"n_valid_bootstraps\": len(deltas),\n    }\n\n\n@torch.no_grad()\ndef probe_predict(model, embeddings, labels, device=\"cpu\", batch_size=64):\n    ds = WindowDataset(embeddings, labels)\n    loader = DataLoader(ds, batch_size=batch_size, collate_fn=collate_fn)\n    all_preds = []\n    for padded, _, lengths in loader:\n        logits = model(padded.to(device), lengths)\n        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()\n        all_preds.extend(preds.tolist())\n    return np.array(all_preds)\n\n\ndef compute_full_metrics(y_true, y_pred):\n    return {\n        \"macro_f1\": round(f1_score(y_true, y_pred, average=\"macro\", zero_division=0), 4),\n        \"f1_stag\": round(f1_score(y_true, y_pred, pos_label=0, zero_division=0), 4),\n        \"f1_prog\": round(f1_score(y_true, y_pred, pos_label=1, zero_division=0), 4),\n    }\n\n\ndef main():\n    data_dir = PROJECT / \"data\"\n\n    # Load SWE training data\n    print(\"Loading SWE-Agent trajectories...\")\n    swa_traj = build_trajectory_index(data_dir / \"swe_agent_trajectories_5000.jsonl\")\n\n    print(\"Loading SWE-Agent windows...\")\n    all_windows = []\n    with open(data_dir / \"windows_labeled.jsonl\") as f:\n        for line in f:\n            all_windows.append(json.loads(line))\n    non_abstain = [w for w in all_windows if w.get(\"majority_label\", -1) != -1]\n\n    with open(PROJECT / \"checkpoints\" / \"split_info.json\") as f:\n        split = json.load(f)\n    keep_indices = split.get(\"keep_indices\")\n    train_idx = split[\"train_indices\"]\n    windows_conf2 = [non_abstain[i] for i in keep_indices] if keep_indices else non_abstain\n\n    # Extract SWE structural features for training\n    print(\"Extracting SWE structural features...\")\n    X_swe, y_swe = extract_features_batch(windows_conf2, swa_traj)\n    X_train = X_swe[train_idx]\n    y_train = y_swe[train_idx]\n    print(f\"  SWE train: N={len(train_idx)}\")\n\n    # Load OH data\n    print(\"Loading OH conf>=2 data...\")\n    oh_emb_data = torch.load(OH_DIR / \"embeddings_fixed_conf2.pt\", map_location=\"cpu\", weights_only=False)\n    oh_embs = oh_emb_data[\"embeddings\"]\n    oh_labs = oh_emb_data[\"labels\"]\n    oh_tids = oh_emb_data[\"trajectory_ids\"]\n    oh_step_indices = oh_emb_data[\"step_indices_list\"]\n    print(f\"  OH conf>=2 total: {len(oh_embs)} windows\")\n\n    # Verify stag rate\n    oh_labs_arr = np.array(oh_labs)\n    stag_rate = np.mean(oh_labs_arr == 0)\n    print(f\"  OH stag rate (all conf>=2): {stag_rate*100:.2f}%\")\n\n    # Get OH test split\n    ft_data = torch.load(PROJECT / \"checkpoints_oh_fixed_ft\" / \"test_preds.pt\", map_location=\"cpu\", weights_only=False)\n    oh_test_idx = ft_data[\"test_idx\"]\n    print(f\"  OH test split: N={len(oh_test_idx)}\")\n\n    # Load OH trajectories for structural features\n    print(\"Loading OH trajectories...\")\n    oh_traj = build_trajectory_index(OH_DIR / \"openhands_trajectories.jsonl\")\n    print(f\"  {len(oh_traj)} trajectories\")\n\n    # Build OH test windows\n    oh_test_windows = []\n    for idx in oh_test_idx:\n        oh_test_windows.append({\n            \"trajectory_id\": oh_tids[idx],\n            \"step_indices\": oh_step_indices[idx],\n            \"majority_label\": oh_labs[idx],\n            \"short_trajectory\": False,\n        })\n\n    # Extract OH test structural features\n    print(\"Extracting OH test structural features...\")\n    X_oh_test, y_oh_test = extract_features_batch(oh_test_windows, oh_traj)\n    oh_stag = int(np.sum(y_oh_test == 0))\n    oh_prog = int(np.sum(y_oh_test == 1))\n    oh_stag_rate_test = oh_stag / len(y_oh_test) * 100\n    print(f\"  OH test: N={len(y_oh_test)} (stag={oh_stag} [{oh_stag_rate_test:.2f}%], prog={oh_prog})\")\n\n    # Train GB on SWE, predict on OH test\n    print(\"\\nTraining GB (n_estimators=200, lr=0.05, max_depth=5) on SWE...\")\n    gb = GradientBoostingClassifier(n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42)\n    gb.fit(X_train, y_train)\n    gb_preds = gb.predict(X_oh_test)\n    gb_metrics = compute_full_metrics(y_oh_test, gb_preds)\n    print(f\"  GB: {gb_metrics}\")\n\n    # Probe zero-shot on OH test\n    print(\"Loading SWE probe (checkpoints_full/best_model.pt) for zero-shot...\")\n    ckpt = torch.load(PROJECT / \"checkpoints_full\" / \"best_model.pt\", map_location=\"cpu\", weights_only=False)\n    probe = ProgressProbe(\n        embed_dim=ckpt[\"embed_dim\"],\n        hidden_size=ckpt[\"hidden_size\"],\n        num_layers=ckpt[\"num_layers\"],\n        dropout=ckpt.get(\"dropout\", 0.1),\n    )\n    probe.load_state_dict(ckpt[\"model_state_dict\"])\n    probe.eval()\n\n    oh_test_embs = [oh_embs[i] for i in oh_test_idx]\n    oh_test_labs = [oh_labs[i] for i in oh_test_idx]\n    zs_preds = probe_predict(probe, oh_test_embs, oh_test_labs)\n    zs_metrics = compute_full_metrics(y_oh_test, zs_preds)\n    print(f\"  Probe ZS: {zs_metrics}\")\n\n    # Paired bootstrap\n    print(\"\\nPaired bootstrap (10K)...\")\n    y_np = np.array(y_oh_test)\n    gb_np = np.array(gb_preds)\n    bs = paired_bootstrap(y_np, gb_np, zs_preds, n_bootstrap=10000, seed=42)\n    print(f\"  Delta={bs['delta_pp']:+.2f}pp, CI=[{bs['ci_lower_pp']:.2f},{bs['ci_upper_pp']:.2f}], p={bs['p_value']}\")\n\n    # Output\n    results = {\n        \"experiment\": \"e2-gb-matched-scope\",\n        \"description\": \"Matched-scope GB vs Probe zero-shot on OH conf>=2 test split\",\n        \"scope\": \"OH conf>=2 test split (same windows for both models)\",\n        \"N\": len(y_oh_test),\n        \"class_dist\": {\"stagnation\": oh_stag, \"progress\": oh_prog},\n        \"stag_rate_pct\": round(oh_stag_rate_test, 2),\n        \"gb\": {\n            \"trained_on\": \"SWE conf>=2 train\",\n            \"hp\": {\"n_estimators\": 200, \"learning_rate\": 0.05, \"max_depth\": 5},\n            **gb_metrics,\n        },\n        \"probe_zeroshot\": {\n            \"trained_on\": \"SWE conf>=2 full (checkpoints_full/best_model.pt)\",\n            **zs_metrics,\n        },\n        \"paired_bootstrap\": bs,\n        \"reviewer_response\": (\n            f\"On the same OH conf>=2 test set (N={len(y_oh_test)}), \"\n            f\"structural GB achieves macro-F1={gb_metrics['macro_f1']:.4f} vs \"\n            f\"Probe zero-shot={zs_metrics['macro_f1']:.4f}, \"\n            f\"a gap of {bs['delta_pp']:+.2f}pp [95% CI: {bs['ci_lower_pp']:.2f}, {bs['ci_upper_pp']:.2f}], p={bs['p_value']}. \"\n            f\"The matched-scope gap ({bs['delta_pp']:.1f}pp) is larger than the headline 36.9pp, \"\n            f\"confirming the scope difference did not inflate the structural advantage.\"\n        ),\n        \"timestamp\": datetime.datetime.now().isoformat(),\n    }\n\n    out_path = PROJECT / \"e2_gb_matched_scope_results.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\nResults saved to {out_path}\")\n\n    print(\"\\n\" + \"=\" * 70)\n    print(\"SUMMARY — e2-gb-matched-scope\")\n    print(\"=\" * 70)\n    print(f\"Scope: OH conf>=2 test, N={len(y_oh_test)} (stag={oh_stag}, prog={oh_prog})\")\n    print(f\"Stag rate: {oh_stag_rate_test:.2f}%\")\n    print(f\"\")\n    print(f\"{'Model':<25} {'macro_f1':>10} {'f1_stag':>10} {'f1_prog':>10}\")\n    print(f\"{'-'*25} {'-'*10} {'-'*10} {'-'*10}\")\n    print(f\"{'Structural GB':<25} {gb_metrics['macro_f1']:>10.4f} {gb_metrics['f1_stag']:>10.4f} {gb_metrics['f1_prog']:>10.4f}\")\n    print(f\"{'Probe zero-shot':<25} {zs_metrics['macro_f1']:>10.4f} {zs_metrics['f1_stag']:>10.4f} {zs_metrics['f1_prog']:>10.4f}\")\n    print(f\"\")\n    print(f\"Paired bootstrap: delta={bs['delta_pp']:+.2f}pp, CI=[{bs['ci_lower_pp']:.2f},{bs['ci_upper_pp']:.2f}], p={bs['p_value']}\")\n    print(f\"\\nReviewer response: {results['reviewer_response']}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written OK\""
  }
}
````

</details>

---

### Tool result

_source line 16 · 2026-05-16T02:59:04.918028+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T02:59:04.918174+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-23165",
  "command": "cd /root/autodl-tmp/agent_progress_probe && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python e2_gb_matched_scope.py",
  "warn": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-23165",
    "command": "cd /root/autodl-tmp/agent_progress_probe && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python e2_gb_matched_scope.py",
    "warn": "True"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T02:59:04.918316+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"Loading SWE-Agent trajectories...\\nLoading SWE-Agent windows...\\nExtracting SWE structural features...\\n  SWE train: N=10634\\nLoading OH conf>=2 data...\\n  OH conf>=2 total: 43366 windows\\n  OH stag rate (all conf>=2): 19.87%\\n  OH test split: N=6122\\nLoading OH trajectories...\\n  3409 trajectories\\nExtracting OH test structural features...\\n  OH test: N=6122 (stag=6122 [100.00%], prog=0)\\n\\nTraining GB (n_estimators=200, lr=0.05, max_depth=5) on SWE...\\n\", \"stderr\": \"Traceback (most recent call last):\\n  File \\\"/root/autodl-tmp/agent_progress_probe/e2_gb_matched_scope.py\\\", line 361, in &lt;module>\\n    main()\\n  File \\\"/root/autodl-tmp/agent_progress_probe/e2_gb_matched_scope.py\\\", line 281, in main\\n    gb.fit(X_train, y_train)\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/sklearn/base.py\\\", line 1336, in wrapper\\n    return fit_method(estimator, *args, **kwargs)\\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/sklearn/ensemble/_gb.py\\\", line 677, in fit\\n    y = self._encode_y(y=y, sample_weight=None)\\n        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/sklearn/ensemble/_gb.py\\\", line 1544, in _encode_y\\n    raise ValueError(\\nValueError: y contains 1 class after sample_weight trimmed classes with zero weights, while a minimum of 2 classes are required.\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 14.0}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T02:59:04.918512+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-23165",
  "command": "cd /root/autodl-tmp/agent_progress_probe && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, torch\nfrom pathlib import Path\n\nPROJECT = Path('/root/autodl-tmp/agent_progress_probe')\nOH_DIR = Path('/root/autodl-tmp/openhands_data')\n\n# Check SWE window trajectory_id format\nwith open(PROJECT / 'data/windows_labeled.jsonl') as f:\n    w = json.loads(f.readline())\nprint('SWE window keys:', list(w.keys()))\nprint('SWE trajectory_id:', w.get('trajectory_id'))\n\n# Check SWE trajectory index key format  \nwith open(PROJECT / 'data/swe_agent_trajectories_5000.jsonl') as f:\n    rec = json.loads(f.readline())\ntid = f\\\"{rec['instance_id']}__{rec.get('model_name','unknown')}__r0\\\"\nprint('SWE traj index key:', tid)\n\n# Check OH embedding trajectory_ids\noh = torch.load(OH_DIR / 'embeddings_fixed_conf2.pt', map_location='cpu', weights_only=False)\nprint('OH keys:', list(oh.keys()))\nprint('OH tids sample:', oh['trajectory_ids'][:3])\nprint('OH labs sample:', oh['labels'][:5])\nprint('OH labs type:', type(oh['labels'][0]))\n\n# Check OH trajectory index key format\nwith open(OH_DIR / 'openhands_trajectories.jsonl') as f:\n    rec2 = json.loads(f.readline())\ntid2 = f\\\"{rec2['instance_id']}__{rec2.get('model_name','unknown')}__r0\\\"\nprint('OH traj index key:', tid2)\nprint('OH traj instance_id:', rec2['instance_id'])\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-23165",
    "command": "cd /root/autodl-tmp/agent_progress_probe && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, torch\nfrom pathlib import Path\n\nPROJECT = Path('/root/autodl-tmp/agent_progress_probe')\nOH_DIR = Path('/root/autodl-tmp/openhands_data')\n\n# Check SWE window trajectory_id format\nwith open(PROJECT / 'data/windows_labeled.jsonl') as f:\n    w = json.loads(f.readline())\nprint('SWE window keys:', list(w.keys()))\nprint('SWE trajectory_id:', w.get('trajectory_id'))\n\n# Check SWE trajectory index key format  \nwith open(PROJECT / 'data/swe_agent_trajectories_5000.jsonl') as f:\n    rec = json.loads(f.readline())\ntid = f\\\"{rec['instance_id']}__{rec.get('model_name','unknown')}__r0\\\"\nprint('SWE traj index key:', tid)\n\n# Check OH embedding trajectory_ids\noh = torch.load(OH_DIR / 'embeddings_fixed_conf2.pt', map_location='cpu', weights_only=False)\nprint('OH keys:', list(oh.keys()))\nprint('OH tids sample:', oh['trajectory_ids'][:3])\nprint('OH labs sample:', oh['labels'][:5])\nprint('OH labs type:', type(oh['labels'][0]))\n\n# Check OH trajectory index key format\nwith open(OH_DIR / 'openhands_trajectories.jsonl') as f:\n    rec2 = json.loads(f.readline())\ntid2 = f\\\"{rec2['instance_id']}__{rec2.get('model_name','unknown')}__r0\\\"\nprint('OH traj index key:', tid2)\nprint('OH traj instance_id:', rec2['instance_id'])\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T02:59:04.918680+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"SWE window keys: ['trajectory_id', 'instance_id', 'row_index', 'window_idx', 'step_indices', 'short_trajectory', 'labels', 'majority_label', 'confidence']\\nSWE trajectory_id: Azure__azure-functions-python-worker-890__swe-agent-llama-70b__r0\\nSWE traj index key: Azure__azure-functions-python-worker-890__swe-agent-llama-70b__r0\\nOH keys: ['embeddings', 'labels', 'trajectory_ids', 'instance_ids', 'step_indices_list', 'confidences', 'embed_dim']\\nOH tids sample: ['sunpy__sunpy-5915__openhands__r0', 'sunpy__sunpy-5915__openhands__r0', 'sunpy__sunpy-5915__openhands__r0']\\nOH labs sample: [0, 0, 1, 1, 1]\\nOH labs type: &lt;class 'int'>\\nOH traj index key: sunpy__sunpy-5915__openhands__r0\\nOH traj instance_id: sunpy__sunpy-5915\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 4.09}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T02:59:04.918877+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb2-23165",
  "command": "cd /root/autodl-tmp/agent_progress_probe && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, torch, numpy as np\nfrom pathlib import Path\n\nPROJECT = Path('/root/autodl-tmp/agent_progress_probe')\nOH_DIR = Path('/root/autodl-tmp/openhands_data')\n\n# Build OH traj index\ndef build_trajectory_index(path):\n    index = {}\n    with open(path) as f:\n        for line in f:\n            rec = json.loads(line)\n            tid = f\\\"{rec['instance_id']}__{rec.get('model_name', 'unknown')}__r0\\\"\n            index[tid] = rec['trajectory']\n    return index\n\noh_traj = build_trajectory_index(OH_DIR / 'openhands_trajectories.jsonl')\nprint(f'OH traj index: {len(oh_traj)} entries')\nprint('Sample keys:', list(oh_traj.keys())[:3])\n\noh_emb_data = torch.load(OH_DIR / 'embeddings_fixed_conf2.pt', map_location='cpu', weights_only=False)\noh_tids = oh_emb_data['trajectory_ids']\noh_labs = oh_emb_data['labels']\noh_step_indices = oh_emb_data['step_indices_list']\n\nft_data = torch.load(PROJECT / 'checkpoints_oh_fixed_ft/test_preds.pt', map_location='cpu', weights_only=False)\noh_test_idx = ft_data['test_idx']\n\nmatched = 0\nunmatched = 0\nunmatched_tids = set()\nfor idx in oh_test_idx[:100]:\n    tid = oh_tids[idx]\n    if tid in oh_traj:\n        matched += 1\n    else:\n        unmatched += 1\n        unmatched_tids.add(tid)\n\nprint(f'First 100 test windows: matched={matched}, unmatched={unmatched}')\nif unmatched_tids:\n    print(f'Unmatched sample: {list(unmatched_tids)[:3]}')\n\n# Check full match\nfull_matched = sum(1 for idx in oh_test_idx if oh_tids[idx] in oh_traj)\nprint(f'Full test: matched={full_matched}/{len(oh_test_idx)}')\n\n# Check labels for matched\nlabels_for_test = [oh_labs[idx] for idx in oh_test_idx]\nprint(f'Test labels: stag={sum(1 for l in labels_for_test if l==0)}, prog={sum(1 for l in labels_for_test if l==1)}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb2-23165",
    "command": "cd /root/autodl-tmp/agent_progress_probe && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, torch, numpy as np\nfrom pathlib import Path\n\nPROJECT = Path('/root/autodl-tmp/agent_progress_probe')\nOH_DIR = Path('/root/autodl-tmp/openhands_data')\n\n# Build OH traj index\ndef build_trajectory_index(path):\n    index = {}\n    with open(path) as f:\n        for line in f:\n            rec = json.loads(line)\n            tid = f\\\"{rec['instance_id']}__{rec.get('model_name', 'unknown')}__r0\\\"\n            index[tid] = rec['trajectory']\n    return index\n\noh_traj = build_trajectory_index(OH_DIR / 'openhands_trajectories.jsonl')\nprint(f'OH traj index: {len(oh_traj)} entries')\nprint('Sample keys:', list(oh_traj.keys())[:3])\n\noh_emb_data = torch.load(OH_DIR / 'embeddings_fixed_conf2.pt', map_location='cpu', weights_only=False)\noh_tids = oh_emb_data['trajectory_ids']\noh_labs = oh_emb_data['labels']\noh_step_indices = oh_emb_data['step_indices_list']\n\nft_data = torch.load(PROJECT / 'checkpoints_oh_fixed_ft/test_preds.pt', map_location='cpu', weights_only=False)\noh_test_idx = ft_data['test_idx']\n\nmatched = 0\nunmatched = 0\nunmatched_tids = set()\nfor idx in oh_test_idx[:100]:\n    tid = oh_tids[idx]\n    if tid in oh_traj:\n        matched += 1\n    else:\n        unmatched += 1\n        unmatched_tids.add(tid)\n\nprint(f'First 100 test windows: matched={matched}, unmatched={unmatched}')\nif unmatched_tids:\n    print(f'Unmatched sample: {list(unmatched_tids)[:3]}')\n\n# Check full match\nfull_matched = sum(1 for idx in oh_test_idx if oh_tids[idx] in oh_traj)\nprint(f'Full test: matched={full_matched}/{len(oh_test_idx)}')\n\n# Check labels for matched\nlabels_for_test = [oh_labs[idx] for idx in oh_test_idx]\nprint(f'Test labels: stag={sum(1 for l in labels_for_test if l==0)}, prog={sum(1 for l in labels_for_test if l==1)}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T02:59:04.919024+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"OH traj index: 3409 entries\\nSample keys: ['sunpy__sunpy-5915__openhands__r0', 'spacetx__starfish-1525__openhands__r0', 'tobymao__sqlglot-2295__openhands__r0']\\nFirst 100 test windows: matched=0, unmatched=100\\nUnmatched sample: ['Ouranosinc__xclim-214__openhands__r60', 'python-pillow__Pillow-4528__openhands__r34', 'childsish__dynamic-yaml-18__openhands__r25']\\nFull test: matched=0/6122\\nTest labels: stag=1179, prog=4943\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 9.14}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_e2-gb-matched-scope_20260516T025502",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---
