# paper figure fig3 jaccard heatmap

**Transformer Model EAP-IG** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_figure_fig3_jaccard_heatmap_20260513T160621.jsonl`
- **Structured JSON:** [`9d6838aa2f9998db4430.json`](../../sessions/9d/9d6838aa2f9998db4430.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-13T16:07:23.919345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_jaccard_heatmap_20260513T160621",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T16:07:23.920486+00:00_

1	---
2	description: 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG
3	name: draw-paper-figure
4	scope: global
5	tags:
6	  - research
7	  - visualization
8	  - paper
9	  - matplotlib
10	version: 1
11	tools:
12	  - ssh_execute
13	---
14	
15	# Draw Paper Figure — 学术图表生成
16	
17	为 ML 论文生成发表级图表。通过 SSH 在 A6000 上运行 matplotlib 脚本，直接输出到实验目录。
18	
19	## 触发条件
20	
21	- 用户说"画个图"、"生成 reliability diagram"、"做个 heatmap"
22	- 论文写作阶段需要插图
23	- 实验结果需要可视化汇总
24	
25	## 通用样式标准（所有图表必须遵守）
26	
27	```python
28	import matplotlib
29	matplotlib.use('Agg')
30	import matplotlib.pyplot as plt
31	import matplotlib.patches as mpatches
32	import numpy as np
33	
34	# 字体和全局样式
35	plt.rcParams.update({
36	    'font.family': 'DejaVu Sans',
37	    'font.size': 11,
38	    'axes.titlesize': 13,
39	    'axes.labelsize': 12,
40	    'xtick.labelsize': 10,
41	    'ytick.labelsize': 10,
42	    'legend.fontsize': 10,
43	    'figure.dpi': 300,
44	    'savefig.dpi': 300,
45	    'savefig.bbox': 'tight',
46	    'savefig.pad_inches': 0.05,
47	    'axes.spines.top': False,
48	    'axes.spines.right': False,
49	    'lines.linewidth': 1.8,
50	})
51	
52	# 色盲友好配色（Okabe-Ito）
53	COLORS = {
54	    'fp16':   '#E69F00',  # 橙黄
55	    'nf4':    '#56B4E9',  # 天蓝
56	    'int8':   '#009E73',  # 绿
57	    'gptq':   '#F0E442',  # 黄
58	    'awq':    '#CC79A7',  # 粉紫
59	    'llama':  '#0072B2',  # 深蓝
60	    'qwen3':  '#D55E00',  # 橙红
61	    'gemma':  '#009E73',  # 绿
62	    'mistral':'#CC79A7',  # 粉紫
63	    'phi3':   '#F0E442',  # 黄
64	}
65	
66	# 方法标签
67	METHOD_LABELS = {
68	    'fp16': 'FP16', 'nf4': 'BNB-NF4',
69	    'int8': 'BNB-INT8', 'gptq': 'GPTQ-4bit', 'awq': 'AWQ-4bit'
70	}
71	```
72	
73	---
74	
75	## 1. Reliability Diagram（校准图）
76	
77	**用途**：显示模型 confidence bin vs accuracy，对角线 = 完美校准。
78	
79	```python
80	def plot_reliability_diagram(confidences, accuracies, n_bins=10,
81	                              label='', color='#0072B2',
82	                              title='Reliability
…[truncated 8160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_jaccard_heatmap_20260513T160621",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T16:07:23.920718+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper/ 2>/dev/null || echo \"DIR_NOT_EXISTS\"",
  "description": "Check if output directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_jaccard_heatmap_20260513T160621",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper/ 2>/dev/null || echo \"DIR_NOT_EXISTS\"",
    "description": "Check if output directory exists"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-13T16:07:23.920891+00:00_

fig1_overview.pdf
fig1_overview.png
fig2_size_controlled.pdf
fig2_size_controlled.png
gen_fig1_overview.py
gen_fig2.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_jaccard_heatmap_20260513T160621",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T16:07:23.921037+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper/gen_fig3_jaccard_heatmap.py",
  "content": "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.colors as mcolors\nimport numpy as np\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 11,\n    'axes.titlesize': 13,\n    'axes.labelsize': 12,\n    'xtick.labelsize': 10,\n    'ytick.labelsize': 10,\n    'legend.fontsize': 10,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n})\n\nmethods = ['EAP-IG', 'EP', 'ACDC']\n\npanels = {\n    '(a) IOI': np.array([\n        [1.00, 0.31, 0.10],\n        [0.31, 1.00, 0.09],\n        [0.10, 0.09, 1.00],\n    ]),\n    '(b) Arithmetic': np.array([\n        [1.00, 0.695, 0.17],\n        [0.695, 1.00, 0.17],\n        [0.17, 0.17, 1.00],\n    ]),\n    '(c) SVA': np.array([\n        [1.00, 0.65, 0.32],\n        [0.65, 1.00, 0.42],\n        [0.32, 0.42, 1.00],\n    ]),\n    '(d) Factual Recall': np.array([\n        [1.00, 0.82, 0.15],\n        [0.82, 1.00, 0.15],\n        [0.15, 0.15, 1.00],\n    ]),\n}\n\nfig, axes = plt.subplots(1, 4, figsize=(14, 3.5))\n\ncmap = plt.cm.YlOrRd\nnorm = mcolors.Normalize(vmin=0, vmax=1)\n\nfor ax, (title, matrix) in zip(axes, panels.items()):\n    masked = np.ma.array(matrix, mask=np.eye(3, dtype=bool))\n    im = ax.imshow(masked, cmap=cmap, norm=norm, aspect='equal')\n\n    for i in range(3):\n        for j in range(3):\n            if i == j:\n                ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1,\n                             fill=True, facecolor='#E8E8E8', edgecolor='white', linewidth=1.5))\n                ax.text(j, i, '1.00', ha='center', va='center',\n                        fontsize=11, color='#888888', fontweight='normal')\n            else:\n                val = matrix[i, j]\n                color = 'white' if val > 0.55 else 'black'\n                ax.text(j, i, f'{val:.2f}', ha='center', va='center',\n                        fontsize=11, color=color, fontweight='bold')\n\n    ax.set_xticks(range(3))\n    ax.set_yticks(range(3))\n    ax.set_xticklabels(methods, rotation=30, ha='right')\n    if ax == axes[0]:\n        ax.set_yticklabels(methods)\n    else:\n        ax.set_yticklabels([])\n    ax.set_title(title, fontsize=12, pad=8)\n\n    ax.set_xlim(-0.5, 2.5)\n    ax.set_ylim(2.5, -0.5)\n\n    for spine in ax.spines.values():\n        spine.set_visible(True)\n        spine.set_color('#CCCCCC')\n        spine.set_linewidth(0.8)\n    ax.tick_params(length=0)\n\ncbar_ax = fig.add_axes([0.93, 0.18, 0.012, 0.65])\ncbar = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), cax=cbar_ax)\ncbar.set_label('Jaccard Similarity', fontsize=11)\ncbar.ax.tick_params(labelsize=9)\n\nplt.subplots_adjust(left=0.06, right=0.91, wspace=0.15, bottom=0.15, top=0.88)\n\noutdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper'\nfig.savefig(f'{outdir}/fig3_jaccard_heatmap.pdf')\nfig.savefig(f'{outdir}/fig3_jaccard_heatmap.png')\nplt.close()\nprint('Saved fig3_jaccard_heatmap.pdf and .png')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_jaccard_heatmap_20260513T160621",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper/gen_fig3_jaccard_heatmap.py",
    "content": "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.colors as mcolors\nimport numpy as np\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 11,\n    'axes.titlesize': 13,\n    'axes.labelsize': 12,\n    'xtick.labelsize': 10,\n    'ytick.labelsize': 10,\n    'legend.fontsize': 10,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n})\n\nmethods = ['EAP-IG', 'EP', 'ACDC']\n\npanels = {\n    '(a) IOI': np.array([\n        [1.00, 0.31, 0.10],\n        [0.31, 1.00, 0.09],\n        [0.10, 0.09, 1.00],\n    ]),\n    '(b) Arithmetic': np.array([\n        [1.00, 0.695, 0.17],\n        [0.695, 1.00, 0.17],\n        [0.17, 0.17, 1.00],\n    ]),\n    '(c) SVA': np.array([\n        [1.00, 0.65, 0.32],\n        [0.65, 1.00, 0.42],\n        [0.32, 0.42, 1.00],\n    ]),\n    '(d) Factual Recall': np.array([\n        [1.00, 0.82, 0.15],\n        [0.82, 1.00, 0.15],\n        [0.15, 0.15, 1.00],\n    ]),\n}\n\nfig, axes = plt.subplots(1, 4, figsize=(14, 3.5))\n\ncmap = plt.cm.YlOrRd\nnorm = mcolors.Normalize(vmin=0, vmax=1)\n\nfor ax, (title, matrix) in zip(axes, panels.items()):\n    masked = np.ma.array(matrix, mask=np.eye(3, dtype=bool))\n    im = ax.imshow(masked, cmap=cmap, norm=norm, aspect='equal')\n\n    for i in range(3):\n        for j in range(3):\n            if i == j:\n                ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1,\n                             fill=True, facecolor='#E8E8E8', edgecolor='white', linewidth=1.5))\n                ax.text(j, i, '1.00', ha='center', va='center',\n                        fontsize=11, color='#888888', fontweight='normal')\n            else:\n                val = matrix[i, j]\n                color = 'white' if val > 0.55 else 'black'\n                ax.text(j, i, f'{val:.2f}', ha='center', va='center',\n                        fontsize=11, color=color, fontweight='bold')\n\n    ax.set_xticks(range(3))\n    ax.set_yticks(range(3))\n    ax.set_xticklabels(methods, rotation=30, ha='right')\n    if ax == axes[0]:\n        ax.set_yticklabels(methods)\n    else:\n        ax.set_yticklabels([])\n    ax.set_title(title, fontsize=12, pad=8)\n\n    ax.set_xlim(-0.5, 2.5)\n    ax.set_ylim(2.5, -0.5)\n\n    for spine in ax.spines.values():\n        spine.set_visible(True)\n        spine.set_color('#CCCCCC')\n        spine.set_linewidth(0.8)\n    ax.tick_params(length=0)\n\ncbar_ax = fig.add_axes([0.93, 0.18, 0.012, 0.65])\ncbar = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), cax=cbar_ax)\ncbar.set_label('Jaccard Similarity', fontsize=11)\ncbar.ax.tick_params(labelsize=9)\n\nplt.subplots_adjust(left=0.06, right=0.91, wspace=0.15, bottom=0.15, top=0.88)\n\noutdir = '/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper'\nfig.savefig(f'{outdir}/fig3_jaccard_heatmap.pdf')\nfig.savefig(f'{outdir}/fig3_jaccard_heatmap.png')\nplt.close()\nprint('Saved fig3_jaccard_heatmap.pdf and .png')\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T16:07:23.921196+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper/gen_fig3_jaccard_heatmap.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_jaccard_heatmap_20260513T160621",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T16:07:23.921345+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "source /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/.venv/bin/activate && python /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper/gen_fig3_jaccard_heatmap.py",
  "description": "Generate fig3 Jaccard heatmap"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_jaccard_heatmap_20260513T160621",
  "tool": "Bash",
  "tool_args": {
    "command": "source /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/.venv/bin/activate && python /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper/gen_fig3_jaccard_heatmap.py",
    "description": "Generate fig3 Jaccard heatmap"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T16:07:23.921462+00:00_

Saved fig3_jaccard_heatmap.pdf and .png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_jaccard_heatmap_20260513T160621",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T16:07:23.921572+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper/fig3_jaccard_heatmap.*",
  "description": "Verify output files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_jaccard_heatmap_20260513T160621",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper/fig3_jaccard_heatmap.*",
    "description": "Verify output files"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T16:07:23.921746+00:00_

-rw-r--r-- 1 ubuntu ubuntu  36630 May 13 16:06 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper/fig3_jaccard_heatmap.pdf
-rw-r--r-- 1 ubuntu ubuntu 162917 May 13 16:07 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper/fig3_jaccard_heatmap.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_jaccard_heatmap_20260513T160621",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T16:07:23.921943+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper/fig3_jaccard_heatmap.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_jaccard_heatmap_20260513T160621",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper/fig3_jaccard_heatmap.png"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T16:07:23.922383+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_jaccard_heatmap_20260513T160621",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T16:07:23.922517+00:00_

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
  "session": "worker_paper_figure_fig3_jaccard_heatmap_20260513T160621",
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

_source line 14 · 2026-05-13T16:07:23.922631+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_jaccard_heatmap_20260513T160621",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T16:07:23.922793+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "fig3_jaccard_heatmap",
  "type": "chart",
  "description": "4-panel pairwise Jaccard similarity heatmap (IOI, Arithmetic, SVA, Factual Recall) for EMNLP 2026 paper. Shows gradient-pair dominance (EAP-IG×EP) and ACDC isolation across tasks.",
  "project": "min_necessary_circuit_css",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper/fig3_jaccard_heatmap.pdf",
  "tags": "['paper', 'figure', 'jaccard', 'heatmap', 'failure_analysis']",
  "skill": "draw-paper-figure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_jaccard_heatmap_20260513T160621",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "fig3_jaccard_heatmap",
    "type": "chart",
    "description": "4-panel pairwise Jaccard similarity heatmap (IOI, Arithmetic, SVA, Factual Recall) for EMNLP 2026 paper. Shows gradient-pair dominance (EAP-IG×EP) and ACDC isolation across tasks.",
    "project": "min_necessary_circuit_css",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/figures/paper/fig3_jaccard_heatmap.pdf",
    "tags": "['paper', 'figure', 'jaccard', 'heatmap', 'failure_analysis']",
    "skill": "draw-paper-figure"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T16:07:23.922948+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260513_7851cd\", \"name\": \"fig3_jaccard_heatmap\", \"type\": \"chart\", \"description\": \"4-panel pairwise Jaccard similarity heatmap (IOI, Arithmetic, SVA, Factual Recall) for EMNLP 2026 paper. Shows gradient-pair dominance (EAP-IG×EP) and ACDC isolation across tasks.\", \"path\": \"projects/min_necessary_circuit_css/artifacts/_project/chart/fig3_jaccard_heatmap.pdf\", \"url\": null, \"project\": \"min_necessary_circuit_css\", \"exp_id\": null, \"skill\": \"draw-paper-figure\", \"created_at\": \"2026-05-13T16:07:16.765540+00:00\", \"tags\": [\"paper\", \"figure\", \"jaccard\", \"heatmap\", \"failure_analysis\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_jaccard_heatmap_20260513T160621",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-13T16:07:23.923106+00:00_

已生成并注册。

- PDF: `figures/paper/fig3_jaccard_heatmap.pdf` (36 KB)
- PNG: `figures/paper/fig3_jaccard_heatmap.png` (163 KB)
- Artifact ID: `art_20260513_7851cd`

视觉确认：4 panel 横排，EAP-IG×EP 格子在 Factual Recall (0.82) 和 Arithmetic (0.69) 上呈深红色，ACDC 行/列在 IOI/Arith/FR 上极低（0.09–0.17），SVA 上相对均匀（0.32–0.42）。对角线灰底区分，共享 colorbar 在右侧。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_figure_fig3_jaccard_heatmap_20260513T160621"
}
```

</details>

---
