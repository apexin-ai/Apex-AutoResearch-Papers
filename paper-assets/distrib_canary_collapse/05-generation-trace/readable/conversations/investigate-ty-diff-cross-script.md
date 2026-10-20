# investigate ty diff cross script

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/chats/worker_investigate_ty_diff_cross_script_20260520T044639.jsonl`
- **Structured JSON:** [`1bc90612673c2846c630.json`](../../sessions/1b/1bc90612673c2846c630.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

67 recorded events

### Tool call

_source line 1 · 2026-05-20T04:54:58.558010+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T04:54:58.558437+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T04:54:58.558632+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"run_5method*.py\" -o -name \"batch_analysis*.py\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -name \"run_5method*.py\" -o -name \"batch_analysis*.py\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T04:54:58.558775+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results -type d -name \"*a075*s43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results -type d -name \"*a075*s43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T04:54:58.558919+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py\\n/root/autodl-tmp/distrib_canary_collapse/batch_analysis.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.07}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T04:54:58.559048+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T04:54:58.559198+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results -type d -maxdepth 2 -name \"*a075*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results -type d -maxdepth 2 -name \"*a075*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T04:54:58.559370+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/intervention/predictive_te_a075_s42_fp32\\n/root/autodl-tmp/distrib_canary_collapse/results/intervention/predictive_te_a075_s42_fp32_v2\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42_fp32\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a075_s42_fp32\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T04:54:58.559530+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T04:54:58.559663+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"ablation\\nalpha_sweep\\nalpha_sweep_c4\\nanalysis\\ndry_run\\ngeneralize\\nintervention\\nmethod_ablation_phase3\\npadding_robustness\\nscale\\nscale_check\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T04:54:58.559809+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results -type d -maxdepth 3 -name \"*s43*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results -type d -maxdepth 3 -name \"*s43*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T04:54:58.559949+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/intervention/predictive_te_s43\\n/root/autodl-tmp/distrib_canary_collapse/results/intervention/reactive_d1_s43\\n/root/autodl-tmp/distrib_canary_collapse/results/intervention/reactive_d1_s43_bf16\\n/root/autodl-tmp/distrib_canary_collapse/results/intervention/predictive_te_s43_bf16\\n/root/autodl-tmp/distrib_canary_collapse/results/intervention/reactive_d1_s43_fp32\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s43_bf16\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s43_fp32\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s43_fp32\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43_fp32\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s43_fp32\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/opt13b_wiki_a100_s43_bf16\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/qwen35_08b_wiki_a100_s43_fp32\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s43\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s43_17855\\n/root/autodl-tmp/distrib_canary_collapse/results/scale_check/pythia69b_wiki_a100_s43\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T04:54:58.560078+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T04:54:58.560209+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"a000_s42_fp32\\na005_s42_fp32\\na005_s42_fp32_v2\\na005_s42_fp32_v3\\na005_s42_fp32_v3_d080\\na010_s42_bf16\\na010_s42_fp32\\na010_s43_bf16\\na010_s43_fp32\\na025_s42_fp32\\na025_s43_fp32\\na025_s44_fp32\\na030_s42_fp32\\na035_s42_fp32\\na040_s42_fp32\\na045_s42_fp32\\na050_postd093_s42_fp32\\na050_s42_fp32\\na050_s43_fp32\\na050_s44_fp32\\na060_s42\\na060_s42_bf16\\na060_s42_fp32\\na060_s42_fp32_v2\\na060_s42_fp32_v3_d080\\na060_s43_fp32\\na075_s42_fp32\\na100_s42_fp32\\nc4_a025_s42_fp32\\nc4_a050_s42_fp32\\nc4_a075_s42_fp32\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T04:54:58.560395+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "wc -l /root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "wc -l /root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T04:54:58.560536+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  431 /root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py\\n  600 /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py\\n 1031 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T04:54:58.560660+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T04:54:58.560780+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T04:54:58.561062+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Self-contained 5-method lead-lag analysis for GPT-2m s43.\\\"\\\"\\\"\\nimport json\\nimport os\\nimport sys\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.tsa.stattools import adfuller\\n\\nN_PERM = 5000\\nALPHA = 0.05\\n\\nCANARIES = [\\\"token_entropy\\\", \\\"ece\\\"]\\nDOWNSTREAMS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"perplexity\\\"]\\n\\nHIGHER_IS_WORSE = {\\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\nDATA_DIR = \\\"/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16\\\"\\n\\n\\ndef load_series(data_dir):\\n    with open(os.path.join(data_dir, \\\"all_metrics.json\\\")) as f:\\n        data = json.load(f)\\n    data.sort(key=lambda x: x[\\\"generation\\\"])\\n    out = {}\\n    for k in CANARIES + DOWNSTREAMS:\\n        out[k] = np.array([d[k] for d in data])\\n    return out, len(data)\\n\\n\\ndef orient(series, name):\\n    return -series.copy() if name in LOWER_IS_WORSE else series.copy()\\n\\n\\ndef bh_fdr(p_values, alpha=0.05):\\n    pv = np.array(p_values, dtype=float)\\n    n = len(pv)\\n    valid = ~np.isnan(pv)\\n    adjusted = np.full(n, np.nan)\\n    if valid.sum() == 0:\\n        return adjusted.tolist(), [False] * n\\n    idx = np.where(valid)[0]\\n    p_valid = pv[idx]\\n    sorted_idx = np.argsort(p_valid)\\n    ranks = np.empty_like(sorted_idx)\\n    ranks[sorted_idx] = np.arange(1, len(p_valid) + 1)\\n    m = len(p_valid)\\n    adj = p_valid * m / ranks\\n    adj_sorted = adj[sorted_idx].copy()\\n    for i in range(m - 2, -1, -1):\\n        adj_sorted[i] = min(adj_sorted[i], adj_sorted[i + 1])\\n    adj_sorted = np.minimum(adj_sorted, 1.0)\\n    adj_final = np.empty(m)\\n    adj_final[sorted_idx] = adj_sorted\\n    for i, ix in enumerate(idx):\\n        adjusted[ix] = adj_final[i]\\n    significant = [(a
…[truncated 7408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T04:54:58.561486+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Batch lead-lag analysis for distributional canary collapse experiments.\\n\\nReads all_metrics.json from an experiment directory, runs 5-method lead-lag\\nanalysis on all canary-diversity pairs, computes K>=4 consensus, and optionally\\nruns full MMCT if null directories are provided.\\n\\nUsage:\\n    python batch_analysis.py --exp_dir results/alpha_sweep/a010_s43_bf16\\n    python batch_analysis.py --exp_dir results/alpha_sweep/a010_s43_bf16 \\\\\\n        --null_dirs results/alpha_sweep/a000_s42 results/alpha_sweep/a000_s43\\n\\nInput:  {exp_dir}/all_metrics.json\\nOutput: {exp_dir}/analysis_results.json (or --output path)\\n\\nDependencies: numpy, scipy, statsmodels\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport traceback\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.tsa.stattools import adfuller\\n\\nN_PERM = 5000\\nALPHA_SIG = 0.05\\n\\nCANARIES = [\\\"token_entropy\\\", \\\"ece\\\"]\\nDOWNSTREAMS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"mauve\\\"]\\n\\nHIGHER_IS_WORSE = {\\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"mauve\\\"}\\n\\nALL_METRICS = [\\\"token_entropy\\\", \\\"ece\\\", \\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\",\\n               \\\"distinct_3\\\", \\\"effective_rank\\\", \\\"mauve\\\"]\\n\\n\\ndef load_series(data_dir):\\n    path = os.path.join(data_dir, \\\"all_metrics.json\\\")\\n    with open(path) as f:\\n        data = json.load(f)\\n    data.sort(key=lambda x: x[\\\"generation\\\"])\\n    out = {}\\n    for k in ALL_METRICS:\\n        vals = []\\n        for d in data:\\n            v = d.get(k)\\n            vals.append(v if v is not None else np.nan)\\n        out[k] = np.array(vals, dtype=float)\\n    return out, len(data)\\n\\n\\ndef orient(series, name):\\n    return -series.co
…[truncated 7388 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T04:54:58.561715+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -n \"def ty_granger\\|def diff_xcorr\\|def perm_granger\\|def threshold_onset\\|def naive_xcorr\\|def analyze\\|def run\\|peak_lag.*0\\|direction\\|max_lag\\|d_max\\|significant\" /root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -n \"def ty_granger\\|def diff_xcorr\\|def perm_granger\\|def threshold_onset\\|def naive_xcorr\\|def analyze\\|def run\\|peak_lag.*0\\|direction\\|max_lag\\|d_max\\|significant\" /root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T04:54:58.561859+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T04:54:58.561989+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -n \"def ty_granger\\|def diff_xcorr\\|def perm_granger\\|def threshold_onset\\|def naive_xcorr\\|def analyze\\|peak_lag.*0\\|direction\\|max_lag\\|d_max\\|significant\\|_count_forward\\|lead_lag\" /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -n \"def ty_granger\\|def diff_xcorr\\|def perm_granger\\|def threshold_onset\\|def naive_xcorr\\|def analyze\\|peak_lag.*0\\|direction\\|max_lag\\|d_max\\|significant\\|_count_forward\\|lead_lag\" /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T04:54:58.562138+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T04:54:58.562299+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -n \"def \" /root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -n \"def \" /root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T04:54:58.562441+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"21:def load_series(data_dir):\\n31:def orient(series, name):\\n35:def bh_fdr(p_values, alpha=0.05):\\n62:def naive_xcorr(c, d, cn, dn, max_lag=5):\\n89:def diff_xcorr(c, d, cn, dn, max_lag=5):\\n118:def threshold_onset(c, d, cn, dn, sigma_mult=3):\\n156:def _build_lag_matrix(y, x, max_lag):\\n169:def _granger_f_stat(y, x, max_lag):\\n187:def perm_granger(x, y, max_lag=1, n_perm=5000, seed=42, difference=True):\\n221:def ty_granger(c, d, cn, dn, max_lag_search=2):\\n300:def run():\\n410:    def clean(obj):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T04:54:58.562564+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "grep -n \"def \" /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "grep -n \"def \" /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T04:54:58.562696+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"40:def load_series(data_dir):\\n55:def orient(series, name):\\n59:def compute_drift(series_dict, n_gens):\\n74:def bh_fdr(p_values, alpha=0.05):\\n102:def naive_xcorr(c, d, cn, dn, max_lag=5):\\n132:def diff_xcorr(c, d, cn, dn, max_lag=5):\\n163:def threshold_onset(c, d, cn, dn, sigma_mult=3):\\n204:def _build_lag_matrix(y, x, max_lag):\\n217:def _granger_f_stat(y, x, max_lag):\\n235:def perm_granger(x, y, max_lag=1, n_perm=N_PERM, seed=42, difference=True):\\n270:def _determine_d_max(series, max_d=2, alpha=0.05):\\n283:def ty_granger(c, d, cn, dn, max_lag=1):\\n334:def run_pair(series, cn, dn):\\n354:def apply_fdr_correction(all_pair_results):\\n372:def compute_consensus(pair_result):\\n392:def run_mmct_full(exp_dir, null_dirs):\\n426:def analyze(exp_dir, output_path=None, null_dirs=None):\\n543:def _save_5method_format(all_pairs, n_gens, exp_dir, analysis_dir):\\n575:def _clean(obj):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T04:54:58.562839+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "tail -n +221 /root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "tail -n +221 /root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T04:54:58.563129+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def ty_granger(c, d, cn, dn, max_lag_search=2):\\n    x, y = orient(c, cn), orient(d, dn)\\n    T = len(x)\\n    try:\\n        adf_x = adfuller(x, maxlag=min(2, T // 3 - 1))\\n        adf_y = adfuller(y, maxlag=min(2, T // 3 - 1))\\n    except Exception:\\n        return {\\\"method\\\": \\\"ty_granger\\\", \\\"significant\\\": False, \\\"note\\\": \\\"ADF failed\\\"}\\n    d_max = 0\\n    if adf_x[1] > 0.05:\\n        d_max = max(d_max, 1)\\n    if adf_y[1] > 0.05:\\n        d_max = max(d_max, 1)\\n    p_opt = 1\\n    best_aic = np.inf\\n    for p_try in range(1, max_lag_search + 1):\\n        n_fit = T - p_try\\n        if n_fit < 5:\\n            continue\\n        Y_fit = y[p_try:]\\n        cols = [np.ones(n_fit)]\\n        for lag in range(1, p_try + 1):\\n            cols.append(y[p_try - lag: T - lag])\\n            cols.append(x[p_try - lag: T - lag])\\n        X_fit = np.column_stack(cols)\\n        try:\\n            beta = np.linalg.lstsq(X_fit, Y_fit, rcond=None)[0]\\n            rss = np.sum((Y_fit - X_fit @ beta) ** 2)\\n            k = X_fit.shape[1]\\n            aic = n_fit * np.log(rss / n_fit + 1e-15) + 2 * k\\n            if aic < best_aic:\\n                best_aic = aic\\n                p_opt = p_try\\n        except Exception:\\n            continue\\n    p_aug = p_opt + d_max\\n    n = T - p_aug\\n    if n < 4:\\n        return {\\\"method\\\": \\\"ty_granger\\\", \\\"significant\\\": False, \\\"note\\\": f\\\"n={n} too small\\\",\\n                \\\"d_max\\\": d_max, \\\"p_opt\\\": p_opt, \\\"p_aug\\\": p_aug}\\n    Y = y[p_aug:]\\n    cols_r = [np.ones(n)]\\n    for lag in range(1, p_aug + 1):\\n        cols_r.append(y[p_aug - lag: T - lag])\\n    for lag in range(p_opt + 1, p_aug + 1):\\n        cols_r.append(x[p_aug - lag: T - lag])\\n    X_r = np.column_stack(cols_r)\\n    cols_u = list(cols_r)\\n    for lag in range(1, p_opt + 1):\\n        cols_u.append(x[p_aug - lag: T - la
…[truncated 7444 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T04:54:58.563313+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "tail -n +270 /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "tail -n +270 /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T04:54:58.563644+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def _determine_d_max(series, max_d=2, alpha=0.05):\\n    for d in range(max_d + 1):\\n        try:\\n            result = adfuller(series, maxlag=min(3, len(series) // 3 - 1),\\n                              regression=\\\"ct\\\", autolag=\\\"AIC\\\")\\n            if result[1] < alpha:\\n                return d\\n            series = np.diff(series)\\n        except Exception:\\n            return d\\n    return max_d\\n\\n\\ndef ty_granger(c, d, cn, dn, max_lag=1):\\n    x, y = orient(c, cn), orient(d, dn)\\n    if np.any(np.isnan(x)) or np.any(np.isnan(y)):\\n        return {\\\"method\\\": \\\"ty_granger\\\", \\\"chi2\\\": None, \\\"p_value\\\": None,\\n                \\\"significant\\\": False, \\\"note\\\": \\\"NaN in data\\\"}\\n    d_max = max(_determine_d_max(x), _determine_d_max(y))\\n    p_total = max_lag + d_max\\n    T = len(x)\\n    n = T - p_total\\n    if n <= p_total + 2:\\n        return {\\\"method\\\": \\\"ty_granger\\\", \\\"chi2\\\": None, \\\"p_value\\\": None,\\n                \\\"significant\\\": False, \\\"d_max\\\": int(d_max),\\n                \\\"note\\\": f\\\"T={T} too short for d_max={d_max}, p={p_total}\\\"}\\n    Y = y[p_total:]\\n    cols_r = [np.ones(n)]\\n    for lag in range(1, p_total + 1):\\n        cols_r.append(y[p_total - lag: T - lag])\\n    for lag in range(max_lag + 1, p_total + 1):\\n        cols_r.append(x[p_total - lag: T - lag])\\n    cols_u = list(cols_r)\\n    for lag in range(1, max_lag + 1):\\n        cols_u.append(x[p_total - lag: T - lag])\\n    X_r = np.column_stack(cols_r)\\n    X_u = np.column_stack(cols_u)\\n    try:\\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\\n    except np.linalg.LinAlgError:\\n        return {\\\"method\\\": \\\"ty_granger\\\", \\\"chi2\\\": None, \\\"p_value\\\": None,\\n                \\\"significant\\\": False, \\\"note\\\": \\\"lstsq failed\\\"}\\n    
…[truncated 7458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T04:54:58.563840+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "head -n 200 /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "head -n 200 /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T04:54:58.564107+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Batch lead-lag analysis for distributional canary collapse experiments.\\n\\nReads all_metrics.json from an experiment directory, runs 5-method lead-lag\\nanalysis on all canary-diversity pairs, computes K>=4 consensus, and optionally\\nruns full MMCT if null directories are provided.\\n\\nUsage:\\n    python batch_analysis.py --exp_dir results/alpha_sweep/a010_s43_bf16\\n    python batch_analysis.py --exp_dir results/alpha_sweep/a010_s43_bf16 \\\\\\n        --null_dirs results/alpha_sweep/a000_s42 results/alpha_sweep/a000_s43\\n\\nInput:  {exp_dir}/all_metrics.json\\nOutput: {exp_dir}/analysis_results.json (or --output path)\\n\\nDependencies: numpy, scipy, statsmodels\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport traceback\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.tsa.stattools import adfuller\\n\\nN_PERM = 5000\\nALPHA_SIG = 0.05\\n\\nCANARIES = [\\\"token_entropy\\\", \\\"ece\\\"]\\nDOWNSTREAMS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"mauve\\\"]\\n\\nHIGHER_IS_WORSE = {\\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"mauve\\\"}\\n\\nALL_METRICS = [\\\"token_entropy\\\", \\\"ece\\\", \\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\",\\n               \\\"distinct_3\\\", \\\"effective_rank\\\", \\\"mauve\\\"]\\n\\n\\ndef load_series(data_dir):\\n    path = os.path.join(data_dir, \\\"all_metrics.json\\\")\\n    with open(path) as f:\\n        data = json.load(f)\\n    data.sort(key=lambda x: x[\\\"generation\\\"])\\n    out = {}\\n    for k in ALL_METRICS:\\n        vals = []\\n        for d in data:\\n            v = d.get(k)\\n            vals.append(v if v is not None else np.nan)\\n        out[k] = np.array(vals, dtype=float)\\n    return out, len(data)\\n\\n\\ndef orient(series, name):\\n    return -series.co
…[truncated 5539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T04:54:58.564313+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "tail -n +370 /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "tail -n +370 /root/autodl-tmp/distrib_canary_collapse/batch_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T04:54:58.564608+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# ── Consensus counting ──\\n\\ndef compute_consensus(pair_result):\\n    r = pair_result[\\\"results\\\"]\\n    votes = 0\\n    methods_sig = []\\n    if r[\\\"naive_xcorr\\\"].get(\\\"significant\\\", False) and (r[\\\"naive_xcorr\\\"].get(\\\"peak_lag\\\") or 0) < 0:\\n        votes += 1; methods_sig.append(\\\"naive\\\")\\n    if (r[\\\"diff_xcorr\\\"].get(\\\"significant_fdr\\\", r[\\\"diff_xcorr\\\"].get(\\\"significant\\\", False))\\n            and (r[\\\"diff_xcorr\\\"].get(\\\"peak_lag\\\") or 0) < 0):\\n        votes += 1; methods_sig.append(\\\"diff\\\")\\n    if r[\\\"threshold_onset\\\"].get(\\\"significant\\\", False):\\n        votes += 1; methods_sig.append(\\\"thresh\\\")\\n    if r[\\\"perm_granger_fwd\\\"].get(\\\"significant_fdr\\\", r[\\\"perm_granger_fwd\\\"].get(\\\"significant\\\", False)):\\n        votes += 1; methods_sig.append(\\\"pg_fwd\\\")\\n    if r[\\\"ty_granger\\\"].get(\\\"significant\\\", False):\\n        votes += 1; methods_sig.append(\\\"ty\\\")\\n    return votes, methods_sig\\n\\n\\n# ── MMCT (full, if null dirs available) ──\\n\\ndef run_mmct_full(exp_dir, null_dirs):\\n    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\\n    from mmct.null_distribution import NullDistribution\\n    from mmct.consensus_test import MMCT\\n    from mmct.methods import METRIC_PAIRS as MMCT_PAIRS\\n\\n    null_dist = NullDistribution(null_dirs, n_bootstrap=10000, seed=42)\\n    mmct = MMCT(null_dist, weighted=True, bidirectional=False, alpha=0.05)\\n\\n    n_sig = 0\\n    n_total = 0\\n    pair_results = []\\n    for canary, downstream in MMCT_PAIRS:\\n        try:\\n            result = mmct.test_from_precomputed(exp_dir, canary, downstream)\\n            r = result.to_dict()\\n            pair_results.append(r)\\n            n_total += 1\\n            if r[\\\"significant\\\"]:\\n                n_sig += 1\\n        except Exception:\\n            n_total += 1\\n    dete
…[truncated 7544 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T04:54:58.564798+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "head -n 220 /root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "head -n 220 /root/autodl-tmp/distrib_canary_collapse/run_5method_s43.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T04:54:58.565027+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Self-contained 5-method lead-lag analysis for GPT-2m s43.\\\"\\\"\\\"\\nimport json\\nimport os\\nimport sys\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.tsa.stattools import adfuller\\n\\nN_PERM = 5000\\nALPHA = 0.05\\n\\nCANARIES = [\\\"token_entropy\\\", \\\"ece\\\"]\\nDOWNSTREAMS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"perplexity\\\"]\\n\\nHIGHER_IS_WORSE = {\\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\nDATA_DIR = \\\"/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s43_bf16\\\"\\n\\n\\ndef load_series(data_dir):\\n    with open(os.path.join(data_dir, \\\"all_metrics.json\\\")) as f:\\n        data = json.load(f)\\n    data.sort(key=lambda x: x[\\\"generation\\\"])\\n    out = {}\\n    for k in CANARIES + DOWNSTREAMS:\\n        out[k] = np.array([d[k] for d in data])\\n    return out, len(data)\\n\\n\\ndef orient(series, name):\\n    return -series.copy() if name in LOWER_IS_WORSE else series.copy()\\n\\n\\ndef bh_fdr(p_values, alpha=0.05):\\n    pv = np.array(p_values, dtype=float)\\n    n = len(pv)\\n    valid = ~np.isnan(pv)\\n    adjusted = np.full(n, np.nan)\\n    if valid.sum() == 0:\\n        return adjusted.tolist(), [False] * n\\n    idx = np.where(valid)[0]\\n    p_valid = pv[idx]\\n    sorted_idx = np.argsort(p_valid)\\n    ranks = np.empty_like(sorted_idx)\\n    ranks[sorted_idx] = np.arange(1, len(p_valid) + 1)\\n    m = len(p_valid)\\n    adj = p_valid * m / ranks\\n    adj_sorted = adj[sorted_idx].copy()\\n    for i in range(m - 2, -1, -1):\\n        adj_sorted[i] = min(adj_sorted[i], adj_sorted[i + 1])\\n    adj_sorted = np.minimum(adj_sorted, 1.0)\\n    adj_final = np.empty(m)\\n    adj_final[sorted_idx] = adj_sorted\\n    for i, ix in enumerate(idx):\\n        adjusted[ix] = adj_final[i]\\n    significant = [(a
…[truncated 6424 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T04:54:58.565315+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "cat > /root/autodl-tmp/distrib_canary_collapse/diagnostic_compare.py << 'PYEOF'\n\"\"\"Diagnostic: compare TY Granger and diff_xcorr between two script implementations.\"\"\"\nimport json, os, sys, numpy as np\nfrom scipy import stats\nfrom statsmodels.tsa.stattools import adfuller\n\nCANARIES = [\"token_entropy\", \"ece\"]\nDOWNSTREAMS_COMMON = [\"distinct_1\", \"distinct_2\", \"distinct_3\"]\nDOWNSTREAMS_R5 = DOWNSTREAMS_COMMON + [\"perplexity\"]\nDOWNSTREAMS_BA = DOWNSTREAMS_COMMON + [\"mauve\"]\n\nHIGHER_IS_WORSE = {\"ece\", \"perplexity\"}\nLOWER_IS_WORSE_R5 = {\"token_entropy\", \"distinct_1\", \"distinct_2\", \"distinct_3\"}\nLOWER_IS_WORSE_BA = {\"token_entropy\", \"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"}\nALL_METRICS = [\"token_entropy\", \"ece\", \"perplexity\", \"distinct_1\", \"distinct_2\", \"distinct_3\", \"effective_rank\", \"mauve\"]\n\ndef load_series(data_dir):\n    path = os.path.join(data_dir, \"all_metrics.json\")\n    with open(path) as f:\n        data = json.load(f)\n    data.sort(key=lambda x: x[\"generation\"])\n    out = {}\n    for k in ALL_METRICS:\n        vals = [d.get(k, np.nan) for d in data]\n        out[k] = np.array(vals, dtype=float)\n    return out, len(data)\n\ndef orient_r5(series, name):\n    return -series.copy() if name in LOWER_IS_WORSE_R5 else series.copy()\n\ndef orient_ba(series, name):\n    return -series.copy() if name in LOWER_IS_WORSE_BA else series.copy()\n\n# ===== TY Granger: run_5method version =====\ndef ty_granger_r5(c, d, cn, dn, max_lag_search=2):\n    x, y = orient_r5(c, cn), orient_r5(d, dn)\n    T = len(x)\n    try:\n        adf_x = adfuller(x, maxlag=min(2, T // 3 - 1))\n        adf_y = adfuller(y, maxlag=min(2, T // 3 - 1))\n    except Exception:\n        return {\"significant\": False, \"note\": \"ADF failed\"}\n    d_max = 0\n    if adf_x[1] > 0.05: d_max = max(d_max, 1)\n    if adf_y[1] > 0.05: d_max = max(d_max, 1)\n    p_opt = 1\n    best_aic = np.inf\n    for p_try in range(1, max_lag_search + 1):\n        n_fit = T - p_try\n        if n_fit < 5: continue\n        Y_fit = y[p_try:]\n        cols = [np.ones(n_fit)]\n        for lag in range(1, p_try + 1):\n            cols.append(y[p_try - lag: T - lag])\n            cols.append(x[p_try - lag: T - lag])\n        X_fit = np.column_stack(cols)\n        try:\n            beta = np.linalg.lstsq(X_fit, Y_fit, rcond=None)[0]\n            rss = np.sum((Y_fit - X_fit @ beta) ** 2)\n            k = X_fit.shape[1]\n            aic = n_fit * np.log(rss / n_fit + 1e-15) + 2 * k\n            if aic < best_aic:\n                best_aic = aic\n                p_opt = p_try\n        except: continue\n    p_aug = p_opt + d_max\n    n = T - p_aug\n    if n < 4:\n        return {\"significant\": False, \"d_max\": d_max, \"p_opt\": p_opt, \"p_aug\": p_aug, \"note\": f\"n={n}\"}\n    Y = y[p_aug:]\n    cols_r = [np.ones(n)]\n    for lag in range(1, p_aug + 1):\n        cols_r.append(y[p_aug - lag: T - lag])\n    for lag in range(p_opt + 1, p_aug + 1):\n        cols_r.append(x[p_aug - lag: T - lag])\n    X_r = np.column_stack(cols_r)\n    cols_u = list(cols_r)\n    for lag in range(1, p_opt + 1):\n        cols_u.append(x[p_aug - lag: T - lag])\n    X_u = np.column_stack(cols_u)\n    try:\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\n    except: return {\"significant\": False, \"note\": \"lstsq failed\"}\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\n    q = p_opt\n    df_resid = n - X_u.shape[1]\n    if df_resid <= 0 or rss_u < 1e-15:\n        return {\"significant\": False, \"d_max\": d_max, \"df_resid\": df_resid}\n    F = ((rss_r - rss_u) / q) / (rss_u / df_resid)\n    p_val = 1 - stats.f.cdf(F, q, df_resid)\n    return {\"stat_type\": \"F\", \"stat\": round(float(F), 4), \"p_raw\": round(float(p_val), 6),\n            \"significant\": bool(p_val < 0.05), \"d_max\": int(d_max), \"p_opt\": int(p_opt),\n            \"p_aug\": int(p_aug), \"df_resid\": int(df_resid)}\n\n# ===== TY Granger: batch_analysis version =====\ndef _determine_d_max(series, max_d=2, alpha=0.05):\n    for d in range(max_d + 1):\n        try:\n            result = adfuller(series, maxlag=min(3, len(series) // 3 - 1),\n                              regression=\"ct\", autolag=\"AIC\")\n            if result[1] < alpha: return d\n            series = np.diff(series)\n        except: return d\n    return max_d\n\ndef ty_granger_ba(c, d, cn, dn, max_lag=1):\n    x, y = orient_ba(c, cn), orient_ba(d, dn)\n    if np.any(np.isnan(x)) or np.any(np.isnan(y)):\n        return {\"significant\": False, \"note\": \"NaN\"}\n    d_max = max(_determine_d_max(x), _determine_d_max(y))\n    p_total = max_lag + d_max\n    T = len(x)\n    n = T - p_total\n    if n <= p_total + 2:\n        return {\"significant\": False, \"d_max\": int(d_max), \"note\": f\"T={T} too short\"}\n    Y = y[p_total:]\n    cols_r = [np.ones(n)]\n    for lag in range(1, p_total + 1):\n        cols_r.append(y[p_total - lag: T - lag])\n    for lag in range(max_lag + 1, p_total + 1):\n        cols_r.append(x[p_total - lag: T - lag])\n    cols_u = list(cols_r)\n    for lag in range(1, max_lag + 1):\n        cols_u.append(x[p_total - lag: T - lag])\n    X_r = np.column_stack(cols_r)\n    X_u = np.column_stack(cols_u)\n    try:\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\n    except: return {\"significant\": False, \"note\": \"lstsq failed\"}\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\n    df_resid = n - X_u.shape[1]\n    if df_resid <= 0 or rss_u < 1e-15:\n        return {\"significant\": False, \"d_max\": int(d_max), \"df_resid\": df_resid}\n    q = max_lag\n    W = n * (rss_r - rss_u) / rss_u\n    p_val = 1.0 - stats.chi2.cdf(W, q)\n    return {\"stat_type\": \"chi2\", \"stat\": round(float(W), 4), \"p_value\": round(float(p_val), 6),\n            \"significant\": bool(p_val < 0.05), \"d_max\": int(d_max), \"df_resid\": int(df_resid)}\n\n# ===== diff_xcorr: both versions identical in core, differ in orient =====\ndef diff_xcorr_impl(c, d, cn, dn, orient_fn, max_lag=5):\n    dx, dy = np.diff(orient_fn(c, cn)), np.diff(orient_fn(d, dn))\n    n = len(dx)\n    best_lag, best_r, best_p = 0, 0.0, 1.0\n    for lag in range(-max_lag, max_lag + 1):\n        if lag >= 0: a, b = dx[lag:], dy[:n - lag]\n        else: a, b = dx[:n + lag], dy[-lag:]\n        if len(a) < 4: continue\n        if np.std(a) < 1e-12 or np.std(b) < 1e-12: continue\n        r, p = stats.pearsonr(a, b)\n        if abs(r) > abs(best_r):\n            best_lag, best_r, best_p = lag, r, p\n    return {\"peak_lag\": int(best_lag), \"r\": round(float(best_r), 4),\n            \"p_value\": round(float(best_p), 6), \"significant\": bool(best_p < 0.05)}\n\n\ndef main(data_dir):\n    series, n_gens = load_series(data_dir)\n    print(f\"Data: {data_dir}, {n_gens} generations\")\n    \n    # Check which downstreams are available\n    has_perplexity = not np.all(np.isnan(series.get(\"perplexity\", np.array([np.nan]))))\n    has_mauve = not np.all(np.isnan(series.get(\"mauve\", np.array([np.nan]))))\n    print(f\"Has perplexity: {has_perplexity}, Has mauve: {has_mauve}\")\n    \n    # Use common downstreams for fair comparison\n    downstreams = DOWNSTREAMS_COMMON\n    if has_mauve: downstreams = downstreams + [\"mauve\"]\n    print(f\"Using downstreams: {downstreams}\")\n    \n    print(f\"\\n{'='*100}\")\n    print(f\"{'Pair':<30} | {'TY_r5 sig':>10} {'TY_r5 p':>10} {'TY_r5 d_max':>12} | {'TY_ba sig':>10} {'TY_ba p':>10} {'TY_ba d_max':>12}\")\n    print(f\"{'-'*100}\")\n    \n    for cn in CANARIES:\n        for dn in downstreams:\n            c, d = series[cn], series[dn]\n            r5 = ty_granger_r5(c, d, cn, dn)\n            ba = ty_granger_ba(c, d, cn, dn)\n            r5_sig = r5.get(\"significant\", False)\n            r5_p = r5.get(\"p_raw\", r5.get(\"p_value\", \"N/A\"))\n            r5_dm = r5.get(\"d_max\", \"N/A\")\n            ba_sig = ba.get(\"significant\", False)\n            ba_p = ba.get(\"p_value\", \"N/A\")\n            ba_dm = ba.get(\"d_max\", \"N/A\")\n            match = \"==\" if r5_sig == ba_sig else \"!!\"\n            print(f\"{cn}->{dn:<15} | {str(r5_sig):>10} {str(r5_p):>10} {str(r5_dm):>12} | {str(ba_sig):>10} {str(ba_p):>10} {str(ba_dm):>12}  {match}\")\n    \n    print(f\"\\n{'='*100}\")\n    print(f\"{'Pair':<30} | {'diff_r5 lag':>12} {'diff_r5 p':>10} {'r5 sig':>7} | {'diff_ba lag':>12} {'diff_ba p':>10} {'ba sig':>7} | {'lag>0':>5} {'lag<0':>5}\")\n    print(f\"{'-'*100}\")\n    \n    for cn in CANARIES:\n        for dn in downstreams:\n            c, d = series[cn], series[dn]\n            r5 = diff_xcorr_impl(c, d, cn, dn, orient_r5)\n            ba = diff_xcorr_impl(c, d, cn, dn, orient_ba)\n            # For common metrics, orient should be the same (mauve only in BA)\n            lag_gt0 = \"Y\" if r5[\"peak_lag\"] > 0 else \"N\"\n            lag_lt0 = \"Y\" if r5[\"peak_lag\"] < 0 else \"N\"\n            print(f\"{cn}->{dn:<15} | {r5['peak_lag']:>12} {r5['p_value']:>10} {str(r5['significant']):>7} | {ba['peak_lag']:>12} {ba['p_value']:>10} {str(ba['significant']):>7} | {lag_gt0:>5} {lag_lt0:>5}\")\n    \n    # Count using both direction conventions\n    print(f\"\\n{'='*80}\")\n    print(\"Direction check impact on diff_xcorr counts:\")\n    r5_gt0 = sum(1 for cn in CANARIES for dn in downstreams\n                 if diff_xcorr_impl(series[cn], series[dn], cn, dn, orient_r5)[\"significant\"]\n                 and diff_xcorr_impl(series[cn], series[dn], cn, dn, orient_r5)[\"peak_lag\"] > 0)\n    r5_lt0 = sum(1 for cn in CANARIES for dn in downstreams\n                 if diff_xcorr_impl(series[cn], series[dn], cn, dn, orient_r5)[\"significant\"]\n                 and diff_xcorr_impl(series[cn], series[dn], cn, dn, orient_r5)[\"peak_lag\"] < 0)\n    print(f\"  peak_lag > 0 (run_5method convention, WRONG):  {r5_gt0}/{len(CANARIES)*len(downstreams)}\")\n    print(f\"  peak_lag < 0 (batch_analysis convention, CORRECT): {r5_lt0}/{len(CANARIES)*len(downstreams)}\")\n    \n    # TY counts\n    ty_r5_sig = sum(1 for cn in CANARIES for dn in downstreams\n                    if ty_granger_r5(series[cn], series[dn], cn, dn).get(\"significant\", False))\n    ty_ba_sig = sum(1 for cn in CANARIES for dn in downstreams\n                    if ty_granger_ba(series[cn], series[dn], cn, dn).get(\"significant\", False))\n    n_pairs = len(CANARIES) * len(downstreams)\n    print(f\"\\nTY Granger counts:\")\n    print(f\"  run_5method (F-test, AIC lag search): {ty_r5_sig}/{n_pairs}\")\n    print(f\"  batch_analysis (chi2, fixed lag=1):   {ty_ba_sig}/{n_pairs}\")\n\n\nif __name__ == \"__main__\":\n    data_dir = sys.argv[1] if len(sys.argv) > 1 else \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s43_fp32\"\n    main(data_dir)\nPYEOF\necho \"Script written\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat > /root/autodl-tmp/distrib_canary_collapse/diagnostic_compare.py << 'PYEOF'\n\"\"\"Diagnostic: compare TY Granger and diff_xcorr between two script implementations.\"\"\"\nimport json, os, sys, numpy as np\nfrom scipy import stats\nfrom statsmodels.tsa.stattools import adfuller\n\nCANARIES = [\"token_entropy\", \"ece\"]\nDOWNSTREAMS_COMMON = [\"distinct_1\", \"distinct_2\", \"distinct_3\"]\nDOWNSTREAMS_R5 = DOWNSTREAMS_COMMON + [\"perplexity\"]\nDOWNSTREAMS_BA = DOWNSTREAMS_COMMON + [\"mauve\"]\n\nHIGHER_IS_WORSE = {\"ece\", \"perplexity\"}\nLOWER_IS_WORSE_R5 = {\"token_entropy\", \"distinct_1\", \"distinct_2\", \"distinct_3\"}\nLOWER_IS_WORSE_BA = {\"token_entropy\", \"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"}\nALL_METRICS = [\"token_entropy\", \"ece\", \"perplexity\", \"distinct_1\", \"distinct_2\", \"distinct_3\", \"effective_rank\", \"mauve\"]\n\ndef load_series(data_dir):\n    path = os.path.join(data_dir, \"all_metrics.json\")\n    with open(path) as f:\n        data = json.load(f)\n    data.sort(key=lambda x: x[\"generation\"])\n    out = {}\n    for k in ALL_METRICS:\n        vals = [d.get(k, np.nan) for d in data]\n        out[k] = np.array(vals, dtype=float)\n    return out, len(data)\n\ndef orient_r5(series, name):\n    return -series.copy() if name in LOWER_IS_WORSE_R5 else series.copy()\n\ndef orient_ba(series, name):\n    return -series.copy() if name in LOWER_IS_WORSE_BA else series.copy()\n\n# ===== TY Granger: run_5method version =====\ndef ty_granger_r5(c, d, cn, dn, max_lag_search=2):\n    x, y = orient_r5(c, cn), orient_r5(d, dn)\n    T = len(x)\n    try:\n        adf_x = adfuller(x, maxlag=min(2, T // 3 - 1))\n        adf_y = adfuller(y, maxlag=min(2, T // 3 - 1))\n    except Exception:\n        return {\"significant\": False, \"note\": \"ADF failed\"}\n    d_max = 0\n    if adf_x[1] > 0.05: d_max = max(d_max, 1)\n    if adf_y[1] > 0.05: d_max = max(d_max, 1)\n    p_opt = 1\n    best_aic = np.inf\n    for p_try in range(1, max_lag_search + 1):\n        n_fit = T - p_try\n        if n_fit < 5: continue\n        Y_fit = y[p_try:]\n        cols = [np.ones(n_fit)]\n        for lag in range(1, p_try + 1):\n            cols.append(y[p_try - lag: T - lag])\n            cols.append(x[p_try - lag: T - lag])\n        X_fit = np.column_stack(cols)\n        try:\n            beta = np.linalg.lstsq(X_fit, Y_fit, rcond=None)[0]\n            rss = np.sum((Y_fit - X_fit @ beta) ** 2)\n            k = X_fit.shape[1]\n            aic = n_fit * np.log(rss / n_fit + 1e-15) + 2 * k\n            if aic < best_aic:\n                best_aic = aic\n                p_opt = p_try\n        except: continue\n    p_aug = p_opt + d_max\n    n = T - p_aug\n    if n < 4:\n        return {\"significant\": False, \"d_max\": d_max, \"p_opt\": p_opt, \"p_aug\": p_aug, \"note\": f\"n={n}\"}\n    Y = y[p_aug:]\n    cols_r = [np.ones(n)]\n    for lag in range(1, p_aug + 1):\n        cols_r.append(y[p_aug - lag: T - lag])\n    for lag in range(p_opt + 1, p_aug + 1):\n        cols_r.append(x[p_aug - lag: T - lag])\n    X_r = np.column_stack(cols_r)\n    cols_u = list(cols_r)\n    for lag in range(1, p_opt + 1):\n        cols_u.append(x[p_aug - lag: T - lag])\n    X_u = np.column_stack(cols_u)\n    try:\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\n    except: return {\"significant\": False, \"note\": \"lstsq failed\"}\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\n    q = p_opt\n    df_resid = n - X_u.shape[1]\n    if df_resid <= 0 or rss_u < 1e-15:\n        return {\"significant\": False, \"d_max\": d_max, \"df_resid\": df_resid}\n    F = ((rss_r - rss_u) / q) / (rss_u / df_resid)\n    p_val = 1 - stats.f.cdf(F, q, df_resid)\n    return {\"stat_type\": \"F\", \"stat\": round(float(F), 4), \"p_raw\": round(float(p_val), 6),\n            \"significant\": bool(p_val < 0.05), \"d_max\": int(d_max), \"p_opt\": int(p_opt),\n            \"p_aug\": int(p_aug), \"df_resid\": int(df_resid)}\n\n# ===== TY Granger: batch_analysis version =====\ndef _determine_d_max(series, max_d=2, alpha=0.05):\n    for d in range(max_d + 1):\n        try:\n            result = adfuller(series, maxlag=min(3, len(series) // 3 - 1),\n                              regression=\"ct\", autolag=\"AIC\")\n            if result[1] < alpha: return d\n            series = np.diff(series)\n        except: return d\n    return max_d\n\ndef ty_granger_ba(c, d, cn, dn, max_lag=1):\n    x, y = orient_ba(c, cn), orient_ba(d, dn)\n    if np.any(np.isnan(x)) or np.any(np.isnan(y)):\n        return {\"significant\": False, \"note\": \"NaN\"}\n    d_max = max(_determine_d_max(x), _determine_d_max(y))\n    p_total = max_lag + d_max\n    T = len(x)\n    n = T - p_total\n    if n <= p_total + 2:\n        return {\"significant\": False, \"d_max\": int(d_max), \"note\": f\"T={T} too short\"}\n    Y = y[p_total:]\n    cols_r = [np.ones(n)]\n    for lag in range(1, p_total + 1):\n        cols_r.append(y[p_total - lag: T - lag])\n    for lag in range(max_lag + 1, p_total + 1):\n        cols_r.append(x[p_total - lag: T - lag])\n    cols_u = list(cols_r)\n    for lag in range(1, max_lag + 1):\n        cols_u.append(x[p_total - lag: T - lag])\n    X_r = np.column_stack(cols_r)\n    X_u = np.column_stack(cols_u)\n    try:\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\n    except: return {\"significant\": False, \"note\": \"lstsq failed\"}\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\n    df_resid = n - X_u.shape[1]\n    if df_resid <= 0 or rss_u < 1e-15:\n        return {\"significant\": False, \"d_max\": int(d_max), \"df_resid\": df_resid}\n    q = max_lag\n    W = n * (rss_r - rss_u) / rss_u\n    p_val = 1.0 - stats.chi2.cdf(W, q)\n    return {\"stat_type\": \"chi2\", \"stat\": round(float(W), 4), \"p_value\": round(float(p_val), 6),\n            \"significant\": bool(p_val < 0.05), \"d_max\": int(d_max), \"df_resid\": int(df_resid)}\n\n# ===== diff_xcorr: both versions identical in core, differ in orient =====\ndef diff_xcorr_impl(c, d, cn, dn, orient_fn, max_lag=5):\n    dx, dy = np.diff(orient_fn(c, cn)), np.diff(orient_fn(d, dn))\n    n = len(dx)\n    best_lag, best_r, best_p = 0, 0.0, 1.0\n    for lag in range(-max_lag, max_lag + 1):\n        if lag >= 0: a, b = dx[lag:], dy[:n - lag]\n        else: a, b = dx[:n + lag], dy[-lag:]\n        if len(a) < 4: continue\n        if np.std(a) < 1e-12 or np.std(b) < 1e-12: continue\n        r, p = stats.pearsonr(a, b)\n        if abs(r) > abs(best_r):\n            best_lag, best_r, best_p = lag, r, p\n    return {\"peak_lag\": int(best_lag), \"r\": round(float(best_r), 4),\n            \"p_value\": round(float(best_p), 6), \"significant\": bool(best_p < 0.05)}\n\n\ndef main(data_dir):\n    series, n_gens = load_series(data_dir)\n    print(f\"Data: {data_dir}, {n_gens} generations\")\n    \n    # Check which downstreams are available\n    has_perplexity = not np.all(np.isnan(series.get(\"perplexity\", np.array([np.nan]))))\n    has_mauve = not np.all(np.isnan(series.get(\"mauve\", np.array([np.nan]))))\n    print(f\"Has perplexity: {has_perplexity}, Has mauve: {has_mauve}\")\n    \n    # Use common downstreams for fair comparison\n    downstreams = DOWNSTREAMS_COMMON\n    if has_mauve: downstreams = downstreams + [\"mauve\"]\n    print(f\"Using downstreams: {downstreams}\")\n    \n    print(f\"\\n{'='*100}\")\n    print(f\"{'Pair':<30} | {'TY_r5 sig':>10} {'TY_r5 p':>10} {'TY_r5 d_max':>12} | {'TY_ba sig':>10} {'TY_ba p':>10} {'TY_ba d_max':>12}\")\n    print(f\"{'-'*100}\")\n    \n    for cn in CANARIES:\n        for dn in downstreams:\n            c, d = series[cn], series[dn]\n            r5 = ty_granger_r5(c, d, cn, dn)\n            ba = ty_granger_ba(c, d, cn, dn)\n            r5_sig = r5.get(\"significant\", False)\n            r5_p = r5.get(\"p_raw\", r5.get(\"p_value\", \"N/A\"))\n            r5_dm = r5.get(\"d_max\", \"N/A\")\n            ba_sig = ba.get(\"significant\", False)\n            ba_p = ba.get(\"p_value\", \"N/A\")\n            ba_dm = ba.get(\"d_max\", \"N/A\")\n            match = \"==\" if r5_sig == ba_sig else \"!!\"\n            print(f\"{cn}->{dn:<15} | {str(r5_sig):>10} {str(r5_p):>10} {str(r5_dm):>12} | {str(ba_sig):>10} {str(ba_p):>10} {str(ba_dm):>12}  {match}\")\n    \n    print(f\"\\n{'='*100}\")\n    print(f\"{'Pair':<30} | {'diff_r5 lag':>12} {'diff_r5 p':>10} {'r5 sig':>7} | {'diff_ba lag':>12} {'diff_ba p':>10} {'ba sig':>7} | {'lag>0':>5} {'lag<0':>5}\")\n    print(f\"{'-'*100}\")\n    \n    for cn in CANARIES:\n        for dn in downstreams:\n            c, d = series[cn], series[dn]\n            r5 = diff_xcorr_impl(c, d, cn, dn, orient_r5)\n            ba = diff_xcorr_impl(c, d, cn, dn, orient_ba)\n            # For common metrics, orient should be the same (mauve only in BA)\n            lag_gt0 = \"Y\" if r5[\"peak_lag\"] > 0 else \"N\"\n            lag_lt0 = \"Y\" if r5[\"peak_lag\"] < 0 else \"N\"\n            print(f\"{cn}->{dn:<15} | {r5['peak_lag']:>12} {r5['p_value']:>10} {str(r5['significant']):>7} | {ba['peak_lag']:>12} {ba['p_value']:>10} {str(ba['significant']):>7} | {lag_gt0:>5} {lag_lt0:>5}\")\n    \n    # Count using both direction conventions\n    print(f\"\\n{'='*80}\")\n    print(\"Direction check impact on diff_xcorr counts:\")\n    r5_gt0 = sum(1 for cn in CANARIES for dn in downstreams\n                 if diff_xcorr_impl(series[cn], series[dn], cn, dn, orient_r5)[\"significant\"]\n                 and diff_xcorr_impl(series[cn], series[dn], cn, dn, orient_r5)[\"peak_lag\"] > 0)\n    r5_lt0 = sum(1 for cn in CANARIES for dn in downstreams\n                 if diff_xcorr_impl(series[cn], series[dn], cn, dn, orient_r5)[\"significant\"]\n                 and diff_xcorr_impl(series[cn], series[dn], cn, dn, orient_r5)[\"peak_lag\"] < 0)\n    print(f\"  peak_lag > 0 (run_5method convention, WRONG):  {r5_gt0}/{len(CANARIES)*len(downstreams)}\")\n    print(f\"  peak_lag < 0 (batch_analysis convention, CORRECT): {r5_lt0}/{len(CANARIES)*len(downstreams)}\")\n    \n    # TY counts\n    ty_r5_sig = sum(1 for cn in CANARIES for dn in downstreams\n                    if ty_granger_r5(series[cn], series[dn], cn, dn).get(\"significant\", False))\n    ty_ba_sig = sum(1 for cn in CANARIES for dn in downstreams\n                    if ty_granger_ba(series[cn], series[dn], cn, dn).get(\"significant\", False))\n    n_pairs = len(CANARIES) * len(downstreams)\n    print(f\"\\nTY Granger counts:\")\n    print(f\"  run_5method (F-test, AIC lag search): {ty_r5_sig}/{n_pairs}\")\n    print(f\"  batch_analysis (chi2, fixed lag=1):   {ty_ba_sig}/{n_pairs}\")\n\n\nif __name__ == \"__main__\":\n    data_dir = sys.argv[1] if len(sys.argv) > 1 else \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s43_fp32\"\n    main(data_dir)\nPYEOF\necho \"Script written\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T04:54:58.565566+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T04:54:58.565703+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python diagnostic_compare.py results/alpha_sweep/a060_s43_fp32",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python diagnostic_compare.py results/alpha_sweep/a060_s43_fp32",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T04:54:58.566041+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Data: results/alpha_sweep/a060_s43_fp32, 10 generations\\nHas perplexity: True, Has mauve: True\\nUsing downstreams: ['distinct_1', 'distinct_2', 'distinct_3', 'mauve']\\n\\n====================================================================================================\\nPair                           |  TY_r5 sig    TY_r5 p  TY_r5 d_max |  TY_ba sig    TY_ba p  TY_ba d_max\\n----------------------------------------------------------------------------------------------------\\ntoken_entropy->distinct_1      |      False        N/A            1 |      False   0.607472            1  ==\\ntoken_entropy->distinct_2      |      False        N/A            1 |       True   0.014429            1  !!\\ntoken_entropy->distinct_3      |      False   0.272216            1 |       True   0.028455            1  !!\\ntoken_entropy->mauve           |      False   0.966319            1 |      False    0.94033            1  ==\\nece->distinct_1      |      False   0.261278            0 |       True   0.003031            1  !!\\nece->distinct_2      |       True      2e-06            0 |      False   0.059939            1  !!\\nece->distinct_3      |       True      4e-06            0 |      False   0.579212            1  !!\\nece->mauve           |      False   0.154282            1 |       True   0.001964            1  !!\\n\\n====================================================================================================\\nPair                           |  diff_r5 lag  diff_r5 p  r5 sig |  diff_ba lag  diff_ba p  ba sig | lag>0 lag<0\\n----------------------------------------------------------------------------------------------------\\ntoken_entropy->distinct_1      |           -4   0.032913    True |           -4   0.032913    True |     N     Y\\ntoken_entropy->distinct_2      |           -5   0.029208    True |           -5   0.029208    True |     N     Y\\ntoken_entropy->distinct_3      |           -5   0.01819
…[truncated 1062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T04:54:58.566316+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json, numpy as np\nfrom statsmodels.tsa.stattools import adfuller\n\nwith open('results/alpha_sweep/a060_s43_fp32/all_metrics.json') as f:\n    data = sorted(json.load(f), key=lambda x: x['generation'])\n\nmetrics = ['token_entropy', 'ece', 'distinct_1', 'distinct_2', 'distinct_3', 'mauve']\nLOWER_IS_WORSE = {'token_entropy', 'distinct_1', 'distinct_2', 'distinct_3', 'mauve'}\nT = len(data)\nprint(f'T={T}')\nprint()\nprint(f'{\\\"Metric\\\":<20} {\\\"ADF_r5 (c) p\\\":>15} {\\\"d_max_r5\\\":>10} {\\\"ADF_ba (ct) p\\\":>15} {\\\"d_max_ba\\\":>10}')\nprint('-'*75)\nfor m in metrics:\n    raw = np.array([d.get(m, np.nan) for d in data], dtype=float)\n    s = -raw.copy() if m in LOWER_IS_WORSE else raw.copy()\n    # run_5method: default regression='c'\n    try:\n        adf_r5 = adfuller(s, maxlag=min(2, T//3-1))\n        p_r5 = adf_r5[1]\n        dm_r5 = 1 if p_r5 > 0.05 else 0\n    except Exception as e:\n        p_r5 = f'ERR:{e}'\n        dm_r5 = 'ERR'\n    # batch_analysis: regression='ct', autolag='AIC'\n    try:\n        adf_ba = adfuller(s, maxlag=min(3, T//3-1), regression='ct', autolag='AIC')\n        p_ba = adf_ba[1]\n        dm_ba_0 = 0 if p_ba < 0.05 else None\n        if dm_ba_0 is None:\n            ds = np.diff(s)\n            adf_ba2 = adfuller(ds, maxlag=min(3, len(ds)//3-1), regression='ct', autolag='AIC')\n            dm_ba = 1 if adf_ba2[1] < 0.05 else 2\n        else:\n            dm_ba = 0\n    except Exception as e:\n        p_ba = f'ERR:{e}'\n        dm_ba = 'ERR'\n    print(f'{m:<20} {str(round(p_r5,6) if isinstance(p_r5,float) else p_r5):>15} {str(dm_r5):>10} {str(round(p_ba,6) if isinstance(p_ba,float) else p_ba):>15} {str(dm_ba):>10}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json, numpy as np\nfrom statsmodels.tsa.stattools import adfuller\n\nwith open('results/alpha_sweep/a060_s43_fp32/all_metrics.json') as f:\n    data = sorted(json.load(f), key=lambda x: x['generation'])\n\nmetrics = ['token_entropy', 'ece', 'distinct_1', 'distinct_2', 'distinct_3', 'mauve']\nLOWER_IS_WORSE = {'token_entropy', 'distinct_1', 'distinct_2', 'distinct_3', 'mauve'}\nT = len(data)\nprint(f'T={T}')\nprint()\nprint(f'{\\\"Metric\\\":<20} {\\\"ADF_r5 (c) p\\\":>15} {\\\"d_max_r5\\\":>10} {\\\"ADF_ba (ct) p\\\":>15} {\\\"d_max_ba\\\":>10}')\nprint('-'*75)\nfor m in metrics:\n    raw = np.array([d.get(m, np.nan) for d in data], dtype=float)\n    s = -raw.copy() if m in LOWER_IS_WORSE else raw.copy()\n    # run_5method: default regression='c'\n    try:\n        adf_r5 = adfuller(s, maxlag=min(2, T//3-1))\n        p_r5 = adf_r5[1]\n        dm_r5 = 1 if p_r5 > 0.05 else 0\n    except Exception as e:\n        p_r5 = f'ERR:{e}'\n        dm_r5 = 'ERR'\n    # batch_analysis: regression='ct', autolag='AIC'\n    try:\n        adf_ba = adfuller(s, maxlag=min(3, T//3-1), regression='ct', autolag='AIC')\n        p_ba = adf_ba[1]\n        dm_ba_0 = 0 if p_ba < 0.05 else None\n        if dm_ba_0 is None:\n            ds = np.diff(s)\n            adf_ba2 = adfuller(ds, maxlag=min(3, len(ds)//3-1), regression='ct', autolag='AIC')\n            dm_ba = 1 if adf_ba2[1] < 0.05 else 2\n        else:\n            dm_ba = 0\n    except Exception as e:\n        p_ba = f'ERR:{e}'\n        dm_ba = 'ERR'\n    print(f'{m:<20} {str(round(p_r5,6) if isinstance(p_r5,float) else p_r5):>15} {str(dm_r5):>10} {str(round(p_ba,6) if isinstance(p_ba,float) else p_ba):>15} {str(dm_ba):>10}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T04:54:58.566489+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"T=10\\n\\nMetric                  ADF_r5 (c) p   d_max_r5   ADF_ba (ct) p   d_max_ba\\n---------------------------------------------------------------------------\\ntoken_entropy               0.998985          1 ERR:maxlag must be less than (nobs/2 - 1 - ntrend) where n trend is the number of included deterministic regressors        ERR\\nece                              0.0          0 ERR:maxlag must be less than (nobs/2 - 1 - ntrend) where n trend is the number of included deterministic regressors        ERR\\ndistinct_1                   4.9e-05          0 ERR:maxlag must be less than (nobs/2 - 1 - ntrend) where n trend is the number of included deterministic regressors        ERR\\ndistinct_2                  0.004512          0             0.0          0\\ndistinct_3                  0.028114          0 ERR:maxlag must be less than (nobs/2 - 1 - ntrend) where n trend is the number of included deterministic regressors        ERR\\nmauve                       0.982305          1             0.0          0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.33}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T04:54:58.566676+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python batch_analysis.py --exp_dir results/alpha_sweep/a060_s43_fp32 --output /tmp/ba_a060_s43.json 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python batch_analysis.py --exp_dir results/alpha_sweep/a060_s43_fp32 --output /tmp/ba_a060_s43.json 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T04:54:58.566831+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading data from results/alpha_sweep/a060_s43_fp32\\n  10 generations loaded\\nComputing drift...\\nRunning 5-method lead-lag analysis...\\nNo null_dirs provided, using simple K>=4 consensus as MMCT proxy\\n\\nSaved: /tmp/ba_a060_s43.json\\n\\n============================================================\\nSUMMARY: results/alpha_sweep/a060_s43_fp32\\n============================================================\\nGenerations: 10\\n\\nDrift (gen0->gen9):\\n  token_entropy       : -28.61%\\n  ece                 : +1530.81%\\n  perplexity          : +85.11%\\n  distinct_1          : -31.02%\\n  distinct_2          : -39.02%\\n  distinct_3          : -37.30%\\n  effective_rank      : +61.00%\\n  mauve               : -10.96%\\n\\nLead-lag (forward significant / total):\\n  naive_xcorr         : 1/8\\n  diff_xcorr          : 6/8\\n  threshold_onset     : 8/8\\n  perm_granger_fwd    : 0/8\\n  perm_granger_rev    : 0/8\\n  ty_granger          : 4/8\\n  consensus_k4        : 0/8\\n\\nMMCT: weighted_pair_forward, detection_rate=0.0\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.75}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T04:54:58.567119+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json\nwith open('/tmp/ba_a060_s43.json') as f:\n    data = json.load(f)\nfor p in data['pair_details']:\n    cn, dn = p['canary'], p['downstream']\n    r = p['results']\n    ty = r.get('ty_granger', {})\n    diff = r.get('diff_xcorr', {})\n    pg = r.get('perm_granger_fwd', {})\n    print(f'{cn}->{dn}:')\n    print(f'  TY: sig={ty.get(\\\"significant\\\")}, p={ty.get(\\\"p_value\\\")}, d_max={ty.get(\\\"d_max\\\")}, chi2={ty.get(\\\"chi2\\\")}')\n    print(f'  diff: sig={diff.get(\\\"significant\\\")}, sig_fdr={diff.get(\\\"significant_fdr\\\")}, p={diff.get(\\\"p_value\\\")}, p_fdr={diff.get(\\\"p_fdr\\\")}, peak_lag={diff.get(\\\"peak_lag\\\")}')\n    print(f'  PG: sig={pg.get(\\\"significant\\\")}, sig_fdr={pg.get(\\\"significant_fdr\\\")}, p={pg.get(\\\"p_value\\\")}, p_fdr={pg.get(\\\"p_fdr\\\")}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json\nwith open('/tmp/ba_a060_s43.json') as f:\n    data = json.load(f)\nfor p in data['pair_details']:\n    cn, dn = p['canary'], p['downstream']\n    r = p['results']\n    ty = r.get('ty_granger', {})\n    diff = r.get('diff_xcorr', {})\n    pg = r.get('perm_granger_fwd', {})\n    print(f'{cn}->{dn}:')\n    print(f'  TY: sig={ty.get(\\\"significant\\\")}, p={ty.get(\\\"p_value\\\")}, d_max={ty.get(\\\"d_max\\\")}, chi2={ty.get(\\\"chi2\\\")}')\n    print(f'  diff: sig={diff.get(\\\"significant\\\")}, sig_fdr={diff.get(\\\"significant_fdr\\\")}, p={diff.get(\\\"p_value\\\")}, p_fdr={diff.get(\\\"p_fdr\\\")}, peak_lag={diff.get(\\\"peak_lag\\\")}')\n    print(f'  PG: sig={pg.get(\\\"significant\\\")}, sig_fdr={pg.get(\\\"significant_fdr\\\")}, p={pg.get(\\\"p_value\\\")}, p_fdr={pg.get(\\\"p_fdr\\\")}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T04:54:58.567329+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"token_entropy->distinct_1:\\n  TY: sig=False, p=0.607472, d_max=1, chi2=0.2639\\n  diff: sig=True, sig_fdr=True, p=0.032913, p_fdr=0.043884, peak_lag=-4\\n  PG: sig=False, sig_fdr=False, p=0.061388, p_fdr=0.070158\\ntoken_entropy->distinct_2:\\n  TY: sig=True, p=0.014429, d_max=1, chi2=5.9849\\n  diff: sig=True, sig_fdr=True, p=0.029208, p_fdr=0.043884, peak_lag=-5\\n  PG: sig=True, sig_fdr=False, p=0.043591, p_fdr=0.069746\\ntoken_entropy->distinct_3:\\n  TY: sig=True, p=0.028455, d_max=1, chi2=4.8003\\n  diff: sig=True, sig_fdr=True, p=0.018191, p_fdr=0.039256, peak_lag=-5\\n  PG: sig=True, sig_fdr=False, p=0.025395, p_fdr=0.05119\\ntoken_entropy->mauve:\\n  TY: sig=False, p=0.94033, d_max=1, chi2=0.0056\\n  diff: sig=False, sig_fdr=False, p=0.097371, p_fdr=0.097371, peak_lag=5\\n  PG: sig=False, sig_fdr=False, p=0.084183, p_fdr=0.084183\\nece->distinct_1:\\n  TY: sig=True, p=0.003031, d_max=1, chi2=8.789\\n  diff: sig=True, sig_fdr=True, p=0.019628, p_fdr=0.039256, peak_lag=-4\\n  PG: sig=True, sig_fdr=False, p=0.025595, p_fdr=0.05119\\nece->distinct_2:\\n  TY: sig=False, p=0.059939, d_max=1, chi2=3.5391\\n  diff: sig=True, sig_fdr=True, p=0.014697, p_fdr=0.039256, peak_lag=-5\\n  PG: sig=True, sig_fdr=False, p=0.025195, p_fdr=0.05119\\nece->distinct_3:\\n  TY: sig=False, p=0.579212, d_max=1, chi2=0.3075\\n  diff: sig=True, sig_fdr=True, p=0.008077, p_fdr=0.039256, peak_lag=-5\\n  PG: sig=True, sig_fdr=False, p=0.022995, p_fdr=0.05119\\nece->mauve:\\n  TY: sig=True, p=0.001964, d_max=1, chi2=9.5833\\n  diff: sig=False, sig_fdr=False, p=0.08272, p_fdr=0.094537, peak_lag=5\\n  PG: sig=False, sig_fdr=False, p=0.057588, p_fdr=0.070158\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T04:54:58.567535+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, numpy as np\nfrom statsmodels.tsa.stattools import adfuller\n\nwith open('/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s43_fp32/all_metrics.json') as f:\n    data = sorted(json.load(f), key=lambda x: x['generation'])\n\nLOWER = {'token_entropy', 'distinct_1', 'distinct_2', 'distinct_3', 'mauve'}\nT = len(data)\n\nfor m in ['token_entropy', 'ece', 'distinct_1', 'distinct_2', 'distinct_3', 'mauve']:\n    raw = np.array([d.get(m, np.nan) for d in data], dtype=float)\n    s = -raw.copy() if m in LOWER else raw.copy()\n    print(f'{m} (T={len(s)}):')\n    # batch_analysis _determine_d_max logic\n    series = s.copy()\n    for d in range(3):\n        try:\n            maxl = min(3, len(series) // 3 - 1)\n            print(f'  d={d}, len={len(series)}, maxlag={maxl}')\n            result = adfuller(series, maxlag=maxl, regression='ct', autolag='AIC')\n            print(f'  ADF p={result[1]:.6f}, usedlag={result[2]}')\n            if result[1] < 0.05:\n                print(f'  => d_max={d}')\n                break\n            series = np.diff(series)\n        except Exception as e:\n            print(f'  EXCEPTION at d={d}: {e}')\n            print(f'  => d_max={d} (from exception)')\n            break\n    else:\n        print(f'  => d_max=2 (max)')\n    print()\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json, numpy as np\nfrom statsmodels.tsa.stattools import adfuller\n\nwith open('/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s43_fp32/all_metrics.json') as f:\n    data = sorted(json.load(f), key=lambda x: x['generation'])\n\nLOWER = {'token_entropy', 'distinct_1', 'distinct_2', 'distinct_3', 'mauve'}\nT = len(data)\n\nfor m in ['token_entropy', 'ece', 'distinct_1', 'distinct_2', 'distinct_3', 'mauve']:\n    raw = np.array([d.get(m, np.nan) for d in data], dtype=float)\n    s = -raw.copy() if m in LOWER else raw.copy()\n    print(f'{m} (T={len(s)}):')\n    # batch_analysis _determine_d_max logic\n    series = s.copy()\n    for d in range(3):\n        try:\n            maxl = min(3, len(series) // 3 - 1)\n            print(f'  d={d}, len={len(series)}, maxlag={maxl}')\n            result = adfuller(series, maxlag=maxl, regression='ct', autolag='AIC')\n            print(f'  ADF p={result[1]:.6f}, usedlag={result[2]}')\n            if result[1] < 0.05:\n                print(f'  => d_max={d}')\n                break\n            series = np.diff(series)\n        except Exception as e:\n            print(f'  EXCEPTION at d={d}: {e}')\n            print(f'  => d_max={d} (from exception)')\n            break\n    else:\n        print(f'  => d_max=2 (max)')\n    print()\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T04:54:58.567695+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"token_entropy (T=10):\\n  d=0, len=10, maxlag=2\\n  ADF p=1.000000, usedlag=2\\n  d=1, len=9, maxlag=2\\n  EXCEPTION at d=1: maxlag must be less than (nobs/2 - 1 - ntrend) where n trend is the number of included deterministic regressors\\n  => d_max=1 (from exception)\\n\\nece (T=10):\\n  d=0, len=10, maxlag=2\\n  ADF p=1.000000, usedlag=2\\n  d=1, len=9, maxlag=2\\n  EXCEPTION at d=1: maxlag must be less than (nobs/2 - 1 - ntrend) where n trend is the number of included deterministic regressors\\n  => d_max=1 (from exception)\\n\\ndistinct_1 (T=10):\\n  d=0, len=10, maxlag=2\\n  ADF p=0.098880, usedlag=2\\n  d=1, len=9, maxlag=2\\n  EXCEPTION at d=1: maxlag must be less than (nobs/2 - 1 - ntrend) where n trend is the number of included deterministic regressors\\n  => d_max=1 (from exception)\\n\\ndistinct_2 (T=10):\\n  d=0, len=10, maxlag=2\\n  ADF p=0.000000, usedlag=1\\n  => d_max=0\\n\\ndistinct_3 (T=10):\\n  d=0, len=10, maxlag=2\\n  ADF p=0.323249, usedlag=2\\n  d=1, len=9, maxlag=2\\n  EXCEPTION at d=1: maxlag must be less than (nobs/2 - 1 - ntrend) where n trend is the number of included deterministic regressors\\n  => d_max=1 (from exception)\\n\\nmauve (T=10):\\n  d=0, len=10, maxlag=2\\n  ADF p=0.000000, usedlag=2\\n  => d_max=0\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T04:54:58.567882+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python diagnostic_compare.py results/alpha_sweep/a050_s43_fp32",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python diagnostic_compare.py results/alpha_sweep/a050_s43_fp32",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T04:54:58.568045+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Data: results/alpha_sweep/a050_s43_fp32, 11 generations\\nHas perplexity: True, Has mauve: True\\nUsing downstreams: ['distinct_1', 'distinct_2', 'distinct_3', 'mauve']\\n\\n====================================================================================================\\nPair                           |  TY_r5 sig    TY_r5 p  TY_r5 d_max |  TY_ba sig    TY_ba p  TY_ba d_max\\n----------------------------------------------------------------------------------------------------\\ntoken_entropy->distinct_1      |       True   0.044899            1 |       True        0.0            0  ==\\ntoken_entropy->distinct_2      |      False    0.44895            1 |       True      4e-06            0  !!\\ntoken_entropy->distinct_3      |      False   0.992971            1 |      False   0.266176            2  ==\\ntoken_entropy->mauve           |      False   0.791076            1 |      False   0.661448            2  ==\\nece->distinct_1      |      False    0.05187            1 |       True    3.9e-05            1  !!\\nece->distinct_2      |      False   0.348714            1 |       True   0.005616            1  !!\\nece->distinct_3      |      False   0.335066            1 |       True        0.0            2  !!\\nece->mauve           |      False   0.334283            1 |      False   0.225058            2  ==\\n\\n====================================================================================================\\nPair                           |  diff_r5 lag  diff_r5 p  r5 sig |  diff_ba lag  diff_ba p  ba sig | lag>0 lag<0\\n----------------------------------------------------------------------------------------------------\\ntoken_entropy->distinct_1      |           -1      7e-06    True |           -1      7e-06    True |     N     Y\\ntoken_entropy->distinct_2      |           -1     0.0001    True |           -1     0.0001    True |     N     Y\\ntoken_entropy->distinct_3      |           -1   0.00299
…[truncated 1062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T04:54:58.568270+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__append_idea",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__append_idea",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T04:54:58.568414+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T04:54:58.568535+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ty_diff_investigation",
  "description": "Create investigation output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ty_diff_investigation",
    "description": "Create investigation output directory"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T04:54:58.568652+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T04:54:58.568800+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ty_diff_investigation/cross_script_comparison.md",
  "content": "# TY/diff_xcorr 跨脚本不一致 Root Cause 调查报告\n\n**日期**: 2026-05-20\n**状态**: P0 CRITICAL — 已定位 root cause\n**调查范围**: `run_5method_s43.py` vs `batch_analysis.py`\n**验证数据**: `alpha_sweep/a060_s43_fp32` (T=10), `alpha_sweep/a050_s43_fp32` (T=11)\n\n---\n\n## 1. 关键参数/方法差异表\n\n| 维度 | run_5method_s43.py | batch_analysis.py | 影响 |\n|------|-------------------|-------------------|------|\n| **DOWNSTREAMS** | distinct_1/2/3, **perplexity** | distinct_1/2/3, **mauve** | 8 pair 中 2 pair 完全不同 |\n| **LOWER_IS_WORSE** | 不含 mauve | 含 mauve | orient 方向不同（但 diff_xcorr 对称，不影响结果） |\n| **Direction check** | `peak_lag > 0` (**WRONG**, 违反 C009) | `peak_lag < 0` (正确) | naive/diff 计数完全反转 |\n| **TY ADF regression** | 默认 `\"c\"` (constant only) | `\"ct\"` (constant + trend) | d_max 判定不同 |\n| **TY ADF maxlag** | `min(2, T//3-1)` | `min(3, T//3-1)` | batch_analysis 在短序列上触发 bug |\n| **TY d_max 逻辑** | 简单 p>0.05→1, 封顶 1 | 迭代差分 _determine_d_max, 封顶 2 | **batch_analysis 有 bug**（见下） |\n| **TY lag 选择** | AIC 搜索 p∈{1,2} | 固定 max_lag=1 | 模型结构不同 |\n| **TY 检验统计量** | F-test: `F = ((RSS_r-RSS_u)/q) / (RSS_u/df)` | Wald χ²: `W = n*(RSS_r-RSS_u)/RSS_u` | 小样本下 F 更准确，χ² 是渐近的 |\n| **TY p-value 分布** | `stats.f.cdf(F, q, df_resid)` | `stats.chi2.cdf(W, q)` | 自由度处理完全不同 |\n| **PermG 实现** | 相同 | 相同 | **一致** |\n| **FDR 校正范围** | diff_xcorr, perm_granger | diff_xcorr, perm_granger_fwd, perm_granger_rev | 实质等价 |\n\n---\n\n## 2. Per-Pair 结果对比\n\n### 2.1 TY Granger (alpha_sweep/a060_s43_fp32, T=10)\n\n| Pair | r5 sig | r5 p | r5 d_max | ba sig | ba p | ba d_max | 一致? |\n|------|--------|------|----------|--------|------|----------|-------|\n| token_entropy→distinct_1 | False | N/A* | 1 | False | 0.607 | 1 | == |\n| token_entropy→distinct_2 | False | N/A* | 1 | **True** | 0.014 | 1 | **!!** |\n| token_entropy→distinct_3 | False | 0.272 | 1 | **True** | 0.028 | 1 | **!!** |\n| token_entropy→mauve | False | 0.966 | 1 | False | 0.940 | 1 | == |\n| ece→distinct_1 | False | 0.261 | **0** | **True** | 0.003 | **1** | **!!** |\n| ece→distinct_2 | **True** | **2e-6** | **0** | False | 0.060 | **1** | **!!** |\n| ece→distinct_3 | **True** | **4e-6** | **0** | False | 0.579 | **1** | **!!** |\n| ece→mauve | False | 0.154 | 1 | **True** | 0.002 | 1 | **!!** |\n\n\\*N/A = n too small (p_aug 过大导致残差自由度不足)\n\n**TY 计数**: run_5method = **2/8**, batch_analysis = **4/8** (6/8 pair 结果不同)\n\n### 2.2 TY Granger (alpha_sweep/a050_s43_fp32, T=11)\n\n| Pair | r5 sig | r5 p | r5 d_max | ba sig | ba p | ba d_max | 一致? |\n|------|--------|------|----------|--------|------|----------|-------|\n| token_entropy→distinct_1 | True | 0.045 | 1 | True | 0.000 | 0 | == |\n| token_entropy→distinct_2 | False | 0.449 | 1 | **True** | **4e-6** | 0 | **!!** |\n| token_entropy→distinct_3 | False | 0.993 | 1 | False | 0.266 | 2 | == |\n| token_entropy→mauve | False | 0.791 | 1 | False | 0.661 | 2 | == |\n| ece→distinct_1 | False | 0.052 | 1 | **True** | **4e-5** | 1 | **!!** |\n| ece→distinct_2 | False | 0.349 | 1 | **True** | 0.006 | 1 | **!!** |\n| ece→distinct_3 | False | 0.335 | 1 | **True** | **0.000** | 2 | **!!** |\n| ece→mauve | False | 0.334 | 1 | False | 0.225 | 2 | == |\n\n**TY 计数**: run_5method = **1/8**, batch_analysis = **5/8**\n\n### 2.3 diff_xcorr (两实验均确认)\n\n**Per-pair 结果完全一致** — 两套脚本的 diff_xcorr 核心计算（差分、pearsonr、peak_lag 选择）相同。计数差异 **100% 来自 direction check**：\n\n| 实验 | peak_lag > 0 (r5, WRONG) | peak_lag < 0 (ba, CORRECT) |\n|------|--------------------------|---------------------------|\n| a060_s43_fp32 | 0/8 | 6/8 |\n| a050_s43_fp32 | 0/8 | 6/8 |\n\nrun_5method 在这两个实验上 diff_xcorr 会报 **0/8**（因 forward 信号全在 lag<0），而 batch_analysis 报 **6/8**。\n\n---\n\n## 3. Root Cause 汇总\n\n### RC-1 (CRITICAL): DOWNSTREAMS 列表不同\n\n- `run_5method_s43.py`: distinct_1/2/3 + **perplexity**\n- `batch_analysis.py`: distinct_1/2/3 + **mauve**\n- 8 pair 中 2 pair（canary→perplexity vs canary→mauve）在不同数据上计算\n- 无法直接对比\n\n### RC-2 (CRITICAL): Direction check 符号反转 — 违反 C009/M035\n\n- `run_5method_s43.py` 共识计数: `(peak_lag or 0) > 0` → **反向因果**\n- `batch_analysis.py` 共识计数: `(peak_lag or 0) < 0` → **正向因果**（正确）\n- xcorr 约定: lag<0 = canary leads downstream = forward causation\n- 影响: naive_xcorr 和 diff_xcorr 的 forward significant 计数完全反转\n- 这是 D111/M035 sign reversal bug 的残留 — batch_analysis 已修正，run_5method 未修正\n\n### RC-3 (CRITICAL): TY Granger 实现完全不同\n\n**3a: ADF 回归类型**\n- run_5method: `regression=\"c\"` (constant) → ece 等单调序列容易判为平稳 (d_max=0)\n- batch_analysis: `regression=\"ct\"` (constant+trend) → 更保守，有 trend 的序列更难拒绝单位根\n\n**3b: _determine_d_max BUG（batch_analysis）**\n\n```\n_determine_d_max 流程 (T=10):\n  d=0: ADF(T=10, maxlag=2, ct) → 成功, p>0.05 → 差分\n  d=1: ADF(T=9, maxlag=2, ct) → CRASH!\n       约束: maxlag < nobs/2 - 1 - ntrend = 9/2 - 1 - 2 = 1.5\n       maxlag=2 > 1.5 → ValueError\n  except → return d=1  ← 不是真正的平稳性判定!\n```\n\n大多数 metric 获得 d_max=1 是因为 **ADF 异常被静默吞掉**，不是因为真正需要一阶差分。\n\n**3c: Lag 阶数选择**\n- run_5method: AIC 选择 p∈{1,2}，可能选 p=2 → 更多参数、更高拟合\n- batch_analysis: 固定 max_lag=1 → 更简约\n\n**3d: 检验统计量**\n- run_5method: F-test（有限样本精确分布）\n- batch_analysis: Wald χ²（渐近分布）\n- T=10-11 远未达到 χ² 渐近条件，两者 p-value 可差 1-2 个数量级\n\n### RC-4: 为什么 PermG 一致\n\n1. **代码路径相同**: 两套脚本的 `perm_granger()` / `_granger_f_stat()` / `_build_lag_matrix()` 实现完全一致\n2. **参数相同**: max_lag=1, n_perm=5000, seed=42, difference=True\n3. **无 direction filter**: PermG 天然有方向性（测试 x→y），不需要 peak_lag 方向判定\n4. **不依赖 ADF/d_max**: 内部自行差分，避开了 ADF 不一致问题\n5. **FDR 校正一致**: 两套都对 PermG p-value 做 BH FDR\n\n---\n\n## 4. 推荐\n\n### 4.1 选择哪套脚本\n\n**batch_analysis.py 更接近正确**，但仍有 bug 需修：\n\n| 项目 | run_5method_s43.py | batch_analysis.py |\n|------|-------------------|-------------------|\n| Direction check | ✗ (peak_lag>0, 违反 C009) | ✓ (peak_lag<0) |\n| DOWNSTREAMS | ✗ (用 perplexity，不含 mauve) | ✓ (用 mauve) |\n| TY d_max | 简单但无 bug | **有 _determine_d_max 异常 bug** |\n| TY test stat | F-test（小样本更优） | χ²（渐近，T≤11 不适用） |\n| 通用性 | 硬编码路径/实验 | 参数化 CLI |\n\n### 4.2 需要修复的问题\n\n1. **[P0] 废弃 run_5method_s43.py** — 方向错误、downstreams 错误、硬编码路径。不应再用于任何分析\n2. **[P0] 修复 batch_analysis.py 的 _determine_d_max bug**:\n   ```python\n   # 修正: 考虑 regression=\"ct\" 的 ntrend=2 约束\n   def _determine_d_max(series, max_d=2, alpha=0.05):\n       for d in range(max_d + 1):\n           try:\n               nobs = len(series)\n               ntrend = 2  # \"ct\" = constant + trend\n               safe_maxlag = max(1, nobs // 2 - 1 - ntrend - 1)\n               result = adfuller(series, maxlag=safe_maxlag,\n                                 regression=\"ct\", autolag=\"AIC\")\n               if result[1] < alpha:\n                   return d\n               series = np.diff(series)\n           except Exception:\n               return min(d, 1)  # fallback 但不超过 1\n       return max_d\n   ```\n3. **[P1] TY 检验统计量**: 对 T≤15 的短序列，改用 F-test 代替 χ²，或直接标注 TY 为 \"underpowered\"\n4. **[P2] 考虑 TY 降级**: 鉴于 C003 已确认 TY 在低 α 下种子不稳定，且 _determine_d_max 有系统性 bug，建议 K≥3 投票中降低 TY 权重或排除\n\n### 4.3 对 K≥3 投票的影响评估\n\n| 方法 | 可信度 | 问题 |\n|------|--------|------|\n| **PermG** | ✓ 高 | 两套脚本一致，无 direction/ADF 依赖 |\n| **threshold_onset** | ✓ 中高 | 两套实现一致（D105 3σ 标准另行校验） |\n| **diff_xcorr** | ⚠ 依赖脚本 | 核心计算一致，但 run_5method 方向错误导致计数反转 |\n| **naive_xcorr** | ⚠ 依赖脚本 | 同上 |\n| **TY Granger** | ✗ 不可信 | 两套实现给出相反结论，batch_analysis 有 d_max bug，run_5method 有方向 bug |\n\n**结论**: 使用 run_5method 产出的任何包含 TY 或 diff/naive direction check 的 K≥3 数值**全部不可信**。batch_analysis 的 diff_xcorr 和 PermG 可信，但 TY 需修 bug 后重跑。\n\n**K≥3 修正策略**:\n- 短期: K≥3 仅基于 PermG + threshold_onset + diff_xcorr (batch_analysis 版)，3 method 中 K≥2 为显著\n- 中期: 修复 _determine_d_max 后重跑 TY，恢复 5-method 投票\n\n---\n\n## 5. 附录: 诊断脚本\n\n诊断脚本位于服务器: `/root/autodl-tmp/distrib_canary_collapse/diagnostic_compare.py`\n\n运行方式:\n```bash\npython diagnostic_compare.py results/alpha_sweep/a060_s43_fp32\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ty_diff_investigation/cross_script_comparison.md",
    "content": "# TY/diff_xcorr 跨脚本不一致 Root Cause 调查报告\n\n**日期**: 2026-05-20\n**状态**: P0 CRITICAL — 已定位 root cause\n**调查范围**: `run_5method_s43.py` vs `batch_analysis.py`\n**验证数据**: `alpha_sweep/a060_s43_fp32` (T=10), `alpha_sweep/a050_s43_fp32` (T=11)\n\n---\n\n## 1. 关键参数/方法差异表\n\n| 维度 | run_5method_s43.py | batch_analysis.py | 影响 |\n|------|-------------------|-------------------|------|\n| **DOWNSTREAMS** | distinct_1/2/3, **perplexity** | distinct_1/2/3, **mauve** | 8 pair 中 2 pair 完全不同 |\n| **LOWER_IS_WORSE** | 不含 mauve | 含 mauve | orient 方向不同（但 diff_xcorr 对称，不影响结果） |\n| **Direction check** | `peak_lag > 0` (**WRONG**, 违反 C009) | `peak_lag < 0` (正确) | naive/diff 计数完全反转 |\n| **TY ADF regression** | 默认 `\"c\"` (constant only) | `\"ct\"` (constant + trend) | d_max 判定不同 |\n| **TY ADF maxlag** | `min(2, T//3-1)` | `min(3, T//3-1)` | batch_analysis 在短序列上触发 bug |\n| **TY d_max 逻辑** | 简单 p>0.05→1, 封顶 1 | 迭代差分 _determine_d_max, 封顶 2 | **batch_analysis 有 bug**（见下） |\n| **TY lag 选择** | AIC 搜索 p∈{1,2} | 固定 max_lag=1 | 模型结构不同 |\n| **TY 检验统计量** | F-test: `F = ((RSS_r-RSS_u)/q) / (RSS_u/df)` | Wald χ²: `W = n*(RSS_r-RSS_u)/RSS_u` | 小样本下 F 更准确，χ² 是渐近的 |\n| **TY p-value 分布** | `stats.f.cdf(F, q, df_resid)` | `stats.chi2.cdf(W, q)` | 自由度处理完全不同 |\n| **PermG 实现** | 相同 | 相同 | **一致** |\n| **FDR 校正范围** | diff_xcorr, perm_granger | diff_xcorr, perm_granger_fwd, perm_granger_rev | 实质等价 |\n\n---\n\n## 2. Per-Pair 结果对比\n\n### 2.1 TY Granger (alpha_sweep/a060_s43_fp32, T=10)\n\n| Pair | r5 sig | r5 p | r5 d_max | ba sig | ba p | ba d_max | 一致? |\n|------|--------|------|----------|--------|------|----------|-------|\n| token_entropy→distinct_1 | False | N/A* | 1 | False | 0.607 | 1 | == |\n| token_entropy→distinct_2 | False | N/A* | 1 | **True** | 0.014 | 1 | **!!** |\n| token_entropy→distinct_3 | False | 0.272 | 1 | **True** | 0.028 | 1 | **!!** |\n| token_entropy→mauve | False | 0.966 | 1 | False | 0.940 | 1 | == |\n| ece→distinct_1 | False | 0.261 | **0** | **True** | 0.003 | **1** | **!!** |\n| ece→distinct_2 | **True** | **2e-6** | **0** | False | 0.060 | **1** | **!!** |\n| ece→distinct_3 | **True** | **4e-6** | **0** | False | 0.579 | **1** | **!!** |\n| ece→mauve | False | 0.154 | 1 | **True** | 0.002 | 1 | **!!** |\n\n\\*N/A = n too small (p_aug 过大导致残差自由度不足)\n\n**TY 计数**: run_5method = **2/8**, batch_analysis = **4/8** (6/8 pair 结果不同)\n\n### 2.2 TY Granger (alpha_sweep/a050_s43_fp32, T=11)\n\n| Pair | r5 sig | r5 p | r5 d_max | ba sig | ba p | ba d_max | 一致? |\n|------|--------|------|----------|--------|------|----------|-------|\n| token_entropy→distinct_1 | True | 0.045 | 1 | True | 0.000 | 0 | == |\n| token_entropy→distinct_2 | False | 0.449 | 1 | **True** | **4e-6** | 0 | **!!** |\n| token_entropy→distinct_3 | False | 0.993 | 1 | False | 0.266 | 2 | == |\n| token_entropy→mauve | False | 0.791 | 1 | False | 0.661 | 2 | == |\n| ece→distinct_1 | False | 0.052 | 1 | **True** | **4e-5** | 1 | **!!** |\n| ece→distinct_2 | False | 0.349 | 1 | **True** | 0.006 | 1 | **!!** |\n| ece→distinct_3 | False | 0.335 | 1 | **True** | **0.000** | 2 | **!!** |\n| ece→mauve | False | 0.334 | 1 | False | 0.225 | 2 | == |\n\n**TY 计数**: run_5method = **1/8**, batch_analysis = **5/8**\n\n### 2.3 diff_xcorr (两实验均确认)\n\n**Per-pair 结果完全一致** — 两套脚本的 diff_xcorr 核心计算（差分、pearsonr、peak_lag 选择）相同。计数差异 **100% 来自 direction check**：\n\n| 实验 | peak_lag > 0 (r5, WRONG) | peak_lag < 0 (ba, CORRECT) |\n|------|--------------------------|---------------------------|\n| a060_s43_fp32 | 0/8 | 6/8 |\n| a050_s43_fp32 | 0/8 | 6/8 |\n\nrun_5method 在这两个实验上 diff_xcorr 会报 **0/8**（因 forward 信号全在 lag<0），而 batch_analysis 报 **6/8**。\n\n---\n\n## 3. Root Cause 汇总\n\n### RC-1 (CRITICAL): DOWNSTREAMS 列表不同\n\n- `run_5method_s43.py`: distinct_1/2/3 + **perplexity**\n- `batch_analysis.py`: distinct_1/2/3 + **mauve**\n- 8 pair 中 2 pair（canary→perplexity vs canary→mauve）在不同数据上计算\n- 无法直接对比\n\n### RC-2 (CRITICAL): Direction check 符号反转 — 违反 C009/M035\n\n- `run_5method_s43.py` 共识计数: `(peak_lag or 0) > 0` → **反向因果**\n- `batch_analysis.py` 共识计数: `(peak_lag or 0) < 0` → **正向因果**（正确）\n- xcorr 约定: lag<0 = canary leads downstream = forward causation\n- 影响: naive_xcorr 和 diff_xcorr 的 forward significant 计数完全反转\n- 这是 D111/M035 sign reversal bug 的残留 — batch_analysis 已修正，run_5method 未修正\n\n### RC-3 (CRITICAL): TY Granger 实现完全不同\n\n**3a: ADF 回归类型**\n- run_5method: `regression=\"c\"` (constant) → ece 等单调序列容易判为平稳 (d_max=0)\n- batch_analysis: `regression=\"ct\"` (constant+trend) → 更保守，有 trend 的序列更难拒绝单位根\n\n**3b: _determine_d_max BUG（batch_analysis）**\n\n```\n_determine_d_max 流程 (T=10):\n  d=0: ADF(T=10, maxlag=2, ct) → 成功, p>0.05 → 差分\n  d=1: ADF(T=9, maxlag=2, ct) → CRASH!\n       约束: maxlag < nobs/2 - 1 - ntrend = 9/2 - 1 - 2 = 1.5\n       maxlag=2 > 1.5 → ValueError\n  except → return d=1  ← 不是真正的平稳性判定!\n```\n\n大多数 metric 获得 d_max=1 是因为 **ADF 异常被静默吞掉**，不是因为真正需要一阶差分。\n\n**3c: Lag 阶数选择**\n- run_5method: AIC 选择 p∈{1,2}，可能选 p=2 → 更多参数、更高拟合\n- batch_analysis: 固定 max_lag=1 → 更简约\n\n**3d: 检验统计量**\n- run_5method: F-test（有限样本精确分布）\n- batch_analysis: Wald χ²（渐近分布）\n- T=10-11 远未达到 χ² 渐近条件，两者 p-value 可差 1-2 个数量级\n\n### RC-4: 为什么 PermG 一致\n\n1. **代码路径相同**: 两套脚本的 `perm_granger()` / `_granger_f_stat()` / `_build_lag_matrix()` 实现完全一致\n2. **参数相同**: max_lag=1, n_perm=5000, seed=42, difference=True\n3. **无 direction filter**: PermG 天然有方向性（测试 x→y），不需要 peak_lag 方向判定\n4. **不依赖 ADF/d_max**: 内部自行差分，避开了 ADF 不一致问题\n5. **FDR 校正一致**: 两套都对 PermG p-value 做 BH FDR\n\n---\n\n## 4. 推荐\n\n### 4.1 选择哪套脚本\n\n**batch_analysis.py 更接近正确**，但仍有 bug 需修：\n\n| 项目 | run_5method_s43.py | batch_analysis.py |\n|------|-------------------|-------------------|\n| Direction check | ✗ (peak_lag>0, 违反 C009) | ✓ (peak_lag<0) |\n| DOWNSTREAMS | ✗ (用 perplexity，不含 mauve) | ✓ (用 mauve) |\n| TY d_max | 简单但无 bug | **有 _determine_d_max 异常 bug** |\n| TY test stat | F-test（小样本更优） | χ²（渐近，T≤11 不适用） |\n| 通用性 | 硬编码路径/实验 | 参数化 CLI |\n\n### 4.2 需要修复的问题\n\n1. **[P0] 废弃 run_5method_s43.py** — 方向错误、downstreams 错误、硬编码路径。不应再用于任何分析\n2. **[P0] 修复 batch_analysis.py 的 _determine_d_max bug**:\n   ```python\n   # 修正: 考虑 regression=\"ct\" 的 ntrend=2 约束\n   def _determine_d_max(series, max_d=2, alpha=0.05):\n       for d in range(max_d + 1):\n           try:\n               nobs = len(series)\n               ntrend = 2  # \"ct\" = constant + trend\n               safe_maxlag = max(1, nobs // 2 - 1 - ntrend - 1)\n               result = adfuller(series, maxlag=safe_maxlag,\n                                 regression=\"ct\", autolag=\"AIC\")\n               if result[1] < alpha:\n                   return d\n               series = np.diff(series)\n           except Exception:\n               return min(d, 1)  # fallback 但不超过 1\n       return max_d\n   ```\n3. **[P1] TY 检验统计量**: 对 T≤15 的短序列，改用 F-test 代替 χ²，或直接标注 TY 为 \"underpowered\"\n4. **[P2] 考虑 TY 降级**: 鉴于 C003 已确认 TY 在低 α 下种子不稳定，且 _determine_d_max 有系统性 bug，建议 K≥3 投票中降低 TY 权重或排除\n\n### 4.3 对 K≥3 投票的影响评估\n\n| 方法 | 可信度 | 问题 |\n|------|--------|------|\n| **PermG** | ✓ 高 | 两套脚本一致，无 direction/ADF 依赖 |\n| **threshold_onset** | ✓ 中高 | 两套实现一致（D105 3σ 标准另行校验） |\n| **diff_xcorr** | ⚠ 依赖脚本 | 核心计算一致，但 run_5method 方向错误导致计数反转 |\n| **naive_xcorr** | ⚠ 依赖脚本 | 同上 |\n| **TY Granger** | ✗ 不可信 | 两套实现给出相反结论，batch_analysis 有 d_max bug，run_5method 有方向 bug |\n\n**结论**: 使用 run_5method 产出的任何包含 TY 或 diff/naive direction check 的 K≥3 数值**全部不可信**。batch_analysis 的 diff_xcorr 和 PermG 可信，但 TY 需修 bug 后重跑。\n\n**K≥3 修正策略**:\n- 短期: K≥3 仅基于 PermG + threshold_onset + diff_xcorr (batch_analysis 版)，3 method 中 K≥2 为显著\n- 中期: 修复 _determine_d_max 后重跑 TY，恢复 5-method 投票\n\n---\n\n## 5. 附录: 诊断脚本\n\n诊断脚本位于服务器: `/root/autodl-tmp/distrib_canary_collapse/diagnostic_compare.py`\n\n运行方式:\n```bash\npython diagnostic_compare.py results/alpha_sweep/a060_s43_fp32\n```\n"
  }
}
````

