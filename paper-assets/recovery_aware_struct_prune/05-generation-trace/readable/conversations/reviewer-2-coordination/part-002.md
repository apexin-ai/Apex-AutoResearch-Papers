# Reviewer 2 coordination — Part 2 of 2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-2-coordination.md) · [Structured JSON](../../../sessions/6d/6d11d3171f6ee01cafc6.json)

## Round 15

### Tool call

_source line 633 · 2026-05-24T18:06:30.760715+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "lottery ticket hypothesis LLM pruning structured 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "lottery ticket hypothesis LLM pruning structured 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 634 · 2026-05-24T18:06:34.674958+00:00_

Web search results for query: ""When Reasoning Meets Compression" LLM pruning 2025 arxiv"

Links: [{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models","url":"https://arxiv.org/html/2504.02010"},{"title":"WHEN REASONING MEETS COMPRESSION: UNDER-","url":"https://arxiv.org/pdf/2504.02010"},{"title":"Reasoning Models Can be Accurately Pruned Via Chain-of ...","url":"https://arxiv.org/pdf/2509.12464"},{"title":"UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization, and Distillation","url":"https://arxiv.org/html/2602.09130v1"},{"title":"When Reasoning Meets Compression: Benchmarking Compressed Large Reasoning Models on Complex Reasoning Tasks","url":"https://arxiv.org/html/2504.02010v1"},{"title":"[2504.02010] When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models","url":"https://arxiv.org/abs/2504.02010"}]

I found the paper you're looking for! Here are the key details:

**"When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models"**

Compression methods, including quantization, distillation, and pruning, improve the computational efficiency of large reasoning models (LRMs). However, existing studies either fail to sufficiently compare all three compression methods on LRMs or lack in-depth interpretation analysis. In this paper, the authors investigate how the reasoning capabilities of LRMs are compromised during compression, through performance benchmarking and mechanistic interpretation.

The paper benchmarks quantized, distilled, and pruned DeepSeek-R1 models on four reasoning datasets (AIME 2024, FOLIO, Temporal Sequences, and MuSiQue). The authors adapt difference of means and attribution patc
…[truncated 302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4516
}
```

</details>

---


### Tool result

_source line 635 · 2026-05-24T18:06:40.597342+00:00_

Web search results for query: "lottery ticket hypothesis LLM pruning structured 2024 2025"

Links: [{"title":"Lottery Ticket Hypothesis in Deep Learning","url":"https://www.emergentmind.com/topics/lottery-ticket-hypothesis-lth"},{"title":"Neural Network Pruning: Lottery Ticket to SparseGPT | Meta Intelligence","url":"https://www.meta-intelligence.tech/en/insight-pruning"},{"title":"Lottery Ticket Hypothesis in Large Language Models: A Comprehensive Analysis of GPT-2 Weight Dynamics and Pruning Efficiency -","url":"https://www.authorea.com/doi/full/10.22541/au.176168540.05810555/v1"},{"title":"When BERT Plays The Lottery, All Tickets Are Winning","url":"https://thegradient.pub/when-bert-plays-the-lottery-all-tickets-are-winning/"},{"title":"Exploring the Lottery Ticket Hypothesis","url":"https://www.lesswrong.com/posts/Z7R6jFjce3J2Ryj44/exploring-the-lottery-ticket-hypothesis"},{"title":"A Generalized Lottery Ticket Hypothesis","url":"https://arxiv.org/pdf/2107.06825"},{"title":"The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks","url":"https://arxiv.org/pdf/1803.03635"},{"title":"When Layers Play the Lottery, all Tickets Win at Initialization","url":"https://arxiv.org/pdf/2301.10835"}]

Based on the search results, here's what I found about the lottery ticket hypothesis, LLM pruning, and structured approaches in 2024-2025:

## Recent Developments (2024-2025)

Structured pruning and data-efficient variants (early-bird, GraSP) accelerate mask discovery according to recent 2024 research. 

New algorithms (e.g., AWS) commit the sign of weights into the transferable structure, enabling one-shot, reusable tickets independent of explicit initialization as of April 2025.

## LLM-Specific Applications

Recent analysis of GPT-2 investigated weight dynamics and pruning efficiency across three model variants: randomly initialized, pre-trained, and fine-tuned, employing Iterative Magnitude Pruning (IMP) with layer-wise progressive sparsity, achieving up to 
…[truncated 780 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9836
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-24T18:07:41.615223+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-24T18:07:41.665936+00:00_

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
16	\usepackage{siunitx}
17	\usepackage{algorithm}
18	\usepackage[noend]{algpseudocode}
19	\usepackage{enumitem}
20	\usepackage{xcolor}
21	\usepackage{hyperref}
22	
23	\newcommand{\rasp}{\textsc{Rasp}}
24	
25	\title{How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs}
26	
27	\author{Anonymous}
28	
29	\begin{document}
30	\maketitle
31	
32	\begin{abstract}
33	\input{abstract}
34	\end{abstract}
35	
36	\input{introduction}
37	\input{related_work}
38	\input{method}
39	\input{experiments}
40	\input{conclusion}
41	
42	\section*{Limitations}
43	\input{limitations}
44	
45	\section*{Ethics Statement}
46	\input{ethics}
47	
48	\bibliography{references}
49	
50	\appendix
51	\input{appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-24T18:07:44.877287+00:00_

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
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-24T18:07:44.978047+00:00_

1	Fine-grained structured pruning of reasoning Large Language Models (LLMs), which removes MLP channel groups rather than entire layers, is typically followed by recovery training (SFT or Reinforcement Learning with Verifiable Rewards, RLVR) to restore reasoning capabilities.
2	RLVR is widely believed to be superior, yet we show this hierarchy reflects suboptimal pruning, not a fundamental property of RL\@.
3	When pruning preserves representational diversity, recovery method choice becomes irrelevant, a phenomenon we term \emph{reward-accuracy decoupling}: Group Relative Policy Optimization (GRPO) and SFT produce near-identical accuracy despite vastly different reward trajectories, a pattern that holds at moderate sparsity (20--25\%) across benchmarks.
4	We propose Recovery-Aware Structured Pruning (\rasp{}), which balances gradient importance with Centered Kernel Alignment (CKA)-based representational diversity via a coefficient $\alpha$.
5	On DeepSeek-R1-Distill-Qwen-7B at 20\% sparsity, a dose-response analysis reveals an inverted-U in recovery accuracy, peaking at $\alpha{=}2.0$ (66.11\% on GSM8K).
6	Under GRPO training, four pruning criteria produce a \emph{recovery capacity spectrum}: diversity-preserving pruning achieves active learning (peak reward 4.4$\times$ vs importance-only), while importance-dominated pruning collapses entirely.
7	The spectrum tracks preserved representational diversity rather than gradient importance, with preliminary evidence at 1.5B scale and, via SFT-based recovery, across Qwen2.5-family models (Qwen2.5-Math-7B).
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-24T18:07:44.978438+00:00_

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
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-24T18:07:45.079107+00:00_

1	\section{Introduction}
2	\label{sec:intro}
3	
4	Reasoning Large Language Models can be compressed through structured pruning, but the pruned model must recover its reasoning capabilities through fine-tuning.
5	The dominant assumption is that the recovery paradigm (SFT versus RLVR) determines recovery quality: \citet{selfhealing2025} demonstrate that RLVR restores pruned reasoning models to near-original accuracy, substantially outperforming SFT.
6	We show that this hierarchy is an artifact of suboptimal pruning.
7	When pruning preserves representational diversity, recovery method choice becomes irrelevant: at 20\% sparsity, mean $|\Delta(\text{GRPO}-\text{SFT})| {=} 0.54$\,pp across the four fine-grained criteria (max $0.61$\,pp); including dose-response variations, MBPP, and MATH-500, the maximum is $1.8$\,pp.
8	What matters is not \emph{how} you train after pruning, but \emph{which structures} you remove.
9	
10	This gap is surprising because RL and SFT impose fundamentally different demands on model representations: RL compresses incorrect paths while SFT expands correct ones~\citep{rlsqueezes2026}. Yet existing structured pruning methods for reasoning LLMs~\citep{graspprune2026,resp2025,llmpruner2023,bonsai2025} optimize for post-pruning quality without studying how the criterion shapes downstream RL recovery.
11	No prior work has compared multiple pruning criteria under RL or asked whether the ``RLVR $>$ SFT'' advantage persists across pruning strategies.
12	We note that \citet{selfhealing2025} evaluate unstructured magnitude pruning retaining 96.5\% of dense parameters; our findings concern fine-grained structural pruning where entire channel groups are removed, and the two settings may impose different demands on RL recovery.
13	
14	\begin{figure}[t]
15	\centering
16	\includegraphics[width=\columnwidth]{../figures/paper/fig1_dose_response.pdf}
17	\caption{Dose-response curve for the CKA diversity coefficient $\alpha$ at 20\% MLP channel sparsity on GSM8K ($N
…[truncated 2637 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 642 · 2026-05-24T18:08:06.024460+00:00_

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
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 643 · 2026-05-24T18:08:06.526714+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Structured pruning of LLMs.}
5	Width pruning methods (LLM-Pruner~\citep{llmpruner2023}, Bonsai~\citep{bonsai2025}, GRASPrune~\citep{graspprune2026}) remove attention heads or FFN channels while preserving dense computation.
6	Depth pruning~\citep{shortgpt2024,slicegpt2024,yang2024laco} removes entire layers but causes severe reasoning degradation~\citep{shrestha2026layerpruninglimits}; \citet{doingmore2026} revisit the trade-off under test-time scaling.
7	For reasoning models, RESP~\citep{resp2025}, RAC~\citep{rac2025}, and SSGR~\citep{ssgr2025} refine calibration data but retain gradient-based importance as the scoring criterion; \citet{llms2lrms2026} confirm width pruning is more robust than depth pruning for reasoning but do not study RLVR recovery.
8	A separate line uses functional structure to guide pruning: FANG~\citep{fang_2025} clusters FFN neurons by activation, FuncNet~\citep{funcnet_2025} decomposes LLMs via ICA, and MPruner~\citep{mpruner2024} applies inter-layer CKA~\citep{kornblith2019cka} for depth pruning in CNNs.
9	We differ in both granularity and objective: \emph{intra-layer} CKA between individual structures, optimizing for RL recovery capacity rather than immediate accuracy.
10	
11	\paragraph{Pruning-aware recovery.}
12	\citet{selfhealing2025} show that RLVR restores pruned reasoning models to near-original accuracy, outperforming SFT, but evaluate only importance-based unstructured pruning at low sparsity (96.5\% retention).
13	Under fine-grained structural pruning, our controlled experiments show that this advantage vanishes when pruning preserves diversity: it is a property of the pruning criterion, not of RL itself.
14	Other work optimizes complementary axes: post-pruning scaling ($P^2$~Law;~\citealp{p2law2025}), recovery data selection (PASER;~\citealp{paser2025}), joint pruning-tuning (PAT;~\citealp{pat2025}), post-hoc attention compensation (RestoreLCC;~\citealp{restorelcc_202
…[truncated 1506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 644 · 2026-05-24T18:08:06.527132+00:00_

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
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-24T18:08:07.029253+00:00_

1	% Limitations --- required by ACL/EMNLP
2	
3	\paragraph{Architecture and scale.}
4	Our primary results are on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1} with GQA ($G{=}7$).
5	Cross-model validation on Qwen2.5-Math-7B covers SFT recovery only ($N{=}200$); both models share the Qwen2.5 base architecture, so our cross-model evidence does not extend to different architecture families (e.g., LLaMA, Mistral).
6	Whether the spectrum generalizes across architecture families and scales (1B--70B) remains open.
7	
8	\paragraph{Diagnostic limitations.}
9	Reward-accuracy decoupling at 20--25\% sparsity means that recovery capacity, operationalized as peak reward, does not predict downstream accuracy improvements within our training horizon.
10	Recovery capacity captures the model's ability to sustain RL training without collapse, but practitioners seeking accuracy gains may require longer training, different reward formulations, or lower sparsity levels.
11	The per-layer capacity floor (40\% retention) was chosen heuristically; an ablation over $\tau \in \{0.3, 0.4, 0.5, 0.6\}$ (Appendix~\ref{sec:appendix_floor}) suggests moderate sensitivity, but a full search over continuous $\tau$ values was not performed.
12	
13	\paragraph{Inference efficiency.}
14	At 20\% sparsity, pruning reduces memory by ${\sim}$28\% and improves time-to-first-token, but inference throughput decreases by 19\% (72.0$\to$58.3 tok/s), likely because channel-group pruning creates irregular sparse patterns that current hardware cannot accelerate.
15	
16	\paragraph{Replication and scope.}
17	CKA-only, Standard, and Random are validated over 3 GRPO seeds; \rasp{} uses a single seed ($N{=}1$).
18	We evaluate on three benchmarks (GSM8K, MATH-500, MBPP) covering math reasoning and code generation; logical, commonsense, and multi-modal reasoning are not addressed.
19	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-24T18:08:07.029740+00:00_

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
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-24T18:08:07.130408+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:conclusion}
3	
4	Whether RLVR outperforms SFT for recovering pruned reasoning models depends on how the model was pruned.
5	Under diversity-preserving pruning at 20--25\% sparsity, the two paradigms produce near-identical accuracy (mean $|\Delta| {=} 0.54$\,pp; max $1.8$\,pp), yet the pruning criterion creates a 4.4$\times$ peak reward gap.
6	SFT warmup performs the bulk of accuracy recovery (${\sim}$60\,pp); GRPO exposes structural capacity differences but adds negligible accuracy, a pattern confirmed at 300 steps where CKA-only reward rises yet accuracy remains unchanged.
7	CKA-only preserves distinct pathways that sustain RL exploration (\S\ref{sec:extended_analysis}); the non-monotonic $\alpha$ dose-response argues against a layer-distribution confound.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-24T18:08:11.496451+00:00_

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
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-24T18:08:11.496906+00:00_

1	This work uses publicly available models (DeepSeek-R1-Distill-Qwen, Qwen2.5-Math) and established benchmarks (GSM8K, MATH-500, MBPP); no private data or human subjects are involved.
2	Structured pruning reduces model size and inference memory, which can lower the computational cost and energy consumption of deploying large language models.
3	Our research focuses on the technical analysis of pruning criteria and their interaction with reinforcement learning recovery; we do not foresee direct negative societal impacts from this work.
4	All models and datasets used in this work are publicly available under permissive licenses: DeepSeek-R1-Distill-Qwen (MIT), Qwen2.5-Math (Apache 2.0), GSM8K (MIT), MATH (MIT), and MBPP (CC-BY-4.0).
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 650 · 2026-05-24T18:08:11.497173+00:00_

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
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 651 · 2026-05-24T18:08:11.597959+00:00_

1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	\subsection{Experimental Setup}
6	\label{sec:exp_setup}
7	
8	\paragraph{Base model and evaluation.}
9	We evaluate on DeepSeek-R1-Distill-Qwen-7B~\citep{deepseek2025r1}, a 7B-parameter reasoning model built on the Qwen2.5 architecture~\citep{qwen2.5} with GQA~\citep{ainslie2023gqa} (architecture details in Section~\ref{sec:prelim}).
10	Our primary benchmark is GSM8K~\citep{cobbe2021gsm8k}, a set of 1{,}319 grade-school math problems requiring multi-step arithmetic reasoning.
11	We report exact-match accuracy: the final numerical answer is extracted from the model's generation and compared against the ground truth.
12	For rapid iteration during development, we use a 100-problem subset ($N{=}100$); final results use the full test set ($N{=}1{,}319$).
13	The original unpruned model achieves 90.83\% on GSM8K (greedy decoding).
14	
15	\paragraph{Pruning methods.}
16	We compare four pruning criteria at 20\% structured sparsity, all removing the same number of MLP channel groups (200 of 784 across 28 layers, ${\sim}$1.45B parameters) with identical per-layer capacity floors (${\ge}$40\% retention per layer):
17	\begin{enumerate}[nosep,leftmargin=*]
18	    \item \textbf{CKA-only}: structures ranked by functional overlap $F(h)$ alone (Eq.~\ref{eq:overlap}); the most redundant groups are removed regardless of gradient importance.
19	    \item \textbf{Random}: uniform random selection among eligible groups.
20	    \item \textbf{Standard}: Taylor-expansion importance $I(h)$ alone (Eq.~\ref{eq:importance}); the least important groups are removed, following LLM-Pruner~\citep{llmpruner2023}.
21	    \item \textbf{\rasp{}} ($\alpha{=}1.0$): the composite score $S(h) = I(h) \times (1 - F(h))^\alpha$ (Eq.~\ref{eq:score}), removing structures that are both low-importance and functionally redundant.
22	\end{enumerate}
23	
24	\paragraph{Recovery pipeline and hardware.}
25	All four methods undergo matched two-stage recovery.
26	Stag
…[truncated 11825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-24T18:13:19.734603+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: \"How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs\"\n**Venue**: EMNLP 2026 (ARR), Long Paper\n\n---\n\n## Strengths\n\n- **S1: 严格控制的实验设计。** 四种剪枝标准共享相同的 recovery pipeline（SFT warmup → GRPO）、相同的剪枝预算（20% MLP channel sparsity, 200/784 groups）、相同的 per-layer capacity floor（≥40%），这使得 pruning criterion 成为唯一自变量。这种控制水平在 LLM 剪枝文献中罕见。\n\n- **S2: Dose-response 分析方法论上出色。** α 系数的连续调控（0.5→4.0）产生可复现的 inverted-U 曲线（Figure 1, Table in Appendix D），为 α 的因果效应提供了比单点消融更强的证据。这超出了多数剪枝论文的方法论标准。\n\n- **S3: 统计严谨性突出。** TOST 等价检验（ε=2pp, 7/8 comparisons p<0.05, Appendix T）、Welch's t-test（CKA-only vs Standard, p=0.0009, Cohen's d=11.1）、multi-seed 验证（3 seeds for 3/4 methods）、95% CI 报告。这在实证 ML 论文中属于高标准。\n\n- **S4: Reward-accuracy decoupling 是有趣的反直觉发现。** 4.4× peak reward gap 对应 <1pp accuracy difference（Table 2, Figure 4）挑战了\"RLVR 优于 SFT\"的社区共识（来自 Ji et al., 2026 的 self-healing 结论），并提供了清晰的实验证据。\n\n- **S5: 充实的 Appendix（A-U, 8 页）。** 覆盖训练细节、算法伪代码、消融分析（sparsity cliff, per-layer floor, cross-scale, cross-model, MATH-500, MBPP, TOST），增强了可复现性。\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Critical\n\n**[Critical] W1: GRPO 训练时长严重不足，reward-accuracy decoupling 可能是训练欠拟合的 artifact。**\n- 具体位置：Section 4.1 (Recovery pipeline), Section 4.3, Section 4.5 (Extended training)\n- 问题：核心实验仅用 100 步 GRPO（扩展实验 300 步），而标准 GRPO 训练通常运行数千步（DeepSeek-R1 原文用数万步 RL）。SFT warmup 已恢复 ~60pp（从 post-prune 到 ~60-64%），留给 GRPO 的 headroom 约 ~27pp（相对于 dense 90.83%）。100 步 GRPO 仅贡献 <1pp，这可能仅仅说明训练不够长——而非 pruning criterion 真正消除了 recovery paradigm 差异。\n- 论文的 300 步扩展（Section 4.5, Figure 6）显示 Standard 仍然 collapsed，CKA-only 维持 5.5× reward gap，但仍未报告 accuracy 变化。如果 CKA-only 在 1000+ 步后 accuracy 显著超过 SFT-only，则 \"decoupling\" 的核心 claim 不成立。\n- 为什么影响接收：这是论文的中心论点。如果 decoupling 仅在训练不充分时成立，则 contribution 1 从\"发现\"降格为\"观察到短 GRPO 不改变 accuracy\"。\n- 建议：至少对 CKA-only 和 Standard 各跑一次 500-1000 步 GRPO 至 reward 饱和，报告 accuracy 变化。如果 accuracy 仍不变，decoupling claim 成立；否则需重新定性。\n\n**[Critical] W2: 单一架构族，\"Reasoning LLMs\" 的 claim scope 远超证据。**\n- 具体位置：Title, Abstract, Section 4.5 (Cross-scale and cross-model)\n- 问题：主实验仅 DeepSeek-R1-Distill-Qwen-7B（Qwen2.5 架构）；cross-model 验证的 Qwen2.5-Math-7B 是同一架构族且只有 SFT recovery（无 GRPO）。1.5B scale 验证仅为\"preliminary evidence\"且是 SFT-only（Table 13, Appendix N）。\n- Title 说 \"Reasoning LLMs\"（复数），Abstract 说 \"across benchmarks\"，但实际仅验证一个架构族。LLaMA、Mistral、Phi 等架构的 GQA 配置不同，MLP 结构不同，recovery spectrum 可能完全不同。\n- 为什么影响接收：EMNLP reviewers 会关注 claim scope 与 evidence 的匹配。当前证据支持\"How Pruning Criteria Shape Recovery in DeepSeek-R1-Distill-Qwen-7B\"而非标题的泛化声称。\n- 建议：(1) 在 Qwen2.5-Math-7B 上补充 GRPO recovery 验证 spectrum ordering；(2) 或大幅缩窄 claim scope——Title 改为明确指定模型/架构。\n\n**[Critical] W3: RASP 方法的贡献叙事自相矛盾。**\n- 具体位置：Section 3.3 (Eq. 5), Section 4.4 (Dose-response), Abstract\n- 问题：RASP 定义为 S(h) = I(h) × (1 − F(h))^α，旨在\"balance gradient importance with CKA-based diversity\"。但：\n  - α=1.0（名义上的\"平衡\"点）导致 collapse（peak reward 0.061, Figure 3）\n  - 最优 α=2.0 实质上是 CKA-dominant scoring（(1−F)^2 项主导，importance 被边缘化）\n  - CKA-only 本身已达 64.39%，RASP α=2.0 仅高 1.72pp（66.11%）\n- 这意味着\"平衡\"叙事不成立——最优策略是尽量最大化 diversity 权重，importance 的边际贡献微弱。论文应该更诚实地讨论：CKA-only 可能是 near-optimal 的简单 baseline，RASP 的 α 调优成本是否值得 1.72pp 的增益？\n- 建议：将 RASP 重新定位为\"dose-response 分析工具\"而非\"方法贡献\"，或提供更多 α 值（如 α=1.5, 2.5, 3.0, 3.5）的 fine-grained 搜索以证明 α=2.0 确实是 robust optimum。\n\n### Warning (Should-Fix)\n\n**[Warning] W4: Random baseline 的 max_completion_length 不一致（512 vs 1024）构成混淆变量。**\n- 具体位置：Section 4.1 最后一段, Table 3 (Appendix A)\n- 问题：Random 使用 TRL 默认 512 tokens，而 CKA-only、Standard、RASP 使用 1024 tokens。论文称这是\"conservative comparison\"，但 512 token 限制可能截断长 chain-of-thought 推理，人为压低 Random 的 GRPO performance。同样，RASP α=1.0 使用 1024 而其他 α 值使用 512（footnote, Section 4.4），使 inverted-U 成为\"conservative estimate\"——但这意味着 α=2.0 的 66.11% 可能在 1024 tokens 下更高，也可能更低。\n- 建议：统一 max_completion_length 为 1024 进行 fair comparison，至少对 Random 和 α=2.0 各补一个 1024-token 实验。\n\n**[Warning] W5: Title 聚焦 \"Post-RLVR Recovery\" 但数据显示 SFT 完成了几乎所有 accuracy recovery。**\n- 具体位置：Title, Section 4.3, Section 5\n- 问题：SFT warmup 恢复 ~60pp（从 post-prune ~1% 到 ~60-64%），GRPO 贡献 <1pp。Title 中的 \"Post-RLVR Recovery\" 暗示 RLVR 是 recovery 的关键阶段，但实验表明 RLVR 在 accuracy 维度上几乎无效。论文的实际发现更接近 \"pruning criteria shape SFT recovery and GRPO training dynamics\"。\n- 建议：考虑调整 title/framing，或在 Discussion 中更明确地阐述 SFT vs GRPO 各自的角色。\n\n**[Warning] W6: Discussion/Conclusion 过于单薄（仅 1 段约 7 行）。**\n- 具体位置：Section 5\n- 问题：对于一篇做了大量实验的 controlled study，Discussion 部分缺乏：(1) 为什么 diversity preservation enables RL trainability 的 mechanistic 解释；(2) 与 Mukherjee et al. (2025) 关于 RL 仅更新 5-30% 参数的联系；(3) 对 practitioner 的 actionable guidance 总结；(4) Future directions。\n- 建议：扩展至少到半页，加入 mechanistic discussion 和 practical implications。\n\n**[Warning] W7: 30% sparsity 全面 collapse 限制了实用性。**\n- 具体位置：Section 4.4, Appendix J\n- 问题：所有方法在 30% sparsity 下全部 collapse（Section 4.4 提及, Appendix J 确认）。论文的有效 operating window 仅为 15-25% sparsity，而 20% sparsity 仅节省 ~28% 内存、吞吐量反而下降 19%（Limitations section）。对 practitioner 而言，这个 efficiency-accuracy tradeoff 可能不够吸引人。\n- 建议：在 Limitations 中更坦诚地讨论实用性边界，或尝试 25% sparsity 下的 dose-response 验证。\n\n### Minor\n\n**[Minor] M1: RASP 仅用 1 个 GRPO seed 验证。**\n- 具体位置：Limitations (Replication and scope)\n- 问题：CKA-only、Standard、Random 各有 3 seeds，但 proposed method RASP 仅 1 seed。论文坦诚承认了这一点，但作为主要 proposed method，variance 估计缺失。\n\n**[Minor] M2: \"Cross-architecture\" overclaiming。**\n- 具体位置：Section 4.5, Abstract (\"across Qwen2.5-family models\")\n- 问题：Qwen2.5-Math-7B 是同一 Qwen2.5 架构族的变体，属于 cross-model 而非 cross-architecture。Abstract 的措辞准确（说了\"Qwen2.5-family\"），但 Introduction contribution list 可能给读者 cross-architecture 的错误印象。\n\n**[Minor] M3: Lottery Ticket Hypothesis 联系过于表面。**\n- 具体位置：Section 2 (Related Work), 最后一句\n- 问题：LTH 是关于 training from scratch 的 subnetwork，而本文是 recovery from pretrained model。一句话类比(\"poses the analogous question\") 没有深入讨论关键差异：LTH subnetworks 保持 initialization，而 pruned models 保持 pretrained weights + recovery training。\n\n**[Minor] M4: Abstract 中 \"a phenomenon we term reward-accuracy decoupling\" 的术语首次出现。**\n- 相较于论文后续的详细定义（Section 4.3），Abstract 中的引入稍显突兀。Decoupling 通常暗示两个变量原本应耦合，但论文未充分论证为什么 reward 和 accuracy 在先验上应该是耦合的。\n\n---\n\n## Questions for Authors\n\n- **Q1**: 如果将 GRPO 训练延长至 1000 步或 reward 完全饱和，CKA-only 的 accuracy 是否会显著超过 SFT-only？300 步实验（Section 4.5）仅报告了 reward gap 维持，未报告 accuracy 变化——这个遗漏是关键的。\n- **Q2**: RASP α=1.0 collapse 的根本原因是什么？既然 importance × diversity 理应是合理的 composite，为什么\"平衡\"点反而最差？这是否暗示 gradient importance scoring 本身对 RL recovery 有害？\n- **Q3**: CKA overlap 的计算使用 M=512 calibration samples（Section 3.2）。对不同 calibration data（如非数学领域的 text）的敏感性如何？\n- **Q4**: 为什么不在 Qwen2.5-Math-7B 上也跑 GRPO recovery？这只需额外几个小时的 GPU 时间，但能大幅增强 cross-model 证据。\n- **Q5**: Table 2 中 Random 的 peak reward (0.19) 高于 Standard (0.081)，但 Random 的 SFT accuracy 远低于 Standard（51.25% vs 59.29%）。为什么更差的 SFT 起点反而有更好的 GRPO reward？这是否进一步说明 reward 和 accuracy 是完全不同的指标？\n\n---\n\n## Missing References\n\n1. **\"When Reasoning Meets Compression\"** (Li et al., 2025, arXiv:2504.02010) — 在 DeepSeek-R1 模型上 benchmark 了包括剪枝在内的压缩方法对推理能力的影响，直接相关。\n2. **\"GPrune-LLM: Generalization-Aware Structured Pruning\"** (2026, arXiv:2603.13418) — 考虑泛化性的结构化剪枝，与本文关注 recovery capacity 的视角互补。\n3. **\"Can Pruning Improve Reasoning?\"** (2025, arXiv:2505.14582) — 探讨剪枝与推理能力的关系，应至少在 Related Work 中提及。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 (Findings)**\n\n**一句话总结**: 实验设计严谨、dose-response 分析出色的 controlled study，但 100 步 GRPO 训练不足以支撑 \"reward-accuracy decoupling\" 的核心 claim，单一架构族限制了泛化性，proposed RASP 方法的 \"balance\" 叙事与数据自相矛盾。\n\n## 官方维度打分（来自 ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 实验设计严格控制（S1），统计方法超过平均水平（S3），但 GRPO 训练时长不足（W1）严重威胁核心 claim，单一架构族限制了 main claims 的支撑范围（W2）|\n| Excitement | 3.0/5 | Pruning criterion 与 RL recovery 的交互是有意义的研究问题，dose-response 分析方法论有启发性（S2），但 findings 可能是训练不充分的 artifact（W1），实际影响受限于狭窄的 sparsity window（W7）|\n| Overall Assessment | 3.0/5 | Findings 接收水平。作为 controlled empirical study 有价值，但需要：(1) 更长的 GRPO 训练验证 decoupling 的 robustness；(2) 缩窄 claim scope 或补充 cross-architecture 证据；(3) 重新审视 RASP 的贡献定位 |\n\n**置信度**: 4/5 (Quite sure — 熟悉 LLM 剪枝和 RLVR 相关文献，仔细检查了实验细节和统计方法)\n\n---\n\n## Detailed Comments（逐 Section 评论）\n\n### Abstract\n- 约 191 words，符合 200-word 限制。\n- \"reward-accuracy decoupling\" 术语首次出现但缺乏前置动机——为什么 reviewer 应该期望 reward 和 accuracy 耦合？\n- \"holds at moderate sparsity (20–25%) across benchmarks\" 的 \"across benchmarks\" 表述偏强——MBPP 结果不显著（Appendix G），MATH-500 gap 缩窄。\n\n### Section 1 (Introduction)\n- Figure 1 dose-response 曲线放在首页有效吸引注意力。\n- Contribution list 仅 2 项：(1) reward-accuracy decoupling（empirical finding），(2) recovery capacity spectrum + RASP。对于 EMNLP long paper，contribution 数量略少。\n- 引用 Matsurani et al. (2026) 的 \"RL compresses incorrect paths while SFT expands correct ones\" 是 framing 的关键前提，但论文未充分解释为什么这种互补性应导致 accuracy 差异。\n\n### Section 2 (Related Work)\n- 覆盖面广：width pruning (LLM-Pruner, Bonsai, GRASPrune), depth pruning (ShortGPT, SliceGP, LaCo), reasoning-specific (RESP, RAC, SSGR, LLMs2LRMs), function-aware (FANG, FuncNet, MPruner), recovery (self-healing, P2Law, PASER, PAT), RL dynamics (RL squeezes, RL subnetworks)。\n- 但遗漏了 \"When Reasoning Meets Compression\" (2025) 和 \"GPrune-LLM\" (2026)。\n- LTH 联系仅一句话，过于表面。\n\n### Section 3 (Method)\n- 3.1 Preliminaries 清晰定义了 GQA pruning unit。\n- 3.2 Structural Analysis 的 importance (Eq. 1) 和 CKA overlap (Eq. 2-3) 计算标准清晰。\n- Intra-layer CKA（同层内不同 structure 间的 CKA）是与 MPruner (inter-layer CKA for depth pruning) 的关键差异，论文正确指出了这一点。\n- 3.3 四个 scoring criteria 定义明确，但 RASP (Eq. 5) 的函数形式 I(h)×(1−F(h))^α 的选择未经讨论——为什么是乘法而非加权和？为什么 diversity 用 (1−F)^α 而非 exp(−αF)？\n- 3.4 Two-Stage Recovery 描述清晰。SFT warmup 的设计意图（恢复 EOS generation + format compliance）说明合理。\n\n### Section 4 (Experiments)\n- **4.1 Setup**: 硬件（2×RTX PRO 6000, 94GB VRAM）、seed 处理、calibration 细节充分。但 Random 的 max_completion_length 差异是重要混淆变量。\n- **4.2 Recovery Capacity Spectrum**: Table 1 清晰展示四级 spectrum。Figure 3 的 training dynamics 可视化有效。但论文将此称为 \"spectrum\" 暗示连续性，实际只有 4 个离散点。\n- **4.3 Reward-Accuracy Decoupling**: 核心 section。TOST 检验方法论正确。但 100 步训练是否足够使 GRPO 发挥效果是根本性问题。Figure 4 的 scatter plot 有效展示了 y=x 附近的聚集。\n- **4.4 Additional Results**: Dose-response α 分析是论文最强的部分。15% vs 20% vs 25% 的 sparsity 比较有价值，显示 15% 时 GRPO 仍可放大 CKA-only 优势。\n- **4.5 Extended Analysis**: CKA heatmap (Figure 5) 和 gradient flow analysis 提供了 mechanistic evidence。Extended training (Figure 6) 仅到 300 步，应继续至 convergence。Cross-model 仅 SFT，不足以验证 spectrum 在 GRPO 下的泛化。\n\n### Section 5 (Discussion and Conclusion)\n- 仅 7 行，对于做了如此多实验的论文显得不成比例。\n- 未讨论：为什么 diversity preservation enables RL trainability（mechanistic explanation）、practical recommendations for practitioners、future work beyond \"remains open\"。\n\n### Limitations\n- 坦诚且全面（architecture scope, diagnostic limitations, inference efficiency, replication）。\n- 诚实承认了 throughput 下降 19% 和 RASP 单 seed 问题。\n- 但 \"30% sparsity collapse\" 仅在 Appendix 中一带而过，应在 Limitations 正文中更突出。\n\n### Ethics Statement\n- 简洁且充分。明确列出了所有 model/dataset 的 license。\n\n### Appendix\n- 内容充实（A-U），覆盖了主要的 reproducibility 需求。\n- Appendix U (Use of AI Assistants) 透明披露了 Claude 的使用——符合 ARR 要求。\n\n### 格式合规\n- ✅ `\\usepackage[review]{acl}` — 正确\n- ✅ 正文 8 页（Section 1-5 到 page 8）\n- ✅ Limitations section 存在且实质性（4 段）\n- ✅ Ethics Statement 存在\n- ✅ 匿名性：无作者信息、无 code repo URL、无可识别自引\n- ✅ Abstract ≤ 200 words\n- ✅ 引用格式正确（natbib/ACL style）\n- ✅ Figure 质量可接受（清晰、可读、颜色区分度尚可）",
  "reviewer_id": "2",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: \"How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in Reasoning LLMs\"\n**Venue**: EMNLP 2026 (ARR), Long Paper\n\n---\n\n## Strengths\n\n- **S1: 严格控制的实验设计。** 四种剪枝标准共享相同的 recovery pipeline（SFT warmup → GRPO）、相同的剪枝预算（20% MLP channel sparsity, 200/784 groups）、相同的 per-layer capacity floor（≥40%），这使得 pruning criterion 成为唯一自变量。这种控制水平在 LLM 剪枝文献中罕见。\n\n- **S2: Dose-response 分析方法论上出色。** α 系数的连续调控（0.5→4.0）产生可复现的 inverted-U 曲线（Figure 1, Table in Appendix D），为 α 的因果效应提供了比单点消融更强的证据。这超出了多数剪枝论文的方法论标准。\n\n- **S3: 统计严谨性突出。** TOST 等价检验（ε=2pp, 7/8 comparisons p<0.05, Appendix T）、Welch's t-test（CKA-only vs Standard, p=0.0009, Cohen's d=11.1）、multi-seed 验证（3 seeds for 3/4 methods）、95% CI 报告。这在实证 ML 论文中属于高标准。\n\n- **S4: Reward-accuracy decoupling 是有趣的反直觉发现。** 4.4× peak reward gap 对应 <1pp accuracy difference（Table 2, Figure 4）挑战了\"RLVR 优于 SFT\"的社区共识（来自 Ji et al., 2026 的 self-healing 结论），并提供了清晰的实验证据。\n\n- **S5: 充实的 Appendix（A-U, 8 页）。** 覆盖训练细节、算法伪代码、消融分析（sparsity cliff, per-layer floor, cross-scale, cross-model, MATH-500, MBPP, TOST），增强了可复现性。\n\n---\n\n## Weaknesses（按严重程度排序）\n\n### Critical\n\n**[Critical] W1: GRPO 训练时长严重不足，reward-accuracy decoupling 可能是训练欠拟合的 artifact。**\n- 具体位置：Section 4.1 (Recovery pipeline), Section 4.3, Section 4.5 (Extended training)\n- 问题：核心实验仅用 100 步 GRPO（扩展实验 300 步），而标准 GRPO 训练通常运行数千步（DeepSeek-R1 原文用数万步 RL）。SFT warmup 已恢复 ~60pp（从 post-prune 到 ~60-64%），留给 GRPO 的 headroom 约 ~27pp（相对于 dense 90.83%）。100 步 GRPO 仅贡献 <1pp，这可能仅仅说明训练不够长——而非 pruning criterion 真正消除了 recovery paradigm 差异。\n- 论文的 300 步扩展（Section 4.5, Figure 6）显示 Standard 仍然 collapsed，CKA-only 维持 5.5× reward gap，但仍未报告 accuracy 变化。如果 CKA-only 在 1000+ 步后 accuracy 显著超过 SFT-only，则 \"decoupling\" 的核心 claim 不成立。\n- 为什么影响接收：这是论文的中心论点。如果 decoupling 仅在训练不充分时成立，则 contribution 1 从\"发现\"降格为\"观察到短 GRPO 不改变 accuracy\"。\n- 建议：至少对 CKA-only 和 Standard 各跑一次 500-1000 步 GRPO 至 reward 饱和，报告 accuracy 变化。如果 accuracy 仍不变，decoupling claim 成立；否则需重新定性。\n\n**[Critical] W2: 单一架构族，\"Reasoning LLMs\" 的 claim scope 远超证据。**\n- 具体位置：Title, Abstract, Section 4.5 (Cross-scale and cross-model)\n- 问题：主实验仅 DeepSeek-R1-Distill-Qwen-7B（Qwen2.5 架构）；cross-model 验证的 Qwen2.5-Math-7B 是同一架构族且只有 SFT recovery（无 GRPO）。1.5B scale 验证仅为\"preliminary evidence\"且是 SFT-only（Table 13, Appendix N）。\n- Title 说 \"Reasoning LLMs\"（复数），Abstract 说 \"across benchmarks\"，但实际仅验证一个架构族。LLaMA、Mistral、Phi 等架构的 GQA 配置不同，MLP 结构不同，recovery spectrum 可能完全不同。\n- 为什么影响接收：EMNLP reviewers 会关注 claim scope 与 evidence 的匹配。当前证据支持\"How Pruning Criteria Shape Recovery in DeepSeek-R1-Distill-Qwen-7B\"而非标题的泛化声称。\n- 建议：(1) 在 Qwen2.5-Math-7B 上补充 GRPO recovery 验证 spectrum ordering；(2) 或大幅缩窄 claim scope——Title 改为明确指定模型/架构。\n\n**[Critical] W3: RASP 方法的贡献叙事自相矛盾。**\n- 具体位置：Section 3.3 (Eq. 5), Section 4.4 (Dose-response), Abstract\n- 问题：RASP 定义为 S(h) = I(h) × (1 − F(h))^α，旨在\"balance gradient importance with CKA-based diversity\"。但：\n  - α=1.0（名义上的\"平衡\"点）导致 collapse（peak reward 0.061, Figure 3）\n  - 最优 α=2.0 实质上是 CKA-dominant scoring（(1−F)^2 项主导，importance 被边缘化）\n  - CKA-only 本身已达 64.39%，RASP α=2.0 仅高 1.72pp（66.11%）\n- 这意味着\"平衡\"叙事不成立——最优策略是尽量最大化 diversity 权重，importance 的边际贡献微弱。论文应该更诚实地讨论：CKA-only 可能是 near-optimal 的简单 baseline，RASP 的 α 调优成本是否值得 1.72pp 的增益？\n- 建议：将 RASP 重新定位为\"dose-response 分析工具\"而非\"方法贡献\"，或提供更多 α 值（如 α=1.5, 2.5, 3.0, 3.5）的 fine-grained 搜索以证明 α=2.0 确实是 robust optimum。\n\n### Warning (Should-Fix)\n\n**[Warning] W4: Random baseline 的 max_completion_length 不一致（512 vs 1024）构成混淆变量。**\n- 具体位置：Section 4.1 最后一段, Table 3 (Appendix A)\n- 问题：Random 使用 TRL 默认 512 tokens，而 CKA-only、Standard、RASP 使用 1024 tokens。论文称这是\"conservative comparison\"，但 512 token 限制可能截断长 chain-of-thought 推理，人为压低 Random 的 GRPO performance。同样，RASP α=1.0 使用 1024 而其他 α 值使用 512（footnote, Section 4.4），使 inverted-U 成为\"conservative estimate\"——但这意味着 α=2.0 的 66.11% 可能在 1024 tokens 下更高，也可能更低。\n- 建议：统一 max_completion_length 为 1024 进行 fair comparison，至少对 Random 和 α=2.0 各补一个 1024-token 实验。\n\n**[Warning] W5: Title 聚焦 \"Post-RLVR Recovery\" 但数据显示 SFT 完成了几乎所有 accuracy recovery。**\n- 具体位置：Title, Section 4.3, Section 5\n- 问题：SFT warmup 恢复 ~60pp（从 post-prune ~1% 到 ~60-64%），GRPO 贡献 <1pp。Title 中的 \"Post-RLVR Recovery\" 暗示 RLVR 是 recovery 的关键阶段，但实验表明 RLVR 在 accuracy 维度上几乎无效。论文的实际发现更接近 \"pruning criteria shape SFT recovery and GRPO training dynamics\"。\n- 建议：考虑调整 title/framing，或在 Discussion 中更明确地阐述 SFT vs GRPO 各自的角色。\n\n**[Warning] W6: Discussion/Conclusion 过于单薄（仅 1 段约 7 行）。**\n- 具体位置：Section 5\n- 问题：对于一篇做了大量实验的 controlled study，Discussion 部分缺乏：(1) 为什么 diversity preservation enables RL trainability 的 mechanistic 解释；(2) 与 Mukherjee et al. (2025) 关于 RL 仅更新 5-30% 参数的联系；(3) 对 practitioner 的 actionable guidance 总结；(4) Future directions。\n- 建议：扩展至少到半页，加入 mechanistic discussion 和 practical implications。\n\n**[Warning] W7: 30% sparsity 全面 collapse 限制了实用性。**\n- 具体位置：Section 4.4, Appendix J\n- 问题：所有方法在 30% sparsity 下全部 collapse（Section 4.4 提及, Appendix J 确认）。论文的有效 operating window 仅为 15-25% sparsity，而 20% sparsity 仅节省 ~28% 内存、吞吐量反而下降 19%（Limitations section）。对 practitioner 而言，这个 efficiency-accuracy tradeoff 可能不够吸引人。\n- 建议：在 Limitations 中更坦诚地讨论实用性边界，或尝试 25% sparsity 下的 dose-response 验证。\n\n### Minor\n\n**[Minor] M1: RASP 仅用 1 个 GRPO seed 验证。**\n- 具体位置：Limitations (Replication and scope)\n- 问题：CKA-only、Standard、Random 各有 3 seeds，但 proposed method RASP 仅 1 seed。论文坦诚承认了这一点，但作为主要 proposed method，variance 估计缺失。\n\n**[Minor] M2: \"Cross-architecture\" overclaiming。**\n- 具体位置：Section 4.5, Abstract (\"across Qwen2.5-family models\")\n- 问题：Qwen2.5-Math-7B 是同一 Qwen2.5 架构族的变体，属于 cross-model 而非 cross-architecture。Abstract 的措辞准确（说了\"Qwen2.5-family\"），但 Introduction contribution list 可能给读者 cross-architecture 的错误印象。\n\n**[Minor] M3: Lottery Ticket Hypothesis 联系过于表面。**\n- 具体位置：Section 2 (Related Work), 最后一句\n- 问题：LTH 是关于 training from scratch 的 subnetwork，而本文是 recovery from pretrained model。一句话类比(\"poses the analogous question\") 没有深入讨论关键差异：LTH subnetworks 保持 initialization，而 pruned models 保持 pretrained weights + recovery training。\n\n**[Minor] M4: Abstract 中 \"a phenomenon we term reward-accuracy decoupling\" 的术语首次出现。**\n- 相较于论文后续的详细定义（Section 4.3），Abstract 中的引入稍显突兀。Decoupling 通常暗示两个变量原本应耦合，但论文未充分论证为什么 reward 和 accuracy 在先验上应该是耦合的。\n\n---\n\n## Questions for Authors\n\n- **Q1**: 如果将 GRPO 训练延长至 1000 步或 reward 完全饱和，CKA-only 的 accuracy 是否会显著超过 SFT-only？300 步实验（Section 4.5）仅报告了 reward gap 维持，未报告 accuracy 变化——这个遗漏是关键的。\n- **Q2**: RASP α=1.0 collapse 的根本原因是什么？既然 importance × diversity 理应是合理的 composite，为什么\"平衡\"点反而最差？这是否暗示 gradient importance scoring 本身对 RL recovery 有害？\n- **Q3**: CKA overlap 的计算使用 M=512 calibration samples（Section 3.2）。对不同 calibration data（如非数学领域的 text）的敏感性如何？\n- **Q4**: 为什么不在 Qwen2.5-Math-7B 上也跑 GRPO recovery？这只需额外几个小时的 GPU 时间，但能大幅增强 cross-model 证据。\n- **Q5**: Table 2 中 Random 的 peak reward (0.19) 高于 Standard (0.081)，但 Random 的 SFT accuracy 远低于 Standard（51.25% vs 59.29%）。为什么更差的 SFT 起点反而有更好的 GRPO reward？这是否进一步说明 reward 和 accuracy 是完全不同的指标？\n\n---\n\n## Missing References\n\n1. **\"When Reasoning Meets Compression\"** (Li et al., 2025, arXiv:2504.02010) — 在 DeepSeek-R1 模型上 benchmark 了包括剪枝在内的压缩方法对推理能力的影响，直接相关。\n2. **\"GPrune-LLM: Generalization-Aware Structured Pruning\"** (2026, arXiv:2603.13418) — 考虑泛化性的结构化剪枝，与本文关注 recovery capacity 的视角互补。\n3. **\"Can Pruning Improve Reasoning?\"** (2025, arXiv:2505.14582) — 探讨剪枝与推理能力的关系，应至少在 Related Work 中提及。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 (Findings)**\n\n**一句话总结**: 实验设计严谨、dose-response 分析出色的 controlled study，但 100 步 GRPO 训练不足以支撑 \"reward-accuracy decoupling\" 的核心 claim，单一架构族限制了泛化性，proposed RASP 方法的 \"balance\" 叙事与数据自相矛盾。\n\n## 官方维度打分（来自 ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.0/5 | 实验设计严格控制（S1），统计方法超过平均水平（S3），但 GRPO 训练时长不足（W1）严重威胁核心 claim，单一架构族限制了 main claims 的支撑范围（W2）|\n| Excitement | 3.0/5 | Pruning criterion 与 RL recovery 的交互是有意义的研究问题，dose-response 分析方法论有启发性（S2），但 findings 可能是训练不充分的 artifact（W1），实际影响受限于狭窄的 sparsity window（W7）|\n| Overall Assessment | 3.0/5 | Findings 接收水平。作为 controlled empirical study 有价值，但需要：(1) 更长的 GRPO 训练验证 decoupling 的 robustness；(2) 缩窄 claim scope 或补充 cross-architecture 证据；(3) 重新审视 RASP 的贡献定位 |\n\n**置信度**: 4/5 (Quite sure — 熟悉 LLM 剪枝和 RLVR 相关文献，仔细检查了实验细节和统计方法)\n\n---\n\n## Detailed Comments（逐 Section 评论）\n\n### Abstract\n- 约 191 words，符合 200-word 限制。\n- \"reward-accuracy decoupling\" 术语首次出现但缺乏前置动机——为什么 reviewer 应该期望 reward 和 accuracy 耦合？\n- \"holds at moderate sparsity (20–25%) across benchmarks\" 的 \"across benchmarks\" 表述偏强——MBPP 结果不显著（Appendix G），MATH-500 gap 缩窄。\n\n### Section 1 (Introduction)\n- Figure 1 dose-response 曲线放在首页有效吸引注意力。\n- Contribution list 仅 2 项：(1) reward-accuracy decoupling（empirical finding），(2) recovery capacity spectrum + RASP。对于 EMNLP long paper，contribution 数量略少。\n- 引用 Matsurani et al. (2026) 的 \"RL compresses incorrect paths while SFT expands correct ones\" 是 framing 的关键前提，但论文未充分解释为什么这种互补性应导致 accuracy 差异。\n\n### Section 2 (Related Work)\n- 覆盖面广：width pruning (LLM-Pruner, Bonsai, GRASPrune), depth pruning (ShortGPT, SliceGP, LaCo), reasoning-specific (RESP, RAC, SSGR, LLMs2LRMs), function-aware (FANG, FuncNet, MPruner), recovery (self-healing, P2Law, PASER, PAT), RL dynamics (RL squeezes, RL subnetworks)。\n- 但遗漏了 \"When Reasoning Meets Compression\" (2025) 和 \"GPrune-LLM\" (2026)。\n- LTH 联系仅一句话，过于表面。\n\n### Section 3 (Method)\n- 3.1 Preliminaries 清晰定义了 GQA pruning unit。\n- 3.2 Structural Analysis 的 importance (Eq. 1) 和 CKA overlap (Eq. 2-3) 计算标准清晰。\n- Intra-layer CKA（同层内不同 structure 间的 CKA）是与 MPruner (inter-layer CKA for depth pruning) 的关键差异，论文正确指出了这一点。\n- 3.3 四个 scoring criteria 定义明确，但 RASP (Eq. 5) 的函数形式 I(h)×(1−F(h))^α 的选择未经讨论——为什么是乘法而非加权和？为什么 diversity 用 (1−F)^α 而非 exp(−αF)？\n- 3.4 Two-Stage Recovery 描述清晰。SFT warmup 的设计意图（恢复 EOS generation + format compliance）说明合理。\n\n### Section 4 (Experiments)\n- **4.1 Setup**: 硬件（2×RTX PRO 6000, 94GB VRAM）、seed 处理、calibration 细节充分。但 Random 的 max_completion_length 差异是重要混淆变量。\n- **4.2 Recovery Capacity Spectrum**: Table 1 清晰展示四级 spectrum。Figure 3 的 training dynamics 可视化有效。但论文将此称为 \"spectrum\" 暗示连续性，实际只有 4 个离散点。\n- **4.3 Reward-Accuracy Decoupling**: 核心 section。TOST 检验方法论正确。但 100 步训练是否足够使 GRPO 发挥效果是根本性问题。Figure 4 的 scatter plot 有效展示了 y=x 附近的聚集。\n- **4.4 Additional Results**: Dose-response α 分析是论文最强的部分。15% vs 20% vs 25% 的 sparsity 比较有价值，显示 15% 时 GRPO 仍可放大 CKA-only 优势。\n- **4.5 Extended Analysis**: CKA heatmap (Figure 5) 和 gradient flow analysis 提供了 mechanistic evidence。Extended training (Figure 6) 仅到 300 步，应继续至 convergence。Cross-model 仅 SFT，不足以验证 spectrum 在 GRPO 下的泛化。\n\n### Section 5 (Discussion and Conclusion)\n- 仅 7 行，对于做了如此多实验的论文显得不成比例。\n- 未讨论：为什么 diversity preservation enables RL trainability（mechanistic explanation）、practical recommendations for practitioners、future work beyond \"remains open\"。\n\n### Limitations\n- 坦诚且全面（architecture scope, diagnostic limitations, inference efficiency, replication）。\n- 诚实承认了 throughput 下降 19% 和 RASP 单 seed 问题。\n- 但 \"30% sparsity collapse\" 仅在 Appendix 中一带而过，应在 Limitations 正文中更突出。\n\n### Ethics Statement\n- 简洁且充分。明确列出了所有 model/dataset 的 license。\n\n### Appendix\n- 内容充实（A-U），覆盖了主要的 reproducibility 需求。\n- Appendix U (Use of AI Assistants) 透明披露了 Claude 的使用——符合 ARR 要求。\n\n### 格式合规\n- ✅ `\\usepackage[review]{acl}` — 正确\n- ✅ 正文 8 页（Section 1-5 到 page 8）\n- ✅ Limitations section 存在且实质性（4 段）\n- ✅ Ethics Statement 存在\n- ✅ 匿名性：无作者信息、无 code repo URL、无可识别自引\n- ✅ Abstract ≤ 200 words\n- ✅ 引用格式正确（natbib/ACL style）\n- ✅ Figure 质量可接受（清晰、可读、颜色区分度尚可）",
    "reviewer_id": "2",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 653 · 2026-05-24T18:13:23.401514+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3666
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-24T18:13:27.283585+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 655 · 2026-05-24T18:13:27.434585+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 656 · 2026-05-24T18:13:31.080116+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_8/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_8/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-24T18:13:31.180914+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_8/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 658 · 2026-05-24T18:13:43.025594+00:00_

审稿完成，已提交给 Review Director。

核心判断：**Overall 3.0 (Findings)**。实验控制和统计方法出色，但三个 critical 问题制约接收：(1) 100 步 GRPO 训练不足以支撑 reward-accuracy decoupling 的核心 claim——可能仅是训练不充分的 artifact；(2) 仅测试 Qwen2.5 一个架构族，"Reasoning LLMs" 的 title scope 远超证据；(3) RASP 最优 α=2.0 实质是 CKA-dominant，"balance" 叙事与数据矛盾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2"
}
```

</details>

---


## Round 16

## Round 16

4 recorded events


### User

_source line 659 · 2026-05-24T18:14:58.864541+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 1 的完整审稿意见

请逐条回应 Reviewer 1 的每个 Weakness 和主要观点：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

特别关注你和 Reviewer 1 在以下方面的异同：
1. CKA 循环使用问题的严重程度（R1 的 W3）
2. RASP 函数形式的理论依据（R1 的 W4）
3. SFT ceiling effect 假说（R1 的 W6）
4. TOST ε=2pp margin 的合理性（R1 的 W7）

---

以下是 Reviewer 1 的完整审稿原文：

## Strengths

- **S1: 重要且新颖的研究问题。** 现有结构化剪枝文献几乎未研究剪枝准则如何影响下游 RLVR 恢复效果。

- **S2: 严格的控制实验设计。** 固定模型、固定剪枝率、固定恢复流水线，仅变化剪枝准则。Algorithm 1 提供了完整伪代码。

- **S3: Reward-accuracy decoupling 是一个有意义的发现。** Table 2 和 Figure 4 清晰展示了 high reward ≠ high accuracy gain。

- **S4: 统计分析比同领域多数工作更严谨。** Welch's t-test、Cohen's d、95% CI、TOST。CKA-only vs Standard 的 Cohen's d = 11.5。

- **S5: 丰富的消融实验。** 21 个附录覆盖广泛。

- **S6: Recovery capacity spectrum 概念。** 将四种准则映射到连续谱并通过四个诊断指标操作化定义。

## Weaknesses

### Critical

**[Critical] W1: RASP（核心方法）仅使用单 seed 验证，dose-response 曲线不可靠。**
- RASP 及 dose-response 分析（α ∈ {0.5, 1.0, 2.0, 3.0, 4.0}）均为 N=1。α=2.0 时精度最高 (66.11%)，但相邻 α=3.0 仅 61.46%——差 4.65pp。inverted-U 形状本身可能是单次采样的伪影。

**[Critical] W2: Random baseline 使用不同的 max_completion_length（512 vs 1024），比较不公平。**
- Random 使用 TRL 默认 512-token，其他方法 1024。bias 方向恰好支持论文叙事。

### Warning

**[Warning] W3: CKA 的双重角色（评分准则 + 分析工具）存在循环论证风险。**
- CKA 同时用于剪枝时计算 functional overlap 和事后分析 layer-wise similarity。当 Section 4.5 用 CKA 发现 "CKA-only diverges most" 时，部分是因为 CKA-only 的剪枝准则本身基于 CKA。

**[Warning] W4: RASP 评分函数 (Eq. 5) 缺乏理论推导，函数形式选择武断。**
- 乘法形式没有理论推导。为什么不是 I(h) + λ(1−F(h))？为什么是 (1−F(h))^α 而非 exp(−αF(h))？

**[Warning] W5: 模型和 benchmark 范围窄，核心 claims 的泛化性存疑。**
- 主实验仅用一个 7B 模型 + GSM8K。Qwen2.5-Math-7B 没有 GRPO 验证，MATH-500 和 MBPP 差异不显著。

**[Warning] W6: SFT 阶段可能引入 ceiling effect，模糊 GRPO 的增量贡献。**
- SFT 已恢复到 59-64%，GRPO 增量 <1pp。可能是 GRPO 仅 100 步不够，而非 "decoupling"。

**[Warning] W7: TOST 等价性检验的 ε=2pp margin 选择缺乏先验依据。**
- ε=2pp 非预注册，ε=1pp 功效不足，ε=3pp 全通过。ε=2pp "刚好合适" 有 post-hoc selection 之嫌。

### Minor
**[Minor] M1: Recovery capacity 概念先用后定义。**
**[Minor] M2: Figure 2 信息密度过高。**
**[Minor] M3: "Reward-accuracy decoupling" 术语可能引起误解。**
**[Minor] M4: Calibration data M=512 选择未说明理由。**
**[Minor] M5: 未明确承诺代码/checkpoint 发布。**

## Missing References
- 无明显缺失，可考虑增加 Wanda (Sun et al., 2024) 讨论。

## Overall Assessment
**评分: 3.5 (Borderline Conference)**，置信度 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-24T18:17:10.745551+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条评议\n\n---\n\n### Critical Weaknesses\n\n**[AGREE] R1-W1: RASP 单 seed + dose-response 不可靠**\n同意 RASP 及 dose-response 分析为 N=1 是重要缺陷。α=2.0 (66.11%) 与 α=3.0 (61.46%) 之间 4.65pp 的差距在单 seed 下确实可能是随机噪声——作为对照，CKA-only 的 3-seed std 为 0.19pp（Section 4.1），若 RASP 的方差类似，4.65pp 差距是显著的；但若 RASP 因包含 importance 项而方差更大，inverted-U 形状可能不成立。\n\n不过，我认为此问题的严重程度更接近 **Warning 而非 Critical**。原因：论文的核心 claim 是 reward-accuracy decoupling 和 recovery capacity spectrum，这两者主要依赖 CKA-only vs Standard vs Random 的多 seed 比较（3 seeds each, Welch's t-test p=0.0009）。RASP 的 dose-response 是 supporting evidence 而非核心 claim 的唯一支撑。如果去掉 RASP，spectrum 的 CKA-only ≫ Random ≫ Standard ordering 仍然成立。\n\n**[AGREE] R1-W2: Random baseline max_completion_length 不公平**\n完全同意。我在自己的审稿中也将此列为 W4 (Warning)。R1 将其升为 Critical，我理解其逻辑——bias 方向恰好支持论文叙事（压低 Random 的 GRPO reward，使 CKA-only 的 spectrum 优势更突出）。\n\n但我仍倾向于 **Warning** 级别：Random 不是论文的 proposed method，也不是 spectrum 的关键对比对象。核心比较是 CKA-only vs Standard（二者均用 1024 tokens），该比较是公平的。Random 的不公平主要影响 \"Random 在 spectrum 中的位置\" 这个次要 claim。\n\n---\n\n### Warning Weaknesses\n\n**[REBUT] R1-W3: CKA 双重角色的循环论证**\n这是一个有洞察力的观察，但我认为循环论证的指控**不完全成立**，需要区分两个不同的 CKA 计算：\n\n1. **剪枝阶段**（Section 3.2, Eq. 3）：计算 **intra-layer** CKA——同一层内不同 MLP channel group 之间的 pairwise CKA similarity，衡量结构间的功能重叠度。CKA-only 移除与其他结构最相似（最冗余）的 group。\n2. **分析阶段**（Section 4.5, Figure 5）：计算 **layer-wise** CKA——dense model 某层输出与 pruned model 同层输出之间的 CKA，衡量剪枝对层级表示的扰动程度。\n\n这两个 CKA 的对象不同（structure-to-structure vs. layer-to-layer）、目标不同（identify redundancy vs. measure perturbation）。Section 4.5 发现 \"CKA-only diverges most from dense (μ=0.62)\" 不是因为 CKA 被自我验证，而是因为一个可解释的因果链：移除冗余结构 → 消除重复表示 → 每层的总体表示变化更大 → layer-wise CKA 下降。这个因果链即使不用 CKA 衡量也应成立——例如用 L2 距离或 procrustes 距离衡量 dense-pruned 表示差异，CKA-only 也应偏离最大。\n\n不过我承认 R1 的 concern 有一定道理：**读者可能产生 metric 自我验证的印象**。建议作者加一句说明两个 CKA 计算的区别，或补充一个非 CKA 的 representational similarity 指标（如 procrustes distance）作为 robustness check。\n\n**严重程度评估**：Minor，非 Warning。核心 experimental findings（spectrum ordering, decoupling）不依赖 Section 4.5 的 layer-wise CKA 分析——即使删除 Figure 5 及相关讨论，Table 1、Table 2、Figure 3、Figure 4 的结论不受影响。\n\n**[AGREE] R1-W4: RASP 函数形式缺乏理论推导**\n同意。我在 Section 3 的 detailed comments 中也提出了相同问题。乘法形式 I(h) × (1−F(h))^α 意味着 importance 为 0 时无论 diversity 多高分数都为 0（被过滤），但这恰好可能是导致 α=1.0 collapse 的原因——很多低 importance 但高 diversity 的结构被不当移除。加法形式 βI(h) + (1−β)(1−F(h)) 会保留这些结构。\n\n这个函数形式的选择直接影响了 \"α=1.0 collapse\" 这个关键实验结果（Section 4.2），因此不仅是理论缺陷，还可能导致对 importance scoring 有害性的错误结论。如果加法形式下 α=1.0 不 collapse，则 \"importance 对 RL recovery 有害\" 的隐含论点不成立。\n\n**严重程度评估**：同意 R1 的 Warning 级别。与我的 W3 (Critical) 中 \"RASP 贡献叙事自相矛盾\" 呼应——函数形式的武断选择加剧了这个问题。\n\n**[AGREE] R1-W5: 模型和 benchmark 范围窄**\n完全同意，与我的 W2 (Critical) 一致。R1 列为 Warning，我给了 Critical。核心分歧：我认为 title 中 \"Reasoning LLMs\" 的泛化声称使此问题上升为 Critical——如果论文明确将 scope 限定为 \"DeepSeek-R1-Distill-Qwen-7B\"，则 Warning 足矣。\n\n**[AGREE] R1-W6: SFT ceiling effect 假说**\n**强烈同意，且认为 R1 对此问题的严重程度评估偏低。**\n\n这与我的 W1 (Critical) 一致。R1 将其列为 Warning，但我认为是本文**最关键的问题**。原因：\n\n1. **数据支持 ceiling 解释**：SFT 恢复 ~60pp（从 post-prune ~1% 到 59-64%），GRPO 仅贡献 <1pp。Dense model 90.83%，即 GRPO 有 ~27pp 的理论 headroom。100 步 GRPO 仅利用了 <4% 的 headroom（<1pp / 27pp），这更可能是训练不充分而非 intrinsic decoupling。\n\n2. **300 步扩展未解决问题**：Section 4.5 的 300 步实验（Figure 6）仅报告了 reward gap 维持（5.5×），但**关键性地缺失了 accuracy 数据**。如果 CKA-only 在 300 步时 accuracy 有所提升（哪怕 1-2pp），则 \"decoupling\" 的 claim 需要 qualify。论文选择性地只报告 reward 而不报告 accuracy，这是一个值得追问的遗漏。\n\n3. **15% sparsity 的反例**：Section 4.3 自己报告了 15% sparsity 下 GRPO 放大了 CKA-only 优势（SFT gap 5.69pp → GRPO gap 7.20pp）。这恰恰说明当 SFT ceiling 不那么低时（15% 比 20% 留给 GRPO 的 headroom 更大），GRPO 是有增量贡献的——**论文自身的数据 undermines decoupling 的普遍性**。\n\n**建议将此问题升至 Critical**。\n\n**[AGREE] R1-W7: TOST ε=2pp margin post-hoc selection**\n部分同意。R1 的 concern 合理——ε=2pp 未预注册，且 paper 自己报告了 ε=1pp 功效不足（Appendix T：\"ε=1pp margin lacks statistical power with binary outcomes at N=1,319\"），ε=3pp 全通过。ε=2pp 时 7/8 通过，确实有\"刚好合适\"的嫌疑。\n\n但我对此的严重程度评估略低于 R1：\n1. **论文的透明度是加分项**——诚实报告了 ε=1 和 ε=3 的结果，没有隐藏不利数据。\n2. **从实际意义看**，2pp 在 GSM8K 60-66% 区间内是合理的 practical significance threshold。EMNLP 社区通常接受 ~1-2pp 的差异为 \"negligible\"。\n3. **关键证据不仅依赖 TOST**——Table 2 的原始 |Δ| 值（CKA-only +0.48, Standard +0.55, Random -0.53, RASP -0.61）已经直观地展示了 <1pp 的差距。TOST 只是形式化了这一观察。\n\n**严重程度评估**：Minor-to-Warning。ε=2pp 的选择确实应该在论文中 justify（例如引用 GSM8K 相关文献中什么差异被认为是 meaningful），但不影响核心结论的可信度。\n\n---\n\n### Minor Issues\n\n**[AGREE] R1-M1: Recovery capacity 概念先用后定义。**\n同意，但 minor 中的 minor。学术论文中 terminology 先用后定义很常见，尤其在 abstract/intro 中。\n\n**[AGREE] R1-M2: Figure 2 信息密度过高。**\n同意。Figure 2 试图在一个图中展示 structural analysis + scoring criteria + recovery pipeline + recovery spectrum，对不熟悉此工作的读者有认知负担。但 page budget 紧张（8 pages），拆分可能不现实。\n\n**[AGREE] R1-M3: \"Reward-accuracy decoupling\" 术语可能误导。**\n同意，与我的 M4 呼应。\"Decoupling\" 暗示两者原本应耦合，但论文未充分建立这一先验预期。\n\n**[AGREE] R1-M4: Calibration data M=512 未说明理由。**\n同意。Section 3.2 说 M=512 randomly sampled examples，但未讨论对 M 的敏感性。不过 CKA 在 moderate sample sizes 下通常稳定（Kornblith et al., 2019），所以影响可能有限。\n\n**[AGREE] R1-M5: 未承诺代码/checkpoint 发布。**\n同意。对于以 controlled experiment 为主要贡献的论文，reproducibility 承诺尤为重要。\n\n---\n\n### Missing References\n\n**[REBUT] R1 说 \"无明显缺失\"**\n我不同意。在我的审稿中识别了三篇缺失的相关工作：\n1. **\"When Reasoning Meets Compression\"** (Li et al., 2025, arXiv:2504.02010) — 直接在 DeepSeek-R1 上 benchmark 了剪枝对推理的影响\n2. **\"GPrune-LLM\"** (2026, arXiv:2603.13418) — generalization-aware 剪枝\n3. **\"Can Pruning Improve Reasoning?\"** (2025, arXiv:2505.14582)\n\nR1 建议加 Wanda (Sun et al., 2024)，但 Wanda 是非结构化剪枝，与本文的结构化剪枝关注点不同，相关性较低。\n\n---\n\n### Overall Assessment 比较\n\nR1 给出 3.5 (Borderline Conference)，我给出 3.0 (Findings)。0.5 分差距主要来自：\n\n1. **我对 W1/R1-W6 (SFT ceiling / GRPO 训练不足) 的严重程度评估更高**（我标 Critical，R1 标 Warning）。如果 decoupling 确实是训练不充分的 artifact，则论文 contribution 1 大幅缩水。\n2. **我对 scope overclaiming 更敏感**（Title 中 \"Reasoning LLMs\" vs 单一 Qwen2.5 架构族）。\n3. **我对 RASP 方法贡献的质疑更强**（α=2.0 essentially CKA-dominant，方法贡献有限）。\n\n如果作者能提供：(a) 1000 步 GRPO 至 convergence 的 accuracy 数据证实 decoupling 持续存在，(b) 非 Qwen2.5 架构的验证，我愿意将评分上调至 3.5。\n\n---\n\n### 对 Director 指定的四个焦点问题的总结\n\n| 问题 | R1 评估 | R2 评估 | 共识 |\n|------|---------|---------|------|\n| CKA 循环使用 (R1-W3) | Warning | Minor | 两种 CKA 计算技术上不同（intra-layer vs layer-wise），循环论证指控部分不成立，但应补充说明 |\n| RASP 函数形式 (R1-W4) | Warning | Warning | 同意缺乏理论推导，乘法形式可能人为导致 α=1.0 collapse |\n| SFT ceiling effect (R1-W6) | Warning | **Critical** | R2 认为这是论文最关键的问题——15% sparsity 数据自相矛盾，300 步实验选择性省略 accuracy |\n| TOST ε=2pp (R1-W7) | Warning | Minor-Warning | 论文透明报告了不同 ε 值结果，2pp 在实际意义上合理，但应提供 justify |",
  "reviewer_id": "2",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿意见的逐条评议\n\n---\n\n### Critical Weaknesses\n\n**[AGREE] R1-W1: RASP 单 seed + dose-response 不可靠**\n同意 RASP 及 dose-response 分析为 N=1 是重要缺陷。α=2.0 (66.11%) 与 α=3.0 (61.46%) 之间 4.65pp 的差距在单 seed 下确实可能是随机噪声——作为对照，CKA-only 的 3-seed std 为 0.19pp（Section 4.1），若 RASP 的方差类似，4.65pp 差距是显著的；但若 RASP 因包含 importance 项而方差更大，inverted-U 形状可能不成立。\n\n不过，我认为此问题的严重程度更接近 **Warning 而非 Critical**。原因：论文的核心 claim 是 reward-accuracy decoupling 和 recovery capacity spectrum，这两者主要依赖 CKA-only vs Standard vs Random 的多 seed 比较（3 seeds each, Welch's t-test p=0.0009）。RASP 的 dose-response 是 supporting evidence 而非核心 claim 的唯一支撑。如果去掉 RASP，spectrum 的 CKA-only ≫ Random ≫ Standard ordering 仍然成立。\n\n**[AGREE] R1-W2: Random baseline max_completion_length 不公平**\n完全同意。我在自己的审稿中也将此列为 W4 (Warning)。R1 将其升为 Critical，我理解其逻辑——bias 方向恰好支持论文叙事（压低 Random 的 GRPO reward，使 CKA-only 的 spectrum 优势更突出）。\n\n但我仍倾向于 **Warning** 级别：Random 不是论文的 proposed method，也不是 spectrum 的关键对比对象。核心比较是 CKA-only vs Standard（二者均用 1024 tokens），该比较是公平的。Random 的不公平主要影响 \"Random 在 spectrum 中的位置\" 这个次要 claim。\n\n---\n\n### Warning Weaknesses\n\n**[REBUT] R1-W3: CKA 双重角色的循环论证**\n这是一个有洞察力的观察，但我认为循环论证的指控**不完全成立**，需要区分两个不同的 CKA 计算：\n\n1. **剪枝阶段**（Section 3.2, Eq. 3）：计算 **intra-layer** CKA——同一层内不同 MLP channel group 之间的 pairwise CKA similarity，衡量结构间的功能重叠度。CKA-only 移除与其他结构最相似（最冗余）的 group。\n2. **分析阶段**（Section 4.5, Figure 5）：计算 **layer-wise** CKA——dense model 某层输出与 pruned model 同层输出之间的 CKA，衡量剪枝对层级表示的扰动程度。\n\n这两个 CKA 的对象不同（structure-to-structure vs. layer-to-layer）、目标不同（identify redundancy vs. measure perturbation）。Section 4.5 发现 \"CKA-only diverges most from dense (μ=0.62)\" 不是因为 CKA 被自我验证，而是因为一个可解释的因果链：移除冗余结构 → 消除重复表示 → 每层的总体表示变化更大 → layer-wise CKA 下降。这个因果链即使不用 CKA 衡量也应成立——例如用 L2 距离或 procrustes 距离衡量 dense-pruned 表示差异，CKA-only 也应偏离最大。\n\n不过我承认 R1 的 concern 有一定道理：**读者可能产生 metric 自我验证的印象**。建议作者加一句说明两个 CKA 计算的区别，或补充一个非 CKA 的 representational similarity 指标（如 procrustes distance）作为 robustness check。\n\n**严重程度评估**：Minor，非 Warning。核心 experimental findings（spectrum ordering, decoupling）不依赖 Section 4.5 的 layer-wise CKA 分析——即使删除 Figure 5 及相关讨论，Table 1、Table 2、Figure 3、Figure 4 的结论不受影响。\n\n**[AGREE] R1-W4: RASP 函数形式缺乏理论推导**\n同意。我在 Section 3 的 detailed comments 中也提出了相同问题。乘法形式 I(h) × (1−F(h))^α 意味着 importance 为 0 时无论 diversity 多高分数都为 0（被过滤），但这恰好可能是导致 α=1.0 collapse 的原因——很多低 importance 但高 diversity 的结构被不当移除。加法形式 βI(h) + (1−β)(1−F(h)) 会保留这些结构。\n\n这个函数形式的选择直接影响了 \"α=1.0 collapse\" 这个关键实验结果（Section 4.2），因此不仅是理论缺陷，还可能导致对 importance scoring 有害性的错误结论。如果加法形式下 α=1.0 不 collapse，则 \"importance 对 RL recovery 有害\" 的隐含论点不成立。\n\n**严重程度评估**：同意 R1 的 Warning 级别。与我的 W3 (Critical) 中 \"RASP 贡献叙事自相矛盾\" 呼应——函数形式的武断选择加剧了这个问题。\n\n**[AGREE] R1-W5: 模型和 benchmark 范围窄**\n完全同意，与我的 W2 (Critical) 一致。R1 列为 Warning，我给了 Critical。核心分歧：我认为 title 中 \"Reasoning LLMs\" 的泛化声称使此问题上升为 Critical——如果论文明确将 scope 限定为 \"DeepSeek-R1-Distill-Qwen-7B\"，则 Warning 足矣。\n\n**[AGREE] R1-W6: SFT ceiling effect 假说**\n**强烈同意，且认为 R1 对此问题的严重程度评估偏低。**\n\n这与我的 W1 (Critical) 一致。R1 将其列为 Warning，但我认为是本文**最关键的问题**。原因：\n\n1. **数据支持 ceiling 解释**：SFT 恢复 ~60pp（从 post-prune ~1% 到 59-64%），GRPO 仅贡献 <1pp。Dense model 90.83%，即 GRPO 有 ~27pp 的理论 headroom。100 步 GRPO 仅利用了 <4% 的 headroom（<1pp / 27pp），这更可能是训练不充分而非 intrinsic decoupling。\n\n2. **300 步扩展未解决问题**：Section 4.5 的 300 步实验（Figure 6）仅报告了 reward gap 维持（5.5×），但**关键性地缺失了 accuracy 数据**。如果 CKA-only 在 300 步时 accuracy 有所提升（哪怕 1-2pp），则 \"decoupling\" 的 claim 需要 qualify。论文选择性地只报告 reward 而不报告 accuracy，这是一个值得追问的遗漏。\n\n3. **15% sparsity 的反例**：Section 4.3 自己报告了 15% sparsity 下 GRPO 放大了 CKA-only 优势（SFT gap 5.69pp → GRPO gap 7.20pp）。这恰恰说明当 SFT ceiling 不那么低时（15% 比 20% 留给 GRPO 的 headroom 更大），GRPO 是有增量贡献的——**论文自身的数据 undermines decoupling 的普遍性**。\n\n**建议将此问题升至 Critical**。\n\n**[AGREE] R1-W7: TOST ε=2pp margin post-hoc selection**\n部分同意。R1 的 concern 合理——ε=2pp 未预注册，且 paper 自己报告了 ε=1pp 功效不足（Appendix T：\"ε=1pp margin lacks statistical power with binary outcomes at N=1,319\"），ε=3pp 全通过。ε=2pp 时 7/8 通过，确实有\"刚好合适\"的嫌疑。\n\n但我对此的严重程度评估略低于 R1：\n1. **论文的透明度是加分项**——诚实报告了 ε=1 和 ε=3 的结果，没有隐藏不利数据。\n2. **从实际意义看**，2pp 在 GSM8K 60-66% 区间内是合理的 practical significance threshold。EMNLP 社区通常接受 ~1-2pp 的差异为 \"negligible\"。\n3. **关键证据不仅依赖 TOST**——Table 2 的原始 |Δ| 值（CKA-only +0.48, Standard +0.55, Random -0.53, RASP -0.61）已经直观地展示了 <1pp 的差距。TOST 只是形式化了这一观察。\n\n**严重程度评估**：Minor-to-Warning。ε=2pp 的选择确实应该在论文中 justify（例如引用 GSM8K 相关文献中什么差异被认为是 meaningful），但不影响核心结论的可信度。\n\n---\n\n### Minor Issues\n\n**[AGREE] R1-M1: Recovery capacity 概念先用后定义。**\n同意，但 minor 中的 minor。学术论文中 terminology 先用后定义很常见，尤其在 abstract/intro 中。\n\n**[AGREE] R1-M2: Figure 2 信息密度过高。**\n同意。Figure 2 试图在一个图中展示 structural analysis + scoring criteria + recovery pipeline + recovery spectrum，对不熟悉此工作的读者有认知负担。但 page budget 紧张（8 pages），拆分可能不现实。\n\n**[AGREE] R1-M3: \"Reward-accuracy decoupling\" 术语可能误导。**\n同意，与我的 M4 呼应。\"Decoupling\" 暗示两者原本应耦合，但论文未充分建立这一先验预期。\n\n**[AGREE] R1-M4: Calibration data M=512 未说明理由。**\n同意。Section 3.2 说 M=512 randomly sampled examples，但未讨论对 M 的敏感性。不过 CKA 在 moderate sample sizes 下通常稳定（Kornblith et al., 2019），所以影响可能有限。\n\n**[AGREE] R1-M5: 未承诺代码/checkpoint 发布。**\n同意。对于以 controlled experiment 为主要贡献的论文，reproducibility 承诺尤为重要。\n\n---\n\n### Missing References\n\n**[REBUT] R1 说 \"无明显缺失\"**\n我不同意。在我的审稿中识别了三篇缺失的相关工作：\n1. **\"When Reasoning Meets Compression\"** (Li et al., 2025, arXiv:2504.02010) — 直接在 DeepSeek-R1 上 benchmark 了剪枝对推理的影响\n2. **\"GPrune-LLM\"** (2026, arXiv:2603.13418) — generalization-aware 剪枝\n3. **\"Can Pruning Improve Reasoning?\"** (2025, arXiv:2505.14582)\n\nR1 建议加 Wanda (Sun et al., 2024)，但 Wanda 是非结构化剪枝，与本文的结构化剪枝关注点不同，相关性较低。\n\n---\n\n### Overall Assessment 比较\n\nR1 给出 3.5 (Borderline Conference)，我给出 3.0 (Findings)。0.5 分差距主要来自：\n\n1. **我对 W1/R1-W6 (SFT ceiling / GRPO 训练不足) 的严重程度评估更高**（我标 Critical，R1 标 Warning）。如果 decoupling 确实是训练不充分的 artifact，则论文 contribution 1 大幅缩水。\n2. **我对 scope overclaiming 更敏感**（Title 中 \"Reasoning LLMs\" vs 单一 Qwen2.5 架构族）。\n3. **我对 RASP 方法贡献的质疑更强**（α=2.0 essentially CKA-dominant，方法贡献有限）。\n\n如果作者能提供：(a) 1000 步 GRPO 至 convergence 的 accuracy 数据证实 decoupling 持续存在，(b) 非 Qwen2.5 架构的验证，我愿意将评分上调至 3.5。\n\n---\n\n### 对 Director 指定的四个焦点问题的总结\n\n| 问题 | R1 评估 | R2 评估 | 共识 |\n|------|---------|---------|------|\n| CKA 循环使用 (R1-W3) | Warning | Minor | 两种 CKA 计算技术上不同（intra-layer vs layer-wise），循环论证指控部分不成立，但应补充说明 |\n| RASP 函数形式 (R1-W4) | Warning | Warning | 同意缺乏理论推导，乘法形式可能人为导致 α=1.0 collapse |\n| SFT ceiling effect (R1-W6) | Warning | **Critical** | R2 认为这是论文最关键的问题——15% sparsity 数据自相矛盾，300 步实验选择性省略 accuracy |\n| TOST ε=2pp (R1-W7) | Warning | Minor-Warning | 论文透明报告了不同 ε 值结果，2pp 在实际意义上合理，但应提供 justify |",
    "reviewer_id": "2",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-24T18:17:14.258000+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3512
}
```

</details>

---


### Assistant

_source line 662 · 2026-05-24T18:17:23.888847+00:00_

交叉回应已提交给 Review Director。

核心分歧在 SFT ceiling effect 的严重程度——我认为这是 Critical 而非 R1 的 Warning，因为论文 15% sparsity 的数据自身就 undermine 了 decoupling 的普遍性，且 300 步扩展实验选择性省略了 accuracy 数据。CKA 循环论证问题则比 R1 评估的更轻（两个 CKA 计算技术上是不同指标）。最终评分差异（3.0 vs 3.5）主要来自对训练充分性和 scope overclaiming 的不同权重。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2"
}
```

</details>

---


## Round 17

## Round 17

58 recorded events


### User

_source line 663 · 2026-05-25T21:16:23.011838+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性**审查。

## 论文信息
- 标题: "How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM"
- 目标 venue: **EMNLP 2026**（通过 ARR 统一审稿）
- 截止日期: 2026-05-25
- 论文路径: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/submitted.pdf`

## Venue 格式要求
- **页数限制**: 正文 8 页，参考文献无限制
- **模板**: ACL style template（`\usepackage[review]{acl}`）
- **匿名规则**: Double-blind（ARR 政策）
- **Limitations**: 必须包含，不计入页数
- **评分标准**: 5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit

## 你的审查侧重

### 1. 新颖性与贡献
- "Reward-accuracy decoupling" 是否是一个真正新颖的发现？还是 SFT 训练不足/GRPO 训练不足的 artifact？
- RASP 作为方法贡献的价值：α=2.0（最佳）本质上是 CKA-dominant（diversity 权重 >> importance 权重），这是否 undermines "balancing importance and diversity" 的叙事？
- "Recovery capacity spectrum" 的实用价值——如果所有方法最终 accuracy 差不多，这个 spectrum 的意义何在？
- GRPO 作为 diagnostic probe 的 claim 是否有 actionable value？

### 2. 相关工作与定位
- 检查以下文献是否被引用和充分讨论：
  * Li et al. (2025, arXiv:2504.02010) "When Reasoning Meets Compression"
  * "Can Pruning Improve Reasoning?" (arXiv:2505.14582)
  * 其他结构化剪枝 + reasoning model 的近期工作
- Self-Healing (Ji et al., 2025) 的定位：本文声称 "RLVR > SFT advantage vanishes under structured pruning"——但 Ji et al. 研究的是 unstructured pruning at 96.5% retention，两者的 setting 差异是否被充分讨论？
- 与 Mukherjee et al. (2025, RL Finetunes Small Subnetworks) 的关系

### 3. Framing 准确性
- Title 中 "a Reasoning LLM"（单数）vs 论文覆盖多个模型——是否准确？
- Abstract 中 "moderate sparsity" 是否精确限定了 20-25% 窗口？
- 30% sparsity 全面 collapse 的事实是否被适当讨论？有效窗口 20-25% 是否过窄？
- Contribution 3 "SFT warmup as the dominant recovery mechanism"——如果这是主要发现，为何 Title 和叙事聚焦于 RLVR/GRPO？
- 论文是否存在 overclaiming？（检查 Abstract、Conclusion、Contribution list）

### 4. 写作质量
- Section 5 (Conclusion) 是否过于简短？Discussion 是否充分？
- "recovery capacity spectrum"、"reward-accuracy decoupling"、"dose-response" 等术语是否被清晰定义？
- 概念先用后定义的问题（如 "recovery capacity" 在 Section 1 使用但 Section 3.4 才定义）
- Limitations section 是否覆盖了关键局限？

### 5. 泛化性
- 所有实验基于 Qwen2.5 架构族——Title 是否 overclaim？
- Qwen2.5-Math-7B 仅有 SFT 验证，GRPO 缺失（脚注提供 preliminary 48.60% 但 83.8% truncated）
- 仅 MLP channel pruning，不包含 attention head pruning——scope 是否被正确限定？

请严格、不留情面地评审。输出格式：
```
## Strengths (逐条)
## Weaknesses (逐条，标注严重程度 Critical/Warning/Minor)
## Questions (需要作者回答的)
## Missing References
## Overall Assessment (评分 + 简短理由)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-25T21:16:37.360622+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-25T21:16:37.361023+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 666 · 2026-05-25T21:16:40.422629+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria dimensions"
  }
}
```

</details>

---


### Tool call

_source line 667 · 2026-05-25T21:16:42.630478+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/submitted.pdf",
  "pages": "1-8",
  "project": "recovery_aware_struct_prune",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/submitted.pdf",
    "pages": "1-8",
    "project": "recovery_aware_struct_prune",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 668 · 2026-05-25T21:16:47.652512+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

Based on the search results, here's what I found about ARR reviewer guidelines for 2025-2026:

## Review Score Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Quality Standards

All papers recommended for Findings or main conference are expected to be sound and reproducible.

## Reviewer Responsibilities and Policies

The program chairs and ARR EiCs will consider egregious cases reported by chairs, including cases of extremely terse reviews, unprofessional tone, and LLM-generated reviews. The 'highly irresponsible' reviewers or chairs may have their work desk-rejected from the current cycle, and ineligible for resubmission or commitment during the following ARR cycle.

The search results show that ARR has a clear three-dimensional scoring system focused on soundness, excitement, and overall recommendation for the 2025-2026 review cycles. For more detailed information
…[truncated 241 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7229
}
```

