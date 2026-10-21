# write d037 stats integration

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 77
- **Recorded user turns:** 0
- **Tool calls:** 38
- **Original source:** `logs/chats/worker_write_d037_stats_integration_20260516T034255.jsonl`
- **Structured JSON:** [`b2d5d24d2c0ed8d20766.json`](../../sessions/b2/b2d5d24d2c0ed8d20766.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

77 recorded events

### Tool call

_source line 1 · 2026-05-16T03:47:46.406464+00:00_

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
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T03:47:46.407208+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	\subsection{Count-Degradation Curves}
5	\label{sec:count_curves}
6	
7	\begin{figure}[t]
8	\centering
9	\begin{minipage}[t]{0.48\columnwidth}
10	\centering
11	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
12	\end{minipage}
13	\hfill
14	\begin{minipage}[t]{0.48\columnwidth}
15	\centering
16	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
17	\end{minipage}
18	\caption{\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}
19	\label{fig:main_results}
20	\end{figure}
21	
22	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\ref{fig:main_results}a).
23	
24	\paragraph{NER (Few-NERD).}
25	Recall generally declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$, a 42\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\,=\,22$ to 0.55 at count${}\,=\,44$; 95\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.
26	
27	\paragraph{RE (FewRel).}
28	Accuracy drops monotonically from 85.7\% at count${}\,=\,1$ through 58.8\% at count${}\,=\,40$ to 50.4\% at count${}\,=\,80$, a
…[truncated 14103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T03:47:46.407500+00:00_

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
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T03:47:46.407717+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that generally suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE; in NER, confusability additionally impairs entity detection (same-domain schemas are subject to a centrality confound). The BCS--accuracy relationship is robust across schema sizes: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.44$), while the wider BCS range at 80 types produces larger absolute accuracy gaps (31.2 vs.\ 9.1\,pp). Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a model-invariant floor. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural challenge for union-based merge pipelines in zero-shot IE.
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T03:47:46.408120+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability",
  "new_string": "0.522 at count${}\\,=\\,22$ to 0.549 at count${}\\,=\\,44$; bootstrap 95\\% CIs overlap: [0.487, 0.562] vs.\\ [0.521, 0.570], indicating this reversal is within sampling variability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability",
    "new_string": "0.522 at count${}\\,=\\,22$ to 0.549 at count${}\\,=\\,44$; bootstrap 95\\% CIs overlap: [0.487, 0.562] vs.\\ [0.521, 0.570], indicating this reversal is within sampling variability"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T03:47:46.408329+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T03:47:46.408512+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "accuracy gaps reaching 31.2\\,pp (\\S\\ref{sec:bcs_controlled})",
  "new_string": "accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled})"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "accuracy gaps reaching 31.2\\,pp (\\S\\ref{sec:bcs_controlled})",
    "new_string": "accuracy gaps reaching 31.2\\,pp under extreme-batch comparison (\\S\\ref{sec:bcs_controlled})"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T03:47:46.408690+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T03:47:46.411957+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.",
  "new_string": "The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.44$; Table~\\ref{tab:within_pool}). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations. The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.",
    "new_string": "The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.44$; Table~\\ref{tab:within_pool}). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T03:47:46.412247+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T03:47:46.412440+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "At the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7]).",
  "new_string": "At the 16-relation scale, the extreme-batch gap is 9.1\\,pp (single batch per level; Table~\\ref{tab:bcs_controlled}); the quartile gap from the within-pool analysis is $-$7.42\\,pp (CI: [$-$9.40, $-$5.54]; Table~\\ref{tab:within_pool}). At 80 relations, the extreme-batch gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7])."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "At the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points. At 80 relations, the gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7]).",
    "new_string": "At the 16-relation scale, the extreme-batch gap is 9.1\\,pp (single batch per level; Table~\\ref{tab:bcs_controlled}); the quartile gap from the within-pool analysis is $-$7.42\\,pp (CI: [$-$9.40, $-$5.54]; Table~\\ref{tab:within_pool}). At 80 relations, the extreme-batch gap reaches 31.2\\,pp (95\\% CI: [17.7, 42.7])."
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T03:47:46.412637+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T03:47:46.412830+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "the 80-relation pool's larger absolute gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity.",
  "new_string": "the 80-relation pool's larger extreme-batch gap (31.2\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (quartile gaps: $-$3.92\\,pp vs.\\ $-$7.42\\,pp; Table~\\ref{tab:within_pool})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "the 80-relation pool's larger absolute gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity.",
    "new_string": "the 80-relation pool's larger extreme-batch gap (31.2\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (quartile gaps: $-$3.92\\,pp vs.\\ $-$7.42\\,pp; Table~\\ref{tab:within_pool})."
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T03:47:46.413041+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T03:47:46.413214+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "high-BCS accuracy is model-invariant: both models converge",
  "new_string": "high-BCS accuracy is consistent across tested models (Qwen3-32B and Llama-3.1-8B): both models converge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "high-BCS accuracy is model-invariant: both models converge",
    "new_string": "high-BCS accuracy is consistent across tested models (Qwen3-32B and Llama-3.1-8B): both models converge"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T03:47:46.413386+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T03:47:46.413555+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp",
  "new_string": "reaching 77--87\\% of Qwen3-32B's extreme-batch gap ($-$31.2\\,pp)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "reaching 77--87\\% of Qwen3-32B's $-$31.2\\,pp",
    "new_string": "reaching 77--87\\% of Qwen3-32B's extreme-batch gap ($-$31.2\\,pp)"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T03:47:46.413725+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T03:47:46.415991+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "a task-inherent difficulty floor independent of model scale.",
  "new_string": "a task-inherent difficulty floor consistent across the tested models."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "a task-inherent difficulty floor independent of model scale.",
    "new_string": "a task-inherent difficulty floor consistent across the tested models."
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T03:47:46.416251+00:00_

