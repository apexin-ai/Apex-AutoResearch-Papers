# Research conversation: I need to analyze the structure of an academic paper for space optimization. The paper is at /home/ubuntu/.agent-ml-rese

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aac173aafa6353ad3.jsonl`
- **Structured JSON:** [`457781a0776ce02c77b6.json`](../../sessions/45/457781a0776ce02c77b6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-24T18:28:16.198Z_

I need to analyze the structure of an academic paper for space optimization. The paper is at /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/

Please do the following:
1. Read related_work.tex fully - I need to know its current subsection structure and approximate length
2. Read introduction.tex fully - check for figures and length
3. Read method.tex fully - check for figures and length  
4. Read experiments.tex fully - check for figures and length
5. Read discussion.tex fully - check for figures and length
6. Read conclusion.tex if it exists
7. Read limitations.tex fully
8. Read appendix.tex - specifically look for figures that could be promoted to main text (list all figure labels and what they show)
9. Count total figures in main text vs appendix

Report:
- Current Related Work subsection structure (how many subsections, their titles)
- List of ALL figures in main text (label, which file, what they show)
- List of ALL figures in appendix (label, which file, what they show, whether they'd add narrative value to main text)
- Which sections seem longest/most compressible
- Line counts for each file

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "51e3df65-9561-4454-8292-70ea3a87414d",
  "agentId": "aac173aafa6353ad3",
  "type": "user",
  "uuid": "2674ba5d-fc3a-497f-8084-c0708421d450",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-24T18:28:18.043Z_

I'll analyze the paper structure and content for you. Let me start by reading all the tex files in the paper directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2674ba5d-fc3a-497f-8084-c0708421d450",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsEpNZoN5nLGezEDMKM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6951bdee-c4c3-47cd-8fc2-25f5bf27a603",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZGJvEMyUqGg1ExhqNTdqy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37449,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T18:28:18.260Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JdvoxFAQDKs5KuMQrNVhgo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6951bdee-c4c3-47cd-8fc2-25f5bf27a603",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsEpNZoN5nLGezEDMKM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b1f43255-f61e-49ee-95db-17f53a6d6a52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZGJvEMyUqGg1ExhqNTdqy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37449,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-24T18:28:18.282Z_

<details><summary>↩ Tool result · `toolu_01JdvoxFAQDKs5KuMQrNVhgo`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and monitoring.}
5	Iterative training collapse was formalized by \citet{shumailov2024curse} and \citet{alemohammad2024mad}; \citet{schaeffer2025position} systematize eight distinct notions of collapse---our operationalization aligns with their \emph{distributional shift} family (definitions~D4--D6).
6	Theoretical analyses sharpen these results: \citet{dohmatob2024tale} recast collapse as changed scaling-law exponents, \citet{dohmatob2025strong} proved collapse at vanishingly small synthetic fractions, and \citet{truong2026phase} prove entropy collapse is a first-order transition, structurally ruling out critical-slowing-down early-warning signals~\cite{scheffer2009early,scheffer2012anticipating}.
7	Monitoring metrics include ECE~\cite{du2025scales}, surplexity~\cite{gambetta2024surplexity}, and machine-generated text detection~\cite{drayson2025detection}; \citet{shi2025closer} independently validate entropy as a collapse diagnostic in diffusion models.
8	We differ from prior work by cross-validating five statistical methods, mapping detectability across contamination regimes, and treating method sensitivity as a primary finding (comparison: Appendix~\ref{app:method_comparison}).
9	
10	\paragraph{Phase transitions and lead-lag methodology.}
11	Critical mixture ratios separating qualitative outcomes have precedent: \citet{kazdan2025collapse} map collapse conditions, \citet{gu2024cmr} establish scaling laws for critical ratios, and \citet{gu2025datamixing} show data mixing induces phase transitions in knowledge acquisition.
12	For temporal precedence testing, Granger causality~\cite{granger1969investigating} is standard, with neural extensions~\citep{tank2021neural,runge2019detecting}; however, non-stationary series inflate rejection rates~\cite{granger1974spurious}, and short series ($T{\leq}25$) preclude reliable nonlinear estimation~\cite{boettiger2012limits}.
13	Our Granger-precedence approach circumvents the CSD limitation by detecting temporal predictive improvement rather than variance/autocorrelation signatures.
14	The multiverse analysis perspective~\cite{steegen2016increasing,coretta2023multidimensional,kapoor2024reforms} motivates our multi-method comparison: five methods on identical data produce conclusions ranging from universal significance to complete null.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1f43255-f61e-49ee-95db-17f53a6d6a52",
  "isSidechain": true,
  "promptId": "51e3df65-9561-4454-8292-70ea3a87414d",
  "agentId": "aac173aafa6353ad3",
  "type": "user",
  "uuid": "404f5ab6-c651-43c0-b1c3-7ec3339a4441",
  "sourceToolAssistantUUID": "b1f43255-f61e-49ee-95db-17f53a6d6a52",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T18:28:18.469Z_

<details open><summary>🔧 Tool call — Read · `toolu_014PUHck2Tz1HtyrDJuf3s5a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "404f5ab6-c651-43c0-b1c3-7ec3339a4441",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsEpNZoN5nLGezEDMKM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eb5cbc8d-896d-413b-9ec2-9f241a002bbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZGJvEMyUqGg1ExhqNTdqy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37449,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-24T18:28:18.477Z_

<details><summary>↩ Tool result · `toolu_014PUHck2Tz1HtyrDJuf3s5a`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When language models train iteratively on their own output, the training distribution progressively loses its tail modes, a phenomenon termed model collapse~\cite{shumailov2024curse,alemohammad2024mad}.
5	This process can be triggered by vanishingly small synthetic fractions~\cite{dohmatob2025strong}: lexical diversity narrows, calibration deteriorates, and each generation inherits the biases of its predecessors.
6	As machine-generated text grows prevalent on the web, such feedback loops pose a growing risk to production pipelines, and by the time standard quality metrics register degradation, the distribution may have already shifted irreversibly.
7	
8	This threat motivates a fundamental question: \emph{what does the detectability landscape of model collapse look like?}
9	At what contamination level does statistical detection become possible, how does this boundary depend on observation length, and what structure does the landscape exhibit?
10	These questions are nontrivial because iterative training produces short, noisy time series (often fewer than 15 points), where detection power drops sharply~\cite{boettiger2012limits}. Moreover, model collapse is a first-order transition~\cite{truong2026phase}, structurally ruling out the critical-slowing-down early-warning signals that ecologists rely on~\cite{scheffer2009early} (\S\ref{sec:related_work}).
11	
12	\begin{figure*}[!tp]
13	\centering
14	\includegraphics[width=\textwidth]{figures/fig_composite_hero.pdf}
15	\caption{Detection landscape overview (Pythia-410M, fp32, PermG direction-checked).
16	\textbf{(a)}~Phase diagram: FDR-significant canary$\to$diversity pairs (of~8) across contamination~$\alpha$ and observation window~$T$; dashed curve: fitted boundary $\alpha_c(T) \propto T^{-\gamma}$; diamonds ($\diamond$): non-monotonic anomaly at $\alpha{=}0.60$; star ($\star$): dissolution at $T{=}25$.
17	\textbf{(b)}~Dose-response: PermG detection rate with sigmoid fit ($\alpha_c{=}0.483$; shaded 95\% CI); regime bands mark blind, onset, sync-dip, and detection zones.
18	\textbf{(c)}~Method sensitivity: five methods yield dramatically different FDR-significant rates on identical data; PermG (dark blue) achieves 0\% null-control FPR with 75\% detection at $\alpha{\geq}0.50$; dashed line: 5\% nominal.
19	\textbf{(d)}~Cross-architecture validation at $\alpha{=}1.0$: PermG forward detection (${\geq}6/8$) in 11/15 model-seed conditions spanning five families (345M--6.9B); faded bars: non-confirming conditions.}
20	\label{fig:hero}
21	\end{figure*}
22	
23	We empirically map this landscape on Pythia-410M~\cite{biderman2023pythia} across 13 contamination levels with multi-seed replication (Figure~\ref{fig:hero}a), and find structured terrain rather than smooth degradation: detection is absent through $\alpha{=}0.45$, then jumps from 0/8 to 6/8 significant pairs within a 2-percentage-point interval, before a non-monotonic dip and eventual reliable detection above a power-law boundary $\alpha_c(T)$ (Eq.~\ref{eq:alpha-c-theory}).
24	Cross-architecture evaluation at $\alpha{=}1.0$ across five families (345M--6.9B) supports forward detection in 11/15 conditions, with four non-confirming cases isolating distinct failure modes (\S\ref{sec:generalization}).
25	A second finding is equally consequential: five statistical methods applied to identical data yield null-control false-positive rates from 7\% to 94\%, demonstrating that the landscape one observes depends critically on the method used to probe it.
26	Our canary claim\footnote{Granger precedence establishes temporal predictive improvement, not true causation~\cite{shojaie2022granger}; bivariate tests cannot exclude confounders.} is scoped to diversity metrics (distinct-$n$~\cite{li2016diversity}).
27	
28	Our contributions are:
29	\begin{enumerate}
30	    \item \textbf{We map the detectability landscape} of iterative model collapse (\S\ref{sec:regime}--\ref{sec:dose_response}).
31	    Detection is absent through $\alpha{=}0.45$, then jumps from 0/8 to 6/8 within 2 percentage points; a detection boundary consistent with power-law scaling $\alpha_c(T) \propto T^{-\gamma}$ ($\gamma \in [0.64, 2.08]$; Eq.~\ref{eq:alpha-c-theory}) organizes three confirmed regimes (blind, onset, detection) plus one unexplained non-monotonic anomaly.
32	
33	    \item \textbf{We document method sensitivity as a primary finding} (\S\ref{sec:mmct}).
34	    Five methods yield null-control FPR from 7\% to 94\% ($\kappa{=}0.185$); PermG, the lowest-FPR method across all five (7.4\%, CI $[2.1\%, 17.9\%]$, 9~seeds), is selected as the primary detector.
35	
36	    \item \textbf{We empirically validate a cascade ordering for canary metric selection} (\S\ref{sec:cascade}).
37	    Under mode amplification, entropy responds before diversity by ${\geq}1$ generation (Principles~\ref{thm:entropy_leads}--\ref{prop:div_lag}), confirmed in 14/15 experiments ($\alpha \geq 0.30$; GPT-2-medium s43 bidirectional).
38	\end{enumerate}
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb5cbc8d-896d-413b-9ec2-9f241a002bbe",
  "isSidechain": true,
  "promptId": "51e3df65-9561-4454-8292-70ea3a87414d",
  "agentId": "aac173aafa6353ad3",
  "type": "user",
  "uuid": "d0fb7a6f-635b-49d5-a8f0-7a2f77182255",
  "sourceToolAssistantUUID": "eb5cbc8d-896d-413b-9ec2-9f241a002bbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T18:28:18.678Z_