</details>

---


### Tool result

_source line 669 · 2026-05-25T21:16:49.816722+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 396.0}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 578.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 1005.4}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 423.0}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 446.6}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 474.8}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 480.1}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 413.0}], \"total_pages\": 17, \"rendered_pages\": 8, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_
…[truncated 96 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7186
}
```

</details>

---


### Tool call

_source line 670 · 2026-05-25T21:16:54.590374+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete review form dimensions, scoring scales, and criteria. I need: 1) All scoring dimensions (soundness, excitement, overall, etc.) with their exact scale definitions. 2) What each score level means. 3) Any specific guidance on what constitutes each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete review form dimensions, scoring scales, and criteria. I need: 1) All scoring dimensions (soundness, excitement, overall, etc.) with their exact scale definitions. 2) What each score level means. 3) Any specific guidance on what constitutes each score level."
  }
}
```

</details>

---


### Tool call

_source line 671 · 2026-05-25T21:16:54.942222+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool result

_source line 672 · 2026-05-25T21:16:55.900984+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 673 · 2026-05-25T21:16:55.901486+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-25T21:16:56.403546+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-25T21:16:56.757245+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 855
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-25T21:16:56.807898+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 677 · 2026-05-25T21:16:58.506120+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2102
}
```

</details>

---


### Tool result

_source line 678 · 2026-05-25T21:16:58.657837+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1849
}
```

