# code cross alpha 5point script

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 0
- **Tool calls:** 31
- **Original source:** `logs/chats/worker_code_cross_alpha_5point_script_20260515T085132.jsonl`
- **Structured JSON:** [`96ec6688794b41afe59f.json`](../../sessions/96/96ec6688794b41afe59f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

63 recorded events

### Tool call

_source line 1 · 2026-05-15T09:02:00.691060+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__save_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__save_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T09:02:00.691392+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T09:02:00.691612+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T09:02:00.691805+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/consensus/consensus_framework.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/consensus/consensus_framework.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T09:02:00.692200+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Cross-alpha analysis for distributional canary collapse experiments.\\n\\nScans results/alpha_sweep/a*_s42/ directories, computes:\\n  1. Dose-response table (gen0->genN drift% per metric per alpha)\\n  2. Bidirectional permutation Granger causality with BH FDR correction\\n  3. Cross-correlation lead-lag analysis (delta-metric pairs)\\n  4. Per-generation velocity analysis for distinct_1\\n\\nInput:  results/alpha_sweep/a{NNN}_s42/all_metrics.json\\nOutput: results/analysis/cross_alpha_v{VERSION}.json + terminal summary\\n\\nDependencies: numpy, statsmodels\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport glob\\nimport json\\nimport os\\nimport re\\nimport sys\\nfrom datetime import datetime\\n\\nimport numpy as np\\nfrom statsmodels.stats.multitest import multipletests\\n\\n\\n# ---------------------------------------------------------------------------\\n# Data loading\\n# ---------------------------------------------------------------------------\\n\\nBASE_DIR = os.path.dirname(os.path.abspath(__file__))\\nSWEEP_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"alpha_sweep\\\")\\nANALYSIS_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"analysis\\\")\\n\\nMETRICS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"token_entropy\\\", \\\"ece\\\", \\\"perplexity\\\"]\\n\\n# Granger test pairs: (cause, effect, label)\\nGRANGER_PAIRS = [\\n    (\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"entropy->d1\\\"),\\n    (\\\"ece\\\",           \\\"distinct_1\\\", \\\"ECE->d1\\\"),\\n    (\\\"token_entropy\\\", \\\"distinct_2\\\", \\\"entropy->d2\\\"),\\n    (\\\"ece\\\",           \\\"distinct_2\\\", \\\"ECE->d2\\\"),\\n    (\\\"distinct_1\\\", \\\"token_entropy\\\", \\\"d1->entropy\\\"),\\n    (\\\"distinct_1\\\", \\\"ece\\\",           \\\"d1->ECE\\\"),\\n    (\\\"distinct_2\\\", \\\"token_entropy\\\", \\\"d2->entropy\\\"),\\n    (\\\"distinct_2\\\", \\\"ece\\\",           \\\"d2->ECE\\\"),\
…[truncated 7371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T09:02:00.692480+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T09:02:00.692684+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"cat: /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/consensus/consensus_framework.py: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T09:02:00.692870+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"a000_s42\\na025_s42\\na050_s42\\na075_s42\\nalpha_monotonicity.png\\nanalysis\\nanalysis_summary.json\\npooled_panel_results.json\\npooled_panel_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.57}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T09:02:00.693079+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"consensus_framework*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"consensus_framework*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T09:02:00.693272+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "wc -l /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "wc -l /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T09:02:00.693464+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/consensus_framework.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T09:02:00.693645+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"489 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T09:02:00.693812+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/consensus_framework.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/consensus_framework.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T09:02:00.693944+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -300 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -300 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T09:02:00.694184+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nMulti-method consensus framework for canary→downstream association robustness.\\n\\nFormalizes \\\"robust association\\\": a pair is robust only when ≥method_threshold\\nindependent statistical methods agree (each requiring ≥seed_threshold seeds\\nsignificant). Two-stage aggregation: seed→method verdict, then method→consensus.\\n\\nInput:  results/mvp/analysis/method_ablation.json\\nOutput: consensus classification, sensitivity heatmap, FPR/FNR table (JSON)\\n\\nDependencies: numpy, json (stdlib)\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\n\\nimport numpy as np\\n\\nMETHOD_NAMES = [\\n    \\\"naive_pearson\\\",\\n    \\\"differenced_xcorr\\\",\\n    \\\"threshold_onset\\\",\\n    \\\"toda_yamamoto\\\",\\n    \\\"permutation_granger\\\",\\n]\\n\\n# differenced_xcorr is the FP ground truth (index 1)\\nDIFF_INDEX = 1\\n\\n\\ndef _to_native(obj):\\n    \\\"\\\"\\\"Convert numpy types to Python native for JSON serialization.\\\"\\\"\\\"\\n    if isinstance(obj, (np.integer,)):\\n        return int(obj)\\n    if isinstance(obj, (np.floating,)):\\n        return float(obj)\\n    if isinstance(obj, (np.bool_,)):\\n        return bool(obj)\\n    if isinstance(obj, np.ndarray):\\n        return obj.tolist()\\n    return obj\\n\\n\\nclass NumpyEncoder(json.JSONEncoder):\\n    \\\"\\\"\\\"JSON encoder that handles numpy types.\\\"\\\"\\\"\\n    def default(self, obj):\\n        native = _to_native(obj)\\n        if native is not obj:\\n            return native\\n        return super().default(obj)\\n\\n\\ndef load_sig_matrix(ablation_path):\\n    \\\"\\\"\\\"\\n    Load method_ablation.json into a boolean significance tensor.\\n\\n    Args:\\n        ablation_path: path to method_ablation.json\\n\\n    Returns:\\n        sig_matrix: np.ndarray, shape (5, 16, 4), dtype bool\\n                    axes = (method, pair, seed)\\n        pair_names: list of (canary, downstream) tuples, len 16\\n        method_n
…[truncated 7220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T09:02:00.694512+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Cross-alpha analysis for distributional canary collapse experiments.\\n\\nScans results/alpha_sweep/a*_s42/ directories, computes:\\n  1. Dose-response table (gen0->genN drift% per metric per alpha)\\n  2. Bidirectional permutation Granger causality with BH FDR correction\\n  3. Cross-correlation lead-lag analysis (delta-metric pairs)\\n  4. Per-generation velocity analysis for distinct_1\\n\\nInput:  results/alpha_sweep/a{NNN}_s42/all_metrics.json\\nOutput: results/analysis/cross_alpha_v{VERSION}.json + terminal summary\\n\\nDependencies: numpy, statsmodels\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport glob\\nimport json\\nimport os\\nimport re\\nimport sys\\nfrom datetime import datetime\\n\\nimport numpy as np\\nfrom statsmodels.stats.multitest import multipletests\\n\\n\\n# ---------------------------------------------------------------------------\\n# Data loading\\n# ---------------------------------------------------------------------------\\n\\nBASE_DIR = os.path.dirname(os.path.abspath(__file__))\\nSWEEP_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"alpha_sweep\\\")\\nANALYSIS_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"analysis\\\")\\n\\nMETRICS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"token_entropy\\\", \\\"ece\\\", \\\"perplexity\\\"]\\n\\n# Granger test pairs: (cause, effect, label)\\nGRANGER_PAIRS = [\\n    (\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"entropy->d1\\\"),\\n    (\\\"ece\\\",           \\\"distinct_1\\\", \\\"ECE->d1\\\"),\\n    (\\\"token_entropy\\\", \\\"distinct_2\\\", \\\"entropy->d2\\\"),\\n    (\\\"ece\\\",           \\\"distinct_2\\\", \\\"ECE->d2\\\"),\\n    (\\\"distinct_1\\\", \\\"token_entropy\\\", \\\"d1->entropy\\\"),\\n    (\\\"distinct_1\\\", \\\"ece\\\",           \\\"d1->ECE\\\"),\\n    (\\\"distinct_2\\\", \\\"token_entropy\\\", \\\"d2->entropy\\\"),\\n    (\\\"distinct_2\\\", \\\"ece\\\",           \\\"d2->ECE\\\"),\
…[truncated 7224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T09:02:00.694698+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -190 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "tail -190 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T09:02:00.694950+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# ---------------------------------------------------------------------------\\n\\ndef auto_version():\\n    \\\"\\\"\\\"Find next version number by scanning existing analysis files.\\\"\\\"\\\"\\n    os.makedirs(ANALYSIS_DIR, exist_ok=True)\\n    existing = glob.glob(os.path.join(ANALYSIS_DIR, \\\"cross_alpha_v*.json\\\"))\\n    max_v = 0\\n    for f in existing:\\n        m = re.search(r\\\"cross_alpha_v(\\\\d+)\\\", f)\\n        if m:\\n            max_v = max(max_v, int(m.group(1)))\\n    return max_v + 1\\n\\n\\ndef print_summary(output):\\n    \\\"\\\"\\\"Print terminal summary tables.\\\"\\\"\\\"\\n    print(\\\"\\\\n\\\" + \\\"=\\\" * 80)\\n    print(\\\"CROSS-ALPHA ANALYSIS SUMMARY\\\")\\n    print(\\\"=\\\" * 80)\\n\\n    # Dose-response table\\n    dr = output[\\\"dose_response\\\"]\\n    alphas = sorted(dr.keys())\\n    print(f\\\"\\\\nDOSE-RESPONSE (drift %)\\\")\\n    print(\\\"-\\\" * 80)\\n    header = f\\\"{'Metric':<16}\\\"\\n    for ak in alphas:\\n        header += f\\\" | a={dr[ak]['alpha']:<5}\\\"\\n    print(header)\\n    print(\\\"-\\\" * 80)\\n    for metric in METRICS:\\n        line = f\\\"{metric:<16}\\\"\\n        for ak in alphas:\\n            d = dr[ak][metric][\\\"drift_pct\\\"]\\n            line += f\\\" | {d:>+7.1f}%\\\"\\n        print(line)\\n\\n    # Granger table\\n    gc = output[\\\"granger_causality\\\"]\\n    print(f\\\"\\\\nGRANGER CAUSALITY (bidirectional, differenced, permutation)\\\")\\n    print(\\\"-\\\" * 80)\\n    header = f\\\"{'Direction':<20}\\\"\\n    alpha_keys = sorted(set(r[\\\"alpha_key\\\"] for r in gc))\\n    for ak in alpha_keys:\\n        header += f\\\" | a={[r for r in gc if r['alpha_key']==ak][0]['alpha']:<4} p_raw   p_fdr\\\"\\n    print(header)\\n    print(\\\"-\\\" * 80)\\n\\n    directions = list(dict.fromkeys(r[\\\"direction\\\"] for r in gc))\\n    for d in directions:\\n        line = f\\\"{d:<20}\\\"\\n        for ak in alpha_keys:\\n   
…[truncated 6700 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T09:02:00.695100+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/mvp/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/mvp/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T09:02:00.695233+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analysis\\nanalysis_dryrun\\nanalysis_maxlag5_backup\\nrep_42\\nrep_42_v1_partial\\nrep_43\\nrep_43_v1_partial\\nrep_44\\nrep_45\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T09:02:00.695393+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T09:02:00.695519+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"all_metrics.json\\nconfig.json\\ngen_0\\ngen_1\\ngen_10\\ngen_2\\ngen_3\\ngen_4\\ngen_5\\ngen_6\\ngen_7\\ngen_8\\ngen_9\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T09:02:00.695658+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T09:02:00.695779+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analysis_summary.json\\nccf_maxlag7.json\\nconsensus\\ncross_correlation.png\\nlead_time_table.csv\\nmethod_ablation.json\\nmethod_ablation_dmax_sensitivity.json\\nmetric_trends.png\\npermutation_granger.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T09:02:00.695891+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -30 /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -30 /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T09:02:00.696024+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"seeds\\\": [\\n      42,\\n      43,\\n      44,\\n      45\\n    ],\\n    \\\"alpha\\\": 0.05,\\n    \\\"canary_metrics\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"self_bleu\\\",\\n      \\\"ece\\\",\\n      \\\"effective_rank\\\"\\n    ],\\n    \\\"downstream_metrics\\\": [\\n      \\\"perplexity\\\",\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\"\\n    ],\\n    \\\"methods\\\": [\\n      \\\"naive_pearson: raw-level Pearson lag-correlation\\\",\\n      \\\"differenced_xcorr: first-differenced cross-correlation\\\",\\n      \\\"threshold_onset: 2-sigma signal-onset lead time\\\",\\n      \\\"toda_yamamoto: augmented-lag Granger causality (Wald F-test)\\\",\\n      \\\"permutation_granger: differenced + shuffle permutation Granger (F-test)\\\"\\n    ]\\n  },\\n  \\\"summary\\\": {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T09:02:00.696151+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "wc -l /root/autodl-tmp/distrib_canary_collapse/consensus_framework.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "wc -l /root/autodl-tmp/distrib_canary_collapse/consensus_framework.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T09:02:00.696284+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"427 /root/autodl-tmp/distrib_canary_collapse/consensus_framework.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T09:02:00.696418+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -260 /root/autodl-tmp/distrib_canary_collapse/consensus_framework.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -260 /root/autodl-tmp/distrib_canary_collapse/consensus_framework.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T09:02:00.696708+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nMulti-method consensus framework for canary→downstream association robustness.\\n\\nFormalizes \\\"robust association\\\": a pair is robust only when ≥method_threshold\\nindependent statistical methods agree (each requiring ≥seed_threshold seeds\\nsignificant). Two-stage aggregation: seed→method verdict, then method→consensus.\\n\\nInput:  results/mvp/analysis/method_ablation.json\\nOutput: consensus classification, sensitivity heatmap, FPR/FNR table (JSON)\\n\\nDependencies: numpy, json (stdlib)\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\n\\nimport numpy as np\\n\\nMETHOD_NAMES = [\\n    \\\"naive_pearson\\\",\\n    \\\"differenced_xcorr\\\",\\n    \\\"threshold_onset\\\",\\n    \\\"toda_yamamoto\\\",\\n    \\\"permutation_granger\\\",\\n]\\n\\n# differenced_xcorr is the FP ground truth (index 1)\\nDIFF_INDEX = 1\\n\\n\\ndef _to_native(obj):\\n    \\\"\\\"\\\"Convert numpy types to Python native for JSON serialization.\\\"\\\"\\\"\\n    if isinstance(obj, (np.integer,)):\\n        return int(obj)\\n    if isinstance(obj, (np.floating,)):\\n        return float(obj)\\n    if isinstance(obj, (np.bool_,)):\\n        return bool(obj)\\n    if isinstance(obj, np.ndarray):\\n        return obj.tolist()\\n    return obj\\n\\n\\nclass NumpyEncoder(json.JSONEncoder):\\n    \\\"\\\"\\\"JSON encoder that handles numpy types.\\\"\\\"\\\"\\n    def default(self, obj):\\n        native = _to_native(obj)\\n        if native is not obj:\\n            return native\\n        return super().default(obj)\\n\\n\\ndef load_sig_matrix(ablation_path):\\n    \\\"\\\"\\\"\\n    Load method_ablation.json into a boolean significance tensor.\\n\\n    Args:\\n        ablation_path: path to method_ablation.json\\n\\n    Returns:\\n        sig_matrix: np.ndarray, shape (5, 16, 4), dtype bool\\n                    axes = (method, pair, seed)\\n        pair_names: list of (canary, downstream) tuples, len 16\\n        method_n
…[truncated 7115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T09:02:00.696936+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"method_ablation*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"method_ablation*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T09:02:00.697087+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/__pycache__/method_ablation.cpython-312.pyc\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation_dmax_sensitivity.json\\n/root/autodl-tmp/distrib_canary_collapse/method_ablation.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T09:02:00.697212+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"*.py\" -maxdepth 1 -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"*.py\" -maxdepth 1 -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T09:02:00.697384+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/metrics.py\\n/root/autodl-tmp/distrib_canary_collapse/iterative_train.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_data.py\\n/root/autodl-tmp/distrib_canary_collapse/analyze_mvp.py\\n/root/autodl-tmp/distrib_canary_collapse/method_ablation.py\\n/root/autodl-tmp/distrib_canary_collapse/dmax_sensitivity.py\\n/root/autodl-tmp/distrib_canary_collapse/analyze_alpha_sweep.py\\n/root/autodl-tmp/distrib_canary_collapse/bootstrap_ty_validation.py\\n/root/autodl-tmp/distrib_canary_collapse/detrending_utils.py\\n/root/autodl-tmp/distrib_canary_collapse/permutation_granger.py\\n/root/autodl-tmp/distrib_canary_collapse/analyze_extended.py\\n/root/autodl-tmp/distrib_canary_collapse/pooled_panel_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/extract_drift.py\\n/root/autodl-tmp/distrib_canary_collapse/gen_dose_response.py\\n/root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/cross_alpha_v3_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4.py\\n/root/autodl-tmp/distrib_canary_collapse/consensus_framework.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_v2.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_v3.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_v4.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T09:02:00.697515+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -120 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -120 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T09:02:00.697632+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"def \" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"def \" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T09:02:00.697834+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Method ablation: compare four lead-lag estimation methods.\\n\\nCompares naive vs robust approaches to detect canary->downstream lead-lag,\\nquantifying the spurious regression rate when non-stationary series are\\ncorrelated without proper detrending.\\n\\nInput:  results/mvp/rep_{seed}/all_metrics.json (seeds 42-45)\\nOutput: results/mvp/analysis/method_ablation.json\\n        (with BH FDR correction and effect sizes)\\n\\nMethods:\\n  1. Naive Pearson lag-correlation (raw levels)\\n  2. Differenced cross-correlation (first-differenced series)\\n  3. Threshold-based lead time (2-sigma onset detection)\\n  4. Toda-Yamamoto augmented-lag Granger causality\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport warnings\\nfrom itertools import product\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.stats.multitest import multipletests\\nfrom statsmodels.tsa.stattools import adfuller\\nfrom permutation_granger import permutation_granger_test\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nCANARY = [\\\"token_entropy\\\", \\\"self_bleu\\\", \\\"ece\\\", \\\"effective_rank\\\"]\\nDOWNSTREAM = [\\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"]\\n\\n# Sign conventions: \\\"higher is worse\\\" kept as-is; \\\"lower is worse\\\" negated\\n# so that degradation = positive direction in all analyses.\\nHIGHER_IS_WORSE = {\\\"self_bleu\\\", \\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"effective_rank\\\",\\n                   \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\nALPHA = 0.05\\n\\n\\ndef load_metrics(data_dir, seeds):\\n    \\\"\\\"\\\"Load all_metrics.json for each seed.\\\"\\\"\\\"\\n    data = {}\\n    for s in seeds:\\n        path = os.path.join(data_dir, f\\\"rep_{s}\\\", \\\"all_metrics.json\\\")\\n        with open(path) as f:\\n            data[s] = json.load(f)\\n    return 
…[truncated 2856 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T09:02:00.697992+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"44:def load_metrics(data_dir, seeds):\\n54:def extract(metrics_list, name):\\n60:def orient(series, name):\\n69:def naive_pearson(c, d, cn, dn, max_lag=3):\\n98:def diff_xcorr(c, d, cn, dn, max_lag=3):\\n129:def _onset_gen(series, name):\\n142:def threshold_lead(c, d, cn, dn):\\n177:def _adf_order(series, max_d=2):\\n193:def toda_yamamoto(c, d, cn, dn):\\n275:def classify_effect_size_r(r_abs):\\n286:def classify_effect_size_f2(f2_val):\\n297:def _apply_fdr_and_effect_size(all_pairs):\\n375:def perm_granger(c, d, cn, dn, max_lag=1, n_perm=1000):\\n401:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T09:02:00.698138+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -400 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -400 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T09:02:00.698409+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Method ablation: compare four lead-lag estimation methods.\\n\\nCompares naive vs robust approaches to detect canary->downstream lead-lag,\\nquantifying the spurious regression rate when non-stationary series are\\ncorrelated without proper detrending.\\n\\nInput:  results/mvp/rep_{seed}/all_metrics.json (seeds 42-45)\\nOutput: results/mvp/analysis/method_ablation.json\\n        (with BH FDR correction and effect sizes)\\n\\nMethods:\\n  1. Naive Pearson lag-correlation (raw levels)\\n  2. Differenced cross-correlation (first-differenced series)\\n  3. Threshold-based lead time (2-sigma onset detection)\\n  4. Toda-Yamamoto augmented-lag Granger causality\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport warnings\\nfrom itertools import product\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.stats.multitest import multipletests\\nfrom statsmodels.tsa.stattools import adfuller\\nfrom permutation_granger import permutation_granger_test\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nCANARY = [\\\"token_entropy\\\", \\\"self_bleu\\\", \\\"ece\\\", \\\"effective_rank\\\"]\\nDOWNSTREAM = [\\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"]\\n\\n# Sign conventions: \\\"higher is worse\\\" kept as-is; \\\"lower is worse\\\" negated\\n# so that degradation = positive direction in all analyses.\\nHIGHER_IS_WORSE = {\\\"self_bleu\\\", \\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"effective_rank\\\",\\n                   \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\nALPHA = 0.05\\n\\n\\ndef load_metrics(data_dir, seeds):\\n    \\\"\\\"\\\"Load all_metrics.json for each seed.\\\"\\\"\\\"\\n    data = {}\\n    for s in seeds:\\n        path = os.path.join(data_dir, f\\\"rep_{s}\\\", \\\"all_metrics.json\\\")\\n        with open(path) as f:\\n            data[s] = json.load(f)\\n    return 
…[truncated 7393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T09:02:00.698590+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -5 /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -5 /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T09:02:00.698736+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"token_entropy\\\": 3.2341948700181407,\\n    \\\"self_bleu\\\": 0.010194395218435404,\\n    \\\"distinct_1\\\": 0.0982156685333268,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T09:02:00.698862+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/all_metrics.json')); print(list(d[0].keys()))\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/all_metrics.json')); print(list(d[0].keys()))\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T09:02:00.698983+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T09:02:00.699106+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -30 /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -30 /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T09:02:00.699298+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"token_entropy\\\": 3.2341948700181407,\\n    \\\"self_bleu\\\": 0.010194395218435404,\\n    \\\"distinct_1\\\": 0.0982156685333268,\\n    \\\"distinct_2\\\": 0.5178027030111348,\\n    \\\"distinct_3\\\": 0.8127277321747353,\\n    \\\"ece\\\": 0.010804557477709054,\\n    \\\"effective_rank\\\": 46.612774691899155,\\n    \\\"perplexity\\\": 26.948958972544652,\\n    \\\"mauve\\\": 0.03406737671684175,\\n    \\\"generation\\\": 0\\n  },\\n  {\\n    \\\"token_entropy\\\": 2.990560020858481,\\n    \\\"self_bleu\\\": 0.01031278388147428,\\n    \\\"distinct_1\\\": 0.09752517633628247,\\n    \\\"distinct_2\\\": 0.5140825545933428,\\n    \\\"distinct_3\\\": 0.8103854590526204,\\n    \\\"ece\\\": 0.011467273049856756,\\n    \\\"effective_rank\\\": 48.678408698897236,\\n    \\\"perplexity\\\": 19.2989086452224,\\n    \\\"mauve\\\": 0.03232946507236373,\\n    \\\"generation\\\": 1\\n  },\\n  {\\n    \\\"token_entropy\\\": 3.0210253027501817,\\n    \\\"self_bleu\\\": 0.012505416640113377,\\n    \\\"distinct_1\\\": 0.08881482826974563,\\n    \\\"distinct_2\\\": 0.4793637756472019,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T09:02:00.699551+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -200 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -200 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T09:02:00.699778+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Cross-alpha analysis for distributional canary collapse experiments.\\n\\nScans results/alpha_sweep/a*_s42/ directories, computes:\\n  1. Dose-response table (gen0->genN drift% per metric per alpha)\\n  2. Bidirectional permutation Granger causality with BH FDR correction\\n  3. Cross-correlation lead-lag analysis (delta-metric pairs)\\n  4. Per-generation velocity analysis for distinct_1\\n\\nInput:  results/alpha_sweep/a{NNN}_s42/all_metrics.json\\nOutput: results/analysis/cross_alpha_v{VERSION}.json + terminal summary\\n\\nDependencies: numpy, statsmodels\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport glob\\nimport json\\nimport os\\nimport re\\nimport sys\\nfrom datetime import datetime\\n\\nimport numpy as np\\nfrom statsmodels.stats.multitest import multipletests\\n\\n\\n# ---------------------------------------------------------------------------\\n# Data loading\\n# ---------------------------------------------------------------------------\\n\\nBASE_DIR = os.path.dirname(os.path.abspath(__file__))\\nSWEEP_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"alpha_sweep\\\")\\nANALYSIS_DIR = os.path.join(BASE_DIR, \\\"results\\\", \\\"analysis\\\")\\n\\nMETRICS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"token_entropy\\\", \\\"ece\\\", \\\"perplexity\\\"]\\n\\n# Granger test pairs: (cause, effect, label)\\nGRANGER_PAIRS = [\\n    (\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"entropy->d1\\\"),\\n    (\\\"ece\\\",           \\\"distinct_1\\\", \\\"ECE->d1\\\"),\\n    (\\\"token_entropy\\\", \\\"distinct_2\\\", \\\"entropy->d2\\\"),\\n    (\\\"ece\\\",           \\\"distinct_2\\\", \\\"ECE->d2\\\"),\\n    (\\\"distinct_1\\\", \\\"token_entropy\\\", \\\"d1->entropy\\\"),\\n    (\\\"distinct_1\\\", \\\"ece\\\",           \\\"d1->ECE\\\"),\\n    (\\\"distinct_2\\\", \\\"token_entropy\\\", \\\"d2->entropy\\\"),\\n    (\\\"distinct_2\\\", \\\"ece\\\",           \\\"d2->ECE\\\"),\
…[truncated 6407 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T09:02:00.699984+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -n +200 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "tail -n +200 /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T09:02:00.700272+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"                \\\"direction\\\": label,\\n                \\\"cause\\\": cause_key,\\n                \\\"effect\\\": effect_key,\\n            })\\n            results.append(res)\\n    return results\\n\\n\\ndef apply_fdr(granger_results):\\n    \\\"\\\"\\\"Apply BH FDR correction across all tests with valid p-values.\\\"\\\"\\\"\\n    valid_idx = [i for i, r in enumerate(granger_results) if r.get(\\\"p_raw\\\") is not None]\\n    if not valid_idx:\\n        return granger_results\\n\\n    raw_ps = [granger_results[i][\\\"p_raw\\\"] for i in valid_idx]\\n    _, fdr_ps, _, _ = multipletests(raw_ps, method=\\\"fdr_bh\\\")\\n\\n    for j, idx in enumerate(valid_idx):\\n        granger_results[idx][\\\"p_fdr\\\"] = round(float(fdr_ps[j]), 6)\\n\\n    # Annotate alpha=0.00 false-positive warning\\n    for r in granger_results:\\n        if r.get(\\\"alpha\\\", -1) == 0.0 and r.get(\\\"p_raw\\\") is not None and r[\\\"p_raw\\\"] < 0.05:\\n            r[\\\"note\\\"] = \\\"consistent with FPR, likely false positive\\\"\\n\\n    return granger_results\\n\\n\\n# ---------------------------------------------------------------------------\\n# 3. Cross-correlation lead-lag\\n# ---------------------------------------------------------------------------\\n\\ndef cross_correlation(all_data, max_lag=3):\\n    \\\"\\\"\\\"Compute delta-metric cross-correlations at various lags.\\\"\\\"\\\"\\n    result = {}\\n    for alpha_key, alpha_val, metrics_list in all_data:\\n        entry = {\\\"alpha\\\": alpha_val}\\n        for cause_key, effect_key, pair_label in XCORR_PAIRS:\\n            dx = np.diff(extract_series(metrics_list, cause_key))\\n            dy = np.diff(extract_series(metrics_list, effect_key))\\n            lags = {}\\n            best_lag, best_r = 0, 0.0\\n            for lag in range(-max_lag, max_lag + 1):\\n                if lag >= 0:\\n                    a, b = dx[:len(dx) - lag] if lag > 0 else dx, dy[l
…[truncated 7145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T09:02:00.700694+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py",
  "content": "\"\"\"Cross-alpha analysis v4 with per-alpha consensus classification.\n\nExtends v3 with:\n  5. Per-alpha multi-method consensus classification (regime-dependent validity)\n  6. Markdown report output\n\nHandles mixed data paths:\n  - alpha-sweep: results/alpha_sweep/a{NNN}_s42/all_metrics.json (single seed)\n  - alpha=1.0:   results/mvp/rep_{42..45}/all_metrics.json (4 seeds)\n  - alpha=1.0 consensus loads existing method_ablation.json\n  - Single-seed alpha points: seed_threshold=1, method agreement only\n\nDependencies: numpy, scipy, statsmodels\n\"\"\"\n\nimport argparse\nimport glob\nimport json\nimport os\nimport re\nimport sys\nimport warnings\nfrom datetime import datetime\n\nimport numpy as np\nfrom statsmodels.stats.multitest import multipletests\n\nwarnings.filterwarnings(\"ignore\")\n\nBASE_DIR = os.path.dirname(os.path.abspath(__file__))\nsys.path.insert(0, BASE_DIR)\n\nfrom method_ablation import (\n    CANARY, DOWNSTREAM,\n    extract as ma_extract,\n    naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto, perm_granger,\n)\nfrom consensus_framework import classify_robust, load_sig_matrix, NumpyEncoder\n\nSWEEP_DIR = os.path.join(BASE_DIR, \"results\", \"alpha_sweep\")\nMVP_DIR = os.path.join(BASE_DIR, \"results\", \"mvp\")\nANALYSIS_DIR = os.path.join(BASE_DIR, \"results\", \"analysis\")\n\nMETRICS = [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"token_entropy\", \"ece\", \"perplexity\"]\n\nGRANGER_PAIRS = [\n    (\"token_entropy\", \"distinct_1\", \"entropy->d1\"),\n    (\"ece\",           \"distinct_1\", \"ECE->d1\"),\n    (\"token_entropy\", \"distinct_2\", \"entropy->d2\"),\n    (\"ece\",           \"distinct_2\", \"ECE->d2\"),\n    (\"distinct_1\", \"token_entropy\", \"d1->entropy\"),\n    (\"distinct_1\", \"ece\",           \"d1->ECE\"),\n    (\"distinct_2\", \"token_entropy\", \"d2->entropy\"),\n    (\"distinct_2\", \"ece\",           \"d2->ECE\"),\n]\n\nXCORR_PAIRS = [\n    (\"token_entropy\", \"distinct_1\", \"entropy_vs_d1\"),\n    (\"ece\",           \"distinct_1\", \"ece_vs_d1\"),\n]\n\nMA_METHODS = [\"naive_pearson\", \"differenced_xcorr\", \"threshold_onset\",\n              \"toda_yamamoto\", \"permutation_granger\"]\nMA_METHOD_FN = {\n    \"naive_pearson\": naive_pearson,\n    \"differenced_xcorr\": diff_xcorr,\n    \"threshold_onset\": threshold_lead,\n    \"toda_yamamoto\": toda_yamamoto,\n    \"permutation_granger\": perm_granger,\n}\n\n\n# ---------------------------------------------------------------------------\n# Data loading (extended for MVP alpha=1.0)\n# ---------------------------------------------------------------------------\n\ndef _find_mvp_seeds():\n    seeds = []\n    if not os.path.isdir(MVP_DIR):\n        return seeds\n    for d in sorted(os.listdir(MVP_DIR)):\n        m = re.match(r\"rep_(\\d+)$\", d)\n        if m and os.path.isfile(os.path.join(MVP_DIR, d, \"all_metrics.json\")):\n            seeds.append(int(m.group(1)))\n    return sorted(seeds)\n\n\ndef discover_alpha_dirs(explicit=None, include_mvp=True):\n    \"\"\"Find alpha directories.\n\n    Returns sorted list of (alpha_key, alpha_float, path, seeds).\n    \"\"\"\n    dirs = []\n\n    if explicit:\n        for name in explicit:\n            if name in (\"mvp\", \"a100_mvp\"):\n                rep42 = os.path.join(MVP_DIR, \"rep_42\")\n                if os.path.isdir(rep42):\n                    dirs.append((\"a100\", 1.0, rep42, _find_mvp_seeds()))\n                continue\n            path = os.path.join(SWEEP_DIR, name)\n            if not os.path.isdir(path):\n                print(f\"WARNING: {path} not found, skipping\", file=sys.stderr)\n                continue\n            m = re.match(r\"a(\\d{3})_s(\\d+)\", name)\n            if m:\n                alpha_val = int(m.group(1)) / 100.0\n                dirs.append((f\"a{m.group(1)}\", alpha_val, path, [int(m.group(2))]))\n    else:\n        pattern = os.path.join(SWEEP_DIR, \"a*_s42\")\n        for path in sorted(glob.glob(pattern)):\n            name = os.path.basename(path)\n            m = re.match(r\"a(\\d{3})_s42\", name)\n            if m:\n                alpha_val = int(m.group(1)) / 100.0\n                dirs.append((f\"a{m.group(1)}\", alpha_val, path, [42]))\n\n        if include_mvp and not any(d[1] == 1.0 for d in dirs):\n            rep42 = os.path.join(MVP_DIR, \"rep_42\")\n            if os.path.isdir(rep42):\n                dirs.append((\"a100\", 1.0, rep42, _find_mvp_seeds()))\n\n    return sorted(dirs, key=lambda x: x[1])\n\n\ndef load_metrics(alpha_dir):\n    path = os.path.join(alpha_dir, \"all_metrics.json\")\n    with open(path) as f:\n        data = json.load(f)\n    return sorted(data, key=lambda x: x[\"generation\"])\n\n\ndef load_all_seeds_metrics(alpha_val, primary_dir, seeds):\n    \"\"\"Load metrics for all seeds. Returns list of (seed, metrics_list).\"\"\"\n    results = []\n    for seed in seeds:\n        if alpha_val == 1.0:\n            path = os.path.join(MVP_DIR, f\"rep_{seed}\")\n        else:\n            path = primary_dir\n        mpath = os.path.join(path, \"all_metrics.json\")\n        if os.path.isfile(mpath):\n            results.append((seed, load_metrics(path)))\n    return results\n\n\ndef extract_series(metrics_list, key):\n    return np.array([m[key] for m in metrics_list], dtype=float)\n\n\n# ---------------------------------------------------------------------------\n# 1. Dose-response\n# ---------------------------------------------------------------------------\n\ndef compute_dose_response(all_data):\n    result = {}\n    for alpha_key, alpha_val, metrics_list in all_data:\n        entry = {\"alpha\": alpha_val}\n        for metric in METRICS:\n            vals = extract_series(metrics_list, metric)\n            gen0, genN = vals[0], vals[-1]\n            drift_pct = round((genN - gen0) / abs(gen0) * 100, 2) if abs(gen0) > 1e-12 else 0.0\n            entry[metric] = {\n                \"gen0\": round(float(gen0), 6),\n                f\"gen{len(vals)-1}\": round(float(genN), 6),\n                \"drift_pct\": drift_pct,\n            }\n        result[alpha_key] = entry\n    return result\n\n\n# ---------------------------------------------------------------------------\n# 2. Permutation Granger causality\n# ---------------------------------------------------------------------------\n\ndef _build_lag_matrix(y, x, max_lag):\n    T = len(y)\n    n = T - max_lag\n    Y = y[max_lag:]\n    cols_r = [np.ones(n)]\n    for lag in range(1, max_lag + 1):\n        cols_r.append(y[max_lag - lag: T - lag])\n    cols_u = list(cols_r)\n    for lag in range(1, max_lag + 1):\n        cols_u.append(x[max_lag - lag: T - lag])\n    return Y, np.column_stack(cols_r), np.column_stack(cols_u)\n\n\ndef _granger_f_stat(y, x, max_lag):\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\n    n = len(Y)\n    q = max_lag\n    try:\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\n    except np.linalg.LinAlgError:\n        return np.nan\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\n    k_u = X_u.shape[1]\n    df_resid = n - k_u\n    if df_resid <= 0 or rss_u < 1e-15:\n        return np.nan\n    return ((rss_r - rss_u) / q) / (rss_u / df_resid)\n\n\ndef permutation_granger_test(x, y, max_lag=1, n_perm=5000, seed=42, difference=True):\n    x = np.asarray(x, dtype=float)\n    y = np.asarray(y, dtype=float)\n    if difference:\n        x, y = np.diff(x), np.diff(y)\n    T = len(x)\n    if T <= max_lag + 2:\n        return {\"f_stat\": None, \"p_raw\": None, \"note\": f\"Series too short: T={T}\"}\n\n    f_obs = _granger_f_stat(y, x, max_lag)\n    if np.isnan(f_obs):\n        return {\"f_stat\": None, \"p_raw\": None, \"note\": \"F-stat computation failed\"}\n\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\n    rss_r = np.sum((Y - X_r @ np.linalg.lstsq(X_r, Y, rcond=None)[0]) ** 2)\n    rss_u = np.sum((Y - X_u @ np.linalg.lstsq(X_u, Y, rcond=None)[0]) ** 2)\n    f2 = (rss_r - rss_u) / rss_u if rss_u > 1e-15 else None\n\n    rng = np.random.default_rng(seed)\n    null_f = np.empty(n_perm)\n    for i in range(n_perm):\n        null_f[i] = _granger_f_stat(y, rng.permutation(x), max_lag)\n    valid = null_f[~np.isnan(null_f)]\n    if len(valid) == 0:\n        return {\"f_stat\": round(float(f_obs), 4), \"p_raw\": None, \"note\": \"All permutations failed\"}\n\n    p_value = (np.sum(valid >= f_obs) + 1) / (len(valid) + 1)\n    return {\n        \"f_stat\": round(float(f_obs), 4),\n        \"p_raw\": round(float(p_value), 6),\n        \"n_perm\": n_perm,\n        \"effect_size_f2\": round(float(f2), 4) if f2 is not None else None,\n    }\n\n\ndef run_granger_all(all_data, max_lag=1, n_perms=5000):\n    results = []\n    for alpha_key, alpha_val, metrics_list in all_data:\n        for cause_key, effect_key, label in GRANGER_PAIRS:\n            x = extract_series(metrics_list, cause_key)\n            y = extract_series(metrics_list, effect_key)\n            res = permutation_granger_test(x, y, max_lag=max_lag, n_perm=n_perms)\n            res.update({\n                \"alpha\": alpha_val,\n                \"alpha_key\": alpha_key,\n                \"direction\": label,\n                \"cause\": cause_key,\n                \"effect\": effect_key,\n            })\n            results.append(res)\n    return results\n\n\ndef apply_fdr(granger_results):\n    valid_idx = [i for i, r in enumerate(granger_results) if r.get(\"p_raw\") is not None]\n    if not valid_idx:\n        return granger_results\n\n    raw_ps = [granger_results[i][\"p_raw\"] for i in valid_idx]\n    _, fdr_ps, _, _ = multipletests(raw_ps, method=\"fdr_bh\")\n\n    for j, idx in enumerate(valid_idx):\n        granger_results[idx][\"p_fdr\"] = round(float(fdr_ps[j]), 6)\n\n    for r in granger_results:\n        if r.get(\"alpha\", -1) == 0.0 and r.get(\"p_raw\") is not None and r[\"p_raw\"] < 0.05:\n            r[\"note\"] = \"consistent with FPR, likely false positive\"\n\n    return granger_results\n\n\n# ---------------------------------------------------------------------------\n# 3. Cross-correlation lead-lag\n# ---------------------------------------------------------------------------\n\ndef cross_correlation(all_data, max_lag=3):\n    result = {}\n    for alpha_key, alpha_val, metrics_list in all_data:\n        entry = {\"alpha\": alpha_val}\n        for cause_key, effect_key, pair_label in XCORR_PAIRS:\n            dx = np.diff(extract_series(metrics_list, cause_key))\n            dy = np.diff(extract_series(metrics_list, effect_key))\n            lags = {}\n            best_lag, best_r = 0, 0.0\n            for lag in range(-max_lag, max_lag + 1):\n                if lag >= 0:\n                    a, b = dx[:len(dx) - lag] if lag > 0 else dx, dy[lag:] if lag > 0 else dy\n                else:\n                    a, b = dx[-lag:], dy[:len(dy) + lag]\n                n = min(len(a), len(b))\n                if n < 3:\n                    continue\n                a, b = a[:n], b[:n]\n                std_a, std_b = np.std(a, ddof=1), np.std(b, ddof=1)\n                if std_a < 1e-15 or std_b < 1e-15:\n                    r = 0.0\n                else:\n                    r = float(np.corrcoef(a, b)[0, 1])\n                lags[str(lag)] = round(r, 4)\n                if abs(r) > abs(best_r):\n                    best_lag, best_r = lag, r\n            entry[pair_label] = {\n                \"peak_lag\": best_lag,\n                \"peak_r\": round(best_r, 4),\n                \"lags\": lags,\n            }\n        result[alpha_key] = entry\n    return result\n\n\n# ---------------------------------------------------------------------------\n# 4. Per-gen velocity\n# ---------------------------------------------------------------------------\n\ndef per_gen_velocity(all_data):\n    result = {}\n    for alpha_key, alpha_val, metrics_list in all_data:\n        vals = extract_series(metrics_list, \"distinct_1\")\n        deltas = np.diff(vals)\n        n = len(deltas)\n        mid = n // 2\n        early_mean = float(np.mean(deltas[:mid])) if mid > 0 else None\n        late_mean = float(np.mean(deltas[mid:])) if mid < n else None\n        max_drop_idx = int(np.argmin(deltas))\n        result[alpha_key] = {\n            \"alpha\": alpha_val,\n            \"d1_values\": [round(float(v), 6) for v in vals],\n            \"d1_deltas\": [round(float(d), 6) for d in deltas],\n            \"cumulative_drift_pct\": round((vals[-1] - vals[0]) / abs(vals[0]) * 100, 2),\n            \"mean_velocity\": round(float(np.mean(deltas)), 6),\n            \"max_drop_gen\": max_drop_idx,\n            \"max_drop_value\": round(float(deltas[max_drop_idx]), 6),\n            \"early_mean_velocity\": round(early_mean, 6) if early_mean is not None else None,\n            \"late_mean_velocity\": round(late_mean, 6) if late_mean is not None else None,\n            \"deceleration_ratio\": round(late_mean / early_mean, 4) if early_mean and abs(early_mean) > 1e-12 else None,\n        }\n    return result\n\n\n# ---------------------------------------------------------------------------\n# 5. Per-alpha consensus classification\n# ---------------------------------------------------------------------------\n\ndef run_consensus_per_alpha(alpha_dirs, mvp_ablation_path=None, consensus_n_perm=1000):\n    \"\"\"Run 5-method consensus classification at each alpha point.\n\n    alpha=1.0 with existing method_ablation.json: load directly (4 seeds).\n    Other alpha points: run 5 methods on single-seed data, seed_threshold=1.\n    \"\"\"\n    results = {}\n\n    for alpha_key, alpha_val, primary_dir, seeds in alpha_dirs:\n        # alpha=1.0: use existing method_ablation.json\n        if alpha_val == 1.0 and mvp_ablation_path and os.path.isfile(mvp_ablation_path):\n            sig, pair_names, method_names, ab_seeds = load_sig_matrix(mvp_ablation_path)\n            n_m, n_p, n_s = sig.shape\n            mt = n_m - 1  # 4/5\n            st = 3        # 3/4 seeds\n            consensus = classify_robust(sig, mt, st)\n\n            for cl in consensus[\"classifications\"]:\n                pi = cl[\"pair_index\"]\n                cl[\"canary\"] = pair_names[pi][0]\n                cl[\"downstream\"] = pair_names[pi][1]\n                cl[\"pair_label\"] = f\"{pair_names[pi][0]}→{pair_names[pi][1]}\"\n\n            results[alpha_key] = {\n                \"alpha\": alpha_val,\n                \"n_seeds\": n_s,\n                \"seeds\": ab_seeds,\n                \"mode\": \"full_consensus\",\n                \"note\": f\"{n_s}-seed full consensus (≥{mt}/{n_m} methods, ≥{st}/{n_s} seeds)\",\n                \"method_threshold\": mt,\n                \"seed_threshold\": st,\n                \"n_methods\": n_m,\n                \"n_pairs\": n_p,\n                \"consensus\": consensus,\n                \"pair_names\": [list(p) for p in pair_names],\n            }\n            continue\n\n        # Other alpha points: run 5 methods from scratch\n        seed_data = load_all_seeds_metrics(alpha_val, primary_dir, seeds)\n        n_seeds = len(seed_data)\n        n_pairs = len(CANARY) * len(DOWNSTREAM)\n        n_methods = len(MA_METHODS)\n\n        sig_matrix = np.zeros((n_methods, n_pairs, n_seeds), dtype=bool)\n        pair_names = []\n\n        for si, (seed, metrics_list) in enumerate(seed_data):\n            pi = 0\n            for cn in CANARY:\n                c = ma_extract(metrics_list, cn)\n                for dn in DOWNSTREAM:\n                    if si == 0:\n                        pair_names.append((cn, dn))\n                    d = ma_extract(metrics_list, dn)\n                    for mi, method_name in enumerate(MA_METHODS):\n                        fn = MA_METHOD_FN[method_name]\n                        try:\n                            if method_name == \"permutation_granger\":\n                                res = fn(c, d, cn, dn, n_perm=consensus_n_perm)\n                            else:\n                                res = fn(c, d, cn, dn)\n                            sig_matrix[mi, pi, si] = res.get(\"significant\", False)\n                        except Exception:\n                            sig_matrix[mi, pi, si] = False\n                    pi += 1\n\n        st = 1 if n_seeds == 1 else 3\n        mt = n_methods - 1  # 4/5\n\n        consensus = classify_robust(sig_matrix, mt, st)\n        for cl in consensus[\"classifications\"]:\n            pi = cl[\"pair_index\"]\n            cl[\"canary\"] = pair_names[pi][0]\n            cl[\"downstream\"] = pair_names[pi][1]\n            cl[\"pair_label\"] = f\"{pair_names[pi][0]}→{pair_names[pi][1]}\"\n\n        mode = \"method_agreement_only\" if n_seeds == 1 else \"full_consensus\"\n        note_prefix = \"single-seed, method agreement only\" if n_seeds == 1 else f\"{n_seeds}-seed full consensus\"\n\n        results[alpha_key] = {\n            \"alpha\": alpha_val,\n            \"n_seeds\": n_seeds,\n            \"seeds\": [s for s, _ in seed_data],\n            \"mode\": mode,\n            \"note\": f\"{note_prefix} (≥{mt}/{n_methods} methods, ≥{st}/{n_seeds} seeds)\",\n            \"method_threshold\": mt,\n            \"seed_threshold\": st,\n            \"n_methods\": n_methods,\n            \"n_pairs\": n_pairs,\n            \"consensus\": consensus,\n            \"pair_names\": [list(p) for p in pair_names],\n        }\n\n    return results\n\n\ndef consensus_regime_comparison(consensus_results):\n    \"\"\"Compare robust/non-robust classifications across alpha points.\"\"\"\n    alpha_keys = sorted(consensus_results.keys(),\n                        key=lambda k: consensus_results[k][\"alpha\"])\n    if not alpha_keys:\n        return {}\n\n    first = consensus_results[alpha_keys[0]]\n    pair_labels = [cl[\"pair_label\"] for cl in first[\"consensus\"][\"classifications\"]]\n\n    pairs_comp = {}\n    for label in pair_labels:\n        row = {\"pair\": label, \"per_alpha\": {}}\n        for ak in alpha_keys:\n            cr = consensus_results[ak]\n            cls = [c for c in cr[\"consensus\"][\"classifications\"] if c[\"pair_label\"] == label]\n            if cls:\n                cl = cls[0]\n                row[\"per_alpha\"][ak] = {\n                    \"alpha\": cr[\"alpha\"],\n                    \"is_robust\": cl[\"is_robust\"],\n                    \"n_sig_methods\": cl[\"n_sig_methods\"],\n                    \"mode\": cr[\"mode\"],\n                }\n        verdicts = [v[\"is_robust\"] for v in row[\"per_alpha\"].values()]\n        row[\"stable\"] = len(set(verdicts)) <= 1\n        row[\"all_robust\"] = all(verdicts) if verdicts else False\n        row[\"all_non_robust\"] = not any(verdicts) if verdicts else True\n        pairs_comp[label] = row\n\n    n_stable = sum(1 for r in pairs_comp.values() if r[\"stable\"])\n    return {\n        \"alpha_keys\": alpha_keys,\n        \"alpha_values\": [consensus_results[ak][\"alpha\"] for ak in alpha_keys],\n        \"n_pairs\": len(pair_labels),\n        \"n_stable\": n_stable,\n        \"n_regime_dependent\": len(pair_labels) - n_stable,\n        \"pairs\": pairs_comp,\n    }\n\n\n# ---------------------------------------------------------------------------\n# 6. Markdown report\n# ---------------------------------------------------------------------------\n\ndef generate_markdown_report(output, out_path):\n    lines = []\n    lines.append(f\"# Cross-Alpha Analysis Report ({output['version']})\")\n    lines.append(\"\")\n    lines.append(f\"**Date:** {output['date']}\")\n    lines.append(f\"**Alpha points:** {output['alpha_points']}\")\n    lines.append(f\"**Generations:** {output['gen_range']}\")\n    lines.append(\"\")\n\n    # 1. Dose-response\n    lines.append(\"## 1. Dose-Response (gen0 to genN drift %)\")\n    lines.append(\"\")\n    dr = output[\"dose_response\"]\n    alphas = sorted(dr.keys())\n    header = \"| Metric |\"\n    sep = \"|--------|\"\n    for ak in alphas:\n        header += f\" α={dr[ak]['alpha']:.2f} |\"\n        sep += \"--------:|\"\n    lines.append(header)\n    lines.append(sep)\n    for metric in METRICS:\n        row = f\"| {metric} |\"\n        for ak in alphas:\n            d = dr[ak][metric][\"drift_pct\"]\n            row += f\" {d:+.1f}% |\"\n        lines.append(row)\n    lines.append(\"\")\n\n    # 2. Granger\n    lines.append(\"## 2. Granger Causality (bidirectional, permutation, FDR-corrected)\")\n    lines.append(\"\")\n    gc = output[\"granger_causality\"]\n    ak_list = sorted(set(r[\"alpha_key\"] for r in gc))\n    header = \"| Direction |\"\n    sep = \"|-----------|\"\n    for ak in ak_list:\n        a = [r for r in gc if r[\"alpha_key\"] == ak][0][\"alpha\"]\n        header += f\" α={a:.2f} p_raw | p_fdr |\"\n        sep += \"--------:|--------:|\"\n    lines.append(header)\n    lines.append(sep)\n    directions = list(dict.fromkeys(r[\"direction\"] for r in gc))\n    for d in directions:\n        row = f\"| {d} |\"\n        for ak in ak_list:\n            match = [r for r in gc if r[\"alpha_key\"] == ak and r[\"direction\"] == d]\n            if match:\n                r = match[0]\n                pr = f\"{r['p_raw']:.4f}\" if r.get(\"p_raw\") is not None else \"N/A\"\n                pf = f\"{r['p_fdr']:.4f}\" if r.get(\"p_fdr\") is not None else \"N/A\"\n                sig = \" *\" if r.get(\"p_fdr\") is not None and r[\"p_fdr\"] < 0.05 else \"\"\n                row += f\" {pr} | {pf}{sig} |\"\n            else:\n                row += \" -- | -- |\"\n        lines.append(row)\n    lines.append(\"\")\n    sc = output[\"statistical_config\"]\n    lines.append(f\"FDR: {sc['n_independent_tests']} tests, BH correction. \\\\* = p_fdr < 0.05\")\n    lines.append(\"\")\n\n    # 3. Consensus per alpha\n    if \"consensus_per_alpha\" in output:\n        lines.append(\"## 3. Consensus Classification (regime-dependent validity)\")\n        lines.append(\"\")\n        cpa = output[\"consensus_per_alpha\"]\n        for ak in sorted(cpa.keys(), key=lambda k: cpa[k][\"alpha\"]):\n            entry = cpa[ak]\n            lines.append(f\"### α={entry['alpha']:.2f} ({entry['note']})\")\n            lines.append(\"\")\n            lines.append(f\"- Robust pairs: {entry['consensus']['n_robust']}/{entry['n_pairs']}\")\n            lines.append(f\"- Non-robust: {entry['consensus']['n_non_robust']}/{entry['n_pairs']}\")\n            lines.append(\"\")\n            lines.append(\"| Pair | Robust | Methods |\")\n            lines.append(\"|------|--------|---------|\")\n            for cl in entry[\"consensus\"][\"classifications\"]:\n                tag = \"**ROBUST**\" if cl[\"is_robust\"] else \"non-robust\"\n                lines.append(f\"| {cl['pair_label']} | {tag} | {cl['n_sig_methods']}/{entry['n_methods']} |\")\n            lines.append(\"\")\n\n        if \"consensus_regime_comparison\" in output:\n            rc = output[\"consensus_regime_comparison\"]\n            lines.append(\"### Regime Comparison Summary\")\n            lines.append(\"\")\n            lines.append(f\"- Stable pairs (same classification at all α): {rc['n_stable']}/{rc['n_pairs']}\")\n            lines.append(f\"- Regime-dependent pairs: {rc['n_regime_dependent']}/{rc['n_pairs']}\")\n            lines.append(\"\")\n            header = \"| Pair |\"\n            sep = \"|------|\"\n            for av in rc[\"alpha_values\"]:\n                header += f\" α={av:.2f} |\"\n                sep += \"--------|\"\n            header += \" Stable |\"\n            sep += \"--------|\"\n            lines.append(header)\n            lines.append(sep)\n            for label, info in rc[\"pairs\"].items():\n                row = f\"| {label} |\"\n                for ak in rc[\"alpha_keys\"]:\n                    if ak in info[\"per_alpha\"]:\n                        v = info[\"per_alpha\"][ak]\n                        tag = f\"R({v['n_sig_methods']})\" if v[\"is_robust\"] else f\".({v['n_sig_methods']})\"\n                        row += f\" {tag} |\"\n                    else:\n                        row += \" - |\"\n                row += f\" {'Y' if info['stable'] else 'N'} |\"\n                lines.append(row)\n            lines.append(\"\")\n\n    # 4. Velocity\n    lines.append(\"## 4. D1 Velocity\")\n    lines.append(\"\")\n    vel = output[\"per_gen_velocity\"]\n    lines.append(\"| α | mean_vel | early | late | decel_ratio |\")\n    lines.append(\"|---|----------|-------|------|-------------|\")\n    for ak in sorted(vel.keys()):\n        v = vel[ak]\n        decel = f\"{v['deceleration_ratio']:.2f}\" if v.get(\"deceleration_ratio\") else \"N/A\"\n        lines.append(f\"| {v['alpha']:.2f} | {v['mean_velocity']:+.6f} | \"\n                     f\"{v['early_mean_velocity']:+.6f} | {v['late_mean_velocity']:+.6f} | {decel} |\")\n    lines.append(\"\")\n\n    with open(out_path, \"w\") as f:\n        f.write(\"\\n\".join(lines))\n    return out_path\n\n\n# ---------------------------------------------------------------------------\n# Output / summary\n# ---------------------------------------------------------------------------\n\ndef auto_version():\n    os.makedirs(ANALYSIS_DIR, exist_ok=True)\n    existing = glob.glob(os.path.join(ANALYSIS_DIR, \"cross_alpha_v*.json\"))\n    max_v = 0\n    for f in existing:\n        m = re.search(r\"cross_alpha_v(\\d+)\", f)\n        if m:\n            max_v = max(max_v, int(m.group(1)))\n    return max_v + 1\n\n\ndef print_summary(output):\n    print(\"\\n\" + \"=\" * 80)\n    print(\"CROSS-ALPHA ANALYSIS SUMMARY (v4)\")\n    print(\"=\" * 80)\n\n    # Dose-response table\n    dr = output[\"dose_response\"]\n    alphas = sorted(dr.keys())\n    print(f\"\\nDOSE-RESPONSE (drift %)\")\n    print(\"-\" * 80)\n    header = f\"{'Metric':<16}\"\n    for ak in alphas:\n        header += f\" | a={dr[ak]['alpha']:<5}\"\n    print(header)\n    print(\"-\" * 80)\n    for metric in METRICS:\n        line = f\"{metric:<16}\"\n        for ak in alphas:\n            d = dr[ak][metric][\"drift_pct\"]\n            line += f\" | {d:>+7.1f}%\"\n        print(line)\n\n    # Granger table\n    gc = output[\"granger_causality\"]\n    print(f\"\\nGRANGER CAUSALITY (bidirectional, differenced, permutation)\")\n    print(\"-\" * 80)\n    header = f\"{'Direction':<20}\"\n    alpha_keys = sorted(set(r[\"alpha_key\"] for r in gc))\n    for ak in alpha_keys:\n        header += f\" | a={[r for r in gc if r['alpha_key']==ak][0]['alpha']:<4} p_raw   p_fdr\"\n    print(header)\n    print(\"-\" * 80)\n\n    directions = list(dict.fromkeys(r[\"direction\"] for r in gc))\n    for d in directions:\n        line = f\"{d:<20}\"\n        for ak in alpha_keys:\n            match = [r for r in gc if r[\"alpha_key\"] == ak and r[\"direction\"] == d]\n            if match:\n                r = match[0]\n                p_raw = f\"{r['p_raw']:.4f}\" if r.get(\"p_raw\") is not None else \"  N/A \"\n                p_fdr = f\"{r.get('p_fdr', 'N/A')}\" if r.get(\"p_fdr\") is not None else \"  N/A \"\n                if isinstance(p_fdr, float):\n                    p_fdr = f\"{p_fdr:.4f}\"\n                sig = \"*\" if r.get(\"p_fdr\") is not None and r[\"p_fdr\"] < 0.05 else \" \"\n                fp = \"FP?\" if r.get(\"note\", \"\").startswith(\"consistent\") else \"   \"\n                line += f\" | {p_raw} {p_fdr:>7} {sig}{fp}\"\n            else:\n                line += f\" |    --       --     \"\n        print(line)\n\n    valid = [r for r in gc if r.get(\"p_raw\") is not None]\n    n_total = len(valid)\n    n_raw_sig = sum(1 for r in valid if r[\"p_raw\"] < 0.05)\n    n_fdr_sig = sum(1 for r in valid if r.get(\"p_fdr\") is not None and r[\"p_fdr\"] < 0.05)\n    print(f\"\\nFDR: {n_raw_sig}/{n_total} raw-sig -> {n_fdr_sig}/{n_total} FDR-sig \"\n          f\"(BH correction across all {n_total} tests)\")\n\n    # Consensus per alpha\n    if \"consensus_per_alpha\" in output:\n        cpa = output[\"consensus_per_alpha\"]\n        print(f\"\\nCONSENSUS CLASSIFICATION PER ALPHA\")\n        print(\"-\" * 80)\n        for ak in sorted(cpa.keys(), key=lambda k: cpa[k][\"alpha\"]):\n            entry = cpa[ak]\n            print(f\"\\n  a={entry['alpha']:.2f} [{entry['note']}]\")\n            print(f\"    Robust: {entry['consensus']['n_robust']}/{entry['n_pairs']}, \"\n                  f\"Non-robust: {entry['consensus']['n_non_robust']}/{entry['n_pairs']}\")\n            for cl in entry[\"consensus\"][\"classifications\"]:\n                if cl[\"is_robust\"]:\n                    print(f\"      ROBUST  {cl['pair_label']:<35s} ({cl['n_sig_methods']}/{entry['n_methods']} methods)\")\n\n        if \"consensus_regime_comparison\" in output:\n            rc = output[\"consensus_regime_comparison\"]\n            print(f\"\\n  REGIME COMPARISON: {rc['n_stable']}/{rc['n_pairs']} stable, \"\n                  f\"{rc['n_regime_dependent']}/{rc['n_pairs']} regime-dependent\")\n            changed = [l for l, p in rc[\"pairs\"].items() if not p[\"stable\"]]\n            if changed:\n                print(f\"    Regime-dependent pairs:\")\n                for label in changed:\n                    info = rc[\"pairs\"][label]\n                    tags = []\n                    for ak in rc[\"alpha_keys\"]:\n                        if ak in info[\"per_alpha\"]:\n                            v = info[\"per_alpha\"][ak]\n                            t = \"R\" if v[\"is_robust\"] else \".\"\n                            tags.append(f\"a={v['alpha']:.2f}:{t}\")\n                    print(f\"      {label:<35s} {' '.join(tags)}\")\n\n    # Cross-correlation\n    xcorr = output[\"cross_correlation\"]\n    print(f\"\\nCROSS-CORRELATION (delta-metric, peak lag)\")\n    print(\"-\" * 60)\n    for pair_label in [\"entropy_vs_d1\", \"ece_vs_d1\"]:\n        line = f\"  {pair_label:<18}\"\n        for ak in sorted(xcorr.keys()):\n            p = xcorr[ak].get(pair_label, {})\n            line += f\" | a={xcorr[ak]['alpha']}: lag={p.get('peak_lag','?'):>2} r={p.get('peak_r','?'):>7}\"\n        print(line)\n\n    # Velocity\n    vel = output[\"per_gen_velocity\"]\n    print(f\"\\nD1 VELOCITY\")\n    print(\"-\" * 60)\n    for ak in sorted(vel.keys()):\n        v = vel[ak]\n        decel = f\"{v['deceleration_ratio']:.2f}\" if v.get(\"deceleration_ratio\") is not None else \"N/A\"\n        print(f\"  a={v['alpha']}: mean_vel={v['mean_velocity']:+.6f}  \"\n              f\"early={v['early_mean_velocity']:+.6f}  late={v['late_mean_velocity']:+.6f}  \"\n              f\"decel_ratio={decel}  max_drop=gen{v['max_drop_gen']}\")\n\n    print()\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Cross-alpha analysis v4 with per-alpha consensus classification.\"\n    )\n    parser.add_argument(\"--alpha-dirs\", nargs=\"*\", default=None,\n                        help=\"Specific alpha dirs (e.g. a000_s42 a025_s42 mvp). Default: auto-discover all.\")\n    parser.add_argument(\"--n-perms\", type=int, default=5000,\n                        help=\"Permutations for Granger test (default: 5000)\")\n    parser.add_argument(\"--consensus-n-perms\", type=int, default=1000,\n                        help=\"Permutations for consensus perm_granger method (default: 1000)\")\n    parser.add_argument(\"--max-lag\", type=int, default=1,\n                        help=\"Max lag for Granger test (default: 1)\")\n    parser.add_argument(\"--no-mvp\", action=\"store_true\",\n                        help=\"Exclude MVP (alpha=1.0) from auto-discovery\")\n    parser.add_argument(\"--no-consensus\", action=\"store_true\",\n                        help=\"Skip consensus classification (faster)\")\n    parser.add_argument(\"--version\", type=int, default=None,\n                        help=\"Output version number (default: auto-increment)\")\n    parser.add_argument(\"--update-registry\", action=\"store_true\",\n                        help=\"Print registry update commands after analysis\")\n    args = parser.parse_args()\n\n    alpha_dirs = discover_alpha_dirs(args.alpha_dirs, include_mvp=not args.no_mvp)\n    if not alpha_dirs:\n        print(\"ERROR: No alpha directories found.\", file=sys.stderr)\n        sys.exit(1)\n\n    print(f\"Found {len(alpha_dirs)} alpha points: \"\n          f\"{[(a[0], f'seeds={a[3]}') for a in alpha_dirs]}\")\n\n    # Load primary seed data (seed=42) for v3 analyses\n    all_data = []\n    for alpha_key, alpha_val, path, seeds in alpha_dirs:\n        metrics = load_metrics(path)\n        print(f\"  {alpha_key} (a={alpha_val}): {len(metrics)} generations, seeds={seeds}\")\n        all_data.append((alpha_key, alpha_val, metrics))\n\n    # 1. Dose-response\n    dose_resp = compute_dose_response(all_data)\n\n    # 2. Granger\n    print(f\"\\nRunning bidirectional Granger ({len(GRANGER_PAIRS)} pairs x {len(all_data)} alphas, \"\n          f\"n_perms={args.n_perms})...\")\n    granger = run_granger_all(all_data, max_lag=args.max_lag, n_perms=args.n_perms)\n    granger = apply_fdr(granger)\n\n    # 3. Cross-correlation\n    xcorr = cross_correlation(all_data)\n\n    # 4. Velocity\n    velocity = per_gen_velocity(all_data)\n\n    # Assemble output\n    version = args.version or auto_version()\n    n_gens = len(all_data[0][2]) if all_data else 0\n    output = {\n        \"version\": f\"v{version}\",\n        \"date\": datetime.now().strftime(\"%Y-%m-%d\"),\n        \"n_alphas\": len(all_data),\n        \"alpha_points\": [a[1] for a in all_data],\n        \"n_generations\": n_gens,\n        \"gen_range\": f\"gen_0 to gen_{n_gens - 1}\" if n_gens else \"N/A\",\n        \"statistical_config\": {\n            \"granger_max_lag\": args.max_lag,\n            \"granger_n_perm\": args.n_perms,\n            \"granger_differenced\": True,\n            \"fdr_method\": \"benjamini-hochberg\",\n            \"fdr_scope\": f\"all {len(granger)} tests corrected together\",\n            \"n_independent_tests\": len([r for r in granger if r.get(\"p_raw\") is not None]),\n        },\n        \"dose_response\": dose_resp,\n        \"granger_causality\": granger,\n        \"cross_correlation\": xcorr,\n        \"per_gen_velocity\": velocity,\n    }\n\n    # 5. Consensus per alpha\n    if not args.no_consensus:\n        mvp_ablation = os.path.join(MVP_DIR, \"analysis\", \"method_ablation.json\")\n        print(f\"\\nRunning per-alpha consensus classification \"\n              f\"(5 methods x 16 pairs x {len(alpha_dirs)} alphas)...\")\n        consensus_results = run_consensus_per_alpha(\n            alpha_dirs, mvp_ablation_path=mvp_ablation,\n            consensus_n_perm=args.consensus_n_perms)\n        output[\"consensus_per_alpha\"] = consensus_results\n        output[\"consensus_regime_comparison\"] = consensus_regime_comparison(consensus_results)\n\n    # Save JSON\n    os.makedirs(ANALYSIS_DIR, exist_ok=True)\n    json_path = os.path.join(ANALYSIS_DIR, f\"cross_alpha_v{version}.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2, ensure_ascii=False, cls=NumpyEncoder)\n\n    # Save Markdown report\n    md_path = os.path.join(ANALYSIS_DIR, f\"cross_alpha_v{version}_report.md\")\n    generate_markdown_report(output, md_path)\n\n    print_summary(output)\n    print(f\"\\nSaved: {json_path}\")\n    print(f\"Report: {md_path}\")\n\n    if args.update_registry:\n        print(\"\\n--- Registry update commands ---\")\n        for alpha_key, alpha_val, _ in all_data:\n            dr = dose_resp[alpha_key]\n            print(f\"# {alpha_key}: d1_drift={dr['distinct_1']['drift_pct']}%, \"\n                  f\"entropy_drift={dr['token_entropy']['drift_pct']}%, \"\n                  f\"ece_drift={dr['ece']['drift_pct']}%\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py",
    "content": "\"\"\"Cross-alpha analysis v4 with per-alpha consensus classification.\n\nExtends v3 with:\n  5. Per-alpha multi-method consensus classification (regime-dependent validity)\n  6. Markdown report output\n\nHandles mixed data paths:\n  - alpha-sweep: results/alpha_sweep/a{NNN}_s42/all_metrics.json (single seed)\n  - alpha=1.0:   results/mvp/rep_{42..45}/all_metrics.json (4 seeds)\n  - alpha=1.0 consensus loads existing method_ablation.json\n  - Single-seed alpha points: seed_threshold=1, method agreement only\n\nDependencies: numpy, scipy, statsmodels\n\"\"\"\n\nimport argparse\nimport glob\nimport json\nimport os\nimport re\nimport sys\nimport warnings\nfrom datetime import datetime\n\nimport numpy as np\nfrom statsmodels.stats.multitest import multipletests\n\nwarnings.filterwarnings(\"ignore\")\n\nBASE_DIR = os.path.dirname(os.path.abspath(__file__))\nsys.path.insert(0, BASE_DIR)\n\nfrom method_ablation import (\n    CANARY, DOWNSTREAM,\n    extract as ma_extract,\n    naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto, perm_granger,\n)\nfrom consensus_framework import classify_robust, load_sig_matrix, NumpyEncoder\n\nSWEEP_DIR = os.path.join(BASE_DIR, \"results\", \"alpha_sweep\")\nMVP_DIR = os.path.join(BASE_DIR, \"results\", \"mvp\")\nANALYSIS_DIR = os.path.join(BASE_DIR, \"results\", \"analysis\")\n\nMETRICS = [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"token_entropy\", \"ece\", \"perplexity\"]\n\nGRANGER_PAIRS = [\n    (\"token_entropy\", \"distinct_1\", \"entropy->d1\"),\n    (\"ece\",           \"distinct_1\", \"ECE->d1\"),\n    (\"token_entropy\", \"distinct_2\", \"entropy->d2\"),\n    (\"ece\",           \"distinct_2\", \"ECE->d2\"),\n    (\"distinct_1\", \"token_entropy\", \"d1->entropy\"),\n    (\"distinct_1\", \"ece\",           \"d1->ECE\"),\n    (\"distinct_2\", \"token_entropy\", \"d2->entropy\"),\n    (\"distinct_2\", \"ece\",           \"d2->ECE\"),\n]\n\nXCORR_PAIRS = [\n    (\"token_entropy\", \"distinct_1\", \"entropy_vs_d1\"),\n    (\"ece\",           \"distinct_1\", \"ece_vs_d1\"),\n]\n\nMA_METHODS = [\"naive_pearson\", \"differenced_xcorr\", \"threshold_onset\",\n              \"toda_yamamoto\", \"permutation_granger\"]\nMA_METHOD_FN = {\n    \"naive_pearson\": naive_pearson,\n    \"differenced_xcorr\": diff_xcorr,\n    \"threshold_onset\": threshold_lead,\n    \"toda_yamamoto\": toda_yamamoto,\n    \"permutation_granger\": perm_granger,\n}\n\n\n# ---------------------------------------------------------------------------\n# Data loading (extended for MVP alpha=1.0)\n# ---------------------------------------------------------------------------\n\ndef _find_mvp_seeds():\n    seeds = []\n    if not os.path.isdir(MVP_DIR):\n        return seeds\n    for d in sorted(os.listdir(MVP_DIR)):\n        m = re.match(r\"rep_(\\d+)$\", d)\n        if m and os.path.isfile(os.path.join(MVP_DIR, d, \"all_metrics.json\")):\n            seeds.append(int(m.group(1)))\n    return sorted(seeds)\n\n\ndef discover_alpha_dirs(explicit=None, include_mvp=True):\n    \"\"\"Find alpha directories.\n\n    Returns sorted list of (alpha_key, alpha_float, path, seeds).\n    \"\"\"\n    dirs = []\n\n    if explicit:\n        for name in explicit:\n            if name in (\"mvp\", \"a100_mvp\"):\n                rep42 = os.path.join(MVP_DIR, \"rep_42\")\n                if os.path.isdir(rep42):\n                    dirs.append((\"a100\", 1.0, rep42, _find_mvp_seeds()))\n                continue\n            path = os.path.join(SWEEP_DIR, name)\n            if not os.path.isdir(path):\n                print(f\"WARNING: {path} not found, skipping\", file=sys.stderr)\n                continue\n            m = re.match(r\"a(\\d{3})_s(\\d+)\", name)\n            if m:\n                alpha_val = int(m.group(1)) / 100.0\n                dirs.append((f\"a{m.group(1)}\", alpha_val, path, [int(m.group(2))]))\n    else:\n        pattern = os.path.join(SWEEP_DIR, \"a*_s42\")\n        for path in sorted(glob.glob(pattern)):\n            name = os.path.basename(path)\n            m = re.match(r\"a(\\d{3})_s42\", name)\n            if m:\n                alpha_val = int(m.group(1)) / 100.0\n                dirs.append((f\"a{m.group(1)}\", alpha_val, path, [42]))\n\n        if include_mvp and not any(d[1] == 1.0 for d in dirs):\n            rep42 = os.path.join(MVP_DIR, \"rep_42\")\n            if os.path.isdir(rep42):\n                dirs.append((\"a100\", 1.0, rep42, _find_mvp_seeds()))\n\n    return sorted(dirs, key=lambda x: x[1])\n\n\ndef load_metrics(alpha_dir):\n    path = os.path.join(alpha_dir, \"all_metrics.json\")\n    with open(path) as f:\n        data = json.load(f)\n    return sorted(data, key=lambda x: x[\"generation\"])\n\n\ndef load_all_seeds_metrics(alpha_val, primary_dir, seeds):\n    \"\"\"Load metrics for all seeds. Returns list of (seed, metrics_list).\"\"\"\n    results = []\n    for seed in seeds:\n        if alpha_val == 1.0:\n            path = os.path.join(MVP_DIR, f\"rep_{seed}\")\n        else:\n            path = primary_dir\n        mpath = os.path.join(path, \"all_metrics.json\")\n        if os.path.isfile(mpath):\n            results.append((seed, load_metrics(path)))\n    return results\n\n\ndef extract_series(metrics_list, key):\n    return np.array([m[key] for m in metrics_list], dtype=float)\n\n\n# ---------------------------------------------------------------------------\n# 1. Dose-response\n# ---------------------------------------------------------------------------\n\ndef compute_dose_response(all_data):\n    result = {}\n    for alpha_key, alpha_val, metrics_list in all_data:\n        entry = {\"alpha\": alpha_val}\n        for metric in METRICS:\n            vals = extract_series(metrics_list, metric)\n            gen0, genN = vals[0], vals[-1]\n            drift_pct = round((genN - gen0) / abs(gen0) * 100, 2) if abs(gen0) > 1e-12 else 0.0\n            entry[metric] = {\n                \"gen0\": round(float(gen0), 6),\n                f\"gen{len(vals)-1}\": round(float(genN), 6),\n                \"drift_pct\": drift_pct,\n            }\n        result[alpha_key] = entry\n    return result\n\n\n# ---------------------------------------------------------------------------\n# 2. Permutation Granger causality\n# ---------------------------------------------------------------------------\n\ndef _build_lag_matrix(y, x, max_lag):\n    T = len(y)\n    n = T - max_lag\n    Y = y[max_lag:]\n    cols_r = [np.ones(n)]\n    for lag in range(1, max_lag + 1):\n        cols_r.append(y[max_lag - lag: T - lag])\n    cols_u = list(cols_r)\n    for lag in range(1, max_lag + 1):\n        cols_u.append(x[max_lag - lag: T - lag])\n    return Y, np.column_stack(cols_r), np.column_stack(cols_u)\n\n\ndef _granger_f_stat(y, x, max_lag):\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\n    n = len(Y)\n    q = max_lag\n    try:\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\n    except np.linalg.LinAlgError:\n        return np.nan\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\n    k_u = X_u.shape[1]\n    df_resid = n - k_u\n    if df_resid <= 0 or rss_u < 1e-15:\n        return np.nan\n    return ((rss_r - rss_u) / q) / (rss_u / df_resid)\n\n\ndef permutation_granger_test(x, y, max_lag=1, n_perm=5000, seed=42, difference=True):\n    x = np.asarray(x, dtype=float)\n    y = np.asarray(y, dtype=float)\n    if difference:\n        x, y = np.diff(x), np.diff(y)\n    T = len(x)\n    if T <= max_lag + 2:\n        return {\"f_stat\": None, \"p_raw\": None, \"note\": f\"Series too short: T={T}\"}\n\n    f_obs = _granger_f_stat(y, x, max_lag)\n    if np.isnan(f_obs):\n        return {\"f_stat\": None, \"p_raw\": None, \"note\": \"F-stat computation failed\"}\n\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\n    rss_r = np.sum((Y - X_r @ np.linalg.lstsq(X_r, Y, rcond=None)[0]) ** 2)\n    rss_u = np.sum((Y - X_u @ np.linalg.lstsq(X_u, Y, rcond=None)[0]) ** 2)\n    f2 = (rss_r - rss_u) / rss_u if rss_u > 1e-15 else None\n\n    rng = np.random.default_rng(seed)\n    null_f = np.empty(n_perm)\n    for i in range(n_perm):\n        null_f[i] = _granger_f_stat(y, rng.permutation(x), max_lag)\n    valid = null_f[~np.isnan(null_f)]\n    if len(valid) == 0:\n        return {\"f_stat\": round(float(f_obs), 4), \"p_raw\": None, \"note\": \"All permutations failed\"}\n\n    p_value = (np.sum(valid >= f_obs) + 1) / (len(valid) + 1)\n    return {\n        \"f_stat\": round(float(f_obs), 4),\n        \"p_raw\": round(float(p_value), 6),\n        \"n_perm\": n_perm,\n        \"effect_size_f2\": round(float(f2), 4) if f2 is not None else None,\n    }\n\n\ndef run_granger_all(all_data, max_lag=1, n_perms=5000):\n    results = []\n    for alpha_key, alpha_val, metrics_list in all_data:\n        for cause_key, effect_key, label in GRANGER_PAIRS:\n            x = extract_series(metrics_list, cause_key)\n            y = extract_series(metrics_list, effect_key)\n            res = permutation_granger_test(x, y, max_lag=max_lag, n_perm=n_perms)\n            res.update({\n                \"alpha\": alpha_val,\n                \"alpha_key\": alpha_key,\n                \"direction\": label,\n                \"cause\": cause_key,\n                \"effect\": effect_key,\n            })\n            results.append(res)\n    return results\n\n\ndef apply_fdr(granger_results):\n    valid_idx = [i for i, r in enumerate(granger_results) if r.get(\"p_raw\") is not None]\n    if not valid_idx:\n        return granger_results\n\n    raw_ps = [granger_results[i][\"p_raw\"] for i in valid_idx]\n    _, fdr_ps, _, _ = multipletests(raw_ps, method=\"fdr_bh\")\n\n    for j, idx in enumerate(valid_idx):\n        granger_results[idx][\"p_fdr\"] = round(float(fdr_ps[j]), 6)\n\n    for r in granger_results:\n        if r.get(\"alpha\", -1) == 0.0 and r.get(\"p_raw\") is not None and r[\"p_raw\"] < 0.05:\n            r[\"note\"] = \"consistent with FPR, likely false positive\"\n\n    return granger_results\n\n\n# ---------------------------------------------------------------------------\n# 3. Cross-correlation lead-lag\n# ---------------------------------------------------------------------------\n\ndef cross_correlation(all_data, max_lag=3):\n    result = {}\n    for alpha_key, alpha_val, metrics_list in all_data:\n        entry = {\"alpha\": alpha_val}\n        for cause_key, effect_key, pair_label in XCORR_PAIRS:\n            dx = np.diff(extract_series(metrics_list, cause_key))\n            dy = np.diff(extract_series(metrics_list, effect_key))\n            lags = {}\n            best_lag, best_r = 0, 0.0\n            for lag in range(-max_lag, max_lag + 1):\n                if lag >= 0:\n                    a, b = dx[:len(dx) - lag] if lag > 0 else dx, dy[lag:] if lag > 0 else dy\n                else:\n                    a, b = dx[-lag:], dy[:len(dy) + lag]\n                n = min(len(a), len(b))\n                if n < 3:\n                    continue\n                a, b = a[:n], b[:n]\n                std_a, std_b = np.std(a, ddof=1), np.std(b, ddof=1)\n                if std_a < 1e-15 or std_b < 1e-15:\n                    r = 0.0\n                else:\n                    r = float(np.corrcoef(a, b)[0, 1])\n                lags[str(lag)] = round(r, 4)\n                if abs(r) > abs(best_r):\n                    best_lag, best_r = lag, r\n            entry[pair_label] = {\n                \"peak_lag\": best_lag,\n                \"peak_r\": round(best_r, 4),\n                \"lags\": lags,\n            }\n        result[alpha_key] = entry\n    return result\n\n\n# ---------------------------------------------------------------------------\n# 4. Per-gen velocity\n# ---------------------------------------------------------------------------\n\ndef per_gen_velocity(all_data):\n    result = {}\n    for alpha_key, alpha_val, metrics_list in all_data:\n        vals = extract_series(metrics_list, \"distinct_1\")\n        deltas = np.diff(vals)\n        n = len(deltas)\n        mid = n // 2\n        early_mean = float(np.mean(deltas[:mid])) if mid > 0 else None\n        late_mean = float(np.mean(deltas[mid:])) if mid < n else None\n        max_drop_idx = int(np.argmin(deltas))\n        result[alpha_key] = {\n            \"alpha\": alpha_val,\n            \"d1_values\": [round(float(v), 6) for v in vals],\n            \"d1_deltas\": [round(float(d), 6) for d in deltas],\n            \"cumulative_drift_pct\": round((vals[-1] - vals[0]) / abs(vals[0]) * 100, 2),\n            \"mean_velocity\": round(float(np.mean(deltas)), 6),\n            \"max_drop_gen\": max_drop_idx,\n            \"max_drop_value\": round(float(deltas[max_drop_idx]), 6),\n            \"early_mean_velocity\": round(early_mean, 6) if early_mean is not None else None,\n            \"late_mean_velocity\": round(late_mean, 6) if late_mean is not None else None,\n            \"deceleration_ratio\": round(late_mean / early_mean, 4) if early_mean and abs(early_mean) > 1e-12 else None,\n        }\n    return result\n\n\n# ---------------------------------------------------------------------------\n# 5. Per-alpha consensus classification\n# ---------------------------------------------------------------------------\n\ndef run_consensus_per_alpha(alpha_dirs, mvp_ablation_path=None, consensus_n_perm=1000):\n    \"\"\"Run 5-method consensus classification at each alpha point.\n\n    alpha=1.0 with existing method_ablation.json: load directly (4 seeds).\n    Other alpha points: run 5 methods on single-seed data, seed_threshold=1.\n    \"\"\"\n    results = {}\n\n    for alpha_key, alpha_val, primary_dir, seeds in alpha_dirs:\n        # alpha=1.0: use existing method_ablation.json\n        if alpha_val == 1.0 and mvp_ablation_path and os.path.isfile(mvp_ablation_path):\n            sig, pair_names, method_names, ab_seeds = load_sig_matrix(mvp_ablation_path)\n            n_m, n_p, n_s = sig.shape\n            mt = n_m - 1  # 4/5\n            st = 3        # 3/4 seeds\n            consensus = classify_robust(sig, mt, st)\n\n            for cl in consensus[\"classifications\"]:\n                pi = cl[\"pair_index\"]\n                cl[\"canary\"] = pair_names[pi][0]\n                cl[\"downstream\"] = pair_names[pi][1]\n                cl[\"pair_label\"] = f\"{pair_names[pi][0]}→{pair_names[pi][1]}\"\n\n            results[alpha_key] = {\n                \"alpha\": alpha_val,\n                \"n_seeds\": n_s,\n                \"seeds\": ab_seeds,\n                \"mode\": \"full_consensus\",\n                \"note\": f\"{n_s}-seed full consensus (≥{mt}/{n_m} methods, ≥{st}/{n_s} seeds)\",\n                \"method_threshold\": mt,\n                \"seed_threshold\": st,\n                \"n_methods\": n_m,\n                \"n_pairs\": n_p,\n                \"consensus\": consensus,\n                \"pair_names\": [list(p) for p in pair_names],\n            }\n            continue\n\n        # Other alpha points: run 5 methods from scratch\n        seed_data = load_all_seeds_metrics(alpha_val, primary_dir, seeds)\n        n_seeds = len(seed_data)\n        n_pairs = len(CANARY) * len(DOWNSTREAM)\n        n_methods = len(MA_METHODS)\n\n        sig_matrix = np.zeros((n_methods, n_pairs, n_seeds), dtype=bool)\n        pair_names = []\n\n        for si, (seed, metrics_list) in enumerate(seed_data):\n            pi = 0\n            for cn in CANARY:\n                c = ma_extract(metrics_list, cn)\n                for dn in DOWNSTREAM:\n                    if si == 0:\n                        pair_names.append((cn, dn))\n                    d = ma_extract(metrics_list, dn)\n                    for mi, method_name in enumerate(MA_METHODS):\n                        fn = MA_METHOD_FN[method_name]\n                        try:\n                            if method_name == \"permutation_granger\":\n                                res = fn(c, d, cn, dn, n_perm=consensus_n_perm)\n                            else:\n                                res = fn(c, d, cn, dn)\n                            sig_matrix[mi, pi, si] = res.get(\"significant\", False)\n                        except Exception:\n                            sig_matrix[mi, pi, si] = False\n                    pi += 1\n\n        st = 1 if n_seeds == 1 else 3\n        mt = n_methods - 1  # 4/5\n\n        consensus = classify_robust(sig_matrix, mt, st)\n        for cl in consensus[\"classifications\"]:\n            pi = cl[\"pair_index\"]\n            cl[\"canary\"] = pair_names[pi][0]\n            cl[\"downstream\"] = pair_names[pi][1]\n            cl[\"pair_label\"] = f\"{pair_names[pi][0]}→{pair_names[pi][1]}\"\n\n        mode = \"method_agreement_only\" if n_seeds == 1 else \"full_consensus\"\n        note_prefix = \"single-seed, method agreement only\" if n_seeds == 1 else f\"{n_seeds}-seed full consensus\"\n\n        results[alpha_key] = {\n            \"alpha\": alpha_val,\n            \"n_seeds\": n_seeds,\n            \"seeds\": [s for s, _ in seed_data],\n            \"mode\": mode,\n            \"note\": f\"{note_prefix} (≥{mt}/{n_methods} methods, ≥{st}/{n_seeds} seeds)\",\n            \"method_threshold\": mt,\n            \"seed_threshold\": st,\n            \"n_methods\": n_methods,\n            \"n_pairs\": n_pairs,\n            \"consensus\": consensus,\n            \"pair_names\": [list(p) for p in pair_names],\n        }\n\n    return results\n\n\ndef consensus_regime_comparison(consensus_results):\n    \"\"\"Compare robust/non-robust classifications across alpha points.\"\"\"\n    alpha_keys = sorted(consensus_results.keys(),\n                        key=lambda k: consensus_results[k][\"alpha\"])\n    if not alpha_keys:\n        return {}\n\n    first = consensus_results[alpha_keys[0]]\n    pair_labels = [cl[\"pair_label\"] for cl in first[\"consensus\"][\"classifications\"]]\n\n    pairs_comp = {}\n    for label in pair_labels:\n        row = {\"pair\": label, \"per_alpha\": {}}\n        for ak in alpha_keys:\n            cr = consensus_results[ak]\n            cls = [c for c in cr[\"consensus\"][\"classifications\"] if c[\"pair_label\"] == label]\n            if cls:\n                cl = cls[0]\n                row[\"per_alpha\"][ak] = {\n                    \"alpha\": cr[\"alpha\"],\n                    \"is_robust\": cl[\"is_robust\"],\n                    \"n_sig_methods\": cl[\"n_sig_methods\"],\n                    \"mode\": cr[\"mode\"],\n                }\n        verdicts = [v[\"is_robust\"] for v in row[\"per_alpha\"].values()]\n        row[\"stable\"] = len(set(verdicts)) <= 1\n        row[\"all_robust\"] = all(verdicts) if verdicts else False\n        row[\"all_non_robust\"] = not any(verdicts) if verdicts else True\n        pairs_comp[label] = row\n\n    n_stable = sum(1 for r in pairs_comp.values() if r[\"stable\"])\n    return {\n        \"alpha_keys\": alpha_keys,\n        \"alpha_values\": [consensus_results[ak][\"alpha\"] for ak in alpha_keys],\n        \"n_pairs\": len(pair_labels),\n        \"n_stable\": n_stable,\n        \"n_regime_dependent\": len(pair_labels) - n_stable,\n        \"pairs\": pairs_comp,\n    }\n\n\n# ---------------------------------------------------------------------------\n# 6. Markdown report\n# ---------------------------------------------------------------------------\n\ndef generate_markdown_report(output, out_path):\n    lines = []\n    lines.append(f\"# Cross-Alpha Analysis Report ({output['version']})\")\n    lines.append(\"\")\n    lines.append(f\"**Date:** {output['date']}\")\n    lines.append(f\"**Alpha points:** {output['alpha_points']}\")\n    lines.append(f\"**Generations:** {output['gen_range']}\")\n    lines.append(\"\")\n\n    # 1. Dose-response\n    lines.append(\"## 1. Dose-Response (gen0 to genN drift %)\")\n    lines.append(\"\")\n    dr = output[\"dose_response\"]\n    alphas = sorted(dr.keys())\n    header = \"| Metric |\"\n    sep = \"|--------|\"\n    for ak in alphas:\n        header += f\" α={dr[ak]['alpha']:.2f} |\"\n        sep += \"--------:|\"\n    lines.append(header)\n    lines.append(sep)\n    for metric in METRICS:\n        row = f\"| {metric} |\"\n        for ak in alphas:\n            d = dr[ak][metric][\"drift_pct\"]\n            row += f\" {d:+.1f}% |\"\n        lines.append(row)\n    lines.append(\"\")\n\n    # 2. Granger\n    lines.append(\"## 2. Granger Causality (bidirectional, permutation, FDR-corrected)\")\n    lines.append(\"\")\n    gc = output[\"granger_causality\"]\n    ak_list = sorted(set(r[\"alpha_key\"] for r in gc))\n    header = \"| Direction |\"\n    sep = \"|-----------|\"\n    for ak in ak_list:\n        a = [r for r in gc if r[\"alpha_key\"] == ak][0][\"alpha\"]\n        header += f\" α={a:.2f} p_raw | p_fdr |\"\n        sep += \"--------:|--------:|\"\n    lines.append(header)\n    lines.append(sep)\n    directions = list(dict.fromkeys(r[\"direction\"] for r in gc))\n    for d in directions:\n        row = f\"| {d} |\"\n        for ak in ak_list:\n            match = [r for r in gc if r[\"alpha_key\"] == ak and r[\"direction\"] == d]\n            if match:\n                r = match[0]\n                pr = f\"{r['p_raw']:.4f}\" if r.get(\"p_raw\") is not None else \"N/A\"\n                pf = f\"{r['p_fdr']:.4f}\" if r.get(\"p_fdr\") is not None else \"N/A\"\n                sig = \" *\" if r.get(\"p_fdr\") is not None and r[\"p_fdr\"] < 0.05 else \"\"\n                row += f\" {pr} | {pf}{sig} |\"\n            else:\n                row += \" -- | -- |\"\n        lines.append(row)\n    lines.append(\"\")\n    sc = output[\"statistical_config\"]\n    lines.append(f\"FDR: {sc['n_independent_tests']} tests, BH correction. \\\\* = p_fdr < 0.05\")\n    lines.append(\"\")\n\n    # 3. Consensus per alpha\n    if \"consensus_per_alpha\" in output:\n        lines.append(\"## 3. Consensus Classification (regime-dependent validity)\")\n        lines.append(\"\")\n        cpa = output[\"consensus_per_alpha\"]\n        for ak in sorted(cpa.keys(), key=lambda k: cpa[k][\"alpha\"]):\n            entry = cpa[ak]\n            lines.append(f\"### α={entry['alpha']:.2f} ({entry['note']})\")\n            lines.append(\"\")\n            lines.append(f\"- Robust pairs: {entry['consensus']['n_robust']}/{entry['n_pairs']}\")\n            lines.append(f\"- Non-robust: {entry['consensus']['n_non_robust']}/{entry['n_pairs']}\")\n            lines.append(\"\")\n            lines.append(\"| Pair | Robust | Methods |\")\n            lines.append(\"|------|--------|---------|\")\n            for cl in entry[\"consensus\"][\"classifications\"]:\n                tag = \"**ROBUST**\" if cl[\"is_robust\"] else \"non-robust\"\n                lines.append(f\"| {cl['pair_label']} | {tag} | {cl['n_sig_methods']}/{entry['n_methods']} |\")\n            lines.append(\"\")\n\n        if \"consensus_regime_comparison\" in output:\n            rc = output[\"consensus_regime_comparison\"]\n            lines.append(\"### Regime Comparison Summary\")\n            lines.append(\"\")\n            lines.append(f\"- Stable pairs (same classification at all α): {rc['n_stable']}/{rc['n_pairs']}\")\n            lines.append(f\"- Regime-dependent pairs: {rc['n_regime_dependent']}/{rc['n_pairs']}\")\n            lines.append(\"\")\n            header = \"| Pair |\"\n            sep = \"|------|\"\n            for av in rc[\"alpha_values\"]:\n                header += f\" α={av:.2f} |\"\n                sep += \"--------|\"\n            header += \" Stable |\"\n            sep += \"--------|\"\n            lines.append(header)\n            lines.append(sep)\n            for label, info in rc[\"pairs\"].items():\n                row = f\"| {label} |\"\n                for ak in rc[\"alpha_keys\"]:\n                    if ak in info[\"per_alpha\"]:\n                        v = info[\"per_alpha\"][ak]\n                        tag = f\"R({v['n_sig_methods']})\" if v[\"is_robust\"] else f\".({v['n_sig_methods']})\"\n                        row += f\" {tag} |\"\n                    else:\n                        row += \" - |\"\n                row += f\" {'Y' if info['stable'] else 'N'} |\"\n                lines.append(row)\n            lines.append(\"\")\n\n    # 4. Velocity\n    lines.append(\"## 4. D1 Velocity\")\n    lines.append(\"\")\n    vel = output[\"per_gen_velocity\"]\n    lines.append(\"| α | mean_vel | early | late | decel_ratio |\")\n    lines.append(\"|---|----------|-------|------|-------------|\")\n    for ak in sorted(vel.keys()):\n        v = vel[ak]\n        decel = f\"{v['deceleration_ratio']:.2f}\" if v.get(\"deceleration_ratio\") else \"N/A\"\n        lines.append(f\"| {v['alpha']:.2f} | {v['mean_velocity']:+.6f} | \"\n                     f\"{v['early_mean_velocity']:+.6f} | {v['late_mean_velocity']:+.6f} | {decel} |\")\n    lines.append(\"\")\n\n    with open(out_path, \"w\") as f:\n        f.write(\"\\n\".join(lines))\n    return out_path\n\n\n# ---------------------------------------------------------------------------\n# Output / summary\n# ---------------------------------------------------------------------------\n\ndef auto_version():\n    os.makedirs(ANALYSIS_DIR, exist_ok=True)\n    existing = glob.glob(os.path.join(ANALYSIS_DIR, \"cross_alpha_v*.json\"))\n    max_v = 0\n    for f in existing:\n        m = re.search(r\"cross_alpha_v(\\d+)\", f)\n        if m:\n            max_v = max(max_v, int(m.group(1)))\n    return max_v + 1\n\n\ndef print_summary(output):\n    print(\"\\n\" + \"=\" * 80)\n    print(\"CROSS-ALPHA ANALYSIS SUMMARY (v4)\")\n    print(\"=\" * 80)\n\n    # Dose-response table\n    dr = output[\"dose_response\"]\n    alphas = sorted(dr.keys())\n    print(f\"\\nDOSE-RESPONSE (drift %)\")\n    print(\"-\" * 80)\n    header = f\"{'Metric':<16}\"\n    for ak in alphas:\n        header += f\" | a={dr[ak]['alpha']:<5}\"\n    print(header)\n    print(\"-\" * 80)\n    for metric in METRICS:\n        line = f\"{metric:<16}\"\n        for ak in alphas:\n            d = dr[ak][metric][\"drift_pct\"]\n            line += f\" | {d:>+7.1f}%\"\n        print(line)\n\n    # Granger table\n    gc = output[\"granger_causality\"]\n    print(f\"\\nGRANGER CAUSALITY (bidirectional, differenced, permutation)\")\n    print(\"-\" * 80)\n    header = f\"{'Direction':<20}\"\n    alpha_keys = sorted(set(r[\"alpha_key\"] for r in gc))\n    for ak in alpha_keys:\n        header += f\" | a={[r for r in gc if r['alpha_key']==ak][0]['alpha']:<4} p_raw   p_fdr\"\n    print(header)\n    print(\"-\" * 80)\n\n    directions = list(dict.fromkeys(r[\"direction\"] for r in gc))\n    for d in directions:\n        line = f\"{d:<20}\"\n        for ak in alpha_keys:\n            match = [r for r in gc if r[\"alpha_key\"] == ak and r[\"direction\"] == d]\n            if match:\n                r = match[0]\n                p_raw = f\"{r['p_raw']:.4f}\" if r.get(\"p_raw\") is not None else \"  N/A \"\n                p_fdr = f\"{r.get('p_fdr', 'N/A')}\" if r.get(\"p_fdr\") is not None else \"  N/A \"\n                if isinstance(p_fdr, float):\n                    p_fdr = f\"{p_fdr:.4f}\"\n                sig = \"*\" if r.get(\"p_fdr\") is not None and r[\"p_fdr\"] < 0.05 else \" \"\n                fp = \"FP?\" if r.get(\"note\", \"\").startswith(\"consistent\") else \"   \"\n                line += f\" | {p_raw} {p_fdr:>7} {sig}{fp}\"\n            else:\n                line += f\" |    --       --     \"\n        print(line)\n\n    valid = [r for r in gc if r.get(\"p_raw\") is not None]\n    n_total = len(valid)\n    n_raw_sig = sum(1 for r in valid if r[\"p_raw\"] < 0.05)\n    n_fdr_sig = sum(1 for r in valid if r.get(\"p_fdr\") is not None and r[\"p_fdr\"] < 0.05)\n    print(f\"\\nFDR: {n_raw_sig}/{n_total} raw-sig -> {n_fdr_sig}/{n_total} FDR-sig \"\n          f\"(BH correction across all {n_total} tests)\")\n\n    # Consensus per alpha\n    if \"consensus_per_alpha\" in output:\n        cpa = output[\"consensus_per_alpha\"]\n        print(f\"\\nCONSENSUS CLASSIFICATION PER ALPHA\")\n        print(\"-\" * 80)\n        for ak in sorted(cpa.keys(), key=lambda k: cpa[k][\"alpha\"]):\n            entry = cpa[ak]\n            print(f\"\\n  a={entry['alpha']:.2f} [{entry['note']}]\")\n            print(f\"    Robust: {entry['consensus']['n_robust']}/{entry['n_pairs']}, \"\n                  f\"Non-robust: {entry['consensus']['n_non_robust']}/{entry['n_pairs']}\")\n            for cl in entry[\"consensus\"][\"classifications\"]:\n                if cl[\"is_robust\"]:\n                    print(f\"      ROBUST  {cl['pair_label']:<35s} ({cl['n_sig_methods']}/{entry['n_methods']} methods)\")\n\n        if \"consensus_regime_comparison\" in output:\n            rc = output[\"consensus_regime_comparison\"]\n            print(f\"\\n  REGIME COMPARISON: {rc['n_stable']}/{rc['n_pairs']} stable, \"\n                  f\"{rc['n_regime_dependent']}/{rc['n_pairs']} regime-dependent\")\n            changed = [l for l, p in rc[\"pairs\"].items() if not p[\"stable\"]]\n            if changed:\n                print(f\"    Regime-dependent pairs:\")\n                for label in changed:\n                    info = rc[\"pairs\"][label]\n                    tags = []\n                    for ak in rc[\"alpha_keys\"]:\n                        if ak in info[\"per_alpha\"]:\n                            v = info[\"per_alpha\"][ak]\n                            t = \"R\" if v[\"is_robust\"] else \".\"\n                            tags.append(f\"a={v['alpha']:.2f}:{t}\")\n                    print(f\"      {label:<35s} {' '.join(tags)}\")\n\n    # Cross-correlation\n    xcorr = output[\"cross_correlation\"]\n    print(f\"\\nCROSS-CORRELATION (delta-metric, peak lag)\")\n    print(\"-\" * 60)\n    for pair_label in [\"entropy_vs_d1\", \"ece_vs_d1\"]:\n        line = f\"  {pair_label:<18}\"\n        for ak in sorted(xcorr.keys()):\n            p = xcorr[ak].get(pair_label, {})\n            line += f\" | a={xcorr[ak]['alpha']}: lag={p.get('peak_lag','?'):>2} r={p.get('peak_r','?'):>7}\"\n        print(line)\n\n    # Velocity\n    vel = output[\"per_gen_velocity\"]\n    print(f\"\\nD1 VELOCITY\")\n    print(\"-\" * 60)\n    for ak in sorted(vel.keys()):\n        v = vel[ak]\n        decel = f\"{v['deceleration_ratio']:.2f}\" if v.get(\"deceleration_ratio\") is not None else \"N/A\"\n        print(f\"  a={v['alpha']}: mean_vel={v['mean_velocity']:+.6f}  \"\n              f\"early={v['early_mean_velocity']:+.6f}  late={v['late_mean_velocity']:+.6f}  \"\n              f\"decel_ratio={decel}  max_drop=gen{v['max_drop_gen']}\")\n\n    print()\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Cross-alpha analysis v4 with per-alpha consensus classification.\"\n    )\n    parser.add_argument(\"--alpha-dirs\", nargs=\"*\", default=None,\n                        help=\"Specific alpha dirs (e.g. a000_s42 a025_s42 mvp). Default: auto-discover all.\")\n    parser.add_argument(\"--n-perms\", type=int, default=5000,\n                        help=\"Permutations for Granger test (default: 5000)\")\n    parser.add_argument(\"--consensus-n-perms\", type=int, default=1000,\n                        help=\"Permutations for consensus perm_granger method (default: 1000)\")\n    parser.add_argument(\"--max-lag\", type=int, default=1,\n                        help=\"Max lag for Granger test (default: 1)\")\n    parser.add_argument(\"--no-mvp\", action=\"store_true\",\n                        help=\"Exclude MVP (alpha=1.0) from auto-discovery\")\n    parser.add_argument(\"--no-consensus\", action=\"store_true\",\n                        help=\"Skip consensus classification (faster)\")\n    parser.add_argument(\"--version\", type=int, default=None,\n                        help=\"Output version number (default: auto-increment)\")\n    parser.add_argument(\"--update-registry\", action=\"store_true\",\n                        help=\"Print registry update commands after analysis\")\n    args = parser.parse_args()\n\n    alpha_dirs = discover_alpha_dirs(args.alpha_dirs, include_mvp=not args.no_mvp)\n    if not alpha_dirs:\n        print(\"ERROR: No alpha directories found.\", file=sys.stderr)\n        sys.exit(1)\n\n    print(f\"Found {len(alpha_dirs)} alpha points: \"\n          f\"{[(a[0], f'seeds={a[3]}') for a in alpha_dirs]}\")\n\n    # Load primary seed data (seed=42) for v3 analyses\n    all_data = []\n    for alpha_key, alpha_val, path, seeds in alpha_dirs:\n        metrics = load_metrics(path)\n        print(f\"  {alpha_key} (a={alpha_val}): {len(metrics)} generations, seeds={seeds}\")\n        all_data.append((alpha_key, alpha_val, metrics))\n\n    # 1. Dose-response\n    dose_resp = compute_dose_response(all_data)\n\n    # 2. Granger\n    print(f\"\\nRunning bidirectional Granger ({len(GRANGER_PAIRS)} pairs x {len(all_data)} alphas, \"\n          f\"n_perms={args.n_perms})...\")\n    granger = run_granger_all(all_data, max_lag=args.max_lag, n_perms=args.n_perms)\n    granger = apply_fdr(granger)\n\n    # 3. Cross-correlation\n    xcorr = cross_correlation(all_data)\n\n    # 4. Velocity\n    velocity = per_gen_velocity(all_data)\n\n    # Assemble output\n    version = args.version or auto_version()\n    n_gens = len(all_data[0][2]) if all_data else 0\n    output = {\n        \"version\": f\"v{version}\",\n        \"date\": datetime.now().strftime(\"%Y-%m-%d\"),\n        \"n_alphas\": len(all_data),\n        \"alpha_points\": [a[1] for a in all_data],\n        \"n_generations\": n_gens,\n        \"gen_range\": f\"gen_0 to gen_{n_gens - 1}\" if n_gens else \"N/A\",\n        \"statistical_config\": {\n            \"granger_max_lag\": args.max_lag,\n            \"granger_n_perm\": args.n_perms,\n            \"granger_differenced\": True,\n            \"fdr_method\": \"benjamini-hochberg\",\n            \"fdr_scope\": f\"all {len(granger)} tests corrected together\",\n            \"n_independent_tests\": len([r for r in granger if r.get(\"p_raw\") is not None]),\n        },\n        \"dose_response\": dose_resp,\n        \"granger_causality\": granger,\n        \"cross_correlation\": xcorr,\n        \"per_gen_velocity\": velocity,\n    }\n\n    # 5. Consensus per alpha\n    if not args.no_consensus:\n        mvp_ablation = os.path.join(MVP_DIR, \"analysis\", \"method_ablation.json\")\n        print(f\"\\nRunning per-alpha consensus classification \"\n              f\"(5 methods x 16 pairs x {len(alpha_dirs)} alphas)...\")\n        consensus_results = run_consensus_per_alpha(\n            alpha_dirs, mvp_ablation_path=mvp_ablation,\n            consensus_n_perm=args.consensus_n_perms)\n        output[\"consensus_per_alpha\"] = consensus_results\n        output[\"consensus_regime_comparison\"] = consensus_regime_comparison(consensus_results)\n\n    # Save JSON\n    os.makedirs(ANALYSIS_DIR, exist_ok=True)\n    json_path = os.path.join(ANALYSIS_DIR, f\"cross_alpha_v{version}.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2, ensure_ascii=False, cls=NumpyEncoder)\n\n    # Save Markdown report\n    md_path = os.path.join(ANALYSIS_DIR, f\"cross_alpha_v{version}_report.md\")\n    generate_markdown_report(output, md_path)\n\n    print_summary(output)\n    print(f\"\\nSaved: {json_path}\")\n    print(f\"Report: {md_path}\")\n\n    if args.update_registry:\n        print(\"\\n--- Registry update commands ---\")\n        for alpha_key, alpha_val, _ in all_data:\n            dr = dose_resp[alpha_key]\n            print(f\"# {alpha_key}: d1_drift={dr['distinct_1']['drift_pct']}%, \"\n                  f\"entropy_drift={dr['token_entropy']['drift_pct']}%, \"\n                  f\"ece_drift={dr['ece']['drift_pct']}%\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T09:02:00.701364+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_analysis_v4.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T09:02:00.701685+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cat > /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py << 'SCRIPT_EOF'\n\"\"\"Cross-alpha analysis v4 with per-alpha consensus classification.\n\nExtends v3 with:\n  5. Per-alpha multi-method consensus classification (regime-dependent validity)\n  6. Markdown report output\n\nHandles mixed data paths:\n  - alpha-sweep: results/alpha_sweep/a{NNN}_s42/all_metrics.json (single seed)\n  - alpha=1.0:   results/mvp/rep_{42..45}/all_metrics.json (4 seeds)\n  - alpha=1.0 consensus loads existing method_ablation.json\n  - Single-seed alpha points: seed_threshold=1, method agreement only\n\nDependencies: numpy, scipy, statsmodels\n\"\"\"\n\nimport argparse\nimport glob\nimport json\nimport os\nimport re\nimport sys\nimport warnings\nfrom datetime import datetime\n\nimport numpy as np\nfrom statsmodels.stats.multitest import multipletests\n\nwarnings.filterwarnings(\"ignore\")\n\nBASE_DIR = os.path.dirname(os.path.abspath(__file__))\nsys.path.insert(0, BASE_DIR)\n\nfrom method_ablation import (\n    CANARY, DOWNSTREAM,\n    extract as ma_extract,\n    naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto, perm_granger,\n)\nfrom consensus_framework import classify_robust, load_sig_matrix, NumpyEncoder\n\nSWEEP_DIR = os.path.join(BASE_DIR, \"results\", \"alpha_sweep\")\nMVP_DIR = os.path.join(BASE_DIR, \"results\", \"mvp\")\nANALYSIS_DIR = os.path.join(BASE_DIR, \"results\", \"analysis\")\n\nMETRICS = [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"token_entropy\", \"ece\", \"perplexity\"]\n\nGRANGER_PAIRS = [\n    (\"token_entropy\", \"distinct_1\", \"entropy->d1\"),\n    (\"ece\",           \"distinct_1\", \"ECE->d1\"),\n    (\"token_entropy\", \"distinct_2\", \"entropy->d2\"),\n    (\"ece\",           \"distinct_2\", \"ECE->d2\"),\n    (\"distinct_1\", \"token_entropy\", \"d1->entropy\"),\n    (\"distinct_1\", \"ece\",           \"d1->ECE\"),\n    (\"distinct_2\", \"token_entropy\", \"d2->entropy\"),\n    (\"distinct_2\", \"ece\",           \"d2->ECE\"),\n]\n\nXCORR_PAIRS = [\n    (\"token_entropy\", \"distinct_1\", \"entropy_vs_d1\"),\n    (\"ece\",           \"distinct_1\", \"ece_vs_d1\"),\n]\n\nMA_METHODS = [\"naive_pearson\", \"differenced_xcorr\", \"threshold_onset\",\n              \"toda_yamamoto\", \"permutation_granger\"]\nMA_METHOD_FN = {\n    \"naive_pearson\": naive_pearson,\n    \"differenced_xcorr\": diff_xcorr,\n    \"threshold_onset\": threshold_lead,\n    \"toda_yamamoto\": toda_yamamoto,\n    \"permutation_granger\": perm_granger,\n}\n\n\n# ---------------------------------------------------------------------------\n# Data loading (extended for MVP alpha=1.0)\n# ---------------------------------------------------------------------------\n\ndef _find_mvp_seeds():\n    seeds = []\n    if not os.path.isdir(MVP_DIR):\n        return seeds\n    for d in sorted(os.listdir(MVP_DIR)):\n        m = re.match(r\"rep_(\\d+)$\", d)\n        if m and os.path.isfile(os.path.join(MVP_DIR, d, \"all_metrics.json\")):\n            seeds.append(int(m.group(1)))\n    return sorted(seeds)\n\n\ndef discover_alpha_dirs(explicit=None, include_mvp=True):\n    \"\"\"Find alpha directories.\n\n    Returns sorted list of (alpha_key, alpha_float, path, seeds).\n    \"\"\"\n    dirs = []\n\n    if explicit:\n        for name in explicit:\n            if name in (\"mvp\", \"a100_mvp\"):\n                rep42 = os.path.join(MVP_DIR, \"rep_42\")\n                if os.path.isdir(rep42):\n                    dirs.append((\"a100\", 1.0, rep42, _find_mvp_seeds()))\n                continue\n            path = os.path.join(SWEEP_DIR, name)\n            if not os.path.isdir(path):\n                print(f\"WARNING: {path} not found, skipping\", file=sys.stderr)\n                continue\n            m = re.match(r\"a(\\d{3})_s(\\d+)\", name)\n            if m:\n                alpha_val = int(m.group(1)) / 100.0\n                dirs.append((f\"a{m.group(1)}\", alpha_val, path, [int(m.group(2))]))\n    else:\n        pattern = os.path.join(SWEEP_DIR, \"a*_s42\")\n        for path in sorted(glob.glob(pattern)):\n            name = os.path.basename(path)\n            m = re.match(r\"a(\\d{3})_s42\", name)\n            if m:\n                alpha_val = int(m.group(1)) / 100.0\n                dirs.append((f\"a{m.group(1)}\", alpha_val, path, [42]))\n\n        if include_mvp and not any(d[1] == 1.0 for d in dirs):\n            rep42 = os.path.join(MVP_DIR, \"rep_42\")\n            if os.path.isdir(rep42):\n                dirs.append((\"a100\", 1.0, rep42, _find_mvp_seeds()))\n\n    return sorted(dirs, key=lambda x: x[1])\n\n\ndef load_metrics(alpha_dir):\n    path = os.path.join(alpha_dir, \"all_metrics.json\")\n    with open(path) as f:\n        data = json.load(f)\n    return sorted(data, key=lambda x: x[\"generation\"])\n\n\ndef load_all_seeds_metrics(alpha_val, primary_dir, seeds):\n    \"\"\"Load metrics for all seeds. Returns list of (seed, metrics_list).\"\"\"\n    results = []\n    for seed in seeds:\n        if alpha_val == 1.0:\n            path = os.path.join(MVP_DIR, f\"rep_{seed}\")\n        else:\n            path = primary_dir\n        mpath = os.path.join(path, \"all_metrics.json\")\n        if os.path.isfile(mpath):\n            results.append((seed, load_metrics(path)))\n    return results\n\n\ndef extract_series(metrics_list, key):\n    return np.array([m[key] for m in metrics_list], dtype=float)\n\n\n# ---------------------------------------------------------------------------\n# 1. Dose-response\n# ---------------------------------------------------------------------------\n\ndef compute_dose_response(all_data):\n    result = {}\n    for alpha_key, alpha_val, metrics_list in all_data:\n        entry = {\"alpha\": alpha_val}\n        for metric in METRICS:\n            vals = extract_series(metrics_list, metric)\n            gen0, genN = vals[0], vals[-1]\n            drift_pct = round((genN - gen0) / abs(gen0) * 100, 2) if abs(gen0) > 1e-12 else 0.0\n            entry[metric] = {\n                \"gen0\": round(float(gen0), 6),\n                f\"gen{len(vals)-1}\": round(float(genN), 6),\n                \"drift_pct\": drift_pct,\n            }\n        result[alpha_key] = entry\n    return result\n\n\n# ---------------------------------------------------------------------------\n# 2. Permutation Granger causality\n# ---------------------------------------------------------------------------\n\ndef _build_lag_matrix(y, x, max_lag):\n    T = len(y)\n    n = T - max_lag\n    Y = y[max_lag:]\n    cols_r = [np.ones(n)]\n    for lag in range(1, max_lag + 1):\n        cols_r.append(y[max_lag - lag: T - lag])\n    cols_u = list(cols_r)\n    for lag in range(1, max_lag + 1):\n        cols_u.append(x[max_lag - lag: T - lag])\n    return Y, np.column_stack(cols_r), np.column_stack(cols_u)\n\n\ndef _granger_f_stat(y, x, max_lag):\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\n    n = len(Y)\n    q = max_lag\n    try:\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\n    except np.linalg.LinAlgError:\n        return np.nan\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\n    k_u = X_u.shape[1]\n    df_resid = n - k_u\n    if df_resid <= 0 or rss_u < 1e-15:\n        return np.nan\n    return ((rss_r - rss_u) / q) / (rss_u / df_resid)\n\n\ndef permutation_granger_test(x, y, max_lag=1, n_perm=5000, seed=42, difference=True):\n    x = np.asarray(x, dtype=float)\n    y = np.asarray(y, dtype=float)\n    if difference:\n        x, y = np.diff(x), np.diff(y)\n    T = len(x)\n    if T <= max_lag + 2:\n        return {\"f_stat\": None, \"p_raw\": None, \"note\": f\"Series too short: T={T}\"}\n\n    f_obs = _granger_f_stat(y, x, max_lag)\n    if np.isnan(f_obs):\n        return {\"f_stat\": None, \"p_raw\": None, \"note\": \"F-stat computation failed\"}\n\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\n    rss_r = np.sum((Y - X_r @ np.linalg.lstsq(X_r, Y, rcond=None)[0]) ** 2)\n    rss_u = np.sum((Y - X_u @ np.linalg.lstsq(X_u, Y, rcond=None)[0]) ** 2)\n    f2 = (rss_r - rss_u) / rss_u if rss_u > 1e-15 else None\n\n    rng = np.random.default_rng(seed)\n    null_f = np.empty(n_perm)\n    for i in range(n_perm):\n        null_f[i] = _granger_f_stat(y, rng.permutation(x), max_lag)\n    valid = null_f[~np.isnan(null_f)]\n    if len(valid) == 0:\n        return {\"f_stat\": round(float(f_obs), 4), \"p_raw\": None, \"note\": \"All permutations failed\"}\n\n    p_value = (np.sum(valid >= f_obs) + 1) / (len(valid) + 1)\n    return {\n        \"f_stat\": round(float(f_obs), 4),\n        \"p_raw\": round(float(p_value), 6),\n        \"n_perm\": n_perm,\n        \"effect_size_f2\": round(float(f2), 4) if f2 is not None else None,\n    }\n\n\ndef run_granger_all(all_data, max_lag=1, n_perms=5000):\n    results = []\n    for alpha_key, alpha_val, metrics_list in all_data:\n        for cause_key, effect_key, label in GRANGER_PAIRS:\n            x = extract_series(metrics_list, cause_key)\n            y = extract_series(metrics_list, effect_key)\n            res = permutation_granger_test(x, y, max_lag=max_lag, n_perm=n_perms)\n            res.update({\n                \"alpha\": alpha_val,\n                \"alpha_key\": alpha_key,\n                \"direction\": label,\n                \"cause\": cause_key,\n                \"effect\": effect_key,\n            })\n            results.append(res)\n    return results\n\n\ndef apply_fdr(granger_results):\n    valid_idx = [i for i, r in enumerate(granger_results) if r.get(\"p_raw\") is not None]\n    if not valid_idx:\n        return granger_results\n\n    raw_ps = [granger_results[i][\"p_raw\"] for i in valid_idx]\n    _, fdr_ps, _, _ = multipletests(raw_ps, method=\"fdr_bh\")\n\n    for j, idx in enumerate(valid_idx):\n        granger_results[idx][\"p_fdr\"] = round(float(fdr_ps[j]), 6)\n\n    for r in granger_results:\n        if r.get(\"alpha\", -1) == 0.0 and r.get(\"p_raw\") is not None and r[\"p_raw\"] < 0.05:\n            r[\"note\"] = \"consistent with FPR, likely false positive\"\n\n    return granger_results\n\n\n# ---------------------------------------------------------------------------\n# 3. Cross-correlation lead-lag\n# ---------------------------------------------------------------------------\n\ndef cross_correlation(all_data, max_lag=3):\n    result = {}\n    for alpha_key, alpha_val, metrics_list in all_data:\n        entry = {\"alpha\": alpha_val}\n        for cause_key, effect_key, pair_label in XCORR_PAIRS:\n            dx = np.diff(extract_series(metrics_list, cause_key))\n            dy = np.diff(extract_series(metrics_list, effect_key))\n            lags = {}\n            best_lag, best_r = 0, 0.0\n            for lag in range(-max_lag, max_lag + 1):\n                if lag >= 0:\n                    a, b = dx[:len(dx) - lag] if lag > 0 else dx, dy[lag:] if lag > 0 else dy\n                else:\n                    a, b = dx[-lag:], dy[:len(dy) + lag]\n                n = min(len(a), len(b))\n                if n < 3:\n                    continue\n                a, b = a[:n], b[:n]\n                std_a, std_b = np.std(a, ddof=1), np.std(b, ddof=1)\n                if std_a < 1e-15 or std_b < 1e-15:\n                    r = 0.0\n                else:\n                    r = float(np.corrcoef(a, b)[0, 1])\n                lags[str(lag)] = round(r, 4)\n                if abs(r) > abs(best_r):\n                    best_lag, best_r = lag, r\n            entry[pair_label] = {\n                \"peak_lag\": best_lag,\n                \"peak_r\": round(best_r, 4),\n                \"lags\": lags,\n            }\n        result[alpha_key] = entry\n    return result\n\n\n# ---------------------------------------------------------------------------\n# 4. Per-gen velocity\n# ---------------------------------------------------------------------------\n\ndef per_gen_velocity(all_data):\n    result = {}\n    for alpha_key, alpha_val, metrics_list in all_data:\n        vals = extract_series(metrics_list, \"distinct_1\")\n        deltas = np.diff(vals)\n        n = len(deltas)\n        mid = n // 2\n        early_mean = float(np.mean(deltas[:mid])) if mid > 0 else None\n        late_mean = float(np.mean(deltas[mid:])) if mid < n else None\n        max_drop_idx = int(np.argmin(deltas))\n        result[alpha_key] = {\n            \"alpha\": alpha_val,\n            \"d1_values\": [round(float(v), 6) for v in vals],\n            \"d1_deltas\": [round(float(d), 6) for d in deltas],\n            \"cumulative_drift_pct\": round((vals[-1] - vals[0]) / abs(vals[0]) * 100, 2),\n            \"mean_velocity\": round(float(np.mean(deltas)), 6),\n            \"max_drop_gen\": max_drop_idx,\n            \"max_drop_value\": round(float(deltas[max_drop_idx]), 6),\n            \"early_mean_velocity\": round(early_mean, 6) if early_mean is not None else None,\n            \"late_mean_velocity\": round(late_mean, 6) if late_mean is not None else None,\n            \"deceleration_ratio\": round(late_mean / early_mean, 4) if early_mean and abs(early_mean) > 1e-12 else None,\n        }\n    return result\n\n\n# ---------------------------------------------------------------------------\n# 5. Per-alpha consensus classification\n# ---------------------------------------------------------------------------\n\ndef run_consensus_per_alpha(alpha_dirs, mvp_ablation_path=None, consensus_n_perm=1000):\n    \"\"\"Run 5-method consensus classification at each alpha point.\n\n    alpha=1.0 with existing method_ablation.json: load directly (4 seeds).\n    Other alpha points: run 5 methods on single-seed data, seed_threshold=1.\n    \"\"\"\n    results = {}\n\n    for alpha_key, alpha_val, primary_dir, seeds in alpha_dirs:\n        # alpha=1.0: use existing method_ablation.json\n        if alpha_val == 1.0 and mvp_ablation_path and os.path.isfile(mvp_ablation_path):\n            sig, pair_names, method_names, ab_seeds = load_sig_matrix(mvp_ablation_path)\n            n_m, n_p, n_s = sig.shape\n            mt = n_m - 1  # 4/5\n            st = 3        # 3/4 seeds\n            consensus = classify_robust(sig, mt, st)\n\n            for cl in consensus[\"classifications\"]:\n                pi = cl[\"pair_index\"]\n                cl[\"canary\"] = pair_names[pi][0]\n                cl[\"downstream\"] = pair_names[pi][1]\n                cl[\"pair_label\"] = f\"{pair_names[pi][0]}→{pair_names[pi][1]}\"\n\n            results[alpha_key] = {\n                \"alpha\": alpha_val,\n                \"n_seeds\": n_s,\n                \"seeds\": ab_seeds,\n                \"mode\": \"full_consensus\",\n                \"note\": f\"{n_s}-seed full consensus (≥{mt}/{n_m} methods, ≥{st}/{n_s} seeds)\",\n                \"method_threshold\": mt,\n                \"seed_threshold\": st,\n                \"n_methods\": n_m,\n                \"n_pairs\": n_p,\n                \"consensus\": consensus,\n                \"pair_names\": [list(p) for p in pair_names],\n            }\n            continue\n\n        # Other alpha points: run 5 methods from scratch\n        seed_data = load_all_seeds_metrics(alpha_val, primary_dir, seeds)\n        n_seeds = len(seed_data)\n        n_pairs = len(CANARY) * len(DOWNSTREAM)\n        n_methods = len(MA_METHODS)\n\n        sig_matrix = np.zeros((n_methods, n_pairs, n_seeds), dtype=bool)\n        pair_names = []\n\n        for si, (seed, metrics_list) in enumerate(seed_data):\n            pi = 0\n            for cn in CANARY:\n                c = ma_extract(metrics_list, cn)\n                for dn in DOWNSTREAM:\n                    if si == 0:\n                        pair_names.append((cn, dn))\n                    d = ma_extract(metrics_list, dn)\n                    for mi, method_name in enumerate(MA_METHODS):\n                        fn = MA_METHOD_FN[method_name]\n                        try:\n                            if method_name == \"permutation_granger\":\n                                res = fn(c, d, cn, dn, n_perm=consensus_n_perm)\n                            else:\n                                res = fn(c, d, cn, dn)\n                            sig_matrix[mi, pi, si] = res.get(\"significant\", False)\n                        except Exception:\n                            sig_matrix[mi, pi, si] = False\n                    pi += 1\n\n        st = 1 if n_seeds == 1 else 3\n        mt = n_methods - 1  # 4/5\n\n        consensus = classify_robust(sig_matrix, mt, st)\n        for cl in consensus[\"classifications\"]:\n            pi = cl[\"pair_index\"]\n            cl[\"canary\"] = pair_names[pi][0]\n            cl[\"downstream\"] = pair_names[pi][1]\n            cl[\"pair_label\"] = f\"{pair_names[pi][0]}→{pair_names[pi][1]}\"\n\n        mode = \"method_agreement_only\" if n_seeds == 1 else \"full_consensus\"\n        note_prefix = \"single-seed, method agreement only\" if n_seeds == 1 else f\"{n_seeds}-seed full consensus\"\n\n        results[alpha_key] = {\n            \"alpha\": alpha_val,\n            \"n_seeds\": n_seeds,\n            \"seeds\": [s for s, _ in seed_data],\n            \"mode\": mode,\n            \"note\": f\"{note_prefix} (≥{mt}/{n_methods} methods, ≥{st}/{n_seeds} seeds)\",\n            \"method_threshold\": mt,\n            \"seed_threshold\": st,\n            \"n_methods\": n_methods,\n            \"n_pairs\": n_pairs,\n            \"consensus\": consensus,\n            \"pair_names\": [list(p) for p in pair_names],\n        }\n\n    return results\n\n\ndef consensus_regime_comparison(consensus_results):\n    \"\"\"Compare robust/non-robust classifications across alpha points.\"\"\"\n    alpha_keys = sorted(consensus_results.keys(),\n                        key=lambda k: consensus_results[k][\"alpha\"])\n    if not alpha_keys:\n        return {}\n\n    first = consensus_results[alpha_keys[0]]\n    pair_labels = [cl[\"pair_label\"] for cl in first[\"consensus\"][\"classifications\"]]\n\n    pairs_comp = {}\n    for label in pair_labels:\n        row = {\"pair\": label, \"per_alpha\": {}}\n        for ak in alpha_keys:\n            cr = consensus_results[ak]\n            cls = [c for c in cr[\"consensus\"][\"classifications\"] if c[\"pair_label\"] == label]\n            if cls:\n                cl = cls[0]\n                row[\"per_alpha\"][ak] = {\n                    \"alpha\": cr[\"alpha\"],\n                    \"is_robust\": cl[\"is_robust\"],\n                    \"n_sig_methods\": cl[\"n_sig_methods\"],\n                    \"mode\": cr[\"mode\"],\n                }\n        verdicts = [v[\"is_robust\"] for v in row[\"per_alpha\"].values()]\n        row[\"stable\"] = len(set(verdicts)) <= 1\n        row[\"all_robust\"] = all(verdicts) if verdicts else False\n        row[\"all_non_robust\"] = not any(verdicts) if verdicts else True\n        pairs_comp[label] = row\n\n    n_stable = sum(1 for r in pairs_comp.values() if r[\"stable\"])\n    return {\n        \"alpha_keys\": alpha_keys,\n        \"alpha_values\": [consensus_results[ak][\"alpha\"] for ak in alpha_keys],\n        \"n_pairs\": len(pair_labels),\n        \"n_stable\": n_stable,\n        \"n_regime_dependent\": len(pair_labels) - n_stable,\n        \"pairs\": pairs_comp,\n    }\n\n\n# ---------------------------------------------------------------------------\n# 6. Markdown report\n# ---------------------------------------------------------------------------\n\ndef generate_markdown_report(output, out_path):\n    lines = []\n    lines.append(f\"# Cross-Alpha Analysis Report ({output['version']})\")\n    lines.append(\"\")\n    lines.append(f\"**Date:** {output['date']}\")\n    lines.append(f\"**Alpha points:** {output['alpha_points']}\")\n    lines.append(f\"**Generations:** {output['gen_range']}\")\n    lines.append(\"\")\n\n    # 1. Dose-response\n    lines.append(\"## 1. Dose-Response (gen0 to genN drift %)\")\n    lines.append(\"\")\n    dr = output[\"dose_response\"]\n    alphas = sorted(dr.keys())\n    header = \"| Metric |\"\n    sep = \"|--------|\"\n    for ak in alphas:\n        header += f\" α={dr[ak]['alpha']:.2f} |\"\n        sep += \"--------:|\"\n    lines.append(header)\n    lines.append(sep)\n    for metric in METRICS:\n        row = f\"| {metric} |\"\n        for ak in alphas:\n            d = dr[ak][metric][\"drift_pct\"]\n            row += f\" {d:+.1f}% |\"\n        lines.append(row)\n    lines.append(\"\")\n\n    # 2. Granger\n    lines.append(\"## 2. Granger Causality (bidirectional, permutation, FDR-corrected)\")\n    lines.append(\"\")\n    gc = output[\"granger_causality\"]\n    ak_list = sorted(set(r[\"alpha_key\"] for r in gc))\n    header = \"| Direction |\"\n    sep = \"|-----------|\"\n    for ak in ak_list:\n        a = [r for r in gc if r[\"alpha_key\"] == ak][0][\"alpha\"]\n        header += f\" α={a:.2f} p_raw | p_fdr |\"\n        sep += \"--------:|--------:|\"\n    lines.append(header)\n    lines.append(sep)\n    directions = list(dict.fromkeys(r[\"direction\"] for r in gc))\n    for d in directions:\n        row = f\"| {d} |\"\n        for ak in ak_list:\n            match = [r for r in gc if r[\"alpha_key\"] == ak and r[\"direction\"] == d]\n            if match:\n                r = match[0]\n                pr = f\"{r['p_raw']:.4f}\" if r.get(\"p_raw\") is not None else \"N/A\"\n                pf = f\"{r['p_fdr']:.4f}\" if r.get(\"p_fdr\") is not None else \"N/A\"\n                sig = \" *\" if r.get(\"p_fdr\") is not None and r[\"p_fdr\"] < 0.05 else \"\"\n                row += f\" {pr} | {pf}{sig} |\"\n            else:\n                row += \" -- | -- |\"\n        lines.append(row)\n    lines.append(\"\")\n    sc = output[\"statistical_config\"]\n    lines.append(f\"FDR: {sc['n_independent_tests']} tests, BH correction. \\\\* = p_fdr < 0.05\")\n    lines.append(\"\")\n\n    # 3. Consensus per alpha\n    if \"consensus_per_alpha\" in output:\n        lines.append(\"## 3. Consensus Classification (regime-dependent validity)\")\n        lines.append(\"\")\n        cpa = output[\"consensus_per_alpha\"]\n        for ak in sorted(cpa.keys(), key=lambda k: cpa[k][\"alpha\"]):\n            entry = cpa[ak]\n            lines.append(f\"### α={entry['alpha']:.2f} ({entry['note']})\")\n            lines.append(\"\")\n            lines.append(f\"- Robust pairs: {entry['consensus']['n_robust']}/{entry['n_pairs']}\")\n            lines.append(f\"- Non-robust: {entry['consensus']['n_non_robust']}/{entry['n_pairs']}\")\n            lines.append(\"\")\n            lines.append(\"| Pair | Robust | Methods |\")\n            lines.append(\"|------|--------|---------|\")\n            for cl in entry[\"consensus\"][\"classifications\"]:\n                tag = \"**ROBUST**\" if cl[\"is_robust\"] else \"non-robust\"\n                lines.append(f\"| {cl['pair_label']} | {tag} | {cl['n_sig_methods']}/{entry['n_methods']} |\")\n            lines.append(\"\")\n\n        if \"consensus_regime_comparison\" in output:\n            rc = output[\"consensus_regime_comparison\"]\n            lines.append(\"### Regime Comparison Summary\")\n            lines.append(\"\")\n            lines.append(f\"- Stable pairs (same classification at all α): {rc['n_stable']}/{rc['n_pairs']}\")\n            lines.append(f\"- Regime-dependent pairs: {rc['n_regime_dependent']}/{rc['n_pairs']}\")\n            lines.append(\"\")\n            header = \"| Pair |\"\n            sep = \"|------|\"\n            for av in rc[\"alpha_values\"]:\n                header += f\" α={av:.2f} |\"\n                sep += \"--------|\"\n            header += \" Stable |\"\n            sep += \"--------|\"\n            lines.append(header)\n            lines.append(sep)\n            for label, info in rc[\"pairs\"].items():\n                row = f\"| {label} |\"\n                for ak in rc[\"alpha_keys\"]:\n                    if ak in info[\"per_alpha\"]:\n                        v = info[\"per_alpha\"][ak]\n                        tag = f\"R({v['n_sig_methods']})\" if v[\"is_robust\"] else f\".({v['n_sig_methods']})\"\n                        row += f\" {tag} |\"\n                    else:\n                        row += \" - |\"\n                row += f\" {'Y' if info['stable'] else 'N'} |\"\n                lines.append(row)\n            lines.append(\"\")\n\n    # 4. Velocity\n    lines.append(\"## 4. D1 Velocity\")\n    lines.append(\"\")\n    vel = output[\"per_gen_velocity\"]\n    lines.append(\"| α | mean_vel | early | late | decel_ratio |\")\n    lines.append(\"|---|----------|-------|------|-------------|\")\n    for ak in sorted(vel.keys()):\n        v = vel[ak]\n        decel = f\"{v['deceleration_ratio']:.2f}\" if v.get(\"deceleration_ratio\") else \"N/A\"\n        lines.append(f\"| {v['alpha']:.2f} | {v['mean_velocity']:+.6f} | \"\n                     f\"{v['early_mean_velocity']:+.6f} | {v['late_mean_velocity']:+.6f} | {decel} |\")\n    lines.append(\"\")\n\n    with open(out_path, \"w\") as f:\n        f.write(\"\\n\".join(lines))\n    return out_path\n\n\n# ---------------------------------------------------------------------------\n# Output / summary\n# ---------------------------------------------------------------------------\n\ndef auto_version():\n    os.makedirs(ANALYSIS_DIR, exist_ok=True)\n    existing = glob.glob(os.path.join(ANALYSIS_DIR, \"cross_alpha_v*.json\"))\n    max_v = 0\n    for f in existing:\n        m = re.search(r\"cross_alpha_v(\\d+)\", f)\n        if m:\n            max_v = max(max_v, int(m.group(1)))\n    return max_v + 1\n\n\ndef print_summary(output):\n    print(\"\\n\" + \"=\" * 80)\n    print(\"CROSS-ALPHA ANALYSIS SUMMARY (v4)\")\n    print(\"=\" * 80)\n\n    dr = output[\"dose_response\"]\n    alphas = sorted(dr.keys())\n    print(f\"\\nDOSE-RESPONSE (drift %)\")\n    print(\"-\" * 80)\n    header = f\"{'Metric':<16}\"\n    for ak in alphas:\n        header += f\" | a={dr[ak]['alpha']:<5}\"\n    print(header)\n    print(\"-\" * 80)\n    for metric in METRICS:\n        line = f\"{metric:<16}\"\n        for ak in alphas:\n            d = dr[ak][metric][\"drift_pct\"]\n            line += f\" | {d:>+7.1f}%\"\n        print(line)\n\n    gc = output[\"granger_causality\"]\n    print(f\"\\nGRANGER CAUSALITY (bidirectional, differenced, permutation)\")\n    print(\"-\" * 80)\n    header = f\"{'Direction':<20}\"\n    alpha_keys = sorted(set(r[\"alpha_key\"] for r in gc))\n    for ak in alpha_keys:\n        header += f\" | a={[r for r in gc if r['alpha_key']==ak][0]['alpha']:<4} p_raw   p_fdr\"\n    print(header)\n    print(\"-\" * 80)\n\n    directions = list(dict.fromkeys(r[\"direction\"] for r in gc))\n    for d in directions:\n        line = f\"{d:<20}\"\n        for ak in alpha_keys:\n            match = [r for r in gc if r[\"alpha_key\"] == ak and r[\"direction\"] == d]\n            if match:\n                r = match[0]\n                p_raw = f\"{r['p_raw']:.4f}\" if r.get(\"p_raw\") is not None else \"  N/A \"\n                p_fdr = f\"{r.get('p_fdr', 'N/A')}\" if r.get(\"p_fdr\") is not None else \"  N/A \"\n                if isinstance(p_fdr, float):\n                    p_fdr = f\"{p_fdr:.4f}\"\n                sig = \"*\" if r.get(\"p_fdr\") is not None and r[\"p_fdr\"] < 0.05 else \" \"\n                fp = \"FP?\" if r.get(\"note\", \"\").startswith(\"consistent\") else \"   \"\n                line += f\" | {p_raw} {p_fdr:>7} {sig}{fp}\"\n            else:\n                line += f\" |    --       --     \"\n        print(line)\n\n    valid = [r for r in gc if r.get(\"p_raw\") is not None]\n    n_total = len(valid)\n    n_raw_sig = sum(1 for r in valid if r[\"p_raw\"] < 0.05)\n    n_fdr_sig = sum(1 for r in valid if r.get(\"p_fdr\") is not None and r[\"p_fdr\"] < 0.05)\n    print(f\"\\nFDR: {n_raw_sig}/{n_total} raw-sig -> {n_fdr_sig}/{n_total} FDR-sig \"\n          f\"(BH correction across all {n_total} tests)\")\n\n    if \"consensus_per_alpha\" in output:\n        cpa = output[\"consensus_per_alpha\"]\n        print(f\"\\nCONSENSUS CLASSIFICATION PER ALPHA\")\n        print(\"-\" * 80)\n        for ak in sorted(cpa.keys(), key=lambda k: cpa[k][\"alpha\"]):\n            entry = cpa[ak]\n            print(f\"\\n  a={entry['alpha']:.2f} [{entry['note']}]\")\n            print(f\"    Robust: {entry['consensus']['n_robust']}/{entry['n_pairs']}, \"\n                  f\"Non-robust: {entry['consensus']['n_non_robust']}/{entry['n_pairs']}\")\n            for cl in entry[\"consensus\"][\"classifications\"]:\n                if cl[\"is_robust\"]:\n                    print(f\"      ROBUST  {cl['pair_label']:<35s} ({cl['n_sig_methods']}/{entry['n_methods']} methods)\")\n\n        if \"consensus_regime_comparison\" in output:\n            rc = output[\"consensus_regime_comparison\"]\n            print(f\"\\n  REGIME COMPARISON: {rc['n_stable']}/{rc['n_pairs']} stable, \"\n                  f\"{rc['n_regime_dependent']}/{rc['n_pairs']} regime-dependent\")\n            changed = [l for l, p in rc[\"pairs\"].items() if not p[\"stable\"]]\n            if changed:\n                print(f\"    Regime-dependent pairs:\")\n                for label in changed:\n                    info = rc[\"pairs\"][label]\n                    tags = []\n                    for ak in rc[\"alpha_keys\"]:\n                        if ak in info[\"per_alpha\"]:\n                            v = info[\"per_alpha\"][ak]\n                            t = \"R\" if v[\"is_robust\"] else \".\"\n                            tags.append(f\"a={v['alpha']:.2f}:{t}\")\n                    print(f\"      {label:<35s} {' '.join(tags)}\")\n\n    xcorr = output[\"cross_correlation\"]\n    print(f\"\\nCROSS-CORRELATION (delta-metric, peak lag)\")\n    print(\"-\" * 60)\n    for pair_label in [\"entropy_vs_d1\", \"ece_vs_d1\"]:\n        line = f\"  {pair_label:<18}\"\n        for ak in sorted(xcorr.keys()):\n            p = xcorr[ak].get(pair_label, {})\n            line += f\" | a={xcorr[ak]['alpha']}: lag={p.get('peak_lag','?'):>2} r={p.get('peak_r','?'):>7}\"\n        print(line)\n\n    vel = output[\"per_gen_velocity\"]\n    print(f\"\\nD1 VELOCITY\")\n    print(\"-\" * 60)\n    for ak in sorted(vel.keys()):\n        v = vel[ak]\n        decel = f\"{v['deceleration_ratio']:.2f}\" if v.get(\"deceleration_ratio\") is not None else \"N/A\"\n        print(f\"  a={v['alpha']}: mean_vel={v['mean_velocity']:+.6f}  \"\n              f\"early={v['early_mean_velocity']:+.6f}  late={v['late_mean_velocity']:+.6f}  \"\n              f\"decel_ratio={decel}  max_drop=gen{v['max_drop_gen']}\")\n\n    print()\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Cross-alpha analysis v4 with per-alpha consensus classification.\"\n    )\n    parser.add_argument(\"--alpha-dirs\", nargs=\"*\", default=None,\n                        help=\"Specific alpha dirs (e.g. a000_s42 a025_s42 mvp). Default: auto-discover all.\")\n    parser.add_argument(\"--n-perms\", type=int, default=5000,\n                        help=\"Permutations for Granger test (default: 5000)\")\n    parser.add_argument(\"--consensus-n-perms\", type=int, default=1000,\n                        help=\"Permutations for consensus perm_granger method (default: 1000)\")\n    parser.add_argument(\"--max-lag\", type=int, default=1,\n                        help=\"Max lag for Granger test (default: 1)\")\n    parser.add_argument(\"--no-mvp\", action=\"store_true\",\n                        help=\"Exclude MVP (alpha=1.0) from auto-discovery\")\n    parser.add_argument(\"--no-consensus\", action=\"store_true\",\n                        help=\"Skip consensus classification (faster)\")\n    parser.add_argument(\"--version\", type=int, default=None,\n                        help=\"Output version number (default: auto-increment)\")\n    parser.add_argument(\"--update-registry\", action=\"store_true\",\n                        help=\"Print registry update commands after analysis\")\n    args = parser.parse_args()\n\n    alpha_dirs = discover_alpha_dirs(args.alpha_dirs, include_mvp=not args.no_mvp)\n    if not alpha_dirs:\n        print(\"ERROR: No alpha directories found.\", file=sys.stderr)\n        sys.exit(1)\n\n    print(f\"Found {len(alpha_dirs)} alpha points: \"\n          f\"{[(a[0], f'seeds={a[3]}') for a in alpha_dirs]}\")\n\n    all_data = []\n    for alpha_key, alpha_val, path, seeds in alpha_dirs:\n        metrics = load_metrics(path)\n        print(f\"  {alpha_key} (a={alpha_val}): {len(metrics)} generations, seeds={seeds}\")\n        all_data.append((alpha_key, alpha_val, metrics))\n\n    # 1. Dose-response\n    dose_resp = compute_dose_response(all_data)\n\n    # 2. Granger\n    print(f\"\\nRunning bidirectional Granger ({len(GRANGER_PAIRS)} pairs x {len(all_data)} alphas, \"\n          f\"n_perms={args.n_perms})...\")\n    granger = run_granger_all(all_data, max_lag=args.max_lag, n_perms=args.n_perms)\n    granger = apply_fdr(granger)\n\n    # 3. Cross-correlation\n    xcorr = cross_correlation(all_data)\n\n    # 4. Velocity\n    velocity = per_gen_velocity(all_data)\n\n    # Assemble output\n    version = args.version or auto_version()\n    n_gens = len(all_data[0][2]) if all_data else 0\n    output = {\n        \"version\": f\"v{version}\",\n        \"date\": datetime.now().strftime(\"%Y-%m-%d\"),\n        \"n_alphas\": len(all_data),\n        \"alpha_points\": [a[1] for a in all_data],\n        \"n_generations\": n_gens,\n        \"gen_range\": f\"gen_0 to gen_{n_gens - 1}\" if n_gens else \"N/A\",\n        \"statistical_config\": {\n            \"granger_max_lag\": args.max_lag,\n            \"granger_n_perm\": args.n_perms,\n            \"granger_differenced\": True,\n            \"fdr_method\": \"benjamini-hochberg\",\n            \"fdr_scope\": f\"all {len(granger)} tests corrected together\",\n            \"n_independent_tests\": len([r for r in granger if r.get(\"p_raw\") is not None]),\n        },\n        \"dose_response\": dose_resp,\n        \"granger_causality\": granger,\n        \"cross_correlation\": xcorr,\n        \"per_gen_velocity\": velocity,\n    }\n\n    # 5. Consensus per alpha\n    if not args.no_consensus:\n        mvp_ablation = os.path.join(MVP_DIR, \"analysis\", \"method_ablation.json\")\n        print(f\"\\nRunning per-alpha consensus classification \"\n              f\"(5 methods x 16 pairs x {len(alpha_dirs)} alphas)...\")\n        consensus_results = run_consensus_per_alpha(\n            alpha_dirs, mvp_ablation_path=mvp_ablation,\n            consensus_n_perm=args.consensus_n_perms)\n        output[\"consensus_per_alpha\"] = consensus_results\n        output[\"consensus_regime_comparison\"] = consensus_regime_comparison(consensus_results)\n\n    # Save JSON\n    os.makedirs(ANALYSIS_DIR, exist_ok=True)\n    json_path = os.path.join(ANALYSIS_DIR, f\"cross_alpha_v{version}.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2, ensure_ascii=False, cls=NumpyEncoder)\n\n    # Save Markdown report\n    md_path = os.path.join(ANALYSIS_DIR, f\"cross_alpha_v{version}_report.md\")\n    generate_markdown_report(output, md_path)\n\n    print_summary(output)\n    print(f\"\\nSaved: {json_path}\")\n    print(f\"Report: {md_path}\")\n\n    if args.update_registry:\n        print(\"\\n--- Registry update commands ---\")\n        for alpha_key, alpha_val, _ in all_data:\n            dr = dose_resp[alpha_key]\n            print(f\"# {alpha_key}: d1_drift={dr['distinct_1']['drift_pct']}%, \"\n                  f\"entropy_drift={dr['token_entropy']['drift_pct']}%, \"\n                  f\"ece_drift={dr['ece']['drift_pct']}%\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"DEPLOY_STATUS: $?\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat > /root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py << 'SCRIPT_EOF'\n\"\"\"Cross-alpha analysis v4 with per-alpha consensus classification.\n\nExtends v3 with:\n  5. Per-alpha multi-method consensus classification (regime-dependent validity)\n  6. Markdown report output\n\nHandles mixed data paths:\n  - alpha-sweep: results/alpha_sweep/a{NNN}_s42/all_metrics.json (single seed)\n  - alpha=1.0:   results/mvp/rep_{42..45}/all_metrics.json (4 seeds)\n  - alpha=1.0 consensus loads existing method_ablation.json\n  - Single-seed alpha points: seed_threshold=1, method agreement only\n\nDependencies: numpy, scipy, statsmodels\n\"\"\"\n\nimport argparse\nimport glob\nimport json\nimport os\nimport re\nimport sys\nimport warnings\nfrom datetime import datetime\n\nimport numpy as np\nfrom statsmodels.stats.multitest import multipletests\n\nwarnings.filterwarnings(\"ignore\")\n\nBASE_DIR = os.path.dirname(os.path.abspath(__file__))\nsys.path.insert(0, BASE_DIR)\n\nfrom method_ablation import (\n    CANARY, DOWNSTREAM,\n    extract as ma_extract,\n    naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto, perm_granger,\n)\nfrom consensus_framework import classify_robust, load_sig_matrix, NumpyEncoder\n\nSWEEP_DIR = os.path.join(BASE_DIR, \"results\", \"alpha_sweep\")\nMVP_DIR = os.path.join(BASE_DIR, \"results\", \"mvp\")\nANALYSIS_DIR = os.path.join(BASE_DIR, \"results\", \"analysis\")\n\nMETRICS = [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"token_entropy\", \"ece\", \"perplexity\"]\n\nGRANGER_PAIRS = [\n    (\"token_entropy\", \"distinct_1\", \"entropy->d1\"),\n    (\"ece\",           \"distinct_1\", \"ECE->d1\"),\n    (\"token_entropy\", \"distinct_2\", \"entropy->d2\"),\n    (\"ece\",           \"distinct_2\", \"ECE->d2\"),\n    (\"distinct_1\", \"token_entropy\", \"d1->entropy\"),\n    (\"distinct_1\", \"ece\",           \"d1->ECE\"),\n    (\"distinct_2\", \"token_entropy\", \"d2->entropy\"),\n    (\"distinct_2\", \"ece\",           \"d2->ECE\"),\n]\n\nXCORR_PAIRS = [\n    (\"token_entropy\", \"distinct_1\", \"entropy_vs_d1\"),\n    (\"ece\",           \"distinct_1\", \"ece_vs_d1\"),\n]\n\nMA_METHODS = [\"naive_pearson\", \"differenced_xcorr\", \"threshold_onset\",\n              \"toda_yamamoto\", \"permutation_granger\"]\nMA_METHOD_FN = {\n    \"naive_pearson\": naive_pearson,\n    \"differenced_xcorr\": diff_xcorr,\n    \"threshold_onset\": threshold_lead,\n    \"toda_yamamoto\": toda_yamamoto,\n    \"permutation_granger\": perm_granger,\n}\n\n\n# ---------------------------------------------------------------------------\n# Data loading (extended for MVP alpha=1.0)\n# ---------------------------------------------------------------------------\n\ndef _find_mvp_seeds():\n    seeds = []\n    if not os.path.isdir(MVP_DIR):\n        return seeds\n    for d in sorted(os.listdir(MVP_DIR)):\n        m = re.match(r\"rep_(\\d+)$\", d)\n        if m and os.path.isfile(os.path.join(MVP_DIR, d, \"all_metrics.json\")):\n            seeds.append(int(m.group(1)))\n    return sorted(seeds)\n\n\ndef discover_alpha_dirs(explicit=None, include_mvp=True):\n    \"\"\"Find alpha directories.\n\n    Returns sorted list of (alpha_key, alpha_float, path, seeds).\n    \"\"\"\n    dirs = []\n\n    if explicit:\n        for name in explicit:\n            if name in (\"mvp\", \"a100_mvp\"):\n                rep42 = os.path.join(MVP_DIR, \"rep_42\")\n                if os.path.isdir(rep42):\n                    dirs.append((\"a100\", 1.0, rep42, _find_mvp_seeds()))\n                continue\n            path = os.path.join(SWEEP_DIR, name)\n            if not os.path.isdir(path):\n                print(f\"WARNING: {path} not found, skipping\", file=sys.stderr)\n                continue\n            m = re.match(r\"a(\\d{3})_s(\\d+)\", name)\n            if m:\n                alpha_val = int(m.group(1)) / 100.0\n                dirs.append((f\"a{m.group(1)}\", alpha_val, path, [int(m.group(2))]))\n    else:\n        pattern = os.path.join(SWEEP_DIR, \"a*_s42\")\n        for path in sorted(glob.glob(pattern)):\n            name = os.path.basename(path)\n            m = re.match(r\"a(\\d{3})_s42\", name)\n            if m:\n                alpha_val = int(m.group(1)) / 100.0\n                dirs.append((f\"a{m.group(1)}\", alpha_val, path, [42]))\n\n        if include_mvp and not any(d[1] == 1.0 for d in dirs):\n            rep42 = os.path.join(MVP_DIR, \"rep_42\")\n            if os.path.isdir(rep42):\n                dirs.append((\"a100\", 1.0, rep42, _find_mvp_seeds()))\n\n    return sorted(dirs, key=lambda x: x[1])\n\n\ndef load_metrics(alpha_dir):\n    path = os.path.join(alpha_dir, \"all_metrics.json\")\n    with open(path) as f:\n        data = json.load(f)\n    return sorted(data, key=lambda x: x[\"generation\"])\n\n\ndef load_all_seeds_metrics(alpha_val, primary_dir, seeds):\n    \"\"\"Load metrics for all seeds. Returns list of (seed, metrics_list).\"\"\"\n    results = []\n    for seed in seeds:\n        if alpha_val == 1.0:\n            path = os.path.join(MVP_DIR, f\"rep_{seed}\")\n        else:\n            path = primary_dir\n        mpath = os.path.join(path, \"all_metrics.json\")\n        if os.path.isfile(mpath):\n            results.append((seed, load_metrics(path)))\n    return results\n\n\ndef extract_series(metrics_list, key):\n    return np.array([m[key] for m in metrics_list], dtype=float)\n\n\n# ---------------------------------------------------------------------------\n# 1. Dose-response\n# ---------------------------------------------------------------------------\n\ndef compute_dose_response(all_data):\n    result = {}\n    for alpha_key, alpha_val, metrics_list in all_data:\n        entry = {\"alpha\": alpha_val}\n        for metric in METRICS:\n            vals = extract_series(metrics_list, metric)\n            gen0, genN = vals[0], vals[-1]\n            drift_pct = round((genN - gen0) / abs(gen0) * 100, 2) if abs(gen0) > 1e-12 else 0.0\n            entry[metric] = {\n                \"gen0\": round(float(gen0), 6),\n                f\"gen{len(vals)-1}\": round(float(genN), 6),\n                \"drift_pct\": drift_pct,\n            }\n        result[alpha_key] = entry\n    return result\n\n\n# ---------------------------------------------------------------------------\n# 2. Permutation Granger causality\n# ---------------------------------------------------------------------------\n\ndef _build_lag_matrix(y, x, max_lag):\n    T = len(y)\n    n = T - max_lag\n    Y = y[max_lag:]\n    cols_r = [np.ones(n)]\n    for lag in range(1, max_lag + 1):\n        cols_r.append(y[max_lag - lag: T - lag])\n    cols_u = list(cols_r)\n    for lag in range(1, max_lag + 1):\n        cols_u.append(x[max_lag - lag: T - lag])\n    return Y, np.column_stack(cols_r), np.column_stack(cols_u)\n\n\ndef _granger_f_stat(y, x, max_lag):\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\n    n = len(Y)\n    q = max_lag\n    try:\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\n    except np.linalg.LinAlgError:\n        return np.nan\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\n    k_u = X_u.shape[1]\n    df_resid = n - k_u\n    if df_resid <= 0 or rss_u < 1e-15:\n        return np.nan\n    return ((rss_r - rss_u) / q) / (rss_u / df_resid)\n\n\ndef permutation_granger_test(x, y, max_lag=1, n_perm=5000, seed=42, difference=True):\n    x = np.asarray(x, dtype=float)\n    y = np.asarray(y, dtype=float)\n    if difference:\n        x, y = np.diff(x), np.diff(y)\n    T = len(x)\n    if T <= max_lag + 2:\n        return {\"f_stat\": None, \"p_raw\": None, \"note\": f\"Series too short: T={T}\"}\n\n    f_obs = _granger_f_stat(y, x, max_lag)\n    if np.isnan(f_obs):\n        return {\"f_stat\": None, \"p_raw\": None, \"note\": \"F-stat computation failed\"}\n\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\n    rss_r = np.sum((Y - X_r @ np.linalg.lstsq(X_r, Y, rcond=None)[0]) ** 2)\n    rss_u = np.sum((Y - X_u @ np.linalg.lstsq(X_u, Y, rcond=None)[0]) ** 2)\n    f2 = (rss_r - rss_u) / rss_u if rss_u > 1e-15 else None\n\n    rng = np.random.default_rng(seed)\n    null_f = np.empty(n_perm)\n    for i in range(n_perm):\n        null_f[i] = _granger_f_stat(y, rng.permutation(x), max_lag)\n    valid = null_f[~np.isnan(null_f)]\n    if len(valid) == 0:\n        return {\"f_stat\": round(float(f_obs), 4), \"p_raw\": None, \"note\": \"All permutations failed\"}\n\n    p_value = (np.sum(valid >= f_obs) + 1) / (len(valid) + 1)\n    return {\n        \"f_stat\": round(float(f_obs), 4),\n        \"p_raw\": round(float(p_value), 6),\n        \"n_perm\": n_perm,\n        \"effect_size_f2\": round(float(f2), 4) if f2 is not None else None,\n    }\n\n\ndef run_granger_all(all_data, max_lag=1, n_perms=5000):\n    results = []\n    for alpha_key, alpha_val, metrics_list in all_data:\n        for cause_key, effect_key, label in GRANGER_PAIRS:\n            x = extract_series(metrics_list, cause_key)\n            y = extract_series(metrics_list, effect_key)\n            res = permutation_granger_test(x, y, max_lag=max_lag, n_perm=n_perms)\n            res.update({\n                \"alpha\": alpha_val,\n                \"alpha_key\": alpha_key,\n                \"direction\": label,\n                \"cause\": cause_key,\n                \"effect\": effect_key,\n            })\n            results.append(res)\n    return results\n\n\ndef apply_fdr(granger_results):\n    valid_idx = [i for i, r in enumerate(granger_results) if r.get(\"p_raw\") is not None]\n    if not valid_idx:\n        return granger_results\n\n    raw_ps = [granger_results[i][\"p_raw\"] for i in valid_idx]\n    _, fdr_ps, _, _ = multipletests(raw_ps, method=\"fdr_bh\")\n\n    for j, idx in enumerate(valid_idx):\n        granger_results[idx][\"p_fdr\"] = round(float(fdr_ps[j]), 6)\n\n    for r in granger_results:\n        if r.get(\"alpha\", -1) == 0.0 and r.get(\"p_raw\") is not None and r[\"p_raw\"] < 0.05:\n            r[\"note\"] = \"consistent with FPR, likely false positive\"\n\n    return granger_results\n\n\n# ---------------------------------------------------------------------------\n# 3. Cross-correlation lead-lag\n# ---------------------------------------------------------------------------\n\ndef cross_correlation(all_data, max_lag=3):\n    result = {}\n    for alpha_key, alpha_val, metrics_list in all_data:\n        entry = {\"alpha\": alpha_val}\n        for cause_key, effect_key, pair_label in XCORR_PAIRS:\n            dx = np.diff(extract_series(metrics_list, cause_key))\n            dy = np.diff(extract_series(metrics_list, effect_key))\n            lags = {}\n            best_lag, best_r = 0, 0.0\n            for lag in range(-max_lag, max_lag + 1):\n                if lag >= 0:\n                    a, b = dx[:len(dx) - lag] if lag > 0 else dx, dy[lag:] if lag > 0 else dy\n                else:\n                    a, b = dx[-lag:], dy[:len(dy) + lag]\n                n = min(len(a), len(b))\n                if n < 3:\n                    continue\n                a, b = a[:n], b[:n]\n                std_a, std_b = np.std(a, ddof=1), np.std(b, ddof=1)\n                if std_a < 1e-15 or std_b < 1e-15:\n                    r = 0.0\n                else:\n                    r = float(np.corrcoef(a, b)[0, 1])\n                lags[str(lag)] = round(r, 4)\n                if abs(r) > abs(best_r):\n                    best_lag, best_r = lag, r\n            entry[pair_label] = {\n                \"peak_lag\": best_lag,\n                \"peak_r\": round(best_r, 4),\n                \"lags\": lags,\n            }\n        result[alpha_key] = entry\n    return result\n\n\n# ---------------------------------------------------------------------------\n# 4. Per-gen velocity\n# ---------------------------------------------------------------------------\n\ndef per_gen_velocity(all_data):\n    result = {}\n    for alpha_key, alpha_val, metrics_list in all_data:\n        vals = extract_series(metrics_list, \"distinct_1\")\n        deltas = np.diff(vals)\n        n = len(deltas)\n        mid = n // 2\n        early_mean = float(np.mean(deltas[:mid])) if mid > 0 else None\n        late_mean = float(np.mean(deltas[mid:])) if mid < n else None\n        max_drop_idx = int(np.argmin(deltas))\n        result[alpha_key] = {\n            \"alpha\": alpha_val,\n            \"d1_values\": [round(float(v), 6) for v in vals],\n            \"d1_deltas\": [round(float(d), 6) for d in deltas],\n            \"cumulative_drift_pct\": round((vals[-1] - vals[0]) / abs(vals[0]) * 100, 2),\n            \"mean_velocity\": round(float(np.mean(deltas)), 6),\n            \"max_drop_gen\": max_drop_idx,\n            \"max_drop_value\": round(float(deltas[max_drop_idx]), 6),\n            \"early_mean_velocity\": round(early_mean, 6) if early_mean is not None else None,\n            \"late_mean_velocity\": round(late_mean, 6) if late_mean is not None else None,\n            \"deceleration_ratio\": round(late_mean / early_mean, 4) if early_mean and abs(early_mean) > 1e-12 else None,\n        }\n    return result\n\n\n# ---------------------------------------------------------------------------\n# 5. Per-alpha consensus classification\n# ---------------------------------------------------------------------------\n\ndef run_consensus_per_alpha(alpha_dirs, mvp_ablation_path=None, consensus_n_perm=1000):\n    \"\"\"Run 5-method consensus classification at each alpha point.\n\n    alpha=1.0 with existing method_ablation.json: load directly (4 seeds).\n    Other alpha points: run 5 methods on single-seed data, seed_threshold=1.\n    \"\"\"\n    results = {}\n\n    for alpha_key, alpha_val, primary_dir, seeds in alpha_dirs:\n        # alpha=1.0: use existing method_ablation.json\n        if alpha_val == 1.0 and mvp_ablation_path and os.path.isfile(mvp_ablation_path):\n            sig, pair_names, method_names, ab_seeds = load_sig_matrix(mvp_ablation_path)\n            n_m, n_p, n_s = sig.shape\n            mt = n_m - 1  # 4/5\n            st = 3        # 3/4 seeds\n            consensus = classify_robust(sig, mt, st)\n\n            for cl in consensus[\"classifications\"]:\n                pi = cl[\"pair_index\"]\n                cl[\"canary\"] = pair_names[pi][0]\n                cl[\"downstream\"] = pair_names[pi][1]\n                cl[\"pair_label\"] = f\"{pair_names[pi][0]}→{pair_names[pi][1]}\"\n\n            results[alpha_key] = {\n                \"alpha\": alpha_val,\n                \"n_seeds\": n_s,\n                \"seeds\": ab_seeds,\n                \"mode\": \"full_consensus\",\n                \"note\": f\"{n_s}-seed full consensus (≥{mt}/{n_m} methods, ≥{st}/{n_s} seeds)\",\n                \"method_threshold\": mt,\n                \"seed_threshold\": st,\n                \"n_methods\": n_m,\n                \"n_pairs\": n_p,\n                \"consensus\": consensus,\n                \"pair_names\": [list(p) for p in pair_names],\n            }\n            continue\n\n        # Other alpha points: run 5 methods from scratch\n        seed_data = load_all_seeds_metrics(alpha_val, primary_dir, seeds)\n        n_seeds = len(seed_data)\n        n_pairs = len(CANARY) * len(DOWNSTREAM)\n        n_methods = len(MA_METHODS)\n\n        sig_matrix = np.zeros((n_methods, n_pairs, n_seeds), dtype=bool)\n        pair_names = []\n\n        for si, (seed, metrics_list) in enumerate(seed_data):\n            pi = 0\n            for cn in CANARY:\n                c = ma_extract(metrics_list, cn)\n                for dn in DOWNSTREAM:\n                    if si == 0:\n                        pair_names.append((cn, dn))\n                    d = ma_extract(metrics_list, dn)\n                    for mi, method_name in enumerate(MA_METHODS):\n                        fn = MA_METHOD_FN[method_name]\n                        try:\n                            if method_name == \"permutation_granger\":\n                                res = fn(c, d, cn, dn, n_perm=consensus_n_perm)\n                            else:\n                                res = fn(c, d, cn, dn)\n                            sig_matrix[mi, pi, si] = res.get(\"significant\", False)\n                        except Exception:\n                            sig_matrix[mi, pi, si] = False\n                    pi += 1\n\n        st = 1 if n_seeds == 1 else 3\n        mt = n_methods - 1  # 4/5\n\n        consensus = classify_robust(sig_matrix, mt, st)\n        for cl in consensus[\"classifications\"]:\n            pi = cl[\"pair_index\"]\n            cl[\"canary\"] = pair_names[pi][0]\n            cl[\"downstream\"] = pair_names[pi][1]\n            cl[\"pair_label\"] = f\"{pair_names[pi][0]}→{pair_names[pi][1]}\"\n\n        mode = \"method_agreement_only\" if n_seeds == 1 else \"full_consensus\"\n        note_prefix = \"single-seed, method agreement only\" if n_seeds == 1 else f\"{n_seeds}-seed full consensus\"\n\n        results[alpha_key] = {\n            \"alpha\": alpha_val,\n            \"n_seeds\": n_seeds,\n            \"seeds\": [s for s, _ in seed_data],\n            \"mode\": mode,\n            \"note\": f\"{note_prefix} (≥{mt}/{n_methods} methods, ≥{st}/{n_seeds} seeds)\",\n            \"method_threshold\": mt,\n            \"seed_threshold\": st,\n            \"n_methods\": n_methods,\n            \"n_pairs\": n_pairs,\n            \"consensus\": consensus,\n            \"pair_names\": [list(p) for p in pair_names],\n        }\n\n    return results\n\n\ndef consensus_regime_comparison(consensus_results):\n    \"\"\"Compare robust/non-robust classifications across alpha points.\"\"\"\n    alpha_keys = sorted(consensus_results.keys(),\n                        key=lambda k: consensus_results[k][\"alpha\"])\n    if not alpha_keys:\n        return {}\n\n    first = consensus_results[alpha_keys[0]]\n    pair_labels = [cl[\"pair_label\"] for cl in first[\"consensus\"][\"classifications\"]]\n\n    pairs_comp = {}\n    for label in pair_labels:\n        row = {\"pair\": label, \"per_alpha\": {}}\n        for ak in alpha_keys:\n            cr = consensus_results[ak]\n            cls = [c for c in cr[\"consensus\"][\"classifications\"] if c[\"pair_label\"] == label]\n            if cls:\n                cl = cls[0]\n                row[\"per_alpha\"][ak] = {\n                    \"alpha\": cr[\"alpha\"],\n                    \"is_robust\": cl[\"is_robust\"],\n                    \"n_sig_methods\": cl[\"n_sig_methods\"],\n                    \"mode\": cr[\"mode\"],\n                }\n        verdicts = [v[\"is_robust\"] for v in row[\"per_alpha\"].values()]\n        row[\"stable\"] = len(set(verdicts)) <= 1\n        row[\"all_robust\"] = all(verdicts) if verdicts else False\n        row[\"all_non_robust\"] = not any(verdicts) if verdicts else True\n        pairs_comp[label] = row\n\n    n_stable = sum(1 for r in pairs_comp.values() if r[\"stable\"])\n    return {\n        \"alpha_keys\": alpha_keys,\n        \"alpha_values\": [consensus_results[ak][\"alpha\"] for ak in alpha_keys],\n        \"n_pairs\": len(pair_labels),\n        \"n_stable\": n_stable,\n        \"n_regime_dependent\": len(pair_labels) - n_stable,\n        \"pairs\": pairs_comp,\n    }\n\n\n# ---------------------------------------------------------------------------\n# 6. Markdown report\n# ---------------------------------------------------------------------------\n\ndef generate_markdown_report(output, out_path):\n    lines = []\n    lines.append(f\"# Cross-Alpha Analysis Report ({output['version']})\")\n    lines.append(\"\")\n    lines.append(f\"**Date:** {output['date']}\")\n    lines.append(f\"**Alpha points:** {output['alpha_points']}\")\n    lines.append(f\"**Generations:** {output['gen_range']}\")\n    lines.append(\"\")\n\n    # 1. Dose-response\n    lines.append(\"## 1. Dose-Response (gen0 to genN drift %)\")\n    lines.append(\"\")\n    dr = output[\"dose_response\"]\n    alphas = sorted(dr.keys())\n    header = \"| Metric |\"\n    sep = \"|--------|\"\n    for ak in alphas:\n        header += f\" α={dr[ak]['alpha']:.2f} |\"\n        sep += \"--------:|\"\n    lines.append(header)\n    lines.append(sep)\n    for metric in METRICS:\n        row = f\"| {metric} |\"\n        for ak in alphas:\n            d = dr[ak][metric][\"drift_pct\"]\n            row += f\" {d:+.1f}% |\"\n        lines.append(row)\n    lines.append(\"\")\n\n    # 2. Granger\n    lines.append(\"## 2. Granger Causality (bidirectional, permutation, FDR-corrected)\")\n    lines.append(\"\")\n    gc = output[\"granger_causality\"]\n    ak_list = sorted(set(r[\"alpha_key\"] for r in gc))\n    header = \"| Direction |\"\n    sep = \"|-----------|\"\n    for ak in ak_list:\n        a = [r for r in gc if r[\"alpha_key\"] == ak][0][\"alpha\"]\n        header += f\" α={a:.2f} p_raw | p_fdr |\"\n        sep += \"--------:|--------:|\"\n    lines.append(header)\n    lines.append(sep)\n    directions = list(dict.fromkeys(r[\"direction\"] for r in gc))\n    for d in directions:\n        row = f\"| {d} |\"\n        for ak in ak_list:\n            match = [r for r in gc if r[\"alpha_key\"] == ak and r[\"direction\"] == d]\n            if match:\n                r = match[0]\n                pr = f\"{r['p_raw']:.4f}\" if r.get(\"p_raw\") is not None else \"N/A\"\n                pf = f\"{r['p_fdr']:.4f}\" if r.get(\"p_fdr\") is not None else \"N/A\"\n                sig = \" *\" if r.get(\"p_fdr\") is not None and r[\"p_fdr\"] < 0.05 else \"\"\n                row += f\" {pr} | {pf}{sig} |\"\n            else:\n                row += \" -- | -- |\"\n        lines.append(row)\n    lines.append(\"\")\n    sc = output[\"statistical_config\"]\n    lines.append(f\"FDR: {sc['n_independent_tests']} tests, BH correction. \\\\* = p_fdr < 0.05\")\n    lines.append(\"\")\n\n    # 3. Consensus per alpha\n    if \"consensus_per_alpha\" in output:\n        lines.append(\"## 3. Consensus Classification (regime-dependent validity)\")\n        lines.append(\"\")\n        cpa = output[\"consensus_per_alpha\"]\n        for ak in sorted(cpa.keys(), key=lambda k: cpa[k][\"alpha\"]):\n            entry = cpa[ak]\n            lines.append(f\"### α={entry['alpha']:.2f} ({entry['note']})\")\n            lines.append(\"\")\n            lines.append(f\"- Robust pairs: {entry['consensus']['n_robust']}/{entry['n_pairs']}\")\n            lines.append(f\"- Non-robust: {entry['consensus']['n_non_robust']}/{entry['n_pairs']}\")\n            lines.append(\"\")\n            lines.append(\"| Pair | Robust | Methods |\")\n            lines.append(\"|------|--------|---------|\")\n            for cl in entry[\"consensus\"][\"classifications\"]:\n                tag = \"**ROBUST**\" if cl[\"is_robust\"] else \"non-robust\"\n                lines.append(f\"| {cl['pair_label']} | {tag} | {cl['n_sig_methods']}/{entry['n_methods']} |\")\n            lines.append(\"\")\n\n        if \"consensus_regime_comparison\" in output:\n            rc = output[\"consensus_regime_comparison\"]\n            lines.append(\"### Regime Comparison Summary\")\n            lines.append(\"\")\n            lines.append(f\"- Stable pairs (same classification at all α): {rc['n_stable']}/{rc['n_pairs']}\")\n            lines.append(f\"- Regime-dependent pairs: {rc['n_regime_dependent']}/{rc['n_pairs']}\")\n            lines.append(\"\")\n            header = \"| Pair |\"\n            sep = \"|------|\"\n            for av in rc[\"alpha_values\"]:\n                header += f\" α={av:.2f} |\"\n                sep += \"--------|\"\n            header += \" Stable |\"\n            sep += \"--------|\"\n            lines.append(header)\n            lines.append(sep)\n            for label, info in rc[\"pairs\"].items():\n                row = f\"| {label} |\"\n                for ak in rc[\"alpha_keys\"]:\n                    if ak in info[\"per_alpha\"]:\n                        v = info[\"per_alpha\"][ak]\n                        tag = f\"R({v['n_sig_methods']})\" if v[\"is_robust\"] else f\".({v['n_sig_methods']})\"\n                        row += f\" {tag} |\"\n                    else:\n                        row += \" - |\"\n                row += f\" {'Y' if info['stable'] else 'N'} |\"\n                lines.append(row)\n            lines.append(\"\")\n\n    # 4. Velocity\n    lines.append(\"## 4. D1 Velocity\")\n    lines.append(\"\")\n    vel = output[\"per_gen_velocity\"]\n    lines.append(\"| α | mean_vel | early | late | decel_ratio |\")\n    lines.append(\"|---|----------|-------|------|-------------|\")\n    for ak in sorted(vel.keys()):\n        v = vel[ak]\n        decel = f\"{v['deceleration_ratio']:.2f}\" if v.get(\"deceleration_ratio\") else \"N/A\"\n        lines.append(f\"| {v['alpha']:.2f} | {v['mean_velocity']:+.6f} | \"\n                     f\"{v['early_mean_velocity']:+.6f} | {v['late_mean_velocity']:+.6f} | {decel} |\")\n    lines.append(\"\")\n\n    with open(out_path, \"w\") as f:\n        f.write(\"\\n\".join(lines))\n    return out_path\n\n\n# ---------------------------------------------------------------------------\n# Output / summary\n# ---------------------------------------------------------------------------\n\ndef auto_version():\n    os.makedirs(ANALYSIS_DIR, exist_ok=True)\n    existing = glob.glob(os.path.join(ANALYSIS_DIR, \"cross_alpha_v*.json\"))\n    max_v = 0\n    for f in existing:\n        m = re.search(r\"cross_alpha_v(\\d+)\", f)\n        if m:\n            max_v = max(max_v, int(m.group(1)))\n    return max_v + 1\n\n\ndef print_summary(output):\n    print(\"\\n\" + \"=\" * 80)\n    print(\"CROSS-ALPHA ANALYSIS SUMMARY (v4)\")\n    print(\"=\" * 80)\n\n    dr = output[\"dose_response\"]\n    alphas = sorted(dr.keys())\n    print(f\"\\nDOSE-RESPONSE (drift %)\")\n    print(\"-\" * 80)\n    header = f\"{'Metric':<16}\"\n    for ak in alphas:\n        header += f\" | a={dr[ak]['alpha']:<5}\"\n    print(header)\n    print(\"-\" * 80)\n    for metric in METRICS:\n        line = f\"{metric:<16}\"\n        for ak in alphas:\n            d = dr[ak][metric][\"drift_pct\"]\n            line += f\" | {d:>+7.1f}%\"\n        print(line)\n\n    gc = output[\"granger_causality\"]\n    print(f\"\\nGRANGER CAUSALITY (bidirectional, differenced, permutation)\")\n    print(\"-\" * 80)\n    header = f\"{'Direction':<20}\"\n    alpha_keys = sorted(set(r[\"alpha_key\"] for r in gc))\n    for ak in alpha_keys:\n        header += f\" | a={[r for r in gc if r['alpha_key']==ak][0]['alpha']:<4} p_raw   p_fdr\"\n    print(header)\n    print(\"-\" * 80)\n\n    directions = list(dict.fromkeys(r[\"direction\"] for r in gc))\n    for d in directions:\n        line = f\"{d:<20}\"\n        for ak in alpha_keys:\n            match = [r for r in gc if r[\"alpha_key\"] == ak and r[\"direction\"] == d]\n            if match:\n                r = match[0]\n                p_raw = f\"{r['p_raw']:.4f}\" if r.get(\"p_raw\") is not None else \"  N/A \"\n                p_fdr = f\"{r.get('p_fdr', 'N/A')}\" if r.get(\"p_fdr\") is not None else \"  N/A \"\n                if isinstance(p_fdr, float):\n                    p_fdr = f\"{p_fdr:.4f}\"\n                sig = \"*\" if r.get(\"p_fdr\") is not None and r[\"p_fdr\"] < 0.05 else \" \"\n                fp = \"FP?\" if r.get(\"note\", \"\").startswith(\"consistent\") else \"   \"\n                line += f\" | {p_raw} {p_fdr:>7} {sig}{fp}\"\n            else:\n                line += f\" |    --       --     \"\n        print(line)\n\n    valid = [r for r in gc if r.get(\"p_raw\") is not None]\n    n_total = len(valid)\n    n_raw_sig = sum(1 for r in valid if r[\"p_raw\"] < 0.05)\n    n_fdr_sig = sum(1 for r in valid if r.get(\"p_fdr\") is not None and r[\"p_fdr\"] < 0.05)\n    print(f\"\\nFDR: {n_raw_sig}/{n_total} raw-sig -> {n_fdr_sig}/{n_total} FDR-sig \"\n          f\"(BH correction across all {n_total} tests)\")\n\n    if \"consensus_per_alpha\" in output:\n        cpa = output[\"consensus_per_alpha\"]\n        print(f\"\\nCONSENSUS CLASSIFICATION PER ALPHA\")\n        print(\"-\" * 80)\n        for ak in sorted(cpa.keys(), key=lambda k: cpa[k][\"alpha\"]):\n            entry = cpa[ak]\n            print(f\"\\n  a={entry['alpha']:.2f} [{entry['note']}]\")\n            print(f\"    Robust: {entry['consensus']['n_robust']}/{entry['n_pairs']}, \"\n                  f\"Non-robust: {entry['consensus']['n_non_robust']}/{entry['n_pairs']}\")\n            for cl in entry[\"consensus\"][\"classifications\"]:\n                if cl[\"is_robust\"]:\n                    print(f\"      ROBUST  {cl['pair_label']:<35s} ({cl['n_sig_methods']}/{entry['n_methods']} methods)\")\n\n        if \"consensus_regime_comparison\" in output:\n            rc = output[\"consensus_regime_comparison\"]\n            print(f\"\\n  REGIME COMPARISON: {rc['n_stable']}/{rc['n_pairs']} stable, \"\n                  f\"{rc['n_regime_dependent']}/{rc['n_pairs']} regime-dependent\")\n            changed = [l for l, p in rc[\"pairs\"].items() if not p[\"stable\"]]\n            if changed:\n                print(f\"    Regime-dependent pairs:\")\n                for label in changed:\n                    info = rc[\"pairs\"][label]\n                    tags = []\n                    for ak in rc[\"alpha_keys\"]:\n                        if ak in info[\"per_alpha\"]:\n                            v = info[\"per_alpha\"][ak]\n                            t = \"R\" if v[\"is_robust\"] else \".\"\n                            tags.append(f\"a={v['alpha']:.2f}:{t}\")\n                    print(f\"      {label:<35s} {' '.join(tags)}\")\n\n    xcorr = output[\"cross_correlation\"]\n    print(f\"\\nCROSS-CORRELATION (delta-metric, peak lag)\")\n    print(\"-\" * 60)\n    for pair_label in [\"entropy_vs_d1\", \"ece_vs_d1\"]:\n        line = f\"  {pair_label:<18}\"\n        for ak in sorted(xcorr.keys()):\n            p = xcorr[ak].get(pair_label, {})\n            line += f\" | a={xcorr[ak]['alpha']}: lag={p.get('peak_lag','?'):>2} r={p.get('peak_r','?'):>7}\"\n        print(line)\n\n    vel = output[\"per_gen_velocity\"]\n    print(f\"\\nD1 VELOCITY\")\n    print(\"-\" * 60)\n    for ak in sorted(vel.keys()):\n        v = vel[ak]\n        decel = f\"{v['deceleration_ratio']:.2f}\" if v.get(\"deceleration_ratio\") is not None else \"N/A\"\n        print(f\"  a={v['alpha']}: mean_vel={v['mean_velocity']:+.6f}  \"\n              f\"early={v['early_mean_velocity']:+.6f}  late={v['late_mean_velocity']:+.6f}  \"\n              f\"decel_ratio={decel}  max_drop=gen{v['max_drop_gen']}\")\n\n    print()\n\n\n# ---------------------------------------------------------------------------\n# Main\n# ---------------------------------------------------------------------------\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Cross-alpha analysis v4 with per-alpha consensus classification.\"\n    )\n    parser.add_argument(\"--alpha-dirs\", nargs=\"*\", default=None,\n                        help=\"Specific alpha dirs (e.g. a000_s42 a025_s42 mvp). Default: auto-discover all.\")\n    parser.add_argument(\"--n-perms\", type=int, default=5000,\n                        help=\"Permutations for Granger test (default: 5000)\")\n    parser.add_argument(\"--consensus-n-perms\", type=int, default=1000,\n                        help=\"Permutations for consensus perm_granger method (default: 1000)\")\n    parser.add_argument(\"--max-lag\", type=int, default=1,\n                        help=\"Max lag for Granger test (default: 1)\")\n    parser.add_argument(\"--no-mvp\", action=\"store_true\",\n                        help=\"Exclude MVP (alpha=1.0) from auto-discovery\")\n    parser.add_argument(\"--no-consensus\", action=\"store_true\",\n                        help=\"Skip consensus classification (faster)\")\n    parser.add_argument(\"--version\", type=int, default=None,\n                        help=\"Output version number (default: auto-increment)\")\n    parser.add_argument(\"--update-registry\", action=\"store_true\",\n                        help=\"Print registry update commands after analysis\")\n    args = parser.parse_args()\n\n    alpha_dirs = discover_alpha_dirs(args.alpha_dirs, include_mvp=not args.no_mvp)\n    if not alpha_dirs:\n        print(\"ERROR: No alpha directories found.\", file=sys.stderr)\n        sys.exit(1)\n\n    print(f\"Found {len(alpha_dirs)} alpha points: \"\n          f\"{[(a[0], f'seeds={a[3]}') for a in alpha_dirs]}\")\n\n    all_data = []\n    for alpha_key, alpha_val, path, seeds in alpha_dirs:\n        metrics = load_metrics(path)\n        print(f\"  {alpha_key} (a={alpha_val}): {len(metrics)} generations, seeds={seeds}\")\n        all_data.append((alpha_key, alpha_val, metrics))\n\n    # 1. Dose-response\n    dose_resp = compute_dose_response(all_data)\n\n    # 2. Granger\n    print(f\"\\nRunning bidirectional Granger ({len(GRANGER_PAIRS)} pairs x {len(all_data)} alphas, \"\n          f\"n_perms={args.n_perms})...\")\n    granger = run_granger_all(all_data, max_lag=args.max_lag, n_perms=args.n_perms)\n    granger = apply_fdr(granger)\n\n    # 3. Cross-correlation\n    xcorr = cross_correlation(all_data)\n\n    # 4. Velocity\n    velocity = per_gen_velocity(all_data)\n\n    # Assemble output\n    version = args.version or auto_version()\n    n_gens = len(all_data[0][2]) if all_data else 0\n    output = {\n        \"version\": f\"v{version}\",\n        \"date\": datetime.now().strftime(\"%Y-%m-%d\"),\n        \"n_alphas\": len(all_data),\n        \"alpha_points\": [a[1] for a in all_data],\n        \"n_generations\": n_gens,\n        \"gen_range\": f\"gen_0 to gen_{n_gens - 1}\" if n_gens else \"N/A\",\n        \"statistical_config\": {\n            \"granger_max_lag\": args.max_lag,\n            \"granger_n_perm\": args.n_perms,\n            \"granger_differenced\": True,\n            \"fdr_method\": \"benjamini-hochberg\",\n            \"fdr_scope\": f\"all {len(granger)} tests corrected together\",\n            \"n_independent_tests\": len([r for r in granger if r.get(\"p_raw\") is not None]),\n        },\n        \"dose_response\": dose_resp,\n        \"granger_causality\": granger,\n        \"cross_correlation\": xcorr,\n        \"per_gen_velocity\": velocity,\n    }\n\n    # 5. Consensus per alpha\n    if not args.no_consensus:\n        mvp_ablation = os.path.join(MVP_DIR, \"analysis\", \"method_ablation.json\")\n        print(f\"\\nRunning per-alpha consensus classification \"\n              f\"(5 methods x 16 pairs x {len(alpha_dirs)} alphas)...\")\n        consensus_results = run_consensus_per_alpha(\n            alpha_dirs, mvp_ablation_path=mvp_ablation,\n            consensus_n_perm=args.consensus_n_perms)\n        output[\"consensus_per_alpha\"] = consensus_results\n        output[\"consensus_regime_comparison\"] = consensus_regime_comparison(consensus_results)\n\n    # Save JSON\n    os.makedirs(ANALYSIS_DIR, exist_ok=True)\n    json_path = os.path.join(ANALYSIS_DIR, f\"cross_alpha_v{version}.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2, ensure_ascii=False, cls=NumpyEncoder)\n\n    # Save Markdown report\n    md_path = os.path.join(ANALYSIS_DIR, f\"cross_alpha_v{version}_report.md\")\n    generate_markdown_report(output, md_path)\n\n    print_summary(output)\n    print(f\"\\nSaved: {json_path}\")\n    print(f\"Report: {md_path}\")\n\n    if args.update_registry:\n        print(\"\\n--- Registry update commands ---\")\n        for alpha_key, alpha_val, _ in all_data:\n            dr = dose_resp[alpha_key]\n            print(f\"# {alpha_key}: d1_drift={dr['distinct_1']['drift_pct']}%, \"\n                  f\"entropy_drift={dr['token_entropy']['drift_pct']}%, \"\n                  f\"ece_drift={dr['ece']['drift_pct']}%\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF\necho \"DEPLOY_STATUS: $?\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T09:02:00.702166+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"DEPLOY_STATUS: 0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.67}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T09:02:00.702324+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"import cross_alpha_analysis_v4; print('SYNTAX OK'); print('Functions:', [x for x in dir(cross_alpha_analysis_v4) if not x.startswith('_') and callable(getattr(cross_alpha_analysis_v4, x))])\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"import cross_alpha_analysis_v4; print('SYNTAX OK'); print('Functions:', [x for x in dir(cross_alpha_analysis_v4) if not x.startswith('_') and callable(getattr(cross_alpha_analysis_v4, x))])\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T09:02:00.702465+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"SYNTAX OK\\nFunctions: ['NumpyEncoder', 'apply_fdr', 'auto_version', 'classify_robust', 'compute_dose_response', 'consensus_regime_comparison', 'cross_correlation', 'datetime', 'diff_xcorr', 'discover_alpha_dirs', 'extract_series', 'generate_markdown_report', 'load_all_seeds_metrics', 'load_metrics', 'load_sig_matrix', 'ma_extract', 'main', 'multipletests', 'naive_pearson', 'per_gen_velocity', 'perm_granger', 'permutation_granger_test', 'print_summary', 'run_consensus_per_alpha', 'run_granger_all', 'threshold_lead', 'toda_yamamoto']\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.71}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T09:02:00.702590+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python3 cross_alpha_analysis_v4.py --help",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python3 cross_alpha_analysis_v4.py --help",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T09:02:00.702732+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"usage: cross_alpha_analysis_v4.py [-h] [--alpha-dirs [ALPHA_DIRS ...]]\\n                                  [--n-perms N_PERMS]\\n                                  [--consensus-n-perms CONSENSUS_N_PERMS]\\n                                  [--max-lag MAX_LAG] [--no-mvp]\\n                                  [--no-consensus] [--version VERSION]\\n                                  [--update-registry]\\n\\nCross-alpha analysis v4 with per-alpha consensus classification.\\n\\noptions:\\n  -h, --help            show this help message and exit\\n  --alpha-dirs [ALPHA_DIRS ...]\\n                        Specific alpha dirs (e.g. a000_s42 a025_s42 mvp).\\n                        Default: auto-discover all.\\n  --n-perms N_PERMS     Permutations for Granger test (default: 5000)\\n  --consensus-n-perms CONSENSUS_N_PERMS\\n                        Permutations for consensus perm_granger method\\n                        (default: 1000)\\n  --max-lag MAX_LAG     Max lag for Granger test (default: 1)\\n  --no-mvp              Exclude MVP (alpha=1.0) from auto-discovery\\n  --no-consensus        Skip consensus classification (faster)\\n  --version VERSION     Output version number (default: auto-increment)\\n  --update-registry     Print registry update commands after analysis\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.76}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T09:02:00.702863+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nfrom cross_alpha_analysis_v4 import discover_alpha_dirs\ndirs = discover_alpha_dirs()\nfor ak, av, path, seeds in dirs:\n    print(f'{ak}: alpha={av}, path={path}, seeds={seeds}')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nfrom cross_alpha_analysis_v4 import discover_alpha_dirs\ndirs = discover_alpha_dirs()\nfor ak, av, path, seeds in dirs:\n    print(f'{ak}: alpha={av}, path={path}, seeds={seeds}')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T09:02:00.702994+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"a000: alpha=0.0, path=/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42, seeds=[42]\\na025: alpha=0.25, path=/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s42, seeds=[42]\\na050: alpha=0.5, path=/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42, seeds=[42]\\na075: alpha=0.75, path=/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42, seeds=[42]\\na100: alpha=1.0, path=/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42, seeds=[42, 43, 44, 45]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.82}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T09:02:00.703139+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_v4_ready.md",
  "content": "# Cross-Alpha Analysis v4 — Execution Ready\n\n## Script\n- **Server:** westd-19828\n- **Path:** `/root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py`\n- **Status:** Deployed, syntax verified, imports OK\n\n## Alpha Directories (5 points)\n\n| Alpha | Key  | Path | Seeds | Mode |\n|-------|------|------|-------|------|\n| 0.00  | a000 | `results/alpha_sweep/a000_s42/` | [42] | single-seed, method agreement only |\n| 0.25  | a025 | `results/alpha_sweep/a025_s42/` | [42] | single-seed, method agreement only |\n| 0.50  | a050 | `results/alpha_sweep/a050_s42/` | [42] | single-seed, method agreement only |\n| 0.75  | a075 | `results/alpha_sweep/a075_s42/` | [42] | single-seed, method agreement only |\n| 1.00  | a100 | `results/mvp/rep_42/` (+rep_43/44/45) | [42,43,44,45] | full consensus via method_ablation.json |\n\n## Execution Command\n\n```bash\nssh westd-19828\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\ncd /root/autodl-tmp/distrib_canary_collapse\n\n# Full run (all 5 alphas, consensus + Granger, ~15-20 min)\npython3 cross_alpha_analysis_v4.py --n-perms 5000 --consensus-n-perms 1000 --update-registry\n\n# Quick test without consensus (skip 5-method classification)\npython3 cross_alpha_analysis_v4.py --no-consensus --n-perms 5000\n```\n\n## Expected Output\n\n- **JSON:** `results/analysis/cross_alpha_v{N}.json`\n- **Markdown:** `results/analysis/cross_alpha_v{N}_report.md`\n\n## v4 New Features (vs v3)\n\n1. **α=1.0 integration:** Auto-discovers MVP rep_42..45 as α=1.0; loads seed=42 for Granger/xcorr, all 4 seeds for consensus\n2. **Per-α consensus classification:** Runs 5 methods (naive_pearson, differenced_xcorr, threshold_onset, toda_yamamoto, permutation_granger) on all 16 canary→downstream pairs at each α. Single-seed α points use seed_threshold=1 (method agreement only). α=1.0 loads existing method_ablation.json (4 seeds, full consensus with seed_threshold=3)\n3. **Regime comparison:** Cross-α stability matrix showing which pairs change robust/non-robust classification — direct evidence of regime-dependent validity\n4. **Markdown report:** Human-readable report alongside JSON\n\n## Prerequisites\n\n- a075_s42 must be complete (check `results/alpha_sweep/a075_s42/all_metrics.json` exists)\n- Dependencies already installed: numpy, scipy, statsmodels\n- Sibling scripts required: `method_ablation.py`, `consensus_framework.py`, `permutation_granger.py`\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_v4_ready.md",
    "content": "# Cross-Alpha Analysis v4 — Execution Ready\n\n## Script\n- **Server:** westd-19828\n- **Path:** `/root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py`\n- **Status:** Deployed, syntax verified, imports OK\n\n## Alpha Directories (5 points)\n\n| Alpha | Key  | Path | Seeds | Mode |\n|-------|------|------|-------|------|\n| 0.00  | a000 | `results/alpha_sweep/a000_s42/` | [42] | single-seed, method agreement only |\n| 0.25  | a025 | `results/alpha_sweep/a025_s42/` | [42] | single-seed, method agreement only |\n| 0.50  | a050 | `results/alpha_sweep/a050_s42/` | [42] | single-seed, method agreement only |\n| 0.75  | a075 | `results/alpha_sweep/a075_s42/` | [42] | single-seed, method agreement only |\n| 1.00  | a100 | `results/mvp/rep_42/` (+rep_43/44/45) | [42,43,44,45] | full consensus via method_ablation.json |\n\n## Execution Command\n\n```bash\nssh westd-19828\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\ncd /root/autodl-tmp/distrib_canary_collapse\n\n# Full run (all 5 alphas, consensus + Granger, ~15-20 min)\npython3 cross_alpha_analysis_v4.py --n-perms 5000 --consensus-n-perms 1000 --update-registry\n\n# Quick test without consensus (skip 5-method classification)\npython3 cross_alpha_analysis_v4.py --no-consensus --n-perms 5000\n```\n\n## Expected Output\n\n- **JSON:** `results/analysis/cross_alpha_v{N}.json`\n- **Markdown:** `results/analysis/cross_alpha_v{N}_report.md`\n\n## v4 New Features (vs v3)\n\n1. **α=1.0 integration:** Auto-discovers MVP rep_42..45 as α=1.0; loads seed=42 for Granger/xcorr, all 4 seeds for consensus\n2. **Per-α consensus classification:** Runs 5 methods (naive_pearson, differenced_xcorr, threshold_onset, toda_yamamoto, permutation_granger) on all 16 canary→downstream pairs at each α. Single-seed α points use seed_threshold=1 (method agreement only). α=1.0 loads existing method_ablation.json (4 seeds, full consensus with seed_threshold=3)\n3. **Regime comparison:** Cross-α stability matrix showing which pairs change robust/non-robust classification — direct evidence of regime-dependent validity\n4. **Markdown report:** Human-readable report alongside JSON\n\n## Prerequisites\n\n- a075_s42 must be complete (check `results/alpha_sweep/a075_s42/all_metrics.json` exists)\n- Dependencies already installed: numpy, scipy, statsmodels\n- Sibling scripts required: `method_ablation.py`, `consensus_framework.py`, `permutation_granger.py`\n"
  }
}
````

</details>

---

### Tool result

_source line 62 · 2026-05-15T09:02:00.703305+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/cross_alpha_v4_ready.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-15T09:02:00.703468+00:00_

完成。

**产出：**
- 服务器脚本：`/root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py` — 已部署、语法验证通过
- 本地执行文档：`artifacts/cross_alpha_v4_ready.md`

**v4 相比 v3 的新增：**
- α=1.0 自动从 `results/mvp/rep_{42..45}` 加载（4 seeds，full consensus via method_ablation.json）
- 对每个 α 点运行 5 方法×16 对的 consensus classification；单 seed 点标注 "method agreement only"（seed_threshold=1）
- 跨 α regime comparison 矩阵，直接显示哪些 pair 在不同 α 下分类变化
- 同时输出 JSON + Markdown 报告

a075_s42 完成后执行：
```bash
python3 cross_alpha_analysis_v4.py --n-perms 5000 --consensus-n-perms 1000 --update-registry
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_cross_alpha_5point_script_20260515T085132"
}
```

</details>

---
