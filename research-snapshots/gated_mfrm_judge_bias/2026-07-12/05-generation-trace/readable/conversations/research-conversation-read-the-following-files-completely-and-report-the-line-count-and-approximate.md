# Research conversation: Read the following files completely and report the line count and approximate word count for each: 1. /home/ubuntu/.agen

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-af0b5f1dbbb0ecf84.jsonl`
- **Structured JSON:** [`db26337bb2875e93c410.json`](../../sessions/db/db26337bb2875e93c410.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-25T15:53:57.466Z_

Read the following files completely and report the line count and approximate word count for each:
1. /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex
2. /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex
3. /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex
4. /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex
5. /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex
6. /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex
7. /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex
8. /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex
9. /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex

For each file, report: filename, total lines, and a brief summary of the content structure (subsections, tables, figures). Also note any content that seems like it could be moved to an appendix (detailed proofs, full result tables, verbose derivations).


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "0b26d185-bf84-492a-b63d-76b41c6c458f",
  "agentId": "af0b5f1dbbb0ecf84",
  "type": "user",
  "uuid": "cce7d03e-6b85-4829-870f-dcea7f3c691f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T15:53:59.694Z_

I'll read all these files and provide you with a detailed analysis of their line counts, word counts, and content structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cce7d03e-6b85-4829-870f-dcea7f3c691f",
  "isSidechain": true,
  "agentId": "af0b5f1dbbb0ecf84",
  "requestId": "req_011CbPZHEh1e3pX9k1NmQyqS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1504ec05-08fc-46fe-be7a-b4155195a498",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GLNqLaD9wLi5XynX4wMkAr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28016,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28016,
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

_source line 3 · 2026-05-25T15:53:59.909Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TfDKSwKmjHgcJAjVw7Mq5T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1504ec05-08fc-46fe-be7a-b4155195a498",
  "isSidechain": true,
  "agentId": "af0b5f1dbbb0ecf84",
  "requestId": "req_011CbPZHEh1e3pX9k1NmQyqS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "79fc4292-5424-4e0a-b6ed-23ae6043b3af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GLNqLaD9wLi5XynX4wMkAr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28016,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28016,
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

### Tool result

_source line 4 · 2026-05-25T15:53:59.919Z_

<details><summary>↩ Tool result · `toolu_01TfDKSwKmjHgcJAjVw7Mq5T`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When multiple LLM judges evaluate model responses on a benchmark, their scores are shaped by at least three forces: the model's genuine ability, the judge's own scoring tendency, and any advantage the model gained from encountering benchmark items during training. These three signals are entangled in every observation. The evaluation community has developed separate tools for the latter two distortions: judge bias correction methods calibrate inter-judge differences \citep{cyclicjudge2026, uda2026}, while contamination detection tools flag or adjust for memorized items \citep{constat2024, dcr2025, logprober2024}. A practitioner who faces both problems must apply these corrections sequentially. This paper shows that sequential correction produces systematically biased rankings, not merely noisy ones.
5	
6	\begin{figure*}[t]
7	\centering
8	\includegraphics[width=\textwidth]{fig1_framework_v2}
9	\caption{(a)~Sequential pipelines address judge bias and contamination independently; omitted variable bias confounds the unmodeled facet into ability estimates. (b)~G-MFRM three-stage joint calibration: Stage~1 fits a standard MFRM for initial estimates $(\hat{\theta}, \hat{b}, \hat{d})$; Stage~2 estimates per-item exposure $e_i$ from external evidence (reference model anchoring, cross-model agreement, and optionally LogProber); Stage~3 performs joint MCMC inference with $e_i$ fixed, recovering contamination-corrected ability $\hat{\theta}_n$, contamination susceptibility $c_n$, and judge severity $d_j$.}
10	\label{fig:framework}
11	\end{figure*}
12	
13	We formalize this failure as an omitted variable bias (OVB) problem \citep{angrist2009mostly}. Consider a model that has memorized some benchmark items and a judge that scores more strictly than average. A bias-only correction adjusts for the strict judge but leaves the contamination signal untouched; the inflated scores on memorized items get absorbed into the model's estimated ability. Conversely, a contamination-only adjustment removes the memorization signal but conflates systematic scoring differences with contamination variation. In both cases, the omitted facet biases the modeled one. Within the Many-Facet Rasch Model (MFRM) framework \citep{linacre1989mfrm}, we prove this bias is directional: contaminated models are systematically overestimated under bias-only correction, and the bias persists regardless of which correction comes first (Section~\ref{sec:confounding}).
14	
15	Resolving this confounding requires joint estimation. We propose the Gated Many-Facet Rasch Model (G-MFRM), which extends MFRM with a multiplicative gating term $c_n \cdot e_i$ for contamination susceptibility, inspired by Doubly-Gated Item Response Theory \citep{shu2013dgirt}. Through a three-stage calibration procedure with externally anchored per-item exposure indicators (Figure~\ref{fig:framework}), G-MFRM simultaneously recovers model ability, item difficulty, judge severity, and contamination susceptibility. We prove that external anchoring of exposure is both necessary and sufficient for parameter identification under standard multi-judge designs (Theorem~\ref{thm:sufficient}), and derive error propagation bounds for the staged estimation.
16	
17	In synthetic experiments ($N = 50$ models, 20 seeds), G-MFRM reduces ability root mean squared error (RMSE) by 51.2\% relative to sequential estimation ($p < 0.001$) and recovers contamination susceptibility with 40\% lower error than binary gating. On Arena-Hard \citep{li2024arenahard} with 9 LLM judges, G-MFRM identifies per-model contamination susceptibility that tracks model age: older models (GPT-3.5-Turbo, GPT-4-0613) exhibit 4--6$\times$ higher susceptibility than recent models (GPT-4o). Judge severity profiles reveal that proprietary judges score consistently more strictly, with the severity range spanning 1.34 logits. Leave-one-out cross-validation strongly favors joint estimation ($|\Delta\mathrm{ELPD}/\mathrm{SE}| = 5.9$; stacking weight 1.0). Our contributions are:
18	\begin{enumerate}
19	    \item A formal analysis of judge-contamination confounding as omitted variable bias, proving that sequential correction cannot resolve the confounding under non-orthogonality (Section~\ref{sec:confounding}).
20	    \item The G-MFRM framework with identifiability guarantees and error propagation bounds for staged estimation (Section~\ref{sec:method}).
21	    \item The first joint diagnostic of per-model contamination susceptibility and per-judge severity within a measurement-theoretic framework, validated on Arena-Hard (Section~\ref{sec:experiments}).
22	\end{enumerate}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "79fc4292-5424-4e0a-b6ed-23ae6043b3af",
  "isSidechain": true,
  "promptId": "0b26d185-bf84-492a-b63d-76b41c6c458f",
  "agentId": "af0b5f1dbbb0ecf84",
  "type": "user",
  "uuid": "2cf7e9c9-9725-4bbb-9481-5a6ea195654e",
  "sourceToolAssistantUUID": "79fc4292-5424-4e0a-b6ed-23ae6043b3af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T15:54:00.223Z_

<details open><summary>🔧 Tool call — Read · `toolu_01P7v2m99SrscvfjgLc1wuMi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cf7e9c9-9725-4bbb-9481-5a6ea195654e",
  "isSidechain": true,
  "agentId": "af0b5f1dbbb0ecf84",
  "requestId": "req_011CbPZHEh1e3pX9k1NmQyqS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2edf5c23-282b-4f4a-8346-7d1f3f600e24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GLNqLaD9wLi5XynX4wMkAr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28016,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28016,
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

### Tool result

_source line 6 · 2026-05-25T15:54:00.229Z_

<details><summary>↩ Tool result · `toolu_01P7v2m99SrscvfjgLc1wuMi`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Judge Bias in LLM Evaluation.}
5	LLM-as-a-judge evaluations exhibit position bias \citep{wang2024positionbias}, self-preference \citep{panickssery2024selffavor}, and other cognitive biases \citep{koo2024cobbler, ye2024justice, bavaresco2025judgebench}; see also \citet{li2024splitmerge} and \citet{fiedler2026bias_uncertainty}. On the correction side, CyclicJudge \citep{cyclicjudge2026} eliminates average bias via round-robin assignment, and UDA \citep{uda2026} learns a neural K-factor reducing inter-judge deviation by 63.4\%. All of these methods model only the judge facet, absorbing contamination effects into ability estimates (Section~\ref{sec:confounding}).
6	
7	\paragraph{Benchmark Contamination Detection and Avoidance.}
8	Detection methods include performance-based tests \citep{constat2024}, unified contamination metrics \citep{dcr2025}, token-level log-probability probes \citep{logprober2024, mink2024}, and guided prompting \citep{golchin2024timetravel, oren2024proving}; see also \citet{deng2024contamination, sainz2023contamination}. \citet{preference_leakage2026} identify judge-side preference leakage, complementary to G-MFRM's examinee-side focus. Avoidance strategies include dynamic benchmarks \citep{livebench2025}, private evaluation \citep{truce2024}, and subset selection \citep{polo2024tinybenchmarks}. G-MFRM instead corrects for residual contamination while simultaneously modeling judge effects.
9	
10	\paragraph{Item Response Theory (IRT) and MFRM for LLM Evaluation.}
11	IRT has been applied to NLP leaderboards for ranking and benchmark analysis \citep{lalor2019irt, rodriguez2021irt, vania2021irt}. The Many-Facet Rasch Model (MFRM) \citep{linacre1989mfrm, linacre1994mfrm} extends IRT to multi-rater settings; \citet{jiao2025mfrm_llm} apply it to LLM judge panels, and \citet{uto2020generalized} and \citet{choi2026irt_judge} propose Bayesian variants; see also \citet{zhou2025psnirt}. The Doubly-Gated IRT (DG-IRT) model of \citet{shu2013dgirt} is the closest antecedent, introducing binary gating for item preknowledge; G-MFRM extends this to continuous exposure, multi-rater designs, and formal identifiability analysis (Section~\ref{sec:model_spec}).
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2edf5c23-282b-4f4a-8346-7d1f3f600e24",
  "isSidechain": true,
  "promptId": "0b26d185-bf84-492a-b63d-76b41c6c458f",
  "agentId": "af0b5f1dbbb0ecf84",
  "type": "user",
  "uuid": "1faf96ec-8c0d-4184-9ab0-84f709d6507c",
  "sourceToolAssistantUUID": "2edf5c23-282b-4f4a-8346-7d1f3f600e24",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T15:54:00.334Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TUYn2gtJ7XBXENTgbZhnpV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1faf96ec-8c0d-4184-9ab0-84f709d6507c",
  "isSidechain": true,
  "agentId": "af0b5f1dbbb0ecf84",
  "requestId": "req_011CbPZHEh1e3pX9k1NmQyqS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0edd0ceb-2c79-4283-9268-a679156c5736",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GLNqLaD9wLi5XynX4wMkAr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28016,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28016,
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

### Tool result

_source line 8 · 2026-05-25T15:54:00.340Z_

<details><summary>↩ Tool result · `toolu_01TUYn2gtJ7XBXENTgbZhnpV`</summary>

