# audit extract paper numbers

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 86
- **Recorded user turns:** 0
- **Tool calls:** 42
- **Original source:** `logs/chats/worker_audit_extract-paper-numbers_20260525T194435.jsonl`
- **Structured JSON:** [`5afb0ec44eb77403e166.json`](../../sessions/5a/5afb0ec44eb77403e166.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

86 recorded events

### Assistant

_source line 1 · 2026-05-25T19:44:45.954324+00:00_

You've hit your limit · resets 12am (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_extract-paper-numbers_20260525T194435"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-25T19:56:13.150679+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/ && echo \"---\" && ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/ && echo \"---\" && ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/ && echo \"---\" && ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/ && echo \"---\" && ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/",
    "description": "List paper directory contents"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-25T19:56:13.151012+00:00_

abstract.tex
acl.sty
acl_natbib.bst
appendix.tex
backup
conclusion.tex
ethics.tex
experiments.tex
figures
introduction.tex
limitations.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
method.md
method.tex
references.bib
related_work.tex
results.md
tables
---
_deprecated
tab1_recovery_gradient.tex
tab2_decoupling.tex
tab5_cross_scale.tex
tab_cka_stability.tex
tab_math500.tex
tab_mbpp.tex
table3_alpha.tex
table4_sparsity_cliff.tex
---
fig1_dose_response.pdf
fig1_dose_response.png
fig1_framework.pdf
fig1_framework.png
fig2_reward_accuracy.pdf
fig2_reward_accuracy.png
fig2_reward_trajectories.pdf
fig2_reward_trajectories.png
fig3_collapse_dynamics.pdf
fig3_collapse_dynamics.png
fig4_cka_heatmap.pdf
fig4_cka_heatmap.png
fig5_extended_training.pdf
fig5_extended_training.png
fig_appendix_kl.pdf
fig_appendix_kl.png
fig_sft_grpo_scatter.pdf
fig_sft_grpo_scatter.png
gen_fig1_dose_response.py
gen_fig1_framework.py
gen_fig2_reward_accuracy.py
gen_fig2_reward_trajectories.py
gen_fig3_collapse_dynamics.py
gen_fig4_cka_heatmap.py
gen_fig5_extended_training.py
gen_fig_appendix_kl.py
gen_fig_sft_grpo_scatter.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T19:56:13.151188+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-25T19:56:13.151375+00:00_

1	Reinforcement learning with verifiable rewards (RLVR) is widely regarded as essential for recovering pruned reasoning models, substantially outperforming supervised fine-tuning (SFT). We find that this advantage vanishes under fine-grained structured pruning: across four criteria applied to a 7B reasoning model at moderate sparsity, SFT and RL recover to near-identical accuracy for each criterion tested. We term this \emph{reward-accuracy decoupling}.
2	What the pruning criterion does control is RL training dynamics. To study this, we introduce Recovery-Aware Structured Pruning (\rasp{}), a scoring function that balances gradient importance with representational diversity via Centered Kernel Alignment (CKA). The resulting \emph{recovery capacity spectrum} shows that diversity-preserving criteria sustain RL optimization while importance-dominated criteria exhibit reward collapse, yet none of these differences translate into accuracy gains over SFT.
3	These findings reframe the role of RL in pruning recovery: SFT warmup captures most recoverable reasoning capacity, while RL serves as a diagnostic that reveals structural deficiencies invisible to accuracy. Directional trends hold across three benchmarks, with preliminary cross-scale and cross-model evidence\footnote{Code and data are available at \url{https://anonymous.4open.science/r/recovery_aware_struct_prune-5FA5/}.}.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-25T19:56:13.151525+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-25T19:56:13.151702+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	Structured pruning compresses reasoning Large Language Models (LLMs) by removing entire channel groups, but the pruned model must recover through fine-tuning.
5	\citet{selfhealing2025} show that reinforcement learning with verifiable rewards (RLVR) substantially outperforms supervised fine-tuning (SFT) for this recovery.
6	This positions RLVR as the dominant paradigm and creates a testable prediction: a pruning criterion that preserves the model's capacity for RL exploration should yield higher final accuracy.
7	The evidence, however, comes from unstructured magnitude pruning at 96.5\% parameter retention; whether the RLVR advantage holds under structural compression, which removes entire computational units and alters the architecture, remains untested.
8	
9	Our experiments reveal that it does not.
10	On DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} pruned to 20\% MLP channel sparsity, one criterion achieves 4.4 times the peak RL reward of another (CKA-only vs.\ Standard) under GRPO~\citep{shao2024grpo}, yet for each criterion individually, SFT and GRPO recover the model to within 1 percentage point of each other.
11	The pruning criterion determines whether RL training succeeds or collapses, but this stark difference leaves almost no trace in final accuracy.
12	We term this pattern \emph{reward-accuracy decoupling}.
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=\columnwidth]{figures/paper/fig1_dose_response.pdf}
17	\caption{Dose-response of CKA coefficient $\alpha$ on GSM8K at 20\% sparsity. SFT and GRPO curves nearly overlap ($|\Delta| \leq 1.14$\,pp): reward-accuracy decoupling.}
18	\label{fig:dose_response}
19	\end{figure}
20	
21	This disconnect is surprising in light of recent mechanistic work.
22	RL compresses incorrect reasoning paths while SFT expands correct ones~\citep{rlsqueezes2026}.
23	These asymmetric pressures predict that the two paradigms should complement each other, not conv
…[truncated 3047 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-25T19:56:13.151850+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-25T19:56:13.152051+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	To isolate how the pruning criterion affects post-RLVR recovery, we hold everything else constant: a shared structural analysis computes importance and functional overlap scores for all prunable structures, four scoring criteria combine these scores differently to select structures for removal, and an identical two-stage recovery pipeline is applied to every pruned model.
5	The only variable across conditions is which structures are removed (Figure~\ref{fig:method_framework}).
6	
7	\subsection{Preliminaries and Notation}
8	\label{sec:prelim}
9	
10	\paragraph{Structured pruning.}
11	Given a pretrained transformer $\mathcal{M}$ with $L$ layers, structured pruning removes entire computational units (attention heads or MLP channels) to reduce model size while maintaining hardware-friendly dense computation.
12	We denote the set of prunable structures as $\mathcal{H} = \{h_1, h_2, \ldots, h_N\}$.
13	In this work, we focus exclusively on MLP channel group pruning; the formalism below covers attention heads for completeness, but all experiments remove only MLP groups.
14	
15	\paragraph{Grouped Query Attention (GQA).}
16	In GQA architectures~\citep{ainslie2023gqa}, $n_Q$ query heads share $n_{KV}$ key-value heads ($G = n_Q / n_{KV}$ per group).
17	For DeepSeek-R1-Distill-Qwen-7B ($n_Q{=}28$, $n_{KV}{=}4$, $G{=}7$), we treat each GQA group (7 Q heads + 1 KV head) as a single prunable unit.
18	
19	\paragraph{RLVR and GRPO.}
20	Reinforcement Learning with Verifiable Rewards (RLVR) recovers pruned model capabilities using outcome-based rewards from tasks with verifiable answers.
21	We use Group Relative Policy Optimization (GRPO;~\citealp{shao2024grpo}) as the recovery algorithm.
22	
23	\subsection{Structural Analysis}
24	\label{sec:structural_analysis}
25	
26	\begin{figure}[t]
27	    \centering
28	    \includegraphics[width=\columnwidth]{figures/paper/fig_intra_layer_cka.pdf}
29	    \caption{Intra-layer pairwise CKA similarity betwe
…[truncated 9161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-25T19:56:13.152205+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-25T19:56:13.152455+00:00_

1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	\begin{figure*}[t]
6	    \centering
7	    \begin{minipage}[t]{0.38\textwidth}
8	        \centering
9	        \includegraphics[width=\textwidth]{figures/paper/fig2_reward_trajectories.pdf}
10	        \centerline{\small (a) Reward trajectories}
11	    \end{minipage}
12	    \hfill
13	    \begin{minipage}[t]{0.58\textwidth}
14	        \centering
15	        \includegraphics[width=\textwidth]{figures/paper/fig3_collapse_dynamics.pdf}
16	        \centerline{\small (b) $f_0$ and gradient norm diagnostics}
17	    \end{minipage}
18	    \caption{GRPO training dynamics at 20\% sparsity. (a)~Reward trajectories. (b)~$f_0$ (zero-variance batch fraction) and gradient norm diagnostics.}
19	    \label{fig:training_dynamics}
20	\end{figure*}
21	
22	\subsection{Experimental Setup}
23	\label{sec:exp_setup}
24	
25	\input{tables/tab1_recovery_gradient}
26	
27	\paragraph{Base model and evaluation.}
28	We evaluate on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1}, a 7B-parameter reasoning model built on the Qwen2.5 architecture~\citep{qwen2.5} with GQA~\citep{ainslie2023gqa} (Section~\ref{sec:prelim}).
29	Our primary benchmark is GSM8K~\citep{cobbe2021gsm8k} ($N{=}1{,}319$ grade-school math problems; exact-match accuracy).
30	The unpruned model achieves 90.83\% (greedy decoding).
31	
32	\paragraph{Pruning methods.}
33	We compare four pruning criteria at 20\% structured sparsity, all removing 200 of 784 MLP channel groups across 28 layers (${\sim}$1.45B parameters) with identical per-layer capacity floors (${\ge}$40\% retention): \textbf{CKA-only} (Eq.~\ref{eq:cka_only}), \textbf{Standard} (Eq.~\ref{eq:standard}; LLM-Pruner~\citep{llmpruner2023}), \textbf{\rasp{}} at $\alpha{=}1.0$ (Eq.~\ref{eq:score}), and \textbf{Random} (uniform selection; uses TRL's default 512-token generation limit vs.\ 1{,}024 for other methods).
34	See Section~\ref{sec:scoring} and Figure~\ref{fig:pruning_decisions} for scoring details.
35	
36	\paragraph{
…[truncated 10074 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-25T19:56:13.152612+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-25T19:56:13.152756+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Structured pruning of LLMs.}
5	Width pruning (LLM-Pruner~\citep{llmpruner2023}, Bonsai~\citep{bonsai2025}, GRASPrune~\citep{graspprune2026}) removes heads or MLP channels; depth pruning~\citep{shortgpt2024,slicegpt2024} removes entire layers but causes severe reasoning degradation~\citep{shrestha2026layerpruninglimits,llms2lrms2026}.
6	For reasoning models, RESP~\citep{resp2025}, RAC~\citep{rac2025}, and SSGR~\citep{ssgr2025} refine calibration data but retain gradient-based importance scoring.
7	Functional-structure-guided methods cluster neurons~\citep{fang_2025}, apply ICA~\citep{funcnet_2025}, or use inter-layer CKA for depth pruning~\citep{mpruner2024,kornblith2019cka}; we differ in using \emph{intra-layer} CKA between individual structures, optimizing for RL recovery.
8	
9	\paragraph{Pruning-aware recovery.}
10	\citet{selfhealing2025} show RLVR restores pruned reasoning models, outperforming SFT, but evaluate only unstructured pruning at 96.5\% retention; our results suggest this advantage diminishes under fine-grained structural pruning that preserves diversity.
11	Complementary axes include post-pruning scaling~\citep{p2law2025}, recovery data selection~\citep{paser2025}, joint pruning-tuning~\citep{pat2025}, post-hoc compensation~\citep{restorelcc_2025}, iterative prune-tune loops~\citep{boiling_frog_2026}, and post-RLVR compression~\citep{opsd2026}; none study which \emph{pruning criterion} enables RL-based recovery.
12	Concurrent benchmarks~\citep{li2025reasoning_compression,canpruning2025} also do not isolate this variable.
13	
14	\paragraph{RLVR training dynamics.}
15	\citet{rlsqueezes2026} show RLVR \emph{compresses} incorrect trajectories while SFT \emph{expands} correct ones, with training evolving linearly by amplifying early trends~\citep{wang2026linearity}; our results qualify this: the asymmetry manifests as a recovery capacity difference, but the expected accuracy gap vanishes when p
…[truncated 681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-25T19:56:13.152900+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-25T19:56:13.153032+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Whether RLVR outperforms SFT for recovering pruned reasoning models appears to depend on how the model was pruned.
5	Under diversity-preserving pruning at 20--25\% MLP sparsity on Qwen2.5-family models, the two paradigms produce near-identical accuracy (mean $|\Delta| {=} 0.54$\,pp for the four main criteria on GSM8K at 20\%; max $1.8$\,pp across benchmarks and $\alpha$ variants), yet the pruning criterion creates a 4.4$\times$ peak reward gap.
6	At 20\% sparsity, SFT warmup recovers the bulk of accuracy (from $<$2\% post-prune to 51--64\%); GRPO exposes structural capacity differences but contributes minimal additional accuracy, a pattern that persists at 300 steps (Appendix~\ref{sec:appendix_extended}).
7	The non-monotonic $\alpha$ dose-response argues against a layer-distribution confound.
8	A practical implication is that GRPO reward trajectories and $f_0$ diagnostics can serve as probes for evaluating pruning quality, surfacing structural deficiencies that accuracy alone would miss.
9	Rather than running full RL recovery to estimate final accuracy (which our results show remains constant across criteria), a short GRPO probe of ${\sim}$100 steps suffices to diagnose whether a pruned model retains the structural diversity needed for downstream RL fine-tuning or task-specific RL alignment.
10	We discuss broader implications in Appendix~\ref{sec:appendix_discussion}.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-25T19:56:13.153221+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-25T19:56:13.153385+00:00_

1	% Limitations --- required by ACL/EMNLP
2	
3	Our results are validated on two Qwen2.5-family models (7B and 1.5B); generalization to other architecture families (e.g., LLaMA, Mistral) and larger scales remains open.
4	We evaluate on three benchmarks (GSM8K, MATH-500, MBPP); logical, commonsense, and multi-modal reasoning are not covered.
5	\rasp{} $\alpha$ variants and Random use single GRPO seeds, so fine-grained ranking among these should be interpreted with caution.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-25T19:56:13.153507+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/ethics.tex"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-25T19:56:13.153625+00:00_

1	This work uses publicly available models (DeepSeek-R1-Distill-Qwen, Qwen2.5-Math) and established benchmarks (GSM8K, MATH-500, MBPP); no private data or human subjects are involved.
2	Structured pruning reduces model size and inference memory, which can lower the computational cost and energy consumption of deploying large language models.
3	Our research focuses on the technical analysis of pruning criteria and their interaction with reinforcement learning recovery; we do not foresee direct negative societal impacts from this work.
4	All models and datasets used in this work are publicly available under permissive licenses: DeepSeek-R1-Distill-Qwen (MIT), Qwen2.5-Math (Apache 2.0), GSM8K (MIT), MATH (MIT), and MBPP (CC-BY-4.0).
5	We disclose our use of AI assistants in Appendix~\ref{sec:appendix_ai_assistants}.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-25T19:56:13.153743+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-25T19:56:13.154038+00:00_

1	\section{Training Details}
2	\label{sec:appendix_training}
3	
4	Table~\ref{tab:hyperparams} lists the full hyperparameter configurations for both recovery stages described in Section~\ref{sec:exp_setup}. All four pruning criteria share identical SFT and GRPO settings; the only difference is Random's shorter generation limit, inherited from the TRL library default.
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Hyperparameter details for SFT warmup and GRPO recovery stages. All methods share the same GRPO configuration; Random uses the TRL default generation limit (marked with $^\dagger$).}
10	\label{tab:hyperparams}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}lll@{}}
13	\toprule
14	Parameter & SFT & GRPO \\
15	\midrule
16	Learning rate & $2 \times 10^{-5}$ & $1 \times 10^{-6}$ \\
17	Batch size & 1 & 1 \\
18	Gradient accumulation & 8 & 1 \\
19	Max sequence length & 2{,}048 & -- \\
20	Max new tokens & -- & 1{,}024\,$^\dagger$512 \\
21	Optimizer & AdamW & AdamW \\
22	Epochs / Steps & 2 epochs & 100 steps \\
23	KL coefficient $\beta$ & -- & 0.01 \\
24	Sampling temperature & -- & 0.4 \\
25	Num generations per prompt & -- & 8 \\
26	Reward & -- & Binary (exact match) \\
27	Loss formulation & Cross-entropy & DAPO-style clipped \\
28	\texttt{reward\_desert\_patience} & -- & 50 \\
29	\bottomrule
30	\multicolumn{3}{l}{\footnotesize $^\dagger$Random uses TRL default of 512 tokens; all other methods use 1{,}024.} \\
31	\end{tabular}}
32	\end{table}
33	
34	\section{Algorithm}
35	\label{sec:appendix_algo}
36	
37	Algorithm~\ref{alg:rasp} summarizes the complete pruning comparison procedure from Section~\ref{sec:method}: shared structural analysis (importance and CKA overlap computation), criterion-specific scoring (Eqs.~\ref{eq:standard}--\ref{eq:cka_only}), and two-stage recovery (SFT warmup followed by GRPO).
38	
39	\begin{algorithm}[h]
40	\caption{Controlled Pruning Comparison Framework}
41	\label{alg:rasp}
42	\begin{algorithmic}[1]
43	\Require Model $\mathc
…[truncated 26367 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-25T19:56:13.154197+00:00_

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
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
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

_source line 23 · 2026-05-25T19:56:13.154340+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-25T19:56:13.154464+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read all main tex files and tables', 'status': 'in_progress', 'activeForm': 'Reading all main tex files and tables'}, {'content': 'Read all gen_fig*.py scripts for hardcoded data', 'status': 'pending', 'activeForm': 'Reading all gen_fig*.py scripts'}, {'content': 'Extract and classify all numbers', 'status': 'pending', 'activeForm': 'Extracting and classifying all numbers'}, {'content': 'Perform internal consistency checks', 'status': 'pending', 'activeForm': 'Performing internal consistency checks'}, {'content': 'Verify derived computations', 'status': 'pending', 'activeForm': 'Verifying derived computations'}, {'content': 'Write audit report', 'status': 'pending', 'activeForm': 'Writing audit report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read all main tex files and tables', 'status': 'in_progress', 'activeForm': 'Reading all main tex files and tables'}, {'content': 'Read all gen_fig*.py scripts for hardcoded data', 'status': 'pending', 'activeForm': 'Reading all gen_fig*.py scripts'}, {'content': 'Extract and classify all numbers', 'status': 'pending', 'activeForm': 'Extracting and classifying all numbers'}, {'content': 'Perform internal consistency checks', 'status': 'pending', 'activeForm': 'Performing internal consistency checks'}, {'content': 'Verify derived computations', 'status': 'pending', 'activeForm': 'Verifying derived computations'}, {'content': 'Write audit report', 'status': 'pending', 'activeForm': 'Writing audit report'}]"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-25T19:56:13.154601+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-25T19:56:13.154715+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-25T19:56:13.154840+00:00_

1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Recovery capacity spectrum at 20\% sparsity. $f_0$: zero-variance batch fraction. Best in \textbf{bold}.}
5	\label{tab:recovery_gradient}
6	\setlength{\tabcolsep}{5pt}
7	\begin{tabular}{@{}lccc@{}}
8	\toprule
9	Method & Peak Rew.\,$\uparrow$ & Mean Rew.\,$\uparrow$ & Min $f_0$\,$\downarrow$ \\
10	\midrule
11	CKA-only & \textbf{0.354} & \textbf{0.285} & \textbf{0.125} \\
12	Random & 0.190 & 0.164 & 0.300 \\
13	Standard & 0.081 & 0.050 & 0.500 \\
14	\rasp{} ($\alpha{=}1.0$) & 0.061 & 0.031 & 0.675 \\
15	\bottomrule
16	\end{tabular}
17	\end{table}
18	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-25T19:56:13.154956+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-25T19:56:13.155078+00:00_

1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Reward-accuracy decoupling on GSM8K ($N{=}1{,}319$) at 20\% sparsity. $\pm$: multi-seed std. Best in \textbf{bold}.}
5	\label{tab:decoupling}
6	\setlength{\tabcolsep}{4pt}
7	\begin{tabular}{@{}lcccc@{}}
8	\toprule
9	Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) & Peak Rew. \\
10	\midrule
11	Unpruned & \textbf{81.27} & \textbf{81.27} & $\phantom{-}$0.00 & \textbf{0.669} \\
12	\rasp{} ($\alpha{=}2.0$) & 64.97 & 66.11 & $+$1.14 & -- \\
13	CKA-only & 63.91 & 64.39{\scriptsize$\pm$0.19} & $+$0.48 & 0.354 \\
14	Standard & 59.29 & 59.84{\scriptsize$\pm$0.38} & $+$0.55 & 0.081 \\
15	\rasp{} ($\alpha{=}1.0$) & 61.49 & 60.88 & $-$0.61 & 0.061 \\
16	Random & 51.25 & 50.72{\scriptsize$\pm$0.15} & $-$0.53 & 0.190 \\
17	\midrule
18	ShortGPT & 44.73 & 43.37 & $-$1.36 & -- \\
19	\bottomrule
20	\end{tabular}
21	\end{table}
22	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-25T19:56:13.155202+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-25T19:56:13.155353+00:00_

