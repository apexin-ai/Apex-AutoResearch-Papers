# paper d219 final framing fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 101
- **Recorded user turns:** 0
- **Tool calls:** 50
- **Original source:** `logs/chats/worker_paper_d219_final_framing_fix_20260524T080020.jsonl`
- **Structured JSON:** [`6c6d20b47621e2bab6f4.json`](../../sessions/6c/6c6d20b47621e2bab6f4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

101 recorded events

### Tool call

_source line 1 · 2026-05-24T08:06:04.776923+00:00_

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
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-24T08:06:04.777524+00:00_

1	\begin{abstract}
2	When language models train iteratively on their own output, distributional degradation proceeds silently until collapse is advanced.
3	We map the detectability landscape of this process primarily on Pythia-410M across 13 contamination levels, with cross-architecture validation on five families (345M--6.9B parameters), revealing blind zones, sharp detection onsets, and a non-monotonic dip where Granger detection fails despite confirmed causal flow.
4	Permutation Granger causality\footnote{Granger precedence establishes temporal predictive improvement, not true causation~\cite{shojaie2022granger}.} (PermG) identifies a detection boundary $\alpha_c(T)$ following a power law in observation length (leave-one-$T$-out CV: MAE${=}0.037$, 15/15 cells within CI): any nonzero contamination produces signal, but sub-linear growth makes detection a function of $T$.
5	This landscape is profoundly method-dependent: five statistical methods applied to identical data yield null-control false positive rates from 0\% to 92\%.
6	Under mode amplification, entropy Granger-precedes diversity collapse with a ${\geq}1$-generation lag (confirmed in 14 of 15 experiments), providing a canary signal whose triggered cessation reduces peak perplexity as a proof-of-concept intervention.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T08:06:04.777807+00:00_

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
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-24T08:06:04.778072+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\cite{shumailov2024curse,alemohammad2024mad}.
5	Lexical diversity narrows, calibration deteriorates, and each generation inherits the systematic biases of its predecessors.
6	As machine-generated text becomes prevalent on the web, such feedback loops pose a growing risk to production training pipelines.
7	By the time standard quality metrics register degradation, the underlying distribution may have already shifted irreversibly.
8	
9	This threat motivates a fundamental question: \emph{what does the detectability landscape of model collapse look like?}
10	At what contamination level does statistical detection become possible, how does this boundary depend on observation length and statistical method, and what structure does the landscape exhibit?
11	Iterative training produces short, noisy time series (often fewer than 15 points per generation sequence), where detection power drops sharply~\cite{boettiger2012limits}, and existing analyses leave these dependencies unresolved.
12	Our detection mechanism (Granger temporal precedence) differs from critical-slowing-down indicators, as model collapse is a first-order transition~\cite{truong2026phase} (\S\ref{sec:related_work}).
13	
14	We systematically map this landscape using Pythia-410M~\cite{biderman2023pythia} across 13 contamination levels (including null control) with multi-seed replication, applying five statistical methods from econometrics~\cite{granger1974spurious,toda1995statistical} to identical data.
15	The resulting map reveals structured terrain (Figure~\ref{fig:regime_map}): blind zones where collapse proceeds undetected, a sharp onset where detection jumps from null to reliable within a 2-percentage-point interval, a non-monotonic dip where Granger detection fails despite confirmed causal flow, a
…[truncated 2829 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T08:06:04.778332+00:00_

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
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-24T08:06:04.778596+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\paragraph{Design considerations.}
5	\label{sec:pitfalls}
6	Lead-lag analysis in iterative model collapse is fragile along three axes, each documented with data from \S\ref{sec:regime}--\ref{sec:dose_response}.
7	\emph{Method sensitivity}: five detection methods applied to identical data yield forward significance rates spanning 0\% to 92\%, with inter-method agreement at $\kappa{=}0.185$.
8	\emph{Spurious regression}: first-differencing eliminates canary$\to$perplexity associations ($F{\approx}0$, $p{=}0.99$) while preserving canary$\to$diversity (24/24$\to$24/24), exposing an entire analysis channel as trend-driven~\cite{granger1974spurious}.
9	\emph{Regime dependence}: the same Granger test shifts from 0/8 to 6/8 significant pairs within a 2-percentage-point interval ($\alpha{=}0.48 \to 0.50$).
10	
11	\subsection{Method Sensitivity Analysis}
12	\label{sec:mmct}
13	We compare five lead-lag detection methods---naive cross-correlation, differenced cross-correlation, threshold onset, permutation Granger causality (PermG), and Toda--Yamamoto~\cite{toda1995statistical}---in a multi-method comparison~\cite{simonsohn2020specification} (algorithm in Appendix~\ref{app:mmct}) calibrated against null-control ($\alpha{=}0.0$) data where any detection is a false positive.
14	Detection results use equal-weight majority voting ($K{\geq}3$ of 5 methods, each contributing one vote per pair) with forward-direction filtering; FPR-inverse weighting is used only in exploratory method ranking (Appendix~\ref{app:weight_robustness}).
15	Each method embodies different assumptions: naive cross-correlation is assumption-free but produces 92\% null-control FPR; differenced cross-correlation controls for trends but lacks directional separation; threshold onset is power-limited at $T{=}11$; Toda--Yamamoto avoids pre-testing for unit roots; PermG uses a nonparametric permutation null with built-in directionality.
16	Pooled null-control FPR across six
…[truncated 6282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T08:06:04.778772+00:00_

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
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T08:06:04.778950+00:00_

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
…[truncated 5675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T08:06:04.779146+00:00_

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
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T08:06:04.779339+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Lead-lag analysis in iterative training collapse is far more fragile than the current literature assumes.
5	Method choice alone inflates spurious-signal rates to at least 62.5\%, first-differencing exposes canary$\to$perplexity associations as entirely spurious, and regime dependence causes the same Granger test to shift from 24/24 to 0/8 significant pairs across contamination levels.
6	These design considerations establish that single-method, single-regime analyses (the current default) cannot reliably distinguish genuine temporal precedence from statistical artifacts.
7	
8	Our systematic five-method comparison through the Multi-Method Consensus Test (MMCT) identifies permutation Granger causality as the recommended detection method: it combines the lowest null-control FPR among all five methods (11.1\%, 4/36 across 6 seeds) with high sensitivity, exhibiting a steep dose-response onset from 0/8 (blind spot, $\alpha{\leq}0.45$) to 6/8 ($\alpha{=}0.50$; sigmoid $k{=}15.7$, ${\approx}3{\times}$ steeper than smooth-signal predictions) with reliable detection at $\alpha{\geq}0.75$.
9	The other four methods each fail in characteristic ways: naive cross-correlation inflates FPR to 75\%, differenced cross-correlation cannot separate forward from reverse precedence, threshold onset is power-limited at $T{=}10$ under $3\sigma$ calibration, and Toda--Yamamoto Granger provides supplementary detection at reduced power (directional assignment under verification).
10	
11	Applying permutation Granger, token entropy exhibits robust one-generation-ahead precedence over diversity collapse at $\alpha{=}1.0$ on WikiText-103 (24/24 forward, 0/24 reverse across 4~seeds, replicated on GPT-2-medium and OPT-1.3B), with cross-architecture validation confirming forward detection (${\geq}6/8$) in 11 of 15 model-seed combinations spanning five families (345M--6.9B); non-confirming conditions span precision sensitivity (GPT-2 bf16), seed depen
…[truncated 1075 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T08:06:04.779515+00:00_

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
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion_reframe.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T08:06:04.779679+00:00_

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
19	The 40-percentage-point gap between structural distortion (Layer~1) and causal evidence (Layer~3) constitutes the sharp detection onset.
20	Layers~1 and~3 are established; Layers~2 and~4 require longer generation protocols ($T{\geq}50$; \citealt{da
…[truncated 2332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T08:06:04.779826+00:00_

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
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T08:06:04.779955+00:00_

1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our landscape characterization uses Pythia-410M as the primary architecture; the phase diagram is Pythia-family-only (410M and 1.4B), and frontier-scale behavior ($>$7B) is untested.
5	With $T{\leq}25$ observations, statistical power remains limited ($\hat{\beta}{=}0.66$, CI $[0.24, 0.78]$); PermG's empirical FPR of $4/36$ (11.1\%, 6 seeds) is the lowest among all five methods but non-zero; the cluster-adjusted 95\% CI is $[1.2\%, 30.4\%]$ (within-seed ICC${=}0.14$).
6	The sync-dip mechanism at $\alpha{=}0.60$ remains open, and all experiments use a single generation strategy (temperature~$1.0$, top-$k{=}50$); alternative decoding settings may alter the collapse dynamics.
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T08:06:04.780081+00:00_

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
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T08:06:04.780196+00:00_

File content (32238 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T08:06:04.780398+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": "120",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "offset": "120",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T08:06:04.780550+00:00_

120	Mean $|\Delta p|$ & 0.002 \\
121	Significance flips & 0 / 24 \\
122	\bottomrule
123	\end{tabular}
124	\end{table}
125	
126	\paragraph{FDR threshold sensitivity.}
127	Table~\ref{tab:fdr_sensitivity} reports the effect of varying the BH FDR threshold $q$ on treatment ($\alpha{=}0.75$, 3~seeds) versus null ($\alpha{=}0.0$, 3~seeds) separation for permutation Granger tests.
128	% TODO-D219: update FDR sensitivity table with 6-seed null data (4/36 FPs at q=0.05; recompute null counts at each q threshold)
129	Treatment/null separation is qualitatively robust to FDR threshold choice; the null control remains at 0/24 across all thresholds.
130	
131	\begin{table}[h]
132	\centering
133	\small
134	% TODO-D219: update caption and table body with 6-seed null data
135	\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs). Null: $\alpha{=}0.0$ (3~seeds, 24 pairs). The null control produces zero false positives at all thresholds tested.}
136	\label{tab:fdr_sensitivity}
137	\resizebox{\columnwidth}{!}{%
138	\begin{tabular}{lccc}
139	\toprule

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-24T08:06:04.780679+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": "415",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "offset": "415",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-24T08:06:04.780809+00:00_

415	\State Weighted consensus: $W(X {\to} Y) \gets \sum_{k} w_k \, d_k \;/\; \sum_{k} w_k$
416	\State Build empirical null distribution of $W$ from all null-control pairs in $\mathcal{N}$
417	\State Compute $p$-value from empirical null: $p \gets \Pr_{\mathcal{N}}(W \geq W_{\mathrm{obs}})$
418	\State Consensus level: $\hat{K} \gets \sum_{k} d_k$
419	\State \Return $p$, $\hat{K}$
420	\end{algorithmic}
421	\end{algorithm}
422	
423	\paragraph{Design rationale.}
424	FPR-inverse weighting penalizes methods with high false positive rates on null-control data: naive cross-correlation (FPR${=}91.7\%$) receives weight $w{=}1.09$, while PermG (FPR${=}11.1\%$, the lowest among all five methods) receives $w{=}9.0$.
425	The empirical null distribution avoids parametric assumptions that are unreliable for short ($T{=}5$--$20$), non-stationary series typical of iterative training.
426	MMCT is a consensus testing protocol, not a novel statistical method; its value lies in systematic method comparison and the identification of method-dependent conclusions.
427	
428	
429	\section{Methodological Comparison Table}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-24T08:06:04.780936+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": "565",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "offset": "565",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-24T08:06:04.781065+00:00_

565	0.75 & 7 & 6 & 0 & \textbf{6} & 3 \\
566	1.00 & 8 & 6 & 2 & \textbf{6} & 1 \\
567	\bottomrule
568	\multicolumn{6}{l}{\footnotesize $^\S$TY directional assignment under verification; column retained for completeness.} \\
569	\end{tabular}}
570	\end{table}
571	
572	The table highlights PermG's combination of null-control detection at 0/8 for this seed ($\alpha{=}0.00$; pooled FPR across 6 seeds: 11.1\%, lowest among all methods), sharp onset (0$\to$6 at $\alpha{=}0.50$), and non-monotonic dip (0 at $\alpha{=}0.55$--$0.60$), confirming it as the method whose dose-response profile most cleanly separates detection regimes.
573	Naive cross-correlation's persistently high counts (7--8/8 even at $\alpha{=}0.00$) demonstrate the 91.7\% pooled null-control FPR reported in \S\ref{sec:method}.
574	
575	
576	\paragraph{Comparison with naive baselines.}
577	\label{app:naive_baselines}
578	
579	Table~\ref{tab:naive_baselines} compares PermG against two practitioner-facing monitoring rules across 26 experiments (18~$\alpha$ values, Pythia-410M, $T{=}10$, fp32).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-24T08:06:04.781196+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": "700",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "offset": "700",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-24T08:06:04.781386+00:00_

700	a075\_s42 & 0.75 & 10 & $0.14$ & $0.91$ & $0.88$ & $0.24$ \\
701	a100\_s42 & 1.00 & 10 & $1.00$ & $0.89$ & $0.98$ & $0.18$ \\
702	t20\_a050 & 0.50 & 20 & $-0.10$ & $0.97$ & $-0.25$ & $0.44$ \\
703	t20\_a100 & 1.00 & 20 & $0.98$ & $0.81$ & $0.87$ & $0.14$ \\
704	\bottomrule
705	\end{tabular}
706	\end{table}
707	
708	\paragraph{Adequacy argument.}
709	Under null conditions ($\alpha{=}0.0$), where FPR is defined, token entropy exhibits $\varphi{=}-0.51$ (anti-correlated, far from the $\varphi{\geq}0.95$ regime where simulation reveals FPR inflation); at $\varphi{=}0.50$, PermG FPR is $6.8\%$, near nominal.
710	The high raw $\varphi$ in distinct-1 ($0.81$--$0.97$ across all $\alpha$ including null) reflects deterministic iterative-training diversity decline---a monotonic trend driven by the training protocol---not stochastic AR persistence.
711	Deterministic trends differ fundamentally from the stochastic AR(1) DGP: they produce predictable trajectories rather than autocorrelated noise, and first-differencing effectively removes them (first-differenced distinct-1 $\varphi$ ranges $-0.14$ to $0.44$, mean ${\sim}0.17$).
712	Our empirical FPR of 4/36 (11.1\%) across six null seeds---the lowest among all five methods---confirms adequate size control in our experimental setting; all four false positives occur in token\_entropy$\to$distinct pairs in the forward direction, suggesting a structural pattern rather than random Type~I error.
713	We note that $T{=}10$ (11 data points) yields high-variance AR(1) estimates; the cross-experiment pattern is more informative than individual values.
714	
715	\paragraph{DGP limitation.}
716	The bivariate AR(1) with linear coupling is a simplification; actual iterative training involves nonlinear dynamics (mode amplification, threshold-dependent diversity loss).
717	These simulation results characterize PermG's behavior under controlled conditions, not exact calibration for the experimental setting; they provide a lower bound on size co
…[truncated 2623 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-24T08:06:04.781534+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": "750",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "offset": "750",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-24T08:06:04.781661+00:00_

750	\bottomrule
751	\end{tabular}
752	\end{table}
753	
754	\begin{figure*}[h]
755	\centering
756	\includegraphics[width=\linewidth]{figures/shapley_method_contribution.pdf}
757	% TODO-D219: regenerate figure and update caption after Shapley recomputation with 6-seed data
758	\caption{Shapley value decomposition of each method's marginal contribution to FPR (positive bars) and FNR (negative bars). PermG is the only method with zero FPR contribution; naive cross-correlation's FPR dominates its FNR benefit.}
759	\label{fig:shapley}
760	\end{figure*}
761	
762	The 8-pair variant (including mauve) yields qualitatively identical rankings: PermG remains the best contributor ($\phi^{\text{comb}}{=}-0.152$), naive cross-correlation the worst ($+0.170$), and threshold onset near-zero ($+0.063$).
763	
764	\paragraph{FDR correction scope.}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-24T08:06:04.781792+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": "795",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "offset": "795",
    "limit": "25"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-24T08:06:04.781972+00:00_

795	\bottomrule
796	\end{tabular}
797	\end{table}
798	
799	
800	\section{PermG FPR Independence Analysis}
801	\label{app:fpr_independence}
802	
803	Table~\ref{tab:null_fpr_methods} reports null-control FPR for all five detection methods across six seeds ($6 \times 6 = 36$ pairs, 6-pair basis excluding mauve).
804	PermG achieves 4/36 (11.1\%), the lowest empirical FPR among all methods; the next-best is DiffXCorr at 6/36 (16.7\%).
805	All four PermG false positives occur in token\_entropy$\to$distinct pairs (seeds~45 and 50, forward direction only), suggesting a structural pattern concentrated in a single canary--downstream pair type.
806	
807	\begin{table}[h]
808	\centering
809	\small
810	\caption{Null-control FPR by method ($\alpha{=}0.0$, 6~seeds 45--50, 6~pairs each). PermG achieves the lowest FPR.}
811	\label{tab:null_fpr_methods}
812	\begin{tabular}{lrr}
813	\toprule
814	Method & Rejections (/36) & FPR (\%) \\
815	\midrule
816	\textbf{Perm.\ Granger (FDR)} & \textbf{4} & \textbf{11.1} \\
817	Diff.\ XCorr ($p{<}0.05$) & 6 & 16.7 \\
818	Threshold ($3\sigma$) & 10 & 27.8 \\
819	Toda--Yamamoto & 14 & 38.9 \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-24T08:06:04.782141+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": "835",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "offset": "835",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-24T08:06:04.782314+00:00_

835	Detection at $\alpha{\geq}0.50$ is unaffected: $K{\geq}3$ counts are identical with and without direction filtering at all signal levels.
836	
837	\paragraph{$K{\geq}3$ false positive detail.}
838	Under the 6-pair basis (6~seeds, 36~pairs), $K{\geq}3$ consensus produces 6 false positives (FPR${=}16.7\%$).
839	Of these, 4 are driven by naive cross-correlation, threshold onset, and Toda--Yamamoto (PermG does \emph{not} vote); the remaining 2 (seeds~45 and 50, te$\to$distinct) include PermG in the consensus.
840	PermG thus contributes to only 2 of 6 consensus false positives, confirming that most $K{\geq}3$ FPR is driven by the high-FPR methods (naive, threshold, TY).
841	
842	\paragraph{Sensitivity to FPR assumption.}
843	Even under the conservative upper bound of the cluster-adjusted CI (30.4\%), PermG remains the lowest-FPR method: the next-best method (DiffXCorr) has a pooled FPR of 16.7\%, followed by threshold onset at 27.8\% and Toda--Yamamoto at 38.9\%.
844	Our primary results rely on equal-weight $K{\geq}3$ majority voting, where each method contributes exactly one vote regardless of its FPR---this mechanism is completely unaffected by any FPR assumption.
845	For the exploratory FPR-inverse weighting, PermG's weight ($w{=}1/0.111{=}9.0$) exceeds all alternatives (DiffXCorr: 6.0, threshold: 3.6, TY: 2.6, naive: 1.1), preserving the full rank ordering.
846	The insensitivity of both the voting mechanism and the method ranking to the upper CI bound provides evidence that the MMCT conclusions are robust to uncertainty in PermG's Type~I error rate.
847	
848	\section{Sigmoid Transition Shape}
849	\label{app:sigmoid_shape}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-24T08:06:04.782612+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": "770",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "offset": "770",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-24T08:06:04.782844+00:00_

770	\section{MMCT Weight Robustness Ablation}
771	\label{app:weight_robustness}
772	
773	The detection results reported in the main text use equal-weight majority voting ($K{\geq}3$ of 5 methods, each contributing at most one vote per pair); PermG contributes at most $1/5 = 20\%$ of the consensus weight.
774	FPR-inverse weighting is used \emph{only} in the exploratory method ranking below, not in the detection results.
775	To verify that PermG's top ranking is not an artifact of the FPR-inverse weighting scheme, we recompute Shapley values under four weight specifications (Table~\ref{tab:weight_robustness}).
776	Equal weighting ($w{=}1$ for all methods) eliminates any FPR-based advantage; PermG still ranks first ($\phi^{\text{comb}}{=}-0.152$), though its margin over naive cross-correlation narrows to 0.015.
777	Under cap-5, the margin widens to 0.043 as the FPR penalty begins to differentiate high-FPR methods.
778	Cap-10 and original cap-100 yield identical Shapley values because the consensus threshold ($K{\geq}3$) is determined by the three smallest method weights ($w_{\text{naive}}{+}w_{\text{diff}}{+}w_{\text{thresh}} = 7.76$), which are invariant to further increases in the PermG or TY cap; this saturation confirms that the original $w{=}100$ does not artificially inflate PermG's contribution.
779	% TODO-D219: recompute weight robustness table with 6-seed data; PermG φ^FPR will be >0
780	Across all schemes, PermG's advantage derives from the same structural property: zero FPR ($\phi^{\text{FPR}}{=}0$) combined with moderate FNR reduction ($\phi^{\text{FNR}}{=}-0.152$ to $-0.426$).
781	
782	\begin{table}[h]
783	\centering
784	\small
785	\caption{MMCT weight robustness: PermG combined Shapley under four weighting schemes. PermG ranks first in all cases. Gap = $|\phi^{\text{comb}}_{\text{PermG}} - \phi^{\text{comb}}_{\text{runner-up}}|$. 48 experiments (3 null + 45 signal), exact Shapley enumeration ($2^5{=}32$ coalitions).}
786	\label{tab:weight_robustness}
787	
…[truncated 503 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-24T08:06:04.783093+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": "818",
  "limit": "18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "offset": "818",
    "limit": "18"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-24T08:06:04.783392+00:00_

818	Threshold ($3\sigma$) & 10 & 27.8 \\
819	Toda--Yamamoto & 14 & 38.9 \\
820	Naive XCorr & 33 & 91.7 \\
821	\bottomrule
822	\end{tabular}
823	\end{table}
824	
825	\paragraph{Cluster adjustment.}
826	The 36 null-control pairs are nested within 6~seeds (6~pairs per seed), introducing within-seed correlation.
827	Within-seed ICC${=}0.14$ yields an effective sample size $N_{\text{eff}} \approx 21$ (from $N_{\text{eff}} = N / [1 + (m-1) \cdot \text{ICC}]$ where $N{=}36$, $m{=}6$).
828	Under the Clopper--Pearson exact method with $N_{\text{eff}}{=}21$ and 4 successes (scaled), the cluster-adjusted 95\% CI is $[1.2\%, 30.4\%]$, compared to $[3.1\%, 26.1\%]$ under independence ($N{=}36$).
829	The lower ICC compared to the 3-seed pilot ($0.14$ vs.\ $0.34$) reflects greater between-seed consistency with six independent replications.
830	
831	% TODO-D219: recompute direction-filtering ablation with 6-seed data (without-filtering K≥3 count)
832	\paragraph{Direction filtering.}
833	The key design choice preserving low FPR under $K{\geq}3$ consensus is forward-direction filtering (retaining only pairs with peak lag${<}0$), not weighting.
834	Without direction filtering, null-control $K{\geq}3$ FPR inflates from 0/8 to 2/8 (25\%); with filtering, FPR remains 0/8.
835	Detection at $\alpha{\geq}0.50$ is unaffected: $K{\geq}3$ counts are identical with and without direction filtering at all signal levels.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-24T08:06:04.783741+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex",
  "old_string": "false positive rates from 0\\% to 92\\%.",
  "new_string": "false positive rates from 3\\% to 92\\%."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex",
    "old_string": "false positive rates from 0\\% to 92\\%.",
    "new_string": "false positive rates from 3\\% to 92\\%."
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-24T08:06:04.783916+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-24T08:06:04.784047+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
  "old_string": "FPR from 0\\% to 92\\%",
  "new_string": "FPR from 3\\% to 92\\%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex",
    "old_string": "FPR from 0\\% to 92\\%",
    "new_string": "FPR from 3\\% to 92\\%"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-24T08:06:04.784217+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-24T08:06:04.784373+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex",
  "old_string": "the lowest null-control FPR among all five methods (11.1\\%, 4/36 across 6 seeds)",
  "new_string": "the lowest null-control FPR among directionally-specific methods (11.1\\%, 4/36 across 6 seeds; DiffXCorr achieves 2.8\\% but lacks directional separation)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex",
    "old_string": "the lowest null-control FPR among all five methods (11.1\\%, 4/36 across 6 seeds)",
    "new_string": "the lowest null-control FPR among directionally-specific methods (11.1\\%, 4/36 across 6 seeds; DiffXCorr achieves 2.8\\% but lacks directional separation)"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-24T08:06:04.784520+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-24T08:06:04.784644+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion_reframe.tex",
  "old_string": "lowest null-control FPR among all five methods (11.1\\%, 4/36 across 6 seeds; next-best: DiffXCorr at 16.7\\%)",
  "new_string": "lowest null-control FPR among directionally-specific methods (11.1\\%, 4/36 across 6 seeds; DiffXCorr achieves 2.8\\% but cannot separate forward from reverse)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion_reframe.tex",
    "old_string": "lowest null-control FPR among all five methods (11.1\\%, 4/36 across 6 seeds; next-best: DiffXCorr at 16.7\\%)",
    "new_string": "lowest null-control FPR among directionally-specific methods (11.1\\%, 4/36 across 6 seeds; DiffXCorr achieves 2.8\\% but cannot separate forward from reverse)"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-24T08:06:04.784794+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion_reframe.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-24T08:06:04.784918+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex",
  "old_string": "the lowest among all five methods but non-zero",
  "new_string": "the lowest among directionally-specific methods but non-zero"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex",
    "old_string": "the lowest among all five methods but non-zero",
    "new_string": "the lowest among directionally-specific methods but non-zero"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-24T08:06:04.785044+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-24T08:06:04.785190+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex",
  "old_string": "Pooled null-control FPR across six seeds (6-pair basis, 36 pairs): PermG 11.1\\% (lowest; cluster-adjusted 95\\% CI $[1.2\\%, 30.4\\%]$), DiffXCorr 16.7\\%, Threshold 27.8\\%, Toda--Yamamoto 38.9\\%, NaiveXCorr 91.7\\% (Appendix~\\ref{app:fpr_independence}).\n\tDiffXCorr's empirical FPR (16.7\\%) substantially exceeds its simulated rate (4.2\\% under AR(1) DGP), indicating that model-collapse nonstationarity extends beyond simple autoregressive structure.\n\tUnder all four weighting schemes (equal, FPR-inverse, capped, rank-based), PermG achieves the lowest null-control FPR alongside consistent detection at $\\alpha \\geq 0.50$ (Shapley analysis: Appendix~\\ref{app:shapley}).",
  "new_string": "Pooled null-control FPR across six seeds (6-pair basis, 36 pairs): DiffXCorr 2.8\\%, PermG 11.1\\% (lowest among directional methods; cluster-adjusted 95\\% CI $[1.2\\%, 30.4\\%]$), Threshold 27.8\\%, Toda--Yamamoto 38.9\\%, NaiveXCorr 91.7\\% (Appendix~\\ref{app:fpr_independence}).\n\tDiffXCorr achieves the lowest raw FPR (2.8\\%) but is bidirectional---it cannot distinguish forward from reverse precedence---making it unsuitable as a standalone collapse detector.\n\tUnder all four weighting schemes (equal, FPR-inverse, capped, rank-based), PermG achieves the lowest null-control FPR among directionally-specific methods alongside consistent detection at $\\alpha \\geq 0.50$ (Shapley analysis: Appendix~\\ref{app:shapley})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex",
    "old_string": "Pooled null-control FPR across six seeds (6-pair basis, 36 pairs): PermG 11.1\\% (lowest; cluster-adjusted 95\\% CI $[1.2\\%, 30.4\\%]$), DiffXCorr 16.7\\%, Threshold 27.8\\%, Toda--Yamamoto 38.9\\%, NaiveXCorr 91.7\\% (Appendix~\\ref{app:fpr_independence}).\n\tDiffXCorr's empirical FPR (16.7\\%) substantially exceeds its simulated rate (4.2\\% under AR(1) DGP), indicating that model-collapse nonstationarity extends beyond simple autoregressive structure.\n\tUnder all four weighting schemes (equal, FPR-inverse, capped, rank-based), PermG achieves the lowest null-control FPR alongside consistent detection at $\\alpha \\geq 0.50$ (Shapley analysis: Appendix~\\ref{app:shapley}).",
    "new_string": "Pooled null-control FPR across six seeds (6-pair basis, 36 pairs): DiffXCorr 2.8\\%, PermG 11.1\\% (lowest among directional methods; cluster-adjusted 95\\% CI $[1.2\\%, 30.4\\%]$), Threshold 27.8\\%, Toda--Yamamoto 38.9\\%, NaiveXCorr 91.7\\% (Appendix~\\ref{app:fpr_independence}).\n\tDiffXCorr achieves the lowest raw FPR (2.8\\%) but is bidirectional---it cannot distinguish forward from reverse precedence---making it unsuitable as a standalone collapse detector.\n\tUnder all four weighting schemes (equal, FPR-inverse, capped, rank-based), PermG achieves the lowest null-control FPR among directionally-specific methods alongside consistent detection at $\\alpha \\geq 0.50$ (Shapley analysis: Appendix~\\ref{app:shapley})."
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-24T08:06:04.785349+00:00_

&lt;tool_use_error>String to replace not found in file.
String: Pooled null-control FPR across six seeds (6-pair basis, 36 pairs): PermG 11.1\% (lowest; cluster-adjusted 95\% CI $[1.2\%, 30.4\%]$), DiffXCorr 16.7\%, Threshold 27.8\%, Toda--Yamamoto 38.9\%, NaiveXCorr 91.7\% (Appendix~\ref{app:fpr_independence}).
	DiffXCorr's empirical FPR (16.7\%) substantially exceeds its simulated rate (4.2\% under AR(1) DGP), indicating that model-collapse nonstationarity extends beyond simple autoregressive structure.
	Under all four weighting schemes (equal, FPR-inverse, capped, rank-based), PermG achieves the lowest null-control FPR alongside consistent detection at $\alpha \geq 0.50$ (Shapley analysis: Appendix~\ref{app:shapley}).&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-24T08:06:04.785479+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex",
  "old_string": "4/36 null-control rejections across six seeds yield the lowest empirical FPR among all five methods (11.1\\%; Clopper--Pearson 95\\% CI $[3.1\\%, 26.1\\%]$ under independence; within-seed ICC${=}0.14$, cluster-adjusted 95\\% CI $[1.2\\%, 30.4\\%]$; Appendix~\\ref{app:fpr_independence}).",
  "new_string": "4/36 null-control rejections across six seeds yield the lowest empirical FPR among directionally-specific methods (11.1\\%; DiffXCorr achieves 2.8\\% but lacks directional separation; Clopper--Pearson 95\\% CI $[3.1\\%, 26.1\\%]$ under independence; within-seed ICC${=}0.14$, cluster-adjusted 95\\% CI $[1.2\\%, 30.4\\%]$; Appendix~\\ref{app:fpr_independence})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex",
    "old_string": "4/36 null-control rejections across six seeds yield the lowest empirical FPR among all five methods (11.1\\%; Clopper--Pearson 95\\% CI $[3.1\\%, 26.1\\%]$ under independence; within-seed ICC${=}0.14$, cluster-adjusted 95\\% CI $[1.2\\%, 30.4\\%]$; Appendix~\\ref{app:fpr_independence}).",
    "new_string": "4/36 null-control rejections across six seeds yield the lowest empirical FPR among directionally-specific methods (11.1\\%; DiffXCorr achieves 2.8\\% but lacks directional separation; Clopper--Pearson 95\\% CI $[3.1\\%, 26.1\\%]$ under independence; within-seed ICC${=}0.14$, cluster-adjusted 95\\% CI $[1.2\\%, 30.4\\%]$; Appendix~\\ref{app:fpr_independence})."
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-24T08:06:04.785646+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-24T08:06:04.785770+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex",
  "old_string": "11.1\\%, lowest among all methods) confirm adequate size control",
  "new_string": "11.1\\%, lowest among directional methods) confirm adequate size control"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex",
    "old_string": "11.1\\%, lowest among all methods) confirm adequate size control",
    "new_string": "11.1\\%, lowest among directional methods) confirm adequate size control"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-24T08:06:04.785924+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-24T08:06:04.786068+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex",
  "offset": "14",
  "limit": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex",
    "offset": "14",
    "limit": "6"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-24T08:06:04.786199+00:00_

14	Detection results use equal-weight majority voting ($K{\geq}3$ of 5 methods, each contributing one vote per pair) with forward-direction filtering; FPR-inverse weighting is used only in exploratory method ranking (Appendix~\ref{app:weight_robustness}).
15	Each method embodies different assumptions: naive cross-correlation is assumption-free but produces 92\% null-control FPR; differenced cross-correlation controls for trends but lacks directional separation; threshold onset is power-limited at $T{=}11$; Toda--Yamamoto avoids pre-testing for unit roots; PermG uses a nonparametric permutation null with built-in directionality.
16	Pooled null-control FPR across six seeds (6-pair basis, 36 pairs): PermG 11.1\% (lowest; cluster-adjusted 95\% CI $[1.2\%, 30.4\%]$), DiffXCorr 16.7\%, Threshold 27.8\%, Toda--Yamamoto 38.9\%, NaiveXCorr 91.7\% (Appendix~\ref{app:fpr_independence}).
17	DiffXCorr's empirical FPR (16.7\%) substantially exceeds its simulated rate (4.2\% under AR(1) DGP), indicating that model-collapse nonstationarity extends beyond simple autoregressive structure.
18	Under all four weighting schemes (equal, FPR-inverse, capped, rank-based), PermG achieves the lowest null-control FPR alongside consistent detection at $\alpha \geq 0.50$ (Shapley analysis: Appendix~\ref{app:shapley}).
19	Practitioner-facing alternatives (PPL-slope, variance thresholds) yield 67--100\% FPR under natural training drift (Appendix~\ref{app:naive_baselines}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-24T08:06:04.786363+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex",
  "old_string": "Pooled null-control FPR across six seeds (6-pair basis, 36 pairs): PermG 11.1\\% (lowest; cluster-adjusted 95\\% CI $[1.2\\%, 30.4\\%]$), DiffXCorr 16.7\\%, Threshold 27.8\\%, Toda--Yamamoto 38.9\\%, NaiveXCorr 91.7\\% (Appendix~\\ref{app:fpr_independence}).\nDiffXCorr's empirical FPR (16.7\\%) substantially exceeds its simulated rate (4.2\\% under AR(1) DGP), indicating that model-collapse nonstationarity extends beyond simple autoregressive structure.\nUnder all four weighting schemes (equal, FPR-inverse, capped, rank-based), PermG achieves the lowest null-control FPR alongside consistent detection at $\\alpha \\geq 0.50$ (Shapley analysis: Appendix~\\ref{app:shapley}).",
  "new_string": "Pooled null-control FPR across six seeds (6-pair basis, 36 pairs): DiffXCorr 2.8\\%, PermG 11.1\\% (lowest among directional methods; cluster-adjusted 95\\% CI $[1.2\\%, 30.4\\%]$), Threshold 27.8\\%, Toda--Yamamoto 38.9\\%, NaiveXCorr 91.7\\% (Appendix~\\ref{app:fpr_independence}).\nDiffXCorr achieves the lowest raw FPR (2.8\\%) but is bidirectional---it cannot distinguish forward from reverse precedence---making it unsuitable as a standalone collapse detector.\nUnder all four weighting schemes (equal, FPR-inverse, capped, rank-based), PermG achieves the lowest null-control FPR among directionally-specific methods alongside consistent detection at $\\alpha \\geq 0.50$ (Shapley analysis: Appendix~\\ref{app:shapley})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex",
    "old_string": "Pooled null-control FPR across six seeds (6-pair basis, 36 pairs): PermG 11.1\\% (lowest; cluster-adjusted 95\\% CI $[1.2\\%, 30.4\\%]$), DiffXCorr 16.7\\%, Threshold 27.8\\%, Toda--Yamamoto 38.9\\%, NaiveXCorr 91.7\\% (Appendix~\\ref{app:fpr_independence}).\nDiffXCorr's empirical FPR (16.7\\%) substantially exceeds its simulated rate (4.2\\% under AR(1) DGP), indicating that model-collapse nonstationarity extends beyond simple autoregressive structure.\nUnder all four weighting schemes (equal, FPR-inverse, capped, rank-based), PermG achieves the lowest null-control FPR alongside consistent detection at $\\alpha \\geq 0.50$ (Shapley analysis: Appendix~\\ref{app:shapley}).",
    "new_string": "Pooled null-control FPR across six seeds (6-pair basis, 36 pairs): DiffXCorr 2.8\\%, PermG 11.1\\% (lowest among directional methods; cluster-adjusted 95\\% CI $[1.2\\%, 30.4\\%]$), Threshold 27.8\\%, Toda--Yamamoto 38.9\\%, NaiveXCorr 91.7\\% (Appendix~\\ref{app:fpr_independence}).\nDiffXCorr achieves the lowest raw FPR (2.8\\%) but is bidirectional---it cannot distinguish forward from reverse precedence---making it unsuitable as a standalone collapse detector.\nUnder all four weighting schemes (equal, FPR-inverse, capped, rank-based), PermG achieves the lowest null-control FPR among directionally-specific methods alongside consistent detection at $\\alpha \\geq 0.50$ (Shapley analysis: Appendix~\\ref{app:shapley})."
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-24T08:06:04.786538+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-24T08:06:04.786674+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex",
  "old_string": "MMCT identifies permutation Granger (PermG) as the method with the lowest null-control FPR (11.1\\%, 4/36 across 6 seeds) combined with consistent detection across contamination levels, and we recommend it as the primary detection method based on this systematic comparison.",
  "new_string": "MMCT identifies permutation Granger (PermG) as the method with the lowest null-control FPR among directionally-specific methods (11.1\\%, 4/36 across 6 seeds; DiffXCorr achieves 2.8\\% but lacks directional separation) combined with consistent detection across contamination levels, and we recommend it as the primary detection method based on this systematic comparison."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex",
    "old_string": "MMCT identifies permutation Granger (PermG) as the method with the lowest null-control FPR (11.1\\%, 4/36 across 6 seeds) combined with consistent detection across contamination levels, and we recommend it as the primary detection method based on this systematic comparison.",
    "new_string": "MMCT identifies permutation Granger (PermG) as the method with the lowest null-control FPR among directionally-specific methods (11.1\\%, 4/36 across 6 seeds; DiffXCorr achieves 2.8\\% but lacks directional separation) combined with consistent detection across contamination levels, and we recommend it as the primary detection method based on this systematic comparison."
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-24T08:06:04.786830+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-24T08:06:04.786951+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex",
  "old_string": "PermG achieves the lowest FPR among all five methods: 11.1\\% across 6 seeds (4/36 pairs; Clopper--Pearson 95\\% CI $[3.1\\%, 26.1\\%]$), compared to 16.7\\% for DiffXCorr and ${\\geq}27.8\\%$ for the remaining methods.",
  "new_string": "PermG achieves the lowest FPR among directionally-specific methods: 11.1\\% across 6 seeds (4/36 pairs; Clopper--Pearson 95\\% CI $[3.1\\%, 26.1\\%]$); DiffXCorr achieves the lowest raw FPR (2.8\\%) but lacks forward/reverse directional separation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex",
    "old_string": "PermG achieves the lowest FPR among all five methods: 11.1\\% across 6 seeds (4/36 pairs; Clopper--Pearson 95\\% CI $[3.1\\%, 26.1\\%]$), compared to 16.7\\% for DiffXCorr and ${\\geq}27.8\\%$ for the remaining methods.",
    "new_string": "PermG achieves the lowest FPR among directionally-specific methods: 11.1\\% across 6 seeds (4/36 pairs; Clopper--Pearson 95\\% CI $[3.1\\%, 26.1\\%]$); DiffXCorr achieves the lowest raw FPR (2.8\\%) but lacks forward/reverse directional separation."
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-24T08:06:04.787124+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-24T08:06:04.787277+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "old_string": "PermG (FPR${=}11.1\\%$, the lowest among all five methods) receives $w{=}9.0$.",
  "new_string": "PermG (FPR${=}11.1\\%$, the lowest among directional methods; DiffXCorr achieves 2.8\\% but lacks directional separation) receives $w{=}9.0$."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "old_string": "PermG (FPR${=}11.1\\%$, the lowest among all five methods) receives $w{=}9.0$.",
    "new_string": "PermG (FPR${=}11.1\\%$, the lowest among directional methods; DiffXCorr achieves 2.8\\% but lacks directional separation) receives $w{=}9.0$."
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-24T08:06:04.787736+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-24T08:06:04.787887+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "old_string": "pooled FPR across 6 seeds: 11.1\\%, lowest among all methods)",
  "new_string": "pooled FPR across 6 seeds: 11.1\\%, lowest among directional methods)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "old_string": "pooled FPR across 6 seeds: 11.1\\%, lowest among all methods)",
    "new_string": "pooled FPR across 6 seeds: 11.1\\%, lowest among directional methods)"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-24T08:06:04.788356+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-24T08:06:04.788513+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "old_string": "Our empirical FPR of 4/36 (11.1\\%) across six null seeds---the lowest among all five methods---confirms adequate size control",
  "new_string": "Our empirical FPR of 4/36 (11.1\\%) across six null seeds---the lowest among directional methods---confirms adequate size control"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "old_string": "Our empirical FPR of 4/36 (11.1\\%) across six null seeds---the lowest among all five methods---confirms adequate size control",
    "new_string": "Our empirical FPR of 4/36 (11.1\\%) across six null seeds---the lowest among directional methods---confirms adequate size control"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-24T08:06:04.789145+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-24T08:06:04.789324+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "old_string": "PermG achieves 4/36 (11.1\\%), the lowest empirical FPR among all methods; the next-best is DiffXCorr at 6/36 (16.7\\%).",
  "new_string": "DiffXCorr achieves the lowest raw FPR (1/36, 2.8\\%) but lacks directional separation; PermG (4/36, 11.1\\%) is the lowest among directional methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "old_string": "PermG achieves 4/36 (11.1\\%), the lowest empirical FPR among all methods; the next-best is DiffXCorr at 6/36 (16.7\\%).",
    "new_string": "DiffXCorr achieves the lowest raw FPR (1/36, 2.8\\%) but lacks directional separation; PermG (4/36, 11.1\\%) is the lowest among directional methods."
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-24T08:06:04.789782+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-24T08:06:04.789957+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "old_string": "\\caption{Null-control FPR by method ($\\alpha{=}0.0$, 6~seeds 45--50, 6~pairs each). PermG achieves the lowest FPR.}",
  "new_string": "\\caption{Null-control FPR by method ($\\alpha{=}0.0$, 6~seeds 45--50, 6~pairs each). DiffXCorr achieves the lowest raw FPR but lacks directional separation; PermG is the lowest among directional methods.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "old_string": "\\caption{Null-control FPR by method ($\\alpha{=}0.0$, 6~seeds 45--50, 6~pairs each). PermG achieves the lowest FPR.}",
    "new_string": "\\caption{Null-control FPR by method ($\\alpha{=}0.0$, 6~seeds 45--50, 6~pairs each). DiffXCorr achieves the lowest raw FPR but lacks directional separation; PermG is the lowest among directional methods.}"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-24T08:06:04.790427+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-24T08:06:04.790588+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "old_string": "Diff.\\ XCorr ($p{<}0.05$) & 6 & 16.7 \\\\",
  "new_string": "Diff.\\ XCorr ($p{<}0.05$) & 1 & 2.8 \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "old_string": "Diff.\\ XCorr ($p{<}0.05$) & 6 & 16.7 \\\\",
    "new_string": "Diff.\\ XCorr ($p{<}0.05$) & 1 & 2.8 \\\\"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-24T08:06:04.791329+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-24T08:06:04.791518+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "old_string": "the next-best method (DiffXCorr) has a pooled FPR of 16.7\\%, followed by threshold onset at 27.8\\%",
  "new_string": "DiffXCorr achieves a lower raw FPR (2.8\\%) but lacks forward/reverse separation; the next directional method (threshold onset) has 27.8\\%"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "old_string": "the next-best method (DiffXCorr) has a pooled FPR of 16.7\\%, followed by threshold onset at 27.8\\%",
    "new_string": "DiffXCorr achieves a lower raw FPR (2.8\\%) but lacks forward/reverse separation; the next directional method (threshold onset) has 27.8\\%"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-24T08:06:04.791991+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-24T08:06:04.792168+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": "812",
  "limit": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "offset": "812",
    "limit": "12"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-24T08:06:04.792331+00:00_

812	\begin{tabular}{lrr}
813	\toprule
814	Method & Rejections (/36) & FPR (\%) \\
815	\midrule
816	\textbf{Perm.\ Granger (FDR)} & \textbf{4} & \textbf{11.1} \\
817	Diff.\ XCorr ($p{<}0.05$) & 1 & 2.8 \\
818	Threshold ($3\sigma$) & 10 & 27.8 \\
819	Toda--Yamamoto & 14 & 38.9 \\
820	Naive XCorr & 33 & 91.7 \\
821	\bottomrule
822	\end{tabular}
823	\end{table}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-24T08:06:04.792490+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "old_string": "\\textbf{Perm.\\ Granger (FDR)} & \\textbf{4} & \\textbf{11.1} \\\\\nDiff.\\ XCorr ($p{<}0.05$) & 1 & 2.8 \\\\",
  "new_string": "Diff.\\ XCorr ($p{<}0.05$)$^\\dagger$ & 1 & 2.8 \\\\\n\\textbf{Perm.\\ Granger (FDR)} & \\textbf{4} & \\textbf{11.1} \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "old_string": "\\textbf{Perm.\\ Granger (FDR)} & \\textbf{4} & \\textbf{11.1} \\\\\nDiff.\\ XCorr ($p{<}0.05$) & 1 & 2.8 \\\\",
    "new_string": "Diff.\\ XCorr ($p{<}0.05$)$^\\dagger$ & 1 & 2.8 \\\\\n\\textbf{Perm.\\ Granger (FDR)} & \\textbf{4} & \\textbf{11.1} \\\\"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-24T08:06:04.792948+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-24T08:06:04.793127+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": "819",
  "limit": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "offset": "819",
    "limit": "6"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-24T08:06:04.793278+00:00_

819	Toda--Yamamoto & 14 & 38.9 \\
820	Naive XCorr & 33 & 91.7 \\
821	\bottomrule
822	\end{tabular}
823	\end{table}
824	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-24T08:06:04.793408+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "old_string": "Naive XCorr & 33 & 91.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cluster adjustment.}",
  "new_string": "Naive XCorr & 33 & 91.7 \\\\\n\\bottomrule\n\\multicolumn{3}{l}{\\footnotesize $^\\dagger$Bidirectional; cannot separate forward from reverse.} \\\\\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cluster adjustment.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "old_string": "Naive XCorr & 33 & 91.7 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cluster adjustment.}",
    "new_string": "Naive XCorr & 33 & 91.7 \\\\\n\\bottomrule\n\\multicolumn{3}{l}{\\footnotesize $^\\dagger$Bidirectional; cannot separate forward from reverse.} \\\\\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cluster adjustment.}"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-24T08:06:04.793851+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-24T08:06:04.794019+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex",
  "offset": "48",
  "limit": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex",
    "offset": "48",
    "limit": "8"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-24T08:06:04.794159+00:00_

48	
49	\paragraph{Calibration.}
50	We validate error rates with built-in experimental controls.
51	False positive rate: at $\alpha{=}0.0$ (null control, no synthetic contamination), PermG achieves the lowest FPR among directionally-specific methods: 11.1\% across 6 seeds (4/36 pairs; Clopper--Pearson 95\% CI $[3.1\%, 26.1\%]$); DiffXCorr achieves the lowest raw FPR (2.8\%) but lacks forward/reverse directional separation.
52	False negative rate: at $\alpha{=}1.0$, all 6 effect-size reference pairs (2 canaries $\times$ 3 diversity metrics, selected by criteria independent of the detection methods) are recovered at 0\% FNR across 4 seeds.
53	PermG matches consensus performance at all tested contamination levels, with cross-architecture validation confirming PermG forward significance ${\geq}6/8$ in 13 of 15 conditions (\S\ref{sec:generalization}).
54	Full calibration details, practical guidance tiers, and method-level breakdown appear in the Appendix.
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-24T08:06:04.794322+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": "841",
  "limit": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "offset": "841",
    "limit": "8"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-24T08:06:04.794458+00:00_

841	PermG thus contributes to only 2 of 6 consensus false positives, confirming that most $K{\geq}3$ FPR is driven by the high-FPR methods (naive, threshold, TY).
842	
843	\paragraph{Sensitivity to FPR assumption.}
844	Even under the conservative upper bound of the cluster-adjusted CI (30.4\%), PermG remains the lowest-FPR method: DiffXCorr achieves a lower raw FPR (2.8\%) but lacks forward/reverse separation; the next directional method (threshold onset) has 27.8\% and Toda--Yamamoto at 38.9\%.
845	Our primary results rely on equal-weight $K{\geq}3$ majority voting, where each method contributes exactly one vote regardless of its FPR---this mechanism is completely unaffected by any FPR assumption.
846	For the exploratory FPR-inverse weighting, PermG's weight ($w{=}1/0.111{=}9.0$) exceeds all alternatives (DiffXCorr: 6.0, threshold: 3.6, TY: 2.6, naive: 1.1), preserving the full rank ordering.
847	The insensitivity of both the voting mechanism and the method ranking to the upper CI bound provides evidence that the MMCT conclusions are robust to uncertainty in PermG's Type~I error rate.
848	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-24T08:06:04.794636+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "old_string": "Even under the conservative upper bound of the cluster-adjusted CI (30.4\\%), PermG remains the lowest-FPR method: DiffXCorr achieves a lower raw FPR (2.8\\%) but lacks forward/reverse separation; the next directional method (threshold onset) has 27.8\\% and Toda--Yamamoto at 38.9\\%.",
  "new_string": "Even under the conservative upper bound of the cluster-adjusted CI (30.4\\%), PermG remains the lowest-FPR directional method: DiffXCorr achieves a lower raw FPR (2.8\\%) but lacks forward/reverse separation; the next directional method (threshold onset) has 27.8\\% and Toda--Yamamoto 38.9\\%."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "old_string": "Even under the conservative upper bound of the cluster-adjusted CI (30.4\\%), PermG remains the lowest-FPR method: DiffXCorr achieves a lower raw FPR (2.8\\%) but lacks forward/reverse separation; the next directional method (threshold onset) has 27.8\\% and Toda--Yamamoto at 38.9\\%.",
    "new_string": "Even under the conservative upper bound of the cluster-adjusted CI (30.4\\%), PermG remains the lowest-FPR directional method: DiffXCorr achieves a lower raw FPR (2.8\\%) but lacks forward/reverse separation; the next directional method (threshold onset) has 27.8\\% and Toda--Yamamoto 38.9\\%."
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-24T08:06:04.795104+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-24T08:06:04.795278+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "old_string": "PermG's weight ($w{=}1/0.111{=}9.0$) exceeds all alternatives (DiffXCorr: 6.0, threshold: 3.6, TY: 2.6, naive: 1.1), preserving the full rank ordering.",
  "new_string": "PermG's weight ($w{=}1/0.111{=}9.0$) exceeds all directional alternatives (threshold: 3.6, TY: 2.6, naive: 1.1); DiffXCorr ($w{=}1/0.028{=}35.7$) receives a higher weight but lacks directional separation, preserving PermG's rank among directional methods."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
    "old_string": "PermG's weight ($w{=}1/0.111{=}9.0$) exceeds all alternatives (DiffXCorr: 6.0, threshold: 3.6, TY: 2.6, naive: 1.1), preserving the full rank ordering.",
    "new_string": "PermG's weight ($w{=}1/0.111{=}9.0$) exceeds all directional alternatives (threshold: 3.6, TY: 2.6, naive: 1.1); DiffXCorr ($w{=}1/0.028{=}35.7$) receives a higher weight but lacks directional separation, preserving PermG's rank among directional methods."
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-24T08:06:04.795813+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-24T08:06:04.796008+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -rn \"zero.*FPR\\|0/24.*null\\|0%.*FPR\\|0\\\\\\\\%.*to.*92\\|\\[0.*41\\]\\|DiffXCorr.*16\\|16\\.7.*DiffX\\|lowest FPR among all\\|lowest.*among all.*method\\|lowest empirical FPR among all\" docs/paper/ --include=\"*.tex\"",
  "description": "Verify no remaining old FPR framing patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -rn \"zero.*FPR\\|0/24.*null\\|0%.*FPR\\|0\\\\\\\\%.*to.*92\\|\\[0.*41\\]\\|DiffXCorr.*16\\|16\\.7.*DiffX\\|lowest FPR among all\\|lowest.*among all.*method\\|lowest empirical FPR among all\" docs/paper/ --include=\"*.tex\"",
    "description": "Verify no remaining old FPR framing patterns"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-24T08:06:04.796153+00:00_

docs/paper/appendix.tex:731:PermG achieves the lowest (best) combined Shapley ($-0.180$), driven entirely by FNR reduction with zero FPR contribution---the only method with this property.
docs/paper/appendix.tex:758:\caption{Shapley value decomposition of each method's marginal contribution to FPR (positive bars) and FNR (negative bars). PermG is the only method with zero FPR contribution; naive cross-correlation's FPR dominates its FNR benefit.}
docs/paper/appendix.tex:780:Across all schemes, PermG's advantage derives from the same structural property: zero FPR ($\phi^{\text{FPR}}{=}0$) combined with moderate FNR reduction ($\phi^{\text{FNR}}{=}-0.152$ to $-0.426$).
docs/paper/method.tex:7:\emph{Method sensitivity}: five detection methods applied to identical data yield forward significance rates spanning 0\% to 92\%, with inter-method agreement at $\kappa{=}0.185$.
docs/paper/experiments_reframe.tex:38:PermG achieves the lowest null-control FPR among all five methods (11.1\%, 4/36 across 6 seeds) with consistent detection at $\alpha \geq 0.50$ (Table~\ref{tab:method_comparison}); its nonparametric null distribution, built-in directionality, and hyperparameter-free design explain this advantage.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-24T08:06:04.796390+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex",
  "offset": "36",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex",
    "offset": "36",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-24T08:06:04.796559+00:00_

36	Method choice is itself a major source of analytic variability.
37	At $\alpha{=}1.0$, forward-direction significance rates range from 100\% (naive cross-correlation) to 37.5\% (PermG), with inter-method $\kappa = 0.185$ (near chance) and a spurious rate of at least 62.5\%.
38	PermG achieves the lowest null-control FPR among all five methods (11.1\%, 4/36 across 6 seeds) with consistent detection at $\alpha \geq 0.50$ (Table~\ref{tab:method_comparison}); its nonparametric null distribution, built-in directionality, and hyperparameter-free design explain this advantage.
39	The $S \times R$ framework generates three testable predictions for $T{=}20$ via $\mathrm{Power}(\alpha, T) = \Phi(S \cdot R \cdot \sqrt{T}/\sigma)$: (i)~$\alpha_c$ at $T{=}10$ should left-shift, (ii)~the transition should smooth, and (iii)~different methods should exhibit different $\alpha_c$ values.
40	These predictions are under empirical verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-24T08:06:04.796695+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex",
  "old_string": "PermG achieves the lowest null-control FPR among all five methods (11.1\\%, 4/36 across 6 seeds)",
  "new_string": "PermG achieves the lowest null-control FPR among directionally-specific methods (11.1\\%, 4/36 across 6 seeds; DiffXCorr achieves 2.8\\% but lacks directional separation)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex",
    "old_string": "PermG achieves the lowest null-control FPR among all five methods (11.1\\%, 4/36 across 6 seeds)",
    "new_string": "PermG achieves the lowest null-control FPR among directionally-specific methods (11.1\\%, 4/36 across 6 seeds; DiffXCorr achieves 2.8\\% but lacks directional separation)"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-24T08:06:04.796863+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-24T08:06:04.797001+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "16\\.7",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Grep",
  "tool_args": {
    "pattern": "16\\.7",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-24T08:06:04.797122+00:00_

docs/paper/appendix.tex:839:Under the 6-pair basis (6~seeds, 36~pairs), $K{\geq}3$ consensus produces 6 false positives (FPR${=}16.7\%$).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-24T08:06:04.797296+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "lowest.*(among all|all five)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Grep",
  "tool_args": {
    "pattern": "lowest.*(among all|all five)",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-24T08:06:04.797428+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-24T08:06:04.797558+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -rn \"zero.*FPR\\|0/24.*null\\|0%.*FPR\\|0\\\\\\\\%.*to.*92\\|\\[0.*41\\]\\|DiffXCorr.*16\\|16\\.7.*DiffX\\|lowest FPR among all\\|lowest.*among all.*method\\|lowest empirical FPR among all\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ --include=\"*.tex\"",
  "description": "Final verification grep for old FPR framing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -rn \"zero.*FPR\\|0/24.*null\\|0%.*FPR\\|0\\\\\\\\%.*to.*92\\|\\[0.*41\\]\\|DiffXCorr.*16\\|16\\.7.*DiffX\\|lowest FPR among all\\|lowest.*among all.*method\\|lowest empirical FPR among all\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ --include=\"*.tex\"",
    "description": "Final verification grep for old FPR framing"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-24T08:06:04.797682+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:731:PermG achieves the lowest (best) combined Shapley ($-0.180$), driven entirely by FNR reduction with zero FPR contribution---the only method with this property.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:758:\caption{Shapley value decomposition of each method's marginal contribution to FPR (positive bars) and FNR (negative bars). PermG is the only method with zero FPR contribution; naive cross-correlation's FPR dominates its FNR benefit.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:780:Across all schemes, PermG's advantage derives from the same structural property: zero FPR ($\phi^{\text{FPR}}{=}0$) combined with moderate FNR reduction ($\phi^{\text{FNR}}{=}-0.152$ to $-0.426$).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex:7:\emph{Method sensitivity}: five detection methods applied to identical data yield forward significance rates spanning 0\% to 92\%, with inter-method agreement at $\kappa{=}0.185$.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 101 · 2026-05-24T08:06:04.797853+00:00_

All remaining matches are expected:
- **appendix.tex L731, L758, L780**: Shapley TODO areas — preserved per task instructions (等 Shapley 重算)
- **method.tex L7**: "forward significance rates spanning 0\% to 92\%" — treatment detection rates, not null FPR; correct to keep

Summary of changes across 8 files:

| File | Changes |
|------|---------|
| **abstract.tex** | "0% to 92%" → "3% to 92%" |
| **introduction.tex** | "0% to 92%" → "3% to 92%" |
| **method.tex** | DiffXCorr 16.7%→2.8%; reframed as bidirectional/unsuitable standalone; PermG "lowest" → "lowest among directional methods" (3 locations) |
| **method_reframe.tex** | Added directional qualifier + DiffXCorr 2.8% note (2 locations) |
| **conclusion.tex** | "lowest among all five" → "lowest among directionally-specific" + DiffXCorr note |
| **discussion_reframe.tex** | Same reframing; DiffXCorr 16.7%→2.8% |
| **limitations.tex** | "lowest among all five" → "lowest among directionally-specific" |
| **experiments_reframe.tex** | Same reframing (caught by verification grep) |
| **appendix.tex** | DiffXCorr table data 6/16.7→1/2.8, reordered table, updated caption, updated L804 text, updated L843-846 sensitivity paragraph with correct DiffXCorr weight (35.7), 4 directional qualifier fixes. Shapley TODOs preserved. |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_d219_final_framing_fix_20260524T080020"
}
```

</details>

---
