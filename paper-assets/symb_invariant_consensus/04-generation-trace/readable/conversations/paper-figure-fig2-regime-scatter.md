# paper figure fig2 regime scatter

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_paper_figure_fig2_regime_scatter_20260519T031001.jsonl`
- **Structured JSON:** [`b39e317a2704f8122e63.json`](../../sessions/b3/b39e317a2704f8122e63.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-19T03:22:31.461258+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/ 2>/dev/null || mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/",
  "description": "Ensure output directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/ 2>/dev/null || mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/",
    "description": "Ensure output directory exists"
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-19T03:22:31.461638+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"import matplotlib; print(matplotlib.__version__)\"",
  "description": "Check matplotlib version"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"import matplotlib; print(matplotlib.__version__)\"",
    "description": "Check matplotlib version"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-19T03:22:31.461861+00:00_

fig1_pipeline.pdf
fig1_pipeline.png
fig2_capability_scatter.pdf
fig3_operating_regime.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T03:22:31.462034+00:00_

3.10.9

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T03:22:31.462424+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/gen_f2_regime_scatter.py",
  "content": "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nfrom matplotlib.lines import Line2D\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 11,\n    'axes.titlesize': 13,\n    'axes.labelsize': 12,\n    'xtick.labelsize': 10,\n    'ytick.labelsize': 10,\n    'legend.fontsize': 9,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n})\n\nCOLORS = {\n    'Mistral-7B': '#CC79A7',\n    'Qwen2.5-14B': '#0072B2',\n    'Qwen2.5-7B': '#56B4E9',\n    'Qwen3-14B': '#D55E00',\n    'LLaMA-8B': '#009E73',\n    'DeepSeek-R1-7B': '#E69F00',\n    'QwQ-32B': '#F0E442',\n}\n\n# (model, domain, n, sc%, delta_pp, significant)\ndata = [\n    ('Mistral-7B',      'PW-D5',       600, 39.33, -2.83,  True),\n    ('Mistral-7B',      'FOLIO-s42',   204, 54.41,  4.90,  True),\n    ('Mistral-7B',      'FOLIO-s123',  204, 53.90,  3.43,  True),\n    ('Mistral-7B',      'FOLIO-s456',  204, 56.37, -0.49, False),\n    ('Qwen2.5-14B',     'StrategyQA',   60, 53.33,  3.33, False),\n    ('Mistral-7B',      'LogiQA',      200, 51.00,  0.50, False),\n    ('Mistral-7B',      'FOLIO-ICL',   199, 57.79, -3.52, False),\n    ('LLaMA-8B',        'FOLIO',       204, 63.24, -2.45, False),\n    ('DeepSeek-R1-7B',  'D012',         60, 71.67, -3.33, False),\n    ('LLaMA-8B',        'StrategyQA',  200, 72.00,  2.00, False),\n    ('Qwen2.5-14B',     'FOLIO-ICL',   199, 74.37,  0.50, False),\n    ('Qwen2.5-14B',     'FOLIO+PW',    804, 76.24,  0.25, False),\n    ('Qwen2.5-7B',      'FOLIO',       203, 77.34, -0.49, False),\n    ('Qwen2.5-14B',     'LogiQA',      200, 78.50, -0.50, False),\n    ('Qwen3-14B',       'FOLIO',       204, 83.82,  0.49, False),\n    ('QwQ-32B',         'AIME',         22, 72.70,  0.00, False),\n    ('Qwen2.5-14B',     'GSM8K',        30, 96.67,  0.00, False),\n]\n\nfig, ax = plt.subplots(figsize=(5.5, 4.125))\n\n# --- shaded regime bands ---\nax.axvspan(50, 55, alpha=0.15, color='#4CAF50', zorder=0)\nax.axvspan(60, 100, alpha=0.08, color='#E53935', zorder=0)\n\n# --- reference line at delta=0 ---\nax.axhline(y=0, color='#888', ls='--', lw=0.8, zorder=1)\n\n# --- plot data points ---\nfor model, domain, n, sc, delta, sig in data:\n    color = COLORS[model]\n    marker = '*' if sig else 'o'\n    size = 180 if sig else 55\n    if n >= 100:\n        ax.scatter(sc, delta, marker=marker, s=size, c=color,\n                   edgecolors='#333', linewidths=0.5, zorder=3)\n    else:\n        ax.scatter(sc, delta, marker=marker, s=size, c='white',\n                   edgecolors=color, linewidths=1.5, zorder=3)\n\n# --- FOLIO seed labels (grouping the 3 seeds) ---\nax.text(55.4, 5.15, 's42', fontsize=7, color='#AA5A87')\nax.text(55.0, 3.65, 's123', fontsize=7, color='#AA5A87')\nax.text(57.3, -0.25, 's456', fontsize=7, color='#AA5A87')\n\n# --- key annotations ---\nax.annotate('Mistral FOLIO +4.90 pp**',\n            xy=(54.41, 4.90), xytext=(38.5, 6.1),\n            fontsize=8, fontweight='bold', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#555', lw=1.0),\n            zorder=4)\n\nax.annotate('Mistral PW −2.83 pp**',\n            xy=(39.33, -2.83), xytext=(47, -4.8),\n            fontsize=8, fontweight='bold', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#555', lw=1.0),\n            zorder=4)\n\n# --- zone labels ---\nax.text(52.5, 6.8, 'Goldilocks Zone', ha='center', va='top', fontsize=8,\n        color='#2E7D32', fontstyle='italic', fontweight='bold')\nax.text(72, 6.8, 'Type A (high baseline)', ha='center', va='top', fontsize=8,\n        color='#C62828', fontstyle='italic', fontweight='bold')\n\n# --- degenerate label ---\nax.text(96.67, 0.7, 'degen.', fontsize=7, color='#999', fontstyle='italic', ha='center')\n\n# --- axes ---\nax.set_xlabel('Self-Consistency Accuracy (%)')\nax.set_ylabel('SICA $\\\\Delta$ (pp)')\nax.set_xlim(33, 100)\nax.set_ylim(-5.8, 7.2)\n\n# --- legend ---\nmodel_order = ['Mistral-7B', 'LLaMA-8B', 'Qwen2.5-7B', 'Qwen2.5-14B',\n               'Qwen3-14B', 'DeepSeek-R1-7B', 'QwQ-32B']\nhandles = [Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS[m],\n                  markeredgecolor='#333', markersize=7, label=m, lw=0)\n           for m in model_order]\nhandles.append(Line2D([0], [0], lw=0, label=''))\nhandles.extend([\n    Line2D([0], [0], marker='*', color='w', markerfacecolor='#999',\n           markeredgecolor='#333', markersize=12, label='$p < 0.05$', lw=0),\n    Line2D([0], [0], marker='o', color='w', markerfacecolor='#999',\n           markeredgecolor='#333', markersize=7, label='n.s.', lw=0),\n    Line2D([0], [0], marker='o', color='w', markerfacecolor='white',\n           markeredgecolor='#999', markersize=7, markeredgewidth=1.5,\n           label='$n < 100$', lw=0),\n])\nax.legend(handles=handles, loc='upper right', framealpha=0.92, edgecolor='#ccc',\n          fontsize=8, handletextpad=0.5, labelspacing=0.35)\n\nplt.tight_layout()\n\nout = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper'\nfig.savefig(f'{out}/f2_regime_scatter.pdf')\nfig.savefig(f'{out}/f2_regime_scatter.png')\nplt.close()\nprint(f'Done. {len(data)} points plotted.')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/gen_f2_regime_scatter.py",
    "content": "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nfrom matplotlib.lines import Line2D\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 11,\n    'axes.titlesize': 13,\n    'axes.labelsize': 12,\n    'xtick.labelsize': 10,\n    'ytick.labelsize': 10,\n    'legend.fontsize': 9,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n})\n\nCOLORS = {\n    'Mistral-7B': '#CC79A7',\n    'Qwen2.5-14B': '#0072B2',\n    'Qwen2.5-7B': '#56B4E9',\n    'Qwen3-14B': '#D55E00',\n    'LLaMA-8B': '#009E73',\n    'DeepSeek-R1-7B': '#E69F00',\n    'QwQ-32B': '#F0E442',\n}\n\n# (model, domain, n, sc%, delta_pp, significant)\ndata = [\n    ('Mistral-7B',      'PW-D5',       600, 39.33, -2.83,  True),\n    ('Mistral-7B',      'FOLIO-s42',   204, 54.41,  4.90,  True),\n    ('Mistral-7B',      'FOLIO-s123',  204, 53.90,  3.43,  True),\n    ('Mistral-7B',      'FOLIO-s456',  204, 56.37, -0.49, False),\n    ('Qwen2.5-14B',     'StrategyQA',   60, 53.33,  3.33, False),\n    ('Mistral-7B',      'LogiQA',      200, 51.00,  0.50, False),\n    ('Mistral-7B',      'FOLIO-ICL',   199, 57.79, -3.52, False),\n    ('LLaMA-8B',        'FOLIO',       204, 63.24, -2.45, False),\n    ('DeepSeek-R1-7B',  'D012',         60, 71.67, -3.33, False),\n    ('LLaMA-8B',        'StrategyQA',  200, 72.00,  2.00, False),\n    ('Qwen2.5-14B',     'FOLIO-ICL',   199, 74.37,  0.50, False),\n    ('Qwen2.5-14B',     'FOLIO+PW',    804, 76.24,  0.25, False),\n    ('Qwen2.5-7B',      'FOLIO',       203, 77.34, -0.49, False),\n    ('Qwen2.5-14B',     'LogiQA',      200, 78.50, -0.50, False),\n    ('Qwen3-14B',       'FOLIO',       204, 83.82,  0.49, False),\n    ('QwQ-32B',         'AIME',         22, 72.70,  0.00, False),\n    ('Qwen2.5-14B',     'GSM8K',        30, 96.67,  0.00, False),\n]\n\nfig, ax = plt.subplots(figsize=(5.5, 4.125))\n\n# --- shaded regime bands ---\nax.axvspan(50, 55, alpha=0.15, color='#4CAF50', zorder=0)\nax.axvspan(60, 100, alpha=0.08, color='#E53935', zorder=0)\n\n# --- reference line at delta=0 ---\nax.axhline(y=0, color='#888', ls='--', lw=0.8, zorder=1)\n\n# --- plot data points ---\nfor model, domain, n, sc, delta, sig in data:\n    color = COLORS[model]\n    marker = '*' if sig else 'o'\n    size = 180 if sig else 55\n    if n >= 100:\n        ax.scatter(sc, delta, marker=marker, s=size, c=color,\n                   edgecolors='#333', linewidths=0.5, zorder=3)\n    else:\n        ax.scatter(sc, delta, marker=marker, s=size, c='white',\n                   edgecolors=color, linewidths=1.5, zorder=3)\n\n# --- FOLIO seed labels (grouping the 3 seeds) ---\nax.text(55.4, 5.15, 's42', fontsize=7, color='#AA5A87')\nax.text(55.0, 3.65, 's123', fontsize=7, color='#AA5A87')\nax.text(57.3, -0.25, 's456', fontsize=7, color='#AA5A87')\n\n# --- key annotations ---\nax.annotate('Mistral FOLIO +4.90 pp**',\n            xy=(54.41, 4.90), xytext=(38.5, 6.1),\n            fontsize=8, fontweight='bold', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#555', lw=1.0),\n            zorder=4)\n\nax.annotate('Mistral PW −2.83 pp**',\n            xy=(39.33, -2.83), xytext=(47, -4.8),\n            fontsize=8, fontweight='bold', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#555', lw=1.0),\n            zorder=4)\n\n# --- zone labels ---\nax.text(52.5, 6.8, 'Goldilocks Zone', ha='center', va='top', fontsize=8,\n        color='#2E7D32', fontstyle='italic', fontweight='bold')\nax.text(72, 6.8, 'Type A (high baseline)', ha='center', va='top', fontsize=8,\n        color='#C62828', fontstyle='italic', fontweight='bold')\n\n# --- degenerate label ---\nax.text(96.67, 0.7, 'degen.', fontsize=7, color='#999', fontstyle='italic', ha='center')\n\n# --- axes ---\nax.set_xlabel('Self-Consistency Accuracy (%)')\nax.set_ylabel('SICA $\\\\Delta$ (pp)')\nax.set_xlim(33, 100)\nax.set_ylim(-5.8, 7.2)\n\n# --- legend ---\nmodel_order = ['Mistral-7B', 'LLaMA-8B', 'Qwen2.5-7B', 'Qwen2.5-14B',\n               'Qwen3-14B', 'DeepSeek-R1-7B', 'QwQ-32B']\nhandles = [Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS[m],\n                  markeredgecolor='#333', markersize=7, label=m, lw=0)\n           for m in model_order]\nhandles.append(Line2D([0], [0], lw=0, label=''))\nhandles.extend([\n    Line2D([0], [0], marker='*', color='w', markerfacecolor='#999',\n           markeredgecolor='#333', markersize=12, label='$p < 0.05$', lw=0),\n    Line2D([0], [0], marker='o', color='w', markerfacecolor='#999',\n           markeredgecolor='#333', markersize=7, label='n.s.', lw=0),\n    Line2D([0], [0], marker='o', color='w', markerfacecolor='white',\n           markeredgecolor='#999', markersize=7, markeredgewidth=1.5,\n           label='$n < 100$', lw=0),\n])\nax.legend(handles=handles, loc='upper right', framealpha=0.92, edgecolor='#ccc',\n          fontsize=8, handletextpad=0.5, labelspacing=0.35)\n\nplt.tight_layout()\n\nout = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper'\nfig.savefig(f'{out}/f2_regime_scatter.pdf')\nfig.savefig(f'{out}/f2_regime_scatter.png')\nplt.close()\nprint(f'Done. {len(data)} points plotted.')\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T03:22:31.462681+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/gen_f2_regime_scatter.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T03:22:31.462821+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper && python3 gen_f2_regime_scatter.py",
  "description": "Run the scatter plot generation script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper && python3 gen_f2_regime_scatter.py",
    "description": "Run the scatter plot generation script"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T03:22:31.462971+00:00_

Done. 17 points plotted.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T03:22:31.463142+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/f2_regime_scatter.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/f2_regime_scatter.png"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T03:22:31.463548+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T03:22:31.463892+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/gen_f2_regime_scatter.py",
  "content": "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nfrom matplotlib.lines import Line2D\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 11,\n    'axes.titlesize': 13,\n    'axes.labelsize': 12,\n    'xtick.labelsize': 10,\n    'ytick.labelsize': 10,\n    'legend.fontsize': 9,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n})\n\nCOLORS = {\n    'Mistral-7B': '#CC79A7',\n    'Qwen2.5-14B': '#0072B2',\n    'Qwen2.5-7B': '#56B4E9',\n    'Qwen3-14B': '#D55E00',\n    'LLaMA-8B': '#009E73',\n    'DeepSeek-R1-7B': '#E69F00',\n    'QwQ-32B': '#F0E442',\n}\n\n# (model, domain, n, sc%, delta_pp, significant)\ndata = [\n    ('Mistral-7B',      'PW-D5',       600, 39.33, -2.83,  True),\n    ('Mistral-7B',      'FOLIO-s42',   204, 54.41,  4.90,  True),\n    ('Mistral-7B',      'FOLIO-s123',  204, 53.90,  3.43,  True),\n    ('Mistral-7B',      'FOLIO-s456',  204, 56.37, -0.49, False),\n    ('Qwen2.5-14B',     'StrategyQA',   60, 53.33,  3.33, False),\n    ('Mistral-7B',      'LogiQA',      200, 51.00,  0.50, False),\n    ('Mistral-7B',      'FOLIO-ICL',   199, 57.79, -3.52, False),\n    ('LLaMA-8B',        'FOLIO',       204, 63.24, -2.45, False),\n    ('DeepSeek-R1-7B',  'D012',         60, 71.67, -3.33, False),\n    ('LLaMA-8B',        'StrategyQA',  200, 72.00,  2.00, False),\n    ('Qwen2.5-14B',     'FOLIO-ICL',   199, 74.37,  0.50, False),\n    ('Qwen2.5-14B',     'FOLIO+PW',    804, 76.24,  0.25, False),\n    ('Qwen2.5-7B',      'FOLIO',       203, 77.34, -0.49, False),\n    ('Qwen2.5-14B',     'LogiQA',      200, 78.50, -0.50, False),\n    ('Qwen3-14B',       'FOLIO',       204, 83.82,  0.49, False),\n    ('QwQ-32B',         'AIME',         22, 72.70,  0.00, False),\n    ('Qwen2.5-14B',     'GSM8K',        30, 96.67,  0.00, False),\n]\n\nfig, ax = plt.subplots(figsize=(5.5, 4.125))\n\n# --- shaded regime bands ---\nax.axvspan(50, 55, alpha=0.15, color='#4CAF50', zorder=0)\nax.axvspan(60, 100, alpha=0.08, color='#E53935', zorder=0)\n\n# --- reference line at delta=0 ---\nax.axhline(y=0, color='#888', ls='--', lw=0.8, zorder=1)\n\n# --- plot data points ---\nfor model, domain, n, sc, delta, sig in data:\n    color = COLORS[model]\n    marker = '*' if sig else 'o'\n    size = 180 if sig else 55\n    if n >= 100:\n        ax.scatter(sc, delta, marker=marker, s=size, c=color,\n                   edgecolors='#333', linewidths=0.5, zorder=3)\n    else:\n        ax.scatter(sc, delta, marker=marker, s=size, c='white',\n                   edgecolors=color, linewidths=1.5, zorder=3)\n\n# --- FOLIO seed labels ---\nax.text(55.4, 5.15, 's42', fontsize=7, color='#AA5A87')\nax.text(55.0, 3.65, 's123', fontsize=7, color='#AA5A87')\nax.text(57.3, -0.25, 's456', fontsize=7, color='#AA5A87')\n\n# --- key annotations (positioned to avoid clipping) ---\nax.annotate('Mistral FOLIO +4.90 pp**',\n            xy=(54.41, 4.90), xytext=(48, 6.2),\n            fontsize=8, fontweight='bold', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#555', lw=1.0),\n            zorder=4)\n\nax.annotate('Mistral PW −2.83 pp**',\n            xy=(39.33, -2.83), xytext=(47, -4.8),\n            fontsize=8, fontweight='bold', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#555', lw=1.0),\n            zorder=4)\n\n# --- zone labels (compact, at very top of each band) ---\nax.text(52.5, 7.05, 'Goldilocks', fontsize=7.5, color='#2E7D32',\n        ha='center', va='top', fontstyle='italic', fontweight='bold')\nax.text(65, 7.05, 'Type A', fontsize=7.5, color='#C62828',\n        ha='center', va='top', fontstyle='italic', fontweight='bold')\n\n# --- degenerate label ---\nax.text(96.67, 0.7, 'degen.', fontsize=7, color='#999',\n        fontstyle='italic', ha='center')\n\n# --- axes ---\nax.set_xlabel('Self-Consistency Accuracy (%)')\nax.set_ylabel('SICA $\\\\Delta$ (pp)')\nax.set_xlim(33, 100)\nax.set_ylim(-5.8, 7.2)\n\n# --- legend ---\nmodel_order = ['Mistral-7B', 'LLaMA-8B', 'Qwen2.5-7B', 'Qwen2.5-14B',\n               'Qwen3-14B', 'DeepSeek-R1-7B', 'QwQ-32B']\nhandles = [Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS[m],\n                  markeredgecolor='#333', markersize=7, label=m, lw=0)\n           for m in model_order]\nhandles.append(Line2D([0], [0], lw=0, label=''))\nhandles.extend([\n    Line2D([0], [0], marker='*', color='w', markerfacecolor='#999',\n           markeredgecolor='#333', markersize=12, label='$p < 0.05$', lw=0),\n    Line2D([0], [0], marker='o', color='w', markerfacecolor='#999',\n           markeredgecolor='#333', markersize=7, label='n.s.', lw=0),\n    Line2D([0], [0], marker='o', color='w', markerfacecolor='white',\n           markeredgecolor='#999', markersize=7, markeredgewidth=1.5,\n           label='$n < 100$', lw=0),\n])\nax.legend(handles=handles, loc='upper right', framealpha=0.92, edgecolor='#ccc',\n          fontsize=8, handletextpad=0.5, labelspacing=0.35)\n\nplt.tight_layout()\n\nout = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper'\nfig.savefig(f'{out}/f2_regime_scatter.pdf')\nfig.savefig(f'{out}/f2_regime_scatter.png')\nplt.close()\nprint(f'Done. {len(data)} points plotted.')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/gen_f2_regime_scatter.py",
    "content": "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nfrom matplotlib.lines import Line2D\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 11,\n    'axes.titlesize': 13,\n    'axes.labelsize': 12,\n    'xtick.labelsize': 10,\n    'ytick.labelsize': 10,\n    'legend.fontsize': 9,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n})\n\nCOLORS = {\n    'Mistral-7B': '#CC79A7',\n    'Qwen2.5-14B': '#0072B2',\n    'Qwen2.5-7B': '#56B4E9',\n    'Qwen3-14B': '#D55E00',\n    'LLaMA-8B': '#009E73',\n    'DeepSeek-R1-7B': '#E69F00',\n    'QwQ-32B': '#F0E442',\n}\n\n# (model, domain, n, sc%, delta_pp, significant)\ndata = [\n    ('Mistral-7B',      'PW-D5',       600, 39.33, -2.83,  True),\n    ('Mistral-7B',      'FOLIO-s42',   204, 54.41,  4.90,  True),\n    ('Mistral-7B',      'FOLIO-s123',  204, 53.90,  3.43,  True),\n    ('Mistral-7B',      'FOLIO-s456',  204, 56.37, -0.49, False),\n    ('Qwen2.5-14B',     'StrategyQA',   60, 53.33,  3.33, False),\n    ('Mistral-7B',      'LogiQA',      200, 51.00,  0.50, False),\n    ('Mistral-7B',      'FOLIO-ICL',   199, 57.79, -3.52, False),\n    ('LLaMA-8B',        'FOLIO',       204, 63.24, -2.45, False),\n    ('DeepSeek-R1-7B',  'D012',         60, 71.67, -3.33, False),\n    ('LLaMA-8B',        'StrategyQA',  200, 72.00,  2.00, False),\n    ('Qwen2.5-14B',     'FOLIO-ICL',   199, 74.37,  0.50, False),\n    ('Qwen2.5-14B',     'FOLIO+PW',    804, 76.24,  0.25, False),\n    ('Qwen2.5-7B',      'FOLIO',       203, 77.34, -0.49, False),\n    ('Qwen2.5-14B',     'LogiQA',      200, 78.50, -0.50, False),\n    ('Qwen3-14B',       'FOLIO',       204, 83.82,  0.49, False),\n    ('QwQ-32B',         'AIME',         22, 72.70,  0.00, False),\n    ('Qwen2.5-14B',     'GSM8K',        30, 96.67,  0.00, False),\n]\n\nfig, ax = plt.subplots(figsize=(5.5, 4.125))\n\n# --- shaded regime bands ---\nax.axvspan(50, 55, alpha=0.15, color='#4CAF50', zorder=0)\nax.axvspan(60, 100, alpha=0.08, color='#E53935', zorder=0)\n\n# --- reference line at delta=0 ---\nax.axhline(y=0, color='#888', ls='--', lw=0.8, zorder=1)\n\n# --- plot data points ---\nfor model, domain, n, sc, delta, sig in data:\n    color = COLORS[model]\n    marker = '*' if sig else 'o'\n    size = 180 if sig else 55\n    if n >= 100:\n        ax.scatter(sc, delta, marker=marker, s=size, c=color,\n                   edgecolors='#333', linewidths=0.5, zorder=3)\n    else:\n        ax.scatter(sc, delta, marker=marker, s=size, c='white',\n                   edgecolors=color, linewidths=1.5, zorder=3)\n\n# --- FOLIO seed labels ---\nax.text(55.4, 5.15, 's42', fontsize=7, color='#AA5A87')\nax.text(55.0, 3.65, 's123', fontsize=7, color='#AA5A87')\nax.text(57.3, -0.25, 's456', fontsize=7, color='#AA5A87')\n\n# --- key annotations (positioned to avoid clipping) ---\nax.annotate('Mistral FOLIO +4.90 pp**',\n            xy=(54.41, 4.90), xytext=(48, 6.2),\n            fontsize=8, fontweight='bold', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#555', lw=1.0),\n            zorder=4)\n\nax.annotate('Mistral PW −2.83 pp**',\n            xy=(39.33, -2.83), xytext=(47, -4.8),\n            fontsize=8, fontweight='bold', ha='center',\n            arrowprops=dict(arrowstyle='->', color='#555', lw=1.0),\n            zorder=4)\n\n# --- zone labels (compact, at very top of each band) ---\nax.text(52.5, 7.05, 'Goldilocks', fontsize=7.5, color='#2E7D32',\n        ha='center', va='top', fontstyle='italic', fontweight='bold')\nax.text(65, 7.05, 'Type A', fontsize=7.5, color='#C62828',\n        ha='center', va='top', fontstyle='italic', fontweight='bold')\n\n# --- degenerate label ---\nax.text(96.67, 0.7, 'degen.', fontsize=7, color='#999',\n        fontstyle='italic', ha='center')\n\n# --- axes ---\nax.set_xlabel('Self-Consistency Accuracy (%)')\nax.set_ylabel('SICA $\\\\Delta$ (pp)')\nax.set_xlim(33, 100)\nax.set_ylim(-5.8, 7.2)\n\n# --- legend ---\nmodel_order = ['Mistral-7B', 'LLaMA-8B', 'Qwen2.5-7B', 'Qwen2.5-14B',\n               'Qwen3-14B', 'DeepSeek-R1-7B', 'QwQ-32B']\nhandles = [Line2D([0], [0], marker='o', color='w', markerfacecolor=COLORS[m],\n                  markeredgecolor='#333', markersize=7, label=m, lw=0)\n           for m in model_order]\nhandles.append(Line2D([0], [0], lw=0, label=''))\nhandles.extend([\n    Line2D([0], [0], marker='*', color='w', markerfacecolor='#999',\n           markeredgecolor='#333', markersize=12, label='$p < 0.05$', lw=0),\n    Line2D([0], [0], marker='o', color='w', markerfacecolor='#999',\n           markeredgecolor='#333', markersize=7, label='n.s.', lw=0),\n    Line2D([0], [0], marker='o', color='w', markerfacecolor='white',\n           markeredgecolor='#999', markersize=7, markeredgewidth=1.5,\n           label='$n < 100$', lw=0),\n])\nax.legend(handles=handles, loc='upper right', framealpha=0.92, edgecolor='#ccc',\n          fontsize=8, handletextpad=0.5, labelspacing=0.35)\n\nplt.tight_layout()\n\nout = '/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper'\nfig.savefig(f'{out}/f2_regime_scatter.pdf')\nfig.savefig(f'{out}/f2_regime_scatter.png')\nplt.close()\nprint(f'Done. {len(data)} points plotted.')\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T03:22:31.464174+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/gen_f2_regime_scatter.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T03:22:31.464319+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 gen_f2_regime_scatter.py",
  "description": "Regenerate the scatter plot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 gen_f2_regime_scatter.py",
    "description": "Regenerate the scatter plot"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T03:22:31.464451+00:00_

Done. 17 points plotted.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T03:22:31.464569+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/f2_regime_scatter.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/f2_regime_scatter.png"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T03:22:31.465277+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T03:22:31.465518+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/f2_regime_scatter.{pdf,png}",
  "description": "Verify output files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/f2_regime_scatter.{pdf,png}",
    "description": "Verify output files exist"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T03:22:31.465655+00:00_

-rw-r--r-- 1 ubuntu ubuntu  40786 May 19 03:20 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/f2_regime_scatter.pdf
-rw-r--r-- 1 ubuntu ubuntu 168438 May 19 03:20 /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/f2_regime_scatter.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T03:22:31.465806+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T03:22:31.465962+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T03:22:31.466284+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "fig2_regime_scatter",
  "type": "chart",
  "description": "Hero figure: scatter plot showing SICA effectiveness depends on baseline SC accuracy regime. Goldilocks zone (50-55% SC) shows significant gains, Type A (≥60%) shows no benefit, Type C (≤40%) hurts. 17 data points across 7 model families.",
  "project": "symb_invariant_consensus",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/f2_regime_scatter.pdf",
  "tags": "['paper', 'figure2', 'hero-figure', 'regime-scatter']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "fig2_regime_scatter",
    "type": "chart",
    "description": "Hero figure: scatter plot showing SICA effectiveness depends on baseline SC accuracy regime. Goldilocks zone (50-55% SC) shows significant gains, Type A (≥60%) shows no benefit, Type C (≤40%) hurts. 17 data points across 7 model families.",
    "project": "symb_invariant_consensus",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/figures/paper/f2_regime_scatter.pdf",
    "tags": "['paper', 'figure2', 'hero-figure', 'regime-scatter']"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T03:22:31.466474+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_fe35df\", \"name\": \"fig2_regime_scatter\", \"type\": \"chart\", \"description\": \"Hero figure: scatter plot showing SICA effectiveness depends on baseline SC accuracy regime. Goldilocks zone (50-55% SC) shows significant gains, Type A (≥60%) shows no benefit, Type C (≤40%) hurts. 17 data points across 7 model families.\", \"path\": \"projects/symb_invariant_consensus/artifacts/_project/chart/f2_regime_scatter.pdf\", \"url\": null, \"project\": \"symb_invariant_consensus\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-19T03:22:20.229568+00:00\", \"tags\": [\"paper\", \"figure2\", \"hero-figure\", \"regime-scatter\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-19T03:22:31.466674+00:00_

Checklist verification:

- [x] All 17 data points plotted (1 Type C + 5 Goldilocks + 9 Type A + 2 Degenerate)
- [x] Green shaded band for Goldilocks zone (50-55% SC)
- [x] Red shaded band for Type A (SC ≥ 60%)
- [x] Key annotations readable: "Mistral FOLIO +4.90 pp**" and "Mistral PW −2.83 pp**"
- [x] Legend in upper right, no data overlap
- [x] Font ≥ 7pt everywhere (smallest: seed labels and "degen." at 7pt)
- [x] Horizontal Δ=0 dashed line visible
- [x] Solid markers for n≥100, hollow for n<100
- [x] Stars for p<0.05, circles for n.s.
- [x] Okabe-Ito colorblind-safe palette
- [x] Three FOLIO seeds labeled (s42, s123, s456) and visually grouped by shared color
- [x] 5.5" × 4.125" (4:3 aspect), 300 DPI

Output saved to:
- PDF: `artifacts/figures/paper/f2_regime_scatter.pdf` (41 KB)
- PNG: `artifacts/figures/paper/f2_regime_scatter.png` (168 KB)
- Script: `artifacts/figures/paper/gen_f2_regime_scatter.py`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_figure_fig2_regime_scatter_20260519T031001"
}
```

</details>

---
