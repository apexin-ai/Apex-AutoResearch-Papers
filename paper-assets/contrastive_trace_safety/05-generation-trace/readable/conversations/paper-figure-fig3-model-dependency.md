# paper figure fig3 model dependency

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/chats/worker_paper_figure_fig3_model_dependency_20260517T000455.jsonl`
- **Structured JSON:** [`5234069c2945e34abbe9.json`](../../sessions/52/5234069c2945e34abbe9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

39 recorded events

### Tool call

_source line 1 · 2026-05-17T00:07:06.229208+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/",
  "description": "Create output directory for figures"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/",
    "description": "Create output directory for figures"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T00:07:06.229555+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T00:07:06.229766+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"import matplotlib; print(matplotlib.__version__)\"",
  "description": "Check matplotlib availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"import matplotlib; print(matplotlib.__version__)\"",
    "description": "Check matplotlib availability"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T00:07:06.229916+00:00_

3.10.9

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T00:07:06.230059+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.py",
  "content": "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport numpy as np\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 11,\n    'axes.titlesize': 13,\n    'axes.labelsize': 12,\n    'xtick.labelsize': 10,\n    'ytick.labelsize': 10,\n    'legend.fontsize': 10,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n})\n\nCOLOR_HS = '#0072B2'\nCOLOR_TEXT = '#E69F00'\n\nmodels = ['r1-8b', 'QwQ-32B', 'R1-32B']\nhs_fpr = [14.8, 22.4, 26.0]\ntext_fpr = [22.2, 21.4, 24.6]\n\nhs_err = [4.0, 5.0, 5.0]\ntext_err = [5.0, 5.0, 5.0]\n\nx = np.arange(len(models))\nwidth = 0.32\n\nfig, ax = plt.subplots(figsize=(5.5, 4.1))\n\nbars_hs = ax.bar(x - width/2, hs_fpr, width, yerr=hs_err,\n                 color=COLOR_HS, edgecolor='white', linewidth=0.5,\n                 capsize=4, error_kw={'linewidth': 1.2}, label='Hidden States', zorder=3)\nbars_text = ax.bar(x + width/2, text_fpr, width, yerr=text_err,\n                   color=COLOR_TEXT, edgecolor='white', linewidth=0.5,\n                   capsize=4, error_kw={'linewidth': 1.2}, label='Text', zorder=3)\n\nax.set_xlabel('Model')\nax.set_ylabel('Pre-CP FPR (trace-level, %)')\nax.set_xticks(x)\nax.set_xticklabels(models)\nax.set_ylim(0, 35)\nax.set_yticks(np.arange(0, 36, 5))\nax.yaxis.grid(True, alpha=0.3, linestyle='--', zorder=0)\nax.legend(loc='upper left', framealpha=0.9)\n\n# Annotation: p=0.044 * for r1-8b\nbracket_y = max(hs_fpr[0] + hs_err[0], text_fpr[0] + text_err[0]) + 1.5\nax.annotate('$p$=0.044 *', xy=(0, bracket_y + 0.5),\n            ha='center', va='bottom', fontsize=9, fontstyle='italic')\n\n# Horizontal dashed line showing the gap for r1-8b\ngap_x_left = x[0] - width/2\ngap_x_right = x[0] + width/2\ngap_y_hs = hs_fpr[0]\ngap_y_text = text_fpr[0]\nmid_x = x[0] + width/2 + 0.15\nax.plot([mid_x, mid_x], [gap_y_hs, gap_y_text], 'k--', linewidth=0.8, zorder=4)\nax.plot([mid_x - 0.03, mid_x + 0.03], [gap_y_hs, gap_y_hs], 'k-', linewidth=0.8, zorder=4)\nax.plot([mid_x - 0.03, mid_x + 0.03], [gap_y_text, gap_y_text], 'k-', linewidth=0.8, zorder=4)\nax.annotate(r'$\\Delta$=7.4pp', xy=(mid_x + 0.05, (gap_y_hs + gap_y_text)/2),\n            ha='left', va='center', fontsize=8.5)\n\n# n.s. annotations for QwQ-32B and R1-32B\nfor i in [1, 2]:\n    top_y = max(hs_fpr[i] + hs_err[i], text_fpr[i] + text_err[i]) + 1.5\n    ax.annotate('n.s.', xy=(x[i], top_y),\n                ha='center', va='bottom', fontsize=9, color='0.4')\n\nplt.tight_layout()\n\nout_base = '/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency'\nfig.savefig(out_base + '.pdf')\nfig.savefig(out_base + '.png', dpi=300)\nplt.close()\nprint('Done.')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.py",
    "content": "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport numpy as np\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 11,\n    'axes.titlesize': 13,\n    'axes.labelsize': 12,\n    'xtick.labelsize': 10,\n    'ytick.labelsize': 10,\n    'legend.fontsize': 10,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n})\n\nCOLOR_HS = '#0072B2'\nCOLOR_TEXT = '#E69F00'\n\nmodels = ['r1-8b', 'QwQ-32B', 'R1-32B']\nhs_fpr = [14.8, 22.4, 26.0]\ntext_fpr = [22.2, 21.4, 24.6]\n\nhs_err = [4.0, 5.0, 5.0]\ntext_err = [5.0, 5.0, 5.0]\n\nx = np.arange(len(models))\nwidth = 0.32\n\nfig, ax = plt.subplots(figsize=(5.5, 4.1))\n\nbars_hs = ax.bar(x - width/2, hs_fpr, width, yerr=hs_err,\n                 color=COLOR_HS, edgecolor='white', linewidth=0.5,\n                 capsize=4, error_kw={'linewidth': 1.2}, label='Hidden States', zorder=3)\nbars_text = ax.bar(x + width/2, text_fpr, width, yerr=text_err,\n                   color=COLOR_TEXT, edgecolor='white', linewidth=0.5,\n                   capsize=4, error_kw={'linewidth': 1.2}, label='Text', zorder=3)\n\nax.set_xlabel('Model')\nax.set_ylabel('Pre-CP FPR (trace-level, %)')\nax.set_xticks(x)\nax.set_xticklabels(models)\nax.set_ylim(0, 35)\nax.set_yticks(np.arange(0, 36, 5))\nax.yaxis.grid(True, alpha=0.3, linestyle='--', zorder=0)\nax.legend(loc='upper left', framealpha=0.9)\n\n# Annotation: p=0.044 * for r1-8b\nbracket_y = max(hs_fpr[0] + hs_err[0], text_fpr[0] + text_err[0]) + 1.5\nax.annotate('$p$=0.044 *', xy=(0, bracket_y + 0.5),\n            ha='center', va='bottom', fontsize=9, fontstyle='italic')\n\n# Horizontal dashed line showing the gap for r1-8b\ngap_x_left = x[0] - width/2\ngap_x_right = x[0] + width/2\ngap_y_hs = hs_fpr[0]\ngap_y_text = text_fpr[0]\nmid_x = x[0] + width/2 + 0.15\nax.plot([mid_x, mid_x], [gap_y_hs, gap_y_text], 'k--', linewidth=0.8, zorder=4)\nax.plot([mid_x - 0.03, mid_x + 0.03], [gap_y_hs, gap_y_hs], 'k-', linewidth=0.8, zorder=4)\nax.plot([mid_x - 0.03, mid_x + 0.03], [gap_y_text, gap_y_text], 'k-', linewidth=0.8, zorder=4)\nax.annotate(r'$\\Delta$=7.4pp', xy=(mid_x + 0.05, (gap_y_hs + gap_y_text)/2),\n            ha='left', va='center', fontsize=8.5)\n\n# n.s. annotations for QwQ-32B and R1-32B\nfor i in [1, 2]:\n    top_y = max(hs_fpr[i] + hs_err[i], text_fpr[i] + text_err[i]) + 1.5\n    ax.annotate('n.s.', xy=(x[i], top_y),\n                ha='center', va='bottom', fontsize=9, color='0.4')\n\nplt.tight_layout()\n\nout_base = '/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency'\nfig.savefig(out_base + '.pdf')\nfig.savefig(out_base + '.png', dpi=300)\nplt.close()\nprint('Done.')\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T00:07:06.230232+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T00:07:06.230364+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper && python3 fig3_model_dependency.py",
  "description": "Generate the figure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper && python3 fig3_model_dependency.py",
    "description": "Generate the figure"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T00:07:06.230489+00:00_

Done.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T00:07:06.230627+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.{pdf,png}",
  "description": "Verify output files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.{pdf,png}",
    "description": "Verify output files"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T00:07:06.230763+00:00_

-rw-r--r-- 1 ubuntu ubuntu 20501 May 17 00:05 /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.pdf
-rw-r--r-- 1 ubuntu ubuntu 76366 May 17 00:05 /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T00:07:06.230886+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.png"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T00:07:06.231310+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T00:07:06.231502+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.py",
  "old_string": "ax.legend(loc='upper left', framealpha=0.9)\n\n# Annotation: p=0.044 * for r1-8b\nbracket_y = max(hs_fpr[0] + hs_err[0], text_fpr[0] + text_err[0]) + 1.5\nax.annotate('$p$=0.044 *', xy=(0, bracket_y + 0.5),\n            ha='center', va='bottom', fontsize=9, fontstyle='italic')\n\n# Horizontal dashed line showing the gap for r1-8b\ngap_x_left = x[0] - width/2\ngap_x_right = x[0] + width/2\ngap_y_hs = hs_fpr[0]\ngap_y_text = text_fpr[0]\nmid_x = x[0] + width/2 + 0.15",
  "new_string": "ax.legend(loc='upper left', framealpha=0.9, bbox_to_anchor=(0.0, 1.0))\n\n# Annotation: p=0.044 * for r1-8b\nbracket_y = max(hs_fpr[0] + hs_err[0], text_fpr[0] + text_err[0]) + 1.5\nax.annotate('$p$=0.044 *', xy=(0, bracket_y + 1.0),\n            ha='center', va='bottom', fontsize=9, fontstyle='italic',\n            color='#333333')\n\n# Bracket connecting the two bars\nbracket_base = bracket_y\nax.plot([x[0] - width/2, x[0] - width/2, x[0] + width/2, x[0] + width/2],\n        [bracket_base - 0.5, bracket_base, bracket_base, bracket_base - 0.5],\n        color='#333333', linewidth=0.8, zorder=4)\n\n# Dashed line showing the gap for r1-8b\ngap_y_hs = hs_fpr[0]\ngap_y_text = text_fpr[0]\nmid_x = x[0] + width/2 + 0.18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.py",
    "old_string": "ax.legend(loc='upper left', framealpha=0.9)\n\n# Annotation: p=0.044 * for r1-8b\nbracket_y = max(hs_fpr[0] + hs_err[0], text_fpr[0] + text_err[0]) + 1.5\nax.annotate('$p$=0.044 *', xy=(0, bracket_y + 0.5),\n            ha='center', va='bottom', fontsize=9, fontstyle='italic')\n\n# Horizontal dashed line showing the gap for r1-8b\ngap_x_left = x[0] - width/2\ngap_x_right = x[0] + width/2\ngap_y_hs = hs_fpr[0]\ngap_y_text = text_fpr[0]\nmid_x = x[0] + width/2 + 0.15",
    "new_string": "ax.legend(loc='upper left', framealpha=0.9, bbox_to_anchor=(0.0, 1.0))\n\n# Annotation: p=0.044 * for r1-8b\nbracket_y = max(hs_fpr[0] + hs_err[0], text_fpr[0] + text_err[0]) + 1.5\nax.annotate('$p$=0.044 *', xy=(0, bracket_y + 1.0),\n            ha='center', va='bottom', fontsize=9, fontstyle='italic',\n            color='#333333')\n\n# Bracket connecting the two bars\nbracket_base = bracket_y\nax.plot([x[0] - width/2, x[0] - width/2, x[0] + width/2, x[0] + width/2],\n        [bracket_base - 0.5, bracket_base, bracket_base, bracket_base - 0.5],\n        color='#333333', linewidth=0.8, zorder=4)\n\n# Dashed line showing the gap for r1-8b\ngap_y_hs = hs_fpr[0]\ngap_y_text = text_fpr[0]\nmid_x = x[0] + width/2 + 0.18"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T00:07:06.231702+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T00:07:06.231840+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 fig3_model_dependency.py",
  "description": "Regenerate the figure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 fig3_model_dependency.py",
    "description": "Regenerate the figure"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T00:07:06.231965+00:00_

Done.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T00:07:06.232086+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.png"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T00:07:06.232503+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T00:07:06.232785+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.py"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T00:07:06.233004+00:00_

1	import matplotlib
2	matplotlib.use('Agg')
3	import matplotlib.pyplot as plt
4	import numpy as np
5	
6	plt.rcParams.update({
7	    'font.family': 'DejaVu Sans',
8	    'font.size': 11,
9	    'axes.titlesize': 13,
10	    'axes.labelsize': 12,
11	    'xtick.labelsize': 10,
12	    'ytick.labelsize': 10,
13	    'legend.fontsize': 10,
14	    'figure.dpi': 300,
15	    'savefig.dpi': 300,
16	    'savefig.bbox': 'tight',
17	    'savefig.pad_inches': 0.05,
18	    'axes.spines.top': False,
19	    'axes.spines.right': False,
20	})
21	
22	COLOR_HS = '#0072B2'
23	COLOR_TEXT = '#E69F00'
24	
25	models = ['r1-8b', 'QwQ-32B', 'R1-32B']
26	hs_fpr = [14.8, 22.4, 26.0]
27	text_fpr = [22.2, 21.4, 24.6]
28	
29	hs_err = [4.0, 5.0, 5.0]
30	text_err = [5.0, 5.0, 5.0]
31	
32	x = np.arange(len(models))
33	width = 0.32
34	
35	fig, ax = plt.subplots(figsize=(5.5, 4.1))
36	
37	bars_hs = ax.bar(x - width/2, hs_fpr, width, yerr=hs_err,
38	                 color=COLOR_HS, edgecolor='white', linewidth=0.5,
39	                 capsize=4, error_kw={'linewidth': 1.2}, label='Hidden States', zorder=3)
40	bars_text = ax.bar(x + width/2, text_fpr, width, yerr=text_err,
41	                   color=COLOR_TEXT, edgecolor='white', linewidth=0.5,
42	                   capsize=4, error_kw={'linewidth': 1.2}, label='Text', zorder=3)
43	
44	ax.set_xlabel('Model')
45	ax.set_ylabel('Pre-CP FPR (trace-level, %)')
46	ax.set_xticks(x)
47	ax.set_xticklabels(models)
48	ax.set_ylim(0, 35)
49	ax.set_yticks(np.arange(0, 36, 5))
50	ax.yaxis.grid(True, alpha=0.3, linestyle='--', zorder=0)
51	ax.legend(loc='upper left', framealpha=0.9, bbox_to_anchor=(0.0, 1.0))
52	
53	# Annotation: p=0.044 * for r1-8b
54	bracket_y = max(hs_fpr[0] + hs_err[0], text_fpr[0] + text_err[0]) + 1.5
55	ax.annotate('$p$=0.044 *', xy=(0, bracket_y + 1.0),
56	            ha='center', va='bottom', fontsize=9, fontstyle='italic',
57	            color='#333333')
58	
59	# Bracket connecting the two bars
60	bracket_base = bracket_y
61	ax.plot([x[0] - width/
…[truncated 1272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T00:07:06.233173+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.py",
  "content": "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport numpy as np\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 11,\n    'axes.titlesize': 13,\n    'axes.labelsize': 12,\n    'xtick.labelsize': 10,\n    'ytick.labelsize': 10,\n    'legend.fontsize': 10,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n})\n\nCOLOR_HS = '#0072B2'\nCOLOR_TEXT = '#E69F00'\n\nmodels = ['r1-8b', 'QwQ-32B', 'R1-32B']\nhs_fpr = [14.8, 22.4, 26.0]\ntext_fpr = [22.2, 21.4, 24.6]\n\nhs_err = [4.0, 5.0, 5.0]\ntext_err = [5.0, 5.0, 5.0]\n\nx = np.arange(len(models))\nwidth = 0.32\n\nfig, ax = plt.subplots(figsize=(5.5, 4.1))\n\nbars_hs = ax.bar(x - width/2, hs_fpr, width, yerr=hs_err,\n                 color=COLOR_HS, edgecolor='white', linewidth=0.5,\n                 capsize=4, error_kw={'linewidth': 1.2}, label='Hidden States', zorder=3)\nbars_text = ax.bar(x + width/2, text_fpr, width, yerr=text_err,\n                   color=COLOR_TEXT, edgecolor='white', linewidth=0.5,\n                   capsize=4, error_kw={'linewidth': 1.2}, label='Text', zorder=3)\n\nax.set_xlabel('Model')\nax.set_ylabel('Pre-CP FPR (trace-level, %)')\nax.set_xticks(x)\nax.set_xticklabels(models)\nax.set_ylim(0, 38)\nax.set_yticks(np.arange(0, 36, 5))\nax.yaxis.grid(True, alpha=0.3, linestyle='--', zorder=0)\n\n# Legend in upper right to avoid overlap with r1-8b annotations\nax.legend(loc='upper right', framealpha=0.9)\n\n# Bracket + p-value for r1-8b\nbracket_y = max(hs_fpr[0] + hs_err[0], text_fpr[0] + text_err[0]) + 2.0\nax.plot([x[0] - width/2, x[0] - width/2, x[0] + width/2, x[0] + width/2],\n        [bracket_y - 0.6, bracket_y, bracket_y, bracket_y - 0.6],\n        color='#333333', linewidth=0.8, zorder=4)\nax.text(x[0], bracket_y + 0.8, '$p$=0.044 *', ha='center', va='bottom',\n        fontsize=9, fontstyle='italic', color='#333333')\n\n# Dashed line showing the 7.4pp gap for r1-8b\ngap_y_hs = hs_fpr[0]\ngap_y_text = text_fpr[0]\nmid_x = x[0] + width/2 + 0.18\nax.plot([mid_x, mid_x], [gap_y_hs, gap_y_text], 'k--', linewidth=0.8, zorder=4)\nax.plot([mid_x - 0.03, mid_x + 0.03], [gap_y_hs, gap_y_hs], 'k-', linewidth=0.8, zorder=4)\nax.plot([mid_x - 0.03, mid_x + 0.03], [gap_y_text, gap_y_text], 'k-', linewidth=0.8, zorder=4)\nax.text(mid_x + 0.06, (gap_y_hs + gap_y_text) / 2, r'$\\Delta$=7.4pp',\n        ha='left', va='center', fontsize=8.5)\n\n# n.s. annotations for QwQ-32B and R1-32B\nfor i in [1, 2]:\n    top_y = max(hs_fpr[i] + hs_err[i], text_fpr[i] + text_err[i]) + 1.5\n    ax.text(x[i], top_y + 0.5, 'n.s.', ha='center', va='bottom',\n            fontsize=9, color='0.4')\n\nplt.tight_layout()\n\nout_base = '/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency'\nfig.savefig(out_base + '.pdf')\nfig.savefig(out_base + '.png', dpi=300)\nplt.close()\nprint('Done.')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.py",
    "content": "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport numpy as np\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 11,\n    'axes.titlesize': 13,\n    'axes.labelsize': 12,\n    'xtick.labelsize': 10,\n    'ytick.labelsize': 10,\n    'legend.fontsize': 10,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n})\n\nCOLOR_HS = '#0072B2'\nCOLOR_TEXT = '#E69F00'\n\nmodels = ['r1-8b', 'QwQ-32B', 'R1-32B']\nhs_fpr = [14.8, 22.4, 26.0]\ntext_fpr = [22.2, 21.4, 24.6]\n\nhs_err = [4.0, 5.0, 5.0]\ntext_err = [5.0, 5.0, 5.0]\n\nx = np.arange(len(models))\nwidth = 0.32\n\nfig, ax = plt.subplots(figsize=(5.5, 4.1))\n\nbars_hs = ax.bar(x - width/2, hs_fpr, width, yerr=hs_err,\n                 color=COLOR_HS, edgecolor='white', linewidth=0.5,\n                 capsize=4, error_kw={'linewidth': 1.2}, label='Hidden States', zorder=3)\nbars_text = ax.bar(x + width/2, text_fpr, width, yerr=text_err,\n                   color=COLOR_TEXT, edgecolor='white', linewidth=0.5,\n                   capsize=4, error_kw={'linewidth': 1.2}, label='Text', zorder=3)\n\nax.set_xlabel('Model')\nax.set_ylabel('Pre-CP FPR (trace-level, %)')\nax.set_xticks(x)\nax.set_xticklabels(models)\nax.set_ylim(0, 38)\nax.set_yticks(np.arange(0, 36, 5))\nax.yaxis.grid(True, alpha=0.3, linestyle='--', zorder=0)\n\n# Legend in upper right to avoid overlap with r1-8b annotations\nax.legend(loc='upper right', framealpha=0.9)\n\n# Bracket + p-value for r1-8b\nbracket_y = max(hs_fpr[0] + hs_err[0], text_fpr[0] + text_err[0]) + 2.0\nax.plot([x[0] - width/2, x[0] - width/2, x[0] + width/2, x[0] + width/2],\n        [bracket_y - 0.6, bracket_y, bracket_y, bracket_y - 0.6],\n        color='#333333', linewidth=0.8, zorder=4)\nax.text(x[0], bracket_y + 0.8, '$p$=0.044 *', ha='center', va='bottom',\n        fontsize=9, fontstyle='italic', color='#333333')\n\n# Dashed line showing the 7.4pp gap for r1-8b\ngap_y_hs = hs_fpr[0]\ngap_y_text = text_fpr[0]\nmid_x = x[0] + width/2 + 0.18\nax.plot([mid_x, mid_x], [gap_y_hs, gap_y_text], 'k--', linewidth=0.8, zorder=4)\nax.plot([mid_x - 0.03, mid_x + 0.03], [gap_y_hs, gap_y_hs], 'k-', linewidth=0.8, zorder=4)\nax.plot([mid_x - 0.03, mid_x + 0.03], [gap_y_text, gap_y_text], 'k-', linewidth=0.8, zorder=4)\nax.text(mid_x + 0.06, (gap_y_hs + gap_y_text) / 2, r'$\\Delta$=7.4pp',\n        ha='left', va='center', fontsize=8.5)\n\n# n.s. annotations for QwQ-32B and R1-32B\nfor i in [1, 2]:\n    top_y = max(hs_fpr[i] + hs_err[i], text_fpr[i] + text_err[i]) + 1.5\n    ax.text(x[i], top_y + 0.5, 'n.s.', ha='center', va='bottom',\n            fontsize=9, color='0.4')\n\nplt.tight_layout()\n\nout_base = '/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency'\nfig.savefig(out_base + '.pdf')\nfig.savefig(out_base + '.png', dpi=300)\nplt.close()\nprint('Done.')\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T00:07:06.233363+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T00:07:06.233498+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 fig3_model_dependency.py",
  "description": "Regenerate figure with fixed layout"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 fig3_model_dependency.py",
    "description": "Regenerate figure with fixed layout"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T00:07:06.233644+00:00_

Done.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T00:07:06.233781+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.png"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T00:07:06.234203+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T00:07:06.234370+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.py",
  "old_string": "ax.set_ylim(0, 38)\nax.set_yticks(np.arange(0, 36, 5))\nax.yaxis.grid(True, alpha=0.3, linestyle='--', zorder=0)\n\n# Legend in upper right to avoid overlap with r1-8b annotations\nax.legend(loc='upper right', framealpha=0.9)",
  "new_string": "ax.set_ylim(0, 40)\nax.set_yticks(np.arange(0, 36, 5))\nax.yaxis.grid(True, alpha=0.3, linestyle='--', zorder=0)\n\nax.legend(ncol=2, loc='upper center', framealpha=0.9)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.py",
    "old_string": "ax.set_ylim(0, 38)\nax.set_yticks(np.arange(0, 36, 5))\nax.yaxis.grid(True, alpha=0.3, linestyle='--', zorder=0)\n\n# Legend in upper right to avoid overlap with r1-8b annotations\nax.legend(loc='upper right', framealpha=0.9)",
    "new_string": "ax.set_ylim(0, 40)\nax.set_yticks(np.arange(0, 36, 5))\nax.yaxis.grid(True, alpha=0.3, linestyle='--', zorder=0)\n\nax.legend(ncol=2, loc='upper center', framealpha=0.9)"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T00:07:06.234522+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T00:07:06.234670+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 fig3_model_dependency.py",
  "description": "Regenerate with horizontal legend"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 fig3_model_dependency.py",
    "description": "Regenerate with horizontal legend"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T00:07:06.234797+00:00_

Done.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-17T00:07:06.234918+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.png"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T00:07:06.235327+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-17T00:07:06.235476+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.{pdf,png}",
  "description": "Verify output file sizes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.{pdf,png}",
    "description": "Verify output file sizes"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T00:07:06.235624+00:00_

-rw-r--r-- 1 ubuntu ubuntu 20503 May 17 00:06 /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.pdf
-rw-r--r-- 1 ubuntu ubuntu 77591 May 17 00:06 /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T00:07:06.235770+00:00_

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
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
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

_source line 36 · 2026-05-17T00:07:06.235892+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T00:07:06.236011+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "fig3_model_dependency",
  "type": "chart",
  "description": "Grouped bar chart showing HS vs Text trace-level FPR by model. Supports Claim 2: modality gap is model-dependent (r1-8b p=0.044, QwQ-32B and R1-32B n.s.).",
  "project": "contrastive_trace_safety",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.pdf",
  "tags": "['paper', 'fig3', 'model-dependency', 'FPR', 'claim2']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "fig3_model_dependency",
    "type": "chart",
    "description": "Grouped bar chart showing HS vs Text trace-level FPR by model. Supports Claim 2: modality gap is model-dependent (r1-8b p=0.044, QwQ-32B and R1-32B n.s.).",
    "project": "contrastive_trace_safety",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/figures/paper/fig3_model_dependency.pdf",
    "tags": "['paper', 'fig3', 'model-dependency', 'FPR', 'claim2']"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-17T00:07:06.236163+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260517_832c4f\", \"name\": \"fig3_model_dependency\", \"type\": \"chart\", \"description\": \"Grouped bar chart showing HS vs Text trace-level FPR by model. Supports Claim 2: modality gap is model-dependent (r1-8b p=0.044, QwQ-32B and R1-32B n.s.).\", \"path\": \"projects/contrastive_trace_safety/artifacts/_project/chart/fig3_model_dependency_832c4f.pdf\", \"url\": null, \"project\": \"contrastive_trace_safety\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-17T00:06:59.720891+00:00\", \"tags\": [\"paper\", \"fig3\", \"model-dependency\", \"FPR\", \"claim2\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 39 · 2026-05-17T00:07:06.236336+00:00_

图表已生成并注册。

输出文件：
- PDF: `artifacts/figures/paper/fig3_model_dependency.pdf` (20KB)
- PNG: `artifacts/figures/paper/fig3_model_dependency.png` (78KB, 300 DPI)

视觉要点：r1-8b 组 HS bar (14.8%) 明显低于 Text bar (22.2%)，带 bracket 标注 *p*=0.044 * 和 Δ=7.4pp；QwQ-32B 和 R1-32B 两组 bar 近乎等高，标注 n.s.。Legend 水平居上，所有标注无遮挡。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_figure_fig3_model_dependency_20260517T000455"
}
```

</details>

---
