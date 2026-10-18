# analysis ner variance decomposition

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_analysis_ner-variance-decomposition_20260517T053347.jsonl`
- **Structured JSON:** [`d19d60fd44a4777dd60f.json`](../../sessions/d1/d19d60fd44a4777dd60f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-17T05:35:31.210529+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport numpy as np\n\ndata = {\n    2:  {'means': [0.5267, 0.4460, 0.5528], 'stds': [0.1905, 0.1984, 0.1402]},\n    6:  {'means': [0.3899, 0.4217, 0.4092], 'stds': [0.1153, 0.1341, 0.1197]},\n    12: {'means': [0.3057, 0.3568, 0.3051], 'stds': [0.1017, 0.1119, 0.1050]},\n    22: {'means': [0.2684, 0.2768, 0.2577], 'stds': [0.1029, 0.0905, 0.0922]},\n    44: {'means': [0.3007, 0.2724, 0.2898], 'stds': [0.1116, 0.1146, 0.1366]},\n    66: {'means': [0.4071, 0.4067, 0.4067], 'stds': [0.0017, 0.0014, 0.0016]},\n}\n\nprint(f'{'Count':>5} {'Batch SD':>10} {'Seed SD':>10} {'Ratio':>8}')\nprint('-' * 38)\nratios = []\nfor count, d in sorted(data.items()):\n    stds = np.array(d['stds'])\n    means = np.array(d['means'])\n    batch_var = np.mean(stds**2)\n    batch_sd = np.sqrt(batch_var)\n    seed_sd = np.std(means, ddof=1)\n    seed_var = seed_sd**2\n    ratio = batch_var / seed_var if seed_var > 0 else float('inf')\n    ratios.append(ratio)\n    print(f'{count:>5} {batch_sd:>10.4f} {seed_sd:>10.4f} {ratio:>8.1f}')\n\nprint()\nprint(f'Mean ratio: {np.mean(ratios):.1f}')\nprint(f'Range: {min(ratios):.1f} -- {max(ratios):.1f}')\n# Excluding count 66\nratios_no66 = ratios[:-1]\nprint(f'Mean ratio (excl. 66): {np.mean(ratios_no66):.1f}')\nprint(f'Range (excl. 66): {min(ratios_no66):.1f} -- {max(ratios_no66):.1f}')\n\"\n",
  "description": "Compute Few-NERD variance decomposition"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ner-variance-decomposition_20260517T053347",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport numpy as np\n\ndata = {\n    2:  {'means': [0.5267, 0.4460, 0.5528], 'stds': [0.1905, 0.1984, 0.1402]},\n    6:  {'means': [0.3899, 0.4217, 0.4092], 'stds': [0.1153, 0.1341, 0.1197]},\n    12: {'means': [0.3057, 0.3568, 0.3051], 'stds': [0.1017, 0.1119, 0.1050]},\n    22: {'means': [0.2684, 0.2768, 0.2577], 'stds': [0.1029, 0.0905, 0.0922]},\n    44: {'means': [0.3007, 0.2724, 0.2898], 'stds': [0.1116, 0.1146, 0.1366]},\n    66: {'means': [0.4071, 0.4067, 0.4067], 'stds': [0.0017, 0.0014, 0.0016]},\n}\n\nprint(f'{'Count':>5} {'Batch SD':>10} {'Seed SD':>10} {'Ratio':>8}')\nprint('-' * 38)\nratios = []\nfor count, d in sorted(data.items()):\n    stds = np.array(d['stds'])\n    means = np.array(d['means'])\n    batch_var = np.mean(stds**2)\n    batch_sd = np.sqrt(batch_var)\n    seed_sd = np.std(means, ddof=1)\n    seed_var = seed_sd**2\n    ratio = batch_var / seed_var if seed_var > 0 else float('inf')\n    ratios.append(ratio)\n    print(f'{count:>5} {batch_sd:>10.4f} {seed_sd:>10.4f} {ratio:>8.1f}')\n\nprint()\nprint(f'Mean ratio: {np.mean(ratios):.1f}')\nprint(f'Range: {min(ratios):.1f} -- {max(ratios):.1f}')\n# Excluding count 66\nratios_no66 = ratios[:-1]\nprint(f'Mean ratio (excl. 66): {np.mean(ratios_no66):.1f}')\nprint(f'Range (excl. 66): {min(ratios_no66):.1f} -- {max(ratios_no66):.1f}')\n\"\n",
    "description": "Compute Few-NERD variance decomposition"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T05:35:31.211373+00:00_

Count   Batch SD    Seed SD    Ratio
--------------------------------------
    2     0.1782     0.0557     10.2
    6     0.1233     0.0160     59.2
   12     0.1063     0.0297     12.8
   22     0.0954     0.0096     99.2
   44     0.1214     0.0143     72.4
   66     0.0016     0.0002     46.3

Mean ratio: 50.0
Range: 10.2 -- 99.2
Mean ratio (excl. 66): 50.8
Range (excl. 66): 10.2 -- 99.2

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ner-variance-decomposition_20260517T053347",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T05:35:31.211729+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
  "limit": "100",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ner-variance-decomposition_20260517T053347",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
    "limit": "100",
    "offset": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T05:35:31.212105+00:00_

0	\documentclass[11pt]{article}
1	
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{graphicx}
10	\usepackage{booktabs}
11	\usepackage{amsmath}
12	\usepackage{enumitem}
13	\usepackage[normalem]{ulem}
14	\usepackage{listings}
15	
16	\title{Supplementary Material for: Schema-Induced Degradation\\in Training-Free LLM Information Extraction}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\appendix
24	
25	\section{Additional Figures}
26	\label{sec:appendix_figures}
27	
28	\begin{table}[h]
29	\centering
30	\small
31	\begin{tabular}{lrr}
32	\toprule
33	\textbf{Count} & \textbf{Llama-3.1-8B} & \textbf{Qwen3-32B} \\
34	\midrule
35	1 & 0.702 & 0.640 \\
36	64 & 0.273 & 0.304 \\
37	\midrule
38	Decline & $-$43\,pp & $-$34\,pp \\
39	\bottomrule
40	\end{tabular}
41	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
42	\label{tab:cross_model}
43	\end{table}
44	
45	\begin{table}[h]
46	\centering
47	\small
48	\resizebox{\columnwidth}{!}{%
49	\begin{tabular}{crrrrrr}
50	\toprule
51	& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
52	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
53	\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
54	\midrule
55	8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
56	16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
57	\bottomrule
58	\end{tabular}}
59	\caption{Cross-model BCS-controlled FewRel accuracy.  
…[truncated 2675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ner-variance-decomposition_20260517T053347",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T05:35:31.212495+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "variance.decomposition|Cross-Seed Variance",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
  "output_mode": "content",
  "-n": "True",
  "-C": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ner-variance-decomposition_20260517T053347",
  "tool": "Grep",
  "tool_args": {
    "pattern": "variance.decomposition|Cross-Seed Variance",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
    "output_mode": "content",
    "-n": "True",
    "-C": "3"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T05:35:31.212946+00:00_

341-\section{Additional Experimental Details}
342-\label{sec:appendix_additional_details}
343-
344:\subsection{Cross-Seed Variance Decomposition}
345:\label{app:variance-decomposition}
346-
347-To quantify whether performance variability is driven by random batch composition or seed-dependent model inference noise, we decompose total variance into intra-seed (batch) and inter-seed components across three seeds (42, 123, 456), each evaluated on 25 random batches per count level.
348-
--
363-\bottomrule
364-\end{tabular}
365-\caption{Variance decomposition across count levels on FewRel. Batch SD is the root-mean intra-seed variance across 25 random type batches (averaged over 3 seeds). Seed SD is the standard deviation of the 3 per-seed means. Ratio = mean batch variance / seed variance. At count 80, only one batch composition exists (the full schema), so batch variance vanishes by construction.}
366:\label{tab:variance_decomposition}
367-\end{table}
368-
369-[Omitted long context line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ner-variance-decomposition_20260517T053347",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T05:35:31.213292+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
  "offset": "344",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ner-variance-decomposition_20260517T053347",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
    "offset": "344",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T05:35:31.213529+00:00_

344	\subsection{Cross-Seed Variance Decomposition}
345	\label{app:variance-decomposition}
346	
347	To quantify whether performance variability is driven by random batch composition or seed-dependent model inference noise, we decompose total variance into intra-seed (batch) and inter-seed components across three seeds (42, 123, 456), each evaluated on 25 random batches per count level.
348	
349	\begin{table}[h]
350	\centering
351	\small
352	\begin{tabular}{rrrr}
353	\toprule
354	\textbf{Count} & \textbf{Batch SD} & \textbf{Seed SD} & \textbf{Ratio} \\
355	\midrule
356	4 & 0.0889 & 0.0122 & 53.5 \\
357	8 & 0.0820 & 0.0098 & 70.0 \\
358	16 & 0.0626 & 0.0270 & 5.4 \\
359	32 & 0.0462 & 0.0091 & 26.0 \\
360	40 & 0.0421 & 0.0019 & 474.4 \\
361	64 & 0.0245 & 0.0022 & 119.8 \\
362	80 & 0.0001 & 0.0088 & $<$0.1 \\
363	\bottomrule
364	\end{tabular}
365	\caption{Variance decomposition across count levels on FewRel. Batch SD is the root-mean intra-seed variance across 25 random type batches (averaged over 3 seeds). Seed SD is the standard deviation of the 3 per-seed means. Ratio = mean batch variance / seed variance. At count 80, only one batch composition exists (the full schema), so batch variance vanishes by construction.}
366	\label{tab:variance_decomposition}
367	\end{table}
368	
369	Intra-batch variance dominates inter-seed variance by 5--474$\times$ across count levels 4--64 (mean 125$\times$), confirming that random batch composition is the primary source of performance variability, not seed-dependent randomness in model inference. The wide ratio range reflects variation in how tightly seed means cluster at each count level; even the minimum ratio (5.4$\times$ at count 16) indicates batch composition contributes the majority of observed variance. At count 80, the ratio inverts because the full schema admits only one batch composition, leaving model inference noise as the sole variance source (seed SD = 0.88\,pp).
370	
371	\subsection{Per-Count-Level Statistics}
372	\labe
…[truncated 358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ner-variance-decomposition_20260517T053347",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T05:35:31.213750+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
  "old_string": "Intra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$), confirming that random batch composition is the primary source of performance variability, not seed-dependent randomness in model inference. The wide ratio range reflects variation in how tightly seed means cluster at each count level; even the minimum ratio (5.4$\\times$ at count 16) indicates batch composition contributes the majority of observed variance. At count 80, the ratio inverts because the full schema admits only one batch composition, leaving model inference noise as the sole variance source (seed SD = 0.88\\,pp).",
  "new_string": "\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n2 & 0.1782 & 0.0557 & 10.2 \\\\\n6 & 0.1233 & 0.0160 & 59.2 \\\\\n12 & 0.1063 & 0.0297 & 12.8 \\\\\n22 & 0.0954 & 0.0096 & 99.2 \\\\\n44 & 0.1214 & 0.0143 & 72.4 \\\\\n66 & 0.0016 & 0.0002 & 46.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on Few-NERD (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed standard deviation averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 66 (full schema), only one composition exists, so both components collapse to near-zero.}\n\\label{tab:variance_decomposition_ner}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ on FewRel (mean 125$\\times$, counts 4--64) and 10--99$\\times$ on Few-NERD (mean 51$\\times$, counts 2--44), confirming that random batch composition is the primary source of performance variability on both tasks, not seed-dependent randomness in model inference. The wide ratio range reflects variation in how tightly seed means cluster at each count level; even the minimum ratio (5.4$\\times$ on FewRel at count 16, 10.2$\\times$ on Few-NERD at count 2) indicates batch composition contributes the majority of observed variance. At count 80 (FewRel) and count 66 (Few-NERD), the full schema admits only one batch composition, collapsing batch variance by construction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ner-variance-decomposition_20260517T053347",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
    "old_string": "Intra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$), confirming that random batch composition is the primary source of performance variability, not seed-dependent randomness in model inference. The wide ratio range reflects variation in how tightly seed means cluster at each count level; even the minimum ratio (5.4$\\times$ at count 16) indicates batch composition contributes the majority of observed variance. At count 80, the ratio inverts because the full schema admits only one batch composition, leaving model inference noise as the sole variance source (seed SD = 0.88\\,pp).",
    "new_string": "\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n2 & 0.1782 & 0.0557 & 10.2 \\\\\n6 & 0.1233 & 0.0160 & 59.2 \\\\\n12 & 0.1063 & 0.0297 & 12.8 \\\\\n22 & 0.0954 & 0.0096 & 99.2 \\\\\n44 & 0.1214 & 0.0143 & 72.4 \\\\\n66 & 0.0016 & 0.0002 & 46.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Variance decomposition on Few-NERD (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed standard deviation averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 66 (full schema), only one composition exists, so both components collapse to near-zero.}\n\\label{tab:variance_decomposition_ner}\n\\end{table}\n\nIntra-batch variance dominates inter-seed variance by 5--474$\\times$ on FewRel (mean 125$\\times$, counts 4--64) and 10--99$\\times$ on Few-NERD (mean 51$\\times$, counts 2--44), confirming that random batch composition is the primary source of performance variability on both tasks, not seed-dependent randomness in model inference. The wide ratio range reflects variation in how tightly seed means cluster at each count level; even the minimum ratio (5.4$\\times$ on FewRel at count 16, 10.2$\\times$ on Few-NERD at count 2) indicates batch composition contributes the majority of observed variance. At count 80 (FewRel) and count 66 (Few-NERD), the full schema admits only one batch composition, collapsing batch variance by construction."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T05:35:31.214166+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ner-variance-decomposition_20260517T053347",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T05:35:31.214402+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && latexmk -pdf -interaction=nonstopmode -g supplementary.tex 2>&1 | tail -5",
  "description": "Compile supplementary.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_ner-variance-decomposition_20260517T053347",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && latexmk -pdf -interaction=nonstopmode -g supplementary.tex 2>&1 | tail -5",
    "description": "Compile supplementary.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T05:35:31.214606+00:00_

  Reference `sec:centrality_confound' on page 2 undefined on input line 153
  Reference `tab:pairwise' on page 3 undefined on input line 189
 And 15 more --- see log file 'supplementary.log'
Latexmk: All targets (supplementary.pdf) are up-to-date

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_ner-variance-decomposition_20260517T053347",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-17T05:35:31.214868+00:00_

编译成功（warnings 仅为跨文件 reference，正常）。

**Few-NERD Variance Decomposition:**

| Count | Batch SD | Seed SD | Ratio |
|------:|--------:|--------:|------:|
| 2 | 0.1782 | 0.0557 | 10.2 |
| 6 | 0.1233 | 0.0160 | 59.2 |
| 12 | 0.1063 | 0.0297 | 12.8 |
| 22 | 0.0954 | 0.0096 | 99.2 |
| 44 | 0.1214 | 0.0143 | 72.4 |
| 66 | 0.0016 | 0.0002 | 46.3 |

**Mean ratio (counts 2--44):** 50.8x  
**Range:** 10.2--99.2x  
**编译:** 成功，PDF 已生成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_ner-variance-decomposition_20260517T053347"
}
```

</details>

---