```text
1	\section{Confounding in LLM Evaluation}
2	\label{sec:confounding}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth]{fig2_ovb_bias}
7	\caption{Sequential estimation bias ($\hat{\theta}_{\mathrm{seq}} - \theta_{\mathrm{true}}$) versus true contamination susceptibility $c_n$. Pearson $r = 0.86$ ($p < 0.001$) confirms systematic overestimation of contaminated models. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}
8	\label{fig:ovb_bias}
9	\end{figure}
10	
11	The Many-Facet Rasch Model (MFRM) extends classical Rasch measurement to settings with multiple rater facets \citep{linacre1989mfrm, linacre1994mfrm}. Originating in educational measurement, the model treats rater variation as a nuisance facet to be estimated and removed rather than a source of noise to be averaged over. In the LLM evaluation context, where $J$ judges score $N$ models across $I$ items, the MFRM specifies
12	%
13	\begin{equation}
14	\label{eq:mfrm}
15	\log \frac{P(Y_{nij} \geq k \mid \theta_n, b_i, d_j, \tau_k)}{P(Y_{nij} < k \mid \theta_n, b_i, d_j, \tau_k)} = \theta_n - b_i - d_j - \tau_k,
16	\end{equation}
17	%
18	where $Y_{nij}$ is the ordinal rating by judge $j$ for model $n$ on item $i$, $\theta_n$ is the ability of model $n$ ($n = 1, \ldots, N$), $b_i$ is the difficulty of item $i$ ($i = 1, \ldots, I$), $d_j$ is the severity of judge $j$ ($j = 1, \ldots, J$), and $\tau_k$ is the threshold for category $k$. All facets reside on a common logit scale, so model ability is directly comparable after adjustment for item difficulty and judge severity. \citet{jiao2025mfrm_llm} applied this framework to compare ten LLM raters with human experts, showing that MFRM separates genuine ability from systematic judge effects in multi-judge panels.
19	
20	However, standard MFRM assumes that all systematic sources of score variation are captured by the modeled facets. This assumption breaks down when some models have been exposed to benchmark items during training \citep{dcr2025}. Such contamination inflates scores on exposed items through memorization rather than genuine ability. We represent this effect as an interaction $c_n \cdot e_i$, where $c_n \geq 0$ is the contamination susceptibility of model $n$ and $e_i \in [0, 1]$ is the exposure level of item $i$. The complete data-generating process becomes
21	%
22	\begin{equation}
23	\label{eq:full}
24	\eta_{nijk} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i.
25	\end{equation}
26	
27	
28	When a practitioner fits the standard MFRM (Eq.~\ref{eq:mfrm}) to data generated by Eq.~\ref{eq:full}, the contamination term is absent from the estimated model. Its influence does not vanish but is absorbed into the estimated parameters $\tilde{\theta}_n$, $\tilde{b}_i$, and $\tilde{d}_j$, which distorts all downstream inferences.
29	
30	The consequence of this omission can be stated precisely.
31	
32	\begin{observation}[Omitted Variable Bias in MFRM]
33	\label{obs:ovb}
34	Let the full model be $\eta_{nijk} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i$ and the short model omit the contamination term: $\tilde{\eta}_{nijk} = \tilde{\theta}_n - \tilde{b}_i - \tilde{d}_j - \tau_k$. Under a linear approximation to the ordinal logit link \citep{wooldridge2010, angrist2009mostly},\footnote{The OVB formula is exact for linear models. We apply it to the MFRM linear predictor $\eta$, which is an approximation. Synthetic validation confirms the approximation quality: the Pearson correlation between the predicted bias direction and empirical bias reaches $r = 0.86$ ($p < 0.001$), indicating that the linear result accurately characterizes bias direction and relative magnitude.}
35	\begin{equation}
36	\label{eq:ovb}
37	\mathrm{plim}(\tilde{\theta}_n - \theta_n) = \gamma_n \cdot c_n,
38	\end{equation}
39	where $\gamma_n$ depends on the projection of the exposure vector $(e_i)$ onto the design matrix of the short model (explicit form in Appendix~\ref{app:gamma}). The bias is non-zero whenever $\mathrm{Cov}(d_j,\, c_n \cdot e_i) \neq 0$. This captures the confounding component; in the nonlinear MFRM, a specification bias from omitting $c_n \cdot e_i$ persists even at zero covariance (Section~\ref{sec:experiments}).
40	\end{observation}
41	
42	G-MFRM's Stage~3 inference (Eq.~\ref{eq:gmfrm}) uses the full nonlinear ordinal logistic likelihood; the linear approximation serves only as directional motivation. Monte Carlo simulation confirms that bias magnitude is approximately constant across confounding levels $\rho$ (see Appendix~\ref{app:bias_vs_rho}), indicating that omission of $c_n \cdot e_i$---not its correlation with $d_j$---is the primary driver. Neither sequential ordering resolves this: bias-first approaches \citep{cyclicjudge2026} absorb contamination into $\hat{\theta}$, while contamination-first approaches \citep{dcr2025} misattribute judge severity as contamination. Synthetic validation ($N = 50$, $I = 100$, $J = 8$, 20 seeds) confirms directional bias ($r = 0.86$, $p < 0.001$; Figure~\ref{fig:ovb_bias}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0edd0ceb-2c79-4283-9268-a679156c5736",
  "isSidechain": true,
  "promptId": "0b26d185-bf84-492a-b63d-76b41c6c458f",
  "agentId": "af0b5f1dbbb0ecf84",
  "type": "user",
  "uuid": "09e2fdcb-bd6d-484f-97ad-c0f3817f3dc5",
  "sourceToolAssistantUUID": "0edd0ceb-2c79-4283-9268-a679156c5736",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T15:54:00.545Z_

<details open><summary>🔧 Tool call — Read · `toolu_016f7zue6PBWPfYWN1RXHN9s`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09e2fdcb-bd6d-484f-97ad-c0f3817f3dc5",
  "isSidechain": true,
  "agentId": "af0b5f1dbbb0ecf84",
  "requestId": "req_011CbPZHEh1e3pX9k1NmQyqS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "84b70030-f480-4b9a-8d8e-81ab0b939dac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GLNqLaD9wLi5XynX4wMkAr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28016,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28016,
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

### Tool result

_source line 10 · 2026-05-25T15:54:00.552Z_

<details><summary>↩ Tool result · `toolu_016f7zue6PBWPfYWN1RXHN9s`</summary>

```text
1	\section{The G-MFRM Framework}
2	\label{sec:method}
3	
4	\begin{table}[t]
5	\centering
6	\small
7	\begin{tabular}{lcccc}
8	\toprule
9	$\sigma$ & $\theta$-RMSE & $\Delta\theta$\% & $c_n$-RMSE & $\Delta c_n$\% \\
10	\midrule
11	0.0 & 0.128 $\pm$ 0.018 & --- & 0.533 $\pm$ 0.187 & --- \\
12	0.1 & 0.130 $\pm$ 0.018 & +1.4 & 0.545 $\pm$ 0.192 & +2.3 \\
13	0.2 & 0.135 $\pm$ 0.018 & +5.9 & 0.575 $\pm$ 0.198 & +7.9 \\
14	0.5 & 0.175 $\pm$ 0.027 & +36.9 & 0.842 $\pm$ 0.281 & +57.9 \\
15	\bottomrule
16	\end{tabular}
17	\caption{Error propagation robustness (exp-012). Ability RMSE degrades by less than 6\% when exposure noise $\sigma \leq 0.2$, matching the theoretical prediction. Contamination estimates are more sensitive due to multiplicative coupling with $e_i$.}
18	\label{tab:error_prop}
19	\end{table}
20	
21	Section~\ref{sec:confounding} established that omitting contamination from the measurement model produces directional bias in ability estimates (Observation~\ref{obs:ovb}). We now introduce the Gated Many-Facet Rasch Model (G-MFRM), which jointly estimates ability, judge severity, and contamination susceptibility within a single measurement framework. The key design choices, staged estimation with externally fixed exposure and a hierarchical HalfNormal prior for the contamination term, are motivated by the identifiability analysis in \S\ref{sec:identifiability} and the error propagation bounds in \S\ref{sec:error_prop}.
22	
23	\subsection{Model Specification}
24	\label{sec:model_spec}
25	
26	G-MFRM extends the standard MFRM \citep{linacre1989mfrm, linacre1994mfrm} by adding a multiplicative contamination gating term to the linear predictor (Eq.~\ref{eq:mfrm}):
27	%
28	\begin{equation}
29	\label{eq:gmfrm}
30	\log \frac{P(Y_{nij} \geq k)}{P(Y_{nij} < k)} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i,
31	\end{equation}
32	%
33	where all terms carry the definitions from Section~\ref{sec:confounding}. The gating structure $c_n \cdot e_i$ separates the model-specific and item-specific components of contamination: $c_n \geq 0$ captures how much model $n$ benefits from memorized benchmark content, while $e_i \in [0,1]$ quantifies how much of item $i$ has leaked into training corpora. When $c_n = 0$ (a clean model) or $e_i = 0$ (a novel item), the gating term vanishes and Eq.~\ref{eq:gmfrm} reduces to the standard MFRM. This graceful degradation ensures that G-MFRM imposes no distortion on uncontaminated model-item pairs.
34	
35	We enforce non-negativity and sparsity of $c_n$ through a hierarchical HalfNormal prior. A global shrinkage scale $\sigma_c \sim \text{HalfNormal}(1.0)$ controls the overall contamination level, and per-model raw effects $c^{\mathrm{raw}}_n \sim \text{HalfNormal}(1.0)$ are scaled to obtain $c_n = c^{\mathrm{raw}}_n \cdot \sigma_c$. The HalfNormal support restricts $c_n \geq 0$, and the hierarchical structure provides adaptive shrinkage: when the data support low overall contamination, $\sigma_c$ contracts toward zero, pulling all $c_n$ values down. Models with genuine contamination retain large $c^{\mathrm{raw}}_n$ relative to the group. The remaining priors are $\theta_n \sim \mathcal{N}(0, 1)$, $b_i \sim \mathcal{N}(0, 1)$, $d_j \sim \mathcal{N}(0, 0.5)$, and standard uniform on thresholds $\tau_k$.
36	
37	G-MFRM extends the Doubly-Gated IRT model of \citet{shu2013dgirt} from binary gating to continuous exposure and multi-rater designs, and contributes the first formal identifiability conditions for gated IRT parameters (Propositions~\ref{prop:no_new}--\ref{prop:exposure_variation}, Theorem~\ref{thm:sufficient}) and error propagation bounds for staged estimation (\S\ref{sec:error_prop}).
38	
39	\subsection{Staged Estimation}
40	\label{sec:staged}
41	
42	Joint estimation of all parameters in Eq.~\ref{eq:gmfrm}, including $e_i$, would require identifying the bilinear product $c_n \cdot e_i$ from response data alone. This creates a fundamental non-identifiability (Proposition~\ref{prop:exposure_variation}). We resolve this through a three-stage procedure that fixes exposure externally before estimating the contamination parameters.
43	
44	\paragraph{Stage 1: Standard MFRM.} We fit the standard MFRM (Eq.~\ref{eq:mfrm}) via MCMC (NUTS) to obtain initial estimates $(\hat{\theta}, \hat{b}, \hat{d})$. These serve as warm-start values for the sampler in Stage~3 and improve convergence.
45	
46	\paragraph{Stage 2: Exposure estimation.} Per-item exposure $e_i$ is estimated from external evidence independent of the response data. The primary signal is \emph{reference model anchoring} (75\% weight): win-rate residuals against a fixed anchor (gpt-4-0314) flag items where target models outperform difficulty-adjusted expectations. The secondary signal is \emph{cross-model agreement} (25\%): uniformly high scores across diverse architectures suggest exposure rather than easiness. The composite is clipped to $[0, 1]$ and fixed in Stage~3. Estimation is non-circular: $e_i$ is item-level while $c_n$ is model-level, and ablation with 100\% anchoring yields $\rho = 0.998$ (Appendix~\ref{app:weight_robustness}).
47	
48	\paragraph{Stage 3: Joint MCMC.} With $e_i$ fixed, we sample $(\theta_n, b_i, d_j, c_n)$ jointly via the No-U-Turn Sampler (NUTS) \citep{betancourt2015}. The priors are as specified in \S\ref{sec:model_spec}. The hierarchical contamination prior decomposes as
49	%
50	\begin{align}
51	\label{eq:contam_prior}
52	\sigma_c &\sim \text{HalfNormal}(1.0), \quad c^{\mathrm{raw}}_n \sim \text{HalfNormal}(1.0), \nonumber \\
53	c_n &= c^{\mathrm{raw}}_n \cdot \sigma_c,
54	\end{align}
55	%
56	where $\sigma_c$ is a shared global scale that governs the overall contamination magnitude. This non-centered parameterization improves sampler geometry by decoupling the global scale from the per-model effects.
57	
58	Convergence is assessed via rank-normalized split-$\hat{R}$ \citep{vehtari2021rhat} and bulk effective sample size (ESS), with thresholds $\hat{R} < 1.05$ and ESS$_{\mathrm{bulk}} > 100$ following standard practice \citep{gelman2013bda}.\footnote{Synthetic validation with $N = 50$, $I = 100$, $J = 8$ yields satisfactory convergence across all parameters (exp-012). Full diagnostic tables are reported in Section~\ref{sec:experiments}.}
59	
60	
61	\begin{figure}[t]
62	\centering
63	\includegraphics[width=\columnwidth]{forest_dj}
64	\caption{Judge severity estimates ($d_j$) for all nine judges with 95\% credible intervals. Positive values indicate stricter scoring. Proprietary judges (Claude Opus, GPT-5.5) cluster at the strict end; open-source judges (Mistral, LLaMA) are more lenient. The severity range spans 1.34 logits.}
65	\label{fig:judge_severity}
66	\end{figure}
67	
68	\subsection{Identifiability}
69	\label{sec:identifiability}
70	
71	Adding a multiplicative term to a measurement model raises the question of whether the new parameters can be separated from the existing ones. We establish that fixing $e_i$ externally is both necessary and sufficient for identification. All proofs assume the standard location constraint $\sum_n \theta_n = 0$.
72	
73	\begin{proposition}[No New Indeterminacy]
74	\label{prop:no_new}
75	When $e_i$ is fixed externally, the gating term $c_n \cdot e_i$ introduces no additional location or scale indeterminacy beyond that already present in the standard MFRM.
76	\end{proposition}
77	
78	\begin{proposition}[Exposure Variation Necessary]
79	\label{prop:exposure_variation}
80	If $e_i = e$ for all $i$ (constant exposure), then $c_n$ and $\theta_n$ are not separately identifiable.
81	\end{proposition}
82	
83	\begin{corollary}
84	$\mathrm{Var}(e_i) > 0$ is a necessary condition for identifiability of $c_n$.
85	\end{corollary}
86	
87	Proofs of Propositions~\ref{prop:no_new} and~\ref{prop:exposure_variation} are given in Appendix~\ref{app:prop_proofs}.
88	
89	\begin{theorem}[Sufficient Conditions for Local Identifiability]
90	\label{thm:sufficient}
91	The G-MFRM is locally identifiable, up to the standard location constraint, if the following conditions hold: (i) a connected observation design (each item is observed by at least one model--judge pair), (ii) $J \geq 2$ judges, (iii) for each model $n$, the set of observed items spans at least two distinct exposure values ($\mathrm{Var}(e_i) > 0$ over observed items), and (iv) standard normalization $\sum_n \theta_n = 0$.
92	\end{theorem}
93	
94	The proof (Appendix~\ref{app:proof}) follows \citet{rothenberg1971}, establishing Fisher information non-singularity via the Cauchy--Schwarz inequality on the $(\theta_n, c_n)$ submatrix and a Schur complement for the remaining blocks. Monte Carlo validation confirms successful $c_n$ recovery (Appendix~\ref{app:cn_recovery}).
95	
96	\subsection{Error Propagation}
97	\label{sec:error_prop}
98	
99	The staged procedure treats the Stage~2 exposure estimates $\hat{e}_i$ as fixed quantities in Stage~3. This is a generated regressors problem \citep{pagan1984}: measurement error in $\hat{e}_i$ propagates into the posterior of $(\theta_n, c_n)$. The multiplicative structure $c_n \cdot e_i$ makes this an errors-in-variables (EIV) problem \citep{fuller1987}, with a predictable attenuation pattern.
100	
101	Let $\hat{e}_i = e_i + \epsilon_i$ with $\epsilon_i \sim \mathcal{N}(0, \sigma^2)$ independent of all model parameters. The attenuation factor for the contamination coefficient is
102	%
103	\begin{equation}
104	\label{eq:attenuation}
105	\lambda(\sigma) = \frac{\mathrm{Var}(e_i)}{\mathrm{Var}(e_i) + \sigma^2},
106	\end{equation}
107	%
108	so attenuation reaches 50\% when $\sigma = \sqrt{\mathrm{Var}(e_i)}$. In the synthetic data-generating process ($\mathrm{Var}(e_i) \approx 0.04$), this corresponds to $\sigma \approx 0.2$.\footnote{The attenuation formula assumes that $\epsilon_i$ is independent of all model parameters, identically distributed, and Gaussian. In practice, exposure estimation errors may be correlated across items sharing the same source or heteroscedastic across difficulty levels. Table~\ref{tab:error_prop} provides empirical validation that $\hat{\theta}$ estimates remain robust under such departures (Section~\ref{sec:experiments}).}
109	
110	Table~\ref{tab:error_prop} and Appendix~\ref{app:error_prop} show empirical degradation: below $\sigma = 0.2$, $\theta$-RMSE increases by 5.9\% and $c_n$-RMSE by 7.9\%; beyond the threshold ($\sigma = 0.5$), degradation becomes severe. Contamination estimates are more sensitive because $c_n$ enters the likelihood only through its product with $e_i$.
111	
112	For honest credible intervals, we apply the Murphy--Topel variance correction \citep{murphy1985} to account for generated-regressor uncertainty (Appendix~\ref{app:murphy_topel}).
113	
114	\subsection{Fair Scores and Diagnostics}
115	\label{sec:fair_scores}
116	
117	The Stage~3 posterior mean of $\theta_n$ provides a bias-and-contamination-corrected ``fair score'' for each model. The remaining parameters serve complementary diagnostic roles: per-model $c_n$ flags candidates for training data audit, per-judge $d_j$ informs judge calibration, and per-item $e_i$ identifies items for retirement or replacement.
118	
119	\begin{table}[t]
120	\centering
121	\small
122	\begin{tabular}{lcccc}
123	\toprule
124	& \multicolumn{2}{c}{\textbf{8 models}} & \multicolumn{2}{c}{\textbf{17 models}} \\
125	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
126	\textbf{Method} & $\tau$ & $\rho$ & $\tau$ & $\rho$ \\
127	\midrule
128	Raw Average & 0.786 & 0.905 & 0.838 & 0.949 \\
129	MFRM-only & 0.786 & 0.905 & TBD & TBD \\
130	Sequential & 0.786 & 0.905 & TBD & TBD \\
131	CyclicJudge & 0.786 & 0.905 & 0.838 & 0.949 \\
132	CyclicJudge+discard & 0.786 & 0.905 & 0.824 & 0.934 \\
133	DCR Factor & 0.786 & 0.905 & 0.824 & 0.946 \\
134	Pref.\ Leakage & 0.786 & 0.905 & 0.838 & 0.949 \\
135	\midrule
136	G-MFRM (ours) & \textbf{0.857} & \textbf{0.952} & \textbf{TBD} & \textbf{TBD} \\
137	\bottomrule
138	\end{tabular}
139	\caption{Correlation with Chatbot Arena human rankings on Arena-Hard (9 judges). All seven baselines produce identical rankings at $N = 8$ ($\tau = 0.786$). G-MFRM yields nominally higher point-estimate rank agreement ($+$7.1pp; bootstrap $\Delta\tau$ CI includes zero). Right columns report the 17-model evaluation (TBD).}
140	\label{tab:main_results}
141	\end{table}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84b70030-f480-4b9a-8d8e-81ab0b939dac",
  "isSidechain": true,
  "promptId": "0b26d185-bf84-492a-b63d-76b41c6c458f",
  "agentId": "af0b5f1dbbb0ecf84",
  "type": "user",
  "uuid": "c8fbca70-8841-4ee9-ac89-fa1ed2d611b4",
  "sourceToolAssistantUUID": "84b70030-f480-4b9a-8d8e-81ab0b939dac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T15:54:00.748Z_