<details open><summary>🔧 Tool call — Read · `toolu_017m9S4w9X6YYSWdhnjZzxp8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0fb7a6f-635b-49d5-a8f0-7a2f77182255",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsEpNZoN5nLGezEDMKM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4e20f613-ba24-474a-a6a4-283310a82255",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZGJvEMyUqGg1ExhqNTdqy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37449,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T18:28:18.690Z_

<details><summary>↩ Tool result · `toolu_017m9S4w9X6YYSWdhnjZzxp8`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Cascade Ordering}
5	\label{sec:cascade}
6	
7	If distributional collapse follows a predictable ordering across metrics, the earliest-responding metric can serve as a canary signal.
8	We formalize known metric properties---entropy as a continuous indicator of mode concentration, diversity as a threshold indicator of lexical coverage---under mode amplification~\cite{shumailov2024curse,dohmatob2024tale} (derivations in Appendix~\ref{app:cascade_theory}).
9	
10	\begin{designprinciple}[Entropy responds before diversity]\label{thm:entropy_leads}
11	Under mode amplification: \textup{(a)} entropy can decrease while the $\epsilon$-effective support $S_\epsilon(p) {=} |\{i: p_i > \epsilon\}|$ (hence distinct-$n$) is unchanged; \textup{(b)} if distinct-$n$ decreases, entropy has already decreased.
12	\end{designprinciple}
13	
14	The asymmetry arises because entropy responds to any mass redistribution (first-order), while diversity changes only when a token probability crosses the generation threshold~$\epsilon$; the margin $\gamma = \min_{i: p_i > \epsilon}(p_i - \epsilon)$ quantifies how much shift diversity absorbs silently.
15	
16	\begin{designprinciple}[Diversity lag $\geq 1$ generation]\label{prop:div_lag}
17	If the per-generation perturbation satisfies $\alpha\|\mathcal{T}(p_t) - p_t\|_\infty < \gamma(p_t, \epsilon)$ through entropy onset $t_H$, then diversity onset $t_D \geq t_H + 1$.
18	\end{designprinciple}
19	
20	ECE co-moves with entropy at zero lag: peakier conditionals simultaneously decrease per-token entropy and increase confidence ($\Delta\mathrm{ECE} \approx \Delta C > 0$ whenever $\Delta\bar{H} < 0$; qualitative argument in Appendix~\ref{app:cascade_theory}).
21	The predicted cascade $\{H, \mathrm{ECE}\} \to \mathrm{Distinct}$-$n$ holds in 14/15 experiments at $\alpha \geq 0.30$ (GPT-2-medium s43 bidirectional; within-domain WikiText, $2\sigma$ onset threshold): entropy and ECE onset at generation~1, distinct-$n$ at generation~2 ($t_H{=}t_{\mathrm{ECE}}{=}1$, $t_D{=}2$ uniformly; \S\ref{sec:regime}; Appendix~\ref{app:moment_cascade}).
22	Five low-$\alpha$ experiments show no detectable onset, leaving the ordering undefined below the detection threshold.
23	The assumption requires monotonic entropy decline; SmolLM3-3B (entropy 0/4; Table~\ref{tab:generalization}) provides an empirical counter-example, possibly due to architectural differences in attention or normalization.
24	This cascade establishes entropy as the earliest available canary and explains PermG's directional selectivity: forward tests detect temporal precedence (6/8) while reverse tests find none (0/8) at $\alpha \geq 0.50$.
25	
26	\subsection{Design Considerations and Method Sensitivity}
27	\label{sec:pitfalls}
28	\paragraph{Design considerations.}
29	We use Granger causality~\cite{granger1969investigating} to test temporal precedence---whether past canary values improve prediction of downstream metrics---not mechanistic causation; bivariate Granger tests cannot exclude confounders~\cite{shojaie2022granger}.
30	Lead-lag analysis in iterative model collapse is fragile along three axes, each documented with data from \S\ref{sec:regime}--\ref{sec:dose_response}.
31	\emph{Method sensitivity}: five detection methods applied to identical data yield forward significance rates spanning 0\% to 92\%, with inter-method agreement at $\kappa{=}0.185$.
32	\emph{Spurious regression}: first-differencing eliminates canary$\to$perplexity associations ($F{\approx}0$, $p{=}0.99$) while preserving canary$\to$diversity (24/24$\to$24/24), exposing an entire analysis channel as trend-driven~\cite{granger1974spurious}.
33	\emph{Regime dependence}: the same Granger test shifts from 0/8 to 6/8 significant pairs within a 2-percentage-point interval ($\alpha{=}0.48 \to 0.50$).
34	
35	\subsection{Method Sensitivity Analysis}
36	\label{sec:mmct}
37	We compare five lead-lag detection methods in a multi-method comparison~\cite{simonsohn2020specification} (algorithm in Appendix~\ref{app:mmct}), calibrated against null-control ($\alpha{=}0.0$) data where any detection is a false positive.
38	PermG's empirical FPR of 7.4\% (CI $[2.1\%, 17.9\%]$; 9 null seeds, 7/9 with 0~FP) exceeds the nominal 5\% threshold; $K{\geq}3$ consensus yields 11.1\% FPR (6/54), driven primarily by high-FPR methods (PermG contributes to only 2/6 consensus false positives; Appendix~\ref{app:fpr_independence}).
39	The five methods are: naive cross-correlation, differenced cross-correlation (DiffXCorr), threshold onset, permutation Granger causality (PermG), and Toda--Yamamoto~\cite{toda1995statistical}.
40	Detection results use equal-weight majority voting ($K{\geq}3$ of 5 methods, each contributing one vote per pair) with forward-direction filtering; FPR-inverse weighting is used only in exploratory method ranking (Appendix~\ref{app:weight_robustness}).
41	Each method encodes different assumptions, and these differences produce dramatically different FPR profiles.
42	Pooled null-control FPR across nine seeds (6-pair basis, 54 pairs): PermG 7.4\%, DiffXCorr 14.8\%, Threshold 24.1\%, Toda--Yamamoto 33.3\%, NaiveXCorr 94.4\% (Appendix~\ref{app:fpr_independence}).
43	We classify a method as \emph{directional} if its test structure inherently separates forward from reverse precedence (PermG tests each direction independently; threshold onset compares crossing order), rather than inferring direction post-hoc from peak lag sign (NaiveXCorr, DiffXCorr).
44	PermG (4/54, 7.4\%; 95\% CI $[2.1\%, 17.9\%]$) achieves the lowest FPR among all five methods, combining directional separation with consistent detection at $\alpha \geq 0.50$ across all four weighting schemes (Shapley analysis: Appendix~\ref{app:shapley}).
45	DiffXCorr (8/54, 14.8\%) is the next lowest but cannot distinguish forward from reverse precedence, making it unsuitable as a standalone collapse detector.
46	Practitioner-facing alternatives (PPL-slope, variance thresholds) yield 67--100\% FPR under natural training drift (Appendix~\ref{app:naive_baselines}).
47	That method choice alone can shift conclusions from universal significance to complete null on identical data motivates reporting method sensitivity as a primary result rather than relegating it to a robustness check.
48	
49	\paragraph{Permutation Granger causality.}
50	PermG tests whether past values of canary metric $X$ improve prediction of downstream metric $Y$ beyond $Y$'s own history~\cite{shojaie2022granger}.
51	We use classical rather than neural Granger methods~\citep{tank2021neural} because $T{\leq}25$ provides insufficient observations for neural network parameter estimation, and apply 5{,}000 permutations~\citep{phipson2010permutation} on first-differenced series with Benjamini--Hochberg FDR correction at $q{=}0.05$ across 8 canary$\to$downstream pairs (2 canaries $\times$ 4 downstream metrics, sharing canary terms and thus positively dependent).
52	
53	The permutation null controls Type~I error exactly by construction; BH-FDR remains valid under positive regression dependence on a subset (PRDS)~\cite{benjamini2001control} (assumption discussed in Appendix~\ref{app:fpr_independence}).
54	Empirically, 4/54 null-control rejections across nine seeds (7.4\%; 95\% CI $[2.1\%, 17.9\%]$; 7/9 seeds yield 0~FP, with seed-dependent hits in s45 and s50; Appendix~\ref{app:fpr_independence}) confirm adequate size control.
55	Simulation under non-stationary AR(1) DGP ($\varphi{=}0.95$--$0.99$) reveals potential FPR inflation to ${\sim}10\%$, but our empirical series exhibit low persistence (null token entropy $\varphi{=}-0.51$; first-differenced distinct-1 $\varphi{<}0.44$; Appendix~\ref{app:nonstationarity}).
56	PermG also retains ${\sim}80\%$ of raw-levels power at $T{=}11$ versus ${\sim}61\%$ for standard first-differencing, justifying the permutation approach at short series lengths (Appendices~\ref{app:robustness}, \ref{app:power_analysis}, \ref{app:transfer_entropy}).
57	
58	\paragraph{Consensus threshold.}
59	The choice of $K{=}3$ balances false positive control against detection power.
60	Lower $K$ increases sensitivity but admits more false positives from high-FPR methods; higher $K$ suppresses detection at boundary contamination levels where only 2--3 methods achieve significance.
61	Table~\ref{tab:mmct_k_operating} (\S\ref{sec:experiments}) presents the operating characteristics across $K \in \{2,3,4,5\}$: $K{=}3$ yields 11.1\% FPR with 75\% TPR at $\alpha{=}1.0$, while $K{=}4$ eliminates false positives but reduces TPR to ${\leq}25\%$.
62	
63	\subsection{Detection Boundary}
64	\label{sec:theory}
65	
66	We model the PermG detection rate as a $T$-dependent steep sigmoid, excluding the non-monotonic anomaly at $\alpha \in [0.55, 0.65]$:
67	\begin{equation}
68	\mathrm{rate}(\alpha, T) = \frac{0.70}{1 + \exp\!\bigl(-100\,(\alpha - \alpha_c(T))\bigr)},
69	\label{eq:joint-sigmoid}
70	\end{equation}
71	fitted to $T{=}10$ data ($n{=}11$, sync-dip excluded; $R^2{=}0.969$).
72	The detection boundary is consistent with power-law scaling in observation length:
73	\begin{equation}
74	\alpha_c(T) = A \cdot T^{-\gamma},
75	\label{eq:alpha-c}
76	\end{equation}
77	where the exponent $\gamma$ is determined by the sub-linear signal model below.
78	
79	\paragraph{Empirical observation (detection boundary).}\label{prop:phase-boundary}
80	Under an empirical sub-linear signal model $S(\alpha) = c \cdot \alpha^\beta$ with $\beta < 1$ (signal exponent, not statistical power), the detection boundary satisfies
81	\begin{equation}
82	\alpha_c(T) = A \cdot T^{-1/(2\beta)},
83	\label{eq:alpha-c-theory}
84	\end{equation}
85	where $A = (z^* \sigma / c)^{1/\beta}$ and $z^* = \Phi^{-1}(\pi^*)$ (justification in Appendix~\ref{app:alpha_c_proof}).
86	
87	\noindent The signal model $S(\alpha) = c\alpha^\beta$ is an empirical parametrization: $\beta$ is fitted from data rather than derived from training dynamics.
88	The power-law form $\alpha_c \propto T^{-1/(2\beta)}$ follows from signal-detection theory (signal-to-noise crossing a threshold), but $\beta$ requires architecture-specific calibration.
89	
90	Cross-$T$ validation (train $T{\in}\{10,20\}$, test $T{\in}\{5,15\}$) yields $\beta{=}0.24$, $\gamma{=}2.08$ (MAE${=}0.106$, CI $6/6$); leave-one-$T$-out CV on the full grid ($T{\in}\{5,10,15,20,25\}$, anomaly excluded) confirms predictive accuracy (MAE${=}0.037$, CI $15/15$; Appendix~\ref{app:alpha_c_proof}).
91	However, $\beta$ is poorly identified: the MLE center estimate $\hat{\beta}{=}0.66$ ($\gamma{\approx}0.76$) diverges from the cross-validation estimate $\beta{=}0.24$ ($\gamma{=}2.08$), with profile 95\% CI $\gamma \in [0.64, 2.08]$.
92	Under PermG's FPR uncertainty ($[2.1\%, 17.9\%]$), $\alpha_c$ estimates carry ${\pm}0.05$ uncertainty; statistical power at $T{\leq}8$ falls below 50\% (Appendix~\ref{app:power_analysis}), so reported boundaries at short $T$ are upper bounds.
93	The qualitative conclusion (detection improves with longer observation) is robust to the specific $\gamma$ value; the precise exponent is a descriptive parametrization rather than a mechanistic prediction.
94	
95	\paragraph{Shape comparison with smooth alternatives.}
96	The scaling exponent alone cannot distinguish smooth from steep-sigmoid boundaries: a concave signal model ($\beta'{=}0.5$) produces $\gamma'{=}1.87$, close to the observed $2.08$.
97	Formal shape testing on dense $T{=}10$ data (17~$\alpha$ values) favors a smooth sigmoid over a literal step function ($\Delta\mathrm{AIC}{=}-110$), but the fitted onset steepness ($k{=}15.7$, 95\% CI $[9.4, 28.2]$; \S\ref{sec:dose_response}) is $3$--$4{\times}$ higher than any smooth signal model predicts.
98	Power simulations confirm this gap: VAR(1) models (1{,}000 per cell; Appendix~\ref{app:power_sim}) produce sigmoids with $k{\approx}5$--$6$, yielding $k_{\mathrm{obs}} / k_{\mathrm{H0}} \approx 3$ (CI lower bound ratio ${\approx}2$), consistent with a genuine phase boundary rather than a gradual power artifact.
99	Since $\alpha_\infty{\approx}0$, any nonzero contamination produces signal ($S \propto \alpha^{0.24}$), but sub-linear growth makes detection a function of $T$.
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e20f613-ba24-474a-a6a4-283310a82255",
  "isSidechain": true,
  "promptId": "51e3df65-9561-4454-8292-70ea3a87414d",
  "agentId": "aac173aafa6353ad3",
  "type": "user",
  "uuid": "30b8fe46-1984-44f9-9f34-64332793ee7c",
  "sourceToolAssistantUUID": "4e20f613-ba24-474a-a6a4-283310a82255",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T18:28:18.888Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DjGzuXtzAWWg2peAeEUAuR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30b8fe46-1984-44f9-9f34-64332793ee7c",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsEpNZoN5nLGezEDMKM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c7dda5b4-e9aa-4d16-9e4c-5d76fe2ac2b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZGJvEMyUqGg1ExhqNTdqy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37449,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T18:28:18.895Z_

<details><summary>↩ Tool result · `toolu_01DjGzuXtzAWWg2peAeEUAuR`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We study the detectability landscape of iterative training collapse using Pythia-410M~\cite{biderman2023pythia} (410M parameters, decoder-only) as the primary architecture, with cross-architecture validation on five families (later verified in \S\ref{sec:generalization}).
8	Training data is drawn from WikiText-103~\cite{merity2017pointer} following the replace paradigm of~\citet{shumailov2024curse}: each generation fine-tunes on a mixture of $\alpha$ synthetic and $(1{-}\alpha)$ real data, generates 5{,}000 replacement samples, and fully replaces the synthetic pool (hyperparameters in Appendix~\ref{app:training_details}; notation in Appendix~\ref{app:background}).
9	We run $T{=}10$ generations across 13 contamination levels ($\alpha \in \{0.00, 0.05, 0.10, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.75, 1.00\}$, including null control) with multi-seed replication (4 seeds at $\alpha{=}1.0$; 3 at primary levels).
10	In total, the study comprises ${\sim}192$ iterative training runs across two model scales (410M, 1.4B), five detection methods, 13 contamination levels, three sequence lengths ($T \in \{10, 15, 20\}$), and up to four random seeds per condition, yielding ${\sim}1{,}500$ statistical tests after BH-FDR correction.
11	
12	We track two \emph{canary metrics} (token entropy and ECE) and three \emph{downstream metrics}: distinct-1, distinct-2~\cite{li2016diversity}, and perplexity (distinct-3: Appendix~\ref{app:distinct3}).
13	All hypothesis tests apply BH-FDR correction~\cite{benjamini1995controlling} at $q{=}0.05$; PermG uses 5{,}000 permutations on first-differenced series~\cite{shojaie2022granger} with maximum lag~5 (window sensitivity: Appendix~\ref{app:window_sensitivity}).
14	As in \S\ref{sec:method}, PermG tests temporal precedence, not causation.
15	
16	
17	\subsection{Sharp Detection Onset}
18	\label{sec:regime}
19	
20	Diversity collapse occurs at every contamination level: distinct-1 declines by $14.1\%$ even at $\alpha{=}0.0$ (fine-tuning drift) and by $40.3{\pm}0.3\%$ at $\alpha{=}0.25$ (3-seed mean).
21	Despite this ubiquitous degradation, Granger detectability is sharply regime-dependent.
22	PermG finds 0/8 canary$\to$downstream pairs FDR-significant from $\alpha{=}0.00$ through $\alpha{=}0.45$, then jumps to 6/8 (Clopper--Pearson 95\% CI $[0.25, 0.92]$) at $\alpha{=}0.50$, uniformly across all 3~fp32 seeds.
23	
24	This transition is striking because cumulative synthetic fraction barely changes across the boundary: $C = 1{-}(1{-}\alpha)^{10}$ yields $99.75\%$ at $\alpha{=}0.45$ versus $99.90\%$ at $\alpha{=}0.50$, a difference of 0.15 percentage points, yet detection jumps from null to reliable.
25	The onset reflects PermG's statistical power crossing the detection threshold, not the emergence of a new physical signal; sub-threshold $p$-values at $\alpha{=}0.45$ ($p_{\mathrm{fdr}} = 0.059$--$0.091$) confirm proximity to the boundary (\S\ref{sec:theory}).
26	Sigmoid regression on the 13-point $T{=}10$ grid yields $\alpha_c = 0.483 \pm 0.006$ ($R^2 = 0.969$; Figure~\ref{fig:hero}b); dense $\alpha$ sampling (17~values) constrains onset steepness to $k{=}15.7$ (95\% CI $[9.4, 28.2]$), a steep but finite-width sigmoid ($\Delta\mathrm{AIC}{=}-110$ vs.\ step function; Appendix~\ref{app:sigmoid_shape}).
27	This steepness (${\approx}3{\times}$ smooth-model predictions; \S\ref{sec:theory}) and cross-seed consistency (3/3 seeds: $0/8{\to}6/8$) argue for a genuine, power-modulated transition rather than a statistical artifact (Fisher exact: $p = 3.45 \times 10^{-11}$; specification-invariance across 1{,}160 configurations in Appendix~\ref{app:spec_curve}).
28	
29	\paragraph{Canary scoping.}
30	First-differencing scopes the canary claim precisely.
31	Canary$\to$diversity pairs retain unanimous FDR significance after first-differencing ($24/24 \to 24/24$ across 4~seeds at $\alpha{=}1.0$, 6 per seed), while canary$\to$perplexity collapses entirely ($F \approx 0$, $p = 0.99$): the apparent perplexity association is a shared-trend artifact~\cite{granger1974spurious}.
32	All canary claims are therefore scoped to diversity metrics only.
33	This scoping reflects a genuine temporal structure difference: canary$\to$diversity correlations peak at lagged offsets (81\% at lag${<}0$), while canary$\to$perplexity correlations are contemporaneous (Appendix~\ref{app:channel_effect_size}).
34	At $\alpha{=}1.0$, all 24 canary$\to$diversity pairs reach FDR significance in the forward direction with 0/24 reverse; entropy onset at generation~1 precedes distinct-$n$ at generation~2 in 16/18 WikiText conditions (\S\ref{sec:cascade}, Appendix~\ref{app:moment_cascade}).
35	
36	\paragraph{Blind zone.}
37	The canary mechanism has a fundamental limitation: at $\alpha{=}0.10$, distinct-1 has already dropped by $39.6\%$, yet token entropy is indistinguishable from the null ($-5.3\%$ versus $-4.6{\pm}0.4\%$ at $\alpha{=}0.0$).
38	The gen-1 entropy deviation spans three orders of magnitude across the $\alpha$ range ($0.5\sigma$ at $\alpha{=}0.10$ to $60\sigma$ at $\alpha{=}0.75$), explaining why the blind zone persists despite increasing contamination.\footnote{Seed~43 at $\alpha{=}0.10$ shows 3/8 versus 0/8 for seed~42; no other sub-threshold level exhibits seed-dependent detection.}
39	Below $\alpha_c$ at $T{=}10$, diversity collapse proceeds without any detectable Granger-precedence signal, though Gaussian MI remains positive (Appendix~\ref{app:mi_analysis}).
40	
41	\begin{figure}[t]
42	\centering
43	\includegraphics[width=\columnwidth]{figures/metric_trajectory.pdf}
44	\caption{Metric trajectories at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead across all four seeds (shaded: inter-seed range). This pattern corresponds to 24/24 forward and 0/24 reverse FDR-significant canary$\to$diversity pairs (6 per seed, mauve excluded).}
45	\label{fig:metric_trajectory}
46	\end{figure}
47	
48	
49	\subsection{Dose-Response and Detection Regimes}
50	\label{sec:dose_response}
51	
52	The PermG dose-response profile (Figure~\ref{fig:hero}b; full per-method table in Appendix~\ref{app:dose_response}) reveals three confirmed detection regimes---\emph{blind} ($\alpha \leq 0.45$, 0/8 FDR-significant pairs), \emph{onset} ($\alpha \approx 0.50$, 6/8), and \emph{detection} ($\alpha{\geq}0.75$, 6/8 across 4~seeds at $\alpha{=}1.0$)---plus a non-monotonic anomaly at $\alpha \approx 0.60$ (0/8) whose mechanism remains unexplained.
53	At $\alpha{=}0.55$, PermG returns 0/8 FDR-significant pairs despite marginal $p$-values ($p_{\mathrm{fdr}}{=}0.062$--$0.092$); differenced cross-correlation detects 8/8 forward pairs at this level (0/8 reverse), confirming that a lead-lag signal exists but falls below PermG's directional detection threshold.
54	At $\alpha{=}0.60$, PermG returns $0/8$ at $T{\leq}20$ but recovers to $5/8$ at $T{=}25$, consistent with $\sqrt{T}$ power scaling (Appendix~\ref{app:t20_comparison}).
55	Notably, $K{\geq}3$ consensus also returns 0/8 at $\alpha{=}0.60$: all direction-checked methods fail at this level (PermG 0/8, threshold onset 0/8, Toda--Yamamoto 1/8), while bidirectional DiffXCorr maintains detection (6/8 forward).
56	This suggests the anomaly reflects compressed temporal lag---canary and downstream respond within the same generation---disrupting all methods that require directional separation.
57	
58	Method choice is itself a major source of variability: at $\alpha{=}1.0$, direction-checked forward significance spans 0\% to 75\% (Figure~\ref{fig:hero}c), with $\kappa{=}0.185$; a specification curve (18~variants; Appendix~\ref{app:spec_curve}) confirms onset invariance.
59	Task degradation corroborates: perplexity jumps $+31\%$ between $\alpha{=}0.50$ and $0.52$ (Appendix~\ref{app:task_degradation}).
60	
61	
62	\subsection{Detection Boundary Left-Shift}
63	\label{sec:t20}
64	
65	Longer observation windows push the detection boundary to lower contamination levels: $\alpha_c(5){\geq}1.0$, $\alpha_c(10){=}0.487$, consistent with power-law scaling (\S\ref{sec:theory}).
66	The $\alpha{=}0.45$ column validates this left-shift: undetectable at $T{\leq}10$ (0/8), it crosses into reliable detection at $T{=}15$ (6/8, dual-seed) and remains there at $T{=}20$ and $T{=}25$.
67	Cross-seed replication shows PermG within ${\pm}1$, though boundary cells exhibit sensitivity ($[0, 6]/8$ at $T{=}10$, $\alpha{=}0.50$).
68	The $\alpha{=}0.60$ anomaly dissolves by $T{=}25$ ($5/8$), consistent with $\sqrt{T}$ power scaling; predict-then-verify yields 2/4 boundary predictions within CI (Appendix~\ref{app:t20_prediction_timeline}).
69	
70	
71	\subsection{Cross-Architecture Validation}
72	\label{sec:generalization}
73	
74	To test whether the phase-diagram structure is Pythia-specific, we evaluate PermG at $\alpha{=}1.0$ across 15 model-seed combinations spanning five families, scales 345M--6.9B, and two domains (Table~\ref{tab:generalization}).
75	Forward detection reaches ${\geq}6/8$ in 11/15 conditions, confirming that PermG generalizes to architectures satisfying the monotonic entropy decline assumption (Principle~\ref{thm:entropy_leads}).
76	Domain matters: C4 yields the strongest detection (Pythia-1.4B: 2/8 WikiText $\to$ 8/8 C4), suggesting that domain-specific mode structure affects detectability.
77	The four non-confirming conditions each isolate a distinct failure mode: precision sensitivity (GPT-2 bf16: 0/8 vs fp32: 6/8), bidirectional confounding (GPT-2 s43), seed dependence (Pythia-1.4B: s42 2/8, s43 6/8), and entropy decoupling (SmolLM3-3B: 3/8, whose non-monotonic entropy violates Principle~\ref{thm:entropy_leads}).
78	
79	\paragraph{FPR caveat.}
80	GPT-2-medium null-control (s42) yields 6/6 PermG forward false positives, an architecture-specific FPR inflation likely driven by its non-standard weight initialization.
81	While $K{\geq}3$ consensus returns 0/6 on GPT-2 null specifically, its overall FPR on Pythia-410M is 11.1\% (6/54; \S\ref{sec:mmct})---higher than standalone PermG---so consensus serves as a robustness mechanism against single-method anomalies rather than a general FPR safety net.
82	Standalone PermG claims require architecture-specific null calibration.
83	
84	Full results are in Table~\ref{tab:generalization} (Appendix~\ref{app:cross_arch_table}).
85	
86	
87	\subsection{Canary-Based Intervention (Proof of Concept)}
88	\label{sec:intervention}
89	
90	As an illustrative proof-of-concept under favorable conditions ($\alpha{=}1.0$, full replacement), we implement predictive cessation: training switches to pure real data when token entropy drops ${>}15\%$ from generation~0.
91	The 15\% threshold was selected post-hoc (robust band $[10\%, 22\%]$, zero false alarms; Appendix~\ref{app:intervention_sensitivity}).
92	The predictive trigger fires at generation~1 (one generation before a reactive distinct-1 baseline), reducing peak perplexity by 64\% ($56.99$ vs.\ $157.09$; Figure~\ref{fig:intervention}) in both Pythia-410M and 1.4B.
93	This single-setting demonstration ($N{=}2$ architectures, $\alpha{=}1.0$, post-hoc threshold) is not rigorously evaluated (CUSUM comparison: Appendix~\ref{app:csmp}).
94	
95	\begin{figure}[t]
96	\centering
97	\includegraphics[width=\columnwidth]{figures/fig_intervention.pdf}
98	\caption{Canary-triggered intervention (Pythia-410M, $\alpha{=}1.0$). Predictive cessation on entropy (generation~1) reduces peak perplexity by 64\% versus reactive triggering on distinct-1 (generation~2).}
99	\label{fig:intervention}
100	\end{figure}
101	
102	\begin{table}[t]
103	\centering
104	\caption{Summary of detection outcomes across contamination levels (Pythia-410M, seed~42, $T{=}10$, fp32). PermG: forward FDR-significant pairs; $K{\geq}3$: consensus pairs (of 8 canary$\to$downstream pairs).}
105	\label{tab:summary_detection}
106	\begin{tabular}{@{}lccc@{}}
107	\toprule
108	$\alpha$ & PermG & $K{\geq}3$ & Regime \\
109	\midrule
110	0.00 & 0/8 & 0/8 & null \\
111	0.25 & 0/8 & 0/8 & blind \\
112	0.45 & 0/8 & 0/8 & blind \\
113	0.50 & 6/8 & 6/8 & onset \\
114	0.60 & 0/8 & 0/8 & anomaly \\
115	0.75 & 6/8 & 6/8 & detection \\
116	1.00 & 6/8 & 6/8 & detection \\
117	\bottomrule
118	\end{tabular}
119	\end{table}
120	
121	\begin{table}[t]
122	\centering
123	\caption{Consensus threshold operating characteristics ($K \in \{2,3,4,5\}$). FPR: null-control rate (9 seeds, 54 pairs); TPR: detection rate at selected $\alpha$ levels (Pythia-410M, $T{=}10$, fp32). $K{=}3$ balances FPR control (11.1\%) against detection power (75\% at $\alpha{=}1.0$); $K{=}4$ eliminates false positives but reduces TPR to ${\leq}25\%$.}
124	\label{tab:mmct_k_operating}
125	\begin{tabular}{@{}lcccc@{}}
126	\toprule
127	& $K{\geq}2$ & $K{\geq}3$ & $K{\geq}4$ & $K{=}5$ \\
128	\midrule
129	FPR ($\alpha{=}0.0$) & 38.9\% & 11.1\% & 0\% & 0\% \\
130	TPR ($\alpha{=}0.50$) & 85.4\% & 66.7\% & 25.0\% & 4.2\% \\
131	TPR ($\alpha{=}0.75$) & 72.9\% & 37.5\% & 0\% & 0\% \\
132	TPR ($\alpha{=}1.0$) & 75.0\% & 75.0\% & 25.0\% & 0\% \\
133	\bottomrule
134	\end{tabular}
135	\end{table}
136	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7dda5b4-e9aa-4d16-9e4c-5d76fe2ac2b4",
  "isSidechain": true,
  "promptId": "51e3df65-9561-4454-8292-70ea3a87414d",
  "agentId": "aac173aafa6353ad3",
  "type": "user",
  "uuid": "adc2bdd7-61b5-4dd2-b0f4-85b9436b8d0d",
  "sourceToolAssistantUUID": "c7dda5b4-e9aa-4d16-9e4c-5d76fe2ac2b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T18:28:19.100Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TjBtnryDC1718RdbjgUcwK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adc2bdd7-61b5-4dd2-b0f4-85b9436b8d0d",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsEpNZoN5nLGezEDMKM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1fcbfcc6-2637-4d4c-a033-c92b86944f5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZGJvEMyUqGg1ExhqNTdqy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37449,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T18:28:19.108Z_

<details><summary>↩ Tool result · `toolu_01TjBtnryDC1718RdbjgUcwK`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:discussion}
2	
3	\paragraph{Scope and failure modes.}
4	Our Granger-precedence claim is scoped to temporal predictive improvement~\cite{granger1969investigating,shojaie2022granger}: bivariate tests cannot exclude confounders, and the FPR CI ($[2.1\%, 17.9\%]$) means Type~I error may be non-negligible.
5	Entropy's greater sensitivity to distributional shifts than $n$-gram diversity means the temporal lead may partly reflect measurement sensitivity rather than a causal cascade.
6	Four of fifteen cross-architecture conditions do not confirm forward detection (\S\ref{sec:generalization}), each violating one PermG assumption: precision sensitivity (GPT-2 bf16), seed dependence (Pythia-1.4B), and entropy decoupling (SmolLM3-3B, where non-monotonic entropy breaks the cascade ordering entirely).
7	These patterns require verifying monotonic entropy response and architecture-specific null calibration (GPT-2 standalone FPR: 50\%) before deployment (Appendix~\ref{app:extended_discussion}).
8	
9	\paragraph{Granger causality limitations.}
10	Our permutation Granger tests inherit fundamental constraints of the framework~\citep{shojaie2022granger}.
11	First, our observation sequences ($T{=}10$--$25$) are far shorter than the $T{\geq}100$ standard in econometric applications; permutation testing avoids asymptotic distributional assumptions but cannot recover statistical power lost to short samples.
12	Second, bivariate Granger precedence is susceptible to omitted variable bias: an unobserved confounder could drive both canary entropy and downstream diversity simultaneously.
13	First-differencing removes shared linear trends, but nonlinear confounds remain possible.
14	Third, PermG tests linear temporal precedence only; nonlinear dependencies go undetected.
15	Transfer entropy (Appendix~\ref{app:transfer_entropy}), which captures arbitrary-order dependencies, yields 0/192 significant pairs after FDR correction, consistent with either genuine absence of nonlinear structure or insufficient power in the short-$T$ regime.
16	These limitations parallel challenges in ecological early-warning detection~\citep{dakos2008slowing,lenton2008tipping}, where short observational windows similarly constrain tipping-point forecasts.
17	Partial correlation analysis controlling for generation number confirms that the canary$\to$diversity lag-one structure persists---and strengthens---after trend removal (35/36 detection-condition pairs significant; Appendix~\ref{app:partial_corr}).
18	
19	\paragraph{The $\alpha{=}0.60$ non-monotonic anomaly.}
20	The detection gap at $\alpha{=}0.60$ affects all direction-checked methods, not only PermG: at $T{=}10$, PermG returns 0/8, threshold onset 0/8, Toda--Yamamoto 1/8, and $K{\geq}3$ consensus 0/8.
21	Only bidirectional DiffXCorr maintains detection (6/8 forward), suggesting that a lead-lag signal exists but its temporal structure defeats directional separation.
22	The mechanism is consistent with relaxation-time compression: at $\alpha \approx 0.60$, contamination drives entropy and diversity responses into the same generation, collapsing the temporal offset that directional methods require.
23	PermG recovers to 5/8 at $T{=}25$, consistent with $\sqrt{T}$ power scaling restoring detection as additional observations disambiguate synchronous from lagged responses.
24	Boundary experiments at $\alpha{=}0.55$ and $\alpha{=}0.65$ will characterize the width of this anomaly and test whether the dip is a point phenomenon or spans a finite interval.
25	
26	\paragraph{Conclusion.}
27	Method choice alone shifts null-control FPR from 7.4\% to 94.4\%, establishing that single-method analyses cannot reliably distinguish temporal precedence from artifacts.
28	PermG, the lowest-FPR method (7.4\%, 9~seeds), yields token entropy one-generation-ahead precedence over diversity collapse (24/24 forward, 0/24 reverse at $\alpha{=}1.0$; ${\geq}6/8$ in 11/15 cross-architecture conditions).
29	The blind zone below $\alpha_c$ constrains practical deployment to settings with sufficient contamination; evaluation at ${>}$7B parameters remains open.
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1fcbfcc6-2637-4d4c-a033-c92b86944f5c",
  "isSidechain": true,
  "promptId": "51e3df65-9561-4454-8292-70ea3a87414d",
  "agentId": "aac173aafa6353ad3",
  "type": "user",
  "uuid": "e2d52a01-cecc-45cd-91cb-08e188533be8",
  "sourceToolAssistantUUID": "1fcbfcc6-2637-4d4c-a033-c92b86944f5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T18:28:19.311Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JvwtLp22cmFLToiFnm5RqV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2d52a01-cecc-45cd-91cb-08e188533be8",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsEpNZoN5nLGezEDMKM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "556779ff-47a6-4549-b955-1d9acc3ca39c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZGJvEMyUqGg1ExhqNTdqy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37449,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T18:28:19.318Z_

<details><summary>↩ Tool result · `toolu_01JvwtLp22cmFLToiFnm5RqV`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Lead-lag analysis in iterative training collapse is far more fragile than the current literature assumes.
5	Method choice alone inflates spurious-signal rates to at least 62.5\%, first-differencing exposes canary$\to$perplexity associations as entirely spurious, and regime dependence causes the same Granger test to shift from 24/24 to 0/8 significant pairs across contamination levels.
6	These design considerations establish that single-method, single-regime analyses (the current default) cannot reliably distinguish genuine temporal precedence from statistical artifacts.
7	
8	Our systematic five-method comparison through the Multi-Method Consensus Test (MMCT) identifies permutation Granger causality as the recommended detection method: it combines the lowest null-control FPR among all five methods (7.4\%, 4/54 across 9 seeds; 7/9 seeds yield 0~FP) with high sensitivity, exhibiting a steep dose-response onset from 0/8 (blind spot, $\alpha{\leq}0.45$) to 6/8 ($\alpha{=}0.50$; sigmoid $k{=}15.7$, ${\approx}3{\times}$ steeper than smooth-signal predictions) with reliable detection at $\alpha{\geq}0.75$.
9	The other four methods each fail in characteristic ways: naive cross-correlation inflates FPR to 75\%, differenced cross-correlation cannot separate forward from reverse precedence, threshold onset is power-limited at $T{=}10$ under $3\sigma$ calibration, and Toda--Yamamoto Granger provides supplementary detection at reduced power (directional assignment under verification).
10	
11	Applying permutation Granger, token entropy exhibits robust one-generation-ahead precedence over diversity collapse at $\alpha{=}1.0$ on WikiText-103 (24/24 forward, 0/24 reverse across 4~seeds, replicated on GPT-2-medium and OPT-1.3B), with cross-architecture validation confirming forward detection (${\geq}6/8$) in 11 of 15 model-seed combinations spanning five families (345M--6.9B); non-confirming conditions span precision sensitivity (GPT-2 bf16), seed dependence (Pythia-1.4B), entropy decoupling (SmolLM3), and bidirectional confounding (GPT-2 s43).
12	Directional asymmetry is domain-dependent: consistent unidirectionality holds on WikiText across all regimes, while C4 exhibits near-symmetric bidirectional coupling at $\alpha{=}0.50$ (PermG reverse 7/8), though forward detection remains robust in both domains.
13	This finding is deliberately scoped to lexical diversity, not model collapse broadly, since the perplexity channel proved entirely spurious under differencing.
14	
15	The design considerations we expose arise from generic properties of short, non-stationary time series.
16	Cross-architecture (five families, 345M--6.9B), cross-scale ($3.4\times$ within Pythia), and cross-domain (C4) validation confirms that both the design considerations and the method recommendation are not specific to a single experimental configuration; evaluation on models at ${>}$7B parameters remains an open direction.
17	Limitations are detailed in \S\ref{sec:limitations}; future directions are discussed in \S\ref{sec:discussion}.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "556779ff-47a6-4549-b955-1d9acc3ca39c",
  "isSidechain": true,
  "promptId": "51e3df65-9561-4454-8292-70ea3a87414d",
  "agentId": "aac173aafa6353ad3",
  "type": "user",
  "uuid": "d8180fbb-8445-40cb-8f6c-1c07f4ab71d2",
  "sourceToolAssistantUUID": "556779ff-47a6-4549-b955-1d9acc3ca39c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T18:28:19.731Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L31RK61wR2Fs4FmnpZ851N`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8180fbb-8445-40cb-8f6c-1c07f4ab71d2",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsEpNZoN5nLGezEDMKM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b20fadf4-f40d-4039-a81e-b145e3338d15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZGJvEMyUqGg1ExhqNTdqy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37449,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T18:28:19.740Z_

