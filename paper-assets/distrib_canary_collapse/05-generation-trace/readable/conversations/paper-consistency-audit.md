# paper consistency audit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_paper_consistency_audit_20260516T002041.jsonl`
- **Structured JSON:** [`5d56c0753b2698fe9b30.json`](../../sessions/5d/5d56c0753b2698fe9b30.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-16T00:32:21.709368+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T00:32:21.709639+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T00:32:21.709794+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "distrib_canary_collapse",
  "fields": "['*']",
  "limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "fields": "['*']",
    "limit": "0"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T00:32:21.709924+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T00:32:21.710529+00:00_

&lt;persisted-output>
Output too large (52.5KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/e4edadb8-3ac1-49c2-8f69-8d594f779b03/tool-results/toolu_01JVWyJFhNFhBDsx8B7okMPd.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"mvp_v2_rep44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:38:10.762Z\", \"updated_at\": \"2026-05-16T00:10:26.251Z\", \"spec\": {\"hypothesis\": \"至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\", \"data_count\": 5000, \"seed\": 44, \"server\": \"autodl-rtx6000\", \"gpu\": \"pending\", \"synthetic_ratio\": 1, \"num_generations\": 10, \"steps_per_gen\": 5000, \"n_prompts\": 5000, \"fix_note\": \"n_prompts 1000→5000, steps_per_gen 10000→5000, 避免过拟合\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:10:26.251Z\"}, \"mvp_rep44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:12:15.033Z\", \"updated_at\": \"2026-05-16T00:10:25.605Z\", \"spec\": {\"hypothesis\": \"至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\", \"seed\": 44, \"server\": \"autodl-rtx6000\", \"gpu\": \"pending\", \"synthetic_ratio\": 1, \"num_generations\": 10, \"steps_per_gen\": 10000}, \"metrics\": {\"gen10_token_entropy\": 1.2205, \"gen10_ece\": 0.4237, \"gen10_perplexity\": 1033.16, \"gen10_distinct_1\": 0.0731, \"gen10_distinct_2\": 0.3637, \"gen10_distinct_3\": 0.6075}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:10:25.605Z\"}, \"alpha_sweep_a025_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:01:39.527Z\", \"updated_at\": \"2026-05-16T00:10:24.97
…[truncated 320 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T00:32:21.710732+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T00:32:21.710901+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T00:32:21.711036+00:00_

artifacts/dream_reports/dream_20260514T184925/best/paper.tex
artifacts/dream_reports/dream_20260514T184925/median/paper.tex
artifacts/dream_reports/dream_20260514T184925/worst/paper.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/background.tex
docs/paper/background.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/conclusion_365dc4.tex
artifacts/_project/paper/abstract_8c6c62.tex
docs/paper/conclusion.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
artifacts/_project/paper/related_work.tex
docs/paper/related_work.tex
artifacts/_project/paper/discussion.tex
docs/paper/method.tex
docs/paper/discussion.tex
docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T00:32:21.711160+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/e4edadb8-3ac1-49c2-8f69-8d594f779b03/tool-results/toolu_01JVWyJFhNFhBDsx8B7okMPd.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-4-projects-distrib-canary-collapse/e4edadb8-3ac1-49c2-8f69-8d594f779b03/tool-results/toolu_01JVWyJFhNFhBDsx8B7okMPd.txt"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T00:32:21.711751+00:00_

1	{"result":"{\"success\": true, \"data\": {\"experiments\": {\"mvp_v2_rep44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:38:10.762Z\", \"updated_at\": \"2026-05-16T00:10:26.251Z\", \"spec\": {\"hypothesis\": \"至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\", \"data_count\": 5000, \"seed\": 44, \"server\": \"autodl-rtx6000\", \"gpu\": \"pending\", \"synthetic_ratio\": 1, \"num_generations\": 10, \"steps_per_gen\": 5000, \"n_prompts\": 5000, \"fix_note\": \"n_prompts 1000→5000, steps_per_gen 10000→5000, 避免过拟合\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:10:26.251Z\"}, \"mvp_rep44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:12:15.033Z\", \"updated_at\": \"2026-05-16T00:10:25.605Z\", \"spec\": {\"hypothesis\": \"至少一族canary指标在100% SC full replacement下对downstream指标有≥1 gen的时序领先性\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103\", \"seed\": 44, \"server\": \"autodl-rtx6000\", \"gpu\": \"pending\", \"synthetic_ratio\": 1, \"num_generations\": 10, \"steps_per_gen\": 10000}, \"metrics\": {\"gen10_token_entropy\": 1.2205, \"gen10_ece\": 0.4237, \"gen10_perplexity\": 1033.16, \"gen10_distinct_1\": 0.0731, \"gen10_distinct_2\": 0.3637, \"gen10_distinct_3\": 0.6075}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-16T00:10:25.605Z\"}, \"alpha_sweep_a025_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:01:39.527Z\", \"updated_at\": \"2026-05-16T00:10:24.973Z\", \"spec\": {\"hypothesis\": \"α=0.25 低污染: 测试 canary→diversity lead 在温和 collapse 下是否保持，canary→perplexity lead 是否出现\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 42, \"synthetic
…[truncated 51755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T00:32:21.711976+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T00:32:21.712116+00:00_

1	\begin{abstract}
2	We demonstrate that lead-lag conclusions in iterative model collapse are determined more by method choice than by the data: naive cross-correlation yields 100\% significance (16/16 metric pairs), while Toda--Yamamoto Granger causality retains only 25\% (4/16), with inter-method agreement of $\kappa = 0.185$. We identify three methodological pitfalls---shared-trend confounding, short-series power loss, and threshold arbitrariness---that together inflate spurious-signal rates to 75\%. To replace single-method reporting, we introduce a multi-method consensus framework requiring agreement across ${\geq}4$ of 5 statistical tests with FDR correction, achieving 0\% false-positive and 0\% false-negative rates on reference extreme regimes. Applied to Pythia-410M across 4 seeds, 5 synthetic-data mixing ratios ($\alpha$), and 10 iterative training generations on WikiText-103, the framework reveals a sharp regime boundary: significant lead-lag relationships emerge at $\alpha{=}1.0$ (with preliminary single-seed evidence at $\alpha{=}0.75$), where token entropy Granger-causes diversity collapse with a one-generation lead ($|r| > 0.99$, 24/24 pairs significant, 0/24 in the reverse direction). Differencing eliminates all perplexity leads ($8/8 \to 0/8$) but preserves all diversity leads (24/24), confirming token entropy as a robust early-warning canary metric.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T00:32:21.712245+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T00:32:21.712421+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training language models on their own output across successive generations leads to progressive distribution degradation, a phenomenon variously termed model collapse~\cite{shumailov2024curse} or Model Autophagy Disorder~\cite{alemohammad2024mad}.
5	Tail modes vanish, lexical diversity narrows, and calibration deteriorates as each generation's output becomes the next generation's training data.
6	As large language models become ubiquitous content generators, the fraction of machine-generated text on the web grows steadily, making iterative training collapse---where models are unwittingly trained on the output of earlier model generations---a practical concern for the long-term stability of language model ecosystems.
7	
8	A natural follow-up question is whether cheap-to-compute statistics---\emph{canary metrics}---can provide early warning of impending collapse, analogous to early-warning signals for critical transitions in ecological and climate systems~\cite{scheffer2009early,scheffer2012anticipating}.
9	Several recent studies have pursued this direction: \citet{du2026geometric} informally observe that expected calibration error rises before accuracy degrades; SIGMA~\cite{sigma2026spectral} proposes spectral indicators of distributional shift; and DCES~\cite{dces2026counter} uses center-edge sampling dynamics as a collapse signal.
10	Yet the statistical methodology underlying these lead-lag claims---whether a canary metric genuinely \emph{precedes} downstream degradation, or merely correlates with it under shared non-stationary trends---has received little scrutiny.
11	
12	We identify four methodological deficiencies that pervade existing lead-lag analyses of iterative training collapse:
13	(1)~no differencing tests to rule out spurious regression arising from shared non-stationary trends---a well-known hazard when correlating co-trending time series;
14	(2)~no multi-method cross-validation---conclusions rest
…[truncated 6321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T00:32:21.712565+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T00:32:21.712742+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	The experiments in \S\ref{sec:method_sensitivity}--\ref{sec:consensus_validation} reveal that lead-lag conclusions in iterative training collapse are fragile along multiple axes.
5	This section distills three methodological pitfalls (\S\ref{sec:pitfalls}), proposes a multi-method consensus framework to address them (\S\ref{sec:consensus}), and calibrates the framework's error rates using built-in experimental controls (\S\ref{sec:calibration}).
6	
7	
8	\subsection{Methodological Pitfalls in Lead-Lag Analysis}
9	\label{sec:pitfalls}
10	
11	We identify three pitfalls that, individually or in combination, can produce incorrect conclusions about temporal precedence in iterative training systems.
12	Each is documented below with representative data from our experiments; full results appear in \S\ref{sec:experiments}.
13	
14	\paragraph{Pitfall 1: Method sensitivity.}
15	Applied to the same data ($\alpha{=}1.0$, 4~seeds, 16 canary$\to$downstream pairs), five lead-lag detection methods yield FDR significance rates ranging from 100\% (naive cross-correlation) to 25\% (Toda--Yamamoto Granger causality), with inter-method agreement of Cohen's $\kappa{=}0.185$---poor agreement (\S\ref{sec:method_sensitivity}).
16	The spurious-signal rate---the fraction of pairs flagged by the most liberal method but not confirmed by the most conservative---is 75\% across all five methods and 62.5\% when excluding Toda--Yamamoto, whose low statistical power at $T{=}10$ inflates this rate.
17	This pitfall is dangerous because method choice alone can determine whether a lead-lag relationship is deemed present or absent.
18	In a literature where single-method analyses are the norm, the implicit assumption that method choice does not matter is demonstrably false.
19	
20	\paragraph{Pitfall 2: Spurious regression under shared trends.}
21	A single preprocessing decision---first-differencing to remove shared non-stationary trends---can eliminate an entire ana
…[truncated 8739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T00:32:21.712881+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T00:32:21.713100+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \cite{biderman2023pythia}, a 410M-parameter autoregressive language model.
8	Pythia provides a controlled setting: small enough for multi-seed experiments across five contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.
9	Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
10	
11	Our protocol follows the full-replacement paradigm of \citet{shumailov2024curse}.
12	Each generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data; (2)~generate 5{,}000 synthetic samples from the fine-tuned model; (3)~fully replace the synthetic pool.
13	We run $T{=}10$ generations (11 time points including the generation-0 baseline) across contamination levels $\alpha \in \{0.00, 0.25, 0.50, 0.75, 1.00\}$.
14	The $\alpha{=}1.0$ condition uses four random seeds $\{42, 43, 44, 45\}$; other conditions use seed~42, with multi-seed replication in progress.
15	
16	We track two \emph{canary metrics}---cheap-to-compute statistics hypothesized to precede downstream degradation, inspired by early-warning signals in dynamical systems \cite{scheffer2009early}---and three \emph{downstream metrics}.
17	Canary metrics are token entropy (next-token prediction entropy averaged over held-out samples) and expected calibration error (ECE).
18	Downstream metrics are distinct-1 and distinct-2 ($n$-gram diversity \cite{li2016diversity}) and perplexity.
19	We additionally evaluate effective rank and Self-BLEU as candidate canaries (\S\ref{sec:case_study}).
20	Results for distinct-3 are reported in Appendix~\ref{app:distinct3}.
21	
22	All hypothesis tests apply Benjamini--Hochberg (BH
…[truncated 15022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T00:32:21.713243+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T00:32:21.713411+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Granger precedence is not causation.}
4	Granger causality tests whether past values of one series improve prediction of another beyond its own history; it does not establish true causation~\cite{granger1969investigating,shojaie2022granger}.
5	Bivariate Granger tests cannot exclude confounders: an unobserved process---such as a latent distributional shift in the training data---could independently drive both token entropy and diversity metrics, producing spurious lead-lag associations even when no direct relationship exists.
6	Our multi-method consensus framework inherits this limitation in full.
7	Throughout this paper, ``Granger precedence'' denotes predictive improvement in a time-series forecasting sense, not a causal mechanism.
8	This distinction is why we scope our central claim to ``token entropy Granger-precedes diversity collapse'' rather than asserting that token entropy \emph{causes} diversity collapse.
9	
10	\paragraph{Calibration scope and generalization.}
11	All FPR and FNR calibration results reported in this work are specific to our experimental setup: Pythia-410M~\cite{biderman2023pythia}, a WikiText-103 subset, $T{=}10$ generation cycles, and five contamination levels ($\alpha \in \{0.0, 0.25, 0.50, 0.75, 1.0\}$).
12	Generalization to other model architectures, datasets, or training protocols requires independent validation.
13	The consensus framework's structure---multi-method agreement combined with multi-seed replication---is intended to be applicable beyond this specific setting, but the operating thresholds ($K{\geq}4/5$ methods, $S{\geq}3/4$ seeds) are empirically calibrated and may require re-tuning under different conditions.
14	For instance, architectures with different tokenizer granularity or training dynamics could shift the balance between false positive and false negative rates at these thresholds.
15	Our ongoing GPT-2-medium experiments represent a first step toward cross-ar
…[truncated 4560 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T00:32:21.713550+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T00:32:21.713677+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Lead-lag analysis in iterative training collapse is far more fragile than the current literature assumes.
5	We demonstrated three pitfalls that undermine standard approaches: method choice alone swings FDR significance from 100\% to 25\% ($\kappa{=}0.185$), first-differencing exposes canary$\to$perplexity associations as entirely spurious ($F{\approx}0$, $p{=}0.99$), and regime dependence causes the same Granger test to shift from 24/24 to 0/8 significant pairs across contamination levels.
6	These findings establish that single-method, single-regime analyses---the current default---cannot reliably distinguish genuine temporal precedence from statistical artifacts.
7	
8	Our multi-method consensus framework addresses this fragility by requiring convergent evidence across ${\geq}4/5$ independent methods and ${\geq}3/4$ random seeds.
9	Calibrated on built-in experimental controls, the framework achieves 0\% false positive rate at the null control ($\alpha{=}0.0$) and 0\% false negative rate against ground-truth pairs at full contamination ($\alpha{=}1.0$), with four tiers of practical guidance scaling from exploratory screening to publication-grade claims.
10	
11	Applying the framework yields a concrete finding: token entropy serves as a one-generation-ahead canary for diversity collapse at $\alpha{=}1.0$ (with preliminary single-seed evidence at $\alpha{=}0.75$), with $|r|{>}0.99$ and complete directional asymmetry (0/24 reverse-direction FDR-significant pairs).
12	This result is deliberately scoped to lexical diversity, not model collapse broadly, since the perplexity channel proved entirely spurious under differencing.
13	
14	The methodological pitfalls we expose are not specific to our experimental setting---they arise from generic properties of short, non-stationary time series---and the consensus framework transfers directly to any domain where multiple detection methods can be applied in parallel.
15	Limitation
…[truncated 65 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T00:32:21.713807+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T00:32:21.713953+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse in iterative training.}
5	
6	The phenomenon of iterative training collapse was formalized by \citet{shumailov2024curse}, who showed that recursively replacing real data with model-generated text causes progressive tail erosion across VAEs, GMMs, and language models, and by \citet{alemohammad2024mad}, who demonstrated quality--diversity tradeoffs in self-consuming generative loops for image models.
7	Theoretical analyses have since sharpened these results: \citet{dohmatob2024tale} recast collapse as a change in scaling-law exponents, showing that even small fractions of synthetic data alter effective scaling behavior, while \citet{dohmatob2025strong} proved that collapse can occur even when synthetic data constitutes a vanishingly small fraction of the training set.
8	The role of data accumulation has been a central theme.
9	\citet{dey2024breaking} proved that accumulating data across generations---rather than replacing it---prevents divergence of population risk in GMMs, HMMs, and language models.
10	\citet{kazdan2025collapse} systematically compared replace and accumulate regimes, finding that synthetic data value depends on the absolute quantity of co-present real data.
11	\citet{fu2025selfconsuming} provided generalization bounds for self-consuming loops, establishing that a constant fraction of real data suffices for convergence under accumulation.
12	On the calibration side, \citet{he2025golden} showed that optimal real-data weighting converges to the golden-ratio inverse ($1/\varphi \approx 0.618$) in Gaussian and GLM settings, and that the risk landscape is non-monotone in mixing ratio---a theoretical prediction with implications for regime-dependent canary behavior.
13	Beyond distributional statistics, \citet{guo2024linguistic} documented progressive decline in lexical, syntactic, and semantic diversity across iterative fine-tuning generations, providing the multi-level divers
…[truncated 6723 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T00:32:21.714113+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/background.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T00:32:21.714273+00:00_

1	\section{Background}
2	\label{sec:background}
3	
4	This section establishes the formal setup and notation used throughout the paper.
5	
6	\paragraph{Iterative training loop.}
7	Let $M_0$ denote a pretrained language model and $\mathcal{D}_\text{real}$ a fixed corpus of human-written text.
8	At each generation $t \geq 1$, the model $M_{t-1}$ generates a synthetic corpus $\mathcal{D}_\text{synth}^{(t-1)}$, and the next-generation model $M_t$ is fine-tuned on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data:
9	\begin{equation}
10	    \mathcal{D}_\text{train}^{(t)} = \alpha \cdot \mathcal{D}_\text{synth}^{(t-1)} \;+\; (1{-}\alpha) \cdot \mathcal{D}_\text{real}, \quad \alpha \in [0, 1].
11	    \label{eq:mixing}
12	\end{equation}
13	The contamination level $\alpha$ controls the fraction of machine-generated text in each training round.
14	At $\alpha{=}1.0$, this reduces to the full-replacement paradigm of \citet{shumailov2024curse}, where each generation trains exclusively on the previous generation's output.
15	Iterating this process for $T$ generations yields a trajectory $M_0 \to M_1 \to \cdots \to M_T$.
16	
17	\paragraph{Metric families.}
18	We distinguish two families of metrics evaluated at each generation~$t$.
19	\emph{Canary metrics} are cheap-to-compute statistics on the model's output distribution, hypothesized to change before downstream quality degrades---analogous to early-warning indicators studied in the context of critical transitions in dynamical systems \cite{scheffer2009early}.
20	We consider two canary metrics: \emph{token entropy}, the average next-token prediction entropy over held-out samples, and \emph{expected calibration error} (ECE), which measures the discrepancy between predicted token probabilities and empirical correctness frequencies.
21	\emph{Downstream metrics} capture generation quality directly.
22	We use \emph{distinct-$n$} ($n \in \{1, 2, 3\}$), the ratio of unique $n$-grams to total $n$-grams in g
…[truncated 2290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T00:32:21.714621+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\nimport numpy as np\n\n# Registry data for α=1.0, 4 seeds (mvp_v4_rep42/43/44/45)\nseeds = {\n    42: {'entropy': -60.5491, 'ece': 3762.4711, 'ppl': 3624.5595, 'd1': -28.3386, 'd2': -35.2126, 'd3': -31.6402},\n    43: {'entropy': -61.0534, 'ece': 3782.5544, 'ppl': 3665.1176, 'd1': -28.4246, 'd2': -35.7628, 'd3': -33.0282},\n    44: {'entropy': -62.2629, 'ece': 3821.2402, 'ppl': 3733.7659, 'd1': -25.473, 'd2': -29.1286, 'd3': -24.6057},\n    45: {'entropy': -59.3296, 'ece': 3755.0671, 'ppl': 3670.9063, 'd1': -29.1304, 'd2': -35.9639, 'd3': -32.7352},\n}\n\nmetrics = ['entropy', 'ece', 'd1', 'd2', 'ppl']\npaper_means = {'entropy': -60.5, 'ece': 3862, 'd1': -25.3, 'd2': -29.7, 'ppl': 3690}\npaper_stds = {'entropy': 1.2, 'ece': 158, 'd1': 1.3, 'd2': 1.5, 'ppl': 320}\n\nfor m in metrics:\n    vals = [seeds[s][m] for s in [42,43,44,45]]\n    mean = np.mean(vals)\n    std = np.std(vals, ddof=1)\n    pm = paper_means[m]\n    ps = paper_stds[m]\n    match_mean = 'OK' if abs(mean - pm) < 0.5 * abs(pm) * 0.01 else 'MISMATCH'\n    match_std = 'OK' if abs(std - ps) < 0.5 * abs(ps) * 0.1 else 'MISMATCH'\n    print(f'{m:>10s}: registry mean={mean:+.1f}±{std:.1f} | paper={pm:+.0f}±{ps:.0f} | mean:{match_mean} std:{match_std}')\n    print(f'           values: {[round(v,2) for v in vals]}')\n\"\n",
  "description": "Verify α=1.0 4-seed statistics against paper values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\nimport numpy as np\n\n# Registry data for α=1.0, 4 seeds (mvp_v4_rep42/43/44/45)\nseeds = {\n    42: {'entropy': -60.5491, 'ece': 3762.4711, 'ppl': 3624.5595, 'd1': -28.3386, 'd2': -35.2126, 'd3': -31.6402},\n    43: {'entropy': -61.0534, 'ece': 3782.5544, 'ppl': 3665.1176, 'd1': -28.4246, 'd2': -35.7628, 'd3': -33.0282},\n    44: {'entropy': -62.2629, 'ece': 3821.2402, 'ppl': 3733.7659, 'd1': -25.473, 'd2': -29.1286, 'd3': -24.6057},\n    45: {'entropy': -59.3296, 'ece': 3755.0671, 'ppl': 3670.9063, 'd1': -29.1304, 'd2': -35.9639, 'd3': -32.7352},\n}\n\nmetrics = ['entropy', 'ece', 'd1', 'd2', 'ppl']\npaper_means = {'entropy': -60.5, 'ece': 3862, 'd1': -25.3, 'd2': -29.7, 'ppl': 3690}\npaper_stds = {'entropy': 1.2, 'ece': 158, 'd1': 1.3, 'd2': 1.5, 'ppl': 320}\n\nfor m in metrics:\n    vals = [seeds[s][m] for s in [42,43,44,45]]\n    mean = np.mean(vals)\n    std = np.std(vals, ddof=1)\n    pm = paper_means[m]\n    ps = paper_stds[m]\n    match_mean = 'OK' if abs(mean - pm) < 0.5 * abs(pm) * 0.01 else 'MISMATCH'\n    match_std = 'OK' if abs(std - ps) < 0.5 * abs(ps) * 0.1 else 'MISMATCH'\n    print(f'{m:>10s}: registry mean={mean:+.1f}±{std:.1f} | paper={pm:+.0f}±{ps:.0f} | mean:{match_mean} std:{match_std}')\n    print(f'           values: {[round(v,2) for v in vals]}')\n\"\n",
    "description": "Verify α=1.0 4-seed statistics against paper values"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T00:32:21.714798+00:00_

   entropy: registry mean=-60.8±1.2 | paper=-60±1 | mean:OK std:OK
           values: [-60.55, -61.05, -62.26, -59.33]
       ece: registry mean=+3780.3±29.6 | paper=+3862±158 | mean:MISMATCH std:MISMATCH
           values: [3762.47, 3782.55, 3821.24, 3755.07]
        d1: registry mean=-27.8±1.6 | paper=-25±1 | mean:MISMATCH std:MISMATCH
           values: [-28.34, -28.42, -25.47, -29.13]
        d2: registry mean=-34.0±3.3 | paper=-30±2 | mean:MISMATCH std:MISMATCH
           values: [-35.21, -35.76, -29.13, -35.96]
       ppl: registry mean=+3673.6±45.1 | paper=+3690±320 | mean:OK std:MISMATCH
           values: [3624.56, 3665.12, 3733.77, 3670.91]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T00:32:21.714959+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "-60\\.5|3862|25\\.3|29\\.7|3690",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Grep",
  "tool_args": {
    "pattern": "-60\\.5|3862|25\\.3|29\\.7|3690",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T00:32:21.715079+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T00:32:21.715194+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "FNR.*25\\\\%|25\\\\%.*FNR|FNR.*33",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Grep",
  "tool_args": {
    "pattern": "FNR.*25\\\\%|25\\\\%.*FNR|FNR.*33",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T00:32:21.715330+00:00_

artifacts/_project/paper/experiments.tex:173:Toda--Yamamoto alone yields FNR${=}$33.3\%, missing ECE$\to$distinct-2 and ECE$\to$distinct-3 due to Type~II errors at $T{=}10$.
artifacts/_project/paper/discussion.tex:27:The Toda-Yamamoto procedure's elevated FNR (33.3\%, missing 2 of 6 directional pairs) is attributable to insufficient residual degrees of freedom at this series length, not to a fundamental deficiency in the method itself.
artifacts/_project/paper/method.tex:100:At $K{=}5/5$, $S{\geq}3/4$, FNR rises to 33.3\% because Toda--Yamamoto misses two ECE pairs due to Type~II errors at $T{=}10$.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T00:32:21.715464+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/experiments.tex",
  "offset": "178",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/_project/paper/experiments.tex",
    "offset": "178",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T00:32:21.715596+00:00_

178	\begin{table}[t]
179	\centering
180	\small
181	\caption{False positive and false negative rates for individual methods and the consensus framework. FPR: $\alpha{=}0.0$ null control (single seed). FNR: $\alpha{=}1.0$ against 6 ground-truth pairs independently validated by first-differencing. Note dimension asymmetry: FPR is method-only; FNR is method$\times$seed joint (\S\ref{sec:consensus_validation}).}
182	\label{tab:fpr_fnr}
183	\begin{tabular}{lcc}
184	\toprule
185	Criterion & FPR ($\alpha{=}0.0$) & FNR ($\alpha{=}1.0$) \\
186	\midrule
187	Naive XCorr              & 100\%  & 0\%  \\
188	Differenced XCorr        & 37.5\% & 0\%  \\
189	Threshold Onset          & 62.5\% & 0\%  \\
190	Permutation Granger      & 0\%    & 0\%  \\
191	Toda--Yamamoto           & 0\%    & 33.3\% \\
192	\midrule
193	Consensus ($K{\geq}4/5$)              & 0\%    & 0\%  \\
194	Consensus ($K{\geq}4/5$, $S{\geq}3/4$) & 0\%    & 0\%  \\
195	\bottomrule
196	\end{tabular}
197	\end{table}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T00:32:21.715793+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T00:32:21.715919+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T00:32:21.716057+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/paper_consistency_audit.md",
  "content": "# Paper–Registry Consistency Audit\n\n**Date**: 2026-05-16\n**Paper location**: `artifacts/_project/paper/*.tex`\n**Registry**: `distrib_canary_collapse` (34 experiments)\n\n---\n\n## ❌ Critical Discrepancies\n\n### 1. Table 1 (tab:drift_summary) — α=1.0 row: 4-seed mean±std values are wrong\n\nThe α=1.0 row reports 4-seed mean±std, but the values do not match the registry data from `mvp_v4_rep42/43/44/45`.\n\n| Metric | Paper | Registry (computed) | Δ mean | Δ std |\n|--------|-------|-------------------|--------|-------|\n| Entropy drift (%) | −60.5±1.2 | −60.8±1.2 | 0.3 (minor) | OK |\n| ECE drift (%) | **+3862±158** | **+3780±30** | **82** | **128** |\n| Distinct-1 drift (%) | **−25.3±1.3** | **−27.8±1.6** | **2.5** | 0.3 |\n| Distinct-2 drift (%) | **−29.7±1.5** | **−34.0±3.3** | **4.3** | **1.8** |\n| Perplexity drift (%) | +3690±320 | +3674±45 | 16 (minor) | **275** |\n\n**Registry source values** (drift_pct from each seed):\n\n| Seed | Entropy | ECE | Distinct-1 | Distinct-2 | Perplexity |\n|------|---------|-----|-----------|-----------|-----------|\n| 42 | −60.55 | +3762.5 | −28.34 | −35.21 | +3624.6 |\n| 43 | −61.05 | +3782.6 | −28.42 | −35.76 | +3665.1 |\n| 44 | −62.26 | +3821.2 | −25.47 | −29.13 | +3733.8 |\n| 45 | −59.33 | +3755.1 | −29.13 | −35.96 | +3670.9 |\n\n**Impact**: This table is referenced by the experiments section (§4.2 Regime-Dependent Detectability). The qualitative conclusions are unaffected (direction and ordering preserved), but the exact numbers are wrong. ECE std is off by 5×, perplexity std by 7×.\n\n**Note**: All single-seed rows (α=0.0, 0.25, 0.50, 0.75) are perfectly consistent with registry — only the α=1.0 aggregated row has errors.\n\n---\n\n## ⚠️ Moderate Issues\n\n### 2. Discussion claims GPT-2-medium results \"not yet available\" — but registry shows completed experiment\n\n**Paper** (discussion.tex, line 15):\n> \"Our ongoing GPT-2-medium experiments represent a first step toward cross-architecture validation, though results are not yet available.\"\n\n**Registry**: `gen_wiki_gpt2m_a100_s42_v3` — status=DONE, conclusion=success (completed 2026-05-15T22:18). Full metrics available:\n- token_entropy_drift: −86.5%\n- ece_drift: +4543%\n- perplexity_drift: +44703%\n- five_method_forward_consensus: \"6/6 pairs at 4/5 methods (Tier 3)\"\n- perm_granger_forward: p_fdr=0.003, BH corrected\n- diff_xcorr_reverse: \"all p>0.18 (clean directional separation)\"\n- cross_arch_note: \"Replicates Pythia entropy-leads-diversity pattern at Tier 3 consensus\"\n\n**Impact**: The paper could be strengthened with cross-architecture validation data. Currently understates available evidence.\n\n### 3. Multi-seed data now partially available for α=0.25 and α=0.50\n\n**Paper** (experiments.tex, line 14):\n> \"other conditions use seed 42, with multi-seed replication in progress\"\n\n**Registry**:\n- α=0.25: seed 42 (done), seed 43 (done), seed 44 (running)\n- α=0.50: seed 42 (done), seed 43 (done)\n\nThe α=0.50 s43 results (drift_pct) closely match s42: ppl 21.1 vs 21.1, entropy −17.4 vs −18.6, d1 −36.5 vs −37.3. Cross-seed note: \"drift direction identical, magnitude <7% deviation.\"\n\n**Impact**: Could update the paper to report α=0.50 as 2-seed replicated. Minor because the paper already correctly hedges with \"in progress.\"\n\n---\n\n## ✅ Verified Consistent\n\n### Drift table — single-seed rows (all 5 metrics match exactly)\n\n| α | Entropy | ECE | Distinct-1 | Distinct-2 | Perplexity | Source |\n|---|---------|-----|-----------|-----------|-----------|--------|\n| 0.00 | −5.1 ✅ | +51.7 ✅ | −13.8 ✅ | −9.8 ✅ | −21.7 ✅ | alpha_sweep_a000_s42 |\n| 0.25 | −4.1 ✅ | +79.7 ✅ | −40.3 ✅ | −57.1 ✅ | −17.2 ✅ | alpha_sweep_a025_s42_v3 |\n| 0.50 | −18.6 ✅ | +842.8 ✅ | −37.3 ✅ | −51.5 ✅ | +21.1 ✅ | alpha_sweep_a050_s42 |\n| 0.75 | −27.7 ✅ | +1809.5 ✅ | −32.7 ✅ | −41.3 ✅ | +182.1 ✅ | alpha_sweep_a075_s42 |\n\n### Method ablation sig rates (method_ablation_phase1)\n\n| Method | Paper | Registry | Status |\n|--------|-------|----------|--------|\n| Naive XCorr | 16/16 (100%) | naive_sig=16/16 | ✅ |\n| Differenced XCorr | 14/16 (87.5%) | differenced_sig=14/16 | ✅ |\n| Threshold Onset | 9/16 (56.3%) | threshold_sig=9/16 | ✅ |\n| Perm. Granger | 6/16 (37.5%) | permutation_granger_sig=6/16 | ✅ |\n| Toda–Yamamoto | 4/16 (25.0%) | ty_sig=4/16 | ✅ |\n\n### Spurious-signal rates\n\n- 75% (5-method) — registry: spurious_rate_5method=0.75 ✅\n- 62.5% (4-method, excl. TY) — registry: spurious_rate_4method=0.625 ✅\n\n### Inter-method agreement\n\n- κ = 0.185 — registry: mean_inter_method_kappa=0.185 ✅\n\n### α=0.75 Granger p-values (alpha_sweep_a075_s42)\n\n| Pair | Paper | Registry | Status |\n|------|-------|----------|--------|\n| ECE→d1 | p_fdr=0.046 | granger_ece_to_d1_p_fdr=0.046 | ✅ |\n| ECE→d2 | p_fdr=0.046 | granger_ece_to_d2_p_fdr=0.046 | ✅ |\n| Entropy→d2 | p_fdr=0.048 | granger_entropy_to_d2_p_fdr=0.048 | ✅ |\n| Entropy→d1 | p_fdr=0.054 (borderline) | granger_entropy_to_d1_p_fdr=0.054 | ✅ |\n\n### α=0.75 Granger sig count\n\n- \"3/8 FDR-sig\" — registry: granger_fdr_sig_count=\"3/8\" ✅\n\n### Cross-α Perm. Granger sig rates (method_ablation_phase2)\n\n| α | Paper (Table 3) | Registry | Status |\n|---|-----------------|----------|--------|\n| 0.00 | 0% | perm_granger_sig_rate_a000_fdr=0 | ✅ |\n| 0.25 | 0% | perm_granger_sig_rate_a025_fdr=0 | ✅ |\n| 0.50 | 0% | perm_granger_sig_rate_a050_fdr=0 | ✅ |\n| 1.00 | 75% | perm_granger_sig_rate_a100_fdr=0.75 | ✅ |\n\n### Cross-α TY sig rates (method_ablation_phase2)\n\n| α | Paper (Table 3) | Registry | Status |\n|---|-----------------|----------|--------|\n| 0.00 | 0% | TY_sig_rate_a000_fdr=0 | ✅ |\n| 0.25 | 37.5% | TY_sig_rate_a025_fdr=0.375 | ✅ |\n| 0.50 | 0% | TY_sig_rate_a050_fdr=0 | ✅ |\n| 1.00 | 59.4% | TY_sig_rate_a100_fdr=0.5938 | ✅ |\n\n### Diff. XCorr at α=0.0\n\n- Paper: 37.5% — registry: diff_sig_rate_a000_fdr=0.375 ✅\n\n### FPR/FNR table (tab:fpr_fnr)\n\n| Criterion | Paper FPR | Paper FNR | Status |\n|-----------|-----------|-----------|--------|\n| Naive XCorr | 100% | 0% | ✅ consistent with phase2 |\n| Diff. XCorr | 37.5% | 0% | ✅ |\n| Threshold | 62.5% | 0% | ✅ |\n| Perm. Granger | 0% | 0% | ✅ |\n| TY | 0% | 33.3% | ✅ consistent with text |\n| Consensus K≥4/5 | 0% | 0% | ✅ |\n| Consensus K≥4/5, S≥3/4 | 0% | 0% | ✅ |\n\n### Practical guidance tiers (tab:practical_guidance)\n\n- Tier 1 FPR=100%: verified (naive alone flags all) ✅\n- Tier 3 FPR=0%, FNR=0%: verified ✅\n- Tier 4 FNR=50%: consistent with calibration text (K=5/5, S=4/4) ✅\n\n### Bootstrap TY power (plan_009_bootstrap_ty)\n\n- Paper: \"power of 0.05–0.20\" — registry: T10 power range 0.05–0.205 ✅\n\n### Experimental setup parameters\n\n| Parameter | Paper | Registry | Status |\n|-----------|-------|----------|--------|\n| Model | Pythia-410M | EleutherAI/pythia-410m | ✅ |\n| Data | WikiText-103 | data/wikitext103_5k | ✅ |\n| Samples/gen | 5,000 | data_count=5000 | ✅ |\n| Steps/gen | 5,000 | steps_per_gen=5000 | ✅ |\n| Generations | T=10 | num_generations=10 | ✅ |\n| α levels | {0.0, 0.25, 0.50, 0.75, 1.0} | all present | ✅ |\n| Seeds (α=1.0) | {42, 43, 44, 45} | 4 mvp_v4 experiments | ✅ |\n| Permutations | 5,000 | stated in paper | ✅ |\n\n### Pipeline filtering counts\n\n- Stage 1: 16 → Stage 2: 14 → Stage 3: 6 → Stage 4: 6 ✅\n  (Matches naive=16/16, diff=14/16, perm_granger=6/16)\n\n### Consensus counts in abstract/conclusion\n\n- 24/24 canary→diversity sig at α=1.0 (6 pairs × 4 seeds) ✅\n- 0/24 reverse-direction ✅ (consistent throughout paper)\n- 8/8 → 0/8 perplexity leads eliminated by differencing ✅\n\n---\n\n## ❓ Cannot Verify from Registry\n\nThese numbers appear in the paper but have no direct registry field to check against. They require access to the raw analysis output files on the server.\n\n- |r| > 0.99 for Pythia α=1.0 cross-correlation\n- All reverse-direction p > 0.49 (Pythia)\n- F = 16–36 for undifferenced canary→perplexity\n- F ≈ 0, p = 0.99 for differenced canary→perplexity\n- TY d_max sensitivity: 6%, 75%, 94% rejection rates\n- Table 3 entries: Diff. XCorr at α=0.25 (25%), Threshold at α=0.25 (37.5%)\n- FPR at K=2 (75%), K=3 (37.5%)\n- Pythia batch size = 4 (mentioned in discussion limitations)\n\n---\n\n## Summary\n\n| Category | Count | Details |\n|----------|-------|---------|\n| ❌ Critical | 1 | Table 1 α=1.0 row: mean±std values for ECE, d1, d2, ppl are wrong |\n| ⚠️ Moderate | 2 | GPT-2m results available but paper says \"not yet\"; multi-seed data partially available |\n| ✅ Verified | 40+ | All single-seed drifts, method ablation rates, p-values, κ, sig counts, FPR/FNR |\n| ❓ Unverifiable | 8 | Require raw analysis files on server |\n\n**Recommended action**: Fix Table 1 α=1.0 row using registry source data. Consider incorporating GPT-2-medium cross-architecture validation results into the discussion.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/paper_consistency_audit.md",
    "content": "# Paper–Registry Consistency Audit\n\n**Date**: 2026-05-16\n**Paper location**: `artifacts/_project/paper/*.tex`\n**Registry**: `distrib_canary_collapse` (34 experiments)\n\n---\n\n## ❌ Critical Discrepancies\n\n### 1. Table 1 (tab:drift_summary) — α=1.0 row: 4-seed mean±std values are wrong\n\nThe α=1.0 row reports 4-seed mean±std, but the values do not match the registry data from `mvp_v4_rep42/43/44/45`.\n\n| Metric | Paper | Registry (computed) | Δ mean | Δ std |\n|--------|-------|-------------------|--------|-------|\n| Entropy drift (%) | −60.5±1.2 | −60.8±1.2 | 0.3 (minor) | OK |\n| ECE drift (%) | **+3862±158** | **+3780±30** | **82** | **128** |\n| Distinct-1 drift (%) | **−25.3±1.3** | **−27.8±1.6** | **2.5** | 0.3 |\n| Distinct-2 drift (%) | **−29.7±1.5** | **−34.0±3.3** | **4.3** | **1.8** |\n| Perplexity drift (%) | +3690±320 | +3674±45 | 16 (minor) | **275** |\n\n**Registry source values** (drift_pct from each seed):\n\n| Seed | Entropy | ECE | Distinct-1 | Distinct-2 | Perplexity |\n|------|---------|-----|-----------|-----------|-----------|\n| 42 | −60.55 | +3762.5 | −28.34 | −35.21 | +3624.6 |\n| 43 | −61.05 | +3782.6 | −28.42 | −35.76 | +3665.1 |\n| 44 | −62.26 | +3821.2 | −25.47 | −29.13 | +3733.8 |\n| 45 | −59.33 | +3755.1 | −29.13 | −35.96 | +3670.9 |\n\n**Impact**: This table is referenced by the experiments section (§4.2 Regime-Dependent Detectability). The qualitative conclusions are unaffected (direction and ordering preserved), but the exact numbers are wrong. ECE std is off by 5×, perplexity std by 7×.\n\n**Note**: All single-seed rows (α=0.0, 0.25, 0.50, 0.75) are perfectly consistent with registry — only the α=1.0 aggregated row has errors.\n\n---\n\n## ⚠️ Moderate Issues\n\n### 2. Discussion claims GPT-2-medium results \"not yet available\" — but registry shows completed experiment\n\n**Paper** (discussion.tex, line 15):\n> \"Our ongoing GPT-2-medium experiments represent a first step toward cross-architecture validation, though results are not yet available.\"\n\n**Registry**: `gen_wiki_gpt2m_a100_s42_v3` — status=DONE, conclusion=success (completed 2026-05-15T22:18). Full metrics available:\n- token_entropy_drift: −86.5%\n- ece_drift: +4543%\n- perplexity_drift: +44703%\n- five_method_forward_consensus: \"6/6 pairs at 4/5 methods (Tier 3)\"\n- perm_granger_forward: p_fdr=0.003, BH corrected\n- diff_xcorr_reverse: \"all p>0.18 (clean directional separation)\"\n- cross_arch_note: \"Replicates Pythia entropy-leads-diversity pattern at Tier 3 consensus\"\n\n**Impact**: The paper could be strengthened with cross-architecture validation data. Currently understates available evidence.\n\n### 3. Multi-seed data now partially available for α=0.25 and α=0.50\n\n**Paper** (experiments.tex, line 14):\n> \"other conditions use seed 42, with multi-seed replication in progress\"\n\n**Registry**:\n- α=0.25: seed 42 (done), seed 43 (done), seed 44 (running)\n- α=0.50: seed 42 (done), seed 43 (done)\n\nThe α=0.50 s43 results (drift_pct) closely match s42: ppl 21.1 vs 21.1, entropy −17.4 vs −18.6, d1 −36.5 vs −37.3. Cross-seed note: \"drift direction identical, magnitude <7% deviation.\"\n\n**Impact**: Could update the paper to report α=0.50 as 2-seed replicated. Minor because the paper already correctly hedges with \"in progress.\"\n\n---\n\n## ✅ Verified Consistent\n\n### Drift table — single-seed rows (all 5 metrics match exactly)\n\n| α | Entropy | ECE | Distinct-1 | Distinct-2 | Perplexity | Source |\n|---|---------|-----|-----------|-----------|-----------|--------|\n| 0.00 | −5.1 ✅ | +51.7 ✅ | −13.8 ✅ | −9.8 ✅ | −21.7 ✅ | alpha_sweep_a000_s42 |\n| 0.25 | −4.1 ✅ | +79.7 ✅ | −40.3 ✅ | −57.1 ✅ | −17.2 ✅ | alpha_sweep_a025_s42_v3 |\n| 0.50 | −18.6 ✅ | +842.8 ✅ | −37.3 ✅ | −51.5 ✅ | +21.1 ✅ | alpha_sweep_a050_s42 |\n| 0.75 | −27.7 ✅ | +1809.5 ✅ | −32.7 ✅ | −41.3 ✅ | +182.1 ✅ | alpha_sweep_a075_s42 |\n\n### Method ablation sig rates (method_ablation_phase1)\n\n| Method | Paper | Registry | Status |\n|--------|-------|----------|--------|\n| Naive XCorr | 16/16 (100%) | naive_sig=16/16 | ✅ |\n| Differenced XCorr | 14/16 (87.5%) | differenced_sig=14/16 | ✅ |\n| Threshold Onset | 9/16 (56.3%) | threshold_sig=9/16 | ✅ |\n| Perm. Granger | 6/16 (37.5%) | permutation_granger_sig=6/16 | ✅ |\n| Toda–Yamamoto | 4/16 (25.0%) | ty_sig=4/16 | ✅ |\n\n### Spurious-signal rates\n\n- 75% (5-method) — registry: spurious_rate_5method=0.75 ✅\n- 62.5% (4-method, excl. TY) — registry: spurious_rate_4method=0.625 ✅\n\n### Inter-method agreement\n\n- κ = 0.185 — registry: mean_inter_method_kappa=0.185 ✅\n\n### α=0.75 Granger p-values (alpha_sweep_a075_s42)\n\n| Pair | Paper | Registry | Status |\n|------|-------|----------|--------|\n| ECE→d1 | p_fdr=0.046 | granger_ece_to_d1_p_fdr=0.046 | ✅ |\n| ECE→d2 | p_fdr=0.046 | granger_ece_to_d2_p_fdr=0.046 | ✅ |\n| Entropy→d2 | p_fdr=0.048 | granger_entropy_to_d2_p_fdr=0.048 | ✅ |\n| Entropy→d1 | p_fdr=0.054 (borderline) | granger_entropy_to_d1_p_fdr=0.054 | ✅ |\n\n### α=0.75 Granger sig count\n\n- \"3/8 FDR-sig\" — registry: granger_fdr_sig_count=\"3/8\" ✅\n\n### Cross-α Perm. Granger sig rates (method_ablation_phase2)\n\n| α | Paper (Table 3) | Registry | Status |\n|---|-----------------|----------|--------|\n| 0.00 | 0% | perm_granger_sig_rate_a000_fdr=0 | ✅ |\n| 0.25 | 0% | perm_granger_sig_rate_a025_fdr=0 | ✅ |\n| 0.50 | 0% | perm_granger_sig_rate_a050_fdr=0 | ✅ |\n| 1.00 | 75% | perm_granger_sig_rate_a100_fdr=0.75 | ✅ |\n\n### Cross-α TY sig rates (method_ablation_phase2)\n\n| α | Paper (Table 3) | Registry | Status |\n|---|-----------------|----------|--------|\n| 0.00 | 0% | TY_sig_rate_a000_fdr=0 | ✅ |\n| 0.25 | 37.5% | TY_sig_rate_a025_fdr=0.375 | ✅ |\n| 0.50 | 0% | TY_sig_rate_a050_fdr=0 | ✅ |\n| 1.00 | 59.4% | TY_sig_rate_a100_fdr=0.5938 | ✅ |\n\n### Diff. XCorr at α=0.0\n\n- Paper: 37.5% — registry: diff_sig_rate_a000_fdr=0.375 ✅\n\n### FPR/FNR table (tab:fpr_fnr)\n\n| Criterion | Paper FPR | Paper FNR | Status |\n|-----------|-----------|-----------|--------|\n| Naive XCorr | 100% | 0% | ✅ consistent with phase2 |\n| Diff. XCorr | 37.5% | 0% | ✅ |\n| Threshold | 62.5% | 0% | ✅ |\n| Perm. Granger | 0% | 0% | ✅ |\n| TY | 0% | 33.3% | ✅ consistent with text |\n| Consensus K≥4/5 | 0% | 0% | ✅ |\n| Consensus K≥4/5, S≥3/4 | 0% | 0% | ✅ |\n\n### Practical guidance tiers (tab:practical_guidance)\n\n- Tier 1 FPR=100%: verified (naive alone flags all) ✅\n- Tier 3 FPR=0%, FNR=0%: verified ✅\n- Tier 4 FNR=50%: consistent with calibration text (K=5/5, S=4/4) ✅\n\n### Bootstrap TY power (plan_009_bootstrap_ty)\n\n- Paper: \"power of 0.05–0.20\" — registry: T10 power range 0.05–0.205 ✅\n\n### Experimental setup parameters\n\n| Parameter | Paper | Registry | Status |\n|-----------|-------|----------|--------|\n| Model | Pythia-410M | EleutherAI/pythia-410m | ✅ |\n| Data | WikiText-103 | data/wikitext103_5k | ✅ |\n| Samples/gen | 5,000 | data_count=5000 | ✅ |\n| Steps/gen | 5,000 | steps_per_gen=5000 | ✅ |\n| Generations | T=10 | num_generations=10 | ✅ |\n| α levels | {0.0, 0.25, 0.50, 0.75, 1.0} | all present | ✅ |\n| Seeds (α=1.0) | {42, 43, 44, 45} | 4 mvp_v4 experiments | ✅ |\n| Permutations | 5,000 | stated in paper | ✅ |\n\n### Pipeline filtering counts\n\n- Stage 1: 16 → Stage 2: 14 → Stage 3: 6 → Stage 4: 6 ✅\n  (Matches naive=16/16, diff=14/16, perm_granger=6/16)\n\n### Consensus counts in abstract/conclusion\n\n- 24/24 canary→diversity sig at α=1.0 (6 pairs × 4 seeds) ✅\n- 0/24 reverse-direction ✅ (consistent throughout paper)\n- 8/8 → 0/8 perplexity leads eliminated by differencing ✅\n\n---\n\n## ❓ Cannot Verify from Registry\n\nThese numbers appear in the paper but have no direct registry field to check against. They require access to the raw analysis output files on the server.\n\n- |r| > 0.99 for Pythia α=1.0 cross-correlation\n- All reverse-direction p > 0.49 (Pythia)\n- F = 16–36 for undifferenced canary→perplexity\n- F ≈ 0, p = 0.99 for differenced canary→perplexity\n- TY d_max sensitivity: 6%, 75%, 94% rejection rates\n- Table 3 entries: Diff. XCorr at α=0.25 (25%), Threshold at α=0.25 (37.5%)\n- FPR at K=2 (75%), K=3 (37.5%)\n- Pythia batch size = 4 (mentioned in discussion limitations)\n\n---\n\n## Summary\n\n| Category | Count | Details |\n|----------|-------|---------|\n| ❌ Critical | 1 | Table 1 α=1.0 row: mean±std values for ECE, d1, d2, ppl are wrong |\n| ⚠️ Moderate | 2 | GPT-2m results available but paper says \"not yet\"; multi-seed data partially available |\n| ✅ Verified | 40+ | All single-seed drifts, method ablation rates, p-values, κ, sig counts, FPR/FNR |\n| ❓ Unverifiable | 8 | Require raw analysis files on server |\n\n**Recommended action**: Fix Table 1 α=1.0 row using registry source data. Consider incorporating GPT-2-medium cross-architecture validation results into the discussion.\n"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T00:32:21.716326+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/paper_consistency_audit.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T00:32:21.716477+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "paper_consistency_audit",
  "type": "report",
  "description": "Paper–Registry consistency audit for EMNLP 2026 submission. Found 1 critical issue (Table 1 α=1.0 row has wrong 4-seed mean±std), 2 moderate issues (GPT-2m results available but paper says not yet; multi-seed data partially available), 40+ verified numbers.",
  "project": "distrib_canary_collapse",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/paper_consistency_audit.md",
  "tags": "['paper', 'audit', 'consistency', 'emnlp2026']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "paper_consistency_audit",
    "type": "report",
    "description": "Paper–Registry consistency audit for EMNLP 2026 submission. Found 1 critical issue (Table 1 α=1.0 row has wrong 4-seed mean±std), 2 moderate issues (GPT-2m results available but paper says not yet; multi-seed data partially available), 40+ verified numbers.",
    "project": "distrib_canary_collapse",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/paper_consistency_audit.md",
    "tags": "['paper', 'audit', 'consistency', 'emnlp2026']"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-16T00:32:21.716637+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_608d86\", \"name\": \"paper_consistency_audit\", \"type\": \"report\", \"description\": \"Paper–Registry consistency audit for EMNLP 2026 submission. Found 1 critical issue (Table 1 α=1.0 row has wrong 4-seed mean±std), 2 moderate issues (GPT-2m results available but paper says not yet; multi-seed data partially available), 40+ verified numbers.\", \"path\": \"projects/distrib_canary_collapse/artifacts/_project/report/paper_consistency_audit.md\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T00:32:07.025497+00:00\", \"tags\": [\"paper\", \"audit\", \"consistency\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_consistency_audit_20260516T002041",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-16T00:32:21.716803+00:00_

审计完成。报告已写入 `artifacts/paper_consistency_audit.md`。

**关键发现：**

**❌ 1 个严重问题** — Table 1 (tab:drift_summary) 的 α=1.0 行，4-seed mean±std 与 registry 数据不一致：
- ECE drift: 论文写 +3862±158，实际 +3780±30（mean 偏 82，std 偏 5 倍）
- Distinct-1: 论文 −25.3，实际 −27.8（偏 2.5 个百分点）
- Distinct-2: 论文 −29.7，实际 −34.0（偏 4.3 个百分点）
- Perplexity std: 论文 ±320，实际 ±45（偏 7 倍）
- 其余 4 行（单 seed）全部精确匹配，问题仅出在聚合计算

**⚠️ 2 个中等问题** — Discussion 称 GPT-2m 结果 "not yet available"，但 registry 已有完整结果（Tier 3 consensus 复现）；α=0.25/0.50 已有部分 multi-seed 数据可纳入

**✅ 40+ 个数字验证通过** — 所有方法消融率、κ 值、Granger p 值、sig 计数、FPR/FNR、实验参数均与 registry 一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_consistency_audit_20260516T002041"
}
```

</details>

---
