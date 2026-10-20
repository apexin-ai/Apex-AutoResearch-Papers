# Research conversation: Find bootstrap CI scripts in /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ — specifi

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a6f8fbc29078dceb8.jsonl`
- **Structured JSON:** [`7b6a121e7a4e0fe13acc.json`](../../sessions/7b/7b6a121e7a4e0fe13acc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

35 recorded events

### User

_source line 1 · 2026-05-18T11:22:05.864Z_

Find bootstrap CI scripts in /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/ — specifically look for `crossscorer_bootstrap_ci.py`, `c4_power_curve.py`, or any script with "bootstrap" in the name under the `scripts/` directory. Also check for any Python files that contain "bootstrap" as a keyword. I need to understand the bootstrap resampling logic used in this project. Search breadth: medium.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8ab46256-1dcf-4174-9343-f64005e6f2a2",
  "agentId": "a6f8fbc29078dceb8",
  "type": "user",
  "uuid": "85e50faa-2311-4015-81ef-70698a6761de",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-18T11:22:07.341Z_

I'll help you find and analyze the bootstrap CI scripts in this project. Let me start with a systematic search.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "85e50faa-2311-4015-81ef-70698a6761de",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wtRb61MBG3ZJ6cVtaU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "58ce0338-c2fe-491e-8052-543782a9ede6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019ys2p7BDtkHcRmgo6eahzG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18821,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18821,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T11:22:07.936Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01AyUbMaUHAte2BGRarajLsE`</summary>

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
  "recorded_role": "assistant",
  "parentUuid": "58ce0338-c2fe-491e-8052-543782a9ede6",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wtRb61MBG3ZJ6cVtaU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d017d6fe-21e9-446d-8ba1-c0d1848b45e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019ys2p7BDtkHcRmgo6eahzG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18821,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18821,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T11:22:07.970Z_

<details><summary>↩ Tool result · `toolu_01AyUbMaUHAte2BGRarajLsE`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d017d6fe-21e9-446d-8ba1-c0d1848b45e8",
  "isSidechain": true,
  "promptId": "8ab46256-1dcf-4174-9343-f64005e6f2a2",
  "agentId": "a6f8fbc29078dceb8",
  "type": "user",
  "uuid": "5145174b-860a-4b9e-8875-97a54531ce5b",
  "sourceToolAssistantUUID": "d017d6fe-21e9-446d-8ba1-c0d1848b45e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T11:22:08.036Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01QS8fwWTsk7PjFcErs44F82`</summary>

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
  "recorded_role": "assistant",
  "parentUuid": "5145174b-860a-4b9e-8875-97a54531ce5b",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wtRb61MBG3ZJ6cVtaU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cddc0795-56dd-4e71-9c2d-bac0f6289ea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019ys2p7BDtkHcRmgo6eahzG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18821,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18821,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T11:22:08.066Z_

<details><summary>↩ Tool result · `toolu_01QS8fwWTsk7PjFcErs44F82`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cddc0795-56dd-4e71-9c2d-bac0f6289ea2",
  "isSidechain": true,
  "promptId": "8ab46256-1dcf-4174-9343-f64005e6f2a2",
  "agentId": "a6f8fbc29078dceb8",
  "type": "user",
  "uuid": "08cfff4e-9dfd-4ee7-af76-bcd246941916",
  "sourceToolAssistantUUID": "cddc0795-56dd-4e71-9c2d-bac0f6289ea2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T11:22:08.482Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01TbLzvU4ZHtAmMJaU5d4ZyM`</summary>

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
  "recorded_role": "assistant",
  "parentUuid": "08cfff4e-9dfd-4ee7-af76-bcd246941916",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wtRb61MBG3ZJ6cVtaU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "89f6acd7-314b-4d00-8462-5c6c16ed570d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019ys2p7BDtkHcRmgo6eahzG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18821,
      "cache_read_input_tokens": 0,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18821
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 326,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18821,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T11:22:08.551Z_

<details><summary>↩ Tool result · `toolu_01TbLzvU4ZHtAmMJaU5d4ZyM`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89f6acd7-314b-4d00-8462-5c6c16ed570d",
  "isSidechain": true,
  "promptId": "8ab46256-1dcf-4174-9343-f64005e6f2a2",
  "agentId": "a6f8fbc29078dceb8",
  "type": "user",
  "uuid": "b525c606-98b8-47a8-9493-c56ea6e07327",
  "sourceToolAssistantUUID": "89f6acd7-314b-4d00-8462-5c6c16ed570d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-18T11:22:09.978Z_

Good start. Let me search more specifically and read the relevant files that mention bootstrap:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b525c606-98b8-47a8-9493-c56ea6e07327",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wtczgfUM4QT9yVvXqV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9b524ee4-a791-462b-bf6c-5706e5233d6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KDDRCmbY4jbZApkUfRqJRU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1879,
      "cache_read_input_tokens": 18821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1879,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T11:22:10.855Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KZzAjCBZa9fz9iDi55ynnK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/scripts/plot_auc_decay_ci.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b524ee4-a791-462b-bf6c-5706e5233d6c",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wtczgfUM4QT9yVvXqV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "53f71e97-dbe3-40df-9dfc-7ed5244158ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KDDRCmbY4jbZApkUfRqJRU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1879,
      "cache_read_input_tokens": 18821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1879,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T11:22:10.872Z_

<details><summary>↩ Tool result · `toolu_01KZzAjCBZa9fz9iDi55ynnK`</summary>

