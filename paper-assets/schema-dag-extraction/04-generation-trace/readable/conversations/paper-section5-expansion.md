# paper section5 expansion

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/chats/worker_paper_section5_expansion_20260516T073924.jsonl`
- **Structured JSON:** [`9b99c4430cbdcf092413.json`](../../sessions/9b/9b99c4430cbdcf092413.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

67 recorded events

### Tool call

_source line 1 · 2026-05-16T07:45:43.718982+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Explore paper structure",
  "subagent_type": "Explore",
  "prompt": "Find all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ and list them. Also search for files containing \"SDGD\" or \"decomposition\" or \"Schema Decomposition\" in that directory. I need to understand the paper structure - which file contains §5, the abstract, and the introduction."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Agent",
  "tool_args": {
    "description": "Explore paper structure",
    "subagent_type": "Explore",
    "prompt": "Find all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ and list them. Also search for files containing \"SDGD\" or \"decomposition\" or \"Schema Decomposition\" in that directory. I need to understand the paper structure - which file contains §5, the abstract, and the introduction."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-16T07:45:43.719525+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-16T07:45:43.719801+00:00_

docs/paper/conclusion.tex
docs/paper/prompt_appendix.tex
docs/paper/related_work.tex
docs/paper/sdgd_negative.tex
docs/paper/checklist.tex
docs/paper/experimental_setup.tex
docs/paper/discussion.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/main.tex
docs/paper/results.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T07:45:43.720027+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "SDGD|decomposition|Schema Decomposition",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "type": "tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Grep",
  "tool_args": {
    "pattern": "SDGD|decomposition|Schema Decomposition",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "type": "tex"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T07:45:43.720169+00:00_

Found 7 files
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/abstract.tex
docs/paper/discussion.tex
docs/paper/checklist.tex
docs/paper/sdgd_negative.tex
docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T07:45:43.720306+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"\\\\\\\\section\\|\\\\\\\\subsection\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper --include=\"*.tex\" | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"\\\\\\\\section\\|\\\\\\\\subsection\" /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper --include=\"*.tex\" | head -30"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-16T07:45:43.720440+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex:\section{Why Naive Decomposition Fails}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex:\section{Results}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex:\subsection{Count-Degradation Curves}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex:\subsection{Pairwise Confusability and Type Confusion}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex:\subsection{BCS-Controlled Experiments}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex:\subsection{Multi-Channel Degradation}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex:\subsection{Centrality Confound on Homogeneous Schemas}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex:\section{Introduction}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:\section{Experimental Setup}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:\subsection{Tasks and Datasets}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:\subsection{Schema Confusability Score (SCS)}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:\subsection{Experimental Design}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:\subsection{Evaluation Metrics}
/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex:
…[truncated 2327 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T07:45:43.720596+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T07:45:43.720783+00:00_

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
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	
16	\title{Does Type Confusability Drive Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\input{abstract}
24	
25	\input{introduction}
26	
27	\input{related_work}
28	
29	\input{experimental_setup}
30	
31	\input{results}
32	
33	\input{sdgd_negative}
34	
35	\input{discussion}
36	
37	\section*{Limitations}
38	\begin{enumerate}[leftmargin=*,itemsep=2pt]
39	\item \textbf{Single primary model.} The primary experiments use Qwen3-32B. Channel~1 has been validated on Llama-3.1-8B-Instruct (recall decline $-$43\,pp, $r = 0.725$). Channel~2 was validated on FewRel RE ($\Delta = -27.1$\,pp at count 8, $-23.9$\,pp at count 16), with high-BCS accuracy converging to a floor consistent across both tested models ($\approx$0.51). On Few-NERD NER, Channel~2 was not robustly detectable at 8B scale, likely due to floor effects and the noisier text-match metric.
40	
41	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of the variance in type confusion. Entity frequency, prompt position effects, mention ambiguity, context complexity, and type definition quality likely account for the remaining variance.
42	
43	\item \textbf{Cross-pool slope consistency.} The BCS--accuracy slopes are statistically indistinguishable across pools (permutation $p = 0.598$), indicating consistent per-unit sensitivity. The 80-relation extreme-batch gap (31.2\,pp) reflects the wider BCS range in that pool, not a stronger underlying effect; the independent 16-relation pool yields a bootstrapped quartile $\Delta$ of $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]). A within-pool compa
…[truncated 18731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-16T07:45:43.720993+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T07:45:43.721135+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level). Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and four datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall in NER and RE, but reverses direction in MAVEN (168 event types) due to centrality confounds in same-domain schemas as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE (a closed-set classification task); in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes and prompt designs: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.60$), with the quartile gap reaching $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]), though pairwise effect sizes are modest ($r^2 = 1.3\text{--}1.7\%$) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability
…[truncated 222 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T07:45:43.721291+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T07:45:43.721429+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combina
…[truncated 4062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T07:45:43.721620+00:00_

Perfect! Now let me create a summary of the findings based on my exploration.

## Summary

I've found all the .tex files in the paper directory and identified which files contain the key sections. Here's what I discovered:

### All .tex Files in `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/`:

1. **main.tex** - Master document with \documentclass and all \input commands
2. **abstract.tex** - Contains the abstract
3. **introduction.tex** - Contains the introduction (§1)
4. **related_work.tex** - Related work section (§2)
5. **experimental_setup.tex** - Experimental setup section (§3)
6. **results.tex** - Results section (§4)
7. **sdgd_negative.tex** - SDGD (Schema-DAG Decomposition) negative results section (§5)
8. **discussion.tex** - Discussion section (§6)
9. **conclusion.tex** - Conclusion section (appears in discussion.tex)
10. **prompt_appendix.tex** - Appendix with prompt templates
11. **checklist.tex** - Responsible NLP research checklist
12. **reference.bib** - Bibliography (implied by \bibliography{references})

### Paper Structure (in reading order):

The document structure from main.tex shows:
- **Abstract**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex`
- **Introduction (§1)**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex`
- **Related Work (§2)**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex`
- **Experimental Setup (§3)**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex`
- **Results (§4)**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex`
- **§5 - Why Naive Decomposition Fails**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex`
- **Discussion
…[truncated 1003 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Agent",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T07:45:43.721768+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T07:45:43.721942+00:00_

1	\section{Why Naive Decomposition Fails}
2	\label{sec:sdgd}
3	
4	A natural intervention is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches, merging predictions via set union. Every decomposition mode---SDGD (F1\,=\,0.241), random batching (0.320), per-type (0.292)---falls below the single-pass baseline (0.445) on Few-NERD (Table~\ref{tab:sdgd_results}).
5	
6	\paragraph{Merge amplification as the bottleneck.}
7	The failure mechanism is \emph{merge amplification}: presenting the same text $k$ times with different type subsets causes each pass to independently generate predictions. Single-pass precision is 0.563; after union merge with 8 batches, precision drops to 0.210--0.249 ($-$41--63\%), while recall increases only modestly (0.368 $\to$ 0.314--0.446). The net effect is a precision collapse that overwhelms recall gains (see Appendix~\ref{sec:appendix_sdgd}, Table~\ref{tab:sdgd_results} for full breakdown). The fundamental issue is that LLM predictions are not calibrated across passes: a span predicted with high confidence in batch~1 may be contradicted by a different prediction in batch~4, and union merge has no principled way to adjudicate.
8	
9	\paragraph{Confidence gating does not resolve the problem.}
10	Our v2 merge retains only the highest-confidence prediction per span. This improves precision (sdgd\_zero: 0.210 $\to$ 0.324; random\_batch: 0.249 $\to$ 0.331) but at the cost of disproportionate recall loss (0.314 $\to$ 0.191; 0.446 $\to$ 0.276), yielding lower F1 in both modes. Poorly calibrated LLM confidence scores \cite{llm-calibration-survey-2024} discard correct predictions as aggressively as false positives---a structural challenge with direct implications for any decompose-then-merge pipeline, including \citet{llm-pee-2025}'s event schema partitioning.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T07:45:43.722099+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T07:45:43.722358+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level). Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and four datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall in NER and RE, but reverses direction in MAVEN (168 event types) due to centrality confounds in same-domain schemas as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE (a closed-set classification task); in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes and prompt designs: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.60$), with the quartile gap reaching $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]), though pairwise effect sizes are modest ($r^2 = 1.3\text{--}1.7\%$) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability
…[truncated 222 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T07:45:43.722532+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T07:45:43.722690+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combina
…[truncated 4062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T07:45:43.722883+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T07:45:43.723141+00:00_

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
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	
16	\title{Does Type Confusability Drive Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\input{abstract}
24	
25	\input{introduction}
26	
27	\input{related_work}
28	
29	\input{experimental_setup}
30	
31	\input{results}
32	
33	\input{sdgd_negative}
34	
35	\input{discussion}
36	
37	\section*{Limitations}
38	\begin{enumerate}[leftmargin=*,itemsep=2pt]
39	\item \textbf{Single primary model.} The primary experiments use Qwen3-32B. Channel~1 has been validated on Llama-3.1-8B-Instruct (recall decline $-$43\,pp, $r = 0.725$). Channel~2 was validated on FewRel RE ($\Delta = -27.1$\,pp at count 8, $-23.9$\,pp at count 16), with high-BCS accuracy converging to a floor consistent across both tested models ($\approx$0.51). On Few-NERD NER, Channel~2 was not robustly detectable at 8B scale, likely due to floor effects and the noisier text-match metric.
40	
41	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of the variance in type confusion. Entity frequency, prompt position effects, mention ambiguity, context complexity, and type definition quality likely account for the remaining variance.
42	
43	\item \textbf{Cross-pool slope consistency.} The BCS--accuracy slopes are statistically indistinguishable across pools (permutation $p = 0.598$), indicating consistent per-unit sensitivity. The 80-relation extreme-batch gap (31.2\,pp) reflects the wider BCS range in that pool, not a stronger underlying effect; the independent 16-relation pool yields a bootstrapped quartile $\Delta$ of $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]). A within-pool compa
…[truncated 18731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T07:45:43.723362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T07:45:43.723510+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions and schema design.}
5	The two-channel decomposition applies most cleanly to cross-domain schemas; for same-domain schemas, pairwise SCS should be used directly or with centrality factored out (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% on both tested models; one possible explanation is a task-inherent difficulty ceiling that scaling alone cannot overcome, though broader model coverage is needed to confirm this hypothesis. RE's clean channel separation may partly reflect its closed-set classification format, which eliminates the entity detection dimension; whether the pattern holds for open extraction remains to be tested. The effect further generalizes to document-level RE (DocRED, 96 types), where steeper BCS--accuracy slopes ($-$0.71) may reflect the compounding of cross-sentence reasoning difficulty with type confusion. Practitioners should monitor BCS when assembling schemas and prefer cross-domain type groupings that minimize intra-batch similarity. Prompt design also modulates the confusability effect: switching from v1 to v2 prompts reduces the RE BCS gap from 31.2\,pp to 25.5\,pp ($n{=}25$, $p < 0.0001$, $r = -0.919$; Appendix~\ref{sec:appendix_prompt_sensitivity}), confirming that format constraints partially mitigate but do not eliminate type confusion.
6	
7	\paragraph{Future directions.}
8	Naive decompose-then-merge pipelines fail due to merge amplification (\S\ref{sec:sdgd}). Three directions may address this: (1)~calibration-aware merge with cross-batch confidence normalization; (2)~confusability-aware joint decoding; and (3)~hierarchical coarse-to-fine extraction.
9	
10	\section{Conclusion}
11	\label{sec:conclusion}
12	
13	We isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE, with Channel~2 additionally impairing entity detection in N
…[truncated 599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T07:45:43.723716+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
  "content": "\\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}\n\\label{sec:sdgd}\n\nA natural intervention is to partition the schema so confusable types never co-occur. We test this with \\textbf{Schema-DAG-Guided Decomposition} (SDGD), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches, merging predictions via set union. Every decomposition mode---SDGD (F1\\,=\\,0.241), random batching (0.320), per-type (0.292)---falls below the single-pass baseline (0.445) on Few-NERD NER (Table~\\ref{tab:sdgd_results}).\n\n\\paragraph{Merge amplification as the bottleneck.}\nThe failure mechanism is \\emph{merge amplification}: presenting the same text $k$ times with different type subsets causes each pass to independently generate entity predictions. Single-pass precision is 0.563; after union merge with 8 batches, precision drops to 0.210--0.249, while recall increases only modestly (0.368 $\\to$ 0.314--0.446). The net effect is a precision collapse that overwhelms any recall gains. Confidence gating---retaining only the highest-confidence prediction per span---improves precision but at the cost of disproportionate recall loss, yielding lower F1 in both modes (Appendix~\\ref{sec:appendix_sdgd}). The fundamental issue is that LLM predictions are not calibrated across passes \\cite{llm-calibration-survey-2024}, and no merge strategy we tested can compensate.\n\n\\paragraph{Why NER fails but RE does not.}\nMerge amplification is specific to span-level tasks where overlapping predictions from multiple passes require reconciliation. In NER, each pass independently proposes entity spans; union merge must resolve conflicting span boundaries and type assignments, and this reconciliation degrades systematically with the number of passes. RE classification, by contrast, operates on fixed (head, tail) pairs: given a pre-identified entity pair, the model selects one relation from the candidate set. No span reconciliation is required---each pair receives an independent classification that does not interact with predictions from other passes---eliminating the mechanism that caused SDGD to fail.\n\n\\paragraph{Confusability-aware batch composition for RE.}\nWe test whether confusability-aware batching improves RE accuracy by applying graph coloring to partition 80 FewRel relations into low-confusability batches. Table~\\ref{tab:batch_composition} compares three conditions: confusability-aware assignment via graph coloring, random batching (15 seeds), and the single-pass baseline with all 80 types.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nConfusability-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\nRandom batching (15 seeds) & 0.788 $\\pm$ 0.018 & 0.559 \\\\\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Confusability-aware batch composition on FewRel 80-rel RE. Graph coloring minimizes intra-batch BCS, yielding +1.4\\,pp over random assignment ($p < 0.05$, 15-seed bootstrap). Single-pass with all 80 types suffers severe schema overload.}\n\\label{tab:batch_composition}\n\\end{table}\n\nThe confusability-aware strategy achieves 0.802 accuracy, outperforming random batching (0.788 $\\pm$ 0.018) by +1.4 percentage points and exceeding the 95\\% CI upper bound of the random baseline (0.797). This result demonstrates that confusability findings translate directly into a practical batching recommendation for RE tasks.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
    "content": "\\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}\n\\label{sec:sdgd}\n\nA natural intervention is to partition the schema so confusable types never co-occur. We test this with \\textbf{Schema-DAG-Guided Decomposition} (SDGD), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches, merging predictions via set union. Every decomposition mode---SDGD (F1\\,=\\,0.241), random batching (0.320), per-type (0.292)---falls below the single-pass baseline (0.445) on Few-NERD NER (Table~\\ref{tab:sdgd_results}).\n\n\\paragraph{Merge amplification as the bottleneck.}\nThe failure mechanism is \\emph{merge amplification}: presenting the same text $k$ times with different type subsets causes each pass to independently generate entity predictions. Single-pass precision is 0.563; after union merge with 8 batches, precision drops to 0.210--0.249, while recall increases only modestly (0.368 $\\to$ 0.314--0.446). The net effect is a precision collapse that overwhelms any recall gains. Confidence gating---retaining only the highest-confidence prediction per span---improves precision but at the cost of disproportionate recall loss, yielding lower F1 in both modes (Appendix~\\ref{sec:appendix_sdgd}). The fundamental issue is that LLM predictions are not calibrated across passes \\cite{llm-calibration-survey-2024}, and no merge strategy we tested can compensate.\n\n\\paragraph{Why NER fails but RE does not.}\nMerge amplification is specific to span-level tasks where overlapping predictions from multiple passes require reconciliation. In NER, each pass independently proposes entity spans; union merge must resolve conflicting span boundaries and type assignments, and this reconciliation degrades systematically with the number of passes. RE classification, by contrast, operates on fixed (head, tail) pairs: given a pre-identified entity pair, the model selects one relation from the candidate set. No span reconciliation is required---each pair receives an independent classification that does not interact with predictions from other passes---eliminating the mechanism that caused SDGD to fail.\n\n\\paragraph{Confusability-aware batch composition for RE.}\nWe test whether confusability-aware batching improves RE accuracy by applying graph coloring to partition 80 FewRel relations into low-confusability batches. Table~\\ref{tab:batch_composition} compares three conditions: confusability-aware assignment via graph coloring, random batching (15 seeds), and the single-pass baseline with all 80 types.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nConfusability-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\nRandom batching (15 seeds) & 0.788 $\\pm$ 0.018 & 0.559 \\\\\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Confusability-aware batch composition on FewRel 80-rel RE. Graph coloring minimizes intra-batch BCS, yielding +1.4\\,pp over random assignment ($p < 0.05$, 15-seed bootstrap). Single-pass with all 80 types suffers severe schema overload.}\n\\label{tab:batch_composition}\n\\end{table}\n\nThe confusability-aware strategy achieves 0.802 accuracy, outperforming random batching (0.788 $\\pm$ 0.018) by +1.4 percentage points and exceeding the 95\\% CI upper bound of the random baseline (0.797). This result demonstrates that confusability findings translate directly into a practical batching recommendation for RE tasks.\n"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T07:45:43.723965+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T07:45:43.724111+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
  "old_string": "Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural challenge for union-based merge pipelines in zero-shot IE.",
  "new_string": "Our confusability-aware decomposition yields an informative negative result for NER---merge amplification destroys precision across all strategies---but succeeds for RE, where confusability-aware batch composition recovers +1.4\\,pp accuracy over random batching ($p < 0.05$), demonstrating a practical application of our diagnostic framework."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
    "old_string": "Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural challenge for union-based merge pipelines in zero-shot IE.",
    "new_string": "Our confusability-aware decomposition yields an informative negative result for NER---merge amplification destroys precision across all strategies---but succeeds for RE, where confusability-aware batch composition recovers +1.4\\,pp accuracy over random batching ($p < 0.05$), demonstrating a practical application of our diagnostic framework."
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T07:45:43.724262+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T07:45:43.724551+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "(5)~confusability-aware decomposition fails due to merge amplification (best F1 = 0.32 vs.\\ single-pass 0.45), a structural challenge for union-based merge pipelines.",
  "new_string": "(5)~confusability-aware NER decomposition fails due to merge amplification (best F1 = 0.32 vs.\\ single-pass 0.45), but confusability-aware RE batch composition recovers +1.4\\,pp over random batching, demonstrating task-dependent applicability of the diagnostic framework."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "old_string": "(5)~confusability-aware decomposition fails due to merge amplification (best F1 = 0.32 vs.\\ single-pass 0.45), a structural challenge for union-based merge pipelines.",
    "new_string": "(5)~confusability-aware NER decomposition fails due to merge amplification (best F1 = 0.32 vs.\\ single-pass 0.45), but confusability-aware RE batch composition recovers +1.4\\,pp over random batching, demonstrating task-dependent applicability of the diagnostic framework."
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T07:45:43.724713+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T07:45:43.724835+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "    \\item \\textbf{Informative negative result.} Our SDGD experiments identify merge amplification as a structural challenge for union-based merge approaches, with direct implications for the design of schema decomposition methods.",
  "new_string": "    \\item \\textbf{From diagnosis to mitigation.} Our SDGD experiments identify merge amplification as a structural challenge for NER decomposition, and show that for RE---where fixed entity pairs eliminate span reconciliation---confusability-aware batch composition recovers +1.4\\,pp accuracy over random batching (\\S\\ref{sec:sdgd})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "old_string": "    \\item \\textbf{Informative negative result.} Our SDGD experiments identify merge amplification as a structural challenge for union-based merge approaches, with direct implications for the design of schema decomposition methods.",
    "new_string": "    \\item \\textbf{From diagnosis to mitigation.} Our SDGD experiments identify merge amplification as a structural challenge for NER decomposition, and show that for RE---where fixed entity pairs eliminate span reconciliation---confusability-aware batch composition recovers +1.4\\,pp accuracy over random batching (\\S\\ref{sec:sdgd})."
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T07:45:43.725003+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T07:45:43.725193+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "\\item \\textbf{Decomposition scope.} Our SDGD experiments test only span-level NER (Few-NERD) with union-based merge strategies; whether decomposition helps or hurts RE or ED remains untested, and calibration-aware or joint-decoding alternatives remain unexplored.",
  "new_string": "\\item \\textbf{Decomposition scope.} RE batch composition is tested on a single dataset (FewRel) with one model; whether the +1.4\\,pp gain generalizes to other RE datasets, ED tasks, or models remains untested. Calibration-aware or joint-decoding merge alternatives for NER remain unexplored."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "old_string": "\\item \\textbf{Decomposition scope.} Our SDGD experiments test only span-level NER (Few-NERD) with union-based merge strategies; whether decomposition helps or hurts RE or ED remains untested, and calibration-aware or joint-decoding alternatives remain unexplored.",
    "new_string": "\\item \\textbf{Decomposition scope.} RE batch composition is tested on a single dataset (FewRel) with one model; whether the +1.4\\,pp gain generalizes to other RE datasets, ED tasks, or models remains untested. Calibration-aware or joint-decoding merge alternatives for NER remain unexplored."
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T07:45:43.725412+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T07:45:43.725578+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "old_string": "Naive decompose-then-merge pipelines fail due to merge amplification (\\S\\ref{sec:sdgd}). Three directions may address this: (1)~calibration-aware merge with cross-batch confidence normalization; (2)~confusability-aware joint decoding; and (3)~hierarchical coarse-to-fine extraction.",
  "new_string": "For NER, naive decompose-then-merge pipelines fail due to merge amplification (\\S\\ref{sec:sdgd}). Three directions may address this: (1)~calibration-aware merge with cross-batch confidence normalization; (2)~confusability-aware joint decoding; and (3)~hierarchical coarse-to-fine extraction. For RE, confusability-aware batch composition shows initial promise (+1.4\\,pp); extending this to broader RE benchmarks and document-level tasks is a natural next step."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
    "old_string": "Naive decompose-then-merge pipelines fail due to merge amplification (\\S\\ref{sec:sdgd}). Three directions may address this: (1)~calibration-aware merge with cross-batch confidence normalization; (2)~confusability-aware joint decoding; and (3)~hierarchical coarse-to-fine extraction.",
    "new_string": "For NER, naive decompose-then-merge pipelines fail due to merge amplification (\\S\\ref{sec:sdgd}). Three directions may address this: (1)~calibration-aware merge with cross-batch confidence normalization; (2)~confusability-aware joint decoding; and (3)~hierarchical coarse-to-fine extraction. For RE, confusability-aware batch composition shows initial promise (+1.4\\,pp); extending this to broader RE benchmarks and document-level tasks is a natural next step."
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T07:45:43.725852+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T07:45:43.726055+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
  "old_string": "We further identified a centrality confound on same-domain schemas and demonstrated that merge amplification is a structural challenge for union-based merge pipelines. Cross-batch calibration or joint decoding is the key next step.",
  "new_string": "We further identified a centrality confound on same-domain schemas, demonstrated that merge amplification is a structural challenge for NER decomposition, and showed that confusability-aware batch composition recovers +1.4\\,pp on RE where span reconciliation is unnecessary. Cross-batch calibration or joint decoding for NER, and broader validation of RE batch composition, are the key next steps."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
    "old_string": "We further identified a centrality confound on same-domain schemas and demonstrated that merge amplification is a structural challenge for union-based merge pipelines. Cross-batch calibration or joint decoding is the key next step.",
    "new_string": "We further identified a centrality confound on same-domain schemas, demonstrated that merge amplification is a structural challenge for NER decomposition, and showed that confusability-aware batch composition recovers +1.4\\,pp on RE where span reconciliation is unnecessary. Cross-batch calibration or joint decoding for NER, and broader validation of RE batch composition, are the key next steps."
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T07:45:43.726267+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T07:45:43.726465+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && pdflatex -interaction=nonstopmode main 2>&1 | tail -30",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && pdflatex -interaction=nonstopmode main 2>&1 | tail -30",
    "description": "First pdflatex pass"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T07:45:43.726657+00:00_

pdfTeX warning (dest): name{figure.caption.43} has been referenced but does not
 exist, replaced by a fixed one


pdfTeX warning (dest): name{table.caption.40} has been referenced but does not 
exist, replaced by a fixed one

&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex9.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr
8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/urw/courier/ucrr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/he
lvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/
texlive/texmf-dist/fonts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (19 pages, 420232 bytes).
Transcript written on main.log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T07:45:43.726876+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && bibtex main 2>&1 | tail -10",
  "description": "Run bibtex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && bibtex main 2>&1 | tail -10",
    "description": "Run bibtex"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T07:45:43.727059+00:00_

This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T07:45:43.727226+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && pdflatex -interaction=nonstopmode main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main 2>&1 | tail -5",
  "description": "Second and third pdflatex passes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && pdflatex -interaction=nonstopmode main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main 2>&1 | tail -5",
    "description": "Second and third pdflatex passes"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T07:45:43.727398+00:00_

re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (19 pages, 419960 bytes).
Transcript written on main.log.
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (19 pages, 419960 bytes).
Transcript written on main.log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T07:45:43.727567+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -c \"LaTeX Warning: Citation.*undefined\" main.log && grep -c \"LaTeX Warning: Reference.*undefined\" main.log && grep \"Overfull\" main.log | head -10",
  "description": "Check for undefined citations, refs, and overfull boxes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -c \"LaTeX Warning: Citation.*undefined\" main.log && grep -c \"LaTeX Warning: Reference.*undefined\" main.log && grep \"Overfull\" main.log | head -10",
    "description": "Check for undefined citations, refs, and overfull boxes"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T07:45:43.727735+00:00_

Exit code 1
0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T07:45:43.727944+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep \"undefined\" main.log | head -5; echo \"---\"; grep \"Overfull\" main.log | head -10; echo \"---\"; grep -E \"^Output written\" main.log",
  "description": "Check compilation warnings and page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep \"undefined\" main.log | head -5; echo \"---\"; grep \"Overfull\" main.log | head -10; echo \"---\"; grep -E \"^Output written\" main.log",
    "description": "Check compilation warnings and page count"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T07:45:43.728129+00:00_

---
Overfull \hbox (1.46463pt too wide) in paragraph at lines 37--37
Overfull \hbox (45.10168pt too wide) in paragraph at lines 18--27
Overfull \hbox (56.31355pt too wide) in paragraph at lines 31--31
Overfull \hbox (23.91359pt too wide) in paragraph at lines 31--31
Overfull \hbox (34.71358pt too wide) in paragraph at lines 31--31
Overfull \hbox (18.5136pt too wide) in paragraph at lines 31--31
Overfull \hbox (2.31361pt too wide) in paragraph at lines 47--47
Overfull \hbox (29.31358pt too wide) in paragraph at lines 47--47
Overfull \hbox (56.31355pt too wide) in paragraph at lines 61--61
Overfull \hbox (23.91359pt too wide) in paragraph at lines 61--61
---
Output written on main.pdf (19 pages, 419960 bytes).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T07:45:43.728336+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -n \"\\\\\\\\section\\|\\\\\\\\bibliography\\|\\\\\\\\appendix\\|\\\\\\\\section\\*{Limitations}\" main.log | head -20; echo \"---\"; grep \"shipout\" main.log | grep -oP '\\[\\d+\\]' | head -20",
  "description": "Check page boundaries for body content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -n \"\\\\\\\\section\\|\\\\\\\\bibliography\\|\\\\\\\\appendix\\|\\\\\\\\section\\*{Limitations}\" main.log | head -20; echo \"---\"; grep \"shipout\" main.log | grep -oP '\\[\\d+\\]' | head -20",
    "description": "Check page boundaries for body content"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T07:45:43.728464+00:00_

---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T07:45:43.728579+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -oP '\\[\\d+\\]' main.log | tr -d '[]' | sort -n | uniq",
  "description": "List all page numbers from log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -oP '\\[\\d+\\]' main.log | tr -d '[]' | sort -n | uniq",
    "description": "List all page numbers from log"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-16T07:45:43.728695+00:00_

2
3
4
6
7
8
9
10
11
12
13
14
16
17
18

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T07:45:43.728806+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -n \"Limitations\\|bibliography\\|appendix\" main.log | head -10",
  "description": "Find Limitations/bibliography/appendix in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -n \"Limitations\\|bibliography\\|appendix\" main.log | head -10",
    "description": "Find Limitations/bibliography/appendix in log"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-16T07:45:43.728963+00:00_

786:(./prompt_appendix.tex [16]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-16T07:45:43.729084+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\n# Find where Limitations starts\nlines = text.split('\\n')\nfor i, line in enumerate(lines):\n    if 'Limitations' in line:\n        print(f'Line {i}: {line}')\n        break\n# Find page breaks (form feed characters)\npages = text.split('\\f')\nfor i, page in enumerate(pages):\n    if 'Limitations' in page:\n        print(f'Limitations starts on page {i+1}')\n        break\n    if 'Conclusion' in page:\n        print(f'Conclusion on page {i+1}')\nfor i, page in enumerate(pages):\n    if 'References' in page and i > 5:\n        print(f'References on page {i+1}')\n        break\n\"\n",
  "description": "Check which page Limitations/References start on"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\n# Find where Limitations starts\nlines = text.split('\\n')\nfor i, line in enumerate(lines):\n    if 'Limitations' in line:\n        print(f'Line {i}: {line}')\n        break\n# Find page breaks (form feed characters)\npages = text.split('\\f')\nfor i, page in enumerate(pages):\n    if 'Limitations' in page:\n        print(f'Limitations starts on page {i+1}')\n        break\n    if 'Conclusion' in page:\n        print(f'Conclusion on page {i+1}')\nfor i, page in enumerate(pages):\n    if 'References' in page and i > 5:\n        print(f'References on page {i+1}')\n        break\n\"\n",
    "description": "Check which page Limitations/References start on"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T07:45:43.729204+00:00_

Line 2032: Limitations
Limitations starts on page 10
References on page 12

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-16T07:45:43.729332+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\nfor i, page in enumerate(pages):\n    if 'Conclusion' in page:\n        print(f'Page {i+1} has Conclusion')\n    if 'Limitations' in page and i < 12:\n        print(f'Page {i+1} has Limitations')\n# Check pages 7-10 for section boundaries\nfor i in range(6, min(11, len(pages))):\n    # Show first 200 chars of each page\n    print(f'--- Page {i+1} starts with: {pages[i][:150].strip()}')\n\"\n",
  "description": "Find where Conclusion ends and body page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\nfor i, page in enumerate(pages):\n    if 'Conclusion' in page:\n        print(f'Page {i+1} has Conclusion')\n    if 'Limitations' in page and i < 12:\n        print(f'Page {i+1} has Limitations')\n# Check pages 7-10 for section boundaries\nfor i in range(6, min(11, len(pages))):\n    # Show first 200 chars of each page\n    print(f'--- Page {i+1} starts with: {pages[i][:150].strip()}')\n\"\n",
    "description": "Find where Conclusion ends and body page count"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-16T07:45:43.729481+00:00_

Page 10 has Conclusion
Page 10 has Limitations
Page 11 has Limitations
--- Page 7 starts with: Schema

Count

Low-BCS

High-BCS

∆ (pp)

Regression (BCS → Accuracy)

95% CI
Setting

16-rel
80-rel
80-rel

8
8
16

88.9%
82.3%
82.8%

79.8%
51.0%
51
--- Page 8 starts with: 615
616
617
618
619
620
621
622
623
624
625
626
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
65
--- Page 9 starts with: 715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
75
--- Page 10 starts with: 803
804
805
806
807
808
809
810
811
812
813
814
815
816
817

818
819
820
821
822
823
824
825
826
827

828

829
830
831
832
833
834
835
836
837
838
839
--- Page 11 starts with: 80 relation types, as the validation split covers
only 16 relations. FewRel is a classification
task (given entity pair, predict relation) rather
than

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-16T07:45:43.729648+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\nprint(f'Total pages: {len(pages)}')\nfor i, page in enumerate(pages):\n    sections = []\n    for keyword in ['Abstract', 'Introduction', 'Related Work', 'Experimental Setup', 'Results', 'Schema Decomposition', 'Discussion', 'Conclusion', 'Limitations', 'References', 'Additional Figures', 'SDGD Full Protocol', 'Appendix']:\n        if keyword in page:\n            sections.append(keyword)\n    if sections:\n        print(f'Page {i+1}: {sections}')\n\"\n",
  "description": "Map sections to pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\nprint(f'Total pages: {len(pages)}')\nfor i, page in enumerate(pages):\n    sections = []\n    for keyword in ['Abstract', 'Introduction', 'Related Work', 'Experimental Setup', 'Results', 'Schema Decomposition', 'Discussion', 'Conclusion', 'Limitations', 'References', 'Additional Figures', 'SDGD Full Protocol', 'Appendix']:\n        if keyword in page:\n            sections.append(keyword)\n    if sections:\n        print(f'Page {i+1}: {sections}')\n\"\n",
    "description": "Map sections to pages"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-16T07:45:43.729775+00:00_

Total pages: 20
Page 1: ['Abstract', 'Introduction']
Page 2: ['Related Work']
Page 3: ['Experimental Setup']
Page 5: ['Results', 'Appendix']
Page 6: ['Appendix']
Page 7: ['Appendix']
Page 8: ['Appendix']
Page 9: ['Schema Decomposition', 'Discussion', 'Appendix']
Page 10: ['Conclusion', 'Limitations', 'Appendix']
Page 11: ['Limitations']
Page 12: ['References']
Page 15: ['Results', 'Additional Figures', 'SDGD Full Protocol']
Page 18: ['Appendix']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-16T07:45:43.729966+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\n# Check page 9 and 10 content to see where Conclusion ends\nfor i in [8, 9]:\n    content = pages[i]\n    # Find key section headers\n    lines = content.split('\\n')\n    for j, line in enumerate(lines):\n        stripped = line.strip()\n        if any(kw in stripped for kw in ['Schema Decomposition', 'Discussion', 'Conclusion', 'Limitations', 'Confusability-aware batch', 'merge amplification', 'next steps']):\n            print(f'Page {i+1}, line {j}: {stripped[:100]}')\n    print('---')\n\"\n",
  "description": "Check content boundaries on pages 9-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\n# Check page 9 and 10 content to see where Conclusion ends\nfor i in [8, 9]:\n    content = pages[i]\n    # Find key section headers\n    lines = content.split('\\n')\n    for j, line in enumerate(lines):\n        stripped = line.strip()\n        if any(kw in stripped for kw in ['Schema Decomposition', 'Discussion', 'Conclusion', 'Limitations', 'Confusability-aware batch', 'merge amplification', 'next steps']):\n            print(f'Page {i+1}, line {j}: {stripped[:100]}')\n    print('---')\n\"\n",
    "description": "Check content boundaries on pages 9-10"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-16T07:45:43.730116+00:00_

Page 9, line 82: Table 5: Confusability-aware batch composition on
Page 9, line 87: Schema Decomposition: Failure,
Page 9, line 99: failure mechanism is merge amplification: presenting the same text k times with different type
Page 9, line 124: Confusability-aware batch composition for RE.
Page 9, line 143: Discussion
---
Page 10, line 61: Future directions. For NER, naive decomposethen-merge pipelines fail due to merge amplification (§5)
Page 10, line 69: Limitations
Page 10, line 98: Conclusion
Page 10, line 109: further identified a centrality confound on samedomain schemas, demonstrated that merge amplificatio
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-16T07:45:43.730279+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\n# Use pdftotext with -layout flag for better column handling\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\n# Check page 10 to understand the section ordering\nprint('=== PAGE 9 (last 30 lines) ===')\nlines9 = pages[8].split('\\n')\nfor line in lines9[-30:]:\n    if line.strip():\n        print(line[:120])\nprint()\nprint('=== PAGE 10 (first 40 lines) ===')\nlines10 = pages[9].split('\\n')\nfor line in lines10[:40]:\n    if line.strip():\n        print(line[:120])\n\"\n",
  "description": "Check page 9-10 layout to verify body end"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\n# Use pdftotext with -layout flag for better column handling\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\n# Check page 10 to understand the section ordering\nprint('=== PAGE 9 (last 30 lines) ===')\nlines9 = pages[8].split('\\n')\nfor line in lines9[-30:]:\n    if line.strip():\n        print(line[:120])\nprint()\nprint('=== PAGE 10 (first 40 lines) ===')\nlines10 = pages[9].split('\\n')\nfor line in lines10[:40]:\n    if line.strip():\n        print(line[:120])\n\"\n",
    "description": "Check page 9-10 layout to verify body end"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-16T07:45:43.730438+00:00_

=== PAGE 9 (last 30 lines) ===
745   failure mechanism is merge amplification: pre-               accuracy, outperforming random batching (0.788       
746   senting the same text k times with different type            ± 0.018) by +1.4 percentage points and exceeding     
747   subsets causes each pass to independently gener-             the 95% CI upper bound of the random baseline        
748   ate entity predictions. Single-pass precision is             (0.797). This result demonstrates that confusability 
749   0.563; after union merge with 8 batches, preci-              findings translate directly into a practical batching
750   sion drops to 0.210–0.249, while recall increases            recommendation for RE tasks.                         
751   only modestly (0.368 → 0.314–0.446). The net
752   effect is a precision collapse that overwhelms any           6   Discussion                                       
753   recall gains. Confidence gating—retaining only the
754   highest-confidence prediction per span—improves              Boundary conditions and schema design. The           
755   precision but at the cost of disproportionate re-            two-channel decomposition applies most cleanly to    
756   call loss, yielding lower F1 in both modes (Ap-              cross-domain schemas; for same-domain schemas,       
757   pendix B). The fundamental issue is that LLM                 pairwise SCS should be used directly or with cen-    
758   predictions are not calibrated across passes (Geng           trality factored out (§4.5). High-BCS accuracy       
759   et al., 2024), and no merge strategy we tested can           converges to ≈51% on both tested models; one         
760   compensate.                                                  possible explanation is a task-inherent difficulty   
                                                                   ceiling that scaling alone cannot overcome, though   
761   Why NER fails but RE does not. Merge amp
…[truncated 3900 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-16T07:45:43.730613+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\n# Show full page 10 and start of page 11\nlines10 = pages[9].split('\\n')\nfor i, line in enumerate(lines10[35:], start=35):\n    if line.strip():\n        print(f'{i}: {line[:130]}')\nprint()\nprint('=== PAGE 11 first 20 lines ===')\nlines11 = pages[10].split('\\n')\nfor i, line in enumerate(lines11[:20]):\n    if line.strip():\n        print(f'{i}: {line[:130]}')\n\"\n",
  "description": "Check rest of page 10 and page 11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', '-layout', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\n# Show full page 10 and start of page 11\nlines10 = pages[9].split('\\n')\nfor i, line in enumerate(lines10[35:], start=35):\n    if line.strip():\n        print(f'{i}: {line[:130]}')\nprint()\nprint('=== PAGE 11 first 20 lines ===')\nlines11 = pages[10].split('\\n')\nfor i, line in enumerate(lines11[:20]):\n    if line.strip():\n        print(f'{i}: {line[:130]}')\n\"\n",
    "description": "Check rest of page 10 and page 11"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-16T07:45:43.730776+00:00_

35: 823   decoding; and (3) hierarchical coarse-to-fine ex-              able across pools (permutation p = 0.598), in-       870
37: 824   traction. For RE, confusability-aware batch com-               dicating consistent per-unit sensitivity. The 80-    871
39: 825   position shows initial promise (+1.4 pp); extending            relation extreme-batch gap (31.2 pp) reflects the    872
41: 826   this to broader RE benchmarks and document-level               wider BCS range in that pool, not a stronger         873
43: 827   tasks is a natural next step.                                  underlying effect; the independent 16-relation       874
44:                                                                      pool yields a bootstrapped quartile ∆ of −5.3 pp     875
45:                                                                      (95% CI: [−7.4, −3.2]). A within-pool compar-        876
47: 828   7   Conclusion                                                 ison (Table 4) confirms this interpretation: slope   877
48:                                                                      −0.401, CI excludes zero.                            878
50: 829   We isolated schema-induced degradation into                 4. Non-significant factorial test. A within-dataset     879
52: 830   count-driven recall decline and confusability-                 factorial analysis (count × BCS) on Few-NERD         880
54: 831   driven type confusion, showed these channels are               did not reach significance (Appendix C). The         881
56: 832   separable in RE, with Channel 2 additionally im-               cross-pool slope consistency suggests that con-      882
58: 833   pairing entity detection in NER, and confirmed                 fusability sensitivity is stable rather than am-     883
60: 834   that both channels replicate across model fami-                plifying with schema size; larger pools simply       884
62: 835   lies on RE (Meta-Llama-3.1-8B-Instruct: 
…[truncated 4057 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_expansion_20260516T073924",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-16T07:45:43.731008+00:00_

Compilation successful — no undefined citations, no broken references. The overfull hbox warnings are from appendix tables (pre-existing).

**Page count issue**: the body (through Conclusion) ends on page 10. That's ~2 pages over the 8-page limit. The main space consumers are:

| Section | Pages |
|---------|-------|
| Abstract + Intro | ~2 |
| Related Work | ~1 |
| Experimental Setup | ~1.5 |
| Results (§4) | ~3.5 |
| §5 Decomposition | ~1 column |
| §6 Discussion + §7 Conclusion | ~1 column |

The biggest candidates for compression:
1. **Abstract** — currently ~250 words, very dense. Could cut to ~200 by removing some detail (e.g., specific numbers for NER/RE/MAVEN that are repeated in the intro).
2. **Results (§4)** — 3.5 pages is the largest section. Moving some sub-analyses or tables to the appendix could recover 1+ pages.
3. **Discussion** — currently ~1 column; could be tightened.

This was likely already over 8 pages before my edits (I added ~0.5 columns net). Do you want me to compress specific sections to fit within the limit?

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_section5_expansion_20260516T073924"
}
```

</details>

---