</details>

---


### Tool result

_source line 679 · 2026-05-25T21:17:00.272385+00:00_

# ARR Review Form Dimensions

Based on the guidelines provided, **the document does not contain the complete review form specifications** with exact scale definitions and score level meanings.

## What Is Specified

The guidelines reference three scoring dimensions introduced in February 2025:

1. **Soundness** - "must be justified by the text of the review"
2. **Excitement** - described as "orthogonal to the assessment of soundness" and reflecting "personal taste"
3. **Overall Assessment** - "a composite score reflecting your assessment of soundness, excitement, and also other factors like novelty and impact"

## Key Guidance Provided

The guidelines emphasize that "low soundness scores should be justified" and that papers committed to venues "are expected to be sufficiently sound and reproducible," though reviewers may find work sound but personally uninteresting.

## Critical Gap

The document states reviewers should check "that your scores reflect the review" but **does not provide the actual numerical scales, point ranges, or explicit definitions** for each score level (e.g., 1-5, 1-10, or categorical labels like "Weak/Acceptable/Strong").

For complete review form specifications, you would need to consult the detailed [review form documentation](https://aclrollingreview.org/reviewform) referenced in the guidelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5682
}
```

</details>

---


### Tool call

_source line 680 · 2026-05-25T21:17:05.699400+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 681 · 2026-05-25T21:17:06.253470+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 682 · 2026-05-25T21:17:06.708100+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool call

_source line 683 · 2026-05-25T21:17:06.708548+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 684 · 2026-05-25T21:17:07.661722+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1408
}
```