<details><summary>↩ Tool result · `toolu_01L31RK61wR2Fs4FmnpZ851N`</summary>

```text
1	\section*{Limitations}
2	\label{sec:limitations}
3	
4	Our landscape characterization uses Pythia-410M as the primary architecture; the phase diagram is Pythia-family-only, frontier-scale behavior (${>}$7B) is untested, and cross-architecture evaluation is limited to $\alpha{=}1.0$.
5	PermG's empirical FPR is 7.4\% (CI $[2.1\%, 17.9\%]$) and $K{\geq}3$ consensus yields 11.1\% (6/54); per-condition detection rates carry wide binomial CIs (e.g., $[0.25, 0.92]$ for 6/8), so the phase diagram represents a coarse topology rather than precise probability estimates.
6	All experiments use full replacement with a single decoding strategy (temperature~$1.0$, top-$k{=}50$); data accumulation~\cite{dey2024breaking} or lower temperatures would shift the landscape.
7	Permutation Granger testing establishes temporal precedence, not causation; our short-sequence regime ($T{\leq}25$) limits statistical power relative to econometric standards ($T{\geq}100$), and nonlinear alternatives to the linear PermG test yield no significant results in our setting (see \S\ref{sec:discussion}).
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b20fadf4-f40d-4039-a81e-b145e3338d15",
  "isSidechain": true,
  "promptId": "51e3df65-9561-4454-8292-70ea3a87414d",
  "agentId": "aac173aafa6353ad3",
  "type": "user",
  "uuid": "191bf408-da4a-472e-a5c7-5ba206fbc422",
  "sourceToolAssistantUUID": "b20fadf4-f40d-4039-a81e-b145e3338d15",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T18:28:19.807Z_

<details open><summary>🔧 Tool call — Read · `toolu_011XSPQaien7es16M1GD65Bc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "191bf408-da4a-472e-a5c7-5ba206fbc422",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsEpNZoN5nLGezEDMKM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "381959d3-86b9-4ec9-8446-230136a9498f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZGJvEMyUqGg1ExhqNTdqy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 37449,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 37449,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T18:28:20.160Z_