<details open><summary>🔧 Tool call — Read · `toolu_01T5Bk4JeUDz8wpMitkKF6GT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8fbca70-8841-4ee9-ac89-fa1ed2d611b4",
  "isSidechain": true,
  "agentId": "af0b5f1dbbb0ecf84",
  "requestId": "req_011CbPZHEh1e3pX9k1NmQyqS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e495fdb0-534e-4655-ae19-fb9a5c3bfeda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GLNqLaD9wLi5XynX4wMkAr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28016,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28016,
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

### Tool result

_source line 12 · 2026-05-25T15:54:00.760Z_

<details><summary>↩ Tool result · `toolu_01T5Bk4JeUDz8wpMitkKF6GT`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=\columnwidth, trim=0 0 250bp 0, clip]{fig6_cn_profile}
7	\caption{Contamination susceptibility $\hat{c}_n$ (posterior mean $\pm$ 95\% CI), ordered by magnitude. Older models (GPT-3.5-Turbo, GPT-4-0613) show 4--6$\times$ higher susceptibility than recent models (GPT-4o).}
8	\label{fig:contamination_bars}
9	\end{figure}
10	
11	\begin{figure}[t]
12	\centering
13	\includegraphics[width=\columnwidth, trim=265bp 0 0 0, clip]{fig6_cn_profile}
14	\caption{Ability bias absorbed by MFRM-only estimation: $\Delta\theta = \hat{\theta}_{\mathrm{MFRM}} - \hat{\theta}_{\mathrm{G\text{-}MFRM}}$. The strong correlation with $\hat{c}_n$ (Spearman $\rho = 1.0$) confirms that contamination inflates MFRM ability estimates for high-$c_n$ models, as predicted by the OVB analysis (Section~\ref{sec:confounding}).}
15	\label{fig:bias_absorption}
16	\end{figure}
17	
18	\subsection{Setup}
19	\label{sec:setup}
20	
21	\paragraph{Data and models.} We evaluate on Arena-Hard \citep{li2024arenahard}, a benchmark of 316 multi-turn conversational items selected for high separability among frontier models. After filtering for coverage, the evaluation set comprises 176 items in a connected incomplete design (36{,}231 observations; 66.0\% fill rate of the full $N \times I \times J$ tensor). Seventeen target models spanning proprietary and open-source families are evaluated: the original 8 models (GPT-4o, GPT-4o-mini, Qwen2.5-72B, LLaMA-3.3-70B, Qwen3-8B, Gemma-2-9B, GPT-4-0613, GPT-3.5-Turbo) plus 9 additional models (Claude-3.5-Sonnet, GPT-4-Turbo, LLaMA-3.1-70B, Gemma-2-27B, Claude-3-Opus, LLaMA-3-70B, Mixtral-8x22B, Claude-3-Haiku, LLaMA-3-8B). Ground-truth rankings are derived from Chatbot Arena human preference data \citep{zheng2023mtbench}.
22	
23	\paragraph{Judges.} Nine LLM judges score model responses in position-swapped pairwise mode: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Gemini-2.5-Pro, Mistral-Large-2, LLaMA-3.3-70B, Qwen2.5-72B, and Qwen3-235B. Seven judges cover all 17 target models; two judges (GPT-5.5 and Claude Opus 4.7) cover only the original 8 models, yielding an asymmetric connected design---Theorem~\ref{thm:sufficient} requires only connectivity, not full crossing. Position swapping controls for position bias and doubles the effective observation count. Two models---Qwen2.5-72B and LLaMA-3.3-70B---serve as both judge and target; $d_j$ absorbs systematic self-evaluation bias, and excluding self-judging observations leaves rankings unchanged ($\tau = 0.857$; Appendix~\ref{app:self_eval}).
24	
25	\paragraph{Exposure estimation.} Per-item exposure $e_i$ is estimated via a two-source pipeline (\S\ref{sec:staged}): reference model anchoring with gpt-4-0314 as anchor (75\% weight) and cross-model agreement (25\% weight). The pipeline is robust to weight configuration (Spearman $\rho \geq 0.998$ across all configurations tested).
26	
27	\paragraph{MCMC.} We use NumPyro's NUTS sampler with 4{,}000 warmup and 4{,}000 sampling iterations across 4 chains (target acceptance 0.95). The contamination prior follows the hierarchical HalfNormal specification (Eq.~\ref{eq:contam_prior}). Convergence is assessed via rank-normalized split-$\hat{R}$ \citep{vehtari2021rhat} with conventional $\hat{R} < 1.05$ and ESS $> 100$ thresholds \citep{gelman2013bda}.
28	
29	\subsection{Baselines and Main Results}
30	\label{sec:main_results}
31	
32	We compare G-MFRM against seven methods that address judge bias or contamination separately: (1) Raw Average, (2) MFRM-only (Eq.~\ref{eq:mfrm}), (3) Sequential pipeline (MFRM then contamination adjustment), (4) CyclicJudge \citep{cyclicjudge2026}, (5) CyclicJudge+discard (exposed items removed), (6) DCR Factor \citep{dcr2025}, and (7) Preference Leakage calibration \citep{preference_leakage2026}. All methods are evaluated by Kendall $\tau$ and Spearman $\rho$ against Chatbot Arena human rankings.
33	
34	All seven baselines produce identical rankings ($\tau = 0.786$, $\rho = 0.905$; raw ability scores differ by $< 0.03$ logits, Table~\ref{tab:raw_scores}). G-MFRM achieves nominally higher rank agreement ($\tau = 0.857$, $\rho = 0.952$), but bootstrap $\Delta\tau$ 95\% CI $[-0.071, 0.071]$ includes zero at $N = 8$, though $P(\Delta\tau \geq 0) = 0.927$. On synthetic data ($N = 50$), the improvement is significant ($\tau = 0.922$ vs.\ $0.839$, Wilcoxon $p < 0.001$), confirming the effect is real but below detection at this sample size.
35	
36	\paragraph{Predictive fit.} LOO cross-validation strongly favors G-MFRM ($\Delta\mathrm{ELPD}_{\mathrm{LOO}} = -55.7$, SE $= 9.4$, $|\Delta/\mathrm{SE}| = 5.9$; \citealp{vehtari2017loo}), with stacking weight 1.0 and all Pareto $\hat{k} < 0.7$ (Appendix~\ref{app:loo_comparison}).
37	
38	\paragraph{Ranking accuracy.} The $\Delta\tau = +0.071$ improvement is not statistically significant at $N = 8$ (bootstrap 95\% CI crosses zero; post-hoc power ${\sim}$50\%). Power analysis indicates $N \approx 17$ for 80\% power (Appendix~\ref{app:power}), validated at $N = 20$ where the improvement reaches significance ($p < 0.001$; Appendix~\ref{app:synthetic_calibration}).
39	
40	All parameters achieve $\hat{R} \leq 1.03$ with ESS $\geq 174$ and zero divergent transitions; model- and judge-level fit statistics fall within acceptable ranges (MNSQ $\in [0.63, 1.07]$; full diagnostics in Appendices~\ref{app:item_diagnostics} and~\ref{app:ppc}). Contamination susceptibility $\hat{c}_n$ exhibits a gradient by model age (Figure~\ref{fig:contamination_bars}): the four oldest models show $\hat{c}_n > 1.0$ (GPT-3.5-Turbo: $5.60$; GPT-4-0613: $4.20$; Qwen2.5-72B: $3.00$; LLaMA-3.3-70B: $2.50$), while recent models show low contamination (GPT-4o: $0.88$; GPT-4o-mini: $0.93$). MFRM-only inflates ability estimates for the most contaminated models by up to 0.79 logits (Figure~\ref{fig:bias_absorption}; Table~\ref{tab:bias_absorption}). Judge severity $d_j$ separates by provenance: proprietary judges score more strictly, spanning 1.34 logits (Figure~\ref{fig:judge_severity}; Table~\ref{tab:judge_severity}). Results are robust to prior specification and judge panel size ($k \geq 4$ suffices; Appendices~\ref{app:prior_robustness} and~\ref{app:judge_count}).
41	
42	\subsection{Error Propagation and Ablation}
43	\label{sec:error_prop_results}
44	
45	\begin{figure}[t]
46	\centering
47	\includegraphics[width=\columnwidth]{fig_ablation_rmse}
48	\caption{Ablation on synthetic data ($N = 50$, 20 seeds). Joint estimation drives the improvement: staged estimation doubles $\theta$-RMSE ($p < 0.001$). Continuous gating provides a moderate gain over binary ($p < 0.001$); removing judge severity $d_j$ has negligible effect on ability recovery (n.s.).}
49	\label{fig:ablation}
50	\end{figure}
51	
52	Table~\ref{tab:error_prop} validates the theoretical prediction (\S\ref{sec:error_prop}): below $\sigma = 0.2$, ability RMSE increases by 5.9\% and contamination RMSE by 7.9\%; beyond the threshold ($\sigma = 0.5$), degradation becomes substantial. Ablation (Figure~\ref{fig:ablation}; full results in Table~\ref{tab:ablation}, Appendix~\ref{app:ablation}) confirms joint estimation as the dominant contributor ($2.0\times$ $\theta$-RMSE increase under staged estimation, $p < 0.001$) and continuous gating over binary ($c_n$-RMSE $-$40\%, $p < 0.001$).
53	
54	\paragraph{Judge panel composition.} Subsampling from the 9-judge panel (Table~\ref{tab:judge_count}, Appendix~\ref{app:judge_count}), G-MFRM's ranking accuracy increases monotonically with judge count ($\tau$: $0.771 \to 0.857$) and exceeds the full-panel baseline at $k \geq 4$. Leave-one-judge-out analysis identifies three judges spanning the severity extremes---Claude Opus 4.7 ($d_j = +0.60$), GPT-5.5 ($+0.53$), and LLaMA-3.3-70B ($-0.42$)---as individually necessary for the ranking improvement; removing any one reduces $\tau$ to the baseline $0.786$, while removing any other judge preserves $\tau = 0.857$. This suggests that severity diversity matters more than panel size for contamination--ability disentanglement, providing practical guidance for judge panel design.
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e495fdb0-534e-4655-ae19-fb9a5c3bfeda",
  "isSidechain": true,
  "promptId": "0b26d185-bf84-492a-b63d-76b41c6c458f",
  "agentId": "af0b5f1dbbb0ecf84",
  "type": "user",
  "uuid": "c268c96a-cbb7-48a0-b31c-772285d6346c",
  "sourceToolAssistantUUID": "e495fdb0-534e-4655-ae19-fb9a5c3bfeda",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T15:54:01.171Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RW31WJwkEH5xQid2BgiXKy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c268c96a-cbb7-48a0-b31c-772285d6346c",
  "isSidechain": true,
  "agentId": "af0b5f1dbbb0ecf84",
  "requestId": "req_011CbPZHEh1e3pX9k1NmQyqS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0efa16f0-8bcc-422d-8dbd-f96ffdff6883",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GLNqLaD9wLi5XynX4wMkAr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28016,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28016,
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

### Tool result

_source line 14 · 2026-05-25T15:54:01.185Z_

<details><summary>↩ Tool result · `toolu_01RW31WJwkEH5xQid2BgiXKy`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We introduced G-MFRM, a Bayesian measurement model that jointly estimates model ability, judge severity, and contamination susceptibility within a single inferential framework. The key theoretical contribution is formalizing the confounding between judge bias and benchmark contamination as omitted variable bias: omitting either facet produces a closed-form bias in the other, with direction and magnitude determined by the exposure--severity covariance (Section~\ref{sec:confounding}).
5	
6	On Arena-Hard, G-MFRM achieves nominally higher rank agreement with human preferences ($\tau = 0.857$ vs.\ $0.786$; $P(\Delta\tau \geq 0) = 0.927$, not significant at $N = 8$), while LOO cross-validation strongly favors the joint model ($|\Delta\mathrm{ELPD}/\mathrm{SE}| = 5.9$, stacking weight 1.0). The contamination susceptibility profile reveals a clear gradient by model age, with older models showing 4--6$\times$ higher susceptibility, and the bias absorption analysis confirms that MFRM-only inflates ability estimates for contaminated models by up to 0.79 logits. Ablation identifies joint estimation as the dominant contributor: staged estimation doubles ability RMSE, while continuous exposure gating improves contamination recovery by 40\% over binary.
7	
8	Two practical implications emerge. First, evaluation frameworks that treat judge bias and contamination as independent---the current default---incur systematic errors that grow with the heterogeneity of model contamination levels; future LLM evaluation should model these facets jointly. Second, judge panels benefit from severity diversity: leave-one-judge-out analysis shows that judges at the severity extremes are individually necessary for the ranking improvement (Appendix~\ref{app:judge_count}), suggesting that panel composition matters as much as panel size.
9	
10	Several directions remain open. The rank-1 contamination structure assumes a single $c_n$ per model; domain-specific contamination (e.g., coding vs.\ reasoning) motivates higher-rank decompositions $\sum_r c_{nr} \cdot e_{ir}$. Posterior credible intervals for $c_n$ exhibit systematic overconfidence (71\% coverage at nominal 95\%); simulation-based calibration \citep{talts2018sbc} offers a path to corrected uncertainty quantification. Scaling G-MFRM to larger model populations and diverse benchmarks would strengthen the generalizability of the joint estimation advantage confirmed in synthetic experiments (Appendix~\ref{app:synthetic_calibration}).
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0efa16f0-8bcc-422d-8dbd-f96ffdff6883",
  "isSidechain": true,
  "promptId": "0b26d185-bf84-492a-b63d-76b41c6c458f",
  "agentId": "af0b5f1dbbb0ecf84",
  "type": "user",
  "uuid": "23b090be-d3c8-4c38-b077-958810f47fc7",
  "sourceToolAssistantUUID": "0efa16f0-8bcc-422d-8dbd-f96ffdff6883",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T15:54:01.390Z_

<details open><summary>🔧 Tool call — Read · `toolu_011whvhCBzUJQ4phBE1yGVzq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "23b090be-d3c8-4c38-b077-958810f47fc7",
  "isSidechain": true,
  "agentId": "af0b5f1dbbb0ecf84",
  "requestId": "req_011CbPZHEh1e3pX9k1NmQyqS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4699cec8-101f-45aa-8b82-b74ff40836c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GLNqLaD9wLi5XynX4wMkAr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28016,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28016,
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