</details>

---


### Tool result

_source line 685 · 2026-05-25T21:17:07.662586+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 686 · 2026-05-25T21:17:07.813306+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-25T21:17:09.619941+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1806
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-25T21:17:09.770941+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their numerical scales, and what each score level means. Include soundness, excitement, overall assessment, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their numerical scales, and what each score level means. Include soundness, excitement, overall assessment, confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool result

_source line 689 · 2026-05-25T21:17:14.828678+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence
**Scale: 1-5**
- 5: "Positive that my evaluation is correct"
- 4: "Quite sure" with unlikely but possible missed details
- 3: "Pretty sure" but may have missed specifics
- 2: "Willing to defend" but likely missed details or novelty
- 1: "Not my area" or paper very difficult to understand

## Soundness
**Scale: 1-5 (with .5 increments)**
- 5: "Excellent: most thorough" study of its type
- 4: "Strong: sufficient support" for claims
- 3: "Acceptable: sufficient support" for main claims
- 2: "Poor: main claims not sufficiently supported"
- 1: "Major Issues: not sufficiently thorough" for publication

## Excitement
**Scale: 1-5 (with .5 increments)**
- 5: "Highly Exciting: would recommend" to others
- 4: "Exciting: would mention" to others
- 3: "Interesting: might mention" some points
- 2: "Potentially Interesting: does not resonate" with reviewer
- 1: "Not Exciting: does not resonate" and unlikely to resonate broadly

