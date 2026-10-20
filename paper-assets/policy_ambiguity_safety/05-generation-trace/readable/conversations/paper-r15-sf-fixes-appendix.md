# paper r15 sf fixes appendix

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_paper_r15_sf_fixes_appendix_20260522T161701.jsonl`
- **Structured JSON:** [`f75e1185f1e91e8167a3.json`](../../sessions/f7/f75e1185f1e91e8167a3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-22T16:18:09.187172+00:00_

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
  "session": "worker_paper_r15_sf_fixes_appendix_20260522T161701",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T16:18:09.187642+00:00_

1	\section{Error Analysis \emph{[Exploratory]}}
2	\label{sec:analysis}
3	
4	The following failure mode taxonomy emerges empirically from LLM-coded traces, distinct from the input ambiguity taxonomy (\S\ref{sec:taxonomy}).
5	
6	We analyze 614 violation traces across all five models, coded into five failure modes: unauthorized escalation, assumption-based action, scope misapplication, arbitrary rule selection, and conservative refusal. GPT-5.4 and GPT-4.1 serve as detailed annotation anchors because they span the judge boundary. Inter-coder reliability is substantial (Gwet's AC$_1$ $= 0.62$ \citep{gwet_2014}; Cohen's $\kappa = 0.52$ \citep{cohen_1960}; the gap partly reflects the prevalence paradox). Using LLMs to code LLM failure modes introduces a circularity risk that the moderate $\kappa$ may partly reflect; human-coded validation of at least one failure category would strengthen these findings.
7	
8	\subsection{Type-Specific Failure Mechanisms}
9	
10	The five-model data reveal three mechanistically distinct failure patterns that crosscut the specification/linguistic layer boundary.
11	
12	\emph{Structural misparse} (scope misapplication): the agent constructs an incorrect parse and follows it consistently, paralleling garden-path processing \citep{frazier_rayner_1982,ferreira_good_enough_2002} at a behavioral (not mechanistic) level. This dominates scopal (all 5 models), conditional precedence (4/5), and coreferential (3/5).
13	
14	\emph{Information gap-filling} (assumption-based action): the agent fills missing information with plausible but incorrect defaults. This dominates incompleteness (3/5) and lexical (3/5).
15	
16	\emph{Boundary violation} (unauthorized escalation): the agent exceeds permission boundaries when authorization scope is underspecified; 69.2\% of such violations involve unauthorized escalation with zero conservative refusals ($p < 10^{-4}$, binomial test), revealing systematic permissiveness bias. This dominates authorization scope exclusivel
…[truncated 1922 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r15_sf_fixes_appendix_20260522T161701",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T16:18:09.187927+00:00_

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
  "session": "worker_paper_r15_sf_fixes_appendix_20260522T161701",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T16:18:09.188109+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Differential nocuity.}
5	Building on \citet{berry_kamsties_2004}'s nocuous/innocuous distinction, our results are consistent with a \emph{differential nocuity} hypothesis \citep{willis_nocuous_2008}: risk depends on ambiguity type (base vulnerability), safety training (selective mitigation), and disambiguation channel availability. Types with explicit decision points (e.g., authorization scope) appear more amenable to both safety training and prompted intervention than gap-filling types (e.g., incompleteness), where mitigation attempts can backfire (see below).
6	
7	\paragraph{Taxonomy as intervention design.}
8	Type membership explains only 0.4\% of violation variance versus 22.4\% for individual clause wording. However, the taxonomy's value lies in predicting failure \emph{mechanisms}: each type maps to a mechanistically distinct failure pattern with cross-model consistency (\S\ref{sec:analysis}). Structural misparse dominates scopal (5/5 models) and conditional precedence (4/5), information gap-filling dominates incompleteness and lexical ($\geq$3/5), and boundary violation dominates authorization scope exclusively (5/5, with zero conservative refusals). This type$\to$mechanism mapping enables targeted intervention design even though type membership is a poor predictor of individual clause risk.
9	
10	\paragraph{Prompt-based mitigation.}
11	A matched-pair mitigation study on GPT-5.4 ($n = 50$ per type; Appendix~\ref{app:mitigation}) finds generic awareness prompting ineffective ($\Delta = +1.3$\,pp), with type-specific results mirroring the mechanism taxonomy: authorization scope improves ($-12$\,pp, $p = 0.070$) but incompleteness \emph{worsens} ($+14$\,pp, $p = 0.118$). Opposite directions under different prompt formulations (incompleteness: $-$3.4\,pp in v1 vs.\ $+$14\,pp in v2) reinforce policy-design-level solutions over prompt-level fixes.
12	
13	\paragraph{Practical implications.}
14	A proof-o
…[truncated 280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r15_sf_fixes_appendix_20260522T161701",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T16:18:09.188341+00:00_

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
  "session": "worker_paper_r15_sf_fixes_appendix_20260522T161701",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T16:18:09.188613+00:00_

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
29	Table~\ref{tab:mitigation} reports the per-type, per-model $\Delta$pp from the disambiguation-instruction mitigation experiment (1,256 treatment episodes across five of six types; coreferential was not tested). Coreferential pairs are excluded from both the mitigation and replication experiments. In mitigation, their ambiguous and unambiguous variants differ only in pronoun resolution, making it impossible to craft targeted disambiguation instructions without revealing the experimental manipulation. In replication, the $\tau^2$-bench episode design for coreferential ambiguity is tightly coupled to the original five-model configuration; extendin
…[truncated 23595 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r15_sf_fixes_appendix_20260522T161701",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T16:18:09.188769+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r15_sf_fixes_appendix_20260522T161701",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T16:18:09.188895+00:00_

docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r15_sf_fixes_appendix_20260522T161701",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T16:18:09.189044+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "liu_ambiguity_2023|hu_ambiguity_2025",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib",
  "output_mode": "content",
  "-C": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_r15_sf_fixes_appendix_20260522T161701",
  "tool": "Grep",
  "tool_args": {
    "pattern": "liu_ambiguity_2023|hu_ambiguity_2025",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/docs/paper/references.bib",
    "output_mode": "content",
    "-C": "2"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T16:18:09.189218+00:00_

296-}
297-
298:@article{hu_ambiguity_2025,
299-  title={Ambiguity in {LLMs} is a Concept Missing Problem},
300-  author={Hu, Zhibo and Wang, Chen and Shu, Yanfeng and Paik, Hye-Young and Zhu, Liming},
--
342-}
343-
344:@inproceedings{liu_ambiguity_2023,
345-  title={We're Afraid Language Models Aren't Modeling Ambiguity},
346-  author={Liu, Alisa and Wu, Zhaofeng and Michael, Julian and Suhr, Alane and West, Peter and Koller, Alexander and Swayamdipta, Swabha and Smith, Noah A. and Choi, Yejin},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_r15_sf_fixes_appendix_20260522T161701",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-22T16:18:09.189405+00:00_

API Error: {"type":"error","error":{"details":null,"type":"overloaded_error","message":"Overloaded"},"request_id":"req_011CbHudj5Ria74DXeCnijVm"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_r15_sf_fixes_appendix_20260522T161701"
}
```

</details>

---