### Tool result

_source line 16 · 2026-05-25T15:54:01.404Z_

<details><summary>↩ Tool result · `toolu_011whvhCBzUJQ4phBE1yGVzq`</summary>

```text
1	The evaluation uses a single benchmark (Arena-Hard) with 66.0\% fill rate (18{,}116 of 27{,}456 potential cells); sparser designs may compromise identifiability of $c_n$ for models with few observed exposed items, and sparse per-item observations produce elevated item-level mean-square residuals (92/176 items), though model- and judge-level fit remains acceptable. Stage~2 exposure estimation relies on a reference model anchor (gpt-4-0314), whose validity should be periodically re-assessed as benchmarks age.
2	
3	Empirical CI coverage differs by parameter type: ability estimates $\theta$ approach nominal coverage (${\sim}$90\% at $N = 8$), while contamination susceptibility $c_n$ exhibits posterior overconfidence (71\% at $N = 50$, 68\% at $N = 8$; \citealp{talts2018sbc}), a structural issue from the multiplicative coupling $c_n \cdot e_i$ and the HalfNormal boundary constraint at $c_n = 0$ that does not improve with sample size; $c_n$ credible intervals should be treated as lower bounds on uncertainty (Appendix~\ref{app:ci_coverage}), with recalibration via simulation-based calibration (SBC) as a direction for future work. The bilinear term also assumes rank-1 structure---a single contamination dimension per model---while contamination may be domain-specific (e.g., coding vs.\ reasoning), requiring a higher-rank decomposition $\sum_r c_{nr} \cdot e_{ir}$ that the current model does not capture.
4	
5	Post-hoc power analysis indicates $N \approx 17$ for 80\% power to detect $\Delta\tau = 0.071$; the $N = 8$ evaluation has ${\sim}$50\% power, explaining the non-significant bootstrap result. Generalization to other benchmarks and larger model populations remains to be verified. While self-evaluation sensitivity analysis (Appendix~\ref{app:self_eval}) confirms robust rankings when excluding self-judging observations, removing overlapping models entirely from the judge panel has not been conducted.
6	
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4699cec8-101f-45aa-8b82-b74ff40836c0",
  "isSidechain": true,
  "promptId": "0b26d185-bf84-492a-b63d-76b41c6c458f",
  "agentId": "af0b5f1dbbb0ecf84",
  "type": "user",
  "uuid": "a6d4a659-a720-4a06-8e6c-657029f9fb3c",
  "sourceToolAssistantUUID": "4699cec8-101f-45aa-8b82-b74ff40836c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T15:54:01.584Z_

<details open><summary>🔧 Tool call — Read · `toolu_01My3KSRKYRDpWtEAtsSTdBT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6d4a659-a720-4a06-8e6c-657029f9fb3c",
  "isSidechain": true,
  "agentId": "af0b5f1dbbb0ecf84",
  "requestId": "req_011CbPZHEh1e3pX9k1NmQyqS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0a0edea7-49e9-4d07-b69c-8fe42b320221",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GLNqLaD9wLi5XynX4wMkAr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28016,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28016,
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

### Tool result

_source line 18 · 2026-05-25T15:54:01.592Z_

<details><summary>↩ Tool result · `toolu_01My3KSRKYRDpWtEAtsSTdBT`</summary>