<details><summary>↩ Tool result · reported error · `toolu_011XSPQaien7es16M1GD65Bc`</summary>

```text
File content (38499 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "381959d3-86b9-4ec9-8446-230136a9498f",
  "isSidechain": true,
  "promptId": "51e3df65-9561-4454-8292-70ea3a87414d",
  "agentId": "aac173aafa6353ad3",
  "type": "user",
  "uuid": "6b162360-ab0d-4cd5-b00f-2d95ca3d9fba",
  "toolUseResult": "Error: File content (38499 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "381959d3-86b9-4ec9-8446-230136a9498f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-24T18:28:21.858Z_

The appendix file is too large. Let me read it in sections:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b162360-ab0d-4cd5-b00f-2d95ca3d9fba",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsF7NGRGfxdHvJV7V22",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ce6fcda7-cd1b-46b2-a69b-231efa8110ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0187qAhvzuqnKF4HgC5Zoxy4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 15054,
      "cache_read_input_tokens": 37449,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15054,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-24T18:28:22.622Z_

<details open><summary>🔧 Tool call — Read · `toolu_0169NJxnDCEoGXPfgqgkAG8m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce6fcda7-cd1b-46b2-a69b-231efa8110ac",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsF7NGRGfxdHvJV7V22",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "364294fe-6f1f-4912-91cd-2c39ec6108dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0187qAhvzuqnKF4HgC5Zoxy4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 15054,
      "cache_read_input_tokens": 37449,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15054
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 123,
          "cache_read_input_tokens": 37449,
          "cache_creation_input_tokens": 15054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15054,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-24T18:28:22.915Z_

<details><summary>↩ Tool result · `toolu_0169NJxnDCEoGXPfgqgkAG8m`</summary>