## Overall Assessment
**Scale: 1-5 (with .5 increments)**
- 5: "Consider for Award" (top 2.5%)
- 4: "Conference: could be accepted"
- 3: "Findings: could be accepted"
- 2: "Resubmit next cycle" with substantial revisions
- 1: "Do not resubmit" or irrelevant to field

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5057
}
```

</details>

---


### Tool call

_source line 690 · 2026-05-25T21:17:30.990731+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/submitted.pdf",
  "pages": "9-17",
  "project": "recovery_aware_struct_prune",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/submitted.pdf",
    "pages": "9-17",
    "project": "recovery_aware_struct_prune",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-25T21:17:31.944079+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 565.2}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 578.4}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 432.7}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 473.1}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 437.9}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 477.2}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 495.1}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 477.4}, {\"page\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_r
…[truncated 335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 692 · 2026-05-25T21:17:35.305681+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 693 · 2026-05-25T21:17:35.506802+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 694 · 2026-05-25T21:17:36.211117+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 695 · 2026-05-25T21:17:36.211574+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 696 · 2026-05-25T21:17:36.563500+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1056
}
```

</details>

---


### Tool call

_source line 697 · 2026-05-25T21:17:36.563837+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 698 · 2026-05-25T21:17:37.317475+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1105
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-25T21:17:37.469476+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 700 · 2026-05-25T21:17:42.487779+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 701 · 2026-05-25T21:17:43.091920+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 604
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-25T21:17:43.094445+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 703 · 2026-05-25T21:17:43.445999+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 704 · 2026-05-25T21:17:44.102081+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool call

_source line 705 · 2026-05-25T21:17:44.102517+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 706 · 2026-05-25T21:17:44.204046+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 758
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-25T21:17:44.759181+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-25T21:17:50.580011+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li et al 2025 arXiv 2504.02010 \"When Reasoning Meets Compression\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li et al 2025 arXiv 2504.02010 \"When Reasoning Meets Compression\""
  }
}
```

</details>

---


### Tool call

_source line 709 · 2026-05-25T21:17:51.332937+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2505.14582 \"Can Pruning Improve Reasoning\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2505.14582 \"Can Pruning Improve Reasoning\""
  }
}
```

</details>

---


### Tool call

_source line 710 · 2026-05-25T21:17:52.136467+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mukherjee et al 2025 \"RL Finetunes Small Subnetworks\" reinforcement learning pruning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mukherjee et al 2025 \"RL Finetunes Small Subnetworks\" reinforcement learning pruning"
  }
}
```

</details>

---


### Tool result

_source line 711 · 2026-05-25T21:17:58.429824+00:00_

Web search results for query: "Li et al 2025 arXiv 2504.02010 "When Reasoning Meets Compression""

Links: [{"title":"[2504.02010] When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models","url":"https://arxiv.org/abs/2504.02010"},{"title":"When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models","url":"https://arxiv.org/html/2504.02010"},{"title":"When Reasoning Meets Compression: Benchmarking Compressed Large Reasoning Models on Complex Reasoning Tasks","url":"https://arxiv.org/html/2504.02010v1"},{"title":"Reasoning as Compression: Unifying Budget Forcing via the Conditional Information Bottleneck","url":"https://arxiv.org/pdf/2603.08462"},{"title":"WHEN REASONING MEETS COMPRESSION: UNDER-","url":"https://arxiv.org/pdf/2504.02010"},{"title":"Machine Learning Apr 2025","url":"https://www.arxiv.org/list/cs.LG/2025-04?skip=100&show=50"}]

I found the paper! Here's what I found about the arXiv preprint 2504.02010:

**Title:** When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models

**Authors:** Nan Zhang, Eugene Kwek, Yusen Zhang, Ngoc-Hieu Nguyen, Prasenjit Mitra, Rui Zhang

**Main Focus:** The paper investigates how the reasoning capabilities of LRMs are compromised during compression, through performance benchmarking and mechanistic interpretation.

**Compression Methods Studied:** Compression methods, including quantization, distillation, and pruning, improve the computational efficiency of large reasoning models (LRMs).

**Research Approach:** The authors benchmark quantized, distilled, and pruned DeepSeek-R1 models on four reasoning datasets (AIME 2024, FOLIO, Temporal Sequences, and MuSiQue). To precisely locate compression effects on model weights, they adapt difference of means and attribution patching techniques, focusing on the activation of every linear component in compressed LRMs, to interpret fine-grained c
…[truncated 260 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7849
}
```

</details>

---


### Tool result

_source line 712 · 2026-05-25T21:17:58.480496+00:00_

Web search results for query: "arXiv 2505.14582 "Can Pruning Improve Reasoning""

Links: [{"title":"[2505.14582v1] Can Pruning Improve Reasoning? Revisiting Long-CoT Compression with Capability in Mind for Better Reasoning","url":"https://arxiv.org/abs/2505.14582v1"},{"title":"[2505.14582v2] Can Pruning Improve Reasoning? Revisiting Long-CoT Compression with Capability in Mind for Better Reasoning","url":"https://arxiv.org/abs/2505.14582v2"},{"title":"[2505.14582] Can Pruning Improve Reasoning? Revisiting Long-CoT Compression with Capability in Mind for Better Reasoning","url":"https://arxiv.org/abs/2505.14582"},{"title":"Can Pruning Improve Reasoning? Revisiting Long-CoT Compression with Capability in Mind for Better Reasoning","url":"https://arxiv.org/pdf/2505.14582"},{"title":"Can Pruning Improve Reasoning? Revisiting Long-CoT Compression with Capability in Mind for Better Reasoning","url":"https://arxiv.org/html/2505.14582"}]

The search returned results for arXiv paper 2505.14582. Here's what I found:

**Title:** "Can Pruning Improve Reasoning? Revisiting Long-CoT Compression with Capability in Mind for Better Reasoning"

**Authors:** Shangziqi Zhao, Jiahao Yuan, Jinyang Wu, Zhenglin Wang, Guisong Yang, Usman Naseem

**Key Findings:**

Long chain-of-thought (Long-CoT) reasoning improves accuracy in LLMs, yet its verbose, self-reflective style often hinders effective distillation into small language models (SLMs).

The paper proposes "Prune-on-Logic, a structure-aware framework that transforms Long-CoT into logic graphs and selectively prunes low-utility reasoning steps under self-verification constraints".

**Main Results:** Through systematic analysis across three pruning strategies targeting entire chains, core reasoning, and verification, verification pruning consistently improves accuracy while reducing token usage, whereas pruning reasoning steps or indiscriminate pruning degrades performance.

**Key Insight:** The study reveals that effective pruning alig
…[truncated 267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7147
}
```

</details>

---


### Tool result

_source line 713 · 2026-05-25T21:18:00.193645+00:00_

Web search results for query: "Mukherjee et al 2025 "RL Finetunes Small Subnetworks" reinforcement learning pruning"

Links: [{"title":"Reinforcement Learning Finetunes Small Subnetworks in Large Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/reinforcement-learning-finetunes-small-subnetworks-large-language"},{"title":"NeurIPS Poster Reinforcement Learning Finetunes Small Subnetworks in Large Language Models","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/120324"},{"title":"[PDF] Reinforcement Learning Finetunes Small Subnetworks in Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Reinforcement-Learning-Finetunes-Small-Subnetworks-Mukherjee-Yuan/177d189e0e939d3afd56569ac908b5d88e0c67f9"},{"title":"Papers by Sagnik Mukherjee","url":"https://www.aimodels.fyi/author-profile/sagnik-mukherjee-93fa029d-5f90-4777-97d9-c3b974219e61"},{"title":"RL'S RAZOR","url":"https://openreview.net/pdf/a9b3d93564c9b0142c39424d0e42b5a20fd13484.pdf"},{"title":"[2505.11711v1] Reinforcement Learning Finetunes Small Subnetworks in Large Language Models","url":"https://arxiv.org/abs/2505.11711v1"},{"title":"[2505.11711] Reinforcement Learning Finetunes Small Subnetworks in Large Language Models","url":"https://arxiv.org/abs/2505.11711"},{"title":"Reinforcement Learning Finetunes Small Subnetworks in Large Language Models","url":"https://arxiv.org/html/2505.11711"},{"title":"Reinforcement Learning Finetunes Small Subnetworks in Large Language Models","url":"https://arxiv.org/pdf/2505.11711"}]

I found the paper! Here's what I found about the Mukherjee et al. 2025 study:

## Key Findings

The paper demonstrates that reinforcement learning yields substantial improvements in large language models' downstream task performance and alignment with human values, but surprisingly, such large gains result from updating only a small subnetwork comprising just 5%-30% of the parameters.

This phenomenon is referred
…[truncated 1051 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8057
}
```

</details>

---


### Tool call