```text
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
55	    name = source_path.stem if source_path.is_file() else source_path.name
56	    name = re.sub(r"^exp\d+_", "", name).replace("bootstrap_ci", "").replace("pairwise_auc", "").strip("_")
57	    return name or source_path.parent.name
58	
59	
60	def discover_ci_sources(root):
61	    """Find bootstrap CI JSONs and pairwise_auc.json with per_fold data."""
62	    ci_patterns = [
63	        "artifacts/*bootstrap*ci*.json",
64	        "artifacts/exp*_bootstrap_ci.json",
65	        "results_*/*bootstrap*ci*.json",
66	        "results/*/*bootstrap*ci*.json",
67	    ]
68	    auc_patterns = [
69	        "results_*/pairwise_auc.json",
70	        "results/*/pairwise_auc.json",
71	    ]
72	    files = set()
73	    for pat in ci_patterns:
74	        files.update(root.glob(pat))
75	    ci_files = sorted(files)
76	
77	    auc_files_set = set()
78	    for pat in auc_patterns:
79	        auc_files_set.update(root.glob(pat))
80	    auc_files = sorted(auc_files_set)
81	
82	    return ci_files, auc_files
83	
84	
85	def load_bootstrap_ci(json_path):
86	    """Load from bootstrap CI JSON. Returns {pair: {mean, ci_lower, ci_upper}}."""
87	    with open(json_path) as f:
88	        raw = json.load(f)
89	
90	    result = {}
91	    pairs_data = raw.get("pairs", raw)
92	    for k in PAIR_KEYS:
93	        if k in pairs_data:
94	            entry = pairs_data[k]
95	            if isinstance(entry, dict) and "ci_lower" in entry:
96	                result[k] = {
97	                    "mean": entry.get("boot_mean", entry.get("auc", entry.get("auc_mean_folds"))),
98	                    "ci_lower": entry["ci_lower"],
99	                    "ci_upper": entry["ci_upper"],
100	                }
101	    return result if result else None, raw
102	
103	
104	def load_pairwise_auc_ci(json_path):
105	    """Compute approximate CI from per-fold AUCs (mean ± 1.96*SE)."""
106	    with open(json_path) as f:
107	        raw = json.load(f)
108	
109	    per_fold = raw.get("per_fold")
110	    mean_data = raw.get("mean")
111	    if not per_fold or not mean_data:
112	        return None, raw
113	
114	    result = {}
115	    for k in PAIR_KEYS:
116	        if k in per_fold and k in mean_data:
117	            folds = np.array(per_fold[k])
118	            m = mean_data[k]
119	            se = np.std(folds, ddof=1) / np.sqrt(len(folds))
120	            result[k] = {
121	                "mean": m,
122	                "ci_lower": m - 1.96 * se,
123	                "ci_upper": m + 1.96 * se,
124	            }
125	    return result if result else None, raw
126	
127	
128	def parse_args():
129	    parser = argparse.ArgumentParser(description="Plot AUC decay with confidence bands")
130	    parser.add_argument("--results-dir", type=Path,
131	                        default=Path(__file__).resolve().parent.parent.parent,
132	                        help="Root directory to scan")
133	    parser.add_argument("--output", type=Path, default=None,
134	                        help="Output PDF path")
135	    parser.add_argument("--filter", type=str, default=None,
136	                        help="Filter models by substring")
137	    return parser.parse_args()
138	
139	
140	def main():
141	    args = parse_args()
142	    root = args.results_dir
143	
144	    ci_files, auc_files = discover_ci_sources(root)
145	    if not ci_files and not auc_files:
146	        print(f"No CI or pairwise_auc files found under {root}")
147	        return
148	
149	    models = {}
150	
151	    for fp in ci_files:
152	        data, metadata = load_bootstrap_ci(fp)
153	        if data is None:
154	            continue
155	        label = infer_label(fp, metadata)
156	        if args.filter and args.filter.lower() not in label.lower():
157	            continue
158	        label = label + " (bootstrap)"
159	        models[label] = data
160	
161	    for fp in auc_files:
162	        data, metadata = load_pairwise_auc_ci(fp)
163	        if data is None:
164	            continue
165	        label = infer_label(fp, metadata)
166	        if args.filter and args.filter.lower() not in label.lower():
167	            continue
168	        if any(label.split(" (")[0] in k for k in models):
169	            continue
170	        models[label] = data
171	
172	    if not models:
173	        print("No valid CI data found after filtering")
174	        return
175	
176	    x = np.arange(len(PAIR_KEYS))
177	
178	    plt.rcParams.update({
179	        "font.family": "serif",
180	        "font.size": 11,
181	        "axes.linewidth": 0.8,
182	        "xtick.major.width": 0.8,
183	        "ytick.major.width": 0.8,
184	    })
185	
186	    fig, ax = plt.subplots(figsize=(7, 4.5), constrained_layout=True)
187	
188	    ax.axhline(0.60, color="grey", ls="--", lw=0.8, zorder=1)
189	    ax.text(len(PAIR_KEYS) - 0.45, 0.608, r"$\theta = 0.60$",
190	            fontsize=8.5, color="grey", va="bottom", ha="right")
191	    ax.axhline(0.50, color="lightgrey", ls="--", lw=0.8, zorder=1)
192	    ax.text(len(PAIR_KEYS) - 0.45, 0.508, "chance",
193	            fontsize=8.5, color="silver", va="bottom", ha="right")
194	
195	    handles = []
196	    for i, (label, ci_data) in enumerate(models.items()):
197	        color = TABLEAU_COLORS[i % len(TABLEAU_COLORS)]
198	        marker = MARKERS[i % len(MARKERS)]
199	
200	        means = [ci_data.get(k, {}).get("mean", float("nan")) for k in PAIR_KEYS]
201	        lowers = [ci_data.get(k, {}).get("ci_lower", float("nan")) for k in PAIR_KEYS]
202	        uppers = [ci_data.get(k, {}).get("ci_upper", float("nan")) for k in PAIR_KEYS]
203	
204	        ax.fill_between(x, lowers, uppers, color=color, alpha=0.15, zorder=2)
205	        line, = ax.plot(x, means, "-", color=color, lw=1.8, marker=marker,
206	                        markersize=5, label=label, zorder=3)
207	        handles.append(line)
208	
209	    ax.set_xticks(x)
210	    ax.set_xticklabels(X_LABELS)
211	    ax.set_xlabel("Depth Pair")
212	    ax.set_ylabel("Pairwise AUC")
213	    ax.set_ylim(0.45, 1.05)
214	    ax.set_xlim(-0.25, len(PAIR_KEYS) - 0.75)
215	    ax.tick_params(direction="in")
216	
217	    ax.legend(handles=handles, fontsize=8.5, loc="upper right",
218	              bbox_to_anchor=(1.0, 0.98), framealpha=0.9, edgecolor="0.8")
219	
220	    if args.output:
221	        out_path = args.output
222	    else:
223	        out_dir = Path(__file__).resolve().parent.parent / "figures"
224	        out_dir.mkdir(parents=True, exist_ok=True)
225	        out_path = out_dir / "fig_s1_auc_decay_ci.pdf"
226	
227	    out_path.parent.mkdir(parents=True, exist_ok=True)
228	    fig.savefig(out_path, dpi=300, bbox_inches="tight")
229	    png_path = out_path.with_suffix(".png")
230	    fig.savefig(png_path, dpi=300, bbox_inches="tight")
231	    plt.close(fig)
232	
233	    pdf_size = out_path.stat().st_size
234	    png_size = png_path.stat().st_size
235	    print(f"Discovered {len(models)} configs: {list(models.keys())}")
236	    print(f"PDF: {pdf_size/1024:.1f} KB | PNG: {png_size/1024:.1f} KB")
237	    assert pdf_size > 3 * 1024, f"PDF too small: {pdf_size}"
238	    print("OK")
239	
240	
241	if __name__ == "__main__":
242	    main()
243	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53f71e97-dbe3-40df-9dfc-7ed5244158ca",
  "isSidechain": true,
  "promptId": "8ab46256-1dcf-4174-9343-f64005e6f2a2",
  "agentId": "a6f8fbc29078dceb8",
  "type": "user",
  "uuid": "8bb34ad7-09bd-43ec-aeff-883883381a43",
  "sourceToolAssistantUUID": "53f71e97-dbe3-40df-9dfc-7ed5244158ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T11:22:11.306Z_

<details open><summary>🔧 Tool call — Read · `toolu_018JcQYPhCQFfrFpbNBk4Sab`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/exp_D_mcnemar.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bb34ad7-09bd-43ec-aeff-883883381a43",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wtczgfUM4QT9yVvXqV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "740d7d10-51b2-4c84-b397-fe2b63f67200",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KDDRCmbY4jbZApkUfRqJRU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1879,
      "cache_read_input_tokens": 18821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1879,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T11:22:11.311Z_

<details><summary>↩ Tool result · `toolu_018JcQYPhCQFfrFpbNBk4Sab`</summary>

```text
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
61	    for k in range(max_depth):
62	        y_bin = (y > k).astype(int)
63	        for train_idx, test_idx in fold_indices:
64	            clf = lgb.LGBMClassifier(
65	                n_estimators=200, max_depth=6, learning_rate=0.05,
66	                num_leaves=31, verbose=-1, n_jobs=-1,
67	            )
68	            clf.fit(X[train_idx], y_bin[train_idx])
69	            cum_probs[test_idx, k] = clf.predict_proba(X[test_idx])[:, 1]
70	
71	    n_classes = max_depth + 1
72	    class_probs = np.zeros((n, n_classes))
73	    class_probs[:, 0] = 1.0 - cum_probs[:, 0]
74	    for k in range(1, max_depth):
75	        class_probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]
76	    class_probs[:, max_depth] = cum_probs[:, max_depth - 1]
77	    class_probs = np.clip(class_probs, 0, None)
78	    row_sums = class_probs.sum(axis=1, keepdims=True)
79	    row_sums[row_sums == 0] = 1.0
80	    class_probs /= row_sums
81	
82	    return class_probs.argmax(axis=1)
83	
84	
85	def parse_exp011_doc_id(doc_id_str):
86	    m = re.match(r"pythia_d(\d+)_(\d+)", doc_id_str)
87	    if not m:
88	        raise ValueError(f"Cannot parse doc_id: {doc_id_str}")
89	    return int(m.group(1)), int(m.group(2))
90	
91	
92	def load_llm_predictions(path):
93	    preds = {}
94	    with open(path) as f:
95	        for line in f:
96	            rec = json.loads(line)
97	            preds[rec["doc_id"]] = rec["predicted_depth"]
98	    return preds
99	
100	
101	def mcnemar_test(obd_correct, llm_correct):
102	    """McNemar exact test using binomial test on discordant pairs."""
103	    from scipy.stats import binomtest
104	
105	    b = int(np.sum(obd_correct & ~llm_correct))  # OBD right, LLM wrong
106	    c = int(np.sum(~obd_correct & llm_correct))   # OBD wrong, LLM right
107	    a = int(np.sum(obd_correct & llm_correct))     # both right
108	    d = int(np.sum(~obd_correct & ~llm_correct))   # both wrong
109	
110	    n_discordant = b + c
111	    if n_discordant == 0:
112	        p_value = 1.0
113	    else:
114	        result = binomtest(b, n_discordant, 0.5, alternative='two-sided')
115	        p_value = result.pvalue
116	
117	    return {"a": a, "b": b, "c": c, "d": d}, p_value
118	
119	
120	def bootstrap_diff_ci(y_true, obd_preds, llm_preds, n_boot, seed):
121	    rng = np.random.RandomState(seed)
122	    n = len(y_true)
123	    diffs = np.empty(n_boot)
124	    for i in range(n_boot):
125	        idx = rng.randint(0, n, size=n)
126	        acc_obd = np.mean(obd_preds[idx] == y_true[idx])
127	        acc_llm = np.mean(llm_preds[idx] == y_true[idx])
128	        diffs[i] = acc_obd - acc_llm
129	    return diffs
130	
131	
132	def run_comparison(y_true, obd_preds, llm_preds, llm_name):
133	    obd_correct = obd_preds == y_true
134	    llm_correct = llm_preds == y_true
135	
136	    acc_obd = float(np.mean(obd_correct))
137	    acc_llm = float(np.mean(llm_correct))
138	    diff = acc_obd - acc_llm
139	
140	    table, p_value = mcnemar_test(obd_correct, llm_correct)
141	
142	    diffs = bootstrap_diff_ci(y_true, obd_preds, llm_preds, N_BOOTSTRAP, SEED)
143	    ci_lower = float(np.percentile(diffs, 2.5))
144	    ci_upper = float(np.percentile(diffs, 97.5))
145	
146	    print(f"\n--- OBD vs {llm_name} ---")
147	    print(f"  OBD accuracy:  {acc_obd:.3f}")
148	    print(f"  {llm_name} accuracy: {acc_llm:.3f}")
149	    print(f"  Difference:    {diff:+.3f}")
150	    print(f"  Contingency:   a={table['a']}, b={table['b']}, c={table['c']}, d={table['d']}")
151	    print(f"  McNemar exact p = {p_value:.4f}")
152	    print(f"  Bootstrap 95% CI on diff: [{ci_lower:+.4f}, {ci_upper:+.4f}]")
153	    print(f"  CI includes 0: {'YES' if ci_lower <= 0 <= ci_upper else 'NO'}")
154	
155	    return {
156	        "accuracy_obd": round(acc_obd, 4),
157	        "accuracy_llm": round(acc_llm, 4),
158	        "accuracy_diff": round(diff, 4),
159	        "contingency_table": table,
160	        "mcnemar_p": round(p_value, 4),
161	        "bootstrap_ci_lower": round(ci_lower, 4),
162	        "bootstrap_ci_upper": round(ci_upper, 4),
163	        "bootstrap_n": N_BOOTSTRAP,
164	        "n_samples": len(y_true),
165	    }
166	
167	
168	def main():
169	    print("Loading features and running OBD OOF...")
170	    X, depths, doc_ids = load_features()
171	    oof_preds = run_obd_oof(X, depths, doc_ids, MAX_DEPTH, N_SPLITS)
172	
173	    # Build lookup: (depth, orig_doc_id) -> row index
174	    lookup = {}
175	    for i in range(len(depths)):
176	        lookup[(int(depths[i]), int(doc_ids[i]))] = i
177	
178	    # Load exp-011 samples and LLM predictions
179	    with open(SAMPLES_PATH) as f:
180	        samples = [json.loads(line) for line in f]
181	    gpt_preds_map = load_llm_predictions(GPT_PATH)
182	    claude_preds_map = load_llm_predictions(CLAUDE_PATH)
183	
184	    # Align all predictions by sample order
185	    y_true_list = []
186	    obd_pred_list = []
187	    gpt_pred_list = []
188	    claude_pred_list = []
189	    skipped = 0
190	
191	    for s in samples:
192	        doc_id = s["doc_id"]
193	        d, orig_id = parse_exp011_doc_id(doc_id)
194	        key = (d, orig_id)
195	
196	        if key not in lookup:
197	            skipped += 1
198	            continue
199	        if doc_id not in gpt_preds_map or doc_id not in claude_preds_map:
200	            skipped += 1
201	            continue
202	
203	        true_depth = s["true_depth"]
204	        # Cap at 4 for 5-class comparison (depths 0-4 only)
205	        if true_depth > 4:
206	            skipped += 1
207	            continue
208	
209	        row_idx = lookup[key]
210	        y_true_list.append(true_depth)
211	        obd_pred_list.append(min(oof_preds[row_idx], 4))
212	        gpt_pred_list.append(min(gpt_preds_map[doc_id], 4))
213	        claude_pred_list.append(min(claude_preds_map[doc_id], 4))
214	
215	    y_true = np.array(y_true_list)
216	    obd_preds = np.array(obd_pred_list)
217	    gpt_preds = np.array(gpt_pred_list)
218	    claude_preds = np.array(claude_pred_list)
219	
220	    print(f"Aligned {len(y_true)} samples (skipped {skipped})")
221	
222	    result_gpt = run_comparison(y_true, obd_preds, gpt_preds, "GPT-5.5")
223	    result_claude = run_comparison(y_true, obd_preds, claude_preds, "Claude")
224	
225	    output = {
226	        "obd_vs_gpt55": result_gpt,
227	        "obd_vs_claude": result_claude,
228	        "method": "McNemar exact test (binomial) + bootstrap 10k difference CI, OBD out-of-fold",
229	        "seed": SEED,
230	    }
231	
232	    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
233	    with open(OUT_PATH, "w") as f:
234	        json.dump(output, f, indent=2)
235	    print(f"\nSaved to {OUT_PATH}")
236	
237	
238	if __name__ == "__main__":
239	    main()
240	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "740d7d10-51b2-4c84-b397-fe2b63f67200",
  "isSidechain": true,
  "promptId": "8ab46256-1dcf-4174-9343-f64005e6f2a2",
  "agentId": "a6f8fbc29078dceb8",
  "type": "user",
  "uuid": "aa12a936-282c-41f7-9e25-b788f4e62aa7",
  "sourceToolAssistantUUID": "740d7d10-51b2-4c84-b397-fe2b63f67200",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T11:22:11.730Z_

