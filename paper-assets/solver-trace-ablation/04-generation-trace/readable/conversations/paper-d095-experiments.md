# paper d095 experiments

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_paper_d095-experiments_20260515T195541.jsonl`
- **Structured JSON:** [`5743e703125de61ec8d9.json`](../../sessions/57/5743e703125de61ec8d9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-15T19:59:14.201913+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T19:59:14.202817+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits meta-level Goodhart's Law (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}8$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with NLL on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
10	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}---legacy filename, no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so training-log ISR is never compared across runs.
11	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the eight cataloged patterns, a necessary but not sufficient condition for semantic correctness.
12	
13	\subsection{ISR as Diagnostic}
14	\label{sec:diagnostic}
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
19	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$93\%$\to$96\% while proved-only ISR falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps. By step 1000, 94.8\% of proved samples hav
…[truncated 16883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T19:59:14.203281+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "\tRandom & 0.1 & \\textbf{85}{\\scriptsize$\\pm$6} & 0.086{\\scriptsize$\\pm$.04} & 0 & 81 & 18 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r2/s44",
  "new_string": "\tRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "old_string": "\tRandom & 0.1 & \\textbf{85}{\\scriptsize$\\pm$6} & 0.086{\\scriptsize$\\pm$.04} & 0 & 81 & 18 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r2/s44",
    "new_string": "\tRandom & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T19:59:14.203554+00:00_

&lt;tool_use_error>String to replace not found in file.
String: 	Random & 0.1 & \textbf{85}{\scriptsize$\pm$6} & 0.086{\scriptsize$\pm$.04} & 0 & 81 & 18 \\ %% registry: plan018-additive-random-b01-s42/s43-r2/s44&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T19:59:14.203834+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": "55",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "offset": "55",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T19:59:14.204075+00:00_

55	\midrule
56	Exec-only$^\dagger$ & --- & 93 & 0.132 & 0 & 87 & 8 \\ %% registry: plan001-exec-only-s42-r2 (H8 corrected)
57	ISR & 0.1 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{70}$^\P$ & 18 & 7 \\ %% registry: plan002-additive-b01-s42/s43/s44 (pooled, H8+FN corrected)
58	Random & 0.1 & \textbf{85}{\scriptsize$\pm$6} & 0.086{\scriptsize$\pm$.04} & 0 & 81 & 18 \\ %% registry: plan018-additive-random-b01-s42/s43-r2/s44
59	\midrule
60	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 14 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled)
61	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)
62	\bottomrule
63	\end{tabular}}
64	\caption{Goodhart landscape across reward conditions. 3-seed rows: H7/H1/N-H pooled across seeds; PR/ISR$^*$: mean$\pm$std of per-seed values. $^\dagger$Seed~42. $\ddagger$$\text{ISR}^*$ omitted for ISR $\beta{=}0.1$ because the raw mean is inflated by H7 gaming; premise-count-matched value is $1.06\times$ random (\S\ref{sec:goodhart}, Appendix~\ref{app:detailed-results}). $^\P$Includes H7 classifier false-negative correction (s44) and H8 premise-subset gaming (s42; 5.2\% of proved; Appendix~\ref{app:h8}). Per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}.}
65	\label{tab:goodhart-landscape}
66	\end{table}
67	
68	\textbf{Low-dose ISR ($\beta{=}0.1$): ISR-specific gaming.}
69	The most striking number at 500 steps is H7: 69.7\% of proved samples under ISR ($n{=}161/231$) vs.\ \emph{zero} under random ($0/256$); however, extended training to 1000 steps reveals random $\beta{=}0.1$ converges to $100\%$ H7 (seed~42), indicating ISR accelerates H7 onset rather than being its sole cause. %% registry: plan002 vs plan018 all seeds

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T19:59:14.204315+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat -A /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex | sed -n '58p'",
  "description": "Show exact characters on line 58"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Bash",
  "tool_args": {
    "command": "cat -A /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex | sed -n '58p'",
    "description": "Show exact characters on line 58"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T19:59:14.204518+00:00_

Random & 0.1 & \textbf{85}{\scriptsize$\pm$6} & 0.086{\scriptsize$\pm$.04} & 0 & 81 & 18 \\ %% registry: plan018-additive-random-b01-s42/s43-r2/s44$

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T19:59:14.204819+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "Random & 0.1 & \\textbf{85}{\\scriptsize$\\pm$6} & 0.086{\\scriptsize$\\pm$.04} & 0 & 81 & 18 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r2/s44",
  "new_string": "Random & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "old_string": "Random & 0.1 & \\textbf{85}{\\scriptsize$\\pm$6} & 0.086{\\scriptsize$\\pm$.04} & 0 & 81 & 18 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r2/s44",
    "new_string": "Random & 0.1 & \\textbf{87}{\\scriptsize$\\pm$8} & 0.117{\\scriptsize$\\pm$.04} & 14$^\\S$ & 71 & 10 \\\\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T19:59:14.205206+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T19:59:14.205491+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "ISR & 0.1 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{70}$^\\P$ & 18 & 7 \\\\ %% registry: plan002-additive-b01-s42/s43/s44 (pooled, H8+FN corrected)",
  "new_string": "ISR & 0.1 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "old_string": "ISR & 0.1 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{70}$^\\P$ & 18 & 7 \\\\ %% registry: plan002-additive-b01-s42/s43/s44 (pooled, H8+FN corrected)",
    "new_string": "ISR & 0.1 & 77{\\scriptsize$\\pm$14} & $\\ddagger$ & \\textbf{71}$^\\P$ & 18 & 6 \\\\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T19:59:14.205900+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T19:59:14.206200+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "\\caption{Goodhart landscape across reward conditions. 3-seed rows: H7/H1/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std of per-seed values. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ omitted for ISR $\\beta{=}0.1$ because the raw mean is inflated by H7 gaming; premise-count-matched value is $1.06\\times$ random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}). $^\\P$Includes H7 classifier false-negative correction (s44) and H8 premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}.}",
  "new_string": "\\caption{Goodhart landscape across reward conditions. 3-seed rows: H7/H1/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std of per-seed values. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ omitted for ISR $\\beta{=}0.1$ because the raw mean is inflated by H7 gaming; premise-count-matched value is $1.06\\times$ random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}). $^\\P$Includes H7 classifier false-negative correction (s44) and H8 premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random H7 driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "old_string": "\\caption{Goodhart landscape across reward conditions. 3-seed rows: H7/H1/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std of per-seed values. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ omitted for ISR $\\beta{=}0.1$ because the raw mean is inflated by H7 gaming; premise-count-matched value is $1.06\\times$ random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}). $^\\P$Includes H7 classifier false-negative correction (s44) and H8 premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}.}",
    "new_string": "\\caption{Goodhart landscape across reward conditions. 3-seed rows: H7/H1/N-H pooled across seeds; PR/ISR$^*$: mean$\\pm$std of per-seed values. $^\\dagger$Seed~42. $\\ddagger$$\\text{ISR}^*$ omitted for ISR $\\beta{=}0.1$ because the raw mean is inflated by H7 gaming; premise-count-matched value is $1.06\\times$ random (\\S\\ref{sec:goodhart}, Appendix~\\ref{app:detailed-results}). $^\\P$Includes H7 classifier false-negative correction (s44) and H8 premise-subset gaming (s42; 5.2\\% of proved; Appendix~\\ref{app:h8}). $^\\S$Random H7 driven by seed~43 (38.3\\%); seeds~42 and~44: 0\\%. Per-seed breakdown in Appendix Table~\\ref{tab:fol-detailed}.}"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T19:59:14.206597+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T19:59:14.206923+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "\\textbf{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nThe most striking number at 500 steps is H7: 69.7\\% of proved samples under ISR ($n{=}161/231$) vs.\\ \\emph{zero} under random ($0/256$); however, extended training to 1000 steps reveals random $\\beta{=}0.1$ converges to $100\\%$ H7 (seed~42), indicating ISR accelerates H7 onset rather than being its sole cause. %% registry: plan002 vs plan018 all seeds\nH7---a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by construction (\\S\\ref{sec:taxonomy-method})---is the canonical meta-level Goodhart move: the model satisfies the LOO definition directly rather than producing a derivation that happens to satisfy it.\nTotal conclusion embedding ($\\text{H1}+\\text{H7}$) is GRPO-universal at $68$--$100\\%$ across both conditions, and is in fact \\emph{higher} under random (pooled H1 81\\% vs.\\ 18\\% under ISR).\nISR does not reduce hacking; it converts H1 into H7 (Figure~\\ref{fig:hacking-composition}).\nRandom also yields higher and more stable PR ($85{\\pm}6\\%$ vs.\\ $77{\\pm}14\\%$).",
  "new_string": "\\textbf{Low-dose ISR ($\\beta{=}0.1$): ISR-amplified gaming.}\nH7 tautological collapse occurs under both ISR and random conditions, but ISR amplifies it ${\\sim}5\\times$: $70.6\\%$ ($163/231$) under ISR vs.\\ $13.7\\%$ ($36/262$) under random (Fisher $p{=}1.3{\\times}10^{-39}$, $\\text{OR}{=}15.05$). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nRandom H7 is highly seed-dependent: $38.3\\%$ in seed~43 vs.\\ $0\\%$ in seeds~42 and~44; ISR makes H7 near-deterministic ($2/3$ seeds at $97$--$100\\%$, Table~\\ref{tab:fol-detailed}).\nH7---a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by construction (\\S\\ref{sec:taxonomy-method})---is the canonical meta-level Goodhart move: the model satisfies the LOO definition directly rather than producing a derivation that happens to satisfy it.\nTotal conclusion embedding ($\\text{H1}+\\text{H7}$) is GRPO-universal at $68$--$100\\%$ across both conditions, and is in fact \\emph{higher} under random (pooled H1 $71\\%$ vs.\\ $18\\%$ under ISR).\nISR does not reduce hacking; it converts H1 into H7 (Figure~\\ref{fig:hacking-composition}).\nRandom also yields higher and more stable PR ($87{\\pm}8\\%$ vs.\\ $77{\\pm}14\\%$)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "old_string": "\\textbf{Low-dose ISR ($\\beta{=}0.1$): ISR-specific gaming.}\nThe most striking number at 500 steps is H7: 69.7\\% of proved samples under ISR ($n{=}161/231$) vs.\\ \\emph{zero} under random ($0/256$); however, extended training to 1000 steps reveals random $\\beta{=}0.1$ converges to $100\\%$ H7 (seed~42), indicating ISR accelerates H7 onset rather than being its sole cause. %% registry: plan002 vs plan018 all seeds\nH7---a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by construction (\\S\\ref{sec:taxonomy-method})---is the canonical meta-level Goodhart move: the model satisfies the LOO definition directly rather than producing a derivation that happens to satisfy it.\nTotal conclusion embedding ($\\text{H1}+\\text{H7}$) is GRPO-universal at $68$--$100\\%$ across both conditions, and is in fact \\emph{higher} under random (pooled H1 81\\% vs.\\ 18\\% under ISR).\nISR does not reduce hacking; it converts H1 into H7 (Figure~\\ref{fig:hacking-composition}).\nRandom also yields higher and more stable PR ($85{\\pm}6\\%$ vs.\\ $77{\\pm}14\\%$).",
    "new_string": "\\textbf{Low-dose ISR ($\\beta{=}0.1$): ISR-amplified gaming.}\nH7 tautological collapse occurs under both ISR and random conditions, but ISR amplifies it ${\\sim}5\\times$: $70.6\\%$ ($163/231$) under ISR vs.\\ $13.7\\%$ ($36/262$) under random (Fisher $p{=}1.3{\\times}10^{-39}$, $\\text{OR}{=}15.05$). %% registry: plan002 vs plan018 all seeds; D095 FINAL\nRandom H7 is highly seed-dependent: $38.3\\%$ in seed~43 vs.\\ $0\\%$ in seeds~42 and~44; ISR makes H7 near-deterministic ($2/3$ seeds at $97$--$100\\%$, Table~\\ref{tab:fol-detailed}).\nH7---a single premise identical to the conclusion, giving $\\text{ISR}\\geq 0.5$ by construction (\\S\\ref{sec:taxonomy-method})---is the canonical meta-level Goodhart move: the model satisfies the LOO definition directly rather than producing a derivation that happens to satisfy it.\nTotal conclusion embedding ($\\text{H1}+\\text{H7}$) is GRPO-universal at $68$--$100\\%$ across both conditions, and is in fact \\emph{higher} under random (pooled H1 $71\\%$ vs.\\ $18\\%$ under ISR).\nISR does not reduce hacking; it converts H1 into H7 (Figure~\\ref{fig:hacking-composition}).\nRandom also yields higher and more stable PR ($87{\\pm}8\\%$ vs.\\ $77{\\pm}14\\%$)."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T19:59:14.207322+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T19:59:14.207594+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "After reclassifying premise-subset gaming (H8; Appendix~\\ref{app:h8}) and correcting H7 classifier false negatives (s44, $n{=}12$; Appendix~\\ref{app:h4}), ISR $\\beta{=}0.1$ genuine rate is \\emph{significantly lower} than random ($6.9\\%$ vs.\\ $18.4\\%$; Fisher $p{=}0.0002$, two-sided; $n{=}231$ vs.\\ $256$; Appendix Table~\\ref{tab:bootstrap-ci}).\nEven a conservative correction (H8 reclassification only, no FN fix) yields $p{=}0.060$---marginal but directionally consistent.\nISR-specific gaming modes (H7 + H8) crowd out genuine proofs: the structural signal provides no quality benefit and actively \\emph{reduces} genuine output by creating optimization targets that are easier to satisfy than real derivations.\nThe raw $3.2\\times$ ISR$^*$ headline collapses once the LOO bias is controlled---a methodological lesson for any LOO-based metric on variable-length outputs. %% artifact: wilson_ci_complete, h8_reclassification",
  "new_string": "After reclassifying premise-subset gaming (H8; Appendix~\\ref{app:h8}) and correcting H7 classifier false negatives (s44, $n{=}12$; Appendix~\\ref{app:h4}), ISR $\\beta{=}0.1$ non-hacking rate ($6.1\\%$, $14/231$) is numerically lower than random ($9.5\\%$, $25/262$), but the difference is not statistically significant (Fisher $p{=}0.182$, two-sided, n.s.; Wilson 95\\% CI: ISR $[3.6\\%, 9.9\\%]$, Random $[6.5\\%, 13.7\\%]$; Appendix Table~\\ref{tab:bootstrap-ci}). %% D095 FINAL Fisher test\nThe key asymmetry is not in non-hacking rates but in gaming \\emph{composition}: ISR converts stochastic H7 into near-deterministic convergence ($2/3$ seeds ${\\geq}97\\%$), while random H7 remains seed-dependent and H1-dominated.\nThe raw $3.2\\times$ ISR$^*$ headline collapses once the LOO bias is controlled---a methodological lesson for any LOO-based metric on variable-length outputs. %% artifact: wilson_ci_complete, h8_reclassification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "old_string": "After reclassifying premise-subset gaming (H8; Appendix~\\ref{app:h8}) and correcting H7 classifier false negatives (s44, $n{=}12$; Appendix~\\ref{app:h4}), ISR $\\beta{=}0.1$ genuine rate is \\emph{significantly lower} than random ($6.9\\%$ vs.\\ $18.4\\%$; Fisher $p{=}0.0002$, two-sided; $n{=}231$ vs.\\ $256$; Appendix Table~\\ref{tab:bootstrap-ci}).\nEven a conservative correction (H8 reclassification only, no FN fix) yields $p{=}0.060$---marginal but directionally consistent.\nISR-specific gaming modes (H7 + H8) crowd out genuine proofs: the structural signal provides no quality benefit and actively \\emph{reduces} genuine output by creating optimization targets that are easier to satisfy than real derivations.\nThe raw $3.2\\times$ ISR$^*$ headline collapses once the LOO bias is controlled---a methodological lesson for any LOO-based metric on variable-length outputs. %% artifact: wilson_ci_complete, h8_reclassification",
    "new_string": "After reclassifying premise-subset gaming (H8; Appendix~\\ref{app:h8}) and correcting H7 classifier false negatives (s44, $n{=}12$; Appendix~\\ref{app:h4}), ISR $\\beta{=}0.1$ non-hacking rate ($6.1\\%$, $14/231$) is numerically lower than random ($9.5\\%$, $25/262$), but the difference is not statistically significant (Fisher $p{=}0.182$, two-sided, n.s.; Wilson 95\\% CI: ISR $[3.6\\%, 9.9\\%]$, Random $[6.5\\%, 13.7\\%]$; Appendix Table~\\ref{tab:bootstrap-ci}). %% D095 FINAL Fisher test\nThe key asymmetry is not in non-hacking rates but in gaming \\emph{composition}: ISR converts stochastic H7 into near-deterministic convergence ($2/3$ seeds ${\\geq}97\\%$), while random H7 remains seed-dependent and H1-dominated.\nThe raw $3.2\\times$ ISR$^*$ headline collapses once the LOO bias is controlled---a methodological lesson for any LOO-based metric on variable-length outputs. %% artifact: wilson_ci_complete, h8_reclassification"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T19:59:14.207992+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T19:59:14.208245+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "Three are quantifiable across conditions: \\textbf{H1} (conclusion embedding) is GRPO-universal at $68$--$100\\%$ regardless of reward type; \\textbf{H7} (conclusion duplication) is ISR-accelerated at 500 steps ($69.7\\%$ combined vs.\\ $0\\%$ under random), though random $\\beta{=}0.1$ converges to $100\\%$ H7 by 1000 steps (seed~42); \\textbf{H8} (premise-subset gaming) appears under both exec-only ($6\\%$) and ISR ($5\\%$) conditions (Appendix~\\ref{app:h8}).",
  "new_string": "Three are quantifiable across conditions: \\textbf{H1} (conclusion embedding) is GRPO-universal at $68$--$100\\%$ regardless of reward type; \\textbf{H7} (conclusion duplication) occurs under both ISR and random but ISR amplifies it ${\\sim}5\\times$ ($70.6\\%$ vs.\\ $13.7\\%$ under random; Fisher $p{=}1.3{\\times}10^{-39}$), with random H7 concentrated in a single seed (s43: $38.3\\%$; s42, s44: $0\\%$); \\textbf{H8} (premise-subset gaming) appears under both exec-only ($6\\%$) and ISR ($5\\%$) conditions (Appendix~\\ref{app:h8})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "old_string": "Three are quantifiable across conditions: \\textbf{H1} (conclusion embedding) is GRPO-universal at $68$--$100\\%$ regardless of reward type; \\textbf{H7} (conclusion duplication) is ISR-accelerated at 500 steps ($69.7\\%$ combined vs.\\ $0\\%$ under random), though random $\\beta{=}0.1$ converges to $100\\%$ H7 by 1000 steps (seed~42); \\textbf{H8} (premise-subset gaming) appears under both exec-only ($6\\%$) and ISR ($5\\%$) conditions (Appendix~\\ref{app:h8}).",
    "new_string": "Three are quantifiable across conditions: \\textbf{H1} (conclusion embedding) is GRPO-universal at $68$--$100\\%$ regardless of reward type; \\textbf{H7} (conclusion duplication) occurs under both ISR and random but ISR amplifies it ${\\sim}5\\times$ ($70.6\\%$ vs.\\ $13.7\\%$ under random; Fisher $p{=}1.3{\\times}10^{-39}$), with random H7 concentrated in a single seed (s43: $38.3\\%$; s42, s44: $0\\%$); \\textbf{H8} (premise-subset gaming) appears under both exec-only ($6\\%$) and ISR ($5\\%$) conditions (Appendix~\\ref{app:h8})."
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T19:59:14.208639+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T19:59:14.208956+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "H7 splits into \\textbf{H7a} (standard, text-match detectable; $65\\%$ of ISR proved) and \\textbf{H7b} (obfuscated tautology; $5\\%$)",
  "new_string": "H7 splits into \\textbf{H7a} (standard, text-match detectable; $64.5\\%$ of ISR proved, $149/231$) and \\textbf{H7b} (obfuscated tautology; $6.1\\%$, $14/231$)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "old_string": "H7 splits into \\textbf{H7a} (standard, text-match detectable; $65\\%$ of ISR proved) and \\textbf{H7b} (obfuscated tautology; $5\\%$)",
    "new_string": "H7 splits into \\textbf{H7a} (standard, text-match detectable; $64.5\\%$ of ISR proved, $149/231$) and \\textbf{H7b} (obfuscated tautology; $6.1\\%$, $14/231$)"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T19:59:14.209338+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T19:59:14.209619+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "H1 embed       & 87 & 18 & 81 & 7 & 0$^\\sharp$ \\\\\nH7 duplicate   & 0  & 70 & 0  & 0 & 100$^\\sharp$ \\\\",
  "new_string": "H1 embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nH7 duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "old_string": "H1 embed       & 87 & 18 & 81 & 7 & 0$^\\sharp$ \\\\\nH7 duplicate   & 0  & 70 & 0  & 0 & 100$^\\sharp$ \\\\",
    "new_string": "H1 embed       & 87 & 18 & 71 & 7 & 0$^\\sharp$ \\\\\nH7 duplicate   & 0  & 71 & 14 & 0 & 100$^\\sharp$ \\\\"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T19:59:14.210097+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T19:59:14.210460+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "\\textbf{Non-hacking} & 8  & 7  & 18 & \\textbf{92} & \\textbf{0} \\\\",
  "new_string": "\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "old_string": "\\textbf{Non-hacking} & 8  & 7  & 18 & \\textbf{92} & \\textbf{0} \\\\",
    "new_string": "\\textbf{Non-hacking} & 8  & 6  & 10 & \\textbf{92} & \\textbf{0} \\\\"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T19:59:14.210861+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T19:59:14.211146+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}12$; s44 only).",
  "new_string": "H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}14$; s44 only)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "old_string": "H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}12$; s44 only).",
    "new_string": "H7 includes subtypes H7a (text-match, $n{=}149$) and H7b (obfuscated tautology, $n{=}14$; s44 only)."
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T19:59:14.211516+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T19:59:14.212026+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "Exec-only, ISR, and random conditions all show $\\geq 80\\%$ pooled hacking among proved samples; only SFT shows $92\\%$ non-hacking.\nAcross 2 logic types, 6 reward conditions, 3 seeds, and up to 1000 steps, no GRPO condition we tested produces a high-PR run that is also majority non-hacking; the closest is ISR $\\beta{=}0.1$ s42 at $\\text{PR}{=}81\\%$, $17\\%$ non-hacking, and even that residual is the premise-minimization artifact analyzed above.",
  "new_string": "Exec-only, ISR, and random conditions all show $\\geq 80\\%$ pooled hacking among proved samples; only SFT shows $92\\%$ non-hacking.\nAcross 2 logic types, 6 reward conditions, 3 seeds, and up to 1000 steps, no GRPO condition we tested produces a high-PR run that is also majority non-hacking; the closest is random $\\beta{=}0.1$ s42 at $\\text{PR}{=}79\\%$, $22.8\\%$ non-hacking, and ISR $\\beta{=}0.1$ s42 at $\\text{PR}{=}81\\%$, $17.3\\%$ non-hacking---both residuals are the premise-minimization artifact analyzed above."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "old_string": "Exec-only, ISR, and random conditions all show $\\geq 80\\%$ pooled hacking among proved samples; only SFT shows $92\\%$ non-hacking.\nAcross 2 logic types, 6 reward conditions, 3 seeds, and up to 1000 steps, no GRPO condition we tested produces a high-PR run that is also majority non-hacking; the closest is ISR $\\beta{=}0.1$ s42 at $\\text{PR}{=}81\\%$, $17\\%$ non-hacking, and even that residual is the premise-minimization artifact analyzed above.",
    "new_string": "Exec-only, ISR, and random conditions all show $\\geq 80\\%$ pooled hacking among proved samples; only SFT shows $92\\%$ non-hacking.\nAcross 2 logic types, 6 reward conditions, 3 seeds, and up to 1000 steps, no GRPO condition we tested produces a high-PR run that is also majority non-hacking; the closest is random $\\beta{=}0.1$ s42 at $\\text{PR}{=}79\\%$, $22.8\\%$ non-hacking, and ISR $\\beta{=}0.1$ s42 at $\\text{PR}{=}81\\%$, $17.3\\%$ non-hacking---both residuals are the premise-minimization artifact analyzed above."
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T19:59:14.212437+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T19:59:14.212803+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "H8 prem-subset & 6  & 5  & --- & 0 & --- \\\\",
  "new_string": "H8 prem-subset & 6  & 5  & 8   & 0 & --- \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "old_string": "H8 prem-subset & 6  & 5  & --- & 0 & --- \\\\",
    "new_string": "H8 prem-subset & 6  & 5  & 8   & 0 & --- \\\\"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T19:59:14.213177+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T19:59:14.213462+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T19:59:14.214083+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits meta-level Goodhart's Law (\S\ref{sec:goodhart}); and STA as a cross-logic protocol (\S\ref{sec:crosslogic}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}8$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline is trained with NLL on gold formalizations.\footnote{All experiments use \texttt{data/train\_500\_seed42.jsonl}; seeds control initialization and rollout sampling only.}
10	Held-out evaluation uses 100 FOLIO examples (\texttt{proofwriter\_fol\_100.jsonl}---legacy filename, no ProofWriter data) with greedy decoding; all cross-run ISR values are recomputed uniformly by a single evaluator (\texttt{eval\_sta.py}) so training-log ISR is never compared across runs.
11	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for H1/H7 plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:taxonomy-method}), and a \emph{non-hacking} (N-H) rate---the residual of proved samples matching none of the eight cataloged patterns, a necessary but not sufficient condition for semantic correctness.
12	
13	\subsection{ISR as Diagnostic}
14	\label{sec:diagnostic}
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=0.95\columnwidth]{figures/fig2_isr_collapse.pdf}
19	\caption{ISR collapse under exec-only GRPO (seed~42). PR rises 32\%$\to$93\%$\to$96\% while proved-only ISR falls $0.642{\to}0.132{\to}0.003$ over 100$\to$500$\to$1000 steps. By step 1000, 94.8\% of proved samples hav
…[truncated 17250 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T19:59:14.215958+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "H7b samples use vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$) to evade the text-match classifier while remaining logically equivalent, with $10/12$ achieving $\\text{ISR}{\\approx}0.8$",
  "new_string": "H7b samples use vacuous quantifier wrapping or structural simplification to evade the text-match classifier while remaining logically equivalent (s44: $11/12$ quantifier wrapping, $1/12$ structural; s43: $2$), with $10/14$ achieving $\\text{ISR}{\\approx}0.8$"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "old_string": "H7b samples use vacuous quantifier wrapping ($11/12$) or structural simplification ($1/12$) to evade the text-match classifier while remaining logically equivalent, with $10/12$ achieving $\\text{ISR}{\\approx}0.8$",
    "new_string": "H7b samples use vacuous quantifier wrapping or structural simplification to evade the text-match classifier while remaining logically equivalent (s44: $11/12$ quantifier wrapping, $1/12$ structural; s43: $2$), with $10/14$ achieving $\\text{ISR}{\\approx}0.8$"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T19:59:14.216328+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T19:59:14.216557+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "old_string": "H7b (obfuscated tautology, $n{=}14$; s44 only)",
  "new_string": "H7b (obfuscated tautology, $n{=}14$; primarily s44)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "old_string": "H7b (obfuscated tautology, $n{=}14$; s44 only)",
    "new_string": "H7b (obfuscated tautology, $n{=}14$; primarily s44)"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T19:59:14.216909+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T19:59:14.217184+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
  "offset": "57",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/experiments.tex",
    "offset": "57",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T19:59:14.217465+00:00_

57	ISR & 0.1 & 77{\scriptsize$\pm$14} & $\ddagger$ & \textbf{71}$^\P$ & 18 & 6 \\ %% registry: plan002-additive-b01-s42/s43-r2/s44 (pooled, D095 FINAL)
58	Random & 0.1 & \textbf{87}{\scriptsize$\pm$8} & 0.117{\scriptsize$\pm$.04} & 14$^\S$ & 71 & 10 \\ %% registry: plan018-additive-random-b01-s42/s43-r3/s44-r2 (D095 FINAL)
59	\midrule
60	ISR & 0.3 & 66{\scriptsize$\pm$42} & 0.39{\scriptsize$\pm$.31} & \textbf{50} & 37 & 14 \\ %% registry: plan002-additive-b03-s42/s43/s44 (pooled)
61	Random & 0.3 & 54{\scriptsize$\pm$35} & 0.09{\scriptsize$\pm$.09} & 7 & 91 & 2 \\ %% registry: plan017-additive-random-s42, exp1-random-b03-s43-r4, exp1-random-b03-s44-r2 (pooled; D086 H7: s42=4,s43=7,s44=0)
62	\bottomrule
63	\end{tabular}}
64	\caption{Goodhart landscape across reward conditions. 3-seed rows: H7/H1/N-H pooled across seeds; PR/ISR$^*$: mean$\pm$std of per-seed values. $^\dagger$Seed~42. $\ddagger$$\text{ISR}^*$ omitted for ISR $\beta{=}0.1$ because the raw mean is inflated by H7 gaming; premise-count-matched value is $1.06\times$ random (\S\ref{sec:goodhart}, Appendix~\ref{app:detailed-results}). $^\P$Includes H7 classifier false-negative correction (s44) and H8 premise-subset gaming (s42; 5.2\% of proved; Appendix~\ref{app:h8}). $^\S$Random H7 driven by seed~43 (38.3\%); seeds~42 and~44: 0\%. Per-seed breakdown in Appendix Table~\ref{tab:fol-detailed}.}
65	\label{tab:goodhart-landscape}
66	\end{table}
67	
68	\textbf{Low-dose ISR ($\beta{=}0.1$): ISR-amplified gaming.}
69	H7 tautological collapse occurs under both ISR and random conditions, but ISR amplifies it ${\sim}5\times$: $70.6\%$ ($163/231$) under ISR vs.\ $13.7\%$ ($36/262$) under random (Fisher $p{=}1.3{\times}10^{-39}$, $\text{OR}{=}15.05$). %% registry: plan002 vs plan018 all seeds; D095 FINAL
70	Random H7 is highly seed-dependent: $38.3\%$ in seed~43 vs.\ $0\%$ in seeds~42 and~44; ISR makes H7 near-deterministic ($2/3$ seeds at $97$--$100\%$, Table~\ref{tab:fol-detailed}).
71	H7---a single premise identical to
…[truncated 2735 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d095-experiments_20260515T195541",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-15T19:59:14.219825+00:00_

All edits are consistent. Let me verify the key data points against D095:

**Table 1 verification:**
- ISR β=0.1: H7=71% (163/231=70.6%→71), H1=18% (42/231=18.2%→18), N-H=6% (14/231=6.06%→6) ✓
- Random β=0.1: PR=87±8, ISR*=0.117±.04, H7=14% (36/262=13.7%→14), H1=71% (187/262=71.4%→71), N-H=10% (25/262=9.5%→10) ✓
- §-footnote for Random H7 seed dependency ✓

**§4.3 verification:**
- Fisher p=1.3×10⁻³⁹, OR=15.05 ✓
- Random H7 per-seed: 38.3% s43, 0% s42/s44 ✓
- H1 updated to 71% (from 81%) ✓
- PR updated to 87±8 (from 85±6) ✓
- Genuine rate: 6.1% vs 9.5%, Fisher p=0.182, n.s. ✓
- Wilson CI: ISR [3.6%, 9.9%], Random [6.5%, 13.7%] ✓
- Removed "significantly lower" claim, "conservative correction" sentence, and "crowd out genuine proofs" ✓

**§4.4 verification:**
- H7: "70.6% vs 13.7%, Fisher p=1.3×10⁻³⁹" ✓
- H7a: "64.5%, 149/231" ✓
- H7b: "6.1%, 14/231" ✓
- Table 2: H1=71, H7=14, H8=8, N-H=10 for Random; H7=71, N-H=6 for ISR ✓

**Narrative A compliance:**
1. No "H7 is ISR-specific" or "zero under random" ✓
2. "H7a is GRPO-general, seed-dependent; ISR amplifies it ~5x" ✓
3. Per-seed and pooled reported ✓
4. Random H7 single-seed source marked with §-footnote ✓
5. Genuine rate difference reported as n.s. (p=0.182) ✓
6. Correct framing: ISR makes H7 "near-deterministic" vs stochastic ✓

All 10 edits applied across 4 sections. Data matches D095 FINAL values exactly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_d095-experiments_20260515T195541"
}
```

</details>

---
