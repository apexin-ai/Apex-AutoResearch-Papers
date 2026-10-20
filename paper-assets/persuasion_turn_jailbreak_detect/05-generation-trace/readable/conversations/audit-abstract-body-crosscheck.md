# audit abstract body crosscheck

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_audit_abstract-body-crosscheck_20260523T191628.jsonl`
- **Structured JSON:** [`6a6eb2760dd1d0d28c9a.json`](../../sessions/6a/6a6eb2760dd1d0d28c9a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-23T19:26:45.927676+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read all paper tex files",
  "subagent_type": "Explore",
  "prompt": "Read the following files in full and return their complete contents. These are LaTeX paper files:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex\n4. /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex\n5. /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex\n\nI need the COMPLETE content of each file, including all tables, figures, and numerical data. Read each file fully (use large limits if needed). Return all content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Agent",
  "tool_args": {
    "description": "Read all paper tex files",
    "subagent_type": "Explore",
    "prompt": "Read the following files in full and return their complete contents. These are LaTeX paper files:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex\n2. /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex\n3. /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex\n4. /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex\n5. /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex\n\nI need the COMPLETE content of each file, including all tables, figures, and numerical data. Read each file fully (use large limits if needed). Return all content."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-23T19:26:45.928028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex",
  "limit": "50000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/abstract.tex",
    "limit": "50000"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-23T19:26:45.928217+00:00_

1	% abstract.tex
2	\begin{abstract}
3	Multi-turn jailbreak attacks spread adversarial intent across benign-seeming turns. Existing defenses fail to generalize: Llama Guard~3 detects only 1.8\% of multi-turn jailbreaks zero-shot in our evaluation. Detecting such attacks benefits substantially from domain adaptation at base model scale, but the form of adaptation matters. We isolate the factors behind cross-attack generalization through controlled ablation: thirteen encoder configurations at base scale (125M--184M parameters) on synthetic multi-turn data decompose contributions of domain exposure, classification supervision, and label granularity across three out-of-distribution (OOD) attack families. On synthetic data, classification-based adaptation recovers OOD detection (F1\,=\,0.97--1.0 vs.\ vanilla 0.26--0.31; attack-side OOD, IID benign upper bound) while unsupervised pretraining collapses; under mixed-LLM training, template attacks remain detectable but strategy-diverse attacks degrade to chance level (F1\,=\,0.504). On human-authored single-turn data (ToxicChat), this hierarchy reverses: masked language modeling outperforms 9-class classification (F1 0.837 vs.\ 0.596). Classification adaptation's advantage is thus condition-specific rather than universal. Orthogonal to attack-side generalization, few-shot benign adaptation reduces false-positive rates from 58--68\% to 0--1.5\%, with 24.3$\times$ inference speedup (43$\times$ fewer parameters) over LLM-as-judge baselines.
4	\end{abstract}
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-23T19:26:45.928364+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex",
  "limit": "50000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/introduction.tex",
    "limit": "50000"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-23T19:26:45.928507+00:00_

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
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-23T19:26:45.928702+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex",
  "limit": "50000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex",
    "limit": "50000"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-23T19:26:45.928891+00:00_

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
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-23T19:26:45.929051+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex",
  "limit": "50000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/conclusion.tex",
    "limit": "50000"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-23T19:26:45.929190+00:00_

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
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-23T19:26:45.929338+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
  "limit": "50000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
    "limit": "50000"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-23T19:26:45.929730+00:00_

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
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T19:26:45.930088+00:00_

Here are the complete contents of all five LaTeX paper files:

---

## 1. abstract.tex

```latex
% abstract.tex
\begin{abstract}
Multi-turn jailbreak attacks spread adversarial intent across benign-seeming turns. Existing defenses fail to generalize: Llama Guard~3 detects only 1.8\% of multi-turn jailbreaks zero-shot in our evaluation. Detecting such attacks benefits substantially from domain adaptation at base model scale, but the form of adaptation matters. We isolate the factors behind cross-attack generalization through controlled ablation: thirteen encoder configurations at base scale (125M--184M parameters) on synthetic multi-turn data decompose contributions of domain exposure, classification supervision, and label granularity across three out-of-distribution (OOD) attack families. On synthetic data, classification-based adaptation recovers OOD detection (F1\,=\,0.97--1.0 vs.\ vanilla 0.26--0.31; attack-side OOD, IID benign upper bound) while unsupervised pretraining collapses; under mixed-LLM training, template attacks remain detectable but strategy-diverse attacks degrade to chance level (F1\,=\,0.504). On human-authored single-turn data (ToxicChat), this hierarchy reverses: masked language modeling outperforms 9-class classification (F1 0.837 vs.\ 0.596). Classification adaptation's advantage is thus condition-specific rather than universal. Orthogonal to attack-side generalization, few-shot benign adaptation reduces false-positive rates from 58--68\% to 0--1.5\%, with 24.3$\times$ inference speedup (43$\times$ fewer parameters) over LLM-as-judge baselines.
\end{abstract}
```

---

## 2. introduction.tex

```latex
% introduction.tex

