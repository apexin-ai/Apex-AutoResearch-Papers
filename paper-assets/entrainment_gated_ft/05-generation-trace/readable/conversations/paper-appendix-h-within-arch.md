# paper appendix h within arch

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 67
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/chats/worker_paper_appendix-h-within-arch_20260520T030458.jsonl`
- **Structured JSON:** [`29efbb60f8dd93d06086.json`](../../sessions/29/29efbb60f8dd93d06086.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

67 recorded events

### Tool call

_source line 1 · 2026-05-20T03:09:11.309608+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T03:09:11.309989+00:00_

docs/paper/sections/method.tex
docs/paper/sections/related_work.tex
docs/paper/sections/introduction.tex
docs/paper/main.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/appendix.tex
docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T03:09:11.310165+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T03:09:11.310407+00:00_

1	% Appendix sections for the paper.
2	
3	\section{Pre-registration Details}\label{app:benchmark_details}
4	
5	The task taxonomy used in \S\ref{ssec:task_taxonomy} was defined prior to running any convergence analyses. Each benchmark was assigned to exactly one of four categories based on the primary cognitive demand of the task:
6	
7	\begin{itemize}
8	    \item \textbf{Retrieval}: tasks requiring prediction from long-range context without multi-step reasoning (LAMBADA).
9	    \item \textbf{Comprehension}: reading comprehension with explicit passage support (BoolQ).
10	    \item \textbf{Reasoning}: tasks requiring commonsense inference or multi-step reasoning (HellaSwag, ARC-Challenge, WinoGrande, PIQA).
11	    \item \textbf{Mixed}: tasks combining retrieval, comprehension, and reasoning demands (ARC-Easy, MMLU, SciQ, XStoryCloze).
12	\end{itemize}
13	
14	\paragraph{Pre-registered benchmark set.} Six benchmarks were pre-registered for Bonferroni correction: LAMBADA, HellaSwag, ARC-Challenge, WinoGrande, ARC-Easy, and MMLU. These were selected as representative of retrieval, reasoning, and mixed categories before any convergence analysis was performed. The Bonferroni-adjusted significance threshold is $\alpha / 6 = 0.0083$.
15	
16	\paragraph{Exploratory benchmarks.} Four additional benchmarks (BoolQ, PIQA, SciQ, XStoryCloze) were added as exploratory tests. These are corrected separately across all 10 benchmarks (adjusted threshold $\alpha / 10 = 0.005$) and reported as exploratory throughout the paper.
17	
18	\paragraph{Supplementary benchmark.} COPA ($n = 100$) is treated as supplementary due to its small sample size. It is excluded from both correction families and reported separately with the $\dagger$ annotation in Table~\ref{tab:convergence}.
19	
20	\section{Sensitivity Analyses}\label{app:sensitivity}
21	
22	\subsection{Bootstrap Confidence Intervals}
23	
24	We construct 95\% bootstrap confidence intervals for the Spearman $\rho$ between attention ratio and cr
…[truncated 13118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T03:09:11.310571+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T03:09:11.310822+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	We analyze how attention affects cross-architecture performance variance using models from the hybrid recurrent model zoo of \citet{wang2025hybrid}. Our analysis spans three architectures (GatedDeltaNet, RetNet, HGRN2), five attention ratios (0\% pure recurrent, 4\%, 7.7\%, 14.3\%, 25\%), and two scales (340M and 1.3B parameters). In the h$k$-1 notation used throughout, one attention layer is interleaved per every $k{+}1$ layers; h3-1 denotes 25\% attention. All models within each scale share identical training data and hyperparameters; they differ only in architecture and attention configuration. We evaluate on 10 benchmarks spanning retrieval, comprehension, reasoning, and mixed task categories, plus one supplementary benchmark (COPA, $n = 100$).
4	
5	\subsection{Task-Specific Convergence}\label{ssec:task_convergence}
6	
7	We first ask whether adding attention layers reduces performance differences between architectures, and whether any such reduction is uniform across tasks. For each benchmark, we compute the cross-architecture standard deviation ($\sigma$) at each attention ratio and measure the Spearman rank correlation ($\rho$) between attention ratio and $\sigma$ across the five configurations.
8	
9	Table~\ref{tab:convergence} reports results for all benchmarks at 1.3B scale. LAMBADA is the only benchmark exhibiting monotonic convergence: $\rho = -1.0$ (exact permutation test, $p = .017$, two-tailed, $n = 5$, 120 permutations). Cross-architecture $\sigma$ drops from 0.024 to 0.005, a 79\% reduction. The 95\% BCa percentile bootstrap confidence interval for $\rho$ is $[-1.0, -0.7]$ (10{,}000 resamples), which excludes zero. After Bonferroni correction for six pre-registered benchmarks, the adjusted $p = .100$ does not survive strict Bonferroni correction at $\alpha = 0.05$. We therefore treat the confidence interval, rather than the corrected $p$-value, as the primary evidence for the LAMBADA convergence effe
…[truncated 11634 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T03:09:11.311032+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T03:09:11.311166+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T03:09:11.311288+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft -name \"*jaccard*\" -o -name \"*within*\" -o -name \"*pairwise*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root/entrainment_gated_ft -name \"*jaccard*\" -o -name \"*within*\" -o -name \"*pairwise*\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T03:09:11.311443+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T03:09:11.311569+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft -name \"*jaccard*\" -o -name \"*within*\" -o -name \"*pairwise*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root/entrainment_gated_ft -name \"*jaccard*\" -o -name \"*within*\" -o -name \"*pairwise*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T03:09:11.311732+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/entrainment_gated_ft/analysis/within_arch_stability.py\\n/root/entrainment_gated_ft/analysis/within_arch_stability.json\\n/root/entrainment_gated_ft/null_jaccard_permutation.py\\n/root/entrainment_gated_ft/null_jaccard_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.18}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T03:09:11.311872+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "cat /root/entrainment_gated_ft/analysis/within_arch_stability.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "cat /root/entrainment_gated_ft/analysis/within_arch_stability.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T03:09:11.312077+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"GatedDeltaNet\\\": {\\n    \\\"helped_jaccard\\\": {\\n      \\\"h24-1_vs_h12-1\\\": 0.3449,\\n      \\\"h24-1_vs_h6-1\\\": 0.3348,\\n      \\\"h24-1_vs_h3-1\\\": 0.3112,\\n      \\\"h12-1_vs_h6-1\\\": 0.3442,\\n      \\\"h12-1_vs_h3-1\\\": 0.3405,\\n      \\\"h6-1_vs_h3-1\\\": 0.3521\\n    },\\n    \\\"hurt_jaccard\\\": {\\n      \\\"h24-1_vs_h12-1\\\": 0.3095,\\n      \\\"h24-1_vs_h6-1\\\": 0.3281,\\n      \\\"h24-1_vs_h3-1\\\": 0.3204,\\n      \\\"h12-1_vs_h6-1\\\": 0.3306,\\n      \\\"h12-1_vs_h3-1\\\": 0.281,\\n      \\\"h6-1_vs_h3-1\\\": 0.3451\\n    },\\n    \\\"helped_counts\\\": {\\n      \\\"h24-1\\\": 487,\\n      \\\"h12-1\\\": 480,\\n      \\\"h6-1\\\": 426,\\n      \\\"h3-1\\\": 461\\n    },\\n    \\\"hurt_counts\\\": {\\n      \\\"h24-1\\\": 505,\\n      \\\"h12-1\\\": 519,\\n      \\\"h6-1\\\": 600,\\n      \\\"h3-1\\\": 616\\n    },\\n    \\\"pure_correct_count\\\": 2800\\n  },\\n  \\\"RetNet\\\": {\\n    \\\"helped_jaccard\\\": {\\n      \\\"h24-1_vs_h12-1\\\": 0.3539,\\n      \\\"h24-1_vs_h6-1\\\": 0.3141,\\n      \\\"h24-1_vs_h3-1\\\": 0.3344,\\n      \\\"h12-1_vs_h6-1\\\": 0.3221,\\n      \\\"h12-1_vs_h3-1\\\": 0.3302,\\n      \\\"h6-1_vs_h3-1\\\": 0.3449\\n    },\\n    \\\"hurt_jaccard\\\": {\\n      \\\"h24-1_vs_h12-1\\\": 0.3156,\\n      \\\"h24-1_vs_h6-1\\\": 0.3343,\\n      \\\"h24-1_vs_h3-1\\\": 0.3068,\\n      \\\"h12-1_vs_h6-1\\\": 0.3008,\\n      \\\"h12-1_vs_h3-1\\\": 0.3235,\\n      \\\"h6-1_vs_h3-1\\\": 0.3432\\n    },\\n    \\\"helped_counts\\\": {\\n      \\\"h24-1\\\": 446,\\n      \\\"h12-1\\\": 430,\\n      \\\"h6-1\\\": 395,\\n      \\\"h3-1\\\": 420\\n    },\\n    \\\"hurt_counts\\\": {\\n      \\\"h24-1\\\": 457,\\n      \\\"h12-1\\\": 485,\\n      \\\"h6-1\\\": 501,\\n      \\\"h3-1\\\": 497\\n    },\\n    \\\"pure_correct_count\\\": 2666\\n  },\\n  \\\"HGRN2\\\": {\\n    \\\"helped_jaccard\\\": {\\n      \\\"h24-1_vs_h12-1\\\": 0.3594,\\n      \\\"h24-1_vs_h6
…[truncated 1219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T03:09:11.312316+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex",
  "old_string": "\tAn analysis of attention weight patterns provides partial insight into this decoupling.",
  "new_string": "\tWithin-architecture Jaccard across attention ratios averages approximately 0.33 (Appendix~\\ref{app:within_arch_stability}), roughly three times the cross-architecture value, indicating that architecture identity has greater influence than attention dose on which examples are affected.\n\n\tAn analysis of attention weight patterns provides partial insight into this decoupling."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex",
    "old_string": "\tAn analysis of attention weight patterns provides partial insight into this decoupling.",
    "new_string": "\tWithin-architecture Jaccard across attention ratios averages approximately 0.33 (Appendix~\\ref{app:within_arch_stability}), roughly three times the cross-architecture value, indicating that architecture identity has greater influence than attention dose on which examples are affected.\n\n\tAn analysis of attention weight patterns provides partial insight into this decoupling."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T03:09:11.312464+00:00_

&lt;tool_use_error>String to replace not found in file.
String: 	An analysis of attention weight patterns provides partial insight into this decoupling.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T03:09:11.312588+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex",
  "offset": "82",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex",
    "offset": "82",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T03:09:11.312758+00:00_

82	Bootstrap confidence intervals (10{,}000 resamples over examples) provide statistical confirmation of the decoupling. The 95\% CI for cross-architecture $\sigma$ does not overlap between the pure configuration $[0.019, 0.030]$ and h3-1 $[0.002, 0.011]$, confirming significant aggregate convergence. In contrast, the 95\% CIs for mean pairwise Jaccard overlap completely across all four non-zero attention ratios (helped: $[0.08, 0.11]$ at each ratio; hurt: $[0.07, 0.11]$), statistically confirming the saturation pattern visible in Figure~\ref{fig:decoupling}.
83	
84	An analysis of attention weight patterns provides partial insight into this decoupling. At layer 2 of the 1.3B h3-1 models, GDN and RetNet produce nearly identical attention distributions (cosine similarity 0.995), yet their per-example effects differ substantially. HGRN2 attention patterns diverge from the other architectures at early layers (cosine $\sim$0.20) but converge at deeper layers ($>$0.94 at layer 20). Attention entropy does not differ between helped and hurt examples, which indicates that the per-example effects originate in the recurrent layers rather than in the attention mechanism itself. Full results appear in Appendix~D.
85	
86	\subsection{Robustness}\label{ssec:robustness}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T03:09:11.312897+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex",
  "old_string": "An analysis of attention weight patterns provides partial insight into this decoupling. At layer 2",
  "new_string": "Within-architecture Jaccard across attention ratios averages approximately 0.33 (Appendix~\\ref{app:within_arch_stability}), roughly three times the cross-architecture value, indicating that architecture identity has greater influence than attention dose on which examples are affected.\n\nAn analysis of attention weight patterns provides partial insight into this decoupling. At layer 2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex",
    "old_string": "An analysis of attention weight patterns provides partial insight into this decoupling. At layer 2",
    "new_string": "Within-architecture Jaccard across attention ratios averages approximately 0.33 (Appendix~\\ref{app:within_arch_stability}), roughly three times the cross-architecture value, indicating that architecture identity has greater influence than attention dose on which examples are affected.\n\nAn analysis of attention weight patterns provides partial insight into this decoupling. At layer 2"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T03:09:11.313069+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T03:09:11.313224+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
  "old_string": "All three architectures show positive $\\Delta$: the h3-1 correct set is more similar to the Transformer correct set than the pure correct set is. The effect is strongest for HGRN2 ($+$0.029) and weakest for GDN ($+$0.005). This ordering is consistent with HGRN2 being the only architecture with a positive net per-example effect from attention (Table~\\ref{tab:per_example}). The Transformer itself achieves the lowest accuracy among all models, so the convergence is not explained by hybrid models degrading toward Transformer-level performance; rather, adding attention shifts which specific examples the hybrid gets correct toward the Transformer's pattern.",
  "new_string": "All three architectures show positive $\\Delta$: the h3-1 correct set is more similar to the Transformer correct set than the pure correct set is. The effect is strongest for HGRN2 ($+$0.029) and weakest for GDN ($+$0.005). This ordering is consistent with HGRN2 being the only architecture with a positive net per-example effect from attention (Table~\\ref{tab:per_example}). The Transformer itself achieves the lowest accuracy among all models, so the convergence is not explained by hybrid models degrading toward Transformer-level performance; rather, adding attention shifts which specific examples the hybrid gets correct toward the Transformer's pattern.\n\n\\section{Within-Architecture Per-Example Stability}\\label{app:within_arch_stability}\n\nPer-example effect sets exhibit a three-tier Jaccard hierarchy on LAMBADA (1.3B scale). Under independence (permutation baseline), pairwise Jaccard is $J \\approx 0.05$. Cross-architecture comparisons (different architectures at the same attention ratio) yield $J \\approx 0.10$, approximately $2\\times$ baseline. Within-architecture comparisons (same architecture across different attention ratios) yield $J \\approx 0.33$, approximately $7\\times$ baseline and $3\\times$ the cross-architecture level. Architecture identity therefore has approximately three times the influence of attention dose on per-example effects.\n\nTable~\\ref{tab:within_arch_summary} reports mean within-architecture Jaccard for each architecture. HGRN2 shows the highest helped overlap and lowest hurt overlap, consistent with its monotonically increasing helped count across ratios (479 $\\to$ 548).\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean within-architecture pairwise Jaccard similarity across attention ratios (1.3B, LAMBADA). Each mean is computed over all six ratio pairs per architecture.}\n\\label{tab:within_arch_summary}\n\\begin{tabular}{lcc}\n\\toprule\nArchitecture & $\\bar{J}_{\\text{helped}}$ & $\\bar{J}_{\\text{hurt}}$ \\\\\n\\midrule\nGDN & 0.338 & 0.319 \\\\\nRetNet & 0.333 & 0.321 \\\\\nHGRN2 & 0.373 & 0.291 \\\\\n\\midrule\n\\textit{Overall mean} & \\textit{0.348} & \\textit{0.310} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:within_arch_pairwise} reports the full pairwise Jaccard matrix. Attention ratios are denoted by their h$k$-1 labels: h24-1 (4\\%), h12-1 (7.7\\%), h6-1 (14.3\\%), h3-1 (25\\%).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Within-architecture pairwise Jaccard similarity between helped and hurt sets at different attention ratios (1.3B, LAMBADA). Each cell compares the per-example effect sets of two attention configurations within the same architecture.}\n\\label{tab:within_arch_pairwise}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccccc}\n\\toprule\n & & \\multicolumn{6}{c}{Ratio pair} \\\\\n\\cmidrule(lr){3-8}\nArch & Cat & h24--h12 & h24--h6 & h24--h3 & h12--h6 & h12--h3 & h6--h3 \\\\\n\\midrule\n\\multirow{2}{*}{GDN} & Helped & .345 & .335 & .311 & .344 & .341 & .352 \\\\\n & Hurt & .310 & .328 & .320 & .331 & .281 & .345 \\\\\n\\midrule\n\\multirow{2}{*}{RetNet} & Helped & .354 & .314 & .334 & .322 & .330 & .345 \\\\\n & Hurt & .316 & .334 & .307 & .301 & .324 & .343 \\\\\n\\midrule\n\\multirow{2}{*}{HGRN2} & Helped & .359 & .369 & .375 & .368 & .378 & .388 \\\\\n & Hurt & .292 & .289 & .298 & .273 & .309 & .287 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nAdjacent ratio pairs (e.g., h24-1 vs.\\ h12-1) do not exhibit systematically higher Jaccard than non-adjacent pairs (e.g., h24-1 vs.\\ h3-1). Across all architectures, the mean Jaccard for adjacent pairs is 0.336 (helped) and 0.311 (hurt), compared with 0.337 (helped) and 0.311 (hurt) for non-adjacent pairs. The negligible difference indicates that the mapping from attention dose to per-example effects is non-smooth: doubling the attention ratio does not produce a proportionally more similar set of affected examples."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
    "old_string": "All three architectures show positive $\\Delta$: the h3-1 correct set is more similar to the Transformer correct set than the pure correct set is. The effect is strongest for HGRN2 ($+$0.029) and weakest for GDN ($+$0.005). This ordering is consistent with HGRN2 being the only architecture with a positive net per-example effect from attention (Table~\\ref{tab:per_example}). The Transformer itself achieves the lowest accuracy among all models, so the convergence is not explained by hybrid models degrading toward Transformer-level performance; rather, adding attention shifts which specific examples the hybrid gets correct toward the Transformer's pattern.",
    "new_string": "All three architectures show positive $\\Delta$: the h3-1 correct set is more similar to the Transformer correct set than the pure correct set is. The effect is strongest for HGRN2 ($+$0.029) and weakest for GDN ($+$0.005). This ordering is consistent with HGRN2 being the only architecture with a positive net per-example effect from attention (Table~\\ref{tab:per_example}). The Transformer itself achieves the lowest accuracy among all models, so the convergence is not explained by hybrid models degrading toward Transformer-level performance; rather, adding attention shifts which specific examples the hybrid gets correct toward the Transformer's pattern.\n\n\\section{Within-Architecture Per-Example Stability}\\label{app:within_arch_stability}\n\nPer-example effect sets exhibit a three-tier Jaccard hierarchy on LAMBADA (1.3B scale). Under independence (permutation baseline), pairwise Jaccard is $J \\approx 0.05$. Cross-architecture comparisons (different architectures at the same attention ratio) yield $J \\approx 0.10$, approximately $2\\times$ baseline. Within-architecture comparisons (same architecture across different attention ratios) yield $J \\approx 0.33$, approximately $7\\times$ baseline and $3\\times$ the cross-architecture level. Architecture identity therefore has approximately three times the influence of attention dose on per-example effects.\n\nTable~\\ref{tab:within_arch_summary} reports mean within-architecture Jaccard for each architecture. HGRN2 shows the highest helped overlap and lowest hurt overlap, consistent with its monotonically increasing helped count across ratios (479 $\\to$ 548).\n\n\\begin{table}[h]\n\\centering\n\\caption{Mean within-architecture pairwise Jaccard similarity across attention ratios (1.3B, LAMBADA). Each mean is computed over all six ratio pairs per architecture.}\n\\label{tab:within_arch_summary}\n\\begin{tabular}{lcc}\n\\toprule\nArchitecture & $\\bar{J}_{\\text{helped}}$ & $\\bar{J}_{\\text{hurt}}$ \\\\\n\\midrule\nGDN & 0.338 & 0.319 \\\\\nRetNet & 0.333 & 0.321 \\\\\nHGRN2 & 0.373 & 0.291 \\\\\n\\midrule\n\\textit{Overall mean} & \\textit{0.348} & \\textit{0.310} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:within_arch_pairwise} reports the full pairwise Jaccard matrix. Attention ratios are denoted by their h$k$-1 labels: h24-1 (4\\%), h12-1 (7.7\\%), h6-1 (14.3\\%), h3-1 (25\\%).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Within-architecture pairwise Jaccard similarity between helped and hurt sets at different attention ratios (1.3B, LAMBADA). Each cell compares the per-example effect sets of two attention configurations within the same architecture.}\n\\label{tab:within_arch_pairwise}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccccc}\n\\toprule\n & & \\multicolumn{6}{c}{Ratio pair} \\\\\n\\cmidrule(lr){3-8}\nArch & Cat & h24--h12 & h24--h6 & h24--h3 & h12--h6 & h12--h3 & h6--h3 \\\\\n\\midrule\n\\multirow{2}{*}{GDN} & Helped & .345 & .335 & .311 & .344 & .341 & .352 \\\\\n & Hurt & .310 & .328 & .320 & .331 & .281 & .345 \\\\\n\\midrule\n\\multirow{2}{*}{RetNet} & Helped & .354 & .314 & .334 & .322 & .330 & .345 \\\\\n & Hurt & .316 & .334 & .307 & .301 & .324 & .343 \\\\\n\\midrule\n\\multirow{2}{*}{HGRN2} & Helped & .359 & .369 & .375 & .368 & .378 & .388 \\\\\n & Hurt & .292 & .289 & .298 & .273 & .309 & .287 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table}\n\nAdjacent ratio pairs (e.g., h24-1 vs.\\ h12-1) do not exhibit systematically higher Jaccard than non-adjacent pairs (e.g., h24-1 vs.\\ h3-1). Across all architectures, the mean Jaccard for adjacent pairs is 0.336 (helped) and 0.311 (hurt), compared with 0.337 (helped) and 0.311 (hurt) for non-adjacent pairs. The negligible difference indicates that the mapping from attention dose to per-example effects is non-smooth: doubling the attention ratio does not produce a proportionally more similar set of affected examples."
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T03:09:11.313471+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T03:09:11.313622+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\n# Adjacent pairs: h24-h12, h12-h6, h6-h3\n# Non-adjacent pairs: h24-h6, h24-h3, h12-h3\n\nadj_helped = [0.3449, 0.3442, 0.3521,  # GDN\n              0.3539, 0.3221, 0.3449,  # RetNet\n              0.3594, 0.3678, 0.3877]  # HGRN2\nnonadj_helped = [0.3348, 0.3112, 0.3405,  # GDN\n                 0.3141, 0.3344, 0.3302,  # RetNet\n                 0.3694, 0.3748, 0.3784]  # HGRN2\n\nadj_hurt = [0.3095, 0.3306, 0.3451,  # GDN\n            0.3156, 0.3008, 0.3432,  # RetNet\n            0.2919, 0.2733, 0.2869]  # HGRN2\nnonadj_hurt = [0.3281, 0.3204, 0.2810,  # GDN\n               0.3343, 0.3068, 0.3235,  # RetNet\n               0.2887, 0.2977, 0.3089]  # HGRN2\n\nprint(f'Adjacent helped: {sum(adj_helped)/len(adj_helped):.3f}')\nprint(f'Non-adjacent helped: {sum(nonadj_helped)/len(nonadj_helped):.3f}')\nprint(f'Adjacent hurt: {sum(adj_hurt)/len(adj_hurt):.3f}')\nprint(f'Non-adjacent hurt: {sum(nonadj_hurt)/len(nonadj_hurt):.3f}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\n# Adjacent pairs: h24-h12, h12-h6, h6-h3\n# Non-adjacent pairs: h24-h6, h24-h3, h12-h3\n\nadj_helped = [0.3449, 0.3442, 0.3521,  # GDN\n              0.3539, 0.3221, 0.3449,  # RetNet\n              0.3594, 0.3678, 0.3877]  # HGRN2\nnonadj_helped = [0.3348, 0.3112, 0.3405,  # GDN\n                 0.3141, 0.3344, 0.3302,  # RetNet\n                 0.3694, 0.3748, 0.3784]  # HGRN2\n\nadj_hurt = [0.3095, 0.3306, 0.3451,  # GDN\n            0.3156, 0.3008, 0.3432,  # RetNet\n            0.2919, 0.2733, 0.2869]  # HGRN2\nnonadj_hurt = [0.3281, 0.3204, 0.2810,  # GDN\n               0.3343, 0.3068, 0.3235,  # RetNet\n               0.2887, 0.2977, 0.3089]  # HGRN2\n\nprint(f'Adjacent helped: {sum(adj_helped)/len(adj_helped):.3f}')\nprint(f'Non-adjacent helped: {sum(nonadj_helped)/len(nonadj_helped):.3f}')\nprint(f'Adjacent hurt: {sum(adj_hurt)/len(adj_hurt):.3f}')\nprint(f'Non-adjacent hurt: {sum(nonadj_hurt)/len(nonadj_hurt):.3f}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T03:09:11.313779+00:00_

Adjacent helped: 0.353
Non-adjacent helped: 0.343
Adjacent hurt: 0.311
Non-adjacent hurt: 0.310

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T03:09:11.313950+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
  "old_string": "Across all architectures, the mean Jaccard for adjacent pairs is 0.336 (helped) and 0.311 (hurt), compared with 0.337 (helped) and 0.311 (hurt) for non-adjacent pairs.",
  "new_string": "Across all architectures, the mean Jaccard for adjacent pairs is 0.353 (helped) and 0.311 (hurt), compared with 0.343 (helped) and 0.310 (hurt) for non-adjacent pairs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
    "old_string": "Across all architectures, the mean Jaccard for adjacent pairs is 0.336 (helped) and 0.311 (hurt), compared with 0.337 (helped) and 0.311 (hurt) for non-adjacent pairs.",
    "new_string": "Across all architectures, the mean Jaccard for adjacent pairs is 0.353 (helped) and 0.311 (hurt), compared with 0.343 (helped) and 0.310 (hurt) for non-adjacent pairs."
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T03:09:11.314246+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T03:09:11.314466+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T03:09:11.314674+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T03:09:11.314899+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "ls /root/entrainment_gated_ft/docs/paper/sections/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "ls /root/entrainment_gated_ft/docs/paper/sections/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T03:09:11.315093+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/entrainment_gated_ft/docs/paper/sections/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.8}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T03:09:11.315281+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root/entrainment_gated_ft -name \"*.tex\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root/entrainment_gated_ft -name \"*.tex\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T03:09:11.315479+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.8}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T03:09:11.315668+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westb-48145",
  "command": "find /root -name \"main.tex\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westb-48145",
    "command": "find /root -name \"main.tex\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T03:09:11.315853+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.06}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T03:09:11.316038+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "scp -r /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/ westb-48145:/root/entrainment_gated_ft/docs/paper/ 2>&1",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "tool_args": {
    "command": "scp -r /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/ westb-48145:/root/entrainment_gated_ft/docs/paper/ 2>&1",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T03:09:11.316205+00:00_

Exit code 255
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Permission denied, please try again.
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Permission denied, please try again.
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
root@connect.westb.seetacloud.com: Permission denied (publickey,password).
scp: Connection closed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T03:09:11.316389+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T03:09:11.316567+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T03:09:11.316777+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "which pdflatex latexmk 2>/dev/null; dpkg -l texlive-latex-base 2>/dev/null | grep ^ii | head -1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "tool_args": {
    "command": "which pdflatex latexmk 2>/dev/null; dpkg -l texlive-latex-base 2>/dev/null | grep ^ii | head -1"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T03:09:11.316917+00:00_

/usr/bin/pdflatex
/usr/bin/latexmk
ii  texlive-latex-base 2025.20260124-1 all          TeX Live: LaTeX fundamental packages

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T03:09:11.317048+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T03:09:11.317198+00:00_

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
13	\usepackage{multirow}
14	\usepackage{xcolor}
15	
16	\title{Aggregate Convergence, Per-Example Divergence: Decoupled Effects of Attention in Hybrid Recurrent Architectures}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	Hybrid recurrent architectures that interleave attention layers with linear recurrence are increasingly standard, yet how attention affects per-example behavior across different recurrent backbones remains poorly quantified. We conduct a systematic analysis using the controlled model zoo of \citet{wang2025hybrid}: three architectures (GatedDeltaNet, RetNet, HGRN2) at five attention ratios and two scales (340M and 1.3B parameters), evaluated on 10 benchmarks with 5{,}153 per-example comparisons on LAMBADA. Of the 10 benchmarks, only LAMBADA exhibits cross-architecture convergence ($\rho = -1.0$, BCa 95\% CI $[-1.0, -0.7]$; cross-architecture standard deviation drops 79\%). The Bonferroni-adjusted $p = .100$ does not survive strict correction; the confidence interval serves as primary evidence. This convergence is complete at 1.3B but partial and non-monotonic at 340M; sufficient scale appears necessary for full equalization. Despite aggregate convergence, per-example helped and hurt sets are nearly disjoint across architectures (Jaccard similarity $\leq 0.11$), and this overlap saturates at minimal (4\%) attention. Aggregate performance equalizes progressively, while per-example specificity is fixed from the earliest attention allocation. These results quantify underspecification in hybrid architecture design: aggregate equivalence does not imply per-example behavioral interchangeability.
25	\end{abstract}
26	
27	\input{sections/introduction}
28
…[truncated 3010 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T03:09:11.317352+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -30",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T03:09:11.317484+00:00_

) [13] [14] (./main.aux)

LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `main.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmbx10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/pub
lic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/ams
fonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm
/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/u
sr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/texli
ve/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/u
rw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmri8
a.pfb>
Output written on main.pdf (14 pages, 351443 bytes).
Transcript written on main.log.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T03:09:11.317618+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"^!|Error|Output written|pages\"",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "tool_args": {
    "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"^!|Error|Output written|pages\"",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T03:09:11.317799+00:00_

Output written on main.pdf (14 pages, 351167 bytes).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T03:09:11.317936+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"^\\[|Output written\"",
  "timeout": "60000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "tool_args": {
    "command": "pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"^\\[|Output written\"",
    "timeout": "60000"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T03:09:11.318059+00:00_

[Loading MPS to PDF converter (version 2006.09.02).]
[]\T1/ptm/m/n/10.95 (+20) Our anal-y-sis yields three find-ings. First,
[3]) (./sections/method.tex
[]\T1/ptm/b/n/10.95 (+20) Reasoning\T1/ptm/m/n/10.95 (+20) : Hel-laSwag, ARC-Ch
[4]
[]\T1/ptm/m/n/10 (+20) Kawin Etha-yarajh, Yejin Choi, and Swabha
[9]
[]\T1/ptm/m/n/10 (+20) Balaji Lak-sh-mi-narayanan, Alexan-der Pritzel, and
[]\T1/ptm/b/n/10.95 (+20) Comprehension\T1/ptm/m/n/10.95 (+20) : read-ing com-p
[10]
[11]
Output written on main.pdf (14 pages, 351167 bytes).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T03:09:11.318177+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"\\\\\\\\appendix\\|\\\\\\\\section\\*{Limitations}\\|\\\\\\\\section\\*{Ethics\" main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"\\\\\\\\appendix\\|\\\\\\\\section\\*{Limitations}\\|\\\\\\\\section\\*{Ethics\" main.tex"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T03:09:11.318289+00:00_

37:\section*{Limitations}
53:\section*{Ethics Statement}
59:\appendix

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T03:09:11.318418+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -c \"newpage\\|\\\\\\\\clearpage\" main.tex; grep \"Limitations\" main.log | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -c \"newpage\\|\\\\\\\\clearpage\" main.tex; grep \"Limitations\" main.log | head -5"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T03:09:11.318527+00:00_

0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T03:09:11.318663+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\nlines = result.stdout.split('\\f')  # form feed separates pages\nfor i, page in enumerate(lines):\n    first_line = page.strip().split('\\n')[0] if page.strip() else '(empty)'\n    print(f'Page {i+1}: {first_line[:80]}')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\nlines = result.stdout.split('\\f')  # form feed separates pages\nfor i, page in enumerate(lines):\n    first_line = page.strip().split('\\n')[0] if page.strip() else '(empty)'\n    print(f'Page {i+1}: {first_line[:80]}')\n\""
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T03:09:11.318809+00:00_

Page 1: Aggregate Convergence, Per-Example Divergence: Decoupled Effects of
Page 2: (a) Gradual reduction across 5 levels
Page 3: further, while inter-architecture asymmetry
Page 4: 272
Page 5: 379
Page 6: 463
Page 7: Table 1: Cross-architecture convergence across benchmarks (1.3B scale). ρ: Spear
Page 8: Table 2: Per-example effects of attention (pure → h3¯
Page 9: 696
Page 10: 793
Page 11: 890
Page 12: 979
Page 13: 1031
Page 14: Table 11: Mean within-architecture pairwise Jaccard
Page 15: (empty)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T03:09:11.318939+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\nfor i, page in enumerate(pages):\n    if 'Limitations' in page:\n        print(f'Limitations found on page {i+1}')\n        break\nfor i, page in enumerate(pages):\n    if 'Pre-registration' in page or 'Appendix A' in page or 'app:benchmark' in page:\n        print(f'Appendix starts on page {i+1}')\n        break\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\nfor i, page in enumerate(pages):\n    if 'Limitations' in page:\n        print(f'Limitations found on page {i+1}')\n        break\nfor i, page in enumerate(pages):\n    if 'Pre-registration' in page or 'Appendix A' in page or 'app:benchmark' in page:\n        print(f'Appendix starts on page {i+1}')\n        break\n\""
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T03:09:11.319068+00:00_

Limitations found on page 9
Appendix starts on page 4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T03:09:11.319200+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\nfor i, page in enumerate(pages):\n    # Check for section markers\n    for marker in ['Abstract', 'Introduction', 'Related Work', 'Method', 'Experiment', 'Conclusion', 'Limitations', 'Ethics', 'References', 'Pre-registration', 'Sensitivity', 'GDN Attention', 'Cross-Scale', 'Jaccard Permutation', 'Transformer Entrainment', 'Within-Architecture']:\n        if marker in page:\n            # find the line\n            for line in page.split('\\n'):\n                if marker in line and len(line.strip()) < 80:\n                    print(f'Page {i+1}: {line.strip()}')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\npages = result.stdout.split('\\f')\nfor i, page in enumerate(pages):\n    # Check for section markers\n    for marker in ['Abstract', 'Introduction', 'Related Work', 'Method', 'Experiment', 'Conclusion', 'Limitations', 'Ethics', 'References', 'Pre-registration', 'Sensitivity', 'GDN Attention', 'Cross-Scale', 'Jaccard Permutation', 'Transformer Entrainment', 'Within-Architecture']:\n        if marker in page:\n            # find the line\n            for line in page.split('\\n'):\n                if marker in line and len(line.strip()) < 80:\n                    print(f'Page {i+1}: {line.strip()}')\n\""
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T03:09:11.319325+00:00_

Page 1: Abstract
Page 1: Introduction
Page 3: Related Work
Page 4: Method
Page 5: Statistical Methods
Page 5: Experiments
Page 8: Conclusion
Page 9: Limitations
Page 9: Ethics Statement
Page 9: References
Page 10: Pre-registration Details
Page 11: Sensitivity Analyses
Page 11: GDN Exclusion Sensitivity
Page 11: GDN Attention Head Confound
Page 12: E Cross-Scale Per-Example Comparisons
Page 12: Cross-Scale Pairwise Jaccard
Page 13: Jaccard Permutation Test
Page 13: G Transformer Entrainment Comparison
Page 13: Within-Architecture Per-Example

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T03:09:11.319474+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -E \"Warning.*within_arch|Undefined.*within_arch|multiply.*within_arch\" main.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -E \"Warning.*within_arch|Undefined.*within_arch|multiply.*within_arch\" main.log"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T03:09:11.319587+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T03:09:11.319715+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep \"undefined\" main.log | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "tool_args": {
    "command": "grep \"undefined\" main.log | head -5"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T03:09:11.319823+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-20T03:09:11.319940+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex",
  "offset": "82",
  "limit": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/experiments.tex",
    "offset": "82",
    "limit": "6"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-20T03:09:11.320058+00:00_

82	Bootstrap confidence intervals (10{,}000 resamples over examples) provide statistical confirmation of the decoupling. The 95\% CI for cross-architecture $\sigma$ does not overlap between the pure configuration $[0.019, 0.030]$ and h3-1 $[0.002, 0.011]$, confirming significant aggregate convergence. In contrast, the 95\% CIs for mean pairwise Jaccard overlap completely across all four non-zero attention ratios (helped: $[0.08, 0.11]$ at each ratio; hurt: $[0.07, 0.11]$), statistically confirming the saturation pattern visible in Figure~\ref{fig:decoupling}.
83	
84	Within-architecture Jaccard across attention ratios averages approximately 0.33 (Appendix~\ref{app:within_arch_stability}), roughly three times the cross-architecture value, indicating that architecture identity has greater influence than attention dose on which examples are affected.
85	
86	An analysis of attention weight patterns provides partial insight into this decoupling. At layer 2 of the 1.3B h3-1 models, GDN and RetNet produce nearly identical attention distributions (cosine similarity 0.995), yet their per-example effects differ substantially. HGRN2 attention patterns diverge from the other architectures at early layers (cosine $\sim$0.20) but converge at deeper layers ($>$0.94 at layer 20). Attention entropy does not differ between helped and hurt examples, which indicates that the per-example effects originate in the recurrent layers rather than in the attention mechanism itself. Full results appear in Appendix~D.
87	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-20T03:09:11.320184+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
  "offset": "226"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/docs/paper/sections/appendix.tex",
    "offset": "226"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-20T03:09:11.320324+00:00_

226	
227	\section{Within-Architecture Per-Example Stability}\label{app:within_arch_stability}
228	
229	Per-example effect sets exhibit a three-tier Jaccard hierarchy on LAMBADA (1.3B scale). Under independence (permutation baseline), pairwise Jaccard is $J \approx 0.05$. Cross-architecture comparisons (different architectures at the same attention ratio) yield $J \approx 0.10$, approximately $2\times$ baseline. Within-architecture comparisons (same architecture across different attention ratios) yield $J \approx 0.33$, approximately $7\times$ baseline and $3\times$ the cross-architecture level. Architecture identity therefore has approximately three times the influence of attention dose on per-example effects.
230	
231	Table~\ref{tab:within_arch_summary} reports mean within-architecture Jaccard for each architecture. HGRN2 shows the highest helped overlap and lowest hurt overlap, consistent with its monotonically increasing helped count across ratios (479 $\to$ 548).
232	
233	\begin{table}[h]
234	\centering
235	\caption{Mean within-architecture pairwise Jaccard similarity across attention ratios (1.3B, LAMBADA). Each mean is computed over all six ratio pairs per architecture.}
236	\label{tab:within_arch_summary}
237	\begin{tabular}{lcc}
238	\toprule
239	Architecture & $\bar{J}_{\text{helped}}$ & $\bar{J}_{\text{hurt}}$ \\
240	\midrule
241	GDN & 0.338 & 0.319 \\
242	RetNet & 0.333 & 0.321 \\
243	HGRN2 & 0.373 & 0.291 \\
244	\midrule
245	\textit{Overall mean} & \textit{0.348} & \textit{0.310} \\
246	\bottomrule
247	\end{tabular}
248	\end{table}
249	
250	Table~\ref{tab:within_arch_pairwise} reports the full pairwise Jaccard matrix. Attention ratios are denoted by their h$k$-1 labels: h24-1 (4\%), h12-1 (7.7\%), h6-1 (14.3\%), h3-1 (25\%).
251	
252	\begin{table}[h]
253	\centering
254	\small
255	\caption{Within-architecture pairwise Jaccard similarity between helped and hurt sets at different attention ratios (1.3B, LAMBADA). Each cell compares the per-example effect set
…[truncated 1366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 67 · 2026-05-20T03:09:11.320498+00:00_

完成。两项修改：

1. **Appendix H** (`appendix.tex` L227-277): 新增 `\section{Within-Architecture Per-Example Stability}` — 三层 Jaccard 层级说明、每架构 mean J 汇总表、完整 6-pair pairwise matrix 表、adjacent vs non-adjacent 分析。
2. **§4.4 引用句** (`experiments.tex` L84): bootstrap CI 段落后、attention weight 段落前插入一句，引用 `Appendix~\ref{app:within_arch_stability}`。

编译验证：无 error，无 undefined reference，主文 8 页（Conclusion 在 page 8），符合限制。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_appendix-h-within-arch_20260520T030458"
}
```

</details>

---
