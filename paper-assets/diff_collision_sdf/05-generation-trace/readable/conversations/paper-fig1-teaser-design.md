# paper fig1 teaser design

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 0
- **Tool calls:** 30
- **Original source:** `logs/chats/worker_paper_fig1_teaser_design_20260527T015636.jsonl`
- **Structured JSON:** [`79c91b39bc84366a3262.json`](../../sessions/79/79c91b39bc84366a3262.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

61 recorded events

### Tool call

_source line 1 · 2026-05-27T02:00:17.667295+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Explore paper structure and figures",
  "subagent_type": "Explore",
  "prompt": "I need to understand the style and structure of existing figures in a CoRL 2026 paper about VLA collision avoidance. The project is at /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/.\n\nPlease find and read:\n1. The introduction.tex file (especially the Figure 1 caption and surrounding context)\n2. Any existing figure generation scripts (matplotlib/tikz) in the artifacts/ directory or elsewhere\n3. The paper's main .tex file to understand figure formatting conventions\n4. Any existing figures (fig2, fig3 mentioned) to understand style consistency\n\nSearch broadly: \"very thorough\". Report back the exact caption text, any figure generation code patterns, color schemes used, and layout conventions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Agent",
  "tool_args": {
    "description": "Explore paper structure and figures",
    "subagent_type": "Explore",
    "prompt": "I need to understand the style and structure of existing figures in a CoRL 2026 paper about VLA collision avoidance. The project is at /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/.\n\nPlease find and read:\n1. The introduction.tex file (especially the Figure 1 caption and surrounding context)\n2. Any existing figure generation scripts (matplotlib/tikz) in the artifacts/ directory or elsewhere\n3. The paper's main .tex file to understand figure formatting conventions\n4. Any existing figures (fig2, fig3 mentioned) to understand style consistency\n\nSearch broadly: \"very thorough\". Report back the exact caption text, any figure generation code patterns, color schemes used, and layout conventions."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-27T02:00:17.667857+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf -type f -name \"*.tex\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf -type f -name \"*.tex\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-27T02:00:17.668148+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/contingency_claim3.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/_archive/conclusion_DEPRECATED.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/_archive/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/_archive/experiments.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/archive/analysis_claim4.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/archive/analysis_claim3.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/archive/analysis_claim1.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/archive/analysis_claim2.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/experimental_framework.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_
…[truncated 160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-27T02:00:17.668383+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-27T02:00:17.668641+00:00_

total 580
drwxr-xr-x 10 ubuntu ubuntu   4096 May 27 01:23 .
drwxrwxr-x  8 ubuntu ubuntu   4096 May 19 16:03 ..
drwxr-xr-x  3 ubuntu ubuntu   4096 May 19 16:03 .claude
drwxr-xr-x  6 ubuntu ubuntu   4096 May 24 21:01 .venv
-rw-r--r--  1 ubuntu ubuntu  13053 May 27 01:56 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu      0 May 19 16:05 ROADMAP.lock
-rw-------  1 ubuntu ubuntu   5130 May 27 00:37 ROADMAP.md
-rw-r--r--  1 ubuntu ubuntu    100 May 24 23:23 _last_visual_review.json
drwxr-xr-x 11 ubuntu ubuntu   4096 May 27 01:55 artifacts
drwxr-xr-x  2 ubuntu ubuntu  65536 May 27 01:22 checkpoints
-rw-r--r--  1 ubuntu ubuntu      0 May 21 17:21 constraints.lock
-rw-------  1 ubuntu ubuntu    636 May 21 17:21 constraints.yaml
-rw-r--r--  1 ubuntu ubuntu      0 May 19 16:08 decisions.lock
-rw-------  1 ubuntu ubuntu  35996 May 27 00:37 decisions.yaml
drwxr-xr-x  4 ubuntu ubuntu   4096 May 19 17:39 docs
-rwxr-xr-x  1 ubuntu ubuntu      0 May 19 17:39 dream_registry.lock
-rw-------  1 ubuntu ubuntu   2258 May 26 03:42 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu   2263 May 26 03:42 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu  31065 May 22 02:54 eval_safelibero.py
-rw-r--r--  1 ubuntu ubuntu      0 May 26 02:36 experiment_plan.lock
-rw-------  1 ubuntu ubuntu   5097 May 26 20:27 experiment_plan.yaml
-rw-r--r--  1 ubuntu ubuntu  17526 May 25 08:32 literature_map.yaml
drwxr-xr-x  4 ubuntu ubuntu   4096 May 19 16:06 logs
-rw-r--r--  1 ubuntu ubuntu   8098 May 26 13:53 memory.md
-rw-r--r--  1 ubuntu ubuntu      0 May 19 18:43 mistakes.lock
-rw-------  1 ubuntu ubuntu  58559 May 26 23:26 mistakes.yaml
drwxr-xr-x  2 ubuntu ubuntu   4096 May 25 08:11 paper
-rw-r--r--  1 ubuntu ubuntu  12545 May 27 01:20 paper_framing.md
-rw-r--r--  1 ubuntu ubuntu      0 May 20 23:06 paper_provenance.lock
-rw-------  1 ubuntu ubuntu  35244 May 27 01:23 paper_provenance.yaml
-rw-r--r--  1 ubuntu ubuntu   8769 May 20 02:15 patch_eval.py
-rw-r--r--  1 ubuntu ubuntu   1850 May 24 21:02 plot_oracle_bar.
…[truncated 441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-27T02:00:17.668892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-27T02:00:17.669106+00:00_

1	\section{Introduction}\label{sec:intro}
2	
3	Vision-Language-Action (VLA) models must avoid collisions to operate safely in physical environments~\cite{li2026vlasafety}. The SafeLIBERO benchmark~\cite{hu2025vlsa} provides the first systematic protocol for measuring collision avoidance in VLA manipulation, and recent methods, including SDF-augmented training~\cite{zhang2025safevla}, constraint-based planning~\cite{yang2025cape}, and collision-free demonstrations~\cite{cofreeevla2026}, report high Collision Avoidance Rate (CAR). Our SDF-augmented Pi0~\cite{black2024pi0} reaches 91.5\% CAR across 800 episodes. The problem appears close to solved.
4	
5	\begin{figure}[t]
6	\centering
7	\includegraphics[width=\linewidth]{fig1_teaser}
8	\caption{The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). CAR$_\text{f}$ filters out action-collapsed episodes where displacement falls below $\tau_d$, revealing that Pi0+A1's 91.5\% safety score drops to ${\approx}$\,0\% (center). Pi0.5 exhibits genuine avoidance with active motion above 288\,mm in all safe episodes, and CAR$_\text{f}$ equals raw CAR (right).}
9	\label{fig:teaser}
10	\end{figure}
11	
12	It is not (Figure~\ref{fig:teaser}). Of the 732 collision-free episodes, 99.6\% exhibit displacement below 0.1\,mm; TSR is 0\% across all 800 episodes. The robot is frozen, not safe. The same pattern holds across all Pi0 configurations (Section~\ref{sec:fake_safety}). We term this \emph{fake safety}: \emph{action collapse} (near-zero actions producing zero collisions) renders reported CAR illusory, and standard evaluation cannot distinguish inaction from deliberate avoidance~\cite{karwowski2024goodhart}.
13	
14	We present a systematic investigation of this problem across the Pi0 and Pi0.5~\cite{black2024pi0} model families on SafeLIBERO, spanning 70+ experiments and 6000+ evaluation episodes. Three findings emerge.
15	
16	\textbf{Fake 
…[truncated 2168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-27T02:00:17.669340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-27T02:00:17.669625+00:00_

1	\documentclass{article}
2	
3	\PassOptionsToPackage{dvipsnames}{xcolor}
4	\usepackage{corl_2026}
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{booktabs}
8	\usepackage{graphicx}
9	\usepackage{multirow}
10	\usepackage{subcaption}
11	\graphicspath{{../../artifacts/figures/}}
12	
13	\newcommand{\placeholder}[1]{\textcolor{red}{\textbf{[#1]}}}
14	
15	\title{Rethinking VLA Safety Evaluation:\\When 98\% of Collision Avoidance is an Illusion}
16	
17	\author{
18	  Anonymous Authors
19	}
20	
21	\begin{document}
22	
23	\maketitle
24	
25	\input{abstract}
26	
27	\keywords{VLA safety, collision avoidance, action collapse, signed distance fields}
28	
29	\input{introduction}
30	
31	\input{related_work}
32	
33	\input{method}
34	
35	\input{claim1}
36	
37	\input{claim2}
38	
39	\input{claim3}
40	
41	\input{discussion}
42	
43	\bibliography{references}
44	
45	\appendix
46	\input{appendix}
47	
48	\end{document}
49	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-27T02:00:17.669845+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts -type f \\( -name \"*.py\" -o -name \"*.tikz\" -o -name \"*.pdf\" -o -name \"*.png\" \\) | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts -type f \\( -name \"*.py\" -o -name \"*.tikz\" -o -name \"*.pdf\" -o -name \"*.png\" \\) | head -30"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-27T02:00:17.670052+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/paper/paper_draft.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/intermediate/reeval_comparison.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/eval_safelibero_openvla.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/chart/fig5_lambda_curve_5f2325.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/chart/fig2_ee_displacement_distribution.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/chart/fig_threshold_sensitivity.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/chart/fig_displacement_hist.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/chart/fig5_lambda_curve.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/chart/fig_threshold_sensitivity_7fcb7e.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/chart/fig_tsr_car_scatter.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/chart/fig3_tsr_car_scatter.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/chart/fig_oracle_bar.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/chart/fig1_teaser.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_threshold_sensitivity.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig3.py
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig1_tease
…[truncated 1668 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-27T02:00:17.670289+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig1_teaser.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig1_teaser.py"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-27T02:00:17.670579+00:00_

1	import matplotlib
2	matplotlib.use('Agg')
3	import matplotlib.pyplot as plt
4	import matplotlib.patheffects as pe
5	import matplotlib.ticker as mticker
6	import numpy as np
7	
8	# ── Colors ──
9	CORAL = '#E8846B'
10	CORAL_DARK = '#C0603E'
11	BLUE = '#0072B2'
12	BLUE_DARK = '#005A8D'
13	RED_TEXT = '#C0392B'
14	GRAY_TEXT = '#888888'
15	
16	plt.rcParams.update({
17	    'font.family': 'DejaVu Sans',
18	    'font.size': 10,
19	    'axes.titlesize': 10.5,
20	    'axes.titleweight': 'bold',
21	    'axes.labelsize': 9.5,
22	    'xtick.labelsize': 8.5,
23	    'ytick.labelsize': 8.5,
24	    'axes.spines.top': False,
25	    'axes.spines.right': False,
26	    'figure.facecolor': 'white',
27	    'axes.facecolor': 'white',
28	    'axes.grid': False,
29	    'axes.linewidth': 0.6,
30	})
31	
32	stroke = [pe.withStroke(linewidth=2.5, foreground='white')]
33	stroke_s = [pe.withStroke(linewidth=1.8, foreground='white')]
34	
35	fig = plt.figure(figsize=(5.5, 2.5))
36	gs = fig.add_gridspec(1, 3, width_ratios=[1, 1.7, 1], wspace=0.45,
37	                      left=0.08, right=0.97, top=0.82, bottom=0.22)
38	
39	models = ['Pi0+A1', 'Pi0.5']
40	x_pos = [0, 1]
41	clrs = [CORAL, BLUE]
42	edge_clrs = ['#B5604A', BLUE_DARK]
43	
44	# ════════════════════════════════════════
45	# Panel (a): Standard CAR
46	# ════════════════════════════════════════
47	ax_a = fig.add_subplot(gs[0])
48	car = [91.5, 26.8]
49	
50	bars = ax_a.bar(x_pos, car, width=0.48, color=clrs, edgecolor=edge_clrs,
51	                linewidth=0.7, zorder=3)
52	bars[0].set_hatch('///')
53	
54	for b, v in zip(bars, car):
55	    ax_a.text(b.get_x() + b.get_width()/2, v + 1.5, f'{v}%',
56	              ha='center', va='bottom', fontsize=8.5, fontweight='bold',
57	              path_effects=stroke)
58	
59	# x-tick labels with TSR embedded as second line
60	ax_a.set_xticks(x_pos)
61	ax_a.set_xticklabels(['Pi0+A1\nTSR=0%', 'Pi0.5\nTSR=74.7%'], fontsize=7.5)
62	# color the TSR portions
63	for i, (tick, color) in enumerate(zip(ax_a.get_
…[truncated 5878 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-27T02:00:17.670832+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig2.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig2.py"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-27T02:00:17.671109+00:00_

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
11	    'xtick.labelsize': 10.5,
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
22	COLORS = {
23	    'baseline': '#0072B2',
24	    'lora': '#E69F00',
25	    'sdf005': '#009E73',
26	    'sdf01': '#D55E00',
27	}
28	
29	baseline_str = "0.410535,0.372157,0.367551,0.347301,0.433721,0.385690,0.371494,0.398433,0.376634,0.381007,0.378640,0.378029,0.368726,0.363974,0.347250,0.393264,0.370445,0.370658,0.374338,0.399881,0.363556,0.332384,0.377387,0.376489,0.440435,0.376108,0.351063,0.426211,0.384493,0.375079,0.376344,0.412179,0.375265,0.375571,0.357926,0.363541,0.366746,0.341888,0.393978,0.428544,0.456280,0.376162,0.374719,0.376060,0.458242,0.366161,0.343575,0.360359,0.361380,0.338410,0.421658,0.387837,0.381387,0.406447,0.434757,0.367999,0.395390,0.382953,0.388771,0.362671,0.365072,0.365499,0.397851,0.381652,0.374391,0.394736,0.363747,0.374413,0.405143,0.372127,0.384909,0.376489,0.390958,0.380031,0.407444,0.374328,0.373997,0.359524,0.368326,0.393558,0.370891,0.375155,0.368425,0.395814,0.376858,0.370888,0.405806,0.369729,0.374194,0.361317,0.408268,0.390279,0.382961,0.404720,0.418936,0.391231,0.381323,0.397479,0.364759,0.363512,0.278502,0.349419,0.288903,0.320112,0.332317,0.372674,0.321285,0.370590,0.326243,0.360339,0.317917,0.353423,0.363516,0.341765,0.326348,0.348660,0.319205,0.335089,0.391541,0.334470,0.315652,0.324379,0.377147,0.392535,0.362931,0.337576,0.376282,0.364730,0.329658,0.321191,0.430344,0.386459,0.277309,0.360727,0.357776,0.322290,0.292745,0.317064,0.330825,0.330340,0.271226,0.336528,0.443525,0.346945,0.316339,0.371906,0
…[truncated 10574 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-27T02:00:17.671355+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig3.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig3.py"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-27T02:00:17.671612+00:00_

1	import matplotlib
2	matplotlib.use('Agg')
3	import matplotlib.pyplot as plt
4	import matplotlib.patches as mpatches
5	from matplotlib.patches import FancyArrowPatch, Ellipse
6	import numpy as np
7	
8	plt.rcParams.update({
9	    'font.family': 'DejaVu Sans',
10	    'font.size': 11,
11	    'axes.titlesize': 13,
12	    'axes.labelsize': 12,
13	    'xtick.labelsize': 10,
14	    'ytick.labelsize': 10,
15	    'legend.fontsize': 9,
16	    'figure.dpi': 300,
17	    'savefig.dpi': 300,
18	    'savefig.bbox': 'tight',
19	    'savefig.pad_inches': 0.05,
20	    'axes.spines.top': False,
21	    'axes.spines.right': False,
22	})
23	
24	COLORS = {
25	    'baseline': '#0072B2',
26	    'lora': '#E69F00',
27	    'sdf005': '#009E73',
28	    'sdf01': '#D55E00',
29	    'phase2': '#CC79A7',
30	}
31	
32	# Data: (name, TSR, CAR, marker, color, size)
33	data = [
34	    ('Pi0.5 baseline', 71.5, 28.5, '*', COLORS['baseline'], 220),
35	    ('LoRA-only s1',   51.5, 52.5, 'o', COLORS['lora'],     80),
36	    ('SDF $\\lambda$=0.005 s0', 55.5, 57.0, '^', COLORS['sdf005'], 80),
37	    ('SDF $\\lambda$=0.01 s0',  52.5, 57.0, 's', COLORS['sdf01'],  80),
38	    ('Phase 2 $\\lambda$=0 s2', 53.5, 57.5, 'D', COLORS['phase2'], 80),
39	]
40	
41	fig, ax = plt.subplots(figsize=(6, 5))
42	
43	# Quadrant boundaries
44	mid_x, mid_y = 50, 50
45	
46	# Quadrant backgrounds
47	ax.fill_between([mid_x, 100], mid_y, 100, alpha=0.06, color='#2ca02c', zorder=0)
48	ax.fill_between([0, mid_x], mid_y, 100, alpha=0.06, color='#d62728', zorder=0)
49	ax.fill_between([mid_x, 100], 0, mid_y, alpha=0.04, color='#ff7f0e', zorder=0)
50	ax.fill_between([0, mid_x], 0, mid_y, alpha=0.04, color='#7f7f7f', zorder=0)
51	
52	# Quadrant divider lines
53	ax.axhline(mid_y, color='#cccccc', linewidth=0.8, linestyle='--', zorder=1)
54	ax.axvline(mid_x, color='#cccccc', linewidth=0.8, linestyle='--', zorder=1)
55	
56	# Quadrant labels
57	ax.text(75, 96, 'Ideal\n(High TSR + High CAR)', ha='center', va='top',
58	        fontsize=8, color='#2ca
…[truncated 4386 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-27T02:00:17.671857+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/plot_scatter.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/plot_scatter.py"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-27T02:00:17.672078+00:00_

1	import matplotlib
2	matplotlib.use('Agg')
3	import matplotlib.pyplot as plt
4	import matplotlib.patches as mpatches
5	import numpy as np
6	
7	plt.rcParams['font.family'] = 'serif'
8	plt.rcParams['mathtext.fontset'] = 'dejavuserif'
9	
10	# Data
11	data = {
12	    'Pi0 (no refinement)': {
13	        'marker': 'o', 'color': '#3274A1', 'size': 60, 'zorder': 5,
14	        'points': {
15	            'LoRA baseline': (0, 82),
16	            'Full-FT baseline': (0.5, 83),
17	            'A1-LoRA (Pi0)': (0, 91.5),
18	            'A3 (Pi0)': (0, 74.5),
19	        }
20	    },
21	    'Oracle (GT SDF)': {
22	        'marker': 'D', 'color': '#8B5CF6', 'size': 55, 'zorder': 5,
23	        'points': {
24	            'Oracle-adaptive': (0, 75),
25	            'Oracle-fixed': (0, 73.1),
26	            'Oracle-feature': (0, 76.9),
27	        }
28	    },
29	    'Pi0.5 baseline': {
30	        'marker': 's', 'color': '#2CA02C', 'size': 55, 'zorder': 5,
31	        'points': {
32	            'Pi0.5 s0': (73, 28),
33	            'Pi0.5 s1': (76, 25),
34	            'Pi0.5 s2': (75, 27.5),
35	        }
36	    },
37	    'Pi0.5+A1 (SDF aux)': {
38	        'marker': '*', 'color': '#E8740C', 'size': 180, 'zorder': 6,
39	        'points': {
40	            r'$\lambda$=0.005': (47, 58),
41	            r'$\lambda$=0.01': (49, 56.5),
42	        }
43	    },
44	    'Pi0.5 spatial': {
45	        'marker': '^', 'color': '#7F7F7F', 'size': 60, 'zorder': 5,
46	        'points': {
47	            'Pi0.5 spatial': (57.5, 13),
48	        }
49	    },
50	}
51	
52	fig, ax = plt.subplots(figsize=(5, 4), dpi=300)
53	
54	# "Fake safety" zone
55	ax.axhspan(70, 100, xmin=0, xmax=0.08, color='#D3D3D3', alpha=0.25, zorder=1)
56	ax.text(3.5, 96, '"Fake safety"\nzone', fontsize=6.5, color='#888888',
57	        ha='center', va='top', style='italic')
58	
59	# Plot each group
60	for group_name, info in data.items():
61	    xs = [p[0] for p in info['points'].values()]
62	    ys = [p[1] for p in info['points'].values()]
63	 
…[truncated 2483 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-27T02:00:17.672319+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"\\\\\\\\begin{figure}\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/*.tex | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"\\\\\\\\begin{figure}\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/*.tex | head -20"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-27T02:00:17.672551+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex:4:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex:28:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex:27:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex:35:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex:5:\begin{figure}[t]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-27T02:00:17.672764+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim1.tex"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-27T02:00:17.672981+00:00_

1	\section{The Fake Safety Problem}\label{sec:fake_safety}
2	
3	Standard CAR assumes that collision-free episodes reflect deliberate avoidance. This assumption is systematically violated: in every Pi0 configuration tested, over 99\% of collision-free episodes are action-collapse artifacts. The robot never moved, never collided, and never avoided anything. Table~\ref{tab:fake_safety} shows that all Pi0 configurations exhibit pervasive fake safety: over 99\% of safe episodes have displacement below 0.1\,mm (73.9\% below 1\,$\mu$m for Pi0+A1), and TSR is at or near 0\%.\footnote{Pi0-family values report obstacle displacement from the original protocol; Pi0.5 reports EE displacement from the rotation-corrected protocol (\S\ref{sec:dfcar}). Sub-millimeter displacement indicates action collapse in both cases.} Applying CAR$_\text{f}$ collapses all three to ${\approx}$\,0\%. Paradoxically, Pi0+A1 achieves the \emph{highest} raw CAR (91.5\%) precisely because a parameter-name mismatch prevented LoRA weight loading (Table~\ref{tab:configurations}), leaving only auxiliary heads trained and producing more complete action collapse than the LoRA or Full-FT baselines; more complete action collapse yields higher fake safety. Pi0.5 validates the metric from the opposite direction: all 57 safe episodes exceed 288\,mm displacement, yielding 0\% fake safe rate and CAR$_\text{f}$ equal to raw CAR (28.5\%). The displacement distribution is sharply bimodal (Figure~\ref{fig:displacement} in Appendix~\ref{sec:appendix_displacement}), with a five-order-of-magnitude gap that makes the threshold robust.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Fake safety decomposition on SafeLIBERO. CAR$_\text{f}$ excludes episodes with displacement $< \tau_d = 0.1$\,mm.}
8	\label{tab:fake_safety}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	Method & Ep. & CAR (\%) & TSR (\%) & Fake Safe (\%) & CAR$_\text{f}$ (\%) \\
14	\midrule
15	Pi0 Full-FT  & 200 & 83.0 & 0.5 & 99.4 & $\approx$
…[truncated 1697 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-27T02:00:17.673213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/docs/paper/claim2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/docs/paper/claim2.tex"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-27T02:00:17.673394+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-27T02:00:17.673640+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim2.tex"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-27T02:00:17.673847+00:00_

1	\section{End-Effector-Only SDF Cannot Ensure Full-Body Safety}\label{sec:ee_only}
2	
3	Could a perfect SDF signal enable effective EE-only refinement? We replace the learned SDF with ground-truth distance fields from the simulation geometry (\S\ref{sec:oracle_setup}). Table~\ref{tab:oracle} and Figure~\ref{fig:oracle_bar} show that all three oracle variants achieve \emph{lower} CAR than unrefined baselines: the best oracle (76.9\%) falls 5.1 points below LoRA (82.0\%). Refinement with perfect distance information produces more collisions, not fewer.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Oracle SDF refinement with ground-truth distance fields. All oracle variants achieve lower CAR than unrefined baselines. Per-task breakdown in Appendix~\ref{sec:appendix_pertask_oracle}.}
8	\label{tab:oracle}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lccc}
12	\toprule
13	Method & CAR (\%) & Fake Safe (\%) & Refines/ep \\
14	\midrule
15	LoRA baseline (no refine) & 82.0 & 99.4 & -- \\
16	Full-FT baseline (no refine) & 83.0 & -- & -- \\
17	\midrule
18	Oracle-adaptive (GT, dyn.\ $\alpha$) & 75.0 & 98.3 & 14.2 \\
19	Oracle-fixed (GT, $\alpha{=}0.005$) & 73.1 & 98.3 & 14.8 \\
20	Oracle-feature (GT, feat.\ space) & 76.9 & 96.7 & 241.7 \\
21	\midrule
22	A3 learned SDF & 77.1 & -- & 0.0 \\
23	\bottomrule
24	\end{tabular}
25	\end{table}
26	
27	\begin{figure}[t]
28	\centering
29	\includegraphics[width=0.85\linewidth]{fig_oracle_bar.pdf}
30	\caption{CAR for oracle SDF refinement versus unrefined baselines. All GT oracle variants underperform baselines despite perfect distance information.}
31	\label{fig:oracle_bar}
32	\end{figure}
33	
34	Per-task analysis reveals the mechanism (Appendix~\ref{sec:appendix_pertask_oracle}). On the one task where the EE is the primary collision body, oracle refinement helps (+9 points). On the remaining three tasks, the SDF gradient pushes the EE away from the nearest surface, but the resulting joint-space displacement rotates intermediate arm links int
…[truncated 584 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-27T02:00:17.674087+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/claim3.tex"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-27T02:00:17.674301+00:00_

1	\section{Avoidance Source Diagnosis}\label{sec:avoidance_source}
2	
3	Fine-tuning on collision-free demonstrations produces genuine collision avoidance: LoRA-adapted Pi0.5 raises CAR by ${\sim}$28 percentage points with zero frozen episodes. Does SDF geometric supervision contribute additional avoidance beyond what demonstrations provide? We compare LoRA-only, LoRA+SDF ($\lambda = 0.005$), and LoRA+SDF ($\lambda = 0.01$) on Pi0.5, all evaluated at the 30K-step checkpoint.
4	
5	\begin{table}[t]
6	\centering
7	\caption{Avoidance source attribution on SafeLIBERO. SDF adds no measurable CAR beyond LoRA-only across $\lambda \in [0.005, 0.1]$ ($p > 0.1$). All fine-tuned models exhibit 0\% frozen rate and displacement $>$\,0.37\,m.}
8	\label{tab:avoidance_source}
9	\vspace{2pt}
10	\small
11	\begin{tabular}{lcccc}
12	\toprule
13	Method & Seeds & TSR (\%) & CAR (\%) & EE Disp (m) \\
14	\midrule
15	Pi0.5 baseline & 3 & 74.7\,$\pm$\,1.5 & 26.8\,$\pm$\,1.6 & 0.367 \\
16	\midrule
17	LoRA-only (no SDF) & 2 & 51.5 & 54.5\,$\pm$\,2.8 & 0.392 \\
18	LoRA+SDF $\lambda{=}0.005$ & 3 & 54.0\,$\pm$\,3.0 & 54.5\,$\pm$\,2.3 & 0.387 \\
19	LoRA+SDF $\lambda{=}0.01$ & 3 & 53.8\,$\pm$\,1.5 & 56.3\,$\pm$\,1.6 & 0.389 \\
20	LoRA+SDF $\lambda{=}0.1$\textsuperscript{$\dagger$} & 2 & 52.5 & 55.5 & -- \\
21	\bottomrule
22	\end{tabular}
23	\vspace{1pt}
24	{\footnotesize \textsuperscript{$\dagger$}20K-step checkpoint, 2 seeds; 30K results pending.}
25	\end{table}
26	
27	Table~\ref{tab:avoidance_source} shows that collision-free demonstrations alone raise CAR by ${\sim}$28 percentage points (26.8\% $\to$ 54.5\%) with zero frozen episodes and displacement above 0.37\,m, confirming genuine avoidance rather than action collapse. Adding SDF supervision produces no measurable benefit: LoRA-only CAR (54.5\%) is identical to $\lambda = 0.005$ and statistically indistinguishable from $\lambda = 0.01$ (56.3\%, $p > 0.1$; null distribution details in Appendix~\ref{sec:appendix_null}). A Phase~2 ablation ($\lamb
…[truncated 2047 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-27T02:00:17.674581+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/appendix.tex",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-27T02:00:17.674836+00:00_

1	\section{Displacement Distribution}
2	\label{sec:appendix_displacement}
3	
4	\begin{figure}[h]
5	\centering
6	\includegraphics[width=\linewidth]{fig2_ee_displacement_distribution}
7	\caption{Displacement distribution across evaluation episodes. Pi0-family models (blue) cluster below 1\,$\mu$m, while Pi0.5 episodes (orange) exceed 200\,mm. The five-order-of-magnitude gap makes $\tau_d$ robust to any value in $[2, 200]$\,mm.}
8	\label{fig:displacement}
9	\end{figure}
10	
11	\section{Displacement Threshold Sensitivity Analysis}
12	\label{sec:appendix_threshold}
13	
14	To validate the robustness of our displacement threshold $\tau_d$, we evaluate the frozen rate across four orders of magnitude. Table~\ref{tab:threshold_sensitivity} shows that the fake safety pattern persists across all reasonable threshold choices: A1-LoRA exhibits near-total action collapse regardless of threshold, while Pi0.5+A1 maintains 0\% frozen rate even at the most conservative setting.
15	
16	\begin{table}[h]
17	\centering
18	\caption{Frozen rate (\% of episodes with $d_\mathrm{max} < \tau_d$) across threshold values.}
19	\label{tab:threshold_sensitivity}
20	\begin{tabular}{lccc}
21	\toprule
22	$\tau_d$ & A1-LoRA (Pi0) & Pi0.5 Baseline & Pi0.5+A1 (SDF aux) \\
23	\midrule
24	0.001 mm (1\,$\mu$m) & 73.9 & 0.0 & 0.0 \\
25	0.1 mm  & 99.6 & 0.0 & 0.0 \\
26	1.0 mm  & 100.0 & 0.0 & 0.0 \\
27	10 mm   & 100.0 & 0.0 & 0.0 \\
28	\bottomrule
29	\end{tabular}
30	\end{table}
31	
32	The choice of $\tau_d = 0.1$\,mm represents a conservative threshold: displacement below this value is physically negligible in manipulation tasks where typical action magnitudes are 1--10\,mm per step. Even at $\tau_d = 1$\,$\mu$m, 73.9\% of A1-LoRA safe episodes are classified as frozen, while all Pi0.5 episodes remain above threshold at every level tested.
33	
34	Table~\ref{tab:dfcar_threshold} extends this analysis to CAR$_\text{f}$ across fine-tuned Pi0.5 configurations. All eight model-seed combinations yield identical CAR
…[truncated 4090 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-27T02:00:17.675083+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/plot_oracle_bar.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/plot_oracle_bar.py"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-27T02:00:17.675294+00:00_

1	import matplotlib
2	matplotlib.use('Agg')
3	import matplotlib.pyplot as plt
4	import numpy as np
5	
6	plt.rcParams['font.family'] = 'serif'
7	plt.rcParams['mathtext.fontset'] = 'dejavuserif'
8	
9	methods = [
10	    'Oracle-fixed\n(GT SDF)',
11	    'A3 no-refine\n(learned SDF)',
12	    'Oracle-adaptive\n(GT SDF)',
13	    'Oracle-feature\n(GT SDF)',
14	    'LoRA baseline',
15	    'Full-FT baseline',
16	]
17	cars = [73.1, 74.5, 75.0, 76.9, 82.0, 83.0]
18	
19	colors = [
20	    '#A78BFA',  # oracle-fixed - light purple
21	    '#3274A1',  # A3 - blue
22	    '#8B5CF6',  # oracle-adaptive - purple
23	    '#7C3AED',  # oracle-feature - dark purple
24	    '#9CA3AF',  # LoRA baseline - gray
25	    '#6B7280',  # Full-FT baseline - darker gray
26	]
27	
28	fig, ax = plt.subplots(figsize=(6, 3.5), dpi=300)
29	
30	y_pos = np.arange(len(methods))
31	bars = ax.barh(y_pos, cars, height=0.55, color=colors, edgecolor='white', linewidth=0.5)
32	
33	# Value labels
34	for bar, val in zip(bars, cars):
35	    ax.text(bar.get_width() + 0.8, bar.get_y() + bar.get_height() / 2,
36	            f'{val:.1f}%', va='center', ha='left', fontsize=8, color='#333333')
37	
38	# Baseline average line
39	baseline_avg = (82.0 + 83.0) / 2
40	ax.axvline(x=baseline_avg, color='#6B7280', linestyle='--', linewidth=0.9, alpha=0.7, zorder=3)
41	ax.text(baseline_avg + 0.5, len(methods) - 0.3, 'No Refinement\navg', fontsize=6.5,
42	        color='#6B7280', va='bottom', ha='left', style='italic')
43	
44	ax.set_yticks(y_pos)
45	ax.set_yticklabels(methods, fontsize=8)
46	ax.set_xlabel('Collision Avoidance Rate (%)', fontsize=10)
47	ax.set_xlim(65, 92)
48	ax.tick_params(axis='x', labelsize=8)
49	ax.spines['top'].set_visible(False)
50	ax.spines['right'].set_visible(False)
51	ax.invert_yaxis()
52	
53	plt.tight_layout()
54	out = '/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig_oracle_bar.pdf'
55	plt.savefig(out, bbox_inches='tight', dpi=300)
56	print(f'Saved: {out}')
57	
…[truncated 15 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-27T02:00:17.675560+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf -name \"*lambda*\" -o -name \"*fig5*\" | grep -E \"\\.(py|pdf|png)$\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf -name \"*lambda*\" -o -name \"*fig5*\" | grep -E \"\\.(py|pdf|png)$\""
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-27T02:00:17.675753+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/chart/fig5_lambda_curve_5f2325.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/chart/fig5_lambda_curve.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig5_lambda_curve.pdf
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig5_lambda_curve.png
/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig5.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-27T02:00:17.675943+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig5.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/plot_fig5.py"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-27T02:00:17.676163+00:00_

1	#!/usr/bin/env python3
2	"""Fig 5: λ Dose-Response Curve — multi-seed means ± std."""
3	
4	import matplotlib
5	matplotlib.use('Agg')
6	import matplotlib.pyplot as plt
7	import matplotlib.patches as mpatches
8	from matplotlib.lines import Line2D
9	import numpy as np
10	from pathlib import Path
11	
12	OUT = Path('/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/'
13	           'diff_collision_sdf/artifacts/figures/fig5_lambda_curve')
14	
15	
16	def main():
17	    # ── Data (Director-审定, 2026-05-26, updated l01 3-seed + TSR) ──
18	    car_seeds = {
19	        0:     [56.5, 52.5],
20	        0.005: [57, 54, 52.5],
21	        0.01:  [57.0, 57.5, 54.5],
22	    }
23	    tsr_seeds = {
24	        0:     [51.5, 51.5],
25	        0.005: [55.5, 50.5, 56.0],
26	        0.01:  [52.5, 55.5, 53.5],
27	    }
28	    n_per_lambda = {0: 2, 0.005: 3, 0.01: 3}
29	
30	    lambdas = [0, 0.005, 0.01, 0.1]
31	    x = np.arange(len(lambdas))
32	    x_labels = ['0\n(LoRA-only)', '0.005', '0.01', '0.1']
33	    pi05 = {'car': 28.5, 'tsr': 71.5}
34	    avail = [0, 0.005, 0.01]
35	
36	    def calc_stats(seeds):
37	        mean = float(np.mean(seeds))
38	        std = float(np.std(seeds, ddof=1)) if len(seeds) >= 2 else None
39	        return mean, std
40	
41	    car_s = {l: calc_stats(car_seeds[l]) for l in avail}
42	    tsr_s = {l: calc_stats(tsr_seeds[l]) for l in avail}
43	
44	    # ── Plot ──
45	    plt.rcParams.update({
46	        'font.family': 'DejaVu Sans',
47	        'font.size': 12,
48	        'figure.dpi': 300,
49	        'savefig.dpi': 300,
50	        'savefig.bbox': 'tight',
51	        'savefig.pad_inches': 0.08,
52	    })
53	
54	    CAR_C, TSR_C = '#2171B5', '#CB181D'
55	    fig, ax1 = plt.subplots(figsize=(8, 5))
56	    ax2 = ax1.twinx()
57	
58	    ax1.set_xlabel(r'SDF Loss Weight $\lambda$', fontsize=13)
59	    ax1.set_ylabel('CAR (%)', color=CAR_C, fontsize=13)
60	    ax2.set_ylabel('TSR (%)', color=TSR_C, fontsize=13)
61	    ax1.tick_params(axis='y', labelcolor=CAR_C)

…[truncated 4755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-27T02:00:17.676392+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/gen_scatter.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/gen_scatter.py"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-27T02:00:17.676644+00:00_

1	import matplotlib
2	matplotlib.use('Agg')
3	import matplotlib.pyplot as plt
4	import matplotlib.patches as mpatches
5	from matplotlib.patches import FancyArrowPatch
6	import numpy as np
7	
8	plt.rcParams['font.family'] = 'serif'
9	plt.rcParams['font.size'] = 9
10	
11	fig, ax = plt.subplots(figsize=(5, 4), dpi=300)
12	
13	# Data points (TSR, CAR)
14	# Left cluster (TSR ≈ 0, CAR 73-91.5) — use letter labels
15	left_cluster = [
16	    ('(a)', 0, 91.5, 'blue', 'o'),      # A1-LoRA
17	    ('(b)', 0.5, 83, 'blue', 'o'),       # Full-FT baseline
18	    ('(c)', 0, 82, 'blue', 'o'),         # LoRA baseline
19	    ('(d)', 0, 76.9, 'purple', 'D'),     # Oracle-feature
20	    ('(e)', 0, 75, 'purple', 'D'),       # Oracle-adaptive
21	    ('(f)', 0, 74.5, 'blue', 'o'),       # A3
22	    ('(g)', 0, 73.1, 'purple', 'D'),     # Oracle-fixed
23	]
24	
25	# Pi0.5 baseline cluster
26	pi05_cluster = [
27	    ('Pi0.5 s0', 73, 28, 'green', 's'),
28	    ('Pi0.5 s1', 76, 25, 'green', 's'),
29	    ('Pi0.5 s2', 75, 27.5, 'green', 's'),
30	]
31	
32	# Pi0.5+A1 points
33	pi05_a1 = [
34	    ('λ=0.005', 47, 58, 'orange', '*'),
35	    ('λ=0.01', 49, 56.5, 'orange', '*'),
36	]
37	
38	# Draw fake safety zone
39	ax.fill_between([0, 5], 60, 100, alpha=0.12, color='gray', zorder=0)
40	ax.text(2.5, 96, 'Fake Safety\nZone', ha='center', va='top', fontsize=7,
41	        color='gray', style='italic')
42	
43	# Plot left cluster points
44	for label, x, y, color, marker in left_cluster:
45	    ax.scatter(x, y, c=color, marker=marker, s=50, zorder=5, edgecolors='black', linewidths=0.3)
46	
47	# Letter labels for left cluster — offset to the right
48	offsets = [
49	    (3.5, 0),    # (a) A1-LoRA
50	    (3.5, 0),    # (b) Full-FT
51	    (3.5, 0),    # (c) LoRA
52	    (3.5, 0),    # (d) Oracle-feature
53	    (3.5, 0),    # (e) Oracle-adaptive
54	    (3.5, 0),    # (f) A3
55	    (3.5, 0),    # (g) Oracle-fixed
56	]
57	
58	for (label, x, y, color, marker), (ox, oy) in zip(left_cluster, offsets):
59	    ax.annotate(
…[truncated 3573 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-27T02:00:17.676880+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-27T02:00:17.677087+00:00_

1	\section{Experimental Setup and Metrics}\label{sec:method}
2	
3	\subsection{Benchmark and Models}\label{sec:benchmark}
4	
5	We evaluate on SafeLIBERO~\cite{hu2025vlsa}, the \textit{object\_pudding} suite (Level~I): four tabletop pick-and-place tasks with collision hazards, using per-timestep collision detection. Two VLA families are tested: \textbf{Pi0} (${\sim}$2.5B)~\cite{black2024pi0} with flow matching~\cite{lipman2023flow}, and \textbf{Pi0.5} with broader pre-training. Table~\ref{tab:configurations} lists all configurations. Each uses 50 episodes per task (200 total); Pi0.5 multi-seed runs use 3 seeds (600 episodes). We report Collision Avoidance Rate (CAR), the fraction of collision-free episodes, and Task Success Rate (TSR), the fraction achieving task completion~\cite{hu2025vlsa,zhang2025safevla}.
6	
7	\begin{table}[t]
8	\centering
9	\caption{Training configurations. Trainable parameters exclude the frozen backbone.}
10	\label{tab:configurations}
11	\vspace{2pt}
12	\small
13	\begin{tabular}{llr}
14	\toprule
15	Configuration & Description & Trainable Params \\
16	\midrule
17	Pi0 Full-FT & Full fine-tune, flow-matching loss & ${\sim}$2.5B \\
18	Pi0 LoRA & LoRA adapters only & ${\sim}$33.5M \\
19	Pi0+A1 (SDF aux)\textsuperscript{$\dagger$} & LoRA + SDF decoder + EE extractor & ${\sim}$658K \\
20	Pi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\sim}$34.2M \\
21	Pi0.5 (pre-trained) & No fine-tuning & 0 \\
22	Pi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\sim}$33.5M \\
23	Pi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\lambda \in \{0.005, 0.01, 0.1\}$ & ${\sim}$34.2M \\
24	\bottomrule
25	\end{tabular}
26	\vspace{2pt}
27	\raggedright\footnotesize\textsuperscript{$\dagger$}LoRA weights not loaded due to parameter-name mismatch; only auxiliary heads trained.
28	\end{table}
29	
30	\subsection{Displacement-Filtered CAR}\label{sec:dfcar}
31	
32	Standard CAR conflates genuine avoidance with action collapse. We define an episode as \emph{action-collapsed
…[truncated 1461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-27T02:00:17.677327+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515 -name \"corl_2026.sty\" -o -name \"corl*.sty\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515 -name \"corl_2026.sty\" -o -name \"corl*.sty\" 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-27T02:00:17.677551+00:00_

/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/corl_2026.sty

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-27T02:00:17.677749+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/corl_2026.sty",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/corl_2026.sty",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-27T02:00:17.677955+00:00_

1	% File: corl_2026.sty 
2	%
3	% Latex templates for the Conference on Robot Learning (CoRL)
4	%
5	% This template is heavily inspired by the NeurIPS, ICML, ICLR and IEEE Transactions latex templates.
6	% Hence we would like to thank: Roman Garnett and the previous mantainers of the NIPS style, Percy Liang and the previous mantainers of the ICML style, Hugo Larochelle for the ICLR style, and Michael Shell for the IEEE Transactions style.
7	%
8	% History:
9	% 2017/04/16 - First revision by Roberto Calandra (roberto.calandra@berkeley.edu).
10	%	       Main changes:
11	%	       - The abstract is more compact compared to NeurIPS/ICML
12	%	       - References are by default using natbib with squared numbers (e.g., [1])
13	%	       - DOI fields from the bibtex are automatically converted to hyperlinks 
14	%	       to the corresponding page
15	%	       - acknowledgments are now a command, and the corresponding subsubsection is
16	%	       automatically included only in the final version
17	% 2017/06/12 - Modified to use corlabbrvnat.bst, which order the reference by order of appearance in the paper
18	% 2017/06/13 - fixed typo
19	% 2018/05/09 - Slightly modified for CoRL 2018 by Jun Morimoto (xmorimo@atr.jp)
20	% 2019/01/28 - Slightly modified for CoRL 2019 by Jun Nakanishi (jnakanis@meijo-u.ac.jp)
21	% 2020/02/02 - Slightly modified for CoRL 2020 by Cynthia Matuszek (cmat@umbc.edu)
22	% 2020/08/19 - Added preprint option by Roberto Calandra (rcalandra@fb.com)
23	% 2021/05/06 - Slightly modified for CoRL 2021 by Gerhard Neumann (gerhard.neumann@kit.edu)
24	% 2022/03/09 - Slightly modified for CoRL 2022 by Minas Liarokapis (minas.liarokapis@auckland.ac.nz)
25	% 2022/03/06 - Slightly modified for CoRL 2023 by Marc Toussaint (toussaint@tu-berlin.de)
26	% 2024/03/26 - Slightly modified for CoRL 2024 by David Held (dheld@andrew.cmu.edu)
27	% 2026/01/10 - Slightly modified for CoRL 2026 by Yoonchang Sung (yoonchang.sung@ntu.edu.sg)
28	%
29	% TODO: nohyperref is not working at th
…[truncated 1658 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-27T02:00:17.678294+00:00_

Perfect! Now I have comprehensive information. Let me compile the final report with all the findings.

## Summary: Figure Style and Structure for CoRL 2026 VLA Collision Avoidance Paper

Based on my thorough exploration of the project, here is the complete guide to the paper's figure conventions:

### **Figure 1 Caption (Teaser)**
Location: `/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/introduction.tex`

**Exact Caption Text:**
> "The fake safety problem in VLA collision avoidance evaluation. Standard CAR classifies a frozen robot as safe because it produces zero collisions (left). CAR_f filters out action-collapsed episodes where displacement falls below τ_d, revealing that Pi0+A1's 91.5% safety score drops to ≈0% (center). Pi0.5 exhibits genuine avoidance with active motion above 288 mm in all safe episodes, and CAR_f equals raw CAR (right)."

### **Figure Generation Code Patterns**

#### **Framework & Libraries**
- matplotlib with Agg backend (non-interactive)
- DejaVu Sans font family (primary)
- DPI: 300 for both savefig and display
- Save as both PDF and PNG in `/artifacts/figures/`

#### **Global matplotlib rc settings (from fig1_teaser.py):**
```python
'font.family': 'DejaVu Sans',
'font.size': 10,
'axes.titlesize': 10.5,
'axes.titleweight': 'bold',
'axes.labelsize': 9.5,
'xtick.labelsize': 8.5,
'ytick.labelsize': 8.5,
'axes.spines.top': False,
'axes.spines.right': False,
'figure.facecolor': 'white',
'axes.facecolor': 'white',
'axes.grid': False,
'axes.linewidth': 0.6,
```

### **Color Scheme**

**Core Palette (from fig1_teaser.py):**
- CORAL: `#E8846B` (Pi0+A1, warm orange-red)
- CORAL_DARK: `#C0603E` (darker coral for accents)
- BLUE: `#0072B2` (Pi0.5, standard blue)
- BLUE_DARK: `#005A8D` (darker blue)
- RED_TEXT: `#C0392B` (alerts, important drops)
- GRAY_TEXT: `#888888` (secondary annotations)

**Alternative Palette (from plot_fig2.py, fig3):**
- Blue baseline: `#0072B2`
- LoRA: `#E69F00` (golden-orange)
- SDF 
…[truncated 4314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Agent",
  "elapsed_ms": 11
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-27T02:00:17.678617+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/fig1_teaser*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/fig1_teaser*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-27T02:00:17.678811+00:00_

artifacts/figures/fig1_teaser.py
artifacts/_project/chart/fig1_teaser.pdf
artifacts/figures/fig1_teaser.pdf
artifacts/figures/fig1_teaser.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-27T02:00:17.678996+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig1_teaser.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig1_teaser.py"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-27T02:00:17.679294+00:00_

1	import matplotlib
2	matplotlib.use('Agg')
3	import matplotlib.pyplot as plt
4	import matplotlib.patheffects as pe
5	import matplotlib.ticker as mticker
6	import numpy as np
7	
8	# ── Colors ──
9	CORAL = '#E8846B'
10	CORAL_DARK = '#C0603E'
11	BLUE = '#0072B2'
12	BLUE_DARK = '#005A8D'
13	RED_TEXT = '#C0392B'
14	GRAY_TEXT = '#888888'
15	
16	plt.rcParams.update({
17	    'font.family': 'DejaVu Sans',
18	    'font.size': 10,
19	    'axes.titlesize': 10.5,
20	    'axes.titleweight': 'bold',
21	    'axes.labelsize': 9.5,
22	    'xtick.labelsize': 8.5,
23	    'ytick.labelsize': 8.5,
24	    'axes.spines.top': False,
25	    'axes.spines.right': False,
26	    'figure.facecolor': 'white',
27	    'axes.facecolor': 'white',
28	    'axes.grid': False,
29	    'axes.linewidth': 0.6,
30	})
31	
32	stroke = [pe.withStroke(linewidth=2.5, foreground='white')]
33	stroke_s = [pe.withStroke(linewidth=1.8, foreground='white')]
34	
35	fig = plt.figure(figsize=(5.5, 2.5))
36	gs = fig.add_gridspec(1, 3, width_ratios=[1, 1.7, 1], wspace=0.45,
37	                      left=0.08, right=0.97, top=0.82, bottom=0.22)
38	
39	models = ['Pi0+A1', 'Pi0.5']
40	x_pos = [0, 1]
41	clrs = [CORAL, BLUE]
42	edge_clrs = ['#B5604A', BLUE_DARK]
43	
44	# ════════════════════════════════════════
45	# Panel (a): Standard CAR
46	# ════════════════════════════════════════
47	ax_a = fig.add_subplot(gs[0])
48	car = [91.5, 26.8]
49	
50	bars = ax_a.bar(x_pos, car, width=0.48, color=clrs, edgecolor=edge_clrs,
51	                linewidth=0.7, zorder=3)
52	bars[0].set_hatch('///')
53	
54	for b, v in zip(bars, car):
55	    ax_a.text(b.get_x() + b.get_width()/2, v + 1.5, f'{v}%',
56	              ha='center', va='bottom', fontsize=8.5, fontweight='bold',
57	              path_effects=stroke)
58	
59	# x-tick labels with TSR embedded as second line
60	ax_a.set_xticks(x_pos)
61	ax_a.set_xticklabels(['Pi0+A1\nTSR=0%', 'Pi0.5\nTSR=74.7%'], fontsize=7.5)
62	# color the TSR portions
63	for i, (tick, color) in enumerate(zip(ax_a.get_
…[truncated 5878 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-27T02:00:17.679609+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig1_teaser.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/figures/fig1_teaser.png"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-27T02:00:17.680847+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-27T02:00:17.681099+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-27T02:00:17.681314+00:00_

__pycache__
_project
a3_lora_fix_result.json
abc_scenario_patches.md
analysis_m022_norm_stats_root_cause.md
analysis_m026_m027_m028_gradient_refine_diagnosis.md
analyze_d012_results.py
analyze_displacement.py
claim3_data_summary.md
comprehensive_fix_report.txt
diagnose_eval_a3_v11_object.md
disk_cleanup_report.md
drafts
dream_reports
emergency_cleanup_report.md
eval_a3_v11_object
eval_batch_20270527.md
eval_collision_enhancement_plan.md
eval_commands_d012.md
eval_commands_d012_final.md
eval_openvla_safelibero.py
eval_pi05_safelibero.py
eval_pi05_safelibero_object_v11
eval_prep_l01_high.md
eval_readiness_westd35807.md
eval_safelibero.py
eval_safelibero_openvla.py
fig5_lambda_data.csv
fig5_lambda_stepwise.csv
figures
fix_a1.py
fix_a3.py
kg3_gradient_toy_test.py
literature_review.md
lora_baseline_launch_checklist.md
manifest.yaml
method_draft.md
metric_definitions.md
openvla_eval_prep.md
paper_data_summary.md
paper_draft.pdf
phase2_fix_report.md
pi05_a1_sdf_feasibility_report.md
pi05_collision_analysis_report.md
prep_spatial_a1.md
reeval_comparison.json
reeval_comparison.py
reeval_comparison.tex
reference_audit_report.md
related_work_outline.md
related_work_survey.md
remaining_train_status.md
report_a1_integration.md
report_action_scale_fix.md
report_baseline_fix.md
report_baseline_prep.md
report_data_pipeline.md
report_env_setup_kg1_kg2.md
report_eval_tsr_zero_fix.md
report_kg3_gradient_test.md
report_openpi_deploy.md
report_pi05_object_collision_analysis.md
report_pi0_baseline_fake_rate.md
report_safelibero.md
report_sdf_extraction.md
report_vla_codebase.md
research_openvla_libero.md
src
step7k_overfit_check.md
task3_collision_matrix_step10k.md
threshold_sensitivity
train_a1_hook.py
train_a1_sdf_aux_pi05.py
train_baseline.py
train_pi05_lora_baseline.py
training_progress_20260520_1020.md
training_progress_20260527.md
worker_output.md
worker_output_diagnose_eval_baseline_fullft_spatial_v11.md
worker_report_westd45947_status.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-27T02:00:17.681593+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-27T02:00:17.681788+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-27T02:00:17.682090+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/fig1_teaser_design.md",
  "content": "# Figure 1 Teaser Design\n\n## Narrative Intent\n\nA frozen robot scores high on CAR not because it is safe, but because it never moves—CAR_f exposes the illusion by filtering action-collapsed episodes.\n\n## Layout\n\n```\n┌─────────────────────────────────────────────────────────────────┐\n│  (a) Fake Safety          (b) CAR_f Filter       (c) Genuine   │\n│                                                      Safety    │\n│ ┌──────────────┐   ┌─────────────────────┐   ┌──────────────┐ │\n│ │              │   │                     │   │   ╭─trajectory │\n│ │  ┌─arm─┐    │   │  ┌───────────────┐  │   │  ╭╯  ╲        │\n│ │  │ (frozen) │   │  │ 91.5%  ──────►│  │   │ arm    ╲      │\n│ │  │  ·       │   │  │  episodes     │  │   │  ╲   obstacle  │\n│ │  │  ·       │   │  │       ┌───┐   │  │   │   ╰──►goal     │\n│ │  └──┘  obs  │   │  │  τ_d  │ ≈0%│  │  │   │              │\n│ │              │   │  └───────┴───┘   │  │   │              │\n│ ├──────────────┤   │                     │   ├──────────────┤ │\n│ │▓░░░░░░░░░░░░│   │  Pi0.5: 26.8%→28.5% │   │▓▓▓▓▓▓▓▓▓▓▓▓▓│ │\n│ │ <0.1mm      │   │  (unchanged)         │   │ >288mm       │ │\n│ └──────────────┘   └─────────────────────┘   └──────────────┘ │\n│                                                                 │\n│  CAR=91.5%  TSR=0%    91.5% ──τ_d──► ≈0%    CAR=26.8% TSR=74.7%│\n└─────────────────────────────────────────────────────────────────┘\n```\n\n- 总尺寸: 5.5 × 2.8 inches（单栏宽度，略高于当前版本以容纳 schematic）\n- 三列 width_ratios=[1, 1.2, 1]，中间 panel 稍宽以容纳 flow 图\n- 每列分上下两区：上区 schematic/flow（~70% 高度），下区 displacement 条（~30% 高度）\n\n## Panel A: Fake Safety\n\n### Elements\n- **Robot arm schematic**（侧视简化）：2-link arm 以灰色/淡色绘制，关节处用圆点标记。手臂完全静止——用虚线轮廓 + \"frozen\" 雪花/锁标记暗示不动。无运动轨迹。\n- **Obstacle**：红色/橙色立方体或圆柱体，位于 arm 工作空间内但未接触（因为 arm 从未伸出）。\n- **Displacement bar**（底部）：水平条形图，填充量极小（< 0.1mm），用 CORAL 色。条形旁标注 \"< 0.1 mm\"。背景为浅灰色 action-collapse zone。\n- **Metric badge**：panel 顶部或 arm 旁，标注 \"CAR = 91.5%\" 和 \"TSR = 0%\"。\n\n### Colors\n- Arm body: `#D0D0D0`（浅灰，暗示无生命/冻结）\n- Arm outline: `CORAL (#E8846B)` 虚线，关联 Pi0+A1 配色\n- Obstacle: `#E8846B` 半透明填充 + `#C0603E` 边框\n- Displacement bar: `CORAL (#E8846B)`\n- Collapse zone bg: `#F0F0F0`\n- TSR=0% 文字: `RED_TEXT (#C0392B)`\n- Panel 标题/badge: `CORAL_DARK (#C0603E)`\n\n### Annotations\n- Arm 上方: 虚线框 + 文字 **\"frozen\"**（或锁图标 🔒，如果 DejaVu Sans 支持）\n- 底部 displacement bar 旁: \"< 0.1 mm\" (小字，`CORAL_DARK`)\n- 右下角 badge: \"CAR = 91.5%\" (大号加粗)，下方 \"TSR = 0%\" (`RED_TEXT`)\n- Panel 标题: **(a) Fake Safety**\n\n### Visual Cues\n- Arm 用 dashed line + 低 alpha (0.4) 传递\"这不是真正的运动\"\n- 在 arm 周围画一个小的 \"displacement cloud\"：一个极小的点簇（< 0.1mm 范围），强调微小抖动\n- Obstacle 与 arm 之间留有间距，暗示\"未碰撞是因为未到达，不是因为躲避\"\n\n## Panel B: CAR_f Filtering\n\n### Elements\n- **Flow diagram**（非 schematic，纯概念图）：\n  1. 顶部：一个大的标注框 \"CAR = 91.5%\"（CORAL 色），代表 Pi0+A1 的原始得分\n  2. 中间：一条水平虚线标注 τ_d = 0.1 mm（displacement threshold），线上标注 \"τ_d\"\n  3. 过滤过程：从 91.5% 框向下画一个漏斗/筛子符号，99.6% 的 episodes 被筛掉（以淡灰色 X 或删除线表示），只剩 ≈0% 通过\n  4. 底部：结果框 \"CAR_f ≈ 0%\"（`RED_TEXT`），极小\n- **Pi0.5 对比行**（下半部分）：\n  1. \"CAR = 26.8%\" → 经过同一 τ_d → \"CAR_f = 28.5%\"（箭头 + \"unchanged\" 标注）\n  2. 用蓝色，与上方 coral 形成对比\n\n### Colors\n- Pi0+A1 flow: `CORAL (#E8846B)` → `RED_TEXT (#C0392B)`\n- Pi0.5 flow: `BLUE (#0072B2)` → `BLUE (#0072B2)`\n- τ_d 线: `#AAAAAA` 虚线\n- 筛掉的 episodes: `#CCCCCC` + 删除线\n- 漏斗/filter 符号: `#666666`\n- 背景: 白色\n\n### Annotations\n- τ_d 线旁: \"$\\tau_d$ = 0.1 mm\"（`#666666`，小字）\n- Pi0+A1 行: \"99.6% filtered\" 标注在筛掉的部分旁（`GRAY_TEXT`）\n- Pi0.5 行: \"all episodes pass\" 或 \"0% filtered\"（`BLUE`，小字）\n- 大号红色文字: **\"91.5% → ≈ 0%\"** 作为 panel 的视觉焦点\n- Panel 标题: **(b) CAR_f Filtering**\n\n### Visual Cues\n- 用从上到下的视觉 flow（不是左右），与 panel A/C 的静态 schematic 形成节奏变化\n- 漏斗收窄效果：Pi0+A1 行的漏斗出口极窄（≈0%），Pi0.5 行的漏斗出口几乎等宽（unchanged）\n- 可选：用 stacked bar 替代漏斗——上方是满条（91.5%），下方几乎为零，中间一个大红色向下箭头\n\n### 备选方案：简化版\n如果漏斗图过于复杂，可改为：\n- 两行 before/after bar chart（类似现有 panel a + panel c 的压缩版）\n- 中间一条 τ_d 水平线作为分界\n- 用大箭头连接 before → after\n\n## Panel C: Genuine Safety\n\n### Elements\n- **Robot arm schematic**（侧视简化）：同 Panel A 的 2-link arm，但以实线、饱和色绘制，关节处有运动弧线标记。\n- **Motion trajectory**：从 arm 末端出发的弧形轨迹（实线，BLUE），绕过 obstacle，到达 goal 位置。用 3-4 个等距的小三角形箭头标示运动方向。\n- **Obstacle**：与 Panel A 相同形状和位置的障碍物，但 arm 的轨迹明确绕过了它。\n- **Displacement bar**（底部）：水平条形图，填充量显著（> 288mm），用 BLUE 色。条形旁标注 \"> 288 mm\"。\n- **Metric badge**：panel 顶部或 arm 旁，标注 \"CAR = 26.8%\" 和 \"TSR = 74.7%\"。\n\n### Colors\n- Arm body: `BLUE (#0072B2)` 实线，饱和\n- Trajectory: `BLUE (#0072B2)` 实线，alpha=0.6，宽度 1.5pt\n- Trajectory 箭头: `BLUE_DARK (#005A8D)`\n- Obstacle: 与 Panel A 相同（`#E8846B` 半透明 + `#C0603E` 边框），保持一致性\n- Displacement bar: `BLUE (#0072B2)`\n- Goal 标记: `#009E73`（teal-green，成功色）\n- TSR badge: `BLUE (#0072B2)`\n\n### Annotations\n- Trajectory 旁: \"> 288 mm\" 标注，指向轨迹弧长\n- 底部 displacement bar 旁: \"> 288 mm\"（`BLUE`）\n- Badge: \"CAR = 26.8%\" + \"TSR = 74.7%\"（BLUE，加粗）\n- Panel 标题: **(c) Genuine Safety**\n\n### Visual Cues\n- Arm 用实线 + 高饱和度，与 Panel A 的虚线/淡色形成鲜明对比\n- 轨迹弧线清晰可见，传达\"机器人在主动运动\"\n- Obstacle 和 arm 之间有明确的安全裕度（clearance），但轨迹确实从附近经过（不是远离）\n- Goal 位置用绿色星号或圆点标记\n\n## A vs C 对称设计\n\n| 维度 | Panel A (Fake) | Panel C (Genuine) |\n|------|---------------|------------------|\n| Arm 线型 | 虚线，低 alpha | 实线，高饱和度 |\n| Arm 颜色 | 灰色 (#D0D0D0) | 蓝色 (BLUE) |\n| 运动轨迹 | 无（静止） | 弧形实线 + 箭头 |\n| Obstacle 交互 | 无接触（因为没动） | 主动绕过 |\n| Displacement bar | 几乎为空 | 满或近满 |\n| 色调 | Coral/Red（警告） | Blue/Green（正面） |\n| 情绪 | \"这是假的\" | \"这是真的\" |\n\n## Technical Notes\n\n### 实现方式\n- **推荐：matplotlib schematic**（与现有 figure pipeline 一致）\n  - Robot arm: `matplotlib.patches.FancyArrowPatch` + `Circle` 关节\n  - Trajectory: `matplotlib.path.Path` + `PathPatch` 贝塞尔曲线\n  - Obstacle: `Rectangle` 或 `FancyBboxPatch`\n  - Displacement bar: `barh` 在子 axes 中\n  - Flow diagram (Panel B): `FancyArrowPatch` + `FancyBboxPatch` + `Text`\n- **备选：tikz**（更精确的 schematic 控制，但脱离现有 pipeline）\n- **不推荐 PaperBanana**：此图需要精确的数据标注和对称布局，PaperBanana 更适合自由形式概念图\n\n### 尺寸约束\n- 总宽度: 5.5 inches（CoRL 单栏 `\\linewidth`）\n- 总高度: 2.5–2.8 inches（比当前版本略高以容纳 schematic）\n- 3 panels width_ratios: [1, 1.2, 1]\n- DPI: 300, 输出 PDF + PNG\n\n### 与现有 figures 的一致性\n- **字体**: DejaVu Sans（与 fig1_teaser.py, plot_fig2.py 等一致）\n- **配色**: CORAL/BLUE 双色系（与全文一致，Pi0+A1=coral, Pi0.5=blue）\n- **spines**: 仅保留 left + bottom（`axes.spines.top/right = False`）\n- **stroke 效果**: 文字白色描边 `pe.withStroke(linewidth=2.5)`（与全文一致）\n- **Panel 标题**: 加粗，10.5pt，格式 \"(a) Title\"\n- **Metric 标注**: 8.5pt 加粗，与 fig1_teaser.py 现有风格一致\n\n### 与当前版本的差异\n当前 fig1_teaser.py 是纯数据图（bar + lollipop）。新设计将 Panel A 和 C 替换为 **robot arm schematic**，Panel B 从 displacement lollipop 替换为 **filtering flow diagram**。保留底部 displacement bar 作为定量锚点，但主体视觉从\"图表\"转变为\"概念示意图+数据\"。\n\n### 降级方案\n如果 robot arm schematic 在 matplotlib 中实现效果不佳（线条不够清晰/美观），可降级为：\n- Panel A/C: 保留当前 bar chart，但在 bar 上方叠加简化的 arm icon（小尺寸，装饰性）\n- Panel B: 保留当前 lollipop，但增加 flow 箭头连接到 Panel C\n\n## Caption Draft\n\n> **The fake safety problem in VLA collision avoidance.** (a) Pi0+A1 achieves CAR = 91.5\\% by remaining frozen—displacement stays below 0.1\\,mm in 99.6\\% of ``safe'' episodes (TSR = 0\\%). (b) CAR$_f$ applies a displacement threshold $\\tau_d$: Pi0+A1's score collapses from 91.5\\% to $\\approx$\\,0\\%, while Pi0.5 is unaffected. (c) Pi0.5 exhibits genuine avoidance—actively navigating around obstacles with displacement $>$\\,288\\,mm (CAR = 26.8\\%, TSR = 74.7\\%). \\emph{The robot is frozen, not safe.}\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/fig1_teaser_design.md",
    "content": "# Figure 1 Teaser Design\n\n## Narrative Intent\n\nA frozen robot scores high on CAR not because it is safe, but because it never moves—CAR_f exposes the illusion by filtering action-collapsed episodes.\n\n## Layout\n\n```\n┌─────────────────────────────────────────────────────────────────┐\n│  (a) Fake Safety          (b) CAR_f Filter       (c) Genuine   │\n│                                                      Safety    │\n│ ┌──────────────┐   ┌─────────────────────┐   ┌──────────────┐ │\n│ │              │   │                     │   │   ╭─trajectory │\n│ │  ┌─arm─┐    │   │  ┌───────────────┐  │   │  ╭╯  ╲        │\n│ │  │ (frozen) │   │  │ 91.5%  ──────►│  │   │ arm    ╲      │\n│ │  │  ·       │   │  │  episodes     │  │   │  ╲   obstacle  │\n│ │  │  ·       │   │  │       ┌───┐   │  │   │   ╰──►goal     │\n│ │  └──┘  obs  │   │  │  τ_d  │ ≈0%│  │  │   │              │\n│ │              │   │  └───────┴───┘   │  │   │              │\n│ ├──────────────┤   │                     │   ├──────────────┤ │\n│ │▓░░░░░░░░░░░░│   │  Pi0.5: 26.8%→28.5% │   │▓▓▓▓▓▓▓▓▓▓▓▓▓│ │\n│ │ <0.1mm      │   │  (unchanged)         │   │ >288mm       │ │\n│ └──────────────┘   └─────────────────────┘   └──────────────┘ │\n│                                                                 │\n│  CAR=91.5%  TSR=0%    91.5% ──τ_d──► ≈0%    CAR=26.8% TSR=74.7%│\n└─────────────────────────────────────────────────────────────────┘\n```\n\n- 总尺寸: 5.5 × 2.8 inches（单栏宽度，略高于当前版本以容纳 schematic）\n- 三列 width_ratios=[1, 1.2, 1]，中间 panel 稍宽以容纳 flow 图\n- 每列分上下两区：上区 schematic/flow（~70% 高度），下区 displacement 条（~30% 高度）\n\n## Panel A: Fake Safety\n\n### Elements\n- **Robot arm schematic**（侧视简化）：2-link arm 以灰色/淡色绘制，关节处用圆点标记。手臂完全静止——用虚线轮廓 + \"frozen\" 雪花/锁标记暗示不动。无运动轨迹。\n- **Obstacle**：红色/橙色立方体或圆柱体，位于 arm 工作空间内但未接触（因为 arm 从未伸出）。\n- **Displacement bar**（底部）：水平条形图，填充量极小（< 0.1mm），用 CORAL 色。条形旁标注 \"< 0.1 mm\"。背景为浅灰色 action-collapse zone。\n- **Metric badge**：panel 顶部或 arm 旁，标注 \"CAR = 91.5%\" 和 \"TSR = 0%\"。\n\n### Colors\n- Arm body: `#D0D0D0`（浅灰，暗示无生命/冻结）\n- Arm outline: `CORAL (#E8846B)` 虚线，关联 Pi0+A1 配色\n- Obstacle: `#E8846B` 半透明填充 + `#C0603E` 边框\n- Displacement bar: `CORAL (#E8846B)`\n- Collapse zone bg: `#F0F0F0`\n- TSR=0% 文字: `RED_TEXT (#C0392B)`\n- Panel 标题/badge: `CORAL_DARK (#C0603E)`\n\n### Annotations\n- Arm 上方: 虚线框 + 文字 **\"frozen\"**（或锁图标 🔒，如果 DejaVu Sans 支持）\n- 底部 displacement bar 旁: \"< 0.1 mm\" (小字，`CORAL_DARK`)\n- 右下角 badge: \"CAR = 91.5%\" (大号加粗)，下方 \"TSR = 0%\" (`RED_TEXT`)\n- Panel 标题: **(a) Fake Safety**\n\n### Visual Cues\n- Arm 用 dashed line + 低 alpha (0.4) 传递\"这不是真正的运动\"\n- 在 arm 周围画一个小的 \"displacement cloud\"：一个极小的点簇（< 0.1mm 范围），强调微小抖动\n- Obstacle 与 arm 之间留有间距，暗示\"未碰撞是因为未到达，不是因为躲避\"\n\n## Panel B: CAR_f Filtering\n\n### Elements\n- **Flow diagram**（非 schematic，纯概念图）：\n  1. 顶部：一个大的标注框 \"CAR = 91.5%\"（CORAL 色），代表 Pi0+A1 的原始得分\n  2. 中间：一条水平虚线标注 τ_d = 0.1 mm（displacement threshold），线上标注 \"τ_d\"\n  3. 过滤过程：从 91.5% 框向下画一个漏斗/筛子符号，99.6% 的 episodes 被筛掉（以淡灰色 X 或删除线表示），只剩 ≈0% 通过\n  4. 底部：结果框 \"CAR_f ≈ 0%\"（`RED_TEXT`），极小\n- **Pi0.5 对比行**（下半部分）：\n  1. \"CAR = 26.8%\" → 经过同一 τ_d → \"CAR_f = 28.5%\"（箭头 + \"unchanged\" 标注）\n  2. 用蓝色，与上方 coral 形成对比\n\n### Colors\n- Pi0+A1 flow: `CORAL (#E8846B)` → `RED_TEXT (#C0392B)`\n- Pi0.5 flow: `BLUE (#0072B2)` → `BLUE (#0072B2)`\n- τ_d 线: `#AAAAAA` 虚线\n- 筛掉的 episodes: `#CCCCCC` + 删除线\n- 漏斗/filter 符号: `#666666`\n- 背景: 白色\n\n### Annotations\n- τ_d 线旁: \"$\\tau_d$ = 0.1 mm\"（`#666666`，小字）\n- Pi0+A1 行: \"99.6% filtered\" 标注在筛掉的部分旁（`GRAY_TEXT`）\n- Pi0.5 行: \"all episodes pass\" 或 \"0% filtered\"（`BLUE`，小字）\n- 大号红色文字: **\"91.5% → ≈ 0%\"** 作为 panel 的视觉焦点\n- Panel 标题: **(b) CAR_f Filtering**\n\n### Visual Cues\n- 用从上到下的视觉 flow（不是左右），与 panel A/C 的静态 schematic 形成节奏变化\n- 漏斗收窄效果：Pi0+A1 行的漏斗出口极窄（≈0%），Pi0.5 行的漏斗出口几乎等宽（unchanged）\n- 可选：用 stacked bar 替代漏斗——上方是满条（91.5%），下方几乎为零，中间一个大红色向下箭头\n\n### 备选方案：简化版\n如果漏斗图过于复杂，可改为：\n- 两行 before/after bar chart（类似现有 panel a + panel c 的压缩版）\n- 中间一条 τ_d 水平线作为分界\n- 用大箭头连接 before → after\n\n## Panel C: Genuine Safety\n\n### Elements\n- **Robot arm schematic**（侧视简化）：同 Panel A 的 2-link arm，但以实线、饱和色绘制，关节处有运动弧线标记。\n- **Motion trajectory**：从 arm 末端出发的弧形轨迹（实线，BLUE），绕过 obstacle，到达 goal 位置。用 3-4 个等距的小三角形箭头标示运动方向。\n- **Obstacle**：与 Panel A 相同形状和位置的障碍物，但 arm 的轨迹明确绕过了它。\n- **Displacement bar**（底部）：水平条形图，填充量显著（> 288mm），用 BLUE 色。条形旁标注 \"> 288 mm\"。\n- **Metric badge**：panel 顶部或 arm 旁，标注 \"CAR = 26.8%\" 和 \"TSR = 74.7%\"。\n\n### Colors\n- Arm body: `BLUE (#0072B2)` 实线，饱和\n- Trajectory: `BLUE (#0072B2)` 实线，alpha=0.6，宽度 1.5pt\n- Trajectory 箭头: `BLUE_DARK (#005A8D)`\n- Obstacle: 与 Panel A 相同（`#E8846B` 半透明 + `#C0603E` 边框），保持一致性\n- Displacement bar: `BLUE (#0072B2)`\n- Goal 标记: `#009E73`（teal-green，成功色）\n- TSR badge: `BLUE (#0072B2)`\n\n### Annotations\n- Trajectory 旁: \"> 288 mm\" 标注，指向轨迹弧长\n- 底部 displacement bar 旁: \"> 288 mm\"（`BLUE`）\n- Badge: \"CAR = 26.8%\" + \"TSR = 74.7%\"（BLUE，加粗）\n- Panel 标题: **(c) Genuine Safety**\n\n### Visual Cues\n- Arm 用实线 + 高饱和度，与 Panel A 的虚线/淡色形成鲜明对比\n- 轨迹弧线清晰可见，传达\"机器人在主动运动\"\n- Obstacle 和 arm 之间有明确的安全裕度（clearance），但轨迹确实从附近经过（不是远离）\n- Goal 位置用绿色星号或圆点标记\n\n## A vs C 对称设计\n\n| 维度 | Panel A (Fake) | Panel C (Genuine) |\n|------|---------------|------------------|\n| Arm 线型 | 虚线，低 alpha | 实线，高饱和度 |\n| Arm 颜色 | 灰色 (#D0D0D0) | 蓝色 (BLUE) |\n| 运动轨迹 | 无（静止） | 弧形实线 + 箭头 |\n| Obstacle 交互 | 无接触（因为没动） | 主动绕过 |\n| Displacement bar | 几乎为空 | 满或近满 |\n| 色调 | Coral/Red（警告） | Blue/Green（正面） |\n| 情绪 | \"这是假的\" | \"这是真的\" |\n\n## Technical Notes\n\n### 实现方式\n- **推荐：matplotlib schematic**（与现有 figure pipeline 一致）\n  - Robot arm: `matplotlib.patches.FancyArrowPatch` + `Circle` 关节\n  - Trajectory: `matplotlib.path.Path` + `PathPatch` 贝塞尔曲线\n  - Obstacle: `Rectangle` 或 `FancyBboxPatch`\n  - Displacement bar: `barh` 在子 axes 中\n  - Flow diagram (Panel B): `FancyArrowPatch` + `FancyBboxPatch` + `Text`\n- **备选：tikz**（更精确的 schematic 控制，但脱离现有 pipeline）\n- **不推荐 PaperBanana**：此图需要精确的数据标注和对称布局，PaperBanana 更适合自由形式概念图\n\n### 尺寸约束\n- 总宽度: 5.5 inches（CoRL 单栏 `\\linewidth`）\n- 总高度: 2.5–2.8 inches（比当前版本略高以容纳 schematic）\n- 3 panels width_ratios: [1, 1.2, 1]\n- DPI: 300, 输出 PDF + PNG\n\n### 与现有 figures 的一致性\n- **字体**: DejaVu Sans（与 fig1_teaser.py, plot_fig2.py 等一致）\n- **配色**: CORAL/BLUE 双色系（与全文一致，Pi0+A1=coral, Pi0.5=blue）\n- **spines**: 仅保留 left + bottom（`axes.spines.top/right = False`）\n- **stroke 效果**: 文字白色描边 `pe.withStroke(linewidth=2.5)`（与全文一致）\n- **Panel 标题**: 加粗，10.5pt，格式 \"(a) Title\"\n- **Metric 标注**: 8.5pt 加粗，与 fig1_teaser.py 现有风格一致\n\n### 与当前版本的差异\n当前 fig1_teaser.py 是纯数据图（bar + lollipop）。新设计将 Panel A 和 C 替换为 **robot arm schematic**，Panel B 从 displacement lollipop 替换为 **filtering flow diagram**。保留底部 displacement bar 作为定量锚点，但主体视觉从\"图表\"转变为\"概念示意图+数据\"。\n\n### 降级方案\n如果 robot arm schematic 在 matplotlib 中实现效果不佳（线条不够清晰/美观），可降级为：\n- Panel A/C: 保留当前 bar chart，但在 bar 上方叠加简化的 arm icon（小尺寸，装饰性）\n- Panel B: 保留当前 lollipop，但增加 flow 箭头连接到 Panel C\n\n## Caption Draft\n\n> **The fake safety problem in VLA collision avoidance.** (a) Pi0+A1 achieves CAR = 91.5\\% by remaining frozen—displacement stays below 0.1\\,mm in 99.6\\% of ``safe'' episodes (TSR = 0\\%). (b) CAR$_f$ applies a displacement threshold $\\tau_d$: Pi0+A1's score collapses from 91.5\\% to $\\approx$\\,0\\%, while Pi0.5 is unaffected. (c) Pi0.5 exhibits genuine avoidance—actively navigating around obstacles with displacement $>$\\,288\\,mm (CAR = 26.8\\%, TSR = 74.7\\%). \\emph{The robot is frozen, not safe.}\n"
  }
}
````

</details>

---

### Tool result

_source line 58 · 2026-05-27T02:00:17.682540+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/fig1_teaser_design.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-27T02:00:17.682771+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "fig1_teaser_design",
  "type": "intermediate",
  "description": "Figure 1 teaser conceptual design doc — schematic robot arm layout with fake/genuine safety contrast and CAR_f filtering flow",
  "project": "diff_collision_sdf",
  "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/fig1_teaser_design.md",
  "tags": "['figure', 'teaser', 'design', 'paper']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "fig1_teaser_design",
    "type": "intermediate",
    "description": "Figure 1 teaser conceptual design doc — schematic robot arm layout with fake/genuine safety contrast and CAR_f filtering flow",
    "project": "diff_collision_sdf",
    "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/fig1_teaser_design.md",
    "tags": "['figure', 'teaser', 'design', 'paper']"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-27T02:00:17.683012+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260527_c724a9\", \"name\": \"fig1_teaser_design\", \"type\": \"intermediate\", \"description\": \"Figure 1 teaser conceptual design doc — schematic robot arm layout with fake/genuine safety contrast and CAR_f filtering flow\", \"path\": \"projects/diff_collision_sdf/artifacts/_project/intermediate/fig1_teaser_design.md\", \"url\": null, \"project\": \"diff_collision_sdf\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-27T02:00:07.679827+00:00\", \"tags\": [\"figure\", \"teaser\", \"design\", \"paper\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_fig1_teaser_design_20260527T015636",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-27T02:00:17.683270+00:00_

设计文档已产出并注册：`artifacts/fig1_teaser_design.md`

核心设计决策：

1. **Panel A/C 从 bar chart → robot arm schematic**：frozen arm（虚线/灰色/静止）vs active arm（实线/蓝色/弧形轨迹），底部保留 displacement bar 作为定量锚点
2. **Panel B 从 lollipop → filtering flow diagram**：垂直 flow 展示 τ_d 如何将 Pi0+A1 的 91.5% 筛到 ≈0%，Pi0.5 不受影响
3. **A/C 对称设计**：虚线 vs 实线、灰色 vs 蓝色、静止 vs 运动、空 bar vs 满 bar，每个维度都在强化 frozen vs genuine 的对比
4. **Caption 改进**：末尾加入论文核心口号 *"The robot is frozen, not safe."* 作为 punch line

实现建议 matplotlib schematic（与现有 pipeline 一致），降级方案也已包含。等 Director 审核后再执行渲染。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_fig1_teaser_design_20260527T015636"
}
```

</details>

---
