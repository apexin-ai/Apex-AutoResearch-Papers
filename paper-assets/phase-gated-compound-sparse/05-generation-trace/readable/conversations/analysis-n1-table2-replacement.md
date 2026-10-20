# analysis n1 table2 replacement

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/chats/worker_analysis_n1_table2_replacement_20260515T113907.jsonl`
- **Structured JSON:** [`1d7aae8a7ac662132ff8.json`](../../sessions/1d/1d7aae8a7ac662132ff8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

21 recorded events

### Tool call

_source line 1 · 2026-05-15T11:41:33.400048+00:00_

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
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
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

_source line 2 · 2026-05-15T11:41:33.400399+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T11:41:33.400615+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "ls -d /root/autodl-tmp/pacs/profiling_output_n500_bf16_*",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "ls -d /root/autodl-tmp/pacs/profiling_output_n500_bf16_*",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T11:41:33.400773+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s015\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s020\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s025\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s030\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_rand_s015\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_rand_s020\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_rand_s025\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_rand_s030\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_qw_imp_s015\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_qw_imp_s020\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_qw_imp_s025\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_qw_imp_s030\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_qw_rand_s015\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_qw_rand_s020\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_qw_rand_s025\\n/root/autodl-tmp/pacs/profiling_output_n500_bf16_qw_rand_s030\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.25}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T11:41:33.400910+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_analysis/crossover_all_sparsity.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_analysis/crossover_all_sparsity.csv"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T11:41:33.401041+00:00_

1	model,sparsity,phase,imp_median,imp_ci_lo,imp_ci_hi,rand_median,rand_ci_lo,rand_ci_hi,diff_median,diff_ci_lo,diff_ci_hi,wilcoxon_p,significant,n
2	deepseek,s015,high,0.002946,0.001192,0.005001,0.083326,0.065059,0.098782,0.087300,0.063454,0.107986,0.000000,yes,496
3	deepseek,s015,low,0.352830,0.318855,0.391251,0.088911,0.072531,0.114714,0.260726,0.212264,0.316819,0.000000,yes,500
4	deepseek,s020,high,0.007754,0.003370,0.011420,0.270200,0.241218,0.324652,0.258850,0.226714,0.316763,0.000000,yes,496
5	deepseek,s020,low,1.198240,1.089282,1.303709,0.349124,0.302835,0.440463,0.733340,0.598388,0.868002,0.000000,yes,500
6	deepseek,s025,high,0.021203,0.016759,0.026641,1.113415,1.020394,1.292353,1.037503,0.909390,1.140881,0.000000,yes,496
7	deepseek,s025,low,3.970990,3.476264,4.405446,1.498281,1.229960,1.709960,2.213629,1.590189,2.883303,0.000000,yes,500
8	deepseek,s030,high,0.037857,0.032560,0.047639,3.112067,2.697992,3.607944,2.856017,2.403335,3.572314,0.000000,yes,496
9	deepseek,s030,low,8.456054,7.779761,9.762422,3.839887,3.224448,4.425942,4.735251,3.260817,6.004473,0.000000,yes,500
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T11:41:33.401195+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-22162",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s025/profiling_results.json')); print(list(d.keys())); pii=d['per_problem_ii']; print(type(pii), len(pii)); print(list(pii[0].keys()) if isinstance(pii, list) else 'dict')\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-22162",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/pacs/profiling_output_n500_bf16_ds_imp_s025/profiling_results.json')); print(list(d.keys())); pii=d['per_problem_ii']; print(type(pii), len(pii)); print(list(pii[0].keys()) if isinstance(pii, list) else 'dict')\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T11:41:33.401333+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T11:41:33.401481+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "cd /root/autodl-tmp/pacs && python3 -c \"\nimport json\nd = json.load(open('profiling_output_n500_bf16_ds_imp_s025/profiling_results.json'))\nprint('Keys:', list(d.keys()))\npii = d['per_problem_ii']\nprint('Type:', type(pii).__name__, 'Len:', len(pii))\nif isinstance(pii, list):\n    print('First item keys:', list(pii[0].keys()))\n    print('First item:', {k: type(v).__name__ for k, v in pii[0].items()})\n    print('Sample:', pii[0])\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "cd /root/autodl-tmp/pacs && python3 -c \"\nimport json\nd = json.load(open('profiling_output_n500_bf16_ds_imp_s025/profiling_results.json'))\nprint('Keys:', list(d.keys()))\npii = d['per_problem_ii']\nprint('Type:', type(pii).__name__, 'Len:', len(pii))\nif isinstance(pii, list):\n    print('First item keys:', list(pii[0].keys()))\n    print('First item:', {k: type(v).__name__ for k, v in pii[0].items()})\n    print('Sample:', pii[0])\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T11:41:33.401613+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Keys: ['config', 'phase_stats', 'perplexity', 'interaction_index', 'pass_fail', 'warnings', 'diagnostics', 'per_problem_ii']\\nType: dict Len: 1\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T11:41:33.401733+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "cd /root/autodl-tmp/pacs && python3 -c \"\nimport json\nd = json.load(open('profiling_output_n500_bf16_ds_imp_s025/profiling_results.json'))\npii = d['per_problem_ii']\nprint('per_problem_ii keys:', list(pii.keys()))\nfor k, v in pii.items():\n    print(f'  {k}: type={type(v).__name__}, len={len(v) if hasattr(v, \\\"__len__\\\") else \\\"N/A\\\"}')\n    if isinstance(v, list) and len(v) > 0:\n        print(f'    sample[0]={v[0]}')\n        print(f'    sample[-1]={v[-1]}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "cd /root/autodl-tmp/pacs && python3 -c \"\nimport json\nd = json.load(open('profiling_output_n500_bf16_ds_imp_s025/profiling_results.json'))\npii = d['per_problem_ii']\nprint('per_problem_ii keys:', list(pii.keys()))\nfor k, v in pii.items():\n    print(f'  {k}: type={type(v).__name__}, len={len(v) if hasattr(v, \\\"__len__\\\") else \\\"N/A\\\"}')\n    if isinstance(v, list) and len(v) > 0:\n        print(f'    sample[0]={v[0]}')\n        print(f'    sample[-1]={v[-1]}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T11:41:33.401860+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"per_problem_ii keys: ['0.25']\\n  0.25: type=list, len=500\\n    sample[0]={'problem_idx': 0, 'problem_id': 'test/precalculus/807.json', 'ii_high': 0.11944170210517191, 'n_segments_high': 5, 'ii_mid': None, 'n_segments_mid': 0, 'ii_low': 18.380367128699447, 'n_segments_low': 2}\\n    sample[-1]={'problem_idx': 499, 'problem_id': 'test/geometry/615.json', 'ii_high': -0.00686203639209837, 'n_segments_high': 3, 'ii_mid': 2.9469390637881965, 'n_segments_mid': 1, 'ii_low': 7.241771483969739, 'n_segments_low': 6}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.62}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T11:41:33.402050+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "cat > /root/autodl-tmp/pacs/extract_table2.py << 'PYEOF'\nimport json, os, numpy as np\nfrom pathlib import Path\n\nnp.random.seed(42)\nB = 10000\nBASE = Path(\"/root/autodl-tmp/pacs\")\n\nmodels = [(\"ds\", \"DS\"), (\"qw\", \"QW\")]\nstrategies = [(\"imp\", \"imp\"), (\"rand\", \"rand\")]\nsparsities = [(\"s015\", \"0.15\"), (\"s020\", \"0.20\"), (\"s025\", \"0.25\"), (\"s030\", \"0.30\")]\n\ndef bootstrap_ci(arr, B=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    n = len(arr)\n    boots = np.array([np.median(rng.choice(arr, size=n, replace=True)) for _ in range(B)])\n    lo, hi = np.percentile(boots, [2.5, 97.5])\n    return np.median(arr), lo, hi\n\ndef wilcoxon_p(x, y):\n    from scipy.stats import wilcoxon\n    try:\n        stat, p = wilcoxon(x - y)\n        return p\n    except:\n        return float('nan')\n\nrows = []\nfor m_key, m_name in models:\n    for st_key, st_name in strategies:\n        for sp_key, sp_val in sparsities:\n            dirname = f\"profiling_output_n500_bf16_{m_key}_{st_key}_{sp_key}\"\n            fpath = BASE / dirname / \"profiling_results.json\"\n            if not fpath.exists():\n                print(f\"MISSING: {fpath}\")\n                continue\n            d = json.load(open(fpath))\n            pii = d[\"per_problem_ii\"]\n            sparsity_key = list(pii.keys())[0]\n            items = pii[sparsity_key]\n            \n            ii_high = np.array([x[\"ii_high\"] for x in items if x[\"ii_high\"] is not None])\n            ii_low = np.array([x[\"ii_low\"] for x in items if x[\"ii_low\"] is not None])\n            \n            # Paired: only problems with both\n            paired_mask = [(x[\"ii_high\"] is not None and x[\"ii_low\"] is not None) for x in items]\n            ii_h_paired = np.array([x[\"ii_high\"] for x, m in zip(items, paired_mask) if m])\n            ii_l_paired = np.array([x[\"ii_low\"] for x, m in zip(items, paired_mask) if m])\n            \n            # D = ii_low - ii_high\n            D = ii_l_paired - ii_h_paired\n            \n            # Per-phase medians\n            med_high, ci_h_lo, ci_h_hi = bootstrap_ci(ii_h_paired, B)\n            med_low, ci_l_lo, ci_l_hi = bootstrap_ci(ii_l_paired, B)\n            med_D, ci_d_lo, ci_d_hi = bootstrap_ci(D, B)\n            \n            # G = ii_low / ii_high, filter |ii_high| > 0.001\n            g_mask = np.abs(ii_h_paired) > 0.001\n            if g_mask.sum() > 0:\n                G = ii_l_paired[g_mask] / ii_h_paired[g_mask]\n                med_G, ci_g_lo, ci_g_hi = bootstrap_ci(G, B)\n                n_g = int(g_mask.sum())\n            else:\n                med_G = ci_g_lo = ci_g_hi = float('nan')\n                n_g = 0\n            \n            # Wilcoxon\n            p = wilcoxon_p(ii_l_paired, ii_h_paired)\n            \n            rows.append({\n                \"model\": m_name, \"strategy\": st_name, \"sparsity\": sp_val,\n                \"n_paired\": len(ii_h_paired),\n                \"ii_high_med\": med_high, \"ii_high_ci_lo\": ci_h_lo, \"ii_high_ci_hi\": ci_h_hi,\n                \"ii_low_med\": med_low, \"ii_low_ci_lo\": ci_l_lo, \"ii_low_ci_hi\": ci_l_hi,\n                \"D_med\": med_D, \"D_ci_lo\": ci_d_lo, \"D_ci_hi\": ci_d_hi,\n                \"G_med\": med_G, \"G_ci_lo\": ci_g_lo, \"G_ci_hi\": ci_g_hi, \"n_G\": n_g,\n                \"p_value\": p,\n            })\n\n# Print table\nprint(\"\\n\" + \"=\"*160)\nprint(\"Table 2 (n=500): Per-Phase Interaction Index — Full Results\")\nprint(\"=\"*160)\nheader = f\"{'Model':<6} {'Strat':<6} {'Spar':<6} {'n':>4} | {'II_high median':>14} {'[CI]':>24} | {'II_low median':>14} {'[CI]':>24} | {'D median':>10} {'[CI]':>24} | {'G median':>10} {'[CI]':>24} {'n_G':>5} | {'p-value':>12}\"\nprint(header)\nprint(\"-\"*160)\n\nfor r in rows:\n    line = (\n        f\"{r['model']:<6} {r['strategy']:<6} {r['sparsity']:<6} {r['n_paired']:>4} | \"\n        f\"{r['ii_high_med']:>14.6f} [{r['ii_high_ci_lo']:>10.6f}, {r['ii_high_ci_hi']:>10.6f}] | \"\n        f\"{r['ii_low_med']:>14.6f} [{r['ii_low_ci_lo']:>10.6f}, {r['ii_low_ci_hi']:>10.6f}] | \"\n        f\"{r['D_med']:>10.6f} [{r['D_ci_lo']:>10.6f}, {r['D_ci_hi']:>10.6f}] | \"\n        f\"{r['G_med']:>10.4f} [{r['G_ci_lo']:>10.4f}, {r['G_ci_hi']:>10.4f}] {r['n_G']:>5} | \"\n        f\"{r['p_value']:>12.2e}\"\n    )\n    print(line)\n\n# Also print CSV\nprint(\"\\n\\nCSV FORMAT:\")\nprint(\"model,strategy,sparsity,n_paired,ii_high_med,ii_high_ci_lo,ii_high_ci_hi,ii_low_med,ii_low_ci_lo,ii_low_ci_hi,D_med,D_ci_lo,D_ci_hi,G_med,G_ci_lo,G_ci_hi,n_G,p_value\")\nfor r in rows:\n    print(f\"{r['model']},{r['strategy']},{r['sparsity']},{r['n_paired']},{r['ii_high_med']:.6f},{r['ii_high_ci_lo']:.6f},{r['ii_high_ci_hi']:.6f},{r['ii_low_med']:.6f},{r['ii_low_ci_lo']:.6f},{r['ii_low_ci_hi']:.6f},{r['D_med']:.6f},{r['D_ci_lo']:.6f},{r['D_ci_hi']:.6f},{r['G_med']:.4f},{r['G_ci_lo']:.4f},{r['G_ci_hi']:.4f},{r['n_G']},{r['p_value']:.2e}\")\n\n# Qwen s025 per-phase comparison (importance vs random)\nprint(\"\\n\\n\" + \"=\"*80)\nprint(\"Qwen s025: Importance vs Random per-phase comparison\")\nprint(\"=\"*80)\nfor phase in [\"high\", \"low\"]:\n    imp_path = BASE / \"profiling_output_n500_bf16_qw_imp_s025\" / \"profiling_results.json\"\n    rand_path = BASE / \"profiling_output_n500_bf16_qw_rand_s025\" / \"profiling_results.json\"\n    d_imp = json.load(open(imp_path))\n    d_rand = json.load(open(rand_path))\n    items_imp = d_imp[\"per_problem_ii\"][list(d_imp[\"per_problem_ii\"].keys())[0]]\n    items_rand = d_rand[\"per_problem_ii\"][list(d_rand[\"per_problem_ii\"].keys())[0]]\n    \n    key = f\"ii_{phase}\"\n    vals_imp = np.array([x[key] for x in items_imp if x[key] is not None])\n    vals_rand = np.array([x[key] for x in items_rand if x[key] is not None])\n    \n    med_imp, ci_imp_lo, ci_imp_hi = bootstrap_ci(vals_imp, B)\n    med_rand, ci_rand_lo, ci_rand_hi = bootstrap_ci(vals_rand, B)\n    \n    print(f\"\\nPhase {phase}:\")\n    print(f\"  Importance: median={med_imp:.6f} [{ci_imp_lo:.6f}, {ci_imp_hi:.6f}] (n={len(vals_imp)})\")\n    print(f\"  Random:     median={med_rand:.6f} [{ci_rand_lo:.6f}, {ci_rand_hi:.6f}] (n={len(vals_rand)})\")\n    print(f\"  Diff (imp-rand): {med_imp - med_rand:.6f}\")\n\nPYEOF\necho \"Script written.\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "cat > /root/autodl-tmp/pacs/extract_table2.py << 'PYEOF'\nimport json, os, numpy as np\nfrom pathlib import Path\n\nnp.random.seed(42)\nB = 10000\nBASE = Path(\"/root/autodl-tmp/pacs\")\n\nmodels = [(\"ds\", \"DS\"), (\"qw\", \"QW\")]\nstrategies = [(\"imp\", \"imp\"), (\"rand\", \"rand\")]\nsparsities = [(\"s015\", \"0.15\"), (\"s020\", \"0.20\"), (\"s025\", \"0.25\"), (\"s030\", \"0.30\")]\n\ndef bootstrap_ci(arr, B=10000, seed=42):\n    rng = np.random.RandomState(seed)\n    n = len(arr)\n    boots = np.array([np.median(rng.choice(arr, size=n, replace=True)) for _ in range(B)])\n    lo, hi = np.percentile(boots, [2.5, 97.5])\n    return np.median(arr), lo, hi\n\ndef wilcoxon_p(x, y):\n    from scipy.stats import wilcoxon\n    try:\n        stat, p = wilcoxon(x - y)\n        return p\n    except:\n        return float('nan')\n\nrows = []\nfor m_key, m_name in models:\n    for st_key, st_name in strategies:\n        for sp_key, sp_val in sparsities:\n            dirname = f\"profiling_output_n500_bf16_{m_key}_{st_key}_{sp_key}\"\n            fpath = BASE / dirname / \"profiling_results.json\"\n            if not fpath.exists():\n                print(f\"MISSING: {fpath}\")\n                continue\n            d = json.load(open(fpath))\n            pii = d[\"per_problem_ii\"]\n            sparsity_key = list(pii.keys())[0]\n            items = pii[sparsity_key]\n            \n            ii_high = np.array([x[\"ii_high\"] for x in items if x[\"ii_high\"] is not None])\n            ii_low = np.array([x[\"ii_low\"] for x in items if x[\"ii_low\"] is not None])\n            \n            # Paired: only problems with both\n            paired_mask = [(x[\"ii_high\"] is not None and x[\"ii_low\"] is not None) for x in items]\n            ii_h_paired = np.array([x[\"ii_high\"] for x, m in zip(items, paired_mask) if m])\n            ii_l_paired = np.array([x[\"ii_low\"] for x, m in zip(items, paired_mask) if m])\n            \n            # D = ii_low - ii_high\n            D = ii_l_paired - ii_h_paired\n            \n            # Per-phase medians\n            med_high, ci_h_lo, ci_h_hi = bootstrap_ci(ii_h_paired, B)\n            med_low, ci_l_lo, ci_l_hi = bootstrap_ci(ii_l_paired, B)\n            med_D, ci_d_lo, ci_d_hi = bootstrap_ci(D, B)\n            \n            # G = ii_low / ii_high, filter |ii_high| > 0.001\n            g_mask = np.abs(ii_h_paired) > 0.001\n            if g_mask.sum() > 0:\n                G = ii_l_paired[g_mask] / ii_h_paired[g_mask]\n                med_G, ci_g_lo, ci_g_hi = bootstrap_ci(G, B)\n                n_g = int(g_mask.sum())\n            else:\n                med_G = ci_g_lo = ci_g_hi = float('nan')\n                n_g = 0\n            \n            # Wilcoxon\n            p = wilcoxon_p(ii_l_paired, ii_h_paired)\n            \n            rows.append({\n                \"model\": m_name, \"strategy\": st_name, \"sparsity\": sp_val,\n                \"n_paired\": len(ii_h_paired),\n                \"ii_high_med\": med_high, \"ii_high_ci_lo\": ci_h_lo, \"ii_high_ci_hi\": ci_h_hi,\n                \"ii_low_med\": med_low, \"ii_low_ci_lo\": ci_l_lo, \"ii_low_ci_hi\": ci_l_hi,\n                \"D_med\": med_D, \"D_ci_lo\": ci_d_lo, \"D_ci_hi\": ci_d_hi,\n                \"G_med\": med_G, \"G_ci_lo\": ci_g_lo, \"G_ci_hi\": ci_g_hi, \"n_G\": n_g,\n                \"p_value\": p,\n            })\n\n# Print table\nprint(\"\\n\" + \"=\"*160)\nprint(\"Table 2 (n=500): Per-Phase Interaction Index — Full Results\")\nprint(\"=\"*160)\nheader = f\"{'Model':<6} {'Strat':<6} {'Spar':<6} {'n':>4} | {'II_high median':>14} {'[CI]':>24} | {'II_low median':>14} {'[CI]':>24} | {'D median':>10} {'[CI]':>24} | {'G median':>10} {'[CI]':>24} {'n_G':>5} | {'p-value':>12}\"\nprint(header)\nprint(\"-\"*160)\n\nfor r in rows:\n    line = (\n        f\"{r['model']:<6} {r['strategy']:<6} {r['sparsity']:<6} {r['n_paired']:>4} | \"\n        f\"{r['ii_high_med']:>14.6f} [{r['ii_high_ci_lo']:>10.6f}, {r['ii_high_ci_hi']:>10.6f}] | \"\n        f\"{r['ii_low_med']:>14.6f} [{r['ii_low_ci_lo']:>10.6f}, {r['ii_low_ci_hi']:>10.6f}] | \"\n        f\"{r['D_med']:>10.6f} [{r['D_ci_lo']:>10.6f}, {r['D_ci_hi']:>10.6f}] | \"\n        f\"{r['G_med']:>10.4f} [{r['G_ci_lo']:>10.4f}, {r['G_ci_hi']:>10.4f}] {r['n_G']:>5} | \"\n        f\"{r['p_value']:>12.2e}\"\n    )\n    print(line)\n\n# Also print CSV\nprint(\"\\n\\nCSV FORMAT:\")\nprint(\"model,strategy,sparsity,n_paired,ii_high_med,ii_high_ci_lo,ii_high_ci_hi,ii_low_med,ii_low_ci_lo,ii_low_ci_hi,D_med,D_ci_lo,D_ci_hi,G_med,G_ci_lo,G_ci_hi,n_G,p_value\")\nfor r in rows:\n    print(f\"{r['model']},{r['strategy']},{r['sparsity']},{r['n_paired']},{r['ii_high_med']:.6f},{r['ii_high_ci_lo']:.6f},{r['ii_high_ci_hi']:.6f},{r['ii_low_med']:.6f},{r['ii_low_ci_lo']:.6f},{r['ii_low_ci_hi']:.6f},{r['D_med']:.6f},{r['D_ci_lo']:.6f},{r['D_ci_hi']:.6f},{r['G_med']:.4f},{r['G_ci_lo']:.4f},{r['G_ci_hi']:.4f},{r['n_G']},{r['p_value']:.2e}\")\n\n# Qwen s025 per-phase comparison (importance vs random)\nprint(\"\\n\\n\" + \"=\"*80)\nprint(\"Qwen s025: Importance vs Random per-phase comparison\")\nprint(\"=\"*80)\nfor phase in [\"high\", \"low\"]:\n    imp_path = BASE / \"profiling_output_n500_bf16_qw_imp_s025\" / \"profiling_results.json\"\n    rand_path = BASE / \"profiling_output_n500_bf16_qw_rand_s025\" / \"profiling_results.json\"\n    d_imp = json.load(open(imp_path))\n    d_rand = json.load(open(rand_path))\n    items_imp = d_imp[\"per_problem_ii\"][list(d_imp[\"per_problem_ii\"].keys())[0]]\n    items_rand = d_rand[\"per_problem_ii\"][list(d_rand[\"per_problem_ii\"].keys())[0]]\n    \n    key = f\"ii_{phase}\"\n    vals_imp = np.array([x[key] for x in items_imp if x[key] is not None])\n    vals_rand = np.array([x[key] for x in items_rand if x[key] is not None])\n    \n    med_imp, ci_imp_lo, ci_imp_hi = bootstrap_ci(vals_imp, B)\n    med_rand, ci_rand_lo, ci_rand_hi = bootstrap_ci(vals_rand, B)\n    \n    print(f\"\\nPhase {phase}:\")\n    print(f\"  Importance: median={med_imp:.6f} [{ci_imp_lo:.6f}, {ci_imp_hi:.6f}] (n={len(vals_imp)})\")\n    print(f\"  Random:     median={med_rand:.6f} [{ci_rand_lo:.6f}, {ci_rand_hi:.6f}] (n={len(vals_rand)})\")\n    print(f\"  Diff (imp-rand): {med_imp - med_rand:.6f}\")\n\nPYEOF\necho \"Script written.\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T11:41:33.402253+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T11:41:33.402378+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "cd /root/autodl-tmp/pacs && python3 extract_table2.py",
  "account": "root",
  "timeout": "300000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "cd /root/autodl-tmp/pacs && python3 extract_table2.py",
    "account": "root",
    "timeout": "300000"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T11:41:33.402526+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/autodl-tmp/pacs && python3 extract_table2.py'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\nTraceback (most recent call last):\\n  File \\\"/root/autodl-tmp/pacs/extract_table2.py\\\", line 1, in &lt;module>\\n    import json, os, numpy as np\\nModuleNotFoundError: No module named 'numpy'\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T11:41:33.402648+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-22162",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 extract_table2.py",
  "account": "root",
  "timeout": "300000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-22162",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/pacs && python3 extract_table2.py",
    "account": "root",
    "timeout": "300000"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T11:41:33.402854+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n================================================================================================================================================================\\nTable 2 (n=500): Per-Phase Interaction Index — Full Results\\n================================================================================================================================================================\\nModel  Strat  Spar      n | II_high median                     [CI] |  II_low median                     [CI] |   D median                     [CI] |   G median                     [CI]   n_G |      p-value\\n----------------------------------------------------------------------------------------------------------------------------------------------------------------\\nDS     imp    0.15    496 |       0.002946 [  0.001192,   0.005001] |       0.357210 [  0.319581,   0.397639] |   0.390717 [  0.349625,   0.443113] |     7.4529 [    4.0978,    11.3624]   475 |     1.27e-70\\nDS     imp    0.20    496 |       0.007754 [  0.003370,   0.011420] |       1.211376 [  1.095412,   1.321248] |   1.214882 [  1.107179,   1.336492] |    17.9049 [   12.7448,    26.3073]   481 |     3.98e-75\\nDS     imp    0.25    496 |       0.021203 [  0.017005,   0.026712] |       3.970990 [  3.476176,   4.405446] |   3.985748 [  3.527160,   4.358754] |    49.0639 [   40.0936,    57.8341]   482 |     1.99e-78\\nDS     imp    0.30    496 |       0.037857 [  0.032560,   0.047639] |       8.456054 [  7.779761,   9.762422] |   8.481292 [  7.754269,   9.691932] |    79.7854 [   63.3276,    96.5117]   487 |     1.09e-79\\nDS     rand   0.15    496 |       0.083326 [  0.065059,   0.098782] |       0.089844 [  0.074080,   0.116304] |   0.013885 [ -0.016685,   0.038949] |     0.5174 [    0.3993,     0.6073]   493 |     8.63e-01\\nDS     rand   0.20    496 |       0.270200 [  0.241218,   0.324652] |       0.356754 [  0.305338,   0.444246] |   0.031471 [ -0.011224, 
…[truncated 5181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T11:41:33.403023+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_analysis/table2_n500_full.csv",
  "content": "model,strategy,sparsity,n_paired,ii_high_med,ii_high_ci_lo,ii_high_ci_hi,ii_low_med,ii_low_ci_lo,ii_low_ci_hi,D_med,D_ci_lo,D_ci_hi,G_med,G_ci_lo,G_ci_hi,n_G,p_value\nDS,imp,0.15,496,0.002946,0.001192,0.005001,0.357210,0.319581,0.397639,0.390717,0.349625,0.443113,7.4529,4.0978,11.3624,475,1.27e-70\nDS,imp,0.20,496,0.007754,0.003370,0.011420,1.211376,1.095412,1.321248,1.214882,1.107179,1.336492,17.9049,12.7448,26.3073,481,3.98e-75\nDS,imp,0.25,496,0.021203,0.017005,0.026712,3.970990,3.476176,4.405446,3.985748,3.527160,4.358754,49.0639,40.0936,57.8341,482,1.99e-78\nDS,imp,0.30,496,0.037857,0.032560,0.047639,8.456054,7.779761,9.762422,8.481292,7.754269,9.691932,79.7854,63.3276,96.5117,487,1.09e-79\nDS,rand,0.15,496,0.083326,0.065059,0.098782,0.089844,0.074080,0.116304,0.013885,-0.016685,0.038949,0.5174,0.3993,0.6073,493,8.63e-01\nDS,rand,0.20,496,0.270200,0.241218,0.324652,0.356754,0.305338,0.444246,0.031471,-0.011224,0.076722,0.7594,0.6496,0.8884,492,2.80e-01\nDS,rand,0.25,496,1.113415,1.020394,1.285834,1.514330,1.236963,1.735700,0.257376,0.126460,0.349785,1.0917,0.9640,1.1948,496,1.46e-03\nDS,rand,0.30,496,3.112067,2.697992,3.607944,3.847827,3.271552,4.481792,0.509626,0.260063,0.890944,1.1487,1.0499,1.2737,496,1.48e-03\nQW,imp,0.15,475,-0.000222,-0.001158,0.000231,0.044056,0.026927,0.062631,0.065910,0.049182,0.092494,0.2065,-0.1867,0.9010,411,8.66e-15\nQW,imp,0.20,475,0.000402,-0.000487,0.001256,0.274640,0.231415,0.326553,0.307299,0.261247,0.356382,2.6103,0.4692,5.0804,427,6.84e-42\nQW,imp,0.25,475,0.004090,0.001893,0.006625,1.053156,0.958889,1.183328,1.074494,0.976606,1.178658,9.4605,5.2186,14.8349,445,1.06e-68\nQW,imp,0.30,475,0.013763,0.009016,0.017461,3.208350,2.797857,3.633680,3.154970,2.798602,3.558180,36.8778,25.3153,49.1356,458,9.21e-74\nQW,rand,0.15,475,0.094092,0.079942,0.109279,0.096917,0.071911,0.119265,-0.011055,-0.038979,0.012407,0.6722,0.4414,0.7779,469,1.72e-01\nQW,rand,0.20,475,0.291458,0.257989,0.337912,0.356306,0.307436,0.430076,0.015276,-0.014526,0.068399,0.8833,0.7440,1.0189,472,2.00e-01\nQW,rand,0.25,475,1.107759,0.995054,1.356483,1.768842,1.511061,2.052440,0.393110,0.236047,0.552889,1.2580,1.1724,1.3718,471,1.59e-11\nQW,rand,0.30,475,2.818713,2.511955,3.377254,4.252661,3.658381,5.247021,0.912682,0.613397,1.258428,1.2986,1.1979,1.3924,472,2.92e-15\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_analysis/table2_n500_full.csv",
    "content": "model,strategy,sparsity,n_paired,ii_high_med,ii_high_ci_lo,ii_high_ci_hi,ii_low_med,ii_low_ci_lo,ii_low_ci_hi,D_med,D_ci_lo,D_ci_hi,G_med,G_ci_lo,G_ci_hi,n_G,p_value\nDS,imp,0.15,496,0.002946,0.001192,0.005001,0.357210,0.319581,0.397639,0.390717,0.349625,0.443113,7.4529,4.0978,11.3624,475,1.27e-70\nDS,imp,0.20,496,0.007754,0.003370,0.011420,1.211376,1.095412,1.321248,1.214882,1.107179,1.336492,17.9049,12.7448,26.3073,481,3.98e-75\nDS,imp,0.25,496,0.021203,0.017005,0.026712,3.970990,3.476176,4.405446,3.985748,3.527160,4.358754,49.0639,40.0936,57.8341,482,1.99e-78\nDS,imp,0.30,496,0.037857,0.032560,0.047639,8.456054,7.779761,9.762422,8.481292,7.754269,9.691932,79.7854,63.3276,96.5117,487,1.09e-79\nDS,rand,0.15,496,0.083326,0.065059,0.098782,0.089844,0.074080,0.116304,0.013885,-0.016685,0.038949,0.5174,0.3993,0.6073,493,8.63e-01\nDS,rand,0.20,496,0.270200,0.241218,0.324652,0.356754,0.305338,0.444246,0.031471,-0.011224,0.076722,0.7594,0.6496,0.8884,492,2.80e-01\nDS,rand,0.25,496,1.113415,1.020394,1.285834,1.514330,1.236963,1.735700,0.257376,0.126460,0.349785,1.0917,0.9640,1.1948,496,1.46e-03\nDS,rand,0.30,496,3.112067,2.697992,3.607944,3.847827,3.271552,4.481792,0.509626,0.260063,0.890944,1.1487,1.0499,1.2737,496,1.48e-03\nQW,imp,0.15,475,-0.000222,-0.001158,0.000231,0.044056,0.026927,0.062631,0.065910,0.049182,0.092494,0.2065,-0.1867,0.9010,411,8.66e-15\nQW,imp,0.20,475,0.000402,-0.000487,0.001256,0.274640,0.231415,0.326553,0.307299,0.261247,0.356382,2.6103,0.4692,5.0804,427,6.84e-42\nQW,imp,0.25,475,0.004090,0.001893,0.006625,1.053156,0.958889,1.183328,1.074494,0.976606,1.178658,9.4605,5.2186,14.8349,445,1.06e-68\nQW,imp,0.30,475,0.013763,0.009016,0.017461,3.208350,2.797857,3.633680,3.154970,2.798602,3.558180,36.8778,25.3153,49.1356,458,9.21e-74\nQW,rand,0.15,475,0.094092,0.079942,0.109279,0.096917,0.071911,0.119265,-0.011055,-0.038979,0.012407,0.6722,0.4414,0.7779,469,1.72e-01\nQW,rand,0.20,475,0.291458,0.257989,0.337912,0.356306,0.307436,0.430076,0.015276,-0.014526,0.068399,0.8833,0.7440,1.0189,472,2.00e-01\nQW,rand,0.25,475,1.107759,0.995054,1.356483,1.768842,1.511061,2.052440,0.393110,0.236047,0.552889,1.2580,1.1724,1.3718,471,1.59e-11\nQW,rand,0.30,475,2.818713,2.511955,3.377254,4.252661,3.658381,5.247021,0.912682,0.613397,1.258428,1.2986,1.1979,1.3924,472,2.92e-15\n"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T11:41:33.403170+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_analysis/table2_n500_full.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-15T11:41:33.403341+00:00_

全部 16 conditions 数据提取完毕。CSV 已存 `artifacts/n500_analysis/table2_n500_full.csv`。

---

**Table 2 (n=500) 关键结果**

**Importance masking — 强 phase-gating 效应：**

| Model | s | II_high median | II_low median | D median | G median | p |
|-------|------|----------------|---------------|----------|----------|------|
| DS | 0.15 | 0.003 [0.001, 0.005] | 0.357 [0.320, 0.398] | 0.391 [0.350, 0.443] | 7.5× [4.1, 11.4] | 1.3e-70 |
| DS | 0.20 | 0.008 [0.003, 0.011] | 1.211 [1.095, 1.321] | 1.215 [1.107, 1.336] | 17.9× [12.7, 26.3] | 4.0e-75 |
| DS | 0.25 | 0.021 [0.017, 0.027] | 3.971 [3.476, 4.405] | 3.986 [3.527, 4.359] | 49.1× [40.1, 57.8] | 2.0e-78 |
| DS | 0.30 | 0.038 [0.033, 0.048] | 8.456 [7.780, 9.762] | 8.481 [7.754, 9.692] | 79.8× [63.3, 96.5] | 1.1e-79 |
| QW | 0.15 | -0.000 [-0.001, 0.000] | 0.044 [0.027, 0.063] | 0.066 [0.049, 0.092] | 0.2× [-0.2, 0.9] | 8.7e-15 |
| QW | 0.20 | 0.000 [-0.000, 0.001] | 0.275 [0.231, 0.327] | 0.307 [0.261, 0.356] | 2.6× [0.5, 5.1] | 6.8e-42 |
| QW | 0.25 | 0.004 [0.002, 0.007] | 1.053 [0.959, 1.183] | 1.074 [0.977, 1.179] | 9.5× [5.2, 14.8] | 1.1e-68 |
| QW | 0.30 | 0.014 [0.009, 0.017] | 3.208 [2.798, 3.634] | 3.155 [2.799, 3.558] | 36.9× [25.3, 49.1] | 9.2e-74 |

**Random masking — 无 phase-gating（flat）：**

| Model | s | II_high median | II_low median | D median | G median | p |
|-------|------|----------------|---------------|----------|----------|------|
| DS | 0.15 | 0.083 | 0.090 | 0.014 [-0.017, 0.039] | 0.52× | 0.86 |
| DS | 0.20 | 0.270 | 0.357 | 0.031 [-0.011, 0.077] | 0.76× | 0.28 |
| DS | 0.25 | 1.113 | 1.514 | 0.257 [0.126, 0.350] | 1.09× | 1.5e-3 |
| DS | 0.30 | 3.112 | 3.848 | 0.510 [0.260, 0.891] | 1.15× | 1.5e-3 |
| QW | 0.15 | 0.094 | 0.097 | -0.011 [-0.039, 0.012] | 0.67× | 0.17 |
| QW | 0.20 | 0.291 | 0.356 | 0.015 [-0.015, 0.068] | 0.88× | 0.20 |
| QW | 0.25 | 1.108 | 1.769 | 0.393 [0.236, 0.553] | 1.26× | 1.6e-11 |
| QW | 0.30 | 2.819 | 4.253 | 0.913 [0.613, 1.258] | 1.30× | 2.9e-15 |

**Qwen s025 crossover 检验（importance vs random per phase）：**
- Phase high: imp=0.004 vs rand=1.109 → random 的 II_high 远大于 importance（差 -1.10）
- Phase low: imp=1.043 vs rand=1.770 → random 的 II_low 也大于 importance（差 -0.73）
- Qwen 无 crossover：random 在两个 phase 的 II 都高于 importance，不像 DS 那样 high-phase random > importance 但 low-phase importance > random。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_n1_table2_replacement_20260515T113907"
}
```

</details>

---
