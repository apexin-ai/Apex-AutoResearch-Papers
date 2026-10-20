# paper cka heatmap

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_paper_cka-heatmap_20260518T190351.jsonl`
- **Structured JSON:** [`eebaf199a663add74f29.json`](../../sessions/ee/eebaf199a663add74f29.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-18T19:04:26.086287+00:00_

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
  "session": "worker_paper_cka-heatmap_20260518T190351",
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

_source line 2 · 2026-05-18T19:04:26.086639+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_cka-heatmap_20260518T190351",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T19:04:26.086833+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-33183",
  "account": "root",
  "command": "mkdir -p /root/persuasion_turn_jailbreak_detect/paper/figures/\n\ncat > /tmp/cka_heatmap.py << 'PYEOF'\nimport numpy as np\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.colors as mcolors\n\nlabels = ['Vanilla', 'MLM', '9-Class']\n\ndeberta_iid = np.array([\n    [1.0,   0.442, 0.393],\n    [0.442, 1.0,   0.586],\n    [0.393, 0.586, 1.0  ],\n])\ndeberta_ood = np.array([\n    [1.0,   0.797, 0.649],\n    [0.797, 1.0,   0.773],\n    [0.649, 0.773, 1.0  ],\n])\nroberta_iid = np.array([\n    [1.0,   0.393, 0.592],\n    [0.393, 1.0,   0.351],\n    [0.592, 0.351, 1.0  ],\n])\nroberta_ood = np.array([\n    [1.0,   0.255, 0.735],\n    [0.255, 1.0,   0.183],\n    [0.735, 0.183, 1.0  ],\n])\n\nmatrices = [deberta_iid, deberta_ood, roberta_iid, roberta_ood]\ntitles = ['DeBERTa (IID)', 'DeBERTa (DD OOD)', 'RoBERTa (IID)', 'RoBERTa (DD OOD)']\n\nfig, axes = plt.subplots(2, 2, figsize=(3.4, 3.2), constrained_layout=True)\ncmap = plt.cm.YlOrRd\nnorm = mcolors.Normalize(vmin=0, vmax=1)\n\nfor ax, mat, title in zip(axes.flat, matrices, titles):\n    im = ax.imshow(mat, cmap=cmap, norm=norm, aspect='equal')\n    ax.set_xticks(range(3))\n    ax.set_yticks(range(3))\n    ax.set_xticklabels(labels, fontsize=7, rotation=45, ha='right')\n    ax.set_yticklabels(labels, fontsize=7)\n    ax.set_title(title, fontsize=8, pad=3)\n    for i in range(3):\n        for j in range(3):\n            val = mat[i, j]\n            color = 'white' if val > 0.65 else 'black'\n            ax.text(j, i, f'{val:.3f}', ha='center', va='center', fontsize=7, color=color)\n    ax.tick_params(length=0)\n\ncbar = fig.colorbar(im, ax=axes, shrink=0.85, aspect=30, pad=0.02)\ncbar.ax.tick_params(labelsize=7)\ncbar.set_label('Centered CKA', fontsize=8)\n\nfig.savefig('/root/persuasion_turn_jailbreak_detect/paper/figures/cka_heatmap.pdf', dpi=300, bbox_inches='tight')\nfig.savefig('/root/persuasion_turn_jailbreak_detect/paper/figures/cka_heatmap.png', dpi=300, bbox_inches='tight')\nprint('Done')\nPYEOF\n\nsource /root/miniconda3/bin/activate && python /tmp/cka_heatmap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_cka-heatmap_20260518T190351",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-33183",
    "account": "root",
    "command": "mkdir -p /root/persuasion_turn_jailbreak_detect/paper/figures/\n\ncat > /tmp/cka_heatmap.py << 'PYEOF'\nimport numpy as np\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.colors as mcolors\n\nlabels = ['Vanilla', 'MLM', '9-Class']\n\ndeberta_iid = np.array([\n    [1.0,   0.442, 0.393],\n    [0.442, 1.0,   0.586],\n    [0.393, 0.586, 1.0  ],\n])\ndeberta_ood = np.array([\n    [1.0,   0.797, 0.649],\n    [0.797, 1.0,   0.773],\n    [0.649, 0.773, 1.0  ],\n])\nroberta_iid = np.array([\n    [1.0,   0.393, 0.592],\n    [0.393, 1.0,   0.351],\n    [0.592, 0.351, 1.0  ],\n])\nroberta_ood = np.array([\n    [1.0,   0.255, 0.735],\n    [0.255, 1.0,   0.183],\n    [0.735, 0.183, 1.0  ],\n])\n\nmatrices = [deberta_iid, deberta_ood, roberta_iid, roberta_ood]\ntitles = ['DeBERTa (IID)', 'DeBERTa (DD OOD)', 'RoBERTa (IID)', 'RoBERTa (DD OOD)']\n\nfig, axes = plt.subplots(2, 2, figsize=(3.4, 3.2), constrained_layout=True)\ncmap = plt.cm.YlOrRd\nnorm = mcolors.Normalize(vmin=0, vmax=1)\n\nfor ax, mat, title in zip(axes.flat, matrices, titles):\n    im = ax.imshow(mat, cmap=cmap, norm=norm, aspect='equal')\n    ax.set_xticks(range(3))\n    ax.set_yticks(range(3))\n    ax.set_xticklabels(labels, fontsize=7, rotation=45, ha='right')\n    ax.set_yticklabels(labels, fontsize=7)\n    ax.set_title(title, fontsize=8, pad=3)\n    for i in range(3):\n        for j in range(3):\n            val = mat[i, j]\n            color = 'white' if val > 0.65 else 'black'\n            ax.text(j, i, f'{val:.3f}', ha='center', va='center', fontsize=7, color=color)\n    ax.tick_params(length=0)\n\ncbar = fig.colorbar(im, ax=axes, shrink=0.85, aspect=30, pad=0.02)\ncbar.ax.tick_params(labelsize=7)\ncbar.set_label('Centered CKA', fontsize=8)\n\nfig.savefig('/root/persuasion_turn_jailbreak_detect/paper/figures/cka_heatmap.pdf', dpi=300, bbox_inches='tight')\nfig.savefig('/root/persuasion_turn_jailbreak_detect/paper/figures/cka_heatmap.png', dpi=300, bbox_inches='tight')\nprint('Done')\nPYEOF\n\nsource /root/miniconda3/bin/activate && python /tmp/cka_heatmap.py"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T19:04:26.087028+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Done\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.97}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_cka-heatmap_20260518T190351",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T19:04:26.087164+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-33183",
  "account": "root",
  "command": "ls -la /root/persuasion_turn_jailbreak_detect/paper/figures/cka_heatmap.*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_cka-heatmap_20260518T190351",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-33183",
    "account": "root",
    "command": "ls -la /root/persuasion_turn_jailbreak_detect/paper/figures/cka_heatmap.*"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T19:04:26.087293+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root  18835 May 19 03:04 /root/persuasion_turn_jailbreak_detect/paper/figures/cka_heatmap.pdf\\n-rw-r--r-- 1 root root 138953 May 19 03:04 /root/persuasion_turn_jailbreak_detect/paper/figures/cka_heatmap.png\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_cka-heatmap_20260518T190351",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-18T19:04:26.087460+00:00_

文件已生成：

- **PDF**: `/root/persuasion_turn_jailbreak_detect/paper/figures/cka_heatmap.pdf` (18.8 KB)
- **PNG**: `/root/persuasion_turn_jailbreak_detect/paper/figures/cka_heatmap.png` (139 KB)

2×2 布局，单栏宽度 (3.4 inch)，YlOrRd colormap，对角线 1.0，所有格子标注数值，字体 ≥ 7pt，共享 colorbar。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_cka-heatmap_20260518T190351"
}
```

</details>

---
