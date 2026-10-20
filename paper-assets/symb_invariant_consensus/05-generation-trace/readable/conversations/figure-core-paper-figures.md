# figure core paper figures

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_figure_core-paper-figures_20260517T172302.jsonl`
- **Structured JSON:** [`c50a15c0eccdf9405073.json`](../../sessions/c5/c50a15c0eccdf9405073.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-17T17:25:38.488601+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T17:25:38.489992+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "ToolSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T17:25:38.490247+00:00_

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
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T17:25:38.490649+00:00_

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
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T17:25:38.490866+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "head -50 /root/symb_invariant_consensus/analysis/f2_per_problem.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "head -50 /root/symb_invariant_consensus/analysis/f2_per_problem.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T17:25:38.491178+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "ls -la /root/symb_invariant_consensus/artifacts/figures/ 2>/dev/null; ls -la /root/symb_invariant_consensus/scripts/ 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "ls -la /root/symb_invariant_consensus/artifacts/figures/ 2>/dev/null; ls -la /root/symb_invariant_consensus/scripts/ 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T17:25:38.491347+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "wc -l /root/symb_invariant_consensus/analysis/f2_per_problem.csv",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "wc -l /root/symb_invariant_consensus/analysis/f2_per_problem.csv",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T17:25:38.491524+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"problem_id,dataset,level,ground_truth,n_unique_answers,vote_entropy,constraint_count,constraint_exclusion_rate,sica_answer,sc_answer,sica_correct,sc_correct,sica_flipped\\nProofWriter_RelNeg-OWA-D5-81_Q11,proofwriter,D5,True,2,0.8113,37,0.027,Unknown,Unknown,0,0,0\\nProofWriter_AttNoneg-OWA-D5-585_Q19,proofwriter,D5,Unknown,2,0.4138,24,0.0417,Unknown,Unknown,1,1,0\\nProofWriter_RelNoneg-OWA-D5-949_Q8,proofwriter,D5,False,2,0.9183,21,0.0476,False,False,1,1,0\\nProofWriter_AttNeg-OWA-D5-270_Q8,proofwriter,D5,False,2,0.65,34,0.0588,False,False,1,1,0\\nProofWriter_AttNoneg-OWA-D5-572_Q18,proofwriter,D5,Unknown,2,1.0,32,0.0312,Unknown,False,1,0,1\\nProofWriter_AttNeg-OWA-D5-285_Q16,proofwriter,D5,Unknown,2,0.8113,30,0.0667,False,False,0,0,0\\nProofWriter_AttNoneg-OWA-D5-735_Q9,proofwriter,D5,True,2,0.9183,29,0.0345,True,Unknown,1,0,1\\nProofWriter_RelNeg-OWA-D5-966_Q7,proofwriter,D5,True,2,0.9183,36,0.0278,Unknown,Unknown,0,0,0\\nProofWriter_AttNoneg-OWA-D5-352_Q8,proofwriter,D5,False,3,1.2807,31,0.0645,False,False,1,1,0\\nProofWriter_AttNoneg-OWA-D5-296_Q13,proofwriter,D5,Unknown,3,1.1887,31,0.0645,True,True,0,0,0\\nProofWriter_AttNeg-OWA-D5-315_Q16,proofwriter,D5,Unknown,2,0.8113,19,0.1053,Unknown,Unknown,1,1,0\\nProofWriter_AttNeg-OWA-D5-891_Q9,proofwriter,D5,True,2,0.9799,15,0.0667,Unknown,Unknown,0,0,0\\nProofWriter_RelNoneg-OWA-D5-992_Q8,proofwriter,D5,False,2,0.8113,32,0.0312,Unknown,Unknown,0,0,0\\nProofWriter_RelNeg-OWA-D5-70_Q11,proofwriter,D5,True,2,0.4138,44,0.0455,Unknown,Unknown,0,0,0\\nProofWriter_AttNoneg-OWA-D5-165_Q13,proofwriter,D5,Unknown,2,0.8113,23,0.0435,Unknown,Unknown,1,1,0\\nProofWriter_AttNoneg-OWA-D5-1330_Q11,proofwriter,D5,True,2,0.9183,35,0.0286,Unknown,Unknown,0,0,0\\nProofWriter_RelNeg-OWA-D5-115_Q19,proofwriter,D5,Unknown,2,0.65,20,0.05,Unknown,Unknown,1,1,0\\nProofWriter_RelNeg-OWA-D5-747_Q6,proofwriter,D5,False,2,0.4138,34,0.0294,Unknown,Unknown,0,0,0\\nProofWriter_RelNeg-OWA-D5-14
…[truncated 3030 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T17:25:38.491673+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T17:25:38.491800+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"308 /root/symb_invariant_consensus/analysis/f2_per_problem.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 12.73}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T17:25:38.491985+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "ls -la /root/symb_invariant_consensus/artifacts/figures/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "ls -la /root/symb_invariant_consensus/artifacts/figures/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T17:25:38.492135+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "ls /root/symb_invariant_consensus/scripts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "ls /root/symb_invariant_consensus/scripts/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T17:25:38.492314+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 340\\ndrwxr-xr-x 3 root root    159 May 18 01:02 .\\ndrwxr-xr-x 3 root root    143 May 18 00:29 ..\\n-rw-r--r-- 1 root root  22990 May 18 00:31 f2_per_problem_scatter.pdf\\n-rw-r--r-- 1 root root 151260 May 18 00:31 f2_per_problem_scatter.png\\n-rw-r--r-- 1 root root  27064 May 18 00:40 f4_c0_vs_gap.pdf\\n-rw-r--r-- 1 root root 139394 May 18 00:40 f4_c0_vs_gap.png\\ndrwxr-xr-x 2 root root     68 May 18 01:03 paper\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.15}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T17:25:38.492478+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"README_experiments.md\\n__pycache__\\nanalyze_discriminative_power.py\\nanalyze_discriminative_power_v2.py\\nanalyze_expanded.py\\ncompute_constraint_quality_correlation.py\\nconstraint_ablation.py\\neval_arc.py\\neval_gsm8k.py\\neval_math_l45.py\\neval_strategyqa.py\\nexp015_logic_lm_baseline.py\\nextract_constraints_for_ablation.py\\nfig1_pipeline.py\\npilot_constraint_filtering.py\\npilot_contrastive_constraints.py\\nplot_f4_fixed.py\\nplot_hero_figures.py\\nprepare_arc.py\\nprepare_gsm8k.py\\nprepare_math_l45.py\\nprepare_strategyqa.py\\nrun_exp004_qwen7b.sh\\nrun_exp010_mistral.sh\\nrun_exp011_llama8b.sh\\nrun_exp012_gsm8k.sh\\nrun_exp014_deepseek_r1_7b.sh\\nrun_exp017_strategyqa.sh\\nrun_exp018_arc.sh\\nrun_exp019_strategyqa_200.sh\\nrun_exp020_folio_200.sh\\nrun_exp020_llama8b_folio204.sh\\nrun_exp021_oracle_folio.py\\nrun_exp021_temp_t03.sh\\nrun_exp022_temp_t05.sh\\nrun_exp023_temp_t10.sh\\nrun_gsm8k_pilot.py\\nrun_k_ablation.py\\nrun_k_ablation.py.bak\\nrun_k_ablation.sh\\nrun_mistral_strategyqa.sh\\nrun_pilot_constraint_filtering.sh\\nrun_pilot_contrastive_v2.sh\\nrun_temperature_ablation.sh\\nstart_vllm_72b_awq.sh\\nstart_vllm_7b.sh\\nstart_vllm_deepseek_r1_7b.sh\\nstart_vllm_deepseek_r1_8b.sh\\nstart_vllm_llama_8b.sh\\nstart_vllm_mistral_7b.sh\\nweighted_sc_baseline.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T17:25:38.492665+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "account": "root",
  "command": "cat > /root/symb_invariant_consensus/scripts/plot_paper_figures_v2.py << 'PYEOF'\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patches as mpatches\nimport numpy as np\nimport pandas as pd\nimport os\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 8,\n    'axes.titlesize': 9,\n    'axes.labelsize': 8,\n    'xtick.labelsize': 7,\n    'ytick.labelsize': 7,\n    'legend.fontsize': 7,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'lines.linewidth': 1.2,\n})\n\nOUTDIR = '/root/symb_invariant_consensus/artifacts/figures/paper'\nos.makedirs(OUTDIR, exist_ok=True)\n\n# Okabe-Ito colorblind-friendly palette\nOI_BLUE    = '#0072B2'\nOI_ORANGE  = '#E69F00'\nOI_GREEN   = '#009E73'\nOI_RED     = '#D55E00'\nOI_PURPLE  = '#CC79A7'\nOI_SKYBLUE = '#56B4E9'\nOI_YELLOW  = '#F0E442'\nOI_BLACK   = '#000000'\n\n# ============================================================\n# Figure 1: operating_regime (C0 vs SICA-SC gap scatter)\n# ============================================================\ndef plot_operating_regime():\n    data = [\n        ('Qwen2.5-14B',    'FOLIO+PW',    804, 38.2,  +0.3),\n        ('Qwen2.5-14B',    'StrategyQA',   60, 10.0,  +3.33),\n        ('Qwen2.5-14B',    'ARC-Chall',    60,  5.0,  -1.67),\n        ('Mistral-7B',     'FOLIO+PW',     60, 50.0,   0.0),\n        ('LLaMA-3.1-8B',   'StrategyQA',  200, 41.0,  +2.0),\n        ('LLaMA-3.1-8B',   'FOLIO',       204, 61.8,  -2.45),\n        ('DeepSeek-R1-7B',  'FOLIO+PW',    60, 58.3,  -3.33),\n        ('Qwen2.5-14B',    'GSM8K',        30, 13.3,   0.0),\n    ]\n\n    models = sorted(set(r[0] for r in data))\n    model_colors = {\n        'Qwen2.5-14B':    OI_BLUE,\n        'Mistral-7B':     OI_PURPLE,\n        'LLaMA-3.1-8B':   OI_ORANGE,\n        'DeepSeek-R1-7B':  OI_RED,\n    }\n    model_markers = {\n        'Qwen2.5-14B':    'o',\n        'Mistral-7B':     's',\n        'LLaMA-3.1-8B':   '^',\n        'DeepSeek-R1-7B':  'D',\n    }\n\n    fig, ax = plt.subplots(figsize=(3.25, 2.6))\n\n    ax.axhline(0, color='#888888', linewidth=0.8, linestyle='-', zorder=1)\n\n    for model, domain, n, c0, delta in data:\n        size = np.sqrt(n) * 1.8\n        color = model_colors[model]\n        marker = model_markers[model]\n        ax.scatter(c0, delta, s=size, c=color, marker=marker,\n                   edgecolors='white', linewidths=0.4, zorder=3, alpha=0.9)\n\n        label_text = f'{domain}'\n        offset_x, offset_y = 1.5, 0.3\n        if domain == 'FOLIO+PW' and model == 'Qwen2.5-14B':\n            offset_y = -0.6\n        if domain == 'FOLIO' and model == 'LLaMA-3.1-8B':\n            offset_x = -1.5\n            offset_y = -0.6\n        if domain == 'StrategyQA' and model == 'LLaMA-3.1-8B':\n            offset_y = 0.5\n        if domain == 'FOLIO+PW' and model == 'DeepSeek-R1-7B':\n            offset_y = -0.6\n\n        ax.annotate(label_text, (c0, delta),\n                    xytext=(offset_x, offset_y), textcoords='offset points',\n                    fontsize=5.5, color='#444444', ha='left', va='bottom')\n\n    handles = []\n    for model in models:\n        h = ax.scatter([], [], s=30, c=model_colors[model],\n                       marker=model_markers[model], edgecolors='white',\n                       linewidths=0.4, label=model)\n        handles.append(h)\n\n    size_legend_ns = [30, 200, 800]\n    for n_val in size_legend_ns:\n        h = ax.scatter([], [], s=np.sqrt(n_val)*1.8, c='#CCCCCC',\n                       edgecolors='#666666', linewidths=0.4,\n                       label=f'n={n_val}')\n        handles.append(h)\n\n    ax.legend(handles=handles, loc='upper left', fontsize=5.5,\n              framealpha=0.9, edgecolor='#CCCCCC', ncol=2,\n              handletextpad=0.3, columnspacing=0.8, borderpad=0.4)\n\n    ax.set_xlabel(r'Multi-candidate rate $C_0$ (%)')\n    ax.set_ylabel(r'SICA$-$SC accuracy gap (pp)')\n    ax.set_xlim(-2, 70)\n    ax.set_ylim(-5, 5)\n    ax.grid(True, alpha=0.2, linewidth=0.5)\n\n    for fmt in ['pdf', 'png']:\n        path = os.path.join(OUTDIR, f'operating_regime.{fmt}')\n        fig.savefig(path)\n        print(f'Saved: {path} ({os.path.getsize(path)} bytes)')\n    plt.close(fig)\n\n\n# ============================================================\n# Figure 2: capability_scatter (vote entropy vs exclusion rate)\n# ============================================================\ndef plot_capability_scatter():\n    csv_path = '/root/symb_invariant_consensus/analysis/f2_per_problem.csv'\n    df = pd.read_csv(csv_path)\n\n    fig, ax = plt.subplots(figsize=(3.25, 2.6))\n\n    mask_correct = df['sica_correct'] == 1\n    mask_wrong = df['sica_correct'] == 0\n    mask_flipped = df['sica_flipped'] == 1\n\n    ax.scatter(df.loc[mask_correct & ~mask_flipped, 'vote_entropy'],\n               df.loc[mask_correct & ~mask_flipped, 'constraint_exclusion_rate'],\n               s=8, c=OI_GREEN, alpha=0.5, edgecolors='none',\n               label='SICA correct', zorder=2, rasterized=True)\n\n    ax.scatter(df.loc[mask_wrong & ~mask_flipped, 'vote_entropy'],\n               df.loc[mask_wrong & ~mask_flipped, 'constraint_exclusion_rate'],\n               s=8, c=OI_RED, alpha=0.5, edgecolors='none',\n               label='SICA wrong', zorder=2, rasterized=True)\n\n    ax.scatter(df.loc[mask_flipped, 'vote_entropy'],\n               df.loc[mask_flipped, 'constraint_exclusion_rate'],\n               s=18, c=OI_SKYBLUE, alpha=0.85, edgecolors=OI_BLUE,\n               linewidths=0.5, marker='D',\n               label='SICA flipped', zorder=4)\n\n    ax.set_xlabel('Vote entropy (K=12)')\n    ax.set_ylabel('Constraint exclusion rate')\n    ax.grid(True, alpha=0.2, linewidth=0.5)\n\n    ax.legend(loc='upper right', fontsize=6, framealpha=0.9,\n              edgecolor='#CCCCCC', handletextpad=0.3, borderpad=0.4,\n              markerscale=1.2)\n\n    for fmt in ['pdf', 'png']:\n        path = os.path.join(OUTDIR, f'capability_scatter.{fmt}')\n        fig.savefig(path)\n        print(f'Saved: {path} ({os.path.getsize(path)} bytes)')\n    plt.close(fig)\n\n\nif __name__ == '__main__':\n    print('=== Figure 1: operating_regime ===')\n    plot_operating_regime()\n    print()\n    print('=== Figure 2: capability_scatter ===')\n    plot_capability_scatter()\n    print()\n    print('Done.')\nPYEOF\necho \"Script written OK\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "account": "root",
    "command": "cat > /root/symb_invariant_consensus/scripts/plot_paper_figures_v2.py << 'PYEOF'\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patches as mpatches\nimport numpy as np\nimport pandas as pd\nimport os\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 8,\n    'axes.titlesize': 9,\n    'axes.labelsize': 8,\n    'xtick.labelsize': 7,\n    'ytick.labelsize': 7,\n    'legend.fontsize': 7,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'lines.linewidth': 1.2,\n})\n\nOUTDIR = '/root/symb_invariant_consensus/artifacts/figures/paper'\nos.makedirs(OUTDIR, exist_ok=True)\n\n# Okabe-Ito colorblind-friendly palette\nOI_BLUE    = '#0072B2'\nOI_ORANGE  = '#E69F00'\nOI_GREEN   = '#009E73'\nOI_RED     = '#D55E00'\nOI_PURPLE  = '#CC79A7'\nOI_SKYBLUE = '#56B4E9'\nOI_YELLOW  = '#F0E442'\nOI_BLACK   = '#000000'\n\n# ============================================================\n# Figure 1: operating_regime (C0 vs SICA-SC gap scatter)\n# ============================================================\ndef plot_operating_regime():\n    data = [\n        ('Qwen2.5-14B',    'FOLIO+PW',    804, 38.2,  +0.3),\n        ('Qwen2.5-14B',    'StrategyQA',   60, 10.0,  +3.33),\n        ('Qwen2.5-14B',    'ARC-Chall',    60,  5.0,  -1.67),\n        ('Mistral-7B',     'FOLIO+PW',     60, 50.0,   0.0),\n        ('LLaMA-3.1-8B',   'StrategyQA',  200, 41.0,  +2.0),\n        ('LLaMA-3.1-8B',   'FOLIO',       204, 61.8,  -2.45),\n        ('DeepSeek-R1-7B',  'FOLIO+PW',    60, 58.3,  -3.33),\n        ('Qwen2.5-14B',    'GSM8K',        30, 13.3,   0.0),\n    ]\n\n    models = sorted(set(r[0] for r in data))\n    model_colors = {\n        'Qwen2.5-14B':    OI_BLUE,\n        'Mistral-7B':     OI_PURPLE,\n        'LLaMA-3.1-8B':   OI_ORANGE,\n        'DeepSeek-R1-7B':  OI_RED,\n    }\n    model_markers = {\n        'Qwen2.5-14B':    'o',\n        'Mistral-7B':     's',\n        'LLaMA-3.1-8B':   '^',\n        'DeepSeek-R1-7B':  'D',\n    }\n\n    fig, ax = plt.subplots(figsize=(3.25, 2.6))\n\n    ax.axhline(0, color='#888888', linewidth=0.8, linestyle='-', zorder=1)\n\n    for model, domain, n, c0, delta in data:\n        size = np.sqrt(n) * 1.8\n        color = model_colors[model]\n        marker = model_markers[model]\n        ax.scatter(c0, delta, s=size, c=color, marker=marker,\n                   edgecolors='white', linewidths=0.4, zorder=3, alpha=0.9)\n\n        label_text = f'{domain}'\n        offset_x, offset_y = 1.5, 0.3\n        if domain == 'FOLIO+PW' and model == 'Qwen2.5-14B':\n            offset_y = -0.6\n        if domain == 'FOLIO' and model == 'LLaMA-3.1-8B':\n            offset_x = -1.5\n            offset_y = -0.6\n        if domain == 'StrategyQA' and model == 'LLaMA-3.1-8B':\n            offset_y = 0.5\n        if domain == 'FOLIO+PW' and model == 'DeepSeek-R1-7B':\n            offset_y = -0.6\n\n        ax.annotate(label_text, (c0, delta),\n                    xytext=(offset_x, offset_y), textcoords='offset points',\n                    fontsize=5.5, color='#444444', ha='left', va='bottom')\n\n    handles = []\n    for model in models:\n        h = ax.scatter([], [], s=30, c=model_colors[model],\n                       marker=model_markers[model], edgecolors='white',\n                       linewidths=0.4, label=model)\n        handles.append(h)\n\n    size_legend_ns = [30, 200, 800]\n    for n_val in size_legend_ns:\n        h = ax.scatter([], [], s=np.sqrt(n_val)*1.8, c='#CCCCCC',\n                       edgecolors='#666666', linewidths=0.4,\n                       label=f'n={n_val}')\n        handles.append(h)\n\n    ax.legend(handles=handles, loc='upper left', fontsize=5.5,\n              framealpha=0.9, edgecolor='#CCCCCC', ncol=2,\n              handletextpad=0.3, columnspacing=0.8, borderpad=0.4)\n\n    ax.set_xlabel(r'Multi-candidate rate $C_0$ (%)')\n    ax.set_ylabel(r'SICA$-$SC accuracy gap (pp)')\n    ax.set_xlim(-2, 70)\n    ax.set_ylim(-5, 5)\n    ax.grid(True, alpha=0.2, linewidth=0.5)\n\n    for fmt in ['pdf', 'png']:\n        path = os.path.join(OUTDIR, f'operating_regime.{fmt}')\n        fig.savefig(path)\n        print(f'Saved: {path} ({os.path.getsize(path)} bytes)')\n    plt.close(fig)\n\n\n# ============================================================\n# Figure 2: capability_scatter (vote entropy vs exclusion rate)\n# ============================================================\ndef plot_capability_scatter():\n    csv_path = '/root/symb_invariant_consensus/analysis/f2_per_problem.csv'\n    df = pd.read_csv(csv_path)\n\n    fig, ax = plt.subplots(figsize=(3.25, 2.6))\n\n    mask_correct = df['sica_correct'] == 1\n    mask_wrong = df['sica_correct'] == 0\n    mask_flipped = df['sica_flipped'] == 1\n\n    ax.scatter(df.loc[mask_correct & ~mask_flipped, 'vote_entropy'],\n               df.loc[mask_correct & ~mask_flipped, 'constraint_exclusion_rate'],\n               s=8, c=OI_GREEN, alpha=0.5, edgecolors='none',\n               label='SICA correct', zorder=2, rasterized=True)\n\n    ax.scatter(df.loc[mask_wrong & ~mask_flipped, 'vote_entropy'],\n               df.loc[mask_wrong & ~mask_flipped, 'constraint_exclusion_rate'],\n               s=8, c=OI_RED, alpha=0.5, edgecolors='none',\n               label='SICA wrong', zorder=2, rasterized=True)\n\n    ax.scatter(df.loc[mask_flipped, 'vote_entropy'],\n               df.loc[mask_flipped, 'constraint_exclusion_rate'],\n               s=18, c=OI_SKYBLUE, alpha=0.85, edgecolors=OI_BLUE,\n               linewidths=0.5, marker='D',\n               label='SICA flipped', zorder=4)\n\n    ax.set_xlabel('Vote entropy (K=12)')\n    ax.set_ylabel('Constraint exclusion rate')\n    ax.grid(True, alpha=0.2, linewidth=0.5)\n\n    ax.legend(loc='upper right', fontsize=6, framealpha=0.9,\n              edgecolor='#CCCCCC', handletextpad=0.3, borderpad=0.4,\n              markerscale=1.2)\n\n    for fmt in ['pdf', 'png']:\n        path = os.path.join(OUTDIR, f'capability_scatter.{fmt}')\n        fig.savefig(path)\n        print(f'Saved: {path} ({os.path.getsize(path)} bytes)')\n    plt.close(fig)\n\n\nif __name__ == '__main__':\n    print('=== Figure 1: operating_regime ===')\n    plot_operating_regime()\n    print()\n    print('=== Figure 2: capability_scatter ===')\n    plot_capability_scatter()\n    print()\n    print('Done.')\nPYEOF\necho \"Script written OK\""
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T17:25:38.492859+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T17:25:38.493054+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "account": "root",
  "command": "source /root/miniconda3/bin/activate && cd /root/symb_invariant_consensus && python scripts/plot_paper_figures_v2.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "account": "root",
    "command": "source /root/miniconda3/bin/activate && cd /root/symb_invariant_consensus && python scripts/plot_paper_figures_v2.py"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T17:25:38.493198+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Figure 1: operating_regime ===\\nSaved: /root/symb_invariant_consensus/artifacts/figures/paper/operating_regime.pdf (22836 bytes)\\nSaved: /root/symb_invariant_consensus/artifacts/figures/paper/operating_regime.png (77133 bytes)\\n\\n=== Figure 2: capability_scatter ===\\nSaved: /root/symb_invariant_consensus/artifacts/figures/paper/capability_scatter.pdf (39792 bytes)\\nSaved: /root/symb_invariant_consensus/artifacts/figures/paper/capability_scatter.png (74163 bytes)\\n\\nDone.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.29}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T17:25:38.493346+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "account": "root",
  "command": "cd /root/symb_invariant_consensus/artifacts/figures/paper && ls -la"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "account": "root",
    "command": "cd /root/symb_invariant_consensus/artifacts/figures/paper && ls -la"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T17:25:38.493482+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 432\\ndrwxr-xr-x 2 root root   4096 May 18 01:24 .\\ndrwxr-xr-x 3 root root    159 May 18 01:02 ..\\n-rw-r--r-- 1 root root  39792 May 18 01:24 capability_scatter.pdf\\n-rw-r--r-- 1 root root  74163 May 18 01:24 capability_scatter.png\\n-rw-r--r-- 1 root root  45917 May 18 01:11 fig1_pipeline.pdf\\n-rw-r--r-- 1 root root 164768 May 18 01:11 fig1_pipeline.png\\n-rw-r--r-- 1 root root  22836 May 18 01:24 operating_regime.pdf\\n-rw-r--r-- 1 root root  77133 May 18 01:24 operating_regime.png\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.04}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T17:25:38.493618+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "scp connect.westd.seetacloud.com:/root/symb_invariant_consensus/artifacts/figures/paper/operating_regime.png /tmp/operating_regime.png && scp connect.westd.seetacloud.com:/root/symb_invariant_consensus/artifacts/figures/paper/capability_scatter.png /tmp/capability_scatter.png",
  "description": "Download generated PNGs for visual inspection",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "Bash",
  "tool_args": {
    "command": "scp connect.westd.seetacloud.com:/root/symb_invariant_consensus/artifacts/figures/paper/operating_regime.png /tmp/operating_regime.png && scp connect.westd.seetacloud.com:/root/symb_invariant_consensus/artifacts/figures/paper/capability_scatter.png /tmp/capability_scatter.png",
    "description": "Download generated PNGs for visual inspection",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T17:25:38.493743+00:00_

Exit code 255
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Host key verification failed.
scp: Connection closed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T17:25:38.493866+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32608",
  "account": "root",
  "command": "cd /root/symb_invariant_consensus/artifacts/figures/paper && base64 operating_regime.png | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32608",
    "account": "root",
    "command": "cd /root/symb_invariant_consensus/artifacts/figures/paper && base64 operating_regime.png | head -20"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T17:25:38.494059+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"iVBORw0KGgoAAAANSUhEUgAAA6EAAALkCAYAAAD+uTNBAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90\\nbGliIHZlcnNpb24zLjEwLjUsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvWftoOwAAAAlwSFlzAAAu\\nIwAALiMBeKU/dgABAABJREFUeJzs3Xd4FFX78PHvbnoPHULoRarUIFVCkeJPiqBI7wgoKCoWRBR7\\nAUSlCII0EQOhKFjovUrvLSEJkARCTdn03Xn/yDvzZJNNSMJusuD9ua5cZGfmnDmzk4S955xzH52i\\nKApCCCGEEEIIIUQh0Bd1A4QQQgghhBBC/HdIECqEEEIIIYQQotBIECqEEEIIIYQQotBIECqEEEII\\nIYQQotBIECqEEEIIIYQQotBIECqEEEIIIYQQotBIECqEEEIIIYQQotBIECqEEEIIIYQQotBIECqE\\nEEIIIYQQotBIECqEEEIIIYQQotBIECqEEEIIIYQQotBIECqEEEIIIYQQotA4FnUDxKMjOTmZ0NBQ\\n7XW1atVwdXUtwhYJIYQQQgghHjUShIo8Cw0NpV69etrrM2fOULdu3SJskRBCCCGEEOJRI8NxRZFS\\nFIX79+9z//59FEUp6uYIC+Qe2T+5R/ZP7pF9k/tj/+Qe2T+5R/ZPvUf2QIJQIYQQQgghhBCFRoJQ\\nIYQQQgghhBCFRoJQIYQQQgghhBCFRoJQIYQQQgghhBCFRoJQIYQQQgghhBCFRoJQIYQQQgghhBCF\\nRoJQIYQQQgghhBCFxrGoGyD+OxRFwWQyma0dpSgKRqMRgPT0dHQ6XVE1T+RA7pH9k3tk/+Qe2YZO\\np0Ov18v7KYQQjxgJQoVNmUwm4uLiuH//PvHx8RYXLzaZTADo9dIxb6/kHtk/uUf2T+6Rbeh0Ory8\\nvPD19cXb21veXyGEeARIECpsxmQyERYWhsFgKOqmCCGEeEwpikJcXBxxcXF4eHhQpUoVCUSFEMLO\\nyV9pYRP5CUB1Op0MpbJzco/sn9wj+yf3yPYMBgNhYWFar7MQQgj7JEGosIm4uDjpARVCCFHoDAYD\\ncXFxRd0MIYQQuZDhuMIm7t+/b/Zap9NRrly5bPN1FEXR5olKL4F9kntk/+Qe2T+5R7ah5h2Ijo42\\nyzlw//59fH19i65hQgghciVBqLA6RVGIj48321auXDlKlixp8Vj5YGbf5B7ZP7lH9k/uke2o/7dE\\nRUVp29REePI+CyGEfZLhuMLqsi7DAuDt7V1ErRFCCPG48/LyMnutLgkmhBDCPkkQKqzO0jIsRZGp\\nUG2HpfYIIYR4fDg4OGTbJn/7hRDCfkkQKh5L6jCspCuH0el08mFECCGEEEIIOyFBqHjsqAHo7b+n\\nEfZxM27/PU0CUSGEEEIIIeyEBKHisZI5AI1Z+Q4AMSvfkUBUCCGEEEIIOyFBqHhsWApAVRKICiGE\\nEEIIYR8kCBWPhdwCUJUEokI1dOhQdDodU6dOLeqmCCGEEEL850gQKh55eQlAVYUdiAYGBmprAqpf\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.2}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T17:25:38.494235+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32608",
  "command": "cat /root/symb_invariant_consensus/scripts/plot_paper_figures_v2.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32608",
    "command": "cat /root/symb_invariant_consensus/scripts/plot_paper_figures_v2.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T17:25:38.494439+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import matplotlib\\nmatplotlib.use('Agg')\\nimport matplotlib.pyplot as plt\\nimport matplotlib.patches as mpatches\\nimport numpy as np\\nimport pandas as pd\\nimport os\\n\\nplt.rcParams.update({\\n    'font.family': 'DejaVu Sans',\\n    'font.size': 8,\\n    'axes.titlesize': 9,\\n    'axes.labelsize': 8,\\n    'xtick.labelsize': 7,\\n    'ytick.labelsize': 7,\\n    'legend.fontsize': 7,\\n    'figure.dpi': 300,\\n    'savefig.dpi': 300,\\n    'savefig.bbox': 'tight',\\n    'savefig.pad_inches': 0.05,\\n    'axes.spines.top': False,\\n    'axes.spines.right': False,\\n    'lines.linewidth': 1.2,\\n})\\n\\nOUTDIR = '/root/symb_invariant_consensus/artifacts/figures/paper'\\nos.makedirs(OUTDIR, exist_ok=True)\\n\\n# Okabe-Ito colorblind-friendly palette\\nOI_BLUE    = '#0072B2'\\nOI_ORANGE  = '#E69F00'\\nOI_GREEN   = '#009E73'\\nOI_RED     = '#D55E00'\\nOI_PURPLE  = '#CC79A7'\\nOI_SKYBLUE = '#56B4E9'\\nOI_YELLOW  = '#F0E442'\\nOI_BLACK   = '#000000'\\n\\n# ============================================================\\n# Figure 1: operating_regime (C0 vs SICA-SC gap scatter)\\n# ============================================================\\ndef plot_operating_regime():\\n    data = [\\n        ('Qwen2.5-14B',    'FOLIO+PW',    804, 38.2,  +0.3),\\n        ('Qwen2.5-14B',    'StrategyQA',   60, 10.0,  +3.33),\\n        ('Qwen2.5-14B',    'ARC-Chall',    60,  5.0,  -1.67),\\n        ('Mistral-7B',     'FOLIO+PW',     60, 50.0,   0.0),\\n        ('LLaMA-3.1-8B',   'StrategyQA',  200, 41.0,  +2.0),\\n        ('LLaMA-3.1-8B',   'FOLIO',       204, 61.8,  -2.45),\\n        ('DeepSeek-R1-7B',  'FOLIO+PW',    60, 58.3,  -3.33),\\n        ('Qwen2.5-14B',    'GSM8K',        30, 13.3,   0.0),\\n    ]\\n\\n    models = sorted(set(r[0] for r in data))\\n    model_colors = {\\n        'Qwen2.5-14B':    OI_BLUE,\\n        'Mistral-7B':     OI_PURPLE,\\n        'LLaMA-3.1-8B':   OI_ORANGE,\\n        'DeepSeek-R1-7B':  OI_RED,\\
…[truncated 4737 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T17:25:38.494595+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/scripts/ 2>/dev/null",
  "description": "Check local scripts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/scripts/ 2>/dev/null",
    "description": "Check local scripts directory"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T17:25:38.494718+00:00_

fig1_pipeline.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T17:25:38.494855+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/scripts/plot_paper_figures_v2.py",
  "content": "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patches as mpatches\nimport numpy as np\nimport pandas as pd\nimport os\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 8,\n    'axes.titlesize': 9,\n    'axes.labelsize': 8,\n    'xtick.labelsize': 7,\n    'ytick.labelsize': 7,\n    'legend.fontsize': 7,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'lines.linewidth': 1.2,\n})\n\nOUTDIR = '/root/symb_invariant_consensus/artifacts/figures/paper'\nos.makedirs(OUTDIR, exist_ok=True)\n\n# Okabe-Ito colorblind-friendly palette\nOI_BLUE    = '#0072B2'\nOI_ORANGE  = '#E69F00'\nOI_GREEN   = '#009E73'\nOI_RED     = '#D55E00'\nOI_PURPLE  = '#CC79A7'\nOI_SKYBLUE = '#56B4E9'\nOI_YELLOW  = '#F0E442'\nOI_BLACK   = '#000000'\n\n# ============================================================\n# Figure 1: operating_regime (C0 vs SICA-SC gap scatter)\n# ============================================================\ndef plot_operating_regime():\n    data = [\n        ('Qwen2.5-14B',    'FOLIO+PW',    804, 38.2,  +0.3),\n        ('Qwen2.5-14B',    'StrategyQA',   60, 10.0,  +3.33),\n        ('Qwen2.5-14B',    'ARC-Chall',    60,  5.0,  -1.67),\n        ('Mistral-7B',     'FOLIO+PW',     60, 50.0,   0.0),\n        ('LLaMA-3.1-8B',   'StrategyQA',  200, 41.0,  +2.0),\n        ('LLaMA-3.1-8B',   'FOLIO',       204, 61.8,  -2.45),\n        ('DeepSeek-R1-7B',  'FOLIO+PW',    60, 58.3,  -3.33),\n        ('Qwen2.5-14B',    'GSM8K',        30, 13.3,   0.0),\n    ]\n\n    models = sorted(set(r[0] for r in data))\n    model_colors = {\n        'Qwen2.5-14B':    OI_BLUE,\n        'Mistral-7B':     OI_PURPLE,\n        'LLaMA-3.1-8B':   OI_ORANGE,\n        'DeepSeek-R1-7B':  OI_RED,\n    }\n    model_markers = {\n        'Qwen2.5-14B':    'o',\n        'Mistral-7B':     's',\n        'LLaMA-3.1-8B':   '^',\n        'DeepSeek-R1-7B':  'D',\n    }\n\n    fig, ax = plt.subplots(figsize=(3.25, 2.6))\n\n    ax.axhline(0, color='#888888', linewidth=0.8, linestyle='-', zorder=1)\n\n    for model, domain, n, c0, delta in data:\n        size = np.sqrt(n) * 1.8\n        color = model_colors[model]\n        marker = model_markers[model]\n        ax.scatter(c0, delta, s=size, c=color, marker=marker,\n                   edgecolors='white', linewidths=0.4, zorder=3, alpha=0.9)\n\n        label_text = f'{domain}'\n        offset_x, offset_y = 1.5, 0.3\n        if domain == 'FOLIO+PW' and model == 'Qwen2.5-14B':\n            offset_y = -0.6\n        if domain == 'FOLIO' and model == 'LLaMA-3.1-8B':\n            offset_x = -1.5\n            offset_y = -0.6\n        if domain == 'StrategyQA' and model == 'LLaMA-3.1-8B':\n            offset_y = 0.5\n        if domain == 'FOLIO+PW' and model == 'DeepSeek-R1-7B':\n            offset_y = -0.6\n\n        ax.annotate(label_text, (c0, delta),\n                    xytext=(offset_x, offset_y), textcoords='offset points',\n                    fontsize=5.5, color='#444444', ha='left', va='bottom')\n\n    handles = []\n    for model in models:\n        h = ax.scatter([], [], s=30, c=model_colors[model],\n                       marker=model_markers[model], edgecolors='white',\n                       linewidths=0.4, label=model)\n        handles.append(h)\n\n    size_legend_ns = [30, 200, 800]\n    for n_val in size_legend_ns:\n        h = ax.scatter([], [], s=np.sqrt(n_val)*1.8, c='#CCCCCC',\n                       edgecolors='#666666', linewidths=0.4,\n                       label=f'n={n_val}')\n        handles.append(h)\n\n    ax.legend(handles=handles, loc='upper left', fontsize=5.5,\n              framealpha=0.9, edgecolor='#CCCCCC', ncol=2,\n              handletextpad=0.3, columnspacing=0.8, borderpad=0.4)\n\n    ax.set_xlabel(r'Multi-candidate rate $C_0$ (%)')\n    ax.set_ylabel(r'SICA$-$SC accuracy gap (pp)')\n    ax.set_xlim(-2, 70)\n    ax.set_ylim(-5, 5)\n    ax.grid(True, alpha=0.2, linewidth=0.5)\n\n    for fmt in ['pdf', 'png']:\n        path = os.path.join(OUTDIR, f'operating_regime.{fmt}')\n        fig.savefig(path)\n        print(f'Saved: {path} ({os.path.getsize(path)} bytes)')\n    plt.close(fig)\n\n\n# ============================================================\n# Figure 2: capability_scatter (vote entropy vs exclusion rate)\n# ============================================================\ndef plot_capability_scatter():\n    csv_path = '/root/symb_invariant_consensus/analysis/f2_per_problem.csv'\n    df = pd.read_csv(csv_path)\n\n    fig, ax = plt.subplots(figsize=(3.25, 2.6))\n\n    mask_correct = df['sica_correct'] == 1\n    mask_wrong = df['sica_correct'] == 0\n    mask_flipped = df['sica_flipped'] == 1\n\n    ax.scatter(df.loc[mask_correct & ~mask_flipped, 'vote_entropy'],\n               df.loc[mask_correct & ~mask_flipped, 'constraint_exclusion_rate'],\n               s=8, c=OI_GREEN, alpha=0.5, edgecolors='none',\n               label='SICA correct', zorder=2, rasterized=True)\n\n    ax.scatter(df.loc[mask_wrong & ~mask_flipped, 'vote_entropy'],\n               df.loc[mask_wrong & ~mask_flipped, 'constraint_exclusion_rate'],\n               s=8, c=OI_RED, alpha=0.5, edgecolors='none',\n               label='SICA wrong', zorder=2, rasterized=True)\n\n    ax.scatter(df.loc[mask_flipped, 'vote_entropy'],\n               df.loc[mask_flipped, 'constraint_exclusion_rate'],\n               s=18, c=OI_SKYBLUE, alpha=0.85, edgecolors=OI_BLUE,\n               linewidths=0.5, marker='D',\n               label='SICA flipped', zorder=4)\n\n    ax.set_xlabel('Vote entropy (K=12)')\n    ax.set_ylabel('Constraint exclusion rate')\n    ax.grid(True, alpha=0.2, linewidth=0.5)\n\n    ax.legend(loc='upper right', fontsize=6, framealpha=0.9,\n              edgecolor='#CCCCCC', handletextpad=0.3, borderpad=0.4,\n              markerscale=1.2)\n\n    for fmt in ['pdf', 'png']:\n        path = os.path.join(OUTDIR, f'capability_scatter.{fmt}')\n        fig.savefig(path)\n        print(f'Saved: {path} ({os.path.getsize(path)} bytes)')\n    plt.close(fig)\n\n\nif __name__ == '__main__':\n    print('=== Figure 1: operating_regime ===')\n    plot_operating_regime()\n    print()\n    print('=== Figure 2: capability_scatter ===')\n    plot_capability_scatter()\n    print()\n    print('Done.')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/scripts/plot_paper_figures_v2.py",
    "content": "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patches as mpatches\nimport numpy as np\nimport pandas as pd\nimport os\n\nplt.rcParams.update({\n    'font.family': 'DejaVu Sans',\n    'font.size': 8,\n    'axes.titlesize': 9,\n    'axes.labelsize': 8,\n    'xtick.labelsize': 7,\n    'ytick.labelsize': 7,\n    'legend.fontsize': 7,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.05,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'lines.linewidth': 1.2,\n})\n\nOUTDIR = '/root/symb_invariant_consensus/artifacts/figures/paper'\nos.makedirs(OUTDIR, exist_ok=True)\n\n# Okabe-Ito colorblind-friendly palette\nOI_BLUE    = '#0072B2'\nOI_ORANGE  = '#E69F00'\nOI_GREEN   = '#009E73'\nOI_RED     = '#D55E00'\nOI_PURPLE  = '#CC79A7'\nOI_SKYBLUE = '#56B4E9'\nOI_YELLOW  = '#F0E442'\nOI_BLACK   = '#000000'\n\n# ============================================================\n# Figure 1: operating_regime (C0 vs SICA-SC gap scatter)\n# ============================================================\ndef plot_operating_regime():\n    data = [\n        ('Qwen2.5-14B',    'FOLIO+PW',    804, 38.2,  +0.3),\n        ('Qwen2.5-14B',    'StrategyQA',   60, 10.0,  +3.33),\n        ('Qwen2.5-14B',    'ARC-Chall',    60,  5.0,  -1.67),\n        ('Mistral-7B',     'FOLIO+PW',     60, 50.0,   0.0),\n        ('LLaMA-3.1-8B',   'StrategyQA',  200, 41.0,  +2.0),\n        ('LLaMA-3.1-8B',   'FOLIO',       204, 61.8,  -2.45),\n        ('DeepSeek-R1-7B',  'FOLIO+PW',    60, 58.3,  -3.33),\n        ('Qwen2.5-14B',    'GSM8K',        30, 13.3,   0.0),\n    ]\n\n    models = sorted(set(r[0] for r in data))\n    model_colors = {\n        'Qwen2.5-14B':    OI_BLUE,\n        'Mistral-7B':     OI_PURPLE,\n        'LLaMA-3.1-8B':   OI_ORANGE,\n        'DeepSeek-R1-7B':  OI_RED,\n    }\n    model_markers = {\n        'Qwen2.5-14B':    'o',\n        'Mistral-7B':     's',\n        'LLaMA-3.1-8B':   '^',\n        'DeepSeek-R1-7B':  'D',\n    }\n\n    fig, ax = plt.subplots(figsize=(3.25, 2.6))\n\n    ax.axhline(0, color='#888888', linewidth=0.8, linestyle='-', zorder=1)\n\n    for model, domain, n, c0, delta in data:\n        size = np.sqrt(n) * 1.8\n        color = model_colors[model]\n        marker = model_markers[model]\n        ax.scatter(c0, delta, s=size, c=color, marker=marker,\n                   edgecolors='white', linewidths=0.4, zorder=3, alpha=0.9)\n\n        label_text = f'{domain}'\n        offset_x, offset_y = 1.5, 0.3\n        if domain == 'FOLIO+PW' and model == 'Qwen2.5-14B':\n            offset_y = -0.6\n        if domain == 'FOLIO' and model == 'LLaMA-3.1-8B':\n            offset_x = -1.5\n            offset_y = -0.6\n        if domain == 'StrategyQA' and model == 'LLaMA-3.1-8B':\n            offset_y = 0.5\n        if domain == 'FOLIO+PW' and model == 'DeepSeek-R1-7B':\n            offset_y = -0.6\n\n        ax.annotate(label_text, (c0, delta),\n                    xytext=(offset_x, offset_y), textcoords='offset points',\n                    fontsize=5.5, color='#444444', ha='left', va='bottom')\n\n    handles = []\n    for model in models:\n        h = ax.scatter([], [], s=30, c=model_colors[model],\n                       marker=model_markers[model], edgecolors='white',\n                       linewidths=0.4, label=model)\n        handles.append(h)\n\n    size_legend_ns = [30, 200, 800]\n    for n_val in size_legend_ns:\n        h = ax.scatter([], [], s=np.sqrt(n_val)*1.8, c='#CCCCCC',\n                       edgecolors='#666666', linewidths=0.4,\n                       label=f'n={n_val}')\n        handles.append(h)\n\n    ax.legend(handles=handles, loc='upper left', fontsize=5.5,\n              framealpha=0.9, edgecolor='#CCCCCC', ncol=2,\n              handletextpad=0.3, columnspacing=0.8, borderpad=0.4)\n\n    ax.set_xlabel(r'Multi-candidate rate $C_0$ (%)')\n    ax.set_ylabel(r'SICA$-$SC accuracy gap (pp)')\n    ax.set_xlim(-2, 70)\n    ax.set_ylim(-5, 5)\n    ax.grid(True, alpha=0.2, linewidth=0.5)\n\n    for fmt in ['pdf', 'png']:\n        path = os.path.join(OUTDIR, f'operating_regime.{fmt}')\n        fig.savefig(path)\n        print(f'Saved: {path} ({os.path.getsize(path)} bytes)')\n    plt.close(fig)\n\n\n# ============================================================\n# Figure 2: capability_scatter (vote entropy vs exclusion rate)\n# ============================================================\ndef plot_capability_scatter():\n    csv_path = '/root/symb_invariant_consensus/analysis/f2_per_problem.csv'\n    df = pd.read_csv(csv_path)\n\n    fig, ax = plt.subplots(figsize=(3.25, 2.6))\n\n    mask_correct = df['sica_correct'] == 1\n    mask_wrong = df['sica_correct'] == 0\n    mask_flipped = df['sica_flipped'] == 1\n\n    ax.scatter(df.loc[mask_correct & ~mask_flipped, 'vote_entropy'],\n               df.loc[mask_correct & ~mask_flipped, 'constraint_exclusion_rate'],\n               s=8, c=OI_GREEN, alpha=0.5, edgecolors='none',\n               label='SICA correct', zorder=2, rasterized=True)\n\n    ax.scatter(df.loc[mask_wrong & ~mask_flipped, 'vote_entropy'],\n               df.loc[mask_wrong & ~mask_flipped, 'constraint_exclusion_rate'],\n               s=8, c=OI_RED, alpha=0.5, edgecolors='none',\n               label='SICA wrong', zorder=2, rasterized=True)\n\n    ax.scatter(df.loc[mask_flipped, 'vote_entropy'],\n               df.loc[mask_flipped, 'constraint_exclusion_rate'],\n               s=18, c=OI_SKYBLUE, alpha=0.85, edgecolors=OI_BLUE,\n               linewidths=0.5, marker='D',\n               label='SICA flipped', zorder=4)\n\n    ax.set_xlabel('Vote entropy (K=12)')\n    ax.set_ylabel('Constraint exclusion rate')\n    ax.grid(True, alpha=0.2, linewidth=0.5)\n\n    ax.legend(loc='upper right', fontsize=6, framealpha=0.9,\n              edgecolor='#CCCCCC', handletextpad=0.3, borderpad=0.4,\n              markerscale=1.2)\n\n    for fmt in ['pdf', 'png']:\n        path = os.path.join(OUTDIR, f'capability_scatter.{fmt}')\n        fig.savefig(path)\n        print(f'Saved: {path} ({os.path.getsize(path)} bytes)')\n    plt.close(fig)\n\n\nif __name__ == '__main__':\n    print('=== Figure 1: operating_regime ===')\n    plot_operating_regime()\n    print()\n    print('=== Figure 2: capability_scatter ===')\n    plot_capability_scatter()\n    print()\n    print('Done.')\n"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T17:25:38.495112+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/scripts/plot_paper_figures_v2.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_figure_core-paper-figures_20260517T172302",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-17T17:25:38.495312+00:00_

两张图表已生成，输出路径：

| 文件 | 大小 |
|------|------|
| `artifacts/figures/paper/operating_regime.pdf` | 22.8 KB |
| `artifacts/figures/paper/operating_regime.png` | 77.1 KB |
| `artifacts/figures/paper/capability_scatter.pdf` | 39.8 KB |
| `artifacts/figures/paper/capability_scatter.png` | 74.2 KB |

**Figure 1 (operating_regime)**: 8 个 model×domain 条件的散点图，点大小 ∝ √n，4 种模型用不同颜色+marker 区分，y=0 参考线，domain 标签标注，含 size legend。单栏宽 3.25"。

**Figure 2 (capability_scatter)**: 307 个 multi-candidate problem 的散点，绿色=SICA correct，红色=SICA wrong，蓝色菱形=flipped 问题高亮。散点层 rasterized 以控制 PDF 体积。

脚本已同步保存到本地 `scripts/plot_paper_figures_v2.py`。LaTeX 中 `\includegraphics` 指向 `figures/paper/operating_regime.pdf` 和 `figures/paper/capability_scatter.pdf` 即可。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_figure_core-paper-figures_20260517T172302"
}
```

</details>

---
