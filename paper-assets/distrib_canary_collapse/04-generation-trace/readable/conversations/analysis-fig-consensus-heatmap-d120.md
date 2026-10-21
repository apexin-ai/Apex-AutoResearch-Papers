# analysis fig consensus heatmap d120

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/chats/worker_analysis_fig_consensus_heatmap_d120_20260520T065207.jsonl`
- **Structured JSON:** [`9d310b7de09a9c372eec.json`](../../sessions/9d/9d310b7de09a9c372eec.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

55 recorded events

### Tool call

_source line 1 · 2026-05-20T06:57:46.326926+00:00_

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
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
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

_source line 2 · 2026-05-20T06:57:46.327309+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T06:57:46.327542+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results -name \"5method_summary.txt\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results -name \"5method_summary.txt\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T06:57:46.327712+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a005_s42_fp32_v3_d080/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s42_fp32_v3_d080/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s43_fp32/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s42_fp32/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s43_fp32/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s44_fp32/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s42_fp32/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42_fp32/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43_fp32/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s44_fp32/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a060_s43_fp32/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a040_s42_fp32/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a030_s42_fp32/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a075_s42_fp32/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a035_s42_fp32/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a050_s42_fp32/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a045_s42_fp32/analysis/5method_summary.txt\\n/root/autodl-t
…[truncated 543 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T06:57:46.327894+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_summary.txt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_summary.txt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T06:57:46.328039+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5-Method Lead-Lag Analysis Summary\\nAlpha=0.5, Seed=42, Generations=11\\n============================================================\\n\\nRobust pairs (>=3/5 methods agree): 6/8\\n\\nPer-method forward significance:\\n  Perm Granger (FDR): 6/8\\n  Diff XCorr (FDR):   7/8\\n  Threshold Onset:    4/8\\n  TY Granger:         3/8\\n\\nConsensus detail:\\n  token_entropy<distinct_1  3/5  [diff, perm, ty]\\n  token_entropy<distinct_2  3/5  [diff, threshold, perm]\\n  token_entropy<distinct_3  4/5  [diff, threshold, perm, ty]\\n  token_entropy<mauve       0/5  [none]\\n  ece<distinct_1            3/5  [naive, diff, perm]\\n  ece<distinct_2            4/5  [naive, diff, threshold, perm]\\n  ece<distinct_3            5/5  [naive, diff, threshold, perm, ty]\\n  ece<mauve                 0/5  [none]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T06:57:46.328215+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a005_s42_fp32_v3_d080/analysis/5method_summary.txt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a005_s42_fp32_v3_d080/analysis/5method_summary.txt",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T06:57:46.328416+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42_fp32/analysis/5method_summary.txt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s42_fp32/analysis/5method_summary.txt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T06:57:46.328569+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5-Method Lead-Lag Analysis Summary\\nAlpha=0.05, Seed=42, Generations=11\\n============================================================\\n\\nRobust pairs (>=3/5 methods agree): 0/8\\n\\nPer-method forward significance:\\n  Perm Granger (FDR): 0/8\\n  Diff XCorr (FDR):   3/8\\n  Threshold Onset:    0/8\\n  TY Granger:         0/8\\n\\nConsensus detail:\\n  token_entropy<distinct_1  2/5  [naive, diff]\\n  token_entropy<distinct_2  2/5  [naive, diff]\\n  token_entropy<distinct_3  2/5  [naive, diff]\\n  token_entropy<mauve       0/5  [none]\\n  ece<distinct_1            0/5  [none]\\n  ece<distinct_2            1/5  [naive]\\n  ece<distinct_3            0/5  [none]\\n  ece<mauve                 0/5  [none]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T06:57:46.328698+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s43/analysis/5method_summary.txt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s43/analysis/5method_summary.txt",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T06:57:46.328819+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a075_s42_fp32/analysis/5method_summary.txt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a075_s42_fp32/analysis/5method_summary.txt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T06:57:46.328948+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5-Method Lead-Lag Analysis Summary\\nAlpha=0.75, Seed=42, Generations=11\\n============================================================\\n\\nRobust pairs (>=3/5 methods agree): 6/8\\n\\nPer-method forward significance:\\n  Perm Granger (FDR): 6/8\\n  Diff XCorr (FDR):   6/8\\n  Threshold Onset:    0/8\\n  TY Granger:         3/8\\n\\nConsensus detail:\\n  token_entropy<distinct_1  3/5  [naive, diff, perm]\\n  token_entropy<distinct_2  4/5  [naive, diff, perm, ty]\\n  token_entropy<distinct_3  3/5  [naive, diff, perm]\\n  token_entropy<mauve       0/5  [none]\\n  ece<distinct_1            4/5  [naive, diff, perm, ty]\\n  ece<distinct_2            4/5  [naive, diff, perm, ty]\\n  ece<distinct_3            3/5  [naive, diff, perm]\\n  ece<mauve                 1/5  [naive]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T06:57:46.329092+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5-Method Lead-Lag Analysis Summary\\nAlpha=1.0, Seed=43, Generations=11\\n============================================================\\n\\nRobust pairs (>=3/5 methods agree): 6/8\\n\\nPer-method forward significance:\\n  Perm Granger (FDR): 6/8\\n  Diff XCorr (FDR):   6/8\\n  Threshold Onset:    0/8\\n  TY Granger:         4/8\\n\\nConsensus detail:\\n  token_entropy<distinct_1  3/5  [naive, diff, perm]\\n  token_entropy<distinct_2  4/5  [naive, diff, perm, ty]\\n  token_entropy<distinct_3  4/5  [naive, diff, perm, ty]\\n  token_entropy<mauve       0/5  [none]\\n  ece<distinct_1            3/5  [naive, diff, perm]\\n  ece<distinct_2            4/5  [naive, diff, perm, ty]\\n  ece<distinct_3            4/5  [naive, diff, perm, ty]\\n  ece<mauve                 0/5  [none]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T06:57:46.329227+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5-Method Lead-Lag Analysis Summary\\nAlpha=0.75, Seed=42, Generations=11\\n============================================================\\n\\nRobust pairs (>=3/5 methods agree): 8/8\\n\\nPer-method forward significance:\\n  Perm Granger (FDR): 8/8\\n  Diff XCorr (FDR):   8/8\\n  Threshold Onset:    0/8\\n  TY Granger:         3/8\\n\\nConsensus detail:\\n  token_entropy<distinct_1  3/5  [naive, diff, perm]\\n  token_entropy<distinct_2  3/5  [naive, diff, perm]\\n  token_entropy<distinct_3  4/5  [naive, diff, perm, ty]\\n  token_entropy<mauve       3/5  [naive, diff, perm]\\n  ece<distinct_1            3/5  [naive, diff, perm]\\n  ece<distinct_2            4/5  [naive, diff, perm, ty]\\n  ece<distinct_3            4/5  [naive, diff, perm, ty]\\n  ece<mauve                 3/5  [naive, diff, perm]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.8}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T06:57:46.329416+00:00_

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
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
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

_source line 16 · 2026-05-20T06:57:46.329540+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T06:57:46.329683+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results -name \"5method_summary.txt\" -type f -exec echo \"===FILE:{}\" \\; -exec cat {} \\;",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results -name \"5method_summary.txt\" -type f -exec echo \"===FILE:{}\" \\; -exec cat {} \\;",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T06:57:46.329815+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T06:57:46.329950+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "python3 -c \"\nimport glob, os\nfiles = sorted(glob.glob('/root/autodl-tmp/distrib_canary_collapse/results/*/*/analysis/5method_summary.txt'))\nfor f in files:\n    print(f'===FILE:{f}')\n    print(open(f).read())\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "python3 -c \"\nimport glob, os\nfiles = sorted(glob.glob('/root/autodl-tmp/distrib_canary_collapse/results/*/*/analysis/5method_summary.txt'))\nfor f in files:\n    print(f'===FILE:{f}')\n    print(open(f).read())\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T06:57:46.330073+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T06:57:46.330274+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "cat << 'PYEOF' > /root/autodl-tmp/distrib_canary_collapse/scripts/gen_consensus_heatmap.py\n#!/usr/bin/env python3\n\"\"\"Generate consensus heatmap from D120 TY-fixed 5method_summary.txt files.\"\"\"\n\nimport glob\nimport re\nimport os\nimport json\nimport numpy as np\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nfrom matplotlib.colors import LinearSegmentedColormap\nfrom collections import defaultdict\n\n# ── 1. Find all summary files ──\nBASE = '/root/autodl-tmp/distrib_canary_collapse/results'\npatterns = [\n    f'{BASE}/*/*/analysis/5method_summary.txt',\n]\nfiles = []\nfor p in patterns:\n    files.extend(glob.glob(p))\nfiles = sorted(files)\nprint(f\"Found {len(files)} summary files\")\n\n# ── 2. Parse each file ──\nMETHOD_NAMES = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']\nMETHOD_SHORT = {'naive': 'naive_xcorr', 'diff': 'diff_xcorr', 'threshold': 'threshold_onset',\n                'perm': 'perm_granger', 'ty': 'ty_granger'}\n\ndef parse_summary(filepath):\n    \"\"\"Parse a 5method_summary.txt file.\"\"\"\n    text = open(filepath).read()\n    \n    # Extract alpha, seed\n    m = re.search(r'Alpha=([\\d.]+),\\s*Seed=(\\d+)', text)\n    if not m:\n        return None\n    alpha = float(m.group(1))\n    seed = int(m.group(2))\n    \n    # Determine domain from path\n    path_parts = filepath.split('/')\n    if any('c4' in p.lower() for p in path_parts):\n        domain = 'C4'\n    else:\n        domain = 'WikiText'\n    \n    # Determine model from path\n    if 'pythia410m' in filepath:\n        model = 'Pythia-410M'\n    elif 'gpt2m' in filepath.lower() or 'gpt2-medium' in filepath.lower():\n        model = 'GPT-2-medium'\n    else:\n        model = 'GPT-2'\n    \n    # Determine experiment category\n    for cat in ['alpha_sweep', 'c4', 'generalize', 'scale', 'ablation', 'padding_robustness']:\n        if cat in filepath:\n            category = cat\n            break\n    else:\n        category = 'unknown'\n    \n    # Extract per-method counts from the summary section\n    results = {}\n    \n    # Perm Granger\n    m = re.search(r'Perm Granger \\(FDR\\):\\s*(\\d+)/(\\d+)', text)\n    if m:\n        results['perm_granger'] = (int(m.group(1)), int(m.group(2)))\n    \n    # Diff XCorr\n    m = re.search(r'Diff XCorr \\(FDR\\):\\s*(\\d+)/(\\d+)', text)\n    if m:\n        results['diff_xcorr'] = (int(m.group(1)), int(m.group(2)))\n    \n    # Threshold Onset\n    m = re.search(r'Threshold Onset:\\s*(\\d+)/(\\d+)', text)\n    if m:\n        results['threshold_onset'] = (int(m.group(1)), int(m.group(2)))\n    \n    # TY Granger\n    m = re.search(r'TY Granger:\\s*(\\d+)/(\\d+)', text)\n    if m:\n        results['ty_granger'] = (int(m.group(1)), int(m.group(2)))\n    \n    # Robust pairs (K>=3)\n    m = re.search(r'Robust pairs \\(>=3/5 methods agree\\):\\s*(\\d+)/(\\d+)', text)\n    k3 = (int(m.group(1)), int(m.group(2))) if m else (0, 8)\n    \n    # Parse consensus detail to get naive_xcorr count and K>=4\n    naive_count = 0\n    k4_count = 0\n    total_pairs = 0\n    consensus_lines = re.findall(r'(\\S+<\\S+)\\s+(\\d+)/5\\s+\\[([^\\]]*)\\]', text)\n    for pair_name, score_str, methods_str in consensus_lines:\n        total_pairs += 1\n        score = int(score_str)\n        methods = [m.strip() for m in methods_str.split(',') if m.strip() != 'none']\n        if 'naive' in methods:\n            naive_count += 1\n        if score >= 4:\n            k4_count += 1\n    \n    if total_pairs > 0:\n        results['naive_xcorr'] = (naive_count, total_pairs)\n    \n    return {\n        'alpha': alpha,\n        'seed': seed,\n        'domain': domain,\n        'model': model,\n        'category': category,\n        'filepath': filepath,\n        'methods': results,\n        'k3': k3,\n        'k4': (k4_count, total_pairs if total_pairs > 0 else 8),\n    }\n\nrecords = []\nfor f in files:\n    r = parse_summary(f)\n    if r:\n        records.append(r)\n        dirname = os.path.basename(os.path.dirname(os.path.dirname(f)))\n        print(f\"  {dirname}: α={r['alpha']}, seed={r['seed']}, domain={r['domain']}, model={r['model']}, cat={r['category']}\")\n    else:\n        print(f\"  SKIP: {f}\")\n\n# ── 3. Filter: main alpha sweep experiments ──\n# WikiText GPT-2 experiments for the main panel\nwiki_records = [r for r in records if r['domain'] == 'WikiText' and r['model'] == 'GPT-2' \n                and r['category'] == 'alpha_sweep'\n                and 'postd' not in r['filepath']]  # exclude post-decay variants\nc4_records = [r for r in records if r['domain'] == 'C4' and r['model'] == 'GPT-2']\n# Also include padding_robustness a100 as WikiText α=1.0 if no alpha_sweep a100 exists\nwiki_alphas = set(r['alpha'] for r in wiki_records)\nif 1.0 not in wiki_alphas:\n    padding_a100 = [r for r in records if r['category'] == 'padding_robustness' and r['alpha'] == 1.0]\n    wiki_records.extend(padding_a100)\n    if padding_a100:\n        print(f\"\\nAdded padding_robustness α=1.0 as WikiText α=1.0 (seed={padding_a100[0]['seed']})\")\n\n# Also include generalize pythia as a separate note but not in main heatmap\ngeneralize_records = [r for r in records if r['category'] == 'generalize']\n\nprint(f\"\\nWikiText records: {len(wiki_records)}\")\nprint(f\"C4 records: {len(c4_records)}\")\nprint(f\"Generalize records: {len(generalize_records)}\")\n\n# ── 4. Build data matrix ──\ndef build_matrix(recs):\n    \"\"\"Build method×alpha matrix, averaging over seeds.\"\"\"\n    # Group by alpha\n    by_alpha = defaultdict(list)\n    for r in recs:\n        by_alpha[r['alpha']].append(r)\n    \n    alphas = sorted(by_alpha.keys())\n    rows = METHOD_NAMES + ['K≥3', 'K≥4']\n    \n    matrix = np.full((len(rows), len(alphas)), np.nan)\n    annotations = [['' for _ in alphas] for _ in rows]\n    seed_counts = {}\n    \n    for j, alpha in enumerate(alphas):\n        group = by_alpha[alpha]\n        seeds = [r['seed'] for r in group]\n        seed_counts[alpha] = len(group)\n        \n        for i, method in enumerate(METHOD_NAMES):\n            vals = []\n            for r in group:\n                if method in r['methods']:\n                    num, den = r['methods'][method]\n                    vals.append(num)\n            if vals:\n                avg = np.mean(vals)\n                matrix[i, j] = avg\n                if len(group) == 1:\n                    annotations[i][j] = f\"{int(vals[0])}/8\"\n                else:\n                    annotations[i][j] = f\"{avg:.1f}/8\"\n        \n        # K>=3\n        k3_vals = [r['k3'][0] for r in group]\n        if k3_vals:\n            avg = np.mean(k3_vals)\n            matrix[len(METHOD_NAMES), j] = avg\n            if len(group) == 1:\n                annotations[len(METHOD_NAMES)][j] = f\"{int(k3_vals[0])}/8\"\n            else:\n                annotations[len(METHOD_NAMES)][j] = f\"{avg:.1f}/8\"\n        \n        # K>=4\n        k4_vals = [r['k4'][0] for r in group]\n        if k4_vals:\n            avg = np.mean(k4_vals)\n            matrix[len(METHOD_NAMES)+1, j] = avg\n            if len(group) == 1:\n                annotations[len(METHOD_NAMES)+1][j] = f\"{int(k4_vals[0])}/8\"\n            else:\n                annotations[len(METHOD_NAMES)+1][j] = f\"{avg:.1f}/8\"\n    \n    return alphas, rows, matrix, annotations, seed_counts\n\n# ── 5. Plot ──\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.size': 10,\n    'axes.labelsize': 11,\n    'axes.titlesize': 12,\n    'xtick.labelsize': 9,\n    'ytick.labelsize': 10,\n    'figure.dpi': 300,\n})\n\nROW_LABELS = {\n    'naive_xcorr': 'Naive XCorr',\n    'diff_xcorr': 'Diff XCorr (FDR)',\n    'threshold_onset': 'Threshold Onset',\n    'perm_granger': 'Perm Granger (FDR)',\n    'ty_granger': 'TY Granger',\n    'K≥3': 'Consensus K≥3',\n    'K≥4': 'Consensus K≥4',\n}\n\n# Determine layout: one or two panels\nhas_c4 = len(c4_records) >= 3  # need at least 3 alpha points for C4\nif has_c4:\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4.2), gridspec_kw={'width_ratios': [11, 3]})\nelse:\n    fig, ax1 = plt.subplots(1, 1, figsize=(9, 4.2))\n\ncmap = plt.cm.YlOrRd\ncmap.set_bad(color='#f0f0f0')\n\ndef plot_heatmap(ax, recs, title, show_ylabel=True):\n    alphas, rows, matrix, annotations, seed_counts = build_matrix(recs)\n    \n    # Normalize to 0-8 range for color\n    im = ax.imshow(matrix, cmap=cmap, vmin=0, vmax=8, aspect='auto',\n                   interpolation='nearest')\n    \n    # Annotations\n    for i in range(len(rows)):\n        for j in range(len(alphas)):\n            val = matrix[i, j]\n            if np.isnan(val):\n                continue\n            color = 'white' if val > 5.5 else 'black'\n            ax.text(j, i, annotations[i][j], ha='center', va='center',\n                    fontsize=8, color=color, fontweight='medium')\n    \n    # Axis labels\n    ax.set_xticks(range(len(alphas)))\n    ax.set_xticklabels([f\"{a:.2f}\" if a < 1 else f\"{a:.1f}\" for a in alphas])\n    ax.set_xlabel('Canary strength α')\n    \n    if show_ylabel:\n        ax.set_yticks(range(len(rows)))\n        ax.set_yticklabels([ROW_LABELS.get(r, r) for r in rows])\n    else:\n        ax.set_yticks(range(len(rows)))\n        ax.set_yticklabels([])\n    \n    # Add seed count annotation at the top\n    for j, alpha in enumerate(alphas):\n        n = seed_counts[alpha]\n        if n > 1:\n            ax.text(j, -0.7, f'n={n}', ha='center', va='center', fontsize=7, color='gray')\n    \n    # Add horizontal line to separate consensus rows\n    ax.axhline(y=len(METHOD_NAMES) - 0.5, color='black', linewidth=1.5)\n    \n    ax.set_title(title, pad=12)\n    \n    return im\n\nim1 = plot_heatmap(ax1, wiki_records, 'WikiText-103 (GPT-2 Small)')\n\nif has_c4:\n    im2 = plot_heatmap(ax2, c4_records, 'C4', show_ylabel=False)\n\n# Colorbar\ncbar_ax = fig.add_axes([0.92, 0.15, 0.015, 0.7])\ncbar = fig.colorbar(im1, cax=cbar_ax)\ncbar.set_ticks([0, 2, 4, 6, 8])\ncbar.set_ticklabels(['0/8', '2/8', '4/8', '6/8', '8/8'])\ncbar.set_label('Significant pairs', fontsize=10)\n\nplt.subplots_adjust(left=0.14, right=0.90, top=0.88, bottom=0.15, wspace=0.08)\n\n# Save\noutdir = '/root/autodl-tmp/distrib_canary_collapse/artifacts'\nos.makedirs(outdir, exist_ok=True)\nfig.savefig(f'{outdir}/fig_consensus_heatmap.pdf', bbox_inches='tight', dpi=300)\nfig.savefig(f'{outdir}/fig_consensus_heatmap.png', bbox_inches='tight', dpi=300)\nprint(f\"\\nSaved to {outdir}/fig_consensus_heatmap.pdf and .png\")\n\n# ── 6. Print full data matrix ──\nprint(\"\\n\" + \"=\"*80)\nprint(\"FULL DATA MATRIX\")\nprint(\"=\"*80)\n\nfor domain_name, recs in [('WikiText', wiki_records), ('C4', c4_records), ('Generalize', generalize_records)]:\n    if not recs:\n        continue\n    print(f\"\\n--- {domain_name} ---\")\n    by_alpha = defaultdict(list)\n    for r in recs:\n        by_alpha[r['alpha']].append(r)\n    \n    for alpha in sorted(by_alpha.keys()):\n        group = by_alpha[alpha]\n        for r in group:\n            print(f\"\\n  α={alpha}, seed={r['seed']}, model={r['model']}:\")\n            for method in METHOD_NAMES:\n                if method in r['methods']:\n                    num, den = r['methods'][method]\n                    print(f\"    {method:20s}: {num}/{den}\")\n            print(f\"    {'K≥3':20s}: {r['k3'][0]}/{r['k3'][1]}\")\n            print(f\"    {'K≥4':20s}: {r['k4'][0]}/{r['k4'][1]}\")\n\nplt.close()\nPYEOF\necho \"Script written.\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat << 'PYEOF' > /root/autodl-tmp/distrib_canary_collapse/scripts/gen_consensus_heatmap.py\n#!/usr/bin/env python3\n\"\"\"Generate consensus heatmap from D120 TY-fixed 5method_summary.txt files.\"\"\"\n\nimport glob\nimport re\nimport os\nimport json\nimport numpy as np\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nfrom matplotlib.colors import LinearSegmentedColormap\nfrom collections import defaultdict\n\n# ── 1. Find all summary files ──\nBASE = '/root/autodl-tmp/distrib_canary_collapse/results'\npatterns = [\n    f'{BASE}/*/*/analysis/5method_summary.txt',\n]\nfiles = []\nfor p in patterns:\n    files.extend(glob.glob(p))\nfiles = sorted(files)\nprint(f\"Found {len(files)} summary files\")\n\n# ── 2. Parse each file ──\nMETHOD_NAMES = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']\nMETHOD_SHORT = {'naive': 'naive_xcorr', 'diff': 'diff_xcorr', 'threshold': 'threshold_onset',\n                'perm': 'perm_granger', 'ty': 'ty_granger'}\n\ndef parse_summary(filepath):\n    \"\"\"Parse a 5method_summary.txt file.\"\"\"\n    text = open(filepath).read()\n    \n    # Extract alpha, seed\n    m = re.search(r'Alpha=([\\d.]+),\\s*Seed=(\\d+)', text)\n    if not m:\n        return None\n    alpha = float(m.group(1))\n    seed = int(m.group(2))\n    \n    # Determine domain from path\n    path_parts = filepath.split('/')\n    if any('c4' in p.lower() for p in path_parts):\n        domain = 'C4'\n    else:\n        domain = 'WikiText'\n    \n    # Determine model from path\n    if 'pythia410m' in filepath:\n        model = 'Pythia-410M'\n    elif 'gpt2m' in filepath.lower() or 'gpt2-medium' in filepath.lower():\n        model = 'GPT-2-medium'\n    else:\n        model = 'GPT-2'\n    \n    # Determine experiment category\n    for cat in ['alpha_sweep', 'c4', 'generalize', 'scale', 'ablation', 'padding_robustness']:\n        if cat in filepath:\n            category = cat\n            break\n    else:\n        category = 'unknown'\n    \n    # Extract per-method counts from the summary section\n    results = {}\n    \n    # Perm Granger\n    m = re.search(r'Perm Granger \\(FDR\\):\\s*(\\d+)/(\\d+)', text)\n    if m:\n        results['perm_granger'] = (int(m.group(1)), int(m.group(2)))\n    \n    # Diff XCorr\n    m = re.search(r'Diff XCorr \\(FDR\\):\\s*(\\d+)/(\\d+)', text)\n    if m:\n        results['diff_xcorr'] = (int(m.group(1)), int(m.group(2)))\n    \n    # Threshold Onset\n    m = re.search(r'Threshold Onset:\\s*(\\d+)/(\\d+)', text)\n    if m:\n        results['threshold_onset'] = (int(m.group(1)), int(m.group(2)))\n    \n    # TY Granger\n    m = re.search(r'TY Granger:\\s*(\\d+)/(\\d+)', text)\n    if m:\n        results['ty_granger'] = (int(m.group(1)), int(m.group(2)))\n    \n    # Robust pairs (K>=3)\n    m = re.search(r'Robust pairs \\(>=3/5 methods agree\\):\\s*(\\d+)/(\\d+)', text)\n    k3 = (int(m.group(1)), int(m.group(2))) if m else (0, 8)\n    \n    # Parse consensus detail to get naive_xcorr count and K>=4\n    naive_count = 0\n    k4_count = 0\n    total_pairs = 0\n    consensus_lines = re.findall(r'(\\S+<\\S+)\\s+(\\d+)/5\\s+\\[([^\\]]*)\\]', text)\n    for pair_name, score_str, methods_str in consensus_lines:\n        total_pairs += 1\n        score = int(score_str)\n        methods = [m.strip() for m in methods_str.split(',') if m.strip() != 'none']\n        if 'naive' in methods:\n            naive_count += 1\n        if score >= 4:\n            k4_count += 1\n    \n    if total_pairs > 0:\n        results['naive_xcorr'] = (naive_count, total_pairs)\n    \n    return {\n        'alpha': alpha,\n        'seed': seed,\n        'domain': domain,\n        'model': model,\n        'category': category,\n        'filepath': filepath,\n        'methods': results,\n        'k3': k3,\n        'k4': (k4_count, total_pairs if total_pairs > 0 else 8),\n    }\n\nrecords = []\nfor f in files:\n    r = parse_summary(f)\n    if r:\n        records.append(r)\n        dirname = os.path.basename(os.path.dirname(os.path.dirname(f)))\n        print(f\"  {dirname}: α={r['alpha']}, seed={r['seed']}, domain={r['domain']}, model={r['model']}, cat={r['category']}\")\n    else:\n        print(f\"  SKIP: {f}\")\n\n# ── 3. Filter: main alpha sweep experiments ──\n# WikiText GPT-2 experiments for the main panel\nwiki_records = [r for r in records if r['domain'] == 'WikiText' and r['model'] == 'GPT-2' \n                and r['category'] == 'alpha_sweep'\n                and 'postd' not in r['filepath']]  # exclude post-decay variants\nc4_records = [r for r in records if r['domain'] == 'C4' and r['model'] == 'GPT-2']\n# Also include padding_robustness a100 as WikiText α=1.0 if no alpha_sweep a100 exists\nwiki_alphas = set(r['alpha'] for r in wiki_records)\nif 1.0 not in wiki_alphas:\n    padding_a100 = [r for r in records if r['category'] == 'padding_robustness' and r['alpha'] == 1.0]\n    wiki_records.extend(padding_a100)\n    if padding_a100:\n        print(f\"\\nAdded padding_robustness α=1.0 as WikiText α=1.0 (seed={padding_a100[0]['seed']})\")\n\n# Also include generalize pythia as a separate note but not in main heatmap\ngeneralize_records = [r for r in records if r['category'] == 'generalize']\n\nprint(f\"\\nWikiText records: {len(wiki_records)}\")\nprint(f\"C4 records: {len(c4_records)}\")\nprint(f\"Generalize records: {len(generalize_records)}\")\n\n# ── 4. Build data matrix ──\ndef build_matrix(recs):\n    \"\"\"Build method×alpha matrix, averaging over seeds.\"\"\"\n    # Group by alpha\n    by_alpha = defaultdict(list)\n    for r in recs:\n        by_alpha[r['alpha']].append(r)\n    \n    alphas = sorted(by_alpha.keys())\n    rows = METHOD_NAMES + ['K≥3', 'K≥4']\n    \n    matrix = np.full((len(rows), len(alphas)), np.nan)\n    annotations = [['' for _ in alphas] for _ in rows]\n    seed_counts = {}\n    \n    for j, alpha in enumerate(alphas):\n        group = by_alpha[alpha]\n        seeds = [r['seed'] for r in group]\n        seed_counts[alpha] = len(group)\n        \n        for i, method in enumerate(METHOD_NAMES):\n            vals = []\n            for r in group:\n                if method in r['methods']:\n                    num, den = r['methods'][method]\n                    vals.append(num)\n            if vals:\n                avg = np.mean(vals)\n                matrix[i, j] = avg\n                if len(group) == 1:\n                    annotations[i][j] = f\"{int(vals[0])}/8\"\n                else:\n                    annotations[i][j] = f\"{avg:.1f}/8\"\n        \n        # K>=3\n        k3_vals = [r['k3'][0] for r in group]\n        if k3_vals:\n            avg = np.mean(k3_vals)\n            matrix[len(METHOD_NAMES), j] = avg\n            if len(group) == 1:\n                annotations[len(METHOD_NAMES)][j] = f\"{int(k3_vals[0])}/8\"\n            else:\n                annotations[len(METHOD_NAMES)][j] = f\"{avg:.1f}/8\"\n        \n        # K>=4\n        k4_vals = [r['k4'][0] for r in group]\n        if k4_vals:\n            avg = np.mean(k4_vals)\n            matrix[len(METHOD_NAMES)+1, j] = avg\n            if len(group) == 1:\n                annotations[len(METHOD_NAMES)+1][j] = f\"{int(k4_vals[0])}/8\"\n            else:\n                annotations[len(METHOD_NAMES)+1][j] = f\"{avg:.1f}/8\"\n    \n    return alphas, rows, matrix, annotations, seed_counts\n\n# ── 5. Plot ──\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.size': 10,\n    'axes.labelsize': 11,\n    'axes.titlesize': 12,\n    'xtick.labelsize': 9,\n    'ytick.labelsize': 10,\n    'figure.dpi': 300,\n})\n\nROW_LABELS = {\n    'naive_xcorr': 'Naive XCorr',\n    'diff_xcorr': 'Diff XCorr (FDR)',\n    'threshold_onset': 'Threshold Onset',\n    'perm_granger': 'Perm Granger (FDR)',\n    'ty_granger': 'TY Granger',\n    'K≥3': 'Consensus K≥3',\n    'K≥4': 'Consensus K≥4',\n}\n\n# Determine layout: one or two panels\nhas_c4 = len(c4_records) >= 3  # need at least 3 alpha points for C4\nif has_c4:\n    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4.2), gridspec_kw={'width_ratios': [11, 3]})\nelse:\n    fig, ax1 = plt.subplots(1, 1, figsize=(9, 4.2))\n\ncmap = plt.cm.YlOrRd\ncmap.set_bad(color='#f0f0f0')\n\ndef plot_heatmap(ax, recs, title, show_ylabel=True):\n    alphas, rows, matrix, annotations, seed_counts = build_matrix(recs)\n    \n    # Normalize to 0-8 range for color\n    im = ax.imshow(matrix, cmap=cmap, vmin=0, vmax=8, aspect='auto',\n                   interpolation='nearest')\n    \n    # Annotations\n    for i in range(len(rows)):\n        for j in range(len(alphas)):\n            val = matrix[i, j]\n            if np.isnan(val):\n                continue\n            color = 'white' if val > 5.5 else 'black'\n            ax.text(j, i, annotations[i][j], ha='center', va='center',\n                    fontsize=8, color=color, fontweight='medium')\n    \n    # Axis labels\n    ax.set_xticks(range(len(alphas)))\n    ax.set_xticklabels([f\"{a:.2f}\" if a < 1 else f\"{a:.1f}\" for a in alphas])\n    ax.set_xlabel('Canary strength α')\n    \n    if show_ylabel:\n        ax.set_yticks(range(len(rows)))\n        ax.set_yticklabels([ROW_LABELS.get(r, r) for r in rows])\n    else:\n        ax.set_yticks(range(len(rows)))\n        ax.set_yticklabels([])\n    \n    # Add seed count annotation at the top\n    for j, alpha in enumerate(alphas):\n        n = seed_counts[alpha]\n        if n > 1:\n            ax.text(j, -0.7, f'n={n}', ha='center', va='center', fontsize=7, color='gray')\n    \n    # Add horizontal line to separate consensus rows\n    ax.axhline(y=len(METHOD_NAMES) - 0.5, color='black', linewidth=1.5)\n    \n    ax.set_title(title, pad=12)\n    \n    return im\n\nim1 = plot_heatmap(ax1, wiki_records, 'WikiText-103 (GPT-2 Small)')\n\nif has_c4:\n    im2 = plot_heatmap(ax2, c4_records, 'C4', show_ylabel=False)\n\n# Colorbar\ncbar_ax = fig.add_axes([0.92, 0.15, 0.015, 0.7])\ncbar = fig.colorbar(im1, cax=cbar_ax)\ncbar.set_ticks([0, 2, 4, 6, 8])\ncbar.set_ticklabels(['0/8', '2/8', '4/8', '6/8', '8/8'])\ncbar.set_label('Significant pairs', fontsize=10)\n\nplt.subplots_adjust(left=0.14, right=0.90, top=0.88, bottom=0.15, wspace=0.08)\n\n# Save\noutdir = '/root/autodl-tmp/distrib_canary_collapse/artifacts'\nos.makedirs(outdir, exist_ok=True)\nfig.savefig(f'{outdir}/fig_consensus_heatmap.pdf', bbox_inches='tight', dpi=300)\nfig.savefig(f'{outdir}/fig_consensus_heatmap.png', bbox_inches='tight', dpi=300)\nprint(f\"\\nSaved to {outdir}/fig_consensus_heatmap.pdf and .png\")\n\n# ── 6. Print full data matrix ──\nprint(\"\\n\" + \"=\"*80)\nprint(\"FULL DATA MATRIX\")\nprint(\"=\"*80)\n\nfor domain_name, recs in [('WikiText', wiki_records), ('C4', c4_records), ('Generalize', generalize_records)]:\n    if not recs:\n        continue\n    print(f\"\\n--- {domain_name} ---\")\n    by_alpha = defaultdict(list)\n    for r in recs:\n        by_alpha[r['alpha']].append(r)\n    \n    for alpha in sorted(by_alpha.keys()):\n        group = by_alpha[alpha]\n        for r in group:\n            print(f\"\\n  α={alpha}, seed={r['seed']}, model={r['model']}:\")\n            for method in METHOD_NAMES:\n                if method in r['methods']:\n                    num, den = r['methods'][method]\n                    print(f\"    {method:20s}: {num}/{den}\")\n            print(f\"    {'K≥3':20s}: {r['k3'][0]}/{r['k3'][1]}\")\n            print(f\"    {'K≥4':20s}: {r['k4'][0]}/{r['k4'][1]}\")\n\nplt.close()\nPYEOF\necho \"Script written.\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T06:57:46.330547+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.66}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T06:57:46.330681+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python scripts/gen_consensus_heatmap.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python scripts/gen_consensus_heatmap.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T06:57:46.330882+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Found 22 summary files\\n  a005_s42_fp32_v3_d080: α=0.05, seed=42, domain=WikiText, model=GPT-2, cat=alpha_sweep\\n  a010_s42_fp32: α=0.1, seed=42, domain=WikiText, model=GPT-2, cat=alpha_sweep\\n  a010_s43_fp32: α=0.1, seed=43, domain=WikiText, model=GPT-2, cat=alpha_sweep\\n  a025_s42_fp32: α=0.25, seed=42, domain=WikiText, model=GPT-2, cat=alpha_sweep\\n  a025_s43_fp32: α=0.25, seed=43, domain=WikiText, model=GPT-2, cat=alpha_sweep\\n  a025_s44_fp32: α=0.25, seed=44, domain=WikiText, model=GPT-2, cat=alpha_sweep\\n  a030_s42_fp32: α=0.3, seed=42, domain=WikiText, model=GPT-2, cat=alpha_sweep\\n  a035_s42_fp32: α=0.35, seed=42, domain=WikiText, model=GPT-2, cat=alpha_sweep\\n  a040_s42_fp32: α=0.4, seed=42, domain=WikiText, model=GPT-2, cat=alpha_sweep\\n  a045_s42_fp32: α=0.45, seed=42, domain=WikiText, model=GPT-2, cat=alpha_sweep\\n  a050_postd093_s42_fp32: α=0.5, seed=42, domain=WikiText, model=GPT-2, cat=alpha_sweep\\n  a050_s42_fp32: α=0.5, seed=42, domain=WikiText, model=GPT-2, cat=alpha_sweep\\n  a050_s43_fp32: α=0.5, seed=43, domain=WikiText, model=GPT-2, cat=alpha_sweep\\n  a050_s44_fp32: α=0.5, seed=44, domain=WikiText, model=GPT-2, cat=alpha_sweep\\n  a060_s42_fp32_v3_d080: α=0.6, seed=42, domain=WikiText, model=GPT-2, cat=alpha_sweep\\n  a060_s43_fp32: α=0.6, seed=43, domain=WikiText, model=GPT-2, cat=alpha_sweep\\n  a075_s42_fp32: α=0.75, seed=42, domain=WikiText, model=GPT-2, cat=alpha_sweep\\n  c4_a025_s42_fp32: α=0.25, seed=42, domain=C4, model=GPT-2, cat=alpha_sweep\\n  c4_a050_s42_fp32: α=0.5, seed=42, domain=C4, model=GPT-2, cat=alpha_sweep\\n  c4_a075_s42_fp32: α=0.75, seed=42, domain=C4, model=GPT-2, cat=alpha_sweep\\n  pythia410m_wiki_a100_s43: α=1.0, seed=43, domain=WikiText, model=Pythia-410M, cat=generalize\\n  a100_s42_fp32: α=1.0, seed=42, domain=WikiText, model=GPT-2, cat=padding_robustness\\n\\nAdded padding_robustness α=1.0 as WikiText α=1.0 (seed=42)\\n\\nWikiText records: 17\\
…[truncated 5970 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T06:57:46.331078+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/",
  "description": "List local artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/",
    "description": "List local artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T06:57:46.331234+00:00_

D040
D105_3sigma_recompute_combined.json
_project
a050_fp32_3seed_5method_analysis.md
a050_fp32_3seed_metrics_summary.md
a050_s44_draft_versions.tex
a075_analysis_prep.md
alpha_sweep
alpha_sweep_a000_s43
alpha_sweep_a000_s44
alpha_sweep_a005_s42
alpha_sweep_a010_s42_v2
alpha_sweep_a010_s43
alpha_sweep_a010_s43_fp32
alpha_sweep_a025_s43_fp32
alpha_sweep_a025_s44_fp32
alpha_sweep_a030_s42_fp32
alpha_sweep_a045_s42_fp32
alpha_sweep_a050_s42
alpha_sweep_a050_s43
alpha_sweep_a050_s44
alpha_sweep_a060_s42_bf16
alpha_sweep_a075_s42
alpha_sweep_a075_s42_fp32
alpha_sweep_a075_s43
alpha_sweep_a075_s44
alpha_sweep_c4_a050_s42_bf16
analysis
analysis_a050_a010_fp32_batch.md
analysis_alpha_sweep_a010_s42_v2.md
analyze_extended.py
analyze_mvp.py
batch3_fp32_analysis.md
c4_a025_mmct_detail.md
c4_a025_s42_fp32
c4_a050_s42_fp32
c4_a075_s42_fp32
c4_cross_seed_s43
c4_vs_wikitext_a050_collapse.md
ccf_maxlag7_report.md
check_progress.sh
consensus_framework
consensus_heatmap_data.csv
consensus_heatmap_data_INVALID_preD105.csv
cross_alpha_aggregation
cross_alpha_analysis_v4.py
cross_alpha_v4_ready.md
cross_arch_table7.csv
d024_literature_notes.md
d026_optimized_commands.md
d059_mvp_reverse_reanalysis.md
d060_pythia69b_prep.md
d061_conditional_granger_analysis.md
d105_5method_diff_report.md
d105_d111_complete_audit.md
d111_a030_a040_audit.md
d111_c4_audit_report.md
d111_full_sweep_audit.md
d120_alpha_sweep_recalc
d120_c4_padding_audit
d120_recalc_19828.md
d120_threshold_fix
d120_ty_fixed_full_rerun
detrending_utils.py
diag_gen_gpt2m_a100_s43_bf16.md
diagnostics_a050_postd093.md
dose_response
dose_response_5method_regime.csv
dose_response_5method_regime_INVALID_preD105.csv
dose_response_fp32.csv
dose_response_fp32_detail.csv
dream_reports
drift_discrepancy_audit
dual_track_figure
effrank_trajectories.csv
figures
fp32_wave2_configs.md
framing_alignment_check.md
gen_gpt2m_a100_s43_bf16
gen_gpt2m_a100_s43_fp32
gen_wiki_gpt2m_a025_s42
gen_wiki_gpt2m_a100_s42_v3
gen_wiki_gpt2m_a100_s42_v4
general
…[truncated 1607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T06:57:46.331415+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "scp westd-17855:/root/autodl-tmp/distrib_canary_collapse/artifacts/fig_consensus_heatmap.pdf /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures/ && scp westd-17855:/root/autodl-tmp/distrib_canary_collapse/artifacts/fig_consensus_heatmap.png /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures/",
  "description": "SCP heatmap files from 17855 to local artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Bash",
  "tool_args": {
    "command": "scp westd-17855:/root/autodl-tmp/distrib_canary_collapse/artifacts/fig_consensus_heatmap.pdf /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures/ && scp westd-17855:/root/autodl-tmp/distrib_canary_collapse/artifacts/fig_consensus_heatmap.png /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures/",
    "description": "SCP heatmap files from 17855 to local artifacts"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T06:57:46.331540+00:00_

Exit code 255
ssh: Could not resolve hostname westd-17855: Temporary failure in name resolution
scp: Connection closed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T06:57:46.331670+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A5 \"westd-17855\" ~/.ssh/config 2>/dev/null || echo \"No SSH config found\"",
  "description": "Check SSH config for westd-17855"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A5 \"westd-17855\" ~/.ssh/config 2>/dev/null || echo \"No SSH config found\"",
    "description": "Check SSH config for westd-17855"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T06:57:46.331790+00:00_

No SSH config found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T06:57:46.331935+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/artifacts/fig_consensus_heatmap.png",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/artifacts/fig_consensus_heatmap.png",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T06:57:46.332058+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 263571 May 20 14:54 /root/autodl-tmp/distrib_canary_collapse/artifacts/fig_consensus_heatmap.png\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T06:57:46.332187+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/artifacts/fig_consensus_heatmap.pdf",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/artifacts/fig_consensus_heatmap.pdf",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T06:57:46.332325+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 36311 May 20 14:54 /root/autodl-tmp/distrib_canary_collapse/artifacts/fig_consensus_heatmap.pdf\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T06:57:46.332443+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "base64 /root/autodl-tmp/distrib_canary_collapse/artifacts/fig_consensus_heatmap.pdf",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "base64 /root/autodl-tmp/distrib_canary_collapse/artifacts/fig_consensus_heatmap.pdf",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T06:57:46.332635+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"JVBERi0xLjQKJazcIKu6CjEgMCBvYmoKPDwgL1R5cGUgL0NhdGFsb2cgL1BhZ2VzIDIgMCBSID4+\\nCmVuZG9iago4IDAgb2JqCjw8IC9Gb250IDMgMCBSIC9YT2JqZWN0IDcgMCBSIC9FeHRHU3RhdGUg\\nNCAwIFIgL1BhdHRlcm4gNSAwIFIKL1NoYWRpbmcgNiAwIFIgL1Byb2NTZXQgWyAvUERGIC9UZXh0\\nIC9JbWFnZUIgL0ltYWdlQyAvSW1hZ2VJIF0gPj4KZW5kb2JqCjExIDAgb2JqCjw8IC9UeXBlIC9Q\\nYWdlIC9QYXJlbnQgMiAwIFIgL1Jlc291cmNlcyA4IDAgUgovTWVkaWFCb3ggWyAwIDAgOTY1LjA0\\nMTI1IDI4Ni43OTI2MjUgXSAvQ29udGVudHMgOSAwIFIgL0Fubm90cyAxMCAwIFIgPj4KZW5kb2Jq\\nCjkgMCBvYmoKPDwgL0xlbmd0aCAxMiAwIFIgL0ZpbHRlciAvRmxhdGVEZWNvZGUgPj4Kc3RyZWFt\\nCniczVtLUxy3Ft73r9ASFgi9H4ssYhNTN7cqiQOVR8VZTDkDjAPjMOD43n+fI/W0R1J3S+oRi1CF\\nzYjWp09H55POaR3OL9Z/b96vf7x8hV5fdeeHT++fOoo+wPctIugDfH9GFF3C921H4NNDZ5XERFAm\\n4dN98IkZhbVlCn68h0ejj3ddd9Odfw0gT9DrsusotVhqibjGmkr30EOnrMFcCMZp0HwfNjNpsFC6\\nbx8gokY/0CMaw0ttsFaWceL+RYwRrCVDuzX6GW3R+dfMUYOJw/dnTzE2yaMHMAY5G7jOZmKM9w/o\\n/D8UXXxEb7u36HFAJWBKh+w6eWzX0lEhAY85MqERwmaB2WCE7hWsyOfuEf4l6IwAHuXwoKTOMERr\\nxDg2mhrtWHSvrrvzNxRZdH3jF+36j+43dEIwkafod3T9bffNdfe283w6CuYV1jiMiEfQnOdhnPmV\\np+yWqIYHJWMeTFJMKRcqtkfYnOXBBMXEMEap5EbW8WAT9uCEY82MESriETbneViOldXSKkekjgef\\nsAeXaqyGh6g5ywNMhjllbgm9w1fxmLCHIAZbP5uIR9ic5wGOZJnhCqwBxqviISbsIRQd7Rhf2rIM\\nBLiQFFxXOoWYMALoDFNLnGOF44fNWQqSwIPSOj+mUtTxkBNGkEphQySsaMwjaM7zAO/RGgziNsJK\\n51QTPBTsfcJJTcQ7eNCc5aGIxdxYZzqn7CoeemJdlGaYeNeKeQTNeR5KwMhM9HKt4QGbTEgjdHSp\\n94rwjm6x4hEQpTHS69V2tfs/enrerbe3z3foAPsIRwWh1J81/U9WgAdrrjgzlEGrO2ne0LOL9YfV\\nT5+u1rvNzdnq/q+71f7sGbb24YQUDLYku9/YqcIkbpwUDfCX3J/rHARMWDwXEs/lu9Xm7zX65RRR\\njb39Tl5/3O0mDpuBEYVdXfGE0aFxcmPVEGh4FRONuVJZQhebm5sRH/Tu5M3Fj+9O53lRDdNmOuYV\\nNE7yMoOlqIYjmZMsseu73frp7uP9H+j77dP6OUNFGEwsTagcGqeoaMzgEfB4K7IkfjhFAo4zMMt6\\n94Aud6vt7brGOsBCSplQOjRO7jggKWcayuB/S/owadY4vw5k5kkYiDdp4suHtskTCIb2/AzFjOUd\\n+fVHWJXt06cn9N89hcNTmmPOhYW9y3nh0IOnuv0iWwSbi5WKSKGM7zCh2tvdevW83q0fP63up8UL\\nBhQmUcqhLTtfp2GT18ny+YoXn68LlY8M2Bn6tg/asXShdXeJkkxm8FwCvY0e5RlBO1jyKozaHfQh\\nYp+GjQLmqXQEICezmofZrAZ6LMiNgqcDlCw6cfPaZyR9rnMb
…[truncated 6410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T06:57:46.332842+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "base64 /root/autodl-tmp/distrib_canary_collapse/artifacts/fig_consensus_heatmap.png",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "base64 /root/autodl-tmp/distrib_canary_collapse/artifacts/fig_consensus_heatmap.png",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T06:57:46.333164+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"iVBORw0KGgoAAAANSUhEUgAAD7YAAASrCAYAAACsD7aUAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90\\nbGliIHZlcnNpb24zLjEwLjUsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvWftoOwAAAAlwSFlzAAAu\\nIwAALiMBeKU/dgABAABJREFUeJzs3Xd4k+XbxvGzm7aUQtm77FmGMmTIkI2AICAyZCiKCCgiCoKA\\nigoqOFmC7CGIIiK7TNlDVtmzUCi7Cwp05v2jL/kRkrZJV1r4fo6Dw95X7nElzahPnuu5HQwGg0EA\\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKQTR3snAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4slHYDgAA\\nAAAAAAAAAAAAAAAAAAAAAAAAAABIVxS2AwAAAAAAAAAAAAAAAAAAAAAAAAAAAADSFYXtAAAAAAAA\\nAAAAAAAAAAAAAAAAAAAAAIB0RWE7AAAAAAAAAAAAAAAAAAAAAAAAAAAAACBdUdgOAAAAAAAAAAAA\\nAAAAAAAAAAAAAAAAAEhXFLYDAAAAAAAAAAAAAAAAAAAAAAAAAAAAANIVhe0AAAAAAAAAAAAAAAAA\\nAAAAAAAAAAAAgHRFYTsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIF1R2A4AAAAAAAAAAAAAAAAAAAAA\\nAAAAAAAASFcUtgMAAAAAAAAAAAAAAAAAAAAAAAAAAAAA0hWF7QAAAAAAAAAAAAAAAAAAAAAAAAAA\\nAACAdEVhOwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgXVHYDgAAAAAAAAAAAAAAAAAAAAAAAAAAAABI\\nVxS2AwAAAAAAAAAAAAAAAAAAAAAAAAAAAADSFYXtAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIB0RWE7\\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBdUdgOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEhXFLYDAAAA\\nAAAAAAAAAAAAAAAAAAAAAAAAANIVhe0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAgHRFYTsAAAAAAAAA\\nAAAAAAAAAAAAAAAAAAAAIF1R2A4AAAAAAAAAAAAAAAAAAAAAAAAAAAAASFcUtgMAAAAAAAAAAAAA\\nAAAAAAAAAAAAAAAA0hWF7QAAAAAAAAAAAAAAAAAAAAAAAAAAAACAdEVhOwAAAAAAAAAAAAAAAAAA\\nAAAAAAAAAAAgXVHYDgAAAAAAAAAAAAAAAAAAAAAAAAAAAABIVxS2AwAAAAAAAAAAAAAAAAAAAAAA\\nAAAAAADSFYXtAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIB05WzvBAAAAAAAAAAAmU9ERISmT5+eZJ/K\\nlSurZcuWGZQRACQIDQ3V7du3Vbp0aXunAuAJZc3fQUWLFlWXLl3SZfxDUVFROnXqlKpUqZJ0wgAA\\nAAAAAAAAAAAAZBEOBoPBYO8kAAAAAAAAAADpLyoqSkuXLlVERIQ6dOigggULJto3MDBQJUqUSHK+\\nXr16ac6cOWmcpbn4+HgtX75cly9f1osvvqhSpUql+5p4ct2/f18jRozQTz/9pPj4eEnSmDFj9Omn\\nn6b72nfu3NGePXt0+vRphYWFycXFRfny5VOVKlVUrVo1OTg4pMu6MTExOnPmjI4fP65bt24pLCxM\\nkuTt7S0fHx/5+fmpXLlycnJySpf100p0dLQmT56ssWPH6rvvvlPv3r3TbO7IyEgdPXpUgYGBun79\\nuiIjI2UwGOTl5aUcOXIoT548KleunEqUKJHpH6enzb1793Tw4EEFBgbq9u3bunPnjry8vJQrVy4V\\nK1ZMNWrUkKenp73TTNadO3d06NAhBQYGKjw8XBEREXJycpKX
…[truncated 6411 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T06:57:46.333477+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures/",
  "description": "List local figures directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures/",
    "description": "List local figures directory"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T06:57:46.333681+00:00_

consensus_heatmap.pdf
consensus_heatmap.png
consensus_workflow.pdf
consensus_workflow.png
plot_regime_map.py
regime_map.pdf
regime_map.png
regime_map_fdr.pdf
shapley_method_contribution.pdf
shapley_method_contribution_data.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T06:57:46.333872+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "which python3 && python3 --version && python3 -c \"import matplotlib; print('matplotlib', matplotlib.__version__)\"",
  "description": "Check local Python and matplotlib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Bash",
  "tool_args": {
    "command": "which python3 && python3 --version && python3 -c \"import matplotlib; print('matplotlib', matplotlib.__version__)\"",
    "description": "Check local Python and matplotlib"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T06:57:46.334050+00:00_

Exit code 1
/usr/bin/python3
Python 3.14.4
Traceback (most recent call last):
  File "&lt;string>", line 1, in &lt;module>
    import matplotlib; print('matplotlib', matplotlib.__version__)
    ^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'matplotlib'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T06:57:46.334221+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pip3 install matplotlib numpy",
  "description": "Install matplotlib and numpy locally",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Bash",
  "tool_args": {
    "command": "pip3 install matplotlib numpy",
    "description": "Install matplotlib and numpy locally",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T06:57:46.334431+00:00_

Exit code 1
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.14/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T06:57:46.334622+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -m venv /tmp/plotenv && /tmp/plotenv/bin/pip install matplotlib numpy",
  "description": "Create venv and install matplotlib",
  "timeout": "180000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -m venv /tmp/plotenv && /tmp/plotenv/bin/pip install matplotlib numpy",
    "description": "Create venv and install matplotlib",
    "timeout": "180000"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T06:57:46.334800+00:00_

Requirement already satisfied: matplotlib in /tmp/plotenv/lib/python3.14/site-packages (3.10.9)
Requirement already satisfied: numpy in /tmp/plotenv/lib/python3.14/site-packages (2.4.4)
Requirement already satisfied: contourpy>=1.0.1 in /tmp/plotenv/lib/python3.14/site-packages (from matplotlib) (1.3.3)
Requirement already satisfied: cycler>=0.10 in /tmp/plotenv/lib/python3.14/site-packages (from matplotlib) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /tmp/plotenv/lib/python3.14/site-packages (from matplotlib) (4.63.0)
Requirement already satisfied: kiwisolver>=1.3.1 in /tmp/plotenv/lib/python3.14/site-packages (from matplotlib) (1.5.0)
Requirement already satisfied: packaging>=20.0 in /tmp/plotenv/lib/python3.14/site-packages (from matplotlib) (26.2)
Requirement already satisfied: pillow>=8 in /tmp/plotenv/lib/python3.14/site-packages (from matplotlib) (12.2.0)
Requirement already satisfied: pyparsing>=3 in /tmp/plotenv/lib/python3.14/site-packages (from matplotlib) (3.3.2)
Requirement already satisfied: python-dateutil>=2.7 in /tmp/plotenv/lib/python3.14/site-packages (from matplotlib) (2.9.0.post0)
Requirement already satisfied: six>=1.5 in /tmp/plotenv/lib/python3.14/site-packages (from python-dateutil>=2.7->matplotlib) (1.17.0)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T06:57:46.335057+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/tmp/gen_heatmap.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Generate consensus heatmap from D120 TY-fixed data (hardcoded from server collection).\"\"\"\n\nimport numpy as np\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nfrom matplotlib.colors import LinearSegmentedColormap\nfrom collections import defaultdict\n\n# ── Hardcoded data from 17855 server collection ──\n# Format: (alpha, seed, domain, model, category, {method: (num, den)}, k3, k4)\n# Methods: naive_xcorr, diff_xcorr, threshold_onset, perm_granger, ty_granger\n\nDATA = [\n    # WikiText alpha_sweep\n    (0.05, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (4,8), 'diff_xcorr': (3,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (0,8)},\n     (0,8), (0,8)),\n    (0.10, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (3,8), 'diff_xcorr': (6,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (0,8)},\n     (0,8), (0,8)),\n    (0.10, 43, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (4,8), 'diff_xcorr': (7,8), 'threshold_onset': (2,8), 'perm_granger': (3,8), 'ty_granger': (3,8)},\n     (4,8), (2,8)),\n    (0.25, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (1,8), 'diff_xcorr': (3,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (2,8)},\n     (0,8), (0,8)),\n    (0.25, 43, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (0,8), 'diff_xcorr': (0,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (1,8)},\n     (0,8), (0,8)),\n    (0.25, 44, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (1,8), 'diff_xcorr': (0,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (0,8)},\n     (0,8), (0,8)),\n    (0.30, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (3,8), 'diff_xcorr': (4,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (3,8)},\n     (1,8), (0,8)),\n    (0.35, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (0,8), 'diff_xcorr': (4,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (1,8)},\n     (0,8), (0,8)),\n    (0.40, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (4,8), 'diff_xcorr': (3,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (4,8)},\n     (1,8), (0,8)),\n    (0.45, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (1,8), 'diff_xcorr': (6,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (1,8)},\n     (0,8), (0,8)),\n    (0.50, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (3,8), 'diff_xcorr': (7,8), 'threshold_onset': (4,8), 'perm_granger': (6,8), 'ty_granger': (3,8)},\n     (6,8), (3,8)),\n    (0.50, 43, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (2,8), 'diff_xcorr': (6,8), 'threshold_onset': (6,8), 'perm_granger': (6,8), 'ty_granger': (0,8)},\n     (5,8), (1,8)),\n    (0.50, 44, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (5,8), 'diff_xcorr': (8,8), 'threshold_onset': (0,8), 'perm_granger': (6,8), 'ty_granger': (0,8)},\n     (3,8), (0,8)),\n    (0.60, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (3,8), 'diff_xcorr': (8,8), 'threshold_onset': (0,8), 'perm_granger': (3,8), 'ty_granger': (0,8)},\n     (2,8), (0,8)),\n    (0.60, 43, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (1,8), 'diff_xcorr': (6,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (1,8)},\n     (0,8), (0,8)),\n    (0.75, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (7,8), 'diff_xcorr': (6,8), 'threshold_onset': (0,8), 'perm_granger': (6,8), 'ty_granger': (3,8)},\n     (6,8), (3,8)),\n    # α=1.0 from padding_robustness (WikiText GPT-2)\n    (1.00, 42, 'WikiText', 'GPT-2', 'padding_robustness',\n     {'naive_xcorr': (6,8), 'diff_xcorr': (6,8), 'threshold_onset': (0,8), 'perm_granger': (6,8), 'ty_granger': (0,8)},\n     (6,8), (0,8)),\n\n    # C4\n    (0.25, 42, 'C4', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (4,8), 'diff_xcorr': (8,8), 'threshold_onset': (2,8), 'perm_granger': (0,8), 'ty_granger': (4,8)},\n     (3,8), (0,8)),\n    (0.50, 42, 'C4', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (4,8), 'diff_xcorr': (8,8), 'threshold_onset': (0,8), 'perm_granger': (8,8), 'ty_granger': (2,8)},\n     (6,8), (0,8)),\n    (0.75, 42, 'C4', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (8,8), 'diff_xcorr': (8,8), 'threshold_onset': (0,8), 'perm_granger': (8,8), 'ty_granger': (3,8)},\n     (8,8), (3,8)),\n]\n\nMETHOD_NAMES = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']\nROW_LABELS = {\n    'naive_xcorr': 'Naïve XCorr',\n    'diff_xcorr': 'Diff XCorr (FDR)',\n    'threshold_onset': 'Threshold Onset (3σ)',\n    'perm_granger': 'Perm Granger (FDR)',\n    'ty_granger': 'TY Granger',\n    'K≥3': 'Consensus K≥3',\n    'K≥4': 'Consensus K≥4',\n}\n\ndef build_matrix(records):\n    by_alpha = defaultdict(list)\n    for r in records:\n        by_alpha[r[0]].append(r)\n\n    alphas = sorted(by_alpha.keys())\n    rows = METHOD_NAMES + ['K≥3', 'K≥4']\n\n    matrix = np.full((len(rows), len(alphas)), np.nan)\n    annotations = [['' for _ in alphas] for _ in rows]\n    seed_counts = {}\n\n    for j, alpha in enumerate(alphas):\n        group = by_alpha[alpha]\n        seed_counts[alpha] = len(group)\n\n        for i, method in enumerate(METHOD_NAMES):\n            vals = [r[5][method][0] for r in group if method in r[5]]\n            if vals:\n                avg = np.mean(vals)\n                matrix[i, j] = avg\n                if len(group) == 1:\n                    annotations[i][j] = f\"{int(vals[0])}/8\"\n                else:\n                    annotations[i][j] = f\"{avg:.1f}/8\"\n\n        # K>=3\n        k3_vals = [r[6][0] for r in group]\n        avg = np.mean(k3_vals)\n        matrix[len(METHOD_NAMES), j] = avg\n        if len(group) == 1:\n            annotations[len(METHOD_NAMES)][j] = f\"{int(k3_vals[0])}/8\"\n        else:\n            annotations[len(METHOD_NAMES)][j] = f\"{avg:.1f}/8\"\n\n        # K>=4\n        k4_vals = [r[7][0] for r in group]\n        avg = np.mean(k4_vals)\n        matrix[len(METHOD_NAMES)+1, j] = avg\n        if len(group) == 1:\n            annotations[len(METHOD_NAMES)+1][j] = f\"{int(k4_vals[0])}/8\"\n        else:\n            annotations[len(METHOD_NAMES)+1][j] = f\"{avg:.1f}/8\"\n\n    return alphas, rows, matrix, annotations, seed_counts\n\n# Filter by domain\nwiki_records = [r for r in DATA if r[2] == 'WikiText']\nc4_records = [r for r in DATA if r[2] == 'C4']\n\n# ── Plot ──\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.size': 10,\n    'axes.labelsize': 11,\n    'axes.titlesize': 12,\n    'xtick.labelsize': 9,\n    'ytick.labelsize': 10,\n    'figure.dpi': 300,\n    'mathtext.fontset': 'cm',\n})\n\ncmap = plt.cm.YlOrRd.copy()\ncmap.set_bad(color='#f5f5f5')\n\ndef plot_heatmap(ax, records, title, show_ylabel=True):\n    alphas, rows, matrix, annotations, seed_counts = build_matrix(records)\n\n    im = ax.imshow(matrix, cmap=cmap, vmin=0, vmax=8, aspect='auto',\n                   interpolation='nearest')\n\n    for i in range(len(rows)):\n        for j in range(len(alphas)):\n            val = matrix[i, j]\n            if np.isnan(val):\n                continue\n            color = 'white' if val > 5.5 else 'black'\n            fontsize = 7.5 if len(alphas) > 8 else 8.5\n            ax.text(j, i, annotations[i][j], ha='center', va='center',\n                    fontsize=fontsize, color=color, fontweight='medium')\n\n    ax.set_xticks(range(len(alphas)))\n    xlabels = []\n    for a in alphas:\n        if a == 1.0:\n            xlabels.append('1.0')\n        elif a == 0.05:\n            xlabels.append('.05')\n        else:\n            xlabels.append(f'{a:.2f}'[1:])  # strip leading 0\n    ax.set_xticklabels(xlabels, rotation=0)\n    ax.set_xlabel(r'Canary strength $\\alpha$')\n\n    if show_ylabel:\n        ax.set_yticks(range(len(rows)))\n        ax.set_yticklabels([ROW_LABELS.get(r, r) for r in rows])\n    else:\n        ax.set_yticks(range(len(rows)))\n        ax.set_yticklabels([])\n\n    # Seed count annotation at top\n    for j, alpha in enumerate(alphas):\n        n = seed_counts[alpha]\n        if n > 1:\n            ax.text(j, -0.65, f'n={n}', ha='center', va='center', fontsize=6.5,\n                    color='#666666', style='italic')\n\n    # Separator line between individual methods and consensus rows\n    ax.axhline(y=len(METHOD_NAMES) - 0.5, color='black', linewidth=1.2)\n\n    ax.set_title(title, fontweight='bold', pad=14)\n    ax.tick_params(axis='both', which='both', length=0)\n\n    # Light grid\n    for i in range(len(rows) + 1):\n        ax.axhline(y=i - 0.5, color='white', linewidth=0.5)\n    for j in range(len(alphas) + 1):\n        ax.axvline(x=j - 0.5, color='white', linewidth=0.5)\n\n    return im\n\n# Two-panel figure\nfig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 3.8),\n                                 gridspec_kw={'width_ratios': [len(set(r[0] for r in wiki_records)),\n                                                                len(set(r[0] for r in c4_records))]})\n\nim1 = plot_heatmap(ax1, wiki_records, 'WikiText-103 (GPT-2 Small)')\nim2 = plot_heatmap(ax2, c4_records, 'C4 (GPT-2 Small)', show_ylabel=False)\n\n# Colorbar\ncbar_ax = fig.add_axes([0.93, 0.18, 0.012, 0.65])\ncbar = fig.colorbar(im1, cax=cbar_ax)\ncbar.set_ticks([0, 2, 4, 6, 8])\ncbar.set_ticklabels(['0/8', '2/8', '4/8', '6/8', '8/8'])\ncbar.set_label('Significant pairs', fontsize=9)\n\nplt.subplots_adjust(left=0.145, right=0.915, top=0.88, bottom=0.18, wspace=0.06)\n\noutdir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures'\nfig.savefig(f'{outdir}/fig_consensus_heatmap_d120.pdf', bbox_inches='tight', dpi=300)\nfig.savefig(f'{outdir}/fig_consensus_heatmap_d120.png', bbox_inches='tight', dpi=300)\nprint(f\"Saved to {outdir}/fig_consensus_heatmap_d120.pdf and .png\")\nplt.close()\n\n# ── Print full data matrix as CSV ──\nprint(\"\\n=== FULL DATA MATRIX ===\")\nheader = \"domain,alpha,seed,model,\" + \",\".join(METHOD_NAMES) + \",K>=3,K>=4\"\nprint(header)\nfor r in sorted(DATA, key=lambda x: (x[2], x[0], x[1])):\n    vals = []\n    for m in METHOD_NAMES:\n        if m in r[5]:\n            vals.append(f\"{r[5][m][0]}/{r[5][m][1]}\")\n        else:\n            vals.append(\"\")\n    vals.append(f\"{r[6][0]}/{r[6][1]}\")\n    vals.append(f\"{r[7][0]}/{r[7][1]}\")\n    print(f\"{r[2]},{r[0]},{r[1]},{r[3]},\" + \",\".join(vals))\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Write",
  "tool_args": {
    "file_path": "/tmp/gen_heatmap.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Generate consensus heatmap from D120 TY-fixed data (hardcoded from server collection).\"\"\"\n\nimport numpy as np\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nfrom matplotlib.colors import LinearSegmentedColormap\nfrom collections import defaultdict\n\n# ── Hardcoded data from 17855 server collection ──\n# Format: (alpha, seed, domain, model, category, {method: (num, den)}, k3, k4)\n# Methods: naive_xcorr, diff_xcorr, threshold_onset, perm_granger, ty_granger\n\nDATA = [\n    # WikiText alpha_sweep\n    (0.05, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (4,8), 'diff_xcorr': (3,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (0,8)},\n     (0,8), (0,8)),\n    (0.10, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (3,8), 'diff_xcorr': (6,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (0,8)},\n     (0,8), (0,8)),\n    (0.10, 43, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (4,8), 'diff_xcorr': (7,8), 'threshold_onset': (2,8), 'perm_granger': (3,8), 'ty_granger': (3,8)},\n     (4,8), (2,8)),\n    (0.25, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (1,8), 'diff_xcorr': (3,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (2,8)},\n     (0,8), (0,8)),\n    (0.25, 43, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (0,8), 'diff_xcorr': (0,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (1,8)},\n     (0,8), (0,8)),\n    (0.25, 44, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (1,8), 'diff_xcorr': (0,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (0,8)},\n     (0,8), (0,8)),\n    (0.30, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (3,8), 'diff_xcorr': (4,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (3,8)},\n     (1,8), (0,8)),\n    (0.35, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (0,8), 'diff_xcorr': (4,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (1,8)},\n     (0,8), (0,8)),\n    (0.40, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (4,8), 'diff_xcorr': (3,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (4,8)},\n     (1,8), (0,8)),\n    (0.45, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (1,8), 'diff_xcorr': (6,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (1,8)},\n     (0,8), (0,8)),\n    (0.50, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (3,8), 'diff_xcorr': (7,8), 'threshold_onset': (4,8), 'perm_granger': (6,8), 'ty_granger': (3,8)},\n     (6,8), (3,8)),\n    (0.50, 43, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (2,8), 'diff_xcorr': (6,8), 'threshold_onset': (6,8), 'perm_granger': (6,8), 'ty_granger': (0,8)},\n     (5,8), (1,8)),\n    (0.50, 44, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (5,8), 'diff_xcorr': (8,8), 'threshold_onset': (0,8), 'perm_granger': (6,8), 'ty_granger': (0,8)},\n     (3,8), (0,8)),\n    (0.60, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (3,8), 'diff_xcorr': (8,8), 'threshold_onset': (0,8), 'perm_granger': (3,8), 'ty_granger': (0,8)},\n     (2,8), (0,8)),\n    (0.60, 43, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (1,8), 'diff_xcorr': (6,8), 'threshold_onset': (0,8), 'perm_granger': (0,8), 'ty_granger': (1,8)},\n     (0,8), (0,8)),\n    (0.75, 42, 'WikiText', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (7,8), 'diff_xcorr': (6,8), 'threshold_onset': (0,8), 'perm_granger': (6,8), 'ty_granger': (3,8)},\n     (6,8), (3,8)),\n    # α=1.0 from padding_robustness (WikiText GPT-2)\n    (1.00, 42, 'WikiText', 'GPT-2', 'padding_robustness',\n     {'naive_xcorr': (6,8), 'diff_xcorr': (6,8), 'threshold_onset': (0,8), 'perm_granger': (6,8), 'ty_granger': (0,8)},\n     (6,8), (0,8)),\n\n    # C4\n    (0.25, 42, 'C4', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (4,8), 'diff_xcorr': (8,8), 'threshold_onset': (2,8), 'perm_granger': (0,8), 'ty_granger': (4,8)},\n     (3,8), (0,8)),\n    (0.50, 42, 'C4', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (4,8), 'diff_xcorr': (8,8), 'threshold_onset': (0,8), 'perm_granger': (8,8), 'ty_granger': (2,8)},\n     (6,8), (0,8)),\n    (0.75, 42, 'C4', 'GPT-2', 'alpha_sweep',\n     {'naive_xcorr': (8,8), 'diff_xcorr': (8,8), 'threshold_onset': (0,8), 'perm_granger': (8,8), 'ty_granger': (3,8)},\n     (8,8), (3,8)),\n]\n\nMETHOD_NAMES = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']\nROW_LABELS = {\n    'naive_xcorr': 'Naïve XCorr',\n    'diff_xcorr': 'Diff XCorr (FDR)',\n    'threshold_onset': 'Threshold Onset (3σ)',\n    'perm_granger': 'Perm Granger (FDR)',\n    'ty_granger': 'TY Granger',\n    'K≥3': 'Consensus K≥3',\n    'K≥4': 'Consensus K≥4',\n}\n\ndef build_matrix(records):\n    by_alpha = defaultdict(list)\n    for r in records:\n        by_alpha[r[0]].append(r)\n\n    alphas = sorted(by_alpha.keys())\n    rows = METHOD_NAMES + ['K≥3', 'K≥4']\n\n    matrix = np.full((len(rows), len(alphas)), np.nan)\n    annotations = [['' for _ in alphas] for _ in rows]\n    seed_counts = {}\n\n    for j, alpha in enumerate(alphas):\n        group = by_alpha[alpha]\n        seed_counts[alpha] = len(group)\n\n        for i, method in enumerate(METHOD_NAMES):\n            vals = [r[5][method][0] for r in group if method in r[5]]\n            if vals:\n                avg = np.mean(vals)\n                matrix[i, j] = avg\n                if len(group) == 1:\n                    annotations[i][j] = f\"{int(vals[0])}/8\"\n                else:\n                    annotations[i][j] = f\"{avg:.1f}/8\"\n\n        # K>=3\n        k3_vals = [r[6][0] for r in group]\n        avg = np.mean(k3_vals)\n        matrix[len(METHOD_NAMES), j] = avg\n        if len(group) == 1:\n            annotations[len(METHOD_NAMES)][j] = f\"{int(k3_vals[0])}/8\"\n        else:\n            annotations[len(METHOD_NAMES)][j] = f\"{avg:.1f}/8\"\n\n        # K>=4\n        k4_vals = [r[7][0] for r in group]\n        avg = np.mean(k4_vals)\n        matrix[len(METHOD_NAMES)+1, j] = avg\n        if len(group) == 1:\n            annotations[len(METHOD_NAMES)+1][j] = f\"{int(k4_vals[0])}/8\"\n        else:\n            annotations[len(METHOD_NAMES)+1][j] = f\"{avg:.1f}/8\"\n\n    return alphas, rows, matrix, annotations, seed_counts\n\n# Filter by domain\nwiki_records = [r for r in DATA if r[2] == 'WikiText']\nc4_records = [r for r in DATA if r[2] == 'C4']\n\n# ── Plot ──\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.size': 10,\n    'axes.labelsize': 11,\n    'axes.titlesize': 12,\n    'xtick.labelsize': 9,\n    'ytick.labelsize': 10,\n    'figure.dpi': 300,\n    'mathtext.fontset': 'cm',\n})\n\ncmap = plt.cm.YlOrRd.copy()\ncmap.set_bad(color='#f5f5f5')\n\ndef plot_heatmap(ax, records, title, show_ylabel=True):\n    alphas, rows, matrix, annotations, seed_counts = build_matrix(records)\n\n    im = ax.imshow(matrix, cmap=cmap, vmin=0, vmax=8, aspect='auto',\n                   interpolation='nearest')\n\n    for i in range(len(rows)):\n        for j in range(len(alphas)):\n            val = matrix[i, j]\n            if np.isnan(val):\n                continue\n            color = 'white' if val > 5.5 else 'black'\n            fontsize = 7.5 if len(alphas) > 8 else 8.5\n            ax.text(j, i, annotations[i][j], ha='center', va='center',\n                    fontsize=fontsize, color=color, fontweight='medium')\n\n    ax.set_xticks(range(len(alphas)))\n    xlabels = []\n    for a in alphas:\n        if a == 1.0:\n            xlabels.append('1.0')\n        elif a == 0.05:\n            xlabels.append('.05')\n        else:\n            xlabels.append(f'{a:.2f}'[1:])  # strip leading 0\n    ax.set_xticklabels(xlabels, rotation=0)\n    ax.set_xlabel(r'Canary strength $\\alpha$')\n\n    if show_ylabel:\n        ax.set_yticks(range(len(rows)))\n        ax.set_yticklabels([ROW_LABELS.get(r, r) for r in rows])\n    else:\n        ax.set_yticks(range(len(rows)))\n        ax.set_yticklabels([])\n\n    # Seed count annotation at top\n    for j, alpha in enumerate(alphas):\n        n = seed_counts[alpha]\n        if n > 1:\n            ax.text(j, -0.65, f'n={n}', ha='center', va='center', fontsize=6.5,\n                    color='#666666', style='italic')\n\n    # Separator line between individual methods and consensus rows\n    ax.axhline(y=len(METHOD_NAMES) - 0.5, color='black', linewidth=1.2)\n\n    ax.set_title(title, fontweight='bold', pad=14)\n    ax.tick_params(axis='both', which='both', length=0)\n\n    # Light grid\n    for i in range(len(rows) + 1):\n        ax.axhline(y=i - 0.5, color='white', linewidth=0.5)\n    for j in range(len(alphas) + 1):\n        ax.axvline(x=j - 0.5, color='white', linewidth=0.5)\n\n    return im\n\n# Two-panel figure\nfig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 3.8),\n                                 gridspec_kw={'width_ratios': [len(set(r[0] for r in wiki_records)),\n                                                                len(set(r[0] for r in c4_records))]})\n\nim1 = plot_heatmap(ax1, wiki_records, 'WikiText-103 (GPT-2 Small)')\nim2 = plot_heatmap(ax2, c4_records, 'C4 (GPT-2 Small)', show_ylabel=False)\n\n# Colorbar\ncbar_ax = fig.add_axes([0.93, 0.18, 0.012, 0.65])\ncbar = fig.colorbar(im1, cax=cbar_ax)\ncbar.set_ticks([0, 2, 4, 6, 8])\ncbar.set_ticklabels(['0/8', '2/8', '4/8', '6/8', '8/8'])\ncbar.set_label('Significant pairs', fontsize=9)\n\nplt.subplots_adjust(left=0.145, right=0.915, top=0.88, bottom=0.18, wspace=0.06)\n\noutdir = '/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures'\nfig.savefig(f'{outdir}/fig_consensus_heatmap_d120.pdf', bbox_inches='tight', dpi=300)\nfig.savefig(f'{outdir}/fig_consensus_heatmap_d120.png', bbox_inches='tight', dpi=300)\nprint(f\"Saved to {outdir}/fig_consensus_heatmap_d120.pdf and .png\")\nplt.close()\n\n# ── Print full data matrix as CSV ──\nprint(\"\\n=== FULL DATA MATRIX ===\")\nheader = \"domain,alpha,seed,model,\" + \",\".join(METHOD_NAMES) + \",K>=3,K>=4\"\nprint(header)\nfor r in sorted(DATA, key=lambda x: (x[2], x[0], x[1])):\n    vals = []\n    for m in METHOD_NAMES:\n        if m in r[5]:\n            vals.append(f\"{r[5][m][0]}/{r[5][m][1]}\")\n        else:\n            vals.append(\"\")\n    vals.append(f\"{r[6][0]}/{r[6][1]}\")\n    vals.append(f\"{r[7][0]}/{r[7][1]}\")\n    print(f\"{r[2]},{r[0]},{r[1]},{r[3]},\" + \",\".join(vals))\n"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T06:57:46.335480+00:00_

File created successfully at: /tmp/gen_heatmap.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T06:57:46.335688+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "/tmp/plotenv/bin/python /tmp/gen_heatmap.py",
  "description": "Generate consensus heatmap locally"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Bash",
  "tool_args": {
    "command": "/tmp/plotenv/bin/python /tmp/gen_heatmap.py",
    "description": "Generate consensus heatmap locally"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T06:57:46.335873+00:00_

Saved to /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures/fig_consensus_heatmap_d120.pdf and .png

=== FULL DATA MATRIX ===
domain,alpha,seed,model,naive_xcorr,diff_xcorr,threshold_onset,perm_granger,ty_granger,K>=3,K>=4
C4,0.25,42,GPT-2,4/8,8/8,2/8,0/8,4/8,3/8,0/8
C4,0.5,42,GPT-2,4/8,8/8,0/8,8/8,2/8,6/8,0/8
C4,0.75,42,GPT-2,8/8,8/8,0/8,8/8,3/8,8/8,3/8
WikiText,0.05,42,GPT-2,4/8,3/8,0/8,0/8,0/8,0/8,0/8
WikiText,0.1,42,GPT-2,3/8,6/8,0/8,0/8,0/8,0/8,0/8
WikiText,0.1,43,GPT-2,4/8,7/8,2/8,3/8,3/8,4/8,2/8
WikiText,0.25,42,GPT-2,1/8,3/8,0/8,0/8,2/8,0/8,0/8
WikiText,0.25,43,GPT-2,0/8,0/8,0/8,0/8,1/8,0/8,0/8
WikiText,0.25,44,GPT-2,1/8,0/8,0/8,0/8,0/8,0/8,0/8
WikiText,0.3,42,GPT-2,3/8,4/8,0/8,0/8,3/8,1/8,0/8
WikiText,0.35,42,GPT-2,0/8,4/8,0/8,0/8,1/8,0/8,0/8
WikiText,0.4,42,GPT-2,4/8,3/8,0/8,0/8,4/8,1/8,0/8
WikiText,0.45,42,GPT-2,1/8,6/8,0/8,0/8,1/8,0/8,0/8
WikiText,0.5,42,GPT-2,3/8,7/8,4/8,6/8,3/8,6/8,3/8
WikiText,0.5,43,GPT-2,2/8,6/8,6/8,6/8,0/8,5/8,1/8
WikiText,0.5,44,GPT-2,5/8,8/8,0/8,6/8,0/8,3/8,0/8
WikiText,0.6,42,GPT-2,3/8,8/8,0/8,3/8,0/8,2/8,0/8
WikiText,0.6,43,GPT-2,1/8,6/8,0/8,0/8,1/8,0/8,0/8
WikiText,0.75,42,GPT-2,7/8,6/8,0/8,6/8,3/8,6/8,3/8
WikiText,1.0,42,GPT-2,6/8,6/8,0/8,6/8,0/8,6/8,0/8

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T06:57:46.336103+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures/fig_consensus_heatmap_d120.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures/fig_consensus_heatmap_d120.png"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T06:57:46.336758+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T06:57:46.336958+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures/consensus_heatmap_d120_data.csv",
  "content": "domain,alpha,seed,model,naive_xcorr,diff_xcorr,threshold_onset,perm_granger,ty_granger,K>=3,K>=4\nC4,0.25,42,GPT-2,4/8,8/8,2/8,0/8,4/8,3/8,0/8\nC4,0.50,42,GPT-2,4/8,8/8,0/8,8/8,2/8,6/8,0/8\nC4,0.75,42,GPT-2,8/8,8/8,0/8,8/8,3/8,8/8,3/8\nWikiText,0.05,42,GPT-2,4/8,3/8,0/8,0/8,0/8,0/8,0/8\nWikiText,0.10,42,GPT-2,3/8,6/8,0/8,0/8,0/8,0/8,0/8\nWikiText,0.10,43,GPT-2,4/8,7/8,2/8,3/8,3/8,4/8,2/8\nWikiText,0.25,42,GPT-2,1/8,3/8,0/8,0/8,2/8,0/8,0/8\nWikiText,0.25,43,GPT-2,0/8,0/8,0/8,0/8,1/8,0/8,0/8\nWikiText,0.25,44,GPT-2,1/8,0/8,0/8,0/8,0/8,0/8,0/8\nWikiText,0.30,42,GPT-2,3/8,4/8,0/8,0/8,3/8,1/8,0/8\nWikiText,0.35,42,GPT-2,0/8,4/8,0/8,0/8,1/8,0/8,0/8\nWikiText,0.40,42,GPT-2,4/8,3/8,0/8,0/8,4/8,1/8,0/8\nWikiText,0.45,42,GPT-2,1/8,6/8,0/8,0/8,1/8,0/8,0/8\nWikiText,0.50,42,GPT-2,3/8,7/8,4/8,6/8,3/8,6/8,3/8\nWikiText,0.50,43,GPT-2,2/8,6/8,6/8,6/8,0/8,5/8,1/8\nWikiText,0.50,44,GPT-2,5/8,8/8,0/8,6/8,0/8,3/8,0/8\nWikiText,0.60,42,GPT-2,3/8,8/8,0/8,3/8,0/8,2/8,0/8\nWikiText,0.60,43,GPT-2,1/8,6/8,0/8,0/8,1/8,0/8,0/8\nWikiText,0.75,42,GPT-2,7/8,6/8,0/8,6/8,3/8,6/8,3/8\nWikiText,1.00,42,GPT-2,6/8,6/8,0/8,6/8,0/8,6/8,0/8\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures/consensus_heatmap_d120_data.csv",
    "content": "domain,alpha,seed,model,naive_xcorr,diff_xcorr,threshold_onset,perm_granger,ty_granger,K>=3,K>=4\nC4,0.25,42,GPT-2,4/8,8/8,2/8,0/8,4/8,3/8,0/8\nC4,0.50,42,GPT-2,4/8,8/8,0/8,8/8,2/8,6/8,0/8\nC4,0.75,42,GPT-2,8/8,8/8,0/8,8/8,3/8,8/8,3/8\nWikiText,0.05,42,GPT-2,4/8,3/8,0/8,0/8,0/8,0/8,0/8\nWikiText,0.10,42,GPT-2,3/8,6/8,0/8,0/8,0/8,0/8,0/8\nWikiText,0.10,43,GPT-2,4/8,7/8,2/8,3/8,3/8,4/8,2/8\nWikiText,0.25,42,GPT-2,1/8,3/8,0/8,0/8,2/8,0/8,0/8\nWikiText,0.25,43,GPT-2,0/8,0/8,0/8,0/8,1/8,0/8,0/8\nWikiText,0.25,44,GPT-2,1/8,0/8,0/8,0/8,0/8,0/8,0/8\nWikiText,0.30,42,GPT-2,3/8,4/8,0/8,0/8,3/8,1/8,0/8\nWikiText,0.35,42,GPT-2,0/8,4/8,0/8,0/8,1/8,0/8,0/8\nWikiText,0.40,42,GPT-2,4/8,3/8,0/8,0/8,4/8,1/8,0/8\nWikiText,0.45,42,GPT-2,1/8,6/8,0/8,0/8,1/8,0/8,0/8\nWikiText,0.50,42,GPT-2,3/8,7/8,4/8,6/8,3/8,6/8,3/8\nWikiText,0.50,43,GPT-2,2/8,6/8,6/8,6/8,0/8,5/8,1/8\nWikiText,0.50,44,GPT-2,5/8,8/8,0/8,6/8,0/8,3/8,0/8\nWikiText,0.60,42,GPT-2,3/8,8/8,0/8,3/8,0/8,2/8,0/8\nWikiText,0.60,43,GPT-2,1/8,6/8,0/8,0/8,1/8,0/8,0/8\nWikiText,0.75,42,GPT-2,7/8,6/8,0/8,6/8,3/8,6/8,3/8\nWikiText,1.00,42,GPT-2,6/8,6/8,0/8,6/8,0/8,6/8,0/8\n"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T06:57:46.337102+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/figures/consensus_heatmap_d120_data.csv

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-20T06:57:46.337291+00:00_

产出文件：

- **PDF**: `artifacts/figures/fig_consensus_heatmap_d120.pdf`
- **PNG**: `artifacts/figures/fig_consensus_heatmap_d120.png`
- **数据表**: `artifacts/figures/consensus_heatmap_d120_data.csv`

几个要点：

1. **α=0.60 异常偏低**（K≥3 平均仅 1.0/8）。原因：s42 来自 `a060_s42_fp32_v3_d080`（v3 decay=0.80 变体，非标准设置），s43 才是标准实验。如果要排除 v3_d080，α=0.60 只剩 s43 单 seed 且 K≥3=0/8。
2. **α=0.05 也来自 v3_d080 变体**（`a005_s42_fp32_v3_d080`），非标准 alpha_sweep，酌情是否纳入。
3. **α=1.00 来自 padding_robustness** 实验（非 alpha_sweep），因 alpha_sweep 无 α=1.0 实验而补入。
4. **Threshold Onset 全面塌陷**：D120 true 3σ 修复后，除 α=0.50 (s42: 4/8, s43: 6/8) 和 C4 α=0.25 (2/8) 外，其余全部 0/8。
5. **TY Granger 信号明显减弱**：D120 signonly bug 修复后，TY 在大多数 α 下降至 0-4/8，不再像之前虚高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_fig_consensus_heatmap_d120_20260520T065207"
}
```

</details>

---