```text
1	\begin{abstract}
2	When a large language model (LLM) judge scores a model response on a benchmark item, the result conflates three signals: genuine ability, the judge's scoring tendency, and any advantage from training data exposure. Current evaluation pipelines correct for judge bias and contamination independently, but we show that separate correction is structurally flawed. We formalize this as an omitted variable bias (OVB) problem: any estimator that models one distortion while omitting the other produces systematically biased ability rankings, regardless of correction order. We propose the Gated Many-Facet Rasch Model (G-MFRM), a Bayesian framework that jointly estimates model ability, judge severity, and contamination susceptibility with formal identifiability guarantees and bounded error propagation. In synthetic experiments ($N = 50$), G-MFRM reduces ability root mean squared error by 51\% over sequential pipelines ($p < 0.001$). On Arena-Hard with 9 LLM judges, G-MFRM produces the first joint contamination-severity diagnostic: older models exhibit 4--6$\times$ higher contamination susceptibility, and judge severity profiles span 1.34 logits across the proprietary-open divide. Leave-one-out cross-validation confirms substantially improved predictive fit ($|\Delta\mathrm{ELPD}/\mathrm{SE}| = 5.9$)\footnote{Code and data are available at \url{https://anonymous.4open.science/r/gated_mfrm_judge_bias-43CC/}.}.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0a0edea7-49e9-4d07-b69c-8fe42b320221",
  "isSidechain": true,
  "promptId": "0b26d185-bf84-492a-b63d-76b41c6c458f",
  "agentId": "af0b5f1dbbb0ecf84",
  "type": "user",
  "uuid": "635dcae2-b6f1-4e80-91d3-1ca262afbcd9",
  "sourceToolAssistantUUID": "0a0edea7-49e9-4d07-b69c-8fe42b320221",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T15:54:01.778Z_

<details open><summary>🔧 Tool call — Read · `toolu_019SALFvufEEfkg4w2josW4G`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "635dcae2-b6f1-4e80-91d3-1ca262afbcd9",
  "isSidechain": true,
  "agentId": "af0b5f1dbbb0ecf84",
  "requestId": "req_011CbPZHEh1e3pX9k1NmQyqS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8fba7d65-0f4a-49c5-bd94-2d6bd9d8b745",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GLNqLaD9wLi5XynX4wMkAr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 28016,
      "cache_read_input_tokens": 0,
      "output_tokens": 667,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 28016
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 667,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 28016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 28016,
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

_source line 20 · 2026-05-25T15:54:02.049Z_

<details><summary>↩ Tool result · `toolu_019SALFvufEEfkg4w2josW4G`</summary>

```text
1	\section{Proofs of Propositions~\ref{prop:no_new} and~\ref{prop:exposure_variation}}
2	\label{app:prop_proofs}
3	
4	\begin{proof}[Proof of Proposition~\ref{prop:no_new}]
5	Suppose $c_n' = c_n + \delta$ preserves all response probabilities. Then $\delta \cdot e_i = 0$ for all items. Since $e_i \neq 0$ for at least one item by assumption, $\delta = 0$. Fixing $e_i$ externally eliminates the bilinear ambiguity $c_n \cdot e_i = (\lambda c_n)(\lambda^{-1} e_i)$ that would otherwise render the decomposition non-unique.
6	\end{proof}
7	
8	\begin{proof}[Proof of Proposition~\ref{prop:exposure_variation}]
9	When exposure is constant, the linear predictor becomes $(\theta_n + c_n \cdot e) - b_i - d_j - \tau_k$, equivalent to a standard MFRM with reparameterized ability $\theta^*_n = \theta_n + c_n \cdot e$. No configuration of response data can distinguish $(\theta_n, c_n)$ from $(\theta_n + \epsilon, c_n - \epsilon/e)$ for any $\epsilon$.
10	\end{proof}
11	
12	
13	\section{Proof of Theorem~\ref{thm:sufficient}}
14	\label{app:proof}
15	
16	We prove that the G-MFRM is locally identifiable under the conditions of Theorem~\ref{thm:sufficient}. Following \citet{rothenberg1971}, a parametric model is locally identifiable at the true parameter vector $\boldsymbol{\psi}_0$ if and only if the Fisher information matrix $\mathbf{F}(\boldsymbol{\psi}_0)$ is non-singular.
17	
18	\paragraph{Setup.} The G-MFRM parameter vector is $\boldsymbol{\psi} = (\boldsymbol{\theta}, \mathbf{c}, \mathbf{b}, \mathbf{d}, \boldsymbol{\tau})$, where $\boldsymbol{\theta} \in \mathbb{R}^{N-1}$ (after the location constraint $\sum_n \theta_n = 0$), $\mathbf{c} \in \mathbb{R}_{\geq 0}^N$, $\mathbf{b} \in \mathbb{R}^I$, $\mathbf{d} \in \mathbb{R}^J$, and $\boldsymbol{\tau} \in \mathbb{R}^{K-1}$. The exposure vector $\mathbf{e} = (e_1, \ldots, e_I)$ is fixed externally and treated as known. The linear predictor is $\eta_{nijk} = \theta_n - b_i - d_j - \tau_k + c_n \cdot e_i$, with partial derivatives:
19	%
20	\begin{align*}
21	\frac{\partial \eta_{nijk}}{\partial \theta_n} &= 1, \quad
22	\frac{\partial \eta_{nijk}}{\partial c_n} = e_i, \quad
23	\frac{\partial \eta_{nijk}}{\partial b_i} = -1, \\
24	\frac{\partial \eta_{nijk}}{\partial d_j} &= -1, \quad
25	\frac{\partial \eta_{nijk}}{\partial \tau_k} = -1.
26	\end{align*}
27	
28	\paragraph{Fisher information weights.} For each observation cell $(n,i,j)$, the Fisher information weight under the cumulative logit model is
29	%
30	\begin{equation}
31	\label{eq:fisher_weight}
32	w_{nij} = \sum_{k=1}^{K} \frac{\bigl[\sigma'(\eta_{nijk}) - \sigma'(\eta_{nij,k+1})\bigr]^2}{P(Y_{nij} = k)},
33	\end{equation}
34	%
35	where $\sigma(x) = (1 + e^{-x})^{-1}$, $\sigma'(x) = \sigma(x)(1 - \sigma(x))$, and we set $\sigma'(\eta_{nij,0}) = \sigma'(\eta_{nij,K+1}) = 0$ at the boundaries. Since $P(Y_{nij} = k) > 0$ for all categories and $\sigma'(\cdot) > 0$, we have $w_{nij} > 0$ for all $(n,i,j)$.
36	
37	\paragraph{Step 1: The $(\theta_n, c_n)$ submatrix.} For each model $n$, the $2 \times 2$ Fisher information submatrix is
38	%
39	\begin{equation}
40	\label{eq:fisher_block}
41	\mathbf{F}_n = \sum_{i=1}^{I} \sum_{j=1}^{J} w_{nij}
42	\begin{pmatrix} 1 & e_i \\ e_i & e_i^2 \end{pmatrix}.
43	\end{equation}
44	%
45	Its determinant is
46	%
47	\begin{multline}
48	\det \mathbf{F}_n = \Bigl(\textstyle\sum_{i,j} w_{nij}\Bigr)\Bigl(\textstyle\sum_{i,j} w_{nij}\, e_i^2\Bigr) \\
49	- \Bigl(\textstyle\sum_{i,j} w_{nij}\, e_i\Bigr)^2 = W_n^2 \cdot \mathrm{Var}_w(e_i),
50	\end{multline}
51	%
52	where $W_n = \sum_{i,j} w_{nij}$ and $\mathrm{Var}_w(e_i) = \overline{e^2}_n - \bar{e}_n^2$ is the weighted variance of exposure with weights $w_{nij}$. By the Cauchy--Schwarz inequality, $\mathrm{Var}_w(e_i) \geq 0$, with equality if and only if $e_i$ is constant across all items with $w_{nij} > 0$. Under conditions~(i) and~(iii), the observed items for model $n$ include at least two distinct exposure values with $w_{nij} > 0$ for the corresponding cells. Therefore $\mathrm{Var}_w(e_i) > 0$, $\det \mathbf{F}_n > 0$, and each $\mathbf{F}_n$ is positive definite.
53	
54	\paragraph{Step 2: Item and judge blocks.} Under the connected design (condition~i), each item $i$ is observed by at least one $(n,j)$ pair, so the item difficulty block has positive diagonal entries $[\mathbf{F}_{bb}]_{ii} = \sum_{n,j} w_{nij} > 0$ (summing over observed cells). Similarly, each judge $j$ observes at least one $(n,i)$ pair, giving $[\mathbf{F}_{dd}]_{jj} = \sum_{n,i} w_{nij} > 0$. Condition~(ii) ($J \geq 2$) ensures the judge block has sufficient dimension to separate judge effects from the intercept. Both blocks are positive definite.
55	
56	\paragraph{Step 3: Schur complement argument.} The full Fisher information matrix $\mathbf{F}$ contains off-diagonal blocks coupling the parameter groups. Partition as
57	%
58	\begin{equation*}
59	\mathbf{F} = \begin{pmatrix} \mathbf{A} & \mathbf{B} \\ \mathbf{B}^\top & \mathbf{D} \end{pmatrix},
60	\end{equation*}
61	%
62	where $\mathbf{A} = \mathrm{blockdiag}(\mathbf{F}_1, \ldots, \mathbf{F}_N)$ collects all $(\theta_n, c_n)$ submatrices and $\mathbf{D}$ collects the $(\mathbf{b}, \mathbf{d}, \boldsymbol{\tau})$ blocks. From Step~1, $\mathbf{A}$ is positive definite. The Schur complement
63	%
64	\begin{equation}
65	\label{eq:schur}
66	\mathbf{S} = \mathbf{D} - \mathbf{B}^\top \mathbf{A}^{-1} \mathbf{B}
67	\end{equation}
68	%
69	equals the conditional Fisher information for $(\mathbf{b}, \mathbf{d}, \boldsymbol{\tau})$ given $(\boldsymbol{\theta}, \mathbf{c})$. Conditioning on $(\boldsymbol{\theta}, \mathbf{c})$ with fixed $\mathbf{e}$ reduces the model to a standard MFRM with known offsets $c_n \cdot e_i$, whose identifiability is established by \citet[Chapter~5]{sanmartin2016} under conditions~(i), (ii), and~(iv). Therefore $\mathbf{S}$ is positive definite.
70	
71	Since both $\mathbf{A}$ and $\mathbf{S}$ are positive definite:
72	%
73	\begin{equation*}
74	\det \mathbf{F} = \det \mathbf{A} \cdot \det \mathbf{S} > 0,
75	\end{equation*}
76	%
77	establishing non-singularity of $\mathbf{F}$ and hence local identifiability. \qed
78	
79	\paragraph{Local vs.\ global identifiability.} Theorem~\ref{thm:sufficient} establishes \emph{local} identifiability: the Fisher information matrix is non-singular at the true parameter value, guaranteeing that no infinitesimally close parameter vector produces the same likelihood. This does not rule out discrete global non-identifiabilities (i.e., isolated points in parameter space with identical likelihood). However, the HalfNormal prior on $c_n$ restricts the parameter space to $c_n \geq 0$, eliminating the sign ambiguity that would otherwise create a global reflection $(\theta_n + \delta,\, c_n - \delta/e_i)$. Combined with the location constraint $\sum_n \theta_n = 0$ and the empirical observation that the posterior is unimodal across all chains (no mode-switching detected), the local result provides a practical guarantee of unique parameter recovery.
80	
81	\paragraph{Role of the Cauchy--Schwarz inequality.} The key step in Step~1 is the decomposition $\det \mathbf{F}_n = W_n^2 \cdot \mathrm{Var}_w(e_i)$, where the weighted variance $\mathrm{Var}_w(e_i) = \mathbb{E}_w[e_i^2] - (\mathbb{E}_w[e_i])^2 \geq 0$ by the Cauchy--Schwarz inequality applied to the vectors $(\sqrt{w_{nij}})$ and $(\sqrt{w_{nij}}\, e_i)$. Strict positivity follows from the requirement that $e_i$ takes at least two distinct values over observed items (condition~iii): if $e_i = e$ for all $i$ with $w_{nij} > 0$, then $\mathrm{Var}_w(e_i) = 0$ and the $(\theta_n, c_n)$ block becomes singular, recovering Proposition~\ref{prop:exposure_variation}. The Cauchy--Schwarz bound is tight only in this degenerate case, so any non-trivial exposure variation suffices for identification.
82	
83	
84	\section{Explicit Form of the OVB Coefficient $\gamma_n$}
85	\label{app:gamma}
86	
87	Under the MFRM logistic link, a first-order Taylor expansion of Observation~\ref{obs:ovb} yields an explicit approximation for the bias coefficient $\gamma_n$:
88	%
89	\begin{equation}
90	\label{eq:gamma_explicit}
91	\gamma_n \approx \frac{\sum_{i} w_{ni} \cdot e_i \cdot p_{ni}(1 - p_{ni})}{\sum_{i} w_{ni} \cdot p_{ni}(1 - p_{ni})},
92	\end{equation}
93	%
94	where $p_{ni} = \sigma(\theta_n - b_i - \bar{d})$ is the MFRM predicted probability averaged over judges and $w_{ni}$ is the effective item weight (number of judge observations for item $i$ on model $n$). Eq.~\ref{eq:gamma_explicit} is a weighted mean of the exposure values $e_i$, with weights proportional to the Fisher information $p_{ni}(1 - p_{ni})$. Items near the boundary ($p_{ni} \approx 0.5$) contribute more to the bias than items at the extremes, because the logistic link is most sensitive at these points. This approximation is accurate to first order in $(c_n \cdot e_i)$; the synthetic validation in Section~\ref{sec:confounding} ($r = 0.86$) confirms that the linear approximation captures the dominant bias structure.
95	
96	
97	\section{Murphy--Topel Variance Correction}
98	\label{app:murphy_topel}
99	
100	The three-stage G-MFRM procedure treats Stage~2 exposure estimates $\hat{e}_i$ as fixed in Stage~3, understating posterior uncertainty by ignoring estimation error in $\hat{e}_i$. We derive the Murphy--Topel correction \citep{murphy1985} adapted to the G-MFRM setting.
101	
102	\paragraph{Setup.} Let $\boldsymbol{\alpha} = (e_1, \ldots, e_I)$ denote the Stage~2 parameters estimated from an independent dataset with log-likelihood $\ell_2(\boldsymbol{\alpha})$, and let $\boldsymbol{\psi} = (\boldsymbol{\theta}, \mathbf{c}, \mathbf{b}, \mathbf{d}, \boldsymbol{\tau})$ denote the Stage~3 parameters estimated with log-likelihood $\ell_3(\boldsymbol{\psi}; \hat{\boldsymbol{\alpha}})$, where $\hat{\boldsymbol{\alpha}}$ is plugged in as known.
103	
104	\paragraph{Naive and Stage~2 variances.} The naive (uncorrected) variance of $\hat{\boldsymbol{\psi}}$ is
105	%
106	\begin{equation}
107	\mathbf{V}_3 = \left[-\frac{\partial^2 \ell_3}{\partial \boldsymbol{\psi}\, \partial \boldsymbol{\psi}^\top}\bigg|_{\hat{\boldsymbol{\psi}},\, \hat{\boldsymbol{\alpha}}}\right]^{-1},
108	\end{equation}
109	%
110	and the Stage~2 variance is
111	%
112	\begin{equation}
113	\mathbf{V}_2 = \left[-\frac{\partial^2 \ell_2}{\partial \boldsymbol{\alpha}\, \partial \boldsymbol{\alpha}^\top}\bigg|_{\hat{\boldsymbol{\alpha}}}\right]^{-1}.
114	\end{equation}
115	
116	\paragraph{Cross-derivative matrix.} The coupling between stages is captured by the cross-derivative
117	%
118	\begin{equation}
119	\mathbf{C} = \frac{\partial^2 \ell_3}{\partial \boldsymbol{\psi}\, \partial \boldsymbol{\alpha}^\top}\bigg|_{\hat{\boldsymbol{\psi}},\, \hat{\boldsymbol{\alpha}}}.
120	\end{equation}
121	%
122	In the G-MFRM, non-zero entries of $\mathbf{C}$ arise from the contamination gating term $c_n \cdot e_i$. The key entry is
123	%
124	\begin{equation}
125	\frac{\partial^2 \ell_3}{\partial c_n\, \partial e_i} = \sum_{j=1}^{J} \frac{\partial^2 \ell_{nij}}{\partial \eta_{nij}^2} \cdot c_n,
126	\end{equation}
127	%
128	which is proportional to $c_n$: models with zero contamination contribute no cross-derivative. Similarly, $\partial^2 \ell_3 / (\partial \theta_n\, \partial e_i)$ involves only indirect coupling through the shared item observations. The correction is therefore concentrated on the contamination parameters of models with $c_n > 0$.
129	
130	\paragraph{Corrected variance.} The Murphy--Topel corrected variance is
131	%
132	\begin{equation}
133	\label{eq:murphy_topel}
134	\mathbf{V}_{\mathrm{MT}} = \mathbf{V}_3 + \mathbf{V}_3\, \mathbf{C}\, \mathbf{V}_2\, \mathbf{C}^\top\, \mathbf{V}_3.
135	\end{equation}
136	%
137	The correction term $\mathbf{V}_3 \mathbf{C} \mathbf{V}_2 \mathbf{C}^\top \mathbf{V}_3$ is positive semi-definite, so $\mathbf{V}_{\mathrm{MT}} \succeq \mathbf{V}_3$: the corrected variance is always at least as large as the naive variance. The inflation is concentrated on $c_n$ for contaminated models and is negligible for $\theta_n$ when contamination is sparse, consistent with the empirical pattern in Table~\ref{tab:error_prop}.
138	
139	\paragraph{Implementation.} We estimate $\mathbf{V}_2$ from the Stage~2 bootstrap and compute $\mathbf{C}$ via finite differences of the Stage~3 log-likelihood evaluated at perturbed $\hat{\boldsymbol{\alpha}}$ values. Corrected credible intervals are obtained by inflating Stage~3 posterior samples by $\sqrt{\mathrm{diag}(\mathbf{V}_{\mathrm{MT}}) / \mathrm{diag}(\mathbf{V}_3)}$.
140	
141	
142	\section{Ablation Study}
143	\label{app:ablation}
144	
145	\begin{table}[h]
146	\centering
147	\scriptsize
148	\setlength{\tabcolsep}{3pt}
149	\begin{tabular}{lccc}
150	\toprule
151	\textbf{Variant} & $\theta$-RMSE & $\tau$ & $c_n$-RMSE \\
152	\midrule
153	Full G-MFRM & 0.124 $\pm$ 0.016 & 0.922 $\pm$ 0.010 & 0.593 $\pm$ 0.224 \\
154	$-$ Judge severity ($d_j$) & 0.127 $\pm$ 0.016 & 0.922 $\pm$ 0.010 & 0.629 $\pm$ 0.243 \\
155	Binary gating & 0.137 $\pm$ 0.016 & 0.909 $\pm$ 0.014 & 0.833 $\pm$ 0.226 \\
156	Staged estimation & 0.254 $\pm$ 0.045 & 0.839 $\pm$ 0.035 & 1.382 $\pm$ 0.164 \\
157	\bottomrule
158	\end{tabular}
159	\caption{Ablation study on synthetic data ($N = 50$, $I = 100$, $J = 8$, 20 seeds). Each row removes or modifies one component of the full G-MFRM. Staged estimation refers to fitting MFRM and contamination sequentially rather than jointly. All differences from Full G-MFRM are significant at $p < 0.001$ (Wilcoxon) except $-d_j$ on $\theta$-RMSE ($p = 0.245$) and $\tau$ ($p = 0.344$).}
160	\label{tab:ablation}
161	\end{table}
162	
163	The ablation confirms that joint estimation is the primary contributor to G-MFRM's advantage: staged estimation increases $\theta$-RMSE by $2.0\times$ (from 0.124 to 0.254, $p < 0.001$) and $c_n$-RMSE by $2.3\times$ (from 0.593 to 1.382, $p < 0.001$), with $\tau$ dropping from 0.922 to 0.839. This degradation directly reflects the omitted variable bias characterized in Section~\ref{sec:confounding}: when contamination and judge effects are estimated sequentially, the first-stage estimates absorb the unmodeled facet.
164	
165	Replacing continuous exposure $e_i \in [0,1]$ with binary gating ($e_i \in \{0, 1\}$) increases $c_n$-RMSE by 40\% (from 0.593 to 0.833, $p < 0.001$), indicating that graded exposure modeling captures contamination magnitude more precisely than a binary flag. The effect on $\theta$-RMSE is moderate ($+$10\%, $p < 0.001$), suggesting that the binary approximation still captures the dominant contamination signal but loses precision on partially exposed items.
166	
167	Removing judge severity $d_j$ does not significantly affect ability estimates ($\theta$-RMSE $+$2.4\%, $p = 0.245$; $\tau$ identical, $p = 0.344$) but significantly degrades contamination recovery ($c_n$-RMSE $+$6.1\%, $p < 0.001$). This confirms that $d_j$ serves as a diagnostic component that improves contamination estimation precision rather than ranking accuracy: without explicit judge severity modeling, judge-induced score variation is partially absorbed into the contamination estimates, inflating $c_n$-RMSE. The $d_j$ profile also provides independent diagnostic value for judge calibration (e.g., Claude Opus $d_j = +0.60$ vs.\ Mistral $-0.74$ in the real-data evaluation).
168	
169	\begin{figure}[h]
170	\centering
171	\includegraphics[width=\columnwidth]{theta_tau_boxplot}
172	\caption{Ranking accuracy (Kendall $\tau$ with ground truth) across ablation variants. Full G-MFRM achieves the highest and most consistent $\tau$; staged estimation shows the largest degradation and highest variance. Synthetic data: $N = 50$, $I = 100$, $J = 8$, 20 seeds.}
173	\label{fig:ablation_tau}
174	\end{figure}
175	
176	
177	\section{Posterior Predictive Check}
178	\label{app:ppc}
179	
180	Figure~\ref{fig:ppc} shows the posterior predictive distribution from 1{,}000 posterior draws over 5{,}661 observations. The predicted and observed response distributions are well-aligned (predicted mean win rate $0.593$ vs.\ observed $0.599$), with no systematic discrepancy across item difficulty or model ability levels.
181	
182	\begin{figure}[h]
183	\centering
184	\includegraphics[width=\columnwidth]{fig_ppc}
185	\caption{Posterior predictive check. Distribution of predicted (gray) and observed (black) response rates across all model--item--judge triplets. Mean predicted $= 0.593$, mean observed $= 0.599$.}
186	\label{fig:ppc}
187	\end{figure}
188	
189	
190	\section{LOO Model Comparison}
191	\label{app:loo_comparison}
192	
193	Figure~\ref{fig:model_comparison} visualizes the LOO-ELPD difference between G-MFRM and MFRM-only. G-MFRM is the reference model ($\Delta\mathrm{ELPD} = 0$); MFRM-only shows a deficit of $-55.7$ (SE $= 9.4$), confirming that the contamination gating term substantially improves held-out predictive fit.
194	
195	\begin{figure}[h]
196	\centering
197	\includegraphics[width=\columnwidth]{model_comparison}
198	\caption{LOO-ELPD model comparison. G-MFRM (reference) versus MFRM-only. Error bars show $\pm$1 SE. The $|\Delta/\mathrm{SE}| = 5.9$ strongly favors G-MFRM.}
199	\label{fig:model_comparison}
200	\end{figure}
201	
202	Figure~\ref{fig:pareto_k} shows the Pareto $\hat{k}$ diagnostic values for both models. All observations have $\hat{k} < 0.7$, confirming that the LOO approximation is reliable for both models.
203	
204	\begin{figure}[h]
205	\centering
206	\includegraphics[width=\columnwidth]{pareto_k_plot}
207	\caption{Pareto $\hat{k}$ diagnostics for G-MFRM (left) and MFRM-only (right). All 5{,}661 observations fall below the $\hat{k} = 0.7$ threshold, confirming reliable LOO estimates.}
208	\label{fig:pareto_k}
209	\end{figure}
210	
211	
212	\section{Self-Evaluation Robustness}
213	\label{app:self_eval}
214	
215	Two models---Qwen2.5-72B and LLaMA-3.3-70B---appear as both judge and target in our evaluation. Self-judging introduces a potential confound: a model may score its own responses more favorably. We examine the empirical magnitude of this effect and its impact on rankings.
216	
217	Qwen2.5-72B achieves a perfect self-judging win rate of 1.000 (42/42 items), compared to a cross-judge mean win rate of 0.714 for the same model. LLaMA-3.3-70B shows a self-judging win rate of 0.912, compared to a cross-judge mean of 0.823. Both values are elevated relative to cross-judge baselines, consistent with same-family preference leakage \citep{preference_leakage2026}.
218	
219	To assess sensitivity, we re-fit G-MFRM excluding all 99 self-judging observations (Qwen2.5-72B and LLaMA-3.3-70B judging their own responses). The resulting ranking yields $\tau = 0.857$, identical to the full-data G-MFRM point estimate, with a swap at ranks 2--3. Contamination susceptibility estimates $c_n$ shift by less than 0.15 for all models. This confirms that $d_j$ absorbs the bulk of self-evaluation bias and that rankings are robust to excluding self-judging pairs.
220	
221	
222	\section{Judge Severity Profiles}
223	\label{app:judge_severity}
224	
225	Table~\ref{tab:judge_severity} reports posterior estimates of judge severity $d_j$ for all nine judges. Positive values indicate stricter scoring (lower win rates); negative values indicate more lenient scoring. Proprietary models cluster at the strict end, while open-source models tend to be more lenient.
226	
227	\begin{table}[h]
228	\centering
229	\small
230	\begin{tabular}{lcc}
231	\toprule
232	\textbf{Judge} & $\hat{d}_j$ & 95\% CI \\
233	\midrule
234	Claude Opus 4.7 & $+0.60$ & [$+0.43$, $+0.76$] \\
235	GPT-5.5 & $+0.53$ & [$+0.37$, $+0.70$] \\
236	DeepSeek-V4-Pro & $+0.31$ & [$+0.07$, $+0.54$] \\
237	Claude Sonnet 4.6 & $+0.14$ & [$-0.04$, $+0.31$] \\
238	Gemini-2.5-Pro & $-0.04$ & [$-0.27$, $+0.19$] \\
239	Qwen3-235B & $-0.04$ & [$-0.24$, $+0.16$] \\
240	Qwen2.5-72B & $-0.35$ & [$-0.64$, $-0.07$] \\
241	LLaMA-3.3-70B & $-0.42$ & [$-0.66$, $-0.18$] \\
242	Mistral-Large-2 & $-0.74$ & [$-1.10$, $-0.37$] \\
243	\bottomrule
244	\end{tabular}
245	\caption{Judge severity estimates ($d_j$) for all nine judges. Positive = stricter scoring. The severity range spans 1.34 logits (Claude Opus to Mistral), comparable to $\sim$1 standard deviation of model ability.}
246	\label{tab:judge_severity}
247	\end{table}
248	
249	
250	\section{Judge Count Sensitivity}
251	\label{app:judge_count}
252	
253	Table~\ref{tab:judge_count} reports ranking accuracy as a function of the number of judges $k$, obtained by subsampling from the full 9-judge panel (10 random subsets per $k$; $k = 9$ uses the full panel). G-MFRM outperforms both raw averaging and sequential estimation at all judge counts. Rank agreement increases monotonically with $k$ ($\tau = 0.771 \to 0.857$), and variance contracts as additional judges improve $d_j$ and $c_n$ estimation. At $k \geq 4$, G-MFRM exceeds the full-panel baseline $\tau = 0.786$, suggesting that four diverse judges suffice for practical deployment.
254	
255	\begin{table}[h]
256	\centering
257	\small
258	\begin{tabular}{lcccc}
259	\toprule
260	$k$ & Raw Avg & Sequential & G-MFRM & $\Delta\tau$ \\
261	\midrule
262	2 & $.755 \pm .088$ & $.764 \pm .096$ & $.771 \pm .081$ & $+.017$ \\
263	4 & $.779 \pm .041$ & $.786 \pm .048$ & $.800 \pm .045$ & $+.021$ \\
264	6 & $.800 \pm .030$ & $.807 \pm .048$ & $.821 \pm .051$ & $+.021$ \\
265	9 & $.786$ & $.786$ & $.857$ & $+.071$ \\
266	\bottomrule
267	\end{tabular}
268	\caption{Kendall $\tau$ with Chatbot Arena rankings as a function of judge count $k$. $\Delta\tau$ = G-MFRM $-$ Raw Average. Values for $k < 9$ are mean $\pm$ std over 10 random judge subsets.}
269	\label{tab:judge_count}
270	\end{table}
271	
272	Leave-one-judge-out analysis reveals that three judges---Claude Opus 4.7 ($d_j = +0.60$), GPT-5.5 ($+0.53$), and LLaMA-3.3-70B ($-0.42$)---are individually necessary for the ranking improvement: removing any one of these reduces G-MFRM $\tau$ to the baseline ($0.786$), while removing any of the other six judges preserves $\tau = 0.857$. These three judges span the severity spectrum (the two strictest and the second-most lenient), suggesting that contamination$\times$judge interaction identification requires sufficient severity diversity. This provides practical guidance: judge panels should include models with diverse scoring tendencies rather than homogeneous judges.
273	
274	G-MFRM requires $\geq 4$ MCMC chains for reliable contamination estimation; reduced chain counts attenuate $c_n$ estimates toward the prior mean, compressing inter-model differences.
275	
276	
277	\section{Stage~2 Weight Robustness}
278	\label{app:weight_robustness}
279	
280	All four weight configurations produce identical model rankings and near-perfect exposure score agreement (Spearman $\rho \geq 0.998$; Table~\ref{tab:weight_robustness}), confirming that the default 75/25 split is not a sensitive hyperparameter choice.
281	
282	\begin{table}[h]
283	\centering
284	\small
285	\begin{tabular}{lc}
286	\toprule
287	\textbf{Weight Config} & \textbf{Exposure} $\rho$ \\
288	\midrule
289	50 / 50 & 0.998 \\
290	75 / 25 (default) & 1.000 \\
291	90 / 10 & 0.999 \\
292	100 / 0 & 0.998 \\
293	\bottomrule
294	\end{tabular}
295	\caption{Stage~2 weight robustness. Weight Config denotes the percentage assigned to reference model anchoring vs.\ cross-model agreement. All configurations produce identical model rankings. Exposure $\rho$ is the Spearman correlation of per-item $e_i$ scores relative to the default 75/25 configuration.}
296	\label{tab:weight_robustness}
297	\end{table}
298	
299	
300	\section{Power Analysis}
301	\label{app:power}
302	
303	The observed effect size in the real-data evaluation is $\Delta\tau = 0.071$ (G-MFRM $\tau = 0.857$ vs.\ baseline $\tau = 0.786$). We conduct a permutation-based power analysis to determine the sample sizes required to detect this effect at $\alpha = 0.05$.
304	
305	We simulate ranking comparisons under the alternative hypothesis $H_1\!: \Delta\tau = 0.071$ by bootstrapping from the observed posterior distribution of G-MFRM ability estimates and recomputing $\tau$ against ground truth at varying model counts $N$. For each $N$, we draw 10{,}000 permutation replicates and compute the rejection rate at $\alpha = 0.05$ (two-sided).
306	
307	At $N = 8$ (our evaluation), power is approximately 50\%, explaining the non-significant bootstrap result ($\Delta\tau$ 95\% CI $[-0.071, 0.071]$). Achieving 80\% power requires $N \approx 17$ models, and 95\% power requires $N \approx 25$. These estimates inform the scope of future evaluations: detecting ranking improvements of the magnitude observed here requires at minimum doubling the number of target models.
308	
309	
310	\section{Per-Model Estimates}
311	\label{app:raw_scores}
312	
313	Table~\ref{tab:raw_scores} reports G-MFRM posterior estimates for all eight target models. All seven baselines produce identical rankings (Table~\ref{tab:main_results}), with ability scores differing by $< 0.03$ logits across methods; G-MFRM is the only method that alters the ranking, swapping gpt-4o-mini and Qwen2.5-72B at ranks 2--3.
314	
315	\begin{table}[h]
316	\centering
317	\scriptsize
318	\setlength{\tabcolsep}{3pt}
319	\resizebox{\linewidth}{!}{%
320	\begin{tabular}{lcccc}
321	\toprule
322	\textbf{Model} & $\hat{\theta}$ [95\% CI] & $\hat{c}_n$ [95\% CI] & \textbf{Base} & \textbf{G-MFRM} \\
323	\midrule
324	GPT-4o & $+2.00$ [$1.70$, $2.30$] & $0.88$ [$0.05$, $2.20$] & 1 & 1 \\
325	GPT-4o-mini & $+1.40$ [$1.10$, $1.70$] & $0.93$ [$0.06$, $2.20$] & 3 & 2 \\
326	Qwen2.5-72B & $+1.20$ [$0.85$, $1.50$] & $3.00$ [$1.40$, $4.60$] & 2 & 3 \\
327	LLaMA-3.3-70B & $+0.54$ [$0.23$, $0.85$] & $2.50$ [$1.10$, $3.90$] & 4 & 4 \\
328	Qwen3-8B & $+0.51$ [$0.22$, $0.79$] & $1.20$ [$0.14$, $2.50$] & 5 & 5 \\
329	Gemma-2-9B & $-0.50$ [$-0.79$, $-0.21$] & $1.70$ [$0.36$, $2.90$] & 6 & 6 \\
330	GPT-4-0613 & $-1.90$ [$-2.20$, $-1.60$] & $4.20$ [$3.10$, $5.30$] & 7 & 7 \\
331	GPT-3.5-Turbo & $-3.30$ [$-3.60$, $-3.00$] & $5.60$ [$4.40$, $6.80$] & 8 & 8 \\
332	\bottomrule
333	\end{tabular}}
334	\caption{G-MFRM posterior estimates for ability ($\hat{\theta}$) and contamination susceptibility ($\hat{c}_n$) with approximate 95\% credible intervals (empirical coverage ${\sim}$71\%; see Limitations). Point estimates and rank orderings are the primary results. ``Base'' and ``G-MFRM'' columns show model rankings; the only rank change is the swap at positions 2--3.}
335	\label{tab:raw_scores}
336	\end{table}
337	
338	
339	\section{Contamination Bias Absorption}
340	\label{app:bias_absorption}
341	
342	Table~\ref{tab:bias_absorption} compares per-model ability estimates from MFRM-only and G-MFRM. The difference $\Delta\theta = \hat{\theta}_{\text{MFRM}} - \hat{\theta}_{\text{G-MFRM}}$ is perfectly rank-correlated with contamination susceptibility $c_n$ (Spearman $\rho = 1.0$), providing direct empirical evidence that MFRM-only absorbs the omitted contamination term into ability estimates.
343	
344	\begin{table}[h]
345	\centering
346	\scriptsize
347	\setlength{\tabcolsep}{3pt}
348	\begin{tabular}{lcccc}
349	\toprule
350	\textbf{Model} & $\hat{\theta}_{\text{MFRM}}$ & $\hat{\theta}_{\text{G-MFRM}}$ & $\Delta\theta$ & $\hat{c}_n$ \\
351	\midrule
352	GPT-3.5-Turbo & $-2.487$ & $-3.274$ & $+0.786$ & $5.587$ \\
353	GPT-4-0613 & $-1.446$ & $-1.877$ & $+0.431$ & $4.168$ \\
354	Qwen2.5-72B & $+1.213$ & $+1.178$ & $+0.035$ & $2.961$ \\
355	LLaMA-3.3-70B & $+0.518$ & $+0.539$ & $-0.022$ & $2.478$ \\
356	Gemma-2-9B & $-0.661$ & $-0.500$ & $-0.161$ & $1.654$ \\
357	Qwen3-8B & $+0.208$ & $+0.513$ & $-0.305$ & $1.178$ \\
358	GPT-4o-mini & $+1.064$ & $+1.432$ & $-0.368$ & $0.934$ \\
359	GPT-4o & $+1.591$ & $+1.988$ & $-0.397$ & $0.880$ \\
360	\bottomrule
361	\end{tabular}
362	\caption{Contamination bias absorption in MFRM-only estimation. $\Delta\theta = \hat{\theta}_{\text{MFRM}} - \hat{\theta}_{\text{G-MFRM}}$. Models with high contamination susceptibility ($c_n$) have inflated ability estimates under MFRM-only; models with low $c_n$ are relatively deflated. The perfect rank correlation (Spearman $\rho = 1.0$) between $\Delta\theta$ and $c_n$ empirically confirms the omitted variable bias predicted in Section~\ref{sec:confounding}.}
363	\label{tab:bias_absorption}
364	\end{table}
365	
366	
367	\section{Synthetic Calibration at Matched Scale}
368	\label{app:synthetic_calibration}
369	
370	We generate synthetic data at matched scale ($N = 8$ models, $I = 176$ items, $J = 9$ judges) with known ground-truth parameters across 20 random seeds. Joint G-MFRM consistently outperforms sequential estimation: $\theta$-RMSE is halved ($0.083$ vs.\ $0.166$), and ranking agreement improves by 7.2 percentage points (mean $\tau = 0.954$ vs.\ $0.882$). Across 20 seeds, joint estimation improves or matches sequential in all cases (10 wins, 0 losses, 10 ties; Wilcoxon signed-rank $p < 0.002$). The synthetic effect size ($\Delta\tau = +0.072$) closely matches the observed real-data effect ($\Delta\tau = +0.071$). All 40 MCMC fits converge ($\hat{R} = 1.0$, ESS $\geq 1{,}678$).
371	
372	\begin{table}[h]
373	\centering
374	\small
375	\begin{tabular}{lccc}
376	\toprule
377	\textbf{Metric} & \textbf{Sequential} & \textbf{Joint G-MFRM} & \textbf{Improv.} \\
378	\midrule
379	$\theta$ RMSE & $0.166 \pm 0.050$ & $0.083 \pm 0.024$ & $-50.3\%$ \\
380	$\theta$ $\tau$ & $0.882 \pm 0.112$ & $0.954 \pm 0.048$ & $+7.2$pp \\
381	$c_n$ RMSE & $1.399 \pm 0.358$ & $0.552 \pm 0.328$ & $-60.5\%$ \\
382	$c_n$ Pearson & $0.850 \pm 0.141$ & $0.866 \pm 0.151$ & $+1.9$\% \\
383	\bottomrule
384	\end{tabular}
385	\caption{Synthetic calibration at $N = 8$ ($I = 176$, $J = 9$, 20 seeds). Joint G-MFRM halves $\theta$-RMSE and reduces $c_n$-RMSE by 61\% relative to sequential estimation.}
386	\label{tab:synthetic_calibration}
387	\end{table}
388	
389	At $N = 20$ (20 seeds), the ranking improvement becomes individually significant: joint G-MFRM achieves $\Delta\tau = +0.052$ over sequential estimation (Wilcoxon $p = 1.81 \times 10^{-4}$, 18 wins / 1 loss / 1 tie), directly validating the power analysis prediction that $N \approx 17$ suffices for 80\% power. The effect size is stable across scales ($\Delta\tau = +0.072$ at $N = 8$, $+0.052$ at $N = 20$).
390	
391	\begin{table}[h]
392	\centering
393	\small
394	\begin{tabular}{lccc}
395	\toprule
396	\textbf{Metric} & \textbf{Sequential} & \textbf{Joint G-MFRM} & \textbf{Improv.} \\
397	\midrule
398	$\theta$ RMSE & $0.171 \pm 0.049$ & $0.094 \pm 0.019$ & $-45.2\%$ \\
399	$\theta$ $\tau$ & $0.891 \pm 0.038$ & $0.943 \pm 0.036$ & $+5.2$pp \\
400	$c_n$ RMSE & $1.375 \pm 0.278$ & $0.626 \pm 0.263$ & $-54.5\%$ \\
401	$c_n$ Pearson & $0.817 \pm 0.096$ & $0.842 \pm 0.106$ & $+2.5\%$ \\
402	\bottomrule
403	\end{tabular}
404	\caption{Synthetic calibration at $N = 20$ ($I = 176$, $J = 9$, 20 seeds). Ranking improvement is individually significant (Wilcoxon $p = 1.81 \times 10^{-4}$), validating the power analysis prediction.}
405	\label{tab:synthetic_calibration_n20}
406	\end{table}
407	
408	
409	\section{Prior Specification Robustness}
410	\label{app:prior_robustness}
411	
412	We compare posterior estimates under two contamination priors: Horseshoe \citep{piironen2017horseshoe} and hierarchical HalfNormal (Eq.~\ref{eq:contam_prior}). Table~\ref{tab:prior_robustness} reports $\hat{c}_n$ and $\hat{\theta}$ posterior means for all eight target models under both specifications.
413	
414	\begin{table}[h]
415	\centering
416	\small
417	\begin{tabular}{lcccc}
418	\toprule
419	\textbf{Model} & $\hat{c}_n$ (HS) & $\hat{c}_n$ (HN) & $\hat{\theta}$ (HS) & $\hat{\theta}$ (HN) \\
420	\midrule
421	Gemma-2-9B & 1.61 & 1.65 & $-0.49$ & $-0.50$ \\
422	GPT-3.5-Turbo & 5.69 & 5.57 & $-3.30$ & $-3.27$ \\
423	GPT-4-0613 & 4.25 & 4.15 & $-1.89$ & $-1.88$ \\
424	GPT-4o & 0.79 & 0.88 & $+2.01$ & $+1.99$ \\
425	GPT-4o-mini & 0.84 & 0.92 & $+1.45$ & $+1.43$ \\
426	LLaMA-3.3-70B & 2.50 & 2.46 & $+0.53$ & $+0.54$ \\
427	Qwen2.5-72B & 3.02 & 2.94 & $+1.17$ & $+1.18$ \\
428	Qwen3-8B & 1.11 & 1.15 & $+0.53$ & $+0.52$ \\
429	\bottomrule
430	\end{tabular}
431	\caption{Posterior estimates under Horseshoe (HS) and HalfNormal (HN) contamination priors. Both priors produce virtually identical estimates: Pearson $r = 1.000$ for $\hat{\theta}$ and $r = 0.9999$ for $\hat{c}_n$.}
432	\label{tab:prior_robustness}
433	\end{table}
434	
435	Posterior estimates are virtually identical across the two prior specifications (Pearson $r = 1.000$ for $\hat{\theta}$, $r > 0.999$ for $\hat{c}_n$), indicating that results are not sensitive to the choice of contamination prior.
436	
437	
438	\section{Item-Level Fit Diagnostics}
439	\label{app:item_diagnostics}
440	
441	We report item-level infit and outfit MNSQ statistics for all 176 items. Items with MNSQ outside $[0.5, 1.5]$ are flagged as potentially misfitting.
442	
443	\begin{table}[h]
444	\centering
445	\small
446	\begin{tabular}{lccccc}
447	\toprule
448	\textbf{Statistic} & \textbf{Mean} & \textbf{SD} & \textbf{Median} & \textbf{Min} & \textbf{Max} \\
449	\midrule
450	Infit MNSQ & 0.78 & 0.41 & 0.76 & 0.05 & 1.95 \\
451	Outfit MNSQ & 0.73 & 0.57 & 0.58 & 0.04 & 3.17 \\
452	\bottomrule
453	\end{tabular}
454	\caption{Item-level fit statistics across 176 items.}
455	\label{tab:item_fit_summary}
456	\end{table}
457	
458	Of the 176 items, 92 are flagged: 18 overfit (MNSQ $> 1.5$) and 74 underfit (MNSQ $< 0.5$). The majority of flagged items are underfit, reflecting sparse low-observation items where the model's predicted variance exceeds the observed variance---a consequence of limited data per item rather than a structural model deficiency. The 18 overfit items exhibit more erratic response patterns than the model predicts. Importantly, no model-level or judge-level facets are flagged (all MNSQ within $[0.63, 1.07]$), confirming that the G-MFRM captures the systematic structure in model ability, judge severity, and contamination.
459	
460	
461	\section{CI Coverage Analysis}
462	\label{app:ci_coverage}
463	
464	We assess empirical coverage of 95\% posterior credible intervals across synthetic replications. At $N=8$ (49 seeds), ability parameter $\theta$ achieves 90.1\% coverage, approaching the nominal level, while contamination susceptibility $c_n$ achieves only 67.9\%. At $N=50$ (50 seeds; exp-009), $c_n$ coverage improves to 71\%. The coverage gap between $\theta$ and $c_n$ reflects the multiplicative coupling $c_n \cdot e_i$: contamination parameters enter the likelihood through an interaction term, making posterior inference more sensitive to exposure estimation noise and the HalfNormal prior's boundary constraint at $c_n = 0$. These results support treating $c_n$ point estimates and rank orderings as reliable diagnostics, while noting that $c_n$ credible intervals are systematically too narrow.
465	
466	\section{Bias vs.\ Confounding Level}
467	\label{app:bias_vs_rho}
468	
469	\begin{figure}[h]
470	\centering
471	\includegraphics[width=\columnwidth]{fig4_bias_vs_rho}
472	\caption{Sequential estimator bias remains approximately constant across confounding levels ($\rho$), confirming omission-driven rather than confounding-strength-dependent bias. Joint G-MFRM estimation reduces bias by approximately 70\% at all $\rho$ levels. Synthetic data: $N = 50$, $I = 100$, $J = 8$.}
473	\label{fig:bias_vs_rho_app}
474	\end{figure}
475	
476	
477	\section{Error Propagation Visualization}
478	\label{app:error_prop}
479	
480	\begin{figure}[h]
481	\centering
482	\includegraphics[width=\columnwidth]{fig3_error_propagation}
483	\caption{Error propagation from Stage~2 exposure noise to Stage~3 parameter estimates. Ability RMSE ($\theta$, left) and contamination RMSE ($c_n$, right) as a function of exposure noise $\sigma_e$. The dashed line marks $\sigma_{\mathrm{crit}} \approx 0.2$, below which degradation remains mild ($\theta$-RMSE $+$5.9\%, $c_n$-RMSE $+$7.9\%). Error bars: $\pm$1 std over 20 seeds.}
484	\label{fig:error_prop_app}
485	\end{figure}
486	
487	
488	\section{Contamination Recovery}
489	\label{app:cn_recovery}
490	
491	\begin{figure}[h]
492	\centering
493	\includegraphics[width=\columnwidth]{fig5_cn_recovery}
494	\caption{Contamination susceptibility recovery ($c_n$: true vs.\ estimated) from 50 Monte Carlo seeds. Empirical CI coverage is 71\% (below nominal 95\%), indicating moderate posterior overconfidence (see Limitations).}
495	\label{fig:cn_recovery_app}
496	\end{figure}
497	
498	
499	\section{Use of AI Assistants}
500	\label{app:ai_assistants}
501	
502	We used Claude (Anthropic) as an AI coding and writing assistant
503	throughout this work. Specifically:
504	\begin{itemize}
505	    \item \textbf{Code:} drafting experiment scripts, data-processing
506	    pipelines, and analysis utilities; debugging and refactoring.
507	    \item \textbf{Writing:} drafting and revising paper sections,
508	    polishing prose, and reformatting LaTeX.
509	    \item \textbf{Literature:} summarizing related papers to inform
510	    the related-work section.
511	\end{itemize}
512	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fba7d65-0f4a-49c5-bd94-2d6bd9d8b745",
  "isSidechain": true,
  "promptId": "0b26d185-bf84-492a-b63d-76b41c6c458f",
  "agentId": "af0b5f1dbbb0ecf84",
  "type": "user",
  "uuid": "eccd5f94-5475-4c08-9907-318021106661",
  "sourceToolAssistantUUID": "8fba7d65-0f4a-49c5-bd94-2d6bd9d8b745",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-25T15:54:04.259Z_

