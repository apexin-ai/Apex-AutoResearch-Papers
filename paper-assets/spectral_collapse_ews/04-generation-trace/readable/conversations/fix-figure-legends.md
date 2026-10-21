# fix figure legends

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_fix_figure_legends_20260523T064838.jsonl`
- **Structured JSON:** [`5267fcc6eae6e8cec809.json`](../../sessions/52/5267fcc6eae6e8cec809.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-23T06:49:50.956944+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T06:49:50.957240+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T06:49:50.957395+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx6000-diagprobe",
  "command": "find /root/spectral_collapse_ews -name \"*.py\" -path \"*/scripts/*\" -o -name \"*.py\" -path \"*/figures/*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx6000-diagprobe",
    "command": "find /root/spectral_collapse_ews -name \"*.py\" -path \"*/scripts/*\" -o -name \"*.py\" -path \"*/figures/*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-23T06:49:50.957525+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx6000-diagprobe",
  "command": "find /root/spectral_collapse_ews -name \"*.py\" -exec grep -l \"spectral_trajectory\\|phase_diagram\" {} \\;",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx6000-diagprobe",
    "command": "find /root/spectral_collapse_ews -name \"*.py\" -exec grep -l \"spectral_trajectory\\|phase_diagram\" {} \\;",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-23T06:49:50.957685+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/spectral_collapse_ews/scripts/plot_spectral_trajectory.py\\n/root/spectral_collapse_ews/scripts/dry_run_d014.py\\n/root/spectral_collapse_ews/scripts/compute_alternative_ews.py\\n/root/spectral_collapse_ews/scripts/compute_alternative_ews_v2.py\\n/root/spectral_collapse_ews/scripts/plot_phase_diagram.py\\n/root/spectral_collapse_ews/scripts/compute_second_order_ews.py\\n/root/spectral_collapse_ews/scripts/compute_controller_activation.py\\n/root/spectral_collapse_ews/scripts/compare_seeds.py\\n/root/spectral_collapse_ews/scripts/benchmark_slv_timing.py\\n/root/spectral_collapse_ews/scripts/n_sensitivity.py\\n/root/spectral_collapse_ews/scripts/n_sensitivity_offline.py\\n/root/spectral_collapse_ews/scripts/collect_phase_table_stats.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T06:49:50.957818+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T06:49:50.957949+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx6000-diagprobe",
  "command": "cat /root/spectral_collapse_ews/scripts/plot_spectral_trajectory.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx6000-diagprobe",
    "command": "cat /root/spectral_collapse_ews/scripts/plot_spectral_trajectory.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T06:49:50.958128+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import json\\nimport numpy as np\\nimport matplotlib\\nmatplotlib.use('Agg')\\nimport matplotlib.pyplot as plt\\nimport matplotlib.gridspec as gridspec\\nfrom pathlib import Path\\n\\nROOT = Path(\\\"/root/spectral_collapse_ews\\\")\\n\\ndata = {\\n    'generation': [0, 1, 2, 3, 4, 5, 6, 7],\\n    'eff_rank': [417.55, 491.77, 496.44, 493.31, 485.67, 479.21, 473.00, 464.20],\\n    'log_det': [2366.68, 2464.76, 2469.93, 2440.57, 2405.05, 2370.17, 2335.17, 2304.19],\\n    'ppl': [9.55, 11.38, 13.58, 16.25, 19.80, 24.59, 30.91, 38.89],\\n    'distinct4': [0.7414, 0.6256, 0.5154, 0.4900, 0.4679, 0.4630, 0.4655, 0.4474],\\n    'hellaswag': [0.4130, 0.3897, 0.3764, 0.3658, 0.3558, 0.3439],\\n}\\n\\ntry:\\n    with open(ROOT / \\\"results\\\" / \\\"phase0_results.json\\\") as f:\\n        records = json.load(f)\\n    if len(records) >= 1:\\n        data['generation'] = [r['generation'] for r in records]\\n        data['eff_rank'] = [r.get('effective_rank', 0) for r in records]\\n        data['log_det'] = [r.get('log_det', 0) for r in records]\\n        data['ppl'] = [r.get('perplexity', 0) for r in records]\\n        data['distinct4'] = [r.get('distinct_4', 0) for r in records]\\nexcept Exception:\\n    pass\\n\\ngens = np.array(data['generation'])\\neff_rank = np.array(data['eff_rank'])\\nlog_det = np.array(data['log_det'])\\nppl = np.array(data['ppl'])\\ndistinct4 = np.array(data['distinct4'])\\nhellaswag = np.array(data['hellaswag'])\\nhella_gens = np.arange(len(hellaswag))\\n\\nCOLOR = '#1f77b4'\\nBASELINE_COLOR = '#888888'\\nPEAK_COLOR = '#d62728'\\nMARKER = 'o'\\nMS = 5\\nLW = 1.8\\n\\nplt.rcParams.update({\\n    'font.size': 9,\\n    'axes.labelsize': 10,\\n    'axes.titlesize': 10,\\n    'xtick.labelsize': 8,\\n    'ytick.labelsize': 8,\\n})\\n\\nfig = plt.figure(figsize=(10, 6.5))\\ngs = gridspec.GridSpec(2, 6, figure=fig, hspace=0.38, wspace=0.8)\\n\\nax_rank = fig.add_subplot(gs[0, 0:2])\\nax_logdet = fig.ad
…[truncated 3796 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T06:49:50.958279+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx6000-diagprobe",
  "command": "cat /root/spectral_collapse_ews/scripts/plot_phase_diagram.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx6000-diagprobe",
    "command": "cat /root/spectral_collapse_ews/scripts/plot_phase_diagram.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T06:49:50.958453+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Phase diagram: SLV trajectories across mixing ratios with type annotations.\\\"\\\"\\\"\\n\\nimport matplotlib\\nmatplotlib.use('Agg')\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\nfrom pathlib import Path\\n\\nFIGURES_DIR = Path('/root/spectral_collapse_ews/figures')\\n\\ngenerations = list(range(11))\\n\\ndata = {\\n    r'$r=0$':    [2366.68, 2464.76, 2469.93, 2440.57, 2405.05, 2370.17, 2335.17, 2304.19, 2252.12, 2207.57, 2178.95],\\n    r'$r=0.2$':  [2366.68, 2367.46, 2358.31, 2362.52, 2379.19, 2398.93, 2429.83, 2436.35, 2454.30, 2463.14, 2479.70],\\n    r'$r=0.25$': [2366.68, 2362.13, 2363.10, 2380.88, 2393.37, 2421.22, 2436.38, 2447.08, 2463.81, 2476.58, 2485.01],\\n    r'$r=0.3$':  [2366.68, 2366.13, 2372.45, 2386.72, 2404.02, 2431.17, 2452.00, 2467.05, 2485.91, 2497.30, 2511.13],\\n    r'$r=0.5$':  [2366.68, 2366.58, 2395.36, 2425.64, 2451.72, 2486.34, 2507.62, 2525.55, 2544.03, 2562.13, 2573.20],\\n}\\n\\nstyles = {\\n    r'$r=0$':    {'color': '#d62728', 'marker': 'o'},\\n    r'$r=0.2$':  {'color': '#ff7f0e', 'marker': 's'},\\n    r'$r=0.25$': {'color': '#bcbd22', 'marker': '^'},\\n    r'$r=0.3$':  {'color': '#2ca02c', 'marker': 'D'},\\n    r'$r=0.5$':  {'color': '#1f77b4', 'marker': 'v'},\\n}\\n\\nS0 = 2366.68\\n\\ndef main():\\n    plt.rcParams.update({\\n        'font.size': 8,\\n        'font.family': 'serif',\\n        'mathtext.fontset': 'cm',\\n        'axes.linewidth': 0.6,\\n        'xtick.major.width': 0.5,\\n        'ytick.major.width': 0.5,\\n        'xtick.minor.width': 0.3,\\n        'ytick.minor.width': 0.3,\\n        'xtick.direction': 'in',\\n        'ytick.direction': 'in',\\n        'xtick.major.pad': 3,\\n        'ytick.major.pad': 3,\\n        'legend.fontsize': 6.5,\\n        'legend.framealpha': 0.92,\\n        'legend.edgecolor': '0.75',\\n        'legend.handlelength': 1.6,\\n        'legend.handletextpad': 0.5,\\n        'legend.
…[truncated 2770 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T06:49:50.958657+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T06:49:50.958792+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T06:49:50.958925+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "rtx6000-diagprobe",
  "command": "sed -i \"s/loc='upper left'/loc='lower left'/\" /root/spectral_collapse_ews/scripts/plot_phase_diagram.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "rtx6000-diagprobe",
    "command": "sed -i \"s/loc='upper left'/loc='lower left'/\" /root/spectral_collapse_ews/scripts/plot_phase_diagram.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T06:49:50.959049+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T06:49:50.959177+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx6000-diagprobe",
  "command": "grep -n \"legend\" /root/spectral_collapse_ews/scripts/plot_phase_diagram.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx6000-diagprobe",
    "command": "grep -n \"legend\" /root/spectral_collapse_ews/scripts/plot_phase_diagram.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T06:49:50.959299+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"46:        'legend.fontsize': 6.5,\\n47:        'legend.framealpha': 0.92,\\n48:        'legend.edgecolor': '0.75',\\n49:        'legend.handlelength': 1.6,\\n50:        'legend.handletextpad': 0.5,\\n51:        'legend.borderpad': 0.4,\\n52:        'legend.labelspacing': 0.35,\\n107:    ax.legend(loc='lower left', frameon=True, fancybox=False)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T06:49:50.959430+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "rtx6000-diagprobe",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/spectral_collapse_ews && python scripts/plot_phase_diagram.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "rtx6000-diagprobe",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/spectral_collapse_ews && python scripts/plot_phase_diagram.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T06:49:50.959548+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Saved: /root/spectral_collapse_ews/figures/phase_diagram.pdf\\nSaved: /root/spectral_collapse_ews/figures/phase_diagram.png\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T06:49:50.959694+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "rtx6000-diagprobe",
  "command": "cp /root/spectral_collapse_ews/figures/phase_diagram.pdf /root/spectral_collapse_ews/paper/figures/phase_diagram.pdf && cp /root/spectral_collapse_ews/figures/phase_diagram.png /root/spectral_collapse_ews/paper/figures/phase_diagram.png",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "rtx6000-diagprobe",
    "command": "cp /root/spectral_collapse_ews/figures/phase_diagram.pdf /root/spectral_collapse_ews/paper/figures/phase_diagram.pdf && cp /root/spectral_collapse_ews/figures/phase_diagram.png /root/spectral_collapse_ews/paper/figures/phase_diagram.png",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T06:49:50.959814+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T06:49:50.959929+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx6000-diagprobe",
  "command": "ls -la /root/spectral_collapse_ews/paper/figures/phase_diagram.pdf /root/spectral_collapse_ews/paper/figures/phase_diagram.png /root/spectral_collapse_ews/figures/phase_diagram.pdf",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx6000-diagprobe",
    "command": "ls -la /root/spectral_collapse_ews/paper/figures/phase_diagram.pdf /root/spectral_collapse_ews/paper/figures/phase_diagram.png /root/spectral_collapse_ews/figures/phase_diagram.pdf",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T06:49:50.960047+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root  33119 May 23 14:49 /root/spectral_collapse_ews/figures/phase_diagram.pdf\\n-rw-r--r-- 1 root root  33119 May 23 14:49 /root/spectral_collapse_ews/paper/figures/phase_diagram.pdf\\n-rw-r--r-- 1 root root 124832 May 23 14:49 /root/spectral_collapse_ews/paper/figures/phase_diagram.png\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_figure_legends_20260523T064838",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-23T06:49:50.960189+00:00_

完成。总结：

**Figure 2 (`phase_diagram.pdf`)**：已将图例从 `upper left` 改为 `lower left`，PDF/PNG 已重新生成并复制到 `paper/figures/`。

**Figure 1 (`spectral_trajectory.pdf`)**：脚本 `plot_spectral_trajectory.py` 是 5 面板图（eff_rank / log_det / ppl / distinct-4 / hellaswag），**没有任何 legend 调用**，不存在图例需要移动。你描述的"SLV 双线图 r=0 solid, r=0.5 dashed"和这个脚本不匹配——可能是另一个脚本生成的，或者 Figure 1 已经换成了这个 5 面板图。需要你确认是否还需要处理 Figure 1。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_fix_figure_legends_20260523T064838"
}
```

</details>

---