_source line 714 · 2026-05-25T21:22:41.906786+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见（Round 1）：新颖性 + 完整性\n\n**论文**: \"How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM\"\n**Venue**: EMNLP 2026 (ARR)\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 / 5 — Findings\n**一句话总结**: 实验设计严谨、控制变量干净，但核心新颖性不足——\"reward-accuracy decoupling\"很可能是 SFT 天花板效应的 artifact 而非独立发现，RASP 方法贡献被 α=2.0 (CKA-dominant) 的最优点 undermined，有效剪枝窗口仅 20–25% 严重限制实用价值。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 控制变量设计好，TOST 等统计检验到位，但核心 claim (\"decoupling\") 存在未排除的混淆因素 |\n| Excitement | 2.5/5 | 研究问题有意义，但主要发现是 \"SFT 做了大部分工作，GRPO 贡献边际\"——这个结论的 actionable value 有限 |\n| Overall | 3.0/5 | Findings 水平：实证贡献扎实但新颖性和影响力不足以支撑主会议接收 |\n| Confidence | 4/5 | 熟悉 LLM 剪枝和 RL fine-tuning 领域 |\n\n---\n\n## Strengths（优势）\n\n**S1. 干净的控制变量实验设计。** 四种剪枝标准共享同一结构分析流程（importance + CKA），仅改变组合方式，然后经历完全相同的两阶段恢复（SFT → GRPO）。这是剪枝文献中罕见的严谨对比，能有效隔离剪枝标准本身的效应。Algorithm 1（Appendix B）清晰形式化了这一框架。\n\n**S2. 统计严谨性远超同领域平均水平。** TOST 等价检验（Appendix T）、多种子 GRPO 验证（Appendix L，3 seeds ×4 methods）、paired Two One-Sided Tests、cross-seed 标准差报告（Section 4.5, σ=0.19 pp）——这些在剪枝实证论文中不常见。\n\n**S3. 丰富的 Appendix 系统。** 从 A 到 V 共 22 个 appendix，覆盖 CKA 稳定性（H）、梯度信号分析（I）、30% 剪枝崩塌（K）、深度优先基线（R）、per-layer capacity floor（S）等。显示了对审稿人可能质疑的全面预判。\n\n**S4. Recovery capacity spectrum 概念有启发性。** 用 GRPO 训练动态（peak reward, f₀, gradient norm, KL divergence）作为剪枝结构质量的诊断信号（Section 3.5, Figure 5），虽然目前主要是 correlational，但提供了一个有趣的视角。\n\n**S5. 跨尺度验证初步覆盖。** DeepSeek-R1-Distill-Qwen-1.5B（Appendix N）和 Qwen2.5-Math-7B（Appendix O）的初步验证显示 recovery capacity spectrum ordering 在不同模型上基本一致。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [Critical] **\"Reward-accuracy decoupling\" 极可能是 SFT 天花板效应的 artifact，而非独立发现**\n- 具体位置：Section 4.3, Table 2, Figure 6\n- 问题：论文声称 GRPO 产生高 reward 但几乎不改变 accuracy，称之为 \"decoupling\"。但数据显示 SFT warmup 已将 accuracy 恢复到 51–64%（取决于剪枝标准），而 dense model 为 90.83%（Table 2, \"Unpruned\" 行）。在 20% 结构化剪枝下，模型的有效天花板显著低于 dense model——SFT 阶段已消耗了大部分可恢复空间。GRPO 仅增加 |Δ|≤1pp（Section 4.3）更可能反映的是该剪枝级别下的 accuracy ceiling，而非 reward 与 accuracy 的本质性解耦。\n- 论文未排除的关键混淆因素：(a) SFT 已用尽 recoverable accuracy headroom；(b) 二值 reward 信号在 f₀ > 0.5 时自然饱和（Section 3.5 自己承认 \"GRPO's group-relative advantage is zero for uniform-reward batches\"）；(c) 更长的 GRPO 训练是否能打破 decoupling（Appendix E 的 300 步扩展仍不充分——真实 RLVR 常训练数千步）。\n- 为什么影响接收：这是论文的核心 contribution 之一（Contribution 1）。如果 decoupling 只是 SFT 接近天花板后的自然现象，那么这个 \"发现\" 就缺乏新颖性——它是任何充分 SFT warmup 后都会出现的预期行为。\n- 建议修改方向：(1) 设计消融实验——减少 SFT 步数（如从 2 epochs 减到 0.5 epoch），在 SFT 未充分恢复时观察 GRPO 是否仍然 decouple；(2) 在不同 SFT recovery 水平（如 post-SFT acc = 40%, 50%, 60%）下测量 GRPO 的 accuracy gain，看是否存在系统性的 headroom 效应；(3) 至少在 Discussion 中承认并讨论这一替代解释。\n\n**N2** [Critical] **RASP 的最优 α=2.0 实质是 CKA-dominant，undermines \"balancing importance and diversity\" 的核心叙事**\n- 具体位置：Section 3.3 Eq. 5, Section 4.4, Table 1, Appendix D\n- 问题：RASP 被 framed 为 \"a scoring function that balances gradient importance with CKA-based representational diversity\"（Abstract）。但 dose-response 分析（Section 4.4）显示最佳 α=2.0，此时 diversity term $(1-F(h))^2$ 远大于 importance term $I(h)$，使得 RASP 实际行为接近 CKA-only。Appendix D 进一步确认 α=2.0 时 peak reward 0.354，接近 CKA-only 的 0.354（Table 1 也显示两者 peak reward 和 mean reward 非常接近）。这意味着 \"balancing\" 叙事与最优解不一致——最优策略实际上是几乎完全依赖 diversity。\n- 为什么影响接收：RASP 是论文的主要方法贡献。如果最优解是 CKA-dominant，那么 RASP 作为一个 parametric family 的贡献就退化为 \"在 CKA-only 基础上加了一个几乎不起作用的 importance 项\"，方法新颖性大打折扣。\n- 建议修改方向：(1) 诚实地将 RASP 重新 frame 为一个 interpolation family，并强调 dose-response 分析本身是贡献（揭示 diversity >> importance 的不对称性），而非 \"balancing\"；(2) 讨论为什么 importance 在 CKA overlap 存在时变得冗余。\n\n**N3** [Critical] **有效剪枝窗口仅 20–25%，30% 全面崩塌——实用价值严重受限但论文 framing 不够坦诚**\n- 具体位置：Section 4.1（\"All methods collapse at 30% sparsity\"），Appendix K（Table 10）\n- 问题：论文在 abstract 中使用 \"moderate sparsity\" 一词，但实际有效窗口仅为 20–25% MLP channel sparsity（Appendix K: 30% 时 accuracy 降至 4–5%，EOS rate < 6%）。对于一个 7B 模型，20–25% MLP 通道剪枝 仅约去除整体参数的约 12-15%（因为 attention 层未被剪枝），实际压缩效果非常有限。Appendix C 报告推理延迟仅减少 18%。在模型压缩文献中，这个操作范围过窄，难以证明方法的实用价值。\n- 论文处理方式：30% collapse 被放在 Appendix K 中，主文仅在 Section 4.1 一句话提及。Abstract 和 Introduction 均未明确限定有效窗口的上限。\n- 为什么影响接收：如果一个关于 \"pruning criteria\" 的研究只在非常窄的窗口内有效，读者需要在最前面就了解这个限制。将其弱化为 \"moderate sparsity\" 并将 collapse 分析放到 appendix，构成 framing 上的不坦诚。\n- 建议修改方向：(1) Abstract 和 Introduction 中明确写出 \"20–25% MLP channel sparsity (approximately 12–15% total parameter reduction)\"；(2) 将 30% collapse 分析从 Appendix K 提升到主文 Discussion 中；(3) 讨论为什么结构化剪枝在 reasoning LLM 上的耐受度如此低，这本身可以是一个有价值的发现。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [Warning] **Title 和叙事聚焦 RLVR/GRPO，但主要发现是 SFT dominates——存在 framing 错位**\n- 具体位置：Title, Abstract, Contribution 3\n- 问题：Title 为 \"How Pruning Criteria Shape Post-RLVR Recovery\"，叙事围绕 RLVR 展开。但 Contribution 3 明确指出 \"SFT warmup as the dominant recovery mechanism\"，Section 4.3 承认 GRPO 仅增加 |Δ|≤1pp。如果 SFT 才是 dominant mechanism，为什么论文不是关于 \"How Pruning Criteria Shape Post-SFT Recovery\"？GRPO 在这里更像是一个 afterthought 而非核心。\n- 建议：要么 (a) 重新组织叙事，将 \"SFT dominates, GRPO serves only as diagnostic\" 作为核心 takeaway 而非第三贡献；要么 (b) 提供证据说明在何种条件下 GRPO 贡献是实质性的（如更高剪枝率、不同 reward signal）。\n\n**W2** [Warning] **Ji et al. (2025, Self-Healing) 对比设置差异过大，论文的 \"advantage vanishes\" claim 过强**\n- 具体位置：Section 2 (Related Work), Abstract 第 2-3 句\n- 问题：Abstract 声称 \"this advantage vanishes under fine-grained structured pruning\"，暗示推翻了 Ji et al. 的发现。但两者设置差异巨大：Ji et al. 研究的是 unstructured pruning at 96.5% retention（仅移除 3.5% 权重），本文研究 structured MLP channel pruning at 75–80% retention（移除 20–25%）。Unstructured vs. structured 是根本不同的剪枝范式，直接对比并声称 \"vanishes\" 是 overclaiming。\n- 建议：(1) 弱化措辞为 \"does not straightforwardly extend to structured pruning\"；(2) 在 Related Work 中更明确地讨论两种范式差异对恢复的影响。\n\n**W3** [Warning] **单一架构族（Qwen2.5）且 Title 暗示泛化性**\n- 具体位置：Title (\"a Reasoning LLM\"), Limitations (page 9)\n- 问题：所有实验模型均基于 Qwen2.5 架构——主模型 DeepSeek-R1-Distill-Qwen-7B（Qwen2.5-7B 蒸馏版）、验证模型 DeepSeek-R1-Distill-Qwen-1.5B 和 Qwen2.5-Math-7B。Title 中 \"a Reasoning LLM\" 在技术上正确（指主模型），但给读者的印象是结论对 reasoning LLM 普遍成立。Limitations section 承认了这一点，但未讨论为什么选择了同一架构族的三个变体而非跨架构验证（如 LLaMA-based reasoning models）。\n- 建议：Title 改为 \"...in Qwen2.5-Family Reasoning Models\" 或在 abstract 中更早明确架构限制。\n\n**W4** [Warning] **Qwen2.5-Math-7B 的 GRPO 验证缺失**\n- 具体位置：Appendix O, 脚注（page 15）\n- 问题：Qwen2.5-Math-7B 仅有 SFT 阶段验证。脚注提到 \"Preliminary GRPO evaluations: 48.60% (2/4500), but 83.8% of responses were truncated at 2048 tokens\"。83.8% truncation rate 意味着 GRPO 结果完全不可靠。对于声称 \"recovery capacity spectrum generalizes across models\" 的论文，在一个验证模型上缺少完整的两阶段验证是显著空白。\n- 建议：要么 (a) 完成 GRPO 验证（增加 max generation length）；要么 (b) 明确将 Qwen2.5-Math-7B 的结论限制在 SFT 阶段，并在 Limitations 中讨论。\n\n**W5** [Warning] **Discussion 被放在 Appendix U 而非主文——削弱了论文的完整性**\n- 具体位置：Section 5 (Conclusion, page 8), Appendix U (page 16)\n- 问题：Section 5 仅有 ~15 行的 conclusion，没有独立的 Discussion section。关于 implications for deployment pipelines 和 GRPO diagnostics 的讨论被放在 Appendix U。对于一篇以 empirical findings 为核心的论文，Discussion 是读者理解 findings 意义的关键部分，不应放在 appendix 中。\n- 建议：将 Appendix U 的核心内容（至少 \"Implications\" 段落）移回主文，可以压缩其他部分（如 Section 4.5 的 representational diversity evidence 部分细节可以移到 appendix）。\n\n**W6** [Warning] **Recovery capacity spectrum 的实用价值不清晰**\n- 具体位置：Section 4.2, Table 1\n- 问题：论文定义了 recovery capacity 作为 GRPO 训练中的 max batch-mean reward（Section 3.5），并据此建立了方法排序（CKA-only > Random > Standard > RASP(α→1)）。但 Table 1 显示 post-SFT+GRPO 的最终 accuracy 差异很小（CKA-only 64.39% vs Standard 59.84%, 主要差异来自 SFT 阶段）。如果最终 accuracy 差异可以通过 post-SFT accuracy 直接观察到，recovery capacity spectrum 作为 GRPO-based diagnostic 的附加价值何在？论文未论证在什么场景下 GRPO probe 比直接评估 post-SFT accuracy 更有信息量。\n- 建议：给出一个 GRPO diagnostic 比 SFT accuracy 更有价值的具体场景（如 GRPO 能揭示 SFT accuracy 无法区分的结构差异），或弱化此 claim。\n\n---\n\n## 小问题（不影响接收）\n\n**M1** [Minor] **概念前向引用**：recovery capacity 在 Section 1（Contribution 2）中使用，但直到 Section 3.5 才正式定义。\"Reward-accuracy decoupling\" 在 Introduction 出现但 Section 4.3 才解释。建议在 Introduction 首次使用时给出简短定义。\n\n**M2** [Minor] **\"dose-response\" 术语借用**：该术语源自药理学/毒理学，在 ML 文献中不常见。Section 4.4 使用但未解释其隐喻意义。对不熟悉该术语的读者可能造成困惑。\n\n**M3** [Minor] **Figure 4 scatter plot 可读性差**：四个子图中的颜色/符号区分度不够，尤其在灰度打印时。建议使用不同形状标记。\n\n**M4** [Minor] **Limitations 遗漏了 MLP-only 限制**：Limitations section 提到了单一架构族和有限 benchmark，但未提及实验仅覆盖 MLP channel pruning 而未包含 attention head pruning。鉴于 attention head pruning 在结构化剪枝文献中同等重要，这应被列为 limitation。\n\n**M5** [Minor] **Figure 1 在 abstract 之前引用**：Page 1 的 Introduction 在 abstract 之后立即引用 Figure 1（\"the dose-response curve (Figure 1)\"），但这个 figure 的上下文在 Section 4.4 才充分展开，对首次阅读的读者来说跳跃较大。\n\n---\n\n## Questions（需要作者回答）\n\n**Q1**: 如果将 SFT warmup 从 2 epochs 减少到 0.5 epochs，使得 post-SFT accuracy 显著低于当前水平，GRPO 阶段是否会产生更大的 accuracy gain？如果是，\"reward-accuracy decoupling\" 是否只是 SFT 充分恢复后的天花板效应？\n\n**Q2**: RASP(α=2.0) 和 CKA-only 的实际剪枝决策在多大程度上重叠？即在 20% sparsity 下，两者移除的 MLP channel groups 有多少比例相同？如果重叠度很高（>80%），RASP 的独立方法贡献就非常有限。\n\n**Q3**: 论文声称 GRPO 可以作为 \"diagnostic probe\"（~100 步即可），但 Table 1 中 post-SFT accuracy 已经能区分不同剪枝标准的恢复质量（CKA-only 64.39% vs Standard 59.84%）。在什么具体场景下，~100 步 GRPO probe 比直接评估 post-SFT accuracy 更有诊断价值？\n\n**Q4**: 30% sparsity 下所有方法崩塌，accuracy 降至 4–5%（Appendix K）。是否尝试过在 25%–30% 之间更细粒度的 sparsity level（如 26%, 27%, 28%）来找到确切的 cliff 位置？这对理解为什么结构化剪枝在 reasoning model 上如此脆弱很有价值。\n\n**Q5**: Extended GRPO training（Appendix E, 300 步）仍然没有改变 ordering 或打破 decoupling。是否考虑过训练更长（如 1000–3000 步，接近文献中常见的 RLVR 训练预算）？\n\n---\n\n## Missing References / 引用讨论不足\n\n**R1**: **Zhang et al. (2025, arXiv:2504.02010) \"When Reasoning Meets Compression\"** — 已出现在参考文献中，但在 Related Work 主文中仅作为 bundled citation 出现，未被单独讨论。该文研究了量化、蒸馏和剪枝对 reasoning LLM 的影响，直接相关——应在 Related Work 中讨论其发现与本文的异同（特别是他们发现的 compression 对不同 reasoning 能力的差异化影响）。\n\n**R2**: **Zhao et al. (2025, arXiv:2505.14582) \"Can Pruning Improve Reasoning?\"** — 已引用，但应在 Related Work 中明确区分：该文研究的是 reasoning trace pruning（Long-CoT token-level），而本文研究的是 model structure pruning。两者使用相同的 \"pruning\" 术语但含义完全不同，需要明确讨论以避免读者混淆。\n\n**R3**: **Mukherjee et al. (2025, arXiv:2505.11711) \"Reinforcement Learning Finetunes Small Subnetworks\"** — 已引用并在 Related Work 中简要讨论。但该文发现 RL 只更新 5–30% 参数的 subnetwork——这与本文 GRPO 阶段 accuracy 增益极小的发现高度相关。建议在 Discussion 中更深入连接：如果 GRPO 只更新一个小 subnetwork，而结构化剪枝可能恰好破坏了该 subnetwork 的关键部分，这是否解释了 criterion-dependent 的 reward 差异？\n\n---\n\n## Overall Assessment\n\n**评分：3.0 / 5 — Findings**\n\n**理由**：这是一篇实验设计严谨、统计方法规范的实证研究，控制变量范式值得肯定。但存在三个核心问题削弱了其主会议接收的竞争力：\n\n1. **新颖性不足**：最核心的 \"reward-accuracy decoupling\" 发现很可能是 SFT 天花板效应的 artifact，而非独立的科学发现。RASP 的方法贡献被 α=2.0 (CKA-dominant) 最优解所 undermined。\n\n2. **Framing 问题**：论文围绕 RLVR/GRPO 组织叙事，但实际主要发现是 SFT 才是 dominant recovery mechanism。Title 和 narrative 的焦点与实际发现不匹配。\n\n3. **实用性受限**：有效窗口仅 20–25% MLP sparsity（~12–15% 总参数压缩），30% 即全面崩塌。这个操作范围过窄，限制了方法的实际应用价值。\n\n如果作者能 (a) 通过消融实验排除天花板效应作为 decoupling 的解释，(b) 诚实地重新 frame RASP 和叙事焦点，(c) 将有效窗口的局限性上提到主文——论文有潜力达到 3.5（Borderline Conference）。当前状态更适合 Findings track。\n",
  "reviewer_id": "2",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿意见（Round 1）：新颖性 + 完整性\n\n**论文**: \"How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM\"\n**Venue**: EMNLP 2026 (ARR)\n\n---\n\n## 总体评分\n\n**Overall Assessment**: 3.0 / 5 — Findings\n**一句话总结**: 实验设计严谨、控制变量干净，但核心新颖性不足——\"reward-accuracy decoupling\"很可能是 SFT 天花板效应的 artifact 而非独立发现，RASP 方法贡献被 α=2.0 (CKA-dominant) 的最优点 undermined，有效剪枝窗口仅 20–25% 严重限制实用价值。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 控制变量设计好，TOST 等统计检验到位，但核心 claim (\"decoupling\") 存在未排除的混淆因素 |\n| Excitement | 2.5/5 | 研究问题有意义，但主要发现是 \"SFT 做了大部分工作，GRPO 贡献边际\"——这个结论的 actionable value 有限 |\n| Overall | 3.0/5 | Findings 水平：实证贡献扎实但新颖性和影响力不足以支撑主会议接收 |\n| Confidence | 4/5 | 熟悉 LLM 剪枝和 RL fine-tuning 领域 |\n\n---\n\n## Strengths（优势）\n\n**S1. 干净的控制变量实验设计。** 四种剪枝标准共享同一结构分析流程（importance + CKA），仅改变组合方式，然后经历完全相同的两阶段恢复（SFT → GRPO）。这是剪枝文献中罕见的严谨对比，能有效隔离剪枝标准本身的效应。Algorithm 1（Appendix B）清晰形式化了这一框架。\n\n**S2. 统计严谨性远超同领域平均水平。** TOST 等价检验（Appendix T）、多种子 GRPO 验证（Appendix L，3 seeds ×4 methods）、paired Two One-Sided Tests、cross-seed 标准差报告（Section 4.5, σ=0.19 pp）——这些在剪枝实证论文中不常见。\n\n**S3. 丰富的 Appendix 系统。** 从 A 到 V 共 22 个 appendix，覆盖 CKA 稳定性（H）、梯度信号分析（I）、30% 剪枝崩塌（K）、深度优先基线（R）、per-layer capacity floor（S）等。显示了对审稿人可能质疑的全面预判。\n\n**S4. Recovery capacity spectrum 概念有启发性。** 用 GRPO 训练动态（peak reward, f₀, gradient norm, KL divergence）作为剪枝结构质量的诊断信号（Section 3.5, Figure 5），虽然目前主要是 correlational，但提供了一个有趣的视角。\n\n**S5. 跨尺度验证初步覆盖。** DeepSeek-R1-Distill-Qwen-1.5B（Appendix N）和 Qwen2.5-Math-7B（Appendix O）的初步验证显示 recovery capacity spectrum ordering 在不同模型上基本一致。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [Critical] **\"Reward-accuracy decoupling\" 极可能是 SFT 天花板效应的 artifact，而非独立发现**\n- 具体位置：Section 4.3, Table 2, Figure 6\n- 问题：论文声称 GRPO 产生高 reward 但几乎不改变 accuracy，称之为 \"decoupling\"。但数据显示 SFT warmup 已将 accuracy 恢复到 51–64%（取决于剪枝标准），而 dense model 为 90.83%（Table 2, \"Unpruned\" 行）。在 20% 结构化剪枝下，模型的有效天花板显著低于 dense model——SFT 阶段已消耗了大部分可恢复空间。GRPO 仅增加 |Δ|≤1pp（Section 4.3）更可能反映的是该剪枝级别下的 accuracy ceiling，而非 reward 与 accuracy 的本质性解耦。\n- 论文未排除的关键混淆因素：(a) SFT 已用尽 recoverable accuracy headroom；(b) 二值 reward 信号在 f₀ > 0.5 时自然饱和（Section 3.5 自己承认 \"GRPO's group-relative advantage is zero for uniform-reward batches\"）；(c) 更长的 GRPO 训练是否能打破 decoupling（Appendix E 的 300 步扩展仍不充分——真实 RLVR 常训练数千步）。\n- 为什么影响接收：这是论文的核心 contribution 之一（Contribution 1）。如果 decoupling 只是 SFT 接近天花板后的自然现象，那么这个 \"发现\" 就缺乏新颖性——它是任何充分 SFT warmup 后都会出现的预期行为。\n- 建议修改方向：(1) 设计消融实验——减少 SFT 步数（如从 2 epochs 减到 0.5 epoch），在 SFT 未充分恢复时观察 GRPO 是否仍然 decouple；(2) 在不同 SFT recovery 水平（如 post-SFT acc = 40%, 50%, 60%）下测量 GRPO 的 accuracy gain，看是否存在系统性的 headroom 效应；(3) 至少在 Discussion 中承认并讨论这一替代解释。\n\n**N2** [Critical] **RASP 的最优 α=2.0 实质是 CKA-dominant，undermines \"balancing importance and diversity\" 的核心叙事**\n- 具体位置：Section 3.3 Eq. 5, Section 4.4, Table 1, Appendix D\n- 问题：RASP 被 framed 为 \"a scoring function that balances gradient importance with CKA-based representational diversity\"（Abstract）。但 dose-response 分析（Section 4.4）显示最佳 α=2.0，此时 diversity term $(1-F(h))^2$ 远大于 importance term $I(h)$，使得 RASP 实际行为接近 CKA-only。Appendix D 进一步确认 α=2.0 时 peak reward 0.354，接近 CKA-only 的 0.354（Table 1 也显示两者 peak reward 和 mean reward 非常接近）。这意味着 \"balancing\" 叙事与最优解不一致——最优策略实际上是几乎完全依赖 diversity。\n- 为什么影响接收：RASP 是论文的主要方法贡献。如果最优解是 CKA-dominant，那么 RASP 作为一个 parametric family 的贡献就退化为 \"在 CKA-only 基础上加了一个几乎不起作用的 importance 项\"，方法新颖性大打折扣。\n- 建议修改方向：(1) 诚实地将 RASP 重新 frame 为一个 interpolation family，并强调 dose-response 分析本身是贡献（揭示 diversity >> importance 的不对称性），而非 \"balancing\"；(2) 讨论为什么 importance 在 CKA overlap 存在时变得冗余。\n\n**N3** [Critical] **有效剪枝窗口仅 20–25%，30% 全面崩塌——实用价值严重受限但论文 framing 不够坦诚**\n- 具体位置：Section 4.1（\"All methods collapse at 30% sparsity\"），Appendix K（Table 10）\n- 问题：论文在 abstract 中使用 \"moderate sparsity\" 一词，但实际有效窗口仅为 20–25% MLP channel sparsity（Appendix K: 30% 时 accuracy 降至 4–5%，EOS rate < 6%）。对于一个 7B 模型，20–25% MLP 通道剪枝 仅约去除整体参数的约 12-15%（因为 attention 层未被剪枝），实际压缩效果非常有限。Appendix C 报告推理延迟仅减少 18%。在模型压缩文献中，这个操作范围过窄，难以证明方法的实用价值。\n- 论文处理方式：30% collapse 被放在 Appendix K 中，主文仅在 Section 4.1 一句话提及。Abstract 和 Introduction 均未明确限定有效窗口的上限。\n- 为什么影响接收：如果一个关于 \"pruning criteria\" 的研究只在非常窄的窗口内有效，读者需要在最前面就了解这个限制。将其弱化为 \"moderate sparsity\" 并将 collapse 分析放到 appendix，构成 framing 上的不坦诚。\n- 建议修改方向：(1) Abstract 和 Introduction 中明确写出 \"20–25% MLP channel sparsity (approximately 12–15% total parameter reduction)\"；(2) 将 30% collapse 分析从 Appendix K 提升到主文 Discussion 中；(3) 讨论为什么结构化剪枝在 reasoning LLM 上的耐受度如此低，这本身可以是一个有价值的发现。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [Warning] **Title 和叙事聚焦 RLVR/GRPO，但主要发现是 SFT dominates——存在 framing 错位**\n- 具体位置：Title, Abstract, Contribution 3\n- 问题：Title 为 \"How Pruning Criteria Shape Post-RLVR Recovery\"，叙事围绕 RLVR 展开。但 Contribution 3 明确指出 \"SFT warmup as the dominant recovery mechanism\"，Section 4.3 承认 GRPO 仅增加 |Δ|≤1pp。如果 SFT 才是 dominant mechanism，为什么论文不是关于 \"How Pruning Criteria Shape Post-SFT Recovery\"？GRPO 在这里更像是一个 afterthought 而非核心。\n- 建议：要么 (a) 重新组织叙事，将 \"SFT dominates, GRPO serves only as diagnostic\" 作为核心 takeaway 而非第三贡献；要么 (b) 提供证据说明在何种条件下 GRPO 贡献是实质性的（如更高剪枝率、不同 reward signal）。\n\n**W2** [Warning] **Ji et al. (2025, Self-Healing) 对比设置差异过大，论文的 \"advantage vanishes\" claim 过强**\n- 具体位置：Section 2 (Related Work), Abstract 第 2-3 句\n- 问题：Abstract 声称 \"this advantage vanishes under fine-grained structured pruning\"，暗示推翻了 Ji et al. 的发现。但两者设置差异巨大：Ji et al. 研究的是 unstructured pruning at 96.5% retention（仅移除 3.5% 权重），本文研究 structured MLP channel pruning at 75–80% retention（移除 20–25%）。Unstructured vs. structured 是根本不同的剪枝范式，直接对比并声称 \"vanishes\" 是 overclaiming。\n- 建议：(1) 弱化措辞为 \"does not straightforwardly extend to structured pruning\"；(2) 在 Related Work 中更明确地讨论两种范式差异对恢复的影响。\n\n**W3** [Warning] **单一架构族（Qwen2.5）且 Title 暗示泛化性**\n- 具体位置：Title (\"a Reasoning LLM\"), Limitations (page 9)\n- 问题：所有实验模型均基于 Qwen2.5 架构——主模型 DeepSeek-R1-Distill-Qwen-7B（Qwen2.5-7B 蒸馏版）、验证模型 DeepSeek-R1-Distill-Qwen-1.5B 和 Qwen2.5-Math-7B。Title 中 \"a Reasoning LLM\" 在技术上正确（指主模型），但给读者的印象是结论对 reasoning LLM 普遍成立。Limitations section 承认了这一点，但未讨论为什么选择了同一架构族的三个变体而非跨架构验证（如 LLaMA-based reasoning models）。\n- 建议：Title 改为 \"...in Qwen2.5-Family Reasoning Models\" 或在 abstract 中更早明确架构限制。\n\n**W4** [Warning] **Qwen2.5-Math-7B 的 GRPO 验证缺失**\n- 具体位置：Appendix O, 脚注（page 15）\n- 问题：Qwen2.5-Math-7B 仅有 SFT 阶段验证。脚注提到 \"Preliminary GRPO evaluations: 48.60% (2/4500), but 83.8% of responses were truncated at 2048 tokens\"。83.8% truncation rate 意味着 GRPO 结果完全不可靠。对于声称 \"recovery capacity spectrum generalizes across models\" 的论文，在一个验证模型上缺少完整的两阶段验证是显著空白。\n- 建议：要么 (a) 完成 GRPO 验证（增加 max generation length）；要么 (b) 明确将 Qwen2.5-Math-7B 的结论限制在 SFT 阶段，并在 Limitations 中讨论。\n\n**W5** [Warning] **Discussion 被放在 Appendix U 而非主文——削弱了论文的完整性**\n- 具体位置：Section 5 (Conclusion, page 8), Appendix U (page 16)\n- 问题：Section 5 仅有 ~15 行的 conclusion，没有独立的 Discussion section。关于 implications for deployment pipelines 和 GRPO diagnostics 的讨论被放在 Appendix U。对于一篇以 empirical findings 为核心的论文，Discussion 是读者理解 findings 意义的关键部分，不应放在 appendix 中。\n- 建议：将 Appendix U 的核心内容（至少 \"Implications\" 段落）移回主文，可以压缩其他部分（如 Section 4.5 的 representational diversity evidence 部分细节可以移到 appendix）。\n\n**W6** [Warning] **Recovery capacity spectrum 的实用价值不清晰**\n- 具体位置：Section 4.2, Table 1\n- 问题：论文定义了 recovery capacity 作为 GRPO 训练中的 max batch-mean reward（Section 3.5），并据此建立了方法排序（CKA-only > Random > Standard > RASP(α→1)）。但 Table 1 显示 post-SFT+GRPO 的最终 accuracy 差异很小（CKA-only 64.39% vs Standard 59.84%, 主要差异来自 SFT 阶段）。如果最终 accuracy 差异可以通过 post-SFT accuracy 直接观察到，recovery capacity spectrum 作为 GRPO-based diagnostic 的附加价值何在？论文未论证在什么场景下 GRPO probe 比直接评估 post-SFT accuracy 更有信息量。\n- 建议：给出一个 GRPO diagnostic 比 SFT accuracy 更有价值的具体场景（如 GRPO 能揭示 SFT accuracy 无法区分的结构差异），或弱化此 claim。\n\n---\n\n## 小问题（不影响接收）\n\n**M1** [Minor] **概念前向引用**：recovery capacity 在 Section 1（Contribution 2）中使用，但直到 Section 3.5 才正式定义。\"Reward-accuracy decoupling\" 在 Introduction 出现但 Section 4.3 才解释。建议在 Introduction 首次使用时给出简短定义。\n\n**M2** [Minor] **\"dose-response\" 术语借用**：该术语源自药理学/毒理学，在 ML 文献中不常见。Section 4.4 使用但未解释其隐喻意义。对不熟悉该术语的读者可能造成困惑。\n\n**M3** [Minor] **Figure 4 scatter plot 可读性差**：四个子图中的颜色/符号区分度不够，尤其在灰度打印时。建议使用不同形状标记。\n\n**M4** [Minor] **Limitations 遗漏了 MLP-only 限制**：Limitations section 提到了单一架构族和有限 benchmark，但未提及实验仅覆盖 MLP channel pruning 而未包含 attention head pruning。鉴于 attention head pruning 在结构化剪枝文献中同等重要，这应被列为 limitation。\n\n**M5** [Minor] **Figure 1 在 abstract 之前引用**：Page 1 的 Introduction 在 abstract 之后立即引用 Figure 1（\"the dose-response curve (Figure 1)\"），但这个 figure 的上下文在 Section 4.4 才充分展开，对首次阅读的读者来说跳跃较大。\n\n---\n\n## Questions（需要作者回答）\n\n**Q1**: 如果将 SFT warmup 从 2 epochs 减少到 0.5 epochs，使得 post-SFT accuracy 显著低于当前水平，GRPO 阶段是否会产生更大的 accuracy gain？如果是，\"reward-accuracy decoupling\" 是否只是 SFT 充分恢复后的天花板效应？\n\n**Q2**: RASP(α=2.0) 和 CKA-only 的实际剪枝决策在多大程度上重叠？即在 20% sparsity 下，两者移除的 MLP channel groups 有多少比例相同？如果重叠度很高（>80%），RASP 的独立方法贡献就非常有限。\n\n**Q3**: 论文声称 GRPO 可以作为 \"diagnostic probe\"（~100 步即可），但 Table 1 中 post-SFT accuracy 已经能区分不同剪枝标准的恢复质量（CKA-only 64.39% vs Standard 59.84%）。在什么具体场景下，~100 步 GRPO probe 比直接评估 post-SFT accuracy 更有诊断价值？\n\n**Q4**: 30% sparsity 下所有方法崩塌，accuracy 降至 4–5%（Appendix K）。是否尝试过在 25%–30% 之间更细粒度的 sparsity level（如 26%, 27%, 28%）来找到确切的 cliff 位置？这对理解为什么结构化剪枝在 reasoning model 上如此脆弱很有价值。\n\n**Q5**: Extended GRPO training（Appendix E, 300 步）仍然没有改变 ordering 或打破 decoupling。是否考虑过训练更长（如 1000–3000 步，接近文献中常见的 RLVR 训练预算）？\n\n---\n\n## Missing References / 引用讨论不足\n\n**R1**: **Zhang et al. (2025, arXiv:2504.02010) \"When Reasoning Meets Compression\"** — 已出现在参考文献中，但在 Related Work 主文中仅作为 bundled citation 出现，未被单独讨论。该文研究了量化、蒸馏和剪枝对 reasoning LLM 的影响，直接相关——应在 Related Work 中讨论其发现与本文的异同（特别是他们发现的 compression 对不同 reasoning 能力的差异化影响）。\n\n**R2**: **Zhao et al. (2025, arXiv:2505.14582) \"Can Pruning Improve Reasoning?\"** — 已引用，但应在 Related Work 中明确区分：该文研究的是 reasoning trace pruning（Long-CoT token-level），而本文研究的是 model structure pruning。两者使用相同的 \"pruning\" 术语但含义完全不同，需要明确讨论以避免读者混淆。\n\n**R3**: **Mukherjee et al. (2025, arXiv:2505.11711) \"Reinforcement Learning Finetunes Small Subnetworks\"** — 已引用并在 Related Work 中简要讨论。但该文发现 RL 只更新 5–30% 参数的 subnetwork——这与本文 GRPO 阶段 accuracy 增益极小的发现高度相关。建议在 Discussion 中更深入连接：如果 GRPO 只更新一个小 subnetwork，而结构化剪枝可能恰好破坏了该 subnetwork 的关键部分，这是否解释了 criterion-dependent 的 reward 差异？\n\n---\n\n## Overall Assessment\n\n**评分：3.0 / 5 — Findings**\n\n**理由**：这是一篇实验设计严谨、统计方法规范的实证研究，控制变量范式值得肯定。但存在三个核心问题削弱了其主会议接收的竞争力：\n\n1. **新颖性不足**：最核心的 \"reward-accuracy decoupling\" 发现很可能是 SFT 天花板效应的 artifact，而非独立的科学发现。RASP 的方法贡献被 α=2.0 (CKA-dominant) 最优解所 undermined。\n\n2. **Framing 问题**：论文围绕 RLVR/GRPO 组织叙事，但实际主要发现是 SFT 才是 dominant recovery mechanism。Title 和 narrative 的焦点与实际发现不匹配。\n\n3. **实用性受限**：有效窗口仅 20–25% MLP sparsity（~12–15% 总参数压缩），30% 即全面崩塌。这个操作范围过窄，限制了方法的实际应用价值。\n\n如果作者能 (a) 通过消融实验排除天花板效应作为 decoupling 的解释，(b) 诚实地重新 frame RASP 和叙事焦点，(c) 将有效窗口的局限性上提到主文——论文有潜力达到 3.5（Borderline Conference）。当前状态更适合 Findings track。\n",
    "reviewer_id": "2",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 715 · 2026-05-25T21:22:45.621465+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3714
}
```

</details>

---


### Tool call

_source line 716 · 2026-05-25T21:22:49.997015+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 717 · 2026-05-25T21:22:49.997466+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 718 · 2026-05-25T21:22:55.163772+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 719 · 2026-05-25T21:22:55.264562+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 17, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/review_round_9/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 100
}
```

