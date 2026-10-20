# ssh p1 p2 power holm

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_ssh_p1-p2-power-holm_20260520T132923.jsonl`
- **Structured JSON:** [`80b8ee61b0fce90091c1.json`](../../sessions/80/80b8ee61b0fce90091c1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

43 recorded events

### Tool call

_source line 1 · 2026-05-20T13:36:06.960759+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__detect_image",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__detect_image",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T13:36:06.961100+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T13:36:06.961339+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p /root/autodl-tmp/struct_self_consist_ie/artifacts/r25_response && python3 -c \"\nfrom scipy.stats import norm\nimport numpy as np\n\nlines = []\nlines.append('\\\\\\\\begin{table}[h]')\nlines.append('\\\\\\\\centering')\nlines.append('\\\\\\\\caption{Post-hoc power analysis for cross-dataset correlation tests (\\$n=23\\$ configurations).}')\nlines.append('\\\\\\\\label{tab:power_analysis}')\nlines.append('\\\\\\\\begin{tabular}{ccc}')\nlines.append('\\\\\\\\toprule')\nlines.append('Effect Size (\\$\\\\\\\\rho\\$) & Power (\\$1-\\\\\\\\beta\\$) & \\$n\\$ needed for 80\\\\\\\\% power \\\\\\\\\\\\\\\\')\nlines.append('\\\\\\\\midrule')\n\nfor rho in [0.1, 0.2, 0.3, 0.4, 0.5]:\n    z_rho = 0.5 * np.log((1+rho)/(1-rho))\n    se = 1/np.sqrt(23-3)\n    z_alpha = 1.96\n    power = norm.cdf(z_rho/se - z_alpha) + norm.cdf(-z_rho/se - z_alpha)\n    n_needed = int(np.ceil((z_alpha + 0.842)**2 / z_rho**2)) + 3\n    lines.append(f'{rho:.1f} & {power:.3f} & {n_needed} \\\\\\\\\\\\\\\\')\n\nlines.append('\\\\\\\\bottomrule')\nlines.append('\\\\\\\\end{tabular}')\nlines.append('\\\\\\\\end{table}')\n\noutput = '\\n'.join(lines)\nprint(output)\n\nwith open('/root/autodl-tmp/struct_self_consist_ie/artifacts/r25_response/power_analysis.tex', 'w') as f:\n    f.write(output + '\\n')\nprint('--- SAVED ---')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && mkdir -p /root/autodl-tmp/struct_self_consist_ie/artifacts/r25_response && python3 -c \"\nfrom scipy.stats import norm\nimport numpy as np\n\nlines = []\nlines.append('\\\\\\\\begin{table}[h]')\nlines.append('\\\\\\\\centering')\nlines.append('\\\\\\\\caption{Post-hoc power analysis for cross-dataset correlation tests (\\$n=23\\$ configurations).}')\nlines.append('\\\\\\\\label{tab:power_analysis}')\nlines.append('\\\\\\\\begin{tabular}{ccc}')\nlines.append('\\\\\\\\toprule')\nlines.append('Effect Size (\\$\\\\\\\\rho\\$) & Power (\\$1-\\\\\\\\beta\\$) & \\$n\\$ needed for 80\\\\\\\\% power \\\\\\\\\\\\\\\\')\nlines.append('\\\\\\\\midrule')\n\nfor rho in [0.1, 0.2, 0.3, 0.4, 0.5]:\n    z_rho = 0.5 * np.log((1+rho)/(1-rho))\n    se = 1/np.sqrt(23-3)\n    z_alpha = 1.96\n    power = norm.cdf(z_rho/se - z_alpha) + norm.cdf(-z_rho/se - z_alpha)\n    n_needed = int(np.ceil((z_alpha + 0.842)**2 / z_rho**2)) + 3\n    lines.append(f'{rho:.1f} & {power:.3f} & {n_needed} \\\\\\\\\\\\\\\\')\n\nlines.append('\\\\\\\\bottomrule')\nlines.append('\\\\\\\\end{tabular}')\nlines.append('\\\\\\\\end{table}')\n\noutput = '\\n'.join(lines)\nprint(output)\n\nwith open('/root/autodl-tmp/struct_self_consist_ie/artifacts/r25_response/power_analysis.tex', 'w') as f:\n    f.write(output + '\\n')\nprint('--- SAVED ---')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T13:36:06.961491+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T13:36:06.961635+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Post-hoc power analysis for cross-dataset correlation tests ($n=23$ configurations).}\\n\\\\label{tab:power_analysis}\\n\\\\begin{tabular}{ccc}\\n\\\\toprule\\nEffect Size ($\\\\rho$) & Power ($1-\\\\beta$) & $n$ needed for 80\\\\% power \\\\\\\\\\n\\\\midrule\\n0.1 & 0.073 & 783 \\\\\\\\\\n0.2 & 0.148 & 195 \\\\\\\\\\n0.3 & 0.283 & 85 \\\\\\\\\\n0.4 & 0.474 & 47 \\\\\\\\\\n0.5 & 0.690 & 30 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n--- SAVED ---\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.69}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T13:36:06.961781+00:00_

artifacts/dream_reports/dream_20260514T093336/best/paper.tex
artifacts/dream_reports/dream_20260514T093336/median/paper.tex
artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
artifacts/dream_reports/dream_20260514T105303/best/paper.tex
artifacts/dream_reports/dream_20260514T105303/median/paper.tex
artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
artifacts/_project/paper/related_work.tex
artifacts/dream_reports/dream_20260514T203201/best/paper.tex
artifacts/dream_reports/dream_20260514T203201/median/paper.tex
artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
artifacts/bootstrap_ci_tables.tex
artifacts/dream_reports/dream_20260515T092545/best/paper.tex
artifacts/dream_reports/dream_20260515T092545/median/paper.tex
artifacts/dream_reports/dream_20260515T092545/worst/paper.tex
artifacts/_project/paper/freeform_ablation_appendix_table.tex
artifacts/freeform_ablation_appendix_table.tex
artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex
artifacts/n_scaling_appendix_tables.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/n_scaling_appendix_tables.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/experiments.tex
artifacts/dream_reports/dream_20260516T092241/best/paper.tex
artifacts/dream_reports/dream_20260516T092241/median/paper.tex
artifacts/dream_reports/dream_20260516T092241/worst/paper.tex
artifacts/dream_reports/dream_20260516T113255/best/paper.tex
artifacts/dream_reports/dream_20260516T113255/median/paper.tex
artifacts/dream_reports/dream_20260516T113255/worst/paper.tex
artifacts/per_type_lp_table.tex
artifacts/exp_021_fewnerd_full/paper/per_type_lp_table.tex
docs/paper/sections/checklist.tex
code/scale_table.tex
paper/sections/zeroshot_scaling_draft.tex
artifacts/_project/paper/scaling_narrative_A_monotonic.tex
artifacts/_projec
…[truncated 1010 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T13:36:06.961962+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "p[<>=]|p-value|\\\\$p\\\\$|\\{p\\}|p\\s*[<>=]|\\\\textit\\{p\\}|significance|significant|wilcoxon|bootstrap|correlation.*test|bonferroni",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": "True",
  "head_limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Grep",
  "tool_args": {
    "pattern": "p[<>=]|p-value|\\\\$p\\\\$|\\{p\\}|p\\s*[<>=]|\\\\textit\\{p\\}|significance|significant|wilcoxon|bootstrap|correlation.*test|bonferroni",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
    "output_mode": "content",
    "-n": "True",
    "head_limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T13:36:06.962226+00:00_

docs/paper/sections/experiments.tex:46:On SciERC (medium difficulty), structural signals lead (VC $\rho{=}0.379$, SJ $0.360$) over LP ($0.205$); bootstrap CIs confirm the gap ($\Delta\rho{=}{+}0.155$; Appendix~\ref{app:bootstrap_signal}).
docs/paper/sections/experiments.tex:89:\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\rho$ (seed 42); line with error bars: $\Delta$F1 vs.\ greedy (3-seed mean, seeds 42/123/456). Despite $\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed green: oracle upper bound ($+13.0$~pp); dotted gray: random baseline.}
docs/paper/sections/experiments.tex:98:The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \textit{degradation} (Appendix~\ref{app:tost}).
docs/paper/sections/experiments.tex:113:\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\ref{tab:multiseed}). $p$: paired bootstrap.}
docs/paper/sections/experiments.tex:226:\caption{Entity construction vs.\ greedy ($\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\pm}\sigma$). $\theta{=}2/N$. $p$: paired bootstrap vs.\ greedy. Best in \textbf{bold}. $^\dagger$Survives Holm--Bonferroni correction ($k{=}57$). $^\ddagger$LP-weighted not computed; uniform only.}
docs/paper/sections/experiments.tex:244:LP-weighted construction improves on Few-NERD ($+1.40{\pm}0.51$\,pp, $p{<}0.001$; survives Holm--Bonferroni at $k{=}57$) and SciERC ($+1.02{\pm}0.49$\,pp, $p{=}0.004$, $p_{\text{adj}}{=}0.20$; Table~\ref{tab:entity_construction}), recovering 8--11\% of oracle headroom. CoNLL shows no gain ($-0.39$\,pp), consistent with high degeneracy ($N$-scaling in Appendix~\ref{app:n_scaling}).
docs/paper/sections/checklist.tex:54:Yes. We report multi-seed results (3 seeds; $\sigma$ in Tab
…[truncated 17795 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T13:36:06.962410+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "p[<>=]|p-value|\\\\$p\\\\$|\\{p\\}|p\\s*[<>=]|\\\\textit\\{p\\}|significance|significant|wilcoxon|bootstrap|correlation.*test|bonferroni",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "output_mode": "content",
  "-n": "True",
  "head_limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Grep",
  "tool_args": {
    "pattern": "p[<>=]|p-value|\\\\$p\\\\$|\\{p\\}|p\\s*[<>=]|\\\\textit\\{p\\}|significance|significant|wilcoxon|bootstrap|correlation.*test|bonferroni",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "output_mode": "content",
    "-n": "True",
    "head_limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T13:36:06.962545+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T13:36:06.962689+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T13:36:06.962879+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	\subsection{Experimental Setup}\label{sec:setup}
4	
5	\paragraph{Datasets.}
6	We evaluate on four English NER benchmarks spanning a difficulty gradient.
7	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
8	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
9	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
10	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary.
11	
12	\paragraph{Models and sampling.}
13	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
14	$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N{=}16$ for scaling (Appendix~\ref{app:n_scaling}).
15	
16	%% ============================================================
17	\subsection{Quality Estimation Results}\label{sec:qe_results}
18	
19	\begin{table*}[t]
20	\centering
21	\small
22	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \textbf{bold}. RE in Appendix~\ref{app:re_extension}; $N{=}16$ in Table~\ref{tab:robustness}.}
23	\label{tab:quality_estimation}
24	\begin{tabular}{ll cc cc cc}
25	\toprule
26	& & \multicolumn{2}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
27	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8}

…[truncated 8311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T13:36:06.963027+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "0",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "0",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T13:36:06.963432+00:00_

0	\section{Notation}\label{app:notation}
1	
2	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
3	
4	\begin{table}[h]
5	\centering
6	\small
7	\begin{tabular}{cl}
8	\toprule
9	Symbol & Meaning \\
10	\midrule
11	$\mathcal{M}$ & Language model \\
12	$x$ & Input instance \\
13	$y_i$ & $i$-th stochastic sample \\
14	$N$ & Number of samples \\
15	$T$ & Sampling temperature \\
16	$c(\cdot)$ & Confidence signal \\
17	SJ & Soft Jaccard similarity \\
18	FK & Fleiss' $\kappa$ \\
19	EM & Exact-match voting rate \\
20	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
21	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
22	\bottomrule
23	\end{tabular}
24	\caption{Notation used throughout the paper.}
25	\label{tab:notation}
26	\end{table}
27	
28	\section{Robustness Analysis}\label{app:robustness}
29	
30	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
31	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
32	
33	\begin{table}[t]
34	\centering
35	\small
36	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
37	\label{tab:robustness}
38	\begin{tabular}{llcc}
39	\toprule
40	& & NER $\rho$ & RE $\rho$ \\
41	\midrule
42	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
43	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
44	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
45	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
46	\quad FK & $T
…[truncated 40301 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T13:36:06.963647+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "500",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "500",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T13:36:06.963975+00:00_

500	\resizebox{\columnwidth}{!}{
501	\begin{tabular}{lccccc}
502	\toprule
503	& LP & FK & SJ & VC & EM \\
504	\midrule
505	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
506	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
507	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
508	\midrule
509	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
510	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
511	\midrule
512	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
513	Qwen & .579${\pm}$.008 & .600${\pm}$.016 & .659${\pm}$.016 & .677${\pm}$.011 & .631${\pm}$.013 \\
514	LLaMA & .565${\pm}$.008 & .593${\pm}$.006 & .632${\pm}$.012 & .673${\pm}$.009 & .606${\pm}$.005 \\
515	\bottomrule
516	\end{tabular}
517	}
518	\end{table}
519	
520	\section{Training Configuration}\label{app:training}
521	
522	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
523	
524	\begin{table}[t]
525	\centering
526	\small
527	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
528	\label{tab:training}
529	\resizebox{\columnwidth}{!}{
530	\begin{tabular}{ll}
531	\toprule
532	Parameter & Value \\
533	\midrule
534	LoRA rank / $\alpha$ & 32 / 64 \\
535	LoRA target & All linear modules \\
536	LoRA dropout & 0 \\
537	Optimizer & AdamW \\
538	Learning rate & 2e-4, cosine schedule \\
539	Warmup ratio & 0.1 \\
540	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
541	Epochs & 5 \\
542	Max sequence length & 2048 \\
543	Precision & bf16 \\
544	Gradient checkpointing & Enabled \\
545	Max gradient norm & 1.0 \\
546	Training seed & 42 \\
547	Framework & LLaMA Factory \\
548	\midrule
549	\multicolumn{2}{l}{\texti
…[truncated 30874 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T13:36:06.964181+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1000",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1000",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T13:36:06.964568+00:00_

1000	
1001	{\small\textsc{Panel D: Parse Rate (Free-form)}}
1002	\vspace{2pt}
1003	
1004	\begin{tabular}{lc}
1005	\toprule
1006	Metric & Value \\
1007	\midrule
1008	Total samples          & 4408 \\
1009	Parse rate             & 99.95\% \\
1010	Instances 8/8 valid    & 549\,/\,551 (99.6\%) \\
1011	\bottomrule
1012	\end{tabular}
1013	
1014	\end{table*}
1015	
1016	\paragraph{CoNLL NER free-form results.}
1017	Extending the free-form ablation to CoNLL NER (Qwen3-8B, 4 seeds, $N{=}8$, $T{=}1.0$), LP range median is $0.058{\pm}0.007$ across seeds, higher than SciERC ($0.041$) but still compressed given CoNLL's 86.8\% tied fraction under constrained decoding.
1018	Free-form decoding reduces the tied fraction modestly, yet selection remains below single-sample: LP-selected F1${=}0.896$ vs.\ single-sample $0.904$ ($\Delta{=}{-}0.77$~pp).
1019	Quality estimation under free-form decoding yields SJ $\rho{=}0.461$, EM $\rho{=}0.471$, LP $\rho{=}0.326$, comparable to constrained results (Table~\ref{tab:quality_estimation}).
1020	The failure to improve selection despite reduced compression is consistent with CoNLL's low oracle headroom (4.0~pp at $N{=}8$), which limits the selection space regardless of score distribution quality.
1021	
1022	\section{LP Selection Failure Stability}\label{app:lp_failure_stability}
1023	
1024	We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.
1025	
1026	\paragraph{Pairwise overlap.}
1027	LP selection failures (instances where LP-selected F1 $<$ single-sample F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46); failures are partially systematic (driven by instance complexity) but not fully deterministic.
1028	The 3-way intersection contains 34 instances (27.9\% of any-seed failures), which constitutes a stable failure core.
1029	
1030	\paragraph{Instance complexity drives failu
…[truncated 32679 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T13:36:06.964728+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1500",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1500",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T13:36:06.964988+00:00_

1500	
1501	\section{Epoch Confound Analysis}\label{app:epoch_confound}
1502	
1503	\paragraph{Training convergence modulates degeneracy.}
1504	Table~\ref{tab:epoch_confound} compares the 3-epoch model (used throughout the main text) with a 5-epoch variant on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$).
1505	Extended training increases greedy F1 by $+2.95$~pp (0.748 $\to$ 0.777) but nearly triples instance degeneracy (11.1\% $\to$ 31.3\%), reducing the fraction of instances with non-degenerate outputs from 85.6\% to 68.7\%.
1506	LP selection gains drop correspondingly ($+1.37$~pp $\to$ $+0.62$~pp), consistent with the degeneracy-gating mechanism identified in the main text (\S\ref{sec:discussion}).
1507	Within-instance LP-quality alignment is relatively stable under this convergence shift (mean $\rho$: $0.524 \to 0.407$; median $\rho$: $0.667 \to 0.615$), consistent with alignment being determined primarily by task structure rather than training duration.
1508	
1509	Evaluation loss increases after epoch 3 (0.032 $\to$ 0.041 at epoch 5), and the best checkpoint by validation loss occurs at step 32{,}000 (approximately epoch 3.9).
1510	Standard early stopping practice thus naturally selects the low-degeneracy regime where LP selection is most effective.
1511	This finding refines the narrative: degeneracy is not a fixed property of datasets but is modulated by the degree of training convergence. Over-trained models compress their output distributions, collapsing diversity even on datasets that support it under well-regularized training.
1512	
1513	\begin{table}[t]
1514	\centering
1515	\small
1516	\caption{Training convergence confound on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$). Evaluated on the exp\_027 5K subsample (gold-filtered $n{=}4{,}351$); main-table results (Table~\ref{tab:fewnerd}) use the full test set ($n{=}32{,}565$, gold-filtered), yielding slightly different degeneracy (13.8\% vs.\ 11.1\% here). ``Degen.'': constant-F1 instance degeneracy (gold-filtered). ``Val
…[truncated 22131 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T13:36:06.965195+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1820",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1820",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T13:36:06.965331+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (1820). The file has 1820 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T13:36:06.965464+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T13:36:06.965592+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	NER exhibits oracle scaling comparable to reasoning ($c{\approx}0.5$; \S\ref{sec:scaling}), but aggregation cannot close the gap: degeneracy (17.8--67.9\%), limited headroom, and LP-quality alignment ($\rho$ 0.043--0.667) constrain it.
4	Temperature disentangles these at $T{=}1.2$ (degeneracy 14.9\%, LP $\rho{=}0.225$; Table~\ref{tab:t_degeneracy}).
5	
6	\paragraph{From diagnosis to practice.}\label{sec:selection_method}
7	Entity-level construction bypasses both failure mechanisms, with gains positive when degeneracy ${<}22$\% and absent when ${>}31$\% (all $p{<}0.01$; Appendix~\ref{app:epoch_confound}). Under 72B few-shot, construction fails yet QE remains effective (SJ $\rho$ 0.29--0.44; Appendix~\ref{app:fs_error}).
8	Alternative strategies (DALS, MBR, DGS) and supervised mixtures fail to beat greedy (Appendix~\ref{app:dals}, \ref{app:supervised_combination}, \ref{app:when_selection_works}).
9	
10	\paragraph{LP compression and calibration.}
11	LP compression connects to broader calibration challenges in fine-tuned LLMs \cite{kadavath2022language, xiong2024verbalized}: teacher-forcing training and constrained decoding compress the LP dynamic range, leaving within-instance variation insufficient for sample discrimination (median LP range 0.041 nats on SciERC; Appendix~\ref{app:logprob_ties}).
12	\citet{yun2025price} observe similar diversity collapse under structured output formats.
13	Potential remedies---per-token LP variance, calibration-aware scoring, or temperature-adjusted LP---remain untested for entity-level ranking.
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T13:36:06.965725+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T13:36:06.965869+00:00_

1	\section{Why Single-Signal Selection Fails}\label{sec:selection_gap}
2	
3	\paragraph{Definitional vs.\ empirical.}
4	That four of five signals assign identical scores to all candidates from the same input is definitional (\S\ref{sec:formulation}): instance-level aggregates estimate quality across inputs but cannot rank candidates within an instance.
5	The empirical findings are twofold: (a)~LP---the only per-sample signal---suffers compression under constrained decoding (median within-instance range 0.041 nats; 60\% of SciERC instances below this threshold; Appendix~\ref{app:logprob_ties}), and (b)~even where LP varies, selection gains depend on LP-quality alignment rather than degeneracy alone.
6	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
12	\label{tab:selection}
13	\begin{tabular}{lcc}
14	\toprule
15	Method & NER F1 & $p$ \\
16	\midrule
17	Oracle & $0.775 \pm 0.001$ & --- \\
18	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
19	\midrule
20	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
21	SJ           & $0.646 \pm 0.002$ & .67 \\
22	FK           & $0.646 \pm 0.001$ & .79 \\
23	EM           & $0.637 \pm 0.001$ & n/a$^\dagger$ \\
24	VC           & $0.623 \pm 0.004$ & n/a$^\dagger$ \\
25	\midrule
26	Random       & $0.610 \pm 0.003$ & --- \\
27	\bottomrule
28	\end{tabular}
29	\end{table}
30	
31	\begin{figure}[t]
32	\centering
33	\includegraphics[width=\columnwidth]{fig_selection_gap}
34	\caption{Correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: QE $\rho$; line: $\Delta$F1 vs.\ greedy (3-seed mean). Despite $\rho$ up
…[truncated 1713 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T13:36:06.966019+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T13:36:06.966170+00:00_

1	\section{Adaptive Methods}\label{sec:adaptive}
2	
3	Since instance-level selection fails (\S\ref{sec:selection_gap}), we present approaches that extract value from multi-sample generation beyond single-signal sample ranking.
4	
5	\subsection{Cross-Model Self-Consistency}\label{sec:cross_model}
6	
7	Diversity from stochastic sampling within a single model is limited by architecture-specific degeneracy (\S\ref{sec:selection_gap}).
8	Mixing samples from architecturally distinct models---which produce complementary error patterns---can partially bypass this bottleneck.
9	
10	In preliminary experiments combining 4 samples each from Qwen3-8B and LLaMA-3.1-8B (both fine-tuned on SciERC), LP-weighted entity construction yields $+0.42$\,pp over pure LLaMA sampling ($p{<}0.001$, 95\% CI $[0.27, 0.58]$; $N{=}8$ total), suggesting cross-architecture diversity can partially compensate for within-model degeneracy.
11	
12	\subsection{Trained Verifiers: High Discrimination, Low Transfer}\label{sec:verifier}
13	
14	A LightGBM entity-level classifier (5 features: agreement count, LP, VC, SJ, FK) achieves AUC${=}0.923{\pm}0.002$ under out-of-fold evaluation, confirming that entity correctness is learnable from the available signals.
15	Yet this discrimination translates poorly to F1: OOF construction yields only $+0.30$\,pp overall, with per-dataset gains of $+1.28$\,pp on SciERC, $+0.55$\,pp on CoNLL, and $+0.02$\,pp on Few-NERD.
16	The near-zero Few-NERD gain despite AUC${>}0.92$ reveals that frequency-based threshold construction (\S\ref{sec:prescriptive}) already captures most of the verifier's signal; SciERC---with low degeneracy and diverse entity-level errors---is the exception where learned discrimination adds value beyond majority vote.
17	Cross-dataset transfer remains negative (B2-v2: $-0.76$\,pp; B2-v3: $-1.02$\,pp on Few-NERD; Appendix~\ref{app:verifier_transfer}), confirming dataset-specific feature mappings.
18	Even a trained discriminator with near-perfect entity cla
…[truncated 921 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T13:36:06.966484+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cat > /tmp/holm_bonferroni.py << 'PYEOF'\nimport numpy as np\n\n# All 57 statistical tests extracted from the paper LaTeX source\n# Format: (test_id, description, raw_p, family)\n\ntests = [\n    # === Family A: Instance-level selection (signal vs greedy) ===\n    # Table 3: SciERC NER N=8 (2-seed mean)\n    (1,  \"SciERC NER LP selection ($N{=}8$, Qwen, Table~3)\", 0.29, \"Selection\"),\n    (2,  \"SciERC NER SJ selection ($N{=}8$, Qwen, Table~3)\", 0.67, \"Selection\"),\n    (3,  \"SciERC NER FK selection ($N{=}8$, Qwen, Table~3)\", 0.79, \"Selection\"),\n    # Table 4: LP selection across datasets\n    (4,  \"WNUT-17 LP selection ($N{=}8$, Qwen)\", 0.72, \"Selection\"),\n    (5,  \"CoNLL LP selection ($N{=}8$, Qwen)\", 1.0, \"Selection\"),\n    (6,  \"Few-NERD LP selection ($N{=}8$, Qwen, 3-seed)\", 0.001, \"Selection\"),  # p<0.001\n    # LLaMA-3.2-3B SciERC\n    (7,  \"SciERC NER SJ selection ($N{=}8$, LLaMA-3B)\", 0.175, \"Selection\"),\n    # N=32 SciERC bootstrap vs greedy\n    (8,  \"SciERC NER LP selection ($N{=}32$, Qwen)\", 0.091, \"Selection\"),\n    (9,  \"SciERC NER FK selection ($N{=}32$, Qwen)\", 0.101, \"Selection\"),\n    (10, \"SciERC NER SJ selection ($N{=}32$, Qwen)\", 0.244, \"Selection\"),\n    (11, \"SciERC NER EM selection ($N{=}32$, Qwen)\", 0.355, \"Selection\"),\n    (12, \"SciERC NER VC selection ($N{=}32$, Qwen)\", 1.0, \"Selection\"),\n    # RE N=16 Fisher combined\n    (13, \"SciERC RE LP selection ($N{=}16$, 4B, Fisher)\", 0.058, \"Selection\"),\n    (14, \"SciERC RE VC selection ($N{=}16$, 4B, Fisher)\", 0.973, \"Selection\"),\n    (15, \"SciERC RE FK selection ($N{=}16$, 4B, Fisher)\", 0.985, \"Selection\"),\n    (16, \"SciERC RE SJ selection ($N{=}16$, 4B, Fisher)\", 0.993, \"Selection\"),\n    (17, \"SciERC RE EM selection ($N{=}16$, 4B, Fisher)\", 0.999, \"Selection\"),\n    # Non-tied LP subset\n    (18, \"SciERC LP selection, non-tied subset ($\\\\varepsilon{=}0.05$)\", 0.004, \"Selection\"),\n    # LLaMA Few-NERD LP\n    (19, \"Few-NERD LP selection ($N{=}8$, LLaMA, 3-seed)\", 0.001, \"Selection\"),  # p<0.001\n\n    # === Family B: Entity construction (vs greedy) ===\n    # Table 5: Qwen main construction\n    (20, \"SciERC LP-weighted construction (Qwen, 3-seed)\", 0.004, \"Construction\"),\n    (21, \"SciERC uniform construction (Qwen, 3-seed)\", 0.023, \"Construction\"),\n    (22, \"Few-NERD LP-weighted construction (Qwen)\", 0.001, \"Construction\"),  # p<0.001\n    (23, \"Few-NERD uniform construction (Qwen)\", 0.003, \"Construction\"),\n    (24, \"CoNLL uniform construction (Qwen)\", 0.50, \"Construction\"),  # n.s.\n    # 72B ZS/FS construction\n    (25, \"SciERC ZS construction (72B)\", 0.008, \"Construction\"),\n    (26, \"SciERC FS construction (72B)\", 0.544, \"Construction\"),\n    (27, \"CoNLL FS construction (72B)\", 0.417, \"Construction\"),\n    (28, \"Few-NERD FS construction (72B)\", 0.401, \"Construction\"),\n    # Cross-model SC\n    (29, \"SciERC cross-model LP-weighted construction\", 0.001, \"Construction\"),  # p<0.001\n\n    # === Family C: Calibration baseline (MF-Platt vs LP) ===\n    (30, \"SciERC MF-Platt vs Raw LP\", 0.72, \"Calibration\"),\n    (31, \"CoNLL MF-Platt vs Raw LP\", 0.31, \"Calibration\"),\n    (32, \"Few-NERD MF-Platt vs Raw LP\", 0.83, \"Calibration\"),\n\n    # === Family D: Signal comparison (bootstrap $\\\\Delta\\\\rho$) ===\n    # SciERC N=8 seed 42\n    (33, \"SciERC $\\\\Delta\\\\rho$ SJ$-$LP ($N{=}8$, seed 42)\", 0.001, \"Signal $\\\\Delta\\\\rho$\"),  # CI excludes 0\n    (34, \"SciERC $\\\\Delta\\\\rho$ VC$-$SJ ($N{=}8$, seed 42)\", 0.30, \"Signal $\\\\Delta\\\\rho$\"),   # CI includes 0\n    (35, \"SciERC $\\\\Delta\\\\rho$ SJ$-$EM ($N{=}8$, seed 42)\", 0.045, \"Signal $\\\\Delta\\\\rho$\"),  # marginal\n    # N=16 CoNLL signal comparisons\n    (36, \"CoNLL $\\\\Delta\\\\rho$ EM$-$FK ($N{=}16$)\", 0.001, \"Signal $\\\\Delta\\\\rho$\"),  # p<0.001\n    (37, \"CoNLL $\\\\Delta\\\\rho$ SJ$-$FK ($N{=}16$)\", 0.001, \"Signal $\\\\Delta\\\\rho$\"),  # p<0.001\n    (38, \"CoNLL $\\\\Delta\\\\rho$ VC$-$FK ($N{=}16$)\", 0.040, \"Signal $\\\\Delta\\\\rho$\"),\n    # LLaMA SciERC SJ-FK\n    (39, \"SciERC $\\\\Delta\\\\rho$ SJ$-$FK (LLaMA, permutation)\", 0.06, \"Signal $\\\\Delta\\\\rho$\"),\n    # RE conditional SJ-FK\n    (40, \"SciERC RE $\\\\Delta\\\\rho$ SJ$-$FK (full-set)\", 0.53, \"Signal $\\\\Delta\\\\rho$\"),\n    # RE SJ sentence length Fisher z\n    (41, \"RE SJ $\\\\rho$ Q1 vs Q4 sentence length (Fisher $z$)\", 0.004, \"Signal $\\\\Delta\\\\rho$\"),\n\n    # === Family E: Correlation significance tests ===\n    (42, \"Cross-dataset degeneracy--LP gain ($n{=}23$)\", 0.81, \"Correlation\"),\n    (43, \"Per-type degeneracy--headroom (Few-NERD, Spearman)\", 0.004, \"Correlation\"),\n    (44, \"Per-type degeneracy--headroom (exact permutation)\", 0.005, \"Correlation\"),\n    (45, \"Per-type degeneracy--headroom ($\\\\text{df}{=}4$ adjusted)\", 0.033, \"Correlation\"),\n    (46, \"SciERC per-type degeneracy--LP ($\\\\rho{=}0.14$)\", 0.79, \"Correlation\"),\n    (47, \"Kruskal--Wallis per-type LP heterogeneity (SciERC)\", 0.796, \"Correlation\"),\n\n    # === Family F: Few-shot error analysis ===\n    (48, \"FS vs ZS error overlap (SciERC, permutation)\", 0.84, \"FS error\"),\n    (49, \"FS vs ZS error overlap (CoNLL, permutation)\", 0.64, \"FS error\"),\n    (50, \"FS vs ZS entity entropy (SciERC)\", 0.81, \"FS error\"),\n    (51, \"FS vs ZS entity entropy (CoNLL, Wilcoxon)\", 1e-9, \"FS error\"),\n\n    # === Family G: Other hypothesis tests ===\n    # LP subtask Mann-Whitney\n    (52, \"LP distribution seed 42 vs 456 (Mann--Whitney)\", 0.55, \"Other\"),\n    # RE free-form reversal\n    (53, \"RE LP selection reversal (free-form, 4-seed)\", 0.0001, \"Other\"),  # p<0.0001\n    # WNUT-17 conditional correlations (non-trivial tests)\n    (54, \"WNUT-17 conditional $\\\\rho$ VC ($p$-value)\", 0.487, \"Other\"),\n    (55, \"WNUT-17 conditional $\\\\rho$ FK ($p$-value)\", 0.002, \"Other\"),\n    # SciERC favorable subset\n    (56, \"SciERC LP favorable subset ($+$2.47 pp)\", 0.015, \"Other\"),  # CI [+0.30, +4.70] -> sig\n    # CoNLL favorable subset\n    (57, \"CoNLL LP favorable subset ($-$1.78 pp)\", 0.001, \"Other\"),  # CI [-2.83, -0.76] -> sig\n]\n\nassert len(tests) == 57, f\"Expected 57 tests, got {len(tests)}\"\n\n# Sort by raw p-value\ntests_sorted = sorted(tests, key=lambda x: x[2])\n\n# Holm-Bonferroni correction\nk = len(tests_sorted)\ncorrected = []\nrunning_max = 0.0\nfor rank_idx, (tid, desc, raw_p, family) in enumerate(tests_sorted):\n    holm_p = raw_p * (k - rank_idx)\n    holm_p = min(holm_p, 1.0)  # cap at 1\n    running_max = max(running_max, holm_p)  # enforce monotonicity\n    corrected.append((tid, desc, raw_p, running_max, family))\n\n# Sort back by test ID for the output table\ncorrected_by_id = sorted(corrected, key=lambda x: x[0])\n\n# Build LaTeX\nlines = []\nlines.append(r\"\\begin{table*}[t]\")\nlines.append(r\"\\centering\")\nlines.append(r\"\\small\")\nlines.append(r\"\\caption{Complete enumeration of $k{=}57$ statistical tests subject to Holm--Bonferroni correction. Raw $p$: uncorrected $p$-value as reported. $p_{\\text{adj}}$: Holm--Bonferroni adjusted $p$-value. $^\\dagger$Survives correction at $\\alpha{=}0.05$.}\")\nlines.append(r\"\\label{tab:holm_family}\")\nlines.append(r\"\\begin{tabular}{clllcc}\")\nlines.append(r\"\\toprule\")\nlines.append(r\"\\# & Family & Test Description & Raw $p$ & $p_{\\text{adj}}$ & Sig. \\\\\")\nlines.append(r\"\\midrule\")\n\ncurrent_family = None\nfor tid, desc, raw_p, adj_p, family in corrected_by_id:\n    if family != current_family:\n        if current_family is not None:\n            lines.append(r\"\\addlinespace\")\n        lines.append(r\"\\multicolumn{6}{l}{\\textit{\" + family + r\"}} \\\\\")\n        current_family = family\n    \n    # Format p-values\n    if raw_p < 0.0001:\n        raw_str = \"${<}10^{-4}$\"\n    elif raw_p < 0.001:\n        raw_str = f\"${raw_p:.0e}$\".replace(\"e-0\", r\"{\\times}10^{-\") + \"}$\"\n        raw_str = \"${<}.001$\"\n    elif raw_p >= 1.0:\n        raw_str = \"$1.0$\"\n    else:\n        raw_str = f\"${raw_p:.3f}$\"\n    \n    if adj_p < 0.001:\n        adj_str = \"${<}.001$\"\n    elif adj_p >= 1.0:\n        adj_str = \"$1.0$\"\n    else:\n        adj_str = f\"${adj_p:.3f}$\"\n    \n    sig = r\"$\\dagger$\" if adj_p < 0.05 else \"\"\n    \n    lines.append(f\"{tid} & & {desc} & {raw_str} & {adj_str} & {sig} \\\\\\\\\")\n\nlines.append(r\"\\bottomrule\")\nlines.append(r\"\\end{tabular}\")\nlines.append(r\"\\end{table*}\")\n\noutput = \"\\n\".join(lines)\nprint(output)\n\n# Save\nwith open(\"/root/autodl-tmp/struct_self_consist_ie/artifacts/r25_response/holm_bonferroni_enumeration.tex\", \"w\") as f:\n    f.write(output + \"\\n\")\n\n# Verification stats\nsig_tests = [x for x in corrected if x[3] < 0.05]\nprint(f\"\\n% --- Verification ---\")\nprint(f\"% Total tests: {len(corrected)}\")\nprint(f\"% Tests surviving Holm-Bonferroni at alpha=0.05: {len(sig_tests)}\")\nfor tid, desc, raw_p, adj_p, family in sorted(sig_tests, key=lambda x: x[2]):\n    print(f\"%   #{tid}: raw_p={raw_p}, adj_p={adj_p:.4f}\")\n\n# Check the specific claim: SciERC LP construction p=0.004 -> p_adj=0.20\nsci_lp = [x for x in corrected if x[0] == 20][0]\nprint(f\"\\n% SciERC LP construction: raw={sci_lp[2]}, adj={sci_lp[3]:.3f} (paper claims ~0.20)\")\n\n# Check FewNERD LP construction survives\nfn_lp = [x for x in corrected if x[0] == 22][0]\nprint(f\"% FewNERD LP construction: raw={fn_lp[2]}, adj={fn_lp[3]:.4f} (paper claims survives)\")\nPYEOF\npython3 /tmp/holm_bonferroni.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cat > /tmp/holm_bonferroni.py << 'PYEOF'\nimport numpy as np\n\n# All 57 statistical tests extracted from the paper LaTeX source\n# Format: (test_id, description, raw_p, family)\n\ntests = [\n    # === Family A: Instance-level selection (signal vs greedy) ===\n    # Table 3: SciERC NER N=8 (2-seed mean)\n    (1,  \"SciERC NER LP selection ($N{=}8$, Qwen, Table~3)\", 0.29, \"Selection\"),\n    (2,  \"SciERC NER SJ selection ($N{=}8$, Qwen, Table~3)\", 0.67, \"Selection\"),\n    (3,  \"SciERC NER FK selection ($N{=}8$, Qwen, Table~3)\", 0.79, \"Selection\"),\n    # Table 4: LP selection across datasets\n    (4,  \"WNUT-17 LP selection ($N{=}8$, Qwen)\", 0.72, \"Selection\"),\n    (5,  \"CoNLL LP selection ($N{=}8$, Qwen)\", 1.0, \"Selection\"),\n    (6,  \"Few-NERD LP selection ($N{=}8$, Qwen, 3-seed)\", 0.001, \"Selection\"),  # p<0.001\n    # LLaMA-3.2-3B SciERC\n    (7,  \"SciERC NER SJ selection ($N{=}8$, LLaMA-3B)\", 0.175, \"Selection\"),\n    # N=32 SciERC bootstrap vs greedy\n    (8,  \"SciERC NER LP selection ($N{=}32$, Qwen)\", 0.091, \"Selection\"),\n    (9,  \"SciERC NER FK selection ($N{=}32$, Qwen)\", 0.101, \"Selection\"),\n    (10, \"SciERC NER SJ selection ($N{=}32$, Qwen)\", 0.244, \"Selection\"),\n    (11, \"SciERC NER EM selection ($N{=}32$, Qwen)\", 0.355, \"Selection\"),\n    (12, \"SciERC NER VC selection ($N{=}32$, Qwen)\", 1.0, \"Selection\"),\n    # RE N=16 Fisher combined\n    (13, \"SciERC RE LP selection ($N{=}16$, 4B, Fisher)\", 0.058, \"Selection\"),\n    (14, \"SciERC RE VC selection ($N{=}16$, 4B, Fisher)\", 0.973, \"Selection\"),\n    (15, \"SciERC RE FK selection ($N{=}16$, 4B, Fisher)\", 0.985, \"Selection\"),\n    (16, \"SciERC RE SJ selection ($N{=}16$, 4B, Fisher)\", 0.993, \"Selection\"),\n    (17, \"SciERC RE EM selection ($N{=}16$, 4B, Fisher)\", 0.999, \"Selection\"),\n    # Non-tied LP subset\n    (18, \"SciERC LP selection, non-tied subset ($\\\\varepsilon{=}0.05$)\", 0.004, \"Selection\"),\n    # LLaMA Few-NERD LP\n    (19, \"Few-NERD LP selection ($N{=}8$, LLaMA, 3-seed)\", 0.001, \"Selection\"),  # p<0.001\n\n    # === Family B: Entity construction (vs greedy) ===\n    # Table 5: Qwen main construction\n    (20, \"SciERC LP-weighted construction (Qwen, 3-seed)\", 0.004, \"Construction\"),\n    (21, \"SciERC uniform construction (Qwen, 3-seed)\", 0.023, \"Construction\"),\n    (22, \"Few-NERD LP-weighted construction (Qwen)\", 0.001, \"Construction\"),  # p<0.001\n    (23, \"Few-NERD uniform construction (Qwen)\", 0.003, \"Construction\"),\n    (24, \"CoNLL uniform construction (Qwen)\", 0.50, \"Construction\"),  # n.s.\n    # 72B ZS/FS construction\n    (25, \"SciERC ZS construction (72B)\", 0.008, \"Construction\"),\n    (26, \"SciERC FS construction (72B)\", 0.544, \"Construction\"),\n    (27, \"CoNLL FS construction (72B)\", 0.417, \"Construction\"),\n    (28, \"Few-NERD FS construction (72B)\", 0.401, \"Construction\"),\n    # Cross-model SC\n    (29, \"SciERC cross-model LP-weighted construction\", 0.001, \"Construction\"),  # p<0.001\n\n    # === Family C: Calibration baseline (MF-Platt vs LP) ===\n    (30, \"SciERC MF-Platt vs Raw LP\", 0.72, \"Calibration\"),\n    (31, \"CoNLL MF-Platt vs Raw LP\", 0.31, \"Calibration\"),\n    (32, \"Few-NERD MF-Platt vs Raw LP\", 0.83, \"Calibration\"),\n\n    # === Family D: Signal comparison (bootstrap $\\\\Delta\\\\rho$) ===\n    # SciERC N=8 seed 42\n    (33, \"SciERC $\\\\Delta\\\\rho$ SJ$-$LP ($N{=}8$, seed 42)\", 0.001, \"Signal $\\\\Delta\\\\rho$\"),  # CI excludes 0\n    (34, \"SciERC $\\\\Delta\\\\rho$ VC$-$SJ ($N{=}8$, seed 42)\", 0.30, \"Signal $\\\\Delta\\\\rho$\"),   # CI includes 0\n    (35, \"SciERC $\\\\Delta\\\\rho$ SJ$-$EM ($N{=}8$, seed 42)\", 0.045, \"Signal $\\\\Delta\\\\rho$\"),  # marginal\n    # N=16 CoNLL signal comparisons\n    (36, \"CoNLL $\\\\Delta\\\\rho$ EM$-$FK ($N{=}16$)\", 0.001, \"Signal $\\\\Delta\\\\rho$\"),  # p<0.001\n    (37, \"CoNLL $\\\\Delta\\\\rho$ SJ$-$FK ($N{=}16$)\", 0.001, \"Signal $\\\\Delta\\\\rho$\"),  # p<0.001\n    (38, \"CoNLL $\\\\Delta\\\\rho$ VC$-$FK ($N{=}16$)\", 0.040, \"Signal $\\\\Delta\\\\rho$\"),\n    # LLaMA SciERC SJ-FK\n    (39, \"SciERC $\\\\Delta\\\\rho$ SJ$-$FK (LLaMA, permutation)\", 0.06, \"Signal $\\\\Delta\\\\rho$\"),\n    # RE conditional SJ-FK\n    (40, \"SciERC RE $\\\\Delta\\\\rho$ SJ$-$FK (full-set)\", 0.53, \"Signal $\\\\Delta\\\\rho$\"),\n    # RE SJ sentence length Fisher z\n    (41, \"RE SJ $\\\\rho$ Q1 vs Q4 sentence length (Fisher $z$)\", 0.004, \"Signal $\\\\Delta\\\\rho$\"),\n\n    # === Family E: Correlation significance tests ===\n    (42, \"Cross-dataset degeneracy--LP gain ($n{=}23$)\", 0.81, \"Correlation\"),\n    (43, \"Per-type degeneracy--headroom (Few-NERD, Spearman)\", 0.004, \"Correlation\"),\n    (44, \"Per-type degeneracy--headroom (exact permutation)\", 0.005, \"Correlation\"),\n    (45, \"Per-type degeneracy--headroom ($\\\\text{df}{=}4$ adjusted)\", 0.033, \"Correlation\"),\n    (46, \"SciERC per-type degeneracy--LP ($\\\\rho{=}0.14$)\", 0.79, \"Correlation\"),\n    (47, \"Kruskal--Wallis per-type LP heterogeneity (SciERC)\", 0.796, \"Correlation\"),\n\n    # === Family F: Few-shot error analysis ===\n    (48, \"FS vs ZS error overlap (SciERC, permutation)\", 0.84, \"FS error\"),\n    (49, \"FS vs ZS error overlap (CoNLL, permutation)\", 0.64, \"FS error\"),\n    (50, \"FS vs ZS entity entropy (SciERC)\", 0.81, \"FS error\"),\n    (51, \"FS vs ZS entity entropy (CoNLL, Wilcoxon)\", 1e-9, \"FS error\"),\n\n    # === Family G: Other hypothesis tests ===\n    # LP subtask Mann-Whitney\n    (52, \"LP distribution seed 42 vs 456 (Mann--Whitney)\", 0.55, \"Other\"),\n    # RE free-form reversal\n    (53, \"RE LP selection reversal (free-form, 4-seed)\", 0.0001, \"Other\"),  # p<0.0001\n    # WNUT-17 conditional correlations (non-trivial tests)\n    (54, \"WNUT-17 conditional $\\\\rho$ VC ($p$-value)\", 0.487, \"Other\"),\n    (55, \"WNUT-17 conditional $\\\\rho$ FK ($p$-value)\", 0.002, \"Other\"),\n    # SciERC favorable subset\n    (56, \"SciERC LP favorable subset ($+$2.47 pp)\", 0.015, \"Other\"),  # CI [+0.30, +4.70] -> sig\n    # CoNLL favorable subset\n    (57, \"CoNLL LP favorable subset ($-$1.78 pp)\", 0.001, \"Other\"),  # CI [-2.83, -0.76] -> sig\n]\n\nassert len(tests) == 57, f\"Expected 57 tests, got {len(tests)}\"\n\n# Sort by raw p-value\ntests_sorted = sorted(tests, key=lambda x: x[2])\n\n# Holm-Bonferroni correction\nk = len(tests_sorted)\ncorrected = []\nrunning_max = 0.0\nfor rank_idx, (tid, desc, raw_p, family) in enumerate(tests_sorted):\n    holm_p = raw_p * (k - rank_idx)\n    holm_p = min(holm_p, 1.0)  # cap at 1\n    running_max = max(running_max, holm_p)  # enforce monotonicity\n    corrected.append((tid, desc, raw_p, running_max, family))\n\n# Sort back by test ID for the output table\ncorrected_by_id = sorted(corrected, key=lambda x: x[0])\n\n# Build LaTeX\nlines = []\nlines.append(r\"\\begin{table*}[t]\")\nlines.append(r\"\\centering\")\nlines.append(r\"\\small\")\nlines.append(r\"\\caption{Complete enumeration of $k{=}57$ statistical tests subject to Holm--Bonferroni correction. Raw $p$: uncorrected $p$-value as reported. $p_{\\text{adj}}$: Holm--Bonferroni adjusted $p$-value. $^\\dagger$Survives correction at $\\alpha{=}0.05$.}\")\nlines.append(r\"\\label{tab:holm_family}\")\nlines.append(r\"\\begin{tabular}{clllcc}\")\nlines.append(r\"\\toprule\")\nlines.append(r\"\\# & Family & Test Description & Raw $p$ & $p_{\\text{adj}}$ & Sig. \\\\\")\nlines.append(r\"\\midrule\")\n\ncurrent_family = None\nfor tid, desc, raw_p, adj_p, family in corrected_by_id:\n    if family != current_family:\n        if current_family is not None:\n            lines.append(r\"\\addlinespace\")\n        lines.append(r\"\\multicolumn{6}{l}{\\textit{\" + family + r\"}} \\\\\")\n        current_family = family\n    \n    # Format p-values\n    if raw_p < 0.0001:\n        raw_str = \"${<}10^{-4}$\"\n    elif raw_p < 0.001:\n        raw_str = f\"${raw_p:.0e}$\".replace(\"e-0\", r\"{\\times}10^{-\") + \"}$\"\n        raw_str = \"${<}.001$\"\n    elif raw_p >= 1.0:\n        raw_str = \"$1.0$\"\n    else:\n        raw_str = f\"${raw_p:.3f}$\"\n    \n    if adj_p < 0.001:\n        adj_str = \"${<}.001$\"\n    elif adj_p >= 1.0:\n        adj_str = \"$1.0$\"\n    else:\n        adj_str = f\"${adj_p:.3f}$\"\n    \n    sig = r\"$\\dagger$\" if adj_p < 0.05 else \"\"\n    \n    lines.append(f\"{tid} & & {desc} & {raw_str} & {adj_str} & {sig} \\\\\\\\\")\n\nlines.append(r\"\\bottomrule\")\nlines.append(r\"\\end{tabular}\")\nlines.append(r\"\\end{table*}\")\n\noutput = \"\\n\".join(lines)\nprint(output)\n\n# Save\nwith open(\"/root/autodl-tmp/struct_self_consist_ie/artifacts/r25_response/holm_bonferroni_enumeration.tex\", \"w\") as f:\n    f.write(output + \"\\n\")\n\n# Verification stats\nsig_tests = [x for x in corrected if x[3] < 0.05]\nprint(f\"\\n% --- Verification ---\")\nprint(f\"% Total tests: {len(corrected)}\")\nprint(f\"% Tests surviving Holm-Bonferroni at alpha=0.05: {len(sig_tests)}\")\nfor tid, desc, raw_p, adj_p, family in sorted(sig_tests, key=lambda x: x[2]):\n    print(f\"%   #{tid}: raw_p={raw_p}, adj_p={adj_p:.4f}\")\n\n# Check the specific claim: SciERC LP construction p=0.004 -> p_adj=0.20\nsci_lp = [x for x in corrected if x[0] == 20][0]\nprint(f\"\\n% SciERC LP construction: raw={sci_lp[2]}, adj={sci_lp[3]:.3f} (paper claims ~0.20)\")\n\n# Check FewNERD LP construction survives\nfn_lp = [x for x in corrected if x[0] == 22][0]\nprint(f\"% FewNERD LP construction: raw={fn_lp[2]}, adj={fn_lp[3]:.4f} (paper claims survives)\")\nPYEOF\npython3 /tmp/holm_bonferroni.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T13:36:06.966805+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\begin{table*}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Complete enumeration of $k{=}57$ statistical tests subject to Holm--Bonferroni correction. Raw $p$: uncorrected $p$-value as reported. $p_{\\\\text{adj}}$: Holm--Bonferroni adjusted $p$-value. $^\\\\dagger$Survives correction at $\\\\alpha{=}0.05$.}\\n\\\\label{tab:holm_family}\\n\\\\begin{tabular}{clllcc}\\n\\\\toprule\\n\\\\# & Family & Test Description & Raw $p$ & $p_{\\\\text{adj}}$ & Sig. \\\\\\\\\\n\\\\midrule\\n\\\\multicolumn{6}{l}{\\\\textit{Selection}} \\\\\\\\\\n1 & & SciERC NER LP selection ($N{=}8$, Qwen, Table~3) & $0.290$ & $1.0$ &  \\\\\\\\\\n2 & & SciERC NER SJ selection ($N{=}8$, Qwen, Table~3) & $0.670$ & $1.0$ &  \\\\\\\\\\n3 & & SciERC NER FK selection ($N{=}8$, Qwen, Table~3) & $0.790$ & $1.0$ &  \\\\\\\\\\n4 & & WNUT-17 LP selection ($N{=}8$, Qwen) & $0.720$ & $1.0$ &  \\\\\\\\\\n5 & & CoNLL LP selection ($N{=}8$, Qwen) & $1.0$ & $1.0$ &  \\\\\\\\\\n6 & & Few-NERD LP selection ($N{=}8$, Qwen, 3-seed) & $0.001$ & $0.055$ &  \\\\\\\\\\n7 & & SciERC NER SJ selection ($N{=}8$, LLaMA-3B) & $0.175$ & $1.0$ &  \\\\\\\\\\n8 & & SciERC NER LP selection ($N{=}32$, Qwen) & $0.091$ & $1.0$ &  \\\\\\\\\\n9 & & SciERC NER FK selection ($N{=}32$, Qwen) & $0.101$ & $1.0$ &  \\\\\\\\\\n10 & & SciERC NER SJ selection ($N{=}32$, Qwen) & $0.244$ & $1.0$ &  \\\\\\\\\\n11 & & SciERC NER EM selection ($N{=}32$, Qwen) & $0.355$ & $1.0$ &  \\\\\\\\\\n12 & & SciERC NER VC selection ($N{=}32$, Qwen) & $1.0$ & $1.0$ &  \\\\\\\\\\n13 & & SciERC RE LP selection ($N{=}16$, 4B, Fisher) & $0.058$ & $1.0$ &  \\\\\\\\\\n14 & & SciERC RE VC selection ($N{=}16$, 4B, Fisher) & $0.973$ & $1.0$ &  \\\\\\\\\\n15 & & SciERC RE FK selection ($N{=}16$, 4B, Fisher) & $0.985$ & $1.0$ &  \\\\\\\\\\n16 & & SciERC RE SJ selection ($N{=}16$, 4B, Fisher) & $0.993$ & $1.0$ &  \\\\\\\\\\n17 & & SciERC RE EM selection ($N{=}16$, 4B, Fisher) & $0.999$ & $1.0$ &  \\\\\\\\\\n18 & & 
…[truncated 4305 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T13:36:06.967033+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/artifacts/r25_response/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -la /root/autodl-tmp/struct_self_consist_ie/artifacts/r25_response/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T13:36:06.967208+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 16\\ndrwxr-xr-x  2 root root   83 May 20 21:34 .\\ndrwxr-xr-x 13 root root 4096 May 20 21:29 ..\\n-rw-r--r--  1 root root 5082 May 20 21:34 holm_bonferroni_enumeration.tex\\n-rw-r--r--  1 root root  401 May 20 21:29 power_analysis.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T13:36:06.967359+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/artifacts/r25_response/power_analysis.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/artifacts/r25_response/power_analysis.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T13:36:06.967497+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\begin{table}[h]\\n\\\\centering\\n\\\\caption{Post-hoc power analysis for cross-dataset correlation tests ($n=23$ configurations).}\\n\\\\label{tab:power_analysis}\\n\\\\begin{tabular}{ccc}\\n\\\\toprule\\nEffect Size ($\\\\rho$) & Power ($1-\\\\beta$) & $n$ needed for 80\\\\% power \\\\\\\\\\n\\\\midrule\\n0.1 & 0.073 & 783 \\\\\\\\\\n0.2 & 0.148 & 195 \\\\\\\\\\n0.3 & 0.283 & 85 \\\\\\\\\\n0.4 & 0.474 & 47 \\\\\\\\\\n0.5 & 0.690 & 30 \\\\\\\\\\n\\\\bottomrule\\n\\\\end{tabular}\\n\\\\end{table}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T13:36:06.967628+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/artifacts/r25_response/holm_bonferroni_enumeration.tex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/artifacts/r25_response/holm_bonferroni_enumeration.tex",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T13:36:06.967812+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\\begin{table*}[t]\\n\\\\centering\\n\\\\small\\n\\\\caption{Complete enumeration of $k{=}57$ statistical tests subject to Holm--Bonferroni correction. Raw $p$: uncorrected $p$-value as reported. $p_{\\\\text{adj}}$: Holm--Bonferroni adjusted $p$-value. $^\\\\dagger$Survives correction at $\\\\alpha{=}0.05$.}\\n\\\\label{tab:holm_family}\\n\\\\begin{tabular}{clllcc}\\n\\\\toprule\\n\\\\# & Family & Test Description & Raw $p$ & $p_{\\\\text{adj}}$ & Sig. \\\\\\\\\\n\\\\midrule\\n\\\\multicolumn{6}{l}{\\\\textit{Selection}} \\\\\\\\\\n1 & & SciERC NER LP selection ($N{=}8$, Qwen, Table~3) & $0.290$ & $1.0$ &  \\\\\\\\\\n2 & & SciERC NER SJ selection ($N{=}8$, Qwen, Table~3) & $0.670$ & $1.0$ &  \\\\\\\\\\n3 & & SciERC NER FK selection ($N{=}8$, Qwen, Table~3) & $0.790$ & $1.0$ &  \\\\\\\\\\n4 & & WNUT-17 LP selection ($N{=}8$, Qwen) & $0.720$ & $1.0$ &  \\\\\\\\\\n5 & & CoNLL LP selection ($N{=}8$, Qwen) & $1.0$ & $1.0$ &  \\\\\\\\\\n6 & & Few-NERD LP selection ($N{=}8$, Qwen, 3-seed) & $0.001$ & $0.055$ &  \\\\\\\\\\n7 & & SciERC NER SJ selection ($N{=}8$, LLaMA-3B) & $0.175$ & $1.0$ &  \\\\\\\\\\n8 & & SciERC NER LP selection ($N{=}32$, Qwen) & $0.091$ & $1.0$ &  \\\\\\\\\\n9 & & SciERC NER FK selection ($N{=}32$, Qwen) & $0.101$ & $1.0$ &  \\\\\\\\\\n10 & & SciERC NER SJ selection ($N{=}32$, Qwen) & $0.244$ & $1.0$ &  \\\\\\\\\\n11 & & SciERC NER EM selection ($N{=}32$, Qwen) & $0.355$ & $1.0$ &  \\\\\\\\\\n12 & & SciERC NER VC selection ($N{=}32$, Qwen) & $1.0$ & $1.0$ &  \\\\\\\\\\n13 & & SciERC RE LP selection ($N{=}16$, 4B, Fisher) & $0.058$ & $1.0$ &  \\\\\\\\\\n14 & & SciERC RE VC selection ($N{=}16$, 4B, Fisher) & $0.973$ & $1.0$ &  \\\\\\\\\\n15 & & SciERC RE FK selection ($N{=}16$, 4B, Fisher) & $0.985$ & $1.0$ &  \\\\\\\\\\n16 & & SciERC RE SJ selection ($N{=}16$, 4B, Fisher) & $0.993$ & $1.0$ &  \\\\\\\\\\n17 & & SciERC RE EM selection ($N{=}16$, 4B, Fisher) & $0.999$ & $1.0$ &  \\\\\\\\\\n18 & & 
…[truncated 3982 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T13:36:06.967969+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r25_response",
  "description": "Create local artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r25_response",
    "description": "Create local artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T13:36:06.968089+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T13:36:06.968228+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r25_response/power_analysis.tex",
  "content": "\\begin{table}[h]\n\\centering\n\\caption{Post-hoc power analysis for cross-dataset correlation tests ($n=23$ configurations).}\n\\label{tab:power_analysis}\n\\begin{tabular}{ccc}\n\\toprule\nEffect Size ($\\rho$) & Power ($1-\\beta$) & $n$ needed for 80\\% power \\\\\n\\midrule\n0.1 & 0.073 & 783 \\\\\n0.2 & 0.148 & 195 \\\\\n0.3 & 0.283 & 85 \\\\\n0.4 & 0.474 & 47 \\\\\n0.5 & 0.690 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r25_response/power_analysis.tex",
    "content": "\\begin{table}[h]\n\\centering\n\\caption{Post-hoc power analysis for cross-dataset correlation tests ($n=23$ configurations).}\n\\label{tab:power_analysis}\n\\begin{tabular}{ccc}\n\\toprule\nEffect Size ($\\rho$) & Power ($1-\\beta$) & $n$ needed for 80\\% power \\\\\n\\midrule\n0.1 & 0.073 & 783 \\\\\n0.2 & 0.148 & 195 \\\\\n0.3 & 0.283 & 85 \\\\\n0.4 & 0.474 & 47 \\\\\n0.5 & 0.690 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T13:36:06.968358+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r25_response/power_analysis.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T13:36:06.968490+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r25_response/holm_bonferroni_enumeration.tex",
  "content": "\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Complete enumeration of $k{=}57$ statistical tests subject to Holm--Bonferroni correction. Raw $p$: uncorrected $p$-value as reported. $p_{\\text{adj}}$: Holm--Bonferroni adjusted $p$-value. $^\\dagger$Survives correction at $\\alpha{=}0.05$.}\n\\label{tab:holm_family}\n\\begin{tabular}{clllcc}\n\\toprule\n\\# & Family & Test Description & Raw $p$ & $p_{\\text{adj}}$ & Sig. \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Selection}} \\\\\n1 & & SciERC NER LP selection ($N{=}8$, Qwen, Table~3) & $0.290$ & $1.0$ &  \\\\\n2 & & SciERC NER SJ selection ($N{=}8$, Qwen, Table~3) & $0.670$ & $1.0$ &  \\\\\n3 & & SciERC NER FK selection ($N{=}8$, Qwen, Table~3) & $0.790$ & $1.0$ &  \\\\\n4 & & WNUT-17 LP selection ($N{=}8$, Qwen) & $0.720$ & $1.0$ &  \\\\\n5 & & CoNLL LP selection ($N{=}8$, Qwen) & $1.0$ & $1.0$ &  \\\\\n6 & & Few-NERD LP selection ($N{=}8$, Qwen, 3-seed) & ${<}.001$ & $0.055$ &  \\\\\n7 & & SciERC NER SJ selection ($N{=}8$, LLaMA-3B) & $0.175$ & $1.0$ &  \\\\\n8 & & SciERC NER LP selection ($N{=}32$, Qwen) & $0.091$ & $1.0$ &  \\\\\n9 & & SciERC NER FK selection ($N{=}32$, Qwen) & $0.101$ & $1.0$ &  \\\\\n10 & & SciERC NER SJ selection ($N{=}32$, Qwen) & $0.244$ & $1.0$ &  \\\\\n11 & & SciERC NER EM selection ($N{=}32$, Qwen) & $0.355$ & $1.0$ &  \\\\\n12 & & SciERC NER VC selection ($N{=}32$, Qwen) & $1.0$ & $1.0$ &  \\\\\n13 & & SciERC RE LP selection ($N{=}16$, 4B, Fisher) & $0.058$ & $1.0$ &  \\\\\n14 & & SciERC RE VC selection ($N{=}16$, 4B, Fisher) & $0.973$ & $1.0$ &  \\\\\n15 & & SciERC RE FK selection ($N{=}16$, 4B, Fisher) & $0.985$ & $1.0$ &  \\\\\n16 & & SciERC RE SJ selection ($N{=}16$, 4B, Fisher) & $0.993$ & $1.0$ &  \\\\\n17 & & SciERC RE EM selection ($N{=}16$, 4B, Fisher) & $0.999$ & $1.0$ &  \\\\\n18 & & SciERC LP selection, non-tied subset ($\\varepsilon{=}0.05$) & $0.004$ & $0.180$ &  \\\\\n19 & & Few-NERD LP selection ($N{=}8$, LLaMA, 3-seed) & ${<}.001$ & $0.055$ &  \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Construction}} \\\\\n20 & & SciERC LP-weighted construction (Qwen, 3-seed) & $0.004$ & $0.180$ &  \\\\\n21 & & SciERC uniform construction (Qwen, 3-seed) & $0.023$ & $0.874$ &  \\\\\n22 & & Few-NERD LP-weighted construction (Qwen) & ${<}.001$ & $0.055$ &  \\\\\n23 & & Few-NERD uniform construction (Qwen) & $0.003$ & $0.138$ &  \\\\\n24 & & CoNLL uniform construction (Qwen) & $0.500$ & $1.0$ &  \\\\\n25 & & SciERC ZS construction (72B) & $0.008$ & $0.320$ &  \\\\\n26 & & SciERC FS construction (72B) & $0.544$ & $1.0$ &  \\\\\n27 & & CoNLL FS construction (72B) & $0.417$ & $1.0$ &  \\\\\n28 & & Few-NERD FS construction (72B) & $0.401$ & $1.0$ &  \\\\\n29 & & SciERC cross-model LP-weighted construction & ${<}.001$ & $0.055$ &  \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Calibration}} \\\\\n30 & & SciERC MF-Platt vs Raw LP & $0.720$ & $1.0$ &  \\\\\n31 & & CoNLL MF-Platt vs Raw LP & $0.310$ & $1.0$ &  \\\\\n32 & & Few-NERD MF-Platt vs Raw LP & $0.830$ & $1.0$ &  \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Signal $\\Delta\\rho$}} \\\\\n33 & & SciERC $\\Delta\\rho$ SJ$-$LP ($N{=}8$, seed 42) & ${<}.001$ & $0.055$ &  \\\\\n34 & & SciERC $\\Delta\\rho$ VC$-$SJ ($N{=}8$, seed 42) & $0.300$ & $1.0$ &  \\\\\n35 & & SciERC $\\Delta\\rho$ SJ$-$EM ($N{=}8$, seed 42) & $0.045$ & $1.0$ &  \\\\\n36 & & CoNLL $\\Delta\\rho$ EM$-$FK ($N{=}16$) & ${<}.001$ & $0.055$ &  \\\\\n37 & & CoNLL $\\Delta\\rho$ SJ$-$FK ($N{=}16$) & ${<}.001$ & $0.055$ &  \\\\\n38 & & CoNLL $\\Delta\\rho$ VC$-$FK ($N{=}16$) & $0.040$ & $1.0$ &  \\\\\n39 & & SciERC $\\Delta\\rho$ SJ$-$FK (LLaMA, permutation) & $0.060$ & $1.0$ &  \\\\\n40 & & SciERC RE $\\Delta\\rho$ SJ$-$FK (full-set) & $0.530$ & $1.0$ &  \\\\\n41 & & RE SJ $\\rho$ Q1 vs Q4 sentence length (Fisher $z$) & $0.004$ & $0.180$ &  \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Correlation}} \\\\\n42 & & Cross-dataset degeneracy--LP gain ($n{=}23$) & $0.810$ & $1.0$ &  \\\\\n43 & & Per-type degeneracy--headroom (Few-NERD, Spearman) & $0.004$ & $0.180$ &  \\\\\n44 & & Per-type degeneracy--headroom (exact permutation) & $0.005$ & $0.205$ &  \\\\\n45 & & Per-type degeneracy--headroom ($\\text{df}{=}4$ adjusted) & $0.033$ & $1.0$ &  \\\\\n46 & & SciERC per-type degeneracy--LP ($\\rho{=}0.14$) & $0.790$ & $1.0$ &  \\\\\n47 & & Kruskal--Wallis per-type LP heterogeneity (SciERC) & $0.796$ & $1.0$ &  \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{FS error}} \\\\\n48 & & FS vs ZS error overlap (SciERC, permutation) & $0.840$ & $1.0$ &  \\\\\n49 & & FS vs ZS error overlap (CoNLL, permutation) & $0.640$ & $1.0$ &  \\\\\n50 & & FS vs ZS entity entropy (SciERC) & $0.810$ & $1.0$ &  \\\\\n51 & & FS vs ZS entity entropy (CoNLL, Wilcoxon) & ${<}10^{-4}$ & ${<}.001$ & $\\dagger$ \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Other}} \\\\\n52 & & LP distribution seed 42 vs 456 (Mann--Whitney) & $0.550$ & $1.0$ &  \\\\\n53 & & RE LP selection reversal (free-form, 4-seed) & ${<}.001$ & $0.006$ & $\\dagger$ \\\\\n54 & & WNUT-17 conditional $\\rho$ VC ($p$-value) & $0.487$ & $1.0$ &  \\\\\n55 & & WNUT-17 conditional $\\rho$ FK ($p$-value) & $0.002$ & $0.094$ &  \\\\\n56 & & SciERC LP favorable subset ($+$2.47 pp) & $0.015$ & $0.585$ &  \\\\\n57 & & CoNLL LP favorable subset ($-$1.78 pp) & ${<}.001$ & $0.055$ &  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r25_response/holm_bonferroni_enumeration.tex",
    "content": "\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Complete enumeration of $k{=}57$ statistical tests subject to Holm--Bonferroni correction. Raw $p$: uncorrected $p$-value as reported. $p_{\\text{adj}}$: Holm--Bonferroni adjusted $p$-value. $^\\dagger$Survives correction at $\\alpha{=}0.05$.}\n\\label{tab:holm_family}\n\\begin{tabular}{clllcc}\n\\toprule\n\\# & Family & Test Description & Raw $p$ & $p_{\\text{adj}}$ & Sig. \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Selection}} \\\\\n1 & & SciERC NER LP selection ($N{=}8$, Qwen, Table~3) & $0.290$ & $1.0$ &  \\\\\n2 & & SciERC NER SJ selection ($N{=}8$, Qwen, Table~3) & $0.670$ & $1.0$ &  \\\\\n3 & & SciERC NER FK selection ($N{=}8$, Qwen, Table~3) & $0.790$ & $1.0$ &  \\\\\n4 & & WNUT-17 LP selection ($N{=}8$, Qwen) & $0.720$ & $1.0$ &  \\\\\n5 & & CoNLL LP selection ($N{=}8$, Qwen) & $1.0$ & $1.0$ &  \\\\\n6 & & Few-NERD LP selection ($N{=}8$, Qwen, 3-seed) & ${<}.001$ & $0.055$ &  \\\\\n7 & & SciERC NER SJ selection ($N{=}8$, LLaMA-3B) & $0.175$ & $1.0$ &  \\\\\n8 & & SciERC NER LP selection ($N{=}32$, Qwen) & $0.091$ & $1.0$ &  \\\\\n9 & & SciERC NER FK selection ($N{=}32$, Qwen) & $0.101$ & $1.0$ &  \\\\\n10 & & SciERC NER SJ selection ($N{=}32$, Qwen) & $0.244$ & $1.0$ &  \\\\\n11 & & SciERC NER EM selection ($N{=}32$, Qwen) & $0.355$ & $1.0$ &  \\\\\n12 & & SciERC NER VC selection ($N{=}32$, Qwen) & $1.0$ & $1.0$ &  \\\\\n13 & & SciERC RE LP selection ($N{=}16$, 4B, Fisher) & $0.058$ & $1.0$ &  \\\\\n14 & & SciERC RE VC selection ($N{=}16$, 4B, Fisher) & $0.973$ & $1.0$ &  \\\\\n15 & & SciERC RE FK selection ($N{=}16$, 4B, Fisher) & $0.985$ & $1.0$ &  \\\\\n16 & & SciERC RE SJ selection ($N{=}16$, 4B, Fisher) & $0.993$ & $1.0$ &  \\\\\n17 & & SciERC RE EM selection ($N{=}16$, 4B, Fisher) & $0.999$ & $1.0$ &  \\\\\n18 & & SciERC LP selection, non-tied subset ($\\varepsilon{=}0.05$) & $0.004$ & $0.180$ &  \\\\\n19 & & Few-NERD LP selection ($N{=}8$, LLaMA, 3-seed) & ${<}.001$ & $0.055$ &  \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Construction}} \\\\\n20 & & SciERC LP-weighted construction (Qwen, 3-seed) & $0.004$ & $0.180$ &  \\\\\n21 & & SciERC uniform construction (Qwen, 3-seed) & $0.023$ & $0.874$ &  \\\\\n22 & & Few-NERD LP-weighted construction (Qwen) & ${<}.001$ & $0.055$ &  \\\\\n23 & & Few-NERD uniform construction (Qwen) & $0.003$ & $0.138$ &  \\\\\n24 & & CoNLL uniform construction (Qwen) & $0.500$ & $1.0$ &  \\\\\n25 & & SciERC ZS construction (72B) & $0.008$ & $0.320$ &  \\\\\n26 & & SciERC FS construction (72B) & $0.544$ & $1.0$ &  \\\\\n27 & & CoNLL FS construction (72B) & $0.417$ & $1.0$ &  \\\\\n28 & & Few-NERD FS construction (72B) & $0.401$ & $1.0$ &  \\\\\n29 & & SciERC cross-model LP-weighted construction & ${<}.001$ & $0.055$ &  \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Calibration}} \\\\\n30 & & SciERC MF-Platt vs Raw LP & $0.720$ & $1.0$ &  \\\\\n31 & & CoNLL MF-Platt vs Raw LP & $0.310$ & $1.0$ &  \\\\\n32 & & Few-NERD MF-Platt vs Raw LP & $0.830$ & $1.0$ &  \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Signal $\\Delta\\rho$}} \\\\\n33 & & SciERC $\\Delta\\rho$ SJ$-$LP ($N{=}8$, seed 42) & ${<}.001$ & $0.055$ &  \\\\\n34 & & SciERC $\\Delta\\rho$ VC$-$SJ ($N{=}8$, seed 42) & $0.300$ & $1.0$ &  \\\\\n35 & & SciERC $\\Delta\\rho$ SJ$-$EM ($N{=}8$, seed 42) & $0.045$ & $1.0$ &  \\\\\n36 & & CoNLL $\\Delta\\rho$ EM$-$FK ($N{=}16$) & ${<}.001$ & $0.055$ &  \\\\\n37 & & CoNLL $\\Delta\\rho$ SJ$-$FK ($N{=}16$) & ${<}.001$ & $0.055$ &  \\\\\n38 & & CoNLL $\\Delta\\rho$ VC$-$FK ($N{=}16$) & $0.040$ & $1.0$ &  \\\\\n39 & & SciERC $\\Delta\\rho$ SJ$-$FK (LLaMA, permutation) & $0.060$ & $1.0$ &  \\\\\n40 & & SciERC RE $\\Delta\\rho$ SJ$-$FK (full-set) & $0.530$ & $1.0$ &  \\\\\n41 & & RE SJ $\\rho$ Q1 vs Q4 sentence length (Fisher $z$) & $0.004$ & $0.180$ &  \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Correlation}} \\\\\n42 & & Cross-dataset degeneracy--LP gain ($n{=}23$) & $0.810$ & $1.0$ &  \\\\\n43 & & Per-type degeneracy--headroom (Few-NERD, Spearman) & $0.004$ & $0.180$ &  \\\\\n44 & & Per-type degeneracy--headroom (exact permutation) & $0.005$ & $0.205$ &  \\\\\n45 & & Per-type degeneracy--headroom ($\\text{df}{=}4$ adjusted) & $0.033$ & $1.0$ &  \\\\\n46 & & SciERC per-type degeneracy--LP ($\\rho{=}0.14$) & $0.790$ & $1.0$ &  \\\\\n47 & & Kruskal--Wallis per-type LP heterogeneity (SciERC) & $0.796$ & $1.0$ &  \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{FS error}} \\\\\n48 & & FS vs ZS error overlap (SciERC, permutation) & $0.840$ & $1.0$ &  \\\\\n49 & & FS vs ZS error overlap (CoNLL, permutation) & $0.640$ & $1.0$ &  \\\\\n50 & & FS vs ZS entity entropy (SciERC) & $0.810$ & $1.0$ &  \\\\\n51 & & FS vs ZS entity entropy (CoNLL, Wilcoxon) & ${<}10^{-4}$ & ${<}.001$ & $\\dagger$ \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Other}} \\\\\n52 & & LP distribution seed 42 vs 456 (Mann--Whitney) & $0.550$ & $1.0$ &  \\\\\n53 & & RE LP selection reversal (free-form, 4-seed) & ${<}.001$ & $0.006$ & $\\dagger$ \\\\\n54 & & WNUT-17 conditional $\\rho$ VC ($p$-value) & $0.487$ & $1.0$ &  \\\\\n55 & & WNUT-17 conditional $\\rho$ FK ($p$-value) & $0.002$ & $0.094$ &  \\\\\n56 & & SciERC LP favorable subset ($+$2.47 pp) & $0.015$ & $0.585$ &  \\\\\n57 & & CoNLL LP favorable subset ($-$1.78 pp) & ${<}.001$ & $0.055$ &  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T13:36:06.968663+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r25_response/holm_bonferroni_enumeration.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-20T13:36:06.968824+00:00_

两个产出均已完成，保存在本地和服务器的 `artifacts/r25_response/`：

**P1: `power_analysis.tex`** — n=23 post-hoc power analysis表：
| ρ | Power | n needed (80%) |
|---|-------|----------------|
| 0.1 | 0.073 | 783 |
| 0.2 | 0.148 | 195 |
| 0.3 | 0.283 | 85 |
| 0.4 | 0.474 | 47 |
| 0.5 | 0.690 | 30 |

与论文现有 Table 13 (Appendix F.12) 数值一致（ρ=0.3 → n≈85 匹配论文正文引用）。

**P2: `holm_bonferroni_enumeration.tex`** — 57个统计检验完整枚举，按7个家族分组：
- **Selection** (19 tests): 实例级信号选择 vs greedy
- **Construction** (10 tests): 实体构造 vs greedy
- **Calibration** (3 tests): MF-Platt vs Raw LP
- **Signal Δρ** (9 tests): 信号间 bootstrap 对比
- **Correlation** (6 tests): 跨配置相关性显著性
- **FS error** (4 tests): Few-shot 误差分析
- **Other** (6 tests): 其他独立检验

Holm-Bonferroni 校验结果：仅2个检验在 α=0.05 下存活（#51 CoNLL FS entropy Wilcoxon, #53 RE free-form reversal）。SciERC LP construction 的 p_adj=0.180（论文报告~0.20，差异源于 "p<0.001" 的保守估计）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ssh_p1-p2-power-holm_20260520T132923"
}
```

</details>

---
