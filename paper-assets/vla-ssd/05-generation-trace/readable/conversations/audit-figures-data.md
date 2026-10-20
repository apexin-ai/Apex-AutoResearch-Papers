# audit figures data

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 83
- **Recorded user turns:** 0
- **Tool calls:** 41
- **Original source:** `logs/chats/worker_audit_figures_data_20260529T050826.jsonl`
- **Structured JSON:** [`02769d18a55768994037.json`](../../sessions/02/02769d18a55768994037.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

83 recorded events

### Tool call

_source line 1 · 2026-05-29T05:18:07.833536+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_*.py /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/gen_fig_*.py 2>/dev/null",
  "description": "List all plot and gen_fig scripts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_*.py /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/gen_fig_*.py 2>/dev/null",
    "description": "List all plot and gen_fig scripts"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-29T05:18:07.833980+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/gen_fig_matrix_heatmap.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_action_r2_threecond.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_claim_evidence.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_counterfactual_bar.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_dose_response.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_l1_attention.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_label_permutation.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_multi_layer_attention.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_nlp_control_overlay.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_overview.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_r2_collapse.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_rsa_perlayer.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_teaser.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_training_dynamics.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-29T05:18:07.834238+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-29T05:18:07.834412+00:00_

docs/paper/corl_example.tex
artifacts/dream_reports/dream_20260515T222933/best/paper.tex
artifacts/dream_reports/dream_20260515T222933/median/paper.tex
artifacts/dream_reports/dream_20260515T222933/worst/paper.tex
artifacts/dream_reports/dream_20260516T011810/best/paper.tex
artifacts/dream_reports/dream_20260516T011810/median/paper.tex
artifacts/dream_reports/dream_20260516T011810/worst/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/method_a6c062.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/introduction_fccb56.tex
docs/paper-a-plus-backup/abstract.tex
docs/paper-a-plus-backup/appendix.tex
docs/paper-a-plus-backup/conclusion.tex
docs/paper-a-plus-backup/corl_example.tex
docs/paper-a-plus-backup/discussion.tex
docs/paper-a-plus-backup/experiments.tex
docs/paper-a-plus-backup/introduction.tex
docs/paper-a-plus-backup/main.tex
docs/paper-a-plus-backup/method.tex
docs/paper-a-plus-backup/related_work.tex
artifacts/_project/report/cross_arch_r2_table.tex
artifacts/phi3v_r2_action_probe/cross_arch_r2_table.tex
artifacts/phi3v_r2_action_probe/cross_arch_r2_2x2_table.tex
artifacts/phi3v_r2_action_probe/cross_arch_r2_2x2_summary.tex
artifacts/_project/paper/cross_arch_r2_2x2_table.tex
artifacts/_project/paper/cross_arch_r2_2x2_summary.tex
artifacts/dream_reports/dream_20260522T021705/best/paper.tex
artifacts/dream_reports/dream_20260522T021705/median/paper.tex
artifacts/dream_reports/dream_20260522T021705/worst/paper.tex
paper/main.tex
artifacts/dream_reports/dream_20260527T022433/best/paper.tex
artifacts/dream_reports/dream_20260527T022433/median/paper.tex
artifacts/dream_reports/dream_20260527T022433/worst/paper.tex
docs/paper/abstract.tex
docs/paper/main.tex
docs/paper/method.tex
docs/paper/related_work.tex
docs/paper/introduction.tex
docs/paper/experiments.tex
docs/paper/appendix.tex
docs/paper/discuss
…[truncated 7 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-29T05:18:07.834577+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-29T05:18:07.834750+00:00_

artifacts/probe_design_plan.md
artifacts/_project/intermediate/probe_dryrun_dinov2_results.txt
artifacts/dinov2_baseline/data/dinov2_subtask_auc_results.txt
artifacts/mvp_probe_trained/report/mvp_probe_analysis.md
artifacts/_project/report/action_probe_design.md
artifacts/action_probe_design.md
artifacts/_project/report/literature_map_probing.md
artifacts/literature_map_probing.md
artifacts/_project/report/controlb_report.md
artifacts/_project/report/controlb_analysis.md
artifacts/mvp_controlb_trained/report/controlb_analysis.md
artifacts/controlb_analysis/controlb_analysis.md
artifacts/_project/report/libero_goal_feasibility.md
artifacts/libero_goal_feasibility.md
artifacts/_project/report/layer_stability_analysis.md
artifacts/layer_stability_analysis.md
artifacts/openvla_libero_goal_compat.md
artifacts/pipeline_audit_libero_goal.md
artifacts/_project/report/literature_survey_instruction_probing.md
artifacts/literature_survey_instruction_probing.md
artifacts/literature_map.yaml
artifacts/_project/chart/perlayer_rsa_comparison_chart_info.txt
artifacts/dream_reports/dream_20260515T222933/logs/phase1_attempt0.log
artifacts/_project/data/perlayer_rsa_summary.txt
artifacts/dream_reports/dream_20260515T222933/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260515T222933/logs/phase2_median_attempt0.log
artifacts/_project/intermediate/figure_data_manifest.txt
artifacts/dream_reports/dream_20260515T222933/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260515T222933/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260515T222933/best/experiment_data.json
artifacts/dream_reports/dream_20260515T222933/best/paper_framing.md
artifacts/dream_reports/dream_20260515T222933/best/paper.tex
artifacts/dream_reports/dream_20260515T222933/best/paper.aux
artifacts/dream_reports/dream_20260515T222933/best/paper.out
artifacts/dream_reports/dream_20260515T222933/best/paper.pdf
artifacts/dream_reports/dream_20260515T222933/best/paper.log
artifacts/dr
…[truncated 4267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-29T05:18:07.834950+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-29T05:18:07.835246+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\looseness=-1
8	We apply all three analyses (\S\ref{sec:cross_arch_analyses}) to the $3 \times 4$ architecture-suite matrix (10 of 12 cells filled; Figure~\ref{fig:result_matrix}, Table~\ref{tab:cross_arch_matrix}).
9	For trained models, counterfactual sensitivity uses Cohen's $d$ on action MSE; reference VLMs use cosine distance on hidden representations (different scale; \S\ref{sec:cf_sensitivity}).
10	OpenVLA's OXE-pretrained checkpoint produces actions, permitting same-metric comparison (Bonferroni correction in Appendix~\ref{sec:bonferroni_correction}).
11	
12	%------------------------------------------------------------------
13	\subsection{OpenVLA: Motivating Single-Architecture Analysis}
14	\label{sec:openvla_routing}
15	
16	\looseness=-1
17	We first establish core phenomena on OpenVLA (Appendix~\ref{sec:openvla_deepdive_appendix}).
18	At L1, instruction-dominant heads form a gradient: random initialization 0/32, Llama-2 base 9/32, VLA-trained 24/32.
19	Per-layer $R^2$ probing (Figure~\ref{fig:action_r2_threecond}) shows the trained model peaks at L9 ($R^2 = 0.643$), Llama-2 base declines from L0, and random initialization collapses at deep layers.
20	All three share L0 ($R^2 = 0.645$); divergence arises from Transformer processing, with VLA training building on pretrained scaffold rather than constructing representations from scratch.
21	
22	\begin{figure}[t]
23	\centering
24	\includegraphics[width=0.8\columnwidth]{figures/fig_action_r2_threecond.pdf}
25	\caption{Per-layer action-probe $R^2$ for three OpenVLA conditions (3 seeds, mean $\pm$ std); all share L0 ($R^2 = 0.645$). Trained model peaks at L9, Llama-2 base declines from L0, random initialization collapses at deep layers.}
26	\label{fig:action_r2_threecond}
27	\end{figure}
28	
29	\begin{figure}[t]
30	\centering
31	\includegraphics[width=\columnwidth]{figures/fig_counterfactual_bar.pdf}
32	
…[truncated 8473 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-29T05:18:07.835427+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-29T05:18:07.835558+00:00_

File content (32210 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-29T05:18:07.835679+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_counterfactual_bar.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_counterfactual_bar.py"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-29T05:18:07.835861+00:00_

1	#!/usr/bin/env python3
2	import matplotlib
3	matplotlib.use('Agg')
4	import matplotlib.pyplot as plt
5	plt.rcParams.update({
6	    'font.family': 'serif',
7	    'font.serif': ['Liberation Serif'],
8	    'pdf.fonttype': 42,
9	    'ps.fonttype': 42,
10	    'mathtext.fontset': 'custom',
11	    'mathtext.rm': 'Liberation Serif',
12	    'mathtext.it': 'Liberation Serif:italic',
13	    'mathtext.bf': 'Liberation Serif:bold',
14	})
15	import numpy as np
16	import os
17	
18	COLORS = {
19	    'empty': '#F4C28C',
20	    'wrong': '#9DC4E6',
21	    'shuffled': '#A3D4A8',
22	    'paraphrased': '#D4AACC',
23	}
24	EDGE = {
25	    'empty': '#D9A56C',
26	    'wrong': '#7AA4C8',
27	    'shuffled': '#7CB888',
28	    'paraphrased': '#B88EAE',
29	}
30	
31	conditions = ['empty', 'wrong', 'shuffled', 'paraphrased']
32	cond_labels = ['E', 'W', 'S', 'P']
33	n_cond = len(conditions)
34	
35	# ── Panel A data: Cohen's d ──
36	cohens_d = {
37	    'OV-G': [1.17, 1.18, 1.10, 1.00],
38	    'OV-S': [1.17, 0.89, 0.98, 0.81],
39	    'OV-O': [1.21, 1.19, 1.12, 0.90],
40	    'OV-L': [0.51, 0.55, 0.57, 0.45],
41	    'TV-G': [1.52, 1.40, 1.34, 1.21],
42	    'TV-S': [1.33, 1.17, 1.30, 1.18],
43	    'TV-O': [1.21, 1.06, 1.16, 0.97],
44	    'TV-L': [1.47, 1.42, 1.39, 1.16],
45	}
46	
47	# ── Panel B data: Cosine distance ──
48	cosine_dist = {
49	    'G':    [1.0,    1.0,    1.0,    1.0],
50	    'S':    [0.24,   0.275,  0.12,   0.03],
51	    'G.':   [0.1530, 0.0160, 0.0839, 0.0043],
52	    'S.':   [0.1805, 0.0046, 0.1395, 0.0044],
53	    'O':    [0.1850, 0.0044, 0.0977, 0.0052],
54	    'L':    [0.1734, 0.0221, 0.1204, 0.0070],
55	    'G..':  [0.0814, 0.0143, 0.0332, 0.0041],
56	    'S..':  [0.0807, 0.0020, 0.0313, 0.0047],
57	}
58	panelB_display = ['G', 'S', 'G', 'S', 'O', 'L', 'G', 'S']
59	panelB_regions = [
60	    ('NORA\n(trained)', 0, 2),
61	    ('Phi-3-Vision\n(ref)', 2, 6),
62	    ('Qwen2.5-VL\n(ref)', 6, 8),
63	]
64	
65	fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.0, 3.0),
66	                     
…[truncated 4483 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-29T05:18:07.836087+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_action_r2_threecond.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_action_r2_threecond.py"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-29T05:18:07.836257+00:00_

1	#!/usr/bin/env python3
2	"""fig_action_r2_threecond: Per-layer action-probe R² for three OpenVLA conditions."""
3	import matplotlib
4	matplotlib.use('Agg')
5	import matplotlib.pyplot as plt
6	plt.rcParams.update({
7	    'font.family': 'serif',
8	    'font.serif': ['Liberation Serif'],
9	    'pdf.fonttype': 42,
10	    'ps.fonttype': 42,
11	    'mathtext.fontset': 'custom',
12	    'mathtext.rm': 'Liberation Serif',
13	    'mathtext.it': 'Liberation Serif:italic',
14	    'mathtext.bf': 'Liberation Serif:bold',
15	})
16	import numpy as np
17	import os
18	
19	layers = np.arange(32)
20	
21	trained_mean = np.array([0.6451, 0.6429, 0.6221, 0.6211, 0.6386, 0.6304, 0.6421, 0.6339,
22	    0.6362, 0.6434, 0.6245, 0.6245, 0.6205, 0.6348, 0.6282, 0.6391,
23	    0.6246, 0.6185, 0.6008, 0.5961, 0.5907, 0.5946, 0.5899, 0.5490,
24	    0.5711, 0.5696, 0.5557, 0.5221, 0.4963, 0.5153, 0.5186, 0.4724])
25	trained_std = np.array([0.0084, 0.0072, 0.0061, 0.0226, 0.0073, 0.0144, 0.0053, 0.0084,
26	    0.0184, 0.0137, 0.0162, 0.0182, 0.0084, 0.0039, 0.0067, 0.0081,
27	    0.0132, 0.0117, 0.0341, 0.0063, 0.0187, 0.0149, 0.0050, 0.0800,
28	    0.0205, 0.0161, 0.0354, 0.0679, 0.0646, 0.0451, 0.0034, 0.0671])
29	
30	llama2base_mean = np.array([0.6451, 0.6276, 0.6204, 0.6287, 0.6279, 0.6220, 0.6271, 0.6321,
31	    0.6202, 0.6271, 0.6287, 0.6284, 0.6344, 0.6136, 0.6053, 0.6085,
32	    0.6137, 0.6062, 0.6117, 0.6032, 0.5788, 0.5875, 0.5860, 0.5905,
33	    0.5810, 0.5690, 0.5755, 0.5689, 0.5607, 0.5814, 0.5619, 0.5571])
34	llama2base_std = np.array([0.0084, 0.0098, 0.0088, 0.0115, 0.0197, 0.0076, 0.0106, 0.0041,
35	    0.0077, 0.0078, 0.0086, 0.0086, 0.0131, 0.0128, 0.0159, 0.0038,
36	    0.0018, 0.0069, 0.0225, 0.0148, 0.0278, 0.0184, 0.0073, 0.0047,
37	    0.0117, 0.0112, 0.0089, 0.0274, 0.0111, 0.0068, 0.0027, 0.0111])
38	
39	untrained_mean = np.array([0.6451, 0.5470, 0.5202, 0.5361, 0.5147, 0.3973, 0.5048, 0.5033,
40	    0.4985, 0.4416, -0.0924, 0.1408, 0.2114, 0.2237, 0.4157, 0.5108,
41	    0
…[truncated 2692 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-29T05:18:07.836403+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/gen_fig_matrix_heatmap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/gen_fig_matrix_heatmap.py"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-29T05:18:07.836810+00:00_

1	"""
2	Regenerate fig_matrix_heatmap.pdf with correct ΔR² values from Table 1.
3	Designed for display at 0.75\\textwidth (~4.9 inches) with minimal scaling.
4	"""
5	import matplotlib
6	matplotlib.use('Agg')
7	import matplotlib.pyplot as plt
8	plt.rcParams.update({
9	    'font.family': 'serif',
10	    'font.serif': ['Liberation Serif'],
11	    'pdf.fonttype': 42,
12	    'ps.fonttype': 42,
13	    'mathtext.fontset': 'custom',
14	    'mathtext.rm': 'Liberation Serif',
15	    'mathtext.it': 'Liberation Serif:italic',
16	    'mathtext.bf': 'Liberation Serif:bold',
17	})
18	import matplotlib.patches as patches
19	import numpy as np
20	
21	architectures = ['OpenVLA', 'TraceVLA', 'NORA']
22	suites = ['Goal', 'Spatial', 'Object', 'Long']
23	transition_types = {
24	    'OpenVLA': 'VLA→VLA',
25	    'TraceVLA': 'VLM→VLA',
26	    'NORA': 'VLM→VLA',
27	}
28	
29	data = {
30	    ('OpenVLA', 'Goal'): 0.086,
31	    ('OpenVLA', 'Spatial'): 0.037,
32	    ('OpenVLA', 'Object'): 0.037,
33	    ('OpenVLA', 'Long'): 0.033,
34	    ('TraceVLA', 'Goal'): 0.333,
35	    ('TraceVLA', 'Spatial'): 0.156,
36	    ('TraceVLA', 'Object'): 0.362,
37	    ('TraceVLA', 'Long'): 0.358,
38	    ('NORA', 'Goal'): 0.455,
39	    ('NORA', 'Spatial'): 0.308,
40	    ('NORA', 'Object'): None,
41	    ('NORA', 'Long'): None,
42	}
43	
44	THRESHOLD = 0.10
45	nrows = len(architectures)
46	ncols = len(suites)
47	
48	cell_w = 1.0
49	cell_h = 0.78
50	
51	fig_w = 5.2
52	fig_h = 2.8
53	fig, ax = plt.subplots(figsize=(fig_w, fig_h))
54	
55	# ── Custom colormap: paper-consistent teal-blue sequential palette ──
56	# Anchored to the paper's primary blue (#0077BB) from Tol's qualitative scheme.
57	# White → light sky → medium blue → deep blue.  Perceptually uniform in
58	# luminance so it degrades gracefully to grayscale and is safe for the three
59	# most common forms of color-vision deficiency (protanopia / deuteranopia /
60	# tritanopia).
61	from matplotlib.colors import LinearSegmentedColormap
62	_cmap_colors = [
63	    '#FFF
…[truncated 5606 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-29T05:18:07.837078+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_l1_attention.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_l1_attention.py"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-29T05:18:07.837279+00:00_

1	#!/usr/bin/env python3
2	"""fig_l1_attention: Horizontal bar chart of L1 instruction-dominant head counts."""
3	import matplotlib
4	matplotlib.use('Agg')
5	import matplotlib.pyplot as plt
6	plt.rcParams.update({
7	    'font.family': 'serif',
8	    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
9	    'pdf.fonttype': 42,
10	    'ps.fonttype': 42,
11	    'mathtext.fontset': 'custom',
12	    'mathtext.rm': 'Liberation Serif',
13	    'mathtext.it': 'Liberation Serif:italic',
14	    'mathtext.bf': 'Liberation Serif:bold',
15	})
16	import numpy as np
17	import os
18	
19	REF_COLOR = '#92C5DE'
20	TRAINED_COLOR = '#2166AC'
21	
22	architectures = ['OpenVLA', 'TraceVLA', 'NORA']
23	total_heads = [32, 32, 16]
24	ref_counts = [26, 32, 14]
25	trained_counts = [23, 29, 13]
26	
27	ref_frac = [r / t * 100 for r, t in zip(ref_counts, total_heads)]
28	trained_frac = [tr / t * 100 for tr, t in zip(trained_counts, total_heads)]
29	
30	fig, ax = plt.subplots(figsize=(3.8, 2.8))
31	
32	y = np.arange(len(architectures))
33	bar_h = 0.32
34	
35	bars_ref = ax.barh(y + bar_h/2, ref_frac, bar_h, color=REF_COLOR,
36	                    edgecolor='white', linewidth=0.5, label='Reference')
37	bars_tr = ax.barh(y - bar_h/2, trained_frac, bar_h, color=TRAINED_COLOR,
38	                   edgecolor='white', linewidth=0.5, label='Trained')
39	
40	for i in range(len(architectures)):
41	    ax.text(ref_frac[i] + 1.5, y[i] + bar_h/2,
42	            f'{ref_counts[i]}/{total_heads[i]}',
43	            va='center', ha='left', fontsize=10, color='#333333')
44	    ax.text(trained_frac[i] + 1.5, y[i] - bar_h/2,
45	            f'{trained_counts[i]}/{total_heads[i]}',
46	            va='center', ha='left', fontsize=10, color='#333333')
47	
48	ax.axvline(x=50, color='gray', linestyle='--', alpha=0.4, linewidth=1)
49	
50	ax.set_yticks(y)
51	ax.set_yticklabels(architectures, fontsize=12, fontweight='bold')
52	ax.set_xlabel('Fraction of Instruction-Dominant Heads', fontsize=11)
53	ax.set_xlim(0, 115)
54	ax.set
…[truncated 925 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-29T05:18:07.837465+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_dose_response.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_dose_response.py"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-29T05:18:07.837654+00:00_

1	#!/usr/bin/env python3
2	"""
3	Plot dose-response ablation curve (Figure 7, right panel).
4	
5	Shows Cohen's d (action MSE divergence) as a function of the number of
6	instruction-routing heads ablated, with 95% bootstrap confidence intervals.
7	
8	Output: fig_dose_response.pdf -> docs/paper/figures/ and artifacts/figures/paper/
9	"""
10	import matplotlib
11	matplotlib.use('Agg')
12	
13	# ── Font: Liberation Serif (metrically identical to Times New Roman) ──
14	matplotlib.rcParams['font.family'] = 'serif'
15	matplotlib.rcParams['font.serif'] = ['Liberation Serif', 'DejaVu Serif']
16	matplotlib.rcParams['mathtext.fontset'] = 'custom'
17	matplotlib.rcParams['mathtext.rm'] = 'Liberation Serif'
18	matplotlib.rcParams['mathtext.it'] = 'Liberation Serif:italic'
19	matplotlib.rcParams['mathtext.bf'] = 'Liberation Serif:bold'
20	matplotlib.rcParams['pdf.fonttype'] = 42
21	matplotlib.rcParams['ps.fonttype'] = 42
22	
23	import matplotlib.pyplot as plt
24	import numpy as np
25	import os
26	
27	plt.rcParams.update({
28	    'font.size': 11,
29	    'axes.titlesize': 13,
30	    'axes.labelsize': 12,
31	    'xtick.labelsize': 10,
32	    'ytick.labelsize': 10,
33	    'legend.fontsize': 10,
34	    'figure.dpi': 300,
35	    'savefig.dpi': 300,
36	    'savefig.bbox': 'tight',
37	    'savefig.pad_inches': 0.05,
38	    'axes.spines.top': False,
39	    'axes.spines.right': False,
40	})
41	
42	# ── Data ──
43	dose_n_heads = np.array([4, 8, 12, 16, 20, 24, 28, 32])
44	
45	dose_cohen_d = np.array([
46	    0.4815412850770599, 0.5082040281351017, 0.5600389203470800,
47	    0.5916585965181512, 0.5929310917614178, 0.6106991692401877,
48	    0.6192428662864000, 0.6385059409290664
49	])
50	
51	dose_ci_lower = np.array([
52	    0.4493981998904407, 0.4792767313857140, 0.5292064204814684,
53	    0.5593699517760848, 0.5591344210287796, 0.5784721762082760,
54	    0.5866794567732834, 0.6033325798526022
55	])
56	
57	dose_ci_upper = np.array([
58	    0.5111655435414341, 0.5407791509767693, 0.59287440392
…[truncated 2026 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-29T05:18:07.837819+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_label_permutation.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_label_permutation.py"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-29T05:18:07.837997+00:00_

1	#!/usr/bin/env python3
2	"""fig_label_permutation: Label permutation sanity check for appendix."""
3	import matplotlib
4	matplotlib.use('Agg')
5	import matplotlib.pyplot as plt
6	import numpy as np
7	import os
8	
9	plt.rcParams.update({
10	    'font.family': 'serif',
11	    'font.serif': ['Liberation Serif'],
12	    'pdf.fonttype': 42,
13	    'ps.fonttype': 42,
14	    'mathtext.fontset': 'custom',
15	    'mathtext.rm': 'Liberation Serif',
16	    'mathtext.it': 'Liberation Serif:italic',
17	    'mathtext.bf': 'Liberation Serif:bold',
18	    'font.size': 9,
19	    'axes.titlesize': 11,
20	    'axes.labelsize': 10,
21	    'xtick.labelsize': 9,
22	    'ytick.labelsize': 9,
23	    'legend.fontsize': 8,
24	    'figure.dpi': 300,
25	    'savefig.dpi': 300,
26	    'savefig.bbox': 'tight',
27	    'savefig.pad_inches': 0.05,
28	    'axes.spines.top': False,
29	    'axes.spines.right': False,
30	})
31	
32	# Data from controlb_analysis.md
33	conditions = ['Trained', 'Untrained']
34	real_rho   = [0.955, 0.933]
35	shuf_rho   = [0.0012, 0.0003]
36	
37	x = np.arange(len(conditions))
38	width = 0.30
39	
40	fig, ax = plt.subplots(figsize=(5, 4))
41	
42	bars1 = ax.bar(x - width/2, real_rho, width, label='Real labels',
43	               color='#4393C3', edgecolor='#2166AC', linewidth=0.8, zorder=3)
44	bars2 = ax.bar(x + width/2, shuf_rho, width, label='Shuffled labels',
45	               color='#FDB863', edgecolor='#E08214', linewidth=0.8, zorder=3)
46	
47	for bar, val in zip(bars1, real_rho):
48	    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
49	            f'{val:.3f}', ha='center', va='bottom', fontsize=9, fontweight='bold',
50	            color='#2166AC')
51	
52	for bar, val in zip(bars2, shuf_rho):
53	    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
54	            f'{val:.4f}', ha='center', va='bottom', fontsize=9, fontweight='bold',
55	            color='#E08214')
56	
57	ax.set_xticks(x)
58	ax.set_xticklabels(conditions)
59	ax.set_ylab
…[truncated 745 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-29T05:18:07.838193+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_r2_collapse.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_r2_collapse.py"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-29T05:18:07.838398+00:00_

1	#!/usr/bin/env python3
2	"""fig_r2_collapse: Three-panel per-layer R² profile (demo-split, bootstrap v3 MCCV)."""
3	import matplotlib
4	matplotlib.use('Agg')
5	import matplotlib.pyplot as plt
6	import numpy as np
7	import os
8	
9	plt.rcParams.update({
10	    'font.family': 'serif',
11	    'font.serif': ['Liberation Serif'],
12	    'pdf.fonttype': 42,
13	    'ps.fonttype': 42,
14	    'mathtext.fontset': 'custom',
15	    'mathtext.rm': 'Liberation Serif',
16	    'mathtext.it': 'Liberation Serif:italic',
17	    'mathtext.bf': 'Liberation Serif:bold',
18	    'font.size': 10,
19	    'axes.titlesize': 13,
20	    'axes.labelsize': 11,
21	    'xtick.labelsize': 10,
22	    'ytick.labelsize': 10,
23	    'legend.fontsize': 9,
24	    'figure.dpi': 300,
25	    'savefig.dpi': 300,
26	    'savefig.bbox': 'tight',
27	    'savefig.pad_inches': 0.05,
28	    'axes.spines.top': False,
29	    'axes.spines.right': False,
30	    'lines.linewidth': 1.8,
31	})
32	
33	TRAINED      = '#0077BB'
34	TRAINED_EDGE = '#005588'
35	REFERENCE    = '#EE7733'
36	REF_EDGE     = '#CC5500'
37	NLP_GRAY     = '#AAAAAA'
38	ANNO_COLOR   = '#444444'
39	DELTA_SHADE  = '#F0F0F0'
40	
41	# ── Demo-split per-layer R² (bootstrap v3 MCCV) ─────────────
42	
43	L32 = np.arange(32)
44	L36 = np.arange(36)
45	
46	# OpenVLA Goal trained: Peak L1, R²=0.418, Exit=0.331, ΔR²=0.086
47	openvla_tr = np.array([
48	    0.3329, 0.4177, 0.3571, 0.2243, 0.3962, 0.3624, 0.3390, 0.3076,
49	    0.2634, 0.2185, 0.4051, 0.3818, 0.3879, 0.3797, 0.3693, 0.3475,
50	    0.3410, 0.3418, 0.3293, 0.3235, 0.3190, 0.2901, 0.2764, 0.2825,
51	    0.2729, 0.2701, 0.2672, 0.2672, 0.4067, 0.3964, 0.3888, 0.3313])
52	
53	# OpenVLA Goal reference (untrained): Peak L27, R²=0.423, Exit=0.367, ΔR²=0.056
54	openvla_ref = np.array([
55	    0.3256, 0.3964, 0.3521, 0.2713, 0.3598, 0.3436, 0.3228, 0.3094,
56	    0.3144, 0.3049, 0.3893, 0.3787, 0.3794, 0.3576, 0.3615, 0.3550,
57	    0.3396, 0.3484, 0.3390, 0.3338, 0.3308, 0.3105, 0.2984, 0.2840,
58	    0.4066, 0
…[truncated 5048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-29T05:18:07.838571+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_multi_layer_attention.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_multi_layer_attention.py"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-29T05:18:07.838762+00:00_

1	#!/usr/bin/env python3
2	"""
3	Plot multi-layer attention profile (Figure 7, left panel).
4	
5	Two sub-panels stacked vertically:
6	  (a) Instruction-dominant head count per layer (L1, L8, L16, L31)
7	  (b) Mean instruction attention fraction per layer
8	
9	Three conditions: Trained VLA, Llama-2 Base, Untrained VLA.
10	
11	Output: fig_multi_layer_attn.pdf -> docs/paper/figures/ and artifacts/figures/paper/
12	"""
13	import matplotlib
14	matplotlib.use('Agg')
15	
16	# ── Font: Liberation Serif (metrically identical to Times New Roman) ──
17	matplotlib.rcParams['font.family'] = 'serif'
18	matplotlib.rcParams['font.serif'] = ['Liberation Serif', 'DejaVu Serif']
19	matplotlib.rcParams['mathtext.fontset'] = 'custom'
20	matplotlib.rcParams['mathtext.rm'] = 'Liberation Serif'
21	matplotlib.rcParams['mathtext.it'] = 'Liberation Serif:italic'
22	matplotlib.rcParams['mathtext.bf'] = 'Liberation Serif:bold'
23	matplotlib.rcParams['pdf.fonttype'] = 42
24	matplotlib.rcParams['ps.fonttype'] = 42
25	
26	import matplotlib.pyplot as plt
27	import numpy as np
28	import os
29	
30	# ── Data ──
31	layers = ['L1', 'L8', 'L16', 'L31']
32	x = np.arange(len(layers))
33	
34	# Panel (a): Instruction-dominant heads count (of 32 total)
35	trained_heads = [24, 4, 10, 19]
36	llama2_heads = [9, 8, 25, 8]
37	untrained_heads = [0, 0, 0, 0]
38	
39	# Panel (b): Mean instruction attention fraction
40	trained_mean = [0.577, 0.468, 0.484, 0.563]
41	llama2_mean = [0.365, 0.488, 0.602, 0.349]
42	untrained_mean = [0.117, 0.079, 0.092, 0.076]
43	
44	colors = {'trained': '#4C72B0', 'llama2': '#55A868', 'untrained': '#C44E52'}
45	
46	fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 4), sharex=True)
47	
48	# ── Panel (a): Head counts ──
49	ax1.plot(x, trained_heads, color=colors['trained'], linestyle='-', marker='o',
50	         markersize=7, linewidth=1.8, label='Trained VLA')
51	ax1.plot(x, llama2_heads, color=colors['llama2'], linestyle='--', marker='s',
52	         markersize=7, linewidth=1.8, label='Llam
…[truncated 2474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-29T05:18:07.838937+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_rsa_perlayer.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_rsa_perlayer.py"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-29T05:18:07.839125+00:00_

1	#!/usr/bin/env python3
2	"""fig_rsa_perlayer_curve: Per-layer RSA rho for trained/reference OpenVLA."""
3	import matplotlib
4	matplotlib.use('Agg')
5	import matplotlib.pyplot as plt
6	import numpy as np
7	import os
8	
9	plt.rcParams.update({
10	    'font.family': 'serif',
11	    'font.serif': ['Liberation Serif', 'DejaVu Serif'],
12	    'pdf.fonttype': 42,
13	    'ps.fonttype': 42,
14	    'mathtext.fontset': 'custom',
15	    'mathtext.rm': 'Liberation Serif',
16	    'mathtext.it': 'Liberation Serif:italic',
17	    'mathtext.bf': 'Liberation Serif:bold',
18	    'font.size': 9,
19	    'axes.linewidth': 0.8,
20	    'xtick.major.width': 0.6,
21	    'ytick.major.width': 0.6,
22	    'xtick.major.size': 3,
23	    'ytick.major.size': 3,
24	})
25	
26	ti_m = np.array([0.6117, 0.6124, 0.6121, 0.6127, 0.6137, 0.6146, 0.6175, 0.6201,
27	                  0.6187, 0.6199, 0.6198, 0.6169, 0.6282, 0.6266, 0.6243, 0.6172,
28	                  0.6128, 0.6088, 0.6071, 0.6072, 0.6041, 0.5959, 0.572, 0.5558,
29	                  0.5459, 0.5346, 0.5159, 0.5136, 0.5125, 0.4971, 0.4395, 0.4328, 0.4223])
30	tp_m = np.array([np.nan, 0.5682, 0.5818, 0.588, 0.5892, 0.5836, 0.5617, 0.543,
31	                  0.5469, 0.5682, 0.5577, 0.5993, 0.6425, 0.6395, 0.6374, 0.6348,
32	                  0.6303, 0.6261, 0.6227, 0.6194, 0.6164, 0.6086, 0.606, 0.6003,
33	                  0.595, 0.5855, 0.5812, 0.5822, 0.5814, 0.5787, 0.5724, 0.5703, 0.5843])
34	ui_m = np.array([0.6117, 0.5712, 0.5604, 0.5597, 0.5576, 0.5576, 0.5588, 0.557,
35	                  0.5553, 0.5532, 0.551, 0.5509, 0.5496, 0.5496, 0.5494, 0.5493,
36	                  0.5497, 0.5495, 0.55, 0.5495, 0.5488, 0.5487, 0.5497, 0.5497,
37	                  0.5494, 0.5482, 0.548, 0.5467, 0.5457, 0.5454, 0.5454, 0.5448, 0.5446])
38	up_m = np.array([np.nan, 0.6262, 0.6207, 0.6156, 0.6119, 0.6084, 0.6053, 0.6029,
39	                  0.6013, 0.6008, 0.5977, 0.5966, 0.5953, 0.5939, 0.5934, 0.5936,
40	                  0.5941, 0.595, 0.5947, 0.
…[truncated 3733 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-29T05:18:07.839286+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_nlp_control_overlay.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_nlp_control_overlay.py"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-29T05:18:07.839475+00:00_

1	#!/usr/bin/env python3
2	"""fig_nlp_control_r2: Three-panel VLA vs NLP control R² overlay for appendix."""
3	import matplotlib
4	matplotlib.use('Agg')
5	import matplotlib.pyplot as plt
6	import numpy as np
7	import os
8	
9	plt.rcParams.update({
10	    'font.family': 'serif',
11	    'font.serif': ['Liberation Serif'],
12	    'pdf.fonttype': 42,
13	    'ps.fonttype': 42,
14	    'mathtext.fontset': 'custom',
15	    'mathtext.rm': 'Liberation Serif',
16	    'mathtext.it': 'Liberation Serif:italic',
17	    'mathtext.bf': 'Liberation Serif:bold',
18	    'font.size': 8,
19	    'axes.titlesize': 10,
20	    'axes.labelsize': 9,
21	    'xtick.labelsize': 8,
22	    'ytick.labelsize': 8,
23	    'legend.fontsize': 7,
24	    'figure.dpi': 300,
25	    'savefig.dpi': 300,
26	    'savefig.bbox': 'tight',
27	    'savefig.pad_inches': 0.05,
28	    'axes.spines.top': False,
29	    'axes.spines.right': False,
30	    'lines.linewidth': 1.8,
31	})
32	
33	TRAINED      = '#92C5DE'
34	TRAINED_EDGE = '#4393C3'
35	REFERENCE    = '#FDB863'
36	REF_EDGE     = '#E08214'
37	NLP_GRAY     = '#888888'
38	PEAK_RED     = '#D6604D'
39	DELTA_SHADE  = '#F4A582'
40	
41	L32 = np.arange(32)
42	L36 = np.arange(36)
43	
44	# Demo-split per-layer R² (bootstrap v3 MCCV)
45	openvla_tr = np.array([
46	    0.3329, 0.4177, 0.3571, 0.2243, 0.3962, 0.3624, 0.3390, 0.3076,
47	    0.2634, 0.2185, 0.4051, 0.3818, 0.3879, 0.3797, 0.3693, 0.3475,
48	    0.3410, 0.3418, 0.3293, 0.3235, 0.3190, 0.2901, 0.2764, 0.2825,
49	    0.2729, 0.2701, 0.2672, 0.2672, 0.4067, 0.3964, 0.3888, 0.3313])
50	
51	openvla_ref = np.array([
52	    0.3256, 0.3964, 0.3521, 0.2713, 0.3598, 0.3436, 0.3228, 0.3094,
53	    0.3144, 0.3049, 0.3893, 0.3787, 0.3794, 0.3576, 0.3615, 0.3550,
54	    0.3396, 0.3484, 0.3390, 0.3338, 0.3308, 0.3105, 0.2984, 0.2840,
55	    0.4066, 0.4066, 0.4122, 0.4230, 0.4111, 0.4080, 0.3994, 0.3672])
56	
57	tracvla_tr = np.array([
58	    0.4550, 0.5002, 0.5105, 0.5059, 0.4393, 0.4509, 0.4767, 0.4736,
59	    0.4390, 0.5085, 0.
…[truncated 4561 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-29T05:18:07.839627+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_training_dynamics.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_training_dynamics.py"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-29T05:18:07.839811+00:00_

1	"""Strip plot of ΔR² across four training pathway categories.
2	Shows that exit collapse emerges at VLM→VLA transition and does not intensify at VLA→VLA.
3	"""
4	import matplotlib
5	matplotlib.use("Agg")
6	import matplotlib.pyplot as plt
7	plt.rcParams.update({
8	    'font.family': 'serif',
9	    'font.serif': ['Liberation Serif'],
10	    'pdf.fonttype': 42,
11	    'ps.fonttype': 42,
12	    'mathtext.fontset': 'custom',
13	    'mathtext.rm': 'Liberation Serif',
14	    'mathtext.it': 'Liberation Serif:italic',
15	    'mathtext.bf': 'Liberation Serif:bold',
16	})
17	import numpy as np
18	import os
19	
20	# --- Data from Table 1 ---
21	categories = ["NLP\nfinetune", "Reference\n(pretrained)", "VLA→VLA\ntrained", "VLM→VLA\ntrained"]
22	
23	data = {
24	    "NLP\nfinetune": [
25	        (0.000, "Llama-2-chat"),
26	        (0.000, "Phi-3-instruct"),
27	        (0.000, "Qwen2.5-Instruct"),
28	    ],
29	    "Reference\n(pretrained)": [
30	        (0.065, "TraceVLA"),   # Goal ref
31	        (0.048, "TraceVLA"),   # Spatial ref
32	        (0.009, "TraceVLA"),   # Object ref
33	        (0.097, "TraceVLA"),   # Long ref
34	        (0.081, "NORA"),      # Goal ref
35	        (0.089, "NORA"),      # Spatial ref
36	        (0.056, "OpenVLA"),   # Goal ref
37	        (0.044, "OpenVLA"),   # Spatial ref
38	        (0.051, "OpenVLA"),   # Object ref
39	        (0.035, "OpenVLA"),   # Long ref
40	    ],
41	    "VLA→VLA\ntrained": [
42	        (0.086, "OpenVLA"),   # Goal
43	        (0.037, "OpenVLA"),   # Spatial
44	        (0.037, "OpenVLA"),   # Object
45	        (0.033, "OpenVLA"),   # Long
46	    ],
47	    "VLM→VLA\ntrained": [
48	        (0.333, "TraceVLA"),   # Goal
49	        (0.156, "TraceVLA"),   # Spatial
50	        (0.362, "TraceVLA"),   # Object
51	        (0.358, "TraceVLA"),   # Long
52	        (0.455, "NORA"),      # Goal
53	        (0.308, "NORA"),      # Spatial
54	    ],
55	}
56	
57	arch_markers = {"OpenVLA": "o", "TraceVLA": "s", "NORA": "D",
58	                "L
…[truncated 2488 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-29T05:18:07.840147+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_claim_evidence.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_claim_evidence.py"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-29T05:18:07.840386+00:00_

1	#!/usr/bin/env python3
2	"""fig_claim_evidence: Claim-evidence-scope summary figure (Appendix)."""
3	import matplotlib
4	matplotlib.use('Agg')
5	import matplotlib.pyplot as plt
6	plt.rcParams.update({
7	    'font.family': 'serif',
8	    'font.serif': ['Liberation Serif'],
9	    'pdf.fonttype': 42,
10	    'ps.fonttype': 42,
11	    'mathtext.fontset': 'custom',
12	    'mathtext.rm': 'Liberation Serif',
13	    'mathtext.it': 'Liberation Serif:italic',
14	    'mathtext.bf': 'Liberation Serif:bold',
15	})
16	import matplotlib.patches as mpatches
17	import os
18	
19	rows = [
20	    {
21	        'finding': 'Training-Associated\nExit Collapse',
22	        'description': '$R^2$ drops at exit layers\nafter VLA fine-tuning',
23	        'evidence': '6/6 VLM→VLA conditions\nshow Δ > 0.10;\n0/4 VLA→VLA;\n0/10 reference conditions',
24	        'limitation': 'Correlational,\nnot causal',
25	        'color': '#FDEBD0',
26	        'edge': '#E8A838',
27	    },
28	    {
29	        'finding': 'Action-Relevant\nSensitivity',
30	        'description': 'Counterfactual perturbation\nreveals action-linked\nrepresentations',
31	        'evidence': "Cohen's $d$ ≥ 0.45 across\n8 trained conditions;\nempty ranks first in 6/8",
32	        'limitation': '$d$ vs cosine metric\nincomparability',
33	        'color': '#D5F5E3',
34	        'edge': '#52BE80',
35	    },
36	    {
37	        'finding': 'Inherited Instruction\nAttention Prior',
38	        'description': 'L1 attention patterns\ninherited from\npre-trained VLMs',
39	        'evidence': 'Reference VLMs already\nshow task-structured\nattention',
40	        'limitation': 'Not causally\ntested',
41	        'color': '#D6EAF8',
42	        'edge': '#5DADE2',
43	    },
44	]
45	
46	col_labels = ['Finding', 'Evidence', 'Limitation']
47	col_colors = ['#2C3E50', '#2C3E50', '#2C3E50']
48	
49	fig_w, fig_h = 7.0, 3.2
50	fig, ax = plt.subplots(figsize=(fig_w, fig_h))
51	ax.set_xlim(0, fig_w)
52	ax.set_ylim(0, fig_h)
53	ax.axis('off')
54	
55	box_h = 0.72
56
…[truncated 2547 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-29T05:18:07.840555+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_teaser.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_teaser.py"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-29T05:18:07.840766+00:00_

1	import matplotlib
2	matplotlib.use('Agg')
3	import matplotlib.pyplot as plt
4	import matplotlib.patches as mpatches
5	import matplotlib.patheffects as pe
6	import numpy as np
7	import os
8	
9	plt.rcParams.update({
10	    'font.family': 'serif',
11	    'font.serif': ['Liberation Serif'],
12	    'pdf.fonttype': 42,
13	    'ps.fonttype': 42,
14	    'mathtext.fontset': 'custom',
15	    'mathtext.rm': 'Liberation Serif',
16	    'mathtext.it': 'Liberation Serif:italic',
17	    'mathtext.bf': 'Liberation Serif:bold',
18	    'font.size': 11,
19	    'axes.titlesize': 13,
20	    'axes.labelsize': 12,
21	    'xtick.labelsize': 10,
22	    'ytick.labelsize': 10,
23	    'legend.fontsize': 10,
24	    'figure.dpi': 300,
25	    'savefig.dpi': 300,
26	    'savefig.bbox': 'tight',
27	    'savefig.pad_inches': 0.05,
28	    'axes.spines.top': False,
29	    'axes.spines.right': False,
30	    'lines.linewidth': 1.8,
31	})
32	
33	# --- Data ---
34	vla_trained = [21,24,4,3,3,4,6,4,5,6,5,6,7,6,5,4,3,2,1,2,1,0,2,1,1,0,1,0,1,3,5,18]
35	pretrained  = [0,9,6,6,7,8,9,10,11,15,16,17,18,19,20,21,22,20,18,16,14,12,10,8,7,6,5,4,3,2,1,0]
36	
37	C_PRETRAINED = '#0072B2'
38	C_VLA        = '#D55E00'
39	C_ARROW      = '#555555'
40	C_ENTRY      = '#FBDCDB'
41	C_MID        = '#EEEEEE'
42	C_LLM_BG     = '#EDF2FA'
43	
44	fig = plt.figure(figsize=(7.0, 3.6))
45	gs = fig.add_gridspec(1, 2, width_ratios=[0.6, 1.35], wspace=0.05)
46	
47	# ============================================================
48	# Panel (a): Simplified VLA architecture
49	# ============================================================
50	ax = fig.add_subplot(gs[0])
51	ax.set_xlim(-1, 11)
52	ax.set_ylim(-0.5, 20)
53	ax.axis('off')
54	
55	ax.text(-0.5, 19.5, '(a)', fontsize=13, fontweight='bold', va='top')
56	
57	akw = dict(arrowstyle='->', color=C_ARROW, lw=1.2, mutation_scale=12)
58	pcx = 4.0
59	
60	def simple_box(cx, cy, w, h, label, fc, fs=8.5, ec='#999', bold=False):
61	    r = mpatches.FancyBboxPatch(
62	        (cx-w/2, cy-h/2), w, h,
…[truncated 6247 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-29T05:18:07.840918+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_overview.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/scripts/plot_overview.py"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-29T05:18:07.841260+00:00_

1	import matplotlib
2	matplotlib.use('Agg')
3	import matplotlib.pyplot as plt
4	import matplotlib.patches as mpatches
5	import matplotlib.patheffects as pe
6	import numpy as np
7	import os, shutil
8	
9	plt.rcParams.update({
10	    'font.family': 'serif',
11	    'font.serif': ['Liberation Serif'],
12	    'pdf.fonttype': 42,
13	    'ps.fonttype': 42,
14	    'mathtext.fontset': 'custom',
15	    'mathtext.rm': 'Liberation Serif',
16	    'mathtext.it': 'Liberation Serif:italic',
17	    'mathtext.bf': 'Liberation Serif:bold',
18	    'font.size': 10,
19	    'figure.dpi': 300,
20	    'savefig.dpi': 300,
21	    'savefig.bbox': 'tight',
22	    'savefig.pad_inches': 0.08,
23	})
24	
25	# ─── Pastel color palette ───────────────────────────────────
26	PASTEL = {
27	    'blue':   '#92C5DE',
28	    'gold':   '#FDB863',
29	    'orange': '#F4A582',
30	    'green':  '#A6DBA0',
31	    'pink':   '#E7B8D4',
32	    'cyan':   '#B2E2E2',
33	}
34	EDGE = {
35	    'blue':   '#4393C3',
36	    'gold':   '#E08214',
37	    'orange': '#D6604D',
38	    'green':  '#5AAE61',
39	    'pink':   '#C2669A',
40	    'cyan':   '#5AB4AC',
41	}
42	
43	PASTEL_BLUE_L  = '#DBE9F4'
44	PASTEL_GOLD_L  = '#FEF0D9'
45	PASTEL_ORANGE_L = '#FDEAE3'
46	PASTEL_GREEN_L = '#E3F5E1'
47	
48	TXT     = '#2B2B2B'
49	TXT2    = '#666666'
50	TXT3    = '#999999'
51	LN      = '#888888'
52	
53	# ─── Figure (compact) ──────────────────────────────────────
54	fig = plt.figure(figsize=(10, 3.2), facecolor='white')
55	
56	ax_a = fig.add_axes([0.01, 0.04, 0.28, 0.88])
57	ax_b = fig.add_axes([0.31, 0.04, 0.38, 0.88])
58	ax_c = fig.add_axes([0.71, 0.04, 0.28, 0.88])
59	
60	for ax in [ax_a, ax_b, ax_c]:
61	    ax.axis('off')
62	
63	# ─── Helpers ─────────────────────────────────────────────────
64	def rbox(ax, cx, cy, w, h, label='', fc='white', ec='#CCC',
65	         fontsize=9, fontweight='normal', tc=TXT,
66	         lw=0.7, ls='-', zorder=3, fontstyle='normal',
67	         shadow=False, radius=0.12, label_lines=None):
68	    if shadow:
69	
…[truncated 13653 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-29T05:18:07.841437+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-29T05:18:07.841672+00:00_

1	\clearpage
2	\appendix
3	
4	\section{Supplementary Material}
5	\label{sec:appendix}
6	
7	Unless noted otherwise, all analyses use OpenVLA-7B (\texttt{openvla/openvla-7b} on HuggingFace) evaluated on LIBERO-Goal (10 tasks $\times$ 50 demonstrations, $N = 63{,}228$ observations after excluding terminal frames).
8	Model conditions, representation extraction, metric definitions, and probe architectures follow \S\ref{sec:method}.
9	Cross-suite experiments (\S\ref{sec:cross_benchmark_appendix}) use LIBERO-Spatial with the same protocol (10 tasks $\times$ 50 demonstrations).
10	All experiments ran on 2$\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs (96\,GB each); random seed is 42 unless stated otherwise.
11	
12	\subsection{Architecture Summary}
13	Architecture details are provided in Table~\ref{tab:arch_overview} (main text).
14	
15	\subsection{OpenVLA-Specific Analysis Methods}
16	\label{sec:openvla_methods_appendix}
17	
18	Three additional analyses are applied to OpenVLA to characterize instruction encoding and representational geometry.
19	
20	\paragraph{Cross-instruction probes.}
21	Each visual frame is paired with all 10 LIBERO-Goal task instructions, producing 10 representation vectors per frame per layer.
22	A 10-way linear classifier identifies which instruction was present, applied separately at image\_mean and readout, with leave-one-out cross-validation (LOOCV) over 10 folds.
23	
24	\paragraph{Representational similarity analysis (RSA).}
25	RSA~\cite{kriegeskorte2008} quantifies geometric alignment between representations and the action space.
26	For each task, we compute pairwise representational dissimilarity matrices (RDMs) using cosine distances for representations and Euclidean distances for 7-D action vectors, from within-task observation pairs across 50 demonstrations.
27	Alignment is measured via Spearman $\rho$ between upper-triangular RDM entries; we report mean $\rho$ across 10 tasks with 95\% confidence intervals from 10{,}000 bootstrap
…[truncated 16129 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-29T05:18:07.841867+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "200",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "200",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-29T05:18:07.842167+00:00_

200	\subsection{Action Trajectory Analysis Details}
201	\label{sec:action_trajectory}
202	
203	Table~\ref{tab:action_shift_perdim} reports per-dimension mean absolute shift for instruction-dominant (24 heads) and control (8 heads) L1 ablations.
204	Both conditions produce negligible shifts on translational dimensions ($dx$, $dy$, $dz$ $< 0.01$) and small rotational shifts ($rx$, $ry$, $rz$ $< 0.04$).
205	The gripper dimension absorbs the majority of the effect: instruction-head ablation shifts gripper predictions by $0.291$ (control: $0.141$), consistent with L1 attention influencing discrete open/close decisions.
206	
207	Per-task Cohen's $d$ values for instruction-head ablation are $0.43$, $0.69$, $0.70$, $0.70$, and $0.73$ (mean $0.65$), with all tasks significant ($p < 10^{-10}$).
208	Token-level KL divergence between original and ablated action distributions is $5.08$ for instruction heads and $1.69$ for control heads.
209	
210	\paragraph{Trajectory-level aggregation.}
211	Aggregating per-demo mean actions to the trajectory level reveals that token-level $d$ values are conservative: within-trajectory averaging reduces noise, yielding ${\sim}4\times$ larger effect sizes (mean token-to-trajectory ratio $0.245$).
212	Instruction-head ablation ($N = 50$: 5 tasks $\times$ 10 demos) yields trajectory $d = 2.943$ (95\% CI $[2.469, 3.707]$); bottom-24 non-instruction heads ($N = 30$) yield $d = 2.347$ (CI $[1.854, 3.221]$).
213	All 14 conditions produce trajectory $d > 2.0$ with CI lower bounds $> 1.7$.
214	Counterfactual trajectory-level $d$ (10 LIBERO-Goal tasks, $N = 100$): wrong $3.798$ (CI $[3.194, 4.938]$), empty $3.438$ ($[2.921, 4.448]$), shuffled $2.595$ ($[2.028, 3.791]$), paraphrased $2.131$ ($[1.740, 2.819]$).
215	Token-level $d$ underestimates trajectory-level effects by ${\times}3.1$--$4.5$, consistent with within-trajectory averaging reducing noise.
216	Fine-grained ordering is not reliably distinguished at trajectory level ($N = 100$); token-level compa
…[truncated 12966 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-29T05:18:07.842335+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-29T05:18:07.842504+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant representations are organized across three VLA architectures using complementary probing, attention, and perturbation analyses.
5	
6	%------------------------------------------------------------------
7	\subsection{Architectures and Data}
8	\label{sec:arch_data}
9	
10	\looseness=-1
11	We study three VLAs spanning distinct backbone families (Table~\ref{tab:arch_overview}):
12	\textbf{OpenVLA}~\cite{kim2024_openvla,karamcheti2024} (Llama-2-7B~\cite{touvron2023_llama2}, 32 layers, pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} [OXE; 970K episodes]),
13	\textbf{TraceVLA}~\cite{zheng2024tracevla} (Phi-3-mini~\cite{abdin2024phi3}, 32 layers, trained on an OXE subset with spatial trace conditioning), and
14	\textbf{NORA}~\cite{hung2025nora} (Qwen2.5-VL-3B, 36 layers, grouped-query attention with 16 query heads).
15	Each is evaluated in trained and reference conditions.
16	A critical asymmetry distinguishes the references: OpenVLA's is an OXE-pretrained VLA (already producing actions), while TraceVLA and NORA references are pure VLMs (Phi-3-Vision, Qwen2.5-VL) with no action training; thus OpenVLA comparisons measure VLA-to-VLA transitions, while TraceVLA and NORA measure VLM-to-VLA transitions.
17	OpenVLA additionally provides Llama-2 base and random-weight conditions (\S\ref{sec:openvla_routing}).
18	
19	We evaluate on LIBERO~\cite{liu2023_libero}, comprising four task suites (Goal, Spatial, Object, Long-Horizon) with 10 tasks and 50 demonstrations each.
20	The three architectures and four suites form a $3 \times 4$ matrix; 10 of 12 cells are filled (NORA Object and Long-Horizon lack available checkpoints).
21	
22	%------------------------------------------------------------------
23	\subsection{Representation Extraction}
24	\looseness=-1
25	From each architecture, we extract hidden states at every transformer layer from two token positions: (a)~\textbf{image\_mean}, the mean activati
…[truncated 3880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-29T05:18:07.842658+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-29T05:18:07.842812+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision-language-action models (VLAs) fine-tune pretrained language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}, but which of the resulting representational changes reflect action training and which are inherited from the pretrained backbone?
5	In these decoder-only architectures, image tokens precede instruction tokens, and the causal attention mask restricts multimodal integration to a single readout token~\cite{wang2025seeing,pei2025rethinking}; how representations at this critical position are reshaped by action fine-tuning remains unknown.
6	
7	Behavioral studies show that VLAs exhibit visual dominance~\cite{grant2026} and underweight instructions~\cite{haon2025}, but existing representational analyses target single architectures.
8	No prior work tests whether instruction routing---the internal mechanisms by which instruction tokens influence action-relevant representations---is consistent across backbone families or decomposes training-associated effects from inherited base-model priors.
9	
10	We address this gap with a cross-architecture analysis of three VLAs (OpenVLA~\cite{kim2024_openvla}, TraceVLA~\cite{zheng2024tracevla}, and NORA~\cite{hung2025nora}) across four LIBERO~\cite{liu2023_libero} task suites (\S\ref{sec:setup}).
11	TraceVLA and NORA baselines are pure VLMs ($N = 2$ independent VLM-to-VLA transitions); OpenVLA's baseline is the OXE-pretrained~\cite{padalkar2023_oxe} VLA (VLA-to-VLA transition).
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=0.88\linewidth]{figures/fig_overview.pdf}
16	\caption{\textbf{Analysis framework.} We analyze hidden states at image-token averages and the readout token via layer-wise action probes, counterfactual instruction perturbations, and L1 attention profiling to distinguish training-associated changes from inherited backbone priors.}
17	\label{fig:
…[truncated 1499 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-29T05:18:07.842976+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-29T05:18:07.843125+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	\looseness=-1
5	We presented a cross-architecture representational analysis of instruction routing in vision-language-action models, studying three VLAs built on distinct backbone families across four LIBERO task suites.
6	Our three complementary analyses---layer-wise action probing, counterfactual instruction perturbation, and L1 attention profiling---consistently decompose VLA instruction routing into two distinct patterns: training-associated effects and inherited base-model priors.
7	Exit collapse ($\Delta R^2 = 0.16$--$0.46$) and graded counterfactual sensitivity ($d = 0.45$--$1.52$) emerge specifically from VLM-to-VLA fine-tuning---absent in both VLA-to-VLA and NLP-only controls---while L1 attention routing is inherited from reference backbones.
8	These findings enable practical diagnostics: $\Delta R^2 > 0.10$ flags under-utilized exit-layer representations without rollouts, and mid-layer features offer principled tap points for downstream reward models and planners.
9	The cross-architecture consistency---with mid-layer action-probe peaks converging to within $R^2 = 0.003$ despite divergent reference profiles---suggests these are general properties of autoregressive VLA fine-tuning, not artifacts of any single model design.
10	
11	\section{Limitations}
12	\label{sec:limitations}
13	
14	\looseness=-1
15	Our conclusions rest on $N{=}2$ VLM-to-VLA transitions plus one VLA-to-VLA case, all autoregressive decoders evaluated on a single benchmark (LIBERO); flow-matching~\cite{black2024_pi0} and diffusion~\cite{ghosh2024_octo} action heads may behave differently.
16	All findings are correlational---$R^2$ measures decodability, not causal reliance---and evaluations are open-loop; the $\Delta R^2$--success-rate correlation ($\rho{=}0.583$, $p{=}0.10$; Appendix~\ref{sec:extended_discussion_appendix}) is suggestive but underpowered ($n{=}9$).
17	Extending to additional architectures, non-autoregressive action heads, a
…[truncated 72 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-29T05:18:07.843293+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "400",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "400",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-29T05:18:07.843507+00:00_

400	Paraphrased & 0.533 & 0.807 & 0.179 \\
401	\bottomrule
402	\end{tabular}
403	\end{table}
404	
405	\paragraph{Cross-Instruction Probe on LIBERO-Spatial}
406	Table~\ref{tab:spatial_cross_instruction} reports cross-instruction 10-way classification accuracy on LIBERO-Spatial.
407	The core pattern from LIBERO-Goal replicates: image\_mean remains at chance (${\sim}10\%$) across all layers and conditions, while the trained readout token saturates to $100\%$ by L4.
408	The reference readout decays more steeply than on LIBERO-Goal ($75.4\%$ at L31 vs.\ $82\%$), consistent with greater task difficulty.
409	
410	\begin{table}[h]
411	\centering
412	\caption{Cross-instruction 10-way classification accuracy on LIBERO-Spatial. Trained readout achieves $100\%$ from L4; image\_mean remains at chance. Reference readout decays more steeply than on LIBERO-Goal (cf.\ \S\ref{sec:openvla_routing}).}
413	\label{tab:spatial_cross_instruction}
414	\small
415	\begin{tabular}{llccccc}
416	\toprule
417	\textbf{Token} & \textbf{Condition} & \textbf{L1} & \textbf{L4} & \textbf{L8} & \textbf{L16} & \textbf{L31} \\
418	\midrule
419	readout & Trained & 98.9\% & 100.0\% & 100.0\% & 100.0\% & 100.0\% \\
420	readout & Reference & 99.5\% & 98.3\% & 85.7\% & 68.3\% & 75.4\% \\
421	image\_mean & Trained & 10.2\% & 10.0\% & 9.9\% & 10.0\% & 10.1\% \\
422	image\_mean & Reference & 10.1\% & 10.0\% & 10.0\% & 10.0\% & 10.2\% \\
423	\bottomrule
424	\end{tabular}
425	\end{table}
426	
427	\subsection{Robustness Analyses}
428	\paragraph{Distance Metric Invariance}
429	The inverted-U profile is robust to distance metric choice: cosine action distance yields identical peak layers (L12) and Pearson correlation $r > 0.989$ with the Euclidean profile reported in the main text (Table~\ref{tab:metric_invariance}).
430	
431	\begin{table}[h]
432	\centering
433	\caption{Peak layer comparison between Euclidean and cosine action distances. Profile $r$ denotes Pearson correlation across all 32 layers.}
434	\label{tab:met
…[truncated 11695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-29T05:18:07.843670+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
  "offset": "600",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/appendix.tex",
    "offset": "600",
    "limit": "250"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-29T05:18:07.843961+00:00_

600	\bottomrule
601	\end{tabular}
602	\end{table}
603	
604	\subsection{Training Effect Size Summary}
605	Table~\ref{tab:training_effect_summary} consolidates training effects across all metrics.
606	Training effects on image\_mean metrics are modest (RSA $\Delta = +0.017$, $R^2$ $\Delta = +0.015$), but effects on readout metrics are substantial (instruction attention $+18$pp, attention $+46$pp, $R^2$ $\Delta = +0.069$).
607	This asymmetry indicates that training primarily changes how the readout token integrates information rather than altering the visual representations carried by image tokens.
608	
609	\begin{table}[h]
610	\centering
611	\caption{Training effect sizes across metrics. Image\_mean effects are modest; readout effects are large. Training targets readout-token information integration.}
612	\label{tab:training_effect_summary}
613	\small
614	\begin{tabular}{lccc}
615	\toprule
616	\textbf{Metric} & \textbf{Trained} & \textbf{Reference} & \textbf{$\Delta$} \\
617	\midrule
618	RSA peak (image\_mean) & 0.628 (L12) & 0.612 (L0) & $+$0.017 \\
619	$R^2$ peak (image\_mean) & 0.655 (L8) & 0.640 (L0) & $+$0.015 \\
620	$R^2$ peak (readout) & 0.678 (L13) & 0.609 (L32) & $+$0.069 \\
621	Instruction attention L31 & 100\% & 82\% & $+$18pp \\
622	Instruction attention L1 & 58\% & 12\% & $+$46pp \\
623	Progress classification & 86.3\% (L20) & 85.3\% (L4) & $+$1pp \\
624	\bottomrule
625	\end{tabular}
626	\end{table}
627	
628	\subsection{Instruction Classification Probes}
629	\paragraph{Cross-Instruction Classification: Dense Layer Profile}
630	\label{sec:dense_routing}
631	
632	Table~\ref{tab:dense_routing} shows the dense per-layer profile of cross-instruction classification (10-way) at the readout token for layers L0--L8.
633	The step-function onset between L0 ($10\%$, chance) and L1 (${\geq}99.6\%$) reflects the high discriminability of instruction embeddings from the frozen tokenizer: even incidental attention (${\sim}12\%$) suffices for linear classification at L1.
6
…[truncated 13638 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-29T05:18:07.844316+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/counterfactual*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/counterfactual*.json",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-29T05:18:07.844482+00:00_

checkpoints/counterfactual_instruction_PREPARING_20260518T165253.json
checkpoints/counterfactual_instruction_QUEUED_20260518T170701.json
checkpoints/counterfactual_instruction_RUNNING_20260518T170711.json
checkpoints/counterfactual_instruction_RUNNING_20260518T173112.json
checkpoints/counterfactual_instruction_RUNNING_20260518T173114.json
checkpoints/counterfactual_instruction_DONE_20260518T173116.json
checkpoints/counterfactual_instruction_DONE_20260518T173126.json
checkpoints/counterfactual_token_overlap_QUEUED_20260519T011941.json
checkpoints/counterfactual_token_overlap_RUNNING_20260519T011949.json
checkpoints/counterfactual_token_overlap_RUNNING_20260519T011954.json
checkpoints/counterfactual_token_overlap_DONE_20260519T012012.json
checkpoints/counterfactual_10tasks_QUEUED_20260520T185104.json
checkpoints/counterfactual_10tasks_RUNNING_20260520T185109.json
checkpoints/counterfactual_10tasks_ANALYZING_20260520T185218.json
checkpoints/counterfactual_10tasks_ANALYZING_20260520T201552.json
checkpoints/counterfactual_10tasks_DONE_20260520T201557.json
checkpoints/counterfactual_spatial_PENDING_20260520T213530.json
checkpoints/counterfactual_spatial_QUEUED_20260520T213537.json
checkpoints/counterfactual_spatial_ALLOCATED_20260520T213542.json
checkpoints/counterfactual_spatial_RUNNING_20260520T213558.json
checkpoints/counterfactual_spatial_ANALYZING_20260520T213602.json
checkpoints/counterfactual_spatial_ANALYZING_20260520T213809.json
checkpoints/counterfactual_spatial_DONE_20260520T213809.json
artifacts/statistical_supplements/counterfactual_spatial.json
artifacts/counterfactual_spatial/data/counterfactual_spatial.json
artifacts/statistical_supplements/counterfactual_10tasks_trajectory.json
artifacts/counterfactual_10tasks/data/counterfactual_10tasks_trajectory.json
checkpoints/counterfactual_10tasks_trajectory_PREPARING_20260520T214716.json
checkpoints/counterfactual_10tasks_trajectory_QUEUED_20260520T214730.json
checkpoints/counterfactual_10tasks_trajectory_ALLOCATE
…[truncated 224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-29T05:18:07.844637+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/cf_*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/cf_*.json",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-29T05:18:07.844769+00:00_

checkpoints/cf_batch_missing_v1_PREPARING_20260521T201839.json
checkpoints/cf_batch_part2_v1_PREPARING_20260521T230239.json
checkpoints/cf_batch_missing_v1_QUEUED_20260521T235920.json
checkpoints/cf_batch_part2_v1_QUEUED_20260521T235922.json
checkpoints/cf_batch_missing_v1_RUNNING_20260521T235930.json
checkpoints/cf_batch_part2_v1_RUNNING_20260521T235932.json
checkpoints/cf_batch_part2_v1_ANALYZING_20260522T000441.json
checkpoints/cf_batch_part2_v1_ANALYZING_20260522T000647.json
checkpoints/cf_batch_part2_v1_DONE_20260522T000710.json
checkpoints/cf_batch_part2_v1_DONE_20260522T000947.json
checkpoints/cf_batch_missing_v1_ANALYZING_20260522T012443.json
checkpoints/cf_batch_missing_v1_ANALYZING_20260522T041724.json
checkpoints/cf_batch_missing_v1_DONE_20260522T041748.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-29T05:18:07.844895+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "counterfactual|cohens_d|cosine_dist",
  "glob": "*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Grep",
  "tool_args": {
    "pattern": "counterfactual|cohens_d|cosine_dist",
    "glob": "*.json",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-29T05:18:07.845047+00:00_

Found 13 files
artifacts/dream_reports/dream_20260527T022433/median/experiment_data.json
artifacts/dream_reports/dream_20260527T022433/best/experiment_data.json
artifacts/dream_reports/dream_20260522T021705/worst/experiment_data.json
artifacts/dream_reports/dream_20260522T021705/median/experiment_data.json
artifacts/dream_reports/dream_20260522T021705/best/experiment_data.json
artifacts/tracvla_spatial/counterfactual_combined.json
artifacts/counterfactual_10tasks/data/counterfactual_10tasks_trajectory.json
artifacts/statistical_supplements/counterfactual_10tasks_trajectory.json
artifacts/counterfactual_spatial/data/counterfactual_spatial.json
artifacts/statistical_supplements/counterfactual_spatial.json
artifacts/_project/data/bonferroni_global.json
artifacts/statistical_supplements/bonferroni_global.json
artifacts/statistical_supplements/power_analysis.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-29T05:18:07.845228+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/tracvla_spatial/counterfactual_combined.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/tracvla_spatial/counterfactual_combined.json"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-29T05:18:07.845431+00:00_

1	{
2	  "config": {
3	    "experiment": "counterfactual_tracvla_spatial",
4	    "conditions": ["wrong", "empty", "shuffled", "paraphrased"],
5	    "n_tasks": 2,
6	    "n_demos_per_task": 1,
7	    "n_timesteps_per_demo": 2,
8	    "model": "tracevla-phi3v",
9	    "action_space": "normalized_bins",
10	    "seed": 42,
11	    "task_names": [
12	      "pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate",
13	      "pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate"
14	    ]
15	  },
16	  "wrong": {
17	    "global_metrics": {
18	      "paired_mse": {"mean": 0.065381, "std": 0.035064, "cohens_d": 1.6148},
19	      "per_dim_shift": {
20	        "means": [0.092157, 0.072549, 0.215686, 0.164706, 0.22549, 0.264706, 0.247059],
21	        "stds": [0.054445, 0.04415, 0.203959, 0.056829, 0.126025, 0.248293, 0.247059],
22	        "dim_names": ["dx", "dy", "dz", "rx", "ry", "rz", "gripper"]
23	      },
24	      "token_divergence_rate": 1.0,
25	      "n_samples": 4
26	    },
27	    "per_task": {
28	      "pick_up_the_black_bowl_between_the_plate_and_the_ramekin_and_place_it_on_the_plate": {
29	        "cohens_d": 1.4614, "demo_level_cohens_d": 0.0, "n_samples": 2, "mean_mse": 0.047467, "demo_mses": [0.047467],
30	        "instruction_correct": "pick up the black bowl between the plate and the ramekin and place it on the plate",
31	        "instruction_counterfactual": "pick up the black bowl on the ramekin and place it on the plate"
32	      },
33	      "pick_up_the_black_bowl_on_the_ramekin_and_place_it_on_the_plate": {
34	        "cohens_d": 1.6401, "demo_level_cohens_d": 0.0, "n_samples": 2, "mean_mse": 0.083295, "demo_mses": [0.083295],
35	        "instruction_correct": "pick up the black bowl on the ramekin and place it on the plate",
36	        "instruction_counterfactual": "pick up the black bowl on the cookie box and place it on the plate"
37	      }
38	    },
39	    "cross_task_variance": {"cohens_d": {"values": [1.4614, 1.6401], "m
…[truncated 4916 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-29T05:18:07.845583+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/tracvla_*/",
  "description": "List TraceVLA artifact directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/tracvla_*/",
    "description": "List TraceVLA artifact directories"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-29T05:18:07.845718+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/tracvla_spatial/:
action_r2_probing.json
counterfactual_combined.json
cross_instruction_classification.json
l1_attention_profile.json

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/tracvla_spatial_trained/:
intermediate

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-29T05:18:07.845867+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/ | grep -E \"tracvla|cf_batch|nora\"",
  "description": "List TraceVLA/NORA/cf_batch artifact dirs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/ | grep -E \"tracvla|cf_batch|nora\"",
    "description": "List TraceVLA/NORA/cf_batch artifact dirs"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-29T05:18:07.846022+00:00_

cf_batch_missing_v1
cf_batch_part2_v1
cf_batch_part2_v1_analysis.md
nora_analysis_report.md
seed_robustness_tracvla.py
tracvla_spatial
tracvla_spatial_full_pipeline.py
tracvla_spatial_trained

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-29T05:18:07.846147+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts -name \"*.json\" | xargs grep -l \"TV-S\\|TV-O\\|tracevla.*spatial\\|tracevla.*object\" 2>/dev/null | head -10",
  "description": "Search for JSON files with TraceVLA Spatial/Object data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts -name \"*.json\" | xargs grep -l \"TV-S\\|TV-O\\|tracevla.*spatial\\|tracevla.*object\" 2>/dev/null | head -10",
    "description": "Search for JSON files with TraceVLA Spatial/Object data"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-29T05:18:07.846265+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-29T05:18:07.846378+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/cf_batch_part2_v1/ /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/cf_batch_missing_v1/ 2>/dev/null",
  "description": "List cf_batch directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/cf_batch_part2_v1/ /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/cf_batch_missing_v1/ 2>/dev/null",
    "description": "List cf_batch directories"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-29T05:18:07.846494+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/cf_batch_missing_v1/:
report

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/cf_batch_part2_v1/:
report

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-29T05:18:07.846607+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/cf_batch_part2_v1/report/ /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/cf_batch_missing_v1/report/",
  "description": "List cf_batch report contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/cf_batch_part2_v1/report/ /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/cf_batch_missing_v1/report/",
    "description": "List cf_batch report contents"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-29T05:18:07.846722+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/cf_batch_missing_v1/report/:
cf_batch_missing_v1_analysis.md
cf_batch_missing_v1_analysis_c4752f.md

/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/cf_batch_part2_v1/report/:
cf_batch_part2_v1_analysis.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-29T05:18:07.846838+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/cf_batch_part2_v1/report/cf_batch_part2_v1_analysis.md",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/cf_batch_part2_v1/report/cf_batch_part2_v1_analysis.md",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-29T05:18:07.847023+00:00_

1	# cf_batch_part2_v1 Analysis: TracVLA Untrained Counterfactual Sensitivity
2	
3	## Experiment Overview
4	- **Content**: TracVLA (Phi-3-Vision base, untrained) counterfactual sensitivity on LIBERO-Goal and LIBERO-Long
5	- **Method**: cosine_dist (representation cosine distance at L31)
6	- **Model**: phi3v-base (microsoft/Phi-3-vision-128k-instruct, NOT fine-tuned on LIBERO)
7	- **Conditions**: wrong, empty, shuffled, paraphrased × 2 suites
8	- **Samples**: 5000 per condition (10 tasks × 10 demos × 50 timesteps)
9	- **Server**: westd-19183, cuda:1
10	- **Runtime**: ~31 min (Goal) + ~29 min (Long) = ~60 min total
11	- **Exit code**: 0 (success)
12	
13	## Results: TracVLA Goal Untrained
14	
15	| Condition | cos_dist (L31) | cohens_d (global) | cross-task mean d |
16	|-----------|---------------|-------------------|------------------|
17	| empty | 0.1530 | 8.8871 | 18.1209 |
18	| shuffled | 0.0839 | 1.4142 | 14.9672 |
19	| wrong | 0.0160 | 1.2932 | 13.1758 |
20	| paraphrased | 0.0043 | 2.1607 | 9.7738 |
21	
22	**Ordering by cos_dist**: empty >> shuffled > wrong > paraphrased
23	
24	## Results: TracVLA Long Untrained
25	
26	| Condition | cos_dist (L31) | cohens_d (global) | cross-task mean d |
27	|-----------|---------------|-------------------|------------------|
28	| empty | 0.1734 | 11.2529 | 19.0888 |
29	| shuffled | 0.1204 | 2.0345 | 16.7802 |
30	| wrong | 0.0221 | 1.8731 | 11.6638 |
31	| paraphrased | 0.0070 | 1.7351 | 12.9783 |
32	
33	**Ordering by cos_dist**: empty >> shuffled > wrong > paraphrased
34	
35	## Comparison with Trained CF
36	
37	⚠️ **Method difference**: Trained CF used `paired_mse` (action output divergence); untrained CF used `cosine_dist` (hidden representation distance). Magnitudes are NOT comparable. Only orderings can be compared.
38	
39	### Ordering Comparison
40	
41	| Suite | Trained (paired_mse) | Untrained (cosine_dist) |
42	|-------|---------------------|------------------------|
43	| Goal | empty(1.52) > wrong(1.40) > shuffled(1.34) > pa
…[truncated 1418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-29T05:18:07.847209+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/cf_batch_missing_v1/report/cf_batch_missing_v1_analysis.md",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/cf_batch_missing_v1/report/cf_batch_missing_v1_analysis.md",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-29T05:18:07.847373+00:00_

1	# cf_batch_missing_v1 Analysis Report
2	
3	## Experiment Overview
4	
5	Batch counterfactual补跑实验，使用 `cosine_dist` 方法（hidden representation cosine distance, L31）为 3x4 矩阵补充 untrained CF cells。
6	
7	- **Method**: representation_cosine_distance (L31)
8	- **Samples**: 5000 per condition (10 tasks x 10 demos x 50 timesteps)
9	- **CF types**: wrong, empty, shuffled, paraphrased
10	- **Runtime**: 06:44 - 09:24 (~2h40m total), EXIT_CODE=0
11	
12	## Conditions Completed (5/5)
13	
14	| # | Model | Suite | Output Path |
15	|---|-------|-------|-------------|
16	| 1 | OpenVLA | Object | `results/libero_object_untrained/counterfactual_combined.json` |
17	| 2 | TracVLA | Spatial | `results/tracvla_spatial/untrained/counterfactual_combined.json` |
18	| 3 | TracVLA | Object | `results/tracvla_object/untrained/counterfactual_combined.json` |
19	| 4 | TracVLA | Goal | `results/tracvla_goal/untrained/counterfactual_combined.json` |
20	| 5 | TracVLA | Long | `results/tracvla_long/untrained/counterfactual_combined.json` |
21	
22	## Results: Untrained Cosine Distance (L31)
23	
24	| Condition | empty | shuffled | wrong | paraphrased | Ordering |
25	|-----------|-------|----------|-------|-------------|----------|
26	| OpenVLA Object | 0.569 | 0.298 | 0.231 | 0.085 | E >> S > W > P |
27	| TracVLA Spatial | 0.180 | 0.140 | 0.005 | 0.004 | E > S >> W ~ P |
28	| TracVLA Object | 0.185 | 0.098 | 0.004 | 0.005 | E >> S >> P ~ W |
29	| TracVLA Goal | 0.153 | 0.084 | 0.016 | 0.004 | E >> S >> W > P |
30	| TracVLA Long | 0.173 | 0.120 | 0.022 | 0.007 | E >> S >> W > P |
31	
32	### Cross-task Cohen's d (L31 global)
33	
34	| Condition | empty | shuffled | wrong | paraphrased |
35	|-----------|-------|----------|-------|-------------|
36	| OpenVLA Object | 16.98 | 11.57 | 5.57 | 9.76 |
37	| TracVLA Spatial | — | — | 1.99 | — |
38	| TracVLA Object | — | — | 1.94 | — |
39	| TracVLA Goal | — | — | 1.29 | — |
40	| TracVLA Long | — | — | 1.87 | — |
41	
42	(Global cohens_d from last_layer_summary; per-task
…[truncated 2691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-29T05:18:07.847575+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-29T05:18:07.847713+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-29T05:18:07.847838+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read all plot scripts and tex files', 'status': 'completed', 'activeForm': 'Reading all plot scripts and tex files'}, {'content': 'Cross-reference script data vs caption numbers', 'status': 'completed', 'activeForm': 'Cross-referencing script data vs caption numbers'}, {'content': 'Verify counterfactual wrong↔shuffled mapping via source JSON', 'status': 'completed', 'activeForm': 'Verifying counterfactual wrong↔shuffled mapping'}, {'content': 'Write audit report to artifacts/audit_figures.md', 'status': 'in_progress', 'activeForm': 'Writing audit report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read all plot scripts and tex files', 'status': 'completed', 'activeForm': 'Reading all plot scripts and tex files'}, {'content': 'Cross-reference script data vs caption numbers', 'status': 'completed', 'activeForm': 'Cross-referencing script data vs caption numbers'}, {'content': 'Verify counterfactual wrong↔shuffled mapping via source JSON', 'status': 'completed', 'activeForm': 'Verifying counterfactual wrong↔shuffled mapping'}, {'content': 'Write audit report to artifacts/audit_figures.md', 'status': 'in_progress', 'activeForm': 'Writing audit report'}]"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-29T05:18:07.848053+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-29T05:18:07.848221+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/audit_figures.md",
  "content": "# 图表数据审计\n\n## 统计\n- 审计图表总数：14（含正文 7 + 附录 7；另有 ~9 个附录图无本地脚本，仅验证 caption 数字）\n- 数据点总数：~750（硬编码在脚本中的数值）\n- 完全匹配：12\n- 问题：2（1 个数据不一致，1 个文本不一致）\n\n---\n\n## 逐图审计\n\n### Figure 1 (fig_teaser): VLA Architecture + 32-Layer Attention Bar\n- 脚本：`scripts/plot_teaser.py`\n- 数据源：硬编码（32-layer bulk extraction）\n- 数据：vla_trained[32], pretrained[32]\n- Caption 数字：无具体数字\n- 数据匹配：✅\n- 详情：teaser 的 32-layer 数据与 multi-layer 4-point 采样使用不同提取方式（bulk vs dedicated），已知差异（appendix 有注释 \"threshold boundary effects\"）。teaser L32=18 与 appendix table L31=18 一致。\n\n### Figure 2 (fig_overview): Analysis Framework Diagram\n- 脚本：`scripts/plot_overview.py`\n- 数据源：概念图，无数值数据\n- 数据匹配：✅ (N/A)\n- 详情：纯架构/方法论示意图，无需数值审计。\n\n### Figure 3 (fig_result_matrix): Cross-Architecture Heatmap\n- 脚本：`scripts/gen_fig_matrix_heatmap.py`\n- 数据源：硬编码（与 Table 1 一致）\n- Caption 数字：ΔR² > 0.10 threshold\n- 数据匹配：✅\n- 详情：全部 10 个有效 cell 的 ΔR² 值与 Table 1 (tab:cross_arch_matrix) 完全一致：\n  - OpenVLA: Goal 0.086, Spatial 0.037, Object 0.037, Long 0.033\n  - TraceVLA: Goal 0.333, Spatial 0.156, Object 0.362, Long 0.358\n  - NORA: Goal 0.455, Spatial 0.308, Object/Long N/A\n\n### Figure 4 (fig_action_r2_threecond): Per-Layer R² Three Conditions\n- 脚本：`scripts/plot_action_r2_threecond.py`\n- 数据源：硬编码（3-seed mean ± std, 32 layers × 3 conditions = 192 values）\n- Caption 数字：\"all share L0 (R² = 0.645)\", \"Trained model peaks at L9\"\n- 数据匹配：✅\n- 详情：\n  - L0 共享值：trained_mean[0] = llama2base_mean[0] = untrained_mean[0] = 0.6451 → 0.645 ✓\n  - Trained L9: trained_mean[9] = 0.6434 → 0.643（3dp 四舍五入）✓\n  - L0 是 embedding 层，L9 是 transformer 处理后的峰值——framing 正确\n  - Appendix text: \"L9 (R² = 0.643 ± 0.014)\" — trained_std[9] = 0.0137 → 0.014 ✓\n  - L0 baseline 水平线：y=0.645 ✓\n\n### Figure 5 (fig_counterfactual_bar): Counterfactual Sensitivity\n- 脚本：`scripts/plot_counterfactual_bar.py`\n- 数据源：硬编码（Panel A: 8×4=32 Cohen's d; Panel B: 8×4=32 cosine dist）\n- Caption 数字：\"E=empty, W=wrong, S=shuffled, P=paraphrased\", \"dashed: d=0.8\"\n- 数据匹配：✅\n- 详情：\n  **Panel A (Cohen's d) 与 Appendix Table 7 (tab:counterfactual) 逐值核对：**\n  | Cell | Script [E,W,S,P] | Table ranking | Match |\n  |------|-----------------|---------------|-------|\n  | OV-G | [1.17, 1.18, 1.10, 1.00] | W 1.18, E 1.17, S 1.10, P 1.00 | ✅ |\n  | OV-S | [1.17, 0.89, 0.98, 0.81] | E 1.17, S 0.98, W 0.89, P 0.81 | ✅ |\n  | OV-O | [1.21, 1.19, 1.12, 0.90] | E 1.21, W 1.19, S 1.12, P 0.90 | ✅ |\n  | OV-L | [0.51, 0.55, 0.57, 0.45] | S 0.57, W 0.55, E 0.51, P 0.45 | ✅ |\n  | TV-G | [1.52, 1.40, 1.34, 1.21] | E 1.52, W 1.40, S 1.34, P 1.21 | ✅ |\n  | TV-S | [1.33, 1.17, 1.30, 1.18] | E 1.33, S 1.30, P 1.18, W 1.17 | ✅ |\n  | TV-O | [1.21, 1.06, 1.16, 0.97] | E 1.21, S 1.16, W 1.06, P 0.97 | ✅ |\n  | TV-L | [1.47, 1.42, 1.39, 1.16] | E 1.47, W 1.42, S 1.39, P 1.16 | ✅ |\n\n  **Main text claims 验证：**\n  - \"Empty ranks first in 6/8 cells\": OV-G(W first), OV-S(E), OV-O(E), OV-L(S first), TV-G(E), TV-S(E), TV-O(E), TV-L(E) → 6/8 ✅\n  - \"Paraphrased ranks last in 7/8\": all except TV-S where W=1.17 is last → 7/8 ✅\n  - \"TraceVLA d = 0.97–1.52\": min TV-O P=0.97, max TV-G E=1.52 ✅\n  - \"OpenVLA d = 0.45–1.21\": min OV-L P=0.45, max OV-O E=1.21 ✅\n\n  **Panel B (Cosine distance) 与 analysis reports 核对：**\n  - NORA Goal trained saturates: [1.0, 1.0, 1.0, 1.0] ✅\n  - Phi-3-Vision Goal (untrained): [0.1530, 0.0160, 0.0839, 0.0043] — 与 cf_batch_part2 report (E=0.153, W=0.016, S=0.084, P=0.004) 一致 ✅\n  - Phi-3-Vision Spatial: [0.1805, 0.0046, 0.1395, 0.0044] — 与 cf_batch_missing report (E=0.180, S=0.140, W=0.005, P=0.004) 一致 ✅\n  - Phi-3-Vision Object: [0.1850, 0.0044, 0.0977, 0.0052] — 与 report (E=0.185, S=0.098, W=0.004, P=0.005) 一致 ✅\n\n  **已知问题验证 — TraceVLA Spatial/Object wrong↔shuffled：**\n  ✅ **NOT AN ISSUE**。通过 `cf_batch_missing_v1_analysis.md` 和 `cf_batch_part2_v1_analysis.md` 交叉验证，trained ordering 与脚本中的条件映射完全一致：\n  - TV-S trained: E(1.33) > S(1.30) > P(1.18) > W(1.17) — report confirms \"E > S > P > W\"\n  - TV-O trained: E(1.21) > S(1.16) > W(1.06) > P(0.97) — report confirms \"E > S > W > P\"\n  条件数组 `['empty', 'wrong', 'shuffled', 'paraphrased']` 映射正确，wrong 和 shuffled 未交换。\n\n### Figure 6 (fig_r2_collapse): Layer-Wise R² Three-Panel\n- 脚本：`scripts/plot_r2_collapse.py`\n- 数据源：硬编码（3 panels × 2 curves = 6 arrays, total ~200 values）\n- Caption 数字：\"ΔR² = 0.16–0.46\", \"< 0.09\", \"ΔR² = 0.000\", \"R² = 0.155\"\n- 数据匹配：✅\n- 详情：\n  **Peak/exit/ΔR² 与 Table 1 核对：**\n  | Panel | Peak idx | Peak R² | Exit R² | ΔR² | Table | Match |\n  |-------|----------|---------|---------|-----|-------|-------|\n  | OpenVLA tr | L1 | 0.418 | 0.331 | 0.086 | 0.086 | ✅ |\n  | OpenVLA ref | L27 | 0.423 | 0.367 | 0.056 | 0.056 | ✅ |\n  | TraceVLA tr | L13 | 0.540 | 0.207 | 0.333 | 0.333 | ✅ |\n  | TraceVLA ref | L11 | 0.505 | 0.440 | 0.065 | 0.065 | ✅ |\n  | NORA tr | L8 | 0.449 | -0.006 | 0.455 | 0.455 | ✅ |\n  | NORA ref | L5 | 0.420 | 0.340 | 0.081 | 0.081 | ✅ |\n\n  - NLP_VAL = 0.155 in script, caption says \"R² = 0.155\" ✅\n  - Caption \"ΔR² = 0.16–0.46\": full range across table is 0.156–0.455 ✅\n  - Caption \"< 0.09\": OpenVLA max trained ΔR² = 0.086 < 0.09 ✅\n  - NLP_VAL 使用单一值 0.155 代表三个不同 NLP 模型（见下方 ℹ️ 注释）\n\n### Figure 7 (fig_synthesis_panels): Multi-Layer Attention + Dose-Response\n- 脚本（左）：`scripts/plot_multi_layer_attention.py`\n- 脚本（右）：`scripts/plot_dose_response.py`\n- Caption 数字：\"L1: 24, L31: 18\" (left); \"d = 0.48–0.64\" (right)\n- 数据匹配：⚠️ 左 panel L31 值不一致\n\n  **左 Panel (Multi-Layer Attention):**\n  - Script: trained_heads = [24, 4, 10, 19] for [L1, L8, L16, L31]\n  - Main text: \"L1: 24, L31: 18\"\n  - Appendix Table 10: L31 Trained = 18/32\n  - **⚠️ 脚本 L31 = 19, 论文 = 18** — 差值 1 head\n  - L1=24, L8=4, L16=10 与 appendix table 一致 ✅\n  - Llama-2 base: script [9, 8, 25, 8] 与 table [9, 8, 25, 8] ✅\n  - Untrained: script [0, 0, 0, 0] 与 table [0, 0, 0, 0] ✅\n\n  **右 Panel (Dose-Response):**\n  - Script values 与 Appendix Table 8 (tab:dose_response) 逐值核对（8 data points + 16 CI bounds）：全部匹配 ✅\n  - d range: 0.482–0.639 → \"0.48–0.64\" ✓\n  - Control line: ref_control_d = 0.41 — appendix \"d = 0.41\" ✅\n\n### Figure (fig_rsa_perlayer_curve): Per-Layer RSA\n- 脚本：`scripts/plot_rsa_perlayer.py`\n- 数据源：硬编码（4 curves × 33 layers + CI bounds）\n- Caption 数字：\"Trained: inverted-U peaking at L12; reference: monotonic decline\"\n- 数据匹配：✅\n- 详情：\n  - Trained image_mean peak: L12, ti_m[12] = 0.6282 → \"0.628\" ✓\n  - Trained readout peak: L12, tp_m[12] = 0.6425 → \"0.643\" ✓\n  - Method.tex says ρ = 0.584 (readout exit) and 0.422 (image_mean exit): tp_m[32]=0.5843→0.584 ✅, ti_m[32]=0.4223→0.422 ✅\n\n### Figure (fig_l1_attention / fig_cross_arch_l1): Cross-Architecture L1 Bar\n- 脚本：`scripts/plot_l1_attention.py`\n- 数据源：硬编码\n- Caption 数字：无具体数字\n- 数据匹配：⚠️ 附近文本值不完全匹配\n- 详情：\n  - Script: ref_counts = [26, 32, 14], trained_counts = [23, 29, 13]\n  - Appendix paragraph near figure: \"OpenVLA: 23/32 vs. 26/32\" ✅\n  - Appendix paragraph: \"TraceVLA: **27**/32 vs. 32/32\" — script plots **29**/32 ⚠️\n  - Appendix paragraph: \"NORA: 13/16 vs. **13**/16\" — script ref = **14**/16 ⚠️\n  - experiments.tex 使用范围值 \"27–30/32\" 和 \"13–14/16\"，script 值在范围内\n  - Main text 对 OpenVLA 使用 dedicated analysis 值 24/32，与此图的 bulk extraction 值 23/32 是已知方法差异（documented in appendix）\n\n### Figure (fig_training_dynamics): ΔR² Strip Plot\n- 脚本：`scripts/plot_training_dynamics.py`\n- 数据源：硬编码（与 Table 1 相同数据）\n- Caption 数字：无\n- 数据匹配：✅\n- 详情：全部 23 个数据点与 Table 1 逐值一致（4 VLA→VLA trained, 6 VLM→VLA trained, 10 reference, 3 NLP）。\n\n### Figure (fig_label_permutation): Label Permutation Control\n- 脚本：`scripts/plot_label_permutation.py`\n- 数据源：硬编码\n- Caption 数字：\"ρ drops from 0.955 to 0.001 (trained) and from 0.933 to 0.000 (reference)\"\n- 数据匹配：✅\n- 详情：real_rho = [0.955, 0.933], shuf_rho = [0.0012, 0.0003] → 0.001 和 0.000（四舍五入）✓\n\n### Figure (fig_nlp_control_r2): NLP Control Overlay (Appendix)\n- 脚本：`scripts/plot_nlp_control_overlay.py`\n- 数据源：硬编码（与 fig_r2_collapse 完全相同的数据数组）\n- 数据匹配：✅\n- 详情：数据与 fig_r2_collapse 完全一致（共用同一组数值）。NLP_VAL = 0.155。\n\n### Figure (fig_claim_evidence): Claim-Evidence Summary (Appendix)\n- 脚本：`scripts/plot_claim_evidence.py`\n- 数据源：概念图\n- 数据匹配：✅ (N/A)\n- 详情：结构化摘要图，文本内容与论文 findings 一致。\"6/6 VLM→VLA conditions show Δ > 0.10; 0/4 VLA→VLA; 0/10 reference conditions\" 与 Table 1 一致。\"Cohen's d ≥ 0.45\" 与 counterfactual 数据最小值 OV-L P=0.45 一致。\n\n### 附录 Figures（无本地脚本，仅验证 caption 数字）\n\n以下 figures 在附录中引用，但无本地 plot 脚本。通过 caption 中的数字与正文/表格交叉验证：\n\n| Figure | File | Caption 关键数字 | 验证 |\n|--------|------|----------------|------|\n| fig_metric_comparison | fig6.pdf | RSA: DINOv2 0.692, Fused 0.634, Proj 0.615; CKA: Ref 0.089, Trained 0.083 | ✅ 与附录文本一致 |\n| fig_rsa_bar | fig2.pdf | DINOv2 cls ρ=0.692, CLIP 0.557 | ✅ 与附录文本一致 |\n| fig_cross_benchmark | fig7.pdf | Spatial RSA L14 ρ=0.691, Δ=+0.023 | ✅ 与附录文本一致 |\n| fig_ood_diagnostics | fig_ood_diagnostics.pdf | 无具体数字 in caption | ✅ N/A |\n| fig_linear_vs_mlp | fig_linear_vs_mlp_probe.pdf | 无具体数字 in caption | ✅ N/A |\n| fig_probe_bars | fig4.pdf | R²=0.678 L13, 0.655 L8, 0.630 proj | ✅ 与 tab:training_effect_summary 一致 |\n| fig_factorial | fig5.pdf | RSA peak shift L0(0.612)→L12(0.628), Δ=+0.017; |Δ|<0.006 | ✅ 与附录表格一致 |\n| fig_random_subset_ablation | fig_specificity_bootstrap_30seeds.pdf | dominant +0.030, random +0.071±0.013, z=-3.11 | ✅ 与附录文本一致 |\n| fig_probe_conditions | fig_probe_conditions.pdf | 99.6% at L1, 100% saturation, 82% L31 decay | ✅ 与 tab:dense_routing 一致 |\n\n---\n\n## 问题清单\n\n### ⚠️ P1: plot_multi_layer_attention.py L31 trained = 19, 论文 = 18\n- **位置**：Figure 7 左 panel（fig_multi_layer_attn.pdf），L31 数据点\n- **脚本值**：`trained_heads = [24, 4, 10, 19]` → L31 = 19\n- **论文值**：\n  - experiments.tex line 131: \"L1: 24, L31: 18\"\n  - appendix Table 10 (tab:multilayer_attention): L31 Trained = 18/32\n  - plot_teaser.py: vla_trained[31] = 18（同一个数据的另一来源）\n- **影响**：Figure 7 左 panel 中 L31 的 VLA-trained 数据点偏高 1 head（19 vs 18）\n- **根因推测**：脚本硬编码时可能使用了不同 threshold 或不同 batch 的提取结果；teaser 和 appendix table 使用了更新后的数据\n- **严重程度**：低（1/32 head 差异，不影响定性结论）\n\n### ⚠️ P2: Appendix 段落文本与 fig_l1_attention 脚本数据不一致\n- **位置**：appendix.tex line 725 附近段落\n- **文本值**：\"TraceVLA: 27/32 vs. 32/32\" 和 \"NORA: 13/16 vs. 13/16\"\n- **脚本值**：TraceVLA trained = 29/32, NORA ref = 14/16\n- **影响**：appendix 正文中引用的具体值与图表实际绘制的值不一致（尽管 experiments.tex 使用了覆盖这些值的范围表述 \"27–30/32\" 和 \"13–14/16\"）\n- **严重程度**：低（在论文认可的范围内，但段落中的 point estimate 与图不匹配）\n\n### ℹ️ INFO: NLP control R² = 0.155 统一值\n- **位置**：fig_r2_collapse (Figure 6) 和 fig_nlp_control_r2，NLP_VAL = 0.155\n- **说明**：三个不同的 NLP 模型（Llama-2-chat, Phi-3-instruct, Qwen2.5-Instruct）共用同一个 R² = 0.155 水平线。如果这是三个模型的平均值或代表值，属于合理简化。但如果三个模型各有不同的 R² 值，则图表丢失了差异信息。\n- **论文 claim**：ΔR² = 0.000（flat profile），不依赖 R² 的绝对值\n- **严重程度**：信息性，不影响结论\n\n### ✅ RESOLVED: TraceVLA Spatial/Object wrong↔shuffled 交换\n- **原始关注**：Figure 5 中 TraceVLA Spatial 和 Object 的 wrong 与 shuffled 值可能交换\n- **验证结果**：通过 `cf_batch_missing_v1_analysis.md` 和 `cf_batch_part2_v1_analysis.md` 分析报告交叉验证，trained ordering 与脚本中的条件映射完全一致\n- **结论**：条件映射正确，wrong 和 shuffled 未交换\n\n### ✅ RESOLVED: OpenVLA L1 heads 24 vs 23\n- **说明**：main text 使用 dedicated L1 analysis 的 24/32，bar chart 使用 32-layer bulk extraction 的 23/32。差异来自不同提取方法（threshold boundary effects），appendix 已明确注释。\n- **结论**：已知方法差异，不是数据错误\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/audit_figures.md",
    "content": "# 图表数据审计\n\n## 统计\n- 审计图表总数：14（含正文 7 + 附录 7；另有 ~9 个附录图无本地脚本，仅验证 caption 数字）\n- 数据点总数：~750（硬编码在脚本中的数值）\n- 完全匹配：12\n- 问题：2（1 个数据不一致，1 个文本不一致）\n\n---\n\n## 逐图审计\n\n### Figure 1 (fig_teaser): VLA Architecture + 32-Layer Attention Bar\n- 脚本：`scripts/plot_teaser.py`\n- 数据源：硬编码（32-layer bulk extraction）\n- 数据：vla_trained[32], pretrained[32]\n- Caption 数字：无具体数字\n- 数据匹配：✅\n- 详情：teaser 的 32-layer 数据与 multi-layer 4-point 采样使用不同提取方式（bulk vs dedicated），已知差异（appendix 有注释 \"threshold boundary effects\"）。teaser L32=18 与 appendix table L31=18 一致。\n\n### Figure 2 (fig_overview): Analysis Framework Diagram\n- 脚本：`scripts/plot_overview.py`\n- 数据源：概念图，无数值数据\n- 数据匹配：✅ (N/A)\n- 详情：纯架构/方法论示意图，无需数值审计。\n\n### Figure 3 (fig_result_matrix): Cross-Architecture Heatmap\n- 脚本：`scripts/gen_fig_matrix_heatmap.py`\n- 数据源：硬编码（与 Table 1 一致）\n- Caption 数字：ΔR² > 0.10 threshold\n- 数据匹配：✅\n- 详情：全部 10 个有效 cell 的 ΔR² 值与 Table 1 (tab:cross_arch_matrix) 完全一致：\n  - OpenVLA: Goal 0.086, Spatial 0.037, Object 0.037, Long 0.033\n  - TraceVLA: Goal 0.333, Spatial 0.156, Object 0.362, Long 0.358\n  - NORA: Goal 0.455, Spatial 0.308, Object/Long N/A\n\n### Figure 4 (fig_action_r2_threecond): Per-Layer R² Three Conditions\n- 脚本：`scripts/plot_action_r2_threecond.py`\n- 数据源：硬编码（3-seed mean ± std, 32 layers × 3 conditions = 192 values）\n- Caption 数字：\"all share L0 (R² = 0.645)\", \"Trained model peaks at L9\"\n- 数据匹配：✅\n- 详情：\n  - L0 共享值：trained_mean[0] = llama2base_mean[0] = untrained_mean[0] = 0.6451 → 0.645 ✓\n  - Trained L9: trained_mean[9] = 0.6434 → 0.643（3dp 四舍五入）✓\n  - L0 是 embedding 层，L9 是 transformer 处理后的峰值——framing 正确\n  - Appendix text: \"L9 (R² = 0.643 ± 0.014)\" — trained_std[9] = 0.0137 → 0.014 ✓\n  - L0 baseline 水平线：y=0.645 ✓\n\n### Figure 5 (fig_counterfactual_bar): Counterfactual Sensitivity\n- 脚本：`scripts/plot_counterfactual_bar.py`\n- 数据源：硬编码（Panel A: 8×4=32 Cohen's d; Panel B: 8×4=32 cosine dist）\n- Caption 数字：\"E=empty, W=wrong, S=shuffled, P=paraphrased\", \"dashed: d=0.8\"\n- 数据匹配：✅\n- 详情：\n  **Panel A (Cohen's d) 与 Appendix Table 7 (tab:counterfactual) 逐值核对：**\n  | Cell | Script [E,W,S,P] | Table ranking | Match |\n  |------|-----------------|---------------|-------|\n  | OV-G | [1.17, 1.18, 1.10, 1.00] | W 1.18, E 1.17, S 1.10, P 1.00 | ✅ |\n  | OV-S | [1.17, 0.89, 0.98, 0.81] | E 1.17, S 0.98, W 0.89, P 0.81 | ✅ |\n  | OV-O | [1.21, 1.19, 1.12, 0.90] | E 1.21, W 1.19, S 1.12, P 0.90 | ✅ |\n  | OV-L | [0.51, 0.55, 0.57, 0.45] | S 0.57, W 0.55, E 0.51, P 0.45 | ✅ |\n  | TV-G | [1.52, 1.40, 1.34, 1.21] | E 1.52, W 1.40, S 1.34, P 1.21 | ✅ |\n  | TV-S | [1.33, 1.17, 1.30, 1.18] | E 1.33, S 1.30, P 1.18, W 1.17 | ✅ |\n  | TV-O | [1.21, 1.06, 1.16, 0.97] | E 1.21, S 1.16, W 1.06, P 0.97 | ✅ |\n  | TV-L | [1.47, 1.42, 1.39, 1.16] | E 1.47, W 1.42, S 1.39, P 1.16 | ✅ |\n\n  **Main text claims 验证：**\n  - \"Empty ranks first in 6/8 cells\": OV-G(W first), OV-S(E), OV-O(E), OV-L(S first), TV-G(E), TV-S(E), TV-O(E), TV-L(E) → 6/8 ✅\n  - \"Paraphrased ranks last in 7/8\": all except TV-S where W=1.17 is last → 7/8 ✅\n  - \"TraceVLA d = 0.97–1.52\": min TV-O P=0.97, max TV-G E=1.52 ✅\n  - \"OpenVLA d = 0.45–1.21\": min OV-L P=0.45, max OV-O E=1.21 ✅\n\n  **Panel B (Cosine distance) 与 analysis reports 核对：**\n  - NORA Goal trained saturates: [1.0, 1.0, 1.0, 1.0] ✅\n  - Phi-3-Vision Goal (untrained): [0.1530, 0.0160, 0.0839, 0.0043] — 与 cf_batch_part2 report (E=0.153, W=0.016, S=0.084, P=0.004) 一致 ✅\n  - Phi-3-Vision Spatial: [0.1805, 0.0046, 0.1395, 0.0044] — 与 cf_batch_missing report (E=0.180, S=0.140, W=0.005, P=0.004) 一致 ✅\n  - Phi-3-Vision Object: [0.1850, 0.0044, 0.0977, 0.0052] — 与 report (E=0.185, S=0.098, W=0.004, P=0.005) 一致 ✅\n\n  **已知问题验证 — TraceVLA Spatial/Object wrong↔shuffled：**\n  ✅ **NOT AN ISSUE**。通过 `cf_batch_missing_v1_analysis.md` 和 `cf_batch_part2_v1_analysis.md` 交叉验证，trained ordering 与脚本中的条件映射完全一致：\n  - TV-S trained: E(1.33) > S(1.30) > P(1.18) > W(1.17) — report confirms \"E > S > P > W\"\n  - TV-O trained: E(1.21) > S(1.16) > W(1.06) > P(0.97) — report confirms \"E > S > W > P\"\n  条件数组 `['empty', 'wrong', 'shuffled', 'paraphrased']` 映射正确，wrong 和 shuffled 未交换。\n\n### Figure 6 (fig_r2_collapse): Layer-Wise R² Three-Panel\n- 脚本：`scripts/plot_r2_collapse.py`\n- 数据源：硬编码（3 panels × 2 curves = 6 arrays, total ~200 values）\n- Caption 数字：\"ΔR² = 0.16–0.46\", \"< 0.09\", \"ΔR² = 0.000\", \"R² = 0.155\"\n- 数据匹配：✅\n- 详情：\n  **Peak/exit/ΔR² 与 Table 1 核对：**\n  | Panel | Peak idx | Peak R² | Exit R² | ΔR² | Table | Match |\n  |-------|----------|---------|---------|-----|-------|-------|\n  | OpenVLA tr | L1 | 0.418 | 0.331 | 0.086 | 0.086 | ✅ |\n  | OpenVLA ref | L27 | 0.423 | 0.367 | 0.056 | 0.056 | ✅ |\n  | TraceVLA tr | L13 | 0.540 | 0.207 | 0.333 | 0.333 | ✅ |\n  | TraceVLA ref | L11 | 0.505 | 0.440 | 0.065 | 0.065 | ✅ |\n  | NORA tr | L8 | 0.449 | -0.006 | 0.455 | 0.455 | ✅ |\n  | NORA ref | L5 | 0.420 | 0.340 | 0.081 | 0.081 | ✅ |\n\n  - NLP_VAL = 0.155 in script, caption says \"R² = 0.155\" ✅\n  - Caption \"ΔR² = 0.16–0.46\": full range across table is 0.156–0.455 ✅\n  - Caption \"< 0.09\": OpenVLA max trained ΔR² = 0.086 < 0.09 ✅\n  - NLP_VAL 使用单一值 0.155 代表三个不同 NLP 模型（见下方 ℹ️ 注释）\n\n### Figure 7 (fig_synthesis_panels): Multi-Layer Attention + Dose-Response\n- 脚本（左）：`scripts/plot_multi_layer_attention.py`\n- 脚本（右）：`scripts/plot_dose_response.py`\n- Caption 数字：\"L1: 24, L31: 18\" (left); \"d = 0.48–0.64\" (right)\n- 数据匹配：⚠️ 左 panel L31 值不一致\n\n  **左 Panel (Multi-Layer Attention):**\n  - Script: trained_heads = [24, 4, 10, 19] for [L1, L8, L16, L31]\n  - Main text: \"L1: 24, L31: 18\"\n  - Appendix Table 10: L31 Trained = 18/32\n  - **⚠️ 脚本 L31 = 19, 论文 = 18** — 差值 1 head\n  - L1=24, L8=4, L16=10 与 appendix table 一致 ✅\n  - Llama-2 base: script [9, 8, 25, 8] 与 table [9, 8, 25, 8] ✅\n  - Untrained: script [0, 0, 0, 0] 与 table [0, 0, 0, 0] ✅\n\n  **右 Panel (Dose-Response):**\n  - Script values 与 Appendix Table 8 (tab:dose_response) 逐值核对（8 data points + 16 CI bounds）：全部匹配 ✅\n  - d range: 0.482–0.639 → \"0.48–0.64\" ✓\n  - Control line: ref_control_d = 0.41 — appendix \"d = 0.41\" ✅\n\n### Figure (fig_rsa_perlayer_curve): Per-Layer RSA\n- 脚本：`scripts/plot_rsa_perlayer.py`\n- 数据源：硬编码（4 curves × 33 layers + CI bounds）\n- Caption 数字：\"Trained: inverted-U peaking at L12; reference: monotonic decline\"\n- 数据匹配：✅\n- 详情：\n  - Trained image_mean peak: L12, ti_m[12] = 0.6282 → \"0.628\" ✓\n  - Trained readout peak: L12, tp_m[12] = 0.6425 → \"0.643\" ✓\n  - Method.tex says ρ = 0.584 (readout exit) and 0.422 (image_mean exit): tp_m[32]=0.5843→0.584 ✅, ti_m[32]=0.4223→0.422 ✅\n\n### Figure (fig_l1_attention / fig_cross_arch_l1): Cross-Architecture L1 Bar\n- 脚本：`scripts/plot_l1_attention.py`\n- 数据源：硬编码\n- Caption 数字：无具体数字\n- 数据匹配：⚠️ 附近文本值不完全匹配\n- 详情：\n  - Script: ref_counts = [26, 32, 14], trained_counts = [23, 29, 13]\n  - Appendix paragraph near figure: \"OpenVLA: 23/32 vs. 26/32\" ✅\n  - Appendix paragraph: \"TraceVLA: **27**/32 vs. 32/32\" — script plots **29**/32 ⚠️\n  - Appendix paragraph: \"NORA: 13/16 vs. **13**/16\" — script ref = **14**/16 ⚠️\n  - experiments.tex 使用范围值 \"27–30/32\" 和 \"13–14/16\"，script 值在范围内\n  - Main text 对 OpenVLA 使用 dedicated analysis 值 24/32，与此图的 bulk extraction 值 23/32 是已知方法差异（documented in appendix）\n\n### Figure (fig_training_dynamics): ΔR² Strip Plot\n- 脚本：`scripts/plot_training_dynamics.py`\n- 数据源：硬编码（与 Table 1 相同数据）\n- Caption 数字：无\n- 数据匹配：✅\n- 详情：全部 23 个数据点与 Table 1 逐值一致（4 VLA→VLA trained, 6 VLM→VLA trained, 10 reference, 3 NLP）。\n\n### Figure (fig_label_permutation): Label Permutation Control\n- 脚本：`scripts/plot_label_permutation.py`\n- 数据源：硬编码\n- Caption 数字：\"ρ drops from 0.955 to 0.001 (trained) and from 0.933 to 0.000 (reference)\"\n- 数据匹配：✅\n- 详情：real_rho = [0.955, 0.933], shuf_rho = [0.0012, 0.0003] → 0.001 和 0.000（四舍五入）✓\n\n### Figure (fig_nlp_control_r2): NLP Control Overlay (Appendix)\n- 脚本：`scripts/plot_nlp_control_overlay.py`\n- 数据源：硬编码（与 fig_r2_collapse 完全相同的数据数组）\n- 数据匹配：✅\n- 详情：数据与 fig_r2_collapse 完全一致（共用同一组数值）。NLP_VAL = 0.155。\n\n### Figure (fig_claim_evidence): Claim-Evidence Summary (Appendix)\n- 脚本：`scripts/plot_claim_evidence.py`\n- 数据源：概念图\n- 数据匹配：✅ (N/A)\n- 详情：结构化摘要图，文本内容与论文 findings 一致。\"6/6 VLM→VLA conditions show Δ > 0.10; 0/4 VLA→VLA; 0/10 reference conditions\" 与 Table 1 一致。\"Cohen's d ≥ 0.45\" 与 counterfactual 数据最小值 OV-L P=0.45 一致。\n\n### 附录 Figures（无本地脚本，仅验证 caption 数字）\n\n以下 figures 在附录中引用，但无本地 plot 脚本。通过 caption 中的数字与正文/表格交叉验证：\n\n| Figure | File | Caption 关键数字 | 验证 |\n|--------|------|----------------|------|\n| fig_metric_comparison | fig6.pdf | RSA: DINOv2 0.692, Fused 0.634, Proj 0.615; CKA: Ref 0.089, Trained 0.083 | ✅ 与附录文本一致 |\n| fig_rsa_bar | fig2.pdf | DINOv2 cls ρ=0.692, CLIP 0.557 | ✅ 与附录文本一致 |\n| fig_cross_benchmark | fig7.pdf | Spatial RSA L14 ρ=0.691, Δ=+0.023 | ✅ 与附录文本一致 |\n| fig_ood_diagnostics | fig_ood_diagnostics.pdf | 无具体数字 in caption | ✅ N/A |\n| fig_linear_vs_mlp | fig_linear_vs_mlp_probe.pdf | 无具体数字 in caption | ✅ N/A |\n| fig_probe_bars | fig4.pdf | R²=0.678 L13, 0.655 L8, 0.630 proj | ✅ 与 tab:training_effect_summary 一致 |\n| fig_factorial | fig5.pdf | RSA peak shift L0(0.612)→L12(0.628), Δ=+0.017; |Δ|<0.006 | ✅ 与附录表格一致 |\n| fig_random_subset_ablation | fig_specificity_bootstrap_30seeds.pdf | dominant +0.030, random +0.071±0.013, z=-3.11 | ✅ 与附录文本一致 |\n| fig_probe_conditions | fig_probe_conditions.pdf | 99.6% at L1, 100% saturation, 82% L31 decay | ✅ 与 tab:dense_routing 一致 |\n\n---\n\n## 问题清单\n\n### ⚠️ P1: plot_multi_layer_attention.py L31 trained = 19, 论文 = 18\n- **位置**：Figure 7 左 panel（fig_multi_layer_attn.pdf），L31 数据点\n- **脚本值**：`trained_heads = [24, 4, 10, 19]` → L31 = 19\n- **论文值**：\n  - experiments.tex line 131: \"L1: 24, L31: 18\"\n  - appendix Table 10 (tab:multilayer_attention): L31 Trained = 18/32\n  - plot_teaser.py: vla_trained[31] = 18（同一个数据的另一来源）\n- **影响**：Figure 7 左 panel 中 L31 的 VLA-trained 数据点偏高 1 head（19 vs 18）\n- **根因推测**：脚本硬编码时可能使用了不同 threshold 或不同 batch 的提取结果；teaser 和 appendix table 使用了更新后的数据\n- **严重程度**：低（1/32 head 差异，不影响定性结论）\n\n### ⚠️ P2: Appendix 段落文本与 fig_l1_attention 脚本数据不一致\n- **位置**：appendix.tex line 725 附近段落\n- **文本值**：\"TraceVLA: 27/32 vs. 32/32\" 和 \"NORA: 13/16 vs. 13/16\"\n- **脚本值**：TraceVLA trained = 29/32, NORA ref = 14/16\n- **影响**：appendix 正文中引用的具体值与图表实际绘制的值不一致（尽管 experiments.tex 使用了覆盖这些值的范围表述 \"27–30/32\" 和 \"13–14/16\"）\n- **严重程度**：低（在论文认可的范围内，但段落中的 point estimate 与图不匹配）\n\n### ℹ️ INFO: NLP control R² = 0.155 统一值\n- **位置**：fig_r2_collapse (Figure 6) 和 fig_nlp_control_r2，NLP_VAL = 0.155\n- **说明**：三个不同的 NLP 模型（Llama-2-chat, Phi-3-instruct, Qwen2.5-Instruct）共用同一个 R² = 0.155 水平线。如果这是三个模型的平均值或代表值，属于合理简化。但如果三个模型各有不同的 R² 值，则图表丢失了差异信息。\n- **论文 claim**：ΔR² = 0.000（flat profile），不依赖 R² 的绝对值\n- **严重程度**：信息性，不影响结论\n\n### ✅ RESOLVED: TraceVLA Spatial/Object wrong↔shuffled 交换\n- **原始关注**：Figure 5 中 TraceVLA Spatial 和 Object 的 wrong 与 shuffled 值可能交换\n- **验证结果**：通过 `cf_batch_missing_v1_analysis.md` 和 `cf_batch_part2_v1_analysis.md` 分析报告交叉验证，trained ordering 与脚本中的条件映射完全一致\n- **结论**：条件映射正确，wrong 和 shuffled 未交换\n\n### ✅ RESOLVED: OpenVLA L1 heads 24 vs 23\n- **说明**：main text 使用 dedicated L1 analysis 的 24/32，bar chart 使用 32-layer bulk extraction 的 23/32。差异来自不同提取方法（threshold boundary effects），appendix 已明确注释。\n- **结论**：已知方法差异，不是数据错误\n"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-29T05:18:07.848513+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/audit_figures.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-29T05:18:07.848649+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read all plot scripts and tex files', 'status': 'completed', 'activeForm': 'Reading all plot scripts and tex files'}, {'content': 'Cross-reference script data vs caption numbers', 'status': 'completed', 'activeForm': 'Cross-referencing script data vs caption numbers'}, {'content': 'Verify counterfactual wrong↔shuffled mapping via source JSON', 'status': 'completed', 'activeForm': 'Verifying counterfactual wrong↔shuffled mapping'}, {'content': 'Write audit report to artifacts/audit_figures.md', 'status': 'completed', 'activeForm': 'Writing audit report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read all plot scripts and tex files', 'status': 'completed', 'activeForm': 'Reading all plot scripts and tex files'}, {'content': 'Cross-reference script data vs caption numbers', 'status': 'completed', 'activeForm': 'Cross-referencing script data vs caption numbers'}, {'content': 'Verify counterfactual wrong↔shuffled mapping via source JSON', 'status': 'completed', 'activeForm': 'Verifying counterfactual wrong↔shuffled mapping'}, {'content': 'Write audit report to artifacts/audit_figures.md', 'status': 'completed', 'activeForm': 'Writing audit report'}]"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-29T05:18:07.848809+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_figures_data_20260529T050826",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 83 · 2026-05-29T05:18:07.848993+00:00_

审计完成。报告已写入 `artifacts/audit_figures.md`。

**结果：14 图审计，~750 数据点，发现 2 个问题：**

1. **⚠️ P1** `plot_multi_layer_attention.py` L31 trained = **19**，论文和 teaser 均为 **18**。差 1 head，不影响结论。
2. **⚠️ P2** 附录段落引用 TraceVLA trained = 27/32 和 NORA ref = 13/16，但 `plot_l1_attention.py` 实际绘制 29/32 和 14/16。experiments.tex 使用范围值覆盖了这些差异。

**已排除的已知关注：**
- TraceVLA Spatial/Object wrong↔shuffled 交换 → ✅ 通过源数据报告验证，映射正确
- OpenVLA L1 24 vs 23 → ✅ 已知方法差异（dedicated vs bulk extraction）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_figures_data_20260529T050826"
}
```

</details>

---
