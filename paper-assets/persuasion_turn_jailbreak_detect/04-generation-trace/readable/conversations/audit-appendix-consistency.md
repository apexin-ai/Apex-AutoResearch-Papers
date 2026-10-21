# audit appendix consistency

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_audit_appendix-consistency_20260523T191656.jsonl`
- **Structured JSON:** [`d05b208a63341733ec06.json`](../../sessions/d0/d05b208a63341733ec06.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

53 recorded events

### Tool call

_source line 1 · 2026-05-23T19:24:29.845865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T19:24:29.846705+00:00_

1	% appendix.tex — Supplementary material
2	
3	\appendix
4	
5	\section{LLM-as-Judge Baseline}
6	\label{sec:llm_judge}
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{LLM-as-judge jailbreak detection. IID: binary F1 (Crescendo test set); OOD: macro F1 (DD = Deceptive Delight, AA = ActorAttack). GPT-5.5 F1 values exclude unparseable responses and represent upper bounds.}
12	\label{tab:llm_judge}
13	\begin{tabular}{@{}lcccr@{}}
14	\toprule
15	\textbf{Method} & DD & AA & IID & Unparse. \\
16	\midrule
17	\multicolumn{5}{l}{\textit{Zero-shot}} \\[2pt]
18	GPT-5.5 & -- & -- & .383 & 30--47\% \\
19	Qwen3-8B & .244 & .244 & .100 & 0\% \\
20	\midrule
21	\multicolumn{5}{l}{\textit{3-shot}} \\[2pt]
22	Qwen3-8B & .566 & .652 & -- & 0\% \\
23	\midrule
24	\multicolumn{5}{l}{\textit{Trained classifier}} \\[2pt]
25	9-class (ours) & \textbf{.994} & \textbf{.972} & \textbf{1.000} & 0\% \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:llm_judge} reports LLM-as-judge performance on IID and OOD data.
31	On IID Crescendo, GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 = 0.383 on full conversations; 30--47\% of responses are unparseable.
32	Qwen3-8B performs worse (IID F1 = 0.100).
33	On OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 on both DD and ActorAttack by predicting nearly all conversations as benign.
34	Even with 3-shot prompting, Qwen3-8B reaches only 0.566 (DD) and 0.652 (AA), while DisPeD maintains macro F1 $\geq$ 0.972.
35	The poor performance of content-level reasoning on unseen attack families underscores the necessity of trained classifiers with domain-adapted representations.
36	
37	\section{Full Cross-Attack Results by Prefix}
38	\label{sec:full_prefix}
39	
40	\begin{table*}[t]
41	\centering
42	\small
43	\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\pm$std where available. ``--'' indicates insufficient conversation length 
…[truncated 65742 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T19:24:29.846943+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T19:24:29.847215+00:00_

1	% experiments.tex
2	
3	\section{Experiments}
4	
5	\paragraph{Terminology.}
6	\emph{Cross-attack OOD}: evaluation on attack families unseen during training; benign distribution remains IID throughout (OOD reflects attack-side shift only). $K$: prefix length (number of conversation turns retained). \emph{DAPT}: all Stage-1 adaptations; we extend \citet{gururangan2020dontstop} to supervised variants. \emph{Evidence hierarchy} (on synthetic data): vanilla $<$ MLM $<$ classification (Section~\ref{sec:decomposition}).
7	
8	\subsection{Setup}
9	
10	\paragraph{Data.}
11	All synthetic data is generated by Qwen3-8B~\citep{qwen3_2025}.
12	The IID dataset contains 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations, split into training (350), validation (74), and test (76) sets with balanced class ratios (e.g., test = 38 jailbreak + 38 benign).
13	Stage~1 (DAPT) uses training + validation conversations; Stage~2 (BiGRU) trains on training, early-stops on validation, and evaluates on test.
14	OOD evaluation pairs attack-specific jailbreak conversations with the 38 IID-test benign conversations: 80 FITD~\citep{fitd2024} (non-discriminative; Section~\ref{sec:decomposition}) + 38 benign = 118 total, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024} + 38 benign = 118 total, and 80 ActorAttack~\citep{ren2024actorattack} + 38 benign = 118 total.
15	No overlap exists in attack templates across families; benign is IID (same generation pipeline).
16	A paraphrased version of the IID test set (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark (Section~\ref{sec:perturbation}).
17	For human data validation, we use ToxicChat~\citep{lin2023toxicchat} (204 jailbreak + 204 benign from real LMSYS user interactions), entirely independent of Qwen3-8B generation.
18	
19	\paragraph{Models.}
20	Seven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method})
…[truncated 16188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T19:24:29.847390+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T19:24:29.847574+00:00_

1	% conclusion.tex
2	
3	\section{Discussion}
4	\label{sec:discussion}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{figures/paper/fig4_svd_subspace.pdf}
9	\caption{Test representations projected onto top-2 SVD directions. 9-class DAPT produces clear cluster separation absent in vanilla.}
10	\label{fig:svd_subspace}
11	\end{figure}
12	
13	\paragraph{Discriminative compression and label equivalence.}
14	Three observations argue against a topic shortcut: unstable topic OOD (F1\,=\,0.541$\pm$0.207), scrambled labels within 3.9\,pp, and label-free MLM detection (F1\,$\geq$\,0.97).
15	Classification DAPT compresses features into few dimensions (participation ratio 3.7--9.4 vs.\ 25--32; Figure~\ref{fig:svd_subspace}; Appendix~\ref{app:representation}), consistent with \citet{zhang2021understanding}: domain-relevant partitioning appears necessary (topic DAPT fails) and compression localizes to 3 SVD dimensions in layers 8--12. A probe confirms sufficiency; removal degrades DD by 17\,pp (Appendix~\ref{app:discriminative_probe}). The partition sufficiency finding implies that the classification objective's value lies in its structural role---forcing class-conditional feature organization---rather than in encoding persuasion-specific semantics.
16	
17	\paragraph{Cross-condition transfer and boundaries.}
18	ToxicChat (+18--42\,pp) and cross-LLM experiments (Appendix~\ref{app:cross_llm}) confirm transfer beyond single-LLM artifacts; domain exposure is universally beneficial (all DAPT variants exceed vanilla by $\geq$40\,pp on ToxicChat) but the ranking reverses across conditions (MLM leads on human data). Mixed-LLM 9-class maintains 0.818 while MLM collapses. Both data scaling (Appendix~\ref{app:scale_validation}) and mixed-LLM training involve distributional heterogeneity that appears to erode classification DAPT's concentrated feature advantage. At larger scales (355M), DAPT can be counterproductive (RoBERTa-large vanilla AA\,=\,1.000 vs.\ 9-class 
…[truncated 2765 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T19:24:29.847902+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T19:24:29.848070+00:00_

docs/paper/checklist.tex
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/abstract.tex
docs/paper/method.tex
docs/paper/related_work.tex
docs/paper/experiments.tex
docs/paper/conclusion.tex
docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T19:24:29.848215+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Label/ref consistency audit",
  "subagent_type": "Explore",
  "prompt": "I need to audit \\label and \\ref consistency across all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/. \n\nFiles: main.tex, introduction.tex, abstract.tex, method.tex, related_work.tex, experiments.tex, conclusion.tex, appendix.tex, checklist.tex\n\nTasks:\n1. Find ALL \\label{...} definitions across all files. List each label and which file defines it.\n2. Find ALL \\ref{...} and \\autoref{...} usages across all files. List each ref and which file uses it.\n3. Identify:\n   - Orphan labels: labels defined but never referenced by any \\ref\n   - Broken refs: \\ref targets that don't have a corresponding \\label\n   \nBe very thorough - search each file individually. Report the complete lists."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Agent",
  "tool_args": {
    "description": "Label/ref consistency audit",
    "subagent_type": "Explore",
    "prompt": "I need to audit \\label and \\ref consistency across all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/. \n\nFiles: main.tex, introduction.tex, abstract.tex, method.tex, related_work.tex, experiments.tex, conclusion.tex, appendix.tex, checklist.tex\n\nTasks:\n1. Find ALL \\label{...} definitions across all files. List each label and which file defines it.\n2. Find ALL \\ref{...} and \\autoref{...} usages across all files. List each ref and which file uses it.\n3. Identify:\n   - Orphan labels: labels defined but never referenced by any \\ref\n   - Broken refs: \\ref targets that don't have a corresponding \\label\n   \nBe very thorough - search each file individually. Report the complete lists."
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-23T19:24:29.848407+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T19:24:29.848532+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T19:24:29.848687+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{graphicx}
11	\graphicspath{{../../}}
12	\usepackage{amsmath}
13	\usepackage{booktabs}
14	\usepackage{enumitem}
15	\usepackage{amssymb}
16	\usepackage{multirow}
17	
18	\title{DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	
27	\input{introduction}
28	
29	\input{related_work}
30	
31	\input{method}
32	
33	\input{experiments}
34	
35	\input{conclusion}
36	
37	\bibliography{references}
38	
39	\input{appendix}
40	
41	% checklist removed — EMNLP 2026 ARR requires checklist in OpenReview form, not in PDF
42	
43	\end{document}
44	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-23T19:24:29.848839+00:00_

1	% introduction.tex
2	
3	\section{Introduction}
4	
5	Multi-turn jailbreak attacks distribute adversarial intent across individually benign turns. Crescendo~\citep{russinovich2024crescendo}, Foot-in-the-Door~\citep{fitd2024}, and Deceptive Delight~\citep{deceptivedelight2024} all rely on persuasion as their core mechanism: \citet{zeng2024pap} catalogue 40 persuasion techniques across jailbreak families, and \citet{hagendorff2026reasoning} identify strategies in 97\% of successful attacks. Because individual attack turns occupy the same embedding region as benign text~\citep{bullwinkel2025repeng}, no single-turn filter can distinguish them from legitimate conversation.
6	
7	Existing defenses leave a critical gap. Production classifiers such as Llama Guard~\citep{inan2023llamaguard}, WildGuard~\citep{han2024wildguard}, and ShieldGemma~\citep{zeng2024shieldgemma} operate on individual turns and miss multi-turn manipulation; Llama Guard~3 detects only 1.8\% of multi-turn jailbreaks in our evaluation (Section~\ref{sec:decomposition}). Multi-turn defenses (DeepContext~\citep{deepcontext2026}, BIID~\citep{tong2025biid}, G-Guard~\citep{gguard2025}) model conversation-level structure but each evaluates on a single attack family. None answers the central question: \emph{what representation properties enable a detector to generalize across attack families it has never seen?}
8	
9	Pretrained language understanding does not suffice at base model scale: vanilla DeBERTa-v3~\citep{he2021deberta} with temporal aggregation (cf.\ DeepContext) drops from F1\,=\,1.000 in-distribution to 0.312 on OOD Deceptive Delight, and GPT-5.5 reaches only 0.191--0.449 F1 (across prefix lengths) with 30--47\% unparseable responses (Appendix~\ref{sec:llm_judge}). The bottleneck is distributional: cross-attack generalization at base model scale benefits substantially from domain adaptation.
10	
11	Our pipeline, \textbf{DisPeD} (Disentangled Persuasion Detection)\footnote{We use `disentangled' to descri
…[truncated 3879 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-23T19:24:29.848988+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-23T19:24:29.849111+00:00_

1	% abstract.tex
2	\begin{abstract}
3	Multi-turn jailbreak attacks spread adversarial intent across benign-seeming turns. Existing defenses fail to generalize: Llama Guard~3 detects only 1.8\% of multi-turn jailbreaks zero-shot in our evaluation. Detecting such attacks benefits substantially from domain adaptation at base model scale, but the form of adaptation matters. We isolate the factors behind cross-attack generalization through controlled ablation: thirteen encoder configurations at base scale (125M--184M parameters) on synthetic multi-turn data decompose contributions of domain exposure, classification supervision, and label granularity across three out-of-distribution (OOD) attack families. On synthetic data, classification-based adaptation recovers OOD detection (F1\,=\,0.97--1.0 vs.\ vanilla 0.26--0.31; attack-side OOD, IID benign upper bound) while unsupervised pretraining collapses; under mixed-LLM training, template attacks remain detectable but strategy-diverse attacks degrade to chance level (F1\,=\,0.504). On human-authored single-turn data (ToxicChat), this hierarchy reverses: masked language modeling outperforms 9-class classification (F1 0.837 vs.\ 0.596). Classification adaptation's advantage is thus condition-specific rather than universal. Orthogonal to attack-side generalization, few-shot benign adaptation reduces false-positive rates from 58--68\% to 0--1.5\%, with 24.3$\times$ inference speedup (43$\times$ fewer parameters) over LLM-as-judge baselines.
4	\end{abstract}
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-23T19:24:29.849238+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-23T19:24:29.849373+00:00_

1	% method.tex
2	
3	\section{Method}
4	\label{sec:method}
5	
6	Cross-attack generalization could stem from domain exposure, classification supervision, label correctness, label granularity, or domain specificity. Disentangling these factors demands an architecture where exactly one component varies across conditions. DisPeD separates encoder adaptation (Stage~1) from temporal classification (Stage~2). Seven Stage-1 variants share the same training data and downstream pipeline but differ solely in their pretraining objective; each isolates a single factor (Figure~\ref{fig:architecture}).
7	
8	\subsection{Problem Formulation}
9	
10	A conversation $C = \{u_1, a_1, \ldots, u_N, a_N\}$ alternates user turns $u_i$ and assistant responses $a_i$. Given a prefix of $K$ user turns, the model predicts $y \in \{0, 1\}$ (jailbreak vs.\ benign). We restrict input to user turns because adversarial intent resides in the attacker's messages. This formulation supports early detection from partial prefixes.
11	
12	\subsection{Stage 1: Turn-Level Encoder Adaptation}
13	
14	Each user turn $u_i$ is encoded by DeBERTa-v3-base~\citep{he2023debertav3}; the \texttt{[CLS]} embedding $h_i \in \mathbb{R}^D$ serves as the turn representation. Seven variants, summarized in Table~\ref{tab:variants}, share the same training data but differ in objective.
15	
16	\begin{table}[t]
17	\centering
18	\small
19	\caption{Stage-1 encoder variants. All operate on the same training conversations except Wikipedia MLM (matched token count on Wikipedia text).}
20	\label{tab:variants}
21	\begin{tabular}{@{}p{1.6cm}p{2.2cm}p{2.8cm}@{}}
22	\toprule
23	\textbf{Variant} & \textbf{Objective} & \textbf{Tests whether\ldots} \\
24	\midrule
25	9-class & 9-class persuasion + binary intent & full model \\
26	Binary & binary persuasion + binary intent & granularity matters \\
27	Scrambled & random 9-class + binary intent & label correctness matters \\
28	MLM-only & 15\% token masking & supervision is necessary \\
29	Topic & 5
…[truncated 3665 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-23T19:24:29.849520+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-23T19:24:29.849682+00:00_

1	% related_work.tex
2	
3	\section{Related Work}
4	
5	\paragraph{Multi-turn jailbreak attacks.}
6	All multi-turn jailbreak families share a persuasion substrate~\citep{zeng2024pap,hagendorff2026reasoning,li2024mhj}, yet each operationalizes it differently: Crescendo~\citep{russinovich2024crescendo} gradually escalates, FITD~\citep{fitd2024} exploits commitment-consistency bias, DD~\citep{deceptivedelight2024} combines emotional manipulation with role assignment, ActorAttack~\citep{ren2024actorattack} steers through multiple personas, Echo Chamber~\citep{alobaid2026echochamber} uses context poisoning via gradual amplification, and automated methods (PAIR~\citep{chao2023pair}, TAP~\citep{mehrotra2024tap}) iteratively refine adversarial prompts, extending the automated red-teaming paradigm~\citep{perez2022redteaming}. \citet{wei2023jailbroken} provide a unifying taxonomy; RED QUEEN~\citep{jiang2024redqueen} constructs concealed multi-turn scenarios across 14 harmful categories; benchmarks~\citep{mazeika2024harmbench,chao2024jailbreakbench} standardize single-turn comparison, while MultiBreak~\citep{song2026multibreak} targets multi-turn evaluation. This shared substrate with diverse surface strategies defines our evaluation: a detector must generalize across families, not merely succeed on its training distribution.
7	
8	\paragraph{Multi-turn defenses and production safety.}
9	No existing defense evaluates cross-attack transfer. Recent conversation-level systems pair fine-tuned BERT~\citep{devlin2019bert} encoders with sequence-level aggregation via GRU hierarchies (DeepContext~\citep{deepcontext2026}), turn-intention inference (BIID~\citep{tong2025biid}), graph neural networks (G-Guard~\citep{gguard2025}), or predictive generation (SafeDream~\citep{safedream2026}), yet each evaluates on a single attack family. Direct experimental comparison with DeepContext, BIID, and G-Guard is precluded by the absence of public implementations and incompatible evaluation protocols; 
…[truncated 3718 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-23T19:24:29.849914+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-23T19:24:29.850237+00:00_

1	% experiments.tex
2	
3	\section{Experiments}
4	
5	\paragraph{Terminology.}
6	\emph{Cross-attack OOD}: evaluation on attack families unseen during training; benign distribution remains IID throughout (OOD reflects attack-side shift only). $K$: prefix length (number of conversation turns retained). \emph{DAPT}: all Stage-1 adaptations; we extend \citet{gururangan2020dontstop} to supervised variants. \emph{Evidence hierarchy} (on synthetic data): vanilla $<$ MLM $<$ classification (Section~\ref{sec:decomposition}).
7	
8	\subsection{Setup}
9	
10	\paragraph{Data.}
11	All synthetic data is generated by Qwen3-8B~\citep{qwen3_2025}.
12	The IID dataset contains 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations, split into training (350), validation (74), and test (76) sets with balanced class ratios (e.g., test = 38 jailbreak + 38 benign).
13	Stage~1 (DAPT) uses training + validation conversations; Stage~2 (BiGRU) trains on training, early-stops on validation, and evaluates on test.
14	OOD evaluation pairs attack-specific jailbreak conversations with the 38 IID-test benign conversations: 80 FITD~\citep{fitd2024} (non-discriminative; Section~\ref{sec:decomposition}) + 38 benign = 118 total, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024} + 38 benign = 118 total, and 80 ActorAttack~\citep{ren2024actorattack} + 38 benign = 118 total.
15	No overlap exists in attack templates across families; benign is IID (same generation pipeline).
16	A paraphrased version of the IID test set (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark (Section~\ref{sec:perturbation}).
17	For human data validation, we use ToxicChat~\citep{lin2023toxicchat} (204 jailbreak + 204 benign from real LMSYS user interactions), entirely independent of Qwen3-8B generation.
18	
19	\paragraph{Models.}
20	Seven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method})
…[truncated 16188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-23T19:24:29.850486+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-23T19:24:29.850747+00:00_

1	% conclusion.tex
2	
3	\section{Discussion}
4	\label{sec:discussion}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{figures/paper/fig4_svd_subspace.pdf}
9	\caption{Test representations projected onto top-2 SVD directions. 9-class DAPT produces clear cluster separation absent in vanilla.}
10	\label{fig:svd_subspace}
11	\end{figure}
12	
13	\paragraph{Discriminative compression and label equivalence.}
14	Three observations argue against a topic shortcut: unstable topic OOD (F1\,=\,0.541$\pm$0.207), scrambled labels within 3.9\,pp, and label-free MLM detection (F1\,$\geq$\,0.97).
15	Classification DAPT compresses features into few dimensions (participation ratio 3.7--9.4 vs.\ 25--32; Figure~\ref{fig:svd_subspace}; Appendix~\ref{app:representation}), consistent with \citet{zhang2021understanding}: domain-relevant partitioning appears necessary (topic DAPT fails) and compression localizes to 3 SVD dimensions in layers 8--12. A probe confirms sufficiency; removal degrades DD by 17\,pp (Appendix~\ref{app:discriminative_probe}). The partition sufficiency finding implies that the classification objective's value lies in its structural role---forcing class-conditional feature organization---rather than in encoding persuasion-specific semantics.
16	
17	\paragraph{Cross-condition transfer and boundaries.}
18	ToxicChat (+18--42\,pp) and cross-LLM experiments (Appendix~\ref{app:cross_llm}) confirm transfer beyond single-LLM artifacts; domain exposure is universally beneficial (all DAPT variants exceed vanilla by $\geq$40\,pp on ToxicChat) but the ranking reverses across conditions (MLM leads on human data). Mixed-LLM 9-class maintains 0.818 while MLM collapses. Both data scaling (Appendix~\ref{app:scale_validation}) and mixed-LLM training involve distributional heterogeneity that appears to erode classification DAPT's concentrated feature advantage. At larger scales (355M), DAPT can be counterproductive (RoBERTa-large vanilla AA\,=\,1.000 vs.\ 9-class 
…[truncated 2765 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-23T19:24:29.850988+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T19:24:29.851179+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Cross-check main_results vs full_prefix",
  "subagent_type": "Explore",
  "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex, find Table tab:main_results and extract the exact DD OOD Full F1 value for the \"9-class\" row.\n\nThen in appendix.tex in the same directory, find Table tab:full_prefix and extract the exact DD OOD Full F1 value for the \"9-class (ours)\" row.\n\nAlso check: in the tab:evidence_hierarchy table in experiments.tex, what is the DD-Full value for 9-class?\n\nReport the exact LaTeX for each value so I can compare them."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Agent",
  "tool_args": {
    "description": "Cross-check main_results vs full_prefix",
    "subagent_type": "Explore",
    "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex, find Table tab:main_results and extract the exact DD OOD Full F1 value for the \"9-class\" row.\n\nThen in appendix.tex in the same directory, find Table tab:full_prefix and extract the exact DD OOD Full F1 value for the \"9-class (ours)\" row.\n\nAlso check: in the tab:evidence_hierarchy table in experiments.tex, what is the DD-Full value for 9-class?\n\nReport the exact LaTeX for each value so I can compare them."
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-23T19:24:29.851401+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/checklist.tex"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-23T19:24:29.851951+00:00_

1	% appendix.tex — Supplementary material
2	
3	\appendix
4	
5	\section{LLM-as-Judge Baseline}
6	\label{sec:llm_judge}
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{LLM-as-judge jailbreak detection. IID: binary F1 (Crescendo test set); OOD: macro F1 (DD = Deceptive Delight, AA = ActorAttack). GPT-5.5 F1 values exclude unparseable responses and represent upper bounds.}
12	\label{tab:llm_judge}
13	\begin{tabular}{@{}lcccr@{}}
14	\toprule
15	\textbf{Method} & DD & AA & IID & Unparse. \\
16	\midrule
17	\multicolumn{5}{l}{\textit{Zero-shot}} \\[2pt]
18	GPT-5.5 & -- & -- & .383 & 30--47\% \\
19	Qwen3-8B & .244 & .244 & .100 & 0\% \\
20	\midrule
21	\multicolumn{5}{l}{\textit{3-shot}} \\[2pt]
22	Qwen3-8B & .566 & .652 & -- & 0\% \\
23	\midrule
24	\multicolumn{5}{l}{\textit{Trained classifier}} \\[2pt]
25	9-class (ours) & \textbf{.994} & \textbf{.972} & \textbf{1.000} & 0\% \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:llm_judge} reports LLM-as-judge performance on IID and OOD data.
31	On IID Crescendo, GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 = 0.383 on full conversations; 30--47\% of responses are unparseable.
32	Qwen3-8B performs worse (IID F1 = 0.100).
33	On OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 on both DD and ActorAttack by predicting nearly all conversations as benign.
34	Even with 3-shot prompting, Qwen3-8B reaches only 0.566 (DD) and 0.652 (AA), while DisPeD maintains macro F1 $\geq$ 0.972.
35	The poor performance of content-level reasoning on unseen attack families underscores the necessity of trained classifiers with domain-adapted representations.
36	
37	\section{Full Cross-Attack Results by Prefix}
38	\label{sec:full_prefix}
39	
40	\begin{table*}[t]
41	\centering
42	\small
43	\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\pm$std where available. ``--'' indicates insufficient conversation length 
…[truncated 65742 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T19:24:29.852245+00:00_

1	% checklist.tex — ARR Responsible NLP Research Checklist
2	
3	\section*{Responsible NLP Research Checklist}
4	
5	\paragraph{A. Limitations.}
6	\begin{enumerate}[label=A\arabic*.,leftmargin=2em]
7	  \item Did you describe the limitations of your work? \textbf{Yes.} Section~\ref{sec:limitations} discusses dataset scale, lexical separability, annotation quality, OOD strategy prediction, single-seed variants, scope, and compute cost.
8	  \item Did you discuss any potential risks of your work? \textbf{Yes.} See below.
9	\end{enumerate}
10	
11	\paragraph{B. Potential Risks and Ethical Considerations.}
12	This work studies multi-turn jailbreak attacks against LLMs. While the analysis is defensive (improving detection), we acknowledge dual-use risk: the persuasion taxonomy and attack strategy analysis could inform adversarial actors. We mitigate this by: (1) using only synthetic conversations generated by an open-weight model (Qwen3-8B), not real attack data targeting production systems; (2) not releasing attack-generation prompts that could enable novel attacks; (3) focusing the contribution on detection mechanisms rather than attack techniques. All jailbreak conversations are synthetic and do not contain real harmful content. No human subjects were involved.
13	
14	\paragraph{C. Computational Experiments.}
15	\begin{enumerate}[label=C\arabic*.,leftmargin=2em]
16	  \item Did you report the number of parameters in the models used? \textbf{Yes.} DeBERTa-v3-base (184M) and RoBERTa-base (125M) in Sections~\ref{sec:method} and~\ref{sec:discussion}.
17	  \item Did you report the total amount of compute and the type of resources used? \textbf{Yes.} Under 4 GPU-hours total on a single NVIDIA A100 (40GB). Section~\ref{sec:limitations} and Appendix~\ref{sec:reproducibility}.
18	  \item Did you report the implementation details sufficient for reproducibility? \textbf{Yes.} Appendix~\ref{sec:reproducibility} provides all hyperparameters. We will release code and data upon acceptance
…[truncated 1416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T19:24:29.852505+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\label\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\label\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T19:24:29.852746+00:00_

docs/paper/experiments.tex:42:\label{tab:main_results}
docs/paper/experiments.tex:67:\label{fig:cross_attack_bar}
docs/paper/experiments.tex:74:\label{sec:decomposition}
docs/paper/experiments.tex:80:\label{tab:evidence_hierarchy}
docs/paper/experiments.tex:113:\label{fig:evidence_hierarchy}
docs/paper/experiments.tex:136:\label{sec:cross_encoder}
docs/paper/experiments.tex:142:\label{tab:cross_encoder}
docs/paper/experiments.tex:180:\label{sec:human_data}
docs/paper/experiments.tex:188:\label{tab:human_data}
docs/paper/experiments.tex:209:\label{sec:perturbation}
docs/paper/experiments.tex:215:\label{sec:benign_shift}
docs/paper/conclusion.tex:4:\label{sec:discussion}
docs/paper/conclusion.tex:10:\label{fig:svd_subspace}
docs/paper/conclusion.tex:28:\label{sec:limitations}
docs/paper/method.tex:4:\label{sec:method}
docs/paper/method.tex:20:\label{tab:variants}
docs/paper/appendix.tex:6:\label{sec:llm_judge}
docs/paper/appendix.tex:12:\label{tab:llm_judge}
docs/paper/appendix.tex:38:\label{sec:full_prefix}
docs/paper/appendix.tex:44:\label{tab:full_prefix}
docs/paper/appendix.tex:72:\label{sec:actorattack_full}
docs/paper/appendix.tex:78:\label{tab:actorattack_full}
docs/paper/appendix.tex:104:\label{app:aa_error}
docs/paper/appendix.tex:109:\label{sec:perturbation_full}
docs/paper/appendix.tex:115:\label{tab:perturbation}
docs/paper/appendix.tex:143:\label{tab:ood_perturbation}
docs/paper/appendix.tex:166:\label{sec:strategy_full}
docs/paper/appendix.tex:172:\label{fig:strategy_heatmap}
docs/paper/appendix.tex:181:\label{sec:cka_heatmap}
docs/paper/appendix.tex:187:\label{fig:cka_heatmap}
docs/paper/appendix.tex:191:\label{app:tsne}
docs/paper/appendix.tex:199:\label{fig:tsne}
docs/paper/appendix.tex:203:\label{app:cross_llm}
docs/paper/appendix.tex:209:\label{tab:cross_llm}
docs/paper/appendix.tex:231:\label{tab:cross_llm_error}
docs/paper/appendix.tex:246:\label{app:mixed_llm}
docs/paper/appendix.tex:252:\label{tab:mixed_llm}
docs/paper/appendix.tex:267:\label{ap
…[truncated 2803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T19:24:29.852964+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\(?:ref|autoref)\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\(?:ref|autoref)\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T19:24:29.853216+00:00_

docs/paper/related_work.tex:9:[Omitted long matching line]
docs/paper/experiments.tex:6:\emph{Cross-attack OOD}: evaluation on attack families unseen during training; benign distribution remains IID throughout (OOD reflects attack-side shift only). $K$: prefix length (number of conversation turns retained). \emph{DAPT}: all Stage-1 adaptations; we extend \citet{gururangan2020dontstop} to supervised variants. \emph{Evidence hierarchy} (on synthetic data): vanilla $<$ MLM $<$ classification (Section~\ref{sec:decomposition}).
docs/paper/experiments.tex:14:OOD evaluation pairs attack-specific jailbreak conversations with the 38 IID-test benign conversations: 80 FITD~\citep{fitd2024} (non-discriminative; Section~\ref{sec:decomposition}) + 38 benign = 118 total, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024} + 38 benign = 118 total, and 80 ActorAttack~\citep{ren2024actorattack} + 38 benign = 118 total.
docs/paper/experiments.tex:16:A paraphrased version of the IID test set (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark (Section~\ref{sec:perturbation}).
docs/paper/experiments.tex:20:Seven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method}).
docs/paper/experiments.tex:22:For cross-encoder validation, we replicate vanilla, MLM, and 9-class variants on RoBERTa-base~\citep{liu2019roberta} (Section~\ref{sec:cross_encoder}).
docs/paper/experiments.tex:23:We also compare TF-IDF LR, LLM-as-judge (Appendix~\ref{sec:llm_judge}), and Llama Guard~3~8B~\citep{metallamaguard3_2024} (zero-shot; evaluates last-response safety given conversation context), which detects only 1.8\% of multi-turn jailbreaks (5/278 pooled recall; Table~\ref{tab:evidence_hierarchy}).
docs/paper/experiments.tex:26:F1 for binary jailbreak detection at prefix $K$=2 and full conversations (full per-$K$ results in Appendix~\ref{sec:full_prefix}).
docs/paper/experiments.tex:28:For key pairwise comparisons, we
…[truncated 17254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-23T19:24:29.853438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T19:24:29.853735+00:00_

1	% experiments.tex
2	
3	\section{Experiments}
4	
5	\paragraph{Terminology.}
6	\emph{Cross-attack OOD}: evaluation on attack families unseen during training; benign distribution remains IID throughout (OOD reflects attack-side shift only). $K$: prefix length (number of conversation turns retained). \emph{DAPT}: all Stage-1 adaptations; we extend \citet{gururangan2020dontstop} to supervised variants. \emph{Evidence hierarchy} (on synthetic data): vanilla $<$ MLM $<$ classification (Section~\ref{sec:decomposition}).
7	
8	\subsection{Setup}
9	
10	\paragraph{Data.}
11	All synthetic data is generated by Qwen3-8B~\citep{qwen3_2025}.
12	The IID dataset contains 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations, split into training (350), validation (74), and test (76) sets with balanced class ratios (e.g., test = 38 jailbreak + 38 benign).
13	Stage~1 (DAPT) uses training + validation conversations; Stage~2 (BiGRU) trains on training, early-stops on validation, and evaluates on test.
14	OOD evaluation pairs attack-specific jailbreak conversations with the 38 IID-test benign conversations: 80 FITD~\citep{fitd2024} (non-discriminative; Section~\ref{sec:decomposition}) + 38 benign = 118 total, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024} + 38 benign = 118 total, and 80 ActorAttack~\citep{ren2024actorattack} + 38 benign = 118 total.
15	No overlap exists in attack templates across families; benign is IID (same generation pipeline).
16	A paraphrased version of the IID test set (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark (Section~\ref{sec:perturbation}).
17	For human data validation, we use ToxicChat~\citep{lin2023toxicchat} (204 jailbreak + 204 benign from real LMSYS user interactions), entirely independent of Qwen3-8B generation.
18	
19	\paragraph{Models.}
20	Seven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method})
…[truncated 16188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-23T19:24:29.853960+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T19:24:29.854388+00:00_

1	% appendix.tex — Supplementary material
2	
3	\appendix
4	
5	\section{LLM-as-Judge Baseline}
6	\label{sec:llm_judge}
7	
8	\begin{table}[t]
9	\centering
10	\small
11	\caption{LLM-as-judge jailbreak detection. IID: binary F1 (Crescendo test set); OOD: macro F1 (DD = Deceptive Delight, AA = ActorAttack). GPT-5.5 F1 values exclude unparseable responses and represent upper bounds.}
12	\label{tab:llm_judge}
13	\begin{tabular}{@{}lcccr@{}}
14	\toprule
15	\textbf{Method} & DD & AA & IID & Unparse. \\
16	\midrule
17	\multicolumn{5}{l}{\textit{Zero-shot}} \\[2pt]
18	GPT-5.5 & -- & -- & .383 & 30--47\% \\
19	Qwen3-8B & .244 & .244 & .100 & 0\% \\
20	\midrule
21	\multicolumn{5}{l}{\textit{3-shot}} \\[2pt]
22	Qwen3-8B & .566 & .652 & -- & 0\% \\
23	\midrule
24	\multicolumn{5}{l}{\textit{Trained classifier}} \\[2pt]
25	9-class (ours) & \textbf{.994} & \textbf{.972} & \textbf{1.000} & 0\% \\
26	\bottomrule
27	\end{tabular}
28	\end{table}
29	
30	Table~\ref{tab:llm_judge} reports LLM-as-judge performance on IID and OOD data.
31	On IID Crescendo, GPT-5.5 achieves precision of 1.0 at all turn prefixes but recall ranges from only 0.105 to 0.290, resulting in F1 = 0.383 on full conversations; 30--47\% of responses are unparseable.
32	Qwen3-8B performs worse (IID F1 = 0.100).
33	On OOD data, zero-shot Qwen3-8B achieves macro F1 = 0.244 on both DD and ActorAttack by predicting nearly all conversations as benign.
34	Even with 3-shot prompting, Qwen3-8B reaches only 0.566 (DD) and 0.652 (AA), while DisPeD maintains macro F1 $\geq$ 0.972.
35	The poor performance of content-level reasoning on unseen attack families underscores the necessity of trained classifiers with domain-adapted representations.
36	
37	\section{Full Cross-Attack Results by Prefix}
38	\label{sec:full_prefix}
39	
40	\begin{table*}[t]
41	\centering
42	\small
43	\caption{Full cross-attack generalization results (F1) at all prefix lengths. 3-seed mean$\pm$std where available. ``--'' indicates insufficient conversation length 
…[truncated 65742 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-23T19:24:29.854613+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Check discussion ≥40pp claim",
  "subagent_type": "Explore",
  "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex, find the exact sentence that mentions \"≥40\" or \"geq.*40\" in the Discussion section. Report the full sentence.\n\nThen in experiments.tex in the same directory, find the ToxicChat results table (tab:human_data). List all variant names and their Macro F1 values. Also note the Vanilla F1 value. I need to verify whether \"all DAPT variants exceed vanilla by ≥40 pp\" is correct by computing each variant's improvement over vanilla."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Agent",
  "tool_args": {
    "description": "Check discussion ≥40pp claim",
    "subagent_type": "Explore",
    "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex, find the exact sentence that mentions \"≥40\" or \"geq.*40\" in the Discussion section. Report the full sentence.\n\nThen in experiments.tex in the same directory, find the ToxicChat results table (tab:human_data). List all variant names and their Macro F1 values. Also note the Vanilla F1 value. I need to verify whether \"all DAPT variants exceed vanilla by ≥40 pp\" is correct by computing each variant's improvement over vanilla."
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-23T19:24:29.854798+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper -type f -name \"*.tex\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper -type f -name \"*.tex\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-23T19:24:29.854924+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-23T19:24:29.855053+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-23T19:24:29.855190+00:00_

1	% conclusion.tex
2	
3	\section{Discussion}
4	\label{sec:discussion}
5	
6	\begin{figure}[t]
7	\centering
8	\includegraphics[width=\columnwidth]{figures/paper/fig4_svd_subspace.pdf}
9	\caption{Test representations projected onto top-2 SVD directions. 9-class DAPT produces clear cluster separation absent in vanilla.}
10	\label{fig:svd_subspace}
11	\end{figure}
12	
13	\paragraph{Discriminative compression and label equivalence.}
14	Three observations argue against a topic shortcut: unstable topic OOD (F1\,=\,0.541$\pm$0.207), scrambled labels within 3.9\,pp, and label-free MLM detection (F1\,$\geq$\,0.97).
15	Classification DAPT compresses features into few dimensions (participation ratio 3.7--9.4 vs.\ 25--32; Figure~\ref{fig:svd_subspace}; Appendix~\ref{app:representation}), consistent with \citet{zhang2021understanding}: domain-relevant partitioning appears necessary (topic DAPT fails) and compression localizes to 3 SVD dimensions in layers 8--12. A probe confirms sufficiency; removal degrades DD by 17\,pp (Appendix~\ref{app:discriminative_probe}). The partition sufficiency finding implies that the classification objective's value lies in its structural role---forcing class-conditional feature organization---rather than in encoding persuasion-specific semantics.
16	
17	\paragraph{Cross-condition transfer and boundaries.}
18	ToxicChat (+18--42\,pp) and cross-LLM experiments (Appendix~\ref{app:cross_llm}) confirm transfer beyond single-LLM artifacts; domain exposure is universally beneficial (all DAPT variants exceed vanilla by $\geq$40\,pp on ToxicChat) but the ranking reverses across conditions (MLM leads on human data). Mixed-LLM 9-class maintains 0.818 while MLM collapses. Both data scaling (Appendix~\ref{app:scale_validation}) and mixed-LLM training involve distributional heterogeneity that appears to erode classification DAPT's concentrated feature advantage. At larger scales (355M), DAPT can be counterproductive (RoBERTa-large vanilla AA\,=\,1.000 vs.\ 9-class 
…[truncated 2765 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-23T19:24:29.855389+00:00_

Now I need to search for the specific tables and extract the exact values. Let me search more carefully for each table:

1. Table tab:main_results - I can see it in experiments.tex at line 42-56
2. Table tab:full_prefix - I need to find this in appendix.tex
3. Table tab:evidence_hierarchy - I can see it in experiments.tex at line 80-105

Let me extract the exact LaTeX values:

From **experiments.tex** (line 48), Table `tab:main_results`:
- Row "9-class", column "OOD (DD)" Full: `.997$\pm$.005`

From **experiments.tex** (line 86), Table `tab:evidence_hierarchy`:
- Row "9-class (full model)", column "DD-Full": `.997$\pm$.005`

From **appendix.tex** (line 56), Table `tab:full_prefix`:
- Row "9-class (ours)", OOD (Deceptive Delight), Full column: `.994$\pm$.005`

Here are the exact values you requested:

**Table tab:main_results** (experiments.tex, line 48):
- 9-class, DD OOD Full F1: `.997$\pm$.005`

**Table tab:evidence_hierarchy** (experiments.tex, line 86):
- 9-class (full model), DD-Full: `.997$\pm$.005`

**Table tab:full_prefix** (appendix.tex, line 56):
- 9-class (ours), OOD (Deceptive Delight) Full: `.994$\pm$.005`

Comparison summary:
- tab:main_results: `.997$\pm$.005`
- tab:evidence_hierarchy: `.997$\pm$.005`  (identical to tab:main_results)
- tab:full_prefix: `.994$\pm$.005`  (3 points lower in the mean value)

The first two tables report the same value, while tab:full_prefix shows a slightly lower mean (0.994 vs 0.997) with the same standard deviation (±0.005).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Agent",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-23T19:24:29.855558+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-23T19:24:29.855792+00:00_

1	% experiments.tex
2	
3	\section{Experiments}
4	
5	\paragraph{Terminology.}
6	\emph{Cross-attack OOD}: evaluation on attack families unseen during training; benign distribution remains IID throughout (OOD reflects attack-side shift only). $K$: prefix length (number of conversation turns retained). \emph{DAPT}: all Stage-1 adaptations; we extend \citet{gururangan2020dontstop} to supervised variants. \emph{Evidence hierarchy} (on synthetic data): vanilla $<$ MLM $<$ classification (Section~\ref{sec:decomposition}).
7	
8	\subsection{Setup}
9	
10	\paragraph{Data.}
11	All synthetic data is generated by Qwen3-8B~\citep{qwen3_2025}.
12	The IID dataset contains 250 Crescendo~\citep{russinovich2024crescendo} jailbreak and 250 topic-anchored benign conversations, split into training (350), validation (74), and test (76) sets with balanced class ratios (e.g., test = 38 jailbreak + 38 benign).
13	Stage~1 (DAPT) uses training + validation conversations; Stage~2 (BiGRU) trains on training, early-stops on validation, and evaluates on test.
14	OOD evaluation pairs attack-specific jailbreak conversations with the 38 IID-test benign conversations: 80 FITD~\citep{fitd2024} (non-discriminative; Section~\ref{sec:decomposition}) + 38 benign = 118 total, 80 Deceptive Delight (DD)~\citep{deceptivedelight2024} + 38 benign = 118 total, and 80 ActorAttack~\citep{ren2024actorattack} + 38 benign = 118 total.
15	No overlap exists in attack templates across families; benign is IID (same generation pipeline).
16	A paraphrased version of the IID test set (BERTScore 0.92, lexical overlap 0.20) serves as the adversarial robustness benchmark (Section~\ref{sec:perturbation}).
17	For human data validation, we use ToxicChat~\citep{lin2023toxicchat} (204 jailbreak + 204 benign from real LMSYS user interactions), entirely independent of Qwen3-8B generation.
18	
19	\paragraph{Models.}
20	Seven DeBERTa-v3 variants share the same Stage-2 pipeline and differ only in Stage-1 training (Section~\ref{sec:method})
…[truncated 16188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-23T19:24:29.855982+00:00_

Perfect! I found all the information needed. Let me compile the results:

## Findings

### 1. Sentence from conclusion.tex (Discussion section)

The exact sentence mentioning "≥40" is found on line 18:

**"ToxicChat (+18--42\,pp) and cross-LLM experiments (Appendix~\ref{app:cross_llm}) confirm transfer beyond single-LLM artifacts; domain exposure is universally beneficial (all DAPT variants exceed vanilla by $\geq$40\,pp on ToxicChat) but the ranking reverses across conditions (MLM leads on human data)."**

### 2. ToxicChat Results Table (tab:human_data)

From experiments.tex lines 184-203, the ToxicChat table shows:

**Variant names and Macro F1 values:**
- JB-MLM: 0.837 ± 0.013
- Wiki-MLM: 0.791 ± 0.093
- Binary: 0.705 ± 0.072
- Scrambled: 0.616 ± 0.056
- 9-class: 0.596 ± 0.087
- Topic: 0.496 ± 0.042

**Vanilla F1 value: 0.413 ± 0.021**

### 3. Verification of "≥40 pp" claim

Computing each variant's improvement over vanilla (0.413):
- JB-MLM: 0.837 - 0.413 = 0.424 (42.4 pp) ✓
- Wiki-MLM: 0.791 - 0.413 = 0.378 (37.8 pp) ✗
- Binary: 0.705 - 0.413 = 0.292 (29.2 pp) ✗
- Scrambled: 0.616 - 0.413 = 0.203 (20.3 pp) ✗
- 9-class: 0.596 - 0.413 = 0.183 (18.3 pp) ✗
- Topic: 0.496 - 0.413 = 0.083 (8.3 pp) ✗

**The statement "all DAPT variants exceed vanilla by ≥40 pp" is INCORRECT.** Only JB-MLM exceeds the 40 pp threshold. The paper's text on line 205 states "All DAPT variants exceed vanilla by 18--42\,pp", which is accurate—this range correctly describes the observed improvements (8.3 pp to 42.4 pp, with most in the 18-42 pp range cited). However, the specific claim in the Discussion section using "≥40\,pp" is not supported by these numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Agent",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-23T19:24:29.856273+00:00_

Perfect! Now let me create a comprehensive audit report by analyzing the data I've collected.

## LaTeX Label and Reference Audit Report

I have completed a thorough audit of all `\label` and `\ref`/`\autoref` definitions and usages across the nine .tex files in your paper directory.

### Task 1: ALL \label{...} DEFINITIONS (95 total)

**introduction.tex (1 label):**
- `fig:architecture` (line 17)

**abstract.tex (0 labels)**

**method.tex (2 labels):**
- `sec:method` (line 4)
- `tab:variants` (line 20)

**related_work.tex (0 labels)**

**experiments.tex (10 labels):**
- `tab:main_results` (line 42)
- `fig:cross_attack_bar` (line 67)
- `sec:decomposition` (line 74)
- `tab:evidence_hierarchy` (line 80)
- `fig:evidence_hierarchy` (line 113)
- `sec:cross_encoder` (line 136)
- `tab:cross_encoder` (line 142)
- `sec:human_data` (line 180)
- `tab:human_data` (line 188)
- `sec:perturbation` (line 209)
- `sec:benign_shift` (line 215)

**conclusion.tex (3 labels):**
- `sec:discussion` (line 4)
- `fig:svd_subspace` (line 10)
- `sec:limitations` (line 28)

**appendix.tex (79 labels):**
- `sec:llm_judge` (line 6)
- `tab:llm_judge` (line 12)
- `sec:full_prefix` (line 38)
- `tab:full_prefix` (line 44)
- `sec:actorattack_full` (line 72)
- `tab:actorattack_full` (line 78)
- `app:aa_error` (line 104)
- `sec:perturbation_full` (line 109)
- `tab:perturbation` (line 115)
- `tab:ood_perturbation` (line 143)
- `sec:strategy_full` (line 166)
- `fig:strategy_heatmap` (line 172)
- `sec:cka_heatmap` (line 181)
- `fig:cka_heatmap` (line 187)
- `app:tsne` (line 191)
- `fig:tsne` (line 199)
- `app:cross_llm` (line 203)
- `tab:cross_llm` (line 209)
- `tab:cross_llm_error` (line 231)
- `app:mixed_llm` (line 246)
- `tab:mixed_llm` (line 252)
- `app:scale_validation` (line 267)
- `tab:scale_validation` (line 273)
- `tab:roberta_large_lr` (line 295)
- `tab:tost_sensitivity` (line 315)
- `app:random_partition` (line 330)
- `app:topic_failure` (line 331)
- `tab:random_partition` (line 339)
- `tab:topic
…[truncated 7043 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Agent",
  "elapsed_ms": 8
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-23T19:24:29.856479+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper && grep -ohP '\\\\\\\\label\\{[^}]+\\}' *.tex | sed 's/\\\\\\\\label{//;s/}//' | sort -u > /tmp/labels.txt && grep -ohP '\\\\\\\\ref\\{[^}]+\\}' *.tex | sed 's/\\\\\\\\ref{//;s/}//' | sort -u > /tmp/refs.txt && echo \"=== Orphan labels (defined but never referenced) ===\" && comm -23 /tmp/labels.txt /tmp/refs.txt && echo \"=== Broken refs (referenced but never defined) ===\" && comm -13 /tmp/labels.txt /tmp/refs.txt",
  "description": "Find orphan labels and broken refs across all tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper && grep -ohP '\\\\\\\\label\\{[^}]+\\}' *.tex | sed 's/\\\\\\\\label{//;s/}//' | sort -u > /tmp/labels.txt && grep -ohP '\\\\\\\\ref\\{[^}]+\\}' *.tex | sed 's/\\\\\\\\ref{//;s/}//' | sort -u > /tmp/refs.txt && echo \"=== Orphan labels (defined but never referenced) ===\" && comm -23 /tmp/labels.txt /tmp/refs.txt && echo \"=== Broken refs (referenced but never defined) ===\" && comm -13 /tmp/labels.txt /tmp/refs.txt",
    "description": "Find orphan labels and broken refs across all tex files"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-23T19:24:29.856638+00:00_

=== Orphan labels (defined but never referenced) ===
=== Broken refs (referenced but never defined) ===

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-23T19:24:29.856827+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "all DAPT variants exceed vanilla by",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Grep",
  "tool_args": {
    "pattern": "all DAPT variants exceed vanilla by",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-23T19:24:29.856951+00:00_

conclusion.tex:18:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-23T19:24:29.857075+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "12--14",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Grep",
  "tool_args": {
    "pattern": "12--14",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-23T19:24:29.857200+00:00_

experiments.tex:217:On WildChat benign conversations, 9-class FPR rises to 68.1\%. Few-shot adaptation (Stage-2 BiGRU, encoder frozen, $N$ benign conversations, BCE loss, 5 epochs) resolves this: 10 WildChat conversations reduce FPR to 0\%, 25 OASST2 to 1.0\%; dual-OOD F1 drops 12--14\,pp without adaptation but recovers within 0.3\,pp (Appendix~\ref{app:dual_ood}).
conclusion.tex:32:\item \textbf{IID benign upper bound.} OOD F1 figures assume IID benign data; dual-OOD evaluation drops 12--14\,pp without adaptation (Table~\ref{tab:main_results}). Few-shot benign adaptation recovers performance but is validated on only two platforms ($n \leq 49$).
appendix.tex:504:Without benign adaptation, dual-OOD F1 drops by 12--14\,pp (DD: $.994 \to .855$; AA: $.981 \to .842$), driven entirely by false positives on OOD benign inputs. After few-shot adaptation---10 WildChat or 25 OASST2 conversations---dual-OOD F1 recovers to within 0.3\,pp of the IID upper bound, confirming that the lightweight adaptation procedure (Section~\ref{sec:benign_shift}) effectively closes the benign distribution gap without compromising attack-side performance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_appendix-consistency_20260523T191656",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-23T19:24:29.857411+00:00_

## Appendix 一致性核对报告

### ✅ 核对一致

- **κ=0.78** (Limitations) ← `fig:strategy_heatmap` caption (appendix:171) "κ=0.78"
- **184M vs 355M** (Limitations) ← `tab:cross_encoder` (experiments:148,158) DeBERTa-v3-base 184M, RoBERTa-large 355M
- **125M--355M** (Limitations) ← `tab:cross_encoder` RoBERTa-base 125M ~ RoBERTa-large 355M
- **PR 3.7--9.4 vs 25--32** (Discussion) ← `tab:representation` (appendix:617-629) Binary=3.7, 9-class=9.4; JB-MLM=24.6, Wiki-MLM=25.0, Vanilla=31.9. "25--32" 是对 24.6-31.9 的四舍五入，可接受
- **17 pp removal degradation** (Discussion) ← `tab:svd_necessity` (appendix:696) DD: 1.000→0.831 = 16.9pp ≈ 17pp
- **+18--42 pp ToxicChat** (Discussion range) ← `tab:human_data` (experiments:189-202) 9-class 0.596−0.413=18.3pp, JB-MLM 0.837−0.413=42.4pp
- **0.818 mixed-LLM** (Discussion) ← `tab:mixed_llm` (appendix:257) 9-class DD OOD = .818±.096
- **68.1% WildChat FPR** (Discussion) ← `tab:wildchat_fpr` (appendix:445) 9-class Mean = 68.1±6.4
- **−57.9 pp padding** (Discussion, 数值) ← `tab:length_independence` Part C (appendix:784) AA padded Δ=−57.9 pp
- **TOST table (tab:tost_sensitivity)** — caption 写 "10 seeds" ✅，3 行数据 (DD/FITD/AA) ✅，experiments:118 引用 "p < 10^{-8}, d = −0.14" 与表中 p=2.06×10^{-9}, d=−0.136 一致
- **n≤49 adaptation samples** — 见下方不一致项
- **Label/Ref** — 所有 `\ref` 均有对应 `\label`，无 broken refs；所有 `\label` 均有对应 `\ref`，无 orphan labels

---

### ⚠️ 不一致

1. **Discussion "≥40 pp" 错误** (conclusion.tex:18)
   - 正文: "all DAPT variants exceed vanilla by ≥40 pp on ToxicChat"
   - 实际: 只有 JB-MLM (42.4pp) 超过 40pp。其余: Wiki-MLM 37.8pp, Binary 29.2pp, Scrambled 20.3pp, 9-class 18.3pp, Topic 8.3pp
   - **建议**: 改为 `$\geq$18\,pp` 或与同句已有的 "+18--42 pp" 保持一致

2. **Limitations 错误 Table 引用** (conclusion.tex:32)
   - 正文: "dual-OOD evaluation drops 12--14 pp without adaptation (Table~\ref{tab:main_results})"
   - 实际: `tab:main_results` 不含 dual-OOD 数据。dual-OOD 数据在 `tab:evidence_hierarchy` (底部 rows) 和 Appendix `tab:dual_ood`
   - **建议**: 改为 `Table~\ref{tab:evidence_hierarchy}`

3. **DD-Full 9-class 数值: .997 vs .994**
   - `tab:main_results` (experiments:48): **.997**±.005
   - `tab:evidence_hierarchy` (experiments:86): **.997**±.005
   - `tab:full_prefix` (appendix:56): **.994**±.005
   - `tab:full_prefix` 的 K=5 列 = .997, Full 列 = .994。正文表格可能误用了 K=5 的值作为 Full
   - 同样问题存在于 **Scrambled**: evidence_hierarchy .997 vs full_prefix .994

4. **Limitations n≤49 错误** (conclusion.tex:32)
   - 正文: "validated on only two platforms ($n \leq 49$)"
   - 实际: OASST2 adaptation curve 最大 N=50 (`tab:oasst2_curve`, appendix:474)
   - **建议**: 改为 `$n \leq 50$`

5. **Discussion "zero-padding" 术语错误** (conclusion.tex:21)
   - 正文: "the −57.9 pp ActorAttack collapse under zero-padding"
   - 实际: 实验是用 **benign conversation turns** 填充，不是 zero-padding (appendix:795: "Padding experiments append benign turns after the complete attack sequence")
   - **建议**: 改为 "benign-turn padding" 或 "dilution padding"

6. **12--14 pp 范围略不精确** (experiments:217, conclusion:32, appendix:504)
   - 从 `tab:evidence_hierarchy`: DD .997→.855 = 14.2pp, AA .972→.842 = 13.0pp → 实际范围 13--14pp
   - 从 `tab:dual_ood`: DD .994→.855 = 13.9pp, AA .981→.842 = 13.9pp → 两者均 ~14pp
   - "12" 没有数据支撑。Minor issue，但如 #3 的 .997/.994 不一致被修正后范围会变

---

### ❌ 待确认

- **Discussion "all DAPT variants exceed vanilla by ≥40 pp" 是否应排除 Topic?** 如果 "DAPT variants" 语义上不含 Topic (因其被归类为 "misaligned supervision")，那范围应为 18--42pp，但 ≥40pp 仍然错误。需确认作者意图。

---

### Label/Ref 检查
- **Orphan labels**: 无
- **Broken refs**: 无

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_appendix-consistency_20260523T191656"
}
```

</details>

---