</details>

---

### Tool result

_source line 58 · 2026-05-20T04:54:58.569041+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/ty_diff_investigation/cross_script_comparison.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T04:54:58.569422+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T04:54:58.569602+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T04:54:58.569750+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T04:54:58.569892+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-20T04:54:58.570025+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "+artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "+artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-20T04:54:58.570180+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-20T04:54:58.570343+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "mcp agent-ml-research",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "mcp agent-ml-research",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-20T04:54:58.570483+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-20T04:54:58.570675+00:00_

`register_artifact` 工具不可用。报告已写入 artifacts 目录。

调查完成。以下是核心发现：

---

## Root Cause 总结

**3 个关键 root cause 导致 TY/diff 跨脚本不一致：**

### RC-1: DOWNSTREAMS 列表不同
- `run_5method_s43.py` 用 `perplexity`，`batch_analysis.py` 用 `mauve`
- 8 pair 中 2 pair 在完全不同的数据上计算

### RC-2: Direction check 符号反转（最大影响）
- `run_5method_s43.py`: `peak_lag > 0` — **错误**，违反 C009/M035
- `batch_analysis.py`: `peak_lag < 0` — 正确
- 实测: peak_lag>0 → 0/8，peak_lag<0 → 6/8。diff_xcorr 核心计算完全一致，计数差异 100% 来自方向判定

