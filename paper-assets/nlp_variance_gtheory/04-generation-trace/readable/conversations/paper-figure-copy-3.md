# paper figure

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_paper_figure_20260521T173555.jsonl`
- **Structured JSON:** [`63f4639e09bf315c28cb.json`](../../sessions/63/63f4639e09bf315c28cb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

43 recorded events

### Tool call

_source line 1 · 2026-05-21T17:52:41.458868+00:00_

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
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T17:52:41.459423+00:00_

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
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T17:52:41.459613+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-visualization.skill.md",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-visualization.skill.md",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T17:52:41.459909+00:00_

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
…[truncated 2783 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T17:52:41.460485+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-visualization.skill.md",
  "offset": "100",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-visualization.skill.md",
    "offset": "100",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T17:52:41.460781+00:00_

100	
101	---
102	
103	## L2 叙事原则（让图变成论证）
104	
105	L1 让图"不丑"，L2 让图"有说服力"。这一层是 Agent 自主画图时最容易缺失的。
106	
107	### 原则 1：每张图回答一个明确问题
108	
109	动笔前用一句话写下："This figure shows that ___."
110	
111	如果写不出来，就不要画。如果写出来的 takeaway 不是论文的 claim，就要重新设计。
112	
113	**反例**：`"Accuracy across methods"` — 这只是个标题，不是问题
114	**正例**：`"FP16 baseline 在小模型上比量化版高 5pp，但 70B 模型上差距消失"` — 这是一张图要说服读者相信的事
115	
116	`visualization_plan.{fig_id}.narrative_intent` 字段写这一句。
117	
118	### 原则 2：颜色绑定语义而非数据顺序
119	
120	错的做法：`colors = ['blue', 'orange', 'green', 'red']` 按数据顺序分配。
121	对的做法：`BN → 蓝色（始终）`、`non-BN → 橙色（始终）`、`collapse/danger → vermillion (#D55E00)`、`safe/baseline → blue (#0072B2)`。
122	
123	整篇论文 6 张图，BN 永远蓝、collapse 永远红——零认知负担，读者一眼建立映射。
124	
125	### 原则 3：信息层级用 visual variable 表达
126	
127	数据的"质量"和"分类"应该可见，不应该藏在 caption 里：
128	
129	| 信息 | Visual 表达 |
130	|------|------------|
131	| n < 50 低置信度点 | hollow marker + 标注 `n=` |
132	| Out-of-sample / pending 数据 | hollow + 不同 marker shape（如 diamond）+ "OOS" label |
133	| Collapse / 异常类别 | hatching（斜线填充）|
134	| 主结果 vs 次要结果 | 主用饱和色，次要用 muted 色或 alpha |
135	
136	### 原则 4：加叙事层，不只画数据
137	
138	数据是图的基础，叙事层是让读者"读懂"的关键。常见叙事层：
139	
140	- **Background bands** — `axhspan/axvspan` 标定性区域（"collapse zone"、"safe zone"、"Regime A/B/C"）
141	- **Fill_between** — 显示两条曲线发散区域（alpha 极低如 0.06，不抢眼但有面积）
142	- **Reference lines** — 锚定真实值（如 dashed line 标"actual W3A16 accuracy"）
143	- **Equivalence band** — `axvspan` gradient fade 标 +/-1pp 等价区间
144	- **Concept curve** — 完全合成的曲线（如 cosine trajectory）建立理论直觉
145	
146	这些都不来自数据，但帮读者"看到"数据想说什么。
147	
148	### 原则 5：Subtitle / panel label 写 insight 不写描述
149	
150	错：`"Layer 6 comparison across three models"`
151	对：`"Same relative position, opposite function"`
152	
153	错：`"Reliability diagram"`
154	对：`"Quantization shifts confidence but not accuracy"`
155	
156	副标题是免费的 takeaway，不要浪费。
157	
158	### 原则 6：Multi-panel 每个面板独立回答一个 sub-question
159	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T17:52:41.460934+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/ 2>/dev/null; /home/ubuntu/agent-ml-research/.venv/bin/python -c \"import matplotlib; print(matplotlib.__version__); import matplotlib.font_manager as fm; fonts = [f.name for f in fm.fontManager.ttflist if 'Serif' in f.name or 'serif' in f.name]; print(sorted(set(fonts))[:10])\"",
  "description": "Check output dir and available serif fonts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/ 2>/dev/null; /home/ubuntu/agent-ml-research/.venv/bin/python -c \"import matplotlib; print(matplotlib.__version__); import matplotlib.font_manager as fm; fonts = [f.name for f in fm.fontManager.ttflist if 'Serif' in f.name or 'serif' in f.name]; print(sorted(set(fonts))[:10])\"",
    "description": "Check output dir and available serif fonts"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T17:52:41.461057+00:00_

fig1_cross_benchmark.pdf
fig1_cross_benchmark.png
gen_fig1_cross_benchmark.py
3.10.8
['DejaVu Serif', 'DejaVu Serif Display', 'Liberation Serif']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T17:52:41.461212+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Figure 3: D-Study Projection Curves — G coefficient vs. number of benchmark items.\"\"\"\n\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nimport numpy as np\nimport os\n\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],\n    'font.size': 9,\n    'axes.labelsize': 9,\n    'xtick.labelsize': 8,\n    'ytick.labelsize': 8,\n    'legend.fontsize': 7.5,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.08,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n})\n\nBLUE = '#2166ac'\nRED  = '#e41a1c'\nGRAY = '#666666'\n\n# ---------------------------------------------------------------------------\n# D-study G coefficient: G(n) = n / (n + C), where C = sigma_delta / sigma_p\n#\n# Variance components from exp-001 cross-model G-study (Henderson I):\n#   item_id (sigma_p): 42.1%  |  model:item 33.6%  |  residual 19.5%\n#   prompt:item 2.8%  |  seed:item 2.5%  |  precision:item 2.0%\n#   temperature:item 1.0%  |  ordering:item 0.6%\n#\n# Multi-facet design: n_model=4, n_prompt=6, n_seed=6, n_temp=3, n_ord=4, n_prec=3\n# C values derived from full G-study (all interaction terms including higher-order):\n# ---------------------------------------------------------------------------\nC_MULTI  = 18.0    # multi-facet (432 conditions/item)\nC_SINGLE = 157.75  # single-condition (1 condition/item)\n\nn = np.arange(1, 701)\nG_m = n / (n + C_MULTI)\nG_s = n / (n + C_SINGLE)\n\nN_M80 = 72\nN_S80 = 631\nN_IRT = 116\nG_IRT = N_IRT / (N_IRT + C_SINGLE)\n\nstroke = [pe.withStroke(linewidth=2.5, foreground='white')]\n\nfig, ax = plt.subplots(figsize=(3.5, 2.8))\n\n# Shaded region below G = 0.80\nax.fill_between([0, 700], 0, 0.80, color='#f4f4f4', zorder=0)\n\n# Threshold line\nax.axhline(0.80, color=GRAY, ls='--', lw=1.0, alpha=0.7, zorder=2)\n\n# IRT vertical line\nax.axvline(N_IRT, color='#bbbbbb', ls=':', lw=0.8, zorder=1)\n\n# Curves\nax.plot(n, G_m, color=BLUE, lw=1.5, solid_capstyle='round',\n        label='Multi-facet (432 cond./item)', zorder=3)\nax.plot(n, G_s, color=RED, lw=1.5, ls='--',\n        label='Single-condition', zorder=3)\n\n# Intersection dots\nfor nx, c in [(N_M80, BLUE), (N_S80, RED)]:\n    ax.plot(nx, 0.80, 'o', color=c, ms=4, zorder=5, mec='white', mew=0.6)\n\n# IRT diamond\nax.plot(N_IRT, G_IRT, 'D', color='#888888', ms=3.5, zorder=5)\n\n# --- Annotations ---\n\nt = ax.annotate('72 items', xy=(72, 0.80), xytext=(170, 0.63),\n                fontsize=7, color=BLUE, fontweight='bold',\n                arrowprops=dict(arrowstyle='->', color=BLUE, lw=0.8),\n                ha='left', zorder=6)\nt.set_path_effects(stroke)\n\nt = ax.annotate('631 items', xy=(631, 0.80), xytext=(495, 0.92),\n                fontsize=7, color=RED, fontweight='bold',\n                arrowprops=dict(arrowstyle='->', color=RED, lw=0.8),\n                ha='right', zorder=6)\nt.set_path_effects(stroke)\n\nt = ax.annotate(f'IRT rec. → G = {G_IRT:.2f}',\n                xy=(N_IRT, G_IRT), xytext=(235, 0.33),\n                fontsize=6.5, color='#777777',\n                arrowprops=dict(arrowstyle='->', color='#aaaaaa', lw=0.7),\n                zorder=6)\nt.set_path_effects(stroke)\n\nt = ax.text(440, 0.825, 'Reliability threshold (G = 0.80)',\n            fontsize=6.5, color=GRAY, ha='center', va='bottom')\nt.set_path_effects(stroke)\n\nax.text(350, 0.15, 'Below reliability threshold',\n        fontsize=7, color='#bbbbbb', ha='center', fontstyle='italic')\n\n# --- Axes ---\nax.set_xlim(0, 700)\nax.set_ylim(0, 1.0)\nax.set_xlabel('Number of items')\nax.set_ylabel('Generalizability coefficient (G)')\nax.set_xticks([0, 100, 200, 300, 400, 500, 600, 700])\nax.set_yticks(np.arange(0, 1.1, 0.2))\n\nax.legend(loc='lower right', framealpha=0.9, edgecolor='none')\nax.yaxis.grid(True, alpha=0.12, lw=0.4)\n\nplt.tight_layout()\n\n# --- Save ---\noutdir = os.path.dirname(os.path.abspath(__file__))\nfor ext in ('pdf', 'png'):\n    fig.savefig(os.path.join(outdir, f'fig3_dstudy_curves.{ext}'))\nplt.close()\n\n# Verification\nprint('Saved fig3_dstudy_curves.pdf + .png')\nfor label, ni, C in [('Multi@72', 72, C_MULTI), ('Multi@200', 200, C_MULTI),\n                      ('Single@200', 200, C_SINGLE), ('Single@631', 631, C_SINGLE)]:\n    print(f'  {label}: G = {ni/(ni+C):.3f}')\nprint(f'  IRT@116 (single): G = {G_IRT:.3f}')\nprint(f'  Ratio: {N_S80/N_M80:.1f}x')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Figure 3: D-Study Projection Curves — G coefficient vs. number of benchmark items.\"\"\"\n\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nimport numpy as np\nimport os\n\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],\n    'font.size': 9,\n    'axes.labelsize': 9,\n    'xtick.labelsize': 8,\n    'ytick.labelsize': 8,\n    'legend.fontsize': 7.5,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.08,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n})\n\nBLUE = '#2166ac'\nRED  = '#e41a1c'\nGRAY = '#666666'\n\n# ---------------------------------------------------------------------------\n# D-study G coefficient: G(n) = n / (n + C), where C = sigma_delta / sigma_p\n#\n# Variance components from exp-001 cross-model G-study (Henderson I):\n#   item_id (sigma_p): 42.1%  |  model:item 33.6%  |  residual 19.5%\n#   prompt:item 2.8%  |  seed:item 2.5%  |  precision:item 2.0%\n#   temperature:item 1.0%  |  ordering:item 0.6%\n#\n# Multi-facet design: n_model=4, n_prompt=6, n_seed=6, n_temp=3, n_ord=4, n_prec=3\n# C values derived from full G-study (all interaction terms including higher-order):\n# ---------------------------------------------------------------------------\nC_MULTI  = 18.0    # multi-facet (432 conditions/item)\nC_SINGLE = 157.75  # single-condition (1 condition/item)\n\nn = np.arange(1, 701)\nG_m = n / (n + C_MULTI)\nG_s = n / (n + C_SINGLE)\n\nN_M80 = 72\nN_S80 = 631\nN_IRT = 116\nG_IRT = N_IRT / (N_IRT + C_SINGLE)\n\nstroke = [pe.withStroke(linewidth=2.5, foreground='white')]\n\nfig, ax = plt.subplots(figsize=(3.5, 2.8))\n\n# Shaded region below G = 0.80\nax.fill_between([0, 700], 0, 0.80, color='#f4f4f4', zorder=0)\n\n# Threshold line\nax.axhline(0.80, color=GRAY, ls='--', lw=1.0, alpha=0.7, zorder=2)\n\n# IRT vertical line\nax.axvline(N_IRT, color='#bbbbbb', ls=':', lw=0.8, zorder=1)\n\n# Curves\nax.plot(n, G_m, color=BLUE, lw=1.5, solid_capstyle='round',\n        label='Multi-facet (432 cond./item)', zorder=3)\nax.plot(n, G_s, color=RED, lw=1.5, ls='--',\n        label='Single-condition', zorder=3)\n\n# Intersection dots\nfor nx, c in [(N_M80, BLUE), (N_S80, RED)]:\n    ax.plot(nx, 0.80, 'o', color=c, ms=4, zorder=5, mec='white', mew=0.6)\n\n# IRT diamond\nax.plot(N_IRT, G_IRT, 'D', color='#888888', ms=3.5, zorder=5)\n\n# --- Annotations ---\n\nt = ax.annotate('72 items', xy=(72, 0.80), xytext=(170, 0.63),\n                fontsize=7, color=BLUE, fontweight='bold',\n                arrowprops=dict(arrowstyle='->', color=BLUE, lw=0.8),\n                ha='left', zorder=6)\nt.set_path_effects(stroke)\n\nt = ax.annotate('631 items', xy=(631, 0.80), xytext=(495, 0.92),\n                fontsize=7, color=RED, fontweight='bold',\n                arrowprops=dict(arrowstyle='->', color=RED, lw=0.8),\n                ha='right', zorder=6)\nt.set_path_effects(stroke)\n\nt = ax.annotate(f'IRT rec. → G = {G_IRT:.2f}',\n                xy=(N_IRT, G_IRT), xytext=(235, 0.33),\n                fontsize=6.5, color='#777777',\n                arrowprops=dict(arrowstyle='->', color='#aaaaaa', lw=0.7),\n                zorder=6)\nt.set_path_effects(stroke)\n\nt = ax.text(440, 0.825, 'Reliability threshold (G = 0.80)',\n            fontsize=6.5, color=GRAY, ha='center', va='bottom')\nt.set_path_effects(stroke)\n\nax.text(350, 0.15, 'Below reliability threshold',\n        fontsize=7, color='#bbbbbb', ha='center', fontstyle='italic')\n\n# --- Axes ---\nax.set_xlim(0, 700)\nax.set_ylim(0, 1.0)\nax.set_xlabel('Number of items')\nax.set_ylabel('Generalizability coefficient (G)')\nax.set_xticks([0, 100, 200, 300, 400, 500, 600, 700])\nax.set_yticks(np.arange(0, 1.1, 0.2))\n\nax.legend(loc='lower right', framealpha=0.9, edgecolor='none')\nax.yaxis.grid(True, alpha=0.12, lw=0.4)\n\nplt.tight_layout()\n\n# --- Save ---\noutdir = os.path.dirname(os.path.abspath(__file__))\nfor ext in ('pdf', 'png'):\n    fig.savefig(os.path.join(outdir, f'fig3_dstudy_curves.{ext}'))\nplt.close()\n\n# Verification\nprint('Saved fig3_dstudy_curves.pdf + .png')\nfor label, ni, C in [('Multi@72', 72, C_MULTI), ('Multi@200', 200, C_MULTI),\n                      ('Single@200', 200, C_SINGLE), ('Single@631', 631, C_SINGLE)]:\n    print(f'  {label}: G = {ni/(ni+C):.3f}')\nprint(f'  IRT@116 (single): G = {G_IRT:.3f}')\nprint(f'  Ratio: {N_S80/N_M80:.1f}x')\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T17:52:41.461429+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T17:52:41.461557+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "/home/ubuntu/agent-ml-research/.venv/bin/python /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py",
  "description": "Generate Figure 3 D-study curves"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Bash",
  "tool_args": {
    "command": "/home/ubuntu/agent-ml-research/.venv/bin/python /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py",
    "description": "Generate Figure 3 D-study curves"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T17:52:41.461673+00:00_

Saved fig3_dstudy_curves.pdf + .png
  Multi@72: G = 0.800
  Multi@200: G = 0.917
  Single@200: G = 0.559
  Single@631: G = 0.800
  IRT@116 (single): G = 0.424
  Ratio: 8.8x

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T17:52:41.461796+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/fig3_dstudy_curves.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/fig3_dstudy_curves.png"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T17:52:41.462332+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T17:52:41.462482+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/fig3_dstudy_curves.{pdf,png}",
  "description": "Check output file sizes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/fig3_dstudy_curves.{pdf,png}",
    "description": "Check output file sizes"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T17:52:41.462600+00:00_

-rw-r--r-- 1 ubuntu ubuntu  43024 May 21 17:49 /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/fig3_dstudy_curves.pdf
-rw-r--r-- 1 ubuntu ubuntu 118738 May 21 17:49 /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/fig3_dstudy_curves.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T17:52:41.462744+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py",
  "old_string": "t = ax.text(440, 0.825, 'Reliability threshold (G = 0.80)',\n            fontsize=6.5, color=GRAY, ha='center', va='bottom')\nt.set_path_effects(stroke)\n\nax.text(350, 0.15, 'Below reliability threshold',\n        fontsize=7, color='#bbbbbb', ha='center', fontstyle='italic')",
  "new_string": "t = ax.text(460, 0.82, 'Reliability threshold (G = 0.80)',\n            fontsize=6.5, color=GRAY, ha='center', va='bottom',\n            bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))\n\nax.text(180, 0.08, 'Below reliability threshold',\n        fontsize=7, color='#bbbbbb', ha='center', fontstyle='italic')"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py",
    "old_string": "t = ax.text(440, 0.825, 'Reliability threshold (G = 0.80)',\n            fontsize=6.5, color=GRAY, ha='center', va='bottom')\nt.set_path_effects(stroke)\n\nax.text(350, 0.15, 'Below reliability threshold',\n        fontsize=7, color='#bbbbbb', ha='center', fontstyle='italic')",
    "new_string": "t = ax.text(460, 0.82, 'Reliability threshold (G = 0.80)',\n            fontsize=6.5, color=GRAY, ha='center', va='bottom',\n            bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))\n\nax.text(180, 0.08, 'Below reliability threshold',\n        fontsize=7, color='#bbbbbb', ha='center', fontstyle='italic')"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T17:52:41.462888+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T17:52:41.463010+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "/home/ubuntu/agent-ml-research/.venv/bin/python /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py",
  "description": "Regenerate figure with adjusted annotations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Bash",
  "tool_args": {
    "command": "/home/ubuntu/agent-ml-research/.venv/bin/python /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py",
    "description": "Regenerate figure with adjusted annotations"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T17:52:41.463127+00:00_

Saved fig3_dstudy_curves.pdf + .png
  Multi@72: G = 0.800
  Multi@200: G = 0.917
  Single@200: G = 0.559
  Single@631: G = 0.800
  IRT@116 (single): G = 0.424
  Ratio: 8.8x

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T17:52:41.463243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/fig3_dstudy_curves.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/fig3_dstudy_curves.png"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T17:52:41.463791+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T17:52:41.463968+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py",
  "old_string": "ax.text(180, 0.08, 'Below reliability threshold',\n        fontsize=7, color='#bbbbbb', ha='center', fontstyle='italic')",
  "new_string": "ax.text(350, 0.06, 'Below reliability threshold',\n        fontsize=6.5, color='#cccccc', ha='center', fontstyle='italic')"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py",
    "old_string": "ax.text(180, 0.08, 'Below reliability threshold',\n        fontsize=7, color='#bbbbbb', ha='center', fontstyle='italic')",
    "new_string": "ax.text(350, 0.06, 'Below reliability threshold',\n        fontsize=6.5, color='#cccccc', ha='center', fontstyle='italic')"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T17:52:41.464115+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T17:52:41.464246+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py",
  "old_string": "ax.legend(loc='lower right', framealpha=0.9, edgecolor='none')",
  "new_string": "ax.legend(loc='center right', framealpha=0.9, edgecolor='none',\n          bbox_to_anchor=(0.98, 0.35))"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py",
    "old_string": "ax.legend(loc='lower right', framealpha=0.9, edgecolor='none')",
    "new_string": "ax.legend(loc='center right', framealpha=0.9, edgecolor='none',\n          bbox_to_anchor=(0.98, 0.35))"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T17:52:41.464381+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T17:52:41.464521+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "/home/ubuntu/agent-ml-research/.venv/bin/python /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py",
  "description": "Regenerate with legend repositioned"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Bash",
  "tool_args": {
    "command": "/home/ubuntu/agent-ml-research/.venv/bin/python /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py",
    "description": "Regenerate with legend repositioned"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T17:52:41.464635+00:00_

Saved fig3_dstudy_curves.pdf + .png
  Multi@72: G = 0.800
  Multi@200: G = 0.917
  Single@200: G = 0.559
  Single@631: G = 0.800
  IRT@116 (single): G = 0.424
  Ratio: 8.8x

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T17:52:41.464744+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/fig3_dstudy_curves.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/fig3_dstudy_curves.png"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T17:52:41.465283+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T17:52:41.465512+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T17:52:41.465678+00:00_

1	#!/usr/bin/env python3
2	"""Figure 3: D-Study Projection Curves — G coefficient vs. number of benchmark items."""
3	
4	import matplotlib
5	matplotlib.use('Agg')
6	import matplotlib.pyplot as plt
7	import matplotlib.patheffects as pe
8	import numpy as np
9	import os
10	
11	plt.rcParams.update({
12	    'font.family': 'serif',
13	    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],
14	    'font.size': 9,
15	    'axes.labelsize': 9,
16	    'xtick.labelsize': 8,
17	    'ytick.labelsize': 8,
18	    'legend.fontsize': 7.5,
19	    'figure.dpi': 300,
20	    'savefig.dpi': 300,
21	    'savefig.bbox': 'tight',
22	    'savefig.pad_inches': 0.08,
23	    'axes.spines.top': False,
24	    'axes.spines.right': False,
25	})
26	
27	BLUE = '#2166ac'
28	RED  = '#e41a1c'
29	GRAY = '#666666'
30	
31	# ---------------------------------------------------------------------------
32	# D-study G coefficient: G(n) = n / (n + C), where C = sigma_delta / sigma_p
33	#
34	# Variance components from exp-001 cross-model G-study (Henderson I):
35	#   item_id (sigma_p): 42.1%  |  model:item 33.6%  |  residual 19.5%
36	#   prompt:item 2.8%  |  seed:item 2.5%  |  precision:item 2.0%
37	#   temperature:item 1.0%  |  ordering:item 0.6%
38	#
39	# Multi-facet design: n_model=4, n_prompt=6, n_seed=6, n_temp=3, n_ord=4, n_prec=3
40	# C values derived from full G-study (all interaction terms including higher-order):
41	# ---------------------------------------------------------------------------
42	C_MULTI  = 18.0    # multi-facet (432 conditions/item)
43	C_SINGLE = 157.75  # single-condition (1 condition/item)
44	
45	n = np.arange(1, 701)
46	G_m = n / (n + C_MULTI)
47	G_s = n / (n + C_SINGLE)
48	
49	N_M80 = 72
50	N_S80 = 631
51	N_IRT = 116
52	G_IRT = N_IRT / (N_IRT + C_SINGLE)
53	
54	stroke = [pe.withStroke(linewidth=2.5, foreground='white')]
55	
56	fig, ax = plt.subplots(figsize=(3.5, 2.8))
57	
58	# Shaded region below G = 0.80
59	ax.fill_between([0, 700], 0, 0.80, color='#f4f4f4', zorder=0)
60	
6
…[truncated 2918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T17:52:41.465844+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Figure 3: D-Study Projection Curves — G coefficient vs. number of benchmark items.\"\"\"\n\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nimport numpy as np\nimport os\n\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],\n    'font.size': 9,\n    'axes.labelsize': 9,\n    'xtick.labelsize': 8,\n    'ytick.labelsize': 8,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.08,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n})\n\nBLUE = '#2166ac'\nRED  = '#e41a1c'\nGRAY = '#666666'\n\n# ---------------------------------------------------------------------------\n# D-study G coefficient: G(n) = n / (n + C), where C = sigma_delta / sigma_p\n#\n# Variance components from exp-001 cross-model G-study (Henderson I):\n#   item_id (sigma_p): 42.1%  |  model:item 33.6%  |  residual 19.5%\n#   prompt:item 2.8%  |  seed:item 2.5%  |  precision:item 2.0%\n#   temperature:item 1.0%  |  ordering:item 0.6%\n#\n# Multi-facet design: n_model=4, n_prompt=6, n_seed=6, n_temp=3, n_ord=4, n_prec=3\n# C values derived from full G-study (all interaction terms including higher-order):\n# ---------------------------------------------------------------------------\nC_MULTI  = 18.0    # multi-facet (432 conditions/item)\nC_SINGLE = 157.75  # single-condition (1 condition/item)\n\nn = np.arange(1, 701)\nG_m = n / (n + C_MULTI)\nG_s = n / (n + C_SINGLE)\n\nN_M80 = 72\nN_S80 = 631\nN_IRT = 116\nG_IRT = N_IRT / (N_IRT + C_SINGLE)\n\nstroke = [pe.withStroke(linewidth=2.5, foreground='white')]\n\nfig, ax = plt.subplots(figsize=(3.5, 2.8))\n\n# Shaded region below G = 0.80\nax.fill_between([0, 700], 0, 0.80, color='#f4f4f4', zorder=0)\n\n# Threshold line\nax.axhline(0.80, color=GRAY, ls='--', lw=1.0, alpha=0.7, zorder=2)\n\n# IRT vertical line\nax.axvline(N_IRT, color='#bbbbbb', ls=':', lw=0.8, zorder=1)\n\n# Curves\nax.plot(n, G_m, color=BLUE, lw=1.5, solid_capstyle='round', zorder=3)\nax.plot(n, G_s, color=RED, lw=1.5, ls='--', zorder=3)\n\n# Intersection dots\nfor nx, c in [(N_M80, BLUE), (N_S80, RED)]:\n    ax.plot(nx, 0.80, 'o', color=c, ms=4, zorder=5, mec='white', mew=0.6)\n\n# IRT diamond\nax.plot(N_IRT, G_IRT, 'D', color='#888888', ms=3.5, zorder=5)\n\n# --- Direct curve labels (no legend) ---\nt = ax.text(320, 0.965, 'Multi-facet', fontsize=7, color=BLUE,\n            ha='center', va='bottom', fontstyle='italic')\nt.set_path_effects(stroke)\n\nt = ax.text(480, 0.665, 'Single-condition', fontsize=7, color=RED,\n            ha='center', va='top', fontstyle='italic')\nt.set_path_effects(stroke)\n\n# --- Annotations ---\n\nt = ax.annotate('72 items', xy=(72, 0.80), xytext=(170, 0.63),\n                fontsize=7, color=BLUE, fontweight='bold',\n                arrowprops=dict(arrowstyle='->', color=BLUE, lw=0.8),\n                ha='left', zorder=6)\nt.set_path_effects(stroke)\n\nt = ax.annotate('631 items', xy=(631, 0.80), xytext=(500, 0.92),\n                fontsize=7, color=RED, fontweight='bold',\n                arrowprops=dict(arrowstyle='->', color=RED, lw=0.8),\n                ha='right', zorder=6)\nt.set_path_effects(stroke)\n\nt = ax.annotate(f'IRT rec. → G = {G_IRT:.2f}',\n                xy=(N_IRT, G_IRT), xytext=(240, 0.33),\n                fontsize=6.5, color='#777777',\n                arrowprops=dict(arrowstyle='->', color='#aaaaaa', lw=0.7),\n                zorder=6)\nt.set_path_effects(stroke)\n\nt = ax.text(460, 0.82, 'Reliability threshold (G = 0.80)',\n            fontsize=6.5, color=GRAY, ha='center', va='bottom',\n            bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))\n\nax.text(350, 0.06, 'Below reliability threshold',\n        fontsize=6.5, color='#cccccc', ha='center', fontstyle='italic')\n\n# --- Axes ---\nax.set_xlim(0, 700)\nax.set_ylim(0, 1.0)\nax.set_xlabel('Number of items')\nax.set_ylabel('Generalizability coefficient (G)')\nax.set_xticks([0, 100, 200, 300, 400, 500, 600, 700])\nax.set_yticks(np.arange(0, 1.1, 0.2))\n\nax.yaxis.grid(True, alpha=0.12, lw=0.4)\n\nplt.tight_layout()\n\n# --- Save ---\noutdir = os.path.dirname(os.path.abspath(__file__))\nfor ext in ('pdf', 'png'):\n    fig.savefig(os.path.join(outdir, f'fig3_dstudy_curves.{ext}'))\nplt.close()\n\n# Verification\nprint('Saved fig3_dstudy_curves.pdf + .png')\nfor label, ni, C in [('Multi@72', 72, C_MULTI), ('Multi@200', 200, C_MULTI),\n                      ('Single@200', 200, C_SINGLE), ('Single@631', 631, C_SINGLE)]:\n    print(f'  {label}: G = {ni/(ni+C):.3f}')\nprint(f'  IRT@116 (single): G = {G_IRT:.3f}')\nprint(f'  Ratio: {N_S80/N_M80:.1f}x')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Figure 3: D-Study Projection Curves — G coefficient vs. number of benchmark items.\"\"\"\n\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nimport numpy as np\nimport os\n\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],\n    'font.size': 9,\n    'axes.labelsize': 9,\n    'xtick.labelsize': 8,\n    'ytick.labelsize': 8,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.08,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n})\n\nBLUE = '#2166ac'\nRED  = '#e41a1c'\nGRAY = '#666666'\n\n# ---------------------------------------------------------------------------\n# D-study G coefficient: G(n) = n / (n + C), where C = sigma_delta / sigma_p\n#\n# Variance components from exp-001 cross-model G-study (Henderson I):\n#   item_id (sigma_p): 42.1%  |  model:item 33.6%  |  residual 19.5%\n#   prompt:item 2.8%  |  seed:item 2.5%  |  precision:item 2.0%\n#   temperature:item 1.0%  |  ordering:item 0.6%\n#\n# Multi-facet design: n_model=4, n_prompt=6, n_seed=6, n_temp=3, n_ord=4, n_prec=3\n# C values derived from full G-study (all interaction terms including higher-order):\n# ---------------------------------------------------------------------------\nC_MULTI  = 18.0    # multi-facet (432 conditions/item)\nC_SINGLE = 157.75  # single-condition (1 condition/item)\n\nn = np.arange(1, 701)\nG_m = n / (n + C_MULTI)\nG_s = n / (n + C_SINGLE)\n\nN_M80 = 72\nN_S80 = 631\nN_IRT = 116\nG_IRT = N_IRT / (N_IRT + C_SINGLE)\n\nstroke = [pe.withStroke(linewidth=2.5, foreground='white')]\n\nfig, ax = plt.subplots(figsize=(3.5, 2.8))\n\n# Shaded region below G = 0.80\nax.fill_between([0, 700], 0, 0.80, color='#f4f4f4', zorder=0)\n\n# Threshold line\nax.axhline(0.80, color=GRAY, ls='--', lw=1.0, alpha=0.7, zorder=2)\n\n# IRT vertical line\nax.axvline(N_IRT, color='#bbbbbb', ls=':', lw=0.8, zorder=1)\n\n# Curves\nax.plot(n, G_m, color=BLUE, lw=1.5, solid_capstyle='round', zorder=3)\nax.plot(n, G_s, color=RED, lw=1.5, ls='--', zorder=3)\n\n# Intersection dots\nfor nx, c in [(N_M80, BLUE), (N_S80, RED)]:\n    ax.plot(nx, 0.80, 'o', color=c, ms=4, zorder=5, mec='white', mew=0.6)\n\n# IRT diamond\nax.plot(N_IRT, G_IRT, 'D', color='#888888', ms=3.5, zorder=5)\n\n# --- Direct curve labels (no legend) ---\nt = ax.text(320, 0.965, 'Multi-facet', fontsize=7, color=BLUE,\n            ha='center', va='bottom', fontstyle='italic')\nt.set_path_effects(stroke)\n\nt = ax.text(480, 0.665, 'Single-condition', fontsize=7, color=RED,\n            ha='center', va='top', fontstyle='italic')\nt.set_path_effects(stroke)\n\n# --- Annotations ---\n\nt = ax.annotate('72 items', xy=(72, 0.80), xytext=(170, 0.63),\n                fontsize=7, color=BLUE, fontweight='bold',\n                arrowprops=dict(arrowstyle='->', color=BLUE, lw=0.8),\n                ha='left', zorder=6)\nt.set_path_effects(stroke)\n\nt = ax.annotate('631 items', xy=(631, 0.80), xytext=(500, 0.92),\n                fontsize=7, color=RED, fontweight='bold',\n                arrowprops=dict(arrowstyle='->', color=RED, lw=0.8),\n                ha='right', zorder=6)\nt.set_path_effects(stroke)\n\nt = ax.annotate(f'IRT rec. → G = {G_IRT:.2f}',\n                xy=(N_IRT, G_IRT), xytext=(240, 0.33),\n                fontsize=6.5, color='#777777',\n                arrowprops=dict(arrowstyle='->', color='#aaaaaa', lw=0.7),\n                zorder=6)\nt.set_path_effects(stroke)\n\nt = ax.text(460, 0.82, 'Reliability threshold (G = 0.80)',\n            fontsize=6.5, color=GRAY, ha='center', va='bottom',\n            bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))\n\nax.text(350, 0.06, 'Below reliability threshold',\n        fontsize=6.5, color='#cccccc', ha='center', fontstyle='italic')\n\n# --- Axes ---\nax.set_xlim(0, 700)\nax.set_ylim(0, 1.0)\nax.set_xlabel('Number of items')\nax.set_ylabel('Generalizability coefficient (G)')\nax.set_xticks([0, 100, 200, 300, 400, 500, 600, 700])\nax.set_yticks(np.arange(0, 1.1, 0.2))\n\nax.yaxis.grid(True, alpha=0.12, lw=0.4)\n\nplt.tight_layout()\n\n# --- Save ---\noutdir = os.path.dirname(os.path.abspath(__file__))\nfor ext in ('pdf', 'png'):\n    fig.savefig(os.path.join(outdir, f'fig3_dstudy_curves.{ext}'))\nplt.close()\n\n# Verification\nprint('Saved fig3_dstudy_curves.pdf + .png')\nfor label, ni, C in [('Multi@72', 72, C_MULTI), ('Multi@200', 200, C_MULTI),\n                      ('Single@200', 200, C_SINGLE), ('Single@631', 631, C_SINGLE)]:\n    print(f'  {label}: G = {ni/(ni+C):.3f}')\nprint(f'  IRT@116 (single): G = {G_IRT:.3f}')\nprint(f'  Ratio: {N_S80/N_M80:.1f}x')\n"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T17:52:41.466060+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T17:52:41.466189+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "/home/ubuntu/agent-ml-research/.venv/bin/python /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py",
  "description": "Regenerate with direct curve labels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Bash",
  "tool_args": {
    "command": "/home/ubuntu/agent-ml-research/.venv/bin/python /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/gen_fig3_dstudy_curves.py",
    "description": "Regenerate with direct curve labels"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T17:52:41.466306+00:00_

Saved fig3_dstudy_curves.pdf + .png
  Multi@72: G = 0.800
  Multi@200: G = 0.917
  Single@200: G = 0.559
  Single@631: G = 0.800
  IRT@116 (single): G = 0.424
  Ratio: 8.8x

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T17:52:41.466464+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/fig3_dstudy_curves.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/fig3_dstudy_curves.png"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T17:52:41.467026+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T17:52:41.467182+00:00_

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
  "session": "worker_paper_figure_20260521T173555",
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

_source line 40 · 2026-05-21T17:52:41.467300+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T17:52:41.467446+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "fig3_dstudy_curves",
  "type": "chart",
  "description": "Figure 3: D-Study Projection Curves — Multi-facet vs single-condition G coefficient as a function of benchmark size. Shows 8.8× efficiency gap (72 vs 631 items to reach G≥0.80) and IRT's 116-item recommendation yielding only G=0.42 under typical practice.",
  "project": "nlp_variance_gtheory",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/fig3_dstudy_curves.pdf",
  "tags": "['paper', 'figure', 'd-study', 'g-theory', 'reliability']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "fig3_dstudy_curves",
    "type": "chart",
    "description": "Figure 3: D-Study Projection Curves — Multi-facet vs single-condition G coefficient as a function of benchmark size. Shows 8.8× efficiency gap (72 vs 631 items to reach G≥0.80) and IRT's 116-item recommendation yielding only G=0.42 under typical practice.",
    "project": "nlp_variance_gtheory",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/figures/paper/fig3_dstudy_curves.pdf",
    "tags": "['paper', 'figure', 'd-study', 'g-theory', 'reliability']"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T17:52:41.467608+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260521_730dfa\", \"name\": \"fig3_dstudy_curves\", \"type\": \"chart\", \"description\": \"Figure 3: D-Study Projection Curves — Multi-facet vs single-condition G coefficient as a function of benchmark size. Shows 8.8× efficiency gap (72 vs 631 items to reach G≥0.80) and IRT's 116-item recommendation yielding only G=0.42 under typical practice.\", \"path\": \"projects/nlp_variance_gtheory/artifacts/_project/chart/fig3_dstudy_curves.pdf\", \"url\": null, \"project\": \"nlp_variance_gtheory\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-21T17:52:35.059423+00:00\", \"tags\": [\"paper\", \"figure\", \"d-study\", \"g-theory\", \"reliability\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_20260521T173555",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-21T17:52:41.467768+00:00_

Figure 3 已生成并注册。

**产出文件：**
- PDF: `figures/paper/fig3_dstudy_curves.pdf`
- PNG: `figures/paper/fig3_dstudy_curves.png`
- 脚本: `figures/paper/gen_fig3_dstudy_curves.py`

**验证点全部通过：**
| 设计点 | 计算值 | 预期值 |
|--------|--------|--------|
| Multi-facet @ 72 items | 0.800 | 0.800 |
| Multi-facet @ 200 items | 0.917 | 0.918 |
| Single-cond @ 200 items | 0.559 | 0.559 |
| Single-cond @ 631 items | 0.800 | 0.800 |
| IRT rec @ 116 items | 0.424 | ~0.424 |
| Ratio | 8.8× | ~8.8× |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_figure_20260521T173555"
}
```

</details>

---
