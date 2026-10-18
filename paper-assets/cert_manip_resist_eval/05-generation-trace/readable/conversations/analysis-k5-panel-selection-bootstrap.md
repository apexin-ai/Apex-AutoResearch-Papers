# analysis k5 panel selection bootstrap

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/chats/worker_analysis_k5-panel-selection-bootstrap_20260523T061740.jsonl`
- **Structured JSON:** [`bd092e2ee52d9185985a.json`](../../sessions/bd/bd092e2ee52d9185985a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

45 recorded events

### Tool call

_source line 1 · 2026-05-23T06:23:53.786578+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__read_project_file",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T06:23:53.786915+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T06:23:53.787081+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat /root/cert_manip_resist_eval/scripts/run_k5_panel_selection.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cat /root/cert_manip_resist_eval/scripts/run_k5_panel_selection.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T06:23:53.787370+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"K=5 Panel Selection Strategy Comparison.\\n\\nFor each of 12 conditions (2 datasets × 6 attacks), enumerate all C(15,5)=3003\\npanels, compute panel ASR / K_eff / η_max, then compare 4 selection strategies:\\n  - min(η_max): select panel with lowest max individual ASR\\n  - max(K_eff): select panel with highest K_eff\\n  - min(K_eff): select panel with lowest K_eff\\n  - random: average over 100 random panels\\n\\n\\\"Best\\\" = lowest panel ASR.\\n\\\"\\\"\\\"\\n\\nimport sys\\nsys.path.insert(0, \\\"/root/cert_manip_resist_eval\\\")\\n\\nimport json\\nimport itertools\\nimport numpy as np\\nfrom pathlib import Path\\n\\nfrom src.unified_data_loader import (\\n    ALL_MODELS, DATASETS, ATTACKS,\\n    load_all_scores, load_pairs, load_mi_data, _is_valid_score,\\n)\\n\\n\\ndef majority_vote(votes):\\n    counts = {\\\"A\\\": 0, \\\"B\\\": 0, \\\"tie\\\": 0}\\n    for v in votes:\\n        counts[v] = counts.get(v, 0) + 1\\n    mc = max(counts.values())\\n    winners = [k for k, c in counts.items() if c == mc]\\n    if len(winners) == 1:\\n        return winners[0]\\n    for w in winners:\\n        if w != \\\"tie\\\":\\n            return w\\n    return \\\"tie\\\"\\n\\n\\ndef compute_individual_asr(clean_list, attacked_list, pairs):\\n    n = min(len(clean_list), len(attacked_list), len(pairs))\\n    n_flips = n_correct = 0\\n    for i in range(n):\\n        if not _is_valid_score(clean_list[i]) or not _is_valid_score(attacked_list[i]):\\n            continue\\n        gt = pairs[i][\\\"ground_truth_winner\\\"]\\n        if clean_list[i][\\\"winner\\\"] == gt:\\n            n_correct += 1\\n            if attacked_list[i][\\\"winner\\\"] != gt:\\n                n_flips += 1\\n    return n_flips / max(n_correct, 1)\\n\\n\\ndef compute_panel_asr(jids, clean_ds, attacked_ds_atk, ds_pairs):\\n    n = min(len(ds_pairs), *(len(clean_ds[j]) for j in jids),\\n            *(len(atta
…[truncated 7426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T06:23:53.787577+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "head -50 /root/cert_manip_resist_eval/src/unified_data_loader.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "head -50 /root/cert_manip_resist_eval/src/unified_data_loader.py"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T06:23:53.787790+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Unified data loader for 15-model cert_manip_resist_eval pipeline.\\n\\nHandles two data formats:\\n  - Checkpoint files (local 6 models): nested {clean_scores: {ds: {model: [...]}}}\\n  - Individual JSON files (API 9 models): flat {scores: [...], asr, accuracy, ...}\\n\\\"\\\"\\\"\\n\\nimport json\\nimport logging\\nfrom pathlib import Path\\n\\nlogger = logging.getLogger(__name__)\\n\\n# ── Model lists ──────────────────────────────────────────────────────\\nLOCAL_MODELS = [\\n    \\\"qwen2.5-72b\\\", \\\"llama3.1-70b\\\", \\\"mistral-large\\\",\\n    \\\"qwen2.5-32b\\\", \\\"qwen2.5-14b\\\", \\\"llama3.1-8b\\\",\\n]\\nAPI_MODELS = [\\n    \\\"claude-opus-4-6\\\", \\\"gpt-5.5\\\", \\\"gemini-3.1-pro-preview\\\", \\\"gpt-4.1\\\",\\n    \\\"claude-sonnet-4-6\\\", \\\"gpt-4.1-nano\\\", \\\"gemini-3.5-flash\\\",\\n    \\\"gpt-4.1-mini\\\", \\\"claude-3-haiku\\\",\\n]\\nALL_MODELS = LOCAL_MODELS + API_MODELS\\nDATASETS = [\\\"mmlu\\\", \\\"arc_challenge\\\"]\\nATTACKS = [\\n    \\\"prompt_injection\\\", \\\"sycophancy\\\", \\\"score_manipulation\\\",\\n    \\\"verbosity_bias\\\", \\\"position_bias\\\", \\\"authority_bias\\\",\\n]\\n\\n# ── Default paths ────────────────────────────────────────────────────\\nRESULTS_DIR = Path(\\\"/root/cert_manip_resist_eval/artifacts/results\\\")\\nPLAN001_DIR = RESULTS_DIR / \\\"plan001\\\"\\nSCORES_DIR = PLAN001_DIR / \\\"individual_scores\\\"\\nMI_PATH = PLAN001_DIR / \\\"mi_matrix\\\" / \\\"mi_matrix_15models.json\\\"\\nCKPT_FILES = [\\n    RESULTS_DIR / \\\"_taxonomy_checkpoint.json\\\",\\n    RESULTS_DIR / \\\"_step2v3_checkpoint.json\\\",\\n]\\nOUTPUT_DIR = PLAN001_DIR / \\\"panel_regression\\\"\\n\\n\\ndef _invert_winners(scores):\\n    swap = {\\\"A\\\": \\\"B\\\", \\\"B\\\": \\\"A\\\", \\\"tie\\\": \\\"tie\\\"}\\n    return [{**s, \\\"winner\\\": swap.get(s.get(\\\"winner\\\", \\\"tie\\\"), \\\"tie\\\")} for s in scores]\\n\\n\\ndef l
…[truncated 151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T06:23:53.787954+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "python3 -c \"import json; d=json.load(open('/root/cert_manip_resist_eval/artifacts/results/plan001/k5_panel_selection.json')); print(json.dumps(d['per_condition'][0], indent=2))\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "python3 -c \"import json; d=json.load(open('/root/cert_manip_resist_eval/artifacts/results/plan001/k5_panel_selection.json')); print(json.dumps(d['per_condition'][0], indent=2))\""
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T06:23:53.788085+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T06:23:53.788205+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "python3 -c \"import json; d=json.load(open('/root/cert_manip_resist_eval/artifacts/results/plan001/k5_panel_selection.json')); print(json.dumps(d['per_condition'][0], indent=2))\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "python3 -c \"import json; d=json.load(open('/root/cert_manip_resist_eval/artifacts/results/plan001/k5_panel_selection.json')); print(json.dumps(d['per_condition'][0], indent=2))\""
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T06:23:53.788338+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'python3 -c \\\"import json; d=json.load(open(\\\\'/root/cert_manip_resist_eval/artifacts/results/plan001/k5_panel_selection.json\\\\')); print(json.dumps(d[\\\\'per_condition\\\\'][0], indent=2))\\\"'\\n\\nExit code: 127\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nbash: line 1: python3: command not found\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T06:23:53.788459+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "head -100 /root/cert_manip_resist_eval/artifacts/results/plan001/k5_panel_selection.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "head -100 /root/cert_manip_resist_eval/artifacts/results/plan001/k5_panel_selection.json"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-23T06:23:53.788575+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "ls /root/miniconda3/bin/python3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "ls /root/miniconda3/bin/python3"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-23T06:23:53.788783+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"panel_size\\\": 5,\\n  \\\"n_models\\\": 15,\\n  \\\"n_total_panels\\\": 3003,\\n  \\\"n_random_samples\\\": 100,\\n  \\\"per_condition\\\": [\\n    {\\n      \\\"condition\\\": \\\"mmlu×prompt_injection\\\",\\n      \\\"n_valid_panels\\\": 3003,\\n      \\\"min_eta_max\\\": {\\n        \\\"panel\\\": [\\n          \\\"claude-opus-4-6\\\",\\n          \\\"gpt-5.5\\\",\\n          \\\"gemini-3.1-pro-preview\\\",\\n          \\\"gpt-4.1\\\",\\n          \\\"gemini-3.5-flash\\\"\\n        ],\\n        \\\"asr\\\": 0.0,\\n        \\\"eta_max\\\": 0.018726591760299626,\\n        \\\"keff\\\": 2.262318849883708\\n      },\\n      \\\"max_keff\\\": {\\n        \\\"panel\\\": [\\n          \\\"qwen2.5-14b\\\",\\n          \\\"llama3.1-8b\\\",\\n          \\\"gpt-4.1-nano\\\",\\n          \\\"gpt-4.1-mini\\\",\\n          \\\"claude-3-haiku\\\"\\n        ],\\n        \\\"asr\\\": 0.4329004329004329,\\n        \\\"eta_max\\\": 0.8173913043478261,\\n        \\\"keff\\\": 4.41469390032275\\n      },\\n      \\\"min_keff\\\": {\\n        \\\"panel\\\": [\\n          \\\"claude-opus-4-6\\\",\\n          \\\"gpt-5.5\\\",\\n          \\\"gemini-3.1-pro-preview\\\",\\n          \\\"gpt-4.1\\\",\\n          \\\"gemini-3.5-flash\\\"\\n        ],\\n        \\\"asr\\\": 0.0,\\n        \\\"eta_max\\\": 0.018726591760299626,\\n        \\\"keff\\\": 2.262318849883708\\n      },\\n      \\\"random_mean\\\": {\\n        \\\"asr_mean\\\": 0.14981798811289132,\\n        \\\"asr_std\\\": 0.1136123038169051\\n      },\\n      \\\"optimal\\\": {\\n        \\\"panel\\\": [\\n          \\\"qwen2.5-72b\\\",\\n          \\\"llama3.1-70b\\\",\\n          \\\"gpt-5.5\\\",\\n          \\\"gemini-3.1-pro-preview\\\",\\n          \\\"gemini-3.5-flash\\\"\\n        ],\\n        \\\"asr\\\": 0.0,\\n        \\\"eta_max\\\": 0.4098360655737705,\\n        \\\"keff\\\": 2.7130269750222737\\n      },\\n      \\\"winner\\\": \\\"tie\\\"\\n    },\\n
…[truncated 1281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T06:23:53.788942+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/bin/python3\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T06:23:53.789167+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat > /root/cert_manip_resist_eval/scripts/run_k5_panel_selection_bootstrap.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"K=5 Panel Selection Bootstrap Confidence Intervals.\n\nTwo types of bootstrap:\n1. Sample-level: resample 300 samples with replacement to get CI on each strategy's ASR\n2. Strategy-level: resample from 3003 panels to simulate panel pool uncertainty\n\nPairwise comparisons test whether ASR differences are significant.\n\"\"\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nfrom pathlib import Path\n\nfrom src.unified_data_loader import (\n    ALL_MODELS, DATASETS, ATTACKS,\n    load_all_scores, load_pairs, load_mi_data, _is_valid_score,\n)\n\n\nB = 9999\nK = 5\nALPHA = 0.05\n\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef get_sample_outcomes(jids, clean_ds, attacked_ds_atk, ds_pairs):\n    \"\"\"Return per-sample binary outcomes: 1=flip, 0=correct-no-flip, NaN=invalid/wrong-clean.\"\"\"\n    n = min(len(ds_pairs), *(len(clean_ds[j]) for j in jids),\n            *(len(attacked_ds_atk[j]) for j in jids))\n    outcomes = []\n    for i in range(n):\n        any_invalid = False\n        for j in jids:\n            if not _is_valid_score(clean_ds[j][i]) or not _is_valid_score(attacked_ds_atk[j][i]):\n                any_invalid = True\n                break\n        if any_invalid:\n            outcomes.append(np.nan)\n            continue\n        gt = ds_pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean_ds[j][i][\"winner\"] for j in jids])\n        if cv != gt:\n            outcomes.append(np.nan)  # clean was wrong, not in denominator\n            continue\n        av = majority_vote([attacked_ds_atk[j][i][\"winner\"] for j in jids])\n        outcomes.append(1.0 if av != gt else 0.0)\n    return np.array(outcomes)\n\n\ndef asr_from_outcomes(outcomes):\n    valid = outcomes[~np.isnan(outcomes)]\n    if len(valid) == 0:\n        return np.nan\n    return np.mean(valid)\n\n\ndef bootstrap_asr(outcomes, rng):\n    \"\"\"Bootstrap resample outcomes B times, return ASR distribution.\"\"\"\n    valid_mask = ~np.isnan(outcomes)\n    valid = outcomes[valid_mask]\n    n_valid = len(valid)\n    if n_valid == 0:\n        return np.full(B, np.nan)\n    idx = rng.integers(0, n_valid, size=(B, n_valid))\n    resampled = valid[idx]\n    return np.mean(resampled, axis=1)\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        if not _is_valid_score(clean_list[i]) or not _is_valid_score(attacked_list[i]):\n            continue\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i][\"winner\"] == gt:\n            n_correct += 1\n            if attacked_list[i][\"winner\"] != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef mi_based_keff(mi_matrix, model_indices):\n    K = len(model_indices)\n    if K <= 1:\n        return 1.0\n    keff = 0.0\n    for i_idx in model_indices:\n        term = 1.0\n        for j_idx in model_indices:\n            if i_idx != j_idx:\n                term += np.exp(-2 * mi_matrix[i_idx, j_idx])\n        keff += term\n    return keff / K\n\n\ndef compute_panel_asr_fast(jids, clean_ds, attacked_ds_atk, ds_pairs):\n    outcomes = get_sample_outcomes(jids, clean_ds, attacked_ds_atk, ds_pairs)\n    return asr_from_outcomes(outcomes)\n\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\ndef main():\n    print(\"Loading data...\")\n    mi_data = load_mi_data()\n    mi_matrices_raw = mi_data[\"mi_matrix\"]\n    pairs = load_pairs()\n    clean, attacked = load_all_scores()\n    mi_matrices = {ds: np.array(mi_matrices_raw[ds]) for ds in DATASETS}\n\n    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), K))\n    print(f\"C(15,5) = {len(all_combos)} panels\")\n\n    rng = np.random.default_rng(42)\n\n    per_condition = []\n    sig_counts = {\n        \"min_eta_vs_random\": 0,\n        \"min_keff_vs_random\": 0,\n        \"min_eta_vs_max_keff\": 0,\n    }\n    n_conditions = 0\n\n    for ds in DATASETS:\n        ds_pairs = pairs[ds]\n        mi_mat = mi_matrices[ds]\n\n        for atk in ATTACKS:\n            cond = f\"{ds}×{atk}\"\n            n_conditions += 1\n            print(f\"\\n{'='*60}\")\n            print(f\"Condition {n_conditions}/12: {cond}\")\n            print(f\"{'='*60}\")\n\n            # Individual ASRs per model\n            ind_asrs = {}\n            for j, m in enumerate(ALL_MODELS):\n                ind_asrs[j] = compute_individual_asr(\n                    clean[ds][m], attacked[ds][atk][m], ds_pairs\n                )\n\n            # ── Enumerate all panels, find strategy-selected panels ──\n            best_eta = {\"eta_max\": float(\"inf\"), \"idx\": None, \"jids\": None}\n            best_max_keff = {\"keff\": -float(\"inf\"), \"idx\": None, \"jids\": None}\n            best_min_keff = {\"keff\": float(\"inf\"), \"idx\": None, \"jids\": None}\n\n            panel_data = []  # for strategy-level bootstrap\n            for ci, combo in enumerate(all_combos):\n                jids = list(combo)\n                eta_max = max(ind_asrs[j] for j in jids)\n                keff = mi_based_keff(mi_mat, jids)\n                panel_data.append({\"jids\": jids, \"eta_max\": eta_max, \"keff\": keff})\n\n                if eta_max < best_eta[\"eta_max\"] or (\n                    eta_max == best_eta[\"eta_max\"] and keff > best_eta.get(\"keff_val\", -1)\n                ):\n                    best_eta = {\"eta_max\": eta_max, \"idx\": ci, \"jids\": jids, \"keff_val\": keff}\n                if keff > best_max_keff[\"keff\"]:\n                    best_max_keff = {\"keff\": keff, \"idx\": ci, \"jids\": jids}\n                if keff < best_min_keff[\"keff\"]:\n                    best_min_keff = {\"keff\": keff, \"idx\": ci, \"jids\": jids}\n\n            strategies = {\n                \"min_eta_max\": best_eta[\"jids\"],\n                \"min_keff\": best_min_keff[\"jids\"],\n                \"max_keff\": best_max_keff[\"jids\"],\n            }\n\n            # Random: sample 100 panels for baseline\n            rand_indices = rng.choice(len(all_combos), size=100, replace=False)\n\n            # ── Sample-level bootstrap for each strategy ──\n            print(\"  Sample-level bootstrap...\")\n            strat_outcomes = {}\n            strat_boot = {}\n            for sname, jids in strategies.items():\n                outcomes = get_sample_outcomes(jids, clean[ds], attacked[ds][atk], ds_pairs)\n                strat_outcomes[sname] = outcomes\n                strat_boot[sname] = bootstrap_asr(outcomes, rng)\n\n            # Random: average over 100 panels, bootstrap each\n            rand_outcomes_list = []\n            for ri in rand_indices:\n                jids = list(all_combos[ri])\n                outcomes = get_sample_outcomes(jids, clean[ds], attacked[ds][atk], ds_pairs)\n                rand_outcomes_list.append(outcomes)\n\n            # For random strategy, bootstrap: for each bootstrap iteration,\n            # resample samples for each of 100 panels, average ASRs\n            print(\"  Random strategy bootstrap...\")\n            rand_boot_asrs = np.zeros(B)\n            for outcomes in rand_outcomes_list:\n                rand_boot_asrs += bootstrap_asr(outcomes, rng)\n            rand_boot_asrs /= len(rand_outcomes_list)\n            strat_boot[\"random\"] = rand_boot_asrs\n\n            rand_asr_mean = np.mean([asr_from_outcomes(o) for o in rand_outcomes_list])\n            strat_outcomes[\"random_mean\"] = rand_asr_mean\n\n            # ── Strategy-level bootstrap ──\n            print(\"  Strategy-level bootstrap...\")\n            strat_level_boot = {\"min_eta_max\": [], \"min_keff\": [], \"max_keff\": []}\n            n_panels = len(all_combos)\n            for b in range(B):\n                boot_idx = rng.integers(0, n_panels, size=n_panels)\n                b_best_eta = float(\"inf\")\n                b_best_eta_jids = None\n                b_best_eta_keff = -1\n                b_max_keff = -float(\"inf\")\n                b_max_keff_jids = None\n                b_min_keff = float(\"inf\")\n                b_min_keff_jids = None\n\n                for bi in boot_idx:\n                    pd = panel_data[bi]\n                    if pd[\"eta_max\"] < b_best_eta or (\n                        pd[\"eta_max\"] == b_best_eta and pd[\"keff\"] > b_best_eta_keff\n                    ):\n                        b_best_eta = pd[\"eta_max\"]\n                        b_best_eta_jids = pd[\"jids\"]\n                        b_best_eta_keff = pd[\"keff\"]\n                    if pd[\"keff\"] > b_max_keff:\n                        b_max_keff = pd[\"keff\"]\n                        b_max_keff_jids = pd[\"jids\"]\n                    if pd[\"keff\"] < b_min_keff:\n                        b_min_keff = pd[\"keff\"]\n                        b_min_keff_jids = pd[\"jids\"]\n\n                for sname, jids in [(\"min_eta_max\", b_best_eta_jids),\n                                     (\"min_keff\", b_min_keff_jids),\n                                     (\"max_keff\", b_max_keff_jids)]:\n                    asr = compute_panel_asr_fast(jids, clean[ds], attacked[ds][atk], ds_pairs)\n                    strat_level_boot[sname].append(asr)\n\n            strat_level_boot = {k: np.array(v) for k, v in strat_level_boot.items()}\n\n            # ── Compute CIs and pairwise tests ──\n            def ci95(arr):\n                arr = arr[~np.isnan(arr)]\n                if len(arr) == 0:\n                    return [None, None]\n                return [float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5))]\n\n            cond_result = {\n                \"condition\": cond,\n            }\n\n            for sname in [\"min_eta_max\", \"min_keff\", \"max_keff\"]:\n                jids = strategies[sname]\n                asr_val = asr_from_outcomes(strat_outcomes[sname])\n                cond_result[sname] = {\n                    \"panel\": [ALL_MODELS[j] for j in jids],\n                    \"asr\": float(asr_val) if not np.isnan(asr_val) else None,\n                    \"sample_bootstrap_ci_95\": ci95(strat_boot[sname]),\n                    \"strategy_bootstrap_ci_95\": ci95(strat_level_boot[sname]),\n                    \"strategy_bootstrap_mean\": float(np.nanmean(strat_level_boot[sname])),\n                }\n\n            cond_result[\"random\"] = {\n                \"asr_mean\": float(rand_asr_mean),\n                \"sample_bootstrap_ci_95\": ci95(rand_boot_asrs),\n            }\n\n            # Pairwise\n            pairwise = {}\n            pairs_to_test = [\n                (\"min_eta_vs_random\", \"min_eta_max\", \"random\"),\n                (\"min_keff_vs_random\", \"min_keff\", \"random\"),\n                (\"min_eta_vs_max_keff\", \"min_eta_max\", \"max_keff\"),\n            ]\n            for pname, s1, s2 in pairs_to_test:\n                b1 = strat_boot[s1]\n                b2 = strat_boot[s2]\n                delta_boot = b1 - b2\n                delta_obs = (\n                    (asr_from_outcomes(strat_outcomes[s1]) if s1 != \"random\" else rand_asr_mean)\n                    - (asr_from_outcomes(strat_outcomes[s2]) if s2 != \"random\" else rand_asr_mean)\n                )\n                lo, hi = ci95(delta_boot)\n                significant = (lo is not None and hi is not None and\n                               not (lo <= 0 <= hi))\n                pairwise[pname] = {\n                    \"delta\": float(delta_obs) if not np.isnan(delta_obs) else None,\n                    \"ci_95\": [lo, hi],\n                    \"significant\": significant,\n                }\n                if significant:\n                    sig_counts[pname] += 1\n\n            cond_result[\"pairwise\"] = pairwise\n\n            # Print summary\n            print(f\"  min(η_max): ASR={cond_result['min_eta_max']['asr']:.4f}  \"\n                  f\"CI={cond_result['min_eta_max']['sample_bootstrap_ci_95']}\")\n            print(f\"  min(K_eff): ASR={cond_result['min_keff']['asr']:.4f}  \"\n                  f\"CI={cond_result['min_keff']['sample_bootstrap_ci_95']}\")\n            print(f\"  random:     ASR={cond_result['random']['asr_mean']:.4f}  \"\n                  f\"CI={cond_result['random']['sample_bootstrap_ci_95']}\")\n            print(f\"  max(K_eff): ASR={cond_result['max_keff']['asr']:.4f}  \"\n                  f\"CI={cond_result['max_keff']['sample_bootstrap_ci_95']}\")\n            for pname, pdata in pairwise.items():\n                sig_str = \"***SIG***\" if pdata[\"significant\"] else \"n.s.\"\n                print(f\"  {pname}: Δ={pdata['delta']:.4f}  CI={pdata['ci_95']}  {sig_str}\")\n\n            per_condition.append(cond_result)\n\n    # Summary\n    output = {\n        \"panel_size\": K,\n        \"n_bootstrap\": B,\n        \"n_models\": len(ALL_MODELS),\n        \"n_total_panels\": len(all_combos),\n        \"per_condition\": per_condition,\n        \"summary\": {\n            \"n_conditions\": n_conditions,\n            \"min_eta_vs_random_sig\": f\"{sig_counts['min_eta_vs_random']}/{n_conditions}\",\n            \"min_keff_vs_random_sig\": f\"{sig_counts['min_keff_vs_random']}/{n_conditions}\",\n            \"min_eta_vs_max_keff_sig\": f\"{sig_counts['min_eta_vs_max_keff']}/{n_conditions}\",\n        },\n    }\n\n    print(f\"\\n{'='*60}\")\n    print(\"SUMMARY\")\n    print(f\"{'='*60}\")\n    for k, v in output[\"summary\"].items():\n        print(f\"  {k}: {v}\")\n\n    out_dir = Path(\"/root/cert_manip_resist_eval/artifacts/results/plan001\")\n    out_dir.mkdir(parents=True, exist_ok=True)\n    out_path = out_dir / \"k5_panel_selection_bootstrap.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    print(f\"\\nSaved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cat > /root/cert_manip_resist_eval/scripts/run_k5_panel_selection_bootstrap.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"K=5 Panel Selection Bootstrap Confidence Intervals.\n\nTwo types of bootstrap:\n1. Sample-level: resample 300 samples with replacement to get CI on each strategy's ASR\n2. Strategy-level: resample from 3003 panels to simulate panel pool uncertainty\n\nPairwise comparisons test whether ASR differences are significant.\n\"\"\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nfrom pathlib import Path\n\nfrom src.unified_data_loader import (\n    ALL_MODELS, DATASETS, ATTACKS,\n    load_all_scores, load_pairs, load_mi_data, _is_valid_score,\n)\n\n\nB = 9999\nK = 5\nALPHA = 0.05\n\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef get_sample_outcomes(jids, clean_ds, attacked_ds_atk, ds_pairs):\n    \"\"\"Return per-sample binary outcomes: 1=flip, 0=correct-no-flip, NaN=invalid/wrong-clean.\"\"\"\n    n = min(len(ds_pairs), *(len(clean_ds[j]) for j in jids),\n            *(len(attacked_ds_atk[j]) for j in jids))\n    outcomes = []\n    for i in range(n):\n        any_invalid = False\n        for j in jids:\n            if not _is_valid_score(clean_ds[j][i]) or not _is_valid_score(attacked_ds_atk[j][i]):\n                any_invalid = True\n                break\n        if any_invalid:\n            outcomes.append(np.nan)\n            continue\n        gt = ds_pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean_ds[j][i][\"winner\"] for j in jids])\n        if cv != gt:\n            outcomes.append(np.nan)  # clean was wrong, not in denominator\n            continue\n        av = majority_vote([attacked_ds_atk[j][i][\"winner\"] for j in jids])\n        outcomes.append(1.0 if av != gt else 0.0)\n    return np.array(outcomes)\n\n\ndef asr_from_outcomes(outcomes):\n    valid = outcomes[~np.isnan(outcomes)]\n    if len(valid) == 0:\n        return np.nan\n    return np.mean(valid)\n\n\ndef bootstrap_asr(outcomes, rng):\n    \"\"\"Bootstrap resample outcomes B times, return ASR distribution.\"\"\"\n    valid_mask = ~np.isnan(outcomes)\n    valid = outcomes[valid_mask]\n    n_valid = len(valid)\n    if n_valid == 0:\n        return np.full(B, np.nan)\n    idx = rng.integers(0, n_valid, size=(B, n_valid))\n    resampled = valid[idx]\n    return np.mean(resampled, axis=1)\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        if not _is_valid_score(clean_list[i]) or not _is_valid_score(attacked_list[i]):\n            continue\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i][\"winner\"] == gt:\n            n_correct += 1\n            if attacked_list[i][\"winner\"] != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef mi_based_keff(mi_matrix, model_indices):\n    K = len(model_indices)\n    if K <= 1:\n        return 1.0\n    keff = 0.0\n    for i_idx in model_indices:\n        term = 1.0\n        for j_idx in model_indices:\n            if i_idx != j_idx:\n                term += np.exp(-2 * mi_matrix[i_idx, j_idx])\n        keff += term\n    return keff / K\n\n\ndef compute_panel_asr_fast(jids, clean_ds, attacked_ds_atk, ds_pairs):\n    outcomes = get_sample_outcomes(jids, clean_ds, attacked_ds_atk, ds_pairs)\n    return asr_from_outcomes(outcomes)\n\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\ndef main():\n    print(\"Loading data...\")\n    mi_data = load_mi_data()\n    mi_matrices_raw = mi_data[\"mi_matrix\"]\n    pairs = load_pairs()\n    clean, attacked = load_all_scores()\n    mi_matrices = {ds: np.array(mi_matrices_raw[ds]) for ds in DATASETS}\n\n    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), K))\n    print(f\"C(15,5) = {len(all_combos)} panels\")\n\n    rng = np.random.default_rng(42)\n\n    per_condition = []\n    sig_counts = {\n        \"min_eta_vs_random\": 0,\n        \"min_keff_vs_random\": 0,\n        \"min_eta_vs_max_keff\": 0,\n    }\n    n_conditions = 0\n\n    for ds in DATASETS:\n        ds_pairs = pairs[ds]\n        mi_mat = mi_matrices[ds]\n\n        for atk in ATTACKS:\n            cond = f\"{ds}×{atk}\"\n            n_conditions += 1\n            print(f\"\\n{'='*60}\")\n            print(f\"Condition {n_conditions}/12: {cond}\")\n            print(f\"{'='*60}\")\n\n            # Individual ASRs per model\n            ind_asrs = {}\n            for j, m in enumerate(ALL_MODELS):\n                ind_asrs[j] = compute_individual_asr(\n                    clean[ds][m], attacked[ds][atk][m], ds_pairs\n                )\n\n            # ── Enumerate all panels, find strategy-selected panels ──\n            best_eta = {\"eta_max\": float(\"inf\"), \"idx\": None, \"jids\": None}\n            best_max_keff = {\"keff\": -float(\"inf\"), \"idx\": None, \"jids\": None}\n            best_min_keff = {\"keff\": float(\"inf\"), \"idx\": None, \"jids\": None}\n\n            panel_data = []  # for strategy-level bootstrap\n            for ci, combo in enumerate(all_combos):\n                jids = list(combo)\n                eta_max = max(ind_asrs[j] for j in jids)\n                keff = mi_based_keff(mi_mat, jids)\n                panel_data.append({\"jids\": jids, \"eta_max\": eta_max, \"keff\": keff})\n\n                if eta_max < best_eta[\"eta_max\"] or (\n                    eta_max == best_eta[\"eta_max\"] and keff > best_eta.get(\"keff_val\", -1)\n                ):\n                    best_eta = {\"eta_max\": eta_max, \"idx\": ci, \"jids\": jids, \"keff_val\": keff}\n                if keff > best_max_keff[\"keff\"]:\n                    best_max_keff = {\"keff\": keff, \"idx\": ci, \"jids\": jids}\n                if keff < best_min_keff[\"keff\"]:\n                    best_min_keff = {\"keff\": keff, \"idx\": ci, \"jids\": jids}\n\n            strategies = {\n                \"min_eta_max\": best_eta[\"jids\"],\n                \"min_keff\": best_min_keff[\"jids\"],\n                \"max_keff\": best_max_keff[\"jids\"],\n            }\n\n            # Random: sample 100 panels for baseline\n            rand_indices = rng.choice(len(all_combos), size=100, replace=False)\n\n            # ── Sample-level bootstrap for each strategy ──\n            print(\"  Sample-level bootstrap...\")\n            strat_outcomes = {}\n            strat_boot = {}\n            for sname, jids in strategies.items():\n                outcomes = get_sample_outcomes(jids, clean[ds], attacked[ds][atk], ds_pairs)\n                strat_outcomes[sname] = outcomes\n                strat_boot[sname] = bootstrap_asr(outcomes, rng)\n\n            # Random: average over 100 panels, bootstrap each\n            rand_outcomes_list = []\n            for ri in rand_indices:\n                jids = list(all_combos[ri])\n                outcomes = get_sample_outcomes(jids, clean[ds], attacked[ds][atk], ds_pairs)\n                rand_outcomes_list.append(outcomes)\n\n            # For random strategy, bootstrap: for each bootstrap iteration,\n            # resample samples for each of 100 panels, average ASRs\n            print(\"  Random strategy bootstrap...\")\n            rand_boot_asrs = np.zeros(B)\n            for outcomes in rand_outcomes_list:\n                rand_boot_asrs += bootstrap_asr(outcomes, rng)\n            rand_boot_asrs /= len(rand_outcomes_list)\n            strat_boot[\"random\"] = rand_boot_asrs\n\n            rand_asr_mean = np.mean([asr_from_outcomes(o) for o in rand_outcomes_list])\n            strat_outcomes[\"random_mean\"] = rand_asr_mean\n\n            # ── Strategy-level bootstrap ──\n            print(\"  Strategy-level bootstrap...\")\n            strat_level_boot = {\"min_eta_max\": [], \"min_keff\": [], \"max_keff\": []}\n            n_panels = len(all_combos)\n            for b in range(B):\n                boot_idx = rng.integers(0, n_panels, size=n_panels)\n                b_best_eta = float(\"inf\")\n                b_best_eta_jids = None\n                b_best_eta_keff = -1\n                b_max_keff = -float(\"inf\")\n                b_max_keff_jids = None\n                b_min_keff = float(\"inf\")\n                b_min_keff_jids = None\n\n                for bi in boot_idx:\n                    pd = panel_data[bi]\n                    if pd[\"eta_max\"] < b_best_eta or (\n                        pd[\"eta_max\"] == b_best_eta and pd[\"keff\"] > b_best_eta_keff\n                    ):\n                        b_best_eta = pd[\"eta_max\"]\n                        b_best_eta_jids = pd[\"jids\"]\n                        b_best_eta_keff = pd[\"keff\"]\n                    if pd[\"keff\"] > b_max_keff:\n                        b_max_keff = pd[\"keff\"]\n                        b_max_keff_jids = pd[\"jids\"]\n                    if pd[\"keff\"] < b_min_keff:\n                        b_min_keff = pd[\"keff\"]\n                        b_min_keff_jids = pd[\"jids\"]\n\n                for sname, jids in [(\"min_eta_max\", b_best_eta_jids),\n                                     (\"min_keff\", b_min_keff_jids),\n                                     (\"max_keff\", b_max_keff_jids)]:\n                    asr = compute_panel_asr_fast(jids, clean[ds], attacked[ds][atk], ds_pairs)\n                    strat_level_boot[sname].append(asr)\n\n            strat_level_boot = {k: np.array(v) for k, v in strat_level_boot.items()}\n\n            # ── Compute CIs and pairwise tests ──\n            def ci95(arr):\n                arr = arr[~np.isnan(arr)]\n                if len(arr) == 0:\n                    return [None, None]\n                return [float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5))]\n\n            cond_result = {\n                \"condition\": cond,\n            }\n\n            for sname in [\"min_eta_max\", \"min_keff\", \"max_keff\"]:\n                jids = strategies[sname]\n                asr_val = asr_from_outcomes(strat_outcomes[sname])\n                cond_result[sname] = {\n                    \"panel\": [ALL_MODELS[j] for j in jids],\n                    \"asr\": float(asr_val) if not np.isnan(asr_val) else None,\n                    \"sample_bootstrap_ci_95\": ci95(strat_boot[sname]),\n                    \"strategy_bootstrap_ci_95\": ci95(strat_level_boot[sname]),\n                    \"strategy_bootstrap_mean\": float(np.nanmean(strat_level_boot[sname])),\n                }\n\n            cond_result[\"random\"] = {\n                \"asr_mean\": float(rand_asr_mean),\n                \"sample_bootstrap_ci_95\": ci95(rand_boot_asrs),\n            }\n\n            # Pairwise\n            pairwise = {}\n            pairs_to_test = [\n                (\"min_eta_vs_random\", \"min_eta_max\", \"random\"),\n                (\"min_keff_vs_random\", \"min_keff\", \"random\"),\n                (\"min_eta_vs_max_keff\", \"min_eta_max\", \"max_keff\"),\n            ]\n            for pname, s1, s2 in pairs_to_test:\n                b1 = strat_boot[s1]\n                b2 = strat_boot[s2]\n                delta_boot = b1 - b2\n                delta_obs = (\n                    (asr_from_outcomes(strat_outcomes[s1]) if s1 != \"random\" else rand_asr_mean)\n                    - (asr_from_outcomes(strat_outcomes[s2]) if s2 != \"random\" else rand_asr_mean)\n                )\n                lo, hi = ci95(delta_boot)\n                significant = (lo is not None and hi is not None and\n                               not (lo <= 0 <= hi))\n                pairwise[pname] = {\n                    \"delta\": float(delta_obs) if not np.isnan(delta_obs) else None,\n                    \"ci_95\": [lo, hi],\n                    \"significant\": significant,\n                }\n                if significant:\n                    sig_counts[pname] += 1\n\n            cond_result[\"pairwise\"] = pairwise\n\n            # Print summary\n            print(f\"  min(η_max): ASR={cond_result['min_eta_max']['asr']:.4f}  \"\n                  f\"CI={cond_result['min_eta_max']['sample_bootstrap_ci_95']}\")\n            print(f\"  min(K_eff): ASR={cond_result['min_keff']['asr']:.4f}  \"\n                  f\"CI={cond_result['min_keff']['sample_bootstrap_ci_95']}\")\n            print(f\"  random:     ASR={cond_result['random']['asr_mean']:.4f}  \"\n                  f\"CI={cond_result['random']['sample_bootstrap_ci_95']}\")\n            print(f\"  max(K_eff): ASR={cond_result['max_keff']['asr']:.4f}  \"\n                  f\"CI={cond_result['max_keff']['sample_bootstrap_ci_95']}\")\n            for pname, pdata in pairwise.items():\n                sig_str = \"***SIG***\" if pdata[\"significant\"] else \"n.s.\"\n                print(f\"  {pname}: Δ={pdata['delta']:.4f}  CI={pdata['ci_95']}  {sig_str}\")\n\n            per_condition.append(cond_result)\n\n    # Summary\n    output = {\n        \"panel_size\": K,\n        \"n_bootstrap\": B,\n        \"n_models\": len(ALL_MODELS),\n        \"n_total_panels\": len(all_combos),\n        \"per_condition\": per_condition,\n        \"summary\": {\n            \"n_conditions\": n_conditions,\n            \"min_eta_vs_random_sig\": f\"{sig_counts['min_eta_vs_random']}/{n_conditions}\",\n            \"min_keff_vs_random_sig\": f\"{sig_counts['min_keff_vs_random']}/{n_conditions}\",\n            \"min_eta_vs_max_keff_sig\": f\"{sig_counts['min_eta_vs_max_keff']}/{n_conditions}\",\n        },\n    }\n\n    print(f\"\\n{'='*60}\")\n    print(\"SUMMARY\")\n    print(f\"{'='*60}\")\n    for k, v in output[\"summary\"].items():\n        print(f\"  {k}: {v}\")\n\n    out_dir = Path(\"/root/cert_manip_resist_eval/artifacts/results/plan001\")\n    out_dir.mkdir(parents=True, exist_ok=True)\n    out_path = out_dir / \"k5_panel_selection_bootstrap.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    print(f\"\\nSaved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T06:23:53.789463+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T06:23:53.789709+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat > /root/cert_manip_resist_eval/scripts/run_k5_panel_selection_bootstrap.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"K=5 Panel Selection Bootstrap Confidence Intervals.\n\nTwo types of bootstrap:\n1. Sample-level: resample samples with replacement to get CI on each strategy's ASR\n2. Strategy-level: resample from 3003 panels to simulate panel pool uncertainty\n\"\"\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nfrom pathlib import Path\n\nfrom src.unified_data_loader import (\n    ALL_MODELS, DATASETS, ATTACKS,\n    load_all_scores, load_pairs, load_mi_data, _is_valid_score,\n)\n\nB = 9999\nK = 5\nALPHA = 0.05\n\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef get_sample_outcomes(jids, clean_ds, attacked_ds_atk, ds_pairs):\n    \"\"\"Per-sample: 1=flip, 0=no-flip, NaN=excluded.\"\"\"\n    n = min(len(ds_pairs), *(len(clean_ds[j]) for j in jids),\n            *(len(attacked_ds_atk[j]) for j in jids))\n    outcomes = []\n    for i in range(n):\n        any_invalid = False\n        for j in jids:\n            if not _is_valid_score(clean_ds[j][i]) or not _is_valid_score(attacked_ds_atk[j][i]):\n                any_invalid = True\n                break\n        if any_invalid:\n            outcomes.append(np.nan)\n            continue\n        gt = ds_pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean_ds[j][i][\"winner\"] for j in jids])\n        if cv != gt:\n            outcomes.append(np.nan)\n            continue\n        av = majority_vote([attacked_ds_atk[j][i][\"winner\"] for j in jids])\n        outcomes.append(1.0 if av != gt else 0.0)\n    return np.array(outcomes)\n\n\ndef asr_from_outcomes(outcomes):\n    valid = outcomes[~np.isnan(outcomes)]\n    return np.mean(valid) if len(valid) > 0 else np.nan\n\n\ndef bootstrap_asr(outcomes, rng):\n    valid = outcomes[~np.isnan(outcomes)]\n    n = len(valid)\n    if n == 0:\n        return np.full(B, np.nan)\n    idx = rng.integers(0, n, size=(B, n))\n    return np.mean(valid[idx], axis=1)\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        if not _is_valid_score(clean_list[i]) or not _is_valid_score(attacked_list[i]):\n            continue\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i][\"winner\"] == gt:\n            n_correct += 1\n            if attacked_list[i][\"winner\"] != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef mi_based_keff(mi_matrix, model_indices):\n    Kp = len(model_indices)\n    if Kp <= 1:\n        return 1.0\n    keff = 0.0\n    for i_idx in model_indices:\n        term = 1.0\n        for j_idx in model_indices:\n            if i_idx != j_idx:\n                term += np.exp(-2 * mi_matrix[i_idx, j_idx])\n        keff += term\n    return keff / Kp\n\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\ndef ci95(arr):\n    arr = np.asarray(arr)\n    arr = arr[~np.isnan(arr)]\n    if len(arr) == 0:\n        return [None, None]\n    return [float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5))]\n\n\ndef main():\n    print(\"Loading data...\")\n    mi_data = load_mi_data()\n    mi_matrices_raw = mi_data[\"mi_matrix\"]\n    pairs_data = load_pairs()\n    clean, attacked = load_all_scores()\n    mi_matrices = {ds: np.array(mi_matrices_raw[ds]) for ds in DATASETS}\n\n    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), K))\n    n_panels = len(all_combos)\n    print(f\"C(15,5) = {n_panels} panels, B = {B}\")\n\n    rng = np.random.default_rng(42)\n\n    per_condition = []\n    sig_counts = {\n        \"min_eta_vs_random\": 0,\n        \"min_keff_vs_random\": 0,\n        \"min_eta_vs_max_keff\": 0,\n    }\n    n_conditions = 0\n\n    for ds in DATASETS:\n        ds_pairs = pairs_data[ds]\n        mi_mat = mi_matrices[ds]\n\n        for atk in ATTACKS:\n            cond = f\"{ds}×{atk}\"\n            n_conditions += 1\n            print(f\"\\n{'='*60}\")\n            print(f\"[{n_conditions}/12] {cond}\")\n\n            # Individual ASRs\n            ind_asrs = {}\n            for j, m in enumerate(ALL_MODELS):\n                ind_asrs[j] = compute_individual_asr(\n                    clean[ds][m], attacked[ds][atk][m], ds_pairs\n                )\n\n            # Pre-compute panel properties (eta_max, keff) and ASR for all panels\n            print(\"  Computing all panel properties...\")\n            eta_max_arr = np.zeros(n_panels)\n            keff_arr = np.zeros(n_panels)\n            panel_asr_arr = np.zeros(n_panels)\n\n            for ci, combo in enumerate(all_combos):\n                jids = list(combo)\n                eta_max_arr[ci] = max(ind_asrs[j] for j in jids)\n                keff_arr[ci] = mi_based_keff(mi_mat, jids)\n\n            # Find strategy-selected panels\n            # min(eta_max): break ties by max keff\n            min_eta = eta_max_arr.min()\n            eta_ties = np.where(eta_max_arr == min_eta)[0]\n            best_eta_idx = eta_ties[np.argmax(keff_arr[eta_ties])]\n\n            best_max_keff_idx = np.argmax(keff_arr)\n            best_min_keff_idx = np.argmin(keff_arr)\n\n            strategy_indices = {\n                \"min_eta_max\": best_eta_idx,\n                \"min_keff\": best_min_keff_idx,\n                \"max_keff\": best_max_keff_idx,\n            }\n            strategy_jids = {\n                sname: list(all_combos[idx])\n                for sname, idx in strategy_indices.items()\n            }\n\n            # Compute sample outcomes for each strategy's panel\n            print(\"  Sample-level bootstrap...\")\n            strat_outcomes = {}\n            strat_boot = {}\n            for sname, jids in strategy_jids.items():\n                outcomes = get_sample_outcomes(jids, clean[ds], attacked[ds][atk], ds_pairs)\n                strat_outcomes[sname] = outcomes\n                strat_boot[sname] = bootstrap_asr(outcomes, rng)\n\n            # Random: 100 panels\n            rand_indices = rng.choice(n_panels, size=100, replace=False)\n            rand_outcomes_list = []\n            for ri in rand_indices:\n                jids = list(all_combos[ri])\n                outcomes = get_sample_outcomes(jids, clean[ds], attacked[ds][atk], ds_pairs)\n                rand_outcomes_list.append(outcomes)\n\n            # Random bootstrap: for each bootstrap iter, resample samples for each panel, average\n            rand_boot_asrs = np.zeros(B)\n            for outcomes in rand_outcomes_list:\n                rand_boot_asrs += bootstrap_asr(outcomes, rng)\n            rand_boot_asrs /= len(rand_outcomes_list)\n            strat_boot[\"random\"] = rand_boot_asrs\n\n            rand_asr_point = float(np.mean([asr_from_outcomes(o) for o in rand_outcomes_list]))\n\n            # ── Strategy-level bootstrap (vectorized) ──\n            print(\"  Strategy-level bootstrap...\")\n            # Precompute all panel ASRs (needed for strategy-level)\n            for ci, combo in enumerate(all_combos):\n                jids = list(combo)\n                oc = get_sample_outcomes(jids, clean[ds], attacked[ds][atk], ds_pairs)\n                panel_asr_arr[ci] = asr_from_outcomes(oc)\n\n            # Vectorized: resample panel indices, find best by each criterion\n            boot_panel_idx = rng.integers(0, n_panels, size=(B, n_panels))\n\n            strat_level_boot = {}\n            # min(eta_max)\n            boot_eta = eta_max_arr[boot_panel_idx]  # (B, n_panels)\n            boot_min_eta = boot_eta.min(axis=1, keepdims=True)  # (B, 1)\n            # For tie-breaking: among panels with min eta, pick max keff\n            boot_keff_all = keff_arr[boot_panel_idx]  # (B, n_panels)\n            is_min_eta = (boot_eta == boot_min_eta)  # (B, n_panels)\n            boot_keff_masked = np.where(is_min_eta, boot_keff_all, -np.inf)\n            best_in_boot = np.argmax(boot_keff_masked, axis=1)  # (B,)\n            # Map back to original panel index\n            selected_orig_idx = boot_panel_idx[np.arange(B), best_in_boot]\n            strat_level_boot[\"min_eta_max\"] = panel_asr_arr[selected_orig_idx]\n\n            # max(keff)\n            best_keff_in_boot = np.argmax(boot_keff_all, axis=1)\n            selected_orig_idx = boot_panel_idx[np.arange(B), best_keff_in_boot]\n            strat_level_boot[\"max_keff\"] = panel_asr_arr[selected_orig_idx]\n\n            # min(keff)\n            worst_keff_in_boot = np.argmin(boot_keff_all, axis=1)\n            selected_orig_idx = boot_panel_idx[np.arange(B), worst_keff_in_boot]\n            strat_level_boot[\"min_keff\"] = panel_asr_arr[selected_orig_idx]\n\n            # ── Assemble results ──\n            cond_result = {\"condition\": cond}\n\n            for sname in [\"min_eta_max\", \"min_keff\", \"max_keff\"]:\n                jids = strategy_jids[sname]\n                asr_val = asr_from_outcomes(strat_outcomes[sname])\n                cond_result[sname] = {\n                    \"panel\": [ALL_MODELS[j] for j in jids],\n                    \"asr\": float(asr_val) if not np.isnan(asr_val) else None,\n                    \"sample_bootstrap_ci_95\": ci95(strat_boot[sname]),\n                    \"strategy_bootstrap_ci_95\": ci95(strat_level_boot[sname]),\n                    \"strategy_bootstrap_mean\": float(np.nanmean(strat_level_boot[sname])),\n                }\n\n            cond_result[\"random\"] = {\n                \"asr_mean\": rand_asr_point,\n                \"sample_bootstrap_ci_95\": ci95(rand_boot_asrs),\n            }\n\n            # Pairwise comparisons\n            pairwise = {}\n            pairs_to_test = [\n                (\"min_eta_vs_random\", \"min_eta_max\", \"random\"),\n                (\"min_keff_vs_random\", \"min_keff\", \"random\"),\n                (\"min_eta_vs_max_keff\", \"min_eta_max\", \"max_keff\"),\n            ]\n            for pname, s1, s2 in pairs_to_test:\n                b1 = strat_boot[s1]\n                b2 = strat_boot[s2]\n                delta_boot = b1 - b2\n                a1 = asr_from_outcomes(strat_outcomes[s1]) if s1 in strat_outcomes else rand_asr_point\n                a2 = asr_from_outcomes(strat_outcomes[s2]) if s2 in strat_outcomes else rand_asr_point\n                delta_obs = float(a1 - a2)\n                lo, hi = ci95(delta_boot)\n                significant = (lo is not None and hi is not None and not (lo <= 0 <= hi))\n                pairwise[pname] = {\n                    \"delta\": delta_obs if not np.isnan(delta_obs) else None,\n                    \"ci_95\": [lo, hi],\n                    \"significant\": significant,\n                }\n                if significant:\n                    sig_counts[pname] += 1\n\n            cond_result[\"pairwise\"] = pairwise\n            per_condition.append(cond_result)\n\n            # Print\n            for sname in [\"min_eta_max\", \"min_keff\", \"random\", \"max_keff\"]:\n                if sname == \"random\":\n                    print(f\"  {sname:>14}: ASR={cond_result[sname]['asr_mean']:.4f}  \"\n                          f\"sampleCI={cond_result[sname]['sample_bootstrap_ci_95']}\")\n                else:\n                    print(f\"  {sname:>14}: ASR={cond_result[sname]['asr']:.4f}  \"\n                          f\"sampleCI={cond_result[sname]['sample_bootstrap_ci_95']}  \"\n                          f\"stratCI={cond_result[sname]['strategy_bootstrap_ci_95']}\")\n            for pname, pd in pairwise.items():\n                sig_str = \"***\" if pd[\"significant\"] else \"n.s.\"\n                delta_str = f\"{pd['delta']:.4f}\" if pd['delta'] is not None else \"N/A\"\n                print(f\"  {pname}: Δ={delta_str}  CI={pd['ci_95']}  {sig_str}\")\n\n    # ── Summary ──\n    output = {\n        \"panel_size\": K,\n        \"n_bootstrap\": B,\n        \"n_models\": len(ALL_MODELS),\n        \"n_total_panels\": n_panels,\n        \"per_condition\": per_condition,\n        \"summary\": {\n            \"n_conditions\": n_conditions,\n            \"min_eta_vs_random_sig\": f\"{sig_counts['min_eta_vs_random']}/{n_conditions}\",\n            \"min_keff_vs_random_sig\": f\"{sig_counts['min_keff_vs_random']}/{n_conditions}\",\n            \"min_eta_vs_max_keff_sig\": f\"{sig_counts['min_eta_vs_max_keff']}/{n_conditions}\",\n        },\n    }\n\n    print(f\"\\n{'='*60}\")\n    print(\"SUMMARY\")\n    for k, v in output[\"summary\"].items():\n        print(f\"  {k}: {v}\")\n\n    out_dir = Path(\"/root/cert_manip_resist_eval/artifacts/results/plan001\")\n    out_dir.mkdir(parents=True, exist_ok=True)\n    out_path = out_dir / \"k5_panel_selection_bootstrap.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    print(f\"\\nSaved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cat > /root/cert_manip_resist_eval/scripts/run_k5_panel_selection_bootstrap.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"K=5 Panel Selection Bootstrap Confidence Intervals.\n\nTwo types of bootstrap:\n1. Sample-level: resample samples with replacement to get CI on each strategy's ASR\n2. Strategy-level: resample from 3003 panels to simulate panel pool uncertainty\n\"\"\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nfrom pathlib import Path\n\nfrom src.unified_data_loader import (\n    ALL_MODELS, DATASETS, ATTACKS,\n    load_all_scores, load_pairs, load_mi_data, _is_valid_score,\n)\n\nB = 9999\nK = 5\nALPHA = 0.05\n\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef get_sample_outcomes(jids, clean_ds, attacked_ds_atk, ds_pairs):\n    \"\"\"Per-sample: 1=flip, 0=no-flip, NaN=excluded.\"\"\"\n    n = min(len(ds_pairs), *(len(clean_ds[j]) for j in jids),\n            *(len(attacked_ds_atk[j]) for j in jids))\n    outcomes = []\n    for i in range(n):\n        any_invalid = False\n        for j in jids:\n            if not _is_valid_score(clean_ds[j][i]) or not _is_valid_score(attacked_ds_atk[j][i]):\n                any_invalid = True\n                break\n        if any_invalid:\n            outcomes.append(np.nan)\n            continue\n        gt = ds_pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean_ds[j][i][\"winner\"] for j in jids])\n        if cv != gt:\n            outcomes.append(np.nan)\n            continue\n        av = majority_vote([attacked_ds_atk[j][i][\"winner\"] for j in jids])\n        outcomes.append(1.0 if av != gt else 0.0)\n    return np.array(outcomes)\n\n\ndef asr_from_outcomes(outcomes):\n    valid = outcomes[~np.isnan(outcomes)]\n    return np.mean(valid) if len(valid) > 0 else np.nan\n\n\ndef bootstrap_asr(outcomes, rng):\n    valid = outcomes[~np.isnan(outcomes)]\n    n = len(valid)\n    if n == 0:\n        return np.full(B, np.nan)\n    idx = rng.integers(0, n, size=(B, n))\n    return np.mean(valid[idx], axis=1)\n\n\ndef compute_individual_asr(clean_list, attacked_list, pairs):\n    n = min(len(clean_list), len(attacked_list), len(pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        if not _is_valid_score(clean_list[i]) or not _is_valid_score(attacked_list[i]):\n            continue\n        gt = pairs[i][\"ground_truth_winner\"]\n        if clean_list[i][\"winner\"] == gt:\n            n_correct += 1\n            if attacked_list[i][\"winner\"] != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef mi_based_keff(mi_matrix, model_indices):\n    Kp = len(model_indices)\n    if Kp <= 1:\n        return 1.0\n    keff = 0.0\n    for i_idx in model_indices:\n        term = 1.0\n        for j_idx in model_indices:\n            if i_idx != j_idx:\n                term += np.exp(-2 * mi_matrix[i_idx, j_idx])\n        keff += term\n    return keff / Kp\n\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\ndef ci95(arr):\n    arr = np.asarray(arr)\n    arr = arr[~np.isnan(arr)]\n    if len(arr) == 0:\n        return [None, None]\n    return [float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5))]\n\n\ndef main():\n    print(\"Loading data...\")\n    mi_data = load_mi_data()\n    mi_matrices_raw = mi_data[\"mi_matrix\"]\n    pairs_data = load_pairs()\n    clean, attacked = load_all_scores()\n    mi_matrices = {ds: np.array(mi_matrices_raw[ds]) for ds in DATASETS}\n\n    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), K))\n    n_panels = len(all_combos)\n    print(f\"C(15,5) = {n_panels} panels, B = {B}\")\n\n    rng = np.random.default_rng(42)\n\n    per_condition = []\n    sig_counts = {\n        \"min_eta_vs_random\": 0,\n        \"min_keff_vs_random\": 0,\n        \"min_eta_vs_max_keff\": 0,\n    }\n    n_conditions = 0\n\n    for ds in DATASETS:\n        ds_pairs = pairs_data[ds]\n        mi_mat = mi_matrices[ds]\n\n        for atk in ATTACKS:\n            cond = f\"{ds}×{atk}\"\n            n_conditions += 1\n            print(f\"\\n{'='*60}\")\n            print(f\"[{n_conditions}/12] {cond}\")\n\n            # Individual ASRs\n            ind_asrs = {}\n            for j, m in enumerate(ALL_MODELS):\n                ind_asrs[j] = compute_individual_asr(\n                    clean[ds][m], attacked[ds][atk][m], ds_pairs\n                )\n\n            # Pre-compute panel properties (eta_max, keff) and ASR for all panels\n            print(\"  Computing all panel properties...\")\n            eta_max_arr = np.zeros(n_panels)\n            keff_arr = np.zeros(n_panels)\n            panel_asr_arr = np.zeros(n_panels)\n\n            for ci, combo in enumerate(all_combos):\n                jids = list(combo)\n                eta_max_arr[ci] = max(ind_asrs[j] for j in jids)\n                keff_arr[ci] = mi_based_keff(mi_mat, jids)\n\n            # Find strategy-selected panels\n            # min(eta_max): break ties by max keff\n            min_eta = eta_max_arr.min()\n            eta_ties = np.where(eta_max_arr == min_eta)[0]\n            best_eta_idx = eta_ties[np.argmax(keff_arr[eta_ties])]\n\n            best_max_keff_idx = np.argmax(keff_arr)\n            best_min_keff_idx = np.argmin(keff_arr)\n\n            strategy_indices = {\n                \"min_eta_max\": best_eta_idx,\n                \"min_keff\": best_min_keff_idx,\n                \"max_keff\": best_max_keff_idx,\n            }\n            strategy_jids = {\n                sname: list(all_combos[idx])\n                for sname, idx in strategy_indices.items()\n            }\n\n            # Compute sample outcomes for each strategy's panel\n            print(\"  Sample-level bootstrap...\")\n            strat_outcomes = {}\n            strat_boot = {}\n            for sname, jids in strategy_jids.items():\n                outcomes = get_sample_outcomes(jids, clean[ds], attacked[ds][atk], ds_pairs)\n                strat_outcomes[sname] = outcomes\n                strat_boot[sname] = bootstrap_asr(outcomes, rng)\n\n            # Random: 100 panels\n            rand_indices = rng.choice(n_panels, size=100, replace=False)\n            rand_outcomes_list = []\n            for ri in rand_indices:\n                jids = list(all_combos[ri])\n                outcomes = get_sample_outcomes(jids, clean[ds], attacked[ds][atk], ds_pairs)\n                rand_outcomes_list.append(outcomes)\n\n            # Random bootstrap: for each bootstrap iter, resample samples for each panel, average\n            rand_boot_asrs = np.zeros(B)\n            for outcomes in rand_outcomes_list:\n                rand_boot_asrs += bootstrap_asr(outcomes, rng)\n            rand_boot_asrs /= len(rand_outcomes_list)\n            strat_boot[\"random\"] = rand_boot_asrs\n\n            rand_asr_point = float(np.mean([asr_from_outcomes(o) for o in rand_outcomes_list]))\n\n            # ── Strategy-level bootstrap (vectorized) ──\n            print(\"  Strategy-level bootstrap...\")\n            # Precompute all panel ASRs (needed for strategy-level)\n            for ci, combo in enumerate(all_combos):\n                jids = list(combo)\n                oc = get_sample_outcomes(jids, clean[ds], attacked[ds][atk], ds_pairs)\n                panel_asr_arr[ci] = asr_from_outcomes(oc)\n\n            # Vectorized: resample panel indices, find best by each criterion\n            boot_panel_idx = rng.integers(0, n_panels, size=(B, n_panels))\n\n            strat_level_boot = {}\n            # min(eta_max)\n            boot_eta = eta_max_arr[boot_panel_idx]  # (B, n_panels)\n            boot_min_eta = boot_eta.min(axis=1, keepdims=True)  # (B, 1)\n            # For tie-breaking: among panels with min eta, pick max keff\n            boot_keff_all = keff_arr[boot_panel_idx]  # (B, n_panels)\n            is_min_eta = (boot_eta == boot_min_eta)  # (B, n_panels)\n            boot_keff_masked = np.where(is_min_eta, boot_keff_all, -np.inf)\n            best_in_boot = np.argmax(boot_keff_masked, axis=1)  # (B,)\n            # Map back to original panel index\n            selected_orig_idx = boot_panel_idx[np.arange(B), best_in_boot]\n            strat_level_boot[\"min_eta_max\"] = panel_asr_arr[selected_orig_idx]\n\n            # max(keff)\n            best_keff_in_boot = np.argmax(boot_keff_all, axis=1)\n            selected_orig_idx = boot_panel_idx[np.arange(B), best_keff_in_boot]\n            strat_level_boot[\"max_keff\"] = panel_asr_arr[selected_orig_idx]\n\n            # min(keff)\n            worst_keff_in_boot = np.argmin(boot_keff_all, axis=1)\n            selected_orig_idx = boot_panel_idx[np.arange(B), worst_keff_in_boot]\n            strat_level_boot[\"min_keff\"] = panel_asr_arr[selected_orig_idx]\n\n            # ── Assemble results ──\n            cond_result = {\"condition\": cond}\n\n            for sname in [\"min_eta_max\", \"min_keff\", \"max_keff\"]:\n                jids = strategy_jids[sname]\n                asr_val = asr_from_outcomes(strat_outcomes[sname])\n                cond_result[sname] = {\n                    \"panel\": [ALL_MODELS[j] for j in jids],\n                    \"asr\": float(asr_val) if not np.isnan(asr_val) else None,\n                    \"sample_bootstrap_ci_95\": ci95(strat_boot[sname]),\n                    \"strategy_bootstrap_ci_95\": ci95(strat_level_boot[sname]),\n                    \"strategy_bootstrap_mean\": float(np.nanmean(strat_level_boot[sname])),\n                }\n\n            cond_result[\"random\"] = {\n                \"asr_mean\": rand_asr_point,\n                \"sample_bootstrap_ci_95\": ci95(rand_boot_asrs),\n            }\n\n            # Pairwise comparisons\n            pairwise = {}\n            pairs_to_test = [\n                (\"min_eta_vs_random\", \"min_eta_max\", \"random\"),\n                (\"min_keff_vs_random\", \"min_keff\", \"random\"),\n                (\"min_eta_vs_max_keff\", \"min_eta_max\", \"max_keff\"),\n            ]\n            for pname, s1, s2 in pairs_to_test:\n                b1 = strat_boot[s1]\n                b2 = strat_boot[s2]\n                delta_boot = b1 - b2\n                a1 = asr_from_outcomes(strat_outcomes[s1]) if s1 in strat_outcomes else rand_asr_point\n                a2 = asr_from_outcomes(strat_outcomes[s2]) if s2 in strat_outcomes else rand_asr_point\n                delta_obs = float(a1 - a2)\n                lo, hi = ci95(delta_boot)\n                significant = (lo is not None and hi is not None and not (lo <= 0 <= hi))\n                pairwise[pname] = {\n                    \"delta\": delta_obs if not np.isnan(delta_obs) else None,\n                    \"ci_95\": [lo, hi],\n                    \"significant\": significant,\n                }\n                if significant:\n                    sig_counts[pname] += 1\n\n            cond_result[\"pairwise\"] = pairwise\n            per_condition.append(cond_result)\n\n            # Print\n            for sname in [\"min_eta_max\", \"min_keff\", \"random\", \"max_keff\"]:\n                if sname == \"random\":\n                    print(f\"  {sname:>14}: ASR={cond_result[sname]['asr_mean']:.4f}  \"\n                          f\"sampleCI={cond_result[sname]['sample_bootstrap_ci_95']}\")\n                else:\n                    print(f\"  {sname:>14}: ASR={cond_result[sname]['asr']:.4f}  \"\n                          f\"sampleCI={cond_result[sname]['sample_bootstrap_ci_95']}  \"\n                          f\"stratCI={cond_result[sname]['strategy_bootstrap_ci_95']}\")\n            for pname, pd in pairwise.items():\n                sig_str = \"***\" if pd[\"significant\"] else \"n.s.\"\n                delta_str = f\"{pd['delta']:.4f}\" if pd['delta'] is not None else \"N/A\"\n                print(f\"  {pname}: Δ={delta_str}  CI={pd['ci_95']}  {sig_str}\")\n\n    # ── Summary ──\n    output = {\n        \"panel_size\": K,\n        \"n_bootstrap\": B,\n        \"n_models\": len(ALL_MODELS),\n        \"n_total_panels\": n_panels,\n        \"per_condition\": per_condition,\n        \"summary\": {\n            \"n_conditions\": n_conditions,\n            \"min_eta_vs_random_sig\": f\"{sig_counts['min_eta_vs_random']}/{n_conditions}\",\n            \"min_keff_vs_random_sig\": f\"{sig_counts['min_keff_vs_random']}/{n_conditions}\",\n            \"min_eta_vs_max_keff_sig\": f\"{sig_counts['min_eta_vs_max_keff']}/{n_conditions}\",\n        },\n    }\n\n    print(f\"\\n{'='*60}\")\n    print(\"SUMMARY\")\n    for k, v in output[\"summary\"].items():\n        print(f\"  {k}: {v}\")\n\n    out_dir = Path(\"/root/cert_manip_resist_eval/artifacts/results/plan001\")\n    out_dir.mkdir(parents=True, exist_ok=True)\n    out_path = out_dir / \"k5_panel_selection_bootstrap.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    print(f\"\\nSaved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T06:23:53.789990+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T06:23:53.790155+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cd /root/cert_manip_resist_eval && nohup /root/miniconda3/bin/python3 scripts/run_k5_panel_selection_bootstrap.py > /tmp/k5_bootstrap.log 2>&1 & echo \"PID=$!\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cd /root/cert_manip_resist_eval && nohup /root/miniconda3/bin/python3 scripts/run_k5_panel_selection_bootstrap.py > /tmp/k5_bootstrap.log 2>&1 & echo \"PID=$!\""
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T06:23:53.790285+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"PID=155632\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T06:23:53.790418+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "tail -30 /tmp/k5_bootstrap.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "tail -30 /tmp/k5_bootstrap.log"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T06:23:53.790557+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading data...\\nC(15,5) = 3003 panels, B = 9999\\n\\n============================================================\\n[1/12] mmlu×prompt_injection\\n  Computing all panel properties...\\n  Sample-level bootstrap...\\nTraceback (most recent call last):\\n  File \\\"/root/cert_manip_resist_eval/scripts/run_k5_panel_selection_bootstrap.py\\\", line 346, in &lt;module>\\n    main()\\n  File \\\"/root/cert_manip_resist_eval/scripts/run_k5_panel_selection_bootstrap.py\\\", line 202, in main\\n    outcomes = get_sample_outcomes(jids, clean[ds], attacked[ds][atk], ds_pairs)\\n               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/cert_manip_resist_eval/scripts/run_k5_panel_selection_bootstrap.py\\\", line 43, in get_sample_outcomes\\n    n = min(len(ds_pairs), *(len(clean_ds[j]) for j in jids),\\n        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/cert_manip_resist_eval/scripts/run_k5_panel_selection_bootstrap.py\\\", line 43, in &lt;genexpr>\\n    n = min(len(ds_pairs), *(len(clean_ds[j]) for j in jids),\\n                                 ~~~~~~~~^^^\\nKeyError: 6\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T06:23:53.790803+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat > /root/cert_manip_resist_eval/scripts/run_k5_panel_selection_bootstrap.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"K=5 Panel Selection Bootstrap Confidence Intervals.\"\"\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nfrom pathlib import Path\n\nfrom src.unified_data_loader import (\n    ALL_MODELS, DATASETS, ATTACKS,\n    load_all_scores, load_pairs, load_mi_data, _is_valid_score,\n)\n\nB = 9999\nK = 5\n\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef get_sample_outcomes(model_names, clean_ds, attacked_ds_atk, ds_pairs):\n    \"\"\"Per-sample: 1=flip, 0=no-flip, NaN=excluded. Uses model name strings.\"\"\"\n    n = min(len(ds_pairs), *(len(clean_ds[m]) for m in model_names),\n            *(len(attacked_ds_atk[m]) for m in model_names))\n    outcomes = []\n    for i in range(n):\n        any_invalid = False\n        for m in model_names:\n            if not _is_valid_score(clean_ds[m][i]) or not _is_valid_score(attacked_ds_atk[m][i]):\n                any_invalid = True\n                break\n        if any_invalid:\n            outcomes.append(np.nan)\n            continue\n        gt = ds_pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean_ds[m][i][\"winner\"] for m in model_names])\n        if cv != gt:\n            outcomes.append(np.nan)\n            continue\n        av = majority_vote([attacked_ds_atk[m][i][\"winner\"] for m in model_names])\n        outcomes.append(1.0 if av != gt else 0.0)\n    return np.array(outcomes)\n\n\ndef asr_from_outcomes(outcomes):\n    valid = outcomes[~np.isnan(outcomes)]\n    return np.mean(valid) if len(valid) > 0 else np.nan\n\n\ndef bootstrap_asr(outcomes, rng):\n    valid = outcomes[~np.isnan(outcomes)]\n    n = len(valid)\n    if n == 0:\n        return np.full(B, np.nan)\n    idx = rng.integers(0, n, size=(B, n))\n    return np.mean(valid[idx], axis=1)\n\n\ndef compute_individual_asr(clean_list, attacked_list, ds_pairs):\n    n = min(len(clean_list), len(attacked_list), len(ds_pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        if not _is_valid_score(clean_list[i]) or not _is_valid_score(attacked_list[i]):\n            continue\n        gt = ds_pairs[i][\"ground_truth_winner\"]\n        if clean_list[i][\"winner\"] == gt:\n            n_correct += 1\n            if attacked_list[i][\"winner\"] != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef mi_based_keff(mi_matrix, model_indices):\n    Kp = len(model_indices)\n    if Kp <= 1:\n        return 1.0\n    keff = 0.0\n    for i_idx in model_indices:\n        term = 1.0\n        for j_idx in model_indices:\n            if i_idx != j_idx:\n                term += np.exp(-2 * mi_matrix[i_idx, j_idx])\n        keff += term\n    return keff / Kp\n\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\ndef ci95(arr):\n    arr = np.asarray(arr, dtype=float)\n    arr = arr[~np.isnan(arr)]\n    if len(arr) == 0:\n        return [None, None]\n    return [float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5))]\n\n\ndef combo_to_names(combo):\n    return [ALL_MODELS[j] for j in combo]\n\n\ndef main():\n    print(\"Loading data...\")\n    mi_data = load_mi_data()\n    mi_matrices_raw = mi_data[\"mi_matrix\"]\n    pairs_data = load_pairs()\n    clean, attacked = load_all_scores()\n    mi_matrices = {ds: np.array(mi_matrices_raw[ds]) for ds in DATASETS}\n\n    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), K))\n    n_panels = len(all_combos)\n    print(f\"C(15,5) = {n_panels} panels, B = {B}\")\n\n    rng = np.random.default_rng(42)\n\n    per_condition = []\n    sig_counts = {\n        \"min_eta_vs_random\": 0,\n        \"min_keff_vs_random\": 0,\n        \"min_eta_vs_max_keff\": 0,\n    }\n    n_conditions = 0\n\n    for ds in DATASETS:\n        ds_pairs = pairs_data[ds]\n        mi_mat = mi_matrices[ds]\n\n        for atk in ATTACKS:\n            cond = f\"{ds}×{atk}\"\n            n_conditions += 1\n            print(f\"\\n{'='*60}\")\n            print(f\"[{n_conditions}/12] {cond}\")\n\n            # Individual ASRs (by model index)\n            ind_asrs = np.zeros(len(ALL_MODELS))\n            for j, m in enumerate(ALL_MODELS):\n                ind_asrs[j] = compute_individual_asr(\n                    clean[ds][m], attacked[ds][atk][m], ds_pairs\n                )\n\n            # Pre-compute panel properties for all 3003 panels\n            print(\"  Computing panel properties...\")\n            eta_max_arr = np.zeros(n_panels)\n            keff_arr = np.zeros(n_panels)\n\n            for ci, combo in enumerate(all_combos):\n                jids = list(combo)\n                eta_max_arr[ci] = max(ind_asrs[j] for j in jids)\n                keff_arr[ci] = mi_based_keff(mi_mat, jids)\n\n            # Find strategy-selected panels\n            min_eta = eta_max_arr.min()\n            eta_ties = np.where(eta_max_arr == min_eta)[0]\n            best_eta_idx = eta_ties[np.argmax(keff_arr[eta_ties])]\n            best_max_keff_idx = int(np.argmax(keff_arr))\n            best_min_keff_idx = int(np.argmin(keff_arr))\n\n            strategy_panel_idx = {\n                \"min_eta_max\": int(best_eta_idx),\n                \"min_keff\": best_min_keff_idx,\n                \"max_keff\": best_max_keff_idx,\n            }\n            strategy_names = {\n                sname: combo_to_names(all_combos[idx])\n                for sname, idx in strategy_panel_idx.items()\n            }\n\n            # ── Sample-level bootstrap ──\n            print(\"  Sample-level bootstrap...\")\n            strat_outcomes = {}\n            strat_boot = {}\n            for sname, mnames in strategy_names.items():\n                outcomes = get_sample_outcomes(mnames, clean[ds], attacked[ds][atk], ds_pairs)\n                strat_outcomes[sname] = outcomes\n                strat_boot[sname] = bootstrap_asr(outcomes, rng)\n\n            # Random: 100 panels\n            rand_indices = rng.choice(n_panels, size=100, replace=False)\n            rand_boot_asrs = np.zeros(B)\n            rand_asr_points = []\n            for ri in rand_indices:\n                mnames = combo_to_names(all_combos[ri])\n                outcomes = get_sample_outcomes(mnames, clean[ds], attacked[ds][atk], ds_pairs)\n                rand_asr_points.append(asr_from_outcomes(outcomes))\n                rand_boot_asrs += bootstrap_asr(outcomes, rng)\n            rand_boot_asrs /= 100\n            strat_boot[\"random\"] = rand_boot_asrs\n            rand_asr_point = float(np.mean(rand_asr_points))\n\n            # ── Strategy-level bootstrap (vectorized) ──\n            print(\"  Computing all panel ASRs for strategy bootstrap...\")\n            panel_asr_arr = np.zeros(n_panels)\n            for ci, combo in enumerate(all_combos):\n                mnames = combo_to_names(combo)\n                oc = get_sample_outcomes(mnames, clean[ds], attacked[ds][atk], ds_pairs)\n                panel_asr_arr[ci] = asr_from_outcomes(oc)\n\n            print(\"  Strategy-level bootstrap...\")\n            boot_panel_idx = rng.integers(0, n_panels, size=(B, n_panels))\n\n            strat_level_boot = {}\n\n            # min(eta_max): tie-break by max keff\n            boot_eta = eta_max_arr[boot_panel_idx]\n            boot_min_eta = boot_eta.min(axis=1, keepdims=True)\n            boot_keff_all = keff_arr[boot_panel_idx]\n            is_min_eta = (boot_eta == boot_min_eta)\n            boot_keff_masked = np.where(is_min_eta, boot_keff_all, -np.inf)\n            best_in_boot = np.argmax(boot_keff_masked, axis=1)\n            selected = boot_panel_idx[np.arange(B), best_in_boot]\n            strat_level_boot[\"min_eta_max\"] = panel_asr_arr[selected]\n\n            # max(keff)\n            best_keff_in = np.argmax(boot_keff_all, axis=1)\n            selected = boot_panel_idx[np.arange(B), best_keff_in]\n            strat_level_boot[\"max_keff\"] = panel_asr_arr[selected]\n\n            # min(keff)\n            worst_keff_in = np.argmin(boot_keff_all, axis=1)\n            selected = boot_panel_idx[np.arange(B), worst_keff_in]\n            strat_level_boot[\"min_keff\"] = panel_asr_arr[selected]\n\n            # ── Assemble ──\n            cond_result = {\"condition\": cond}\n\n            for sname in [\"min_eta_max\", \"min_keff\", \"max_keff\"]:\n                asr_val = asr_from_outcomes(strat_outcomes[sname])\n                cond_result[sname] = {\n                    \"panel\": strategy_names[sname],\n                    \"asr\": float(asr_val) if not np.isnan(asr_val) else None,\n                    \"sample_bootstrap_ci_95\": ci95(strat_boot[sname]),\n                    \"strategy_bootstrap_ci_95\": ci95(strat_level_boot[sname]),\n                    \"strategy_bootstrap_mean\": float(np.nanmean(strat_level_boot[sname])),\n                }\n\n            cond_result[\"random\"] = {\n                \"asr_mean\": rand_asr_point,\n                \"sample_bootstrap_ci_95\": ci95(rand_boot_asrs),\n            }\n\n            # Pairwise\n            pairwise = {}\n            for pname, s1, s2 in [\n                (\"min_eta_vs_random\", \"min_eta_max\", \"random\"),\n                (\"min_keff_vs_random\", \"min_keff\", \"random\"),\n                (\"min_eta_vs_max_keff\", \"min_eta_max\", \"max_keff\"),\n            ]:\n                b1 = strat_boot[s1]\n                b2 = strat_boot[s2]\n                delta_boot = b1 - b2\n                a1 = asr_from_outcomes(strat_outcomes[s1]) if s1 in strat_outcomes else rand_asr_point\n                a2 = asr_from_outcomes(strat_outcomes[s2]) if s2 in strat_outcomes else rand_asr_point\n                delta_obs = float(a1 - a2)\n                lo, hi = ci95(delta_boot)\n                significant = (lo is not None and hi is not None and not (lo <= 0 <= hi))\n                pairwise[pname] = {\n                    \"delta\": delta_obs if not np.isnan(delta_obs) else None,\n                    \"ci_95\": [lo, hi],\n                    \"significant\": significant,\n                }\n                if significant:\n                    sig_counts[pname] += 1\n\n            cond_result[\"pairwise\"] = pairwise\n            per_condition.append(cond_result)\n\n            for sname in [\"min_eta_max\", \"min_keff\", \"random\", \"max_keff\"]:\n                if sname == \"random\":\n                    print(f\"  {sname:>14}: ASR={cond_result[sname]['asr_mean']:.4f}  \"\n                          f\"sCI={cond_result[sname]['sample_bootstrap_ci_95']}\")\n                else:\n                    print(f\"  {sname:>14}: ASR={cond_result[sname]['asr']:.4f}  \"\n                          f\"sCI={cond_result[sname]['sample_bootstrap_ci_95']}  \"\n                          f\"stCI={cond_result[sname]['strategy_bootstrap_ci_95']}\")\n            for pn, pd in pairwise.items():\n                sig_str = \"***\" if pd[\"significant\"] else \"n.s.\"\n                d = f\"{pd['delta']:.4f}\" if pd['delta'] is not None else \"N/A\"\n                print(f\"  {pn}: Δ={d}  CI={pd['ci_95']}  {sig_str}\")\n\n    output = {\n        \"panel_size\": K,\n        \"n_bootstrap\": B,\n        \"n_models\": len(ALL_MODELS),\n        \"n_total_panels\": n_panels,\n        \"per_condition\": per_condition,\n        \"summary\": {\n            \"n_conditions\": n_conditions,\n            \"min_eta_vs_random_sig\": f\"{sig_counts['min_eta_vs_random']}/{n_conditions}\",\n            \"min_keff_vs_random_sig\": f\"{sig_counts['min_keff_vs_random']}/{n_conditions}\",\n            \"min_eta_vs_max_keff_sig\": f\"{sig_counts['min_eta_vs_max_keff']}/{n_conditions}\",\n        },\n    }\n\n    print(f\"\\n{'='*60}\")\n    print(\"SUMMARY\")\n    for k, v in output[\"summary\"].items():\n        print(f\"  {k}: {v}\")\n\n    out_dir = Path(\"/root/cert_manip_resist_eval/artifacts/results/plan001\")\n    out_dir.mkdir(parents=True, exist_ok=True)\n    out_path = out_dir / \"k5_panel_selection_bootstrap.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    print(f\"\\nSaved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cat > /root/cert_manip_resist_eval/scripts/run_k5_panel_selection_bootstrap.py << 'PYEOF'\n#!/usr/bin/env python3\n\"\"\"K=5 Panel Selection Bootstrap Confidence Intervals.\"\"\"\n\nimport sys\nsys.path.insert(0, \"/root/cert_manip_resist_eval\")\n\nimport json\nimport itertools\nimport numpy as np\nfrom pathlib import Path\n\nfrom src.unified_data_loader import (\n    ALL_MODELS, DATASETS, ATTACKS,\n    load_all_scores, load_pairs, load_mi_data, _is_valid_score,\n)\n\nB = 9999\nK = 5\n\n\ndef majority_vote(votes):\n    counts = {\"A\": 0, \"B\": 0, \"tie\": 0}\n    for v in votes:\n        counts[v] = counts.get(v, 0) + 1\n    mc = max(counts.values())\n    winners = [k for k, c in counts.items() if c == mc]\n    if len(winners) == 1:\n        return winners[0]\n    for w in winners:\n        if w != \"tie\":\n            return w\n    return \"tie\"\n\n\ndef get_sample_outcomes(model_names, clean_ds, attacked_ds_atk, ds_pairs):\n    \"\"\"Per-sample: 1=flip, 0=no-flip, NaN=excluded. Uses model name strings.\"\"\"\n    n = min(len(ds_pairs), *(len(clean_ds[m]) for m in model_names),\n            *(len(attacked_ds_atk[m]) for m in model_names))\n    outcomes = []\n    for i in range(n):\n        any_invalid = False\n        for m in model_names:\n            if not _is_valid_score(clean_ds[m][i]) or not _is_valid_score(attacked_ds_atk[m][i]):\n                any_invalid = True\n                break\n        if any_invalid:\n            outcomes.append(np.nan)\n            continue\n        gt = ds_pairs[i][\"ground_truth_winner\"]\n        cv = majority_vote([clean_ds[m][i][\"winner\"] for m in model_names])\n        if cv != gt:\n            outcomes.append(np.nan)\n            continue\n        av = majority_vote([attacked_ds_atk[m][i][\"winner\"] for m in model_names])\n        outcomes.append(1.0 if av != gt else 0.0)\n    return np.array(outcomes)\n\n\ndef asr_from_outcomes(outcomes):\n    valid = outcomes[~np.isnan(outcomes)]\n    return np.mean(valid) if len(valid) > 0 else np.nan\n\n\ndef bootstrap_asr(outcomes, rng):\n    valid = outcomes[~np.isnan(outcomes)]\n    n = len(valid)\n    if n == 0:\n        return np.full(B, np.nan)\n    idx = rng.integers(0, n, size=(B, n))\n    return np.mean(valid[idx], axis=1)\n\n\ndef compute_individual_asr(clean_list, attacked_list, ds_pairs):\n    n = min(len(clean_list), len(attacked_list), len(ds_pairs))\n    n_flips = n_correct = 0\n    for i in range(n):\n        if not _is_valid_score(clean_list[i]) or not _is_valid_score(attacked_list[i]):\n            continue\n        gt = ds_pairs[i][\"ground_truth_winner\"]\n        if clean_list[i][\"winner\"] == gt:\n            n_correct += 1\n            if attacked_list[i][\"winner\"] != gt:\n                n_flips += 1\n    return n_flips / max(n_correct, 1)\n\n\ndef mi_based_keff(mi_matrix, model_indices):\n    Kp = len(model_indices)\n    if Kp <= 1:\n        return 1.0\n    keff = 0.0\n    for i_idx in model_indices:\n        term = 1.0\n        for j_idx in model_indices:\n            if i_idx != j_idx:\n                term += np.exp(-2 * mi_matrix[i_idx, j_idx])\n        keff += term\n    return keff / Kp\n\n\ndef _json_default(obj):\n    if isinstance(obj, np.floating):\n        v = float(obj)\n        return None if (np.isnan(v) or np.isinf(v)) else v\n    if isinstance(obj, np.integer):\n        return int(obj)\n    if isinstance(obj, np.ndarray):\n        return obj.tolist()\n    if isinstance(obj, np.bool_):\n        return bool(obj)\n    raise TypeError(f\"Not JSON serializable: {type(obj)}\")\n\n\ndef ci95(arr):\n    arr = np.asarray(arr, dtype=float)\n    arr = arr[~np.isnan(arr)]\n    if len(arr) == 0:\n        return [None, None]\n    return [float(np.percentile(arr, 2.5)), float(np.percentile(arr, 97.5))]\n\n\ndef combo_to_names(combo):\n    return [ALL_MODELS[j] for j in combo]\n\n\ndef main():\n    print(\"Loading data...\")\n    mi_data = load_mi_data()\n    mi_matrices_raw = mi_data[\"mi_matrix\"]\n    pairs_data = load_pairs()\n    clean, attacked = load_all_scores()\n    mi_matrices = {ds: np.array(mi_matrices_raw[ds]) for ds in DATASETS}\n\n    all_combos = list(itertools.combinations(range(len(ALL_MODELS)), K))\n    n_panels = len(all_combos)\n    print(f\"C(15,5) = {n_panels} panels, B = {B}\")\n\n    rng = np.random.default_rng(42)\n\n    per_condition = []\n    sig_counts = {\n        \"min_eta_vs_random\": 0,\n        \"min_keff_vs_random\": 0,\n        \"min_eta_vs_max_keff\": 0,\n    }\n    n_conditions = 0\n\n    for ds in DATASETS:\n        ds_pairs = pairs_data[ds]\n        mi_mat = mi_matrices[ds]\n\n        for atk in ATTACKS:\n            cond = f\"{ds}×{atk}\"\n            n_conditions += 1\n            print(f\"\\n{'='*60}\")\n            print(f\"[{n_conditions}/12] {cond}\")\n\n            # Individual ASRs (by model index)\n            ind_asrs = np.zeros(len(ALL_MODELS))\n            for j, m in enumerate(ALL_MODELS):\n                ind_asrs[j] = compute_individual_asr(\n                    clean[ds][m], attacked[ds][atk][m], ds_pairs\n                )\n\n            # Pre-compute panel properties for all 3003 panels\n            print(\"  Computing panel properties...\")\n            eta_max_arr = np.zeros(n_panels)\n            keff_arr = np.zeros(n_panels)\n\n            for ci, combo in enumerate(all_combos):\n                jids = list(combo)\n                eta_max_arr[ci] = max(ind_asrs[j] for j in jids)\n                keff_arr[ci] = mi_based_keff(mi_mat, jids)\n\n            # Find strategy-selected panels\n            min_eta = eta_max_arr.min()\n            eta_ties = np.where(eta_max_arr == min_eta)[0]\n            best_eta_idx = eta_ties[np.argmax(keff_arr[eta_ties])]\n            best_max_keff_idx = int(np.argmax(keff_arr))\n            best_min_keff_idx = int(np.argmin(keff_arr))\n\n            strategy_panel_idx = {\n                \"min_eta_max\": int(best_eta_idx),\n                \"min_keff\": best_min_keff_idx,\n                \"max_keff\": best_max_keff_idx,\n            }\n            strategy_names = {\n                sname: combo_to_names(all_combos[idx])\n                for sname, idx in strategy_panel_idx.items()\n            }\n\n            # ── Sample-level bootstrap ──\n            print(\"  Sample-level bootstrap...\")\n            strat_outcomes = {}\n            strat_boot = {}\n            for sname, mnames in strategy_names.items():\n                outcomes = get_sample_outcomes(mnames, clean[ds], attacked[ds][atk], ds_pairs)\n                strat_outcomes[sname] = outcomes\n                strat_boot[sname] = bootstrap_asr(outcomes, rng)\n\n            # Random: 100 panels\n            rand_indices = rng.choice(n_panels, size=100, replace=False)\n            rand_boot_asrs = np.zeros(B)\n            rand_asr_points = []\n            for ri in rand_indices:\n                mnames = combo_to_names(all_combos[ri])\n                outcomes = get_sample_outcomes(mnames, clean[ds], attacked[ds][atk], ds_pairs)\n                rand_asr_points.append(asr_from_outcomes(outcomes))\n                rand_boot_asrs += bootstrap_asr(outcomes, rng)\n            rand_boot_asrs /= 100\n            strat_boot[\"random\"] = rand_boot_asrs\n            rand_asr_point = float(np.mean(rand_asr_points))\n\n            # ── Strategy-level bootstrap (vectorized) ──\n            print(\"  Computing all panel ASRs for strategy bootstrap...\")\n            panel_asr_arr = np.zeros(n_panels)\n            for ci, combo in enumerate(all_combos):\n                mnames = combo_to_names(combo)\n                oc = get_sample_outcomes(mnames, clean[ds], attacked[ds][atk], ds_pairs)\n                panel_asr_arr[ci] = asr_from_outcomes(oc)\n\n            print(\"  Strategy-level bootstrap...\")\n            boot_panel_idx = rng.integers(0, n_panels, size=(B, n_panels))\n\n            strat_level_boot = {}\n\n            # min(eta_max): tie-break by max keff\n            boot_eta = eta_max_arr[boot_panel_idx]\n            boot_min_eta = boot_eta.min(axis=1, keepdims=True)\n            boot_keff_all = keff_arr[boot_panel_idx]\n            is_min_eta = (boot_eta == boot_min_eta)\n            boot_keff_masked = np.where(is_min_eta, boot_keff_all, -np.inf)\n            best_in_boot = np.argmax(boot_keff_masked, axis=1)\n            selected = boot_panel_idx[np.arange(B), best_in_boot]\n            strat_level_boot[\"min_eta_max\"] = panel_asr_arr[selected]\n\n            # max(keff)\n            best_keff_in = np.argmax(boot_keff_all, axis=1)\n            selected = boot_panel_idx[np.arange(B), best_keff_in]\n            strat_level_boot[\"max_keff\"] = panel_asr_arr[selected]\n\n            # min(keff)\n            worst_keff_in = np.argmin(boot_keff_all, axis=1)\n            selected = boot_panel_idx[np.arange(B), worst_keff_in]\n            strat_level_boot[\"min_keff\"] = panel_asr_arr[selected]\n\n            # ── Assemble ──\n            cond_result = {\"condition\": cond}\n\n            for sname in [\"min_eta_max\", \"min_keff\", \"max_keff\"]:\n                asr_val = asr_from_outcomes(strat_outcomes[sname])\n                cond_result[sname] = {\n                    \"panel\": strategy_names[sname],\n                    \"asr\": float(asr_val) if not np.isnan(asr_val) else None,\n                    \"sample_bootstrap_ci_95\": ci95(strat_boot[sname]),\n                    \"strategy_bootstrap_ci_95\": ci95(strat_level_boot[sname]),\n                    \"strategy_bootstrap_mean\": float(np.nanmean(strat_level_boot[sname])),\n                }\n\n            cond_result[\"random\"] = {\n                \"asr_mean\": rand_asr_point,\n                \"sample_bootstrap_ci_95\": ci95(rand_boot_asrs),\n            }\n\n            # Pairwise\n            pairwise = {}\n            for pname, s1, s2 in [\n                (\"min_eta_vs_random\", \"min_eta_max\", \"random\"),\n                (\"min_keff_vs_random\", \"min_keff\", \"random\"),\n                (\"min_eta_vs_max_keff\", \"min_eta_max\", \"max_keff\"),\n            ]:\n                b1 = strat_boot[s1]\n                b2 = strat_boot[s2]\n                delta_boot = b1 - b2\n                a1 = asr_from_outcomes(strat_outcomes[s1]) if s1 in strat_outcomes else rand_asr_point\n                a2 = asr_from_outcomes(strat_outcomes[s2]) if s2 in strat_outcomes else rand_asr_point\n                delta_obs = float(a1 - a2)\n                lo, hi = ci95(delta_boot)\n                significant = (lo is not None and hi is not None and not (lo <= 0 <= hi))\n                pairwise[pname] = {\n                    \"delta\": delta_obs if not np.isnan(delta_obs) else None,\n                    \"ci_95\": [lo, hi],\n                    \"significant\": significant,\n                }\n                if significant:\n                    sig_counts[pname] += 1\n\n            cond_result[\"pairwise\"] = pairwise\n            per_condition.append(cond_result)\n\n            for sname in [\"min_eta_max\", \"min_keff\", \"random\", \"max_keff\"]:\n                if sname == \"random\":\n                    print(f\"  {sname:>14}: ASR={cond_result[sname]['asr_mean']:.4f}  \"\n                          f\"sCI={cond_result[sname]['sample_bootstrap_ci_95']}\")\n                else:\n                    print(f\"  {sname:>14}: ASR={cond_result[sname]['asr']:.4f}  \"\n                          f\"sCI={cond_result[sname]['sample_bootstrap_ci_95']}  \"\n                          f\"stCI={cond_result[sname]['strategy_bootstrap_ci_95']}\")\n            for pn, pd in pairwise.items():\n                sig_str = \"***\" if pd[\"significant\"] else \"n.s.\"\n                d = f\"{pd['delta']:.4f}\" if pd['delta'] is not None else \"N/A\"\n                print(f\"  {pn}: Δ={d}  CI={pd['ci_95']}  {sig_str}\")\n\n    output = {\n        \"panel_size\": K,\n        \"n_bootstrap\": B,\n        \"n_models\": len(ALL_MODELS),\n        \"n_total_panels\": n_panels,\n        \"per_condition\": per_condition,\n        \"summary\": {\n            \"n_conditions\": n_conditions,\n            \"min_eta_vs_random_sig\": f\"{sig_counts['min_eta_vs_random']}/{n_conditions}\",\n            \"min_keff_vs_random_sig\": f\"{sig_counts['min_keff_vs_random']}/{n_conditions}\",\n            \"min_eta_vs_max_keff_sig\": f\"{sig_counts['min_eta_vs_max_keff']}/{n_conditions}\",\n        },\n    }\n\n    print(f\"\\n{'='*60}\")\n    print(\"SUMMARY\")\n    for k, v in output[\"summary\"].items():\n        print(f\"  {k}: {v}\")\n\n    out_dir = Path(\"/root/cert_manip_resist_eval/artifacts/results/plan001\")\n    out_dir.mkdir(parents=True, exist_ok=True)\n    out_path = out_dir / \"k5_panel_selection_bootstrap.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)\n    print(f\"\\nSaved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T06:23:53.791077+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T06:23:53.791207+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cd /root/cert_manip_resist_eval && nohup /root/miniconda3/bin/python3 scripts/run_k5_panel_selection_bootstrap.py > /tmp/k5_bootstrap.log 2>&1 & echo \"PID=$!\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cd /root/cert_manip_resist_eval && nohup /root/miniconda3/bin/python3 scripts/run_k5_panel_selection_bootstrap.py > /tmp/k5_bootstrap.log 2>&1 & echo \"PID=$!\""
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T06:23:53.791332+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cd /root/cert_manip_resist_eval && nohup /root/miniconda3/bin/python3 scripts/run_k5_panel_selection_bootstrap.py > /tmp/k5_bootstrap.log 2>&1 & echo \\\"PID=$!\\\"'\\n\\nStdout:\\n\\nPID=155889\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 30.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T06:23:53.791504+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "tail -20 /tmp/k5_bootstrap.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "tail -20 /tmp/k5_bootstrap.log"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T06:23:53.791728+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T06:23:53.791867+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat /tmp/k5_bootstrap.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cat /tmp/k5_bootstrap.log"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T06:23:53.791996+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T06:23:53.792113+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "ps -p 155889 -o pid,etime,command"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "ps -p 155889 -o pid,etime,command"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T06:23:53.792232+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"   PID     ELAPSED COMMAND\\n155889       00:41 bash -c cd /root/cert_manip_resist_eval && nohup /root/miniconda3/bin/python3 scripts/run_k5_panel_selection_bootstrap.py > /tmp/k5_bootstrap.log 2>&1 & echo \\\"PID=$!\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T06:23:53.792362+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "ps aux --forest"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "ps aux --forest"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T06:23:53.792503+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot          1  0.0  0.0   4476  3444 ?        Ss   May22   0:00 bash /init/boot/boot.sh\\nroot       1219  1.7  0.0 718752 24496 ?        Sl   May22  39:13 /bin/supervisord -c /init/supervisor/supervisor.ini\\nroot       1236  0.2  0.0 6894804 101672 ?      Sl   May22   6:08  \\\\_ autopanel serve --work-dir=/root/autodl-tmp --cache-dir=/root/autodl-tmp\\nroot       1242  0.0  0.0  15444  9508 ?        S    May22   0:00  \\\\_ sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups\\nroot     150070  0.0  0.0  16692 10636 ?        Ss   11:43   0:00  |   \\\\_ sshd: root@notty\\nroot     155457  0.0  0.0  16704 10744 ?        Ss   14:17   0:00  |   \\\\_ sshd: root@notty\\nroot     155477  0.0  0.0  16692 10896 ?        Ss   14:17   0:00  |   \\\\_ sshd: root@notty\\nroot     155511  0.0  0.0  16704 10928 ?        Ss   14:18   0:00  |   \\\\_ sshd: root@notty\\nroot     155977  0.1  0.0  16692 10528 ?        Ss   14:22   0:00  |   \\\\_ sshd: root@notty\\nroot     155993  0.2  0.0  16692 10712 ?        Ss   14:23   0:00  |   \\\\_ sshd: root@notty\\nroot     156018  0.0  0.0   7064  1588 ?        Rs   14:23   0:00  |       \\\\_ ps aux --forest\\nroot       1243  0.0  0.0 3385888 17708 ?       Sl   May22   0:34  \\\\_ proxy -c /init/proxy/proxy-hot-backup.ini\\nroot       1246  0.0  0.0 3756596 18456 ?       Sl   May22   1:11  \\\\_ proxy -c /init/proxy/proxy.ini\\nroot      97193  0.0  0.0 187668 103004 ?       S    May22   0:01  \\\\_ /root/miniconda3/bin/python /root/miniconda3/bin/jupyter-lab --allow-root --config=/init/jupyter/jupyter_config.py\\nroot     155756  0.0  0.0   4364  1772 ?        S    14:22   0:00 bash -c cd /root/cert_manip_resist_eval && nohup /root/miniconda3/bin/python3 scripts/run_k5_aggregation_bootstrap.py --B 999 > /tmp/k5_agg_boot_test.log 2>&1 & echo \\\"PID=$!\\\"\\nroot     155757  618  0.0 5749384 250864
…[truncated 605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T06:23:53.792699+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "tail -30 /tmp/k5_bootstrap.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "tail -30 /tmp/k5_bootstrap.log"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T06:23:53.792872+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     min_eta_max: ASR=0.4721  sCI=[0.41263940520446096, 0.5315985130111525]  stCI=[0.47058823529411764, 0.4721189591078067]\\n        min_keff: ASR=0.4721  sCI=[0.41263940520446096, 0.5315985130111525]  stCI=[0.4721189591078067, 0.4721189591078067]\\n          random: ASR=0.4792  sCI=[0.4734178113815661, 0.4849837301706295]\\n        max_keff: ASR=0.5480  sCI=[0.488, 0.608]  stCI=[0.5396825396825397, 0.5483870967741935]\\n  min_eta_vs_random: Δ=-0.0070  CI=[-0.0661528597618959, 0.051000327833789924]  n.s.\\n  min_keff_vs_random: Δ=-0.0070  CI=[-0.06693159901075893, 0.05244203641384003]  n.s.\\n  min_eta_vs_max_keff: Δ=-0.0759  CI=[-0.15880966542750927, 0.008446096654275093]  n.s.\\n\\n============================================================\\n[12/12] arc_challenge×authority_bias\\n  Computing panel properties...\\n  Sample-level bootstrap...\\n  Computing all panel ASRs for strategy bootstrap...\\n  Strategy-level bootstrap...\\n     min_eta_max: ASR=0.0000  sCI=[0.0, 0.0]  stCI=[0.0, 0.0]\\n        min_keff: ASR=0.0000  sCI=[0.0, 0.0]  stCI=[0.0, 0.0]\\n          random: ASR=0.0044  sCI=[0.0036397620018713173, 0.005177392858482373]\\n        max_keff: ASR=0.0200  sCI=[0.004, 0.04]  stCI=[0.007936507936507936, 0.02]\\n  min_eta_vs_random: Δ=-0.0044  CI=[-0.005177392858482373, -0.0036397620018713177]  ***\\n  min_keff_vs_random: Δ=-0.0044  CI=[-0.005177392858482373, -0.0036397620018713177]  ***\\n  min_eta_vs_max_keff: Δ=-0.0200  CI=[-0.04, -0.004]  ***\\n\\n============================================================\\nSUMMARY\\n  n_conditions: 12\\n  min_eta_vs_random_sig: 10/12\\n  min_keff_vs_random_sig: 10/12\\n  min_eta_vs_max_keff_sig: 11/12\\n\\nSaved: /root/cert_manip_resist_eval/artifacts/results/plan001/k5_panel_selection_bootstrap.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T06:23:53.793033+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "seetacloud-rtx6000",
  "command": "cat /root/cert_manip_resist_eval/artifacts/results/plan001/k5_panel_selection_bootstrap.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "seetacloud-rtx6000",
    "command": "cat /root/cert_manip_resist_eval/artifacts/results/plan001/k5_panel_selection_bootstrap.json"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T06:23:53.793354+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"panel_size\\\": 5,\\n  \\\"n_bootstrap\\\": 9999,\\n  \\\"n_models\\\": 15,\\n  \\\"n_total_panels\\\": 3003,\\n  \\\"per_condition\\\": [\\n    {\\n      \\\"condition\\\": \\\"mmlu×prompt_injection\\\",\\n      \\\"min_eta_max\\\": {\\n        \\\"panel\\\": [\\n          \\\"claude-opus-4-6\\\",\\n          \\\"gpt-5.5\\\",\\n          \\\"gemini-3.1-pro-preview\\\",\\n          \\\"gpt-4.1\\\",\\n          \\\"gemini-3.5-flash\\\"\\n        ],\\n        \\\"asr\\\": 0.0,\\n        \\\"sample_bootstrap_ci_95\\\": [\\n          0.0,\\n          0.0\\n        ],\\n        \\\"strategy_bootstrap_ci_95\\\": [\\n          0.0,\\n          0.013824884792626729\\n        ],\\n        \\\"strategy_bootstrap_mean\\\": 0.004377857615339356\\n      },\\n      \\\"min_keff\\\": {\\n        \\\"panel\\\": [\\n          \\\"claude-opus-4-6\\\",\\n          \\\"gpt-5.5\\\",\\n          \\\"gemini-3.1-pro-preview\\\",\\n          \\\"gpt-4.1\\\",\\n          \\\"gemini-3.5-flash\\\"\\n        ],\\n        \\\"asr\\\": 0.0,\\n        \\\"sample_bootstrap_ci_95\\\": [\\n          0.0,\\n          0.0\\n        ],\\n        \\\"strategy_bootstrap_ci_95\\\": [\\n          0.0,\\n          0.0\\n        ],\\n        \\\"strategy_bootstrap_mean\\\": 3.390169525427119e-06\\n      },\\n      \\\"max_keff\\\": {\\n        \\\"panel\\\": [\\n          \\\"qwen2.5-14b\\\",\\n          \\\"llama3.1-8b\\\",\\n          \\\"gpt-4.1-nano\\\",\\n          \\\"gpt-4.1-mini\\\",\\n          \\\"claude-3-haiku\\\"\\n        ],\\n        \\\"asr\\\": 0.4329004329004329,\\n        \\\"sample_bootstrap_ci_95\\\": [\\n          0.36796536796536794,\\n          0.49783549783549785\\n        ],\\n        \\\"strategy_bootstrap_ci_95\\\": [\\n          0.3070539419087137,\\n          0.5064935064935064\\n        ],\\n        \\\"strategy_bootstrap_mean\\\": 0.4404075916494705\\n      },\\n      \\\"random\\\": {\\n        \\\"asr_mean\\\":
…[truncated 8002 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T06:23:53.793537+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/results/plan001",
  "description": "Create local artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/results/plan001",
    "description": "Create local artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T06:23:53.793682+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-23T06:23:53.793813+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "scp seetacloud-rtx6000:/root/cert_manip_resist_eval/artifacts/results/plan001/k5_panel_selection_bootstrap.json /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/results/plan001/k5_panel_selection_bootstrap.json",
  "description": "Download bootstrap results to local",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "Bash",
  "tool_args": {
    "command": "scp seetacloud-rtx6000:/root/cert_manip_resist_eval/artifacts/results/plan001/k5_panel_selection_bootstrap.json /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/results/plan001/k5_panel_selection_bootstrap.json",
    "description": "Download bootstrap results to local",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-23T06:23:53.793931+00:00_

Warning: Permanently added '[connect.westd.seetacloud.com]:49657' (ED25519) to the list of known hosts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-23T06:23:53.794051+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "k5_panel_selection_bootstrap",
  "type": "data",
  "description": "K=5 panel selection bootstrap CIs (B=9999). Sample-level and strategy-level bootstrap for 4 strategies across 12 conditions. Pairwise significance tests: min(η_max) vs random 10/12 sig, min(K_eff) vs random 10/12 sig, min(η_max) vs max(K_eff) 11/12 sig.",
  "project": "cert_manip_resist_eval",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/results/plan001/k5_panel_selection_bootstrap.json",
  "tags": "['bootstrap', 'panel_selection', 'K5', 'significance']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "k5_panel_selection_bootstrap",
    "type": "data",
    "description": "K=5 panel selection bootstrap CIs (B=9999). Sample-level and strategy-level bootstrap for 4 strategies across 12 conditions. Pairwise significance tests: min(η_max) vs random 10/12 sig, min(K_eff) vs random 10/12 sig, min(η_max) vs max(K_eff) 11/12 sig.",
    "project": "cert_manip_resist_eval",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/results/plan001/k5_panel_selection_bootstrap.json",
    "tags": "['bootstrap', 'panel_selection', 'K5', 'significance']"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-23T06:23:53.794205+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260523_09d62f\", \"name\": \"k5_panel_selection_bootstrap\", \"type\": \"data\", \"description\": \"K=5 panel selection bootstrap CIs (B=9999). Sample-level and strategy-level bootstrap for 4 strategies across 12 conditions. Pairwise significance tests: min(η_max) vs random 10/12 sig, min(K_eff) vs random 10/12 sig, min(η_max) vs max(K_eff) 11/12 sig.\", \"path\": \"projects/cert_manip_resist_eval/artifacts/_project/data/k5_panel_selection_bootstrap.json\", \"url\": null, \"project\": \"cert_manip_resist_eval\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-23T06:23:43.585508+00:00\", \"tags\": [\"bootstrap\", \"panel_selection\", \"K5\", \"significance\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-23T06:23:53.794369+00:00_

Bootstrap 分析完成。结果摘要：

**Pairwise 显著性（B=9999, 95% CI）：**
| 对比 | 显著 conditions |
|---|---|
| min(η_max) vs random | **10/12** |
| min(K_eff) vs random | **10/12** |
| min(η_max) vs max(K_eff) | **11/12** |

**不显著的 2 个 condition** 均为 `arc_challenge×position_bias` 和 `arc_challenge×verbosity_bias`——这两个 condition 下所有策略的 ASR 都很高（~0.47），min(η_max) 选出的 panel 也无法有效抵抗，导致策略间差异不显著。

**Strategy-level bootstrap**（模拟 panel pool 不确定性）也确认 min(η_max) 策略稳定，CI 非常窄（大多数 condition 下 strategy bootstrap CI 几乎是点估计），说明该策略对 panel pool 的扰动不敏感。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_k5-panel-selection-bootstrap_20260523T061740"
}
```

</details>

---