</details>

---


### Assistant

_source line 720 · 2026-05-25T21:23:15.083510+00:00_

审稿意见已提交给 Review Director。

**评分：Overall 3.0/5（Findings）**，三个 Critical 问题：

1. **Reward-accuracy decoupling 可能是 SFT 天花板效应的 artifact**——SFT 已恢复大部分 accuracy，GRPO 无 headroom，需要消融实验排除
2. **RASP 最优 α=2.0 本质是 CKA-dominant**——undermines "balancing importance and diversity" 的叙事，方法新颖性打折扣
3. **有效窗口仅 20–25% MLP sparsity，30% 全面崩塌**——Abstract 用 "moderate sparsity" 模糊处理，实际压缩比约 12–15%，实用价值受限

另有 6 个 Warning（Title/叙事与 SFT-dominant 发现的错位、Ji et al. 对比 overclaiming、单一架构族、Math-7B GRPO 缺失、Discussion 被放 Appendix、spectrum 实用价值不清）和 5 个 Minor 问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2"
}
```

</details>

---


## Round 18

## Round 18

4 recorded events


### User

_source line 721 · 2026-05-25T21:25:48.518974+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的审稿意见，对每个点标注 `[AGREE]` 或 `[REBUT]`（附理由）。

---

**Reviewer 1 评分：Overall 3.0/5（Findings）**

### Critical 问题

**N1**: RASP 作为方法贡献被自身消融否定——CKA-only（α→∞ 极限）在 recovery capacity spectrum 排第一（Peak Rew 0.354），RASP 默认 α=1.0 reward collapse（Peak Rew 0.061）。论文最终推荐 CKA-only 而非 RASP，方法贡献不成立。

**N2**: 乘法形式 I(h)=0 退化行为未与加法替代对比——I(h)=0⟹S=0 是 RASP 败给 CKA-only 的原因，加法形式不存在此退化。缺少加法对照无法区分乘法 artifact 与 tradeoff 本质。

**N3**: Random baseline max_completion_length 不一致违反受控实验设计——Random GRPO 用 512 vs 其他 1024，论文自称 "hold everything else constant" 但此处不一致。

**N4**: RASP α 变体全部单 seed，dose-response 曲线不可靠——α=2.0 的 66.11% vs CKA-only 64.39±0.19% 的 1.72pp 差距在方差未知时不可信。

### Warning 问题

**W1**: TOST ε=2pp 缺乏 a priori justification
**W2**: 15% sparsity 下 GRPO 放大 CKA 优势（+1.51pp），Standard Δ=-0.93pp 接近 1pp 边界
**W3**: 25% sparsity 单 seed，Standard Δ=+0.99pp 恰在 1pp 边界
**W4**: 300-step extended training 未报告 step-by-step accuracy 曲线
**W5**: Limitations 关于 Random seed 的表述与正文矛盾
**W6**: Calibration M=512 importance score 稳定性未验证

### Questions

Q1: α=1.0 collapse 是乘法 I(h)≈0 退化还是 diversity-importance 平衡失败？
Q2: 为什么不统一 Random 的 max_completion_length 为 1024？
Q3: 如果 α=2.0 补跑 3 seeds 仍优于 CKA-only，结论是否需根本性修改？

---

请对 N1-N4 和 W1-W6 逐条给出 [AGREE] 或 [REBUT]，重点关注：
1. N1/N2 与你的 C2（α=2.0 本质 CKA-dominant）是否指向同一根本问题
2. N3 的控制变量问题对你的 spectrum 有效窗口判断有无影响
3. N4 的单 seed 问题是否加剧了你对方法新颖性的质疑

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-25T21:27:12.752554+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 交叉回应：逐条回应 Reviewer 1 的审稿意见\n\n---\n\n## Critical 问题\n\n**[AGREE] R1-N1: RASP 方法贡献被自身消融否定**\n\n同意，且与我的 N2 指向同一根本问题。我的 N2 从 \"α=2.0 最优意味着 CKA-dominant，undermines balancing 叙事\" 角度论述，R1-N1 从 \"论文最终推荐 CKA-only 而非 RASP\" 角度论述——本质一致：RASP 作为独立方法贡献不成立。\n\n补充一点 R1 未提及的：Table 1 数据显示 RASP(α=2.0) Peak Rew = 0.354，CKA-only Peak Rew = 0.354，两者完全相同。这比 R1 的论证更直接——在最优配置下 RASP 与 CKA-only 的 recovery capacity 指标无差异，RASP 框架的额外 parametric 复杂性没有带来任何增益。如果作者声称 α=2.0 时 accuracy (66.11%) 优于 CKA-only (64.39%)，这个 1.72pp 差异恰好落在 R1-N4 指出的单 seed 不可信区间内。\n\n**[AGREE] R1-N2: 乘法形式退化行为未与加法替代对比**\n\n同意，这是一个我未覆盖的有价值技术点。RASP 的乘法形式 $S_{RASP}(h) = I(h) \\times (1-F(h))^\\alpha$（Eq. 5）意味着 $I(h)=0$ 的结构无论 diversity 多高都被零化。加法替代（如 $S = \\beta \\cdot I(h) + (1-\\beta) \\cdot (1-F(h))$）不存在此退化，是合理的 ablation 对照。缺少这个对照，无法判断 α=1.0 collapse（Table 1, Peak Rew 0.061）是乘法形式的 pathological artifact 还是 importance-diversity tradeoff 在该配置下的真实行为。这一遗漏与我的 N2 构成互补——我关注 α=2.0 端（CKA-dominant），R1 关注 α=1.0 端（collapse），合在一起说明 RASP 的整个 parametric 空间都有问题：一端退化，另一端等价于 CKA-only。\n\n**[AGREE with nuance] R1-N3: Random baseline max_completion_length 不一致**\n\n同意这违反了受控实验设计原则，论文自称 \"hold everything else constant\"（Section 3）但此处不一致。但我对严重程度的评估略低于 R1：\n\n- Random 是四种方法中最弱的 baseline，用于 \"控制 informative scoring 的效应\"\n- max_completion_length 512 vs 1024 可能导致 Random 的 GRPO reward 被低估（因为 reasoning trace 更容易截断），但 Random 在 recovery capacity spectrum 中已经排在 Standard 之上（Peak Rew 0.125 vs 0.060, Table 1），如果统一到 1024 可能进一步拉大这个差距\n- 关键影响：如果 Random 在 1024 设置下 accuracy 和 reward 都更高，那 Standard（唯一一个低于 Random 的 informative method）的表现就更显尴尬，这反而强化了论文关于 \"importance-only 不如 diversity-preserving\" 的结论\n\n所以不一致是真实问题，应报告并修复，但不太可能翻转核心 spectrum ordering。对我的有效窗口判断（N3）无直接影响——30% collapse 是所有方法共享的架构限制，与 Random 的超参数无关。\n\n**[AGREE] R1-N4: RASP α 变体全部单 seed，dose-response 曲线不可靠**\n\n强烈同意，且与我的 N2 直接相关。我的 N2 指出 \"α=2.0 CKA-dominant undermines balancing narrative\"，R1-N4 进一步指出这个 α=2.0 的优势本身在统计上就不可信。两个问题叠加：\n\n1. (我的 N2) 即使 α=2.0 真的更好，它也只是 CKA-only 的近似\n2. (R1-N4) α=2.0 是否真的更好，在单 seed 下无法确认\n\nAppendix J 报告 CKA-only 的 3-seed 标准差为 0.19pp（Section 4.5）。α=2.0 的 66.11% vs CKA-only 64.39% 差距为 1.72pp，看似显著，但 α=2.0 自身方差未知。如果 α=2.0 的标准差与 CKA-only 相当（~0.19pp），则 1.72pp 可能显著；但如果 α=2.0 方差更大（考虑到 RASP 在不同 α 下表现差异巨大——从 collapse 到 66%——variance 可能更高），则 1.72pp 不可信。\n\n这加剧了我对方法新颖性的质疑：RASP 不仅在最优配置下等价于 CKA-only（我的 N2），而且连 \"是否真的优于 CKA-only\" 这个前提都未被统计验证（R1-N4）。\n\n---\n\n## Warning 问题\n\n**[AGREE] R1-W1: TOST ε=2pp 缺乏 a priori justification**\n\n同意。TOST 的 equivalence margin 是结论成立与否的关键参数。ε=2pp 对于 GSM8K（~1300 题，准确率 60-65%）意味着约 26 题的差异，这在教育评测中算实质性差异还是噪音？论文选择 2pp 但未引用文献或给出统计 power 分析来证明这个选择。如果 ε=1pp，部分 \"等价\" 结论可能不成立。\n\n**[AGREE] R1-W2: 15% sparsity 下 CKA-only 优势被 GRPO 放大**\n\n同意这削弱了 \"SFT+GRPO 抹平差异\" 的叙事。Appendix M 的 15% 数据（CKA-only vs Standard: +1.51pp post-GRPO，而 post-SFT 差距更小）表明 GRPO 在低剪枝率下并非纯粹的 diagnostic——它可以放大方法间差异。这与我的 N1（decoupling 可能是天花板效应）一致：在 15% sparsity 下 accuracy headroom 更大，GRPO 开始产生实质性差异，进一步暗示 20% 下的 \"decoupling\" 是 headroom 耗尽的 artifact。\n\n**[REBUT] R1-W3: 25% sparsity 单 seed，Standard Δ=+0.99pp 恰在 1pp 边界**\n\n部分反驳。R1 的担忧合理——单 seed 下 0.99pp 恰在边界确实不够稳健。但这个数据点不是论文核心 claim 的支撑：25% sparsity 主要作为 \"collapse 前的边界条件\" 出现（Section 4.1, \"All methods collapse at 30%\"），而非核心 spectrum 分析的基础。论文的核心 spectrum 结论建立在 20% sparsity 数据上（Table 1, 3 seeds for CKA-only/Standard/Random）。25% 数据的不确定性是真实问题，但严重程度低于 R1 隐含的判断。\n\n**[AGREE] R1-W4: 300-step extended training 未报告 step-by-step accuracy 曲线**\n\n同意。Appendix E 只报告了 100 步和 300 步的 checkpoint accuracy，但没有中间步骤的 accuracy trajectory。这是一个遗漏——如果 CKA-only 在 150-200 步时 accuracy 仍在上升，而 Standard 在 100 步后就 plateau 了，这将是非常有信息量的。更重要的是，300 步仍然远少于 RLVR 文献中常见的训练预算（通常 1000-5000 步），这与我的 Q5 一致。\n\n**[AGREE] R1-W5: Limitations 关于 Random seed 的表述与正文矛盾**\n\n同意这是写作问题。如果 Limitations 说 \"RASP α variants and Random use single GRPO seeds\" 但 Appendix L (Table 11) 显示 Random 有 3 seeds（42, 123, 456），则存在矛盾。这类不一致会降低审稿人对其他声称的信任度。\n\n**[REBUT] R1-W6: Calibration M=512 importance score 稳定性未验证**\n\n部分反驳。R1 关心 M=512 样本量是否足够计算稳定的 importance score。但 Appendix H（Table 8）报告了 CKA scoring 在不同 calibration set sizes（256/512/1024）下的 Spearman ρ 稳定性（ρ=0.964-0.979），虽然这只验证了 CKA ranking 的稳定性而非 importance score 的稳定性，但暗示 512 样本量对 structure ranking 的计算已经足够稳定。更直接的反驳：importance score 基于 Taylor expansion（一阶梯度×激活），这在剪枝文献中是标准做法，M=512 远超 LLM-Pruner（Ma et al., 2023）使用的 calibration 规模。\n\n---\n\n## 综合评估\n\nR1 的审稿意见整体高质量，与我的评审高度互补：\n\n| 问题域 | R1 视角 | R2 视角 | 关系 |\n|--------|---------|---------|------|\n| RASP 贡献 | N1: 推荐 CKA-only 否定 RASP | N2: α=2.0 CKA-dominant 否定 balancing | 同一问题的两面 |\n| 乘法退化 | N2: 缺加法对照 | 未覆盖 | R1 独有贡献 |\n| 实验控制 | N3: Random 超参不一致 | 未覆盖 | R1 独有贡献 |\n| 统计可靠性 | N4: α 变体单 seed | Q2: RASP vs CKA-only 重叠度 | 互补 |\n| Decoupling 本质 | 未深入讨论 | N1: SFT 天花板效应 | R2 独有贡献 |\n| 有效窗口 | 未直接讨论 | N3: 20-25% 过窄 | R2 独有贡献 |\n| Framing 错位 | 未直接讨论 | W1: Title vs 实际发现 | R2 独有贡献 |\n\n两份审稿合在一起对 RASP 方法贡献形成了全面否定：从 α→0（Standard 退化）到 α=1.0（乘法 collapse）到 α=2.0（CKA-only 等价且单 seed 不可信）到 α→∞（CKA-only 本身）。RASP 作为 parametric family 在整个参数空间都不优于其端点。\n\n我维持 Overall 3.0（Findings）评分。R1 的技术细节问题（N2 乘法 vs 加法、N3 超参不一致）加强了我对方法贡献不足的判断，但未改变总体评估——论文的控制变量实验设计和实证发现（尤其 SFT dominance 和 criterion-dependent training dynamics）仍然有 Findings 级别的价值。\n",
  "reviewer_id": "2",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 交叉回应：逐条回应 Reviewer 1 的审稿意见\n\n---\n\n## Critical 问题\n\n**[AGREE] R1-N1: RASP 方法贡献被自身消融否定**\n\n同意，且与我的 N2 指向同一根本问题。我的 N2 从 \"α=2.0 最优意味着 CKA-dominant，undermines balancing 叙事\" 角度论述，R1-N1 从 \"论文最终推荐 CKA-only 而非 RASP\" 角度论述——本质一致：RASP 作为独立方法贡献不成立。\n\n补充一点 R1 未提及的：Table 1 数据显示 RASP(α=2.0) Peak Rew = 0.354，CKA-only Peak Rew = 0.354，两者完全相同。这比 R1 的论证更直接——在最优配置下 RASP 与 CKA-only 的 recovery capacity 指标无差异，RASP 框架的额外 parametric 复杂性没有带来任何增益。如果作者声称 α=2.0 时 accuracy (66.11%) 优于 CKA-only (64.39%)，这个 1.72pp 差异恰好落在 R1-N4 指出的单 seed 不可信区间内。\n\n**[AGREE] R1-N2: 乘法形式退化行为未与加法替代对比**\n\n同意，这是一个我未覆盖的有价值技术点。RASP 的乘法形式 $S_{RASP}(h) = I(h) \\times (1-F(h))^\\alpha$（Eq. 5）意味着 $I(h)=0$ 的结构无论 diversity 多高都被零化。加法替代（如 $S = \\beta \\cdot I(h) + (1-\\beta) \\cdot (1-F(h))$）不存在此退化，是合理的 ablation 对照。缺少这个对照，无法判断 α=1.0 collapse（Table 1, Peak Rew 0.061）是乘法形式的 pathological artifact 还是 importance-diversity tradeoff 在该配置下的真实行为。这一遗漏与我的 N2 构成互补——我关注 α=2.0 端（CKA-dominant），R1 关注 α=1.0 端（collapse），合在一起说明 RASP 的整个 parametric 空间都有问题：一端退化，另一端等价于 CKA-only。\n\n**[AGREE with nuance] R1-N3: Random baseline max_completion_length 不一致**\n\n同意这违反了受控实验设计原则，论文自称 \"hold everything else constant\"（Section 3）但此处不一致。但我对严重程度的评估略低于 R1：\n\n- Random 是四种方法中最弱的 baseline，用于 \"控制 informative scoring 的效应\"\n- max_completion_length 512 vs 1024 可能导致 Random 的 GRPO reward 被低估（因为 reasoning trace 更容易截断），但 Random 在 recovery capacity spectrum 中已经排在 Standard 之上（Peak Rew 0.125 vs 0.060, Table 1），如果统一到 1024 可能进一步拉大这个差距\n- 关键影响：如果 Random 在 1024 设置下 accuracy 和 reward 都更高，那 Standard（唯一一个低于 Random 的 informative method）的表现就更显尴尬，这反而强化了论文关于 \"importance-only 不如 diversity-preserving\" 的结论\n\n所以不一致是真实问题，应报告并修复，但不太可能翻转核心 spectrum ordering。对我的有效窗口判断（N3）无直接影响——30% collapse 是所有方法共享的架构限制，与 Random 的超参数无关。\n\n**[AGREE] R1-N4: RASP α 变体全部单 seed，dose-response 曲线不可靠**\n\n强烈同意，且与我的 N2 直接相关。我的 N2 指出 \"α=2.0 CKA-dominant undermines balancing narrative\"，R1-N4 进一步指出这个 α=2.0 的优势本身在统计上就不可信。两个问题叠加：\n\n1. (我的 N2) 即使 α=2.0 真的更好，它也只是 CKA-only 的近似\n2. (R1-N4) α=2.0 是否真的更好，在单 seed 下无法确认\n\nAppendix J 报告 CKA-only 的 3-seed 标准差为 0.19pp（Section 4.5）。α=2.0 的 66.11% vs CKA-only 64.39% 差距为 1.72pp，看似显著，但 α=2.0 自身方差未知。如果 α=2.0 的标准差与 CKA-only 相当（~0.19pp），则 1.72pp 可能显著；但如果 α=2.0 方差更大（考虑到 RASP 在不同 α 下表现差异巨大——从 collapse 到 66%——variance 可能更高），则 1.72pp 不可信。\n\n这加剧了我对方法新颖性的质疑：RASP 不仅在最优配置下等价于 CKA-only（我的 N2），而且连 \"是否真的优于 CKA-only\" 这个前提都未被统计验证（R1-N4）。\n\n---\n\n## Warning 问题\n\n**[AGREE] R1-W1: TOST ε=2pp 缺乏 a priori justification**\n\n同意。TOST 的 equivalence margin 是结论成立与否的关键参数。ε=2pp 对于 GSM8K（~1300 题，准确率 60-65%）意味着约 26 题的差异，这在教育评测中算实质性差异还是噪音？论文选择 2pp 但未引用文献或给出统计 power 分析来证明这个选择。如果 ε=1pp，部分 \"等价\" 结论可能不成立。\n\n**[AGREE] R1-W2: 15% sparsity 下 CKA-only 优势被 GRPO 放大**\n\n同意这削弱了 \"SFT+GRPO 抹平差异\" 的叙事。Appendix M 的 15% 数据（CKA-only vs Standard: +1.51pp post-GRPO，而 post-SFT 差距更小）表明 GRPO 在低剪枝率下并非纯粹的 diagnostic——它可以放大方法间差异。这与我的 N1（decoupling 可能是天花板效应）一致：在 15% sparsity 下 accuracy headroom 更大，GRPO 开始产生实质性差异，进一步暗示 20% 下的 \"decoupling\" 是 headroom 耗尽的 artifact。\n\n**[REBUT] R1-W3: 25% sparsity 单 seed，Standard Δ=+0.99pp 恰在 1pp 边界**\n\n部分反驳。R1 的担忧合理——单 seed 下 0.99pp 恰在边界确实不够稳健。但这个数据点不是论文核心 claim 的支撑：25% sparsity 主要作为 \"collapse 前的边界条件\" 出现（Section 4.1, \"All methods collapse at 30%\"），而非核心 spectrum 分析的基础。论文的核心 spectrum 结论建立在 20% sparsity 数据上（Table 1, 3 seeds for CKA-only/Standard/Random）。25% 数据的不确定性是真实问题，但严重程度低于 R1 隐含的判断。\n\n**[AGREE] R1-W4: 300-step extended training 未报告 step-by-step accuracy 曲线**\n\n同意。Appendix E 只报告了 100 步和 300 步的 checkpoint accuracy，但没有中间步骤的 accuracy trajectory。这是一个遗漏——如果 CKA-only 在 150-200 步时 accuracy 仍在上升，而 Standard 在 100 步后就 plateau 了，这将是非常有信息量的。更重要的是，300 步仍然远少于 RLVR 文献中常见的训练预算（通常 1000-5000 步），这与我的 Q5 一致。\n\n**[AGREE] R1-W5: Limitations 关于 Random seed 的表述与正文矛盾**\n\n同意这是写作问题。如果 Limitations 说 \"RASP α variants and Random use single GRPO seeds\" 但 Appendix L (Table 11) 显示 Random 有 3 seeds（42, 123, 456），则存在矛盾。这类不一致会降低审稿人对其他声称的信任度。\n\n**[REBUT] R1-W6: Calibration M=512 importance score 稳定性未验证**\n\n部分反驳。R1 关心 M=512 样本量是否足够计算稳定的 importance score。但 Appendix H（Table 8）报告了 CKA scoring 在不同 calibration set sizes（256/512/1024）下的 Spearman ρ 稳定性（ρ=0.964-0.979），虽然这只验证了 CKA ranking 的稳定性而非 importance score 的稳定性，但暗示 512 样本量对 structure ranking 的计算已经足够稳定。更直接的反驳：importance score 基于 Taylor expansion（一阶梯度×激活），这在剪枝文献中是标准做法，M=512 远超 LLM-Pruner（Ma et al., 2023）使用的 calibration 规模。\n\n---\n\n## 综合评估\n\nR1 的审稿意见整体高质量，与我的评审高度互补：\n\n| 问题域 | R1 视角 | R2 视角 | 关系 |\n|--------|---------|---------|------|\n| RASP 贡献 | N1: 推荐 CKA-only 否定 RASP | N2: α=2.0 CKA-dominant 否定 balancing | 同一问题的两面 |\n| 乘法退化 | N2: 缺加法对照 | 未覆盖 | R1 独有贡献 |\n| 实验控制 | N3: Random 超参不一致 | 未覆盖 | R1 独有贡献 |\n| 统计可靠性 | N4: α 变体单 seed | Q2: RASP vs CKA-only 重叠度 | 互补 |\n| Decoupling 本质 | 未深入讨论 | N1: SFT 天花板效应 | R2 独有贡献 |\n| 有效窗口 | 未直接讨论 | N3: 20-25% 过窄 | R2 独有贡献 |\n| Framing 错位 | 未直接讨论 | W1: Title vs 实际发现 | R2 独有贡献 |\n\n两份审稿合在一起对 RASP 方法贡献形成了全面否定：从 α→0（Standard 退化）到 α=1.0（乘法 collapse）到 α=2.0（CKA-only 等价且单 seed 不可信）到 α→∞（CKA-only 本身）。RASP 作为 parametric family 在整个参数空间都不优于其端点。\n\n我维持 Overall 3.0（Findings）评分。R1 的技术细节问题（N2 乘法 vs 加法、N3 超参不一致）加强了我对方法贡献不足的判断，但未改变总体评估——论文的控制变量实验设计和实证发现（尤其 SFT dominance 和 criterion-dependent training dynamics）仍然有 Findings 级别的价值。\n",
    "reviewer_id": "2",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---


### Tool result

_source line 723 · 2026-05-25T21:27:16.265457+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_40839c097b00df44480b45ab767f59cf:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3512
}
```

</details>

---


### Assistant

_source line 724 · 2026-05-25T21:27:26.193617+00:00_

交叉回应已提交。逐条回应了 R1 的 N1-N4 和 W1-W6：

- **N1/N2/N4**：全部 AGREE，与我的 N2 形成互补——R1 从 "论文推荐 CKA-only 否定 RASP" 和 "乘法退化" 角度，我从 "α=2.0 CKA-dominant" 角度，共同否定 RASP 的方法贡献
- **N3**（Random 超参不一致）：AGREE with nuance——违反控制原则但不太可能翻转 spectrum ordering
- **W3**：REBUT——25% 单 seed 问题真实但非核心 claim 支撑
- **W6**：REBUT——Appendix H 的 CKA 稳定性数据和 Taylor expansion 文献标准提供了间接支持

维持 Overall 3.0（Findings）不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_40839c097b00df44480b45ab767f59cf:reviewer_2"
}
```

</details>

---