```text
1	\appendix
2	
3	\section{Training Details and Metric Drift}
4	\label{app:training_details}
5	\label{app:drift}
6	
7	\paragraph{Hyperparameters.}
8	Each generation fine-tunes for 5{,}000 steps using AdamW (learning rate $5 \times 10^{-5}$, 500 warmup steps, weight decay $0.01$, batch size 4 for Pythia-410M, 32 for GPT-2-medium).
9	Generation uses temperature $1.0$, top-$k{=}50$, max length 512 tokens, producing 5{,}000 samples per generation from 5{,}000-sample subsets of WikiText-103.
10	Canary metrics: token entropy $H(p_\theta | \text{context})$ over 1{,}000 held-out samples; ECE with 15 bins.
11	Additional downstream metrics (distinct-3, effective rank, Self-BLEU) appear in subsequent appendix sections.
12	
13	\paragraph{Metric drift.}
14	
15	\begin{table}[h]
16	\centering
17	\small
18	\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
19	\label{tab:drift_summary}
20	\resizebox{\columnwidth}{!}{%
21	\begin{tabular}{lccccc}
22	\toprule
23	$\alpha$ & Entropy & ECE & Distinct-1 & Distinct-2 & Perplexity \\
24	\midrule
25	0.00 & $-4.6{\pm}0.4$ & $+37.6{\pm}14$ & $-14.1{\pm}0.4$ & $-9.6{\pm}0.4$ & $-20.6{\pm}1.0$ \\
26	0.10$^\dagger$ & $-5.3$ & $+57$ & $-39.6$ & $-56.4$ & $-21.0$ \\
27	0.25 & $-4.7{\pm}0.5$ & $+81.8{\pm}15.9$ & $-40.3{\pm}0.3$ & $-56.4{\pm}0.7$ & $-18.1{\pm}0.8$ \\
28	0.50 & $-18.0{\pm}0.5$ & $+822.6{\pm}18.3$ & $-37.1{\pm}0.4$ & $-50.4{\pm}1.0$ & $+21.0{\pm}0.1$ \\
29	0.75 & $-27.6{\pm}0.2$ & $+1791{\pm}18$ & $-32.3{\pm}0.5$ & $-41.0{\pm}1.0$ & $+182.6{\pm}0.7$ \\
30	1.00 & $-60.8{\pm}1.2$ & $+3780{\pm}30$ & $-27.8{\pm}1.6$ & $-34.0{\pm}3.3$ & $+3674{\pm}45$ \\
31	\bottomrule
32	\end{tabular}}
33	\end{table}
34	
35	
36	\section{Distinct-3 Results}
37	\label{app:distinct3}
38	
39	Table~\ref{tab:distinct3_drift} reports distinct-3 drift across all contamination levels.
40	Distinct-3 exhibits the largest absolute decline among diversity metrics at low contamination ($-58.9{\pm}0.9\%$ at $\alpha{=}0.25$) but attenuates at higher levels ($-30.5\%$ at $\alpha{=}1.0$), consistent with the diversity--calibration dissociation discussed in \S\ref{sec:discussion}.
41	
42	\begin{table}[h]
43	\centering
44	\small
45	\caption{Distinct-3 drift (\%, generation~0$\to$10) across contamination levels. $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.75$: 3-seed mean${\pm}$std; $\alpha{=}1.0$: 4-seed mean${\pm}$std; $\alpha{=}0.50$: single seed.}
46	\label{tab:distinct3_drift}
47	\begin{tabular}{lc}
48	\toprule
49	$\alpha$ & Distinct-3 drift (\%) \\
50	\midrule
51	0.00 & $-4.4{\pm}0.5$ \\
52	0.25 & $-58.9{\pm}0.9$ \\
53	0.50 & $-52.4$ \\
54	0.75 & $-38.6{\pm}1.3$ \\
55	1.00 & $-30.5{\pm}4.0$ \\
56	\bottomrule
57	\end{tabular}
58	\end{table}
59	
60	\paragraph{Lead-lag analysis.}
61	At $\alpha{=}1.0$, token entropy Granger-precedes distinct-3 at the same consensus level as distinct-1 and distinct-2: $K{\geq}4/5$ methods, $S{\geq}3/4$ seeds (Tier~3).
62	However, the optimal lag is less stable than for distinct-1/2: at max\_lag${=}7$, the lag standard deviation across seeds exceeds 1.5 generations, compared to $<0.5$ for distinct-1/2.
63	This instability reflects bimodal lag distributions (modes at lag~1 and lag~3--4), suggesting that distinct-3 captures two temporally distinct diversity loss mechanisms: rapid n-gram homogenization (lag~1) and slower distributional narrowing (lag~3--4).
64	
65	\paragraph{Sensitivity to sequence length.}
66	Higher-order $n$-gram diversity metrics are more sensitive to generation length and random sampling variability.
67	With our 512-token generation length, distinct-3 has a smaller effective denominator (number of possible unique trigrams observed) than distinct-1 or distinct-2, amplifying stochastic fluctuations.
68	This partially explains the higher lag instability: the signal-to-noise ratio for temporal precedence is lower for distinct-3, requiring more observations (longer $T$ or more seeds) to achieve stable estimates.
69	For this reason, we report distinct-3 in this appendix rather than in the main text, where distinct-1 and distinct-2 provide cleaner evidence of the entropy-leads-diversity pattern.
70	
71	
72	\section{Observation Window Sensitivity}
73	\label{app:window_sensitivity}
74	
75	Table~\ref{tab:window_sensitivity} reports how the Tier~3 consensus classification ($K{\geq}4/5$ methods) varies as a function of the minimum observation window $T_{\min}$, where analysis uses only generations $0$ through $T_{\min}$.
76	The consensus classification stabilizes at $T_{\min}{\geq}5$ (6 data points), well below our full observation window of $T{=}10$: all six effect-size reference pairs (token entropy and ECE $\to$ distinct-1, distinct-2, distinct-3) reach $K{\geq}4/5$ agreement at every window length from $T_{\min}{=}5$ through $T_{\min}{=}10$, with no spurious pairs (canary$\to$perplexity) admitted.
77	
78	Toda--Yamamoto is the only method exhibiting window-dependent sensitivity (note: TY directional assignment is under verification; these counts are retained for completeness): TY consensus stabilizes at $T_{\min}{\geq}6$, slightly later than the primary methods, reflecting the additional degrees of freedom consumed by the augmentation order $d_{\max}$.
79	This does not affect the consensus classification because the remaining four methods provide stable $K{\geq}4/5$ agreement independently of Toda--Yamamoto's vote.
80	
81	\begin{table}[h]
82	\centering
83	\small
84	\caption{Observation window sensitivity for Tier~3 consensus ($K{\geq}4/5$) at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Tier~3 pairs: number of canary$\to$downstream pairs (out of 8 validated) reaching $K{\geq}4/5$ method agreement. TY pairs: number of effect-size reference pairs (out of 6) reaching Toda--Yamamoto significance (moderate supplementary method; \S\ref{sec:method}). Consensus stabilizes at $T_{\min}{\geq}5$; TY stabilizes at $T_{\min}{\geq}6$.}
85	\label{tab:window_sensitivity}
86	\resizebox{\columnwidth}{!}{%
87	\begin{tabular}{lccccccccc}
88	\toprule
89	& \multicolumn{8}{c}{Minimum observation window $T_{\min}$} \\
90	\cmidrule(lr){2-9}
91	& 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
92	\midrule
93	Tier~3 pairs (/8)    & $\dagger$ & $\dagger$ & 6 & 6 & 6 & 6 & 6 & 6 \\
94	TY pairs$^\S$ (/6)   & $\dagger$ & $\dagger$ & 3--6 & 3--6 & 3--6 & 3--6 & 3--6 & 6 \\
95	Stable               & ---       & ---       & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark \\
96	\bottomrule
97	\multicolumn{9}{l}{\footnotesize $\dagger$~Insufficient degrees of freedom for Granger-type tests ($<6$ data points).} \\
98	\multicolumn{9}{l}{\footnotesize $^\S$~TY directional assignment under verification.}
99	\end{tabular}}
100	\end{table}
101	
102	\begin{figure}[h]
103	\centering
104	\includegraphics[width=\columnwidth]{figures/fig_window_sensitivity.pdf}
105	\caption{Consensus stability across minimum observation windows $T_{\min} \in \{5, \ldots, 10\}$. Left: $K{\geq}3$ consensus count at $\alpha{=}0.75$ (3 seeds). Right: per-method detection count across $T_{\min}$. Consensus stabilises at $T_{\min}{=}5$, confirming that the 10-generation default provides ample statistical power.}
106	\label{fig:window_sensitivity}
107	\end{figure}
108	
109	\section{Robustness Checks}
110	\label{app:robustness}
111	
112	\paragraph{Permutation count stability.}
113	Table~\ref{tab:nperm_stability} compares permutation Granger $p$-values at 5{,}000 versus 10{,}000 permutations across all canary$\to$downstream pairs at $\alpha{=}0.75$ (3~seeds, 24~pairs).
114	Permutation Granger $p$-values are stable to within 0.002 between 5{,}000 and 10{,}000 permutations, with zero significance decisions affected.
115	
116	\begin{table}[h]
117	\centering
118	\small
119	\caption{Permutation count stability analysis ($\alpha{=}0.75$, 3~seeds, 24 canary$\to$downstream pairs). $p$-values from permutation Granger tests at $n_{\text{perm}}{=}5{,}000$ versus $n_{\text{perm}}{=}10{,}000$.}
120	\label{tab:nperm_stability}
121	\begin{tabular}{lc}
122	\toprule
123	Metric & Value \\
124	\midrule
125	Max $|\Delta p|$ & 0.010 \\
126	Mean $|\Delta p|$ & 0.002 \\
127	Significance flips & 0 / 24 \\
128	\bottomrule
129	\end{tabular}
130	\end{table}
131	
132	\paragraph{FDR threshold sensitivity.}
133	Table~\ref{tab:fdr_sensitivity} reports the effect of varying the BH FDR threshold $q$ on treatment ($\alpha{=}0.75$, 3~seeds, 8-pair basis) versus null ($\alpha{=}0.0$, 6~seeds 45--50, 6-pair basis) separation for permutation Granger tests.
134	Treatment/null separation is qualitatively robust to FDR threshold choice, though the expanded null sample reveals a small number of false positives at each threshold (3--8 of 36 pairs).
135	
136	\begin{table}[h]
137	\centering
138	\small
139	\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs, 8-pair basis). Null: $\alpha{=}0.0$ (6 of 9 null seeds, seeds 45--50, 36 pairs, 6-pair basis; the full 9-seed pooled PermG FPR at $q{=}0.05$ is 4/54${=}7.4\%$, Table~\ref{tab:null_fpr_methods}). The expanded null sample reveals modest false positive rates that increase with $q$.}
140	\label{tab:fdr_sensitivity}
141	\resizebox{\columnwidth}{!}{%
142	\begin{tabular}{lccc}
143	\toprule
144	$q$ & Null FDR-sig (/36) & Treatment FDR-sig (/24) & Separation \\
145	\midrule
146	0.01 & 3 & 0  & Underpowered \\
147	0.05 & 4 & 19 & Good \\
148	0.10 & 8 & 24 & Good (elevated null) \\
149	\bottomrule
150	\end{tabular}}
151	\end{table}
152	
153	\paragraph{PermG $p$-value gradient at the onset boundary ($\alpha{=}0.45$).}
154	At the onset boundary, PermG operates near its detection limit, and marginal $p$-values exhibit seed-dependent variation consistent with the statistical power interpretation (\S\ref{sec:theory}).
155	Table~\ref{tab:fdr_gradient_a045} reports BH-corrected $p$-values for all 8 canary$\to$downstream pairs across two seeds at $\alpha{=}0.45$.
156	Seed~43 reaches a minimum FDR-corrected $p{=}0.059$ (18\% above the $q{=}0.05$ threshold), while seed~42 reaches $p{=}0.091$ (82\% above threshold).
157	No pair crosses the significance threshold at either seed, yielding the aggregate 0/8 detection rate reported in \S\ref{sec:regime}.
158	The gradient is consistent with a continuous power transition rather than a binary absence of signal: PermG operates near its detection limit at $\alpha{=}0.45$, with seed-dependent variation in marginal $p$-values.
159	
160	\begin{table}[h]
161	\centering
162	\small
163	\caption{BH-corrected PermG $p$-values at $\alpha{=}0.45$ (8 canary$\to$downstream pairs $\times$ 2 seeds). Min $p_{\mathrm{fdr}}$ per seed shown. All pairs remain above the $q{=}0.05$ threshold, yielding 0/8 aggregate detection.}
164	\label{tab:fdr_gradient_a045}
165	\begin{tabular}{lcc}
166	\toprule
167	 & Seed 42 & Seed 43 \\
168	\midrule
169	Min FDR $p$ & 0.091 & 0.059 \\
170	Gap to $q{=}0.05$ & 82\% & 18\% \\
171	PermG fwd sig (/8) & 0 & 0 \\
172	\bottomrule
173	\end{tabular}
174	\end{table}
175	
176	\section{Systematic Robustness Analysis}
177	\label{app:spec_curve}
178	
179	The sharp detection onset reported in \S\ref{sec:regime} could in principle depend on specific analytical choices (pair selection, seed, $\alpha$ level, method parameters).
180	We assess robustness via specification curve analysis~\cite{simonsohn2020specification,steegen2016increasing}, systematically varying analytical degrees of freedom to test whether the 0/8$\to$6/8 transition is specification-invariant.
181	Our specification curve varies data subsets and pair selections while holding the detection method (PermG) and its hyperparameters fixed, more closely resembling a systematic subset analysis than a full specification curve in the sense of \citet{simonsohn2020specification}.
182	
183	We construct 1{,}160 analytical specifications from the combinatorial space of: 13 contamination levels ($\alpha$ grid), seed selection ($\{42, 43, 44, 45\}$ where available), 8 canonical canary$\to$downstream pairs (\{token entropy, ECE\} $\times$ \{distinct-1, distinct-2, distinct-3, mauve\}), and method parameters (all PermG with $n_\text{perm}{=}5{,}000$, BH FDR $q{=}0.05$).
184	All specifications use the D120-canonical analysis pipeline with $3\sigma$ threshold calibration (D105) as a hard filter.
185	
186	\begin{table}[h]
187	\centering
188	\small
189	\caption{Specification curve summary (1{,}160 specifications, D120-compliant). The blind$\to$onset jump is robust across specifications: 0\% significance rate through $\alpha{=}0.45$, rising to 75\% at $\alpha{=}0.50$.}
190	\label{tab:spec_curve}
191	\begin{tabular}{lc}
192	\toprule
193	Metric & Value \\
194	\midrule
195	Total specifications & 1{,}160 \\
196	Significant (FDR $q{<}0.05$) & 536 (46.2\%) \\
197	\midrule
198	\emph{By regime} & \\
199	\quad Blind ($\alpha \leq 0.45$) & 0\% \\
200	\quad Onset ($\alpha{=}0.50$) & 75\% \\
201	\quad Detection ($\alpha \geq 0.75$) & 62--75\% \\
202	\bottomrule
203	\end{tabular}
204	\end{table}
205	
206	The specification curve confirms that the sharp detection onset is not an artifact of particular analytical choices: the categorical jump from 0\% to ${\geq}75\%$ significance at $\alpha_c{\approx}0.50$ holds across the vast majority of specifications, supporting the main text claim (\S\ref{sec:regime}).
207	Figure~\ref{fig:spec_curve} visualizes the specification-level detection rates.
208	
209	\begin{figure}[h]
210	\centering
211	\includegraphics[width=\columnwidth]{figures/fig_spec_curve.pdf}
212	\caption{Specification curve analysis (1{,}160 configurations). Each point is one analytical specification (method $\times$ pair $\times$ seed); lines trace detection rates across contamination levels. Bottom bar indicates the method for each specification. The blind$\to$onset jump at $\alpha_c{\approx}0.50$ is robust across specifications.}
213	\label{fig:spec_curve}
214	\end{figure}
215	
216	
217	\section{Transfer Entropy Analysis}
218	\label{app:transfer_entropy}
219	
220	Table~\ref{tab:te_results} reports transfer entropy (TE; \citealp{schreiber2000measuring}) results aggregated across all baseline conditions.
221	TE was estimated using 3-bin discretization with permutation testing ($n{=}5{,}000$).
222	No pair reaches BH-corrected significance ($q{=}0.05$) in any condition, confirming that non-parametric information-theoretic methods lack detection power at $T{=}11$.
223	
224	\begin{table}[h]
225	\centering
226	\small
227	\caption{Transfer Entropy results (12 runs across all $\alpha$ levels). TE\textsubscript{fwd}: canary$\to$downstream; TE\textsubscript{rev}: downstream$\to$canary. Mean uncorrected permutation $p$-values ($n{=}5{,}000$). No pair reaches BH-corrected $q{<}0.05$ in any run.}
228	\label{tab:te_results}
229	\resizebox{\columnwidth}{!}{%
230	\begin{tabular}{llcccc}
231	\toprule
232	Canary & Downstream & TE\textsubscript{fwd} (mean) & $p$\textsubscript{fwd} (mean) & TE\textsubscript{rev} (mean) & $p$\textsubscript{rev} (mean) \\
233	\midrule
234	token\_entropy & distinct-1 & 0.289 & 0.559 & 0.480 & 0.490 \\
235	token\_entropy & distinct-2 & 0.300 & 0.529 & 0.496 & 0.447 \\
236	token\_entropy & distinct-3 & 0.255 & 0.645 & 0.484 & 0.459 \\
237	token\_entropy & perplexity & 0.257 & 0.676 & 0.386 & 0.626 \\
238	ECE & distinct-1 & 0.185 & 0.720 & 0.184 & 0.891 \\
239	ECE & distinct-2 & 0.208 & 0.683 & 0.216 & 0.846 \\
240	ECE & distinct-3 & 0.209 & 0.689 & 0.227 & 0.807 \\
241	ECE & perplexity & 0.296 & 0.572 & 0.263 & 0.747 \\
242	\bottomrule
243	\end{tabular}}
244	\end{table}
245	
246	\phantomsection\label{app:te_mi}
247	\paragraph{KNN-based TE/MI decomposition.}
248	A $k$-nearest-neighbor TE estimator ($k{=}5$) provides a model-free complement to the parametric Granger framework.
249	Forward-dominant TE fraction increases monotonically with $\alpha$: 4/8 pairs at $\alpha{=}0.25$ (mean net TE${=}0.14$), 5/8 at $\alpha{=}0.50$ (net TE${=}0.42$), 6/8 at $\alpha{=}0.60$ (net TE${=}0.57$), and 8/8 at $\alpha{=}1.0$ (net TE${=}1.59$).
250	All 120 forward TE bootstrap 95\% CIs exclude zero at $T{=}10$; all 48 at $T{=}20$.
251	The ``high MI, low TE'' hypothesis for the non-monotonic dip is supported by only 2/8 pairs (ECE$\to$perplexity and token entropy$\to$perplexity); the remaining 6 pairs show elevated TE even at $\alpha{=}0.60$, indicating confounded co-variation rather than a universal mechanism.
252	
253	\section{Change-Point Detection Analysis}
254	\label{app:change_point}
255	
256	We apply a max-split change-point test with bootstrap significance assessment ($n{=}5{,}000$, $p{<}0.05$) to each metric's generation-level time series ($T{=}11$).
257	
258	Under the null control ($\alpha{=}0.00$, 3~seeds), downstream diversity metrics (distinct-1, distinct-2, distinct-3) produce significant change-points at generation~2 in all seeds (9/9 tests). With additional significant tests from ECE (2/3 seeds) and token entropy (1/3 seeds), the overall false positive rate reaches 66.7\% (12/18 tests; Table~\ref{tab:cp_null}). The monotonic drift inherent in iterative self-training is sufficient to trigger change-point detection even without canary contamination. Individual change-point significance therefore cannot serve as standalone evidence for a canary-specific effect.
259	
260	Although individual significance is unreliable as a discriminator, the temporal ordering of detected change-points reverses between null and treatment conditions. In the null ($\alpha{=}0.00$), downstream metrics show the earliest significant breaks at generation~2 (all seeds), while significant canary breaks appear later (ECE at generations~4--8). Under treatment conditions ($\alpha{\geq}0.75$), this ordering flips: canary metrics place their best splits at generation~1, followed by downstream diversity metrics at generations~2--4 and perplexity at generation~4 (Table~\ref{tab:cp_results}). This ordering reversal provides complementary evidence from a distinct statistical framework, consistent with the Granger-precedence analysis in \S\ref{sec:experiments}.
261	
262	Several caveats apply. The 18 individual tests per condition were not corrected for multiple comparisons (BH or Bonferroni); primary inference rests on the cross-metric temporal ordering rather than on individual significance tests. Under treatment conditions, token entropy places its best split at generation~1 with large effect sizes ($|d|{>}2.5$) in all seeds, but the pre-change segment at a generation-1 split contains only a single data point, reducing bootstrap power (1/3 seeds significant at $\alpha{=}0.75$). The short series length ($T{=}11$) further limits overall detection power.
263	
264	\begin{table}[h]
265	\centering
266	\small
267	\caption{Change-point detection under null control ($\alpha{=}0.00$, 3 seeds). CP: detected change-point generation (mean across significant seeds); $|d|$: Cohen's $d$ effect size (mean across all seeds); Sig.\ rate: fraction of seeds where $p{<}0.05$. Overall FPR: 12/18 = 66.7\%.}
268	\label{tab:cp_null}
269	\resizebox{\columnwidth}{!}{%
270	\begin{tabular}{lcccc}
271	\toprule
272	Metric & CP gen (mean) & $|d|$ (mean) & Sig.\ rate & Type \\
273	\midrule
274	token\_entropy & 1.0 & 2.94 & 1/3 & canary \\
275	ECE & 6.0 & 1.62 & 2/3 & canary \\
276	distinct-1 & 2.0 & 2.27 & 3/3 & downstream \\
277	distinct-2 & 2.0 & 2.40 & 3/3 & downstream \\
278	distinct-3 & 2.0 & 2.27 & 3/3 & downstream \\
279	perplexity & --- & 3.11 & 0/3 & downstream \\
280	\bottomrule
281	\end{tabular}}
282	\end{table}
283	
284	\begin{table}[h]
285	\centering
286	\small
287	\caption{Change-point detection at $\alpha{=}0.75$ (3 seeds). CP: detected change-point generation; $|d|$: Cohen's $d$ effect size between pre- and post-change segments. Sig.\ rate: fraction of seeds where $p{<}0.05$.}
288	\label{tab:cp_results}
289	\resizebox{\columnwidth}{!}{%
290	\begin{tabular}{lcccc}
291	\toprule
292	Metric & CP gen (mean) & $|d|$ (mean) & Sig.\ rate & Type \\
293	\midrule
294	token\_entropy & 1.0 & 3.21 & 1/3 & canary \\
295	ECE & 1.0 & 3.10 & 1/3 & canary \\
296	distinct-1 & 2.3 & 2.18 & 3/3 & downstream \\
297	distinct-2 & 3.0 & 1.97 & 3/3 & downstream \\
298	distinct-3 & 3.7 & 1.86 & 3/3 & downstream \\
299	perplexity & 4.0 & 1.70 & 3/3 & downstream \\
300	\bottomrule
301	\end{tabular}}
302	\end{table}
303	
304	\paragraph{Dose-response ordering pattern.}
305	Table~\ref{tab:cp_ordering} summarizes the ordering pattern across contamination levels.
306	The canary-to-downstream gap shifts monotonically from negative (downstream first) under the null to positive (canary first) under treatment, ruling out a methodological artifact in which canary metrics would systematically appear earlier regardless of condition.
307	The $\alpha{=}1.0$ analysis is limited to a single seed (s42); all other conditions use 3 seeds.
308	
309	\begin{table}[h]
310	\centering
311	\small
312	\resizebox{\columnwidth}{!}{%
313	\begin{tabular}{lcccl}
314	\toprule
315	$\alpha$ & Canary cp & Downstream cp & Gap & Direction \\
316	\midrule
317	0.00 & gen 4--8 & gen 2 & $-$2.5 & Downstream first \\
318	0.25 & gen 3--4 & gen 3--4 & $\approx$0 & Simultaneous \\
319	0.75 & gen 1 & gen 2--4 & $+$2.25 & Canary first \\
320	1.00 & gen 2 & gen 2--5 & $+$1.0 & Canary first \\
321	\bottomrule
322	\end{tabular}}
323	\caption{Change-point ordering reversal across contamination levels. Under the null ($\alpha{=}0.00$), downstream metrics break before canary metrics; this ordering reverses monotonically as $\alpha$ increases, consistent with the Granger-precedence analysis.}
324	\label{tab:cp_ordering}
325	\end{table}
326	
327	
328	\section{Sequential Monitoring: CUSUM vs Calibrated Threshold}
329	\label{app:csmp}
330	
331	We translate the Granger-precedence finding into a deployable monitoring protocol using CUSUM (cumulative sum) sequential testing~\cite{page1954continuous}, calibrated against the $\alpha{=}0.0$ null control.
332	The null-calibration procedure sets the alarm threshold $h$ such that the false alarm rate (FAR) is 0\% on null data (3~seeds, $T{=}10$), providing controlled Type~I error guarantees.
333	
334	\paragraph{Method.}
335	CUSUM monitors the cumulative deviation of token entropy from its null-control baseline: $S_t = \max(0,\; S_{t-1} + (\mu_0 - x_t) - k)$, where $\mu_0$ is the null-control mean, $k$ is the allowance parameter, and the alarm triggers when $S_t > h$.
336	We calibrate $h$ for each $k$ from the $\alpha{=}0.0$ null data (Table~\ref{tab:csmp_calibration}).
337	As a baseline, we compare against a simple calibrated threshold: alarm when the metric crosses $\mu_0 - 2\sigma_0$ for $n{\geq}1$ or $n{\geq}2$ consecutive generations.
338	
339	\begin{table}[h]
340	\centering
341	\small
342	\caption{CUSUM calibration parameters from $\alpha{=}0.0$ null control (3~seeds). $h$: alarm threshold calibrated to achieve FAR${=}$0\%. For $k{\geq}0.25$, the null CUSUM statistic remains at zero, yielding $h \approx 0$.}
343	\label{tab:csmp_calibration}
344	\begin{tabular}{lcc}
345	\toprule
346	$k$ & $h$ & FAR \\
347	\midrule
348	0.05 & 1.530 & 0\% \\
349	0.10 & 1.005 & 0\% \\
350	0.25 & $\approx$0 & 0\% \\
351	0.50 & $\approx$0 & 0\% \\
352	1.00 & $\approx$0 & 0\% \\
353	\bottomrule
354	\end{tabular}
355	\end{table}
356	
357	\paragraph{Results.}
358	Table~\ref{tab:csmp_comparison} compares CUSUM and simple threshold detection times across gradual contamination levels.
359	At the recommended operating point ($k{=}0.25$), CUSUM and the simple threshold ($n{\geq}1$) produce identical alarm times (generation~1) across all seeds and contamination levels.
360	More conservative CUSUM settings ($k{=}0.1$, $k{=}0.05$) delay detection to match the $n{\geq}2$ threshold or later.
361	At $k{=}1.0$ with $\alpha{=}0.50$, CUSUM fails entirely ($S_t \equiv 0$ for all seeds), demonstrating sensitivity to the allowance parameter.
362	No CUSUM configuration outperforms the simple calibrated threshold at any operating point tested.
363	
364	\begin{table}[h]
365	\centering
366	\small
367	\caption{CUSUM vs simple calibrated threshold: alarm generation across contamination levels (3~seeds each; all seeds agree on the alarm generation shown). Threshold: metric crosses $\mu_0 - 2\sigma_0$. No CUSUM configuration outperforms the simple threshold at any operating point.}
368	\label{tab:csmp_comparison}
369	\resizebox{\columnwidth}{!}{%
370	\begin{tabular}{lccccc}
371	\toprule
372	$\alpha$ & CUSUM $k{=}0.25$ & CUSUM $k{=}0.1$ & CUSUM $k{=}0.05$ & Thresh $n{\geq}1$ & Thresh $n{\geq}2$ \\
373	\midrule
374	0.50 & gen 1 & gen 2 & gen 3 & gen 1 & gen 2 \\
375	0.75 & gen 1 & gen 2 & gen 2 & gen 1 & gen 2 \\
376	\bottomrule
377	\multicolumn{6}{l}{\footnotesize CUSUM $k{=}1.0$ at $\alpha{=}0.50$: $S_t \equiv 0$ for all seeds (complete detection failure).} \\
378	\end{tabular}}
379	\end{table}
380	
381	\paragraph{Interpretation.}
382	The equivalence arises because the generation-0$\to$1 entropy drop is large ($|\Delta x| > 0.7$ for $\alpha{=}0.50$, $> 1.0$ for $\alpha{=}0.75$) relative to the null-control variability ($\sigma_0 \approx 0.03$).
383	Any detector with a near-zero or small threshold triggers at generation~1; CUSUM's cumulative memory provides no advantage when the initial shift already exceeds the control limit.
384	This result extends Claim~3 (method sensitivity) beyond lead-lag detection to the monitoring domain: even a sequential testing procedure with stronger theoretical properties (optimal expected detection delay under continuous monitoring) does not improve over a calibrated baseline when the initial contamination signal dominates the allowance parameter.
385	The contribution of the null-calibrated monitoring framework is the calibration procedure itself (setting alarm boundaries from $\alpha{=}0.0$ data to guarantee FAR${=}$0\%), not the CUSUM algorithm.
386	
387	\begin{figure}[h]
388	\centering
389	\includegraphics[width=\columnwidth]{figures/fig_cusum_monitoring.pdf}
390	\caption{CUSUM sequential monitoring of token entropy at two contamination levels ($\alpha{=}0.50$, $\alpha{=}0.75$; seed~42). Null control limits calibrated from $\alpha{=}0.0$ runs. At both operating points, the simple $2\sigma$ threshold triggers at the same generation as CUSUM ($k{=}0.25$), confirming that the large initial shift dominates any cumulative memory advantage.}
391	\label{fig:cusum_monitoring}
392	\end{figure}
393	
394	\section{Background and Notation}
395	\label{app:background}
396	\label{sec:background}
397	
398	This section establishes the formal setup and notation used throughout the paper.
399	
400	\paragraph{Iterative training loop.}
401	Let $M_0$ denote a pretrained language model and $\mathcal{D}_\text{real}$ a fixed corpus of human-written text.
402	At each generation $t \geq 1$, the model $M_{t-1}$ generates a synthetic corpus $\mathcal{D}_\text{synth}^{(t-1)}$, and the next-generation model $M_t$ is fine-tuned on a mixture of $\alpha$ fraction synthetic data and $(1{-}\alpha)$ fraction real data:
403	\begin{equation}
404	    \mathcal{D}_\text{train}^{(t)} = \alpha \cdot \mathcal{D}_\text{synth}^{(t-1)} \;+\; (1{-}\alpha) \cdot \mathcal{D}_\text{real}, \quad \alpha \in [0, 1].
405	    \label{eq:mixing}
406	\end{equation}
407	At $\alpha{=}1.0$, this reduces to the full-replacement paradigm of \citet{shumailov2024curse}.
408	
409	\paragraph{Metric families.}
410	\emph{Canary metrics}: token entropy ($H(p_\theta | \text{context})$ on held-out samples) and expected calibration error (ECE).
411	\emph{Downstream metrics}: distinct-$n$ ($n \in \{1, 2, 3\}$)~\cite{li2016diversity} and perplexity.
412	Each metric produces a time series of $T{+}1$ observations.
413	
414	\paragraph{Lead-lag testing.}
415	Given canary series $X$ and downstream series $Y$, the central question is whether changes in $X$ temporally precede changes in $Y$, requiring directionality and confounder control beyond simple correlation.
416	We employ five methods spanning permissive to conservative: naive cross-correlation, differenced cross-correlation, threshold onset detection, permutation Granger causality~\cite{shojaie2022granger}, and Toda--Yamamoto Granger causality~\cite{toda1995statistical}.
417	
418	\section{MMCT Algorithm}
419	\label{app:mmct}
420	
421	Algorithm~\ref{alg:mmct} describes the Multi-Method Consensus Test (MMCT) introduced in \S\ref{sec:mmct}.
422	
423	\begin{algorithm}[h]
424	\caption{Multi-Method Consensus Test (MMCT)}
425	\label{alg:mmct}
426	\begin{algorithmic}[1]
427	\Require Time series pair $(X, Y)$; methods $\{m_1, \ldots, m_K\}$ ($K{=}5$); null-control data $\mathcal{N}$ (from $\alpha{=}0.0$); tolerance $\epsilon{=}0.01$
428	\Ensure $p$-value, consensus level $\hat{K}$
429	\For{each method $m_k$}
430	    \State Compute empirical FPR: $\widehat{\mathrm{FPR}}_k \gets$ fraction of null-control pairs where $m_k$ rejects $H_0$
431	    \State Compute weight: $w_k \gets 1 / \max(\widehat{\mathrm{FPR}}_k,\; \epsilon)$
432	    \State Apply $m_k$ to $(X, Y)$: $d_k \gets \mathbf{1}[m_k \text{ rejects } H_0]$
433	\EndFor
434	\State Weighted consensus: $W(X {\to} Y) \gets \sum_{k} w_k \, d_k \;/\; \sum_{k} w_k$
435	\State Build empirical null distribution of $W$ from all null-control pairs in $\mathcal{N}$
436	\State Compute $p$-value from empirical null: $p \gets \Pr_{\mathcal{N}}(W \geq W_{\mathrm{obs}})$
437	\State Consensus level: $\hat{K} \gets \sum_{k} d_k$
438	\State \Return $p$, $\hat{K}$
439	\end{algorithmic}
440	\end{algorithm}
441	
442	\paragraph{Design rationale.}
443	FPR-inverse weighting penalizes methods with high false positive rates on null-control data: naive cross-correlation (FPR${=}94.4\%$) receives weight $w{=}1.06$, while PermG (FPR${=}7.4\%$, the lowest among all five methods) receives $w{=}13.5$.
444	The empirical null distribution avoids parametric assumptions that are unreliable for short ($T{=}5$--$20$), non-stationary series typical of iterative training.
445	MMCT is a consensus testing protocol, not a novel statistical method; its value lies in systematic method comparison and the identification of method-dependent conclusions.
446	
447	
448	\section{Methodological Comparison Table}
449	\label{app:method_comparison}
450	
451	Table~\ref{tab:method-comparison} summarizes the methodological coverage of existing canary and monitoring analyses across the diagnostic dimensions identified in \S\ref{sec:method}.
452	No prior work combines all six dimensions.
453	
454	\begin{table}[h]
455	\centering
456	\small
457	\caption{Methodological comparison of canary and monitoring analyses. \checkmark\ = present, $\times$ = absent, $\circ$ = partial (${\leq}2$ levels or limited replication). Diff.\ = differencing/stationarity controls. Multi-M.\ = ${\geq}2$ independent statistical methods. MTC = multiple testing correction. Regime = systematic variation of $\alpha$. Seeds = ${\geq}3$ independent seeds. Arch.\ = ${\geq}2$ architecturally distinct model families.}
458	\label{tab:method-comparison}
459	\resizebox{\columnwidth}{!}{%
460	\begin{tabular}{lccccccl}
461	\toprule
462	Work & Diff. & Multi-M. & MTC & Regime & Seeds & Arch. & Metrics \\
463	\midrule
464	\citet{shumailov2024curse}     & $\times$   & $\times$   & $\times$   & $\circ$    & \checkmark & \checkmark & PPL \\
465	\citet{du2025scales}           & $\times$   & $\times$   & \checkmark & \checkmark & \checkmark & $\times$   & ECE, Acc, Dist-$n$ \\
466	\citet{gambetta2024surplexity} & $\times$   & $\times$   & $\times$   & \checkmark & \checkmark & \checkmark & Surplexity, Ent \\
467	SIGMA~\cite{sigma2026spectral} & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & Spectral \\
468	DCES~\cite{dces2026counter}    & $\times$   & $\times$   & $\times$   & $\times$   & $\times$   & \checkmark & ECE, Ent, PPL \\
469	\midrule
470	\textbf{Ours}                  & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & \checkmark & Ent, ECE, PPL, Dist-$n$ \\
471	\bottomrule
472	\end{tabular}%
473	}
474	\end{table}
475	
476	\section{Extended Discussion}
477	\label{app:extended_discussion}
478	
479	\paragraph{Calibration scope and generalization.}
480	All FPR and FNR calibration results are specific to our experimental setup: Pythia-410M, WikiText-103 subset, $T{=}10$, and six contamination levels.
481	Cross-architecture validation across 15 conditions spanning five model families shows that the entropy-leads-diversity pattern generalizes in 11 of 15 architecture-seed combinations (Table~\ref{tab:generalization}); GPT-2 bf16 (0/8), GPT-2 s43 (6/8 bidirectional), SmolLM3-3B (3/8, entropy decoupling), and Pythia-1.4B s42 (2/8) do not confirm the pattern.
482	
483	\paragraph{Domain-dependent directionality.}
484	The unidirectional forward causation observed on WikiText (PermG reverse${=}$0/8 across all conditions) does not hold universally.
485	On C4 at $\alpha{=}0.50$ (s42 fp32), PermG reverse reaches 7/8, indicating near-symmetric bidirectional coupling; however, this is seed-dependent (s43: 1/8) and noted as preliminary.
486	The practical implication is that directional asymmetry should be verified per domain.
487	
488	\paragraph{Token entropy versus perplexity.}
489	The distinction lies in the evaluation domain: token entropy is $H(p_\theta | \text{context})$ on held-out real data, while perplexity is $\exp(H_\text{cross})$ on model-generated text.
490	First-differencing removes their shared downward trend: the canary$\to$diversity channel survives because entropy leads diversity by one generation, whereas the canary$\to$perplexity channel vanishes because both co-move synchronously.
491	
492	\paragraph{NLP-specific constraints.}
493	Our application of Granger-type methods faces constraints absent in econometrics: (i)~observation length ($T{=}5$--$20$ vs.\ $T{=}100$--$1000$); (ii)~non-stationarity by design rather than incidental; (iii)~small multiplicity for FDR correction (8--32 pairs per regime).
494	Transfer entropy (0/192 FDR-significant results) confirms that method sensitivity extends beyond the five-method panel.
495	
496	\paragraph{Prevention paradox.}
497	Effective intervention truncates the collapse trajectory that established Granger precedence.
498	Differenced cross-correlation retains significance under intervention (31/32 pairs), while threshold onset fails entirely (0/8), reinforcing the multi-method rationale.
499	
500	\paragraph{Grouped testing rationale.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "364294fe-6f1f-4912-91cd-2c39ec6108dd",
  "isSidechain": true,
  "promptId": "51e3df65-9561-4454-8292-70ea3a87414d",
  "agentId": "aac173aafa6353ad3",
  "type": "user",
  "uuid": "70b6155b-54dc-482a-9d1b-339ae599c3ea",
  "sourceToolAssistantUUID": "364294fe-6f1f-4912-91cd-2c39ec6108dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-24T18:28:24.682Z_

Let me continue reading the appendix to find all figures:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70b6155b-54dc-482a-9d1b-339ae599c3ea",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsFK2VLk4dEbLX4Dvym",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a7738cec-865c-456b-b8d4-41d5bc5eef7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MiBNSNUyb5Y6zaXjJ7XCZe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 12943,
      "cache_read_input_tokens": 52503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12943,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-24T18:28:25.406Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01X4zSuyGc4Vaj6uDoAxKb9S`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\begin{figure}\\|\\\\\\\\label{fig:\\|\\\\\\\\caption\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/*.tex | head -100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7738cec-865c-456b-b8d4-41d5bc5eef7a",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsFK2VLk4dEbLX4Dvym",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "56b1dde4-f608-4734-b23a-89e13a37073d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MiBNSNUyb5Y6zaXjJ7XCZe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 12943,
      "cache_read_input_tokens": 52503,
      "output_tokens": 125,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12943
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 125,
          "cache_read_input_tokens": 52503,
          "cache_creation_input_tokens": 12943,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12943,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-24T18:28:25.583Z_

<details><summary>↩ Tool result · `toolu_01X4zSuyGc4Vaj6uDoAxKb9S`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:18:\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:45:\caption{Distinct-3 drift (\%, generation~0$\to$10) across contamination levels. $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.75$: 3-seed mean${\pm}$std; $\alpha{=}1.0$: 4-seed mean${\pm}$std; $\alpha{=}0.50$: single seed.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:84:\caption{Observation window sensitivity for Tier~3 consensus ($K{\geq}4/5$) at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Tier~3 pairs: number of canary$\to$downstream pairs (out of 8 validated) reaching $K{\geq}4/5$ method agreement. TY pairs: number of effect-size reference pairs (out of 6) reaching Toda--Yamamoto significance (moderate supplementary method; \S\ref{sec:method}). Consensus stabilizes at $T_{\min}{\geq}5$; TY stabilizes at $T_{\min}{\geq}6$.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:102:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:105:\caption{Consensus stability across minimum observation windows $T_{\min} \in \{5, \ldots, 10\}$. Left: $K{\geq}3$ consensus count at $\alpha{=}0.75$ (3 seeds). Right: per-method detection count across $T_{\min}$. Consensus stabilises at $T_{\min}{=}5$, confirming that the 10-generation default provides ample statistical power.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:106:\label{fig:window_sensitivity}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:119:\caption{Permutation count stability analysis ($\alpha{=}0.75$, 3~seeds, 24 canary$\to$downstream pairs). $p$-values from permutation Granger tests at $n_{\text{perm}}{=}5{,}000$ versus $n_{\text{perm}}{=}10{,}000$.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:139:\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs, 8-pair basis). Null: $\alpha{=}0.0$ (6 of 9 null seeds, seeds 45--50, 36 pairs, 6-pair basis; the full 9-seed pooled PermG FPR at $q{=}0.05$ is 4/54${=}7.4\%$, Table~\ref{tab:null_fpr_methods}). The expanded null sample reveals modest false positive rates that increase with $q$.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:163:\caption{BH-corrected PermG $p$-values at $\alpha{=}0.45$ (8 canary$\to$downstream pairs $\times$ 2 seeds). Min $p_{\mathrm{fdr}}$ per seed shown. All pairs remain above the $q{=}0.05$ threshold, yielding 0/8 aggregate detection.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:189:\caption{Specification curve summary (1{,}160 specifications, D120-compliant). The blind$\to$onset jump is robust across specifications: 0\% significance rate through $\alpha{=}0.45$, rising to 75\% at $\alpha{=}0.50$.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:209:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:212:\caption{Specification curve analysis (1{,}160 configurations). Each point is one analytical specification (method $\times$ pair $\times$ seed); lines trace detection rates across contamination levels. Bottom bar indicates the method for each specification. The blind$\to$onset jump at $\alpha_c{\approx}0.50$ is robust across specifications.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:213:\label{fig:spec_curve}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:227:\caption{Transfer Entropy results (12 runs across all $\alpha$ levels). TE\textsubscript{fwd}: canary$\to$downstream; TE\textsubscript{rev}: downstream$\to$canary. Mean uncorrected permutation $p$-values ($n{=}5{,}000$). No pair reaches BH-corrected $q{<}0.05$ in any run.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:267:\caption{Change-point detection under null control ($\alpha{=}0.00$, 3 seeds). CP: detected change-point generation (mean across significant seeds); $|d|$: Cohen's $d$ effect size (mean across all seeds); Sig.\ rate: fraction of seeds where $p{<}0.05$. Overall FPR: 12/18 = 66.7\%.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:287:\caption{Change-point detection at $\alpha{=}0.75$ (3 seeds). CP: detected change-point generation; $|d|$: Cohen's $d$ effect size between pre- and post-change segments. Sig.\ rate: fraction of seeds where $p{<}0.05$.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:323:\caption{Change-point ordering reversal across contamination levels. Under the null ($\alpha{=}0.00$), downstream metrics break before canary metrics; this ordering reverses monotonically as $\alpha$ increases, consistent with the Granger-precedence analysis.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:342:\caption{CUSUM calibration parameters from $\alpha{=}0.0$ null control (3~seeds). $h$: alarm threshold calibrated to achieve FAR${=}$0\%. For $k{\geq}0.25$, the null CUSUM statistic remains at zero, yielding $h \approx 0$.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:367:\caption{CUSUM vs simple calibrated threshold: alarm generation across contamination levels (3~seeds each; all seeds agree on the alarm generation shown). Threshold: metric crosses $\mu_0 - 2\sigma_0$. No CUSUM configuration outperforms the simple threshold at any operating point.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:387:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:390:\caption{CUSUM sequential monitoring of token entropy at two contamination levels ($\alpha{=}0.50$, $\alpha{=}0.75$; seed~42). Null control limits calibrated from $\alpha{=}0.0$ runs. At both operating points, the simple $2\sigma$ threshold triggers at the same generation as CUSUM ($k{=}0.25$), confirming that the large initial shift dominates any cumulative memory advantage.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:391:\label{fig:cusum_monitoring}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:424:\caption{Multi-Method Consensus Test (MMCT)}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:457:\caption{Methodological comparison of canary and monitoring analyses. \checkmark\ = present, $\times$ = absent, $\circ$ = partial (${\leq}2$ levels or limited replication). Diff.\ = differencing/stationarity controls. Multi-M.\ = ${\geq}2$ independent statistical methods. MTC = multiple testing correction. Regime = systematic variation of $\alpha$. Seeds = ${\geq}3$ independent seeds. Arch.\ = ${\geq}2$ architecturally distinct model families.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:520:\caption{Pythia-1.4B phase-diagram cells (fp32, PermG forward, direction-checked).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:544:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:547:\caption{Pythia-1.4B phase diagram (PermG forward, 6-pair basis). Each cell shows per-seed detection fractions (s42\,|\,s44 for $T{=}10$; s42\,|\,s43 for $T{=}15$). The detection boundary ($\alpha_c \approx 0.50$) is qualitatively consistent with the 410M results, confirming cross-scale generality.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:548:\label{fig:14b_phase}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:575:\caption{Per-method FDR significance (/8 pairs) across contamination levels (Pythia-410M, seed~42, WikiText, fp32). PermG and Diff.\ XCorr use BH-corrected FDR ($q{=}0.05$); Naive XCorr, Threshold, and TY use uncorrected $p{<}0.05$ (no FDR field in pipeline). $\alpha{=}1.0$ from Pythia-410M cross-architecture condition (same seed/domain/precision).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:602:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:605:\caption{Per-method detection heatmaps (Pythia-410M, seed~42, fp32, $T \in \{10, 20\}$). Each panel shows forward-direction detection rate (\%) across contamination levels for one method. PermG exhibits the sharpest onset (0\%$\to$75\% between $\alpha{=}0.45$ and 0.50) with zero null-control detection, while Naive XCorr saturates across all levels including null. TY and Threshold show diffuse, unstable profiles.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:606:\label{fig:per_method_phase}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:618:\caption{Naive baseline comparison (Pythia-410M, $T{=}10$, fp32, 3 null-control runs).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:658:\caption{PermG power analysis: $\beta_{50}$ (coupling for 50\% power) under BH-FDR correction ($q{=}0.05$, 8 pairs). $\beta_{50} \cdot \sqrt{T}$ decreases with $T$, indicating power grows faster than $\sqrt{T}$. FPR: false positive rate at $\beta{=}0$ (raw / FDR-corrected). Dashes indicate $<$50\% power not reached within $\beta \leq 2.0$.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:676:\caption{PermG detection power as a function of coupling strength $\beta$ for five observation lengths ($T{=}6$--$20$; 100 replications $\times$ 5{,}000 permutations, BH FDR $q{=}0.05$). Power increases with both $\beta$ and $T$; at $T{=}6$--$8$, PermG remains underpowered ($<$20\%) even at $\beta{=}2.0$, consistent with the $T{=}10$ minimum required for reliable detection in our experimental setting.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:677:\label{fig:permg_power}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:699:\caption{Size (FPR at $\beta{=}0$) and power ($\beta{=}0.6$) under stationary and non-stationary AR(1) DGP ($T{=}11$, 1{,}000 reps, 500 perms). First-differencing maintains nominal size across all $\varphi$; PermG FPR inflates to ${\sim}10\%$ at $\varphi{\geq}0.95$.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:726:\caption{Empirical AR(1) coefficients for token entropy (te) and distinct-1 (d1), raw and first-differenced series. High raw $\varphi$ in d1 reflects deterministic iterative-training decline, not stochastic AR persistence; first-differencing reduces $\varphi$ to $< 0.44$.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:751:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:754:\caption{Empirical AR(1) coefficients by contamination level (Pythia-410M, seed~42, $T{=}10$). (a)~Token entropy: raw $\varphi$ transitions from anti-correlated ($-0.51$) at $\alpha{=}0$ to near-unity ($1.00$) at $\alpha{=}1.0$; first-differencing reduces all values below the $\varphi{=}0.95$ FPR danger zone (dashed red). (b)~Distinct-1: high raw $\varphi$ ($0.81$--$0.97$) across all $\alpha$ including null reflects deterministic trend, not stochastic AR persistence; first-differenced $\varphi$ drops to near zero.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:755:\label{fig:ar1_diagnostic}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:781:\caption{Shapley value decomposition (6-pair, mauve excluded). FPR-Shapley computed from 6 null seeds (seeds 45--50, 36 pairs; 9-seed pooled FPR in Table~\ref{tab:null_fpr_methods}); FNR-Shapley from 45 signal experiments (270 pairs). Combined = FPR + FNR (more negative = better). $2^5{=}32$ coalitions, exact enumeration.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:799:\caption{Shapley value decomposition of each method's marginal contribution to FPR (positive bars, red) and FNR (negative bars, green/blue), computed from 6 null seeds (seeds 45--50, 36 pairs) and 45 signal experiments (270 pairs). DiffXCorr achieves the best combined Shapley ($-0.299$) in this 6-seed subset; PermG ranks second ($-0.141$) as the best directional method. The 9-seed pooled analysis (Table~\ref{tab:null_fpr_methods}) shows PermG's FPR (7.4\%) is now the lowest among all five methods, with DiffXCorr rising to 14.8\%.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:800:\label{fig:shapley}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:825:\caption{MMCT weight robustness (3-seed null, 48 experiments): PermG combined Shapley under four weighting schemes. PermG ranks first among directional methods in all cases. Gap = $|\phi^{\text{comb}}_{\text{PermG}} - \phi^{\text{comb}}_{\text{runner-up}}|$. $2^5{=}32$ coalitions, exact enumeration.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:853:\caption{Null-control FPR by method ($\alpha{=}0.0$, 9~seeds 42--50, 6~pairs each). All p-value--based methods (DiffXCorr, PermG, TY) report BH-FDR--corrected rejections at $q{=}0.05$ for fair comparison. Threshold uses a deterministic $3\sigma$ criterion; NaiveXCorr uses uncorrected correlation significance.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:870:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:875:\caption{Null-control FPR by method ($\alpha{=}0.0$, 6~seeds 45--50, 6-pair basis). Bars: pooled FPR; dots: per-seed FPR. Updated 9-seed pooled rates in Table~\ref{tab:null_fpr_methods}.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:876:\label{fig:null_fpr_diagnostic}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:882:\caption{Bootstrap distribution of PermG FPR (10{,}000 resamples, 6 null seeds 45--50). Mean FPR $= 11.1\%$ (red line); bootstrap percentile 95\% CI $[0.0\%, 22.2\%]$ (orange band). Updated 9-seed PermG FPR: 4/54 $= 7.4\%$, CI $[2.1\%, 17.9\%]$.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:883:\label{fig:bootstrap_fpr}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:885:\caption{PermG null-control false positive analysis. (a)~Per-method FPR comparison. (b)~Bootstrap FPR distribution.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:886:\label{fig:fpr_combined}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:925:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:928:\caption{Detection rate surface over the $\alpha \times T$ operating space (PermG forward, 3 seeds). Contour lines indicate 25\%, 50\%, and 75\% detection rates. The fitted power-law boundary $\alpha_c(T)$ (dashed) separates the blind zone ($\alpha \leq 0.45$) from the reliable detection regime ($\alpha \geq 0.75$). The transition zone ($0.50 \leq \alpha \leq 0.60$) widens at shorter $T$.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:929:\label{fig:detection_surface}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:943:\caption{Threshold sensitivity at $\alpha{=}1.0$ (Pythia-410M, s42, fp32). All thresholds trigger at generation~1 (entropy drop 40.7\%$\gg$threshold), producing identical recovery trajectories.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:983:\caption{First-differencing effect by channel type. $|r|$ retention = diff $|r|$ / naive $|r|$. Despite comparable $|r|$ retention, Granger $F$ differs by an order of magnitude. Perplexity channel has limited sample ($n{=}8$); all paired comparisons are from bf16 experiments.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1009:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1012:\caption{Channel effect size asymmetry. (a)~First-differencing retains comparable correlation magnitude for diversity ($95.2\%$) and perplexity ($100.2\%$) channels, ruling out blanket power loss. (b)~Despite equivalent $|r|$ retention, Granger $F$-statistic is ${\sim}6\times$ higher for diversity ($F{=}67.8$) than perplexity ($F{=}11.5$), reflecting a genuine temporal structure difference: diversity channels exhibit canary-leading lags while perplexity co-moves contemporaneously.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1013:\label{fig:channel_effect}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1033:\caption{Gaussian MI lower bound (bits) between token entropy and distinct-$n$ diversity metrics ($T{=}11$, Pythia-410M, fp32). Mean across distinct-1/2/3; $\alpha{=}0.05$ excluded (see text). CIs omitted due to width at $T{=}11$.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1063:\caption{Partial correlation analysis controlling for generation number. Contemporaneous: canary$_t$ vs downstream$_t$; Lagged: canary$_{t-1}$ vs downstream$_t$. Zero-order: raw Pearson; Partial: controlling for generation $t$. Sig.: pairs with $p{<}0.05$ out of 18. Negative $\Delta$ indicates partial $|r|$ \emph{exceeds} zero-order (trend removal strengthens the association).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1101:\caption{Degradation onset generation (5\% threshold) by metric and condition (Pythia-410M, WikiText, fp32). Token entropy reaches onset at generation~1 in all non-null conditions; distinct-$n$ metrics follow at generation~2.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1120:\begin{figure}[h]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1123:\caption{Cascade onset timeline (Pythia-410M, WikiText, fp32, 5\% threshold). Token entropy and ECE reach onset at generation~1 (Phase~1, blue shading), while distinct-$n$ metrics follow at generation~2 (Phase~2, orange shading). Perplexity onset occurs at generation~4 only at $\alpha{\geq}0.50$; MAUVE onset is condition-dependent. The ordering $t_H \leq t_D$ holds across all 5 conditions (2 seeds $\times$ 3 $\alpha$ levels minus $\alpha{=}0.25$ s42, which has identical Phase~1 and~2 onset).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1124:\label{fig:cascade_onset}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1201:\caption{Cascade onset generations (5\% threshold) for representative experiments (Pythia-410M, WikiText, fp32). Phase~1: entropy and ECE ($t_H$, $t_{\mathrm{ECE}}$); Phase~2: diversity ($t_D$, min over distinct-$n$); Phase~3: MAUVE ($t_M$). All conditions confirm the predicted ordering $t_H = t_{\mathrm{ECE}} \leq t_D \leq t_M$.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1273:\caption{T=20 predict-then-verify comparison (Pythia-410M, seed~42, WikiText, fp32). Excluding $\alpha{=}1.0$, two of four predictions fall within CI ($\alpha{=}0.50$, $0.75$); boundary cases show systematic bias---$\alpha{=}0.45$ falsifies the ceiling hypothesis (under-prediction), $\alpha{=}0.60$ over-predicts under raw $p$-values (v1; matches under FDR v2, not pre-committed).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1318:\caption{Task degradation across contamination levels (Pythia-410M, seed~42, fp32, generation~10). Perplexity evaluated on held-out WikiText-103.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1345:\caption{Cross-architecture PermG forward detection ($\alpha{=}1.0$, 15 model-seed combinations across five families---Pythia, GPT-2, OPT, Qwen, SmolLM3---and two domains; Padding-410M is a Pythia variant). PermG fwd $=$ count of FDR-significant forward pairs out of 8.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1384:\caption{Null-condition FPR for GPT-2-medium ($\alpha{=}0$, $T{=}10$, 6-pair basis). PermG forward detection shows extreme seed dependence; $K{\geq}3$ consensus remains at 0\% across both seeds.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1404:\caption{Null drift magnitude ($\alpha{=}0$, gen\,0$\to$10; GPT-2-medium: 2 seeds; Pythia-410M: 4 seeds, s46/s48--s50). GPT-2-medium exhibits ${\sim}4{\times}$ stronger entropy drift and ${\sim}7{\times}$ stronger distinct-3 drift than Pythia-410M.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1433:\caption{Cross-architecture PermG forward detection rates at $\alpha{=}1.0$ across 15 model-seed combinations spanning five families (345M--6.9B). Dark bars: PermG forward detection; light bars: $K{\geq}3$ consensus.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1434:\label{fig:cross_arch_heatmap}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1440:\caption{Null-control FPR by method (Pythia-410M, seed~42, 8-pair basis). Dashed line: 5\% nominal level.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1441:\label{fig:fpr_sensitivity}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1443:\caption{Cross-architecture validation and FPR sensitivity. (a)~Detection generalizes to 11/15 conditions. (b)~Method-level FPR comparison.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex:1444:\label{fig:cross_arch_combined}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:41:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:44:\caption{Metric trajectories at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead across all four seeds (shaded: inter-seed range). This pattern corresponds to 24/24 forward and 0/24 reverse FDR-significant canary$\to$diversity pairs (6 per seed, mauve excluded).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:45:\label{fig:metric_trajectory}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:95:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:98:\caption{Canary-triggered intervention (Pythia-410M, $\alpha{=}1.0$). Predictive cessation on entropy (generation~1) reduces peak perplexity by 64\% versus reactive triggering on distinct-1 (generation~2).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:99:\label{fig:intervention}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:104:\caption{Summary of detection outcomes across contamination levels (Pythia-410M, seed~42, $T{=}10$, fp32). PermG: forward FDR-significant pairs; $K{\geq}3$: consensus pairs (of 8 canary$\to$downstream pairs).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:123:\caption{Consensus threshold operating characteristics ($K \in \{2,3,4,5\}$). FPR: null-control rate (9 seeds, 54 pairs); TPR: detection rate at selected $\alpha$ levels (Pythia-410M, $T{=}10$, fp32). $K{=}3$ balances FPR control (11.1\%) against detection power (75\% at $\alpha{=}1.0$); $K{=}4$ eliminates false positives but reduces TPR to ${\leq}25\%$.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex:19:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex:22:\caption{Metric trajectories at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead across all four seeds (shaded: inter-seed range). This pattern corresponds to 24/24 forward and 0/24 reverse FDR-significant pairs.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex:23:\label{fig:metric_trajectory}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex:42:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex:46:\caption{PermG forward detection rate across 13 contamination levels (Pythia-410M, fp32, direction-checked). Four regimes: blind ($\alpha \leq 0.45$, 0/8), onset ($\alpha{=}0.50$, 6/8), synchronous dip ($\alpha{=}0.60$, 0/8), and detection ($\alpha \geq 0.75$, 0--6/8).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex:47:\label{fig:regime_map}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex:53:\caption{Forward-direction FDR significance rates (\%) across contamination levels (Pythia-410M, seed~42, fp32, direction-checked). Each cell: fraction of 8 validated pairs at BH-corrected significance ($q{=}0.05$). PermG achieves the lowest null-control FPR among directional methods (11.1\% pooled across 6 seeds) with consistent detection at $\alpha \geq 0.50$.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex:88:\caption{Cross-architecture PermG forward detection ($\alpha{=}1.0$). Detection (${\geq}$6/8) confirmed in 11/15 conditions (73\%) across six model families, scales from 345M to 6.9B, and two domains.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex:15:\caption{Detection landscape overview (Pythia-410M, fp32, PermG direction-checked).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex:20:\label{fig:hero}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex:30:\caption{Analytical framework overview. (a)~Iterative contamination loop: each generation fine-tunes on an $\alpha$-fraction synthetic mixture, producing canary (entropy, ECE) and downstream (distinct-$n$, perplexity) time series. (b)~Multi-Method Consensus Test: five detection methods weighted by inverse null-control FPR converge to a $K{\geq}3$ consensus decision. (c)~Detection regimes in the $(\alpha, T)$ plane: the boundary $\alpha_c(T)$ separates blind and detection zones, with onset and sync-dip as transitional regions.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex:31:\label{fig:framework}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56b1dde4-f608-4734-b23a-89e13a37073d",
  "isSidechain": true,
  "promptId": "51e3df65-9561-4454-8292-70ea3a87414d",
  "agentId": "aac173aafa6353ad3",
  "type": "user",
  "uuid": "a5f970b7-2e32-4b2a-8d8a-b8f567e87b32",
  "sourceToolAssistantUUID": "56b1dde4-f608-4734-b23a-89e13a37073d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-24T18:28:27.248Z_

Now let me get line counts for each file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5f970b7-2e32-4b2a-8d8a-b8f567e87b32",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsFWS6EpJqhF1e39X8q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c56120b2-97ad-4037-a254-d16a92eae308",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ETd5k4zFeJQAKkiMtryE27",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 10781,
      "cache_read_input_tokens": 65446,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10781
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 101,
          "cache_read_input_tokens": 65446,
          "cache_creation_input_tokens": 10781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10781,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-24T18:28:27.316Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VuXiws9ZsQnYXyKDUYrZms`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c56120b2-97ad-4037-a254-d16a92eae308",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsFWS6EpJqhF1e39X8q",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "90154ff1-ba6f-4e6d-b5b6-b7ee24656505",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ETd5k4zFeJQAKkiMtryE27",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 10781,
      "cache_read_input_tokens": 65446,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10781
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 101,
          "cache_read_input_tokens": 65446,
          "cache_creation_input_tokens": 10781,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10781,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-24T18:28:27.374Z_

<details><summary>↩ Tool result · `toolu_01VuXiws9ZsQnYXyKDUYrZms`</summary>

```text
     7 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex
  1456 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex
    38 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex
    16 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex
    29 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex
    35 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion_reframe.tex
    12 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ethics.tex
   135 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex
   131 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex
    45 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/intro_reframe.tex
    38 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex
     7 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex
    43 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex
    99 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex
    61 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex
    14 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex
    22 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work_reframe.tex
    21 /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/theory.tex
  2209 total
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "90154ff1-ba6f-4e6d-b5b6-b7ee24656505",
  "isSidechain": true,
  "promptId": "51e3df65-9561-4454-8292-70ea3a87414d",
  "agentId": "aac173aafa6353ad3",
  "type": "user",
  "uuid": "ae3e91f4-1dca-48ee-b796-e7d103d5cb4e",
  "sourceToolAssistantUUID": "90154ff1-ba6f-4e6d-b5b6-b7ee24656505",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-24T18:28:28.916Z_

Let me search for all figures more comprehensively:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae3e91f4-1dca-48ee-b796-e7d103d5cb4e",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsFe5xtiSC1Rig8moFA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4c98560b-5986-40f0-b8b4-c01b3c447133",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EvYoPiwJhcFbaBGRZWFse4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 877,
      "cache_read_input_tokens": 76227,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 877,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-24T18:28:29.217Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UeUDZwWSP5doZgxNPsKMih`</summary>

```json
{
  "command": "grep -h \"\\\\\\\\label{fig:\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/*.tex | sort | uniq"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c98560b-5986-40f0-b8b4-c01b3c447133",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsFe5xtiSC1Rig8moFA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ec207551-a24f-4ea2-99da-228c996ae6aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EvYoPiwJhcFbaBGRZWFse4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 877,
      "cache_read_input_tokens": 76227,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 877
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 113,
          "cache_read_input_tokens": 76227,
          "cache_creation_input_tokens": 877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 877,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-24T18:28:29.286Z_

<details><summary>↩ Tool result · `toolu_01UeUDZwWSP5doZgxNPsKMih`</summary>

```text
\label{fig:14b_phase}
\label{fig:ar1_diagnostic}
\label{fig:bootstrap_fpr}
\label{fig:cascade_onset}
\label{fig:channel_effect}
\label{fig:cross_arch_combined}
\label{fig:cross_arch_heatmap}
\label{fig:cusum_monitoring}
\label{fig:detection_surface}
\label{fig:fpr_combined}
\label{fig:fpr_sensitivity}
\label{fig:framework}
\label{fig:hero}
\label{fig:intervention}
\label{fig:metric_trajectory}
\label{fig:null_fpr_diagnostic}
\label{fig:per_method_phase}
\label{fig:permg_power}
\label{fig:regime_map}
\label{fig:shapley}
\label{fig:spec_curve}
\label{fig:window_sensitivity}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ec207551-a24f-4ea2-99da-228c996ae6aa",
  "isSidechain": true,
  "promptId": "51e3df65-9561-4454-8292-70ea3a87414d",
  "agentId": "aac173aafa6353ad3",
  "type": "user",
  "uuid": "6a354538-8511-4f2f-a585-d5e57f5fadd4",
  "sourceToolAssistantUUID": "ec207551-a24f-4ea2-99da-228c996ae6aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-24T18:28:31.582Z_

Perfect! Now let me compile the comprehensive analysis. Let me verify which files contain which figures:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a354538-8511-4f2f-a585-d5e57f5fadd4",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsFnMo1ZgHBdqEPUG2C",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fa5036b7-a4f6-4ebf-8297-8fd9e105c598",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018wySdHZNyikBUcxDtycAaV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 354,
      "cache_read_input_tokens": 77104,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 354,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-24T18:28:32.175Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VvgAtvgnC12J3UZZN1okCe`</summary>

```json
{
  "command": "for fig in hero metric_trajectory intervention window_sensitivity spec_curve cascade_onset; do echo \"=== fig:$fig ===\"; grep -l \"\\\\\\\\label{fig:$fig}\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/*.tex; done"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa5036b7-a4f6-4ebf-8297-8fd9e105c598",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsFnMo1ZgHBdqEPUG2C",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3148bed4-6b00-4fc7-8867-968efbbbb8a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_018wySdHZNyikBUcxDtycAaV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 354,
      "cache_read_input_tokens": 77104,
      "output_tokens": 151,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 354
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 151,
          "cache_read_input_tokens": 77104,
          "cache_creation_input_tokens": 354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 354,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-24T18:28:32.269Z_

<details><summary>↩ Tool result · `toolu_01VvgAtvgnC12J3UZZN1okCe`</summary>

```text
=== fig:hero ===
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex
=== fig:metric_trajectory ===
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex
=== fig:intervention ===
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex
=== fig:window_sensitivity ===
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex
=== fig:spec_curve ===
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex
=== fig:cascade_onset ===
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3148bed4-6b00-4fc7-8867-968efbbbb8a5",
  "isSidechain": true,
  "promptId": "51e3df65-9561-4454-8292-70ea3a87414d",
  "agentId": "aac173aafa6353ad3",
  "type": "user",
  "uuid": "1f82bbfa-c19c-4b68-bf4f-d6d74620f35e",
  "sourceToolAssistantUUID": "3148bed4-6b00-4fc7-8867-968efbbbb8a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-24T18:29:22.657Z_

Excellent. Now let me provide the comprehensive analysis:

## Paper Space Optimization Analysis

### Line Counts by Section
- **introduction.tex**: 38 lines
- **related_work.tex**: 14 lines
- **method.tex**: 99 lines
- **experiments.tex**: 135 lines
- **discussion.tex**: 29 lines
- **conclusion.tex**: 16 lines
- **limitations.tex**: 7 lines (very brief)
- **appendix.tex**: 1,456 lines (heavily loaded with tables, figures, robustness checks)

**Total main text**: 338 lines | **Total with appendix**: 1,794 lines

---

### Related Work Structure
The related_work.tex uses **paragraph-level organization** rather than formal subsections:
1. **"Model collapse and monitoring"** - covers formalization, theoretical analyses, monitoring metrics, and positions own contribution (7 sentences)
2. **"Phase transitions and lead-lag methodology"** - covers critical mixture ratios, Granger causality, non-stationary series issues, and multiverse analysis perspective (4 sentences)

Total: 2 paragraph blocks, 15 lines. This is **extremely compressed** for a related work section. Most papers have 10-15 dedicated subsections; this has essentially none (just topic paragraphs).

---

### Figures in Main Text (5 total)

| Label | File | Description | Narrative Value |
|-------|------|-------------|-----------------|
| **fig:hero** | introduction.tex | 4-panel composite: (a) FDR-significant phase diagram across contamination α and window T with fitted boundary; (b) Dose-response sigmoid with regime bands; (c) Method sensitivity comparison showing 5 methods' FPR rates; (d) Cross-architecture validation across 15 model-seed conditions | ESSENTIAL - Leads all three main contributions; appears in introduction |
| **fig:metric_trajectory** | experiments.tex | Token entropy and distinct-1 time series across 4 seeds at α=1.0, showing canary lead by 1 generation | SUPPORTING - Illustrates the cascade pattern quantified in Experiments |
| **fig:intervention** | experiments.tex | Line plot comparing entropy-triggered vs. distinct-1-triggered cessation, showing 64% perplexity reduction | PROOF-OF-CONCEPT - Demonstrates practical application |
| **Table: tab:summary_detection** | experiments.tex (line 102-119) | Detection outcomes table across α levels | STRUCTURAL - Summarizes regime results |
| **Table: tab:mmct_k_operating** | experiments.tex (line 121-135) | Operating characteristics for K∈{2,3,4,5} | METHODOLOGICAL - Shows K=3 choice |

---

### Figures in Appendix (23 total)

**Early Validation & Robustness** (Appendix A-C):

| Label | Location | Description | Add to Main Text? |
|-------|----------|-------------|------------------|
| **fig:window_sensitivity** | app:window_sensitivity | Consensus stability across T_min∈{5,...,10} with dual panels (left: K≥3 count, right: per-method detection) | MAYBE - Supports claim that T=10 provides ample power, but specialized audience (methodologists only) |
| **fig:spec_curve** | app:spec_curve | 1,160 analytical specifications; lines trace detection across α; shows 0%→75% jump is robust | STRONG CANDIDATE - Demonstrates specification invariance of main finding; highly persuasive for rigor; ~1/3 page |
| **fig:per_method_phase** | app:dose_response table region | Per-method heatmaps (5 methods × 2 window sizes) showing PermG sharpness vs. others' diffuse profiles | CANDIDATE - Visually supports method sensitivity claim but partially redundant with fig:hero(c) |

**Method Sensitivity Deep-Dive** (Appendix D):

| Label | Location | Description | Add to Main Text? |
|-------|----------|-------------|------------------|
| **fig:permg_power** | app:power_analysis | Power curves β_50 vs. T; shows why T≤8 underpowered, T=10 minimum justified | WEAK - Highly technical; relegated to appendix appropriately; adds <1/3 page if included |
| **fig:null_fpr_diagnostic** | app:fpr_independence | Per-seed FPR bars for 6 null seeds across 5 methods | WEAK - Redundant with table; bar chart doesn't add info beyond numbers |
| **fig:bootstrap_fpr** | app:fpr_independence | Bootstrap distribution of PermG FPR; CI [2.1%, 17.9%] | WEAK - Confidence interval already stated in main text; visual doesn't materially aid understanding |

**Theory & Boundary** (Appendix E):

| Label | Location | Description | Add to Main Text? |
|-------|----------|-------------|------------------|
| **fig:detection_surface** | app:alpha_c_proof | 3D-like surface plot over α×T space; contours at 25%, 50%, 75% detection | STRONG CANDIDATE - Directly visualizes the power-law boundary α_c(T); synthesizes Fig 1(a) and Section 3 results; ~1/2 page; highly compelling for demonstrating T-dependence |
| **fig:ar1_diagnostic** | app:nonstationarity | AR(1) coefficients raw vs. first-differenced; shows why differencing necessary | WEAK - Technical appendix material; appropriate where it is |

**Cross-Architecture Validation** (Appendix F):

| Label | Location | Description | Add to Main Text? |
|-------|----------|-------------|------------------|
| **fig:14b_phase** | app:cross_arch_table | Pythia-1.4B phase diagram (6-pair basis); per-seed detection fractions | CANDIDATE - Shows detection generalizes to 1.4B scale; ~1/3 page; but introduces second model only for one comparison |
| **fig:cross_arch_heatmap** | app:generalization | Bar chart: forward detection rates across 15 conditions (5 families, 345M–6.9B) with dark/light bars | STRONG CANDIDATE - Directly supports "11 of 15 confirmed" claim; ~1/4 page; shows both PermG and consensus; high narrative impact |
| **fig:cross_arch_combined** | app:generalization | Composite: (a) heatmap as above, (b) FPR comparison bars | REDUNDANT IF (a) ADDED - Don't include both |

**Cascade Analysis** (Appendix G):

| Label | Location | Description | Add to Main Text? |
|-------|----------|-------------|------------------|
| **fig:cascade_onset** | app:moment_cascade | Timeline of onset generations (5% threshold); Phase 1 (blue, gen 1: H, ECE), Phase 2 (orange, gen 2: distinct-n) | STRONG CANDIDATE - Visually proves cascade ordering; ~1/2 page; directly supports Principle 1 and 2; alternative to current fig:metric_trajectory (which is less structured) |

**Sequential Monitoring & Intervention** (Appendix H):

| Label | Location | Description | Add to Main Text? |
|-------|----------|-------------|------------------|
| **fig:cusum_monitoring** | app:csmp | CUSUM vs. simple threshold monitoring; trajectory plots at two α levels; shows equivalence | WEAK - Intervention already shown via fig:intervention; this is methodological detail; appropriate in appendix |

**Effect-Size & Partial Correlation** (Appendix I):

| Label | Location | Description | Add to Main Text? |
|-------|----------|-------------|------------------|
| **fig:channel_effect** | app:channel_effect_size | Dual panels: (a) correlation retention by channel, (b) Granger F asymmetry (diversity 6× > perplexity) | CANDIDATE - Explains the spurious regression finding; ~1/3 page; somewhat technical but important for methodology section |
| **fig:shapley** | app:shapley | Shapley value decomposition FPR/FNR bars per method; combined score | WEAK - Specialized for method comparison; bar chart format less persuasive than table |

**Results Summaries** (Appendix J):

| Label | Location | Description | Add to Main Text? |
|-------|----------|-------------|------------------|
| **fig:regime_map** | experiments_reframe.tex | PermG detection rate across 13 α levels (4 regimes marked) | MODERATE - Equivalent to main text dose-response but different layout; used in alternate reframing |

---

### Compression Opportunities (Ranked by Efficiency)

**Quick Wins (save 2-3 pages)**:
1. **Compress related_work.tex** (currently 14 lines)
   - Currently: 2 topic paragraphs
   - Potential: Merge into single 7-line dense paragraph OR split into 3 named subsections with 2-3 sentences each
   - Save: ~0.3 pages (unlikely to be significant)

2. **Remove redundant table descriptions**
   - Tables tab:drift_summary, tab:distinct3_drift appear with lengthy captions in appendix
   - Save: ~0.2 pages (minimal—these are data summaries needed)

3. **Consolidate discussion.tex (currently 29 lines across multiple paragraphs)**
   - Appears split between main discussion and conclusion
   - Merge: scope/failure modes + Granger limitations + anomaly discussion → single 2-column discussion section
   - Save: ~0.5 pages

**Medium Gains (save 1-2 pages)**:
4. **Move bottom-tier appendix tables to supplementary material**
   - Tables like tab:window_sensitivity, tab:permutation_count_stability are robustness checks
   - These provide confidence but aren't load-bearing for narrative
   - Save: ~1 page

5. **Replace 4 separate FPR/power/AR diagnostic tables with 1 composite figure**
   - Currently: tab:nperm_stability (line 116), tab:fpr_sensitivity (line 139), tab:fdr_gradient (line 163) are all single-row or 3-row tables
   - Consolidate: Create 1 fig with 3 subpanels (permutation stability, FDR sensitivity, AR diagnostic)
   - Save: ~0.5 pages

**Strategic Removals (save 2-3 pages)**:
6. **Demote Toda–Yamamoto results** (currently Appendix app:method_comparison, Table at line 457)
   - TY is marked "under verification" and contributes minimally to narrative
   - Move TY columns to supplementary CSV; keep only PermG, DiffXCorr, Threshold, NaiveXCorr in main appendix
   - Save: ~0.4 pages (fewer rows/columns across multiple tables)

7. **Consolidate CUSUM vs. simple threshold analysis** (currently app:csmp with fig:cusum_monitoring + 3 tables)
   - Finding: "simple threshold performs as well"
   - Reduce: Keep Table tab:csmp_comparison (results), remove tab:csmp_calibration (derivation), summarize fig:cusum_monitoring to single panel
   - Save: ~0.7 pages

**Large Impact (save 3-5 pages)**:
8. **Move cross-domain C4 results to supplementary**
   - Currently: mentioned in text + tab:generalization + cross-domain notes in app:extended_discussion
   - These results show "domain matters" but aren't central to paper narrative (main claims use WikiText)
   - Move: Keep statement "C4 exhibits stronger detection" in main text; move tab:c4 results to supp
   - Save: ~0.4 pages

9. **Streamline Transfer Entropy analysis** (currently app:transfer_entropy with lengthy KNN-based subsection)
   - Key finding: "0/192 significant, confirming linear methods sufficient"
   - Reduce: Single table + 1 sentence summary; remove KNN subsection (line 246-251)
   - Save: ~0.5 pages

10. **Reduce change-point detection section** (currently app:change_point with 3 tables + lengthy discussion)
    - Finding: "ordering reversal supports Granger-precedence; individual significance unreliable"
    - Current: Detailed null/treatment comparisons with effect sizes
    - Reduce: Keep single Table tab:cp_ordering (key result), move detailed null/treatment tables to supp
    - Save: ~0.8 pages

---

### Appendix Subsection Structure (Currently)
The appendix is organized chronologically by experiment rather than thematically:
- A. Training Details & Metric Drift
- B. Distinct-3 Results
- C. Observation Window Sensitivity
- D. Robustness Checks (permutation count, FDR threshold)
- E. Specification Curve
- F. Transfer Entropy & KNN-based TE/MI
- G. Change-Point Detection
- H. CUSUM Monitoring
- I. Background & Notation
- J. MMCT Algorithm
- K. Method Comparison Table
- L. Extended Discussion
- M–N. Pythia-1.4B Phase Diagram & Tables
- O–U. Per-method detection, Shaplay decomposition, null FPR diagnostics, power analysis, AR diagnostics, channel effect, MI analysis, partial correlation, cascade onset, task degradation, cross-architecture validation, etc.

**Issue**: Readers navigating for "all power analysis" or "all FPR results" must jump across sections. Some reorganization would help, but the current structure follows experimental workflow (acceptable for long papers).

---

### Compressibility Summary

**Most Compressible Sections** (by % reduction without loss):
1. **Related Work** - 14 lines (33% compressible by merging paragraphs into 1–2 dense sections)
2. **Limitations** - 7 lines (already minimal; 20% compressible by deduplication with discussion)
3. **Appendix robustness tables** - ~3 pages (20% compressible by consolidation or supplementary material)
4. **Discussion & Conclusion** - 45 lines combined (15% compressible by merging overlapping scope/failure mode discussions)

**Least Compressible**:
1. **Method section** (99 lines) - Each subsection load-bearing (cascade theory, method comparison, consensus details all cited in intro)
2. **Experiments** (135 lines) - Dense with multiple regimes, each requires brief exposition
3. **Cross-architecture results** - Expanding, not compressible (11/15 conditions require space to list)

---

### Figure Promotion Recommendations

**High-Impact Promotions** (clear narrative value):

| Current Location | Recommendation | Rationale | Est. Space Needed |
|-----------------|-----------------|-----------|------------------|
| fig:spec_curve (app:spec_curve) | Move to Method section after MMCT discussion | Demonstrates 0%→75% jump robust across 1,160 specs; directly answers "is this just methodology choice?" | 0.3 pages (1-column) |
| fig:detection_surface (app:alpha_c_proof) | Move to Theory subsection (§Method) or after Results | Visualizes α_c(T) power-law boundary compactly; shows T-dependence of detection threshold | 0.35 pages (1-column) |
| fig:cascade_onset (app:moment_cascade) | Replace or augment fig:metric_trajectory in Experiments | More structured timeline showing Phase 1/2/3 ordering; quantifies Principles 1–2 better than current trajectory | 0.5 pages (1-column); trade-off: remove or demote fig:metric_trajectory |
| fig:cross_arch_heatmap (app:generalization) | Promote to Experiments or Results heading | Directly shows "11/15 confirmed"; currently buried in appendix table; high visual impact | 0.25 pages (0.5-column bar chart) |

**Modest Promotions** (supporting role):

| Current Location | Recommendation | Rationale | Est. Space Needed |
|-----------------|-----------------|-----------|------------------|
| fig:14b_phase (app:cross_arch_table) | Keep in appendix; reference in main text | Shows 1.4B scale generality; useful but secondary to overall cross-arch pattern | 0.5 pages |
| fig:per_method_phase (heatmap region) | Conditional: keep only if fig:hero(c) removed | Method comparison is important but fig:hero(c) already shows it; avoid duplication | Depends on fig:hero revision |
| fig:channel_effect (app:channel_effect_size) | Promote to Method section as subsection | Explains why diversity-only canary claim (removes spurious perplexity); currently logic is in text only | 0.3 pages |

---

### Summary for Venue Constraints

Assuming **9-page NeurIPS/ICLR limit** (typical):

**Current state**: ~10.5 pages (estimated)
- Main: 2.5 pp (intro 0.3, related 0.1, method 0.6, expt 0.9, disc/concl 0.3, limits 0.05)
- Appendix: 8.0 pp

**To reach 9 pages**:
- Compress Related Work → 1/4 page (save 0.1 pp)
- Merge Discussion/Conclusion, demote some limitations → save 0.2 pp
- Promote 2–3 key figures (fig:spec_curve, fig:detection_surface, fig:cross_arch_heatmap) at expense of appendix text → net 0 pp
- Move CUSUM, Transfer Entropy, some per-method tables to supplement → save 1.5 pp
- **Total reachable: ~8.5 pp** ✓

**Key insight**: Space isn't the limiting factor if appendix is streamlined. The paper is inherently long because it documents 5 methods × 13 contamination levels × multiple seeds × robustness checks. That scope justifies the length.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f82bbfa-c19c-4b68-bf4f-d6d74620f35e",
  "isSidechain": true,
  "agentId": "aac173aafa6353ad3",
  "requestId": "req_011CbMsG1XZM8MY3Zgytp2im",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "43cf3746-d0c2-48fb-9a2c-ffdcc0b9f172",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/director_6dc4a1c8",
  "sessionId": "42bf092e-a344-4684-8cb8-222ac50c19a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MmoR4qYzU3dB7hJmbfBmCU",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 489,
      "cache_read_input_tokens": 77458,
      "output_tokens": 4417,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 489
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4417,
          "cache_read_input_tokens": 77458,
          "cache_creation_input_tokens": 489,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 489,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
