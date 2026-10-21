# paper scaling placeholder into experiments

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/chats/worker_paper_scaling-placeholder-into-experiments_20260519T220841.jsonl`
- **Structured JSON:** [`a4dbf5e201b0d9be410c.json`](../../sessions/a4/a4dbf5e201b0d9be410c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

15 recorded events

### Tool call

_source line 1 · 2026-05-19T22:10:22.911520+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_scaling-placeholder-into-experiments_20260519T220841",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T22:10:22.911948+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on four English NER benchmarks spanning a difficulty gradient, each serving a distinct role.
9	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
10	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
11	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
12	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
13	
14	\paragraph{Models and sampling.}
15	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (training details in Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others due to earlier convergence; Appendix~\ref{app:epoch_confound}).
16	We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\ref{app:n_scaling}).
17	
18	%% ============================================================
19	\subsection{Quality Estimation Results}
20	\label{sec:qe_results}
21	
22	\begin{table*}[t]
23	\centering
24	\small
25	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \textbf{bold}. RE in Appendix~\ref{app:re_extension}; $N{=}16$ in Table~\ref{tab:robustness}.}
26	\label{tab:quality_estimation}
27	\begin{tabula
…[truncated 18482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_scaling-placeholder-into-experiments_20260519T220841",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T22:10:22.912155+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/scaling_narrative_A_monotonic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_scaling-placeholder-into-experiments_20260519T220841",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/scaling_narrative_A_monotonic.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T22:10:22.912343+00:00_

1	%% Version A: Monotonic scaling narrative (7B < 14B < 32B degeneracy)
2	%% Use condition: Qwen2.5 FT results show degeneracy rising monotonically with scale.
3	%% Status: Placeholder framework — fill numbers when exp results arrive.
4	
5	%% ---- Placeholder commands (replace with actual values) ----
6	\newcommand{\scaleSevenDegen}{XX.X}    % 7B degeneracy %
7	\newcommand{\scaleFourteenDegen}{XX.X} % 14B degeneracy %
8	\newcommand{\scaleThirtytwoDegen}{XX.X}% 32B degeneracy %
9	\newcommand{\scaleSevenGreedy}{.XXX}   % 7B greedy F1
10	\newcommand{\scaleFourteenGreedy}{.XXX}% 14B greedy F1
11	\newcommand{\scaleThirtytwoGreedy}{.XXX}% 32B greedy F1
12	\newcommand{\scaleSevenConstr}{X.XX}   % 7B construction Δ (pp)
13	\newcommand{\scaleFourteenConstr}{X.XX}% 14B construction Δ (pp)
14	\newcommand{\scaleThirtytwoConstr}{X.XX}% 32B construction Δ (pp)
15	\newcommand{\scaleSevenLP}{.XXX}       % 7B LP ρ
16	\newcommand{\scaleFourteenLP}{.XXX}    % 14B LP ρ
17	\newcommand{\scaleThirtytwoLP}{.XXX}   % 32B LP ρ
18	
19	%% ---- Narrative ----
20	
21	\paragraph{Degeneracy rises with scale within a model family.}
22	To examine how model scale affects the capability--diversity tradeoff, we fine-tune Qwen2.5 at three scales (7B, 14B, 32B) with an identical QLoRA recipe on Few-NERD ($N{=}8$, $T{=}1.0$).
23	Degeneracy increases monotonically with parameter count: $\scaleSevenDegen\%\to\scaleFourteenDegen\%\to\scaleThirtytwoDegen\%$ (Figure~\ref{fig:scaling_curve}a).
24	Greedy F1 also rises ($\scaleSevenGreedy\to\scaleFourteenGreedy\to\scaleThirtytwoGreedy$), confirming that larger models are more capable but less diverse in their sampled outputs.
25	LP-weighted construction $\Delta$F1 inversely tracks degeneracy ($\scaleSevenConstr\to\scaleFourteenConstr\to\scaleThirtytwoConstr$\,pp), consistent with the gating hypothesis from \S\ref{sec:fewnerd}: the selection window narrows as stronger greedy performance comes at the cost of reduced output diversity.
26	
27	This within-family trend
…[truncated 695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_scaling-placeholder-into-experiments_20260519T220841",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T22:10:22.912504+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_scaling-placeholder-into-experiments_20260519T220841",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/sections/zeroshot_scaling_draft.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T22:10:22.912664+00:00_

1	%% Draft: Zero-shot / Scaling paragraph for \S5.5 (Scaling Behavior)
2	%% Exp ID: exp_qwen25_72b_zeroshot (all 72B ZS numbers)
3	%% Status: Draft for Paper Agent integration. Replaces current \S5.5 content.
4	%% Pending: 7B/14B/32B FT results for full scaling curve; 72B FT for regime disentanglement.
5	
6	\subsection{Scaling Behavior}
7	\label{sec:scaling}
8	
9	To test whether the correlation-selection gap is specific to fine-tuned models, we evaluate Qwen2.5-72B-Instruct (AWQ 4-bit) in a zero-shot setting across all three primary datasets ($N{=}8$, $T{=}1.0$, no task-specific training).
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\caption{Fine-tuned 8B vs.\ zero-shot 72B: QE correlations and entity construction ($N{=}8$, $T{=}1.0$). Degen.\ = instance degeneracy (\%). Constr.\ = LP-weighted entity construction $\Delta$F1 vs.\ greedy (pp). $^\dagger$Majority voting (uniform weights).}
15	\label{tab:zs_72b}
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}llcccccr@{}}
18	\toprule
19	Dataset & Regime & Greedy & Degen. & LP $\rho$ & SJ $\rho$ & VC $\rho$ & Constr. \\
20	\midrule
21	SciERC & 8B FT  & .645 & 17.8\% & .205 & .360 & .379 & $+$1.02 \\
22	       & 72B ZS & .399 & 21.0\% & .081 & .217 & .277 & $+$1.53 \\
23	\midrule
24	Few-NERD & 8B FT & .748 & 13.0\% & .220 & .380 & --- & $+$1.40 \\
25	         & 72B ZS & .628 & 46.2\% & .119 & .345 & .416 & $-$0.20 \\
26	\midrule
27	CoNLL  & 8B FT  & .908 & 61.7\% & .302 & .436 & .424 & $-$0.39 \\
28	       & 72B ZS & .712 & 67.7\% & $-$.002 & .304 & .297 & $-$0.37 \\
29	\bottomrule
30	\end{tabular}}
31	\end{table}
32	
33	\paragraph{LP requires fine-tuning calibration.}
34	Table~\ref{tab:zs_72b} compares QE correlations between regimes.
35	LP $\rho$ drops to near zero in the zero-shot setting: from $0.205$ to $0.081$ on SciERC, $0.220$ to $0.119$ on Few-NERD, and $0.302$ to $-0.002$ on CoNLL.
36	Fine-tuning calibrates the model's token-level confidence to task-specific quality gradients; without this calibrat
…[truncated 2836 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_scaling-placeholder-into-experiments_20260519T220841",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T22:10:22.912861+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "old_string": "%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}",
  "new_string": "%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\n%% ---- Scaling placeholder commands (replace with actual values) ----\n\\newcommand{\\scaleSevenDegen}{XX.X}    % 7B degeneracy %\n\\newcommand{\\scaleFourteenDegen}{XX.X} % 14B degeneracy %\n\\newcommand{\\scaleThirtytwoDegen}{XX.X}% 32B degeneracy %\n\\newcommand{\\scaleSevenGreedy}{.XXX}   % 7B greedy F1\n\\newcommand{\\scaleFourteenGreedy}{.XXX}% 14B greedy F1\n\\newcommand{\\scaleThirtytwoGreedy}{.XXX}% 32B greedy F1\n\\newcommand{\\scaleSevenConstr}{X.XX}   % 7B construction Δ (pp)\n\\newcommand{\\scaleFourteenConstr}{X.XX}% 14B construction Δ (pp)\n\\newcommand{\\scaleThirtytwoConstr}{X.XX}% 32B construction Δ (pp)\n\\newcommand{\\scaleSevenLP}{.XXX}       % 7B LP ρ\n\\newcommand{\\scaleFourteenLP}{.XXX}    % 14B LP ρ\n\\newcommand{\\scaleThirtytwoLP}{.XXX}   % 32B LP ρ"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_scaling-placeholder-into-experiments_20260519T220841",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "old_string": "%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}",
    "new_string": "%% ============================================================\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\n%% ---- Scaling placeholder commands (replace with actual values) ----\n\\newcommand{\\scaleSevenDegen}{XX.X}    % 7B degeneracy %\n\\newcommand{\\scaleFourteenDegen}{XX.X} % 14B degeneracy %\n\\newcommand{\\scaleThirtytwoDegen}{XX.X}% 32B degeneracy %\n\\newcommand{\\scaleSevenGreedy}{.XXX}   % 7B greedy F1\n\\newcommand{\\scaleFourteenGreedy}{.XXX}% 14B greedy F1\n\\newcommand{\\scaleThirtytwoGreedy}{.XXX}% 32B greedy F1\n\\newcommand{\\scaleSevenConstr}{X.XX}   % 7B construction Δ (pp)\n\\newcommand{\\scaleFourteenConstr}{X.XX}% 14B construction Δ (pp)\n\\newcommand{\\scaleThirtytwoConstr}{X.XX}% 32B construction Δ (pp)\n\\newcommand{\\scaleSevenLP}{.XXX}       % 7B LP ρ\n\\newcommand{\\scaleFourteenLP}{.XXX}    % 14B LP ρ\n\\newcommand{\\scaleThirtytwoLP}{.XXX}   % 32B LP ρ"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T22:10:22.913144+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_scaling-placeholder-into-experiments_20260519T220841",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T22:10:22.913317+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "old_string": "This comparison simultaneously varies model family (Qwen3$\\to$Qwen2.5), training regime (fine-tuned$\\to$zero-shot), and quantization (FP16$\\to$AWQ 4-bit); while the consistency of structural signal rankings across these changes suggests the gap is robust, we cannot fully disentangle these factors.\nLP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]; $d{=}0.10$), recovering $10.2$\\% of headroom (FT: $7.8$\\% SciERC, $11.3$\\% Few-NERD). Majority vote also succeeds ($+1.39$\\,pp); LP-weighting adds $+0.14$\\,pp. Construction fails on Few-NERD 72B ZS ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp), where degeneracy exceeds $46$\\%---consistent with the degeneracy-gating pattern in the fine-tuned regime ($n{=}3$ datasets).\n\n%% ============================================================\n\\subsection{Prescriptive Results}",
  "new_string": "This comparison simultaneously varies model family (Qwen3$\\to$Qwen2.5), training regime (fine-tuned$\\to$zero-shot), and quantization (FP16$\\to$AWQ 4-bit); while the consistency of structural signal rankings across these changes suggests the gap is robust, we cannot fully disentangle these factors.\nLP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]; $d{=}0.10$), recovering $10.2$\\% of headroom (FT: $7.8$\\% SciERC, $11.3$\\% Few-NERD). Majority vote also succeeds ($+1.39$\\,pp); LP-weighting adds $+0.14$\\,pp. Construction fails on Few-NERD 72B ZS ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp), where degeneracy exceeds $46$\\%---consistent with the degeneracy-gating pattern in the fine-tuned regime ($n{=}3$ datasets).\n\n\\paragraph{Degeneracy rises with scale within a model family.}\nTo examine how model scale affects the capability--diversity tradeoff, we fine-tune Qwen2.5 at three scales (7B, 14B, 32B) with an identical QLoRA recipe on Few-NERD ($N{=}8$, $T{=}1.0$).\nDegeneracy increases monotonically with parameter count: $\\scaleSevenDegen\\%\\to\\scaleFourteenDegen\\%\\to\\scaleThirtytwoDegen\\%$ (Figure~\\ref{fig:scaling_curve}a).\nGreedy F1 also rises ($\\scaleSevenGreedy\\to\\scaleFourteenGreedy\\to\\scaleThirtytwoGreedy$), confirming that larger models are more capable but less diverse in their sampled outputs.\nLP-weighted construction $\\Delta$F1 inversely tracks degeneracy ($\\scaleSevenConstr\\to\\scaleFourteenConstr\\to\\scaleThirtytwoConstr$\\,pp), consistent with the gating hypothesis from \\S\\ref{sec:fewnerd}: the selection window narrows as stronger greedy performance comes at the cost of reduced output diversity.\n\nThis within-family trend converges with two independent dimensions of evidence.\nAlong the \\emph{epoch} dimension, extending Qwen3-8B training from 3 to 5 epochs on Few-NERD raises degeneracy from 11.1\\% to 31.3\\% (\\S\\ref{sec:fewnerd}), mirroring the effect of added parameters.\nAlong the \\emph{family} dimension, Qwen3-8B FT (13.0\\% degeneracy, $+1.40$\\,pp construction) and Qwen2.5-72B ZS (46.2\\%, $-0.20$\\,pp) bracket the trade-off from opposite ends.\nAcross all three dimensions---scale, training duration, and model family---higher degeneracy consistently predicts smaller or negative construction gains, supporting degeneracy as a robust diagnostic for when self-consistency aggregation can add value.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scaling analysis: Qwen2.5 fine-tuned on FewNERD ($N{=}8$, $T{=}1.0$, 3-seed mean). 8B row from Qwen3-8B (Table~\\ref{tab:fewnerd}).}\n\\label{tab:scaling_ft}\n\\begin{tabular}{lcccccc}\n\\toprule\nScale & Degen\\% & LP $\\rho$ & SJ $\\rho$ & Greedy & Constr.\\ $\\Delta$ & $p$ \\\\\n\\midrule\n7B  & \\scaleSevenDegen & \\scaleSevenLP & --- & \\scaleSevenGreedy & \\scaleSevenConstr & --- \\\\\n8B  & 13.0 & .220 & .380 & .748 & $+$1.40 & ${<}.001$ \\\\\n14B & \\scaleFourteenDegen & \\scaleFourteenLP & --- & \\scaleFourteenGreedy & \\scaleFourteenConstr & --- \\\\\n32B & \\scaleThirtytwoDegen & \\scaleThirtytwoLP & --- & \\scaleThirtytwoGreedy & \\scaleThirtytwoConstr & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n%\\includegraphics[width=\\columnwidth]{figures/scaling_curve.pdf}\n\\caption{Degeneracy and LP-weighted construction $\\Delta$F1 across model scales (FewNERD, $N{=}8$). Placeholder --- data pending.}\n\\label{fig:scaling_curve}\n\\end{figure}\n\n% NOTE: Version B (non-monotonic narrative) available at artifacts/scaling_narrative_B_nonmonotonic.tex\n\n%% ============================================================\n\\subsection{Prescriptive Results}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_scaling-placeholder-into-experiments_20260519T220841",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "old_string": "This comparison simultaneously varies model family (Qwen3$\\to$Qwen2.5), training regime (fine-tuned$\\to$zero-shot), and quantization (FP16$\\to$AWQ 4-bit); while the consistency of structural signal rankings across these changes suggests the gap is robust, we cannot fully disentangle these factors.\nLP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]; $d{=}0.10$), recovering $10.2$\\% of headroom (FT: $7.8$\\% SciERC, $11.3$\\% Few-NERD). Majority vote also succeeds ($+1.39$\\,pp); LP-weighting adds $+0.14$\\,pp. Construction fails on Few-NERD 72B ZS ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp), where degeneracy exceeds $46$\\%---consistent with the degeneracy-gating pattern in the fine-tuned regime ($n{=}3$ datasets).\n\n%% ============================================================\n\\subsection{Prescriptive Results}",
    "new_string": "This comparison simultaneously varies model family (Qwen3$\\to$Qwen2.5), training regime (fine-tuned$\\to$zero-shot), and quantization (FP16$\\to$AWQ 4-bit); while the consistency of structural signal rankings across these changes suggests the gap is robust, we cannot fully disentangle these factors.\nLP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]; $d{=}0.10$), recovering $10.2$\\% of headroom (FT: $7.8$\\% SciERC, $11.3$\\% Few-NERD). Majority vote also succeeds ($+1.39$\\,pp); LP-weighting adds $+0.14$\\,pp. Construction fails on Few-NERD 72B ZS ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp), where degeneracy exceeds $46$\\%---consistent with the degeneracy-gating pattern in the fine-tuned regime ($n{=}3$ datasets).\n\n\\paragraph{Degeneracy rises with scale within a model family.}\nTo examine how model scale affects the capability--diversity tradeoff, we fine-tune Qwen2.5 at three scales (7B, 14B, 32B) with an identical QLoRA recipe on Few-NERD ($N{=}8$, $T{=}1.0$).\nDegeneracy increases monotonically with parameter count: $\\scaleSevenDegen\\%\\to\\scaleFourteenDegen\\%\\to\\scaleThirtytwoDegen\\%$ (Figure~\\ref{fig:scaling_curve}a).\nGreedy F1 also rises ($\\scaleSevenGreedy\\to\\scaleFourteenGreedy\\to\\scaleThirtytwoGreedy$), confirming that larger models are more capable but less diverse in their sampled outputs.\nLP-weighted construction $\\Delta$F1 inversely tracks degeneracy ($\\scaleSevenConstr\\to\\scaleFourteenConstr\\to\\scaleThirtytwoConstr$\\,pp), consistent with the gating hypothesis from \\S\\ref{sec:fewnerd}: the selection window narrows as stronger greedy performance comes at the cost of reduced output diversity.\n\nThis within-family trend converges with two independent dimensions of evidence.\nAlong the \\emph{epoch} dimension, extending Qwen3-8B training from 3 to 5 epochs on Few-NERD raises degeneracy from 11.1\\% to 31.3\\% (\\S\\ref{sec:fewnerd}), mirroring the effect of added parameters.\nAlong the \\emph{family} dimension, Qwen3-8B FT (13.0\\% degeneracy, $+1.40$\\,pp construction) and Qwen2.5-72B ZS (46.2\\%, $-0.20$\\,pp) bracket the trade-off from opposite ends.\nAcross all three dimensions---scale, training duration, and model family---higher degeneracy consistently predicts smaller or negative construction gains, supporting degeneracy as a robust diagnostic for when self-consistency aggregation can add value.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Scaling analysis: Qwen2.5 fine-tuned on FewNERD ($N{=}8$, $T{=}1.0$, 3-seed mean). 8B row from Qwen3-8B (Table~\\ref{tab:fewnerd}).}\n\\label{tab:scaling_ft}\n\\begin{tabular}{lcccccc}\n\\toprule\nScale & Degen\\% & LP $\\rho$ & SJ $\\rho$ & Greedy & Constr.\\ $\\Delta$ & $p$ \\\\\n\\midrule\n7B  & \\scaleSevenDegen & \\scaleSevenLP & --- & \\scaleSevenGreedy & \\scaleSevenConstr & --- \\\\\n8B  & 13.0 & .220 & .380 & .748 & $+$1.40 & ${<}.001$ \\\\\n14B & \\scaleFourteenDegen & \\scaleFourteenLP & --- & \\scaleFourteenGreedy & \\scaleFourteenConstr & --- \\\\\n32B & \\scaleThirtytwoDegen & \\scaleThirtytwoLP & --- & \\scaleThirtytwoGreedy & \\scaleThirtytwoConstr & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n%\\includegraphics[width=\\columnwidth]{figures/scaling_curve.pdf}\n\\caption{Degeneracy and LP-weighted construction $\\Delta$F1 across model scales (FewNERD, $N{=}8$). Placeholder --- data pending.}\n\\label{fig:scaling_curve}\n\\end{figure}\n\n% NOTE: Version B (non-monotonic narrative) available at artifacts/scaling_narrative_B_nonmonotonic.tex\n\n%% ============================================================\n\\subsection{Prescriptive Results}"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T22:10:22.913615+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_scaling-placeholder-into-experiments_20260519T220841",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T22:10:22.913771+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": "179",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_scaling-placeholder-into-experiments_20260519T220841",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "offset": "179",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T22:10:22.913947+00:00_

179	%% ============================================================
180	\subsection{Scaling Behavior}
181	\label{sec:scaling}
182	
183	%% ---- Scaling placeholder commands (replace with actual values) ----
184	\newcommand{\scaleSevenDegen}{XX.X}    % 7B degeneracy %
185	\newcommand{\scaleFourteenDegen}{XX.X} % 14B degeneracy %
186	\newcommand{\scaleThirtytwoDegen}{XX.X}% 32B degeneracy %
187	\newcommand{\scaleSevenGreedy}{.XXX}   % 7B greedy F1
188	\newcommand{\scaleFourteenGreedy}{.XXX}% 14B greedy F1
189	\newcommand{\scaleThirtytwoGreedy}{.XXX}% 32B greedy F1
190	\newcommand{\scaleSevenConstr}{X.XX}   % 7B construction Δ (pp)
191	\newcommand{\scaleFourteenConstr}{X.XX}% 14B construction Δ (pp)
192	\newcommand{\scaleThirtytwoConstr}{X.XX}% 32B construction Δ (pp)
193	\newcommand{\scaleSevenLP}{.XXX}       % 7B LP ρ
194	\newcommand{\scaleFourteenLP}{.XXX}    % 14B LP ρ
195	\newcommand{\scaleThirtytwoLP}{.XXX}   % 32B LP ρ
196	
197	We evaluate Qwen2.5-72B-Instruct in a zero-shot setting to test whether the gap persists at larger scale without fine-tuning.
198	
199	\begin{table}[t]
200	\centering
201	\small
202	\caption{Fine-tuned 8B vs.\ zero-shot 72B ($N{=}8$, $T{=}1.0$). Hdr.\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\%).}
203	\label{tab:scale_comparison}
204	\resizebox{\columnwidth}{!}{%
205	\begin{tabular}{@{}llccccccc@{}}
206	\toprule
207	Dataset & Regime & Greedy & Hdr. & Degen. & VC & SJ & FK & LP \\
208	\midrule
209	SciERC & 8B FT  & .644 & 13.0 & 17.8 & .379 & .360 & .267 & .205 \\
210	       & 72B ZS & .399 & 15.0 & 21.0 & .277 & .217 & .227 & .081 \\
211	\midrule
212	Few-NERD & 8B FT & .748 & 12.4 & 13.0 & --- & --- & --- & .220 \\
213	         & 72B ZS & .628 & --- & 46.2 & .416 & .345 & --- & .119 \\
214	\midrule
215	CoNLL  & 8B FT  & .908 & ${\approx}$4 & 61.7 & .424 & .436 & .400 & .302 \\
216	       & 72B ZS & .712 & 5.3 & 67.7 & .297 & .304 & .302 & $-$.002 \\
217	\bottomrule
218	\end{tabular}}
219	\end{table}
220	
221	LP $\rho$ drops s
…[truncated 3802 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_scaling-placeholder-into-experiments_20260519T220841",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T22:10:22.914102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
  "offset": "258",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_scaling-placeholder-into-experiments_20260519T220841",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
    "offset": "258",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T22:10:22.914254+00:00_

258	\end{figure}
259	
260	% NOTE: Version B (non-monotonic narrative) available at artifacts/scaling_narrative_B_nonmonotonic.tex
261	
262	%% ============================================================
263	\subsection{Prescriptive Results}
264	\label{sec:prescriptive}
265	
266	The preceding sections establish that instance-level selection fails for structured IE. We now present two approaches that extract value from multi-sample generation without relying on sample ranking.
267	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_scaling-placeholder-into-experiments_20260519T220841",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-19T22:10:22.914422+00:00_

已完成。experiments.tex 中新增内容位于 §5.5 Scaling Behavior：

**插入位置和内容：**
- **L183–195**: 12 个 `\newcommand` placeholder（7B/14B/32B 的 degen、greedy、constr、LP）
- **L225–234**: Version A 叙事段落 — "Degeneracy rises with scale within a model family"，含三维证据收敛（scale/epoch/family）
- **L236–251**: Table `tab:scaling_ft` — 7B/14B/32B/8B 对比表，8B 行填入已知值
- **L253–258**: Figure `fig:scaling_curve` placeholder（`\includegraphics` 已注释）
- **L260**: Version B 备选注释

**待填 placeholder 清单（12 个）：**

| 命令 | 含义 |
|------|------|
| `\scaleSevenDegen` | 7B degeneracy % |
| `\scaleFourteenDegen` | 14B degeneracy % |
| `\scaleThirtytwoDegen` | 32B degeneracy % |
| `\scaleSevenGreedy` | 7B greedy F1 |
| `\scaleFourteenGreedy` | 14B greedy F1 |
| `\scaleThirtytwoGreedy` | 32B greedy F1 |
| `\scaleSevenConstr` | 7B construction Δ (pp) |
| `\scaleFourteenConstr` | 14B construction Δ (pp) |
| `\scaleThirtytwoConstr` | 32B construction Δ (pp) |
| `\scaleSevenLP` | 7B LP ρ |
| `\scaleFourteenLP` | 14B LP ρ |
| `\scaleThirtytwoLP` | 32B LP ρ |

Table 中 SJ ρ 列 7B/14B/32B 也为 `---`，待实验数据补充。Figure 的 `scaling_curve.pdf` 待生成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_scaling-placeholder-into-experiments_20260519T220841"
}
```

</details>

---
