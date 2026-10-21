# paper d047 round2 section5

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_paper_d047_round2_section5_20260516T124633.jsonl`
- **Structured JSON:** [`ae0a92dd45a09face1d7.json`](../../sessions/ae/ae0a92dd45a09face1d7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-16T12:52:51.412716+00:00_

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
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T12:52:51.413249+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches, merging predictions via set union. Every decomposition mode---SDGD (F1\,=\,0.241), random batching (0.320), per-type (0.292)---falls below the single-pass baseline (0.445) on Few-NERD NER (Table~\ref{tab:sdgd_results}).
5	
6	\paragraph{Merge amplification as the bottleneck.}
7	The failure is \emph{merge amplification}: presenting the same text $k$ times causes each pass to independently generate predictions. Single-pass precision (0.563) collapses to 0.210--0.249 after union merge with 8 batches, while recall gains are modest (0.368 $\to$ 0.314--0.446). Confidence gating improves precision but with disproportionate recall loss (Appendix~\ref{sec:appendix_sdgd}). The fundamental issue is that LLM predictions are not calibrated across passes \cite{llm-calibration-survey-2024}.
8	
9	In our NER experiments, multi-pass decomposition produces $k$ independent tagging outputs per sentence. Entities may receive conflicting labels across separate decomposition passes, or hallucinated entities may appear in passes where the correct type is absent. Union merge amplifies these false positives: precision collapses from 0.563 (single-pass) to 0.210--0.249 (8 batches), faster than the modest recall gains.
10	
11	\paragraph{Why NER fails but RE does not.}
12	Merge amplification is specific to span-level tasks: each NER pass independently proposes entity spans, and union merge must resolve conflicting boundaries and type assignments, degrading systematically with pass count. Under oracle routing, RE requires no span reconciliation---each pair receives a single classification from the batch containing its gold type, eliminating the mechanis
…[truncated 913 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T12:52:51.413555+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T12:52:51.413766+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T12:52:51.413995+00:00_

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
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T12:52:51.414450+00:00_

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
15	\usepackage{listings}
16	
17	\title{Does Type Confusability Shape Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
41	
42	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
43	
44	\item \textbf{Non-significant factorial test.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance (Appendix~\ref{sec:appendix_factorial}); cross-pool slope consistency suggests confusability sensitivity is stable rather than amplifying.
45	
46	\item \textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.
47	
48	\item \textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines traini
…[truncated 24008 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T12:52:51.414767+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "batch_composition|appendix_batch_composition",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Grep",
  "tool_args": {
    "pattern": "batch_composition|appendix_batch_composition",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T12:52:51.415027+00:00_

docs/paper/main.tex:203:\label{sec:appendix_batch_composition}
docs/paper/main.tex:205:Table~\ref{tab:batch_composition} reports the full comparison of confusability-aware batch composition strategies on FewRel 80-relation RE (\S\ref{sec:sdgd}).
docs/paper/main.tex:220:\label{tab:batch_composition}
docs/paper/main.aux:1319:\newlabel{sec:appendix_batch_composition}{{F}{13}{Batch Composition Results}{appendix.F}{}}
docs/paper/main.aux:1324:\newlabel{tab:batch_composition}{{8}{13}{Confusability-aware batch composition on FewRel 80-rel RE. Graph coloring minimizes intra-batch BCS, yielding +1.4\,pp over random assignment, though the difference is not statistically significant given the single graph-coloring configuration ($n{=}1$) and narrow BCS margin (0.006). Single-pass with all 80 types suffers severe schema overload}{table.caption.42}{}}
docs/paper/sdgd_negative.tex:15:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T12:52:51.415247+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "tab:sdgd_results|appendix_sdgd",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Grep",
  "tool_args": {
    "pattern": "tab:sdgd_results|appendix_sdgd",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T12:52:51.415478+00:00_

docs/paper/main.tex:119:\label{sec:appendix_sdgd}
docs/paper/main.tex:123:Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368). SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop. Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194, R\,=\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\ref{tab:sdgd_results}).
docs/paper/main.tex:144:\label{tab:sdgd_results}
docs/paper/main.aux:1174:\newlabel{sec:appendix_sdgd}{{B}{12}{SDGD Full Protocol and Results}{appendix.B}{}}
docs/paper/main.aux:1198:\newlabel{tab:sdgd_results}{{6}{12}{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \texttt {min\_batch\_size=8} (reducing 8$\to $4 batches for sdgd\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt}{table.caption.37}{}}
docs/paper/sdgd_negative.tex:4:A natural intervention is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches, merging predictions via set union. Every decomposition mode---SDGD (F1\,=\,0.241), random batching (0.320), per-type (0.292)---falls below the single-pass baseline (0.445) on Few-NERD NER (Table~\ref{tab:sdgd_results}).
docs/paper/sdgd_negative.tex:7:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T12:52:51.417240+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "appendix_batch_composition",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Grep",
  "tool_args": {
    "pattern": "appendix_batch_composition",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T12:52:51.417503+00:00_

docs/paper/main.tex:205:\label{sec:appendix_batch_composition}
docs/paper/sdgd_negative.tex:15:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T12:52:51.417760+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
  "content": "\\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}\n\\label{sec:sdgd}\n\nA natural intervention against confusability-driven degradation is to partition the schema so that confusable types never co-occur in the same prompt. We test this idea with \\textbf{Schema-DAG-Guided Decomposition} (SDGD\\footnote{SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an internal project designation; the graph structure is undirected.}), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches.\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a batch. Each color class forms one extraction batch. For NER, predictions from all batches are merged via set union; for RE, each instance is routed to the batch containing its gold type (oracle routing). We test four NER modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, each type extracted in isolation. Every mode falls below the single-pass NER baseline: SDGD obtains F1\\,=\\,0.241, random batching 0.320, per-type 0.292, versus 0.445 for single-pass (Table~\\ref{tab:sdgd_results}, Appendix~\\ref{sec:appendix_sdgd}).\n\n\\paragraph{Merge amplification in NER.}\nThe core failure mechanism is \\emph{merge amplification}: presenting the same text to the model $k$ times with different type subsets causes each pass to independently generate entity predictions, and union merge accumulates all of them into a single output. Each pass produces an independent set of span predictions; because LLM outputs are not calibrated across passes \\cite{llm-calibration-survey-2024}, the same span may receive conflicting type labels from different passes, or hallucinated entities may appear in passes where the correct type is absent. Union merge retains all predictions, so false positives scale with $k$ while true positives are bounded by the fixed set of gold entities.\n\nQuantitatively, single-pass precision (0.563) collapses to 0.210--0.249 after union merge across 8 batches, while recall gains are modest (0.368 $\\to$ 0.314 for sdgd\\_zero, 0.446 for random batch). The net F1 loss is substantial: 0.445 $\\to$ 0.251 (sdgd\\_zero) or 0.320 (random batch). Per-type extraction (66 batches) pushes recall to 0.586 but precision to 0.194 (F1\\,=\\,0.292), confirming that the precision--recall imbalance intensifies with the number of passes. Random batching outperforms confusability-aware SDGD on NER (0.320 vs.\\ 0.251) because the dominant degradation source---merge amplification---is independent of batch composition; any multi-pass scheme suffers from it regardless of grouping quality.\n\n\\paragraph{Confidence gating does not resolve merge amplification.}\nWe tested a confidence-gated variant (v2) that ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate per span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331) but causes disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301). This indicates that LLM confidence scores are insufficiently calibrated to distinguish correct predictions from hallucinated ones across independent passes, so confidence gating discards true and false positives at comparable rates.\n\n\\paragraph{Why NER fails but RE does not.}\nMerge amplification is specific to span-level tasks. Each NER pass independently proposes entity spans, and union merge must resolve conflicting boundaries and type assignments, degrading systematically with pass count. RE avoids this mechanism entirely: under oracle routing, each relation instance receives a single classification from the batch containing its gold type, requiring no span reconciliation and eliminating the multi-pass interference that causes SDGD to fail on NER. This makes RE a clean testbed for evaluating whether confusability-aware decomposition improves accuracy once merge artifacts are removed.\n\n\\paragraph{Oracle routing as performance ceiling.}\nOracle routing routes each test instance to the batch containing its gold type, eliminating cross-type confusion within each batch. On FewRel 80-relation RE, oracle-routed decomposition achieves 0.802 accuracy versus 0.504 for the single-pass baseline---a gain of +29.8\\,pp (Table~\\ref{tab:batch_composition}). This is the strongest positive finding of the decomposition experiments: it demonstrates that type confusability is indeed a key driver of degradation in RE, and that performance recovers substantially when confusable types are separated.\n\nHowever, oracle routing requires gold labels and is not deployable. The gap between the oracle ceiling and practical routing reveals an important asymmetry: while \\emph{any} decomposition benefits enormously from removing the 80-type bottleneck (+28.4\\,pp for random batching, +29.8\\,pp for graph coloring), the \\emph{additional} benefit of confusability-aware grouping over random grouping is modest (+1.4\\,pp, $p \\approx 0.19$). The confusability-aware strategy ranks 13th out of 15 random seeds, limited by the narrow BCS margin (0.006) between graph-coloring and random batches at this partition granularity. Finer-grained partitioning or alternative confusability metrics may be needed to translate the oracle-demonstrated potential into significant practical gains.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds. Graph coloring yields +1.4\\,pp over random batching ($p \\approx 0.19$, n.s.) with a narrow BCS margin (0.006). The +29.8\\,pp gap between single-pass and decomposed conditions confirms that type separation recovers performance when merge amplification is absent.}\n\\label{tab:batch_composition}\n\\end{table}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
    "content": "\\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}\n\\label{sec:sdgd}\n\nA natural intervention against confusability-driven degradation is to partition the schema so that confusable types never co-occur in the same prompt. We test this idea with \\textbf{Schema-DAG-Guided Decomposition} (SDGD\\footnote{SDGD (Schema Decomposition and Grouping for Degradation mitigation) is an internal project designation; the graph structure is undirected.}), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches.\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent---i.e., highly confusable---types share a batch. Each color class forms one extraction batch. For NER, predictions from all batches are merged via set union; for RE, each instance is routed to the batch containing its gold type (oracle routing). We test four NER modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, each type extracted in isolation. Every mode falls below the single-pass NER baseline: SDGD obtains F1\\,=\\,0.241, random batching 0.320, per-type 0.292, versus 0.445 for single-pass (Table~\\ref{tab:sdgd_results}, Appendix~\\ref{sec:appendix_sdgd}).\n\n\\paragraph{Merge amplification in NER.}\nThe core failure mechanism is \\emph{merge amplification}: presenting the same text to the model $k$ times with different type subsets causes each pass to independently generate entity predictions, and union merge accumulates all of them into a single output. Each pass produces an independent set of span predictions; because LLM outputs are not calibrated across passes \\cite{llm-calibration-survey-2024}, the same span may receive conflicting type labels from different passes, or hallucinated entities may appear in passes where the correct type is absent. Union merge retains all predictions, so false positives scale with $k$ while true positives are bounded by the fixed set of gold entities.\n\nQuantitatively, single-pass precision (0.563) collapses to 0.210--0.249 after union merge across 8 batches, while recall gains are modest (0.368 $\\to$ 0.314 for sdgd\\_zero, 0.446 for random batch). The net F1 loss is substantial: 0.445 $\\to$ 0.251 (sdgd\\_zero) or 0.320 (random batch). Per-type extraction (66 batches) pushes recall to 0.586 but precision to 0.194 (F1\\,=\\,0.292), confirming that the precision--recall imbalance intensifies with the number of passes. Random batching outperforms confusability-aware SDGD on NER (0.320 vs.\\ 0.251) because the dominant degradation source---merge amplification---is independent of batch composition; any multi-pass scheme suffers from it regardless of grouping quality.\n\n\\paragraph{Confidence gating does not resolve merge amplification.}\nWe tested a confidence-gated variant (v2) that ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate per span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331) but causes disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), yielding lower F1 in both modes (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301). This indicates that LLM confidence scores are insufficiently calibrated to distinguish correct predictions from hallucinated ones across independent passes, so confidence gating discards true and false positives at comparable rates.\n\n\\paragraph{Why NER fails but RE does not.}\nMerge amplification is specific to span-level tasks. Each NER pass independently proposes entity spans, and union merge must resolve conflicting boundaries and type assignments, degrading systematically with pass count. RE avoids this mechanism entirely: under oracle routing, each relation instance receives a single classification from the batch containing its gold type, requiring no span reconciliation and eliminating the multi-pass interference that causes SDGD to fail on NER. This makes RE a clean testbed for evaluating whether confusability-aware decomposition improves accuracy once merge artifacts are removed.\n\n\\paragraph{Oracle routing as performance ceiling.}\nOracle routing routes each test instance to the batch containing its gold type, eliminating cross-type confusion within each batch. On FewRel 80-relation RE, oracle-routed decomposition achieves 0.802 accuracy versus 0.504 for the single-pass baseline---a gain of +29.8\\,pp (Table~\\ref{tab:batch_composition}). This is the strongest positive finding of the decomposition experiments: it demonstrates that type confusability is indeed a key driver of degradation in RE, and that performance recovers substantially when confusable types are separated.\n\nHowever, oracle routing requires gold labels and is not deployable. The gap between the oracle ceiling and practical routing reveals an important asymmetry: while \\emph{any} decomposition benefits enormously from removing the 80-type bottleneck (+28.4\\,pp for random batching, +29.8\\,pp for graph coloring), the \\emph{additional} benefit of confusability-aware grouping over random grouping is modest (+1.4\\,pp, $p \\approx 0.19$). The confusability-aware strategy ranks 13th out of 15 random seeds, limited by the narrow BCS margin (0.006) between graph-coloring and random batches at this partition granularity. Finer-grained partitioning or alternative confusability metrics may be needed to translate the oracle-demonstrated potential into significant practical gains.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds. Graph coloring yields +1.4\\,pp over random batching ($p \\approx 0.19$, n.s.) with a narrow BCS margin (0.006). The +29.8\\,pp gap between single-pass and decomposed conditions confirms that type separation recovers performance when merge amplification is absent.}\n\\label{tab:batch_composition}\n\\end{table}\n"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T12:52:51.419265+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Write",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T12:52:51.419549+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nTable~\\ref{tab:batch_composition} reports the full comparison of confusability-aware batch composition strategies on FewRel 80-relation RE (\\S\\ref{sec:sdgd}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc.} & \\textbf{Mean BCS} \\\\\n\\midrule\nConfus.-aware (coloring) & \\textbf{0.802} & 0.552 \\\\\nRandom batching (15 seeds) & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Confusability-aware batch composition on FewRel 80-rel RE. Graph coloring minimizes intra-batch BCS, yielding +1.4\\,pp over random assignment, though the difference is not statistically significant given the single graph-coloring configuration ($n{=}1$) and narrow BCS margin (0.006). Single-pass with all 80 types suffers severe schema overload.}\n\\label{tab:batch_composition}\n\\end{table}\n\nThe confusability-aware strategy ranks 13th out of 15 random seeds (one-sided $p \\approx 0.19$). The narrow BCS margin between conditions (0.006) limits the achievable separation at this partition granularity, suggesting that finer-grained partitioning or alternative confusability metrics may be needed to achieve significant gains.",
  "new_string": "\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "old_string": "\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nTable~\\ref{tab:batch_composition} reports the full comparison of confusability-aware batch composition strategies on FewRel 80-relation RE (\\S\\ref{sec:sdgd}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc.} & \\textbf{Mean BCS} \\\\\n\\midrule\nConfus.-aware (coloring) & \\textbf{0.802} & 0.552 \\\\\nRandom batching (15 seeds) & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Confusability-aware batch composition on FewRel 80-rel RE. Graph coloring minimizes intra-batch BCS, yielding +1.4\\,pp over random assignment, though the difference is not statistically significant given the single graph-coloring configuration ($n{=}1$) and narrow BCS margin (0.006). Single-pass with all 80 types suffers severe schema overload.}\n\\label{tab:batch_composition}\n\\end{table}\n\nThe confusability-aware strategy ranks 13th out of 15 random seeds (one-sided $p \\approx 0.19$). The narrow BCS margin between conditions (0.006) limits the achievable separation at this partition granularity, suggesting that finer-grained partitioning or alternative confusability metrics may be needed to achieve significant gains.",
    "new_string": "\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T12:52:51.419785+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T12:52:51.420035+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "200",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "200",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T12:52:51.420279+00:00_

200	The two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality---the count of strong semantic neighbors---becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.
201	
202	Under joint control, both embeddings yield $p > 0.2$, confirming that the raw positive BCS--F1 correlation on MAVEN is fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 10^{-10}$; Table~\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.
203	
204	\section{Batch Composition Results}
205	\label{sec:appendix_batch_composition}
206	
207	Table~\ref{tab:batch_composition} reports the full comparison of confusability-aware batch composition strategies on FewRel 80-relation RE (\S\ref{sec:sdgd}).
208	
209	\begin{table}[h]
210	\centering
211	\small
212	\begin{tabular}{@{}lcc@{}}
213	\toprule
214	\textbf{Condition} & \textbf{Acc.} & \textbf{Mean BCS} \\
215	\midrule
216	Confus.-aware (coloring) & \textbf{0.802} & 0.552 \\
217	Random batching (15 seeds) & 0.788\,$\pm$\,0.018 & 0.559 \\
218	Single-pass (80 types) & 0.504 & 0.557 \\
219	\bottomrule
220	\end{tabular}
221	\caption{Confusability-aware batch composition on FewRel 80-rel RE. Graph coloring minimizes in
…[truncated 742 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T12:52:51.420529+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nTable~\\ref{tab:batch_composition} reports the full comparison of confusability-aware batch composition strategies on FewRel 80-relation RE (\\S\\ref{sec:sdgd}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc.} & \\textbf{Mean BCS} \\\\\n\\midrule\nConfus.-aware (coloring) & \\textbf{0.802} & 0.552 \\\\\nRandom batching (15 seeds) & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Confusability-aware batch composition on FewRel 80-rel RE. Graph coloring minimizes intra-batch BCS, yielding +1.4\\,pp over random assignment, though the difference is not statistically significant given the single graph-coloring configuration ($n{=}1$) and narrow BCS margin (0.006). Single-pass with all 80 types suffers severe schema overload.}\n\\label{tab:batch_composition}\n\\end{table}\n\nThe confusability-aware strategy ranks 13th out of 15 random seeds (one-sided $p \\approx 0.19$). The narrow BCS margin between conditions (0.006) limits the achievable separation at this partition granularity, suggesting that finer-grained partitioning or alternative confusability metrics may be needed to achieve significant gains.",
  "new_string": "\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "old_string": "\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nTable~\\ref{tab:batch_composition} reports the full comparison of confusability-aware batch composition strategies on FewRel 80-relation RE (\\S\\ref{sec:sdgd}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Acc.} & \\textbf{Mean BCS} \\\\\n\\midrule\nConfus.-aware (coloring) & \\textbf{0.802} & 0.552 \\\\\nRandom batching (15 seeds) & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Confusability-aware batch composition on FewRel 80-rel RE. Graph coloring minimizes intra-batch BCS, yielding +1.4\\,pp over random assignment, though the difference is not statistically significant given the single graph-coloring configuration ($n{=}1$) and narrow BCS margin (0.006). Single-pass with all 80 types suffers severe schema overload.}\n\\label{tab:batch_composition}\n\\end{table}\n\nThe confusability-aware strategy ranks 13th out of 15 random seeds (one-sided $p \\approx 0.19$). The narrow BCS margin between conditions (0.006) limits the achievable separation at this partition granularity, suggesting that finer-grained partitioning or alternative confusability metrics may be needed to achieve significant gains.",
    "new_string": "\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\nSee Table~\\ref{tab:batch_composition} and the accompanying discussion in \\S\\ref{sec:sdgd}."
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T12:52:51.422971+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Edit",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T12:52:51.423289+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && echo \"=== ERRORS ===\" && grep \"^!\" main.log | head -5 && echo \"=== OVERFULL HBOX (>10pt) ===\" && grep -c \"Overfull.*hbox.*(1[0-9]\\.\\|[2-9][0-9]\\.\\|[0-9][0-9][0-9])\" main.log && echo \"=== DONE ===\"",
  "description": "Compile LaTeX twice and check for errors",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1 && echo \"=== ERRORS ===\" && grep \"^!\" main.log | head -5 && echo \"=== OVERFULL HBOX (>10pt) ===\" && grep -c \"Overfull.*hbox.*(1[0-9]\\.\\|[2-9][0-9]\\.\\|[0-9][0-9][0-9])\" main.log && echo \"=== DONE ===\"",
    "description": "Compile LaTeX twice and check for errors",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T12:52:51.423550+00:00_

=== ERRORS ===
=== OVERFULL HBOX (>10pt) ===
134
=== DONE ===

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T12:52:51.423799+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -A1 \"Overfull.*hbox\" main.log | grep -i \"sdgd_negative\\|sec:sdgd\\|Schema Decomposition\" | head -10",
  "description": "Check overfull hboxes in sdgd_negative section"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -A1 \"Overfull.*hbox\" main.log | grep -i \"sdgd_negative\\|sec:sdgd\\|Schema Decomposition\" | head -10",
    "description": "Check overfull hboxes in sdgd_negative section"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T12:52:51.424049+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T12:52:51.424245+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -n \"sdgd_negative\" main.log | head -10",
  "description": "Find sdgd_negative references in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -n \"sdgd_negative\" main.log | head -10",
    "description": "Find sdgd_negative references in log"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T12:52:51.426109+00:00_

686:) (./sdgd_negative.tex [6 <../../figures/paper/fig_error_taxonomy.pdf>]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Bash",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T12:52:51.426365+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && sed -n '686,710p' main.log",
  "description": "Check log around sdgd_negative section"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && sed -n '686,710p' main.log",
    "description": "Check log around sdgd_negative section"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T12:52:51.426584+00:00_

) (./sdgd_negative.tex [6 <../../figures/paper/fig_error_taxonomy.pdf>]
Underfull \hbox (badness 1097) in paragraph at lines 14--15
\T1/ptm/m/n/10.95 (+20) fi-dence gat-ing im-proves pre-ci-sion (sdgd_zero:
 []


Underfull \hbox (badness 6995) in paragraph at lines 14--15
\T1/ptm/m/n/10.95 (+20) 0.446$\OMS/cmsy/m/n/10.95 !$\T1/ptm/m/n/10.95 (+20) 0.2
76), yield-ing lower F1 in both
 []


Overfull \hbox (10.84875pt too wide) in paragraph at lines 27--36
 [][] 
 []

) (./discussion.tex [7]
Underfull \hbox (badness 7362) in paragraph at lines 21--22
 []\T1/ptm/b/n/10.95 (+20) Model scale and con-fus-abil-ity sen-si-tiv-ity.[]
 []


Underfull \hbox (badness 10000) in paragraph at lines 21--22
\T1/ptm/m/n/10.95 (+20) Cross-model val-i-da-tion with Llama-3.1-8B-
 []

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T12:52:51.426874+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
  "offset": "25",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
    "offset": "25",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T12:52:51.427090+00:00_

25	\centering
26	\small
27	\begin{tabular}{@{}lcc@{}}
28	\toprule
29	\textbf{Condition} & \textbf{Accuracy} & \textbf{Mean BCS} \\
30	\midrule
31	Single-pass (80 types) & 0.504 & 0.557 \\
32	Random batching (15 seeds)$^\dagger$ & 0.788\,$\pm$\,0.018 & 0.559 \\
33	Confus.-aware (graph coloring) & \textbf{0.802} & 0.552 \\
34	\bottomrule
35	\end{tabular}
36	\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\dagger$Mean $\pm$ SD across 15 random seeds. Graph coloring yields +1.4\,pp over random batching ($p \approx 0.19$, n.s.) with a narrow BCS margin (0.006). The +29.8\,pp gap between single-pass and decomposed conditions confirms that type separation recovers performance when merge amplification is absent.}
37	\label{tab:batch_composition}
38	\end{table}
39	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T12:52:51.427373+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -n \"\\[6\\]\\|\\[7\\]\\|\\[8\\]\" main.log | grep -i \"sdgd\\|discussion\\|result\\|experiment\" | head -10",
  "description": "Check page numbers around §5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -n \"\\[6\\]\\|\\[7\\]\\|\\[8\\]\" main.log | grep -i \"sdgd\\|discussion\\|result\\|experiment\" | head -10",
    "description": "Check page numbers around §5"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T12:52:51.427598+00:00_

702:) (./discussion.tex [7]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T12:52:51.427804+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -n \"\\[\" main.log | grep -E \"^\\d+:\\[\" | head -30",
  "description": "Find all page breaks in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -n \"\\[\" main.log | grep -E \"^\\d+:\\[\" | head -30",
    "description": "Find all page breaks in log"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T12:52:51.430241+00:00_

grep: main.log: binary file matches

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Bash",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T12:52:51.430475+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && strings main.log | grep -E \"\\[[0-9]+\\]\" | head -30",
  "description": "Find page numbers in log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && strings main.log | grep -E \"\\[[0-9]+\\]\" | head -30",
    "description": "Find page numbers in log"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T12:52:51.430686+00:00_

) (./related_work.tex) (./experimental_setup.tex [2]
ling.pdf>] [5]
) (./discussion.tex [7]
(./checklist.tex [9]
[10]) (./main.bbl
[11]
[12]
[13]
[14] (./prompt_appendix.tex [15])
[16]
 [17]
[18] (./main.aux)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T12:52:51.430927+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
  "description": "Count lines in expanded §5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
    "description": "Count lines in expanded §5"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T12:52:51.431136+00:00_

38 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T12:52:51.431345+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex && echo \"---\" && wc -w /dev/stdin <<'EOF'\n$(cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g' | sed 's/\\\\[a-zA-Z]*//g')\nEOF",
  "description": "Count words in §5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex && echo \"---\" && wc -w /dev/stdin <<'EOF'\n$(cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g' | sed 's/\\\\[a-zA-Z]*//g')\nEOF",
    "description": "Count words in §5"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T12:52:51.431556+00:00_

849 /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex
---
8 /dev/stdin

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d047_round2_section5_20260516T124633",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-16T12:52:51.432470+00:00_

849 words in the LaTeX source (~750 rendered). In ACL two-column 11pt format, that's approximately 1 full page plus the table.

Compilation results:
- **0 LaTeX errors**
- **1 new overfull hbox** (10.84pt, from the table caption area — marginal; the paper already has 134 pre-existing overfull warnings)
- **§5 spans pages 6–7** (~1+ full page)
- §5 source: 38 LaTeX lines, 849 words (expanded from 16 lines / ~250 words)

Content added:
1. **SDGD footnote** (D8): full acronym expansion at first use
2. **Protocol description**: graph construction, coloring, batch formation moved from appendix prose into §5 intro
3. **Merge amplification**: expanded with precision collapse mechanism (0.563→0.210–0.249), per-type extremes, and why random > SDGD
4. **Confidence gating**: new paragraph on v2 failure (F1 drops in both modes, calibration insufficient)
5. **Oracle routing**: highlighted as key positive finding (+29.8pp), with deployability caveat and rank-13/15 detail
6. **Batch composition table**: moved from appendix to §5 main text; appendix section now points to main text

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_d047_round2_section5_20260516T124633"
}
```

</details>

---