Now let me get the line counts using bash for accurate statistics:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eccd5f94-5475-4c08-9907-318021106661",
  "isSidechain": true,
  "agentId": "af0b5f1dbbb0ecf84",
  "requestId": "req_011CbPZHZzNF9KELAPVkbykV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "93be661f-2902-486d-81e7-8507dd42868d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011UpaSXn64rutTqwnYTwJyd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 28939,
      "cache_read_input_tokens": 28016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 28939,
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

_source line 22 · 2026-05-25T15:54:04.829Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UXimNFw3aKjeas1zEVRkWQ`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93be661f-2902-486d-81e7-8507dd42868d",
  "isSidechain": true,
  "agentId": "af0b5f1dbbb0ecf84",
  "requestId": "req_011CbPZHZzNF9KELAPVkbykV",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5a6da51f-1eef-4f78-9cb1-67324f0b30a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011UpaSXn64rutTqwnYTwJyd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 28939,
      "cache_read_input_tokens": 28016,
      "output_tokens": 101,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 28939
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 101,
          "cache_read_input_tokens": 28016,
          "cache_creation_input_tokens": 28939,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 28939,
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

_source line 23 · 2026-05-25T15:54:04.985Z_

<details><summary>↩ Tool result · `toolu_01UXimNFw3aKjeas1zEVRkWQ`</summary>

```text
    3 /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/abstract.tex
  511 /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/appendix.tex
   41 /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/background.tex
   10 /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/conclusion.tex
   54 /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/experiments.tex
   22 /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/introduction.tex
    6 /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/limitations.tex
   48 /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/main.tex
  140 /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/method.tex
   11 /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/related_work.tex
  846 total
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a6da51f-1eef-4f78-9cb1-67324f0b30a6",
  "isSidechain": true,
  "promptId": "0b26d185-bf84-492a-b63d-76b41c6c458f",
  "agentId": "af0b5f1dbbb0ecf84",
  "type": "user",
  "uuid": "d6325f0b-f40c-4d8f-9aa2-188939fd10a0",
  "sourceToolAssistantUUID": "5a6da51f-1eef-4f78-9cb1-67324f0b30a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-25T15:54:06.759Z_