1	\begin{table}[h]
2	\centering
3	\small
4	\caption{MATH-500 out-of-distribution evaluation ($N{=}500$, greedy decoding, \texttt{max\_new\_tokens=2048}). CKA-only and Standard both outperform \rasp{} and Random; the CKA-only--Standard GRPO gap is 0.6\,pp (vs.\ 4.62\,pp on GSM8K), consistent with difficulty and truncation compressing scores toward a floor. Best per section in \textbf{bold}.}
5	\label{tab:math500}
6	\begin{tabular}{@{}lccc@{}}
7	\toprule
8	Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	Dense & \multicolumn{3}{c}{53.0\,$^\dagger$} \\
11	\midrule
12	\multicolumn{4}{l}{\textit{20\% sparsity --- method comparison}} \\
13	CKA-only & \textbf{27.4} & \textbf{27.6} & $+$0.2 \\
14	Standard & 25.6 & 27.0 & $+$1.4 \\
15	\rasp{} ($\alpha{=}1.0$) & 21.6 & 23.0 & $+$1.4 \\
16	Random & 16.6 & 15.0 & $-$1.6 \\
17	\midrule
18	\multicolumn{4}{l}{\textit{20\% sparsity --- $\alpha$ dose-response}} \\
19	$\alpha{=}0.5$ & 26.8 & 26.8 & $+$0.0 \\
20	$\alpha{=}2.0$ & 25.6 & \textbf{27.4} & $+$1.8 \\
21	$\alpha{=}3.0$ & 23.6 & -- & -- \\
22	$\alpha{=}4.0$ & \textbf{27.8} & 27.2 & $-$0.6 \\
23	\midrule
24	\multicolumn{4}{l}{\textit{25\% sparsity}} \\
25	CKA-only & 18.8 & 17.6 & $-$1.2 \\
26	Standard & 15.4 & -- & -- \\
27	\bottomrule
28	\multicolumn{4}{p{0.85\columnwidth}}{\footnotesize $^\dagger$Over half of Dense responses truncated at 2048 tokens (73.6\% at 4096); all pruned models evaluated under the same constraint.}
29	\end{tabular}
30	\end{table}
31	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T19:56:13.155481+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-25T19:56:13.155603+00:00_

1	\begin{table}[h]
2	\centering
3	\small
4	\caption{MBPP code generation accuracy ($N{=}374$, greedy decoding). All fine-grained pruning methods converge near a capability floor (${\sim}$75\% code capability loss vs Dense), limiting differentiation (${\sim}$1\,pp range, within stderr). ShortGPT shows a larger GRPO delta ($+$4.01\,pp) but at the 95\% CI boundary (stderr ${\approx}$1.55\,pp).}
5	\label{tab:mbpp}
6	\begin{tabular}{@{}lccc@{}}
7	\toprule
8	Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	Dense & -- & 53.48 & -- \\
11	\midrule
12	CKA-only 20\% & 12.83 & 14.17 & $+$1.34 \\
13	Standard 20\% & 12.03 & 13.10 & $+$1.07 \\
14	\rasp{} ($\alpha{=}1.0$) 20\% & 11.76 & 13.10 & $+$1.34 \\
15	\midrule
16	ShortGPT 20\%$^\dagger$ & 10.43 & 14.44 & $+$4.01 \\
17	\bottomrule
18	\multicolumn{4}{l}{\footnotesize $^\dagger$Depth pruning; removes entire layers.}
19	\end{tabular}
20	\end{table}
21	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-25T19:56:13.155728+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-25T19:56:13.155850+00:00_

1	\begin{table}[h]
2	\centering
3	\small
4	\caption{CKA scoring stability across calibration sizes. Spearman $\rho$ between structure rankings produced by different calibration set sizes. High correlation ($\rho \geq 0.964$) indicates that CKA-based scoring is robust to calibration data volume.}
5	\label{tab:cka_stability}
6	\begin{tabular}{@{}lcc@{}}
7	\toprule
8	Calibration Sizes & Spearman $\rho$ (min) & Spearman $\rho$ (mean) \\
9	\midrule
10	256 / 512 / 1024 & 0.964 & 0.979 \\
11	\bottomrule
12	\end{tabular}
13	\end{table}
14	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-25T19:56:13.155964+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-25T19:56:13.156082+00:00_

1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Dose-response analysis: effect of CKA coefficient $\alpha$ on GSM8K accuracy ($N{=}1{,}319$) at 20\% MLP channel sparsity. $\alpha{=}0$ reduces to Standard (importance-only); higher $\alpha$ weights representational diversity. Best in \textbf{bold}.}
5	\label{tab:alpha}
6	\begin{tabular}{@{}cccc@{}}
7	\toprule
8	$\alpha$ & SFT Acc.\,(\%) & GRPO Acc.\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	0.5 & 60.73 & 61.18 & $+$0.45 \\
11	1.0 & 61.49 & 60.88 & $-$0.61 \\
12	\textbf{2.0} & \textbf{64.97} & \textbf{66.11} & $+$1.14 \\
13	3.0 & 64.14 & 63.46 & $-$0.68 \\
14	4.0 & 61.94 & 62.77 & $+$0.83 \\
15	\bottomrule
16	\end{tabular}
17	\end{table}
18	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-25T19:56:13.156197+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-25T19:56:13.156331+00:00_

1	\begin{table}[t]
2	\centering
3	\caption{Sparsity cliff at 30\% structured sparsity. All tested pruning criteria collapse, with near-zero accuracy and EOS generation rates below 6\%.}
4	\label{tab:sparsity_cliff}
5	\begin{tabular}{@{}lccc@{}}
6	\toprule
7	Method & $N$ & Acc.\,(\%) & EOS Rate\,(\%) \\
8	\midrule
9	Standard & 200 & 4 & 5.5 \\
10	\rasp{} ($\alpha{=}1.0$) & 200 & 0 & 3.0 \\
11	CKA-only & 500$^\dagger$ & 1.6 & --$^\dagger$ \\
12	\bottomrule
13	\multicolumn{4}{@{}l}{\footnotesize $^\dagger$Terminated early after collapse confirmed; 8/500 correct.}
14	\end{tabular}
15	\end{table}
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-25T19:56:13.156453+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-25T19:56:13.156576+00:00_

