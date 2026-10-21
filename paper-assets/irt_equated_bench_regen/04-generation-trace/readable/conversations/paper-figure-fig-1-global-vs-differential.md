# paper figure fig 1 global vs differential

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_paper_figure_fig_1_global_vs_differential_20260521T011552.jsonl`
- **Structured JSON:** [`3823393f517595562358.json`](../../sessions/38/3823393f517595562358.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-21T01:17:24.841170+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-visualization.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-visualization.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T01:17:24.841808+00:00_

1	---
2	description: 学术论文图表设计与生成——四层指南（防丑原则 + 叙事原则 + Pattern 库 + 工具路由）。Paper Agent 规划 visualization_plan 时读，Worker 执行时也读。
3	name: paper-visualization
4	scope: global
5	tags:
6	- research
7	- visualization
8	- paper
9	- matplotlib
10	- paperbanana
11	version: 5
12	roles:
13	- agent
14	- paper_agent
15	---
16	
17	# Paper Visualization — 学术图表设计与生成
18	
19	> **核心理念**：好图不是"画得对"，是"回答一个问题"。每张图动笔前先问：**这张图要让读者看到什么？**
20	
21	本 skill 分五层：
22	
23	- **L0 学习同行** — 设计前看几张优秀同类型论文图，比读任何原则都有效
24	- **L1 防丑原则** — 底线，所有图必须遵守
25	- **L2 叙事原则** — 让图有说服力（区分"数据图"和"论证图"）
26	- **L3 Pattern 库** — 具体技法目录，按 `design_notes` 选用
27	- **L4 工具路由 + 模板** — paperbanana vs matplotlib，常用统计图模板
28	
29	---
30	
31	## L0 学习同行（设计前的功课）
32	
33	你的子领域里，**最被引用、最被记住的论文是怎么画图的？** 在动笔之前花点时间去看一眼——这个动作的回报远高于读完下面的 L1-L4。
34	
35	### 为什么这一步是重要的
36	
37	- 同领域读者已经被这些论文的视觉语言"训练"过——遵循惯例 = 降低读者认知负担
38	- 顶会论文经历过 reviewer 严苛审查，能登出来的图基本说明它的 narrative 设计是被接受的
39	- 抽象原则告诉你"用 fill_between 表示发散"，但好论文告诉你"在这种数据上，发散到底应该画多淡才合适"
40	- 一个领域往往有它特有的图表惯例（如校准研究的 reliability diagram、scaling 研究的 log-log curve、RL 的 learning curve with seed bands），不看就不会用
41	
42	### 什么时候值得投入
43	
44	判断权交给你。一些可参考的信号：
45	
46	- **值得多花时间**：会决定论文成败的图（hero figure、main result、新颖的实验类型）
47	- **不太值得**：常规 supplementary 图、loss curve 这类标准化已经很高的图
48	- **强烈建议看**：你打算画一种自己不熟悉的图，或者数据形态是这个领域少见的
49	
50	### 怎么看
51	
52	工具：`paper-image-extractor` skill 可以从 arXiv source 或 PDF 提取参考论文里的 figure。你已经有 `literature_map.yaml` 里的论文清单作为起点。
53	
54	看的时候问自己（不是机械检查清单，是真的去理解）：
55	
56	- 这张图回答了什么问题？读者一眼能 get 到吗？
57	- 它用了哪些叙事层（background band / 参考线 / 概念曲线 / fill 区域）？这些层在我的数据上有对应物吗？
58	- 它的颜色和 marker 怎么承载语义？我的图能不能借鉴这套映射？
59	- 它有什么是这篇论文特有的（与他们的具体数据 / claim 绑死）？这些不要照搬。
60	- 如果让我重画它的图，我会怎么改？为什么作者没这么做？
61	
62	### 怎么把学到的传下去
63	
64	把你看完后的判断**直接写进对应 fig 的 `design_notes`**，用人话不用模板。例子：
65	
66	```yaml
67	design_notes:
68	  - "学 GPTQ Fig 4：用 log-scale bit-width + dashed FP16 baseline + 不同 marker shape 分模型族"
69	  - "Pattern A（regime band）划分 in-domain / OOD 两段"
70	  - "AWQ Fig 2 那种 hatching 区分 outlier 不适用我们的数据，跳过"
71	```
72	
73	
…[truncated 11092 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T01:17:24.842031+00:00_

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
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T01:17:24.842413+00:00_

1	---
2	description: 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG
3	name: draw-paper-figure
4	scope: global
5	tags:
6	  - research
7	  - visualization
8	  - paper
9	  - matplotlib
10	version: 2
11	tools:
12	  - ssh_execute
13	---
14	
15	# Draw Paper Figure — 学术图表生成（Worker 执行）
16	
17	Worker 收到画图任务时读本 skill。**画图前必读** `skills/global/paper-visualization.skill.md` 的 L1/L2 原则和 L3 pattern 库。
18	
19	本 skill 提供：
20	- 通用样式（rcParams + 色板）
21	- 三个常用图表的起点模板（reliability/heatmap/scatter）
22	- NeurIPS 经验提炼的 pattern 实现示例
23	
24	## 输入字段（从 Paper Agent 传入）
25	
26	- `fig_id` / `type` / `placement` / `data_source` / `aspect_ratio` / 输出路径
27	- **`narrative_intent`**：一句话，这张图要让读者相信什么
28	- **`design_notes`**：从 paper-visualization L3 选的 pattern 列表
29	
30	## 画图工作流
31	
32	1. 读 paper-visualization skill 的 L1 防丑原则 + L2 叙事原则
33	2. 根据 `narrative_intent` 选起点模板（本 skill §模板）
34	3. 按 `design_notes` 中每个 pattern 添加相应技法（本 skill §pattern 实现）
35	4. 提交前过本 skill §checklist
36	
37	## 通用样式标准（所有图表必须遵守）
38	
39	```python
40	import matplotlib
41	matplotlib.use('Agg')
42	import matplotlib.pyplot as plt
43	import matplotlib.patches as mpatches
44	import numpy as np
45	
46	# 字体和全局样式
47	plt.rcParams.update({
48	    'font.family': 'DejaVu Sans',
49	    'font.size': 11,
50	    'axes.titlesize': 13,
51	    'axes.labelsize': 12,
52	    'xtick.labelsize': 10,
53	    'ytick.labelsize': 10,
54	    'legend.fontsize': 10,
55	    'figure.dpi': 300,
56	    'savefig.dpi': 300,
57	    'savefig.bbox': 'tight',
58	    'savefig.pad_inches': 0.05,
59	    'axes.spines.top': False,
60	    'axes.spines.right': False,
61	    'lines.linewidth': 1.8,
62	})
63	
64	# 色盲友好配色（Okabe-Ito）
65	COLORS = {
66	    'fp16':   '#E69F00',  # 橙黄
67	    'nf4':    '#56B4E9',  # 天蓝
68	    'int8':   '#009E73',  # 绿
69	    'gptq':   '#F0E442',  # 黄
70	    'awq':    '#CC79A7',  # 粉紫
71	    'llama':  '#0072B2',  # 深蓝
72	    'qwen3':  '#D55E00',  # 橙红
73	    'gemma':  '#009E73',  # 绿
74	    'mistral':'#CC79A7',  # 
…[truncated 15285 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T01:17:24.842603+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper",
  "description": "Create output directory for figures"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper",
    "description": "Create output directory for figures"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T01:17:24.842774+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T01:17:24.842942+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_1_global_vs_differential.py",
  "content": "\"\"\"\nfig_1_global_vs_differential — Global vs Differential Contamination concept diagram.\n\nTwo-panel ICC illustration: left panel shows overlapping curves (global contamination,\nno DIF), right panel shows diverging curves (differential contamination, DIF detected).\n\"\"\"\n\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nimport numpy as np\nfrom pathlib import Path\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 11,\n    'axes.titlesize': 13,\n    'axes.labelsize': 12,\n    'xtick.labelsize': 10,\n    'ytick.labelsize': 10,\n    'legend.fontsize': 10,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n    'lines.linewidth': 1.8,\n})\n\nCOL_REF = '#0072B2'\nCOL_FOCAL = '#D55E00'\n\nOUTDIR = Path(__file__).parent\nSTEM = 'fig_1_global_vs_differential'\n\n\ndef icc(theta, a=1.5, b=0.0):\n    return 1.0 / (1.0 + np.exp(-a * (theta - b)))\n\n\ntheta = np.linspace(-3, 3, 300)\n\n# --- Left panel curves (identical) ---\ny_ref_L = icc(theta, a=1.5, b=0.0)\ny_foc_L = icc(theta, a=1.5, b=0.0)\n\n# --- Right panel curves (DIF: focal shifted left) ---\ny_ref_R = icc(theta, a=1.5, b=0.0)\ny_foc_R = icc(theta, a=1.5, b=-1.2)\n\n# --- Figure ---\nfig, (ax_L, ax_R) = plt.subplots(\n    1, 2, figsize=(11, 4.5), sharey=True,\n    gridspec_kw={'wspace': 0.25}\n)\n\nbbox_style = dict(boxstyle='round,pad=0.4', facecolor='#F0F0F0', edgecolor='#CCCCCC',\n                  alpha=0.92)\n\n# ====== LEFT PANEL: Global Contamination ======\nax_L.plot(theta, y_ref_L, color=COL_REF, linestyle='-', linewidth=2.2,\n          label='Reference cohort (2023)')\nax_L.plot(theta, y_foc_L, color=COL_FOCAL, linestyle='--', linewidth=2.2,\n          label='Focal cohort (2024-H1)')\n\nax_L.set_title('Global Contamination', fontweight='bold', pad=10)\nax_L.set_xlabel(r'Ability ($\\theta$)')\nax_L.set_ylabel('P(correct)')\nax_L.set_xlim(-3, 3)\nax_L.set_ylim(0, 1.0)\n\nax_L.legend(loc='lower right', frameon=True, fancybox=True, framealpha=0.9,\n            edgecolor='#CCCCCC')\n\n# Annotations — left panel\nax_L.text(0.04, 0.92, r'$\\Delta_\\mathrm{MH} \\approx 0$  (no DIF)',\n          transform=ax_L.transAxes, fontsize=9.5, color='#444444',\n          bbox=bbox_style, va='top')\n\nax_L.text(0.04, 0.78,\n          'Li et al.: ✓ contaminated\\nDIF: ✗ no group difference',\n          transform=ax_L.transAxes, fontsize=8.5, color='#555555',\n          bbox=bbox_style, va='top', linespacing=1.5)\n\n# Subtle note about web overlap\nax_L.annotate('Item on Common Crawl since 2020\\n→ both cohorts trained on it',\n              xy=(0.0, icc(0.0)), xytext=(-2.4, 0.78),\n              fontsize=8, color='#666666', fontstyle='italic',\n              arrowprops=dict(arrowstyle='->', color='#999999', lw=0.8),\n              bbox=dict(boxstyle='round,pad=0.3', facecolor='white',\n                        edgecolor='#DDDDDD', alpha=0.85))\n\n# ====== RIGHT PANEL: Differential Contamination ======\nax_R.plot(theta, y_ref_R, color=COL_REF, linestyle='-', linewidth=2.2)\nax_R.plot(theta, y_foc_R, color=COL_FOCAL, linestyle='--', linewidth=2.2)\n\n# Shaded DIF area between curves\nax_R.fill_between(theta, y_ref_R, y_foc_R, where=(y_foc_R > y_ref_R),\n                  color=COL_FOCAL, alpha=0.18, label='_nolegend_')\nax_R.fill_between(theta, y_ref_R, y_foc_R, where=(y_foc_R <= y_ref_R),\n                  color=COL_FOCAL, alpha=0.18, label='_nolegend_')\n\n# DIF magnitude label inside shaded area\nmid_theta = -0.6\nmid_y = (icc(mid_theta, b=0.0) + icc(mid_theta, b=-1.2)) / 2\nax_R.annotate('DIF\\nmagnitude', xy=(mid_theta, mid_y),\n              fontsize=8.5, color=COL_FOCAL, fontweight='bold',\n              ha='center', va='center',\n              bbox=dict(boxstyle='round,pad=0.3', facecolor='white',\n                        edgecolor=COL_FOCAL, alpha=0.85, linewidth=0.8))\n\nax_R.set_title('Differential Contamination', fontweight='bold', pad=10)\nax_R.set_xlabel(r'Ability ($\\theta$)')\nax_R.set_xlim(-3, 3)\n\n# Annotations — right panel\nax_R.text(0.04, 0.92, r'$|\\Delta_\\mathrm{MH}| \\geq 1.5$  (ETS C)',\n          transform=ax_R.transAxes, fontsize=9.5, color='#444444',\n          bbox=bbox_style, va='top')\n\nax_R.text(0.04, 0.78,\n          'Li et al.: may or may not flag\\nDIF: ✓ detected (ETS C)',\n          transform=ax_R.transAxes, fontsize=8.5, color='#555555',\n          bbox=bbox_style, va='top', linespacing=1.5)\n\n# Arrow noting focal curve is shifted\nax_R.annotate('Focal curve shifted left\\n(easier for focal group)',\n              xy=(-1.2, 0.5), xytext=(-2.6, 0.28),\n              fontsize=8, color=COL_FOCAL, fontstyle='italic',\n              arrowprops=dict(arrowstyle='->', color=COL_FOCAL, lw=0.9),\n              bbox=dict(boxstyle='round,pad=0.3', facecolor='white',\n                        edgecolor='#DDDDDD', alpha=0.85))\n\n# ====== BOTTOM ANNOTATION spanning both panels ======\nfig.text(0.5, -0.02,\n         'Enrichment ≈ 1.0: most MMLU items are globally contaminated (left), '\n         'not differentially (right)',\n         ha='center', va='top', fontsize=10, color='#333333',\n         bbox=dict(boxstyle='round,pad=0.5', facecolor='#FAFAFA',\n                   edgecolor='#BBBBBB', alpha=0.95))\n\n# ====== SAVE ======\nfor ext in ('pdf', 'png'):\n    outpath = OUTDIR / f'{STEM}.{ext}'\n    fig.savefig(outpath, dpi=300, bbox_inches='tight')\n    print(f'Saved: {outpath}')\n\nplt.close(fig)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_1_global_vs_differential.py",
    "content": "\"\"\"\nfig_1_global_vs_differential — Global vs Differential Contamination concept diagram.\n\nTwo-panel ICC illustration: left panel shows overlapping curves (global contamination,\nno DIF), right panel shows diverging curves (differential contamination, DIF detected).\n\"\"\"\n\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nimport numpy as np\nfrom pathlib import Path\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 11,\n    'axes.titlesize': 13,\n    'axes.labelsize': 12,\n    'xtick.labelsize': 10,\n    'ytick.labelsize': 10,\n    'legend.fontsize': 10,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n    'lines.linewidth': 1.8,\n})\n\nCOL_REF = '#0072B2'\nCOL_FOCAL = '#D55E00'\n\nOUTDIR = Path(__file__).parent\nSTEM = 'fig_1_global_vs_differential'\n\n\ndef icc(theta, a=1.5, b=0.0):\n    return 1.0 / (1.0 + np.exp(-a * (theta - b)))\n\n\ntheta = np.linspace(-3, 3, 300)\n\n# --- Left panel curves (identical) ---\ny_ref_L = icc(theta, a=1.5, b=0.0)\ny_foc_L = icc(theta, a=1.5, b=0.0)\n\n# --- Right panel curves (DIF: focal shifted left) ---\ny_ref_R = icc(theta, a=1.5, b=0.0)\ny_foc_R = icc(theta, a=1.5, b=-1.2)\n\n# --- Figure ---\nfig, (ax_L, ax_R) = plt.subplots(\n    1, 2, figsize=(11, 4.5), sharey=True,\n    gridspec_kw={'wspace': 0.25}\n)\n\nbbox_style = dict(boxstyle='round,pad=0.4', facecolor='#F0F0F0', edgecolor='#CCCCCC',\n                  alpha=0.92)\n\n# ====== LEFT PANEL: Global Contamination ======\nax_L.plot(theta, y_ref_L, color=COL_REF, linestyle='-', linewidth=2.2,\n          label='Reference cohort (2023)')\nax_L.plot(theta, y_foc_L, color=COL_FOCAL, linestyle='--', linewidth=2.2,\n          label='Focal cohort (2024-H1)')\n\nax_L.set_title('Global Contamination', fontweight='bold', pad=10)\nax_L.set_xlabel(r'Ability ($\\theta$)')\nax_L.set_ylabel('P(correct)')\nax_L.set_xlim(-3, 3)\nax_L.set_ylim(0, 1.0)\n\nax_L.legend(loc='lower right', frameon=True, fancybox=True, framealpha=0.9,\n            edgecolor='#CCCCCC')\n\n# Annotations — left panel\nax_L.text(0.04, 0.92, r'$\\Delta_\\mathrm{MH} \\approx 0$  (no DIF)',\n          transform=ax_L.transAxes, fontsize=9.5, color='#444444',\n          bbox=bbox_style, va='top')\n\nax_L.text(0.04, 0.78,\n          'Li et al.: ✓ contaminated\\nDIF: ✗ no group difference',\n          transform=ax_L.transAxes, fontsize=8.5, color='#555555',\n          bbox=bbox_style, va='top', linespacing=1.5)\n\n# Subtle note about web overlap\nax_L.annotate('Item on Common Crawl since 2020\\n→ both cohorts trained on it',\n              xy=(0.0, icc(0.0)), xytext=(-2.4, 0.78),\n              fontsize=8, color='#666666', fontstyle='italic',\n              arrowprops=dict(arrowstyle='->', color='#999999', lw=0.8),\n              bbox=dict(boxstyle='round,pad=0.3', facecolor='white',\n                        edgecolor='#DDDDDD', alpha=0.85))\n\n# ====== RIGHT PANEL: Differential Contamination ======\nax_R.plot(theta, y_ref_R, color=COL_REF, linestyle='-', linewidth=2.2)\nax_R.plot(theta, y_foc_R, color=COL_FOCAL, linestyle='--', linewidth=2.2)\n\n# Shaded DIF area between curves\nax_R.fill_between(theta, y_ref_R, y_foc_R, where=(y_foc_R > y_ref_R),\n                  color=COL_FOCAL, alpha=0.18, label='_nolegend_')\nax_R.fill_between(theta, y_ref_R, y_foc_R, where=(y_foc_R <= y_ref_R),\n                  color=COL_FOCAL, alpha=0.18, label='_nolegend_')\n\n# DIF magnitude label inside shaded area\nmid_theta = -0.6\nmid_y = (icc(mid_theta, b=0.0) + icc(mid_theta, b=-1.2)) / 2\nax_R.annotate('DIF\\nmagnitude', xy=(mid_theta, mid_y),\n              fontsize=8.5, color=COL_FOCAL, fontweight='bold',\n              ha='center', va='center',\n              bbox=dict(boxstyle='round,pad=0.3', facecolor='white',\n                        edgecolor=COL_FOCAL, alpha=0.85, linewidth=0.8))\n\nax_R.set_title('Differential Contamination', fontweight='bold', pad=10)\nax_R.set_xlabel(r'Ability ($\\theta$)')\nax_R.set_xlim(-3, 3)\n\n# Annotations — right panel\nax_R.text(0.04, 0.92, r'$|\\Delta_\\mathrm{MH}| \\geq 1.5$  (ETS C)',\n          transform=ax_R.transAxes, fontsize=9.5, color='#444444',\n          bbox=bbox_style, va='top')\n\nax_R.text(0.04, 0.78,\n          'Li et al.: may or may not flag\\nDIF: ✓ detected (ETS C)',\n          transform=ax_R.transAxes, fontsize=8.5, color='#555555',\n          bbox=bbox_style, va='top', linespacing=1.5)\n\n# Arrow noting focal curve is shifted\nax_R.annotate('Focal curve shifted left\\n(easier for focal group)',\n              xy=(-1.2, 0.5), xytext=(-2.6, 0.28),\n              fontsize=8, color=COL_FOCAL, fontstyle='italic',\n              arrowprops=dict(arrowstyle='->', color=COL_FOCAL, lw=0.9),\n              bbox=dict(boxstyle='round,pad=0.3', facecolor='white',\n                        edgecolor='#DDDDDD', alpha=0.85))\n\n# ====== BOTTOM ANNOTATION spanning both panels ======\nfig.text(0.5, -0.02,\n         'Enrichment ≈ 1.0: most MMLU items are globally contaminated (left), '\n         'not differentially (right)',\n         ha='center', va='top', fontsize=10, color='#333333',\n         bbox=dict(boxstyle='round,pad=0.5', facecolor='#FAFAFA',\n                   edgecolor='#BBBBBB', alpha=0.95))\n\n# ====== SAVE ======\nfor ext in ('pdf', 'png'):\n    outpath = OUTDIR / f'{STEM}.{ext}'\n    fig.savefig(outpath, dpi=300, bbox_inches='tight')\n    print(f'Saved: {outpath}')\n\nplt.close(fig)\n"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T01:17:24.843154+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_1_global_vs_differential.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T01:17:24.843326+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper && python3 fig_1_global_vs_differential.py",
  "description": "Execute figure generation script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper && python3 fig_1_global_vs_differential.py",
    "description": "Execute figure generation script"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T01:17:24.843453+00:00_

Saved: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_1_global_vs_differential.pdf
Saved: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_1_global_vs_differential.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T01:17:24.843572+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_1_global_vs_differential.{pdf,png}",
  "description": "Verify output files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_1_global_vs_differential.{pdf,png}",
    "description": "Verify output files exist"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T01:17:24.843688+00:00_

-rw-r--r-- 1 ubuntu ubuntu  41007 May 21 01:16 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_1_global_vs_differential.pdf
-rw-r--r-- 1 ubuntu ubuntu 304087 May 21 01:16 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_1_global_vs_differential.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T01:17:24.843876+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_1_global_vs_differential.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_1_global_vs_differential.png"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T01:17:24.844458+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T01:17:24.844643+00:00_

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
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552",
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

_source line 16 · 2026-05-21T01:17:24.844818+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T01:17:24.844958+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "fig_1_global_vs_differential",
  "type": "chart",
  "description": "Two-panel ICC concept diagram: left panel shows overlapping curves (global contamination, no DIF), right panel shows diverging curves (differential contamination, DIF detected). Illustrates why enrichment ≈ 1.0 between DIF flags and web-overlap labels is expected.",
  "project": "irt_equated_bench_regen",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_1_global_vs_differential.pdf",
  "tags": "['figure1', 'introduction', 'concept-diagram', 'ICC', 'DIF', 'contamination']",
  "skill": "draw-paper-figure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "fig_1_global_vs_differential",
    "type": "chart",
    "description": "Two-panel ICC concept diagram: left panel shows overlapping curves (global contamination, no DIF), right panel shows diverging curves (differential contamination, DIF detected). Illustrates why enrichment ≈ 1.0 between DIF flags and web-overlap labels is expected.",
    "project": "irt_equated_bench_regen",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_1_global_vs_differential.pdf",
    "tags": "['figure1', 'introduction', 'concept-diagram', 'ICC', 'DIF', 'contamination']",
    "skill": "draw-paper-figure"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T01:17:24.845119+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_1a7f36\", \"name\": \"fig_1_global_vs_differential\", \"type\": \"chart\", \"description\": \"Two-panel ICC concept diagram: left panel shows overlapping curves (global contamination, no DIF), right panel shows diverging curves (differential contamination, DIF detected). Illustrates why enrichment ≈ 1.0 between DIF flags and web-overlap labels is expected.\", \"path\": \"projects/irt_equated_bench_regen/artifacts/_project/chart/fig_1_global_vs_differential.pdf\", \"url\": null, \"project\": \"irt_equated_bench_regen\", \"exp_id\": null, \"skill\": \"draw-paper-figure\", \"created_at\": \"2026-05-21T01:17:17.476076+00:00\", \"tags\": [\"figure1\", \"introduction\", \"concept-diagram\", \"ICC\", \"DIF\", \"contamination\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-21T01:17:24.845293+00:00_

Figure generated and registered (`art_20260521_1a7f36`).

**Output files:**
- PDF: `figures/paper/fig_1_global_vs_differential.pdf` (41 KB, vector)
- PNG: `figures/paper/fig_1_global_vs_differential.png` (304 KB, 300 DPI)
- Script: `figures/paper/fig_1_global_vs_differential.py`

**What's in the figure:**
- **Left panel** — two perfectly overlapping ICC curves (Reference blue solid, Focal orange dashed). Annotated: Li et al. flags it as contaminated, but DIF finds no group difference (Δ_MH ≈ 0).
- **Right panel** — focal curve shifted left (b = −1.2), creating a visible divergence with orange shaded DIF area. Annotated: |Δ_MH| ≥ 1.5 (ETS C), Li et al. may or may not flag.
- **Bottom text** — "Enrichment ≈ 1.0: most MMLU items are globally contaminated (left), not differentially (right)"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_figure_fig_1_global_vs_differential_20260521T011552"
}
```

</details>

---