&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T03:47:46.416465+00:00_

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
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T03:47:46.416645+00:00_

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
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-16T03:47:46.416835+00:00_

File unchanged since last read. The content from the earlier Read tool_result in this conversation is still current — refer to that instead of re-reading.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T03:47:46.417234+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	Unless otherwise noted, all experiments in this section use the v1 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\begin{figure}[t]
10	\centering
11	\begin{minipage}[t]{0.48\columnwidth}
12	\centering
13	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
14	\end{minipage}
15	\hfill
16	\begin{minipage}[t]{0.48\columnwidth}
17	\centering
18	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
19	\end{minipage}
20	\caption{\textbf{(a)} Count-degradation curves across three IE tasks. NER recall generally declines and RE accuracy declines monotonically with schema size; MAVEN relaxed F1 increases (\S\ref{sec:centrality_confound}). \textbf{(b)} BCS-controlled FewRel accuracy. The BCS--accuracy slope is consistent across the independent 16-relation pool and within-pool 16-relation subsets (permutation $p = 0.44$); the wider BCS range available at 80 relations produces larger absolute gaps.}
21	\label{fig:main_results}
22	\end{figure}
23	
24	We first examine how extraction performance changes as the number of types in the prompt schema increases (Experiment~1; Figure~\ref{fig:main_results}a).
25	
26	\paragraph{NER (Few-NERD).}
27	Recall generally declines from 0.72 at count${}\,=\,1$ to 0.42 at count${}\,=\,64$, a 42\% relative drop, with minor non-monotonicity at intermediate counts (e.g., 0.52 at count${}\,=\,22$ to 0.55 at count${}\,=\,44$; 95\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability). Precision moves in the opposite direction, rising from 0.11 to 0.52, reflecting a shift from over-prediction to under-prediction as more candidate types compete in the prompt. F1 exhibits an inverted-U shape, peaking at intermediate counts where the precision--recall trade-off is most balanced.
28	
2
…[truncated 14622 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T03:47:46.417533+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability",
  "new_string": "0.522 at count${}\\,=\\,22$ to 0.549 at count${}\\,=\\,44$; bootstrap 95\\% CIs overlap: [0.487, 0.562] vs.\\ [0.521, 0.570], indicating this reversal is within sampling variability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "0.52 at count${}\\,=\\,22$ to 0.55 at count${}\\,=\\,44$; 95\\% CIs [0.487, 0.562] and [0.521, 0.570] overlap, permutation $p = 0.31$, indicating this reversal is within sampling variability",
    "new_string": "0.522 at count${}\\,=\\,22$ to 0.549 at count${}\\,=\\,44$; bootstrap 95\\% CIs overlap: [0.487, 0.562] vs.\\ [0.521, 0.570], indicating this reversal is within sampling variability"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T03:47:46.419626+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T03:47:46.419926+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations (extreme-batch comparison; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).",
  "new_string": "The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.44$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "The confusability gap widens from 9.1\\,pp at 16 relations to 31.2\\,pp at 80 relations (extreme-batch comparison; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).",
    "new_string": "The 80-relation extreme-batch gap (31.2\\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.44$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes)."
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T03:47:46.420251+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T03:47:46.420444+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "At the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points.",
  "new_string": "At the 16-relation scale, the extreme-batch gap is 9.1\\,pp (single batch per level; Table~\\ref{tab:bcs_controlled}); the quartile gap from the within-pool analysis is $-$7.42\\,pp (CI: [$-$9.40, $-$5.54]; Table~\\ref{tab:within_pool})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "At the 16-relation scale, switching from low-BCS to high-BCS batches reduces accuracy by 9.1 percentage points.",
    "new_string": "At the 16-relation scale, the extreme-batch gap is 9.1\\,pp (single batch per level; Table~\\ref{tab:bcs_controlled}); the quartile gap from the within-pool analysis is $-$7.42\\,pp (CI: [$-$9.40, $-$5.54]; Table~\\ref{tab:within_pool})."
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T03:47:46.420721+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T03:47:46.420946+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "the 80-relation pool's larger extreme-batch gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).",
  "new_string": "the 80-relation pool's larger extreme-batch gap (31.2\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (quartile gaps: $-$3.92\\,pp vs.\\ $-$7.42\\,pp; Table~\\ref{tab:within_pool})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "the 80-relation pool's larger extreme-batch gap (31.2\\,pp vs.\\ 9.1\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes).",
    "new_string": "the 80-relation pool's larger extreme-batch gap (31.2\\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (quartile gaps: $-$3.92\\,pp vs.\\ $-$7.42\\,pp; Table~\\ref{tab:within_pool})."
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T03:47:46.421242+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T03:47:46.421426+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "high-BCS accuracy is model-invariant: both models converge",
  "new_string": "high-BCS accuracy is consistent across tested models (Qwen3-32B and Llama-3.1-8B): both models converge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "high-BCS accuracy is model-invariant: both models converge",
    "new_string": "high-BCS accuracy is consistent across tested models (Qwen3-32B and Llama-3.1-8B): both models converge"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T03:47:46.421740+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T03:47:46.424093+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "a task-inherent difficulty floor independent of model scale.",
  "new_string": "a task-inherent difficulty floor consistent across the tested models."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "a task-inherent difficulty floor independent of model scale.",
    "new_string": "a task-inherent difficulty floor consistent across the tested models."
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T03:47:46.424453+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T03:47:46.424688+00:00_

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
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T03:47:46.424927+00:00_

1	\begin{abstract}
2	Training-free LLM information extraction---prompting models with target schemas without fine-tuning---degrades sharply as schema complexity grows: NER recall drops from 0.72 to 0.42 with 64 candidate types, and RE accuracy falls from 85.7\% to 50.4\% with 80 relations. Prior work conflates type count with type confusability, leaving the mechanisms unclear. We conduct the first controlled empirical study isolating these factors across three IE tasks and three datasets, introducing the Schema Confusability Score (SCS) and two experimental paradigms: count curves that vary schema size while randomizing confusability, and BCS-controlled experiments that fix size while varying confusability. Our experiments reveal two degradation channels: a count channel that generally suppresses recall as candidate types increase, and a confusability channel where semantically similar types trigger intra-batch substitution errors---cleanly separable in RE; in NER, confusability additionally impairs entity detection. The BCS--accuracy relationship is robust across schema sizes: the regression slope is consistent between independent 16-type and within-pool 80-type evaluations (permutation $p = 0.44$), with the quartile gap reaching $-$7.4\,pp (95\% CI: [$-$9.4, $-$5.5]) on the independent 16-relation pool. On MAVEN's same-domain schema (168 event types), per-type confusability reverses direction due to a centrality confound, though pairwise confusability remains significant (\S\ref{sec:centrality_confound}). Both channels replicate on Llama-3.1-8B (count $r = 0.725$; confusability $\Delta = -27$\,pp), with high-BCS accuracy converging to a floor consistent across both tested models. Our confusability-aware decomposition yields an informative negative result: merge amplification destroys precision across all strategies, identifying a structural challenge for union-based merge pipelines in zero-shot IE.
3	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T03:47:46.425223+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
  "old_string": "though pairwise confusability remains significant (\\S\\ref{sec:centrality_confound})",
  "new_string": "though pairwise confusability remains significant"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
    "old_string": "though pairwise confusability remains significant (\\S\\ref{sec:centrality_confound})",
    "new_string": "though pairwise confusability remains significant"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T03:47:46.425455+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T03:47:46.425657+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "9\\.1",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Grep",
  "tool_args": {
    "pattern": "9\\.1",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T03:47:46.425834+00:00_

81:16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
90:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T03:47:46.427104+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "model-invariant",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Grep",
  "tool_args": {
    "pattern": "model-invariant",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T03:47:46.427292+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T03:47:46.427466+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "model-invariant",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Grep",
  "tool_args": {
    "pattern": "model-invariant",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T03:47:46.427636+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T03:47:46.427804+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "31\\.2",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Grep",
  "tool_args": {
    "pattern": "31\\.2",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T03:47:46.428015+00:00_

66:[Omitted long matching line]
82:80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
83:80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
86:\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap (31.2\,pp) reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.44$; Table~\ref{tab:within_pool}; see \S\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
90:[Omitted long matching line]
119:[Omitted long matching line]
123:[Omitted long matching line]
126:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-16T03:47:46.428240+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": "88",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "offset": "88",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T03:47:46.428434+00:00_

88	\end{table}
89	
90	At the 16-relation scale, the extreme-batch gap is 9.1\,pp (single batch per level; Table~\ref{tab:bcs_controlled}); the quartile gap from the within-pool analysis is $-$7.42\,pp (CI: [$-$9.40, $-$5.54]; Table~\ref{tab:within_pool}). At 80 relations, the gap reaches 31.2\,pp (extreme-batch comparison; 95\% CI: [17.7, 42.7]). The effect is stable across count levels: at count${}\,=\,16$, the gap remains 31.2\,pp (CI: [22.9, 39.6]). An intermediate evaluation at count${}\,=\,40$ (40-relation subsets sampled from the 80-relation pool) yields accuracy 0.588 and BCS gaps of $-$33.3\,pp (count 8) and $-$31.8\,pp (count 16), consistent with the 80-relation results and confirming monotonic decline within the pool.
91	
92	The larger absolute gap at 80 relations does not reflect a stronger per-unit sensitivity to confusability. As we show in the within-pool analysis below (\S\ref{sec:within_pool}), the BCS--accuracy slope is statistically indistinguishable across pools ($p = 0.44$). Rather, the 80-relation pool spans a wider BCS range (0.46--0.68 vs.\ 0.65--0.90 for 16-rel), enabling more extreme high-BCS batches that push accuracy further down the same gradient.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T03:47:46.428648+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "offset": "117",
  "limit": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "offset": "117",
    "limit": "10"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-16T03:47:46.428887+00:00_

117	\end{table}
118	
119	The within-pool condition confirms that the BCS--accuracy relationship is not an artifact of pool composition. The regression slope for 80-pool subsets ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.449; permutation $p = 0.436$), and the smaller absolute quartile gap ($-$3.92\,pp vs.\ $-$7.42\,pp) reflects the narrower BCS range available within the 80-relation pool (0.46--0.68 vs.\ 0.65--0.90; see Appendix~\ref{sec:appendix_within_pool} for CI details). This reinterprets the cross-pool gap in Table~\ref{tab:bcs_controlled}: the 80-relation pool's larger extreme-batch gap (31.2\,pp) reflects a wider BCS range, not a stronger per-unit sensitivity (quartile gaps: $-$3.92\,pp vs.\ $-$7.42\,pp; Table~\ref{tab:within_pool}).
120	
121	\paragraph{Practical magnitude.}
122	\label{sec:practical_magnitude}
123	For representative batches drawn from the 80-relation pool, the typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI: [0.4, 4.0]), roughly 7\% of the 31.2\,pp extreme-batch gap. A direct quartile comparison confirms this: the mean accuracy of bottom-quartile BCS batches is 82.8\%, versus 78.9\% for top-quartile batches, a gap of 3.9\,pp. The 31.2\,pp figure reflects the maximum BCS contrast available in the pool (extreme-batch comparison), not the typical batch experience; the 10th--90th percentile BCS span produces a gap of 4.2\,pp.
124	
125	\paragraph{Cross-model validation.}
126	The confusability effect replicates on Meta-Llama-3.1-8B-Instruct: on FewRel, the BCS gap is $-$27.1\,pp at count${}\,=\,8$ (low-BCS 78.1\% vs.\ high-BCS 51.0\%) and $-$23.9\,pp at count${}\,=\,16$ (75.5\% vs.\ 51.6\%), reaching 77--87\% of Qwen3-32B's $-$31.2\,pp extreme-batch gap. Strikingly, high-BCS accuracy is consistent across tested models (Qwen3-32B and Llama-3.1-8B): both models converge to $\approx$51\% under high confusability (count${}\,=\,8$: 51.0\% vs.\ 51.0\%; cou
…[truncated 254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-16T03:47:46.429179+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "the gap remains 31.2\\,pp (CI: [22.9, 39.6])",
  "new_string": "the extreme-batch gap remains 31.2\\,pp (CI: [22.9, 39.6])"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "old_string": "the gap remains 31.2\\,pp (CI: [22.9, 39.6])",
    "new_string": "the extreme-batch gap remains 31.2\\,pp (CI: [22.9, 39.6])"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-16T03:47:46.429476+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-16T03:47:46.429692+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "description": "First pdflatex pass",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
    "description": "First pdflatex pass",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T03:47:46.429921+00:00_

                                                  ^^@^^@^^@^^@^^@^^@^^@^^@^^...

! Text line contains an invalid character.
l.230 ...^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@
                                                  ^^@^^@^^@^^@^^@^^@^^@^^@^^...

! Text line contains an invalid character.
l.230 ...^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@
                                                  ^^@^^@^^@^^@^^@^^@^^@^^@^^...

! Text line contains an invalid character.
l.230 ...^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@
                                                  ^^@^^@^^@^^@^^@^^@^^@^^@^^...

! Text line contains an invalid character.
l.230 ...^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@^^@
                                                  ^^@^^@^^@^^@^^@^^@^^@^^@^^...
(That makes 100 errors; please try again.)
!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on main.log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-16T03:47:46.430157+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -rl $'\\x00' *.tex 2>/dev/null || echo \"no null bytes in .tex files\"",
  "description": "Find files with null bytes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -rl $'\\x00' *.tex 2>/dev/null || echo \"no null bytes in .tex files\"",
    "description": "Find files with null bytes"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-16T03:47:46.430339+00:00_

abstract.tex
checklist.tex
conclusion.tex
discussion.tex
experimental_setup.tex
introduction.tex
main.tex
prompt_appendix.tex
related_work.tex
results.tex
sdgd_negative.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-16T03:47:46.430559+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "xxd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex | grep '0000 0000' | head -5",
  "description": "Check null byte locations in results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "tool_args": {
    "command": "xxd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex | grep '0000 0000' | head -5",
    "description": "Check null byte locations in results.tex"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-16T03:47:46.430736+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-16T03:47:46.430927+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "xxd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex | grep '0000 0000' | head -5",
  "description": "Check null byte locations in abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "tool_args": {
    "command": "xxd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex | grep '0000 0000' | head -5",
    "description": "Check null byte locations in abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-16T03:47:46.431106+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-16T03:47:46.431276+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "xxd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex | grep ' 00' | head -3; echo \"---\"; xxd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex | grep ' 00' | head -3",
  "description": "Check for any null bytes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "tool_args": {
    "command": "xxd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex | grep ' 00' | head -3; echo \"---\"; xxd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex | grep ' 00' | head -3",
    "description": "Check for any null bytes"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-16T03:47:46.431459+00:00_

---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-16T03:47:46.432065+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "file results.tex abstract.tex main.tex introduction.tex experimental_setup.tex",
  "description": "Check file types"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "tool_args": {
    "command": "file results.tex abstract.tex main.tex introduction.tex experimental_setup.tex",
    "description": "Check file types"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-16T03:47:46.432299+00:00_

results.tex:            LaTeX document, ASCII text, with very long lines (1192)
abstract.tex:           LaTeX document, ASCII text, with very long lines (1878)
main.tex:               LaTeX 2e document, ASCII text, with very long lines (781)
introduction.tex:       LaTeX document, ASCII text, with very long lines (1284)
experimental_setup.tex: LaTeX document, ASCII text, with very long lines (1071)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-16T03:47:46.432488+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "for f in *.tex; do if file \"$f\" | grep -q -v ASCII; then echo \"BAD: $f\"; file \"$f\"; fi; done",
  "description": "Find non-ASCII tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "tool_args": {
    "command": "for f in *.tex; do if file \"$f\" | grep -q -v ASCII; then echo \"BAD: $f\"; file \"$f\"; fi; done",
    "description": "Find non-ASCII tex files"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-16T03:47:46.432666+00:00_

BAD: conclusion.tex
conclusion.tex: TeX document, Unicode text, UTF-8 text

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-16T03:47:46.432887+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "for f in *.tex; do if LC_ALL=C grep -P '\\x00' \"$f\" > /dev/null 2>&1; then echo \"NULL: $f\"; fi; done",
  "description": "Find files with actual null bytes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "tool_args": {
    "command": "for f in *.tex; do if LC_ALL=C grep -P '\\x00' \"$f\" > /dev/null 2>&1; then echo \"NULL: $f\"; fi; done",
    "description": "Find files with actual null bytes"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-16T03:47:46.433081+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-16T03:47:46.433304+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "rm -f main.aux main.bbl main.blg main.log main.out main.pdf && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30",
  "description": "Clean build first pdflatex pass",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "tool_args": {
    "command": "rm -f main.aux main.bbl main.blg main.log main.out main.pdf && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30",
    "description": "Clean build first pdflatex pass",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-16T03:47:46.433505+00:00_

LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `main.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmex10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cmextra/cmex9.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pf
b>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/
share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/te
xlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/te
xmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-di
st/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/u
crr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/f
onts/type1/urw/times/utmri8a.pfb>
Output written on main.pdf (13 pages, 352807 bytes).
Transcript written on main.log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-16T03:47:46.433719+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "bibtex main 2>&1 | tail -10 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"(Error|Warning|Output written)\" && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"(Error|Warning|Output written)\"",
  "description": "bibtex + two more pdflatex passes",
  "timeout": "120000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "tool_args": {
    "command": "bibtex main 2>&1 | tail -10 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"(Error|Warning|Output written)\" && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"(Error|Warning|Output written)\"",
    "description": "bibtex + two more pdflatex passes",
    "timeout": "120000"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-16T03:47:46.434010+00:00_

This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
Warning--I didn't find a database entry for "ding-fewnerd-2021"
Warning--I didn't find a database entry for "wang-maven-2020"
Warning--I didn't find a database entry for "han-fewrel-2018"
(There were 3 warnings)
Package natbib Warning: Citation `llm4ie-survey-2024' on page 1 undefined on in
Package natbib Warning: Citation `uniner-2024' on page 1 undefined on input lin
Package natbib Warning: Citation `llm-pee-2025' on page 1 undefined on input li
Package natbib Warning: Citation `parse-2025' on page 1 undefined on input line
Package natbib Warning: Citation `llm-pee-2025' on page 1 undefined on input li
Package natbib Warning: Citation `fewnerd-2021' on page 2 undefined on input li
Package natbib Warning: Citation `fewrel-2018' on page 2 undefined on input lin
Package natbib Warning: Citation `maven-2020' on page 2 undefined on input line
Package natbib Warning: Citation `instructuie-2023' on page 2 undefined on inpu
Package natbib Warning: Citation `knowcoder-2024' on page 2 undefined on input 
Package natbib Warning: Citation `codeie-2023' on page 2 undefined on input lin
Package natbib Warning: Citation `gollie-2024' on page 2 undefined on input lin
Package natbib Warning: Citation `adelie-2024' on page 2 undefined on input lin
Package natbib Warning: Citation `slot-2025' on page 2 undefined on input line 
Package natbib Warning: Citation `oneke-2025' on page 2 undefined on input line
Package natbib Warning: Citation `json-schema-bench-2025' on page 2 undefined o
Package natbib Warning: Citation `chatgpt-ie-eval-2023' on page 2 undefined on 
Package natbib Warning: Citation `wadhwa-re-llm-2023' on page 2 undefined on in
Package natbib Warning: Citation `xie-zeroshot-ner-2023' on page 2 undefined on
Package natbib Warning: Citation `promptner-2023' on page 2 undefined on input 
Package natbib Warning: Citation
…[truncated 4569 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-16T03:47:46.434267+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"(Error|Output written)\"",
  "description": "Final pdflatex pass to resolve cross-refs",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "tool_args": {
    "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"(Error|Output written)\"",
    "description": "Final pdflatex pass to resolve cross-refs",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-16T03:47:46.434448+00:00_

Output written on main.pdf (16 pages, 389316 bytes).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_write_d037_stats_integration_20260516T034255",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 77 · 2026-05-16T03:47:46.434687+00:00_

Compilation successful, no errors. 16 pages.

**Summary of edits made:**

**results.tex:**
- **2A**: NER paragraph — 0.52→0.522, 0.55→0.549, added "bootstrap" before CIs, reformatted as "overlap: ... vs.\ ..."
- **C2 (9.1pp)**: Table caption reframed from "widens from 9.1 to 31.2" to slope-consistency narrative; line 90 now shows 9.1pp as extreme-batch with quartile gap $-$7.42pp alongside; line 119 replaced "31.2 vs.\ 9.1" with quartile gaps from Table 4
- **C3 (31.2pp)**: Added "extreme-batch" caveat to all remaining 31.2pp mentions (line 90 count=16 reference)
- **W12**: "model-invariant" → "consistent across tested models (Qwen3-32B and Llama-3.1-8B)" (2 occurrences)

**abstract.tex:**
- Removed `\S\ref{sec:centrality_confound}` cross-reference (abstracts should be self-contained)
- C2, W7, W12 were already applied by the other worker

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_write_d037_stats_integration_20260516T034255"
}
```

</details>

---
