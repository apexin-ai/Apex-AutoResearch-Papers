# paper mistral footnote fix

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_paper_mistral_footnote_fix_20260514T213232.jsonl`
- **Structured JSON:** [`3a0674c22f02eea09328.json`](../../sessions/3a/3a0674c22f02eea09328.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-14T21:33:03.513182+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
  "offset": "25",
  "limit": "35"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_mistral_footnote_fix_20260514T213232",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
    "offset": "25",
    "limit": "35"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T21:33:03.513923+00:00_

25	
26	The remaining three architectures fill out the diagnostic picture.
27	Llama-3.1-8B shows moderate concentration ($0.34$) with a spike-like shape ($t_1/t_5{=}0.71$, $t_1/t_2{=}21.7$); its allocation benefit is marginal ($+$0.36 vs.\ $+$0.38 uniform). %exp_id=llama_hires_constrained
28	Mistral-7B-v0.3 and Gemma-2-9B both exhibit flat distributions ($t_1/t_5{=}0.18$) with low concentration ($0.22$ and $0.23$ respectively), leaving the profiler with no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\ $+$0.10 for Mistral; $+$0.15 vs.\ $+$0.13 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline
29	
30	\begin{table}[t]
31	\centering
32	\small
33	\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at $4\times$ compression. $t_1/t_5$: ratio of top-1 to top-5 per-head 2-bit distortion (low${=}$spread, high${=}$spike). $^\dagger$Hires profiling (64 seq $\times$ 2048 tok); $^\ddagger$standard profiling, hires pending.}
34	\label{tab:heterogeneity}
35	\begin{tabular}{lcccccc}
36	\toprule
37	Model & GQA & Top-5\% & $t_1/t_5$ & $\Delta$ PPL & $\Delta$ PPL & Shape \\
38	 & Ratio & Conc. & & (Uniform) & (Ours) & \\
39	\midrule
40	Qwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.42 & Spread \\
41	Yi-1.5-9B$^\dagger$ & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\
42	Llama-3.1-8B$^\ddagger$ & 4:1 & 0.34 & 0.71 & $+$0.38 & $+$0.36 & Spike \\
43	Mistral-7B-v0.3$^\ddagger$ & 4:1 & 0.22 & 0.18 & $+$0.10 & $+$0.13 & Flat \\
44	Gemma-2-9B$^\ddagger$ & 2:1 & 0.23 & 0.18 & $+$0.13 & $+$0.15 & Flat \\
45	\bottomrule
46	\end{tabular}
47	\end{table}
48	
49	\begin{figure*}[t]
50	\centering
51	\includegraphics[width=\textwidth]{figures/fig1_head_delta_heatmap.pdf}
52	\caption{Per-head 2-bit quantization sensitivity across five architectures. Qwen2.5-7B shows high concentration in Layer-0 heads (``spread'' pattern); Yi-1.5-9B shows a single extreme outlier at Layer-4 Head-3 (``sp
…[truncated 899 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_mistral_footnote_fix_20260514T213232",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T21:33:03.514236+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Mistral.*ddagger",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_mistral_footnote_fix_20260514T213232",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Mistral.*ddagger",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T21:33:03.514488+00:00_

docs/paper/analysis.tex:43:Mistral-7B-v0.3$^\ddagger$ & 4:1 & 0.22 & 0.18 & $+$0.10 & $+$0.13 & Flat \\
docs/paper/experiments.tex:52:Mistral-7B-v0.3 & 7.04  & 7.13  & ---   & ---   & 7.16$^{\dagger\ddagger}$ \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_mistral_footnote_fix_20260514T213232",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T21:33:03.514720+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "ddagger",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_mistral_footnote_fix_20260514T213232",
  "tool": "Grep",
  "tool_args": {
    "pattern": "ddagger",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T21:33:03.514924+00:00_

docs/paper/analysis.tex:33:\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at $4\times$ compression. $t_1/t_5$: ratio of top-1 to top-5 per-head 2-bit distortion (low${=}$spread, high${=}$spike). $^\dagger$Hires profiling (64 seq $\times$ 2048 tok); $^\ddagger$standard profiling, hires pending.}
docs/paper/analysis.tex:42:Llama-3.1-8B$^\ddagger$ & 4:1 & 0.34 & 0.71 & $+$0.38 & $+$0.36 & Spike \\
docs/paper/analysis.tex:43:Mistral-7B-v0.3$^\ddagger$ & 4:1 & 0.22 & 0.18 & $+$0.10 & $+$0.13 & Flat \\
docs/paper/analysis.tex:44:Gemma-2-9B$^\ddagger$ & 2:1 & 0.23 & 0.18 & $+$0.13 & $+$0.15 & Flat \\
docs/paper/experiments.tex:43:[Omitted long matching line]
docs/paper/experiments.tex:52:Mistral-7B-v0.3 & 7.04  & 7.13  & ---   & ---   & 7.16$^{\dagger\ddagger}$ \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_mistral_footnote_fix_20260514T213232",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T21:33:03.517223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "offset": "35",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_mistral_footnote_fix_20260514T213232",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
    "offset": "35",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T21:33:03.517490+00:00_

35	and (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.
36	
37	\subsection{Main Results}
38	\label{sec:main_results}
39	
40	\begin{table}[t]
41	\centering
42	\small
43	\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained allocation fails catastrophically on $\{2,4,8,16\}$; our cardinality constraint restores performance. Best constrained result per model in \textbf{bold}. $^\dagger$Hires profiling (64 seq $\times$ 2048 tok); standard profiling does not improve over uniform on these architectures. $^\ddagger$Best $k$ from ablation ($k{=}4$). The $\pm$0.06 on Qwen reports std over 3 calibration seeds (hires profiling); bit distributions are identical across seeds.}
44	\label{tab:main_results}
45	\begin{tabular}{lcccccc}
46	\toprule
47	Model & Baseline & Uniform & \multicolumn{2}{c}{Unconstrained} & Ours \\
48	 & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\
49	\midrule
50	Qwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \textbf{11.23}$\pm$0.06 \\
51	Llama-3.1-8B    & 8.09  & 8.47  & ---   & ---   & \textbf{8.45}$^\dagger$ \\
52	Mistral-7B-v0.3 & 7.04  & 7.13  & ---   & ---   & 7.16$^{\dagger\ddagger}$ \\
53	Yi-1.5-9B$^\dagger$       & 7.02  & 7.22  & ---   & ---   & 7.22 \\
54	Gemma-2-9B      & 8.90  & 9.03  & ---   & ---   & 9.05 \\
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	Table~\ref{tab:main_results} summarizes the main results.
60	On Qwen2.5-7B, constrained MCKP achieves 11.23 PPL, a 27.3\% reduction over uniform 4-bit (15.45).
61	Higher-resolution profiling (64 seq $\times$ 2048 tok) further improves this to 10.91; we report the standard-profiling result here and analyze the effect of profiling resolution in Appendix~\ref{sec:profiling_resolution}.
62	Without the cardinality constraint, both greedy (32.45) and MCKP (36.92) perform \emph{worse} than uniform---a catastrophic failure caused by excessive 2-bit assignments that compound across layers.
63	The constraint elimin
…[truncated 222 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_mistral_footnote_fix_20260514T213232",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T21:33:03.518200+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
  "old_string": "Mistral-7B-v0.3$^\\ddagger$ & 4:1 & 0.22 & 0.18 & $+$0.10 & $+$0.13 & Flat \\\\",
  "new_string": "Mistral-7B-v0.3$^\\dagger$ & 4:1 & 0.22 & 0.18 & $+$0.10 & $+$0.13 & Flat \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_mistral_footnote_fix_20260514T213232",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
    "old_string": "Mistral-7B-v0.3$^\\ddagger$ & 4:1 & 0.22 & 0.18 & $+$0.10 & $+$0.13 & Flat \\\\",
    "new_string": "Mistral-7B-v0.3$^\\dagger$ & 4:1 & 0.22 & 0.18 & $+$0.10 & $+$0.13 & Flat \\\\"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T21:33:03.518449+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_mistral_footnote_fix_20260514T213232",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-14T21:33:03.518694+00:00_

Done. Summary:

- **analysis.tex L43**: Changed Mistral footnote from `$^\ddagger$` (standard profiling) to `$^\dagger$` (hires profiling).
- **analysis.tex caption**: `$^\ddagger$` definition kept — Llama and Gemma still use it.
- **experiments.tex L52**: No change needed — `$^{\dagger\ddagger}$` there means hires profiling (`†`) + best $k$ from ablation (`‡`), which are different footnotes with different definitions in that table's caption. Both are correct.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_mistral_footnote_fix_20260514T213232"
}
```

</details>

---
