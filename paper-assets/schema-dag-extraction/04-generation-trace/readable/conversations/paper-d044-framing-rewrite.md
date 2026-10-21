# paper d044 framing rewrite

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 0
- **Tool calls:** 22
- **Original source:** `logs/chats/worker_paper_d044_framing_rewrite_20260516T093329.jsonl`
- **Structured JSON:** [`993ed06fc37da8fc0441.json`](../../sessions/99/993ed06fc37da8fc0441.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

45 recorded events

### Tool call

_source line 1 · 2026-05-16T09:36:23.304751+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T09:36:23.305684+00:00_

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
39	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B with cross-model validation on Llama-3.1-8B-Instruct. Whether patterns hold for proprietary models (GPT-4, Gemini) remains unverified. Channel~2 was not robustly detectable on NER at 8B scale, likely due to floor effects.
40	
41	\item \textbf{Modest pairwise effect size.} Pairwise SCS explains 1.3--1.7\% of type confusion variance; entity frequency, prompt position, mention ambiguity, and type definition quality likely account for the remainder.
42	
43	\item \textbf{Non-significant factorial test.} Within-dataset count $\times$ BCS interaction on Few-NERD did not reach significance (Appendix~\ref{sec:appendix_factorial}); cross-pool slope consistency suggests confusability sensitivity is stable rather than amplifying.
44	
45	\item \textbf{Decomposition and metric scope.} RE batch composition is tested on FewRel only; NER merge alternatives remain unexplored. SCS relies on embedding cosine similarity; label entropy or ontological depth may capture complementary dimensions.
46	
47	\item \textbf{RE format specificity.} RE's clean channel separation may reflect its closed-set classification format. FewRel combines training and validation splits 
…[truncated 288 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T09:36:23.305950+00:00_

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
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T09:36:23.306129+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level). Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and four datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall in NER and RE, but reverses direction in MAVEN (168 event types) due to centrality confounds in same-domain schemas as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE (a closed-set classification task); in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes and prompt designs: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.60$), with the quartile gap reaching $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]), though pairwise effect sizes are modest ($r^2 = 1.3\text{--}1.7\%$) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability
…[truncated 344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T09:36:23.306299+00:00_

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
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T09:36:23.306620+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this degradation? Prior decomposition strategies implicitly assume different answers: \citet{uniner-2024} extract each type independently; \citet{llm-pee-2025} partition schemas by type embedding similarity; \citet{parse-2025} optimize schema definitions. None isolates \emph{why} schemas degrade performance. The closest work, LLM-PEE, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor accounts for the gains. All prior approaches conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these, decomposition strategies optimize a black-box objective without understanding its components.
7	
8	We ask three questions. \textbf{RQ1}: Does type confusabil
…[truncated 2602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T09:36:23.306855+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "robust across prompt designs|prompt-invariant",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Grep",
  "tool_args": {
    "pattern": "robust across prompt designs|prompt-invariant",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T09:36:23.306993+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T09:36:23.307122+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "[Dd]rive",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Grep",
  "tool_args": {
    "pattern": "[Dd]rive",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T09:36:23.307244+00:00_

12:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T09:36:23.307359+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "robust.*prompt|prompt.*robust",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Grep",
  "tool_args": {
    "pattern": "robust.*prompt|prompt.*robust",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T09:36:23.307478+00:00_

docs/paper/main.tex:236:We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
docs/paper/main.tex:245:[Omitted long matching line]
docs/paper/abstract.tex:2:[Omitted long matching line]
docs/paper/introduction.tex:12:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T09:36:23.307598+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "prompt.*(design|variant|invariant)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Grep",
  "tool_args": {
    "pattern": "prompt.*(design|variant|invariant)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T09:36:23.307796+00:00_

docs/paper/main.bbl:180:  models' sensitivity to spurious features in prompt design}.
docs/paper/main.tex:236:We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
docs/paper/main.tex:245:[Omitted long matching line]
docs/paper/abstract.tex:2:[Omitted long matching line]
docs/paper/introduction.tex:12:[Omitted long matching line]
docs/paper/results.tex:67:[Omitted long matching line]
docs/paper/results.tex:134:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T09:36:23.308251+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "230",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "230",
    "limit": "25"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T09:36:23.308442+00:00_

230	
231	\input{prompt_appendix}
232	
233	\section{Prompt Version Sensitivity Analysis}
234	\label{sec:appendix_prompt_sensitivity}
235	
236	We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
237	
238	\paragraph{RE (FewRel).}
239	Under the v1 prompt, the extreme-batch BCS gap is $-$31.2\,pp (low-BCS 82.3\% vs.\ high-BCS 51.0\%; Table~\ref{tab:bcs_controlled}). Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI: [22.4, 28.6]; $p < 0.0001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.
240	
241	\paragraph{NER (Few-NERD).}
242	The batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\,=\,12$, $r = +0.58$ ($p = 0.002$, 95\% CI: [0.19, 0.81]) vs.\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \S\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\S\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.
243	
244	\paragraph{Interpretation.}
245	The $n{=}25$ v2 result confirms that the confusability effect is 
…[truncated 1245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T09:36:23.308602+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": "60",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "offset": "60",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T09:36:23.308747+00:00_

60	\end{tabular}}
61	\caption{Pairwise SCS--confusion correlation. $r^2$ indicates the fraction of variance in type confusion explained by embedding similarity. Both correlations are modest in magnitude but robust across datasets and embedding models (both $p \ll 0.001$). Confusion rate for each ordered pair $(t_i, t_j)$ is computed as the total bidirectional confusion count $C(t_i{\to}t_j) + C(t_j{\to}t_i)$ divided by the sum of gold frequencies, aggregated over all count conditions; CIs are pair-level percentile bootstrap ($B{=}1{,}000$).}
62	\label{tab:pairwise}
63	\end{table}
64	
65	The correlations are statistically significant but modest: $r^2 \approx 1.3\text{--}1.7\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). We omit FewRel: RE's per-instance classification format makes its confusion matrix not directly comparable to span-level confusion rates; the BCS-controlled experiments (\S\ref{sec:bcs_controlled}) provide quasi-experimental evidence for RE. Spearman correlations corroborate: $\rho = 0.144\text{--}0.168$ across all pairs, strengthening to $\rho = 0.27\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).
66	
67	The remaining ${\sim}$98\% of variance likely reflects entity frequency, prompt position effects \cite{lost-in-middle-2024}, mention ambiguity, and type definition quality. We frame pairwise SCS as one specific, actionable mechanism---semantic overlap between type labels is directly amenable to schema design---rather than the totality of degradation. Although pairwise $r^2$ is modest, the signal compounds at the batch level into gaps reaching 31.2\,pp under extreme-batch comparison ($-$25.5\,pp under v2 prompts; typical-batch gap ${\approx}\,2\text{--}4$\,pp, \S\ref{sec:practical_magnitude}).
68	
69	\subsection{BCS-Controlled Experiments}
70	\label{sec:bcs_controlled}
71	
72	We fix the type cou
…[truncated 275 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T09:36:23.308908+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": "128",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "offset": "128",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T09:36:23.309061+00:00_

128	For representative batches from the 80-relation pool ($n{=}100$ random 16-type subsets), the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI: [0.4, 4.0])---roughly 7\% of the 31.2\,pp extreme-batch gap. Quartile comparison confirms: bottom-quartile BCS batches average 82.8\% vs.\ 78.9\% for top-quartile ($\Delta = 3.9$\,pp). The 31.2\,pp figure reflects maximum BCS contrast, not the typical batch experience.
129	
130	\paragraph{Cross-model validation.}
131	The effect replicates on Meta-Llama-3.1-8B-Instruct: BCS gaps of $-$27.1\,pp (count 8) and $-$23.9\,pp (count 16), reaching 77--87\% of Qwen3-32B's gap. Both models converge to $\approx$51\% under high confusability regardless of count, while divergence is confined to the low-BCS regime---suggesting a task-inherent difficulty floor under high confusability (Table~\ref{tab:cross_model_bcs}).
132	
133	\paragraph{Prompt sensitivity.}
134	Under the v2 prompt (stricter format constraints), the extreme-batch BCS gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI: [22.4, 28.6]; $n{=}25$; $r = -0.919$; $p < 0.0001$). Compared to v1's $-$31.2\,pp, the effect attenuates modestly ($-$5.7\,pp) but remains highly significant. NER v2 yields consistent batch-level correlations ($r = +0.58$ vs.\ $r = +0.50$ under v1). Prompt design modulates the magnitude but does not eliminate the confusability effect (full analysis in Appendix~\ref{sec:appendix_prompt_sensitivity}).
135	
136	\subsection{Multi-Channel Degradation}
137	\label{sec:multi_channel}
138	
139	Error taxonomy decomposition (Table~\ref{tab:error_taxonomy} and Figure~\ref{fig:error_taxonomy} in Appendix~\ref{sec:appendix_figures}) shows intra-batch substitution (IntraSub) scales monotonically with BCS: $\rho = 1.0$ ($p < 0.001$) for NER and $\rho = 0.954$ ($p < 10^{-6}$) for RE. In RE, 100\% of confusion errors are intra-batch and missed-entity rates remain flat (10--16\%); in NER, missed rates are higher (43--65\%) and 
…[truncated 422 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T09:36:23.309200+00:00_

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
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T09:36:23.309333+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	The two-channel model applies cleanly to cross-domain schemas; same-domain schemas require pairwise SCS or centrality adjustment (\S\ref{sec:centrality_confound}). High-BCS accuracy converges to $\approx$51\% across tested models, suggesting a task-inherent difficulty ceiling. RE's clean channel separation may partly reflect its closed-set format; the effect generalizes to document-level RE (DocRED slope $-$0.71). Practitioners should monitor BCS and prefer cross-domain type groupings. Prompt design modulates but does not eliminate the effect (v2 gap: $-$25.5\,pp vs.\ v1: $-$31.2\,pp; Appendix~\ref{sec:appendix_prompt_sensitivity}).
6	
7	\paragraph{Future directions.}
8	For NER, merge amplification blocks naive decomposition (\S\ref{sec:sdgd}); calibration-aware merge, joint decoding, or coarse-to-fine extraction may address this. For RE, extending confusability-aware batching to broader benchmarks is a natural next step.
9	
10	\section{Conclusion}
11	\label{sec:conclusion}
12	
13	We isolated schema-induced degradation into count-driven recall decline and confusability-driven type confusion, showed these channels are separable in RE, with Channel~2 additionally impairing entity detection in NER, and confirmed that both channels replicate across model families on RE (Meta-Llama-3.1-8B-Instruct: count $r = 0.725$, confusability $\Delta = -27$\,pp) and across extraction granularities (DocRED document-level RE: count decline $-$49\,pp; BCS slope $= -0.71$, $R^2 = 0.53$), with high-BCS accuracy converging to a floor consistent across both tested models. We further identified a centrality confound on same-domain schemas, demonstrated that merge amplification is a structural challenge for NER decomposition, and showed that confusability-aware batch composition recovers +1.4\,pp on RE where span reconciliation is unnecessary. Cross-batch calibration or joint decoding for NER, and broader
…[truncated 64 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T09:36:23.309560+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "\\title{Does Type Confusability Drive Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}",
  "new_string": "\\title{Does Type Confusability Shape Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "old_string": "\\title{Does Type Confusability Drive Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}",
    "new_string": "\\title{Does Type Confusability Shape Schema-Induced Degradation\\\\in Training-Free LLM Information Extraction?}"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T09:36:23.309763+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T09:36:23.309934+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "old_string": "The $n{=}25$ v2 result confirms that the confusability effect is robust to prompt design: the gap narrows modestly ($-$5.7\\,pp) but remains highly significant ($p < 0.0001$, $r = -0.919$).",
  "new_string": "The $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.0001$, $r = -0.919$)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "old_string": "The $n{=}25$ v2 result confirms that the confusability effect is robust to prompt design: the gap narrows modestly ($-$5.7\\,pp) but remains highly significant ($p < 0.0001$, $r = -0.919$).",
    "new_string": "The $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.0001$, $r = -0.919$)."
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T09:36:23.310135+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T09:36:23.310266+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
  "content": "\\begin{abstract}\nTraining-free LLM information extraction degrades as schema complexity grows. We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.\n\nWe identify two degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\\approx}\\,2.2$\\,pp. Under extreme-batch construction maximizing BCS contrast, the gap reaches 31.2\\,pp. Batch-level BCS explains $R^2 = 0.22\\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\\text{--}1.7\\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. MAVEN generally suppresses extraction for cross-domain schemas; same-domain schemas exhibit centrality confounding. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\\,pp, $p\\approx 0.19$).\n\\end{abstract}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
    "content": "\\begin{abstract}\nTraining-free LLM information extraction degrades as schema complexity grows. We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.\n\nWe identify two degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\\approx}\\,2.2$\\,pp. Under extreme-batch construction maximizing BCS contrast, the gap reaches 31.2\\,pp. Batch-level BCS explains $R^2 = 0.22\\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\\text{--}1.7\\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. MAVEN generally suppresses extraction for cross-domain schemas; same-domain schemas exhibit centrality confounding. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\\,pp, $p\\approx 0.19$).\n\\end{abstract}\n"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T09:36:23.310425+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T09:36:23.310572+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "Our experiments yield five findings: (1)~degradation operates through two separable channels---count-driven recall decline (up to $-$49\\,pp) and confusability-driven type confusion; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are robust across schema sizes, granularities, and prompt designs (BCS slopes consistent across pools, $p = 0.60$; DocRED replication: slope $= -0.71$, $R^2 = 0.53$); (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.",
  "new_string": "Our experiments yield five findings: (1)~degradation operates through two separable channels---a confusability channel producing quartile gaps of $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]) on RE with typical-batch differences of ${\\approx}\\,2.2$\\,pp, and a count channel driving recall decline up to $-$49\\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "old_string": "Our experiments yield five findings: (1)~degradation operates through two separable channels---count-driven recall decline (up to $-$49\\,pp) and confusability-driven type confusion; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are robust across schema sizes, granularities, and prompt designs (BCS slopes consistent across pools, $p = 0.60$; DocRED replication: slope $= -0.71$, $R^2 = 0.53$); (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain.",
    "new_string": "Our experiments yield five findings: (1)~degradation operates through two separable channels---a confusability channel producing quartile gaps of $-$5.3\\,pp (95\\% CI: [$-$7.4, $-$3.2]) on RE with typical-batch differences of ${\\approx}\\,2.2$\\,pp, and a count channel driving recall decline up to $-$49\\,pp; (2)~pairwise SCS predicts type confusion ($r = 0.112$--$0.129$), the first factor empirically isolated in controlled zero-shot IE; (3)~effects are consistent across schema sizes and granularities (BCS slopes: $p = 0.60$; DocRED: slope $= -0.71$, $R^2 = 0.53$), and directionally consistent across prompt designs, with attenuated magnitude under improved prompts; (4)~per-type aggregation is confounded by centrality on homogeneous schemas; (5)~NER decomposition fails due to merge amplification, but RE batch composition yields a directional +1.4\\,pp gain."
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T09:36:23.310732+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T09:36:23.310878+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "    \\item \\textbf{Diagnosis to mitigation.} Merge amplification blocks NER decomposition; RE batch composition yields +1.4\\,pp via confusability-aware grouping (\\S\\ref{sec:sdgd}).",
  "new_string": "    \\item \\textbf{Diagnosis to mitigation.} A diagnosis of schema decomposition feasibility: oracle routing recovers count-based degradation in RE (+29.8\\,pp); confusability-aware grouping is inconclusive (+1.4\\,pp, $p\\approx 0.19$); NER decomposition fails due to merge amplification (\\S\\ref{sec:sdgd})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "old_string": "    \\item \\textbf{Diagnosis to mitigation.} Merge amplification blocks NER decomposition; RE batch composition yields +1.4\\,pp via confusability-aware grouping (\\S\\ref{sec:sdgd}).",
    "new_string": "    \\item \\textbf{Diagnosis to mitigation.} A diagnosis of schema decomposition feasibility: oracle routing recovers count-based degradation in RE (+29.8\\,pp); confusability-aware grouping is inconclusive (+1.4\\,pp, $p\\approx 0.19$); NER decomposition fails due to merge amplification (\\S\\ref{sec:sdgd})."
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T09:36:23.311052+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T09:36:23.311205+00:00_

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
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T09:36:23.311337+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction degrades as schema complexity grows. We conduct the first controlled study isolating type confusability from type count across NER, RE (a closed-set classification task), and event detection on four datasets, introducing the Schema Confusability Score (SCS) and two paradigms: count curves varying schema size while randomizing confusability, and BCS-controlled experiments fixing size while varying confusability.
3	
4	We identify two degradation channels: count-driven recall decline and confusability-driven type substitution. For RE, the quartile BCS gap is $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]); typical random batches differ by ${\approx}\,2.2$\,pp. Under extreme-batch construction maximizing BCS contrast, the gap reaches 31.2\,pp. Batch-level BCS explains $R^2 = 0.22\text{--}0.53$ of accuracy variance as an aggregated signal, while pairwise effect sizes remain modest ($r^2 = 1.3\text{--}1.7\%$). The effect is directionally consistent across prompt designs, with attenuated magnitude under improved prompts. Channel~1 replicates fully on Llama-3.1-8B; Channel~2 replicates on RE but shows floor effects on 8B NER. MAVEN generally suppresses extraction for cross-domain schemas; same-domain schemas exhibit centrality confounding. Schema decomposition via oracle routing recovers count-based degradation for RE (+29.8\,pp over single-pass), but confusability-aware grouping yields no significant additional gain (+1.4\,pp, $p\approx 0.19$).
5	\end{abstract}
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T09:36:23.311467+00:00_

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
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T09:36:23.311744+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this degradation? Prior decomposition strategies implicitly assume different answers: \citet{uniner-2024} extract each type independently; \citet{llm-pee-2025} partition schemas by type embedding similarity; \citet{parse-2025} optimize schema definitions. None isolates \emph{why} schemas degrade performance. The closest work, LLM-PEE, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor accounts for the gains. All prior approaches conflate two mechanisms: having more types to discriminate among (count) and having semantically similar types to confuse (confusability). Without disentangling these, decomposition strategies optimize a black-box objective without understanding its components.
7	
8	We ask three questions. \textbf{RQ1}: Does type confusabil
…[truncated 2905 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T09:36:23.312011+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "15",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "15",
    "limit": "3"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T09:36:23.312152+00:00_

15	
16	\title{Does Type Confusability Shape Schema-Induced Degradation\\in Training-Free LLM Information Extraction?}
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T09:36:23.312274+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/\\$[^$]*\\$//g; s/[{}()~,;:]/ /g; s/---/ /g; s/  */ /g' | wc -w",
  "description": "Count approximate word count of abstract"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/\\$[^$]*\\$//g; s/[{}()~,;:]/ /g; s/---/ /g; s/  */ /g' | wc -w",
    "description": "Count approximate word count of abstract"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T09:36:23.312395+00:00_

187

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T09:36:23.312533+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex | grep -v '\\\\begin{abstract}' | grep -v '\\\\end{abstract}' | sed 's/\\\\,/ /g; s/\\\\text{[^}]*}/X/g; s/\\$[^$]*\\$/NUM/g; s/\\\\[a-zA-Z]*//g; s/[{}~]/ /g; s/---/ /g; s/  */ /g' | wc -w",
  "description": "More accurate abstract word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex | grep -v '\\\\begin{abstract}' | grep -v '\\\\end{abstract}' | sed 's/\\\\,/ /g; s/\\\\text{[^}]*}/X/g; s/\\$[^$]*\\$/NUM/g; s/\\\\[a-zA-Z]*//g; s/[{}~]/ /g; s/---/ /g; s/  */ /g' | wc -w",
    "description": "More accurate abstract word count"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T09:36:23.312651+00:00_

189

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T09:36:23.312785+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\bDrive\\b",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\bDrive\\b",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T09:36:23.312926+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-16T09:36:23.313084+00:00_

All edits complete:

1. **Title**: "Drive" → "Shape" in `main.tex:16`
2. **Abstract**: Fully rewritten (~195 words). Leads with quartile Δ=-5.3pp and typical-batch 2.2pp; 31.2pp demoted to "under extreme-batch construction"; includes all required phrasings verbatim (cross-model, prompt robustness, MAVEN, decomposition, RE closed-set).
3. **Introduction**:
   - Finding (1) now leads with typical magnitudes (quartile -5.3pp, typical 2.2pp) before extreme -49pp count effect
   - Finding (3) changed from "robust across ... prompt designs" to "directionally consistent across prompt designs, with attenuated magnitude under improved prompts"
   - Contribution #4 rewritten with oracle routing +29.8pp, inconclusive grouping +1.4pp p≈0.19, merge amplification
   - RQ1 doesn't use "Drive" (already phrased differently), so no change needed there
4. **Prompt robustness (S12)**: `main.tex:245` updated from "robust to prompt design" to "directionally consistent across prompt designs, with attenuated magnitude"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_d044_framing_rewrite_20260516T093329"
}
```

</details>

---
