# code update analyze script

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/chats/worker_code_update-analyze-script_20260515T110435.jsonl`
- **Structured JSON:** [`e67c73d77c4e7e03e99c.json`](../../sessions/e6/e67c73d77c4e7e03e99c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

45 recorded events

### Tool call

_source line 1 · 2026-05-15T11:16:07.411274+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T11:16:07.411593+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T11:16:07.411773+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "cat /root/vla-ssd/scripts/analyze_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "cat /root/vla-ssd/scripts/analyze_results.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T11:16:07.412114+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"analyze_results.py — Compare probe results across models and visualize.\\n\\nInput:  Multiple result directories (from train_probes.py)\\nOutput: Comparison tables, plots, PASS/FAIL judgment\\n\\nUsage:\\n  python analyze_results.py \\\\\\n    --results_dirs trained:results/trained/,untrained:results/untrained/,dinov2:results/dinov2/ \\\\\\n    --output_dir results/analysis/\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport glob\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"Analyze and compare probe results\\\")\\n    p.add_argument(\\\"--results_dirs\\\", required=True,\\n                   help=\\\"Comma-separated name:path pairs, e.g. trained:results/trained/\\\")\\n    p.add_argument(\\\"--output_dir\\\", required=True)\\n    p.add_argument(\\\"--probe_type\\\", default=\\\"temporal_distance\\\",\\n                   choices=[\\\"temporal_distance\\\", \\\"subtask_predicate\\\"])\\n    return p.parse_args()\\n\\n\\ndef parse_results_dirs(s):\\n    d = {}\\n    for entry in s.split(\\\",\\\"):\\n        name, path = entry.strip().split(\\\":\\\")\\n        d[name.strip()] = path.strip()\\n    return d\\n\\n\\ndef load_results(results_dir, probe_type):\\n    \\\"\\\"\\\"Load probe results from a directory.\\\"\\\"\\\"\\n    probe_dir = os.path.join(results_dir, probe_type)\\n    summary_path = os.path.join(probe_dir, \\\"summary.json\\\")\\n    if os.path.exists(summary_path):\\n        with open(summary_path) as f:\\n            return json.load(f)\\n\\n    results = {}\\n    for p in sorted(glob.glob(os.path.join(probe_dir, \\\"layer_*.json\\\"))):\\n        with open(p) as f:\\n            m = json.load(f)\\n        key = m.get(\\\"layer\\\", Path(p).stem.replace(\\\"layer_\\\", \\\"\\\"))\\n        results[s
…[truncated 7387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T11:16:07.412345+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "wc -l /root/vla-ssd/scripts/analyze_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "wc -l /root/vla-ssd/scripts/analyze_results.py"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T11:16:07.412478+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "head -200 /root/vla-ssd/scripts/analyze_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "head -200 /root/vla-ssd/scripts/analyze_results.py"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T11:16:07.412606+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"377 /root/vla-ssd/scripts/analyze_results.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T11:16:07.412852+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"analyze_results.py — Compare probe results across models and visualize.\\n\\nInput:  Multiple result directories (from train_probes.py)\\nOutput: Comparison tables, plots, PASS/FAIL judgment\\n\\nUsage:\\n  python analyze_results.py \\\\\\n    --results_dirs trained:results/trained/,untrained:results/untrained/,dinov2:results/dinov2/ \\\\\\n    --output_dir results/analysis/\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport glob\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\n\\n\\ndef parse_args():\\n    p = argparse.ArgumentParser(description=\\\"Analyze and compare probe results\\\")\\n    p.add_argument(\\\"--results_dirs\\\", required=True,\\n                   help=\\\"Comma-separated name:path pairs, e.g. trained:results/trained/\\\")\\n    p.add_argument(\\\"--output_dir\\\", required=True)\\n    p.add_argument(\\\"--probe_type\\\", default=\\\"temporal_distance\\\",\\n                   choices=[\\\"temporal_distance\\\", \\\"subtask_predicate\\\"])\\n    return p.parse_args()\\n\\n\\ndef parse_results_dirs(s):\\n    d = {}\\n    for entry in s.split(\\\",\\\"):\\n        name, path = entry.strip().split(\\\":\\\")\\n        d[name.strip()] = path.strip()\\n    return d\\n\\n\\ndef load_results(results_dir, probe_type):\\n    \\\"\\\"\\\"Load probe results from a directory.\\\"\\\"\\\"\\n    probe_dir = os.path.join(results_dir, probe_type)\\n    summary_path = os.path.join(probe_dir, \\\"summary.json\\\")\\n    if os.path.exists(summary_path):\\n        with open(summary_path) as f:\\n            return json.load(f)\\n\\n    results = {}\\n    for p in sorted(glob.glob(os.path.join(probe_dir, \\\"layer_*.json\\\"))):\\n        with open(p) as f:\\n            m = json.load(f)\\n        key = m.get(\\\"layer\\\", Path(p).stem.replace(\\\"layer_\\\", \\\"\\\"))\\n        results[s
…[truncated 5797 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T11:16:07.413082+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "tail -n +200 /root/vla-ssd/scripts/analyze_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "tail -n +200 /root/vla-ssd/scripts/analyze_results.py"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T11:16:07.413317+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    ax.set_title(f\\\"Sub-task Predicate AUC ({name})\\\")\\n    fig.colorbar(im, ax=ax, label=\\\"AUC-ROC\\\")\\n\\n    path = os.path.join(output_dir, f\\\"subtask_auc_{name}.png\\\")\\n    fig.savefig(path, dpi=150, bbox_inches=\\\"tight\\\")\\n    fig.savefig(path.replace(\\\".png\\\", \\\".pdf\\\"), bbox_inches=\\\"tight\\\")\\n    plt.close(fig)\\n    print(f\\\"Saved {path}\\\")\\n\\n\\n# ============================================================\\n# Judgment\\n# ============================================================\\n\\ndef compute_judgment(all_data):\\n    \\\"\\\"\\\"PASS/FAIL based on three criteria.\\\"\\\"\\\"\\n    criteria = {}\\n\\n    # 1) best rho > 0.3\\n    if \\\"trained\\\" in all_data:\\n        _, rhos = extract_layer_metrics(all_data[\\\"trained\\\"], \\\"spearman_rho\\\")\\n        best_rho = float(rhos.max()) if len(rhos) > 0 else 0.0\\n        layers, _ = extract_layer_metrics(all_data[\\\"trained\\\"], \\\"spearman_rho\\\")\\n        best_layer = int(layers[np.argmax(rhos)]) if len(rhos) > 0 else -1\\n    else:\\n        best_rho, best_layer = 0.0, -1\\n\\n    criteria[\\\"best_rho\\\"] = best_rho\\n    criteria[\\\"best_layer\\\"] = best_layer\\n    criteria[\\\"rho_pass\\\"] = best_rho > 0.3\\n\\n    # 2) delta-rho > 0.1\\n    max_delta = 0.0\\n    if \\\"trained\\\" in all_data and \\\"untrained\\\" in all_data:\\n        l_tr, rho_tr = extract_layer_metrics(all_data[\\\"trained\\\"], \\\"spearman_rho\\\")\\n        l_un, rho_un = extract_layer_metrics(all_data[\\\"untrained\\\"], \\\"spearman_rho\\\")\\n        tr_map = dict(zip(l_tr.tolist(), rho_tr.tolist()))\\n        un_map = dict(zip(l_un.tolist(), rho_un.tolist()))\\n        common = set(l_tr.tolist()) & set(l_un.tolist())\\n        if common:\\n            max_delta = max(tr_map[l] - un_map[l] for l in common)\\n\\n    criteria[\\\"max_delta_rho\\\"] = max_delta\\n    criteria[\\\"delta_pass\\\"] = max_delta > 0.
…[truncated 5388 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T11:16:07.413737+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/tmp/analyze_results_new.py",
  "content": "\"\"\"analyze_results.py — Compare probe results across models and visualize.\n\nInput:  Multiple result directories (from train_probes.py)\nOutput: Comparison tables, plots, PASS/FAIL judgment\n\nUsage:\n  python analyze_results.py \\\n    --results_dirs trained:results/trained/,untrained:results/untrained/,dinov2:results/dinov2/ \\\n    --output_dir results/analysis/\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport glob\nfrom pathlib import Path\n\nimport numpy as np\n\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"Analyze and compare probe results\")\n    p.add_argument(\"--results_dirs\", required=True,\n                   help=\"Comma-separated name:path pairs, e.g. trained:results/trained/\")\n    p.add_argument(\"--output_dir\", required=True)\n    p.add_argument(\"--probe_type\", default=\"temporal_distance\",\n                   choices=[\"temporal_distance\", \"subtask_predicate\"])\n    return p.parse_args()\n\n\ndef parse_results_dirs(s):\n    d = {}\n    for entry in s.split(\",\"):\n        name, path = entry.strip().split(\":\")\n        d[name.strip()] = path.strip()\n    return d\n\n\ndef load_results(results_dir, probe_type):\n    \"\"\"Load probe results from a directory.\"\"\"\n    probe_dir = os.path.join(results_dir, probe_type)\n    summary_path = os.path.join(probe_dir, \"summary.json\")\n    if os.path.exists(summary_path):\n        with open(summary_path) as f:\n            return json.load(f)\n\n    results = {}\n    for p in sorted(glob.glob(os.path.join(probe_dir, \"layer_*.json\"))):\n        with open(p) as f:\n            m = json.load(f)\n        key = m.get(\"layer\", Path(p).stem.replace(\"layer_\", \"\"))\n        results[str(key)] = m\n    return {\"results\": results}\n\n\ndef load_oracle(results_dirs):\n    \"\"\"Auto-detect oracle results from any provided directory.\"\"\"\n    for path in results_dirs.values():\n        oracle_dir = os.path.join(path, \"oracle\")\n        summary = os.path.join(oracle_dir, \"summary.json\")\n        if os.path.exists(summary):\n            with open(summary) as f:\n                data = json.load(f)\n            r = data.get(\"results\", {})\n            if \"oracle\" in r:\n                return r[\"oracle\"].get(\"spearman_rho\")\n    return None\n\n\ndef _sort_key(x):\n    try:\n        return (0, int(x))\n    except ValueError:\n        return (1, x)\n\n\ndef extract_layer_metrics(data, metric=\"spearman_rho\"):\n    results = data.get(\"results\", {})\n    layers, values = [], []\n    for k, v in sorted(results.items(), key=lambda x: _sort_key(x[0])):\n        if k == \"oracle\":\n            continue\n        val = v.get(metric)\n        if val is not None and not (isinstance(val, float) and np.isnan(val)):\n            layers.append(int(k))\n            values.append(float(val))\n    return np.array(layers), np.array(values)\n\n\n# ============================================================\n# Plots\n# ============================================================\n\nCOLORS = {\n    \"trained\": \"#2196F3\", \"untrained\": \"#F44336\",\n    \"dinov2\": \"#4CAF50\", \"oracle\": \"#FF9800\",\n}\nMARKERS = {\"trained\": \"o\", \"untrained\": \"s\", \"dinov2\": \"^\", \"oracle\": \"D\"}\n\n\ndef plot_layer_rho(all_data, oracle_rho, output_dir):\n    fig, ax = plt.subplots(figsize=(10, 5))\n\n    for name, data in all_data.items():\n        layers, rhos = extract_layer_metrics(data, \"spearman_rho\")\n        if len(layers) == 0:\n            continue\n        ax.plot(layers, rhos,\n                marker=MARKERS.get(name, \"o\"),\n                color=COLORS.get(name, \"#999\"),\n                label=name, linewidth=2, markersize=5)\n\n    if oracle_rho is not None:\n        ax.axhline(y=oracle_rho, color=COLORS[\"oracle\"],\n                   linestyle=\"--\", label=f\"oracle (rho={oracle_rho:.3f})\", alpha=0.7)\n\n    ax.set_xlabel(\"Layer\")\n    ax.set_ylabel(\"Spearman rho\")\n    ax.set_title(\"Temporal Distance Probe: Layer-wise Spearman rho\")\n    ax.legend()\n    ax.grid(True, alpha=0.3)\n\n    path = os.path.join(output_dir, \"layer_rho.png\")\n    fig.savefig(path, dpi=150, bbox_inches=\"tight\")\n    fig.savefig(path.replace(\".png\", \".pdf\"), bbox_inches=\"tight\")\n    plt.close(fig)\n    print(f\"Saved {path}\")\n\n\ndef plot_delta_rho(all_data, output_dir):\n    if \"trained\" not in all_data or \"untrained\" not in all_data:\n        print(\"Skipping delta-rho plot (need trained + untrained)\")\n        return\n\n    l_tr, rho_tr = extract_layer_metrics(all_data[\"trained\"], \"spearman_rho\")\n    l_un, rho_un = extract_layer_metrics(all_data[\"untrained\"], \"spearman_rho\")\n\n    tr_map = dict(zip(l_tr.tolist(), rho_tr.tolist()))\n    un_map = dict(zip(l_un.tolist(), rho_un.tolist()))\n    common = sorted(set(l_tr.tolist()) & set(l_un.tolist()))\n    if not common:\n        return\n\n    layers = np.array(common)\n    deltas = np.array([tr_map[l] - un_map[l] for l in common])\n\n    fig, ax = plt.subplots(figsize=(10, 5))\n    colors = [\"#2196F3\" if d >= 0 else \"#F44336\" for d in deltas]\n    ax.bar(layers, deltas, color=colors, width=0.8)\n    ax.axhline(y=0.1, color=\"green\", linestyle=\"--\", alpha=0.5, label=\"threshold=0.1\")\n    ax.axhline(y=0, color=\"black\", linewidth=0.5)\n    ax.set_xlabel(\"Layer\")\n    ax.set_ylabel(\"Delta-rho (trained - untrained)\")\n    ax.set_title(\"Temporal Distance Probe: Delta-rho per Layer\")\n    ax.legend()\n    ax.grid(True, alpha=0.3)\n\n    path = os.path.join(output_dir, \"delta_rho.png\")\n    fig.savefig(path, dpi=150, bbox_inches=\"tight\")\n    fig.savefig(path.replace(\".png\", \".pdf\"), bbox_inches=\"tight\")\n    plt.close(fig)\n    print(f\"Saved {path}\")\n\n\ndef plot_subtask_auc_heatmap(data, output_dir, name=\"trained\"):\n    results = data.get(\"results\", {})\n    layers = sorted([int(k) for k in results if k != \"oracle\"])\n    if not layers:\n        return\n\n    pred_names = None\n    for v in results.values():\n        if \"predicate_names\" in v:\n            pred_names = v[\"predicate_names\"]\n            break\n    if pred_names is None:\n        return\n\n    n_pred = len(pred_names)\n    heatmap = np.full((len(layers), n_pred), np.nan)\n\n    for li, layer in enumerate(layers):\n        auc = results[str(layer)].get(\"auc_per_predicate\", {})\n        for k in range(n_pred):\n            val = auc.get(str(k), np.nan)\n            heatmap[li, k] = val\n\n    fig, ax = plt.subplots(figsize=(max(8, n_pred), max(6, len(layers) * 0.3)))\n    im = ax.imshow(heatmap, aspect=\"auto\", cmap=\"YlOrRd\", vmin=0.5, vmax=1.0)\n    ax.set_xticks(range(n_pred))\n    ax.set_xticklabels(pred_names, rotation=45, ha=\"right\", fontsize=8)\n    ax.set_yticks(range(len(layers)))\n    ax.set_yticklabels(layers)\n    ax.set_xlabel(\"Predicate\")\n    ax.set_ylabel(\"Layer\")\n    ax.set_title(f\"Sub-task Predicate AUC ({name})\")\n    fig.colorbar(im, ax=ax, label=\"AUC-ROC\")\n\n    path = os.path.join(output_dir, f\"subtask_auc_{name}.png\")\n    fig.savefig(path, dpi=150, bbox_inches=\"tight\")\n    fig.savefig(path.replace(\".png\", \".pdf\"), bbox_inches=\"tight\")\n    plt.close(fig)\n    print(f\"Saved {path}\")\n\n\ndef plot_per_layer_rho_profile(all_data, output_dir):\n    fig, ax = plt.subplots(figsize=(10, 5))\n\n    for name in [\"trained\", \"untrained\"]:\n        if name not in all_data:\n            continue\n        layers, rhos = extract_layer_metrics(all_data[name], \"spearman_rho\")\n        if len(layers) == 0:\n            continue\n        ax.plot(layers, rhos,\n                marker=MARKERS.get(name, \"o\"),\n                color=COLORS.get(name, \"#999\"),\n                label=name, linewidth=2, markersize=5)\n\n    if \"dinov2\" in all_data:\n        _, rho_dino = extract_layer_metrics(all_data[\"dinov2\"], \"spearman_rho\")\n        if len(rho_dino) > 0:\n            dino_val = float(rho_dino.max())\n            ax.axhline(y=dino_val, color=COLORS.get(\"dinov2\", \"#4CAF50\"),\n                       linestyle=\"--\", linewidth=2,\n                       label=f\"DINO-V2 (rho={dino_val:.3f})\")\n\n    ax.set_xlabel(\"Layer Index\")\n    ax.set_ylabel(\"Spearman rho\")\n    ax.set_title(\"Per-layer rho Profile: VLA (trained/untrained) vs DINO-V2\")\n    ax.legend()\n    ax.grid(True, alpha=0.3)\n\n    path = os.path.join(output_dir, \"per_layer_rho_profile.png\")\n    fig.savefig(path, dpi=150, bbox_inches=\"tight\")\n    fig.savefig(path.replace(\".png\", \".pdf\"), bbox_inches=\"tight\")\n    plt.close(fig)\n    print(f\"Saved {path}\")\n\n\n# ============================================================\n# Judgment\n# ============================================================\n\ndef bootstrap_delta_rho(trained_rhos, untrained_rhos, n_bootstrap=1000, seed=42):\n    rng = np.random.RandomState(seed)\n    deltas = []\n    n = len(trained_rhos)\n    for _ in range(n_bootstrap):\n        idx = rng.choice(n, n, replace=True)\n        delta = np.mean(np.array(trained_rhos)[idx]) - np.mean(np.array(untrained_rhos)[idx])\n        deltas.append(delta)\n    deltas = sorted(deltas)\n    ci_lower = deltas[int(0.025 * n_bootstrap)]\n    ci_upper = deltas[int(0.975 * n_bootstrap)]\n    return np.mean(deltas), ci_lower, ci_upper\n\n\ndef compute_judgment(all_data):\n    \"\"\"PASS/FAIL based on three criteria (D001 calibration).\"\"\"\n    criteria = {}\n\n    # 1) best rho > 0.5\n    if \"trained\" in all_data:\n        layers, rhos = extract_layer_metrics(all_data[\"trained\"], \"spearman_rho\")\n        best_rho = float(rhos.max()) if len(rhos) > 0 else 0.0\n        best_layer = int(layers[np.argmax(rhos)]) if len(rhos) > 0 else -1\n    else:\n        best_rho, best_layer = 0.0, -1\n\n    criteria[\"best_rho\"] = best_rho\n    criteria[\"best_layer\"] = best_layer\n    criteria[\"rho_pass\"] = best_rho > 0.5\n\n    # 2) delta-rho > 0.1 with bootstrapped 95% CI excluding 0\n    max_delta = 0.0\n    delta_ci_lower = 0.0\n    delta_ci_upper = 0.0\n    ci_excludes_zero = False\n    if \"trained\" in all_data and \"untrained\" in all_data:\n        l_tr, rho_tr = extract_layer_metrics(all_data[\"trained\"], \"spearman_rho\")\n        l_un, rho_un = extract_layer_metrics(all_data[\"untrained\"], \"spearman_rho\")\n        tr_map = dict(zip(l_tr.tolist(), rho_tr.tolist()))\n        un_map = dict(zip(l_un.tolist(), rho_un.tolist()))\n        common = set(l_tr.tolist()) & set(l_un.tolist())\n        if common:\n            max_delta = max(tr_map[l] - un_map[l] for l in common)\n            trained_rhos = [tr_map[l] for l in sorted(common)]\n            untrained_rhos = [un_map[l] for l in sorted(common)]\n            _, delta_ci_lower, delta_ci_upper = bootstrap_delta_rho(\n                trained_rhos, untrained_rhos\n            )\n            ci_excludes_zero = delta_ci_lower > 0\n\n    criteria[\"max_delta_rho\"] = max_delta\n    criteria[\"delta_ci_lower\"] = delta_ci_lower\n    criteria[\"delta_ci_upper\"] = delta_ci_upper\n    criteria[\"ci_excludes_zero\"] = ci_excludes_zero\n    criteria[\"delta_pass\"] = max_delta > 0.1 and ci_excludes_zero\n\n    # 3) VLA_rho >= DINO_rho OR (subtask_AUC > 0.7 AND subtask_AUC > DINO_subtask_AUC + 0.05)\n    vla_ge_dino = False\n    if \"trained\" in all_data and \"dinov2\" in all_data:\n        _, rho_vla = extract_layer_metrics(all_data[\"trained\"], \"spearman_rho\")\n        _, rho_dino = extract_layer_metrics(all_data[\"dinov2\"], \"spearman_rho\")\n        if len(rho_vla) > 0 and len(rho_dino) > 0:\n            vla_ge_dino = float(rho_vla.max()) >= float(rho_dino.max())\n\n    vla_best_auc = 0.0\n    dino_best_auc = 0.0\n    if \"trained\" in all_data:\n        for v in all_data[\"trained\"].get(\"results\", {}).values():\n            if isinstance(v.get(\"macro_auc\"), (int, float)):\n                vla_best_auc = max(vla_best_auc, v[\"macro_auc\"])\n    if \"dinov2\" in all_data:\n        for v in all_data[\"dinov2\"].get(\"results\", {}).values():\n            if isinstance(v.get(\"macro_auc\"), (int, float)):\n                dino_best_auc = max(dino_best_auc, v[\"macro_auc\"])\n    subtask_pass = vla_best_auc > 0.7 and vla_best_auc > dino_best_auc + 0.05\n\n    criteria[\"vla_ge_dinov2\"] = vla_ge_dino\n    criteria[\"vla_best_auc\"] = vla_best_auc\n    criteria[\"dino_best_auc\"] = dino_best_auc\n    criteria[\"subtask_auc_pass\"] = subtask_pass\n    criteria[\"third_criterion\"] = vla_ge_dino or subtask_pass\n\n    if criteria[\"rho_pass\"] and criteria[\"delta_pass\"] and criteria[\"third_criterion\"]:\n        judgment = \"PASS\"\n    elif criteria[\"delta_pass\"] and not criteria[\"third_criterion\"]:\n        judgment = \"CONDITIONAL\"\n    else:\n        judgment = \"FAIL\"\n\n    reasons = []\n    if not criteria[\"rho_pass\"]:\n        reasons.append(f\"best rho = {best_rho:.4f} <= 0.5\")\n    if not criteria[\"delta_pass\"]:\n        if max_delta <= 0.1:\n            reasons.append(f\"max delta-rho = {max_delta:.4f} <= 0.1\")\n        elif not ci_excludes_zero:\n            reasons.append(f\"delta-rho CI [{delta_ci_lower:.4f}, {delta_ci_upper:.4f}] includes 0\")\n    if not criteria[\"third_criterion\"]:\n        reasons.append(\"VLA < DINO-V2 AND subtask gate not met\")\n\n    return dict(judgment=judgment, criteria=criteria,\n                reasons=reasons if reasons else [\"All criteria met\"])\n\n\n# ============================================================\n# Main\n# ============================================================\n\ndef main():\n    args = parse_args()\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    dirs = parse_results_dirs(args.results_dirs)\n    print(f\"Loading results: {list(dirs.keys())}\")\n\n    all_data = {}\n    for name, path in dirs.items():\n        try:\n            data = load_results(path, args.probe_type)\n            all_data[name] = data\n            n = len(data.get(\"results\", {}))\n            print(f\"  {name}: {n} entries\")\n        except Exception as e:\n            print(f\"  {name}: FAILED ({e})\")\n\n    if not all_data:\n        print(\"No data loaded.\")\n        return\n\n    oracle_rho = load_oracle(dirs)\n    if oracle_rho is not None:\n        print(f\"Oracle rho: {oracle_rho:.4f}\")\n\n    # --- Comparison table ---\n    print(\"\\n=== Layer-wise Spearman rho ===\")\n    names = list(all_data.keys())\n    header = [\"Layer\"] + names\n    print(\" | \".join(f\"{h:>12}\" for h in header))\n    print(\"-\" * (14 * len(header)))\n\n    all_layers = set()\n    for data in all_data.values():\n        layers, _ = extract_layer_metrics(data, \"spearman_rho\")\n        all_layers.update(layers.tolist())\n\n    for layer in sorted(all_layers):\n        row = [f\"{layer:>12}\"]\n        for name in names:\n            layers, rhos = extract_layer_metrics(all_data[name], \"spearman_rho\")\n            lmap = dict(zip(layers.tolist(), rhos.tolist()))\n            val = lmap.get(layer, float(\"nan\"))\n            row.append(f\"{val:>12.4f}\")\n        print(\" | \".join(row))\n\n    print(\"\\n=== Best Layer ===\")\n    for name, data in all_data.items():\n        layers, rhos = extract_layer_metrics(data, \"spearman_rho\")\n        if len(rhos) > 0:\n            bi = int(np.argmax(rhos))\n            print(f\"  {name}: layer {layers[bi]} (rho={rhos[bi]:.4f})\")\n\n    # --- Plots ---\n    if args.probe_type == \"temporal_distance\":\n        plot_layer_rho(all_data, oracle_rho, args.output_dir)\n        plot_delta_rho(all_data, args.output_dir)\n        plot_per_layer_rho_profile(all_data, args.output_dir)\n\n    if args.probe_type == \"subtask_predicate\":\n        for name, data in all_data.items():\n            plot_subtask_auc_heatmap(data, args.output_dir, name)\n\n    # --- Judgment ---\n    judgment = compute_judgment(all_data)\n    print(f\"\\n=== Judgment: {judgment['judgment']} ===\")\n    for k, v in judgment[\"criteria\"].items():\n        print(f\"  {k}: {v}\")\n    for r in judgment[\"reasons\"]:\n        print(f\"  >> {r}\")\n\n    # --- Save ---\n    summary = dict(\n        models=names,\n        probe_type=args.probe_type,\n        judgment=judgment,\n    )\n    for name, data in all_data.items():\n        layers, rhos = extract_layer_metrics(data, \"spearman_rho\")\n        if len(rhos) > 0:\n            bi = int(np.argmax(rhos))\n            summary[name] = dict(best_layer=int(layers[bi]), best_rho=float(rhos[bi]))\n    if oracle_rho is not None:\n        summary[\"oracle_rho\"] = oracle_rho\n\n    with open(os.path.join(args.output_dir, \"summary.json\"), \"w\") as f:\n        json.dump(summary, f, indent=2)\n    print(f\"\\nSaved {args.output_dir}/summary.json\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "Write",
  "tool_args": {
    "file_path": "/tmp/analyze_results_new.py",
    "content": "\"\"\"analyze_results.py — Compare probe results across models and visualize.\n\nInput:  Multiple result directories (from train_probes.py)\nOutput: Comparison tables, plots, PASS/FAIL judgment\n\nUsage:\n  python analyze_results.py \\\n    --results_dirs trained:results/trained/,untrained:results/untrained/,dinov2:results/dinov2/ \\\n    --output_dir results/analysis/\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport glob\nfrom pathlib import Path\n\nimport numpy as np\n\nimport matplotlib\nmatplotlib.use(\"Agg\")\nimport matplotlib.pyplot as plt\n\n\ndef parse_args():\n    p = argparse.ArgumentParser(description=\"Analyze and compare probe results\")\n    p.add_argument(\"--results_dirs\", required=True,\n                   help=\"Comma-separated name:path pairs, e.g. trained:results/trained/\")\n    p.add_argument(\"--output_dir\", required=True)\n    p.add_argument(\"--probe_type\", default=\"temporal_distance\",\n                   choices=[\"temporal_distance\", \"subtask_predicate\"])\n    return p.parse_args()\n\n\ndef parse_results_dirs(s):\n    d = {}\n    for entry in s.split(\",\"):\n        name, path = entry.strip().split(\":\")\n        d[name.strip()] = path.strip()\n    return d\n\n\ndef load_results(results_dir, probe_type):\n    \"\"\"Load probe results from a directory.\"\"\"\n    probe_dir = os.path.join(results_dir, probe_type)\n    summary_path = os.path.join(probe_dir, \"summary.json\")\n    if os.path.exists(summary_path):\n        with open(summary_path) as f:\n            return json.load(f)\n\n    results = {}\n    for p in sorted(glob.glob(os.path.join(probe_dir, \"layer_*.json\"))):\n        with open(p) as f:\n            m = json.load(f)\n        key = m.get(\"layer\", Path(p).stem.replace(\"layer_\", \"\"))\n        results[str(key)] = m\n    return {\"results\": results}\n\n\ndef load_oracle(results_dirs):\n    \"\"\"Auto-detect oracle results from any provided directory.\"\"\"\n    for path in results_dirs.values():\n        oracle_dir = os.path.join(path, \"oracle\")\n        summary = os.path.join(oracle_dir, \"summary.json\")\n        if os.path.exists(summary):\n            with open(summary) as f:\n                data = json.load(f)\n            r = data.get(\"results\", {})\n            if \"oracle\" in r:\n                return r[\"oracle\"].get(\"spearman_rho\")\n    return None\n\n\ndef _sort_key(x):\n    try:\n        return (0, int(x))\n    except ValueError:\n        return (1, x)\n\n\ndef extract_layer_metrics(data, metric=\"spearman_rho\"):\n    results = data.get(\"results\", {})\n    layers, values = [], []\n    for k, v in sorted(results.items(), key=lambda x: _sort_key(x[0])):\n        if k == \"oracle\":\n            continue\n        val = v.get(metric)\n        if val is not None and not (isinstance(val, float) and np.isnan(val)):\n            layers.append(int(k))\n            values.append(float(val))\n    return np.array(layers), np.array(values)\n\n\n# ============================================================\n# Plots\n# ============================================================\n\nCOLORS = {\n    \"trained\": \"#2196F3\", \"untrained\": \"#F44336\",\n    \"dinov2\": \"#4CAF50\", \"oracle\": \"#FF9800\",\n}\nMARKERS = {\"trained\": \"o\", \"untrained\": \"s\", \"dinov2\": \"^\", \"oracle\": \"D\"}\n\n\ndef plot_layer_rho(all_data, oracle_rho, output_dir):\n    fig, ax = plt.subplots(figsize=(10, 5))\n\n    for name, data in all_data.items():\n        layers, rhos = extract_layer_metrics(data, \"spearman_rho\")\n        if len(layers) == 0:\n            continue\n        ax.plot(layers, rhos,\n                marker=MARKERS.get(name, \"o\"),\n                color=COLORS.get(name, \"#999\"),\n                label=name, linewidth=2, markersize=5)\n\n    if oracle_rho is not None:\n        ax.axhline(y=oracle_rho, color=COLORS[\"oracle\"],\n                   linestyle=\"--\", label=f\"oracle (rho={oracle_rho:.3f})\", alpha=0.7)\n\n    ax.set_xlabel(\"Layer\")\n    ax.set_ylabel(\"Spearman rho\")\n    ax.set_title(\"Temporal Distance Probe: Layer-wise Spearman rho\")\n    ax.legend()\n    ax.grid(True, alpha=0.3)\n\n    path = os.path.join(output_dir, \"layer_rho.png\")\n    fig.savefig(path, dpi=150, bbox_inches=\"tight\")\n    fig.savefig(path.replace(\".png\", \".pdf\"), bbox_inches=\"tight\")\n    plt.close(fig)\n    print(f\"Saved {path}\")\n\n\ndef plot_delta_rho(all_data, output_dir):\n    if \"trained\" not in all_data or \"untrained\" not in all_data:\n        print(\"Skipping delta-rho plot (need trained + untrained)\")\n        return\n\n    l_tr, rho_tr = extract_layer_metrics(all_data[\"trained\"], \"spearman_rho\")\n    l_un, rho_un = extract_layer_metrics(all_data[\"untrained\"], \"spearman_rho\")\n\n    tr_map = dict(zip(l_tr.tolist(), rho_tr.tolist()))\n    un_map = dict(zip(l_un.tolist(), rho_un.tolist()))\n    common = sorted(set(l_tr.tolist()) & set(l_un.tolist()))\n    if not common:\n        return\n\n    layers = np.array(common)\n    deltas = np.array([tr_map[l] - un_map[l] for l in common])\n\n    fig, ax = plt.subplots(figsize=(10, 5))\n    colors = [\"#2196F3\" if d >= 0 else \"#F44336\" for d in deltas]\n    ax.bar(layers, deltas, color=colors, width=0.8)\n    ax.axhline(y=0.1, color=\"green\", linestyle=\"--\", alpha=0.5, label=\"threshold=0.1\")\n    ax.axhline(y=0, color=\"black\", linewidth=0.5)\n    ax.set_xlabel(\"Layer\")\n    ax.set_ylabel(\"Delta-rho (trained - untrained)\")\n    ax.set_title(\"Temporal Distance Probe: Delta-rho per Layer\")\n    ax.legend()\n    ax.grid(True, alpha=0.3)\n\n    path = os.path.join(output_dir, \"delta_rho.png\")\n    fig.savefig(path, dpi=150, bbox_inches=\"tight\")\n    fig.savefig(path.replace(\".png\", \".pdf\"), bbox_inches=\"tight\")\n    plt.close(fig)\n    print(f\"Saved {path}\")\n\n\ndef plot_subtask_auc_heatmap(data, output_dir, name=\"trained\"):\n    results = data.get(\"results\", {})\n    layers = sorted([int(k) for k in results if k != \"oracle\"])\n    if not layers:\n        return\n\n    pred_names = None\n    for v in results.values():\n        if \"predicate_names\" in v:\n            pred_names = v[\"predicate_names\"]\n            break\n    if pred_names is None:\n        return\n\n    n_pred = len(pred_names)\n    heatmap = np.full((len(layers), n_pred), np.nan)\n\n    for li, layer in enumerate(layers):\n        auc = results[str(layer)].get(\"auc_per_predicate\", {})\n        for k in range(n_pred):\n            val = auc.get(str(k), np.nan)\n            heatmap[li, k] = val\n\n    fig, ax = plt.subplots(figsize=(max(8, n_pred), max(6, len(layers) * 0.3)))\n    im = ax.imshow(heatmap, aspect=\"auto\", cmap=\"YlOrRd\", vmin=0.5, vmax=1.0)\n    ax.set_xticks(range(n_pred))\n    ax.set_xticklabels(pred_names, rotation=45, ha=\"right\", fontsize=8)\n    ax.set_yticks(range(len(layers)))\n    ax.set_yticklabels(layers)\n    ax.set_xlabel(\"Predicate\")\n    ax.set_ylabel(\"Layer\")\n    ax.set_title(f\"Sub-task Predicate AUC ({name})\")\n    fig.colorbar(im, ax=ax, label=\"AUC-ROC\")\n\n    path = os.path.join(output_dir, f\"subtask_auc_{name}.png\")\n    fig.savefig(path, dpi=150, bbox_inches=\"tight\")\n    fig.savefig(path.replace(\".png\", \".pdf\"), bbox_inches=\"tight\")\n    plt.close(fig)\n    print(f\"Saved {path}\")\n\n\ndef plot_per_layer_rho_profile(all_data, output_dir):\n    fig, ax = plt.subplots(figsize=(10, 5))\n\n    for name in [\"trained\", \"untrained\"]:\n        if name not in all_data:\n            continue\n        layers, rhos = extract_layer_metrics(all_data[name], \"spearman_rho\")\n        if len(layers) == 0:\n            continue\n        ax.plot(layers, rhos,\n                marker=MARKERS.get(name, \"o\"),\n                color=COLORS.get(name, \"#999\"),\n                label=name, linewidth=2, markersize=5)\n\n    if \"dinov2\" in all_data:\n        _, rho_dino = extract_layer_metrics(all_data[\"dinov2\"], \"spearman_rho\")\n        if len(rho_dino) > 0:\n            dino_val = float(rho_dino.max())\n            ax.axhline(y=dino_val, color=COLORS.get(\"dinov2\", \"#4CAF50\"),\n                       linestyle=\"--\", linewidth=2,\n                       label=f\"DINO-V2 (rho={dino_val:.3f})\")\n\n    ax.set_xlabel(\"Layer Index\")\n    ax.set_ylabel(\"Spearman rho\")\n    ax.set_title(\"Per-layer rho Profile: VLA (trained/untrained) vs DINO-V2\")\n    ax.legend()\n    ax.grid(True, alpha=0.3)\n\n    path = os.path.join(output_dir, \"per_layer_rho_profile.png\")\n    fig.savefig(path, dpi=150, bbox_inches=\"tight\")\n    fig.savefig(path.replace(\".png\", \".pdf\"), bbox_inches=\"tight\")\n    plt.close(fig)\n    print(f\"Saved {path}\")\n\n\n# ============================================================\n# Judgment\n# ============================================================\n\ndef bootstrap_delta_rho(trained_rhos, untrained_rhos, n_bootstrap=1000, seed=42):\n    rng = np.random.RandomState(seed)\n    deltas = []\n    n = len(trained_rhos)\n    for _ in range(n_bootstrap):\n        idx = rng.choice(n, n, replace=True)\n        delta = np.mean(np.array(trained_rhos)[idx]) - np.mean(np.array(untrained_rhos)[idx])\n        deltas.append(delta)\n    deltas = sorted(deltas)\n    ci_lower = deltas[int(0.025 * n_bootstrap)]\n    ci_upper = deltas[int(0.975 * n_bootstrap)]\n    return np.mean(deltas), ci_lower, ci_upper\n\n\ndef compute_judgment(all_data):\n    \"\"\"PASS/FAIL based on three criteria (D001 calibration).\"\"\"\n    criteria = {}\n\n    # 1) best rho > 0.5\n    if \"trained\" in all_data:\n        layers, rhos = extract_layer_metrics(all_data[\"trained\"], \"spearman_rho\")\n        best_rho = float(rhos.max()) if len(rhos) > 0 else 0.0\n        best_layer = int(layers[np.argmax(rhos)]) if len(rhos) > 0 else -1\n    else:\n        best_rho, best_layer = 0.0, -1\n\n    criteria[\"best_rho\"] = best_rho\n    criteria[\"best_layer\"] = best_layer\n    criteria[\"rho_pass\"] = best_rho > 0.5\n\n    # 2) delta-rho > 0.1 with bootstrapped 95% CI excluding 0\n    max_delta = 0.0\n    delta_ci_lower = 0.0\n    delta_ci_upper = 0.0\n    ci_excludes_zero = False\n    if \"trained\" in all_data and \"untrained\" in all_data:\n        l_tr, rho_tr = extract_layer_metrics(all_data[\"trained\"], \"spearman_rho\")\n        l_un, rho_un = extract_layer_metrics(all_data[\"untrained\"], \"spearman_rho\")\n        tr_map = dict(zip(l_tr.tolist(), rho_tr.tolist()))\n        un_map = dict(zip(l_un.tolist(), rho_un.tolist()))\n        common = set(l_tr.tolist()) & set(l_un.tolist())\n        if common:\n            max_delta = max(tr_map[l] - un_map[l] for l in common)\n            trained_rhos = [tr_map[l] for l in sorted(common)]\n            untrained_rhos = [un_map[l] for l in sorted(common)]\n            _, delta_ci_lower, delta_ci_upper = bootstrap_delta_rho(\n                trained_rhos, untrained_rhos\n            )\n            ci_excludes_zero = delta_ci_lower > 0\n\n    criteria[\"max_delta_rho\"] = max_delta\n    criteria[\"delta_ci_lower\"] = delta_ci_lower\n    criteria[\"delta_ci_upper\"] = delta_ci_upper\n    criteria[\"ci_excludes_zero\"] = ci_excludes_zero\n    criteria[\"delta_pass\"] = max_delta > 0.1 and ci_excludes_zero\n\n    # 3) VLA_rho >= DINO_rho OR (subtask_AUC > 0.7 AND subtask_AUC > DINO_subtask_AUC + 0.05)\n    vla_ge_dino = False\n    if \"trained\" in all_data and \"dinov2\" in all_data:\n        _, rho_vla = extract_layer_metrics(all_data[\"trained\"], \"spearman_rho\")\n        _, rho_dino = extract_layer_metrics(all_data[\"dinov2\"], \"spearman_rho\")\n        if len(rho_vla) > 0 and len(rho_dino) > 0:\n            vla_ge_dino = float(rho_vla.max()) >= float(rho_dino.max())\n\n    vla_best_auc = 0.0\n    dino_best_auc = 0.0\n    if \"trained\" in all_data:\n        for v in all_data[\"trained\"].get(\"results\", {}).values():\n            if isinstance(v.get(\"macro_auc\"), (int, float)):\n                vla_best_auc = max(vla_best_auc, v[\"macro_auc\"])\n    if \"dinov2\" in all_data:\n        for v in all_data[\"dinov2\"].get(\"results\", {}).values():\n            if isinstance(v.get(\"macro_auc\"), (int, float)):\n                dino_best_auc = max(dino_best_auc, v[\"macro_auc\"])\n    subtask_pass = vla_best_auc > 0.7 and vla_best_auc > dino_best_auc + 0.05\n\n    criteria[\"vla_ge_dinov2\"] = vla_ge_dino\n    criteria[\"vla_best_auc\"] = vla_best_auc\n    criteria[\"dino_best_auc\"] = dino_best_auc\n    criteria[\"subtask_auc_pass\"] = subtask_pass\n    criteria[\"third_criterion\"] = vla_ge_dino or subtask_pass\n\n    if criteria[\"rho_pass\"] and criteria[\"delta_pass\"] and criteria[\"third_criterion\"]:\n        judgment = \"PASS\"\n    elif criteria[\"delta_pass\"] and not criteria[\"third_criterion\"]:\n        judgment = \"CONDITIONAL\"\n    else:\n        judgment = \"FAIL\"\n\n    reasons = []\n    if not criteria[\"rho_pass\"]:\n        reasons.append(f\"best rho = {best_rho:.4f} <= 0.5\")\n    if not criteria[\"delta_pass\"]:\n        if max_delta <= 0.1:\n            reasons.append(f\"max delta-rho = {max_delta:.4f} <= 0.1\")\n        elif not ci_excludes_zero:\n            reasons.append(f\"delta-rho CI [{delta_ci_lower:.4f}, {delta_ci_upper:.4f}] includes 0\")\n    if not criteria[\"third_criterion\"]:\n        reasons.append(\"VLA < DINO-V2 AND subtask gate not met\")\n\n    return dict(judgment=judgment, criteria=criteria,\n                reasons=reasons if reasons else [\"All criteria met\"])\n\n\n# ============================================================\n# Main\n# ============================================================\n\ndef main():\n    args = parse_args()\n    os.makedirs(args.output_dir, exist_ok=True)\n\n    dirs = parse_results_dirs(args.results_dirs)\n    print(f\"Loading results: {list(dirs.keys())}\")\n\n    all_data = {}\n    for name, path in dirs.items():\n        try:\n            data = load_results(path, args.probe_type)\n            all_data[name] = data\n            n = len(data.get(\"results\", {}))\n            print(f\"  {name}: {n} entries\")\n        except Exception as e:\n            print(f\"  {name}: FAILED ({e})\")\n\n    if not all_data:\n        print(\"No data loaded.\")\n        return\n\n    oracle_rho = load_oracle(dirs)\n    if oracle_rho is not None:\n        print(f\"Oracle rho: {oracle_rho:.4f}\")\n\n    # --- Comparison table ---\n    print(\"\\n=== Layer-wise Spearman rho ===\")\n    names = list(all_data.keys())\n    header = [\"Layer\"] + names\n    print(\" | \".join(f\"{h:>12}\" for h in header))\n    print(\"-\" * (14 * len(header)))\n\n    all_layers = set()\n    for data in all_data.values():\n        layers, _ = extract_layer_metrics(data, \"spearman_rho\")\n        all_layers.update(layers.tolist())\n\n    for layer in sorted(all_layers):\n        row = [f\"{layer:>12}\"]\n        for name in names:\n            layers, rhos = extract_layer_metrics(all_data[name], \"spearman_rho\")\n            lmap = dict(zip(layers.tolist(), rhos.tolist()))\n            val = lmap.get(layer, float(\"nan\"))\n            row.append(f\"{val:>12.4f}\")\n        print(\" | \".join(row))\n\n    print(\"\\n=== Best Layer ===\")\n    for name, data in all_data.items():\n        layers, rhos = extract_layer_metrics(data, \"spearman_rho\")\n        if len(rhos) > 0:\n            bi = int(np.argmax(rhos))\n            print(f\"  {name}: layer {layers[bi]} (rho={rhos[bi]:.4f})\")\n\n    # --- Plots ---\n    if args.probe_type == \"temporal_distance\":\n        plot_layer_rho(all_data, oracle_rho, args.output_dir)\n        plot_delta_rho(all_data, args.output_dir)\n        plot_per_layer_rho_profile(all_data, args.output_dir)\n\n    if args.probe_type == \"subtask_predicate\":\n        for name, data in all_data.items():\n            plot_subtask_auc_heatmap(data, args.output_dir, name)\n\n    # --- Judgment ---\n    judgment = compute_judgment(all_data)\n    print(f\"\\n=== Judgment: {judgment['judgment']} ===\")\n    for k, v in judgment[\"criteria\"].items():\n        print(f\"  {k}: {v}\")\n    for r in judgment[\"reasons\"]:\n        print(f\"  >> {r}\")\n\n    # --- Save ---\n    summary = dict(\n        models=names,\n        probe_type=args.probe_type,\n        judgment=judgment,\n    )\n    for name, data in all_data.items():\n        layers, rhos = extract_layer_metrics(data, \"spearman_rho\")\n        if len(rhos) > 0:\n            bi = int(np.argmax(rhos))\n            summary[name] = dict(best_layer=int(layers[bi]), best_rho=float(rhos[bi]))\n    if oracle_rho is not None:\n        summary[\"oracle_rho\"] = oracle_rho\n\n    with open(os.path.join(args.output_dir, \"summary.json\"), \"w\") as f:\n        json.dump(summary, f, indent=2)\n    print(f\"\\nSaved {args.output_dir}/summary.json\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T11:16:07.414184+00:00_

File created successfully at: /tmp/analyze_results_new.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T11:16:07.414333+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "base64 /tmp/analyze_results_new.py | tr -d '\\n'",
  "description": "Base64 encode the new file for transfer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "Bash",
  "tool_args": {
    "command": "base64 /tmp/analyze_results_new.py | tr -d '\\n'",
    "description": "Base64 encode the new file for transfer"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T11:16:07.414522+00:00_

IiIiYW5hbHl6ZV9yZXN1bHRzLnB5IOKAlCBDb21wYXJlIHByb2JlIHJlc3VsdHMgYWNyb3NzIG1vZGVscyBhbmQgdmlzdWFsaXplLgoKSW5wdXQ6ICBNdWx0aXBsZSByZXN1bHQgZGlyZWN0b3JpZXMgKGZyb20gdHJhaW5fcHJvYmVzLnB5KQpPdXRwdXQ6IENvbXBhcmlzb24gdGFibGVzLCBwbG90cywgUEFTUy9GQUlMIGp1ZGdtZW50CgpVc2FnZToKICBweXRob24gYW5hbHl6ZV9yZXN1bHRzLnB5IFwKICAgIC0tcmVzdWx0c19kaXJzIHRyYWluZWQ6cmVzdWx0cy90cmFpbmVkLyx1bnRyYWluZWQ6cmVzdWx0cy91bnRyYWluZWQvLGRpbm92MjpyZXN1bHRzL2Rpbm92Mi8gXAogICAgLS1vdXRwdXRfZGlyIHJlc3VsdHMvYW5hbHlzaXMvCiIiIgoKaW1wb3J0IGFyZ3BhcnNlCmltcG9ydCBqc29uCmltcG9ydCBvcwppbXBvcnQgZ2xvYgpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKCmltcG9ydCBudW1weSBhcyBucAoKaW1wb3J0IG1hdHBsb3RsaWIKbWF0cGxvdGxpYi51c2UoIkFnZyIpCmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKCgpkZWYgcGFyc2VfYXJncygpOgogICAgcCA9IGFyZ3BhcnNlLkFyZ3VtZW50UGFyc2VyKGRlc2NyaXB0aW9uPSJBbmFseXplIGFuZCBjb21wYXJlIHByb2JlIHJlc3VsdHMiKQogICAgcC5hZGRfYXJndW1lbnQoIi0tcmVzdWx0c19kaXJzIiwgcmVxdWlyZWQ9VHJ1ZSwKICAgICAgICAgICAgICAgICAgIGhlbHA9IkNvbW1hLXNlcGFyYXRlZCBuYW1lOnBhdGggcGFpcnMsIGUuZy4gdHJhaW5lZDpyZXN1bHRzL3RyYWluZWQvIikKICAgIHAuYWRkX2FyZ3VtZW50KCItLW91dHB1dF9kaXIiLCByZXF1aXJlZD1UcnVlKQogICAgcC5hZGRfYXJndW1lbnQoIi0tcHJvYmVfdHlwZSIsIGRlZmF1bHQ9InRlbXBvcmFsX2Rpc3RhbmNlIiwKICAgICAgICAgICAgICAgICAgIGNob2ljZXM9WyJ0ZW1wb3JhbF9kaXN0YW5jZSIsICJzdWJ0YXNrX3ByZWRpY2F0ZSJdKQogICAgcmV0dXJuIHAucGFyc2VfYXJncygpCgoKZGVmIHBhcnNlX3Jlc3VsdHNfZGlycyhzKToKICAgIGQgPSB7fQogICAgZm9yIGVudHJ5IGluIHMuc3BsaXQoIiwiKToKICAgICAgICBuYW1lLCBwYXRoID0gZW50cnkuc3RyaXAoKS5zcGxpdCgiOiIpCiAgICAgICAgZFtuYW1lLnN0cmlwKCldID0gcGF0aC5zdHJpcCgpCiAgICByZXR1cm4gZAoKCmRlZiBsb2FkX3Jlc3VsdHMocmVzdWx0c19kaXIsIHByb2JlX3R5cGUpOgogICAgIiIiTG9hZCBwcm9iZSByZXN1bHRzIGZyb20gYSBkaXJlY3RvcnkuIiIiCiAgICBwcm9iZV9kaXIgPSBvcy5wYXRoLmpvaW4ocmVzdWx0c19kaXIsIHByb2JlX3R5cGUpCiAgICBzdW1tYXJ5X3BhdGggPSBvcy5wYXRoLmpvaW4ocHJvYmVfZGlyLCAic3VtbWFyeS5qc29uIikKICAgIGlmIG9zLnBhdGguZXhpc3RzKHN1bW1hcnlfcGF0aCk6CiAgICAgICAgd2l0aCBvcGVuKHN1bW1hcnlfcGF0aCkgYXMgZjoKICAgICAgICAgICAgcmV0dXJuIGpzb24ubG9hZChmKQoKICAgIHJlc3VsdHMgPSB7fQogICAgZm9yIHAgaW4g
…[truncated 19296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T11:16:07.414723+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "cp /root/vla-ssd/scripts/analyze_results.py /root/vla-ssd/scripts/analyze_results.py.bak && echo 'IiIiYW5hbHl6ZV9yZXN1bHRzLnB5IOKAlCBDb21wYXJlIHByb2JlIHJlc3VsdHMgYWNyb3NzIG1vZGVscyBhbmQgdmlzdWFsaXplLgoKSW5wdXQ6ICBNdWx0aXBsZSByZXN1bHQgZGlyZWN0b3JpZXMgKGZyb20gdHJhaW5fcHJvYmVzLnB5KQpPdXRwdXQ6IENvbXBhcmlzb24gdGFibGVzLCBwbG90cywgUEFTUy9GQUlMIGp1ZGdtZW50CgpVc2FnZToKICBweXRob24gYW5hbHl6ZV9yZXN1bHRzLnB5IFwKICAgIC0tcmVzdWx0c19kaXJzIHRyYWluZWQ6cmVzdWx0cy90cmFpbmVkLyx1bnRyYWluZWQ6cmVzdWx0cy91bnRyYWluZWQvLGRpbm92MjpyZXN1bHRzL2Rpbm92Mi8gXAogICAgLS1vdXRwdXRfZGlyIHJlc3VsdHMvYW5hbHlzaXMvCiIiIgoKaW1wb3J0IGFyZ3BhcnNlCmltcG9ydCBqc29uCmltcG9ydCBvcwppbXBvcnQgZ2xvYgpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKCmltcG9ydCBudW1weSBhcyBucAoKaW1wb3J0IG1hdHBsb3RsaWIKbWF0cGxvdGxpYi51c2UoIkFnZyIpCmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKCgpkZWYgcGFyc2VfYXJncygpOgogICAgcCA9IGFyZ3BhcnNlLkFyZ3VtZW50UGFyc2VyKGRlc2NyaXB0aW9uPSJBbmFseXplIGFuZCBjb21wYXJlIHByb2JlIHJlc3VsdHMiKQogICAgcC5hZGRfYXJndW1lbnQoIi0tcmVzdWx0c19kaXJzIiwgcmVxdWlyZWQ9VHJ1ZSwKICAgICAgICAgICAgICAgICAgIGhlbHA9IkNvbW1hLXNlcGFyYXRlZCBuYW1lOnBhdGggcGFpcnMsIGUuZy4gdHJhaW5lZDpyZXN1bHRzL3RyYWluZWQvIikKICAgIHAuYWRkX2FyZ3VtZW50KCItLW91dHB1dF9kaXIiLCByZXF1aXJlZD1UcnVlKQogICAgcC5hZGRfYXJndW1lbnQoIi0tcHJvYmVfdHlwZSIsIGRlZmF1bHQ9InRlbXBvcmFsX2Rpc3RhbmNlIiwKICAgICAgICAgICAgICAgICAgIGNob2ljZXM9WyJ0ZW1wb3JhbF9kaXN0YW5jZSIsICJzdWJ0YXNrX3ByZWRpY2F0ZSJdKQogICAgcmV0dXJuIHAucGFyc2VfYXJncygpCgoKZGVmIHBhcnNlX3Jlc3VsdHNfZGlycyhzKToKICAgIGQgPSB7fQogICAgZm9yIGVudHJ5IGluIHMuc3BsaXQoIiwiKToKICAgICAgICBuYW1lLCBwYXRoID0gZW50cnkuc3RyaXAoKS5zcGxpdCgiOiIpCiAgICAgICAgZFtuYW1lLnN0cmlwKCldID0gcGF0aC5zdHJpcCgpCiAgICByZXR1cm4gZAoKCmRlZiBsb2FkX3Jlc3VsdHMocmVzdWx0c19kaXIsIHByb2JlX3R5cGUpOgogICAgIiIiTG9hZCBwcm9iZSByZXN1bHRzIGZyb20gYSBkaXJlY3RvcnkuIiIiCiAgICBwcm9iZV9kaXIgPSBvcy5wYXRoLmpvaW4ocmVzdWx0c19kaXIsIHByb2JlX3R5cGUpCiAgICBzdW1tYXJ5X3BhdGggPSBvcy5wYXRoLmpvaW4ocHJvYmVfZGlyLCAic3VtbWFyeS5qc29uIikKICAgIGlmIG9zLnBhdGguZXhpc3RzKHN1bW1hcnlfcGF0aCk6CiAgICAgICAgd2l0aCBvcGVuKHN1bW1hcnlfcGF0aCkgYXMgZjoKICAgICAgICAgICAgcmV0dXJuIGpzb24ubG9hZChmKQoKICAgIHJlc3VsdHMgPSB7fQogICAgZm9yIHAgaW4gc29ydGVkKGdsb2IuZ2xvYihvcy5wYXRoLmpvaW4ocHJvYmVfZGlyLCAibGF5ZXJfKi5qc29uIikpKToKICAgICAgICB3aXRoIG9wZW4ocCkgYXMgZjoKICAgICAgICAgICAgbSA9IGpzb24ubG9hZChmKQogICAgICAgIGtleSA9IG0uZ2V0KCJsYXllciIsIFBhdGgocCkuc3RlbS5yZXBsYWNlKCJsYXllcl8iLCAiIikpCiAgICAgICAgcmVzdWx0c1tzdHIoa2V5KV0gPSBtCiAgICByZXR1cm4geyJyZXN1bHRzIjogcmVzdWx0c30KCgpkZWYgbG9hZF9vcmFjbGUocmVzdWx0c19kaXJzKToKICAgICIiIkF1dG8tZGV0ZWN0IG9yYWNsZSByZXN1bHRzIGZyb20gYW55IHByb3ZpZGVkIGRpcmVjdG9yeS4iIiIKICAgIGZvciBwYXRoIGluIHJlc3VsdHNfZGlycy52YWx1ZXMoKToKICAgICAgICBvcmFjbGVfZGlyID0gb3MucGF0aC5qb2luKHBhdGgsICJvcmFjbGUiKQogICAgICAgIHN1bW1hcnkgPSBvcy5wYXRoLmpvaW4ob3JhY2xlX2RpciwgInN1bW1hcnkuanNvbiIpCiAgICAgICAgaWYgb3MucGF0aC5leGlzdHMoc3VtbWFyeSk6CiAgICAgICAgICAgIHdpdGggb3BlbihzdW1tYXJ5KSBhcyBmOgogICAgICAgICAgICAgICAgZGF0YSA9IGpzb24ubG9hZChmKQogICAgICAgICAgICByID0gZGF0YS5nZXQoInJlc3VsdHMiLCB7fSkKICAgICAgICAgICAgaWYgIm9yYWNsZSIgaW4gcjoKICAgICAgICAgICAgICAgIHJldHVybiByWyJvcmFjbGUiXS5nZXQoInNwZWFybWFuX3JobyIpCiAgICByZXR1cm4gTm9uZQoKCmRlZiBfc29ydF9rZXkoeCk6CiAgICB0cnk6CiAgICAgICAgcmV0dXJuICgwLCBpbnQoeCkpCiAgICBleGNlcHQgVmFsdWVFcnJvcjoKICAgICAgICByZXR1cm4gKDEsIHgpCgoKZGVmIGV4dHJhY3RfbGF5ZXJfbWV0cmljcyhkYXRhLCBtZXRyaWM9InNwZWFybWFuX3JobyIpOgogICAgcmVzdWx0cyA9IGRhdGEuZ2V0KCJyZXN1bHRzIiwge30pCiAgICBsYXllcnMsIHZhbHVlcyA9IFtdLCBbXQogICAgZm9yIGssIHYgaW4gc29ydGVkKHJlc3VsdHMuaXRlbXMoKSwga2V5PWxhbWJkYSB4OiBfc29ydF9rZXkoeFswXSkpOgogICAgICAgIGlmIGsgPT0gIm9yYWNsZSI6CiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgdmFsID0gdi5nZXQobWV0cmljKQogICAgICAgIGlmIHZhbCBpcyBub3QgTm9uZSBhbmQgbm90IChpc2luc3RhbmNlKHZhbCwgZmxvYXQpIGFuZCBucC5pc25hbih2YWwpKToKICAgICAgICAgICAgbGF5ZXJzLmFwcGVuZChpbnQoaykpCiAgICAgICAgICAgIHZhbHVlcy5hcHBlbmQoZmxvYXQodmFsKSkKICAgIHJldHVybiBucC5hcnJheShsYXllcnMpLCBucC5hcnJheSh2YWx1ZXMpCgoKIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KIyBQbG90cwojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQoKQ09MT1JTID0gewogICAgInRyYWluZWQiOiAiIzIxOTZGMyIsICJ1bnRyYWluZWQiOiAiI0Y0NDMzNiIsCiAgICAiZGlub3YyIjogIiM0Q0FGNTAiLCAib3JhY2xlIjogIiNGRjk4MDAiLAp9Ck1BUktFUlMgPSB7InRyYWluZWQiOiAibyIsICJ1bnRyYWluZWQiOiAicyIsICJkaW5vdjIiOiAiXiIsICJvcmFjbGUiOiAiRCJ9CgoKZGVmIHBsb3RfbGF5ZXJfcmhvKGFsbF9kYXRhLCBvcmFjbGVfcmhvLCBvdXRwdXRfZGlyKToKICAgIGZpZywgYXggPSBwbHQuc3VicGxvdHMoZmlnc2l6ZT0oMTAsIDUpKQoKICAgIGZvciBuYW1lLCBkYXRhIGluIGFsbF9kYXRhLml0ZW1zKCk6CiAgICAgICAgbGF5ZXJzLCByaG9zID0gZXh0cmFjdF9sYXllcl9tZXRyaWNzKGRhdGEsICJzcGVhcm1hbl9yaG8iKQogICAgICAgIGlmIGxlbihsYXllcnMpID09IDA6CiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgYXgucGxvdChsYXllcnMsIHJob3MsCiAgICAgICAgICAgICAgICBtYXJrZXI9TUFSS0VSUy5nZXQobmFtZSwgIm8iKSwKICAgICAgICAgICAgICAgIGNvbG9yPUNPTE9SUy5nZXQobmFtZSwgIiM5OTkiKSwKICAgICAgICAgICAgICAgIGxhYmVsPW5hbWUsIGxpbmV3aWR0aD0yLCBtYXJrZXJzaXplPTUpCgogICAgaWYgb3JhY2xlX3JobyBpcyBub3QgTm9uZToKICAgICAgICBheC5heGhsaW5lKHk9b3JhY2xlX3JobywgY29sb3I9Q09MT1JTWyJvcmFjbGUiXSwKICAgICAgICAgICAgICAgICAgIGxpbmVzdHlsZT0iLS0iLCBsYWJlbD1mIm9yYWNsZSAocmhvPXtvcmFjbGVfcmhvOi4zZn0pIiwgYWxwaGE9MC43KQoKICAgIGF4LnNldF94bGFiZWwoIkxheWVyIikKICAgIGF4LnNldF95bGFiZWwoIlNwZWFybWFuIHJobyIpCiAgICBheC5zZXRfdGl0bGUoIlRlbXBvcmFsIERpc3RhbmNlIFByb2JlOiBMYXllci13aXNlIFNwZWFybWFuIHJobyIpCiAgICBheC5sZWdlbmQoKQogICAgYXguZ3JpZChUcnVlLCBhbHBoYT0wLjMpCgogICAgcGF0aCA9IG9zLnBhdGguam9pbihvdXRwdXRfZGlyLCAibGF5ZXJfcmhvLnBuZyIpCiAgICBmaWcuc2F2ZWZpZyhwYXRoLCBkcGk9MTUwLCBiYm94X2luY2hlcz0idGlnaHQiKQogICAgZmlnLnNhdmVmaWcocGF0aC5yZXBsYWNlKCIucG5nIiwgIi5wZGYiKSwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgIHBsdC5jbG9zZShmaWcpCiAgICBwcmludChmIlNhdmVkIHtwYXRofSIpCgoKZGVmIHBsb3RfZGVsdGFfcmhvKGFsbF9kYXRhLCBvdXRwdXRfZGlyKToKICAgIGlmICJ0cmFpbmVkIiBub3QgaW4gYWxsX2RhdGEgb3IgInVudHJhaW5lZCIgbm90IGluIGFsbF9kYXRhOgogICAgICAgIHByaW50KCJTa2lwcGluZyBkZWx0YS1yaG8gcGxvdCAobmVlZCB0cmFpbmVkICsgdW50cmFpbmVkKSIpCiAgICAgICAgcmV0dXJuCgogICAgbF90ciwgcmhvX3RyID0gZXh0cmFjdF9sYXllcl9tZXRyaWNzKGFsbF9kYXRhWyJ0cmFpbmVkIl0sICJzcGVhcm1hbl9yaG8iKQogICAgbF91biwgcmhvX3VuID0gZXh0cmFjdF9sYXllcl9tZXRyaWNzKGFsbF9kYXRhWyJ1bnRyYWluZWQiXSwgInNwZWFybWFuX3JobyIpCgogICAgdHJfbWFwID0gZGljdCh6aXAobF90ci50b2xpc3QoKSwgcmhvX3RyLnRvbGlzdCgpKSkKICAgIHVuX21hcCA9IGRpY3QoemlwKGxfdW4udG9saXN0KCksIHJob191bi50b2xpc3QoKSkpCiAgICBjb21tb24gPSBzb3J0ZWQoc2V0KGxfdHIudG9saXN0KCkpICYgc2V0KGxfdW4udG9saXN0KCkpKQogICAgaWYgbm90IGNvbW1vbjoKICAgICAgICByZXR1cm4KCiAgICBsYXllcnMgPSBucC5hcnJheShjb21tb24pCiAgICBkZWx0YXMgPSBucC5hcnJheShbdHJfbWFwW2xdIC0gdW5fbWFwW2xdIGZvciBsIGluIGNvbW1vbl0pCgogICAgZmlnLCBheCA9IHBsdC5zdWJwbG90cyhmaWdzaXplPSgxMCwgNSkpCiAgICBjb2xvcnMgPSBbIiMyMTk2RjMiIGlmIGQgPj0gMCBlbHNlICIjRjQ0MzM2IiBmb3IgZCBpbiBkZWx0YXNdCiAgICBheC5iYXIobGF5ZXJzLCBkZWx0YXMsIGNvbG9yPWNvbG9ycywgd2lkdGg9MC44KQogICAgYXguYXhobGluZSh5PTAuMSwgY29sb3I9ImdyZWVuIiwgbGluZXN0eWxlPSItLSIsIGFscGhhPTAuNSwgbGFiZWw9InRocmVzaG9sZD0wLjEiKQogICAgYXguYXhobGluZSh5PTAsIGNvbG9yPSJibGFjayIsIGxpbmV3aWR0aD0wLjUpCiAgICBheC5zZXRfeGxhYmVsKCJMYXllciIpCiAgICBheC5zZXRfeWxhYmVsKCJEZWx0YS1yaG8gKHRyYWluZWQgLSB1bnRyYWluZWQpIikKICAgIGF4LnNldF90aXRsZSgiVGVtcG9yYWwgRGlzdGFuY2UgUHJvYmU6IERlbHRhLXJobyBwZXIgTGF5ZXIiKQogICAgYXgubGVnZW5kKCkKICAgIGF4LmdyaWQoVHJ1ZSwgYWxwaGE9MC4zKQoKICAgIHBhdGggPSBvcy5wYXRoLmpvaW4ob3V0cHV0X2RpciwgImRlbHRhX3Joby5wbmciKQogICAgZmlnLnNhdmVmaWcocGF0aCwgZHBpPTE1MCwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgIGZpZy5zYXZlZmlnKHBhdGgucmVwbGFjZSgiLnBuZyIsICIucGRmIiksIGJib3hfaW5jaGVzPSJ0aWdodCIpCiAgICBwbHQuY2xvc2UoZmlnKQogICAgcHJpbnQoZiJTYXZlZCB7cGF0aH0iKQoKCmRlZiBwbG90X3N1YnRhc2tfYXVjX2hlYXRtYXAoZGF0YSwgb3V0cHV0X2RpciwgbmFtZT0idHJhaW5lZCIpOgogICAgcmVzdWx0cyA9IGRhdGEuZ2V0KCJyZXN1bHRzIiwge30pCiAgICBsYXllcnMgPSBzb3J0ZWQoW2ludChrKSBmb3IgayBpbiByZXN1bHRzIGlmIGsgIT0gIm9yYWNsZSJdKQogICAgaWYgbm90IGxheWVyczoKICAgICAgICByZXR1cm4KCiAgICBwcmVkX25hbWVzID0gTm9uZQogICAgZm9yIHYgaW4gcmVzdWx0cy52YWx1ZXMoKToKICAgICAgICBpZiAicHJlZGljYXRlX25hbWVzIiBpbiB2OgogICAgICAgICAgICBwcmVkX25hbWVzID0gdlsicHJlZGljYXRlX25hbWVzIl0KICAgICAgICAgICAgYnJlYWsKICAgIGlmIHByZWRfbmFtZXMgaXMgTm9uZToKICAgICAgICByZXR1cm4KCiAgICBuX3ByZWQgPSBsZW4ocHJlZF9uYW1lcykKICAgIGhlYXRtYXAgPSBucC5mdWxsKChsZW4obGF5ZXJzKSwgbl9wcmVkKSwgbnAubmFuKQoKICAgIGZvciBsaSwgbGF5ZXIgaW4gZW51bWVyYXRlKGxheWVycyk6CiAgICAgICAgYXVjID0gcmVzdWx0c1tzdHIobGF5ZXIpXS5nZXQoImF1Y19wZXJfcHJlZGljYXRlIiwge30pCiAgICAgICAgZm9yIGsgaW4gcmFuZ2Uobl9wcmVkKToKICAgICAgICAgICAgdmFsID0gYXVjLmdldChzdHIoayksIG5wLm5hbikKICAgICAgICAgICAgaGVhdG1hcFtsaSwga10gPSB2YWwKCiAgICBmaWcsIGF4ID0gcGx0LnN1YnBsb3RzKGZpZ3NpemU9KG1heCg4LCBuX3ByZWQpLCBtYXgoNiwgbGVuKGxheWVycykgKiAwLjMpKSkKICAgIGltID0gYXguaW1zaG93KGhlYXRtYXAsIGFzcGVjdD0iYXV0byIsIGNtYXA9IllsT3JSZCIsIHZtaW49MC41LCB2bWF4PTEuMCkKICAgIGF4LnNldF94dGlja3MocmFuZ2Uobl9wcmVkKSkKICAgIGF4LnNldF94dGlja2xhYmVscyhwcmVkX25hbWVzLCByb3RhdGlvbj00NSwgaGE9InJpZ2h0IiwgZm9udHNpemU9OCkKICAgIGF4LnNldF95dGlja3MocmFuZ2UobGVuKGxheWVycykpKQogICAgYXguc2V0X3l0aWNrbGFiZWxzKGxheWVycykKICAgIGF4LnNldF94bGFiZWwoIlByZWRpY2F0ZSIpCiAgICBheC5zZXRfeWxhYmVsKCJMYXllciIpCiAgICBheC5zZXRfdGl0bGUoZiJTdWItdGFzayBQcmVkaWNhdGUgQVVDICh7bmFtZX0pIikKICAgIGZpZy5jb2xvcmJhcihpbSwgYXg9YXgsIGxhYmVsPSJBVUMtUk9DIikKCiAgICBwYXRoID0gb3MucGF0aC5qb2luKG91dHB1dF9kaXIsIGYic3VidGFza19hdWNfe25hbWV9LnBuZyIpCiAgICBmaWcuc2F2ZWZpZyhwYXRoLCBkcGk9MTUwLCBiYm94X2luY2hlcz0idGlnaHQiKQogICAgZmlnLnNhdmVmaWcocGF0aC5yZXBsYWNlKCIucG5nIiwgIi5wZGYiKSwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgIHBsdC5jbG9zZShmaWcpCiAgICBwcmludChmIlNhdmVkIHtwYXRofSIpCgoKZGVmIHBsb3RfcGVyX2xheWVyX3Job19wcm9maWxlKGFsbF9kYXRhLCBvdXRwdXRfZGlyKToKICAgIGZpZywgYXggPSBwbHQuc3VicGxvdHMoZmlnc2l6ZT0oMTAsIDUpKQoKICAgIGZvciBuYW1lIGluIFsidHJhaW5lZCIsICJ1bnRyYWluZWQiXToKICAgICAgICBpZiBuYW1lIG5vdCBpbiBhbGxfZGF0YToKICAgICAgICAgICAgY29udGludWUKICAgICAgICBsYXllcnMsIHJob3MgPSBleHRyYWN0X2xheWVyX21ldHJpY3MoYWxsX2RhdGFbbmFtZV0sICJzcGVhcm1hbl9yaG8iKQogICAgICAgIGlmIGxlbihsYXllcnMpID09IDA6CiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgYXgucGxvdChsYXllcnMsIHJob3MsCiAgICAgICAgICAgICAgICBtYXJrZXI9TUFSS0VSUy5nZXQobmFtZSwgIm8iKSwKICAgICAgICAgICAgICAgIGNvbG9yPUNPTE9SUy5nZXQobmFtZSwgIiM5OTkiKSwKICAgICAgICAgICAgICAgIGxhYmVsPW5hbWUsIGxpbmV3aWR0aD0yLCBtYXJrZXJzaXplPTUpCgogICAgaWYgImRpbm92MiIgaW4gYWxsX2RhdGE6CiAgICAgICAgXywgcmhvX2Rpbm8gPSBleHRyYWN0X2xheWVyX21ldHJpY3MoYWxsX2RhdGFbImRpbm92MiJdLCAic3BlYXJtYW5fcmhvIikKICAgICAgICBpZiBsZW4ocmhvX2Rpbm8pID4gMDoKICAgICAgICAgICAgZGlub192YWwgPSBmbG9hdChyaG9fZGluby5tYXgoKSkKICAgICAgICAgICAgYXguYXhobGluZSh5PWRpbm9fdmFsLCBjb2xvcj1DT0xPUlMuZ2V0KCJkaW5vdjIiLCAiIzRDQUY1MCIpLAogICAgICAgICAgICAgICAgICAgICAgIGxpbmVzdHlsZT0iLS0iLCBsaW5ld2lkdGg9MiwKICAgICAgICAgICAgICAgICAgICAgICBsYWJlbD1mIkRJTk8tVjIgKHJobz17ZGlub192YWw6LjNmfSkiKQoKICAgIGF4LnNldF94bGFiZWwoIkxheWVyIEluZGV4IikKICAgIGF4LnNldF95bGFiZWwoIlNwZWFybWFuIHJobyIpCiAgICBheC5zZXRfdGl0bGUoIlBlci1sYXllciByaG8gUHJvZmlsZTogVkxBICh0cmFpbmVkL3VudHJhaW5lZCkgdnMgRElOTy1WMiIpCiAgICBheC5sZWdlbmQoKQogICAgYXguZ3JpZChUcnVlLCBhbHBoYT0wLjMpCgogICAgcGF0aCA9IG9zLnBhdGguam9pbihvdXRwdXRfZGlyLCAicGVyX2xheWVyX3Job19wcm9maWxlLnBuZyIpCiAgICBmaWcuc2F2ZWZpZyhwYXRoLCBkcGk9MTUwLCBiYm94X2luY2hlcz0idGlnaHQiKQogICAgZmlnLnNhdmVmaWcocGF0aC5yZXBsYWNlKCIucG5nIiwgIi5wZGYiKSwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgIHBsdC5jbG9zZShmaWcpCiAgICBwcmludChmIlNhdmVkIHtwYXRofSIpCgoKIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KIyBKdWRnbWVudAojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQoKZGVmIGJvb3RzdHJhcF9kZWx0YV9yaG8odHJhaW5lZF9yaG9zLCB1bnRyYWluZWRfcmhvcywgbl9ib290c3RyYXA9MTAwMCwgc2VlZD00Mik6CiAgICBybmcgPSBucC5yYW5kb20uUmFuZG9tU3RhdGUoc2VlZCkKICAgIGRlbHRhcyA9IFtdCiAgICBuID0gbGVuKHRyYWluZWRfcmhvcykKICAgIGZvciBfIGluIHJhbmdlKG5fYm9vdHN0cmFwKToKICAgICAgICBpZHggPSBybmcuY2hvaWNlKG4sIG4sIHJlcGxhY2U9VHJ1ZSkKICAgICAgICBkZWx0YSA9IG5wLm1lYW4obnAuYXJyYXkodHJhaW5lZF9yaG9zKVtpZHhdKSAtIG5wLm1lYW4obnAuYXJyYXkodW50cmFpbmVkX3Job3MpW2lkeF0pCiAgICAgICAgZGVsdGFzLmFwcGVuZChkZWx0YSkKICAgIGRlbHRhcyA9IHNvcnRlZChkZWx0YXMpCiAgICBjaV9sb3dlciA9IGRlbHRhc1tpbnQoMC4wMjUgKiBuX2Jvb3RzdHJhcCldCiAgICBjaV91cHBlciA9IGRlbHRhc1tpbnQoMC45NzUgKiBuX2Jvb3RzdHJhcCldCiAgICByZXR1cm4gbnAubWVhbihkZWx0YXMpLCBjaV9sb3dlciwgY2lfdXBwZXIKCgpkZWYgY29tcHV0ZV9qdWRnbWVudChhbGxfZGF0YSk6CiAgICAiIiJQQVNTL0ZBSUwgYmFzZWQgb24gdGhyZWUgY3JpdGVyaWEgKEQwMDEgY2FsaWJyYXRpb24pLiIiIgogICAgY3JpdGVyaWEgPSB7fQoKICAgICMgMSkgYmVzdCByaG8gPiAwLjUKICAgIGlmICJ0cmFpbmVkIiBpbiBhbGxfZGF0YToKICAgICAgICBsYXllcnMsIHJob3MgPSBleHRyYWN0X2xheWVyX21ldHJpY3MoYWxsX2RhdGFbInRyYWluZWQiXSwgInNwZWFybWFuX3JobyIpCiAgICAgICAgYmVzdF9yaG8gPSBmbG9hdChyaG9zLm1heCgpKSBpZiBsZW4ocmhvcykgPiAwIGVsc2UgMC4wCiAgICAgICAgYmVzdF9sYXllciA9IGludChsYXllcnNbbnAuYXJnbWF4KHJob3MpXSkgaWYgbGVuKHJob3MpID4gMCBlbHNlIC0xCiAgICBlbHNlOgogICAgICAgIGJlc3RfcmhvLCBiZXN0X2xheWVyID0gMC4wLCAtMQoKICAgIGNyaXRlcmlhWyJiZXN0X3JobyJdID0gYmVzdF9yaG8KICAgIGNyaXRlcmlhWyJiZXN0X2xheWVyIl0gPSBiZXN0X2xheWVyCiAgICBjcml0ZXJpYVsicmhvX3Bhc3MiXSA9IGJlc3RfcmhvID4gMC41CgogICAgIyAyKSBkZWx0YS1yaG8gPiAwLjEgd2l0aCBib290c3RyYXBwZWQgOTUlIENJIGV4Y2x1ZGluZyAwCiAgICBtYXhfZGVsdGEgPSAwLjAKICAgIGRlbHRhX2NpX2xvd2VyID0gMC4wCiAgICBkZWx0YV9jaV91cHBlciA9IDAuMAogICAgY2lfZXhjbHVkZXNfemVybyA9IEZhbHNlCiAgICBpZiAidHJhaW5lZCIgaW4gYWxsX2RhdGEgYW5kICJ1bnRyYWluZWQiIGluIGFsbF9kYXRhOgogICAgICAgIGxfdHIsIHJob190ciA9IGV4dHJhY3RfbGF5ZXJfbWV0cmljcyhhbGxfZGF0YVsidHJhaW5lZCJdLCAic3BlYXJtYW5fcmhvIikKICAgICAgICBsX3VuLCByaG9fdW4gPSBleHRyYWN0X2xheWVyX21ldHJpY3MoYWxsX2RhdGFbInVudHJhaW5lZCJdLCAic3BlYXJtYW5fcmhvIikKICAgICAgICB0cl9tYXAgPSBkaWN0KHppcChsX3RyLnRvbGlzdCgpLCByaG9fdHIudG9saXN0KCkpKQogICAgICAgIHVuX21hcCA9IGRpY3QoemlwKGxfdW4udG9saXN0KCksIHJob191bi50b2xpc3QoKSkpCiAgICAgICAgY29tbW9uID0gc2V0KGxfdHIudG9saXN0KCkpICYgc2V0KGxfdW4udG9saXN0KCkpCiAgICAgICAgaWYgY29tbW9uOgogICAgICAgICAgICBtYXhfZGVsdGEgPSBtYXgodHJfbWFwW2xdIC0gdW5fbWFwW2xdIGZvciBsIGluIGNvbW1vbikKICAgICAgICAgICAgdHJhaW5lZF9yaG9zID0gW3RyX21hcFtsXSBmb3IgbCBpbiBzb3J0ZWQoY29tbW9uKV0KICAgICAgICAgICAgdW50cmFpbmVkX3Job3MgPSBbdW5fbWFwW2xdIGZvciBsIGluIHNvcnRlZChjb21tb24pXQogICAgICAgICAgICBfLCBkZWx0YV9jaV9sb3dlciwgZGVsdGFfY2lfdXBwZXIgPSBib290c3RyYXBfZGVsdGFfcmhvKAogICAgICAgICAgICAgICAgdHJhaW5lZF9yaG9zLCB1bnRyYWluZWRfcmhvcwogICAgICAgICAgICApCiAgICAgICAgICAgIGNpX2V4Y2x1ZGVzX3plcm8gPSBkZWx0YV9jaV9sb3dlciA+IDAKCiAgICBjcml0ZXJpYVsibWF4X2RlbHRhX3JobyJdID0gbWF4X2RlbHRhCiAgICBjcml0ZXJpYVsiZGVsdGFfY2lfbG93ZXIiXSA9IGRlbHRhX2NpX2xvd2VyCiAgICBjcml0ZXJpYVsiZGVsdGFfY2lfdXBwZXIiXSA9IGRlbHRhX2NpX3VwcGVyCiAgICBjcml0ZXJpYVsiY2lfZXhjbHVkZXNfemVybyJdID0gY2lfZXhjbHVkZXNfemVybwogICAgY3JpdGVyaWFbImRlbHRhX3Bhc3MiXSA9IG1heF9kZWx0YSA+IDAuMSBhbmQgY2lfZXhjbHVkZXNfemVybwoKICAgICMgMykgVkxBX3JobyA+PSBESU5PX3JobyBPUiAoc3VidGFza19BVUMgPiAwLjcgQU5EIHN1YnRhc2tfQVVDID4gRElOT19zdWJ0YXNrX0FVQyArIDAuMDUpCiAgICB2bGFfZ2VfZGlubyA9IEZhbHNlCiAgICBpZiAidHJhaW5lZCIgaW4gYWxsX2RhdGEgYW5kICJkaW5vdjIiIGluIGFsbF9kYXRhOgogICAgICAgIF8sIHJob192bGEgPSBleHRyYWN0X2xheWVyX21ldHJpY3MoYWxsX2RhdGFbInRyYWluZWQiXSwgInNwZWFybWFuX3JobyIpCiAgICAgICAgXywgcmhvX2Rpbm8gPSBleHRyYWN0X2xheWVyX21ldHJpY3MoYWxsX2RhdGFbImRpbm92MiJdLCAic3BlYXJtYW5fcmhvIikKICAgICAgICBpZiBsZW4ocmhvX3ZsYSkgPiAwIGFuZCBsZW4ocmhvX2Rpbm8pID4gMDoKICAgICAgICAgICAgdmxhX2dlX2Rpbm8gPSBmbG9hdChyaG9fdmxhLm1heCgpKSA+PSBmbG9hdChyaG9fZGluby5tYXgoKSkKCiAgICB2bGFfYmVzdF9hdWMgPSAwLjAKICAgIGRpbm9fYmVzdF9hdWMgPSAwLjAKICAgIGlmICJ0cmFpbmVkIiBpbiBhbGxfZGF0YToKICAgICAgICBmb3IgdiBpbiBhbGxfZGF0YVsidHJhaW5lZCJdLmdldCgicmVzdWx0cyIsIHt9KS52YWx1ZXMoKToKICAgICAgICAgICAgaWYgaXNpbnN0YW5jZSh2LmdldCgibWFjcm9fYXVjIiksIChpbnQsIGZsb2F0KSk6CiAgICAgICAgICAgICAgICB2bGFfYmVzdF9hdWMgPSBtYXgodmxhX2Jlc3RfYXVjLCB2WyJtYWNyb19hdWMiXSkKICAgIGlmICJkaW5vdjIiIGluIGFsbF9kYXRhOgogICAgICAgIGZvciB2IGluIGFsbF9kYXRhWyJkaW5vdjIiXS5nZXQoInJlc3VsdHMiLCB7fSkudmFsdWVzKCk6CiAgICAgICAgICAgIGlmIGlzaW5zdGFuY2Uodi5nZXQoIm1hY3JvX2F1YyIpLCAoaW50LCBmbG9hdCkpOgogICAgICAgICAgICAgICAgZGlub19iZXN0X2F1YyA9IG1heChkaW5vX2Jlc3RfYXVjLCB2WyJtYWNyb19hdWMiXSkKICAgIHN1YnRhc2tfcGFzcyA9IHZsYV9iZXN0X2F1YyA+IDAuNyBhbmQgdmxhX2Jlc3RfYXVjID4gZGlub19iZXN0X2F1YyArIDAuMDUKCiAgICBjcml0ZXJpYVsidmxhX2dlX2Rpbm92MiJdID0gdmxhX2dlX2Rpbm8KICAgIGNyaXRlcmlhWyJ2bGFfYmVzdF9hdWMiXSA9IHZsYV9iZXN0X2F1YwogICAgY3JpdGVyaWFbImRpbm9fYmVzdF9hdWMiXSA9IGRpbm9fYmVzdF9hdWMKICAgIGNyaXRlcmlhWyJzdWJ0YXNrX2F1Y19wYXNzIl0gPSBzdWJ0YXNrX3Bhc3MKICAgIGNyaXRlcmlhWyJ0aGlyZF9jcml0ZXJpb24iXSA9IHZsYV9nZV9kaW5vIG9yIHN1YnRhc2tfcGFzcwoKICAgIGlmIGNyaXRlcmlhWyJyaG9fcGFzcyJdIGFuZCBjcml0ZXJpYVsiZGVsdGFfcGFzcyJdIGFuZCBjcml0ZXJpYVsidGhpcmRfY3JpdGVyaW9uIl06CiAgICAgICAganVkZ21lbnQgPSAiUEFTUyIKICAgIGVsaWYgY3JpdGVyaWFbImRlbHRhX3Bhc3MiXSBhbmQgbm90IGNyaXRlcmlhWyJ0aGlyZF9jcml0ZXJpb24iXToKICAgICAgICBqdWRnbWVudCA9ICJDT05ESVRJT05BTCIKICAgIGVsc2U6CiAgICAgICAganVkZ21lbnQgPSAiRkFJTCIKCiAgICByZWFzb25zID0gW10KICAgIGlmIG5vdCBjcml0ZXJpYVsicmhvX3Bhc3MiXToKICAgICAgICByZWFzb25zLmFwcGVuZChmImJlc3QgcmhvID0ge2Jlc3RfcmhvOi40Zn0gPD0gMC41IikKICAgIGlmIG5vdCBjcml0ZXJpYVsiZGVsdGFfcGFzcyJdOgogICAgICAgIGlmIG1heF9kZWx0YSA8PSAwLjE6CiAgICAgICAgICAgIHJlYXNvbnMuYXBwZW5kKGYibWF4IGRlbHRhLXJobyA9IHttYXhfZGVsdGE6LjRmfSA8PSAwLjEiKQogICAgICAgIGVsaWYgbm90IGNpX2V4Y2x1ZGVzX3plcm86CiAgICAgICAgICAgIHJlYXNvbnMuYXBwZW5kKGYiZGVsdGEtcmhvIENJIFt7ZGVsdGFfY2lfbG93ZXI6LjRmfSwge2RlbHRhX2NpX3VwcGVyOi40Zn1dIGluY2x1ZGVzIDAiKQogICAgaWYgbm90IGNyaXRlcmlhWyJ0aGlyZF9jcml0ZXJpb24iXToKICAgICAgICByZWFzb25zLmFwcGVuZCgiVkxBIDwgRElOTy1WMiBBTkQgc3VidGFzayBnYXRlIG5vdCBtZXQiKQoKICAgIHJldHVybiBkaWN0KGp1ZGdtZW50PWp1ZGdtZW50LCBjcml0ZXJpYT1jcml0ZXJpYSwKICAgICAgICAgICAgICAgIHJlYXNvbnM9cmVhc29ucyBpZiByZWFzb25zIGVsc2UgWyJBbGwgY3JpdGVyaWEgbWV0Il0pCgoKIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KIyBNYWluCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09CgpkZWYgbWFpbigpOgogICAgYXJncyA9IHBhcnNlX2FyZ3MoKQogICAgb3MubWFrZWRpcnMoYXJncy5vdXRwdXRfZGlyLCBleGlzdF9vaz1UcnVlKQoKICAgIGRpcnMgPSBwYXJzZV9yZXN1bHRzX2RpcnMoYXJncy5yZXN1bHRzX2RpcnMpCiAgICBwcmludChmIkxvYWRpbmcgcmVzdWx0czoge2xpc3QoZGlycy5rZXlzKCkpfSIpCgogICAgYWxsX2RhdGEgPSB7fQogICAgZm9yIG5hbWUsIHBhdGggaW4gZGlycy5pdGVtcygpOgogICAgICAgIHRyeToKICAgICAgICAgICAgZGF0YSA9IGxvYWRfcmVzdWx0cyhwYXRoLCBhcmdzLnByb2JlX3R5cGUpCiAgICAgICAgICAgIGFsbF9kYXRhW25hbWVdID0gZGF0YQogICAgICAgICAgICBuID0gbGVuKGRhdGEuZ2V0KCJyZXN1bHRzIiwge30pKQogICAgICAgICAgICBwcmludChmIiAge25hbWV9OiB7bn0gZW50cmllcyIpCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgICAgICBwcmludChmIiAge25hbWV9OiBGQUlMRUQgKHtlfSkiKQoKICAgIGlmIG5vdCBhbGxfZGF0YToKICAgICAgICBwcmludCgiTm8gZGF0YSBsb2FkZWQuIikKICAgICAgICByZXR1cm4KCiAgICBvcmFjbGVfcmhvID0gbG9hZF9vcmFjbGUoZGlycykKICAgIGlmIG9yYWNsZV9yaG8gaXMgbm90IE5vbmU6CiAgICAgICAgcHJpbnQoZiJPcmFjbGUgcmhvOiB7b3JhY2xlX3JobzouNGZ9IikKCiAgICAjIC0tLSBDb21wYXJpc29uIHRhYmxlIC0tLQogICAgcHJpbnQoIlxuPT09IExheWVyLXdpc2UgU3BlYXJtYW4gcmhvID09PSIpCiAgICBuYW1lcyA9IGxpc3QoYWxsX2RhdGEua2V5cygpKQogICAgaGVhZGVyID0gWyJMYXllciJdICsgbmFtZXMKICAgIHByaW50KCIgfCAiLmpvaW4oZiJ7aDo+MTJ9IiBmb3IgaCBpbiBoZWFkZXIpKQogICAgcHJpbnQoIi0iICogKDE0ICogbGVuKGhlYWRlcikpKQoKICAgIGFsbF9sYXllcnMgPSBzZXQoKQogICAgZm9yIGRhdGEgaW4gYWxsX2RhdGEudmFsdWVzKCk6CiAgICAgICAgbGF5ZXJzLCBfID0gZXh0cmFjdF9sYXllcl9tZXRyaWNzKGRhdGEsICJzcGVhcm1hbl9yaG8iKQogICAgICAgIGFsbF9sYXllcnMudXBkYXRlKGxheWVycy50b2xpc3QoKSkKCiAgICBmb3IgbGF5ZXIgaW4gc29ydGVkKGFsbF9sYXllcnMpOgogICAgICAgIHJvdyA9IFtmIntsYXllcjo+MTJ9Il0KICAgICAgICBmb3IgbmFtZSBpbiBuYW1lczoKICAgICAgICAgICAgbGF5ZXJzLCByaG9zID0gZXh0cmFjdF9sYXllcl9tZXRyaWNzKGFsbF9kYXRhW25hbWVdLCAic3BlYXJtYW5fcmhvIikKICAgICAgICAgICAgbG1hcCA9IGRpY3QoemlwKGxheWVycy50b2xpc3QoKSwgcmhvcy50b2xpc3QoKSkpCiAgICAgICAgICAgIHZhbCA9IGxtYXAuZ2V0KGxheWVyLCBmbG9hdCgibmFuIikpCiAgICAgICAgICAgIHJvdy5hcHBlbmQoZiJ7dmFsOj4xMi40Zn0iKQogICAgICAgIHByaW50KCIgfCAiLmpvaW4ocm93KSkKCiAgICBwcmludCgiXG49PT0gQmVzdCBMYXllciA9PT0iKQogICAgZm9yIG5hbWUsIGRhdGEgaW4gYWxsX2RhdGEuaXRlbXMoKToKICAgICAgICBsYXllcnMsIHJob3MgPSBleHRyYWN0X2xheWVyX21ldHJpY3MoZGF0YSwgInNwZWFybWFuX3JobyIpCiAgICAgICAgaWYgbGVuKHJob3MpID4gMDoKICAgICAgICAgICAgYmkgPSBpbnQobnAuYXJnbWF4KHJob3MpKQogICAgICAgICAgICBwcmludChmIiAge25hbWV9OiBsYXllciB7bGF5ZXJzW2JpXX0gKHJobz17cmhvc1tiaV06LjRmfSkiKQoKICAgICMgLS0tIFBsb3RzIC0tLQogICAgaWYgYXJncy5wcm9iZV90eXBlID09ICJ0ZW1wb3JhbF9kaXN0YW5jZSI6CiAgICAgICAgcGxvdF9sYXllcl9yaG8oYWxsX2RhdGEsIG9yYWNsZV9yaG8sIGFyZ3Mub3V0cHV0X2RpcikKICAgICAgICBwbG90X2RlbHRhX3JobyhhbGxfZGF0YSwgYXJncy5vdXRwdXRfZGlyKQogICAgICAgIHBsb3RfcGVyX2xheWVyX3Job19wcm9maWxlKGFsbF9kYXRhLCBhcmdzLm91dHB1dF9kaXIpCgogICAgaWYgYXJncy5wcm9iZV90eXBlID09ICJzdWJ0YXNrX3ByZWRpY2F0ZSI6CiAgICAgICAgZm9yIG5hbWUsIGRhdGEgaW4gYWxsX2RhdGEuaXRlbXMoKToKICAgICAgICAgICAgcGxvdF9zdWJ0YXNrX2F1Y19oZWF0bWFwKGRhdGEsIGFyZ3Mub3V0cHV0X2RpciwgbmFtZSkKCiAgICAjIC0tLSBKdWRnbWVudCAtLS0KICAgIGp1ZGdtZW50ID0gY29tcHV0ZV9qdWRnbWVudChhbGxfZGF0YSkKICAgIHByaW50KGYiXG49PT0gSnVkZ21lbnQ6IHtqdWRnbWVudFsnanVkZ21lbnQnXX0gPT09IikKICAgIGZvciBrLCB2IGluIGp1ZGdtZW50WyJjcml0ZXJpYSJdLml0ZW1zKCk6CiAgICAgICAgcHJpbnQoZiIgIHtrfToge3Z9IikKICAgIGZvciByIGluIGp1ZGdtZW50WyJyZWFzb25zIl06CiAgICAgICAgcHJpbnQoZiIgID4+IHtyfSIpCgogICAgIyAtLS0gU2F2ZSAtLS0KICAgIHN1bW1hcnkgPSBkaWN0KAogICAgICAgIG1vZGVscz1uYW1lcywKICAgICAgICBwcm9iZV90eXBlPWFyZ3MucHJvYmVfdHlwZSwKICAgICAgICBqdWRnbWVudD1qdWRnbWVudCwKICAgICkKICAgIGZvciBuYW1lLCBkYXRhIGluIGFsbF9kYXRhLml0ZW1zKCk6CiAgICAgICAgbGF5ZXJzLCByaG9zID0gZXh0cmFjdF9sYXllcl9tZXRyaWNzKGRhdGEsICJzcGVhcm1hbl9yaG8iKQogICAgICAgIGlmIGxlbihyaG9zKSA+IDA6CiAgICAgICAgICAgIGJpID0gaW50KG5wLmFyZ21heChyaG9zKSkKICAgICAgICAgICAgc3VtbWFyeVtuYW1lXSA9IGRpY3QoYmVzdF9sYXllcj1pbnQobGF5ZXJzW2JpXSksIGJlc3RfcmhvPWZsb2F0KHJob3NbYmldKSkKICAgIGlmIG9yYWNsZV9yaG8gaXMgbm90IE5vbmU6CiAgICAgICAgc3VtbWFyeVsib3JhY2xlX3JobyJdID0gb3JhY2xlX3JobwoKICAgIHdpdGggb3Blbihvcy5wYXRoLmpvaW4oYXJncy5vdXRwdXRfZGlyLCAic3VtbWFyeS5qc29uIiksICJ3IikgYXMgZjoKICAgICAgICBqc29uLmR1bXAoc3VtbWFyeSwgZiwgaW5kZW50PTIpCiAgICBwcmludChmIlxuU2F2ZWQge2FyZ3Mub3V0cHV0X2Rpcn0vc3VtbWFyeS5qc29uIikKCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg==' | base64 -d > /root/vla-ssd/scripts/analyze_results.py && echo \"WRITE_OK\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "cp /root/vla-ssd/scripts/analyze_results.py /root/vla-ssd/scripts/analyze_results.py.bak && echo 'IiIiYW5hbHl6ZV9yZXN1bHRzLnB5IOKAlCBDb21wYXJlIHByb2JlIHJlc3VsdHMgYWNyb3NzIG1vZGVscyBhbmQgdmlzdWFsaXplLgoKSW5wdXQ6ICBNdWx0aXBsZSByZXN1bHQgZGlyZWN0b3JpZXMgKGZyb20gdHJhaW5fcHJvYmVzLnB5KQpPdXRwdXQ6IENvbXBhcmlzb24gdGFibGVzLCBwbG90cywgUEFTUy9GQUlMIGp1ZGdtZW50CgpVc2FnZToKICBweXRob24gYW5hbHl6ZV9yZXN1bHRzLnB5IFwKICAgIC0tcmVzdWx0c19kaXJzIHRyYWluZWQ6cmVzdWx0cy90cmFpbmVkLyx1bnRyYWluZWQ6cmVzdWx0cy91bnRyYWluZWQvLGRpbm92MjpyZXN1bHRzL2Rpbm92Mi8gXAogICAgLS1vdXRwdXRfZGlyIHJlc3VsdHMvYW5hbHlzaXMvCiIiIgoKaW1wb3J0IGFyZ3BhcnNlCmltcG9ydCBqc29uCmltcG9ydCBvcwppbXBvcnQgZ2xvYgpmcm9tIHBhdGhsaWIgaW1wb3J0IFBhdGgKCmltcG9ydCBudW1weSBhcyBucAoKaW1wb3J0IG1hdHBsb3RsaWIKbWF0cGxvdGxpYi51c2UoIkFnZyIpCmltcG9ydCBtYXRwbG90bGliLnB5cGxvdCBhcyBwbHQKCgpkZWYgcGFyc2VfYXJncygpOgogICAgcCA9IGFyZ3BhcnNlLkFyZ3VtZW50UGFyc2VyKGRlc2NyaXB0aW9uPSJBbmFseXplIGFuZCBjb21wYXJlIHByb2JlIHJlc3VsdHMiKQogICAgcC5hZGRfYXJndW1lbnQoIi0tcmVzdWx0c19kaXJzIiwgcmVxdWlyZWQ9VHJ1ZSwKICAgICAgICAgICAgICAgICAgIGhlbHA9IkNvbW1hLXNlcGFyYXRlZCBuYW1lOnBhdGggcGFpcnMsIGUuZy4gdHJhaW5lZDpyZXN1bHRzL3RyYWluZWQvIikKICAgIHAuYWRkX2FyZ3VtZW50KCItLW91dHB1dF9kaXIiLCByZXF1aXJlZD1UcnVlKQogICAgcC5hZGRfYXJndW1lbnQoIi0tcHJvYmVfdHlwZSIsIGRlZmF1bHQ9InRlbXBvcmFsX2Rpc3RhbmNlIiwKICAgICAgICAgICAgICAgICAgIGNob2ljZXM9WyJ0ZW1wb3JhbF9kaXN0YW5jZSIsICJzdWJ0YXNrX3ByZWRpY2F0ZSJdKQogICAgcmV0dXJuIHAucGFyc2VfYXJncygpCgoKZGVmIHBhcnNlX3Jlc3VsdHNfZGlycyhzKToKICAgIGQgPSB7fQogICAgZm9yIGVudHJ5IGluIHMuc3BsaXQoIiwiKToKICAgICAgICBuYW1lLCBwYXRoID0gZW50cnkuc3RyaXAoKS5zcGxpdCgiOiIpCiAgICAgICAgZFtuYW1lLnN0cmlwKCldID0gcGF0aC5zdHJpcCgpCiAgICByZXR1cm4gZAoKCmRlZiBsb2FkX3Jlc3VsdHMocmVzdWx0c19kaXIsIHByb2JlX3R5cGUpOgogICAgIiIiTG9hZCBwcm9iZSByZXN1bHRzIGZyb20gYSBkaXJlY3RvcnkuIiIiCiAgICBwcm9iZV9kaXIgPSBvcy5wYXRoLmpvaW4ocmVzdWx0c19kaXIsIHByb2JlX3R5cGUpCiAgICBzdW1tYXJ5X3BhdGggPSBvcy5wYXRoLmpvaW4ocHJvYmVfZGlyLCAic3VtbWFyeS5qc29uIikKICAgIGlmIG9zLnBhdGguZXhpc3RzKHN1bW1hcnlfcGF0aCk6CiAgICAgICAgd2l0aCBvcGVuKHN1bW1hcnlfcGF0aCkgYXMgZjoKICAgICAgICAgICAgcmV0dXJuIGpzb24ubG9hZChmKQoKICAgIHJlc3VsdHMgPSB7fQogICAgZm9yIHAgaW4gc29ydGVkKGdsb2IuZ2xvYihvcy5wYXRoLmpvaW4ocHJvYmVfZGlyLCAibGF5ZXJfKi5qc29uIikpKToKICAgICAgICB3aXRoIG9wZW4ocCkgYXMgZjoKICAgICAgICAgICAgbSA9IGpzb24ubG9hZChmKQogICAgICAgIGtleSA9IG0uZ2V0KCJsYXllciIsIFBhdGgocCkuc3RlbS5yZXBsYWNlKCJsYXllcl8iLCAiIikpCiAgICAgICAgcmVzdWx0c1tzdHIoa2V5KV0gPSBtCiAgICByZXR1cm4geyJyZXN1bHRzIjogcmVzdWx0c30KCgpkZWYgbG9hZF9vcmFjbGUocmVzdWx0c19kaXJzKToKICAgICIiIkF1dG8tZGV0ZWN0IG9yYWNsZSByZXN1bHRzIGZyb20gYW55IHByb3ZpZGVkIGRpcmVjdG9yeS4iIiIKICAgIGZvciBwYXRoIGluIHJlc3VsdHNfZGlycy52YWx1ZXMoKToKICAgICAgICBvcmFjbGVfZGlyID0gb3MucGF0aC5qb2luKHBhdGgsICJvcmFjbGUiKQogICAgICAgIHN1bW1hcnkgPSBvcy5wYXRoLmpvaW4ob3JhY2xlX2RpciwgInN1bW1hcnkuanNvbiIpCiAgICAgICAgaWYgb3MucGF0aC5leGlzdHMoc3VtbWFyeSk6CiAgICAgICAgICAgIHdpdGggb3BlbihzdW1tYXJ5KSBhcyBmOgogICAgICAgICAgICAgICAgZGF0YSA9IGpzb24ubG9hZChmKQogICAgICAgICAgICByID0gZGF0YS5nZXQoInJlc3VsdHMiLCB7fSkKICAgICAgICAgICAgaWYgIm9yYWNsZSIgaW4gcjoKICAgICAgICAgICAgICAgIHJldHVybiByWyJvcmFjbGUiXS5nZXQoInNwZWFybWFuX3JobyIpCiAgICByZXR1cm4gTm9uZQoKCmRlZiBfc29ydF9rZXkoeCk6CiAgICB0cnk6CiAgICAgICAgcmV0dXJuICgwLCBpbnQoeCkpCiAgICBleGNlcHQgVmFsdWVFcnJvcjoKICAgICAgICByZXR1cm4gKDEsIHgpCgoKZGVmIGV4dHJhY3RfbGF5ZXJfbWV0cmljcyhkYXRhLCBtZXRyaWM9InNwZWFybWFuX3JobyIpOgogICAgcmVzdWx0cyA9IGRhdGEuZ2V0KCJyZXN1bHRzIiwge30pCiAgICBsYXllcnMsIHZhbHVlcyA9IFtdLCBbXQogICAgZm9yIGssIHYgaW4gc29ydGVkKHJlc3VsdHMuaXRlbXMoKSwga2V5PWxhbWJkYSB4OiBfc29ydF9rZXkoeFswXSkpOgogICAgICAgIGlmIGsgPT0gIm9yYWNsZSI6CiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgdmFsID0gdi5nZXQobWV0cmljKQogICAgICAgIGlmIHZhbCBpcyBub3QgTm9uZSBhbmQgbm90IChpc2luc3RhbmNlKHZhbCwgZmxvYXQpIGFuZCBucC5pc25hbih2YWwpKToKICAgICAgICAgICAgbGF5ZXJzLmFwcGVuZChpbnQoaykpCiAgICAgICAgICAgIHZhbHVlcy5hcHBlbmQoZmxvYXQodmFsKSkKICAgIHJldHVybiBucC5hcnJheShsYXllcnMpLCBucC5hcnJheSh2YWx1ZXMpCgoKIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KIyBQbG90cwojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQoKQ09MT1JTID0gewogICAgInRyYWluZWQiOiAiIzIxOTZGMyIsICJ1bnRyYWluZWQiOiAiI0Y0NDMzNiIsCiAgICAiZGlub3YyIjogIiM0Q0FGNTAiLCAib3JhY2xlIjogIiNGRjk4MDAiLAp9Ck1BUktFUlMgPSB7InRyYWluZWQiOiAibyIsICJ1bnRyYWluZWQiOiAicyIsICJkaW5vdjIiOiAiXiIsICJvcmFjbGUiOiAiRCJ9CgoKZGVmIHBsb3RfbGF5ZXJfcmhvKGFsbF9kYXRhLCBvcmFjbGVfcmhvLCBvdXRwdXRfZGlyKToKICAgIGZpZywgYXggPSBwbHQuc3VicGxvdHMoZmlnc2l6ZT0oMTAsIDUpKQoKICAgIGZvciBuYW1lLCBkYXRhIGluIGFsbF9kYXRhLml0ZW1zKCk6CiAgICAgICAgbGF5ZXJzLCByaG9zID0gZXh0cmFjdF9sYXllcl9tZXRyaWNzKGRhdGEsICJzcGVhcm1hbl9yaG8iKQogICAgICAgIGlmIGxlbihsYXllcnMpID09IDA6CiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgYXgucGxvdChsYXllcnMsIHJob3MsCiAgICAgICAgICAgICAgICBtYXJrZXI9TUFSS0VSUy5nZXQobmFtZSwgIm8iKSwKICAgICAgICAgICAgICAgIGNvbG9yPUNPTE9SUy5nZXQobmFtZSwgIiM5OTkiKSwKICAgICAgICAgICAgICAgIGxhYmVsPW5hbWUsIGxpbmV3aWR0aD0yLCBtYXJrZXJzaXplPTUpCgogICAgaWYgb3JhY2xlX3JobyBpcyBub3QgTm9uZToKICAgICAgICBheC5heGhsaW5lKHk9b3JhY2xlX3JobywgY29sb3I9Q09MT1JTWyJvcmFjbGUiXSwKICAgICAgICAgICAgICAgICAgIGxpbmVzdHlsZT0iLS0iLCBsYWJlbD1mIm9yYWNsZSAocmhvPXtvcmFjbGVfcmhvOi4zZn0pIiwgYWxwaGE9MC43KQoKICAgIGF4LnNldF94bGFiZWwoIkxheWVyIikKICAgIGF4LnNldF95bGFiZWwoIlNwZWFybWFuIHJobyIpCiAgICBheC5zZXRfdGl0bGUoIlRlbXBvcmFsIERpc3RhbmNlIFByb2JlOiBMYXllci13aXNlIFNwZWFybWFuIHJobyIpCiAgICBheC5sZWdlbmQoKQogICAgYXguZ3JpZChUcnVlLCBhbHBoYT0wLjMpCgogICAgcGF0aCA9IG9zLnBhdGguam9pbihvdXRwdXRfZGlyLCAibGF5ZXJfcmhvLnBuZyIpCiAgICBmaWcuc2F2ZWZpZyhwYXRoLCBkcGk9MTUwLCBiYm94X2luY2hlcz0idGlnaHQiKQogICAgZmlnLnNhdmVmaWcocGF0aC5yZXBsYWNlKCIucG5nIiwgIi5wZGYiKSwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgIHBsdC5jbG9zZShmaWcpCiAgICBwcmludChmIlNhdmVkIHtwYXRofSIpCgoKZGVmIHBsb3RfZGVsdGFfcmhvKGFsbF9kYXRhLCBvdXRwdXRfZGlyKToKICAgIGlmICJ0cmFpbmVkIiBub3QgaW4gYWxsX2RhdGEgb3IgInVudHJhaW5lZCIgbm90IGluIGFsbF9kYXRhOgogICAgICAgIHByaW50KCJTa2lwcGluZyBkZWx0YS1yaG8gcGxvdCAobmVlZCB0cmFpbmVkICsgdW50cmFpbmVkKSIpCiAgICAgICAgcmV0dXJuCgogICAgbF90ciwgcmhvX3RyID0gZXh0cmFjdF9sYXllcl9tZXRyaWNzKGFsbF9kYXRhWyJ0cmFpbmVkIl0sICJzcGVhcm1hbl9yaG8iKQogICAgbF91biwgcmhvX3VuID0gZXh0cmFjdF9sYXllcl9tZXRyaWNzKGFsbF9kYXRhWyJ1bnRyYWluZWQiXSwgInNwZWFybWFuX3JobyIpCgogICAgdHJfbWFwID0gZGljdCh6aXAobF90ci50b2xpc3QoKSwgcmhvX3RyLnRvbGlzdCgpKSkKICAgIHVuX21hcCA9IGRpY3QoemlwKGxfdW4udG9saXN0KCksIHJob191bi50b2xpc3QoKSkpCiAgICBjb21tb24gPSBzb3J0ZWQoc2V0KGxfdHIudG9saXN0KCkpICYgc2V0KGxfdW4udG9saXN0KCkpKQogICAgaWYgbm90IGNvbW1vbjoKICAgICAgICByZXR1cm4KCiAgICBsYXllcnMgPSBucC5hcnJheShjb21tb24pCiAgICBkZWx0YXMgPSBucC5hcnJheShbdHJfbWFwW2xdIC0gdW5fbWFwW2xdIGZvciBsIGluIGNvbW1vbl0pCgogICAgZmlnLCBheCA9IHBsdC5zdWJwbG90cyhmaWdzaXplPSgxMCwgNSkpCiAgICBjb2xvcnMgPSBbIiMyMTk2RjMiIGlmIGQgPj0gMCBlbHNlICIjRjQ0MzM2IiBmb3IgZCBpbiBkZWx0YXNdCiAgICBheC5iYXIobGF5ZXJzLCBkZWx0YXMsIGNvbG9yPWNvbG9ycywgd2lkdGg9MC44KQogICAgYXguYXhobGluZSh5PTAuMSwgY29sb3I9ImdyZWVuIiwgbGluZXN0eWxlPSItLSIsIGFscGhhPTAuNSwgbGFiZWw9InRocmVzaG9sZD0wLjEiKQogICAgYXguYXhobGluZSh5PTAsIGNvbG9yPSJibGFjayIsIGxpbmV3aWR0aD0wLjUpCiAgICBheC5zZXRfeGxhYmVsKCJMYXllciIpCiAgICBheC5zZXRfeWxhYmVsKCJEZWx0YS1yaG8gKHRyYWluZWQgLSB1bnRyYWluZWQpIikKICAgIGF4LnNldF90aXRsZSgiVGVtcG9yYWwgRGlzdGFuY2UgUHJvYmU6IERlbHRhLXJobyBwZXIgTGF5ZXIiKQogICAgYXgubGVnZW5kKCkKICAgIGF4LmdyaWQoVHJ1ZSwgYWxwaGE9MC4zKQoKICAgIHBhdGggPSBvcy5wYXRoLmpvaW4ob3V0cHV0X2RpciwgImRlbHRhX3Joby5wbmciKQogICAgZmlnLnNhdmVmaWcocGF0aCwgZHBpPTE1MCwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgIGZpZy5zYXZlZmlnKHBhdGgucmVwbGFjZSgiLnBuZyIsICIucGRmIiksIGJib3hfaW5jaGVzPSJ0aWdodCIpCiAgICBwbHQuY2xvc2UoZmlnKQogICAgcHJpbnQoZiJTYXZlZCB7cGF0aH0iKQoKCmRlZiBwbG90X3N1YnRhc2tfYXVjX2hlYXRtYXAoZGF0YSwgb3V0cHV0X2RpciwgbmFtZT0idHJhaW5lZCIpOgogICAgcmVzdWx0cyA9IGRhdGEuZ2V0KCJyZXN1bHRzIiwge30pCiAgICBsYXllcnMgPSBzb3J0ZWQoW2ludChrKSBmb3IgayBpbiByZXN1bHRzIGlmIGsgIT0gIm9yYWNsZSJdKQogICAgaWYgbm90IGxheWVyczoKICAgICAgICByZXR1cm4KCiAgICBwcmVkX25hbWVzID0gTm9uZQogICAgZm9yIHYgaW4gcmVzdWx0cy52YWx1ZXMoKToKICAgICAgICBpZiAicHJlZGljYXRlX25hbWVzIiBpbiB2OgogICAgICAgICAgICBwcmVkX25hbWVzID0gdlsicHJlZGljYXRlX25hbWVzIl0KICAgICAgICAgICAgYnJlYWsKICAgIGlmIHByZWRfbmFtZXMgaXMgTm9uZToKICAgICAgICByZXR1cm4KCiAgICBuX3ByZWQgPSBsZW4ocHJlZF9uYW1lcykKICAgIGhlYXRtYXAgPSBucC5mdWxsKChsZW4obGF5ZXJzKSwgbl9wcmVkKSwgbnAubmFuKQoKICAgIGZvciBsaSwgbGF5ZXIgaW4gZW51bWVyYXRlKGxheWVycyk6CiAgICAgICAgYXVjID0gcmVzdWx0c1tzdHIobGF5ZXIpXS5nZXQoImF1Y19wZXJfcHJlZGljYXRlIiwge30pCiAgICAgICAgZm9yIGsgaW4gcmFuZ2Uobl9wcmVkKToKICAgICAgICAgICAgdmFsID0gYXVjLmdldChzdHIoayksIG5wLm5hbikKICAgICAgICAgICAgaGVhdG1hcFtsaSwga10gPSB2YWwKCiAgICBmaWcsIGF4ID0gcGx0LnN1YnBsb3RzKGZpZ3NpemU9KG1heCg4LCBuX3ByZWQpLCBtYXgoNiwgbGVuKGxheWVycykgKiAwLjMpKSkKICAgIGltID0gYXguaW1zaG93KGhlYXRtYXAsIGFzcGVjdD0iYXV0byIsIGNtYXA9IllsT3JSZCIsIHZtaW49MC41LCB2bWF4PTEuMCkKICAgIGF4LnNldF94dGlja3MocmFuZ2Uobl9wcmVkKSkKICAgIGF4LnNldF94dGlja2xhYmVscyhwcmVkX25hbWVzLCByb3RhdGlvbj00NSwgaGE9InJpZ2h0IiwgZm9udHNpemU9OCkKICAgIGF4LnNldF95dGlja3MocmFuZ2UobGVuKGxheWVycykpKQogICAgYXguc2V0X3l0aWNrbGFiZWxzKGxheWVycykKICAgIGF4LnNldF94bGFiZWwoIlByZWRpY2F0ZSIpCiAgICBheC5zZXRfeWxhYmVsKCJMYXllciIpCiAgICBheC5zZXRfdGl0bGUoZiJTdWItdGFzayBQcmVkaWNhdGUgQVVDICh7bmFtZX0pIikKICAgIGZpZy5jb2xvcmJhcihpbSwgYXg9YXgsIGxhYmVsPSJBVUMtUk9DIikKCiAgICBwYXRoID0gb3MucGF0aC5qb2luKG91dHB1dF9kaXIsIGYic3VidGFza19hdWNfe25hbWV9LnBuZyIpCiAgICBmaWcuc2F2ZWZpZyhwYXRoLCBkcGk9MTUwLCBiYm94X2luY2hlcz0idGlnaHQiKQogICAgZmlnLnNhdmVmaWcocGF0aC5yZXBsYWNlKCIucG5nIiwgIi5wZGYiKSwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgIHBsdC5jbG9zZShmaWcpCiAgICBwcmludChmIlNhdmVkIHtwYXRofSIpCgoKZGVmIHBsb3RfcGVyX2xheWVyX3Job19wcm9maWxlKGFsbF9kYXRhLCBvdXRwdXRfZGlyKToKICAgIGZpZywgYXggPSBwbHQuc3VicGxvdHMoZmlnc2l6ZT0oMTAsIDUpKQoKICAgIGZvciBuYW1lIGluIFsidHJhaW5lZCIsICJ1bnRyYWluZWQiXToKICAgICAgICBpZiBuYW1lIG5vdCBpbiBhbGxfZGF0YToKICAgICAgICAgICAgY29udGludWUKICAgICAgICBsYXllcnMsIHJob3MgPSBleHRyYWN0X2xheWVyX21ldHJpY3MoYWxsX2RhdGFbbmFtZV0sICJzcGVhcm1hbl9yaG8iKQogICAgICAgIGlmIGxlbihsYXllcnMpID09IDA6CiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgYXgucGxvdChsYXllcnMsIHJob3MsCiAgICAgICAgICAgICAgICBtYXJrZXI9TUFSS0VSUy5nZXQobmFtZSwgIm8iKSwKICAgICAgICAgICAgICAgIGNvbG9yPUNPTE9SUy5nZXQobmFtZSwgIiM5OTkiKSwKICAgICAgICAgICAgICAgIGxhYmVsPW5hbWUsIGxpbmV3aWR0aD0yLCBtYXJrZXJzaXplPTUpCgogICAgaWYgImRpbm92MiIgaW4gYWxsX2RhdGE6CiAgICAgICAgXywgcmhvX2Rpbm8gPSBleHRyYWN0X2xheWVyX21ldHJpY3MoYWxsX2RhdGFbImRpbm92MiJdLCAic3BlYXJtYW5fcmhvIikKICAgICAgICBpZiBsZW4ocmhvX2Rpbm8pID4gMDoKICAgICAgICAgICAgZGlub192YWwgPSBmbG9hdChyaG9fZGluby5tYXgoKSkKICAgICAgICAgICAgYXguYXhobGluZSh5PWRpbm9fdmFsLCBjb2xvcj1DT0xPUlMuZ2V0KCJkaW5vdjIiLCAiIzRDQUY1MCIpLAogICAgICAgICAgICAgICAgICAgICAgIGxpbmVzdHlsZT0iLS0iLCBsaW5ld2lkdGg9MiwKICAgICAgICAgICAgICAgICAgICAgICBsYWJlbD1mIkRJTk8tVjIgKHJobz17ZGlub192YWw6LjNmfSkiKQoKICAgIGF4LnNldF94bGFiZWwoIkxheWVyIEluZGV4IikKICAgIGF4LnNldF95bGFiZWwoIlNwZWFybWFuIHJobyIpCiAgICBheC5zZXRfdGl0bGUoIlBlci1sYXllciByaG8gUHJvZmlsZTogVkxBICh0cmFpbmVkL3VudHJhaW5lZCkgdnMgRElOTy1WMiIpCiAgICBheC5sZWdlbmQoKQogICAgYXguZ3JpZChUcnVlLCBhbHBoYT0wLjMpCgogICAgcGF0aCA9IG9zLnBhdGguam9pbihvdXRwdXRfZGlyLCAicGVyX2xheWVyX3Job19wcm9maWxlLnBuZyIpCiAgICBmaWcuc2F2ZWZpZyhwYXRoLCBkcGk9MTUwLCBiYm94X2luY2hlcz0idGlnaHQiKQogICAgZmlnLnNhdmVmaWcocGF0aC5yZXBsYWNlKCIucG5nIiwgIi5wZGYiKSwgYmJveF9pbmNoZXM9InRpZ2h0IikKICAgIHBsdC5jbG9zZShmaWcpCiAgICBwcmludChmIlNhdmVkIHtwYXRofSIpCgoKIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KIyBKdWRnbWVudAojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PQoKZGVmIGJvb3RzdHJhcF9kZWx0YV9yaG8odHJhaW5lZF9yaG9zLCB1bnRyYWluZWRfcmhvcywgbl9ib290c3RyYXA9MTAwMCwgc2VlZD00Mik6CiAgICBybmcgPSBucC5yYW5kb20uUmFuZG9tU3RhdGUoc2VlZCkKICAgIGRlbHRhcyA9IFtdCiAgICBuID0gbGVuKHRyYWluZWRfcmhvcykKICAgIGZvciBfIGluIHJhbmdlKG5fYm9vdHN0cmFwKToKICAgICAgICBpZHggPSBybmcuY2hvaWNlKG4sIG4sIHJlcGxhY2U9VHJ1ZSkKICAgICAgICBkZWx0YSA9IG5wLm1lYW4obnAuYXJyYXkodHJhaW5lZF9yaG9zKVtpZHhdKSAtIG5wLm1lYW4obnAuYXJyYXkodW50cmFpbmVkX3Job3MpW2lkeF0pCiAgICAgICAgZGVsdGFzLmFwcGVuZChkZWx0YSkKICAgIGRlbHRhcyA9IHNvcnRlZChkZWx0YXMpCiAgICBjaV9sb3dlciA9IGRlbHRhc1tpbnQoMC4wMjUgKiBuX2Jvb3RzdHJhcCldCiAgICBjaV91cHBlciA9IGRlbHRhc1tpbnQoMC45NzUgKiBuX2Jvb3RzdHJhcCldCiAgICByZXR1cm4gbnAubWVhbihkZWx0YXMpLCBjaV9sb3dlciwgY2lfdXBwZXIKCgpkZWYgY29tcHV0ZV9qdWRnbWVudChhbGxfZGF0YSk6CiAgICAiIiJQQVNTL0ZBSUwgYmFzZWQgb24gdGhyZWUgY3JpdGVyaWEgKEQwMDEgY2FsaWJyYXRpb24pLiIiIgogICAgY3JpdGVyaWEgPSB7fQoKICAgICMgMSkgYmVzdCByaG8gPiAwLjUKICAgIGlmICJ0cmFpbmVkIiBpbiBhbGxfZGF0YToKICAgICAgICBsYXllcnMsIHJob3MgPSBleHRyYWN0X2xheWVyX21ldHJpY3MoYWxsX2RhdGFbInRyYWluZWQiXSwgInNwZWFybWFuX3JobyIpCiAgICAgICAgYmVzdF9yaG8gPSBmbG9hdChyaG9zLm1heCgpKSBpZiBsZW4ocmhvcykgPiAwIGVsc2UgMC4wCiAgICAgICAgYmVzdF9sYXllciA9IGludChsYXllcnNbbnAuYXJnbWF4KHJob3MpXSkgaWYgbGVuKHJob3MpID4gMCBlbHNlIC0xCiAgICBlbHNlOgogICAgICAgIGJlc3RfcmhvLCBiZXN0X2xheWVyID0gMC4wLCAtMQoKICAgIGNyaXRlcmlhWyJiZXN0X3JobyJdID0gYmVzdF9yaG8KICAgIGNyaXRlcmlhWyJiZXN0X2xheWVyIl0gPSBiZXN0X2xheWVyCiAgICBjcml0ZXJpYVsicmhvX3Bhc3MiXSA9IGJlc3RfcmhvID4gMC41CgogICAgIyAyKSBkZWx0YS1yaG8gPiAwLjEgd2l0aCBib290c3RyYXBwZWQgOTUlIENJIGV4Y2x1ZGluZyAwCiAgICBtYXhfZGVsdGEgPSAwLjAKICAgIGRlbHRhX2NpX2xvd2VyID0gMC4wCiAgICBkZWx0YV9jaV91cHBlciA9IDAuMAogICAgY2lfZXhjbHVkZXNfemVybyA9IEZhbHNlCiAgICBpZiAidHJhaW5lZCIgaW4gYWxsX2RhdGEgYW5kICJ1bnRyYWluZWQiIGluIGFsbF9kYXRhOgogICAgICAgIGxfdHIsIHJob190ciA9IGV4dHJhY3RfbGF5ZXJfbWV0cmljcyhhbGxfZGF0YVsidHJhaW5lZCJdLCAic3BlYXJtYW5fcmhvIikKICAgICAgICBsX3VuLCByaG9fdW4gPSBleHRyYWN0X2xheWVyX21ldHJpY3MoYWxsX2RhdGFbInVudHJhaW5lZCJdLCAic3BlYXJtYW5fcmhvIikKICAgICAgICB0cl9tYXAgPSBkaWN0KHppcChsX3RyLnRvbGlzdCgpLCByaG9fdHIudG9saXN0KCkpKQogICAgICAgIHVuX21hcCA9IGRpY3QoemlwKGxfdW4udG9saXN0KCksIHJob191bi50b2xpc3QoKSkpCiAgICAgICAgY29tbW9uID0gc2V0KGxfdHIudG9saXN0KCkpICYgc2V0KGxfdW4udG9saXN0KCkpCiAgICAgICAgaWYgY29tbW9uOgogICAgICAgICAgICBtYXhfZGVsdGEgPSBtYXgodHJfbWFwW2xdIC0gdW5fbWFwW2xdIGZvciBsIGluIGNvbW1vbikKICAgICAgICAgICAgdHJhaW5lZF9yaG9zID0gW3RyX21hcFtsXSBmb3IgbCBpbiBzb3J0ZWQoY29tbW9uKV0KICAgICAgICAgICAgdW50cmFpbmVkX3Job3MgPSBbdW5fbWFwW2xdIGZvciBsIGluIHNvcnRlZChjb21tb24pXQogICAgICAgICAgICBfLCBkZWx0YV9jaV9sb3dlciwgZGVsdGFfY2lfdXBwZXIgPSBib290c3RyYXBfZGVsdGFfcmhvKAogICAgICAgICAgICAgICAgdHJhaW5lZF9yaG9zLCB1bnRyYWluZWRfcmhvcwogICAgICAgICAgICApCiAgICAgICAgICAgIGNpX2V4Y2x1ZGVzX3plcm8gPSBkZWx0YV9jaV9sb3dlciA+IDAKCiAgICBjcml0ZXJpYVsibWF4X2RlbHRhX3JobyJdID0gbWF4X2RlbHRhCiAgICBjcml0ZXJpYVsiZGVsdGFfY2lfbG93ZXIiXSA9IGRlbHRhX2NpX2xvd2VyCiAgICBjcml0ZXJpYVsiZGVsdGFfY2lfdXBwZXIiXSA9IGRlbHRhX2NpX3VwcGVyCiAgICBjcml0ZXJpYVsiY2lfZXhjbHVkZXNfemVybyJdID0gY2lfZXhjbHVkZXNfemVybwogICAgY3JpdGVyaWFbImRlbHRhX3Bhc3MiXSA9IG1heF9kZWx0YSA+IDAuMSBhbmQgY2lfZXhjbHVkZXNfemVybwoKICAgICMgMykgVkxBX3JobyA+PSBESU5PX3JobyBPUiAoc3VidGFza19BVUMgPiAwLjcgQU5EIHN1YnRhc2tfQVVDID4gRElOT19zdWJ0YXNrX0FVQyArIDAuMDUpCiAgICB2bGFfZ2VfZGlubyA9IEZhbHNlCiAgICBpZiAidHJhaW5lZCIgaW4gYWxsX2RhdGEgYW5kICJkaW5vdjIiIGluIGFsbF9kYXRhOgogICAgICAgIF8sIHJob192bGEgPSBleHRyYWN0X2xheWVyX21ldHJpY3MoYWxsX2RhdGFbInRyYWluZWQiXSwgInNwZWFybWFuX3JobyIpCiAgICAgICAgXywgcmhvX2Rpbm8gPSBleHRyYWN0X2xheWVyX21ldHJpY3MoYWxsX2RhdGFbImRpbm92MiJdLCAic3BlYXJtYW5fcmhvIikKICAgICAgICBpZiBsZW4ocmhvX3ZsYSkgPiAwIGFuZCBsZW4ocmhvX2Rpbm8pID4gMDoKICAgICAgICAgICAgdmxhX2dlX2Rpbm8gPSBmbG9hdChyaG9fdmxhLm1heCgpKSA+PSBmbG9hdChyaG9fZGluby5tYXgoKSkKCiAgICB2bGFfYmVzdF9hdWMgPSAwLjAKICAgIGRpbm9fYmVzdF9hdWMgPSAwLjAKICAgIGlmICJ0cmFpbmVkIiBpbiBhbGxfZGF0YToKICAgICAgICBmb3IgdiBpbiBhbGxfZGF0YVsidHJhaW5lZCJdLmdldCgicmVzdWx0cyIsIHt9KS52YWx1ZXMoKToKICAgICAgICAgICAgaWYgaXNpbnN0YW5jZSh2LmdldCgibWFjcm9fYXVjIiksIChpbnQsIGZsb2F0KSk6CiAgICAgICAgICAgICAgICB2bGFfYmVzdF9hdWMgPSBtYXgodmxhX2Jlc3RfYXVjLCB2WyJtYWNyb19hdWMiXSkKICAgIGlmICJkaW5vdjIiIGluIGFsbF9kYXRhOgogICAgICAgIGZvciB2IGluIGFsbF9kYXRhWyJkaW5vdjIiXS5nZXQoInJlc3VsdHMiLCB7fSkudmFsdWVzKCk6CiAgICAgICAgICAgIGlmIGlzaW5zdGFuY2Uodi5nZXQoIm1hY3JvX2F1YyIpLCAoaW50LCBmbG9hdCkpOgogICAgICAgICAgICAgICAgZGlub19iZXN0X2F1YyA9IG1heChkaW5vX2Jlc3RfYXVjLCB2WyJtYWNyb19hdWMiXSkKICAgIHN1YnRhc2tfcGFzcyA9IHZsYV9iZXN0X2F1YyA+IDAuNyBhbmQgdmxhX2Jlc3RfYXVjID4gZGlub19iZXN0X2F1YyArIDAuMDUKCiAgICBjcml0ZXJpYVsidmxhX2dlX2Rpbm92MiJdID0gdmxhX2dlX2Rpbm8KICAgIGNyaXRlcmlhWyJ2bGFfYmVzdF9hdWMiXSA9IHZsYV9iZXN0X2F1YwogICAgY3JpdGVyaWFbImRpbm9fYmVzdF9hdWMiXSA9IGRpbm9fYmVzdF9hdWMKICAgIGNyaXRlcmlhWyJzdWJ0YXNrX2F1Y19wYXNzIl0gPSBzdWJ0YXNrX3Bhc3MKICAgIGNyaXRlcmlhWyJ0aGlyZF9jcml0ZXJpb24iXSA9IHZsYV9nZV9kaW5vIG9yIHN1YnRhc2tfcGFzcwoKICAgIGlmIGNyaXRlcmlhWyJyaG9fcGFzcyJdIGFuZCBjcml0ZXJpYVsiZGVsdGFfcGFzcyJdIGFuZCBjcml0ZXJpYVsidGhpcmRfY3JpdGVyaW9uIl06CiAgICAgICAganVkZ21lbnQgPSAiUEFTUyIKICAgIGVsaWYgY3JpdGVyaWFbImRlbHRhX3Bhc3MiXSBhbmQgbm90IGNyaXRlcmlhWyJ0aGlyZF9jcml0ZXJpb24iXToKICAgICAgICBqdWRnbWVudCA9ICJDT05ESVRJT05BTCIKICAgIGVsc2U6CiAgICAgICAganVkZ21lbnQgPSAiRkFJTCIKCiAgICByZWFzb25zID0gW10KICAgIGlmIG5vdCBjcml0ZXJpYVsicmhvX3Bhc3MiXToKICAgICAgICByZWFzb25zLmFwcGVuZChmImJlc3QgcmhvID0ge2Jlc3RfcmhvOi40Zn0gPD0gMC41IikKICAgIGlmIG5vdCBjcml0ZXJpYVsiZGVsdGFfcGFzcyJdOgogICAgICAgIGlmIG1heF9kZWx0YSA8PSAwLjE6CiAgICAgICAgICAgIHJlYXNvbnMuYXBwZW5kKGYibWF4IGRlbHRhLXJobyA9IHttYXhfZGVsdGE6LjRmfSA8PSAwLjEiKQogICAgICAgIGVsaWYgbm90IGNpX2V4Y2x1ZGVzX3plcm86CiAgICAgICAgICAgIHJlYXNvbnMuYXBwZW5kKGYiZGVsdGEtcmhvIENJIFt7ZGVsdGFfY2lfbG93ZXI6LjRmfSwge2RlbHRhX2NpX3VwcGVyOi40Zn1dIGluY2x1ZGVzIDAiKQogICAgaWYgbm90IGNyaXRlcmlhWyJ0aGlyZF9jcml0ZXJpb24iXToKICAgICAgICByZWFzb25zLmFwcGVuZCgiVkxBIDwgRElOTy1WMiBBTkQgc3VidGFzayBnYXRlIG5vdCBtZXQiKQoKICAgIHJldHVybiBkaWN0KGp1ZGdtZW50PWp1ZGdtZW50LCBjcml0ZXJpYT1jcml0ZXJpYSwKICAgICAgICAgICAgICAgIHJlYXNvbnM9cmVhc29ucyBpZiByZWFzb25zIGVsc2UgWyJBbGwgY3JpdGVyaWEgbWV0Il0pCgoKIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KIyBNYWluCiMgPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09CgpkZWYgbWFpbigpOgogICAgYXJncyA9IHBhcnNlX2FyZ3MoKQogICAgb3MubWFrZWRpcnMoYXJncy5vdXRwdXRfZGlyLCBleGlzdF9vaz1UcnVlKQoKICAgIGRpcnMgPSBwYXJzZV9yZXN1bHRzX2RpcnMoYXJncy5yZXN1bHRzX2RpcnMpCiAgICBwcmludChmIkxvYWRpbmcgcmVzdWx0czoge2xpc3QoZGlycy5rZXlzKCkpfSIpCgogICAgYWxsX2RhdGEgPSB7fQogICAgZm9yIG5hbWUsIHBhdGggaW4gZGlycy5pdGVtcygpOgogICAgICAgIHRyeToKICAgICAgICAgICAgZGF0YSA9IGxvYWRfcmVzdWx0cyhwYXRoLCBhcmdzLnByb2JlX3R5cGUpCiAgICAgICAgICAgIGFsbF9kYXRhW25hbWVdID0gZGF0YQogICAgICAgICAgICBuID0gbGVuKGRhdGEuZ2V0KCJyZXN1bHRzIiwge30pKQogICAgICAgICAgICBwcmludChmIiAge25hbWV9OiB7bn0gZW50cmllcyIpCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgICAgICBwcmludChmIiAge25hbWV9OiBGQUlMRUQgKHtlfSkiKQoKICAgIGlmIG5vdCBhbGxfZGF0YToKICAgICAgICBwcmludCgiTm8gZGF0YSBsb2FkZWQuIikKICAgICAgICByZXR1cm4KCiAgICBvcmFjbGVfcmhvID0gbG9hZF9vcmFjbGUoZGlycykKICAgIGlmIG9yYWNsZV9yaG8gaXMgbm90IE5vbmU6CiAgICAgICAgcHJpbnQoZiJPcmFjbGUgcmhvOiB7b3JhY2xlX3JobzouNGZ9IikKCiAgICAjIC0tLSBDb21wYXJpc29uIHRhYmxlIC0tLQogICAgcHJpbnQoIlxuPT09IExheWVyLXdpc2UgU3BlYXJtYW4gcmhvID09PSIpCiAgICBuYW1lcyA9IGxpc3QoYWxsX2RhdGEua2V5cygpKQogICAgaGVhZGVyID0gWyJMYXllciJdICsgbmFtZXMKICAgIHByaW50KCIgfCAiLmpvaW4oZiJ7aDo+MTJ9IiBmb3IgaCBpbiBoZWFkZXIpKQogICAgcHJpbnQoIi0iICogKDE0ICogbGVuKGhlYWRlcikpKQoKICAgIGFsbF9sYXllcnMgPSBzZXQoKQogICAgZm9yIGRhdGEgaW4gYWxsX2RhdGEudmFsdWVzKCk6CiAgICAgICAgbGF5ZXJzLCBfID0gZXh0cmFjdF9sYXllcl9tZXRyaWNzKGRhdGEsICJzcGVhcm1hbl9yaG8iKQogICAgICAgIGFsbF9sYXllcnMudXBkYXRlKGxheWVycy50b2xpc3QoKSkKCiAgICBmb3IgbGF5ZXIgaW4gc29ydGVkKGFsbF9sYXllcnMpOgogICAgICAgIHJvdyA9IFtmIntsYXllcjo+MTJ9Il0KICAgICAgICBmb3IgbmFtZSBpbiBuYW1lczoKICAgICAgICAgICAgbGF5ZXJzLCByaG9zID0gZXh0cmFjdF9sYXllcl9tZXRyaWNzKGFsbF9kYXRhW25hbWVdLCAic3BlYXJtYW5fcmhvIikKICAgICAgICAgICAgbG1hcCA9IGRpY3QoemlwKGxheWVycy50b2xpc3QoKSwgcmhvcy50b2xpc3QoKSkpCiAgICAgICAgICAgIHZhbCA9IGxtYXAuZ2V0KGxheWVyLCBmbG9hdCgibmFuIikpCiAgICAgICAgICAgIHJvdy5hcHBlbmQoZiJ7dmFsOj4xMi40Zn0iKQogICAgICAgIHByaW50KCIgfCAiLmpvaW4ocm93KSkKCiAgICBwcmludCgiXG49PT0gQmVzdCBMYXllciA9PT0iKQogICAgZm9yIG5hbWUsIGRhdGEgaW4gYWxsX2RhdGEuaXRlbXMoKToKICAgICAgICBsYXllcnMsIHJob3MgPSBleHRyYWN0X2xheWVyX21ldHJpY3MoZGF0YSwgInNwZWFybWFuX3JobyIpCiAgICAgICAgaWYgbGVuKHJob3MpID4gMDoKICAgICAgICAgICAgYmkgPSBpbnQobnAuYXJnbWF4KHJob3MpKQogICAgICAgICAgICBwcmludChmIiAge25hbWV9OiBsYXllciB7bGF5ZXJzW2JpXX0gKHJobz17cmhvc1tiaV06LjRmfSkiKQoKICAgICMgLS0tIFBsb3RzIC0tLQogICAgaWYgYXJncy5wcm9iZV90eXBlID09ICJ0ZW1wb3JhbF9kaXN0YW5jZSI6CiAgICAgICAgcGxvdF9sYXllcl9yaG8oYWxsX2RhdGEsIG9yYWNsZV9yaG8sIGFyZ3Mub3V0cHV0X2RpcikKICAgICAgICBwbG90X2RlbHRhX3JobyhhbGxfZGF0YSwgYXJncy5vdXRwdXRfZGlyKQogICAgICAgIHBsb3RfcGVyX2xheWVyX3Job19wcm9maWxlKGFsbF9kYXRhLCBhcmdzLm91dHB1dF9kaXIpCgogICAgaWYgYXJncy5wcm9iZV90eXBlID09ICJzdWJ0YXNrX3ByZWRpY2F0ZSI6CiAgICAgICAgZm9yIG5hbWUsIGRhdGEgaW4gYWxsX2RhdGEuaXRlbXMoKToKICAgICAgICAgICAgcGxvdF9zdWJ0YXNrX2F1Y19oZWF0bWFwKGRhdGEsIGFyZ3Mub3V0cHV0X2RpciwgbmFtZSkKCiAgICAjIC0tLSBKdWRnbWVudCAtLS0KICAgIGp1ZGdtZW50ID0gY29tcHV0ZV9qdWRnbWVudChhbGxfZGF0YSkKICAgIHByaW50KGYiXG49PT0gSnVkZ21lbnQ6IHtqdWRnbWVudFsnanVkZ21lbnQnXX0gPT09IikKICAgIGZvciBrLCB2IGluIGp1ZGdtZW50WyJjcml0ZXJpYSJdLml0ZW1zKCk6CiAgICAgICAgcHJpbnQoZiIgIHtrfToge3Z9IikKICAgIGZvciByIGluIGp1ZGdtZW50WyJyZWFzb25zIl06CiAgICAgICAgcHJpbnQoZiIgID4+IHtyfSIpCgogICAgIyAtLS0gU2F2ZSAtLS0KICAgIHN1bW1hcnkgPSBkaWN0KAogICAgICAgIG1vZGVscz1uYW1lcywKICAgICAgICBwcm9iZV90eXBlPWFyZ3MucHJvYmVfdHlwZSwKICAgICAgICBqdWRnbWVudD1qdWRnbWVudCwKICAgICkKICAgIGZvciBuYW1lLCBkYXRhIGluIGFsbF9kYXRhLml0ZW1zKCk6CiAgICAgICAgbGF5ZXJzLCByaG9zID0gZXh0cmFjdF9sYXllcl9tZXRyaWNzKGRhdGEsICJzcGVhcm1hbl9yaG8iKQogICAgICAgIGlmIGxlbihyaG9zKSA+IDA6CiAgICAgICAgICAgIGJpID0gaW50KG5wLmFyZ21heChyaG9zKSkKICAgICAgICAgICAgc3VtbWFyeVtuYW1lXSA9IGRpY3QoYmVzdF9sYXllcj1pbnQobGF5ZXJzW2JpXSksIGJlc3RfcmhvPWZsb2F0KHJob3NbYmldKSkKICAgIGlmIG9yYWNsZV9yaG8gaXMgbm90IE5vbmU6CiAgICAgICAgc3VtbWFyeVsib3JhY2xlX3JobyJdID0gb3JhY2xlX3JobwoKICAgIHdpdGggb3Blbihvcy5wYXRoLmpvaW4oYXJncy5vdXRwdXRfZGlyLCAic3VtbWFyeS5qc29uIiksICJ3IikgYXMgZjoKICAgICAgICBqc29uLmR1bXAoc3VtbWFyeSwgZiwgaW5kZW50PTIpCiAgICBwcmludChmIlxuU2F2ZWQge2FyZ3Mub3V0cHV0X2Rpcn0vc3VtbWFyeS5qc29uIikKCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigpCg==' | base64 -d > /root/vla-ssd/scripts/analyze_results.py && echo \"WRITE_OK\""
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T11:16:07.415039+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"WRITE_OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T11:16:07.415199+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "python3 -c \"import ast; ast.parse(open('/root/vla-ssd/scripts/analyze_results.py').read()); print('SYNTAX_OK')\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "python3 -c \"import ast; ast.parse(open('/root/vla-ssd/scripts/analyze_results.py').read()); print('SYNTAX_OK')\""
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T11:16:07.415329+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T11:16:07.415448+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "wc -l /root/vla-ssd/scripts/analyze_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "wc -l /root/vla-ssd/scripts/analyze_results.py"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T11:16:07.415567+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"448 /root/vla-ssd/scripts/analyze_results.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T11:16:07.415689+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"rho_pass\\|delta_pass\\|bootstrap_delta_rho\\|plot_per_layer_rho_profile\\|subtask_pass\\|0\\.5\\|0\\.3\\|ci_excludes_zero\\|dino_best_auc\\|vla_best_auc\" /root/vla-ssd/scripts/analyze_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"rho_pass\\|delta_pass\\|bootstrap_delta_rho\\|plot_per_layer_rho_profile\\|subtask_pass\\|0\\.5\\|0\\.3\\|ci_excludes_zero\\|dino_best_auc\\|vla_best_auc\" /root/vla-ssd/scripts/analyze_results.py"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T11:16:07.415806+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T11:16:07.415945+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19183",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"import ast; ast.parse(open('/root/vla-ssd/scripts/analyze_results.py').read()); print('SYNTAX_OK')\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19183",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"import ast; ast.parse(open('/root/vla-ssd/scripts/analyze_results.py').read()); print('SYNTAX_OK')\""
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T11:16:07.416093+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"SYNTAX_OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T11:16:07.416211+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"rho_pass\\|delta_pass\\|bootstrap_delta_rho\\|plot_per_layer_rho_profile\\|subtask_pass\\|ci_excludes_zero\\|dino_best_auc\\|vla_best_auc\" /root/vla-ssd/scripts/analyze_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"rho_pass\\|delta_pass\\|bootstrap_delta_rho\\|plot_per_layer_rho_profile\\|subtask_pass\\|ci_excludes_zero\\|dino_best_auc\\|vla_best_auc\" /root/vla-ssd/scripts/analyze_results.py"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T11:16:07.416327+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T11:16:07.416447+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"rho_pass\\|delta_pass\\|bootstrap_delta_rho\\|plot_per_layer_rho_profile\\|ci_excludes_zero\\|dino_best_auc\\|vla_best_auc\\|0\\.5\" /root/vla-ssd/scripts/analyze_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"rho_pass\\|delta_pass\\|bootstrap_delta_rho\\|plot_per_layer_rho_profile\\|ci_excludes_zero\\|dino_best_auc\\|vla_best_auc\\|0\\.5\" /root/vla-ssd/scripts/analyze_results.py"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T11:16:07.416567+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T11:16:07.416685+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"rho_pass\" /root/vla-ssd/scripts/analyze_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"rho_pass\" /root/vla-ssd/scripts/analyze_results.py"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T11:16:07.416806+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"277:    criteria[\\\"rho_pass\\\"] = best_rho > 0.5\\n331:    if criteria[\\\"rho_pass\\\"] and criteria[\\\"delta_pass\\\"] and criteria[\\\"third_criterion\\\"]:\\n339:    if not criteria[\\\"rho_pass\\\"]:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T11:16:07.416940+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"bootstrap_delta_rho\" /root/vla-ssd/scripts/analyze_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"bootstrap_delta_rho\" /root/vla-ssd/scripts/analyze_results.py"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T11:16:07.417102+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"249:def bootstrap_delta_rho(trained_rhos, untrained_rhos, n_bootstrap=1000, seed=42):\\n294:            _, delta_ci_lower, delta_ci_upper = bootstrap_delta_rho(\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T11:16:07.417221+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"plot_per_layer_rho_profile\" /root/vla-ssd/scripts/analyze_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"plot_per_layer_rho_profile\" /root/vla-ssd/scripts/analyze_results.py"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T11:16:07.417335+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"ci_excludes_zero\\|vla_best_auc\\|dino_best_auc\" /root/vla-ssd/scripts/analyze_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"ci_excludes_zero\\|vla_best_auc\\|dino_best_auc\" /root/vla-ssd/scripts/analyze_results.py"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T11:16:07.417451+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"210:def plot_per_layer_rho_profile(all_data, output_dir):\\n414:        plot_per_layer_rho_profile(all_data, args.output_dir)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T11:16:07.417576+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T11:16:07.417705+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"ci_excludes_zero\" /root/vla-ssd/scripts/analyze_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"ci_excludes_zero\" /root/vla-ssd/scripts/analyze_results.py"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T11:16:07.417825+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"283:    ci_excludes_zero = False\\n297:            ci_excludes_zero = delta_ci_lower > 0\\n302:    criteria[\\\"ci_excludes_zero\\\"] = ci_excludes_zero\\n303:    criteria[\\\"delta_pass\\\"] = max_delta > 0.1 and ci_excludes_zero\\n344:        elif not ci_excludes_zero:\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T11:16:07.417977+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"vla_best_auc\\|dino_best_auc\" /root/vla-ssd/scripts/analyze_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"vla_best_auc\\|dino_best_auc\" /root/vla-ssd/scripts/analyze_results.py"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T11:16:07.418128+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T11:16:07.418246+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"vla_best_auc\" /root/vla-ssd/scripts/analyze_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"vla_best_auc\" /root/vla-ssd/scripts/analyze_results.py"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T11:16:07.418365+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"313:    vla_best_auc = 0.0\\n318:                vla_best_auc = max(vla_best_auc, v[\\\"macro_auc\\\"])\\n323:    subtask_pass = vla_best_auc > 0.7 and vla_best_auc > dino_best_auc + 0.05\\n326:    criteria[\\\"vla_best_auc\\\"] = vla_best_auc\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T11:16:07.418479+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19183",
  "command": "grep -n \"subtask_pass\" /root/vla-ssd/scripts/analyze_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19183",
    "command": "grep -n \"subtask_pass\" /root/vla-ssd/scripts/analyze_results.py"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T11:16:07.418597+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"323:    subtask_pass = vla_best_auc > 0.7 and vla_best_auc > dino_best_auc + 0.05\\n328:    criteria[\\\"subtask_auc_pass\\\"] = subtask_pass\\n329:    criteria[\\\"third_criterion\\\"] = vla_ge_dino or subtask_pass\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_update-analyze-script_20260515T110435",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-15T11:16:07.418748+00:00_

全部改动验证通过。汇总：

| 改动 | 行号 | 状态 |
|------|------|------|
| ρ 下限 0.3→0.5 | L277 `best_rho > 0.5` | OK |
| `bootstrap_delta_rho()` | L249 定义, L294 调用 | OK |
| Δρ CI 排除 0 才 PASS | L303 `max_delta > 0.1 and ci_excludes_zero` | OK |
| subtask gate: `vla_AUC > 0.7 AND > dino_AUC + 0.05` | L323 | OK |
| `plot_per_layer_rho_profile()` | L210 定义, L414 调用 | OK |
| 三分支判定逻辑 | L331-337 | OK |
| 语法检查 | `ast.parse` SYNTAX_OK | OK |
| 原文件备份 | `analyze_results.py.bak` | OK |

文件从 377 行增长到 448 行（+71 行：bootstrap 函数、per-layer profile 图、更丰富的 criteria 字段）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_update-analyze-script_20260515T110435"
}
```

</details>

---