<details open><summary>🔧 Tool call — Read · `toolu_019nZnPYBJbx3YEyL1sGWRga`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/exp_D_obd_n500_v2.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa12a936-282c-41f7-9e25-b788f4e62aa7",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wtczgfUM4QT9yVvXqV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1f579925-c711-4f4d-9bd2-aab759944b3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KDDRCmbY4jbZApkUfRqJRU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1879,
      "cache_read_input_tokens": 18821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1879,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-18T11:22:11.738Z_

<details><summary>↩ Tool result · `toolu_019nZnPYBJbx3YEyL1sGWRga`</summary>

```text
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
57	def run_obd_oof(X, y, groups, max_depth, n_splits):
58	    """OBD: K-1 binary LightGBM classifiers for P(Y > k), out-of-fold."""
59	    import lightgbm as lgb
60	    from sklearn.model_selection import GroupKFold
61	
62	    n = len(y)
63	    cum_probs = np.zeros((n, max_depth))
64	
65	    gkf = GroupKFold(n_splits=n_splits)
66	    fold_indices = list(gkf.split(X, y, groups=groups))
67	
68	    for k in range(max_depth):
69	        y_bin = (y > k).astype(int)
70	        for train_idx, test_idx in fold_indices:
71	            clf = lgb.LGBMClassifier(
72	                n_estimators=200, max_depth=6, learning_rate=0.05,
73	                num_leaves=31, verbose=-1, n_jobs=-1,
74	            )
75	            clf.fit(X[train_idx], y_bin[train_idx])
76	            cum_probs[test_idx, k] = clf.predict_proba(X[test_idx])[:, 1]
77	
78	    n_classes = max_depth + 1
79	    class_probs = np.zeros((n, n_classes))
80	    class_probs[:, 0] = 1.0 - cum_probs[:, 0]
81	    for k in range(1, max_depth):
82	        class_probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]
83	    class_probs[:, max_depth] = cum_probs[:, max_depth - 1]
84	    class_probs = np.clip(class_probs, 0, None)
85	    row_sums = class_probs.sum(axis=1, keepdims=True)
86	    row_sums[row_sums == 0] = 1.0
87	    class_probs /= row_sums
88	
89	    preds = class_probs.argmax(axis=1)
90	    return preds
91	
92	
93	def parse_exp011_doc_id(doc_id_str):
94	    """Parse 'pythia_d{depth}_{orig_id}' -> (depth, orig_id)."""
95	    m = re.match(r"pythia_d(\d+)_(\d+)", doc_id_str)
96	    if not m:
97	        raise ValueError(f"Cannot parse doc_id: {doc_id_str}")
98	    return int(m.group(1)), int(m.group(2))
99	
100	
101	def bootstrap_ci(y_true, y_pred, n_bootstrap, seed=42):
102	    rng = np.random.RandomState(seed)
103	    n = len(y_true)
104	    accs = []
105	    for _ in range(n_bootstrap):
106	        idx = rng.randint(0, n, size=n)
107	        accs.append(float(np.mean(y_pred[idx] == y_true[idx])))
108	    return np.array(accs)
109	
110	
111	def main():
112	    print("Loading features...")
113	    X, depths, doc_ids = load_features()
114	    print(f"  {len(depths)} samples, {len(FEAT_COLS)} features, depths {depths.min()}-{depths.max()}")
115	
116	    print("Running OBD 5-fold CV (K-1 binary classifiers)...")
117	    oof_preds = run_obd_oof(X, depths, doc_ids, MAX_DEPTH, N_SPLITS)
118	    full_acc = float(np.mean(oof_preds == depths))
119	    print(f"  Full OBD accuracy (N={len(depths)}, {MAX_DEPTH+1}-class): {full_acc:.4f}")
120	
121	    print("Loading exp-011 samples...")
122	    with open(SAMPLES_PATH) as f:
123	        samples = [json.loads(line) for line in f]
124	    print(f"  {len(samples)} samples loaded")
125	
126	    # Build (depth, doc_id) -> row index mapping
127	    lookup = {}
128	    for i in range(len(depths)):
129	        lookup[(int(depths[i]), int(doc_ids[i]))] = i
130	
131	    # Match exp-011 samples to features.csv rows
132	    matched_indices = []
133	    matched_true_depths = []
134	    missing = 0
135	    for s in samples:
136	        d, orig_id = parse_exp011_doc_id(s["doc_id"])
137	        key = (d, orig_id)
138	        if key in lookup:
139	            matched_indices.append(lookup[key])
140	            matched_true_depths.append(d)
141	        else:
142	            missing += 1
143	            print(f"  WARNING: sample {s['doc_id']} not found in features.csv")
144	
145	    matched_indices = np.array(matched_indices)
146	    matched_true_depths = np.array(matched_true_depths)
147	    print(f"  Matched {len(matched_indices)} / {len(samples)} samples (missing: {missing})")
148	
149	    # Verify depth consistency
150	    assert np.all(depths[matched_indices] == matched_true_depths), "Depth mismatch!"
151	
152	    # Compute accuracy on the 500 samples
153	    y_true = depths[matched_indices]
154	    y_pred = oof_preds[matched_indices]
155	    accuracy = float(np.mean(y_pred == y_true))
156	    print(f"\n  OBD 5-class accuracy on N=500 (exp-011 samples): {accuracy:.4f}")
157	
158	    # Per-depth accuracy
159	    for d in sorted(set(matched_true_depths)):
160	        mask = matched_true_depths == d
161	        d_acc = float(np.mean(y_pred[mask] == y_true[mask]))
162	        print(f"    depth {d}: {d_acc:.4f} (n={mask.sum()})")
163	
164	    # Bootstrap CI
165	    print(f"\n  Bootstrap CI ({N_BOOTSTRAP} resamples)...")
166	    boot_accs = bootstrap_ci(y_true, y_pred, N_BOOTSTRAP)
167	    ci_lower = float(np.percentile(boot_accs, 2.5))
168	    ci_upper = float(np.percentile(boot_accs, 97.5))
169	    print(f"  95% CI: [{ci_lower:.4f}, {ci_upper:.4f}]")
170	
171	    gpt_acc = 0.332
172	    claude_acc = 0.331
173	
174	    result = {
175	        "obd_n500_accuracy": round(accuracy, 4),
176	        "obd_n500_ci_lower": round(ci_lower, 4),
177	        "obd_n500_ci_upper": round(ci_upper, 4),
178	        "n_bootstrap": N_BOOTSTRAP,
179	        "n_samples": len(matched_indices),
180	        "sample_source": "exp011_samples.jsonl (same as LLM baseline)",
181	        "gpt55_n500_accuracy": gpt_acc,
182	        "claude_n500_accuracy": claude_acc,
183	        "obd_full_accuracy": round(full_acc, 4),
184	        "obd_full_n": len(depths),
185	        "method": "OBD-LightGBM out-of-fold predictions, same 500 samples as exp-011",
186	        "obd_hyperparams": {
187	            "n_estimators": 200,
188	            "max_depth": 6,
189	            "learning_rate": 0.05,
190	            "num_leaves": 31,
191	            "n_binary_classifiers": MAX_DEPTH,
192	            "n_folds": N_SPLITS,
193	        },
194	        "per_depth_accuracy": {
195	            str(d): round(float(np.mean(y_pred[matched_true_depths == d] == y_true[matched_true_depths == d])), 4)
196	            for d in sorted(set(matched_true_depths))
197	        },
198	        "conclusion": (
199	            f"OBD at N=500 achieves {accuracy:.1%} "
200	            f"[{ci_lower:.1%}, {ci_upper:.1%}], "
201	            f"above LLM baselines (GPT-5.5: {gpt_acc:.1%}, Claude: {claude_acc:.1%})"
202	        ),
203	    }
204	
205	    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
206	    with open(OUT_PATH, "w") as f:
207	        json.dump(result, f, indent=2)
208	    print(f"\nSaved to {OUT_PATH}")
209	    print(f"Conclusion: {result['conclusion']}")
210	
211	
212	if __name__ == "__main__":
213	    main()
214	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f579925-c711-4f4d-9bd2-aab759944b3c",
  "isSidechain": true,
  "promptId": "8ab46256-1dcf-4174-9343-f64005e6f2a2",
  "agentId": "a6f8fbc29078dceb8",
  "type": "user",
  "uuid": "f034c461-6f80-4654-b345-6daa8ff3e6c5",
  "sourceToolAssistantUUID": "1f579925-c711-4f4d-9bd2-aab759944b3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T11:22:12.149Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JUZoSuKXzddeHFdr18mK7P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/draw_kstar_theta.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f034c461-6f80-4654-b345-6daa8ff3e6c5",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wtczgfUM4QT9yVvXqV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ff264894-450e-41e5-9e4a-4fe2251259e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KDDRCmbY4jbZApkUfRqJRU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1879,
      "cache_read_input_tokens": 18821,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1879,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T11:22:12.155Z_

<details><summary>↩ Tool result · `toolu_01JUZoSuKXzddeHFdr18mK7P`</summary>

```text
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
55	        (r"llama", "LLaMA-8B"),
56	    ]
57	    for pat, label in patterns:
58	        if re.search(pat, name, re.IGNORECASE):
59	            return label
60	    return name or source_path.parent.name
61	
62	
63	def discover_ci_files(root: Path) -> list[Path]:
64	    """Find all bootstrap CI JSON files."""
65	    patterns = [
66	        "artifacts/*bootstrap*ci*.json",
67	        "artifacts/exp*_bootstrap_ci.json",
68	        "results_*/*bootstrap*ci*.json",
69	        "results_*/bootstrap_ci.json",
70	        "results/*/*bootstrap*ci*.json",
71	    ]
72	    files = set()
73	    for pat in patterns:
74	        files.update(root.glob(pat))
75	    return sorted(files)
76	
77	
78	def load_ci_lower_bounds(json_path: Path) -> tuple[list[float], dict | None]:
79	    """Extract CI lower bounds for ordered pairs. Returns ([ci_lower...], metadata)."""
80	    with open(json_path) as f:
81	        raw = json.load(f)
82	
83	    pair_keys = ["0v1", "1v2", "2v3", "3v4", "4v5"]
84	    ci_lowers = []
85	
86	    if "pairs" in raw:
87	        pairs = raw["pairs"]
88	        for k in pair_keys:
89	            if k in pairs:
90	                ci_lowers.append(pairs[k].get("ci_lower", pairs[k].get("auc", 0.5)))
91	        return ci_lowers, raw
92	    else:
93	        for k in pair_keys:
94	            if k in raw:
95	                val = raw[k]
96	                if isinstance(val, dict):
97	                    ci_lowers.append(val.get("ci_lower", val.get("auc", 0.5)))
98	                else:
99	                    ci_lowers.append(val)
100	        return ci_lowers, raw
101	
102	
103	def compute_kstar(auc_list: list[float], theta: float) -> int:
104	    """Compute K* = max consecutive pairs with AUC >= theta."""
105	    k = 0
106	    for auc in auc_list:
107	        if auc >= theta:
108	            k += 1
109	        else:
110	            break
111	    return k
112	
113	
114	def parse_args():
115	    parser = argparse.ArgumentParser(description="Plot K*(theta) step function")
116	    parser.add_argument("--results-dir", type=Path,
117	                        default=Path(__file__).resolve().parent.parent,
118	                        help="Root directory to scan for bootstrap CI files")
119	    parser.add_argument("--output", type=Path, default=None,
120	                        help="Output PDF path")
121	    parser.add_argument("--filter", type=str, default=None,
122	                        help="Filter models by substring")
123	    return parser.parse_args()
124	
125	
126	def main():
127	    args = parse_args()
128	    root = args.results_dir
129	
130	    ci_files = discover_ci_files(root)
131	    if not ci_files:
132	        print(f"No bootstrap CI files found under {root}")
133	        return
134	
135	    models = {}
136	    for fp in ci_files:
137	        ci_lowers, metadata = load_ci_lower_bounds(fp)
138	        if not ci_lowers or len(ci_lowers) < 2:
139	            continue
140	        label = infer_label(fp, metadata)
141	        if args.filter and args.filter.lower() not in label.lower():
142	            continue
143	        models[label] = ci_lowers
144	
145	    if not models:
146	        print("No valid CI data found after filtering")
147	        return
148	
149	    thetas = np.arange(0.50, 0.751, 0.01)
150	
151	    plt.rcParams.update({
152	        "font.family": "serif",
153	        "font.size": 11,
154	        "axes.linewidth": 0.8,
155	        "xtick.direction": "in",
156	        "ytick.direction": "in",
157	    })
158	
159	    fig, ax = plt.subplots(figsize=(6, 3.5))
160	
161	    for i, (name, aucs) in enumerate(models.items()):
162	        color = TABLEAU_COLORS[i % len(TABLEAU_COLORS)]
163	        marker = MARKERS[i % len(MARKERS)]
164	        ls = LINESTYLES[i % len(LINESTYLES)]
165	        ks = [compute_kstar(aucs, t) for t in thetas]
166	        ax.step(thetas, ks, where="post", label=name,
167	                linewidth=1.8, color=color, linestyle=ls)
168	
169	    ax.axvline(x=0.60, color="grey", linestyle="--", linewidth=0.8, alpha=0.7)
170	    ax.text(0.605, max(len(list(models.values())[0]), 4) + 0.3,
171	            r"$\theta=0.60$", color="grey", fontsize=9, va="top")
172	
173	    ax.set_xlabel(r"Threshold $\theta$")
174	    ax.set_ylabel(r"$K^*(\theta)$")
175	    ax.set_xlim(0.495, 0.755)
176	    max_k = max(len(v) for v in models.values())
177	    ax.set_ylim(-0.2, max_k + 0.5)
178	    ax.set_yticks(range(max_k + 1))
179	    ax.legend(loc="best", fontsize=9, framealpha=0.9, edgecolor="none")
180	    ax.grid(axis="y", color="#e0e0e0", linewidth=0.5)
181	
182	    fig.tight_layout()
183	
184	    if args.output:
185	        out_path = args.output
186	    else:
187	        out_dir = Path(__file__).resolve().parent.parent / "docs" / "paper" / "figures"
188	        out_dir.mkdir(parents=True, exist_ok=True)
189	        out_path = out_dir / "fig_kstar_theta.pdf"
190	
191	    out_path.parent.mkdir(parents=True, exist_ok=True)
192	    fig.savefig(out_path, bbox_inches="tight")
193	    fig.savefig(out_path.with_suffix(".png"), bbox_inches="tight", dpi=300)
194	    plt.close(fig)
195	
196	    print(f"Discovered {len(models)} models: {list(models.keys())}")
197	    print(f"Saved to {out_path}")
198	    pdf_size = out_path.stat().st_size
199	    assert pdf_size > 3 * 1024, f"PDF too small: {pdf_size}"
200	    print("OK")
201	
202	
203	if __name__ == "__main__":
204	    main()
205	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff264894-450e-41e5-9e4a-4fe2251259e3",
  "isSidechain": true,
  "promptId": "8ab46256-1dcf-4174-9343-f64005e6f2a2",
  "agentId": "a6f8fbc29078dceb8",
  "type": "user",
  "uuid": "1c0c453a-0a72-4742-b72b-35dc90fd6e43",
  "sourceToolAssistantUUID": "ff264894-450e-41e5-9e4a-4fe2251259e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T11:22:12.311Z_