\section{Introduction}

Multi-turn jailbreak attacks distribute adversarial intent across individually benign turns. Crescendo~\citep{russinovich2024crescendo}, Foot-in-the-Door~\citep{fitd2024}, and Deceptive Delight~\citep{deceptivedelight2024} all rely on persuasion as their core mechanism: \citet{zeng2024pap} catalogue 40 
…[truncated 30439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Agent",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T19:26:45.930275+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T19:26:45.930495+00:00_

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
…[truncated 10762 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T19:26:45.930678+00:00_

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
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T19:26:45.930913+00:00_

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
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T19:26:45.931093+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
  "offset": "200",
  "limit": "250"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
    "offset": "200",
    "limit": "250"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T19:26:45.931323+00:00_

200	\end{figure}
201	
202	\section{Cross-LLM Validation}
203	\label{app:cross_llm}
204	
205	\begin{table}[ht]
206	\centering
207	\footnotesize
208	\caption{Cross-LLM validation (F1, full conversation). All models are trained on Qwen3-8B data; conditions vary the source of jailbreak (JB) and benign (ben.) conversations at inference. Values are evaluated under a matched 50-sample subset protocol and differ from Table~\ref{tab:evidence_hierarchy}, which uses the full evaluation set.}
209	\label{tab:cross_llm}
210	\begin{tabular}{@{}lcccccc@{}}
211	\toprule
212	& \multicolumn{3}{c}{\textit{DD Full}} & \multicolumn{3}{c}{\textit{AA Full}} \\
213	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
214	\textbf{Condition} & Van. & MLM & 9-cl. & Van. & MLM & 9-cl. \\
215	\midrule
216	Qwen JB + Qwen ben. & .312 & .914 & .997 & .258 & .893 & .972 \\
217	Llama JB + Llama ben. & .261 & .282 & .433 & .261 & .368 & .321 \\
218	Llama JB + Qwen ben. & .302 & .778$^{*}$ & 1.000 & .302 & .903 & .801 \\
219	\bottomrule
220	\end{tabular}
221	\vspace{-2pt}
222	{\footnotesize $^{*}$High seed variance (std = 0.306): seed 456 outlier (F1 = 0.345); remaining two seeds achieve F1 $\geq$ 0.97.}
223	\end{table}
224	
225	Table~\ref{tab:cross_llm} shows three inference conditions. When both jailbreak and benign text come from Llama (row~2), all variants collapse (F1 = 0.26--0.43), but this conflates two sources of distribution shift: unfamiliar jailbreak patterns and unfamiliar benign text. Row~3 isolates jailbreak transferability by pairing Llama jailbreaks with the original Qwen benign distribution. Under this condition, 9-class recovers to F1 = 1.000 on DD and 0.801 on ActorAttack, and JB-MLM reaches 0.903 on ActorAttack. The contrast between rows~2 and~3 shows that the dominant failure mode in row~2 is benign distribution mismatch (false positives from unfamiliar benign text), not inability to recognize cross-LLM jailbreak patterns. Vanilla remains at 0.26--0.31 across all conditions, further confirming th
…[truncated 16429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T19:26:45.931471+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
  "offset": "430",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
    "offset": "430",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T19:26:45.931696+00:00_

430	
431	End-to-end fine-tuning unfreezes the Stage-1 encoder during Stage-2 BiGRU training, allowing gradient flow through the full pipeline. On IID and OOD DD, the two configurations are indistinguishable; on structurally complex ActorAttack, E2E recovers +5.8\,pp. The modest gain confirms that frozen probing captures the vast majority of discriminative information encoded by Stage-1 DAPT, and that the remaining OOD gap in the frozen setting reflects downstream optimization constraints rather than missing representational capacity.
432	
433	\section{Real-World False Positive Rate}
434	\label{app:wildchat_fpr}
435	
436	\begin{table}[ht]
437	\centering
438	\footnotesize
439	\caption{False positive rate (\%) on 226 WildChat benign multi-turn conversations (GPT-3.5 users, avg 7.4 turns per conversation). All models trained on synthetic Qwen3-8B data (1{,}000-conversation scale). 3-seed mean$\pm$std.}
440	\label{tab:wildchat_fpr}
441	\begin{tabular}{@{}lcccc@{}}
442	\toprule
443	\textbf{Variant} & Seed 42 & Seed 123 & Seed 456 & Mean$\pm$Std \\
444	\midrule
445	9-class & 66.8 & 61.1 & 76.5 & 68.1$\pm$6.4 \\
446	MLM & 36.7 & 64.6 & 32.3 & 44.5$\pm$14.3 \\
447	Vanilla & 47.3 & 42.5 & 54.4 & 48.1$\pm$4.9 \\
448	\bottomrule
449	\end{tabular}
450	\end{table}
451	
452	Table~\ref{tab:wildchat_fpr} evaluates false positive rates on 226 WildChat benign multi-turn conversations from real GPT-3.5 users (avg 7.4 turns). All variants produce FPR far exceeding deployable thresholds: 9-class is worst at 68.1\%, followed by vanilla (48.1\%) and MLM (44.5\%). Domain adaptation \emph{increases} FPR relative to vanilla (+20\,pp for 9-class), indicating that continued pretraining amplifies dependence on the training benign distribution. This is consistent with the cross-LLM false positive spike (Table~\ref{tab:cross_llm_error}): models trained on synthetic Qwen3-8B benign text implicitly treat unfamiliar conversational styles as jailbreak indicators. High MLM seed variance (std\,=\,14.3\%
…[truncated 12792 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T19:26:45.931853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
  "offset": "600",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
    "offset": "600",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T19:26:45.932074+00:00_

600	FITD OOD & Last turn & 1.000 & .927 \\
601	\bottomrule
602	\end{tabular}
603	\vspace{-2pt}
604	{\footnotesize Mean $\Delta$ (9-class $-$ MLM): Full +1.6\,pp, Last turn +6.0\,pp. 9-class advantage widens under truncation across all families, indicating the reversal on ToxicChat is driven by distributional differences between synthetic and human text, not by multi-turn structural dependence.}
605	\end{table}
606	
607	\paragraph{Representation geometry analysis.}
608	\label{app:representation}
609	
610	To characterize the mechanism behind classification DAPT's robustness, we analyze Stage-1 representations across all seven DeBERTa-v3-base variants (seed 42). We extract \texttt{[CLS]} embeddings from 150 test conversations (50 IID + 50 DD OOD + 50 AA OOD) and compute three metrics.
611	
612	\begin{table}[ht]
613	\centering
614	\footnotesize
615	\caption{Representation geometry and class separability across Stage-1 variants. PR: participation ratio (effective dimensionality of the embedding space). Fisher ratio: inter-class distance$^2$ / sum of intra-class variances. Weight $\Delta$: L2 distance from pretrained weights (relative to pretrained norm).}
616	\label{tab:representation}
617	\begin{tabular}{@{}lccc@{}}
618	\toprule
619	\textbf{Variant} & \textbf{PR} & \textbf{Fisher} & \textbf{Wt.\ $\Delta$ (\%)} \\
620	\midrule
621	Vanilla & 31.9 & $<$0.001 & 0.000 \\
622	Wiki-MLM & 25.0 & $<$0.001 & 0.221 \\
623	JB-MLM & 24.6 & $<$0.001 & 0.256 \\
624	Topic & 14.5 & 0.012 & 0.371 \\
625	Scrambled & 7.8 & 2.60 & 0.283 \\
626	9-class & 9.4 & 4.47 & 0.303 \\
627	Binary & 3.7 & 19.7 & 0.239 \\
628	\bottomrule
629	\end{tabular}
630	\end{table}
631	
632	Classification variants compress representations into 2--9 effective dimensions (vs.\ 25--32 for MLM/vanilla) while increasing Fisher ratio by 3--5 orders of magnitude. Weight distances from pretrained are comparable across all variants ($\sim$0.2--0.4\%), indicating that the mechanism is representational restructuring rather t
…[truncated 12891 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T19:26:45.932232+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
  "offset": "790",
  "limit": "160"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/persuasion_turn_jailbreak_detect/docs/paper/appendix.tex",
    "offset": "790",
    "limit": "160"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T19:26:45.932422+00:00_

790	
791	Truncating benign conversations to match jailbreak turn counts (Part~A) produces zero false positives across all truncation levels and all 3 seeds, directly confirming that the model does not use conversation length as a detection shortcut. $K$=3 and $K$=5 are the effective control conditions where all 38 conversations were truncated; $K$=10 exceeds the maximum test benign length and serves as a no-op control.
792	
793	WildChat FPR by turn count (Part~B) provides complementary evidence: short conversations (3--10 turns, $n$=196) have \emph{lower} FPR than medium-length ones (11--15 turns, $n$=23), inconsistent with a ``short\,=\,jailbreak'' shortcut. Medium and long buckets have limited sample sizes and should be interpreted as directional evidence only.
794	
795	Padding jailbreak conversations with benign turns (Part~C) reveals an asymmetry: DD detection is resilient ($\Delta$=$-$2.5\,pp), but ActorAttack collapses ($\Delta$=$-$57.9\,pp). Padding experiments append benign turns \emph{after} the complete attack sequence; in practice, adversaries would not dilute their own successful attacks. The collapse nonetheless exposes BiGRU temporal aggregation as vulnerable to attention dilution on subtle attack signals, a limitation discussed in Section~\ref{sec:limitations}.
796	
797	\section{Inference Efficiency}
798	\label{app:efficiency}
799	
800	\begin{table}[ht]
801	\centering
802	\footnotesize
803	\caption{Inference efficiency comparison. DeBERTa+BiGRU and TF-IDF+LR measured on IID test (76 conversations, avg 8.3 turns, single A100). LLM latency from separate OOD evaluation (118 conversations; exp10); cross-condition comparison is indicative only.}
804	\label{tab:efficiency}
805	\begin{tabular}{@{}lrcr@{}}
806	\toprule
807	\textbf{Method} & Latency (ms) & Params & VRAM \\
808	\midrule
809	TF-IDF+LR & 0.43$\pm$0.05 & $\sim$10K & CPU \\
810	DeBERTa+BiGRU (ours) & 12.1$\pm$1.2 & 186.7M & 862\,MB \\
811	Qwen3-8B 3-shot$^{\dagger}$ & $\sim$5{,}200 & 8B & $\sim$16\
…[truncated 9151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-23T19:26:45.932850+00:00_

Now I have all the data needed for cross-referencing. Let me compile the report.

## Abstract + 正文数字交叉核对报告

### ✅ 已核对一致

- **"F1=0.97--1.0"** in abstract.tex:6 ← Table 2 (evidence_hierarchy): 9-class DD-Full=.997, AA-Full=.972, FITD=1.000; range 0.972–1.000 rounds to 0.97–1.0
- **"vanilla 0.26--0.31"** in abstract.tex:6 ← Table 2: Vanilla DD=.312, AA=.258 → 0.258–0.312 ≈ 0.26–0.31
- **"F1=0.504"** in abstract.tex:6 ← Table 5 (mixed_llm): 9-class AA OOD = .504±.107
- **"0.837 vs 0.596"** in abstract.tex:6 ← Table 6 (human_data): JB-MLM=.837±.013, 9-class=.596±.087
- **"58--68%"** FPR in abstract.tex:6 ← OASST2 baseline FPR=57.5%≈58%, WildChat 9-class FPR=68.1%
- **"24.3×"** speedup in abstract.tex:6 ← Appendix efficiency (line 818): exp46 matched comparison 318.53ms/13.12ms=24.3×
- **"43×"** fewer parameters in abstract.tex:6 ← 8B(Qwen3-8B)/186.7M(DeBERTa+BiGRU)=42.85≈43×
- **"1.8%"** Llama Guard in abstract.tex:4 / experiments.tex:23 ← 5/278 pooled recall = 1.8%; 278 = 38(Crescendo)+80(DD)+80(FITD)+80(AA)
- **"0.312 on OOD Deceptive Delight"** in introduction.tex:14 ← Table 1: Vanilla DD-Full=.312±.026
- **"0.818"** mixed-LLM 9-class in conclusion.tex:8 ← Table 5: 9-class DD OOD=.818±.096
- **"AA=1.000 vs 9-class 0.946"** RoBERTa-large in conclusion.tex:8 ← Table 4 (cross_encoder): RoBERTa-large vanilla AA=1.000, 9-class AA=.946
- **"68.1%"** WildChat FPR in conclusion.tex:8 / experiments.tex:217 ← Table wildchat_fpr: 9-class Mean=68.1±6.4%
- **"F1=0.541±0.207"** topic OOD in conclusion.tex:5 ← Table 2: Topic DD-Full=.541±.207
- **"within 3.9 pp"** scrambled labels in conclusion.tex:5 ← Table 2 AA: Binary=.990, Scrambled=.951 → max gap=3.9 pp
- **"participation ratio 3.7--9.4 vs 25--32"** in conclusion.tex:5 ← Table representation: Binary PR=3.7, 9-class=9.4; JB-MLM=24.6, Vanilla=31.9
- **"−57.9 pp"** zero-padding collapse in conclusion.tex:12 ← Table length_independence Part C: AA padded Δ=−57.9 pp
- **"Δ≤1 pp"** mean pooling vs BiGRU in conclusion.tex:8 ← Table temporal: Frozen max gap=1.0 pp (AA: .972 vs .962)
- **"N=155"** length-matched in conclusion.tex:12 ← Table length_independence: 80 jailbreak + 75 benign = 155
- **"κ=0.78"** in experiments.tex:211 / conclusion.tex:27 ← Appendix strategy heatmap caption: κ=0.78
- **"184M vs 355M"** in conclusion.tex:27 ← DeBERTa-v3-base=184M, RoBERTa-large=355M
- **"125M--355M"** in conclusion.tex:27 ← RoBERTa-base=125M to RoBERTa-large=355M
- **"12--14 pp"** dual-OOD drop in conclusion.tex:24 ← Table dual_ood: WildChat drops ~14 pp, OASST2 drops ~12 pp → range 12–14 pp
- **"~60 pp from vanilla"** MLM bridge in experiments.tex:117 ← .914−.312=.602≈60 pp
- **"71 pp gap"** TF-IDF vs 9-class in experiments.tex:60 ← .972−.261=.711≈71 pp
- **"3--23× lower cross-seed variance"** in experiments.tex:119 ← AA: .080/.026≈3×; DD: .115/.005=23×
- **"d=−0.14 on DD, d≈0 on FITD"** TOST in introduction.tex:27 ← Table tost_sensitivity: DD d=−0.136, FITD d=0.000
- **"d=0.44"** ActorAttack in introduction.tex:27 / experiments.tex:118 ← Table tost_sensitivity: AA d=0.440
- **"0.628→0.312"** vanilla DD degradation in experiments.tex:59 ← Table full_prefix: Vanilla DD K=1=.628, Full=.312

---

### ⚠️ 不一致

1. **Introduction "over 60 percentage points" classification vs MLM** (introduction.tex:22)
   - 期望: classification vs MLM 最大差值 ~53 pp (mixed-LLM DD: .818−.289=52.9 pp)
   - 实际: "over 60 pp" 的差距是 classification vs **vanilla** (.997−.312=68.5 pp), 不是 vs MLM
   - → 需修复: 改为 "over 60 percentage points over vanilla" 或 "over 50 percentage points over MLM"

2. **Discussion "all DAPT variants exceed vanilla by ≥40 pp on ToxicChat"** (conclusion.tex:8)
   - 期望: 所有 DAPT 变体 ≥40 pp
   - 实际: Table 6 数据 — JB-MLM 42.4pp ✓, Wiki-MLM 37.8pp ✗, Binary 29.2pp ✗, Scrambled 20.3pp ✗, 9-class 18.3pp ✗, Topic 8.3pp ✗
   - → 需修复: 改为 "18--42 pp" 或 "all jailbreak-domain DAPT variants exceed vanilla"

3. **Discussion "DD/AA Δ ≤ 2.5 pp" for length-matched** (conclusion.tex:12)
   - 期望: DD 和 AA 都 ≤2.5 pp
   - 实际: Table length_independence Part C — DD Δ=−2.5pp ✓, AA Δ=−57.9pp ✗
   - 且下一句就说 "−57.9 pp ActorAttack collapse", 前后矛盾
   - → 需修复: 改为 "DD $\Delta \leq$ 2.5 pp" 去掉 "/AA", 或明确说 "DD shows negligible change ($\Delta$=−2.5 pp) while AA collapses"

4. **experiments.tex "25 OASST2 to 1.0%" vs appendix table 1.5%** (experiments.tex:217)
   - 期望: 与 OASST2 adaptation curve 表一致
   - 实际: Appendix Table oasst2_curve 行 N=25 → FPR=1.5%（不是 1.0%）
   - Abstract 和 conclusion 写 "0--1.5%" 与表一致; experiments.tex 写 "1.0%" 不一致
   - → 需修复: experiments.tex 改为 "25 OASST2 to 1.5\%"

5. **Appendix full_prefix 9-class DD-Full = .994 vs 主表 .997** (appendix.tex:56 vs experiments.tex:48,86)
   - Table 1 (main_results): .997±.005; Table 2 (evidence_hierarchy): .997±.005
   - Appendix Table full_prefix: .994±.005
   - Seed-level 数据 (s42=1.000, s123=1.000, s456=.990) → mean=.997, 确认主表正确
   - → 需修复: Appendix full_prefix 的 DD-Full 从 .994 改为 .997 (或核实是否使用了不同 checkpoint)

6. **Abstract "base scale (125M--184M)" vs Introduction "three scales (125--355M)"** (abstract.tex:4 vs introduction.tex:27)
   - Abstract: "thirteen encoder configurations at base scale (125M--184M parameters)"
   - Introduction: "thirteen encoder configurations at three scales (125--355M)"
   - 13个配置含 3 个 RoBERTa-large (355M), 不全是 base scale
   - → 需修复: abstract 改为 "at base to large scale (125M--355M)" 或与 introduction 一致

7. **experiments.tex "All DAPT variants exceed vanilla by 18--42 pp"** (experiments.tex:205)
   - Topic 也是 DAPT 变体, 但 Topic−Vanilla = 8.3 pp (< 18 pp)
   - → 需修复: 改为 "Most DAPT variants exceed vanilla by 18--42 pp" 或注明排除 Topic

8. **Discussion "label-free MLM detection (F1≥0.97)" 缺少限定** (conclusion.tex:5)
   - MLM DD-Full = 0.914±0.115 (< 0.97); 仅 K≤5 时 ≥0.97
   - experiments.tex 正确限定为 "MLM recovers to ≥0.97 at K≤5"
   - → 需修复: Discussion 应加限定 "at early prefixes" 或 "at K≤5"

9. **Conclusion "with 10 conversations" 过度简化** (conclusion.tex:17)
   - WildChat: N=10 → 0% ✓; OASST2: N=25 → 1.5% (不是 N=10)
   - Introduction 正确写 "10--25 conversations"
   - → 需修复: 改为 "with 10--25 conversations"

10. **Limitations "n ≤ 49"** (conclusion.tex:24)
    - OASST2 表最大 N=50, WildChat 实验也有大样本
    - 不清楚 49 的来源
    - → 需确认: 如果指 adaptation 用的最大 conversation 数, 应为 n≤50

---

### ❌ 无法溯源

- **"0.191--0.449 F1 (across prefix lengths)"** in introduction.tex:14 — GPT-5.5 per-prefix F1 不在任何表中; LLM-judge 表仅有 full-conversation F1=.383. Full 值落在声称范围内但无法验证两端.

---

### 四舍五入一致性

- **0.97 vs 0.972**: Abstract/Conclusion 写 "F1=0.97--1.0", 实际 9-class AA-Full=.972. 作为范围下界, 0.97 是 0.972 的合理简写. ✓
- **0.26 vs 0.258**: Vanilla AA=.258 简写为 0.26. 一致. ✓
- **0.31 vs 0.312**: Vanilla DD=.312 简写为 0.31. 一致. ✓
- **58% vs 57.5%**: OASST2 FPR=57.5% 取整为 58%. 一致. ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_abstract-body-crosscheck_20260523T191628"
}
```

</details>

---
