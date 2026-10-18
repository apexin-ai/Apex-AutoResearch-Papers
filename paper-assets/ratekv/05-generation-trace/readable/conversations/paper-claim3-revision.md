# paper claim3 revision

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_paper_claim3_revision_20260514T204030.jsonl`
- **Structured JSON:** [`c38260a9e5fb2be48602.json`](../../sessions/c3/c38260a9e5fb2be48602.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-14T20:46:28.809268+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T20:46:28.809739+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Heterogeneity Characterization}
5	\label{sec:heterogeneity}
6	
7	The benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.
8	We quantify this with a \emph{top-5\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\% of heads.
9	High concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.
10	
11	Table~\ref{tab:heterogeneity} summarizes the results across five architectures at $4\times$ compression.
12	Qwen2.5-7B exhibits the highest heterogeneity (top-5\% concentration 0.61), with Layer-0 heads contributing the majority of total 2-bit distortion.
13	Constrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\% improvement over uniform 4-bit.
14	Yi-1.5-9B has a concentration of $0.49$---just below the $0.50$ diagnostic threshold---despite having the highest GQA ratio tested (8:1).
15	Its heterogeneity is concentrated in a single extreme outlier (Layer-4 Head-3, contributing 34\% of total delta, CV${=}4.79$), a ``spike'' pattern that MCKP cannot exploit because the freed budget from one 2-bit head is insufficient to upgrade others meaningfully.
16	In contrast, Qwen's Layer-0 cluster of 4 heads ($26\times$ dominance ratio) forms a ``spread'' pattern that enables differentiated allocation across multiple heads.
17	Yi-1.5's constrained MCKP is \emph{worse} than uniform ($+$0.30 vs.\ $+$0.20), a genuine negative result.
18	Llama-3.1-8B shows moderate heterogeneity (0.34--0.59), and the allocation benefit is marginal ($+$0.36 vs.\ $+$0.38).
19	Mistral-7B-v0.3 has a concentration of 0.42 but near-zero absolute distortion for most heads, leaving the profiler with no reliable signal.
20	Here, constrained MCKP is slightly \emph{worse} than uniform ($+$0.13 vs.\ $+$0.10), confirmi
…[truncated 3997 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T20:46:28.810033+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T20:46:28.810254+00:00_

1	Per-head mixed-precision quantization of the KV cache promises lower perplexity than uniform quantization at the same average bit-width, but on hardware-aligned bit-widths $\{2, 4, 8, 16\}$, existing solvers fail catastrophically: unconstrained greedy and MCKP allocation achieve 32.45 and 36.92 perplexity on Qwen2.5-7B---far worse than uniform 4-bit (15.45).
2	We trace this failure to \emph{2-bit distortion compounding}: when the majority of heads are assigned 2-bit precision, per-head quantization errors interact non-additively through the residual stream, violating the additive objective assumed by standard solvers.
3	We show that a single cardinality constraint capping the number of 2-bit assignments is a minimal sufficient fix.
4	On Qwen2.5-7B at $4\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\% reduction over uniform 4-bit.
5	The constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures ($\Delta{=}0.0000$), enabling use of a simple $O(H \log H)$ greedy algorithm; per-layer brute-force oracle confirms near-optimality (max gap 0.02 PPL).
6	However, the benefit depends on architecture: on Llama-3.1-8B the improvement is marginal (8.45 vs.\ 8.47), and on Mistral-7B-v0.3, Yi-1.5-9B, and Gemma-2-9B non-uniform allocation is counterproductive.
7	Notably, Yi-1.5-9B has the highest GQA ratio tested (8:1) yet degrades by 1.3\%, showing that the distribution shape of head sensitivity, not GQA ratio alone, determines the benefit.
8	We propose a heterogeneity diagnostic based on the concentration of per-head sensitivity, validated on five architectures, that can indicate before any allocation whether a given architecture will benefit from non-uniform quantization.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T20:46:28.810479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T20:46:28.810745+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Per-head mixed-precision quantization of the KV cache is a natural strategy for reducing memory during LLM inference: assign fewer bits to insensitive heads and more bits to sensitive ones, achieving lower perplexity than uniform quantization at the same average bit-width.
5	Recent work on KV cache quantization explores both uniform schemes~\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\cite{zhang2023h2o,li2024snapkv}.
6	RateQuant~\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\{2,3,4,5,6\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).
7	
8	In practice, hardware-efficient inference requires bit-widths drawn from $\{2, 4, 8, 16\}$---the formats natively supported by modern accelerators.
9	On this non-consecutive set, the polymatroid structure breaks down, and greedy is no longer provably optimal.
10	One might expect that exact MCKP solvers would fill this gap.
11	They do not.
12	On Qwen2.5-7B at $4\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \emph{far worse} than uniform 4-bit (15.45).
13	The optimization does not merely underperform; it fails catastrophically.
14	
15	The root cause is not solver suboptimality but a violation of the objective's additive distortion assumption.
16	Both solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors are large enough to compound through the residual stream.
17	The additive model predicts $\sim$11 PPL for these allocations; the actual PPL is $3$--$4\times$ higher.
18	At 4-bit and above, per-head distortions are small and compound negligibly---uniform 4-bit achieves clos
…[truncated 4585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T20:46:28.810974+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T20:46:28.811189+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We showed that per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \{2, 4, 8, 16\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding through the residual stream.
4	A single constraint---limiting simultaneously active 2-bit heads to $k \leq 8$ (7\% of heads)---reduces perplexity on Qwen2.5-7B from 15.45 (uniform 4-bit) to 11.23, a 27.3\% improvement at $4\times$ compression.
5	Under the constraint, solver choice becomes irrelevant: greedy and MCKP produce equivalent allocations across all three architectures ($\Delta = 0.0000$), so a simple $O(H \log H)$ greedy algorithm suffices.
6	The benefit of non-uniform allocation scales with head sensitivity heterogeneity, as measured by the top-5\% concentration diagnostic: Qwen2.5-7B (concentration 0.61) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\ 8.47 PPL), while Mistral-7B-v0.3 (0.42), Yi-1.5-9B (0.49), and Gemma-2-9B (0.23) are counterproductive.
7	Yi-1.5-9B is a particularly instructive case: despite the highest GQA ratio tested (8:1), its sensitivity heterogeneity is a single-outlier spike rather than a spread, placing it just below the $0.50$ diagnostic threshold.
8	This diagnostic, computable from the same profiling pass used for allocation, lets practitioners decide \emph{before deployment} whether non-uniform quantization is worthwhile for a given model.
9	
10	\paragraph{Limitations.}
11	Our study has several limitations that temper the generality of the findings.
12	First, we evaluate only five 7--9B-scale models---too few to establish a statistically robust correlation between heterogeneity and quantization benefit; the observed trend is directional evidence, not a predictive law.
13	Second, profiling relies on a single sensitivity metric (perplexity-based per-head distortion); alternative measures such as gradient-based or activation-norm diagnost
…[truncated 955 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T20:46:28.811448+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "placeholder",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Grep",
  "tool_args": {
    "pattern": "placeholder",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T20:46:28.811627+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T20:46:28.811842+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T20:46:28.812032+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{amsmath}
6	\usepackage{amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{enumitem}
10	
11	\title{When Does Non-Uniform KV Cache Quantization Help?\\Cardinality Constraints and a Heterogeneity Diagnostic}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	\begin{abstract}
19	\input{abstract}
20	\end{abstract}
21	
22	\input{introduction}
23	\input{related_work}
24	\input{method}
25	\input{experiments}
26	\input{analysis}
27	\input{conclusion}
28	
29	\bibliography{references}
30	
31	\input{appendix}
32	
33	\end{document}
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T20:46:28.812444+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T20:46:28.812819+00:00_

1	\appendix
2	
3	\section{Aggressive Compression}
4	\label{sec:aggressive}
5	
6	At $4\times$ compression, Llama and Mistral show minimal benefit from non-uniform allocation.
7	At more aggressive ratios, the picture changes: at $5.3\times$ (average 3 bits), constrained MCKP achieves $45\times$ lower PPL than uniform on Llama (57.60 vs.\ 2643.77) and $44\times$ on Mistral (11.91 vs.\ 519.11), because the constraint protects sensitive heads from 2-bit assignment.
8	At $8\times$, the budget is too constrained for any allocation to preserve quality (both methods degrade catastrophically).
9	The intermediate regime ($5.3\times$) provides the largest relative benefit.
10	
11	\section{Profiling Resolution and Stability}
12	\label{sec:profiling_resolution}
13	
14	We compare standard-resolution profiling (16 sequences $\times$ 512 tokens) against high-resolution profiling (64 sequences $\times$ 2048 tokens) on Qwen2.5-7B at $4\times$ compression.
15	
16	High-resolution profiling improves constrained MCKP from 11.23 to 10.91 PPL ($-$0.32 absolute).
17	Relative to the bf16 baseline (9.81), this reduces the degradation from 1.42 to 1.10, a 22.5\% reduction.
18	The improvement comes from finer-grained sensitivity estimates: standard profiling detects non-zero 2-bit distortion in 37 of 112 heads, while high-resolution profiling detects 100 of 112 (2.7$\times$ more).
19	
20	The additional signal changes 8 of 112 head assignments.
21	High-resolution profiling protects shallow layers (L1--L3) at higher bit-widths while compressing mid-layers (L5--L11) more aggressively---a redistribution that standard profiling misses because its distortion estimates for these heads fall below the noise floor.
22	
23	\paragraph{Multi-seed stability.}
24	The profiled allocation is stable across calibration subsets.
25	Under hires profiling on Qwen2.5-7B, constrained MCKP yields mean PPL $10.99 \pm 0.06$ across 3 random calibration seeds (individual runs: 11.02, 10.90, 11.05), with std/mean below 0.6\%
…[truncated 5106 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T20:46:28.813060+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex",
  "old_string": "Notably, Yi-1.5-9B has the highest GQA ratio tested (8:1) yet degrades by 1.3\\%, showing that the distribution shape of head sensitivity, not GQA ratio alone, determines the benefit.\nWe propose a heterogeneity diagnostic based on the concentration of per-head sensitivity, validated on five architectures, that can indicate before any allocation whether a given architecture will benefit from non-uniform quantization.",
  "new_string": "Notably, Yi-1.5-9B has the highest GQA ratio tested (8:1) and the highest top-5\\% concentration (0.71), yet degrades under non-uniform allocation---because its heterogeneity is a single-outlier ``spike'' with no cross-bitwidth sensitivity gradient, rather than the ``spread'' pattern that enables MCKP to redistribute budget across heads.\nWe propose a joint heterogeneity diagnostic combining concentration and distribution shape, validated on five architectures, that can indicate before any allocation whether a given architecture will benefit from non-uniform quantization."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex",
    "old_string": "Notably, Yi-1.5-9B has the highest GQA ratio tested (8:1) yet degrades by 1.3\\%, showing that the distribution shape of head sensitivity, not GQA ratio alone, determines the benefit.\nWe propose a heterogeneity diagnostic based on the concentration of per-head sensitivity, validated on five architectures, that can indicate before any allocation whether a given architecture will benefit from non-uniform quantization.",
    "new_string": "Notably, Yi-1.5-9B has the highest GQA ratio tested (8:1) and the highest top-5\\% concentration (0.71), yet degrades under non-uniform allocation---because its heterogeneity is a single-outlier ``spike'' with no cross-bitwidth sensitivity gradient, rather than the ``spread'' pattern that enables MCKP to redistribute budget across heads.\nWe propose a joint heterogeneity diagnostic combining concentration and distribution shape, validated on five architectures, that can indicate before any allocation whether a given architecture will benefit from non-uniform quantization."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T20:46:28.813221+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T20:46:28.813354+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex",
  "old_string": "We propose a heterogeneity diagnostic based on the top-5\\% concentration of per-head distortion (\\S\\ref{sec:heterogeneity}).\nOn our five architectures, the concentration metric---combined with the absolute magnitude of per-head distortion---separates the beneficial case (Qwen, concentration 0.61, 27.3\\% PPL improvement) from cases where non-uniform allocation provides marginal (Llama) or no benefit (Mistral, Yi-1.5, Gemma-2).\nYi-1.5 (concentration 0.49) falls just below the $0.50$ threshold and is correctly classified as negative despite its high GQA ratio.",
  "new_string": "We propose a joint heterogeneity diagnostic based on concentration \\emph{and} distribution shape of per-head distortion (\\S\\ref{sec:heterogeneity}).\nOn our five architectures, the diagnostic separates the beneficial case (Qwen, concentration 0.61, spread pattern) from cases where non-uniform allocation provides marginal or no benefit.\nYi-1.5 is a critical test: its concentration ($0.71$) exceeds Qwen's, but its heterogeneity is a single-outlier spike with no cross-bitwidth gradient---precisely the pattern where MCKP cannot redistribute budget."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex",
    "old_string": "We propose a heterogeneity diagnostic based on the top-5\\% concentration of per-head distortion (\\S\\ref{sec:heterogeneity}).\nOn our five architectures, the concentration metric---combined with the absolute magnitude of per-head distortion---separates the beneficial case (Qwen, concentration 0.61, 27.3\\% PPL improvement) from cases where non-uniform allocation provides marginal (Llama) or no benefit (Mistral, Yi-1.5, Gemma-2).\nYi-1.5 (concentration 0.49) falls just below the $0.50$ threshold and is correctly classified as negative despite its high GQA ratio.",
    "new_string": "We propose a joint heterogeneity diagnostic based on concentration \\emph{and} distribution shape of per-head distortion (\\S\\ref{sec:heterogeneity}).\nOn our five architectures, the diagnostic separates the beneficial case (Qwen, concentration 0.61, spread pattern) from cases where non-uniform allocation provides marginal or no benefit.\nYi-1.5 is a critical test: its concentration ($0.71$) exceeds Qwen's, but its heterogeneity is a single-outlier spike with no cross-bitwidth gradient---precisely the pattern where MCKP cannot redistribute budget."
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T20:46:28.813520+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T20:46:28.813683+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex",
  "old_string": "\\item We propose a heterogeneity-based diagnostic framework that can indicate whether non-uniform allocation will help a given architecture, validated on five models spanning beneficial, marginal, and counterproductive outcomes (\\S\\ref{sec:heterogeneity}).",
  "new_string": "\\item We propose a joint diagnostic combining concentration and distribution shape ($t_1/t_5$ ratio) to indicate whether non-uniform allocation will help a given architecture, distinguishing ``spread'' heterogeneity (MCKP-exploitable) from ``spike'' and ``flat'' patterns, validated on five models (\\S\\ref{sec:heterogeneity})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex",
    "old_string": "\\item We propose a heterogeneity-based diagnostic framework that can indicate whether non-uniform allocation will help a given architecture, validated on five models spanning beneficial, marginal, and counterproductive outcomes (\\S\\ref{sec:heterogeneity}).",
    "new_string": "\\item We propose a joint diagnostic combining concentration and distribution shape ($t_1/t_5$ ratio) to indicate whether non-uniform allocation will help a given architecture, distinguishing ``spread'' heterogeneity (MCKP-exploitable) from ``spike'' and ``flat'' patterns, validated on five models (\\S\\ref{sec:heterogeneity})."
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T20:46:28.813864+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T20:46:28.813994+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex",
  "old_string": "The benefit of non-uniform allocation scales with head sensitivity heterogeneity, as measured by the top-5\\% concentration diagnostic: Qwen2.5-7B (concentration 0.61) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\\ 8.47 PPL), while Mistral-7B-v0.3 (0.42), Yi-1.5-9B (0.49), and Gemma-2-9B (0.23) are counterproductive.\nYi-1.5-9B is a particularly instructive case: despite the highest GQA ratio tested (8:1), its sensitivity heterogeneity is a single-outlier spike rather than a spread, placing it just below the $0.50$ diagnostic threshold.\nThis diagnostic, computable from the same profiling pass used for allocation, lets practitioners decide \\emph{before deployment} whether non-uniform quantization is worthwhile for a given model.",
  "new_string": "The benefit of non-uniform allocation depends on both the concentration and \\emph{shape} of head sensitivity heterogeneity.\nQwen2.5-7B (concentration 0.61, $t_1/t_5{=}0.57$, spread pattern) shows large gains; Llama-3.1-8B ($t_1/t_5{=}0.71$, spike) shows marginal improvement (8.45 vs.\\ 8.47 PPL); Mistral-7B-v0.3, Yi-1.5-9B, and Gemma-2-9B are counterproductive.\nYi-1.5-9B is a critical test case: despite the highest concentration tested ($0.71$, exceeding Qwen), its heterogeneity is a single-outlier spike ($t_1/t_5{=}0.90$) with no cross-bitwidth sensitivity gradient, so MCKP cannot redistribute budget.\nA joint diagnostic using concentration and $t_1/t_5$ ratio distinguishes spread, spike, and flat patterns across our five models, computable from the same profiling pass used for allocation, letting practitioners decide \\emph{before deployment} whether non-uniform quantization is worthwhile."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex",
    "old_string": "The benefit of non-uniform allocation scales with head sensitivity heterogeneity, as measured by the top-5\\% concentration diagnostic: Qwen2.5-7B (concentration 0.61) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\\ 8.47 PPL), while Mistral-7B-v0.3 (0.42), Yi-1.5-9B (0.49), and Gemma-2-9B (0.23) are counterproductive.\nYi-1.5-9B is a particularly instructive case: despite the highest GQA ratio tested (8:1), its sensitivity heterogeneity is a single-outlier spike rather than a spread, placing it just below the $0.50$ diagnostic threshold.\nThis diagnostic, computable from the same profiling pass used for allocation, lets practitioners decide \\emph{before deployment} whether non-uniform quantization is worthwhile for a given model.",
    "new_string": "The benefit of non-uniform allocation depends on both the concentration and \\emph{shape} of head sensitivity heterogeneity.\nQwen2.5-7B (concentration 0.61, $t_1/t_5{=}0.57$, spread pattern) shows large gains; Llama-3.1-8B ($t_1/t_5{=}0.71$, spike) shows marginal improvement (8.45 vs.\\ 8.47 PPL); Mistral-7B-v0.3, Yi-1.5-9B, and Gemma-2-9B are counterproductive.\nYi-1.5-9B is a critical test case: despite the highest concentration tested ($0.71$, exceeding Qwen), its heterogeneity is a single-outlier spike ($t_1/t_5{=}0.90$) with no cross-bitwidth sensitivity gradient, so MCKP cannot redistribute budget.\nA joint diagnostic using concentration and $t_1/t_5$ ratio distinguishes spread, spike, and flat patterns across our five models, computable from the same profiling pass used for allocation, letting practitioners decide \\emph{before deployment} whether non-uniform quantization is worthwhile."
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T20:46:28.814156+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T20:46:28.814314+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
  "old_string": "Table~\\ref{tab:heterogeneity} summarizes the results across five architectures at $4\\times$ compression.\nQwen2.5-7B exhibits the highest heterogeneity (top-5\\% concentration 0.61), with Layer-0 heads contributing the majority of total 2-bit distortion.\nConstrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\\% improvement over uniform 4-bit.\nYi-1.5-9B has a concentration of $0.49$---just below the $0.50$ diagnostic threshold---despite having the highest GQA ratio tested (8:1).\nIts heterogeneity is concentrated in a single extreme outlier (Layer-4 Head-3, contributing 34\\% of total delta, CV${=}4.79$), a ``spike'' pattern that MCKP cannot exploit because the freed budget from one 2-bit head is insufficient to upgrade others meaningfully.\nIn contrast, Qwen's Layer-0 cluster of 4 heads ($26\\times$ dominance ratio) forms a ``spread'' pattern that enables differentiated allocation across multiple heads.\nYi-1.5's constrained MCKP is \\emph{worse} than uniform ($+$0.30 vs.\\ $+$0.20), a genuine negative result.\nLlama-3.1-8B shows moderate heterogeneity (0.34--0.59), and the allocation benefit is marginal ($+$0.36 vs.\\ $+$0.38).\nMistral-7B-v0.3 has a concentration of 0.42 but near-zero absolute distortion for most heads, leaving the profiler with no reliable signal.\nHere, constrained MCKP is slightly \\emph{worse} than uniform ($+$0.13 vs.\\ $+$0.10), confirming that non-uniform allocation is counterproductive when heterogeneity is low.\nGemma-2-9B has the lowest heterogeneity ($0.23$), consistent with its low GQA ratio (2:1) and attention logit softcapping.\nConstrained MCKP degrades by $+$0.15 vs.\\ $+$0.13 for uniform, the strongest negative anchor in our evaluation.",
  "new_string": "Table~\\ref{tab:heterogeneity} summarizes the results across five architectures at $4\\times$ compression.\nQwen2.5-7B exhibits the highest \\emph{spread} heterogeneity (top-5\\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.\nConstrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\\% improvement over uniform 4-bit. %exp_id=qwen_constrained_mckp\n\nHowever, concentration alone does not predict MCKP benefit.\nYi-1.5-9B has a hires concentration of $0.71$---\\emph{higher} than Qwen's $0.61$---yet constrained MCKP is counterproductive ($+$0.30 vs.\\ $+$0.20 uniform). %exp_id=yi15_hires_constrained\nThe explanation lies in the \\emph{shape} of the heterogeneity.\nYi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 has a 2-bit delta of 13.12, while the second-ranked head has delta 0.55---a $24\\times$ gap ($t_1/t_5{=}0.90$, $t_1/t_2{=}23.7$). %exp_id=yi15_hires_profiling\nCritically, L4H3's sensitivity is confined to the 2-bit operating point: its 4-bit and 8-bit deltas are ${\\approx}\\,0$.\nThe solver therefore has no cross-bitwidth gradient to exploit---upgrading L4H3 from 2-bit to 4-bit removes the distortion, but further upgrading to 8-bit provides no additional benefit, so the budget freed by downgrading other heads has nowhere useful to go.\nWe call this a ``spike'' pattern: high concentration, but a single outlier with sensitivity at only one bitwidth.\n\nIn contrast, Qwen's Layer-0 heads exhibit non-zero deltas at multiple bitwidths (e.g., L0H0: 2-bit delta ${=}6.74$, with positive 4-bit and 8-bit deltas), giving the solver a multi-bitwidth sensitivity gradient across several heads---a ``spread'' pattern that enables meaningful budget reallocation. %exp_id=qwen_hires_profiling\n\nThe remaining three architectures fill out the diagnostic picture.\nLlama-3.1-8B shows moderate concentration ($0.34$) with a spike-like shape ($t_1/t_5{=}0.71$, $t_1/t_2{=}21.7$); its allocation benefit is marginal ($+$0.36 vs.\\ $+$0.38 uniform). %exp_id=llama_hires_constrained\nMistral-7B-v0.3 and Gemma-2-9B both exhibit flat distributions ($t_1/t_5{=}0.18$) with low concentration ($0.22$ and $0.23$ respectively), leaving the profiler with no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\\ $+$0.10 for Mistral; $+$0.15 vs.\\ $+$0.13 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
    "old_string": "Table~\\ref{tab:heterogeneity} summarizes the results across five architectures at $4\\times$ compression.\nQwen2.5-7B exhibits the highest heterogeneity (top-5\\% concentration 0.61), with Layer-0 heads contributing the majority of total 2-bit distortion.\nConstrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\\% improvement over uniform 4-bit.\nYi-1.5-9B has a concentration of $0.49$---just below the $0.50$ diagnostic threshold---despite having the highest GQA ratio tested (8:1).\nIts heterogeneity is concentrated in a single extreme outlier (Layer-4 Head-3, contributing 34\\% of total delta, CV${=}4.79$), a ``spike'' pattern that MCKP cannot exploit because the freed budget from one 2-bit head is insufficient to upgrade others meaningfully.\nIn contrast, Qwen's Layer-0 cluster of 4 heads ($26\\times$ dominance ratio) forms a ``spread'' pattern that enables differentiated allocation across multiple heads.\nYi-1.5's constrained MCKP is \\emph{worse} than uniform ($+$0.30 vs.\\ $+$0.20), a genuine negative result.\nLlama-3.1-8B shows moderate heterogeneity (0.34--0.59), and the allocation benefit is marginal ($+$0.36 vs.\\ $+$0.38).\nMistral-7B-v0.3 has a concentration of 0.42 but near-zero absolute distortion for most heads, leaving the profiler with no reliable signal.\nHere, constrained MCKP is slightly \\emph{worse} than uniform ($+$0.13 vs.\\ $+$0.10), confirming that non-uniform allocation is counterproductive when heterogeneity is low.\nGemma-2-9B has the lowest heterogeneity ($0.23$), consistent with its low GQA ratio (2:1) and attention logit softcapping.\nConstrained MCKP degrades by $+$0.15 vs.\\ $+$0.13 for uniform, the strongest negative anchor in our evaluation.",
    "new_string": "Table~\\ref{tab:heterogeneity} summarizes the results across five architectures at $4\\times$ compression.\nQwen2.5-7B exhibits the highest \\emph{spread} heterogeneity (top-5\\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.\nConstrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\\% improvement over uniform 4-bit. %exp_id=qwen_constrained_mckp\n\nHowever, concentration alone does not predict MCKP benefit.\nYi-1.5-9B has a hires concentration of $0.71$---\\emph{higher} than Qwen's $0.61$---yet constrained MCKP is counterproductive ($+$0.30 vs.\\ $+$0.20 uniform). %exp_id=yi15_hires_constrained\nThe explanation lies in the \\emph{shape} of the heterogeneity.\nYi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 has a 2-bit delta of 13.12, while the second-ranked head has delta 0.55---a $24\\times$ gap ($t_1/t_5{=}0.90$, $t_1/t_2{=}23.7$). %exp_id=yi15_hires_profiling\nCritically, L4H3's sensitivity is confined to the 2-bit operating point: its 4-bit and 8-bit deltas are ${\\approx}\\,0$.\nThe solver therefore has no cross-bitwidth gradient to exploit---upgrading L4H3 from 2-bit to 4-bit removes the distortion, but further upgrading to 8-bit provides no additional benefit, so the budget freed by downgrading other heads has nowhere useful to go.\nWe call this a ``spike'' pattern: high concentration, but a single outlier with sensitivity at only one bitwidth.\n\nIn contrast, Qwen's Layer-0 heads exhibit non-zero deltas at multiple bitwidths (e.g., L0H0: 2-bit delta ${=}6.74$, with positive 4-bit and 8-bit deltas), giving the solver a multi-bitwidth sensitivity gradient across several heads---a ``spread'' pattern that enables meaningful budget reallocation. %exp_id=qwen_hires_profiling\n\nThe remaining three architectures fill out the diagnostic picture.\nLlama-3.1-8B shows moderate concentration ($0.34$) with a spike-like shape ($t_1/t_5{=}0.71$, $t_1/t_2{=}21.7$); its allocation benefit is marginal ($+$0.36 vs.\\ $+$0.38 uniform). %exp_id=llama_hires_constrained\nMistral-7B-v0.3 and Gemma-2-9B both exhibit flat distributions ($t_1/t_5{=}0.18$) with low concentration ($0.22$ and $0.23$ respectively), leaving the profiler with no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\\ $+$0.10 for Mistral; $+$0.15 vs.\\ $+$0.13 for Gemma-2). %exp_id=mistral_c4_cross_dataset %exp_id=gemma2_full_pipeline"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T20:46:28.814517+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T20:46:28.814670+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
  "old_string": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at 4$\\times$ compression. $^\\dagger$Hires profiling (64 seq $\\times$ 2048 tok).}\n\\label{tab:heterogeneity}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & GQA & Top-5\\% & $\\Delta$ PPL & $\\Delta$ PPL & Recommendation \\\\\n & Ratio & Conc. & (Uniform) & (Ours) & \\\\\n\\midrule\nQwen2.5-7B & 7:1 & 0.61 & $+$5.64 & $+$1.42 & Non-uniform \\\\\nYi-1.5-9B & 8:1 & 0.49 & $+$0.20 & $+$0.30 & Uniform \\\\\nLlama-3.1-8B$^\\dagger$ & 4:1 & 0.34--0.59 & $+$0.38 & $+$0.36 & Marginal \\\\\nMistral-7B-v0.3$^\\dagger$ & 4:1 & 0.42 & $+$0.10 & $+$0.13 & Uniform \\\\\nGemma-2-9B & 2:1 & 0.23 & $+$0.13 & $+$0.15 & Uniform \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
  "new_string": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at $4\\times$ compression. $t_1/t_5$: ratio of top-1 to top-5 per-head 2-bit distortion (low${=}$spread, high${=}$spike). $^\\dagger$Hires profiling (64 seq $\\times$ 2048 tok); $^\\ddagger$standard profiling, hires pending.}\n\\label{tab:heterogeneity}\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & GQA & Top-5\\% & $t_1/t_5$ & $\\Delta$ PPL & $\\Delta$ PPL & Shape \\\\\n & Ratio & Conc. & & (Uniform) & (Ours) & \\\\\n\\midrule\nQwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.42 & Spread \\\\\nYi-1.5-9B$^\\dagger$ & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.30 & Spike \\\\\nLlama-3.1-8B$^\\ddagger$ & 4:1 & 0.34 & 0.71 & $+$0.38 & $+$0.36 & Spike \\\\\nMistral-7B-v0.3$^\\ddagger$ & 4:1 & 0.22 & 0.18 & $+$0.10 & $+$0.13 & Flat \\\\\nGemma-2-9B$^\\ddagger$ & 2:1 & 0.23 & 0.18 & $+$0.13 & $+$0.15 & Flat \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
    "old_string": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at 4$\\times$ compression. $^\\dagger$Hires profiling (64 seq $\\times$ 2048 tok).}\n\\label{tab:heterogeneity}\n\\begin{tabular}{lccccc}\n\\toprule\nModel & GQA & Top-5\\% & $\\Delta$ PPL & $\\Delta$ PPL & Recommendation \\\\\n & Ratio & Conc. & (Uniform) & (Ours) & \\\\\n\\midrule\nQwen2.5-7B & 7:1 & 0.61 & $+$5.64 & $+$1.42 & Non-uniform \\\\\nYi-1.5-9B & 8:1 & 0.49 & $+$0.20 & $+$0.30 & Uniform \\\\\nLlama-3.1-8B$^\\dagger$ & 4:1 & 0.34--0.59 & $+$0.38 & $+$0.36 & Marginal \\\\\nMistral-7B-v0.3$^\\dagger$ & 4:1 & 0.42 & $+$0.10 & $+$0.13 & Uniform \\\\\nGemma-2-9B & 2:1 & 0.23 & $+$0.13 & $+$0.15 & Uniform \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
    "new_string": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at $4\\times$ compression. $t_1/t_5$: ratio of top-1 to top-5 per-head 2-bit distortion (low${=}$spread, high${=}$spike). $^\\dagger$Hires profiling (64 seq $\\times$ 2048 tok); $^\\ddagger$standard profiling, hires pending.}\n\\label{tab:heterogeneity}\n\\begin{tabular}{lcccccc}\n\\toprule\nModel & GQA & Top-5\\% & $t_1/t_5$ & $\\Delta$ PPL & $\\Delta$ PPL & Shape \\\\\n & Ratio & Conc. & & (Uniform) & (Ours) & \\\\\n\\midrule\nQwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.42 & Spread \\\\\nYi-1.5-9B$^\\dagger$ & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.30 & Spike \\\\\nLlama-3.1-8B$^\\ddagger$ & 4:1 & 0.34 & 0.71 & $+$0.38 & $+$0.36 & Spike \\\\\nMistral-7B-v0.3$^\\ddagger$ & 4:1 & 0.22 & 0.18 & $+$0.10 & $+$0.13 & Flat \\\\\nGemma-2-9B$^\\ddagger$ & 2:1 & 0.23 & 0.18 & $+$0.13 & $+$0.15 & Flat \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T20:46:28.814851+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T20:46:28.814985+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
  "old_string": "The heterogeneity characterization yields a preliminary guideline, based on five architectures, for deciding when non-uniform allocation is worthwhile:\n\n\\begin{enumerate}[nosep]\n\\item Run per-head profiling as described in \\S\\ref{sec:profiling}.\n\\item Compute the top-5\\% concentration from the resulting distortion table.\n\\item Select allocation strategy:\n  \\begin{itemize}[nosep]\n  \\item Concentration ${>}\\,0.50$: non-uniform allocation recommended (Qwen; 27.3\\% PPL improvement).\n  \\item Concentration $0.30$--$0.50$: marginal or negative; benefit depends on distribution shape. Llama (0.34--0.59) shows 0.2\\% improvement at $4\\times$; Mistral (0.42) and Yi-1.5 (0.49) are counterproductive despite Yi-1.5 having GQA 8:1.\n  \\item Concentration ${<}\\,0.30$: use uniform (Gemma-2, 0.23; non-uniform is counterproductive).\n  \\end{itemize}\n\\end{enumerate}\n\nThe diagnostic adds no computational overhead: it reuses the profiling data already required for the allocation solver.\nThis avoids wasted optimization effort on architectures where non-uniform allocation provides no benefit.\nThe thresholds above are derived from five architectures and correctly classify all five models (1 positive, 1 marginal, 3 negative), but should be validated on a broader set before being treated as general rules.\nAdditional analyses---the effect of aggressive compression ratios, profiling resolution and multi-seed stability, per-layer optimality validation, and KV separation ablation---are provided in Appendices~\\ref{sec:aggressive}--\\ref{sec:kv_separation}.",
  "new_string": "The heterogeneity characterization shows that MCKP benefit requires not just high concentration but a specific \\emph{shape}---spread heterogeneity across multiple heads with cross-bitwidth sensitivity gradients.\nThis motivates a joint diagnostic, based on five architectures, for deciding when non-uniform allocation is worthwhile:\n\n\\begin{enumerate}[nosep]\n\\item Run per-head profiling as described in \\S\\ref{sec:profiling}.\n\\item Compute the top-5\\% concentration and the $t_1/t_5$ ratio (top-1 distortion divided by top-5 distortion) from the resulting distortion table.\n\\item Select allocation strategy based on concentration \\emph{and} shape:\n  \\begin{itemize}[nosep]\n  \\item \\textbf{Spread} (moderate-to-high concentration, $t_1/t_5 \\lesssim 0.70$): non-uniform allocation recommended. Multiple heads have sensitivity gradients across bitwidths, giving the solver room to redistribute budget. Qwen (0.61, $t_1/t_5{=}0.57$): 27.3\\% PPL improvement.\n  \\item \\textbf{Spike} (any concentration, $t_1/t_5 \\gtrsim 0.70$): use uniform. Sensitivity is confined to a single outlier with no cross-bitwidth gradient; the solver cannot exploit it. Yi-1.5 (0.71, $t_1/t_5{=}0.90$) and Llama (0.34, $t_1/t_5{=}0.71$): counterproductive or marginal.\n  \\item \\textbf{Flat} (low concentration, any shape): use uniform. Near-uniform sensitivity provides no signal for differentiated allocation. Mistral ($t_1/t_5{=}0.18$) and Gemma-2 ($t_1/t_5{=}0.18$): counterproductive.\n  \\end{itemize}\n\\end{enumerate}\n\nThe $t_1/t_5 \\approx 0.70$ boundary is an illustrative threshold derived from five architectures; it should be validated on a broader set before being treated as a general rule.\nThe diagnostic adds no computational overhead: it reuses the profiling data already required for the allocation solver and avoids wasted optimization effort on architectures where non-uniform allocation provides no benefit.\nAdditional analyses---the effect of aggressive compression ratios, profiling resolution and multi-seed stability, per-layer optimality validation, and KV separation ablation---are provided in Appendices~\\ref{sec:aggressive}--\\ref{sec:kv_separation}."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
    "old_string": "The heterogeneity characterization yields a preliminary guideline, based on five architectures, for deciding when non-uniform allocation is worthwhile:\n\n\\begin{enumerate}[nosep]\n\\item Run per-head profiling as described in \\S\\ref{sec:profiling}.\n\\item Compute the top-5\\% concentration from the resulting distortion table.\n\\item Select allocation strategy:\n  \\begin{itemize}[nosep]\n  \\item Concentration ${>}\\,0.50$: non-uniform allocation recommended (Qwen; 27.3\\% PPL improvement).\n  \\item Concentration $0.30$--$0.50$: marginal or negative; benefit depends on distribution shape. Llama (0.34--0.59) shows 0.2\\% improvement at $4\\times$; Mistral (0.42) and Yi-1.5 (0.49) are counterproductive despite Yi-1.5 having GQA 8:1.\n  \\item Concentration ${<}\\,0.30$: use uniform (Gemma-2, 0.23; non-uniform is counterproductive).\n  \\end{itemize}\n\\end{enumerate}\n\nThe diagnostic adds no computational overhead: it reuses the profiling data already required for the allocation solver.\nThis avoids wasted optimization effort on architectures where non-uniform allocation provides no benefit.\nThe thresholds above are derived from five architectures and correctly classify all five models (1 positive, 1 marginal, 3 negative), but should be validated on a broader set before being treated as general rules.\nAdditional analyses---the effect of aggressive compression ratios, profiling resolution and multi-seed stability, per-layer optimality validation, and KV separation ablation---are provided in Appendices~\\ref{sec:aggressive}--\\ref{sec:kv_separation}.",
    "new_string": "The heterogeneity characterization shows that MCKP benefit requires not just high concentration but a specific \\emph{shape}---spread heterogeneity across multiple heads with cross-bitwidth sensitivity gradients.\nThis motivates a joint diagnostic, based on five architectures, for deciding when non-uniform allocation is worthwhile:\n\n\\begin{enumerate}[nosep]\n\\item Run per-head profiling as described in \\S\\ref{sec:profiling}.\n\\item Compute the top-5\\% concentration and the $t_1/t_5$ ratio (top-1 distortion divided by top-5 distortion) from the resulting distortion table.\n\\item Select allocation strategy based on concentration \\emph{and} shape:\n  \\begin{itemize}[nosep]\n  \\item \\textbf{Spread} (moderate-to-high concentration, $t_1/t_5 \\lesssim 0.70$): non-uniform allocation recommended. Multiple heads have sensitivity gradients across bitwidths, giving the solver room to redistribute budget. Qwen (0.61, $t_1/t_5{=}0.57$): 27.3\\% PPL improvement.\n  \\item \\textbf{Spike} (any concentration, $t_1/t_5 \\gtrsim 0.70$): use uniform. Sensitivity is confined to a single outlier with no cross-bitwidth gradient; the solver cannot exploit it. Yi-1.5 (0.71, $t_1/t_5{=}0.90$) and Llama (0.34, $t_1/t_5{=}0.71$): counterproductive or marginal.\n  \\item \\textbf{Flat} (low concentration, any shape): use uniform. Near-uniform sensitivity provides no signal for differentiated allocation. Mistral ($t_1/t_5{=}0.18$) and Gemma-2 ($t_1/t_5{=}0.18$): counterproductive.\n  \\end{itemize}\n\\end{enumerate}\n\nThe $t_1/t_5 \\approx 0.70$ boundary is an illustrative threshold derived from five architectures; it should be validated on a broader set before being treated as a general rule.\nThe diagnostic adds no computational overhead: it reuses the profiling data already required for the allocation solver and avoids wasted optimization effort on architectures where non-uniform allocation provides no benefit.\nAdditional analyses---the effect of aggressive compression ratios, profiling resolution and multi-seed stability, per-layer optimality validation, and KV separation ablation---are provided in Appendices~\\ref{sec:aggressive}--\\ref{sec:kv_separation}."
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T20:46:28.815185+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T20:46:28.815327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T20:46:28.815490+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Heterogeneity Characterization}
5	\label{sec:heterogeneity}
6	
7	The benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.
8	We quantify this with a \emph{top-5\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\% of heads.
9	High concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.
10	
11	Table~\ref{tab:heterogeneity} summarizes the results across five architectures at $4\times$ compression.
12	Qwen2.5-7B exhibits the highest \emph{spread} heterogeneity (top-5\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.
13	Constrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\% improvement over uniform 4-bit. %exp_id=qwen_constrained_mckp
14	
15	However, concentration alone does not predict MCKP benefit.
16	Yi-1.5-9B has a hires concentration of $0.71$---\emph{higher} than Qwen's $0.61$---yet constrained MCKP is counterproductive ($+$0.30 vs.\ $+$0.20 uniform). %exp_id=yi15_hires_constrained
17	The explanation lies in the \emph{shape} of the heterogeneity.
18	Yi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 has a 2-bit delta of 13.12, while the second-ranked head has delta 0.55---a $24\times$ gap ($t_1/t_5{=}0.90$, $t_1/t_2{=}23.7$). %exp_id=yi15_hires_profiling
19	Critically, L4H3's sensitivity is confined to the 2-bit operating point: its 4-bit and 8-bit deltas are ${\approx}\,0$.
20	The solver therefore has no cross-bitwidth gradient to exploit---upgrading L4H3 from 2-bit to 4-bit removes the distortion, but further upgrading to 8-bit provides no additional benefit, so the budget freed by downgrading other heads has nowhere useful to go.
21	We call
…[truncated 5573 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T20:46:28.815652+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T20:46:28.815815+00:00_

1	Per-head mixed-precision quantization of the KV cache promises lower perplexity than uniform quantization at the same average bit-width, but on hardware-aligned bit-widths $\{2, 4, 8, 16\}$, existing solvers fail catastrophically: unconstrained greedy and MCKP allocation achieve 32.45 and 36.92 perplexity on Qwen2.5-7B---far worse than uniform 4-bit (15.45).
2	We trace this failure to \emph{2-bit distortion compounding}: when the majority of heads are assigned 2-bit precision, per-head quantization errors interact non-additively through the residual stream, violating the additive objective assumed by standard solvers.
3	We show that a single cardinality constraint capping the number of 2-bit assignments is a minimal sufficient fix.
4	On Qwen2.5-7B at $4\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\% reduction over uniform 4-bit.
5	The constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures ($\Delta{=}0.0000$), enabling use of a simple $O(H \log H)$ greedy algorithm; per-layer brute-force oracle confirms near-optimality (max gap 0.02 PPL).
6	However, the benefit depends on architecture: on Llama-3.1-8B the improvement is marginal (8.45 vs.\ 8.47), and on Mistral-7B-v0.3, Yi-1.5-9B, and Gemma-2-9B non-uniform allocation is counterproductive.
7	Notably, Yi-1.5-9B has the highest GQA ratio tested (8:1) and the highest top-5\% concentration (0.71), yet degrades under non-uniform allocation---because its heterogeneity is a single-outlier ``spike'' with no cross-bitwidth sensitivity gradient, rather than the ``spread'' pattern that enables MCKP to redistribute budget across heads.
8	We propose a joint heterogeneity diagnostic combining concentration and distribution shape, validated on five architectures, that can indicate before any allocation whether a given architecture will benefit from non-uniform quantization.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T20:46:28.815959+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T20:46:28.816112+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Per-head mixed-precision quantization of the KV cache is a natural strategy for reducing memory during LLM inference: assign fewer bits to insensitive heads and more bits to sensitive ones, achieving lower perplexity than uniform quantization at the same average bit-width.
5	Recent work on KV cache quantization explores both uniform schemes~\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\cite{zhang2023h2o,li2024snapkv}.
6	RateQuant~\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\{2,3,4,5,6\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).
7	
8	In practice, hardware-efficient inference requires bit-widths drawn from $\{2, 4, 8, 16\}$---the formats natively supported by modern accelerators.
9	On this non-consecutive set, the polymatroid structure breaks down, and greedy is no longer provably optimal.
10	One might expect that exact MCKP solvers would fill this gap.
11	They do not.
12	On Qwen2.5-7B at $4\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \emph{far worse} than uniform 4-bit (15.45).
13	The optimization does not merely underperform; it fails catastrophically.
14	
15	The root cause is not solver suboptimality but a violation of the objective's additive distortion assumption.
16	Both solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors are large enough to compound through the residual stream.
17	The additive model predicts $\sim$11 PPL for these allocations; the actual PPL is $3$--$4\times$ higher.
18	At 4-bit and above, per-head distortions are small and compound negligibly---uniform 4-bit achieves clos
…[truncated 4641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T20:46:28.816253+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T20:46:28.816387+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	We showed that per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \{2, 4, 8, 16\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding through the residual stream.
4	A single constraint---limiting simultaneously active 2-bit heads to $k \leq 8$ (7\% of heads)---reduces perplexity on Qwen2.5-7B from 15.45 (uniform 4-bit) to 11.23, a 27.3\% improvement at $4\times$ compression.
5	Under the constraint, solver choice becomes irrelevant: greedy and MCKP produce equivalent allocations across all three architectures ($\Delta = 0.0000$), so a simple $O(H \log H)$ greedy algorithm suffices.
6	The benefit of non-uniform allocation depends on both the concentration and \emph{shape} of head sensitivity heterogeneity.
7	Qwen2.5-7B (concentration 0.61, $t_1/t_5{=}0.57$, spread pattern) shows large gains; Llama-3.1-8B ($t_1/t_5{=}0.71$, spike) shows marginal improvement (8.45 vs.\ 8.47 PPL); Mistral-7B-v0.3, Yi-1.5-9B, and Gemma-2-9B are counterproductive.
8	Yi-1.5-9B is a critical test case: despite the highest concentration tested ($0.71$, exceeding Qwen), its heterogeneity is a single-outlier spike ($t_1/t_5{=}0.90$) with no cross-bitwidth sensitivity gradient, so MCKP cannot redistribute budget.
9	A joint diagnostic using concentration and $t_1/t_5$ ratio distinguishes spread, spike, and flat patterns across our five models, computable from the same profiling pass used for allocation, letting practitioners decide \emph{before deployment} whether non-uniform quantization is worthwhile.
10	
11	\paragraph{Limitations.}
12	Our study has several limitations that temper the generality of the findings.
13	First, we evaluate only five 7--9B-scale models---too few to establish a statistically robust correlation between heterogeneity and quantization benefit; the observed trend is directional evidence, not a predictive law.
14	Second, profiling relies on a sing
…[truncated 1088 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_claim3_revision_20260514T204030",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-14T20:46:28.816606+00:00_

All edits verified. Summary of changes across four files:

**analysis.tex** (§5.1 + §5.2):
- Yi-1.5 concentration updated 0.49 → 0.71 (hires); the old threshold-based claim is replaced by mechanism-based analysis
- Added Yi-1.5 case study: L4H3 2-bit delta=13.12 (24× gap), 4-bit/8-bit deltas ≈ 0 → no cross-bitwidth gradient
- Contrasted with Qwen L0H0 multi-bitwidth gradient → spread pattern
- Table: added $t_1/t_5$ column, Shape column (Spread/Spike/Flat); Llama/Mistral/Gemma-2 marked $^\ddagger$ (standard profiling, hires pending)
- Diagnostic framework: concentration + shape joint diagnosis with three patterns; t1/t5 ≈ 0.70 as illustrative boundary
- All quantitative claims tagged with `%exp_id=`

**abstract.tex**: Yi-1.5 now described as "highest concentration (0.71)" with spike/spread mechanism; "joint heterogeneity diagnostic" replaces old phrasing

**introduction.tex**: Updated diagnostic description (lines 42-44) and contribution #3 to reference joint diagnostic with $t_1/t_5$ ratio

**conclusion.tex**: Rewritten lines 6-9 with concentration + shape framing, Yi-1.5 as critical test case ($0.71 > 0.61$ yet counterproductive)

Float32 appendix note was already present (appendix.tex line 29-30).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_claim3_revision_20260514T204030"
}
```

</details>

---