1	\begin{table}[h]
2	\centering
3	\small
4	\caption{Cross-scale validation at 20\% sparsity. 7B: DeepSeek-R1-Distill-Qwen-7B (GSM8K mean over 3 seeds for CKA-only and Standard; see Table~\ref{tab:decoupling}). 1.5B: DeepSeek-R1-Distill-Qwen-1.5B (single seed). GSM8K accuracy ($N{=}1{,}319$). 7B reward = peak across 100 GRPO steps (cf.\ Table~\ref{tab:recovery_gradient}); 1.5B reward = mean across training steps.}
5	\label{tab:cross_scale}
6	\resizebox{\columnwidth}{!}{%
7	\begin{tabular}{@{}lcccc@{}}
8	\toprule
9	\multirow{2}{*}{Method} & \multicolumn{2}{c}{7B} & \multicolumn{2}{c}{1.5B} \\
10	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
11	 & Peak Rew. & GSM8K\,(\%) & Rew. & GSM8K\,(\%) \\
12	\midrule
13	CKA-only & \textbf{0.354} & \textbf{64.39} & \textbf{0.238} & \textbf{35.48} \\
14	Standard & 0.081 & 59.84 & 0.084 & 22.29 \\
15	\rasp{} ($\alpha{=}1.0$) & 0.061 & 60.88 & 0.099 & 26.16 \\
16	Random & 0.190 & -- & -- & -- \\
17	\bottomrule
18	\end{tabular}}
19	\end{table}
20	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-25T19:56:13.156693+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-25T19:56:13.156814+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	\usepackage{algorithm}
17	\usepackage[noend]{algpseudocode}
18	\usepackage{enumitem}
19	
20	\newcommand{\rasp}{\textsc{Rasp}}
21	
22	\title{How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM}
23	
24	\author{Anonymous}
25	
26	\begin{document}
27	\maketitle
28	
29	\begin{abstract}
30	\input{abstract}
31	\end{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{method}
36	\input{experiments}
37	\input{conclusion}
38	
39	\section*{Limitations}
40	\input{limitations}
41	
42	\section*{Ethics Statement}
43	\input{ethics}
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{appendix}
49	
50	\end{document}
51	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-25T19:56:13.156937+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read all main tex files and tables', 'status': 'completed', 'activeForm': 'Reading all main tex files and tables'}, {'content': 'Read all gen_fig*.py scripts for hardcoded data', 'status': 'in_progress', 'activeForm': 'Reading all gen_fig*.py scripts'}, {'content': 'Extract and classify all numbers', 'status': 'pending', 'activeForm': 'Extracting and classifying all numbers'}, {'content': 'Perform internal consistency checks', 'status': 'pending', 'activeForm': 'Performing internal consistency checks'}, {'content': 'Verify derived computations', 'status': 'pending', 'activeForm': 'Verifying derived computations'}, {'content': 'Write audit report', 'status': 'pending', 'activeForm': 'Writing audit report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read all main tex files and tables', 'status': 'completed', 'activeForm': 'Reading all main tex files and tables'}, {'content': 'Read all gen_fig*.py scripts for hardcoded data', 'status': 'in_progress', 'activeForm': 'Reading all gen_fig*.py scripts'}, {'content': 'Extract and classify all numbers', 'status': 'pending', 'activeForm': 'Extracting and classifying all numbers'}, {'content': 'Perform internal consistency checks', 'status': 'pending', 'activeForm': 'Performing internal consistency checks'}, {'content': 'Verify derived computations', 'status': 'pending', 'activeForm': 'Verifying derived computations'}, {'content': 'Write audit report', 'status': 'pending', 'activeForm': 'Writing audit report'}]"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-25T19:56:13.157091+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-25T19:56:13.157244+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig1_dose_response.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig1_dose_response.py"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-25T19:56:13.157450+00:00_

1	#!/usr/bin/env python3
2	"""Generate dose-response grouped bar chart for CKA coefficient α (Figure 1)."""
3	
4	import matplotlib
5	matplotlib.use('Agg')
6	import matplotlib.pyplot as plt
7	import numpy as np
8	import os
9	
10	plt.rcParams.update({
11	    'font.family': 'serif',
12	    'font.serif': ['Times New Roman', 'DejaVu Serif'],
13	    'font.size': 6,
14	    'axes.labelsize': 7,
15	    'xtick.labelsize': 6,
16	    'ytick.labelsize': 6,
17	    'legend.fontsize': 6,
18	    'figure.dpi': 300,
19	    'savefig.dpi': 300,
20	    'savefig.bbox': 'tight',
21	    'savefig.pad_inches': 0.02,
22	    'axes.spines.top': False,
23	    'axes.spines.right': False,
24	    'figure.facecolor': 'white',
25	    'axes.facecolor': 'white',
26	    'axes.linewidth': 0.5,
27	    'xtick.major.width': 0.4,
28	    'ytick.major.width': 0.4,
29	})
30	
31	alphas = [0.5, 1.0, 2.0, 3.0, 4.0]
32	sft_acc =  [64.52, 61.49, 64.97, 64.06, 62.02]
33	grpo_acc = [65.05, 60.88, 66.11, 64.59, 62.77]
34	deltas = [g - s for s, g in zip(sft_acc, grpo_acc)]
35	
36	x = np.arange(len(alphas))
37	width = 0.32
38	
39	fig, ax = plt.subplots(figsize=(3.25, 2.0))
40	
41	bars_sft = ax.bar(x - width/2, sft_acc, width, color='#2C3E50', alpha=0.7,
42	                  edgecolor='#2C3E50', linewidth=0.5, label='SFT', zorder=3)
43	bars_grpo = ax.bar(x + width/2, grpo_acc, width, color='#C0392B', alpha=0.7,
44	                   edgecolor='#C0392B', linewidth=0.5, label='GRPO', zorder=3)
45	
46	for i, (sx, gx, d) in enumerate(zip(sft_acc, grpo_acc, deltas)):
47	    top = max(sx, gx)
48	    sign = '+' if d >= 0 else ''
49	    ax.text(x[i], top + 0.4, f'{sign}{d:.2f}', ha='center', va='bottom',
50	            fontsize=5.5, color='#555555')
51	
52	ax.set_xlabel(r'CKA coefficient $\alpha$')
53	ax.set_ylabel('GSM8K Accuracy (%)')
54	ax.set_xticks(x)
55	ax.set_xticklabels([str(a) for a in alphas])
56	ax.set_ylim(58, 69)
57	ax.legend(frameon=False, loc='upper right')
58	
59	ax.axhline(y=64.39, color='#AAAAAA', linestyle=':', 
…[truncated 643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-25T19:56:13.157621+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig1_framework.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig1_framework.py"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-25T19:56:13.157818+00:00_

1	import matplotlib
2	matplotlib.use('Agg')
3	import matplotlib.pyplot as plt
4	import matplotlib.patches as mpatches
5	from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
6	import numpy as np
7	
8	plt.rcParams.update({
9	    'font.family': 'DejaVu Sans',
10	    'font.size': 11,
11	    'figure.dpi': 300,
12	    'savefig.dpi': 300,
13	    'savefig.bbox': 'tight',
14	    'savefig.pad_inches': 0.05,
15	})
16	
17	# Okabe-Ito palette
18	C_STANDARD = '#56B4E9'
19	C_RASP = '#E69F00'
20	C_COLLAPSE = '#D55E00'
21	C_TRADEOFF = '#009E73'
22	C_BG_STANDARD = '#E8F4FD'
23	C_BG_RASP = '#FFF3E0'
24	C_TEXT = '#333333'
25	C_LIGHT_GRAY = '#F5F5F5'
26	
27	fig, ax = plt.subplots(1, 1, figsize=(14, 7))
28	ax.set_xlim(0, 14)
29	ax.set_ylim(0, 7)
30	ax.axis('off')
31	
32	def draw_box(ax, x, y, w, h, text, color, fc=None, fontsize=10, bold=False, text_color=C_TEXT):
33	    if fc is None:
34	        fc = color + '22'
35	    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
36	                         facecolor=fc, edgecolor=color, linewidth=1.8)
37	    ax.add_patch(box)
38	    weight = 'bold' if bold else 'normal'
39	    ax.text(x + w/2, y + h/2, text, ha='center', va='center',
40	            fontsize=fontsize, fontweight=weight, color=text_color,
41	            multialignment='center')
42	    return box
43	
44	def draw_arrow(ax, x1, y1, x2, y2, color='#555555', style='->', lw=1.5):
45	    arrow = FancyArrowPatch((x1, y1), (x2, y2),
46	                            arrowstyle=style, color=color,
47	                            linewidth=lw, mutation_scale=15,
48	                            connectionstyle="arc3,rad=0")
49	    ax.add_patch(arrow)
50	
51	# === Title ===
52	ax.text(7, 6.75, 'Recovery-Aware Structured Pruning (RASP): Framework Overview',
53	        ha='center', va='center', fontsize=13, fontweight='bold', color=C_TEXT)
54	
55	# === STANDARD PIPELINE (top row) ===
56	y_std = 4.8
57	row_h = 1.5
58	ax.text(0.3, y_std + row_h/2, 'Standard\nPipeline', ha='center', 
…[truncated 6557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-25T19:56:13.157985+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig2_reward_accuracy.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig2_reward_accuracy.py"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-25T19:56:13.158157+00:00_

1	import matplotlib
2	matplotlib.use('Agg')
3	import matplotlib.pyplot as plt
4	import numpy as np
5	from pathlib import Path
6	
7	plt.rcParams.update({
8	    'font.family': 'DejaVu Sans',
9	    'font.size': 11,
10	    'axes.titlesize': 13,
11	    'axes.labelsize': 12,
12	    'xtick.labelsize': 10,
13	    'ytick.labelsize': 10,
14	    'legend.fontsize': 10,
15	    'figure.dpi': 300,
16	    'savefig.dpi': 300,
17	    'savefig.bbox': 'tight',
18	    'savefig.pad_inches': 0.05,
19	    'axes.spines.top': False,
20	    'axes.spines.right': False,
21	    'lines.linewidth': 1.8,
22	})
23	
24	COLORS = {
25	    'unpruned': '#0072B2',
26	    'standard': '#56B4E9',
27	    'rasp': '#E69F00',
28	    'collapse': '#D55E00',
29	}
30	
31	# --- Data ---
32	# Unpruned (100 steps)
33	unpruned_steps = np.array([1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
34	unpruned_reward = np.array([0.0, 0.15, 0.32, 0.425, 0.5, 0.55, 0.6, 0.64, 0.669, 0.665, 0.661])
35	
36	# Standard 20% (90 steps)
37	standard_steps = np.array([1, 10, 20, 30, 40, 50, 60, 70, 80, 90])
38	standard_reward = np.array([0.0, 0.03, 0.06, 0.08, 0.096, 0.037, 0.041, 0.05, 0.058, 0.065])
39	
40	# RASP 20% (30 steps)
41	rasp_steps = np.array([1, 5, 10, 15, 20, 25, 30])
42	rasp_reward = np.array([0.0, 0.005, 0.015, 0.028, 0.039, 0.030, 0.021])
43	
44	# Accuracy data (GSM8K, N=1319)
45	models = ['Unpruned', 'Standard\n20%', 'RASP\n20%']
46	sft_acc = [81.27, 59.29, 61.49]
47	grpo_acc = [81.27, 58.91, 61.87]
48	deltas = [0.00, -0.38, +0.38]
49	
50	# --- Figure ---
51	fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5), gridspec_kw={'width_ratios': [1.3, 1]})
52	
53	# Panel (a): Reward curves
54	ax1.plot(unpruned_steps, unpruned_reward, color=COLORS['unpruned'], marker='o', markersize=4, label='Unpruned')
55	ax1.plot(standard_steps, standard_reward, color=COLORS['standard'], marker='s', markersize=4, label='Standard 20%')
56	ax1.plot(rasp_steps, rasp_reward, color=COLORS['rasp'], marker='^', markersize=4, label='RASP 20%')
57	
58
…[truncated 2230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-25T19:56:13.158341+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper && grep -l \"fig2_reward_accuracy\\|fig1_method_framework\\|fig1_framework\" *.tex tables/*.tex 2>/dev/null",
  "description": "Check which figures are referenced"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper && grep -l \"fig2_reward_accuracy\\|fig1_method_framework\\|fig1_framework\" *.tex tables/*.tex 2>/dev/null",
    "description": "Check which figures are referenced"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-25T19:56:13.158468+00:00_

introduction.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-25T19:56:13.158581+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "includegraphics|fig.*\\.pdf|fig.*\\.png",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper",
  "output_mode": "content",
  "-n": "True",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Grep",
  "tool_args": {
    "pattern": "includegraphics|fig.*\\.pdf|fig.*\\.png",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper",
    "output_mode": "content",
    "-n": "True",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-25T19:56:13.158705+00:00_

appendix.tex:303:    \includegraphics[width=0.75\columnwidth]{figures/paper/fig_appendix_kl.pdf}
experiments.tex:9:        \includegraphics[width=\textwidth]{figures/paper/fig2_reward_trajectories.pdf}
experiments.tex:15:        \includegraphics[width=\textwidth]{figures/paper/fig3_collapse_dynamics.pdf}
experiments.tex:67:    \includegraphics[width=\columnwidth]{figures/paper/fig_sft_grpo_scatter.pdf}
experiments.tex:101:    \includegraphics[width=\textwidth]{figures/paper/fig4_cka_heatmap.pdf}
experiments.tex:108:    \includegraphics[width=\textwidth]{figures/paper/fig5_extended_training.pdf}
introduction.tex:16:\includegraphics[width=\columnwidth]{figures/paper/fig1_dose_response.pdf}
introduction.tex:42:\includegraphics[width=\textwidth]{figures/paper/fig1_method_framework.pdf}
method.tex:28:    \includegraphics[width=\columnwidth]{figures/paper/fig_intra_layer_cka.pdf}
method.tex:114:    \includegraphics[width=\columnwidth]{figures/paper/fig_pruning_decisions.png}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-25T19:56:13.158836+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/figures/paper/ 2>/dev/null",
  "description": "Check figures in docs/paper/figures/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/figures/paper/ 2>/dev/null",
    "description": "Check figures in docs/paper/figures/paper"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-25T19:56:13.158954+00:00_

fig1_dose_response.pdf
fig1_dose_response.png
fig1_framework.pdf
fig1_framework.png
fig1_method_framework.pdf
fig1_method_framework.png
fig2_reward_trajectories.pdf
fig2_reward_trajectories.png
fig3_collapse_dynamics.pdf
fig3_collapse_dynamics.png
fig4_cka_heatmap.pdf
fig4_cka_heatmap.png
fig5_extended_training.pdf
fig5_extended_training.png
fig_appendix_kl.pdf
fig_appendix_kl.png
fig_intra_layer_cka.pdf
fig_intra_layer_cka.png
fig_pruning_decisions.pdf
fig_pruning_decisions.png
fig_sft_grpo_scatter.pdf
fig_sft_grpo_scatter.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-25T19:56:13.159079+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig2_reward_trajectories.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig2_reward_trajectories.py"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-25T19:56:13.159220+00:00_

1	#!/usr/bin/env python3
2	"""Generate reward trajectories (Figure 5a in combined training dynamics figure)."""
3	
4	import matplotlib
5	matplotlib.use('Agg')
6	import matplotlib.pyplot as plt
7	import numpy as np
8	import os
9	
10	plt.rcParams.update({
11	    'font.family': 'serif',
12	    'font.serif': ['Times New Roman', 'DejaVu Serif'],
13	    'font.size': 4,
14	    'axes.labelsize': 4.5,
15	    'xtick.labelsize': 3.5,
16	    'ytick.labelsize': 3.5,
17	    'legend.fontsize': 3.5,
18	    'figure.dpi': 300,
19	    'savefig.dpi': 300,
20	    'savefig.bbox': 'tight',
21	    'savefig.pad_inches': 0.02,
22	    'axes.spines.top': False,
23	    'axes.spines.right': False,
24	    'figure.facecolor': 'white',
25	    'axes.facecolor': 'white',
26	    'axes.linewidth': 0.5,
27	    'xtick.major.width': 0.4,
28	    'ytick.major.width': 0.4,
29	})
30	
31	COLORS = {
32	    'cka_only': '#2C3E50',
33	    'standard': '#C0392B',
34	    'random': '#7F8C8D',
35	    'rasp': '#27AE60',
36	}
37	
38	data = {
39	    'Unpruned': {
40	        'steps':  [30, 40, 50, 60, 70, 80, 90, 100],
41	        'reward': [0.4250, 0.5381, 0.5894, 0.6469, 0.6031, 0.6694, 0.5644, 0.6612],
42	        'color': '#555555', 'ls': '-', 'lw': 1.0,
43	    },
44	    'CKA-only (20%)': {
45	        'steps':  [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
46	        'reward': [0.2531, 0.2181, 0.2500, 0.2344, 0.3544, 0.2994, 0.3075, 0.3419, 0.2419, 0.3444],
47	        'color': COLORS['cka_only'], 'ls': '-', 'lw': 1.0,
48	    },
49	    'Random (20%)': {
50	        'steps':  [10, 20, 30, 40, 50, 60, 70, 80, 90],
51	        'reward': [0.161, 0.142, 0.166, 0.145, 0.175, 0.184, 0.190, 0.142, 0.173],
52	        'color': COLORS['random'], 'ls': '--', 'lw': 1.0,
53	    },
54	    'Standard (20%)': {
55	        'steps':  [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
56	        'reward': [0.0513, 0.0556, 0.0669, 0.0813, 0.0188, 0.0431, 0.0469, 0.0456, 0.0306, 0.0538],
57	        'color': COLORS['standard'], 'ls': '-.', 'lw': 1.0,
58	    
…[truncated 1350 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-25T19:56:13.159383+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig3_collapse_dynamics.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig3_collapse_dynamics.py"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-25T19:56:13.159536+00:00_

1	#!/usr/bin/env python3
2	"""Generate f0 and gradient norm panels (Figure 5b in combined training dynamics figure)."""
3	
4	import matplotlib
5	matplotlib.use('Agg')
6	import matplotlib.pyplot as plt
7	import numpy as np
8	import os
9	
10	plt.rcParams.update({
11	    'font.family': 'serif',
12	    'font.serif': ['Times New Roman', 'DejaVu Serif'],
13	    'font.size': 4,
14	    'axes.labelsize': 4.5,
15	    'xtick.labelsize': 3.5,
16	    'ytick.labelsize': 3.5,
17	    'legend.fontsize': 3.5,
18	    'figure.dpi': 300,
19	    'savefig.dpi': 300,
20	    'savefig.bbox': 'tight',
21	    'savefig.pad_inches': 0.02,
22	    'axes.spines.top': False,
23	    'axes.spines.right': False,
24	    'figure.facecolor': 'white',
25	    'axes.facecolor': 'white',
26	    'axes.linewidth': 0.5,
27	    'xtick.major.width': 0.4,
28	    'ytick.major.width': 0.4,
29	})
30	
31	COLORS = {
32	    'cka_only': '#2C3E50',
33	    'standard': '#C0392B',
34	    'random': '#7F8C8D',
35	    'rasp': '#27AE60',
36	}
37	
38	methods = {
39	    'CKA-only': {
40	        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
41	        'frac_zero': [0.175, 0.200, 0.200, 0.350, 0.150, 0.200, 0.125, 0.250, 0.300, 0.200],
42	        'grad_norm': [1.8906, 1.2500, 1.1016, 0.9844, 1.9766, 3.7500, 1.1641, 2.6719, 1.2188, 1.4141],
43	        'color': COLORS['cka_only'], 'ls': '-',
44	    },
45	    'Random': {
46	        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90],
47	        'frac_zero': [0.300, 0.325, 0.325, 0.350, 0.300, 0.350, 0.300, 0.350, 0.325],
48	        'grad_norm': [3.75, 8.62, 3.67, 4.20, 5.10, 3.80, 5.50, 4.00, 3.90],
49	        'color': COLORS['random'], 'ls': '--',
50	    },
51	    'Standard': {
52	        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
53	        'frac_zero': [0.500, 0.625, 0.500, 0.500, 0.575, 0.550, 0.575, 0.550, 0.550, 0.550],
54	        'grad_norm': [6.6250, 2.9531, 2.1250, 0.7969, 1.8594, 2.1875, 2.2969, 1.6953, 0.0173, 2.4062],
55	        'color': COLORS['standard'], 'ls': '-
…[truncated 2129 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-25T19:56:13.159692+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig4_cka_heatmap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig4_cka_heatmap.py"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-25T19:56:13.159838+00:00_

1	#!/usr/bin/env python3
2	"""Generate CKA heatmap bar chart (Figure 7 in paper)."""
3	
4	import matplotlib
5	matplotlib.use('Agg')
6	import matplotlib.pyplot as plt
7	import numpy as np
8	import os
9	
10	plt.rcParams.update({
11	    'font.family': 'serif',
12	    'font.serif': ['Times New Roman', 'DejaVu Serif'],
13	    'font.size': 4,
14	    'axes.labelsize': 4.5,
15	    'xtick.labelsize': 3.5,
16	    'ytick.labelsize': 3.5,
17	    'axes.titlesize': 4.5,
18	    'figure.dpi': 300,
19	    'savefig.dpi': 300,
20	    'savefig.bbox': 'tight',
21	    'savefig.pad_inches': 0.02,
22	    'axes.spines.top': False,
23	    'axes.spines.right': False,
24	    'figure.facecolor': 'white',
25	    'axes.facecolor': 'white',
26	    'axes.linewidth': 0.5,
27	    'xtick.major.width': 0.4,
28	    'ytick.major.width': 0.4,
29	})
30	
31	COLORS = {
32	    'cka_only': '#2C3E50',
33	    'standard': '#C0392B',
34	    'random': '#7F8C8D',
35	    'rasp': '#27AE60',
36	}
37	
38	layers = np.arange(28)
39	
40	cka_only_diag = np.array([0.992078, 0.970804, 0.975216, 0.404565, 0.625708, 0.623903, 0.598962, 0.533124, 0.443967, 0.379374, 0.391774, 0.580886, 0.592159, 0.624592, 0.650729, 0.693671, 0.624036, 0.607008, 0.636153, 0.541262, 0.500812, 0.504471, 0.503854, 0.536129, 0.593986, 0.664982, 0.866145, 0.706587])
41	standard_diag = np.array([0.991821, 0.97916, 0.975323, 0.992554, 0.956368, 0.934576, 0.929565, 0.923715, 0.924731, 0.908191, 0.911368, 0.8923, 0.889276, 0.884304, 0.880501, 0.885459, 0.879751, 0.878502, 0.886264, 0.873357, 0.879117, 0.865639, 0.852384, 0.849021, 0.8412, 0.876013, 0.92356, 0.845257])
42	random_diag   = np.array([0.995953, 0.983455, 0.989856, 0.994252, 0.991933, 0.985995, 0.985967, 0.983163, 0.979579, 0.971516, 0.972551, 0.961018, 0.952727, 0.950374, 0.94448, 0.943773, 0.93139, 0.922787, 0.928291, 0.913079, 0.880656, 0.840093, 0.80336, 0.766821, 0.768002, 0.815259, 0.909149, 0.785565])
43	rasp_diag     = np.array([0.991693, 0.975358, 0.974914, 0.993405, 0.960868, 0.934946
…[truncated 1539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-25T19:56:13.159990+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport numpy as np\ncka_only_diag = np.array([0.992078, 0.970804, 0.975216, 0.404565, 0.625708, 0.623903, 0.598962, 0.533124, 0.443967, 0.379374, 0.391774, 0.580886, 0.592159, 0.624592, 0.650729, 0.693671, 0.624036, 0.607008, 0.636153, 0.541262, 0.500812, 0.504471, 0.503854, 0.536129, 0.593986, 0.664982, 0.866145, 0.706587])\nstandard_diag = np.array([0.991821, 0.97916, 0.975323, 0.992554, 0.956368, 0.934576, 0.929565, 0.923715, 0.924731, 0.908191, 0.911368, 0.8923, 0.889276, 0.884304, 0.880501, 0.885459, 0.879751, 0.878502, 0.886264, 0.873357, 0.879117, 0.865639, 0.852384, 0.849021, 0.8412, 0.876013, 0.92356, 0.845257])\nrandom_diag   = np.array([0.995953, 0.983455, 0.989856, 0.994252, 0.991933, 0.985995, 0.985967, 0.983163, 0.979579, 0.971516, 0.972551, 0.961018, 0.952727, 0.950374, 0.94448, 0.943773, 0.93139, 0.922787, 0.928291, 0.913079, 0.880656, 0.840093, 0.80336, 0.766821, 0.768002, 0.815259, 0.909149, 0.785565])\nrasp_diag     = np.array([0.991693, 0.975358, 0.974914, 0.993405, 0.960868, 0.934946, 0.933927, 0.922086, 0.921308, 0.90173, 0.905182, 0.865596, 0.851913, 0.850003, 0.847234, 0.852437, 0.845246, 0.843156, 0.850639, 0.842069, 0.864349, 0.849892, 0.825763, 0.804426, 0.798232, 0.84092, 0.896333, 0.757363])\nprint('CKA-only mean:', round(cka_only_diag.mean(), 4))\nprint('Standard mean:', round(standard_diag.mean(), 4))\nprint('Random mean:', round(random_diag.mean(), 4))\nprint('RASP mean:', round(rasp_diag.mean(), 4))\n\"\n",
  "description": "Compute CKA heatmap means"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport numpy as np\ncka_only_diag = np.array([0.992078, 0.970804, 0.975216, 0.404565, 0.625708, 0.623903, 0.598962, 0.533124, 0.443967, 0.379374, 0.391774, 0.580886, 0.592159, 0.624592, 0.650729, 0.693671, 0.624036, 0.607008, 0.636153, 0.541262, 0.500812, 0.504471, 0.503854, 0.536129, 0.593986, 0.664982, 0.866145, 0.706587])\nstandard_diag = np.array([0.991821, 0.97916, 0.975323, 0.992554, 0.956368, 0.934576, 0.929565, 0.923715, 0.924731, 0.908191, 0.911368, 0.8923, 0.889276, 0.884304, 0.880501, 0.885459, 0.879751, 0.878502, 0.886264, 0.873357, 0.879117, 0.865639, 0.852384, 0.849021, 0.8412, 0.876013, 0.92356, 0.845257])\nrandom_diag   = np.array([0.995953, 0.983455, 0.989856, 0.994252, 0.991933, 0.985995, 0.985967, 0.983163, 0.979579, 0.971516, 0.972551, 0.961018, 0.952727, 0.950374, 0.94448, 0.943773, 0.93139, 0.922787, 0.928291, 0.913079, 0.880656, 0.840093, 0.80336, 0.766821, 0.768002, 0.815259, 0.909149, 0.785565])\nrasp_diag     = np.array([0.991693, 0.975358, 0.974914, 0.993405, 0.960868, 0.934946, 0.933927, 0.922086, 0.921308, 0.90173, 0.905182, 0.865596, 0.851913, 0.850003, 0.847234, 0.852437, 0.845246, 0.843156, 0.850639, 0.842069, 0.864349, 0.849892, 0.825763, 0.804426, 0.798232, 0.84092, 0.896333, 0.757363])\nprint('CKA-only mean:', round(cka_only_diag.mean(), 4))\nprint('Standard mean:', round(standard_diag.mean(), 4))\nprint('Random mean:', round(random_diag.mean(), 4))\nprint('RASP mean:', round(rasp_diag.mean(), 4))\n\"\n",
    "description": "Compute CKA heatmap means"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-25T19:56:13.160124+00:00_

CKA-only mean: 0.6202
Standard mean: 0.9039
Random mean: 0.9233
RASP mean: 0.8822

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-25T19:56:13.160250+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig5_extended_training.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig5_extended_training.py"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-25T19:56:13.160422+00:00_

1	#!/usr/bin/env python3
2	"""Generate extended 300-step training figure (Figure 8 in paper)."""
3	
4	import matplotlib
5	matplotlib.use('Agg')
6	import matplotlib.pyplot as plt
7	import numpy as np
8	import os
9	
10	plt.rcParams.update({
11	    'font.family': 'serif',
12	    'font.serif': ['Times New Roman', 'DejaVu Serif'],
13	    'font.size': 4,
14	    'axes.labelsize': 4.5,
15	    'xtick.labelsize': 3.5,
16	    'ytick.labelsize': 3.5,
17	    'legend.fontsize': 3.5,
18	    'figure.dpi': 300,
19	    'savefig.dpi': 300,
20	    'savefig.bbox': 'tight',
21	    'savefig.pad_inches': 0.02,
22	    'axes.spines.top': False,
23	    'axes.spines.right': False,
24	    'figure.facecolor': 'white',
25	    'axes.facecolor': 'white',
26	    'axes.linewidth': 0.5,
27	    'xtick.major.width': 0.4,
28	    'ytick.major.width': 0.4,
29	})
30	
31	COLORS = {
32	    'cka_only': '#2C3E50',
33	    'standard': '#C0392B',
34	}
35	
36	standard_steps = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
37	                  150, 200, 250, 300]
38	standard_reward = [0.0513, 0.0556, 0.0669, 0.0813, 0.0188, 0.0431,
39	                   0.0469, 0.0456, 0.0306, 0.0538,
40	                   0.055, 0.054, 0.058, 0.0562]
41	standard_f0 = [0.500, 0.625, 0.500, 0.500, 0.575, 0.550,
42	               0.575, 0.550, 0.550, 0.550,
43	               0.530, 0.540, 0.520, 0.525]
44	
45	cka_steps = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
46	             110, 120, 130, 260, 270, 280, 290, 300]
47	cka_reward = [0.2531, 0.2181, 0.2500, 0.2344, 0.3544, 0.2994,
48	              0.3075, 0.3419, 0.2419, 0.3444,
49	              0.3206, 0.2562, 0.2963, 0.3900, 0.3188, 0.4444, 0.2238, 0.3075]
50	cka_f0 = [0.175, 0.200, 0.200, 0.350, 0.150, 0.200, 0.125, 0.250, 0.300, 0.200,
51	           0.175, 0.225, 0.200, 0.125, 0.225, 0.100, 0.250, 0.275]
52	
53	fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(3.25, 2.6))
54	plt.subplots_adjust(hspace=0.55)
55	
56	common_kw = dict(marker='o', markersize=1.8, markerfacecolor='white', mark
…[truncated 2475 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-25T19:56:13.160576+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig_appendix_kl.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig_appendix_kl.py"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-25T19:56:13.160714+00:00_

1	import matplotlib
2	matplotlib.use('Agg')
3	import matplotlib.pyplot as plt
4	import numpy as np
5	
6	plt.rcParams.update({
7	    'font.family': 'DejaVu Sans',
8	    'font.size': 11,
9	    'axes.titlesize': 11,
10	    'axes.titleweight': 'bold',
11	    'axes.labelsize': 10,
12	    'xtick.labelsize': 9,
13	    'ytick.labelsize': 9,
14	    'legend.fontsize': 9,
15	    'figure.dpi': 300,
16	    'savefig.dpi': 300,
17	    'savefig.bbox': 'tight',
18	    'savefig.pad_inches': 0.05,
19	    'axes.spines.top': False,
20	    'axes.spines.right': False,
21	})
22	
23	# All data verified from W&B or server logs (2026-05-18)
24	methods = {
25	    'CKA-only': {
26	        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
27	        'kl': [0.001206, 0.001232, 0.001671, 0.001500, 0.001567, 0.001579, 0.001558, 0.001701, 0.001508, 0.001609],
28	        'color': '#009E73', 'ls': '-',
29	    },
30	    'Random': {
31	        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90],
32	        'kl': [0.0042, 0.0047, 0.0046, 0.0044, 0.0045, 0.0043, 0.0046, 0.0045, 0.0044],
33	        'color': '#E69F00', 'ls': '--',
34	    },
35	    'Standard': {
36	        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
37	        'kl': [0.002187, 0.002394, 0.002652, 0.002662, 0.002266, 0.002454, 0.002444, 0.002470, 0.002462, 0.003229],
38	        'color': '#CC79A7', 'ls': '-',
39	    },
40	    'RASP': {
41	        'steps': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
42	        'kl': [0.0008379, 0.0009728, 0.001022, 0.0007673, 0.001035, 0.000894, 0.001119, 0.0008899, 0.001043, 0.0008991],
43	        'color': '#D55E00', 'ls': '-',
44	    },
45	}
46	
47	fig, ax = plt.subplots(figsize=(5.5, 3.5))
48	
49	for name, d in methods.items():
50	    ax.plot(d['steps'], d['kl'], color=d['color'], linestyle=d['ls'],
51	            marker='o', markersize=4, linewidth=1.8, label=name, zorder=3)
52	
53	ax.set_xlabel('Training Step')
54	ax.set_ylabel('KL Divergence')
55	ax.set_xlim(0, 105)
56	ax.set_xticks(np.arange(0, 110, 2
…[truncated 412 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-25T19:56:13.160858+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig_sft_grpo_scatter.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig_sft_grpo_scatter.py"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-25T19:56:13.161071+00:00_

1	#!/usr/bin/env python3
2	"""Generate SFT vs GRPO accuracy scatter plot (Figure 4 in paper)."""
3	
4	import matplotlib
5	matplotlib.use('Agg')
6	import matplotlib.pyplot as plt
7	import numpy as np
8	import os
9	
10	plt.rcParams.update({
11	    'font.family': 'serif',
12	    'font.serif': ['Times New Roman', 'DejaVu Serif'],
13	    'font.size': 10,
14	    'axes.labelsize': 11,
15	    'xtick.labelsize': 10,
16	    'ytick.labelsize': 10,
17	    'legend.fontsize': 8.5,
18	    'figure.dpi': 300,
19	    'savefig.dpi': 300,
20	    'savefig.bbox': 'tight',
21	    'savefig.pad_inches': 0.05,
22	    'axes.spines.top': False,
23	    'axes.spines.right': False,
24	    'figure.facecolor': 'white',
25	    'axes.facecolor': 'white',
26	})
27	
28	COLORS = {
29	    'cka_only': '#2C3E50',
30	    'standard': '#C0392B',
31	    'random': '#7F8C8D',
32	    'rasp': '#27AE60',
33	}
34	
35	data_20pct = {
36	    'CKA-only 20%':    {'sft': 63.91, 'grpo': 64.39, 'marker': 'o', 'color': COLORS['cka_only'], 'size': 80},
37	    'Standard 20%':    {'sft': 59.29, 'grpo': 59.84, 'marker': 's', 'color': COLORS['standard'], 'size': 80},
38	    r'RASP ($\alpha$=1) 20%': {'sft': 61.49, 'grpo': 60.88, 'marker': '^', 'color': COLORS['rasp'], 'size': 80},
39	    'Random 20%':      {'sft': 51.25, 'grpo': 50.72, 'marker': 'D', 'color': COLORS['random'], 'size': 80},
40	}
41	
42	alpha_variants = {
43	    r'$\alpha$=0.5': {'sft': 60.73, 'grpo': 61.18},
44	    r'$\alpha$=2.0': {'sft': 64.97, 'grpo': 66.11},
45	    r'$\alpha$=3.0': {'sft': 64.14, 'grpo': 63.46},
46	    r'$\alpha$=4.0': {'sft': 61.94, 'grpo': 62.77},
47	}
48	
49	cross_sparsity_cka = {
50	    'CKA 15%': {'sft': 72.18, 'grpo': 72.76},
51	    'CKA 25%': {'sft': 60.12, 'grpo': 59.59},
52	}
53	
54	cross_sparsity_std = {
55	    'Std 15%': {'sft': 66.49, 'grpo': 65.56},
56	    'Std 25%': {'sft': 50.87, 'grpo': 51.86},
57	}
58	
59	shortgpt = {'sft': 44.73, 'grpo': 43.37}
60	unpruned = {'sft': 81.27, 'grpo': 81.27}
61	
62	fig, ax = plt.subplots(1, 1, fi
…[truncated 2803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-25T19:56:13.161366+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_*.py",
  "description": "List all generation scripts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_*.py",
    "description": "List all generation scripts"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-25T19:56:13.161522+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig1_dose_response.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig1_framework.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig2_reward_accuracy.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig2_reward_trajectories.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig3_collapse_dynamics.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig4_cka_heatmap.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig5_extended_training.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig_appendix_kl.py
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/figures/paper/gen_fig_sft_grpo_scatter.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-25T19:56:13.161711+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read all main tex files and tables', 'status': 'completed', 'activeForm': 'Reading all main tex files and tables'}, {'content': 'Read all gen_fig*.py scripts for hardcoded data', 'status': 'completed', 'activeForm': 'Reading all gen_fig*.py scripts'}, {'content': 'Extract and classify all numbers', 'status': 'in_progress', 'activeForm': 'Extracting and classifying all numbers'}, {'content': 'Perform internal consistency checks', 'status': 'in_progress', 'activeForm': 'Performing internal consistency checks'}, {'content': 'Verify derived computations', 'status': 'in_progress', 'activeForm': 'Verifying derived computations'}, {'content': 'Write audit report', 'status': 'pending', 'activeForm': 'Writing audit report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read all main tex files and tables', 'status': 'completed', 'activeForm': 'Reading all main tex files and tables'}, {'content': 'Read all gen_fig*.py scripts for hardcoded data', 'status': 'completed', 'activeForm': 'Reading all gen_fig*.py scripts'}, {'content': 'Extract and classify all numbers', 'status': 'in_progress', 'activeForm': 'Extracting and classifying all numbers'}, {'content': 'Perform internal consistency checks', 'status': 'in_progress', 'activeForm': 'Performing internal consistency checks'}, {'content': 'Verify derived computations', 'status': 'in_progress', 'activeForm': 'Verifying derived computations'}, {'content': 'Write audit report', 'status': 'pending', 'activeForm': 'Writing audit report'}]"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-25T19:56:13.161859+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-25T19:56:13.161996+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Verify various derived calculations\n# 1. Conclusion mean |Δ|\ndeltas = [0.48, 0.55, 0.61, 0.53]\nprint('mean |Δ| =', sum(deltas)/4)\n# 2. 4.4× peak reward gap\nprint('peak reward ratio =', round(0.354/0.081, 2))\n# 3. CKA-Standard gap 20%\nprint('20% gap:', round(64.39-59.84, 2))\n# 4. CKA-Standard gap 15%\nprint('15% gap:', round(72.76-65.56, 2))\n# 5. SFT 15% gap\nprint('SFT 15% gap:', round(72.18-66.49, 2))\n# 6. Amplification at 15%\nprint('15% GRPO amp:', round(7.20-5.69, 2))\n# 7. 5.5x at step 300\nprint('300-step ratio:', round(0.308/0.056, 2))\n# 8. Mean of Random deltas\nprint('Random:', 51.25-50.57, 51.25-50.72, 51.25-50.87)\n# 9. Standard SFT decline rates\nprint('Std decline 15->20:', 66.49-59.29, '20->25:', 59.29-50.87)\nprint('CKA decline 15->20:', 72.18-63.91, '20->25:', 63.91-60.12)\n# 10. 80.1% retention\nprint('80.1% check:', round(72.76/90.83*100, 2))\n# 11. 30.5pp cross-model\nprint('30.5 pp:', round(51.50-21.00, 2))\n# 12. 4.6 pp primary\nprint('4.6 pp:', round(64.39-59.84, 2))\n# 13. α=3 drop from α=2 peak\nprint('alpha 2->3 drop:', round(66.11-63.46, 2))\n# 14. α=2 over CKA-only\nprint('alpha 2 vs CKA:', round(66.11-64.39, 2))\n# 15. MBPP mean delta\nprint('MBPP mean delta:', round((1.34+1.07+1.34)/3, 3))\n# 16. ShortGPT MBPP\nprint('ShortGPT MBPP:', round(14.44-10.43, 2))\n# 17. ShortGPT GSM8K\nprint('ShortGPT GSM8K:', round(43.37-44.73, 2))\n# 18. Inference improvements\nprint('TTFT improve %:', round((20.1-16.4)/20.1*100, 2))\nprint('TPS decrease %:', round((72.0-58.3)/72.0*100, 2))\nprint('per-token increase %:', round((16.7-13.9)/13.9*100, 2))\n# 19. Param reduction\nprint('Param reduction:', round((7.62-6.16)/7.62*100, 2), '%')\nprint('Pruned params:', round(7.62-6.16, 2), 'B')\n# 20. Math500 alpha SFT range\nprint('M500 alpha SFT range:', max([26.8,21.6,25.6,23.6,27.8])-min([26.8,21.6,25.6,23.6,27.8]))\n# 21. 9.56 pp gap\nprint('Unpruned 9.56 pp:', round(90.83-81.27, 2))\n# 22. 200/784\nprint('200/784 =', round(200/784*100, 2), '%')\n# 23. CKA-only seed range\nprint('CKA seed range:', 64.59-64.22)\n# 24. Standard seed range\nprint('Std seed range:', 60.20-59.44)\n# 25. fig1_dose_response deltas\nsft = [64.52, 61.49, 64.97, 64.06, 62.02]\ngrpo = [65.05, 60.88, 66.11, 64.59, 62.77]\nprint('fig1 deltas:', [round(g-s, 2) for s,g in zip(sft, grpo)])\nprint('table3 deltas:', [round(g-s, 2) for s,g in zip([60.73,61.49,64.97,64.14,61.94], [61.18,60.88,66.11,63.46,62.77])])\n# 26. seed-by-seed standard\nprint('Standard per-seed (recomputed):', 59.21+0.23, 59.29+0.68, 59.29+0.99)\n# 27. RASP +1.72\nprint('RASP α=2 over CKA:', round(66.11-64.39, 2))\n# 28. 0.08 SFT diff\nprint('SFT 0.08 diff:', round(59.29-59.21, 2))\n\"\n",
  "description": "Verify derived calculations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Verify various derived calculations\n# 1. Conclusion mean |Δ|\ndeltas = [0.48, 0.55, 0.61, 0.53]\nprint('mean |Δ| =', sum(deltas)/4)\n# 2. 4.4× peak reward gap\nprint('peak reward ratio =', round(0.354/0.081, 2))\n# 3. CKA-Standard gap 20%\nprint('20% gap:', round(64.39-59.84, 2))\n# 4. CKA-Standard gap 15%\nprint('15% gap:', round(72.76-65.56, 2))\n# 5. SFT 15% gap\nprint('SFT 15% gap:', round(72.18-66.49, 2))\n# 6. Amplification at 15%\nprint('15% GRPO amp:', round(7.20-5.69, 2))\n# 7. 5.5x at step 300\nprint('300-step ratio:', round(0.308/0.056, 2))\n# 8. Mean of Random deltas\nprint('Random:', 51.25-50.57, 51.25-50.72, 51.25-50.87)\n# 9. Standard SFT decline rates\nprint('Std decline 15->20:', 66.49-59.29, '20->25:', 59.29-50.87)\nprint('CKA decline 15->20:', 72.18-63.91, '20->25:', 63.91-60.12)\n# 10. 80.1% retention\nprint('80.1% check:', round(72.76/90.83*100, 2))\n# 11. 30.5pp cross-model\nprint('30.5 pp:', round(51.50-21.00, 2))\n# 12. 4.6 pp primary\nprint('4.6 pp:', round(64.39-59.84, 2))\n# 13. α=3 drop from α=2 peak\nprint('alpha 2->3 drop:', round(66.11-63.46, 2))\n# 14. α=2 over CKA-only\nprint('alpha 2 vs CKA:', round(66.11-64.39, 2))\n# 15. MBPP mean delta\nprint('MBPP mean delta:', round((1.34+1.07+1.34)/3, 3))\n# 16. ShortGPT MBPP\nprint('ShortGPT MBPP:', round(14.44-10.43, 2))\n# 17. ShortGPT GSM8K\nprint('ShortGPT GSM8K:', round(43.37-44.73, 2))\n# 18. Inference improvements\nprint('TTFT improve %:', round((20.1-16.4)/20.1*100, 2))\nprint('TPS decrease %:', round((72.0-58.3)/72.0*100, 2))\nprint('per-token increase %:', round((16.7-13.9)/13.9*100, 2))\n# 19. Param reduction\nprint('Param reduction:', round((7.62-6.16)/7.62*100, 2), '%')\nprint('Pruned params:', round(7.62-6.16, 2), 'B')\n# 20. Math500 alpha SFT range\nprint('M500 alpha SFT range:', max([26.8,21.6,25.6,23.6,27.8])-min([26.8,21.6,25.6,23.6,27.8]))\n# 21. 9.56 pp gap\nprint('Unpruned 9.56 pp:', round(90.83-81.27, 2))\n# 22. 200/784\nprint('200/784 =', round(200/784*100, 2), '%')\n# 23. CKA-only seed range\nprint('CKA seed range:', 64.59-64.22)\n# 24. Standard seed range\nprint('Std seed range:', 60.20-59.44)\n# 25. fig1_dose_response deltas\nsft = [64.52, 61.49, 64.97, 64.06, 62.02]\ngrpo = [65.05, 60.88, 66.11, 64.59, 62.77]\nprint('fig1 deltas:', [round(g-s, 2) for s,g in zip(sft, grpo)])\nprint('table3 deltas:', [round(g-s, 2) for s,g in zip([60.73,61.49,64.97,64.14,61.94], [61.18,60.88,66.11,63.46,62.77])])\n# 26. seed-by-seed standard\nprint('Standard per-seed (recomputed):', 59.21+0.23, 59.29+0.68, 59.29+0.99)\n# 27. RASP +1.72\nprint('RASP α=2 over CKA:', round(66.11-64.39, 2))\n# 28. 0.08 SFT diff\nprint('SFT 0.08 diff:', round(59.29-59.21, 2))\n\"\n",
    "description": "Verify derived calculations"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-25T19:56:13.162166+00:00_

mean |Δ| = 0.5425
peak reward ratio = 4.37
20% gap: 4.55
15% gap: 7.2
SFT 15% gap: 5.69
15% GRPO amp: 1.51
300-step ratio: 5.5
Random: 0.6799999999999997 0.5300000000000011 0.38000000000000256
Std decline 15->20: 7.199999999999996 20->25: 8.420000000000002
CKA decline 15->20: 8.27000000000001 20->25: 3.789999999999999
80.1% check: 80.11
30.5 pp: 30.5
4.6 pp: 4.55
alpha 2->3 drop: 2.65
alpha 2 vs CKA: 1.72
MBPP mean delta: 1.25
ShortGPT MBPP: 4.01
ShortGPT GSM8K: -1.36
TTFT improve %: 18.41
TPS decrease %: 19.03
per-token increase %: 20.14
Param reduction: 19.16 %
Pruned params: 1.46 B
M500 alpha SFT range: 6.199999999999999
Unpruned 9.56 pp: 9.56
200/784 = 25.51 %
CKA seed range: 0.37000000000000455
Std seed range: 0.7600000000000051
fig1 deltas: [0.53, -0.61, 1.14, 0.53, 0.75]
table3 deltas: [0.45, -0.61, 1.14, -0.68, 0.83]
Standard per-seed (recomputed): 59.44 59.97 60.28
RASP α=2 over CKA: 1.72
SFT 0.08 diff: 0.08

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-25T19:56:13.162426+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/audit_paper_numbers.md",
  "content": "# 论文数字提取清单\n\n审计日期: 2026-05-25\n审计范围: docs/paper/{abstract,introduction,method,related_work,experiments,conclusion,limitations,ethics,appendix}.tex + tables/*.tex + figures/paper/gen_*.py\n\n## 统计\n\n- A类(实验结果): ~140个\n- B类(模型/超参): ~35个\n- C类(统计描述): ~25个\n- D类(派生计算): ~30个\n\n---\n\n## 逐文件数字清单\n\n### abstract.tex\n\n| 行号 | 数字 | 上下文 | 分类 | 备注 |\n|------|------|--------|------|------|\n| 1 | 7B | \"7B reasoning model\" | B | DeepSeek-R1-Distill-Qwen-7B |\n| 1 | four (4) | \"across four criteria\" | C | CKA-only/Standard/RASP/Random |\n\n### introduction.tex\n\n| 行号 | 数字 | 上下文 | 分类 | 备注 |\n|------|------|--------|------|------|\n| 7 | 96.5% | \"96.5\\% parameter retention\" | A | 来自 selfhealing2025 外部引用 |\n| 10 | 7B | DeepSeek-R1-Distill-Qwen-7B | B | |\n| 10 | 20% | \"20\\% MLP channel sparsity\" | C | ⚠ 详见一致性检查 |\n| 10 | 4.4 (×) | \"4.4 times the peak RL reward\" | D | 0.354/0.081=4.37→4.4 ✓ |\n| 10 | 1 (pp) | \"within 1 percentage point\" | D | 上界描述 |\n| 17 | 20% | \"20\\% sparsity\" 图1 caption | C | |\n| 17 | 1.14 (pp) | \"$\\|\\Delta\\| \\leq 1.14$\\,pp\" | D | α=2.0 时 +1.14 |\n| 28 | $\\alpha{=}2.0$ | 峰值 α | B | |\n| 28 | 66.11% | GSM8K α=2.0 | A | 对应 Table 3 ✓ |\n| 31 | -1.36 (pp) | ShortGPT GSM8K Δ | A | 43.37-44.73=-1.36 ✓ |\n| 35 | 20-25% | 解耦适用范围 | C | |\n| 35 | $p{<}0.05$ | TOST | A | |\n| 35 | 7 of 8 | TOST 通过 | C | |\n| 35 | 15% | 解耦边界 | C | |\n| 36 | four (4) | 四个评价指标 | C | |\n| 37 | 20% | \"20\\% sparsity\" | C | |\n| 37 | 51-64% | SFT recovery range | A | 51.25-63.91 ✓ |\n| 37 | 1.14 (pp) | \"at most 1.14\\,pp\" | D | α=2.0 |\n| 37 | 300 | training steps | B | |\n\n### method.tex\n\n| 行号 | 数字 | 上下文 | 分类 | 备注 |\n|------|------|--------|------|------|\n| 17 | $n_Q{=}28$ | DeepSeek-R1-Distill-Qwen-7B | B | |\n| 17 | $n_{KV}{=}4$ | | B | |\n| 17 | $G{=}7$ | 28/4=7 | D | ✓ |\n| 17 | 7 Q + 1 KV | GQA group | B | |\n| 29 | 28 | \"28 MLP channel groups\" Layer 27 | B | |\n| 37 | $M{=}512$ | calibration set | C | |\n| 64 | $O(L \\cdot k^2)$ | CKA 计算复杂度 | B | $k \\le 28$ |\n| 65 | 28 | $k \\le 28$ | B | |\n| 65 | <2 min | CKA 计算时间 | A | |\n| 69 | $\\rho \\geq 0.964$ | Spearman 稳定性 | A | 对应 Table |\n| 75 | 40% | per-layer capacity floor | B | $\\tau=0.4$ |\n| 75 | {0.3, 0.4, 0.5, 0.6} | τ ablation | C | |\n| 91 | $\\alpha{=}0$ | reduces to Standard | B | |\n| 93 | $\\alpha{=}2.0$ | 峰值 | B | |\n| 93 | 66.11% | α=2.0 GRPO acc | A | |\n| 93 | +1.72 (pp) | over CKA-only | D | 66.11-64.39=1.72 ✓ |\n| 115 | 20% | sparsity | C | |\n| 122 | 1, 2 | 阶段编号 | B | |\n\n### related_work.tex\n\n| 行号 | 数字 | 上下文 | 分类 | 备注 |\n|------|------|--------|------|------|\n| 10 | 96.5% | selfhealing2025 retention | A | 外部 |\n| 15 | 1.8 (pp) | \"$\\|\\Delta\\| \\leq 1.8$\\,pp\" | D | MATH-500 α=2.0 时的最大值 |\n| 17 | 5-30% | RL 参数更新比例 | A | 外部引用 |\n\n### experiments.tex\n\n| 行号 | 数字 | 上下文 | 分类 | 备注 |\n|------|------|--------|------|------|\n| 18 | 20% | sparsity | C | |\n| 28 | 7B | DeepSeek-R1 | B | |\n| 29 | $N{=}1{,}319$ | GSM8K size | C | |\n| 30 | 90.83% | Unpruned greedy GSM8K | A | |\n| 33 | 20% | structured sparsity | C | ⚠ 详见一致性 |\n| 33 | 200 of 784 | MLP groups | C | 200/784=25.5% ⚠ |\n| 33 | 28 | layers | B | |\n| 33 | ~1.45B | params removed | A | 实际 7.62-6.16=1.46B |\n| 33 | 40% | retention floor | B | |\n| 33 | $\\alpha{=}1.0$ | RASP main | B | |\n| 33 | 512 | TRL default tokens | B | Random |\n| 33 | 1,024 | other methods tokens | B | |\n| 37 | <2% | post-prune accuracy | A | |\n| 38 | 2 (epochs) | SFT | B | |\n| 38 | 7,473 | GSM8K examples SFT | C | |\n| 38 | 37 min | SFT wall time | A | |\n| 38 | $1{\\times}10^{-6}$ | GRPO lr | B | |\n| 38 | $\\beta{=}0.01$ | KL coef | B | |\n| 38 | $T{=}0.4$ | temperature | B | |\n| 38 | 100 | GRPO steps | B | |\n| 38 | 1,000 | GRPO problems | C | |\n| 39 | 3 | seeds | C | |\n| 39 | 64.39% | CKA-only mean | A | |\n| 39 | 0.19 pp | CKA-only std | A | |\n| 39 | 59.84% | Standard mean | A | |\n| 39 | 0.38 pp | Standard std | A | |\n| 39 | $p{<}0.001$ | Welch's t | A | |\n| 40 | 9.56 pp | \"Unpruned\"-warmup gap | D | 90.83-81.27=9.56 ✓ |\n| 40 | 90.83% | pre-warmup | A | |\n| 41 | 2× | RTX PRO 6000 GPUs | B | |\n| 41 | 94 GB | VRAM | B | |\n| 47 | 20% | sparsity | C | |\n| 50 | 0.354 | CKA-only peak reward | A | |\n| 50 | 0.125 | CKA-only min $f_0$ | A | |\n| 51 | 0.14-0.19 | Random reward range | A | |\n| 51 | 0.300 | Random min $f_0$ | A | |\n| 51 | 0.50 | Standard $f_0$ | A | |\n| 51 | 0.081 | Standard peak reward | A | |\n| 51 | 0.675 | RASP $f_0$ | A | |\n| 51 | 0.010 | RASP reward decline | A | |\n| 73 | 4.4× | peak reward gap | D | 0.354/0.081 ✓ |\n| 73 | $\\|\\Delta\\| < 1$ pp | 上界 | D | |\n| 73 | +0.48 | CKA-only Δ | A | 64.39-63.91 ✓ |\n| 73 | +0.55 | Standard Δ | A | 59.84-59.29 ✓ |\n| 73 | -0.53 | Random Δ | A | 50.72-51.25 ✓ |\n| 73 | -0.61 | RASP Δ | A | 60.88-61.49 ✓ |\n| 74 | 20-25% | 解耦范围 | C | |\n| 76 | 15% | 边界 | C | |\n| 76 | 5.69 pp | SFT 15% gap | D | 72.18-66.49 ✓ |\n| 76 | 7.20 pp | GRPO 15% gap | D | 72.76-65.56 ✓ |\n| 76 | 1 pp | 上界 | D | |\n| 76 | 1.14 pp | α=2.0 Δ | D | |\n| 78 | $\\varepsilon{=}2$ pp | TOST margin | B | |\n| 78 | $4\\times$ | 4× cross-seed σ | D | 2/0.19≈10× actually, 2/0.38≈5× — 取近似 |\n| 78 | $N{=}1{,}319$ | TOST samples | C | |\n| 78 | 7/8 | TOST 通过 | C | |\n| 78 | 0.37 pp | seed range | A | 64.59-64.22=0.37 ✓ |\n| 78 | 300 | extended steps | B | |\n| 79 | 2 pp | \"$\\|\\Delta\\| < 2$\\,pp\" MBPP | D | 实际最大 +1.34 |\n| 81 | -1.36 pp | ShortGPT GSM8K | A | |\n| 81 | +4.01 pp | ShortGPT MBPP | A | 14.44-10.43 ✓ |\n| 81 | 1.8 pp | fine-grained 上界 | D | MATH-500 α=2.0 |\n| 90 | {0.5, 1.0, 2.0, 3.0, 4.0} | α 范围 | B | |\n| 90 | 66.11% | α=2.0 peak | A | |\n| 90 | 1.14 pp | 上界 | D | |\n| 90 | 62.77% | α=4.0 | A | |\n| 91 | 23.0% | MATH-500 α=1.0 worst | A | |\n| 91 | 27.2-27.6% | higher-α 集群 | A | |\n| 92 | 30% | sparsity cliff | C | |\n| 92 | 19% | param reduction | D | 1.46/7.62=0.192 ✓ |\n| 92 | ~28% | memory reduction | A | |\n| 102 | $\\mu{=}0.62$ | CKA-only layer CKA mean | A | 实算 0.6202 ✓ |\n| 109 | 5.5× | 300-step gap | D | 0.308/0.056=5.50 ✓ |\n| 116 | $\\mu{=}0.62$ | CKA-only | A | |\n| 116 | $\\mu{=}0.90$ | Standard | A | 实算 0.9039 ✓ |\n| 116 | $\\mu{=}0.92$ | Random | A | 实算 0.9233 ✓ |\n| 116 | $\\mu{=}0.88$ | RASP | A | 实算 0.8822 ✓ |\n| 118 | L0-9 | 早层 | C | |\n| 118 | 72.5% | CKA-only 移除集中度 | A | |\n| 118 | 2.89× | gradient ratio | A | |\n| 118 | 55/56 | 显著层 | C | |\n| 118 | $p{<}0.05$ | | A | |\n| 119 | 22% | CKA-only truncation | A | |\n| 119 | 655 (tokens) | CKA-only mean | A | |\n| 119 | 44% | Standard truncation | A | |\n| 119 | 1,128 (tokens) | Standard mean | A | |\n| 123 | 100, 300 | step extension | B | |\n| 123 | 0.054-0.058 | Standard reward range | A | 与 fig5 数据一致 |\n| 123 | 0.5 | $f_0$ threshold | B | |\n| 123 | 5.5× | gap | D | |\n| 123 | 0.308 | CKA-only step 300 | A | 0.3075 → 0.308 ✓ |\n| 123 | 0.056 | Standard step 300 | A | 0.0562 → 0.056 ✓ |\n| 124 | 10 (steps) | Standard 进入 collapse | B | |\n| 124 | 0.5 | $f_0$ | B | |\n| 124 | 0.35 | CKA-only $f_0$ | A | |\n| 129 | 1.5B | scale | B | |\n| 129 | 1.0% | post-prune Math-7B | A | |\n| 129 | 51.50% | CKA-only Math-7B | A | |\n| 129 | 21.00% | Standard Math-7B | A | |\n| 130 | 30.5 pp | cross-model gap | D | 51.50-21.00=30.50 ✓ |\n| 130 | 4.6 pp | primary | D | 64.39-59.84=4.55, rounded 4.6 ⚠ |\n\n### conclusion.tex\n\n| 行号 | 数字 | 上下文 | 分类 | 备注 |\n|------|------|--------|------|------|\n| 5 | 20-25% | sparsity range | C | |\n| 5 | mean \\|Δ\\| = 0.54 pp | four criteria | D | (0.48+0.55+0.61+0.53)/4=0.5425 ✓ |\n| 5 | 1.8 pp | max across benchmarks | D | MATH-500 α=2.0 |\n| 5 | 4.4× | peak reward gap | D | |\n| 6 | 20% | sparsity | C | |\n| 6 | <2% | post-prune | A | |\n| 6 | 51-64% | recovery range | A | |\n| 6 | 300 | steps | B | |\n| 9 | ~100 | diagnostic steps | B | |\n\n### limitations.tex\n\n| 行号 | 数字 | 上下文 | 分类 | 备注 |\n|------|------|--------|------|------|\n| 3 | 两个 (7B, 1.5B) | Qwen2.5 模型 | C | |\n\n### ethics.tex\n\n无数字。\n\n### appendix.tex\n\n| 行号 | 数字 | 上下文 | 分类 | 备注 |\n|------|------|--------|------|------|\n| 16 | $2 \\times 10^{-5}$ | SFT lr | B | |\n| 16 | $1 \\times 10^{-6}$ | GRPO lr | B | |\n| 17 | 1, 1 | batch size | B | |\n| 18 | 8, 1 | grad accumulation | B | |\n| 19 | 2,048 | max seq len | B | |\n| 20 | 1,024, 512 | max new tokens | B | |\n| 22 | 2 epochs / 100 steps | | B | |\n| 23 | 0.01 | KL β | B | |\n| 24 | 0.4 | sampling temp | B | |\n| 25 | 8 | generations per prompt | B | |\n| 28 | 50 | reward_desert_patience | B | |\n| 80 | 72.0 | Dense TPS | A | |\n| 80 | 20.1 | Dense TTFT (ms) | A | |\n| 80 | 13.9 | Dense per-token (ms) | A | |\n| 80 | 7.62 | Dense params (B) | A | |\n| 81 | 58.3 | CKA TPS | A | |\n| 81 | 16.4 | CKA TTFT | A | |\n| 81 | 16.7 | CKA per-token | A | |\n| 81 | 6.16 | CKA params | A | |\n| 82 | 58.2 | Standard TPS | A | |\n| 82 | 16.4 | Standard TTFT | A | |\n| 82 | 16.7 | Standard per-token | A | |\n| 82 | 6.16 | Standard params | A | |\n| 87 | ~28% | memory reduction | A | |\n| 88 | 18% | TTFT improvement | D | (20.1-16.4)/20.1=18.4% ✓ |\n| 88 | 20.1→16.4 | | A | |\n| 89 | 19% | per-token decrease | D | (72.0-58.3)/72.0=19.0% ✓ |\n| 89 | 72.0→58.3 | | A | |\n| 89 | 13.9→16.7 | | A | |\n| 90 | 58.3 vs 58.2 | identical throughput | A | |\n| 97 | α=2.0 | peak | B | |\n| 97 | 64.97% | SFT α=2.0 | A | |\n| 97 | 66.11% | GRPO α=2.0 | A | |\n| 97 | +1.14 pp | Δ | A | |\n| 98 | α=0.5 | | B | |\n| 98 | 60.73% | SFT α=0.5 | A | ⚠ 与 fig1 数据不一致 |\n| 98 | 61.18% | GRPO α=0.5 | A | ⚠ 与 fig1 数据不一致 |\n| 99 | α=1.0 | | B | |\n| 99 | 0.061 | RASP peak reward | A | |\n| 99 | 60.88% | RASP GRPO | A | |\n| 99 | -0.61 pp | Δ | A | |\n| 100 | α=3.0 | | B | |\n| 100 | 64.14% | SFT α=3.0 | A | |\n| 100 | 63.46% | GRPO α=3.0 | A | |\n| 100 | -0.68 pp | Δ | A | |\n| 100 | 2.65 pp | drop from peak | D | 66.11-63.46=2.65 ✓ |\n| 101 | α=4.0 | | B | |\n| 101 | 62.77% | GRPO α=4.0 | A | |\n| 101 | 61.94% | SFT α=4.0 | A | |\n| 101 | +0.83 pp | Δ | A | |\n| 101 | 0.146→0.256→0.198 | reward trajectory | A | |\n| 102 | 1.14 pp | 上界 | D | |\n| 107 | 100, 300 | steps | B | |\n| 108 | 64.37% | CKA-only seed 42 at 300 | A | |\n| 108 | 59.29% | Standard at 300 | A | |\n| 108 | 0.38 pp | std | A | |\n| 109 | 0.354 | peak step 100 | A | ⚠ peak at step 50 实际是 0.3544 |\n| 109 | 0.308 | step 300 | A | |\n| 110 | 0.054-0.058 | Standard range | A | |\n| 117 | 27.4%, 25.6%, 21.6%, 16.6% | MATH-500 SFT | A | |\n| 117 | 27.6%, 27.0%, 23.0%, 15.0% | MATH-500 GRPO | A | |\n| 118 | 4.6 pp | GSM8K SFT gap | D | 63.91-59.29=4.62 ⚠ 论文写4.6 |\n| 118 | 1.8 pp | MATH-500 SFT gap | D | 27.4-25.6=1.8 ✓ |\n| 118 | 0.6 pp | MATH-500 GRPO gap | D | 27.6-27.0=0.6 ✓ |\n| 120 | 53.0% | dense MATH-500 | A | |\n| 120 | 90.83% | dense GSM8K | A | |\n| 120 | 2,048 | token limit | B | |\n| 121 | 22% | CKA truncation | A | |\n| 121 | 655 | CKA mean tokens | A | |\n| 121 | 44% | Standard truncation | A | |\n| 121 | 1,128 | Standard mean tokens | A | |\n| 122 | ~8 pp | α SFT range MATH-500 | A | ⚠ 实算 6.2 pp |\n| 122 | ~2 pp | stderr | A | |\n| 122 | 2048 | token limit | B | |\n| 128 | $N{=}374$ | MBPP size | C | |\n| 132 | +1.25 pp | MBPP mean | D | (1.34+1.07+1.34)/3=1.25 ✓ |\n| 132 | $N{=}374$ | | C | |\n| 132 | ~1.7 pp | stderr | A | |\n| 142 | 256/512/1024 | calibration sizes | C | |\n| 142 | 0.964 to 0.979 | Spearman range | A | 对应表 |\n| 147 | $N{=}200$ | gradient samples | C | |\n| 158 | 2.89× | CKA vs Standard ratio | A | |\n| 158 | 55/56 | sig layers | C | |\n| 159 | 2.26× | CKA vs RASP | A | |\n| 159 | 56/56 | | C | |\n| 160 | 1.28× | RASP vs Standard | A | |\n| 160 | 45/56 | | C | |\n| 165 | 64.39%, 60.88%, 59.84% | recovery hierarchy | A | |\n| 172 | 64.37% | seed 42 | A | |\n| 172 | 64.22% | seed 123 | A | |\n| 172 | 64.59% | seed 456 | A | |\n| 172 | 64.39% | mean | A | |\n| 172 | 0.19 pp | std | A | |\n| 173 | 59.84% | Standard mean | A | |\n| 173 | 0.38 pp | std | A | |\n| 174 | 4.55 pp | gap | D | 64.39-59.84 ✓ |\n| 184 | 4% | Standard 30% | A | |\n| 184 | 1.6% | CKA 30% | A | |\n| 184 | 0% | RASP 30% | A | |\n| 200 | 64.39, 0.19, 3 | multi-seed table | A | |\n| 201 | 59.84, 0.38, 3 | | A | |\n| 202 | 60.88, 1 | | A | |\n| 203 | 50.72, 0.15, 3 | | A | |\n| 205 | 72.76, 0.57, 3 | 15% CKA | A | |\n| 206 | 65.56, 0.50, 3 | 15% Std | A | |\n| 210 | 4.55 pp | gap 20% | D | ✓ |\n| 210 | 64.22--64.59% | CKA range | A | |\n| 210 | 59.44--60.20% | Standard range | A | ⚠ 实算 seed456 GRPO=60.28 (>60.20) |\n| 211 | 0.76 pp vs 0.37 pp | observed ranges | D | 60.20-59.44=0.76, 64.59-64.22=0.37 |\n| 212 | 50.57%, 50.72%, 50.87% | Random seeds | A | |\n| 212 | 0.15 pp | σ | A | |\n| 212 | 0.30 pp | range | D | 50.87-50.57=0.30 ✓ |\n| 212 | 51.25% | SFT | A | |\n| 213 | -0.68, -0.53, -0.38 pp | Random Δ | D | 51.25-50.57/72/87 ✓ |\n| 214 | 59.21% vs 59.29% | Standard SFT 差异 | A | |\n| 214 | 0.08 pp | Δ | D | ✓ |\n| 215 | 7.20 pp | 15% gap | D | ✓ |\n| 215 | 72.76 vs 65.56 | | A | |\n| 215 | $t{\\approx}16.4$ | | A | |\n| 215 | $p{<}0.001$ | | A | |\n| 215 | 72.10--73.09%, 65.13--65.43% | seed ranges 15% | A | |\n| 229-237 | cross-sparsity 表 | (见表) | A | |\n| 243 | +7.20 pp | 15% gap | D | ✓ |\n| 244 | 80.1% | retention | D | 72.76/90.83=80.11% ✓ |\n| 245 | -7.20, -8.42 | Standard decline | D | 66.49-59.29, 59.29-50.87 ✓ |\n| 245 | -8.27, -3.79 | CKA decline | D | 72.18-63.91, 63.91-60.12 ✓ |\n| 246 | 0.008 | Standard 25% peak reward | A | |\n| 256 | 35.48, 22.29, 26.16 | 1.5B accs | A | |\n| 256 | -0.15, -0.61 pp | 1.5B Δ | A | |\n| 257 | 49.81% | 1.5B dense | A | |\n| 257 | 90.83% | 7B dense | A | |\n| 265 | $N{=}200$ | Math-7B size | C | |\n| 272 | 1.0%, 51.50%, 27.0% | CKA Math-7B | A | |\n| 272 | 3.53 (stderr) | binomial | D | sqrt(0.515*0.485/200)=0.0353 ✓ |\n| 273 | 18.5%, 21.00%, 36.5% | Standard Math-7B | A | |\n| 273 | 2.88 stderr | | D | sqrt(0.21*0.79/200)=0.0288 ✓ |\n| 278 | 1.0%, 18.5%, 51.50%, 21.00% | Math-7B 复述 | A | |\n| 280 | 40%, 48.60%, 243/500, 83.8%, 2048 | EOS/GRPO/truncation | A | 243/500=48.6% ✓ |\n| 285 | 28 layers | | B | |\n| 285 | 20% | sparsity | C | |\n| 286 | L0--9, 72.5% | CKA early-layer | A | |\n| 286 | L16--27 | preserved late | C | |\n| 287 | L16-18, L22, L25-26 | Standard distribution | C | |\n| 290 | 65 (groups) | CKA exclusive | A | |\n| 290 | L6-9, L27 | | C | |\n| 291 | 46+ (groups) | Standard exclusive | A | |\n| 291 | L16-18, L22, L25-26 | | C | |\n| 293 | $\\mu{=}0.62$, 0.90 | | A | |\n| 304 | <0.001 | RASP KL | A | |\n| 304 | ~0.004-0.005 | Random KL | A | |\n| 308 | $\\alpha{=}1.0$ | | B | |\n| 308 | <0.001 | KL | A | ⚠ 实际 RASP max=0.001119 (微超) |\n| 309 | 0.001-0.003 | CKA/Standard KL | A | 数据范围合理 |\n| 309 | ~0.004-0.005 | Random | A | |\n| 313 | 0.001, 0.5, 1.0 | depth-first synthetic | B | |\n| 313 | 20% | sparsity | C | |\n| 317 | ~10%, ~8% | SFT/GRPO depth-first | A | |\n| 317 | $N{\\approx}50$--88 | early stopped | C | |\n| 326 | $N{=}1{,}319$ | | C | |\n| 326 | 100 steps | | B | |\n| 326 | $\\tau{=}0.4$ | default | B | |\n| 332 | 0.3, 65.05%, +0.68 | floor 0.3 | A | |\n| 333 | 0.4, 64.37% | default | A | |\n| 334 | 0.5, 61.71%, -2.66 | | A | 64.37-61.71=2.66 ✓ |\n| 335 | 0.6, 62.02%, -2.35 | | A | 64.37-62.02=2.35 ✓ |\n| 342 | +0.68 pp | | D | |\n| 342 | -2.66, -2.35 pp | | D | |\n| 342 | 0.31 pp | 0.5/0.6 diff | D | 62.02-61.71=0.31 ✓ |\n| 342 | ~1.3 pp | stderr | A | |\n| 348 | $N{=}1{,}319$ | | C | |\n| 348 | 20% | sparsity | C | |\n| 350 | $\\varepsilon$ | margin | B | |\n| 361-369 | TOST 表数值 | (per-seed Δ) | A | 详见一致性检查 |\n| 374 | 2 pp | $\\varepsilon$ | B | |\n| 374 | 4× | σ multiplier | D | 2/0.19≈10.5× ⚠ 论文说4× (应基于Standard σ=0.38?: 2/0.38=5.3 也不是4) |\n| 374 | 0.19 pp | σ | A | |\n| 375 | 2 pp | | B | |\n| 375 | 7/8 | | C | |\n| 375 | -0.99 pp | borderline | A | |\n| 375 | $p{=}0.069$ | | A | |\n| 376 | 3 pp | | B | |\n| 376 | 8/8 | | C | |\n| 376 | $p{<}0.002$ | | A | |\n| 377 | 1 pp | | B | |\n| 377 | $N{=}1{,}319$ | | C | |\n| 384 | 15% | | C | |\n| 384 | +1.51 pp | CKA-guided amp | D | 7.20-5.69=1.51 ✓ |\n| 388 | 96.5% | external retention | A | |\n| 388 | 20-25% | sparsity | C | |\n\n### tables/tab1_recovery_gradient.tex\n\n| 数字 | 上下文 | 备注 |\n|------|--------|------|\n| 20% | sparsity | |\n| 0.354, 0.285, 0.125 | CKA peak/mean/min $f_0$ | |\n| 0.190, 0.164, 0.300 | Random | |\n| 0.081, 0.050, 0.500 | Standard | |\n| 0.061, 0.031, 0.675 | RASP | |\n\n### tables/tab2_decoupling.tex\n\n| 数字 | 上下文 | 备注 |\n|------|--------|------|\n| $N{=}1{,}319$, 20% | |\n| 81.27, 81.27, 0.00, 0.669 | Unpruned | |\n| 64.97, 66.11, +1.14 | α=2.0 | |\n| 63.91, 64.39, ±0.19, +0.48, 0.354 | CKA-only | |\n| 59.29, 59.84, ±0.38, +0.55, 0.081 | Standard | |\n| 61.49, 60.88, -0.61, 0.061 | RASP α=1.0 | |\n| 51.25, 50.72, ±0.15, -0.53, 0.190 | Random | |\n| 44.73, 43.37, -1.36 | ShortGPT | |\n\n### tables/tab_math500.tex\n\n| 数字 | 上下文 | 备注 |\n|------|--------|------|\n| $N{=}500$, 2048 tokens | |\n| 0.6 pp, 4.62 pp | GRPO/GSM8K SFT gaps in caption | 4.62=63.91-59.29 ⚠ 主文写4.6 |\n| 53.0 | dense | |\n| 20% method: 27.4/27.6, 25.6/27.0, 21.6/23.0, 16.6/15.0 | |\n| Δ: +0.2, +1.4, +1.4, -1.6 | |\n| α: 26.8/26.8, 25.6/27.4, 23.6/--, 27.8/27.2 | 0.5/2.0/3.0/4.0 |\n| Δ α: +0.0, +1.8, --, -0.6 | |\n| 25%: 18.8/17.6, 15.4/-- | -1.2, -- | |\n| 73.6% at 4096 | dense truncation | |\n\n### tables/tab_mbpp.tex\n\n| 数字 | 上下文 | 备注 |\n|------|--------|------|\n| $N{=}374$ | |\n| ~75% | code capability loss | |\n| ~1 pp | range | |\n| +4.01 pp, 1.55 stderr | ShortGPT | |\n| Dense: 53.48 | |\n| CKA 20%: 12.83/14.17/+1.34 | |\n| Standard 20%: 12.03/13.10/+1.07 | |\n| RASP α=1.0 20%: 11.76/13.10/+1.34 | |\n| ShortGPT 20%: 10.43/14.44/+4.01 | |\n\n### tables/tab_cka_stability.tex\n\n| 数字 | 上下文 | 备注 |\n|------|--------|------|\n| $\\rho \\geq 0.964$, 0.964/0.979 | 256/512/1024 | |\n\n### tables/table3_alpha.tex\n\n| 数字 | 上下文 | 备注 |\n|------|--------|------|\n| $N{=}1{,}319$, 20% | |\n| α=0.5: 60.73/61.18/+0.45 | |\n| α=1.0: 61.49/60.88/-0.61 | |\n| α=2.0: 64.97/66.11/+1.14 | |\n| α=3.0: 64.14/63.46/-0.68 | |\n| α=4.0: 61.94/62.77/+0.83 | |\n\n### tables/table4_sparsity_cliff.tex\n\n| 数字 | 上下文 | 备注 |\n|------|--------|------|\n| 30% | sparsity | |\n| Standard: N=200, 4%, 5.5% EOS | |\n| RASP α=1: N=200, 0%, 3.0% EOS | |\n| CKA: N=500, 1.6%, 8/500 | |\n\n### tables/tab5_cross_scale.tex\n\n| 数字 | 上下文 | 备注 |\n|------|--------|------|\n| 20%, 100 steps | |\n| CKA: 0.354/64.39, 0.238/35.48 | 7B/1.5B |\n| Standard: 0.081/59.84, 0.084/22.29 | |\n| RASP α=1: 0.061/60.88, 0.099/26.16 | |\n| Random: 0.190 | 7B only |\n\n---\n\n## 内部一致性检查\n\n### ✅ 已验证一致\n\n| 数字 | 位置1 | 位置2 | 结果 |\n|------|-------|-------|------|\n| 64.39% CKA-only GRPO | exp.tex:39 | tab2:13 | ✓ |\n| 59.84% Standard GRPO | exp.tex:39 | tab2:14 | ✓ |\n| 4.4× peak reward | intro:10, exp:73, concl:5 | 0.354/0.081=4.37 | ✓ |\n| mean \\|Δ\\|=0.54 | concl:5 | (0.48+0.55+0.61+0.53)/4=0.5425 | ✓ |\n| 90.83% Unpruned | exp:30, exp:40, app:120, app:257 | | ✓ |\n| 81.27% Unpruned post-SFT | tab2:11 | exp:40 (隐含 9.56 pp gap) | ✓ |\n| $f_0$ 值 (0.125/0.300/0.500/0.675) | exp:50, tab1, fig3 | | ✓ |\n| α=2.0 peak (64.97/66.11/+1.14) | intro:28, method:93, exp:90, app:97, tab2:12, tab3:12 | | ✓ |\n| ShortGPT GSM8K -1.36 pp | intro:31, exp:81, tab2:18 | | ✓ |\n| ShortGPT MBPP +4.01 pp | exp:81, tab_mbpp:16 | | ✓ |\n| 7.20 pp 15% GRPO gap | exp:76, app:215, app:243 | | ✓ |\n| 5.5× 300-step gap | exp:109, exp:123 | | ✓ |\n| 19% / ~28% param/mem reduction | exp:92, app:73, app:87 | | ✓ |\n| RASP α=1.0 reward 0.061 | exp:51, tab1, tab2:15, tab5 | | ✓ |\n| 51-64% SFT recovery range | intro:37, concl:6 | tab2 实际 51.25-63.91 | ✓ |\n| $\\|\\Delta\\| ≤ 1.14$ pp | intro:17, exp:76, app:102 | α=2.0 最大 | ✓ |\n| 1.5B 三方法排序 | exp:129 | tab5 | ✓ |\n| 30.5 pp cross-model | exp:130 | 51.50-21.00 | ✓ |\n| Spearman ρ ≥ 0.964 | method:69 | tab_cka_stability | ✓ |\n| 2.89× gradient ratio | exp:118, app:158 | | ✓ |\n\n### ⚠ 发现的问题（按严重度排序）\n\n| # | 严重度 | 位置1 | 位置2 | 差异说明 |\n|---|--------|-------|-------|---------|\n| **1** | **HIGH** | gen_fig1_dose_response.py:32-33 | table3_alpha.tex:10-14 | **Fig 1 的 SFT/GRPO 硬编码值与 Table 3 不一致**（详见下方） |\n| **2** | **MEDIUM** | intro.tex:10 \"20% MLP channel sparsity\"; exp.tex:33 \"20% structured sparsity, all removing 200 of 784 MLP channel groups\" | app.tex:88 \"Pruning reduces parameters by 19%\" | **200/784 = 25.5% MLP groups, 不是 20%**。看似\"20% sparsity\"是相对于总模型参数（19% rounded），但 intro 写 \"MLP channel sparsity\" 是术语错误 |\n| **3** | **MEDIUM** | app.tex:122 \"SFT accuracy varies by ${\\sim}$8\\,pp across $\\alpha$ values\" | tab_math500.tex α SFT 值 | 实际 max-min = 27.8-21.6 = 6.2 pp，\"~8 pp\" 偏大 |\n| **4** | **LOW** | exp.tex:130 \"4.6 pp difference on the primary model\" | exp.tex:39, tab2 64.39-59.84=4.55 | 4.55 rounded to 4.6（合理近似）；但 tab_math500.tex caption 写 \"4.62 pp\"——同一数字两种舍入并存 |\n| **5** | **LOW** | exp.tex:78 \"$4\\times$ cross-seed $\\sigma$\" | app.tex:374 \"$2$\\,pp because it is approximately $4\\times$ the observed cross-seed standard deviation ($\\sigma{=}0.19$\\,pp for CKA-only)\" | 2/0.19 = 10.5×，不是 4×。若以 Standard σ=0.38 计算 = 5.3×，也不是 4×。\"4×\" 数字来源不明 |\n| **6** | **LOW** | app.tex:308 \"near-zero KL ($<$0.001)\" | gen_fig_appendix_kl.py:42 RASP max=0.001119 | RASP KL 实际值有少数点 (0.001022, 0.001119, 0.001043) 略超 0.001 |\n| **7** | **LOW** | app.tex:109 \"CKA-only reward rises from 0.354 (peak at step 100) to 0.308 (step 300)\" | 0.354 > 0.308 | \"rises from X to Y\" 当 X > Y 时是反向表述（语义错误，非数字错误） |\n| **8** | **LOW** | app.tex:210 \"Standard: 59.44--60.20\\%\" | 从 TOST 反推 seed 456 GRPO = 59.29 + 0.99 = **60.28**, 不是 60.20 | 范围上界与重算 0.08 pp 差异 |\n| **9** | **LOW** | exp.tex:33 \"~1.45B parameters\" pruned | app.tex 7.62-6.16 = 1.46B | 1.45 vs 1.46 rounding |\n| **10** | **VERY LOW** | exp.tex:81, related:15 \"$\\|\\Delta\\| \\leq 1.8$\\,pp\" fine-grained | exp.tex:73 \"$\\|\\Delta\\| < 1$ pp\" 20% sparsity | 不冲突：20% 是 <1 pp，1.8 是涵盖 α=2.0 时的最大值。表述兼容但需读者解读 |\n\n### 详细分析：Issue #1（Fig 1 数据不一致）\n\n```\n              gen_fig1_dose_response.py     table3_alpha.tex / app:97-101\nα=0.5  SFT/GRPO:  64.52 / 65.05    vs   60.73 / 61.18    ⚠ 差异约 4 pp!\nα=1.0  SFT/GRPO:  61.49 / 60.88    vs   61.49 / 60.88    ✓ 一致\nα=2.0  SFT/GRPO:  64.97 / 66.11    vs   64.97 / 66.11    ✓ 一致\nα=3.0  SFT/GRPO:  64.06 / 64.59    vs   64.14 / 63.46    ⚠ GRPO 差 1.13 pp!\nα=4.0  SFT/GRPO:  62.02 / 62.77    vs   61.94 / 62.77    ⚠ SFT 差 0.08 pp (微差)\n```\n\n**结论**：Fig 1 中 α=0.5 与 α=3.0 的数据明显与 Table 3 / Appendix text 不一致；α=4.0 SFT 有小差。Figure caption 的 \"$|\\Delta| \\leq 1.14$ pp\" 描述在两个数据集上都成立（因 α=2.0 给出 +1.14），所以读者不会从 caption 发现矛盾，但内部数据源不统一。\n\n**疑似原因**：Fig 1 数据可能是早期实验值（pre-rerun）；Table 3 是后续重跑值。需检查 W&B / 原始日志确认哪个为真。\n\n### 详细分析：Issue #2（\"20% sparsity\" 术语）\n\n- `intro.tex:10`: \"20\\% MLP channel sparsity\"\n- `intro.tex:37`: \"20\\% sparsity\"\n- `intro.tex:35`: \"20--25\\% fine-grained MLP sparsity\"\n- `exp.tex:33`: \"20\\% structured sparsity, all removing 200 of 784 MLP channel groups across 28 layers (${\\sim}$1.45B parameters)\"\n- `exp.tex:92`: \"pruning reduces parameters by 19\\%\"\n- `app.tex:73`: \"Pruning reduces parameters by 19\\%\"\n\n**数学**：\n- 200/784 = **25.5%** MLP channel groups\n- 1.46B/7.62B = **19.2%** total parameters\n- \"20%\" 既不等于 25.5%（MLP channels）也不精确等于 19.2%（total params）\n\n**推测**：作者用 \"20% structured sparsity\" 作为目标设定值（target sparsity），但实际去掉的 MLP groups 比例（25.5%）和总参数比例（19%）都不是 20%。在 intro 写 \"20\\% MLP channel sparsity\" 是不准确（应该是 25.5%）。这是术语滥用，但若读者按\"约 20% reduction\"理解则可接受。\n\n---\n\n## 图表脚本数据源\n\n| 脚本 | 输出文件 | 数据来源 | 硬编码数据点 | 论文引用 |\n|------|---------|---------|-------------|---------|\n| gen_fig1_dose_response.py | fig1_dose_response.pdf | 硬编码 | sft_acc=[64.52,61.49,64.97,64.06,62.02], grpo_acc=[65.05,60.88,66.11,64.59,62.77], CKA baseline=64.39 | intro.tex:16 ⚠ Issue #1 |\n| gen_fig1_framework.py | fig1_framework.pdf | 硬编码 (示意图) | \"+2.2pp advantage\" 标注（论文文本中未提及）；\"Peak 0.081\" Standard, \"Peak 0.061\" RASP, collapse step 90 / step 10 | (论文引用 fig1_method_framework.pdf, 文件名不同；脚本与论文图可能不是同一来源) |\n| gen_fig2_reward_accuracy.py | fig2_reward_accuracy.pdf | 硬编码 | RASP grpo=61.87, Standard grpo=58.91 ⚠ 与现行 Table 2 不一致 | **未被引用**（orphan figure） |\n| gen_fig2_reward_trajectories.py | fig2_reward_trajectories.pdf | 硬编码 | unpruned/CKA/Random/Standard/RASP 各 step reward 序列；CKA peak 0.3544 (step 50), Standard 0.0813 (step 40), Random 0.190 (step 70), RASP 0.06125 (step 50) | exp.tex:9 ✓ |\n| gen_fig3_collapse_dynamics.py | fig3_collapse_dynamics.pdf | 硬编码 | $f_0$ 与 grad_norm 序列；CKA min $f_0$=0.125, Random=0.300, Standard=0.500, RASP=0.675 | exp.tex:15 ✓ |\n| gen_fig4_cka_heatmap.py | fig4_cka_heatmap.pdf | 硬编码 | 28 层 CKA(dense, pruned)；μ 实算: CKA=0.6202, Standard=0.9039, Random=0.9233, RASP=0.8822 | exp.tex:101 ✓ |\n| gen_fig5_extended_training.py | fig5_extended_training.pdf | 硬编码 | Standard 300-step reward {150:0.055, 200:0.054, 250:0.058, 300:0.0562}, CKA 300-step reward {300:0.3075} 等 | exp.tex:108 ✓ |\n| gen_fig_appendix_kl.py | fig_appendix_kl.pdf | 硬编码 (注释: \"W&B/server logs 2026-05-18\") | KL 序列；RASP max=0.001119 略超 \"<0.001\" claim | app.tex:303 ✓ |\n| gen_fig_sft_grpo_scatter.py | fig_sft_grpo_scatter.pdf | 硬编码 | 与 Table 2/3/cross_sparsity 一致 | exp.tex:67 ✓ |\n| (无脚本) | fig_intra_layer_cka.pdf | unknown | — | method.tex:28 |\n| (无脚本) | fig_pruning_decisions.png | unknown | — | method.tex:114 |\n| (无脚本) | fig1_method_framework.pdf | unknown (脚本 gen_fig1_framework.py 输出名不同) | — | intro.tex:42 |\n\n---\n\n## D类派生计算验证\n\n| # | 位置 | 论文写的 | 推导过程 | 正确? |\n|---|------|----------|---------|-------|\n| 1 | concl:5 | mean \\|Δ\\| = 0.54 pp | (0.48+0.55+0.61+0.53)/4 = 0.5425 | ✓ |\n| 2 | intro:10, exp:73, concl:5 | 4.4× peak reward gap | 0.354/0.081 = 4.37 → 4.4 | ✓ |\n| 3 | exp:39, app:174, app:210 | 4.55 pp gap | 64.39-59.84 = 4.55 | ✓ |\n| 4 | exp:76, app:215, app:243 | 7.20 pp gap (15%) | 72.76-65.56 = 7.20 | ✓ |\n| 5 | exp:76 | 5.69 pp SFT 15% gap | 72.18-66.49 = 5.69 | ✓ |\n| 6 | app:384 | +1.51 pp amplification | 7.20-5.69 = 1.51 | ✓ |\n| 7 | exp:109, exp:123 | 5.5× 300-step | 0.308/0.056 = 5.50 | ✓ |\n| 8 | exp:40 | 9.56 pp warmup gap | 90.83-81.27 = 9.56 | ✓ |\n| 9 | exp:92, app:73 | 19% param reduction | 1.46/7.62 = 0.1916 ≈ 19% | ✓ |\n| 10 | app:88 | 18% TTFT improve | (20.1-16.4)/20.1 = 18.41% | ✓ |\n| 11 | app:89 | 19% per-token decrease | (72.0-58.3)/72.0 = 19.03% | ✓ |\n| 12 | exp:130 | 30.5 pp cross-model | 51.50-21.00 = 30.50 | ✓ |\n| 13 | exp:130 | 4.6 pp primary | 64.39-59.84 = 4.55 → 4.6 | ✓ (但 caption 用 4.62) |\n| 14 | app:100 | 2.65 pp from α=2 peak | 66.11-63.46 = 2.65 | ✓ |\n| 15 | method:93 | +1.72 pp α=2.0 over CKA | 66.11-64.39 = 1.72 | ✓ |\n| 16 | app:132 | +1.25 pp MBPP mean | (1.34+1.07+1.34)/3 = 1.25 | ✓ |\n| 17 | exp:81, tab_mbpp:16 | +4.01 pp ShortGPT MBPP | 14.44-10.43 = 4.01 | ✓ |\n| 18 | intro:31, exp:81, tab2 | -1.36 pp ShortGPT GSM8K | 43.37-44.73 = -1.36 | ✓ |\n| 19 | app:244 | 80.1% retention | 72.76/90.83 = 80.11% | ✓ |\n| 20 | app:245 | -7.20, -8.42 Std decline | 66.49-59.29, 59.29-50.87 | ✓ |\n| 21 | app:245 | -8.27, -3.79 CKA decline | 72.18-63.91, 63.91-60.12 | ✓ |\n| 22 | app:213 | Random Δ -0.68, -0.53, -0.38 | 51.25-{50.57,50.72,50.87} | ✓ |\n| 23 | app:212 | Random range 0.30 pp | 50.87-50.57 = 0.30 | ✓ |\n| 24 | app:174, app:210 | CKA seed range 0.37 pp | 64.59-64.22 = 0.37 | ✓ |\n| 25 | app:211 | Std seed range 0.76 pp | 60.20-59.44 = 0.76 | ✓ (但参见 Issue #8) |\n| 26 | app:214 | 0.08 pp SFT diff | 59.29-59.21 = 0.08 | ✓ |\n| 27 | app:280 | 48.60% (243/500) | 243/500 = 48.6% | ✓ |\n| 28 | app:272 | 3.53 stderr | sqrt(0.515*0.485/200) = 0.0353 | ✓ |\n| 29 | tab_math500 caption | 4.62 pp GSM8K SFT gap | 63.91-59.29 = 4.62 | ✓ |\n| 30 | tab_math500 caption | 0.6 pp MATH GRPO gap | 27.6-27.0 = 0.6 | ✓ |\n| 31 | exp:118 | 1.8 pp MATH SFT gap | 27.4-25.6 = 1.8 | ✓ |\n| 32 | app:342 | 2.66, 2.35 floor drops | 64.37-{61.71, 62.02} | ✓ |\n| 33 | app:342 | 0.31 pp floor 0.5/0.6 diff | 62.02-61.71 = 0.31 | ✓ |\n| 34 | concl:5 | 1.8 pp max | MATH-500 α=2.0 +1.8 | ✓ |\n| 35 | exp:33 | 1.45B params | 1.46B 实算 | ≈ |\n| 36 | app:122 | ~8 pp α range MATH-500 | 27.8-21.6 = 6.2 | ⚠ |\n| 37 | exp:78, app:374 | 4× cross-seed σ | 2/0.19 = 10.5× | ⚠ |\n| 38 | intro:10, exp:33 | \"20% MLP channel sparsity\" | 200/784 = 25.5% | ⚠ |\n| 39 | method:17 | G=7 (28/4) | 28/4 = 7 | ✓ |\n\n---\n\n## 总结\n\n### 数据保真度评估\n- **绝大多数数字（>95%）内部一致**：tables 之间、tables 与正文之间、tables 与脚本之间的核心数据高度一致。\n- **派生计算几乎全部正确**（mean、ratio、difference、percentage 等手动验证 39 项中 36 项正确，3 项有小问题）。\n\n### 需立即修复\n1. **gen_fig1_dose_response.py** 硬编码值与 Table 3 不一致（α=0.5/3.0 显著不一致）。应统一数据源——要么重新生成 Fig 1 使用 Table 3 的值，要么修改 Table 3 / Appendix 文字使用 Fig 1 的值（前者更可能正确）。\n\n### 建议修复\n2. \"20% MLP channel sparsity\" 在 intro/exp 重复出现，但实际 MLP 群组比例为 25.5%。可改为 \"20% structured sparsity (≈25% MLP groups, 19% total params)\" 或类似精确表述。\n3. App:122 \"~8 pp\" α SFT range 改为 \"~6 pp\" 更准确。\n4. App:374 \"4× cross-seed σ\" 推导不清楚——重新检查 σ 选择或修改倍数描述。\n\n### 风格/语义问题（非数字错误）\n5. App:109 \"rises from 0.354 to 0.308\" 应改为 \"moves between 0.354 (peak) and 0.308 (step 300)\" 或类似避免方向矛盾。\n6. App:308 \"near-zero KL (<0.001)\" 应改为 \"≈0.001\" 或 \"<0.0012\"，因实际有点超 0.001。\n\n### Orphan / 文件管理\n7. fig2_reward_accuracy.py 是 orphan（生成的 fig 不在论文中使用），且包含与现行数据不一致的硬编码值。建议删除或加注释。\n8. fig1_framework.py 的输出 fig1_framework.pdf 与论文引用的 fig1_method_framework.pdf 文件名不一致，并含 \"+2.2pp advantage\" 等论文不再使用的旧文案。需确认论文用的 fig1_method_framework.pdf 是哪个版本/由哪个脚本生成。\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/audit_paper_numbers.md",
    "content": "# 论文数字提取清单\n\n审计日期: 2026-05-25\n审计范围: docs/paper/{abstract,introduction,method,related_work,experiments,conclusion,limitations,ethics,appendix}.tex + tables/*.tex + figures/paper/gen_*.py\n\n## 统计\n\n- A类(实验结果): ~140个\n- B类(模型/超参): ~35个\n- C类(统计描述): ~25个\n- D类(派生计算): ~30个\n\n---\n\n## 逐文件数字清单\n\n### abstract.tex\n\n| 行号 | 数字 | 上下文 | 分类 | 备注 |\n|------|------|--------|------|------|\n| 1 | 7B | \"7B reasoning model\" | B | DeepSeek-R1-Distill-Qwen-7B |\n| 1 | four (4) | \"across four criteria\" | C | CKA-only/Standard/RASP/Random |\n\n### introduction.tex\n\n| 行号 | 数字 | 上下文 | 分类 | 备注 |\n|------|------|--------|------|------|\n| 7 | 96.5% | \"96.5\\% parameter retention\" | A | 来自 selfhealing2025 外部引用 |\n| 10 | 7B | DeepSeek-R1-Distill-Qwen-7B | B | |\n| 10 | 20% | \"20\\% MLP channel sparsity\" | C | ⚠ 详见一致性检查 |\n| 10 | 4.4 (×) | \"4.4 times the peak RL reward\" | D | 0.354/0.081=4.37→4.4 ✓ |\n| 10 | 1 (pp) | \"within 1 percentage point\" | D | 上界描述 |\n| 17 | 20% | \"20\\% sparsity\" 图1 caption | C | |\n| 17 | 1.14 (pp) | \"$\\|\\Delta\\| \\leq 1.14$\\,pp\" | D | α=2.0 时 +1.14 |\n| 28 | $\\alpha{=}2.0$ | 峰值 α | B | |\n| 28 | 66.11% | GSM8K α=2.0 | A | 对应 Table 3 ✓ |\n| 31 | -1.36 (pp) | ShortGPT GSM8K Δ | A | 43.37-44.73=-1.36 ✓ |\n| 35 | 20-25% | 解耦适用范围 | C | |\n| 35 | $p{<}0.05$ | TOST | A | |\n| 35 | 7 of 8 | TOST 通过 | C | |\n| 35 | 15% | 解耦边界 | C | |\n| 36 | four (4) | 四个评价指标 | C | |\n| 37 | 20% | \"20\\% sparsity\" | C | |\n| 37 | 51-64% | SFT recovery range | A | 51.25-63.91 ✓ |\n| 37 | 1.14 (pp) | \"at most 1.14\\,pp\" | D | α=2.0 |\n| 37 | 300 | training steps | B | |\n\n### method.tex\n\n| 行号 | 数字 | 上下文 | 分类 | 备注 |\n|------|------|--------|------|------|\n| 17 | $n_Q{=}28$ | DeepSeek-R1-Distill-Qwen-7B | B | |\n| 17 | $n_{KV}{=}4$ | | B | |\n| 17 | $G{=}7$ | 28/4=7 | D | ✓ |\n| 17 | 7 Q + 1 KV | GQA group | B | |\n| 29 | 28 | \"28 MLP channel groups\" Layer 27 | B | |\n| 37 | $M{=}512$ | calibration set | C | |\n| 64 | $O(L \\cdot k^2)$ | CKA 计算复杂度 | B | $k \\le 28$ |\n| 65 | 28 | $k \\le 28$ | B | |\n| 65 | <2 min | CKA 计算时间 | A | |\n| 69 | $\\rho \\geq 0.964$ | Spearman 稳定性 | A | 对应 Table |\n| 75 | 40% | per-layer capacity floor | B | $\\tau=0.4$ |\n| 75 | {0.3, 0.4, 0.5, 0.6} | τ ablation | C | |\n| 91 | $\\alpha{=}0$ | reduces to Standard | B | |\n| 93 | $\\alpha{=}2.0$ | 峰值 | B | |\n| 93 | 66.11% | α=2.0 GRPO acc | A | |\n| 93 | +1.72 (pp) | over CKA-only | D | 66.11-64.39=1.72 ✓ |\n| 115 | 20% | sparsity | C | |\n| 122 | 1, 2 | 阶段编号 | B | |\n\n### related_work.tex\n\n| 行号 | 数字 | 上下文 | 分类 | 备注 |\n|------|------|--------|------|------|\n| 10 | 96.5% | selfhealing2025 retention | A | 外部 |\n| 15 | 1.8 (pp) | \"$\\|\\Delta\\| \\leq 1.8$\\,pp\" | D | MATH-500 α=2.0 时的最大值 |\n| 17 | 5-30% | RL 参数更新比例 | A | 外部引用 |\n\n### experiments.tex\n\n| 行号 | 数字 | 上下文 | 分类 | 备注 |\n|------|------|--------|------|------|\n| 18 | 20% | sparsity | C | |\n| 28 | 7B | DeepSeek-R1 | B | |\n| 29 | $N{=}1{,}319$ | GSM8K size | C | |\n| 30 | 90.83% | Unpruned greedy GSM8K | A | |\n| 33 | 20% | structured sparsity | C | ⚠ 详见一致性 |\n| 33 | 200 of 784 | MLP groups | C | 200/784=25.5% ⚠ |\n| 33 | 28 | layers | B | |\n| 33 | ~1.45B | params removed | A | 实际 7.62-6.16=1.46B |\n| 33 | 40% | retention floor | B | |\n| 33 | $\\alpha{=}1.0$ | RASP main | B | |\n| 33 | 512 | TRL default tokens | B | Random |\n| 33 | 1,024 | other methods tokens | B | |\n| 37 | <2% | post-prune accuracy | A | |\n| 38 | 2 (epochs) | SFT | B | |\n| 38 | 7,473 | GSM8K examples SFT | C | |\n| 38 | 37 min | SFT wall time | A | |\n| 38 | $1{\\times}10^{-6}$ | GRPO lr | B | |\n| 38 | $\\beta{=}0.01$ | KL coef | B | |\n| 38 | $T{=}0.4$ | temperature | B | |\n| 38 | 100 | GRPO steps | B | |\n| 38 | 1,000 | GRPO problems | C | |\n| 39 | 3 | seeds | C | |\n| 39 | 64.39% | CKA-only mean | A | |\n| 39 | 0.19 pp | CKA-only std | A | |\n| 39 | 59.84% | Standard mean | A | |\n| 39 | 0.38 pp | Standard std | A | |\n| 39 | $p{<}0.001$ | Welch's t | A | |\n| 40 | 9.56 pp | \"Unpruned\"-warmup gap | D | 90.83-81.27=9.56 ✓ |\n| 40 | 90.83% | pre-warmup | A | |\n| 41 | 2× | RTX PRO 6000 GPUs | B | |\n| 41 | 94 GB | VRAM | B | |\n| 47 | 20% | sparsity | C | |\n| 50 | 0.354 | CKA-only peak reward | A | |\n| 50 | 0.125 | CKA-only min $f_0$ | A | |\n| 51 | 0.14-0.19 | Random reward range | A | |\n| 51 | 0.300 | Random min $f_0$ | A | |\n| 51 | 0.50 | Standard $f_0$ | A | |\n| 51 | 0.081 | Standard peak reward | A | |\n| 51 | 0.675 | RASP $f_0$ | A | |\n| 51 | 0.010 | RASP reward decline | A | |\n| 73 | 4.4× | peak reward gap | D | 0.354/0.081 ✓ |\n| 73 | $\\|\\Delta\\| < 1$ pp | 上界 | D | |\n| 73 | +0.48 | CKA-only Δ | A | 64.39-63.91 ✓ |\n| 73 | +0.55 | Standard Δ | A | 59.84-59.29 ✓ |\n| 73 | -0.53 | Random Δ | A | 50.72-51.25 ✓ |\n| 73 | -0.61 | RASP Δ | A | 60.88-61.49 ✓ |\n| 74 | 20-25% | 解耦范围 | C | |\n| 76 | 15% | 边界 | C | |\n| 76 | 5.69 pp | SFT 15% gap | D | 72.18-66.49 ✓ |\n| 76 | 7.20 pp | GRPO 15% gap | D | 72.76-65.56 ✓ |\n| 76 | 1 pp | 上界 | D | |\n| 76 | 1.14 pp | α=2.0 Δ | D | |\n| 78 | $\\varepsilon{=}2$ pp | TOST margin | B | |\n| 78 | $4\\times$ | 4× cross-seed σ | D | 2/0.19≈10× actually, 2/0.38≈5× — 取近似 |\n| 78 | $N{=}1{,}319$ | TOST samples | C | |\n| 78 | 7/8 | TOST 通过 | C | |\n| 78 | 0.37 pp | seed range | A | 64.59-64.22=0.37 ✓ |\n| 78 | 300 | extended steps | B | |\n| 79 | 2 pp | \"$\\|\\Delta\\| < 2$\\,pp\" MBPP | D | 实际最大 +1.34 |\n| 81 | -1.36 pp | ShortGPT GSM8K | A | |\n| 81 | +4.01 pp | ShortGPT MBPP | A | 14.44-10.43 ✓ |\n| 81 | 1.8 pp | fine-grained 上界 | D | MATH-500 α=2.0 |\n| 90 | {0.5, 1.0, 2.0, 3.0, 4.0} | α 范围 | B | |\n| 90 | 66.11% | α=2.0 peak | A | |\n| 90 | 1.14 pp | 上界 | D | |\n| 90 | 62.77% | α=4.0 | A | |\n| 91 | 23.0% | MATH-500 α=1.0 worst | A | |\n| 91 | 27.2-27.6% | higher-α 集群 | A | |\n| 92 | 30% | sparsity cliff | C | |\n| 92 | 19% | param reduction | D | 1.46/7.62=0.192 ✓ |\n| 92 | ~28% | memory reduction | A | |\n| 102 | $\\mu{=}0.62$ | CKA-only layer CKA mean | A | 实算 0.6202 ✓ |\n| 109 | 5.5× | 300-step gap | D | 0.308/0.056=5.50 ✓ |\n| 116 | $\\mu{=}0.62$ | CKA-only | A | |\n| 116 | $\\mu{=}0.90$ | Standard | A | 实算 0.9039 ✓ |\n| 116 | $\\mu{=}0.92$ | Random | A | 实算 0.9233 ✓ |\n| 116 | $\\mu{=}0.88$ | RASP | A | 实算 0.8822 ✓ |\n| 118 | L0-9 | 早层 | C | |\n| 118 | 72.5% | CKA-only 移除集中度 | A | |\n| 118 | 2.89× | gradient ratio | A | |\n| 118 | 55/56 | 显著层 | C | |\n| 118 | $p{<}0.05$ | | A | |\n| 119 | 22% | CKA-only truncation | A | |\n| 119 | 655 (tokens) | CKA-only mean | A | |\n| 119 | 44% | Standard truncation | A | |\n| 119 | 1,128 (tokens) | Standard mean | A | |\n| 123 | 100, 300 | step extension | B | |\n| 123 | 0.054-0.058 | Standard reward range | A | 与 fig5 数据一致 |\n| 123 | 0.5 | $f_0$ threshold | B | |\n| 123 | 5.5× | gap | D | |\n| 123 | 0.308 | CKA-only step 300 | A | 0.3075 → 0.308 ✓ |\n| 123 | 0.056 | Standard step 300 | A | 0.0562 → 0.056 ✓ |\n| 124 | 10 (steps) | Standard 进入 collapse | B | |\n| 124 | 0.5 | $f_0$ | B | |\n| 124 | 0.35 | CKA-only $f_0$ | A | |\n| 129 | 1.5B | scale | B | |\n| 129 | 1.0% | post-prune Math-7B | A | |\n| 129 | 51.50% | CKA-only Math-7B | A | |\n| 129 | 21.00% | Standard Math-7B | A | |\n| 130 | 30.5 pp | cross-model gap | D | 51.50-21.00=30.50 ✓ |\n| 130 | 4.6 pp | primary | D | 64.39-59.84=4.55, rounded 4.6 ⚠ |\n\n### conclusion.tex\n\n| 行号 | 数字 | 上下文 | 分类 | 备注 |\n|------|------|--------|------|------|\n| 5 | 20-25% | sparsity range | C | |\n| 5 | mean \\|Δ\\| = 0.54 pp | four criteria | D | (0.48+0.55+0.61+0.53)/4=0.5425 ✓ |\n| 5 | 1.8 pp | max across benchmarks | D | MATH-500 α=2.0 |\n| 5 | 4.4× | peak reward gap | D | |\n| 6 | 20% | sparsity | C | |\n| 6 | <2% | post-prune | A | |\n| 6 | 51-64% | recovery range | A | |\n| 6 | 300 | steps | B | |\n| 9 | ~100 | diagnostic steps | B | |\n\n### limitations.tex\n\n| 行号 | 数字 | 上下文 | 分类 | 备注 |\n|------|------|--------|------|------|\n| 3 | 两个 (7B, 1.5B) | Qwen2.5 模型 | C | |\n\n### ethics.tex\n\n无数字。\n\n### appendix.tex\n\n| 行号 | 数字 | 上下文 | 分类 | 备注 |\n|------|------|--------|------|------|\n| 16 | $2 \\times 10^{-5}$ | SFT lr | B | |\n| 16 | $1 \\times 10^{-6}$ | GRPO lr | B | |\n| 17 | 1, 1 | batch size | B | |\n| 18 | 8, 1 | grad accumulation | B | |\n| 19 | 2,048 | max seq len | B | |\n| 20 | 1,024, 512 | max new tokens | B | |\n| 22 | 2 epochs / 100 steps | | B | |\n| 23 | 0.01 | KL β | B | |\n| 24 | 0.4 | sampling temp | B | |\n| 25 | 8 | generations per prompt | B | |\n| 28 | 50 | reward_desert_patience | B | |\n| 80 | 72.0 | Dense TPS | A | |\n| 80 | 20.1 | Dense TTFT (ms) | A | |\n| 80 | 13.9 | Dense per-token (ms) | A | |\n| 80 | 7.62 | Dense params (B) | A | |\n| 81 | 58.3 | CKA TPS | A | |\n| 81 | 16.4 | CKA TTFT | A | |\n| 81 | 16.7 | CKA per-token | A | |\n| 81 | 6.16 | CKA params | A | |\n| 82 | 58.2 | Standard TPS | A | |\n| 82 | 16.4 | Standard TTFT | A | |\n| 82 | 16.7 | Standard per-token | A | |\n| 82 | 6.16 | Standard params | A | |\n| 87 | ~28% | memory reduction | A | |\n| 88 | 18% | TTFT improvement | D | (20.1-16.4)/20.1=18.4% ✓ |\n| 88 | 20.1→16.4 | | A | |\n| 89 | 19% | per-token decrease | D | (72.0-58.3)/72.0=19.0% ✓ |\n| 89 | 72.0→58.3 | | A | |\n| 89 | 13.9→16.7 | | A | |\n| 90 | 58.3 vs 58.2 | identical throughput | A | |\n| 97 | α=2.0 | peak | B | |\n| 97 | 64.97% | SFT α=2.0 | A | |\n| 97 | 66.11% | GRPO α=2.0 | A | |\n| 97 | +1.14 pp | Δ | A | |\n| 98 | α=0.5 | | B | |\n| 98 | 60.73% | SFT α=0.5 | A | ⚠ 与 fig1 数据不一致 |\n| 98 | 61.18% | GRPO α=0.5 | A | ⚠ 与 fig1 数据不一致 |\n| 99 | α=1.0 | | B | |\n| 99 | 0.061 | RASP peak reward | A | |\n| 99 | 60.88% | RASP GRPO | A | |\n| 99 | -0.61 pp | Δ | A | |\n| 100 | α=3.0 | | B | |\n| 100 | 64.14% | SFT α=3.0 | A | |\n| 100 | 63.46% | GRPO α=3.0 | A | |\n| 100 | -0.68 pp | Δ | A | |\n| 100 | 2.65 pp | drop from peak | D | 66.11-63.46=2.65 ✓ |\n| 101 | α=4.0 | | B | |\n| 101 | 62.77% | GRPO α=4.0 | A | |\n| 101 | 61.94% | SFT α=4.0 | A | |\n| 101 | +0.83 pp | Δ | A | |\n| 101 | 0.146→0.256→0.198 | reward trajectory | A | |\n| 102 | 1.14 pp | 上界 | D | |\n| 107 | 100, 300 | steps | B | |\n| 108 | 64.37% | CKA-only seed 42 at 300 | A | |\n| 108 | 59.29% | Standard at 300 | A | |\n| 108 | 0.38 pp | std | A | |\n| 109 | 0.354 | peak step 100 | A | ⚠ peak at step 50 实际是 0.3544 |\n| 109 | 0.308 | step 300 | A | |\n| 110 | 0.054-0.058 | Standard range | A | |\n| 117 | 27.4%, 25.6%, 21.6%, 16.6% | MATH-500 SFT | A | |\n| 117 | 27.6%, 27.0%, 23.0%, 15.0% | MATH-500 GRPO | A | |\n| 118 | 4.6 pp | GSM8K SFT gap | D | 63.91-59.29=4.62 ⚠ 论文写4.6 |\n| 118 | 1.8 pp | MATH-500 SFT gap | D | 27.4-25.6=1.8 ✓ |\n| 118 | 0.6 pp | MATH-500 GRPO gap | D | 27.6-27.0=0.6 ✓ |\n| 120 | 53.0% | dense MATH-500 | A | |\n| 120 | 90.83% | dense GSM8K | A | |\n| 120 | 2,048 | token limit | B | |\n| 121 | 22% | CKA truncation | A | |\n| 121 | 655 | CKA mean tokens | A | |\n| 121 | 44% | Standard truncation | A | |\n| 121 | 1,128 | Standard mean tokens | A | |\n| 122 | ~8 pp | α SFT range MATH-500 | A | ⚠ 实算 6.2 pp |\n| 122 | ~2 pp | stderr | A | |\n| 122 | 2048 | token limit | B | |\n| 128 | $N{=}374$ | MBPP size | C | |\n| 132 | +1.25 pp | MBPP mean | D | (1.34+1.07+1.34)/3=1.25 ✓ |\n| 132 | $N{=}374$ | | C | |\n| 132 | ~1.7 pp | stderr | A | |\n| 142 | 256/512/1024 | calibration sizes | C | |\n| 142 | 0.964 to 0.979 | Spearman range | A | 对应表 |\n| 147 | $N{=}200$ | gradient samples | C | |\n| 158 | 2.89× | CKA vs Standard ratio | A | |\n| 158 | 55/56 | sig layers | C | |\n| 159 | 2.26× | CKA vs RASP | A | |\n| 159 | 56/56 | | C | |\n| 160 | 1.28× | RASP vs Standard | A | |\n| 160 | 45/56 | | C | |\n| 165 | 64.39%, 60.88%, 59.84% | recovery hierarchy | A | |\n| 172 | 64.37% | seed 42 | A | |\n| 172 | 64.22% | seed 123 | A | |\n| 172 | 64.59% | seed 456 | A | |\n| 172 | 64.39% | mean | A | |\n| 172 | 0.19 pp | std | A | |\n| 173 | 59.84% | Standard mean | A | |\n| 173 | 0.38 pp | std | A | |\n| 174 | 4.55 pp | gap | D | 64.39-59.84 ✓ |\n| 184 | 4% | Standard 30% | A | |\n| 184 | 1.6% | CKA 30% | A | |\n| 184 | 0% | RASP 30% | A | |\n| 200 | 64.39, 0.19, 3 | multi-seed table | A | |\n| 201 | 59.84, 0.38, 3 | | A | |\n| 202 | 60.88, 1 | | A | |\n| 203 | 50.72, 0.15, 3 | | A | |\n| 205 | 72.76, 0.57, 3 | 15% CKA | A | |\n| 206 | 65.56, 0.50, 3 | 15% Std | A | |\n| 210 | 4.55 pp | gap 20% | D | ✓ |\n| 210 | 64.22--64.59% | CKA range | A | |\n| 210 | 59.44--60.20% | Standard range | A | ⚠ 实算 seed456 GRPO=60.28 (>60.20) |\n| 211 | 0.76 pp vs 0.37 pp | observed ranges | D | 60.20-59.44=0.76, 64.59-64.22=0.37 |\n| 212 | 50.57%, 50.72%, 50.87% | Random seeds | A | |\n| 212 | 0.15 pp | σ | A | |\n| 212 | 0.30 pp | range | D | 50.87-50.57=0.30 ✓ |\n| 212 | 51.25% | SFT | A | |\n| 213 | -0.68, -0.53, -0.38 pp | Random Δ | D | 51.25-50.57/72/87 ✓ |\n| 214 | 59.21% vs 59.29% | Standard SFT 差异 | A | |\n| 214 | 0.08 pp | Δ | D | ✓ |\n| 215 | 7.20 pp | 15% gap | D | ✓ |\n| 215 | 72.76 vs 65.56 | | A | |\n| 215 | $t{\\approx}16.4$ | | A | |\n| 215 | $p{<}0.001$ | | A | |\n| 215 | 72.10--73.09%, 65.13--65.43% | seed ranges 15% | A | |\n| 229-237 | cross-sparsity 表 | (见表) | A | |\n| 243 | +7.20 pp | 15% gap | D | ✓ |\n| 244 | 80.1% | retention | D | 72.76/90.83=80.11% ✓ |\n| 245 | -7.20, -8.42 | Standard decline | D | 66.49-59.29, 59.29-50.87 ✓ |\n| 245 | -8.27, -3.79 | CKA decline | D | 72.18-63.91, 63.91-60.12 ✓ |\n| 246 | 0.008 | Standard 25% peak reward | A | |\n| 256 | 35.48, 22.29, 26.16 | 1.5B accs | A | |\n| 256 | -0.15, -0.61 pp | 1.5B Δ | A | |\n| 257 | 49.81% | 1.5B dense | A | |\n| 257 | 90.83% | 7B dense | A | |\n| 265 | $N{=}200$ | Math-7B size | C | |\n| 272 | 1.0%, 51.50%, 27.0% | CKA Math-7B | A | |\n| 272 | 3.53 (stderr) | binomial | D | sqrt(0.515*0.485/200)=0.0353 ✓ |\n| 273 | 18.5%, 21.00%, 36.5% | Standard Math-7B | A | |\n| 273 | 2.88 stderr | | D | sqrt(0.21*0.79/200)=0.0288 ✓ |\n| 278 | 1.0%, 18.5%, 51.50%, 21.00% | Math-7B 复述 | A | |\n| 280 | 40%, 48.60%, 243/500, 83.8%, 2048 | EOS/GRPO/truncation | A | 243/500=48.6% ✓ |\n| 285 | 28 layers | | B | |\n| 285 | 20% | sparsity | C | |\n| 286 | L0--9, 72.5% | CKA early-layer | A | |\n| 286 | L16--27 | preserved late | C | |\n| 287 | L16-18, L22, L25-26 | Standard distribution | C | |\n| 290 | 65 (groups) | CKA exclusive | A | |\n| 290 | L6-9, L27 | | C | |\n| 291 | 46+ (groups) | Standard exclusive | A | |\n| 291 | L16-18, L22, L25-26 | | C | |\n| 293 | $\\mu{=}0.62$, 0.90 | | A | |\n| 304 | <0.001 | RASP KL | A | |\n| 304 | ~0.004-0.005 | Random KL | A | |\n| 308 | $\\alpha{=}1.0$ | | B | |\n| 308 | <0.001 | KL | A | ⚠ 实际 RASP max=0.001119 (微超) |\n| 309 | 0.001-0.003 | CKA/Standard KL | A | 数据范围合理 |\n| 309 | ~0.004-0.005 | Random | A | |\n| 313 | 0.001, 0.5, 1.0 | depth-first synthetic | B | |\n| 313 | 20% | sparsity | C | |\n| 317 | ~10%, ~8% | SFT/GRPO depth-first | A | |\n| 317 | $N{\\approx}50$--88 | early stopped | C | |\n| 326 | $N{=}1{,}319$ | | C | |\n| 326 | 100 steps | | B | |\n| 326 | $\\tau{=}0.4$ | default | B | |\n| 332 | 0.3, 65.05%, +0.68 | floor 0.3 | A | |\n| 333 | 0.4, 64.37% | default | A | |\n| 334 | 0.5, 61.71%, -2.66 | | A | 64.37-61.71=2.66 ✓ |\n| 335 | 0.6, 62.02%, -2.35 | | A | 64.37-62.02=2.35 ✓ |\n| 342 | +0.68 pp | | D | |\n| 342 | -2.66, -2.35 pp | | D | |\n| 342 | 0.31 pp | 0.5/0.6 diff | D | 62.02-61.71=0.31 ✓ |\n| 342 | ~1.3 pp | stderr | A | |\n| 348 | $N{=}1{,}319$ | | C | |\n| 348 | 20% | sparsity | C | |\n| 350 | $\\varepsilon$ | margin | B | |\n| 361-369 | TOST 表数值 | (per-seed Δ) | A | 详见一致性检查 |\n| 374 | 2 pp | $\\varepsilon$ | B | |\n| 374 | 4× | σ multiplier | D | 2/0.19≈10.5× ⚠ 论文说4× (应基于Standard σ=0.38?: 2/0.38=5.3 也不是4) |\n| 374 | 0.19 pp | σ | A | |\n| 375 | 2 pp | | B | |\n| 375 | 7/8 | | C | |\n| 375 | -0.99 pp | borderline | A | |\n| 375 | $p{=}0.069$ | | A | |\n| 376 | 3 pp | | B | |\n| 376 | 8/8 | | C | |\n| 376 | $p{<}0.002$ | | A | |\n| 377 | 1 pp | | B | |\n| 377 | $N{=}1{,}319$ | | C | |\n| 384 | 15% | | C | |\n| 384 | +1.51 pp | CKA-guided amp | D | 7.20-5.69=1.51 ✓ |\n| 388 | 96.5% | external retention | A | |\n| 388 | 20-25% | sparsity | C | |\n\n### tables/tab1_recovery_gradient.tex\n\n| 数字 | 上下文 | 备注 |\n|------|--------|------|\n| 20% | sparsity | |\n| 0.354, 0.285, 0.125 | CKA peak/mean/min $f_0$ | |\n| 0.190, 0.164, 0.300 | Random | |\n| 0.081, 0.050, 0.500 | Standard | |\n| 0.061, 0.031, 0.675 | RASP | |\n\n### tables/tab2_decoupling.tex\n\n| 数字 | 上下文 | 备注 |\n|------|--------|------|\n| $N{=}1{,}319$, 20% | |\n| 81.27, 81.27, 0.00, 0.669 | Unpruned | |\n| 64.97, 66.11, +1.14 | α=2.0 | |\n| 63.91, 64.39, ±0.19, +0.48, 0.354 | CKA-only | |\n| 59.29, 59.84, ±0.38, +0.55, 0.081 | Standard | |\n| 61.49, 60.88, -0.61, 0.061 | RASP α=1.0 | |\n| 51.25, 50.72, ±0.15, -0.53, 0.190 | Random | |\n| 44.73, 43.37, -1.36 | ShortGPT | |\n\n### tables/tab_math500.tex\n\n| 数字 | 上下文 | 备注 |\n|------|--------|------|\n| $N{=}500$, 2048 tokens | |\n| 0.6 pp, 4.62 pp | GRPO/GSM8K SFT gaps in caption | 4.62=63.91-59.29 ⚠ 主文写4.6 |\n| 53.0 | dense | |\n| 20% method: 27.4/27.6, 25.6/27.0, 21.6/23.0, 16.6/15.0 | |\n| Δ: +0.2, +1.4, +1.4, -1.6 | |\n| α: 26.8/26.8, 25.6/27.4, 23.6/--, 27.8/27.2 | 0.5/2.0/3.0/4.0 |\n| Δ α: +0.0, +1.8, --, -0.6 | |\n| 25%: 18.8/17.6, 15.4/-- | -1.2, -- | |\n| 73.6% at 4096 | dense truncation | |\n\n### tables/tab_mbpp.tex\n\n| 数字 | 上下文 | 备注 |\n|------|--------|------|\n| $N{=}374$ | |\n| ~75% | code capability loss | |\n| ~1 pp | range | |\n| +4.01 pp, 1.55 stderr | ShortGPT | |\n| Dense: 53.48 | |\n| CKA 20%: 12.83/14.17/+1.34 | |\n| Standard 20%: 12.03/13.10/+1.07 | |\n| RASP α=1.0 20%: 11.76/13.10/+1.34 | |\n| ShortGPT 20%: 10.43/14.44/+4.01 | |\n\n### tables/tab_cka_stability.tex\n\n| 数字 | 上下文 | 备注 |\n|------|--------|------|\n| $\\rho \\geq 0.964$, 0.964/0.979 | 256/512/1024 | |\n\n### tables/table3_alpha.tex\n\n| 数字 | 上下文 | 备注 |\n|------|--------|------|\n| $N{=}1{,}319$, 20% | |\n| α=0.5: 60.73/61.18/+0.45 | |\n| α=1.0: 61.49/60.88/-0.61 | |\n| α=2.0: 64.97/66.11/+1.14 | |\n| α=3.0: 64.14/63.46/-0.68 | |\n| α=4.0: 61.94/62.77/+0.83 | |\n\n### tables/table4_sparsity_cliff.tex\n\n| 数字 | 上下文 | 备注 |\n|------|--------|------|\n| 30% | sparsity | |\n| Standard: N=200, 4%, 5.5% EOS | |\n| RASP α=1: N=200, 0%, 3.0% EOS | |\n| CKA: N=500, 1.6%, 8/500 | |\n\n### tables/tab5_cross_scale.tex\n\n| 数字 | 上下文 | 备注 |\n|------|--------|------|\n| 20%, 100 steps | |\n| CKA: 0.354/64.39, 0.238/35.48 | 7B/1.5B |\n| Standard: 0.081/59.84, 0.084/22.29 | |\n| RASP α=1: 0.061/60.88, 0.099/26.16 | |\n| Random: 0.190 | 7B only |\n\n---\n\n## 内部一致性检查\n\n### ✅ 已验证一致\n\n| 数字 | 位置1 | 位置2 | 结果 |\n|------|-------|-------|------|\n| 64.39% CKA-only GRPO | exp.tex:39 | tab2:13 | ✓ |\n| 59.84% Standard GRPO | exp.tex:39 | tab2:14 | ✓ |\n| 4.4× peak reward | intro:10, exp:73, concl:5 | 0.354/0.081=4.37 | ✓ |\n| mean \\|Δ\\|=0.54 | concl:5 | (0.48+0.55+0.61+0.53)/4=0.5425 | ✓ |\n| 90.83% Unpruned | exp:30, exp:40, app:120, app:257 | | ✓ |\n| 81.27% Unpruned post-SFT | tab2:11 | exp:40 (隐含 9.56 pp gap) | ✓ |\n| $f_0$ 值 (0.125/0.300/0.500/0.675) | exp:50, tab1, fig3 | | ✓ |\n| α=2.0 peak (64.97/66.11/+1.14) | intro:28, method:93, exp:90, app:97, tab2:12, tab3:12 | | ✓ |\n| ShortGPT GSM8K -1.36 pp | intro:31, exp:81, tab2:18 | | ✓ |\n| ShortGPT MBPP +4.01 pp | exp:81, tab_mbpp:16 | | ✓ |\n| 7.20 pp 15% GRPO gap | exp:76, app:215, app:243 | | ✓ |\n| 5.5× 300-step gap | exp:109, exp:123 | | ✓ |\n| 19% / ~28% param/mem reduction | exp:92, app:73, app:87 | | ✓ |\n| RASP α=1.0 reward 0.061 | exp:51, tab1, tab2:15, tab5 | | ✓ |\n| 51-64% SFT recovery range | intro:37, concl:6 | tab2 实际 51.25-63.91 | ✓ |\n| $\\|\\Delta\\| ≤ 1.14$ pp | intro:17, exp:76, app:102 | α=2.0 最大 | ✓ |\n| 1.5B 三方法排序 | exp:129 | tab5 | ✓ |\n| 30.5 pp cross-model | exp:130 | 51.50-21.00 | ✓ |\n| Spearman ρ ≥ 0.964 | method:69 | tab_cka_stability | ✓ |\n| 2.89× gradient ratio | exp:118, app:158 | | ✓ |\n\n### ⚠ 发现的问题（按严重度排序）\n\n| # | 严重度 | 位置1 | 位置2 | 差异说明 |\n|---|--------|-------|-------|---------|\n| **1** | **HIGH** | gen_fig1_dose_response.py:32-33 | table3_alpha.tex:10-14 | **Fig 1 的 SFT/GRPO 硬编码值与 Table 3 不一致**（详见下方） |\n| **2** | **MEDIUM** | intro.tex:10 \"20% MLP channel sparsity\"; exp.tex:33 \"20% structured sparsity, all removing 200 of 784 MLP channel groups\" | app.tex:88 \"Pruning reduces parameters by 19%\" | **200/784 = 25.5% MLP groups, 不是 20%**。看似\"20% sparsity\"是相对于总模型参数（19% rounded），但 intro 写 \"MLP channel sparsity\" 是术语错误 |\n| **3** | **MEDIUM** | app.tex:122 \"SFT accuracy varies by ${\\sim}$8\\,pp across $\\alpha$ values\" | tab_math500.tex α SFT 值 | 实际 max-min = 27.8-21.6 = 6.2 pp，\"~8 pp\" 偏大 |\n| **4** | **LOW** | exp.tex:130 \"4.6 pp difference on the primary model\" | exp.tex:39, tab2 64.39-59.84=4.55 | 4.55 rounded to 4.6（合理近似）；但 tab_math500.tex caption 写 \"4.62 pp\"——同一数字两种舍入并存 |\n| **5** | **LOW** | exp.tex:78 \"$4\\times$ cross-seed $\\sigma$\" | app.tex:374 \"$2$\\,pp because it is approximately $4\\times$ the observed cross-seed standard deviation ($\\sigma{=}0.19$\\,pp for CKA-only)\" | 2/0.19 = 10.5×，不是 4×。若以 Standard σ=0.38 计算 = 5.3×，也不是 4×。\"4×\" 数字来源不明 |\n| **6** | **LOW** | app.tex:308 \"near-zero KL ($<$0.001)\" | gen_fig_appendix_kl.py:42 RASP max=0.001119 | RASP KL 实际值有少数点 (0.001022, 0.001119, 0.001043) 略超 0.001 |\n| **7** | **LOW** | app.tex:109 \"CKA-only reward rises from 0.354 (peak at step 100) to 0.308 (step 300)\" | 0.354 > 0.308 | \"rises from X to Y\" 当 X > Y 时是反向表述（语义错误，非数字错误） |\n| **8** | **LOW** | app.tex:210 \"Standard: 59.44--60.20\\%\" | 从 TOST 反推 seed 456 GRPO = 59.29 + 0.99 = **60.28**, 不是 60.20 | 范围上界与重算 0.08 pp 差异 |\n| **9** | **LOW** | exp.tex:33 \"~1.45B parameters\" pruned | app.tex 7.62-6.16 = 1.46B | 1.45 vs 1.46 rounding |\n| **10** | **VERY LOW** | exp.tex:81, related:15 \"$\\|\\Delta\\| \\leq 1.8$\\,pp\" fine-grained | exp.tex:73 \"$\\|\\Delta\\| < 1$ pp\" 20% sparsity | 不冲突：20% 是 <1 pp，1.8 是涵盖 α=2.0 时的最大值。表述兼容但需读者解读 |\n\n### 详细分析：Issue #1（Fig 1 数据不一致）\n\n```\n              gen_fig1_dose_response.py     table3_alpha.tex / app:97-101\nα=0.5  SFT/GRPO:  64.52 / 65.05    vs   60.73 / 61.18    ⚠ 差异约 4 pp!\nα=1.0  SFT/GRPO:  61.49 / 60.88    vs   61.49 / 60.88    ✓ 一致\nα=2.0  SFT/GRPO:  64.97 / 66.11    vs   64.97 / 66.11    ✓ 一致\nα=3.0  SFT/GRPO:  64.06 / 64.59    vs   64.14 / 63.46    ⚠ GRPO 差 1.13 pp!\nα=4.0  SFT/GRPO:  62.02 / 62.77    vs   61.94 / 62.77    ⚠ SFT 差 0.08 pp (微差)\n```\n\n**结论**：Fig 1 中 α=0.5 与 α=3.0 的数据明显与 Table 3 / Appendix text 不一致；α=4.0 SFT 有小差。Figure caption 的 \"$|\\Delta| \\leq 1.14$ pp\" 描述在两个数据集上都成立（因 α=2.0 给出 +1.14），所以读者不会从 caption 发现矛盾，但内部数据源不统一。\n\n**疑似原因**：Fig 1 数据可能是早期实验值（pre-rerun）；Table 3 是后续重跑值。需检查 W&B / 原始日志确认哪个为真。\n\n### 详细分析：Issue #2（\"20% sparsity\" 术语）\n\n- `intro.tex:10`: \"20\\% MLP channel sparsity\"\n- `intro.tex:37`: \"20\\% sparsity\"\n- `intro.tex:35`: \"20--25\\% fine-grained MLP sparsity\"\n- `exp.tex:33`: \"20\\% structured sparsity, all removing 200 of 784 MLP channel groups across 28 layers (${\\sim}$1.45B parameters)\"\n- `exp.tex:92`: \"pruning reduces parameters by 19\\%\"\n- `app.tex:73`: \"Pruning reduces parameters by 19\\%\"\n\n**数学**：\n- 200/784 = **25.5%** MLP channel groups\n- 1.46B/7.62B = **19.2%** total parameters\n- \"20%\" 既不等于 25.5%（MLP channels）也不精确等于 19.2%（total params）\n\n**推测**：作者用 \"20% structured sparsity\" 作为目标设定值（target sparsity），但实际去掉的 MLP groups 比例（25.5%）和总参数比例（19%）都不是 20%。在 intro 写 \"20\\% MLP channel sparsity\" 是不准确（应该是 25.5%）。这是术语滥用，但若读者按\"约 20% reduction\"理解则可接受。\n\n---\n\n## 图表脚本数据源\n\n| 脚本 | 输出文件 | 数据来源 | 硬编码数据点 | 论文引用 |\n|------|---------|---------|-------------|---------|\n| gen_fig1_dose_response.py | fig1_dose_response.pdf | 硬编码 | sft_acc=[64.52,61.49,64.97,64.06,62.02], grpo_acc=[65.05,60.88,66.11,64.59,62.77], CKA baseline=64.39 | intro.tex:16 ⚠ Issue #1 |\n| gen_fig1_framework.py | fig1_framework.pdf | 硬编码 (示意图) | \"+2.2pp advantage\" 标注（论文文本中未提及）；\"Peak 0.081\" Standard, \"Peak 0.061\" RASP, collapse step 90 / step 10 | (论文引用 fig1_method_framework.pdf, 文件名不同；脚本与论文图可能不是同一来源) |\n| gen_fig2_reward_accuracy.py | fig2_reward_accuracy.pdf | 硬编码 | RASP grpo=61.87, Standard grpo=58.91 ⚠ 与现行 Table 2 不一致 | **未被引用**（orphan figure） |\n| gen_fig2_reward_trajectories.py | fig2_reward_trajectories.pdf | 硬编码 | unpruned/CKA/Random/Standard/RASP 各 step reward 序列；CKA peak 0.3544 (step 50), Standard 0.0813 (step 40), Random 0.190 (step 70), RASP 0.06125 (step 50) | exp.tex:9 ✓ |\n| gen_fig3_collapse_dynamics.py | fig3_collapse_dynamics.pdf | 硬编码 | $f_0$ 与 grad_norm 序列；CKA min $f_0$=0.125, Random=0.300, Standard=0.500, RASP=0.675 | exp.tex:15 ✓ |\n| gen_fig4_cka_heatmap.py | fig4_cka_heatmap.pdf | 硬编码 | 28 层 CKA(dense, pruned)；μ 实算: CKA=0.6202, Standard=0.9039, Random=0.9233, RASP=0.8822 | exp.tex:101 ✓ |\n| gen_fig5_extended_training.py | fig5_extended_training.pdf | 硬编码 | Standard 300-step reward {150:0.055, 200:0.054, 250:0.058, 300:0.0562}, CKA 300-step reward {300:0.3075} 等 | exp.tex:108 ✓ |\n| gen_fig_appendix_kl.py | fig_appendix_kl.pdf | 硬编码 (注释: \"W&B/server logs 2026-05-18\") | KL 序列；RASP max=0.001119 略超 \"<0.001\" claim | app.tex:303 ✓ |\n| gen_fig_sft_grpo_scatter.py | fig_sft_grpo_scatter.pdf | 硬编码 | 与 Table 2/3/cross_sparsity 一致 | exp.tex:67 ✓ |\n| (无脚本) | fig_intra_layer_cka.pdf | unknown | — | method.tex:28 |\n| (无脚本) | fig_pruning_decisions.png | unknown | — | method.tex:114 |\n| (无脚本) | fig1_method_framework.pdf | unknown (脚本 gen_fig1_framework.py 输出名不同) | — | intro.tex:42 |\n\n---\n\n## D类派生计算验证\n\n| # | 位置 | 论文写的 | 推导过程 | 正确? |\n|---|------|----------|---------|-------|\n| 1 | concl:5 | mean \\|Δ\\| = 0.54 pp | (0.48+0.55+0.61+0.53)/4 = 0.5425 | ✓ |\n| 2 | intro:10, exp:73, concl:5 | 4.4× peak reward gap | 0.354/0.081 = 4.37 → 4.4 | ✓ |\n| 3 | exp:39, app:174, app:210 | 4.55 pp gap | 64.39-59.84 = 4.55 | ✓ |\n| 4 | exp:76, app:215, app:243 | 7.20 pp gap (15%) | 72.76-65.56 = 7.20 | ✓ |\n| 5 | exp:76 | 5.69 pp SFT 15% gap | 72.18-66.49 = 5.69 | ✓ |\n| 6 | app:384 | +1.51 pp amplification | 7.20-5.69 = 1.51 | ✓ |\n| 7 | exp:109, exp:123 | 5.5× 300-step | 0.308/0.056 = 5.50 | ✓ |\n| 8 | exp:40 | 9.56 pp warmup gap | 90.83-81.27 = 9.56 | ✓ |\n| 9 | exp:92, app:73 | 19% param reduction | 1.46/7.62 = 0.1916 ≈ 19% | ✓ |\n| 10 | app:88 | 18% TTFT improve | (20.1-16.4)/20.1 = 18.41% | ✓ |\n| 11 | app:89 | 19% per-token decrease | (72.0-58.3)/72.0 = 19.03% | ✓ |\n| 12 | exp:130 | 30.5 pp cross-model | 51.50-21.00 = 30.50 | ✓ |\n| 13 | exp:130 | 4.6 pp primary | 64.39-59.84 = 4.55 → 4.6 | ✓ (但 caption 用 4.62) |\n| 14 | app:100 | 2.65 pp from α=2 peak | 66.11-63.46 = 2.65 | ✓ |\n| 15 | method:93 | +1.72 pp α=2.0 over CKA | 66.11-64.39 = 1.72 | ✓ |\n| 16 | app:132 | +1.25 pp MBPP mean | (1.34+1.07+1.34)/3 = 1.25 | ✓ |\n| 17 | exp:81, tab_mbpp:16 | +4.01 pp ShortGPT MBPP | 14.44-10.43 = 4.01 | ✓ |\n| 18 | intro:31, exp:81, tab2 | -1.36 pp ShortGPT GSM8K | 43.37-44.73 = -1.36 | ✓ |\n| 19 | app:244 | 80.1% retention | 72.76/90.83 = 80.11% | ✓ |\n| 20 | app:245 | -7.20, -8.42 Std decline | 66.49-59.29, 59.29-50.87 | ✓ |\n| 21 | app:245 | -8.27, -3.79 CKA decline | 72.18-63.91, 63.91-60.12 | ✓ |\n| 22 | app:213 | Random Δ -0.68, -0.53, -0.38 | 51.25-{50.57,50.72,50.87} | ✓ |\n| 23 | app:212 | Random range 0.30 pp | 50.87-50.57 = 0.30 | ✓ |\n| 24 | app:174, app:210 | CKA seed range 0.37 pp | 64.59-64.22 = 0.37 | ✓ |\n| 25 | app:211 | Std seed range 0.76 pp | 60.20-59.44 = 0.76 | ✓ (但参见 Issue #8) |\n| 26 | app:214 | 0.08 pp SFT diff | 59.29-59.21 = 0.08 | ✓ |\n| 27 | app:280 | 48.60% (243/500) | 243/500 = 48.6% | ✓ |\n| 28 | app:272 | 3.53 stderr | sqrt(0.515*0.485/200) = 0.0353 | ✓ |\n| 29 | tab_math500 caption | 4.62 pp GSM8K SFT gap | 63.91-59.29 = 4.62 | ✓ |\n| 30 | tab_math500 caption | 0.6 pp MATH GRPO gap | 27.6-27.0 = 0.6 | ✓ |\n| 31 | exp:118 | 1.8 pp MATH SFT gap | 27.4-25.6 = 1.8 | ✓ |\n| 32 | app:342 | 2.66, 2.35 floor drops | 64.37-{61.71, 62.02} | ✓ |\n| 33 | app:342 | 0.31 pp floor 0.5/0.6 diff | 62.02-61.71 = 0.31 | ✓ |\n| 34 | concl:5 | 1.8 pp max | MATH-500 α=2.0 +1.8 | ✓ |\n| 35 | exp:33 | 1.45B params | 1.46B 实算 | ≈ |\n| 36 | app:122 | ~8 pp α range MATH-500 | 27.8-21.6 = 6.2 | ⚠ |\n| 37 | exp:78, app:374 | 4× cross-seed σ | 2/0.19 = 10.5× | ⚠ |\n| 38 | intro:10, exp:33 | \"20% MLP channel sparsity\" | 200/784 = 25.5% | ⚠ |\n| 39 | method:17 | G=7 (28/4) | 28/4 = 7 | ✓ |\n\n---\n\n## 总结\n\n### 数据保真度评估\n- **绝大多数数字（>95%）内部一致**：tables 之间、tables 与正文之间、tables 与脚本之间的核心数据高度一致。\n- **派生计算几乎全部正确**（mean、ratio、difference、percentage 等手动验证 39 项中 36 项正确，3 项有小问题）。\n\n### 需立即修复\n1. **gen_fig1_dose_response.py** 硬编码值与 Table 3 不一致（α=0.5/3.0 显著不一致）。应统一数据源——要么重新生成 Fig 1 使用 Table 3 的值，要么修改 Table 3 / Appendix 文字使用 Fig 1 的值（前者更可能正确）。\n\n### 建议修复\n2. \"20% MLP channel sparsity\" 在 intro/exp 重复出现，但实际 MLP 群组比例为 25.5%。可改为 \"20% structured sparsity (≈25% MLP groups, 19% total params)\" 或类似精确表述。\n3. App:122 \"~8 pp\" α SFT range 改为 \"~6 pp\" 更准确。\n4. App:374 \"4× cross-seed σ\" 推导不清楚——重新检查 σ 选择或修改倍数描述。\n\n### 风格/语义问题（非数字错误）\n5. App:109 \"rises from 0.354 to 0.308\" 应改为 \"moves between 0.354 (peak) and 0.308 (step 300)\" 或类似避免方向矛盾。\n6. App:308 \"near-zero KL (<0.001)\" 应改为 \"≈0.001\" 或 \"<0.0012\"，因实际有点超 0.001。\n\n### Orphan / 文件管理\n7. fig2_reward_accuracy.py 是 orphan（生成的 fig 不在论文中使用），且包含与现行数据不一致的硬编码值。建议删除或加注释。\n8. fig1_framework.py 的输出 fig1_framework.pdf 与论文引用的 fig1_method_framework.pdf 文件名不一致，并含 \"+2.2pp advantage\" 等论文不再使用的旧文案。需确认论文用的 fig1_method_framework.pdf 是哪个版本/由哪个脚本生成。\n"
  }
}
````

</details>

---

### Tool result

_source line 79 · 2026-05-25T19:56:13.162977+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/audit_paper_numbers.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-25T19:56:13.163128+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Read all main tex files and tables', 'status': 'completed', 'activeForm': 'Reading all main tex files and tables'}, {'content': 'Read all gen_fig*.py scripts for hardcoded data', 'status': 'completed', 'activeForm': 'Reading all gen_fig*.py scripts'}, {'content': 'Extract and classify all numbers', 'status': 'completed', 'activeForm': 'Extracting and classifying all numbers'}, {'content': 'Perform internal consistency checks', 'status': 'completed', 'activeForm': 'Performing internal consistency checks'}, {'content': 'Verify derived computations', 'status': 'completed', 'activeForm': 'Verifying derived computations'}, {'content': 'Write audit report', 'status': 'completed', 'activeForm': 'Writing audit report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Read all main tex files and tables', 'status': 'completed', 'activeForm': 'Reading all main tex files and tables'}, {'content': 'Read all gen_fig*.py scripts for hardcoded data', 'status': 'completed', 'activeForm': 'Reading all gen_fig*.py scripts'}, {'content': 'Extract and classify all numbers', 'status': 'completed', 'activeForm': 'Extracting and classifying all numbers'}, {'content': 'Perform internal consistency checks', 'status': 'completed', 'activeForm': 'Performing internal consistency checks'}, {'content': 'Verify derived computations', 'status': 'completed', 'activeForm': 'Verifying derived computations'}, {'content': 'Write audit report', 'status': 'completed', 'activeForm': 'Writing audit report'}]"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-25T19:56:13.163298+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-25T19:56:13.163427+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-25T19:56:13.163545+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-25T19:56:13.163663+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "audit_paper_numbers",
  "type": "report",
  "description": "论文全文数字提取与内部一致性审计：覆盖10个tex文件、8个表格、9个figure脚本，识别1个HIGH级（fig1_dose_response与Table 3数据不一致）、2个MEDIUM级（20%/25.5%术语；MATH-500 α范围~8pp vs 实际6.2pp）、6个LOW级问题；验证39项派生计算（36正确，3有问题）。",
  "project": "recovery_aware_struct_prune",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/audit_paper_numbers.md",
  "tags": "['audit', 'paper', 'numbers', 'consistency']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "audit_paper_numbers",
    "type": "report",
    "description": "论文全文数字提取与内部一致性审计：覆盖10个tex文件、8个表格、9个figure脚本，识别1个HIGH级（fig1_dose_response与Table 3数据不一致）、2个MEDIUM级（20%/25.5%术语；MATH-500 α范围~8pp vs 实际6.2pp）、6个LOW级问题；验证39项派生计算（36正确，3有问题）。",
    "project": "recovery_aware_struct_prune",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/audit_paper_numbers.md",
    "tags": "['audit', 'paper', 'numbers', 'consistency']"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-25T19:56:13.163812+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260525_7984c8\", \"name\": \"audit_paper_numbers\", \"type\": \"report\", \"description\": \"论文全文数字提取与内部一致性审计：覆盖10个tex文件、8个表格、9个figure脚本，识别1个HIGH级（fig1_dose_response与Table 3数据不一致）、2个MEDIUM级（20%/25.5%术语；MATH-500 α范围~8pp vs 实际6.2pp）、6个LOW级问题；验证39项派生计算（36正确，3有问题）。\", \"path\": \"projects/recovery_aware_struct_prune/artifacts/_project/report/audit_paper_numbers.md\", \"url\": null, \"project\": \"recovery_aware_struct_prune\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-25T19:55:53.402073+00:00\", \"tags\": [\"audit\", \"paper\", \"numbers\", \"consistency\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_extract-paper-numbers_20260525T194435",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 86 · 2026-05-25T19:56:13.163983+00:00_

审计完成。报告已写入 `artifacts/audit_paper_numbers.md` 并注册（art_20260525_7984c8）。

## 关键发现

**HIGH（必须修复）**
1. **gen_fig1_dose_response.py 与 Table 3 数据不一致**：α=0.5 (64.52/65.05 vs 60.73/61.18，差约4 pp)、α=3.0 (64.06/64.59 vs 64.14/63.46，GRPO 差 1.13 pp)、α=4.0 SFT 微差。caption "|Δ|≤1.14 pp" 在两份数据上都恰好成立（因 α=2.0），所以读者表面看不出矛盾，但底层数据源不统一。

**MEDIUM**
2. **"20% MLP channel sparsity" 术语不准确**：200/784 = 25.5% MLP groups, 1.46B/7.62B = 19.2% total params, 无一为 20%。
3. **App:122 "α SFT 范围 ~8 pp"** vs 实际 27.8-21.6 = 6.2 pp。

**LOW**
4. tab_math500 caption 用 "4.62 pp"，正文用 "4.6 pp"（同一数字两种舍入）。
5. App:374 "$\varepsilon$=2 pp 约为 4× cross-seed σ" 推导不清（2/0.19=10.5×）。
6. App:308 RASP KL "<0.001" 实际有点超 0.001（max=0.001119）。
7. App:109 "rises from 0.354 to 0.308" 方向矛盾（实为下降）。
8. App:210 Standard 范围上界 60.20% vs TOST 反推 60.28%（差 0.08）。

**Orphan / 文件管理**
- `gen_fig2_reward_accuracy.py` 是 orphan，含与现行数据不一致的硬编码值。
- `gen_fig1_framework.py` 输出 `fig1_framework.pdf` 而论文引用 `fig1_method_framework.pdf`；脚本含 "+2.2pp advantage" 等论文文本不再使用的文案。

**整体保真度**: 验证 39 项派生计算，36 项正确（含 mean |Δ|=0.54 准确为 0.5425，4.4× 准确为 4.37，5.5× 准确为 5.50 等所有 headline 数字）。绝大多数表格-正文-脚本数据高度一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_extract-paper-numbers_20260525T194435"
}
```

</details>

---