Perfect. Now let me generate word counts for each file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6325f0b-f40c-4d8f-9aa2-188939fd10a0",
  "isSidechain": true,
  "agentId": "af0b5f1dbbb0ecf84",
  "requestId": "req_011CbPZHnXRt8WwDCXYfLqs2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8f336025-ab21-4417-8e3d-a039f5992b33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ByPFV8NKGFagF3pLxh1VGv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 501,
      "cache_read_input_tokens": 56955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 501,
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

_source line 25 · 2026-05-25T15:54:07.361Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0152YQkPC3nHPe98m6N5wyoU`</summary>

```json
{
  "command": "for file in /home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/docs/paper/{abstract,introduction,related_work,background,method,experiments,conclusion,limitations,appendix}.tex; do echo \"=== $(basename $file) ===\"; wc -w < \"$file\"; done"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f336025-ab21-4417-8e3d-a039f5992b33",
  "isSidechain": true,
  "agentId": "af0b5f1dbbb0ecf84",
  "requestId": "req_011CbPZHnXRt8WwDCXYfLqs2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "78313732-ee70-4494-be52-848579c587ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ByPFV8NKGFagF3pLxh1VGv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 501,
      "cache_read_input_tokens": 56955,
      "output_tokens": 143,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 501
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 143,
          "cache_read_input_tokens": 56955,
          "cache_creation_input_tokens": 501,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 501,
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

_source line 26 · 2026-05-25T15:54:07.522Z_

<details><summary>↩ Tool result · `toolu_0152YQkPC3nHPe98m6N5wyoU`</summary>

```text
=== abstract.tex ===
180
=== introduction.tex ===
543
=== related_work.tex ===
214
=== background.tex ===
664
=== method.tex ===
1458
=== experiments.tex ===
908
=== conclusion.tex ===
307
=== limitations.tex ===
252
=== appendix.tex ===
4420
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78313732-ee70-4494-be52-848579c587ba",
  "isSidechain": true,
  "promptId": "0b26d185-bf84-492a-b63d-76b41c6c458f",
  "agentId": "af0b5f1dbbb0ecf84",
  "type": "user",
  "uuid": "a3f25642-5e76-4efb-9a73-9a5e75811543",
  "sourceToolAssistantUUID": "78313732-ee70-4494-be52-848579c587ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-25T15:54:35.878Z_

Perfect. Now I have all the information. Let me compile a comprehensive report.

## Paper Section Analysis Report

### File Statistics and Content Summary

**1. abstract.tex** | **3 lines** | **~180 words**
- Contains a single LaTeX abstract environment with one comprehensive paragraph
- Introduces the problem (conflation of ability, judge bias, and training data exposure)
- States the main contribution (G-MFRM framework with identifiability guarantees)
- Reports key empirical results (51% RMSE reduction, contamination gradient by model age, LOO cross-validation improvement)
- Includes a footnote with anonymous repository link

**2. introduction.tex** | **22 lines** | **~543 words**
- Subsection label and opening paragraph framing the problem
- Large Figure 1 (framework diagram comparing sequential vs. joint pipelines)
- Core contribution: formalization of judge-contamination confounding as omitted variable bias (OVB)
- Introduces G-MFRM three-stage calibration procedure with technical details
- Presents key empirical findings in paragraph form (51.2% RMSE reduction, 4-6x contamination gradient)
- Enumerated list of three main contributions

**3. related_work.tex** | **11 lines** | **~214 words**
- Three paragraph blocks organized by topic:
  - Judge Bias in LLM Evaluation (position bias, self-preference, bias correction methods)
  - Benchmark Contamination Detection and Avoidance (detection methods, avoidance strategies, judge-side leakage)
  - Item Response Theory (IRT) and MFRM (IRT for NLP, MFRM applications, relationship to DG-IRT)
- No tables, figures, or subsections—purely text with citations
- Relatively concise survey of the field

**4. background.tex** | **41 lines** | **~664 words**
- Titled "Confounding in LLM Evaluation" (Section 2)
- Small Figure (fig2_ovb_bias) showing sequential estimation bias vs. contamination susceptibility
- Two key equations: standard MFRM (Eq. 15) and contamination-augmented model (Eq. 24)
- Theoretical treatment of omitted variable bias (Observation 1 with formal statement)
- Detailed discussion of bias mechanism and empirical validation (r=0.86, p<0.001)
- No explicit subsections but logically organized by equation blocks and derivations
- **Potential appendix content**: The extended discussion of OVB formula and linear approximation quality (lines 32-40) could move to appendix; detailed proof of OVB formula moved to appendix

**5. method.tex** | **140 lines** | **~1458 words** (Longest main-text section)
- Three major subsections:
  - **Model Specification** (3 equations: G-MFRM Eq. 30, contamination interaction, hierarchical priors)
  - **Staged Estimation** (3-stage procedure description: Standard MFRM, exposure estimation pipeline, joint MCMC)
  - **Identifiability** (2 propositions + 1 theorem with detailed proofs)
  - **Error Propagation** (attenuation formula, empirical validation, Murphy-Topel correction)
  - **Fair Scores and Diagnostics** (interpretation section)
- Contains Table 1 (error propagation robustness across noise levels)
- Contains Table 2 (main results: correlation with human rankings)
- Contains Figure (forest plot of judge severity estimates)
- **Potential appendix content**: Identifiability proofs (lines 73-95) are already referenced to appendix; error propagation derivation (lines 96-112) and Murphy-Topel correction details (lines 113-140) could be entirely moved to appendix with just citations in main text

**6. experiments.tex** | **54 lines** | **~908 words**
- Two figures: contamination susceptibility bar plots and bias absorption visualization
- Subsections:
  - **Setup** (data/models, judges, exposure estimation, MCMC settings)
  - **Baselines and Main Results** (7 baseline methods, ranking metrics, LOO cross-validation)
  - **Error Propagation and Ablation** (error propagation validation, ablation results, judge panel composition analysis)
- Contains Table 3 (main ranking accuracy results: Kendall τ and Spearman ρ)
- Contains Figure (ablation RMSE comparison)
- Dense with empirical details and references to appendices for full diagnostic tables
- **Potential appendix content**: Detailed judge panel composition analysis (lines 54-55) showing leave-one-judge-out results; extensive ablation results already referenced to appendix; per-model breakdowns of contamination and bias metrics

**7. conclusion.tex** | **10 lines** | **~307 words**
- Brief but comprehensive summary section
- Reiterates key theoretical contribution (OVB formalization)
- Summarizes empirical findings (ranking agreement, contamination gradient, bias absorption)
- Discusses practical implications (joint modeling vs. sequential, judge panel diversity)
- Lists three open directions: domain-specific contamination decomposition, CI coverage calibration, scaling to larger benchmarks
- Clean and focused; all content is appropriate for main text

**8. limitations.tex** | **6 lines** | **~252 words**
- Discusses practical constraints: single benchmark, sparse design, exposure anchor validity
- Parameter-specific coverage analysis (θ ~90%, c_n ~71%)
- Structural issues with multiplicative coupling and HalfNormal boundary
- Power analysis implications (N≈17 for 80% power)
- Generalization caveats and self-evaluation robustness analysis reference
- All content necessary for transparency; appropriate location

**9. appendix.tex** | **511 lines** | **~4420 words** (Substantial appendix)
- 18+ labeled sections covering:
  - **Proofs**: Propositions 1-2 (identifiability), Theorem 1 (sufficient conditions, ~60 lines of proof)
  - **Theory**: OVB coefficient formula, Murphy-Topel variance correction (detailed derivation)
  - **Ablation Study**: Full ablation table + visualization comparing joint, staged, binary gating, and judge-less variants
  - **Validation**: Posterior predictive check, LOO model comparison with Pareto-k diagnostics
  - **Robustness**: Self-evaluation sensitivity, judge severity table, judge count subsampling, weight sensitivity
  - **Power Analysis**: Permutation-based power analysis to detect observed effect size
  - **Per-Model Estimates**: Full results table for 8 target models
  - **Contamination Bias Absorption**: Detailed table of bias absorption by model
  - **Synthetic Calibration**: Matched-scale validation at N=8 and N=20
  - **Prior Robustness**: Horseshoe vs. HalfNormal comparison
  - **Fit Diagnostics**: Item-level MNSQ statistics, CI coverage analysis
  - **Error Propagation Visualization**: Detailed figures and tables
  - **AI Assistant Declaration**: Disclosure of Claude use in code, writing, literature
- Well-organized and comprehensive; contains material that naturally belongs in appendix (proofs, robustness checks, implementation details)

---

### Content Relocation Recommendations

**Already appropriately in appendix (no action needed):**
- Identifiability proofs (Propositions and Theorem)
- Murphy-Topel variance correction derivation
- Synthetic calibration tables
- Robustness checks (prior, weight, judge count)
- Fit diagnostics and coverage analysis

**Candidates for appendix relocation to reduce main-text length:**

1. **From method.tex** (lines 96-112, ~400 words):
   - Error propagation bounds discussion and attenuation formula could be condensed to 1-2 lines in main text with full details in appendix
   - Would save ~150 words from main text

2. **From background.tex** (lines 30-40, ~200 words):
   - Extended discussion of linear approximation quality and Monte Carlo validation could move to appendix
   - Keep only the Observation statement in main text

3. **From experiments.tex** (lines 54-55, ~150 words):
   - Detailed leave-one-judge-out analysis for three specific judges could be summarized in main text (1-2 sentences) with full table in appendix

**Verdict**: The paper is already well-balanced. The appendix contains appropriate material (proofs, detailed robustness checks, implementation notes). The main text is densely written but not bloated—all sections contribute essential narrative. No major content needs to be moved.

---

### Summary Table

| Section | Lines | Words | Key Elements | Structure |
|---------|-------|-------|--------------|-----------|
| abstract.tex | 3 | 180 | Problem statement, method, results | Single paragraph |
| introduction.tex | 22 | 543 | Framework figure, OVB formalization, contributions | Text + 1 figure + enumerated list |
| related_work.tex | 11 | 214 | Judge bias, contamination, IRT | 3 paragraph blocks |
| background.tex | 41 | 664 | Confounding analysis, omitted variable bias | 2 equations + 1 figure + observation |
| method.tex | 140 | 1458 | G-MFRM spec, staged estimation, identifiability, error propagation | 4 subsections + 2 tables + 1 figure + 3 theorems |
| experiments.tex | 54 | 908 | Setup, baselines, main results, ablation | 3 subsections + 2 figures + 1 table |
| conclusion.tex | 10 | 307 | Summary, implications, future work | 4 paragraphs |
| limitations.tex | 6 | 252 | Design constraints, coverage issues, generalizations | Prose section |
| appendix.tex | 511 | 4420 | Proofs, robustness, validation, diagnostics | 18+ labeled sections |
| **TOTAL** | **846** | **9545** | | |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a3f25642-5e76-4efb-9a73-9a5e75811543",
  "isSidechain": true,
  "agentId": "af0b5f1dbbb0ecf84",
  "requestId": "req_011CbPZHyPHpCnfPCsmNsmTE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ec6c3e20-14cf-4e9a-8b12-628de3e34d7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/.claude/sessions/paper_agent_412cd05f",
  "sessionId": "f43f6472-0c6e-4dfb-9e17-a42387f82f06",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "buzzing-wobbling-quokka",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DvVpbDHy1yE6WsheWqYJBT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 248,
      "cache_read_input_tokens": 57456,
      "output_tokens": 2437,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 248
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 2437,
          "cache_read_input_tokens": 57456,
          "cache_creation_input_tokens": 248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 248,
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
