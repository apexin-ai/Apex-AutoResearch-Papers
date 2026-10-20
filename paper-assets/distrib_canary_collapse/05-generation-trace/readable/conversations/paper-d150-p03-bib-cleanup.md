# paper d150 p03 bib cleanup

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 99
- **Recorded user turns:** 0
- **Tool calls:** 49
- **Original source:** `logs/chats/worker_paper_d150_p03_bib_cleanup_20260520T132043.jsonl`
- **Structured JSON:** [`77edaf4cbcb7ecc30a5d.json`](../../sessions/77/77edaf4cbcb7ecc30a5d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

99 recorded events

### Tool call

_source line 1 · 2026-05-20T13:28:10.759990+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T13:28:10.760507+00:00_

docs/paper/ethics.tex
docs/paper/background.tex
docs/paper/conclusion.tex
docs/paper/related_work_reframe.tex
docs/paper/discussion_reframe.tex
docs/paper/abstract.tex
docs/paper/discussion.tex
docs/paper/limitations.tex
docs/paper/related_work.tex
docs/paper/intro_reframe.tex
docs/paper/method.tex
docs/paper/method_reframe.tex
docs/paper/experiments_reframe.tex
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/experiments.tex
docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T13:28:10.760763+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T13:28:10.760966+00:00_

docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T13:28:10.761170+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract all cite keys from tex",
  "subagent_type": "Explore",
  "prompt": "I need to extract ALL citation keys from ALL .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/. \n\nSearch for all citation commands: \\cite, \\citep, \\citet, \\citealt, \\citealp, \\citeauthor, \\citeyear, and any other \\cite* variants. Note that a single cite command can contain multiple keys separated by commas like \\cite{key1, key2, key3}.\n\nUse grep with a broad pattern like `\\\\cite` to find ALL citation usages across all .tex files. Report every unique citation key found, and which file(s) each key appears in. Be very thorough - search \"very thorough\" breadth."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract all cite keys from tex",
    "subagent_type": "Explore",
    "prompt": "I need to extract ALL citation keys from ALL .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/. \n\nSearch for all citation commands: \\cite, \\citep, \\citet, \\citealt, \\citealp, \\citeauthor, \\citeyear, and any other \\cite* variants. Note that a single cite command can contain multiple keys separated by commas like \\cite{key1, key2, key3}.\n\nUse grep with a broad pattern like `\\\\cite` to find ALL citation usages across all .tex files. Report every unique citation key found, and which file(s) each key appears in. Be very thorough - search \"very thorough\" breadth."
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T13:28:10.761447+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T13:28:10.761865+00:00_

1	% ============================================================
2	% CORE MODEL COLLAPSE
3	% ============================================================
4	
5	@article{shumailov2024curse,
6	  title     = {The Curse of Recursion: Training on Generated Data Makes Models Forget},
7	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},
8	  journal   = {Nature},
9	  year      = {2024},
10	  url       = {https://arxiv.org/abs/2305.17493},
11	}
12	
13	@inproceedings{alemohammad2024mad,
14	  title     = {Self-Consuming Generative Models Go {MAD}},
15	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard},
16	  booktitle = {International Conference on Learning Representations},
17	  year      = {2024},
18	  url       = {https://arxiv.org/abs/2307.01850},
19	}
20	
21	@inproceedings{dohmatob2024tale,
22	  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},
23	  author    = {Dohmatob, Elvis and Feng, Yunzhen and others},
24	  booktitle = {International Conference on Machine Learning},
25	  year      = {2024},
26	  url       = {https://arxiv.org/abs/2402.07043},
27	}
28	
29	@inproceedings{dohmatob2025strong,
30	  title     = {Strong Model Collapse},
31	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
32	  booktitle = {International Conference on Learning Representations},
33	  year      = {2025},
34	  url       = {https://arxiv.org/abs/2410.04840},
35	}
36	
37	@inproceedings{guo2024linguistic,
38	  title     = {The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text},
39	  author    = {Guo, Yanzhu and Shang, Guokan and others},
40	  booktitle = {Findings of the Association for Computational Linguistics: {NAACL}},
41	  year      = {2024},
42	  url       = {https://arxiv.org/abs/2311.0
…[truncated 19998 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T13:28:10.762143+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Glob",
  "tool_args": {
    "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/**/*.tex"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T13:28:10.762375+00:00_

docs/paper/ethics.tex
docs/paper/background.tex
docs/paper/conclusion.tex
docs/paper/related_work_reframe.tex
docs/paper/discussion_reframe.tex
docs/paper/abstract.tex
docs/paper/discussion.tex
docs/paper/limitations.tex
docs/paper/related_work.tex
docs/paper/intro_reframe.tex
docs/paper/method.tex
docs/paper/method_reframe.tex
docs/paper/experiments_reframe.tex
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/experiments.tex
docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T13:28:10.762597+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/",
  "type": "tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/",
    "type": "tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T13:28:10.762867+00:00_

docs/paper/related_work.tex:5:Iterative training collapse was formalized by \citet{shumailov2024curse} and \citet{alemohammad2024mad}, who showed that recursively replacing real data with model-generated text causes progressive tail erosion.
docs/paper/related_work.tex:6:Theoretical analyses have sharpened these results: \citet{dohmatob2024tale} recast collapse as a change in scaling-law exponents, and \citet{dohmatob2025strong} proved that collapse can occur even at vanishingly small synthetic fractions.
docs/paper/related_work.tex:7:Several works have proposed monitoring metrics: \citet{du2026geometric} observe that calibration error rises before accuracy degrades, \citet{du2025scales} report ECE increases at 30\% contamination before accuracy drops, and \citet{gambetta2024surplexity} introduces surplexity as a collapse detector.
docs/paper/related_work.tex:8:We differ from the closest predecessor, \citet{du2026geometric}, in four respects: (i)~we compare an entire family of canary metrics; (ii)~we cross-validate across five statistical methods; (iii)~we map detectability as a function of contamination regime; and (iv)~we treat method-selection sensitivity itself as a primary finding.
docs/paper/related_work.tex:11:\citet{gu2024cmr} establish a scaling law for critical mixture ratios in continual pre-training, and \citet{gu2025datamixing} show that data mixing can induce phase transitions in knowledge acquisition---a direct theoretical analogue to our detection phase transition, where a critical mixing ratio separates qualitatively different detection regimes.
docs/paper/related_work.tex:14:\citet{scheffer2009early} established that systems approaching tipping points exhibit generic early-warning signals (rising autocorrelation and variance), while \citet{boettiger2012limits} quantified detection limits in short time series---directly relevant to iterative training where $T{=}5$--$20$.
docs/paper/related_work.tex:15:The standard framework for testing temporal prec
…[truncated 15144 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T13:28:10.763127+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T13:28:10.763375+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and canary metrics.}
5	Iterative training collapse was formalized by \citet{shumailov2024curse} and \citet{alemohammad2024mad}, who showed that recursively replacing real data with model-generated text causes progressive tail erosion.
6	Theoretical analyses have sharpened these results: \citet{dohmatob2024tale} recast collapse as a change in scaling-law exponents, and \citet{dohmatob2025strong} proved that collapse can occur even at vanishingly small synthetic fractions.
7	Several works have proposed monitoring metrics: \citet{du2026geometric} observe that calibration error rises before accuracy degrades, \citet{du2025scales} report ECE increases at 30\% contamination before accuracy drops, and \citet{gambetta2024surplexity} introduces surplexity as a collapse detector.
8	We differ from the closest predecessor, \citet{du2026geometric}, in four respects: (i)~we compare an entire family of canary metrics; (ii)~we cross-validate across five statistical methods; (iii)~we map detectability as a function of contamination regime; and (iv)~we treat method-selection sensitivity itself as a primary finding.
9	
10	\paragraph{Data mixing phase transitions.}
11	\citet{gu2024cmr} establish a scaling law for critical mixture ratios in continual pre-training, and \citet{gu2025datamixing} show that data mixing can induce phase transitions in knowledge acquisition---a direct theoretical analogue to our detection phase transition, where a critical mixing ratio separates qualitatively different detection regimes.
12	
13	\paragraph{Critical transitions and lead-lag methodology.}
14	\citet{scheffer2009early} established that systems approaching tipping points exhibit generic early-warning signals (rising autocorrelation and variance), while \citet{boettiger2012limits} quantified detection limits in short time series---directly relevant to iterative training where $T{=}5$--$20$.
15	The standard framework fo
…[truncated 857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T13:28:10.763627+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion_reframe.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion_reframe.tex"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T13:28:10.763849+00:00_

1	\section{Discussion and Conclusion}\label{sec:discussion}
2	
3	\paragraph{Granger precedence is not causation.}
4	Granger causality tests predictive improvement, not true causation~\cite{granger1969investigating,shojaie2022granger}: an unobserved process could independently drive both token entropy and diversity metrics.
5	Our central claim is scoped accordingly---``token entropy Granger-precedes diversity collapse''---and bivariate tests cannot exclude confounders; multivariate VAR models would be required to test for confounders directly.
6	
7	\paragraph{Practical utility paradox.}
8	The framework works best where it is least needed: at $\alpha{\geq}0.75$, PermG reliably detects canary precedence, but degradation is already severe; at $\alpha{\leq}0.45$, where early warning would be most valuable, detection remains null.
9	However, in realistic pipelines, contamination $\alpha$ is unknown and typically increases over time as web-scraped corpora accumulate machine-generated text.
10	A continuous monitoring dashboard would trigger when $\alpha$ crosses the detectability threshold, converting the static limitation into a temporal advantage.
11	The regime map itself is actionable: practitioners who know $\alpha{<}0.25$ should invest in data provenance rather than metric monitoring.
12	
13	\paragraph{Four-layer detection taxonomy.}
14	Our results suggest a layered taxonomy ordered by onset threshold:
15	(1)~distributional dimensionality (effective rank, onset $\alpha{\approx}0.10$);
16	(2)~distributional instability (entropy variance, suggestive at $\alpha{\approx}0.25$);
17	(3)~causal coupling (Granger-type, onset $\alpha_c{\approx}0.50$); and
18	(4)~dynamical stability (AC1, suggestive but not conclusive at $T{=}11$).
19	The 40-percentage-point gap between structural distortion (Layer~1) and causal evidence (Layer~3) constitutes the detection phase transition.
20	Layers~1 and~3 are established; Layers~2 and~4 require longer generation protocols ($T{\geq}50$; \citea
…[truncated 2250 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T13:28:10.764095+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T13:28:10.764376+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study lead-lag analysis pitfalls in iterative training collapse using Pythia-410M \cite{biderman2023pythia}, a 410M-parameter decoder-only language model.
8	Pythia provides a controlled setting: small enough for multi-seed experiments across thirteen contamination levels, yet large enough to exhibit meaningful generation-over-generation degradation.
9	Cross-architecture validation uses GPT-2-medium (345M parameters, also decoder-only), a second transformer family of similar scale; results are reported in \S\ref{sec:regime} and \S\ref{sec:discussion}.
10	Training data is drawn from WikiText-103 \cite{merity2017pointer}, using 5{,}000-sample subsets per generation.
11	
12	Our protocol follows the replace paradigm of \citet{shumailov2024curse}, adapted for mixed synthetic-real training at $\alpha{<}1.0$.
13	Each generation $t$ proceeds in three steps: (1)~fine-tune the generation-$(t{-}1)$ model for 5{,}000 steps on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data (AdamW optimizer, learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium); (2)~generate 5{,}000 synthetic samples from the fine-tuned model (temperature $1.0$, top-$k{=}50$, max length 512 tokens); (3)~fully replace the synthetic pool.
14	We run $T{=}10$ generations (11 time points including the generation-0 baseline) across six primary contamination levels $\alpha \in \{0.00, 0.10, 0.25, 0.50, 0.75, 1.00\}$ with multi-seed replication, plus seven single-seed probing points ($\alpha \in \{0.05, 0.30, 0.35, 0.40, 0.45, 0.55, 0.60\}$) to resolve the onset boundary, yielding a 13-point $\alpha$ grid.
15	The $\alpha{=}1.0$ condition uses four random seeds $\{42, 43, 44, 45\}$; $\alpha \in \{0.00, 0.25, 0.50, 0.75\}$ each use three seeds $\{42, 43, 44\}$; remaining levels use a single seed (42).
16	

…[truncated 13633 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T13:28:10.764628+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T13:28:10.764854+00:00_

1	\section{Discussion and Conclusion}\label{sec:discussion}
2	
3	\paragraph{Granger precedence is not causation.}
4	Granger causality tests predictive improvement, not true causation~\cite{granger1969investigating,shojaie2022granger}: an unobserved process could independently drive both token entropy and diversity metrics.
5	Our central claim is scoped accordingly---``token entropy Granger-precedes diversity collapse''---and bivariate tests cannot exclude confounders; multivariate VAR models would be required for confounder testing.
6	
7	\paragraph{Calibration scope.}
8	First-differencing exposes canary$\to$perplexity associations as entirely spurious ($F{\approx}0$, $p{=}0.99$) while preserving canary$\to$diversity leads (24/24$\to$24/24), confirming that the apparent perplexity association is a shared-trend artifact.
9	All canary claims are therefore scoped to diversity metrics only.
10	
11	\paragraph{Short time-series constraint.}
12	With $T{=}10$ (11 data points per series), our analyses operate near the lower bound of what standard methods require~\cite{boettiger2012limits}; threshold onset and Toda--Yamamoto are power-limited at this length (\S\ref{sec:method}).
13	Longer generation chains ($T{\geq}20$) are predicted by the $S \times R$ framework to left-shift $\alpha_c$ and smooth the transition; these predictions are under empirical verification.
14	
15	\paragraph{Regime interpretation.}
16	The four-regime dose-response---blind, onset, synchronous dip, detection---parallels hormetic patterns in toxicology~\cite{calabrese2003hormesis}, where opposing dose-dependent mechanisms produce non-monotonic responses.
17	At $\alpha{\approx}0.60$, temporal resolution $R \to 0$ (entropy and diversity respond within the same generation), suppressing detection despite rising signal, analogous to zero-lag Granger causality failure in synchronous systems.
18	Exploratory CSD analysis reveals a consistent pattern---canary metrics show rising autocorrelation (Kendall $\tau{=}0.
…[truncated 1320 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T13:28:10.765099+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work_reframe.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work_reframe.tex"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T13:28:10.765333+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and canary metrics.}
5	
6	Iterative training collapse was formalized by \citet{shumailov2024curse} for language models and by \citet{alemohammad2024mad} for image generation, establishing that recursive self-training erodes tail modes and reduces output diversity.
7	Theoretical analyses have since shown that even small synthetic fractions alter effective scaling-law exponents \cite{dohmatob2024tale}.
8	Several metrics have been proposed as early collapse indicators: calibration error \cite{du2026geometric,du2025scales}, surplexity \cite{gambetta2024surplexity}, spectral divergence \cite{sigma2026spectral}, topological persistence \cite{kalinowski2026topology}, and center-edge dynamics \cite{dces2026counter}.
9	Yet none of these analyses apply differencing tests to rule out spurious co-trending, cross-validate across multiple statistical methods, or apply false discovery rate correction when testing multiple metric pairs.
10	
11	\paragraph{Early-warning signals and lead-lag methodology.}
12	
13	The concept of early-warning indicators originates in ecology, where \citet{scheffer2009early} showed that systems approaching tipping points exhibit rising autocorrelation and variance independent of system-specific mechanisms.
14	\citet{boettiger2012limits} quantified the detection limits of such signals in short time series, a constraint directly relevant to iterative training where generation counts rarely exceed 20.
15	Granger causality \cite{granger1969investigating} provides the standard test for temporal precedence but produces spurious rejections on non-stationary series \cite{granger1974spurious}; the Toda--Yamamoto procedure \cite{toda1995statistical} restores valid inference at the cost of degrees of freedom \cite{shojaie2022granger}, a severe trade-off when $T{\leq}20$.
16	Yet these ecological and econometric tools have not been combined for model collapse; existing canary studies r
…[truncated 863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T13:28:10.765593+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T13:28:10.765834+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\paragraph{Methodological pitfalls.}
5	\label{sec:pitfalls}
6	Lead-lag analysis in iterative model collapse is fragile along three axes, each documented with data from \S\ref{sec:regime}--\ref{sec:dose_response}.
7	\emph{Method sensitivity}: five detection methods applied to identical data ($\alpha{=}1.0$, 8 validated canary$\to$downstream pairs, direction-checked) yield forward significance rates spanning 0\% to 75\%, with inter-method agreement at $\kappa{=}0.185$ and naive cross-correlation reaching 75\% null-control FPR.
8	\emph{Spurious regression}: first-differencing to remove shared trends~\cite{granger1974spurious} eliminates canary$\to$perplexity associations ($F{\approx}0$, $p{=}0.99$) while preserving canary$\to$diversity (24/24$\to$24/24), exposing an entire analysis channel as trend-driven rather than temporally precedent.
9	\emph{Regime dependence}: the same Granger test finds 0/8 pairs significant through $\alpha{=}0.45$ but 6/8 at $\alpha{=}0.50$, a categorical shift at a 5-percentage-point boundary that a single-$\alpha$ study would miss entirely.
10	These pitfalls motivate systematic method comparison rather than reliance on any single detection approach.
11	
12	\paragraph{Multi-Method Consensus Test (MMCT).}
13	\label{sec:mmct}
14	We apply the Multi-Method Consensus Test, a weighted consensus framework in the specification curve~\cite{simonsohn2020specification} and multi-method early-warning~\cite{scheffer2009early,bell2022modeling} traditions, adapted to the constraints of iterative training analysis: short series ($T{=}5$--$20$), non-stationarity by design, and heterogeneous method sensitivities.
15	MMCT is a consensus testing protocol, not a novel statistical method.
16	It compares five lead-lag detection methods through FPR-inverse weighted consensus, calibrated against null-control ($\alpha{=}0.0$) data where any detection is a false positive.
17	Each method $m_k$ receives weight $w_k = 1/\max(\ha
…[truncated 5517 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T13:28:10.766077+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T13:28:10.766294+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our experiments are validated at scales ${\leq}6.9$B parameters across six decoder-only transformer families; whether the temporal lead persists at frontier scale is open.
5	Training data is drawn from WikiText-103 and C4 subsets, three orders of magnitude smaller than production corpora; C4 results carry a pre-training data confound (Pythia was pre-trained on Pile, which overlaps with C4).
6	With $T{=}10$ (11 data points), threshold onset and Toda--Yamamoto are power-limited; $T{\geq}20$ validation is pending.
7	PermG requires null-control ($\alpha{=}0.0$) calibration data, which may not be available in all deployment settings.
8	The $\alpha{=}0.60$ results use bf16 precision from a single seed; fp32 multi-seed confirmation is needed.
9	Canary claims are scoped to distinct-$n$ diversity~\cite{li2016diversity}, not model collapse broadly~\cite{schaeffer2025position}; replace-only protocol means accumulate-mode dynamics~\cite{dey2024breaking} are untested.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T13:28:10.766533+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T13:28:10.766766+00:00_

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
19	\emph{Canary metrics} are cheap-to-compute statistics on the model's output distribution, hypothesized to change before downstream quality degrades, analogous to early-warning indicators studied in the context of critical transitions in dynamical systems \cite{scheffer2009early}.
20	We consider two canary metrics: \emph{token entropy}, the average next-token prediction entropy over held-out samples, and \emph{expected calibration error} (ECE), which measures the discrepancy between predicted token probabilities and empirical correctness frequencies.
21	\emph{Downstream metrics} capture generation quality directly.
22	We use \emph{distinct-$n$} ($n \in \{1, 2, 3\}$), the ratio of unique $n$-grams to total $n$-grams in ge
…[truncated 2279 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T13:28:10.767011+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T13:28:10.767249+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\paragraph{Methodological pitfalls.}
5	\label{sec:pitfalls}
6	Lead-lag analysis in iterative model collapse is fragile along three axes, each documented with data from \S\ref{sec:regime}--\ref{sec:dose_response}.
7	\emph{Method sensitivity}: five detection methods applied to identical data ($\alpha{=}1.0$, 16 canary$\to$downstream pairs) yield significance rates from 100\% (naive cross-correlation) to 37.5\% (permutation Granger), with inter-method agreement at $\kappa{=}0.185$ and a spurious-signal rate ${\geq}62.5\%$.
8	\emph{Spurious regression}: first-differencing to remove shared trends~\cite{granger1974spurious} eliminates canary$\to$perplexity associations ($F{\approx}0$, $p{=}0.99$) while preserving canary$\to$diversity (24/24$\to$24/24), exposing an entire analysis channel as trend-driven rather than temporally precedent.
9	\emph{Regime dependence}: the same Granger test finds 0/8 pairs significant through $\alpha{=}0.45$ but 6/8 at $\alpha{=}0.50$, a categorical shift at a 5-percentage-point boundary that a single-$\alpha$ study would miss entirely.
10	These pitfalls motivate systematic method comparison rather than reliance on any single detection approach.
11	
12	\paragraph{Multi-Method Consensus Test (MMCT).}
13	\label{sec:mmct}
14	We apply the Multi-Method Consensus Test, a weighted consensus framework in the specification curve~\cite{simonsohn2020specification} and multi-method early-warning~\cite{scheffer2009early,bell2022modeling} traditions, adapted to the constraints of iterative training analysis: short series ($T{=}5$--$20$), non-stationarity by design, and heterogeneous method sensitivities.
15	MMCT is a consensus testing protocol, not a novel statistical method.
16	It compares five lead-lag detection methods through FPR-inverse weighted consensus, calibrated against null-control ($\alpha{=}0.0$) data where any detection is a false positive.
17	Each method $m_k$ receives weight $w_k = 1/\max(\hat{\te
…[truncated 5538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T13:28:10.767547+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T13:28:10.767763+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/intro_reframe.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/intro_reframe.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T13:28:10.768112+00:00_

1	\appendix
2	
3	\section{Metric Drift Summary}
4	\label{app:drift}
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
10	\label{tab:drift_summary}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{lccccc}
13	\toprule
14	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
15	\midrule
16	0.00 & $-4.6{\pm}0.4$ & $+37.6{\pm}14$ & $-14.1{\pm}0.4$ & $-9.6{\pm}0.4$ & $-20.6{\pm}1.0$ \\
17	0.10$^\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\
18	0.25 & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & $-18.1{\pm}0.8$ \\
19	0.50 & $-18.0{\pm}0.5$ & $+822.6{\pm}18.3$ & $-37.1{\pm}0.4$ & $-50.4{\pm}1.0$ & $+21.0{\pm}0.1$ \\
20	0.75 & $-27.6{\pm}0.2$ & $+1791{\pm}18$ & $-32.3{\pm}0.5$ & $-41.0{\pm}1.0$ & $+182.6{\pm}0.7$ \\
21	1.00 & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & $+3674{\pm}45$ \\
22	\bottomrule
23	\end{tabular}}
24	\end{table}
25	
26	
27	\section{Distinct-3 Results}
28	\label{app:distinct3}
29	
30	Table~\ref{tab:distinct3_drift} reports distinct-3 drift across all contamination levels.
31	Distinct-3 exhibits the largest absolute decline among diversity metrics at low contamination ($-58.9{\pm}0.9\%$ at $\alpha{=}0.25$) but attenuates at higher levels ($-30.5\%$ at $\alpha{=}1.0$), consistent with the diversity--calibration dissociation discussed in \S\ref{sec:discussion}.
32	
33	\begin{table}[h]
34	\centering
35	\small
36	\caption{Distinct-3 drift (
…[truncated 25764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-20T13:28:10.768406+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\cite{shumailov2024curse,alemohammad2024mad}.
5	Lexical diversity narrows, calibration deteriorates, and each generation inherits the systematic biases of its predecessors.
6	As machine-generated text becomes prevalent on the web, such feedback loops pose a growing and often invisible risk to production training pipelines.
7	By the time standard quality metrics register degradation, the underlying distribution may have already shifted irreversibly.
8	This threat motivates the search for cheap-to-compute \emph{canary metrics}: leading indicators that signal distributional degradation before expensive downstream measures reveal the full extent of collapse.
9	The concept parallels early-warning signals for critical transitions in ecological systems~\cite{scheffer2009early,scheffer2012anticipating}, where proxy indicators allow intervention before a tipping point.
10	
11	Yet a fundamental question remains unanswered: \emph{at what contamination level does causal detection of collapse become possible?}
12	Whether a candidate canary genuinely \emph{precedes} downstream degradation or merely correlates with it under shared non-stationary trends depends on contamination regime and statistical method in ways that existing analyses leave unresolved.
13	Iterative training produces short, noisy time series (often fewer than 15 points per generation sequence), where detection power drops sharply and false positive rates can be high~\cite{boettiger2012limits}.
14	
15	We identify four deficiencies in existing lead-lag analyses of iterative training collapse.
16	(1)~No differencing tests rule out spurious regression from shared non-stationary trends~\cite{granger1974spurious}.
17	(2)~Conclusions rest on a single statistical method whose assumptions about stationarity and 
…[truncated 3742 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T13:28:10.768651+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T13:28:10.768876+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\cite{shumailov2024curse,alemohammad2024mad}.
5	Lexical diversity narrows, calibration deteriorates, and each generation inherits the systematic biases of its predecessors.
6	As machine-generated text becomes prevalent on the web, such feedback loops pose a growing and often invisible risk to production training pipelines.
7	By the time standard quality metrics register degradation, the underlying distribution may have already shifted irreversibly.
8	This threat motivates the search for cheap-to-compute \emph{canary metrics}: leading indicators that signal distributional degradation before expensive downstream measures reveal the full extent of collapse.
9	The concept parallels early-warning signals for critical transitions in ecological systems~\cite{scheffer2009early,scheffer2012anticipating}, where proxy indicators allow intervention before a tipping point.
10	
11	Yet a fundamental question remains unanswered: \emph{at what contamination level does causal detection of collapse become possible?}
12	Whether a candidate canary genuinely \emph{precedes} downstream degradation or merely correlates with it under shared non-stationary trends depends on contamination regime and statistical method in ways that existing analyses leave unresolved.
13	Iterative training produces short, noisy time series (often fewer than 15 points per generation sequence), where detection power drops sharply and false positive rates can be high~\cite{boettiger2012limits}.
14	
15	We identify four deficiencies in existing lead-lag analyses of iterative training collapse.
16	(1)~No differencing tests rule out spurious regression from shared non-stationary trends~\cite{granger1974spurious}.
17	(2)~Conclusions rest on a single statistical method whose assumptions about stationarity and 
…[truncated 3707 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T13:28:10.769123+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-20T13:28:10.769394+00:00_

1	\subsection{Detection Phase Transition}
2	\label{sec:regime}
3	
4	Diversity collapse occurs at every contamination level: distinct-1 declines by $14.1\%$ at $\alpha{=}0.0$ (fine-tuning drift) and by $40.3{\pm}0.3\%$ at $\alpha{=}0.25$ (3-seed mean).
5	Despite this ubiquitous degradation, causal detectability is sharply regime-dependent.
6	Permutation Granger (PermG) tests find 0/8 canary$\to$downstream pairs FDR-significant from $\alpha{=}0.00$ through $\alpha{=}0.45$, then jump to 6/8 at $\alpha{=}0.50$ (2~fp32 seeds, consistent).
7	This transition is striking because cumulative synthetic fraction barely changes across the boundary: $C = 1{-}(1{-}\alpha)^{10}$ yields $99.75\%$ at $\alpha{=}0.45$ versus $99.90\%$ at $\alpha{=}0.50$, a difference of 0.15 percentage points, yet detection jumps from null to reliable.
8	Sigmoid regression across the 13-point $\alpha$ grid quantifies this steep onset: $\alpha_c = 0.476$ at $T{=}10$, steepness $k \geq 200$, transition width $\Delta\alpha \approx 0.02$, $R^2 = 0.969$ (versus power-law $R^2 = 0.808$, $\Delta\mathrm{AIC} = 18.2$; Figure~\ref{fig:phase_transition}).
9	At $\alpha{=}0.45$, PermG $p$-values reveal sub-threshold signal ($p_{\mathrm{fdr}} = 0.059$ for seed~43, $0.091$ for seed~42), consistent with the power-threshold interpretation of $\alpha_c$ at $T{=}10$ (\S\ref{sec:theory}): the onset reflects PermG's power curve crossing the detection floor, not the emergence of a new physical signal.
10	A specification curve analysis spanning 1{,}160 analytical specifications confirms that the detection phase transition is specification-invariant.
11	
12	First-differencing scopes the canary claim precisely.
13	Canary$\to$diversity pairs retain unanimous FDR significance after first-differencing ($24/24 \to 24/24$ across 4~seeds at $\alpha{=}1.0$), while canary$\to$perplexity collapses entirely ($F \approx 0$, $p = 0.99$): the apparent perplexity association is a shared-trend artifact.
14	All canary claims are therefore sco
…[truncated 9504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T13:28:10.769632+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ethics.tex"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-20T13:28:10.769841+00:00_

1	\section*{Ethics Statement and AI Writing Disclosure}
2	
3	\paragraph{AI writing assistance.}
4	This paper was drafted with assistance from Claude (Anthropic), used for LaTeX formatting, literature search, and iterative revision.
5	All scientific claims, experimental design decisions, data analysis, and interpretations are the sole responsibility of the authors.
6	The AI assistant did not design experiments, run code, or make editorial judgments about which results to include or exclude.
7	
8	\paragraph{Responsible NLP considerations.}
9	This work studies degradation in iterative language model training.
10	We do not release models trained on synthetic data, as they exhibit reduced diversity and calibration.
11	Our findings highlight a failure mode relevant to the responsible deployment of language models: unmonitored iterative training on web-crawled data (which increasingly contains LLM outputs) may degrade model quality in ways detectable only through the multi-method framework we propose.
12	We encourage practitioners to implement canary monitoring in production training pipelines as a safeguard against silent quality degradation.
13	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T13:28:10.770064+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-20T13:28:10.770288+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Lead-lag analysis in iterative training collapse is far more fragile than the current literature assumes.
5	Method choice alone inflates spurious-signal rates to at least 62.5\%, first-differencing exposes canary$\to$perplexity associations as entirely spurious, and regime dependence causes the same Granger test to shift from 24/24 to 0/8 significant pairs across contamination levels.
6	These pitfalls establish that single-method, single-regime analyses (the current default) cannot reliably distinguish genuine temporal precedence from statistical artifacts.
7	
8	Our systematic five-method comparison through the Multi-Method Consensus Test (MMCT) identifies permutation Granger causality as the recommended detection method: it is the only one combining zero null-control FPR with high sensitivity, exhibiting a clean step-function dose-response from 0/8 (blind spot, $\alpha{\leq}0.45$) to 6/8 (onset, $\alpha{=}0.50$) with reliable detection at $\alpha{\geq}0.75$.
9	The other four methods each fail in characteristic ways: naive cross-correlation inflates FPR to 75\%, differenced cross-correlation cannot separate forward from reverse precedence, threshold onset is power-limited at $T{=}10$ under $3\sigma$ calibration, and Toda--Yamamoto Granger achieves moderate detection (3--4/8 at $\alpha{\geq}0.50$) as a supplementary method.
10	
11	Applying permutation Granger, token entropy exhibits robust one-generation-ahead precedence over diversity collapse at $\alpha{=}1.0$ on WikiText-103 (24/24 forward, 0/24 reverse across 4~seeds, replicated on GPT-2-medium and OPT-1.3B), with cross-architecture validation confirming detection (${\geq}6/8$) in 13 of 15 model-seed combinations spanning six families (345M--6.9B).
12	Directional asymmetry is domain-dependent: consistent unidirectionality holds on WikiText across all regimes, while C4 exhibits near-symmetric bidirectional coupling at $\alpha{=}0.50$ (PermG reverse 7/8), though 
…[truncated 753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T13:28:10.770541+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-20T13:28:10.770755+00:00_

1	\begin{abstract}
2	In iterative training on synthetic data, causal detection of collapse does not track cumulative contamination: at 99.75\% total synthetic exposure, no canary-downstream metric pair shows significant Granger precedence (0/8); at 99.90\%---a mere 0.15 percentage points more---detection jumps to 6/8 (dual-seed confirmed).
3	This \emph{detection phase transition} at $T{=}10$ (sigmoid $R^2{=}0.969$, $\alpha_c{=}0.476$, $\Delta\alpha{\approx}0.02$; transition steepness predicted T-dependent by the statistical power interpretation below) reveals that detectability is governed by per-generation mixing ratio, not cumulative contamination, and establishes a four-regime dose-response: blind ($\alpha{\leq}0.45$), onset ($\alpha{\approx}0.50$), synchronous dip ($\alpha{\approx}0.60$), and detection ($\alpha{\geq}0.75$).
4	A signal-times-resolution ($S \times R$) framework explains the non-monotonic pattern---signal strength rises monotonically but temporal resolution drops when relaxation time matches the observation interval---and a statistical power interpretation predicts three testable consequences for longer chains ($T{=}20$): left-shift of $\alpha_c$, transition smoothing, and method-dependent thresholds.
5	The discovery is enabled by a multi-method consensus framework (MMCT) comparing five statistical methods, which reveals that method choice alone inflates spurious-signal rates to 75\% and first-differencing eliminates all canary$\to$perplexity associations while preserving canary$\to$diversity leads (24/24$\to$24/24).
6	Permutation Granger causality (PermG) is the only method combining zero null-control FPR with high sensitivity; applied to Pythia-410M and validated across 15 model-seed combinations spanning six families (345M--6.9B), it identifies token entropy as a one-generation-ahead canary for diversity collapse (24/24 forward, 0/24 reverse at $\alpha{=}1.0$).
7	Canary-based predictive cessation reduces peak perplexity by 58\% compared to react
…[truncated 31 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T13:28:10.770999+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-20T13:28:10.771199+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{graphicx}
13	\usepackage{booktabs}
14	\usepackage{subcaption}
15	\usepackage{algorithm}
16	\usepackage{algpseudocode}
17	
18	\title{A Detection Phase Transition in Iterative Model Collapse}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	\input{introduction}
27	\input{related_work}
28	\input{method}
29	\input{experiments}
30	\input{discussion}
31	\input{limitations}
32	\input{ethics}
33	
34	\bibliography{references}
35	
36	\input{appendix}
37	
38	\end{document}
39	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T13:28:10.771528+00:00_

Perfect! Now I have extracted all the content from all .tex files. Let me compile a comprehensive list of all unique citation keys found in the paper. Based on my thorough analysis of all .tex files, here is the complete extraction of citation keys:

## COMPLETE CITATION KEY EXTRACTION

Below are ALL unique citation keys found across ALL .tex files in `/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/`:

### Unique Citation Keys (Alphabetically Sorted):

1. **alemohammad2024mad** - Found in: introduction.tex, intro_reframe.tex, related_work.tex, related_work_reframe.tex
2. **bell2022modeling** - Found in: related_work.tex, related_work_reframe.tex, method.tex, method_reframe.tex
3. **biderman2023pythia** - Found in: experiments.tex, introduction.tex, intro_reframe.tex
4. **boettiger2012limits** - Found in: background.tex, introduction.tex, intro_reframe.tex, method.tex, method_reframe.tex, related_work.tex, related_work_reframe.tex
5. **calabrese2003hormesis** - Found in: discussion.tex
6. **coretta2023multidimensional** - Found in: related_work.tex, related_work_reframe.tex
7. **dakos2012methods** - Found in: discussion_reframe.tex
8. **dces2026counter** - Found in: appendix.tex, related_work_reframe.tex
9. **dey2024breaking** - Found in: appendix.tex, limitations.tex
10. **dohmatob2024tale** - Found in: related_work.tex
11. **dohmatob2025strong** - Found in: related_work.tex
12. **du2025scales** - Found in: appendix.tex, related_work.tex, related_work_reframe.tex
13. **du2026geometric** - Found in: appendix.tex, related_work.tex, related_work_reframe.tex
14. **gambetta2024surplexity** - Found in: appendix.tex, related_work.tex, related_work_reframe.tex
15. **granger1969investigating** - Found in: background.tex, discussion.tex, discussion_reframe.tex, method.tex, method_reframe.tex, related_work.tex, related_work_reframe.tex
16. **granger1974spurious** - Found in: background.tex, discussion.tex, discussion_reframe.tex, in
…[truncated 3607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Agent",
  "elapsed_ms": 10
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T13:28:10.771865+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -ohP '\\\\\\\\cite[a-z]*\\{[^}]+\\}' docs/paper/*.tex | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "Extract all unique cite keys from tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -ohP '\\\\\\\\cite[a-z]*\\{[^}]+\\}' docs/paper/*.tex | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
    "description": "Extract all unique cite keys from tex files"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T13:28:10.772069+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T13:28:10.772281+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -ohP '@\\w+\\{([^,]+),' docs/paper/references.bib | sed 's/@[^{]*{//;s/,$//' | sort -u",
  "description": "Extract all bib entry keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -ohP '@\\w+\\{([^,]+),' docs/paper/references.bib | sed 's/@[^{]*{//;s/,$//' | sort -u",
    "description": "Extract all bib entry keys"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T13:28:10.772492+00:00_

alemohammad2024mad
bell2022modeling
biderman2023pythia
boettiger2012limits
calabrese2003hormesis
cao2025entropycal
coretta2023multidimensional
dakos2012methods
dces2026counter
deshpande2010instantaneous
dey2024breaking
dohare2024plasticity
dohmatob2024tale
dohmatob2025strong
du2025scales
du2026geometric
falahati2026curated
fu2025selfconsuming
gambetta2024surplexity
gao2021pile
granger1969investigating
granger1974spurious
gu2024cmr
gu2025datamixing
guo2024linguistic
hataya2023will
he2025golden
kalinowski2026topology
kapoor2024reforms
kazdan2025collapse
li2016diversity
lyle2023plasticity
marcinkevics2022neural
merity2017pointer
roy2007effective
ruiz2026causalaudit
sahoo2026calibration
schaeffer2025position
scheffer2009early
scheffer2012anticipating
schreiber2000measuring
seddik2024bad
shojaie2022granger
shumailov2024curse
sigma2026spectral
simonsohn2020specification
titus2020speeding
toda1995statistical
truong2025entropy
yi2026causalcompass

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T13:28:10.772696+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T13:28:10.772894+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	
10	\usepackage{amsmath}
11	\usepackage{amssymb}
12	\usepackage{graphicx}
13	\usepackage{booktabs}
14	\usepackage{subcaption}
15	\usepackage{algorithm}
16	\usepackage{algpseudocode}
17	
18	\title{A Detection Phase Transition in Iterative Model Collapse}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	\input{introduction}
27	\input{related_work}
28	\input{method}
29	\input{experiments}
30	\input{discussion}
31	\input{limitations}
32	\input{ethics}
33	
34	\bibliography{references}
35	
36	\input{appendix}
37	
38	\end{document}
39	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T13:28:10.773154+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -ohP '\\\\cite[a-z]*\\{[^}]+\\}' docs/paper/*.tex | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "Extract all unique cite keys from tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -ohP '\\\\cite[a-z]*\\{[^}]+\\}' docs/paper/*.tex | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
    "description": "Extract all unique cite keys from tex files"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T13:28:10.773388+00:00_

alemohammad2024mad
bell2022modeling
biderman2023pythia
boettiger2012limits
calabrese2003hormesis
coretta2023multidimensional
dakos2012methods
dces2026counter
dey2024breaking
dohmatob2024tale
dohmatob2025strong
du2025scales
du2026geometric
gambetta2024surplexity
granger1969investigating
granger1974spurious
gu2024cmr
gu2025datamixing
kalinowski2026topology
kapoor2024reforms
li2016diversity
merity2017pointer
schaeffer2025position
scheffer2009early
scheffer2012anticipating
shojaie2022granger
shumailov2024curse
sigma2026spectral
simonsohn2020specification
toda1995statistical

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T13:28:10.773650+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -ohP '\\\\cite[a-z]*\\{[^}]+\\}' docs/paper/abstract.tex docs/paper/introduction.tex docs/paper/related_work.tex docs/paper/method.tex docs/paper/experiments.tex docs/paper/discussion.tex docs/paper/limitations.tex docs/paper/ethics.tex docs/paper/appendix.tex docs/paper/background.tex | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "Extract cite keys from only active tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -ohP '\\\\cite[a-z]*\\{[^}]+\\}' docs/paper/abstract.tex docs/paper/introduction.tex docs/paper/related_work.tex docs/paper/method.tex docs/paper/experiments.tex docs/paper/discussion.tex docs/paper/limitations.tex docs/paper/ethics.tex docs/paper/appendix.tex docs/paper/background.tex | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
    "description": "Extract cite keys from only active tex files"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T13:28:10.773863+00:00_

alemohammad2024mad
bell2022modeling
biderman2023pythia
boettiger2012limits
calabrese2003hormesis
coretta2023multidimensional
dces2026counter
dey2024breaking
dohmatob2024tale
dohmatob2025strong
du2025scales
du2026geometric
gambetta2024surplexity
granger1969investigating
granger1974spurious
gu2024cmr
gu2025datamixing
kapoor2024reforms
li2016diversity
merity2017pointer
schaeffer2025position
scheffer2009early
scheffer2012anticipating
shojaie2022granger
shumailov2024curse
sigma2026spectral
simonsohn2020specification
toda1995statistical

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T13:28:10.774105+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r '\\\\input{background}' docs/paper/*.tex",
  "description": "Check if background.tex is included by any active file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r '\\\\input{background}' docs/paper/*.tex",
    "description": "Check if background.tex is included by any active file"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T13:28:10.774334+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-20T13:28:10.774579+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -ohP '\\\\cite[a-z]*\\{[^}]+\\}' docs/paper/abstract.tex docs/paper/introduction.tex docs/paper/related_work.tex docs/paper/method.tex docs/paper/experiments.tex docs/paper/discussion.tex docs/paper/limitations.tex docs/paper/ethics.tex docs/paper/appendix.tex | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "Extract cite keys from only 9 active tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -ohP '\\\\cite[a-z]*\\{[^}]+\\}' docs/paper/abstract.tex docs/paper/introduction.tex docs/paper/related_work.tex docs/paper/method.tex docs/paper/experiments.tex docs/paper/discussion.tex docs/paper/limitations.tex docs/paper/ethics.tex docs/paper/appendix.tex | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u",
    "description": "Extract cite keys from only 9 active tex files"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-20T13:28:10.774789+00:00_

alemohammad2024mad
bell2022modeling
biderman2023pythia
boettiger2012limits
calabrese2003hormesis
coretta2023multidimensional
dces2026counter
dey2024breaking
dohmatob2024tale
dohmatob2025strong
du2025scales
du2026geometric
gambetta2024surplexity
granger1969investigating
granger1974spurious
gu2024cmr
gu2025datamixing
kapoor2024reforms
li2016diversity
merity2017pointer
schaeffer2025position
scheffer2009early
scheffer2012anticipating
shojaie2022granger
shumailov2024curse
sigma2026spectral
simonsohn2020specification
toda1995statistical

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-20T13:28:10.775072+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "comm -23 <(grep -ohP '@\\w+\\{([^,]+),' docs/paper/references.bib | sed 's/@[^{]*{//;s/,$//' | sort -u) <(grep -ohP '\\\\cite[a-z]*\\{[^}]+\\}' docs/paper/abstract.tex docs/paper/introduction.tex docs/paper/related_work.tex docs/paper/method.tex docs/paper/experiments.tex docs/paper/discussion.tex docs/paper/limitations.tex docs/paper/ethics.tex docs/paper/appendix.tex | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u)",
  "description": "Compute orphan bib entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Bash",
  "tool_args": {
    "command": "comm -23 <(grep -ohP '@\\w+\\{([^,]+),' docs/paper/references.bib | sed 's/@[^{]*{//;s/,$//' | sort -u) <(grep -ohP '\\\\cite[a-z]*\\{[^}]+\\}' docs/paper/abstract.tex docs/paper/introduction.tex docs/paper/related_work.tex docs/paper/method.tex docs/paper/experiments.tex docs/paper/discussion.tex docs/paper/limitations.tex docs/paper/ethics.tex docs/paper/appendix.tex | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u)",
    "description": "Compute orphan bib entries"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-20T13:28:10.775306+00:00_

cao2025entropycal
dakos2012methods
deshpande2010instantaneous
dohare2024plasticity
falahati2026curated
fu2025selfconsuming
gao2021pile
guo2024linguistic
hataya2023will
he2025golden
kalinowski2026topology
kazdan2025collapse
lyle2023plasticity
marcinkevics2022neural
roy2007effective
ruiz2026causalaudit
sahoo2026calibration
schreiber2000measuring
seddik2024bad
titus2020speeding
truong2025entropy
yi2026causalcompass

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-20T13:28:10.775554+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-20T13:28:10.775787+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and canary metrics.}
5	Iterative training collapse was formalized by \citet{shumailov2024curse} and \citet{alemohammad2024mad}, who showed that recursively replacing real data with model-generated text causes progressive tail erosion.
6	Theoretical analyses have sharpened these results: \citet{dohmatob2024tale} recast collapse as a change in scaling-law exponents, and \citet{dohmatob2025strong} proved that collapse can occur even at vanishingly small synthetic fractions.
7	Several works have proposed monitoring metrics: \citet{du2026geometric} observe that calibration error rises before accuracy degrades, \citet{du2025scales} report ECE increases at 30\% contamination before accuracy drops, and \citet{gambetta2024surplexity} introduces surplexity as a collapse detector.
8	We differ from the closest predecessor, \citet{du2026geometric}, in four respects: (i)~we compare an entire family of canary metrics; (ii)~we cross-validate across five statistical methods; (iii)~we map detectability as a function of contamination regime; and (iv)~we treat method-selection sensitivity itself as a primary finding.
9	
10	\paragraph{Data mixing phase transitions.}
11	\citet{gu2024cmr} establish a scaling law for critical mixture ratios in continual pre-training, and \citet{gu2025datamixing} show that data mixing can induce phase transitions in knowledge acquisition---a direct theoretical analogue to our detection phase transition, where a critical mixing ratio separates qualitatively different detection regimes.
12	
13	\paragraph{Critical transitions and lead-lag methodology.}
14	\citet{scheffer2009early} established that systems approaching tipping points exhibit generic early-warning signals (rising autocorrelation and variance), while \citet{boettiger2012limits} quantified detection limits in short time series---directly relevant to iterative training where $T{=}5$--$20$.
15	The standard framework fo
…[truncated 857 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-20T13:28:10.776048+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-20T13:28:10.776349+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\paragraph{Methodological pitfalls.}
5	\label{sec:pitfalls}
6	Lead-lag analysis in iterative model collapse is fragile along three axes, each documented with data from \S\ref{sec:regime}--\ref{sec:dose_response}.
7	\emph{Method sensitivity}: five detection methods applied to identical data ($\alpha{=}1.0$, 8 validated canary$\to$downstream pairs, direction-checked) yield forward significance rates spanning 0\% to 75\%, with inter-method agreement at $\kappa{=}0.185$ and naive cross-correlation reaching 75\% null-control FPR.
8	\emph{Spurious regression}: first-differencing to remove shared trends~\cite{granger1974spurious} eliminates canary$\to$perplexity associations ($F{\approx}0$, $p{=}0.99$) while preserving canary$\to$diversity (24/24$\to$24/24), exposing an entire analysis channel as trend-driven rather than temporally precedent.
9	\emph{Regime dependence}: the same Granger test finds 0/8 pairs significant through $\alpha{=}0.45$ but 6/8 at $\alpha{=}0.50$, a categorical shift at a 5-percentage-point boundary that a single-$\alpha$ study would miss entirely.
10	These pitfalls motivate systematic method comparison rather than reliance on any single detection approach.
11	
12	\paragraph{Multi-Method Consensus Test (MMCT).}
13	\label{sec:mmct}
14	We apply the Multi-Method Consensus Test, a weighted consensus framework in the specification curve~\cite{simonsohn2020specification} and multi-method early-warning~\cite{scheffer2009early,bell2022modeling} traditions, adapted to the constraints of iterative training analysis: short series ($T{=}5$--$20$), non-stationarity by design, and heterogeneous method sensitivities.
15	MMCT is a consensus testing protocol, not a novel statistical method.
16	It compares five lead-lag detection methods through FPR-inverse weighted consensus, calibrated against null-control ($\alpha{=}0.0$) data where any detection is a false positive.
17	Each method $m_k$ receives weight $w_k = 1/\max(\ha
…[truncated 5741 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-20T13:28:10.776594+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-20T13:28:10.777085+00:00_

1	\appendix
2	
3	\section{Metric Drift Summary}
4	\label{app:drift}
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
10	\label{tab:drift_summary}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{lccccc}
13	\toprule
14	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
15	\midrule
16	0.00 & $-4.6{\pm}0.4$ & $+37.6{\pm}14$ & $-14.1{\pm}0.4$ & $-9.6{\pm}0.4$ & $-20.6{\pm}1.0$ \\
17	0.10$^\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\
18	0.25 & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & $-18.1{\pm}0.8$ \\
19	0.50 & $-18.0{\pm}0.5$ & $+822.6{\pm}18.3$ & $-37.1{\pm}0.4$ & $-50.4{\pm}1.0$ & $+21.0{\pm}0.1$ \\
20	0.75 & $-27.6{\pm}0.2$ & $+1791{\pm}18$ & $-32.3{\pm}0.5$ & $-41.0{\pm}1.0$ & $+182.6{\pm}0.7$ \\
21	1.00 & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & $+3674{\pm}45$ \\
22	\bottomrule
23	\end{tabular}}
24	\end{table}
25	
26	
27	\section{Distinct-3 Results}
28	\label{app:distinct3}
29	
30	Table~\ref{tab:distinct3_drift} reports distinct-3 drift across all contamination levels.
31	Distinct-3 exhibits the largest absolute decline among diversity metrics at low contamination ($-58.9{\pm}0.9\%$ at $\alpha{=}0.25$) but attenuates at higher levels ($-30.5\%$ at $\alpha{=}1.0$), consistent with the diversity--calibration dissociation discussed in \S\ref{sec:discussion}.
32	
33	\begin{table}[h]
34	\centering
35	\small
36	\caption{Distinct-3 drift (
…[truncated 25764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-20T13:28:10.777353+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-20T13:28:10.777570+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our experiments are validated at scales ${\leq}6.9$B parameters across six decoder-only transformer families; whether the temporal lead persists at frontier scale is open.
5	Training data is drawn from WikiText-103 and C4 subsets, three orders of magnitude smaller than production corpora; C4 results carry a pre-training data confound (Pythia was pre-trained on Pile, which overlaps with C4).
6	With $T{=}10$ (11 data points), threshold onset and Toda--Yamamoto are power-limited; $T{\geq}20$ validation is pending.
7	PermG requires null-control ($\alpha{=}0.0$) calibration data, which may not be available in all deployment settings.
8	The $\alpha{=}0.60$ synchronous dip (0/8 both seeds, fp32) deserves further investigation: bf16 precision produces qualitatively different results (PermG 8/8 vs.\ 0/8 at fp32), indicating sensitivity to numerical precision at this contamination level.
9	Canary claims are scoped to distinct-$n$ diversity~\cite{li2016diversity}, not model collapse broadly~\cite{schaeffer2025position}; replace-only protocol means accumulate-mode dynamics~\cite{dey2024breaking} are untested.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-20T13:28:10.777791+00:00_

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
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
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

_source line 72 · 2026-05-20T13:28:10.777986+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-20T13:28:10.778243+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2502.15654 detection-based mitigation model collapse bibtex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2502.15654 detection-based mitigation model collapse bibtex"
  }
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-20T13:28:10.778472+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Phipson Smyth 2010 permutation p-values bibtex statistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Phipson Smyth 2010 permutation p-values bibtex statistics"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-20T13:28:10.778714+00:00_

Web search results for query: "Phipson Smyth 2010 permutation p-values bibtex statistics"

Links: [{"title":"permp: Exact permutation p-values in statmod: Statistical Modeling","url":"https://rdrr.io/cran/statmod/man/permp.html"},{"title":"CRAN: statmod citation info","url":"https://cran.r-project.org/web/packages/statmod/citation.html"},{"title":"Permutation P-values Should Never Be Zero:","url":"https://arxiv.org/pdf/1603.05766"},{"title":"Permutation P-values Should Never Be Zero: Calculating Exact P-values When Permutations Are Randomly Drawn","url":"https://ideas.repec.org/a/bpj/sagmbi/v9y2010i1n39.html"},{"title":"Permutation P-values Should Never Be Zero: Calculating Exact P-values When Permutations Are Randomly Drawn | Request PDF","url":"https://www.researchgate.net/publication/47660026_Permutation_P-values_Should_Never_Be_Zero_Calculating_Exact_P-values_When_Permutations_Are_Randomly_Drawn"},{"title":"Exact testing with random permutations - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC6405018/"},{"title":"[1603.05766] Permutation p-values should never be zero: calculating exact p-values when permutations are randomly drawn","url":"https://arxiv.org/abs/1603.05766"},{"title":"Permutation P-values Should Never Be Zero: Calculating Exact P-values When Permutations Are Randomly Drawn","url":"https://www.degruyterbrill.com/document/doi/10.2202/1544-6115.1585/html"},{"title":"Statistical Applications in Genetics and Molecular Biology Permutation P -values Should Never Be Zero: Calculating Exact P -values When Permutations Are Randomly Drawn | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Statistical-Applications-in-Genetics-and-Molecular-Phipson-Hall/a1239adf05b9d8127aa190b90229d13f603d35fe"},{"title":"A Study of Galcanezumab in Participants With Chronic Cluster Headache","url":"https://cdn.clinicaltrials.gov/large-docs/26/NCT02438826/SAP_001.pdf"}]

Based on the search results, I found comprehensive information about the Phipson and Sm
…[truncated 1208 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-20T13:28:10.778971+00:00_

Web search results for query: "arXiv 2502.15654 detection-based mitigation model collapse bibtex"

Links: [{"title":"[2502.15654] Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/abs/2502.15654"},{"title":"Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/html/2502.15654"},{"title":"Machine-generated text detection prevents language model collapse","url":"https://arxiv.org/pdf/2502.15654"},{"title":"Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative AI","url":"https://arxiv.org/pdf/2410.12341"},{"title":"A Probabilistic Perspective on Model Collapse","url":"https://arxiv.org/pdf/2505.13947"}]

I found the arXiv paper 2502.15654. Here's what I can tell you about it:

The paper is titled "Machine-generated text detection prevents language model collapse" by George Drayson, Emine Yilmaz, and Vasileios Lampos from University College London.

The paper addresses model collapse, a degenerative process where LLMs reinforce their own errors, and proposes training a machine-generated text detector with an importance sampling approach to alleviate model collapse. The method is validated on two LLM variants (GPT-2 and SmolLM2) and demonstrates that it can prevent model collapse and improve performance when sufficient human-authored samples are present.

If you need the BibTeX citation for this paper, you can find it directly on the arXiv abstract page at https://arxiv.org/abs/2502.15654, where there is typically a BibTeX export option available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-20T13:28:10.779495+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib",
  "content": "% ============================================================\n% CORE MODEL COLLAPSE\n% ============================================================\n\n@article{shumailov2024curse,\n  title     = {The Curse of Recursion: Training on Generated Data Makes Models Forget},\n  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},\n  journal   = {Nature},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2305.17493},\n}\n\n@inproceedings{alemohammad2024mad,\n  title     = {Self-Consuming Generative Models Go {MAD}},\n  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2307.01850},\n}\n\n@inproceedings{dohmatob2024tale,\n  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and others},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.07043},\n}\n\n@inproceedings{dohmatob2025strong,\n  title     = {Strong Model Collapse},\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2410.04840},\n}\n\n@article{du2026geometric,\n  title     = {Escaping Mode Collapse in {LLM} Generation via Geometric Regulation},\n  author    = {Du, Xin and Tanaka-Ishii, Kumiko},\n  journal   = {arXiv preprint arXiv:2605.00435},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2605.00435},\n}\n\n% ============================================================\n% CANARY / EARLY WARNING METRICS\n% ============================================================\n\n@article{du2025scales,\n  title     = {Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios},\n  author    = {Du, Y. and Wu, G. and Tang, G. and Wang, W. and Fan, Q.},\n  journal   = {arXiv preprint arXiv:2510.05133},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2510.05133},\n}\n\n@article{gambetta2024surplexity,\n  title     = {Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},\n  author    = {Gambetta, Daniele and others},\n  journal   = {arXiv preprint arXiv:2410.12341},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2410.12341},\n}\n\n\n@article{sigma2026spectral,\n  title     = {{SIGMA}: Scalable Spectral Insights for {LLM} Model Collapse},\n  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},\n  journal   = {arXiv preprint arXiv:2601.03385},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2601.03385},\n}\n\n@article{kalinowski2026topology,\n  title     = {Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index},\n  author    = {Kalinowski, Alexander},\n  journal   = {arXiv preprint arXiv:2604.26984},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2604.26984},\n}\n\n% ============================================================\n% DIVERSITY METRICS (BACKGROUND)\n% ============================================================\n\n\n@inproceedings{li2016diversity,\n  title     = {A Diversity-Promoting Objective Function for Neural Conversation Models},\n  author    = {Li, Jiwei and others},\n  booktitle = {North American Chapter of the Association for Computational Linguistics},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1510.03055},\n}\n\n% ============================================================\n% DATA MIXING & ACCUMULATION\n% ============================================================\n\n@inproceedings{kazdan2025collapse,\n  title     = {Collapse or Thrive? {P}erils and Promises of Synthetic Data in a Self-Generating World},\n  author    = {Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David L. and Koyejo, Sanmi},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2410.16713},\n}\n\n@inproceedings{dey2024breaking,\n  title     = {Is Model Collapse Inevitable? {B}reaking the Curse of Recursion by Accumulating Real and Synthetic Data},\n  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2404.01413},\n}\n\n% ============================================================\n% MITIGATION & VERIFICATION\n% ============================================================\n\n@article{dces2026counter,\n  title     = {Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling},\n  author    = {Zhu, Bingze and Xie, Yubo},\n  journal   = {Electronics},\n  year      = {2026},\n  url       = {https://www.mdpi.com/2079-9292/15/4/869},\n}\n\n@article{drayson2025detection,\n  title     = {Machine-generated text detection prevents language model collapse},\n  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  journal   = {arXiv preprint arXiv:2502.15654},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2502.15654},\n}\n\n% ============================================================\n% POSITION / SURVEY / EPISTEMICS / ANALYTICAL ROBUSTNESS\n% ============================================================\n\n@inproceedings{bell2022modeling,\n  title     = {Modeling the Machine Learning Multiverse},\n  author    = {Bell, Samuel J. and Kampman, Onno P. and Dodge, Jesse and Lawrence, Neil D.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2206.05985},\n}\n\n@article{kapoor2024reforms,\n  title     = {{REFORMS}: Consensus-based Recommendations for Machine-learning-based Science},\n  author    = {Kapoor, Sayash and Cantrell, Emily and Peng, Kenny and Pham, Thanh Hien and Bail, Christopher A. and Gundersen, Odd Erik and Hofman, Jake M. and Hullman, Jessica and Lones, Michael A. and Malik, Momin M. and Nanayakkara, Priyanka and Poldrack, Russell A. and Raji, Inioluwa Deborah and Roberts, Michael and Salganik, Matthew J. and Serra-Garcia, Marta and Stewart, Brandon M. and Vandewiele, Gilles and Narayanan, Arvind},\n  journal   = {Science Advances},\n  volume    = {10},\n  number    = {18},\n  pages     = {eadk3452},\n  year      = {2024},\n  doi       = {10.1126/sciadv.adk3452},\n}\n\n@article{coretta2023multidimensional,\n  title     = {Multidimensional Signals and Analytic Flexibility: Estimating Degrees of Freedom in Human-Speech Analyses},\n  author    = {Coretta, Stefano and Casillas, Joseph V. and Roessig, Simon and Franke, Michael and others},\n  journal   = {Advances in Methods and Practices in Psychological Science},\n  volume    = {6},\n  number    = {3},\n  year      = {2023},\n  doi       = {10.1177/25152459231162567},\n}\n\n@article{simonsohn2020specification,\n  title     = {Specification curve analysis},\n  author    = {Simonsohn, Uri and Simmons, Joseph P. and Nelson, Leif D.},\n  journal   = {Nature Human Behaviour},\n  volume    = {4},\n  number    = {11},\n  pages     = {1208--1214},\n  year      = {2020},\n  doi       = {10.1038/s41562-020-0912-z},\n}\n\n@article{schaeffer2025position,\n  title     = {Position: Model Collapse Does Not Mean What You Think},\n  author    = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},\n  journal   = {arXiv preprint arXiv:2503.03150},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2503.03150},\n}\n\n% ============================================================\n% METHODOLOGY (GRANGER / LEAD-LAG)\n% ============================================================\n\n@article{granger1969investigating,\n  author    = {Granger, Clive W. J.},\n  title     = {Investigating Causal Relations by Econometric Models and Cross-spectral Methods},\n  journal   = {Econometrica},\n  volume    = {37},\n  number    = {3},\n  pages     = {424--438},\n  year      = {1969},\n  publisher = {Wiley},\n}\n\n@article{shojaie2022granger,\n  title     = {{Granger} Causality: A Review and Recent Advances},\n  author    = {Shojaie, Ali and Fox, Emily B.},\n  journal   = {Annual Review of Statistics and Its Application},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2105.02675},\n}\n\n@article{marcinkevics2022neural,\n  title     = {{Granger} Causality Using Neural Networks},\n  author    = {Marcinkevics, Raphael and Vogt, Julia},\n  journal   = {arXiv preprint arXiv:2208.03703},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2208.03703},\n}\n\n@article{granger1974spurious,\n  title     = {Spurious Regressions in Econometrics},\n  author    = {Granger, Clive W. J. and Newbold, Paul},\n  journal   = {Journal of Econometrics},\n  volume    = {2},\n  number    = {2},\n  pages     = {111--120},\n  year      = {1974},\n  doi       = {10.1016/0304-4076(74)90034-7},\n}\n\n@article{toda1995statistical,\n  title     = {Statistical Inference in Vector Autoregressions with Possibly Integrated Processes},\n  author    = {Toda, Hiro Y. and Yamamoto, Taku},\n  journal   = {Journal of Econometrics},\n  volume    = {66},\n  number    = {1--2},\n  pages     = {225--250},\n  year      = {1995},\n  doi       = {10.1016/0304-4076(94)01616-8},\n}\n\n% ============================================================\n% EARLY WARNING SIGNALS / TIPPING POINTS (ECOLOGICAL THEORY)\n% ============================================================\n\n@article{scheffer2009early,\n  title     = {Early-warning signals for critical transitions},\n  author    = {Scheffer, Marten and Bascompte, Jordi and Brock, William A. and Brovkin, Victor and Carpenter, Stephen R. and Dakos, Vasilis and Held, Hermann and van Nes, Egbert H. and Rietkerk, Max and Sugihara, George},\n  journal   = {Nature},\n  year      = {2009},\n  doi       = {10.1038/nature08227},\n}\n\n@article{scheffer2012anticipating,\n  title     = {Anticipating Critical Transitions},\n  author    = {Scheffer, Marten and Carpenter, Stephen R. and Lenton, Timothy M. and Bascompte, Jordi and Brock, William and Dakos, Vasilis and van de Koppel, Johan and van de Leemput, Ingrid A. and Levin, Simon A. and van Nes, Egbert H. and Pascual, Mercedes and Vandermeer, John},\n  journal   = {Science},\n  year      = {2012},\n  doi       = {10.1126/science.1225244},\n}\n\n@article{boettiger2012limits,\n  title     = {Quantifying Limits to Detection of Early Warning for Critical Transitions},\n  author    = {Boettiger, Carl and Hastings, Alan},\n  journal   = {Journal of the Royal Society Interface},\n  year      = {2012},\n  doi       = {10.1098/rsif.2012.0125},\n}\n\n@article{dakos2012methods,\n  title     = {Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data},\n  author    = {Dakos, Vasilis and Carpenter, Stephen R. and Brock, William A. and Ellison, Aaron M. and Guttal, Vishwesha and Ives, Anthony R. and K\\'{e}fi, Sonia and Livina, Vasilis and Seekell, David A. and van Nes, Egbert H. and Scheffer, Marten},\n  journal   = {PLoS ONE},\n  year      = {2012},\n  volume    = {7},\n  number    = {7},\n  pages     = {e41010},\n  doi       = {10.1371/journal.pone.0041010},\n}\n\n@inproceedings{gu2024cmr,\n  title     = {{CMR} Scaling Law: Predicting Critical Mixture Ratios for Continual Pre-training of Language Models},\n  author    = {Gu, Jiawei and Yang, Zacc and Ding, Chuanghao and Zhao, Rui and Tan, Fei},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2407.17467},\n}\n\n@inproceedings{gu2025datamixing,\n  title     = {Data Mixing Can Induce Phase Transitions in Knowledge Acquisition},\n  author    = {Gu, Xinran and Liang, Hayden and Pehlevan, Cengiz},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  note      = {Spotlight},\n  url       = {https://arxiv.org/abs/2505.18091},\n}\n\n@article{calabrese2003hormesis,\n  title     = {Toxicology Rethinks Its Central Belief},\n  author    = {Calabrese, Edward J. and Baldwin, Linda A.},\n  journal   = {Nature},\n  year      = {2003},\n  volume    = {421},\n  number    = {6924},\n  pages     = {691--692},\n  doi       = {10.1038/421691a},\n}\n\n% ============================================================\n% MODELS\n% ============================================================\n\n@inproceedings{biderman2023pythia,\n  title     = {Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling},\n  author    = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purber, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and van der Wal, Oskar},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2304.01373},\n}\n\n% ============================================================\n% DATASETS\n% ============================================================\n\n@inproceedings{merity2017pointer,\n  title     = {Pointer Sentinel Mixture Models},\n  author    = {Merity, Stephen and Xiong, Caiming and Bradbury, James and Socher, Richard},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2017},\n  url       = {https://arxiv.org/abs/1609.07843},\n}\n\n% ============================================================\n% STATISTICAL METHODOLOGY\n% ============================================================\n\n@article{schreiber2000measuring,\n  title     = {Measuring Information Transfer},\n  author    = {Schreiber, Thomas},\n  journal   = {Physical Review Letters},\n  volume    = {85},\n  number    = {2},\n  pages     = {461--464},\n  year      = {2000},\n}\n\n@article{phipson2010permutation,\n  title     = {Permutation P-values Should Never Be Zero: Calculating Exact P-values When Permutations Are Randomly Drawn},\n  author    = {Phipson, Belinda and Smyth, Gordon K.},\n  journal   = {Statistical Applications in Genetics and Molecular Biology},\n  volume    = {9},\n  number    = {1},\n  pages     = {Article 39},\n  year      = {2010},\n  doi       = {10.2202/1544-6115.1585},\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib",
    "content": "% ============================================================\n% CORE MODEL COLLAPSE\n% ============================================================\n\n@article{shumailov2024curse,\n  title     = {The Curse of Recursion: Training on Generated Data Makes Models Forget},\n  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},\n  journal   = {Nature},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2305.17493},\n}\n\n@inproceedings{alemohammad2024mad,\n  title     = {Self-Consuming Generative Models Go {MAD}},\n  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2307.01850},\n}\n\n@inproceedings{dohmatob2024tale,\n  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and others},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.07043},\n}\n\n@inproceedings{dohmatob2025strong,\n  title     = {Strong Model Collapse},\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2410.04840},\n}\n\n@article{du2026geometric,\n  title     = {Escaping Mode Collapse in {LLM} Generation via Geometric Regulation},\n  author    = {Du, Xin and Tanaka-Ishii, Kumiko},\n  journal   = {arXiv preprint arXiv:2605.00435},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2605.00435},\n}\n\n% ============================================================\n% CANARY / EARLY WARNING METRICS\n% ============================================================\n\n@article{du2025scales,\n  title     = {Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios},\n  author    = {Du, Y. and Wu, G. and Tang, G. and Wang, W. and Fan, Q.},\n  journal   = {arXiv preprint arXiv:2510.05133},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2510.05133},\n}\n\n@article{gambetta2024surplexity,\n  title     = {Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},\n  author    = {Gambetta, Daniele and others},\n  journal   = {arXiv preprint arXiv:2410.12341},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2410.12341},\n}\n\n\n@article{sigma2026spectral,\n  title     = {{SIGMA}: Scalable Spectral Insights for {LLM} Model Collapse},\n  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},\n  journal   = {arXiv preprint arXiv:2601.03385},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2601.03385},\n}\n\n@article{kalinowski2026topology,\n  title     = {Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index},\n  author    = {Kalinowski, Alexander},\n  journal   = {arXiv preprint arXiv:2604.26984},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2604.26984},\n}\n\n% ============================================================\n% DIVERSITY METRICS (BACKGROUND)\n% ============================================================\n\n\n@inproceedings{li2016diversity,\n  title     = {A Diversity-Promoting Objective Function for Neural Conversation Models},\n  author    = {Li, Jiwei and others},\n  booktitle = {North American Chapter of the Association for Computational Linguistics},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1510.03055},\n}\n\n% ============================================================\n% DATA MIXING & ACCUMULATION\n% ============================================================\n\n@inproceedings{kazdan2025collapse,\n  title     = {Collapse or Thrive? {P}erils and Promises of Synthetic Data in a Self-Generating World},\n  author    = {Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David L. and Koyejo, Sanmi},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2410.16713},\n}\n\n@inproceedings{dey2024breaking,\n  title     = {Is Model Collapse Inevitable? {B}reaking the Curse of Recursion by Accumulating Real and Synthetic Data},\n  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2404.01413},\n}\n\n% ============================================================\n% MITIGATION & VERIFICATION\n% ============================================================\n\n@article{dces2026counter,\n  title     = {Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling},\n  author    = {Zhu, Bingze and Xie, Yubo},\n  journal   = {Electronics},\n  year      = {2026},\n  url       = {https://www.mdpi.com/2079-9292/15/4/869},\n}\n\n@article{drayson2025detection,\n  title     = {Machine-generated text detection prevents language model collapse},\n  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  journal   = {arXiv preprint arXiv:2502.15654},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2502.15654},\n}\n\n% ============================================================\n% POSITION / SURVEY / EPISTEMICS / ANALYTICAL ROBUSTNESS\n% ============================================================\n\n@inproceedings{bell2022modeling,\n  title     = {Modeling the Machine Learning Multiverse},\n  author    = {Bell, Samuel J. and Kampman, Onno P. and Dodge, Jesse and Lawrence, Neil D.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2206.05985},\n}\n\n@article{kapoor2024reforms,\n  title     = {{REFORMS}: Consensus-based Recommendations for Machine-learning-based Science},\n  author    = {Kapoor, Sayash and Cantrell, Emily and Peng, Kenny and Pham, Thanh Hien and Bail, Christopher A. and Gundersen, Odd Erik and Hofman, Jake M. and Hullman, Jessica and Lones, Michael A. and Malik, Momin M. and Nanayakkara, Priyanka and Poldrack, Russell A. and Raji, Inioluwa Deborah and Roberts, Michael and Salganik, Matthew J. and Serra-Garcia, Marta and Stewart, Brandon M. and Vandewiele, Gilles and Narayanan, Arvind},\n  journal   = {Science Advances},\n  volume    = {10},\n  number    = {18},\n  pages     = {eadk3452},\n  year      = {2024},\n  doi       = {10.1126/sciadv.adk3452},\n}\n\n@article{coretta2023multidimensional,\n  title     = {Multidimensional Signals and Analytic Flexibility: Estimating Degrees of Freedom in Human-Speech Analyses},\n  author    = {Coretta, Stefano and Casillas, Joseph V. and Roessig, Simon and Franke, Michael and others},\n  journal   = {Advances in Methods and Practices in Psychological Science},\n  volume    = {6},\n  number    = {3},\n  year      = {2023},\n  doi       = {10.1177/25152459231162567},\n}\n\n@article{simonsohn2020specification,\n  title     = {Specification curve analysis},\n  author    = {Simonsohn, Uri and Simmons, Joseph P. and Nelson, Leif D.},\n  journal   = {Nature Human Behaviour},\n  volume    = {4},\n  number    = {11},\n  pages     = {1208--1214},\n  year      = {2020},\n  doi       = {10.1038/s41562-020-0912-z},\n}\n\n@article{schaeffer2025position,\n  title     = {Position: Model Collapse Does Not Mean What You Think},\n  author    = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},\n  journal   = {arXiv preprint arXiv:2503.03150},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2503.03150},\n}\n\n% ============================================================\n% METHODOLOGY (GRANGER / LEAD-LAG)\n% ============================================================\n\n@article{granger1969investigating,\n  author    = {Granger, Clive W. J.},\n  title     = {Investigating Causal Relations by Econometric Models and Cross-spectral Methods},\n  journal   = {Econometrica},\n  volume    = {37},\n  number    = {3},\n  pages     = {424--438},\n  year      = {1969},\n  publisher = {Wiley},\n}\n\n@article{shojaie2022granger,\n  title     = {{Granger} Causality: A Review and Recent Advances},\n  author    = {Shojaie, Ali and Fox, Emily B.},\n  journal   = {Annual Review of Statistics and Its Application},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2105.02675},\n}\n\n@article{marcinkevics2022neural,\n  title     = {{Granger} Causality Using Neural Networks},\n  author    = {Marcinkevics, Raphael and Vogt, Julia},\n  journal   = {arXiv preprint arXiv:2208.03703},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2208.03703},\n}\n\n@article{granger1974spurious,\n  title     = {Spurious Regressions in Econometrics},\n  author    = {Granger, Clive W. J. and Newbold, Paul},\n  journal   = {Journal of Econometrics},\n  volume    = {2},\n  number    = {2},\n  pages     = {111--120},\n  year      = {1974},\n  doi       = {10.1016/0304-4076(74)90034-7},\n}\n\n@article{toda1995statistical,\n  title     = {Statistical Inference in Vector Autoregressions with Possibly Integrated Processes},\n  author    = {Toda, Hiro Y. and Yamamoto, Taku},\n  journal   = {Journal of Econometrics},\n  volume    = {66},\n  number    = {1--2},\n  pages     = {225--250},\n  year      = {1995},\n  doi       = {10.1016/0304-4076(94)01616-8},\n}\n\n% ============================================================\n% EARLY WARNING SIGNALS / TIPPING POINTS (ECOLOGICAL THEORY)\n% ============================================================\n\n@article{scheffer2009early,\n  title     = {Early-warning signals for critical transitions},\n  author    = {Scheffer, Marten and Bascompte, Jordi and Brock, William A. and Brovkin, Victor and Carpenter, Stephen R. and Dakos, Vasilis and Held, Hermann and van Nes, Egbert H. and Rietkerk, Max and Sugihara, George},\n  journal   = {Nature},\n  year      = {2009},\n  doi       = {10.1038/nature08227},\n}\n\n@article{scheffer2012anticipating,\n  title     = {Anticipating Critical Transitions},\n  author    = {Scheffer, Marten and Carpenter, Stephen R. and Lenton, Timothy M. and Bascompte, Jordi and Brock, William and Dakos, Vasilis and van de Koppel, Johan and van de Leemput, Ingrid A. and Levin, Simon A. and van Nes, Egbert H. and Pascual, Mercedes and Vandermeer, John},\n  journal   = {Science},\n  year      = {2012},\n  doi       = {10.1126/science.1225244},\n}\n\n@article{boettiger2012limits,\n  title     = {Quantifying Limits to Detection of Early Warning for Critical Transitions},\n  author    = {Boettiger, Carl and Hastings, Alan},\n  journal   = {Journal of the Royal Society Interface},\n  year      = {2012},\n  doi       = {10.1098/rsif.2012.0125},\n}\n\n@article{dakos2012methods,\n  title     = {Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data},\n  author    = {Dakos, Vasilis and Carpenter, Stephen R. and Brock, William A. and Ellison, Aaron M. and Guttal, Vishwesha and Ives, Anthony R. and K\\'{e}fi, Sonia and Livina, Vasilis and Seekell, David A. and van Nes, Egbert H. and Scheffer, Marten},\n  journal   = {PLoS ONE},\n  year      = {2012},\n  volume    = {7},\n  number    = {7},\n  pages     = {e41010},\n  doi       = {10.1371/journal.pone.0041010},\n}\n\n@inproceedings{gu2024cmr,\n  title     = {{CMR} Scaling Law: Predicting Critical Mixture Ratios for Continual Pre-training of Language Models},\n  author    = {Gu, Jiawei and Yang, Zacc and Ding, Chuanghao and Zhao, Rui and Tan, Fei},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2407.17467},\n}\n\n@inproceedings{gu2025datamixing,\n  title     = {Data Mixing Can Induce Phase Transitions in Knowledge Acquisition},\n  author    = {Gu, Xinran and Liang, Hayden and Pehlevan, Cengiz},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  note      = {Spotlight},\n  url       = {https://arxiv.org/abs/2505.18091},\n}\n\n@article{calabrese2003hormesis,\n  title     = {Toxicology Rethinks Its Central Belief},\n  author    = {Calabrese, Edward J. and Baldwin, Linda A.},\n  journal   = {Nature},\n  year      = {2003},\n  volume    = {421},\n  number    = {6924},\n  pages     = {691--692},\n  doi       = {10.1038/421691a},\n}\n\n% ============================================================\n% MODELS\n% ============================================================\n\n@inproceedings{biderman2023pythia,\n  title     = {Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling},\n  author    = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purber, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and van der Wal, Oskar},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2304.01373},\n}\n\n% ============================================================\n% DATASETS\n% ============================================================\n\n@inproceedings{merity2017pointer,\n  title     = {Pointer Sentinel Mixture Models},\n  author    = {Merity, Stephen and Xiong, Caiming and Bradbury, James and Socher, Richard},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2017},\n  url       = {https://arxiv.org/abs/1609.07843},\n}\n\n% ============================================================\n% STATISTICAL METHODOLOGY\n% ============================================================\n\n@article{schreiber2000measuring,\n  title     = {Measuring Information Transfer},\n  author    = {Schreiber, Thomas},\n  journal   = {Physical Review Letters},\n  volume    = {85},\n  number    = {2},\n  pages     = {461--464},\n  year      = {2000},\n}\n\n@article{phipson2010permutation,\n  title     = {Permutation P-values Should Never Be Zero: Calculating Exact P-values When Permutations Are Randomly Drawn},\n  author    = {Phipson, Belinda and Smyth, Gordon K.},\n  journal   = {Statistical Applications in Genetics and Molecular Biology},\n  volume    = {9},\n  number    = {1},\n  pages     = {Article 39},\n  year      = {2010},\n  doi       = {10.2202/1544-6115.1585},\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-20T13:28:10.780152+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-20T13:28:10.780426+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex",
  "old_string": "who showed that recursively replacing real data with model-generated text causes progressive tail erosion.",
  "new_string": "who showed that recursively replacing real data with model-generated text causes progressive tail erosion; \\citet{schaeffer2025position} systematize eight distinct notions of ``collapse'' that this literature conflates."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex",
    "old_string": "who showed that recursively replacing real data with model-generated text causes progressive tail erosion.",
    "new_string": "who showed that recursively replacing real data with model-generated text causes progressive tail erosion; \\citet{schaeffer2025position} systematize eight distinct notions of ``collapse'' that this literature conflates."
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-20T13:28:10.780676+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-20T13:28:10.780880+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex",
  "old_string": "and \\citet{gambetta2024surplexity} introduces surplexity as a collapse detector.",
  "new_string": "\\citet{gambetta2024surplexity} introduces surplexity as a collapse detector, and \\citet{drayson2025detection} show that machine-generated text detection can prevent collapse."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex",
    "old_string": "and \\citet{gambetta2024surplexity} introduces surplexity as a collapse detector.",
    "new_string": "\\citet{gambetta2024surplexity} introduces surplexity as a collapse detector, and \\citet{drayson2025detection} show that machine-generated text detection can prevent collapse."
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-20T13:28:10.781111+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-20T13:28:10.781333+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex",
  "old_string": "\\citet{scheffer2009early} established that systems approaching tipping points exhibit generic early-warning signals (rising autocorrelation and variance), while \\citet{boettiger2012limits} quantified detection limits in short time series",
  "new_string": "\\citet{scheffer2009early} established that systems approaching tipping points exhibit generic early-warning signals (rising autocorrelation and variance); \\citet{dakos2012methods} developed a practical toolkit for estimating such signals, while \\citet{boettiger2012limits} quantified detection limits in short time series"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex",
    "old_string": "\\citet{scheffer2009early} established that systems approaching tipping points exhibit generic early-warning signals (rising autocorrelation and variance), while \\citet{boettiger2012limits} quantified detection limits in short time series",
    "new_string": "\\citet{scheffer2009early} established that systems approaching tipping points exhibit generic early-warning signals (rising autocorrelation and variance); \\citet{dakos2012methods} developed a practical toolkit for estimating such signals, while \\citet{boettiger2012limits} quantified detection limits in short time series"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-20T13:28:10.781574+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-20T13:28:10.781776+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex",
  "old_string": "The standard framework for testing temporal precedence is Granger causality~\\cite{granger1969investigating};",
  "new_string": "The standard framework for testing temporal precedence is Granger causality~\\cite{granger1969investigating}, with neural extensions for nonlinear settings~\\citep{marcinkevics2022neural};"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex",
    "old_string": "The standard framework for testing temporal precedence is Granger causality~\\cite{granger1969investigating};",
    "new_string": "The standard framework for testing temporal precedence is Granger causality~\\cite{granger1969investigating}, with neural extensions for nonlinear settings~\\citep{marcinkevics2022neural};"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-20T13:28:10.782016+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-20T13:28:10.782217+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex",
  "old_string": "\\citet{gu2024cmr} establish a scaling law for critical mixture ratios in continual pre-training, and \\citet{gu2025datamixing} show that data mixing can induce phase transitions in knowledge acquisition",
  "new_string": "\\citet{kazdan2025collapse} map the conditions under which synthetic data triggers collapse versus improves performance, \\citet{gu2024cmr} establish a scaling law for critical mixture ratios in continual pre-training, and \\citet{gu2025datamixing} show that data mixing can induce phase transitions in knowledge acquisition"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex",
    "old_string": "\\citet{gu2024cmr} establish a scaling law for critical mixture ratios in continual pre-training, and \\citet{gu2025datamixing} show that data mixing can induce phase transitions in knowledge acquisition",
    "new_string": "\\citet{kazdan2025collapse} map the conditions under which synthetic data triggers collapse versus improves performance, \\citet{gu2024cmr} establish a scaling law for critical mixture ratios in continual pre-training, and \\citet{gu2025datamixing} show that data mixing can induce phase transitions in knowledge acquisition"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-20T13:28:10.782471+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-20T13:28:10.782661+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex",
  "old_string": "We apply 5{,}000 permutations on first-differenced series with Benjamini--Hochberg FDR correction",
  "new_string": "We apply 5{,}000 permutations~\\citep{phipson2010permutation} on first-differenced series with Benjamini--Hochberg FDR correction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex",
    "old_string": "We apply 5{,}000 permutations on first-differenced series with Benjamini--Hochberg FDR correction",
    "new_string": "We apply 5{,}000 permutations~\\citep{phipson2010permutation} on first-differenced series with Benjamini--Hochberg FDR correction"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-20T13:28:10.782908+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-20T13:28:10.783109+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "old_string": "Table~\\ref{tab:te_results} reports Transfer Entropy (TE) results aggregated across all baseline conditions.",
  "new_string": "Table~\\ref{tab:te_results} reports transfer entropy (TE; \\citealp{schreiber2000measuring}) results aggregated across all baseline conditions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "old_string": "Table~\\ref{tab:te_results} reports Transfer Entropy (TE) results aggregated across all baseline conditions.",
    "new_string": "Table~\\ref{tab:te_results} reports transfer entropy (TE; \\citealp{schreiber2000measuring}) results aggregated across all baseline conditions."
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-20T13:28:10.783493+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-20T13:28:10.783747+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "echo \"=== BIB ENTRIES ===\" && grep -ohP '@\\w+\\{([^,]+),' docs/paper/references.bib | sed 's/@[^{]*{//;s/,$//' | sort -u | tee /tmp/bib_keys.txt | wc -l && echo \"=== CITE KEYS (active files) ===\" && grep -ohP '\\\\cite[a-z]*\\{[^}]+\\}' docs/paper/abstract.tex docs/paper/introduction.tex docs/paper/related_work.tex docs/paper/method.tex docs/paper/experiments.tex docs/paper/discussion.tex docs/paper/limitations.tex docs/paper/ethics.tex docs/paper/appendix.tex | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u | tee /tmp/cite_keys.txt | wc -l && echo \"=== CITE KEYS (all tex) ===\" && grep -ohP '\\\\cite[a-z]*\\{[^}]+\\}' docs/paper/*.tex | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u | tee /tmp/cite_keys_all.txt | wc -l && echo \"=== ORPHANS (all tex) ===\" && comm -23 /tmp/bib_keys.txt /tmp/cite_keys_all.txt && echo \"=== MISSING (cited but not in bib, all tex) ===\" && comm -23 /tmp/cite_keys_all.txt /tmp/bib_keys.txt",
  "description": "Verify bib vs cite counts and orphans"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Bash",
  "tool_args": {
    "command": "echo \"=== BIB ENTRIES ===\" && grep -ohP '@\\w+\\{([^,]+),' docs/paper/references.bib | sed 's/@[^{]*{//;s/,$//' | sort -u | tee /tmp/bib_keys.txt | wc -l && echo \"=== CITE KEYS (active files) ===\" && grep -ohP '\\\\cite[a-z]*\\{[^}]+\\}' docs/paper/abstract.tex docs/paper/introduction.tex docs/paper/related_work.tex docs/paper/method.tex docs/paper/experiments.tex docs/paper/discussion.tex docs/paper/limitations.tex docs/paper/ethics.tex docs/paper/appendix.tex | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u | tee /tmp/cite_keys.txt | wc -l && echo \"=== CITE KEYS (all tex) ===\" && grep -ohP '\\\\cite[a-z]*\\{[^}]+\\}' docs/paper/*.tex | sed 's/\\\\cite[a-z]*{//;s/}//' | tr ',' '\\n' | sed 's/^ *//;s/ *$//' | sort -u | tee /tmp/cite_keys_all.txt | wc -l && echo \"=== ORPHANS (all tex) ===\" && comm -23 /tmp/bib_keys.txt /tmp/cite_keys_all.txt && echo \"=== MISSING (cited but not in bib, all tex) ===\" && comm -23 /tmp/cite_keys_all.txt /tmp/bib_keys.txt",
    "description": "Verify bib vs cite counts and orphans"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-20T13:28:10.783973+00:00_

=== BIB ENTRIES ===
35
=== CITE KEYS (active files) ===
34
=== CITE KEYS (all tex) ===
35
=== ORPHANS (all tex) ===
=== MISSING (cited but not in bib, all tex) ===

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-20T13:28:10.784220+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-20T13:28:10.784486+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and canary metrics.}
5	Iterative training collapse was formalized by \citet{shumailov2024curse} and \citet{alemohammad2024mad}, who showed that recursively replacing real data with model-generated text causes progressive tail erosion; \citet{schaeffer2025position} systematize eight distinct notions of ``collapse'' that this literature conflates.
6	Theoretical analyses have sharpened these results: \citet{dohmatob2024tale} recast collapse as a change in scaling-law exponents, and \citet{dohmatob2025strong} proved that collapse can occur even at vanishingly small synthetic fractions.
7	Several works have proposed monitoring metrics: \citet{du2026geometric} observe that calibration error rises before accuracy degrades, \citet{du2025scales} report ECE increases at 30\% contamination before accuracy drops, \citet{gambetta2024surplexity} introduces surplexity as a collapse detector, and \citet{drayson2025detection} show that machine-generated text detection can prevent collapse.
8	We differ from the closest predecessor, \citet{du2026geometric}, in four respects: (i)~we compare an entire family of canary metrics; (ii)~we cross-validate across five statistical methods; (iii)~we map detectability as a function of contamination regime; and (iv)~we treat method-selection sensitivity itself as a primary finding.
9	
10	\paragraph{Data mixing phase transitions.}
11	\citet{kazdan2025collapse} map the conditions under which synthetic data triggers collapse versus improves performance, \citet{gu2024cmr} establish a scaling law for critical mixture ratios in continual pre-training, and \citet{gu2025datamixing} show that data mixing can induce phase transitions in knowledge acquisition---a direct theoretical analogue to our detection phase transition, where a critical mixing ratio separates qualitatively different detection regimes.
12	
13	\paragraph{Critical transitions and lead-lag methodology.}
14	\c
…[truncated 1346 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-20T13:28:10.784767+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/d150_p03_bib_cleanup_log.md",
  "content": "# D150-P03: references.bib Cleanup Log\n\n**Date**: 2026-05-20\n\n## Part 1-2: Orphan Removal\n\nDeleted 17 orphan entries (in bib, not cited in any .tex file):\n\ncao2025entropycal, deshpande2010instantaneous, dohare2024plasticity, falahati2026curated, fu2025selfconsuming, gao2021pile, guo2024linguistic, hataya2023will, he2025golden, lyle2023plasticity, roy2007effective, ruiz2026causalaudit, sahoo2026calibration, seddik2024bad, titus2020speeding, truong2025entropy, yi2026causalcompass\n\n## Part 3: Added 7 Citations\n\n| # | Key | Bib status | Cited in | Location |\n|---|-----|-----------|----------|----------|\n| 1 | drayson2025detection | NEW entry added | related_work.tex | Para 1, monitoring metrics sentence |\n| 2 | schaeffer2025position | Already in bib | related_work.tex | Para 1, after tail erosion (already in limitations.tex) |\n| 3 | dakos2012methods | Already in bib | related_work.tex | Para 3, early-warning toolkit |\n| 4 | schreiber2000measuring | Already in bib | appendix.tex | Transfer Entropy section, first sentence |\n| 5 | phipson2010permutation | NEW entry added | method.tex | PermG paragraph, permutation count |\n| 6 | marcinkevics2022neural | Already in bib | related_work.tex | Para 3, neural Granger extensions |\n| 7 | kazdan2025collapse | Already in bib | related_work.tex | Para 2, data mixing conditions |\n\n## Part 4: Verification\n\n- Bib entries: 35\n- Cite keys (all .tex): 35\n- Orphans: 0\n- Missing: 0\n\n## Files Modified\n\n- `docs/paper/references.bib` — removed 17 orphans, added 2 new entries\n- `docs/paper/related_work.tex` — added 5 citations\n- `docs/paper/method.tex` — added 1 citation (phipson2010permutation)\n- `docs/paper/appendix.tex` — added 1 citation (schreiber2000measuring)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/d150_p03_bib_cleanup_log.md",
    "content": "# D150-P03: references.bib Cleanup Log\n\n**Date**: 2026-05-20\n\n## Part 1-2: Orphan Removal\n\nDeleted 17 orphan entries (in bib, not cited in any .tex file):\n\ncao2025entropycal, deshpande2010instantaneous, dohare2024plasticity, falahati2026curated, fu2025selfconsuming, gao2021pile, guo2024linguistic, hataya2023will, he2025golden, lyle2023plasticity, roy2007effective, ruiz2026causalaudit, sahoo2026calibration, seddik2024bad, titus2020speeding, truong2025entropy, yi2026causalcompass\n\n## Part 3: Added 7 Citations\n\n| # | Key | Bib status | Cited in | Location |\n|---|-----|-----------|----------|----------|\n| 1 | drayson2025detection | NEW entry added | related_work.tex | Para 1, monitoring metrics sentence |\n| 2 | schaeffer2025position | Already in bib | related_work.tex | Para 1, after tail erosion (already in limitations.tex) |\n| 3 | dakos2012methods | Already in bib | related_work.tex | Para 3, early-warning toolkit |\n| 4 | schreiber2000measuring | Already in bib | appendix.tex | Transfer Entropy section, first sentence |\n| 5 | phipson2010permutation | NEW entry added | method.tex | PermG paragraph, permutation count |\n| 6 | marcinkevics2022neural | Already in bib | related_work.tex | Para 3, neural Granger extensions |\n| 7 | kazdan2025collapse | Already in bib | related_work.tex | Para 2, data mixing conditions |\n\n## Part 4: Verification\n\n- Bib entries: 35\n- Cite keys (all .tex): 35\n- Orphans: 0\n- Missing: 0\n\n## Files Modified\n\n- `docs/paper/references.bib` — removed 17 orphans, added 2 new entries\n- `docs/paper/related_work.tex` — added 5 citations\n- `docs/paper/method.tex` — added 1 citation (phipson2010permutation)\n- `docs/paper/appendix.tex` — added 1 citation (schreiber2000measuring)\n"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-20T13:28:10.785038+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/d150_p03_bib_cleanup_log.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 99 · 2026-05-20T13:28:10.785316+00:00_

完成。

**结果**:
- 删除 17 个 orphan bib entries（从 50 减至 35）
- 新增 2 个 bib entries：`drayson2025detection`（arXiv:2502.15654）、`phipson2010permutation`（Phipson & Smyth 2010）
- 在 `related_work.tex` 插入 5 处 `\cite`（schaeffer2025position、drayson2025detection、dakos2012methods、marcinkevics2022neural、kazdan2025collapse）
- 在 `method.tex` 插入 1 处 `\citep`（phipson2010permutation）
- 在 `appendix.tex` 插入 1 处 `\citealp`（schreiber2000measuring）
- 验证：35 bib entries = 35 cite keys，0 orphans，0 missing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_d150_p03_bib_cleanup_20260520T132043"
}
```

</details>

---
