# paper section5 critical fix

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/chats/worker_paper_section5_critical_fix_20260516T075926.jsonl`
- **Structured JSON:** [`2b9491b7308b599903ec.json`](../../sessions/2b/2b9491b7308b599903ec.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

47 recorded events

### Tool call

_source line 1 · 2026-05-16T08:01:49.454049+00:00_

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
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T08:01:49.454427+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches, merging predictions via set union. Every decomposition mode---SDGD (F1\,=\,0.241), random batching (0.320), per-type (0.292)---falls below the single-pass baseline (0.445) on Few-NERD NER (Table~\ref{tab:sdgd_results}).
5	
6	\paragraph{Merge amplification as the bottleneck.}
7	The failure mechanism is \emph{merge amplification}: presenting the same text $k$ times with different type subsets causes each pass to independently generate entity predictions. Single-pass precision is 0.563; after union merge with 8 batches, precision drops to 0.210--0.249, while recall increases only modestly (0.368 $\to$ 0.314--0.446). The net effect is a precision collapse that overwhelms any recall gains. Confidence gating---retaining only the highest-confidence prediction per span---improves precision but at the cost of disproportionate recall loss, yielding lower F1 in both modes (Appendix~\ref{sec:appendix_sdgd}). The fundamental issue is that LLM predictions are not calibrated across passes \cite{llm-calibration-survey-2024}, and no merge strategy we tested can compensate.
8	
9	\paragraph{Why NER fails but RE does not.}
10	Merge amplification is specific to span-level tasks where overlapping predictions from multiple passes require reconciliation. In NER, each pass independently proposes entity spans; union merge must resolve conflicting span boundaries and type assignments, and this reconciliation degrades systematically with the number of passes. RE classification, by contrast, operates on fixed (head, tail) pairs: given a pre-identified entity pair, the model selects one relation from the candidate set. No span reconciliation is requir
…[truncated 1586 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T08:01:49.454622+00:00_

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
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T08:01:49.454784+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level). Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and four datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall in NER and RE, but reverses direction in MAVEN (168 event types) due to centrality confounds in same-domain schemas as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE (a closed-set classification task); in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes and prompt designs: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.60$), with the quartile gap reaching $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]), though pairwise effect sizes are modest ($r^2 = 1.3\text{--}1.7\%$) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability
…[truncated 342 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T08:01:49.455021+00:00_

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
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T08:01:49.455197+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training-free LLM information extraction---prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning---enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, making it attractive for applications where annotation is expensive or schemas evolve frequently \cite{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to 0.42 with 64 types, a 42\% relative decline. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level)---near or exceeding halving. This degradation is not academic: real-world ontologies routinely define 50--200+ types, placing them squarely in the regime where training-free extraction becomes unreliable.
5	
6	What causes this schema-induced degradation? Prior work has proposed decomposition strategies that implicitly assume different answers. \citet{uniner-2024} extract each type independently, assuming types can be treated as separable. \citet{llm-pee-2025} partition large event schemas by type embedding similarity before extraction, assuming that semantic overlap between co-presented types drives errors. \citet{parse-2025} rewrite and optimize schema definitions, assuming that description quality is the bottleneck. Each approach improves extraction under certain conditions, but none isolates \emph{why} schemas degrade performance in the first place. The closest work, LLM-PEE \cite{llm-pee-2025}, reduces both the number of co-presented types and their inter-type similarity simultaneously, making it impossible to determine which factor---or what combina
…[truncated 4270 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T08:01:49.455365+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
  "old_string": "\\caption{Confusability-aware batch composition on FewRel 80-rel RE. Graph coloring minimizes intra-batch BCS, yielding +1.4\\,pp over random assignment ($p < 0.05$, 15-seed bootstrap). Single-pass with all 80 types suffers severe schema overload.}",
  "new_string": "\\caption{Confusability-aware batch composition on FewRel 80-rel RE. Graph coloring minimizes intra-batch BCS, yielding +1.4\\,pp over random assignment, though the difference is not statistically significant given the single graph-coloring configuration ($n{=}1$) and narrow BCS margin (0.006). Single-pass with all 80 types suffers severe schema overload.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
    "old_string": "\\caption{Confusability-aware batch composition on FewRel 80-rel RE. Graph coloring minimizes intra-batch BCS, yielding +1.4\\,pp over random assignment ($p < 0.05$, 15-seed bootstrap). Single-pass with all 80 types suffers severe schema overload.}",
    "new_string": "\\caption{Confusability-aware batch composition on FewRel 80-rel RE. Graph coloring minimizes intra-batch BCS, yielding +1.4\\,pp over random assignment, though the difference is not statistically significant given the single graph-coloring configuration ($n{=}1$) and narrow BCS margin (0.006). Single-pass with all 80 types suffers severe schema overload.}"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T08:01:49.455517+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T08:01:49.455644+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
  "old_string": "The confusability-aware strategy achieves 0.802 accuracy, outperforming random batching (0.788 $\\pm$ 0.018) by +1.4 percentage points and exceeding the 95\\% CI upper bound of the random baseline (0.797). This result demonstrates that confusability findings translate directly into a practical batching recommendation for RE tasks.",
  "new_string": "The confusability-aware strategy achieves 0.802 accuracy compared to random batching (0.788 $\\pm$ 0.018). Although the +1.4\\,pp gain is directionally consistent with the confusability hypothesis, it does not reach statistical significance (rank 13/15 among random seeds, one-sided $p \\approx 0.19$); the narrow BCS margin between conditions (0.006) limits the achievable separation at this partition granularity. This suggests that confusability-aware grouping warrants further investigation at finer partition granularity."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
    "old_string": "The confusability-aware strategy achieves 0.802 accuracy, outperforming random batching (0.788 $\\pm$ 0.018) by +1.4 percentage points and exceeding the 95\\% CI upper bound of the random baseline (0.797). This result demonstrates that confusability findings translate directly into a practical batching recommendation for RE tasks.",
    "new_string": "The confusability-aware strategy achieves 0.802 accuracy compared to random batching (0.788 $\\pm$ 0.018). Although the +1.4\\,pp gain is directionally consistent with the confusability hypothesis, it does not reach statistical significance (rank 13/15 among random seeds, one-sided $p \\approx 0.19$); the narrow BCS margin between conditions (0.006) limits the achievable separation at this partition granularity. This suggests that confusability-aware grouping warrants further investigation at finer partition granularity."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T08:01:49.455788+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T08:01:49.455971+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
  "old_string": "RE classification, by contrast, operates on fixed (head, tail) pairs: given a pre-identified entity pair, the model selects one relation from the candidate set. No span reconciliation is required---each pair receives an independent classification that does not interact with predictions from other passes---eliminating the mechanism that caused SDGD to fail.",
  "new_string": "RE classification, by contrast, operates on fixed (head, tail) pairs with no span reconciliation, assuming an oracle or learned router that assigns each instance to the batch containing its gold type. Each pair receives an independent classification that does not interact with predictions from other passes, eliminating the mechanism that caused SDGD to fail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
    "old_string": "RE classification, by contrast, operates on fixed (head, tail) pairs: given a pre-identified entity pair, the model selects one relation from the candidate set. No span reconciliation is required---each pair receives an independent classification that does not interact with predictions from other passes---eliminating the mechanism that caused SDGD to fail.",
    "new_string": "RE classification, by contrast, operates on fixed (head, tail) pairs with no span reconciliation, assuming an oracle or learned router that assigns each instance to the batch containing its gold type. Each pair receives an independent classification that does not interact with predictions from other passes, eliminating the mechanism that caused SDGD to fail."
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T08:01:49.456127+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T08:01:49.456267+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
  "old_string": "but succeeds for RE, where confusability-aware batch composition recovers +1.4\\,pp accuracy over random batching ($p < 0.05$), demonstrating a practical application of our diagnostic framework.",
  "new_string": "but succeeds for RE, where confusability-aware batch composition recovers +1.4\\,pp accuracy over random batching, demonstrating a directionally consistent application of our diagnostic framework."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
    "old_string": "but succeeds for RE, where confusability-aware batch composition recovers +1.4\\,pp accuracy over random batching ($p < 0.05$), demonstrating a practical application of our diagnostic framework.",
    "new_string": "but succeeds for RE, where confusability-aware batch composition recovers +1.4\\,pp accuracy over random batching, demonstrating a directionally consistent application of our diagnostic framework."
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T08:01:49.456414+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T08:01:49.456556+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "\\item \\textbf{From diagnosis to mitigation.} Our SDGD experiments identify merge amplification as a structural challenge for NER decomposition, and show that for RE---where fixed entity pairs eliminate span reconciliation---confusability-aware batch composition recovers +1.4\\,pp accuracy over random batching (\\S\\ref{sec:sdgd}).",
  "new_string": "\\item \\textbf{From diagnosis to mitigation.} Our SDGD experiments identify merge amplification as a structural challenge for NER decomposition, and show that for RE---where fixed entity pairs eliminate span reconciliation---a confusability-aware batching strategy yields directional improvement (+1.4\\,pp) over random batching, suggesting practical utility of confusability diagnostics (\\S\\ref{sec:sdgd})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "old_string": "\\item \\textbf{From diagnosis to mitigation.} Our SDGD experiments identify merge amplification as a structural challenge for NER decomposition, and show that for RE---where fixed entity pairs eliminate span reconciliation---confusability-aware batch composition recovers +1.4\\,pp accuracy over random batching (\\S\\ref{sec:sdgd}).",
    "new_string": "\\item \\textbf{From diagnosis to mitigation.} Our SDGD experiments identify merge amplification as a structural challenge for NER decomposition, and show that for RE---where fixed entity pairs eliminate span reconciliation---a confusability-aware batching strategy yields directional improvement (+1.4\\,pp) over random batching, suggesting practical utility of confusability diagnostics (\\S\\ref{sec:sdgd})."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T08:01:49.456707+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T08:01:49.456858+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "but confusability-aware RE batch composition recovers +1.4\\,pp over random batching, demonstrating task-dependent applicability of the diagnostic framework.",
  "new_string": "but confusability-aware RE batch composition yields a directional +1.4\\,pp gain over random batching ($p \\approx 0.19$, not significant), suggesting task-dependent applicability of the diagnostic framework."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "old_string": "but confusability-aware RE batch composition recovers +1.4\\,pp over random batching, demonstrating task-dependent applicability of the diagnostic framework.",
    "new_string": "but confusability-aware RE batch composition yields a directional +1.4\\,pp gain over random batching ($p \\approx 0.19$, not significant), suggesting task-dependent applicability of the diagnostic framework."
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T08:01:49.457016+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T08:01:49.457148+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "significant.*batch|batch.*significant|p\\s*<\\s*0\\.05.*batch|batch.*p\\s*<\\s*0\\.05",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Grep",
  "tool_args": {
    "pattern": "significant.*batch|batch.*significant|p\\s*<\\s*0\\.05.*batch|batch.*p\\s*<\\s*0\\.05",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T08:01:49.457274+00:00_

docs/paper/main.tex:224:[Omitted long matching line]
docs/paper/main.tex:256:[Omitted long matching line]
docs/paper/main.aux:907:\@writefile{lot}{\contentsline {table}{\numberline {5}{\ignorespaces Confusability-aware batch composition on FewRel 80-rel RE. Graph coloring minimizes intra-batch BCS, yielding +1.4\,pp over random assignment ($p < 0.05$, 15-seed bootstrap). Single-pass with all 80 types suffers severe schema overload.}}{9}{table.caption.31}\protected@file@percent }
docs/paper/main.aux:908:\newlabel{tab:batch_composition}{{5}{9}{Confusability-aware batch composition on FewRel 80-rel RE. Graph coloring minimizes intra-batch BCS, yielding +1.4\,pp over random assignment ($p < 0.05$, 15-seed bootstrap). Single-pass with all 80 types suffers severe schema overload}{table.caption.31}{}}
docs/paper/sdgd_negative.tex:27:\caption{Confusability-aware batch composition on FewRel 80-rel RE. Graph coloring minimizes intra-batch BCS, yielding +1.4\,pp over random assignment, though the difference is not statistically significant given the single graph-coloring configuration ($n{=}1$) and narrow BCS margin (0.006). Single-pass with all 80 types suffers severe schema overload.}
docs/paper/introduction.tex:12:[Omitted long matching line]
docs/paper/abstract.tex:2:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T08:01:49.457405+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "translates directly|practical recommendation",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Grep",
  "tool_args": {
    "pattern": "translates directly|practical recommendation",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T08:01:49.457520+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T08:01:49.457643+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": "220",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
    "offset": "220",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T08:01:49.457790+00:00_

220	
221	We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
222	
223	\paragraph{RE (FewRel).}
224	Under the v1 prompt, the extreme-batch BCS gap is $-$31.2\,pp (low-BCS 82.3\% vs.\ high-BCS 51.0\%; Table~\ref{tab:bcs_controlled}). Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI: [22.4, 28.6]; $p < 0.0001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\,pp (CI: [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal---a cautionary note for small-sample prompt sensitivity studies.
225	
226	\paragraph{NER (Few-NERD).}
227	The batch-level BCS--F1 correlation under v2 is consistent with v1: at count${}\,=\,12$, $r = +0.58$ ($p = 0.002$, 95\% CI: [0.19, 0.81]) vs.\ v1 $r = +0.50$ ($p = 0.008$). As discussed in \S\ref{sec:pairwise}, this positive direction reflects a type-frequency confound at the batch level---high-BCS batches contain high-frequency entity types that models extract more reliably---rather than evidence against the confusability hypothesis. The pairwise SCS--confusion analysis (\S\ref{sec:pairwise}), which is immune to this aggregation artifact, remains the primary evidence for the NER confusability channel.
228	
229	\paragraph{Interpretation.}
230	The $n{=}25$ v2 result confirms that the confusability effect is robust to prompt design: the gap narrows modestly ($-$5.7\,pp) but remains highly significant ($p < 0.0001$, $r = -0.919$). The earl
…[truncated 2778 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T08:01:49.458274+00:00_

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
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T08:01:49.458434+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level). Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and four datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that suppresses recall in NER and RE, but reverses direction in MAVEN (168 event types) due to centrality confounds in same-domain schemas as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE (a closed-set classification task); in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes and prompt designs: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.60$), with the quartile gap reaching $-$5.3\,pp (95\% CI: [$-$7.4, $-$3.2]), though pairwise effect sizes are modest ($r^2 = 1.3\text{--}1.7\%$) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant. Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability
…[truncated 344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T08:01:49.458581+00:00_

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
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T08:01:49.458894+00:00_

1	\section{Schema Decomposition: Failure, Diagnosis, and Mitigation}
2	\label{sec:sdgd}
3	
4	A natural intervention is to partition the schema so confusable types never co-occur. We test this with \textbf{Schema-DAG-Guided Decomposition} (SDGD), which uses greedy graph coloring on the pairwise SCS graph to assign types to low-confusability batches, merging predictions via set union. Every decomposition mode---SDGD (F1\,=\,0.241), random batching (0.320), per-type (0.292)---falls below the single-pass baseline (0.445) on Few-NERD NER (Table~\ref{tab:sdgd_results}).
5	
6	\paragraph{Merge amplification as the bottleneck.}
7	The failure mechanism is \emph{merge amplification}: presenting the same text $k$ times with different type subsets causes each pass to independently generate entity predictions. Single-pass precision is 0.563; after union merge with 8 batches, precision drops to 0.210--0.249, while recall increases only modestly (0.368 $\to$ 0.314--0.446). The net effect is a precision collapse that overwhelms any recall gains. Confidence gating---retaining only the highest-confidence prediction per span---improves precision but at the cost of disproportionate recall loss, yielding lower F1 in both modes (Appendix~\ref{sec:appendix_sdgd}). The fundamental issue is that LLM predictions are not calibrated across passes \cite{llm-calibration-survey-2024}, and no merge strategy we tested can compensate.
8	
9	\paragraph{Why NER fails but RE does not.}
10	Merge amplification is specific to span-level tasks where overlapping predictions from multiple passes require reconciliation. In NER, each pass independently proposes entity spans; union merge must resolve conflicting span boundaries and type assignments, and this reconciliation degrades systematically with the number of passes. RE classification, by contrast, operates on fixed (head, tail) pairs with no span reconciliation, assuming an oracle or learned router that assigns each instance to the batch containing its gol
…[truncated 1891 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T08:01:49.459299+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && pdflatex -interaction=nonstopmode main 2>&1 | tail -20",
  "description": "First pdflatex pass",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && pdflatex -interaction=nonstopmode main 2>&1 | tail -20",
    "description": "First pdflatex pass",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T08:01:49.459457+00:00_

s/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (19 pages, 420959 bytes).
Transcript written on main.log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T08:01:49.459586+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && bibtex main 2>&1 | tail -5",
  "description": "Run bibtex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && bibtex main 2>&1 | tail -5",
    "description": "Run bibtex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T08:01:49.459702+00:00_

This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T08:01:49.459815+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && pdflatex -interaction=nonstopmode main 2>&1 | grep -E \"Warning.*undefined|Error|Output written\" | head -10",
  "description": "Second pdflatex pass checking for issues"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && pdflatex -interaction=nonstopmode main 2>&1 | grep -E \"Warning.*undefined|Error|Output written\" | head -10",
    "description": "Second pdflatex pass checking for issues"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T08:01:49.460056+00:00_

Output written on main.pdf (19 pages, 420702 bytes).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T08:01:49.460195+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && pdflatex -interaction=nonstopmode main 2>&1 | grep -E \"Warning.*undefined|Error|Output written|pages\" | head -10",
  "description": "Final pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && pdflatex -interaction=nonstopmode main 2>&1 | grep -E \"Warning.*undefined|Error|Output written|pages\" | head -10",
    "description": "Final pdflatex pass"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T08:01:49.460467+00:00_

Output written on main.pdf (19 pages, 420702 bytes).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T08:01:49.460606+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -n \"\\\\\\\\clearpage\\|\\\\\\\\newpage\\|appendix\\|\\\\\\\\section.*Appendix\\|\\\\\\\\appendix\" main.tex | head -5",
  "description": "Find where appendix starts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -n \"\\\\\\\\clearpage\\|\\\\\\\\newpage\\|appendix\\|\\\\\\\\section.*Appendix\\|\\\\\\\\appendix\" main.tex | head -5",
    "description": "Find where appendix starts"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T08:01:49.460733+00:00_

45:\item \textbf{Non-significant factorial test.} A within-dataset factorial analysis (count $\times$ BCS) on Few-NERD did not reach significance (Appendix~\ref{sec:appendix_factorial}). The cross-pool slope consistency suggests that confusability sensitivity is stable rather than amplifying with schema size; larger pools simply expose more of the BCS spectrum.
64:\appendix
67:\label{sec:appendix_figures}
133:\label{sec:appendix_sdgd}
166:\label{sec:appendix_factorial}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T08:01:49.460869+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -c \"\\\\\\\\newpage\" main.log 2>/dev/null; grep \"page.*shipout\\|Output written\" main.log | tail -3",
  "description": "Check page info from log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -c \"\\\\\\\\newpage\" main.log 2>/dev/null; grep \"page.*shipout\\|Output written\" main.log | tail -3",
    "description": "Check page info from log"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T08:01:49.460991+00:00_

0
Output written on main.pdf (19 pages, 420702 bytes).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T08:01:49.461124+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -A2 \"\\\\\\\\newlabel{sec:appendix_figures}\" main.aux",
  "description": "Check appendix page number from aux"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep -A2 \"\\\\\\\\newlabel{sec:appendix_figures}\" main.aux",
    "description": "Check appendix page number from aux"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T08:01:49.461400+00:00_

\newlabel{sec:appendix_figures}{{A}{15}{Additional Figures}{appendix.A}{}}
\@writefile{lot}{\contentsline {table}{\numberline {6}{\ignorespaces Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S  \ref {sec:model}) for fair cross-model comparison; the count-curve results in \S  \ref {sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}}{15}{table.caption.42}\protected@file@percent }
\newlabel{tab:cross_model}{{6}{15}{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S \ref {sec:model}) for fair cross-model comparison; the count-curve results in \S \ref {sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1}{table.caption.42}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T08:01:49.461575+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep \"newlabel{sec:sdgd\\|newlabel{sec:conclusion\\|newlabel{sec:bcs_agg\\|newlabel{sec:appendix_bcs\" main.aux",
  "description": "Find body section page numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep \"newlabel{sec:sdgd\\|newlabel{sec:conclusion\\|newlabel{sec:bcs_agg\\|newlabel{sec:appendix_bcs\" main.aux",
    "description": "Find body section page numbers"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T08:01:49.461697+00:00_

\newlabel{sec:sdgd}{{5}{9}{Schema Decomposition: Failure, Diagnosis, and Mitigation}{section.5}{}}
\newlabel{sec:conclusion}{{7}{10}{Conclusion}{section.7}{}}
\newlabel{sec:appendix_bcs_sensitivity}{{H}{18}{BCS Aggregation Sensitivity}{appendix.H}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T08:01:49.461830+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep \"newlabel{sec:\" main.aux | grep -v appendix",
  "description": "Check all body section page numbers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/ && grep \"newlabel{sec:\" main.aux | grep -v appendix",
    "description": "Check all body section page numbers"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T08:01:49.462004+00:00_

\newlabel{sec:introduction}{{1}{1}{Introduction}{section.1}{}}
\newlabel{sec:related_work}{{2}{3}{Related Work}{section.2}{}}
\newlabel{sec:rw_training_free}{{2.1}{3}{Training-Free LLM Information Extraction}{subsection.2.1}{}}
\newlabel{sec:rw_schema}{{2.2}{3}{Schema Complexity in IE}{subsection.2.2}{}}
\newlabel{sec:rw_anisotropy}{{2.3}{3}{Representation Degeneration and Embedding Anisotropy}{subsection.2.3}{}}
\newlabel{sec:experimental_setup}{{3}{3}{Experimental Setup}{section.3}{}}
\newlabel{sec:datasets}{{3.1}{3}{Tasks and Datasets}{subsection.3.1}{}}
\newlabel{sec:scs}{{3.2}{4}{Schema Confusability Score (SCS)}{subsection.3.2}{}}
\newlabel{sec:exp_design}{{3.3}{4}{Experimental Design}{subsection.3.3}{}}
\newlabel{sec:metrics}{{3.4}{5}{Evaluation Metrics}{subsection.3.4}{}}
\newlabel{sec:model}{{3.5}{5}{Model and Inference}{subsection.3.5}{}}
\newlabel{sec:results}{{4}{5}{Results}{section.4}{}}
\newlabel{sec:count_curves}{{4.1}{5}{Count-Degradation Curves}{subsection.4.1}{}}
\newlabel{sec:pairwise}{{4.2}{6}{Pairwise Confusability and Type Confusion}{subsection.4.2}{}}
\newlabel{sec:bcs_controlled}{{4.3}{7}{BCS-Controlled Experiments}{subsection.4.3}{}}
\newlabel{sec:within_pool}{{4.3}{7}{Within-pool controlled comparison}{section*.23}{}}
\newlabel{sec:practical_magnitude}{{4.3}{8}{Practical magnitude}{section*.25}{}}
\newlabel{sec:multi_channel}{{4.4}{8}{Multi-Channel Degradation}{subsection.4.4}{}}
\newlabel{sec:centrality_confound}{{4.5}{9}{Centrality Confound on Homogeneous Schemas}{subsection.4.5}{}}
\newlabel{sec:sdgd}{{5}{9}{Schema Decomposition: Failure, Diagnosis, and Mitigation}{section.5}{}}
\newlabel{sec:discussion}{{6}{10}{Discussion}{section.6}{}}
\newlabel{sec:conclusion}{{7}{10}{Conclusion}{section.7}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_section5_critical_fix_20260516T075926",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-16T08:01:49.462195+00:00_

Body sections end on page 10 (Conclusion). The task says ≤8 pages body — this is already 10 pages, but that's a pre-existing issue unrelated to my edits (my changes only replaced text without adding significant length). The task was to fix the statistical errors, not restructure for page count.

All corrections complete. Here's the summary of changes:

---

## Changes Made

### `sdgd_negative.tex` (3 edits)

**1. Table caption (line 27)** — removed false `p < 0.05` claim:
```diff
-\caption{...yielding +1.4\,pp over random assignment ($p < 0.05$, 15-seed bootstrap). Single-pass...}
+\caption{...yielding +1.4\,pp over random assignment, though the difference is not statistically significant given the single graph-coloring configuration ($n{=}1$) and narrow BCS margin (0.006). Single-pass...}
```

**2. Body paragraph (line 31)** — removed "exceeding 95% CI" overclaim:
```diff
-The confusability-aware strategy achieves 0.802 accuracy, outperforming random batching (0.788 $\pm$ 0.018) by +1.4 percentage points and exceeding the 95\% CI upper bound of the random baseline (0.797). This result demonstrates that confusability findings translate directly into a practical batching recommendation for RE tasks.
+The confusability-aware strategy achieves 0.802 accuracy compared to random batching (0.788 $\pm$ 0.018). Although the +1.4\,pp gain is directionally consistent with the confusability hypothesis, it does not reach statistical significance (rank 13/15 among random seeds, one-sided $p \approx 0.19$); the narrow BCS margin between conditions (0.006) limits the achievable separation at this partition granularity. This suggests that confusability-aware grouping warrants further investigation at finer partition granularity.
```

**3. "Why NER fails" paragraph (line 10)** — added oracle routing caveat:
```diff
-RE classification, by contrast, operates on fixed (head, tail) pairs: given a pre-identified entity pair, the model selects one relation from the candidate set. No span reconciliation is required---each pair receives an independent classification that does not interact with predictions from other passes---eliminating the mechanism that caused SDGD to fail.
+RE classification, by contrast, operates on fixed (head, tail) pairs with no span reconciliation, assuming an oracle or learned router that assigns each instance to the batch containing its gold type. Each pair receives an independent classification that does not interact with predictions from other passes, eliminating the mechanism that caused SDGD to fail.
```

### `abstract.tex` (1 edit)

```diff
-...recovers +1.4\,pp accuracy over random batching ($p < 0.05$), demonstrating a practical application of our diagnostic framework.
+...recovers +1.4\,pp accuracy over random batching, demonstrating a directionally consistent application of our diagnostic framework.
```

### `introduction.tex` (2 edits)

**Finding (5):**
```diff
-but confusability-aware RE batch composition recovers +1.4\,pp over random batching, demonstrating task-dependent applicability
+but confusability-aware RE batch composition yields a directional +1.4\,pp gain over random batching ($p \approx 0.19$, not significant), suggesting task-dependent applicability
```

**Contribution item 4:**
```diff
-confusability-aware batch composition recovers +1.4\,pp accuracy over random batching (\S\ref{sec:sdgd}).
+a confusability-aware batching strategy yields directional improvement (+1.4\,pp) over random batching, suggesting practical utility of confusability diagnostics (\S\ref{sec:sdgd}).
```

---

Compilation: clean, no undefined references or errors. Note: body is 10 pages (pre-existing; not caused by these edits).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_section5_critical_fix_20260516T075926"
}
```

</details>

---
