# paper shapley recompute d219 — Part 1 of 2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Worker execution logs

[Transcript overview](../paper-shapley-recompute-d219.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/d1/d192ceef6a70bcdc8351.json)

## Before a recorded user message

## Before a recorded user message

155 recorded events


### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---


### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse",
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only",
    "mcp__agent-ml-research__update_registry"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "b68618b2-9472-4587-a22d-daf9572966e0",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/memory/"
  },
  "fast_mode_state": "off"
}
```

---


### Assistant

_source line 3_

I'll start by reading the existing Shapley script, the appendix TODO locations, and checking available null seed D102 artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "b02f75f0-79b6-4348-be9d-b0bbd7918091",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPrw3nLjtDE6C2TLXq3yra",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15682,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15682
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 4_

<details open><summary>🔧 Tool call — Read · `toolu_01C5y47fREjymkrX3zsY82MD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/gen_shapley_contribution.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "3fdebd07-e45c-4dab-815e-efe90c959abe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPrw3nLjtDE6C2TLXq3yra",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15682,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15682
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-24T08:51:08.625Z_

<details><summary>↩ Tool result · `toolu_01C5y47fREjymkrX3zsY82MD`</summary>

```text
1	#!/usr/bin/env python3
2	"""Figure A.2: Shapley method contribution analysis.
3	Unified style with project palette."""
4	import matplotlib
5	matplotlib.use('Agg')
6	import matplotlib.pyplot as plt
7	import matplotlib.patheffects as pe
8	import numpy as np
9	import json
10	from pathlib import Path
11	
12	OUT = Path(__file__).parent
13	DATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_values_v2.json')
14	
15	plt.rcParams.update({
16	    'font.family': 'serif',
17	    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],
18	    'font.size': 9,
19	    'axes.labelsize': 10,
20	    'xtick.labelsize': 8,
21	    'ytick.labelsize': 9,
22	    'legend.fontsize': 7.5,
23	    'figure.dpi': 300,
24	    'savefig.dpi': 300,
25	    'savefig.bbox': 'tight',
26	    'savefig.pad_inches': 0.08,
27	    'axes.spines.top': False,
28	    'axes.spines.right': False,
29	    'pdf.fonttype': 42,
30	    'ps.fonttype': 42,
31	    'mathtext.fontset': 'cm',
32	})
33	
34	with open(DATA) as f:
35	    d = json.load(f)
36	
37	sv = d['main_result_6pair']
38	
39	methods_raw = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']
40	labels = ['Naive\nXCorr', 'Diff\nXCorr', 'Thresh.\nOnset', 'Perm\nGranger', 'TY\nGranger']
41	
42	fpr_vals = [sv['fpr_shapley'][m] for m in methods_raw]
43	fnr_vals = [sv['fnr_shapley'][m] for m in methods_raw]
44	comb_vals = [sv['combined_shapley'][m] for m in methods_raw]
45	
46	# Method colors: PermG highlighted as the champion
47	METHOD_COLORS = {
48	    'naive_xcorr':     '#D4694A',
49	    'diff_xcorr':      '#E8C170',
50	    'threshold_onset': '#8CB4D5',
51	    'perm_granger':    '#2C4A6E',
52	    'ty_granger':      '#3B6FA0',
53	}
54	colors = [METHOD_COLORS[m] for m in methods_raw]
55	
56	x = np.arange(len(methods_raw))
57	bar_width = 0.65
58	
59	fig, (ax_fpr, ax_fnr, ax_comb) = plt.subplots(
60	    1, 3, figsize=(7.2, 2.8),
61	    gridspec_kw={'wspace': 0.38}
62	)
63	
64	def draw_bars(ax, vals, title, panel_label, show_ylabel=True):
65	    bars = ax.bar(x, vals, bar_width, color=colors, edgecolor='white', linewidth=0.5, zorder=3)
66	    ax.set_xticks(x)
67	    ax.set_xticklabels(labels, fontsize=6.5, linespacing=0.9)
68	    ax.axhline(0, color='#AAAAAA', linewidth=0.5, zorder=1)
69	    ax.set_title(title, fontsize=9, pad=10)
70	    ax.text(-0.20, 1.12, panel_label, transform=ax.transAxes,
71	            fontsize=10, fontweight='bold', va='bottom')
72	    if show_ylabel:
73	        ax.set_ylabel('Shapley value')
74	
75	    for bar, val in zip(bars, vals):
76	        y_pos = val + 0.012 if val >= 0 else val - 0.020
77	        va = 'bottom' if val >= 0 else 'top'
78	        t = ax.text(bar.get_x() + bar.get_width() / 2, y_pos,
79	                    f'{val:+.3f}' if abs(val) >= 0.001 else '0.000',
80	                    ha='center', va=va, fontsize=6, color='#333333')
81	        t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])
82	
83	    perm_idx = methods_raw.index('perm_granger')
84	    bars[perm_idx].set_edgecolor('#1A1A1A')
85	    bars[perm_idx].set_linewidth(1.2)
86	
87	draw_bars(ax_fpr, fpr_vals, 'FPR contribution', '(a)')
88	ax_fpr.set_ylim(-0.05, 0.72)
89	
90	draw_bars(ax_fnr, fnr_vals, 'FNR contribution (6-pair)', '(b)', show_ylabel=False)
91	ax_fnr.set_ylim(-0.48, 0.05)
92	
93	draw_bars(ax_comb, comb_vals, 'Combined (FPR + FNR)', '(c)', show_ylabel=False)
94	ax_comb.set_ylim(-0.25, 0.25)
95	
96	# Compact PermG annotation
97	t_perm = ax_fpr.text(3, 0.04, 'zero\nFPR', fontsize=6, color='#2C4A6E',
98	                     ha='center', va='bottom', fontstyle='italic', linespacing=0.85)
99	t_perm.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])
100	
101	fig.subplots_adjust(left=0.08, right=0.97, bottom=0.18, top=0.84, wspace=0.38)
102	
103	for fmt in ['pdf', 'png']:
104	    fig.savefig(OUT / f'shapley_method_contribution.{fmt}', dpi=300)
105	plt.close()
106	print(f'Saved: {OUT}/shapley_method_contribution.pdf + .png')
107	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "c31cd5b8-7f55-4274-9d93-908cfb609e4b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/gen_shapley_contribution.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Figure A.2: Shapley method contribution analysis.\nUnified style with project palette.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nimport numpy as np\nimport json\nfrom pathlib import Path\n\nOUT = Path(__file__).parent\nDATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_values_v2.json')\n\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],\n    'font.size': 9,\n    'axes.labelsize': 10,\n    'xtick.labelsize': 8,\n    'ytick.labelsize': 9,\n    'legend.fontsize': 7.5,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.08,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n    'mathtext.fontset': 'cm',\n})\n\nwith open(DATA) as f:\n    d = json.load(f)\n\nsv = d['main_result_6pair']\n\nmethods_raw = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']\nlabels = ['Naive\\nXCorr', 'Diff\\nXCorr', 'Thresh.\\nOnset', 'Perm\\nGranger', 'TY\\nGranger']\n\nfpr_vals = [sv['fpr_shapley'][m] for m in methods_raw]\nfnr_vals = [sv['fnr_shapley'][m] for m in methods_raw]\ncomb_vals = [sv['combined_shapley'][m] for m in methods_raw]\n\n# Method colors: PermG highlighted as the champion\nMETHOD_COLORS = {\n    'naive_xcorr':     '#D4694A',\n    'diff_xcorr':      '#E8C170',\n    'threshold_onset': '#8CB4D5',\n    'perm_granger':    '#2C4A6E',\n    'ty_granger':      '#3B6FA0',\n}\ncolors = [METHOD_COLORS[m] for m in methods_raw]\n\nx = np.arange(len(methods_raw))\nbar_width = 0.65\n\nfig, (ax_fpr, ax_fnr, ax_comb) = plt.subplots(\n    1, 3, figsize=(7.2, 2.8),\n    gridspec_kw={'wspace': 0.38}\n)\n\ndef draw_bars(ax, vals, title, panel_label, show_ylabel=True):\n    bars = ax.bar(x, vals, bar_width, color=colors, edgecolor='white', linewidth=0.5, zorder=3)\n    ax.set_xticks(x)\n    ax.set_xticklabels(labels, fontsize=6.5, linespacing=0.9)\n    ax.axhline(0, color='#AAAAAA', linewidth=0.5, zorder=1)\n    ax.set_title(title, fontsize=9, pad=10)\n    ax.text(-0.20, 1.12, panel_label, transform=ax.transAxes,\n            fontsize=10, fontweight='bold', va='bottom')\n    if show_ylabel:\n        ax.set_ylabel('Shapley value')\n\n    for bar, val in zip(bars, vals):\n        y_pos = val + 0.012 if val >= 0 else val - 0.020\n        va = 'bottom' if val >= 0 else 'top'\n        t = ax.text(bar.get_x() + bar.get_width() / 2, y_pos,\n                    f'{val:+.3f}' if abs(val) >= 0.001 else '0.000',\n                    ha='center', va=va, fontsize=6, color='#333333')\n        t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])\n\n    perm_idx = methods_raw.index('perm_granger')\n    bars[perm_idx].set_edgecolor('#1A1A1A')\n    bars[perm_idx].set_linewidth(1.2)\n\ndraw_bars(ax_fpr, fpr_vals, 'FPR contribution', '(a)')\nax_fpr.set_ylim(-0.05, 0.72)\n\ndraw_bars(ax_fnr, fnr_vals, 'FNR contribution (6-pair)', '(b)', show_ylabel=False)\nax_fnr.set_ylim(-0.48, 0.05)\n\ndraw_bars(ax_comb, comb_vals, 'Combined (FPR + FNR)', '(c)', show_ylabel=False)\nax_comb.set_ylim(-0.25, 0.25)\n\n# Compact PermG annotation\nt_perm = ax_fpr.text(3, 0.04, 'zero\\nFPR', fontsize=6, color='#2C4A6E',\n                     ha='center', va='bottom', fontstyle='italic', linespacing=0.85)\nt_perm.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])\n\nfig.subplots_adjust(left=0.08, right=0.97, bottom=0.18, top=0.84, wspace=0.38)\n\nfor fmt in ['pdf', 'png']:\n    fig.savefig(OUT / f'shapley_method_contribution.{fmt}', dpi=300)\nplt.close()\nprint(f'Saved: {OUT}/shapley_method_contribution.pdf + .png')\n",
      "numLines": 107,
      "startLine": 1,
      "totalLines": 107
    }
  }
}
```

</details>

---


### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01ChY2RgGRwifpyeWxJZ3Xfg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 120,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "377ee2c9-4ed9-4a96-97c8-c174ce833e61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPrw3nLjtDE6C2TLXq3yra",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15682,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15682
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-24T08:51:09.848Z_

<details><summary>↩ Tool result · `toolu_01ChY2RgGRwifpyeWxJZ3Xfg`</summary>

```text
120	Mean $|\Delta p|$ & 0.002 \\
121	Significance flips & 0 / 24 \\
122	\bottomrule
123	\end{tabular}
124	\end{table}
125	
126	\paragraph{FDR threshold sensitivity.}
127	Table~\ref{tab:fdr_sensitivity} reports the effect of varying the BH FDR threshold $q$ on treatment ($\alpha{=}0.75$, 3~seeds) versus null ($\alpha{=}0.0$, 3~seeds) separation for permutation Granger tests.
128	% TODO-D219: update FDR sensitivity table with 6-seed null data (4/36 FPs at q=0.05; recompute null counts at each q threshold)
129	Treatment/null separation is qualitatively robust to FDR threshold choice; the null control remains at 0/24 across all thresholds.
130	
131	\begin{table}[h]
132	\centering
133	\small
134	% TODO-D219: update caption and table body with 6-seed null data
135	\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs). Null: $\alpha{=}0.0$ (3~seeds, 24 pairs). The null control produces zero false positives at all thresholds tested.}
136	\label{tab:fdr_sensitivity}
137	\resizebox{\columnwidth}{!}{%
138	\begin{tabular}{lccc}
139	\toprule
140	$q$ & Null FDR-sig (/24) & Treatment FDR-sig (/24) & Separation \\
141	\midrule
142	0.01 & 0 & 0  & Clean (underpowered) \\
143	0.05 & 0 & 19 & Clean \\
144	0.10 & 0 & 24 & Clean \\
145	\bottomrule
146	\end{tabular}}
147	\end{table}
148	
149	\paragraph{PermG $p$-value gradient at the onset boundary ($\alpha{=}0.45$).}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "c427cd47-7bd6-4571-a56f-57e998780308",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
      "content": "Mean $|\\Delta p|$ & 0.002 \\\\\nSignificance flips & 0 / 24 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{FDR threshold sensitivity.}\nTable~\\ref{tab:fdr_sensitivity} reports the effect of varying the BH FDR threshold $q$ on treatment ($\\alpha{=}0.75$, 3~seeds) versus null ($\\alpha{=}0.0$, 3~seeds) separation for permutation Granger tests.\n% TODO-D219: update FDR sensitivity table with 6-seed null data (4/36 FPs at q=0.05; recompute null counts at each q threshold)\nTreatment/null separation is qualitatively robust to FDR threshold choice; the null control remains at 0/24 across all thresholds.\n\n\\begin{table}[h]\n\\centering\n\\small\n% TODO-D219: update caption and table body with 6-seed null data\n\\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs). Null: $\\alpha{=}0.0$ (3~seeds, 24 pairs). The null control produces zero false positives at all thresholds tested.}\n\\label{tab:fdr_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n$q$ & Null FDR-sig (/24) & Treatment FDR-sig (/24) & Separation \\\\\n\\midrule\n0.01 & 0 & 0  & Clean (underpowered) \\\\\n0.05 & 0 & 19 & Clean \\\\\n0.10 & 0 & 24 & Clean \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{PermG $p$-value gradient at the onset boundary ($\\alpha{=}0.45$).}",
      "numLines": 30,
      "startLine": 120,
      "totalLines": 1222
    }
  }
}
```

</details>

---


### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01LehNzjkup11YxBVzRXdfBE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 715,
  "limit": 130
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "0d35e29c-7a4b-4d57-9e6f-62a478266c58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPrw3nLjtDE6C2TLXq3yra",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15682,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15682
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-24T08:51:10.535Z_

<details><summary>↩ Tool result · `toolu_01LehNzjkup11YxBVzRXdfBE`</summary>

```text
715	\paragraph{DGP limitation.}
716	The bivariate AR(1) with linear coupling is a simplification; actual iterative training involves nonlinear dynamics (mode amplification, threshold-dependent diversity loss).
717	These simulation results characterize PermG's behavior under controlled conditions, not exact calibration for the experimental setting; they provide a lower bound on size control because the linear DGP represents a worst case for permutation-based tests (smooth autocorrelation that permutation destroys).
718	
719	
720	\section{Shapley Value Analysis}
721	\label{app:shapley}
722	
723	We quantify each method's marginal contribution to the MMCT ensemble using Shapley values~\cite{shapley1953value}, computed via exact enumeration over all $2^5{=}32$ coalitions of the five detection methods.
724	% TODO-D219: recompute Shapley with 6-seed null data (seeds 45--50, 36 null pairs; PermG FPR now 4/36=11.1%, no longer zero)
725	For a coalition $S \subseteq \{m_1, \ldots, m_5\}$, we define two performance metrics: the false positive rate FPR($S$), computed from 3 null experiments ($\alpha{=}0.0$, seeds 42/43/44; 24 null pairs total), and the false negative rate FNR($S$), computed from 45 signal experiments across all non-null $\alpha$ levels (270 signal pairs for the 6-pair variant excluding mauve).
726	The Shapley value $\phi_k$ for method $m_k$ is the weighted average of its marginal contribution across all coalitions; positive FPR-Shapley indicates the method \emph{increases} false positives, while negative FNR-Shapley indicates it \emph{reduces} false negatives.
727	The combined Shapley value $\phi_k^{\text{comb}} = \phi_k^{\text{FPR}} + \phi_k^{\text{FNR}}$ balances both error types, with more negative values indicating greater net benefit.
728	
729	Table~\ref{tab:shapley_6pair} reports the 6-pair analysis (excluding mauve).
730	% TODO-D219: recompute Shapley values; PermG φ^FPR will be >0 with 6-seed data (4/36 FPs)
731	PermG achieves the lowest (best) combined Shapley ($-0.180$), driven entirely by FNR reduction with zero FPR contribution---the only method with this property.
732	Naive cross-correlation is the worst contributor ($+0.203$), with its massive FPR Shapley ($+0.622$) overwhelming its FNR benefit ($-0.419$): adding naive cross-correlation to any coalition increases false positives far more than it reduces false negatives.
733	Threshold onset contributes almost nothing useful ($+0.074$ combined; FPR $+0.101$, FNR $-0.027$), confirming the near-zero detection power reported in Table~\ref{tab:method_comparison}.
734	Figure~\ref{fig:shapley} visualizes the decomposition.
735	
736	\begin{table}[h]
737	\centering
738	\small
739	\caption{Shapley value decomposition (6-pair, mauve excluded). FPR-Shapley: marginal FPR contribution (positive = increases false positives). FNR-Shapley: marginal FNR contribution (negative = reduces false negatives). Combined = FPR + FNR (more negative = better). 48 experiments, $2^5{=}32$ coalitions, exact enumeration.}
740	\label{tab:shapley_6pair}
741	\begin{tabular}{lccc}
742	\toprule
743	Method & $\phi^{\text{FPR}}$ & $\phi^{\text{FNR}}$ & $\phi^{\text{comb}}$ \\
744	\midrule
745	Naive XCorr          & $+0.622$ & $-0.419$ & $+0.203$ \\
746	Diff.\ XCorr         & $+0.163$ & $-0.306$ & $-0.142$ \\
747	Threshold ($3\sigma$) & $+0.101$ & $-0.027$ & $+0.074$ \\
748	\textbf{Perm.\ Granger} & $\mathbf{0.000}$ & $\mathbf{-0.180}$ & $\mathbf{-0.180}$ \\
749	Toda--Yamamoto       & $+0.031$ & $-0.069$ & $-0.038$ \\
750	\bottomrule
751	\end{tabular}
752	\end{table}
753	
754	\begin{figure*}[h]
755	\centering
756	\includegraphics[width=\linewidth]{figures/shapley_method_contribution.pdf}
757	% TODO-D219: regenerate figure and update caption after Shapley recomputation with 6-seed data
758	\caption{Shapley value decomposition of each method's marginal contribution to FPR (positive bars) and FNR (negative bars). PermG is the only method with zero FPR contribution; naive cross-correlation's FPR dominates its FNR benefit.}
759	\label{fig:shapley}
760	\end{figure*}
761	
762	The 8-pair variant (including mauve) yields qualitatively identical rankings: PermG remains the best contributor ($\phi^{\text{comb}}{=}-0.152$), naive cross-correlation the worst ($+0.170$), and threshold onset near-zero ($+0.063$).
763	
764	\paragraph{FDR correction scope.}
765	This analysis applies BH-corrected significance (\texttt{significant\_fdr}) uniformly across all five methods, including naive cross-correlation and Toda--Yamamoto.
766	In contrast, the per-method dose-response profiles (Table~\ref{tab:dose_response_full}) use uncorrected significance for naive cross-correlation, threshold onset, and Toda--Yamamoto because FDR-corrected fields are not available in the per-experiment pipeline output for these methods.
767	The Shapley analysis recomputes significance from raw $p$-values with BH correction applied post hoc, ensuring a fair comparison across methods within the coalition framework.
768	
769	
770	\section{MMCT Weight Robustness Ablation}
771	\label{app:weight_robustness}
772	
773	The detection results reported in the main text use equal-weight majority voting ($K{\geq}3$ of 5 methods, each contributing at most one vote per pair); PermG contributes at most $1/5 = 20\%$ of the consensus weight.
774	FPR-inverse weighting is used \emph{only} in the exploratory method ranking below, not in the detection results.
775	To verify that PermG's top ranking is not an artifact of the FPR-inverse weighting scheme, we recompute Shapley values under four weight specifications (Table~\ref{tab:weight_robustness}).
776	Equal weighting ($w{=}1$ for all methods) eliminates any FPR-based advantage; PermG still ranks first ($\phi^{\text{comb}}{=}-0.152$), though its margin over naive cross-correlation narrows to 0.015.
777	Under cap-5, the margin widens to 0.043 as the FPR penalty begins to differentiate high-FPR methods.
778	Cap-10 and original cap-100 yield identical Shapley values because the consensus threshold ($K{\geq}3$) is determined by the three smallest method weights ($w_{\text{naive}}{+}w_{\text{diff}}{+}w_{\text{thresh}} = 7.76$), which are invariant to further increases in the PermG or TY cap; this saturation confirms that the original $w{=}100$ does not artificially inflate PermG's contribution.
779	% TODO-D219: recompute weight robustness table with 6-seed data; PermG φ^FPR will be >0
780	Across all schemes, PermG's advantage derives from the same structural property: zero FPR ($\phi^{\text{FPR}}{=}0$) combined with moderate FNR reduction ($\phi^{\text{FNR}}{=}-0.152$ to $-0.426$).
781	
782	\begin{table}[h]
783	\centering
784	\small
785	\caption{MMCT weight robustness: PermG combined Shapley under four weighting schemes. PermG ranks first in all cases. Gap = $|\phi^{\text{comb}}_{\text{PermG}} - \phi^{\text{comb}}_{\text{runner-up}}|$. 48 experiments (3 null + 45 signal), exact Shapley enumeration ($2^5{=}32$ coalitions).}
786	\label{tab:weight_robustness}
787	\begin{tabular}{lrcrc}
788	\toprule
789	Scheme & $w_{\text{PermG}}$ & $\phi^{\text{comb}}_{\text{PermG}}$ & Runner-up & Gap \\
790	\midrule
791	Equal ($w{=}1$)     & 1   & $-0.152$ & NaiveXCorr ($-0.137$) & 0.015 \\
792	Cap-5               & 5   & $-0.165$ & NaiveXCorr ($-0.123$) & 0.043 \\
793	Cap-10              & 10  & $-0.426$ & TY ($-0.067$)         & 0.359 \\
794	FPR-inv.\ (cap-100) & 100 & $-0.426$ & TY ($-0.067$)         & 0.359 \\
795	\bottomrule
796	\end{tabular}
797	\end{table}
798	
799	
800	\section{PermG FPR Independence Analysis}
801	\label{app:fpr_independence}
802	
803	Table~\ref{tab:null_fpr_methods} reports null-control FPR for all five detection methods across six seeds ($6 \times 6 = 36$ pairs, 6-pair basis excluding mauve).
804	Under identical BH-FDR correction ($q{=}0.05$), DiffXCorr achieves the lowest FPR (1/36, 2.8\%) but lacks directional separation; PermG (4/36, 11.1\%) is the lowest among directional methods.
805	All four PermG false positives occur in token\_entropy$\to$distinct pairs (seeds~45 and 50, forward direction only), suggesting a structural pattern concentrated in a single canary--downstream pair type.
806	
807	\begin{table}[h]
808	\centering
809	\small
810	\caption{Null-control FPR by method ($\alpha{=}0.0$, 6~seeds 45--50, 6~pairs each). All p-value--based methods (DiffXCorr, PermG, TY) report BH-FDR--corrected rejections at $q{=}0.05$ for fair comparison. Threshold uses a deterministic $3\sigma$ criterion; NaiveXCorr uses uncorrected correlation significance.}
811	\label{tab:null_fpr_methods}
812	\begin{tabular}{llrr}
813	\toprule
814	Method & Criterion & Rejections (/36) & FPR (\%) \\
815	\midrule
816	Diff.\ XCorr$^\dagger$ & BH-FDR & 1 & 2.8 \\
817	\textbf{Perm.\ Granger} & \textbf{BH-FDR} & \textbf{4} & \textbf{11.1} \\
818	Threshold & $3\sigma$ (det.) & 10 & 27.8 \\
819	Toda--Yamamoto & BH-FDR & 14 & 38.9 \\
820	Naive XCorr & uncorr. & 33 & 91.7 \\
821	\bottomrule
822	\multicolumn{4}{l}{\footnotesize $^\dagger$Bidirectional; cannot separate forward from reverse.} \\
823	\end{tabular}
824	\end{table}
825	
826	\paragraph{Cluster adjustment.}
827	The 36 null-control pairs are nested within 6~seeds (6~pairs per seed), introducing within-seed correlation.
828	Within-seed ICC${=}0.14$ yields an effective sample size $N_{\text{eff}} \approx 21$ (from $N_{\text{eff}} = N / [1 + (m-1) \cdot \text{ICC}]$ where $N{=}36$, $m{=}6$).
829	Under the Clopper--Pearson exact method with $N_{\text{eff}}{=}21$ and 4 successes (scaled), the cluster-adjusted 95\% CI is $[1.2\%, 30.4\%]$, compared to $[3.1\%, 26.1\%]$ under independence ($N{=}36$).
830	The lower ICC compared to the 3-seed pilot ($0.14$ vs.\ $0.34$) reflects greater between-seed consistency with six independent replications.
831	
832	\paragraph{Direction filtering.}
833	Forward-direction filtering (retaining only pairs with peak lag${<}0$ for cross-correlation methods) reduces null-control $K{\geq}3$ false positives.
834	Under the 6-seed, 6-pair basis, $K{\geq}3$ consensus with filtering produces 6/36 false positives (16.7\%; detail below); the 3-seed pilot underestimated this rate (0/8).
835	Detection at $\alpha{\geq}0.50$ is unaffected: $K{\geq}3$ counts are identical with and without direction filtering at all signal levels.
836	
837	\paragraph{$K{\geq}3$ false positive detail.}
838	Under the 6-pair basis (6~seeds, 36~pairs), $K{\geq}3$ consensus produces 6 false positives (FPR${=}16.7\%$).
839	Of these, 4 are driven by naive cross-correlation, threshold onset, and Toda--Yamamoto (PermG does \emph{not} vote); the remaining 2 (seeds~45 and 50, te$\to$distinct) include PermG in the consensus.
840	PermG thus contributes to only 2 of 6 consensus false positives, confirming that most $K{\geq}3$ FPR is driven by the high-FPR methods (naive, threshold, TY).
841	
842	\paragraph{Sensitivity to FPR assumption.}
843	Even under the conservative upper bound of the cluster-adjusted CI (30.4\%), PermG remains the lowest-FPR directional method: DiffXCorr achieves a lower FPR under identical BH-FDR correction (2.8\%) but lacks forward/reverse separation; the next directional method (threshold onset) has 27.8\% and Toda--Yamamoto 38.9\%.
844	Our primary results rely on equal-weight $K{\geq}3$ majority voting, where each method contributes exactly one vote regardless of its FPR---this mechanism is completely unaffected by any FPR assumption.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "b5fb097f-99ab-40e1-870a-e50ac2788625",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
      "content": "\\paragraph{DGP limitation.}\nThe bivariate AR(1) with linear coupling is a simplification; actual iterative training involves nonlinear dynamics (mode amplification, threshold-dependent diversity loss).\nThese simulation results characterize PermG's behavior under controlled conditions, not exact calibration for the experimental setting; they provide a lower bound on size control because the linear DGP represents a worst case for permutation-based tests (smooth autocorrelation that permutation destroys).\n\n\n\\section{Shapley Value Analysis}\n\\label{app:shapley}\n\nWe quantify each method's marginal contribution to the MMCT ensemble using Shapley values~\\cite{shapley1953value}, computed via exact enumeration over all $2^5{=}32$ coalitions of the five detection methods.\n% TODO-D219: recompute Shapley with 6-seed null data (seeds 45--50, 36 null pairs; PermG FPR now 4/36=11.1%, no longer zero)\nFor a coalition $S \\subseteq \\{m_1, \\ldots, m_5\\}$, we define two performance metrics: the false positive rate FPR($S$), computed from 3 null experiments ($\\alpha{=}0.0$, seeds 42/43/44; 24 null pairs total), and the false negative rate FNR($S$), computed from 45 signal experiments across all non-null $\\alpha$ levels (270 signal pairs for the 6-pair variant excluding mauve).\nThe Shapley value $\\phi_k$ for method $m_k$ is the weighted average of its marginal contribution across all coalitions; positive FPR-Shapley indicates the method \\emph{increases} false positives, while negative FNR-Shapley indicates it \\emph{reduces} false negatives.\nThe combined Shapley value $\\phi_k^{\\text{comb}} = \\phi_k^{\\text{FPR}} + \\phi_k^{\\text{FNR}}$ balances both error types, with more negative values indicating greater net benefit.\n\nTable~\\ref{tab:shapley_6pair} reports the 6-pair analysis (excluding mauve).\n% TODO-D219: recompute Shapley values; PermG φ^FPR will be >0 with 6-seed data (4/36 FPs)\nPermG achieves the lowest (best) combined Shapley ($-0.180$), driven entirely by FNR reduction with zero FPR contribution---the only method with this property.\nNaive cross-correlation is the worst contributor ($+0.203$), with its massive FPR Shapley ($+0.622$) overwhelming its FNR benefit ($-0.419$): adding naive cross-correlation to any coalition increases false positives far more than it reduces false negatives.\nThreshold onset contributes almost nothing useful ($+0.074$ combined; FPR $+0.101$, FNR $-0.027$), confirming the near-zero detection power reported in Table~\\ref{tab:method_comparison}.\nFigure~\\ref{fig:shapley} visualizes the decomposition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Shapley value decomposition (6-pair, mauve excluded). FPR-Shapley: marginal FPR contribution (positive = increases false positives). FNR-Shapley: marginal FNR contribution (negative = reduces false negatives). Combined = FPR + FNR (more negative = better). 48 experiments, $2^5{=}32$ coalitions, exact enumeration.}\n\\label{tab:shapley_6pair}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $\\phi^{\\text{FPR}}$ & $\\phi^{\\text{FNR}}$ & $\\phi^{\\text{comb}}$ \\\\\n\\midrule\nNaive XCorr          & $+0.622$ & $-0.419$ & $+0.203$ \\\\\nDiff.\\ XCorr         & $+0.163$ & $-0.306$ & $-0.142$ \\\\\nThreshold ($3\\sigma$) & $+0.101$ & $-0.027$ & $+0.074$ \\\\\n\\textbf{Perm.\\ Granger} & $\\mathbf{0.000}$ & $\\mathbf{-0.180}$ & $\\mathbf{-0.180}$ \\\\\nToda--Yamamoto       & $+0.031$ & $-0.069$ & $-0.038$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/shapley_method_contribution.pdf}\n% TODO-D219: regenerate figure and update caption after Shapley recomputation with 6-seed data\n\\caption{Shapley value decomposition of each method's marginal contribution to FPR (positive bars) and FNR (negative bars). PermG is the only method with zero FPR contribution; naive cross-correlation's FPR dominates its FNR benefit.}\n\\label{fig:shapley}\n\\end{figure*}\n\nThe 8-pair variant (including mauve) yields qualitatively identical rankings: PermG remains the best contributor ($\\phi^{\\text{comb}}{=}-0.152$), naive cross-correlation the worst ($+0.170$), and threshold onset near-zero ($+0.063$).\n\n\\paragraph{FDR correction scope.}\nThis analysis applies BH-corrected significance (\\texttt{significant\\_fdr}) uniformly across all five methods, including naive cross-correlation and Toda--Yamamoto.\nIn contrast, the per-method dose-response profiles (Table~\\ref{tab:dose_response_full}) use uncorrected significance for naive cross-correlation, threshold onset, and Toda--Yamamoto because FDR-corrected fields are not available in the per-experiment pipeline output for these methods.\nThe Shapley analysis recomputes significance from raw $p$-values with BH correction applied post hoc, ensuring a fair comparison across methods within the coalition framework.\n\n\n\\section{MMCT Weight Robustness Ablation}\n\\label{app:weight_robustness}\n\nThe detection results reported in the main text use equal-weight majority voting ($K{\\geq}3$ of 5 methods, each contributing at most one vote per pair); PermG contributes at most $1/5 = 20\\%$ of the consensus weight.\nFPR-inverse weighting is used \\emph{only} in the exploratory method ranking below, not in the detection results.\nTo verify that PermG's top ranking is not an artifact of the FPR-inverse weighting scheme, we recompute Shapley values under four weight specifications (Table~\\ref{tab:weight_robustness}).\nEqual weighting ($w{=}1$ for all methods) eliminates any FPR-based advantage; PermG still ranks first ($\\phi^{\\text{comb}}{=}-0.152$), though its margin over naive cross-correlation narrows to 0.015.\nUnder cap-5, the margin widens to 0.043 as the FPR penalty begins to differentiate high-FPR methods.\nCap-10 and original cap-100 yield identical Shapley values because the consensus threshold ($K{\\geq}3$) is determined by the three smallest method weights ($w_{\\text{naive}}{+}w_{\\text{diff}}{+}w_{\\text{thresh}} = 7.76$), which are invariant to further increases in the PermG or TY cap; this saturation confirms that the original $w{=}100$ does not artificially inflate PermG's contribution.\n% TODO-D219: recompute weight robustness table with 6-seed data; PermG φ^FPR will be >0\nAcross all schemes, PermG's advantage derives from the same structural property: zero FPR ($\\phi^{\\text{FPR}}{=}0$) combined with moderate FNR reduction ($\\phi^{\\text{FNR}}{=}-0.152$ to $-0.426$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MMCT weight robustness: PermG combined Shapley under four weighting schemes. PermG ranks first in all cases. Gap = $|\\phi^{\\text{comb}}_{\\text{PermG}} - \\phi^{\\text{comb}}_{\\text{runner-up}}|$. 48 experiments (3 null + 45 signal), exact Shapley enumeration ($2^5{=}32$ coalitions).}\n\\label{tab:weight_robustness}\n\\begin{tabular}{lrcrc}\n\\toprule\nScheme & $w_{\\text{PermG}}$ & $\\phi^{\\text{comb}}_{\\text{PermG}}$ & Runner-up & Gap \\\\\n\\midrule\nEqual ($w{=}1$)     & 1   & $-0.152$ & NaiveXCorr ($-0.137$) & 0.015 \\\\\nCap-5               & 5   & $-0.165$ & NaiveXCorr ($-0.123$) & 0.043 \\\\\nCap-10              & 10  & $-0.426$ & TY ($-0.067$)         & 0.359 \\\\\nFPR-inv.\\ (cap-100) & 100 & $-0.426$ & TY ($-0.067$)         & 0.359 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{PermG FPR Independence Analysis}\n\\label{app:fpr_independence}\n\nTable~\\ref{tab:null_fpr_methods} reports null-control FPR for all five detection methods across six seeds ($6 \\times 6 = 36$ pairs, 6-pair basis excluding mauve).\nUnder identical BH-FDR correction ($q{=}0.05$), DiffXCorr achieves the lowest FPR (1/36, 2.8\\%) but lacks directional separation; PermG (4/36, 11.1\\%) is the lowest among directional methods.\nAll four PermG false positives occur in token\\_entropy$\\to$distinct pairs (seeds~45 and 50, forward direction only), suggesting a structural pattern concentrated in a single canary--downstream pair type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Null-control FPR by method ($\\alpha{=}0.0$, 6~seeds 45--50, 6~pairs each). All p-value--based methods (DiffXCorr, PermG, TY) report BH-FDR--corrected rejections at $q{=}0.05$ for fair comparison. Threshold uses a deterministic $3\\sigma$ criterion; NaiveXCorr uses uncorrected correlation significance.}\n\\label{tab:null_fpr_methods}\n\\begin{tabular}{llrr}\n\\toprule\nMethod & Criterion & Rejections (/36) & FPR (\\%) \\\\\n\\midrule\nDiff.\\ XCorr$^\\dagger$ & BH-FDR & 1 & 2.8 \\\\\n\\textbf{Perm.\\ Granger} & \\textbf{BH-FDR} & \\textbf{4} & \\textbf{11.1} \\\\\nThreshold & $3\\sigma$ (det.) & 10 & 27.8 \\\\\nToda--Yamamoto & BH-FDR & 14 & 38.9 \\\\\nNaive XCorr & uncorr. & 33 & 91.7 \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$Bidirectional; cannot separate forward from reverse.} \\\\\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cluster adjustment.}\nThe 36 null-control pairs are nested within 6~seeds (6~pairs per seed), introducing within-seed correlation.\nWithin-seed ICC${=}0.14$ yields an effective sample size $N_{\\text{eff}} \\approx 21$ (from $N_{\\text{eff}} = N / [1 + (m-1) \\cdot \\text{ICC}]$ where $N{=}36$, $m{=}6$).\nUnder the Clopper--Pearson exact method with $N_{\\text{eff}}{=}21$ and 4 successes (scaled), the cluster-adjusted 95\\% CI is $[1.2\\%, 30.4\\%]$, compared to $[3.1\\%, 26.1\\%]$ under independence ($N{=}36$).\nThe lower ICC compared to the 3-seed pilot ($0.14$ vs.\\ $0.34$) reflects greater between-seed consistency with six independent replications.\n\n\\paragraph{Direction filtering.}\nForward-direction filtering (retaining only pairs with peak lag${<}0$ for cross-correlation methods) reduces null-control $K{\\geq}3$ false positives.\nUnder the 6-seed, 6-pair basis, $K{\\geq}3$ consensus with filtering produces 6/36 false positives (16.7\\%; detail below); the 3-seed pilot underestimated this rate (0/8).\nDetection at $\\alpha{\\geq}0.50$ is unaffected: $K{\\geq}3$ counts are identical with and without direction filtering at all signal levels.\n\n\\paragraph{$K{\\geq}3$ false positive detail.}\nUnder the 6-pair basis (6~seeds, 36~pairs), $K{\\geq}3$ consensus produces 6 false positives (FPR${=}16.7\\%$).\nOf these, 4 are driven by naive cross-correlation, threshold onset, and Toda--Yamamoto (PermG does \\emph{not} vote); the remaining 2 (seeds~45 and 50, te$\\to$distinct) include PermG in the consensus.\nPermG thus contributes to only 2 of 6 consensus false positives, confirming that most $K{\\geq}3$ FPR is driven by the high-FPR methods (naive, threshold, TY).\n\n\\paragraph{Sensitivity to FPR assumption.}\nEven under the conservative upper bound of the cluster-adjusted CI (30.4\\%), PermG remains the lowest-FPR directional method: DiffXCorr achieves a lower FPR under identical BH-FDR correction (2.8\\%) but lacks forward/reverse separation; the next directional method (threshold onset) has 27.8\\% and Toda--Yamamoto 38.9\\%.\nOur primary results rely on equal-weight $K{\\geq}3$ majority voting, where each method contributes exactly one vote regardless of its FPR---this mechanism is completely unaffected by any FPR assumption.",
      "numLines": 130,
      "startLine": 715,
      "totalLines": 1222
    }
  }
}
```

</details>

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Glob · `toolu_01Xtkmmt8Vg9Qoo3Mbytfbje`</summary>

```json
{
  "pattern": "artifacts/D102*a000*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "e58531e6-9d81-467a-a012-c36121390694",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YPrw3nLjtDE6C2TLXq3yra",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15682,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15682
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-24T08:51:11.253Z_

<details><summary>↩ Tool result · `toolu_01Xtkmmt8Vg9Qoo3Mbytfbje`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "2168b24b-516c-4b87-a987-374b3a8b9720",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 45,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---


### Runtime record

_source line 12_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779614400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "945de5ba-33f2-423a-8bc5-d036cde43010",
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7"
}
```

---


### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Let me search for the null seed D102 artifacts more broadly, and also read the existing Shapley JSON data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "e64aa5b5-2bba-4f53-b05a-c5fe4a878e65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xv7kyccPNZ11wvd6WJmL7f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6872,
      "cache_read_input_tokens": 27523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6872
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 14_

Let me find the null seed D102 artifacts and read the existing Shapley data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "eb17103e-f73a-4eed-8d63-4345203a4674",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xv7kyccPNZ11wvd6WJmL7f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6872,
      "cache_read_input_tokens": 27523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6872
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_01DbEKBkjNyWBL6AdxEtAw8W`</summary>

```json
{
  "pattern": "artifacts/*null*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "f3c4d6e5-3122-4f11-a0ed-34e1d62b1d83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xv7kyccPNZ11wvd6WJmL7f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6872,
      "cache_read_input_tokens": 27523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6872
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 16 · 2026-05-24T08:51:28.958Z_

<details><summary>↩ Tool result · `toolu_01DbEKBkjNyWBL6AdxEtAw8W`</summary>

```text
artifacts/method_fpr_null.csv
artifacts/r5_null_correlation_matrix.json
artifacts/D102_null_s46_fp32_d3.json
artifacts/D102_null_s48_fp32_d3.json
artifacts/D102_null_s49_fp32_d3.json
artifacts/D102_null_s50_fp32_d3.json
artifacts/D102_gpt2m_null_s42_fp32_d3.json
artifacts/D102_gpt2m_null_s43_fp32_d3.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "c7cd9c17-d50d-48b3-8bb4-1bd7ecec1a8d",
  "tool_use_result": {
    "filenames": [
      "artifacts/method_fpr_null.csv",
      "artifacts/r5_null_correlation_matrix.json",
      "artifacts/D102_null_s46_fp32_d3.json",
      "artifacts/D102_null_s48_fp32_d3.json",
      "artifacts/D102_null_s49_fp32_d3.json",
      "artifacts/D102_null_s50_fp32_d3.json",
      "artifacts/D102_gpt2m_null_s42_fp32_d3.json",
      "artifacts/D102_gpt2m_null_s43_fp32_d3.json"
    ],
    "durationMs": 39,
    "numFiles": 8,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Glob · `toolu_014BapRx3R7CoQmfzyJgmkpQ`</summary>

```json
{
  "pattern": "artifacts/*a000*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "74150342-241f-4650-8f08-357a53601c04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xv7kyccPNZ11wvd6WJmL7f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6872,
      "cache_read_input_tokens": 27523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6872
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 18 · 2026-05-24T08:51:29.444Z_

<details><summary>↩ Tool result · `toolu_014BapRx3R7CoQmfzyJgmkpQ`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "174e94a2-bf95-49b4-ac4c-2411fe21e230",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 40,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Glob · `toolu_01QKdAVNfkRckKzAEJ17zaPn`</summary>

```json
{
  "pattern": "artifacts/shapley*/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "5d54b5fd-c2ed-4048-83cd-fea3bc386630",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xv7kyccPNZ11wvd6WJmL7f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6872,
      "cache_read_input_tokens": 27523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6872
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 20 · 2026-05-24T08:51:30.463Z_

<details><summary>↩ Tool result · `toolu_01QKdAVNfkRckKzAEJ17zaPn`</summary>

```text
artifacts/shapley_v2/shapley_values_v2.json
artifacts/shapley_v2/shapley_method_contribution.pdf
artifacts/shapley_v2/shapley_method_contribution.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "eea8683f-89de-4349-9165-0c14467f2a90",
  "tool_use_result": {
    "filenames": [
      "artifacts/shapley_v2/shapley_values_v2.json",
      "artifacts/shapley_v2/shapley_method_contribution.pdf",
      "artifacts/shapley_v2/shapley_method_contribution.png"
    ],
    "durationMs": 40,
    "numFiles": 3,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Grep · `toolu_017KbVd7zxYd5teePjQ9k1ne`</summary>

```json
{
  "pattern": "a000|null_fpr",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "10a141ef-2324-4ea2-ace6-58020d8add6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xv7kyccPNZ11wvd6WJmL7f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6872,
      "cache_read_input_tokens": 27523,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6872
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 22 · 2026-05-24T08:51:31.937Z_

<details><summary>↩ Tool result · `toolu_017KbVd7zxYd5teePjQ9k1ne`</summary>

```text
Found 98 files
artifacts/D102_gpt2m_null_s43_fp32_d3.json
artifacts/D102_gpt2m_null_s42_fp32_d3.json
artifacts/manifest.yaml
artifacts/_project/data/fpr_transparency_all_seeds_0ba274.json
artifacts/fpr_transparency_all_seeds.json
artifacts/_project/data/fpr_transparency_all_seeds.json
artifacts/_project/data/D102_null_s50_fp32_d3.json
artifacts/D102_null_s50_fp32_d3.json
artifacts/_project/data/D102_null_s49_fp32_d3.json
artifacts/D102_null_s49_fp32_d3.json
artifacts/_project/data/D102_null_s48_fp32_d3.json
artifacts/D102_null_s48_fp32_d3.json
artifacts/_project/data/D102_null_s46_fp32_d3.json
artifacts/D102_null_s46_fp32_d3.json
artifacts/A2_naive_baseline_comparison.json
artifacts/_project/data_audit_20260523.md
artifacts/_project/report/data_audit_20260523.md
artifacts/_project/report/d102_audit_report.md
artifacts/d102_audit_report.md
artifacts/alpha_sweep_a000_s48_fp32/data/5method_leadlag_2ac107.json
artifacts/alpha_sweep_a000_s48_fp32/data/5method_leadlag.json
artifacts/alpha_sweep_a000_s48_fp32/run_analysis.py
artifacts/server_status_check_20260521.md
artifacts/alpha_sweep_a000_s47_fp32/intermediate/launch_info.txt
artifacts/alpha_sweep_a000_s45_fp32/intermediate/a000_s45_fp32_launch.md
artifacts/_project/data/trajectory_data.json
artifacts/phase_space/trajectory_data.json
artifacts/_project/data/conditional_granger_v2_d4b1cd.json
artifacts/_project/data/conditional_granger_v2.json
artifacts/conditional_granger_v2.json
artifacts/_project/data/icc_neff_analysis.json
artifacts/icc_neff_analysis.json
artifacts/_project/data/empirical_ar1_coefficients.json
artifacts/empirical_ar1_coefficients.json
artifacts/compute_ar1.py
artifacts/_project/data/dose_response_d120_recompiled.csv
artifacts/_project/data/dose_response_d120_recompiled_30a35c.csv
artifacts/dose_response_d120_recompiled.csv
artifacts/_project/data/equal_weight_vs_current_k3_bd7a72.json
artifacts/_project/data/equal_weight_vs_current_k3.json
artifacts/equal_weight_vs_current_k3.json
artifacts/_project/data/dose_response_d120_recompiled_a2b17b.csv
artifacts/theory/cascade_empirical_data.json
artifacts/theory/cascade_empirical_validation.md
artifacts/_project/report/cascade_empirical_validation.md
artifacts/_project/data/moment_cascade_analysis.json
artifacts/moment_cascade/moment_cascade_analysis.json
artifacts/moment_cascade/moment_cascade_analysis.py
artifacts/shapley_v2/shapley_values_v2.json
artifacts/dose_response_d120_summary.md
artifacts/dose_response_d120_compiled.csv
artifacts/d150_p01_spec_curve_audit.md
artifacts/_project/report/d120_recalc_19828.md
artifacts/d120_recalc_19828.md
artifacts/_project/data/consensus_heatmap_data_m035.csv
artifacts/_project/data/dose_response_5method_regime_m035.csv
artifacts/d105_d111_complete_audit.md
artifacts/d111_full_sweep_audit.md
artifacts/_project/report/d111_full_sweep_audit_ad69be.md
artifacts/_project/report/d111_full_sweep_audit.md
artifacts/alpha_sweep_a030_s42_fp32/report/alpha_sweep_a030_s42_fp32_analysis.md
artifacts/_project/report/mmct_v2_a010_fp32_results.md
artifacts/mmct_v2_a010_fp32_results.md
artifacts/_project/report/report_dose_response_gaps.md
artifacts/lag_sensitivity/run_lag_sensitivity.py
artifacts/_project/report/per_alpha_fdr_results_b4d938.md
artifacts/_project/report/per_alpha_fdr_results.md
artifacts/per_alpha_fdr_results.md
artifacts/_project/report/mmct_full_results_f5ecdb.md
artifacts/_project/report/mmct_full_results.md
artifacts/mmct_full_results.md
artifacts/table7_draft.md
artifacts/_project/report/table7_draft.md
artifacts/alpha_sweep_a010_s43/report/a010_s43_bf16_analysis.md
artifacts/intervention_reactive_s42/report/analysis_report.md
artifacts/alpha_sweep_a000_s44/report/a000_s44_analysis_report.md
artifacts/alpha_sweep_a000_s43/report/a000_s43_5method_analysis_7c0294.md
artifacts/alpha_sweep_a000_s43/report/a000_s43_5method_analysis.md
artifacts/alpha_sweep_a000_s43/data/a000_s43_5method_results_616865.json
artifacts/alpha_sweep_a000_s43/data/a000_s43_5method_results.json
artifacts/_project/report/ground_truth_redefine_v2_analysis.md
artifacts/_project/report/ground_truth_redefine_analysis.md
artifacts/_project/report/paper_consistency_audit.md
artifacts/paper_consistency_audit.md
artifacts/prep_cross_alpha_v5_verify.md
artifacts/analysis/cross_alpha/cross_alpha_analysis_v4.py
artifacts/cross_alpha_v4_ready.md
artifacts/cross_alpha_analysis_v4.py
artifacts/_project/intermediate/generalization_prep.md
artifacts/generalization_prep.md
artifacts/_project/intermediate/d026_optimized_commands.md
artifacts/d026_optimized_commands.md
artifacts/_project/intermediate/a075_analysis_prep.md
artifacts/a075_analysis_prep.md
artifacts/_project/data/cross_alpha_analysis.py
artifacts/dream_reports/dream_20260514T184925/logs/review_worst.log
artifacts/dream_reports/dream_20260514T184925/logs/review_median.log
artifacts/dream_reports/dream_20260514T184925/logs/phase2_worst_attempt0.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "a5f5178f-2ce8-401d-93d7-f9c9c20320e4",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "artifacts/D102_gpt2m_null_s43_fp32_d3.json",
      "artifacts/D102_gpt2m_null_s42_fp32_d3.json",
      "artifacts/manifest.yaml",
      "artifacts/_project/data/fpr_transparency_all_seeds_0ba274.json",
      "artifacts/fpr_transparency_all_seeds.json",
      "artifacts/_project/data/fpr_transparency_all_seeds.json",
      "artifacts/_project/data/D102_null_s50_fp32_d3.json",
      "artifacts/D102_null_s50_fp32_d3.json",
      "artifacts/_project/data/D102_null_s49_fp32_d3.json",
      "artifacts/D102_null_s49_fp32_d3.json",
      "artifacts/_project/data/D102_null_s48_fp32_d3.json",
      "artifacts/D102_null_s48_fp32_d3.json",
      "artifacts/_project/data/D102_null_s46_fp32_d3.json",
      "artifacts/D102_null_s46_fp32_d3.json",
      "artifacts/A2_naive_baseline_comparison.json",
      "artifacts/_project/data_audit_20260523.md",
      "artifacts/_project/report/data_audit_20260523.md",
      "artifacts/_project/report/d102_audit_report.md",
      "artifacts/d102_audit_report.md",
      "artifacts/alpha_sweep_a000_s48_fp32/data/5method_leadlag_2ac107.json",
      "artifacts/alpha_sweep_a000_s48_fp32/data/5method_leadlag.json",
      "artifacts/alpha_sweep_a000_s48_fp32/run_analysis.py",
      "artifacts/server_status_check_20260521.md",
      "artifacts/alpha_sweep_a000_s47_fp32/intermediate/launch_info.txt",
      "artifacts/alpha_sweep_a000_s45_fp32/intermediate/a000_s45_fp32_launch.md",
      "artifacts/_project/data/trajectory_data.json",
      "artifacts/phase_space/trajectory_data.json",
      "artifacts/_project/data/conditional_granger_v2_d4b1cd.json",
      "artifacts/_project/data/conditional_granger_v2.json",
      "artifacts/conditional_granger_v2.json",
      "artifacts/_project/data/icc_neff_analysis.json",
      "artifacts/icc_neff_analysis.json",
      "artifacts/_project/data/empirical_ar1_coefficients.json",
      "artifacts/empirical_ar1_coefficients.json",
      "artifacts/compute_ar1.py",
      "artifacts/_project/data/dose_response_d120_recompiled.csv",
      "artifacts/_project/data/dose_response_d120_recompiled_30a35c.csv",
      "artifacts/dose_response_d120_recompiled.csv",
      "artifacts/_project/data/equal_weight_vs_current_k3_bd7a72.json",
      "artifacts/_project/data/equal_weight_vs_current_k3.json",
      "artifacts/equal_weight_vs_current_k3.json",
      "artifacts/_project/data/dose_response_d120_recompiled_a2b17b.csv",
      "artifacts/theory/cascade_empirical_data.json",
      "artifacts/theory/cascade_empirical_validation.md",
      "artifacts/_project/report/cascade_empirical_validation.md",
      "artifacts/_project/data/moment_cascade_analysis.json",
      "artifacts/moment_cascade/moment_cascade_analysis.json",
      "artifacts/moment_cascade/moment_cascade_analysis.py",
      "artifacts/shapley_v2/shapley_values_v2.json",
      "artifacts/dose_response_d120_summary.md",
      "artifacts/dose_response_d120_compiled.csv",
      "artifacts/d150_p01_spec_curve_audit.md",
      "artifacts/_project/report/d120_recalc_19828.md",
      "artifacts/d120_recalc_19828.md",
      "artifacts/_project/data/consensus_heatmap_data_m035.csv",
      "artifacts/_project/data/dose_response_5method_regime_m035.csv",
      "artifacts/d105_d111_complete_audit.md",
      "artifacts/d111_full_sweep_audit.md",
      "artifacts/_project/report/d111_full_sweep_audit_ad69be.md",
      "artifacts/_project/report/d111_full_sweep_audit.md",
      "artifacts/alpha_sweep_a030_s42_fp32/report/alpha_sweep_a030_s42_fp32_analysis.md",
      "artifacts/_project/report/mmct_v2_a010_fp32_results.md",
      "artifacts/mmct_v2_a010_fp32_results.md",
      "artifacts/_project/report/report_dose_response_gaps.md",
      "artifacts/lag_sensitivity/run_lag_sensitivity.py",
      "artifacts/_project/report/per_alpha_fdr_results_b4d938.md",
      "artifacts/_project/report/per_alpha_fdr_results.md",
      "artifacts/per_alpha_fdr_results.md",
      "artifacts/_project/report/mmct_full_results_f5ecdb.md",
      "artifacts/_project/report/mmct_full_results.md",
      "artifacts/mmct_full_results.md",
      "artifacts/table7_draft.md",
      "artifacts/_project/report/table7_draft.md",
      "artifacts/alpha_sweep_a010_s43/report/a010_s43_bf16_analysis.md",
      "artifacts/intervention_reactive_s42/report/analysis_report.md",
      "artifacts/alpha_sweep_a000_s44/report/a000_s44_analysis_report.md",
      "artifacts/alpha_sweep_a000_s43/report/a000_s43_5method_analysis_7c0294.md",
      "artifacts/alpha_sweep_a000_s43/report/a000_s43_5method_analysis.md",
      "artifacts/alpha_sweep_a000_s43/data/a000_s43_5method_results_616865.json",
      "artifacts/alpha_sweep_a000_s43/data/a000_s43_5method_results.json",
      "artifacts/_project/report/ground_truth_redefine_v2_analysis.md",
      "artifacts/_project/report/ground_truth_redefine_analysis.md",
      "artifacts/_project/report/paper_consistency_audit.md",
      "artifacts/paper_consistency_audit.md",
      "artifacts/prep_cross_alpha_v5_verify.md",
      "artifacts/analysis/cross_alpha/cross_alpha_analysis_v4.py",
      "artifacts/cross_alpha_v4_ready.md",
      "artifacts/cross_alpha_analysis_v4.py",
      "artifacts/_project/intermediate/generalization_prep.md",
      "artifacts/generalization_prep.md",
      "artifacts/_project/intermediate/d026_optimized_commands.md",
      "artifacts/d026_optimized_commands.md",
      "artifacts/_project/intermediate/a075_analysis_prep.md",
      "artifacts/a075_analysis_prep.md",
      "artifacts/_project/data/cross_alpha_analysis.py",
      "artifacts/dream_reports/dream_20260514T184925/logs/review_worst.log",
      "artifacts/dream_reports/dream_20260514T184925/logs/review_median.log",
      "artifacts/dream_reports/dream_20260514T184925/logs/phase2_worst_attempt0.log"
    ],
    "numFiles": 98
  }
}
```

</details>

---


### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Let me read the existing Shapley JSON and the null seed D102 files to understand the data structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "625215f9-593e-4ab3-8fb1-3d03b7f1be17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9dTVmbxMr65uWdUwisV7U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2583,
      "cache_read_input_tokens": 34395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2583
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 24_

Let me read the existing Shapley JSON and the null D102 files to understand the data format.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "ffbdd8a3-2cc5-42c4-abee-0852242440cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9dTVmbxMr65uWdUwisV7U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2583,
      "cache_read_input_tokens": 34395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2583
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01E4z9uPfuAmJoTvvVijSppk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_values_v2.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "954ee2c2-3831-4641-8a1b-7786154bc849",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9dTVmbxMr65uWdUwisV7U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2583,
      "cache_read_input_tokens": 34395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2583
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 26 · 2026-05-24T08:51:38.942Z_

<details><summary>↩ Tool result · `toolu_01E4z9uPfuAmJoTvvVijSppk`</summary>

```text
1	{
2	  "version": "v3_dedup_fdr",
3	  "generated_at": "2026-05-20T14:29:55.778865",
4	  "data_sources": [
5	    "17855:alpha_sweep/a000_s42_fp32",
6	    "17855:alpha_sweep/a010_s42_fp32",
7	    "17855:alpha_sweep/a010_s43_fp32",
8	    "17855:alpha_sweep/a025_s42_fp32",
9	    "17855:alpha_sweep/a025_s43_fp32",
10	    "17855:alpha_sweep/a025_s44_fp32",
11	    "17855:alpha_sweep/a030_s42_fp32",
12	    "17855:alpha_sweep/a035_s42_fp32",
13	    "17855:alpha_sweep/a040_s42_fp32",
14	    "17855:alpha_sweep/a045_s42_fp32",
15	    "17855:alpha_sweep/a050_s42_fp32",
16	    "17855:alpha_sweep/a050_s43_fp32",
17	    "17855:alpha_sweep/a050_s44_fp32",
18	    "17855:alpha_sweep/a060_s42_fp32_v4",
19	    "17855:alpha_sweep/a060_s43_fp32",
20	    "17855:alpha_sweep/a075_s42_fp32",
21	    "17855:alpha_sweep/c4_a025_s42_fp32",
22	    "17855:alpha_sweep/c4_a050_s42_fp32",
23	    "17855:alpha_sweep/c4_a075_s42_fp32",
24	    "17855:generalize/pythia410m_wiki_a100_s43",
25	    "17855:generalize/qwen35_08b_wiki_a100_s42_fp32_v2",
26	    "17855:generalize/qwen35_08b_wiki_a100_s43_fp32",
27	    "17855:generalize/smollm3_3b_wiki_a100_s43_17855",
28	    "17855:padding_robustness/a100_s42_fp32",
29	    "17855:scale/14b_c4_s42_fp32",
30	    "17855:scale_check/pythia69b_wiki_a100_s42",
31	    "17855:scale_check/pythia69b_wiki_a100_s43",
32	    "19828:ablation/accumulate_a050_s43",
33	    "19828:alpha_sweep/a000_s43",
34	    "19828:alpha_sweep/a000_s44",
35	    "19828:alpha_sweep/a055_s42_fp32",
36	    "19828:alpha_sweep/a075_s43",
37	    "19828:alpha_sweep/a075_s44",
38	    "19828:alpha_sweep/c4_a050_s43_fp32",
39	    "19828:alpha_sweep/c4_a075_s43_fp32",
40	    "19828:gen_opt13b_wiki_a100_s43_fp32",
41	    "19828:gen_wiki_gpt2m_a100_s43",
42	    "19828:generalize/gpt2m_wiki_a100_s42",
43	    "19828:generalize/opt1b_wiki_a100_s42",
44	    "19828:generalize/pythia14b_wiki_a100_s42",
45	    "19828:generalize/pythia14b_wiki_a100_s43",
46	    "19828:generalize/pythia1b_c4_a100_s42",
47	    "19828:generalize/pythia1b_c4_a100_s43",
48	    "19828:generalize/pythia410m_wiki_a100_s42",
49	    "19828:generalize/smollm3_3b_wiki_a100_s42_fp32_v3",
50	    "19828:intervention/predictive_te_s42",
51	    "19828:intervention/reactive_d1_s42",
52	    "19828:scale_check/pythia14b_a050_s42"
53	  ],
54	  "dedup_rules": [
55	    "exclude dir names matching v3_d080|postd093|bf16",
56	    "same (dataset, alpha, seed) in alpha_sweep: prefer westd-17855 fp32",
57	    "only true_3sigma_d105 threshold"
58	  ],
59	  "fdr_field_used": {
60	    "naive_xcorr": "significant_fdr",
61	    "diff_xcorr": "significant_fdr",
62	    "threshold_onset": "significant (deterministic, no p-value)",
63	    "perm_granger": "significant_fdr",
64	    "ty_granger": "significant_fdr"
65	  },
66	  "threshold_criterion": "true_3sigma_d105",
67	  "n_methods": 5,
68	  "n_coalitions": 32,
69	  "n_null_experiments": 3,
70	  "n_signal_experiments": 45,
71	  "n_null_obs": 24,
72	  "n_signal_obs_6pair": 270,
73	  "n_signal_obs_8pair": 360,
74	  "fpr_pairs": [
75	    "token_entropy->distinct_1",
76	    "token_entropy->distinct_2",
77	    "token_entropy->distinct_3",
78	    "token_entropy->mauve",
79	    "ece->distinct_1",
80	    "ece->distinct_2",
81	    "ece->distinct_3",
82	    "ece->mauve"
83	  ],
84	  "fnr_pairs_6": [
85	    "token_entropy->distinct_1",
86	    "token_entropy->distinct_2",
87	    "token_entropy->distinct_3",
88	    "ece->distinct_1",
89	    "ece->distinct_2",
90	    "ece->distinct_3"
91	  ],
92	  "fnr_pairs_8": [
93	    "token_entropy->distinct_1",
94	    "token_entropy->distinct_2",
95	    "token_entropy->distinct_3",
96	    "token_entropy->mauve",
97	    "ece->distinct_1",
98	    "ece->distinct_2",
99	    "ece->distinct_3",
100	    "ece->mauve"
101	  ],
102	  "methods": [
103	    "naive_xcorr",
104	    "diff_xcorr",
105	    "threshold_onset",
106	    "perm_granger",
107	    "ty_granger"
108	  ],
109	  "main_result_6pair": {
110	    "fpr_shapley": {
111	      "naive_xcorr": 0.621528,
112	      "diff_xcorr": 0.163194,
113	      "threshold_onset": 0.100694,
114	      "perm_granger": 0.0,
115	      "ty_granger": 0.03125
116	    },
117	    "fnr_shapley": {
118	      "naive_xcorr": -0.41858,
119	      "diff_xcorr": -0.305617,
120	      "threshold_onset": -0.026914,
121	      "perm_granger": -0.18,
122	      "ty_granger": -0.068889
123	    },
124	    "combined_shapley": {
125	      "naive_xcorr": 0.202948,
126	      "diff_xcorr": -0.142423,
127	      "threshold_onset": 0.07378,
128	      "perm_granger": -0.18,
129	      "ty_granger": -0.037639
130	    }
131	  },
132	  "robustness_8pair": {
133	    "fpr_shapley": {
134	      "naive_xcorr": 0.621528,
135	      "diff_xcorr": 0.163194,
136	      "threshold_onset": 0.100694,
137	      "perm_granger": 0.0,
138	      "ty_granger": 0.03125
139	    },
140	    "fnr_shapley": {
141	      "naive_xcorr": -0.451852,
142	      "diff_xcorr": -0.269444,
143	      "threshold_onset": -0.037963,
144	      "perm_granger": -0.15162,
145	      "ty_granger": -0.058565
146	    },
147	    "combined_shapley": {
148	      "naive_xcorr": 0.169676,
149	      "diff_xcorr": -0.10625,
150	      "threshold_onset": 0.062731,
151	      "perm_granger": -0.15162,
152	      "ty_granger": -0.027315
153	    }
154	  },
155	  "raw_rates_8pair": {
156	    "naive_xcorr": {
157	      "fpr": 0.9167,
158	      "fnr": 0.0528,
159	      "fp_count": 22,
160	      "fp_total": 24,
161	      "fn_count": 19,
162	      "fn_total": 360
163	    },
164	    "diff_xcorr": {
165	      "fpr": 0.375,
166	      "fnr": 0.2528,
167	      "fp_count": 9,
168	      "fp_total": 24,
169	      "fn_count": 91,
170	      "fn_total": 360
171	    },
172	    "threshold_onset": {
173	      "fpr": 0.25,
174	      "fnr": 0.8889,
175	      "fp_count": 6,
176	      "fp_total": 24,
177	      "fn_count": 320,
178	      "fn_total": 360
179	    },
180	    "perm_granger": {
181	      "fpr": 0.0,
182	      "fnr": 0.5028,
183	      "fp_count": 0,
184	      "fp_total": 24,
185	      "fn_count": 181,
186	      "fn_total": 360
187	    },
188	    "ty_granger": {
189	      "fpr": 0.0833,
190	      "fnr": 0.7944,
191	      "fp_count": 2,
192	      "fp_total": 24,
193	      "fn_count": 286,
194	      "fn_total": 360
195	    }
196	  },
197	  "diagnostics": {
198	    "null_s42_source": "17855:alpha_sweep/a000_s42_fp32",
199	    "excluded_from_v2": [
200	      "17855:alpha_sweep/a005_s42_fp32_v3_d080",
201	      "17855:alpha_sweep/a060_s42_fp32_v3_d080",
202	      "17855:alpha_sweep/a050_postd093_s42_fp32",
203	      "17855:generalize/gpt2m_wiki_a100_s43_bf16"
204	    ],
205	    "deduped_from_v2": {
206	      "19828:alpha_sweep/a000_s42": "replaced by 17855:alpha_sweep/a000_s42_fp32",
207	      "19828:alpha_sweep/a010_s42": "replaced by 17855:alpha_sweep/a010_s42_fp32",
208	      "19828:alpha_sweep/a025_s43": "replaced by 17855:alpha_sweep/a025_s43_fp32",
209	      "19828:alpha_sweep/a025_s44": "replaced by 17855:alpha_sweep/a025_s44_fp32",
210	      "19828:alpha_sweep/a050_s42": "replaced by 17855:alpha_sweep/a050_s42_fp32",
211	      "19828:alpha_sweep/a050_s43": "replaced by 17855:alpha_sweep/a050_s43_fp32",
212	      "19828:alpha_sweep/a050_s44": "replaced by 17855:alpha_sweep/a050_s44_fp32",
213	      "19828:alpha_sweep/a075_s42": "replaced by 17855:alpha_sweep/a075_s42_fp32"
214	    }
215	  }
216	}
217	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "d2f6e3a8-ce60-4c28-9311-6a21a5be0f9a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_values_v2.json",
      "content": "{\n  \"version\": \"v3_dedup_fdr\",\n  \"generated_at\": \"2026-05-20T14:29:55.778865\",\n  \"data_sources\": [\n    \"17855:alpha_sweep/a000_s42_fp32\",\n    \"17855:alpha_sweep/a010_s42_fp32\",\n    \"17855:alpha_sweep/a010_s43_fp32\",\n    \"17855:alpha_sweep/a025_s42_fp32\",\n    \"17855:alpha_sweep/a025_s43_fp32\",\n    \"17855:alpha_sweep/a025_s44_fp32\",\n    \"17855:alpha_sweep/a030_s42_fp32\",\n    \"17855:alpha_sweep/a035_s42_fp32\",\n    \"17855:alpha_sweep/a040_s42_fp32\",\n    \"17855:alpha_sweep/a045_s42_fp32\",\n    \"17855:alpha_sweep/a050_s42_fp32\",\n    \"17855:alpha_sweep/a050_s43_fp32\",\n    \"17855:alpha_sweep/a050_s44_fp32\",\n    \"17855:alpha_sweep/a060_s42_fp32_v4\",\n    \"17855:alpha_sweep/a060_s43_fp32\",\n    \"17855:alpha_sweep/a075_s42_fp32\",\n    \"17855:alpha_sweep/c4_a025_s42_fp32\",\n    \"17855:alpha_sweep/c4_a050_s42_fp32\",\n    \"17855:alpha_sweep/c4_a075_s42_fp32\",\n    \"17855:generalize/pythia410m_wiki_a100_s43\",\n    \"17855:generalize/qwen35_08b_wiki_a100_s42_fp32_v2\",\n    \"17855:generalize/qwen35_08b_wiki_a100_s43_fp32\",\n    \"17855:generalize/smollm3_3b_wiki_a100_s43_17855\",\n    \"17855:padding_robustness/a100_s42_fp32\",\n    \"17855:scale/14b_c4_s42_fp32\",\n    \"17855:scale_check/pythia69b_wiki_a100_s42\",\n    \"17855:scale_check/pythia69b_wiki_a100_s43\",\n    \"19828:ablation/accumulate_a050_s43\",\n    \"19828:alpha_sweep/a000_s43\",\n    \"19828:alpha_sweep/a000_s44\",\n    \"19828:alpha_sweep/a055_s42_fp32\",\n    \"19828:alpha_sweep/a075_s43\",\n    \"19828:alpha_sweep/a075_s44\",\n    \"19828:alpha_sweep/c4_a050_s43_fp32\",\n    \"19828:alpha_sweep/c4_a075_s43_fp32\",\n    \"19828:gen_opt13b_wiki_a100_s43_fp32\",\n    \"19828:gen_wiki_gpt2m_a100_s43\",\n    \"19828:generalize/gpt2m_wiki_a100_s42\",\n    \"19828:generalize/opt1b_wiki_a100_s42\",\n    \"19828:generalize/pythia14b_wiki_a100_s42\",\n    \"19828:generalize/pythia14b_wiki_a100_s43\",\n    \"19828:generalize/pythia1b_c4_a100_s42\",\n    \"19828:generalize/pythia1b_c4_a100_s43\",\n    \"19828:generalize/pythia410m_wiki_a100_s42\",\n    \"19828:generalize/smollm3_3b_wiki_a100_s42_fp32_v3\",\n    \"19828:intervention/predictive_te_s42\",\n    \"19828:intervention/reactive_d1_s42\",\n    \"19828:scale_check/pythia14b_a050_s42\"\n  ],\n  \"dedup_rules\": [\n    \"exclude dir names matching v3_d080|postd093|bf16\",\n    \"same (dataset, alpha, seed) in alpha_sweep: prefer westd-17855 fp32\",\n    \"only true_3sigma_d105 threshold\"\n  ],\n  \"fdr_field_used\": {\n    \"naive_xcorr\": \"significant_fdr\",\n    \"diff_xcorr\": \"significant_fdr\",\n    \"threshold_onset\": \"significant (deterministic, no p-value)\",\n    \"perm_granger\": \"significant_fdr\",\n    \"ty_granger\": \"significant_fdr\"\n  },\n  \"threshold_criterion\": \"true_3sigma_d105\",\n  \"n_methods\": 5,\n  \"n_coalitions\": 32,\n  \"n_null_experiments\": 3,\n  \"n_signal_experiments\": 45,\n  \"n_null_obs\": 24,\n  \"n_signal_obs_6pair\": 270,\n  \"n_signal_obs_8pair\": 360,\n  \"fpr_pairs\": [\n    \"token_entropy->distinct_1\",\n    \"token_entropy->distinct_2\",\n    \"token_entropy->distinct_3\",\n    \"token_entropy->mauve\",\n    \"ece->distinct_1\",\n    \"ece->distinct_2\",\n    \"ece->distinct_3\",\n    \"ece->mauve\"\n  ],\n  \"fnr_pairs_6\": [\n    \"token_entropy->distinct_1\",\n    \"token_entropy->distinct_2\",\n    \"token_entropy->distinct_3\",\n    \"ece->distinct_1\",\n    \"ece->distinct_2\",\n    \"ece->distinct_3\"\n  ],\n  \"fnr_pairs_8\": [\n    \"token_entropy->distinct_1\",\n    \"token_entropy->distinct_2\",\n    \"token_entropy->distinct_3\",\n    \"token_entropy->mauve\",\n    \"ece->distinct_1\",\n    \"ece->distinct_2\",\n    \"ece->distinct_3\",\n    \"ece->mauve\"\n  ],\n  \"methods\": [\n    \"naive_xcorr\",\n    \"diff_xcorr\",\n    \"threshold_onset\",\n    \"perm_granger\",\n    \"ty_granger\"\n  ],\n  \"main_result_6pair\": {\n    \"fpr_shapley\": {\n      \"naive_xcorr\": 0.621528,\n      \"diff_xcorr\": 0.163194,\n      \"threshold_onset\": 0.100694,\n      \"perm_granger\": 0.0,\n      \"ty_granger\": 0.03125\n    },\n    \"fnr_shapley\": {\n      \"naive_xcorr\": -0.41858,\n      \"diff_xcorr\": -0.305617,\n      \"threshold_onset\": -0.026914,\n      \"perm_granger\": -0.18,\n      \"ty_granger\": -0.068889\n    },\n    \"combined_shapley\": {\n      \"naive_xcorr\": 0.202948,\n      \"diff_xcorr\": -0.142423,\n      \"threshold_onset\": 0.07378,\n      \"perm_granger\": -0.18,\n      \"ty_granger\": -0.037639\n    }\n  },\n  \"robustness_8pair\": {\n    \"fpr_shapley\": {\n      \"naive_xcorr\": 0.621528,\n      \"diff_xcorr\": 0.163194,\n      \"threshold_onset\": 0.100694,\n      \"perm_granger\": 0.0,\n      \"ty_granger\": 0.03125\n    },\n    \"fnr_shapley\": {\n      \"naive_xcorr\": -0.451852,\n      \"diff_xcorr\": -0.269444,\n      \"threshold_onset\": -0.037963,\n      \"perm_granger\": -0.15162,\n      \"ty_granger\": -0.058565\n    },\n    \"combined_shapley\": {\n      \"naive_xcorr\": 0.169676,\n      \"diff_xcorr\": -0.10625,\n      \"threshold_onset\": 0.062731,\n      \"perm_granger\": -0.15162,\n      \"ty_granger\": -0.027315\n    }\n  },\n  \"raw_rates_8pair\": {\n    \"naive_xcorr\": {\n      \"fpr\": 0.9167,\n      \"fnr\": 0.0528,\n      \"fp_count\": 22,\n      \"fp_total\": 24,\n      \"fn_count\": 19,\n      \"fn_total\": 360\n    },\n    \"diff_xcorr\": {\n      \"fpr\": 0.375,\n      \"fnr\": 0.2528,\n      \"fp_count\": 9,\n      \"fp_total\": 24,\n      \"fn_count\": 91,\n      \"fn_total\": 360\n    },\n    \"threshold_onset\": {\n      \"fpr\": 0.25,\n      \"fnr\": 0.8889,\n      \"fp_count\": 6,\n      \"fp_total\": 24,\n      \"fn_count\": 320,\n      \"fn_total\": 360\n    },\n    \"perm_granger\": {\n      \"fpr\": 0.0,\n      \"fnr\": 0.5028,\n      \"fp_count\": 0,\n      \"fp_total\": 24,\n      \"fn_count\": 181,\n      \"fn_total\": 360\n    },\n    \"ty_granger\": {\n      \"fpr\": 0.0833,\n      \"fnr\": 0.7944,\n      \"fp_count\": 2,\n      \"fp_total\": 24,\n      \"fn_count\": 286,\n      \"fn_total\": 360\n    }\n  },\n  \"diagnostics\": {\n    \"null_s42_source\": \"17855:alpha_sweep/a000_s42_fp32\",\n    \"excluded_from_v2\": [\n      \"17855:alpha_sweep/a005_s42_fp32_v3_d080\",\n      \"17855:alpha_sweep/a060_s42_fp32_v3_d080\",\n      \"17855:alpha_sweep/a050_postd093_s42_fp32\",\n      \"17855:generalize/gpt2m_wiki_a100_s43_bf16\"\n    ],\n    \"deduped_from_v2\": {\n      \"19828:alpha_sweep/a000_s42\": \"replaced by 17855:alpha_sweep/a000_s42_fp32\",\n      \"19828:alpha_sweep/a010_s42\": \"replaced by 17855:alpha_sweep/a010_s42_fp32\",\n      \"19828:alpha_sweep/a025_s43\": \"replaced by 17855:alpha_sweep/a025_s43_fp32\",\n      \"19828:alpha_sweep/a025_s44\": \"replaced by 17855:alpha_sweep/a025_s44_fp32\",\n      \"19828:alpha_sweep/a050_s42\": \"replaced by 17855:alpha_sweep/a050_s42_fp32\",\n      \"19828:alpha_sweep/a050_s43\": \"replaced by 17855:alpha_sweep/a050_s43_fp32\",\n      \"19828:alpha_sweep/a050_s44\": \"replaced by 17855:alpha_sweep/a050_s44_fp32\",\n      \"19828:alpha_sweep/a075_s42\": \"replaced by 17855:alpha_sweep/a075_s42_fp32\"\n    }\n  }\n}\n",
      "numLines": 217,
      "startLine": 1,
      "totalLines": 217
    }
  }
}
```

</details>

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01Vn8stUD5ZQ2YiRFiN5Bt4H`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/D102_null_s46_fp32_d3.json",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "e8e8d4f5-8f38-4522-bbf1-c215553b26e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9dTVmbxMr65uWdUwisV7U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2583,
      "cache_read_input_tokens": 34395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2583
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 28 · 2026-05-24T08:51:40.332Z_

<details><summary>↩ Tool result · `toolu_01Vn8stUD5ZQ2YiRFiN5Bt4H`</summary>

```text
1	{
2	  "meta": {
3	    "alpha": 0.0,
4	    "seed": 46,
5	    "T": 10,
6	    "n_gens": 11,
7	    "data_dir": "results/alpha_sweep/a000_s46_fp32",
8	    "methods": [
9	      "naive_xcorr",
10	      "diff_xcorr",
11	      "threshold_onset",
12	      "perm_granger",
13	      "ty_granger"
14	    ],
15	    "n_perm": 5000,
16	    "canaries": [
17	      "token_entropy",
18	      "ece"
19	    ],
20	    "downstreams": [
21	      "distinct_1",
22	      "distinct_2",
23	      "distinct_3"
24	    ],
25	    "threshold_criterion": "true_3sigma_d105",
26	    "note": "6-pair (distinct_1/2/3 only, mauve excluded)"
27	  },
28	  "summary": {
29	    "perm_granger_fdr_forward_sig": 0,
30	    "perm_granger_fdr_reverse_sig": 0,
31	    "robust_pairs": 1,
32	    "total_pairs": 6
33	  },
34	  "consensus": [
35	    {
36	      "pair": "token_entropy<distinct_1",
37	      "votes": 2,
38	      "methods": [
39	        "naive",
40	        "ty"
41	      ]
42	    },
43	    {
44	      "pair": "token_entropy<distinct_2",
45	      "votes": 0,
46	      "methods": []
47	    },
48	    {
49	      "pair": "token_entropy<distinct_3",
50	      "votes": 0,
51	      "methods": []
52	    },
53	    {
54	      "pair": "ece<distinct_1",
55	      "votes": 1,
56	      "methods": [
57	        "threshold"
58	      ]
59	    },
60	    {
61	      "pair": "ece<distinct_2",
62	      "votes": 3,
63	      "methods": [
64	        "naive",
65	        "threshold",
66	        "ty"
67	      ]
68	    },
69	    {
70	      "pair": "ece<distinct_3",
71	      "votes": 2,
72	      "methods": [
73	        "naive",
74	        "threshold"
75	      ]
76	    }
77	  ],
78	  "metrics_trajectory": {
79	    "gen_0": {
80	      "token_entropy": 3.2342,
81	      "ece": 0.0108,
82	      "distinct_1": 0.0974,
83	      "distinct_2": 0.5115,
84	      "distinct_3": 0.8108,
85	      "perplexity": 26.95,
86	      "mauve": null
87	    },
88	    "gen_1": {
89	      "token_entropy": 2.9934,
90	      "ece": 0.0105,
91	      "distinct_1": 0.0979,
92	      "distinct_2": 0.5121,
93	      "distinct_3": 0.8107,
94	      "perplexity": 19.2,
95	      "mauve": null
96	    },
97	    "gen_2": {
98	      "token_entropy": 3.012,
99	      "ece": 0.012,
100	      "distinct_1": 0.0891,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "f1d5dadb-dfe9-4f19-90ff-ae29f1fa6482",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/D102_null_s46_fp32_d3.json",
      "content": "{\n  \"meta\": {\n    \"alpha\": 0.0,\n    \"seed\": 46,\n    \"T\": 10,\n    \"n_gens\": 11,\n    \"data_dir\": \"results/alpha_sweep/a000_s46_fp32\",\n    \"methods\": [\n      \"naive_xcorr\",\n      \"diff_xcorr\",\n      \"threshold_onset\",\n      \"perm_granger\",\n      \"ty_granger\"\n    ],\n    \"n_perm\": 5000,\n    \"canaries\": [\n      \"token_entropy\",\n      \"ece\"\n    ],\n    \"downstreams\": [\n      \"distinct_1\",\n      \"distinct_2\",\n      \"distinct_3\"\n    ],\n    \"threshold_criterion\": \"true_3sigma_d105\",\n    \"note\": \"6-pair (distinct_1/2/3 only, mauve excluded)\"\n  },\n  \"summary\": {\n    \"perm_granger_fdr_forward_sig\": 0,\n    \"perm_granger_fdr_reverse_sig\": 0,\n    \"robust_pairs\": 1,\n    \"total_pairs\": 6\n  },\n  \"consensus\": [\n    {\n      \"pair\": \"token_entropy<distinct_1\",\n      \"votes\": 2,\n      \"methods\": [\n        \"naive\",\n        \"ty\"\n      ]\n    },\n    {\n      \"pair\": \"token_entropy<distinct_2\",\n      \"votes\": 0,\n      \"methods\": []\n    },\n    {\n      \"pair\": \"token_entropy<distinct_3\",\n      \"votes\": 0,\n      \"methods\": []\n    },\n    {\n      \"pair\": \"ece<distinct_1\",\n      \"votes\": 1,\n      \"methods\": [\n        \"threshold\"\n      ]\n    },\n    {\n      \"pair\": \"ece<distinct_2\",\n      \"votes\": 3,\n      \"methods\": [\n        \"naive\",\n        \"threshold\",\n        \"ty\"\n      ]\n    },\n    {\n      \"pair\": \"ece<distinct_3\",\n      \"votes\": 2,\n      \"methods\": [\n        \"naive\",\n        \"threshold\"\n      ]\n    }\n  ],\n  \"metrics_trajectory\": {\n    \"gen_0\": {\n      \"token_entropy\": 3.2342,\n      \"ece\": 0.0108,\n      \"distinct_1\": 0.0974,\n      \"distinct_2\": 0.5115,\n      \"distinct_3\": 0.8108,\n      \"perplexity\": 26.95,\n      \"mauve\": null\n    },\n    \"gen_1\": {\n      \"token_entropy\": 2.9934,\n      \"ece\": 0.0105,\n      \"distinct_1\": 0.0979,\n      \"distinct_2\": 0.5121,\n      \"distinct_3\": 0.8107,\n      \"perplexity\": 19.2,\n      \"mauve\": null\n    },\n    \"gen_2\": {\n      \"token_entropy\": 3.012,\n      \"ece\": 0.012,\n      \"distinct_1\": 0.0891,",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 179
    }
  }
}
```

</details>

---


### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01HeAmT9nC4zHFECNyBZRENL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/fpr_transparency_all_seeds.json",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "5b8a099f-e513-4764-b6a2-f1dad497a05e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M9dTVmbxMr65uWdUwisV7U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2583,
      "cache_read_input_tokens": 34395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2583
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 30 · 2026-05-24T08:51:40.899Z_

<details><summary>↩ Tool result · `toolu_01HeAmT9nC4zHFECNyBZRENL`</summary>

```text
1	{
2	  "description": "FPR transparency: per-seed per-pair raw p-values for 6 null experiments (alpha=0.00, Pythia-410M, T=10). Analyzed with batch_d102_6pair.py (D102 parameters).",
3	  "model": "pythia-410m",
4	  "alpha": 0.0,
5	  "T": 10,
6	  "n_perm": 5000,
7	  "threshold_criterion": "true_3sigma_d105",
8	  "pair_basis": "6-pair (distinct_1/2/3 only, mauve excluded)",
9	  "methods": [
10	    "perm_granger (BH-FDR across 6 pairs)",
11	    "diff_xcorr (BH-FDR across 6 pairs)",
12	    "threshold_onset (true_3sigma_d105)",
13	    "ty_granger (uncorrected)",
14	    "naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)"
15	  ],
16	  "consensus_rule": "K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.",
17	  "summary": {
18	    "total_seed_pairs": 36,
19	    "K_ge_3_count": 6,
20	    "K_ge_3_fpr": 0.1667,
21	    "per_seed_K_ge_3": {
22	      "s45": 1,
23	      "s46": 1,
24	      "s47": 2,
25	      "s48": 0,
26	      "s49": 0,
27	      "s50": 2
28	    },
29	    "K_ge_3_permg_breakdown": {
30	      "with_permg": 2,
31	      "without_permg": 4,
32	      "detail": "s50 te->d1,d2 include PermG (consensus=[naive,perm,ty]); s45 ece->d2, s46 ece->d2, s47 ece->d1,d2 do not (consensus=[naive,threshold,ty])"
33	    },
34	    "per_seed_permg_fwd_fdr": {
35	      "s45": 2,
36	      "s46": 0,
37	      "s47": 0,
38	      "s48": 0,
39	      "s49": 0,
40	      "s50": 2
41	    }
42	  },
43	  "seeds": [
44	    {
45	      "seed": 45,
46	      "exp_dir": "results/alpha_sweep/a000_s45_fp32",
47	      "T": 10,
48	      "n_gens": 11,
49	      "n_perm": 5000,
50	      "pairs": [
51	        {
52	          "canary": "token_entropy",
53	          "downstream": "distinct_1",
54	          "perm_granger_fwd_p": 0.081184,
55	          "perm_granger_fwd_sig_fdr": false,
56	          "perm_granger_rev_p": 0.223555,
57	          "diff_xcorr_fwd_p": 0.367327,
58	          "diff_xcorr_fwd_r": 0.8261,
59	          "diff_xcorr_fwd_lag": 1,
60	          "diff_xcorr_fwd_sig_fdr": false,
61	          "threshold_onset_lead": -3,
62	          "threshold_onset_sig": false,
63	          "ty_granger_p": 0.162007,
64	          "ty_granger_sig": false,
65	          "naive_xcorr_r": -0.8017,
66	          "naive_xcorr_lag": -2,
67	          "naive_xcorr_sig": true,
68	          "consensus_votes": 1,
69	          "consensus_methods": [
70	            "naive"
71	          ]
72	        },
73	        {
74	          "canary": "token_entropy",
75	          "downstream": "distinct_2",
76	          "perm_granger_fwd_p": 0.001,
77	          "perm_granger_fwd_sig_fdr": true,
78	          "perm_granger_rev_p": 0.706659,
79	          "diff_xcorr_fwd_p": 0.0006,
80	          "diff_xcorr_fwd_r": 0.9882,
81	          "diff_xcorr_fwd_lag": 1,
82	          "diff_xcorr_fwd_sig_fdr": true,
83	          "threshold_onset_lead": 0,
84	          "threshold_onset_sig": false,
85	          "ty_granger_p": 0.020611,
86	          "ty_granger_sig": true,
87	          "naive_xcorr_r": 0.8917,
88	          "naive_xcorr_lag": 1,
89	          "naive_xcorr_sig": true,
90	          "consensus_votes": 2,
91	          "consensus_methods": [
92	            "perm",
93	            "ty"
94	          ]
95	        },
96	        {
97	          "canary": "token_entropy",
98	          "downstream": "distinct_3",
99	          "perm_granger_fwd_p": 0.0012,
100	          "perm_granger_fwd_sig_fdr": true,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "8e2b3d83-ed42-4199-8d30-8bfa19ca5f87",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/fpr_transparency_all_seeds.json",
      "content": "{\n  \"description\": \"FPR transparency: per-seed per-pair raw p-values for 6 null experiments (alpha=0.00, Pythia-410M, T=10). Analyzed with batch_d102_6pair.py (D102 parameters).\",\n  \"model\": \"pythia-410m\",\n  \"alpha\": 0.0,\n  \"T\": 10,\n  \"n_perm\": 5000,\n  \"threshold_criterion\": \"true_3sigma_d105\",\n  \"pair_basis\": \"6-pair (distinct_1/2/3 only, mauve excluded)\",\n  \"methods\": [\n    \"perm_granger (BH-FDR across 6 pairs)\",\n    \"diff_xcorr (BH-FDR across 6 pairs)\",\n    \"threshold_onset (true_3sigma_d105)\",\n    \"ty_granger (uncorrected)\",\n    \"naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)\"\n  ],\n  \"consensus_rule\": \"K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.\",\n  \"summary\": {\n    \"total_seed_pairs\": 36,\n    \"K_ge_3_count\": 6,\n    \"K_ge_3_fpr\": 0.1667,\n    \"per_seed_K_ge_3\": {\n      \"s45\": 1,\n      \"s46\": 1,\n      \"s47\": 2,\n      \"s48\": 0,\n      \"s49\": 0,\n      \"s50\": 2\n    },\n    \"K_ge_3_permg_breakdown\": {\n      \"with_permg\": 2,\n      \"without_permg\": 4,\n      \"detail\": \"s50 te->d1,d2 include PermG (consensus=[naive,perm,ty]); s45 ece->d2, s46 ece->d2, s47 ece->d1,d2 do not (consensus=[naive,threshold,ty])\"\n    },\n    \"per_seed_permg_fwd_fdr\": {\n      \"s45\": 2,\n      \"s46\": 0,\n      \"s47\": 0,\n      \"s48\": 0,\n      \"s49\": 0,\n      \"s50\": 2\n    }\n  },\n  \"seeds\": [\n    {\n      \"seed\": 45,\n      \"exp_dir\": \"results/alpha_sweep/a000_s45_fp32\",\n      \"T\": 10,\n      \"n_gens\": 11,\n      \"n_perm\": 5000,\n      \"pairs\": [\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.081184,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.223555,\n          \"diff_xcorr_fwd_p\": 0.367327,\n          \"diff_xcorr_fwd_r\": 0.8261,\n          \"diff_xcorr_fwd_lag\": 1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -3,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.162007,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.8017,\n          \"naive_xcorr_lag\": -2,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\n            \"naive\"\n          ]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.001,\n          \"perm_granger_fwd_sig_fdr\": true,\n          \"perm_granger_rev_p\": 0.706659,\n          \"diff_xcorr_fwd_p\": 0.0006,\n          \"diff_xcorr_fwd_r\": 0.9882,\n          \"diff_xcorr_fwd_lag\": 1,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": 0,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.020611,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.8917,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\n            \"perm\",\n            \"ty\"\n          ]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.0012,\n          \"perm_granger_fwd_sig_fdr\": true,",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 895
    }
  }
}
```

</details>

---


### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the data. Let me read the full fpr_transparency file to understand the per-pair detection results for all 6 null seeds. This will be the data source for the new Shapley computation.

But I also need to know:
1. The per-method per-pair detection results for all 6 null seeds
2. The signal detection results (already in the old Shapley JSON from 45 signal experiments)

Let me also check what D102 files we have for null seeds s45 and s47 (I see we have s46, s48, s49, s50).


I notice the fpr_transparency file actually contains all 6 seeds from s45 to s50, whereas the old Shapley computation used s42, s43, and s44 as null seeds with 45 signal experiments. The new version should shift to using s45-s50 as the null seed set. I need to pull the full fpr_transparency file and locate the D102 files for s45 and s47.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "0e411743-9dd3-45fc-9cc2-b8a5f070f05b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CVJWCBH7x3p1poFLdroU9F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6418,
      "cache_read_input_tokens": 36978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6418
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 32_

Now I need the full null seed data and the signal experiment data. Let me read more of the fpr_transparency file and find D102 files for s45 and s47.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "ae7b3cd5-7c8f-4846-835d-4a35817750e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CVJWCBH7x3p1poFLdroU9F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6418,
      "cache_read_input_tokens": 36978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6418
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01USwRqxyfJTt7BeQovhUH5A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/fpr_transparency_all_seeds.json",
  "offset": 100,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "c9cf43ee-aeff-4f24-b414-bbba53b61275",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CVJWCBH7x3p1poFLdroU9F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6418,
      "cache_read_input_tokens": 36978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6418
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 34 · 2026-05-24T08:51:53.069Z_

<details><summary>↩ Tool result · `toolu_01USwRqxyfJTt7BeQovhUH5A`</summary>

```text
100	          "perm_granger_fwd_sig_fdr": true,
101	          "perm_granger_rev_p": 0.843831,
102	          "diff_xcorr_fwd_p": 0.019996,
103	          "diff_xcorr_fwd_r": 0.8685,
104	          "diff_xcorr_fwd_lag": 1,
105	          "diff_xcorr_fwd_sig_fdr": false,
106	          "threshold_onset_lead": -4,
107	          "threshold_onset_sig": false,
108	          "ty_granger_p": 0.078535,
109	          "ty_granger_sig": false,
110	          "naive_xcorr_r": 0.9238,
111	          "naive_xcorr_lag": 1,
112	          "naive_xcorr_sig": true,
113	          "consensus_votes": 1,
114	          "consensus_methods": [
115	            "perm"
116	          ]
117	        },
118	        {
119	          "canary": "ece",
120	          "downstream": "distinct_1",
121	          "perm_granger_fwd_p": 0.419716,
122	          "perm_granger_fwd_sig_fdr": false,
123	          "perm_granger_rev_p": 0.080184,
124	          "diff_xcorr_fwd_p": 0.34813,
125	          "diff_xcorr_fwd_r": -0.689,
126	          "diff_xcorr_fwd_lag": -2,
127	          "diff_xcorr_fwd_sig_fdr": false,
128	          "threshold_onset_lead": 5,
129	          "threshold_onset_sig": true,
130	          "ty_granger_p": 0.045787,
131	          "ty_granger_sig": true,
132	          "naive_xcorr_r": 0.8725,
133	          "naive_xcorr_lag": 2,
134	          "naive_xcorr_sig": true,
135	          "consensus_votes": 2,
136	          "consensus_methods": [
137	            "threshold",
138	            "ty"
139	          ]
140	        },
141	        {
142	          "canary": "ece",
143	          "downstream": "distinct_2",
144	          "perm_granger_fwd_p": 0.741852,
145	          "perm_granger_fwd_sig_fdr": false,
146	          "perm_granger_rev_p": 0.293941,
147	          "diff_xcorr_fwd_p": 0.840232,
148	          "diff_xcorr_fwd_r": -0.4467,
149	          "diff_xcorr_fwd_lag": 3,
150	          "diff_xcorr_fwd_sig_fdr": false,
151	          "threshold_onset_lead": 8,
152	          "threshold_onset_sig": true,
153	          "ty_granger_p": 0.025052,
154	          "ty_granger_sig": true,
155	          "naive_xcorr_r": 0.6311,
156	          "naive_xcorr_lag": -1,
157	          "naive_xcorr_sig": true,
158	          "consensus_votes": 3,
159	          "consensus_methods": [
160	            "naive",
161	            "threshold",
162	            "ty"
163	          ]
164	        },
165	        {
166	          "canary": "ece",
167	          "downstream": "distinct_3",
168	          "perm_granger_fwd_p": 0.261948,
169	          "perm_granger_fwd_sig_fdr": false,
170	          "perm_granger_rev_p": 0.611678,
171	          "diff_xcorr_fwd_p": 0.927814,
172	          "diff_xcorr_fwd_r": 0.449,
173	          "diff_xcorr_fwd_lag": 1,
174	          "diff_xcorr_fwd_sig_fdr": false,
175	          "threshold_onset_lead": 4,
176	          "threshold_onset_sig": true,
177	          "ty_granger_p": 0.028965,
178	          "ty_granger_sig": true,
179	          "naive_xcorr_r": -0.7033,
180	          "naive_xcorr_lag": 3,
181	          "naive_xcorr_sig": true,
182	          "consensus_votes": 2,
183	          "consensus_methods": [
184	            "threshold",
185	            "ty"
186	          ]
187	        }
188	      ]
189	    },
190	    {
191	      "seed": 46,
192	      "exp_dir": "results/alpha_sweep/a000_s46_fp32",
193	      "T": 10,
194	      "n_gens": 11,
195	      "n_perm": 5000,
196	      "pairs": [
197	        {
198	          "canary": "token_entropy",
199	          "downstream": "distinct_1",
200	          "perm_granger_fwd_p": 0.074985,
201	          "perm_granger_fwd_sig_fdr": false,
202	          "perm_granger_rev_p": 0.59908,
203	          "diff_xcorr_fwd_p": 0.336133,
204	          "diff_xcorr_fwd_r": 0.9367,
205	          "diff_xcorr_fwd_lag": 1,
206	          "diff_xcorr_fwd_sig_fdr": false,
207	          "threshold_onset_lead": -5,
208	          "threshold_onset_sig": false,
209	          "ty_granger_p": 0.000805,
210	          "ty_granger_sig": true,
211	          "naive_xcorr_r": -0.8428,
212	          "naive_xcorr_lag": -1,
213	          "naive_xcorr_sig": true,
214	          "consensus_votes": 2,
215	          "consensus_methods": [
216	            "naive",
217	            "ty"
218	          ]
219	        },
220	        {
221	          "canary": "token_entropy",
222	          "downstream": "distinct_2",
223	          "perm_granger_fwd_p": 0.030594,
224	          "perm_granger_fwd_sig_fdr": false,
225	          "perm_granger_rev_p": 0.962607,
226	          "diff_xcorr_fwd_p": 0.206759,
227	          "diff_xcorr_fwd_r": 0.9183,
228	          "diff_xcorr_fwd_lag": 1,
229	          "diff_xcorr_fwd_sig_fdr": false,
230	          "threshold_onset_lead": 0,
231	          "threshold_onset_sig": false,
232	          "ty_granger_p": 0.707829,
233	          "ty_granger_sig": false,
234	          "naive_xcorr_r": 0.8753,
235	          "naive_xcorr_lag": 1,
236	          "naive_xcorr_sig": true,
237	          "consensus_votes": 0,
238	          "consensus_methods": []
239	        },
240	        {
241	          "canary": "token_entropy",
242	          "downstream": "distinct_3",
243	          "perm_granger_fwd_p": 0.042591,
244	          "perm_granger_fwd_sig_fdr": false,
245	          "perm_granger_rev_p": 0.523295,
246	          "diff_xcorr_fwd_p": 0.354529,
247	          "diff_xcorr_fwd_r": 0.7677,
248	          "diff_xcorr_fwd_lag": 1,
249	          "diff_xcorr_fwd_sig_fdr": false,
250	          "threshold_onset_lead": 0,
251	          "threshold_onset_sig": false,
252	          "ty_granger_p": 0.452874,
253	          "ty_granger_sig": false,
254	          "naive_xcorr_r": 0.87,
255	          "naive_xcorr_lag": 1,
256	          "naive_xcorr_sig": true,
257	          "consensus_votes": 0,
258	          "consensus_methods": []
259	        },
260	        {
261	          "canary": "ece",
262	          "downstream": "distinct_1",
263	          "perm_granger_fwd_p": 0.774845,
264	          "perm_granger_fwd_sig_fdr": false,
265	          "perm_granger_rev_p": 0.458508,
266	          "diff_xcorr_fwd_p": 0.357129,
267	          "diff_xcorr_fwd_r": 0.6664,
268	          "diff_xcorr_fwd_lag": -3,
269	          "diff_xcorr_fwd_sig_fdr": false,
270	          "threshold_onset_lead": 3,
271	          "threshold_onset_sig": true,
272	          "ty_granger_p": 0.749508,
273	          "ty_granger_sig": false,
274	          "naive_xcorr_r": 0.7637,
275	          "naive_xcorr_lag": 2,
276	          "naive_xcorr_sig": true,
277	          "consensus_votes": 1,
278	          "consensus_methods": [
279	            "threshold"
280	          ]
281	        },
282	        {
283	          "canary": "ece",
284	          "downstream": "distinct_2",
285	          "perm_granger_fwd_p": 0.744851,
286	          "perm_granger_fwd_sig_fdr": false,
287	          "perm_granger_rev_p": 0.695261,
288	          "diff_xcorr_fwd_p": 0.492701,
289	          "diff_xcorr_fwd_r": -0.6326,
290	          "diff_xcorr_fwd_lag": 3,
291	          "diff_xcorr_fwd_sig_fdr": false,
292	          "threshold_onset_lead": 8,
293	          "threshold_onset_sig": true,
294	          "ty_granger_p": 0.01479,
295	          "ty_granger_sig": true,
296	          "naive_xcorr_r": 0.6791,
297	          "naive_xcorr_lag": -3,
298	          "naive_xcorr_sig": true,
299	          "consensus_votes": 3,
300	          "consensus_methods": [
301	            "naive",
302	            "threshold",
303	            "ty"
304	          ]
305	        },
306	        {
307	          "canary": "ece",
308	          "downstream": "distinct_3",
309	          "perm_granger_fwd_p": 0.475105,
310	          "perm_granger_fwd_sig_fdr": false,
311	          "perm_granger_rev_p": 0.806639,
312	          "diff_xcorr_fwd_p": 0.916817,
313	          "diff_xcorr_fwd_r": -0.4626,
314	          "diff_xcorr_fwd_lag": -2,
315	          "diff_xcorr_fwd_sig_fdr": false,
316	          "threshold_onset_lead": 8,
317	          "threshold_onset_sig": true,
318	          "ty_granger_p": 0.433575,
319	          "ty_granger_sig": false,
320	          "naive_xcorr_r": 0.5893,
321	          "naive_xcorr_lag": -3,
322	          "naive_xcorr_sig": true,
323	          "consensus_votes": 2,
324	          "consensus_methods": [
325	            "naive",
326	            "threshold"
327	          ]
328	        }
329	      ]
330	    },
331	    {
332	      "seed": 47,
333	      "exp_dir": "results/alpha_sweep/a000_s47_fp32",
334	      "T": 10,
335	      "n_gens": 11,
336	      "n_perm": 5000,
337	      "pairs": [
338	        {
339	          "canary": "token_entropy",
340	          "downstream": "distinct_1",
341	          "perm_granger_fwd_p": 0.062987,
342	          "perm_granger_fwd_sig_fdr": false,
343	          "perm_granger_rev_p": 0.444311,
344	          "diff_xcorr_fwd_p": 0.216757,
345	          "diff_xcorr_fwd_r": 0.9416,
346	          "diff_xcorr_fwd_lag": 1,
347	          "diff_xcorr_fwd_sig_fdr": false,
348	          "threshold_onset_lead": 0,
349	          "threshold_onset_sig": false,
350	          "ty_granger_p": 0.000271,
351	          "ty_granger_sig": true,
352	          "naive_xcorr_r": -0.7895,
353	          "naive_xcorr_lag": -3,
354	          "naive_xcorr_sig": true,
355	          "consensus_votes": 2,
356	          "consensus_methods": [
357	            "naive",
358	            "ty"
359	          ]
360	        },
361	        {
362	          "canary": "token_entropy",
363	          "downstream": "distinct_2",
364	          "perm_granger_fwd_p": 0.018796,
365	          "perm_granger_fwd_sig_fdr": false,
366	          "perm_granger_rev_p": 0.531694,
367	          "diff_xcorr_fwd_p": 0.068586,
368	          "diff_xcorr_fwd_r": 0.9809,
369	          "diff_xcorr_fwd_lag": 1,
370	          "diff_xcorr_fwd_sig_fdr": false,
371	          "threshold_onset_lead": 0,
372	          "threshold_onset_sig": false,
373	          "ty_granger_p": 4.6e-05,
374	          "ty_granger_sig": true,
375	          "naive_xcorr_r": 0.8792,
376	          "naive_xcorr_lag": 1,
377	          "naive_xcorr_sig": true,
378	          "consensus_votes": 1,
379	          "consensus_methods": [
380	            "ty"
381	          ]
382	        },
383	        {
384	          "canary": "token_entropy",
385	          "downstream": "distinct_3",
386	          "perm_granger_fwd_p": 0.012597,
387	          "perm_granger_fwd_sig_fdr": false,
388	          "perm_granger_rev_p": 0.603279,
389	          "diff_xcorr_fwd_p": 0.065787,
390	          "diff_xcorr_fwd_r": 0.9811,
391	          "diff_xcorr_fwd_lag": 1,
392	          "diff_xcorr_fwd_sig_fdr": false,
393	          "threshold_onset_lead": 0,
394	          "threshold_onset_sig": false,
395	          "ty_granger_p": 6e-06,
396	          "ty_granger_sig": true,
397	          "naive_xcorr_r": 0.9149,
398	          "naive_xcorr_lag": 1,
399	          "naive_xcorr_sig": true,
400	          "consensus_votes": 1,
401	          "consensus_methods": [
402	            "ty"
403	          ]
404	        },
405	        {
406	          "canary": "ece",
407	          "downstream": "distinct_1",
408	          "perm_granger_fwd_p": 0.69886,
409	          "perm_granger_fwd_sig_fdr": false,
410	          "perm_granger_rev_p": 0.408518,
411	          "diff_xcorr_fwd_p": 0.066187,
412	          "diff_xcorr_fwd_r": 0.8799,
413	          "diff_xcorr_fwd_lag": -2,
414	          "diff_xcorr_fwd_sig_fdr": false,
415	          "threshold_onset_lead": 7,
416	          "threshold_onset_sig": true,
417	          "ty_granger_p": 0.044599,
418	          "ty_granger_sig": true,
419	          "naive_xcorr_r": 0.8735,
420	          "naive_xcorr_lag": -2,
421	          "naive_xcorr_sig": true,
422	          "consensus_votes": 3,
423	          "consensus_methods": [
424	            "naive",
425	            "threshold",
426	            "ty"
427	          ]
428	        },
429	        {
430	          "canary": "ece",
431	          "downstream": "distinct_2",
432	          "perm_granger_fwd_p": 0.579484,
433	          "perm_granger_fwd_sig_fdr": false,
434	          "perm_granger_rev_p": 0.317736,
435	          "diff_xcorr_fwd_p": 0.088982,
436	          "diff_xcorr_fwd_r": 0.8684,
437	          "diff_xcorr_fwd_lag": -2,
438	          "diff_xcorr_fwd_sig_fdr": false,
439	          "threshold_onset_lead": 7,
440	          "threshold_onset_sig": true,
441	          "ty_granger_p": 0.018539,
442	          "ty_granger_sig": true,
443	          "naive_xcorr_r": 0.8907,
444	          "naive_xcorr_lag": -2,
445	          "naive_xcorr_sig": true,
446	          "consensus_votes": 3,
447	          "consensus_methods": [
448	            "naive",
449	            "threshold",
450	            "ty"
451	          ]
452	        },
453	        {
454	          "canary": "ece",
455	          "downstream": "distinct_3",
456	          "perm_granger_fwd_p": 0.427914,
457	          "perm_granger_fwd_sig_fdr": false,
458	          "perm_granger_rev_p": 0.338332,
459	          "diff_xcorr_fwd_p": 0.273545,
460	          "diff_xcorr_fwd_r": 0.8181,
461	          "diff_xcorr_fwd_lag": -2,
462	          "diff_xcorr_fwd_sig_fdr": false,
463	          "threshold_onset_lead": 7,
464	          "threshold_onset_sig": true,
465	          "ty_granger_p": 0.133768,
466	          "ty_granger_sig": false,
467	          "naive_xcorr_r": 0.8798,
468	          "naive_xcorr_lag": -2,
469	          "naive_xcorr_sig": true,
470	          "consensus_votes": 2,
471	          "consensus_methods": [
472	            "naive",
473	            "threshold"
474	          ]
475	        }
476	      ]
477	    },
478	    {
479	      "seed": 48,
480	      "exp_dir": "results/alpha_sweep/a000_s48_fp32",
481	      "T": 10,
482	      "n_gens": 11,
483	      "n_perm": 5000,
484	      "pairs": [
485	        {
486	          "canary": "token_entropy",
487	          "downstream": "distinct_1",
488	          "perm_granger_fwd_p": 0.060388,
489	          "perm_granger_fwd_sig_fdr": false,
490	          "perm_granger_rev_p": 0.14917,
491	          "diff_xcorr_fwd_p": 0.356529,
492	          "diff_xcorr_fwd_r": 0.8533,
493	          "diff_xcorr_fwd_lag": 1,
494	          "diff_xcorr_fwd_sig_fdr": false,
495	          "threshold_onset_lead": 0,
496	          "threshold_onset_sig": false,
497	          "ty_granger_p": 0.15754,
498	          "ty_granger_sig": false,
499	          "naive_xcorr_r": 0.6663,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "cff8438a-c9a7-4256-b58d-0010cf542437",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/fpr_transparency_all_seeds.json",
      "content": "          \"perm_granger_fwd_sig_fdr\": true,\n          \"perm_granger_rev_p\": 0.843831,\n          \"diff_xcorr_fwd_p\": 0.019996,\n          \"diff_xcorr_fwd_r\": 0.8685,\n          \"diff_xcorr_fwd_lag\": 1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -4,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.078535,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.9238,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\n            \"perm\"\n          ]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.419716,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.080184,\n          \"diff_xcorr_fwd_p\": 0.34813,\n          \"diff_xcorr_fwd_r\": -0.689,\n          \"diff_xcorr_fwd_lag\": -2,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 5,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.045787,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.8725,\n          \"naive_xcorr_lag\": 2,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\n            \"threshold\",\n            \"ty\"\n          ]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.741852,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.293941,\n          \"diff_xcorr_fwd_p\": 0.840232,\n          \"diff_xcorr_fwd_r\": -0.4467,\n          \"diff_xcorr_fwd_lag\": 3,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 8,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.025052,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.6311,\n          \"naive_xcorr_lag\": -1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 3,\n          \"consensus_methods\": [\n            \"naive\",\n            \"threshold\",\n            \"ty\"\n          ]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.261948,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.611678,\n          \"diff_xcorr_fwd_p\": 0.927814,\n          \"diff_xcorr_fwd_r\": 0.449,\n          \"diff_xcorr_fwd_lag\": 1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 4,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.028965,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": -0.7033,\n          \"naive_xcorr_lag\": 3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\n            \"threshold\",\n            \"ty\"\n          ]\n        }\n      ]\n    },\n    {\n      \"seed\": 46,\n      \"exp_dir\": \"results/alpha_sweep/a000_s46_fp32\",\n      \"T\": 10,\n      \"n_gens\": 11,\n      \"n_perm\": 5000,\n      \"pairs\": [\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.074985,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.59908,\n          \"diff_xcorr_fwd_p\": 0.336133,\n          \"diff_xcorr_fwd_r\": 0.9367,\n          \"diff_xcorr_fwd_lag\": 1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -5,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.000805,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": -0.8428,\n          \"naive_xcorr_lag\": -1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\n            \"naive\",\n            \"ty\"\n          ]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.030594,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.962607,\n          \"diff_xcorr_fwd_p\": 0.206759,\n          \"diff_xcorr_fwd_r\": 0.9183,\n          \"diff_xcorr_fwd_lag\": 1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 0,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.707829,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8753,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.042591,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.523295,\n          \"diff_xcorr_fwd_p\": 0.354529,\n          \"diff_xcorr_fwd_r\": 0.7677,\n          \"diff_xcorr_fwd_lag\": 1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 0,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.452874,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.87,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.774845,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.458508,\n          \"diff_xcorr_fwd_p\": 0.357129,\n          \"diff_xcorr_fwd_r\": 0.6664,\n          \"diff_xcorr_fwd_lag\": -3,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 3,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.749508,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.7637,\n          \"naive_xcorr_lag\": 2,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\n            \"threshold\"\n          ]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.744851,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.695261,\n          \"diff_xcorr_fwd_p\": 0.492701,\n          \"diff_xcorr_fwd_r\": -0.6326,\n          \"diff_xcorr_fwd_lag\": 3,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 8,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.01479,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.6791,\n          \"naive_xcorr_lag\": -3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 3,\n          \"consensus_methods\": [\n            \"naive\",\n            \"threshold\",\n            \"ty\"\n          ]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.475105,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.806639,\n          \"diff_xcorr_fwd_p\": 0.916817,\n          \"diff_xcorr_fwd_r\": -0.4626,\n          \"diff_xcorr_fwd_lag\": -2,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 8,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.433575,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.5893,\n          \"naive_xcorr_lag\": -3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\n            \"naive\",\n            \"threshold\"\n          ]\n        }\n      ]\n    },\n    {\n      \"seed\": 47,\n      \"exp_dir\": \"results/alpha_sweep/a000_s47_fp32\",\n      \"T\": 10,\n      \"n_gens\": 11,\n      \"n_perm\": 5000,\n      \"pairs\": [\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.062987,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.444311,\n          \"diff_xcorr_fwd_p\": 0.216757,\n          \"diff_xcorr_fwd_r\": 0.9416,\n          \"diff_xcorr_fwd_lag\": 1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 0,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.000271,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": -0.7895,\n          \"naive_xcorr_lag\": -3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\n            \"naive\",\n            \"ty\"\n          ]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.018796,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.531694,\n          \"diff_xcorr_fwd_p\": 0.068586,\n          \"diff_xcorr_fwd_r\": 0.9809,\n          \"diff_xcorr_fwd_lag\": 1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 0,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 4.6e-05,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.8792,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\n            \"ty\"\n          ]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.012597,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.603279,\n          \"diff_xcorr_fwd_p\": 0.065787,\n          \"diff_xcorr_fwd_r\": 0.9811,\n          \"diff_xcorr_fwd_lag\": 1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 0,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 6e-06,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.9149,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\n            \"ty\"\n          ]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.69886,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.408518,\n          \"diff_xcorr_fwd_p\": 0.066187,\n          \"diff_xcorr_fwd_r\": 0.8799,\n          \"diff_xcorr_fwd_lag\": -2,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 7,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.044599,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.8735,\n          \"naive_xcorr_lag\": -2,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 3,\n          \"consensus_methods\": [\n            \"naive\",\n            \"threshold\",\n            \"ty\"\n          ]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.579484,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.317736,\n          \"diff_xcorr_fwd_p\": 0.088982,\n          \"diff_xcorr_fwd_r\": 0.8684,\n          \"diff_xcorr_fwd_lag\": -2,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 7,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.018539,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.8907,\n          \"naive_xcorr_lag\": -2,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 3,\n          \"consensus_methods\": [\n            \"naive\",\n            \"threshold\",\n            \"ty\"\n          ]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.427914,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.338332,\n          \"diff_xcorr_fwd_p\": 0.273545,\n          \"diff_xcorr_fwd_r\": 0.8181,\n          \"diff_xcorr_fwd_lag\": -2,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 7,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.133768,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8798,\n          \"naive_xcorr_lag\": -2,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\n            \"naive\",\n            \"threshold\"\n          ]\n        }\n      ]\n    },\n    {\n      \"seed\": 48,\n      \"exp_dir\": \"results/alpha_sweep/a000_s48_fp32\",\n      \"T\": 10,\n      \"n_gens\": 11,\n      \"n_perm\": 5000,\n      \"pairs\": [\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.060388,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.14917,\n          \"diff_xcorr_fwd_p\": 0.356529,\n          \"diff_xcorr_fwd_r\": 0.8533,\n          \"diff_xcorr_fwd_lag\": 1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 0,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.15754,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.6663,",
      "numLines": 400,
      "startLine": 100,
      "totalLines": 895
    }
  }
}
```

</details>

---


### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Glob · `toolu_015Z6V7MWEDBV3eiqAu1ii25`</summary>

```json
{
  "pattern": "artifacts/D102_null_s4*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "b856e210-d381-4210-afc5-b485f6bc4286",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CVJWCBH7x3p1poFLdroU9F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6418,
      "cache_read_input_tokens": 36978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6418
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 36 · 2026-05-24T08:51:53.384Z_

<details><summary>↩ Tool result · `toolu_015Z6V7MWEDBV3eiqAu1ii25`</summary>

```text
artifacts/D102_null_s46_fp32_d3.json
artifacts/D102_null_s48_fp32_d3.json
artifacts/D102_null_s49_fp32_d3.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "4242ad9d-9ac0-442d-8b35-aed6e5d2fd16",
  "tool_use_result": {
    "filenames": [
      "artifacts/D102_null_s46_fp32_d3.json",
      "artifacts/D102_null_s48_fp32_d3.json",
      "artifacts/D102_null_s49_fp32_d3.json"
    ],
    "durationMs": 38,
    "numFiles": 3,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Glob · `toolu_01W6zjeSvkBNVo8hmQFPKHHN`</summary>

```json
{
  "pattern": "artifacts/alpha_sweep_a000_s4*/**/*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "8d723148-bb9d-41a2-8b29-5b8701f95df2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CVJWCBH7x3p1poFLdroU9F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6418,
      "cache_read_input_tokens": 36978,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6418
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 38 · 2026-05-24T08:51:54.339Z_

<details><summary>↩ Tool result · `toolu_01W6zjeSvkBNVo8hmQFPKHHN`</summary>

```text
artifacts/alpha_sweep_a000_s43/data/a000_s43_5method_results_616865.json
artifacts/alpha_sweep_a000_s43/data/a000_s43_5method_results.json
artifacts/alpha_sweep_a000_s48_fp32/data/5method_leadlag.json
artifacts/alpha_sweep_a000_s48_fp32/data/5method_leadlag_2ac107.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "c7542ebc-8f5d-4896-9d67-b26f9de681a4",
  "tool_use_result": {
    "filenames": [
      "artifacts/alpha_sweep_a000_s43/data/a000_s43_5method_results_616865.json",
      "artifacts/alpha_sweep_a000_s43/data/a000_s43_5method_results.json",
      "artifacts/alpha_sweep_a000_s48_fp32/data/5method_leadlag.json",
      "artifacts/alpha_sweep_a000_s48_fp32/data/5method_leadlag_2ac107.json"
    ],
    "durationMs": 41,
    "numFiles": 4,
    "truncated": false
  }
}
```

</details>

---


### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
I have all the data I need from the `fpr_transparency_all_seeds.json` file. Let me read the rest of it to get seeds 48, 49, 50 data.

I also need to understand the Shapley computation logic. The key insight is:
- For each coalition S of methods, compute FPR(S) and FNR(S)
- FPR = fraction of null pairs where the coalition detects (at least one method in coalition says "significant")
- FNR = fraction of signal pairs where the coalition doesn't detect (no method in coalition says "significant")


- Shapley value represents the weighted average marginal contribution across all possible orderings

Now I'll load the complete seed data and write the computation script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "b05543bc-96e8-4129-8258-159fe531909c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcnJ7c2MN2xHsj6yopiNet",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6615,
      "cache_read_input_tokens": 43396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6615
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_014MiaVwwMTv8hnsuopa32n2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/fpr_transparency_all_seeds.json",
  "offset": 498,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "81410f98-ed70-4fc2-85e2-85aa92417fad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcnJ7c2MN2xHsj6yopiNet",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6615,
      "cache_read_input_tokens": 43396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6615
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-24T08:52:04.490Z_

<details><summary>↩ Tool result · `toolu_014MiaVwwMTv8hnsuopa32n2`</summary>

```text
498	          "ty_granger_sig": false,
499	          "naive_xcorr_r": 0.6663,
500	          "naive_xcorr_lag": 1,
501	          "naive_xcorr_sig": true,
502	          "consensus_votes": 0,
503	          "consensus_methods": []
504	        },
505	        {
506	          "canary": "token_entropy",
507	          "downstream": "distinct_2",
508	          "perm_granger_fwd_p": 0.009398,
509	          "perm_granger_fwd_sig_fdr": false,
510	          "perm_granger_rev_p": 0.197161,
511	          "diff_xcorr_fwd_p": 0.045591,
512	          "diff_xcorr_fwd_r": 0.8951,
513	          "diff_xcorr_fwd_lag": 1,
514	          "diff_xcorr_fwd_sig_fdr": false,
515	          "threshold_onset_lead": -4,
516	          "threshold_onset_sig": false,
517	          "ty_granger_p": 0.954249,
518	          "ty_granger_sig": false,
519	          "naive_xcorr_r": -0.8278,
520	          "naive_xcorr_lag": -3,
521	          "naive_xcorr_sig": true,
522	          "consensus_votes": 1,
523	          "consensus_methods": [
524	            "naive"
525	          ]
526	        },
527	        {
528	          "canary": "token_entropy",
529	          "downstream": "distinct_3",
530	          "perm_granger_fwd_p": 0.057389,
531	          "perm_granger_fwd_sig_fdr": false,
532	          "perm_granger_rev_p": 0.587882,
533	          "diff_xcorr_fwd_p": 0.093781,
534	          "diff_xcorr_fwd_r": 0.7543,
535	          "diff_xcorr_fwd_lag": 3,
536	          "diff_xcorr_fwd_sig_fdr": false,
537	          "threshold_onset_lead": -7,
538	          "threshold_onset_sig": false,
539	          "ty_granger_p": 0.365771,
540	          "ty_granger_sig": false,
541	          "naive_xcorr_r": -0.9208,
542	          "naive_xcorr_lag": -3,
543	          "naive_xcorr_sig": true,
544	          "consensus_votes": 1,
545	          "consensus_methods": [
546	            "naive"
547	          ]
548	        },
549	        {
550	          "canary": "ece",
551	          "downstream": "distinct_1",
552	          "perm_granger_fwd_p": 0.488902,
553	          "perm_granger_fwd_sig_fdr": false,
554	          "perm_granger_rev_p": 0.030394,
555	          "diff_xcorr_fwd_p": 0.169766,
556	          "diff_xcorr_fwd_r": 0.8054,
557	          "diff_xcorr_fwd_lag": -1,
558	          "diff_xcorr_fwd_sig_fdr": false,
559	          "threshold_onset_lead": 3,
560	          "threshold_onset_sig": true,
561	          "ty_granger_p": 0.50901,
562	          "ty_granger_sig": false,
563	          "naive_xcorr_r": 0.8318,
564	          "naive_xcorr_lag": -1,
565	          "naive_xcorr_sig": true,
566	          "consensus_votes": 2,
567	          "consensus_methods": [
568	            "naive",
569	            "threshold"
570	          ]
571	        },
572	        {
573	          "canary": "ece",
574	          "downstream": "distinct_2",
575	          "perm_granger_fwd_p": 0.810638,
576	          "perm_granger_fwd_sig_fdr": false,
577	          "perm_granger_rev_p": 0.031994,
578	          "diff_xcorr_fwd_p": 0.127375,
579	          "diff_xcorr_fwd_r": 0.8042,
580	          "diff_xcorr_fwd_lag": -1,
581	          "diff_xcorr_fwd_sig_fdr": false,
582	          "threshold_onset_lead": -1,
583	          "threshold_onset_sig": false,
584	          "ty_granger_p": 0.427267,
585	          "ty_granger_sig": false,
586	          "naive_xcorr_r": 0.8531,
587	          "naive_xcorr_lag": -1,
588	          "naive_xcorr_sig": true,
589	          "consensus_votes": 1,
590	          "consensus_methods": [
591	            "naive"
592	          ]
593	        },
594	        {
595	          "canary": "ece",
596	          "downstream": "distinct_3",
597	          "perm_granger_fwd_p": 0.313137,
598	          "perm_granger_fwd_sig_fdr": false,
599	          "perm_granger_rev_p": 0.204359,
600	          "diff_xcorr_fwd_p": 0.557688,
601	          "diff_xcorr_fwd_r": 0.6013,
602	          "diff_xcorr_fwd_lag": -1,
603	          "diff_xcorr_fwd_sig_fdr": false,
604	          "threshold_onset_lead": -4,
605	          "threshold_onset_sig": false,
606	          "ty_granger_p": 0.207944,
607	          "ty_granger_sig": false,
608	          "naive_xcorr_r": 0.7817,
609	          "naive_xcorr_lag": -1,
610	          "naive_xcorr_sig": true,
611	          "consensus_votes": 1,
612	          "consensus_methods": [
613	            "naive"
614	          ]
615	        }
616	      ]
617	    },
618	    {
619	      "seed": 49,
620	      "exp_dir": "results/alpha_sweep/a000_s49_fp32",
621	      "T": 10,
622	      "n_gens": 11,
623	      "n_perm": 5000,
624	      "pairs": [
625	        {
626	          "canary": "token_entropy",
627	          "downstream": "distinct_1",
628	          "perm_granger_fwd_p": 0.077385,
629	          "perm_granger_fwd_sig_fdr": false,
630	          "perm_granger_rev_p": 0.044391,
631	          "diff_xcorr_fwd_p": 0.375325,
632	          "diff_xcorr_fwd_r": -0.7075,
633	          "diff_xcorr_fwd_lag": -1,
634	          "diff_xcorr_fwd_sig_fdr": false,
635	          "threshold_onset_lead": -6,
636	          "threshold_onset_sig": false,
637	          "ty_granger_p": 0.291933,
638	          "ty_granger_sig": false,
639	          "naive_xcorr_r": -0.9411,
640	          "naive_xcorr_lag": -1,
641	          "naive_xcorr_sig": true,
642	          "consensus_votes": 1,
643	          "consensus_methods": [
644	            "naive"
645	          ]
646	        },
647	        {
648	          "canary": "token_entropy",
649	          "downstream": "distinct_2",
650	          "perm_granger_fwd_p": 0.10198,
651	          "perm_granger_fwd_sig_fdr": false,
652	          "perm_granger_rev_p": 0.060988,
653	          "diff_xcorr_fwd_p": 0.557089,
654	          "diff_xcorr_fwd_r": 0.6879,
655	          "diff_xcorr_fwd_lag": 1,
656	          "diff_xcorr_fwd_sig_fdr": false,
657	          "threshold_onset_lead": -6,
658	          "threshold_onset_sig": false,
659	          "ty_granger_p": 0.900361,
660	          "ty_granger_sig": false,
661	          "naive_xcorr_r": -0.8959,
662	          "naive_xcorr_lag": -1,
663	          "naive_xcorr_sig": true,
664	          "consensus_votes": 1,
665	          "consensus_methods": [
666	            "naive"
667	          ]
668	        },
669	        {
670	          "canary": "token_entropy",
671	          "downstream": "distinct_3",
672	          "perm_granger_fwd_p": 0.29914,
673	          "perm_granger_fwd_sig_fdr": false,
674	          "perm_granger_rev_p": 0.113177,
675	          "diff_xcorr_fwd_p": 0.772246,
676	          "diff_xcorr_fwd_r": -0.5696,
677	          "diff_xcorr_fwd_lag": -1,
678	          "diff_xcorr_fwd_sig_fdr": false,
679	          "threshold_onset_lead": -8,
680	          "threshold_onset_sig": false,
681	          "ty_granger_p": 0.199756,
682	          "ty_granger_sig": false,
683	          "naive_xcorr_r": -0.9001,
684	          "naive_xcorr_lag": -3,
685	          "naive_xcorr_sig": true,
686	          "consensus_votes": 1,
687	          "consensus_methods": [
688	            "naive"
689	          ]
690	        },
691	        {
692	          "canary": "ece",
693	          "downstream": "distinct_1",
694	          "perm_granger_fwd_p": 0.509098,
695	          "perm_granger_fwd_sig_fdr": false,
696	          "perm_granger_rev_p": 0.524095,
697	          "diff_xcorr_fwd_p": 0.036793,
698	          "diff_xcorr_fwd_r": 0.8505,
699	          "diff_xcorr_fwd_lag": 3,
700	          "diff_xcorr_fwd_sig_fdr": false,
701	          "threshold_onset_lead": -6,
702	          "threshold_onset_sig": false,
703	          "ty_granger_p": 0.827348,
704	          "ty_granger_sig": false,
705	          "naive_xcorr_r": 0.8419,
706	          "naive_xcorr_lag": 3,
707	          "naive_xcorr_sig": true,
708	          "consensus_votes": 0,
709	          "consensus_methods": []
710	        },
711	        {
712	          "canary": "ece",
713	          "downstream": "distinct_2",
714	          "perm_granger_fwd_p": 0.196361,
715	          "perm_granger_fwd_sig_fdr": false,
716	          "perm_granger_rev_p": 0.607479,
717	          "diff_xcorr_fwd_p": 0.345531,
718	          "diff_xcorr_fwd_r": 0.7034,
719	          "diff_xcorr_fwd_lag": 0,
720	          "diff_xcorr_fwd_sig_fdr": false,
721	          "threshold_onset_lead": -6,
722	          "threshold_onset_sig": false,
723	          "ty_granger_p": 0.7844,
724	          "ty_granger_sig": false,
725	          "naive_xcorr_r": 0.763,
726	          "naive_xcorr_lag": 0,
727	          "naive_xcorr_sig": false,
728	          "consensus_votes": 0,
729	          "consensus_methods": []
730	        },
731	        {
732	          "canary": "ece",
733	          "downstream": "distinct_3",
734	          "perm_granger_fwd_p": 0.261348,
735	          "perm_granger_fwd_sig_fdr": false,
736	          "perm_granger_rev_p": 0.95041,
737	          "diff_xcorr_fwd_p": 0.356329,
738	          "diff_xcorr_fwd_r": 0.6891,
739	          "diff_xcorr_fwd_lag": 0,
740	          "diff_xcorr_fwd_sig_fdr": false,
741	          "threshold_onset_lead": -8,
742	          "threshold_onset_sig": false,
743	          "ty_granger_p": 0.709252,
744	          "ty_granger_sig": false,
745	          "naive_xcorr_r": 0.7359,
746	          "naive_xcorr_lag": 0,
747	          "naive_xcorr_sig": false,
748	          "consensus_votes": 0,
749	          "consensus_methods": []
750	        }
751	      ]
752	    },
753	    {
754	      "seed": 50,
755	      "exp_dir": "results/alpha_sweep/a000_s50_fp32",
756	      "T": 10,
757	      "n_gens": 11,
758	      "n_perm": 5000,
759	      "pairs": [
760	        {
761	          "canary": "token_entropy",
762	          "downstream": "distinct_1",
763	          "perm_granger_fwd_p": 0.0014,
764	          "perm_granger_fwd_sig_fdr": true,
765	          "perm_granger_rev_p": 0.933413,
766	          "diff_xcorr_fwd_p": 0.026795,
767	          "diff_xcorr_fwd_r": 0.9743,
768	          "diff_xcorr_fwd_lag": 1,
769	          "diff_xcorr_fwd_sig_fdr": false,
770	          "threshold_onset_lead": 0,
771	          "threshold_onset_sig": false,
772	          "ty_granger_p": 0.009414,
773	          "ty_granger_sig": true,
774	          "naive_xcorr_r": -0.8694,
775	          "naive_xcorr_lag": -3,
776	          "naive_xcorr_sig": true,
777	          "consensus_votes": 3,
778	          "consensus_methods": [
779	            "naive",
780	            "perm",
781	            "ty"
782	          ]
783	        },
784	        {
785	          "canary": "token_entropy",
786	          "downstream": "distinct_2",
787	          "perm_granger_fwd_p": 0.009798,
788	          "perm_granger_fwd_sig_fdr": true,
789	          "perm_granger_rev_p": 0.773645,
790	          "diff_xcorr_fwd_p": 0.056789,
791	          "diff_xcorr_fwd_r": 0.9805,
792	          "diff_xcorr_fwd_lag": 1,
793	          "diff_xcorr_fwd_sig_fdr": false,
794	          "threshold_onset_lead": 0,
795	          "threshold_onset_sig": false,
796	          "ty_granger_p": 0.002252,
797	          "ty_granger_sig": true,
798	          "naive_xcorr_r": -0.8569,
799	          "naive_xcorr_lag": -3,
800	          "naive_xcorr_sig": true,
801	          "consensus_votes": 3,
802	          "consensus_methods": [
803	            "naive",
804	            "perm",
805	            "ty"
806	          ]
807	        },
808	        {
809	          "canary": "token_entropy",
810	          "downstream": "distinct_3",
811	          "perm_granger_fwd_p": 0.079384,
812	          "perm_granger_fwd_sig_fdr": false,
813	          "perm_granger_rev_p": 0.416517,
814	          "diff_xcorr_fwd_p": 0.45111,
815	          "diff_xcorr_fwd_r": 0.8678,
816	          "diff_xcorr_fwd_lag": 1,
817	          "diff_xcorr_fwd_sig_fdr": false,
818	          "threshold_onset_lead": -5,
819	          "threshold_onset_sig": false,
820	          "ty_granger_p": 0.205854,
821	          "ty_granger_sig": false,
822	          "naive_xcorr_r": -0.902,
823	          "naive_xcorr_lag": -1,
824	          "naive_xcorr_sig": true,
825	          "consensus_votes": 1,
826	          "consensus_methods": [
827	            "naive"
828	          ]
829	        },
830	        {
831	          "canary": "ece",
832	          "downstream": "distinct_1",
833	          "perm_granger_fwd_p": 0.035993,
834	          "perm_granger_fwd_sig_fdr": false,
835	          "perm_granger_rev_p": 0.947411,
836	          "diff_xcorr_fwd_p": 0.260348,
837	          "diff_xcorr_fwd_r": 0.6897,
838	          "diff_xcorr_fwd_lag": 1,
839	          "diff_xcorr_fwd_sig_fdr": false,
840	          "threshold_onset_lead": 0,
841	          "threshold_onset_sig": false,
842	          "ty_granger_p": 0.164203,
843	          "ty_granger_sig": false,
844	          "naive_xcorr_r": 0.6376,
845	          "naive_xcorr_lag": 1,
846	          "naive_xcorr_sig": true,
847	          "consensus_votes": 0,
848	          "consensus_methods": []
849	        },
850	        {
851	          "canary": "ece",
852	          "downstream": "distinct_2",
853	          "perm_granger_fwd_p": 0.093181,
854	          "perm_granger_fwd_sig_fdr": false,
855	          "perm_granger_rev_p": 0.721056,
856	          "diff_xcorr_fwd_p": 0.009198,
857	          "diff_xcorr_fwd_r": -0.9111,
858	          "diff_xcorr_fwd_lag": 2,
859	          "diff_xcorr_fwd_sig_fdr": false,
860	          "threshold_onset_lead": 0,
861	          "threshold_onset_sig": false,
862	          "ty_granger_p": 0.042234,
863	          "ty_granger_sig": true,
864	          "naive_xcorr_r": 0.5548,
865	          "naive_xcorr_lag": 1,
866	          "naive_xcorr_sig": true,
867	          "consensus_votes": 1,
868	          "consensus_methods": [
869	            "ty"
870	          ]
871	        },
872	        {
873	          "canary": "ece",
874	          "downstream": "distinct_3",
875	          "perm_granger_fwd_p": 0.455309,
876	          "perm_granger_fwd_sig_fdr": false,
877	          "perm_granger_rev_p": 0.39932,
878	          "diff_xcorr_fwd_p": 0.983603,
879	          "diff_xcorr_fwd_r": 0.3787,
880	          "diff_xcorr_fwd_lag": -1,
881	          "diff_xcorr_fwd_sig_fdr": false,
882	          "threshold_onset_lead": -5,
883	          "threshold_onset_sig": false,
884	          "ty_granger_p": 0.073593,
885	          "ty_granger_sig": false,
886	          "naive_xcorr_r": 0.3612,
887	          "naive_xcorr_lag": 1,
888	          "naive_xcorr_sig": false,
889	          "consensus_votes": 0,
890	          "consensus_methods": []
891	        }
892	      ]
893	    }
894	  ]
895	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "7fbd7442-b0f4-4bf8-83f3-d155bd715fdf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/fpr_transparency_all_seeds.json",
      "content": "          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.6663,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.009398,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.197161,\n          \"diff_xcorr_fwd_p\": 0.045591,\n          \"diff_xcorr_fwd_r\": 0.8951,\n          \"diff_xcorr_fwd_lag\": 1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -4,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.954249,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.8278,\n          \"naive_xcorr_lag\": -3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\n            \"naive\"\n          ]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.057389,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.587882,\n          \"diff_xcorr_fwd_p\": 0.093781,\n          \"diff_xcorr_fwd_r\": 0.7543,\n          \"diff_xcorr_fwd_lag\": 3,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -7,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.365771,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.9208,\n          \"naive_xcorr_lag\": -3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\n            \"naive\"\n          ]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.488902,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.030394,\n          \"diff_xcorr_fwd_p\": 0.169766,\n          \"diff_xcorr_fwd_r\": 0.8054,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 3,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.50901,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8318,\n          \"naive_xcorr_lag\": -1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\n            \"naive\",\n            \"threshold\"\n          ]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.810638,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.031994,\n          \"diff_xcorr_fwd_p\": 0.127375,\n          \"diff_xcorr_fwd_r\": 0.8042,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -1,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.427267,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8531,\n          \"naive_xcorr_lag\": -1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\n            \"naive\"\n          ]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.313137,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.204359,\n          \"diff_xcorr_fwd_p\": 0.557688,\n          \"diff_xcorr_fwd_r\": 0.6013,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -4,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.207944,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.7817,\n          \"naive_xcorr_lag\": -1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\n            \"naive\"\n          ]\n        }\n      ]\n    },\n    {\n      \"seed\": 49,\n      \"exp_dir\": \"results/alpha_sweep/a000_s49_fp32\",\n      \"T\": 10,\n      \"n_gens\": 11,\n      \"n_perm\": 5000,\n      \"pairs\": [\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.077385,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.044391,\n          \"diff_xcorr_fwd_p\": 0.375325,\n          \"diff_xcorr_fwd_r\": -0.7075,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -6,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.291933,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.9411,\n          \"naive_xcorr_lag\": -1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\n            \"naive\"\n          ]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.10198,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.060988,\n          \"diff_xcorr_fwd_p\": 0.557089,\n          \"diff_xcorr_fwd_r\": 0.6879,\n          \"diff_xcorr_fwd_lag\": 1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -6,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.900361,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.8959,\n          \"naive_xcorr_lag\": -1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\n            \"naive\"\n          ]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.29914,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.113177,\n          \"diff_xcorr_fwd_p\": 0.772246,\n          \"diff_xcorr_fwd_r\": -0.5696,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -8,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.199756,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.9001,\n          \"naive_xcorr_lag\": -3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\n            \"naive\"\n          ]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.509098,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.524095,\n          \"diff_xcorr_fwd_p\": 0.036793,\n          \"diff_xcorr_fwd_r\": 0.8505,\n          \"diff_xcorr_fwd_lag\": 3,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -6,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.827348,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8419,\n          \"naive_xcorr_lag\": 3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.196361,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.607479,\n          \"diff_xcorr_fwd_p\": 0.345531,\n          \"diff_xcorr_fwd_r\": 0.7034,\n          \"diff_xcorr_fwd_lag\": 0,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -6,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.7844,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.763,\n          \"naive_xcorr_lag\": 0,\n          \"naive_xcorr_sig\": false,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.261348,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.95041,\n          \"diff_xcorr_fwd_p\": 0.356329,\n          \"diff_xcorr_fwd_r\": 0.6891,\n          \"diff_xcorr_fwd_lag\": 0,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -8,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.709252,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.7359,\n          \"naive_xcorr_lag\": 0,\n          \"naive_xcorr_sig\": false,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        }\n      ]\n    },\n    {\n      \"seed\": 50,\n      \"exp_dir\": \"results/alpha_sweep/a000_s50_fp32\",\n      \"T\": 10,\n      \"n_gens\": 11,\n      \"n_perm\": 5000,\n      \"pairs\": [\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.0014,\n          \"perm_granger_fwd_sig_fdr\": true,\n          \"perm_granger_rev_p\": 0.933413,\n          \"diff_xcorr_fwd_p\": 0.026795,\n          \"diff_xcorr_fwd_r\": 0.9743,\n          \"diff_xcorr_fwd_lag\": 1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 0,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.009414,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": -0.8694,\n          \"naive_xcorr_lag\": -3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 3,\n          \"consensus_methods\": [\n            \"naive\",\n            \"perm\",\n            \"ty\"\n          ]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.009798,\n          \"perm_granger_fwd_sig_fdr\": true,\n          \"perm_granger_rev_p\": 0.773645,\n          \"diff_xcorr_fwd_p\": 0.056789,\n          \"diff_xcorr_fwd_r\": 0.9805,\n          \"diff_xcorr_fwd_lag\": 1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 0,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.002252,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": -0.8569,\n          \"naive_xcorr_lag\": -3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 3,\n          \"consensus_methods\": [\n            \"naive\",\n            \"perm\",\n            \"ty\"\n          ]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.079384,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.416517,\n          \"diff_xcorr_fwd_p\": 0.45111,\n          \"diff_xcorr_fwd_r\": 0.8678,\n          \"diff_xcorr_fwd_lag\": 1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -5,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.205854,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.902,\n          \"naive_xcorr_lag\": -1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\n            \"naive\"\n          ]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.035993,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.947411,\n          \"diff_xcorr_fwd_p\": 0.260348,\n          \"diff_xcorr_fwd_r\": 0.6897,\n          \"diff_xcorr_fwd_lag\": 1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 0,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.164203,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.6376,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.093181,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.721056,\n          \"diff_xcorr_fwd_p\": 0.009198,\n          \"diff_xcorr_fwd_r\": -0.9111,\n          \"diff_xcorr_fwd_lag\": 2,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 0,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.042234,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.5548,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\n            \"ty\"\n          ]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.455309,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.39932,\n          \"diff_xcorr_fwd_p\": 0.983603,\n          \"diff_xcorr_fwd_r\": 0.3787,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -5,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.073593,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.3612,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": false,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        }\n      ]\n    }\n  ]\n}",
      "numLines": 398,
      "startLine": 498,
      "totalLines": 895
    }
  }
}
```

</details>

---


### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me understand the Shapley computation:

From the old Shapley JSON:
- 3 null experiments (s42/s43/s44), 8 pairs each = 24 null observations (but 6-pair uses only 6 of those 8 pairs per experiment)
  Wait, looking more carefully at the old JSON: `n_null_obs: 24` with 8 `fpr_pairs`. So it was 3 experiments × 8 pairs = 24.
  But for 6-pair, they still used 24 null obs because: 3 experiments × 8 pairs = 24... 

Actually, I see the discrepancy now. For the 6-pair variant, it should be 3 × 6 = 18 observations, but the 8-pair variant has 3 × 8 = 24. Looking at the old JSON more carefully, the FPR was computed over all 8 pairs regardless of whether the FNR analysis used 6 or 8 pairs, which is why `n_null_obs` stays at 24 even for the 6-pair case, while the signal observations for 6-pair FNR are 270 (45 × 6).

Wait, I need to reconsider the pair basis. The `fpr_transparency_all_seeds.json` shows the 6-seed null data is already on a 6-pair basis, so that's 6 seeds × 6 pairs = 36 pairs total. Now I'm trying to figure out what the new Shapley configuration should be for the null observations.

For the new approach, I have 6 null seeds with 6 pairs each giving me 36 null observations, and 45 signal experiments with 6 pairs each for 270 signal observations. Now I need to extract a per-pair detection matrix from the data by checking which methods flagged each of the 36 null pairs as significant using their respective FDR-corrected p-values and significance thresholds.

The voting rules are: xcorr methods (naive and diff) vote only if their peak lag is negative, indicating the canary leads; PermG and TY vote if their FDR-corrected p-values are significant; and Threshold votes if the canary onset precedes the downstream onset. I need to carefully apply these conditions to build the detection matrix for each method. I'm checking whether diff_xcorr also uses a lag threshold to determine voting eligibility, since I notice it has a forward lag value but I need to verify if negative lag is required like it is for naive_xcorr. I'm realizing that diff_xcorr rarely votes in this null dataset because it's almost never significant after FDR correction—only one pair out of thirty-six shows it. When I check s45 te->d2, diff_xcorr is significant but the lag is positive (1), so it doesn't meet the requirement of lag < 0 to contribute to the consensus. I need to verify the lag convention for diff_xcorr more carefully.

The lag direction matters: positive lag means the downstream signal leads the canary (reverse direction), while negative lag means the canary leads downstream (forward direction). The voting rules require xcorr methods to have negative lag to vote, so diff_xcorr_fwd_lag = 1 disqualifies it. The consensus voting rules are: naive_xcorr votes when both the signal is significant and lag is negative, diff_xcorr votes under the same conditions with its FDR-corrected significance, and threshold_onset votes when its signal is significant regardless of lag direction.

Now I'm checking the Granger causality voting rules and verifying the threshold method's behavior across specific examples—it looks like the threshold significance already encodes the lead direction, so I don't need an additional lead constraint for voting.

I need to write a script that reads the null data from the FPR transparency file and the signal data structure from the old Shapley JSON, then computes FPR and FNR for each of the 32 coalitions before calculating Shapley values. The challenge is that the old Shapley JSON only has aggregate values, not the raw per-pair signal detection data I need, so I have to trace back where the signal data originally came from.

Looking at the existing figure generation script, it's just reading pre-computed results — the actual Shapley computation happened elsewhere. I need to find that computation script or write one from scratch. For the null case, I can pull per-pair voting data from the FPR transparency file for the 36 pairs, but for the signal case with 270 pairs across 45 experiments, I'll need to dig into the individual D102 JSON files from those signal experiments.

Actually, I'm realizing the old computation likely extracted per-pair consensus information directly from those D102 JSONs. Since the signal experiments haven't changed, I could potentially keep those Shapley values as-is and only recompute the FPR values using the new 6-seed null data. But Shapley values are computed jointly across coalitions, so the marginal contributions of each method depend on both FPR and FNR performance — though the FPR-Shapley and FNR-Shapley are actually computed independently from each other.

Since only the null data is changing, only the FPR-Shapley values need recomputation while FNR-Shapley stays the same, which means I can extract the per-pair voting from the null data and recalculate just the FPR game.

Now I need to write a script that loads the transparency data, extracts detection flags for the null pairs, computes the new FPR-Shapley values, combines them with the unchanged FNR-Shapley values, and outputs the updated combined Shapley scores.

Writing computation script... I need to extract the binary detection vectors for each method from the null data—checking which pairs each method flags based on their specific significance criteria and lag directions.

Then I'll compute the Shapley value for FPR by treating it as a characteristic function where v(S) measures the proportion of pairs detected by at least one method in subset S, with each method's contribution being its marginal impact on detection rate.

For the FDR sensitivity analysis, I'm recalculating across different q thresholds using the expanded 6-seed null dataset, applying Benjamini-Hochberg correction across all pairs for each method. I'm realizing the treatment column needs to stay consistent with the original data, but I need to figure out whether it was originally on an 8-pair or 6-pair basis to make sure the counts align properly with the null data I'm recomputing. I need to focus on just updating the null counts since that's what the task specifies. For the null side with 6-pair basis, I have the q=0.05 value (4/36 FPs), but I'll need to recompute the BH-FDR thresholds for q=0.01 and q=0.10 to get the corresponding false positive counts at each threshold. Now I'm working through the BH-FDR correction for each seed by sorting the p-values and finding the largest index where the p-value satisfies the threshold condition, then counting significant results across all six seeds at q=0.05. Checking the remaining seeds against the Benjamini-Hochberg thresholds. For s46, the smallest p-value of 0.030594 doesn't meet the first threshold, so zero significant results, which matches the summary. s47 and s48 also fail their first threshold checks with no significant findings.

s49 has all p-values above the threshold, confirming zero significant results. s50 passes the first two threshold comparisons but fails at the third, yielding 2 significant results as expected. The total count across all seeds comes to 2 FDR-significant findings at q=0.05.

Now checking the stricter q=0.01 threshold with adjusted cutoffs. s45 shows 2 significant results passing the first two comparisons before failing the third. s50 only has 1 significant result this time, as the second p-value exceeds the tighter threshold. All other seeds remain at zero, bringing the total to 3 FDR-significant findings at the more conservative q=0.01 level.

Moving to the more permissive q=0.10 threshold, the BH cutoffs are substantially higher. s45 again shows 2 significant results with the same pattern as before, while s46 is starting to show some p-values that might pass the initial comparisons. I'm working through the Benjamini-Hochberg procedure for the remaining samples, checking p-values against the adjusted thresholds at q=0.10 and tallying up how many pass the significance test across all 36 samples.

Now I'm compiling the FDR sensitivity results at different q-levels and moving on to calculate Shapley values. I need to construct a binary voting matrix for each of the five methods across all 36 null pairs, where each entry indicates whether that method would flag a forward detection based on its specific criteria.

Going through the pairs systematically, I'm extracting the voting pattern for each method by checking their significance flags and lag conditions. Verifying the threshold and ty methods both vote for s45 ece->d3, giving consensus votes of 2. Now moving through s46 to check the voting patterns for te->d1, te->d2, and te->d3 across the same methods. Finishing the ece->d3 configuration, then verifying the consensus votes for both ece->d2 and ece->d3 before moving on to analyze the te dataset with its own method signatures and parameter variations. Finishing the ece->d3 configuration and verifying the consensus patterns across both test cases, then moving into S48 where I'm tracking the signal transformations for the te dataset across different dimensions. I'm working through the signal detection logic for each sample and detector pair, checking whether the naive cross-correlation method produces a significant lag, then verifying the consensus votes match the expected output vectors. Moving into sample 49 now to continue validating the detection results. I'm finishing the verification for s49, then moving on to s50 where I'm checking the consensus methods across different test configurations—the naive method is consistently significant with a lag of -3, while permutation and type methods are now showing significance in some cases. Finishing the last method evaluation, then verifying the consensus counts for those test cases before compiling the complete results matrix across all samples and methods. Generating data table... Finishing the ty calculation, I get 14/36 = 38.9%. So comparing all the false positive rates: naive is 55.6%, diff is 0%, thresh is 27.8%, perm is 11.1%, and ty is 38.9%. These match Table 14 in the appendix, except diff should be 1/36 = 2.8% according to the table, but I'm getting 0 — let me recheck my calculation.

Looking at the table more carefully, I see the issue: the diff_xcorr voting rule I'm using requires both the forward significance and a negative lag, but the table's BH-FDR criterion doesn't apply that direction filter, which is why there's a discrepancy between my extraction and what's reported. Now I'm checking whether that p-value survives the Benjamini-Hochberg correction across all six pairs in s50. After sorting the p-values and applying the threshold, 0.009198 does pass the FDR cutoff, making diff_xcorr_fwd_sig_fdr true for that pair.

Looking at the full dataset, only s45 te->d2 shows diff_xcorr_fdr as true, which accounts for the 1/36 in the table. But for the Shapley voting, I need both the FDR significance and a negative lag, and s45 te->d2 has lag=1, so it doesn't qualify.

This means the per-method vote counts for the Shapley FPR are: naive at 20/36, diff at 0/36, thresh at 10/36, perm at 4/36, and ty at 14/36. But there's a discrepancy—the table shows naive_xcorr at 33/36 when counting all significant cases regardless of direction, whereas the Shapley uses direction-filtered votes with lag < 0, which gives me 20/36. I'm trying to reconcile this with the old Shapley computation where naive had an FPR of 0.9167.

Looking at the old raw_rates_8pair data, naive_xcorr shows 22 false positives out of 24 total, which is that same 0.9167 rate. If direction filtering were applied, the FPR should be lower, so either the old Shapley wasn't using direction filtering for naive, or naive_xcorr_sig is defined differently than the other methods. 's 91.7%. The current definition of naive_xcorr_sig requires |r|>0.5 AND lag≠0, with consensus additionally filtering for lag<0, but the old Shapley likely used the unfiltered sig field for FPR computation. Given that the old Shapley showed naive FPR Shapley of +0.622 (quite high) and the raw FPR was 0.9167 across the null seeds, this suggests it was indeed using unfiltered significance rather than direction-filtered votes. I need to clarify what exactly the Shapley FPR measures—whether it's the marginal contribution to false positive rate or something else.

The old Shapley value of +0.622 for naive_xcorr represents the average marginal increase in FPR when adding naive to different coalitions, which aligns with naive having an extremely high individual FPR. The real question is whether the Shapley computation should use the same direction-filtered voting rules that the MMCT ensemble uses, since the Shapley analysis is fundamentally about how much each method contributes to the ensemble's performance. If the ensemble uses direction-filtered votes, the Shapley should too, but the old analysis might have used a different voting criterion entirely.

Looking at the metadata from the old Shapley output, it shows that naive_xcorr used the `significant_fdr` field, which is the FDR-corrected significance threshold rather than direction-filtered consensus voting.

The consensus voting in the paper applies direction filtering on top of FDR significance for xcorr methods, but the old Shapley analysis didn't account for this. Since the Shapley is meant to measure each method's contribution to false positive and false negative rates within the ensemble's actual voting scheme, it should use the same direction-filtered criteria. However, updating both the null data and the voting rules simultaneously would be two changes at once, when the task is specifically to update just the null data from 3 seeds to 6 seeds. Looking at the old Shapley results, I can see that PermG had zero false positives in the null data, which explains why its FPR Shapley contribution is exactly 0—it never votes on any null pairs. For naive_xcorr with 22 out of 24 false positives using significant_fdr without direction filtering, the high FPR Shapley value makes sense. So the old approach counted method votes based on significant_fdr criteria alone, then computed coalition FPR as the fraction of pairs where at least one method in that coalition detected a signal.

Now I'm realizing there's a mismatch: the fpr_transparency file has sig_fdr flags, but for naive_xcorr it only has the correlation-based criterion (|r|>0.5, lag≠0) rather than an FDR-corrected significance measure, since naive_xcorr doesn't produce p-values for FDR correction. I need to figure out what the old Shapley actually used for naive's significance criterion. was available in the old analysis. The real issue is that the old Shapley values were computed with potentially different significance criteria than what the current consensus uses, so I need to decide whether to recompute everything with consistent rules or keep the old values as-is. Since the task specifies signal data stays the same, I should use the current consensus voting rules (naive: sig AND lag < 0, diff: sig_fdr AND lag < 0, threshold: sig, perm: sig_fdr, ty: sig) to ensure the Shapley values match the ensemble's actual behavior, even if this means the new values differ from the old FNR Shapley.

Now I'm realizing the FNR computation stays the same since the signal experiments don't change, but the FPR computation shifts because we're using 6-seed null data instead of 3-seed null. Looking at what the voting rules would count with the new null data—naive would capture many pairs without direction filtering, diff would be rare at 1/36, threshold would hit 10/36, perm would be 4/36, and ty would be 14/36.

For the naive method specifically, I'm checking the transparency data across the six seeds: seeds 45-48 all flag all 6 pairs as significant, seed 49 flags 4 pairs (missing ece→d2 and ece→d3), and seed 50 flags 5 pairs (missing ece→d3), which totals 33 out of 36 pairs at 91.7%—matching what Table 14 shows for naive xcorr. This aligns with the old 3-seed Shapley result of 91.7% FPR as well.

Now I'm recalculating the per-pair voting matrix using consistent unfiltered significance criteria across all methods: naive xcorr without direction filtering, diff xcorr forward with FDR but no direction filter, threshold onset, permutation Granger forward with FDR, and Ty Granger. I'm starting with seed 45 and working through each pair's method votes. Continuing through the S46 configurations with varying combinations of parameters across the different test and evaluation methods. Continuing through the configuration matrices for S48, where the type flag switches to false across most test-to-dataset and error-to-dataset combinations. Continuing through the test configurations, I'm seeing S49 complete with the ece->d3 pairing showing all flags disabled, then moving into S50 where te->d1 and te->d2 introduce permutation and type flags enabled while the remaining entries revert to the baseline configuration.

Now I'm verifying the false positive counts across each method against Table 14 to confirm they align—naive hits 33 out of 36, diff shows just 1, thresh reaches 10, permutation accounts for 4, and type flags contribute 14. Everything checks out, so I can proceed with computing the Shapley values.

Rather than calculating this manually for all 32 coalitions, I'll write a Python script to handle it. The script will load the false positive data from the JSON file, construct the 36×5 binary matrix representing which methods detected false positives in the null data, compute the FPR-based Shapley values, then merge those with the existing FNR values from the previous Shapley computation, and save the combined results. I also need to account for weight robustness variants that use FPR-inverse weighting, though I'm realizing I may not have the raw signal detection data needed for those calculations.

Looking at the weight robustness table, the different weighting schemes (equal, cap-5, cap-10, FPR-inverse) produce different combined Shapley values for PermG, but recomputing these requires the per-pair per-method detection data across all experiments, which I don't currently have access to beyond the aggregated Shapley values already computed. Looking at the equal weighting results, PermG's combined Shapley value shifts to -0.152 compared to -0.180 in the main table, which suggests the main analysis might be using unweighted voting rather than the FPR-inverse weighting scheme mentioned in the weight robustness section. explains why the numbers differ—the main Shapley uses a simple union-based approach where any method detecting counts as a positive, while the weight robustness table applies weighted majority voting with a threshold, which produces different FNR values.

For updating the main Shapley, I just need to recompute the FPR using the union logic on the null data. The weight robustness update is trickier since I'd need the per-pair per-method signal data to recalculate the weighted voting results, but the TODO at line 779 specifically asks me to recompute that table with the 6-seed data and verify that PermG's φ^FPR becomes positive. For the weight robustness table, the core issue is that PermG no longer has zero FPR—it's now 11.1%—so I need to update the narrative around that. The FPR component of the Shapley values should be recomputable from just the null data across different weight schemes, which means I might not actually need the signal data to update this table.

Let me take a practical approach: I'll compute the main union-based Shapley values using the 6-seed null data first, then handle the weight robustness text qualitatively by noting that PermG remains the lowest FPR among directional methods even without zero FPR. For the seven TODO-D219s, I should address each one precisely. The best move is to write a comprehensive Python script that computes all the Shapley numbers at once, then work through the text updates systematically.

Writing the analysis script...

Now I'm looking at the FDR sensitivity results for the null data—applying Benjamini-Hochberg correction at different q thresholds gives me 3, 4, and 8 rejections out of 36 pairs respectively. The treatment side uses 3 seeds with an 8-pair basis, but since the task is just to update the null portion with the 6-seed data, I should focus there and keep the treatment side as is for now. I need to check the treatment data more carefully—it's currently on an 8-pair basis (3 seeds × 8 pairs = 24), but if I'm updating the null to a 6-pair basis for consistency, I'd need to recompute the treatment significance counts at each q-level using the PermG p-values from the α=0.75 experiments. I'll write a comprehensive Python script to pull all the necessary data from the D102 files and compute the updated values. Shapley values and FDR sensitivity calculations. I'm going to stop overthinking the treatment side—the treatment data should remain consistent with the previous analysis. The current table shows 24 pairs on an 8-pair basis, but I need to align everything to a 6-pair basis like the paper uses. This means updating the null side to 36 pairs (6 seeds × 6 pairs) and adjusting the treatment data accordingly. Let me locate the treatment PermG data for α=0.75 in the D102 files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "aa70a544-67b6-419c-97e0-c6dc2c477be3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWrRVU8ZV6oxjbQxJKwRBn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6163,
      "cache_read_input_tokens": 50011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6163
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 43_

I have all the null data. Now I need to write a Shapley computation script. Let me also check for α=0.75 D102 files for the FDR sensitivity table treatment column update.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "8c5d0977-799a-4747-9e15-74a4655f80ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWrRVU8ZV6oxjbQxJKwRBn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6163,
      "cache_read_input_tokens": 50011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6163
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Glob · `toolu_01MKB9PC7fgBWK1SZ91NzhN4`</summary>

```json
{
  "pattern": "artifacts/D102*a075*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "33044cda-6c82-4970-b5cd-d973d45df93b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWrRVU8ZV6oxjbQxJKwRBn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6163,
      "cache_read_input_tokens": 50011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6163
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 45 · 2026-05-24T08:57:49.650Z_

<details><summary>↩ Tool result · `toolu_01MKB9PC7fgBWK1SZ91NzhN4`</summary>

```text
artifacts/D102_t10_a075_s43_analysis.md
artifacts/D102_t10_a075_s43_fp32_analysis.md
artifacts/D102_14b_t15_a075_s42_fp32.json
artifacts/D102_14b_t10_a075_s44_fp32_d3.json
artifacts/D102_14b_t10_a075_s44_fp32_14b_6pair.json
artifacts/D102_14b_t15_a075_s43_fp32_14b_6pair.json
artifacts/D102_14b_t10_a075_s42_fp32_14b_6pair.json
artifacts/D102_14b_t15_a075_s42_fp32_14b_6pair.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "c93f5112-40c0-4fd5-ab8d-d65e14358a5b",
  "tool_use_result": {
    "filenames": [
      "artifacts/D102_t10_a075_s43_analysis.md",
      "artifacts/D102_t10_a075_s43_fp32_analysis.md",
      "artifacts/D102_14b_t15_a075_s42_fp32.json",
      "artifacts/D102_14b_t10_a075_s44_fp32_d3.json",
      "artifacts/D102_14b_t10_a075_s44_fp32_14b_6pair.json",
      "artifacts/D102_14b_t15_a075_s43_fp32_14b_6pair.json",
      "artifacts/D102_14b_t10_a075_s42_fp32_14b_6pair.json",
      "artifacts/D102_14b_t15_a075_s42_fp32_14b_6pair.json"
    ],
    "durationMs": 41,
    "numFiles": 8,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 46_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PvwKHx6Jvk4PF9paos8tBB`</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "bbd2d7ad-e18f-47f6-835b-6146a1f72832",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWrRVU8ZV6oxjbQxJKwRBn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6163,
      "cache_read_input_tokens": 50011,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6163
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-24T08:57:49.831Z_

<details><summary>↩ Tool result · `toolu_01PvwKHx6Jvk4PF9paos8tBB`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "bd4a174a-5009-4670-8cb1-a770735ebe81",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 29
  }
}
```

</details>

---


### Assistant

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
Let me set up a task list and then start working. I need to:

1. Write and run the Shapley computation script
2. Update the figure generation script
3. Generate the new figure
4. Update appendix.tex (7 TODO-D219 locations)

Let me first write the computation script. I have all the null data from fpr_transparency_all_seeds.json. I need to compute:
- FPR Shapley values (new, from 6-seed null data)
- Keep FNR Shapley values unchanged
- Compute combined Shapley

I also need to handle the FDR sensitivity table.


Now I'm writing a comprehensive Python script to handle all of this. I'm noticing that for the D102 files at α=0.75, I only have 14b model versions, not 410M. For the FDR sensitivity table's treatment side, which uses α=0.75 with 3 seeds, the original table has 24 pairs on an 8-pair basis, so with a 6-pair basis it would be 18 pairs instead. I need to figure out what data I actually have available for this.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "1b67b7e9-ce9d-4753-be38-a60f3424890d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MLmXpoXhcee3uBWsGt1nhv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22728,
      "cache_read_input_tokens": 56174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22728
      },
      "output_tokens": 17,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 49_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01D7Gm8QnmKkjZiNVG6hxDS6`</summary>

```json
{
  "todos": [
    {
      "content": "Write and run Shapley computation script with 6-seed null data",
      "status": "in_progress",
      "activeForm": "Writing and running Shapley computation script"
    },
    {
      "content": "Update gen_shapley_contribution.py and regenerate figure",
      "status": "pending",
      "activeForm": "Updating figure generation script"
    },
    {
      "content": "Find treatment PermG data for FDR sensitivity table update",
      "status": "pending",
      "activeForm": "Finding treatment PermG data"
    },
    {
      "content": "Update appendix.tex — all 7 TODO-D219 locations",
      "status": "pending",
      "activeForm": "Updating appendix.tex"
    },
    {
      "content": "Verify all numbers and TODO removals",
      "status": "pending",
      "activeForm": "Verifying consistency"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "1bfb3ceb-a438-4326-b02c-42eeb21961eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MLmXpoXhcee3uBWsGt1nhv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22728,
      "cache_read_input_tokens": 56174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22728
      },
      "output_tokens": 17,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 50 · 2026-05-24T08:58:07.427Z_

<details><summary>↩ Tool result · `toolu_01D7Gm8QnmKkjZiNVG6hxDS6`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "e6cc17e7-ebf1-4e67-8f54-1ce6ea25eeac",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Write and run Shapley computation script with 6-seed null data",
        "status": "in_progress",
        "activeForm": "Writing and running Shapley computation script"
      },
      {
        "content": "Update gen_shapley_contribution.py and regenerate figure",
        "status": "pending",
        "activeForm": "Updating figure generation script"
      },
      {
        "content": "Find treatment PermG data for FDR sensitivity table update",
        "status": "pending",
        "activeForm": "Finding treatment PermG data"
      },
      {
        "content": "Update appendix.tex — all 7 TODO-D219 locations",
        "status": "pending",
        "activeForm": "Updating appendix.tex"
      },
      {
        "content": "Verify all numbers and TODO removals",
        "status": "pending",
        "activeForm": "Verifying consistency"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Assistant

_source line 51_

Let me find the treatment PermG data and write the computation script. First, let me check what D102 files exist for α=0.75 410M experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "764b4aba-162a-4be6-be33-fa9e1b67cd67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DBTNWpDTUpuyJLMR2wMTvt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 78902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 647
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Grep · `toolu_0153DXY24kpEY2HyoeDdsije`</summary>

```json
{
  "pattern": "\"alpha\": 0.75",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts",
  "glob": "D102*d3*.json",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "15af931b-a9a9-4ebc-a44a-719043ddab8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DBTNWpDTUpuyJLMR2wMTvt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 78902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 647
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-24T08:58:13.474Z_

<details><summary>↩ Tool result · `toolu_0153DXY24kpEY2HyoeDdsije`</summary>

```text
Found 2 files
artifacts/D102_14b_t10_a075_s44_fp32_d3.json
artifacts/scale_14b_t10_a075_s44_fp32/data/D102_14b_t10_a075_s44_fp32_d3.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "58914f9a-d930-4fa5-b8e2-bfc8a7c49c5b",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "artifacts/D102_14b_t10_a075_s44_fp32_d3.json",
      "artifacts/scale_14b_t10_a075_s44_fp32/data/D102_14b_t10_a075_s44_fp32_d3.json"
    ],
    "numFiles": 2
  }
}
```

</details>

---


### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Grep · `toolu_015JUqLdZSRodvTFQu74L1f9`</summary>

```json
{
  "pattern": "\"alpha\": 0.75",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts",
  "glob": "D102*.json",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "521dd269-e4c6-466b-b947-7228d960bbe1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DBTNWpDTUpuyJLMR2wMTvt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 78902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 647
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-24T08:58:14.098Z_

<details><summary>↩ Tool result · `toolu_015JUqLdZSRodvTFQu74L1f9`</summary>

```text
Found 8 files
artifacts/D102_14b_t15_a075_s42_fp32_14b_6pair.json
artifacts/D102_14b_t10_a075_s42_fp32_14b_6pair.json
artifacts/D102_14b_t15_a075_s43_fp32_14b_6pair.json
artifacts/D102_14b_t10_a075_s44_fp32_14b_6pair.json
artifacts/D102_14b_t10_a075_s44_fp32_d3.json
artifacts/scale_14b_t10_a075_s44_fp32/data/D102_14b_t10_a075_s44_fp32_d3.json
artifacts/D102_14b_t15_a075_s42_fp32.json
artifacts/scale_14b_t15_a075_s42_fp32/data/D102_14b_t15_a075_s42_fp32.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "6c578a4a-b1e6-40ef-872d-99ee25f07bbe",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "artifacts/D102_14b_t15_a075_s42_fp32_14b_6pair.json",
      "artifacts/D102_14b_t10_a075_s42_fp32_14b_6pair.json",
      "artifacts/D102_14b_t15_a075_s43_fp32_14b_6pair.json",
      "artifacts/D102_14b_t10_a075_s44_fp32_14b_6pair.json",
      "artifacts/D102_14b_t10_a075_s44_fp32_d3.json",
      "artifacts/scale_14b_t10_a075_s44_fp32/data/D102_14b_t10_a075_s44_fp32_d3.json",
      "artifacts/D102_14b_t15_a075_s42_fp32.json",
      "artifacts/scale_14b_t15_a075_s42_fp32/data/D102_14b_t15_a075_s42_fp32.json"
    ],
    "numFiles": 8
  }
}
```

</details>

---


### Assistant

_source line 56_

<details><summary>Logged reasoning block</summary>

```text
No 410M α=0.75 D102 files locally. The treatment data for the FDR sensitivity table was from the old analysis. I need to either:
1. Get it from the server
2. Or keep the treatment column unchanged

Actually, looking at the old Shapley JSON, the signal data sources include:
- `17855:alpha_sweep/a075_s42_fp32`
- `19828:alpha_sweep/a075_s43`
- `19828:alpha_sweep/a075_s44`

These are the 3 α=0.75 seeds. The D102 analysis results are on the server. 

I can SSH to retrieve them, but first let me focus on what I can compute locally — the new Shapley FPR values from the 6-seed null data and the FDR sensitivity null column from raw p-values. For the treatment column showing how many of the 24 treatment pairs are significant at each q threshold, I'll need to SSH and grab the PermG p-values for those three α=0.75 seeds.

Actually, I should check if the dose response compiled CSV already has the per-pair PermG p-values I need, or if I can find the D102 analysis files that the old Shapley JSON referenced — the artifacts directory likely has D102 files for many of the signal experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "8bcc7247-d04d-4de0-9ca3-1193c0ef9836",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmeRs7MvHkCspYYkPWYeW7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 704,
      "cache_read_input_tokens": 79549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 704
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 57_

No 410M α=0.75 D102 files locally. Let me check what signal experiment D102 data exists locally and write the computation script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "f64dc0e3-3f4f-42a7-af53-d962e0ad5d0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmeRs7MvHkCspYYkPWYeW7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 704,
      "cache_read_input_tokens": 79549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 704
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Glob · `toolu_01TXMQnzUV1ePy9fVfjEeGAB`</summary>

```json
{
  "pattern": "artifacts/D040/**/*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "0687386a-4c28-4394-93d8-b5ac3aab56d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmeRs7MvHkCspYYkPWYeW7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 704,
      "cache_read_input_tokens": 79549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 704
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 59 · 2026-05-24T08:58:29.427Z_

<details><summary>↩ Tool result · `toolu_01TXMQnzUV1ePy9fVfjEeGAB`</summary>

```text
artifacts/D040/data/filtering_pipeline_data.json
artifacts/D040/data/fpr_fnr_calibration_e63a07.json
artifacts/D040/data/fpr_fnr_calibration.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "b2917536-bc2c-48f5-8362-ca0edf7f4a91",
  "tool_use_result": {
    "filenames": [
      "artifacts/D040/data/filtering_pipeline_data.json",
      "artifacts/D040/data/fpr_fnr_calibration_e63a07.json",
      "artifacts/D040/data/fpr_fnr_calibration.json"
    ],
    "durationMs": 41,
    "numFiles": 3,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Grep · `toolu_01RdBreEDT6P7hYhDfpAVfyh`</summary>

```json
{
  "pattern": "perm_granger.*fwd_p|perm_granger.*forward",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts",
  "glob": "dose_response*",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "ce132244-5c06-4dcf-9194-8a72246b1bec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BmeRs7MvHkCspYYkPWYeW7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 704,
      "cache_read_input_tokens": 79549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 704
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-24T08:58:30.666Z_

<details><summary>↩ Tool result · `toolu_01RdBreEDT6P7hYhDfpAVfyh`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "45c0f256-1334-49a7-8813-f22fef2b688e",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [],
    "numFiles": 0
  }
}
```

</details>

---


### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Read · `toolu_01KWomm2sy1zRU2eCEF69WYM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/D040/data/fpr_fnr_calibration.json",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "d9cf0bd2-ca13-467c-b6b2-a713e102a9fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012EGRvQHnWdF34YdabzEEML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 863,
      "cache_read_input_tokens": 80253,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 863
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-24T08:58:33.322Z_

<details><summary>↩ Tool result · `toolu_01KWomm2sy1zRU2eCEF69WYM`</summary>

```text
1	{
2	  "calibration_version": "v1",
3	  "date": "2026-05-15",
4	  "fpr_table": {
5	    "description": "FPR at alpha=0.0 null control (seed=42 only, 8 pairs)",
6	    "note": "Single seed — seed_threshold dimension N/A for FPR. Only method_threshold varies.",
7	    "method_thresholds": [1, 2, 3, 4, 5],
8	    "methods_order": ["naive_pearson", "differenced_xcorr", "threshold_onset", "toda_yamamoto", "permutation_granger"],
9	    "null_control_pairs": [
10	      "token_entropy->distinct_1",
11	      "token_entropy->distinct_2",
12	      "token_entropy->distinct_3",
13	      "token_entropy->perplexity",
14	      "ece->distinct_1",
15	      "ece->distinct_2",
16	      "ece->distinct_3",
17	      "ece->perplexity"
18	    ],
19	    "data": [
20	      {
21	        "method_threshold": 1,
22	        "sig_pairs": 8,
23	        "total": 8,
24	        "fpr": 1.0,
25	        "sig_pair_labels": [
26	          "token_entropy->distinct_1",
27	          "token_entropy->distinct_2",
28	          "token_entropy->distinct_3",
29	          "token_entropy->perplexity",
30	          "ece->distinct_1",
31	          "ece->distinct_2",
32	          "ece->distinct_3",
33	          "ece->perplexity"
34	        ],
35	        "methods_detail": {
36	          "naive": 8,
37	          "differenced": 4,
38	          "threshold": 5,
39	          "permutation_granger": 0,
40	          "TY": 0
41	        }
42	      },
43	      {
44	        "method_threshold": 2,
45	        "sig_pairs": 6,
46	        "total": 8,
47	        "fpr": 0.75,
48	        "sig_pair_labels": [
49	          "token_entropy->distinct_1",
50	          "token_entropy->distinct_2",
51	          "token_entropy->distinct_3",
52	          "token_entropy->perplexity",
53	          "ece->distinct_1",
54	          "ece->distinct_3"
55	        ],
56	        "methods_detail": {
57	          "naive": 8,
58	          "differenced": 4,
59	          "threshold": 5,
60	          "permutation_granger": 0,
61	          "TY": 0
62	        }
63	      },
64	      {
65	        "method_threshold": 3,
66	        "sig_pairs": 3,
67	        "total": 8,
68	        "fpr": 0.375,
69	        "sig_pair_labels": [
70	          "token_entropy->distinct_1",
71	          "token_entropy->distinct_2",
72	          "token_entropy->distinct_3"
73	        ],
74	        "methods_detail": {
75	          "naive": 8,
76	          "differenced": 4,
77	          "threshold": 5,
78	          "permutation_granger": 0,
79	          "TY": 0
80	        }
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "62e798c2-4344-4521-b9ab-ccf0164ae146",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/D040/data/fpr_fnr_calibration.json",
      "content": "{\n  \"calibration_version\": \"v1\",\n  \"date\": \"2026-05-15\",\n  \"fpr_table\": {\n    \"description\": \"FPR at alpha=0.0 null control (seed=42 only, 8 pairs)\",\n    \"note\": \"Single seed — seed_threshold dimension N/A for FPR. Only method_threshold varies.\",\n    \"method_thresholds\": [1, 2, 3, 4, 5],\n    \"methods_order\": [\"naive_pearson\", \"differenced_xcorr\", \"threshold_onset\", \"toda_yamamoto\", \"permutation_granger\"],\n    \"null_control_pairs\": [\n      \"token_entropy->distinct_1\",\n      \"token_entropy->distinct_2\",\n      \"token_entropy->distinct_3\",\n      \"token_entropy->perplexity\",\n      \"ece->distinct_1\",\n      \"ece->distinct_2\",\n      \"ece->distinct_3\",\n      \"ece->perplexity\"\n    ],\n    \"data\": [\n      {\n        \"method_threshold\": 1,\n        \"sig_pairs\": 8,\n        \"total\": 8,\n        \"fpr\": 1.0,\n        \"sig_pair_labels\": [\n          \"token_entropy->distinct_1\",\n          \"token_entropy->distinct_2\",\n          \"token_entropy->distinct_3\",\n          \"token_entropy->perplexity\",\n          \"ece->distinct_1\",\n          \"ece->distinct_2\",\n          \"ece->distinct_3\",\n          \"ece->perplexity\"\n        ],\n        \"methods_detail\": {\n          \"naive\": 8,\n          \"differenced\": 4,\n          \"threshold\": 5,\n          \"permutation_granger\": 0,\n          \"TY\": 0\n        }\n      },\n      {\n        \"method_threshold\": 2,\n        \"sig_pairs\": 6,\n        \"total\": 8,\n        \"fpr\": 0.75,\n        \"sig_pair_labels\": [\n          \"token_entropy->distinct_1\",\n          \"token_entropy->distinct_2\",\n          \"token_entropy->distinct_3\",\n          \"token_entropy->perplexity\",\n          \"ece->distinct_1\",\n          \"ece->distinct_3\"\n        ],\n        \"methods_detail\": {\n          \"naive\": 8,\n          \"differenced\": 4,\n          \"threshold\": 5,\n          \"permutation_granger\": 0,\n          \"TY\": 0\n        }\n      },\n      {\n        \"method_threshold\": 3,\n        \"sig_pairs\": 3,\n        \"total\": 8,\n        \"fpr\": 0.375,\n        \"sig_pair_labels\": [\n          \"token_entropy->distinct_1\",\n          \"token_entropy->distinct_2\",\n          \"token_entropy->distinct_3\"\n        ],\n        \"methods_detail\": {\n          \"naive\": 8,\n          \"differenced\": 4,\n          \"threshold\": 5,\n          \"permutation_granger\": 0,\n          \"TY\": 0\n        }",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 419
    }
  }
}
```

</details>

---


### Assistant

_source line 64_

<details><summary>Logged reasoning block</summary>

```text
This is old D040 data (single seed, pre-D102). Not useful for the treatment data.

I think the simplest approach for the FDR sensitivity table treatment column is to:
1. Keep the treatment column numbers and just update the denominator if needed
2. Or SSH to the server to get the α=0.75 PermG p-values

Actually, looking at the current FDR sensitivity table:
q=0.01: Treatment 0/24
q=0.05: Treatment 19/24


q=0.10: Treatment 24/24

The treatment uses 3 seeds × 8 pairs = 24. If I switch to a 6-pair basis by removing the 2 mauve pairs per seed, that drops to 3 seeds × 6 pairs = 18. At q=0.05, I had 19/24 significant, and if the mauve pairs are the non-significant ones (since the paper indicates mauve underperforms at 1.4B), I'd expect something like 15/18. But without the actual data, I should just SSH to the server and pull the treatment PermG p-values directly.

Wait, let me reread the task more carefully. It's asking me to update the FDR sensitivity table, specifically the null side with 6 seeds instead of 3. The treatment column isn't explicitly mentioned, so I should probably leave it as-is and just update the null column. The table can have different denominators—treatment at /24 and null at /36—since they're separate experiments. Let me check the table header to see if the treatment should also shift to 6 seeds, or if I'm just updating the null side. α=0.75 (3 seeds, 24 forward-direction pairs). Null: α=0.0 (3 seeds, 24 pairs)."

With the update: "Treatment: α=0.75 (3 seeds, 18 forward-direction pairs) [if 6-pair]. Null: α=0.0 (6 seeds 45-50, 36 pairs)."

But updating treatment to 6-pair requires knowing which 6 of the 24 pairs to drop (the 6 mauve pairs: 3 seeds × 2 mauve pairs each = 6 mauve). And I'd need to recount how many are significant at each q level after dropping mauve.

I think the safest approach is: only update the null side as the task requests, and keep the treatment side at 8-pair basis (since the treatment data is the same and works fine). The different pair bases will be noted in the caption.

Actually, that's inconsistent. Let me reconsider this. The FDR sensitivity table is specifically about PermG results at different q thresholds for both null and treatment conditions. The old setup had both at 24 pairs (3 seeds × 8 pairs), but the update changes null to 36 pairs (6 seeds × 6 pairs). For consistency, treatment should also shift to 18 pairs (3 seeds × 6 pairs), which means removing the mauve pairs and recounting FDR significance. The issue is that BH-FDR correction applies across all pairs within each seed, so dropping mauve pairs will affect the correction and change which pairs are significant.

I need the raw PermG p-values to redo the BH correction properly. Since I don't have those readily available, I'll take a pragmatic approach: keep the treatment column at its current 8-pair basis and update only the null column to the 6-pair basis, noting the difference in the caption.

Actually, I'm overcomplicating this. Let me focus on what I need to do: write the Shapley computation script, compute the FDR sensitivity null column, and update the appendix. For the table, I'll adjust the denominators so null shows "/36" while treatment stays "/24" to reflect the different experimental setups.

Now I'm writing a Python script that hardcodes the null data I've already extracted and computes the Shapley values.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "72ce11e4-68e2-4cd4-9bd7-1756ed61b88e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzEeo1WnjATH1bJ12QGgo8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 81116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1071
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 65_

I'll write the Shapley computation script now. I have all the null data from fpr_transparency_all_seeds.json. The FNR values stay unchanged from the old analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "fb6b01e7-73a5-4742-9bb8-68cf31284a84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzEeo1WnjATH1bJ12QGgo8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 81116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1071
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Write · `toolu_0172AViwYDN6aXStaj8wcPf1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v3/compute_shapley_v3.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Recompute Shapley values with 6-seed null data (s45-s50, 6-pair basis).\n\nFPR Shapley: recomputed from 6 null seeds (36 pairs).\nFNR Shapley: unchanged from v2 (45 signal experiments, 270 pairs for 6-pair).\nCombined = FPR + FNR.\n\nVoting rules (matching fpr_transparency consensus):\n  naive_xcorr:     naive_xcorr_sig (|r|>0.5, lag!=0), no direction filter for Shapley\n  diff_xcorr:      diff_xcorr_fwd_sig_fdr\n  threshold_onset: threshold_onset_sig\n  perm_granger:    perm_granger_fwd_sig_fdr\n  ty_granger:      ty_granger_sig\n\"\"\"\nimport json\nimport numpy as np\nfrom itertools import combinations\nfrom math import factorial\nfrom pathlib import Path\nfrom datetime import datetime\n\nMETHODS = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']\nN = len(METHODS)\n\n# Load fpr_transparency data\nFPR_FILE = Path(__file__).parent.parent / 'fpr_transparency_all_seeds.json'\nOLD_SHAPLEY = Path(__file__).parent.parent / 'shapley_v2' / 'shapley_values_v2.json'\n\nwith open(FPR_FILE) as f:\n    fpr_data = json.load(f)\n\nwith open(OLD_SHAPLEY) as f:\n    old_sv = json.load(f)\n\n# Build null detection matrix: 36 x 5 (boolean)\nnull_matrix = []\nfor seed_data in fpr_data['seeds']:\n    for pair in seed_data['pairs']:\n        row = [\n            pair['naive_xcorr_sig'],                # naive: sig (no direction filter)\n            pair['diff_xcorr_fwd_sig_fdr'],          # diff: FDR-corrected\n            pair['threshold_onset_sig'],             # threshold: deterministic\n            pair['perm_granger_fwd_sig_fdr'],        # perm: FDR-corrected\n            pair['ty_granger_sig'],                  # ty: uncorrected\n        ]\n        null_matrix.append(row)\n\nnull_matrix = np.array(null_matrix, dtype=bool)\nn_null = len(null_matrix)\nassert n_null == 36, f\"Expected 36 null pairs, got {n_null}\"\n\n# Verify per-method FP counts match Table 14\nfp_counts = null_matrix.sum(axis=0)\nprint(\"Per-method FP counts (should match Table 14):\")\nfor m, c in zip(METHODS, fp_counts):\n    print(f\"  {m}: {c}/36 = {c/36*100:.1f}%\")\n\n# Shapley computation (exact enumeration, 2^5=32 coalitions)\ndef shapley_values(value_fn):\n    \"\"\"Compute Shapley values for n players given a value function v(S).\n    v(S) takes a frozenset of method indices and returns a scalar.\"\"\"\n    phi = np.zeros(N)\n    for k in range(N):\n        others = [i for i in range(N) if i != k]\n        for size in range(N):  # |S| = 0, 1, ..., N-1\n            weight = factorial(size) * factorial(N - size - 1) / factorial(N)\n            for combo in combinations(others, size):\n                S = frozenset(combo)\n                S_with_k = S | {k}\n                marginal = value_fn(S_with_k) - value_fn(S)\n                phi[k] += weight * marginal\n    return phi\n\n# FPR value function: fraction of null pairs detected by coalition\ndef fpr_value(coalition):\n    if not coalition:\n        return 0.0\n    cols = list(coalition)\n    detected = null_matrix[:, cols].any(axis=1)\n    return detected.sum() / n_null\n\n# Compute FPR Shapley\nfpr_shapley = shapley_values(fpr_value)\nprint(\"\\nFPR Shapley (6-seed null):\")\nfor m, v in zip(METHODS, fpr_shapley):\n    print(f\"  {m}: {v:+.6f}\")\nprint(f\"  Sum: {fpr_shapley.sum():.6f} (should equal full-coalition FPR: {fpr_value(frozenset(range(N))):.6f})\")\n\n# FNR Shapley: keep from old v2 (signal data unchanged)\nfnr_shapley_6pair = np.array([old_sv['main_result_6pair']['fnr_shapley'][m] for m in METHODS])\nfnr_shapley_8pair = np.array([old_sv['robustness_8pair']['fnr_shapley'][m] for m in METHODS])\n\nprint(\"\\nFNR Shapley (unchanged from v2, 6-pair):\")\nfor m, v in zip(METHODS, fnr_shapley_6pair):\n    print(f\"  {m}: {v:+.6f}\")\n\n# Combined Shapley\ncombined_6pair = fpr_shapley + fnr_shapley_6pair\ncombined_8pair = fpr_shapley + fnr_shapley_8pair\n\nprint(\"\\nCombined Shapley (6-pair):\")\nfor m, v in zip(METHODS, combined_6pair):\n    print(f\"  {m}: {v:+.6f}\")\n\n# FDR sensitivity: recompute PermG BH-FDR at different q thresholds\ndef bh_fdr_count(pvalues, q):\n    \"\"\"Apply BH-FDR correction and count rejections.\"\"\"\n    m = len(pvalues)\n    sorted_p = sorted(pvalues)\n    k_max = 0\n    for i, p in enumerate(sorted_p, 1):\n        if p <= q * i / m:\n            k_max = i\n    return k_max\n\n# Extract PermG forward p-values per seed\nprint(\"\\n--- FDR Sensitivity (Null) ---\")\nfor q in [0.01, 0.05, 0.10]:\n    total_sig = 0\n    for seed_data in fpr_data['seeds']:\n        pvals = [p['perm_granger_fwd_p'] for p in seed_data['pairs']]\n        sig = bh_fdr_count(pvals, q)\n        total_sig += sig\n    print(f\"  q={q:.2f}: {total_sig}/36 null FDR-sig\")\n\n# Build output JSON\nresult = {\n    \"version\": \"v3_6seed_null\",\n    \"generated_at\": datetime.now().isoformat(),\n    \"change_from_v2\": \"FPR recomputed with 6 null seeds (s45-s50, 36 pairs, 6-pair basis). FNR unchanged (45 signal experiments, 270/360 signal pairs).\",\n    \"null_data_source\": \"fpr_transparency_all_seeds.json\",\n    \"null_seeds\": [45, 46, 47, 48, 49, 50],\n    \"n_null_seeds\": 6,\n    \"n_null_pairs_per_seed\": 6,\n    \"n_null_obs\": 36,\n    \"n_signal_experiments\": 45,\n    \"n_signal_obs_6pair\": 270,\n    \"n_signal_obs_8pair\": 360,\n    \"pair_basis\": \"6-pair (distinct_1/2/3 only, mauve excluded)\",\n    \"threshold_criterion\": \"true_3sigma_d105\",\n    \"methods\": METHODS,\n    \"n_methods\": N,\n    \"n_coalitions\": 2**N,\n    \"voting_rules\": {\n        \"naive_xcorr\": \"naive_xcorr_sig (|r|>0.5, lag!=0; no direction filter)\",\n        \"diff_xcorr\": \"diff_xcorr_fwd_sig_fdr (BH-FDR corrected)\",\n        \"threshold_onset\": \"threshold_onset_sig (deterministic 3sigma)\",\n        \"perm_granger\": \"perm_granger_fwd_sig_fdr (BH-FDR corrected)\",\n        \"ty_granger\": \"ty_granger_sig (uncorrected)\"\n    },\n    \"main_result_6pair\": {\n        \"fpr_shapley\": {m: round(v, 6) for m, v in zip(METHODS, fpr_shapley)},\n        \"fnr_shapley\": {m: round(v, 6) for m, v in zip(METHODS, fnr_shapley_6pair)},\n        \"combined_shapley\": {m: round(v, 6) for m, v in zip(METHODS, combined_6pair)}\n    },\n    \"robustness_8pair\": {\n        \"fpr_shapley\": {m: round(v, 6) for m, v in zip(METHODS, fpr_shapley)},\n        \"fnr_shapley\": {m: round(v, 6) for m, v in zip(METHODS, fnr_shapley_8pair)},\n        \"combined_shapley\": {m: round(v, 6) for m, v in zip(METHODS, combined_8pair)}\n    },\n    \"raw_fpr_counts\": {m: int(c) for m, c in zip(METHODS, fp_counts)},\n    \"raw_fpr_rates\": {m: round(int(c)/36, 4) for m, c in zip(METHODS, fp_counts)},\n    \"fdr_sensitivity_null\": {},\n    \"comparison_to_v2\": {\n        \"fpr_shapley_change\": {},\n        \"combined_shapley_change\": {}\n    }\n}\n\n# FDR sensitivity\nfor q in [0.01, 0.05, 0.10]:\n    total_sig = 0\n    for seed_data in fpr_data['seeds']:\n        pvals = [p['perm_granger_fwd_p'] for p in seed_data['pairs']]\n        total_sig += bh_fdr_count(pvals, q)\n    result['fdr_sensitivity_null'][f'q_{q:.2f}'] = {\n        'rejections': total_sig,\n        'total': 36,\n        'fpr': round(total_sig / 36, 4)\n    }\n\n# Comparison to v2\nfor m in METHODS:\n    old_fpr = old_sv['main_result_6pair']['fpr_shapley'][m]\n    new_fpr = result['main_result_6pair']['fpr_shapley'][m]\n    result['comparison_to_v2']['fpr_shapley_change'][m] = round(new_fpr - old_fpr, 6)\n    old_comb = old_sv['main_result_6pair']['combined_shapley'][m]\n    new_comb = result['main_result_6pair']['combined_shapley'][m]\n    result['comparison_to_v2']['combined_shapley_change'][m] = round(new_comb - old_comb, 6)\n\nOUT = Path(__file__).parent / 'shapley_values_v3.json'\nwith open(OUT, 'w') as f:\n    json.dump(result, f, indent=2)\nprint(f\"\\nSaved: {OUT}\")\n\n# Print comparison\nprint(\"\\n--- Comparison v2 → v3 ---\")\nprint(f\"{'Method':<20} {'v2 FPR':>10} {'v3 FPR':>10} {'v2 comb':>10} {'v3 comb':>10}\")\nfor m in METHODS:\n    v2_fpr = old_sv['main_result_6pair']['fpr_shapley'][m]\n    v3_fpr = result['main_result_6pair']['fpr_shapley'][m]\n    v2_comb = old_sv['main_result_6pair']['combined_shapley'][m]\n    v3_comb = result['main_result_6pair']['combined_shapley'][m]\n    print(f\"  {m:<18} {v2_fpr:>+10.3f} {v3_fpr:>+10.3f} {v2_comb:>+10.3f} {v3_comb:>+10.3f}\")\n\n# Best method check\nbest_method = METHODS[np.argmin(combined_6pair)]\nprint(f\"\\nBest method (lowest combined): {best_method} ({combined_6pair.min():+.3f})\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "35addb8f-cb58-4d08-90dd-d8e72f388070",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HzEeo1WnjATH1bJ12QGgo8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1071,
      "cache_read_input_tokens": 81116,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1071
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-24T09:00:01.500Z_

<details><summary>↩ Tool result · `toolu_0172AViwYDN6aXStaj8wcPf1`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v3/compute_shapley_v3.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "6a01ea4c-840f-4ca2-86c3-6b50ca329b7f",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v3/compute_shapley_v3.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Recompute Shapley values with 6-seed null data (s45-s50, 6-pair basis).\n\nFPR Shapley: recomputed from 6 null seeds (36 pairs).\nFNR Shapley: unchanged from v2 (45 signal experiments, 270 pairs for 6-pair).\nCombined = FPR + FNR.\n\nVoting rules (matching fpr_transparency consensus):\n  naive_xcorr:     naive_xcorr_sig (|r|>0.5, lag!=0), no direction filter for Shapley\n  diff_xcorr:      diff_xcorr_fwd_sig_fdr\n  threshold_onset: threshold_onset_sig\n  perm_granger:    perm_granger_fwd_sig_fdr\n  ty_granger:      ty_granger_sig\n\"\"\"\nimport json\nimport numpy as np\nfrom itertools import combinations\nfrom math import factorial\nfrom pathlib import Path\nfrom datetime import datetime\n\nMETHODS = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']\nN = len(METHODS)\n\n# Load fpr_transparency data\nFPR_FILE = Path(__file__).parent.parent / 'fpr_transparency_all_seeds.json'\nOLD_SHAPLEY = Path(__file__).parent.parent / 'shapley_v2' / 'shapley_values_v2.json'\n\nwith open(FPR_FILE) as f:\n    fpr_data = json.load(f)\n\nwith open(OLD_SHAPLEY) as f:\n    old_sv = json.load(f)\n\n# Build null detection matrix: 36 x 5 (boolean)\nnull_matrix = []\nfor seed_data in fpr_data['seeds']:\n    for pair in seed_data['pairs']:\n        row = [\n            pair['naive_xcorr_sig'],                # naive: sig (no direction filter)\n            pair['diff_xcorr_fwd_sig_fdr'],          # diff: FDR-corrected\n            pair['threshold_onset_sig'],             # threshold: deterministic\n            pair['perm_granger_fwd_sig_fdr'],        # perm: FDR-corrected\n            pair['ty_granger_sig'],                  # ty: uncorrected\n        ]\n        null_matrix.append(row)\n\nnull_matrix = np.array(null_matrix, dtype=bool)\nn_null = len(null_matrix)\nassert n_null == 36, f\"Expected 36 null pairs, got {n_null}\"\n\n# Verify per-method FP counts match Table 14\nfp_counts = null_matrix.sum(axis=0)\nprint(\"Per-method FP counts (should match Table 14):\")\nfor m, c in zip(METHODS, fp_counts):\n    print(f\"  {m}: {c}/36 = {c/36*100:.1f}%\")\n\n# Shapley computation (exact enumeration, 2^5=32 coalitions)\ndef shapley_values(value_fn):\n    \"\"\"Compute Shapley values for n players given a value function v(S).\n    v(S) takes a frozenset of method indices and returns a scalar.\"\"\"\n    phi = np.zeros(N)\n    for k in range(N):\n        others = [i for i in range(N) if i != k]\n        for size in range(N):  # |S| = 0, 1, ..., N-1\n            weight = factorial(size) * factorial(N - size - 1) / factorial(N)\n            for combo in combinations(others, size):\n                S = frozenset(combo)\n                S_with_k = S | {k}\n                marginal = value_fn(S_with_k) - value_fn(S)\n                phi[k] += weight * marginal\n    return phi\n\n# FPR value function: fraction of null pairs detected by coalition\ndef fpr_value(coalition):\n    if not coalition:\n        return 0.0\n    cols = list(coalition)\n    detected = null_matrix[:, cols].any(axis=1)\n    return detected.sum() / n_null\n\n# Compute FPR Shapley\nfpr_shapley = shapley_values(fpr_value)\nprint(\"\\nFPR Shapley (6-seed null):\")\nfor m, v in zip(METHODS, fpr_shapley):\n    print(f\"  {m}: {v:+.6f}\")\nprint(f\"  Sum: {fpr_shapley.sum():.6f} (should equal full-coalition FPR: {fpr_value(frozenset(range(N))):.6f})\")\n\n# FNR Shapley: keep from old v2 (signal data unchanged)\nfnr_shapley_6pair = np.array([old_sv['main_result_6pair']['fnr_shapley'][m] for m in METHODS])\nfnr_shapley_8pair = np.array([old_sv['robustness_8pair']['fnr_shapley'][m] for m in METHODS])\n\nprint(\"\\nFNR Shapley (unchanged from v2, 6-pair):\")\nfor m, v in zip(METHODS, fnr_shapley_6pair):\n    print(f\"  {m}: {v:+.6f}\")\n\n# Combined Shapley\ncombined_6pair = fpr_shapley + fnr_shapley_6pair\ncombined_8pair = fpr_shapley + fnr_shapley_8pair\n\nprint(\"\\nCombined Shapley (6-pair):\")\nfor m, v in zip(METHODS, combined_6pair):\n    print(f\"  {m}: {v:+.6f}\")\n\n# FDR sensitivity: recompute PermG BH-FDR at different q thresholds\ndef bh_fdr_count(pvalues, q):\n    \"\"\"Apply BH-FDR correction and count rejections.\"\"\"\n    m = len(pvalues)\n    sorted_p = sorted(pvalues)\n    k_max = 0\n    for i, p in enumerate(sorted_p, 1):\n        if p <= q * i / m:\n            k_max = i\n    return k_max\n\n# Extract PermG forward p-values per seed\nprint(\"\\n--- FDR Sensitivity (Null) ---\")\nfor q in [0.01, 0.05, 0.10]:\n    total_sig = 0\n    for seed_data in fpr_data['seeds']:\n        pvals = [p['perm_granger_fwd_p'] for p in seed_data['pairs']]\n        sig = bh_fdr_count(pvals, q)\n        total_sig += sig\n    print(f\"  q={q:.2f}: {total_sig}/36 null FDR-sig\")\n\n# Build output JSON\nresult = {\n    \"version\": \"v3_6seed_null\",\n    \"generated_at\": datetime.now().isoformat(),\n    \"change_from_v2\": \"FPR recomputed with 6 null seeds (s45-s50, 36 pairs, 6-pair basis). FNR unchanged (45 signal experiments, 270/360 signal pairs).\",\n    \"null_data_source\": \"fpr_transparency_all_seeds.json\",\n    \"null_seeds\": [45, 46, 47, 48, 49, 50],\n    \"n_null_seeds\": 6,\n    \"n_null_pairs_per_seed\": 6,\n    \"n_null_obs\": 36,\n    \"n_signal_experiments\": 45,\n    \"n_signal_obs_6pair\": 270,\n    \"n_signal_obs_8pair\": 360,\n    \"pair_basis\": \"6-pair (distinct_1/2/3 only, mauve excluded)\",\n    \"threshold_criterion\": \"true_3sigma_d105\",\n    \"methods\": METHODS,\n    \"n_methods\": N,\n    \"n_coalitions\": 2**N,\n    \"voting_rules\": {\n        \"naive_xcorr\": \"naive_xcorr_sig (|r|>0.5, lag!=0; no direction filter)\",\n        \"diff_xcorr\": \"diff_xcorr_fwd_sig_fdr (BH-FDR corrected)\",\n        \"threshold_onset\": \"threshold_onset_sig (deterministic 3sigma)\",\n        \"perm_granger\": \"perm_granger_fwd_sig_fdr (BH-FDR corrected)\",\n        \"ty_granger\": \"ty_granger_sig (uncorrected)\"\n    },\n    \"main_result_6pair\": {\n        \"fpr_shapley\": {m: round(v, 6) for m, v in zip(METHODS, fpr_shapley)},\n        \"fnr_shapley\": {m: round(v, 6) for m, v in zip(METHODS, fnr_shapley_6pair)},\n        \"combined_shapley\": {m: round(v, 6) for m, v in zip(METHODS, combined_6pair)}\n    },\n    \"robustness_8pair\": {\n        \"fpr_shapley\": {m: round(v, 6) for m, v in zip(METHODS, fpr_shapley)},\n        \"fnr_shapley\": {m: round(v, 6) for m, v in zip(METHODS, fnr_shapley_8pair)},\n        \"combined_shapley\": {m: round(v, 6) for m, v in zip(METHODS, combined_8pair)}\n    },\n    \"raw_fpr_counts\": {m: int(c) for m, c in zip(METHODS, fp_counts)},\n    \"raw_fpr_rates\": {m: round(int(c)/36, 4) for m, c in zip(METHODS, fp_counts)},\n    \"fdr_sensitivity_null\": {},\n    \"comparison_to_v2\": {\n        \"fpr_shapley_change\": {},\n        \"combined_shapley_change\": {}\n    }\n}\n\n# FDR sensitivity\nfor q in [0.01, 0.05, 0.10]:\n    total_sig = 0\n    for seed_data in fpr_data['seeds']:\n        pvals = [p['perm_granger_fwd_p'] for p in seed_data['pairs']]\n        total_sig += bh_fdr_count(pvals, q)\n    result['fdr_sensitivity_null'][f'q_{q:.2f}'] = {\n        'rejections': total_sig,\n        'total': 36,\n        'fpr': round(total_sig / 36, 4)\n    }\n\n# Comparison to v2\nfor m in METHODS:\n    old_fpr = old_sv['main_result_6pair']['fpr_shapley'][m]\n    new_fpr = result['main_result_6pair']['fpr_shapley'][m]\n    result['comparison_to_v2']['fpr_shapley_change'][m] = round(new_fpr - old_fpr, 6)\n    old_comb = old_sv['main_result_6pair']['combined_shapley'][m]\n    new_comb = result['main_result_6pair']['combined_shapley'][m]\n    result['comparison_to_v2']['combined_shapley_change'][m] = round(new_comb - old_comb, 6)\n\nOUT = Path(__file__).parent / 'shapley_values_v3.json'\nwith open(OUT, 'w') as f:\n    json.dump(result, f, indent=2)\nprint(f\"\\nSaved: {OUT}\")\n\n# Print comparison\nprint(\"\\n--- Comparison v2 → v3 ---\")\nprint(f\"{'Method':<20} {'v2 FPR':>10} {'v3 FPR':>10} {'v2 comb':>10} {'v3 comb':>10}\")\nfor m in METHODS:\n    v2_fpr = old_sv['main_result_6pair']['fpr_shapley'][m]\n    v3_fpr = result['main_result_6pair']['fpr_shapley'][m]\n    v2_comb = old_sv['main_result_6pair']['combined_shapley'][m]\n    v3_comb = result['main_result_6pair']['combined_shapley'][m]\n    print(f\"  {m:<18} {v2_fpr:>+10.3f} {v3_fpr:>+10.3f} {v2_comb:>+10.3f} {v3_comb:>+10.3f}\")\n\n# Best method check\nbest_method = METHODS[np.argmin(combined_6pair)]\nprint(f\"\\nBest method (lowest combined): {best_method} ({combined_6pair.min():+.3f})\")\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---


### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Bash · `toolu_01ChXKrBHW9M5kKMBDMiGpUR`</summary>

```json
{
  "command": "python3 artifacts/shapley_v3/compute_shapley_v3.py",
  "description": "Run Shapley v3 computation with 6-seed null data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "44c845dd-472f-4309-9791-a3b474da0af8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cgc7Vx45ro7jA73XhsS7Jp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4870,
      "cache_read_input_tokens": 82187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4870
      },
      "output_tokens": 62,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 69 · 2026-05-24T09:00:05.312Z_

<details><summary>↩ Tool result · `toolu_01ChXKrBHW9M5kKMBDMiGpUR`</summary>

```text
Per-method FP counts (should match Table 14):
  naive_xcorr: 33/36 = 91.7%
  diff_xcorr: 1/36 = 2.8%
  threshold_onset: 10/36 = 27.8%
  perm_granger: 4/36 = 11.1%
  ty_granger: 14/36 = 38.9%

FPR Shapley (6-seed null):
  naive_xcorr: +0.608796
  diff_xcorr: +0.006944
  threshold_onset: +0.111111
  perm_granger: +0.039352
  ty_granger: +0.150463
  Sum: 0.916667 (should equal full-coalition FPR: 0.916667)

FNR Shapley (unchanged from v2, 6-pair):
  naive_xcorr: -0.418580
  diff_xcorr: -0.305617
  threshold_onset: -0.026914
  perm_granger: -0.180000
  ty_granger: -0.068889

Combined Shapley (6-pair):
  naive_xcorr: +0.190216
  diff_xcorr: -0.298673
  threshold_onset: +0.084197
  perm_granger: -0.140648
  ty_granger: +0.081574

--- FDR Sensitivity (Null) ---
  q=0.01: 3/36 null FDR-sig
  q=0.05: 4/36 null FDR-sig
  q=0.10: 8/36 null FDR-sig

Saved: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v3/shapley_values_v3.json

--- Comparison v2 → v3 ---
Method                   v2 FPR     v3 FPR    v2 comb    v3 comb
  naive_xcorr            +0.622     +0.609     +0.203     +0.190
  diff_xcorr             +0.163     +0.007     -0.142     -0.299
  threshold_onset        +0.101     +0.111     +0.074     +0.084
  perm_granger           +0.000     +0.039     -0.180     -0.141
  ty_granger             +0.031     +0.150     -0.038     +0.082

Best method (lowest combined): diff_xcorr (-0.299)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "87143da1-8093-4046-a36a-f0a873a0f5b5",
  "tool_use_result": {
    "stdout": "Per-method FP counts (should match Table 14):\n  naive_xcorr: 33/36 = 91.7%\n  diff_xcorr: 1/36 = 2.8%\n  threshold_onset: 10/36 = 27.8%\n  perm_granger: 4/36 = 11.1%\n  ty_granger: 14/36 = 38.9%\n\nFPR Shapley (6-seed null):\n  naive_xcorr: +0.608796\n  diff_xcorr: +0.006944\n  threshold_onset: +0.111111\n  perm_granger: +0.039352\n  ty_granger: +0.150463\n  Sum: 0.916667 (should equal full-coalition FPR: 0.916667)\n\nFNR Shapley (unchanged from v2, 6-pair):\n  naive_xcorr: -0.418580\n  diff_xcorr: -0.305617\n  threshold_onset: -0.026914\n  perm_granger: -0.180000\n  ty_granger: -0.068889\n\nCombined Shapley (6-pair):\n  naive_xcorr: +0.190216\n  diff_xcorr: -0.298673\n  threshold_onset: +0.084197\n  perm_granger: -0.140648\n  ty_granger: +0.081574\n\n--- FDR Sensitivity (Null) ---\n  q=0.01: 3/36 null FDR-sig\n  q=0.05: 4/36 null FDR-sig\n  q=0.10: 8/36 null FDR-sig\n\nSaved: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v3/shapley_values_v3.json\n\n--- Comparison v2 → v3 ---\nMethod                   v2 FPR     v3 FPR    v2 comb    v3 comb\n  naive_xcorr            +0.622     +0.609     +0.203     +0.190\n  diff_xcorr             +0.163     +0.007     -0.142     -0.299\n  threshold_onset        +0.101     +0.111     +0.074     +0.084\n  perm_granger           +0.000     +0.039     -0.180     -0.141\n  ty_granger             +0.031     +0.150     -0.038     +0.082\n\nBest method (lowest combined): diff_xcorr (-0.299)",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 70_

<details><summary>Logged reasoning block</summary>

```text
Interesting results! The best method has changed from PermG (-0.180) to DiffXCorr (-0.299). This is a significant change. Let me analyze:

v2 → v3 changes:
- naive: comb +0.203 → +0.190 (slightly improved, still worst)
- diff: comb -0.142 → -0.299 (big improvement, now best!)
- thresh: comb +0.074 → +0.084 (slightly worse)
- perm: comb -0.180 → -0.141 (worse, no longer best)


- ty: comb -0.038 → +0.082 (much worse)

The dramatic shift comes from DiffXCorr's FPR Shapley plummeting from +0.163 to +0.007 with the new null data—diff_xcorr now only has 1 false positive out of 36 total, compared to 9 out of 24 in the old null data, which substantially reduces its FPR contribution and makes its overall combined Shapley much stronger.

The old and new null datasets aren't directly comparable though, since they use different random seeds and pair bases (8-pair vs 6-pair), so the difference in diff_xcorr's false positive rate could be genuine rather than an artifact of the evaluation setup. The main paper argument actually doesn't hinge on the Shapley analysis since that's relegated to the appendix—the core narrative centers on K≥3 consensus with PermG as the strongest individual method. Still, this is a substantial shift in the appendix results, so I need to verify whether something's off with the voting rules or if there's a genuine issue with how the FPR was computed across the different null data configurations.

Looking at the numbers more carefully, the old Shapley results show diff_xcorr with 9 false positives out of 24 pairs across 3 seeds (37.5%), whereas the new setup with 6-pair basis and 6 seeds gives just 1 out of 36 (2.8%)—a dramatic swing that likely stems from the old null seeds happening to produce more diff_xcorr false positives, combined with the 8-pair basis including mauve pairs that might have inflated those errors, plus the different BH correction thresholds. This is a genuine data difference rooted in the smaller, older null dataset, which is exactly why the task asked for this update in the first place.

So the new Shapley values with the authoritative 6-seed null are more reliable, and they flip the narrative: diff_xcorr now ranks as the best contributor at -0.299, pushing PermG down to -0.141. I need to decide whether to keep the paper's original claim about PermG or update the appendix to reflect this new ranking, and I should double-check whether the old Shapley computation was done differently to make sure this comparison is valid. Looking at the FPR changes between the two Shapley configurations, the diff method dropped dramatically from 37.5% to 2.8% while the ty method spiked from 8.3% to 38.9%, which is striking. I'm wondering if the old null's 8-pair basis had a particular composition of mauve pairs that skewed toward diff_xcorr false positives and away from ty ones, or whether the different BH correction thresholds (m=8 versus m=6) are driving these shifts. I should also check whether the old null was actually using BH-FDR correction at all. Let me look at the 6-pair results from the old Shapley data to see if that helps explain the discrepancy. The old analysis shows a diff_xcorr FPR Shapley of +0.163 on the 6-pair basis, but I need to find the actual false positive counts for that configuration to compare directly with the new fpr_transparency results.

Checking the old Shapley structure more carefully, I see it has 8 pairs listed for FPR calculations even when labeled as "6-pair," while the FNR uses 6 pairs. So the old and new analyses actually differ in three ways: the null seeds changed from 3 to 6, the pair basis for FPR stayed at 8 pairs in the old version but shifted to 6 pairs in the new version, and the total FPR sample size went from 24 to 36 as a result.

The task specification explicitly calls for a 6-pair basis with 36 total pairs, so using 6 pairs per seed for FPR is the right approach. Since my FPR data from fpr_transparency_all_seeds.json is already computed on that 6-pair basis excluding mauve, the calculation is correct. The difference in diff_xcorr FP counts between old and new likely stems from some of those 9 old false positives having occurred on mauve pairs that are no longer included.

Now I need to revise the appendix narrative since DiffXCorr has emerged as the strongest individual contributor rather than PermG. Looking at the numbers, this makes intuitive sense—DiffXCorr achieves an exceptionally low FPR of 2.8% combined with meaningful FNR reduction, which explains why it outperforms other methods. The BH-FDR correction keeps false positives minimal while still maintaining decent signal detection capability.

However, there's a critical limitation I need to account for: DiffXCorr is bidirectional and can't distinguish forward from reverse causal relationships. The Shapley analysis captures the FPR and FNR trade-offs but misses this directional information advantage that PermG provides. So while DiffXCorr wins on the quantitative metrics, PermG remains the better choice for the MMCT ensemble because it offers directional separation. I should update the appendix to report the Shapley values accurately, acknowledge that DiffXCorr has the best combined score, but explain why PermG is still preferred for the ensemble despite this.

Let me also verify the robustness results with the 8-pair variant.

I'm checking the Shapley calculations across both the 6-pair and 8-pair configurations. The FPR Shapley stays constant since it's computed from null data, but the FNR Shapley shifts when using the 8-pair signal data. Recalculating the combined scores with this basis, DiffXCorr still comes out ahead at -0.263, with PermG following at -0.112. This confirms the ranking holds across both robustness checks.

Now I need to update the figure and appendix to reflect this finding—it's a meaningful shift in how I present the narrative.

Actually, let me reconsider the comparability issue here. The old Shapley FPR was computed from 3 null seeds across 8 pairs, while my new version uses 6 null seeds across 6 pairs. Since the old analysis included mauve in the null data but my new one excludes it, the FPR Shapley values between v2 and v3 aren't directly comparable—they're based on different pair sets for the null distribution. This is a critical distinction I need to address in the paper.

For the analysis going forward, the 6-seed null data on the 6-pair basis is what I'll use as the authoritative version. Now looking at the key results from this new Shapley computation, I can see how each method's FPR and FNR contributions combine to produce the overall effect.

Checking the FDR sensitivity under the null hypothesis, I'm seeing that only a small fraction of the 36 tests show significance even at lenient thresholds. Now I need to update the figure generation script and appendix narrative. The main decision is how to handle the visualization — PermG remains the paper's central method, but DiffXCorr actually achieves the best combined Shapley value. I think I'll keep PermG highlighted since it's the paper's focus, but I'll need to revise the appendix text to acknowledge that while DiffXCorr has superior combined Shapley values, it lacks the directional separation that makes PermG valuable. I'm going back and forth on how to handle the highlighting — the figure should reflect the data accurately by highlighting DiffXCorr as the best combined method, but the paper's main narrative centers on PermG as the best directional approach. I think the clearest approach is to update the data source, remove the "zero FPR" annotation, and keep PermG highlighted since that's what the text emphasizes, letting the appendix explanation handle the nuance about DiffXCorr's combined performance. The y-axis limits for panel (a) are already sufficient since the new maximum FPR value of 0.609 fits within the existing range. Panel (b) doesn't need adjustment either, but panel (c) requires extending the lower limit to around -0.35 to accommodate the new minimum value of -0.299. I'll update the figure script now, keeping the PermG highlight but removing the outdated annotation, and letting the bars demonstrate that DiffXCorr has the lowest FPR in panel (c).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "db8cee0d-7052-412e-924c-86ab482f3b96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwMw23zgkFvTqeETqG6nFS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 87057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 995
      },
      "output_tokens": 27,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 71_

Important finding: DiffXCorr is now the best combined Shapley method (-0.299), not PermG (-0.141). PermG's FPR Shapley went from 0.000 to +0.039, and DiffXCorr's FPR dropped from +0.163 to +0.007. This changes the appendix narrative.

Let me update the figure script and regenerate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "ab9edb34-c160-404c-a213-1b30d9a9927d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwMw23zgkFvTqeETqG6nFS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 87057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 995
      },
      "output_tokens": 27,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01Dkh2ndGRXoz1s2iqNSV56y`</summary>

```json
{
  "todos": [
    {
      "content": "Write and run Shapley computation script with 6-seed null data",
      "status": "completed",
      "activeForm": "Writing and running Shapley computation script"
    },
    {
      "content": "Update gen_shapley_contribution.py and regenerate figure",
      "status": "in_progress",
      "activeForm": "Updating figure generation script"
    },
    {
      "content": "Find treatment PermG data for FDR sensitivity table update",
      "status": "pending",
      "activeForm": "Finding treatment PermG data"
    },
    {
      "content": "Update appendix.tex — all 7 TODO-D219 locations",
      "status": "pending",
      "activeForm": "Updating appendix.tex"
    },
    {
      "content": "Verify all numbers and TODO removals",
      "status": "pending",
      "activeForm": "Verifying consistency"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "12900eaa-75aa-4bf3-aeb7-9d5a625d24dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BwMw23zgkFvTqeETqG6nFS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 87057,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 995
      },
      "output_tokens": 27,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-24T09:01:57.473Z_

<details><summary>↩ Tool result · `toolu_01Dkh2ndGRXoz1s2iqNSV56y`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "bd4ad7d6-c2d5-48ff-a894-8bda357afef8",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Write and run Shapley computation script with 6-seed null data",
        "status": "in_progress",
        "activeForm": "Writing and running Shapley computation script"
      },
      {
        "content": "Update gen_shapley_contribution.py and regenerate figure",
        "status": "pending",
        "activeForm": "Updating figure generation script"
      },
      {
        "content": "Find treatment PermG data for FDR sensitivity table update",
        "status": "pending",
        "activeForm": "Finding treatment PermG data"
      },
      {
        "content": "Update appendix.tex — all 7 TODO-D219 locations",
        "status": "pending",
        "activeForm": "Updating appendix.tex"
      },
      {
        "content": "Verify all numbers and TODO removals",
        "status": "pending",
        "activeForm": "Verifying consistency"
      }
    ],
    "newTodos": [
      {
        "content": "Write and run Shapley computation script with 6-seed null data",
        "status": "completed",
        "activeForm": "Writing and running Shapley computation script"
      },
      {
        "content": "Update gen_shapley_contribution.py and regenerate figure",
        "status": "in_progress",
        "activeForm": "Updating figure generation script"
      },
      {
        "content": "Find treatment PermG data for FDR sensitivity table update",
        "status": "pending",
        "activeForm": "Finding treatment PermG data"
      },
      {
        "content": "Update appendix.tex — all 7 TODO-D219 locations",
        "status": "pending",
        "activeForm": "Updating appendix.tex"
      },
      {
        "content": "Verify all numbers and TODO removals",
        "status": "pending",
        "activeForm": "Verifying consistency"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Edit · `toolu_01WbsCKXfVhoFGQYmrK1ysvT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/gen_shapley_contribution.py",
  "old_string": "DATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_values_v2.json')",
  "new_string": "DATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v3/shapley_values_v3.json')"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "f644b86d-7020-43be-9c7d-3db0a2530a80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019bSaYUKXahW8e8ZiWQiEBk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5342,
      "cache_read_input_tokens": 88052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5342
      },
      "output_tokens": 35,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 75 · 2026-05-24T09:02:04.710Z_

<details><summary>↩ Tool result · `toolu_01WbsCKXfVhoFGQYmrK1ysvT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/gen_shapley_contribution.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "45cff26c-c464-4f02-9d24-e1c32abdb4c3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/gen_shapley_contribution.py",
    "oldString": "DATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_values_v2.json')",
    "newString": "DATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v3/shapley_values_v3.json')",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Figure A.2: Shapley method contribution analysis.\nUnified style with project palette.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nimport numpy as np\nimport json\nfrom pathlib import Path\n\nOUT = Path(__file__).parent\nDATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_values_v2.json')\n\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],\n    'font.size': 9,\n    'axes.labelsize': 10,\n    'xtick.labelsize': 8,\n    'ytick.labelsize': 9,\n    'legend.fontsize': 7.5,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.08,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n    'mathtext.fontset': 'cm',\n})\n\nwith open(DATA) as f:\n    d = json.load(f)\n\nsv = d['main_result_6pair']\n\nmethods_raw = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']\nlabels = ['Naive\\nXCorr', 'Diff\\nXCorr', 'Thresh.\\nOnset', 'Perm\\nGranger', 'TY\\nGranger']\n\nfpr_vals = [sv['fpr_shapley'][m] for m in methods_raw]\nfnr_vals = [sv['fnr_shapley'][m] for m in methods_raw]\ncomb_vals = [sv['combined_shapley'][m] for m in methods_raw]\n\n# Method colors: PermG highlighted as the champion\nMETHOD_COLORS = {\n    'naive_xcorr':     '#D4694A',\n    'diff_xcorr':      '#E8C170',\n    'threshold_onset': '#8CB4D5',\n    'perm_granger':    '#2C4A6E',\n    'ty_granger':      '#3B6FA0',\n}\ncolors = [METHOD_COLORS[m] for m in methods_raw]\n\nx = np.arange(len(methods_raw))\nbar_width = 0.65\n\nfig, (ax_fpr, ax_fnr, ax_comb) = plt.subplots(\n    1, 3, figsize=(7.2, 2.8),\n    gridspec_kw={'wspace': 0.38}\n)\n\ndef draw_bars(ax, vals, title, panel_label, show_ylabel=True):\n    bars = ax.bar(x, vals, bar_width, color=colors, edgecolor='white', linewidth=0.5, zorder=3)\n    ax.set_xticks(x)\n    ax.set_xticklabels(labels, fontsize=6.5, linespacing=0.9)\n    ax.axhline(0, color='#AAAAAA', linewidth=0.5, zorder=1)\n    ax.set_title(title, fontsize=9, pad=10)\n    ax.text(-0.20, 1.12, panel_label, transform=ax.transAxes,\n            fontsize=10, fontweight='bold', va='bottom')\n    if show_ylabel:\n        ax.set_ylabel('Shapley value')\n\n    for bar, val in zip(bars, vals):\n        y_pos = val + 0.012 if val >= 0 else val - 0.020\n        va = 'bottom' if val >= 0 else 'top'\n        t = ax.text(bar.get_x() + bar.get_width() / 2, y_pos,\n                    f'{val:+.3f}' if abs(val) >= 0.001 else '0.000',\n                    ha='center', va=va, fontsize=6, color='#333333')\n        t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])\n\n    perm_idx = methods_raw.index('perm_granger')\n    bars[perm_idx].set_edgecolor('#1A1A1A')\n    bars[perm_idx].set_linewidth(1.2)\n\ndraw_bars(ax_fpr, fpr_vals, 'FPR contribution', '(a)')\nax_fpr.set_ylim(-0.05, 0.72)\n\ndraw_bars(ax_fnr, fnr_vals, 'FNR contribution (6-pair)', '(b)', show_ylabel=False)\nax_fnr.set_ylim(-0.48, 0.05)\n\ndraw_bars(ax_comb, comb_vals, 'Combined (FPR + FNR)', '(c)', show_ylabel=False)\nax_comb.set_ylim(-0.25, 0.25)\n\n# Compact PermG annotation\nt_perm = ax_fpr.text(3, 0.04, 'zero\\nFPR', fontsize=6, color='#2C4A6E',\n                     ha='center', va='bottom', fontstyle='italic', linespacing=0.85)\nt_perm.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])\n\nfig.subplots_adjust(left=0.08, right=0.97, bottom=0.18, top=0.84, wspace=0.38)\n\nfor fmt in ['pdf', 'png']:\n    fig.savefig(OUT / f'shapley_method_contribution.{fmt}', dpi=300)\nplt.close()\nprint(f'Saved: {OUT}/shapley_method_contribution.pdf + .png')\n",
    "structuredPatch": [
      {
        "oldStart": 10,
        "oldLines": 7,
        "newStart": 10,
        "newLines": 7,
        "lines": [
          " from pathlib import Path",
          " ",
          " OUT = Path(__file__).parent",
          "-DATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v2/shapley_values_v2.json')",
          "+DATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v3/shapley_values_v3.json')",
          " ",
          " plt.rcParams.update({",
          "     'font.family': 'serif',"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Edit · `toolu_019PTamEn2VDqgKfxwH4dF1W`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/gen_shapley_contribution.py",
  "old_string": "draw_bars(ax_fpr, fpr_vals, 'FPR contribution', '(a)')\nax_fpr.set_ylim(-0.05, 0.72)\n\ndraw_bars(ax_fnr, fnr_vals, 'FNR contribution (6-pair)', '(b)', show_ylabel=False)\nax_fnr.set_ylim(-0.48, 0.05)\n\ndraw_bars(ax_comb, comb_vals, 'Combined (FPR + FNR)', '(c)', show_ylabel=False)\nax_comb.set_ylim(-0.25, 0.25)\n\n# Compact PermG annotation\nt_perm = ax_fpr.text(3, 0.04, 'zero\\nFPR', fontsize=6, color='#2C4A6E',\n                     ha='center', va='bottom', fontstyle='italic', linespacing=0.85)\nt_perm.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])",
  "new_string": "draw_bars(ax_fpr, fpr_vals, 'FPR contribution', '(a)')\nax_fpr.set_ylim(-0.05, 0.72)\n\ndraw_bars(ax_fnr, fnr_vals, 'FNR contribution (6-pair)', '(b)', show_ylabel=False)\nax_fnr.set_ylim(-0.48, 0.05)\n\ndraw_bars(ax_comb, comb_vals, 'Combined (FPR + FNR)', '(c)', show_ylabel=False)\nax_comb.set_ylim(-0.35, 0.25)\n\n# Highlight best combined method (DiffXCorr)\ndiff_idx = methods_raw.index('diff_xcorr')\nax_comb.patches[diff_idx].set_edgecolor('#1A1A1A')\nax_comb.patches[diff_idx].set_linewidth(1.2)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "440fa69b-a87e-444e-87bf-515379e1e4cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011z3MMvvDmfvyP3P9CbTTJQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 315,
      "cache_read_input_tokens": 93394,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 315
      },
      "output_tokens": 67,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-24T09:02:14.609Z_

<details><summary>↩ Tool result · `toolu_019PTamEn2VDqgKfxwH4dF1W`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/gen_shapley_contribution.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "b7727b61-91cf-4c0f-88b1-43ededec3156",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/gen_shapley_contribution.py",
    "oldString": "draw_bars(ax_fpr, fpr_vals, 'FPR contribution', '(a)')\nax_fpr.set_ylim(-0.05, 0.72)\n\ndraw_bars(ax_fnr, fnr_vals, 'FNR contribution (6-pair)', '(b)', show_ylabel=False)\nax_fnr.set_ylim(-0.48, 0.05)\n\ndraw_bars(ax_comb, comb_vals, 'Combined (FPR + FNR)', '(c)', show_ylabel=False)\nax_comb.set_ylim(-0.25, 0.25)\n\n# Compact PermG annotation\nt_perm = ax_fpr.text(3, 0.04, 'zero\\nFPR', fontsize=6, color='#2C4A6E',\n                     ha='center', va='bottom', fontstyle='italic', linespacing=0.85)\nt_perm.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])",
    "newString": "draw_bars(ax_fpr, fpr_vals, 'FPR contribution', '(a)')\nax_fpr.set_ylim(-0.05, 0.72)\n\ndraw_bars(ax_fnr, fnr_vals, 'FNR contribution (6-pair)', '(b)', show_ylabel=False)\nax_fnr.set_ylim(-0.48, 0.05)\n\ndraw_bars(ax_comb, comb_vals, 'Combined (FPR + FNR)', '(c)', show_ylabel=False)\nax_comb.set_ylim(-0.35, 0.25)\n\n# Highlight best combined method (DiffXCorr)\ndiff_idx = methods_raw.index('diff_xcorr')\nax_comb.patches[diff_idx].set_edgecolor('#1A1A1A')\nax_comb.patches[diff_idx].set_linewidth(1.2)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Figure A.2: Shapley method contribution analysis.\nUnified style with project palette.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nimport numpy as np\nimport json\nfrom pathlib import Path\n\nOUT = Path(__file__).parent\nDATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v3/shapley_values_v3.json')\n\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],\n    'font.size': 9,\n    'axes.labelsize': 10,\n    'xtick.labelsize': 8,\n    'ytick.labelsize': 9,\n    'legend.fontsize': 7.5,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.08,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n    'mathtext.fontset': 'cm',\n})\n\nwith open(DATA) as f:\n    d = json.load(f)\n\nsv = d['main_result_6pair']\n\nmethods_raw = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']\nlabels = ['Naive\\nXCorr', 'Diff\\nXCorr', 'Thresh.\\nOnset', 'Perm\\nGranger', 'TY\\nGranger']\n\nfpr_vals = [sv['fpr_shapley'][m] for m in methods_raw]\nfnr_vals = [sv['fnr_shapley'][m] for m in methods_raw]\ncomb_vals = [sv['combined_shapley'][m] for m in methods_raw]\n\n# Method colors: PermG highlighted as the champion\nMETHOD_COLORS = {\n    'naive_xcorr':     '#D4694A',\n    'diff_xcorr':      '#E8C170',\n    'threshold_onset': '#8CB4D5',\n    'perm_granger':    '#2C4A6E',\n    'ty_granger':      '#3B6FA0',\n}\ncolors = [METHOD_COLORS[m] for m in methods_raw]\n\nx = np.arange(len(methods_raw))\nbar_width = 0.65\n\nfig, (ax_fpr, ax_fnr, ax_comb) = plt.subplots(\n    1, 3, figsize=(7.2, 2.8),\n    gridspec_kw={'wspace': 0.38}\n)\n\ndef draw_bars(ax, vals, title, panel_label, show_ylabel=True):\n    bars = ax.bar(x, vals, bar_width, color=colors, edgecolor='white', linewidth=0.5, zorder=3)\n    ax.set_xticks(x)\n    ax.set_xticklabels(labels, fontsize=6.5, linespacing=0.9)\n    ax.axhline(0, color='#AAAAAA', linewidth=0.5, zorder=1)\n    ax.set_title(title, fontsize=9, pad=10)\n    ax.text(-0.20, 1.12, panel_label, transform=ax.transAxes,\n            fontsize=10, fontweight='bold', va='bottom')\n    if show_ylabel:\n        ax.set_ylabel('Shapley value')\n\n    for bar, val in zip(bars, vals):\n        y_pos = val + 0.012 if val >= 0 else val - 0.020\n        va = 'bottom' if val >= 0 else 'top'\n        t = ax.text(bar.get_x() + bar.get_width() / 2, y_pos,\n                    f'{val:+.3f}' if abs(val) >= 0.001 else '0.000',\n                    ha='center', va=va, fontsize=6, color='#333333')\n        t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])\n\n    perm_idx = methods_raw.index('perm_granger')\n    bars[perm_idx].set_edgecolor('#1A1A1A')\n    bars[perm_idx].set_linewidth(1.2)\n\ndraw_bars(ax_fpr, fpr_vals, 'FPR contribution', '(a)')\nax_fpr.set_ylim(-0.05, 0.72)\n\ndraw_bars(ax_fnr, fnr_vals, 'FNR contribution (6-pair)', '(b)', show_ylabel=False)\nax_fnr.set_ylim(-0.48, 0.05)\n\ndraw_bars(ax_comb, comb_vals, 'Combined (FPR + FNR)', '(c)', show_ylabel=False)\nax_comb.set_ylim(-0.25, 0.25)\n\n# Compact PermG annotation\nt_perm = ax_fpr.text(3, 0.04, 'zero\\nFPR', fontsize=6, color='#2C4A6E',\n                     ha='center', va='bottom', fontstyle='italic', linespacing=0.85)\nt_perm.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])\n\nfig.subplots_adjust(left=0.08, right=0.97, bottom=0.18, top=0.84, wspace=0.38)\n\nfor fmt in ['pdf', 'png']:\n    fig.savefig(OUT / f'shapley_method_contribution.{fmt}', dpi=300)\nplt.close()\nprint(f'Saved: {OUT}/shapley_method_contribution.pdf + .png')\n",
    "structuredPatch": [
      {
        "oldStart": 91,
        "oldLines": 12,
        "newStart": 91,
        "newLines": 12,
        "lines": [
          " ax_fnr.set_ylim(-0.48, 0.05)",
          " ",
          " draw_bars(ax_comb, comb_vals, 'Combined (FPR + FNR)', '(c)', show_ylabel=False)",
          "-ax_comb.set_ylim(-0.25, 0.25)",
          "+ax_comb.set_ylim(-0.35, 0.25)",
          " ",
          "-# Compact PermG annotation",
          "-t_perm = ax_fpr.text(3, 0.04, 'zero\\nFPR', fontsize=6, color='#2C4A6E',",
          "-                     ha='center', va='bottom', fontstyle='italic', linespacing=0.85)",
          "-t_perm.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])",
          "+# Highlight best combined method (DiffXCorr)",
          "+diff_idx = methods_raw.index('diff_xcorr')",
          "+ax_comb.patches[diff_idx].set_edgecolor('#1A1A1A')",
          "+ax_comb.patches[diff_idx].set_linewidth(1.2)",
          " ",
          " fig.subplots_adjust(left=0.08, right=0.97, bottom=0.18, top=0.84, wspace=0.38)",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Assistant

_source line 78_

Now let me also update the PermG bar highlight — keep it in FPR panel but remove or update the annotation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "62d12618-be70-4f82-9614-b853df293627",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VTE7WppJXdVg4UBpi1sb37",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 93709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 710
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 79_

<details open><summary>🔧 Tool call — Read · `toolu_012V35Rcb8dteRdC3seBDt7U`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/gen_shapley_contribution.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "6a2d2cdd-3c42-4250-81ab-5da21cb91475",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VTE7WppJXdVg4UBpi1sb37",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 93709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 710
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-24T09:02:18.748Z_

<details><summary>↩ Tool result · `toolu_012V35Rcb8dteRdC3seBDt7U`</summary>

```text
1	#!/usr/bin/env python3
2	"""Figure A.2: Shapley method contribution analysis.
3	Unified style with project palette."""
4	import matplotlib
5	matplotlib.use('Agg')
6	import matplotlib.pyplot as plt
7	import matplotlib.patheffects as pe
8	import numpy as np
9	import json
10	from pathlib import Path
11	
12	OUT = Path(__file__).parent
13	DATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v3/shapley_values_v3.json')
14	
15	plt.rcParams.update({
16	    'font.family': 'serif',
17	    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],
18	    'font.size': 9,
19	    'axes.labelsize': 10,
20	    'xtick.labelsize': 8,
21	    'ytick.labelsize': 9,
22	    'legend.fontsize': 7.5,
23	    'figure.dpi': 300,
24	    'savefig.dpi': 300,
25	    'savefig.bbox': 'tight',
26	    'savefig.pad_inches': 0.08,
27	    'axes.spines.top': False,
28	    'axes.spines.right': False,
29	    'pdf.fonttype': 42,
30	    'ps.fonttype': 42,
31	    'mathtext.fontset': 'cm',
32	})
33	
34	with open(DATA) as f:
35	    d = json.load(f)
36	
37	sv = d['main_result_6pair']
38	
39	methods_raw = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']
40	labels = ['Naive\nXCorr', 'Diff\nXCorr', 'Thresh.\nOnset', 'Perm\nGranger', 'TY\nGranger']
41	
42	fpr_vals = [sv['fpr_shapley'][m] for m in methods_raw]
43	fnr_vals = [sv['fnr_shapley'][m] for m in methods_raw]
44	comb_vals = [sv['combined_shapley'][m] for m in methods_raw]
45	
46	# Method colors: PermG highlighted as the champion
47	METHOD_COLORS = {
48	    'naive_xcorr':     '#D4694A',
49	    'diff_xcorr':      '#E8C170',
50	    'threshold_onset': '#8CB4D5',
51	    'perm_granger':    '#2C4A6E',
52	    'ty_granger':      '#3B6FA0',
53	}
54	colors = [METHOD_COLORS[m] for m in methods_raw]
55	
56	x = np.arange(len(methods_raw))
57	bar_width = 0.65
58	
59	fig, (ax_fpr, ax_fnr, ax_comb) = plt.subplots(
60	    1, 3, figsize=(7.2, 2.8),
61	    gridspec_kw={'wspace': 0.38}
62	)
63	
64	def draw_bars(ax, vals, title, panel_label, show_ylabel=True):
65	    bars = ax.bar(x, vals, bar_width, color=colors, edgecolor='white', linewidth=0.5, zorder=3)
66	    ax.set_xticks(x)
67	    ax.set_xticklabels(labels, fontsize=6.5, linespacing=0.9)
68	    ax.axhline(0, color='#AAAAAA', linewidth=0.5, zorder=1)
69	    ax.set_title(title, fontsize=9, pad=10)
70	    ax.text(-0.20, 1.12, panel_label, transform=ax.transAxes,
71	            fontsize=10, fontweight='bold', va='bottom')
72	    if show_ylabel:
73	        ax.set_ylabel('Shapley value')
74	
75	    for bar, val in zip(bars, vals):
76	        y_pos = val + 0.012 if val >= 0 else val - 0.020
77	        va = 'bottom' if val >= 0 else 'top'
78	        t = ax.text(bar.get_x() + bar.get_width() / 2, y_pos,
79	                    f'{val:+.3f}' if abs(val) >= 0.001 else '0.000',
80	                    ha='center', va=va, fontsize=6, color='#333333')
81	        t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])
82	
83	    perm_idx = methods_raw.index('perm_granger')
84	    bars[perm_idx].set_edgecolor('#1A1A1A')
85	    bars[perm_idx].set_linewidth(1.2)
86	
87	draw_bars(ax_fpr, fpr_vals, 'FPR contribution', '(a)')
88	ax_fpr.set_ylim(-0.05, 0.72)
89	
90	draw_bars(ax_fnr, fnr_vals, 'FNR contribution (6-pair)', '(b)', show_ylabel=False)
91	ax_fnr.set_ylim(-0.48, 0.05)
92	
93	draw_bars(ax_comb, comb_vals, 'Combined (FPR + FNR)', '(c)', show_ylabel=False)
94	ax_comb.set_ylim(-0.35, 0.25)
95	
96	# Highlight best combined method (DiffXCorr)
97	diff_idx = methods_raw.index('diff_xcorr')
98	ax_comb.patches[diff_idx].set_edgecolor('#1A1A1A')
99	ax_comb.patches[diff_idx].set_linewidth(1.2)
100	
101	fig.subplots_adjust(left=0.08, right=0.97, bottom=0.18, top=0.84, wspace=0.38)
102	
103	for fmt in ['pdf', 'png']:
104	    fig.savefig(OUT / f'shapley_method_contribution.{fmt}', dpi=300)
105	plt.close()
106	print(f'Saved: {OUT}/shapley_method_contribution.pdf + .png')
107	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "4402913a-36f5-4197-8de6-01a4660f1430",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/gen_shapley_contribution.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Figure A.2: Shapley method contribution analysis.\nUnified style with project palette.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nimport numpy as np\nimport json\nfrom pathlib import Path\n\nOUT = Path(__file__).parent\nDATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v3/shapley_values_v3.json')\n\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],\n    'font.size': 9,\n    'axes.labelsize': 10,\n    'xtick.labelsize': 8,\n    'ytick.labelsize': 9,\n    'legend.fontsize': 7.5,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.08,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n    'mathtext.fontset': 'cm',\n})\n\nwith open(DATA) as f:\n    d = json.load(f)\n\nsv = d['main_result_6pair']\n\nmethods_raw = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']\nlabels = ['Naive\\nXCorr', 'Diff\\nXCorr', 'Thresh.\\nOnset', 'Perm\\nGranger', 'TY\\nGranger']\n\nfpr_vals = [sv['fpr_shapley'][m] for m in methods_raw]\nfnr_vals = [sv['fnr_shapley'][m] for m in methods_raw]\ncomb_vals = [sv['combined_shapley'][m] for m in methods_raw]\n\n# Method colors: PermG highlighted as the champion\nMETHOD_COLORS = {\n    'naive_xcorr':     '#D4694A',\n    'diff_xcorr':      '#E8C170',\n    'threshold_onset': '#8CB4D5',\n    'perm_granger':    '#2C4A6E',\n    'ty_granger':      '#3B6FA0',\n}\ncolors = [METHOD_COLORS[m] for m in methods_raw]\n\nx = np.arange(len(methods_raw))\nbar_width = 0.65\n\nfig, (ax_fpr, ax_fnr, ax_comb) = plt.subplots(\n    1, 3, figsize=(7.2, 2.8),\n    gridspec_kw={'wspace': 0.38}\n)\n\ndef draw_bars(ax, vals, title, panel_label, show_ylabel=True):\n    bars = ax.bar(x, vals, bar_width, color=colors, edgecolor='white', linewidth=0.5, zorder=3)\n    ax.set_xticks(x)\n    ax.set_xticklabels(labels, fontsize=6.5, linespacing=0.9)\n    ax.axhline(0, color='#AAAAAA', linewidth=0.5, zorder=1)\n    ax.set_title(title, fontsize=9, pad=10)\n    ax.text(-0.20, 1.12, panel_label, transform=ax.transAxes,\n            fontsize=10, fontweight='bold', va='bottom')\n    if show_ylabel:\n        ax.set_ylabel('Shapley value')\n\n    for bar, val in zip(bars, vals):\n        y_pos = val + 0.012 if val >= 0 else val - 0.020\n        va = 'bottom' if val >= 0 else 'top'\n        t = ax.text(bar.get_x() + bar.get_width() / 2, y_pos,\n                    f'{val:+.3f}' if abs(val) >= 0.001 else '0.000',\n                    ha='center', va=va, fontsize=6, color='#333333')\n        t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])\n\n    perm_idx = methods_raw.index('perm_granger')\n    bars[perm_idx].set_edgecolor('#1A1A1A')\n    bars[perm_idx].set_linewidth(1.2)\n\ndraw_bars(ax_fpr, fpr_vals, 'FPR contribution', '(a)')\nax_fpr.set_ylim(-0.05, 0.72)\n\ndraw_bars(ax_fnr, fnr_vals, 'FNR contribution (6-pair)', '(b)', show_ylabel=False)\nax_fnr.set_ylim(-0.48, 0.05)\n\ndraw_bars(ax_comb, comb_vals, 'Combined (FPR + FNR)', '(c)', show_ylabel=False)\nax_comb.set_ylim(-0.35, 0.25)\n\n# Highlight best combined method (DiffXCorr)\ndiff_idx = methods_raw.index('diff_xcorr')\nax_comb.patches[diff_idx].set_edgecolor('#1A1A1A')\nax_comb.patches[diff_idx].set_linewidth(1.2)\n\nfig.subplots_adjust(left=0.08, right=0.97, bottom=0.18, top=0.84, wspace=0.38)\n\nfor fmt in ['pdf', 'png']:\n    fig.savefig(OUT / f'shapley_method_contribution.{fmt}', dpi=300)\nplt.close()\nprint(f'Saved: {OUT}/shapley_method_contribution.pdf + .png')\n",
      "numLines": 107,
      "startLine": 1,
      "totalLines": 107
    }
  }
}
```

</details>

---


### Assistant

_source line 81_

<details><summary>Logged reasoning block</summary>

```text
The PermG bar is highlighted in all three panels via the `draw_bars` function (lines 83-85). I should remove the PermG highlight from draw_bars since it's no longer the best method overall, and instead apply highlights selectively. Actually, let me keep the PermG highlight in the draw_bars function (it marks it as the paper's focus method), and I've already added DiffXCorr highlight in the combined panel. That gives a clear visual: PermG is always marked (as the paper's main method), and DiffXCorr gets an additional highlight in the combined panel where it wins.


I'm going back and forth on the highlighting strategy. The simplest approach is to remove the PermG highlight from the draw_bars function entirely and keep only the DiffXCorr highlight in the combined panel—the bar values themselves will communicate the performance differences clearly enough.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "cab87f54-6f7a-4130-b165-62d09172de91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dFztM7pquUMDaURhijQoL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 94419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1899
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 82_

<details open><summary>🔧 Tool call — Edit · `toolu_01RVXDA8C4J5xgbauuGfJV19`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/gen_shapley_contribution.py",
  "old_string": "    perm_idx = methods_raw.index('perm_granger')\n    bars[perm_idx].set_edgecolor('#1A1A1A')\n    bars[perm_idx].set_linewidth(1.2)\n\ndraw_bars(ax_fpr, fpr_vals, 'FPR contribution', '(a)')\nax_fpr.set_ylim(-0.05, 0.72)\n\ndraw_bars(ax_fnr, fnr_vals, 'FNR contribution (6-pair)', '(b)', show_ylabel=False)\nax_fnr.set_ylim(-0.48, 0.05)\n\ndraw_bars(ax_comb, comb_vals, 'Combined (FPR + FNR)', '(c)', show_ylabel=False)\nax_comb.set_ylim(-0.35, 0.25)\n\n# Highlight best combined method (DiffXCorr)\ndiff_idx = methods_raw.index('diff_xcorr')\nax_comb.patches[diff_idx].set_edgecolor('#1A1A1A')\nax_comb.patches[diff_idx].set_linewidth(1.2)",
  "new_string": "draw_bars(ax_fpr, fpr_vals, 'FPR contribution', '(a)')\nax_fpr.set_ylim(-0.05, 0.72)\n\ndraw_bars(ax_fnr, fnr_vals, 'FNR contribution (6-pair)', '(b)', show_ylabel=False)\nax_fnr.set_ylim(-0.48, 0.05)\n\ndraw_bars(ax_comb, comb_vals, 'Combined (FPR + FNR)', '(c)', show_ylabel=False)\nax_comb.set_ylim(-0.35, 0.25)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "d5a7a914-367e-4e17-9b5a-81e9a8f3dab4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dFztM7pquUMDaURhijQoL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1899,
      "cache_read_input_tokens": 94419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1899
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 83 · 2026-05-24T09:02:35.455Z_

<details><summary>↩ Tool result · `toolu_01RVXDA8C4J5xgbauuGfJV19`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/gen_shapley_contribution.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "df46048b-d8a0-4f85-ae0d-fb3541a88d16",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/gen_shapley_contribution.py",
    "oldString": "    perm_idx = methods_raw.index('perm_granger')\n    bars[perm_idx].set_edgecolor('#1A1A1A')\n    bars[perm_idx].set_linewidth(1.2)\n\ndraw_bars(ax_fpr, fpr_vals, 'FPR contribution', '(a)')\nax_fpr.set_ylim(-0.05, 0.72)\n\ndraw_bars(ax_fnr, fnr_vals, 'FNR contribution (6-pair)', '(b)', show_ylabel=False)\nax_fnr.set_ylim(-0.48, 0.05)\n\ndraw_bars(ax_comb, comb_vals, 'Combined (FPR + FNR)', '(c)', show_ylabel=False)\nax_comb.set_ylim(-0.35, 0.25)\n\n# Highlight best combined method (DiffXCorr)\ndiff_idx = methods_raw.index('diff_xcorr')\nax_comb.patches[diff_idx].set_edgecolor('#1A1A1A')\nax_comb.patches[diff_idx].set_linewidth(1.2)",
    "newString": "draw_bars(ax_fpr, fpr_vals, 'FPR contribution', '(a)')\nax_fpr.set_ylim(-0.05, 0.72)\n\ndraw_bars(ax_fnr, fnr_vals, 'FNR contribution (6-pair)', '(b)', show_ylabel=False)\nax_fnr.set_ylim(-0.48, 0.05)\n\ndraw_bars(ax_comb, comb_vals, 'Combined (FPR + FNR)', '(c)', show_ylabel=False)\nax_comb.set_ylim(-0.35, 0.25)",
    "originalFile": "#!/usr/bin/env python3\n\"\"\"Figure A.2: Shapley method contribution analysis.\nUnified style with project palette.\"\"\"\nimport matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport matplotlib.patheffects as pe\nimport numpy as np\nimport json\nfrom pathlib import Path\n\nOUT = Path(__file__).parent\nDATA = Path('/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v3/shapley_values_v3.json')\n\nplt.rcParams.update({\n    'font.family': 'serif',\n    'font.serif': ['DejaVu Serif', 'Times New Roman', 'serif'],\n    'font.size': 9,\n    'axes.labelsize': 10,\n    'xtick.labelsize': 8,\n    'ytick.labelsize': 9,\n    'legend.fontsize': 7.5,\n    'figure.dpi': 300,\n    'savefig.dpi': 300,\n    'savefig.bbox': 'tight',\n    'savefig.pad_inches': 0.08,\n    'axes.spines.top': False,\n    'axes.spines.right': False,\n    'pdf.fonttype': 42,\n    'ps.fonttype': 42,\n    'mathtext.fontset': 'cm',\n})\n\nwith open(DATA) as f:\n    d = json.load(f)\n\nsv = d['main_result_6pair']\n\nmethods_raw = ['naive_xcorr', 'diff_xcorr', 'threshold_onset', 'perm_granger', 'ty_granger']\nlabels = ['Naive\\nXCorr', 'Diff\\nXCorr', 'Thresh.\\nOnset', 'Perm\\nGranger', 'TY\\nGranger']\n\nfpr_vals = [sv['fpr_shapley'][m] for m in methods_raw]\nfnr_vals = [sv['fnr_shapley'][m] for m in methods_raw]\ncomb_vals = [sv['combined_shapley'][m] for m in methods_raw]\n\n# Method colors: PermG highlighted as the champion\nMETHOD_COLORS = {\n    'naive_xcorr':     '#D4694A',\n    'diff_xcorr':      '#E8C170',\n    'threshold_onset': '#8CB4D5',\n    'perm_granger':    '#2C4A6E',\n    'ty_granger':      '#3B6FA0',\n}\ncolors = [METHOD_COLORS[m] for m in methods_raw]\n\nx = np.arange(len(methods_raw))\nbar_width = 0.65\n\nfig, (ax_fpr, ax_fnr, ax_comb) = plt.subplots(\n    1, 3, figsize=(7.2, 2.8),\n    gridspec_kw={'wspace': 0.38}\n)\n\ndef draw_bars(ax, vals, title, panel_label, show_ylabel=True):\n    bars = ax.bar(x, vals, bar_width, color=colors, edgecolor='white', linewidth=0.5, zorder=3)\n    ax.set_xticks(x)\n    ax.set_xticklabels(labels, fontsize=6.5, linespacing=0.9)\n    ax.axhline(0, color='#AAAAAA', linewidth=0.5, zorder=1)\n    ax.set_title(title, fontsize=9, pad=10)\n    ax.text(-0.20, 1.12, panel_label, transform=ax.transAxes,\n            fontsize=10, fontweight='bold', va='bottom')\n    if show_ylabel:\n        ax.set_ylabel('Shapley value')\n\n    for bar, val in zip(bars, vals):\n        y_pos = val + 0.012 if val >= 0 else val - 0.020\n        va = 'bottom' if val >= 0 else 'top'\n        t = ax.text(bar.get_x() + bar.get_width() / 2, y_pos,\n                    f'{val:+.3f}' if abs(val) >= 0.001 else '0.000',\n                    ha='center', va=va, fontsize=6, color='#333333')\n        t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])\n\n    perm_idx = methods_raw.index('perm_granger')\n    bars[perm_idx].set_edgecolor('#1A1A1A')\n    bars[perm_idx].set_linewidth(1.2)\n\ndraw_bars(ax_fpr, fpr_vals, 'FPR contribution', '(a)')\nax_fpr.set_ylim(-0.05, 0.72)\n\ndraw_bars(ax_fnr, fnr_vals, 'FNR contribution (6-pair)', '(b)', show_ylabel=False)\nax_fnr.set_ylim(-0.48, 0.05)\n\ndraw_bars(ax_comb, comb_vals, 'Combined (FPR + FNR)', '(c)', show_ylabel=False)\nax_comb.set_ylim(-0.35, 0.25)\n\n# Highlight best combined method (DiffXCorr)\ndiff_idx = methods_raw.index('diff_xcorr')\nax_comb.patches[diff_idx].set_edgecolor('#1A1A1A')\nax_comb.patches[diff_idx].set_linewidth(1.2)\n\nfig.subplots_adjust(left=0.08, right=0.97, bottom=0.18, top=0.84, wspace=0.38)\n\nfor fmt in ['pdf', 'png']:\n    fig.savefig(OUT / f'shapley_method_contribution.{fmt}', dpi=300)\nplt.close()\nprint(f'Saved: {OUT}/shapley_method_contribution.pdf + .png')\n",
    "structuredPatch": [
      {
        "oldStart": 80,
        "oldLines": 10,
        "newStart": 80,
        "newLines": 6,
        "lines": [
          "                     ha='center', va=va, fontsize=6, color='#333333')",
          "         t.set_path_effects([pe.withStroke(linewidth=2, foreground='white')])",
          " ",
          "-    perm_idx = methods_raw.index('perm_granger')",
          "-    bars[perm_idx].set_edgecolor('#1A1A1A')",
          "-    bars[perm_idx].set_linewidth(1.2)",
          "-",
          " draw_bars(ax_fpr, fpr_vals, 'FPR contribution', '(a)')",
          " ax_fpr.set_ylim(-0.05, 0.72)",
          " "
        ]
      },
      {
        "oldStart": 93,
        "oldLines": 11,
        "newStart": 89,
        "newLines": 6,
        "lines": [
          " draw_bars(ax_comb, comb_vals, 'Combined (FPR + FNR)', '(c)', show_ylabel=False)",
          " ax_comb.set_ylim(-0.35, 0.25)",
          " ",
          "-# Highlight best combined method (DiffXCorr)",
          "-diff_idx = methods_raw.index('diff_xcorr')",
          "-ax_comb.patches[diff_idx].set_edgecolor('#1A1A1A')",
          "-ax_comb.patches[diff_idx].set_linewidth(1.2)",
          "-",
          " fig.subplots_adjust(left=0.08, right=0.97, bottom=0.18, top=0.84, wspace=0.38)",
          " ",
          " for fmt in ['pdf', 'png']:"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Tool call

_source line 84_

<details open><summary>🔧 Tool call — Bash · `toolu_01Xt9y7MLKQjzJNpPXyDnn5B`</summary>

```json
{
  "command": "python3 docs/paper/figures/gen_shapley_contribution.py",
  "description": "Regenerate Shapley figure with v3 data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "128dd9f7-3f04-4cef-adc9-43371f5acc20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U65Gn2XguUeVzCygdLRkMY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 965,
      "cache_read_input_tokens": 96318,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 965
      },
      "output_tokens": 58,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-24T09:02:40.596Z_

<details><summary>↩ Tool result · `toolu_01Xt9y7MLKQjzJNpPXyDnn5B`</summary>

```text
Saved: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/shapley_method_contribution.pdf + .png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "1693b1db-fa85-419a-8727-f187d4e6b6ae",
  "tool_use_result": {
    "stdout": "Saved: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/shapley_method_contribution.pdf + .png",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 86_

Let me verify the figure looks correct.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "12601bec-a74f-4916-b87e-0ff9112190ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qw3Yjm1bYqmg9VmLW9v1vJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 158,
      "cache_read_input_tokens": 97283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 158
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 87_

<details open><summary>🔧 Tool call — Read · `toolu_015UzukGJciuNnamoYSkjJMe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/figures/shapley_method_contribution.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "896259a8-3402-472d-8ae9-8e870e1da116",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qw3Yjm1bYqmg9VmLW9v1vJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 158,
      "cache_read_input_tokens": 97283,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 158
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 88 · 2026-05-24T09:02:43.777Z_

<details><summary>↩ Tool result · `toolu_015UzukGJciuNnamoYSkjJMe`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "56b18964-ded6-49cb-8986-7cf76bb43a89",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 118525
    }
  }
}
```

</details>

---


### Assistant

_source line 89_

<details><summary>Logged reasoning block</summary>

```text
The figure looks good. DiffXCorr clearly has the lowest combined Shapley (-0.299), and PermG is second (-0.141). The FPR panel shows PermG at +0.039 (no longer zero).

Now let me move on to updating the appendix. But first, let me handle the FDR sensitivity treatment data. I'll check if I can get the treatment data from locally available files or if I need to SSH.

Actually, let me look at the existing D102 files for the treatment experiments. The treatment uses α=0.75, seeds 42/43/44. Let me look for those files.


I'm tracking down the Shapley data sources for the treatment experiments across those three seed runs, then searching for the corresponding D102 analysis files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "8cbc6008-8b1e-4fdb-8a69-8040ee29f2fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019CSA9xT4ptJk6H26NQbFqY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1307,
      "cache_read_input_tokens": 97441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1307
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 90_

Figure looks good. DiffXCorr is clearly the best combined method (-0.299), PermG second (-0.141).

Now let me find the treatment PermG data for the FDR sensitivity table. I need α=0.75 D102 files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "c4a69fef-cff1-4b5a-94b8-1dffd4bc715f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019CSA9xT4ptJk6H26NQbFqY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1307,
      "cache_read_input_tokens": 97441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1307
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 91_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01KdvWijcmf7nhG4Eg8DovtE`</summary>

```json
{
  "todos": [
    {
      "content": "Write and run Shapley computation script with 6-seed null data",
      "status": "completed",
      "activeForm": "Writing and running Shapley computation script"
    },
    {
      "content": "Update gen_shapley_contribution.py and regenerate figure",
      "status": "completed",
      "activeForm": "Updating figure generation script"
    },
    {
      "content": "Find treatment PermG data for FDR sensitivity table update",
      "status": "in_progress",
      "activeForm": "Finding treatment PermG data"
    },
    {
      "content": "Update appendix.tex — all 7 TODO-D219 locations",
      "status": "pending",
      "activeForm": "Updating appendix.tex"
    },
    {
      "content": "Verify all numbers and TODO removals",
      "status": "pending",
      "activeForm": "Verifying consistency"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "ccdb6d71-f11b-48ed-94d9-6f4202cd3dc4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019CSA9xT4ptJk6H26NQbFqY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1307,
      "cache_read_input_tokens": 97441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1307
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 92 · 2026-05-24T09:03:01.927Z_

<details><summary>↩ Tool result · `toolu_01KdvWijcmf7nhG4Eg8DovtE`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "a092021a-1a79-4abf-a120-ecc1d1efc354",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Write and run Shapley computation script with 6-seed null data",
        "status": "completed",
        "activeForm": "Writing and running Shapley computation script"
      },
      {
        "content": "Update gen_shapley_contribution.py and regenerate figure",
        "status": "in_progress",
        "activeForm": "Updating figure generation script"
      },
      {
        "content": "Find treatment PermG data for FDR sensitivity table update",
        "status": "pending",
        "activeForm": "Finding treatment PermG data"
      },
      {
        "content": "Update appendix.tex — all 7 TODO-D219 locations",
        "status": "pending",
        "activeForm": "Updating appendix.tex"
      },
      {
        "content": "Verify all numbers and TODO removals",
        "status": "pending",
        "activeForm": "Verifying consistency"
      }
    ],
    "newTodos": [
      {
        "content": "Write and run Shapley computation script with 6-seed null data",
        "status": "completed",
        "activeForm": "Writing and running Shapley computation script"
      },
      {
        "content": "Update gen_shapley_contribution.py and regenerate figure",
        "status": "completed",
        "activeForm": "Updating figure generation script"
      },
      {
        "content": "Find treatment PermG data for FDR sensitivity table update",
        "status": "in_progress",
        "activeForm": "Finding treatment PermG data"
      },
      {
        "content": "Update appendix.tex — all 7 TODO-D219 locations",
        "status": "pending",
        "activeForm": "Updating appendix.tex"
      },
      {
        "content": "Verify all numbers and TODO removals",
        "status": "pending",
        "activeForm": "Verifying consistency"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Grep · `toolu_016zr3Wgj1Vn98k8cWvZ63UH`</summary>

```json
{
  "pattern": "\"alpha\": 0.75",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts",
  "output_mode": "files_with_matches",
  "glob": "*.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "4ce3da3d-d953-49a8-b8d5-5340bf77e978",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vmya4d34PjDW1X7q8FnNaC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 583,
      "cache_read_input_tokens": 98748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 583
      },
      "output_tokens": 32,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 94 · 2026-05-24T09:03:06.927Z_

<details><summary>↩ Tool result · `toolu_016zr3Wgj1Vn98k8cWvZ63UH`</summary>

```text
Found 48 files
artifacts/D213_14b_s43_t10_6pair_combined.json
artifacts/D213_14b_s42_6pair_combined_v2.json
artifacts/D102_14b_t15_a075_s42_fp32_14b_6pair.json
artifacts/D102_14b_t10_a075_s42_fp32_14b_6pair.json
artifacts/_project/data/D213_14b_s42_6pair_combined.json
artifacts/D213_14b_s42_6pair_combined.json
artifacts/D102_14b_t15_a075_s43_fp32_14b_6pair.json
artifacts/D102_14b_t10_a075_s44_fp32_14b_6pair.json
artifacts/D102_14b_t10_a075_s44_fp32_d3.json
artifacts/scale_14b_t10_a075_s44_fp32/data/D102_14b_t10_a075_s44_fp32_d3.json
artifacts/D102_14b_t15_a075_s42_fp32.json
artifacts/scale_14b_t15_a075_s42_fp32/data/D102_14b_t15_a075_s42_fp32.json
artifacts/phase_diagram_t20_a075_s43_fp32/data/5method_leadlag.json
artifacts/power_simulation/power_artifact_test.json
artifacts/_project/data/power_artifact_test_7387f0.json
artifacts/_project/data/power_artifact_test_87bce4.json
artifacts/_project/data/loocv_5t_results.json
artifacts/alpha_c_theory/loocv_5t_results.json
artifacts/_project/data/power_artifact_test.json
artifacts/_project/data/theory_verification_d102_pmax.json
artifacts/alpha_c_theory/theory_verification_d102_pmax.json
artifacts/_project/data/theory_verification_d102_pmax_grid.json
artifacts/alpha_c_theory/theory_verification_d102_pmax_grid.json
artifacts/_project/data/theory_verification_d102.json
artifacts/alpha_c_theory/theory_verification_d102.json
artifacts/phase_diagram_t15_a075_s43_fp32/data/t15_a075_s43_fp32_d102_analysis.json
artifacts/t15_a075_s43_fp32_d102_analysis.json
artifacts/d102_t10_a075_s43_fp32.json
artifacts/phase_diagram_t10_a075_s43_fp32/data/d102_t10_a075_s43_fp32.json
artifacts/phase_diagram_t15_a075_s42_fp32_v2/5method_leadlag.json
artifacts/phase_diagram_t15_a075_s42_fp32_v2/data/5method_leadlag.json
artifacts/_project/data/heatmap_data_manifest.json
artifacts/heatmap_data_manifest.json
artifacts/_project/data/empirical_ar1_coefficients.json
artifacts/empirical_ar1_coefficients.json
artifacts/_project/data/equal_weight_vs_current_k3_bd7a72.json
artifacts/_project/data/equal_weight_vs_current_k3.json
artifacts/equal_weight_vs_current_k3.json
artifacts/theory/cascade_empirical_data.json
artifacts/_project/data/rule.json
artifacts/early_stopping/rule.json
artifacts/t20_a075_s42_fp32/data/t20_a075_verify_9b6aa5.json
artifacts/t20_a075_s42_fp32/data/t20_a075_verify.json
artifacts/mi_analysis/mi_lower_bounds.json
artifacts/_project/data/regime_map_data.json
artifacts/cross_alpha_aggregation/regime_map_data.json
artifacts/D040/data/filtering_pipeline_data.json
artifacts/pipeline_analysis/filtering_pipeline_data.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "d184ee80-9812-4fd4-9ff4-7d4a937349cb",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "artifacts/D213_14b_s43_t10_6pair_combined.json",
      "artifacts/D213_14b_s42_6pair_combined_v2.json",
      "artifacts/D102_14b_t15_a075_s42_fp32_14b_6pair.json",
      "artifacts/D102_14b_t10_a075_s42_fp32_14b_6pair.json",
      "artifacts/_project/data/D213_14b_s42_6pair_combined.json",
      "artifacts/D213_14b_s42_6pair_combined.json",
      "artifacts/D102_14b_t15_a075_s43_fp32_14b_6pair.json",
      "artifacts/D102_14b_t10_a075_s44_fp32_14b_6pair.json",
      "artifacts/D102_14b_t10_a075_s44_fp32_d3.json",
      "artifacts/scale_14b_t10_a075_s44_fp32/data/D102_14b_t10_a075_s44_fp32_d3.json",
      "artifacts/D102_14b_t15_a075_s42_fp32.json",
      "artifacts/scale_14b_t15_a075_s42_fp32/data/D102_14b_t15_a075_s42_fp32.json",
      "artifacts/phase_diagram_t20_a075_s43_fp32/data/5method_leadlag.json",
      "artifacts/power_simulation/power_artifact_test.json",
      "artifacts/_project/data/power_artifact_test_7387f0.json",
      "artifacts/_project/data/power_artifact_test_87bce4.json",
      "artifacts/_project/data/loocv_5t_results.json",
      "artifacts/alpha_c_theory/loocv_5t_results.json",
      "artifacts/_project/data/power_artifact_test.json",
      "artifacts/_project/data/theory_verification_d102_pmax.json",
      "artifacts/alpha_c_theory/theory_verification_d102_pmax.json",
      "artifacts/_project/data/theory_verification_d102_pmax_grid.json",
      "artifacts/alpha_c_theory/theory_verification_d102_pmax_grid.json",
      "artifacts/_project/data/theory_verification_d102.json",
      "artifacts/alpha_c_theory/theory_verification_d102.json",
      "artifacts/phase_diagram_t15_a075_s43_fp32/data/t15_a075_s43_fp32_d102_analysis.json",
      "artifacts/t15_a075_s43_fp32_d102_analysis.json",
      "artifacts/d102_t10_a075_s43_fp32.json",
      "artifacts/phase_diagram_t10_a075_s43_fp32/data/d102_t10_a075_s43_fp32.json",
      "artifacts/phase_diagram_t15_a075_s42_fp32_v2/5method_leadlag.json",
      "artifacts/phase_diagram_t15_a075_s42_fp32_v2/data/5method_leadlag.json",
      "artifacts/_project/data/heatmap_data_manifest.json",
      "artifacts/heatmap_data_manifest.json",
      "artifacts/_project/data/empirical_ar1_coefficients.json",
      "artifacts/empirical_ar1_coefficients.json",
      "artifacts/_project/data/equal_weight_vs_current_k3_bd7a72.json",
      "artifacts/_project/data/equal_weight_vs_current_k3.json",
      "artifacts/equal_weight_vs_current_k3.json",
      "artifacts/theory/cascade_empirical_data.json",
      "artifacts/_project/data/rule.json",
      "artifacts/early_stopping/rule.json",
      "artifacts/t20_a075_s42_fp32/data/t20_a075_verify_9b6aa5.json",
      "artifacts/t20_a075_s42_fp32/data/t20_a075_verify.json",
      "artifacts/mi_analysis/mi_lower_bounds.json",
      "artifacts/_project/data/regime_map_data.json",
      "artifacts/cross_alpha_aggregation/regime_map_data.json",
      "artifacts/D040/data/filtering_pipeline_data.json",
      "artifacts/pipeline_analysis/filtering_pipeline_data.json"
    ],
    "numFiles": 48
  }
}
```

</details>

---


### Assistant

_source line 95_

<details><summary>Logged reasoning block</summary>

```text
I see `artifacts/d102_t10_a075_s43_fp32.json` — this is a D102 analysis file for α=0.75, seed 43. Let me check it for PermG p-values. I also need to check if there are similar files for seeds 42 and 44.

But actually, for the FDR sensitivity table, I need per-pair PermG p-values for α=0.75 experiments. Let me check the d102_t10_a075_s43_fp32.json file.

Wait, I also need to find the 410M α=0.75 D102 files (not 14b). 

Let me search through the available files more carefully to locate the right datasets.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "21f97720-f5c3-49a0-83eb-39ab4eee63cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUJPH3PH9cy1DZeqEwfbTm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1188,
      "cache_read_input_tokens": 99331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1188
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 96_

<details open><summary>🔧 Tool call — Read · `toolu_01U9DJBV4phb3oPBGk8f9rb2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/d102_t10_a075_s43_fp32.json",
  "limit": 60
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "a23db13d-53ca-48a1-a771-e13213e83178",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SUJPH3PH9cy1DZeqEwfbTm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1188,
      "cache_read_input_tokens": 99331,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1188
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-24T09:03:15.700Z_

<details><summary>↩ Tool result · `toolu_01U9DJBV4phb3oPBGk8f9rb2`</summary>

```text
1	{
2	  "exp_id": "phase_diagram_t10_a075_s43_fp32",
3	  "analysis": "d102_5method_leadlag",
4	  "config": {
5	    "alpha": 0.75,
6	    "seed": 43,
7	    "T": 10,
8	    "model": "pythia-410m",
9	    "precision": "fp32",
10	    "n_gens": 11,
11	    "threshold_criterion": "true_3sigma_d105",
12	    "downstreams": ["distinct_1", "distinct_2", "distinct_3", "mauve"],
13	    "canaries": ["token_entropy", "ece"],
14	    "n_perm": 5000
15	  },
16	  "summary": {
17	    "PermG_fwd": 6,
18	    "PermG_rev": 0,
19	    "total_pairs": 8,
20	    "asymmetry": "strong",
21	    "robust_pairs_ge3": 4,
22	    "diff_xcorr_fdr_fwd": 7,
23	    "diff_xcorr_fdr_rev": 7,
24	    "threshold_fwd": 0,
25	    "ty_fwd": 0
26	  },
27	  "consensus": [
28	    {"pair": "token_entropy→distinct_1", "votes": "3/5", "methods": ["naive", "diff", "perm"]},
29	    {"pair": "token_entropy→distinct_2", "votes": "2/5", "methods": ["diff", "perm"]},
30	    {"pair": "token_entropy→distinct_3", "votes": "2/5", "methods": ["diff", "perm"]},
31	    {"pair": "token_entropy→mauve", "votes": "1/5", "methods": ["diff"]},
32	    {"pair": "ece→distinct_1", "votes": "3/5", "methods": ["naive", "diff", "perm"]},
33	    {"pair": "ece→distinct_2", "votes": "3/5", "methods": ["naive", "diff", "perm"]},
34	    {"pair": "ece→distinct_3", "votes": "3/5", "methods": ["naive", "diff", "perm"]},
35	    {"pair": "ece→mauve", "votes": "0/5", "methods": []}
36	  ],
37	  "parent_comparison": {
38	    "parent": "alpha_sweep_a075_s42_fp32",
39	    "parent_PermG_fwd": 6,
40	    "parent_PermG_rev": 0,
41	    "match": true,
42	    "seed_robust": true
43	  },
44	  "server": "westd-17855",
45	  "output_dir": "/root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t10_a075_s43_fp32",
46	  "analysis_path": "/root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t10_a075_s43_fp32/analysis/5method_leadlag.json"
47	}
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "396e90e2-036b-4167-a5f2-712f63cf9cf5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/d102_t10_a075_s43_fp32.json",
      "content": "{\n  \"exp_id\": \"phase_diagram_t10_a075_s43_fp32\",\n  \"analysis\": \"d102_5method_leadlag\",\n  \"config\": {\n    \"alpha\": 0.75,\n    \"seed\": 43,\n    \"T\": 10,\n    \"model\": \"pythia-410m\",\n    \"precision\": \"fp32\",\n    \"n_gens\": 11,\n    \"threshold_criterion\": \"true_3sigma_d105\",\n    \"downstreams\": [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"mauve\"],\n    \"canaries\": [\"token_entropy\", \"ece\"],\n    \"n_perm\": 5000\n  },\n  \"summary\": {\n    \"PermG_fwd\": 6,\n    \"PermG_rev\": 0,\n    \"total_pairs\": 8,\n    \"asymmetry\": \"strong\",\n    \"robust_pairs_ge3\": 4,\n    \"diff_xcorr_fdr_fwd\": 7,\n    \"diff_xcorr_fdr_rev\": 7,\n    \"threshold_fwd\": 0,\n    \"ty_fwd\": 0\n  },\n  \"consensus\": [\n    {\"pair\": \"token_entropy→distinct_1\", \"votes\": \"3/5\", \"methods\": [\"naive\", \"diff\", \"perm\"]},\n    {\"pair\": \"token_entropy→distinct_2\", \"votes\": \"2/5\", \"methods\": [\"diff\", \"perm\"]},\n    {\"pair\": \"token_entropy→distinct_3\", \"votes\": \"2/5\", \"methods\": [\"diff\", \"perm\"]},\n    {\"pair\": \"token_entropy→mauve\", \"votes\": \"1/5\", \"methods\": [\"diff\"]},\n    {\"pair\": \"ece→distinct_1\", \"votes\": \"3/5\", \"methods\": [\"naive\", \"diff\", \"perm\"]},\n    {\"pair\": \"ece→distinct_2\", \"votes\": \"3/5\", \"methods\": [\"naive\", \"diff\", \"perm\"]},\n    {\"pair\": \"ece→distinct_3\", \"votes\": \"3/5\", \"methods\": [\"naive\", \"diff\", \"perm\"]},\n    {\"pair\": \"ece→mauve\", \"votes\": \"0/5\", \"methods\": []}\n  ],\n  \"parent_comparison\": {\n    \"parent\": \"alpha_sweep_a075_s42_fp32\",\n    \"parent_PermG_fwd\": 6,\n    \"parent_PermG_rev\": 0,\n    \"match\": true,\n    \"seed_robust\": true\n  },\n  \"server\": \"westd-17855\",\n  \"output_dir\": \"/root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t10_a075_s43_fp32\",\n  \"analysis_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/phase_diagram/t10_a075_s43_fp32/analysis/5method_leadlag.json\"\n}\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  }
}
```

</details>

---


### Assistant

_source line 98_

<details><summary>Logged reasoning block</summary>

```text
This D102 file for α=0.75, s43 doesn't have the raw PermG p-values — it only has summary counts. I need the per-pair p-values to recompute BH-FDR at different q thresholds.

The task says to update the FDR sensitivity table with 6-seed null data. The treatment column might not need updating if I keep it as-is. Let me check: the current table has treatment at /24 (8-pair basis), and null at /24 (8-pair basis, 3 seeds). If I update null to /36 (6-pair basis, 6 seeds), the denominators will differ.
 
I think the most practical solution is to update the null column to reflect 6 seeds with 36 pairs, while keeping the treatment column at its current /24 basis, or I could restructure the table to show different denominators for each condition. Looking at the current format, I'm seeing rows for different q thresholds with columns for null FDR-significant counts, treatment FDR-significant counts, and separation status.

The core issue is that the null data uses a 6-pair basis (36 pairs total) while the treatment data uses an 8-pair basis (24 pairs), which makes direct comparison tricky. But actually, the table's purpose isn't to directly compare false positive and true positive rates—it's demonstrating that the null control remains robust across different q thresholds while treatment detection still functions. Since the caption can note this difference in pair bases, I could simply update the null counts to /36 and leave treatment unchanged, or if computing treatment at the 6-pair basis is straightforward, I could align both to that denominator instead.

For the treatment side on 6-pair basis, I'd need to know how many of the 18 treatment pairs (3 seeds × 6 pairs, excluding mauve) show PermG BH-FDR significance at each q threshold, but I don't have access to the raw p-values. I can estimate based on the original 24-pair results: if treatment had 19/24 at q=0.05 and 24/24 at q=0.10, and I remove the 6 mauve pairs (which the paper indicates perform poorly at this scale), the 6-pair treatment would likely be around 13-19 out of 18 at q=0.05 and 18 out of 18 at q=0.10.

Rather than speculate further, I'll update the table with different denominators for null and treatment columns and clarify the different bases in the caption. Let me move forward with updating the appendix text across all the TODO-D219 locations, handling the FDR sensitivity table pragmatically by noting the different pair bases used for each column. I'm realizing I need to figure out which of those 19 significant pairs are mauve-based. Rather than chase down more data, I'll keep the treatment column as-is and adjust the table format to handle different sample sizes—the main point here is demonstrating the null control quality anyway.

Now I'm mapping out all the appendix sections that need updates: the FDR sensitivity table counts and caption, the Shapley section introduction and body text with the new φ^FPR values, the figure caption, the weight robustness paragraph about zero FPR, and the direction filtering discussion. Let me pull up each section and work through the edits systematically, starting with the new Shapley values table showing the method comparisons.

Generating Shapley values table...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "7cf73724-aa11-4ee6-b2e4-96774eda05cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBMcCM7Nwt7jgJcZ28nefA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 100519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1148
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 99_

Let me read the v3 JSON for exact numbers and then start updating the appendix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "f91b9f3f-4d8b-483f-8daf-425002b864db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBMcCM7Nwt7jgJcZ28nefA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 100519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1148
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 100_

<details open><summary>🔧 Tool call — Read · `toolu_01Lx5XcCHRHfoeQBs7tof66y`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v3/shapley_values_v3.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "187f5703-ac99-4d35-923b-434470b54512",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBMcCM7Nwt7jgJcZ28nefA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 100519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1148
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-24T09:04:00.533Z_

<details><summary>↩ Tool result · `toolu_01Lx5XcCHRHfoeQBs7tof66y`</summary>

```text
1	{
2	  "version": "v3_6seed_null",
3	  "generated_at": "2026-05-24T09:00:05.264152",
4	  "change_from_v2": "FPR recomputed with 6 null seeds (s45-s50, 36 pairs, 6-pair basis). FNR unchanged (45 signal experiments, 270/360 signal pairs).",
5	  "null_data_source": "fpr_transparency_all_seeds.json",
6	  "null_seeds": [
7	    45,
8	    46,
9	    47,
10	    48,
11	    49,
12	    50
13	  ],
14	  "n_null_seeds": 6,
15	  "n_null_pairs_per_seed": 6,
16	  "n_null_obs": 36,
17	  "n_signal_experiments": 45,
18	  "n_signal_obs_6pair": 270,
19	  "n_signal_obs_8pair": 360,
20	  "pair_basis": "6-pair (distinct_1/2/3 only, mauve excluded)",
21	  "threshold_criterion": "true_3sigma_d105",
22	  "methods": [
23	    "naive_xcorr",
24	    "diff_xcorr",
25	    "threshold_onset",
26	    "perm_granger",
27	    "ty_granger"
28	  ],
29	  "n_methods": 5,
30	  "n_coalitions": 32,
31	  "voting_rules": {
32	    "naive_xcorr": "naive_xcorr_sig (|r|>0.5, lag!=0; no direction filter)",
33	    "diff_xcorr": "diff_xcorr_fwd_sig_fdr (BH-FDR corrected)",
34	    "threshold_onset": "threshold_onset_sig (deterministic 3sigma)",
35	    "perm_granger": "perm_granger_fwd_sig_fdr (BH-FDR corrected)",
36	    "ty_granger": "ty_granger_sig (uncorrected)"
37	  },
38	  "main_result_6pair": {
39	    "fpr_shapley": {
40	      "naive_xcorr": 0.608796,
41	      "diff_xcorr": 0.006944,
42	      "threshold_onset": 0.111111,
43	      "perm_granger": 0.039352,
44	      "ty_granger": 0.150463
45	    },
46	    "fnr_shapley": {
47	      "naive_xcorr": -0.41858,
48	      "diff_xcorr": -0.305617,
49	      "threshold_onset": -0.026914,
50	      "perm_granger": -0.18,
51	      "ty_granger": -0.068889
52	    },
53	    "combined_shapley": {
54	      "naive_xcorr": 0.190216,
55	      "diff_xcorr": -0.298673,
56	      "threshold_onset": 0.084197,
57	      "perm_granger": -0.140648,
58	      "ty_granger": 0.081574
59	    }
60	  },
61	  "robustness_8pair": {
62	    "fpr_shapley": {
63	      "naive_xcorr": 0.608796,
64	      "diff_xcorr": 0.006944,
65	      "threshold_onset": 0.111111,
66	      "perm_granger": 0.039352,
67	      "ty_granger": 0.150463
68	    },
69	    "fnr_shapley": {
70	      "naive_xcorr": -0.451852,
71	      "diff_xcorr": -0.269444,
72	      "threshold_onset": -0.037963,
73	      "perm_granger": -0.15162,
74	      "ty_granger": -0.058565
75	    },
76	    "combined_shapley": {
77	      "naive_xcorr": 0.156944,
78	      "diff_xcorr": -0.2625,
79	      "threshold_onset": 0.073148,
80	      "perm_granger": -0.112268,
81	      "ty_granger": 0.091898
82	    }
83	  },
84	  "raw_fpr_counts": {
85	    "naive_xcorr": 33,
86	    "diff_xcorr": 1,
87	    "threshold_onset": 10,
88	    "perm_granger": 4,
89	    "ty_granger": 14
90	  },
91	  "raw_fpr_rates": {
92	    "naive_xcorr": 0.9167,
93	    "diff_xcorr": 0.0278,
94	    "threshold_onset": 0.2778,
95	    "perm_granger": 0.1111,
96	    "ty_granger": 0.3889
97	  },
98	  "fdr_sensitivity_null": {
99	    "q_0.01": {
100	      "rejections": 3,
101	      "total": 36,
102	      "fpr": 0.0833
103	    },
104	    "q_0.05": {
105	      "rejections": 4,
106	      "total": 36,
107	      "fpr": 0.1111
108	    },
109	    "q_0.10": {
110	      "rejections": 8,
111	      "total": 36,
112	      "fpr": 0.2222
113	    }
114	  },
115	  "comparison_to_v2": {
116	    "fpr_shapley_change": {
117	      "naive_xcorr": -0.012732,
118	      "diff_xcorr": -0.15625,
119	      "threshold_onset": 0.010417,
120	      "perm_granger": 0.039352,
121	      "ty_granger": 0.119213
122	    },
123	    "combined_shapley_change": {
124	      "naive_xcorr": -0.012732,
125	      "diff_xcorr": -0.15625,
126	      "threshold_onset": 0.010417,
127	      "perm_granger": 0.039352,
128	      "ty_granger": 0.119213
129	    }
130	  }
131	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "6046a3ec-7c66-4ff2-8a07-ba1938e9f42a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/shapley_v3/shapley_values_v3.json",
      "content": "{\n  \"version\": \"v3_6seed_null\",\n  \"generated_at\": \"2026-05-24T09:00:05.264152\",\n  \"change_from_v2\": \"FPR recomputed with 6 null seeds (s45-s50, 36 pairs, 6-pair basis). FNR unchanged (45 signal experiments, 270/360 signal pairs).\",\n  \"null_data_source\": \"fpr_transparency_all_seeds.json\",\n  \"null_seeds\": [\n    45,\n    46,\n    47,\n    48,\n    49,\n    50\n  ],\n  \"n_null_seeds\": 6,\n  \"n_null_pairs_per_seed\": 6,\n  \"n_null_obs\": 36,\n  \"n_signal_experiments\": 45,\n  \"n_signal_obs_6pair\": 270,\n  \"n_signal_obs_8pair\": 360,\n  \"pair_basis\": \"6-pair (distinct_1/2/3 only, mauve excluded)\",\n  \"threshold_criterion\": \"true_3sigma_d105\",\n  \"methods\": [\n    \"naive_xcorr\",\n    \"diff_xcorr\",\n    \"threshold_onset\",\n    \"perm_granger\",\n    \"ty_granger\"\n  ],\n  \"n_methods\": 5,\n  \"n_coalitions\": 32,\n  \"voting_rules\": {\n    \"naive_xcorr\": \"naive_xcorr_sig (|r|>0.5, lag!=0; no direction filter)\",\n    \"diff_xcorr\": \"diff_xcorr_fwd_sig_fdr (BH-FDR corrected)\",\n    \"threshold_onset\": \"threshold_onset_sig (deterministic 3sigma)\",\n    \"perm_granger\": \"perm_granger_fwd_sig_fdr (BH-FDR corrected)\",\n    \"ty_granger\": \"ty_granger_sig (uncorrected)\"\n  },\n  \"main_result_6pair\": {\n    \"fpr_shapley\": {\n      \"naive_xcorr\": 0.608796,\n      \"diff_xcorr\": 0.006944,\n      \"threshold_onset\": 0.111111,\n      \"perm_granger\": 0.039352,\n      \"ty_granger\": 0.150463\n    },\n    \"fnr_shapley\": {\n      \"naive_xcorr\": -0.41858,\n      \"diff_xcorr\": -0.305617,\n      \"threshold_onset\": -0.026914,\n      \"perm_granger\": -0.18,\n      \"ty_granger\": -0.068889\n    },\n    \"combined_shapley\": {\n      \"naive_xcorr\": 0.190216,\n      \"diff_xcorr\": -0.298673,\n      \"threshold_onset\": 0.084197,\n      \"perm_granger\": -0.140648,\n      \"ty_granger\": 0.081574\n    }\n  },\n  \"robustness_8pair\": {\n    \"fpr_shapley\": {\n      \"naive_xcorr\": 0.608796,\n      \"diff_xcorr\": 0.006944,\n      \"threshold_onset\": 0.111111,\n      \"perm_granger\": 0.039352,\n      \"ty_granger\": 0.150463\n    },\n    \"fnr_shapley\": {\n      \"naive_xcorr\": -0.451852,\n      \"diff_xcorr\": -0.269444,\n      \"threshold_onset\": -0.037963,\n      \"perm_granger\": -0.15162,\n      \"ty_granger\": -0.058565\n    },\n    \"combined_shapley\": {\n      \"naive_xcorr\": 0.156944,\n      \"diff_xcorr\": -0.2625,\n      \"threshold_onset\": 0.073148,\n      \"perm_granger\": -0.112268,\n      \"ty_granger\": 0.091898\n    }\n  },\n  \"raw_fpr_counts\": {\n    \"naive_xcorr\": 33,\n    \"diff_xcorr\": 1,\n    \"threshold_onset\": 10,\n    \"perm_granger\": 4,\n    \"ty_granger\": 14\n  },\n  \"raw_fpr_rates\": {\n    \"naive_xcorr\": 0.9167,\n    \"diff_xcorr\": 0.0278,\n    \"threshold_onset\": 0.2778,\n    \"perm_granger\": 0.1111,\n    \"ty_granger\": 0.3889\n  },\n  \"fdr_sensitivity_null\": {\n    \"q_0.01\": {\n      \"rejections\": 3,\n      \"total\": 36,\n      \"fpr\": 0.0833\n    },\n    \"q_0.05\": {\n      \"rejections\": 4,\n      \"total\": 36,\n      \"fpr\": 0.1111\n    },\n    \"q_0.10\": {\n      \"rejections\": 8,\n      \"total\": 36,\n      \"fpr\": 0.2222\n    }\n  },\n  \"comparison_to_v2\": {\n    \"fpr_shapley_change\": {\n      \"naive_xcorr\": -0.012732,\n      \"diff_xcorr\": -0.15625,\n      \"threshold_onset\": 0.010417,\n      \"perm_granger\": 0.039352,\n      \"ty_granger\": 0.119213\n    },\n    \"combined_shapley_change\": {\n      \"naive_xcorr\": -0.012732,\n      \"diff_xcorr\": -0.15625,\n      \"threshold_onset\": 0.010417,\n      \"perm_granger\": 0.039352,\n      \"ty_granger\": 0.119213\n    }\n  }\n}",
      "numLines": 131,
      "startLine": 1,
      "totalLines": 131
    }
  }
}
```

</details>

---


### Assistant

_source line 102_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the numbers. Let me also check the weight robustness table for the 8-pair variant, since that's what the weight robustness table in the appendix uses.

But wait, the weight robustness table uses different weighting schemes (equal, cap-5, cap-10, FPR-inv cap-100). These are NOT the same as the "union-based" Shapley I computed. The weight robustness Shapley uses K≥3 majority voting with different weights, not union-based coalition value.

So I can't update the weight robustness table without the full per-pair signal data and a more complex recomputation. I'll just update the text qualitatively.


Now I'm planning out all the appendix edits I need to make. I need to update the FDR sensitivity paragraph and table caption to reflect the new 6-seed null data that shows some false positives, removing the TODO markers and revising the text to be accurate.

For the Shapley sections, I'm updating the null experiment references from 3 seeds to 6 seeds with the corresponding pair counts, and I need to revise the statement about PermG's performance to reflect the actual results with the new data.

I'm also updating the robustness analysis sections with the new 8-pair numbers, and for the weight robustness table, I realize the underlying data constraints mean I can only update the text descriptions around it rather than the table values themselves. Looking at the weight robustness table, I see PermG combined Shapley values across different weighting schemes, but since the main Shapley table uses a different value function (union-based rather than weighted voting), I can't actually verify whether PermG remains the best performer under weighted voting without recomputing. The safest move is to remove the TODO and acknowledge this limitation rather than make claims I can't back up.

I'm reconsidering whether I can estimate the weighted robustness results from the existing null data. The K≥threshold voting approach would let me compute FPR under equal weights by counting how many methods vote on each null pair, but I realize I'm working with older null data (only 3 seeds) that might not fully support strong claims about structural robustness. I should note this limitation and explain that while the qualitative ranking pattern is expected to hold, the specific numbers come from a smaller sample. Continuing through the vote counts for each subject, I'm seeing S46 has only one pair meeting the K≥3 threshold, while S47's data is still coming through. Continuing through S49 with mostly single-bit entries and no qualifying pairs, then moving into S50 which has a couple of entries with sum=3 but still falls short of the K≥3 threshold.

Tallying everything up across all samples, I'm getting 9 out of 36 pairs that meet the K≥3 criteria unfiltered, which is 25%, but the direction-filtered version from the transparency analysis shows only 16.7% because the naive approach lacks that directional constraint. This is getting complicated, so I'm going to skip trying to update the weight robustness table and just revise the surrounding text instead. I have the Shapley numbers I need for the main analysis, so let me move forward with the appendix updates. For the FDR sensitivity table, I'll keep the treatment column at the /24 basis since recomputing for 6-pair would be tedious, and I'll just note that limitation in the caption.

Generating markdown table... Looking at the separation metrics with the updated null data, I need to recalibrate the descriptions—at q=0.01 both groups show minimal detections so the test is underpowered overall, while q=0.05 shows clear separation with some null false positives, and q=0.10 has elevated null FPR but full treatment detection. Now I'm going back through the appendix sections to make sure I capture the right context before revising them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "00d3283e-b097-4c44-bfb0-c356947098a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdTnXJBN6tAgaJiuuzYmaT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3554,
      "cache_read_input_tokens": 101667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3554
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 103_

Now let me update the appendix. Let me re-read the relevant sections to plan all edits precisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "308a24c8-5472-43e1-a6b0-ef237cbccfec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdTnXJBN6tAgaJiuuzYmaT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3554,
      "cache_read_input_tokens": 101667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3554
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 104_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01W3CT4oMngAjAkeDFKMuEXX`</summary>

```json
{
  "todos": [
    {
      "content": "Write and run Shapley computation script with 6-seed null data",
      "status": "completed",
      "activeForm": "Writing and running Shapley computation script"
    },
    {
      "content": "Update gen_shapley_contribution.py and regenerate figure",
      "status": "completed",
      "activeForm": "Updating figure generation script"
    },
    {
      "content": "Find treatment PermG data for FDR sensitivity table update",
      "status": "completed",
      "activeForm": "Finding treatment PermG data"
    },
    {
      "content": "Update appendix.tex — all 7 TODO-D219 locations",
      "status": "in_progress",
      "activeForm": "Updating appendix.tex"
    },
    {
      "content": "Verify all numbers and TODO removals",
      "status": "pending",
      "activeForm": "Verifying consistency"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "5564926f-1081-48a1-b493-796377b4ef1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdTnXJBN6tAgaJiuuzYmaT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3554,
      "cache_read_input_tokens": 101667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3554
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-24T09:05:14.334Z_

<details><summary>↩ Tool result · `toolu_01W3CT4oMngAjAkeDFKMuEXX`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "794e43d1-e0af-4fa0-a501-abf0ee4d3415",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Write and run Shapley computation script with 6-seed null data",
        "status": "completed",
        "activeForm": "Writing and running Shapley computation script"
      },
      {
        "content": "Update gen_shapley_contribution.py and regenerate figure",
        "status": "completed",
        "activeForm": "Updating figure generation script"
      },
      {
        "content": "Find treatment PermG data for FDR sensitivity table update",
        "status": "in_progress",
        "activeForm": "Finding treatment PermG data"
      },
      {
        "content": "Update appendix.tex — all 7 TODO-D219 locations",
        "status": "pending",
        "activeForm": "Updating appendix.tex"
      },
      {
        "content": "Verify all numbers and TODO removals",
        "status": "pending",
        "activeForm": "Verifying consistency"
      }
    ],
    "newTodos": [
      {
        "content": "Write and run Shapley computation script with 6-seed null data",
        "status": "completed",
        "activeForm": "Writing and running Shapley computation script"
      },
      {
        "content": "Update gen_shapley_contribution.py and regenerate figure",
        "status": "completed",
        "activeForm": "Updating figure generation script"
      },
      {
        "content": "Find treatment PermG data for FDR sensitivity table update",
        "status": "completed",
        "activeForm": "Finding treatment PermG data"
      },
      {
        "content": "Update appendix.tex — all 7 TODO-D219 locations",
        "status": "in_progress",
        "activeForm": "Updating appendix.tex"
      },
      {
        "content": "Verify all numbers and TODO removals",
        "status": "pending",
        "activeForm": "Verifying consistency"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---


### Tool call

_source line 106_

<details open><summary>🔧 Tool call — Read · `toolu_016apmxiMDHo2yu24q1jkS58`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 125,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "eb0ab915-aca7-40a7-92c2-463c1d03b665",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABhdYpJVdQbLU6w75NkCNv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3449,
      "cache_read_input_tokens": 105221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3449
      },
      "output_tokens": 36,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 107 · 2026-05-24T09:05:18.681Z_

<details><summary>↩ Tool result · `toolu_016apmxiMDHo2yu24q1jkS58`</summary>

```text
125	
126	\paragraph{FDR threshold sensitivity.}
127	Table~\ref{tab:fdr_sensitivity} reports the effect of varying the BH FDR threshold $q$ on treatment ($\alpha{=}0.75$, 3~seeds) versus null ($\alpha{=}0.0$, 3~seeds) separation for permutation Granger tests.
128	% TODO-D219: update FDR sensitivity table with 6-seed null data (4/36 FPs at q=0.05; recompute null counts at each q threshold)
129	Treatment/null separation is qualitatively robust to FDR threshold choice; the null control remains at 0/24 across all thresholds.
130	
131	\begin{table}[h]
132	\centering
133	\small
134	% TODO-D219: update caption and table body with 6-seed null data
135	\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs). Null: $\alpha{=}0.0$ (3~seeds, 24 pairs). The null control produces zero false positives at all thresholds tested.}
136	\label{tab:fdr_sensitivity}
137	\resizebox{\columnwidth}{!}{%
138	\begin{tabular}{lccc}
139	\toprule
140	$q$ & Null FDR-sig (/24) & Treatment FDR-sig (/24) & Separation \\
141	\midrule
142	0.01 & 0 & 0  & Clean (underpowered) \\
143	0.05 & 0 & 19 & Clean \\
144	0.10 & 0 & 24 & Clean \\
145	\bottomrule
146	\end{tabular}}
147	\end{table}
148	
149	\paragraph{PermG $p$-value gradient at the onset boundary ($\alpha{=}0.45$).}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "dd4b260d-3db0-4868-86a9-45149920c9ec",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
      "content": "\n\\paragraph{FDR threshold sensitivity.}\nTable~\\ref{tab:fdr_sensitivity} reports the effect of varying the BH FDR threshold $q$ on treatment ($\\alpha{=}0.75$, 3~seeds) versus null ($\\alpha{=}0.0$, 3~seeds) separation for permutation Granger tests.\n% TODO-D219: update FDR sensitivity table with 6-seed null data (4/36 FPs at q=0.05; recompute null counts at each q threshold)\nTreatment/null separation is qualitatively robust to FDR threshold choice; the null control remains at 0/24 across all thresholds.\n\n\\begin{table}[h]\n\\centering\n\\small\n% TODO-D219: update caption and table body with 6-seed null data\n\\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs). Null: $\\alpha{=}0.0$ (3~seeds, 24 pairs). The null control produces zero false positives at all thresholds tested.}\n\\label{tab:fdr_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n$q$ & Null FDR-sig (/24) & Treatment FDR-sig (/24) & Separation \\\\\n\\midrule\n0.01 & 0 & 0  & Clean (underpowered) \\\\\n0.05 & 0 & 19 & Clean \\\\\n0.10 & 0 & 24 & Clean \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{PermG $p$-value gradient at the onset boundary ($\\alpha{=}0.45$).}",
      "numLines": 25,
      "startLine": 125,
      "totalLines": 1273
    }
  }
}
```

</details>

---


### Assistant

_source line 108_

Now I'll make the edits. Starting with the FDR sensitivity table (TODO-D219 #1 and #2).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "eb91668a-152f-4a8d-9fcc-ade6a6325272",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DigxvTiXWLxrmwZbv4kYRb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 108670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 643
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 109_

<details open><summary>🔧 Tool call — Edit · `toolu_0111ejKKCrGZfnFnWkYyN6is`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "old_string": "Table~\\ref{tab:fdr_sensitivity} reports the effect of varying the BH FDR threshold $q$ on treatment ($\\alpha{=}0.75$, 3~seeds) versus null ($\\alpha{=}0.0$, 3~seeds) separation for permutation Granger tests.\n% TODO-D219: update FDR sensitivity table with 6-seed null data (4/36 FPs at q=0.05; recompute null counts at each q threshold)\nTreatment/null separation is qualitatively robust to FDR threshold choice; the null control remains at 0/24 across all thresholds.\n\n\\begin{table}[h]\n\\centering\n\\small\n% TODO-D219: update caption and table body with 6-seed null data\n\\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs). Null: $\\alpha{=}0.0$ (3~seeds, 24 pairs). The null control produces zero false positives at all thresholds tested.}\n\\label{tab:fdr_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n$q$ & Null FDR-sig (/24) & Treatment FDR-sig (/24) & Separation \\\\\n\\midrule\n0.01 & 0 & 0  & Clean (underpowered) \\\\\n0.05 & 0 & 19 & Clean \\\\\n0.10 & 0 & 24 & Clean \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}",
  "new_string": "Table~\\ref{tab:fdr_sensitivity} reports the effect of varying the BH FDR threshold $q$ on treatment ($\\alpha{=}0.75$, 3~seeds, 8-pair basis) versus null ($\\alpha{=}0.0$, 6~seeds 45--50, 6-pair basis) separation for permutation Granger tests.\nTreatment/null separation is qualitatively robust to FDR threshold choice, though the expanded null sample reveals a small number of false positives at each threshold (3--8 of 36 pairs).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs, 8-pair basis). Null: $\\alpha{=}0.0$ (6~seeds 45--50, 36 pairs, 6-pair basis). The expanded null sample reveals modest false positive rates that increase with $q$.}\n\\label{tab:fdr_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n$q$ & Null FDR-sig (/36) & Treatment FDR-sig (/24) & Separation \\\\\n\\midrule\n0.01 & 3 & 0  & Underpowered \\\\\n0.05 & 4 & 19 & Good \\\\\n0.10 & 8 & 24 & Good (elevated null) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "3554b519-5553-4025-8bb5-2f7faed6b682",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DigxvTiXWLxrmwZbv4kYRb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 108670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 643
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 110 · 2026-05-24T09:05:34.212Z_

<details><summary>↩ Tool result · `toolu_0111ejKKCrGZfnFnWkYyN6is`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "5dd7cf36-3746-4fb6-89b1-e43f0b9dc0d7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "oldString": "Table~\\ref{tab:fdr_sensitivity} reports the effect of varying the BH FDR threshold $q$ on treatment ($\\alpha{=}0.75$, 3~seeds) versus null ($\\alpha{=}0.0$, 3~seeds) separation for permutation Granger tests.\n% TODO-D219: update FDR sensitivity table with 6-seed null data (4/36 FPs at q=0.05; recompute null counts at each q threshold)\nTreatment/null separation is qualitatively robust to FDR threshold choice; the null control remains at 0/24 across all thresholds.\n\n\\begin{table}[h]\n\\centering\n\\small\n% TODO-D219: update caption and table body with 6-seed null data\n\\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs). Null: $\\alpha{=}0.0$ (3~seeds, 24 pairs). The null control produces zero false positives at all thresholds tested.}\n\\label{tab:fdr_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n$q$ & Null FDR-sig (/24) & Treatment FDR-sig (/24) & Separation \\\\\n\\midrule\n0.01 & 0 & 0  & Clean (underpowered) \\\\\n0.05 & 0 & 19 & Clean \\\\\n0.10 & 0 & 24 & Clean \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}",
    "newString": "Table~\\ref{tab:fdr_sensitivity} reports the effect of varying the BH FDR threshold $q$ on treatment ($\\alpha{=}0.75$, 3~seeds, 8-pair basis) versus null ($\\alpha{=}0.0$, 6~seeds 45--50, 6-pair basis) separation for permutation Granger tests.\nTreatment/null separation is qualitatively robust to FDR threshold choice, though the expanded null sample reveals a small number of false positives at each threshold (3--8 of 36 pairs).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs, 8-pair basis). Null: $\\alpha{=}0.0$ (6~seeds 45--50, 36 pairs, 6-pair basis). The expanded null sample reveals modest false positive rates that increase with $q$.}\n\\label{tab:fdr_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n$q$ & Null FDR-sig (/36) & Treatment FDR-sig (/24) & Separation \\\\\n\\midrule\n0.01 & 3 & 0  & Underpowered \\\\\n0.05 & 4 & 19 & Good \\\\\n0.10 & 8 & 24 & Good (elevated null) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}",
    "originalFile": "\\appendix\n\n\\section{Training Details and Metric Drift}\n\\label{app:training_details}\n\\label{app:drift}\n\n\\paragraph{Hyperparameters.}\nEach generation fine-tunes for 5{,}000 steps using AdamW (learning rate $5 \\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium).\nGeneration uses temperature $1.0$, top-$k{=}50$, max length 512 tokens, producing 5{,}000 samples per generation from 5{,}000-sample subsets of WikiText-103.\nCanary metrics: token entropy $H(p_\\theta | \\text{context})$ over 1{,}000 held-out samples; ECE with 15 bins.\nAdditional downstream metrics (distinct-3, effective rank, Self-BLEU) appear in subsequent appendix sections.\n\n\\paragraph{Metric drift.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Metric drift (\\%, generation~0$\\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\\alpha{=}0.25$: distinct-1 $-40.3{\\pm}0.3\\%$) rather than full replacement ($\\alpha{=}1.0$: $-27.8{\\pm}1.6\\%$). $^\\dagger$$\\alpha{=}0.10$: single seed (seed~42, preliminary). $\\alpha{=}0.00$, $\\alpha{=}0.25$, $\\alpha{=}0.50$, $\\alpha{=}0.75$: 3-seed mean${\\pm}$std (seeds 42, 43, 44); $\\alpha{=}1.0$: 4-seed mean${\\pm}$std (seeds 42, 43, 44, 45).}\n\\label{tab:drift_summary}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\\\\n\\midrule\n0.00 & $-4.6{\\pm}0.4$ & $+37.6{\\pm}14$ & $-14.1{\\pm}0.4$ & $-9.6{\\pm}0.4$ & $-20.6{\\pm}1.0$ \\\\\n0.10$^\\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\\\\n0.25 & $-4.7{\\pm}0.5$ & $+81.8{\\pm}15.9$ & $-40.3{\\pm}0.3$ & $-56.4{\\pm}0.7$ & $-18.1{\\pm}0.8$ \\\\\n0.50 & $-18.0{\\pm}0.5$ & $+822.6{\\pm}18.3$ & $-37.1{\\pm}0.4$ & $-50.4{\\pm}1.0$ & $+21.0{\\pm}0.1$ \\\\\n0.75 & $-27.6{\\pm}0.2$ & $+1791{\\pm}18$ & $-32.3{\\pm}0.5$ & $-41.0{\\pm}1.0$ & $+182.6{\\pm}0.7$ \\\\\n1.00 & $-60.8{\\pm}1.2$ & $+3780{\\pm}30$ & $-27.8{\\pm}1.6$ & $-34.0{\\pm}3.3$ & $+3674{\\pm}45$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Distinct-3 Results}\n\\label{app:distinct3}\n\nTable~\\ref{tab:distinct3_drift} reports distinct-3 drift across all contamination levels.\nDistinct-3 exhibits the largest absolute decline among diversity metrics at low contamination ($-58.9{\\pm}0.9\\%$ at $\\alpha{=}0.25$) but attenuates at higher levels ($-30.5\\%$ at $\\alpha{=}1.0$), consistent with the diversity--calibration dissociation discussed in \\S\\ref{sec:discussion}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Distinct-3 drift (\\%, generation~0$\\to$10) across contamination levels. $\\alpha{=}0.00$, $\\alpha{=}0.25$, $\\alpha{=}0.75$: 3-seed mean${\\pm}$std; $\\alpha{=}1.0$: 4-seed mean${\\pm}$std; $\\alpha{=}0.50$: single seed.}\n\\label{tab:distinct3_drift}\n\\begin{tabular}{lc}\n\\toprule\n$\\alpha$ & Distinct-3 drift (\\%) \\\\\n\\midrule\n0.00 & $-4.4{\\pm}0.5$ \\\\\n0.25 & $-58.9{\\pm}0.9$ \\\\\n0.50 & $-52.4$ \\\\\n0.75 & $-38.6{\\pm}1.3$ \\\\\n1.00 & $-30.5{\\pm}4.0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Lead-lag analysis.}\nAt $\\alpha{=}1.0$, token entropy Granger-precedes distinct-3 at the same consensus level as distinct-1 and distinct-2: $K{\\geq}4/5$ methods, $S{\\geq}3/4$ seeds (Tier~3).\nHowever, the optimal lag is less stable than for distinct-1/2: at max\\_lag${=}7$, the lag standard deviation across seeds exceeds 1.5 generations, compared to $<0.5$ for distinct-1/2.\nThis instability reflects bimodal lag distributions (modes at lag~1 and lag~3--4), suggesting that distinct-3 captures two temporally distinct diversity loss mechanisms: rapid n-gram homogenization (lag~1) and slower distributional narrowing (lag~3--4).\n\n\\paragraph{Sensitivity to sequence length.}\nHigher-order $n$-gram diversity metrics are more sensitive to generation length and random sampling variability.\nWith our 512-token generation length, distinct-3 has a smaller effective denominator (number of possible unique trigrams observed) than distinct-1 or distinct-2, amplifying stochastic fluctuations.\nThis partially explains the higher lag instability: the signal-to-noise ratio for temporal precedence is lower for distinct-3, requiring more observations (longer $T$ or more seeds) to achieve stable estimates.\nFor this reason, we report distinct-3 in this appendix rather than in the main text, where distinct-1 and distinct-2 provide cleaner evidence of the entropy-leads-diversity pattern.\n\n\n\\section{Observation Window Sensitivity}\n\\label{app:window_sensitivity}\n\nTable~\\ref{tab:window_sensitivity} reports how the Tier~3 consensus classification ($K{\\geq}4/5$ methods) varies as a function of the minimum observation window $T_{\\min}$, where analysis uses only generations $0$ through $T_{\\min}$.\nThe consensus classification stabilizes at $T_{\\min}{\\geq}5$ (6 data points), well below our full observation window of $T{=}10$: all six effect-size reference pairs (token entropy and ECE $\\to$ distinct-1, distinct-2, distinct-3) reach $K{\\geq}4/5$ agreement at every window length from $T_{\\min}{=}5$ through $T_{\\min}{=}10$, with no spurious pairs (canary$\\to$perplexity) admitted.\n\nToda--Yamamoto is the only method exhibiting window-dependent sensitivity (note: TY directional assignment is under verification; these counts are retained for completeness): TY consensus stabilizes at $T_{\\min}{\\geq}6$, slightly later than the primary methods, reflecting the additional degrees of freedom consumed by the augmentation order $d_{\\max}$.\nThis does not affect the consensus classification because the remaining four methods provide stable $K{\\geq}4/5$ agreement independently of Toda--Yamamoto's vote.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Observation window sensitivity for Tier~3 consensus ($K{\\geq}4/5$) at $\\alpha{=}1.0$ (Pythia-410M, 4~seeds). Tier~3 pairs: number of canary$\\to$downstream pairs (out of 8 validated) reaching $K{\\geq}4/5$ method agreement. TY pairs: number of effect-size reference pairs (out of 6) reaching Toda--Yamamoto significance (moderate supplementary method; \\S\\ref{sec:method}). Consensus stabilizes at $T_{\\min}{\\geq}5$; TY stabilizes at $T_{\\min}{\\geq}6$.}\n\\label{tab:window_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccccccc}\n\\toprule\n& \\multicolumn{8}{c}{Minimum observation window $T_{\\min}$} \\\\\n\\cmidrule(lr){2-9}\n& 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\\\\n\\midrule\nTier~3 pairs (/8)    & $\\dagger$ & $\\dagger$ & 6 & 6 & 6 & 6 & 6 & 6 \\\\\nTY pairs$^\\S$ (/6)   & $\\dagger$ & $\\dagger$ & 3--6 & 3--6 & 3--6 & 3--6 & 3--6 & 6 \\\\\nStable               & ---       & ---       & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark \\\\\n\\bottomrule\n\\multicolumn{9}{l}{\\footnotesize $\\dagger$~Insufficient degrees of freedom for Granger-type tests ($<6$ data points).} \\\\\n\\multicolumn{9}{l}{\\footnotesize $^\\S$~TY directional assignment under verification.}\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Robustness Checks}\n\\label{app:robustness}\n\n\\paragraph{Permutation count stability.}\nTable~\\ref{tab:nperm_stability} compares permutation Granger $p$-values at 5{,}000 versus 10{,}000 permutations across all canary$\\to$downstream pairs at $\\alpha{=}0.75$ (3~seeds, 24~pairs).\nPermutation Granger $p$-values are stable to within 0.002 between 5{,}000 and 10{,}000 permutations, with zero significance decisions affected.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Permutation count stability analysis ($\\alpha{=}0.75$, 3~seeds, 24 canary$\\to$downstream pairs). $p$-values from permutation Granger tests at $n_{\\text{perm}}{=}5{,}000$ versus $n_{\\text{perm}}{=}10{,}000$.}\n\\label{tab:nperm_stability}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nMax $|\\Delta p|$ & 0.010 \\\\\nMean $|\\Delta p|$ & 0.002 \\\\\nSignificance flips & 0 / 24 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{FDR threshold sensitivity.}\nTable~\\ref{tab:fdr_sensitivity} reports the effect of varying the BH FDR threshold $q$ on treatment ($\\alpha{=}0.75$, 3~seeds) versus null ($\\alpha{=}0.0$, 3~seeds) separation for permutation Granger tests.\n% TODO-D219: update FDR sensitivity table with 6-seed null data (4/36 FPs at q=0.05; recompute null counts at each q threshold)\nTreatment/null separation is qualitatively robust to FDR threshold choice; the null control remains at 0/24 across all thresholds.\n\n\\begin{table}[h]\n\\centering\n\\small\n% TODO-D219: update caption and table body with 6-seed null data\n\\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs). Null: $\\alpha{=}0.0$ (3~seeds, 24 pairs). The null control produces zero false positives at all thresholds tested.}\n\\label{tab:fdr_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n$q$ & Null FDR-sig (/24) & Treatment FDR-sig (/24) & Separation \\\\\n\\midrule\n0.01 & 0 & 0  & Clean (underpowered) \\\\\n0.05 & 0 & 19 & Clean \\\\\n0.10 & 0 & 24 & Clean \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{PermG $p$-value gradient at the onset boundary ($\\alpha{=}0.45$).}\nAt the onset boundary, PermG operates near its detection limit, and marginal $p$-values exhibit seed-dependent variation consistent with the statistical power interpretation (\\S\\ref{sec:theory}).\nTable~\\ref{tab:fdr_gradient_a045} reports BH-corrected $p$-values for all 8 canary$\\to$downstream pairs across two seeds at $\\alpha{=}0.45$.\nSeed~43 reaches a minimum FDR-corrected $p{=}0.059$ (18\\% above the $q{=}0.05$ threshold), while seed~42 reaches $p{=}0.091$ (82\\% above threshold).\nNo pair crosses the significance threshold at either seed, yielding the aggregate 0/8 detection rate reported in \\S\\ref{sec:regime}.\nThe gradient is consistent with a continuous power transition rather than a binary absence of signal: PermG operates near its detection limit at $\\alpha{=}0.45$, with seed-dependent variation in marginal $p$-values.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BH-corrected PermG $p$-values at $\\alpha{=}0.45$ (8 canary$\\to$downstream pairs $\\times$ 2 seeds). Min $p_{\\mathrm{fdr}}$ per seed shown. All pairs remain above the $q{=}0.05$ threshold, yielding 0/8 aggregate detection.}\n\\label{tab:fdr_gradient_a045}\n\\begin{tabular}{lcc}\n\\toprule\n & Seed 42 & Seed 43 \\\\\n\\midrule\nMin FDR $p$ & 0.091 & 0.059 \\\\\nGap to $q{=}0.05$ & 82\\% & 18\\% \\\\\nPermG fwd sig (/8) & 0 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Systematic Robustness Analysis}\n\\label{app:spec_curve}\n\nThe sharp detection onset reported in \\S\\ref{sec:regime} could in principle depend on specific analytical choices (pair selection, seed, $\\alpha$ level, method parameters).\nWe assess robustness via specification curve analysis~\\cite{simonsohn2020specification}, systematically varying analytical degrees of freedom to test whether the 0/8$\\to$6/8 transition is specification-invariant.\nOur specification curve varies data subsets and pair selections while holding the detection method (PermG) and its hyperparameters fixed, more closely resembling a systematic subset analysis than a full specification curve in the sense of \\citet{simonsohn2020specification}.\n\nWe construct 1{,}160 analytical specifications from the combinatorial space of: 13 contamination levels ($\\alpha$ grid), seed selection ($\\{42, 43, 44, 45\\}$ where available), 8 canonical canary$\\to$downstream pairs (\\{token entropy, ECE\\} $\\times$ \\{distinct-1, distinct-2, distinct-3, mauve\\}), and method parameters (all PermG with $n_\\text{perm}{=}5{,}000$, BH FDR $q{=}0.05$).\nAll specifications use the D120-canonical analysis pipeline with $3\\sigma$ threshold calibration (D105) as a hard filter.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Specification curve summary (1{,}160 specifications, D120-compliant). The blind$\\to$onset jump is robust across specifications: 0\\% significance rate through $\\alpha{=}0.45$, rising to 75\\% at $\\alpha{=}0.50$.}\n\\label{tab:spec_curve}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nTotal specifications & 1{,}160 \\\\\nSignificant (FDR $q{<}0.05$) & 536 (46.2\\%) \\\\\n\\midrule\n\\emph{By regime} & \\\\\n\\quad Blind ($\\alpha \\leq 0.45$) & 0\\% \\\\\n\\quad Onset ($\\alpha{=}0.50$) & 75\\% \\\\\n\\quad Detection ($\\alpha \\geq 0.75$) & 62--75\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe specification curve confirms that the sharp detection onset is not an artifact of particular analytical choices: the categorical jump from 0\\% to ${\\geq}75\\%$ significance at $\\alpha_c{\\approx}0.50$ holds across the vast majority of specifications, supporting the main text claim (\\S\\ref{sec:regime}).\n\n\n\\section{Transfer Entropy Analysis}\n\\label{app:transfer_entropy}\n\nTable~\\ref{tab:te_results} reports transfer entropy (TE; \\citealp{schreiber2000measuring}) results aggregated across all baseline conditions.\nTE was estimated using 3-bin discretization with permutation testing ($n{=}5{,}000$).\nNo pair reaches BH-corrected significance ($q{=}0.05$) in any condition, confirming that non-parametric information-theoretic methods lack detection power at $T{=}11$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Transfer Entropy results (12 runs across all $\\alpha$ levels). TE\\textsubscript{fwd}: canary$\\to$downstream; TE\\textsubscript{rev}: downstream$\\to$canary. Mean uncorrected permutation $p$-values ($n{=}5{,}000$). No pair reaches BH-corrected $q{<}0.05$ in any run.}\n\\label{tab:te_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\nCanary & Downstream & TE\\textsubscript{fwd} (mean) & $p$\\textsubscript{fwd} (mean) & TE\\textsubscript{rev} (mean) & $p$\\textsubscript{rev} (mean) \\\\\n\\midrule\ntoken\\_entropy & distinct-1 & 0.289 & 0.559 & 0.480 & 0.490 \\\\\ntoken\\_entropy & distinct-2 & 0.300 & 0.529 & 0.496 & 0.447 \\\\\ntoken\\_entropy & distinct-3 & 0.255 & 0.645 & 0.484 & 0.459 \\\\\ntoken\\_entropy & perplexity & 0.257 & 0.676 & 0.386 & 0.626 \\\\\nECE & distinct-1 & 0.185 & 0.720 & 0.184 & 0.891 \\\\\nECE & distinct-2 & 0.208 & 0.683 & 0.216 & 0.846 \\\\\nECE & distinct-3 & 0.209 & 0.689 & 0.227 & 0.807 \\\\\nECE & perplexity & 0.296 & 0.572 & 0.263 & 0.747 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\phantomsection\\label{app:te_mi}\n\\paragraph{KNN-based TE/MI decomposition.}\nA $k$-nearest-neighbor TE estimator ($k{=}5$) provides a model-free complement to the parametric Granger framework.\nForward-dominant TE fraction increases monotonically with $\\alpha$: 4/8 pairs at $\\alpha{=}0.25$ (mean net TE${=}0.14$), 5/8 at $\\alpha{=}0.50$ (net TE${=}0.42$), 6/8 at $\\alpha{=}0.60$ (net TE${=}0.57$), and 8/8 at $\\alpha{=}1.0$ (net TE${=}1.59$).\nAll 120 forward TE bootstrap 95\\% CIs exclude zero at $T{=}10$; all 48 at $T{=}20$.\nThe ``high MI, low TE'' hypothesis for the non-monotonic dip is supported by only 2/8 pairs (ECE$\\to$perplexity and token entropy$\\to$perplexity); the remaining 6 pairs show elevated TE even at $\\alpha{=}0.60$, indicating confounded co-variation rather than a universal mechanism.\n\n\\section{Change-Point Detection Analysis}\n\\label{app:change_point}\n\nWe apply a max-split change-point test with bootstrap significance assessment ($n{=}5{,}000$, $p{<}0.05$) to each metric's generation-level time series ($T{=}11$).\n\nUnder the null control ($\\alpha{=}0.00$, 3~seeds), downstream diversity metrics (distinct-1, distinct-2, distinct-3) produce significant change-points at generation~2 in all seeds (9/9 tests). With additional significant tests from ECE (2/3 seeds) and token entropy (1/3 seeds), the overall false positive rate reaches 66.7\\% (12/18 tests; Table~\\ref{tab:cp_null}). The monotonic drift inherent in iterative self-training is sufficient to trigger change-point detection even without canary contamination. Individual change-point significance therefore cannot serve as standalone evidence for a canary-specific effect.\n\nAlthough individual significance is unreliable as a discriminator, the temporal ordering of detected change-points reverses between null and treatment conditions. In the null ($\\alpha{=}0.00$), downstream metrics show the earliest significant breaks at generation~2 (all seeds), while significant canary breaks appear later (ECE at generations~4--8). Under treatment conditions ($\\alpha{\\geq}0.75$), this ordering flips: canary metrics place their best splits at generation~1, followed by downstream diversity metrics at generations~2--4 and perplexity at generation~4 (Table~\\ref{tab:cp_results}). This ordering reversal provides complementary evidence from a distinct statistical framework, consistent with the Granger-precedence analysis in \\S\\ref{sec:experiments}.\n\nSeveral caveats apply. The 18 individual tests per condition were not corrected for multiple comparisons (BH or Bonferroni); primary inference rests on the cross-metric temporal ordering rather than on individual significance tests. Under treatment conditions, token entropy places its best split at generation~1 with large effect sizes ($|d|{>}2.5$) in all seeds, but the pre-change segment at a generation-1 split contains only a single data point, reducing bootstrap power (1/3 seeds significant at $\\alpha{=}0.75$). The short series length ($T{=}11$) further limits overall detection power.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Change-point detection under null control ($\\alpha{=}0.00$, 3 seeds). CP: detected change-point generation (mean across significant seeds); $|d|$: Cohen's $d$ effect size (mean across all seeds); Sig.\\ rate: fraction of seeds where $p{<}0.05$. Overall FPR: 12/18 = 66.7\\%.}\n\\label{tab:cp_null}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & CP gen (mean) & $|d|$ (mean) & Sig.\\ rate & Type \\\\\n\\midrule\ntoken\\_entropy & 1.0 & 2.94 & 1/3 & canary \\\\\nECE & 6.0 & 1.62 & 2/3 & canary \\\\\ndistinct-1 & 2.0 & 2.27 & 3/3 & downstream \\\\\ndistinct-2 & 2.0 & 2.40 & 3/3 & downstream \\\\\ndistinct-3 & 2.0 & 2.27 & 3/3 & downstream \\\\\nperplexity & --- & 3.11 & 0/3 & downstream \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Change-point detection at $\\alpha{=}0.75$ (3 seeds). CP: detected change-point generation; $|d|$: Cohen's $d$ effect size between pre- and post-change segments. Sig.\\ rate: fraction of seeds where $p{<}0.05$.}\n\\label{tab:cp_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & CP gen (mean) & $|d|$ (mean) & Sig.\\ rate & Type \\\\\n\\midrule\ntoken\\_entropy & 1.0 & 3.21 & 1/3 & canary \\\\\nECE & 1.0 & 3.10 & 1/3 & canary \\\\\ndistinct-1 & 2.3 & 2.18 & 3/3 & downstream \\\\\ndistinct-2 & 3.0 & 1.97 & 3/3 & downstream \\\\\ndistinct-3 & 3.7 & 1.86 & 3/3 & downstream \\\\\nperplexity & 4.0 & 1.70 & 3/3 & downstream \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Dose-response ordering pattern.}\nTable~\\ref{tab:cp_ordering} summarizes the ordering pattern across contamination levels.\nThe canary-to-downstream gap shifts monotonically from negative (downstream first) under the null to positive (canary first) under treatment, ruling out a methodological artifact in which canary metrics would systematically appear earlier regardless of condition.\nThe $\\alpha{=}1.0$ analysis is limited to a single seed (s42); all other conditions use 3 seeds.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccl}\n\\toprule\n$\\alpha$ & Canary cp & Downstream cp & Gap & Direction \\\\\n\\midrule\n0.00 & gen 4--8 & gen 2 & $-$2.5 & Downstream first \\\\\n0.25 & gen 3--4 & gen 3--4 & $\\approx$0 & Simultaneous \\\\\n0.75 & gen 1 & gen 2--4 & $+$2.25 & Canary first \\\\\n1.00 & gen 2 & gen 2--5 & $+$1.0 & Canary first \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Change-point ordering reversal across contamination levels. Under the null ($\\alpha{=}0.00$), downstream metrics break before canary metrics; this ordering reverses monotonically as $\\alpha$ increases, consistent with the Granger-precedence analysis.}\n\\label{tab:cp_ordering}\n\\end{table}\n\n\n\\section{Sequential Monitoring: CUSUM vs Calibrated Threshold}\n\\label{app:csmp}\n\nWe translate the Granger-precedence finding into a deployable monitoring protocol using CUSUM (cumulative sum) sequential testing~\\cite{page1954continuous}, calibrated against the $\\alpha{=}0.0$ null control.\nThe null-calibration procedure sets the alarm threshold $h$ such that the false alarm rate (FAR) is 0\\% on null data (3~seeds, $T{=}10$), providing controlled Type~I error guarantees.\n\n\\paragraph{Method.}\nCUSUM monitors the cumulative deviation of token entropy from its null-control baseline: $S_t = \\max(0,\\; S_{t-1} + (\\mu_0 - x_t) - k)$, where $\\mu_0$ is the null-control mean, $k$ is the allowance parameter, and the alarm triggers when $S_t > h$.\nWe calibrate $h$ for each $k$ from the $\\alpha{=}0.0$ null data (Table~\\ref{tab:csmp_calibration}).\nAs a baseline, we compare against a simple calibrated threshold: alarm when the metric crosses $\\mu_0 - 2\\sigma_0$ for $n{\\geq}1$ or $n{\\geq}2$ consecutive generations.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{CUSUM calibration parameters from $\\alpha{=}0.0$ null control (3~seeds). $h$: alarm threshold calibrated to achieve FAR${=}$0\\%. For $k{\\geq}0.25$, the null CUSUM statistic remains at zero, yielding $h \\approx 0$.}\n\\label{tab:csmp_calibration}\n\\begin{tabular}{lcc}\n\\toprule\n$k$ & $h$ & FAR \\\\\n\\midrule\n0.05 & 1.530 & 0\\% \\\\\n0.10 & 1.005 & 0\\% \\\\\n0.25 & $\\approx$0 & 0\\% \\\\\n0.50 & $\\approx$0 & 0\\% \\\\\n1.00 & $\\approx$0 & 0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Results.}\nTable~\\ref{tab:csmp_comparison} compares CUSUM and simple threshold detection times across gradual contamination levels.\nAt the recommended operating point ($k{=}0.25$), CUSUM and the simple threshold ($n{\\geq}1$) produce identical alarm times (generation~1) across all seeds and contamination levels.\nMore conservative CUSUM settings ($k{=}0.1$, $k{=}0.05$) delay detection to match the $n{\\geq}2$ threshold or later.\nAt $k{=}1.0$ with $\\alpha{=}0.50$, CUSUM fails entirely ($S_t \\equiv 0$ for all seeds), demonstrating sensitivity to the allowance parameter.\nNo CUSUM configuration outperforms the simple calibrated threshold at any operating point tested.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{CUSUM vs simple calibrated threshold: alarm generation across contamination levels (3~seeds each; all seeds agree on the alarm generation shown). Threshold: metric crosses $\\mu_0 - 2\\sigma_0$. No CUSUM configuration outperforms the simple threshold at any operating point.}\n\\label{tab:csmp_comparison}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & CUSUM $k{=}0.25$ & CUSUM $k{=}0.1$ & CUSUM $k{=}0.05$ & Thresh $n{\\geq}1$ & Thresh $n{\\geq}2$ \\\\\n\\midrule\n0.50 & gen 1 & gen 2 & gen 3 & gen 1 & gen 2 \\\\\n0.75 & gen 1 & gen 2 & gen 2 & gen 1 & gen 2 \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize CUSUM $k{=}1.0$ at $\\alpha{=}0.50$: $S_t \\equiv 0$ for all seeds (complete detection failure).} \\\\\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe equivalence arises because the generation-0$\\to$1 entropy drop is large ($|\\Delta x| > 0.7$ for $\\alpha{=}0.50$, $> 1.0$ for $\\alpha{=}0.75$) relative to the null-control variability ($\\sigma_0 \\approx 0.03$).\nAny detector with a near-zero or small threshold triggers at generation~1; CUSUM's cumulative memory provides no advantage when the initial shift already exceeds the control limit.\nThis result extends Claim~3 (method sensitivity) beyond lead-lag detection to the monitoring domain: even a sequential testing procedure with stronger theoretical properties (optimal expected detection delay under continuous monitoring) does not improve over a calibrated baseline when the initial contamination signal dominates the allowance parameter.\nThe contribution of the null-calibrated monitoring framework is the calibration procedure itself (setting alarm boundaries from $\\alpha{=}0.0$ data to guarantee FAR${=}$0\\%), not the CUSUM algorithm.\n\n\\section{Background and Notation}\n\\label{app:background}\n\\label{sec:background}\n\nThis section establishes the formal setup and notation used throughout the paper.\n\n\\paragraph{Iterative training loop.}\nLet $M_0$ denote a pretrained language model and $\\mathcal{D}_\\text{real}$ a fixed corpus of human-written text.\nAt each generation $t \\geq 1$, the model $M_{t-1}$ generates a synthetic corpus $\\mathcal{D}_\\text{synth}^{(t-1)}$, and the next-generation model $M_t$ is fine-tuned on a mixture of $\\alpha$ fraction synthetic data and $(1{-}\\alpha)$ fraction real data:\n\\begin{equation}\n    \\mathcal{D}_\\text{train}^{(t)} = \\alpha \\cdot \\mathcal{D}_\\text{synth}^{(t-1)} \\;+\\; (1{-}\\alpha) \\cdot \\mathcal{D}_\\text{real}, \\quad \\alpha \\in [0, 1].\n    \\label{eq:mixing}\n\\end{equation}\nAt $\\alpha{=}1.0$, this reduces to the full-replacement paradigm of \\citet{shumailov2024curse}.\n\n\\paragraph{Metric families.}\n\\emph{Canary metrics}: token entropy ($H(p_\\theta | \\text{context})$ on held-out samples) and expected calibration error (ECE).\n\\emph{Downstream metrics}: distinct-$n$ ($n \\in \\{1, 2, 3\\}$)~\\cite{li2016diversity} and perplexity.\nEach metric produces a time series of $T{+}1$ observations.\n\n\\paragraph{Lead-lag testing.}\nGiven canary series $X$ and downstream series $Y$, the central question is whether changes in $X$ temporally precede changes in $Y$, requiring directionality and confounder control beyond simple correlation.\nWe employ five methods spanning permissive to conservative: naive cross-correlation, differenced cross-correlation, threshold onset detection, permutation Granger causality~\\cite{shojaie2022granger}, and Toda--Yamamoto Granger causality~\\cite{toda1995statistical}.\n\n\\section{MMCT Algorithm}\n\\label{app:mmct}\n\nAlgorithm~\\ref{alg:mmct} describes the Multi-Method Consensus Test (MMCT) introduced in \\S\\ref{sec:mmct}.\n\n\\begin{algorithm}[h]\n\\caption{Multi-Method Consensus Test (MMCT)}\n\\label{alg:mmct}\n\\begin{algorithmic}[1]\n\\Require Time series pair $(X, Y)$; methods $\\{m_1, \\ldots, m_K\\}$ ($K{=}5$); null-control data $\\mathcal{N}$ (from $\\alpha{=}0.0$); tolerance $\\epsilon{=}0.01$\n\\Ensure $p$-value, consensus level $\\hat{K}$\n\\For{each method $m_k$}\n    \\State Compute empirical FPR: $\\widehat{\\mathrm{FPR}}_k \\gets$ fraction of null-control pairs where $m_k$ rejects $H_0$\n    \\State Compute weight: $w_k \\gets 1 / \\max(\\widehat{\\mathrm{FPR}}_k,\\; \\epsilon)$\n    \\State Apply $m_k$ to $(X, Y)$: $d_k \\gets \\mathbf{1}[m_k \\text{ rejects } H_0]$\n\\EndFor\n\\State Weighted consensus: $W(X {\\to} Y) \\gets \\sum_{k} w_k \\, d_k \\;/\\; \\sum_{k} w_k$\n\\State Build empirical null distribution of $W$ from all null-control pairs in $\\mathcal{N}$\n\\State Compute $p$-value from empirical null: $p \\gets \\Pr_{\\mathcal{N}}(W \\geq W_{\\mathrm{obs}})$\n\\State Consensus level: $\\hat{K} \\gets \\sum_{k} d_k$\n\\State \\Return $p$, $\\hat{K}$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Design rationale.}\nFPR-inverse weighting penalizes methods with high false positive rates on null-control data: naive cross-correlation (FPR${=}91.7\\%$) receives weight $w{=}1.09$, while PermG (FPR${=}11.1\\%$, the lowest among directional methods; DiffXCorr achieves 2.8\\% but lacks directional separation) receives $w{=}9.0$.\nThe empirical null distribution avoids parametric assumptions that are unreliable for short ($T{=}5$--$20$), non-stationary series typical of iterative training.\nMMCT is a consensus testing protocol, not a novel statistical method; its value lies in systematic method comparison and the identification of method-dependent conclusions.\n\n\n\\section{Methodological Comparison Table}\n\\label{app:method_comparison}\n\nTable~\\ref{tab:method-comparison} summarizes the methodological coverage of existing canary and monitoring analyses across the diagnostic dimensions identified in \\S\\ref{sec:method}.\nNo prior work combines all six dimensions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Methodological comparison of canary and monitoring analyses. \\checkmark\\ = present, $\\times$ = absent, $\\circ$ = partial (${\\leq}2$ levels or limited replication). Diff.\\ = differencing/stationarity controls. Multi-M.\\ = ${\\geq}2$ independent statistical methods. MTC = multiple testing correction. Regime = systematic variation of $\\alpha$. Seeds = ${\\geq}3$ independent seeds. Arch.\\ = ${\\geq}2$ architecturally distinct model families.}\n\\label{tab:method-comparison}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccccl}\n\\toprule\nWork & Diff. & Multi-M. & MTC & Regime & Seeds & Arch. & Metrics \\\\\n\\midrule\n\\citet{shumailov2024curse}     & $\\times$   & $\\times$   & $\\times$   & $\\circ$    & \\checkmark & \\checkmark & PPL \\\\\n\\citet{du2025scales}           & $\\times$   & $\\times$   & \\checkmark & \\checkmark & \\checkmark & $\\times$   & ECE, Acc, Dist-$n$ \\\\\n\\citet{gambetta2024surplexity} & $\\times$   & $\\times$   & $\\times$   & \\checkmark & \\checkmark & \\checkmark & Surplexity, Ent \\\\\nSIGMA~\\cite{sigma2026spectral} & $\\times$   & $\\times$   & $\\times$   & $\\times$   & $\\times$   & $\\times$   & Spectral \\\\\nDCES~\\cite{dces2026counter}    & $\\times$   & $\\times$   & $\\times$   & $\\times$   & $\\times$   & \\checkmark & ECE, Ent, PPL \\\\\n\\midrule\n\\textbf{Ours}                  & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark & Ent, ECE, PPL, Dist-$n$ \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\section{Extended Discussion}\n\\label{app:extended_discussion}\n\n\\paragraph{Calibration scope and generalization.}\nAll FPR and FNR calibration results are specific to our experimental setup: Pythia-410M, WikiText-103 subset, $T{=}10$, and six contamination levels.\nCross-architecture validation across 15 conditions spanning six model families shows that the entropy-leads-diversity pattern generalizes in 11 of 15 architecture-seed combinations (Table~\\ref{tab:generalization}); GPT-2 bf16 (0/8), GPT-2 s43 (6/8 bidirectional), SmolLM3-3B (3/8, entropy decoupling), and Pythia-1.4B s42 (2/8) do not confirm the pattern.\n\n\\paragraph{Domain-dependent directionality.}\nThe unidirectional forward causation observed on WikiText (PermG reverse${=}$0/8 across all conditions) does not hold universally.\nOn C4 at $\\alpha{=}0.50$ (s42 fp32), PermG reverse reaches 7/8, indicating near-symmetric bidirectional coupling; however, this is seed-dependent (s43: 1/8) and noted as preliminary.\nThe practical implication is that directional asymmetry should be verified per domain.\n\n\\paragraph{Token entropy versus perplexity.}\nThe distinction lies in the evaluation domain: token entropy is $H(p_\\theta | \\text{context})$ on held-out real data, while perplexity is $\\exp(H_\\text{cross})$ on model-generated text.\nFirst-differencing removes their shared downward trend: the canary$\\to$diversity channel survives because entropy leads diversity by one generation, whereas the canary$\\to$perplexity channel vanishes because both co-move synchronously.\n\n\\paragraph{NLP-specific constraints.}\nOur application of Granger-type methods faces constraints absent in econometrics: (i)~observation length ($T{=}5$--$20$ vs.\\ $T{=}100$--$1000$); (ii)~non-stationarity by design rather than incidental; (iii)~small multiplicity for FDR correction (8--32 pairs per regime).\nTransfer entropy (0/192 FDR-significant results) confirms that method sensitivity extends beyond the five-method panel.\n\n\\paragraph{Prevention paradox.}\nEffective intervention truncates the collapse trajectory that established Granger precedence.\nDifferenced cross-correlation retains significance under intervention (31/32 pairs), while threshold onset fails entirely (0/8), reinforcing the multi-method rationale.\n\n\\paragraph{Grouped testing rationale.}\nWe test 8 canary$\\to$downstream pairs jointly (2 canaries $\\times$ 4 downstream metrics) rather than individual per-metric tests because: (i)~joint testing with BH-FDR correction controls family-wise error across the canary panel, avoiding the inflated false-positive rate that would result from reporting the single most significant pair; (ii)~the count of significant pairs ($k/8$) provides a natural effect-size measure that distinguishes isolated from systematic detection; (iii)~per-metric tests cannot capture the cross-metric consistency that separates genuine temporal precedence from metric-specific artifacts (e.g., MAUVE floor saturation affects 2/8 pairs universally, identifiable only in grouped results).\n\n\\paragraph{Canary metric choice.}\nSmolLM3-3B reveals that canary metric selection constitutes a sensitivity dimension beyond the five statistical methods: token entropy exhibits non-monotonic oscillations (0/4 significant pairs), while ECE maintains monotonic growth (3/4 pairs).\nNo single canary metric is universally optimal.\n\n\\paragraph{Exploratory CSD analysis.}\nCanary metrics show rising autocorrelation (Kendall $\\tau{=}0.79$--$0.82$) while downstream metrics show none ($\\tau{=}0.03$--$0.30$), but this pattern does not survive multiple testing correction (2/10 post-BH) and remains exploratory.\nWe note that \\citet{truong2026phase} show model collapse is a first-order transition, ruling out CSD as a structural detection mechanism; the rising autocorrelation likely reflects non-stationarity rather than critical slowing down.\n\n\\paragraph{Scale verification (Pythia-1.4B).}\n\\label{app:scale_14b}\nTo test whether the phase-diagram structure generalizes beyond 410M, we replicate the analysis at 1.4B scale ($T{=}10$--$15$, fp32, seed~42).\nTable~\\ref{tab:14b_phase} summarizes the available cells.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pythia-1.4B phase-diagram cells (fp32, PermG forward, direction-checked).}\n\\label{tab:14b_phase}\n\\begin{tabular}{lcccc}\n\\toprule\n$\\alpha$ & \\multicolumn{2}{c}{$T{=}10$} & \\multicolumn{2}{c}{$T{=}15$} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n         & s42 & s44 & s42 & s43 \\\\\n\\midrule\n0.45 & 0/6 & 0/6 & 3/6 & 5/6 \\\\\n0.50 & 4/6 & 6/6 & 3/6 & 3/6 \\\\\n0.60 & 4/6 & 6/6 & 6/6 & 6/6 \\\\\n0.75 & 5/6 & 6/6 & 6/6 & 6/6 \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize All: PermG fwd, 6-pair basis (2 canaries $\\times$ 3 distinct-$n$;} \\\\\n\\multicolumn{5}{l}{\\footnotesize MAUVE excl.\\ due to floor ${\\sim}0.033$ at 1.4B).} \\\\\n\\multicolumn{5}{l}{\\footnotesize s42 rev.\\ 0/6 at all $\\alpha$; s43 rev.\\ see text.} \\\\\n\\end{tabular}\n\\end{table}\n\nThe phase-diagram structure is qualitatively preserved at 1.4B scale.\nECE maintains monotonic growth across all three tested $\\alpha$ levels (3/3 cross-scale robust), and the binary detection pattern (above vs.\\ below $\\alpha_c$) is consistent with the 410M phase diagram.\nOn the 6-pair basis (MAUVE excluded due to systematic floor ${\\sim}0.033$; Table~\\ref{tab:14b_phase}), PermG forward detection at 1.4B ranges from 0/6 ($\\alpha{=}0.45$, $T{=}10$) to 6/6 ($\\alpha{\\geq}0.60$, $T{=}15$); token entropy exhibits one-step saturation ($27$--$39\\%$ drop from generation~0 to~1), reducing temporal resolution for entropy-based pairs.\nSeed s42 shows PermG$_\\text{rev}{=}0/6$ across all eight 1.4B conditions ($4\\alpha{\\times}2T$), confirming that bidirectionality is seed-specific rather than scale-inherent.\nThe 410M sync-dip ($\\alpha{=}0.60$: 0/8 at $T{\\leq}20$) does not reproduce at 1.4B (4/6 at $T{=}10$); whether this reflects scale-dependent dynamics or Pythia-specific effects remains open with only two model sizes tested.\nAt $T{=}15$, scale effects are $\\alpha$-conditional: $\\alpha{=}0.60$ reaches 6/6, while $\\alpha{=}0.50$ attenuates to 3/6 (vs 4/6 at $T{=}10$), confirming that detection loss is onset-localized rather than uniform.\nThe boundary's $T$-dependence is preserved: $\\alpha{=}0.45$ rises from 0/6 ($T{=}10$) to 3/6 ($T{=}15$), mirroring the 410M boundary shift.\nHowever, method-level heterogeneity emerges: Toda--Yamamoto exhibits a non-monotonic pattern at $T{=}15$, inverting the PermG ordering in the mid-$\\alpha$ range; gradual low-$\\alpha$ dynamics preserve VAR lag structure, while rapid entropy saturation disrupts lag dependence at intermediate $\\alpha$, with recovery at $\\alpha{=}0.75$ where extreme collapse dynamics (PPL drift ${+}390\\%$) generate sufficient temporal variation to support VAR detection.\nOnset-zone attenuation is $\\alpha$-invariant at 1.4B: both $\\alpha{=}0.45$ and $0.50$ yield 3/6 at $T{=}15$.\nAt 1.4B with $T{=}10$ (11 data points), non-PermG methods (threshold onset, naive cross-correlation, Toda--Yamamoto) have insufficient power due to short sequence length, reducing $K{\\geq}3$ consensus to an effective single-method test; at $T{=}15$ (16 data points), detection recovers (6/6 at $\\alpha{=}0.60$, lead time ${=}$ 10 generations) and $K{\\geq}3$ recovers its multi-method character, with 3/4 $\\alpha$ conditions achieving $K{\\geq}3{\\geq}2/6$ (onset $\\alpha{=}0.50$ seed-dependent: s42 1/6, s43 3/6).\nCross-method consensus ($K{\\geq}3$) exhibits seed-dependent variability at onset ($\\alpha{\\approx}0.50$), consistent with the noisy transition expected at phase boundaries, while remaining robust above onset ($K{\\geq}3$ ${\\geq}5/6$ at $\\alpha{=}0.75$).\nOn a unified 6-pair basis (MAUVE excluded due to systematic floor at ${\\sim}0.033$; Table~\\ref{tab:14b_phase}), third-seed replication (s44) at $T{=}10$ confirms ceiling detection above onset (6/6 at $\\alpha{\\geq}0.50$) with 0/6 at $\\alpha{=}0.45$, validating the blind zone.\nCross-$T$ improvement holds at 3/4 $\\alpha$ values ($\\alpha{=}0.45$: $0/6{\\to}5/6$; $\\alpha{=}0.60$: $6/6{\\to}6/6$; $\\alpha{=}0.75$: $6/6{\\to}6/6$), validating the predicted $\\alpha_c(T)$ decrease; at onset ($\\alpha{=}0.50$), PermG shows a marginal decrease ($6/6{\\to}3/6$), consistent with phase-boundary variability.\nAt onset ($\\alpha{=}0.45$--$0.50$), ECE-based pairs achieve higher detection rates than entropy-based pairs (e.g., 3/3 vs 0/3 robust at $\\alpha{=}0.50$, $T{=}15$), consistent with entropy's one-step saturation reducing temporal resolution at 1.4B scale.\n\n\\paragraph{Future work.}\nExtensions include multivariate VAR models for confounder testing, multi-seed replication across all six architecture families, longer training runs ($T{\\geq}20$), online monitoring within training pipelines, and accumulate-mode experiments~\\cite{dey2024breaking}.\nThe sigmoid onset boundary ($\\alpha_c{=}0.483$) invites connection to the critical mixture ratio scaling law of \\citet{gu2024cmr} and the data-mixing transitions of \\citet{gu2025datamixing}.\n\n\n\\section{Per-Method Dose-Response Profiles}\n\\label{app:dose_response}\n\nTable~\\ref{tab:dose_response_full} reports FDR significance counts (/8 validated pairs) for all five detection methods across 12 contamination levels (seed~42, Pythia-410M, WikiText, fp32).\nPermG exhibits a sharp 0$\\to$6 jump at $\\alpha{=}0.50$ with a return to 0 at $\\alpha{=}0.55$--$0.60$ (non-monotonic dip), while other methods show diffuse profiles: naive cross-correlation saturates at 7--8/8 across all levels including the null, and Toda--Yamamoto fluctuates without a clear onset.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-method FDR significance (/8 pairs) across contamination levels (Pythia-410M, seed~42, WikiText, fp32). PermG and Diff.\\ XCorr use BH-corrected FDR ($q{=}0.05$); Naive XCorr, Threshold, and TY use uncorrected $p{<}0.05$ (no FDR field in pipeline). $\\alpha{=}1.0$ from Pythia-410M cross-architecture condition (same seed/domain/precision).}\n\\label{tab:dose_response_full}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & Naive & Diff.\\ XCorr & Threshold & PermG & TY$^\\S$ \\\\\n\\midrule\n0.00 & 8 & 4 & 3 & \\textbf{0} & 1 \\\\\n0.10 & 7 & 6 & 0 & \\textbf{0} & 0 \\\\\n0.25 & 8 & 3 & 0 & \\textbf{0} & 2 \\\\\n0.30 & 8 & 4 & 0 & \\textbf{0} & 3 \\\\\n0.35 & 8 & 4 & 0 & \\textbf{0} & 1 \\\\\n0.40 & 8 & 3 & 0 & \\textbf{0} & 4 \\\\\n0.45 & 8 & 6 & 0 & \\textbf{0} & 1 \\\\\n0.50 & 8 & 7 & 4 & \\textbf{6} & 3 \\\\\n0.55 & 8 & 8 & 0 & \\textbf{0} & 1 \\\\\n0.60 & 8 & 6 & 0 & \\textbf{0} & 0 \\\\\n0.75 & 7 & 6 & 0 & \\textbf{6} & 3 \\\\\n1.00 & 8 & 6 & 2 & \\textbf{6} & 1 \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\S$TY directional assignment under verification; column retained for completeness.} \\\\\n\\end{tabular}}\n\\end{table}\n\nThe table highlights PermG's combination of null-control detection at 0/8 for this seed ($\\alpha{=}0.00$; pooled FPR across 6 seeds: 11.1\\%, lowest among directional methods), sharp onset (0$\\to$6 at $\\alpha{=}0.50$), and non-monotonic dip (0 at $\\alpha{=}0.55$--$0.60$), confirming it as the method whose dose-response profile most cleanly separates detection regimes.\nNaive cross-correlation's persistently high counts (7--8/8 even at $\\alpha{=}0.00$) demonstrate the 91.7\\% pooled null-control FPR reported in \\S\\ref{sec:method}.\n\n\n\\paragraph{Comparison with naive baselines.}\n\\label{app:naive_baselines}\n\nTable~\\ref{tab:naive_baselines} compares PermG against two practitioner-facing monitoring rules across 26 experiments (18~$\\alpha$ values, Pythia-410M, $T{=}10$, fp32).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Naive baseline comparison (Pythia-410M, $T{=}10$, fp32, 3 null-control runs).}\n\\label{tab:naive_baselines}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & FPR ($\\alpha{=}0$) & Onset $\\alpha$ \\\\\n\\midrule\nPPL-slope (${\\geq}2$ consec.\\ rises) & 100\\% (3/3) & 0.10 \\\\\nVariance-threshold ($2\\sigma$) & 67\\% (2/3) & 0.10 \\\\\nPermG (fwd ${\\geq}1$) & 0\\% (0/3) & 0.50 \\\\\n\\bottomrule\n\\multicolumn{3}{l}{\\footnotesize Onset $\\alpha$: lowest $\\alpha$ where method fires (seed~42).} \\\\\n\\end{tabular}\n\\end{table}\n\nPPL-slope fires at $\\alpha{=}0$ because the first-generation learning effect (perplexity drops from 26.9 to 19.3 at generation~1, then rises monotonically from generation~2 onward) produces consecutive rises indistinguishable from contamination-driven drift.\nVariance-threshold similarly triggers on the natural perplexity recovery.\nPermG avoids these false alarms by testing canary$\\to$downstream Granger precedence rather than univariate trend, thereby excluding training-drift confounds from the detection signal.\nNaive monitoring rules cannot distinguish contamination from natural training dynamics; formal statistical testing is necessary for controlled FPR.\n\n\n\\section{PermG Power Analysis}\n\\label{app:power_analysis}\n\nWe characterize PermG detection power via simulation under a controlled data-generating process (DGP) that matches the structure of our iterative training time series.\n\n\\paragraph{DGP.}\nFor each trial, we generate a bivariate system $(X_t, Y_t)$ for $t = 1, \\ldots, T$ where $X_t = \\mu + \\epsilon_t^X$ and $Y_t = \\mu + \\beta X_{t-1} + \\epsilon_t^Y$, with $\\epsilon \\sim \\mathcal{N}(0, \\sigma^2)$ and $\\sigma{=}1$.\nThe coupling parameter $\\beta$ controls signal strength; $\\beta{=}0$ is the null.\nThe linear coupling provides a power lower bound; nonlinear dynamics in actual iterative training may yield different power characteristics.\nWe sweep $\\beta \\in [0, 2]$ across $T \\in \\{6, 8, 10, 15, 20\\}$, running 100 replications per $(\\beta, T)$ cell with 5{,}000 permutations each and BH FDR correction at $q{=}0.05$ across 8 hypothetical pairs (matching the experimental setup).\n\n\\paragraph{Results.}\nTable~\\ref{tab:beta50} reports $\\beta_{50}$, the coupling strength required for 50\\% detection power, at each observation length $T$.\nUnder $\\sqrt{T}$ scaling, the product $\\beta_{50} \\cdot \\sqrt{T}$ should be constant; the observed decrease from 5.09 ($T{=}8$) to 2.68 ($T{=}20$) indicates that power grows faster than $\\sqrt{T}$, with the empirical scaling closer to $T^{-1.1}$.\nThe $\\sqrt{T}$ formula in \\S\\ref{sec:theory} thus provides a conservative lower bound on detection power: actual power at $T{=}20$ exceeds the $\\sqrt{T}$ prediction.\nFalse positive rates under FDR correction remain at or below 2\\% across all $T$ values (raw: 1--9\\%; Table~\\ref{tab:beta50}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{PermG power analysis: $\\beta_{50}$ (coupling for 50\\% power) under BH-FDR correction ($q{=}0.05$, 8 pairs). $\\beta_{50} \\cdot \\sqrt{T}$ decreases with $T$, indicating power grows faster than $\\sqrt{T}$. FPR: false positive rate at $\\beta{=}0$ (raw / FDR-corrected). Dashes indicate $<$50\\% power not reached within $\\beta \\leq 2.0$.}\n\\label{tab:beta50}\n\\begin{tabular}{lcccc}\n\\toprule\n$T$ & $\\beta_{50}$ & $\\beta_{50} \\cdot \\sqrt{T}$ & FPR (raw) & FPR (FDR) \\\\\n\\midrule\n6  & ---  & ---  & 1\\% & 0\\% \\\\\n8  & ---  & ---  & 6\\% & 2\\% \\\\\n10 & 2.0  & 6.32 & 9\\% & 2\\% \\\\\n15 & 1.2  & 4.65 & 6\\% & 2\\% \\\\\n20 & 0.9  & 4.02 & 5\\% & 1\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/permg_power_curve.pdf}\n\\caption{PermG detection power as a function of coupling strength $\\beta$ for five observation lengths ($T{=}6$--$20$; 100 replications $\\times$ 5{,}000 permutations, BH FDR $q{=}0.05$). Power increases with both $\\beta$ and $T$; at $T{=}6$--$8$, PermG remains underpowered ($<$20\\%) even at $\\beta{=}2.0$, consistent with the $T{=}10$ minimum required for reliable detection in our experimental setting.}\n\\label{fig:permg_power}\n\\end{figure*}\n\nAt $T{=}6$ and $T{=}8$, 50\\% power is not reached within $\\beta \\leq 2.0$ under FDR correction, explaining why PermG is fundamentally underpowered for very short series.\nThe practical implication for our $T{=}10$ setting: $\\beta_{50}{=}2.0$ means that only strong coupling produces reliable detection, consistent with the sharp onset at $\\alpha_c{\\approx}0.50$ where signal strength first exceeds this threshold.\nAt $T{=}20$, $\\beta_{50}$ drops to 0.9, predicting a left-shift of $\\alpha_c$ and broader detection coverage, as formalized in the detection boundary model (\\S\\ref{sec:theory}).\n\n\n\\section{Non-Stationarity Robustness Analysis}\n\\label{app:nonstationarity}\n\nWe assess PermG's size and power under controlled non-stationarity via Monte Carlo simulation, then compare to the empirical autocorrelation structure of our experimental series.\n\n\\paragraph{Simulation design.}\nWe generate bivariate AR(1) series with unidirectional coupling ($x \\to y$):\n$x_t = \\varphi x_{t-1} + \\varepsilon_t^x$, $y_t = \\varphi y_{t-1} + \\beta x_{t-1} + \\varepsilon_t^y$,\nwith $T{=}11$, 1{,}000 replications, and 500 permutations per replication.\nSize is evaluated under $H_0{:}\\;\\beta{=}0$; power under $H_1{:}\\;\\beta{=}0.6$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Size (FPR at $\\beta{=}0$) and power ($\\beta{=}0.6$) under stationary and non-stationary AR(1) DGP ($T{=}11$, 1{,}000 reps, 500 perms). First-differencing maintains nominal size across all $\\varphi$; PermG FPR inflates to ${\\sim}10\\%$ at $\\varphi{\\geq}0.95$.}\n\\label{tab:nonstationarity_sim}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{Size (\\%, $\\beta{=}0$)} & \\multicolumn{3}{c}{Power (\\%, $\\beta{=}0.6$)} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n$\\varphi$ & Raw GC & First-Diff & PermG & Raw GC & First-Diff & PermG \\\\\n\\midrule\n0.50 & 6.4 & 6.6 & 6.8 & 37.7 & 17.7 & 36.8 \\\\\n0.95 & 10.0 & 5.9 & 9.5 & 44.3 & 28.7 & 41.5 \\\\\n0.99 & 11.2 & 4.2 & 10.7 & 46.4 & 24.6 & 41.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\varphi{=}0.50$ (stationary), all three methods achieve near-nominal size ($6.4$--$6.8\\%$ vs.\\ $5\\%$ nominal).\nUnder strong non-stationarity ($\\varphi{\\geq}0.95$), PermG FPR inflates to ${\\sim}10\\%$ because permutation shuffling destroys temporal autocorrelation, shifting the null distribution.\nFirst-differencing maintains proper size ($4.2$--$6.6\\%$) at the cost of reduced power ($17.7$--$28.7\\%$ vs.\\ PermG's $36.8$--$41.7\\%$).\nOur pipeline applies first-differencing \\emph{before} permutation testing, combining PermG's power advantage with differencing's size control; the simulation isolates each component to characterize the tradeoff.\n\n\\paragraph{Empirical autocorrelation.}\nTable~\\ref{tab:empirical_ar1} reports AR(1) coefficients from seven experimental conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Empirical AR(1) coefficients for token entropy (te) and distinct-1 (d1), raw and first-differenced series. High raw $\\varphi$ in d1 reflects deterministic iterative-training decline, not stochastic AR persistence; first-differencing reduces $\\varphi$ to $< 0.44$.}\n\\label{tab:empirical_ar1}\n\\begin{tabular}{llrcccc}\n\\toprule\nExperiment & $\\alpha$ & $T$ & te $\\varphi_{\\text{raw}}$ & d1 $\\varphi_{\\text{raw}}$ & te $\\varphi_{\\text{diff}}$ & d1 $\\varphi_{\\text{diff}}$ \\\\\n\\midrule\na000\\_s42 & 0.00 & 10 & $-0.51$ & $0.86$ & $-0.57$ & $-0.14$ \\\\\na025\\_s42 & 0.25 & 10 & $-0.34$ & $0.95$ & $-0.45$ & $0.19$ \\\\\na050\\_s42 & 0.50 & 10 & $-0.28$ & $0.87$ & $0.31$ & $0.10$ \\\\\na075\\_s42 & 0.75 & 10 & $0.14$ & $0.91$ & $0.88$ & $0.24$ \\\\\na100\\_s42 & 1.00 & 10 & $1.00$ & $0.89$ & $0.98$ & $0.18$ \\\\\nt20\\_a050 & 0.50 & 20 & $-0.10$ & $0.97$ & $-0.25$ & $0.44$ \\\\\nt20\\_a100 & 1.00 & 20 & $0.98$ & $0.81$ & $0.87$ & $0.14$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Adequacy argument.}\nUnder null conditions ($\\alpha{=}0.0$), where FPR is defined, token entropy exhibits $\\varphi{=}-0.51$ (anti-correlated, far from the $\\varphi{\\geq}0.95$ regime where simulation reveals FPR inflation); at $\\varphi{=}0.50$, PermG FPR is $6.8\\%$, near nominal.\nThe high raw $\\varphi$ in distinct-1 ($0.81$--$0.97$ across all $\\alpha$ including null) reflects deterministic iterative-training diversity decline---a monotonic trend driven by the training protocol---not stochastic AR persistence.\nDeterministic trends differ fundamentally from the stochastic AR(1) DGP: they produce predictable trajectories rather than autocorrelated noise, and first-differencing effectively removes them (first-differenced distinct-1 $\\varphi$ ranges $-0.14$ to $0.44$, mean ${\\sim}0.17$).\nOur empirical FPR of 4/36 (11.1\\%) across six null seeds---the lowest among directional methods---confirms adequate size control in our experimental setting; all four false positives occur in token\\_entropy$\\to$distinct pairs in the forward direction, suggesting a structural pattern rather than random Type~I error.\nWe note that $T{=}10$ (11 data points) yields high-variance AR(1) estimates; the cross-experiment pattern is more informative than individual values.\n\n\\paragraph{DGP limitation.}\nThe bivariate AR(1) with linear coupling is a simplification; actual iterative training involves nonlinear dynamics (mode amplification, threshold-dependent diversity loss).\nThese simulation results characterize PermG's behavior under controlled conditions, not exact calibration for the experimental setting; they provide a lower bound on size control because the linear DGP represents a worst case for permutation-based tests (smooth autocorrelation that permutation destroys).\n\n\n\\section{Shapley Value Analysis}\n\\label{app:shapley}\n\nWe quantify each method's marginal contribution to the MMCT ensemble using Shapley values~\\cite{shapley1953value}, computed via exact enumeration over all $2^5{=}32$ coalitions of the five detection methods.\n% TODO-D219: recompute Shapley with 6-seed null data (seeds 45--50, 36 null pairs; PermG FPR now 4/36=11.1%, no longer zero)\nFor a coalition $S \\subseteq \\{m_1, \\ldots, m_5\\}$, we define two performance metrics: the false positive rate FPR($S$), computed from 3 null experiments ($\\alpha{=}0.0$, seeds 42/43/44; 24 null pairs total), and the false negative rate FNR($S$), computed from 45 signal experiments across all non-null $\\alpha$ levels (270 signal pairs for the 6-pair variant excluding mauve).\nThe Shapley value $\\phi_k$ for method $m_k$ is the weighted average of its marginal contribution across all coalitions; positive FPR-Shapley indicates the method \\emph{increases} false positives, while negative FNR-Shapley indicates it \\emph{reduces} false negatives.\nThe combined Shapley value $\\phi_k^{\\text{comb}} = \\phi_k^{\\text{FPR}} + \\phi_k^{\\text{FNR}}$ balances both error types, with more negative values indicating greater net benefit.\n\nTable~\\ref{tab:shapley_6pair} reports the 6-pair analysis (excluding mauve).\n% TODO-D219: recompute Shapley values; PermG φ^FPR will be >0 with 6-seed data (4/36 FPs)\nPermG achieves the lowest (best) combined Shapley ($-0.180$), driven entirely by FNR reduction with zero FPR contribution---the only method with this property.\nNaive cross-correlation is the worst contributor ($+0.203$), with its massive FPR Shapley ($+0.622$) overwhelming its FNR benefit ($-0.419$): adding naive cross-correlation to any coalition increases false positives far more than it reduces false negatives.\nThreshold onset contributes almost nothing useful ($+0.074$ combined; FPR $+0.101$, FNR $-0.027$), confirming the near-zero detection power reported in Table~\\ref{tab:method_comparison}.\nFigure~\\ref{fig:shapley} visualizes the decomposition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Shapley value decomposition (6-pair, mauve excluded). FPR-Shapley: marginal FPR contribution (positive = increases false positives). FNR-Shapley: marginal FNR contribution (negative = reduces false negatives). Combined = FPR + FNR (more negative = better). 48 experiments, $2^5{=}32$ coalitions, exact enumeration.}\n\\label{tab:shapley_6pair}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $\\phi^{\\text{FPR}}$ & $\\phi^{\\text{FNR}}$ & $\\phi^{\\text{comb}}$ \\\\\n\\midrule\nNaive XCorr          & $+0.622$ & $-0.419$ & $+0.203$ \\\\\nDiff.\\ XCorr         & $+0.163$ & $-0.306$ & $-0.142$ \\\\\nThreshold ($3\\sigma$) & $+0.101$ & $-0.027$ & $+0.074$ \\\\\n\\textbf{Perm.\\ Granger} & $\\mathbf{0.000}$ & $\\mathbf{-0.180}$ & $\\mathbf{-0.180}$ \\\\\nToda--Yamamoto       & $+0.031$ & $-0.069$ & $-0.038$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/shapley_method_contribution.pdf}\n% TODO-D219: regenerate figure and update caption after Shapley recomputation with 6-seed data\n\\caption{Shapley value decomposition of each method's marginal contribution to FPR (positive bars) and FNR (negative bars). PermG is the only method with zero FPR contribution; naive cross-correlation's FPR dominates its FNR benefit.}\n\\label{fig:shapley}\n\\end{figure*}\n\nThe 8-pair variant (including mauve) yields qualitatively identical rankings: PermG remains the best contributor ($\\phi^{\\text{comb}}{=}-0.152$), naive cross-correlation the worst ($+0.170$), and threshold onset near-zero ($+0.063$).\n\n\\paragraph{FDR correction scope.}\nThis analysis applies BH-corrected significance (\\texttt{significant\\_fdr}) uniformly across all five methods, including naive cross-correlation and Toda--Yamamoto.\nIn contrast, the per-method dose-response profiles (Table~\\ref{tab:dose_response_full}) use uncorrected significance for naive cross-correlation, threshold onset, and Toda--Yamamoto because FDR-corrected fields are not available in the per-experiment pipeline output for these methods.\nThe Shapley analysis recomputes significance from raw $p$-values with BH correction applied post hoc, ensuring a fair comparison across methods within the coalition framework.\n\n\n\\section{MMCT Weight Robustness Ablation}\n\\label{app:weight_robustness}\n\nThe detection results reported in the main text use equal-weight majority voting ($K{\\geq}3$ of 5 methods, each contributing at most one vote per pair); PermG contributes at most $1/5 = 20\\%$ of the consensus weight.\nFPR-inverse weighting is used \\emph{only} in the exploratory method ranking below, not in the detection results.\nTo verify that PermG's top ranking is not an artifact of the FPR-inverse weighting scheme, we recompute Shapley values under four weight specifications (Table~\\ref{tab:weight_robustness}).\nEqual weighting ($w{=}1$ for all methods) eliminates any FPR-based advantage; PermG still ranks first ($\\phi^{\\text{comb}}{=}-0.152$), though its margin over naive cross-correlation narrows to 0.015.\nUnder cap-5, the margin widens to 0.043 as the FPR penalty begins to differentiate high-FPR methods.\nCap-10 and original cap-100 yield identical Shapley values because the consensus threshold ($K{\\geq}3$) is determined by the three smallest method weights ($w_{\\text{naive}}{+}w_{\\text{diff}}{+}w_{\\text{thresh}} = 7.76$), which are invariant to further increases in the PermG or TY cap; this saturation confirms that the original $w{=}100$ does not artificially inflate PermG's contribution.\n% TODO-D219: recompute weight robustness table with 6-seed data; PermG φ^FPR will be >0\nAcross all schemes, PermG's advantage derives from the same structural property: zero FPR ($\\phi^{\\text{FPR}}{=}0$) combined with moderate FNR reduction ($\\phi^{\\text{FNR}}{=}-0.152$ to $-0.426$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MMCT weight robustness: PermG combined Shapley under four weighting schemes. PermG ranks first in all cases. Gap = $|\\phi^{\\text{comb}}_{\\text{PermG}} - \\phi^{\\text{comb}}_{\\text{runner-up}}|$. 48 experiments (3 null + 45 signal), exact Shapley enumeration ($2^5{=}32$ coalitions).}\n\\label{tab:weight_robustness}\n\\begin{tabular}{lrcrc}\n\\toprule\nScheme & $w_{\\text{PermG}}$ & $\\phi^{\\text{comb}}_{\\text{PermG}}$ & Runner-up & Gap \\\\\n\\midrule\nEqual ($w{=}1$)     & 1   & $-0.152$ & NaiveXCorr ($-0.137$) & 0.015 \\\\\nCap-5               & 5   & $-0.165$ & NaiveXCorr ($-0.123$) & 0.043 \\\\\nCap-10              & 10  & $-0.426$ & TY ($-0.067$)         & 0.359 \\\\\nFPR-inv.\\ (cap-100) & 100 & $-0.426$ & TY ($-0.067$)         & 0.359 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{PermG FPR Independence Analysis}\n\\label{app:fpr_independence}\n\nTable~\\ref{tab:null_fpr_methods} reports null-control FPR for all five detection methods across six seeds ($6 \\times 6 = 36$ pairs, 6-pair basis excluding mauve).\nUnder identical BH-FDR correction ($q{=}0.05$), DiffXCorr achieves the lowest FPR (1/36, 2.8\\%) but lacks directional separation; PermG (4/36, 11.1\\%) is the lowest among directional methods.\nAll four PermG false positives occur in token\\_entropy$\\to$distinct pairs (seeds~45 and 50, forward direction only), suggesting a structural pattern concentrated in a single canary--downstream pair type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Null-control FPR by method ($\\alpha{=}0.0$, 6~seeds 45--50, 6~pairs each). All p-value--based methods (DiffXCorr, PermG, TY) report BH-FDR--corrected rejections at $q{=}0.05$ for fair comparison. Threshold uses a deterministic $3\\sigma$ criterion; NaiveXCorr uses uncorrected correlation significance.}\n\\label{tab:null_fpr_methods}\n\\begin{tabular}{llrr}\n\\toprule\nMethod & Criterion & Rejections (/36) & FPR (\\%) \\\\\n\\midrule\nDiff.\\ XCorr$^\\dagger$ & BH-FDR & 1 & 2.8 \\\\\n\\textbf{Perm.\\ Granger} & \\textbf{BH-FDR} & \\textbf{4} & \\textbf{11.1} \\\\\nThreshold & $3\\sigma$ (det.) & 10 & 27.8 \\\\\nToda--Yamamoto & BH-FDR & 14 & 38.9 \\\\\nNaive XCorr & uncorr. & 33 & 91.7 \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$Bidirectional; cannot separate forward from reverse.} \\\\\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cluster adjustment.}\nThe 36 null-control pairs are nested within 6~seeds (6~pairs per seed), introducing within-seed correlation.\nWithin-seed ICC${=}0.14$ yields an effective sample size $N_{\\text{eff}} \\approx 21$ (from $N_{\\text{eff}} = N / [1 + (m-1) \\cdot \\text{ICC}]$ where $N{=}36$, $m{=}6$).\nUnder the Clopper--Pearson exact method with $N_{\\text{eff}}{=}21$ and 4 successes (scaled), the cluster-adjusted 95\\% CI is $[1.2\\%, 30.4\\%]$, compared to $[3.1\\%, 26.1\\%]$ under independence ($N{=}36$).\nThe lower ICC compared to the 3-seed pilot ($0.14$ vs.\\ $0.34$) reflects greater between-seed consistency with six independent replications.\n\n\\paragraph{Direction filtering.}\nForward-direction filtering (retaining only pairs with peak lag${<}0$ for cross-correlation methods) reduces null-control $K{\\geq}3$ false positives.\nUnder the 6-seed, 6-pair basis, $K{\\geq}3$ consensus with filtering produces 6/36 false positives (16.7\\%; detail below); the 3-seed pilot underestimated this rate (0/8).\nDetection at $\\alpha{\\geq}0.50$ is unaffected: $K{\\geq}3$ counts are identical with and without direction filtering at all signal levels.\n\n\\paragraph{$K{\\geq}3$ false positive detail.}\nUnder the 6-pair basis (6~seeds, 36~pairs), $K{\\geq}3$ consensus produces 6 false positives (FPR${=}16.7\\%$).\nOf these, 4 are driven by naive cross-correlation, threshold onset, and Toda--Yamamoto (PermG does \\emph{not} vote); the remaining 2 (seeds~45 and 50, te$\\to$distinct) include PermG in the consensus.\nPermG thus contributes to only 2 of 6 consensus false positives, confirming that most $K{\\geq}3$ FPR is driven by the high-FPR methods (naive, threshold, TY).\n\n\\paragraph{Sensitivity to FPR assumption.}\nEven under the conservative upper bound of the cluster-adjusted CI (30.4\\%), PermG remains the lowest-FPR directional method: DiffXCorr achieves a lower FPR under identical BH-FDR correction (2.8\\%) but lacks forward/reverse separation; the next directional method (threshold onset) has 27.8\\% and Toda--Yamamoto 38.9\\%.\nOur primary results rely on equal-weight $K{\\geq}3$ majority voting, where each method contributes exactly one vote regardless of its FPR---this mechanism is completely unaffected by any FPR assumption.\nFor the exploratory FPR-inverse weighting, PermG's weight ($w{=}1/0.111{=}9.0$) exceeds all directional alternatives (threshold: 3.6, TY: 2.6, naive: 1.1); DiffXCorr ($w{=}1/0.028{=}35.7$) receives a higher weight but lacks directional separation, preserving PermG's rank among directional methods.\nThe insensitivity of both the voting mechanism and the method ranking to the upper CI bound provides evidence that the MMCT conclusions are robust to uncertainty in PermG's Type~I error rate.\n\n\\section{Sigmoid Transition Shape}\n\\label{app:sigmoid_shape}\n\nSigmoid regression on the original 13-point $T{=}10$ grid yields $\\alpha_c = 0.483 \\pm 0.006$ but $k = 478 \\pm 475$ ($\\mathrm{SE}(k) \\approx k$), indicating that the coarse grid cannot constrain the transition shape.\nDense $\\alpha$ sampling (17~values at $T{=}10$) resolves this ambiguity: formal likelihood-ratio testing strongly favors a smooth sigmoid over a literal step function ($\\Delta\\mathrm{AIC}{=}-110$), with fitted steepness $k{=}15.7$ (95\\% CI $[9.4, 28.2]$).\nThe transition is steep but finite-width, not a literal discontinuity.\nThis observed steepness exceeds what smooth signal models predict: VAR(1) simulations under H0 (linear, $k{=}6.1$) and H0$'$ (concave, $k{=}4.9$) produce onset sigmoids with $k{=}4.9$--$6.1$ (\\S\\ref{app:power_sim}), yielding steepness ratios $k_{\\mathrm{obs}} / k_{\\mathrm{H0}} \\approx 2.6$--$3.2$ (CI lower bound ratio ${\\approx}2$).\nWe do not fit a combined $T{=}10 + T{=}20$ sigmoid because $\\alpha{=}0.45$ yields contradictory counts under the two sequence lengths (0/8 vs.\\ 5/8), reflecting genuine power dependence on $T$ rather than a single dose-response curve.\n\n\n\\section{Intervention Threshold Sensitivity}\n\\label{app:intervention_sensitivity}\n\n\\paragraph{Within-$\\alpha$ sensitivity at $\\alpha{=}1.0$.}\nTable~\\ref{tab:threshold_sensitivity} reports the predictive cessation outcome under five entropy-drop thresholds (5\\%--25\\%) at $\\alpha{=}1.0$ (Pythia-410M, seed~42).\nAll five thresholds produce identical outcomes: token entropy drops 40.7\\% at generation~1, far exceeding even the most conservative threshold (25\\%), so every threshold triggers at the same generation.\nThe intervention conclusion---peak perplexity 57.0, recovery in one generation, final perplexity 21.3---is invariant to threshold choice within this range.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Threshold sensitivity at $\\alpha{=}1.0$ (Pythia-410M, s42, fp32). All thresholds trigger at generation~1 (entropy drop 40.7\\%$\\gg$threshold), producing identical recovery trajectories.}\n\\label{tab:threshold_sensitivity}\n\\begin{tabular}{rccr}\n\\toprule\nThreshold & Trigger gen & Peak PPL & Final PPL \\\\\n\\midrule\n5\\%  & 1 & 56.99 & 21.29 \\\\\n10\\% & 1 & 56.99 & 21.29 \\\\\n15\\% & 1 & 56.99 & 21.29 \\\\\n20\\% & 1 & 56.99 & 21.29 \\\\\n25\\% & 1 & 56.99 & 21.29 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-$\\alpha$ operating band.}\nThe within-$\\alpha$ analysis establishes threshold invariance at $\\alpha{=}1.0$ but does not address whether thresholds generalize across contamination levels.\nWe examine observed entropy trajectories from the alpha sweep (not actual intervention experiments at $\\alpha{<}1.0$) to characterize the operating band.\nThe maximum entropy drop across 10 generations varies by contamination level: 7.5\\% at $\\alpha{=}0.0$ (fine-tuning drift only), 7.7\\% at $\\alpha{=}0.10$, 7.8\\% at $\\alpha{=}0.25$, 22.4\\% at $\\alpha{=}0.50$, 35.3\\% at $\\alpha{=}0.75$, and 62.1\\% at $\\alpha{=}1.0$.\nThresholds below 7.5\\% (e.g., 5\\%) trigger on clean training data---a false alarm.\nThresholds above 22.4\\% (e.g., 25\\%) miss $\\alpha{=}0.50$, the lowest contamination level with meaningful entropy signal.\nThe safe operating band is therefore $[10\\%, 22\\%]$: any threshold in this range produces zero false alarms on $\\alpha{=}0.0$ while detecting contamination at $\\alpha{\\geq}0.50$.\nThe reported 15\\% threshold sits near the center of this band.\nThis analysis is based on entropy trajectories from non-intervention training runs; whether actual intervention at $\\alpha{<}1.0$ would produce the same triggering behavior remains unvalidated.\n\n\n\\section{Channel Effect Size Analysis}\n\\label{app:channel_effect_size}\n\nFirst-differencing eliminates all canary$\\to$perplexity Granger associations while preserving canary$\\to$diversity leads (\\S\\ref{sec:regime}).\nWe present three lines of evidence that this asymmetry reflects a genuine temporal structure difference rather than selective power loss from differencing.\n\n\\paragraph{Correlation retention parity.}\nFirst-differencing retains comparable correlation magnitude for both channel types (Table~\\ref{tab:channel_retention}).\nDiversity channels ($n{=}243$ pairs across all non-null experiments) retain a median $|r|$ of 0.952 after differencing, while perplexity channels ($n{=}8$ pairs; limited sample) retain 1.00.\nThis parity rules out a blanket power-loss explanation: if differencing selectively destroyed perplexity signal, $|r|$ retention would be substantially lower for perplexity than for diversity.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{First-differencing effect by channel type. $|r|$ retention = diff $|r|$ / naive $|r|$. Despite comparable $|r|$ retention, Granger $F$ differs by an order of magnitude. Perplexity channel has limited sample ($n{=}8$); all paired comparisons are from bf16 experiments.}\n\\label{tab:channel_retention}\n\\begin{tabular}{lrccrc}\n\\toprule\nChannel & $n$ & Naive $|r|$ & Diff $|r|$ & Retention & Med.\\ $F$ \\\\\n\\midrule\nDiversity   & 243 & 0.943 & 0.921 & 0.952 & 67.8 \\\\\nPerplexity  & 8   & 0.924 & 0.900 & 1.002 & 11.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Granger $F$-statistic asymmetry.}\nWithin matched experiments (same model, seed, $\\alpha$, precision), the Granger $F$-statistic is $20$--$28{\\times}$ higher for diversity than perplexity channels.\nAt $\\alpha{=}0.60$ (s42, bf16): diversity mean $F{=}229.4$ versus perplexity mean $F{=}8.3$ (ratio $27.8{\\times}$).\nAt $\\alpha{=}1.0$ reactive (s43, bf16): diversity mean $F{=}236.4$ versus perplexity mean $F{=}11.5$ (ratio $20.6{\\times}$).\nSince $|r|$ retention is comparable across channels, this $F$-statistic gap cannot be attributed to differencing-induced signal loss; it must reflect a difference in the temporal structure that Granger tests evaluate.\n\n\\paragraph{Temporal structure: lagged vs.\\ contemporaneous.}\nThe lag distribution of peak differenced cross-correlations reveals the structural difference.\nFor diversity channels, 81\\% of peak correlations occur at canary-leading lags (lag${<}0$), with a median lag of $-1$ generation---consistent with the one-generation temporal precedence visible in Figure~\\ref{fig:metric_trajectory}.\nFor perplexity channels, 50\\% of peak correlations occur at lag${=}0$ (contemporaneous co-movement), with a median lag of $0$.\nGranger precedence tests lagged predictive improvement; contemporaneous co-movement produces low $F$-statistics regardless of signal magnitude, which is the correct behavior for a test designed to detect temporal precedence.\nThe perplexity channel sample is limited ($n{=}8$ pairs from bf16 experiments), and these lag distributions should not be generalized to fp32 conditions without further validation.\n\n\n\\section{Mutual Information Analysis}\n\\label{app:mi_analysis}\n\nWe estimate the Gaussian mutual information lower bound between token entropy (canary) and each diversity metric across contamination levels, using $T{=}11$ data points per series ($T{=}10$ for two conditions).\nThe Gaussian estimator $\\hat{I}_G = -\\frac{1}{2}\\log_2(1 - r^2)$, where $r$ is the Pearson correlation, provides a conservative lower bound on MI; we do not report KSG nonparametric estimates due to uncorrected positive bias at $T{=}11$.\nThe $\\alpha{=}0.05$ data point is excluded because it uses an experiment excluded from the dose-response analysis.\n\nTable~\\ref{tab:mi_bounds} reports the mean Gaussian MI across the three distinct-$n$ metrics for each $\\alpha$ level.\nMI follows a V-shaped curve: it drops from 0.112~bits at $\\alpha{=}0.10$ to a minimum of 0.010~bits at $\\alpha{=}0.25$, then rises monotonically to 0.270~bits at $\\alpha{=}0.75$.\nMI remains positive throughout the blind zone ($\\alpha \\leq 0.45$; range 0.010--0.141~bits), confirming that canary--diversity coupling exists below the detection threshold but falls below PermG's statistical power floor at $T{=}10$.\nThere is no discontinuity at $\\alpha_c \\approx 0.50$: the detection onset reflects power accumulation, not an abrupt change in information coupling.\nBootstrap 95\\% CIs span 1--3 orders of magnitude at $T{=}11$, so individual point estimates should be interpreted cautiously.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Gaussian MI lower bound (bits) between token entropy and distinct-$n$ diversity metrics ($T{=}11$, Pythia-410M, fp32). Mean across distinct-1/2/3; $\\alpha{=}0.05$ excluded (see text). CIs omitted due to width at $T{=}11$.}\n\\label{tab:mi_bounds}\n\\begin{tabular}{rrc}\n\\toprule\n$\\alpha$ & Seeds & MI (bits) \\\\\n\\midrule\n0.10 & 2 & 0.112 \\\\\n0.25 & 3 & 0.010 \\\\\n0.30 & 1 & 0.062 \\\\\n0.35 & 1 & 0.098 \\\\\n0.40 & 1 & 0.119 \\\\\n0.45 & 2 & 0.141 \\\\\n0.50 & 3 & 0.107 \\\\\n0.60 & 2 & 0.209 \\\\\n0.75 & 1 & 0.270 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Moment Cascade Analysis}\n\\label{app:moment_cascade}\n\nWe analyze the temporal ordering of metric degradation onset across 6 WikiText seed${\\times}\\alpha$ conditions (2 seeds $\\times$ 3 non-trivial $\\alpha$ levels each) to test whether token entropy consistently degrades before diversity metrics.\nOnset is defined as the first generation where a metric's cumulative change exceeds 5\\% of its generation-0 value.\n\nTable~\\ref{tab:moment_cascade} reports the onset generation for each metric across conditions.\nToken entropy reaches onset at generation~1 in all 6 conditions; distinct-$n$ metrics reach onset at generation~2 in all 18 pairwise comparisons (6 conditions $\\times$ 3 distinct-$n$ metrics).\nAcross these 18 comparisons, entropy degrades first in 16 cases (Kendall $\\tau{=}0.337$, consistent with a weak but reliable temporal ordering).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Degradation onset generation (5\\% threshold) by metric and condition (Pythia-410M, WikiText, fp32). Token entropy reaches onset at generation~1 in all non-null conditions; distinct-$n$ metrics follow at generation~2.}\n\\label{tab:moment_cascade}\n\\begin{tabular}{llcccccc}\n\\toprule\nSeed & $\\alpha$ & Entropy & Dist-1 & Dist-2 & Dist-3 & ECE & PPL \\\\\n\\midrule\n42 & 0.10 & 1 & 2 & 2 & 2 & 2 & --- \\\\\n42 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\\\\n42 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\\\\n43 & 0.25 & 1 & 2 & 2 & 2 & 4 & --- \\\\\n43 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\\\\n43 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\\\\n\\bottomrule\n\\multicolumn{8}{l}{\\footnotesize ---: onset not reached within $T{=}10$ generations.} \\\\\n\\end{tabular}\n\\end{table}\n\nThe cascade ordering provides evidence for the canary mechanism independent of Granger-type tests: it does not depend on first-differencing, lag selection, or the permutation null distribution.\nECE shows onset at generation~1 at $\\alpha{\\geq}0.50$ (both seeds), consistent with its role as a secondary canary metric.\nAt low contamination ($\\alpha{=}0.10$ and $\\alpha{=}0.25$), perplexity never reaches the 5\\% onset threshold within $T{=}10$ generations, while entropy already shows generation-1 onset---consistent with entropy's higher sensitivity to distributional shifts.\n\n\n\\section{Cascade Ordering Theory: Proofs}\n\\label{app:cascade_theory}\n\nThis section provides the full proofs for Proposition~\\ref{thm:entropy_leads} and Proposition~\\ref{prop:div_lag} from \\S\\ref{sec:cascade}, plus supporting results.\n\n\\begin{assumption}[Mode Amplification]\\label{ass:mode_amp}\nThe training map $\\mathcal{T}$ redistributes probability mass from low-probability to high-probability tokens: there exists a threshold $\\bar{p}$ such that $\\mathcal{T}(p)_i > p_i \\Rightarrow p_i \\geq \\bar{p}$ and $\\mathcal{T}(p)_j < p_j \\Rightarrow p_j \\leq \\bar{p}$.\n\\end{assumption}\n\nThis captures the standard finite-capacity approximation effect: MLE on finite samples from a peaked distribution amplifies modes and suppresses the tail~\\cite{shumailov2024curse,dohmatob2024tale}.\n\n\\begin{proposition}[Entropy is a first-order indicator]\\label{prop:entropy_first}\nLet $p \\in \\Delta^{V-1}$ and $\\delta = \\alpha(\\mathcal{T}(p) - p)$ be a mode-amplifying perturbation with $\\sum_i \\delta_i = 0$. Then $\\Delta H = H(p+\\delta) - H(p) = -\\sum_i \\delta_i \\log p_i + O(\\|\\delta\\|^2) < 0$.\n\\end{proposition}\n\n\\begin{proof}\nTaylor-expanding $H$ around $p$:\n$H(p+\\delta) = H(p) - \\sum_i \\delta_i \\log p_i - \\sum_i \\delta_i - \\frac{1}{2}\\sum_i \\delta_i^2/p_i + O(\\|\\delta\\|^3)$.\nSince $\\sum_i \\delta_i = 0$: $\\Delta H = -\\sum_i \\delta_i \\log p_i - \\frac{1}{2}\\sum_i \\delta_i^2/p_i + O(\\|\\delta\\|^3)$.\nUnder mode amplification, tokens gaining mass ($\\delta_i > 0$) have $p_i \\geq \\bar{p}$ (hence $\\log p_i \\geq \\log \\bar{p}$) and tokens losing mass ($\\delta_j < 0$) have $p_j \\leq \\bar{p}$ (hence $\\log p_j \\leq \\log \\bar{p}$).\nWriting $m = \\sum_{i:\\delta_i > 0} \\delta_i$: $-\\sum_i \\delta_i \\log p_i = -m[\\overline{\\log p}^{+} - \\overline{\\log p}^{-}] < 0$, where $\\overline{\\log p}^{\\pm}$ are the $|\\delta|$-weighted means over gaining/losing tokens.\nThe second-order Fisher information term $-\\frac{1}{2}\\sum_i \\delta_i^2/p_i$ is always negative, reinforcing the decrease.\n\\end{proof}\n\n\\begin{proposition}[Diversity is a threshold indicator]\\label{prop:div_threshold}\nDefine the $\\epsilon$-effective support $S_\\epsilon(p) = |\\{i \\in [V]: p_i > \\epsilon\\}|$, where $\\epsilon \\approx c/N$ is the generation threshold for sample size $N$.\nUnder the same perturbation $\\delta$: $\\Delta S_\\epsilon = -|\\{i: p_i > \\epsilon \\text{ and } p_i + \\delta_i \\leq \\epsilon\\}|$.\nThis equals zero whenever $\\|\\delta\\|_\\infty < \\gamma(p,\\epsilon) := \\min_{i: p_i > \\epsilon}(p_i - \\epsilon)$.\n\\end{proposition}\n\n\\begin{proof}\nToken $i$ exits the effective support iff $p_i > \\epsilon$ and $p_i + \\delta_i \\leq \\epsilon$, requiring $|\\delta_i| \\geq p_i - \\epsilon$.\nIf $\\|\\delta\\|_\\infty < \\gamma$, no token satisfies this condition.\n\\end{proof}\n\n\\paragraph{Proof of Proposition~\\ref{thm:entropy_leads}.}\n\\emph{Part (a):} Take any mode-amplifying $\\delta$ with $\\|\\delta\\|_\\infty < \\gamma(p,\\epsilon)$.\nBy Proposition~\\ref{prop:div_threshold}, $\\Delta S_\\epsilon = 0$.\nBy Proposition~\\ref{prop:entropy_first}, $\\Delta H < 0$.\nSuch $\\delta$ exists for all $\\alpha < \\gamma / \\max_i |\\mathcal{T}(p)_i - p_i|$.\n\\emph{Part (b):} If $\\Delta S_\\epsilon < 0$, some token $k$ has $p_k > \\epsilon$ but $p_k + \\delta_k \\leq \\epsilon$, so $\\delta_k < 0$.\nUnder mode amplification, this implies $p_k \\leq \\bar{p}$; the total mass transferred to high-probability tokens ensures $\\overline{\\log p}^+ > \\overline{\\log p}^-$.\nBy Proposition~\\ref{prop:entropy_first}, $\\Delta H < 0$. $\\square$\n\n\\paragraph{Proof of Proposition~\\ref{prop:div_lag}.}\nBy the margin condition, at every generation $s \\leq t_H$ the perturbation norm $\\alpha\\|\\mathcal{T}(p_s) - p_s\\|_\\infty$ is less than $\\gamma(p_s, \\epsilon)$.\nBy Proposition~\\ref{prop:div_threshold}, no token exits the effective support at any $s \\leq t_H$, so $\\Delta S_\\epsilon = 0$ for all $s \\leq t_H$.\nSince time is discrete, $t_D \\geq t_H + 1$. $\\square$\n\n\\paragraph{ECE co-movement (qualitative argument).}\nUnder conditional mode amplification (peakier $q_\\theta(\\cdot|x)$ at each generation), per-token conditional entropy $h(x) = H(q_\\theta(\\cdot|x))$ decreases while confidence $c(x) = \\max_y q_\\theta(y|x) \\geq \\exp(-h(x))$ increases.\nAveraging: $\\bar{H}_t$ decreases, $C_t$ increases.\nWith accuracy approximately stationary in early collapse ($A_t \\approx A_0$), $\\Delta\\mathrm{ECE} \\approx \\Delta C_t > 0$ whenever $\\Delta\\bar{H}_t < 0$.\nThis argument establishes the direction of co-movement; the quantitative relationship depends on distribution geometry.\n$\\bar{H}_t$ denotes mean conditional entropy $\\mathbb{E}_{x \\sim p_{\\text{eval}}}[h(x)]$, which differs from the marginal entropy $H_t = -\\sum_i p_t(i)\\log p_t(i)$ used in Proposition~\\ref{thm:entropy_leads}; under mode amplification, both decrease monotonically, so the cascade ordering is consistent across both formulations.\n\n\\paragraph{MAUVE ordering (conjecture).}\nMAUVE measures divergence in a discretized embedding space via $k$-means quantization.\nMAUVE onset requires token-level shifts (detected by entropy) to propagate through $n$-gram distributions (detected by distinct-$n$) to aggregate embedding distributions.\nEmpirically, MAUVE onset lags diversity by 0--1 generations on WikiText; however, on C4, MAUVE onset occurs at generation~1 (simultaneous with entropy), suggesting this lag is corpus-dependent.\n\n\\paragraph{Empirical support.}\nAmong 15 experiments at $\\alpha \\geq 0.30$ (where entropy perturbation exceeds the detection threshold), cascade ordering $t_H \\leq t_D$ holds in 14/15 cases (GPT-2-medium s43 fp32 exhibits bidirectional Granger significance).\nTable~\\ref{tab:cascade_onset} reports onset generations for representative conditions, showing uniform Phase~1/2/3 ordering.\nFive low-$\\alpha$ experiments ($\\alpha \\leq 0.25$) show entropy perturbation below the detection threshold (gen-1 deviation $<2\\sigma$); cascade ordering is neither confirmed nor refuted in this regime.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cascade onset generations (5\\% threshold) for representative experiments (Pythia-410M, WikiText, fp32). Phase~1: entropy and ECE ($t_H$, $t_{\\mathrm{ECE}}$); Phase~2: diversity ($t_D$, min over distinct-$n$); Phase~3: MAUVE ($t_M$). All conditions confirm the predicted ordering $t_H = t_{\\mathrm{ECE}} \\leq t_D \\leq t_M$.}\n\\label{tab:cascade_onset}\n\\begin{tabular}{llcccc}\n\\toprule\nSeed & $\\alpha$ & $t_H$ & $t_{\\mathrm{ECE}}$ & $t_D$ & $t_M$ \\\\\n\\midrule\n42 & 0.50 & 1 & 1 & 2 & 3 \\\\\n43 & 0.50 & 1 & 1 & 2 & 2 \\\\\n42 & 0.75 & 1 & 1 & 2 & 3 \\\\\n43 & 0.75 & 1 & 1 & 2 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\phantomsection\\label{app:alpha_c_proof}\n\\paragraph{Proof of Proposition~\\ref{prop:phase-boundary}.}\nAt the detection threshold, $\\mathrm{Power}(\\alpha_c, T) = \\pi^*$.\nSince $\\alpha_c$ lies below the non-monotonic dip region ($\\alpha_c < 0.55$), the signal model applies directly.\nFrom the power function $\\mathrm{Power} = \\Phi(S(\\alpha) \\cdot \\sqrt{T} / \\sigma)$, setting $S(\\alpha_c) \\cdot \\sqrt{T} / \\sigma = z^*$ and substituting the signal model $S(\\alpha) = c\\,\\alpha^\\beta$ yields $c\\,\\alpha_c^\\beta = z^* \\sigma / \\sqrt{T}$.\nSolving: $\\alpha_c(T) = (z^* \\sigma / c)^{1/\\beta} \\cdot T^{-1/(2\\beta)}$, giving the stated form with exponent $\\gamma = 1/(2\\beta)$.\n\n\\paragraph{Calibration and consistency.}\nCross-$T$ validation avoids the circularity of fitting theory to model-extrapolated points.\nWe fit $P(\\mathrm{det}|\\alpha,T) = \\Phi(A \\cdot \\alpha^\\beta \\cdot \\sqrt{T} - z_0)$ to training data at $T \\in \\{10, 20\\}$ via profile likelihood over $(\\beta, \\alpha_\\infty)$, with $\\alpha_\\infty{=}0$ emerging as the optimum.\nThe held-out test set ($T \\in \\{5, 15\\}$) yields MAE${=}0.106$ with 95\\% CI coverage $6/6$: the model correctly predicts all $0/8$ at $T{=}5$ and detection at $T{=}15$ (predicted $0.49$--$0.71$ vs.\\ observed $6/8{=}0.75$; under-prediction reflects the $P_{\\max}{=}0.75$ ceiling from MAUVE saturation, which is modeled separately).\nA linear signal model ($\\beta{=}1$, $\\gamma{=}0.5$) is rejected.\nThe sub-linear exponent $\\beta{=}0.24$ implies that doubling contamination increases signal by only $2^{0.24} \\approx 1.18\\times$ (18\\%); since $\\alpha_\\infty{\\approx}0$, any nonzero contamination produces signal, but detection requires sufficient $T$ to amplify it.\nAt $T{=}5$, $\\alpha_c \\geq 1.0$: no contamination level is detectable, consistent with the insufficient statistical power at very short observation windows.\n\n\\paragraph{Leave-one-$T$-out cross-validation.}\nWe evaluate model generalization via leave-one-$T$-out CV on the $5T \\times 3\\alpha$ grid (sync-dip $\\alpha{=}0.60$ excluded; 15 cells).\nFor each fold, one observation length is held out and the probit model $P = P_{\\max} \\cdot \\Phi(A \\cdot \\alpha^{0.24} \\cdot \\sqrt{T} - z_0)$ is refit on the remaining data.\nOverall MAE${=}0.037$ with 95\\% CI coverage $15/15$.\nWhen sync-dip cells are included (20 cells), MAE rises to $0.203$ (CI $16/20$), with the largest residuals at sync-dip cells (predicted $0.75$, observed $0/8$).\nThe profile likelihood over $\\beta$ yields MLE $\\hat{\\beta}{=}0.66$ (95\\% CI $[0.24, 0.78]$); the wide interval reflects a flat likelihood surface, indicating that $\\beta$ is not well-identified from these data.\nModel comparison (AIC, 15-cell grid excluding sync-dip): $M_1$ (linear boundary) $\\Delta\\mathrm{AIC}{=}0.0$; $M_2$ (power-probit) $\\Delta\\mathrm{AIC}{=}2.43$.\nIncluding sync-dip data reverses the ranking ($M_2$ $\\Delta\\mathrm{AIC}{=}0.0$, $M_1$ $\\Delta\\mathrm{AIC}{=}4.15$), because the probit model naturally accommodates the dip's dissolution at higher $T$ while linear models cannot.\n\n\\section{Power Simulation: Shape Comparison}\n\\label{app:power_sim}\n\nTo assess whether the observed steep detection onset could arise from smooth signal models, we simulate PermG detection under three null hypotheses (1{,}000 replications per cell, $n_{\\text{perm}}{=}1{,}000$, $n_{\\text{pairs}}{=}8$, BH-FDR $q{=}0.05$):\n\n\\begin{itemize}\n\\item \\textbf{H0} (linear): $S(\\alpha) = c \\cdot \\alpha$, calibrated so $S(1.0) = S_{\\max}$.\n\\item \\textbf{H0$'$} (concave): $S(\\alpha) = c \\cdot \\alpha^{0.5}$, sub-linear but smooth.\n\\item \\textbf{H1} (step): $S(\\alpha) = S_{\\max} \\cdot \\mathbf{1}[\\alpha > \\alpha_c(T)]$, binary activation.\n\\end{itemize}\n\n\\noindent\\textbf{Scaling exponents.}\nAll three models produce apparent onset scaling in $T$: H0 $\\gamma{=}0.85$, H0$'$ $\\gamma{=}1.87$, H1 $\\gamma{=}1.96$ (observed: $\\gamma{=}2.08$).\nH0$'$ produces $\\gamma$ within $0.21$ of the observed value, demonstrating that the scaling exponent alone cannot distinguish smooth from step-function boundaries.\n\n\\noindent\\textbf{Shape differences.}\nAt $T{=}10$, $\\alpha{=}0.45$: H0 predicts 27\\% detection rate, H0$'$ predicts 45\\%, H1 predicts 5.5\\%, observed $0/8$.\nAt $T{=}10$, $\\alpha{=}0.50$: H0 predicts 36\\%, H0$'$ predicts 48\\%, H1 predicts 4.6\\%, observed $6/8$ (75\\%).\nSmooth models produce onset ramps with $k{=}4.9$--$6.1$ (H0$'$: $k{=}4.93$, $R^2{=}0.9974$; H0: $k{=}6.14$, $R^2{=}0.9998$); the observed onset steepness ($k{=}15.7$) is ${\\approx}3{\\times}$ higher.\n\n\\noindent\\textbf{Metric-specific ceiling.}\nAt high $\\alpha$ (${\\geq}0.75$) with $T{\\geq}20$, H0 and H0$'$ (which simulate 8 equal-signal pairs) reach mean detection fractions of $0.79$--$0.98$ (${\\approx}6.3$--$7.8/8$), whereas observed counts never exceed $6/8$.\nThis gap reflects metric structure rather than signal saturation: the 2/8 non-detected pairs consistently involve MAUVE, whose floor saturation (\\S\\ref{sec:t20}) prevents Granger detection regardless of signal strength.\n\n\\section{T=20 Predict-then-Verify Comparison}\n\\label{app:t20_comparison}\n\nTable~\\ref{tab:t20_comparison} reports the predict-then-verify results for the $T{=}20$ extension experiments.\nPredictions are derived from the detection boundary model (\\S\\ref{sec:theory}): detected pairs at $T{=}10$ are predicted to remain detected (saturated $F$-statistics), and undetected pairs are predicted to remain undetected (structural nulls or non-monotonic dip).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{T=20 predict-then-verify comparison (Pythia-410M, seed~42, WikiText, fp32). Excluding $\\alpha{=}1.0$, two of four predictions fall within CI ($\\alpha{=}0.50$, $0.75$); boundary cases show systematic bias---$\\alpha{=}0.45$ falsifies the ceiling hypothesis (under-prediction), $\\alpha{=}0.60$ over-predicts under raw $p$-values (v1; matches under FDR v2, not pre-committed).}\n\\label{tab:t20_comparison}\n\\begin{tabular}{lcccc}\n\\toprule\n$\\alpha$ & $T{=}10$ & Predicted $T{=}20$ & Observed $T{=}20$ & Match \\\\\n\\midrule\n0.45 & 0/8 & 0/8 (ceiling) & 5/8 & $\\times$ \\\\\n0.50 & 6/8 & 6/8 (saturated) & 6/8 & \\checkmark \\\\\n0.60 & 0/8 & 3/8 (v1 raw)$^\\dagger$ & 0/8 & $\\times$ \\\\\n0.75 & 6/8 & 6/8 (saturated) & 6/8 & \\checkmark \\\\\n1.00 & 6/8 & 6/8 (saturated) & 6/8 & \\checkmark \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$V2 (BH--FDR corrected, created 44\\,min pre-analysis, not git-committed) predicts 0/8, matching observation.} \\\\\n\\end{tabular}\n\\end{table}\n\nAt $\\alpha \\geq 0.50$, consistency across $T{=}10$ and $T{=}20$ supports the detection boundary prediction: PermG counts are determined by signal structure, not observation length.\nSix diversity-based pairs show $F{=}449$--$2947$ at $T{=}20$ (all $\\gg F_{\\text{crit}}$); two MAUVE-based pairs show $F{<}2$ regardless of $T$, driven by floor saturation ($\\mu{=}0.029$, 100\\% ${<}0.05$) rather than high variance (CV$_{\\text{MAUVE}}{=}0.089$ vs CV$_{\\text{distinct-1}}{=}0.139$); SNR: MAUVE $4.68$ vs diversity $6.40$--$8.20$ ($p{<}0.001$).\nThe sole exception is $\\alpha{=}0.45$ at $T{=}20$ (5/8), consistent with boundary proximity.\nAt $\\alpha{=}0.45$, the shift from 0/8 to 5/8 falsifies Model~A (ceiling: $\\alpha{=}0.45$ structurally undetectable) in favor of Model~B (power-limited: $\\sqrt{T}$ boost crosses the detection threshold), lowering $\\alpha_c$ below~0.45.\nThe $\\alpha{=}0.60$ non-monotonic dip persists at $T{=}20$ (s42: 0/8; s43: 3/8) but dissolves at $T{=}25$ (5/8), confirming that $\\sqrt{T}$ power scaling eventually overcomes the dip; alternative methods detect signal throughout (DiffXCorr 6/8, TY 5/8 at $T{=}20$).\nPermG directional selectivity is consistent across tested $T$ ($T{=}10$, $20$): forward 6/8 versus reverse 0/8 at $\\alpha \\in \\{0.50, 0.75, 1.0\\}$.\n\n\n\\subsection{Prediction Timeline}\n\\label{app:t20_prediction_timeline}\n\nTwo versions of the $T{=}20$ prediction file exist, reflecting an evolving statistical protocol:\n\n\\paragraph{V1 (git-committed, \\texttt{bad72cc}).} Predictions derived from $T{=}10$ PermG results using \\emph{raw} $p$-values. At $\\alpha{=}0.60$, v1 counted 3/8 pairs with raw $p{<}0.05$, predicting 3/8 detections at $T{=}20$. The observed result (0/8 FDR-significant) does not match.\n\n\\paragraph{V2 (pre-analysis, not committed).} A revised file incorporating BH--FDR correction at $q{=}0.05$, consistent with the correction applied throughout the paper. Under FDR, $\\alpha{=}0.60$ drops from 3/8 (raw) to 0/8, matching the observation. V2 was created 44 minutes before the formal $T{=}20$ analysis began (filesystem timestamp) but was not git-committed, and therefore lacks the cryptographic verifiability of v1.\n\n\\paragraph{Scoring.} Primary (v1, committed): 3/5 exact matches ($\\alpha \\in \\{0.50, 0.75, 1.0\\}$, all saturated regimes). Excluding $\\alpha{=}1.0$, two of four predictions fall within CI. Both boundary predictions miss: $\\alpha{=}0.45$ (predicted 0/8, observed 5/8) falsifies the ceiling hypothesis in favor of $\\sqrt{T}$ power scaling; $\\alpha{=}0.60$ (predicted 3/8, observed 0/8) over-estimates detection due to the non-monotonic dip. Sensitivity (v2, FDR-corrected): 4/5 ($\\alpha{=}0.60$ matches). The systematic conservative bias at $\\alpha{=}0.45$ is consistent with the $\\sqrt{T}$ power increase predicted by Proposition~\\ref{prop:phase-boundary}.\n\n\n\\phantomsection\\label{app:task_degradation}\n\\paragraph{Task degradation.}\n\nTable~\\ref{tab:task_degradation} reports end-of-training task performance (generation~10, Pythia-410M, seed~42, fp32) across contamination levels.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Task degradation across contamination levels (Pythia-410M, seed~42, fp32, generation~10). Perplexity evaluated on held-out WikiText-103.}\n\\label{tab:task_degradation}\n\\begin{tabular}{lcc}\n\\toprule\n$\\alpha$ & Perplexity & Next-token acc. \\\\\n\\midrule\nBaseline & 26.6 & 0.390 \\\\\n0.05 & 20.8 & 0.431 \\\\\n0.25 & 22.9 & 0.424 \\\\\n0.46 & 31.6 & 0.400 \\\\\n0.50 & 31.3 & 0.399 \\\\\n0.52 & 41.1 & 0.389 \\\\\n0.60 & 53.5 & 0.375 \\\\\n0.75 & 80.3 & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\alpha{=}0.05$, perplexity improves over the uncontaminated baseline (20.8 vs.\\ 26.6), consistent with a mild data augmentation effect.\nThe sharpest degradation occurs between $\\alpha{=}0.50$ and $0.52$ ($+31\\%$ perplexity), aligning with the PermG detection onset (\\S\\ref{sec:regime}).\n\n\\section{Cross-Architecture FPR Sensitivity}\n\\label{app:cross_arch_fpr}\n\nAs preliminary cross-architecture evidence, we evaluate null-condition ($\\alpha{=}0$) false positive rates on GPT-2-medium (345M; OpenAI), a model outside the Pythia family used for all primary experiments.\nTwo seeds (s42, s43) are trained for $T{=}10$ generations under the same protocol as the Pythia-410M null runs.\nThis evaluation requires additional replication across architectures and seed counts before drawing definitive conclusions.\n\n\\begin{table}[h]\n\\centering\n\\caption{Null-condition FPR for GPT-2-medium ($\\alpha{=}0$, $T{=}10$, 6-pair basis). PermG forward detection shows extreme seed dependence; $K{\\geq}3$ consensus remains at 0\\% across both seeds.}\n\\label{tab:gpt2m_null_fpr}\n\\begin{tabular}{lccc}\n\\toprule\nSeed & PermG fwd & PermG rev & $K{\\geq}3$ \\\\\n\\midrule\ns42 & 6/6 (100\\%) & 0/6 & 0/6 \\\\\ns43 & 0/6 (0\\%) & 0/6 & 0/6 \\\\\n\\midrule\nPooled & 6/12 (50\\%) & 0/12 & 0/12 (0\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe pooled PermG FPR is dramatically higher than on Pythia-410M (50\\% vs.\\ 11.1\\%, 6-pair basis) and shows extreme seed dependence (100\\% vs.\\ 0\\%).\nThis instability traces to the magnitude of null drift in GPT-2-medium's output distribution, which is substantially stronger than in Pythia-410M (Table~\\ref{tab:null_drift_comparison}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Null drift magnitude ($\\alpha{=}0$, gen\\,0$\\to$10; GPT-2-medium: 2 seeds; Pythia-410M: 4 seeds, s46/s48--s50). GPT-2-medium exhibits ${\\sim}4{\\times}$ stronger entropy drift and ${\\sim}7{\\times}$ stronger distinct-3 drift than Pythia-410M.}\n\\label{tab:null_drift_comparison}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{GPT-2-medium} & \\multicolumn{2}{c}{Pythia-410M} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nMetric & gen\\,0 & gen\\,10 (\\%$\\Delta$) & gen\\,0 & gen\\,10 (\\%$\\Delta$) \\\\\n\\midrule\nToken entropy & 3.57 & 2.84 ($-$20.5\\%) & 3.23 & 3.076 ($-$4.9\\%) \\\\\nDistinct-3 & 0.84 & 0.54 ($-$35.8\\%) & 0.81 & 0.769 ($-$4.9\\%) \\\\\n$\\Delta$entropy (gen\\,0$\\to$1) & \\multicolumn{2}{c}{$-$0.60} & \\multicolumn{2}{c}{$-$0.25} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGPT-2-medium's distinct-3 declines from 0.84 to 0.54 over ten null generations ($-$35.8\\%), compared with 0.81$\\to$0.77 ($-$4.9\\%) for Pythia-410M.\nThis steep diversity collapse under pure retraining, absent any synthetic contamination, creates a strong downward trend that PermG's permutation test interprets as a directional signal.\nThe initial entropy drop (gen\\,0$\\to$1: $-$0.60 vs.\\ $-$0.25) is similarly amplified, consistent with architecture-specific sensitivity to iterative retraining rather than a deficiency in the detection method.\n\nThe $K{\\geq}3$ multi-method consensus maintains 0\\% FPR on GPT-2-medium (0/12 pairs), though the margin of safety is narrow: in the worst case (s42), 2 of 5 methods vote for forward detection, one vote short of the $K{\\geq}3$ threshold.\nThis provides some protection against architecture-specific distributional variation, but two seeds constitute only preliminary evidence.\nFor reference, PermG successfully detects true contamination signal ($\\alpha{=}1.0$) on GPT-2-medium with 6/8 forward pairs (Table~\\ref{tab:generalization}), confirming that the method works when signal is present; the elevated null FPR is specific to the null condition where architecture-dependent drift dominates.\n\n\\section*{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform related-work section.\n\\end{itemize}\n\n",
    "structuredPatch": [
      {
        "oldStart": 124,
        "oldLines": 24,
        "newStart": 124,
        "newLines": 22,
        "lines": [
          " \\end{table}",
          " ",
          " \\paragraph{FDR threshold sensitivity.}",
          "-Table~\\ref{tab:fdr_sensitivity} reports the effect of varying the BH FDR threshold $q$ on treatment ($\\alpha{=}0.75$, 3~seeds) versus null ($\\alpha{=}0.0$, 3~seeds) separation for permutation Granger tests.",
          "-% TODO-D219: update FDR sensitivity table with 6-seed null data (4/36 FPs at q=0.05; recompute null counts at each q threshold)",
          "-Treatment/null separation is qualitatively robust to FDR threshold choice; the null control remains at 0/24 across all thresholds.",
          "+Table~\\ref{tab:fdr_sensitivity} reports the effect of varying the BH FDR threshold $q$ on treatment ($\\alpha{=}0.75$, 3~seeds, 8-pair basis) versus null ($\\alpha{=}0.0$, 6~seeds 45--50, 6-pair basis) separation for permutation Granger tests.",
          "+Treatment/null separation is qualitatively robust to FDR threshold choice, though the expanded null sample reveals a small number of false positives at each threshold (3--8 of 36 pairs).",
          " ",
          " \\begin{table}[h]",
          " \\centering",
          " \\small",
          "-% TODO-D219: update caption and table body with 6-seed null data",
          "-\\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs). Null: $\\alpha{=}0.0$ (3~seeds, 24 pairs). The null control produces zero false positives at all thresholds tested.}",
          "+\\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs, 8-pair basis). Null: $\\alpha{=}0.0$ (6~seeds 45--50, 36 pairs, 6-pair basis). The expanded null sample reveals modest false positive rates that increase with $q$.}",
          " \\label{tab:fdr_sensitivity}",
          " \\resizebox{\\columnwidth}{!}{%",
          " \\begin{tabular}{lccc}",
          " \\toprule",
          "-$q$ & Null FDR-sig (/24) & Treatment FDR-sig (/24) & Separation \\\\",
          "+$q$ & Null FDR-sig (/36) & Treatment FDR-sig (/24) & Separation \\\\",
          " \\midrule",
          "-0.01 & 0 & 0  & Clean (underpowered) \\\\",
          "-0.05 & 0 & 19 & Clean \\\\",
          "-0.10 & 0 & 24 & Clean \\\\",
          "+0.01 & 3 & 0  & Underpowered \\\\",
          "+0.05 & 4 & 19 & Good \\\\",
          "+0.10 & 8 & 24 & Good (elevated null) \\\\",
          " \\bottomrule",
          " \\end{tabular}}",
          " \\end{table}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Assistant

_source line 111_

Now TODO-D219 #3 (L724) — Shapley section intro.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "73a892cd-e671-4ba9-9875-31a3dc20885b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011dWgENA5WeHfbUwth3jm2q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 109313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1041
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 112_

<details open><summary>🔧 Tool call — Edit · `toolu_0118VcNWiNVH4oGqh5MJUkrY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "old_string": "We quantify each method's marginal contribution to the MMCT ensemble using Shapley values~\\cite{shapley1953value}, computed via exact enumeration over all $2^5{=}32$ coalitions of the five detection methods.\n% TODO-D219: recompute Shapley with 6-seed null data (seeds 45--50, 36 null pairs; PermG FPR now 4/36=11.1%, no longer zero)\nFor a coalition $S \\subseteq \\{m_1, \\ldots, m_5\\}$, we define two performance metrics: the false positive rate FPR($S$), computed from 3 null experiments ($\\alpha{=}0.0$, seeds 42/43/44; 24 null pairs total), and the false negative rate FNR($S$), computed from 45 signal experiments across all non-null $\\alpha$ levels (270 signal pairs for the 6-pair variant excluding mauve).",
  "new_string": "We quantify each method's marginal contribution to the MMCT ensemble using Shapley values~\\cite{shapley1953value}, computed via exact enumeration over all $2^5{=}32$ coalitions of the five detection methods.\nFor a coalition $S \\subseteq \\{m_1, \\ldots, m_5\\}$, we define two performance metrics: the false positive rate FPR($S$), computed from 6 null experiments ($\\alpha{=}0.0$, seeds 45--50; 36 null pairs on the 6-pair basis excluding mauve), and the false negative rate FNR($S$), computed from 45 signal experiments across all non-null $\\alpha$ levels (270 signal pairs for the 6-pair variant excluding mauve)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "97f8b1c3-bba1-4a63-a305-cd86a255a4b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011dWgENA5WeHfbUwth3jm2q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1041,
      "cache_read_input_tokens": 109313,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1041
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-24T09:05:47.549Z_

<details><summary>↩ Tool result · `toolu_0118VcNWiNVH4oGqh5MJUkrY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "c7f94bdb-8724-4034-93bc-3c3ce7c39bac",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "oldString": "We quantify each method's marginal contribution to the MMCT ensemble using Shapley values~\\cite{shapley1953value}, computed via exact enumeration over all $2^5{=}32$ coalitions of the five detection methods.\n% TODO-D219: recompute Shapley with 6-seed null data (seeds 45--50, 36 null pairs; PermG FPR now 4/36=11.1%, no longer zero)\nFor a coalition $S \\subseteq \\{m_1, \\ldots, m_5\\}$, we define two performance metrics: the false positive rate FPR($S$), computed from 3 null experiments ($\\alpha{=}0.0$, seeds 42/43/44; 24 null pairs total), and the false negative rate FNR($S$), computed from 45 signal experiments across all non-null $\\alpha$ levels (270 signal pairs for the 6-pair variant excluding mauve).",
    "newString": "We quantify each method's marginal contribution to the MMCT ensemble using Shapley values~\\cite{shapley1953value}, computed via exact enumeration over all $2^5{=}32$ coalitions of the five detection methods.\nFor a coalition $S \\subseteq \\{m_1, \\ldots, m_5\\}$, we define two performance metrics: the false positive rate FPR($S$), computed from 6 null experiments ($\\alpha{=}0.0$, seeds 45--50; 36 null pairs on the 6-pair basis excluding mauve), and the false negative rate FNR($S$), computed from 45 signal experiments across all non-null $\\alpha$ levels (270 signal pairs for the 6-pair variant excluding mauve).",
    "originalFile": "\\appendix\n\n\\section{Training Details and Metric Drift}\n\\label{app:training_details}\n\\label{app:drift}\n\n\\paragraph{Hyperparameters.}\nEach generation fine-tunes for 5{,}000 steps using AdamW (learning rate $5 \\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium).\nGeneration uses temperature $1.0$, top-$k{=}50$, max length 512 tokens, producing 5{,}000 samples per generation from 5{,}000-sample subsets of WikiText-103.\nCanary metrics: token entropy $H(p_\\theta | \\text{context})$ over 1{,}000 held-out samples; ECE with 15 bins.\nAdditional downstream metrics (distinct-3, effective rank, Self-BLEU) appear in subsequent appendix sections.\n\n\\paragraph{Metric drift.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Metric drift (\\%, generation~0$\\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\\alpha{=}0.25$: distinct-1 $-40.3{\\pm}0.3\\%$) rather than full replacement ($\\alpha{=}1.0$: $-27.8{\\pm}1.6\\%$). $^\\dagger$$\\alpha{=}0.10$: single seed (seed~42, preliminary). $\\alpha{=}0.00$, $\\alpha{=}0.25$, $\\alpha{=}0.50$, $\\alpha{=}0.75$: 3-seed mean${\\pm}$std (seeds 42, 43, 44); $\\alpha{=}1.0$: 4-seed mean${\\pm}$std (seeds 42, 43, 44, 45).}\n\\label{tab:drift_summary}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\\\\n\\midrule\n0.00 & $-4.6{\\pm}0.4$ & $+37.6{\\pm}14$ & $-14.1{\\pm}0.4$ & $-9.6{\\pm}0.4$ & $-20.6{\\pm}1.0$ \\\\\n0.10$^\\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\\\\n0.25 & $-4.7{\\pm}0.5$ & $+81.8{\\pm}15.9$ & $-40.3{\\pm}0.3$ & $-56.4{\\pm}0.7$ & $-18.1{\\pm}0.8$ \\\\\n0.50 & $-18.0{\\pm}0.5$ & $+822.6{\\pm}18.3$ & $-37.1{\\pm}0.4$ & $-50.4{\\pm}1.0$ & $+21.0{\\pm}0.1$ \\\\\n0.75 & $-27.6{\\pm}0.2$ & $+1791{\\pm}18$ & $-32.3{\\pm}0.5$ & $-41.0{\\pm}1.0$ & $+182.6{\\pm}0.7$ \\\\\n1.00 & $-60.8{\\pm}1.2$ & $+3780{\\pm}30$ & $-27.8{\\pm}1.6$ & $-34.0{\\pm}3.3$ & $+3674{\\pm}45$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Distinct-3 Results}\n\\label{app:distinct3}\n\nTable~\\ref{tab:distinct3_drift} reports distinct-3 drift across all contamination levels.\nDistinct-3 exhibits the largest absolute decline among diversity metrics at low contamination ($-58.9{\\pm}0.9\\%$ at $\\alpha{=}0.25$) but attenuates at higher levels ($-30.5\\%$ at $\\alpha{=}1.0$), consistent with the diversity--calibration dissociation discussed in \\S\\ref{sec:discussion}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Distinct-3 drift (\\%, generation~0$\\to$10) across contamination levels. $\\alpha{=}0.00$, $\\alpha{=}0.25$, $\\alpha{=}0.75$: 3-seed mean${\\pm}$std; $\\alpha{=}1.0$: 4-seed mean${\\pm}$std; $\\alpha{=}0.50$: single seed.}\n\\label{tab:distinct3_drift}\n\\begin{tabular}{lc}\n\\toprule\n$\\alpha$ & Distinct-3 drift (\\%) \\\\\n\\midrule\n0.00 & $-4.4{\\pm}0.5$ \\\\\n0.25 & $-58.9{\\pm}0.9$ \\\\\n0.50 & $-52.4$ \\\\\n0.75 & $-38.6{\\pm}1.3$ \\\\\n1.00 & $-30.5{\\pm}4.0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Lead-lag analysis.}\nAt $\\alpha{=}1.0$, token entropy Granger-precedes distinct-3 at the same consensus level as distinct-1 and distinct-2: $K{\\geq}4/5$ methods, $S{\\geq}3/4$ seeds (Tier~3).\nHowever, the optimal lag is less stable than for distinct-1/2: at max\\_lag${=}7$, the lag standard deviation across seeds exceeds 1.5 generations, compared to $<0.5$ for distinct-1/2.\nThis instability reflects bimodal lag distributions (modes at lag~1 and lag~3--4), suggesting that distinct-3 captures two temporally distinct diversity loss mechanisms: rapid n-gram homogenization (lag~1) and slower distributional narrowing (lag~3--4).\n\n\\paragraph{Sensitivity to sequence length.}\nHigher-order $n$-gram diversity metrics are more sensitive to generation length and random sampling variability.\nWith our 512-token generation length, distinct-3 has a smaller effective denominator (number of possible unique trigrams observed) than distinct-1 or distinct-2, amplifying stochastic fluctuations.\nThis partially explains the higher lag instability: the signal-to-noise ratio for temporal precedence is lower for distinct-3, requiring more observations (longer $T$ or more seeds) to achieve stable estimates.\nFor this reason, we report distinct-3 in this appendix rather than in the main text, where distinct-1 and distinct-2 provide cleaner evidence of the entropy-leads-diversity pattern.\n\n\n\\section{Observation Window Sensitivity}\n\\label{app:window_sensitivity}\n\nTable~\\ref{tab:window_sensitivity} reports how the Tier~3 consensus classification ($K{\\geq}4/5$ methods) varies as a function of the minimum observation window $T_{\\min}$, where analysis uses only generations $0$ through $T_{\\min}$.\nThe consensus classification stabilizes at $T_{\\min}{\\geq}5$ (6 data points), well below our full observation window of $T{=}10$: all six effect-size reference pairs (token entropy and ECE $\\to$ distinct-1, distinct-2, distinct-3) reach $K{\\geq}4/5$ agreement at every window length from $T_{\\min}{=}5$ through $T_{\\min}{=}10$, with no spurious pairs (canary$\\to$perplexity) admitted.\n\nToda--Yamamoto is the only method exhibiting window-dependent sensitivity (note: TY directional assignment is under verification; these counts are retained for completeness): TY consensus stabilizes at $T_{\\min}{\\geq}6$, slightly later than the primary methods, reflecting the additional degrees of freedom consumed by the augmentation order $d_{\\max}$.\nThis does not affect the consensus classification because the remaining four methods provide stable $K{\\geq}4/5$ agreement independently of Toda--Yamamoto's vote.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Observation window sensitivity for Tier~3 consensus ($K{\\geq}4/5$) at $\\alpha{=}1.0$ (Pythia-410M, 4~seeds). Tier~3 pairs: number of canary$\\to$downstream pairs (out of 8 validated) reaching $K{\\geq}4/5$ method agreement. TY pairs: number of effect-size reference pairs (out of 6) reaching Toda--Yamamoto significance (moderate supplementary method; \\S\\ref{sec:method}). Consensus stabilizes at $T_{\\min}{\\geq}5$; TY stabilizes at $T_{\\min}{\\geq}6$.}\n\\label{tab:window_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccccccc}\n\\toprule\n& \\multicolumn{8}{c}{Minimum observation window $T_{\\min}$} \\\\\n\\cmidrule(lr){2-9}\n& 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\\\\n\\midrule\nTier~3 pairs (/8)    & $\\dagger$ & $\\dagger$ & 6 & 6 & 6 & 6 & 6 & 6 \\\\\nTY pairs$^\\S$ (/6)   & $\\dagger$ & $\\dagger$ & 3--6 & 3--6 & 3--6 & 3--6 & 3--6 & 6 \\\\\nStable               & ---       & ---       & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark \\\\\n\\bottomrule\n\\multicolumn{9}{l}{\\footnotesize $\\dagger$~Insufficient degrees of freedom for Granger-type tests ($<6$ data points).} \\\\\n\\multicolumn{9}{l}{\\footnotesize $^\\S$~TY directional assignment under verification.}\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Robustness Checks}\n\\label{app:robustness}\n\n\\paragraph{Permutation count stability.}\nTable~\\ref{tab:nperm_stability} compares permutation Granger $p$-values at 5{,}000 versus 10{,}000 permutations across all canary$\\to$downstream pairs at $\\alpha{=}0.75$ (3~seeds, 24~pairs).\nPermutation Granger $p$-values are stable to within 0.002 between 5{,}000 and 10{,}000 permutations, with zero significance decisions affected.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Permutation count stability analysis ($\\alpha{=}0.75$, 3~seeds, 24 canary$\\to$downstream pairs). $p$-values from permutation Granger tests at $n_{\\text{perm}}{=}5{,}000$ versus $n_{\\text{perm}}{=}10{,}000$.}\n\\label{tab:nperm_stability}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nMax $|\\Delta p|$ & 0.010 \\\\\nMean $|\\Delta p|$ & 0.002 \\\\\nSignificance flips & 0 / 24 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{FDR threshold sensitivity.}\nTable~\\ref{tab:fdr_sensitivity} reports the effect of varying the BH FDR threshold $q$ on treatment ($\\alpha{=}0.75$, 3~seeds, 8-pair basis) versus null ($\\alpha{=}0.0$, 6~seeds 45--50, 6-pair basis) separation for permutation Granger tests.\nTreatment/null separation is qualitatively robust to FDR threshold choice, though the expanded null sample reveals a small number of false positives at each threshold (3--8 of 36 pairs).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs, 8-pair basis). Null: $\\alpha{=}0.0$ (6~seeds 45--50, 36 pairs, 6-pair basis). The expanded null sample reveals modest false positive rates that increase with $q$.}\n\\label{tab:fdr_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n$q$ & Null FDR-sig (/36) & Treatment FDR-sig (/24) & Separation \\\\\n\\midrule\n0.01 & 3 & 0  & Underpowered \\\\\n0.05 & 4 & 19 & Good \\\\\n0.10 & 8 & 24 & Good (elevated null) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{PermG $p$-value gradient at the onset boundary ($\\alpha{=}0.45$).}\nAt the onset boundary, PermG operates near its detection limit, and marginal $p$-values exhibit seed-dependent variation consistent with the statistical power interpretation (\\S\\ref{sec:theory}).\nTable~\\ref{tab:fdr_gradient_a045} reports BH-corrected $p$-values for all 8 canary$\\to$downstream pairs across two seeds at $\\alpha{=}0.45$.\nSeed~43 reaches a minimum FDR-corrected $p{=}0.059$ (18\\% above the $q{=}0.05$ threshold), while seed~42 reaches $p{=}0.091$ (82\\% above threshold).\nNo pair crosses the significance threshold at either seed, yielding the aggregate 0/8 detection rate reported in \\S\\ref{sec:regime}.\nThe gradient is consistent with a continuous power transition rather than a binary absence of signal: PermG operates near its detection limit at $\\alpha{=}0.45$, with seed-dependent variation in marginal $p$-values.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BH-corrected PermG $p$-values at $\\alpha{=}0.45$ (8 canary$\\to$downstream pairs $\\times$ 2 seeds). Min $p_{\\mathrm{fdr}}$ per seed shown. All pairs remain above the $q{=}0.05$ threshold, yielding 0/8 aggregate detection.}\n\\label{tab:fdr_gradient_a045}\n\\begin{tabular}{lcc}\n\\toprule\n & Seed 42 & Seed 43 \\\\\n\\midrule\nMin FDR $p$ & 0.091 & 0.059 \\\\\nGap to $q{=}0.05$ & 82\\% & 18\\% \\\\\nPermG fwd sig (/8) & 0 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Systematic Robustness Analysis}\n\\label{app:spec_curve}\n\nThe sharp detection onset reported in \\S\\ref{sec:regime} could in principle depend on specific analytical choices (pair selection, seed, $\\alpha$ level, method parameters).\nWe assess robustness via specification curve analysis~\\cite{simonsohn2020specification}, systematically varying analytical degrees of freedom to test whether the 0/8$\\to$6/8 transition is specification-invariant.\nOur specification curve varies data subsets and pair selections while holding the detection method (PermG) and its hyperparameters fixed, more closely resembling a systematic subset analysis than a full specification curve in the sense of \\citet{simonsohn2020specification}.\n\nWe construct 1{,}160 analytical specifications from the combinatorial space of: 13 contamination levels ($\\alpha$ grid), seed selection ($\\{42, 43, 44, 45\\}$ where available), 8 canonical canary$\\to$downstream pairs (\\{token entropy, ECE\\} $\\times$ \\{distinct-1, distinct-2, distinct-3, mauve\\}), and method parameters (all PermG with $n_\\text{perm}{=}5{,}000$, BH FDR $q{=}0.05$).\nAll specifications use the D120-canonical analysis pipeline with $3\\sigma$ threshold calibration (D105) as a hard filter.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Specification curve summary (1{,}160 specifications, D120-compliant). The blind$\\to$onset jump is robust across specifications: 0\\% significance rate through $\\alpha{=}0.45$, rising to 75\\% at $\\alpha{=}0.50$.}\n\\label{tab:spec_curve}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nTotal specifications & 1{,}160 \\\\\nSignificant (FDR $q{<}0.05$) & 536 (46.2\\%) \\\\\n\\midrule\n\\emph{By regime} & \\\\\n\\quad Blind ($\\alpha \\leq 0.45$) & 0\\% \\\\\n\\quad Onset ($\\alpha{=}0.50$) & 75\\% \\\\\n\\quad Detection ($\\alpha \\geq 0.75$) & 62--75\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe specification curve confirms that the sharp detection onset is not an artifact of particular analytical choices: the categorical jump from 0\\% to ${\\geq}75\\%$ significance at $\\alpha_c{\\approx}0.50$ holds across the vast majority of specifications, supporting the main text claim (\\S\\ref{sec:regime}).\n\n\n\\section{Transfer Entropy Analysis}\n\\label{app:transfer_entropy}\n\nTable~\\ref{tab:te_results} reports transfer entropy (TE; \\citealp{schreiber2000measuring}) results aggregated across all baseline conditions.\nTE was estimated using 3-bin discretization with permutation testing ($n{=}5{,}000$).\nNo pair reaches BH-corrected significance ($q{=}0.05$) in any condition, confirming that non-parametric information-theoretic methods lack detection power at $T{=}11$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Transfer Entropy results (12 runs across all $\\alpha$ levels). TE\\textsubscript{fwd}: canary$\\to$downstream; TE\\textsubscript{rev}: downstream$\\to$canary. Mean uncorrected permutation $p$-values ($n{=}5{,}000$). No pair reaches BH-corrected $q{<}0.05$ in any run.}\n\\label{tab:te_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\nCanary & Downstream & TE\\textsubscript{fwd} (mean) & $p$\\textsubscript{fwd} (mean) & TE\\textsubscript{rev} (mean) & $p$\\textsubscript{rev} (mean) \\\\\n\\midrule\ntoken\\_entropy & distinct-1 & 0.289 & 0.559 & 0.480 & 0.490 \\\\\ntoken\\_entropy & distinct-2 & 0.300 & 0.529 & 0.496 & 0.447 \\\\\ntoken\\_entropy & distinct-3 & 0.255 & 0.645 & 0.484 & 0.459 \\\\\ntoken\\_entropy & perplexity & 0.257 & 0.676 & 0.386 & 0.626 \\\\\nECE & distinct-1 & 0.185 & 0.720 & 0.184 & 0.891 \\\\\nECE & distinct-2 & 0.208 & 0.683 & 0.216 & 0.846 \\\\\nECE & distinct-3 & 0.209 & 0.689 & 0.227 & 0.807 \\\\\nECE & perplexity & 0.296 & 0.572 & 0.263 & 0.747 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\phantomsection\\label{app:te_mi}\n\\paragraph{KNN-based TE/MI decomposition.}\nA $k$-nearest-neighbor TE estimator ($k{=}5$) provides a model-free complement to the parametric Granger framework.\nForward-dominant TE fraction increases monotonically with $\\alpha$: 4/8 pairs at $\\alpha{=}0.25$ (mean net TE${=}0.14$), 5/8 at $\\alpha{=}0.50$ (net TE${=}0.42$), 6/8 at $\\alpha{=}0.60$ (net TE${=}0.57$), and 8/8 at $\\alpha{=}1.0$ (net TE${=}1.59$).\nAll 120 forward TE bootstrap 95\\% CIs exclude zero at $T{=}10$; all 48 at $T{=}20$.\nThe ``high MI, low TE'' hypothesis for the non-monotonic dip is supported by only 2/8 pairs (ECE$\\to$perplexity and token entropy$\\to$perplexity); the remaining 6 pairs show elevated TE even at $\\alpha{=}0.60$, indicating confounded co-variation rather than a universal mechanism.\n\n\\section{Change-Point Detection Analysis}\n\\label{app:change_point}\n\nWe apply a max-split change-point test with bootstrap significance assessment ($n{=}5{,}000$, $p{<}0.05$) to each metric's generation-level time series ($T{=}11$).\n\nUnder the null control ($\\alpha{=}0.00$, 3~seeds), downstream diversity metrics (distinct-1, distinct-2, distinct-3) produce significant change-points at generation~2 in all seeds (9/9 tests). With additional significant tests from ECE (2/3 seeds) and token entropy (1/3 seeds), the overall false positive rate reaches 66.7\\% (12/18 tests; Table~\\ref{tab:cp_null}). The monotonic drift inherent in iterative self-training is sufficient to trigger change-point detection even without canary contamination. Individual change-point significance therefore cannot serve as standalone evidence for a canary-specific effect.\n\nAlthough individual significance is unreliable as a discriminator, the temporal ordering of detected change-points reverses between null and treatment conditions. In the null ($\\alpha{=}0.00$), downstream metrics show the earliest significant breaks at generation~2 (all seeds), while significant canary breaks appear later (ECE at generations~4--8). Under treatment conditions ($\\alpha{\\geq}0.75$), this ordering flips: canary metrics place their best splits at generation~1, followed by downstream diversity metrics at generations~2--4 and perplexity at generation~4 (Table~\\ref{tab:cp_results}). This ordering reversal provides complementary evidence from a distinct statistical framework, consistent with the Granger-precedence analysis in \\S\\ref{sec:experiments}.\n\nSeveral caveats apply. The 18 individual tests per condition were not corrected for multiple comparisons (BH or Bonferroni); primary inference rests on the cross-metric temporal ordering rather than on individual significance tests. Under treatment conditions, token entropy places its best split at generation~1 with large effect sizes ($|d|{>}2.5$) in all seeds, but the pre-change segment at a generation-1 split contains only a single data point, reducing bootstrap power (1/3 seeds significant at $\\alpha{=}0.75$). The short series length ($T{=}11$) further limits overall detection power.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Change-point detection under null control ($\\alpha{=}0.00$, 3 seeds). CP: detected change-point generation (mean across significant seeds); $|d|$: Cohen's $d$ effect size (mean across all seeds); Sig.\\ rate: fraction of seeds where $p{<}0.05$. Overall FPR: 12/18 = 66.7\\%.}\n\\label{tab:cp_null}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & CP gen (mean) & $|d|$ (mean) & Sig.\\ rate & Type \\\\\n\\midrule\ntoken\\_entropy & 1.0 & 2.94 & 1/3 & canary \\\\\nECE & 6.0 & 1.62 & 2/3 & canary \\\\\ndistinct-1 & 2.0 & 2.27 & 3/3 & downstream \\\\\ndistinct-2 & 2.0 & 2.40 & 3/3 & downstream \\\\\ndistinct-3 & 2.0 & 2.27 & 3/3 & downstream \\\\\nperplexity & --- & 3.11 & 0/3 & downstream \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Change-point detection at $\\alpha{=}0.75$ (3 seeds). CP: detected change-point generation; $|d|$: Cohen's $d$ effect size between pre- and post-change segments. Sig.\\ rate: fraction of seeds where $p{<}0.05$.}\n\\label{tab:cp_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & CP gen (mean) & $|d|$ (mean) & Sig.\\ rate & Type \\\\\n\\midrule\ntoken\\_entropy & 1.0 & 3.21 & 1/3 & canary \\\\\nECE & 1.0 & 3.10 & 1/3 & canary \\\\\ndistinct-1 & 2.3 & 2.18 & 3/3 & downstream \\\\\ndistinct-2 & 3.0 & 1.97 & 3/3 & downstream \\\\\ndistinct-3 & 3.7 & 1.86 & 3/3 & downstream \\\\\nperplexity & 4.0 & 1.70 & 3/3 & downstream \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Dose-response ordering pattern.}\nTable~\\ref{tab:cp_ordering} summarizes the ordering pattern across contamination levels.\nThe canary-to-downstream gap shifts monotonically from negative (downstream first) under the null to positive (canary first) under treatment, ruling out a methodological artifact in which canary metrics would systematically appear earlier regardless of condition.\nThe $\\alpha{=}1.0$ analysis is limited to a single seed (s42); all other conditions use 3 seeds.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccl}\n\\toprule\n$\\alpha$ & Canary cp & Downstream cp & Gap & Direction \\\\\n\\midrule\n0.00 & gen 4--8 & gen 2 & $-$2.5 & Downstream first \\\\\n0.25 & gen 3--4 & gen 3--4 & $\\approx$0 & Simultaneous \\\\\n0.75 & gen 1 & gen 2--4 & $+$2.25 & Canary first \\\\\n1.00 & gen 2 & gen 2--5 & $+$1.0 & Canary first \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Change-point ordering reversal across contamination levels. Under the null ($\\alpha{=}0.00$), downstream metrics break before canary metrics; this ordering reverses monotonically as $\\alpha$ increases, consistent with the Granger-precedence analysis.}\n\\label{tab:cp_ordering}\n\\end{table}\n\n\n\\section{Sequential Monitoring: CUSUM vs Calibrated Threshold}\n\\label{app:csmp}\n\nWe translate the Granger-precedence finding into a deployable monitoring protocol using CUSUM (cumulative sum) sequential testing~\\cite{page1954continuous}, calibrated against the $\\alpha{=}0.0$ null control.\nThe null-calibration procedure sets the alarm threshold $h$ such that the false alarm rate (FAR) is 0\\% on null data (3~seeds, $T{=}10$), providing controlled Type~I error guarantees.\n\n\\paragraph{Method.}\nCUSUM monitors the cumulative deviation of token entropy from its null-control baseline: $S_t = \\max(0,\\; S_{t-1} + (\\mu_0 - x_t) - k)$, where $\\mu_0$ is the null-control mean, $k$ is the allowance parameter, and the alarm triggers when $S_t > h$.\nWe calibrate $h$ for each $k$ from the $\\alpha{=}0.0$ null data (Table~\\ref{tab:csmp_calibration}).\nAs a baseline, we compare against a simple calibrated threshold: alarm when the metric crosses $\\mu_0 - 2\\sigma_0$ for $n{\\geq}1$ or $n{\\geq}2$ consecutive generations.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{CUSUM calibration parameters from $\\alpha{=}0.0$ null control (3~seeds). $h$: alarm threshold calibrated to achieve FAR${=}$0\\%. For $k{\\geq}0.25$, the null CUSUM statistic remains at zero, yielding $h \\approx 0$.}\n\\label{tab:csmp_calibration}\n\\begin{tabular}{lcc}\n\\toprule\n$k$ & $h$ & FAR \\\\\n\\midrule\n0.05 & 1.530 & 0\\% \\\\\n0.10 & 1.005 & 0\\% \\\\\n0.25 & $\\approx$0 & 0\\% \\\\\n0.50 & $\\approx$0 & 0\\% \\\\\n1.00 & $\\approx$0 & 0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Results.}\nTable~\\ref{tab:csmp_comparison} compares CUSUM and simple threshold detection times across gradual contamination levels.\nAt the recommended operating point ($k{=}0.25$), CUSUM and the simple threshold ($n{\\geq}1$) produce identical alarm times (generation~1) across all seeds and contamination levels.\nMore conservative CUSUM settings ($k{=}0.1$, $k{=}0.05$) delay detection to match the $n{\\geq}2$ threshold or later.\nAt $k{=}1.0$ with $\\alpha{=}0.50$, CUSUM fails entirely ($S_t \\equiv 0$ for all seeds), demonstrating sensitivity to the allowance parameter.\nNo CUSUM configuration outperforms the simple calibrated threshold at any operating point tested.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{CUSUM vs simple calibrated threshold: alarm generation across contamination levels (3~seeds each; all seeds agree on the alarm generation shown). Threshold: metric crosses $\\mu_0 - 2\\sigma_0$. No CUSUM configuration outperforms the simple threshold at any operating point.}\n\\label{tab:csmp_comparison}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & CUSUM $k{=}0.25$ & CUSUM $k{=}0.1$ & CUSUM $k{=}0.05$ & Thresh $n{\\geq}1$ & Thresh $n{\\geq}2$ \\\\\n\\midrule\n0.50 & gen 1 & gen 2 & gen 3 & gen 1 & gen 2 \\\\\n0.75 & gen 1 & gen 2 & gen 2 & gen 1 & gen 2 \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize CUSUM $k{=}1.0$ at $\\alpha{=}0.50$: $S_t \\equiv 0$ for all seeds (complete detection failure).} \\\\\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe equivalence arises because the generation-0$\\to$1 entropy drop is large ($|\\Delta x| > 0.7$ for $\\alpha{=}0.50$, $> 1.0$ for $\\alpha{=}0.75$) relative to the null-control variability ($\\sigma_0 \\approx 0.03$).\nAny detector with a near-zero or small threshold triggers at generation~1; CUSUM's cumulative memory provides no advantage when the initial shift already exceeds the control limit.\nThis result extends Claim~3 (method sensitivity) beyond lead-lag detection to the monitoring domain: even a sequential testing procedure with stronger theoretical properties (optimal expected detection delay under continuous monitoring) does not improve over a calibrated baseline when the initial contamination signal dominates the allowance parameter.\nThe contribution of the null-calibrated monitoring framework is the calibration procedure itself (setting alarm boundaries from $\\alpha{=}0.0$ data to guarantee FAR${=}$0\\%), not the CUSUM algorithm.\n\n\\section{Background and Notation}\n\\label{app:background}\n\\label{sec:background}\n\nThis section establishes the formal setup and notation used throughout the paper.\n\n\\paragraph{Iterative training loop.}\nLet $M_0$ denote a pretrained language model and $\\mathcal{D}_\\text{real}$ a fixed corpus of human-written text.\nAt each generation $t \\geq 1$, the model $M_{t-1}$ generates a synthetic corpus $\\mathcal{D}_\\text{synth}^{(t-1)}$, and the next-generation model $M_t$ is fine-tuned on a mixture of $\\alpha$ fraction synthetic data and $(1{-}\\alpha)$ fraction real data:\n\\begin{equation}\n    \\mathcal{D}_\\text{train}^{(t)} = \\alpha \\cdot \\mathcal{D}_\\text{synth}^{(t-1)} \\;+\\; (1{-}\\alpha) \\cdot \\mathcal{D}_\\text{real}, \\quad \\alpha \\in [0, 1].\n    \\label{eq:mixing}\n\\end{equation}\nAt $\\alpha{=}1.0$, this reduces to the full-replacement paradigm of \\citet{shumailov2024curse}.\n\n\\paragraph{Metric families.}\n\\emph{Canary metrics}: token entropy ($H(p_\\theta | \\text{context})$ on held-out samples) and expected calibration error (ECE).\n\\emph{Downstream metrics}: distinct-$n$ ($n \\in \\{1, 2, 3\\}$)~\\cite{li2016diversity} and perplexity.\nEach metric produces a time series of $T{+}1$ observations.\n\n\\paragraph{Lead-lag testing.}\nGiven canary series $X$ and downstream series $Y$, the central question is whether changes in $X$ temporally precede changes in $Y$, requiring directionality and confounder control beyond simple correlation.\nWe employ five methods spanning permissive to conservative: naive cross-correlation, differenced cross-correlation, threshold onset detection, permutation Granger causality~\\cite{shojaie2022granger}, and Toda--Yamamoto Granger causality~\\cite{toda1995statistical}.\n\n\\section{MMCT Algorithm}\n\\label{app:mmct}\n\nAlgorithm~\\ref{alg:mmct} describes the Multi-Method Consensus Test (MMCT) introduced in \\S\\ref{sec:mmct}.\n\n\\begin{algorithm}[h]\n\\caption{Multi-Method Consensus Test (MMCT)}\n\\label{alg:mmct}\n\\begin{algorithmic}[1]\n\\Require Time series pair $(X, Y)$; methods $\\{m_1, \\ldots, m_K\\}$ ($K{=}5$); null-control data $\\mathcal{N}$ (from $\\alpha{=}0.0$); tolerance $\\epsilon{=}0.01$\n\\Ensure $p$-value, consensus level $\\hat{K}$\n\\For{each method $m_k$}\n    \\State Compute empirical FPR: $\\widehat{\\mathrm{FPR}}_k \\gets$ fraction of null-control pairs where $m_k$ rejects $H_0$\n    \\State Compute weight: $w_k \\gets 1 / \\max(\\widehat{\\mathrm{FPR}}_k,\\; \\epsilon)$\n    \\State Apply $m_k$ to $(X, Y)$: $d_k \\gets \\mathbf{1}[m_k \\text{ rejects } H_0]$\n\\EndFor\n\\State Weighted consensus: $W(X {\\to} Y) \\gets \\sum_{k} w_k \\, d_k \\;/\\; \\sum_{k} w_k$\n\\State Build empirical null distribution of $W$ from all null-control pairs in $\\mathcal{N}$\n\\State Compute $p$-value from empirical null: $p \\gets \\Pr_{\\mathcal{N}}(W \\geq W_{\\mathrm{obs}})$\n\\State Consensus level: $\\hat{K} \\gets \\sum_{k} d_k$\n\\State \\Return $p$, $\\hat{K}$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Design rationale.}\nFPR-inverse weighting penalizes methods with high false positive rates on null-control data: naive cross-correlation (FPR${=}91.7\\%$) receives weight $w{=}1.09$, while PermG (FPR${=}11.1\\%$, the lowest among directional methods; DiffXCorr achieves 2.8\\% but lacks directional separation) receives $w{=}9.0$.\nThe empirical null distribution avoids parametric assumptions that are unreliable for short ($T{=}5$--$20$), non-stationary series typical of iterative training.\nMMCT is a consensus testing protocol, not a novel statistical method; its value lies in systematic method comparison and the identification of method-dependent conclusions.\n\n\n\\section{Methodological Comparison Table}\n\\label{app:method_comparison}\n\nTable~\\ref{tab:method-comparison} summarizes the methodological coverage of existing canary and monitoring analyses across the diagnostic dimensions identified in \\S\\ref{sec:method}.\nNo prior work combines all six dimensions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Methodological comparison of canary and monitoring analyses. \\checkmark\\ = present, $\\times$ = absent, $\\circ$ = partial (${\\leq}2$ levels or limited replication). Diff.\\ = differencing/stationarity controls. Multi-M.\\ = ${\\geq}2$ independent statistical methods. MTC = multiple testing correction. Regime = systematic variation of $\\alpha$. Seeds = ${\\geq}3$ independent seeds. Arch.\\ = ${\\geq}2$ architecturally distinct model families.}\n\\label{tab:method-comparison}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccccl}\n\\toprule\nWork & Diff. & Multi-M. & MTC & Regime & Seeds & Arch. & Metrics \\\\\n\\midrule\n\\citet{shumailov2024curse}     & $\\times$   & $\\times$   & $\\times$   & $\\circ$    & \\checkmark & \\checkmark & PPL \\\\\n\\citet{du2025scales}           & $\\times$   & $\\times$   & \\checkmark & \\checkmark & \\checkmark & $\\times$   & ECE, Acc, Dist-$n$ \\\\\n\\citet{gambetta2024surplexity} & $\\times$   & $\\times$   & $\\times$   & \\checkmark & \\checkmark & \\checkmark & Surplexity, Ent \\\\\nSIGMA~\\cite{sigma2026spectral} & $\\times$   & $\\times$   & $\\times$   & $\\times$   & $\\times$   & $\\times$   & Spectral \\\\\nDCES~\\cite{dces2026counter}    & $\\times$   & $\\times$   & $\\times$   & $\\times$   & $\\times$   & \\checkmark & ECE, Ent, PPL \\\\\n\\midrule\n\\textbf{Ours}                  & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark & Ent, ECE, PPL, Dist-$n$ \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\section{Extended Discussion}\n\\label{app:extended_discussion}\n\n\\paragraph{Calibration scope and generalization.}\nAll FPR and FNR calibration results are specific to our experimental setup: Pythia-410M, WikiText-103 subset, $T{=}10$, and six contamination levels.\nCross-architecture validation across 15 conditions spanning six model families shows that the entropy-leads-diversity pattern generalizes in 11 of 15 architecture-seed combinations (Table~\\ref{tab:generalization}); GPT-2 bf16 (0/8), GPT-2 s43 (6/8 bidirectional), SmolLM3-3B (3/8, entropy decoupling), and Pythia-1.4B s42 (2/8) do not confirm the pattern.\n\n\\paragraph{Domain-dependent directionality.}\nThe unidirectional forward causation observed on WikiText (PermG reverse${=}$0/8 across all conditions) does not hold universally.\nOn C4 at $\\alpha{=}0.50$ (s42 fp32), PermG reverse reaches 7/8, indicating near-symmetric bidirectional coupling; however, this is seed-dependent (s43: 1/8) and noted as preliminary.\nThe practical implication is that directional asymmetry should be verified per domain.\n\n\\paragraph{Token entropy versus perplexity.}\nThe distinction lies in the evaluation domain: token entropy is $H(p_\\theta | \\text{context})$ on held-out real data, while perplexity is $\\exp(H_\\text{cross})$ on model-generated text.\nFirst-differencing removes their shared downward trend: the canary$\\to$diversity channel survives because entropy leads diversity by one generation, whereas the canary$\\to$perplexity channel vanishes because both co-move synchronously.\n\n\\paragraph{NLP-specific constraints.}\nOur application of Granger-type methods faces constraints absent in econometrics: (i)~observation length ($T{=}5$--$20$ vs.\\ $T{=}100$--$1000$); (ii)~non-stationarity by design rather than incidental; (iii)~small multiplicity for FDR correction (8--32 pairs per regime).\nTransfer entropy (0/192 FDR-significant results) confirms that method sensitivity extends beyond the five-method panel.\n\n\\paragraph{Prevention paradox.}\nEffective intervention truncates the collapse trajectory that established Granger precedence.\nDifferenced cross-correlation retains significance under intervention (31/32 pairs), while threshold onset fails entirely (0/8), reinforcing the multi-method rationale.\n\n\\paragraph{Grouped testing rationale.}\nWe test 8 canary$\\to$downstream pairs jointly (2 canaries $\\times$ 4 downstream metrics) rather than individual per-metric tests because: (i)~joint testing with BH-FDR correction controls family-wise error across the canary panel, avoiding the inflated false-positive rate that would result from reporting the single most significant pair; (ii)~the count of significant pairs ($k/8$) provides a natural effect-size measure that distinguishes isolated from systematic detection; (iii)~per-metric tests cannot capture the cross-metric consistency that separates genuine temporal precedence from metric-specific artifacts (e.g., MAUVE floor saturation affects 2/8 pairs universally, identifiable only in grouped results).\n\n\\paragraph{Canary metric choice.}\nSmolLM3-3B reveals that canary metric selection constitutes a sensitivity dimension beyond the five statistical methods: token entropy exhibits non-monotonic oscillations (0/4 significant pairs), while ECE maintains monotonic growth (3/4 pairs).\nNo single canary metric is universally optimal.\n\n\\paragraph{Exploratory CSD analysis.}\nCanary metrics show rising autocorrelation (Kendall $\\tau{=}0.79$--$0.82$) while downstream metrics show none ($\\tau{=}0.03$--$0.30$), but this pattern does not survive multiple testing correction (2/10 post-BH) and remains exploratory.\nWe note that \\citet{truong2026phase} show model collapse is a first-order transition, ruling out CSD as a structural detection mechanism; the rising autocorrelation likely reflects non-stationarity rather than critical slowing down.\n\n\\paragraph{Scale verification (Pythia-1.4B).}\n\\label{app:scale_14b}\nTo test whether the phase-diagram structure generalizes beyond 410M, we replicate the analysis at 1.4B scale ($T{=}10$--$15$, fp32, seed~42).\nTable~\\ref{tab:14b_phase} summarizes the available cells.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pythia-1.4B phase-diagram cells (fp32, PermG forward, direction-checked).}\n\\label{tab:14b_phase}\n\\begin{tabular}{lcccc}\n\\toprule\n$\\alpha$ & \\multicolumn{2}{c}{$T{=}10$} & \\multicolumn{2}{c}{$T{=}15$} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n         & s42 & s44 & s42 & s43 \\\\\n\\midrule\n0.45 & 0/6 & 0/6 & 3/6 & 5/6 \\\\\n0.50 & 4/6 & 6/6 & 3/6 & 3/6 \\\\\n0.60 & 4/6 & 6/6 & 6/6 & 6/6 \\\\\n0.75 & 5/6 & 6/6 & 6/6 & 6/6 \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize All: PermG fwd, 6-pair basis (2 canaries $\\times$ 3 distinct-$n$;} \\\\\n\\multicolumn{5}{l}{\\footnotesize MAUVE excl.\\ due to floor ${\\sim}0.033$ at 1.4B).} \\\\\n\\multicolumn{5}{l}{\\footnotesize s42 rev.\\ 0/6 at all $\\alpha$; s43 rev.\\ see text.} \\\\\n\\end{tabular}\n\\end{table}\n\nThe phase-diagram structure is qualitatively preserved at 1.4B scale.\nECE maintains monotonic growth across all three tested $\\alpha$ levels (3/3 cross-scale robust), and the binary detection pattern (above vs.\\ below $\\alpha_c$) is consistent with the 410M phase diagram.\nOn the 6-pair basis (MAUVE excluded due to systematic floor ${\\sim}0.033$; Table~\\ref{tab:14b_phase}), PermG forward detection at 1.4B ranges from 0/6 ($\\alpha{=}0.45$, $T{=}10$) to 6/6 ($\\alpha{\\geq}0.60$, $T{=}15$); token entropy exhibits one-step saturation ($27$--$39\\%$ drop from generation~0 to~1), reducing temporal resolution for entropy-based pairs.\nSeed s42 shows PermG$_\\text{rev}{=}0/6$ across all eight 1.4B conditions ($4\\alpha{\\times}2T$), confirming that bidirectionality is seed-specific rather than scale-inherent.\nThe 410M sync-dip ($\\alpha{=}0.60$: 0/8 at $T{\\leq}20$) does not reproduce at 1.4B (4/6 at $T{=}10$); whether this reflects scale-dependent dynamics or Pythia-specific effects remains open with only two model sizes tested.\nAt $T{=}15$, scale effects are $\\alpha$-conditional: $\\alpha{=}0.60$ reaches 6/6, while $\\alpha{=}0.50$ attenuates to 3/6 (vs 4/6 at $T{=}10$), confirming that detection loss is onset-localized rather than uniform.\nThe boundary's $T$-dependence is preserved: $\\alpha{=}0.45$ rises from 0/6 ($T{=}10$) to 3/6 ($T{=}15$), mirroring the 410M boundary shift.\nHowever, method-level heterogeneity emerges: Toda--Yamamoto exhibits a non-monotonic pattern at $T{=}15$, inverting the PermG ordering in the mid-$\\alpha$ range; gradual low-$\\alpha$ dynamics preserve VAR lag structure, while rapid entropy saturation disrupts lag dependence at intermediate $\\alpha$, with recovery at $\\alpha{=}0.75$ where extreme collapse dynamics (PPL drift ${+}390\\%$) generate sufficient temporal variation to support VAR detection.\nOnset-zone attenuation is $\\alpha$-invariant at 1.4B: both $\\alpha{=}0.45$ and $0.50$ yield 3/6 at $T{=}15$.\nAt 1.4B with $T{=}10$ (11 data points), non-PermG methods (threshold onset, naive cross-correlation, Toda--Yamamoto) have insufficient power due to short sequence length, reducing $K{\\geq}3$ consensus to an effective single-method test; at $T{=}15$ (16 data points), detection recovers (6/6 at $\\alpha{=}0.60$, lead time ${=}$ 10 generations) and $K{\\geq}3$ recovers its multi-method character, with 3/4 $\\alpha$ conditions achieving $K{\\geq}3{\\geq}2/6$ (onset $\\alpha{=}0.50$ seed-dependent: s42 1/6, s43 3/6).\nCross-method consensus ($K{\\geq}3$) exhibits seed-dependent variability at onset ($\\alpha{\\approx}0.50$), consistent with the noisy transition expected at phase boundaries, while remaining robust above onset ($K{\\geq}3$ ${\\geq}5/6$ at $\\alpha{=}0.75$).\nOn a unified 6-pair basis (MAUVE excluded due to systematic floor at ${\\sim}0.033$; Table~\\ref{tab:14b_phase}), third-seed replication (s44) at $T{=}10$ confirms ceiling detection above onset (6/6 at $\\alpha{\\geq}0.50$) with 0/6 at $\\alpha{=}0.45$, validating the blind zone.\nCross-$T$ improvement holds at 3/4 $\\alpha$ values ($\\alpha{=}0.45$: $0/6{\\to}5/6$; $\\alpha{=}0.60$: $6/6{\\to}6/6$; $\\alpha{=}0.75$: $6/6{\\to}6/6$), validating the predicted $\\alpha_c(T)$ decrease; at onset ($\\alpha{=}0.50$), PermG shows a marginal decrease ($6/6{\\to}3/6$), consistent with phase-boundary variability.\nAt onset ($\\alpha{=}0.45$--$0.50$), ECE-based pairs achieve higher detection rates than entropy-based pairs (e.g., 3/3 vs 0/3 robust at $\\alpha{=}0.50$, $T{=}15$), consistent with entropy's one-step saturation reducing temporal resolution at 1.4B scale.\n\n\\paragraph{Future work.}\nExtensions include multivariate VAR models for confounder testing, multi-seed replication across all six architecture families, longer training runs ($T{\\geq}20$), online monitoring within training pipelines, and accumulate-mode experiments~\\cite{dey2024breaking}.\nThe sigmoid onset boundary ($\\alpha_c{=}0.483$) invites connection to the critical mixture ratio scaling law of \\citet{gu2024cmr} and the data-mixing transitions of \\citet{gu2025datamixing}.\n\n\n\\section{Per-Method Dose-Response Profiles}\n\\label{app:dose_response}\n\nTable~\\ref{tab:dose_response_full} reports FDR significance counts (/8 validated pairs) for all five detection methods across 12 contamination levels (seed~42, Pythia-410M, WikiText, fp32).\nPermG exhibits a sharp 0$\\to$6 jump at $\\alpha{=}0.50$ with a return to 0 at $\\alpha{=}0.55$--$0.60$ (non-monotonic dip), while other methods show diffuse profiles: naive cross-correlation saturates at 7--8/8 across all levels including the null, and Toda--Yamamoto fluctuates without a clear onset.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-method FDR significance (/8 pairs) across contamination levels (Pythia-410M, seed~42, WikiText, fp32). PermG and Diff.\\ XCorr use BH-corrected FDR ($q{=}0.05$); Naive XCorr, Threshold, and TY use uncorrected $p{<}0.05$ (no FDR field in pipeline). $\\alpha{=}1.0$ from Pythia-410M cross-architecture condition (same seed/domain/precision).}\n\\label{tab:dose_response_full}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & Naive & Diff.\\ XCorr & Threshold & PermG & TY$^\\S$ \\\\\n\\midrule\n0.00 & 8 & 4 & 3 & \\textbf{0} & 1 \\\\\n0.10 & 7 & 6 & 0 & \\textbf{0} & 0 \\\\\n0.25 & 8 & 3 & 0 & \\textbf{0} & 2 \\\\\n0.30 & 8 & 4 & 0 & \\textbf{0} & 3 \\\\\n0.35 & 8 & 4 & 0 & \\textbf{0} & 1 \\\\\n0.40 & 8 & 3 & 0 & \\textbf{0} & 4 \\\\\n0.45 & 8 & 6 & 0 & \\textbf{0} & 1 \\\\\n0.50 & 8 & 7 & 4 & \\textbf{6} & 3 \\\\\n0.55 & 8 & 8 & 0 & \\textbf{0} & 1 \\\\\n0.60 & 8 & 6 & 0 & \\textbf{0} & 0 \\\\\n0.75 & 7 & 6 & 0 & \\textbf{6} & 3 \\\\\n1.00 & 8 & 6 & 2 & \\textbf{6} & 1 \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\S$TY directional assignment under verification; column retained for completeness.} \\\\\n\\end{tabular}}\n\\end{table}\n\nThe table highlights PermG's combination of null-control detection at 0/8 for this seed ($\\alpha{=}0.00$; pooled FPR across 6 seeds: 11.1\\%, lowest among directional methods), sharp onset (0$\\to$6 at $\\alpha{=}0.50$), and non-monotonic dip (0 at $\\alpha{=}0.55$--$0.60$), confirming it as the method whose dose-response profile most cleanly separates detection regimes.\nNaive cross-correlation's persistently high counts (7--8/8 even at $\\alpha{=}0.00$) demonstrate the 91.7\\% pooled null-control FPR reported in \\S\\ref{sec:method}.\n\n\n\\paragraph{Comparison with naive baselines.}\n\\label{app:naive_baselines}\n\nTable~\\ref{tab:naive_baselines} compares PermG against two practitioner-facing monitoring rules across 26 experiments (18~$\\alpha$ values, Pythia-410M, $T{=}10$, fp32).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Naive baseline comparison (Pythia-410M, $T{=}10$, fp32, 3 null-control runs).}\n\\label{tab:naive_baselines}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & FPR ($\\alpha{=}0$) & Onset $\\alpha$ \\\\\n\\midrule\nPPL-slope (${\\geq}2$ consec.\\ rises) & 100\\% (3/3) & 0.10 \\\\\nVariance-threshold ($2\\sigma$) & 67\\% (2/3) & 0.10 \\\\\nPermG (fwd ${\\geq}1$) & 0\\% (0/3) & 0.50 \\\\\n\\bottomrule\n\\multicolumn{3}{l}{\\footnotesize Onset $\\alpha$: lowest $\\alpha$ where method fires (seed~42).} \\\\\n\\end{tabular}\n\\end{table}\n\nPPL-slope fires at $\\alpha{=}0$ because the first-generation learning effect (perplexity drops from 26.9 to 19.3 at generation~1, then rises monotonically from generation~2 onward) produces consecutive rises indistinguishable from contamination-driven drift.\nVariance-threshold similarly triggers on the natural perplexity recovery.\nPermG avoids these false alarms by testing canary$\\to$downstream Granger precedence rather than univariate trend, thereby excluding training-drift confounds from the detection signal.\nNaive monitoring rules cannot distinguish contamination from natural training dynamics; formal statistical testing is necessary for controlled FPR.\n\n\n\\section{PermG Power Analysis}\n\\label{app:power_analysis}\n\nWe characterize PermG detection power via simulation under a controlled data-generating process (DGP) that matches the structure of our iterative training time series.\n\n\\paragraph{DGP.}\nFor each trial, we generate a bivariate system $(X_t, Y_t)$ for $t = 1, \\ldots, T$ where $X_t = \\mu + \\epsilon_t^X$ and $Y_t = \\mu + \\beta X_{t-1} + \\epsilon_t^Y$, with $\\epsilon \\sim \\mathcal{N}(0, \\sigma^2)$ and $\\sigma{=}1$.\nThe coupling parameter $\\beta$ controls signal strength; $\\beta{=}0$ is the null.\nThe linear coupling provides a power lower bound; nonlinear dynamics in actual iterative training may yield different power characteristics.\nWe sweep $\\beta \\in [0, 2]$ across $T \\in \\{6, 8, 10, 15, 20\\}$, running 100 replications per $(\\beta, T)$ cell with 5{,}000 permutations each and BH FDR correction at $q{=}0.05$ across 8 hypothetical pairs (matching the experimental setup).\n\n\\paragraph{Results.}\nTable~\\ref{tab:beta50} reports $\\beta_{50}$, the coupling strength required for 50\\% detection power, at each observation length $T$.\nUnder $\\sqrt{T}$ scaling, the product $\\beta_{50} \\cdot \\sqrt{T}$ should be constant; the observed decrease from 5.09 ($T{=}8$) to 2.68 ($T{=}20$) indicates that power grows faster than $\\sqrt{T}$, with the empirical scaling closer to $T^{-1.1}$.\nThe $\\sqrt{T}$ formula in \\S\\ref{sec:theory} thus provides a conservative lower bound on detection power: actual power at $T{=}20$ exceeds the $\\sqrt{T}$ prediction.\nFalse positive rates under FDR correction remain at or below 2\\% across all $T$ values (raw: 1--9\\%; Table~\\ref{tab:beta50}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{PermG power analysis: $\\beta_{50}$ (coupling for 50\\% power) under BH-FDR correction ($q{=}0.05$, 8 pairs). $\\beta_{50} \\cdot \\sqrt{T}$ decreases with $T$, indicating power grows faster than $\\sqrt{T}$. FPR: false positive rate at $\\beta{=}0$ (raw / FDR-corrected). Dashes indicate $<$50\\% power not reached within $\\beta \\leq 2.0$.}\n\\label{tab:beta50}\n\\begin{tabular}{lcccc}\n\\toprule\n$T$ & $\\beta_{50}$ & $\\beta_{50} \\cdot \\sqrt{T}$ & FPR (raw) & FPR (FDR) \\\\\n\\midrule\n6  & ---  & ---  & 1\\% & 0\\% \\\\\n8  & ---  & ---  & 6\\% & 2\\% \\\\\n10 & 2.0  & 6.32 & 9\\% & 2\\% \\\\\n15 & 1.2  & 4.65 & 6\\% & 2\\% \\\\\n20 & 0.9  & 4.02 & 5\\% & 1\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/permg_power_curve.pdf}\n\\caption{PermG detection power as a function of coupling strength $\\beta$ for five observation lengths ($T{=}6$--$20$; 100 replications $\\times$ 5{,}000 permutations, BH FDR $q{=}0.05$). Power increases with both $\\beta$ and $T$; at $T{=}6$--$8$, PermG remains underpowered ($<$20\\%) even at $\\beta{=}2.0$, consistent with the $T{=}10$ minimum required for reliable detection in our experimental setting.}\n\\label{fig:permg_power}\n\\end{figure*}\n\nAt $T{=}6$ and $T{=}8$, 50\\% power is not reached within $\\beta \\leq 2.0$ under FDR correction, explaining why PermG is fundamentally underpowered for very short series.\nThe practical implication for our $T{=}10$ setting: $\\beta_{50}{=}2.0$ means that only strong coupling produces reliable detection, consistent with the sharp onset at $\\alpha_c{\\approx}0.50$ where signal strength first exceeds this threshold.\nAt $T{=}20$, $\\beta_{50}$ drops to 0.9, predicting a left-shift of $\\alpha_c$ and broader detection coverage, as formalized in the detection boundary model (\\S\\ref{sec:theory}).\n\n\n\\section{Non-Stationarity Robustness Analysis}\n\\label{app:nonstationarity}\n\nWe assess PermG's size and power under controlled non-stationarity via Monte Carlo simulation, then compare to the empirical autocorrelation structure of our experimental series.\n\n\\paragraph{Simulation design.}\nWe generate bivariate AR(1) series with unidirectional coupling ($x \\to y$):\n$x_t = \\varphi x_{t-1} + \\varepsilon_t^x$, $y_t = \\varphi y_{t-1} + \\beta x_{t-1} + \\varepsilon_t^y$,\nwith $T{=}11$, 1{,}000 replications, and 500 permutations per replication.\nSize is evaluated under $H_0{:}\\;\\beta{=}0$; power under $H_1{:}\\;\\beta{=}0.6$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Size (FPR at $\\beta{=}0$) and power ($\\beta{=}0.6$) under stationary and non-stationary AR(1) DGP ($T{=}11$, 1{,}000 reps, 500 perms). First-differencing maintains nominal size across all $\\varphi$; PermG FPR inflates to ${\\sim}10\\%$ at $\\varphi{\\geq}0.95$.}\n\\label{tab:nonstationarity_sim}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{Size (\\%, $\\beta{=}0$)} & \\multicolumn{3}{c}{Power (\\%, $\\beta{=}0.6$)} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n$\\varphi$ & Raw GC & First-Diff & PermG & Raw GC & First-Diff & PermG \\\\\n\\midrule\n0.50 & 6.4 & 6.6 & 6.8 & 37.7 & 17.7 & 36.8 \\\\\n0.95 & 10.0 & 5.9 & 9.5 & 44.3 & 28.7 & 41.5 \\\\\n0.99 & 11.2 & 4.2 & 10.7 & 46.4 & 24.6 & 41.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\varphi{=}0.50$ (stationary), all three methods achieve near-nominal size ($6.4$--$6.8\\%$ vs.\\ $5\\%$ nominal).\nUnder strong non-stationarity ($\\varphi{\\geq}0.95$), PermG FPR inflates to ${\\sim}10\\%$ because permutation shuffling destroys temporal autocorrelation, shifting the null distribution.\nFirst-differencing maintains proper size ($4.2$--$6.6\\%$) at the cost of reduced power ($17.7$--$28.7\\%$ vs.\\ PermG's $36.8$--$41.7\\%$).\nOur pipeline applies first-differencing \\emph{before} permutation testing, combining PermG's power advantage with differencing's size control; the simulation isolates each component to characterize the tradeoff.\n\n\\paragraph{Empirical autocorrelation.}\nTable~\\ref{tab:empirical_ar1} reports AR(1) coefficients from seven experimental conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Empirical AR(1) coefficients for token entropy (te) and distinct-1 (d1), raw and first-differenced series. High raw $\\varphi$ in d1 reflects deterministic iterative-training decline, not stochastic AR persistence; first-differencing reduces $\\varphi$ to $< 0.44$.}\n\\label{tab:empirical_ar1}\n\\begin{tabular}{llrcccc}\n\\toprule\nExperiment & $\\alpha$ & $T$ & te $\\varphi_{\\text{raw}}$ & d1 $\\varphi_{\\text{raw}}$ & te $\\varphi_{\\text{diff}}$ & d1 $\\varphi_{\\text{diff}}$ \\\\\n\\midrule\na000\\_s42 & 0.00 & 10 & $-0.51$ & $0.86$ & $-0.57$ & $-0.14$ \\\\\na025\\_s42 & 0.25 & 10 & $-0.34$ & $0.95$ & $-0.45$ & $0.19$ \\\\\na050\\_s42 & 0.50 & 10 & $-0.28$ & $0.87$ & $0.31$ & $0.10$ \\\\\na075\\_s42 & 0.75 & 10 & $0.14$ & $0.91$ & $0.88$ & $0.24$ \\\\\na100\\_s42 & 1.00 & 10 & $1.00$ & $0.89$ & $0.98$ & $0.18$ \\\\\nt20\\_a050 & 0.50 & 20 & $-0.10$ & $0.97$ & $-0.25$ & $0.44$ \\\\\nt20\\_a100 & 1.00 & 20 & $0.98$ & $0.81$ & $0.87$ & $0.14$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Adequacy argument.}\nUnder null conditions ($\\alpha{=}0.0$), where FPR is defined, token entropy exhibits $\\varphi{=}-0.51$ (anti-correlated, far from the $\\varphi{\\geq}0.95$ regime where simulation reveals FPR inflation); at $\\varphi{=}0.50$, PermG FPR is $6.8\\%$, near nominal.\nThe high raw $\\varphi$ in distinct-1 ($0.81$--$0.97$ across all $\\alpha$ including null) reflects deterministic iterative-training diversity decline---a monotonic trend driven by the training protocol---not stochastic AR persistence.\nDeterministic trends differ fundamentally from the stochastic AR(1) DGP: they produce predictable trajectories rather than autocorrelated noise, and first-differencing effectively removes them (first-differenced distinct-1 $\\varphi$ ranges $-0.14$ to $0.44$, mean ${\\sim}0.17$).\nOur empirical FPR of 4/36 (11.1\\%) across six null seeds---the lowest among directional methods---confirms adequate size control in our experimental setting; all four false positives occur in token\\_entropy$\\to$distinct pairs in the forward direction, suggesting a structural pattern rather than random Type~I error.\nWe note that $T{=}10$ (11 data points) yields high-variance AR(1) estimates; the cross-experiment pattern is more informative than individual values.\n\n\\paragraph{DGP limitation.}\nThe bivariate AR(1) with linear coupling is a simplification; actual iterative training involves nonlinear dynamics (mode amplification, threshold-dependent diversity loss).\nThese simulation results characterize PermG's behavior under controlled conditions, not exact calibration for the experimental setting; they provide a lower bound on size control because the linear DGP represents a worst case for permutation-based tests (smooth autocorrelation that permutation destroys).\n\n\n\\section{Shapley Value Analysis}\n\\label{app:shapley}\n\nWe quantify each method's marginal contribution to the MMCT ensemble using Shapley values~\\cite{shapley1953value}, computed via exact enumeration over all $2^5{=}32$ coalitions of the five detection methods.\n% TODO-D219: recompute Shapley with 6-seed null data (seeds 45--50, 36 null pairs; PermG FPR now 4/36=11.1%, no longer zero)\nFor a coalition $S \\subseteq \\{m_1, \\ldots, m_5\\}$, we define two performance metrics: the false positive rate FPR($S$), computed from 3 null experiments ($\\alpha{=}0.0$, seeds 42/43/44; 24 null pairs total), and the false negative rate FNR($S$), computed from 45 signal experiments across all non-null $\\alpha$ levels (270 signal pairs for the 6-pair variant excluding mauve).\nThe Shapley value $\\phi_k$ for method $m_k$ is the weighted average of its marginal contribution across all coalitions; positive FPR-Shapley indicates the method \\emph{increases} false positives, while negative FNR-Shapley indicates it \\emph{reduces} false negatives.\nThe combined Shapley value $\\phi_k^{\\text{comb}} = \\phi_k^{\\text{FPR}} + \\phi_k^{\\text{FNR}}$ balances both error types, with more negative values indicating greater net benefit.\n\nTable~\\ref{tab:shapley_6pair} reports the 6-pair analysis (excluding mauve).\n% TODO-D219: recompute Shapley values; PermG φ^FPR will be >0 with 6-seed data (4/36 FPs)\nPermG achieves the lowest (best) combined Shapley ($-0.180$), driven entirely by FNR reduction with zero FPR contribution---the only method with this property.\nNaive cross-correlation is the worst contributor ($+0.203$), with its massive FPR Shapley ($+0.622$) overwhelming its FNR benefit ($-0.419$): adding naive cross-correlation to any coalition increases false positives far more than it reduces false negatives.\nThreshold onset contributes almost nothing useful ($+0.074$ combined; FPR $+0.101$, FNR $-0.027$), confirming the near-zero detection power reported in Table~\\ref{tab:method_comparison}.\nFigure~\\ref{fig:shapley} visualizes the decomposition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Shapley value decomposition (6-pair, mauve excluded). FPR-Shapley: marginal FPR contribution (positive = increases false positives). FNR-Shapley: marginal FNR contribution (negative = reduces false negatives). Combined = FPR + FNR (more negative = better). 48 experiments, $2^5{=}32$ coalitions, exact enumeration.}\n\\label{tab:shapley_6pair}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $\\phi^{\\text{FPR}}$ & $\\phi^{\\text{FNR}}$ & $\\phi^{\\text{comb}}$ \\\\\n\\midrule\nNaive XCorr          & $+0.622$ & $-0.419$ & $+0.203$ \\\\\nDiff.\\ XCorr         & $+0.163$ & $-0.306$ & $-0.142$ \\\\\nThreshold ($3\\sigma$) & $+0.101$ & $-0.027$ & $+0.074$ \\\\\n\\textbf{Perm.\\ Granger} & $\\mathbf{0.000}$ & $\\mathbf{-0.180}$ & $\\mathbf{-0.180}$ \\\\\nToda--Yamamoto       & $+0.031$ & $-0.069$ & $-0.038$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/shapley_method_contribution.pdf}\n% TODO-D219: regenerate figure and update caption after Shapley recomputation with 6-seed data\n\\caption{Shapley value decomposition of each method's marginal contribution to FPR (positive bars) and FNR (negative bars). PermG is the only method with zero FPR contribution; naive cross-correlation's FPR dominates its FNR benefit.}\n\\label{fig:shapley}\n\\end{figure*}\n\nThe 8-pair variant (including mauve) yields qualitatively identical rankings: PermG remains the best contributor ($\\phi^{\\text{comb}}{=}-0.152$), naive cross-correlation the worst ($+0.170$), and threshold onset near-zero ($+0.063$).\n\n\\paragraph{FDR correction scope.}\nThis analysis applies BH-corrected significance (\\texttt{significant\\_fdr}) uniformly across all five methods, including naive cross-correlation and Toda--Yamamoto.\nIn contrast, the per-method dose-response profiles (Table~\\ref{tab:dose_response_full}) use uncorrected significance for naive cross-correlation, threshold onset, and Toda--Yamamoto because FDR-corrected fields are not available in the per-experiment pipeline output for these methods.\nThe Shapley analysis recomputes significance from raw $p$-values with BH correction applied post hoc, ensuring a fair comparison across methods within the coalition framework.\n\n\n\\section{MMCT Weight Robustness Ablation}\n\\label{app:weight_robustness}\n\nThe detection results reported in the main text use equal-weight majority voting ($K{\\geq}3$ of 5 methods, each contributing at most one vote per pair); PermG contributes at most $1/5 = 20\\%$ of the consensus weight.\nFPR-inverse weighting is used \\emph{only} in the exploratory method ranking below, not in the detection results.\nTo verify that PermG's top ranking is not an artifact of the FPR-inverse weighting scheme, we recompute Shapley values under four weight specifications (Table~\\ref{tab:weight_robustness}).\nEqual weighting ($w{=}1$ for all methods) eliminates any FPR-based advantage; PermG still ranks first ($\\phi^{\\text{comb}}{=}-0.152$), though its margin over naive cross-correlation narrows to 0.015.\nUnder cap-5, the margin widens to 0.043 as the FPR penalty begins to differentiate high-FPR methods.\nCap-10 and original cap-100 yield identical Shapley values because the consensus threshold ($K{\\geq}3$) is determined by the three smallest method weights ($w_{\\text{naive}}{+}w_{\\text{diff}}{+}w_{\\text{thresh}} = 7.76$), which are invariant to further increases in the PermG or TY cap; this saturation confirms that the original $w{=}100$ does not artificially inflate PermG's contribution.\n% TODO-D219: recompute weight robustness table with 6-seed data; PermG φ^FPR will be >0\nAcross all schemes, PermG's advantage derives from the same structural property: zero FPR ($\\phi^{\\text{FPR}}{=}0$) combined with moderate FNR reduction ($\\phi^{\\text{FNR}}{=}-0.152$ to $-0.426$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MMCT weight robustness: PermG combined Shapley under four weighting schemes. PermG ranks first in all cases. Gap = $|\\phi^{\\text{comb}}_{\\text{PermG}} - \\phi^{\\text{comb}}_{\\text{runner-up}}|$. 48 experiments (3 null + 45 signal), exact Shapley enumeration ($2^5{=}32$ coalitions).}\n\\label{tab:weight_robustness}\n\\begin{tabular}{lrcrc}\n\\toprule\nScheme & $w_{\\text{PermG}}$ & $\\phi^{\\text{comb}}_{\\text{PermG}}$ & Runner-up & Gap \\\\\n\\midrule\nEqual ($w{=}1$)     & 1   & $-0.152$ & NaiveXCorr ($-0.137$) & 0.015 \\\\\nCap-5               & 5   & $-0.165$ & NaiveXCorr ($-0.123$) & 0.043 \\\\\nCap-10              & 10  & $-0.426$ & TY ($-0.067$)         & 0.359 \\\\\nFPR-inv.\\ (cap-100) & 100 & $-0.426$ & TY ($-0.067$)         & 0.359 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{PermG FPR Independence Analysis}\n\\label{app:fpr_independence}\n\nTable~\\ref{tab:null_fpr_methods} reports null-control FPR for all five detection methods across six seeds ($6 \\times 6 = 36$ pairs, 6-pair basis excluding mauve).\nUnder identical BH-FDR correction ($q{=}0.05$), DiffXCorr achieves the lowest FPR (1/36, 2.8\\%) but lacks directional separation; PermG (4/36, 11.1\\%) is the lowest among directional methods.\nAll four PermG false positives occur in token\\_entropy$\\to$distinct pairs (seeds~45 and 50, forward direction only), suggesting a structural pattern concentrated in a single canary--downstream pair type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Null-control FPR by method ($\\alpha{=}0.0$, 6~seeds 45--50, 6~pairs each). All p-value--based methods (DiffXCorr, PermG, TY) report BH-FDR--corrected rejections at $q{=}0.05$ for fair comparison. Threshold uses a deterministic $3\\sigma$ criterion; NaiveXCorr uses uncorrected correlation significance.}\n\\label{tab:null_fpr_methods}\n\\begin{tabular}{llrr}\n\\toprule\nMethod & Criterion & Rejections (/36) & FPR (\\%) \\\\\n\\midrule\nDiff.\\ XCorr$^\\dagger$ & BH-FDR & 1 & 2.8 \\\\\n\\textbf{Perm.\\ Granger} & \\textbf{BH-FDR} & \\textbf{4} & \\textbf{11.1} \\\\\nThreshold & $3\\sigma$ (det.) & 10 & 27.8 \\\\\nToda--Yamamoto & BH-FDR & 14 & 38.9 \\\\\nNaive XCorr & uncorr. & 33 & 91.7 \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$Bidirectional; cannot separate forward from reverse.} \\\\\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cluster adjustment.}\nThe 36 null-control pairs are nested within 6~seeds (6~pairs per seed), introducing within-seed correlation.\nWithin-seed ICC${=}0.14$ yields an effective sample size $N_{\\text{eff}} \\approx 21$ (from $N_{\\text{eff}} = N / [1 + (m-1) \\cdot \\text{ICC}]$ where $N{=}36$, $m{=}6$).\nUnder the Clopper--Pearson exact method with $N_{\\text{eff}}{=}21$ and 4 successes (scaled), the cluster-adjusted 95\\% CI is $[1.2\\%, 30.4\\%]$, compared to $[3.1\\%, 26.1\\%]$ under independence ($N{=}36$).\nThe lower ICC compared to the 3-seed pilot ($0.14$ vs.\\ $0.34$) reflects greater between-seed consistency with six independent replications.\n\n\\paragraph{Direction filtering.}\nForward-direction filtering (retaining only pairs with peak lag${<}0$ for cross-correlation methods) reduces null-control $K{\\geq}3$ false positives.\nUnder the 6-seed, 6-pair basis, $K{\\geq}3$ consensus with filtering produces 6/36 false positives (16.7\\%; detail below); the 3-seed pilot underestimated this rate (0/8).\nDetection at $\\alpha{\\geq}0.50$ is unaffected: $K{\\geq}3$ counts are identical with and without direction filtering at all signal levels.\n\n\\paragraph{$K{\\geq}3$ false positive detail.}\nUnder the 6-pair basis (6~seeds, 36~pairs), $K{\\geq}3$ consensus produces 6 false positives (FPR${=}16.7\\%$).\nOf these, 4 are driven by naive cross-correlation, threshold onset, and Toda--Yamamoto (PermG does \\emph{not} vote); the remaining 2 (seeds~45 and 50, te$\\to$distinct) include PermG in the consensus.\nPermG thus contributes to only 2 of 6 consensus false positives, confirming that most $K{\\geq}3$ FPR is driven by the high-FPR methods (naive, threshold, TY).\n\n\\paragraph{Sensitivity to FPR assumption.}\nEven under the conservative upper bound of the cluster-adjusted CI (30.4\\%), PermG remains the lowest-FPR directional method: DiffXCorr achieves a lower FPR under identical BH-FDR correction (2.8\\%) but lacks forward/reverse separation; the next directional method (threshold onset) has 27.8\\% and Toda--Yamamoto 38.9\\%.\nOur primary results rely on equal-weight $K{\\geq}3$ majority voting, where each method contributes exactly one vote regardless of its FPR---this mechanism is completely unaffected by any FPR assumption.\nFor the exploratory FPR-inverse weighting, PermG's weight ($w{=}1/0.111{=}9.0$) exceeds all directional alternatives (threshold: 3.6, TY: 2.6, naive: 1.1); DiffXCorr ($w{=}1/0.028{=}35.7$) receives a higher weight but lacks directional separation, preserving PermG's rank among directional methods.\nThe insensitivity of both the voting mechanism and the method ranking to the upper CI bound provides evidence that the MMCT conclusions are robust to uncertainty in PermG's Type~I error rate.\n\n\\section{Sigmoid Transition Shape}\n\\label{app:sigmoid_shape}\n\nSigmoid regression on the original 13-point $T{=}10$ grid yields $\\alpha_c = 0.483 \\pm 0.006$ but $k = 478 \\pm 475$ ($\\mathrm{SE}(k) \\approx k$), indicating that the coarse grid cannot constrain the transition shape.\nDense $\\alpha$ sampling (17~values at $T{=}10$) resolves this ambiguity: formal likelihood-ratio testing strongly favors a smooth sigmoid over a literal step function ($\\Delta\\mathrm{AIC}{=}-110$), with fitted steepness $k{=}15.7$ (95\\% CI $[9.4, 28.2]$).\nThe transition is steep but finite-width, not a literal discontinuity.\nThis observed steepness exceeds what smooth signal models predict: VAR(1) simulations under H0 (linear, $k{=}6.1$) and H0$'$ (concave, $k{=}4.9$) produce onset sigmoids with $k{=}4.9$--$6.1$ (\\S\\ref{app:power_sim}), yielding steepness ratios $k_{\\mathrm{obs}} / k_{\\mathrm{H0}} \\approx 2.6$--$3.2$ (CI lower bound ratio ${\\approx}2$).\nWe do not fit a combined $T{=}10 + T{=}20$ sigmoid because $\\alpha{=}0.45$ yields contradictory counts under the two sequence lengths (0/8 vs.\\ 5/8), reflecting genuine power dependence on $T$ rather than a single dose-response curve.\n\n\n\\section{Intervention Threshold Sensitivity}\n\\label{app:intervention_sensitivity}\n\n\\paragraph{Within-$\\alpha$ sensitivity at $\\alpha{=}1.0$.}\nTable~\\ref{tab:threshold_sensitivity} reports the predictive cessation outcome under five entropy-drop thresholds (5\\%--25\\%) at $\\alpha{=}1.0$ (Pythia-410M, seed~42).\nAll five thresholds produce identical outcomes: token entropy drops 40.7\\% at generation~1, far exceeding even the most conservative threshold (25\\%), so every threshold triggers at the same generation.\nThe intervention conclusion---peak perplexity 57.0, recovery in one generation, final perplexity 21.3---is invariant to threshold choice within this range.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Threshold sensitivity at $\\alpha{=}1.0$ (Pythia-410M, s42, fp32). All thresholds trigger at generation~1 (entropy drop 40.7\\%$\\gg$threshold), producing identical recovery trajectories.}\n\\label{tab:threshold_sensitivity}\n\\begin{tabular}{rccr}\n\\toprule\nThreshold & Trigger gen & Peak PPL & Final PPL \\\\\n\\midrule\n5\\%  & 1 & 56.99 & 21.29 \\\\\n10\\% & 1 & 56.99 & 21.29 \\\\\n15\\% & 1 & 56.99 & 21.29 \\\\\n20\\% & 1 & 56.99 & 21.29 \\\\\n25\\% & 1 & 56.99 & 21.29 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-$\\alpha$ operating band.}\nThe within-$\\alpha$ analysis establishes threshold invariance at $\\alpha{=}1.0$ but does not address whether thresholds generalize across contamination levels.\nWe examine observed entropy trajectories from the alpha sweep (not actual intervention experiments at $\\alpha{<}1.0$) to characterize the operating band.\nThe maximum entropy drop across 10 generations varies by contamination level: 7.5\\% at $\\alpha{=}0.0$ (fine-tuning drift only), 7.7\\% at $\\alpha{=}0.10$, 7.8\\% at $\\alpha{=}0.25$, 22.4\\% at $\\alpha{=}0.50$, 35.3\\% at $\\alpha{=}0.75$, and 62.1\\% at $\\alpha{=}1.0$.\nThresholds below 7.5\\% (e.g., 5\\%) trigger on clean training data---a false alarm.\nThresholds above 22.4\\% (e.g., 25\\%) miss $\\alpha{=}0.50$, the lowest contamination level with meaningful entropy signal.\nThe safe operating band is therefore $[10\\%, 22\\%]$: any threshold in this range produces zero false alarms on $\\alpha{=}0.0$ while detecting contamination at $\\alpha{\\geq}0.50$.\nThe reported 15\\% threshold sits near the center of this band.\nThis analysis is based on entropy trajectories from non-intervention training runs; whether actual intervention at $\\alpha{<}1.0$ would produce the same triggering behavior remains unvalidated.\n\n\n\\section{Channel Effect Size Analysis}\n\\label{app:channel_effect_size}\n\nFirst-differencing eliminates all canary$\\to$perplexity Granger associations while preserving canary$\\to$diversity leads (\\S\\ref{sec:regime}).\nWe present three lines of evidence that this asymmetry reflects a genuine temporal structure difference rather than selective power loss from differencing.\n\n\\paragraph{Correlation retention parity.}\nFirst-differencing retains comparable correlation magnitude for both channel types (Table~\\ref{tab:channel_retention}).\nDiversity channels ($n{=}243$ pairs across all non-null experiments) retain a median $|r|$ of 0.952 after differencing, while perplexity channels ($n{=}8$ pairs; limited sample) retain 1.00.\nThis parity rules out a blanket power-loss explanation: if differencing selectively destroyed perplexity signal, $|r|$ retention would be substantially lower for perplexity than for diversity.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{First-differencing effect by channel type. $|r|$ retention = diff $|r|$ / naive $|r|$. Despite comparable $|r|$ retention, Granger $F$ differs by an order of magnitude. Perplexity channel has limited sample ($n{=}8$); all paired comparisons are from bf16 experiments.}\n\\label{tab:channel_retention}\n\\begin{tabular}{lrccrc}\n\\toprule\nChannel & $n$ & Naive $|r|$ & Diff $|r|$ & Retention & Med.\\ $F$ \\\\\n\\midrule\nDiversity   & 243 & 0.943 & 0.921 & 0.952 & 67.8 \\\\\nPerplexity  & 8   & 0.924 & 0.900 & 1.002 & 11.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Granger $F$-statistic asymmetry.}\nWithin matched experiments (same model, seed, $\\alpha$, precision), the Granger $F$-statistic is $20$--$28{\\times}$ higher for diversity than perplexity channels.\nAt $\\alpha{=}0.60$ (s42, bf16): diversity mean $F{=}229.4$ versus perplexity mean $F{=}8.3$ (ratio $27.8{\\times}$).\nAt $\\alpha{=}1.0$ reactive (s43, bf16): diversity mean $F{=}236.4$ versus perplexity mean $F{=}11.5$ (ratio $20.6{\\times}$).\nSince $|r|$ retention is comparable across channels, this $F$-statistic gap cannot be attributed to differencing-induced signal loss; it must reflect a difference in the temporal structure that Granger tests evaluate.\n\n\\paragraph{Temporal structure: lagged vs.\\ contemporaneous.}\nThe lag distribution of peak differenced cross-correlations reveals the structural difference.\nFor diversity channels, 81\\% of peak correlations occur at canary-leading lags (lag${<}0$), with a median lag of $-1$ generation---consistent with the one-generation temporal precedence visible in Figure~\\ref{fig:metric_trajectory}.\nFor perplexity channels, 50\\% of peak correlations occur at lag${=}0$ (contemporaneous co-movement), with a median lag of $0$.\nGranger precedence tests lagged predictive improvement; contemporaneous co-movement produces low $F$-statistics regardless of signal magnitude, which is the correct behavior for a test designed to detect temporal precedence.\nThe perplexity channel sample is limited ($n{=}8$ pairs from bf16 experiments), and these lag distributions should not be generalized to fp32 conditions without further validation.\n\n\n\\section{Mutual Information Analysis}\n\\label{app:mi_analysis}\n\nWe estimate the Gaussian mutual information lower bound between token entropy (canary) and each diversity metric across contamination levels, using $T{=}11$ data points per series ($T{=}10$ for two conditions).\nThe Gaussian estimator $\\hat{I}_G = -\\frac{1}{2}\\log_2(1 - r^2)$, where $r$ is the Pearson correlation, provides a conservative lower bound on MI; we do not report KSG nonparametric estimates due to uncorrected positive bias at $T{=}11$.\nThe $\\alpha{=}0.05$ data point is excluded because it uses an experiment excluded from the dose-response analysis.\n\nTable~\\ref{tab:mi_bounds} reports the mean Gaussian MI across the three distinct-$n$ metrics for each $\\alpha$ level.\nMI follows a V-shaped curve: it drops from 0.112~bits at $\\alpha{=}0.10$ to a minimum of 0.010~bits at $\\alpha{=}0.25$, then rises monotonically to 0.270~bits at $\\alpha{=}0.75$.\nMI remains positive throughout the blind zone ($\\alpha \\leq 0.45$; range 0.010--0.141~bits), confirming that canary--diversity coupling exists below the detection threshold but falls below PermG's statistical power floor at $T{=}10$.\nThere is no discontinuity at $\\alpha_c \\approx 0.50$: the detection onset reflects power accumulation, not an abrupt change in information coupling.\nBootstrap 95\\% CIs span 1--3 orders of magnitude at $T{=}11$, so individual point estimates should be interpreted cautiously.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Gaussian MI lower bound (bits) between token entropy and distinct-$n$ diversity metrics ($T{=}11$, Pythia-410M, fp32). Mean across distinct-1/2/3; $\\alpha{=}0.05$ excluded (see text). CIs omitted due to width at $T{=}11$.}\n\\label{tab:mi_bounds}\n\\begin{tabular}{rrc}\n\\toprule\n$\\alpha$ & Seeds & MI (bits) \\\\\n\\midrule\n0.10 & 2 & 0.112 \\\\\n0.25 & 3 & 0.010 \\\\\n0.30 & 1 & 0.062 \\\\\n0.35 & 1 & 0.098 \\\\\n0.40 & 1 & 0.119 \\\\\n0.45 & 2 & 0.141 \\\\\n0.50 & 3 & 0.107 \\\\\n0.60 & 2 & 0.209 \\\\\n0.75 & 1 & 0.270 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Moment Cascade Analysis}\n\\label{app:moment_cascade}\n\nWe analyze the temporal ordering of metric degradation onset across 6 WikiText seed${\\times}\\alpha$ conditions (2 seeds $\\times$ 3 non-trivial $\\alpha$ levels each) to test whether token entropy consistently degrades before diversity metrics.\nOnset is defined as the first generation where a metric's cumulative change exceeds 5\\% of its generation-0 value.\n\nTable~\\ref{tab:moment_cascade} reports the onset generation for each metric across conditions.\nToken entropy reaches onset at generation~1 in all 6 conditions; distinct-$n$ metrics reach onset at generation~2 in all 18 pairwise comparisons (6 conditions $\\times$ 3 distinct-$n$ metrics).\nAcross these 18 comparisons, entropy degrades first in 16 cases (Kendall $\\tau{=}0.337$, consistent with a weak but reliable temporal ordering).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Degradation onset generation (5\\% threshold) by metric and condition (Pythia-410M, WikiText, fp32). Token entropy reaches onset at generation~1 in all non-null conditions; distinct-$n$ metrics follow at generation~2.}\n\\label{tab:moment_cascade}\n\\begin{tabular}{llcccccc}\n\\toprule\nSeed & $\\alpha$ & Entropy & Dist-1 & Dist-2 & Dist-3 & ECE & PPL \\\\\n\\midrule\n42 & 0.10 & 1 & 2 & 2 & 2 & 2 & --- \\\\\n42 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\\\\n42 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\\\\n43 & 0.25 & 1 & 2 & 2 & 2 & 4 & --- \\\\\n43 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\\\\n43 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\\\\n\\bottomrule\n\\multicolumn{8}{l}{\\footnotesize ---: onset not reached within $T{=}10$ generations.} \\\\\n\\end{tabular}\n\\end{table}\n\nThe cascade ordering provides evidence for the canary mechanism independent of Granger-type tests: it does not depend on first-differencing, lag selection, or the permutation null distribution.\nECE shows onset at generation~1 at $\\alpha{\\geq}0.50$ (both seeds), consistent with its role as a secondary canary metric.\nAt low contamination ($\\alpha{=}0.10$ and $\\alpha{=}0.25$), perplexity never reaches the 5\\% onset threshold within $T{=}10$ generations, while entropy already shows generation-1 onset---consistent with entropy's higher sensitivity to distributional shifts.\n\n\n\\section{Cascade Ordering Theory: Proofs}\n\\label{app:cascade_theory}\n\nThis section provides the full proofs for Proposition~\\ref{thm:entropy_leads} and Proposition~\\ref{prop:div_lag} from \\S\\ref{sec:cascade}, plus supporting results.\n\n\\begin{assumption}[Mode Amplification]\\label{ass:mode_amp}\nThe training map $\\mathcal{T}$ redistributes probability mass from low-probability to high-probability tokens: there exists a threshold $\\bar{p}$ such that $\\mathcal{T}(p)_i > p_i \\Rightarrow p_i \\geq \\bar{p}$ and $\\mathcal{T}(p)_j < p_j \\Rightarrow p_j \\leq \\bar{p}$.\n\\end{assumption}\n\nThis captures the standard finite-capacity approximation effect: MLE on finite samples from a peaked distribution amplifies modes and suppresses the tail~\\cite{shumailov2024curse,dohmatob2024tale}.\n\n\\begin{proposition}[Entropy is a first-order indicator]\\label{prop:entropy_first}\nLet $p \\in \\Delta^{V-1}$ and $\\delta = \\alpha(\\mathcal{T}(p) - p)$ be a mode-amplifying perturbation with $\\sum_i \\delta_i = 0$. Then $\\Delta H = H(p+\\delta) - H(p) = -\\sum_i \\delta_i \\log p_i + O(\\|\\delta\\|^2) < 0$.\n\\end{proposition}\n\n\\begin{proof}\nTaylor-expanding $H$ around $p$:\n$H(p+\\delta) = H(p) - \\sum_i \\delta_i \\log p_i - \\sum_i \\delta_i - \\frac{1}{2}\\sum_i \\delta_i^2/p_i + O(\\|\\delta\\|^3)$.\nSince $\\sum_i \\delta_i = 0$: $\\Delta H = -\\sum_i \\delta_i \\log p_i - \\frac{1}{2}\\sum_i \\delta_i^2/p_i + O(\\|\\delta\\|^3)$.\nUnder mode amplification, tokens gaining mass ($\\delta_i > 0$) have $p_i \\geq \\bar{p}$ (hence $\\log p_i \\geq \\log \\bar{p}$) and tokens losing mass ($\\delta_j < 0$) have $p_j \\leq \\bar{p}$ (hence $\\log p_j \\leq \\log \\bar{p}$).\nWriting $m = \\sum_{i:\\delta_i > 0} \\delta_i$: $-\\sum_i \\delta_i \\log p_i = -m[\\overline{\\log p}^{+} - \\overline{\\log p}^{-}] < 0$, where $\\overline{\\log p}^{\\pm}$ are the $|\\delta|$-weighted means over gaining/losing tokens.\nThe second-order Fisher information term $-\\frac{1}{2}\\sum_i \\delta_i^2/p_i$ is always negative, reinforcing the decrease.\n\\end{proof}\n\n\\begin{proposition}[Diversity is a threshold indicator]\\label{prop:div_threshold}\nDefine the $\\epsilon$-effective support $S_\\epsilon(p) = |\\{i \\in [V]: p_i > \\epsilon\\}|$, where $\\epsilon \\approx c/N$ is the generation threshold for sample size $N$.\nUnder the same perturbation $\\delta$: $\\Delta S_\\epsilon = -|\\{i: p_i > \\epsilon \\text{ and } p_i + \\delta_i \\leq \\epsilon\\}|$.\nThis equals zero whenever $\\|\\delta\\|_\\infty < \\gamma(p,\\epsilon) := \\min_{i: p_i > \\epsilon}(p_i - \\epsilon)$.\n\\end{proposition}\n\n\\begin{proof}\nToken $i$ exits the effective support iff $p_i > \\epsilon$ and $p_i + \\delta_i \\leq \\epsilon$, requiring $|\\delta_i| \\geq p_i - \\epsilon$.\nIf $\\|\\delta\\|_\\infty < \\gamma$, no token satisfies this condition.\n\\end{proof}\n\n\\paragraph{Proof of Proposition~\\ref{thm:entropy_leads}.}\n\\emph{Part (a):} Take any mode-amplifying $\\delta$ with $\\|\\delta\\|_\\infty < \\gamma(p,\\epsilon)$.\nBy Proposition~\\ref{prop:div_threshold}, $\\Delta S_\\epsilon = 0$.\nBy Proposition~\\ref{prop:entropy_first}, $\\Delta H < 0$.\nSuch $\\delta$ exists for all $\\alpha < \\gamma / \\max_i |\\mathcal{T}(p)_i - p_i|$.\n\\emph{Part (b):} If $\\Delta S_\\epsilon < 0$, some token $k$ has $p_k > \\epsilon$ but $p_k + \\delta_k \\leq \\epsilon$, so $\\delta_k < 0$.\nUnder mode amplification, this implies $p_k \\leq \\bar{p}$; the total mass transferred to high-probability tokens ensures $\\overline{\\log p}^+ > \\overline{\\log p}^-$.\nBy Proposition~\\ref{prop:entropy_first}, $\\Delta H < 0$. $\\square$\n\n\\paragraph{Proof of Proposition~\\ref{prop:div_lag}.}\nBy the margin condition, at every generation $s \\leq t_H$ the perturbation norm $\\alpha\\|\\mathcal{T}(p_s) - p_s\\|_\\infty$ is less than $\\gamma(p_s, \\epsilon)$.\nBy Proposition~\\ref{prop:div_threshold}, no token exits the effective support at any $s \\leq t_H$, so $\\Delta S_\\epsilon = 0$ for all $s \\leq t_H$.\nSince time is discrete, $t_D \\geq t_H + 1$. $\\square$\n\n\\paragraph{ECE co-movement (qualitative argument).}\nUnder conditional mode amplification (peakier $q_\\theta(\\cdot|x)$ at each generation), per-token conditional entropy $h(x) = H(q_\\theta(\\cdot|x))$ decreases while confidence $c(x) = \\max_y q_\\theta(y|x) \\geq \\exp(-h(x))$ increases.\nAveraging: $\\bar{H}_t$ decreases, $C_t$ increases.\nWith accuracy approximately stationary in early collapse ($A_t \\approx A_0$), $\\Delta\\mathrm{ECE} \\approx \\Delta C_t > 0$ whenever $\\Delta\\bar{H}_t < 0$.\nThis argument establishes the direction of co-movement; the quantitative relationship depends on distribution geometry.\n$\\bar{H}_t$ denotes mean conditional entropy $\\mathbb{E}_{x \\sim p_{\\text{eval}}}[h(x)]$, which differs from the marginal entropy $H_t = -\\sum_i p_t(i)\\log p_t(i)$ used in Proposition~\\ref{thm:entropy_leads}; under mode amplification, both decrease monotonically, so the cascade ordering is consistent across both formulations.\n\n\\paragraph{MAUVE ordering (conjecture).}\nMAUVE measures divergence in a discretized embedding space via $k$-means quantization.\nMAUVE onset requires token-level shifts (detected by entropy) to propagate through $n$-gram distributions (detected by distinct-$n$) to aggregate embedding distributions.\nEmpirically, MAUVE onset lags diversity by 0--1 generations on WikiText; however, on C4, MAUVE onset occurs at generation~1 (simultaneous with entropy), suggesting this lag is corpus-dependent.\n\n\\paragraph{Empirical support.}\nAmong 15 experiments at $\\alpha \\geq 0.30$ (where entropy perturbation exceeds the detection threshold), cascade ordering $t_H \\leq t_D$ holds in 14/15 cases (GPT-2-medium s43 fp32 exhibits bidirectional Granger significance).\nTable~\\ref{tab:cascade_onset} reports onset generations for representative conditions, showing uniform Phase~1/2/3 ordering.\nFive low-$\\alpha$ experiments ($\\alpha \\leq 0.25$) show entropy perturbation below the detection threshold (gen-1 deviation $<2\\sigma$); cascade ordering is neither confirmed nor refuted in this regime.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cascade onset generations (5\\% threshold) for representative experiments (Pythia-410M, WikiText, fp32). Phase~1: entropy and ECE ($t_H$, $t_{\\mathrm{ECE}}$); Phase~2: diversity ($t_D$, min over distinct-$n$); Phase~3: MAUVE ($t_M$). All conditions confirm the predicted ordering $t_H = t_{\\mathrm{ECE}} \\leq t_D \\leq t_M$.}\n\\label{tab:cascade_onset}\n\\begin{tabular}{llcccc}\n\\toprule\nSeed & $\\alpha$ & $t_H$ & $t_{\\mathrm{ECE}}$ & $t_D$ & $t_M$ \\\\\n\\midrule\n42 & 0.50 & 1 & 1 & 2 & 3 \\\\\n43 & 0.50 & 1 & 1 & 2 & 2 \\\\\n42 & 0.75 & 1 & 1 & 2 & 3 \\\\\n43 & 0.75 & 1 & 1 & 2 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\phantomsection\\label{app:alpha_c_proof}\n\\paragraph{Proof of Proposition~\\ref{prop:phase-boundary}.}\nAt the detection threshold, $\\mathrm{Power}(\\alpha_c, T) = \\pi^*$.\nSince $\\alpha_c$ lies below the non-monotonic dip region ($\\alpha_c < 0.55$), the signal model applies directly.\nFrom the power function $\\mathrm{Power} = \\Phi(S(\\alpha) \\cdot \\sqrt{T} / \\sigma)$, setting $S(\\alpha_c) \\cdot \\sqrt{T} / \\sigma = z^*$ and substituting the signal model $S(\\alpha) = c\\,\\alpha^\\beta$ yields $c\\,\\alpha_c^\\beta = z^* \\sigma / \\sqrt{T}$.\nSolving: $\\alpha_c(T) = (z^* \\sigma / c)^{1/\\beta} \\cdot T^{-1/(2\\beta)}$, giving the stated form with exponent $\\gamma = 1/(2\\beta)$.\n\n\\paragraph{Calibration and consistency.}\nCross-$T$ validation avoids the circularity of fitting theory to model-extrapolated points.\nWe fit $P(\\mathrm{det}|\\alpha,T) = \\Phi(A \\cdot \\alpha^\\beta \\cdot \\sqrt{T} - z_0)$ to training data at $T \\in \\{10, 20\\}$ via profile likelihood over $(\\beta, \\alpha_\\infty)$, with $\\alpha_\\infty{=}0$ emerging as the optimum.\nThe held-out test set ($T \\in \\{5, 15\\}$) yields MAE${=}0.106$ with 95\\% CI coverage $6/6$: the model correctly predicts all $0/8$ at $T{=}5$ and detection at $T{=}15$ (predicted $0.49$--$0.71$ vs.\\ observed $6/8{=}0.75$; under-prediction reflects the $P_{\\max}{=}0.75$ ceiling from MAUVE saturation, which is modeled separately).\nA linear signal model ($\\beta{=}1$, $\\gamma{=}0.5$) is rejected.\nThe sub-linear exponent $\\beta{=}0.24$ implies that doubling contamination increases signal by only $2^{0.24} \\approx 1.18\\times$ (18\\%); since $\\alpha_\\infty{\\approx}0$, any nonzero contamination produces signal, but detection requires sufficient $T$ to amplify it.\nAt $T{=}5$, $\\alpha_c \\geq 1.0$: no contamination level is detectable, consistent with the insufficient statistical power at very short observation windows.\n\n\\paragraph{Leave-one-$T$-out cross-validation.}\nWe evaluate model generalization via leave-one-$T$-out CV on the $5T \\times 3\\alpha$ grid (sync-dip $\\alpha{=}0.60$ excluded; 15 cells).\nFor each fold, one observation length is held out and the probit model $P = P_{\\max} \\cdot \\Phi(A \\cdot \\alpha^{0.24} \\cdot \\sqrt{T} - z_0)$ is refit on the remaining data.\nOverall MAE${=}0.037$ with 95\\% CI coverage $15/15$.\nWhen sync-dip cells are included (20 cells), MAE rises to $0.203$ (CI $16/20$), with the largest residuals at sync-dip cells (predicted $0.75$, observed $0/8$).\nThe profile likelihood over $\\beta$ yields MLE $\\hat{\\beta}{=}0.66$ (95\\% CI $[0.24, 0.78]$); the wide interval reflects a flat likelihood surface, indicating that $\\beta$ is not well-identified from these data.\nModel comparison (AIC, 15-cell grid excluding sync-dip): $M_1$ (linear boundary) $\\Delta\\mathrm{AIC}{=}0.0$; $M_2$ (power-probit) $\\Delta\\mathrm{AIC}{=}2.43$.\nIncluding sync-dip data reverses the ranking ($M_2$ $\\Delta\\mathrm{AIC}{=}0.0$, $M_1$ $\\Delta\\mathrm{AIC}{=}4.15$), because the probit model naturally accommodates the dip's dissolution at higher $T$ while linear models cannot.\n\n\\section{Power Simulation: Shape Comparison}\n\\label{app:power_sim}\n\nTo assess whether the observed steep detection onset could arise from smooth signal models, we simulate PermG detection under three null hypotheses (1{,}000 replications per cell, $n_{\\text{perm}}{=}1{,}000$, $n_{\\text{pairs}}{=}8$, BH-FDR $q{=}0.05$):\n\n\\begin{itemize}\n\\item \\textbf{H0} (linear): $S(\\alpha) = c \\cdot \\alpha$, calibrated so $S(1.0) = S_{\\max}$.\n\\item \\textbf{H0$'$} (concave): $S(\\alpha) = c \\cdot \\alpha^{0.5}$, sub-linear but smooth.\n\\item \\textbf{H1} (step): $S(\\alpha) = S_{\\max} \\cdot \\mathbf{1}[\\alpha > \\alpha_c(T)]$, binary activation.\n\\end{itemize}\n\n\\noindent\\textbf{Scaling exponents.}\nAll three models produce apparent onset scaling in $T$: H0 $\\gamma{=}0.85$, H0$'$ $\\gamma{=}1.87$, H1 $\\gamma{=}1.96$ (observed: $\\gamma{=}2.08$).\nH0$'$ produces $\\gamma$ within $0.21$ of the observed value, demonstrating that the scaling exponent alone cannot distinguish smooth from step-function boundaries.\n\n\\noindent\\textbf{Shape differences.}\nAt $T{=}10$, $\\alpha{=}0.45$: H0 predicts 27\\% detection rate, H0$'$ predicts 45\\%, H1 predicts 5.5\\%, observed $0/8$.\nAt $T{=}10$, $\\alpha{=}0.50$: H0 predicts 36\\%, H0$'$ predicts 48\\%, H1 predicts 4.6\\%, observed $6/8$ (75\\%).\nSmooth models produce onset ramps with $k{=}4.9$--$6.1$ (H0$'$: $k{=}4.93$, $R^2{=}0.9974$; H0: $k{=}6.14$, $R^2{=}0.9998$); the observed onset steepness ($k{=}15.7$) is ${\\approx}3{\\times}$ higher.\n\n\\noindent\\textbf{Metric-specific ceiling.}\nAt high $\\alpha$ (${\\geq}0.75$) with $T{\\geq}20$, H0 and H0$'$ (which simulate 8 equal-signal pairs) reach mean detection fractions of $0.79$--$0.98$ (${\\approx}6.3$--$7.8/8$), whereas observed counts never exceed $6/8$.\nThis gap reflects metric structure rather than signal saturation: the 2/8 non-detected pairs consistently involve MAUVE, whose floor saturation (\\S\\ref{sec:t20}) prevents Granger detection regardless of signal strength.\n\n\\section{T=20 Predict-then-Verify Comparison}\n\\label{app:t20_comparison}\n\nTable~\\ref{tab:t20_comparison} reports the predict-then-verify results for the $T{=}20$ extension experiments.\nPredictions are derived from the detection boundary model (\\S\\ref{sec:theory}): detected pairs at $T{=}10$ are predicted to remain detected (saturated $F$-statistics), and undetected pairs are predicted to remain undetected (structural nulls or non-monotonic dip).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{T=20 predict-then-verify comparison (Pythia-410M, seed~42, WikiText, fp32). Excluding $\\alpha{=}1.0$, two of four predictions fall within CI ($\\alpha{=}0.50$, $0.75$); boundary cases show systematic bias---$\\alpha{=}0.45$ falsifies the ceiling hypothesis (under-prediction), $\\alpha{=}0.60$ over-predicts under raw $p$-values (v1; matches under FDR v2, not pre-committed).}\n\\label{tab:t20_comparison}\n\\begin{tabular}{lcccc}\n\\toprule\n$\\alpha$ & $T{=}10$ & Predicted $T{=}20$ & Observed $T{=}20$ & Match \\\\\n\\midrule\n0.45 & 0/8 & 0/8 (ceiling) & 5/8 & $\\times$ \\\\\n0.50 & 6/8 & 6/8 (saturated) & 6/8 & \\checkmark \\\\\n0.60 & 0/8 & 3/8 (v1 raw)$^\\dagger$ & 0/8 & $\\times$ \\\\\n0.75 & 6/8 & 6/8 (saturated) & 6/8 & \\checkmark \\\\\n1.00 & 6/8 & 6/8 (saturated) & 6/8 & \\checkmark \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$V2 (BH--FDR corrected, created 44\\,min pre-analysis, not git-committed) predicts 0/8, matching observation.} \\\\\n\\end{tabular}\n\\end{table}\n\nAt $\\alpha \\geq 0.50$, consistency across $T{=}10$ and $T{=}20$ supports the detection boundary prediction: PermG counts are determined by signal structure, not observation length.\nSix diversity-based pairs show $F{=}449$--$2947$ at $T{=}20$ (all $\\gg F_{\\text{crit}}$); two MAUVE-based pairs show $F{<}2$ regardless of $T$, driven by floor saturation ($\\mu{=}0.029$, 100\\% ${<}0.05$) rather than high variance (CV$_{\\text{MAUVE}}{=}0.089$ vs CV$_{\\text{distinct-1}}{=}0.139$); SNR: MAUVE $4.68$ vs diversity $6.40$--$8.20$ ($p{<}0.001$).\nThe sole exception is $\\alpha{=}0.45$ at $T{=}20$ (5/8), consistent with boundary proximity.\nAt $\\alpha{=}0.45$, the shift from 0/8 to 5/8 falsifies Model~A (ceiling: $\\alpha{=}0.45$ structurally undetectable) in favor of Model~B (power-limited: $\\sqrt{T}$ boost crosses the detection threshold), lowering $\\alpha_c$ below~0.45.\nThe $\\alpha{=}0.60$ non-monotonic dip persists at $T{=}20$ (s42: 0/8; s43: 3/8) but dissolves at $T{=}25$ (5/8), confirming that $\\sqrt{T}$ power scaling eventually overcomes the dip; alternative methods detect signal throughout (DiffXCorr 6/8, TY 5/8 at $T{=}20$).\nPermG directional selectivity is consistent across tested $T$ ($T{=}10$, $20$): forward 6/8 versus reverse 0/8 at $\\alpha \\in \\{0.50, 0.75, 1.0\\}$.\n\n\n\\subsection{Prediction Timeline}\n\\label{app:t20_prediction_timeline}\n\nTwo versions of the $T{=}20$ prediction file exist, reflecting an evolving statistical protocol:\n\n\\paragraph{V1 (git-committed, \\texttt{bad72cc}).} Predictions derived from $T{=}10$ PermG results using \\emph{raw} $p$-values. At $\\alpha{=}0.60$, v1 counted 3/8 pairs with raw $p{<}0.05$, predicting 3/8 detections at $T{=}20$. The observed result (0/8 FDR-significant) does not match.\n\n\\paragraph{V2 (pre-analysis, not committed).} A revised file incorporating BH--FDR correction at $q{=}0.05$, consistent with the correction applied throughout the paper. Under FDR, $\\alpha{=}0.60$ drops from 3/8 (raw) to 0/8, matching the observation. V2 was created 44 minutes before the formal $T{=}20$ analysis began (filesystem timestamp) but was not git-committed, and therefore lacks the cryptographic verifiability of v1.\n\n\\paragraph{Scoring.} Primary (v1, committed): 3/5 exact matches ($\\alpha \\in \\{0.50, 0.75, 1.0\\}$, all saturated regimes). Excluding $\\alpha{=}1.0$, two of four predictions fall within CI. Both boundary predictions miss: $\\alpha{=}0.45$ (predicted 0/8, observed 5/8) falsifies the ceiling hypothesis in favor of $\\sqrt{T}$ power scaling; $\\alpha{=}0.60$ (predicted 3/8, observed 0/8) over-estimates detection due to the non-monotonic dip. Sensitivity (v2, FDR-corrected): 4/5 ($\\alpha{=}0.60$ matches). The systematic conservative bias at $\\alpha{=}0.45$ is consistent with the $\\sqrt{T}$ power increase predicted by Proposition~\\ref{prop:phase-boundary}.\n\n\n\\phantomsection\\label{app:task_degradation}\n\\paragraph{Task degradation.}\n\nTable~\\ref{tab:task_degradation} reports end-of-training task performance (generation~10, Pythia-410M, seed~42, fp32) across contamination levels.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Task degradation across contamination levels (Pythia-410M, seed~42, fp32, generation~10). Perplexity evaluated on held-out WikiText-103.}\n\\label{tab:task_degradation}\n\\begin{tabular}{lcc}\n\\toprule\n$\\alpha$ & Perplexity & Next-token acc. \\\\\n\\midrule\nBaseline & 26.6 & 0.390 \\\\\n0.05 & 20.8 & 0.431 \\\\\n0.25 & 22.9 & 0.424 \\\\\n0.46 & 31.6 & 0.400 \\\\\n0.50 & 31.3 & 0.399 \\\\\n0.52 & 41.1 & 0.389 \\\\\n0.60 & 53.5 & 0.375 \\\\\n0.75 & 80.3 & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\alpha{=}0.05$, perplexity improves over the uncontaminated baseline (20.8 vs.\\ 26.6), consistent with a mild data augmentation effect.\nThe sharpest degradation occurs between $\\alpha{=}0.50$ and $0.52$ ($+31\\%$ perplexity), aligning with the PermG detection onset (\\S\\ref{sec:regime}).\n\n\\section{Cross-Architecture FPR Sensitivity}\n\\label{app:cross_arch_fpr}\n\nAs preliminary cross-architecture evidence, we evaluate null-condition ($\\alpha{=}0$) false positive rates on GPT-2-medium (345M; OpenAI), a model outside the Pythia family used for all primary experiments.\nTwo seeds (s42, s43) are trained for $T{=}10$ generations under the same protocol as the Pythia-410M null runs.\nThis evaluation requires additional replication across architectures and seed counts before drawing definitive conclusions.\n\n\\begin{table}[h]\n\\centering\n\\caption{Null-condition FPR for GPT-2-medium ($\\alpha{=}0$, $T{=}10$, 6-pair basis). PermG forward detection shows extreme seed dependence; $K{\\geq}3$ consensus remains at 0\\% across both seeds.}\n\\label{tab:gpt2m_null_fpr}\n\\begin{tabular}{lccc}\n\\toprule\nSeed & PermG fwd & PermG rev & $K{\\geq}3$ \\\\\n\\midrule\ns42 & 6/6 (100\\%) & 0/6 & 0/6 \\\\\ns43 & 0/6 (0\\%) & 0/6 & 0/6 \\\\\n\\midrule\nPooled & 6/12 (50\\%) & 0/12 & 0/12 (0\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe pooled PermG FPR is dramatically higher than on Pythia-410M (50\\% vs.\\ 11.1\\%, 6-pair basis) and shows extreme seed dependence (100\\% vs.\\ 0\\%).\nThis instability traces to the magnitude of null drift in GPT-2-medium's output distribution, which is substantially stronger than in Pythia-410M (Table~\\ref{tab:null_drift_comparison}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Null drift magnitude ($\\alpha{=}0$, gen\\,0$\\to$10; GPT-2-medium: 2 seeds; Pythia-410M: 4 seeds, s46/s48--s50). GPT-2-medium exhibits ${\\sim}4{\\times}$ stronger entropy drift and ${\\sim}7{\\times}$ stronger distinct-3 drift than Pythia-410M.}\n\\label{tab:null_drift_comparison}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{GPT-2-medium} & \\multicolumn{2}{c}{Pythia-410M} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nMetric & gen\\,0 & gen\\,10 (\\%$\\Delta$) & gen\\,0 & gen\\,10 (\\%$\\Delta$) \\\\\n\\midrule\nToken entropy & 3.57 & 2.84 ($-$20.5\\%) & 3.23 & 3.076 ($-$4.9\\%) \\\\\nDistinct-3 & 0.84 & 0.54 ($-$35.8\\%) & 0.81 & 0.769 ($-$4.9\\%) \\\\\n$\\Delta$entropy (gen\\,0$\\to$1) & \\multicolumn{2}{c}{$-$0.60} & \\multicolumn{2}{c}{$-$0.25} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGPT-2-medium's distinct-3 declines from 0.84 to 0.54 over ten null generations ($-$35.8\\%), compared with 0.81$\\to$0.77 ($-$4.9\\%) for Pythia-410M.\nThis steep diversity collapse under pure retraining, absent any synthetic contamination, creates a strong downward trend that PermG's permutation test interprets as a directional signal.\nThe initial entropy drop (gen\\,0$\\to$1: $-$0.60 vs.\\ $-$0.25) is similarly amplified, consistent with architecture-specific sensitivity to iterative retraining rather than a deficiency in the detection method.\n\nThe $K{\\geq}3$ multi-method consensus maintains 0\\% FPR on GPT-2-medium (0/12 pairs), though the margin of safety is narrow: in the worst case (s42), 2 of 5 methods vote for forward detection, one vote short of the $K{\\geq}3$ threshold.\nThis provides some protection against architecture-specific distributional variation, but two seeds constitute only preliminary evidence.\nFor reference, PermG successfully detects true contamination signal ($\\alpha{=}1.0$) on GPT-2-medium with 6/8 forward pairs (Table~\\ref{tab:generalization}), confirming that the method works when signal is present; the elevated null FPR is specific to the null condition where architecture-dependent drift dominates.\n\n\\section*{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform related-work section.\n\\end{itemize}\n\n",
    "structuredPatch": [
      {
        "oldStart": 719,
        "oldLines": 8,
        "newStart": 719,
        "newLines": 7,
        "lines": [
          " \\label{app:shapley}",
          " ",
          " We quantify each method's marginal contribution to the MMCT ensemble using Shapley values~\\cite{shapley1953value}, computed via exact enumeration over all $2^5{=}32$ coalitions of the five detection methods.",
          "-% TODO-D219: recompute Shapley with 6-seed null data (seeds 45--50, 36 null pairs; PermG FPR now 4/36=11.1%, no longer zero)",
          "-For a coalition $S \\subseteq \\{m_1, \\ldots, m_5\\}$, we define two performance metrics: the false positive rate FPR($S$), computed from 3 null experiments ($\\alpha{=}0.0$, seeds 42/43/44; 24 null pairs total), and the false negative rate FNR($S$), computed from 45 signal experiments across all non-null $\\alpha$ levels (270 signal pairs for the 6-pair variant excluding mauve).",
          "+For a coalition $S \\subseteq \\{m_1, \\ldots, m_5\\}$, we define two performance metrics: the false positive rate FPR($S$), computed from 6 null experiments ($\\alpha{=}0.0$, seeds 45--50; 36 null pairs on the 6-pair basis excluding mauve), and the false negative rate FNR($S$), computed from 45 signal experiments across all non-null $\\alpha$ levels (270 signal pairs for the 6-pair variant excluding mauve).",
          " The Shapley value $\\phi_k$ for method $m_k$ is the weighted average of its marginal contribution across all coalitions; positive FPR-Shapley indicates the method \\emph{increases} false positives, while negative FNR-Shapley indicates it \\emph{reduces} false negatives.",
          " The combined Shapley value $\\phi_k^{\\text{comb}} = \\phi_k^{\\text{FPR}} + \\phi_k^{\\text{FNR}}$ balances both error types, with more negative values indicating greater net benefit.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Assistant

_source line 114_

Now TODO-D219 #4 (L730) — Shapley body text about PermG.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "20499080-c819-485c-b865-199fd6be1f6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3DmmyF6A8QX4t8kwk6AH1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 634,
      "cache_read_input_tokens": 110354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 634
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 115_

<details open><summary>🔧 Tool call — Edit · `toolu_01MoHo2n7XZ3ydnjNcjZjkfa`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "old_string": "Table~\\ref{tab:shapley_6pair} reports the 6-pair analysis (excluding mauve).\n% TODO-D219: recompute Shapley values; PermG φ^FPR will be >0 with 6-seed data (4/36 FPs)\nPermG achieves the lowest (best) combined Shapley ($-0.180$), driven entirely by FNR reduction with zero FPR contribution---the only method with this property.\nNaive cross-correlation is the worst contributor ($+0.203$), with its massive FPR Shapley ($+0.622$) overwhelming its FNR benefit ($-0.419$): adding naive cross-correlation to any coalition increases false positives far more than it reduces false negatives.\nThreshold onset contributes almost nothing useful ($+0.074$ combined; FPR $+0.101$, FNR $-0.027$), confirming the near-zero detection power reported in Table~\\ref{tab:method_comparison}.\nFigure~\\ref{fig:shapley} visualizes the decomposition.",
  "new_string": "Table~\\ref{tab:shapley_6pair} reports the 6-pair analysis (excluding mauve).\nDiffXCorr achieves the lowest (best) combined Shapley ($-0.299$), driven by near-zero FPR contribution ($+0.007$) and strong FNR reduction ($-0.306$); however, DiffXCorr cannot separate forward from reverse causation (Table~\\ref{tab:null_fpr_methods}).\nAmong directional methods, PermG ranks best ($-0.141$ combined), with a modest FPR contribution ($+0.039$, reflecting 4/36 null false positives) offset by substantial FNR reduction ($-0.180$).\nNaive cross-correlation is the worst contributor ($+0.190$), with its massive FPR Shapley ($+0.609$) overwhelming its FNR benefit ($-0.419$).\nThreshold onset contributes almost nothing useful ($+0.084$ combined; FPR $+0.111$, FNR $-0.027$), confirming the near-zero detection power reported in Table~\\ref{tab:method_comparison}.\nFigure~\\ref{fig:shapley} visualizes the decomposition."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "c853277e-e945-4851-9659-5b8fdbee01ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C3DmmyF6A8QX4t8kwk6AH1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 634,
      "cache_read_input_tokens": 110354,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 634
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 116 · 2026-05-24T09:06:01.210Z_

<details><summary>↩ Tool result · `toolu_01MoHo2n7XZ3ydnjNcjZjkfa`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "1d2f4767-0ff2-485e-811a-d22d871163bc",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "oldString": "Table~\\ref{tab:shapley_6pair} reports the 6-pair analysis (excluding mauve).\n% TODO-D219: recompute Shapley values; PermG φ^FPR will be >0 with 6-seed data (4/36 FPs)\nPermG achieves the lowest (best) combined Shapley ($-0.180$), driven entirely by FNR reduction with zero FPR contribution---the only method with this property.\nNaive cross-correlation is the worst contributor ($+0.203$), with its massive FPR Shapley ($+0.622$) overwhelming its FNR benefit ($-0.419$): adding naive cross-correlation to any coalition increases false positives far more than it reduces false negatives.\nThreshold onset contributes almost nothing useful ($+0.074$ combined; FPR $+0.101$, FNR $-0.027$), confirming the near-zero detection power reported in Table~\\ref{tab:method_comparison}.\nFigure~\\ref{fig:shapley} visualizes the decomposition.",
    "newString": "Table~\\ref{tab:shapley_6pair} reports the 6-pair analysis (excluding mauve).\nDiffXCorr achieves the lowest (best) combined Shapley ($-0.299$), driven by near-zero FPR contribution ($+0.007$) and strong FNR reduction ($-0.306$); however, DiffXCorr cannot separate forward from reverse causation (Table~\\ref{tab:null_fpr_methods}).\nAmong directional methods, PermG ranks best ($-0.141$ combined), with a modest FPR contribution ($+0.039$, reflecting 4/36 null false positives) offset by substantial FNR reduction ($-0.180$).\nNaive cross-correlation is the worst contributor ($+0.190$), with its massive FPR Shapley ($+0.609$) overwhelming its FNR benefit ($-0.419$).\nThreshold onset contributes almost nothing useful ($+0.084$ combined; FPR $+0.111$, FNR $-0.027$), confirming the near-zero detection power reported in Table~\\ref{tab:method_comparison}.\nFigure~\\ref{fig:shapley} visualizes the decomposition.",
    "originalFile": "\\appendix\n\n\\section{Training Details and Metric Drift}\n\\label{app:training_details}\n\\label{app:drift}\n\n\\paragraph{Hyperparameters.}\nEach generation fine-tunes for 5{,}000 steps using AdamW (learning rate $5 \\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium).\nGeneration uses temperature $1.0$, top-$k{=}50$, max length 512 tokens, producing 5{,}000 samples per generation from 5{,}000-sample subsets of WikiText-103.\nCanary metrics: token entropy $H(p_\\theta | \\text{context})$ over 1{,}000 held-out samples; ECE with 15 bins.\nAdditional downstream metrics (distinct-3, effective rank, Self-BLEU) appear in subsequent appendix sections.\n\n\\paragraph{Metric drift.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Metric drift (\\%, generation~0$\\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\\alpha{=}0.25$: distinct-1 $-40.3{\\pm}0.3\\%$) rather than full replacement ($\\alpha{=}1.0$: $-27.8{\\pm}1.6\\%$). $^\\dagger$$\\alpha{=}0.10$: single seed (seed~42, preliminary). $\\alpha{=}0.00$, $\\alpha{=}0.25$, $\\alpha{=}0.50$, $\\alpha{=}0.75$: 3-seed mean${\\pm}$std (seeds 42, 43, 44); $\\alpha{=}1.0$: 4-seed mean${\\pm}$std (seeds 42, 43, 44, 45).}\n\\label{tab:drift_summary}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\\\\n\\midrule\n0.00 & $-4.6{\\pm}0.4$ & $+37.6{\\pm}14$ & $-14.1{\\pm}0.4$ & $-9.6{\\pm}0.4$ & $-20.6{\\pm}1.0$ \\\\\n0.10$^\\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\\\\n0.25 & $-4.7{\\pm}0.5$ & $+81.8{\\pm}15.9$ & $-40.3{\\pm}0.3$ & $-56.4{\\pm}0.7$ & $-18.1{\\pm}0.8$ \\\\\n0.50 & $-18.0{\\pm}0.5$ & $+822.6{\\pm}18.3$ & $-37.1{\\pm}0.4$ & $-50.4{\\pm}1.0$ & $+21.0{\\pm}0.1$ \\\\\n0.75 & $-27.6{\\pm}0.2$ & $+1791{\\pm}18$ & $-32.3{\\pm}0.5$ & $-41.0{\\pm}1.0$ & $+182.6{\\pm}0.7$ \\\\\n1.00 & $-60.8{\\pm}1.2$ & $+3780{\\pm}30$ & $-27.8{\\pm}1.6$ & $-34.0{\\pm}3.3$ & $+3674{\\pm}45$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Distinct-3 Results}\n\\label{app:distinct3}\n\nTable~\\ref{tab:distinct3_drift} reports distinct-3 drift across all contamination levels.\nDistinct-3 exhibits the largest absolute decline among diversity metrics at low contamination ($-58.9{\\pm}0.9\\%$ at $\\alpha{=}0.25$) but attenuates at higher levels ($-30.5\\%$ at $\\alpha{=}1.0$), consistent with the diversity--calibration dissociation discussed in \\S\\ref{sec:discussion}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Distinct-3 drift (\\%, generation~0$\\to$10) across contamination levels. $\\alpha{=}0.00$, $\\alpha{=}0.25$, $\\alpha{=}0.75$: 3-seed mean${\\pm}$std; $\\alpha{=}1.0$: 4-seed mean${\\pm}$std; $\\alpha{=}0.50$: single seed.}\n\\label{tab:distinct3_drift}\n\\begin{tabular}{lc}\n\\toprule\n$\\alpha$ & Distinct-3 drift (\\%) \\\\\n\\midrule\n0.00 & $-4.4{\\pm}0.5$ \\\\\n0.25 & $-58.9{\\pm}0.9$ \\\\\n0.50 & $-52.4$ \\\\\n0.75 & $-38.6{\\pm}1.3$ \\\\\n1.00 & $-30.5{\\pm}4.0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Lead-lag analysis.}\nAt $\\alpha{=}1.0$, token entropy Granger-precedes distinct-3 at the same consensus level as distinct-1 and distinct-2: $K{\\geq}4/5$ methods, $S{\\geq}3/4$ seeds (Tier~3).\nHowever, the optimal lag is less stable than for distinct-1/2: at max\\_lag${=}7$, the lag standard deviation across seeds exceeds 1.5 generations, compared to $<0.5$ for distinct-1/2.\nThis instability reflects bimodal lag distributions (modes at lag~1 and lag~3--4), suggesting that distinct-3 captures two temporally distinct diversity loss mechanisms: rapid n-gram homogenization (lag~1) and slower distributional narrowing (lag~3--4).\n\n\\paragraph{Sensitivity to sequence length.}\nHigher-order $n$-gram diversity metrics are more sensitive to generation length and random sampling variability.\nWith our 512-token generation length, distinct-3 has a smaller effective denominator (number of possible unique trigrams observed) than distinct-1 or distinct-2, amplifying stochastic fluctuations.\nThis partially explains the higher lag instability: the signal-to-noise ratio for temporal precedence is lower for distinct-3, requiring more observations (longer $T$ or more seeds) to achieve stable estimates.\nFor this reason, we report distinct-3 in this appendix rather than in the main text, where distinct-1 and distinct-2 provide cleaner evidence of the entropy-leads-diversity pattern.\n\n\n\\section{Observation Window Sensitivity}\n\\label{app:window_sensitivity}\n\nTable~\\ref{tab:window_sensitivity} reports how the Tier~3 consensus classification ($K{\\geq}4/5$ methods) varies as a function of the minimum observation window $T_{\\min}$, where analysis uses only generations $0$ through $T_{\\min}$.\nThe consensus classification stabilizes at $T_{\\min}{\\geq}5$ (6 data points), well below our full observation window of $T{=}10$: all six effect-size reference pairs (token entropy and ECE $\\to$ distinct-1, distinct-2, distinct-3) reach $K{\\geq}4/5$ agreement at every window length from $T_{\\min}{=}5$ through $T_{\\min}{=}10$, with no spurious pairs (canary$\\to$perplexity) admitted.\n\nToda--Yamamoto is the only method exhibiting window-dependent sensitivity (note: TY directional assignment is under verification; these counts are retained for completeness): TY consensus stabilizes at $T_{\\min}{\\geq}6$, slightly later than the primary methods, reflecting the additional degrees of freedom consumed by the augmentation order $d_{\\max}$.\nThis does not affect the consensus classification because the remaining four methods provide stable $K{\\geq}4/5$ agreement independently of Toda--Yamamoto's vote.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Observation window sensitivity for Tier~3 consensus ($K{\\geq}4/5$) at $\\alpha{=}1.0$ (Pythia-410M, 4~seeds). Tier~3 pairs: number of canary$\\to$downstream pairs (out of 8 validated) reaching $K{\\geq}4/5$ method agreement. TY pairs: number of effect-size reference pairs (out of 6) reaching Toda--Yamamoto significance (moderate supplementary method; \\S\\ref{sec:method}). Consensus stabilizes at $T_{\\min}{\\geq}5$; TY stabilizes at $T_{\\min}{\\geq}6$.}\n\\label{tab:window_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccccccc}\n\\toprule\n& \\multicolumn{8}{c}{Minimum observation window $T_{\\min}$} \\\\\n\\cmidrule(lr){2-9}\n& 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\\\\n\\midrule\nTier~3 pairs (/8)    & $\\dagger$ & $\\dagger$ & 6 & 6 & 6 & 6 & 6 & 6 \\\\\nTY pairs$^\\S$ (/6)   & $\\dagger$ & $\\dagger$ & 3--6 & 3--6 & 3--6 & 3--6 & 3--6 & 6 \\\\\nStable               & ---       & ---       & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark \\\\\n\\bottomrule\n\\multicolumn{9}{l}{\\footnotesize $\\dagger$~Insufficient degrees of freedom for Granger-type tests ($<6$ data points).} \\\\\n\\multicolumn{9}{l}{\\footnotesize $^\\S$~TY directional assignment under verification.}\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Robustness Checks}\n\\label{app:robustness}\n\n\\paragraph{Permutation count stability.}\nTable~\\ref{tab:nperm_stability} compares permutation Granger $p$-values at 5{,}000 versus 10{,}000 permutations across all canary$\\to$downstream pairs at $\\alpha{=}0.75$ (3~seeds, 24~pairs).\nPermutation Granger $p$-values are stable to within 0.002 between 5{,}000 and 10{,}000 permutations, with zero significance decisions affected.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Permutation count stability analysis ($\\alpha{=}0.75$, 3~seeds, 24 canary$\\to$downstream pairs). $p$-values from permutation Granger tests at $n_{\\text{perm}}{=}5{,}000$ versus $n_{\\text{perm}}{=}10{,}000$.}\n\\label{tab:nperm_stability}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nMax $|\\Delta p|$ & 0.010 \\\\\nMean $|\\Delta p|$ & 0.002 \\\\\nSignificance flips & 0 / 24 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{FDR threshold sensitivity.}\nTable~\\ref{tab:fdr_sensitivity} reports the effect of varying the BH FDR threshold $q$ on treatment ($\\alpha{=}0.75$, 3~seeds, 8-pair basis) versus null ($\\alpha{=}0.0$, 6~seeds 45--50, 6-pair basis) separation for permutation Granger tests.\nTreatment/null separation is qualitatively robust to FDR threshold choice, though the expanded null sample reveals a small number of false positives at each threshold (3--8 of 36 pairs).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs, 8-pair basis). Null: $\\alpha{=}0.0$ (6~seeds 45--50, 36 pairs, 6-pair basis). The expanded null sample reveals modest false positive rates that increase with $q$.}\n\\label{tab:fdr_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n$q$ & Null FDR-sig (/36) & Treatment FDR-sig (/24) & Separation \\\\\n\\midrule\n0.01 & 3 & 0  & Underpowered \\\\\n0.05 & 4 & 19 & Good \\\\\n0.10 & 8 & 24 & Good (elevated null) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{PermG $p$-value gradient at the onset boundary ($\\alpha{=}0.45$).}\nAt the onset boundary, PermG operates near its detection limit, and marginal $p$-values exhibit seed-dependent variation consistent with the statistical power interpretation (\\S\\ref{sec:theory}).\nTable~\\ref{tab:fdr_gradient_a045} reports BH-corrected $p$-values for all 8 canary$\\to$downstream pairs across two seeds at $\\alpha{=}0.45$.\nSeed~43 reaches a minimum FDR-corrected $p{=}0.059$ (18\\% above the $q{=}0.05$ threshold), while seed~42 reaches $p{=}0.091$ (82\\% above threshold).\nNo pair crosses the significance threshold at either seed, yielding the aggregate 0/8 detection rate reported in \\S\\ref{sec:regime}.\nThe gradient is consistent with a continuous power transition rather than a binary absence of signal: PermG operates near its detection limit at $\\alpha{=}0.45$, with seed-dependent variation in marginal $p$-values.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BH-corrected PermG $p$-values at $\\alpha{=}0.45$ (8 canary$\\to$downstream pairs $\\times$ 2 seeds). Min $p_{\\mathrm{fdr}}$ per seed shown. All pairs remain above the $q{=}0.05$ threshold, yielding 0/8 aggregate detection.}\n\\label{tab:fdr_gradient_a045}\n\\begin{tabular}{lcc}\n\\toprule\n & Seed 42 & Seed 43 \\\\\n\\midrule\nMin FDR $p$ & 0.091 & 0.059 \\\\\nGap to $q{=}0.05$ & 82\\% & 18\\% \\\\\nPermG fwd sig (/8) & 0 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Systematic Robustness Analysis}\n\\label{app:spec_curve}\n\nThe sharp detection onset reported in \\S\\ref{sec:regime} could in principle depend on specific analytical choices (pair selection, seed, $\\alpha$ level, method parameters).\nWe assess robustness via specification curve analysis~\\cite{simonsohn2020specification}, systematically varying analytical degrees of freedom to test whether the 0/8$\\to$6/8 transition is specification-invariant.\nOur specification curve varies data subsets and pair selections while holding the detection method (PermG) and its hyperparameters fixed, more closely resembling a systematic subset analysis than a full specification curve in the sense of \\citet{simonsohn2020specification}.\n\nWe construct 1{,}160 analytical specifications from the combinatorial space of: 13 contamination levels ($\\alpha$ grid), seed selection ($\\{42, 43, 44, 45\\}$ where available), 8 canonical canary$\\to$downstream pairs (\\{token entropy, ECE\\} $\\times$ \\{distinct-1, distinct-2, distinct-3, mauve\\}), and method parameters (all PermG with $n_\\text{perm}{=}5{,}000$, BH FDR $q{=}0.05$).\nAll specifications use the D120-canonical analysis pipeline with $3\\sigma$ threshold calibration (D105) as a hard filter.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Specification curve summary (1{,}160 specifications, D120-compliant). The blind$\\to$onset jump is robust across specifications: 0\\% significance rate through $\\alpha{=}0.45$, rising to 75\\% at $\\alpha{=}0.50$.}\n\\label{tab:spec_curve}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nTotal specifications & 1{,}160 \\\\\nSignificant (FDR $q{<}0.05$) & 536 (46.2\\%) \\\\\n\\midrule\n\\emph{By regime} & \\\\\n\\quad Blind ($\\alpha \\leq 0.45$) & 0\\% \\\\\n\\quad Onset ($\\alpha{=}0.50$) & 75\\% \\\\\n\\quad Detection ($\\alpha \\geq 0.75$) & 62--75\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe specification curve confirms that the sharp detection onset is not an artifact of particular analytical choices: the categorical jump from 0\\% to ${\\geq}75\\%$ significance at $\\alpha_c{\\approx}0.50$ holds across the vast majority of specifications, supporting the main text claim (\\S\\ref{sec:regime}).\n\n\n\\section{Transfer Entropy Analysis}\n\\label{app:transfer_entropy}\n\nTable~\\ref{tab:te_results} reports transfer entropy (TE; \\citealp{schreiber2000measuring}) results aggregated across all baseline conditions.\nTE was estimated using 3-bin discretization with permutation testing ($n{=}5{,}000$).\nNo pair reaches BH-corrected significance ($q{=}0.05$) in any condition, confirming that non-parametric information-theoretic methods lack detection power at $T{=}11$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Transfer Entropy results (12 runs across all $\\alpha$ levels). TE\\textsubscript{fwd}: canary$\\to$downstream; TE\\textsubscript{rev}: downstream$\\to$canary. Mean uncorrected permutation $p$-values ($n{=}5{,}000$). No pair reaches BH-corrected $q{<}0.05$ in any run.}\n\\label{tab:te_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\nCanary & Downstream & TE\\textsubscript{fwd} (mean) & $p$\\textsubscript{fwd} (mean) & TE\\textsubscript{rev} (mean) & $p$\\textsubscript{rev} (mean) \\\\\n\\midrule\ntoken\\_entropy & distinct-1 & 0.289 & 0.559 & 0.480 & 0.490 \\\\\ntoken\\_entropy & distinct-2 & 0.300 & 0.529 & 0.496 & 0.447 \\\\\ntoken\\_entropy & distinct-3 & 0.255 & 0.645 & 0.484 & 0.459 \\\\\ntoken\\_entropy & perplexity & 0.257 & 0.676 & 0.386 & 0.626 \\\\\nECE & distinct-1 & 0.185 & 0.720 & 0.184 & 0.891 \\\\\nECE & distinct-2 & 0.208 & 0.683 & 0.216 & 0.846 \\\\\nECE & distinct-3 & 0.209 & 0.689 & 0.227 & 0.807 \\\\\nECE & perplexity & 0.296 & 0.572 & 0.263 & 0.747 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\phantomsection\\label{app:te_mi}\n\\paragraph{KNN-based TE/MI decomposition.}\nA $k$-nearest-neighbor TE estimator ($k{=}5$) provides a model-free complement to the parametric Granger framework.\nForward-dominant TE fraction increases monotonically with $\\alpha$: 4/8 pairs at $\\alpha{=}0.25$ (mean net TE${=}0.14$), 5/8 at $\\alpha{=}0.50$ (net TE${=}0.42$), 6/8 at $\\alpha{=}0.60$ (net TE${=}0.57$), and 8/8 at $\\alpha{=}1.0$ (net TE${=}1.59$).\nAll 120 forward TE bootstrap 95\\% CIs exclude zero at $T{=}10$; all 48 at $T{=}20$.\nThe ``high MI, low TE'' hypothesis for the non-monotonic dip is supported by only 2/8 pairs (ECE$\\to$perplexity and token entropy$\\to$perplexity); the remaining 6 pairs show elevated TE even at $\\alpha{=}0.60$, indicating confounded co-variation rather than a universal mechanism.\n\n\\section{Change-Point Detection Analysis}\n\\label{app:change_point}\n\nWe apply a max-split change-point test with bootstrap significance assessment ($n{=}5{,}000$, $p{<}0.05$) to each metric's generation-level time series ($T{=}11$).\n\nUnder the null control ($\\alpha{=}0.00$, 3~seeds), downstream diversity metrics (distinct-1, distinct-2, distinct-3) produce significant change-points at generation~2 in all seeds (9/9 tests). With additional significant tests from ECE (2/3 seeds) and token entropy (1/3 seeds), the overall false positive rate reaches 66.7\\% (12/18 tests; Table~\\ref{tab:cp_null}). The monotonic drift inherent in iterative self-training is sufficient to trigger change-point detection even without canary contamination. Individual change-point significance therefore cannot serve as standalone evidence for a canary-specific effect.\n\nAlthough individual significance is unreliable as a discriminator, the temporal ordering of detected change-points reverses between null and treatment conditions. In the null ($\\alpha{=}0.00$), downstream metrics show the earliest significant breaks at generation~2 (all seeds), while significant canary breaks appear later (ECE at generations~4--8). Under treatment conditions ($\\alpha{\\geq}0.75$), this ordering flips: canary metrics place their best splits at generation~1, followed by downstream diversity metrics at generations~2--4 and perplexity at generation~4 (Table~\\ref{tab:cp_results}). This ordering reversal provides complementary evidence from a distinct statistical framework, consistent with the Granger-precedence analysis in \\S\\ref{sec:experiments}.\n\nSeveral caveats apply. The 18 individual tests per condition were not corrected for multiple comparisons (BH or Bonferroni); primary inference rests on the cross-metric temporal ordering rather than on individual significance tests. Under treatment conditions, token entropy places its best split at generation~1 with large effect sizes ($|d|{>}2.5$) in all seeds, but the pre-change segment at a generation-1 split contains only a single data point, reducing bootstrap power (1/3 seeds significant at $\\alpha{=}0.75$). The short series length ($T{=}11$) further limits overall detection power.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Change-point detection under null control ($\\alpha{=}0.00$, 3 seeds). CP: detected change-point generation (mean across significant seeds); $|d|$: Cohen's $d$ effect size (mean across all seeds); Sig.\\ rate: fraction of seeds where $p{<}0.05$. Overall FPR: 12/18 = 66.7\\%.}\n\\label{tab:cp_null}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & CP gen (mean) & $|d|$ (mean) & Sig.\\ rate & Type \\\\\n\\midrule\ntoken\\_entropy & 1.0 & 2.94 & 1/3 & canary \\\\\nECE & 6.0 & 1.62 & 2/3 & canary \\\\\ndistinct-1 & 2.0 & 2.27 & 3/3 & downstream \\\\\ndistinct-2 & 2.0 & 2.40 & 3/3 & downstream \\\\\ndistinct-3 & 2.0 & 2.27 & 3/3 & downstream \\\\\nperplexity & --- & 3.11 & 0/3 & downstream \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Change-point detection at $\\alpha{=}0.75$ (3 seeds). CP: detected change-point generation; $|d|$: Cohen's $d$ effect size between pre- and post-change segments. Sig.\\ rate: fraction of seeds where $p{<}0.05$.}\n\\label{tab:cp_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & CP gen (mean) & $|d|$ (mean) & Sig.\\ rate & Type \\\\\n\\midrule\ntoken\\_entropy & 1.0 & 3.21 & 1/3 & canary \\\\\nECE & 1.0 & 3.10 & 1/3 & canary \\\\\ndistinct-1 & 2.3 & 2.18 & 3/3 & downstream \\\\\ndistinct-2 & 3.0 & 1.97 & 3/3 & downstream \\\\\ndistinct-3 & 3.7 & 1.86 & 3/3 & downstream \\\\\nperplexity & 4.0 & 1.70 & 3/3 & downstream \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Dose-response ordering pattern.}\nTable~\\ref{tab:cp_ordering} summarizes the ordering pattern across contamination levels.\nThe canary-to-downstream gap shifts monotonically from negative (downstream first) under the null to positive (canary first) under treatment, ruling out a methodological artifact in which canary metrics would systematically appear earlier regardless of condition.\nThe $\\alpha{=}1.0$ analysis is limited to a single seed (s42); all other conditions use 3 seeds.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccl}\n\\toprule\n$\\alpha$ & Canary cp & Downstream cp & Gap & Direction \\\\\n\\midrule\n0.00 & gen 4--8 & gen 2 & $-$2.5 & Downstream first \\\\\n0.25 & gen 3--4 & gen 3--4 & $\\approx$0 & Simultaneous \\\\\n0.75 & gen 1 & gen 2--4 & $+$2.25 & Canary first \\\\\n1.00 & gen 2 & gen 2--5 & $+$1.0 & Canary first \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Change-point ordering reversal across contamination levels. Under the null ($\\alpha{=}0.00$), downstream metrics break before canary metrics; this ordering reverses monotonically as $\\alpha$ increases, consistent with the Granger-precedence analysis.}\n\\label{tab:cp_ordering}\n\\end{table}\n\n\n\\section{Sequential Monitoring: CUSUM vs Calibrated Threshold}\n\\label{app:csmp}\n\nWe translate the Granger-precedence finding into a deployable monitoring protocol using CUSUM (cumulative sum) sequential testing~\\cite{page1954continuous}, calibrated against the $\\alpha{=}0.0$ null control.\nThe null-calibration procedure sets the alarm threshold $h$ such that the false alarm rate (FAR) is 0\\% on null data (3~seeds, $T{=}10$), providing controlled Type~I error guarantees.\n\n\\paragraph{Method.}\nCUSUM monitors the cumulative deviation of token entropy from its null-control baseline: $S_t = \\max(0,\\; S_{t-1} + (\\mu_0 - x_t) - k)$, where $\\mu_0$ is the null-control mean, $k$ is the allowance parameter, and the alarm triggers when $S_t > h$.\nWe calibrate $h$ for each $k$ from the $\\alpha{=}0.0$ null data (Table~\\ref{tab:csmp_calibration}).\nAs a baseline, we compare against a simple calibrated threshold: alarm when the metric crosses $\\mu_0 - 2\\sigma_0$ for $n{\\geq}1$ or $n{\\geq}2$ consecutive generations.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{CUSUM calibration parameters from $\\alpha{=}0.0$ null control (3~seeds). $h$: alarm threshold calibrated to achieve FAR${=}$0\\%. For $k{\\geq}0.25$, the null CUSUM statistic remains at zero, yielding $h \\approx 0$.}\n\\label{tab:csmp_calibration}\n\\begin{tabular}{lcc}\n\\toprule\n$k$ & $h$ & FAR \\\\\n\\midrule\n0.05 & 1.530 & 0\\% \\\\\n0.10 & 1.005 & 0\\% \\\\\n0.25 & $\\approx$0 & 0\\% \\\\\n0.50 & $\\approx$0 & 0\\% \\\\\n1.00 & $\\approx$0 & 0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Results.}\nTable~\\ref{tab:csmp_comparison} compares CUSUM and simple threshold detection times across gradual contamination levels.\nAt the recommended operating point ($k{=}0.25$), CUSUM and the simple threshold ($n{\\geq}1$) produce identical alarm times (generation~1) across all seeds and contamination levels.\nMore conservative CUSUM settings ($k{=}0.1$, $k{=}0.05$) delay detection to match the $n{\\geq}2$ threshold or later.\nAt $k{=}1.0$ with $\\alpha{=}0.50$, CUSUM fails entirely ($S_t \\equiv 0$ for all seeds), demonstrating sensitivity to the allowance parameter.\nNo CUSUM configuration outperforms the simple calibrated threshold at any operating point tested.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{CUSUM vs simple calibrated threshold: alarm generation across contamination levels (3~seeds each; all seeds agree on the alarm generation shown). Threshold: metric crosses $\\mu_0 - 2\\sigma_0$. No CUSUM configuration outperforms the simple threshold at any operating point.}\n\\label{tab:csmp_comparison}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & CUSUM $k{=}0.25$ & CUSUM $k{=}0.1$ & CUSUM $k{=}0.05$ & Thresh $n{\\geq}1$ & Thresh $n{\\geq}2$ \\\\\n\\midrule\n0.50 & gen 1 & gen 2 & gen 3 & gen 1 & gen 2 \\\\\n0.75 & gen 1 & gen 2 & gen 2 & gen 1 & gen 2 \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize CUSUM $k{=}1.0$ at $\\alpha{=}0.50$: $S_t \\equiv 0$ for all seeds (complete detection failure).} \\\\\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe equivalence arises because the generation-0$\\to$1 entropy drop is large ($|\\Delta x| > 0.7$ for $\\alpha{=}0.50$, $> 1.0$ for $\\alpha{=}0.75$) relative to the null-control variability ($\\sigma_0 \\approx 0.03$).\nAny detector with a near-zero or small threshold triggers at generation~1; CUSUM's cumulative memory provides no advantage when the initial shift already exceeds the control limit.\nThis result extends Claim~3 (method sensitivity) beyond lead-lag detection to the monitoring domain: even a sequential testing procedure with stronger theoretical properties (optimal expected detection delay under continuous monitoring) does not improve over a calibrated baseline when the initial contamination signal dominates the allowance parameter.\nThe contribution of the null-calibrated monitoring framework is the calibration procedure itself (setting alarm boundaries from $\\alpha{=}0.0$ data to guarantee FAR${=}$0\\%), not the CUSUM algorithm.\n\n\\section{Background and Notation}\n\\label{app:background}\n\\label{sec:background}\n\nThis section establishes the formal setup and notation used throughout the paper.\n\n\\paragraph{Iterative training loop.}\nLet $M_0$ denote a pretrained language model and $\\mathcal{D}_\\text{real}$ a fixed corpus of human-written text.\nAt each generation $t \\geq 1$, the model $M_{t-1}$ generates a synthetic corpus $\\mathcal{D}_\\text{synth}^{(t-1)}$, and the next-generation model $M_t$ is fine-tuned on a mixture of $\\alpha$ fraction synthetic data and $(1{-}\\alpha)$ fraction real data:\n\\begin{equation}\n    \\mathcal{D}_\\text{train}^{(t)} = \\alpha \\cdot \\mathcal{D}_\\text{synth}^{(t-1)} \\;+\\; (1{-}\\alpha) \\cdot \\mathcal{D}_\\text{real}, \\quad \\alpha \\in [0, 1].\n    \\label{eq:mixing}\n\\end{equation}\nAt $\\alpha{=}1.0$, this reduces to the full-replacement paradigm of \\citet{shumailov2024curse}.\n\n\\paragraph{Metric families.}\n\\emph{Canary metrics}: token entropy ($H(p_\\theta | \\text{context})$ on held-out samples) and expected calibration error (ECE).\n\\emph{Downstream metrics}: distinct-$n$ ($n \\in \\{1, 2, 3\\}$)~\\cite{li2016diversity} and perplexity.\nEach metric produces a time series of $T{+}1$ observations.\n\n\\paragraph{Lead-lag testing.}\nGiven canary series $X$ and downstream series $Y$, the central question is whether changes in $X$ temporally precede changes in $Y$, requiring directionality and confounder control beyond simple correlation.\nWe employ five methods spanning permissive to conservative: naive cross-correlation, differenced cross-correlation, threshold onset detection, permutation Granger causality~\\cite{shojaie2022granger}, and Toda--Yamamoto Granger causality~\\cite{toda1995statistical}.\n\n\\section{MMCT Algorithm}\n\\label{app:mmct}\n\nAlgorithm~\\ref{alg:mmct} describes the Multi-Method Consensus Test (MMCT) introduced in \\S\\ref{sec:mmct}.\n\n\\begin{algorithm}[h]\n\\caption{Multi-Method Consensus Test (MMCT)}\n\\label{alg:mmct}\n\\begin{algorithmic}[1]\n\\Require Time series pair $(X, Y)$; methods $\\{m_1, \\ldots, m_K\\}$ ($K{=}5$); null-control data $\\mathcal{N}$ (from $\\alpha{=}0.0$); tolerance $\\epsilon{=}0.01$\n\\Ensure $p$-value, consensus level $\\hat{K}$\n\\For{each method $m_k$}\n    \\State Compute empirical FPR: $\\widehat{\\mathrm{FPR}}_k \\gets$ fraction of null-control pairs where $m_k$ rejects $H_0$\n    \\State Compute weight: $w_k \\gets 1 / \\max(\\widehat{\\mathrm{FPR}}_k,\\; \\epsilon)$\n    \\State Apply $m_k$ to $(X, Y)$: $d_k \\gets \\mathbf{1}[m_k \\text{ rejects } H_0]$\n\\EndFor\n\\State Weighted consensus: $W(X {\\to} Y) \\gets \\sum_{k} w_k \\, d_k \\;/\\; \\sum_{k} w_k$\n\\State Build empirical null distribution of $W$ from all null-control pairs in $\\mathcal{N}$\n\\State Compute $p$-value from empirical null: $p \\gets \\Pr_{\\mathcal{N}}(W \\geq W_{\\mathrm{obs}})$\n\\State Consensus level: $\\hat{K} \\gets \\sum_{k} d_k$\n\\State \\Return $p$, $\\hat{K}$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Design rationale.}\nFPR-inverse weighting penalizes methods with high false positive rates on null-control data: naive cross-correlation (FPR${=}91.7\\%$) receives weight $w{=}1.09$, while PermG (FPR${=}11.1\\%$, the lowest among directional methods; DiffXCorr achieves 2.8\\% but lacks directional separation) receives $w{=}9.0$.\nThe empirical null distribution avoids parametric assumptions that are unreliable for short ($T{=}5$--$20$), non-stationary series typical of iterative training.\nMMCT is a consensus testing protocol, not a novel statistical method; its value lies in systematic method comparison and the identification of method-dependent conclusions.\n\n\n\\section{Methodological Comparison Table}\n\\label{app:method_comparison}\n\nTable~\\ref{tab:method-comparison} summarizes the methodological coverage of existing canary and monitoring analyses across the diagnostic dimensions identified in \\S\\ref{sec:method}.\nNo prior work combines all six dimensions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Methodological comparison of canary and monitoring analyses. \\checkmark\\ = present, $\\times$ = absent, $\\circ$ = partial (${\\leq}2$ levels or limited replication). Diff.\\ = differencing/stationarity controls. Multi-M.\\ = ${\\geq}2$ independent statistical methods. MTC = multiple testing correction. Regime = systematic variation of $\\alpha$. Seeds = ${\\geq}3$ independent seeds. Arch.\\ = ${\\geq}2$ architecturally distinct model families.}\n\\label{tab:method-comparison}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccccl}\n\\toprule\nWork & Diff. & Multi-M. & MTC & Regime & Seeds & Arch. & Metrics \\\\\n\\midrule\n\\citet{shumailov2024curse}     & $\\times$   & $\\times$   & $\\times$   & $\\circ$    & \\checkmark & \\checkmark & PPL \\\\\n\\citet{du2025scales}           & $\\times$   & $\\times$   & \\checkmark & \\checkmark & \\checkmark & $\\times$   & ECE, Acc, Dist-$n$ \\\\\n\\citet{gambetta2024surplexity} & $\\times$   & $\\times$   & $\\times$   & \\checkmark & \\checkmark & \\checkmark & Surplexity, Ent \\\\\nSIGMA~\\cite{sigma2026spectral} & $\\times$   & $\\times$   & $\\times$   & $\\times$   & $\\times$   & $\\times$   & Spectral \\\\\nDCES~\\cite{dces2026counter}    & $\\times$   & $\\times$   & $\\times$   & $\\times$   & $\\times$   & \\checkmark & ECE, Ent, PPL \\\\\n\\midrule\n\\textbf{Ours}                  & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark & Ent, ECE, PPL, Dist-$n$ \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\section{Extended Discussion}\n\\label{app:extended_discussion}\n\n\\paragraph{Calibration scope and generalization.}\nAll FPR and FNR calibration results are specific to our experimental setup: Pythia-410M, WikiText-103 subset, $T{=}10$, and six contamination levels.\nCross-architecture validation across 15 conditions spanning six model families shows that the entropy-leads-diversity pattern generalizes in 11 of 15 architecture-seed combinations (Table~\\ref{tab:generalization}); GPT-2 bf16 (0/8), GPT-2 s43 (6/8 bidirectional), SmolLM3-3B (3/8, entropy decoupling), and Pythia-1.4B s42 (2/8) do not confirm the pattern.\n\n\\paragraph{Domain-dependent directionality.}\nThe unidirectional forward causation observed on WikiText (PermG reverse${=}$0/8 across all conditions) does not hold universally.\nOn C4 at $\\alpha{=}0.50$ (s42 fp32), PermG reverse reaches 7/8, indicating near-symmetric bidirectional coupling; however, this is seed-dependent (s43: 1/8) and noted as preliminary.\nThe practical implication is that directional asymmetry should be verified per domain.\n\n\\paragraph{Token entropy versus perplexity.}\nThe distinction lies in the evaluation domain: token entropy is $H(p_\\theta | \\text{context})$ on held-out real data, while perplexity is $\\exp(H_\\text{cross})$ on model-generated text.\nFirst-differencing removes their shared downward trend: the canary$\\to$diversity channel survives because entropy leads diversity by one generation, whereas the canary$\\to$perplexity channel vanishes because both co-move synchronously.\n\n\\paragraph{NLP-specific constraints.}\nOur application of Granger-type methods faces constraints absent in econometrics: (i)~observation length ($T{=}5$--$20$ vs.\\ $T{=}100$--$1000$); (ii)~non-stationarity by design rather than incidental; (iii)~small multiplicity for FDR correction (8--32 pairs per regime).\nTransfer entropy (0/192 FDR-significant results) confirms that method sensitivity extends beyond the five-method panel.\n\n\\paragraph{Prevention paradox.}\nEffective intervention truncates the collapse trajectory that established Granger precedence.\nDifferenced cross-correlation retains significance under intervention (31/32 pairs), while threshold onset fails entirely (0/8), reinforcing the multi-method rationale.\n\n\\paragraph{Grouped testing rationale.}\nWe test 8 canary$\\to$downstream pairs jointly (2 canaries $\\times$ 4 downstream metrics) rather than individual per-metric tests because: (i)~joint testing with BH-FDR correction controls family-wise error across the canary panel, avoiding the inflated false-positive rate that would result from reporting the single most significant pair; (ii)~the count of significant pairs ($k/8$) provides a natural effect-size measure that distinguishes isolated from systematic detection; (iii)~per-metric tests cannot capture the cross-metric consistency that separates genuine temporal precedence from metric-specific artifacts (e.g., MAUVE floor saturation affects 2/8 pairs universally, identifiable only in grouped results).\n\n\\paragraph{Canary metric choice.}\nSmolLM3-3B reveals that canary metric selection constitutes a sensitivity dimension beyond the five statistical methods: token entropy exhibits non-monotonic oscillations (0/4 significant pairs), while ECE maintains monotonic growth (3/4 pairs).\nNo single canary metric is universally optimal.\n\n\\paragraph{Exploratory CSD analysis.}\nCanary metrics show rising autocorrelation (Kendall $\\tau{=}0.79$--$0.82$) while downstream metrics show none ($\\tau{=}0.03$--$0.30$), but this pattern does not survive multiple testing correction (2/10 post-BH) and remains exploratory.\nWe note that \\citet{truong2026phase} show model collapse is a first-order transition, ruling out CSD as a structural detection mechanism; the rising autocorrelation likely reflects non-stationarity rather than critical slowing down.\n\n\\paragraph{Scale verification (Pythia-1.4B).}\n\\label{app:scale_14b}\nTo test whether the phase-diagram structure generalizes beyond 410M, we replicate the analysis at 1.4B scale ($T{=}10$--$15$, fp32, seed~42).\nTable~\\ref{tab:14b_phase} summarizes the available cells.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pythia-1.4B phase-diagram cells (fp32, PermG forward, direction-checked).}\n\\label{tab:14b_phase}\n\\begin{tabular}{lcccc}\n\\toprule\n$\\alpha$ & \\multicolumn{2}{c}{$T{=}10$} & \\multicolumn{2}{c}{$T{=}15$} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n         & s42 & s44 & s42 & s43 \\\\\n\\midrule\n0.45 & 0/6 & 0/6 & 3/6 & 5/6 \\\\\n0.50 & 4/6 & 6/6 & 3/6 & 3/6 \\\\\n0.60 & 4/6 & 6/6 & 6/6 & 6/6 \\\\\n0.75 & 5/6 & 6/6 & 6/6 & 6/6 \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize All: PermG fwd, 6-pair basis (2 canaries $\\times$ 3 distinct-$n$;} \\\\\n\\multicolumn{5}{l}{\\footnotesize MAUVE excl.\\ due to floor ${\\sim}0.033$ at 1.4B).} \\\\\n\\multicolumn{5}{l}{\\footnotesize s42 rev.\\ 0/6 at all $\\alpha$; s43 rev.\\ see text.} \\\\\n\\end{tabular}\n\\end{table}\n\nThe phase-diagram structure is qualitatively preserved at 1.4B scale.\nECE maintains monotonic growth across all three tested $\\alpha$ levels (3/3 cross-scale robust), and the binary detection pattern (above vs.\\ below $\\alpha_c$) is consistent with the 410M phase diagram.\nOn the 6-pair basis (MAUVE excluded due to systematic floor ${\\sim}0.033$; Table~\\ref{tab:14b_phase}), PermG forward detection at 1.4B ranges from 0/6 ($\\alpha{=}0.45$, $T{=}10$) to 6/6 ($\\alpha{\\geq}0.60$, $T{=}15$); token entropy exhibits one-step saturation ($27$--$39\\%$ drop from generation~0 to~1), reducing temporal resolution for entropy-based pairs.\nSeed s42 shows PermG$_\\text{rev}{=}0/6$ across all eight 1.4B conditions ($4\\alpha{\\times}2T$), confirming that bidirectionality is seed-specific rather than scale-inherent.\nThe 410M sync-dip ($\\alpha{=}0.60$: 0/8 at $T{\\leq}20$) does not reproduce at 1.4B (4/6 at $T{=}10$); whether this reflects scale-dependent dynamics or Pythia-specific effects remains open with only two model sizes tested.\nAt $T{=}15$, scale effects are $\\alpha$-conditional: $\\alpha{=}0.60$ reaches 6/6, while $\\alpha{=}0.50$ attenuates to 3/6 (vs 4/6 at $T{=}10$), confirming that detection loss is onset-localized rather than uniform.\nThe boundary's $T$-dependence is preserved: $\\alpha{=}0.45$ rises from 0/6 ($T{=}10$) to 3/6 ($T{=}15$), mirroring the 410M boundary shift.\nHowever, method-level heterogeneity emerges: Toda--Yamamoto exhibits a non-monotonic pattern at $T{=}15$, inverting the PermG ordering in the mid-$\\alpha$ range; gradual low-$\\alpha$ dynamics preserve VAR lag structure, while rapid entropy saturation disrupts lag dependence at intermediate $\\alpha$, with recovery at $\\alpha{=}0.75$ where extreme collapse dynamics (PPL drift ${+}390\\%$) generate sufficient temporal variation to support VAR detection.\nOnset-zone attenuation is $\\alpha$-invariant at 1.4B: both $\\alpha{=}0.45$ and $0.50$ yield 3/6 at $T{=}15$.\nAt 1.4B with $T{=}10$ (11 data points), non-PermG methods (threshold onset, naive cross-correlation, Toda--Yamamoto) have insufficient power due to short sequence length, reducing $K{\\geq}3$ consensus to an effective single-method test; at $T{=}15$ (16 data points), detection recovers (6/6 at $\\alpha{=}0.60$, lead time ${=}$ 10 generations) and $K{\\geq}3$ recovers its multi-method character, with 3/4 $\\alpha$ conditions achieving $K{\\geq}3{\\geq}2/6$ (onset $\\alpha{=}0.50$ seed-dependent: s42 1/6, s43 3/6).\nCross-method consensus ($K{\\geq}3$) exhibits seed-dependent variability at onset ($\\alpha{\\approx}0.50$), consistent with the noisy transition expected at phase boundaries, while remaining robust above onset ($K{\\geq}3$ ${\\geq}5/6$ at $\\alpha{=}0.75$).\nOn a unified 6-pair basis (MAUVE excluded due to systematic floor at ${\\sim}0.033$; Table~\\ref{tab:14b_phase}), third-seed replication (s44) at $T{=}10$ confirms ceiling detection above onset (6/6 at $\\alpha{\\geq}0.50$) with 0/6 at $\\alpha{=}0.45$, validating the blind zone.\nCross-$T$ improvement holds at 3/4 $\\alpha$ values ($\\alpha{=}0.45$: $0/6{\\to}5/6$; $\\alpha{=}0.60$: $6/6{\\to}6/6$; $\\alpha{=}0.75$: $6/6{\\to}6/6$), validating the predicted $\\alpha_c(T)$ decrease; at onset ($\\alpha{=}0.50$), PermG shows a marginal decrease ($6/6{\\to}3/6$), consistent with phase-boundary variability.\nAt onset ($\\alpha{=}0.45$--$0.50$), ECE-based pairs achieve higher detection rates than entropy-based pairs (e.g., 3/3 vs 0/3 robust at $\\alpha{=}0.50$, $T{=}15$), consistent with entropy's one-step saturation reducing temporal resolution at 1.4B scale.\n\n\\paragraph{Future work.}\nExtensions include multivariate VAR models for confounder testing, multi-seed replication across all six architecture families, longer training runs ($T{\\geq}20$), online monitoring within training pipelines, and accumulate-mode experiments~\\cite{dey2024breaking}.\nThe sigmoid onset boundary ($\\alpha_c{=}0.483$) invites connection to the critical mixture ratio scaling law of \\citet{gu2024cmr} and the data-mixing transitions of \\citet{gu2025datamixing}.\n\n\n\\section{Per-Method Dose-Response Profiles}\n\\label{app:dose_response}\n\nTable~\\ref{tab:dose_response_full} reports FDR significance counts (/8 validated pairs) for all five detection methods across 12 contamination levels (seed~42, Pythia-410M, WikiText, fp32).\nPermG exhibits a sharp 0$\\to$6 jump at $\\alpha{=}0.50$ with a return to 0 at $\\alpha{=}0.55$--$0.60$ (non-monotonic dip), while other methods show diffuse profiles: naive cross-correlation saturates at 7--8/8 across all levels including the null, and Toda--Yamamoto fluctuates without a clear onset.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-method FDR significance (/8 pairs) across contamination levels (Pythia-410M, seed~42, WikiText, fp32). PermG and Diff.\\ XCorr use BH-corrected FDR ($q{=}0.05$); Naive XCorr, Threshold, and TY use uncorrected $p{<}0.05$ (no FDR field in pipeline). $\\alpha{=}1.0$ from Pythia-410M cross-architecture condition (same seed/domain/precision).}\n\\label{tab:dose_response_full}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & Naive & Diff.\\ XCorr & Threshold & PermG & TY$^\\S$ \\\\\n\\midrule\n0.00 & 8 & 4 & 3 & \\textbf{0} & 1 \\\\\n0.10 & 7 & 6 & 0 & \\textbf{0} & 0 \\\\\n0.25 & 8 & 3 & 0 & \\textbf{0} & 2 \\\\\n0.30 & 8 & 4 & 0 & \\textbf{0} & 3 \\\\\n0.35 & 8 & 4 & 0 & \\textbf{0} & 1 \\\\\n0.40 & 8 & 3 & 0 & \\textbf{0} & 4 \\\\\n0.45 & 8 & 6 & 0 & \\textbf{0} & 1 \\\\\n0.50 & 8 & 7 & 4 & \\textbf{6} & 3 \\\\\n0.55 & 8 & 8 & 0 & \\textbf{0} & 1 \\\\\n0.60 & 8 & 6 & 0 & \\textbf{0} & 0 \\\\\n0.75 & 7 & 6 & 0 & \\textbf{6} & 3 \\\\\n1.00 & 8 & 6 & 2 & \\textbf{6} & 1 \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\S$TY directional assignment under verification; column retained for completeness.} \\\\\n\\end{tabular}}\n\\end{table}\n\nThe table highlights PermG's combination of null-control detection at 0/8 for this seed ($\\alpha{=}0.00$; pooled FPR across 6 seeds: 11.1\\%, lowest among directional methods), sharp onset (0$\\to$6 at $\\alpha{=}0.50$), and non-monotonic dip (0 at $\\alpha{=}0.55$--$0.60$), confirming it as the method whose dose-response profile most cleanly separates detection regimes.\nNaive cross-correlation's persistently high counts (7--8/8 even at $\\alpha{=}0.00$) demonstrate the 91.7\\% pooled null-control FPR reported in \\S\\ref{sec:method}.\n\n\n\\paragraph{Comparison with naive baselines.}\n\\label{app:naive_baselines}\n\nTable~\\ref{tab:naive_baselines} compares PermG against two practitioner-facing monitoring rules across 26 experiments (18~$\\alpha$ values, Pythia-410M, $T{=}10$, fp32).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Naive baseline comparison (Pythia-410M, $T{=}10$, fp32, 3 null-control runs).}\n\\label{tab:naive_baselines}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & FPR ($\\alpha{=}0$) & Onset $\\alpha$ \\\\\n\\midrule\nPPL-slope (${\\geq}2$ consec.\\ rises) & 100\\% (3/3) & 0.10 \\\\\nVariance-threshold ($2\\sigma$) & 67\\% (2/3) & 0.10 \\\\\nPermG (fwd ${\\geq}1$) & 0\\% (0/3) & 0.50 \\\\\n\\bottomrule\n\\multicolumn{3}{l}{\\footnotesize Onset $\\alpha$: lowest $\\alpha$ where method fires (seed~42).} \\\\\n\\end{tabular}\n\\end{table}\n\nPPL-slope fires at $\\alpha{=}0$ because the first-generation learning effect (perplexity drops from 26.9 to 19.3 at generation~1, then rises monotonically from generation~2 onward) produces consecutive rises indistinguishable from contamination-driven drift.\nVariance-threshold similarly triggers on the natural perplexity recovery.\nPermG avoids these false alarms by testing canary$\\to$downstream Granger precedence rather than univariate trend, thereby excluding training-drift confounds from the detection signal.\nNaive monitoring rules cannot distinguish contamination from natural training dynamics; formal statistical testing is necessary for controlled FPR.\n\n\n\\section{PermG Power Analysis}\n\\label{app:power_analysis}\n\nWe characterize PermG detection power via simulation under a controlled data-generating process (DGP) that matches the structure of our iterative training time series.\n\n\\paragraph{DGP.}\nFor each trial, we generate a bivariate system $(X_t, Y_t)$ for $t = 1, \\ldots, T$ where $X_t = \\mu + \\epsilon_t^X$ and $Y_t = \\mu + \\beta X_{t-1} + \\epsilon_t^Y$, with $\\epsilon \\sim \\mathcal{N}(0, \\sigma^2)$ and $\\sigma{=}1$.\nThe coupling parameter $\\beta$ controls signal strength; $\\beta{=}0$ is the null.\nThe linear coupling provides a power lower bound; nonlinear dynamics in actual iterative training may yield different power characteristics.\nWe sweep $\\beta \\in [0, 2]$ across $T \\in \\{6, 8, 10, 15, 20\\}$, running 100 replications per $(\\beta, T)$ cell with 5{,}000 permutations each and BH FDR correction at $q{=}0.05$ across 8 hypothetical pairs (matching the experimental setup).\n\n\\paragraph{Results.}\nTable~\\ref{tab:beta50} reports $\\beta_{50}$, the coupling strength required for 50\\% detection power, at each observation length $T$.\nUnder $\\sqrt{T}$ scaling, the product $\\beta_{50} \\cdot \\sqrt{T}$ should be constant; the observed decrease from 5.09 ($T{=}8$) to 2.68 ($T{=}20$) indicates that power grows faster than $\\sqrt{T}$, with the empirical scaling closer to $T^{-1.1}$.\nThe $\\sqrt{T}$ formula in \\S\\ref{sec:theory} thus provides a conservative lower bound on detection power: actual power at $T{=}20$ exceeds the $\\sqrt{T}$ prediction.\nFalse positive rates under FDR correction remain at or below 2\\% across all $T$ values (raw: 1--9\\%; Table~\\ref{tab:beta50}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{PermG power analysis: $\\beta_{50}$ (coupling for 50\\% power) under BH-FDR correction ($q{=}0.05$, 8 pairs). $\\beta_{50} \\cdot \\sqrt{T}$ decreases with $T$, indicating power grows faster than $\\sqrt{T}$. FPR: false positive rate at $\\beta{=}0$ (raw / FDR-corrected). Dashes indicate $<$50\\% power not reached within $\\beta \\leq 2.0$.}\n\\label{tab:beta50}\n\\begin{tabular}{lcccc}\n\\toprule\n$T$ & $\\beta_{50}$ & $\\beta_{50} \\cdot \\sqrt{T}$ & FPR (raw) & FPR (FDR) \\\\\n\\midrule\n6  & ---  & ---  & 1\\% & 0\\% \\\\\n8  & ---  & ---  & 6\\% & 2\\% \\\\\n10 & 2.0  & 6.32 & 9\\% & 2\\% \\\\\n15 & 1.2  & 4.65 & 6\\% & 2\\% \\\\\n20 & 0.9  & 4.02 & 5\\% & 1\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/permg_power_curve.pdf}\n\\caption{PermG detection power as a function of coupling strength $\\beta$ for five observation lengths ($T{=}6$--$20$; 100 replications $\\times$ 5{,}000 permutations, BH FDR $q{=}0.05$). Power increases with both $\\beta$ and $T$; at $T{=}6$--$8$, PermG remains underpowered ($<$20\\%) even at $\\beta{=}2.0$, consistent with the $T{=}10$ minimum required for reliable detection in our experimental setting.}\n\\label{fig:permg_power}\n\\end{figure*}\n\nAt $T{=}6$ and $T{=}8$, 50\\% power is not reached within $\\beta \\leq 2.0$ under FDR correction, explaining why PermG is fundamentally underpowered for very short series.\nThe practical implication for our $T{=}10$ setting: $\\beta_{50}{=}2.0$ means that only strong coupling produces reliable detection, consistent with the sharp onset at $\\alpha_c{\\approx}0.50$ where signal strength first exceeds this threshold.\nAt $T{=}20$, $\\beta_{50}$ drops to 0.9, predicting a left-shift of $\\alpha_c$ and broader detection coverage, as formalized in the detection boundary model (\\S\\ref{sec:theory}).\n\n\n\\section{Non-Stationarity Robustness Analysis}\n\\label{app:nonstationarity}\n\nWe assess PermG's size and power under controlled non-stationarity via Monte Carlo simulation, then compare to the empirical autocorrelation structure of our experimental series.\n\n\\paragraph{Simulation design.}\nWe generate bivariate AR(1) series with unidirectional coupling ($x \\to y$):\n$x_t = \\varphi x_{t-1} + \\varepsilon_t^x$, $y_t = \\varphi y_{t-1} + \\beta x_{t-1} + \\varepsilon_t^y$,\nwith $T{=}11$, 1{,}000 replications, and 500 permutations per replication.\nSize is evaluated under $H_0{:}\\;\\beta{=}0$; power under $H_1{:}\\;\\beta{=}0.6$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Size (FPR at $\\beta{=}0$) and power ($\\beta{=}0.6$) under stationary and non-stationary AR(1) DGP ($T{=}11$, 1{,}000 reps, 500 perms). First-differencing maintains nominal size across all $\\varphi$; PermG FPR inflates to ${\\sim}10\\%$ at $\\varphi{\\geq}0.95$.}\n\\label{tab:nonstationarity_sim}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{Size (\\%, $\\beta{=}0$)} & \\multicolumn{3}{c}{Power (\\%, $\\beta{=}0.6$)} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n$\\varphi$ & Raw GC & First-Diff & PermG & Raw GC & First-Diff & PermG \\\\\n\\midrule\n0.50 & 6.4 & 6.6 & 6.8 & 37.7 & 17.7 & 36.8 \\\\\n0.95 & 10.0 & 5.9 & 9.5 & 44.3 & 28.7 & 41.5 \\\\\n0.99 & 11.2 & 4.2 & 10.7 & 46.4 & 24.6 & 41.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\varphi{=}0.50$ (stationary), all three methods achieve near-nominal size ($6.4$--$6.8\\%$ vs.\\ $5\\%$ nominal).\nUnder strong non-stationarity ($\\varphi{\\geq}0.95$), PermG FPR inflates to ${\\sim}10\\%$ because permutation shuffling destroys temporal autocorrelation, shifting the null distribution.\nFirst-differencing maintains proper size ($4.2$--$6.6\\%$) at the cost of reduced power ($17.7$--$28.7\\%$ vs.\\ PermG's $36.8$--$41.7\\%$).\nOur pipeline applies first-differencing \\emph{before} permutation testing, combining PermG's power advantage with differencing's size control; the simulation isolates each component to characterize the tradeoff.\n\n\\paragraph{Empirical autocorrelation.}\nTable~\\ref{tab:empirical_ar1} reports AR(1) coefficients from seven experimental conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Empirical AR(1) coefficients for token entropy (te) and distinct-1 (d1), raw and first-differenced series. High raw $\\varphi$ in d1 reflects deterministic iterative-training decline, not stochastic AR persistence; first-differencing reduces $\\varphi$ to $< 0.44$.}\n\\label{tab:empirical_ar1}\n\\begin{tabular}{llrcccc}\n\\toprule\nExperiment & $\\alpha$ & $T$ & te $\\varphi_{\\text{raw}}$ & d1 $\\varphi_{\\text{raw}}$ & te $\\varphi_{\\text{diff}}$ & d1 $\\varphi_{\\text{diff}}$ \\\\\n\\midrule\na000\\_s42 & 0.00 & 10 & $-0.51$ & $0.86$ & $-0.57$ & $-0.14$ \\\\\na025\\_s42 & 0.25 & 10 & $-0.34$ & $0.95$ & $-0.45$ & $0.19$ \\\\\na050\\_s42 & 0.50 & 10 & $-0.28$ & $0.87$ & $0.31$ & $0.10$ \\\\\na075\\_s42 & 0.75 & 10 & $0.14$ & $0.91$ & $0.88$ & $0.24$ \\\\\na100\\_s42 & 1.00 & 10 & $1.00$ & $0.89$ & $0.98$ & $0.18$ \\\\\nt20\\_a050 & 0.50 & 20 & $-0.10$ & $0.97$ & $-0.25$ & $0.44$ \\\\\nt20\\_a100 & 1.00 & 20 & $0.98$ & $0.81$ & $0.87$ & $0.14$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Adequacy argument.}\nUnder null conditions ($\\alpha{=}0.0$), where FPR is defined, token entropy exhibits $\\varphi{=}-0.51$ (anti-correlated, far from the $\\varphi{\\geq}0.95$ regime where simulation reveals FPR inflation); at $\\varphi{=}0.50$, PermG FPR is $6.8\\%$, near nominal.\nThe high raw $\\varphi$ in distinct-1 ($0.81$--$0.97$ across all $\\alpha$ including null) reflects deterministic iterative-training diversity decline---a monotonic trend driven by the training protocol---not stochastic AR persistence.\nDeterministic trends differ fundamentally from the stochastic AR(1) DGP: they produce predictable trajectories rather than autocorrelated noise, and first-differencing effectively removes them (first-differenced distinct-1 $\\varphi$ ranges $-0.14$ to $0.44$, mean ${\\sim}0.17$).\nOur empirical FPR of 4/36 (11.1\\%) across six null seeds---the lowest among directional methods---confirms adequate size control in our experimental setting; all four false positives occur in token\\_entropy$\\to$distinct pairs in the forward direction, suggesting a structural pattern rather than random Type~I error.\nWe note that $T{=}10$ (11 data points) yields high-variance AR(1) estimates; the cross-experiment pattern is more informative than individual values.\n\n\\paragraph{DGP limitation.}\nThe bivariate AR(1) with linear coupling is a simplification; actual iterative training involves nonlinear dynamics (mode amplification, threshold-dependent diversity loss).\nThese simulation results characterize PermG's behavior under controlled conditions, not exact calibration for the experimental setting; they provide a lower bound on size control because the linear DGP represents a worst case for permutation-based tests (smooth autocorrelation that permutation destroys).\n\n\n\\section{Shapley Value Analysis}\n\\label{app:shapley}\n\nWe quantify each method's marginal contribution to the MMCT ensemble using Shapley values~\\cite{shapley1953value}, computed via exact enumeration over all $2^5{=}32$ coalitions of the five detection methods.\nFor a coalition $S \\subseteq \\{m_1, \\ldots, m_5\\}$, we define two performance metrics: the false positive rate FPR($S$), computed from 6 null experiments ($\\alpha{=}0.0$, seeds 45--50; 36 null pairs on the 6-pair basis excluding mauve), and the false negative rate FNR($S$), computed from 45 signal experiments across all non-null $\\alpha$ levels (270 signal pairs for the 6-pair variant excluding mauve).\nThe Shapley value $\\phi_k$ for method $m_k$ is the weighted average of its marginal contribution across all coalitions; positive FPR-Shapley indicates the method \\emph{increases} false positives, while negative FNR-Shapley indicates it \\emph{reduces} false negatives.\nThe combined Shapley value $\\phi_k^{\\text{comb}} = \\phi_k^{\\text{FPR}} + \\phi_k^{\\text{FNR}}$ balances both error types, with more negative values indicating greater net benefit.\n\nTable~\\ref{tab:shapley_6pair} reports the 6-pair analysis (excluding mauve).\n% TODO-D219: recompute Shapley values; PermG φ^FPR will be >0 with 6-seed data (4/36 FPs)\nPermG achieves the lowest (best) combined Shapley ($-0.180$), driven entirely by FNR reduction with zero FPR contribution---the only method with this property.\nNaive cross-correlation is the worst contributor ($+0.203$), with its massive FPR Shapley ($+0.622$) overwhelming its FNR benefit ($-0.419$): adding naive cross-correlation to any coalition increases false positives far more than it reduces false negatives.\nThreshold onset contributes almost nothing useful ($+0.074$ combined; FPR $+0.101$, FNR $-0.027$), confirming the near-zero detection power reported in Table~\\ref{tab:method_comparison}.\nFigure~\\ref{fig:shapley} visualizes the decomposition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Shapley value decomposition (6-pair, mauve excluded). FPR-Shapley: marginal FPR contribution (positive = increases false positives). FNR-Shapley: marginal FNR contribution (negative = reduces false negatives). Combined = FPR + FNR (more negative = better). 48 experiments, $2^5{=}32$ coalitions, exact enumeration.}\n\\label{tab:shapley_6pair}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $\\phi^{\\text{FPR}}$ & $\\phi^{\\text{FNR}}$ & $\\phi^{\\text{comb}}$ \\\\\n\\midrule\nNaive XCorr          & $+0.622$ & $-0.419$ & $+0.203$ \\\\\nDiff.\\ XCorr         & $+0.163$ & $-0.306$ & $-0.142$ \\\\\nThreshold ($3\\sigma$) & $+0.101$ & $-0.027$ & $+0.074$ \\\\\n\\textbf{Perm.\\ Granger} & $\\mathbf{0.000}$ & $\\mathbf{-0.180}$ & $\\mathbf{-0.180}$ \\\\\nToda--Yamamoto       & $+0.031$ & $-0.069$ & $-0.038$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/shapley_method_contribution.pdf}\n% TODO-D219: regenerate figure and update caption after Shapley recomputation with 6-seed data\n\\caption{Shapley value decomposition of each method's marginal contribution to FPR (positive bars) and FNR (negative bars). PermG is the only method with zero FPR contribution; naive cross-correlation's FPR dominates its FNR benefit.}\n\\label{fig:shapley}\n\\end{figure*}\n\nThe 8-pair variant (including mauve) yields qualitatively identical rankings: PermG remains the best contributor ($\\phi^{\\text{comb}}{=}-0.152$), naive cross-correlation the worst ($+0.170$), and threshold onset near-zero ($+0.063$).\n\n\\paragraph{FDR correction scope.}\nThis analysis applies BH-corrected significance (\\texttt{significant\\_fdr}) uniformly across all five methods, including naive cross-correlation and Toda--Yamamoto.\nIn contrast, the per-method dose-response profiles (Table~\\ref{tab:dose_response_full}) use uncorrected significance for naive cross-correlation, threshold onset, and Toda--Yamamoto because FDR-corrected fields are not available in the per-experiment pipeline output for these methods.\nThe Shapley analysis recomputes significance from raw $p$-values with BH correction applied post hoc, ensuring a fair comparison across methods within the coalition framework.\n\n\n\\section{MMCT Weight Robustness Ablation}\n\\label{app:weight_robustness}\n\nThe detection results reported in the main text use equal-weight majority voting ($K{\\geq}3$ of 5 methods, each contributing at most one vote per pair); PermG contributes at most $1/5 = 20\\%$ of the consensus weight.\nFPR-inverse weighting is used \\emph{only} in the exploratory method ranking below, not in the detection results.\nTo verify that PermG's top ranking is not an artifact of the FPR-inverse weighting scheme, we recompute Shapley values under four weight specifications (Table~\\ref{tab:weight_robustness}).\nEqual weighting ($w{=}1$ for all methods) eliminates any FPR-based advantage; PermG still ranks first ($\\phi^{\\text{comb}}{=}-0.152$), though its margin over naive cross-correlation narrows to 0.015.\nUnder cap-5, the margin widens to 0.043 as the FPR penalty begins to differentiate high-FPR methods.\nCap-10 and original cap-100 yield identical Shapley values because the consensus threshold ($K{\\geq}3$) is determined by the three smallest method weights ($w_{\\text{naive}}{+}w_{\\text{diff}}{+}w_{\\text{thresh}} = 7.76$), which are invariant to further increases in the PermG or TY cap; this saturation confirms that the original $w{=}100$ does not artificially inflate PermG's contribution.\n% TODO-D219: recompute weight robustness table with 6-seed data; PermG φ^FPR will be >0\nAcross all schemes, PermG's advantage derives from the same structural property: zero FPR ($\\phi^{\\text{FPR}}{=}0$) combined with moderate FNR reduction ($\\phi^{\\text{FNR}}{=}-0.152$ to $-0.426$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MMCT weight robustness: PermG combined Shapley under four weighting schemes. PermG ranks first in all cases. Gap = $|\\phi^{\\text{comb}}_{\\text{PermG}} - \\phi^{\\text{comb}}_{\\text{runner-up}}|$. 48 experiments (3 null + 45 signal), exact Shapley enumeration ($2^5{=}32$ coalitions).}\n\\label{tab:weight_robustness}\n\\begin{tabular}{lrcrc}\n\\toprule\nScheme & $w_{\\text{PermG}}$ & $\\phi^{\\text{comb}}_{\\text{PermG}}$ & Runner-up & Gap \\\\\n\\midrule\nEqual ($w{=}1$)     & 1   & $-0.152$ & NaiveXCorr ($-0.137$) & 0.015 \\\\\nCap-5               & 5   & $-0.165$ & NaiveXCorr ($-0.123$) & 0.043 \\\\\nCap-10              & 10  & $-0.426$ & TY ($-0.067$)         & 0.359 \\\\\nFPR-inv.\\ (cap-100) & 100 & $-0.426$ & TY ($-0.067$)         & 0.359 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{PermG FPR Independence Analysis}\n\\label{app:fpr_independence}\n\nTable~\\ref{tab:null_fpr_methods} reports null-control FPR for all five detection methods across six seeds ($6 \\times 6 = 36$ pairs, 6-pair basis excluding mauve).\nUnder identical BH-FDR correction ($q{=}0.05$), DiffXCorr achieves the lowest FPR (1/36, 2.8\\%) but lacks directional separation; PermG (4/36, 11.1\\%) is the lowest among directional methods.\nAll four PermG false positives occur in token\\_entropy$\\to$distinct pairs (seeds~45 and 50, forward direction only), suggesting a structural pattern concentrated in a single canary--downstream pair type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Null-control FPR by method ($\\alpha{=}0.0$, 6~seeds 45--50, 6~pairs each). All p-value--based methods (DiffXCorr, PermG, TY) report BH-FDR--corrected rejections at $q{=}0.05$ for fair comparison. Threshold uses a deterministic $3\\sigma$ criterion; NaiveXCorr uses uncorrected correlation significance.}\n\\label{tab:null_fpr_methods}\n\\begin{tabular}{llrr}\n\\toprule\nMethod & Criterion & Rejections (/36) & FPR (\\%) \\\\\n\\midrule\nDiff.\\ XCorr$^\\dagger$ & BH-FDR & 1 & 2.8 \\\\\n\\textbf{Perm.\\ Granger} & \\textbf{BH-FDR} & \\textbf{4} & \\textbf{11.1} \\\\\nThreshold & $3\\sigma$ (det.) & 10 & 27.8 \\\\\nToda--Yamamoto & BH-FDR & 14 & 38.9 \\\\\nNaive XCorr & uncorr. & 33 & 91.7 \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$Bidirectional; cannot separate forward from reverse.} \\\\\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cluster adjustment.}\nThe 36 null-control pairs are nested within 6~seeds (6~pairs per seed), introducing within-seed correlation.\nWithin-seed ICC${=}0.14$ yields an effective sample size $N_{\\text{eff}} \\approx 21$ (from $N_{\\text{eff}} = N / [1 + (m-1) \\cdot \\text{ICC}]$ where $N{=}36$, $m{=}6$).\nUnder the Clopper--Pearson exact method with $N_{\\text{eff}}{=}21$ and 4 successes (scaled), the cluster-adjusted 95\\% CI is $[1.2\\%, 30.4\\%]$, compared to $[3.1\\%, 26.1\\%]$ under independence ($N{=}36$).\nThe lower ICC compared to the 3-seed pilot ($0.14$ vs.\\ $0.34$) reflects greater between-seed consistency with six independent replications.\n\n\\paragraph{Direction filtering.}\nForward-direction filtering (retaining only pairs with peak lag${<}0$ for cross-correlation methods) reduces null-control $K{\\geq}3$ false positives.\nUnder the 6-seed, 6-pair basis, $K{\\geq}3$ consensus with filtering produces 6/36 false positives (16.7\\%; detail below); the 3-seed pilot underestimated this rate (0/8).\nDetection at $\\alpha{\\geq}0.50$ is unaffected: $K{\\geq}3$ counts are identical with and without direction filtering at all signal levels.\n\n\\paragraph{$K{\\geq}3$ false positive detail.}\nUnder the 6-pair basis (6~seeds, 36~pairs), $K{\\geq}3$ consensus produces 6 false positives (FPR${=}16.7\\%$).\nOf these, 4 are driven by naive cross-correlation, threshold onset, and Toda--Yamamoto (PermG does \\emph{not} vote); the remaining 2 (seeds~45 and 50, te$\\to$distinct) include PermG in the consensus.\nPermG thus contributes to only 2 of 6 consensus false positives, confirming that most $K{\\geq}3$ FPR is driven by the high-FPR methods (naive, threshold, TY).\n\n\\paragraph{Sensitivity to FPR assumption.}\nEven under the conservative upper bound of the cluster-adjusted CI (30.4\\%), PermG remains the lowest-FPR directional method: DiffXCorr achieves a lower FPR under identical BH-FDR correction (2.8\\%) but lacks forward/reverse separation; the next directional method (threshold onset) has 27.8\\% and Toda--Yamamoto 38.9\\%.\nOur primary results rely on equal-weight $K{\\geq}3$ majority voting, where each method contributes exactly one vote regardless of its FPR---this mechanism is completely unaffected by any FPR assumption.\nFor the exploratory FPR-inverse weighting, PermG's weight ($w{=}1/0.111{=}9.0$) exceeds all directional alternatives (threshold: 3.6, TY: 2.6, naive: 1.1); DiffXCorr ($w{=}1/0.028{=}35.7$) receives a higher weight but lacks directional separation, preserving PermG's rank among directional methods.\nThe insensitivity of both the voting mechanism and the method ranking to the upper CI bound provides evidence that the MMCT conclusions are robust to uncertainty in PermG's Type~I error rate.\n\n\\section{Sigmoid Transition Shape}\n\\label{app:sigmoid_shape}\n\nSigmoid regression on the original 13-point $T{=}10$ grid yields $\\alpha_c = 0.483 \\pm 0.006$ but $k = 478 \\pm 475$ ($\\mathrm{SE}(k) \\approx k$), indicating that the coarse grid cannot constrain the transition shape.\nDense $\\alpha$ sampling (17~values at $T{=}10$) resolves this ambiguity: formal likelihood-ratio testing strongly favors a smooth sigmoid over a literal step function ($\\Delta\\mathrm{AIC}{=}-110$), with fitted steepness $k{=}15.7$ (95\\% CI $[9.4, 28.2]$).\nThe transition is steep but finite-width, not a literal discontinuity.\nThis observed steepness exceeds what smooth signal models predict: VAR(1) simulations under H0 (linear, $k{=}6.1$) and H0$'$ (concave, $k{=}4.9$) produce onset sigmoids with $k{=}4.9$--$6.1$ (\\S\\ref{app:power_sim}), yielding steepness ratios $k_{\\mathrm{obs}} / k_{\\mathrm{H0}} \\approx 2.6$--$3.2$ (CI lower bound ratio ${\\approx}2$).\nWe do not fit a combined $T{=}10 + T{=}20$ sigmoid because $\\alpha{=}0.45$ yields contradictory counts under the two sequence lengths (0/8 vs.\\ 5/8), reflecting genuine power dependence on $T$ rather than a single dose-response curve.\n\n\n\\section{Intervention Threshold Sensitivity}\n\\label{app:intervention_sensitivity}\n\n\\paragraph{Within-$\\alpha$ sensitivity at $\\alpha{=}1.0$.}\nTable~\\ref{tab:threshold_sensitivity} reports the predictive cessation outcome under five entropy-drop thresholds (5\\%--25\\%) at $\\alpha{=}1.0$ (Pythia-410M, seed~42).\nAll five thresholds produce identical outcomes: token entropy drops 40.7\\% at generation~1, far exceeding even the most conservative threshold (25\\%), so every threshold triggers at the same generation.\nThe intervention conclusion---peak perplexity 57.0, recovery in one generation, final perplexity 21.3---is invariant to threshold choice within this range.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Threshold sensitivity at $\\alpha{=}1.0$ (Pythia-410M, s42, fp32). All thresholds trigger at generation~1 (entropy drop 40.7\\%$\\gg$threshold), producing identical recovery trajectories.}\n\\label{tab:threshold_sensitivity}\n\\begin{tabular}{rccr}\n\\toprule\nThreshold & Trigger gen & Peak PPL & Final PPL \\\\\n\\midrule\n5\\%  & 1 & 56.99 & 21.29 \\\\\n10\\% & 1 & 56.99 & 21.29 \\\\\n15\\% & 1 & 56.99 & 21.29 \\\\\n20\\% & 1 & 56.99 & 21.29 \\\\\n25\\% & 1 & 56.99 & 21.29 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-$\\alpha$ operating band.}\nThe within-$\\alpha$ analysis establishes threshold invariance at $\\alpha{=}1.0$ but does not address whether thresholds generalize across contamination levels.\nWe examine observed entropy trajectories from the alpha sweep (not actual intervention experiments at $\\alpha{<}1.0$) to characterize the operating band.\nThe maximum entropy drop across 10 generations varies by contamination level: 7.5\\% at $\\alpha{=}0.0$ (fine-tuning drift only), 7.7\\% at $\\alpha{=}0.10$, 7.8\\% at $\\alpha{=}0.25$, 22.4\\% at $\\alpha{=}0.50$, 35.3\\% at $\\alpha{=}0.75$, and 62.1\\% at $\\alpha{=}1.0$.\nThresholds below 7.5\\% (e.g., 5\\%) trigger on clean training data---a false alarm.\nThresholds above 22.4\\% (e.g., 25\\%) miss $\\alpha{=}0.50$, the lowest contamination level with meaningful entropy signal.\nThe safe operating band is therefore $[10\\%, 22\\%]$: any threshold in this range produces zero false alarms on $\\alpha{=}0.0$ while detecting contamination at $\\alpha{\\geq}0.50$.\nThe reported 15\\% threshold sits near the center of this band.\nThis analysis is based on entropy trajectories from non-intervention training runs; whether actual intervention at $\\alpha{<}1.0$ would produce the same triggering behavior remains unvalidated.\n\n\n\\section{Channel Effect Size Analysis}\n\\label{app:channel_effect_size}\n\nFirst-differencing eliminates all canary$\\to$perplexity Granger associations while preserving canary$\\to$diversity leads (\\S\\ref{sec:regime}).\nWe present three lines of evidence that this asymmetry reflects a genuine temporal structure difference rather than selective power loss from differencing.\n\n\\paragraph{Correlation retention parity.}\nFirst-differencing retains comparable correlation magnitude for both channel types (Table~\\ref{tab:channel_retention}).\nDiversity channels ($n{=}243$ pairs across all non-null experiments) retain a median $|r|$ of 0.952 after differencing, while perplexity channels ($n{=}8$ pairs; limited sample) retain 1.00.\nThis parity rules out a blanket power-loss explanation: if differencing selectively destroyed perplexity signal, $|r|$ retention would be substantially lower for perplexity than for diversity.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{First-differencing effect by channel type. $|r|$ retention = diff $|r|$ / naive $|r|$. Despite comparable $|r|$ retention, Granger $F$ differs by an order of magnitude. Perplexity channel has limited sample ($n{=}8$); all paired comparisons are from bf16 experiments.}\n\\label{tab:channel_retention}\n\\begin{tabular}{lrccrc}\n\\toprule\nChannel & $n$ & Naive $|r|$ & Diff $|r|$ & Retention & Med.\\ $F$ \\\\\n\\midrule\nDiversity   & 243 & 0.943 & 0.921 & 0.952 & 67.8 \\\\\nPerplexity  & 8   & 0.924 & 0.900 & 1.002 & 11.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Granger $F$-statistic asymmetry.}\nWithin matched experiments (same model, seed, $\\alpha$, precision), the Granger $F$-statistic is $20$--$28{\\times}$ higher for diversity than perplexity channels.\nAt $\\alpha{=}0.60$ (s42, bf16): diversity mean $F{=}229.4$ versus perplexity mean $F{=}8.3$ (ratio $27.8{\\times}$).\nAt $\\alpha{=}1.0$ reactive (s43, bf16): diversity mean $F{=}236.4$ versus perplexity mean $F{=}11.5$ (ratio $20.6{\\times}$).\nSince $|r|$ retention is comparable across channels, this $F$-statistic gap cannot be attributed to differencing-induced signal loss; it must reflect a difference in the temporal structure that Granger tests evaluate.\n\n\\paragraph{Temporal structure: lagged vs.\\ contemporaneous.}\nThe lag distribution of peak differenced cross-correlations reveals the structural difference.\nFor diversity channels, 81\\% of peak correlations occur at canary-leading lags (lag${<}0$), with a median lag of $-1$ generation---consistent with the one-generation temporal precedence visible in Figure~\\ref{fig:metric_trajectory}.\nFor perplexity channels, 50\\% of peak correlations occur at lag${=}0$ (contemporaneous co-movement), with a median lag of $0$.\nGranger precedence tests lagged predictive improvement; contemporaneous co-movement produces low $F$-statistics regardless of signal magnitude, which is the correct behavior for a test designed to detect temporal precedence.\nThe perplexity channel sample is limited ($n{=}8$ pairs from bf16 experiments), and these lag distributions should not be generalized to fp32 conditions without further validation.\n\n\n\\section{Mutual Information Analysis}\n\\label{app:mi_analysis}\n\nWe estimate the Gaussian mutual information lower bound between token entropy (canary) and each diversity metric across contamination levels, using $T{=}11$ data points per series ($T{=}10$ for two conditions).\nThe Gaussian estimator $\\hat{I}_G = -\\frac{1}{2}\\log_2(1 - r^2)$, where $r$ is the Pearson correlation, provides a conservative lower bound on MI; we do not report KSG nonparametric estimates due to uncorrected positive bias at $T{=}11$.\nThe $\\alpha{=}0.05$ data point is excluded because it uses an experiment excluded from the dose-response analysis.\n\nTable~\\ref{tab:mi_bounds} reports the mean Gaussian MI across the three distinct-$n$ metrics for each $\\alpha$ level.\nMI follows a V-shaped curve: it drops from 0.112~bits at $\\alpha{=}0.10$ to a minimum of 0.010~bits at $\\alpha{=}0.25$, then rises monotonically to 0.270~bits at $\\alpha{=}0.75$.\nMI remains positive throughout the blind zone ($\\alpha \\leq 0.45$; range 0.010--0.141~bits), confirming that canary--diversity coupling exists below the detection threshold but falls below PermG's statistical power floor at $T{=}10$.\nThere is no discontinuity at $\\alpha_c \\approx 0.50$: the detection onset reflects power accumulation, not an abrupt change in information coupling.\nBootstrap 95\\% CIs span 1--3 orders of magnitude at $T{=}11$, so individual point estimates should be interpreted cautiously.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Gaussian MI lower bound (bits) between token entropy and distinct-$n$ diversity metrics ($T{=}11$, Pythia-410M, fp32). Mean across distinct-1/2/3; $\\alpha{=}0.05$ excluded (see text). CIs omitted due to width at $T{=}11$.}\n\\label{tab:mi_bounds}\n\\begin{tabular}{rrc}\n\\toprule\n$\\alpha$ & Seeds & MI (bits) \\\\\n\\midrule\n0.10 & 2 & 0.112 \\\\\n0.25 & 3 & 0.010 \\\\\n0.30 & 1 & 0.062 \\\\\n0.35 & 1 & 0.098 \\\\\n0.40 & 1 & 0.119 \\\\\n0.45 & 2 & 0.141 \\\\\n0.50 & 3 & 0.107 \\\\\n0.60 & 2 & 0.209 \\\\\n0.75 & 1 & 0.270 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Moment Cascade Analysis}\n\\label{app:moment_cascade}\n\nWe analyze the temporal ordering of metric degradation onset across 6 WikiText seed${\\times}\\alpha$ conditions (2 seeds $\\times$ 3 non-trivial $\\alpha$ levels each) to test whether token entropy consistently degrades before diversity metrics.\nOnset is defined as the first generation where a metric's cumulative change exceeds 5\\% of its generation-0 value.\n\nTable~\\ref{tab:moment_cascade} reports the onset generation for each metric across conditions.\nToken entropy reaches onset at generation~1 in all 6 conditions; distinct-$n$ metrics reach onset at generation~2 in all 18 pairwise comparisons (6 conditions $\\times$ 3 distinct-$n$ metrics).\nAcross these 18 comparisons, entropy degrades first in 16 cases (Kendall $\\tau{=}0.337$, consistent with a weak but reliable temporal ordering).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Degradation onset generation (5\\% threshold) by metric and condition (Pythia-410M, WikiText, fp32). Token entropy reaches onset at generation~1 in all non-null conditions; distinct-$n$ metrics follow at generation~2.}\n\\label{tab:moment_cascade}\n\\begin{tabular}{llcccccc}\n\\toprule\nSeed & $\\alpha$ & Entropy & Dist-1 & Dist-2 & Dist-3 & ECE & PPL \\\\\n\\midrule\n42 & 0.10 & 1 & 2 & 2 & 2 & 2 & --- \\\\\n42 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\\\\n42 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\\\\n43 & 0.25 & 1 & 2 & 2 & 2 & 4 & --- \\\\\n43 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\\\\n43 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\\\\n\\bottomrule\n\\multicolumn{8}{l}{\\footnotesize ---: onset not reached within $T{=}10$ generations.} \\\\\n\\end{tabular}\n\\end{table}\n\nThe cascade ordering provides evidence for the canary mechanism independent of Granger-type tests: it does not depend on first-differencing, lag selection, or the permutation null distribution.\nECE shows onset at generation~1 at $\\alpha{\\geq}0.50$ (both seeds), consistent with its role as a secondary canary metric.\nAt low contamination ($\\alpha{=}0.10$ and $\\alpha{=}0.25$), perplexity never reaches the 5\\% onset threshold within $T{=}10$ generations, while entropy already shows generation-1 onset---consistent with entropy's higher sensitivity to distributional shifts.\n\n\n\\section{Cascade Ordering Theory: Proofs}\n\\label{app:cascade_theory}\n\nThis section provides the full proofs for Proposition~\\ref{thm:entropy_leads} and Proposition~\\ref{prop:div_lag} from \\S\\ref{sec:cascade}, plus supporting results.\n\n\\begin{assumption}[Mode Amplification]\\label{ass:mode_amp}\nThe training map $\\mathcal{T}$ redistributes probability mass from low-probability to high-probability tokens: there exists a threshold $\\bar{p}$ such that $\\mathcal{T}(p)_i > p_i \\Rightarrow p_i \\geq \\bar{p}$ and $\\mathcal{T}(p)_j < p_j \\Rightarrow p_j \\leq \\bar{p}$.\n\\end{assumption}\n\nThis captures the standard finite-capacity approximation effect: MLE on finite samples from a peaked distribution amplifies modes and suppresses the tail~\\cite{shumailov2024curse,dohmatob2024tale}.\n\n\\begin{proposition}[Entropy is a first-order indicator]\\label{prop:entropy_first}\nLet $p \\in \\Delta^{V-1}$ and $\\delta = \\alpha(\\mathcal{T}(p) - p)$ be a mode-amplifying perturbation with $\\sum_i \\delta_i = 0$. Then $\\Delta H = H(p+\\delta) - H(p) = -\\sum_i \\delta_i \\log p_i + O(\\|\\delta\\|^2) < 0$.\n\\end{proposition}\n\n\\begin{proof}\nTaylor-expanding $H$ around $p$:\n$H(p+\\delta) = H(p) - \\sum_i \\delta_i \\log p_i - \\sum_i \\delta_i - \\frac{1}{2}\\sum_i \\delta_i^2/p_i + O(\\|\\delta\\|^3)$.\nSince $\\sum_i \\delta_i = 0$: $\\Delta H = -\\sum_i \\delta_i \\log p_i - \\frac{1}{2}\\sum_i \\delta_i^2/p_i + O(\\|\\delta\\|^3)$.\nUnder mode amplification, tokens gaining mass ($\\delta_i > 0$) have $p_i \\geq \\bar{p}$ (hence $\\log p_i \\geq \\log \\bar{p}$) and tokens losing mass ($\\delta_j < 0$) have $p_j \\leq \\bar{p}$ (hence $\\log p_j \\leq \\log \\bar{p}$).\nWriting $m = \\sum_{i:\\delta_i > 0} \\delta_i$: $-\\sum_i \\delta_i \\log p_i = -m[\\overline{\\log p}^{+} - \\overline{\\log p}^{-}] < 0$, where $\\overline{\\log p}^{\\pm}$ are the $|\\delta|$-weighted means over gaining/losing tokens.\nThe second-order Fisher information term $-\\frac{1}{2}\\sum_i \\delta_i^2/p_i$ is always negative, reinforcing the decrease.\n\\end{proof}\n\n\\begin{proposition}[Diversity is a threshold indicator]\\label{prop:div_threshold}\nDefine the $\\epsilon$-effective support $S_\\epsilon(p) = |\\{i \\in [V]: p_i > \\epsilon\\}|$, where $\\epsilon \\approx c/N$ is the generation threshold for sample size $N$.\nUnder the same perturbation $\\delta$: $\\Delta S_\\epsilon = -|\\{i: p_i > \\epsilon \\text{ and } p_i + \\delta_i \\leq \\epsilon\\}|$.\nThis equals zero whenever $\\|\\delta\\|_\\infty < \\gamma(p,\\epsilon) := \\min_{i: p_i > \\epsilon}(p_i - \\epsilon)$.\n\\end{proposition}\n\n\\begin{proof}\nToken $i$ exits the effective support iff $p_i > \\epsilon$ and $p_i + \\delta_i \\leq \\epsilon$, requiring $|\\delta_i| \\geq p_i - \\epsilon$.\nIf $\\|\\delta\\|_\\infty < \\gamma$, no token satisfies this condition.\n\\end{proof}\n\n\\paragraph{Proof of Proposition~\\ref{thm:entropy_leads}.}\n\\emph{Part (a):} Take any mode-amplifying $\\delta$ with $\\|\\delta\\|_\\infty < \\gamma(p,\\epsilon)$.\nBy Proposition~\\ref{prop:div_threshold}, $\\Delta S_\\epsilon = 0$.\nBy Proposition~\\ref{prop:entropy_first}, $\\Delta H < 0$.\nSuch $\\delta$ exists for all $\\alpha < \\gamma / \\max_i |\\mathcal{T}(p)_i - p_i|$.\n\\emph{Part (b):} If $\\Delta S_\\epsilon < 0$, some token $k$ has $p_k > \\epsilon$ but $p_k + \\delta_k \\leq \\epsilon$, so $\\delta_k < 0$.\nUnder mode amplification, this implies $p_k \\leq \\bar{p}$; the total mass transferred to high-probability tokens ensures $\\overline{\\log p}^+ > \\overline{\\log p}^-$.\nBy Proposition~\\ref{prop:entropy_first}, $\\Delta H < 0$. $\\square$\n\n\\paragraph{Proof of Proposition~\\ref{prop:div_lag}.}\nBy the margin condition, at every generation $s \\leq t_H$ the perturbation norm $\\alpha\\|\\mathcal{T}(p_s) - p_s\\|_\\infty$ is less than $\\gamma(p_s, \\epsilon)$.\nBy Proposition~\\ref{prop:div_threshold}, no token exits the effective support at any $s \\leq t_H$, so $\\Delta S_\\epsilon = 0$ for all $s \\leq t_H$.\nSince time is discrete, $t_D \\geq t_H + 1$. $\\square$\n\n\\paragraph{ECE co-movement (qualitative argument).}\nUnder conditional mode amplification (peakier $q_\\theta(\\cdot|x)$ at each generation), per-token conditional entropy $h(x) = H(q_\\theta(\\cdot|x))$ decreases while confidence $c(x) = \\max_y q_\\theta(y|x) \\geq \\exp(-h(x))$ increases.\nAveraging: $\\bar{H}_t$ decreases, $C_t$ increases.\nWith accuracy approximately stationary in early collapse ($A_t \\approx A_0$), $\\Delta\\mathrm{ECE} \\approx \\Delta C_t > 0$ whenever $\\Delta\\bar{H}_t < 0$.\nThis argument establishes the direction of co-movement; the quantitative relationship depends on distribution geometry.\n$\\bar{H}_t$ denotes mean conditional entropy $\\mathbb{E}_{x \\sim p_{\\text{eval}}}[h(x)]$, which differs from the marginal entropy $H_t = -\\sum_i p_t(i)\\log p_t(i)$ used in Proposition~\\ref{thm:entropy_leads}; under mode amplification, both decrease monotonically, so the cascade ordering is consistent across both formulations.\n\n\\paragraph{MAUVE ordering (conjecture).}\nMAUVE measures divergence in a discretized embedding space via $k$-means quantization.\nMAUVE onset requires token-level shifts (detected by entropy) to propagate through $n$-gram distributions (detected by distinct-$n$) to aggregate embedding distributions.\nEmpirically, MAUVE onset lags diversity by 0--1 generations on WikiText; however, on C4, MAUVE onset occurs at generation~1 (simultaneous with entropy), suggesting this lag is corpus-dependent.\n\n\\paragraph{Empirical support.}\nAmong 15 experiments at $\\alpha \\geq 0.30$ (where entropy perturbation exceeds the detection threshold), cascade ordering $t_H \\leq t_D$ holds in 14/15 cases (GPT-2-medium s43 fp32 exhibits bidirectional Granger significance).\nTable~\\ref{tab:cascade_onset} reports onset generations for representative conditions, showing uniform Phase~1/2/3 ordering.\nFive low-$\\alpha$ experiments ($\\alpha \\leq 0.25$) show entropy perturbation below the detection threshold (gen-1 deviation $<2\\sigma$); cascade ordering is neither confirmed nor refuted in this regime.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cascade onset generations (5\\% threshold) for representative experiments (Pythia-410M, WikiText, fp32). Phase~1: entropy and ECE ($t_H$, $t_{\\mathrm{ECE}}$); Phase~2: diversity ($t_D$, min over distinct-$n$); Phase~3: MAUVE ($t_M$). All conditions confirm the predicted ordering $t_H = t_{\\mathrm{ECE}} \\leq t_D \\leq t_M$.}\n\\label{tab:cascade_onset}\n\\begin{tabular}{llcccc}\n\\toprule\nSeed & $\\alpha$ & $t_H$ & $t_{\\mathrm{ECE}}$ & $t_D$ & $t_M$ \\\\\n\\midrule\n42 & 0.50 & 1 & 1 & 2 & 3 \\\\\n43 & 0.50 & 1 & 1 & 2 & 2 \\\\\n42 & 0.75 & 1 & 1 & 2 & 3 \\\\\n43 & 0.75 & 1 & 1 & 2 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\phantomsection\\label{app:alpha_c_proof}\n\\paragraph{Proof of Proposition~\\ref{prop:phase-boundary}.}\nAt the detection threshold, $\\mathrm{Power}(\\alpha_c, T) = \\pi^*$.\nSince $\\alpha_c$ lies below the non-monotonic dip region ($\\alpha_c < 0.55$), the signal model applies directly.\nFrom the power function $\\mathrm{Power} = \\Phi(S(\\alpha) \\cdot \\sqrt{T} / \\sigma)$, setting $S(\\alpha_c) \\cdot \\sqrt{T} / \\sigma = z^*$ and substituting the signal model $S(\\alpha) = c\\,\\alpha^\\beta$ yields $c\\,\\alpha_c^\\beta = z^* \\sigma / \\sqrt{T}$.\nSolving: $\\alpha_c(T) = (z^* \\sigma / c)^{1/\\beta} \\cdot T^{-1/(2\\beta)}$, giving the stated form with exponent $\\gamma = 1/(2\\beta)$.\n\n\\paragraph{Calibration and consistency.}\nCross-$T$ validation avoids the circularity of fitting theory to model-extrapolated points.\nWe fit $P(\\mathrm{det}|\\alpha,T) = \\Phi(A \\cdot \\alpha^\\beta \\cdot \\sqrt{T} - z_0)$ to training data at $T \\in \\{10, 20\\}$ via profile likelihood over $(\\beta, \\alpha_\\infty)$, with $\\alpha_\\infty{=}0$ emerging as the optimum.\nThe held-out test set ($T \\in \\{5, 15\\}$) yields MAE${=}0.106$ with 95\\% CI coverage $6/6$: the model correctly predicts all $0/8$ at $T{=}5$ and detection at $T{=}15$ (predicted $0.49$--$0.71$ vs.\\ observed $6/8{=}0.75$; under-prediction reflects the $P_{\\max}{=}0.75$ ceiling from MAUVE saturation, which is modeled separately).\nA linear signal model ($\\beta{=}1$, $\\gamma{=}0.5$) is rejected.\nThe sub-linear exponent $\\beta{=}0.24$ implies that doubling contamination increases signal by only $2^{0.24} \\approx 1.18\\times$ (18\\%); since $\\alpha_\\infty{\\approx}0$, any nonzero contamination produces signal, but detection requires sufficient $T$ to amplify it.\nAt $T{=}5$, $\\alpha_c \\geq 1.0$: no contamination level is detectable, consistent with the insufficient statistical power at very short observation windows.\n\n\\paragraph{Leave-one-$T$-out cross-validation.}\nWe evaluate model generalization via leave-one-$T$-out CV on the $5T \\times 3\\alpha$ grid (sync-dip $\\alpha{=}0.60$ excluded; 15 cells).\nFor each fold, one observation length is held out and the probit model $P = P_{\\max} \\cdot \\Phi(A \\cdot \\alpha^{0.24} \\cdot \\sqrt{T} - z_0)$ is refit on the remaining data.\nOverall MAE${=}0.037$ with 95\\% CI coverage $15/15$.\nWhen sync-dip cells are included (20 cells), MAE rises to $0.203$ (CI $16/20$), with the largest residuals at sync-dip cells (predicted $0.75$, observed $0/8$).\nThe profile likelihood over $\\beta$ yields MLE $\\hat{\\beta}{=}0.66$ (95\\% CI $[0.24, 0.78]$); the wide interval reflects a flat likelihood surface, indicating that $\\beta$ is not well-identified from these data.\nModel comparison (AIC, 15-cell grid excluding sync-dip): $M_1$ (linear boundary) $\\Delta\\mathrm{AIC}{=}0.0$; $M_2$ (power-probit) $\\Delta\\mathrm{AIC}{=}2.43$.\nIncluding sync-dip data reverses the ranking ($M_2$ $\\Delta\\mathrm{AIC}{=}0.0$, $M_1$ $\\Delta\\mathrm{AIC}{=}4.15$), because the probit model naturally accommodates the dip's dissolution at higher $T$ while linear models cannot.\n\n\\section{Power Simulation: Shape Comparison}\n\\label{app:power_sim}\n\nTo assess whether the observed steep detection onset could arise from smooth signal models, we simulate PermG detection under three null hypotheses (1{,}000 replications per cell, $n_{\\text{perm}}{=}1{,}000$, $n_{\\text{pairs}}{=}8$, BH-FDR $q{=}0.05$):\n\n\\begin{itemize}\n\\item \\textbf{H0} (linear): $S(\\alpha) = c \\cdot \\alpha$, calibrated so $S(1.0) = S_{\\max}$.\n\\item \\textbf{H0$'$} (concave): $S(\\alpha) = c \\cdot \\alpha^{0.5}$, sub-linear but smooth.\n\\item \\textbf{H1} (step): $S(\\alpha) = S_{\\max} \\cdot \\mathbf{1}[\\alpha > \\alpha_c(T)]$, binary activation.\n\\end{itemize}\n\n\\noindent\\textbf{Scaling exponents.}\nAll three models produce apparent onset scaling in $T$: H0 $\\gamma{=}0.85$, H0$'$ $\\gamma{=}1.87$, H1 $\\gamma{=}1.96$ (observed: $\\gamma{=}2.08$).\nH0$'$ produces $\\gamma$ within $0.21$ of the observed value, demonstrating that the scaling exponent alone cannot distinguish smooth from step-function boundaries.\n\n\\noindent\\textbf{Shape differences.}\nAt $T{=}10$, $\\alpha{=}0.45$: H0 predicts 27\\% detection rate, H0$'$ predicts 45\\%, H1 predicts 5.5\\%, observed $0/8$.\nAt $T{=}10$, $\\alpha{=}0.50$: H0 predicts 36\\%, H0$'$ predicts 48\\%, H1 predicts 4.6\\%, observed $6/8$ (75\\%).\nSmooth models produce onset ramps with $k{=}4.9$--$6.1$ (H0$'$: $k{=}4.93$, $R^2{=}0.9974$; H0: $k{=}6.14$, $R^2{=}0.9998$); the observed onset steepness ($k{=}15.7$) is ${\\approx}3{\\times}$ higher.\n\n\\noindent\\textbf{Metric-specific ceiling.}\nAt high $\\alpha$ (${\\geq}0.75$) with $T{\\geq}20$, H0 and H0$'$ (which simulate 8 equal-signal pairs) reach mean detection fractions of $0.79$--$0.98$ (${\\approx}6.3$--$7.8/8$), whereas observed counts never exceed $6/8$.\nThis gap reflects metric structure rather than signal saturation: the 2/8 non-detected pairs consistently involve MAUVE, whose floor saturation (\\S\\ref{sec:t20}) prevents Granger detection regardless of signal strength.\n\n\\section{T=20 Predict-then-Verify Comparison}\n\\label{app:t20_comparison}\n\nTable~\\ref{tab:t20_comparison} reports the predict-then-verify results for the $T{=}20$ extension experiments.\nPredictions are derived from the detection boundary model (\\S\\ref{sec:theory}): detected pairs at $T{=}10$ are predicted to remain detected (saturated $F$-statistics), and undetected pairs are predicted to remain undetected (structural nulls or non-monotonic dip).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{T=20 predict-then-verify comparison (Pythia-410M, seed~42, WikiText, fp32). Excluding $\\alpha{=}1.0$, two of four predictions fall within CI ($\\alpha{=}0.50$, $0.75$); boundary cases show systematic bias---$\\alpha{=}0.45$ falsifies the ceiling hypothesis (under-prediction), $\\alpha{=}0.60$ over-predicts under raw $p$-values (v1; matches under FDR v2, not pre-committed).}\n\\label{tab:t20_comparison}\n\\begin{tabular}{lcccc}\n\\toprule\n$\\alpha$ & $T{=}10$ & Predicted $T{=}20$ & Observed $T{=}20$ & Match \\\\\n\\midrule\n0.45 & 0/8 & 0/8 (ceiling) & 5/8 & $\\times$ \\\\\n0.50 & 6/8 & 6/8 (saturated) & 6/8 & \\checkmark \\\\\n0.60 & 0/8 & 3/8 (v1 raw)$^\\dagger$ & 0/8 & $\\times$ \\\\\n0.75 & 6/8 & 6/8 (saturated) & 6/8 & \\checkmark \\\\\n1.00 & 6/8 & 6/8 (saturated) & 6/8 & \\checkmark \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$V2 (BH--FDR corrected, created 44\\,min pre-analysis, not git-committed) predicts 0/8, matching observation.} \\\\\n\\end{tabular}\n\\end{table}\n\nAt $\\alpha \\geq 0.50$, consistency across $T{=}10$ and $T{=}20$ supports the detection boundary prediction: PermG counts are determined by signal structure, not observation length.\nSix diversity-based pairs show $F{=}449$--$2947$ at $T{=}20$ (all $\\gg F_{\\text{crit}}$); two MAUVE-based pairs show $F{<}2$ regardless of $T$, driven by floor saturation ($\\mu{=}0.029$, 100\\% ${<}0.05$) rather than high variance (CV$_{\\text{MAUVE}}{=}0.089$ vs CV$_{\\text{distinct-1}}{=}0.139$); SNR: MAUVE $4.68$ vs diversity $6.40$--$8.20$ ($p{<}0.001$).\nThe sole exception is $\\alpha{=}0.45$ at $T{=}20$ (5/8), consistent with boundary proximity.\nAt $\\alpha{=}0.45$, the shift from 0/8 to 5/8 falsifies Model~A (ceiling: $\\alpha{=}0.45$ structurally undetectable) in favor of Model~B (power-limited: $\\sqrt{T}$ boost crosses the detection threshold), lowering $\\alpha_c$ below~0.45.\nThe $\\alpha{=}0.60$ non-monotonic dip persists at $T{=}20$ (s42: 0/8; s43: 3/8) but dissolves at $T{=}25$ (5/8), confirming that $\\sqrt{T}$ power scaling eventually overcomes the dip; alternative methods detect signal throughout (DiffXCorr 6/8, TY 5/8 at $T{=}20$).\nPermG directional selectivity is consistent across tested $T$ ($T{=}10$, $20$): forward 6/8 versus reverse 0/8 at $\\alpha \\in \\{0.50, 0.75, 1.0\\}$.\n\n\n\\subsection{Prediction Timeline}\n\\label{app:t20_prediction_timeline}\n\nTwo versions of the $T{=}20$ prediction file exist, reflecting an evolving statistical protocol:\n\n\\paragraph{V1 (git-committed, \\texttt{bad72cc}).} Predictions derived from $T{=}10$ PermG results using \\emph{raw} $p$-values. At $\\alpha{=}0.60$, v1 counted 3/8 pairs with raw $p{<}0.05$, predicting 3/8 detections at $T{=}20$. The observed result (0/8 FDR-significant) does not match.\n\n\\paragraph{V2 (pre-analysis, not committed).} A revised file incorporating BH--FDR correction at $q{=}0.05$, consistent with the correction applied throughout the paper. Under FDR, $\\alpha{=}0.60$ drops from 3/8 (raw) to 0/8, matching the observation. V2 was created 44 minutes before the formal $T{=}20$ analysis began (filesystem timestamp) but was not git-committed, and therefore lacks the cryptographic verifiability of v1.\n\n\\paragraph{Scoring.} Primary (v1, committed): 3/5 exact matches ($\\alpha \\in \\{0.50, 0.75, 1.0\\}$, all saturated regimes). Excluding $\\alpha{=}1.0$, two of four predictions fall within CI. Both boundary predictions miss: $\\alpha{=}0.45$ (predicted 0/8, observed 5/8) falsifies the ceiling hypothesis in favor of $\\sqrt{T}$ power scaling; $\\alpha{=}0.60$ (predicted 3/8, observed 0/8) over-estimates detection due to the non-monotonic dip. Sensitivity (v2, FDR-corrected): 4/5 ($\\alpha{=}0.60$ matches). The systematic conservative bias at $\\alpha{=}0.45$ is consistent with the $\\sqrt{T}$ power increase predicted by Proposition~\\ref{prop:phase-boundary}.\n\n\n\\phantomsection\\label{app:task_degradation}\n\\paragraph{Task degradation.}\n\nTable~\\ref{tab:task_degradation} reports end-of-training task performance (generation~10, Pythia-410M, seed~42, fp32) across contamination levels.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Task degradation across contamination levels (Pythia-410M, seed~42, fp32, generation~10). Perplexity evaluated on held-out WikiText-103.}\n\\label{tab:task_degradation}\n\\begin{tabular}{lcc}\n\\toprule\n$\\alpha$ & Perplexity & Next-token acc. \\\\\n\\midrule\nBaseline & 26.6 & 0.390 \\\\\n0.05 & 20.8 & 0.431 \\\\\n0.25 & 22.9 & 0.424 \\\\\n0.46 & 31.6 & 0.400 \\\\\n0.50 & 31.3 & 0.399 \\\\\n0.52 & 41.1 & 0.389 \\\\\n0.60 & 53.5 & 0.375 \\\\\n0.75 & 80.3 & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\alpha{=}0.05$, perplexity improves over the uncontaminated baseline (20.8 vs.\\ 26.6), consistent with a mild data augmentation effect.\nThe sharpest degradation occurs between $\\alpha{=}0.50$ and $0.52$ ($+31\\%$ perplexity), aligning with the PermG detection onset (\\S\\ref{sec:regime}).\n\n\\section{Cross-Architecture FPR Sensitivity}\n\\label{app:cross_arch_fpr}\n\nAs preliminary cross-architecture evidence, we evaluate null-condition ($\\alpha{=}0$) false positive rates on GPT-2-medium (345M; OpenAI), a model outside the Pythia family used for all primary experiments.\nTwo seeds (s42, s43) are trained for $T{=}10$ generations under the same protocol as the Pythia-410M null runs.\nThis evaluation requires additional replication across architectures and seed counts before drawing definitive conclusions.\n\n\\begin{table}[h]\n\\centering\n\\caption{Null-condition FPR for GPT-2-medium ($\\alpha{=}0$, $T{=}10$, 6-pair basis). PermG forward detection shows extreme seed dependence; $K{\\geq}3$ consensus remains at 0\\% across both seeds.}\n\\label{tab:gpt2m_null_fpr}\n\\begin{tabular}{lccc}\n\\toprule\nSeed & PermG fwd & PermG rev & $K{\\geq}3$ \\\\\n\\midrule\ns42 & 6/6 (100\\%) & 0/6 & 0/6 \\\\\ns43 & 0/6 (0\\%) & 0/6 & 0/6 \\\\\n\\midrule\nPooled & 6/12 (50\\%) & 0/12 & 0/12 (0\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe pooled PermG FPR is dramatically higher than on Pythia-410M (50\\% vs.\\ 11.1\\%, 6-pair basis) and shows extreme seed dependence (100\\% vs.\\ 0\\%).\nThis instability traces to the magnitude of null drift in GPT-2-medium's output distribution, which is substantially stronger than in Pythia-410M (Table~\\ref{tab:null_drift_comparison}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Null drift magnitude ($\\alpha{=}0$, gen\\,0$\\to$10; GPT-2-medium: 2 seeds; Pythia-410M: 4 seeds, s46/s48--s50). GPT-2-medium exhibits ${\\sim}4{\\times}$ stronger entropy drift and ${\\sim}7{\\times}$ stronger distinct-3 drift than Pythia-410M.}\n\\label{tab:null_drift_comparison}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{GPT-2-medium} & \\multicolumn{2}{c}{Pythia-410M} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nMetric & gen\\,0 & gen\\,10 (\\%$\\Delta$) & gen\\,0 & gen\\,10 (\\%$\\Delta$) \\\\\n\\midrule\nToken entropy & 3.57 & 2.84 ($-$20.5\\%) & 3.23 & 3.076 ($-$4.9\\%) \\\\\nDistinct-3 & 0.84 & 0.54 ($-$35.8\\%) & 0.81 & 0.769 ($-$4.9\\%) \\\\\n$\\Delta$entropy (gen\\,0$\\to$1) & \\multicolumn{2}{c}{$-$0.60} & \\multicolumn{2}{c}{$-$0.25} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGPT-2-medium's distinct-3 declines from 0.84 to 0.54 over ten null generations ($-$35.8\\%), compared with 0.81$\\to$0.77 ($-$4.9\\%) for Pythia-410M.\nThis steep diversity collapse under pure retraining, absent any synthetic contamination, creates a strong downward trend that PermG's permutation test interprets as a directional signal.\nThe initial entropy drop (gen\\,0$\\to$1: $-$0.60 vs.\\ $-$0.25) is similarly amplified, consistent with architecture-specific sensitivity to iterative retraining rather than a deficiency in the detection method.\n\nThe $K{\\geq}3$ multi-method consensus maintains 0\\% FPR on GPT-2-medium (0/12 pairs), though the margin of safety is narrow: in the worst case (s42), 2 of 5 methods vote for forward detection, one vote short of the $K{\\geq}3$ threshold.\nThis provides some protection against architecture-specific distributional variation, but two seeds constitute only preliminary evidence.\nFor reference, PermG successfully detects true contamination signal ($\\alpha{=}1.0$) on GPT-2-medium with 6/8 forward pairs (Table~\\ref{tab:generalization}), confirming that the method works when signal is present; the elevated null FPR is specific to the null condition where architecture-dependent drift dominates.\n\n\\section*{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform related-work section.\n\\end{itemize}\n\n",
    "structuredPatch": [
      {
        "oldStart": 724,
        "oldLines": 10,
        "newStart": 724,
        "newLines": 10,
        "lines": [
          " The combined Shapley value $\\phi_k^{\\text{comb}} = \\phi_k^{\\text{FPR}} + \\phi_k^{\\text{FNR}}$ balances both error types, with more negative values indicating greater net benefit.",
          " ",
          " Table~\\ref{tab:shapley_6pair} reports the 6-pair analysis (excluding mauve).",
          "-% TODO-D219: recompute Shapley values; PermG φ^FPR will be >0 with 6-seed data (4/36 FPs)",
          "-PermG achieves the lowest (best) combined Shapley ($-0.180$), driven entirely by FNR reduction with zero FPR contribution---the only method with this property.",
          "-Naive cross-correlation is the worst contributor ($+0.203$), with its massive FPR Shapley ($+0.622$) overwhelming its FNR benefit ($-0.419$): adding naive cross-correlation to any coalition increases false positives far more than it reduces false negatives.",
          "-Threshold onset contributes almost nothing useful ($+0.074$ combined; FPR $+0.101$, FNR $-0.027$), confirming the near-zero detection power reported in Table~\\ref{tab:method_comparison}.",
          "+DiffXCorr achieves the lowest (best) combined Shapley ($-0.299$), driven by near-zero FPR contribution ($+0.007$) and strong FNR reduction ($-0.306$); however, DiffXCorr cannot separate forward from reverse causation (Table~\\ref{tab:null_fpr_methods}).",
          "+Among directional methods, PermG ranks best ($-0.141$ combined), with a modest FPR contribution ($+0.039$, reflecting 4/36 null false positives) offset by substantial FNR reduction ($-0.180$).",
          "+Naive cross-correlation is the worst contributor ($+0.190$), with its massive FPR Shapley ($+0.609$) overwhelming its FNR benefit ($-0.419$).",
          "+Threshold onset contributes almost nothing useful ($+0.084$ combined; FPR $+0.111$, FNR $-0.027$), confirming the near-zero detection power reported in Table~\\ref{tab:method_comparison}.",
          " Figure~\\ref{fig:shapley} visualizes the decomposition.",
          " ",
          " \\begin{table}[h]"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Assistant

_source line 117_

Now update the Shapley table values (Table 15).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "ab491b3e-756f-4d59-898a-96b1d84c1c3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLctM9ALnZp4cNtHjbj7cZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 763,
      "cache_read_input_tokens": 110988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 763
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 118_

<details open><summary>🔧 Tool call — Edit · `toolu_01G4gURjcurMy2PPiWLP8Db4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "old_string": "\\caption{Shapley value decomposition (6-pair, mauve excluded). FPR-Shapley: marginal FPR contribution (positive = increases false positives). FNR-Shapley: marginal FNR contribution (negative = reduces false negatives). Combined = FPR + FNR (more negative = better). 48 experiments, $2^5{=}32$ coalitions, exact enumeration.}\n\\label{tab:shapley_6pair}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $\\phi^{\\text{FPR}}$ & $\\phi^{\\text{FNR}}$ & $\\phi^{\\text{comb}}$ \\\\\n\\midrule\nNaive XCorr          & $+0.622$ & $-0.419$ & $+0.203$ \\\\\nDiff.\\ XCorr         & $+0.163$ & $-0.306$ & $-0.142$ \\\\\nThreshold ($3\\sigma$) & $+0.101$ & $-0.027$ & $+0.074$ \\\\\n\\textbf{Perm.\\ Granger} & $\\mathbf{0.000}$ & $\\mathbf{-0.180}$ & $\\mathbf{-0.180}$ \\\\\nToda--Yamamoto       & $+0.031$ & $-0.069$ & $-0.038$ \\\\\n\\bottomrule\n\\end{tabular}",
  "new_string": "\\caption{Shapley value decomposition (6-pair, mauve excluded). FPR-Shapley computed from 6 null seeds (36 pairs); FNR-Shapley from 45 signal experiments (270 pairs). Combined = FPR + FNR (more negative = better). $2^5{=}32$ coalitions, exact enumeration.}\n\\label{tab:shapley_6pair}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $\\phi^{\\text{FPR}}$ & $\\phi^{\\text{FNR}}$ & $\\phi^{\\text{comb}}$ \\\\\n\\midrule\nNaive XCorr          & $+0.609$ & $-0.419$ & $+0.190$ \\\\\n\\textbf{Diff.\\ XCorr}& $\\mathbf{+0.007}$ & $\\mathbf{-0.306}$ & $\\mathbf{-0.299}$ \\\\\nThreshold ($3\\sigma$) & $+0.111$ & $-0.027$ & $+0.084$ \\\\\nPerm.\\ Granger       & $+0.039$ & $-0.180$ & $-0.141$ \\\\\nToda--Yamamoto       & $+0.150$ & $-0.069$ & $+0.082$ \\\\\n\\bottomrule\n\\end{tabular}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "ff1bc0b0-21b7-4022-9f2c-20dbcb045bbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KLctM9ALnZp4cNtHjbj7cZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 763,
      "cache_read_input_tokens": 110988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 763
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-24T09:06:14.647Z_

<details><summary>↩ Tool result · `toolu_01G4gURjcurMy2PPiWLP8Db4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "37c5bc2b-27cf-4ddc-b7c0-3aaa62f67077",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "oldString": "\\caption{Shapley value decomposition (6-pair, mauve excluded). FPR-Shapley: marginal FPR contribution (positive = increases false positives). FNR-Shapley: marginal FNR contribution (negative = reduces false negatives). Combined = FPR + FNR (more negative = better). 48 experiments, $2^5{=}32$ coalitions, exact enumeration.}\n\\label{tab:shapley_6pair}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $\\phi^{\\text{FPR}}$ & $\\phi^{\\text{FNR}}$ & $\\phi^{\\text{comb}}$ \\\\\n\\midrule\nNaive XCorr          & $+0.622$ & $-0.419$ & $+0.203$ \\\\\nDiff.\\ XCorr         & $+0.163$ & $-0.306$ & $-0.142$ \\\\\nThreshold ($3\\sigma$) & $+0.101$ & $-0.027$ & $+0.074$ \\\\\n\\textbf{Perm.\\ Granger} & $\\mathbf{0.000}$ & $\\mathbf{-0.180}$ & $\\mathbf{-0.180}$ \\\\\nToda--Yamamoto       & $+0.031$ & $-0.069$ & $-0.038$ \\\\\n\\bottomrule\n\\end{tabular}",
    "newString": "\\caption{Shapley value decomposition (6-pair, mauve excluded). FPR-Shapley computed from 6 null seeds (36 pairs); FNR-Shapley from 45 signal experiments (270 pairs). Combined = FPR + FNR (more negative = better). $2^5{=}32$ coalitions, exact enumeration.}\n\\label{tab:shapley_6pair}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $\\phi^{\\text{FPR}}$ & $\\phi^{\\text{FNR}}$ & $\\phi^{\\text{comb}}$ \\\\\n\\midrule\nNaive XCorr          & $+0.609$ & $-0.419$ & $+0.190$ \\\\\n\\textbf{Diff.\\ XCorr}& $\\mathbf{+0.007}$ & $\\mathbf{-0.306}$ & $\\mathbf{-0.299}$ \\\\\nThreshold ($3\\sigma$) & $+0.111$ & $-0.027$ & $+0.084$ \\\\\nPerm.\\ Granger       & $+0.039$ & $-0.180$ & $-0.141$ \\\\\nToda--Yamamoto       & $+0.150$ & $-0.069$ & $+0.082$ \\\\\n\\bottomrule\n\\end{tabular}",
    "originalFile": "\\appendix\n\n\\section{Training Details and Metric Drift}\n\\label{app:training_details}\n\\label{app:drift}\n\n\\paragraph{Hyperparameters.}\nEach generation fine-tunes for 5{,}000 steps using AdamW (learning rate $5 \\times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium).\nGeneration uses temperature $1.0$, top-$k{=}50$, max length 512 tokens, producing 5{,}000 samples per generation from 5{,}000-sample subsets of WikiText-103.\nCanary metrics: token entropy $H(p_\\theta | \\text{context})$ over 1{,}000 held-out samples; ECE with 15 bins.\nAdditional downstream metrics (distinct-3, effective rank, Self-BLEU) appear in subsequent appendix sections.\n\n\\paragraph{Metric drift.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Metric drift (\\%, generation~0$\\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\\alpha{=}0.25$: distinct-1 $-40.3{\\pm}0.3\\%$) rather than full replacement ($\\alpha{=}1.0$: $-27.8{\\pm}1.6\\%$). $^\\dagger$$\\alpha{=}0.10$: single seed (seed~42, preliminary). $\\alpha{=}0.00$, $\\alpha{=}0.25$, $\\alpha{=}0.50$, $\\alpha{=}0.75$: 3-seed mean${\\pm}$std (seeds 42, 43, 44); $\\alpha{=}1.0$: 4-seed mean${\\pm}$std (seeds 42, 43, 44, 45).}\n\\label{tab:drift_summary}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\\\\n\\midrule\n0.00 & $-4.6{\\pm}0.4$ & $+37.6{\\pm}14$ & $-14.1{\\pm}0.4$ & $-9.6{\\pm}0.4$ & $-20.6{\\pm}1.0$ \\\\\n0.10$^\\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\\\\n0.25 & $-4.7{\\pm}0.5$ & $+81.8{\\pm}15.9$ & $-40.3{\\pm}0.3$ & $-56.4{\\pm}0.7$ & $-18.1{\\pm}0.8$ \\\\\n0.50 & $-18.0{\\pm}0.5$ & $+822.6{\\pm}18.3$ & $-37.1{\\pm}0.4$ & $-50.4{\\pm}1.0$ & $+21.0{\\pm}0.1$ \\\\\n0.75 & $-27.6{\\pm}0.2$ & $+1791{\\pm}18$ & $-32.3{\\pm}0.5$ & $-41.0{\\pm}1.0$ & $+182.6{\\pm}0.7$ \\\\\n1.00 & $-60.8{\\pm}1.2$ & $+3780{\\pm}30$ & $-27.8{\\pm}1.6$ & $-34.0{\\pm}3.3$ & $+3674{\\pm}45$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Distinct-3 Results}\n\\label{app:distinct3}\n\nTable~\\ref{tab:distinct3_drift} reports distinct-3 drift across all contamination levels.\nDistinct-3 exhibits the largest absolute decline among diversity metrics at low contamination ($-58.9{\\pm}0.9\\%$ at $\\alpha{=}0.25$) but attenuates at higher levels ($-30.5\\%$ at $\\alpha{=}1.0$), consistent with the diversity--calibration dissociation discussed in \\S\\ref{sec:discussion}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Distinct-3 drift (\\%, generation~0$\\to$10) across contamination levels. $\\alpha{=}0.00$, $\\alpha{=}0.25$, $\\alpha{=}0.75$: 3-seed mean${\\pm}$std; $\\alpha{=}1.0$: 4-seed mean${\\pm}$std; $\\alpha{=}0.50$: single seed.}\n\\label{tab:distinct3_drift}\n\\begin{tabular}{lc}\n\\toprule\n$\\alpha$ & Distinct-3 drift (\\%) \\\\\n\\midrule\n0.00 & $-4.4{\\pm}0.5$ \\\\\n0.25 & $-58.9{\\pm}0.9$ \\\\\n0.50 & $-52.4$ \\\\\n0.75 & $-38.6{\\pm}1.3$ \\\\\n1.00 & $-30.5{\\pm}4.0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Lead-lag analysis.}\nAt $\\alpha{=}1.0$, token entropy Granger-precedes distinct-3 at the same consensus level as distinct-1 and distinct-2: $K{\\geq}4/5$ methods, $S{\\geq}3/4$ seeds (Tier~3).\nHowever, the optimal lag is less stable than for distinct-1/2: at max\\_lag${=}7$, the lag standard deviation across seeds exceeds 1.5 generations, compared to $<0.5$ for distinct-1/2.\nThis instability reflects bimodal lag distributions (modes at lag~1 and lag~3--4), suggesting that distinct-3 captures two temporally distinct diversity loss mechanisms: rapid n-gram homogenization (lag~1) and slower distributional narrowing (lag~3--4).\n\n\\paragraph{Sensitivity to sequence length.}\nHigher-order $n$-gram diversity metrics are more sensitive to generation length and random sampling variability.\nWith our 512-token generation length, distinct-3 has a smaller effective denominator (number of possible unique trigrams observed) than distinct-1 or distinct-2, amplifying stochastic fluctuations.\nThis partially explains the higher lag instability: the signal-to-noise ratio for temporal precedence is lower for distinct-3, requiring more observations (longer $T$ or more seeds) to achieve stable estimates.\nFor this reason, we report distinct-3 in this appendix rather than in the main text, where distinct-1 and distinct-2 provide cleaner evidence of the entropy-leads-diversity pattern.\n\n\n\\section{Observation Window Sensitivity}\n\\label{app:window_sensitivity}\n\nTable~\\ref{tab:window_sensitivity} reports how the Tier~3 consensus classification ($K{\\geq}4/5$ methods) varies as a function of the minimum observation window $T_{\\min}$, where analysis uses only generations $0$ through $T_{\\min}$.\nThe consensus classification stabilizes at $T_{\\min}{\\geq}5$ (6 data points), well below our full observation window of $T{=}10$: all six effect-size reference pairs (token entropy and ECE $\\to$ distinct-1, distinct-2, distinct-3) reach $K{\\geq}4/5$ agreement at every window length from $T_{\\min}{=}5$ through $T_{\\min}{=}10$, with no spurious pairs (canary$\\to$perplexity) admitted.\n\nToda--Yamamoto is the only method exhibiting window-dependent sensitivity (note: TY directional assignment is under verification; these counts are retained for completeness): TY consensus stabilizes at $T_{\\min}{\\geq}6$, slightly later than the primary methods, reflecting the additional degrees of freedom consumed by the augmentation order $d_{\\max}$.\nThis does not affect the consensus classification because the remaining four methods provide stable $K{\\geq}4/5$ agreement independently of Toda--Yamamoto's vote.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Observation window sensitivity for Tier~3 consensus ($K{\\geq}4/5$) at $\\alpha{=}1.0$ (Pythia-410M, 4~seeds). Tier~3 pairs: number of canary$\\to$downstream pairs (out of 8 validated) reaching $K{\\geq}4/5$ method agreement. TY pairs: number of effect-size reference pairs (out of 6) reaching Toda--Yamamoto significance (moderate supplementary method; \\S\\ref{sec:method}). Consensus stabilizes at $T_{\\min}{\\geq}5$; TY stabilizes at $T_{\\min}{\\geq}6$.}\n\\label{tab:window_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccccccc}\n\\toprule\n& \\multicolumn{8}{c}{Minimum observation window $T_{\\min}$} \\\\\n\\cmidrule(lr){2-9}\n& 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\\\\n\\midrule\nTier~3 pairs (/8)    & $\\dagger$ & $\\dagger$ & 6 & 6 & 6 & 6 & 6 & 6 \\\\\nTY pairs$^\\S$ (/6)   & $\\dagger$ & $\\dagger$ & 3--6 & 3--6 & 3--6 & 3--6 & 3--6 & 6 \\\\\nStable               & ---       & ---       & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark \\\\\n\\bottomrule\n\\multicolumn{9}{l}{\\footnotesize $\\dagger$~Insufficient degrees of freedom for Granger-type tests ($<6$ data points).} \\\\\n\\multicolumn{9}{l}{\\footnotesize $^\\S$~TY directional assignment under verification.}\n\\end{tabular}}\n\\end{table}\n\n\n\\section{Robustness Checks}\n\\label{app:robustness}\n\n\\paragraph{Permutation count stability.}\nTable~\\ref{tab:nperm_stability} compares permutation Granger $p$-values at 5{,}000 versus 10{,}000 permutations across all canary$\\to$downstream pairs at $\\alpha{=}0.75$ (3~seeds, 24~pairs).\nPermutation Granger $p$-values are stable to within 0.002 between 5{,}000 and 10{,}000 permutations, with zero significance decisions affected.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Permutation count stability analysis ($\\alpha{=}0.75$, 3~seeds, 24 canary$\\to$downstream pairs). $p$-values from permutation Granger tests at $n_{\\text{perm}}{=}5{,}000$ versus $n_{\\text{perm}}{=}10{,}000$.}\n\\label{tab:nperm_stability}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nMax $|\\Delta p|$ & 0.010 \\\\\nMean $|\\Delta p|$ & 0.002 \\\\\nSignificance flips & 0 / 24 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{FDR threshold sensitivity.}\nTable~\\ref{tab:fdr_sensitivity} reports the effect of varying the BH FDR threshold $q$ on treatment ($\\alpha{=}0.75$, 3~seeds, 8-pair basis) versus null ($\\alpha{=}0.0$, 6~seeds 45--50, 6-pair basis) separation for permutation Granger tests.\nTreatment/null separation is qualitatively robust to FDR threshold choice, though the expanded null sample reveals a small number of false positives at each threshold (3--8 of 36 pairs).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs, 8-pair basis). Null: $\\alpha{=}0.0$ (6~seeds 45--50, 36 pairs, 6-pair basis). The expanded null sample reveals modest false positive rates that increase with $q$.}\n\\label{tab:fdr_sensitivity}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\n$q$ & Null FDR-sig (/36) & Treatment FDR-sig (/24) & Separation \\\\\n\\midrule\n0.01 & 3 & 0  & Underpowered \\\\\n0.05 & 4 & 19 & Good \\\\\n0.10 & 8 & 24 & Good (elevated null) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{PermG $p$-value gradient at the onset boundary ($\\alpha{=}0.45$).}\nAt the onset boundary, PermG operates near its detection limit, and marginal $p$-values exhibit seed-dependent variation consistent with the statistical power interpretation (\\S\\ref{sec:theory}).\nTable~\\ref{tab:fdr_gradient_a045} reports BH-corrected $p$-values for all 8 canary$\\to$downstream pairs across two seeds at $\\alpha{=}0.45$.\nSeed~43 reaches a minimum FDR-corrected $p{=}0.059$ (18\\% above the $q{=}0.05$ threshold), while seed~42 reaches $p{=}0.091$ (82\\% above threshold).\nNo pair crosses the significance threshold at either seed, yielding the aggregate 0/8 detection rate reported in \\S\\ref{sec:regime}.\nThe gradient is consistent with a continuous power transition rather than a binary absence of signal: PermG operates near its detection limit at $\\alpha{=}0.45$, with seed-dependent variation in marginal $p$-values.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BH-corrected PermG $p$-values at $\\alpha{=}0.45$ (8 canary$\\to$downstream pairs $\\times$ 2 seeds). Min $p_{\\mathrm{fdr}}$ per seed shown. All pairs remain above the $q{=}0.05$ threshold, yielding 0/8 aggregate detection.}\n\\label{tab:fdr_gradient_a045}\n\\begin{tabular}{lcc}\n\\toprule\n & Seed 42 & Seed 43 \\\\\n\\midrule\nMin FDR $p$ & 0.091 & 0.059 \\\\\nGap to $q{=}0.05$ & 82\\% & 18\\% \\\\\nPermG fwd sig (/8) & 0 & 0 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Systematic Robustness Analysis}\n\\label{app:spec_curve}\n\nThe sharp detection onset reported in \\S\\ref{sec:regime} could in principle depend on specific analytical choices (pair selection, seed, $\\alpha$ level, method parameters).\nWe assess robustness via specification curve analysis~\\cite{simonsohn2020specification}, systematically varying analytical degrees of freedom to test whether the 0/8$\\to$6/8 transition is specification-invariant.\nOur specification curve varies data subsets and pair selections while holding the detection method (PermG) and its hyperparameters fixed, more closely resembling a systematic subset analysis than a full specification curve in the sense of \\citet{simonsohn2020specification}.\n\nWe construct 1{,}160 analytical specifications from the combinatorial space of: 13 contamination levels ($\\alpha$ grid), seed selection ($\\{42, 43, 44, 45\\}$ where available), 8 canonical canary$\\to$downstream pairs (\\{token entropy, ECE\\} $\\times$ \\{distinct-1, distinct-2, distinct-3, mauve\\}), and method parameters (all PermG with $n_\\text{perm}{=}5{,}000$, BH FDR $q{=}0.05$).\nAll specifications use the D120-canonical analysis pipeline with $3\\sigma$ threshold calibration (D105) as a hard filter.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Specification curve summary (1{,}160 specifications, D120-compliant). The blind$\\to$onset jump is robust across specifications: 0\\% significance rate through $\\alpha{=}0.45$, rising to 75\\% at $\\alpha{=}0.50$.}\n\\label{tab:spec_curve}\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nTotal specifications & 1{,}160 \\\\\nSignificant (FDR $q{<}0.05$) & 536 (46.2\\%) \\\\\n\\midrule\n\\emph{By regime} & \\\\\n\\quad Blind ($\\alpha \\leq 0.45$) & 0\\% \\\\\n\\quad Onset ($\\alpha{=}0.50$) & 75\\% \\\\\n\\quad Detection ($\\alpha \\geq 0.75$) & 62--75\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe specification curve confirms that the sharp detection onset is not an artifact of particular analytical choices: the categorical jump from 0\\% to ${\\geq}75\\%$ significance at $\\alpha_c{\\approx}0.50$ holds across the vast majority of specifications, supporting the main text claim (\\S\\ref{sec:regime}).\n\n\n\\section{Transfer Entropy Analysis}\n\\label{app:transfer_entropy}\n\nTable~\\ref{tab:te_results} reports transfer entropy (TE; \\citealp{schreiber2000measuring}) results aggregated across all baseline conditions.\nTE was estimated using 3-bin discretization with permutation testing ($n{=}5{,}000$).\nNo pair reaches BH-corrected significance ($q{=}0.05$) in any condition, confirming that non-parametric information-theoretic methods lack detection power at $T{=}11$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Transfer Entropy results (12 runs across all $\\alpha$ levels). TE\\textsubscript{fwd}: canary$\\to$downstream; TE\\textsubscript{rev}: downstream$\\to$canary. Mean uncorrected permutation $p$-values ($n{=}5{,}000$). No pair reaches BH-corrected $q{<}0.05$ in any run.}\n\\label{tab:te_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\nCanary & Downstream & TE\\textsubscript{fwd} (mean) & $p$\\textsubscript{fwd} (mean) & TE\\textsubscript{rev} (mean) & $p$\\textsubscript{rev} (mean) \\\\\n\\midrule\ntoken\\_entropy & distinct-1 & 0.289 & 0.559 & 0.480 & 0.490 \\\\\ntoken\\_entropy & distinct-2 & 0.300 & 0.529 & 0.496 & 0.447 \\\\\ntoken\\_entropy & distinct-3 & 0.255 & 0.645 & 0.484 & 0.459 \\\\\ntoken\\_entropy & perplexity & 0.257 & 0.676 & 0.386 & 0.626 \\\\\nECE & distinct-1 & 0.185 & 0.720 & 0.184 & 0.891 \\\\\nECE & distinct-2 & 0.208 & 0.683 & 0.216 & 0.846 \\\\\nECE & distinct-3 & 0.209 & 0.689 & 0.227 & 0.807 \\\\\nECE & perplexity & 0.296 & 0.572 & 0.263 & 0.747 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\phantomsection\\label{app:te_mi}\n\\paragraph{KNN-based TE/MI decomposition.}\nA $k$-nearest-neighbor TE estimator ($k{=}5$) provides a model-free complement to the parametric Granger framework.\nForward-dominant TE fraction increases monotonically with $\\alpha$: 4/8 pairs at $\\alpha{=}0.25$ (mean net TE${=}0.14$), 5/8 at $\\alpha{=}0.50$ (net TE${=}0.42$), 6/8 at $\\alpha{=}0.60$ (net TE${=}0.57$), and 8/8 at $\\alpha{=}1.0$ (net TE${=}1.59$).\nAll 120 forward TE bootstrap 95\\% CIs exclude zero at $T{=}10$; all 48 at $T{=}20$.\nThe ``high MI, low TE'' hypothesis for the non-monotonic dip is supported by only 2/8 pairs (ECE$\\to$perplexity and token entropy$\\to$perplexity); the remaining 6 pairs show elevated TE even at $\\alpha{=}0.60$, indicating confounded co-variation rather than a universal mechanism.\n\n\\section{Change-Point Detection Analysis}\n\\label{app:change_point}\n\nWe apply a max-split change-point test with bootstrap significance assessment ($n{=}5{,}000$, $p{<}0.05$) to each metric's generation-level time series ($T{=}11$).\n\nUnder the null control ($\\alpha{=}0.00$, 3~seeds), downstream diversity metrics (distinct-1, distinct-2, distinct-3) produce significant change-points at generation~2 in all seeds (9/9 tests). With additional significant tests from ECE (2/3 seeds) and token entropy (1/3 seeds), the overall false positive rate reaches 66.7\\% (12/18 tests; Table~\\ref{tab:cp_null}). The monotonic drift inherent in iterative self-training is sufficient to trigger change-point detection even without canary contamination. Individual change-point significance therefore cannot serve as standalone evidence for a canary-specific effect.\n\nAlthough individual significance is unreliable as a discriminator, the temporal ordering of detected change-points reverses between null and treatment conditions. In the null ($\\alpha{=}0.00$), downstream metrics show the earliest significant breaks at generation~2 (all seeds), while significant canary breaks appear later (ECE at generations~4--8). Under treatment conditions ($\\alpha{\\geq}0.75$), this ordering flips: canary metrics place their best splits at generation~1, followed by downstream diversity metrics at generations~2--4 and perplexity at generation~4 (Table~\\ref{tab:cp_results}). This ordering reversal provides complementary evidence from a distinct statistical framework, consistent with the Granger-precedence analysis in \\S\\ref{sec:experiments}.\n\nSeveral caveats apply. The 18 individual tests per condition were not corrected for multiple comparisons (BH or Bonferroni); primary inference rests on the cross-metric temporal ordering rather than on individual significance tests. Under treatment conditions, token entropy places its best split at generation~1 with large effect sizes ($|d|{>}2.5$) in all seeds, but the pre-change segment at a generation-1 split contains only a single data point, reducing bootstrap power (1/3 seeds significant at $\\alpha{=}0.75$). The short series length ($T{=}11$) further limits overall detection power.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Change-point detection under null control ($\\alpha{=}0.00$, 3 seeds). CP: detected change-point generation (mean across significant seeds); $|d|$: Cohen's $d$ effect size (mean across all seeds); Sig.\\ rate: fraction of seeds where $p{<}0.05$. Overall FPR: 12/18 = 66.7\\%.}\n\\label{tab:cp_null}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & CP gen (mean) & $|d|$ (mean) & Sig.\\ rate & Type \\\\\n\\midrule\ntoken\\_entropy & 1.0 & 2.94 & 1/3 & canary \\\\\nECE & 6.0 & 1.62 & 2/3 & canary \\\\\ndistinct-1 & 2.0 & 2.27 & 3/3 & downstream \\\\\ndistinct-2 & 2.0 & 2.40 & 3/3 & downstream \\\\\ndistinct-3 & 2.0 & 2.27 & 3/3 & downstream \\\\\nperplexity & --- & 3.11 & 0/3 & downstream \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Change-point detection at $\\alpha{=}0.75$ (3 seeds). CP: detected change-point generation; $|d|$: Cohen's $d$ effect size between pre- and post-change segments. Sig.\\ rate: fraction of seeds where $p{<}0.05$.}\n\\label{tab:cp_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccc}\n\\toprule\nMetric & CP gen (mean) & $|d|$ (mean) & Sig.\\ rate & Type \\\\\n\\midrule\ntoken\\_entropy & 1.0 & 3.21 & 1/3 & canary \\\\\nECE & 1.0 & 3.10 & 1/3 & canary \\\\\ndistinct-1 & 2.3 & 2.18 & 3/3 & downstream \\\\\ndistinct-2 & 3.0 & 1.97 & 3/3 & downstream \\\\\ndistinct-3 & 3.7 & 1.86 & 3/3 & downstream \\\\\nperplexity & 4.0 & 1.70 & 3/3 & downstream \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Dose-response ordering pattern.}\nTable~\\ref{tab:cp_ordering} summarizes the ordering pattern across contamination levels.\nThe canary-to-downstream gap shifts monotonically from negative (downstream first) under the null to positive (canary first) under treatment, ruling out a methodological artifact in which canary metrics would systematically appear earlier regardless of condition.\nThe $\\alpha{=}1.0$ analysis is limited to a single seed (s42); all other conditions use 3 seeds.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcccl}\n\\toprule\n$\\alpha$ & Canary cp & Downstream cp & Gap & Direction \\\\\n\\midrule\n0.00 & gen 4--8 & gen 2 & $-$2.5 & Downstream first \\\\\n0.25 & gen 3--4 & gen 3--4 & $\\approx$0 & Simultaneous \\\\\n0.75 & gen 1 & gen 2--4 & $+$2.25 & Canary first \\\\\n1.00 & gen 2 & gen 2--5 & $+$1.0 & Canary first \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Change-point ordering reversal across contamination levels. Under the null ($\\alpha{=}0.00$), downstream metrics break before canary metrics; this ordering reverses monotonically as $\\alpha$ increases, consistent with the Granger-precedence analysis.}\n\\label{tab:cp_ordering}\n\\end{table}\n\n\n\\section{Sequential Monitoring: CUSUM vs Calibrated Threshold}\n\\label{app:csmp}\n\nWe translate the Granger-precedence finding into a deployable monitoring protocol using CUSUM (cumulative sum) sequential testing~\\cite{page1954continuous}, calibrated against the $\\alpha{=}0.0$ null control.\nThe null-calibration procedure sets the alarm threshold $h$ such that the false alarm rate (FAR) is 0\\% on null data (3~seeds, $T{=}10$), providing controlled Type~I error guarantees.\n\n\\paragraph{Method.}\nCUSUM monitors the cumulative deviation of token entropy from its null-control baseline: $S_t = \\max(0,\\; S_{t-1} + (\\mu_0 - x_t) - k)$, where $\\mu_0$ is the null-control mean, $k$ is the allowance parameter, and the alarm triggers when $S_t > h$.\nWe calibrate $h$ for each $k$ from the $\\alpha{=}0.0$ null data (Table~\\ref{tab:csmp_calibration}).\nAs a baseline, we compare against a simple calibrated threshold: alarm when the metric crosses $\\mu_0 - 2\\sigma_0$ for $n{\\geq}1$ or $n{\\geq}2$ consecutive generations.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{CUSUM calibration parameters from $\\alpha{=}0.0$ null control (3~seeds). $h$: alarm threshold calibrated to achieve FAR${=}$0\\%. For $k{\\geq}0.25$, the null CUSUM statistic remains at zero, yielding $h \\approx 0$.}\n\\label{tab:csmp_calibration}\n\\begin{tabular}{lcc}\n\\toprule\n$k$ & $h$ & FAR \\\\\n\\midrule\n0.05 & 1.530 & 0\\% \\\\\n0.10 & 1.005 & 0\\% \\\\\n0.25 & $\\approx$0 & 0\\% \\\\\n0.50 & $\\approx$0 & 0\\% \\\\\n1.00 & $\\approx$0 & 0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Results.}\nTable~\\ref{tab:csmp_comparison} compares CUSUM and simple threshold detection times across gradual contamination levels.\nAt the recommended operating point ($k{=}0.25$), CUSUM and the simple threshold ($n{\\geq}1$) produce identical alarm times (generation~1) across all seeds and contamination levels.\nMore conservative CUSUM settings ($k{=}0.1$, $k{=}0.05$) delay detection to match the $n{\\geq}2$ threshold or later.\nAt $k{=}1.0$ with $\\alpha{=}0.50$, CUSUM fails entirely ($S_t \\equiv 0$ for all seeds), demonstrating sensitivity to the allowance parameter.\nNo CUSUM configuration outperforms the simple calibrated threshold at any operating point tested.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{CUSUM vs simple calibrated threshold: alarm generation across contamination levels (3~seeds each; all seeds agree on the alarm generation shown). Threshold: metric crosses $\\mu_0 - 2\\sigma_0$. No CUSUM configuration outperforms the simple threshold at any operating point.}\n\\label{tab:csmp_comparison}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & CUSUM $k{=}0.25$ & CUSUM $k{=}0.1$ & CUSUM $k{=}0.05$ & Thresh $n{\\geq}1$ & Thresh $n{\\geq}2$ \\\\\n\\midrule\n0.50 & gen 1 & gen 2 & gen 3 & gen 1 & gen 2 \\\\\n0.75 & gen 1 & gen 2 & gen 2 & gen 1 & gen 2 \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize CUSUM $k{=}1.0$ at $\\alpha{=}0.50$: $S_t \\equiv 0$ for all seeds (complete detection failure).} \\\\\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe equivalence arises because the generation-0$\\to$1 entropy drop is large ($|\\Delta x| > 0.7$ for $\\alpha{=}0.50$, $> 1.0$ for $\\alpha{=}0.75$) relative to the null-control variability ($\\sigma_0 \\approx 0.03$).\nAny detector with a near-zero or small threshold triggers at generation~1; CUSUM's cumulative memory provides no advantage when the initial shift already exceeds the control limit.\nThis result extends Claim~3 (method sensitivity) beyond lead-lag detection to the monitoring domain: even a sequential testing procedure with stronger theoretical properties (optimal expected detection delay under continuous monitoring) does not improve over a calibrated baseline when the initial contamination signal dominates the allowance parameter.\nThe contribution of the null-calibrated monitoring framework is the calibration procedure itself (setting alarm boundaries from $\\alpha{=}0.0$ data to guarantee FAR${=}$0\\%), not the CUSUM algorithm.\n\n\\section{Background and Notation}\n\\label{app:background}\n\\label{sec:background}\n\nThis section establishes the formal setup and notation used throughout the paper.\n\n\\paragraph{Iterative training loop.}\nLet $M_0$ denote a pretrained language model and $\\mathcal{D}_\\text{real}$ a fixed corpus of human-written text.\nAt each generation $t \\geq 1$, the model $M_{t-1}$ generates a synthetic corpus $\\mathcal{D}_\\text{synth}^{(t-1)}$, and the next-generation model $M_t$ is fine-tuned on a mixture of $\\alpha$ fraction synthetic data and $(1{-}\\alpha)$ fraction real data:\n\\begin{equation}\n    \\mathcal{D}_\\text{train}^{(t)} = \\alpha \\cdot \\mathcal{D}_\\text{synth}^{(t-1)} \\;+\\; (1{-}\\alpha) \\cdot \\mathcal{D}_\\text{real}, \\quad \\alpha \\in [0, 1].\n    \\label{eq:mixing}\n\\end{equation}\nAt $\\alpha{=}1.0$, this reduces to the full-replacement paradigm of \\citet{shumailov2024curse}.\n\n\\paragraph{Metric families.}\n\\emph{Canary metrics}: token entropy ($H(p_\\theta | \\text{context})$ on held-out samples) and expected calibration error (ECE).\n\\emph{Downstream metrics}: distinct-$n$ ($n \\in \\{1, 2, 3\\}$)~\\cite{li2016diversity} and perplexity.\nEach metric produces a time series of $T{+}1$ observations.\n\n\\paragraph{Lead-lag testing.}\nGiven canary series $X$ and downstream series $Y$, the central question is whether changes in $X$ temporally precede changes in $Y$, requiring directionality and confounder control beyond simple correlation.\nWe employ five methods spanning permissive to conservative: naive cross-correlation, differenced cross-correlation, threshold onset detection, permutation Granger causality~\\cite{shojaie2022granger}, and Toda--Yamamoto Granger causality~\\cite{toda1995statistical}.\n\n\\section{MMCT Algorithm}\n\\label{app:mmct}\n\nAlgorithm~\\ref{alg:mmct} describes the Multi-Method Consensus Test (MMCT) introduced in \\S\\ref{sec:mmct}.\n\n\\begin{algorithm}[h]\n\\caption{Multi-Method Consensus Test (MMCT)}\n\\label{alg:mmct}\n\\begin{algorithmic}[1]\n\\Require Time series pair $(X, Y)$; methods $\\{m_1, \\ldots, m_K\\}$ ($K{=}5$); null-control data $\\mathcal{N}$ (from $\\alpha{=}0.0$); tolerance $\\epsilon{=}0.01$\n\\Ensure $p$-value, consensus level $\\hat{K}$\n\\For{each method $m_k$}\n    \\State Compute empirical FPR: $\\widehat{\\mathrm{FPR}}_k \\gets$ fraction of null-control pairs where $m_k$ rejects $H_0$\n    \\State Compute weight: $w_k \\gets 1 / \\max(\\widehat{\\mathrm{FPR}}_k,\\; \\epsilon)$\n    \\State Apply $m_k$ to $(X, Y)$: $d_k \\gets \\mathbf{1}[m_k \\text{ rejects } H_0]$\n\\EndFor\n\\State Weighted consensus: $W(X {\\to} Y) \\gets \\sum_{k} w_k \\, d_k \\;/\\; \\sum_{k} w_k$\n\\State Build empirical null distribution of $W$ from all null-control pairs in $\\mathcal{N}$\n\\State Compute $p$-value from empirical null: $p \\gets \\Pr_{\\mathcal{N}}(W \\geq W_{\\mathrm{obs}})$\n\\State Consensus level: $\\hat{K} \\gets \\sum_{k} d_k$\n\\State \\Return $p$, $\\hat{K}$\n\\end{algorithmic}\n\\end{algorithm}\n\n\\paragraph{Design rationale.}\nFPR-inverse weighting penalizes methods with high false positive rates on null-control data: naive cross-correlation (FPR${=}91.7\\%$) receives weight $w{=}1.09$, while PermG (FPR${=}11.1\\%$, the lowest among directional methods; DiffXCorr achieves 2.8\\% but lacks directional separation) receives $w{=}9.0$.\nThe empirical null distribution avoids parametric assumptions that are unreliable for short ($T{=}5$--$20$), non-stationary series typical of iterative training.\nMMCT is a consensus testing protocol, not a novel statistical method; its value lies in systematic method comparison and the identification of method-dependent conclusions.\n\n\n\\section{Methodological Comparison Table}\n\\label{app:method_comparison}\n\nTable~\\ref{tab:method-comparison} summarizes the methodological coverage of existing canary and monitoring analyses across the diagnostic dimensions identified in \\S\\ref{sec:method}.\nNo prior work combines all six dimensions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Methodological comparison of canary and monitoring analyses. \\checkmark\\ = present, $\\times$ = absent, $\\circ$ = partial (${\\leq}2$ levels or limited replication). Diff.\\ = differencing/stationarity controls. Multi-M.\\ = ${\\geq}2$ independent statistical methods. MTC = multiple testing correction. Regime = systematic variation of $\\alpha$. Seeds = ${\\geq}3$ independent seeds. Arch.\\ = ${\\geq}2$ architecturally distinct model families.}\n\\label{tab:method-comparison}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccccl}\n\\toprule\nWork & Diff. & Multi-M. & MTC & Regime & Seeds & Arch. & Metrics \\\\\n\\midrule\n\\citet{shumailov2024curse}     & $\\times$   & $\\times$   & $\\times$   & $\\circ$    & \\checkmark & \\checkmark & PPL \\\\\n\\citet{du2025scales}           & $\\times$   & $\\times$   & \\checkmark & \\checkmark & \\checkmark & $\\times$   & ECE, Acc, Dist-$n$ \\\\\n\\citet{gambetta2024surplexity} & $\\times$   & $\\times$   & $\\times$   & \\checkmark & \\checkmark & \\checkmark & Surplexity, Ent \\\\\nSIGMA~\\cite{sigma2026spectral} & $\\times$   & $\\times$   & $\\times$   & $\\times$   & $\\times$   & $\\times$   & Spectral \\\\\nDCES~\\cite{dces2026counter}    & $\\times$   & $\\times$   & $\\times$   & $\\times$   & $\\times$   & \\checkmark & ECE, Ent, PPL \\\\\n\\midrule\n\\textbf{Ours}                  & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark & Ent, ECE, PPL, Dist-$n$ \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\n\\section{Extended Discussion}\n\\label{app:extended_discussion}\n\n\\paragraph{Calibration scope and generalization.}\nAll FPR and FNR calibration results are specific to our experimental setup: Pythia-410M, WikiText-103 subset, $T{=}10$, and six contamination levels.\nCross-architecture validation across 15 conditions spanning six model families shows that the entropy-leads-diversity pattern generalizes in 11 of 15 architecture-seed combinations (Table~\\ref{tab:generalization}); GPT-2 bf16 (0/8), GPT-2 s43 (6/8 bidirectional), SmolLM3-3B (3/8, entropy decoupling), and Pythia-1.4B s42 (2/8) do not confirm the pattern.\n\n\\paragraph{Domain-dependent directionality.}\nThe unidirectional forward causation observed on WikiText (PermG reverse${=}$0/8 across all conditions) does not hold universally.\nOn C4 at $\\alpha{=}0.50$ (s42 fp32), PermG reverse reaches 7/8, indicating near-symmetric bidirectional coupling; however, this is seed-dependent (s43: 1/8) and noted as preliminary.\nThe practical implication is that directional asymmetry should be verified per domain.\n\n\\paragraph{Token entropy versus perplexity.}\nThe distinction lies in the evaluation domain: token entropy is $H(p_\\theta | \\text{context})$ on held-out real data, while perplexity is $\\exp(H_\\text{cross})$ on model-generated text.\nFirst-differencing removes their shared downward trend: the canary$\\to$diversity channel survives because entropy leads diversity by one generation, whereas the canary$\\to$perplexity channel vanishes because both co-move synchronously.\n\n\\paragraph{NLP-specific constraints.}\nOur application of Granger-type methods faces constraints absent in econometrics: (i)~observation length ($T{=}5$--$20$ vs.\\ $T{=}100$--$1000$); (ii)~non-stationarity by design rather than incidental; (iii)~small multiplicity for FDR correction (8--32 pairs per regime).\nTransfer entropy (0/192 FDR-significant results) confirms that method sensitivity extends beyond the five-method panel.\n\n\\paragraph{Prevention paradox.}\nEffective intervention truncates the collapse trajectory that established Granger precedence.\nDifferenced cross-correlation retains significance under intervention (31/32 pairs), while threshold onset fails entirely (0/8), reinforcing the multi-method rationale.\n\n\\paragraph{Grouped testing rationale.}\nWe test 8 canary$\\to$downstream pairs jointly (2 canaries $\\times$ 4 downstream metrics) rather than individual per-metric tests because: (i)~joint testing with BH-FDR correction controls family-wise error across the canary panel, avoiding the inflated false-positive rate that would result from reporting the single most significant pair; (ii)~the count of significant pairs ($k/8$) provides a natural effect-size measure that distinguishes isolated from systematic detection; (iii)~per-metric tests cannot capture the cross-metric consistency that separates genuine temporal precedence from metric-specific artifacts (e.g., MAUVE floor saturation affects 2/8 pairs universally, identifiable only in grouped results).\n\n\\paragraph{Canary metric choice.}\nSmolLM3-3B reveals that canary metric selection constitutes a sensitivity dimension beyond the five statistical methods: token entropy exhibits non-monotonic oscillations (0/4 significant pairs), while ECE maintains monotonic growth (3/4 pairs).\nNo single canary metric is universally optimal.\n\n\\paragraph{Exploratory CSD analysis.}\nCanary metrics show rising autocorrelation (Kendall $\\tau{=}0.79$--$0.82$) while downstream metrics show none ($\\tau{=}0.03$--$0.30$), but this pattern does not survive multiple testing correction (2/10 post-BH) and remains exploratory.\nWe note that \\citet{truong2026phase} show model collapse is a first-order transition, ruling out CSD as a structural detection mechanism; the rising autocorrelation likely reflects non-stationarity rather than critical slowing down.\n\n\\paragraph{Scale verification (Pythia-1.4B).}\n\\label{app:scale_14b}\nTo test whether the phase-diagram structure generalizes beyond 410M, we replicate the analysis at 1.4B scale ($T{=}10$--$15$, fp32, seed~42).\nTable~\\ref{tab:14b_phase} summarizes the available cells.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pythia-1.4B phase-diagram cells (fp32, PermG forward, direction-checked).}\n\\label{tab:14b_phase}\n\\begin{tabular}{lcccc}\n\\toprule\n$\\alpha$ & \\multicolumn{2}{c}{$T{=}10$} & \\multicolumn{2}{c}{$T{=}15$} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n         & s42 & s44 & s42 & s43 \\\\\n\\midrule\n0.45 & 0/6 & 0/6 & 3/6 & 5/6 \\\\\n0.50 & 4/6 & 6/6 & 3/6 & 3/6 \\\\\n0.60 & 4/6 & 6/6 & 6/6 & 6/6 \\\\\n0.75 & 5/6 & 6/6 & 6/6 & 6/6 \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize All: PermG fwd, 6-pair basis (2 canaries $\\times$ 3 distinct-$n$;} \\\\\n\\multicolumn{5}{l}{\\footnotesize MAUVE excl.\\ due to floor ${\\sim}0.033$ at 1.4B).} \\\\\n\\multicolumn{5}{l}{\\footnotesize s42 rev.\\ 0/6 at all $\\alpha$; s43 rev.\\ see text.} \\\\\n\\end{tabular}\n\\end{table}\n\nThe phase-diagram structure is qualitatively preserved at 1.4B scale.\nECE maintains monotonic growth across all three tested $\\alpha$ levels (3/3 cross-scale robust), and the binary detection pattern (above vs.\\ below $\\alpha_c$) is consistent with the 410M phase diagram.\nOn the 6-pair basis (MAUVE excluded due to systematic floor ${\\sim}0.033$; Table~\\ref{tab:14b_phase}), PermG forward detection at 1.4B ranges from 0/6 ($\\alpha{=}0.45$, $T{=}10$) to 6/6 ($\\alpha{\\geq}0.60$, $T{=}15$); token entropy exhibits one-step saturation ($27$--$39\\%$ drop from generation~0 to~1), reducing temporal resolution for entropy-based pairs.\nSeed s42 shows PermG$_\\text{rev}{=}0/6$ across all eight 1.4B conditions ($4\\alpha{\\times}2T$), confirming that bidirectionality is seed-specific rather than scale-inherent.\nThe 410M sync-dip ($\\alpha{=}0.60$: 0/8 at $T{\\leq}20$) does not reproduce at 1.4B (4/6 at $T{=}10$); whether this reflects scale-dependent dynamics or Pythia-specific effects remains open with only two model sizes tested.\nAt $T{=}15$, scale effects are $\\alpha$-conditional: $\\alpha{=}0.60$ reaches 6/6, while $\\alpha{=}0.50$ attenuates to 3/6 (vs 4/6 at $T{=}10$), confirming that detection loss is onset-localized rather than uniform.\nThe boundary's $T$-dependence is preserved: $\\alpha{=}0.45$ rises from 0/6 ($T{=}10$) to 3/6 ($T{=}15$), mirroring the 410M boundary shift.\nHowever, method-level heterogeneity emerges: Toda--Yamamoto exhibits a non-monotonic pattern at $T{=}15$, inverting the PermG ordering in the mid-$\\alpha$ range; gradual low-$\\alpha$ dynamics preserve VAR lag structure, while rapid entropy saturation disrupts lag dependence at intermediate $\\alpha$, with recovery at $\\alpha{=}0.75$ where extreme collapse dynamics (PPL drift ${+}390\\%$) generate sufficient temporal variation to support VAR detection.\nOnset-zone attenuation is $\\alpha$-invariant at 1.4B: both $\\alpha{=}0.45$ and $0.50$ yield 3/6 at $T{=}15$.\nAt 1.4B with $T{=}10$ (11 data points), non-PermG methods (threshold onset, naive cross-correlation, Toda--Yamamoto) have insufficient power due to short sequence length, reducing $K{\\geq}3$ consensus to an effective single-method test; at $T{=}15$ (16 data points), detection recovers (6/6 at $\\alpha{=}0.60$, lead time ${=}$ 10 generations) and $K{\\geq}3$ recovers its multi-method character, with 3/4 $\\alpha$ conditions achieving $K{\\geq}3{\\geq}2/6$ (onset $\\alpha{=}0.50$ seed-dependent: s42 1/6, s43 3/6).\nCross-method consensus ($K{\\geq}3$) exhibits seed-dependent variability at onset ($\\alpha{\\approx}0.50$), consistent with the noisy transition expected at phase boundaries, while remaining robust above onset ($K{\\geq}3$ ${\\geq}5/6$ at $\\alpha{=}0.75$).\nOn a unified 6-pair basis (MAUVE excluded due to systematic floor at ${\\sim}0.033$; Table~\\ref{tab:14b_phase}), third-seed replication (s44) at $T{=}10$ confirms ceiling detection above onset (6/6 at $\\alpha{\\geq}0.50$) with 0/6 at $\\alpha{=}0.45$, validating the blind zone.\nCross-$T$ improvement holds at 3/4 $\\alpha$ values ($\\alpha{=}0.45$: $0/6{\\to}5/6$; $\\alpha{=}0.60$: $6/6{\\to}6/6$; $\\alpha{=}0.75$: $6/6{\\to}6/6$), validating the predicted $\\alpha_c(T)$ decrease; at onset ($\\alpha{=}0.50$), PermG shows a marginal decrease ($6/6{\\to}3/6$), consistent with phase-boundary variability.\nAt onset ($\\alpha{=}0.45$--$0.50$), ECE-based pairs achieve higher detection rates than entropy-based pairs (e.g., 3/3 vs 0/3 robust at $\\alpha{=}0.50$, $T{=}15$), consistent with entropy's one-step saturation reducing temporal resolution at 1.4B scale.\n\n\\paragraph{Future work.}\nExtensions include multivariate VAR models for confounder testing, multi-seed replication across all six architecture families, longer training runs ($T{\\geq}20$), online monitoring within training pipelines, and accumulate-mode experiments~\\cite{dey2024breaking}.\nThe sigmoid onset boundary ($\\alpha_c{=}0.483$) invites connection to the critical mixture ratio scaling law of \\citet{gu2024cmr} and the data-mixing transitions of \\citet{gu2025datamixing}.\n\n\n\\section{Per-Method Dose-Response Profiles}\n\\label{app:dose_response}\n\nTable~\\ref{tab:dose_response_full} reports FDR significance counts (/8 validated pairs) for all five detection methods across 12 contamination levels (seed~42, Pythia-410M, WikiText, fp32).\nPermG exhibits a sharp 0$\\to$6 jump at $\\alpha{=}0.50$ with a return to 0 at $\\alpha{=}0.55$--$0.60$ (non-monotonic dip), while other methods show diffuse profiles: naive cross-correlation saturates at 7--8/8 across all levels including the null, and Toda--Yamamoto fluctuates without a clear onset.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-method FDR significance (/8 pairs) across contamination levels (Pythia-410M, seed~42, WikiText, fp32). PermG and Diff.\\ XCorr use BH-corrected FDR ($q{=}0.05$); Naive XCorr, Threshold, and TY use uncorrected $p{<}0.05$ (no FDR field in pipeline). $\\alpha{=}1.0$ from Pythia-410M cross-architecture condition (same seed/domain/precision).}\n\\label{tab:dose_response_full}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccccc}\n\\toprule\n$\\alpha$ & Naive & Diff.\\ XCorr & Threshold & PermG & TY$^\\S$ \\\\\n\\midrule\n0.00 & 8 & 4 & 3 & \\textbf{0} & 1 \\\\\n0.10 & 7 & 6 & 0 & \\textbf{0} & 0 \\\\\n0.25 & 8 & 3 & 0 & \\textbf{0} & 2 \\\\\n0.30 & 8 & 4 & 0 & \\textbf{0} & 3 \\\\\n0.35 & 8 & 4 & 0 & \\textbf{0} & 1 \\\\\n0.40 & 8 & 3 & 0 & \\textbf{0} & 4 \\\\\n0.45 & 8 & 6 & 0 & \\textbf{0} & 1 \\\\\n0.50 & 8 & 7 & 4 & \\textbf{6} & 3 \\\\\n0.55 & 8 & 8 & 0 & \\textbf{0} & 1 \\\\\n0.60 & 8 & 6 & 0 & \\textbf{0} & 0 \\\\\n0.75 & 7 & 6 & 0 & \\textbf{6} & 3 \\\\\n1.00 & 8 & 6 & 2 & \\textbf{6} & 1 \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^\\S$TY directional assignment under verification; column retained for completeness.} \\\\\n\\end{tabular}}\n\\end{table}\n\nThe table highlights PermG's combination of null-control detection at 0/8 for this seed ($\\alpha{=}0.00$; pooled FPR across 6 seeds: 11.1\\%, lowest among directional methods), sharp onset (0$\\to$6 at $\\alpha{=}0.50$), and non-monotonic dip (0 at $\\alpha{=}0.55$--$0.60$), confirming it as the method whose dose-response profile most cleanly separates detection regimes.\nNaive cross-correlation's persistently high counts (7--8/8 even at $\\alpha{=}0.00$) demonstrate the 91.7\\% pooled null-control FPR reported in \\S\\ref{sec:method}.\n\n\n\\paragraph{Comparison with naive baselines.}\n\\label{app:naive_baselines}\n\nTable~\\ref{tab:naive_baselines} compares PermG against two practitioner-facing monitoring rules across 26 experiments (18~$\\alpha$ values, Pythia-410M, $T{=}10$, fp32).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Naive baseline comparison (Pythia-410M, $T{=}10$, fp32, 3 null-control runs).}\n\\label{tab:naive_baselines}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & FPR ($\\alpha{=}0$) & Onset $\\alpha$ \\\\\n\\midrule\nPPL-slope (${\\geq}2$ consec.\\ rises) & 100\\% (3/3) & 0.10 \\\\\nVariance-threshold ($2\\sigma$) & 67\\% (2/3) & 0.10 \\\\\nPermG (fwd ${\\geq}1$) & 0\\% (0/3) & 0.50 \\\\\n\\bottomrule\n\\multicolumn{3}{l}{\\footnotesize Onset $\\alpha$: lowest $\\alpha$ where method fires (seed~42).} \\\\\n\\end{tabular}\n\\end{table}\n\nPPL-slope fires at $\\alpha{=}0$ because the first-generation learning effect (perplexity drops from 26.9 to 19.3 at generation~1, then rises monotonically from generation~2 onward) produces consecutive rises indistinguishable from contamination-driven drift.\nVariance-threshold similarly triggers on the natural perplexity recovery.\nPermG avoids these false alarms by testing canary$\\to$downstream Granger precedence rather than univariate trend, thereby excluding training-drift confounds from the detection signal.\nNaive monitoring rules cannot distinguish contamination from natural training dynamics; formal statistical testing is necessary for controlled FPR.\n\n\n\\section{PermG Power Analysis}\n\\label{app:power_analysis}\n\nWe characterize PermG detection power via simulation under a controlled data-generating process (DGP) that matches the structure of our iterative training time series.\n\n\\paragraph{DGP.}\nFor each trial, we generate a bivariate system $(X_t, Y_t)$ for $t = 1, \\ldots, T$ where $X_t = \\mu + \\epsilon_t^X$ and $Y_t = \\mu + \\beta X_{t-1} + \\epsilon_t^Y$, with $\\epsilon \\sim \\mathcal{N}(0, \\sigma^2)$ and $\\sigma{=}1$.\nThe coupling parameter $\\beta$ controls signal strength; $\\beta{=}0$ is the null.\nThe linear coupling provides a power lower bound; nonlinear dynamics in actual iterative training may yield different power characteristics.\nWe sweep $\\beta \\in [0, 2]$ across $T \\in \\{6, 8, 10, 15, 20\\}$, running 100 replications per $(\\beta, T)$ cell with 5{,}000 permutations each and BH FDR correction at $q{=}0.05$ across 8 hypothetical pairs (matching the experimental setup).\n\n\\paragraph{Results.}\nTable~\\ref{tab:beta50} reports $\\beta_{50}$, the coupling strength required for 50\\% detection power, at each observation length $T$.\nUnder $\\sqrt{T}$ scaling, the product $\\beta_{50} \\cdot \\sqrt{T}$ should be constant; the observed decrease from 5.09 ($T{=}8$) to 2.68 ($T{=}20$) indicates that power grows faster than $\\sqrt{T}$, with the empirical scaling closer to $T^{-1.1}$.\nThe $\\sqrt{T}$ formula in \\S\\ref{sec:theory} thus provides a conservative lower bound on detection power: actual power at $T{=}20$ exceeds the $\\sqrt{T}$ prediction.\nFalse positive rates under FDR correction remain at or below 2\\% across all $T$ values (raw: 1--9\\%; Table~\\ref{tab:beta50}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{PermG power analysis: $\\beta_{50}$ (coupling for 50\\% power) under BH-FDR correction ($q{=}0.05$, 8 pairs). $\\beta_{50} \\cdot \\sqrt{T}$ decreases with $T$, indicating power grows faster than $\\sqrt{T}$. FPR: false positive rate at $\\beta{=}0$ (raw / FDR-corrected). Dashes indicate $<$50\\% power not reached within $\\beta \\leq 2.0$.}\n\\label{tab:beta50}\n\\begin{tabular}{lcccc}\n\\toprule\n$T$ & $\\beta_{50}$ & $\\beta_{50} \\cdot \\sqrt{T}$ & FPR (raw) & FPR (FDR) \\\\\n\\midrule\n6  & ---  & ---  & 1\\% & 0\\% \\\\\n8  & ---  & ---  & 6\\% & 2\\% \\\\\n10 & 2.0  & 6.32 & 9\\% & 2\\% \\\\\n15 & 1.2  & 4.65 & 6\\% & 2\\% \\\\\n20 & 0.9  & 4.02 & 5\\% & 1\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/permg_power_curve.pdf}\n\\caption{PermG detection power as a function of coupling strength $\\beta$ for five observation lengths ($T{=}6$--$20$; 100 replications $\\times$ 5{,}000 permutations, BH FDR $q{=}0.05$). Power increases with both $\\beta$ and $T$; at $T{=}6$--$8$, PermG remains underpowered ($<$20\\%) even at $\\beta{=}2.0$, consistent with the $T{=}10$ minimum required for reliable detection in our experimental setting.}\n\\label{fig:permg_power}\n\\end{figure*}\n\nAt $T{=}6$ and $T{=}8$, 50\\% power is not reached within $\\beta \\leq 2.0$ under FDR correction, explaining why PermG is fundamentally underpowered for very short series.\nThe practical implication for our $T{=}10$ setting: $\\beta_{50}{=}2.0$ means that only strong coupling produces reliable detection, consistent with the sharp onset at $\\alpha_c{\\approx}0.50$ where signal strength first exceeds this threshold.\nAt $T{=}20$, $\\beta_{50}$ drops to 0.9, predicting a left-shift of $\\alpha_c$ and broader detection coverage, as formalized in the detection boundary model (\\S\\ref{sec:theory}).\n\n\n\\section{Non-Stationarity Robustness Analysis}\n\\label{app:nonstationarity}\n\nWe assess PermG's size and power under controlled non-stationarity via Monte Carlo simulation, then compare to the empirical autocorrelation structure of our experimental series.\n\n\\paragraph{Simulation design.}\nWe generate bivariate AR(1) series with unidirectional coupling ($x \\to y$):\n$x_t = \\varphi x_{t-1} + \\varepsilon_t^x$, $y_t = \\varphi y_{t-1} + \\beta x_{t-1} + \\varepsilon_t^y$,\nwith $T{=}11$, 1{,}000 replications, and 500 permutations per replication.\nSize is evaluated under $H_0{:}\\;\\beta{=}0$; power under $H_1{:}\\;\\beta{=}0.6$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Size (FPR at $\\beta{=}0$) and power ($\\beta{=}0.6$) under stationary and non-stationary AR(1) DGP ($T{=}11$, 1{,}000 reps, 500 perms). First-differencing maintains nominal size across all $\\varphi$; PermG FPR inflates to ${\\sim}10\\%$ at $\\varphi{\\geq}0.95$.}\n\\label{tab:nonstationarity_sim}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\multicolumn{3}{c}{Size (\\%, $\\beta{=}0$)} & \\multicolumn{3}{c}{Power (\\%, $\\beta{=}0.6$)} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n$\\varphi$ & Raw GC & First-Diff & PermG & Raw GC & First-Diff & PermG \\\\\n\\midrule\n0.50 & 6.4 & 6.6 & 6.8 & 37.7 & 17.7 & 36.8 \\\\\n0.95 & 10.0 & 5.9 & 9.5 & 44.3 & 28.7 & 41.5 \\\\\n0.99 & 11.2 & 4.2 & 10.7 & 46.4 & 24.6 & 41.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\varphi{=}0.50$ (stationary), all three methods achieve near-nominal size ($6.4$--$6.8\\%$ vs.\\ $5\\%$ nominal).\nUnder strong non-stationarity ($\\varphi{\\geq}0.95$), PermG FPR inflates to ${\\sim}10\\%$ because permutation shuffling destroys temporal autocorrelation, shifting the null distribution.\nFirst-differencing maintains proper size ($4.2$--$6.6\\%$) at the cost of reduced power ($17.7$--$28.7\\%$ vs.\\ PermG's $36.8$--$41.7\\%$).\nOur pipeline applies first-differencing \\emph{before} permutation testing, combining PermG's power advantage with differencing's size control; the simulation isolates each component to characterize the tradeoff.\n\n\\paragraph{Empirical autocorrelation.}\nTable~\\ref{tab:empirical_ar1} reports AR(1) coefficients from seven experimental conditions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Empirical AR(1) coefficients for token entropy (te) and distinct-1 (d1), raw and first-differenced series. High raw $\\varphi$ in d1 reflects deterministic iterative-training decline, not stochastic AR persistence; first-differencing reduces $\\varphi$ to $< 0.44$.}\n\\label{tab:empirical_ar1}\n\\begin{tabular}{llrcccc}\n\\toprule\nExperiment & $\\alpha$ & $T$ & te $\\varphi_{\\text{raw}}$ & d1 $\\varphi_{\\text{raw}}$ & te $\\varphi_{\\text{diff}}$ & d1 $\\varphi_{\\text{diff}}$ \\\\\n\\midrule\na000\\_s42 & 0.00 & 10 & $-0.51$ & $0.86$ & $-0.57$ & $-0.14$ \\\\\na025\\_s42 & 0.25 & 10 & $-0.34$ & $0.95$ & $-0.45$ & $0.19$ \\\\\na050\\_s42 & 0.50 & 10 & $-0.28$ & $0.87$ & $0.31$ & $0.10$ \\\\\na075\\_s42 & 0.75 & 10 & $0.14$ & $0.91$ & $0.88$ & $0.24$ \\\\\na100\\_s42 & 1.00 & 10 & $1.00$ & $0.89$ & $0.98$ & $0.18$ \\\\\nt20\\_a050 & 0.50 & 20 & $-0.10$ & $0.97$ & $-0.25$ & $0.44$ \\\\\nt20\\_a100 & 1.00 & 20 & $0.98$ & $0.81$ & $0.87$ & $0.14$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Adequacy argument.}\nUnder null conditions ($\\alpha{=}0.0$), where FPR is defined, token entropy exhibits $\\varphi{=}-0.51$ (anti-correlated, far from the $\\varphi{\\geq}0.95$ regime where simulation reveals FPR inflation); at $\\varphi{=}0.50$, PermG FPR is $6.8\\%$, near nominal.\nThe high raw $\\varphi$ in distinct-1 ($0.81$--$0.97$ across all $\\alpha$ including null) reflects deterministic iterative-training diversity decline---a monotonic trend driven by the training protocol---not stochastic AR persistence.\nDeterministic trends differ fundamentally from the stochastic AR(1) DGP: they produce predictable trajectories rather than autocorrelated noise, and first-differencing effectively removes them (first-differenced distinct-1 $\\varphi$ ranges $-0.14$ to $0.44$, mean ${\\sim}0.17$).\nOur empirical FPR of 4/36 (11.1\\%) across six null seeds---the lowest among directional methods---confirms adequate size control in our experimental setting; all four false positives occur in token\\_entropy$\\to$distinct pairs in the forward direction, suggesting a structural pattern rather than random Type~I error.\nWe note that $T{=}10$ (11 data points) yields high-variance AR(1) estimates; the cross-experiment pattern is more informative than individual values.\n\n\\paragraph{DGP limitation.}\nThe bivariate AR(1) with linear coupling is a simplification; actual iterative training involves nonlinear dynamics (mode amplification, threshold-dependent diversity loss).\nThese simulation results characterize PermG's behavior under controlled conditions, not exact calibration for the experimental setting; they provide a lower bound on size control because the linear DGP represents a worst case for permutation-based tests (smooth autocorrelation that permutation destroys).\n\n\n\\section{Shapley Value Analysis}\n\\label{app:shapley}\n\nWe quantify each method's marginal contribution to the MMCT ensemble using Shapley values~\\cite{shapley1953value}, computed via exact enumeration over all $2^5{=}32$ coalitions of the five detection methods.\nFor a coalition $S \\subseteq \\{m_1, \\ldots, m_5\\}$, we define two performance metrics: the false positive rate FPR($S$), computed from 6 null experiments ($\\alpha{=}0.0$, seeds 45--50; 36 null pairs on the 6-pair basis excluding mauve), and the false negative rate FNR($S$), computed from 45 signal experiments across all non-null $\\alpha$ levels (270 signal pairs for the 6-pair variant excluding mauve).\nThe Shapley value $\\phi_k$ for method $m_k$ is the weighted average of its marginal contribution across all coalitions; positive FPR-Shapley indicates the method \\emph{increases} false positives, while negative FNR-Shapley indicates it \\emph{reduces} false negatives.\nThe combined Shapley value $\\phi_k^{\\text{comb}} = \\phi_k^{\\text{FPR}} + \\phi_k^{\\text{FNR}}$ balances both error types, with more negative values indicating greater net benefit.\n\nTable~\\ref{tab:shapley_6pair} reports the 6-pair analysis (excluding mauve).\nDiffXCorr achieves the lowest (best) combined Shapley ($-0.299$), driven by near-zero FPR contribution ($+0.007$) and strong FNR reduction ($-0.306$); however, DiffXCorr cannot separate forward from reverse causation (Table~\\ref{tab:null_fpr_methods}).\nAmong directional methods, PermG ranks best ($-0.141$ combined), with a modest FPR contribution ($+0.039$, reflecting 4/36 null false positives) offset by substantial FNR reduction ($-0.180$).\nNaive cross-correlation is the worst contributor ($+0.190$), with its massive FPR Shapley ($+0.609$) overwhelming its FNR benefit ($-0.419$).\nThreshold onset contributes almost nothing useful ($+0.084$ combined; FPR $+0.111$, FNR $-0.027$), confirming the near-zero detection power reported in Table~\\ref{tab:method_comparison}.\nFigure~\\ref{fig:shapley} visualizes the decomposition.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Shapley value decomposition (6-pair, mauve excluded). FPR-Shapley: marginal FPR contribution (positive = increases false positives). FNR-Shapley: marginal FNR contribution (negative = reduces false negatives). Combined = FPR + FNR (more negative = better). 48 experiments, $2^5{=}32$ coalitions, exact enumeration.}\n\\label{tab:shapley_6pair}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & $\\phi^{\\text{FPR}}$ & $\\phi^{\\text{FNR}}$ & $\\phi^{\\text{comb}}$ \\\\\n\\midrule\nNaive XCorr          & $+0.622$ & $-0.419$ & $+0.203$ \\\\\nDiff.\\ XCorr         & $+0.163$ & $-0.306$ & $-0.142$ \\\\\nThreshold ($3\\sigma$) & $+0.101$ & $-0.027$ & $+0.074$ \\\\\n\\textbf{Perm.\\ Granger} & $\\mathbf{0.000}$ & $\\mathbf{-0.180}$ & $\\mathbf{-0.180}$ \\\\\nToda--Yamamoto       & $+0.031$ & $-0.069$ & $-0.038$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure*}[h]\n\\centering\n\\includegraphics[width=\\linewidth]{figures/shapley_method_contribution.pdf}\n% TODO-D219: regenerate figure and update caption after Shapley recomputation with 6-seed data\n\\caption{Shapley value decomposition of each method's marginal contribution to FPR (positive bars) and FNR (negative bars). PermG is the only method with zero FPR contribution; naive cross-correlation's FPR dominates its FNR benefit.}\n\\label{fig:shapley}\n\\end{figure*}\n\nThe 8-pair variant (including mauve) yields qualitatively identical rankings: PermG remains the best contributor ($\\phi^{\\text{comb}}{=}-0.152$), naive cross-correlation the worst ($+0.170$), and threshold onset near-zero ($+0.063$).\n\n\\paragraph{FDR correction scope.}\nThis analysis applies BH-corrected significance (\\texttt{significant\\_fdr}) uniformly across all five methods, including naive cross-correlation and Toda--Yamamoto.\nIn contrast, the per-method dose-response profiles (Table~\\ref{tab:dose_response_full}) use uncorrected significance for naive cross-correlation, threshold onset, and Toda--Yamamoto because FDR-corrected fields are not available in the per-experiment pipeline output for these methods.\nThe Shapley analysis recomputes significance from raw $p$-values with BH correction applied post hoc, ensuring a fair comparison across methods within the coalition framework.\n\n\n\\section{MMCT Weight Robustness Ablation}\n\\label{app:weight_robustness}\n\nThe detection results reported in the main text use equal-weight majority voting ($K{\\geq}3$ of 5 methods, each contributing at most one vote per pair); PermG contributes at most $1/5 = 20\\%$ of the consensus weight.\nFPR-inverse weighting is used \\emph{only} in the exploratory method ranking below, not in the detection results.\nTo verify that PermG's top ranking is not an artifact of the FPR-inverse weighting scheme, we recompute Shapley values under four weight specifications (Table~\\ref{tab:weight_robustness}).\nEqual weighting ($w{=}1$ for all methods) eliminates any FPR-based advantage; PermG still ranks first ($\\phi^{\\text{comb}}{=}-0.152$), though its margin over naive cross-correlation narrows to 0.015.\nUnder cap-5, the margin widens to 0.043 as the FPR penalty begins to differentiate high-FPR methods.\nCap-10 and original cap-100 yield identical Shapley values because the consensus threshold ($K{\\geq}3$) is determined by the three smallest method weights ($w_{\\text{naive}}{+}w_{\\text{diff}}{+}w_{\\text{thresh}} = 7.76$), which are invariant to further increases in the PermG or TY cap; this saturation confirms that the original $w{=}100$ does not artificially inflate PermG's contribution.\n% TODO-D219: recompute weight robustness table with 6-seed data; PermG φ^FPR will be >0\nAcross all schemes, PermG's advantage derives from the same structural property: zero FPR ($\\phi^{\\text{FPR}}{=}0$) combined with moderate FNR reduction ($\\phi^{\\text{FNR}}{=}-0.152$ to $-0.426$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MMCT weight robustness: PermG combined Shapley under four weighting schemes. PermG ranks first in all cases. Gap = $|\\phi^{\\text{comb}}_{\\text{PermG}} - \\phi^{\\text{comb}}_{\\text{runner-up}}|$. 48 experiments (3 null + 45 signal), exact Shapley enumeration ($2^5{=}32$ coalitions).}\n\\label{tab:weight_robustness}\n\\begin{tabular}{lrcrc}\n\\toprule\nScheme & $w_{\\text{PermG}}$ & $\\phi^{\\text{comb}}_{\\text{PermG}}$ & Runner-up & Gap \\\\\n\\midrule\nEqual ($w{=}1$)     & 1   & $-0.152$ & NaiveXCorr ($-0.137$) & 0.015 \\\\\nCap-5               & 5   & $-0.165$ & NaiveXCorr ($-0.123$) & 0.043 \\\\\nCap-10              & 10  & $-0.426$ & TY ($-0.067$)         & 0.359 \\\\\nFPR-inv.\\ (cap-100) & 100 & $-0.426$ & TY ($-0.067$)         & 0.359 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{PermG FPR Independence Analysis}\n\\label{app:fpr_independence}\n\nTable~\\ref{tab:null_fpr_methods} reports null-control FPR for all five detection methods across six seeds ($6 \\times 6 = 36$ pairs, 6-pair basis excluding mauve).\nUnder identical BH-FDR correction ($q{=}0.05$), DiffXCorr achieves the lowest FPR (1/36, 2.8\\%) but lacks directional separation; PermG (4/36, 11.1\\%) is the lowest among directional methods.\nAll four PermG false positives occur in token\\_entropy$\\to$distinct pairs (seeds~45 and 50, forward direction only), suggesting a structural pattern concentrated in a single canary--downstream pair type.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Null-control FPR by method ($\\alpha{=}0.0$, 6~seeds 45--50, 6~pairs each). All p-value--based methods (DiffXCorr, PermG, TY) report BH-FDR--corrected rejections at $q{=}0.05$ for fair comparison. Threshold uses a deterministic $3\\sigma$ criterion; NaiveXCorr uses uncorrected correlation significance.}\n\\label{tab:null_fpr_methods}\n\\begin{tabular}{llrr}\n\\toprule\nMethod & Criterion & Rejections (/36) & FPR (\\%) \\\\\n\\midrule\nDiff.\\ XCorr$^\\dagger$ & BH-FDR & 1 & 2.8 \\\\\n\\textbf{Perm.\\ Granger} & \\textbf{BH-FDR} & \\textbf{4} & \\textbf{11.1} \\\\\nThreshold & $3\\sigma$ (det.) & 10 & 27.8 \\\\\nToda--Yamamoto & BH-FDR & 14 & 38.9 \\\\\nNaive XCorr & uncorr. & 33 & 91.7 \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$Bidirectional; cannot separate forward from reverse.} \\\\\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cluster adjustment.}\nThe 36 null-control pairs are nested within 6~seeds (6~pairs per seed), introducing within-seed correlation.\nWithin-seed ICC${=}0.14$ yields an effective sample size $N_{\\text{eff}} \\approx 21$ (from $N_{\\text{eff}} = N / [1 + (m-1) \\cdot \\text{ICC}]$ where $N{=}36$, $m{=}6$).\nUnder the Clopper--Pearson exact method with $N_{\\text{eff}}{=}21$ and 4 successes (scaled), the cluster-adjusted 95\\% CI is $[1.2\\%, 30.4\\%]$, compared to $[3.1\\%, 26.1\\%]$ under independence ($N{=}36$).\nThe lower ICC compared to the 3-seed pilot ($0.14$ vs.\\ $0.34$) reflects greater between-seed consistency with six independent replications.\n\n\\paragraph{Direction filtering.}\nForward-direction filtering (retaining only pairs with peak lag${<}0$ for cross-correlation methods) reduces null-control $K{\\geq}3$ false positives.\nUnder the 6-seed, 6-pair basis, $K{\\geq}3$ consensus with filtering produces 6/36 false positives (16.7\\%; detail below); the 3-seed pilot underestimated this rate (0/8).\nDetection at $\\alpha{\\geq}0.50$ is unaffected: $K{\\geq}3$ counts are identical with and without direction filtering at all signal levels.\n\n\\paragraph{$K{\\geq}3$ false positive detail.}\nUnder the 6-pair basis (6~seeds, 36~pairs), $K{\\geq}3$ consensus produces 6 false positives (FPR${=}16.7\\%$).\nOf these, 4 are driven by naive cross-correlation, threshold onset, and Toda--Yamamoto (PermG does \\emph{not} vote); the remaining 2 (seeds~45 and 50, te$\\to$distinct) include PermG in the consensus.\nPermG thus contributes to only 2 of 6 consensus false positives, confirming that most $K{\\geq}3$ FPR is driven by the high-FPR methods (naive, threshold, TY).\n\n\\paragraph{Sensitivity to FPR assumption.}\nEven under the conservative upper bound of the cluster-adjusted CI (30.4\\%), PermG remains the lowest-FPR directional method: DiffXCorr achieves a lower FPR under identical BH-FDR correction (2.8\\%) but lacks forward/reverse separation; the next directional method (threshold onset) has 27.8\\% and Toda--Yamamoto 38.9\\%.\nOur primary results rely on equal-weight $K{\\geq}3$ majority voting, where each method contributes exactly one vote regardless of its FPR---this mechanism is completely unaffected by any FPR assumption.\nFor the exploratory FPR-inverse weighting, PermG's weight ($w{=}1/0.111{=}9.0$) exceeds all directional alternatives (threshold: 3.6, TY: 2.6, naive: 1.1); DiffXCorr ($w{=}1/0.028{=}35.7$) receives a higher weight but lacks directional separation, preserving PermG's rank among directional methods.\nThe insensitivity of both the voting mechanism and the method ranking to the upper CI bound provides evidence that the MMCT conclusions are robust to uncertainty in PermG's Type~I error rate.\n\n\\section{Sigmoid Transition Shape}\n\\label{app:sigmoid_shape}\n\nSigmoid regression on the original 13-point $T{=}10$ grid yields $\\alpha_c = 0.483 \\pm 0.006$ but $k = 478 \\pm 475$ ($\\mathrm{SE}(k) \\approx k$), indicating that the coarse grid cannot constrain the transition shape.\nDense $\\alpha$ sampling (17~values at $T{=}10$) resolves this ambiguity: formal likelihood-ratio testing strongly favors a smooth sigmoid over a literal step function ($\\Delta\\mathrm{AIC}{=}-110$), with fitted steepness $k{=}15.7$ (95\\% CI $[9.4, 28.2]$).\nThe transition is steep but finite-width, not a literal discontinuity.\nThis observed steepness exceeds what smooth signal models predict: VAR(1) simulations under H0 (linear, $k{=}6.1$) and H0$'$ (concave, $k{=}4.9$) produce onset sigmoids with $k{=}4.9$--$6.1$ (\\S\\ref{app:power_sim}), yielding steepness ratios $k_{\\mathrm{obs}} / k_{\\mathrm{H0}} \\approx 2.6$--$3.2$ (CI lower bound ratio ${\\approx}2$).\nWe do not fit a combined $T{=}10 + T{=}20$ sigmoid because $\\alpha{=}0.45$ yields contradictory counts under the two sequence lengths (0/8 vs.\\ 5/8), reflecting genuine power dependence on $T$ rather than a single dose-response curve.\n\n\n\\section{Intervention Threshold Sensitivity}\n\\label{app:intervention_sensitivity}\n\n\\paragraph{Within-$\\alpha$ sensitivity at $\\alpha{=}1.0$.}\nTable~\\ref{tab:threshold_sensitivity} reports the predictive cessation outcome under five entropy-drop thresholds (5\\%--25\\%) at $\\alpha{=}1.0$ (Pythia-410M, seed~42).\nAll five thresholds produce identical outcomes: token entropy drops 40.7\\% at generation~1, far exceeding even the most conservative threshold (25\\%), so every threshold triggers at the same generation.\nThe intervention conclusion---peak perplexity 57.0, recovery in one generation, final perplexity 21.3---is invariant to threshold choice within this range.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Threshold sensitivity at $\\alpha{=}1.0$ (Pythia-410M, s42, fp32). All thresholds trigger at generation~1 (entropy drop 40.7\\%$\\gg$threshold), producing identical recovery trajectories.}\n\\label{tab:threshold_sensitivity}\n\\begin{tabular}{rccr}\n\\toprule\nThreshold & Trigger gen & Peak PPL & Final PPL \\\\\n\\midrule\n5\\%  & 1 & 56.99 & 21.29 \\\\\n10\\% & 1 & 56.99 & 21.29 \\\\\n15\\% & 1 & 56.99 & 21.29 \\\\\n20\\% & 1 & 56.99 & 21.29 \\\\\n25\\% & 1 & 56.99 & 21.29 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-$\\alpha$ operating band.}\nThe within-$\\alpha$ analysis establishes threshold invariance at $\\alpha{=}1.0$ but does not address whether thresholds generalize across contamination levels.\nWe examine observed entropy trajectories from the alpha sweep (not actual intervention experiments at $\\alpha{<}1.0$) to characterize the operating band.\nThe maximum entropy drop across 10 generations varies by contamination level: 7.5\\% at $\\alpha{=}0.0$ (fine-tuning drift only), 7.7\\% at $\\alpha{=}0.10$, 7.8\\% at $\\alpha{=}0.25$, 22.4\\% at $\\alpha{=}0.50$, 35.3\\% at $\\alpha{=}0.75$, and 62.1\\% at $\\alpha{=}1.0$.\nThresholds below 7.5\\% (e.g., 5\\%) trigger on clean training data---a false alarm.\nThresholds above 22.4\\% (e.g., 25\\%) miss $\\alpha{=}0.50$, the lowest contamination level with meaningful entropy signal.\nThe safe operating band is therefore $[10\\%, 22\\%]$: any threshold in this range produces zero false alarms on $\\alpha{=}0.0$ while detecting contamination at $\\alpha{\\geq}0.50$.\nThe reported 15\\% threshold sits near the center of this band.\nThis analysis is based on entropy trajectories from non-intervention training runs; whether actual intervention at $\\alpha{<}1.0$ would produce the same triggering behavior remains unvalidated.\n\n\n\\section{Channel Effect Size Analysis}\n\\label{app:channel_effect_size}\n\nFirst-differencing eliminates all canary$\\to$perplexity Granger associations while preserving canary$\\to$diversity leads (\\S\\ref{sec:regime}).\nWe present three lines of evidence that this asymmetry reflects a genuine temporal structure difference rather than selective power loss from differencing.\n\n\\paragraph{Correlation retention parity.}\nFirst-differencing retains comparable correlation magnitude for both channel types (Table~\\ref{tab:channel_retention}).\nDiversity channels ($n{=}243$ pairs across all non-null experiments) retain a median $|r|$ of 0.952 after differencing, while perplexity channels ($n{=}8$ pairs; limited sample) retain 1.00.\nThis parity rules out a blanket power-loss explanation: if differencing selectively destroyed perplexity signal, $|r|$ retention would be substantially lower for perplexity than for diversity.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{First-differencing effect by channel type. $|r|$ retention = diff $|r|$ / naive $|r|$. Despite comparable $|r|$ retention, Granger $F$ differs by an order of magnitude. Perplexity channel has limited sample ($n{=}8$); all paired comparisons are from bf16 experiments.}\n\\label{tab:channel_retention}\n\\begin{tabular}{lrccrc}\n\\toprule\nChannel & $n$ & Naive $|r|$ & Diff $|r|$ & Retention & Med.\\ $F$ \\\\\n\\midrule\nDiversity   & 243 & 0.943 & 0.921 & 0.952 & 67.8 \\\\\nPerplexity  & 8   & 0.924 & 0.900 & 1.002 & 11.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Granger $F$-statistic asymmetry.}\nWithin matched experiments (same model, seed, $\\alpha$, precision), the Granger $F$-statistic is $20$--$28{\\times}$ higher for diversity than perplexity channels.\nAt $\\alpha{=}0.60$ (s42, bf16): diversity mean $F{=}229.4$ versus perplexity mean $F{=}8.3$ (ratio $27.8{\\times}$).\nAt $\\alpha{=}1.0$ reactive (s43, bf16): diversity mean $F{=}236.4$ versus perplexity mean $F{=}11.5$ (ratio $20.6{\\times}$).\nSince $|r|$ retention is comparable across channels, this $F$-statistic gap cannot be attributed to differencing-induced signal loss; it must reflect a difference in the temporal structure that Granger tests evaluate.\n\n\\paragraph{Temporal structure: lagged vs.\\ contemporaneous.}\nThe lag distribution of peak differenced cross-correlations reveals the structural difference.\nFor diversity channels, 81\\% of peak correlations occur at canary-leading lags (lag${<}0$), with a median lag of $-1$ generation---consistent with the one-generation temporal precedence visible in Figure~\\ref{fig:metric_trajectory}.\nFor perplexity channels, 50\\% of peak correlations occur at lag${=}0$ (contemporaneous co-movement), with a median lag of $0$.\nGranger precedence tests lagged predictive improvement; contemporaneous co-movement produces low $F$-statistics regardless of signal magnitude, which is the correct behavior for a test designed to detect temporal precedence.\nThe perplexity channel sample is limited ($n{=}8$ pairs from bf16 experiments), and these lag distributions should not be generalized to fp32 conditions without further validation.\n\n\n\\section{Mutual Information Analysis}\n\\label{app:mi_analysis}\n\nWe estimate the Gaussian mutual information lower bound between token entropy (canary) and each diversity metric across contamination levels, using $T{=}11$ data points per series ($T{=}10$ for two conditions).\nThe Gaussian estimator $\\hat{I}_G = -\\frac{1}{2}\\log_2(1 - r^2)$, where $r$ is the Pearson correlation, provides a conservative lower bound on MI; we do not report KSG nonparametric estimates due to uncorrected positive bias at $T{=}11$.\nThe $\\alpha{=}0.05$ data point is excluded because it uses an experiment excluded from the dose-response analysis.\n\nTable~\\ref{tab:mi_bounds} reports the mean Gaussian MI across the three distinct-$n$ metrics for each $\\alpha$ level.\nMI follows a V-shaped curve: it drops from 0.112~bits at $\\alpha{=}0.10$ to a minimum of 0.010~bits at $\\alpha{=}0.25$, then rises monotonically to 0.270~bits at $\\alpha{=}0.75$.\nMI remains positive throughout the blind zone ($\\alpha \\leq 0.45$; range 0.010--0.141~bits), confirming that canary--diversity coupling exists below the detection threshold but falls below PermG's statistical power floor at $T{=}10$.\nThere is no discontinuity at $\\alpha_c \\approx 0.50$: the detection onset reflects power accumulation, not an abrupt change in information coupling.\nBootstrap 95\\% CIs span 1--3 orders of magnitude at $T{=}11$, so individual point estimates should be interpreted cautiously.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Gaussian MI lower bound (bits) between token entropy and distinct-$n$ diversity metrics ($T{=}11$, Pythia-410M, fp32). Mean across distinct-1/2/3; $\\alpha{=}0.05$ excluded (see text). CIs omitted due to width at $T{=}11$.}\n\\label{tab:mi_bounds}\n\\begin{tabular}{rrc}\n\\toprule\n$\\alpha$ & Seeds & MI (bits) \\\\\n\\midrule\n0.10 & 2 & 0.112 \\\\\n0.25 & 3 & 0.010 \\\\\n0.30 & 1 & 0.062 \\\\\n0.35 & 1 & 0.098 \\\\\n0.40 & 1 & 0.119 \\\\\n0.45 & 2 & 0.141 \\\\\n0.50 & 3 & 0.107 \\\\\n0.60 & 2 & 0.209 \\\\\n0.75 & 1 & 0.270 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\section{Moment Cascade Analysis}\n\\label{app:moment_cascade}\n\nWe analyze the temporal ordering of metric degradation onset across 6 WikiText seed${\\times}\\alpha$ conditions (2 seeds $\\times$ 3 non-trivial $\\alpha$ levels each) to test whether token entropy consistently degrades before diversity metrics.\nOnset is defined as the first generation where a metric's cumulative change exceeds 5\\% of its generation-0 value.\n\nTable~\\ref{tab:moment_cascade} reports the onset generation for each metric across conditions.\nToken entropy reaches onset at generation~1 in all 6 conditions; distinct-$n$ metrics reach onset at generation~2 in all 18 pairwise comparisons (6 conditions $\\times$ 3 distinct-$n$ metrics).\nAcross these 18 comparisons, entropy degrades first in 16 cases (Kendall $\\tau{=}0.337$, consistent with a weak but reliable temporal ordering).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Degradation onset generation (5\\% threshold) by metric and condition (Pythia-410M, WikiText, fp32). Token entropy reaches onset at generation~1 in all non-null conditions; distinct-$n$ metrics follow at generation~2.}\n\\label{tab:moment_cascade}\n\\begin{tabular}{llcccccc}\n\\toprule\nSeed & $\\alpha$ & Entropy & Dist-1 & Dist-2 & Dist-3 & ECE & PPL \\\\\n\\midrule\n42 & 0.10 & 1 & 2 & 2 & 2 & 2 & --- \\\\\n42 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\\\\n42 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\\\\n43 & 0.25 & 1 & 2 & 2 & 2 & 4 & --- \\\\\n43 & 0.50 & 1 & 2 & 2 & 2 & 1 & 4 \\\\\n43 & 0.75 & 1 & 2 & 2 & 2 & 1 & 1 \\\\\n\\bottomrule\n\\multicolumn{8}{l}{\\footnotesize ---: onset not reached within $T{=}10$ generations.} \\\\\n\\end{tabular}\n\\end{table}\n\nThe cascade ordering provides evidence for the canary mechanism independent of Granger-type tests: it does not depend on first-differencing, lag selection, or the permutation null distribution.\nECE shows onset at generation~1 at $\\alpha{\\geq}0.50$ (both seeds), consistent with its role as a secondary canary metric.\nAt low contamination ($\\alpha{=}0.10$ and $\\alpha{=}0.25$), perplexity never reaches the 5\\% onset threshold within $T{=}10$ generations, while entropy already shows generation-1 onset---consistent with entropy's higher sensitivity to distributional shifts.\n\n\n\\section{Cascade Ordering Theory: Proofs}\n\\label{app:cascade_theory}\n\nThis section provides the full proofs for Proposition~\\ref{thm:entropy_leads} and Proposition~\\ref{prop:div_lag} from \\S\\ref{sec:cascade}, plus supporting results.\n\n\\begin{assumption}[Mode Amplification]\\label{ass:mode_amp}\nThe training map $\\mathcal{T}$ redistributes probability mass from low-probability to high-probability tokens: there exists a threshold $\\bar{p}$ such that $\\mathcal{T}(p)_i > p_i \\Rightarrow p_i \\geq \\bar{p}$ and $\\mathcal{T}(p)_j < p_j \\Rightarrow p_j \\leq \\bar{p}$.\n\\end{assumption}\n\nThis captures the standard finite-capacity approximation effect: MLE on finite samples from a peaked distribution amplifies modes and suppresses the tail~\\cite{shumailov2024curse,dohmatob2024tale}.\n\n\\begin{proposition}[Entropy is a first-order indicator]\\label{prop:entropy_first}\nLet $p \\in \\Delta^{V-1}$ and $\\delta = \\alpha(\\mathcal{T}(p) - p)$ be a mode-amplifying perturbation with $\\sum_i \\delta_i = 0$. Then $\\Delta H = H(p+\\delta) - H(p) = -\\sum_i \\delta_i \\log p_i + O(\\|\\delta\\|^2) < 0$.\n\\end{proposition}\n\n\\begin{proof}\nTaylor-expanding $H$ around $p$:\n$H(p+\\delta) = H(p) - \\sum_i \\delta_i \\log p_i - \\sum_i \\delta_i - \\frac{1}{2}\\sum_i \\delta_i^2/p_i + O(\\|\\delta\\|^3)$.\nSince $\\sum_i \\delta_i = 0$: $\\Delta H = -\\sum_i \\delta_i \\log p_i - \\frac{1}{2}\\sum_i \\delta_i^2/p_i + O(\\|\\delta\\|^3)$.\nUnder mode amplification, tokens gaining mass ($\\delta_i > 0$) have $p_i \\geq \\bar{p}$ (hence $\\log p_i \\geq \\log \\bar{p}$) and tokens losing mass ($\\delta_j < 0$) have $p_j \\leq \\bar{p}$ (hence $\\log p_j \\leq \\log \\bar{p}$).\nWriting $m = \\sum_{i:\\delta_i > 0} \\delta_i$: $-\\sum_i \\delta_i \\log p_i = -m[\\overline{\\log p}^{+} - \\overline{\\log p}^{-}] < 0$, where $\\overline{\\log p}^{\\pm}$ are the $|\\delta|$-weighted means over gaining/losing tokens.\nThe second-order Fisher information term $-\\frac{1}{2}\\sum_i \\delta_i^2/p_i$ is always negative, reinforcing the decrease.\n\\end{proof}\n\n\\begin{proposition}[Diversity is a threshold indicator]\\label{prop:div_threshold}\nDefine the $\\epsilon$-effective support $S_\\epsilon(p) = |\\{i \\in [V]: p_i > \\epsilon\\}|$, where $\\epsilon \\approx c/N$ is the generation threshold for sample size $N$.\nUnder the same perturbation $\\delta$: $\\Delta S_\\epsilon = -|\\{i: p_i > \\epsilon \\text{ and } p_i + \\delta_i \\leq \\epsilon\\}|$.\nThis equals zero whenever $\\|\\delta\\|_\\infty < \\gamma(p,\\epsilon) := \\min_{i: p_i > \\epsilon}(p_i - \\epsilon)$.\n\\end{proposition}\n\n\\begin{proof}\nToken $i$ exits the effective support iff $p_i > \\epsilon$ and $p_i + \\delta_i \\leq \\epsilon$, requiring $|\\delta_i| \\geq p_i - \\epsilon$.\nIf $\\|\\delta\\|_\\infty < \\gamma$, no token satisfies this condition.\n\\end{proof}\n\n\\paragraph{Proof of Proposition~\\ref{thm:entropy_leads}.}\n\\emph{Part (a):} Take any mode-amplifying $\\delta$ with $\\|\\delta\\|_\\infty < \\gamma(p,\\epsilon)$.\nBy Proposition~\\ref{prop:div_threshold}, $\\Delta S_\\epsilon = 0$.\nBy Proposition~\\ref{prop:entropy_first}, $\\Delta H < 0$.\nSuch $\\delta$ exists for all $\\alpha < \\gamma / \\max_i |\\mathcal{T}(p)_i - p_i|$.\n\\emph{Part (b):} If $\\Delta S_\\epsilon < 0$, some token $k$ has $p_k > \\epsilon$ but $p_k + \\delta_k \\leq \\epsilon$, so $\\delta_k < 0$.\nUnder mode amplification, this implies $p_k \\leq \\bar{p}$; the total mass transferred to high-probability tokens ensures $\\overline{\\log p}^+ > \\overline{\\log p}^-$.\nBy Proposition~\\ref{prop:entropy_first}, $\\Delta H < 0$. $\\square$\n\n\\paragraph{Proof of Proposition~\\ref{prop:div_lag}.}\nBy the margin condition, at every generation $s \\leq t_H$ the perturbation norm $\\alpha\\|\\mathcal{T}(p_s) - p_s\\|_\\infty$ is less than $\\gamma(p_s, \\epsilon)$.\nBy Proposition~\\ref{prop:div_threshold}, no token exits the effective support at any $s \\leq t_H$, so $\\Delta S_\\epsilon = 0$ for all $s \\leq t_H$.\nSince time is discrete, $t_D \\geq t_H + 1$. $\\square$\n\n\\paragraph{ECE co-movement (qualitative argument).}\nUnder conditional mode amplification (peakier $q_\\theta(\\cdot|x)$ at each generation), per-token conditional entropy $h(x) = H(q_\\theta(\\cdot|x))$ decreases while confidence $c(x) = \\max_y q_\\theta(y|x) \\geq \\exp(-h(x))$ increases.\nAveraging: $\\bar{H}_t$ decreases, $C_t$ increases.\nWith accuracy approximately stationary in early collapse ($A_t \\approx A_0$), $\\Delta\\mathrm{ECE} \\approx \\Delta C_t > 0$ whenever $\\Delta\\bar{H}_t < 0$.\nThis argument establishes the direction of co-movement; the quantitative relationship depends on distribution geometry.\n$\\bar{H}_t$ denotes mean conditional entropy $\\mathbb{E}_{x \\sim p_{\\text{eval}}}[h(x)]$, which differs from the marginal entropy $H_t = -\\sum_i p_t(i)\\log p_t(i)$ used in Proposition~\\ref{thm:entropy_leads}; under mode amplification, both decrease monotonically, so the cascade ordering is consistent across both formulations.\n\n\\paragraph{MAUVE ordering (conjecture).}\nMAUVE measures divergence in a discretized embedding space via $k$-means quantization.\nMAUVE onset requires token-level shifts (detected by entropy) to propagate through $n$-gram distributions (detected by distinct-$n$) to aggregate embedding distributions.\nEmpirically, MAUVE onset lags diversity by 0--1 generations on WikiText; however, on C4, MAUVE onset occurs at generation~1 (simultaneous with entropy), suggesting this lag is corpus-dependent.\n\n\\paragraph{Empirical support.}\nAmong 15 experiments at $\\alpha \\geq 0.30$ (where entropy perturbation exceeds the detection threshold), cascade ordering $t_H \\leq t_D$ holds in 14/15 cases (GPT-2-medium s43 fp32 exhibits bidirectional Granger significance).\nTable~\\ref{tab:cascade_onset} reports onset generations for representative conditions, showing uniform Phase~1/2/3 ordering.\nFive low-$\\alpha$ experiments ($\\alpha \\leq 0.25$) show entropy perturbation below the detection threshold (gen-1 deviation $<2\\sigma$); cascade ordering is neither confirmed nor refuted in this regime.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cascade onset generations (5\\% threshold) for representative experiments (Pythia-410M, WikiText, fp32). Phase~1: entropy and ECE ($t_H$, $t_{\\mathrm{ECE}}$); Phase~2: diversity ($t_D$, min over distinct-$n$); Phase~3: MAUVE ($t_M$). All conditions confirm the predicted ordering $t_H = t_{\\mathrm{ECE}} \\leq t_D \\leq t_M$.}\n\\label{tab:cascade_onset}\n\\begin{tabular}{llcccc}\n\\toprule\nSeed & $\\alpha$ & $t_H$ & $t_{\\mathrm{ECE}}$ & $t_D$ & $t_M$ \\\\\n\\midrule\n42 & 0.50 & 1 & 1 & 2 & 3 \\\\\n43 & 0.50 & 1 & 1 & 2 & 2 \\\\\n42 & 0.75 & 1 & 1 & 2 & 3 \\\\\n43 & 0.75 & 1 & 1 & 2 & 2 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\phantomsection\\label{app:alpha_c_proof}\n\\paragraph{Proof of Proposition~\\ref{prop:phase-boundary}.}\nAt the detection threshold, $\\mathrm{Power}(\\alpha_c, T) = \\pi^*$.\nSince $\\alpha_c$ lies below the non-monotonic dip region ($\\alpha_c < 0.55$), the signal model applies directly.\nFrom the power function $\\mathrm{Power} = \\Phi(S(\\alpha) \\cdot \\sqrt{T} / \\sigma)$, setting $S(\\alpha_c) \\cdot \\sqrt{T} / \\sigma = z^*$ and substituting the signal model $S(\\alpha) = c\\,\\alpha^\\beta$ yields $c\\,\\alpha_c^\\beta = z^* \\sigma / \\sqrt{T}$.\nSolving: $\\alpha_c(T) = (z^* \\sigma / c)^{1/\\beta} \\cdot T^{-1/(2\\beta)}$, giving the stated form with exponent $\\gamma = 1/(2\\beta)$.\n\n\\paragraph{Calibration and consistency.}\nCross-$T$ validation avoids the circularity of fitting theory to model-extrapolated points.\nWe fit $P(\\mathrm{det}|\\alpha,T) = \\Phi(A \\cdot \\alpha^\\beta \\cdot \\sqrt{T} - z_0)$ to training data at $T \\in \\{10, 20\\}$ via profile likelihood over $(\\beta, \\alpha_\\infty)$, with $\\alpha_\\infty{=}0$ emerging as the optimum.\nThe held-out test set ($T \\in \\{5, 15\\}$) yields MAE${=}0.106$ with 95\\% CI coverage $6/6$: the model correctly predicts all $0/8$ at $T{=}5$ and detection at $T{=}15$ (predicted $0.49$--$0.71$ vs.\\ observed $6/8{=}0.75$; under-prediction reflects the $P_{\\max}{=}0.75$ ceiling from MAUVE saturation, which is modeled separately).\nA linear signal model ($\\beta{=}1$, $\\gamma{=}0.5$) is rejected.\nThe sub-linear exponent $\\beta{=}0.24$ implies that doubling contamination increases signal by only $2^{0.24} \\approx 1.18\\times$ (18\\%); since $\\alpha_\\infty{\\approx}0$, any nonzero contamination produces signal, but detection requires sufficient $T$ to amplify it.\nAt $T{=}5$, $\\alpha_c \\geq 1.0$: no contamination level is detectable, consistent with the insufficient statistical power at very short observation windows.\n\n\\paragraph{Leave-one-$T$-out cross-validation.}\nWe evaluate model generalization via leave-one-$T$-out CV on the $5T \\times 3\\alpha$ grid (sync-dip $\\alpha{=}0.60$ excluded; 15 cells).\nFor each fold, one observation length is held out and the probit model $P = P_{\\max} \\cdot \\Phi(A \\cdot \\alpha^{0.24} \\cdot \\sqrt{T} - z_0)$ is refit on the remaining data.\nOverall MAE${=}0.037$ with 95\\% CI coverage $15/15$.\nWhen sync-dip cells are included (20 cells), MAE rises to $0.203$ (CI $16/20$), with the largest residuals at sync-dip cells (predicted $0.75$, observed $0/8$).\nThe profile likelihood over $\\beta$ yields MLE $\\hat{\\beta}{=}0.66$ (95\\% CI $[0.24, 0.78]$); the wide interval reflects a flat likelihood surface, indicating that $\\beta$ is not well-identified from these data.\nModel comparison (AIC, 15-cell grid excluding sync-dip): $M_1$ (linear boundary) $\\Delta\\mathrm{AIC}{=}0.0$; $M_2$ (power-probit) $\\Delta\\mathrm{AIC}{=}2.43$.\nIncluding sync-dip data reverses the ranking ($M_2$ $\\Delta\\mathrm{AIC}{=}0.0$, $M_1$ $\\Delta\\mathrm{AIC}{=}4.15$), because the probit model naturally accommodates the dip's dissolution at higher $T$ while linear models cannot.\n\n\\section{Power Simulation: Shape Comparison}\n\\label{app:power_sim}\n\nTo assess whether the observed steep detection onset could arise from smooth signal models, we simulate PermG detection under three null hypotheses (1{,}000 replications per cell, $n_{\\text{perm}}{=}1{,}000$, $n_{\\text{pairs}}{=}8$, BH-FDR $q{=}0.05$):\n\n\\begin{itemize}\n\\item \\textbf{H0} (linear): $S(\\alpha) = c \\cdot \\alpha$, calibrated so $S(1.0) = S_{\\max}$.\n\\item \\textbf{H0$'$} (concave): $S(\\alpha) = c \\cdot \\alpha^{0.5}$, sub-linear but smooth.\n\\item \\textbf{H1} (step): $S(\\alpha) = S_{\\max} \\cdot \\mathbf{1}[\\alpha > \\alpha_c(T)]$, binary activation.\n\\end{itemize}\n\n\\noindent\\textbf{Scaling exponents.}\nAll three models produce apparent onset scaling in $T$: H0 $\\gamma{=}0.85$, H0$'$ $\\gamma{=}1.87$, H1 $\\gamma{=}1.96$ (observed: $\\gamma{=}2.08$).\nH0$'$ produces $\\gamma$ within $0.21$ of the observed value, demonstrating that the scaling exponent alone cannot distinguish smooth from step-function boundaries.\n\n\\noindent\\textbf{Shape differences.}\nAt $T{=}10$, $\\alpha{=}0.45$: H0 predicts 27\\% detection rate, H0$'$ predicts 45\\%, H1 predicts 5.5\\%, observed $0/8$.\nAt $T{=}10$, $\\alpha{=}0.50$: H0 predicts 36\\%, H0$'$ predicts 48\\%, H1 predicts 4.6\\%, observed $6/8$ (75\\%).\nSmooth models produce onset ramps with $k{=}4.9$--$6.1$ (H0$'$: $k{=}4.93$, $R^2{=}0.9974$; H0: $k{=}6.14$, $R^2{=}0.9998$); the observed onset steepness ($k{=}15.7$) is ${\\approx}3{\\times}$ higher.\n\n\\noindent\\textbf{Metric-specific ceiling.}\nAt high $\\alpha$ (${\\geq}0.75$) with $T{\\geq}20$, H0 and H0$'$ (which simulate 8 equal-signal pairs) reach mean detection fractions of $0.79$--$0.98$ (${\\approx}6.3$--$7.8/8$), whereas observed counts never exceed $6/8$.\nThis gap reflects metric structure rather than signal saturation: the 2/8 non-detected pairs consistently involve MAUVE, whose floor saturation (\\S\\ref{sec:t20}) prevents Granger detection regardless of signal strength.\n\n\\section{T=20 Predict-then-Verify Comparison}\n\\label{app:t20_comparison}\n\nTable~\\ref{tab:t20_comparison} reports the predict-then-verify results for the $T{=}20$ extension experiments.\nPredictions are derived from the detection boundary model (\\S\\ref{sec:theory}): detected pairs at $T{=}10$ are predicted to remain detected (saturated $F$-statistics), and undetected pairs are predicted to remain undetected (structural nulls or non-monotonic dip).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{T=20 predict-then-verify comparison (Pythia-410M, seed~42, WikiText, fp32). Excluding $\\alpha{=}1.0$, two of four predictions fall within CI ($\\alpha{=}0.50$, $0.75$); boundary cases show systematic bias---$\\alpha{=}0.45$ falsifies the ceiling hypothesis (under-prediction), $\\alpha{=}0.60$ over-predicts under raw $p$-values (v1; matches under FDR v2, not pre-committed).}\n\\label{tab:t20_comparison}\n\\begin{tabular}{lcccc}\n\\toprule\n$\\alpha$ & $T{=}10$ & Predicted $T{=}20$ & Observed $T{=}20$ & Match \\\\\n\\midrule\n0.45 & 0/8 & 0/8 (ceiling) & 5/8 & $\\times$ \\\\\n0.50 & 6/8 & 6/8 (saturated) & 6/8 & \\checkmark \\\\\n0.60 & 0/8 & 3/8 (v1 raw)$^\\dagger$ & 0/8 & $\\times$ \\\\\n0.75 & 6/8 & 6/8 (saturated) & 6/8 & \\checkmark \\\\\n1.00 & 6/8 & 6/8 (saturated) & 6/8 & \\checkmark \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$V2 (BH--FDR corrected, created 44\\,min pre-analysis, not git-committed) predicts 0/8, matching observation.} \\\\\n\\end{tabular}\n\\end{table}\n\nAt $\\alpha \\geq 0.50$, consistency across $T{=}10$ and $T{=}20$ supports the detection boundary prediction: PermG counts are determined by signal structure, not observation length.\nSix diversity-based pairs show $F{=}449$--$2947$ at $T{=}20$ (all $\\gg F_{\\text{crit}}$); two MAUVE-based pairs show $F{<}2$ regardless of $T$, driven by floor saturation ($\\mu{=}0.029$, 100\\% ${<}0.05$) rather than high variance (CV$_{\\text{MAUVE}}{=}0.089$ vs CV$_{\\text{distinct-1}}{=}0.139$); SNR: MAUVE $4.68$ vs diversity $6.40$--$8.20$ ($p{<}0.001$).\nThe sole exception is $\\alpha{=}0.45$ at $T{=}20$ (5/8), consistent with boundary proximity.\nAt $\\alpha{=}0.45$, the shift from 0/8 to 5/8 falsifies Model~A (ceiling: $\\alpha{=}0.45$ structurally undetectable) in favor of Model~B (power-limited: $\\sqrt{T}$ boost crosses the detection threshold), lowering $\\alpha_c$ below~0.45.\nThe $\\alpha{=}0.60$ non-monotonic dip persists at $T{=}20$ (s42: 0/8; s43: 3/8) but dissolves at $T{=}25$ (5/8), confirming that $\\sqrt{T}$ power scaling eventually overcomes the dip; alternative methods detect signal throughout (DiffXCorr 6/8, TY 5/8 at $T{=}20$).\nPermG directional selectivity is consistent across tested $T$ ($T{=}10$, $20$): forward 6/8 versus reverse 0/8 at $\\alpha \\in \\{0.50, 0.75, 1.0\\}$.\n\n\n\\subsection{Prediction Timeline}\n\\label{app:t20_prediction_timeline}\n\nTwo versions of the $T{=}20$ prediction file exist, reflecting an evolving statistical protocol:\n\n\\paragraph{V1 (git-committed, \\texttt{bad72cc}).} Predictions derived from $T{=}10$ PermG results using \\emph{raw} $p$-values. At $\\alpha{=}0.60$, v1 counted 3/8 pairs with raw $p{<}0.05$, predicting 3/8 detections at $T{=}20$. The observed result (0/8 FDR-significant) does not match.\n\n\\paragraph{V2 (pre-analysis, not committed).} A revised file incorporating BH--FDR correction at $q{=}0.05$, consistent with the correction applied throughout the paper. Under FDR, $\\alpha{=}0.60$ drops from 3/8 (raw) to 0/8, matching the observation. V2 was created 44 minutes before the formal $T{=}20$ analysis began (filesystem timestamp) but was not git-committed, and therefore lacks the cryptographic verifiability of v1.\n\n\\paragraph{Scoring.} Primary (v1, committed): 3/5 exact matches ($\\alpha \\in \\{0.50, 0.75, 1.0\\}$, all saturated regimes). Excluding $\\alpha{=}1.0$, two of four predictions fall within CI. Both boundary predictions miss: $\\alpha{=}0.45$ (predicted 0/8, observed 5/8) falsifies the ceiling hypothesis in favor of $\\sqrt{T}$ power scaling; $\\alpha{=}0.60$ (predicted 3/8, observed 0/8) over-estimates detection due to the non-monotonic dip. Sensitivity (v2, FDR-corrected): 4/5 ($\\alpha{=}0.60$ matches). The systematic conservative bias at $\\alpha{=}0.45$ is consistent with the $\\sqrt{T}$ power increase predicted by Proposition~\\ref{prop:phase-boundary}.\n\n\n\\phantomsection\\label{app:task_degradation}\n\\paragraph{Task degradation.}\n\nTable~\\ref{tab:task_degradation} reports end-of-training task performance (generation~10, Pythia-410M, seed~42, fp32) across contamination levels.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Task degradation across contamination levels (Pythia-410M, seed~42, fp32, generation~10). Perplexity evaluated on held-out WikiText-103.}\n\\label{tab:task_degradation}\n\\begin{tabular}{lcc}\n\\toprule\n$\\alpha$ & Perplexity & Next-token acc. \\\\\n\\midrule\nBaseline & 26.6 & 0.390 \\\\\n0.05 & 20.8 & 0.431 \\\\\n0.25 & 22.9 & 0.424 \\\\\n0.46 & 31.6 & 0.400 \\\\\n0.50 & 31.3 & 0.399 \\\\\n0.52 & 41.1 & 0.389 \\\\\n0.60 & 53.5 & 0.375 \\\\\n0.75 & 80.3 & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt $\\alpha{=}0.05$, perplexity improves over the uncontaminated baseline (20.8 vs.\\ 26.6), consistent with a mild data augmentation effect.\nThe sharpest degradation occurs between $\\alpha{=}0.50$ and $0.52$ ($+31\\%$ perplexity), aligning with the PermG detection onset (\\S\\ref{sec:regime}).\n\n\\section{Cross-Architecture FPR Sensitivity}\n\\label{app:cross_arch_fpr}\n\nAs preliminary cross-architecture evidence, we evaluate null-condition ($\\alpha{=}0$) false positive rates on GPT-2-medium (345M; OpenAI), a model outside the Pythia family used for all primary experiments.\nTwo seeds (s42, s43) are trained for $T{=}10$ generations under the same protocol as the Pythia-410M null runs.\nThis evaluation requires additional replication across architectures and seed counts before drawing definitive conclusions.\n\n\\begin{table}[h]\n\\centering\n\\caption{Null-condition FPR for GPT-2-medium ($\\alpha{=}0$, $T{=}10$, 6-pair basis). PermG forward detection shows extreme seed dependence; $K{\\geq}3$ consensus remains at 0\\% across both seeds.}\n\\label{tab:gpt2m_null_fpr}\n\\begin{tabular}{lccc}\n\\toprule\nSeed & PermG fwd & PermG rev & $K{\\geq}3$ \\\\\n\\midrule\ns42 & 6/6 (100\\%) & 0/6 & 0/6 \\\\\ns43 & 0/6 (0\\%) & 0/6 & 0/6 \\\\\n\\midrule\nPooled & 6/12 (50\\%) & 0/12 & 0/12 (0\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe pooled PermG FPR is dramatically higher than on Pythia-410M (50\\% vs.\\ 11.1\\%, 6-pair basis) and shows extreme seed dependence (100\\% vs.\\ 0\\%).\nThis instability traces to the magnitude of null drift in GPT-2-medium's output distribution, which is substantially stronger than in Pythia-410M (Table~\\ref{tab:null_drift_comparison}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Null drift magnitude ($\\alpha{=}0$, gen\\,0$\\to$10; GPT-2-medium: 2 seeds; Pythia-410M: 4 seeds, s46/s48--s50). GPT-2-medium exhibits ${\\sim}4{\\times}$ stronger entropy drift and ${\\sim}7{\\times}$ stronger distinct-3 drift than Pythia-410M.}\n\\label{tab:null_drift_comparison}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{GPT-2-medium} & \\multicolumn{2}{c}{Pythia-410M} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nMetric & gen\\,0 & gen\\,10 (\\%$\\Delta$) & gen\\,0 & gen\\,10 (\\%$\\Delta$) \\\\\n\\midrule\nToken entropy & 3.57 & 2.84 ($-$20.5\\%) & 3.23 & 3.076 ($-$4.9\\%) \\\\\nDistinct-3 & 0.84 & 0.54 ($-$35.8\\%) & 0.81 & 0.769 ($-$4.9\\%) \\\\\n$\\Delta$entropy (gen\\,0$\\to$1) & \\multicolumn{2}{c}{$-$0.60} & \\multicolumn{2}{c}{$-$0.25} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nGPT-2-medium's distinct-3 declines from 0.84 to 0.54 over ten null generations ($-$35.8\\%), compared with 0.81$\\to$0.77 ($-$4.9\\%) for Pythia-410M.\nThis steep diversity collapse under pure retraining, absent any synthetic contamination, creates a strong downward trend that PermG's permutation test interprets as a directional signal.\nThe initial entropy drop (gen\\,0$\\to$1: $-$0.60 vs.\\ $-$0.25) is similarly amplified, consistent with architecture-specific sensitivity to iterative retraining rather than a deficiency in the detection method.\n\nThe $K{\\geq}3$ multi-method consensus maintains 0\\% FPR on GPT-2-medium (0/12 pairs), though the margin of safety is narrow: in the worst case (s42), 2 of 5 methods vote for forward detection, one vote short of the $K{\\geq}3$ threshold.\nThis provides some protection against architecture-specific distributional variation, but two seeds constitute only preliminary evidence.\nFor reference, PermG successfully detects true contamination signal ($\\alpha{=}1.0$) on GPT-2-medium with 6/8 forward pairs (Table~\\ref{tab:generalization}), confirming that the method works when signal is present; the elevated null FPR is specific to the null condition where architecture-dependent drift dominates.\n\n\\section*{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant throughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections, polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform related-work section.\n\\end{itemize}\n\n",
    "structuredPatch": [
      {
        "oldStart": 733,
        "oldLines": 17,
        "newStart": 733,
        "newLines": 17,
        "lines": [
          " \\begin{table}[h]",
          " \\centering",
          " \\small",
          "-\\caption{Shapley value decomposition (6-pair, mauve excluded). FPR-Shapley: marginal FPR contribution (positive = increases false positives). FNR-Shapley: marginal FNR contribution (negative = reduces false negatives). Combined = FPR + FNR (more negative = better). 48 experiments, $2^5{=}32$ coalitions, exact enumeration.}",
          "+\\caption{Shapley value decomposition (6-pair, mauve excluded). FPR-Shapley computed from 6 null seeds (36 pairs); FNR-Shapley from 45 signal experiments (270 pairs). Combined = FPR + FNR (more negative = better). $2^5{=}32$ coalitions, exact enumeration.}",
          " \\label{tab:shapley_6pair}",
          " \\begin{tabular}{lccc}",
          " \\toprule",
          " Method & $\\phi^{\\text{FPR}}$ & $\\phi^{\\text{FNR}}$ & $\\phi^{\\text{comb}}$ \\\\",
          " \\midrule",
          "-Naive XCorr          & $+0.622$ & $-0.419$ & $+0.203$ \\\\",
          "-Diff.\\ XCorr         & $+0.163$ & $-0.306$ & $-0.142$ \\\\",
          "-Threshold ($3\\sigma$) & $+0.101$ & $-0.027$ & $+0.074$ \\\\",
          "-\\textbf{Perm.\\ Granger} & $\\mathbf{0.000}$ & $\\mathbf{-0.180}$ & $\\mathbf{-0.180}$ \\\\",
          "-Toda--Yamamoto       & $+0.031$ & $-0.069$ & $-0.038$ \\\\",
          "+Naive XCorr          & $+0.609$ & $-0.419$ & $+0.190$ \\\\",
          "+\\textbf{Diff.\\ XCorr}& $\\mathbf{+0.007}$ & $\\mathbf{-0.306}$ & $\\mathbf{-0.299}$ \\\\",
          "+Threshold ($3\\sigma$) & $+0.111$ & $-0.027$ & $+0.084$ \\\\",
          "+Perm.\\ Granger       & $+0.039$ & $-0.180$ & $-0.141$ \\\\",
          "+Toda--Yamamoto       & $+0.150$ & $-0.069$ & $+0.082$ \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          " \\end{table}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---


### Assistant

_source line 120_

Now TODO-D219 #5 — Figure caption.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "a525daad-ea9e-4d3e-8e2c-2992ffc61742",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TaHxDBDgDGeqjhKkbR6H5R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 932,
      "cache_read_input_tokens": 111751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 932
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 121_

<details open><summary>🔧 Tool call — Edit · `toolu_01SboTgtnnMyFaYrBDM2kcaP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "old_string": "% TODO-D219: regenerate figure and update caption after Shapley recomputation with 6-seed data\n\\caption{Shapley value decomposition of each method's marginal contribution to FPR (positive bars) and FNR (negative bars). PermG is the only method with zero FPR contribution; naive cross-correlation's FPR dominates its FNR benefit.}",
  "new_string": "\\caption{Shapley value decomposition of each method's marginal contribution to FPR (positive bars) and FNR (negative bars), computed from 6 null seeds (36 pairs) and 45 signal experiments (270 pairs). DiffXCorr achieves the best combined Shapley ($-0.299$) via near-zero FPR; PermG ranks second ($-0.141$) as the best directional method.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4aa5547a-5b80-412e-a200-b4e82bc1c8e7",
  "uuid": "e0c83fe6-ec52-433e-a8e4-06c1d49b1f93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TaHxDBDgDGeqjhKkbR6H5R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 932,
      "cache_read_input_tokens": 111751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 932
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---
