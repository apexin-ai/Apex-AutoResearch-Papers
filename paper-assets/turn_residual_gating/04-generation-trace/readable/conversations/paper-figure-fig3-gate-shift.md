# paper figure fig3 gate shift

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 0
- **Tool calls:** 30
- **Original source:** `logs/chats/worker_paper_figure_fig3_gate_shift_20260519T202802.jsonl`
- **Structured JSON:** [`45bb5e6148ef20dd2f97.json`](../../sessions/45/45bb5e6148ef20dd2f97.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

61 recorded events

### Tool call

_source line 1 · 2026-05-19T20:35:15.392511+00:00_

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
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T20:35:15.393189+00:00_

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
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T20:35:15.393389+00:00_

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
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-visualization.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T20:35:15.393859+00:00_

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
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T20:35:15.394046+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__list_artifacts",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__list_artifacts",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T20:35:15.394185+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T20:35:15.394330+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "turn_residual_gating",
  "filters": "{'exp_id': 'phase2_tg_s42_v7'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "turn_residual_gating",
    "filters": "{'exp_id': 'phase2_tg_s42_v7'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T20:35:15.394480+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.075}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T20:35:15.394608+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "ssh execute read_only",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "ssh execute read_only",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T20:35:15.394725+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T20:35:15.394859+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "turn_residual_gating",
  "limit": "20",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "turn_residual_gating",
    "limit": "20",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T20:35:15.395521+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"phase2_tg_s42_v9_pcgrad\": {\"status\": \"RUNNING\", \"retry_count\": 2, \"created_at\": \"2026-05-19T16:13:21.907Z\", \"updated_at\": \"2026-05-19T19:45:00.000Z\", \"hypothesis\": \"PCGrad (Yu et al. NeurIPS 2020) 消除 NTP-GAR 梯度方向冲突后（仅对 gate 参数投影 NTP 梯度到 GAR 梯度正交平面），如果 30x training-inference GAR gap 仍在 → 因果证据证明 exposure bias（非梯度竞争）是 gap 根因。与 v7 对比：相同超参（lambda_gar=1.0, MSE+gate_div），唯一变量是梯度处理方式。成功标准：(1) 梯度 cos_sim 显著改善（从 v7 的 -0.089 提升到 ≥0），(2) 但推理 GAR 仍 ≈ v7 水平（0.016），证明梯度冲突不是 gap 的因。\", \"parent\": \"phase2_tg_s42_v7\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/turn_residual_gating && PYTHONUNBUFFERED=1 python src/train_phase2_v9_pcgrad.py --model /root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir data/ultrachat_8k --output-dir checkpoints/tg_v9_pcgrad_s42 --gate-type threadgate --gar-loss-mode mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 --grad-accum 8 --seed 42\\\"\", \"server\": \"westd-20861\", \"gpu\": [\"cuda:0\"], \"pid\": \"83860\", \"log_path\": \"~/runs/turn_residual_gating/phase2_tg_s42_v9_pcgrad.log\", \"submitted_at\": \"2026-05-19T17:42:10.820Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"reproduce\": {\"finished_at\": \"2026-05-19T17:35:37.703Z\"}, \"failure_reason\": null, \"conclusion\": null, \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T17:35:39.776243+00:00\", \"note\": \"第1次提交 EXIT_CODE=2 残留事件\"}]}, \"completed_at\": null, \"notes\": \"第3次提交 (PID 83860, westd-20861:cuda:0)。前两次失败：#1 EXIT_CODE=2 (--pcgrad flag 不存在), #2 EXIT_CODE=143 (服务器重启 SIGTERM at step 100)。第3次运行正常，Epoch 0 step 6150/24000 micro-steps (25.6%)。超参与 v7 一致。训练端发现：L_GAR 在 step 0-350 有高原期 (0.22-0.23)，之后缓慢下降，step 5000+ 坍塌到≈0（同 v7 终态）。PCG
…[truncated 31804 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T20:35:15.395724+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "ssh",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "ssh",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T20:35:15.395861+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T20:35:15.396101+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"import matplotlib; print(matplotlib.__version__)\" 2>&1 && ls -d /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/ 2>&1 || echo \"DIR_MISSING\"",
  "description": "Check matplotlib and output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"import matplotlib; print(matplotlib.__version__)\" 2>&1 && ls -d /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/ 2>&1 || echo \"DIR_MISSING\"",
    "description": "Check matplotlib and output directory"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T20:35:15.396234+00:00_

3.10.9
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T20:35:15.396399+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
  "content": "\"\"\"Generate Figure 3: Gate Turn Conditioning + Distribution Shift (2-panel).\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nimport numpy as np\nimport os\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 9,\n    'axes.titlesize': 10,\n    'axes.labelsize': 9,\n    'xtick.labelsize': 8,\n    'ytick.labelsize': 8,\n    'legend.fontsize': 7.5,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n    'lines.linewidth': 1.5,\n})\n\nC_EARLY = '#0072B2'   # blue — early turn / active gate\nC_LATE  = '#D55E00'   # vermillion — late turn / passive gate\nC_IID   = '#009E73'   # green — IID eval\nC_MG    = '#D55E00'   # vermillion — model-generated\n\nfig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(7, 3.5),\n                                  gridspec_kw={'width_ratios': [1, 1.2],\n                                               'wspace': 0.38})\n\n# ======================================================================\n# Panel (a): Gate Turn Conditioning — Cleveland dot plot (top-5 layers)\n# Data: phase2_tg_s42_v7 registry → eval_gate_dynamic_range_top5\n# Sorted by |diff| ascending (smallest gap at bottom, largest at top)\n# ======================================================================\nlayers = ['L9', 'L20', 'L12', 'L14', 'L23']\nturn1  = [0.8578, 0.8228, 0.8200, 0.7473, 0.7693]\nturn21 = [0.9679, 0.9393, 0.9465, 0.9276, 0.9793]\ndiffs  = [-0.1101, -0.1165, -0.1265, -0.1803, -0.2100]\n\ny = np.arange(len(layers))\n\n# Connecting lines\nfor i in range(len(layers)):\n    ax_a.plot([turn1[i], turn21[i]], [y[i], y[i]],\n             color='#cccccc', linewidth=1.8, zorder=1, solid_capstyle='round')\n\n# Dots\nax_a.scatter(turn1, y, color=C_EARLY, s=48, zorder=3,\n            edgecolors='white', linewidths=0.6, label='Turn 1 (early)')\nax_a.scatter(turn21, y, color=C_LATE, s=48, zorder=3,\n            edgecolors='white', linewidths=0.6, label='Turn 21 (late)')\n\n# Diff annotations (right side)\nfor i, d in enumerate(diffs):\n    ax_a.text(1.015, y[i], f'{d:+.2f}', fontsize=6.5, va='center',\n             color='#555555', family='monospace')\n\nax_a.set_yticks(y)\nax_a.set_yticklabels(layers)\nax_a.set_xlim(0.70, 1.01)\nax_a.set_xlabel('Gate value')\nax_a.set_title('(a) Gates become passive at late turns',\n               fontsize=9, fontweight='bold', pad=8, loc='left')\nax_a.legend(loc='lower right', fontsize=7, framealpha=0.9,\n           handletextpad=0.3, borderpad=0.4, edgecolor='#cccccc')\n\n# Stats box\nstats_text = ('27/28 layers: gate ↑ at late turns\\n'\n              'Wilcoxon p = 3.73×10⁻⁸\\n'\n              'Effect size r = 0.975')\nax_a.text(0.04, 0.97, stats_text, transform=ax_a.transAxes,\n          fontsize=6.5, va='top', color='#555555',\n          bbox=dict(boxstyle='round,pad=0.3', fc='#f8f8f8',\n                    ec='#cccccc', alpha=0.9, lw=0.6))\n\n# Footnote\nax_a.text(0.04, 0.02, 'Top-5 most differentiated layers shown',\n          transform=ax_a.transAxes, fontsize=6, color='#aaaaaa', va='bottom')\n\n# Direction arrow under x-axis\nax_a.annotate('more passive', xy=(1.00, -0.8), fontsize=6.5, color='#999999',\n             ha='right', va='top', annotation_clip=False,\n             xycoords=('data', 'data'))\nax_a.annotate('', xy=(1.00, -0.65), xytext=(0.85, -0.65),\n             arrowprops=dict(arrowstyle='->', color='#bbbbbb', lw=1.0),\n             annotation_clip=False)\n\n# ======================================================================\n# Panel (b): Distribution Shift — Grouped bar chart (log scale)\n# IID data: phase2_4way_eval registry\n# Model-gen data: phase2_tg_s42_v7 eval metrics (TG + Base only)\n# ======================================================================\nmodels = ['Base', 'TG', 'UG', 'LoRA-only']\niid    = [0.0107, 0.4866, 0.4923, 0.486]\nmg     = [0.0122, 0.0157, None, None]\n\nx = np.arange(len(models))\nw = 0.30\n\n# IID bars\nbars_iid = ax_b.bar(x - w/2, iid, w, color=C_IID, label='IID eval',\n                     zorder=2, alpha=0.88, edgecolor='white', linewidth=0.5)\n\n# Model-gen bars (only where data exists)\nfor i in range(len(models)):\n    if mg[i] is not None:\n        lbl = 'Model-generated' if i == 0 else ''\n        ax_b.bar(i + w/2, mg[i], w, color=C_MG, zorder=2, alpha=0.88,\n                label=lbl, edgecolor='white', linewidth=0.5)\n    else:\n        ax_b.text(i + w/2, 0.0065, 'n/a', ha='center', va='bottom',\n                 fontsize=5.5, color='#bbbbbb', fontstyle='italic')\n\nax_b.set_yscale('log')\nax_b.set_ylim(0.005, 1.0)\nax_b.set_xticks(x)\nax_b.set_xticklabels(models, fontsize=8)\nax_b.set_ylabel('GAR (ours)')\nax_b.set_title('(b) Exposure bias selectively disrupts GAR',\n               fontsize=9, fontweight='bold', pad=8, loc='left')\nax_b.legend(loc='upper left', fontsize=7, framealpha=0.9,\n           edgecolor='#cccccc', handletextpad=0.3, borderpad=0.4)\n\n# Value labels on bars\nfor i, v in enumerate(iid):\n    label = f'{v:.3f}' if v < 0.1 else f'{v:.2f}'\n    y_off = v * 1.25\n    ax_b.text(i - w/2, y_off, label, ha='center', va='bottom',\n             fontsize=6, color='#333333')\n\nfor i, v in enumerate(mg):\n    if v is not None:\n        ax_b.text(i + w/2, v * 1.25, f'{v:.4f}', ha='center', va='bottom',\n                 fontsize=6, color='#333333')\n\n# 30x gap annotation — double-headed arrow + bold label\ntg_x = 1 + w/2 + 0.22\nax_b.annotate('', xy=(tg_x, 0.0157), xytext=(tg_x, 0.4866),\n             arrowprops=dict(arrowstyle='<->', color=C_MG, lw=1.3,\n                            shrinkA=1, shrinkB=1))\ngeo_mean = np.sqrt(0.0157 * 0.4866)  # log-scale midpoint\nt30 = ax_b.text(tg_x + 0.12, geo_mean, '30×', fontsize=11,\n               fontweight='bold', color=C_MG, ha='left', va='center')\nt30.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])\n\n# Background bands to separate IID vs model-gen conceptual zones\nax_b.axhspan(0.005, 0.05, color='#FFF3E0', alpha=0.3, zorder=0)\nax_b.axhspan(0.05, 1.0, color='#E8F5E9', alpha=0.3, zorder=0)\nax_b.text(3.7, 0.015, 'model-gen\\nregime', fontsize=5.5, color='#BF360C',\n          ha='right', va='center', alpha=0.6, fontstyle='italic')\nax_b.text(3.7, 0.3, 'IID\\nregime', fontsize=5.5, color='#2E7D32',\n          ha='right', va='center', alpha=0.6, fontstyle='italic')\n\n# Minor gridlines for log scale readability\nax_b.yaxis.set_minor_locator(matplotlib.ticker.LogLocator(base=10, subs=np.arange(2, 10)))\nax_b.grid(axis='y', which='major', alpha=0.15, zorder=0)\nax_b.grid(axis='y', which='minor', alpha=0.06, zorder=0)\n\nplt.tight_layout()\n\nout_dir = os.path.dirname(os.path.abspath(__file__))\nplt.savefig(os.path.join(out_dir, 'fig3_gate_shift.pdf'))\nplt.savefig(os.path.join(out_dir, 'fig3_gate_shift.png'))\nplt.close()\nprint('Saved: fig3_gate_shift.pdf + .png')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
    "content": "\"\"\"Generate Figure 3: Gate Turn Conditioning + Distribution Shift (2-panel).\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nimport numpy as np\nimport os\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 9,\n    'axes.titlesize': 10,\n    'axes.labelsize': 9,\n    'xtick.labelsize': 8,\n    'ytick.labelsize': 8,\n    'legend.fontsize': 7.5,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n    'lines.linewidth': 1.5,\n})\n\nC_EARLY = '#0072B2'   # blue — early turn / active gate\nC_LATE  = '#D55E00'   # vermillion — late turn / passive gate\nC_IID   = '#009E73'   # green — IID eval\nC_MG    = '#D55E00'   # vermillion — model-generated\n\nfig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(7, 3.5),\n                                  gridspec_kw={'width_ratios': [1, 1.2],\n                                               'wspace': 0.38})\n\n# ======================================================================\n# Panel (a): Gate Turn Conditioning — Cleveland dot plot (top-5 layers)\n# Data: phase2_tg_s42_v7 registry → eval_gate_dynamic_range_top5\n# Sorted by |diff| ascending (smallest gap at bottom, largest at top)\n# ======================================================================\nlayers = ['L9', 'L20', 'L12', 'L14', 'L23']\nturn1  = [0.8578, 0.8228, 0.8200, 0.7473, 0.7693]\nturn21 = [0.9679, 0.9393, 0.9465, 0.9276, 0.9793]\ndiffs  = [-0.1101, -0.1165, -0.1265, -0.1803, -0.2100]\n\ny = np.arange(len(layers))\n\n# Connecting lines\nfor i in range(len(layers)):\n    ax_a.plot([turn1[i], turn21[i]], [y[i], y[i]],\n             color='#cccccc', linewidth=1.8, zorder=1, solid_capstyle='round')\n\n# Dots\nax_a.scatter(turn1, y, color=C_EARLY, s=48, zorder=3,\n            edgecolors='white', linewidths=0.6, label='Turn 1 (early)')\nax_a.scatter(turn21, y, color=C_LATE, s=48, zorder=3,\n            edgecolors='white', linewidths=0.6, label='Turn 21 (late)')\n\n# Diff annotations (right side)\nfor i, d in enumerate(diffs):\n    ax_a.text(1.015, y[i], f'{d:+.2f}', fontsize=6.5, va='center',\n             color='#555555', family='monospace')\n\nax_a.set_yticks(y)\nax_a.set_yticklabels(layers)\nax_a.set_xlim(0.70, 1.01)\nax_a.set_xlabel('Gate value')\nax_a.set_title('(a) Gates become passive at late turns',\n               fontsize=9, fontweight='bold', pad=8, loc='left')\nax_a.legend(loc='lower right', fontsize=7, framealpha=0.9,\n           handletextpad=0.3, borderpad=0.4, edgecolor='#cccccc')\n\n# Stats box\nstats_text = ('27/28 layers: gate ↑ at late turns\\n'\n              'Wilcoxon p = 3.73×10⁻⁸\\n'\n              'Effect size r = 0.975')\nax_a.text(0.04, 0.97, stats_text, transform=ax_a.transAxes,\n          fontsize=6.5, va='top', color='#555555',\n          bbox=dict(boxstyle='round,pad=0.3', fc='#f8f8f8',\n                    ec='#cccccc', alpha=0.9, lw=0.6))\n\n# Footnote\nax_a.text(0.04, 0.02, 'Top-5 most differentiated layers shown',\n          transform=ax_a.transAxes, fontsize=6, color='#aaaaaa', va='bottom')\n\n# Direction arrow under x-axis\nax_a.annotate('more passive', xy=(1.00, -0.8), fontsize=6.5, color='#999999',\n             ha='right', va='top', annotation_clip=False,\n             xycoords=('data', 'data'))\nax_a.annotate('', xy=(1.00, -0.65), xytext=(0.85, -0.65),\n             arrowprops=dict(arrowstyle='->', color='#bbbbbb', lw=1.0),\n             annotation_clip=False)\n\n# ======================================================================\n# Panel (b): Distribution Shift — Grouped bar chart (log scale)\n# IID data: phase2_4way_eval registry\n# Model-gen data: phase2_tg_s42_v7 eval metrics (TG + Base only)\n# ======================================================================\nmodels = ['Base', 'TG', 'UG', 'LoRA-only']\niid    = [0.0107, 0.4866, 0.4923, 0.486]\nmg     = [0.0122, 0.0157, None, None]\n\nx = np.arange(len(models))\nw = 0.30\n\n# IID bars\nbars_iid = ax_b.bar(x - w/2, iid, w, color=C_IID, label='IID eval',\n                     zorder=2, alpha=0.88, edgecolor='white', linewidth=0.5)\n\n# Model-gen bars (only where data exists)\nfor i in range(len(models)):\n    if mg[i] is not None:\n        lbl = 'Model-generated' if i == 0 else ''\n        ax_b.bar(i + w/2, mg[i], w, color=C_MG, zorder=2, alpha=0.88,\n                label=lbl, edgecolor='white', linewidth=0.5)\n    else:\n        ax_b.text(i + w/2, 0.0065, 'n/a', ha='center', va='bottom',\n                 fontsize=5.5, color='#bbbbbb', fontstyle='italic')\n\nax_b.set_yscale('log')\nax_b.set_ylim(0.005, 1.0)\nax_b.set_xticks(x)\nax_b.set_xticklabels(models, fontsize=8)\nax_b.set_ylabel('GAR (ours)')\nax_b.set_title('(b) Exposure bias selectively disrupts GAR',\n               fontsize=9, fontweight='bold', pad=8, loc='left')\nax_b.legend(loc='upper left', fontsize=7, framealpha=0.9,\n           edgecolor='#cccccc', handletextpad=0.3, borderpad=0.4)\n\n# Value labels on bars\nfor i, v in enumerate(iid):\n    label = f'{v:.3f}' if v < 0.1 else f'{v:.2f}'\n    y_off = v * 1.25\n    ax_b.text(i - w/2, y_off, label, ha='center', va='bottom',\n             fontsize=6, color='#333333')\n\nfor i, v in enumerate(mg):\n    if v is not None:\n        ax_b.text(i + w/2, v * 1.25, f'{v:.4f}', ha='center', va='bottom',\n                 fontsize=6, color='#333333')\n\n# 30x gap annotation — double-headed arrow + bold label\ntg_x = 1 + w/2 + 0.22\nax_b.annotate('', xy=(tg_x, 0.0157), xytext=(tg_x, 0.4866),\n             arrowprops=dict(arrowstyle='<->', color=C_MG, lw=1.3,\n                            shrinkA=1, shrinkB=1))\ngeo_mean = np.sqrt(0.0157 * 0.4866)  # log-scale midpoint\nt30 = ax_b.text(tg_x + 0.12, geo_mean, '30×', fontsize=11,\n               fontweight='bold', color=C_MG, ha='left', va='center')\nt30.set_path_effects([pe.withStroke(linewidth=2.5, foreground='white')])\n\n# Background bands to separate IID vs model-gen conceptual zones\nax_b.axhspan(0.005, 0.05, color='#FFF3E0', alpha=0.3, zorder=0)\nax_b.axhspan(0.05, 1.0, color='#E8F5E9', alpha=0.3, zorder=0)\nax_b.text(3.7, 0.015, 'model-gen\\nregime', fontsize=5.5, color='#BF360C',\n          ha='right', va='center', alpha=0.6, fontstyle='italic')\nax_b.text(3.7, 0.3, 'IID\\nregime', fontsize=5.5, color='#2E7D32',\n          ha='right', va='center', alpha=0.6, fontstyle='italic')\n\n# Minor gridlines for log scale readability\nax_b.yaxis.set_minor_locator(matplotlib.ticker.LogLocator(base=10, subs=np.arange(2, 10)))\nax_b.grid(axis='y', which='major', alpha=0.15, zorder=0)\nax_b.grid(axis='y', which='minor', alpha=0.06, zorder=0)\n\nplt.tight_layout()\n\nout_dir = os.path.dirname(os.path.abspath(__file__))\nplt.savefig(os.path.join(out_dir, 'fig3_gate_shift.pdf'))\nplt.savefig(os.path.join(out_dir, 'fig3_gate_shift.png'))\nplt.close()\nprint('Saved: fig3_gate_shift.pdf + .png')\n"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T20:35:15.396661+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T20:35:15.396792+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper && python3 gen_fig3_gate_shift.py 2>&1",
  "description": "Generate figure 3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper && python3 gen_fig3_gate_shift.py 2>&1",
    "description": "Generate figure 3"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T20:35:15.396912+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py:166: UserWarning: This figure includes Axes that are not compatible with tight_layout, so results might be incorrect.
  plt.tight_layout()
Saved: fig3_gate_shift.pdf + .png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T20:35:15.397028+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig3_gate_shift.{pdf,png}",
  "description": "Verify output files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig3_gate_shift.{pdf,png}",
    "description": "Verify output files"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T20:35:15.397140+00:00_

-rw-r--r-- 1 ubuntu ubuntu  39532 May 19 20:32 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig3_gate_shift.pdf
-rw-r--r-- 1 ubuntu ubuntu 159086 May 19 20:32 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig3_gate_shift.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T20:35:15.397263+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig3_gate_shift.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig3_gate_shift.png"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T20:35:15.397642+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T20:35:15.397830+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
  "old_string": "fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(7, 3.5),\n                                  gridspec_kw={'width_ratios': [1, 1.2],\n                                               'wspace': 0.38})",
  "new_string": "fig = plt.figure(figsize=(7, 3.5), constrained_layout=True)\ngs = fig.add_gridspec(1, 2, width_ratios=[1, 1.2], wspace=0.08)\nax_a = fig.add_subplot(gs[0])\nax_b = fig.add_subplot(gs[1])"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
    "old_string": "fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(7, 3.5),\n                                  gridspec_kw={'width_ratios': [1, 1.2],\n                                               'wspace': 0.38})",
    "new_string": "fig = plt.figure(figsize=(7, 3.5), constrained_layout=True)\ngs = fig.add_gridspec(1, 2, width_ratios=[1, 1.2], wspace=0.08)\nax_a = fig.add_subplot(gs[0])\nax_b = fig.add_subplot(gs[1])"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T20:35:15.398002+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T20:35:15.398130+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
  "old_string": "plt.tight_layout()\n\nout_dir = os.path.dirname(os.path.abspath(__file__))",
  "new_string": "out_dir = os.path.dirname(os.path.abspath(__file__))"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
    "old_string": "plt.tight_layout()\n\nout_dir = os.path.dirname(os.path.abspath(__file__))",
    "new_string": "out_dir = os.path.dirname(os.path.abspath(__file__))"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T20:35:15.398302+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-19T20:35:15.398443+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 gen_fig3_gate_shift.py 2>&1",
  "description": "Regenerate figure with constrained_layout"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 gen_fig3_gate_shift.py 2>&1",
    "description": "Regenerate figure with constrained_layout"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T20:35:15.398566+00:00_

Saved: fig3_gate_shift.pdf + .png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T20:35:15.398676+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig3_gate_shift.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig3_gate_shift.png"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T20:35:15.399034+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T20:35:15.399196+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T20:35:15.399395+00:00_

1	"""Generate Figure 3: Gate Turn Conditioning + Distribution Shift (2-panel)."""
2	import matplotlib
3	matplotlib.use('Agg')
4	import matplotlib.pyplot as plt
5	import matplotlib.patheffects as pe
6	import numpy as np
7	import os
8	
9	plt.rcParams.update({
10	    'font.family': 'DejaVu Sans',
11	    'font.size': 9,
12	    'axes.titlesize': 10,
13	    'axes.labelsize': 9,
14	    'xtick.labelsize': 8,
15	    'ytick.labelsize': 8,
16	    'legend.fontsize': 7.5,
17	    'figure.dpi': 300,
18	    'savefig.dpi': 300,
19	    'savefig.bbox': 'tight',
20	    'savefig.pad_inches': 0.05,
21	    'axes.spines.top': False,
22	    'axes.spines.right': False,
23	    'pdf.fonttype': 42,
24	    'ps.fonttype': 42,
25	    'lines.linewidth': 1.5,
26	})
27	
28	C_EARLY = '#0072B2'   # blue — early turn / active gate
29	C_LATE  = '#D55E00'   # vermillion — late turn / passive gate
30	C_IID   = '#009E73'   # green — IID eval
31	C_MG    = '#D55E00'   # vermillion — model-generated
32	
33	fig = plt.figure(figsize=(7, 3.5), constrained_layout=True)
34	gs = fig.add_gridspec(1, 2, width_ratios=[1, 1.2], wspace=0.08)
35	ax_a = fig.add_subplot(gs[0])
36	ax_b = fig.add_subplot(gs[1])
37	
38	# ======================================================================
39	# Panel (a): Gate Turn Conditioning — Cleveland dot plot (top-5 layers)
40	# Data: phase2_tg_s42_v7 registry → eval_gate_dynamic_range_top5
41	# Sorted by |diff| ascending (smallest gap at bottom, largest at top)
42	# ======================================================================
43	layers = ['L9', 'L20', 'L12', 'L14', 'L23']
44	turn1  = [0.8578, 0.8228, 0.8200, 0.7473, 0.7693]
45	turn21 = [0.9679, 0.9393, 0.9465, 0.9276, 0.9793]
46	diffs  = [-0.1101, -0.1165, -0.1265, -0.1803, -0.2100]
47	
48	y = np.arange(len(layers))
49	
50	# Connecting lines
51	for i in range(len(layers)):
52	    ax_a.plot([turn1[i], turn21[i]], [y[i], y[i]],
53	             color='#cccccc', linewidth=1.8, zorder=1, solid_capstyle='round')
54	
55	# Dots
56	ax
…[truncated 5402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T20:35:15.399594+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
  "old_string": "# Stats box\nstats_text = ('27/28 layers: gate ↑ at late turns\\n'\n              'Wilcoxon p = 3.73×10⁻⁸\\n'\n              'Effect size r = 0.975')\nax_a.text(0.04, 0.97, stats_text, transform=ax_a.transAxes,\n          fontsize=6.5, va='top', color='#555555',\n          bbox=dict(boxstyle='round,pad=0.3', fc='#f8f8f8',\n                    ec='#cccccc', alpha=0.9, lw=0.6))\n\n# Footnote\nax_a.text(0.04, 0.02, 'Top-5 most differentiated layers shown',\n          transform=ax_a.transAxes, fontsize=6, color='#aaaaaa', va='bottom')",
  "new_string": "# Stats box (includes footnote to avoid legend overlap)\nstats_text = ('27/28 layers: gate ↑ at late turns\\n'\n              'Wilcoxon p = 3.73×10⁻⁸, r = 0.975\\n'\n              'Top-5 most differentiated layers shown')\nax_a.text(0.04, 0.97, stats_text, transform=ax_a.transAxes,\n          fontsize=6.5, va='top', color='#555555',\n          bbox=dict(boxstyle='round,pad=0.3', fc='#f8f8f8',\n                    ec='#cccccc', alpha=0.9, lw=0.6))"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
    "old_string": "# Stats box\nstats_text = ('27/28 layers: gate ↑ at late turns\\n'\n              'Wilcoxon p = 3.73×10⁻⁸\\n'\n              'Effect size r = 0.975')\nax_a.text(0.04, 0.97, stats_text, transform=ax_a.transAxes,\n          fontsize=6.5, va='top', color='#555555',\n          bbox=dict(boxstyle='round,pad=0.3', fc='#f8f8f8',\n                    ec='#cccccc', alpha=0.9, lw=0.6))\n\n# Footnote\nax_a.text(0.04, 0.02, 'Top-5 most differentiated layers shown',\n          transform=ax_a.transAxes, fontsize=6, color='#aaaaaa', va='bottom')",
    "new_string": "# Stats box (includes footnote to avoid legend overlap)\nstats_text = ('27/28 layers: gate ↑ at late turns\\n'\n              'Wilcoxon p = 3.73×10⁻⁸, r = 0.975\\n'\n              'Top-5 most differentiated layers shown')\nax_a.text(0.04, 0.97, stats_text, transform=ax_a.transAxes,\n          fontsize=6.5, va='top', color='#555555',\n          bbox=dict(boxstyle='round,pad=0.3', fc='#f8f8f8',\n                    ec='#cccccc', alpha=0.9, lw=0.6))"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T20:35:15.399793+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T20:35:15.399926+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 gen_fig3_gate_shift.py 2>&1",
  "description": "Regenerate figure with fix"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 gen_fig3_gate_shift.py 2>&1",
    "description": "Regenerate figure with fix"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T20:35:15.400043+00:00_

Saved: fig3_gate_shift.pdf + .png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T20:35:15.400154+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig3_gate_shift.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig3_gate_shift.png"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T20:35:15.400536+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T20:35:15.400706+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
  "old_string": "# Diff annotations (right side)\nfor i, d in enumerate(diffs):\n    ax_a.text(1.015, y[i], f'{d:+.2f}', fontsize=6.5, va='center',\n             color='#555555', family='monospace')",
  "new_string": "# Diff annotations (right side)\nfor i, d in enumerate(diffs):\n    ax_a.text(1.015, y[i], f'{d:+.2f}', fontsize=7, va='center',\n             color='#555555', family='monospace')"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
    "old_string": "# Diff annotations (right side)\nfor i, d in enumerate(diffs):\n    ax_a.text(1.015, y[i], f'{d:+.2f}', fontsize=6.5, va='center',\n             color='#555555', family='monospace')",
    "new_string": "# Diff annotations (right side)\nfor i, d in enumerate(diffs):\n    ax_a.text(1.015, y[i], f'{d:+.2f}', fontsize=7, va='center',\n             color='#555555', family='monospace')"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T20:35:15.400871+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T20:35:15.400993+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
  "old_string": "          fontsize=6.5, va='top', color='#555555',",
  "new_string": "          fontsize=7, va='top', color='#555555',"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
    "old_string": "          fontsize=6.5, va='top', color='#555555',",
    "new_string": "          fontsize=7, va='top', color='#555555',"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T20:35:15.401150+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T20:35:15.401275+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
  "old_string": "ax_a.annotate('more passive', xy=(1.00, -0.8), fontsize=6.5, color='#999999',",
  "new_string": "ax_a.annotate('more passive', xy=(1.00, -0.8), fontsize=7, color='#999999',"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
    "old_string": "ax_a.annotate('more passive', xy=(1.00, -0.8), fontsize=6.5, color='#999999',",
    "new_string": "ax_a.annotate('more passive', xy=(1.00, -0.8), fontsize=7, color='#999999',"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T20:35:15.401440+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T20:35:15.401569+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
  "old_string": "        ax_b.text(i + w/2, 0.0065, 'n/a', ha='center', va='bottom',\n                 fontsize=5.5, color='#bbbbbb', fontstyle='italic')",
  "new_string": "        ax_b.text(i + w/2, 0.0065, 'n/a', ha='center', va='bottom',\n                 fontsize=7, color='#bbbbbb', fontstyle='italic')"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
    "old_string": "        ax_b.text(i + w/2, 0.0065, 'n/a', ha='center', va='bottom',\n                 fontsize=5.5, color='#bbbbbb', fontstyle='italic')",
    "new_string": "        ax_b.text(i + w/2, 0.0065, 'n/a', ha='center', va='bottom',\n                 fontsize=7, color='#bbbbbb', fontstyle='italic')"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T20:35:15.401723+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T20:35:15.401844+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "True",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
  "old_string": "fontsize=5.5, color='#BF360C',",
  "new_string": "fontsize=7, color='#BF360C',"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "True",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
    "old_string": "fontsize=5.5, color='#BF360C',",
    "new_string": "fontsize=7, color='#BF360C',"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T20:35:15.401990+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py has been updated. All occurrences were successfully replaced.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T20:35:15.402109+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "True",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
  "old_string": "fontsize=5.5, color='#2E7D32',",
  "new_string": "fontsize=7, color='#2E7D32',"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "True",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
    "old_string": "fontsize=5.5, color='#2E7D32',",
    "new_string": "fontsize=7, color='#2E7D32',"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T20:35:15.402254+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py has been updated. All occurrences were successfully replaced.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T20:35:15.402383+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "True",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
  "old_string": "             fontsize=6, color='#333333')",
  "new_string": "             fontsize=7, color='#333333')"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "True",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py",
    "old_string": "             fontsize=6, color='#333333')",
    "new_string": "             fontsize=7, color='#333333')"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T20:35:15.402563+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig3_gate_shift.py has been updated. All occurrences were successfully replaced.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T20:35:15.402685+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 gen_fig3_gate_shift.py 2>&1",
  "description": "Regenerate with 7pt minimum fonts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 gen_fig3_gate_shift.py 2>&1",
    "description": "Regenerate with 7pt minimum fonts"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T20:35:15.402797+00:00_

Saved: fig3_gate_shift.pdf + .png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T20:35:15.402906+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig3_gate_shift.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig3_gate_shift.png"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-19T20:35:15.403287+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-19T20:35:15.403468+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "fig3_gate_shift",
  "type": "chart",
  "description": "Figure 3: 2-panel statistical figure. (a) Cleveland dot plot showing gate passivization at late turns (top-5 layers, Wilcoxon p=3.73e-8). (b) Log-scale grouped bar chart showing 30x GAR gap between IID and model-generated evaluation, demonstrating exposure bias selectively disrupts learned attention patterns.",
  "project": "turn_residual_gating",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig3_gate_shift.pdf",
  "tags": "['paper', 'figure', 'gate_analysis', 'exposure_bias', 'distribution_shift']",
  "skill": "draw-paper-figure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "fig3_gate_shift",
    "type": "chart",
    "description": "Figure 3: 2-panel statistical figure. (a) Cleveland dot plot showing gate passivization at late turns (top-5 layers, Wilcoxon p=3.73e-8). (b) Log-scale grouped bar chart showing 30x GAR gap between IID and model-generated evaluation, demonstrating exposure bias selectively disrupts learned attention patterns.",
    "project": "turn_residual_gating",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig3_gate_shift.pdf",
    "tags": "['paper', 'figure', 'gate_analysis', 'exposure_bias', 'distribution_shift']",
    "skill": "draw-paper-figure"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T20:35:15.403623+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260519_91c17c\", \"name\": \"fig3_gate_shift\", \"type\": \"chart\", \"description\": \"Figure 3: 2-panel statistical figure. (a) Cleveland dot plot showing gate passivization at late turns (top-5 layers, Wilcoxon p=3.73e-8). (b) Log-scale grouped bar chart showing 30x GAR gap between IID and model-generated evaluation, demonstrating exposure bias selectively disrupts learned attention patterns.\", \"path\": \"projects/turn_residual_gating/artifacts/_project/chart/fig3_gate_shift.pdf\", \"url\": null, \"project\": \"turn_residual_gating\", \"exp_id\": null, \"skill\": \"draw-paper-figure\", \"created_at\": \"2026-05-19T20:35:03.842471+00:00\", \"tags\": [\"paper\", \"figure\", \"gate_analysis\", \"exposure_bias\", \"distribution_shift\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-19T20:35:15.403801+00:00_

Figure 3 已生成并注册。

**输出**:
- PDF: `figures/paper/fig3_gate_shift.pdf`
- PNG: `figures/paper/fig3_gate_shift.png`
- 生成脚本: `figures/paper/gen_fig3_gate_shift.py`

**两面板内容**:
- **(a)** Cleveland dot plot — top-5 层的 gate turn conditioning，early turn (蓝) vs late turn (橙红) 连线图，diff 标注在右侧，stats box 含 Wilcoxon p=3.73×10⁻⁸, r=0.975
- **(b)** Log-scale grouped bar chart — 4 模型 IID eval (绿) vs model-generated (橙红)，TG 的 30× GAR gap 用双向箭头+粗体标注突出；UG/LoRA-only 的 model-gen 数据标 "n/a"（未评估）；背景色带区分 IID/model-gen regime

**数据来源均已验证**: panel (a) 取自 `phase2_tg_s42_v7` registry 的 `eval_gate_dynamic_range_top5`，panel (b) IID 取自 `phase2_4way_eval`，model-gen 取自 v7 eval metrics。所有字号 ≥ 7pt。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_figure_fig3_gate_shift_20260519T202802"
}
```

</details>

---