<details open><summary>🔧 Tool call — Read · `toolu_011nbLmHxG3up5JemEDf7kiC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp008_retrain_chain.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c0c453a-0a72-4742-b72b-35dc90fd6e43",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wtczgfUM4QT9yVvXqV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "44a3264a-52d9-4363-961b-772c5f0851b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KDDRCmbY4jbZApkUfRqJRU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1879,
      "cache_read_input_tokens": 18821,
      "output_tokens": 417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1879
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 417,
          "cache_read_input_tokens": 18821,
          "cache_creation_input_tokens": 1879,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1879,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T11:22:12.568Z_

<details><summary>↩ Tool result · `toolu_011nbLmHxG3up5JemEDf7kiC`</summary>

```text
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
67	        for r in records:
68	            f.write(json.dumps(r, ensure_ascii=False) + "\n")
69	
70	
71	def ngrams(tokens, n):
72	    return [tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]
73	
74	
75	def simple_bleu(candidate_tokens, reference_tokens, max_n=4):
76	    if len(candidate_tokens) == 0:
77	        return 0.0
78	    precisions = []
79	    for n in range(1, max_n + 1):
80	        cand_ngrams = ngrams(candidate_tokens, n)
81	        ref_ngrams = ngrams(reference_tokens, n)
82	        if not cand_ngrams:
83	            precisions.append(0.0)
84	            continue
85	        ref_counts = Counter(ref_ngrams)
86	        clipped = sum(min(cnt, ref_counts.get(ng, 0)) for ng, cnt in Counter(cand_ngrams).items())
87	        precisions.append(clipped / len(cand_ngrams))
88	    if any(p == 0 for p in precisions):
89	        return 0.0
90	    log_avg = sum(math.log(p) for p in precisions) / max_n
91	    bp = min(1.0, math.exp(1 - len(reference_tokens) / max(len(candidate_tokens), 1)))
92	    return bp * math.exp(log_avg)
93	
94	
95	# ---------------------------------------------------------------------------
96	# Phase 1: LoRA Fine-tuning
97	# ---------------------------------------------------------------------------
98	
99	def finetune_lora(base_model_path, train_texts, device="cuda:0"):
100	    from transformers import AutoModelForCausalLM, AutoTokenizer, DataCollatorForLanguageModeling
101	    from peft import LoraConfig, get_peft_model, TaskType
102	    from torch.utils.data import Dataset, DataLoader
103	
104	    log.info(f"Loading base model for fine-tuning ({len(train_texts)} texts)...")
105	    tokenizer = AutoTokenizer.from_pretrained(base_model_path)
106	    if tokenizer.pad_token is None:
107	        tokenizer.pad_token = tokenizer.eos_token
108	        tokenizer.pad_token_id = tokenizer.eos_token_id
109	
110	    model = AutoModelForCausalLM.from_pretrained(
111	        base_model_path, torch_dtype=torch.float16, device_map={"": device}
112	    )
113	
114	    lora_config = LoraConfig(
115	        task_type=TaskType.CAUSAL_LM,
116	        r=LORA_RANK,
117	        lora_alpha=LORA_ALPHA,
118	        target_modules=LORA_TARGET_MODULES,
119	        lora_dropout=0.05,
120	        bias="none",
121	    )
122	    model = get_peft_model(model, lora_config)
123	    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
124	    total = sum(p.numel() for p in model.parameters())
125	    log.info(f"LoRA params: {trainable:,} / {total:,} ({100*trainable/total:.2f}%)")
126	
127	    class TextDataset(Dataset):
128	        def __init__(self, texts, tokenizer, max_length=256):
129	            self.encodings = []
130	            for t in texts:
131	                ids = tokenizer.encode(t, add_special_tokens=True, truncation=True, max_length=max_length)
132	                self.encodings.append(torch.tensor(ids, dtype=torch.long))
133	
134	        def __len__(self):
135	            return len(self.encodings)
136	
137	        def __getitem__(self, idx):
138	            ids = self.encodings[idx]
139	            return {"input_ids": ids, "labels": ids.clone()}
140	
141	    dataset = TextDataset(train_texts, tokenizer, max_length=GEN_MAX_NEW_TOKENS)
142	    collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
143	    dataloader = DataLoader(
144	        dataset, batch_size=TRAIN_BATCH_SIZE, shuffle=True, collate_fn=collator
145	    )
146	
147	    optimizer = torch.optim.AdamW(
148	        [p for p in model.parameters() if p.requires_grad], lr=TRAIN_LR
149	    )
150	
151	    model.train()
152	    total_loss = 0.0
153	    steps = 0
154	    optimizer.zero_grad()
155	
156	    for epoch in range(TRAIN_EPOCHS):
157	        for batch_idx, batch in enumerate(tqdm(dataloader, desc="Fine-tuning")):
158	            batch = {k: v.to(device) for k, v in batch.items()}
159	            outputs = model(**batch)
160	            loss = outputs.loss / GRADIENT_ACCUMULATION
161	            loss.backward()
162	            total_loss += loss.item() * GRADIENT_ACCUMULATION
163	
164	            if (batch_idx + 1) % GRADIENT_ACCUMULATION == 0:
165	                optimizer.step()
166	                optimizer.zero_grad()
167	                steps += 1
168	
169	        # final accumulation step
170	        if (batch_idx + 1) % GRADIENT_ACCUMULATION != 0:
171	            optimizer.step()
172	            optimizer.zero_grad()
173	            steps += 1
174	
175	    avg_loss = total_loss / max(len(dataloader), 1)
176	    log.info(f"Fine-tuning done. Avg loss: {avg_loss:.4f}, steps: {steps}")
177	
178	    model.eval()
179	    return model, tokenizer
180	
181	
182	# ---------------------------------------------------------------------------
183	# Phase 2: Text Generation (continuation mode for base model)
184	# ---------------------------------------------------------------------------
185	
186	def generate_texts(model, tokenizer, input_texts, device="cuda:0"):
187	    log.info(f"Generating {len(input_texts)} texts (nucleus p={GEN_TOP_P}, T={GEN_TEMPERATURE})...")
188	    tokenizer.padding_side = "left"
189	    results = []
190	
191	    for start in tqdm(range(0, len(input_texts), GEN_BATCH_SIZE), desc="Generating"):
192	        batch_texts = input_texts[start:start + GEN_BATCH_SIZE]
193	
194	        # continuation mode: use first half as prefix, generate rest
195	        prefix_texts = []
196	        for text in batch_texts:
197	            ids = tokenizer.encode(text, add_special_tokens=False)
198	            prefix_len = max(1, len(ids) // 2)
199	            prefix_texts.append(tokenizer.decode(ids[:prefix_len], skip_special_tokens=True))
200	
201	        inputs = tokenizer(
202	            prefix_texts, return_tensors="pt", padding=True, truncation=True, max_length=256
203	        ).to(device)
204	
205	        with torch.no_grad():
206	            outputs = model.generate(
207	                **inputs,
208	                max_new_tokens=GEN_MAX_NEW_TOKENS,
209	                do_sample=True,
210	                top_p=GEN_TOP_P,
211	                temperature=GEN_TEMPERATURE,
212	                pad_token_id=tokenizer.pad_token_id,
213	            )
214	
215	        for j, out_ids in enumerate(outputs):
216	            prompt_len = inputs["input_ids"].shape[1]
217	            generated_ids = out_ids[prompt_len:]
218	            text = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
219	            results.append(text)
220	
221	        torch.cuda.empty_cache()
222	
223	    return results
224	
225	
226	# ---------------------------------------------------------------------------
227	# Phase 3: Feature extraction (using scorer)
228	# ---------------------------------------------------------------------------
229	
230	SURPRISAL_COLS = [
231	    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
232	    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
233	    "surp_d2_mean", "surp_d2_std",
234	]
235	VOCAB_COLS = ["ttr", "hapax_ratio", "self_bleu"]
236	TAIL_COLS = ["freq_kurtosis", "freq_entropy", "low_freq_ratio"]
237	ALL_FEAT_COLS = SURPRISAL_COLS + VOCAB_COLS + TAIL_COLS
238	
239	
240	def compute_surprisal_features(model, tokenizer, texts, batch_size=8):
241	    features = []
242	    tokenizer.padding_side = "left"
243	
244	    for start in tqdm(range(0, len(texts), batch_size), desc="Surprisal"):
245	        batch_texts = texts[start:start + batch_size]
246	        inputs = tokenizer(
247	            batch_texts, return_tensors="pt", padding=True, truncation=True, max_length=512
248	        ).to(model.device)
249	
250	        with torch.no_grad():
251	            outputs = model(**inputs)
252	            logits = outputs.logits
253	
254	        for j in range(len(batch_texts)):
255	            ids = inputs["input_ids"][j]
256	            attn = inputs["attention_mask"][j]
257	            valid_len = attn.sum().item()
258	            if valid_len < 3:
259	                features.append([0.0] * 9)
260	                continue
261	
262	            valid_logits = logits[j, :valid_len - 1]
263	            valid_targets = ids[1:valid_len]
264	
265	            log_probs = torch.log_softmax(valid_logits.float(), dim=-1)
266	            token_surprisals = -log_probs.gather(1, valid_targets.unsqueeze(1)).squeeze(1)
267	            surp = token_surprisals.cpu().numpy()
268	
269	            if len(surp) < 2:
270	                features.append([0.0] * 9)
271	                continue
272	
273	            s_mean = float(np.mean(surp))
274	            s_std = float(np.std(surp))
275	            s_skew = float(stats.skew(surp)) if len(surp) >= 3 else 0.0
276	            s_kurt = float(stats.kurtosis(surp)) if len(surp) >= 4 else 0.0
277	
278	            d1 = np.diff(surp)
279	            d1_mean = float(np.mean(d1)) if len(d1) > 0 else 0.0
280	            d1_std = float(np.std(d1)) if len(d1) > 0 else 0.0
281	            d1_skew = float(stats.skew(d1)) if len(d1) >= 3 else 0.0
282	
283	            d2 = np.diff(d1)
284	            d2_mean = float(np.mean(d2)) if len(d2) > 0 else 0.0
285	            d2_std = float(np.std(d2)) if len(d2) > 0 else 0.0
286	
287	            features.append([s_mean, s_std, s_skew, s_kurt, d1_mean, d1_std, d1_skew, d2_mean, d2_std])
288	
289	        torch.cuda.empty_cache()
290	
291	    return features
292	
293	
294	def compute_vocab_diversity(texts, tokenizer, depth_texts_map, depth, bleu_refs=100):
295	    same_depth_tokens = [tokenizer.encode(t, add_special_tokens=False) for t in texts]
296	    features = []
297	
298	    for idx, tokens in enumerate(tqdm(same_depth_tokens, desc=f"Vocab d={depth}", leave=False)):
299	        total = len(tokens)
300	        if total == 0:
301	            features.append([0.0, 0.0, 0.0])
302	            continue
303	
304	        ttr = len(set(tokens)) / total
305	        freq = Counter(tokens)
306	        hapax_ratio = sum(1 for v in freq.values() if v == 1) / max(len(set(tokens)), 1)
307	
308	        rng_local = np.random.RandomState(idx)
309	        ref_pool = [j for j in range(len(same_depth_tokens)) if j != idx]
310	        if len(ref_pool) > bleu_refs:
311	            ref_pool = rng_local.choice(ref_pool, bleu_refs, replace=False).tolist()
312	        bleu_scores = [simple_bleu(tokens, same_depth_tokens[j]) for j in ref_pool]
313	        self_bleu = float(np.mean(bleu_scores)) if bleu_scores else 0.0
314	
315	        features.append([ttr, hapax_ratio, self_bleu])
316	
317	    return features
318	
319	
320	def compute_tail_features(texts):
321	    features = []
322	    for text in texts:
323	        tokens = text.split()
324	        if len(tokens) < 2:
325	            features.append([0.0, 0.0, 0.0])
326	            continue
327	        freq = Counter(tokens)
328	        counts = np.array(list(freq.values()), dtype=float)
329	        kurt = float(stats.kurtosis(counts)) if len(counts) >= 4 else 0.0
330	        total = counts.sum()
331	        probs = counts / total
332	        entropy = float(-np.sum(probs * np.log2(probs + 1e-12)))
333	        low_freq_ratio = float(np.sum(counts <= 2)) / max(len(counts), 1)
334	        features.append([kurt, entropy, low_freq_ratio])
335	    return features
336	
337	
338	def extract_all_features(scorer_path, data_dir, max_depth, device="cuda:0"):
339	    import csv
340	    from transformers import AutoModelForCausalLM, AutoTokenizer
341	
342	    out_path = data_dir / "features.csv"
343	    log.info(f"Loading scorer from {scorer_path}...")
344	    tokenizer = AutoTokenizer.from_pretrained(scorer_path, trust_remote_code=True)
345	    if tokenizer.pad_token is None:
346	        tokenizer.pad_token = tokenizer.eos_token
347	        tokenizer.pad_token_id = tokenizer.eos_token_id
348	    tokenizer.padding_side = "left"
349	
350	    model = AutoModelForCausalLM.from_pretrained(
351	        scorer_path, torch_dtype=torch.float16, device_map={"": device}, trust_remote_code=True
352	    )
353	    model.eval()
354	
355	    depth_texts = {}
356	    for d in range(max_depth + 1):
357	        records = load_jsonl(data_dir / f"depth_{d}.jsonl")
358	        depth_texts[d] = [r["text"] for r in records]
359	
360	    rows = []
361	    for d in range(max_depth + 1):
362	        texts = depth_texts[d]
363	        records = load_jsonl(data_dir / f"depth_{d}.jsonl")
364	        doc_ids = [r["doc_id"] for r in records]
365	        log.info(f"  Extracting features depth {d}: {len(texts)} texts")
366	
367	        surp = compute_surprisal_features(model, tokenizer, texts, batch_size=8)
368	        vocab = compute_vocab_diversity(texts, tokenizer, depth_texts, d)
369	        tail = compute_tail_features(texts)
370	
371	        for i in range(len(texts)):
372	            row = {"doc_id": doc_ids[i], "depth": d}
373	            for j, col in enumerate(SURPRISAL_COLS):
374	                row[col] = surp[i][j]
375	            for j, col in enumerate(VOCAB_COLS):
376	                row[col] = vocab[i][j]
377	            for j, col in enumerate(TAIL_COLS):
378	                row[col] = tail[i][j]
379	            rows.append(row)
380	
381	    with open(out_path, "w", newline="") as f:
382	        writer = csv.DictWriter(f, fieldnames=["doc_id", "depth"] + ALL_FEAT_COLS)
383	        writer.writeheader()
384	        writer.writerows(rows)
385	    log.info(f"Saved {len(rows)} feature rows to {out_path}")
386	
387	    del model
388	    torch.cuda.empty_cache()
389	    gc.collect()
390	
391	
392	# ---------------------------------------------------------------------------
393	# Phase 4: Analysis (pairwise AUC, JSD, K*, bootstrap CI, permutation test)
394	# ---------------------------------------------------------------------------
395	
396	def run_analysis(data_dir, results_dir, max_depth):
397	    import csv
398	    import lightgbm as lgb
399	    from sklearn.model_selection import GroupKFold
400	    from sklearn.metrics import roc_auc_score
401	
402	    results_dir.mkdir(parents=True, exist_ok=True)
403	    feat_path = data_dir / "features.csv"
404	    log.info(f"Loading features from {feat_path}...")
405	
406	    with open(feat_path) as f:
407	        reader = csv.DictReader(f)
408	        rows = list(reader)
409	
410	    depths = np.array([int(r["depth"]) for r in rows])
411	    doc_ids = np.array([int(r["doc_id"]) for r in rows])
412	    feat_matrix = np.array(
413	        [[float(r[c]) if r[c] not in ("", "nan") else np.nan for c in ALL_FEAT_COLS] for r in rows]
414	    )
415	    col_means = np.nanmean(feat_matrix, axis=0)
416	    for j in range(feat_matrix.shape[1]):
417	        mask = np.isnan(feat_matrix[:, j])
418	        feat_matrix[mask, j] = col_means[j]
419	
420	    # Pairwise AUC with GroupKFold
421	    log.info("Computing pairwise AUC...")
422	    pairwise_auc = {}
423	    pairwise_auc_folds = {}
424	    for k in range(1, max_depth + 1):
425	        mask = (depths == k - 1) | (depths == k)
426	        X = feat_matrix[mask]
427	        y = (depths[mask] == k).astype(int)
428	        if len(np.unique(y)) < 2:
429	            pairwise_auc[f"{k-1}v{k}"] = float("nan")
430	            continue
431	
432	        gkf = GroupKFold(n_splits=5)
433	        groups = doc_ids[mask]
434	        fold_aucs = []
435	        for train_idx, test_idx in gkf.split(X, y, groups=groups):
436	            clf = lgb.LGBMClassifier(
437	                n_estimators=200, max_depth=6, learning_rate=0.05,
438	                num_leaves=31, verbose=-1, n_jobs=-1,
439	            )
440	            clf.fit(X[train_idx], y[train_idx])
441	            proba = clf.predict_proba(X[test_idx])[:, 1]
442	            fold_aucs.append(roc_auc_score(y[test_idx], proba))
443	        auc_mean = float(np.mean(fold_aucs))
444	        auc_std = float(np.std(fold_aucs))
445	        pairwise_auc[f"{k-1}v{k}"] = round(auc_mean, 4)
446	        pairwise_auc_folds[f"{k-1}v{k}"] = [round(a, 4) for a in fold_aucs]
447	        log.info(f"  AUC({k-1} vs {k}) = {auc_mean:.4f} +/- {auc_std:.4f}")
448	
449	    with open(results_dir / "pairwise_auc.json", "w") as f:
450	        json.dump({"mean": pairwise_auc, "per_fold": pairwise_auc_folds}, f, indent=2)
451	
452	    # JSD
453	    log.info("Computing pairwise JSD...")
454	    pairwise_jsd = {}
455	    for k in range(1, max_depth + 1):
456	        feat_prev = feat_matrix[depths == k - 1]
457	        feat_curr = feat_matrix[depths == k]
458	        jsds = []
459	        for j in range(feat_matrix.shape[1]):
460	            a, b = feat_prev[:, j], feat_curr[:, j]
461	            lo, hi = min(a.min(), b.min()), max(a.max(), b.max())
462	            if hi - lo < 1e-12:
463	                jsds.append(0.0)
464	                continue
465	            bins = np.linspace(lo, hi, 51)
466	            p = np.histogram(a, bins=bins, density=True)[0] + 1e-12
467	            q = np.histogram(b, bins=bins, density=True)[0] + 1e-12
468	            p, q = p / p.sum(), q / q.sum()
469	            m = 0.5 * (p + q)
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
519	            log.info(f"  Bootstrap AUC({k-1}v{k}): {np.mean(boot_aucs):.4f} [{ci_lo:.4f}, {ci_hi:.4f}]")
520	
521	    with open(results_dir / "bootstrap_ci.json", "w") as f:
522	        json.dump(bootstrap_results, f, indent=2)
523	
524	    # Permutation test
525	    log.info("Permutation test (1000 permutations)...")
526	    perm_results = {}
527	    for k in range(1, max_depth + 1):
528	        mask = (depths == k - 1) | (depths == k)
529	        X = feat_matrix[mask]
530	        y = (depths[mask] == k).astype(int)
531	        if len(np.unique(y)) < 2:
532	            continue
533	
534	        clf = lgb.LGBMClassifier(
535	            n_estimators=200, max_depth=6, learning_rate=0.05,
536	            num_leaves=31, verbose=-1, n_jobs=-1,
537	        )
538	        clf.fit(X, y)
539	        true_auc = roc_auc_score(y, clf.predict_proba(X)[:, 1])
540	
541	        null_aucs = []
542	        for _ in range(1000):
543	            y_perm = rng.permutation(y)
544	            clf_p = lgb.LGBMClassifier(
545	                n_estimators=200, max_depth=6, learning_rate=0.05,
546	                num_leaves=31, verbose=-1, n_jobs=-1,
547	            )
548	            clf_p.fit(X, y_perm)
549	            null_aucs.append(roc_auc_score(y_perm, clf_p.predict_proba(X)[:, 1]))
550	
551	        p_value = float(np.mean([a >= true_auc for a in null_aucs]))
552	        perm_results[f"{k-1}v{k}"] = {"true_auc": round(true_auc, 4), "p_value": round(p_value, 4)}
553	        log.info(f"  Perm test({k-1}v{k}): true_auc={true_auc:.4f}, p={p_value:.4f}")
554	
555	    with open(results_dir / "permutation_test.json", "w") as f:
556	        json.dump(perm_results, f, indent=2)
557	
558	    # Summary
559	    summary = {
560	        "experiment": "exp-008 retrain-chain",
561	        "model": "Pythia-1.4B",
562	        "scorer": "Qwen2.5-1.5B",
563	        "protocol": "retrain-chain (independent LoRA per generation)",
564	        "lora_config": {"rank": LORA_RANK, "alpha": LORA_ALPHA, "target_modules": LORA_TARGET_MODULES},
565	        "decoding": {"top_p": GEN_TOP_P, "temperature": GEN_TEMPERATURE},
566	        "max_depth": max_depth,
567	        "num_samples": NUM_SAMPLES,
568	        "k_star": k_star,
569	        "pairwise_auc": pairwise_auc,
570	        "pairwise_jsd": pairwise_jsd,
571	        "bootstrap_ci": bootstrap_results,
572	        "permutation_test": perm_results,
573	    }
574	    with open(results_dir / "summary.json", "w") as f:
575	        json.dump(summary, f, indent=2)
576	    log.info(f"Summary saved. K*={k_star}")
577	
578	    return summary
579	
580	
581	# ---------------------------------------------------------------------------
582	# Main pipeline
583	# ---------------------------------------------------------------------------
584	
585	def main():
586	    parser = argparse.ArgumentParser(description="exp-008: retrain-chain ecological validity")
587	    parser.add_argument("--data_dir", type=str,
588	                        default="/root/autodl-tmp/gen-depth-contamination/data/exp_008_retrain_chain")
589	    parser.add_argument("--results_dir", type=str,
590	                        default="/root/autodl-tmp/gen-depth-contamination/results/exp_008_retrain_chain")
591	    parser.add_argument("--log_file", type=str,
592	                        default="/root/autodl-tmp/gen-depth-contamination/logs/exp_008_retrain_chain.log")
593	    parser.add_argument("--device", type=str, default="cuda:0")
594	    parser.add_argument("--max_depth", type=int, default=MAX_DEPTH)
595	    parser.add_argument("--skip_generation", action="store_true", help="Skip to evaluation only")
596	    args = parser.parse_args()
597	
598	    data_dir = Path(args.data_dir)
599	    results_dir = Path(args.results_dir)
600	    data_dir.mkdir(parents=True, exist_ok=True)
601	    results_dir.mkdir(parents=True, exist_ok=True)
602	
603	    # Setup file logging
604	    log_path = Path(args.log_file)
605	    log_path.parent.mkdir(parents=True, exist_ok=True)
606	    fh = logging.FileHandler(log_path)
607	    fh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S"))
608	    logging.getLogger().addHandler(fh)
609	
610	    log.info("=" * 60)
611	    log.info("exp-008: Retrain-chain ecological validity experiment")
612	    log.info(f"Model: {PYTHIA_PATH}")
613	    log.info(f"Scorer: {SCORER_PATH}")
614	    log.info(f"LoRA: rank={LORA_RANK}, alpha={LORA_ALPHA}, target={LORA_TARGET_MODULES}")
615	    log.info(f"Decoding: nucleus p={GEN_TOP_P}, T={GEN_TEMPERATURE}")
616	    log.info(f"Data dir: {data_dir}")
617	    log.info(f"Max depth: {args.max_depth}")
618	    log.info("=" * 60)
619	
620	    if not args.skip_generation:
621	        # Copy seed data
622	        seed_dest = data_dir / "depth_0.jsonl"
623	        if not seed_dest.exists():
624	            log.info(f"Copying seed data from {SEED_DATA}")
625	            shutil.copy2(SEED_DATA, seed_dest)
626	        log.info(f"Seed data: {sum(1 for _ in open(seed_dest))} docs")
627	
628	        # Retrain-chain loop
629	        for d in range(args.max_depth):
630	            log.info("=" * 40 + f" Generation {d} -> {d+1} " + "=" * 40)
631	            out_path = data_dir / f"depth_{d+1}.jsonl"
632	
633	            if out_path.exists() and sum(1 for _ in open(out_path)) >= NUM_SAMPLES:
634	                log.info(f"depth_{d+1}.jsonl already exists ({sum(1 for _ in open(out_path))} docs) — skipping")
635	                continue
636	
637	            # Load training data for this depth
638	            train_records = load_jsonl(data_dir / f"depth_{d}.jsonl")
639	            train_texts = [r["text"] for r in train_records]
640	            log.info(f"Training on {len(train_texts)} texts from depth_{d}")
641	
642	            # Fine-tune with LoRA
643	            model, tokenizer = finetune_lora(PYTHIA_PATH, train_texts, device=args.device)
644	
645	            # Generate next depth
646	            generated_texts = generate_texts(model, tokenizer, train_texts, device=args.device)
647	
648	            # Save
649	            records = [{"text": t, "doc_id": i} for i, t in enumerate(generated_texts)]
650	            save_jsonl(records, out_path)
651	            log.info(f"Saved {len(records)} docs to {out_path}")
652	
653	            # Cleanup
654	            del model, tokenizer
655	            torch.cuda.empty_cache()
656	            gc.collect()
657	            log.info(f"Generation {d}->{d+1} complete, memory released")
658	
659	    # Feature extraction
660	    log.info("=" * 40 + " Feature Extraction " + "=" * 40)
661	    extract_all_features(SCORER_PATH, data_dir, args.max_depth, device=args.device)
662	
663	    # Analysis
664	    log.info("=" * 40 + " Analysis " + "=" * 40)
665	    summary = run_analysis(data_dir, results_dir, args.max_depth)
666	
667	    log.info("=" * 60)
668	    log.info(f"DONE. K*={summary['k_star']}")
669	    log.info(f"Results: {results_dir}")
670	    log.info("=" * 60)
671	
672	
673	if __name__ == "__main__":
674	    main()
675	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44a3264a-52d9-4363-961b-772c5f0851b7",
  "isSidechain": true,
  "promptId": "8ab46256-1dcf-4174-9343-f64005e6f2a2",
  "agentId": "a6f8fbc29078dceb8",
  "type": "user",
  "uuid": "2d796f5f-ed97-468b-ae83-3514be69f077",
  "sourceToolAssistantUUID": "44a3264a-52d9-4363-961b-772c5f0851b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-18T11:22:19.713Z_

Excellent findings. Let me search for a few more specific files and check if there's a dedicated bootstrap CI script in the scripts directory:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d796f5f-ed97-468b-ae83-3514be69f077",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wtvCXrb9p88eZhhfC4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2a38df7f-587b-49fc-8e31-32e4461b08e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AddK4avyVo7CsQsVdA9fzw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 23964,
      "cache_read_input_tokens": 20700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23964,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T11:22:20.358Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Qew1uLEPweYXD4HUbvJrzV`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a38df7f-587b-49fc-8e31-32e4461b08e0",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wtvCXrb9p88eZhhfC4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "290fe67c-968c-4ad8-bfe1-a61edd0c1621",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AddK4avyVo7CsQsVdA9fzw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 23964,
      "cache_read_input_tokens": 20700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23964,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T11:22:20.523Z_

<details><summary>↩ Tool result · `toolu_01Qew1uLEPweYXD4HUbvJrzV`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "290fe67c-968c-4ad8-bfe1-a61edd0c1621",
  "isSidechain": true,
  "promptId": "8ab46256-1dcf-4174-9343-f64005e6f2a2",
  "agentId": "a6f8fbc29078dceb8",
  "type": "user",
  "uuid": "e8f731a4-aec8-4d2b-bc34-de34c2031986",
  "sourceToolAssistantUUID": "290fe67c-968c-4ad8-bfe1-a61edd0c1621",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T11:22:21.138Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01GWNJBsWS6oWYf2Qmteqya5`</summary>

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
  "recorded_role": "assistant",
  "parentUuid": "e8f731a4-aec8-4d2b-bc34-de34c2031986",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wtvCXrb9p88eZhhfC4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3eca8ed7-3764-499b-9429-0178836f384e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AddK4avyVo7CsQsVdA9fzw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 23964,
      "cache_read_input_tokens": 20700,
      "output_tokens": 256,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 23964
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 256,
          "cache_read_input_tokens": 20700,
          "cache_creation_input_tokens": 23964,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 23964,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T11:22:21.203Z_

<details><summary>↩ Tool result · `toolu_01GWNJBsWS6oWYf2Qmteqya5`</summary>

```text
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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3eca8ed7-3764-499b-9429-0178836f384e",
  "isSidechain": true,
  "promptId": "8ab46256-1dcf-4174-9343-f64005e6f2a2",
  "agentId": "a6f8fbc29078dceb8",
  "type": "user",
  "uuid": "6aa8974c-4e66-4824-9231-c467a485e4cf",
  "sourceToolAssistantUUID": "3eca8ed7-3764-499b-9429-0178836f384e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-18T11:22:22.848Z_

Let me examine the remaining files that use bootstrap logic:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6aa8974c-4e66-4824-9231-c467a485e4cf",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wuZBm6wqM5g7abEez9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f056d63a-6ced-4406-bf35-275b5d797274",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y67rZ6kUDEsmfSkYRvaJLH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 44664,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-18T11:22:23.024Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Bncf5Gonozx1w4ja7CSerX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/exp_E_paired_stats.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f056d63a-6ced-4406-bf35-275b5d797274",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wuZBm6wqM5g7abEez9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "225aa635-5d7f-4b55-a8df-b043aafdaa44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y67rZ6kUDEsmfSkYRvaJLH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 44664,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-18T11:22:23.029Z_

<details><summary>↩ Tool result · `toolu_01Bncf5Gonozx1w4ja7CSerX`</summary>

```text
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
55	    results = []
56	
57	    for s1, s2 in pairs:
58	        x = np.array(data[s1][metric])
59	        y = np.array(data[s2][metric])
60	        t_stat, p_val = stats.ttest_rel(x, y)
61	        d = cohens_d_paired(x, y)
62	        raw_ps.append(p_val)
63	        results.append({
64	            "pair": [s1, s2],
65	            "mean_diff": float(np.mean(x - y)),
66	            "t_stat": float(t_stat),
67	            "raw_p": float(p_val),
68	            "cohens_d": float(d),
69	        })
70	
71	    corrected = holm_bonferroni(raw_ps)
72	    for i, r in enumerate(results):
73	        r["corrected_p"] = float(corrected[i])
74	        r["significant"] = bool(corrected[i] < 0.05)
75	
76	    results.sort(key=lambda r: r["raw_p"])
77	    return results
78	
79	
80	def summarize(mmlu_res, hswag_res):
81	    sig_mmlu = [r for r in mmlu_res if r["significant"]]
82	    sig_hswag = [r for r in hswag_res if r["significant"]]
83	    lines = []
84	    lines.append(f"MMLU: {len(sig_mmlu)}/{len(mmlu_res)} pairs significant after Holm-Bonferroni correction.")
85	    lines.append(f"HellaSwag: {len(sig_hswag)}/{len(hswag_res)} pairs significant after Holm-Bonferroni correction.")
86	
87	    top_mmlu = sorted(mmlu_res, key=lambda r: abs(r["cohens_d"]), reverse=True)[:3]
88	    lines.append("Largest MMLU effect sizes: " + "; ".join(
89	        f"{r['pair'][0]} vs {r['pair'][1]} (d={r['cohens_d']:.2f}, p_corr={r['corrected_p']:.4f})"
90	        for r in top_mmlu
91	    ))
92	    top_hswag = sorted(hswag_res, key=lambda r: abs(r["cohens_d"]), reverse=True)[:3]
93	    lines.append("Largest HellaSwag effect sizes: " + "; ".join(
94	        f"{r['pair'][0]} vs {r['pair'][1]} (d={r['cohens_d']:.2f}, p_corr={r['corrected_p']:.4f})"
95	        for r in top_hswag
96	    ))
97	    return " ".join(lines)
98	
99	
100	def main():
101	    data = load_scores()
102	
103	    # Print per-strategy means for verification
104	    print("=== Per-strategy means ===")
105	    for strat in ALL_STRATEGIES:
106	        mmlu_mean = np.mean(data[strat]["mmlu"])
107	        hswag_mean = np.mean(data[strat]["hellaswag"])
108	        print(f"  {strat:25s}  MMLU={mmlu_mean:.4f}  HellaSwag={hswag_mean:.4f}")
109	
110	    # Main 6-strategy pairwise (C(6,2)=15 comparisons)
111	    mmlu_main = run_pairwise(data, "mmlu", MAIN_STRATEGIES)
112	    hswag_main = run_pairwise(data, "hellaswag", MAIN_STRATEGIES)
113	
114	    # All 10 strategies pairwise (C(10,2)=45 comparisons) for graduated alpha sweep
115	    mmlu_all = run_pairwise(data, "mmlu", ALL_STRATEGIES)
116	    hswag_all = run_pairwise(data, "hellaswag", ALL_STRATEGIES)
117	
118	    output = {
119	        "mmlu": {
120	            "pairwise_comparisons": mmlu_main,
121	            "correction_method": "Holm-Bonferroni",
122	            "n_comparisons": len(mmlu_main),
123	            "n_seeds": len(SEEDS),
124	            "alpha": 0.05,
125	        },
126	        "hellaswag": {
127	            "pairwise_comparisons": hswag_main,
128	            "correction_method": "Holm-Bonferroni",
129	            "n_comparisons": len(hswag_main),
130	            "n_seeds": len(SEEDS),
131	            "alpha": 0.05,
132	        },
133	        "per_seed_data": {
134	            strat: {
135	                "mmlu": data[strat]["mmlu"],
136	                "hellaswag": data[strat]["hellaswag"],
137	                "seeds": SEEDS,
138	            }
139	            for strat in ALL_STRATEGIES
140	        },
141	        "graduated_alpha_sweep": {
142	            "mmlu": {
143	                "pairwise_comparisons": [r for r in mmlu_all if any(
144	                    s.startswith("graduated") for s in r["pair"]
145	                )],
146	                "correction_method": "Holm-Bonferroni",
147	                "n_comparisons": len(mmlu_all),
148	            },
149	            "hellaswag": {
150	                "pairwise_comparisons": [r for r in hswag_all if any(
151	                    s.startswith("graduated") for s in r["pair"]
152	                )],
153	                "correction_method": "Holm-Bonferroni",
154	                "n_comparisons": len(hswag_all),
155	            },
156	        },
157	        "key_findings": summarize(mmlu_main, hswag_main),
158	    }
159	
160	    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
161	    with open(OUT_PATH, "w") as f:
162	        json.dump(output, f, indent=2)
163	    print(f"\nSaved to {OUT_PATH}")
164	
165	    # Print main comparison table
166	    print("\n=== MMLU Pairwise (6 main strategies, Holm-Bonferroni corrected) ===")
167	    print(f"{'Pair':50s} {'mean_diff':>10s} {'t':>8s} {'p_raw':>10s} {'p_corr':>10s} {'d':>8s} {'sig':>5s}")
168	    for r in mmlu_main:
169	        pair_str = f"{r['pair'][0]} vs {r['pair'][1]}"
170	        sig = "*" if r["significant"] else ""
171	        print(f"{pair_str:50s} {r['mean_diff']:>10.5f} {r['t_stat']:>8.3f} {r['raw_p']:>10.4f} {r['corrected_p']:>10.4f} {r['cohens_d']:>8.3f} {sig:>5s}")
172	
173	    print("\n=== HellaSwag Pairwise (6 main strategies, Holm-Bonferroni corrected) ===")
174	    print(f"{'Pair':50s} {'mean_diff':>10s} {'t':>8s} {'p_raw':>10s} {'p_corr':>10s} {'d':>8s} {'sig':>5s}")
175	    for r in hswag_main:
176	        pair_str = f"{r['pair'][0]} vs {r['pair'][1]}"
177	        sig = "*" if r["significant"] else ""
178	        print(f"{pair_str:50s} {r['mean_diff']:>10.5f} {r['t_stat']:>8.3f} {r['raw_p']:>10.4f} {r['corrected_p']:>10.4f} {r['cohens_d']:>8.3f} {sig:>5s}")
179	
180	
181	if __name__ == "__main__":
182	    main()
183	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "225aa635-5d7f-4b55-a8df-b043aafdaa44",
  "isSidechain": true,
  "promptId": "8ab46256-1dcf-4174-9343-f64005e6f2a2",
  "agentId": "a6f8fbc29078dceb8",
  "type": "user",
  "uuid": "d32a7606-003b-46d3-94ff-d15bda6a2c13",
  "sourceToolAssistantUUID": "225aa635-5d7f-4b55-a8df-b043aafdaa44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-18T11:22:23.448Z_

<details open><summary>🔧 Tool call — Read · `toolu_015HHHxkDFvDB12PV3bcoxq6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_exp009_dose_response.py",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d32a7606-003b-46d3-94ff-d15bda6a2c13",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wuZBm6wqM5g7abEez9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cb45b870-8df9-40ee-95b9-90691a07c69a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y67rZ6kUDEsmfSkYRvaJLH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 44664,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1404,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-18T11:22:23.460Z_

<details><summary>↩ Tool result · `toolu_015HHHxkDFvDB12PV3bcoxq6`</summary>

```text
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
56	    """Subsample a fixed-size dataset at the target synthetic injection ratio.
57	
58	    Samples without replacement from human (depth=0) and synthetic (depth>0)
59	    pools to construct a dataset where exactly ratio*total_n samples are synthetic.
60	    All strategies at the same (ratio, seed) see identical data for fair comparison.
61	    """
62	    rng = np.random.RandomState(seed)
63	
64	    human_idx = np.where(df["depth"].values == 0)[0]
65	    synthetic_idx = np.where(df["depth"].values > 0)[0]
66	
67	    n_synthetic = int(round(total_n * ratio))
68	    n_human = total_n - n_synthetic
69	
70	    if n_human > len(human_idx):
71	        raise ValueError(f"Need {n_human} human samples but only have {len(human_idx)}")
72	    if n_synthetic > len(synthetic_idx):
73	        raise ValueError(f"Need {n_synthetic} synthetic samples but only have {len(synthetic_idx)}")
74	
75	    sel_h = rng.choice(human_idx, size=n_human, replace=False)
76	    sel_s = rng.choice(synthetic_idx, size=n_synthetic, replace=False)
77	
78	    selected = np.concatenate([sel_h, sel_s])
79	    rng.shuffle(selected)
80	
81	    sub_df = df.iloc[selected].reset_index(drop=True)
82	    sub_texts = [texts[i] for i in selected]
83	    return sub_df, sub_texts
84	
85	
86	class TextDataset(Dataset):
87	    def __init__(self, texts, tokenizer, max_length=512):
88	        self.texts = texts
89	        self.tokenizer = tokenizer
90	        self.max_length = max_length
91	
92	    def __len__(self):
93	        return len(self.texts)
94	
95	    def __getitem__(self, idx):
96	        enc = self.tokenizer(
97	            self.texts[idx],
98	            truncation=True,
99	            max_length=self.max_length,
100	            padding=False,
101	            return_attention_mask=False,
102	        )
103	        return {"input_ids": enc["input_ids"]}
104	
105	
106	def make_weighted_trainer(weights_array):
107	    """Trainer subclass that uses WeightedRandomSampler when weights are non-uniform."""
108	    uniform = np.allclose(weights_array, 1.0)
109	
110	    class WeightedTrainer(Trainer):
111	        def get_train_dataloader(self):
112	            if uniform:
113	                return super().get_train_dataloader()
114	            sampler = WeightedRandomSampler(
115	                weights=weights_array.tolist(),
116	                num_samples=len(weights_array),
117	                replacement=True,
118	            )
119	            return DataLoader(
120	                self.train_dataset,
121	                batch_size=self.args.per_device_train_batch_size,
122	                sampler=sampler,
123	                collate_fn=self.data_collator,
124	                num_workers=self.args.dataloader_num_workers,
125	                pin_memory=self.args.dataloader_pin_memory,
126	            )
127	
128	    return WeightedTrainer
129	
130	
131	def train_one(model_name, texts, weights, output_dir, seed, args):
132	    """LoRA continued pretraining on weighted text data. Returns adapter path."""
133	    set_seed(seed)
134	    os.makedirs(output_dir, exist_ok=True)
135	
136	    tokenizer = AutoTokenizer.from_pretrained(
137	        model_name, cache_dir=args.cache_dir, trust_remote_code=True,
138	    )
139	    if tokenizer.pad_token is None:
140	        tokenizer.pad_token = tokenizer.eos_token
141	
142	    model = AutoModelForCausalLM.from_pretrained(
143	        model_name, cache_dir=args.cache_dir,
144	        torch_dtype=torch.bfloat16, trust_remote_code=True,
145	    )
146	
147	    lora_config = LoraConfig(
148	        task_type=TaskType.CAUSAL_LM,
149	        r=args.lora_rank,
150	        lora_alpha=args.lora_alpha,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb45b870-8df9-40ee-95b9-90691a07c69a",
  "isSidechain": true,
  "promptId": "8ab46256-1dcf-4174-9343-f64005e6f2a2",
  "agentId": "a6f8fbc29078dceb8",
  "type": "user",
  "uuid": "ca2ccf8a-146e-4b7d-b284-2e5814c6c7ab",
  "sourceToolAssistantUUID": "cb45b870-8df9-40ee-95b9-90691a07c69a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-18T11:22:23.680Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RS6JmicCcYadzvwfX7Abpw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/artifacts/exp006_filtering_strategies.py",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca2ccf8a-146e-4b7d-b284-2e5814c6c7ab",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wuZBm6wqM5g7abEez9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f7af3888-49a8-4d71-9415-b88e22103849",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y67rZ6kUDEsmfSkYRvaJLH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1404,
      "cache_read_input_tokens": 44664,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1404
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 288,
          "cache_read_input_tokens": 44664,
          "cache_creation_input_tokens": 1404,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1404,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-18T11:22:23.685Z_

<details><summary>↩ Tool result · `toolu_01RS6JmicCcYadzvwfX7Abpw`</summary>

```text
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
58	    Weight = 1 - P(synthetic). Hard mask at P(synthetic) < threshold.
59	    Uses same 15D features as Graduated for fair comparison (C3 claim).
60	    """
61	
62	    def __init__(self, threshold=0.5):
63	        self.threshold = threshold
64	        self.model = None
65	
66	    def fit(self, features, depths, texts=None):
67	        import lightgbm as lgb
68	        labels = (depths > 0).astype(int)
69	        self.model = lgb.LGBMClassifier(
70	            n_estimators=200, max_depth=6, learning_rate=0.05,
71	            subsample=0.8, colsample_bytree=0.8,
72	            random_state=42, verbose=-1,
73	        )
74	        self.model.fit(features, labels)
75	
76	    def get_weights(self, features, texts=None):
77	        return 1.0 - self.model.predict_proba(features)[:, 1]
78	
79	    def get_mask(self, features, texts=None, threshold=None):
80	        t = threshold if threshold is not None else self.threshold
81	        proba_syn = self.model.predict_proba(features)[:, 1]
82	        return proba_syn < t
83	
84	
85	class BinaryDrayson(FilterStrategy):
86	    """SIR (Drayson et al. 2025): w_j = (1-q(x_j))^b / Z, resample k*n."""
87	
88	    def __init__(self, b=1, k=1.5, seed=42):
89	        self.b = b
90	        self.k = k
91	        self.seed = seed
92	        self.model = None
93	
94	    def fit(self, features, depths, texts=None):
95	        import lightgbm as lgb
96	        labels = (depths > 0).astype(int)
97	        self.model = lgb.LGBMClassifier(
98	            n_estimators=200, max_depth=6, learning_rate=0.05,
99	            subsample=0.8, colsample_bytree=0.8,
100	            random_state=42, verbose=-1,
101	        )
102	        self.model.fit(features, labels)
103	
104	    def get_weights(self, features, texts=None):
105	        q = self.model.predict_proba(features)[:, 1]
106	        raw = (1.0 - q) ** self.b
107	        return raw / raw.max()
108	
109	    def get_mask(self, features, texts=None, threshold=None):
110	        q = self.model.predict_proba(features)[:, 1]
111	        raw = (1.0 - q) ** self.b
112	        prob = raw / raw.sum()
113	        rng = np.random.RandomState(self.seed)
114	        n = len(features)
115	        selected = rng.choice(n, size=int(self.k * n), replace=True, p=prob)
116	        mask = np.zeros(n, dtype=bool)
117	        mask[np.unique(selected)] = True
118	        return mask
119	
120	
121	class Graduated(FilterStrategy):
122	    """OBD-LightGBM: K-1 binary classifiers for P(depth>k), then exp(-alpha * E[depth])."""
123	
124	    def __init__(self, alpha=0.5, n_depths=6):
125	        self.alpha = alpha
126	        self.n_depths = n_depths
127	        self.models = []
128	
129	    def fit(self, features, depths, texts=None):
130	        import lightgbm as lgb
131	        self.models = []
132	        for k in range(self.n_depths - 1):
133	            labels = (depths > k).astype(int)
134	            clf = lgb.LGBMClassifier(
135	                n_estimators=200, max_depth=6, learning_rate=0.05,
136	                subsample=0.8, colsample_bytree=0.8,
137	                random_state=42, verbose=-1,
138	            )
139	            clf.fit(features, labels)
140	            self.models.append(clf)
141	
142	    def predict_depth_distribution(self, features):
143	        """(n_samples, n_depths) matrix of P(depth=d)."""
144	        n = len(features)
145	        cum = np.zeros((n, self.n_depths - 1))
146	        for k, model in enumerate(self.models):
147	            cum[:, k] = model.predict_proba(features)[:, 1]
148	
149	        dist = np.zeros((n, self.n_depths))
150	        dist[:, 0] = 1.0 - cum[:, 0]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7af3888-49a8-4d71-9415-b88e22103849",
  "isSidechain": true,
  "promptId": "8ab46256-1dcf-4174-9343-f64005e6f2a2",
  "agentId": "a6f8fbc29078dceb8",
  "type": "user",
  "uuid": "ea5f7e23-40fb-46e5-813d-29dd1e3d7b01",
  "sourceToolAssistantUUID": "f7af3888-49a8-4d71-9415-b88e22103849",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-18T11:22:24.913Z_

Let me check one more file for additional bootstrap context:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ea5f7e23-40fb-46e5-813d-29dd1e3d7b01",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wujwRCFbuHzSrdkXcm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4d499b17-797e-4400-b23c-7b82d0d00106",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018AZa4GCHw6tLQhXsVPpFaa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7346,
      "cache_read_input_tokens": 46068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7346,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T11:22:25.823Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BAiDLqajzR6R8sQXbBxPAD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/run_pipeline.py",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d499b17-797e-4400-b23c-7b82d0d00106",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wujwRCFbuHzSrdkXcm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e9d3394b-d2a5-40db-9098-0e788718fa66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018AZa4GCHw6tLQhXsVPpFaa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7346,
      "cache_read_input_tokens": 46068,
      "output_tokens": 117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7346
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 117,
          "cache_read_input_tokens": 46068,
          "cache_creation_input_tokens": 7346,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7346,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T11:22:25.847Z_

<details><summary>↩ Tool result · `toolu_01BAiDLqajzR6R8sQXbBxPAD`</summary>

```text
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
61	        return 0.0
62	    log_avg = sum(math.log(p) for p in precisions) / max_n
63	    bp = min(1.0, math.exp(1 - len(reference_tokens) / max(len(candidate_tokens), 1)))
64	    return bp * math.exp(log_avg)
65	
66	
67	# ===================================================================
68	# Step 2: Seed data preparation
69	# ===================================================================
70	
71	def prepare_seed_data(tokenizer, data_dir: Path, num_samples: int, max_tokens: int = 256):
72	    """Download C4 validation, truncate to max_tokens, save as depth_0.jsonl."""
73	    out_path = data_dir / "depth_0.jsonl"
74	    if out_path.exists() and sum(1 for _ in open(out_path)) >= num_samples:
75	        log.info("depth_0.jsonl already exists with enough samples — skipping")
76	        return
77	
78	    from datasets import load_dataset
79	
80	    # Use a single validation shard to avoid slow full-tree listing on proxied networks
81	    hf_endpoint = os.environ.get("HF_ENDPOINT", "https://huggingface.co")
82	    C4_SHARD_URL = f"{hf_endpoint}/datasets/allenai/c4/resolve/main/en/c4-validation.00000-of-00008.json.gz"
83	    log.info("Loading C4 validation shard (streaming) ...")
84	    try:
85	        ds = load_dataset("json", data_files=C4_SHARD_URL, split="train", streaming=True)
86	    except Exception as e:
87	        log.warning(f"Direct shard download failed ({e}), falling back to full dataset listing")
88	        ds = load_dataset("allenai/c4", "en", split="validation", streaming=True)
89	
90	    records = []
91	    for i, example in enumerate(tqdm(ds, total=num_samples, desc="Sampling C4")):
92	        if i >= num_samples:
93	            break
94	        text = example["text"].strip()
95	        if not text:
96	            continue
97	        ids = tokenizer.encode(text, add_special_tokens=False)[:max_tokens]
98	        truncated = tokenizer.decode(ids, skip_special_tokens=True)
99	        records.append({"text": truncated, "doc_id": len(records)})
100	        if len(records) >= num_samples:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9d3394b-d2a5-40db-9098-0e788718fa66",
  "isSidechain": true,
  "promptId": "8ab46256-1dcf-4174-9343-f64005e6f2a2",
  "agentId": "a6f8fbc29078dceb8",
  "type": "user",
  "uuid": "100b293b-b0c1-44ff-92d0-c00176275910",
  "sourceToolAssistantUUID": "e9d3394b-d2a5-40db-9098-0e788718fa66",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-18T11:22:37.330Z_

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
   - **Two Methods**:
     - `load_bootstrap_ci()`: Loads from bootstrap_ci.json with explicit ci_lower/ci_upper
     - `load_pairwise_auc_ci()`: Computes approximate CI from per-fold data using standard error (mean ± 1.96*SE)
   - Used for visualization of AUC decay curves with CI bands

**5. `/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scripts/draw_kstar_theta.py`** (Lines 78-111)
   - Loads bootstrap CI JSON files and extracts ci_lower bounds
   - Computes K*(theta) = max consecutive pairs with AUC >= theta threshold
   - Used for K* step function visualization

### Core Bootstrap Resampling Patterns

The project uses two main bootstrap approaches:

1. **Simple Resampling** (Lines 125-129 in exp_D_mcnemar.py):
   ```python
   rng = np.random.RandomState(seed)
   for i in range(n_boot):
       idx = rng.randint(0, n, size=n)  # or rng.choice(n, n, replace=True)
       # Compute statistic on resampled indices
   ```

2. **Percentile CI** (consistent across all files):
   ```python
   ci_lower = np.percentile(boot_statistics, 2.5)
   ci_upper = np.percentile(boot_statistics, 97.5)
   ```

### Bootstrap Parameters Across Files

- **N_BOOTSTRAP values**: 1,000 (exp_D_obd_n500_v2.py), 10,000 (exp_D_mcnemar.py, exp008), varies in visualization
- **Random Seed**: Typically 42 for reproducibility
- **CI Level**: 95% (2.5th and 97.5th percentiles)

### Output Formats

Bootstrap CI results are saved to JSON files with structures like:
- `{"pairs": {"0v1": {"ci_lower": X, "ci_upper": Y, "boot_mean": Z}, ...}}`
- `{"0v1": {"mean": X, "ci_95": [lower, upper]}, ...}`

All implementations use numpy's percentile method for CI computation, ensuring consistency across the project.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "100b293b-b0c1-44ff-92d0-c00176275910",
  "isSidechain": true,
  "agentId": "a6f8fbc29078dceb8",
  "requestId": "req_011Cb9wutzdeAgesX4bEf8uH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "76da91b8-b6eb-4f2e-8ff5-3fa3b5495b08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination",
  "sessionId": "0eb0119c-751b-4ee4-862f-7c124e4aa0a0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W9ah9LV8HyQxVKASJikS5E",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1481,
      "cache_read_input_tokens": 53414,
      "output_tokens": 1146,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1481
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1146,
          "cache_read_input_tokens": 53414,
          "cache_creation_input_tokens": 1481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1481,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
