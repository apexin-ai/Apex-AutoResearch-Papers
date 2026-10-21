# analysis r16 w1 routing variance

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_analysis_r16-w1-routing-variance_20260523T135203.jsonl`
- **Structured JSON:** [`b694e4165ea6ad820034.json`](../../sessions/b6/b694e4165ea6ad820034.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-23T13:55:27.505913+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/ -type f \\( -name \"*routing*\" -o -name \"*rescue*\" -o -name \"*cross_val*\" -o -name \"*oracle*\" -o -name \"*threshold*\" \\) 2>/dev/null",
  "description": "Search for routing/rescue related files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/ -type f \\( -name \"*routing*\" -o -name \"*rescue*\" -o -name \"*cross_val*\" -o -name \"*oracle*\" -o -name \"*threshold*\" \\) 2>/dev/null",
    "description": "Search for routing/rescue related files"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T13:55:27.506389+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/figures/paper/gen_fig3_alpha_routing.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/figures/paper/fig3_alpha_routing.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/figures/paper/fig3_alpha_routing.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_analysis_r16-w1-routing-variance_20260523T135203.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T13:55:27.506692+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/ -type f 2>/dev/null | head -80",
  "description": "List artifact files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/ -type f 2>/dev/null | head -80",
    "description": "List artifact files"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T13:55:27.507015+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_12/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_8/_pdf_images_appendix/submitted_p11.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_8/_pdf_images_appendix/submitted_p18.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_8/_pdf_images_appendix/submitted_p12.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_8/_pdf_images_appendix/submitted_p15.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_8/_pdf_images_appendix/submitted_p16.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_8/_pdf_images_appendix/submitted_p17.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_8/_pdf_images_appendix/submitted_p14.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_8/_pdf_images_appendix/submitted_p13.png
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/review_round_8/submitted.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/scripts/e3_calibration.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/scripts/e2_continuous_jaccard.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/per_example_table.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/decoupling_data.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/convergence_table.csv
/home/
…[truncated 8472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T13:55:27.507287+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T13:55:27.507509+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T13:55:27.507806+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -rl -i \"routing\\|rescue\\|cross.val\\|oracle\\|majority.vote\" /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/ 2>/dev/null",
  "description": "Search for routing-related content in data files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -rl -i \"routing\\|rescue\\|cross.val\\|oracle\\|majority.vote\" /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/ 2>/dev/null",
    "description": "Search for routing-related content in data files"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T13:55:27.508035+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/a3_complementarity_decomposition.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/a2_confidence_prediction.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/majority_vote_and_rho_analysis.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/confidence_margin_analysis.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/e1_confidence_selection.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/e1_confidence_selection_e4231e.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T13:55:27.508240+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/figures/paper/gen_fig3_alpha_routing.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/figures/paper/gen_fig3_alpha_routing.py"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T13:55:27.508492+00:00_

1	import matplotlib
2	matplotlib.use('Agg')
3	import matplotlib.pyplot as plt
4	import numpy as np
5	
6	plt.rcParams.update({
7	    'font.family': 'DejaVu Sans',
8	    'font.size': 13,
9	    'axes.titlesize': 14,
10	    'axes.labelsize': 14,
11	    'xtick.labelsize': 12,
12	    'ytick.labelsize': 12,
13	    'legend.fontsize': 11,
14	    'figure.dpi': 300,
15	    'savefig.dpi': 300,
16	    'savefig.bbox': 'tight',
17	    'savefig.pad_inches': 0.05,
18	    'axes.spines.top': False,
19	    'axes.spines.right': False,
20	    'pdf.fonttype': 42,
21	    'ps.fonttype': 42,
22	})
23	
24	# --- Data from paper ---
25	benchmarks = ['PIQA', 'HellaSwag', 'ARC-Easy', 'LAMBADA']
26	alpha_values = [0.14, 0.15, 0.21, 0.30]
27	categories = ['Reasoning', 'Reasoning', 'Mixed', 'Retrieval']
28	
29	# Routing gains (pp over majority vote)
30	routing_gains = [-0.6, 0.0, 1.0, 5.3]
31	
32	# Oracle gap extraction (%)
33	oracle_pct = [0, 0, 12, 36]  # approximate from paper
34	
35	# Colors by category
36	cat_colors = {
37	    'Reasoning': '#4DBBD5',
38	    'Mixed': '#E64B35',
39	    'Retrieval': '#3C5488',
40	}
41	bar_colors = [cat_colors[c] for c in categories]
42	
43	fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.2), gridspec_kw={'width_ratios': [1, 1]})
44	
45	# --- Panel (a): Alpha spectrum ---
46	x = np.arange(len(benchmarks))
47	bars = ax1.bar(x, alpha_values, color=bar_colors, width=0.6, edgecolor='white', linewidth=0.5)
48	
49	# Add value labels
50	for i, (bar, val) in enumerate(zip(bars, alpha_values)):
51	    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.008,
52	             f'{val:.2f}', ha='center', va='bottom', fontsize=11, fontweight='bold')
53	
54	ax1.set_xticks(x)
55	ax1.set_xticklabels(benchmarks, rotation=0)
56	ax1.set_ylabel('Ambiguity $\\alpha$')
57	ax1.set_ylim(0, 0.38)
58	ax1.set_title('(a) Per-example ambiguity', fontsize=13, pad=8)
59	
60	# Category legend
61	from matplotlib.patches import Patch
62	legend_elements = [
63	    Patch(facecolor=cat_colo
…[truncated 1258 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T13:55:27.508776+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "entrainment_gated_ft",
  "limit": "0",
  "fields": "['exp_id', 'title', 'status', 'conclusion', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "entrainment_gated_ft",
    "limit": "0",
    "fields": "['exp_id', 'title', 'status', 'conclusion', 'metrics']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T13:55:27.509542+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp-005\": {\"status\": \"PREPARING\", \"metrics\": {\"6arch_jaccard\": {\"arc_easy\": {\"mean_J_helped\": 0.1109, \"mean_J_hurt\": 0.1032, \"sig_helped\": \"15/15\", \"sig_hurt\": \"15/15\", \"n_samples\": 2376}, \"lambada_openai\": {\"mean_J_helped\": 0.1295, \"mean_J_hurt\": 0.0906, \"sig_helped\": \"15/15\", \"sig_hurt\": \"15/15\", \"n_samples\": 5153}, \"subgroup_trend_lambada_J_helped\": {\"3arch\": 0.1194, \"4arch\": 0.1219, \"5arch\": 0.1221, \"6arch\": 0.1295}, \"subgroup_trend_lambada_J_hurt\": {\"3arch\": 0.0955, \"4arch\": 0.0965, \"5arch\": 0.0946, \"6arch\": 0.0906}, \"hgrn_eval\": {\"h31_lambada_acc\": 0.3586, \"h31_arceasy_acc\": 0.6065, \"pure_lambada_acc\": 0.2602, \"pure_arceasy_acc\": 0.6157}}, \"extended_jaccard_4benchmarks\": {\"lambada_openai\": {\"mean_J_helped\": 0.1221, \"mean_J_hurt\": 0.0946, \"z_range_helped\": [9.03, 12.21], \"z_range_hurt\": [6.33, 10.89], \"sig_pairs\": \"10/10\", \"n_samples\": 5153}, \"arc_easy\": {\"mean_J_helped\": 0.1081, \"mean_J_hurt\": 0.1047, \"z_range_helped\": [3.49, 9.19], \"z_range_hurt\": [3.72, 7.48], \"sig_pairs\": \"10/10\", \"n_samples\": 2376}, \"hellaswag\": {\"mean_J_helped\": 0.0931, \"mean_J_hurt\": 0.0815, \"z_range_helped\": [10.31, 19.2], \"z_range_hurt\": [10.2, 16.33], \"sig_pairs\": \"10/10\", \"n_samples\": 10042}, \"piqa\": {\"mean_J_helped\": 0.0928, \"mean_J_hurt\": 0.0863, \"z_range_helped\": [3.08, 9.46], \"z_range_hurt\": [3.17, 7.16], \"sig_pairs\": \"10/10\", \"n_samples\": 1838}, \"grand_mean_J_helped\": 0.104, \"grand_mean_J_hurt\": 0.0918, \"total_significant\": \"40/40\"}}, \"conclusion\": \"success\"}, \"exp-005-pure-baselines\": {\"status\": \"PREPARING\", \"conclusion\": \"failed\"}, \"exp-005-pure-v10\": {\"status\": \"PREPARING\"}, \"exp-005-pure-v9\": {\"status\": \"PREPARING\"}, \"exp-005-pure-v8\": {\"status\": \"PREPARING\"}, \"exp-005-pure-v7\": {\"status\": \"PREPARING\"}, \"exp-005-pure-v6\": {\"status\
…[truncated 16972 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T13:55:27.509957+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/e1_confidence_selection.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/e1_confidence_selection.json"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T13:55:27.510361+00:00_

1	{
2	  "analysis": "e1_confidence_selection",
3	  "date": "2026-05-22",
4	  "method": {
5	    "attention_ratio": "h3-1 (25%)",
6	    "architectures": ["GDN", "RetNet", "HGRN2"],
7	    "cv": "50/50 random split x 10 repeats",
8	    "confidence_measure": {
9	      "lambada": "target word loglikelihood",
10	      "hellaswag": "max char-length-normalized loglikelihood",
11	      "piqa": "max raw loglikelihood across choices",
12	      "arc_easy": "max raw loglikelihood across choices"
13	    }
14	  },
15	  "results": {
16	    "lambada": {
17	      "strategies": {
18	        "max_confidence": {
19	          "mean_acc": 0.525378,
20	          "std_acc": 0.006802,
21	          "vs_mv_pp": 1.634,
22	          "vs_best_single_pp": 1.649
23	        },
24	        "rescue_threshold": {
25	          "mean_acc": 0.562321,
26	          "std_acc": 0.005296,
27	          "vs_mv_pp": 5.328,
28	          "vs_best_single_pp": 5.343,
29	          "mean_threshold": 1.7244,
30	          "std_threshold": 0.1688
31	        },
32	        "confidence_weighted": {
33	          "mean_acc": 0.527163,
34	          "std_acc": 0.006393,
35	          "vs_mv_pp": 1.812,
36	          "vs_best_single_pp": 1.828
37	        }
38	      },
39	      "baselines": {
40	        "majority_vote_acc": 0.509042,
41	        "majority_vote_std": 0.005642,
42	        "best_single_acc": 0.508886,
43	        "best_single_std": 0.005018,
44	        "oracle_acc": 0.654637,
45	        "oracle_std": 0.005371,
46	        "random_acc": 0.50683,
47	        "random_std": 0.008304
48	      },
49	      "per_arch": {
50	        "GDN": {"pure_acc": 0.543373, "hybrid_acc": 0.513293},
51	        "RetNet": {"pure_acc": 0.517369, "hybrid_acc": 0.502426},
52	        "HGRN2": {"pure_acc": 0.48399, "hybrid_acc": 0.514264}
53	      },
54	      "n_samples": 5153
55	    },
56	    "hellaswag": {
57	      "strategies": {
58	        "max_confidence": {
59	          "mean_acc": 0.596415,
60	          "std_acc": 0.004721,
61	          "vs_mv_pp
…[truncated 3861 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T13:55:27.510683+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/majority_vote_and_rho_analysis.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/majority_vote_and_rho_analysis.json"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T13:55:27.510977+00:00_

1	{
2	  "task_1_majority_vote": {
3	    "LAMBADA": {
4	      "N": 5153,
5	      "majority_vote_acc": 0.5121,
6	      "mean_individual_acc": 0.51,
7	      "mv_vs_mean_pp": 0.21,
8	      "agreement_pct": 70.41,
9	      "disagreement_pct": 29.59,
10	      "unanimous_correct": 1860,
11	      "two_of_three": 779,
12	      "one_of_three": 746,
13	      "unanimous_wrong": 1768,
14	      "individual_accs": {
15	        "GDN": 0.5133,
16	        "RetNet": 0.5024,
17	        "HGRN2": 0.5143
18	      },
19	      "best_single": "HGRN2",
20	      "best_single_acc": 0.5143,
21	      "mv_vs_best_pp": -0.21
22	    },
23	    "HellaSwag (acc_norm)": {
24	      "N": 10042,
25	      "majority_vote_acc": 0.5965,
26	      "mean_individual_acc": 0.5949,
27	      "mv_vs_mean_pp": 0.16,
28	      "agreement_pct": 84.95,
29	      "disagreement_pct": 15.05,
30	      "unanimous_correct": 5211,
31	      "two_of_three": 779,
32	      "one_of_three": 732,
33	      "unanimous_wrong": 3320
34	    },
35	    "ARC-Easy": {
36	      "N": 2376,
37	      "majority_vote_acc": 0.7096,
38	      "mean_individual_acc": 0.7083,
39	      "mv_vs_mean_pp": 0.13,
40	      "agreement_pct": 79.0,
41	      "disagreement_pct": 21.0,
42	      "unanimous_correct": 1432,
43	      "two_of_three": 254,
44	      "one_of_three": 245,
45	      "unanimous_wrong": 445,
46	      "individual_accs": {
47	        "GDN": 0.7083,
48	        "RetNet": 0.6961,
49	        "HGRN2": 0.7205
50	      },
51	      "best_single": "HGRN2",
52	      "best_single_acc": 0.7205,
53	      "mv_vs_best_pp": -1.09
54	    },
55	    "BoolQ": {
56	      "N": 3270,
57	      "majority_vote_acc": 0.633,
58	      "mean_individual_acc": 0.6131,
59	      "mv_vs_mean_pp": 1.99,
60	      "agreement_pct": 54.65,
61	      "disagreement_pct": 45.35,
62	      "unanimous_correct": 1231,
63	      "two_of_three": 839,
64	      "one_of_three": 644,
65	      "unanimous_wrong": 556
66	    }
67	  },
68	  "task_2_rho_sigma_j": {
69	    "sigma_values": [
70	      0.016238,
71	
…[truncated 1010 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T13:55:27.511234+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/a3_complementarity_decomposition.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/a3_complementarity_decomposition.json"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T13:55:27.511861+00:00_

1	{
2	  "description": "A3: Complementarity Decomposition Analysis",
3	  "methodology": {
4	    "categories": {
5	      "unanimous_correct": "3_of_3: all 3 architectures correct \u2192 redundant correct",
6	      "unanimous_wrong": "0_of_3: all 3 architectures wrong \u2192 redundant wrong (hard examples)",
7	      "minority_correct": "1_of_3: exactly 1 correct, 2 wrong \u2192 complementary but MV-hostile (MV votes wrong)",
8	      "majority_correct": "2_of_3: exactly 2 correct, 1 wrong \u2192 complementary and MV-exploitable"
9	    },
10	    "derived_metrics": {
11	      "oracle_exploitable": "1_of_3 + 2_of_3 (any disagreement where at least one is correct)",
12	      "mv_exploitable": "2_of_3 only (MV needs majority to be correct)",
13	      "mv_hostile": "1_of_3 (MV votes with wrong majority \u2014 actively harmful)",
14	      "redundant_total": "0_of_3 + 3_of_3 (all agree, no ensemble value)",
15	      "complementary_total": "1_of_3 + 2_of_3 (disagreement with at least one correct)",
16	      "mv_exploitation_ratio": "2_of_3 / (1_of_3 + 2_of_3) \u2014 fraction of complementary cases MV can exploit",
17	      "minority_dominance": "1_of_3 / (1_of_3 + 2_of_3) \u2014 fraction of complementary cases where MV fails"
18	    }
19	  },
20	  "benchmarks": {
21	    "lambada": {
22	      "n_samples": 5153,
23	      "attention_ratios": {
24	        "pure": {
25	          "counts": {
26	            "unanimous_wrong_0of3": 1719,
27	            "minority_correct_1of3": 762,
28	            "majority_correct_2of3": 818,
29	            "unanimous_correct_3of3": 1854
30	          },
31	          "fractions": {
32	            "unanimous_wrong_0of3": 0.333592,
33	            "minority_correct_1of3": 0.147875,
34	            "majority_correct_2of3": 0.158742,
35	            "unanimous_correct_3of3": 0.35979
36	          },
37	          "category_fractions": {
38	            "redundant": 0.693382,
39	            "complementary": 0.306618,
40	            "complementary_mv_exploitable": 
…[truncated 30551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T13:55:27.512180+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/e1_confidence_selection_e4231e.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/e1_confidence_selection_e4231e.json"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T13:55:27.512478+00:00_

1	{
2	  "analysis": "e1_confidence_selection",
3	  "date": "2026-05-22",
4	  "method": {
5	    "attention_ratio": "h3-1 (25%)",
6	    "architectures": ["GDN", "RetNet", "HGRN2"],
7	    "cv": "50/50 random split x 10 repeats",
8	    "confidence_measure": {
9	      "lambada": "target word loglikelihood",
10	      "hellaswag": "max char-length-normalized loglikelihood",
11	      "piqa": "max raw loglikelihood across choices",
12	      "arc_easy": "max raw loglikelihood across choices"
13	    }
14	  },
15	  "results": {
16	    "lambada": {
17	      "strategies": {
18	        "max_confidence": {
19	          "mean_acc": 0.525378,
20	          "std_acc": 0.006802,
21	          "vs_mv_pp": 1.634,
22	          "vs_best_single_pp": 1.649
23	        },
24	        "rescue_threshold": {
25	          "mean_acc": 0.562321,
26	          "std_acc": 0.005296,
27	          "vs_mv_pp": 5.328,
28	          "vs_best_single_pp": 5.343,
29	          "mean_threshold": 1.7244,
30	          "std_threshold": 0.1688
31	        },
32	        "confidence_weighted": {
33	          "mean_acc": 0.527163,
34	          "std_acc": 0.006393,
35	          "vs_mv_pp": 1.812,
36	          "vs_best_single_pp": 1.828
37	        }
38	      },
39	      "baselines": {
40	        "majority_vote_acc": 0.509042,
41	        "majority_vote_std": 0.005642,
42	        "best_single_acc": 0.508886,
43	        "best_single_std": 0.005018,
44	        "oracle_acc": 0.654637,
45	        "oracle_std": 0.005371,
46	        "random_acc": 0.50683,
47	        "random_std": 0.008304
48	      },
49	      "per_arch": {
50	        "GDN": {"pure_acc": 0.543373, "hybrid_acc": 0.513293},
51	        "RetNet": {"pure_acc": 0.517369, "hybrid_acc": 0.502426},
52	        "HGRN2": {"pure_acc": 0.48399, "hybrid_acc": 0.514264}
53	      },
54	      "n_samples": 5153
55	    },
56	    "hellaswag": {
57	      "strategies": {
58	        "max_confidence": {
59	          "mean_acc": 0.596415,
60	          "std_acc": 0.004721,
61	          "vs_mv_pp
…[truncated 3861 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T13:55:27.512740+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_analysis_r16-w1-routing-variance_20260523T135203.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_analysis_r16-w1-routing-variance_20260523T135203.log"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T13:55:27.512935+00:00_

File content (93518 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T13:55:27.513113+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "per.split|per_split|split_acc|fold_acc|repeat_acc|cv_results|cross_val",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Grep",
  "tool_args": {
    "pattern": "per.split|per_split|split_acc|fold_acc|repeat_acc|cv_results|cross_val",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T13:55:27.513350+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T13:55:27.513583+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"per.split\\|per_fold\\|split_results\\|routing_gain\\|paired.*t.test\\|SD\\|variance\\|split.*acc\" /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_analysis_r16-w1-routing-variance_20260523T135203.log 2>/dev/null | head -50",
  "description": "Search worker log for routing variance analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"per.split\\|per_fold\\|split_results\\|routing_gain\\|paired.*t.test\\|SD\\|variance\\|split.*acc\" /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_analysis_r16-w1-routing-variance_20260523T135203.log 2>/dev/null | head -50",
    "description": "Search worker log for routing variance analysis"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T13:55:27.514005+00:00_

&lt;persisted-output>
Output too large (114.7KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft/852b4152-b0ef-4a48-9fc4-f75679441dd1/tool-results/bsac7exk1.txt

Preview (first 2KB):
4:{"type":"assistant","message":{"model":"claude-opus-4-6","id":"msg_01TUdr4fSFCz8WeP4qgrBjbL","type":"message","role":"assistant","content":[{"type":"thinking","thinking":"Let me search for the routing/rescue related data files in the project directory and check the registry.","signature":"Eq0CCmMIDhgCKkChvjpOS1ZVefR3Zy0kdombc0dj0Gfs/NgloLLxVH6z0SoDQHT7gI/V9ud3FNPpWgvEUnnh0On6Wy5Ypl9kbxE/Mg9jbGF1ZGUtb3B1cy00LTY4AEIIdGhpbmtpbmcSDIHMBvdi8aSJ+CLgOhoMVrbW3CLG+L43S3GTIjAYJIEzWSoYqGTk3t27ae9TPYNCu2YZqJ6AH7XEV4X8a6NoXAK6BO7UjA3qKUUBwDMqeAOMcWo3kjR8jcYmZLdfcTp0BkMImGLlMnAS1w9MqdbkwR14YDS4rNi7sNjPfNVdscSs18t1QWCTF/1NCKHYRuXWIMqOmOXTXg5WxPEtV0d5sn1mfxNQxkjBnBHvaihMMcdKJJzVVLYvmJHC3ztuuRnqKVHd7l+N0RgB"}],"stop_reason":null,"stop_sequence":null,"stop_details":null,"usage":{"input_tokens":3,"cache_creation_input_tokens":12283,"cache_read_input_tokens":11841,"cache_creation":{"ephemeral_5m_input_tokens":0,"ephemeral_1h_input_tokens":12283},"output_tokens":9,"service_tier":"standard","inference_geo":"not_available"},"diagnostics":null,"context_management":null},"parent_tool_use_id":null,"session_id":"852b4152-b0ef-4a48-9fc4-f75679441dd1","uuid":"50d98cd9-bd81-42e1-a636-3d844dbcc265"}
...
&lt;/persisted-output>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T13:55:27.514232+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "confidence_selection|rescue_threshold|routing",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/",
  "glob": "*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Grep",
  "tool_args": {
    "pattern": "confidence_selection|rescue_threshold|routing",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/",
    "glob": "*.py"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T13:55:27.514419+00:00_

Found 1 file
figures/paper/gen_fig3_alpha_routing.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T13:55:27.514664+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft/852b4152-b0ef-4a48-9fc4-f75679441dd1/tool-results/bsac7exk1.txt",
  "limit": "50",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft/852b4152-b0ef-4a48-9fc4-f75679441dd1/tool-results/bsac7exk1.txt",
    "limit": "50",
    "offset": "0"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T13:55:27.514859+00:00_

File content (49184 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T13:55:27.515036+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -o '\"text\":\"[^\"]*\"' /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_analysis_r16-w1-routing-variance_20260523T135203.log | grep -iE \"per.split|variance|SD|paired|t.test|CI|p.value|gain_sd|routing.*var\" | head -30",
  "description": "Extract relevant text from worker log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -o '\"text\":\"[^\"]*\"' /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/logs/workers/worker_analysis_r16-w1-routing-variance_20260523T135203.log | grep -iE \"per.split|variance|SD|paired|t.test|CI|p.value|gain_sd|routing.*var\" | head -30",
    "description": "Extract relevant text from worker log"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T13:55:27.515215+00:00_

"text":"Found the aggregated data in `e1_confidence_selection.json`. It has mean and std for the rescue_threshold (routing) and majority_vote strategies across 10 CV splits, but not per-split values needed for paired t-test. Let me check if per-split data exists elsewhere."
"text":"Let me search the worker log for the actual computed variance statistics."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T13:55:27.515454+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "confidence_selection|rescue_threshold|routing_gain",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/",
  "glob": "*.py",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Grep",
  "tool_args": {
    "pattern": "confidence_selection|rescue_threshold|routing_gain",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/",
    "glob": "*.py",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T13:55:27.515666+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T13:55:27.515892+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/bootstrap_ci_alpha.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/bootstrap_ci_alpha.json"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T13:55:27.516170+00:00_

1	{
2	  "analysis": "bootstrap_ci_alpha",
3	  "n_bootstrap": 10000,
4	  "seed": 42,
5	  "results": {
6	    "PIQA": {
7	      "pure": {
8	        "alpha_hat": 0.14309031556039173,
9	        "ci_lower": 0.12731229597388466,
10	        "ci_upper": 0.15941240478781285,
11	        "ci_width": 0.03210010881392819,
12	        "se": 0.008172885407242578,
13	        "n_samples": 1838
14	      },
15	      "h24-1": {
16	        "alpha_hat": 0.13764961915125137,
17	        "ci_lower": 0.12187159956474429,
18	        "ci_upper": 0.15397170837867247,
19	        "ci_width": 0.03210010881392818,
20	        "se": 0.008049918755941087,
21	        "n_samples": 1838
22	      },
23	      "h12-1": {
24	        "alpha_hat": 0.132208922742111,
25	        "ci_lower": 0.11697497279651796,
26	        "ci_upper": 0.14744287268770404,
27	        "ci_width": 0.030467899891186076,
28	        "se": 0.007920239711124856,
29	        "n_samples": 1838
30	      },
31	      "h6-1": {
32	        "alpha_hat": 0.14309031556039173,
33	        "ci_lower": 0.12731229597388466,
34	        "ci_upper": 0.1588683351468988,
35	        "ci_width": 0.03155603917301414,
36	        "se": 0.008112638902848992,
37	        "n_samples": 1838
38	      },
39	      "h3-1": {
40	        "alpha_hat": 0.1398258977149075,
41	        "ci_lower": 0.12404787812840043,
42	        "ci_upper": 0.15505984766050054,
43	        "ci_width": 0.031011969532100114,
44	        "se": 0.008016795777695875,
45	        "n_samples": 1838
46	      }
47	    },
48	    "HellaSwag": {
49	      "pure": {
50	        "alpha_hat": 0.14817765385381398,
51	        "ci_lower": 0.1411073491336387,
52	        "ci_upper": 0.15504879506074487,
53	        "ci_width": 0.013941445927106166,
54	        "se": 0.0035155620322709705,
55	        "n_samples": 10042
56	      },
57	      "h24-1": {
58	        "alpha_hat": 0.1504680342561243,
59	        "ci_lower": 0.14369647480581557,
60	        "ci_upper": 0.15733917546305518,
61	        "ci_width": 0.013642700657239604,

…[truncated 3831 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T13:55:27.516416+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/bca_ci_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/artifacts/_project/data/bca_ci_data.json"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T13:55:27.516630+00:00_

1	{
2	  "benchmark": "LAMBADA",
3	  "rho": -1.0,
4	  "method_used": "percentile",
5	  "ci_lower": -1.0,
6	  "ci_upper": -0.7,
7	  "confidence_level": 0.95,
8	  "crosses_zero": false,
9	  "n_bootstrap": 10000,
10	  "n_valid": 8875,
11	  "degenerate_count": 1125,
12	  "degenerate_pct": 11.25,
13	  "seed": 42,
14	  "p_rho_negative": 1.0,
15	  "p_rho_positive": 0.0,
16	  "bca_note": "BCa degenerate at rho=-1.0 boundary (11.25% of bootstrap samples had zero variance); percentile CI used instead. The CI [-1.0, -0.7] excludes zero, supporting a negative correlation.",
17	  "percentile_vs_bca": "BCa correction requires finite acceleration estimate, which degenerates when the point estimate is at the parameter boundary (rho=-1.0). Percentile CI is valid but slightly less accurate for skewed distributions. With 88.75% valid samples, the percentile interval is reliable."
18	}
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-23T13:55:27.516984+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport math\nfrom scipy import stats\n\n# Data from e1_confidence_selection.json\n# rescue_threshold = routing strategy reported in paper\nbenchmarks = {\n    'LAMBADA': {\n        'routing_mean': 0.562321, 'routing_std': 0.005296,\n        'mv_mean': 0.509042, 'mv_std': 0.005642,\n        'gain_pp': 5.328, 'n_samples': 5153\n    },\n    'ARC-Easy': {\n        'routing_mean': 0.716414, 'routing_std': 0.007323,\n        'mv_mean': 0.706229, 'mv_std': 0.005494,\n        'gain_pp': 1.019, 'n_samples': 2376\n    },\n    'HellaSwag': {\n        'routing_mean': 0.595041, 'routing_std': 0.004511,\n        'mv_mean': 0.595240, 'mv_std': 0.005038,\n        'gain_pp': -0.020, 'n_samples': 10042\n    },\n    'PIQA': {\n        'routing_mean': 0.734059, 'routing_std': 0.010268,\n        'mv_mean': 0.740152, 'mv_std': 0.010581,\n        'gain_pp': -0.609, 'n_samples': 1838\n    }\n}\n\nn_splits = 10\ndf = n_splits - 1  # 9\n\nprint(\"=\" * 80)\nprint(\"Routing Variance Report (rescue_threshold vs majority_vote)\")\nprint(\"Method: 50/50 random split × 10 repeats, 3 architectures (GDN, RetNet, HGRN2)\")\nprint(\"=\" * 80)\n\n# Since we don't have per-split paired data, compute for a range of correlations\n# r=0 gives the most conservative (widest CI, least significant p)\n# In practice, r should be high (>0.9) since both strategies share the same test split\n\nfor r_assumed in [0.0, 0.9, 0.95]:\n    print(f\"\\n--- Assuming split-level correlation r = {r_assumed} ---\\n\")\n    for name, d in benchmarks.items():\n        sd_r = d['routing_std'] * 100  # convert to pp\n        sd_mv = d['mv_std'] * 100\n        gain = d['gain_pp']\n        \n        # SD of paired difference\n        sd_diff_sq = sd_r**2 + sd_mv**2 - 2 * r_assumed * sd_r * sd_mv\n        if sd_diff_sq < 0:\n            sd_diff_sq = 0.0001  # numerical floor\n        sd_diff = math.sqrt(sd_diff_sq)\n        \n        se_diff = sd_diff / math.sqrt(n_splits)\n        \n        if se_diff > 0.0001:\n            t_stat = gain / se_diff\n            p_val = 2 * (1 - stats.t.cdf(abs(t_stat), df))\n        else:\n            t_stat = float('inf')\n            p_val = 0.0\n        \n        # 95% CI (t-based)\n        t_crit = stats.t.ppf(0.975, df)\n        ci_lo = gain - t_crit * se_diff\n        ci_hi = gain + t_crit * se_diff\n        \n        if p_val < 0.0001:\n            p_str = \"<0.0001\"\n        else:\n            p_str = f\"{p_val:.4f}\"\n        \n        print(f\"{name:12s}: mean={gain:+.2f}pp, SD={sd_diff:.3f}pp, \"\n              f\"95% CI=[{ci_lo:+.2f}, {ci_hi:+.2f}], t({df})={t_stat:.2f}, p={p_str}\")\n\nprint(\"\\n\" + \"=\" * 80)\nprint(\"CONSERVATIVE REPORT (r=0, most conservative / unpaired assumption)\")\nprint(\"=\" * 80 + \"\\n\")\n\nr_assumed = 0.0\nfor name, d in benchmarks.items():\n    sd_r = d['routing_std'] * 100\n    sd_mv = d['mv_std'] * 100\n    gain = d['gain_pp']\n    \n    sd_diff = math.sqrt(sd_r**2 + sd_mv**2 - 2 * r_assumed * sd_r * sd_mv)\n    se_diff = sd_diff / math.sqrt(n_splits)\n    \n    if se_diff > 0.0001:\n        t_stat = gain / se_diff\n        p_val = 2 * (1 - stats.t.cdf(abs(t_stat), df))\n    else:\n        t_stat = float('inf')\n        p_val = 0.0\n    \n    t_crit = stats.t.ppf(0.975, df)\n    ci_lo = gain - t_crit * se_diff\n    ci_hi = gain + t_crit * se_diff\n    \n    if p_val < 0.0001:\n        p_str = \"<0.0001\"\n    else:\n        p_str = f\"{p_val:.4f}\"\n    \n    print(f\"{name:12s}: mean={gain:+.2f}pp, SD={sd_diff:.3f}pp, 95% CI=[{ci_lo:+.2f}, {ci_hi:+.2f}], p={p_str}\")\n\nPYEOF",
  "description": "Compute routing variance statistics from aggregated data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport math\nfrom scipy import stats\n\n# Data from e1_confidence_selection.json\n# rescue_threshold = routing strategy reported in paper\nbenchmarks = {\n    'LAMBADA': {\n        'routing_mean': 0.562321, 'routing_std': 0.005296,\n        'mv_mean': 0.509042, 'mv_std': 0.005642,\n        'gain_pp': 5.328, 'n_samples': 5153\n    },\n    'ARC-Easy': {\n        'routing_mean': 0.716414, 'routing_std': 0.007323,\n        'mv_mean': 0.706229, 'mv_std': 0.005494,\n        'gain_pp': 1.019, 'n_samples': 2376\n    },\n    'HellaSwag': {\n        'routing_mean': 0.595041, 'routing_std': 0.004511,\n        'mv_mean': 0.595240, 'mv_std': 0.005038,\n        'gain_pp': -0.020, 'n_samples': 10042\n    },\n    'PIQA': {\n        'routing_mean': 0.734059, 'routing_std': 0.010268,\n        'mv_mean': 0.740152, 'mv_std': 0.010581,\n        'gain_pp': -0.609, 'n_samples': 1838\n    }\n}\n\nn_splits = 10\ndf = n_splits - 1  # 9\n\nprint(\"=\" * 80)\nprint(\"Routing Variance Report (rescue_threshold vs majority_vote)\")\nprint(\"Method: 50/50 random split × 10 repeats, 3 architectures (GDN, RetNet, HGRN2)\")\nprint(\"=\" * 80)\n\n# Since we don't have per-split paired data, compute for a range of correlations\n# r=0 gives the most conservative (widest CI, least significant p)\n# In practice, r should be high (>0.9) since both strategies share the same test split\n\nfor r_assumed in [0.0, 0.9, 0.95]:\n    print(f\"\\n--- Assuming split-level correlation r = {r_assumed} ---\\n\")\n    for name, d in benchmarks.items():\n        sd_r = d['routing_std'] * 100  # convert to pp\n        sd_mv = d['mv_std'] * 100\n        gain = d['gain_pp']\n        \n        # SD of paired difference\n        sd_diff_sq = sd_r**2 + sd_mv**2 - 2 * r_assumed * sd_r * sd_mv\n        if sd_diff_sq < 0:\n            sd_diff_sq = 0.0001  # numerical floor\n        sd_diff = math.sqrt(sd_diff_sq)\n        \n        se_diff = sd_diff / math.sqrt(n_splits)\n        \n        if se_diff > 0.0001:\n            t_stat = gain / se_diff\n            p_val = 2 * (1 - stats.t.cdf(abs(t_stat), df))\n        else:\n            t_stat = float('inf')\n            p_val = 0.0\n        \n        # 95% CI (t-based)\n        t_crit = stats.t.ppf(0.975, df)\n        ci_lo = gain - t_crit * se_diff\n        ci_hi = gain + t_crit * se_diff\n        \n        if p_val < 0.0001:\n            p_str = \"<0.0001\"\n        else:\n            p_str = f\"{p_val:.4f}\"\n        \n        print(f\"{name:12s}: mean={gain:+.2f}pp, SD={sd_diff:.3f}pp, \"\n              f\"95% CI=[{ci_lo:+.2f}, {ci_hi:+.2f}], t({df})={t_stat:.2f}, p={p_str}\")\n\nprint(\"\\n\" + \"=\" * 80)\nprint(\"CONSERVATIVE REPORT (r=0, most conservative / unpaired assumption)\")\nprint(\"=\" * 80 + \"\\n\")\n\nr_assumed = 0.0\nfor name, d in benchmarks.items():\n    sd_r = d['routing_std'] * 100\n    sd_mv = d['mv_std'] * 100\n    gain = d['gain_pp']\n    \n    sd_diff = math.sqrt(sd_r**2 + sd_mv**2 - 2 * r_assumed * sd_r * sd_mv)\n    se_diff = sd_diff / math.sqrt(n_splits)\n    \n    if se_diff > 0.0001:\n        t_stat = gain / se_diff\n        p_val = 2 * (1 - stats.t.cdf(abs(t_stat), df))\n    else:\n        t_stat = float('inf')\n        p_val = 0.0\n    \n    t_crit = stats.t.ppf(0.975, df)\n    ci_lo = gain - t_crit * se_diff\n    ci_hi = gain + t_crit * se_diff\n    \n    if p_val < 0.0001:\n        p_str = \"<0.0001\"\n    else:\n        p_str = f\"{p_val:.4f}\"\n    \n    print(f\"{name:12s}: mean={gain:+.2f}pp, SD={sd_diff:.3f}pp, 95% CI=[{ci_lo:+.2f}, {ci_hi:+.2f}], p={p_str}\")\n\nPYEOF",
    "description": "Compute routing variance statistics from aggregated data"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T13:55:27.517265+00:00_

================================================================================
Routing Variance Report (rescue_threshold vs majority_vote)
Method: 50/50 random split × 10 repeats, 3 architectures (GDN, RetNet, HGRN2)
================================================================================

--- Assuming split-level correlation r = 0.0 ---

LAMBADA     : mean=+5.33pp, SD=0.774pp, 95% CI=[+4.77, +5.88], t(9)=21.77, p=<0.0001
ARC-Easy    : mean=+1.02pp, SD=0.915pp, 95% CI=[+0.36, +1.67], t(9)=3.52, p=0.0065
HellaSwag   : mean=-0.02pp, SD=0.676pp, 95% CI=[-0.50, +0.46], t(9)=-0.09, p=0.9275
PIQA        : mean=-0.61pp, SD=1.474pp, 95% CI=[-1.66, +0.45], t(9)=-1.31, p=0.2239

--- Assuming split-level correlation r = 0.9 ---

LAMBADA     : mean=+5.33pp, SD=0.247pp, 95% CI=[+5.15, +5.50], t(9)=68.24, p=<0.0001
ARC-Easy    : mean=+1.02pp, SD=0.338pp, 95% CI=[+0.78, +1.26], t(9)=9.55, p=<0.0001
HellaSwag   : mean=-0.02pp, SD=0.220pp, 95% CI=[-0.18, +0.14], t(9)=-0.29, p=0.7799
PIQA        : mean=-0.61pp, SD=0.467pp, 95% CI=[-0.94, -0.27], t(9)=-4.12, p=0.0026

--- Assuming split-level correlation r = 0.95 ---

LAMBADA     : mean=+5.33pp, SD=0.176pp, 95% CI=[+5.20, +5.45], t(9)=95.57, p=<0.0001
ARC-Easy    : mean=+1.02pp, SD=0.271pp, 95% CI=[+0.82, +1.21], t(9)=11.87, p=<0.0001
HellaSwag   : mean=-0.02pp, SD=0.160pp, 95% CI=[-0.13, +0.09], t(9)=-0.40, p=0.7013
PIQA        : mean=-0.61pp, SD=0.331pp, 95% CI=[-0.85, -0.37], t(9)=-5.82, p=0.0003

================================================================================
CONSERVATIVE REPORT (r=0, most conservative / unpaired assumption)
================================================================================

LAMBADA     : mean=+5.33pp, SD=0.774pp, 95% CI=[+4.77, +5.88], p=<0.0001
ARC-Easy    : mean=+1.02pp, SD=0.915pp, 95% CI=[+0.36, +1.67], p=0.0065
HellaSwag   : mean=-0.02pp, SD=0.676pp, 95% CI=[-0.50, +0.46], p=0.9275
PIQA        : mean=-0.61pp, SD=1.474pp, 95% CI=[-1.66, +0.45], p=0.2239

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-23T13:55:27.517551+00:00_

## Routing Variance Report

**数据来源**: `artifacts/_project/data/e1_confidence_selection.json`
**方法**: rescue_threshold routing vs majority vote, 50/50 split × 10 repeats, 3 architectures (GDN, RetNet, HGRN2), h3-1

### 限制

本地仅有聚合统计量（各策略跨 10 splits 的 mean/std），**无 per-split paired data**。因此 SD_gain 和 paired t-test 需要假设 splits 间 routing 与 MV accuracy 的相关系数 r。下面报告 conservative bound (r=0, 等效 unpaired Welch test)：

### Conservative Report (r=0, worst case)

```
LAMBADA:   mean=+5.3pp, SD=0.77pp, 95% CI=[+4.8, +5.9], p<0.0001
ARC-Easy:  mean=+1.0pp, SD=0.92pp, 95% CI=[+0.4, +1.7], p=0.0065
HellaSwag: mean=-0.0pp, SD=0.68pp, 95% CI=[-0.5, +0.5], p=0.9275
PIQA:      mean=-0.6pp, SD=1.47pp, 95% CI=[-1.7, +0.4], p=0.2239
```

### 关键结论

- **LAMBADA**: 即使用最保守的 unpaired 假设，p < 0.0001，gain 高度显著
- **ARC-Easy**: p = 0.0065，显著（实际 paired test 的 p 会更小）
- **HellaSwag**: gain ≈ 0，无显著差异
- **PIQA**: 实际 gain = -0.6pp（论文报告为 0），无显著差异（p=0.22）

### 精确计算需要的数据

per-split paired data（10 组 routing acc 和 MV acc 配对值）不在本地。可能在 westb-48145 服务器上的以下路径：
- `/root/entrainment_gated_ft/analysis/` 或 `/root/entrainment_gated_ft/results/`
- 生成 `e1_confidence_selection.json` 的分析脚本的中间输出

如果需要精确 paired t-test，需 SSH 到服务器提取 per-split 数据，或重新运行分析脚本保存 per-split 结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_r16-w1-routing-variance_20260523T135203"
}
```

</details>

---
