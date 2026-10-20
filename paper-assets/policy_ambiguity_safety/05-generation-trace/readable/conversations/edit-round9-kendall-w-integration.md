# edit round9 kendall w integration

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 77
- **Recorded user turns:** 0
- **Tool calls:** 38
- **Original source:** `logs/chats/worker_edit_round9_kendall_w_integration_20260521T185400.jsonl`
- **Structured JSON:** [`bc3d351388910122b874.json`](../../sessions/bc/bc3d351388910122b874.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

77 recorded events

### Tool call

_source line 1 · 2026-05-21T18:59:50.061685+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T18:59:50.062037+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	\usepackage{graphicx}
9	\usepackage{booktabs}
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{multirow}
13	\usepackage{xcolor}
14	\usepackage{subcaption}
15	
16	\definecolor{speccolor}{HTML}{C44E52}
17	\definecolor{lingcolor}{HTML}{4C72B0}
18	
19	\title{Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM Agents}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	\input{sections/introduction}
28	\input{sections/related_work}
29	\input{sections/taxonomy}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/analysis}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	\input{sections/limitations}
36	
37	\bibliography{references}
38	
39	\appendix
40	\input{sections/appendix}
41	
42	\end{document}
43	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T18:59:50.062239+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T18:59:50.062434+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around four analyses of increasing specificity: the binary ambiguity effect (C1), the type hierarchy (C2), the aggregate layer effect (C3), and the model$\times$type interaction (C4). C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory but provides the model$\times$type interaction analysis.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). Clause identity explains 22.4\% of variance versus 1.0\% for model identity. A replication on two additional model families (Gemini-2.5-Flash, LLaMA-4-Scout; Appendix~\ref{app:model_expansion}) confirms the effect across seven models spanning six providers ($\Delta = +20.0$ to $+33.6$\,pp, both $p < 10^{-6}$).
9	
10	\subsection{Type Hierarchy (C2)}
11	
12	\begin{table*}[t]
13	\centering
14	\caption{Violation rates (\%) under ambiguous policy clauses by type and model. $\Delta$pp denotes the pooled difference between ambiguous and unambiguous conditions across all five models. All per-type differences are significant ($p < 10^{-5}$, Fisher's exact test).}
15	\label{tab:main_results}
16	\small
17	\begin{tabular}{llrrrrrrrr}
18	\toprule
19	Layer & Type & Pooled & GPT-5.4 & GPT-4.1 & Claude & Qwen3 & DeepSeek & $\Delta$pp & $p$ \\
20	\midrule
21	\multirow{3}{*}{\textcolor{speccolor}{Spec.}} & Incompleteness & 53.6 & 46.0 & 58.0 & 48.0 & 62.0 & 54.0 & +49.2 & $<10^{-37}$ \\
22	 & Auth.\ Scope & 41.6 & 64.0 & 46.0 & 12.0 & 26.0 & 60.0 & +36.0 & $<10^{-22}$ \\
23	 & Cond.\ Precedence 
…[truncated 6240 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T18:59:50.062672+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T18:59:50.062921+00:00_

1	\section{TOST Equivalence Sensitivity}
2	\label{app:tost}
3	
4	Table~\ref{tab:tost_sensitivity} reports the TOST equivalence analysis \citep{lakens_2017} across seven margins. Three pairs involving incompleteness never reach equivalence even at $\pm 20$ pp: conditional precedence--incompleteness ($\Delta = 16.8$ pp), coreferential--incompleteness ($\Delta = 22.0$ pp), and incompleteness--scopal ($\Delta = 14.2$ pp).
5	
6	\begin{table}[!ht]
7	\centering
8	\small
9	\caption{TOST equivalence sensitivity across margins. Mid-tier = fraction of the six within-cluster pairs (lexical, auth.\ scope, scopal, cond.\ prec.) that are equivalent. Inc.\ and Cor.\ columns indicate separation from the mid-tier cluster.}
10	\label{tab:tost_sensitivity}
11	\begin{tabular}{lcccc}
12	\toprule
13	Margin & Equiv.\ pairs & Mid-tier & Inc.\ sep. & Cor.\ sep. \\
14	\midrule
15	$\pm 5$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
16	$\pm 8$ pp & 0/15 & 0/6 & \checkmark & \checkmark \\
17	$\pm 10$ pp & 3/15 & 3/6 & \checkmark & \checkmark \\
18	$\pm 12$ pp & 5/15 & 5/6 & \checkmark & \checkmark \\
19	$\pm 15$ pp & 8/15 & 6/6 & \checkmark & -- \\
20	$\pm 18$ pp & 9/15 & 6/6 & \checkmark & -- \\
21	$\pm 20$ pp & 12/15 & 6/6 & -- & -- \\
22	\bottomrule
23	\end{tabular}
24	\end{table}
25	
26	\section{Mitigation Experiment}
27	\label{app:mitigation}
28	
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). Coreferential pairs are excluded because their ambiguous and unambiguous variants differ only in pronoun resolution, making it impossible to craft targeted mitigation instructions without revealing the experimental manipulation. The treatment appends a type-specific disambiguation instruction to the agent's system prompt. Control rates are the matched 5-type subset from the full study (\S\ref{sec:results}).
30	
31	\begin{table*}[!ht]
32	
…[truncated 15626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T18:59:50.063076+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T18:59:50.063251+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity.}
5	\citet{berry_kamsties_2004} distinguish nocuous from innocuous ambiguity. Our results can be interpreted through a \emph{differential nocuity} lens: risk depends on ambiguity type (base vulnerability), safety training (selective mitigation), and disambiguation channel availability. This generates two testable predictions: (P1) types with explicit decision points should show larger safety-training gains than gap-filling types; (P2) disambiguation channels should reduce violations more for high-deficit types. Our mitigation experiment (Appendix~\ref{app:mitigation}) is consistent with, though not a formal test of, P1 ($-18.0$\,pp for authorization scope vs.\ $-3.4$\,pp for incompleteness).
6	
7	\paragraph{Practical implications.}
8	A proof-of-concept classifier (Appendix~\ref{app:detection}) achieves F1\,=\,0.81 for binary ambiguity detection but only 0.34 for incompleteness---the highest-risk type is the hardest to detect. With agents exhibiting disambiguation deficit in $>$89\% of cases, type-aware auditing and externalized detection \citep{chantree_2006,ferrari_ambiguity_2019} are necessary for policy-governed deployments.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T18:59:50.063404+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T18:59:50.063550+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A customer asks to return a customized item within the 30-day window. The agent consults the store policy, which states that ``items may be returned within 30 days.'' The word ``items'' scopes over all product categories, including custom orders that are normally final sale. The agent grants a full refund and arranges free return shipping. One word of scopal ambiguity costs the retailer \$200.
5	
6	LLM-based agents increasingly operate under natural-language policy specifications that govern their permitted actions. These specifications inevitably contain ambiguity: a property that has been studied for decades in requirements engineering (RE) and computational linguistics. \citet{berry_kamsties_2004} distinguish between \emph{nocuous} (i.e., harmful) ambiguity, where different stakeholders arrive at different interpretations, and \emph{innocuous} ambiguity, where shared organizational context ensures convergent interpretation. In human RE workflows, most ambiguity is innocuous because developers share domain knowledge, can consult colleagues, and iteratively clarify requirements.
7	
8	LLM agents lack these disambiguation channels. They cannot consult colleagues, rarely escalate to users, and must resolve ambiguity in real time from the text alone. This raises a question that has not been empirically addressed: does policy ambiguity cause safety violations in LLM agents, and if so, does the \emph{type} of ambiguity predict the severity of the violation? Prior work classifies ambiguity types in policies \citep{drip_r_2026,li_ambiguity_taxonomy_2024} or measures policy understanding quality \citep{policybank_2026}, but no existing study provides a causal, type-granularity mapping from ambiguity to safety violations.
9	
10	\begin{figure*}[t]
11	\centering
12	\includegraphics[width=\textwidth]{figures/fig1_overview.pdf}
13	\caption{Experimental overview. We construct 300 matched clause pairs across a six-type, two-
…[truncated 2016 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T18:59:50.063708+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T18:59:50.063864+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Experimental Platform}
5	
6	We conduct all experiments on the original release of $\tau^2$-bench \citep{tau2_bench_2025}, a dual-control conversational agent benchmark spanning retail and airline customer service domains. $\tau^2$-bench provides natural-language policy documents, tool APIs, and multi-turn user interactions with ground-truth evaluation via assertion checking. Its policy injection mechanism allows us to replace individual policy clauses while preserving the surrounding context, enabling controlled ambiguity manipulation.
7	
8	\subsection{Matched-Pair Design}
9	
10	For each of the six ambiguity types, we construct 50 \emph{clause pairs}: an ambiguous variant and a matched unambiguous variant that conveys the same intended policy but resolves the ambiguity. Pairs are minimal edits: the unambiguous variant adds only the information necessary to eliminate the target ambiguity (e.g., for scopal ambiguity, replacing ``items may be returned within 30 days'' with ``standard items may be returned within 30 days; customized items are final sale''). This yields 300 clause pairs $\times$ 2 conditions $\times$ 5 models $= 2{,}997$ episodes (3 episodes lost to API errors in one Qwen3 batch).
11	
12	Clause pairs are generated through a template-based pipeline and reviewed by two independent annotators (both with NLP background) to ensure (1) the ambiguous variant contains exactly one instance of the target type, (2) the unambiguous variant resolves it without changing policy scope, and (3) the ambiguity is plausibly natural. Annotators independently verified type assignments with a 96\% pass rate; disagreements were resolved by discussion. A post-hoc realism validation confirms linguistic consistency with original $\tau^2$-bench policy text (\S\ref{sec:limitations}).
13	
14	\subsection{Models}
15	
16	We evaluate five models spanning four providers and two architecture families: GPT-5.4 and GPT-4.1 (OpenAI, pro
…[truncated 5193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T18:59:50.064010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/taxonomy.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T18:59:50.064171+00:00_

1	\section{Ambiguity Taxonomy}
2	\label{sec:taxonomy}
3	
4	We adopt an operational definition of ambiguity following \citet{wasow_ambiguity_2005}: a policy clause is ambiguous when it admits multiple distinct interpretations available to a competent reader, including cases of vagueness where the boundary between interpretations is gradient rather than discrete \citep{kennedy_vagueness_2007}.
5	
6	Our taxonomy comprises six types organized into two layers, drawing on \citet{li_ambiguity_taxonomy_2024}'s NLP taxonomy (11 types), \citet{massey_ambiguity_re_2014}'s requirements engineering taxonomy (6 types), and the concurrent DRIP-R benchmark \citep{drip_r_2026} (5 types). We select types based on two criteria: frequency in operational policy documents (assessed via manual audit of $\tau^2$-bench policies) and theoretical distinctiveness (each type maps to a different resolution mechanism).
7	
8	\paragraph{Linguistic layer.} These types operate at the syntactic or semantic level and can, in principle, be resolved by parsing or contextual cues within the text.
9	\begin{itemize}
10	\item \textbf{Scopal}: quantifier, negation, or modal scope interactions (e.g., ``all items may not be returned'' admits universal-negation and negation-of-universal readings).
11	\item \textbf{Lexical}: polysemy or homonymy (e.g., ``charge'' as financial cost vs.\ penalty; ``party'' as individual vs.\ group).
12	\item \textbf{Coreferential}: unclear pronoun or noun-phrase reference (e.g., ``the agent should verify the customer's identity before processing their refund request, which must be approved by a supervisor'' where ``which'' could refer to the verification or the refund).
13	\end{itemize}
14	
15	\paragraph{Specification layer.} These types arise from pragmatic or discourse-level gaps that require domain knowledge or organizational context to resolve.
16	\begin{itemize}
17	\item \textbf{Authorization scope}: vague permission or role boundaries (e.g., ``authorized personnel may issue r
…[truncated 2007 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T18:59:50.064347+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T18:59:50.064478+00:00_

1	\section{Conclusion}
2	
3	Ambiguous policy clauses increase agent safety violations by 34.0\,pp (OR\,$=$\,15.1) across five models, with clause identity explaining 22$\times$ more variance than model identity. The two-tier type hierarchy replicates across seven models ($\rho = 0.60$--$0.90$). With agents exhibiting disambiguation deficit in over 89\% of cases, type-aware auditing and externalized detection are critical for policy-governed deployments.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T18:59:50.064601+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T18:59:50.064738+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	\paragraph{Model coverage.} We evaluate seven API-accessible models from six providers (four proprietary, three open-source; two in replication, Appendix~\ref{app:model_expansion}). Smaller open-source models (7B--70B parameters) may show different vulnerability patterns, and our findings may not generalize to models with fundamentally different training approaches.
5	
6	\paragraph{Domain scope.} $\tau^2$-bench covers retail and airline customer service. Policy ambiguity effects in other domains (healthcare, finance, legal) remain to be tested, though the within-study cross-domain consistency is encouraging: failure mode distributions share the same top-two modes (assumption-based action and unauthorized escalation) across domains, with individual mode base rates differing by up to 12.5 pp, likely reflecting domain policy structure rather than methodological artifacts.
7	
8	\paragraph{Synthetic ambiguity.} Our matched-pair design requires synthetic construction of ambiguous variants, which may not capture the full distribution of naturally occurring policy ambiguities. We mitigate this through expert review and a realism validation comparing ambiguous clauses against original $\tau^2$-bench policy text. Ambiguous clauses are indistinguishable from originals in lexical diversity (TTR, KS $p = 0.89$) and word length ($p = 0.09$). Readability is slightly higher (Flesch--Kincaid $d = 0.29$, $p = 0.006$) and sentence length moderately higher ($d = 0.74$), both reflecting the structural demands of encoding ambiguity in standalone clauses. Across matched pairs, disambiguation preserves readability (Flesch--Kincaid $d = 0.14$, $p = 0.10$), confirming that minimal edits change semantic precision without altering linguistic register.
9	
10	\paragraph{Cross-judge asymmetry.} Although our dual-judge calibration (\S\ref{sec:method}) shows no systematic bias ($p = 0.606$) and human validation confirms the LLM judge operates 
…[truncated 2965 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T18:59:50.064872+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T18:59:50.065009+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes: unauthorized escalation, assumption-based action, scope misapplication, arbitrary rule selection, and conservative refusal. GPT-5.4 and GPT-4.1 serve as detailed annotation anchors because they span the judge boundary. Inter-coder reliability is substantial (Gwet's AC$_1$ $= 0.62$ \citep{gwet_2014}; Cohen's $\kappa = 0.52$ \citep{cohen_1960}). The gap reflects the prevalence paradox: three categories account for ${\sim}$90\% of instances, compressing the $\kappa$ denominator and yielding artificially low values despite high raw agreement.
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse} (scope misapplication): the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002}---e.g., parsing ``items purchased with a coupon or during a sale are final'' as restricting only coupon purchases. This dominates scopal (all 5 models), conditional precedence (all 5), and coreferential (3/5).
13	
14	\emph{Information gap-filling} (assumption-based action): the agent fills missing information with plausible but incorrect defaults---e.g., inventing a 30-day return window when none is specified. This dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation} (unauthorized escalation): the agent exceeds permission boundaries when authorization scope is underspecified---e.g., issuing a refund above its stated limit rather than escalating; 69.2\% of such violations involve unauthorized esc
…[truncated 2108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T18:59:50.065150+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T18:59:50.065317+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Ambiguity in NLP and requirements engineering.}
5	Ambiguity has been studied extensively in both computational linguistics and software engineering. Word sense disambiguation \citep{navigli_wsd_2009} addresses lexical ambiguity at the token level; our lexical type extends this to policy-specific polysemy. \citet{li_ambiguity_taxonomy_2024} propose an 11-type NLP taxonomy covering syntactic, semantic, and pragmatic ambiguity, from which we draw our linguistic-layer types. In requirements engineering (RE), \citet{massey_ambiguity_re_2014} classify six ambiguity types in regulatory texts, and \citet{berry_kamsties_2004} introduce the distinction between nocuous ambiguity (where stakeholders diverge on interpretation) and innocuous ambiguity (where they converge). Computational detection of nocuous ambiguity has progressed from heuristic methods \citep{chantree_2006,willis_nocuous_2008} through NLP-based cross-domain detectors \citep{ferrari_ambiguity_2019,ferrari_defects_2018} to transformer-based approaches for anaphoric ambiguity \citep{ezzini_taphsir_2022,ezzini_anaphoric_2022}. \citet{zhao_nlp4re_2021} survey the broader NLP4RE landscape. Our work extends Berry and Kamsties' framework to LLM agents, where the absence of shared organizational context makes previously innocuous ambiguity nocuous.
6	
7	\paragraph{Psycholinguistics of ambiguity processing.}
8	\citet{ferreira_good_enough_2002} show that human comprehenders build shallow, ``good-enough'' representations rather than full parses, paralleling our observation that LLM agents adopt surface interpretations. \citet{frazier_rayner_1982} demonstrate early commitment to a single parse; \citet{li_garden_path_llm_2024} provide direct evidence that LLMs exhibit analogous garden-path effects. \citet{liu_ambiguity_2023} demonstrate that language models fail to represent ambiguity, collapsing multiple interpretations into a single output. These findings
…[truncated 2322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T18:59:50.065461+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T18:59:50.065586+00:00_

1	\begin{abstract}
2	LLM-based agents operate under natural-language policy specifications that inevitably contain ambiguity, yet the causal relationship between ambiguity type and safety violations remains unmeasured. We present a matched-pair study on $\tau^2$-bench with 300 clause pairs spanning a six-type ambiguity taxonomy, evaluated across five models (2,997 episodes). Three findings emerge. First, ambiguous clauses increase violation rates by 34.0 percentage points (OR $= 15.1$), with a perturbation control supporting ambiguity-specific causation. Second, a two-tier type hierarchy separates incompleteness (46--62\% violation rate across seven models) from the remaining five types, with type identity explaining 22$\times$ more variance than model identity (22.4\% vs.\ 1.0\%). Third, authorization scope shows the widest cross-model range (52\,pp, though measured with the lowest inter-judge agreement, $\kappa = 0.385$), suggesting that safety training may differentially mitigate specific ambiguity types. Agents show fewer than 11\% disambiguation awareness, adopting surface interpretations without flagging uncertainty. These results motivate type-aware policy auditing and externalized ambiguity detection for policy-governed agent deployments.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T18:59:50.065796+00:00_

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
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
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

_source line 26 · 2026-05-21T18:59:50.065930+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T18:59:50.066073+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': \"Add Kendall's W sentence to §5.2 (experiments.tex)\", 'status': 'in_progress', 'activeForm': \"Adding Kendall's W sentence to experiments.tex\"}, {'content': \"Add Kendall's W appendix subsection to appendix.tex\", 'status': 'pending', 'activeForm': \"Adding Kendall's W appendix subsection\"}, {'content': 'Compress main text to ≤ 8 pages', 'status': 'pending', 'activeForm': 'Compressing main text'}, {'content': 'Compile and verify page count', 'status': 'pending', 'activeForm': 'Compiling and verifying page count'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': \"Add Kendall's W sentence to §5.2 (experiments.tex)\", 'status': 'in_progress', 'activeForm': \"Adding Kendall's W sentence to experiments.tex\"}, {'content': \"Add Kendall's W appendix subsection to appendix.tex\", 'status': 'pending', 'activeForm': \"Adding Kendall's W appendix subsection\"}, {'content': 'Compress main text to ≤ 8 pages', 'status': 'pending', 'activeForm': 'Compressing main text'}, {'content': 'Compile and verify page count', 'status': 'pending', 'activeForm': 'Compiling and verifying page count'}]"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T18:59:50.066246+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T18:59:50.066385+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
  "old_string": "At the more stringent $\\pm 10$\\,pp margin, only three of six mid-tier pairs reach equivalence, yielding a partially fragmented structure. The core finding---incompleteness as an upper-bound tier---is robust across all margins; the mid-tier cohesion is margin-dependent.\n\nIncompleteness produces the highest violation rate",
  "new_string": "At the more stringent $\\pm 10$\\,pp margin, only three of six mid-tier pairs reach equivalence, yielding a partially fragmented structure. The core finding---incompleteness as an upper-bound tier---is robust across all margins; the mid-tier cohesion is margin-dependent.\nType rankings are concordant across models (seven-model Kendall's $W = 0.353$, $\\chi^2(4) = 9.89$, $p = 0.038$, excluding coreferential which lacks replication data; five-model $W = 0.398$, $p = 0.072$), confirming that the hierarchy is not driven by any single model.\n\nIncompleteness produces the highest violation rate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
    "old_string": "At the more stringent $\\pm 10$\\,pp margin, only three of six mid-tier pairs reach equivalence, yielding a partially fragmented structure. The core finding---incompleteness as an upper-bound tier---is robust across all margins; the mid-tier cohesion is margin-dependent.\n\nIncompleteness produces the highest violation rate",
    "new_string": "At the more stringent $\\pm 10$\\,pp margin, only three of six mid-tier pairs reach equivalence, yielding a partially fragmented structure. The core finding---incompleteness as an upper-bound tier---is robust across all margins; the mid-tier cohesion is margin-dependent.\nType rankings are concordant across models (seven-model Kendall's $W = 0.353$, $\\chi^2(4) = 9.89$, $p = 0.038$, excluding coreferential which lacks replication data; five-model $W = 0.398$, $p = 0.072$), confirming that the hierarchy is not driven by any single model.\n\nIncompleteness produces the highest violation rate"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T18:59:50.066521+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T18:59:50.066698+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T18:59:50.066864+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around four analyses of increasing specificity: the binary ambiguity effect (C1), the type hierarchy (C2), the aggregate layer effect (C3), and the model$\times$type interaction (C4). C1 and C2 constitute our primary claims; C3 is inconclusive; C4 is exploratory but provides the model$\times$type interaction analysis.
5	
6	\subsection{Binary Ambiguity Effect (C1)}
7	
8	Across all five models and six types, ambiguous clauses increase violation rates by 34.0 pp (41.0\% vs.\ 6.9\%, OR $= 15.1$, 95\% CI $[10.78, 21.17]$, $p < 10^{-105}$). All six types individually produce significant increases (all $p < 10^{-5}$), and all five models show large effects ($+25.7$ to $+39.0$ pp, all $p < 10^{-17}$). Perturbation controls confirm specificity to semantic ambiguity ($n = 300$, $\Delta_{\text{perturb}} = -0.67$\,pp, CI containing zero). Clause identity explains 22.4\% of variance versus 1.0\% for model identity. A replication on two additional model families (Gemini-2.5-Flash, LLaMA-4-Scout; Appendix~\ref{app:model_expansion}) confirms the effect across seven models spanning six providers ($\Delta = +20.0$ to $+33.6$\,pp, both $p < 10^{-6}$).
9	
10	\subsection{Type Hierarchy (C2)}
11	
12	\begin{table*}[t]
13	\centering
14	\caption{Violation rates (\%) under ambiguous policy clauses by type and model. $\Delta$pp denotes the pooled difference between ambiguous and unambiguous conditions across all five models. All per-type differences are significant ($p < 10^{-5}$, Fisher's exact test).}
15	\label{tab:main_results}
16	\small
17	\begin{tabular}{llrrrrrrrr}
18	\toprule
19	Layer & Type & Pooled & GPT-5.4 & GPT-4.1 & Claude & Qwen3 & DeepSeek & $\Delta$pp & $p$ \\
20	\midrule
21	\multirow{3}{*}{\textcolor{speccolor}{Spec.}} & Incompleteness & 53.6 & 46.0 & 58.0 & 48.0 & 62.0 & 54.0 & +49.2 & $<10^{-37}$ \\
22	 & Auth.\ Scope & 41.6 & 64.0 & 46.0 & 12.0 & 26.0 & 60.0 & +36.0 & $<10^{-22}$ \\
23	 & Cond.\ Precedence 
…[truncated 5514 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T18:59:50.067035+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
  "old_string": "At $\\pm 10$\\,pp, only three mid-tier pairs reach equivalence; the incompleteness upper-bound is robust across all margins while mid-tier cohesion is margin-dependent.\n\nIncompleteness is highest",
  "new_string": "At $\\pm 10$\\,pp, only three mid-tier pairs reach equivalence; the incompleteness upper-bound is robust across all margins while mid-tier cohesion is margin-dependent.\nType rankings are concordant across models (seven-model Kendall's $W = 0.353$, $\\chi^2(4) = 9.89$, $p = 0.038$, excluding coreferential which lacks replication data; five-model $W = 0.398$, $p = 0.072$), confirming that the hierarchy is not driven by any single model.\n\nIncompleteness is highest"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
    "old_string": "At $\\pm 10$\\,pp, only three mid-tier pairs reach equivalence; the incompleteness upper-bound is robust across all margins while mid-tier cohesion is margin-dependent.\n\nIncompleteness is highest",
    "new_string": "At $\\pm 10$\\,pp, only three mid-tier pairs reach equivalence; the incompleteness upper-bound is robust across all margins while mid-tier cohesion is margin-dependent.\nType rankings are concordant across models (seven-model Kendall's $W = 0.353$, $\\chi^2(4) = 9.89$, $p = 0.038$, excluding coreferential which lacks replication data; five-model $W = 0.398$, $p = 0.072$), confirming that the hierarchy is not driven by any single model.\n\nIncompleteness is highest"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T18:59:50.067219+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T18:59:50.067368+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': \"Add Kendall's W sentence to §5.2 (experiments.tex)\", 'status': 'completed', 'activeForm': \"Adding Kendall's W sentence to experiments.tex\"}, {'content': \"Add Kendall's W appendix subsection to appendix.tex\", 'status': 'in_progress', 'activeForm': \"Adding Kendall's W appendix subsection\"}, {'content': 'Compress main text to ≤ 8 pages', 'status': 'pending', 'activeForm': 'Compressing main text'}, {'content': 'Compile and verify page count', 'status': 'pending', 'activeForm': 'Compiling and verifying page count'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': \"Add Kendall's W sentence to §5.2 (experiments.tex)\", 'status': 'completed', 'activeForm': \"Adding Kendall's W sentence to experiments.tex\"}, {'content': \"Add Kendall's W appendix subsection to appendix.tex\", 'status': 'in_progress', 'activeForm': \"Adding Kendall's W appendix subsection\"}, {'content': 'Compress main text to ≤ 8 pages', 'status': 'pending', 'activeForm': 'Compressing main text'}, {'content': 'Compile and verify page count', 'status': 'pending', 'activeForm': 'Compiling and verifying page count'}]"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T18:59:50.067522+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T18:59:50.067659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex",
  "offset": "230"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex",
    "offset": "230"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T18:59:50.067782+00:00_

230	\section{Multiple Comparison Correction}
231	\label{app:multiple_comparison}
232	
233	We apply Holm--Bonferroni correction within three test families: (i) per-type$\times$model McNemar tests for C1 (30 tests), (ii) TOST pairwise equivalence for C2 (15 pairs), and (iii) model$\times$type interaction for C4 (1 omnibus + post-hoc).
234	
235	\section{DRIP-R Category Mapping}
236	\label{app:drip_mapping}
237	
238	DRIP-R's five RE ambiguity categories---attachment, coordination, anaphora, scope, and ellipsis---overlap partially with our six-type taxonomy: scopal ambiguity and coreferential ambiguity correspond directly, while our remaining four types (lexical, authorization scope, incompleteness, conditional precedence) address policy-specific phenomena outside DRIP-R's RE scope.
239	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T18:59:50.067910+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex",
  "old_string": "DRIP-R's five RE ambiguity categories---attachment, coordination, anaphora, scope, and ellipsis---overlap partially with our six-type taxonomy: scopal ambiguity and coreferential ambiguity correspond directly, while our remaining four types (lexical, authorization scope, incompleteness, conditional precedence) address policy-specific phenomena outside DRIP-R's RE scope.",
  "new_string": "DRIP-R's five RE ambiguity categories---attachment, coordination, anaphora, scope, and ellipsis---overlap partially with our six-type taxonomy: scopal ambiguity and coreferential ambiguity correspond directly, while our remaining four types (lexical, authorization scope, incompleteness, conditional precedence) address policy-specific phenomena outside DRIP-R's RE scope.\n\n\\section{Cross-Model Type Ranking Concordance}\n\\label{app:kendall_w}\n\nTo quantify agreement among models on the relative difficulty of ambiguity types, we compute Kendall's coefficient of concordance $W$. For the five main-study models across all six types, $W = 0.398$ ($\\chi^2(5) = 9.94$, $p = 0.072$), indicating moderate but non-significant concordance. Including the two replication models (Gemini 2.5 Flash and LLaMA 4 Scout) over five shared types (excluding coreferential, which was not included in replication), concordance reaches significance: $W = 0.353$ ($\\chi^2(4) = 9.89$, $p = 0.038$). In both analyses, incompleteness consistently ranks highest (mean rank 5.5 / 4.5) and conditional precedence lowest (2.8 / 2.1), supporting the two-tier structure identified in \\S\\ref{sec:results}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex",
    "old_string": "DRIP-R's five RE ambiguity categories---attachment, coordination, anaphora, scope, and ellipsis---overlap partially with our six-type taxonomy: scopal ambiguity and coreferential ambiguity correspond directly, while our remaining four types (lexical, authorization scope, incompleteness, conditional precedence) address policy-specific phenomena outside DRIP-R's RE scope.",
    "new_string": "DRIP-R's five RE ambiguity categories---attachment, coordination, anaphora, scope, and ellipsis---overlap partially with our six-type taxonomy: scopal ambiguity and coreferential ambiguity correspond directly, while our remaining four types (lexical, authorization scope, incompleteness, conditional precedence) address policy-specific phenomena outside DRIP-R's RE scope.\n\n\\section{Cross-Model Type Ranking Concordance}\n\\label{app:kendall_w}\n\nTo quantify agreement among models on the relative difficulty of ambiguity types, we compute Kendall's coefficient of concordance $W$. For the five main-study models across all six types, $W = 0.398$ ($\\chi^2(5) = 9.94$, $p = 0.072$), indicating moderate but non-significant concordance. Including the two replication models (Gemini 2.5 Flash and LLaMA 4 Scout) over five shared types (excluding coreferential, which was not included in replication), concordance reaches significance: $W = 0.353$ ($\\chi^2(4) = 9.89$, $p = 0.038$). In both analyses, incompleteness consistently ranks highest (mean rank 5.5 / 4.5) and conditional precedence lowest (2.8 / 2.1), supporting the two-tier structure identified in \\S\\ref{sec:results}."
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T18:59:50.068102+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-21T18:59:50.068265+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': \"Add Kendall's W sentence to §5.2 (experiments.tex)\", 'status': 'completed', 'activeForm': \"Adding Kendall's W sentence to experiments.tex\"}, {'content': \"Add Kendall's W appendix subsection to appendix.tex\", 'status': 'completed', 'activeForm': \"Adding Kendall's W appendix subsection\"}, {'content': 'Compress main text to ≤ 8 pages', 'status': 'in_progress', 'activeForm': 'Compressing main text'}, {'content': 'Compile and verify page count', 'status': 'pending', 'activeForm': 'Compiling and verifying page count'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': \"Add Kendall's W sentence to §5.2 (experiments.tex)\", 'status': 'completed', 'activeForm': \"Adding Kendall's W sentence to experiments.tex\"}, {'content': \"Add Kendall's W appendix subsection to appendix.tex\", 'status': 'completed', 'activeForm': \"Adding Kendall's W appendix subsection\"}, {'content': 'Compress main text to ≤ 8 pages', 'status': 'in_progress', 'activeForm': 'Compressing main text'}, {'content': 'Compile and verify page count', 'status': 'pending', 'activeForm': 'Compiling and verifying page count'}]"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T18:59:50.068419+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T18:59:50.068555+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T18:59:50.068682+00:00_

ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/
texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fon
ts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/symbols/msam10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic
/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/urw/times/utmbi8a.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (14 pages, 423797 bytes).
Transcript written on main.log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T18:59:50.068813+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "bibtex main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"Output written|pages\" | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"Output written|pages\" | tail -3",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "tool_args": {
    "command": "bibtex main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"Output written|pages\" | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"Output written|pages\" | tail -3",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T18:59:50.068941+00:00_

This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
Output written on main.pdf (14 pages, 424026 bytes).
Output written on main.pdf (14 pages, 424026 bytes).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T18:59:50.069071+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"^\\[|Output written\" | head -20",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "tool_args": {
    "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"^\\[|Output written\" | head -20",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T18:59:50.069212+00:00_

[Loading MPS to PDF converter (version 2006.09.02).]
[]\T1/ptm/m/n/10 (+20) LLM-based agents op-er-ate un-der natural-
[][]\T1/ptm/m/n/10.95 (+20) 2026[][]) syn-the-sizes SMT-validated com-pli-ance
[]\T1/ptm/b/n/10.95 (+20) Scopal\T1/ptm/m/n/10.95 (+20) : quan-ti-fier, nega-ti
[]\T1/ptm/b/n/10.95 (+20) Lexical\T1/ptm/m/n/10.95 (+20) : pol-y-semy or homony
[3]) (./sections/method.tex [4]) (./sections/experiments.tex [5]
[6 <./figures/fig2_forest_plot.pdf>]
[8] (/usr/share/texlive/texmf-dist/tex/latex/psnfss/t1pcr.fd))
[][]$\T1/pcr/m/n/10.95 https : / / github . com / anonymous /
[]\T1/ptm/m/n/10 (+20) Ashwani Anand, Ivi Chatzi, Ri-tam Raha, and
[9]
[]\T1/ptm/m/n/10 (+20) Benedetta Rosa-dini, Alessio Fer-rari, Glo-ria Gori,
[10]) (./sections/appendix.tex
[11] [12] [13]
Output written on main.pdf (14 pages, 424026 bytes).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T18:59:50.069379+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"shipout\" main.log 2>/dev/null | head -20; echo \"---\"; grep -n \"\\[.*\\]\" main.log | grep -E \"^\\d+:\\[\" | head -20",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"shipout\" main.log 2>/dev/null | head -20; echo \"---\"; grep -n \"\\[.*\\]\" main.log | grep -E \"^\\d+:\\[\" | head -20",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T18:59:50.069498+00:00_

---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T18:59:50.069612+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -E \"^\\[\" main.log | head -30",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -E \"^\\[\" main.log | head -30",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T18:59:50.069729+00:00_

[Loading MPS to PDF converter (version 2006.09.02).]
[]\T1/ptm/m/n/10 (+20) LLM-based agents op-er-ate un-der natural-
[][]\T1/ptm/m/n/10.95 (+20) 2026[][]) syn-the-sizes SMT-validated com-pli-ance
[]\T1/ptm/b/n/10.95 (+20) Scopal\T1/ptm/m/n/10.95 (+20) : quan-ti-fier, nega-ti
[]\T1/ptm/b/n/10.95 (+20) Lexical\T1/ptm/m/n/10.95 (+20) : pol-y-semy or homony
[3]) (./sections/method.tex [4]) (./sections/experiments.tex [5]
[6 <./figures/fig2_forest_plot.pdf>]
[8]
[][]$\T1/pcr/m/n/10.95 https : / / github . com / anonymous /
[]\T1/ptm/m/n/10 (+20) Ashwani Anand, Ivi Chatzi, Ri-tam Raha, and
[9]
[]\T1/ptm/m/n/10 (+20) Benedetta Rosa-dini, Alessio Fer-rari, Glo-ria Gori,
[10]) (./sections/appendix.tex
[11] [12] [13]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T18:59:50.069887+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext main.pdf - 2>/dev/null | grep -n -E \"^(1|2|3|4|5|6|7|8|9|10|11|12|13|14)$\" | head -20",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext main.pdf - 2>/dev/null | grep -n -E \"^(1|2|3|4|5|6|7|8|9|10|11|12|13|14)$\" | head -20",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-21T18:59:50.070009+00:00_

59:1
128:1
265:2
324:2
430:3
516:3
625:4
701:4
921:5
999:5
1257:6
1337:10
1401:6
1445:7
1577:7
1595:8
1629:8
1759:9
1984:10
2312:11

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-21T18:59:50.070127+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext main.pdf - 2>/dev/null | head -1650 | tail -120",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext main.pdf - 2>/dev/null | head -1650 | tail -120",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-21T18:59:50.070292+00:00_

547
548
549
550
551
552
553
554
555
556
557
558

562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581

6.3

Systematic Nocuity

Among ambiguous clauses, 41.3% trigger majorityconvergent violations (≥3/5 models), with 13%
producing universal violations. This extends Berry
et al. (2004)’s framework with systematic nocuity:
all models converge on the same incorrect interpretation, invisible in agreement-based evaluation.
Incompleteness has the highest universal convergence (24%).

583

7

591

Discussion

Differential nocuity. Berry et al. (2004) distinguish nocuous from innocuous ambiguity. Our
results can be interpreted through a differential
nocuity lens: risk depends on ambiguity type (base
vulnerability), safety training (selective mitigation),
and disambiguation channel availability. This generates two testable predictions: (P1) types with
explicit decision points should show larger safetytraining gains than gap-filling types; (P2) disambiguation channels should reduce violations more
for high-deficit types. Our mitigation experiment
(Appendix B) is consistent with, though not a formal test of, P1 (−18.0 pp for authorization scope
vs. −3.4 pp for incompleteness).

Disambiguation Deficit

8

582

584
585
586
587
588
589
590

592
593
594
595
596
597
598
599
600
601
602
603
604
605

Practical implications. A proof-of-concept classifier (Appendix D) achieves F1 = 0.81 for binary ambiguity detection but only 0.34 for
incompleteness—the highest-risk type is the hardest to detect. With agents exhibiting disambiguation deficit in >89% of cases, type-aware auditing
and externalized detection (Chantree et al., 2006;
Ferrari and Esuli, 2019) are necessary for policygoverned deployments.

606

8

615

Conclusion

607
608
609
610
611
612
613
614

Ambiguous policy clauses increase agent safety violations by 34.0 pp (OR = 15.1) across five models,
with clause identity explaining 22× more variance
than model identity. The two-tier type hierarchy
replic
…[truncated 202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-21T18:59:50.070446+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext main.pdf - 2>/dev/null | head -1850 | tail -200",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext main.pdf - 2>/dev/null | head -1850 | tail -200",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-21T18:59:50.070646+00:00_

624

Limitations

625

Model coverage. We evaluate seven APIaccessible models from six providers (four proprietary, three open-source; two in replication,

626

616
617
618
619
620
621
622
623

627
628

629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678

Appendix E). Smaller open-source models (7B–
70B parameters) may show different vulnerability
patterns, and our findings may not generalize to
models with fundamentally different training approaches.
Domain scope. τ 2 -bench covers retail and airline customer service. Policy ambiguity effects in
other domains (healthcare, finance, legal) remain
to be tested, though the within-study cross-domain
consistency is encouraging: failure mode distributions share the same top-two modes (assumptionbased action and unauthorized escalation) across
domains, with individual mode base rates differing
by up to 12.5 pp, likely reflecting domain policy
structure rather than methodological artifacts.
Synthetic ambiguity. Our matched-pair design
requires synthetic construction of ambiguous variants, which may not capture the full distribution of
naturally occurring policy ambiguities. We mitigate this through expert review and a realism
validation comparing ambiguous clauses against
original τ 2 -bench policy text. Ambiguous clauses
are indistinguishable from originals in lexical diversity (TTR, KS p = 0.89) and word length
(p = 0.09). Readability is slightly higher (Flesch–
Kincaid d = 0.29, p = 0.006) and sentence length
moderately higher (d = 0.74), both reflecting
the structural demands of encoding ambiguity in
standalone clauses. Across matched pairs, disambiguation preserves readability (Flesch–Kincaid
d = 0.14, p = 0.10), confirming that minimal
edits change semantic precision without altering
linguistic register.
Cross-judge asymmetry. Although our dualjudge calibration (§4) shows
…[truncated 2903 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-21T18:59:50.070842+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext -layout main.pdf - 2>/dev/null | grep -n \"Conclusion\" | head -5",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext -layout main.pdf - 2>/dev/null | grep -n \"Conclusion\" | head -5",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-21T18:59:50.070968+00:00_

546:566   disambiguation awareness is 4.6%: Claude (11.0%)            8     Conclusion                                          615

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-21T18:59:50.071124+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
  "offset": "35",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
    "offset": "35",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-21T18:59:50.071281+00:00_

35	
36	Sensitivity analysis across seven margins ($\pm 5$--$20$ pp; Appendix~\ref{app:tost}) confirms this structure: the two-tier pattern emerges at $\pm 12$ pp (5/6 mid-tier pairs equivalent) and stabilizes at $\pm 15$ pp (6/6). A margin-free bootstrap cluster analysis (Ward's method, $B = 10{,}000$) corroborates: at $k = 2$, incompleteness forms a singleton with the remaining five types in one cluster; at $k = 3$, coreferential additionally separates---consistent with the TOST two-tier pattern (Appendix~\ref{app:cluster}).
37	At $\pm 10$\,pp, only three mid-tier pairs reach equivalence; the incompleteness upper-bound is robust across all margins while mid-tier cohesion is margin-dependent. Cross-model type ranking concordance is moderate (Kendall's $W$; Appendix~\ref{app:kendall_w}).
38	
39	Incompleteness is highest in four of five models (rates $\geq$46\% in all seven; Appendix~\ref{app:model_expansion}). Its unambiguous variant adds policy content, so the 49.2\,pp effect is an upper bound; a confound analysis confirms significance after controlling for information delta (Appendix~\ref{app:confound}). Coreferential, whose variants are lexically identical, provides a confound-free lower bound at 31.6\%.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-21T18:59:50.071436+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5 && bibtex main 2>&1 | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "tool_args": {
    "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5 && bibtex main 2>&1 | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -3",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-21T18:59:50.071605+00:00_

sr/share/texlive/texmf-dist/fonts/type1/urw/times/utmbi8a.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (14 pages, 424007 bytes).
Transcript written on main.log.
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
onts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (14 pages, 424007 bytes).
Transcript written on main.log.
onts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (14 pages, 424007 bytes).
Transcript written on main.log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-21T18:59:50.071746+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdftotext -layout main.pdf - 2>/dev/null | grep -n \"Conclusion\\|Limitations\\|References\\|^A \" | head -10",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "tool_args": {
    "command": "pdftotext -layout main.pdf - 2>/dev/null | grep -n \"Conclusion\\|Limitations\\|References\\|^A \" | head -10",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-21T18:59:50.071866+00:00_

531:                                                                  8   Conclusion                                            611
543:575   tion deficit: defaulting to single-parse adoption           Limitations                                               621
624:                                                                 References                                               722

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-21T18:59:50.072004+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\nfor i, page in enumerate(pages, 1):\n    lines = page.strip().split('\\n')\n    first_line = lines[0][:80] if lines else '(empty)'\n    last_line = lines[-1][:80] if lines else '(empty)'\n    print(f'Page {i}: starts={first_line!r} ends={last_line!r}')\n    # Check for section headers\n    for line in lines:\n        line = line.strip()\n        if any(h in line for h in ['Introduction', 'Related Work', 'Ambiguity Taxonomy', 'Method', 'Results', 'Error Analysis', 'Discussion', 'Conclusion', 'Limitations', 'Data and Code', 'References', 'Appendix', 'TOST', 'Mitigation', 'Severity', 'Detection', 'Replication', 'Confound', 'Judge', 'Regression', 'Bootstrap', 'Clause-Level', 'Multiple', 'DRIP', 'Cross-Model Type']):\n            if len(line) < 80:\n                print(f'  -> Section: {line}')\n\"\n",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\npages = text.split('\\f')\nfor i, page in enumerate(pages, 1):\n    lines = page.strip().split('\\n')\n    first_line = lines[0][:80] if lines else '(empty)'\n    last_line = lines[-1][:80] if lines else '(empty)'\n    print(f'Page {i}: starts={first_line!r} ends={last_line!r}')\n    # Check for section headers\n    for line in lines:\n        line = line.strip()\n        if any(h in line for h in ['Introduction', 'Related Work', 'Ambiguity Taxonomy', 'Method', 'Results', 'Error Analysis', 'Discussion', 'Conclusion', 'Limitations', 'Data and Code', 'References', 'Appendix', 'TOST', 'Mitigation', 'Severity', 'Detection', 'Replication', 'Confound', 'Judge', 'Regression', 'Bootstrap', 'Clause-Level', 'Multiple', 'DRIP', 'Cross-Model Type']):\n            if len(line) < 80:\n                print(f'  -> Section: {line}')\n\"\n",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-21T18:59:50.072184+00:00_

Page 1: starts='Not All Policy Ambiguity Is Equal: Type-Specific Safety Risks for LLM' ends='084'
  -> Section: Introduction
Page 2: starts='Policy Ambiguity Taxonomy' ends='147'
  -> Section: Policy Ambiguity Taxonomy
  -> Section: Cross-Judge Evaluation
  -> Section: 4-Tier Violation Severity
  -> Section: Related Work
Page 3: starts='148' ends='243'
  -> Section: Policy specification for agents. DRIP-R
  -> Section: model×type interaction. We map DRIP-R’s five
  -> Section: in Appendix L. PolicyBank (Choi et al., 2026)
  -> Section: the concurrent DRIP-R benchmark (Borkakoty
  -> Section: Ambiguity Taxonomy
Page 4: starts='244' ends='340'
  -> Section: Method
Page 5: starts='341' ends='437'
  -> Section: analyses use binary thresholds (Appendix C).
  -> Section: via logistic regression (Appendix F).
  -> Section: TOST equivalence testing (Lakens, 2017) with a
  -> Section: power exceeds 0.99 for both C1 and C2; TOST
  -> Section: Results
Page 6: starts='Table 1: Violation rates (%) under ambiguous policy clauses by type and model. ∆' ends='485'
  -> Section: 20 pp; Appendix A) confirms this structure: the
  -> Section: TOST two-tier pattern (Appendix I). At ±10 pp,
  -> Section: (Kendall’s W ; Appendix M).
  -> Section: delta (Appendix F). Coreferential, whose variants
Page 7: starts='Model × Ambiguity Type Violation Rates' ends='533'
  -> Section: Error Analysis [Exploratory]
Page 8: starts='555' ends='629'
  -> Section: Discussion
  -> Section: Conclusion
  -> Section: Limitations
  -> Section: Appendix E). Smaller open-source models (7B–
Page 9: starts='630' ends='727'
  -> Section: Severity threshold. Our primary analysis uses
  -> Section: Data and Code Availability
  -> Section: References
Page 10: starts='728' ends='10'
  -> Section: Chen, and Yufang Hou. 2026. DRIP-R: A benchmark
Page 11: starts='834' ends='918'
  -> Section: TOST Equivalence Sensitivity
  -> Section: Table 2 reports the TOST equivalence analysis
  -> Section: Table 2: TOST equivalence se
…[truncated 1156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-21T18:59:50.072394+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"Overfull\" main.log; echo \"---\"; grep \"Overfull\" main.log | head -10; echo \"===\"; grep -i \"undefined\" main.log | head -10; echo \"===\"; grep \"Warning.*Citation\" main.log | head -5",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"Overfull\" main.log; echo \"---\"; grep \"Overfull\" main.log | head -10; echo \"===\"; grep -i \"undefined\" main.log | head -10; echo \"===\"; grep \"Warning.*Citation\" main.log | head -5",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-21T18:59:50.072524+00:00_

2
---
Overfull \hbox (3.28299pt too wide) in paragraph at lines 11--24
Overfull \hbox (10.16498pt too wide) in paragraph at lines 198--218
===
===

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-21T18:59:50.072645+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -A2 \"Overfull\" main.log",
  "timeout": "10000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -A2 \"Overfull\" main.log",
    "timeout": "10000"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-21T18:59:50.072762+00:00_

Overfull \hbox (3.28299pt too wide) in paragraph at lines 11--24
 [][] 
 []
--
Overfull \hbox (10.16498pt too wide) in paragraph at lines 198--218
 [][] 
 []

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-21T18:59:50.072896+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -i \"multiply defined\\|label.*rerun\\|rerun\" main.log | head -5",
  "timeout": "10000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -i \"multiply defined\\|label.*rerun\\|rerun\" main.log | head -5",
    "timeout": "10000"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-21T18:59:50.073016+00:00_

(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
Package: rerunfilecheck 2025-06-21 v1.11 Rerun checks for auxiliary files (HO)
Package uniquecounter Info: New unique counter `rerunfilecheck' on input line 2
Package rerunfilecheck Info: File `main.out' has not changed.
(rerunfilecheck)             Checksum: 7D4F360E5ADE56DD792CB9A87429899B;5607.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-21T18:59:50.073178+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': \"Add Kendall's W sentence to §5.2 (experiments.tex)\", 'status': 'completed', 'activeForm': \"Adding Kendall's W sentence to experiments.tex\"}, {'content': \"Add Kendall's W appendix subsection to appendix.tex\", 'status': 'completed', 'activeForm': \"Adding Kendall's W appendix subsection\"}, {'content': 'Compress main text to ≤ 8 pages', 'status': 'completed', 'activeForm': 'Compressing main text'}, {'content': 'Compile and verify page count', 'status': 'completed', 'activeForm': 'Compiling and verifying page count'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': \"Add Kendall's W sentence to §5.2 (experiments.tex)\", 'status': 'completed', 'activeForm': \"Adding Kendall's W sentence to experiments.tex\"}, {'content': \"Add Kendall's W appendix subsection to appendix.tex\", 'status': 'completed', 'activeForm': \"Adding Kendall's W appendix subsection\"}, {'content': 'Compress main text to ≤ 8 pages', 'status': 'completed', 'activeForm': 'Compressing main text'}, {'content': 'Compile and verify page count', 'status': 'completed', 'activeForm': 'Compiling and verifying page count'}]"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-21T18:59:50.073348+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-21T18:59:50.073511+00:00_

## 完成报告

### 修改汇总

**1. Kendall's W 整合**

| 文件 | 修改 |
|------|------|
| `experiments.tex` L37 | C2 段末添加简短引用: `Cross-model type ranking concordance is moderate (Kendall's $W$; Appendix~\ref{app:kendall_w}).`（hook 自动将完整数据句压缩为附录引用） |
| `appendix.tex` 末尾 | 新增 `\section{Cross-Model Type Ranking Concordance}` (`\label{app:kendall_w}`)，包含五模型 W=0.398/p=0.072、七模型 W=0.353/p=0.038 完整数据，及 mean rank 分析 |

**2. 页数压缩**

主文在添加 Kendall's W 前已被压缩到 8 页（experiments.tex 的 incompleteness 段落此前已精简）。添加后仍 ≤ 8 页，无需额外压缩。

### 编译结果

| 指标 | 结果 |
|------|------|
| 总页数 | 14（含附录） |
| 主文页数 | **8**（Discussion + Conclusion 均在第 8 页内） |
| ≤ 8 页 | **是** ✓（Limitations 从第 8 页开始，不计入限制） |
| Undefined citations | 0 |
| Overfull hbox | 2（均在表格中，3.3pt 和 10.2pt，可接受） |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_edit_round9_kendall_w_integration_20260521T185400"
}
```

</details>

---
