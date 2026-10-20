# figure fig3 evidence hierarchy

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_figure_fig3-evidence-hierarchy_20260523T123646.jsonl`
- **Structured JSON:** [`6c3ce7d10d6d2e070f35.json`](../../sessions/6c/6c3ce7d10d6d2e070f35.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-23T12:37:48.063926+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
  "description": "Check if output directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_fig3-evidence-hierarchy_20260523T123646",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/ 2>/dev/null || echo \"DIR_NOT_FOUND\"",
    "description": "Check if output directory exists"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T12:37:48.064313+00:00_

DIR_NOT_FOUND

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_fig3-evidence-hierarchy_20260523T123646",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T12:37:48.064494+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_fig3-evidence-hierarchy_20260523T123646",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper",
    "description": "Create output directory"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T12:37:48.064664+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_fig3-evidence-hierarchy_20260523T123646",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T12:37:48.064804+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/fig3_evidence_hierarchy.py",
  "content": "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport numpy as np\n\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['Times New Roman', 'DejaVu Serif'],\n    'font.size': 7,\n    'axes.linewidth': 0.5,\n    'xtick.major.width': 0.5,\n    'ytick.major.width': 0.5,\n    'xtick.major.size': 2,\n    'ytick.major.size': 2,\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n})\n\nvariants = ['9-Class', 'Binary', 'Scrambled', 'JB-MLM', 'Wiki-MLM', 'Topic', 'Vanilla']\n\ndd_mean = [0.997, 1.000, 0.997, 0.914, 0.904, 0.541, 0.312]\ndd_std  = [0.005, 0.000, 0.005, 0.115, 0.115, 0.207, 0.026]\n\naa_mean = [0.972, 0.990, 0.951, 0.893, 0.686, 0.625, 0.258]\naa_std  = [0.026, 0.008, 0.043, 0.080, 0.297, 0.141, 0.000]\n\ntc_mean = [0.596, 0.705, 0.616, 0.837, 0.791, 0.496, 0.413]\ntc_std  = [0.087, 0.072, 0.056, 0.013, 0.093, 0.042, 0.021]\n\nn = len(variants)\nx = np.arange(n)\nbar_w = 0.22\n\nfig, ax = plt.subplots(figsize=(3.25, 2.0))\n\nax.bar(x - bar_w, dd_mean, bar_w, yerr=dd_std,\n       color='#2166ac', edgecolor='white', linewidth=0.3,\n       error_kw=dict(lw=0.8, capsize=2, capthick=0.6),\n       label='DD OOD', zorder=3)\n\nax.bar(x, aa_mean, bar_w, yerr=aa_std,\n       color='#67a9cf', edgecolor='white', linewidth=0.3,\n       error_kw=dict(lw=0.8, capsize=2, capthick=0.6),\n       label='AA OOD', zorder=3)\n\nax.bar(x + bar_w, tc_mean, bar_w, yerr=tc_std,\n       color='#ef8a62', edgecolor='white', linewidth=0.3,\n       error_kw=dict(lw=0.8, capsize=2, capthick=0.6),\n       label='ToxicChat', zorder=3)\n\nax.set_ylabel('F1 Score', fontsize=7)\nax.set_ylim(0.0, 1.05)\nax.set_xticks(x)\nax.set_xticklabels(variants, rotation=45, ha='right', fontsize=7)\nax.tick_params(axis='y', labelsize=7)\n\nax.yaxis.set_major_locator(plt.MultipleLocator(0.2))\nax.grid(axis='y', linestyle='--', linewidth=0.4, color='#cccccc', zorder=0)\nax.set_axisbelow(True)\n\nax.legend(fontsize=6, loc='upper right', frameon=True, fancybox=False,\n          edgecolor='#cccccc', framealpha=0.9, handlelength=1.0,\n          handletextpad=0.4, borderpad=0.3, labelspacing=0.3)\n\nax.spines['top'].set_visible(False)\nax.spines['right'].set_visible(False)\n\nout_base = '/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/fig3_evidence_hierarchy'\nfig.savefig(out_base + '.pdf', bbox_inches='tight', pad_inches=0.02)\nfig.savefig(out_base + '.png', bbox_inches='tight', pad_inches=0.02, dpi=300)\nplt.close()\nprint('OK')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_fig3-evidence-hierarchy_20260523T123646",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/fig3_evidence_hierarchy.py",
    "content": "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport numpy as np\n\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['Times New Roman', 'DejaVu Serif'],\n    'font.size': 7,\n    'axes.linewidth': 0.5,\n    'xtick.major.width': 0.5,\n    'ytick.major.width': 0.5,\n    'xtick.major.size': 2,\n    'ytick.major.size': 2,\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n})\n\nvariants = ['9-Class', 'Binary', 'Scrambled', 'JB-MLM', 'Wiki-MLM', 'Topic', 'Vanilla']\n\ndd_mean = [0.997, 1.000, 0.997, 0.914, 0.904, 0.541, 0.312]\ndd_std  = [0.005, 0.000, 0.005, 0.115, 0.115, 0.207, 0.026]\n\naa_mean = [0.972, 0.990, 0.951, 0.893, 0.686, 0.625, 0.258]\naa_std  = [0.026, 0.008, 0.043, 0.080, 0.297, 0.141, 0.000]\n\ntc_mean = [0.596, 0.705, 0.616, 0.837, 0.791, 0.496, 0.413]\ntc_std  = [0.087, 0.072, 0.056, 0.013, 0.093, 0.042, 0.021]\n\nn = len(variants)\nx = np.arange(n)\nbar_w = 0.22\n\nfig, ax = plt.subplots(figsize=(3.25, 2.0))\n\nax.bar(x - bar_w, dd_mean, bar_w, yerr=dd_std,\n       color='#2166ac', edgecolor='white', linewidth=0.3,\n       error_kw=dict(lw=0.8, capsize=2, capthick=0.6),\n       label='DD OOD', zorder=3)\n\nax.bar(x, aa_mean, bar_w, yerr=aa_std,\n       color='#67a9cf', edgecolor='white', linewidth=0.3,\n       error_kw=dict(lw=0.8, capsize=2, capthick=0.6),\n       label='AA OOD', zorder=3)\n\nax.bar(x + bar_w, tc_mean, bar_w, yerr=tc_std,\n       color='#ef8a62', edgecolor='white', linewidth=0.3,\n       error_kw=dict(lw=0.8, capsize=2, capthick=0.6),\n       label='ToxicChat', zorder=3)\n\nax.set_ylabel('F1 Score', fontsize=7)\nax.set_ylim(0.0, 1.05)\nax.set_xticks(x)\nax.set_xticklabels(variants, rotation=45, ha='right', fontsize=7)\nax.tick_params(axis='y', labelsize=7)\n\nax.yaxis.set_major_locator(plt.MultipleLocator(0.2))\nax.grid(axis='y', linestyle='--', linewidth=0.4, color='#cccccc', zorder=0)\nax.set_axisbelow(True)\n\nax.legend(fontsize=6, loc='upper right', frameon=True, fancybox=False,\n          edgecolor='#cccccc', framealpha=0.9, handlelength=1.0,\n          handletextpad=0.4, borderpad=0.3, labelspacing=0.3)\n\nax.spines['top'].set_visible(False)\nax.spines['right'].set_visible(False)\n\nout_base = '/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/fig3_evidence_hierarchy'\nfig.savefig(out_base + '.pdf', bbox_inches='tight', pad_inches=0.02)\nfig.savefig(out_base + '.png', bbox_inches='tight', pad_inches=0.02, dpi=300)\nplt.close()\nprint('OK')\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T12:37:48.064960+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/fig3_evidence_hierarchy.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_fig3-evidence-hierarchy_20260523T123646",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T12:37:48.065090+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper && python3 fig3_evidence_hierarchy.py",
  "description": "Run the figure generation script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_fig3-evidence-hierarchy_20260523T123646",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper && python3 fig3_evidence_hierarchy.py",
    "description": "Run the figure generation script"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T12:37:48.065212+00:00_

OK

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_fig3-evidence-hierarchy_20260523T123646",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T12:37:48.065327+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/fig3_evidence_hierarchy.{pdf,png}",
  "description": "Verify output files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_fig3-evidence-hierarchy_20260523T123646",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/fig3_evidence_hierarchy.{pdf,png}",
    "description": "Verify output files"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T12:37:48.065444+00:00_

-rw-r--r-- 1 ubuntu ubuntu 16K May 23 12:37 /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/fig3_evidence_hierarchy.pdf
-rw-r--r-- 1 ubuntu ubuntu 58K May 23 12:37 /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/fig3_evidence_hierarchy.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_fig3-evidence-hierarchy_20260523T123646",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T12:37:48.065581+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/fig3_evidence_hierarchy.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_fig3-evidence-hierarchy_20260523T123646",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/fig3_evidence_hierarchy.png"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T12:37:48.065941+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_fig3-evidence-hierarchy_20260523T123646",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T12:37:48.066090+00:00_

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
  "session": "worker_figure_fig3-evidence-hierarchy_20260523T123646",
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

_source line 14 · 2026-05-23T12:37:48.066214+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_fig3-evidence-hierarchy_20260523T123646",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T12:37:48.066337+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "fig3_evidence_hierarchy",
  "type": "chart",
  "description": "Fig 3: Evidence hierarchy grouped bar chart — 7 Stage-1 DAPT variants × 3 evaluation conditions (DD OOD, AA OOD, ToxicChat), showing reversal where JB-MLM leads on ToxicChat despite classification variants dominating synthetic OOD.",
  "project": "persuasion_turn_jailbreak_detect",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/fig3_evidence_hierarchy.pdf",
  "tags": "['paper', 'fig3', 'evidence-hierarchy', 'toxicchat']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_fig3-evidence-hierarchy_20260523T123646",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "fig3_evidence_hierarchy",
    "type": "chart",
    "description": "Fig 3: Evidence hierarchy grouped bar chart — 7 Stage-1 DAPT variants × 3 evaluation conditions (DD OOD, AA OOD, ToxicChat), showing reversal where JB-MLM leads on ToxicChat despite classification variants dominating synthetic OOD.",
    "project": "persuasion_turn_jailbreak_detect",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/figures/paper/fig3_evidence_hierarchy.pdf",
    "tags": "['paper', 'fig3', 'evidence-hierarchy', 'toxicchat']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T12:37:48.066494+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260523_817f9b\", \"name\": \"fig3_evidence_hierarchy\", \"type\": \"chart\", \"description\": \"Fig 3: Evidence hierarchy grouped bar chart — 7 Stage-1 DAPT variants × 3 evaluation conditions (DD OOD, AA OOD, ToxicChat), showing reversal where JB-MLM leads on ToxicChat despite classification variants dominating synthetic OOD.\", \"path\": \"projects/persuasion_turn_jailbreak_detect/artifacts/_project/chart/fig3_evidence_hierarchy.pdf\", \"url\": null, \"project\": \"persuasion_turn_jailbreak_detect\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-23T12:37:41.471094+00:00\", \"tags\": [\"paper\", \"fig3\", \"evidence-hierarchy\", \"toxicchat\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_fig3-evidence-hierarchy_20260523T123646",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-23T12:37:48.066694+00:00_

PDF + PNG 已生成并注册：

- **PDF**: `docs/paper/figures/paper/fig3_evidence_hierarchy.pdf` (16K)
- **PNG**: `docs/paper/figures/paper/fig3_evidence_hierarchy.png` (58K, 300dpi)

视觉效果符合预期：左侧 3 个 classification 变体在 DD/AA 上接近 1.0 但 ToxicChat 橙色柱明显低（~0.6-0.7）；JB-MLM 的 ToxicChat 柱反超至 0.837，反转清晰可见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_figure_fig3-evidence-hierarchy_20260523T123646"
}
```

</details>

---
