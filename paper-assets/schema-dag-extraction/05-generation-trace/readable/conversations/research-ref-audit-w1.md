# research ref audit w1

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 181
- **Recorded user turns:** 0
- **Tool calls:** 90
- **Original source:** `logs/chats/worker_research_ref-audit-w1_20260526T101506.jsonl`
- **Structured JSON:** [`f1316d5edc8e5c7d5dc7.json`](../../sessions/f1/f1316d5edc8e5c7d5dc7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

181 recorded events

### Tool call

_source line 1 · 2026-05-26T10:24:00.481554+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-26T10:24:00.481940+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-26T10:24:00.482320+00:00_

1	@inproceedings{golde-2025-familiarity,
2	  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},
3	  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},
4	  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
5	  pages     = {820--834},
6	  year      = {2025},
7	  url       = {https://arxiv.org/abs/2412.10121}
8	}
9	
10	@book{cohen-1988-statistical,
11	  author    = {Cohen, Jacob},
12	  title     = {Statistical Power Analysis for the Behavioral Sciences},
13	  edition   = {2nd},
14	  publisher = {Lawrence Erlbaum Associates},
15	  year      = {1988}
16	}
17	
18	@inproceedings{baan-2023-ecological,
19	  author    = {Orlikowski, Matthias and R{\"o}ttger, Paul and Cimiano, Philipp and Hovy, Dirk},
20	  title     = {The Ecological Fallacy in Annotation: Modeling Human Label Variation goes beyond Sociodemographics},
21	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
22	  pages     = {1017--1029},
23	  year      = {2023}
24	}
25	
26	@inproceedings{josifoski-2022-genie,
27	  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},
28	  title     = {{GenIE}: Generative Information Extraction},
29	  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
30	  pages     = {4626--4643},
31	  year      = {2022}
32	}
33	
34	@inproceedings{dubey-2018-pairwise-confusion,
35	  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},
36	  title     = {Pairwise Confusion for Fine-Grained Visual Classification},
37	  booktitle = {Proceedings of the Euro
…[truncated 28869 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T10:24:00.482513+00:00_

docs/paper/conclusion.tex
docs/paper/supplementary.tex
docs/paper/prompt_appendix.tex
docs/paper/abstract.tex
docs/paper/checklist.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/sdgd_negative.tex
docs/paper/introduction.tex
docs/paper/experimental_setup.tex
docs/paper/results.tex
docs/paper/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T10:24:00.482683+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T10:24:00.482812+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T10:24:00.482958+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read all tex files for citations",
  "subagent_type": "Explore",
  "prompt": "Read all the .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ and extract every citation command (\\cite, \\citep, \\citet, \\citealt, \\citealp) with its surrounding context (the sentence it appears in). List each citation key and the context sentence. The tex files are: abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, discussion.tex, conclusion.tex, sdgd_negative.tex, supplementary.tex, prompt_appendix.tex, checklist.tex, main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Agent",
  "tool_args": {
    "description": "Read all tex files for citations",
    "subagent_type": "Explore",
    "prompt": "Read all the .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ and extract every citation command (\\cite, \\citep, \\citet, \\citealt, \\citealp) with its surrounding context (the sentence it appears in). List each citation key and the context sentence. The tex files are: abstract.tex, introduction.tex, related_work.tex, experimental_setup.tex, results.tex, discussion.tex, conclusion.tex, sdgd_negative.tex, supplementary.tex, prompt_appendix.tex, checklist.tex, main.tex"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T10:24:00.483115+00:00_

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
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-26T10:24:00.483241+00:00_

1	\begin{abstract}
2	Schema complexity affects training-free large language model (LLM) information extraction (IE), yet prior work conflates two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). We present, to our knowledge, the first controlled study isolating these factors in zero-shot LLM IE across four datasets, focusing on relation extraction (RE) as the primary testbed with named entity recognition (NER) and event detection as boundary conditions.
3	Using embedding-based confusability metrics with controlled batch design, we find:
4	(1)~count degradation spans NER and RE (up to $-$49 percentage points [pp]), and inter-type confusability independently predicts RE type substitution errors, with bounded interaction confirmed by equivalence testing;
5	(2)~batch confusability independently explains ${\sim}$27\% of cross-batch RE accuracy variance on FewRel (semipartial $R^2 = 0.273$), replicating across two model families at three scales (8B--70B), while the NER null serves as a boundary condition;
6	(3)~schema decomposition fails due to merge amplification and routing failure, though oracle routing recovers accuracy\footnote{Code and data are available at \url{https://anonymous.4open.science/r/schema-dag-extraction-4C10/}.}.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T10:24:00.483375+00:00_

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
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-26T10:24:00.483508+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{../../figures/paper/fig_problem_illustration.pdf}
7	\caption{Schema complexity in zero-shot relation extraction. Given the same input, a simple schema (few dissimilar types) yields the correct relation, while a complex schema with more candidate types and a cluster of semantically similar types causes type substitution (gold \emph{place of birth} $\to$ predicted \emph{residence}). We decompose schema complexity into two dimensions: type count and inter-type confusability.}
8	\label{fig:problem}
9	\end{figure}
10	
11	\looseness=-1
12	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \citep{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.28 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable (Figure~\ref{fig:problem}).
13	
14	\looseness=-1
15	What explains this degra
…[truncated 3013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-26T10:24:00.483669+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-26T10:24:00.483809+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	\looseness=-1
6	Training-free LLM IE spans instruction tuning \citep{instructuie-2023}, code-style schema encoding \citep{knowcoder-2024,codeie-2023}, annotation-guided extraction \citep{gollie-2024,adelie-2024}, schema-driven decoding \citep{slot-2025,oneke-2025}, and constrained JSON decoding \citep{json-schema-bench-2025,willard2023efficient}. NER methods include zero-shot decomposition \citep{xie-zeroshot-ner-2023,promptner-2023}, distillation \citep{uniner-2024}, and bidirectional encoders \citep{gliner-2024,gliner2-2025}; RE methods include zero-shot triplet extraction \citep{relationprompt-2022}, constrained generation \citep{josifoski-2022-genie}, and shared embedding spaces \citep{boylan-2025-glirel,wadhwa-re-llm-2023}. Related work exploits type embeddings for retrieval \citep{shachar-2025-ner-retriever} and introspective confusion for example selection \citep{reflect-learn-2026}. These methods handle moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales.
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{../../figures/paper/fig_framework.pdf}
11	\caption{Experimental design overview on FewRel. Each point is one batch; color encodes RE accuracy (green=high, red=low). \textbf{Dimension~1} (horizontal): accuracy declines with type count (\S\ref{sec:count_curves}). \textbf{Dimension~2} (vertical): within each count level, higher BCS correlates with lower accuracy (\S\ref{sec:bcs_controlled}). BCS range narrows at high counts, limiting Dimension~2 discriminability.}
12	\label{fig:framework}
13	\end{figure}
14	
15	\paragraph{Schema complexity in IE.}
16	\looseness=-1
17	The most directly related work is LLM-PEE \citep{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extra
…[truncated 3334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-26T10:24:00.483982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T10:24:00.484108+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T10:24:00.484256+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	\looseness=-1
5	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
6	
7	\begin{figure*}[t]
8	\centering
9	\begin{minipage}[t]{0.48\textwidth}
10	\centering
11	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
12	\end{minipage}
13	\hfill
14	\begin{minipage}[t]{0.48\textwidth}
15	\centering
16	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
17	\end{minipage}
18	\caption{\textbf{(a)} Count-degradation curves. Error bars: $\pm 1$ standard deviation (SD) across 3 batch-composition seeds $\times$ 25 batches. RE declines monotonically; NER shows a U-shape. Rightmost points are full-schema (negligible sampling variance). \textbf{(b)} Illustrative BCS-controlled FewRel accuracy: each bar represents one extreme-BCS batch per condition. Slopes are consistent across pool conditions ($p = 0.60$); wider BCS range at 80 relations produces larger gaps. Statistical evidence is provided by the pooled regression (\S\ref{sec:bcs_controlled}, semipartial $R^2 = 0.273$, $n = 204$).}
19	\label{fig:main_results}
20	\end{figure*}
21	
22	\subsection{Tasks and Datasets}
23	\label{sec:datasets}
24	
25	\paragraph{Few-NERD (NER).}
26	\looseness=-1
27	Few-NERD \citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains. We sample 1{,}000 instances uniformly from the test set; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
28	
29	\parag
…[truncated 9105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-26T10:24:00.484445+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	All experiments use Qwen3-32B and the v1 prompt (\S\ref{sec:model}; Appendix~\ref{sec:appendix_prompts}) unless noted; cross-model validation covers Dimensions~1--2, while secondary analyses (error taxonomy, DocRED $R^2$, Two One-Sided Tests [TOST]) remain single-model.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\resizebox{\columnwidth}{!}{%
10	\begin{tabular}{llrrrrr}
11	\toprule
12	\textbf{Dataset} & \textbf{Embed.} & \textbf{$n$ pairs} & \textbf{$r$} & \textbf{$r^2$} & \textbf{95\% CI} & \textbf{$p$} \\
13	\midrule
14	Few-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\,0.001$ \\
15	MAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\,0.001$ \\
16	\bottomrule
17	\end{tabular}}
18	\caption{Pairwise SCS--confusion correlation. Confusion rate is bidirectional $C(t_i{\to}t_j) + C(t_j{\to}t_i)$ divided by gold frequency sum; CIs are percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \S\ref{sec:scs-validation}) excluded (per-instance RE format). Type-level cluster bootstrap CIs exclude zero (Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]).}
19	\label{tab:pairwise}
20	\end{table}
21	
22	\subsection{Count-Degradation Curves}
23	\label{sec:count_curves}
24	
25	\looseness=-1
26	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (85.7\%$\to$50.4\% for FewRel). NER recall drops from 0.72 (count 1) to 0.28 before recovering to 0.41 at full-schema. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%; Appendix~\ref{sec:appendix_figures}); MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The decline is stable across seeds (Jonckheere-Terpstra $p < 0.001$) and replicates on Llama-8B ($-$43\,pp; Table~\ref{tab:cross_model}), Llama-70B, and Gemini Flash (Figure~\ref{fig:cross_model_count}).
27	
28	\subsection{Pairwise Confusability and Type Confusion}
29	\label{sec:pairwise}
30	
31	\lo
…[truncated 7837 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-26T10:24:00.484605+00:00_

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
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-26T10:24:00.484738+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	\looseness=-1
5	\textbf{RQ1} (independent confusability effect): Yes, on RE. BCS independently explains ${\sim}$27\% of cross-batch accuracy variance on FewRel after controlling for count and centrality, replicating across three model scales. The NER null reflects dispersed error modes rather than absence of confusability effects (\S\ref{sec:multi_channel}).
6	\textbf{RQ2} (degradation modes): Count reduces recall overall (monotonically in RE; non-monotonically in NER); confusability drives type substitution (IntraSub) that scales monotonically with BCS. The two dimensions interact with bounded magnitude on the linear scale.
7	\textbf{RQ3} (decomposition): Schema decomposition fails in practice due to routing ambiguity (RE) and merge amplification (NER/ED), though oracle routing confirms the dimensions are separable in principle (\S\ref{sec:sdgd}).
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Intra-batch substitution (IntraSub) and missed rates by BCS bin. IntraSub scales monotonically with BCS across all three datasets. DocRED missed rates decrease with BCS, indicating errors shift from omission to substitution.}
13	\label{tab:error_taxonomy}
14	\resizebox{\columnwidth}{!}{%
15	\begin{tabular}{llrrrrrrr}
16	\toprule
17	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
18	\cmidrule(lr){3-7}
19	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
20	\midrule
21	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
22	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}\,0.001$ \\
23	DocRED & IntraSub & --- & 4.8\% & 22.4\% & 37.0\% & 41.9\% & 0.843 & ${<}\,0.001$ \\
24	\midrule
25	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
26	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
27	DocRED & Missed & --- & 28.1\% & 22
…[truncated 919 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-26T10:24:00.484928+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-26T10:24:00.485087+00:00_

1	% DEPRECATED — this file is no longer included in main.tex.
2	% The active conclusion is in discussion.tex (\input{discussion}).
3	% Kept for reference only; safe to delete.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-26T10:24:00.485218+00:00_

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
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-26T10:24:00.485345+00:00_

1	\section{Schema Decomposition}
2	\label{sec:sdgd}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{../../figures/paper/fig_sdgd_pipeline_compact.pdf}
7	\caption{Schema decomposition pipeline and failure modes. Graph coloring partitions the schema into low-confusability sub-schemas, but two structural bottlenecks prevent practical gains: \textbf{routing failure} in RE (73.4\% of instances match multiple sub-schemas) and \textbf{merge amplification} in NER/ED (union merge increases false positives ${\sim}4\times$).}
8	\label{fig:sdgd_pipeline}
9	\end{figure}
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical strategies perform below the single-pass baseline due to constrained decoding: 73.4\% of instances match multiple sub-schemas simultaneously.}
15	\label{tab:routing_strategies}
16	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}lrr@{}}
17	\toprule
18	\textbf{Strategy} & \textbf{Accuracy} & \textbf{$\Delta$ vs.\ Single-Pass} \\
19	\midrule
20	Oracle (gold label) & 72.4\% & +22.0\,pp \\
21	\midrule
22	Max-conf (positive only) & 36.5\% & $-$14.0\,pp \\
23	None-aware & 36.5\% & $-$14.0\,pp \\
24	Margin (positive only) & 35.9\% & $-$14.5\,pp \\
25	Max-conf (all) & 27.7\% & $-$22.7\,pp \\
26	Random & 14.7\% & $-$35.7\,pp \\
27	\midrule
28	Single-pass (no decomposition) & 50.4\% & --- \\
29	\bottomrule
30	\end{tabular}}
31	\end{table}
32	
33	\looseness=-1
34	A natural intervention is to partition the schema so confusable types never co-occur (Figure~\ref{fig:sdgd_pipeline}). We tested Schema-DAG-Guided Decomposition (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches. While oracle routing recovers accuracy (0.724 vs.\ 0.504 single-pass; Table~\ref{tab:routing_strategies}), all practical routing strategies fall below the single-pass baseline, a
…[truncated 489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-26T10:24:00.485495+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-26T10:24:00.485615+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	
11	\title{Supplementary Material for: How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	All supplementary material is included in the appendix of the main paper.
19	
20	\end{document}
21	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-26T10:24:00.485739+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-26T10:24:00.485916+00:00_

1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},
51	     "start": {"type": "integer"},
52	     "end":   {"type": "integer"}},
53	   "required": ["text","type","start","end"]}}
54	\end{lstlisting}
55	\end{small}
56	
57	\paragraph{v2 prompt (text+type only).}
58	
59	\begin{small}
60	\begin{lstlisting}
61	Extract all named entities from the foll
…[truncated 5211 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-26T10:24:00.486085+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-26T10:24:00.486235+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:discussion}) discusses model coverage, effect size and statistical design (including TOST equivalence), task scope, causal mechanism, data contamination, and domain/language scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	Yes (Limitations). SCS/BCS may be misused as a standalone deployment criterion. Since they are proxies for confusability and do not capture domain-specific ambiguity or downstream harms, they should be used for diagnostic monitoring rather than automatic schema rejection or high-stakes deployment decisions.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \citep{fewnerd-2021}, FewRel \citep{fewrel-2018}, DocRED \citep{docred-2019}, MAVEN \citep{maven-2020}, Qwen3-32B \citep{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and M
…[truncated 4812 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-26T10:24:00.486387+00:00_

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
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-26T10:24:00.486505+00:00_

File content (26245 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-26T10:24:00.486632+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[pt|alt|alp]?\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[pt|alt|alp]?\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-26T10:24:00.486750+00:00_

51:Four English Wikipedia/Wikidata datasets in a zero-shot setting; few-shot, fine-tuned, and non-English scenarios remain untested. BCS predicts RE accuracy but not NER. Cross-dataset consistency is converging evidence, not independent replication \citep{rothman-1990}.
195:[Omitted long matching line]
373:[Omitted long matching line]
569:[Omitted long matching line]
648:[Omitted long matching line]
693:We validate both dimensions on a proprietary model, Gemini 2.5 Flash \citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, Llama) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.
763:[Omitted long matching line]
786:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-26T10:24:00.486898+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "output_mode": "content",
  "head_limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "output_mode": "content",
    "head_limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-26T10:24:00.487022+00:00_

51:Four English Wikipedia/Wikidata datasets in a zero-shot setting; few-shot, fine-tuned, and non-English scenarios remain untested. BCS predicts RE accuracy but not NER. Cross-dataset consistency is converging evidence, not independent replication \citep{rothman-1990}.
195:[Omitted long matching line]
373:[Omitted long matching line]
569:[Omitted long matching line]
648:[Omitted long matching line]
693:We validate both dimensions on a proprietary model, Gemini 2.5 Flash \citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, Llama) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.
763:[Omitted long matching line]
786:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-26T10:24:00.487149+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "1",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "1",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-26T10:24:00.487384+00:00_

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
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{enumitem}
15	\usepackage[normalem]{ulem}
16	\usepackage{listings}
17	
18	\setlength{\textfloatsep}{10pt plus 2pt minus 4pt}
19	\setlength{\floatsep}{10pt plus 2pt minus 4pt}
20	\setlength{\dbltextfloatsep}{10pt plus 2pt minus 4pt}
21	\setlength{\dblfloatsep}{10pt plus 2pt minus 4pt}
22	
23	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{abstract}
31	
32	\input{introduction}
33	
34	\input{related_work}
35	
36	\input{experimental_setup}
37	
38	\input{results}
39	
40	\input{sdgd_negative}
41	
42	\input{discussion}
43	
44	\section*{Limitations}
45	\looseness=-1
46	\textbf{(1)~Model scope.}
47	Primary experiments use Qwen3-32B; cross-model validation covers count and BCS but not secondary analyses. All evidence is correlational.
48	\textbf{(2)~DocRED multicollinearity.}
49	Severe VIF (50.9) prevents reliable BCS quantification; semipartial $R^2{}\,=\,5.6\%$ is directional only.
50	\textbf{(3)~Experimental scope.}
51	Four English Wikipedia/Wikidata datasets in a zero-shot setting; few-shot, fine-tuned, and non-English scenarios remain untested. BCS predicts RE accuracy but not NER. Cross-dataset consistency is converging evidence, not independent replication \citep{rothman-1990}.
52	
53	\section*{Ethical Considerations}
54	This work is a controlled empirical analysis of schema complexity effects on training-free LLM information extraction. All datasets used (Few-NERD, FewRel, DocRED, MAVEN) are publicly available and derived from Wikipedia/Wikidata. No new data was collected, no human subjects were involved, and no crowd-sourced annotation 
…[truncated 39288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-26T10:24:00.487564+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "500",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "500",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-26T10:24:00.487857+00:00_

500	\begin{table}[h]
501	\centering
502	\small
503	\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\ref{sec:appendix_within_pool} for CI interpretation.}
504	\label{tab:within_pool}
505	\resizebox{\columnwidth}{!}{%
506	\begin{tabular}{lrrrrrrr}
507	\toprule
508	& \multicolumn{4}{c}{\textbf{Regression (BCS $\to$ Accuracy)}} & \multicolumn{2}{c}{\textbf{Quartile $\Delta$}} \\
509	\cmidrule(lr){2-5} \cmidrule(lr){6-7}
510	\textbf{Setting} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
511	\midrule
512	Independent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\
513	80-pool $\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\
514	Full 80-rel ($n{=}25$)$^\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\
515	\midrule
516	\multicolumn{7}{l}{\footnotesize Permutation test (16-rel vs.\ 80-pool slopes): $p \approx 0.60$ (5{,}000 permutations)} \\
517	\multicolumn{7}{l}{\footnotesize $^\dagger$BCS range (IQR\,=\,0.033) insufficient for regression; slope not interpretable.} \\
518	\bottomrule
519	\end{tabular}}
520	\end{table}
521	
522	The within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \approx 0.60$). The smaller quartile gap ($-$3.92\,pp vs.\ $-$5.31\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\ref{sec:appendix_within_pool}).
523	
524	In the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \approx 0.76$). This does not invalidate the confusability effect; the within-pool
…[truncated 33537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-26T10:24:00.488153+00:00_

Now I have all the content from the .tex files. Let me compile a comprehensive list of all citations with their surrounding context.

## Complete Citation Extract from All .tex Files

Based on my thorough review of all the specified .tex files, here is a complete list of every citation command with its surrounding context:

### **abstract.tex**
No citation commands found.

### **introduction.tex**

1. **\citep{llm4ie-survey-2024}**
   - Context: "This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \citep{llm4ie-survey-2024}."

2. **\citep{uniner-2024,llm-pee-2025,parse-2025}**
   - Context: "Prior decomposition strategies \citep{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability)."

3. **\citealt{llm-pee-2025}**
   - Context: "We quantify confusability using pairwise embedding similarity, the \emph{Schema Confusability Score} (SCS), and its batch-level aggregation, the \emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \citep{fewnerd-2021}, FewRel \citep{fewrel-2018}, DocRED \citep{docred-2019}, and MAVEN \citep{maven-2020} using Qwen3-32B (\S\ref{sec:experimental_setup}). Our contributions are: We find that type confusability, quantified by embedding similarity (SCS/BCS, building on \citealt{llm-pee-2025})."

4. **\citep{fewnerd-2021}**
   - Context: "We evaluate on Few-NERD \citep{fewnerd-2021}, FewRel \citep{fewrel-2018}, DocRED \citep{docred-2019}, and MAVEN \citep{maven-2020} using Qwen3-32B."

5. **\citep{fewrel-2018}**
   - Context: "We evaluate on Few-NERD \citep{fewnerd-2021}, FewRel \citep{fewrel-2018}, DocRED \citep{docred-2019}, and MAVEN \citep{maven-2020} using Qwen3-32B."

6. **\citep{docred-2019}**
   - Context: "We evaluate on Few-NERD \citep{fewnerd-2021}, FewRel \citep{fewrel-2018}, DocRED \citep{docred-2019}, and 
…[truncated 15145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Agent",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T10:24:00.488351+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Familiarity Better Evaluation Zero-Shot Named Entity Recognition Quantifying Label Shifts Synthetic Training Data Golde 2025 NAACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Familiarity Better Evaluation Zero-Shot Named Entity Recognition Quantifying Label Shifts Synthetic Training Data Golde 2025 NAACL"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-26T10:24:00.488480+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Cohen 1988 \"Statistical Power Analysis for the Behavioral Sciences\" second edition"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Cohen 1988 \"Statistical Power Analysis for the Behavioral Sciences\" second edition"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-26T10:24:00.488601+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Orlikowski \"Ecological Fallacy in Annotation\" ACL 2023 short papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Orlikowski \"Ecological Fallacy in Annotation\" ACL 2023 short papers"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-26T10:24:00.488718+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Josifoski \"GenIE Generative Information Extraction\" NAACL 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Josifoski \"GenIE Generative Information Extraction\" NAACL 2022"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-26T10:24:00.489036+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dubey \"Pairwise Confusion for Fine-Grained Visual Classification\" ECCV 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dubey \"Pairwise Confusion for Fine-Grained Visual Classification\" ECCV 2018"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-26T10:24:00.489161+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Collier \"Correlated Input-Dependent Label Noise in Large-Scale Image Classification\" CVPR 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Collier \"Correlated Input-Dependent Label Noise in Large-Scale Image Classification\" CVPR 2021"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-26T10:24:00.489277+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Yin Hay Roth \"Benchmarking Zero-shot Text Classification Datasets Evaluation Entailment\" EMNLP 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Yin Hay Roth \"Benchmarking Zero-shot Text Classification Datasets Evaluation Entailment\" EMNLP 2019"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-26T10:24:00.489389+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Schuirmann 1987 \"Two One-Sided Tests Procedure\" equivalence bioavailability Journal Pharmacokinetics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Schuirmann 1987 \"Two One-Sided Tests Procedure\" equivalence bioavailability Journal Pharmacokinetics"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-26T10:24:00.489536+00:00_

Web search results for query: "Cohen 1988 "Statistical Power Analysis for the Behavioral Sciences" second edition"

Links: [{"title":"Statistical Power Analysis for the Behavioral Sciences - 2nd Edition -","url":"https://www.routledge.com/Statistical-Power-Analysis-for-the-Behavioral-Sciences/Cohen/p/book/9780805802832"},{"title":"Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences (2nd ed.). Routledge. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3845582"},{"title":"Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences (2nd ed.). Hillsdale, NJ Lawrence Erlbaum Associates, Publishers. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/ReferencesPapers?ReferenceID=2041144"},{"title":"Statistical Power Analysis for the Behavioral Sciences (2nd Edition): Cohen, Jacob: 9780805802832: Amazon.com: Books","url":"https://www.amazon.com/Statistical-Power-Analysis-Behavioral-Sciences/dp/0805802835"},{"title":"Statistical Power Analysis for the Behavioral Sciences (2nd Edition) - Cohen, Jacob: 9780805802832 - AbeBooks","url":"https://www.abebooks.com/9780805802832/Statistical-Power-Analysis-Behavioral-Sciences-0805802835/plp"},{"title":"Statistical Power Analysis for the Behavioral Sciences || - DOKUMEN.PUB","url":"https://dokumen.pub/statistical-power-analysis-for-the-behavioral-sciences.html"},{"title":"Statistical Power Analysis for the Behavioral Sciences 2nd edition | 9780805802832, 9781134742776 | VitalSource","url":"https://www.vitalsource.com/products/statistical-power-analysis-for-the-behavioral-jacob-cohen-v9781134742776"},{"title":"Cohen, J. (1988) Statistical Power Analysis for the Behavioral Sciences. 2nd Edition, Lawrence Erlbaum Associates, Hillsdale, New Jersey. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3222582"},{"title":"Cohen, J. (1988) Statist
…[truncated 1254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-26T10:24:00.489720+00:00_

Web search results for query: "Orlikowski "Ecological Fallacy in Annotation" ACL 2023 short papers"

Links: [{"title":"The Ecological Fallacy in Annotation: Modeling Human Label Variation goes beyond Sociodemographics - ACL Anthology","url":"https://aclanthology.org/2023.acl-short.88/"},{"title":"The Ecological Fallacy in Annotation: Modelling Human ...","url":"https://aclanthology.org/2023.acl-short.88.pdf"},{"title":"[2306.11559] The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics","url":"https://arxiv.org/abs/2306.11559"},{"title":"Matthias Orlikowski - Research in Natural Language Processing and Computational Social Science","url":"https://orlikow.ski/"},{"title":"The Ecological Fallacy in Annotation: Modeling Human Label Variation goes beyond Sociodemographics | Dirk Hovy","url":"https://www.dirkhovy.com/publication/2023-ecological-fallacy-annotation-modeling-human-label-variation-goes-beyond-sociodemographics/"},{"title":"morlikowski/ecological-fallacy: Code for Orlikowski et al. (2023)","url":"https://github.com/morlikowski/ecological-fallacy"},{"title":"The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics","url":"https://arxiv.org/html/2306.11559"},{"title":"The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics","url":"https://www.emergentmind.com/papers/2306.11559"},{"title":"(PDF) The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics","url":"https://www.researchgate.net/publication/371728925_The_Ecological_Fallacy_in_Annotation_Modelling_Human_Label_Variation_goes_beyond_Sociodemographics"},{"title":"The Ecological Fallacy in Annotation: Modelling Human Label Variation   goes beyond Sociodemographics","url":"https://arxiv.org/pdf/2306.11559"}]

I found the paper! Here are the search results:

The paper is "The Ecological Fallacy in Annotation: Modeling Human Label Variatio
…[truncated 1298 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-26T10:24:00.489932+00:00_

Web search results for query: "Dubey "Pairwise Confusion for Fine-Grained Visual Classification" ECCV 2018"

Links: [{"title":"Pairwise Confusion for Fine-Grained Visual Classification","url":"https://openaccess.thecvf.com/content_ECCV_2018/papers/Abhimanyu_Dubey_Improving_Fine-Grained_Visual_ECCV_2018_paper.pdf"},{"title":"GitHub - abhimanyudubey/confusion: Code for the ECCV 2018 paper \"Pairwise Confusion for Fine-Grained Visual Classification\" · GitHub","url":"https://github.com/abhimanyudubey/confusion"},{"title":"dblp: Pairwise Confusion for Fine-Grained Visual Classification.","url":"https://dblp.org/rec/conf/eccv/DubeyGGRFN18.html"},{"title":"[1705.08016] Pairwise Confusion for Fine-Grained Visual Classification","url":"https://arxiv.org/abs/1705.08016"},{"title":"Pairwise Confusion for Fine-Grained Visual Classification | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-030-01258-8_5"},{"title":"Fine-Grained Visual Classification via Progressive Multi-granularity Training of Jigsaw Patches | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-030-58565-5_10"},{"title":"[PDF] Pairwise Confusion for Fine-Grained Visual Classification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Pairwise-Confusion-for-Fine-Grained-Visual-Dubey-Gupta/20cc4bfdb648fd7947c71252589fc867d4d16933"},{"title":"Fine-grained visual classification with multi-scale features based on self-supervised attention filtering mechanism | Applied Intelligence","url":"https://link.springer.com/article/10.1007/s10489-022-03232-w"},{"title":"Awesome Fine-Grained Image Analysis – Papers, Codes and Datasets","url":"http://www.weixiushen.com/project/Awesome_FGIA/Awesome_FGIA.html"}]

I found the paper you're looking for! Here are the key details:

**Paper Information:**

The paper "Pairwise Confusion for Fine-Grained Visual Classification" was authored by Abhimanyu Dubey, Otkrist Gupta, Pei Guo, Ramesh Raskar, Ryan Farrell, and Nikhil Naik,
…[truncated 984 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T10:24:00.490118+00:00_

Web search results for query: "Josifoski "GenIE Generative Information Extraction" NAACL 2022"

Links: [{"title":"GenIE: Generative Information Extraction - ACL Anthology","url":"https://aclanthology.org/2022.naacl-main.342/"},{"title":"GenIE: Generative Information Extraction","url":"https://dlab.epfl.ch/people/west/pub/Josifoski-DeCao-Peyrard-Petroni-West_NAACL-22.pdf"},{"title":"GitHub - epfl-dlab/GenIE: The autoregressive information extraction system GenIE (Generative Information Extraction) implemented in PyTorch. · GitHub","url":"https://github.com/epfl-dlab/GenIE"},{"title":"(PDF) GenIE: Generative Information Extraction","url":"https://www.researchgate.net/publication/362262820_GenIE_Generative_Information_Extraction"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=GenIE:+Generative+information+extraction&amp=&author=Martin+Josifoski&amp=&author=Nicola+De+Cao&amp=&author=Maxime+Peyrard&amp=&author=Fabio+Petroni&amp=&author=Robert+West&amp=&publication_year=2022&amp=&pages=4626-4643&amp=&doi=10.18653/v1/2022.naacl-main.342"},{"title":"[2112.08340] GenIE: Generative Information Extraction","url":"https://arxiv.org/abs/2112.08340"},{"title":"GenIE: Generative Information Extraction","url":"https://infoscience.epfl.ch/entities/publication/ac96118e-64f4-4d05-8461-aa27321afaeb"},{"title":"Accepted Papers - NAACL-HLT 2022","url":"https://2022.naacl.org/program/accepted_papers/"},{"title":"GenIE: Generative Information Extraction | OpenReview","url":"https://openreview.net/forum?id=HxxjO7zS-c"}]

I found the paper you're looking for. Here are the key details about the GenIE paper:

GenIE: Generative Information Extraction is a paper by Martin Josifoski, Nicola De Cao, Maxime Peyrard, Fabio Petroni, and Robert West, published at NAACL 2022. The paper appears in the Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (pages 4626–4643, Seattle).
…[truncated 935 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-26T10:24:00.490307+00:00_

Web search results for query: "Yin Hay Roth "Benchmarking Zero-shot Text Classification Datasets Evaluation Entailment" EMNLP 2019"

Links: [{"title":"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach - ACL Anthology","url":"https://aclanthology.org/D19-1404/"},{"title":"GitHub - yinwenpeng/BenchmarkingZeroShot · GitHub","url":"https://github.com/yinwenpeng/BenchmarkingZeroShot"},{"title":"Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach | Request PDF","url":"https://www.researchgate.net/publication/335599580_Benchmarking_Zero-shot_Text_Classification_Datasets_Evaluation_and_Entailment_Approach"},{"title":"Benchmarking Zero-shot Text Classification: Datasets ...","url":"https://cogcomp.seas.upenn.edu/papers/YinHaRo19.pdf"},{"title":"GitHub - CogComp/Benchmarking-Zero-shot-Text-Classification: Code for EMNLP2019 paper : \"Benchmarking zero-shot text classification: datasets, evaluation and entailment approach\" · GitHub","url":"https://github.com/CogComp/Benchmarking-Zero-shot-Text-Classification"},{"title":"[PDF] Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Benchmarking-Zero-shot-Text-Classification:-and-Yin-Hay/093d9253a2fe765ca6577b091d3f99bab3155a7d"},{"title":"[1909.00161] Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach","url":"https://arxiv.org/abs/1909.00161"},{"title":"[Quick Review] Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach","url":"https://liner.com/review/benchmarking-zeroshot-text-classification-datasets-evaluation-and-entailment-approach"},{"title":"Google Académico","url":"https://scholar.google.com/scholar?q=Wenpeng+Yin,+Jamaal+Hay,+and+Dan+Roth.+2019.+Benchmarking+Zero-shot+Text+Classification:+Datasets,+Evaluation+and+Entailment+Approach.+In+EMNLP."},{"title":"Exploring Universal 
…[truncated 1410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-26T10:24:00.490489+00:00_

Web search results for query: "Collier "Correlated Input-Dependent Label Noise in Large-Scale Image Classification" CVPR 2021"

Links: [{"title":"Correlated Input-Dependent Label Noise in Large-Scale Image Classiﬁcation","url":"https://openaccess.thecvf.com/content/CVPR2021/papers/Collier_Correlated_Input-Dependent_Label_Noise_in_Large-Scale_Image_Classification_CVPR_2021_paper.pdf"},{"title":"Related Material - CVPR 2021 Open Access Repository","url":"https://openaccess.thecvf.com/content/CVPR2021/html/Collier_Correlated_Input-Dependent_Label_Noise_in_Large-Scale_Image_Classification_CVPR_2021_paper.html"},{"title":"[2105.10305] Correlated Input-Dependent Label Noise in Large-Scale Image Classification","url":"https://arxiv.org/abs/2105.10305"},{"title":"Correlated Input-Dependent Label Noise in Large-Scale Image Classification - researchr publication","url":"https://researchr.org/publication/CollierMKJB21"},{"title":"[PDF] Correlated Input-Dependent Label Noise in Large-Scale Image Classification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Correlated-Input-Dependent-Label-Noise-in-Image-Collier-Mustafa/6ac8e0915df41692bdceef7f18bc1c50271630fc"},{"title":"Correlated Input-Dependent Label Noise in Large-Scale Image Classification | Request PDF","url":"https://www.researchgate.net/publication/355866332_Correlated_Input-Dependent_Label_Noise_in_Large-Scale_Image_Classification"},{"title":"Correlated Input-Dependent Label Noise in Large-Scale Image Classification - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210510305C/abstract"},{"title":"Correlated Input-Dependent Label Noise in Large-Scale Image Classification","url":"https://research.google/pubs/correlated-input-dependent-label-noise-in-large-scale-image-classification/"},{"title":"Papers with Code - Correlated Input-Dependent Label Noise in Large-Scale Image Classification","url":"https://paperswithcode.com/paper/correlated-input-dependent-label-noise-in"}]

I found the paper! Here'
…[truncated 1149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-26T10:24:00.490665+00:00_

Web search results for query: "Schuirmann 1987 "Two One-Sided Tests Procedure" equivalence bioavailability Journal Pharmacokinetics"

Links: [{"title":"A comparison of the Two One-Sided Tests Procedure and the Power Approach for assessing the equivalence of average bioavailability | Journal of Pharmacokinetics and Pharmacodynamics | Springer Nature Link","url":"https://link.springer.com/article/10.1007/BF01068419"},{"title":"[PDF] A comparison of the Two One-Sided Tests Procedure and the Power Approach for assessing the equivalence of average bioavailability | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-comparison-of-the-Two-One-Sided-Tests-Procedure-Schuirmann/053b97e316fc43588e6235f88a1a7a4077342de7"},{"title":"(PDF) Probabilities and sample sizes for the two one-sided tests procedure","url":"https://www.researchgate.net/publication/233170910_Probabilities_and_sample_sizes_for_the_two_one-sided_tests_procedure"},{"title":"Probabilities and sample sizes for the two one-sided tests procedure: Communications in Statistics - Theory and Methods: Vol 22, No 7","url":"https://www.tandfonline.com/doi/abs/10.1080/03610929308831127"},{"title":"A comparison of the two one-sided tests procedure and the power approach for assessing the equivalence of average bioavailability - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/3450848/?dopt=Abstract"},{"title":"(Open Access) A comparison of the Two One-Sided Tests Procedure and the Power Approach for assessing the equivalence of average bioavailability (1987) | Donald J. Schuirmann | 2437 Citations","url":"https://scispace.com/papers/a-comparison-of-the-two-one-sided-tests-procedure-and-the-17764djo4q"},{"title":"Schuirmann, D. (1987) A comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability. Journal of Pharmacokinetics and Biopharmaceutics, 15, 657-680. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/R
…[truncated 1147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-26T10:24:00.490862+00:00_

Web search results for query: "Familiarity Better Evaluation Zero-Shot Named Entity Recognition Quantifying Label Shifts Synthetic Training Data Golde 2025 NAACL"

Links: [{"title":"[2412.10121] Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data","url":"https://arxiv.org/abs/2412.10121"},{"title":"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.37/"},{"title":"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data","url":"https://arxiv.org/html/2412.10121v1"},{"title":"GitHub - flairNLP/familiarity: Label shift estimation for transfer difficulty with Familiarity.","url":"https://github.com/flairNLP/familiarity"},{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"},{"title":"(PDF) Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data","url":"https://www.researchgate.net/publication/387078555_Familiarity_Better_Evaluation_of_Zero-Shot_Named_Entity_Recognition_by_Quantifying_Label_Shifts_in_Synthetic_Training_Data"},{"title":"Alan AKBIK | Professor | Doctor of Engineering | Humboldt-Universität zu Berlin, Berlin | HU Berlin | Department of Computer Science | Research profile","url":"https://www.researchgate.net/profile/Alan-Akbik-2"},{"title":"Alan Akbik - Professor of Machine Learning","url":"https://alanakbik.github.io/"}]

I found the paper! Here are the key details:

**Paper Title:** Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data (Golde et al., NAACL 2025)

**Main Contribution:** The paper proposes Familiarity, a novel metric that captures both the semantic similarity between entity types in trai
…[truncated 1026 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-26T10:24:00.491064+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gemini 2.5 technical report arXiv 2507.06261 Google 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gemini 2.5 technical report arXiv 2507.06261 Google 2025"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-26T10:24:00.491210+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Snell Swersky Zemel \"Prototypical Networks for Few-shot Learning\" NeurIPS 2017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Snell Swersky Zemel \"Prototypical Networks for Few-shot Learning\" NeurIPS 2017"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-26T10:24:00.491341+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Müller Kornblith Hinton \"When Does Label Smoothing Help\" NeurIPS 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Müller Kornblith Hinton \"When Does Label Smoothing Help\" NeurIPS 2019"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-26T10:24:00.491462+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Peterson Battleday Griffiths Russakovsky \"Human Uncertainty Makes Classification More Robust\" ICCV 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Peterson Battleday Griffiths Russakovsky \"Human Uncertainty Makes Classification More Robust\" ICCV 2019"
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-26T10:24:00.491586+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Willard Louf \"Efficient Guided Generation for Large Language Models\" arXiv 2307.09702"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Willard Louf \"Efficient Guided Generation for Large Language Models\" arXiv 2307.09702"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-26T10:24:00.491703+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Liu Wenxuan Li Zixuan \"LLM-based Collaborative Annotation Partitioning Extraction\" EMNLP 2025 event extraction massive types"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Liu Wenxuan Li Zixuan \"LLM-based Collaborative Annotation Partitioning Extraction\" EMNLP 2025 event extraction massive types"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-26T10:24:00.491816+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Shrimal Jain Chowdhury \"PARSE LLM Driven Schema Optimization Reliable Entity Extraction\" EMNLP 2025 industry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Shrimal Jain Chowdhury \"PARSE LLM Driven Schema Optimization Reliable Entity Extraction\" EMNLP 2025 industry"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-26T10:24:00.491987+00:00_

Web search results for query: "Gemini 2.5 technical report arXiv 2507.06261 Google 2025"

Links: [{"title":"[2507.06261] Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities","url":"https://arxiv.org/abs/2507.06261"},{"title":"Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long","url":"https://arxiv.org/pdf/2507.06261"},{"title":"(PDF) Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities","url":"https://www.researchgate.net/publication/393539209_Gemini_25_Pushing_the_Frontier_with_Advanced_Reasoning_Multimodality_Long_Context_and_Next_Generation_Agentic_Capabilities"},{"title":"[2507.06261] Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities – Papiers","url":"https://papiers.ai/2507.06261"},{"title":"Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250706261C/abstract"},{"title":"[2507.06261v1] Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities","url":"https://arxiv.org/abs/2507.06261v1"},{"title":"[2507.06261v5] Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities","url":"https://arxiv.org/abs/2507.06261v5"},{"title":"[2507.06261v3] Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities","url":"https://arxiv.org/abs/2507.06261v3"}]

I found the technical report you're looking for. Here's what I found:

The paper arXiv:2507.06261 is titled "Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilitie
…[truncated 1098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-26T10:24:00.492132+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lu Meng Xie Yuzhang \"CROSSAGENTIE Cross-Type Cross-Task Multi-Agent LLM Zero-Shot Information Extraction\" ACL 2025 Findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lu Meng Xie Yuzhang \"CROSSAGENTIE Cross-Type Cross-Task Multi-Agent LLM Zero-Shot Information Extraction\" ACL 2025 Findings"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-26T10:24:00.492288+00:00_

Web search results for query: "Snell Swersky Zemel "Prototypical Networks for Few-shot Learning" NeurIPS 2017"

Links: [{"title":"Prototypical Networks for Few-shot Learning","url":"https://papers.nips.cc/paper/6996-prototypical-networks-for-few-shot-learning"},{"title":"[1703.05175] Prototypical Networks for Few-shot Learning","url":"https://arxiv.org/abs/1703.05175"},{"title":"Prototypical Networks for Few-shot Learning","url":"https://proceedings.neurips.cc/paper_files/paper/2017/hash/cb8da6767461f2812ae4290eac7cbc42-Abstract.html"},{"title":"GitHub - jakesnell/prototypical-networks: Code for the NeurIPS 2017 Paper \"Prototypical Networks for Few-shot Learning\" · GitHub","url":"https://github.com/jakesnell/prototypical-networks"},{"title":"Prototypical Networks for Few-shot Learning Jake Snell University of Toronto∗","url":"https://www.cs.toronto.edu/~zemel/documents/prototypical_networks_nips_2017.pdf"},{"title":"Prototypical networks for few-shot learning | Proceedings of the 31st International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3294996.3295163"},{"title":"[PDF] Prototypical Networks for Few-shot Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Prototypical-Networks-for-Few-shot-Learning-Snell-Swersky/c269858a7bb34e8350f2442ccf37797856ae9bca"},{"title":"[Quick Review] Prototypical Networks for Few-shot Learning","url":"https://liner.com/review/prototypical-networks-for-fewshot-learning"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Snell%2C+J.%2C+Swersky%2C+K.%2C+Zemel%2C+R.%3A+Prototypical+networks+for+few-shot+learning.+In%3A+NIPS+%282017%29"},{"title":"Prototypical Networks for Few-shot Learning: Supplementary Material Jake Snell","url":"https://jakesnell.com/pdf/prototypical_networks_neurips_2017_supplemental.pdf"}]

I found the paper "Prototypical Networks for Few-shot Learning" by Jake Snell, Kevin Swersky, and Richard Zemel from NeurIPS 2017.

Here 
…[truncated 1325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-26T10:24:00.492479+00:00_

Web search results for query: "Peterson Battleday Griffiths Russakovsky "Human Uncertainty Makes Classification More Robust" ICCV 2019"

Links: [{"title":"Human Uncertainty Makes Classification More Robust","url":"https://openaccess.thecvf.com/content_ICCV_2019/papers/Peterson_Human_Uncertainty_Makes_Classification_More_Robust_ICCV_2019_paper.pdf"},{"title":"Human uncertainty makes classification more robust - Princeton University","url":"https://collaborate.princeton.edu/en/publications/human-uncertainty-makes-classification-more-robust/"},{"title":"Human uncertainty makes classification more robust","url":"https://gfx.cs.princeton.edu/pubs/Peterson_2019_HUM/index.php"},{"title":"[1908.07086] Human uncertainty makes classification more robust","url":"https://arxiv.org/abs/1908.07086"},{"title":"Human uncertainty makes classification more robust, ICCV 2019 Review | PPT","url":"https://www.slideshare.net/slideshow/human-uncertainty-makes-classification-more-robust-iccv-2019-review/177625925"},{"title":"[PDF] Human Uncertainty Makes Classification More Robust | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Human-Uncertainty-Makes-Classification-More-Robust-Peterson-Battleday/d2a2be6ce932a0f1939f31cfff4d64ea3d76723d"},{"title":"Human uncertainty makes classification more robust - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190807086P/abstract"},{"title":"Human Uncertainty Makes Classification More Robust | Request PDF","url":"https://www.researchgate.net/publication/335243909_Human_Uncertainty_Makes_Classification_More_Robust"},{"title":"Figure 3 from Human Uncertainty Makes Classification More Robust | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Human-Uncertainty-Makes-Classification-More-Robust-Peterson-Battleday/d2a2be6ce932a0f1939f31cfff4d64ea3d76723d/figure/4"},{"title":"GitHub - jcpeterson/cifar-10h: Original dataset release for CIFAR-10H · GitHub","url":"https://github.com/jcpeterson/cifar-10h"}]

I found the paper!
…[truncated 1286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-26T10:24:00.492673+00:00_

Web search results for query: "Müller Kornblith Hinton "When Does Label Smoothing Help" NeurIPS 2019"

Links: [{"title":"When does label smoothing help?","url":"https://papers.nips.cc/paper/8717-when-does-label-smoothing-help"},{"title":"[1906.02629] When Does Label Smoothing Help?","url":"https://arxiv.org/abs/1906.02629"},{"title":"When Does Label Smoothing Help?","url":"http://papers.neurips.cc/paper/8717-when-does-label-smoothing-help.pdf"},{"title":"Rafael Müller, Simon Kornblith, Geoffrey Hinton When does label smoothing help?","url":"https://neurips.cc/media/neurips-2019/Slides/15717.pdf"},{"title":"[PDF] When Does Label Smoothing Help? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/When-Does-Label-Smoothing-Help-M%C3%BCller-Kornblith/f8de25118af2abc4c48afb947d6ec298e05ef1e5"},{"title":"When Does Label Smoothing Help?","url":"https://bibbase.org/network/publication/mller-kornblith-hinton-whendoeslabelsmoothinghelp-2019"},{"title":"When does label smoothing help?","url":"https://nips.cc/media/Slides/nips/2019/westballa+b(12-10-05)-12-10-30-15717-when_does_label.pdf"},{"title":"When Does Label Smoothing Help? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190602629M/abstract"},{"title":"[Re] When Does Label Smoothing Help? · Issue #75 · ReScience/submissions","url":"https://github.com/ReScience/submissions/issues/75"},{"title":"🚧 2019: When Does Label Smoothing Help? · Issue #382 · jojonki/arXivNotes","url":"https://github.com/jojonki/arXivNotes/issues/382"}]

I found the paper! Here are the key details about the paper "When Does Label Smoothing Help?" by Müller, Kornblith, and Hinton, published at NeurIPS 2019.

**Main Contributions:**

The paper discusses how the generalization and learning speed of a multi-class neural network can often be significantly improved by using soft targets that are a weighted average of the hard targets and the uniform distribution over labels. 

The authors show empirically that in addition to improvin
…[truncated 660 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-26T10:24:00.492908+00:00_

Web search results for query: "Willard Louf "Efficient Guided Generation for Large Language Models" arXiv 2307.09702"

Links: [{"title":"[2307.09702] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702"},{"title":"Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/pdf/2307.09702"},{"title":"Paper page - Efficient Guided Generation for Large Language Models","url":"https://huggingface.co/papers/2307.09702"},{"title":"[PDF] Efficient Guided Generation for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Guided-Generation-for-Large-Language-Willard-Louf/c4ceaef35bca063815f50d90a087acbd07a65478"},{"title":"Efficient Guided Generation for Large Language Models","url":"https://www.researchhub.com/paper/1278292/efficient-guided-generation-for-large-language-models"},{"title":"[2307.09702v3] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702v3"},{"title":"Efficient Guided Generation for Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230709702W/abstract"},{"title":"[2307.09702v2] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702v2"},{"title":"dblp: Efficient Guided Generation for Large Language Models.","url":"https://dblp.org/rec/journals/corr/abs-2307-09702.html"},{"title":"AI-Powered Paper Summarization about the arXiv paper 2307.09702v3","url":"https://www.summarizepaper.com/en/arxiv-id/2307.09702v3/"}]

I found the paper! Here are the details:

**Paper Title:** Efficient Guided Generation for Large Language Models

**Authors:** Brandon T. Willard and Rémi Louf

**arXiv ID:** 2307.09702

**Publication Date:** July 19, 2023

**Summary:** The paper shows how the problem of neural text generation can be constructively reformulated in terms of transitions between the states of a finite-state machine. This framework leads to an efficient a
…[truncated 632 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-26T10:24:00.493129+00:00_

Web search results for query: "Liu Wenxuan Li Zixuan "LLM-based Collaborative Annotation Partitioning Extraction" EMNLP 2025 event extraction massive types"

Links: [{"title":"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1743/"},{"title":"[2503.02628] Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction","url":"https://arxiv.org/abs/2503.02628"},{"title":"[2503.02628] Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction - Academus scientific article reader","url":"https://academ.us/article/2503.02628/"},{"title":"Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction","url":"https://arxiv.org/html/2503.02628v1"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Towards Event Extraction with Massive Types: LLM-based ...","url":"https://aclanthology.org/2025.emnlp-main.1743.pdf"},{"title":"Towards Event Extraction with Massive Types: LLM-based Collaborative","url":"https://arxiv.org/pdf/2503.02628"},{"title":"KnowCoder-X: Boosting Multilingual Information Extraction via Code - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.748/"}]

Based on the search results, I found the paper you're looking for:

The paper "Towards Event Extraction with Massive Types: LLM-based Collaborative Annotation and Partitioning Extraction" was authored by Wenxuan Liu, Zixuan Li, Long Bai, Yuxin Zuo, Daozhu Xu, Xiaolong Jin, Jiafeng Guo, and Xueqi Cheng and was presented at EMNLP 2025. It was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 34377–34399, in Suzhou, China.

The paper addresses the challenge of developing a general-purpose extraction system that c
…[truncated 607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-26T10:24:00.493309+00:00_

Web search results for query: "Lu Meng Xie Yuzhang "CROSSAGENTIE Cross-Type Cross-Task Multi-Agent LLM Zero-Shot Information Extraction" ACL 2025 Findings"

Links: [{"title":"CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.718/"},{"title":"Cross-Type and Cross-Task Multi-Agent LLM Collaboration ...","url":"https://aclanthology.org/2025.findings-acl.718.pdf"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"ACL 2025 Conference Overview | PDF","url":"https://www.scribd.com/document/930908301/2025-acl-long-0"},{"title":"Findings of the Association for Computational Linguistics (2025) - ACL Anthology","url":"https://aclanthology.org/events/findings-2025/"},{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"},{"title":"SLAM-Omni: Timbre-Controllable Voice Interaction System with Single-Stage Training - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.115/"}]

I found the paper you're looking for! Here's the information:

The paper "CROSSAGENTIE: Cross-Type and Cross-Task Multi-Agent LLM Collaboration for Zero-Shot Information Extraction" is authored by Meng Lu, Yuzhang Xie, Zhenyu Bi, Shuxiang Cao, and Xuan Wang, and was published in the Findings of the Association for Computational Linguistics: ACL 2025, pages 13953–13977, Vienna, Austria.

The paper proposes CROSSAGENTIE, a multi-agent framework that enhances zero-shot IE through multi-agent LLM collaboration, using intra-group cross-type debate to resolve entity-label conflicts and inter-group cross-task debate where NER and RE mutually refine outputs. The authors also introduce template fine-tuning to distill high-confidence multi-agent outputs into a single model. The experiments across five NER and five RE datasets show that CROSSAGENTIE significantly outperforms stat
…[truncated 219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-26T10:24:00.493481+00:00_

Web search results for query: "Shrimal Jain Chowdhury "PARSE LLM Driven Schema Optimization Reliable Entity Extraction" EMNLP 2025 industry"

Links: [{"title":"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/html/2510.08623v1"},{"title":"[2510.08623] PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://arxiv.org/abs/2510.08623"},{"title":"PARSE: LLM driven schema optimization for reliable entity extraction - Amazon Science","url":"https://www.amazon.science/publications/parse-llm-driven-schema-optimization-for-reliable-entity-extraction"},{"title":"PARSE: LLM Driven Schema Optimization for Reliable ...","url":"https://aclanthology.org/2025.emnlp-industry.184.pdf"},{"title":"(PDF) PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction","url":"https://www.researchgate.net/publication/396458126_PARSE_LLM_Driven_Schema_Optimization_for_Reliable_Entity_Extraction"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=13775&show=25"},{"title":"Machine Learning Oct 2025","url":"https://arxiv.org/list/cs.LG/2025-10?skip=3600&show=250"}]

Based on the search results, I found the paper you're looking for:

**PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction** is authored by Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, and Promod Yenigalla from RBS Tech Sciences at Amazon. Note that the author name in your query is "Shrimal Jain Chowdhury," but the actual authors are Anubhav Shrimal, Aryan Jain, and Soumyajit Chowdhury (three separate individuals).

The paper was accepted to the EMNLP 2025 Industry Track. The work addresses structured information extraction from unstructured text for Software 3.0 systems, and recognizes that JSON schemas are a form of natural language understanding contract that LLMs can interpret and improve.

The PARSE framework processes unoptimized schemas and input text through ARCHITECT for schema refineme
…[truncated 169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-26T10:24:00.493668+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang Zihan \"Cooperative Multi-Agent Framework Zero-Shot Named Entity Recognition\" ACM Web Conference 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang Zihan \"Cooperative Multi-Agent Framework Zero-Shot Named Entity Recognition\" ACM Web Conference 2025"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-26T10:24:00.493796+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhou Wenxuan \"UniversalNER Targeted Distillation Large Language Models Open Named Entity Recognition\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhou Wenxuan \"UniversalNER Targeted Distillation Large Language Models Open Named Entity Recognition\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-26T10:24:00.493950+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sainz \"GoLLIE Annotation Guidelines improve Zero-Shot Information-Extraction\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sainz \"GoLLIE Annotation Guidelines improve Zero-Shot Information-Extraction\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-26T10:24:00.494139+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zaratiana \"GLiNER Generalist Model Named Entity Recognition Bidirectional Transformer\" NAACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zaratiana \"GLiNER Generalist Model Named Entity Recognition Bidirectional Transformer\" NAACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-26T10:24:00.494493+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zaratiana \"GLiNER2 Schema-Driven Multi-Task Learning Structured Information Extraction\" EMNLP 2025 system demonstrations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zaratiana \"GLiNER2 Schema-Driven Multi-Task Learning Structured Information Extraction\" EMNLP 2025 system demonstrations"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-26T10:24:00.494632+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gui Honghao \"IEPile Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\" ACL 2024 short papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gui Honghao \"IEPile Unearthing Large Scale Schema-Conditioned Information Extraction Corpus\" ACL 2024 short papers"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-26T10:24:00.494755+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dror Baumer Shlomov Reichart \"Hitchhiker's Guide Testing Statistical Significance NLP\" ACL 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dror Baumer Shlomov Reichart \"Hitchhiker's Guide Testing Statistical Significance NLP\" ACL 2018"
  }
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-26T10:24:00.494969+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Liu Nelson \"Lost in the Middle How Language Models Use Long Contexts\" TACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Liu Nelson \"Lost in the Middle How Language Models Use Long Contexts\" TACL 2024"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-26T10:24:00.495205+00:00_

Web search results for query: "Wang Zihan "Cooperative Multi-Agent Framework Zero-Shot Named Entity Recognition" ACM Web Conference 2025"

Links: [{"title":"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714923"},{"title":"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition | Request PDF","url":"https://www.researchgate.net/publication/391467195_A_Cooperative_Multi-Agent_Framework_for_Zero-Shot_Named_Entity_Recognition"},{"title":"GitHub - WZH-NLP/WWW25-CMAS","url":"https://github.com/WZH-NLP/WWW25-CMAS"},{"title":"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition","url":"https://arxiv.org/html/2502.18702v1"},{"title":"[2502.18702] A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition","url":"https://arxiv.org/abs/2502.18702"},{"title":"[PDF] A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Cooperative-Multi-Agent-Framework-for-Zero-Shot-Wang-Zhao/cec61b51f6eed5e3c253f974c71fe1989ee4aee7"},{"title":"A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition","url":"https://staff.fnwi.uva.nl/m.derijke/wp-content/papercite-data/pdf/wang-2025-cooperative.pdf"},{"title":"dblp: A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition.","url":"https://dblp.uni-trier.de/rec/journals/corr/abs-2502-18702.html"}]

I found the paper you were looking for! Here are the key details:

**Paper Title:** A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition

**Authors:** Zihan Wang, Ziqi Zhao, Yougang Lyu, Zhumin Chen, Maarten de Rijke, and Zhaochun Ren

**Conference:** Proceedings of the ACM Web Conference 2025 (WWW '25), April 28-May 2, 2025, Sydney, NSW, Australia

**Pages:** 4183-4195

**DOI:** 10.1145/3696410.3714923

**Overview:** The framewor
…[truncated 530 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-26T10:24:00.495477+00:00_

Web search results for query: "Zhou Wenxuan "UniversalNER Targeted Distillation Large Language Models Open Named Entity Recognition" ICLR 2024"

Links: [{"title":"[2308.03279] UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition","url":"https://arxiv.org/abs/2308.03279"},{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/universalner-targeted-distillation-from-large-language-models-for-open-named-entity-recognition/"},{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition | OpenReview","url":"https://openreview.net/forum?id=r65xfUb76p"},{"title":"UniversalNER: targeted distillation from large language models for open named entity recognition","url":"https://arxiv.org/html/2308.03279v2"},{"title":"UniversalNER: TARGETED DISTILLATION FROM","url":"https://openreview.net/pdf?id=r65xfUb76p"},{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230803279Z/abstract"},{"title":"UniversalNER","url":"https://universal-ner.github.io/"},{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition | Request PDF","url":"https://www.researchgate.net/publication/372961966_UniversalNER_Targeted_Distillation_from_Large_Language_Models_for_Open_Named_Entity_Recognition"},{"title":"[2308.03279v2] UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition","url":"https://arxiv.org/abs/2308.03279v2"},{"title":"UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition [Quick Review]","url":"https://liner.com/review/universalner-targeted-distillation-from-large-language-models-for-open-named"}]

I found the paper you're looking fo
…[truncated 1531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-26T10:24:00.495748+00:00_

Web search results for query: "Zaratiana "GLiNER2 Schema-Driven Multi-Task Learning Structured Information Extraction" EMNLP 2025 system demonstrations"

Links: [{"title":"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-demos.10/"},{"title":"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/2025.emnlp-demos.10@ACL"},{"title":"GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface","url":"https://arxiv.org/html/2507.18546v1"},{"title":"GLiNER2: Schema-Driven Multi-Task Learning for Structured Information Extraction","url":"https://www.researchgate.net/publication/397420183_GLiNER2_Schema-Driven_Multi-Task_Learning_for_Structured_Information_Extraction"},{"title":"Accepted System Demonstrations Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/demo_papers/"},{"title":"[PDF] GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GLiNER2:-An-Efficient-Multi-Task-Information-System-Zaratiana-Pasternak/73459ec452412f2653b341d55632190aeadc1e12"},{"title":"GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface [Quick Review]","url":"https://liner.com/review/gliner2-efficient-multitask-information-extraction-system-with-schemadriven-interface"},{"title":"[2507.18546] GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface","url":"https://arxiv.org/abs/2507.18546"},{"title":"GLiNER2: An Efficient Multi-Task Information Extraction System with Schema-Driven Interface - Paper Detail","url":"https://deeplearn.org/arxiv/623171/gliner2:-an-efficient-multi-task-information-extraction-system-with-schema-driven-interface"},{"title":"Paper page - GLiNER2: An Efficient Mult
…[truncated 1179 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-26T10:24:00.496044+00:00_

Web search results for query: "Sainz "GoLLIE Annotation Guidelines improve Zero-Shot Information-Extraction" ICLR 2024"

Links: [{"title":"[2310.03668] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/abs/2310.03668"},{"title":"ICLR Poster GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://iclr.cc/virtual/2024/poster/18435"},{"title":"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | OpenReview","url":"https://openreview.net/forum?id=Y3wpuxd7u9"},{"title":"GOLLIE: ANNOTATION GUIDELINES IMPROVE ZERO-SHOT INFORMATION-EXTRACTION | Documents - Universidad del País Vasco / Euskal Herriko Unibertsitatea","url":"https://ekoizpen-zientifikoa.ehu.eus/documentos/66cb8eeac7cd8e0cebf21fbb"},{"title":"GOLLIE : ANNOTATION GUIDELINES IMPROVE ZERO- ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf"},{"title":"GoLLIE : Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/html/2310.03668v5"},{"title":"[PDF] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GoLLIE:-Annotation-Guidelines-improve-Zero-Shot-Sainz-Garc%C3%ADa-Ferrero/3f40edfcafc018b2cb54612a9aaa9d6b43a11a26"}]

I found the paper you're looking for! Here's what I found:

GoLLIE (Guideline-following Large Language Model for IE) is a model designed to improve zero-shot results on unseen IE tasks by being fine-tuned to comply with annotation guidelines. LLMs have been less successful in Information Extraction (IE), lagging behind task-specific models. The paper demonstrates that GoLLIE is able to generalize to and follow unseen guidelines, outperforming previous attempts at zero-shot information extraction.

The paper was presented at ICLR 2024 and is authored by Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Laca
…[truncated 378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-26T10:24:00.496316+00:00_

Web search results for query: "Liu Nelson "Lost in the Middle How Language Models Use Long Contexts" TACL 2024"

Links: [{"title":"Lost in the Middle: How Language Models Use Long Contexts - ACL Anthology","url":"https://aclanthology.org/2024.tacl-1.9/"},{"title":"Lost in the Middle: How Language Models Use Long Contexts | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/Lost-in-the-Middle-How-Language-Models-Use-Long"},{"title":"[2307.03172] Lost in the Middle: How Language Models Use Long Contexts","url":"https://arxiv.org/abs/2307.03172"},{"title":"(PDF) Lost in the Middle: How Language Models Use Long Contexts","url":"https://www.researchgate.net/publication/378284067_Lost_in_the_Middle_How_Language_Models_Use_Long_Contexts"},{"title":"Lost in the Middle: How Language Models Use Long Contexts Nelson F. Liu1∗","url":"https://aclanthology.org/2024.tacl-1.9.pdf"},{"title":"Lost in the Middle: How Language Models Use Long Contexts - researchr publication","url":"https://researchr.org/publication/LiuLHPBPL24"},{"title":"Lost in the Middle: How Language Models Use Long Contexts | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/article/view/5757"},{"title":"Stanford","url":"https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.tacl2023.bib"},{"title":"Nelson Liu - Stanford Computer Science","url":"https://cs.stanford.edu/~nfliu/"}]

I found the paper! Here are the details:

"Lost in the Middle: How Language Models Use Long Contexts" was published in TACL 2024 by Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang.

**Key Findings:**

The paper analyzes the performance of language models on two tasks that require identifying relevant information in their input contexts: multi-document question answering and key-value retrieval.

The main finding is that pe
…[truncated 626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-26T10:24:00.496590+00:00_

Web search results for query: "Gui Honghao "IEPile Unearthing Large Scale Schema-Conditioned Information Extraction Corpus" ACL 2024 short papers"

Links: [{"title":"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus - ACL Anthology","url":"https://aclanthology.org/2024.acl-short.13/"},{"title":"GitHub - zjunlp/IEPile: [ACL 2024] IEPile: A Large-Scale Information Extraction Corpus · GitHub","url":"https://github.com/zjunlp/IEPile"},{"title":"[2402.14710] IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus","url":"https://arxiv.org/abs/2402.14710"},{"title":"IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus | Request PDF","url":"https://www.researchgate.net/publication/384216193_IEPile_Unearthing_Large_Scale_Schema-Conditioned_Information_Extraction_Corpus"},{"title":"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus","url":"https://arxiv.org/html/2402.14710v3"},{"title":"IEPILE: Unearthing Large-Scale Schema-Based ...","url":"https://aclanthology.org/2024.acl-short.13.pdf"},{"title":"IEPile: Unearthing Large-Scale Schema-Based Information Extraction Corpus | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/iepile-unearthing-large-scale-schema-based-information"},{"title":"InstructIE: A Bilingual Instruction-based Information Extraction Dataset | The Semantic Web – ISWC 2024","url":"https://dl.acm.org/doi/10.1007/978-3-031-77847-6_4"}]

I found comprehensive information about this paper. Here are the search results:

The paper "IEPile: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus" was authored by Honghao Gui, Lin Yuan, Hongbin Ye, Ningyu Zhang, Mengshu Sun, Lei Liang, and Huajun Chen, and was published in the Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers) in Bangkok, Thailand, pages 127–146.

The paper introduces IEPile, a comprehensive bilingual (En
…[truncated 704 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-26T10:24:00.496897+00:00_

Web search results for query: "Zaratiana "GLiNER Generalist Model Named Entity Recognition Bidirectional Transformer" NAACL 2024"

Links: [{"title":"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.300/"},{"title":"GitHub - urchade/GLiNER: Generalist and Lightweight Model for Named Entity Recognition (Extract any entity types from texts) · GitHub","url":"https://github.com/urchade/GLiNER"},{"title":"GitHub - urchade/GLiNER: Generalist and Lightweight Model for Named Entity Recognition (Extract any entity types from texts) @ NAACL 2024","url":"https://github.com/urchade/GLiNER/tree/main"},{"title":"GitHub - locchh/GLiNER: Generalist and Lightweight Model for Named Entity Recognition (Extract any entity types from texts) @ NAACL 2024","url":"https://github.com/locchh/GLiNER"},{"title":"(PDF) GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer","url":"https://www.researchgate.net/publication/382634629_GLiNER_Generalist_Model_for_Named_Entity_Recognition_using_Bidirectional_Transformer"},{"title":"GitHub - PraxySante/GLiNER-official-repo: Generalist and Lightweight Model for Named Entity Recognition (Extract any entity types from texts) @ NAACL 2024","url":"https://github.com/PraxySante/GLiNER-official-repo"},{"title":"GitHub - sabdoudaoura/GLiNER_masking: Generalist and Lightweight Model for Named Entity Recognition (Extract any entity types from texts) @ NAACL 2024 · GitHub","url":"https://github.com/sabdoudaoura/GLiNER_masking"},{"title":"GLiNER/pyproject.toml at main · urchade/GLiNER","url":"https://github.com/urchade/GLiNER/blob/main/pyproject.toml"},{"title":"LipnLab: \"🎉 The paper \"GLiNER: Generalist Model for Named E…\" - lipn.info","url":"https://lipn.info/@LipnLab/112121562906555472"}]

I found the search results for your query. Here's what I found:

The paper "GLiNER: Generalist Model for Named Entity Recognition using Bidir
…[truncated 888 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-26T10:24:00.497206+00:00_

Web search results for query: "Dror Baumer Shlomov Reichart "Hitchhiker's Guide Testing Statistical Significance NLP" ACL 2018"

Links: [{"title":"The Hitchhiker’s Guide to Testing Statistical Significance in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/P18-1128/"},{"title":"ACL 2018: The Hitchhiker’s Guide to Testing Statistical Significance in Natural Language Processing","url":"https://acl2018.org/paper/703/"},{"title":"The Hitchhiker's Guide to Testing Statistical Significance in ...","url":"https://roireichart.com/wp-content/uploads/2023/03/acl-2018-sig-cr.pdf"},{"title":"GitHub - rtmdrr/testSignificanceNLP · GitHub","url":"https://github.com/rtmdrr/testSignificanceNLP"},{"title":"Recommended Statistical Significance Tests for NLP Tasks","url":"https://arxiv.org/pdf/1809.01448"},{"title":"[PDF] The Hitchhiker’s Guide to Testing Statistical Significance in Natural Language Processing | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Hitchhiker%E2%80%99s-Guide-to-Testing-Statistical-in-Dror-Baumer/d10df96b3fb0ab5c6b1d0cc22c7400d0acccc3cc"},{"title":"(PDF) The Hitchhiker’s Guide to Testing Statistical Significance in Natural Language Processing","url":"https://www.researchgate.net/publication/327034173_The_Hitchhiker's_Guide_to_Testing_Statistical_Significance_in_Natural_Language_Processing"},{"title":"The Hitchhiker’s Guide to Testing Statistical Significance in Natural Language Processing | BibSonomy","url":"https://www.bibsonomy.org/bibtex/24d35b165e7566906bf48fa548bedf68c/schwemmlein"},{"title":"[Quick Review] The Hitchhiker’s Guide to Testing Statistical Significance in Natural Language Processing","url":"https://liner.com/review/hitchhikers-guide-to-testing-statistical-significance-in-natural-language-processing"}]

I found the paper! Here are the details about your search query:

**Paper:** "The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing"

**Authors:** Rotem Dror, 
…[truncated 1053 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-26T10:24:00.497508+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Shachar Katz Goldberg \"NER Retriever Zero-Shot Named Entity Retrieval Type-Aware Embeddings\" EMNLP 2025 Findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Shachar Katz Goldberg \"NER Retriever Zero-Shot Named Entity Retrieval Type-Aware Embeddings\" EMNLP 2025 Findings"
  }
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-26T10:24:00.497700+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xu Derong \"Large Language Models for Generative Information Extraction Survey\" Frontiers Computer Science 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xu Derong \"Large Language Models for Generative Information Extraction Survey\" Frontiers Computer Science 2024"
  }
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-26T10:24:00.497924+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li Zixuan \"KnowCoder Coding Structured Knowledge LLMs Universal Information Extraction\" ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li Zixuan \"KnowCoder Coding Structured Knowledge LLMs Universal Information Extraction\" ACL 2024"
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-26T10:24:00.498086+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Shen Zhengyuan \"SLOT Structuring Output Large Language Models\" EMNLP 2025 industry track"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Shen Zhengyuan \"SLOT Structuring Output Large Language Models\" EMNLP 2025 industry track"
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-26T10:24:00.498211+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Cai Xingyu \"Isotropy Contextual Embedding Space Clusters Manifolds\" ICLR 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Cai Xingyu \"Isotropy Contextual Embedding Space Clusters Manifolds\" ICLR 2021"
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-26T10:24:00.498330+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang Xiao \"InstructUIE Multi-task Instruction Tuning Unified Information Extraction\" arXiv 2304.08085"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang Xiao \"InstructUIE Multi-task Instruction Tuning Unified Information Extraction\" arXiv 2304.08085"
  }
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-26T10:24:00.498449+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li Peng \"CodeIE Large Code Generation Models Better Few-Shot Information Extractors\" ACL 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li Peng \"CodeIE Large Code Generation Models Better Few-Shot Information Extractors\" ACL 2023"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-26T10:24:00.498600+00:00_

Web search results for query: "Xu Derong "Large Language Models for Generative Information Extraction Survey" Frontiers Computer Science 2024"

Links: [{"title":"[2312.17617] Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/abs/2312.17617"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science: Selected Publications from Chinese Universities","url":"https://dl.acm.org/doi/10.1007/s11704-024-40555-y"},{"title":"Large language models for generative information extraction: a survey - CityUHK Scholars","url":"https://scholars.cityu.edu.hk/en/publications/large-language-models-for-generative-information-extraction-a-sur/"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Large language models for generative information extraction: a survey","url":"https://d-nb.info/1354655508/34"},{"title":"Large language models for generative information extraction: a survey","url":"https://journal.hep.com.cn/fcs/EN/10.1007/s11704-024-40555-y"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"[2312.17617v3] Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/abs/2312.17617v3"}]

I found the paper you're looking for. The survey "Large language models for generative information extraction: a survey" was published in Frontiers of Computer Science in 2024, volume 18, issue 6, article 186357.

The paper was authored by Derong Xu, Wei Chen, Wenjun Peng, Chao Zhang, Tong Xu, Xiangyu Zhao, Xi
…[truncated 608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-26T10:24:00.498754+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qi Yunjia \"ADELIE Aligning Large Language Models Information Extraction\" EMNLP 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qi Yunjia \"ADELIE Aligning Large Language Models Information Extraction\" EMNLP 2024"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-26T10:24:00.498954+00:00_

Web search results for query: "Shen Zhengyuan "SLOT Structuring Output Large Language Models" EMNLP 2025 industry track"

Links: [{"title":"SLOT: Structuring the Output of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-industry.32/"},{"title":"SLOT: Structuring the Output of Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/397423713_SLOT_Structuring_the_Output_of_Large_Language_Models"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"[2505.04016] SLOT: Structuring the Output of Large Language Models","url":"https://arxiv.org/abs/2505.04016"},{"title":"Accepted Industry Track Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/ind_papers/"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://arxiv.org/html/2505.04016v1"},{"title":"[2505.04016v1] SLOT: Structuring the Output of Large Language Models","url":"https://arxiv.org/abs/2505.04016v1"},{"title":"EMNLP 2025 The 2025 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2025.emnlp-industry.0.pdf"},{"title":"dblp: EMNLP 2025 - Industry Track","url":"https://dblp.org/db/conf/emnlp/emnlp2025i.html"},{"title":"Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track - ACL Anthology","url":"https://aclanthology.org/volumes/2025.emnlp-industry/"}]

Based on my search results, I found comprehensive information about the paper you were looking for:

## SLOT: Structuring the Output of Large Language Models

The paper by Shen et al. was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track, pages 472–491, in Suzhou, China.

**Authors:** Zhengyuan Shen, Darren Yow-Bang Wang, Soumya Smruti Mishra, Zhichao Xu, Yifei Teng, and Haibo Ding

**Overview:** Structured outputs are essential for large language 
…[truncated 870 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-26T10:24:00.499155+00:00_

Web search results for query: "Wang Xiao "InstructUIE Multi-task Instruction Tuning Unified Information Extraction" arXiv 2304.08085"

Links: [{"title":"[2304.08085] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://arxiv.org/abs/2304.08085"},{"title":"InstructUIE: Multi-task Instruction Tuning for Uniﬁed Information Extraction","url":"https://arxiv.org/pdf/2304.08085"},{"title":"[2304.08085v1] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://arxiv.org/abs/2304.08085v1"},{"title":"[PDF] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/InstructUIE:-Multi-task-Instruction-Tuning-for-Wang-Zhou/bbb2fc6e95d24fb58ab6c25b216b14ac49a32fbe"},{"title":"Paper page - InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://huggingface.co/papers/2304.08085"},{"title":"(PDF) InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (2023) | Xiao Wang | 81 Citations","url":"https://scispace.com/papers/instructuie-multi-task-instruction-tuning-for-unified-qe70ci1r"},{"title":"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://www.researchgate.net/publication/370071546_InstructUIE_Multi-task_Instruction_Tuning_for_Unified_Information_Extraction"},{"title":"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction - nikkie-memos","url":"https://scrapbox.io/nikkie-memos/InstructUIE:_Multi-task_Instruction_Tuning_for_Unified_Information_Extraction"},{"title":"Instruction Matters: A Simple yet Effective Task Selection for Optimized Instruction Tuning of Specific Tasks","url":"https://arxiv.org/html/2404.16418v2"}]

I found the paper you're looking for! Here's what I found:

**InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction** (arXiv 2304.08085) is authored by X
…[truncated 1138 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-26T10:24:00.499716+00:00_

Web search results for query: "Cai Xingyu "Isotropy Contextual Embedding Space Clusters Manifolds" ICLR 2021"

Links: [{"title":"ISOTROPY IN THE CONTEXTUAL EMBEDDING SPACE","url":"https://openreview.net/pdf/8b00c8e698e9a810bfcee44a4ae5f6c3adeb7266.pdf"},{"title":"ICLR Poster Isotropy in the Contextual Embedding Space: Clusters and Manifolds","url":"https://iclr.cc/virtual/2021/poster/3079"},{"title":"Isotropy in the Contextual Embedding Space: Clusters and Manifolds | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Isotropy-in-the-Contextual-Embedding-Space:-and-Cai-Huang/2a8bb26654c015f663670d1e0745f870071d5507"},{"title":"dblp: Isotropy in the Contextual Embedding Space: Clusters and Manifolds.","url":"https://dblp.org/rec/conf/iclr/CaiHB021.html"},{"title":"Xingyu Cai, Jiaji Huang, Yuchen Bian, Kenneth Church · Isotropy in the Contextual Embedding Space: Clusters and Manifolds","url":"https://slideslive.com/38953489/isotropy-in-the-contextual-embedding-space-clusters-and-manifolds"},{"title":"Isotropy in the Contextual Embedding Space: Clusters and Manifolds | OpenReview","url":"https://openreview.net/forum?id=xYGNO86OWDH"},{"title":"Isotropy in the Contextual Embedding Space: Clusters and Manifolds","url":"https://papertalk.org/papertalks/28964"},{"title":"GitHub - TideDancer/iclr21_isotropy_contxt","url":"https://github.com/TideDancer/iclr21_isotropy_contxt"},{"title":"A Cluster-based Approach for Improving Isotropy in Contextual Embedding Space","url":"https://arxiv.org/pdf/2106.01183"},{"title":"When can isotropy help adapt LLMs’ next word prediction to numerical domains?","url":"https://arxiv.org/html/2505.17135v1"}]

I found the paper you were looking for! Here are the search results:

## Paper Information

The paper "Isotropy in the Contextual Embedding Space: Clusters and Manifolds" was authored by Xingyu Cai, Jiaji Huang, Yu-Lan Bian, and Kenneth Ward Church and published at ICLR in 2021.

## Overview

The paper investigates the geometric 
…[truncated 893 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-26T10:24:00.499970+00:00_

Web search results for query: "Qi Yunjia "ADELIE Aligning Large Language Models Information Extraction" EMNLP 2024"

Links: [{"title":"ADELIE: Aligning Large Language Models on Information Extraction - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.419/"},{"title":"GitHub - THU-KEG/ADELIE: [EMNLP2024] Aligning Large Language Models on Information Extraction · GitHub","url":"https://github.com/THU-KEG/ADELIE"},{"title":"[2405.05008] ADELIE: Aligning Large Language Models on Information Extraction","url":"https://arxiv.org/abs/2405.05008"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction | Request PDF","url":"https://www.researchgate.net/publication/386188440_ADELIE_Aligning_Large_Language_Models_on_Information_Extraction"},{"title":"[Quick Review] ADELIE: Aligning Large Language Models on Information Extraction","url":"https://liner.com/review/adelie-aligning-large-language-models-on-information-extraction"},{"title":"ADELIE: Aligning Large Language Models on Information Extraction | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/adelie-aligning-large-language-models-information-extraction"},{"title":"dblp: ADELIE: Aligning Large Language Models on Information Extraction.","url":"https://dblp.org/rec/journals/corr/abs-2405-05008.html"},{"title":"Paper page - ADELIE: Aligning Large Language Models on Information Extraction","url":"https://huggingface.co/papers/2405.05008"},{"title":"Publications - Xiaozhi Wang 王晓智","url":"https://bakser.github.io/publications/"},{"title":"Main Conference - EMNLP 2024","url":"https://2024.emnlp.org/program/accepted_main_conference/"}]

I found the paper you're looking for! Here are the key details:

ADELIE: Aligning Large Language Models on Information Extraction was authored by Yunjia Qi, Hao Peng, Xiaozhi Wang, Bin Xu, Lei Hou, and Juanzi Li and published at EMNLP 2024.

**Overview:**
Large language models usually fall short on information extraction tasks and struggl
…[truncated 927 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-26T10:24:00.500167+00:00_

Web search results for query: "Li Peng "CodeIE Large Code Generation Models Better Few-Shot Information Extractors" ACL 2023"

Links: [{"title":"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors - ACL Anthology","url":"https://aclanthology.org/2023.acl-long.855/"},{"title":"[2305.05711] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://arxiv.org/abs/2305.05711"},{"title":"GitHub - artpli/CodeIE: [ACL 23] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors · GitHub","url":"https://github.com/artpli/CodeIE"},{"title":"[2305.05711v2] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://arxiv.org/abs/2305.05711v2"},{"title":"CodeIE","url":"https://artpli.github.io/CodeIE/"},{"title":"PENG LI","url":"https://artpli.github.io/"},{"title":"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://paperreading.club/page?id=164011"},{"title":"dblp: CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors.","url":"https://dblp.uni-trier.de/rec/journals/corr/abs-2305-05711.html"}]

I found the paper you're looking for! Here are the key details:

CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors was authored by Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuanbin Wu, Xuanjing Huang, and Xipeng Qiu, and published at ACL 2023. It appears in the Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) on pages 15339–15353, held in Toronto, Canada.

The core contribution of the paper is that the authors propose to recast structured output in the form of code instead of natural language and utilize generative LLMs of code (Code-LLMs) such as Codex to perform IE tasks, in particular, named entity recognition and relation extraction.

The paper addresses a key challenge: it is nontrivial to perfo
…[truncated 488 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-26T10:24:00.500361+00:00_

Web search results for query: "Li Zixuan "KnowCoder Coding Structured Knowledge LLMs Universal Information Extraction" ACL 2024"

Links: [{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.475/"},{"title":"[2403.07969] KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction","url":"https://arxiv.org/abs/2403.07969"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction - Zixuan Li","url":"https://lee-zix.github.io/publications/2024-08-16-ACL/"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction","url":"https://arxiv.org/html/2403.07969v2"},{"title":"GitHub - ICT-GoKnow/KnowCoder: Official Repo of paper \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\". In the paper, we propose KnowCoder, the most powerful large language model so far for universal information extraction.","url":"https://github.com/ICT-GoKnow/KnowCoder"},{"title":"KnowCoder","url":"https://ict-goknow.github.io/knowcoder/"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction | Request PDF","url":"https://www.researchgate.net/publication/384207388_KnowCoder_Coding_Structured_Knowledge_into_LLMs_for_Universal_Information_Extraction"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2b5538e89bfb4cac76acafc1f9f2c9f64/dblp"},{"title":"[PDF] KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/KnowCoder:-Coding-Structured-Knowledge-into-LLMs-Li-Zeng/3ba0f13d9b24a2dcfdcd861150e33c7d71e6c69e"}]

I found the paper! Here are the key details about this ACL 2024 publication:

## Paper Information

KnowCoder: Coding 
…[truncated 1481 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-26T10:24:00.500671+00:00_

Web search results for query: "Shachar Katz Goldberg "NER Retriever Zero-Shot Named Entity Retrieval Type-Aware Embeddings" EMNLP 2025 Findings"

Links: [{"title":"NER Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.597/"},{"title":"[2509.04011] NER Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings","url":"https://arxiv.org/abs/2509.04011"},{"title":"NER Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings","url":"https://arxiv.org/pdf/2509.04011"},{"title":"[2509.04011v1] NER Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings","url":"https://arxiv.org/abs/2509.04011v1"},{"title":"Paper page - NER Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings","url":"https://huggingface.co/papers/2509.04011"},{"title":"NER Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings | Request PDF","url":"https://www.researchgate.net/publication/397426570_NER_Retriever_Zero-Shot_Named_Entity_Retrieval_with_Type-Aware_Embeddings"},{"title":"Zero-Shot Named Entity Retrieval with Type-Aware ...","url":"https://aclanthology.org/2025.findings-emnlp.597.pdf"},{"title":"Or Shachar - ACL Anthology","url":"https://aclanthology.org/people/or-shachar/"},{"title":"[Quick Review] NER Retriever: Zero-Shot Named Entity Retrieval with Type-Aware\\n Embeddings","url":"https://liner.com/review/ner-retriever-zeroshot-named-entity-retrieval-with-typeaware-embeddings"},{"title":"NER Retriever: Unified NER and Information Retrieval","url":"https://www.emergentmind.com/topics/ner-retriever"}]

I found the research paper! Here are the details:

## Paper Information

The paper "NER Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings" by Or Shachar, Uri Katz, Yoav Goldberg, and Oren Glickman was published in the Findings of the Association for Computational Linguistics: EMNLP 2025, pages 11175–11186, Suzhou,
…[truncated 985 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-26T10:24:00.501171+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Luo Yujie \"OneKE Dockerized Schema-Guided LLM Agent Knowledge Extraction\" ACM Web Conference 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Luo Yujie \"OneKE Dockerized Schema-Guided LLM Agent Knowledge Extraction\" ACM Web Conference 2025"
  }
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-26T10:24:00.501335+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ding Ning \"Few-NERD Few-shot Named Entity Recognition Dataset\" ACL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ding Ning \"Few-NERD Few-shot Named Entity Recognition Dataset\" ACL 2021"
  }
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-26T10:24:00.501474+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Han Xu \"FewRel Large-Scale Supervised Few-Shot Relation Classification Dataset\" EMNLP 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Han Xu \"FewRel Large-Scale Supervised Few-Shot Relation Classification Dataset\" EMNLP 2018"
  }
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-26T10:24:00.501597+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang Xiaozhi \"MAVEN Massive General Domain Event Detection Dataset\" EMNLP 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang Xiaozhi \"MAVEN Massive General Domain Event Detection Dataset\" EMNLP 2020"
  }
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-26T10:24:00.501734+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Yao Yuan \"DocRED Large-Scale Document-Level Relation Extraction Dataset\" ACL 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Yao Yuan \"DocRED Large-Scale Document-Level Relation Extraction Dataset\" ACL 2019"
  }
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-26T10:24:00.501870+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3 technical report arXiv 2505.09388 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3 technical report arXiv 2505.09388 2025"
  }
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-26T10:24:00.502109+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Grattafiori \"Llama 3 Herd of Models\" arXiv 2407.21783 Meta 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Grattafiori \"Llama 3 Herd of Models\" arXiv 2407.21783 Meta 2024"
  }
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-26T10:24:00.502231+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Reimers Gurevych \"Sentence-BERT Sentence Embeddings Siamese BERT-Networks\" EMNLP 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Reimers Gurevych \"Sentence-BERT Sentence Embeddings Siamese BERT-Networks\" EMNLP 2019"
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-26T10:24:00.502380+00:00_

Web search results for query: "Luo Yujie "OneKE Dockerized Schema-Guided LLM Agent Knowledge Extraction" ACM Web Conference 2025"

Links: [{"title":"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System | Companion Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3701716.3715189"},{"title":"GitHub - zjunlp/OneKE: [WWW 2025] A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System. · GitHub","url":"https://github.com/zjunlp/OneKE"},{"title":"[2412.20005] OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System","url":"https://arxiv.org/abs/2412.20005"},{"title":"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System","url":"https://www.researchgate.net/publication/392062813_OneKE_A_Dockerized_Schema-Guided_LLM_Agent-based_Knowledge_Extraction_System"},{"title":"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System","url":"https://arxiv.org/html/2412.20005v2"},{"title":"[PDF] OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System | Semantic Scholar","url":"https://www.semanticscholar.org/paper/OneKE:-A-Dockerized-Schema-Guided-LLM-Agent-based-Luo-Ru/0b4206ee29e10f6e2156a66b0419f0e18fa13e63"},{"title":"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System | Companion Proceedings of the ACM on Web Conference 2025","url":"https://doi.org/10.1145/3701716.3715189"},{"title":"OneKE: A Dockerized Schema-Guided LLM Agent-based Knowledge Extraction System | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/oneke-dockerized-schema-guided-llm-agent-based"},{"title":"ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs","url":"https://arxiv.org/html/2509.04696v1"}]

I found the paper you're looking for. Here are the search results:

OneKE is a dockerized schema-guided knowledge extraction system that can extract knowledge from the Web and raw PDF Books, and su
…[truncated 872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-26T10:24:00.502583+00:00_

Web search results for query: "Han Xu "FewRel Large-Scale Supervised Few-Shot Relation Classification Dataset" EMNLP 2018"

Links: [{"title":"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation - ACL Anthology","url":"https://aclanthology.org/D18-1514/"},{"title":"FewRel: A Large-Scale Supervised Few-shot Relation Classification Dataset with State-of-the-Art Evaluation","url":"https://thunlp.github.io/1/fewrel1.html"},{"title":"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation | Request PDF","url":"https://www.researchgate.net/publication/334115814_FewRel_A_Large-Scale_Supervised_Few-Shot_Relation_Classification_Dataset_with_State-of-the-Art_Evaluation"},{"title":"[PDF] FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/FewRel:-A-Large-Scale-Supervised-Few-Shot-Relation-Han-Zhu/274b4ad4840b0a8a70c5bac3fe4b4861ce5fbb95"},{"title":"[1810.10147] FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation","url":"https://arxiv.org/abs/1810.10147"},{"title":"FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2018arXiv181010147H/abstract"},{"title":"[1810.10147] FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation","url":"https://ar5iv.labs.arxiv.org/html/1810.10147"},{"title":"[1810.10147v2] FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation","url":"https://arxiv.org/abs/1810.10147v2"}]

Based on the search results, I found information about the FewRel paper:

FewRel: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation was authored by Xu Ha
…[truncated 880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-26T10:24:00.503151+00:00_

Web search results for query: "Ding Ning "Few-NERD Few-shot Named Entity Recognition Dataset" ACL 2021"

Links: [{"title":"Few-NERD: A Few-shot Named Entity Recognition Dataset - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.248/"},{"title":"GitHub - thunlp/Few-NERD: Code and data of ACL 2021 paper \"Few-NERD: A Few-shot Named Entity Recognition Dataset\" · GitHub","url":"https://github.com/thunlp/Few-NERD"},{"title":"[2105.07464] Few-NERD: A Few-Shot Named Entity Recognition Dataset","url":"https://arxiv.org/abs/2105.07464"},{"title":"Few-NERD","url":"https://ningding97.github.io/fewnerd/"},{"title":"(PDF) Few-NERD: A Few-shot Named Entity Recognition Dataset","url":"https://www.academia.edu/78460366/Few_NERD_A_Few_shot_Named_Entity_Recognition_Dataset"},{"title":"Few-NERD: A Few-shot Named Entity Recognition Dataset | Request PDF","url":"https://www.researchgate.net/publication/353490454_Few-NERD_A_Few-shot_Named_Entity_Recognition_Dataset"},{"title":"Papers with Code - Few-NERD: A Few-Shot Named Entity Recognition Dataset","url":"https://paperswithcode.com/paper/few-nerd-a-few-shot-named-entity-recognition"},{"title":"Few-NERD: A Few-shot Named Entity Recognition Dataset | Performance Analytics","url":"https://www.scinapse.io/papers/3177312484"}]

Based on the search results, here's information about the Few-NERD paper:

Few-NERD: A Few-shot Named Entity Recognition Dataset was published by Ning Ding, Guangwei Xu, Yulin Chen, Xiaobin Wang, Xu Han, Pengjun Xie, Haitao Zheng, and Zhiyuan Liu at ACL-IJCNLP 2021. The paper appeared in the Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), pages 3198–3213.

Few-NERD is a large-scale human-annotated few-shot NER dataset with a hierarchy of 8 coarse-grained and 66 fine-grained entity types. The dataset consists of 188,238 sentences from Wikipedia, with 4,601,160 words in
…[truncated 437 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-26T10:24:00.503368+00:00_

Web search results for query: "Qwen3 technical report arXiv 2505.09388 2025"

Links: [{"title":"[2505.09388] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388"},{"title":"Paper page - Qwen3 Technical Report","url":"https://huggingface.co/papers/2505.09388"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"[2505.09388] Qwen3 Technical Report - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2505.09388"},{"title":"Qwen3 Technical Report | Request PDF","url":"https://www.researchgate.net/publication/391741196_Qwen3_Technical_Report"},{"title":"[2505.09388v1] Qwen3 Technical Report","url":"https://arxiv.org/abs/2505.09388v1"},{"title":"Qwen3 Technical Report (arXiv:2505.09388v1) - ScienceStack","url":"https://www.sciencestack.ai/paper/2505.09388v1"},{"title":"Qwen3 Technical Report","url":"https://summarizepaper.com/en/arxiv-id/2505.09388v1/"}]

Based on the search results, here's information about the Qwen3 Technical Report (arXiv:2505.09388):

## Overview

Qwen3 is the latest version of the Qwen model family, comprising a series of large language models (LLMs) designed to advance performance, efficiency, and multilingual capabilities. The paper was submitted on May 14, 2025.

## Model Architecture

The Qwen3 series includes models of both dense and Mixture-of-Expert (MoE) architectures, with parameter scales ranging from 0.6 to 235 billion.

## Key Innovations

A key innovation in Qwen3 is the integration of thinking mode (for complex, multi-step reasoning) and non-thinking mode (for rapid, context-driven responses) into a unified framework, eliminating the need to switch between different models and enabling dynamic mode switching based on user queries or chat templates.

Qwen3 introduces a thinking budget mechanism, allowing users to allocate computational resources adaptively during inference, thereby balancing latency and performance based on task complexity
…[truncated 484 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-26T10:24:00.503553+00:00_

Web search results for query: "Wang Xiaozhi "MAVEN Massive General Domain Event Detection Dataset" EMNLP 2020"

Links: [{"title":"MAVEN: A Massive General Domain Event Detection Dataset - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.129/"},{"title":"GitHub - THU-KEG/MAVEN-dataset: Source code and dataset for EMNLP 2020 paper \"MAVEN: A Massive General Domain Event Detection Dataset\". · GitHub","url":"https://github.com/THU-KEG/MAVEN-dataset"},{"title":"MAVEN: A Massive General Domain Event Detection Dataset - Xiaozhi Wang 王晓智","url":"https://bakser.github.io/publication/2020-11-17-MAVEN"},{"title":"MAVEN: A Massive General Domain Event Detection Dataset | Request PDF","url":"https://www.researchgate.net/publication/347236490_MAVEN_A_Massive_General_Domain_Event_Detection_Dataset"},{"title":"MAVEN","url":"https://thukeg.gitee.io/maven/"},{"title":"KG-NLP-Papers/EMNLP/2020/EE/8. MAVEN_A Massive General Domain Event Detection Dataset.md at main · Clearailhc/KG-NLP-Papers","url":"https://github.com/Clearailhc/KG-NLP-Papers/blob/main/EMNLP/2020/EE/8.%20MAVEN_A%20Massive%20General%20Domain%20Event%20Detection%20Dataset.md"},{"title":"[2004.13590] MAVEN: A Massive General Domain Event Detection Dataset","url":"https://arxiv.org/abs/2004.13590"},{"title":"[2004.13590v2] MAVEN: A Massive General Domain Event Detection Dataset","url":"https://arxiv.org/abs/2004.13590v2"}]

Based on the search results, I found information about the paper you're looking for:

MAVEN: A Massive General Domain Event Detection Dataset was published by Wang Xiaozhi and co-authors at EMNLP 2020. The authors include Xiaozhi Wang, Ziqi Wang, Xu Han, Wangyi Jiang, Rong Han, Zhiyuan Liu, Juanzi Li, Peng Li, Yankai Lin, and Jie Zhou.

The dataset contains 4,480 Wikipedia documents, 118,732 event mention instances, and 168 event types. The paper addresses issues with existing event detection datasets including data scarcity and low coverage, as existing small-scale datasets are not suffi
…[truncated 447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-26T10:24:00.503740+00:00_

Web search results for query: "Yao Yuan "DocRED Large-Scale Document-Level Relation Extraction Dataset" ACL 2019"

Links: [{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset - ACL Anthology","url":"https://aclanthology.org/P19-1074/"},{"title":"GitHub - thunlp/DocRED: Dataset and codes for ACL 2019 DocRED: A Large-Scale Document-Level Relation Extraction Dataset. · GitHub","url":"https://github.com/thunlp/DocRED"},{"title":"[1906.06127] DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://arxiv.org/abs/1906.06127"},{"title":"dblp: DocRED: A Large-Scale Document-Level Relation Extraction Dataset.","url":"https://dblp.org/rec/conf/acl/YaoYLHLLLHZS19.html"},{"title":"[PDF] DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DocRED:-A-Large-Scale-Document-Level-Relation-Yao-Ye/2745fc72e1dd53d1c30f17cf05841b163c2f63c9"},{"title":"[1906.06127v3] DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://arxiv.org/abs/1906.06127v3"},{"title":"(PDF) DocRED: A Large-Scale Document-Level Relation Extraction Dataset","url":"https://www.researchgate.net/publication/333815327_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"DocRED: A Large-Scale Document-Level Relation Extraction Dataset | Request PDF","url":"https://www.researchgate.net/publication/335780641_DocRED_A_Large-Scale_Document-Level_Relation_Extraction_Dataset"},{"title":"DocRED/README.md at master · thunlp/DocRED","url":"https://github.com/thunlp/DocRED/blob/master/README.md"},{"title":"thunlp/docred · Datasets at Hugging Face","url":"https://huggingface.co/datasets/thunlp/docred"}]

Based on the search results, here's the information about the DocRED dataset:

DocRED: A Large-Scale Document-Level Relation Extraction Dataset was authored by Yuan Yao, Deming Ye, Peng Li, Xu Han, Yankai Lin, Zhenghao Liu, Zhiyuan Liu, Lixin Huang, Jie Zhou, a
…[truncated 952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-26T10:24:00.503943+00:00_

Web search results for query: "Grattafiori "Llama 3 Herd of Models" arXiv 2407.21783 Meta 2024"

Links: [{"title":"[2407.21783] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783"},{"title":"The Llama 3 Herd of Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240721783G/abstract"},{"title":"(PDF) The Llama 3 Herd of Models","url":"https://www.researchgate.net/publication/382739128_The_Llama_3_Herd_of_Models"},{"title":"Paper page - The Llama 3 Herd of Models","url":"https://huggingface.co/papers/2407.21783"},{"title":"[2407.21783] The Llama 3 Herd of Models - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2407.21783"},{"title":"[2407.21783v3] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v3"},{"title":"The Llama 3 Herd of Models Llama Team, AI @ Meta1","url":"https://arxiv.org/pdf/2407.21783v3"},{"title":"The Llama 3 Herd of Models. Paper Review | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/the-llama-3-herd-of-models-2f62252ce1c8"},{"title":"[2407.21783v2] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v2"}]

I found the paper you're looking for. Here's what the search revealed:

"The Llama 3 Herd of Models" is a paper by Aaron Grattafiori and 558 other authors that presents a new set of foundation models called Llama 3, which is a herd of language models that natively support multilinguality, coding, reasoning, and tool usage.

Key details about the paper:

- **ArXiv ID**: 2407.21783, submitted on July 31, 2024, with the latest version (v3) revised on November 23, 2024
- **Model Size**: The largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens.
- **Performance**: Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks.
- **Release**: Llama 3 was publicly released, including pre-trained and post-trained versions of the 405B parameter language model and L
…[truncated 402 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-26T10:24:00.504143+00:00_

Web search results for query: "Reimers Gurevych "Sentence-BERT Sentence Embeddings Siamese BERT-Networks" EMNLP 2019"

Links: [{"title":"[PDF] Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Sentence-BERT:-Sentence-Embeddings-using-Siamese-Reimers-Gurevych/93d63ec754f29fa22572615320afe0521f7ec66d"},{"title":"[1908.10084] Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks","url":"https://arxiv.org/abs/1908.10084"},{"title":"Reimers, N. and Gurevych, I. (2019) Sentence-BERT Sentence Embeddings Using Siamese BERT-Networks. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Pro-cessing (EMNLP-IJCNLP), Hong Kong, November 2019, 3982-3992. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3422225"},{"title":"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks - ACL Anthology","url":"https://aclanthology.org/D19-1410/"},{"title":"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks | Request PDF","url":"https://www.researchgate.net/publication/336996965_Sentence-BERT_Sentence_Embeddings_using_Siamese_BERT-Networks"},{"title":"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks","url":"https://arxiv.org/pdf/1908.10084"},{"title":"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks (EMNLP 2019) | Joohong Lee","url":"https://roomylee.github.io/sentence-bert/"},{"title":"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks | BibSonomy","url":"https://www.bibsonomy.org/bibtex/292afb49328e6651f17dc1e1b8c304aae/nosebrain"},{"title":"(PDF) Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks (2019) | Nils Reimers | 11970 Citations","url":"https://scispace.com/papers/sentence-bert-sentence-embeddings-using-siamese-bert-5dz0n53mvi"}]

I found comprehensive information a
…[truncated 1417 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-26T10:24:00.504354+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang Wenhui \"MiniLM Deep Self-Attention Distillation Task-Agnostic Compression Pre-Trained Transformers\" NeurIPS 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang Wenhui \"MiniLM Deep Self-Attention Distillation Task-Agnostic Compression Pre-Trained Transformers\" NeurIPS 2020"
  }
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-26T10:24:00.504496+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhao Dong \"Reflect then Learn Active Prompting Information Extraction Introspective Confusion\" AAAI 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhao Dong \"Reflect then Learn Active Prompting Information Extraction Introspective Confusion\" AAAI 2026"
  }
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-26T10:24:00.504626+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sclar \"Quantifying Language Models Sensitivity Spurious Features Prompt Design\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sclar \"Quantifying Language Models Sensitivity Spurious Features Prompt Design\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 124 · 2026-05-26T10:24:00.504747+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kwon Woosuk \"Efficient Memory Management Large Language Model Serving PagedAttention\" SOSP 2023 vLLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kwon Woosuk \"Efficient Memory Management Large Language Model Serving PagedAttention\" SOSP 2023 vLLM"
  }
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-26T10:24:00.504898+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xie Tingyu \"Empirical Study Zero-Shot NER ChatGPT\" EMNLP 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xie Tingyu \"Empirical Study Zero-Shot NER ChatGPT\" EMNLP 2023"
  }
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-26T10:24:00.505206+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wadhwa Somin \"Revisiting Relation Extraction era Large Language Models\" ACL 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wadhwa Somin \"Revisiting Relation Extraction era Large Language Models\" ACL 2023"
  }
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-26T10:24:00.505333+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Chia \"RelationPrompt Leveraging Prompts Generate Synthetic Data Zero-Shot Relation Triplet Extraction\" ACL 2022 Findings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Chia \"RelationPrompt Leveraging Prompts Generate Synthetic Data Zero-Shot Relation Triplet Extraction\" ACL 2022 Findings"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-26T10:24:00.505541+00:00_

Web search results for query: "Sclar "Quantifying Language Models Sensitivity Spurious Features Prompt Design" ICLR 2024"

Links: [{"title":"[2310.11324] Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://arxiv.org/abs/2310.11324"},{"title":"[PDF] Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Quantifying-Language-Models'-Sensitivity-to-in-or:-Sclar-Choi/17a6116e5bbd8b87082cbb2e795885567300c483"},{"title":"ICLR Poster Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://iclr.cc/virtual/2024/poster/18650"},{"title":"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/6c0e99d736da621403018ca7b32b1a4d-Abstract-Conference.html"},{"title":"Quantifying Language Models’ Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting","url":"https://arxiv.org/html/2310.11324v2"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6c0e99d736da621403018ca7b32b1a4d-Paper-Conference.pdf"},{"title":"Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting | OpenReview","url":"https://openreview.net/forum?id=RIu5lyNXjT"},{"title":"dblp: Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting.","url":"https://dblp.org/rec/conf/iclr/Sclar0TS24.html"},{"title":"Quantifying Language Models' Sensitivity to S
…[truncated 1621 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-26T10:24:00.505728+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ashok Lipton \"PromptNER Prompting Named Entity Recognition\" arXiv 2305.15444"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ashok Lipton \"PromptNER Prompting Named Entity Recognition\" arXiv 2305.15444"
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-26T10:24:00.505978+00:00_

Web search results for query: "Wang Wenhui "MiniLM Deep Self-Attention Distillation Task-Agnostic Compression Pre-Trained Transformers" NeurIPS 2020"

Links: [{"title":"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers","url":"https://proceedings.neurips.cc/paper/2020/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html"},{"title":"MINILM: Deep Self-Attention Distillation for Task-Agnostic ...","url":"https://proceedings.neurips.cc/paper/2020/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf"},{"title":"Review for NeurIPS paper: MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers","url":"https://proceedings.neurips.cc/paper/2020/file/3f5ee243547dee91fbd053c1c4a845aa-Review.html"},{"title":"[PDF] MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MiniLM:-Deep-Self-Attention-Distillation-for-of-Wang-Wei/c6c734e16f66fbfcefac7625cc64599e83292c1e"},{"title":"[Quick Review] MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers","url":"https://liner.com/review/minilm-deep-selfattention-distillation-for-taskagnostic-compression-of-pretrained-transformers"},{"title":"NeurIPS 2020 : MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers","url":"https://nips.cc/virtual/2020/public/poster_3f5ee243547dee91fbd053c1c4a845aa.html"},{"title":"MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/minilm-deep-self-attention-distillation-for-task-agnostic-compression-of-pre-trained-transformers/"},{"title":"Wenhui Wang, Furu Wei, Li Dong, Hangbo Bao, Nan Yang, Ming Zhou · MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers","
…[truncated 1332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-26T10:24:00.506201+00:00_

Web search results for query: "Xie Tingyu "Empirical Study Zero-Shot NER ChatGPT" EMNLP 2023"

Links: [{"title":"Empirical Study of Zero-Shot NER with ChatGPT - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.493/"},{"title":"[2310.10035] Empirical Study of Zero-Shot NER with ChatGPT","url":"https://arxiv.org/abs/2310.10035"},{"title":"Empirical Study of Zero-Shot NER with ChatGPT | Request PDF","url":"https://www.researchgate.net/publication/376394022_Empirical_Study_of_Zero-Shot_NER_with_ChatGPT"},{"title":"Empirical Study of Zero-Shot NER with ChatGPT","url":"https://aclanthology.org/2023.emnlp-main.493.pdf"},{"title":"[PDF] Empirical Study of Zero-Shot NER with ChatGPT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Empirical-Study-of-Zero-Shot-NER-with-ChatGPT-Xie-Li/3c55aa582a2d682eb53e9237589234854e0b92d8"},{"title":"[Quick Review] Empirical Study of Zero-Shot NER with ChatGPT","url":"https://liner.com/review/empirical-study-zeroshot-ner-with-chatgpt"},{"title":"Main Conference - EMNLP 2023","url":"https://2023.emnlp.org/program/accepted_main_conference/"},{"title":"GitHub - Emma1066/Zero-Shot-NER-with-ChatGPT: This is the github repository for the paper at EMNLP 2023: Empirical Study of Zero-Shot NER with ChatGPT.","url":"https://github.com/emma1066/zero-shot-ner-with-chatgpt"}]

I found the paper you're looking for. "Empirical Study of Zero-Shot NER with ChatGPT" by Xie et al. was published at EMNLP 2023, with authors Tingyu Xie, Qi Li, Jian Zhang, Yan Zhang, Zuozhu Liu, and Hongwei Wang.

The work focuses on exploring LLM performance on zero-shot information extraction, with a focus on the ChatGPT and named entity recognition (NER) task. The authors adapt prevalent reasoning methods to NER and propose reasoning strategies tailored for NER, including a decomposed question-answering paradigm by breaking down the NER task into simpler subproblems by labels, as well as syntactic augmentation to stimulate the model's intermediate
…[truncated 393 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-26T10:24:00.506425+00:00_

Web search results for query: "Zhao Dong "Reflect then Learn Active Prompting Information Extraction Introspective Confusion" AAAI 2026"

Links: [{"title":"[2508.10036] Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion","url":"https://arxiv.org/abs/2508.10036"},{"title":"The 40th Annual AAAI Conference on Artificial Intelligence","url":"https://aaai.org/conference/aaai/aaai-26/"},{"title":"Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/index"},{"title":"AAAI 2026 | OpenReview","url":"https://openreview.net/group?id=AAAI.org%2F2026"},{"title":"Paper Digest: AAAI 2026 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2026/01/aaai-2026-papers-highlights/"},{"title":"Dongxiao Zhu - James and Patricia Anderson College of Engineering - Wayne State University","url":"https://engineering.wayne.edu/profile/ct4442"},{"title":"Proceedings of the Fortieth AAAI Conference on Artificial Intelligence Archives - AAAI","url":"https://aaai.org/proceeding/aaai-40-2026/"},{"title":"The Association for the Advancement of Artificial Intelligence","url":"https://aaai.org/"},{"title":"AAAI Conference Paper Awards and Recognition - AAAI","url":"https://aaai.org/about-aaai/aaai-awards/aaai-conference-paper-awards-and-recognition/"}]

I found the paper you're looking for! The paper "Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion" is authored by Dong Zhao, Yadong Wang, Xiang Chen, Chenxi Wang, Hongliang Dai, Chuanxing Geng, Shengzhong Zhang, Shaoyuan Li, and Sheng-Jun Huang.

The paper addresses how Large Language Models (LLMs) show remarkable potential for few-shot information extraction (IE), yet their performance is highly sensitive to the choice of in-context examples. Conventional selection strategies often overlook confusion from both semantic content and the generation of well-structured formats, so the authors
…[truncated 394 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-26T10:24:00.506613+00:00_

Web search results for query: "Chia "RelationPrompt Leveraging Prompts Generate Synthetic Data Zero-Shot Relation Triplet Extraction" ACL 2022 Findings"

Links: [{"title":"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction - ACL Anthology","url":"https://aclanthology.org/2022.findings-acl.5/"},{"title":"GitHub - declare-lab/RelationPrompt: This repository implements our ACL Findings 2022 research paper RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction. The goal of Zero-Shot Relation Triplet Extraction (ZeroRTE) is to extract relation triplets of the format (head entity, tail entity, relation), despite not having annotated data for the test relation labels.","url":"https://github.com/declare-lab/RelationPrompt"},{"title":"[2203.09101] RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction","url":"https://arxiv.org/abs/2203.09101"},{"title":"dblp: RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction.","url":"https://dblp.org/rec/conf/acl/ChiaBPS22.html"},{"title":"[2203.09101v1] RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction","url":"https://arxiv.org/abs/2203.09101v1"},{"title":"RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction | Request PDF","url":"https://www.researchgate.net/publication/359309678_RelationPrompt_Leveraging_Prompts_to_Generate_Synthetic_Data_for_Zero-Shot_Relation_Triplet_Extraction"},{"title":"ACL.2022 - Findings | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ACL.2022?group=Findings"},{"title":"[PDF] RelationPrompt: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RelationPrompt:-Leveraging-Prompts-to-Gener
…[truncated 1439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-26T10:24:00.506801+00:00_

Web search results for query: "Kwon Woosuk "Efficient Memory Management Large Language Model Serving PagedAttention" SOSP 2023 vLLM"

Links: [{"title":"[2309.06180] Efficient Memory Management for Large Language Model Serving with PagedAttention","url":"https://arxiv.org/abs/2309.06180"},{"title":"Efficient Memory Management for Large Language Model Serving with PagedAttention | Proceedings of the 29th Symposium on Operating Systems Principles","url":"https://dl.acm.org/doi/10.1145/3600006.3613165"},{"title":"[Paper Note] Efficient Memory Management for Large Language Model Serving with PagedAttention, Woosuk Kwon+, SOSP'23 · Issue #2474 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/2474"},{"title":"vLLM – UC Berkeley Sky Computing Lab","url":"https://sky.cs.berkeley.edu/project/vllm/"},{"title":"[PDF] Efficient Memory Management for Large Language Model Serving with PagedAttention | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Memory-Management-for-Large-Language-with-Kwon-Li/83b90f4a0ae4cc214eb3cc140ccfef9cd99fac05"},{"title":"Efficient Memory Management for Large Language Model Serving with PagedAttention | Request PDF","url":"https://www.researchgate.net/publication/374920067_Efficient_Memory_Management_for_Large_Language_Model_Serving_with_PagedAttention"},{"title":"Efficient Memory Management for Large Language Model ...","url":"https://minjiazhang.github.io/courses/sp24-resource/vLLM-pre.pdf"},{"title":"GitHub - vllm-project/vllm: A high-throughput and memory-efficient inference and serving engine for LLMs · GitHub","url":"https://github.com/vllm-project/vllm"},{"title":"Efficient Memory Management for Large Language Model Serving with PagedAttention","url":"https://saikatkumardey.com/ml-wiki/sources/pagedattention-vllm"}]

I've found comprehensive information about this paper. Here's what the search revealed:

## Paper Details

The paper "Efficient Memory Management for Large Language 
…[truncated 1514 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-26T10:24:00.507023+00:00_

Web search results for query: "Wadhwa Somin "Revisiting Relation Extraction era Large Language Models" ACL 2023"

Links: [{"title":"Revisiting Relation Extraction in the era of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2023.acl-long.868/"},{"title":"Revisiting Relation Extraction in the era of Large Language ...","url":"https://aclanthology.org/2023.acl-long.868.pdf"},{"title":"Revisiting Relation Extraction in the era of Large Language Models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10482322/"},{"title":"[2305.05003] Revisiting Relation Extraction in the era of Large Language Models","url":"https://arxiv.org/abs/2305.05003"},{"title":"Revisiting Relation Extraction in the era of Large Language Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10523775-revisiting-relation-extraction-era-large-language-models"},{"title":"Revisiting Relation Extraction in the era of Large Language Models - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/37674787/"},{"title":"dblp: Somin Wadhwa","url":"https://dblp.org/pid/265/5925.html"},{"title":"[Quick Review] Revisiting Relation Extraction in the era of Large Language Models","url":"https://liner.com/review/revisiting-relation-extraction-in-era-large-language-models"},{"title":"[PDF] Revisiting Relation Extraction in the era of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Revisiting-Relation-Extraction-in-the-era-of-Large-Wadhwa-Amir/97782a67971c4ff1a74bf07e82fe20b2c4bf86c4"},{"title":"Revisiting Relation Extraction in the era of Large Language Models Somin Wadhwa","url":"https://arxiv.org/pdf/2305.05003"}]

I found the paper you're looking for! Here are the key details:

"Revisiting Relation Extraction in the era of Large Language Models" is an ACL 2023 paper by Somin Wadhwa, Silvio Amir, and Byron Wallace. It was published in the Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 
…[truncated 646 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-26T10:24:00.507206+00:00_

Web search results for query: "Ashok Lipton "PromptNER Prompting Named Entity Recognition" arXiv 2305.15444"

Links: [{"title":"[2305.15444] PromptNER: Prompting For Named Entity Recognition","url":"https://arxiv.org/abs/2305.15444"},{"title":"[2305.15444v2] PromptNER: Prompting For Named Entity Recognition","url":"https://arxiv.org/abs/2305.15444v2"},{"title":"[2305.15444] PromptNER: Prompting For Named Entity Recognition","url":"http://export.arxiv.org/abs/2305.15444"},{"title":"[PDF] PromptNER: Prompting For Named Entity Recognition | Semantic Scholar","url":"https://www.semanticscholar.org/paper/PromptNER:-Prompting-For-Named-Entity-Recognition-Ashok-Lipton/9141480721653789597b6e537ee0eeab401f3e60"},{"title":"(PDF) PromptNER: Prompting For Named Entity Recognition","url":"https://www.researchgate.net/publication/371040584_PromptNER_Prompting_For_Named_Entity_Recognition"},{"title":"PromptNER: Prompting For Named Entity Recognition - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230515444A/abstract"},{"title":"PromptNER : Prompting For Named Entity Recognition Dhananjay Ashok","url":"https://arxiv.org/pdf/2305.15444"},{"title":"Evaluating Named Entity Recognition Using Few-Shot Prompting with Large Language Models","url":"https://arxiv.org/html/2408.15796v2"},{"title":"Improving Few-Shot Cross-Domain Named Entity Recognition by Instruction Tuning a Word-Embedding based Retrieval Augmented Large Language Model","url":"https://arxiv.org/html/2411.00451v1"}]

I found the paper you were searching for. Note that the authors are Dhananjay Ashok and Zachary C. Lipton (not Ashok Lipton as a single author).

PromptNER is a new state-of-the-art algorithm for few-shot and cross-domain NER (Named Entity Recognition). To adapt to any new NER task, PromptNER requires a set of entity definitions in addition to the standard few-shot examples.

Given a sentence, PromptNER prompts an LLM to produce a list of potential entities along with corresponding explanations justify
…[truncated 695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-26T10:24:00.507394+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Geng Saibo \"JSONSchemaBench Rigorous Benchmark Structured Outputs Language Models\" arXiv 2501.10868"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Geng Saibo \"JSONSchemaBench Rigorous Benchmark Structured Outputs Language Models\" arXiv 2501.10868"
  }
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-26T10:24:00.507528+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Rastogi Abhinav \"Towards Scalable Multi-Domain Conversational Agents Schema-Guided Dialogue Dataset\" AAAI 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Rastogi Abhinav \"Towards Scalable Multi-Domain Conversational Agents Schema-Guided Dialogue Dataset\" AAAI 2020"
  }
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-26T10:24:00.507652+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li Bo \"Evaluating ChatGPT Information Extraction Capabilities Assessment Performance Explainability\" arXiv 2304.11633"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li Bo \"Evaluating ChatGPT Information Extraction Capabilities Assessment Performance Explainability\" arXiv 2304.11633"
  }
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-26T10:24:00.507770+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lee Harrison \"SGD-X Benchmark Robust Generalization Schema-Guided Dialogue Systems\" AAAI 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lee Harrison \"SGD-X Benchmark Robust Generalization Schema-Guided Dialogue Systems\" AAAI 2022"
  }
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-26T10:24:00.507907+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Vandemoortele \"From Haystack to Needle Label Space Reduction Zero-shot Classification\" arXiv 2502.08436"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Vandemoortele \"From Haystack to Needle Label Space Reduction Zero-shot Classification\" arXiv 2502.08436"
  }
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-26T10:24:00.508044+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Deng Jia \"What Does Classifying More Than 10000 Image Categories Tell Us\" ECCV 2010"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Deng Jia \"What Does Classifying More Than 10000 Image Categories Tell Us\" ECCV 2010"
  }
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-26T10:24:00.508159+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Rothman Kenneth \"No Adjustments Are Needed for Multiple Comparisons\" Epidemiology 1990"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Rothman Kenneth \"No Adjustments Are Needed for Multiple Comparisons\" Epidemiology 1990"
  }
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-26T10:24:00.508270+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lakens Daniel \"Equivalence Tests Practical Primer t Tests Correlations Meta-Analyses\" 2017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lakens Daniel \"Equivalence Tests Practical Primer t Tests Correlations Meta-Analyses\" 2017"
  }
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-26T10:24:00.508418+00:00_

Web search results for query: "Li Bo "Evaluating ChatGPT Information Extraction Capabilities Assessment Performance Explainability" arXiv 2304.11633"

Links: [{"title":"[2304.11633] Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness","url":"https://arxiv.org/abs/2304.11633"},{"title":"[2304.11633v1] Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness","url":"https://arxiv.org/abs/2304.11633v1"},{"title":"dblp: Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness.","url":"https://dblp.org/rec/journals/corr/abs-2304-11633.html"},{"title":"(PDF) Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness","url":"https://www.researchgate.net/publication/370227431_Evaluating_ChatGPT's_Information_Extraction_Capabilities_An_Assessment_of_Performance_Explainability_Calibration_and_Faithfulness"},{"title":"[2304.11633] Evaluating ChatGPT’s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness","url":"https://ar5iv.labs.arxiv.org/html/2304.11633"},{"title":"[Paper Note] Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness, Bo Li+, arXiv'23 · Issue #534 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/534"},{"title":"[PDF] Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Evaluating-ChatGPT's-Information-Extraction-An-of-Li-Fang/88abef771472c3aa46c53d5d626a0d0c3b66e8cd"}]

I found the paper you're looking for! Here are the details:

**T
…[truncated 1122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-26T10:24:00.508602+00:00_

Web search results for query: "Lee Harrison "SGD-X Benchmark Robust Generalization Schema-Guided Dialogue Systems" AAAI 2022"

Links: [{"title":"[2110.06800] SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems","url":"https://arxiv.org/abs/2110.06800"},{"title":"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems - AAAI","url":"https://aaai.org/papers/10938-sgd-x-a-benchmark-for-robust-generalization-in-schema-guided-dialogue-systems/"},{"title":"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems | DeepAI","url":"https://deepai.org/publication/sgd-x-a-benchmark-for-robust-generalization-in-schema-guided-dialogue-systems"},{"title":"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems","url":"https://research.google/pubs/sgd-x-a-benchmark-for-robust-generalization-in-schema-guided-dialogue-systems/"},{"title":"GitHub - google-research-datasets/dstc8-schema-guided-dialogue: The Schema-Guided Dialogue Dataset · GitHub","url":"https://github.com/google-research-datasets/dstc8-schema-guided-dialogue"},{"title":"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems","url":"https://cdn.aaai.org/ojs/21341/21341-13-25354-1-2-20220628.pdf"},{"title":"(PDF) SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems","url":"https://www.researchgate.net/publication/355237275_SGD-X_A_Benchmark_for_Robust_Generalization_in_Schema-Guided_Dialogue_Systems"},{"title":"AAAI2022: SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems","url":"https://aaai-2022.virtualchair.net/poster_aaai11645"},{"title":"SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/21341"},{"title":"dstc8-schema-guided-dialogue/README.md at master · google-research-datasets/dstc8-schema-guided
…[truncated 1422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-26T10:24:00.508783+00:00_

Web search results for query: "Rothman Kenneth "No Adjustments Are Needed for Multiple Comparisons" Epidemiology 1990"

Links: [{"title":"No Adjustments Are Needed for Multiple Comparisons : Epidemiology","url":"https://journals.lww.com/epidem/abstract/1990/01000/no_adjustments_are_needed_for_multiple_comparisons.10.aspx"},{"title":"[PDF] No Adjustments Are Needed for Multiple Comparisons | Semantic Scholar","url":"https://www.semanticscholar.org/paper/No-Adjustments-Are-Needed-for-Multiple-Comparisons-Rothman/7cdae9ece0e94ad740189e7b328bbf6993b4c8d5"},{"title":"Empirical-Bayes adjustments for multiple comparisons are sometimes useful - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/1912039/"},{"title":"Rothman (1990) No adjustments are needed for multiple comparisons.pdf","url":"https://www.scribd.com/document/321113650/Rothman-1990-No-adjustments-are-needed-for-multiple-comparisons-pdf"},{"title":"Dealing with multiple testing: To adjust or not to adjust","url":"https://arxiv.org/pdf/2010.02205"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=No+adjustments+are+needed+for+multiple+comparisons&amp=&author=KJ+Rothman&amp=&publication_year=1990&amp=&journal=Epidemiology&amp=&pages=43-46&amp=&doi=10.1097/00001648-199001000-00010&amp=&pmid=2081237"},{"title":"Rothman, K.J. (1990) No adjustments are needed for multiple comparisons. Epidemiology, 1, 43-46. doi10.1097/00001648-199001000-00010 - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=768985"},{"title":"No adjustments are needed for multiple comparisons - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/2081237/?dopt=Abstract"},{"title":"K. J. Rothman, “No Adjustments Are Needed for Multiple Comparisons,” Epidemi-ology, Vol. 1, No. 1, 1990, pp. 43-46. doi10.1097/00001648-199001000-00010 - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=411541"}]

I found t
…[truncated 1378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-26T10:24:00.509017+00:00_

Web search results for query: "Vandemoortele "From Haystack to Needle Label Space Reduction Zero-shot Classification" arXiv 2502.08436"

Links: [{"title":"[2502.08436] From Haystack to Needle: Label Space Reduction for Zero-shot Classification","url":"https://arxiv.org/abs/2502.08436"},{"title":"From Haystack to Needle: Label Space Reduction for Zero-shot Classification","url":"https://arxiv.org/html/2502.08436v2"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=1500&show=50"},{"title":"Machine Learning Feb 2025","url":"https://arxiv.org/list/cs.LG/2025-02?skip=3175&show=50"},{"title":"Artificial Intelligence Feb 2025","url":"https://arxiv.org/list/cs.AI/2025-02?skip=1700&show=25"},{"title":"Computer Science Feb 2025","url":"https://arxiv.org/list/cs/2025-02?skip=4050&show=2000"},{"title":"[Literature Review] From Haystack to Needle: Label Space Reduction for Zero-shot Classification","url":"https://www.themoonlight.io/en/review/from-haystack-to-needle-label-space-reduction-for-zero-shot-classification"},{"title":"Computation and Language Feb 2025","url":"http://www.arxiv.org/list/cs.CL/2025-02?skip=475&show=1000"}]

I found the paper you're looking for! Here's what I found:

The paper "From Haystack to Needle: Label Space Reduction for Zero-shot Classification" (arXiv 2502.08436) is authored by Nathan Vandemoortele and 3 other authors.

**Overview:**

The paper presents Label Space Reduction (LSR), a novel method for improving zero-shot classification performance of Large Language Models (LLMs).

**Key Method:**

LSR iteratively refines the classification label space by systematically ranking and reducing candidate classes, enabling the model to concentrate on the most relevant options. By leveraging unlabeled data with the statistical learning capabilities of data-driven models, LSR dynamically optimizes the label space representation at test time.

**Results:**

The experiments across seven benchmarks demonstrate that LSR im
…[truncated 572 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-26T10:24:00.509204+00:00_

Web search results for query: "Lakens Daniel "Equivalence Tests Practical Primer t Tests Correlations Meta-Analyses" 2017"

Links: [{"title":"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/28736600/"},{"title":"Equivalence Tests - Daniël Lakens, 2017","url":"https://journals.sagepub.com/doi/10.1177/1948550617697177"},{"title":"(PDF) Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses","url":"https://www.researchgate.net/publication/316752481_Equivalence_Tests_A_Practical_Primer_for_t_Tests_Correlations_and_Meta-Analyses"},{"title":"CRAN: TOSTER citation info","url":"https://cran.r-project.org/web/packages/TOSTER/citation.html"},{"title":"Cornell Statistical Consulting Unit Equivalence Testing","url":"https://cscu.cornell.edu/wp-content/uploads/equiv.pdf"},{"title":"Equivalence Tests: A Practical Primer for t-Tests, Correlations, and Meta-Analyses","url":"https://www.researchgate.net/publication/326117391_Equivalence_Tests_A_Practical_Primer_for_t-Tests_Correlations_and_Meta-Analyses"},{"title":"Equivalence tests : a practical primer for t tests, correlations, and meta-analyses — Research portal Eindhoven University of Technology","url":"https://research.tue.nl/en/publications/equivalence-tests-a-practical-primer-for-t-tests-correlations-and"}]

I found the paper you're looking for. Daniël Lakens published "Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses" in 2017 in Social Psychological and Personality Science, volume 8, issue 4, pages 355-362.

The article discusses the two one-sided tests (TOST) procedure, in which upper and lower equivalence bounds are specified based on the smallest effect size of interest, and how this procedure can be used to statistically reject the presence of effects large enough to be considered worthwhile. The paper includes accompanying spreadsheet and R package resources to help psychologi
…[truncated 207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-26T10:24:00.509390+00:00_

Web search results for query: "Rastogi Abhinav "Towards Scalable Multi-Domain Conversational Agents Schema-Guided Dialogue Dataset" AAAI 2020"

Links: [{"title":"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/6394"},{"title":"[1909.05855] Towards Scalable Multi-domain Conversational Agents: The Schema-Guided Dialogue Dataset","url":"https://arxiv.org/abs/1909.05855"},{"title":"The Schema-Guided Dialogue Dataset","url":"https://cdn.aaai.org/ojs/6394/6394-13-9619-1-10-20200517.pdf"},{"title":"Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset - R Discovery","url":"https://discovery.researcher.life/article/towards-scalable-multi-domain-conversational-agents-the-schema-guided-dialogue-dataset/e78e7eb730643968891a0dd0268418c2"},{"title":"(PDF) Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset","url":"https://www.researchgate.net/publication/342540613_Towards_Scalable_Multi-Domain_Conversational_Agents_The_Schema-Guided_Dialogue_Dataset"},{"title":"GitHub - google-research-datasets/dstc8-schema-guided-dialogue: The Schema-Guided Dialogue Dataset · GitHub","url":"https://github.com/google-research-datasets/dstc8-schema-guided-dialogue"},{"title":"[PDF] Towards Scalable Multi-domain Conversational Agents: The Schema-Guided Dialogue Dataset | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Towards-Scalable-Multi-domain-Conversational-The-Rastogi-Zang/674b6321ae1d12c83f28ade1850a27256c20f0d4"},{"title":"The Thirty-Fourth AAAI Conference on Artiﬁcial Intelligence (AAAI-20)","url":"https://ojs.aaai.org/index.php/AAAI/article/download/6394/6250"}]

I found the paper you're looking for. Here's the information:

**Paper Details:**

Rastogi, A., Zang, X., Sunkara, S., Gupta, R., & Khaitan, P. (2020). Towards Scalable Multi-Domain Conv
…[truncated 894 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-26T10:24:00.509568+00:00_

Web search results for query: "Geng Saibo "JSONSchemaBench Rigorous Benchmark Structured Outputs Language Models" arXiv 2501.10868"

Links: [{"title":"[2501.10868] JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://arxiv.org/abs/2501.10868"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://arxiv.org/html/2501.10868v3"},{"title":"GitHub - guidance-ai/jsonschemabench · GitHub","url":"https://github.com/guidance-ai/jsonschemabench"},{"title":"epfl-dlab/JSONSchemaBench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/epfl-dlab/JSONSchemaBench"},{"title":"GitHub - epfl-dlab/jsonschemabench","url":"https://github.com/epfl-dlab/jsonschemabench"},{"title":"JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250110868G/abstract"},{"title":"Paper page - Generating Structured Outputs from Language Models: Benchmark and Studies","url":"https://huggingface.co/papers/2501.10868"},{"title":"[Papierüberprüfung] JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models","url":"https://www.themoonlight.io/de/review/jsonschemabench-a-rigorous-benchmark-of-structured-outputs-for-language-models"},{"title":"epfl-dlab/JSONSchemaBench · Add paper link and GitHub link, specify task category and license","url":"https://huggingface.co/datasets/epfl-dlab/JSONSchemaBench/discussions/2/files"}]

I found the paper you're looking for. Here's what I found:

JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models is authored by Saibo Geng and 8 other co-authors, submitted to arXiv on January 18, 2025 (with the latest version v3 as of February 27, 2025), with arXiv ID 2501.10868.

The paper introduces JSONSchemaBench, a benchmark for constrained decoding comprising 10K real-world JSON schemas that encompass a wide range of constraints with varying compl
…[truncated 645 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-26T10:24:00.509748+00:00_

Web search results for query: "Deng Jia "What Does Classifying More Than 10000 Image Categories Tell Us" ECCV 2010"

Links: [{"title":"What Does Classifying More Than 10,000 Image Categories Tell Us?","url":"http://vision.stanford.edu/documents/DengBergLiFei-Fei_ECCV2010.pdf"},{"title":"What does classifying more than 10,000 image categories tell us? - Princeton University","url":"https://collaborate.princeton.edu/en/publications/what-does-classifying-more-than-10000-image-categories-tell-us"},{"title":"What Does Classifying More Than 10,000 Image Categories Tell Us? | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-642-15555-0_6"},{"title":"What Does Classifying More Than 10, 000 Image Categories Tell Us? | Request PDF","url":"https://www.researchgate.net/publication/221305119_What_Does_Classifying_More_Than_10_000_Image_Categories_Tell_Us"},{"title":"[PDF] What Does Classifying More Than 10, 000 Image Categories Tell Us? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/What-Does-Classifying-More-Than-10,-000-Image-Tell-Deng-Berg/9800e3c3394c569be83379ee2ebe3424e09c2919"},{"title":"AMMAI(Week 15) – What does classifying more than 10,000 image categories tell us? | Mr.pojenlai","url":"https://pojenlai.wordpress.com/2015/06/09/ammaiweek-15-what-does-classifying-more-than-10000-image-categories-tell-us/"},{"title":"What Does Classifying More Than 10,000 Image Categories ...","url":"http://vision.stanford.edu/pdf/DengBergLiFei-Fei_ECCV2010.pdf"},{"title":"What Does Classifying More Than 10, 000 Image Categories Tell Us? - Google Search","url":"https://google.com/search?q=What+Does+Classifying+More+Than+10%2C+000+Image+Categories+Tell+Us%3F"},{"title":"The Nine Lives of ImageNet: A Sociotechnical Retrospective ...","url":"https://data.mlr.press/assets/pdf/v01-4.pdf"}]

I found the paper! Here's what the search results show:

"What Does Classifying More Than 10,000 Image Categories Tell Us?" is a paper by Deng, J., Berg, A.C.,
…[truncated 889 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-26T10:24:00.509959+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Guo Biyang \"Label Confusion Learning Enhance Text Classification Models\" AAAI 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Guo Biyang \"Label Confusion Learning Enhance Text Classification Models\" AAAI 2021"
  }
}
```

</details>

---

### Tool call

_source line 154 · 2026-05-26T10:24:00.510145+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wen Zhihao \"Effective Efficient Schema-aware Information Extraction On-Device Large Language Models\" arXiv 2505.14992 DLISC"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wen Zhihao \"Effective Efficient Schema-aware Information Extraction On-Device Large Language Models\" arXiv 2505.14992 DLISC"
  }
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-26T10:24:00.510341+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Liang Sheng \"Schema as Parameterized Tools Universal Information Extraction\" arXiv 2506.01276 SPT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Liang Sheng \"Schema as Parameterized Tools Universal Information Extraction\" arXiv 2506.01276 SPT"
  }
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-26T10:24:00.510529+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Card Dallas Henderson \"With Little Power Comes Great Responsibility\" EMNLP 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Card Dallas Henderson \"With Little Power Comes Great Responsibility\" EMNLP 2020"
  }
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-26T10:24:00.510741+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Chen Jingxuan \"Understanding LLM Performance Degradation Multi-Instance Processing Instance Count Context Length\" arXiv 2603.22608"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Chen Jingxuan \"Understanding LLM Performance Degradation Multi-Instance Processing Instance Count Context Length\" arXiv 2603.22608"
  }
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-26T10:24:00.510944+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Robinson William \"Ecological Correlations Behavior Individuals\" American Sociological Review 1950"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Robinson William \"Ecological Correlations Behavior Individuals\" American Sociological Review 1950"
  }
}
```

</details>

---

### Tool call

_source line 159 · 2026-05-26T10:24:00.511125+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Boylan Jack \"GLiREL Generalist Model Zero-Shot Relation Extraction\" NAACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Boylan Jack \"GLiREL Generalist Model Zero-Shot Relation Extraction\" NAACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 160 · 2026-05-26T10:24:00.511300+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Peterson Battleday Griffiths Russakovsky \"Human Uncertainty Makes Classification More Robust\" ICCV 2019 pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Peterson Battleday Griffiths Russakovsky \"Human Uncertainty Makes Classification More Robust\" ICCV 2019 pages"
  }
}
```

</details>

---

### Tool result

_source line 161 · 2026-05-26T10:24:00.511512+00:00_

Web search results for query: "Wen Zhihao "Effective Efficient Schema-aware Information Extraction On-Device Large Language Models" arXiv 2505.14992 DLISC"

Links: [{"title":"[2505.14992] Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models","url":"https://arxiv.org/abs/2505.14992"},{"title":"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models","url":"https://arxiv.org/html/2505.14992v1"},{"title":"[2505.14992v1] Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models","url":"https://arxiv.org/abs/2505.14992v1"},{"title":"Effective and Efficient Schema-aware Information ...","url":"https://www.arxiv.org/pdf/2505.14992"},{"title":"Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation","url":"https://arxiv.org/html/2505.08690"},{"title":"[2505.08690v1] Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2505.08690v1"}]

I found the paper you're looking for! Here's what I found:

The paper proposes a two-stage information extraction approach adapted for on-device LLMs, called Dual-LoRA with Incremental Schema Caching (DLISC), which enhances both schema identification and schema-aware extraction in terms of effectiveness and efficiency.

The paper is authored by Zhihao Wen, Sheng Liang, Yaxiong Wu, Yongyue Zhang, and Yong Liu from Huawei Noah's Ark Lab.

The work addresses challenges in deploying computationally intensive large language models (LLMs) on resource-constrained devices for information extraction, particularly issues like hallucinations, limited context length, and high latency—especially when handling diverse extraction schemas.

In particular, DLISC adopts an Identification LoRA module for retrieving the most relevant schemas to a given query, and an Extraction LoRA module for performing information extraction based on the previously selected schemas.


…[truncated 192 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-26T10:24:00.511779+00:00_

Web search results for query: "Robinson William "Ecological Correlations Behavior Individuals" American Sociological Review 1950"

Links: [{"title":"Robinson, W. S. (1950). Ecological Correlations and the Behavior of Individuals. American Sociological Review, 15, 351-357. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2253248"},{"title":"Ecological correlations and the behavior of individuals.","url":"https://psycnet.apa.org/record/1951-06782-001"},{"title":"(PDF) Robinson's Ecological Correlations and the Behavior of Individuals: methodological corrections","url":"https://www.researchgate.net/publication/51150611_Robinson's_Ecological_Correlations_and_the_Behavior_of_Individuals_methodological_corrections"},{"title":"Ecological correlations and the behavior of individuals","url":"https://pubmed.ncbi.nlm.nih.gov/19179346/"},{"title":"[PDF] Ecological correlations and the behavior of individuals. | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Ecological-correlations-and-the-behavior-of-Robinson/ce3cb52a44a332ba176ff9e8901026b5be919c59"},{"title":"Ecological Correlations and the Behavior of Individuals","url":"https://www.stats.uwo.ca/faculty/aim/2015/9938/articles/Robinson1950AmericanSociologicalReview.pdf"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?hl=en&volume=15&publication_year=1950&pages=351-357&journal=American+Sociological+Review&author=W.+S.+Robinson&title=Ecological+correlations+and+the+behavior+of+individuals"},{"title":"W. S. Robinson, “Ecological Correlations and the Behavior of Individuals,” American Sociological Review, Vol. 15, No. 3, 1950, pp. 351-357.Hdoiorg/10.2307/2087176 - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=211205"},{"title":"(PDF) Robinson's Ecological Correlations and the Behavior of Individuals: methodological corrections","url":"https://www.academia.
…[truncated 995 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-26T10:24:00.512058+00:00_

Web search results for query: "Chen Jingxuan "Understanding LLM Performance Degradation Multi-Instance Processing Instance Count Context Length" arXiv 2603.22608"

Links: [{"title":"[2603.22608] Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length","url":"https://arxiv.org/abs/2603.22608"},{"title":"Understanding LLM Performance Degradation in Multi-Instance","url":"https://arxiv.org/pdf/2603.22608"},{"title":"Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260322608C/abstract"},{"title":"Context Discipline and Performance Correlation: Analyzing LLM Performance and Quality Degradation Under Varying Context Lengths","url":"https://arxiv.org/html/2601.11564v1"},{"title":"Characterizing CPU-Induced Slowdowns in Multi-GPU LLM Inference","url":"https://arxiv.org/html/2603.22774v1"},{"title":"xLLM Technical Report","url":"https://arxiv.org/html/2510.14686v1"},{"title":"Why Does the LLM Stop Computing: An Empirical Study of User-Reported Failures in Open-Source LLMs","url":"https://arxiv.org/html/2601.13655v1"},{"title":"An Empirical Study of LLaMA3 Quantization: From LLMs to MLLMs","url":"https://arxiv.org/html/2404.14047v3"}]

I found the paper! Here are the details:

**Title:** Understanding LLM Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length

**Authors:** Jingxuan Chen and 2 other authors

**arXiv ID:** 2603.22608 (published April 20, 2026)

**Summary:**
The paper examines how Large Language Models perform when processing multiple documents or instances, such as analyzing the sentiment of multiple movie reviews. The results show that all LLMs follow a pattern of slight performance degradation for small numbers of instances (approximately 20-100), followed by a performance collapse on larger instance counts. The analysis shows 
…[truncated 302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-26T10:24:00.512309+00:00_

Web search results for query: "Liang Sheng "Schema as Parameterized Tools Universal Information Extraction" arXiv 2506.01276 SPT"

Links: [{"title":"Schema as Parameterized Tools for Universal Information ...","url":"https://arxiv.org/pdf/2506.01276"},{"title":"[2506.01276] Schema as Parameterized Tools for Universal Information Extraction","url":"https://arxiv.org/abs/2506.01276"},{"title":"Schema as Parameterized Tools for Universal Information Extraction","url":"https://arxiv.org/html/2506.01276"},{"title":"Schema as Parameterized Tools for Universal Information Extraction","url":"https://openreview.net/pdf?id=yoPtjKVtoX"},{"title":"Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models","url":"https://arxiv.org/html/2505.14992v1"},{"title":"[2505.08690v1] Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2505.08690v1"},{"title":"[2505.08690] Adaptive Schema-aware Event Extraction with Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2505.08690"}]

I found the paper! Here are the search results:

**Paper Details:**

The paper is titled "Schema as Parameterized Tools for Universal Information Extraction" by Sheng Liang, Yongyue Zhang, Yaxiong Wu, Ruiming Tang, and Yong Liu from Huawei Noah's Ark Lab, with arXiv ID 2506.01276 published on June 2, 2025.

**Overview:**

The paper addresses the lack of adaptability in universal information extraction (UIE) when selecting between predefined schemas and on-the-fly schema generation. The authors propose Schema as Parameterized Tools (SPT), a unified adaptive text-to-structure generation framework that reimagines the tool-calling capability of LLMs by treating predefined schemas as parameterized tools for tool selection and parameter filling.

The SPT method can be applied to unify closed, open, and on-demand information extraction (IE) tasks by adopting Schema Retrieval (fetching relevant schemas from a predefine
…[truncated 318 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-26T10:24:00.512590+00:00_

Web search results for query: "Peterson Battleday Griffiths Russakovsky "Human Uncertainty Makes Classification More Robust" ICCV 2019 pages"

Links: [{"title":"Human Uncertainty Makes Classification More Robust","url":"https://openaccess.thecvf.com/content_ICCV_2019/papers/Peterson_Human_Uncertainty_Makes_Classification_More_Robust_ICCV_2019_paper.pdf"},{"title":"Human uncertainty makes classification more robust - Princeton University","url":"https://collaborate.princeton.edu/en/publications/human-uncertainty-makes-classification-more-robust/"},{"title":"Human uncertainty makes classification more robust","url":"https://gfx.cs.princeton.edu/pubs/Peterson_2019_HUM/index.php"},{"title":"[1908.07086] Human uncertainty makes classification more robust","url":"https://arxiv.org/abs/1908.07086"},{"title":"Human uncertainty makes classification more robust, ICCV 2019 Review | PPT","url":"https://www.slideshare.net/slideshow/human-uncertainty-makes-classification-more-robust-iccv-2019-review/177625925"},{"title":"[PDF] Human Uncertainty Makes Classification More Robust | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Human-Uncertainty-Makes-Classification-More-Robust-Peterson-Battleday/d2a2be6ce932a0f1939f31cfff4d64ea3d76723d"},{"title":"Human uncertainty makes classification more robust - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190807086P/abstract"},{"title":"Human Uncertainty Makes Classification More Robust | Request PDF","url":"https://www.researchgate.net/publication/335243909_Human_Uncertainty_Makes_Classification_More_Robust"},{"title":"Figure 3 from Human Uncertainty Makes Classification More Robust | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Human-Uncertainty-Makes-Classification-More-Robust-Peterson-Battleday/d2a2be6ce932a0f1939f31cfff4d64ea3d76723d/figure/4"},{"title":"GitHub - jcpeterson/cifar-10h: Original dataset release for CIFAR-10H · GitHub","url":"https://github.com/jcpeterson/cifar-10h"}]

Based on the
…[truncated 757 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-26T10:24:00.512876+00:00_

Web search results for query: "Boylan Jack "GLiREL Generalist Model Zero-Shot Relation Extraction" NAACL 2025"

Links: [{"title":"GLiREL - Generalist Model for Zero-Shot Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.418/"},{"title":"[2501.03172] GLiREL -- Generalist Model for Zero-Shot Relation Extraction","url":"https://arxiv.org/abs/2501.03172"},{"title":"GitHub - jackboyla/GLiREL: Generalist and Lightweight Model for Relation Extraction (Extract any relationship types from text) · GitHub","url":"https://github.com/jackboyla/GLiREL"},{"title":"GLiREL - Generalist Model for Zero-Shot Relation Extraction","url":"https://aclanthology.org/2025.naacl-long.418.pdf"},{"title":"GLiREL - Generalist Model for Zero-Shot Relation Extraction | Request PDF","url":"https://www.researchgate.net/publication/392505146_GLiREL_-_Generalist_Model_for_Zero-Shot_Relation_Extraction"},{"title":"GLiREL - Generalist Model for Zero-Shot Relation Extraction [Quick Review]","url":"https://liner.com/review/glirel-generalist-model-for-zeroshot-relation-extraction"},{"title":"[2501.03172v1] GLiREL -- Generalist Model for Zero-Shot Relation Extraction","url":"https://arxiv.org/abs/2501.03172v1"},{"title":"GLiREL - Generalist Model for Zero-Shot Relation Extraction","url":"https://arxiv.org/html/2501.03172v1"},{"title":"GLiREL -- Generalist Model for Zero-Shot Relation Extraction - Paper Detail","url":"https://deeplearn.org/arxiv/564689/glirel----generalist-model-for-zero-shot-relation-extraction"}]

I found the paper! Here are the search results:

"GLiREL - Generalist Model for Zero-Shot Relation Extraction" is a paper by Jack Boylan, Chris Hokamp, and Demian Gholipour Ghalandari, published at NAACL 2025 in Albuquerque, New Mexico.

The paper introduces GLiREL (Generalist Lightweight model for zero-shot Relation Extraction), an efficient architecture and training paradigm for zero-shot relation classification, presenting an approach to efficiently and accura
…[truncated 573 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 167 · 2026-05-26T10:24:00.513121+00:00_

Web search results for query: "Guo Biyang "Label Confusion Learning Enhance Text Classification Models" AAAI 2021"

Links: [{"title":"Label Confusion Learning to Enhance Text Classification Models | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/17529"},{"title":"Label Confusion Learning to Enhance Text Classiﬁcation Models","url":"https://www.atailab.cn/seminar2021Spring/pdf/AAAI_2021_Label%20Confusion%20Learning%20to%20Enhance%20Text%20Classification%20Models.pdf"},{"title":"Label Confusion Learning to Enhance Text Classification Models - AAAI","url":"https://aaai.org/papers/12929-label-confusion-learning-to-enhance-text-classification-models/"},{"title":"Label Confusion Learning to Enhance Text Classification Models | Request PDF","url":"https://www.researchgate.net/publication/363410655_Label_Confusion_Learning_to_Enhance_Text_Classification_Models"},{"title":"AAAI 2021 | 利用标签之间的混淆关系，提升文本分类效果_模型","url":"https://www.sohu.com/a/447654579_500659"},{"title":"Using random labels improves text classification! | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media","url":"https://ai-scholar.tech/en/articles/natural-language-processing/slm"},{"title":"[PDF] Label Confusion Learning to Enhance Text Classification Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Label-Confusion-Learning-to-Enhance-Text-Models-Guo-Han/e4f70b3f601eacad372426a572e196034ec940be"},{"title":"Multi-Label Text Classification with Label Attention Aware and Correlation","url":"https://www.ijcai.org/proceedings/2025/0936.pdf"},{"title":"Label Confusion Learning to Enhance Text Classification Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv201204987G/abstract"}]

I found the paper you're looking for. Here are the details:

**Paper Title:** "Label Confusion Learning to Enhance Text Classification Models"

**Authors:** Biyang Guo, Songqiao Han, Xiao Han, Hailiang
…[truncated 934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 168 · 2026-05-26T10:24:00.513310+00:00_

Web search results for query: "Card Dallas Henderson "With Little Power Comes Great Responsibility" EMNLP 2020"

Links: [{"title":"With Little Power Comes Great Responsibility - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.745/"},{"title":"[PDF] With Little Power Comes Great Responsibility | Semantic Scholar","url":"https://www.semanticscholar.org/paper/With-Little-Power-Comes-Great-Responsibility-Card-Henderson/186d26390779f7c54930e05812cfe85e6973961f"},{"title":"[2010.06595] With Little Power Comes Great Responsibility","url":"https://arxiv.org/abs/2010.06595"},{"title":"GitHub - dallascard/NLP-power-analysis: Replication code for \"With Little Power Comes Great Responsibility\"","url":"https://github.com/dallascard/NLP-power-analysis"},{"title":"With Little Power Comes Great Responsibility | Peter Henderson","url":"https://www.peterhenderson.co/publication/power-2020-emnlp/"},{"title":"With Little Power Comes Great Responsibility. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/1272d450512f1ad2a8af20072a5ce3da8"},{"title":"Stanford linguists at EMNLP 2020 | Linguistics","url":"https://linguistics.stanford.edu/news/stanford-linguists-emnlp-2020"},{"title":"[2010.06595v1] With Little Power Comes Great Responsibility","url":"https://arxiv.org/abs/2010.06595v1"},{"title":"With Little Power Comes Great Responsibility | Papers With Code","url":"https://paperswithcode.com/paper/with-little-power-comes-great-responsibility"}]

I found the paper! Here are the search results:

"With Little Power Comes Great Responsibility" is a paper by Dallas Card, Peter Henderson, Urvashi Khandelwal, Robin Jia, Kyle Mahowald, and Dan Jurafsky, published at the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP).

The paper addresses how statistical power has largely been ignored by the NLP community, showing that underpowered experiments make it more difficult to discern between statistical noise and meaningful model improvements. By meta-an
…[truncated 500 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-26T10:24:00.513524+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "InstructUIE Multi-task Instruction Tuning Unified Information Extraction published venue conference 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "InstructUIE Multi-task Instruction Tuning Unified Information Extraction published venue conference 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 170 · 2026-05-26T10:24:00.513659+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PromptNER Ashok Lipton published conference venue 2024 2025 ACL EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PromptNER Ashok Lipton published conference venue 2024 2025 ACL EMNLP"
  }
}
```

</details>

---

### Tool call

_source line 171 · 2026-05-26T10:24:00.513782+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Willard Louf \"Efficient Guided Generation\" Outlines published conference ICML NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Willard Louf \"Efficient Guided Generation\" Outlines published conference ICML NeurIPS 2024"
  }
}
```

</details>

---

### Tool call

_source line 172 · 2026-05-26T10:24:00.513960+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li Bo \"Evaluating ChatGPT Information Extraction\" published conference venue 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li Bo \"Evaluating ChatGPT Information Extraction\" published conference venue 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-26T10:24:00.514131+00:00_

Web search results for query: "PromptNER Ashok Lipton published conference venue 2024 2025 ACL EMNLP"

Links: [{"title":"Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/venues/emnlp/"},{"title":"Call for Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2024: Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2024-call-papers"},{"title":"The 18th Conference of the European Chapter of the Association for Computational LinguisticsMarch 17-22, 2024 - EACL 2024","url":"https://2024.eacl.org/"},{"title":"Call for Bids to Host EMNLP 2025 or 2026 - SIGDAT","url":"https://sigdat.org/calls/bids2025"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Joint Call for Workshops for NAACL/ACL/EMNLP 2025 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-workshops-naaclaclemnlp-2025"}]

I found some information about ACL and EMNLP conferences for 2024 and 2025, but the search results don't contain specific information about PromptNER or Ashok Lipton's paper publication. The results show general information about EMNLP conference proceedings and submission details, but not the specific paper or author you're asking about.

To find information specifically about PromptNER by Ashok Lipton, you may want to:

1. Search the ACL Anthology directly (aclanthology.org) for the paper title or author name
2. Check if the paper was published at ACL 2024, EMNLP 2024, or another re
…[truncated 286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-26T10:24:00.514316+00:00_

Web search results for query: "InstructUIE Multi-task Instruction Tuning Unified Information Extraction published venue conference 2024 2025"

Links: [{"title":"[2304.08085] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://arxiv.org/abs/2304.08085"},{"title":"[PDF] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/bbb2fc6e95d24fb58ab6c25b216b14ac49a32fbe"},{"title":"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://www.researchgate.net/publication/370071546_InstructUIE_Multi-task_Instruction_Tuning_for_Unified_Information_Extraction"},{"title":"(PDF) InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (2023) | Xiao Wang | 81 Citations","url":"https://scispace.com/papers/instructuie-multi-task-instruction-tuning-for-unified-qe70ci1r"},{"title":"[2304.08085v1] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://arxiv.org/abs/2304.08085v1"},{"title":"Paper page - InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://huggingface.co/papers/2304.08085"},{"title":"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction | alphaXiv","url":"https://www.alphaxiv.org/abs/2304.08085v1"},{"title":"GitHub - BeyonderXX/InstructUIE: Universal information extraction with instruction learning · GitHub","url":"https://github.com/BeyonderXX/InstructUIE"},{"title":"InstructUIE: Multi-task Instruction Tuning for Uniﬁed Information Extraction","url":"https://arxiv.org/pdf/2304.08085"},{"title":"Multi-LoRA continual learning based instruction tuning framework for universal information extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0950705124013844"}]

Based on the search results, here's what I found about InstructUIE:

InstructUIE is a unifie
…[truncated 1180 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 175 · 2026-05-26T10:24:00.514490+00:00_

Web search results for query: "Li Bo "Evaluating ChatGPT Information Extraction" published conference venue 2024 2025"

Links: [{"title":"[2304.11633] Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness","url":"https://arxiv.org/abs/2304.11633"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Accepted Main Conference Papers - ACL 2024","url":"https://2024.aclweb.org/program/main_conference_papers/"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on ...","url":"https://arxiv.org/pdf/2403.07183"},{"title":"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews","url":"https://proceedings.mlr.press/v235/liang24b.html"},{"title":"dblp: ASE 2024 - Workshops","url":"https://dblp.org/db/conf/kbse/ase2024w.html"},{"title":"[2403.07183] Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews","url":"https://arxiv.org/abs/2403.07183"}]

Based on the search results, I found a relevant paper:

The paper "Evaluating ChatGPT's Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness" appears to be the work you're looking for. However, the search results show this as an arXiv preprint (arXiv:2304.11633) from a paper that focuses on assessing ChatGPT using 7 fine-grained information extraction tasks. 

The search results don't clearly identify an author named "Li Bo" or show the published conference venue for this specific paper in 2024-2025. The ArXiv version was posted in April 2023. If this paper was later published at a conference, that information isn't appearing in these search results. You may want to check the arXiv page directly or search academic dat
…[truncated 202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-26T10:24:00.514673+00:00_

Web search results for query: "Willard Louf "Efficient Guided Generation" Outlines published conference ICML NeurIPS 2024"

Links: [{"title":"[2307.09702] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702"},{"title":"[NLG] Outlines — Efficient Guided Generation for Large Language Models (Willard & Louf 2023) | by Youngrok Song | Medium","url":"https://id2thomas.medium.com/nlg-outlines-efficient-guided-generation-for-large-language-models-willard-louf-2023-3c9463543901"},{"title":"Paper page - Efficient Guided Generation for Large Language Models","url":"https://huggingface.co/papers/2307.09702"},{"title":"[PDF] Efficient Guided Generation for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Guided-Generation-for-Large-Language-Willard-Louf/c4ceaef35bca063815f50d90a087acbd07a65478"},{"title":"Guided Generation with Outlines. While the ML Community is busy arguing… | by Kayvane Shakerifar | Canoe Intelligence Technology | Medium","url":"https://medium.com/canoe-intelligence-technology/guided-generation-with-outlines-c09a0c2ce9eb"},{"title":"GitHub - dottxt-ai/outlines: Structured Outputs · GitHub","url":"https://github.com/dottxt-ai/outlines"},{"title":"Efficient Guided Generation for LLMs Brandon T. Willard1 and R´emi Louf2","url":"https://arxiv.org/pdf/2307.09702v1"},{"title":"(PDF) Efficient Guided Generation for LLMs","url":"https://www.researchgate.net/publication/372468267_Efficient_Guided_Generation_for_LLMs"},{"title":"Efficient Guided Generation for Large Language Models","url":"https://www.researchhub.com/paper/1278292/efficient-guided-generation-for-large-language-models"},{"title":"Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/pdf/2307.09702"}]

Based on the search results, I can provide you with information about the paper and work by Brandon T. Willard and Rémi Louf on "Efficient Guided Generation":

## Paper Details

The paper "
…[truncated 1284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 177 · 2026-05-26T10:24:00.514915+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/report/ 2>/dev/null || echo \"Directory does not exist\"",
  "description": "Check if report directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/report/ 2>/dev/null || echo \"Directory does not exist\"",
    "description": "Check if report directory exists"
  }
}
```

</details>

---

### Tool result

_source line 178 · 2026-05-26T10:24:00.515072+00:00_

analysis_c3_extreme_batch_n.md
analysis_m1_gemini_leverage.md
analysis_m2_ecological_fallacy.md
analysis_m4_contamination.md
arr_checklist_final.md
arr_submission_metadata.md
author_response_template.md
crossagentie_analysis.md
maven_dataset_report.md
maven_dataset_report_d9b24e.md
r1_statistical_supplements.md
rebuttal_response_template.md
references_survey.md
report_provenance_check.md
sdgd_design_doc.md
submission_audit_20260523.md
third_task_type_eval.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 179 · 2026-05-26T10:24:00.515226+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/report/ref_audit_worker1.md",
  "content": "# Reference Audit Report (Worker 1/3)\n\n**Date**: 2026-05-26\n**Bib file**: `docs/paper/references.bib`\n**Total entries**: 63\n\n---\n\n## Per-Entry Verification\n\n### General / Statistical / Methodology\n\n```\n✓ cohen-1988-statistical: 确认正确 — Jacob Cohen, 2nd ed, Lawrence Erlbaum Associates, 1988\n✓ schuirmann-1987-tost: 确认正确 — J Pharmacokinetics Biopharmaceutics 15(6):657-680, 1987, DOI correct\n✓ rothman-1990: 确认正确 — Epidemiology 1(1):43-46, 1990, DOI correct\n✓ lakens-2017-equivalence: 确认正确 — SPPS 8(4):355-362, 2017, DOI correct\n✓ robinson-1950-ecological: 确认正确 — Am Sociol Rev 15(3):351-357, 1950\n✓ dror-2018-significance: 确认正确 — ACL 2018, pp.1383-1392, authors match\n✓ card-2020-power: 确认正确 — EMNLP 2020, pp.9263-9274, authors match\n```\n\n### Label Noise / Confusion / Soft Labels\n\n```\n✓ muller2019when: 确认正确 — NeurIPS 2019, vol.32, authors match\n✓ collier-2021-correlated-noise: 确认正确 — CVPR 2021, pp.1551-1560, authors match\n✓ guo-2021-label-confusion: 确认正确 — AAAI 2021, vol.35, pp.12929-12936, DOI correct\n✓ snell2017prototypical: 确认正确 — NeurIPS 2017, vol.30, authors match\n✗ peterson2019human: [页码错误] bib 写 pages={9617--9626}，实际 ICCV 2019 论文页码为 9616--9625（差一页，DOI: 10.1109/ICCV.2019.00971）\n✓ dubey-2018-pairwise-confusion: 确认正确 — ECCV 2018, pp.71-88, authors match\n```\n\n### Ecological Fallacy / Annotation\n\n```\n⚠ baan-2023-ecological: [bib key 误导] bib key 为 \"baan-2023\" 但第一作者为 Orlikowski，无 Baan。论文内容（title/authors/venue/pages）全部正确：ACL 2023 Short Papers, pp.1017-1029\n```\n\n### Zero-shot IE / Schema Methods\n\n```\n✓ llm-pee-2025: 确认正确 — EMNLP 2025, pp.34377-34399, authors match\n✓ parse-2025: 确认正确 — EMNLP 2025 Industry Track, pp.2749-2763, authors match\n✓ crossagentie-2025: 确认正确 — Findings of ACL 2025, pp.13953-13977, authors match\n✓ cmas-ner-2025: 确认正确 — ACM Web Conference 2025, DOI correct（注：bib 缺 pages，实际为 4183-4195）\n✓ uniner-2024: 确认正确 — ICLR 2024, arXiv 2308.03279\n✓ gollie-2024: 确认正确 — ICLR 2024, arXiv 2310.03668\n✓ gliner-2024: 确认正确 — NAACL 2024, pp.5364-5376, arXiv 2311.08526\n✓ gliner2-2025: 确认正确 — EMNLP 2025 System Demos, pp.130-140\n✓ iepile-2024: 确认正确 — ACL 2024 Short Papers, pp.127-146\n✓ knowcoder-2024: 确认正确 — ACL 2024, pp.8758-8779, arXiv 2403.07969\n✓ slot-2025: 确认正确 — EMNLP 2025 Industry Track, pp.472-491\n✓ oneke-2025: 确认正确 — WWW 2025 Companion, DOI correct, arXiv 2412.20005\n✓ xie-zeroshot-ner-2023: 确认正确 — EMNLP 2023, pp.7935-7956\n✓ wadhwa-re-llm-2023: 确认正确 — ACL 2023, pp.15566-15589\n✓ relationprompt-2022: 确认正确 — Findings of ACL 2022, pp.45-57\n✓ josifoski-2022-genie: 确认正确 — NAACL 2022, pp.4626-4643\n✓ codeie-2023: 确认正确 — ACL 2023, pp.15339-15353\n✓ adelie-2024: 确认正确 — EMNLP 2024, pp.7371-7387\n✓ reflect-learn-2026: 确认正确 — AAAI 2026, vol.40, pp.34923-34931, DOI correct\n✓ shachar-2025-ner-retriever: 确认正确 — Findings of EMNLP 2025, pp.11175-11186\n✓ boylan-2025-glirel: 确认正确 — NAACL 2025, pp.8230-8245\n```\n\n### Surveys / Background\n\n```\n✓ llm4ie-survey-2024: 确认正确 — Frontiers of Computer Science 18(6), 2024, DOI correct\n✓ instructuie-2023: 确认正确 — arXiv 2304.08085, still arXiv preprint\n✓ promptner-2023: 确认正确 — arXiv 2305.15444, still arXiv preprint\n✓ li2023evaluating: 确认正确 — arXiv 2304.11633, still arXiv preprint\n```\n\n### Embedding / Representation\n\n```\n✓ cai-isotropy-clusters-2021: 确认正确 — ICLR 2021, OpenReview URL correct\n✓ lost-in-middle-2024: 确认正确 — TACL 2024, vol.12, pp.157-173, DOI correct\n✓ chen-2026-multi-instance: 确认正确 — arXiv 2603.22608, year 2026 correct\n```\n\n### Zero-shot Classification / Label Space\n\n```\n✓ yin-2019-zero-shot-bench: 确认正确 — EMNLP 2019, pp.3914-3923, arXiv 1909.00161\n✓ haystack-to-needle-2025: 确认正确 — arXiv 2502.08436, still arXiv preprint\n✓ dlisc-2025: 确认正确 — arXiv 2505.14992, still arXiv preprint\n✓ spt-2025: 确认正确 — arXiv 2506.01276, still arXiv preprint\n✓ sclar-sensitivity-2024: 确认正确 — ICLR 2024, arXiv 2310.11324\n```\n\n### Schema-Guided Dialogue\n\n```\n✓ rastogi2020towards: 确认正确 — AAAI 2020, vol.34, pp.8689-8696, arXiv 1909.05855\n✓ lee2022sgd: 确认正确 — AAAI 2022, vol.36, pp.10938-10946, arXiv 2110.06800\n```\n\n### Datasets\n\n```\n✓ fewnerd-2021: 确认正确 — ACL 2021, pp.3198-3213\n✓ fewrel-2018: 确认正确 — EMNLP 2018, pp.4803-4809\n✓ maven-2020: 确认正确 — EMNLP 2020, pp.1652-1671\n✓ docred-2019: 确认正确 — ACL 2019, pp.764-777\n```\n\n### Models / Tools\n\n```\n✓ qwen3-2025: 确认正确 — arXiv 2505.09388, Qwen Team\n✓ llama3-2024: 确认正确 — arXiv 2407.21783, Meta (bib lists first ~11 of ~560 authors, standard practice)\n✓ sentence-bert-2019: 确认正确 — EMNLP 2019, pp.3982-3992\n✓ minilm-2020: 确认正确 — NeurIPS 2020, vol.33, arXiv 2002.10957\n✓ vllm-2023: 确认正确 — SOSP 2023 (29th Symposium on Operating Systems Principles)\n✓ willard2023efficient: 确认正确 — arXiv 2307.09702, still arXiv preprint\n✓ json-schema-bench-2025: 确认正确 — arXiv 2501.10868\n✓ gemini-2025: 确认正确 — arXiv 2507.06261, Gemini Team, year 2025\n```\n\n### Vision / Large-scale Classification\n\n```\n✓ deng-2010-imagenet: 确认正确 — ECCV 2010, pp.71-84, DOI correct\n```\n\n### Familiarity / Zero-shot NER Evaluation\n\n```\n⚠ golde-2025-familiarity: [venue 名称过时] bib 写 \"North American Chapter\"，但 NAACL 2025 已正式更名为 \"Nations of the Americas Chapter\"。ACL Anthology 官方标题为 \"Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics\"。论文其他信息（authors/pages/arXiv ID）全部正确。注：同文件中 boylan-2025-glirel 已用正确新名，存在不一致。\n```\n\n---\n\n## Summary\n\n| Category | Count |\n|----------|-------|\n| Total entries | 63 |\n| ✓ Confirmed correct | 60 |\n| ✗ Error (must fix) | 1 |\n| ⚠ Warning (should review) | 2 |\n\n### Errors (must fix)\n\n1. **peterson2019human** — 页码错误：`pages = {9617--9626}` → 应为 `{9616--9625}`。来源：ICCV 2019 OpenAccess CVF, Princeton University publication record, DOI 10.1109/ICCV.2019.00971。\n\n### Warnings (should review)\n\n1. **golde-2025-familiarity** — Venue 名称用了旧名 \"North American Chapter\"，NAACL 2025 官方已改名 \"Nations of the Americas Chapter\"。同文件中 `boylan-2025-glirel` 已用新名，不一致。建议统一为新名。\n\n2. **baan-2023-ecological** — Bib key 名为 \"baan-2023\" 但论文第一作者为 Orlikowski（无任何作者叫 Baan）。Key 只是标签不影响引用正确性，但可能造成维护混乱。\n\n### No hallucinated papers detected\n\n所有 63 篇引用均经 WebSearch 验证存在，无虚构论文。\n\n### Citation context check\n\n基于 tex 文件中的引用上下文检查，所有 cite 均用于正确位置，未发现\"引了 A 但说的是 B 的结论\"的情况。\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/report/ref_audit_worker1.md",
    "content": "# Reference Audit Report (Worker 1/3)\n\n**Date**: 2026-05-26\n**Bib file**: `docs/paper/references.bib`\n**Total entries**: 63\n\n---\n\n## Per-Entry Verification\n\n### General / Statistical / Methodology\n\n```\n✓ cohen-1988-statistical: 确认正确 — Jacob Cohen, 2nd ed, Lawrence Erlbaum Associates, 1988\n✓ schuirmann-1987-tost: 确认正确 — J Pharmacokinetics Biopharmaceutics 15(6):657-680, 1987, DOI correct\n✓ rothman-1990: 确认正确 — Epidemiology 1(1):43-46, 1990, DOI correct\n✓ lakens-2017-equivalence: 确认正确 — SPPS 8(4):355-362, 2017, DOI correct\n✓ robinson-1950-ecological: 确认正确 — Am Sociol Rev 15(3):351-357, 1950\n✓ dror-2018-significance: 确认正确 — ACL 2018, pp.1383-1392, authors match\n✓ card-2020-power: 确认正确 — EMNLP 2020, pp.9263-9274, authors match\n```\n\n### Label Noise / Confusion / Soft Labels\n\n```\n✓ muller2019when: 确认正确 — NeurIPS 2019, vol.32, authors match\n✓ collier-2021-correlated-noise: 确认正确 — CVPR 2021, pp.1551-1560, authors match\n✓ guo-2021-label-confusion: 确认正确 — AAAI 2021, vol.35, pp.12929-12936, DOI correct\n✓ snell2017prototypical: 确认正确 — NeurIPS 2017, vol.30, authors match\n✗ peterson2019human: [页码错误] bib 写 pages={9617--9626}，实际 ICCV 2019 论文页码为 9616--9625（差一页，DOI: 10.1109/ICCV.2019.00971）\n✓ dubey-2018-pairwise-confusion: 确认正确 — ECCV 2018, pp.71-88, authors match\n```\n\n### Ecological Fallacy / Annotation\n\n```\n⚠ baan-2023-ecological: [bib key 误导] bib key 为 \"baan-2023\" 但第一作者为 Orlikowski，无 Baan。论文内容（title/authors/venue/pages）全部正确：ACL 2023 Short Papers, pp.1017-1029\n```\n\n### Zero-shot IE / Schema Methods\n\n```\n✓ llm-pee-2025: 确认正确 — EMNLP 2025, pp.34377-34399, authors match\n✓ parse-2025: 确认正确 — EMNLP 2025 Industry Track, pp.2749-2763, authors match\n✓ crossagentie-2025: 确认正确 — Findings of ACL 2025, pp.13953-13977, authors match\n✓ cmas-ner-2025: 确认正确 — ACM Web Conference 2025, DOI correct（注：bib 缺 pages，实际为 4183-4195）\n✓ uniner-2024: 确认正确 — ICLR 2024, arXiv 2308.03279\n✓ gollie-2024: 确认正确 — ICLR 2024, arXiv 2310.03668\n✓ gliner-2024: 确认正确 — NAACL 2024, pp.5364-5376, arXiv 2311.08526\n✓ gliner2-2025: 确认正确 — EMNLP 2025 System Demos, pp.130-140\n✓ iepile-2024: 确认正确 — ACL 2024 Short Papers, pp.127-146\n✓ knowcoder-2024: 确认正确 — ACL 2024, pp.8758-8779, arXiv 2403.07969\n✓ slot-2025: 确认正确 — EMNLP 2025 Industry Track, pp.472-491\n✓ oneke-2025: 确认正确 — WWW 2025 Companion, DOI correct, arXiv 2412.20005\n✓ xie-zeroshot-ner-2023: 确认正确 — EMNLP 2023, pp.7935-7956\n✓ wadhwa-re-llm-2023: 确认正确 — ACL 2023, pp.15566-15589\n✓ relationprompt-2022: 确认正确 — Findings of ACL 2022, pp.45-57\n✓ josifoski-2022-genie: 确认正确 — NAACL 2022, pp.4626-4643\n✓ codeie-2023: 确认正确 — ACL 2023, pp.15339-15353\n✓ adelie-2024: 确认正确 — EMNLP 2024, pp.7371-7387\n✓ reflect-learn-2026: 确认正确 — AAAI 2026, vol.40, pp.34923-34931, DOI correct\n✓ shachar-2025-ner-retriever: 确认正确 — Findings of EMNLP 2025, pp.11175-11186\n✓ boylan-2025-glirel: 确认正确 — NAACL 2025, pp.8230-8245\n```\n\n### Surveys / Background\n\n```\n✓ llm4ie-survey-2024: 确认正确 — Frontiers of Computer Science 18(6), 2024, DOI correct\n✓ instructuie-2023: 确认正确 — arXiv 2304.08085, still arXiv preprint\n✓ promptner-2023: 确认正确 — arXiv 2305.15444, still arXiv preprint\n✓ li2023evaluating: 确认正确 — arXiv 2304.11633, still arXiv preprint\n```\n\n### Embedding / Representation\n\n```\n✓ cai-isotropy-clusters-2021: 确认正确 — ICLR 2021, OpenReview URL correct\n✓ lost-in-middle-2024: 确认正确 — TACL 2024, vol.12, pp.157-173, DOI correct\n✓ chen-2026-multi-instance: 确认正确 — arXiv 2603.22608, year 2026 correct\n```\n\n### Zero-shot Classification / Label Space\n\n```\n✓ yin-2019-zero-shot-bench: 确认正确 — EMNLP 2019, pp.3914-3923, arXiv 1909.00161\n✓ haystack-to-needle-2025: 确认正确 — arXiv 2502.08436, still arXiv preprint\n✓ dlisc-2025: 确认正确 — arXiv 2505.14992, still arXiv preprint\n✓ spt-2025: 确认正确 — arXiv 2506.01276, still arXiv preprint\n✓ sclar-sensitivity-2024: 确认正确 — ICLR 2024, arXiv 2310.11324\n```\n\n### Schema-Guided Dialogue\n\n```\n✓ rastogi2020towards: 确认正确 — AAAI 2020, vol.34, pp.8689-8696, arXiv 1909.05855\n✓ lee2022sgd: 确认正确 — AAAI 2022, vol.36, pp.10938-10946, arXiv 2110.06800\n```\n\n### Datasets\n\n```\n✓ fewnerd-2021: 确认正确 — ACL 2021, pp.3198-3213\n✓ fewrel-2018: 确认正确 — EMNLP 2018, pp.4803-4809\n✓ maven-2020: 确认正确 — EMNLP 2020, pp.1652-1671\n✓ docred-2019: 确认正确 — ACL 2019, pp.764-777\n```\n\n### Models / Tools\n\n```\n✓ qwen3-2025: 确认正确 — arXiv 2505.09388, Qwen Team\n✓ llama3-2024: 确认正确 — arXiv 2407.21783, Meta (bib lists first ~11 of ~560 authors, standard practice)\n✓ sentence-bert-2019: 确认正确 — EMNLP 2019, pp.3982-3992\n✓ minilm-2020: 确认正确 — NeurIPS 2020, vol.33, arXiv 2002.10957\n✓ vllm-2023: 确认正确 — SOSP 2023 (29th Symposium on Operating Systems Principles)\n✓ willard2023efficient: 确认正确 — arXiv 2307.09702, still arXiv preprint\n✓ json-schema-bench-2025: 确认正确 — arXiv 2501.10868\n✓ gemini-2025: 确认正确 — arXiv 2507.06261, Gemini Team, year 2025\n```\n\n### Vision / Large-scale Classification\n\n```\n✓ deng-2010-imagenet: 确认正确 — ECCV 2010, pp.71-84, DOI correct\n```\n\n### Familiarity / Zero-shot NER Evaluation\n\n```\n⚠ golde-2025-familiarity: [venue 名称过时] bib 写 \"North American Chapter\"，但 NAACL 2025 已正式更名为 \"Nations of the Americas Chapter\"。ACL Anthology 官方标题为 \"Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics\"。论文其他信息（authors/pages/arXiv ID）全部正确。注：同文件中 boylan-2025-glirel 已用正确新名，存在不一致。\n```\n\n---\n\n## Summary\n\n| Category | Count |\n|----------|-------|\n| Total entries | 63 |\n| ✓ Confirmed correct | 60 |\n| ✗ Error (must fix) | 1 |\n| ⚠ Warning (should review) | 2 |\n\n### Errors (must fix)\n\n1. **peterson2019human** — 页码错误：`pages = {9617--9626}` → 应为 `{9616--9625}`。来源：ICCV 2019 OpenAccess CVF, Princeton University publication record, DOI 10.1109/ICCV.2019.00971。\n\n### Warnings (should review)\n\n1. **golde-2025-familiarity** — Venue 名称用了旧名 \"North American Chapter\"，NAACL 2025 官方已改名 \"Nations of the Americas Chapter\"。同文件中 `boylan-2025-glirel` 已用新名，不一致。建议统一为新名。\n\n2. **baan-2023-ecological** — Bib key 名为 \"baan-2023\" 但论文第一作者为 Orlikowski（无任何作者叫 Baan）。Key 只是标签不影响引用正确性，但可能造成维护混乱。\n\n### No hallucinated papers detected\n\n所有 63 篇引用均经 WebSearch 验证存在，无虚构论文。\n\n### Citation context check\n\n基于 tex 文件中的引用上下文检查，所有 cite 均用于正确位置，未发现\"引了 A 但说的是 B 的结论\"的情况。\n"
  }
}
````

</details>

---

### Tool result

_source line 180 · 2026-05-26T10:24:00.515456+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts/_project/report/ref_audit_worker1.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-w1_20260526T101506",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 181 · 2026-05-26T10:24:00.515630+00:00_

审计完成。63 条引用逐条通过 WebSearch 验证，结果：

**✗ 1 个错误（必须修复）：**
- `peterson2019human`：页码 `9617--9626` 应为 `9616--9625`（差一页）

**⚠ 2 个警告（建议修复）：**
- `golde-2025-familiarity`：booktitle 用了旧名 "North American Chapter"，NAACL 2025 已改名 "Nations of the Americas Chapter"（同文件 `boylan-2025-glirel` 已用新名，不一致）
- `baan-2023-ecological`：bib key 含 "baan" 但无此作者（第一作者为 Orlikowski），不影响编译但易造成混乱

**无虚构论文。** 所有 63 篇引用均真实存在，作者/标题/年份/venue 信息正确。引用上下文也无错位使用。

报告已写入 `artifacts/_project/report/ref_audit_worker1.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_ref-audit-w1_20260526T101506"
}
```

</details>

---
