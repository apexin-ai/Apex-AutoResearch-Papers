# cpu paper n500 audit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_cpu_paper-n500-audit_20260515T005319.jsonl`
- **Structured JSON:** [`34bfacc94289b80cfe7d.json`](../../sessions/34/34bfacc94289b80cfe7d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-15T00:57:13.631067+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T00:57:13.631715+00:00_

artifacts/_project/paper/appendix.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/appendix_disc_analysis.tex
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/appendix_results.tex
artifacts/_project/paper/appendix_moved.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/discussion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T00:57:13.632040+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "n\\s*[=≈]\\s*50[^0-9]|50 problems|fifty|\\bn=50\\b|n = 50|sample.{0,20}50",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "head_limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Grep",
  "tool_args": {
    "pattern": "n\\s*[=≈]\\s*50[^0-9]|50 problems|fifty|\\bn=50\\b|n = 50|sample.{0,20}50",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "head_limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T00:57:13.632297+00:00_

artifacts/_project/paper/results.tex:34:\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$. $G = \widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$.}
artifacts/_project/paper/numerical_audit_report.md:31:### W2. DeepSeek n=50 vs n=49 inconsistency
artifacts/_project/paper/numerical_audit_report.md:35:- **Correct**: DeepSeek has n=49 valid problems for paired analysis (1 excluded), not n=50
artifacts/_project/paper/numerical_audit_report.md:36:- **Note**: The methodology correctly says "50 problems" (total tested), and Tab 5 (`tab:permutation`) correctly says n=49. The error is specifically in the cross-model comparison sentence.
artifacts/_project/paper/main.aux:449:[Omitted long matching line]
artifacts/_project/paper/main.aux:450:\newlabel{tab:main-results}{{2}{5}{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\Delta = \widetilde {\mathrm {II}}_{\textit {low}} - \widetilde {\mathrm {II}}_{\textit {high}}$. $G = \widetilde {\mathrm {II}}_{\textit {low}} / \widetilde {\mathrm {II}}_{\textit {high}}$}{table.caption.14}{}}
artifacts/_project/paper/appendix_moved.tex:26:Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\S\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\ $n{=}49$ for DeepSeek).
artifacts/_project/paper/methodology.tex:10:We use 50 problems stratified from MATH-500~\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2
…[truncated 5 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T00:57:13.632541+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "n\\s*[={}]\\s*4[69]|n=4[69]|n\\{=\\}4[69]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "head_limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Grep",
  "tool_args": {
    "pattern": "n\\s*[={}]\\s*4[69]|n=4[69]|n\\{=\\}4[69]",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "head_limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T00:57:13.632798+00:00_

artifacts/_project/paper/appendix_disc_analysis.tex:45:Bootstrap confidence intervals use $B{=}10{,}000$ resamples (recomputed from initial $B{=}1{,}000$ profiling runs). The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json
artifacts/_project/paper/results.tex:77:To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems). Table~\ref{tab:llama-cross-arch} reports the strategy-dependent severity comparison across sparsity levels.
artifacts/_project/paper/main.aux:452:\@writefile{lot}{\contentsline {table}{\numberline {3}{\ignorespaces Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $d_z$: paired Cohen's $d$ for importance vs.\ random severity; $\setbox \z@ \hbox {\mathsurround \z@ $\textstyle \Delta $}\mathaccent "0365{\Delta }$: median paired difference with bootstrap 95\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon $p$ ($k{=}4$). $n{=}49$ paired problems.}}{5}{table.caption.16}\protected@file@percent }
artifacts/_project/paper/main.aux:453:\newlabel{tab:llama-cross-arch}{{3}{5}{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $d_z$: paired Cohen's $d$ for importance vs.\ random severity; $\widetilde {\Delta }$: median paired difference with bootstrap 95\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon $p$ ($k{=}4$). $n{=}49$ paired problems}{table.caption.16}{}}
artifacts/_project/paper/main.aux:1000:\@writefile{lot}{\contentsline {table}{\numberline {6}{\ignorespaces Paired permutation test for compound severity: importance vs.\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}}{10}{table.caption.36}\protected@file@percent }
artifacts/_project/paper/ma
…[truncated 1954 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T00:57:13.633028+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T00:57:13.633232+00:00_

1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	Prior work treats compound interaction magnitude as approximately constant across the generation process.
4	We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.
5	
6	We evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.
7	Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
8	Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible median difference ($\widetilde{\Delta} = \placeholder{}$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
9	At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
10	The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$; Spearman $\rho 
…[truncated 934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T00:57:13.633455+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T00:57:13.633664+00:00_

1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	\label{sec:models}
6	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
7	
8	\paragraph{Dataset.}
9	\label{sec:dataset}
10	We use 50 problems stratified from MATH-500~\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048).
11	
12	\paragraph{Sparsity configuration.}
13	\label{sec:sparsity-config}
14	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.
15	
16	\paragraph{Phase segmentation and metrics.}
17	\label{sec:phase-seg}
18	Each sequence is segmented into three phases using the quantile-based method (\S\ref{sec:phase-segmentation}), with $\texttt{min\_phase\_length}{=}10$. We compute segment-level perplexity, II (Eq.~\ref{eq:ii}), and $G$ (Eq.~\ref{eq:gradient}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1).
19	
20	\paragraph{Statistical analysis.}
21	\label{sec:stats}
22	All reported confidence intervals and significance t
…[truncated 397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T00:57:13.633855+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T00:57:13.634123+00:00_

1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\times}$ amplification. Under random eviction, no systematic growth is observed ($-0.02$ to $1.54$), confirming that compound severity depends qualitatively on eviction strategy. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff
20	Random     & 0.01 & $-$0.02 & 0.54 & 1.54 \\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \approx 0.9$--$1.7{
…[truncated 8932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T00:57:13.634347+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T00:57:13.634579+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.

…[truncated 1862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T00:57:13.634780+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T00:57:13.634959+00:00_

1	\section{Analysis: Entropy-Discrimination Collapse}
2	\label{sec:analysis}
3	
4	We propose \emph{discrimination collapse} as the primary mechanism driving the phase-strategy interaction. Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) across all sparsity levels, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	Beyond discrimination collapse, head pruning redistributes the attention entropy of surviving heads. For DeepSeek, the entropy delta is consistently negative ($\Delta\mathcal{H} \in [-0.047, -0.040]$), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in survivors. For Qwen, the pattern partially replicates at $s \leq 0.20$ but reverses at $s{=}0.25$ ($\Delta\mathcal{H} = +0.045$), suggesting model-specific head specialization patterns (Appendix~\ref{app:analysis}, Table~\ref{tab:entropy-deltas}). We characterize discrimination collapse as the robust, model-independent driver, with entropy redistribution as a secondary, model-dependent amplifier. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T00:57:13.635136+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T00:57:13.635325+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-2024}), suggesting broad applicability.
9	
10	A preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. At $s{=}0.25$, oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached \placeholder{ORACLE\_PCT}\% (Wilcoxon $p = \placeholder{ORACLE\_P}$), below t
…[truncated 1685 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T00:57:13.635545+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T00:57:13.635719+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\times}$ to $274{\times}$ across sparsity levels ($d_z$: $0.44 \to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$) and partially extends cross-architecture to DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\sim$1/40 the magnitude. Discrimination collapse provides a mechanistic explanation supported by both Qwen2-based models; LLaMA results are directionally consistent but the interaction is weaker than in Qwen2 architectures.
5	These findings motivate phase-aware sparsity allocation for reasoning model deployment.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T00:57:13.635913+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T00:57:13.636092+00:00_

1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7--8B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) partially confirms the qualitative pattern beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
6	
7	\paragraph{Mechanism.}
8	The discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.
9	
10	\paragraph{Sparsity range.}
11	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\ref{app:lim
…[truncated 14 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T00:57:13.636285+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T00:57:13.636601+00:00_

1	% Content moved from main body to appendix:
2	% - Phase-strategy crossover details (from results §5.3)
3	% - Cross-model replication details with tables/figures (from results §5.4)
4	% - Permutation test details with table/forest plot (from results §5.5)
5	% - Full entropy-discrimination collapse analysis with tables (from analysis §6)
6	% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.
7	
8	\section{Phase-Strategy Crossover Details}
9	\label{app:crossover-details}
10	
11	At $s{=}0.25$, a strategy ranking reversal emerges (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\ $0.818$) but \emph{higher} II in the low-sparsity phase ($7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\times}$ at $s{=}0.15$, $5.4{\times}$ at $s{=}0.20$, $5.3{\times}$ at $s{=}0.25$, and $3.6{\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
16	\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
17	\label{fig:crossover}
18	\end{figure}
19	
20	
21	\section{Cross-Model Replication Details}
22	\label{app:cross-model-details}
23	
24	Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in trai
…[truncated 12246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T00:57:13.636813+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T00:57:13.636995+00:00_

1	% Appendix: supplementary results details
2	
3	\section{Cross-Model Replication Details}
4	\label{app:cross-model-details}
5	
6	\paragraph{Per-problem concordance.}
7	The per-problem concordance across models is not significant (median $\rho = \placeholder{}$, $p = \placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
8	
9	\paragraph{Random eviction control.}
10	As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible median difference ($\widetilde{\Delta} = \placeholder{}$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T00:57:13.637168+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T00:57:13.637428+00:00_

1	\section{Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment, indicating onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051
12	
13	\paragraph{Random masking as falsification control.}
14	Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($\widetilde{\Delta} = \placeholder{}$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy sh
…[truncated 6847 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T00:57:13.637656+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T00:57:13.637869+00:00_

1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position spar
…[truncated 1336 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T00:57:13.638064+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T00:57:13.638263+00:00_

1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	\label{sec:compound-sparsity}
12	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
13	
14	\paragraph{Interaction Index.}
15	\label{sec:interaction-index}
16	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
17	\begin{equation}
18	    \mathrm{II} = r_b - r_a - r_k + 1.
19	    \label{eq:ii}
20	\end{equation}
21	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative co
…[truncated 1036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T00:57:13.638480+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T00:57:13.638682+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
11	
12	\paragraph{KV cache eviction.}
13	Most methods rely on importance scoring whose reliability is increasingly questioned.
14	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
15	\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
16	RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
17	\cite{hies-2025} independently show that importance-based head discrimination collapses under heavy pruning, further questioning single-metric reliability.
18	Lethe~\cite{lethe-aaai2026} introduces temporal adaptivity with layer-wise multi-round pruning, and SparK~\cite{spark-aaai2026} extends eviction to the channel dimension with recoverable sparsity.
19	These me
…[truncated 1295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T00:57:13.639083+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\placeholder",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
  "output_mode": "content",
  "-n": "True",
  "head_limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\placeholder",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper",
    "output_mode": "content",
    "-n": "True",
    "head_limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T00:57:13.639298+00:00_

artifacts/_project/paper/main.tex:21:\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
artifacts/_project/paper/discussion.tex:10:[Omitted long matching line]
artifacts/_project/paper/discussion.tex:15:[Omitted long matching line]
artifacts/_project/paper/appendix_moved.tex:30:Table~\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with $|\mathrm{II}| > 0.001$ in each phase. The mid-phase null rate (\placeholder{NULL\_PCT}\%) reflects problems where compound interaction is absent in intermediate phases; this does not affect the low--high contrast ($\Delta$) used in the primary analysis.
artifacts/_project/paper/appendix_moved.tex:35:\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\text{total}} = \placeholder{N\_QW}$).}
artifacts/_project/paper/appendix_moved.tex:41:High & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
artifacts/_project/paper/appendix_moved.tex:42:Mid  & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
artifacts/_project/paper/appendix_moved.tex:43:Low  & \placeholder{} & \placeholder{} & \placeholder{} & \placeholder{} \\
artifacts/_project/paper/appendix_moved.tex:73:The per-problem concordance across models is not significant (median $\rho = \placeholder{}$, $p = \placeholder{}$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
artifacts/_project/paper/appendix_moved.tex:76:As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (
…[truncated 3381 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T00:57:13.639519+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T00:57:13.639705+00:00_

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
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}
22	
23	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Reasoning Models}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	
29	\maketitle
30	
31	\input{abstract}
32	
33	\input{introduction}
34	\input{related_work}
35	\input{background}
36	\input{methodology}
37	\input{results}
38	\input{analysis}
39	\input{discussion}
40	\input{conclusion}
41	
42	\bibliography{references}
43	
44	\section*{Limitations}
45	\input{limitations}
46	
47	\appendix
48	\input{appendix}
49	\input{appendix_moved}
50	\input{appendix_disc_analysis}
51	
52	\end{document}
53	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T00:57:13.640037+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_n500_update_checklist.md",
  "content": "# Paper n=500 Update Checklist\n\n> Generated 2026-05-15. Covers all .tex files in `artifacts/_project/paper/`.\n> \"Current\" = n=50 era values. \"Replace with\" = description of n=500 data source needed.\n\n---\n\n## 1. abstract.tex\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 6 | `using 50 MATH-500 problems` | `500 MATH-500 problems` |\n| 7 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | DeepSeek n=500 importance Δ at s=0.15..0.30 |\n| 7 | `$d_z$ growing from $0.44$ (small) to $0.80$ (large)` | DeepSeek n=500 Cohen's d_z at s=0.15..0.30 |\n| 7 | `$p < 0.005$ at all four sparsity levels` | DeepSeek n=500 permutation p-values (likely still < 0.005 with more power) |\n| 8 | `$\\widetilde{\\Delta} = \\placeholder{}$` — Qwen random s=0.30 median diff | Qwen n=500 random s=0.30 Δ̃ |\n| 9 | `$\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$` (high-phase crossover) | DeepSeek n=500 II_high at s=0.25 (importance vs random) |\n| 9 | `$7.196$ vs.\\ $1.363$` (low-phase crossover) | DeepSeek n=500 II_low at s=0.25 (importance vs random) |\n| 10 | `$d_z \\geq 0.55$; Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$` | Qwen n=500 d_z, Spearman ρ, gradient permutation p |\n| 10 | `$\\widetilde{\\Delta}$: $0.020 \\to 0.356$; $s{=}0.30$ Wilcoxon $p_{\\text{Bonf}}{=}0.029$` | LLaMA n=500 (if rerun; otherwise keep n=50 with caveat) |\n\n---\n\n## 2. methodology.tex\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 10 | `We use 50 problems stratified from MATH-500` | `500 problems from MATH-500` (or `the full MATH-500 set`) |\n| 22 | `All tests yield $p_{\\text{Bonf}} < 0.005$ at every sparsity level` | Verify with n=500 data; likely still holds or strengthens |\n\n---\n\n## 3. results.tex\n\n### §5.1 Strategy-Dependent Severity (Tab 1)\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 8 | `$\\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\\times}$ amplification` | DeepSeek n=500 aggregate Δ values + ratio |\n| 8 | `$-0.02$ to $1.54$` (random Δ range) | DeepSeek n=500 random Δ values |\n| 13 | `$n{=}50$ MATH-500 problems` (Tab 1 caption) | `$n{=}500$` |\n| 19 | `0.39 & 1.48 & 7.16 & 14.59` (Importance row) | DeepSeek n=500 importance Δ |\n| 20 | `0.01 & $-$0.02 & 0.54 & 1.54` (Random row) | DeepSeek n=500 random Δ |\n\n### §5.2 Phase-Modulated Amplification (Tab 2 + Fig 1)\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 29 | `$G$ increases from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$` | DeepSeek n=500 G values |\n| 29 | `$\\widetilde{\\mathrm{II}}_{\\textit{high}}$ ranges from $0.006$ to $0.053$` | DeepSeek n=500 II_high values |\n| 29 | `$G \\approx 0.9$--$1.7{\\times}$` (random G range) | DeepSeek n=500 random G values |\n| 34 | `50 problems` (Tab 2 caption) | `500 problems` |\n| 40 | `0.006 & 0.081 & 0.398 & 0.39 & $\\mathbf{69}$` (s=0.15 imp) | n=500 values |\n| 41 | `0.093 & 0.097 & 0.103 & 0.01 & 1.1` (s=0.15 rand) | n=500 values |\n| 43 | `0.015 & 0.203 & 1.496 & 1.48 & $\\mathbf{103}$` (s=0.20 imp) | n=500 values |\n| 44 | `0.292 & 0.350 & 0.276 & $-$0.02 & 0.9` (s=0.20 rand) | n=500 values |\n| 46 | `0.032 & 1.118 & 7.196 & 7.16 & $\\mathbf{222}$` (s=0.25 imp) | n=500 values |\n| 47 | `0.818 & 0.932 & 1.363 & 0.54 & 1.7` (s=0.25 rand) | n=500 values |\n| 49 | `0.053 & 2.283 & 14.639 & 14.59 & $\\mathbf{274}$` (s=0.30 imp) | n=500 values |\n| 50 | `2.503 & 2.592 & 4.041 & 1.54 & 1.6` (s=0.30 rand) | n=500 values |\n| 58 | Fig 1 caption: `$69{\\times}$ to $274{\\times}$` | n=500 G range |\n\n### §5.3 Phase-Strategy Crossover\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 66 | `$0.032$ vs.\\ $0.818$` and `$7.196$ vs.\\ $1.363$---a $5.3{\\times}$ reversal` | DeepSeek n=500 crossover values at s=0.25 |\n\n### §5.4 Cross-Model Replication\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 71 | `$\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$` | Qwen n=500 Δ values |\n| 71 | `${\\sim}1/5$ the magnitude` | Recalculate ratio with n=500 |\n| 71 | `$d_z{=}0.28$, CI includes zero` (s=0.15 marginal) | Qwen n=500 d_z at s=0.15; check if still marginal |\n| 71 | `$d_z \\geq 0.55$` (s≥0.20) | Qwen n=500 d_z |\n| 71 | `\\placeholder{NULL\\_PCT}\\%` (Qwen mid-phase null rate) | Qwen n=500 mid-phase null rate |\n| 71 | `Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$` | Qwen n=500 Spearman ρ and gradient permutation p |\n\n### §5.5 Cross-Architecture Validation\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 77 | `$n{=}49$ paired problems` | LLaMA n=500 paired problem count |\n| 79 | `$[0.002, 0.043]$` (s=0.15 CI) | LLaMA n=500 bootstrap CI at s=0.15 |\n| 79 | `$p_{\\text{Bonf}}{=}0.219$` (s=0.15 Wilcoxon) | LLaMA n=500 |\n| 79 | `$[-0.069, 0.544]$` (s=0.30 CI) | LLaMA n=500 |\n| 79 | `$p_{\\text{Bonf}}{=}0.029$` (s=0.30 Wilcoxon) | LLaMA n=500 |\n| 79 | `$\\widetilde{\\Delta}$: $0.020 \\to 0.356$` (monotonic increase) | LLaMA n=500 |\n| 81 | `${\\sim}40{\\times}$ smaller ... ${\\sim}7{\\times}$ smaller` | Recalculate ratios with n=500 |\n| 81 | `Wilcoxon $p < \\placeholder{}$` (LLaMA random s=0.30) | LLaMA n=500 random Wilcoxon p |\n| 86 | `$n{=}\\placeholder{N\\_LLAMA}$` (table caption) | LLaMA n=500 paired count |\n| 92-95 | All `\\placeholder{}` in LLaMA table | LLaMA n=500 Δ̃, CI, p_Bonf at all 4 sparsity levels |\n\n### §5.6 Statistical Validation (Tab 3 + Tab 4)\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 104 | `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$` (permutation Δ) | DeepSeek n=500 permutation test observed Δ |\n| 106 | `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)` (DeepSeek d_z) | DeepSeek n=500 d_z |\n| 106 | `$d_z{=}0.28$` (Qwen s=0.15); `$d_z \\geq 0.55$` | Qwen n=500 d_z |\n| 106 | `$d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$` (QW vs DS at s≥0.25) | n=500 d_z comparison |\n| 117 | `0.44 & 0.32\\; $[0.20, 0.47]$ & 0.28 & 0.05\\; $[-0.01, 0.11]$` (s=0.15 row) | n=500 d_z and Δ̃ CI for both models |\n| 118 | `0.52 & 1.15\\; $[0.66, 1.26]$ & 0.55 & 0.21\\; $[0.07, 0.40]$` (s=0.20 row) | n=500 |\n| 119 | `0.68 & 3.97\\; $[2.83, 5.29]$ & 0.89 & 1.11\\; $[0.61, 1.47]$` (s=0.25 row) | n=500 |\n| 120 | `0.80 & 9.94\\; $[8.39, 16.65]$ & 1.02 & 2.62\\; $[1.72, 3.65]$` (s=0.30 row) | n=500 |\n\n---\n\n## 4. introduction.tex\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 14 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | DeepSeek n=500 Δ |\n| 14 | `$d_z$: $0.44 \\to 0.80$` | DeepSeek n=500 d_z |\n| 14 | `Bonferroni-corrected $p < 0.005$` | n=500 p-values |\n| 15 | `$d_z \\geq 0.55$` (Qwen) | Qwen n=500 d_z |\n| 15 | `$\\sim$1/40 the magnitude` (LLaMA ratio) | LLaMA n=500 ratio |\n\n---\n\n## 5. analysis.tex\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 4 | `$0.030$--$0.081$ (DeepSeek)` (ΔGini) | DeepSeek n=500 Gini deltas |\n| 4 | `$0.010$--$0.020$ (Qwen)` (ΔGini) | Qwen n=500 Gini deltas |\n| 6 | `$\\Delta\\mathcal{H} \\in [-0.047, -0.040]$` (DeepSeek entropy) | DeepSeek n=500 entropy deltas |\n| 6 | `$\\Delta\\mathcal{H} = +0.045$` (Qwen s=0.25 reversal) | Qwen n=500 entropy delta at s=0.25 |\n\n---\n\n## 6. discussion.tex\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 5 | `$69$--$274{\\times}$` (G range) | n=500 G range |\n| 5 | `$0.032$ vs.\\ $0.818$` and `$7.196$ vs.\\ $1.363$` (crossover) | n=500 crossover values |\n| 10 | `\\placeholder{ORACLE\\_PCT}\\%` | Oracle recovery % from pilot (may not change with n=500; verify) |\n| 10 | `\\placeholder{ORACLE\\_P}` | Oracle Wilcoxon p |\n| 10 | `\\placeholder{HEUR\\_PCT}\\%` | Heuristic recovery % |\n| 10 | `\\placeholder{HEUR\\_P}` | Heuristic Wilcoxon p |\n| 15 | `${\\sim}40{\\times}$ smaller ... ${\\sim}7{\\times}$ smaller` (LLaMA ratios) | n=500 ratios |\n| 15 | `$d_z \\geq 1.0$` (LLaMA within-importance) | LLaMA n=500 |\n| 15 | `Wilcoxon $p < \\placeholder{}$` (LLaMA random) | LLaMA n=500 random Wilcoxon p |\n\n---\n\n## 7. conclusion.tex\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 4 | `$69{\\times}$ to $274{\\times}$` | n=500 G range |\n| 4 | `$d_z$: $0.44 \\to 0.80$` | DeepSeek n=500 d_z |\n| 4 | `7/8 conditions non-significant` (random) | Verify with n=500 (could become 8/8 or stay 7/8) |\n| 4 | `$d_z \\geq 0.55$` (Qwen) | Qwen n=500 d_z |\n| 4 | `$\\sim$1/40 the magnitude` (LLaMA) | LLaMA n=500 ratio |\n\n---\n\n## 8. limitations.tex\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 2 | `$\\sim$1/40 of DeepSeek` | LLaMA n=500 ratio |\n| 2 | `only $s{=}0.30$ significant after Bonferroni correction` | LLaMA n=500 significance pattern |\n| 45 | `$n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded)` | n=500 valid paired counts |\n| 46 | `mean/median ratio ${\\sim}1.6{:}1$ at $s{=}0.30$` | n=500 skewness stats |\n| 47 | `CI lower bounds increasing from $0.19$ to $6.70$` | n=500 CI bounds |\n| 47 | `$[6.70,\\; 16.29]$` (s=0.30 CI) | n=500 CI at s=0.30 |\n\n---\n\n## 9. appendix_moved.tex\n\n### App: Crossover Details\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 11 | `$0.032$ vs.\\ $0.818$` and `$7.196$ vs.\\ $1.363$---a $5.3{\\times}$` | n=500 crossover values at s=0.25 |\n| 11 | `$3.9{\\times}$ at $s{=}0.15$, $5.4{\\times}$ at $s{=}0.20$, $5.3{\\times}$ at $s{=}0.25$, and $3.6{\\times}$ at $s{=}0.30$` | n=500 reversal magnitudes at all 4 levels |\n| 16 | Fig 3 caption: `$5.3{\\times}$` | n=500 value |\n\n### App: Cross-Model Replication Details\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 26 | `Four of the 50 problems are excluded ... $n{=}46$ valid problems for Qwen (vs.\\ $n{=}49$ for DeepSeek)` | n=500 exclusion counts and valid n |\n| 30 | `\\placeholder{NULL\\_PCT}\\%` (Qwen null rate) | Qwen n=500 mid-phase null rate |\n| 35 | `$n_{\\text{total}} = \\placeholder{N\\_QW}$` (table caption) | Qwen n=500 total |\n| 41-43 | All `\\placeholder{}` in effective-n table (12 cells) | Qwen n=500 per-phase effective n (3 phases × 4 sparsity levels) |\n| 59 | `0.39 & 1.48 & 7.16 & 14.59` (DeepSeek Δ in cross-model table) | DeepSeek n=500 Δ |\n| 60 | `0.04 & 0.23 & 1.27 & 2.94` (Qwen Δ in cross-model table) | Qwen n=500 Δ |\n| 73 | `median $\\rho = \\placeholder{}$, $p = \\placeholder{}$` (concordance) | n=500 per-problem concordance ρ and p |\n| 76 | `$\\widetilde{\\Delta} = \\placeholder{}$` (Qwen random s=0.30) | Qwen n=500 random Δ̃ at s=0.30 |\n\n### App: Permutation Test\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 84 | `$1.2{\\times}$ ($s{=}0.15$) to $1.6{\\times}$ ($s{=}0.30$)` (mean/median ratios DS) | DeepSeek n=500 skewness |\n| 84 | `$1.1{\\times}$ to $1.4{\\times}$ for Qwen` | Qwen n=500 skewness |\n| 86 | `$99.92$th percentile ... $p_{\\text{Bonf}} = 0.0032$` | n=500 permutation percentile/p |\n| 88 | `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$` (observed Δ) | n=500 observed Δ |\n| 88 | `$0.19 \\to 0.69 \\to 1.66 \\to 6.70$` (CI lower bounds) | n=500 CI lower bounds |\n| 93 | `$n{=}49$` (permutation table caption) | n=500 paired count |\n| 99 | `0.37 & $[0.19,\\; 0.62]$ & 0.0032` (s=0.15) | n=500 |\n| 100 | `0.97 & $[0.69,\\; 1.49]$ & ${<}\\,0.001$` (s=0.20) | n=500 |\n| 101 | `3.34 & $[1.66,\\; 6.64]$ & ${<}\\,0.001$` (s=0.25) | n=500 |\n| 102 | `9.85 & $[6.70,\\; 16.29]$ & ${<}\\,0.001$` (s=0.30) | n=500 |\n\n---\n\n## 10. appendix_disc_analysis.tex\n\n### App: Discrimination Collapse\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 4 | `$-0.031$ to $-0.073$` (DS random Gini) | DeepSeek n=500 random Gini deltas |\n| 4 | `$-0.019$ to $-0.045$` (QW random Gini) | Qwen n=500 random Gini deltas |\n| 11 | `$\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$` | n=500 II_high range |\n| 11 | `$0.105$` (s=0.35 supplementary) | Verify if s=0.35 pilot was rerun |\n| 14 | `$\\widetilde{\\Delta} = \\placeholder{}$` (Qwen random) | Qwen n=500 random Δ̃ |\n| 45 | `$n{=}49$ ... $n{=}46$` | n=500 valid counts |\n| 46 | `mean/median ratio ${\\sim}1.6{:}1$` and `median_diff=9.9436` | n=500 values |\n| 47 | `$0.19$ to $6.70$` and `$[6.70,\\; 16.29]$` | n=500 CIs |\n| 49 | `$\\widetilde{\\Delta} = \\placeholder{}$, bootstrap CI spanning zero` | Qwen n=500 random s=0.30 |\n\n---\n\n## 11. appendix.tex (Formulation)\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 38 | `$G_{\\times} = 58$--$241{\\times}$` (multiplicative null G) | Recompute with n=500 data if running multiplicative null verification |\n\n---\n\n## 12. appendix_results.tex (duplicates content from appendix_moved.tex)\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 7 | `median $\\rho = \\placeholder{}$, $p = \\placeholder{}$` | Same as appendix_moved L73 |\n| 10 | `$\\widetilde{\\Delta} = \\placeholder{}$` | Same as appendix_moved L76 |\n\n**Note:** `appendix_results.tex` is not included in `main.tex`; may be an orphan duplicate. Verify whether to delete or keep in sync.\n\n---\n\n## 13. Entropy / Discrimination Metrics Tables (in appendix_moved.tex)\n\n| Line | Table | Current Content | Replace With |\n|------|-------|----------------|-------------|\n| 132-135 | tab:discrimination-metrics-full | DS ΔGini: -0.030, -0.040, -0.065, -0.081; ΔCV: -0.56, -0.77, -1.29, -1.66 | DeepSeek n=500 |\n| 137-140 | tab:discrimination-metrics-full | QW ΔGini: -0.010, -0.012, -0.010, -0.020; ΔCV: -0.05, -0.21, -1.49, -1.14 | Qwen n=500 |\n| 172-175 | tab:entropy-deltas | DS ΔH: -0.040, -0.047, -0.045, -0.044 | DeepSeek n=500 |\n| 177-180 | tab:entropy-deltas | QW ΔH: -0.073, -0.076, +0.045, -0.007 | Qwen n=500 |\n\n*(These tables are in `appendix_moved.tex` lines 123-183)*\n\n---\n\n## 14. Figures (require regeneration from n=500 data)\n\n| Figure | File | Description | Data Source |\n|--------|------|-------------|-------------|\n| Fig 1 | `fig1_dose_response.pdf` | G vs s curve (importance vs random) | DeepSeek n=500 experiment_summary_table |\n| Fig 3 | `fig3_crossover.pdf` | Crossover bar chart at s=0.25 | DeepSeek n=500 II per phase |\n| Fig 4 | `fig4_bootstrap.pdf` | Forest plot of permutation test | DeepSeek n=500 permutation_test_results |\n| Fig 5 | `fig5_crossmodel.pdf` | Cross-model Δ comparison | DeepSeek + Qwen n=500 Δ |\n\n---\n\n## 15. Reviewer-Related Updates\n\n### W2: Statistical Power\n- n=500 directly addresses W2 (statistical power concern). Update:\n  - **methodology.tex L10**: sample size 50 → 500\n  - **limitations.tex L45**: paired n counts\n  - All CI widths should narrow substantially → update all CI values\n  - If any previously marginal results (Qwen s=0.15 d_z=0.28) become significant, update narrative accordingly\n\n### W5: Qwen Mid-Phase Null Rate\n- **results.tex L71**: `\\placeholder{NULL_PCT}` → Qwen n=500 null rate (was ~45.2% at n=50; recheck)\n- **appendix_moved.tex L30**: same `\\placeholder{NULL_PCT}`\n- **appendix_moved.tex L35, L41-43**: Per-phase effective-n table → fill with n=500 data\n- If null rate drops substantially at n=500, update the caveat language in results.tex L71\n\n---\n\n## 16. Conditional Updates (depend on n=500 results)\n\nThese items may or may not need textual changes depending on how n=500 results compare:\n\n| Item | Condition | Action if True |\n|------|-----------|---------------|\n| \"7/8 conditions non-significant\" (random) | Random results change at n=500 | Update count in abstract L8, conclusion L4, introduction L16 |\n| Qwen s=0.15 marginal ($d_z=0.28$, CI includes zero) | Becomes significant at n=500 | Remove \"marginal\" caveat in results L71, L106, Tab 4, conclusion |\n| LLaMA \"mixed evidence\" narrative | LLaMA results clarify at n=500 | Rewrite results.tex L77-81, discussion.tex L15, limitations L2-3 |\n| \"~1/5 magnitude\" (Qwen/DS ratio) | Ratio changes at n=500 | Update results L71, appendix_moved L48/L68 |\n| \"~1/40 magnitude\" (LLaMA/DS ratio) | Ratio changes at n=500 | Update abstract L10, intro L15, discussion L15, conclusion L4 |\n| C8 LLaMA \"qualitative consistent\" qualifier | Evidence strengthens/weakens | Adjust qualifier strength throughout |\n\n---\n\n## Summary Statistics\n\n- **Total locations requiring numerical update**: ~120+\n- **Placeholder values already marked** (`\\placeholder{}`): ~30\n- **Hard-coded n=50 values needing replacement**: ~90\n- **Figures to regenerate**: 4\n- **Files affected**: 11 of 15 .tex files (background.tex, related_work.tex, main.tex, appendix_results.tex not substantively affected)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_n500_update_checklist.md",
    "content": "# Paper n=500 Update Checklist\n\n> Generated 2026-05-15. Covers all .tex files in `artifacts/_project/paper/`.\n> \"Current\" = n=50 era values. \"Replace with\" = description of n=500 data source needed.\n\n---\n\n## 1. abstract.tex\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 6 | `using 50 MATH-500 problems` | `500 MATH-500 problems` |\n| 7 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | DeepSeek n=500 importance Δ at s=0.15..0.30 |\n| 7 | `$d_z$ growing from $0.44$ (small) to $0.80$ (large)` | DeepSeek n=500 Cohen's d_z at s=0.15..0.30 |\n| 7 | `$p < 0.005$ at all four sparsity levels` | DeepSeek n=500 permutation p-values (likely still < 0.005 with more power) |\n| 8 | `$\\widetilde{\\Delta} = \\placeholder{}$` — Qwen random s=0.30 median diff | Qwen n=500 random s=0.30 Δ̃ |\n| 9 | `$\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$` (high-phase crossover) | DeepSeek n=500 II_high at s=0.25 (importance vs random) |\n| 9 | `$7.196$ vs.\\ $1.363$` (low-phase crossover) | DeepSeek n=500 II_low at s=0.25 (importance vs random) |\n| 10 | `$d_z \\geq 0.55$; Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$` | Qwen n=500 d_z, Spearman ρ, gradient permutation p |\n| 10 | `$\\widetilde{\\Delta}$: $0.020 \\to 0.356$; $s{=}0.30$ Wilcoxon $p_{\\text{Bonf}}{=}0.029$` | LLaMA n=500 (if rerun; otherwise keep n=50 with caveat) |\n\n---\n\n## 2. methodology.tex\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 10 | `We use 50 problems stratified from MATH-500` | `500 problems from MATH-500` (or `the full MATH-500 set`) |\n| 22 | `All tests yield $p_{\\text{Bonf}} < 0.005$ at every sparsity level` | Verify with n=500 data; likely still holds or strengthens |\n\n---\n\n## 3. results.tex\n\n### §5.1 Strategy-Dependent Severity (Tab 1)\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 8 | `$\\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\\times}$ amplification` | DeepSeek n=500 aggregate Δ values + ratio |\n| 8 | `$-0.02$ to $1.54$` (random Δ range) | DeepSeek n=500 random Δ values |\n| 13 | `$n{=}50$ MATH-500 problems` (Tab 1 caption) | `$n{=}500$` |\n| 19 | `0.39 & 1.48 & 7.16 & 14.59` (Importance row) | DeepSeek n=500 importance Δ |\n| 20 | `0.01 & $-$0.02 & 0.54 & 1.54` (Random row) | DeepSeek n=500 random Δ |\n\n### §5.2 Phase-Modulated Amplification (Tab 2 + Fig 1)\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 29 | `$G$ increases from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$` | DeepSeek n=500 G values |\n| 29 | `$\\widetilde{\\mathrm{II}}_{\\textit{high}}$ ranges from $0.006$ to $0.053$` | DeepSeek n=500 II_high values |\n| 29 | `$G \\approx 0.9$--$1.7{\\times}$` (random G range) | DeepSeek n=500 random G values |\n| 34 | `50 problems` (Tab 2 caption) | `500 problems` |\n| 40 | `0.006 & 0.081 & 0.398 & 0.39 & $\\mathbf{69}$` (s=0.15 imp) | n=500 values |\n| 41 | `0.093 & 0.097 & 0.103 & 0.01 & 1.1` (s=0.15 rand) | n=500 values |\n| 43 | `0.015 & 0.203 & 1.496 & 1.48 & $\\mathbf{103}$` (s=0.20 imp) | n=500 values |\n| 44 | `0.292 & 0.350 & 0.276 & $-$0.02 & 0.9` (s=0.20 rand) | n=500 values |\n| 46 | `0.032 & 1.118 & 7.196 & 7.16 & $\\mathbf{222}$` (s=0.25 imp) | n=500 values |\n| 47 | `0.818 & 0.932 & 1.363 & 0.54 & 1.7` (s=0.25 rand) | n=500 values |\n| 49 | `0.053 & 2.283 & 14.639 & 14.59 & $\\mathbf{274}$` (s=0.30 imp) | n=500 values |\n| 50 | `2.503 & 2.592 & 4.041 & 1.54 & 1.6` (s=0.30 rand) | n=500 values |\n| 58 | Fig 1 caption: `$69{\\times}$ to $274{\\times}$` | n=500 G range |\n\n### §5.3 Phase-Strategy Crossover\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 66 | `$0.032$ vs.\\ $0.818$` and `$7.196$ vs.\\ $1.363$---a $5.3{\\times}$ reversal` | DeepSeek n=500 crossover values at s=0.25 |\n\n### §5.4 Cross-Model Replication\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 71 | `$\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$` | Qwen n=500 Δ values |\n| 71 | `${\\sim}1/5$ the magnitude` | Recalculate ratio with n=500 |\n| 71 | `$d_z{=}0.28$, CI includes zero` (s=0.15 marginal) | Qwen n=500 d_z at s=0.15; check if still marginal |\n| 71 | `$d_z \\geq 0.55$` (s≥0.20) | Qwen n=500 d_z |\n| 71 | `\\placeholder{NULL\\_PCT}\\%` (Qwen mid-phase null rate) | Qwen n=500 mid-phase null rate |\n| 71 | `Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$` | Qwen n=500 Spearman ρ and gradient permutation p |\n\n### §5.5 Cross-Architecture Validation\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 77 | `$n{=}49$ paired problems` | LLaMA n=500 paired problem count |\n| 79 | `$[0.002, 0.043]$` (s=0.15 CI) | LLaMA n=500 bootstrap CI at s=0.15 |\n| 79 | `$p_{\\text{Bonf}}{=}0.219$` (s=0.15 Wilcoxon) | LLaMA n=500 |\n| 79 | `$[-0.069, 0.544]$` (s=0.30 CI) | LLaMA n=500 |\n| 79 | `$p_{\\text{Bonf}}{=}0.029$` (s=0.30 Wilcoxon) | LLaMA n=500 |\n| 79 | `$\\widetilde{\\Delta}$: $0.020 \\to 0.356$` (monotonic increase) | LLaMA n=500 |\n| 81 | `${\\sim}40{\\times}$ smaller ... ${\\sim}7{\\times}$ smaller` | Recalculate ratios with n=500 |\n| 81 | `Wilcoxon $p < \\placeholder{}$` (LLaMA random s=0.30) | LLaMA n=500 random Wilcoxon p |\n| 86 | `$n{=}\\placeholder{N\\_LLAMA}$` (table caption) | LLaMA n=500 paired count |\n| 92-95 | All `\\placeholder{}` in LLaMA table | LLaMA n=500 Δ̃, CI, p_Bonf at all 4 sparsity levels |\n\n### §5.6 Statistical Validation (Tab 3 + Tab 4)\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 104 | `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$` (permutation Δ) | DeepSeek n=500 permutation test observed Δ |\n| 106 | `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)` (DeepSeek d_z) | DeepSeek n=500 d_z |\n| 106 | `$d_z{=}0.28$` (Qwen s=0.15); `$d_z \\geq 0.55$` | Qwen n=500 d_z |\n| 106 | `$d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$` (QW vs DS at s≥0.25) | n=500 d_z comparison |\n| 117 | `0.44 & 0.32\\; $[0.20, 0.47]$ & 0.28 & 0.05\\; $[-0.01, 0.11]$` (s=0.15 row) | n=500 d_z and Δ̃ CI for both models |\n| 118 | `0.52 & 1.15\\; $[0.66, 1.26]$ & 0.55 & 0.21\\; $[0.07, 0.40]$` (s=0.20 row) | n=500 |\n| 119 | `0.68 & 3.97\\; $[2.83, 5.29]$ & 0.89 & 1.11\\; $[0.61, 1.47]$` (s=0.25 row) | n=500 |\n| 120 | `0.80 & 9.94\\; $[8.39, 16.65]$ & 1.02 & 2.62\\; $[1.72, 3.65]$` (s=0.30 row) | n=500 |\n\n---\n\n## 4. introduction.tex\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 14 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | DeepSeek n=500 Δ |\n| 14 | `$d_z$: $0.44 \\to 0.80$` | DeepSeek n=500 d_z |\n| 14 | `Bonferroni-corrected $p < 0.005$` | n=500 p-values |\n| 15 | `$d_z \\geq 0.55$` (Qwen) | Qwen n=500 d_z |\n| 15 | `$\\sim$1/40 the magnitude` (LLaMA ratio) | LLaMA n=500 ratio |\n\n---\n\n## 5. analysis.tex\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 4 | `$0.030$--$0.081$ (DeepSeek)` (ΔGini) | DeepSeek n=500 Gini deltas |\n| 4 | `$0.010$--$0.020$ (Qwen)` (ΔGini) | Qwen n=500 Gini deltas |\n| 6 | `$\\Delta\\mathcal{H} \\in [-0.047, -0.040]$` (DeepSeek entropy) | DeepSeek n=500 entropy deltas |\n| 6 | `$\\Delta\\mathcal{H} = +0.045$` (Qwen s=0.25 reversal) | Qwen n=500 entropy delta at s=0.25 |\n\n---\n\n## 6. discussion.tex\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 5 | `$69$--$274{\\times}$` (G range) | n=500 G range |\n| 5 | `$0.032$ vs.\\ $0.818$` and `$7.196$ vs.\\ $1.363$` (crossover) | n=500 crossover values |\n| 10 | `\\placeholder{ORACLE\\_PCT}\\%` | Oracle recovery % from pilot (may not change with n=500; verify) |\n| 10 | `\\placeholder{ORACLE\\_P}` | Oracle Wilcoxon p |\n| 10 | `\\placeholder{HEUR\\_PCT}\\%` | Heuristic recovery % |\n| 10 | `\\placeholder{HEUR\\_P}` | Heuristic Wilcoxon p |\n| 15 | `${\\sim}40{\\times}$ smaller ... ${\\sim}7{\\times}$ smaller` (LLaMA ratios) | n=500 ratios |\n| 15 | `$d_z \\geq 1.0$` (LLaMA within-importance) | LLaMA n=500 |\n| 15 | `Wilcoxon $p < \\placeholder{}$` (LLaMA random) | LLaMA n=500 random Wilcoxon p |\n\n---\n\n## 7. conclusion.tex\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 4 | `$69{\\times}$ to $274{\\times}$` | n=500 G range |\n| 4 | `$d_z$: $0.44 \\to 0.80$` | DeepSeek n=500 d_z |\n| 4 | `7/8 conditions non-significant` (random) | Verify with n=500 (could become 8/8 or stay 7/8) |\n| 4 | `$d_z \\geq 0.55$` (Qwen) | Qwen n=500 d_z |\n| 4 | `$\\sim$1/40 the magnitude` (LLaMA) | LLaMA n=500 ratio |\n\n---\n\n## 8. limitations.tex\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 2 | `$\\sim$1/40 of DeepSeek` | LLaMA n=500 ratio |\n| 2 | `only $s{=}0.30$ significant after Bonferroni correction` | LLaMA n=500 significance pattern |\n| 45 | `$n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded)` | n=500 valid paired counts |\n| 46 | `mean/median ratio ${\\sim}1.6{:}1$ at $s{=}0.30$` | n=500 skewness stats |\n| 47 | `CI lower bounds increasing from $0.19$ to $6.70$` | n=500 CI bounds |\n| 47 | `$[6.70,\\; 16.29]$` (s=0.30 CI) | n=500 CI at s=0.30 |\n\n---\n\n## 9. appendix_moved.tex\n\n### App: Crossover Details\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 11 | `$0.032$ vs.\\ $0.818$` and `$7.196$ vs.\\ $1.363$---a $5.3{\\times}$` | n=500 crossover values at s=0.25 |\n| 11 | `$3.9{\\times}$ at $s{=}0.15$, $5.4{\\times}$ at $s{=}0.20$, $5.3{\\times}$ at $s{=}0.25$, and $3.6{\\times}$ at $s{=}0.30$` | n=500 reversal magnitudes at all 4 levels |\n| 16 | Fig 3 caption: `$5.3{\\times}$` | n=500 value |\n\n### App: Cross-Model Replication Details\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 26 | `Four of the 50 problems are excluded ... $n{=}46$ valid problems for Qwen (vs.\\ $n{=}49$ for DeepSeek)` | n=500 exclusion counts and valid n |\n| 30 | `\\placeholder{NULL\\_PCT}\\%` (Qwen null rate) | Qwen n=500 mid-phase null rate |\n| 35 | `$n_{\\text{total}} = \\placeholder{N\\_QW}$` (table caption) | Qwen n=500 total |\n| 41-43 | All `\\placeholder{}` in effective-n table (12 cells) | Qwen n=500 per-phase effective n (3 phases × 4 sparsity levels) |\n| 59 | `0.39 & 1.48 & 7.16 & 14.59` (DeepSeek Δ in cross-model table) | DeepSeek n=500 Δ |\n| 60 | `0.04 & 0.23 & 1.27 & 2.94` (Qwen Δ in cross-model table) | Qwen n=500 Δ |\n| 73 | `median $\\rho = \\placeholder{}$, $p = \\placeholder{}$` (concordance) | n=500 per-problem concordance ρ and p |\n| 76 | `$\\widetilde{\\Delta} = \\placeholder{}$` (Qwen random s=0.30) | Qwen n=500 random Δ̃ at s=0.30 |\n\n### App: Permutation Test\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 84 | `$1.2{\\times}$ ($s{=}0.15$) to $1.6{\\times}$ ($s{=}0.30$)` (mean/median ratios DS) | DeepSeek n=500 skewness |\n| 84 | `$1.1{\\times}$ to $1.4{\\times}$ for Qwen` | Qwen n=500 skewness |\n| 86 | `$99.92$th percentile ... $p_{\\text{Bonf}} = 0.0032$` | n=500 permutation percentile/p |\n| 88 | `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$` (observed Δ) | n=500 observed Δ |\n| 88 | `$0.19 \\to 0.69 \\to 1.66 \\to 6.70$` (CI lower bounds) | n=500 CI lower bounds |\n| 93 | `$n{=}49$` (permutation table caption) | n=500 paired count |\n| 99 | `0.37 & $[0.19,\\; 0.62]$ & 0.0032` (s=0.15) | n=500 |\n| 100 | `0.97 & $[0.69,\\; 1.49]$ & ${<}\\,0.001$` (s=0.20) | n=500 |\n| 101 | `3.34 & $[1.66,\\; 6.64]$ & ${<}\\,0.001$` (s=0.25) | n=500 |\n| 102 | `9.85 & $[6.70,\\; 16.29]$ & ${<}\\,0.001$` (s=0.30) | n=500 |\n\n---\n\n## 10. appendix_disc_analysis.tex\n\n### App: Discrimination Collapse\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 4 | `$-0.031$ to $-0.073$` (DS random Gini) | DeepSeek n=500 random Gini deltas |\n| 4 | `$-0.019$ to $-0.045$` (QW random Gini) | Qwen n=500 random Gini deltas |\n| 11 | `$\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$` | n=500 II_high range |\n| 11 | `$0.105$` (s=0.35 supplementary) | Verify if s=0.35 pilot was rerun |\n| 14 | `$\\widetilde{\\Delta} = \\placeholder{}$` (Qwen random) | Qwen n=500 random Δ̃ |\n| 45 | `$n{=}49$ ... $n{=}46$` | n=500 valid counts |\n| 46 | `mean/median ratio ${\\sim}1.6{:}1$` and `median_diff=9.9436` | n=500 values |\n| 47 | `$0.19$ to $6.70$` and `$[6.70,\\; 16.29]$` | n=500 CIs |\n| 49 | `$\\widetilde{\\Delta} = \\placeholder{}$, bootstrap CI spanning zero` | Qwen n=500 random s=0.30 |\n\n---\n\n## 11. appendix.tex (Formulation)\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 38 | `$G_{\\times} = 58$--$241{\\times}$` (multiplicative null G) | Recompute with n=500 data if running multiplicative null verification |\n\n---\n\n## 12. appendix_results.tex (duplicates content from appendix_moved.tex)\n\n| Line | Current Content | Replace With |\n|------|----------------|-------------|\n| 7 | `median $\\rho = \\placeholder{}$, $p = \\placeholder{}$` | Same as appendix_moved L73 |\n| 10 | `$\\widetilde{\\Delta} = \\placeholder{}$` | Same as appendix_moved L76 |\n\n**Note:** `appendix_results.tex` is not included in `main.tex`; may be an orphan duplicate. Verify whether to delete or keep in sync.\n\n---\n\n## 13. Entropy / Discrimination Metrics Tables (in appendix_moved.tex)\n\n| Line | Table | Current Content | Replace With |\n|------|-------|----------------|-------------|\n| 132-135 | tab:discrimination-metrics-full | DS ΔGini: -0.030, -0.040, -0.065, -0.081; ΔCV: -0.56, -0.77, -1.29, -1.66 | DeepSeek n=500 |\n| 137-140 | tab:discrimination-metrics-full | QW ΔGini: -0.010, -0.012, -0.010, -0.020; ΔCV: -0.05, -0.21, -1.49, -1.14 | Qwen n=500 |\n| 172-175 | tab:entropy-deltas | DS ΔH: -0.040, -0.047, -0.045, -0.044 | DeepSeek n=500 |\n| 177-180 | tab:entropy-deltas | QW ΔH: -0.073, -0.076, +0.045, -0.007 | Qwen n=500 |\n\n*(These tables are in `appendix_moved.tex` lines 123-183)*\n\n---\n\n## 14. Figures (require regeneration from n=500 data)\n\n| Figure | File | Description | Data Source |\n|--------|------|-------------|-------------|\n| Fig 1 | `fig1_dose_response.pdf` | G vs s curve (importance vs random) | DeepSeek n=500 experiment_summary_table |\n| Fig 3 | `fig3_crossover.pdf` | Crossover bar chart at s=0.25 | DeepSeek n=500 II per phase |\n| Fig 4 | `fig4_bootstrap.pdf` | Forest plot of permutation test | DeepSeek n=500 permutation_test_results |\n| Fig 5 | `fig5_crossmodel.pdf` | Cross-model Δ comparison | DeepSeek + Qwen n=500 Δ |\n\n---\n\n## 15. Reviewer-Related Updates\n\n### W2: Statistical Power\n- n=500 directly addresses W2 (statistical power concern). Update:\n  - **methodology.tex L10**: sample size 50 → 500\n  - **limitations.tex L45**: paired n counts\n  - All CI widths should narrow substantially → update all CI values\n  - If any previously marginal results (Qwen s=0.15 d_z=0.28) become significant, update narrative accordingly\n\n### W5: Qwen Mid-Phase Null Rate\n- **results.tex L71**: `\\placeholder{NULL_PCT}` → Qwen n=500 null rate (was ~45.2% at n=50; recheck)\n- **appendix_moved.tex L30**: same `\\placeholder{NULL_PCT}`\n- **appendix_moved.tex L35, L41-43**: Per-phase effective-n table → fill with n=500 data\n- If null rate drops substantially at n=500, update the caveat language in results.tex L71\n\n---\n\n## 16. Conditional Updates (depend on n=500 results)\n\nThese items may or may not need textual changes depending on how n=500 results compare:\n\n| Item | Condition | Action if True |\n|------|-----------|---------------|\n| \"7/8 conditions non-significant\" (random) | Random results change at n=500 | Update count in abstract L8, conclusion L4, introduction L16 |\n| Qwen s=0.15 marginal ($d_z=0.28$, CI includes zero) | Becomes significant at n=500 | Remove \"marginal\" caveat in results L71, L106, Tab 4, conclusion |\n| LLaMA \"mixed evidence\" narrative | LLaMA results clarify at n=500 | Rewrite results.tex L77-81, discussion.tex L15, limitations L2-3 |\n| \"~1/5 magnitude\" (Qwen/DS ratio) | Ratio changes at n=500 | Update results L71, appendix_moved L48/L68 |\n| \"~1/40 magnitude\" (LLaMA/DS ratio) | Ratio changes at n=500 | Update abstract L10, intro L15, discussion L15, conclusion L4 |\n| C8 LLaMA \"qualitative consistent\" qualifier | Evidence strengthens/weakens | Adjust qualifier strength throughout |\n\n---\n\n## Summary Statistics\n\n- **Total locations requiring numerical update**: ~120+\n- **Placeholder values already marked** (`\\placeholder{}`): ~30\n- **Hard-coded n=50 values needing replacement**: ~90\n- **Figures to regenerate**: 4\n- **Files affected**: 11 of 15 .tex files (background.tex, related_work.tex, main.tex, appendix_results.tex not substantively affected)\n"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T00:57:13.640555+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/paper_n500_update_checklist.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_cpu_paper-n500-audit_20260515T005319",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-15T00:57:13.640805+00:00_

已保存到 `artifacts/paper_n500_update_checklist.md`。

要点：
- **~120+ 处**需要数值更新，分布在 11 个 .tex 文件中
- 其中 ~30 处已用 `\placeholder{}` 标记，~90 处是硬编码的 n=50 数值
- **4 张图**需用 n=500 数据重新生成（fig1/3/4/5）
- 最密集的文件是 `results.tex`（~40 处）和 `appendix_moved.tex`（~25 处）
- 还有 ~6 处**条件性更新**，取决于 n=500 结果是否改变了定性结论（如 Qwen s=0.15 是否不再 marginal、random 7/8 是否变为 8/8）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_cpu_paper-n500-audit_20260515T005319"
}
```

</details>

---