### RC-3: TY Granger 实现完全不同（4 处分歧）
1. **ADF regression**: `"c"` vs `"ct"` → d_max 判定不同
2. **`_determine_d_max` bug (batch_analysis)**: T=10 时 ADF 在差分后序列上因 maxlag 违反 `regression="ct"` 约束而 crash，异常被静默捕获返回 d_max=1 — 不是真正的平稳性判定
3. **Lag 选择**: AIC 搜索 {1,2} vs 固定 1
4. **检验统计量**: F-test vs Wald χ²（T≤11 时差异巨大）

实测 TY 计数：a060_s43 上 run_5method=2/8 vs batch_analysis=4/8，6/8 pair 结论相反

### PermG 一致的原因
代码路径完全相同、参数相同、不依赖 ADF/direction filter

## 影响与建议
- **run_5method_s43.py 应废弃**（方向错误、downstreams 错误、硬编码路径）
- **batch_analysis.py 的 `_determine_d_max` 需修 bug**（maxlag 未考虑 ct 约束）
- **K≥3 投票**：TY 不可信，短期建议仅基于 PermG + threshold_onset + diff_xcorr (batch_analysis)

报告位于: `artifacts/ty_diff_investigation/cross_script_comparison.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_investigate_ty_diff_cross_script_20260520T044639"
}
```

</details>

---
