# Research conversation: In /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/, read ALL .tex files

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a4f6b5b2e69085d89.jsonl`
- **Structured JSON:** [`21528339d09d0af47a38.json`](../../sessions/21/21528339d09d0af47a38.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

17 recorded events

### User

_source line 1 · 2026-05-25T19:40:59.479Z_

In /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/, read ALL .tex files and extract EVERY specific number that appears. I need a comprehensive catalog.

Read these files completely:
- abstract.tex
- introduction.tex  
- method.tex
- results.tex
- discussion.tex
- conclusion.tex
- appendix.tex

For each file, list every number with its context. Include:
- Effect sizes (Cohen's d values)
- Percentages (accuracy, contamination levels)
- Counts (n=10, 14042 items, 295 items, etc.)
- Bootstrap CIs
- Standard deviations
- Model parameters (rank=16, alpha=32, etc.)
- Any other numerical values

Format: "Section: [file:line] number = context"

Be thorough - this is an audit. Don't skip any numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "da07976a-f226-4e2d-8dce-e30611d2ccf3",
  "agentId": "a4f6b5b2e69085d89",
  "type": "user",
  "uuid": "29b1ab2b-6b5f-4f28-a8f4-58db6092bde6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-25T19:41:00.874Z_

I'll read all the .tex files in the sections directory and extract every numerical value with its context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29b1ab2b-6b5f-4f28-a8f4-58db6092bde6",
  "isSidechain": true,
  "agentId": "a4f6b5b2e69085d89",
  "requestId": "req_011CbPrbNNMVoqTrGNcFxbJD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cfd9c073-5bd7-45e6-8bd4-d48aa35b88da",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DdhGWECHaDNbwX1P6Pnz1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 36740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 643,
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

_source line 3 · 2026-05-25T19:41:01.247Z_

<details open><summary>🔧 Tool call — Read · `toolu_0199oMAh4MzCyrNy3iq1vB6G`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfd9c073-5bd7-45e6-8bd4-d48aa35b88da",
  "isSidechain": true,
  "agentId": "a4f6b5b2e69085d89",
  "requestId": "req_011CbPrbNNMVoqTrGNcFxbJD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "701117d2-2d0a-4a2e-bb09-f750e8d67e63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DdhGWECHaDNbwX1P6Pnz1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 36740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 643,
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

_source line 4 · 2026-05-25T19:41:01.257Z_

<details><summary>↩ Tool result · `toolu_0199oMAh4MzCyrNy3iq1vB6G`</summary>

```text
1	Benchmark contamination in Large Language Models (LLMs) undermines evaluation validity, yet most detection methods require privileged access to training data, model internals, or output probabilities.
2	We present the first controlled characterization of Item Response Theory (IRT) person-fit statistics for detecting supervised fine-tuning (SFT) contamination, requiring only binary response patterns and calibrated four-parameter logistic item parameters; diagnostic $\theta$-anchoring requires a clean baseline.
3	A contaminated LLM produces aberrant response patterns analogous to a test-taker with item preknowledge.
4	Using $\ell_z^*$ in a matched-difference design ($\Delta\ell_z^*$) across three 7--8B model families ($n{=}10$ clean seeds per family) on MMLU (14,042 items) and ARC-Challenge (295 items), we identify three boundaries:
5	(1) model-specific $\theta$-shift dynamics, where contamination-induced ability inflation absorbs the person-fit signal; $\theta$-anchoring amplifies detection by 2.4$\times$ while reducing coefficient of variation from 60\% to 19\%;
6	(2) a detection-diagnosis tradeoff where simpler statistics yield stronger detection but lack $\ell_z^*$'s diagnostic capabilities (seen/unseen decomposition, mechanistic $\theta$-shift analysis);
7	and (3, exploratory) ability-dependent non-monotonic dose-response under free-$\theta$ estimation, driven by $\theta$-shift absorption; $\theta$-anchored analysis reveals stable positive dose-response.
8	These findings establish when and why binary response patterns carry contamination information beyond aggregate accuracy\footnote{Code and data are available at \url{https://anonymous.4open.science/r/irt_personfit_contam-6004/}.}.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "701117d2-2d0a-4a2e-bb09-f750e8d67e63",
  "isSidechain": true,
  "promptId": "da07976a-f226-4e2d-8dce-e30611d2ccf3",
  "agentId": "a4f6b5b2e69085d89",
  "type": "user",
  "uuid": "b8b28be3-1465-434e-a155-fbdda8e48f45",
  "sourceToolAssistantUUID": "701117d2-2d0a-4a2e-bb09-f750e8d67e63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T19:41:01.329Z_

<details open><summary>🔧 Tool call — Read · `toolu_014rcdij8dKTuaHv6VF3oFnB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8b28be3-1465-434e-a155-fbdda8e48f45",
  "isSidechain": true,
  "agentId": "a4f6b5b2e69085d89",
  "requestId": "req_011CbPrbNNMVoqTrGNcFxbJD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "19536d50-7a8b-431a-8a8f-d1096b2253be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DdhGWECHaDNbwX1P6Pnz1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 36740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 643,
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

_source line 6 · 2026-05-25T19:41:01.336Z_

<details><summary>↩ Tool result · `toolu_014rcdij8dKTuaHv6VF3oFnB`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	\begin{figure*}[t]
4	  \centering
5	  \includegraphics[width=\textwidth]{fig_1_composite.pdf}
6	  \caption{Overview of IRT person-fit detection. (a)~A clean model's responses track the IRT-predicted probability curve; (b)~a contaminated model shows anomalous successes on hard items (red diamonds), producing a large $|\Delta\ell_z^*|$. (c)~Effect-size landscape: baseline accuracy vs.\ Cohen's $|d|$ across model families (diamonds: 5\%, triangles: 15\%, squares: 25\%, circles: 50\%; multi-seed means where available, single-seed otherwise; values from Table~\ref{tab:cohens_d}). (d)~Dose-response trajectories; free-$\theta$ shows non-monotonic artifact, fixed-$\theta$ recovers consistent positive dose-response.}
7	  \label{fig:composite}
8	\end{figure*}
9	
10	\begin{figure*}[t]
11	  \centering
12	  \includegraphics[width=\textwidth]{fig_framework.pdf}
13	  \caption{Overview of \irtfit{}: (a)~positioning in the detection frontier by information access; (b)~pipeline from binary responses through $\ell_z^*$ person-fit analysis to detection and characterization; (c)~three behavioral boundaries discovered; (d)~recommended practitioner workflow.}
14	  \label{fig:pipeline}
15	\end{figure*}
16	
17	Benchmark contamination (the unintended inclusion of evaluation data in training corpora) poses a growing threat to LLM evaluation integrity \citep{dodge2021, magar2022, sainz2023}, as the probability of overlap increases structurally with expanding corpora and benchmarks \citep{jacovi2023, chang2024survey}.
18	Existing detection methods all require privileged access beyond binary response records: training corpora, token-level probabilities, crafted prompts, or multiple test variants (\S\ref{sec:related_work}).
19	Moreover, all log-probability-based detectors fail after RL post-training \citep{wang2025fragility}, motivating the question: \emph{what can binary response patterns alone reveal about contamination?}
20	
21	A contaminated LLM is functionally analogous to a test-taker with item preknowledge: both produce response patterns where difficult items are answered correctly through memorization rather than genuine ability (Figure~\ref{fig:composite}a--b).
22	This connection points to person-fit statistics from psychometric cheating detection \citep{drasgow1985, snijders2001, karabatsos2003}.
23	We focus on SFT-stage contamination, where benchmark answers are explicitly included in fine-tuning data, as it provides controlled ground truth and is increasingly relevant as fine-tuning-as-a-service platforms proliferate (Figure~\ref{fig:pipeline}).
24	
25	Using $\ell_z^*$ in a matched-difference design across three 7--8B model families (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B; $n{=}10$ clean seeds each) with pre-calibrated 4PL item parameters \citep{psnirt2026} on MMLU \citep{hendrycks2021mmlu} and ARC-Challenge, we identify three behavioral boundaries:
26	
27	\begin{enumerate}[leftmargin=*,nosep]
28	\item \textbf{Model-specific $\theta$-shift dynamics.} Contamination inflates ability estimates ($\hat{\theta}$), absorbing the person-fit signal; $\theta$-anchoring amplifies Qwen's multi-seed $|d|$ by 2.4$\times$ at 50\% contamination while reducing inter-seed CV from 60\% to 19\%, establishing $\theta$-anchoring as a necessary condition for reliable detection of high-ability models at high contamination. ARC-C reverses through a ceiling effect.
29	
30	\item \textbf{Detection-diagnosis tradeoff.} Simpler statistics yield stronger detection: accuracy $z$-scores produce $|d|$ values several-fold to over an order of magnitude larger than person-fit statistics, and HT generally exceeds $\ell_z^*$. Yet the diagnostic power reverses: only $\ell_z^*$ supports seen/unseen decomposition, mechanistic $\theta$-shift analysis, and sensitivity to response-pattern structure (57/60 vs.\ 4/60 flagged cells on real-world data).
31	
32	\item \textbf{Non-monotonic dose-response under free-$\theta$ (exploratory).} The Qwen dose-response ($|d|$: $4.15 \to 5.36 \to 7.44 \to 5.08$ at 5\%/15\%/25\%/50\%; 5\% is single-seed, remainder are multi-seed means) shows non-monotonicity; $\theta$-anchoring eliminates the pattern and reveals a broadly increasing dose-response ($|d|{=}12.32$ at 50\%). The non-monotonicity is a $\theta$-estimation artifact, not a detection boundary.
33	\end{enumerate}
34	
35	Our contributions are threefold:
36	(1) We provide the first empirical characterization of IRT person-fit behavior for LLM contamination, quantifying theoretically predicted phenomena ($\theta$-shift absorption, detection-diagnosis tradeoff) whose magnitudes and boundary conditions are not derivable from IRT theory alone.
37	(2) We establish that $\Delta\ell_z^*$ reliably detects SFT-stage contamination across three model families (all single-seed bootstrap 95\% CIs exclude zero, $n{=}10$).
38	(3) We document the detection-diagnosis tradeoff, clarifying what binary response patterns can and cannot reveal.
39	Findings~1--2 are confirmatory (pre-planned 15\%/50\% $\times$ 3 families); Finding~3 is exploratory (5\%/25\% added post-hoc).
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19536d50-7a8b-431a-8a8f-d1096b2253be",
  "isSidechain": true,
  "promptId": "da07976a-f226-4e2d-8dce-e30611d2ccf3",
  "agentId": "a4f6b5b2e69085d89",
  "type": "user",
  "uuid": "e7f6b93c-c25f-4e22-a1e9-b5b955f3856f",
  "sourceToolAssistantUUID": "19536d50-7a8b-431a-8a8f-d1096b2253be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T19:41:01.581Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WUM2Htd7E2NaDiqzgrWFAd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7f6b93c-c25f-4e22-a1e9-b5b955f3856f",
  "isSidechain": true,
  "agentId": "a4f6b5b2e69085d89",
  "requestId": "req_011CbPrbNNMVoqTrGNcFxbJD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "243b2afe-927d-41fb-8873-23c8f1a56c6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DdhGWECHaDNbwX1P6Pnz1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 36740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 643,
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

_source line 8 · 2026-05-25T19:41:01.588Z_

<details><summary>↩ Tool result · `toolu_01WUM2Htd7E2NaDiqzgrWFAd`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{IRT Person-Fit Framework}
5	\label{sec:framework}
6	
7	We adopt the four-parameter logistic (4PL) IRT model to characterize contamination-induced aberrance in LLM response patterns.
8	The 4PL model defines the probability that a model with ability $\theta$ answers item $i$ correctly:
9	\begin{equation}
10	  P_i(\theta) = c_i + (d_i - c_i)\,\frac{1}{1 + e^{-a_i(\theta - b_i)}}
11	  \label{eq:4pl}
12	\end{equation}
13	where $a_i$ is discrimination, $b_i$ difficulty, $c_i$ the lower asymptote (guessing), and $d_i$ the upper asymptote.
14	The 4PL extension is essential for LLM evaluation: \citet{psnirt2026} find 46\% of MMLU items have $d_i < 0.95$, meaning even high-ability models err on these items due to ambiguity or format effects; a 3PL model that forces $d_i{=}1$ misattributes such errors to low ability, inflating $\ell_z^*$ variance and reducing detection power ($+$55.7pp gain with 4PL; \S\ref{sec:degradation}).
15	Item parameters are pre-calibrated by PSN-IRT \citep{psnirt2026} from a large-scale leaderboard dataset spanning 39 models; we use these external parameters rather than re-estimating from potentially contaminated data, since our marginal maximum likelihood EM (MML-EM) refit shows discrimination recovery degrades to $r_a{=}0.127$ on contaminated leaderboard data (Appendix~\ref{app:mml_em}).
16	
17	Given item parameters and a binary response vector $\mathbf{x} = (x_1, \ldots, x_n)$, we compute the person-fit statistic $\ell_z^*$ \citep{snijders2001}, a standardized log-likelihood residual quantifying deviation between observed and expected response patterns.
18	The Snijders correction accounts for estimation uncertainty in $\hat{\theta}_{\text{MLE}}$, so that $\ell_z^* \sim \mathcal{N}(0,1)$ under the null \citep{drasgow1985, snijders2001}; \citet{magis2012} provide a detailed treatment of how response model selection and ability estimation affect $\ell_z^*$.
19	Large negative $\ell_z^*$ indicates aberrant responding (unexpected failures on easy items or unexpected successes on hard items); large positive values indicate over-consistent patterns.
20	
21	We consider two estimation modes: \emph{free-$\theta$}, where $\hat{\theta}_{\text{MLE}}$ is estimated jointly from the (potentially contaminated) response vector, and \emph{fixed-$\theta$} ($\theta$-anchoring), where $\hat{\theta}$ is held at the clean-baseline mean.
22	Under free-$\theta$, contamination inflates $\hat{\theta}$, which partially ``explains away'' anomalous successes and attenuates $\ell_z^*$; fixed-$\theta$ eliminates this absorption but requires a clean reference (\S\ref{sec:theta_dynamics}).
23	
24	\begin{figure}[t]
25	  \centering
26	  \includegraphics[width=\columnwidth]{fig_dose_response.pdf}
27	  \caption{Dose-response trajectories on MMLU. Free-$\theta$ (solid) shows non-monotonic behavior for Qwen due to $\theta$-shift absorption (shaded); fixed-$\theta$ (dashed) removes the inverted-U artifact and yields an overall positive dose-response ($|d|{=}12.32$ at 50\%). Llama's flat trajectory reflects minimal absorption. Hollow markers: single-seed ($n{=}1$); error bars: $\pm$SD ($n{=}3$).}
28	  \label{fig:dose_response}
29	\end{figure}
30	
31	\subsection{$\Delta\ell_z^*$ Matched-Difference Design}
32	\label{sec:did}
33	
34	LLM response patterns systematically violate IRT assumptions of local independence and unidimensionality.
35	In our empirical data, 57 of 60 model-benchmark cells yield $|\ell_z^*| > 1.96$ even absent contamination, rendering absolute thresholds uninformative.
36	We address this through a matched-difference design.
37	
38	For controlled experiments with clean baselines, we compute:
39	\begin{equation}
40	  \Delta\ell_z^* = \ell_{z,\text{contam}}^{*} - \bar{\ell}_{z,\text{clean}}^{*}
41	  \label{eq:delta_lz}
42	\end{equation}
43	where $\bar{\ell}_{z,\text{clean}}^{*}$ averages over $n{=}10$ clean seeds.
44	The shared model misfit cancels, isolating contamination-specific aberrance.
45	We quantify effect sizes as $d = (\ell_{z,\text{contam}}^{*} - \bar{\ell}_{z,\text{clean}}^{*})\,/\,s_{\text{clean}}$, where $s_{\text{clean}}$ is the SD of the $n{=}10$ clean-seed $\ell_z^*$ values; with a single contaminated observation per condition, $d$ is a standardized departure rather than a two-sample effect size (Hedges' $g = J \cdot d$, $J \approx 0.914$ for $n{=}10$; \citealp{hedges1981}).
46	We report percentile bootstrap 95\% CIs (10,000 resamples) reflecting clean-seed variability only; bias-corrected and accelerated (BCa) correction (Appendix~\ref{app:bca}) generally confirms conservative coverage; multi-seed contamination-run variance appears in Appendix~\ref{app:reproducibility}.
47	
48	For deployment without clean baselines, cross-benchmark comparison provides the reference: the target benchmark's $\ell_z^*$ is compared against benchmarks presumed clean from the same model.
49	Significance thresholds derive from a nonparametric bootstrap null rather than the asymptotic $\mathcal{N}(0,1)$ reference, accommodating residual model misspecification.
50	Simulation analysis (Appendix~\ref{app:local_dep}) confirms that the matched-difference design is robust to local dependence at realistic levels ($d_{\text{ratio}} \geq 0.93$ for $\sigma_\tau \leq 0.5$) and maintains ${\geq}98.5\%$ power even under contamination-specific asymmetric dependence.
51	
52	\subsection{Experimental Setup}
53	\label{sec:setup}
54	
55	\paragraph{Models and contamination.}
56	We validate on three 7--8B model families: Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, and Mistral-7B-Instruct-v0.3.
57	Each is fine-tuned with Quantized Low-Rank Adaptation (QLoRA; rank\,$=$\,16, $\alpha$\,$=$\,32; full hyperparameters in Appendix~\ref{app:hyperparams}) under clean and contaminated conditions at varying levels: at $X\%$ contamination, $X\%$ of SFT training examples are benchmark items (questions paired with gold answers in the standard evaluation format), with the remainder drawn from a general instruction-following dataset.
58	All three families are tested at 15\% and 50\% contamination.
59	Following initial observation of non-monotonic dose-response for Qwen, we added 5\% and 25\% conditions for Qwen to trace the full dose-response curve.
60	Both conditions were subsequently extended to Llama to test whether the pattern generalizes; Mistral was additionally tested at 5\% but not at 25\% due to computational constraints.
61	We train $n{=}10$ independent clean seeds per model to establish baseline variability and construct bootstrap confidence intervals.
62	Reported CIs reflect variability across $n$ clean baseline seeds; for each model family, selected contamination levels were additionally replicated with $n{=}3$ independent QLoRA seeds to assess training-run variance: Qwen at 15\%/25\%/50\%, Llama at 5\%/15\%/25\%/50\%, and Mistral at 5\%/15\%/50\% (Appendix~\ref{app:reproducibility}).
63	
64	\paragraph{Benchmarks.}
65	We evaluate on MMLU \citep{hendrycks2021mmlu} (14,042 items) and ARC-Challenge \citep{clark2018arc} (295 PSN-IRT-calibrated items), spanning two orders of magnitude in benchmark size.
66	All 4PL item parameters are from \citet{psnirt2026}.
67	ARC-Challenge experiments were conducted on Qwen only, as the primary evaluation of cross-benchmark generalizability; extending to additional families was constrained by computational budget.
68	
69	\paragraph{Post-RL extension.}
70	To probe behavior boundaries beyond SFT, we apply Group Relative Policy Optimization (GRPO; \citealp{shao2024}) to one contaminated Qwen model (15\% MMLU) for 1,500 steps, evaluating at three checkpoints.
71	This extension is $N{=}1$ (single model family, single contamination level).
72	
73	\paragraph{Evaluation protocol.}
74	Ability estimation uses maximum likelihood (MLE) with Newton--Raphson optimization on the 4PL log-likelihood.
75	For each model, we compute $\ell_z^*$ on the full benchmark response vector; seen/unseen decomposition recomputes $\ell_z^*$ on item subsets to localize the contamination signal.
76	All evaluations use greedy decoding (temperature~0) with the standard multiple-choice prompt format from the lm-evaluation-harness \citep{eval-harness}.
77	
78	\paragraph{Contamination model.}
79	QLoRA SFT on benchmark items proxies SFT-stage contamination, analogous to a test-taker with item preknowledge.
80	At each contamination level, contaminated items are shuffled into the training mixture and presented in the same question--answer format used during evaluation, maximizing the memorization signal.
81	We term contaminated items \emph{seen} and the remainder \emph{unseen}, enabling person-fit decomposition (\S\ref{sec:degradation}).
82	Findings are scoped to SFT-based contamination.
83	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "243b2afe-927d-41fb-8873-23c8f1a56c6e",
  "isSidechain": true,
  "promptId": "da07976a-f226-4e2d-8dce-e30611d2ccf3",
  "agentId": "a4f6b5b2e69085d89",
  "type": "user",
  "uuid": "151cfd7d-1bf7-4923-8538-944facfddbd6",
  "sourceToolAssistantUUID": "243b2afe-927d-41fb-8873-23c8f1a56c6e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T19:41:01.736Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CV5Nt3wvaG1s7sCctqfBSU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "151cfd7d-1bf7-4923-8538-944facfddbd6",
  "isSidechain": true,
  "agentId": "a4f6b5b2e69085d89",
  "requestId": "req_011CbPrbNNMVoqTrGNcFxbJD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ea3494d8-f864-414c-a7c0-e1b58ba89ddf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DdhGWECHaDNbwX1P6Pnz1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 36740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 643,
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

_source line 10 · 2026-05-25T19:41:01.743Z_

<details><summary>↩ Tool result · `toolu_01CV5Nt3wvaG1s7sCctqfBSU`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	\begin{table}[t]
5	\centering
6	\caption{Cohen's $d$ for $\Delta\ell_z^*$ across model families ($n{=}10$ clean seeds). Single-seed conditions: percentile bootstrap 95\% CI (10,000 resamples). $^{\dagger}$Multi-seed conditions: mean $\pm$ SD ($n{=}3$ independent runs). All single-seed CIs exclude zero.}
7	\label{tab:cohens_d}
8	\footnotesize
9	\resizebox{\columnwidth}{!}{%
10	\begin{tabular}{@{}llrrrr@{}}
11	\toprule
12	Model & Bench. & $d$ (5\%) [CI] & $d$ (15\%) [CI] & $d$ (25\%) [CI] & $d$ (50\%) [CI] \\
13	\midrule
14	Qwen$^{\dagger}$ & MMLU & $-4.15$ [$-9.9$, $-2.7$] & $-5.36$ ($\pm$1.10) & $-7.44$ ($\pm$1.86) & $-5.08$ ($\pm$3.02) \\
15	Llama$^{\dagger}$ & MMLU & $-2.57$ ($\pm$0.99) & $-2.80$ ($\pm$0.60) & $-2.56$ ($\pm$0.52) & $-2.30$ ($\pm$0.30) \\
16	Mistral$^{\dagger}$ & MMLU & $-3.83^{*}$ ($\pm$1.42) & $-3.37$ ($\pm$0.68) & --- & $-4.09$ ($\pm$0.53) \\
17	Qwen$^{\dagger}$ & ARC-C & --- & $+3.16$ [$2.0$, $9.5$] & --- & $+5.30$ [$3.6$, $15.2$] \\
18	\bottomrule
19	\multicolumn{6}{@{}l}{\scriptsize $^{\dagger}$Multi-seed conditions: means ($n{=}3$ independent runs) shown as $\pm$SD; remaining conditions are single-seed with bootstrap CIs.} \\
20	\multicolumn{6}{@{}l}{\scriptsize $^{*}$$n{=}2$ seeds. Per-seed values in Appendix~\ref{app:reproducibility}.}
21	\end{tabular}}
22	\end{table}
23	
24	\subsection{Detection Signal Across Model Families}
25	\label{sec:detection}
26	
27	Table~\ref{tab:cohens_d} presents Cohen's $d$ effect sizes for $\ell_z^*$ across three model families and two benchmarks.
28	All single-seed bootstrap CIs exclude zero, confirming that $\Delta\ell_z^*$ reliably separates contaminated from clean models at both contamination levels.
29	
30	On MMLU, effect sizes range from $|d|{=}2.30$ (Llama at 50\%) to $|d|{=}7.44$ (Qwen at 25\%), with Qwen at 5\% ($|d|{=}4.15$) confirming detection at the lowest contamination level tested. Llama ($|d|{=}2.57$/$2.80$/$2.56$/$2.30$) and Mistral ($|d|{=}3.83$/$3.37$/$4.09$) show comparable magnitudes.
31	On ARC-C (295 items), Qwen yields $|d|{=}3.16$ at 15\% and $|d|{=}5.30$ at 50\%, demonstrating that detection remains feasible even on small benchmarks when contamination is sufficiently concentrated.
32	The positive sign on ARC-C (vs.\ negative on MMLU) reflects a ceiling effect: with 89.7\% baseline accuracy, contamination pushes responses toward over-consistency rather than the unexpected-success pattern seen on MMLU.
33	
34	Clean-model $\ell_z^*$ baselines diverge substantially: Qwen ${+}8.68$ (over-consistent), Llama ${+}0.26$ (near-expected), Mistral ${+}4.02$ (Appendix~\ref{app:baseline_meaning}); seed sensitivity analysis confirms these reflect systematic misfit rather than seed artifacts (Appendix~\ref{app:seed_sensitivity}), making absolute thresholds uninformative.
35	The $\Delta\ell_z^*$ design normalizes these divergent baselines (Figure~\ref{fig:heatmap}).
36	
37	\begin{figure}[t]
38	  \centering
39	  \includegraphics[width=\columnwidth]{fig_heatmap.pdf}
40	  \caption{Cohen's $|d|$ heatmap (values from Table~\ref{tab:cohens_d}; multi-seed means where available). Blue intensity reflects effect-size magnitude. Grey cells: not tested.}
41	  \label{fig:heatmap}
42	\end{figure}
43	
44	\subsection{Model-Specific $\theta$-Shift Dynamics}
45	\label{sec:theta_dynamics}
46	
47	Contamination inflates $\hat{\theta}_{\text{MLE}}$, which ``explains away'' anomalous successes on hard items; we term this \emph{$\theta$-shift absorption}.
48	$\theta$-shift magnitude is comparable across families ($\Delta\theta{\approx}0.5$), yet fixed-$\theta$ amplification diverges markedly (Table~\ref{tab:theta_fixed}; Figure~\ref{fig:composite}c).
49	
50	$\theta$-shift absorption is the dominant source of detection variability for high-ability models at high contamination:
51	(i) fixed-$\theta$ estimation amplifies Qwen's multi-seed $|d|$ by 2.4$\times$ at 50\% ($5.08 \to 12.32$; Table~\ref{tab:theta_fixed}), while Llama shows no amplification ($0.4\times$);
52	(ii) $\theta$-anchoring reduces Qwen's inter-seed CV from 60\% to 19\%, confirming that training-run variance is driven by $\theta$-shift stochasticity rather than true signal variance;
53	(iii) the cross-model ranking under free-$\theta$ is seed-dependent at 50\%, making $\theta$-anchoring a necessary condition for reliable detection of high-ability models at high contamination.
54	
55	ARC-C reverses this pattern: despite 89.7\% baseline accuracy, contamination produces \emph{larger} effect sizes ($|d|{=}3.16$/$5.30$).
56	This ceiling effect arises because 295 items with high baseline accuracy leave minimal room for $\theta$ inflation; contamination manifests as anomalous successes on the few remaining hard items, producing disproportionately large $\ell_z^*$ shifts.
57	Detection sensitivity thus depends on the interaction between model ability and benchmark characteristics, suggesting that practitioners should interpret effect sizes relative to the specific model--benchmark pairing rather than applying universal thresholds.
58	
59	\paragraph{Seen vs.\ unseen decomposition.}
60	To localize the contamination signal, we recompute $\ell_z^*$ separately on seen and unseen item subsets.
61	At 15\% contamination, Qwen's seen-item $\ell_z^*$ shifts by $\Delta{=}{-}14.2$ while unseen items shift by only $\Delta{=}{-}1.8$ (Appendix~\ref{app:post_rl}), confirming that the person-fit signal originates predominantly from memorized items.
62	This decomposition is unique to $\ell_z^*$ among the statistics we evaluate: neither accuracy $z$-scores nor HT support item-subset analysis.
63	
64	\paragraph{Fixed-$\theta$ estimation.}
65	Table~\ref{tab:theta_fixed} compares free- and fixed-$\theta$ Cohen's $d$.
66	The amplification ratio tracks baseline $|\ell_z^*|$ monotonically: Qwen ($\ell_z^*{=}{+}8.68$) shows $2.4{\times}$ at 50\%, Mistral ($+4.02$) $1.7{\times}$, while Llama ($+0.26$) shows $0.4{\times}$ despite comparable $\theta$-shift ($\Delta\theta{=}0.52$).
67	Fixed-$\theta$ is thus a targeted remedy for models with substantial baseline misfit, not a universal one.
68	
69	\begin{table}[t]
70	\centering
71	\caption{Free-$\theta$ vs.\ fixed-$\theta$ Cohen's $|d|$ on MMLU. Qwen$^{\S}$: multi-seed mean ($n{=}3$); Llama and Mistral: seed-42 single run. Fixed-$\theta$ anchors $\hat{\theta}$ at the clean-model mean, eliminating $\theta$-shift absorption.}
72	\label{tab:theta_fixed}
73	\footnotesize
74	\resizebox{\columnwidth}{!}{%
75	\begin{tabular}{@{}lcccc@{}}
76	\toprule
77	Model & $|d_{\text{free}}|$ & $|d_{\text{fixed}}|$ & Ratio & Fixed 95\% CI / SD \\
78	\midrule
79	\multicolumn{5}{@{}l}{\textit{5\% contamination}} \\
80	Qwen & 4.15 & 3.52 & 0.8$\times$ & [2.9, 5.7] \\
81	\addlinespace
82	\multicolumn{5}{@{}l}{\textit{15\% contamination}} \\
83	Qwen$^{\S}$ & 5.36 & 6.85 & 1.3$\times$ & ($\pm$1.80) \\
84	Llama & 2.11 & 0.58 & 0.3$\times$ & [0, 2.37]$^{\dagger}$ \\
85	Mistral$^{\ddagger}$ & 2.64 & 2.69 & 1.0$\times$ & [1.53, 9.06] \\
86	\addlinespace
87	\multicolumn{5}{@{}l}{\textit{50\% contamination}} \\
88	Qwen$^{\S}$ & 5.08 & 12.32 & 2.4$\times$ & ($\pm$2.38) \\
89	Llama & 2.33 & 0.84 & 0.4$\times$ & [0.17, 2.97] \\
90	Mistral$^{\ddagger}$ & 3.50 & 5.80 & 1.7$\times$ & [3.87, 18.45] \\
91	\bottomrule
92	\multicolumn{5}{@{}l}{\scriptsize $^{\dagger}$CI includes zero.} \\
93	\multicolumn{5}{@{}l}{\scriptsize $^{\S}$Multi-seed mean ($n{=}3$); CI column shows $\pm$SD of fixed-$\theta$ $|d|$.} \\
94	\multicolumn{5}{@{}l}{\scriptsize $^{\ddagger}$Fixed-$\theta$: 6 seeds (response vectors from seeds 4--7 excluded due to incomplete evaluation runs); free-$\theta$ uses all 10.} \\
95	\multicolumn{5}{@{}p{0.9\columnwidth}}{\scriptsize $d_{\text{free}}$ CIs omitted; multi-seed means in Table~\ref{tab:cohens_d}.}
96	\end{tabular}}
97	\end{table}
98	
99	\subsection{Detection-Diagnosis Tradeoff}
100	\label{sec:degradation}
101	
102	Table~\ref{tab:degradation} compares three statistics: $\ell_z^*$ (4PL parameters), HT (difficulty only), and accuracy $z$-scores (no item parameters).
103	For pure detection, simpler statistics are more powerful: accuracy $z$-scores yield $|d|$ values up to an order of magnitude larger than person-fit statistics, because cross-seed accuracy variance is near-zero ($\text{SD}{\approx}0.0003$ for Qwen clean seeds).
104	These extreme effect sizes reflect the controlled setting where training-run variance is minimal; in deployment without matched clean baselines, accuracy $z$-scores would lack this stability.
105	HT generally exceeds $\ell_z^*$, since HT is not attenuated by the Snijders correction.
106	
107	Yet the diagnostic power reverses.
108	$\ell_z^*$ uniquely supports (a)~\emph{seen/unseen decomposition}, though item-level detection is near-random (AUROC${\approx}0.53$; Appendix~\ref{app:item_auroc}); (b)~\emph{$\theta$-shift mechanism} (\S\ref{sec:theta_dynamics}); and (c)~\emph{structural sensitivity}: $\ell_z^*$ flags 57/60 leaderboard cells as aberrant (Figure~\ref{fig:leaderboard_heatmap}) vs.\ 4/60 for accuracy $z$-scores \citep{stonge2011}.
109	In practice, accuracy $z$-scores screen candidates; $\ell_z^*$ then characterizes whether the signal reflects $\theta$-shift absorption or direct memorization.
110	Within the IRT family, 4PL gains $+$55.7pp power over 3PL on MMLU at 15\% contamination ($96.9\%$ vs.\ $41.2\%$; Appendix~\ref{app:4pl_ablation}), because 46\% of MMLU items have upper asymptote $d < 0.95$; the advantage persists across benchmarks (HellaSwag $+$34.3pp, GSM8K $+$20.7pp).
111	
112	\begin{table}[t]
113	\centering
114	\caption{Detection-diagnosis tradeoff on MMLU: Cohen's $|d|$ across three statistics. Qwen$^\dagger$: multi-seed means ($n{=}3$); Llama and Mistral: seed-42 single run with bootstrap CIs.}
115	\label{tab:degradation}
116	\footnotesize
117	\begin{tabular}{@{}llrr@{}}
118	\toprule
119	Model & Statistic & $|d|$ (15\%) & $|d|$ (50\%) \\
120	\midrule
121	Qwen$^\dagger$ & $\ell_z^*$ & $5.36$ ($\pm$1.10) & $5.08$ ($\pm$3.02) \\
122	     & HT & $5.83$ ($\pm$1.30) & $5.29$ ($\pm$3.41) \\
123	     & Acc.\ $z$ & $45.0$ ($\pm$2.5) & $70.0$ ($\pm$1.1) \\
124	\addlinespace
125	Llama & $\ell_z^*$ & $2.11$ [$1.4$, $4.8$] & $2.33$ [$1.6$, $5.1$] \\
126	      & HT & $2.45$ [$1.5$, $4.3$] & $3.07$ [$1.9$, $5.3$] \\
127	      & Acc.\ $z$ & $22.5$ [$13.6$, $47.0$] & $32.8$ [$19.8$, $68.6$] \\
128	\addlinespace
129	Mistral & $\ell_z^*$ & $2.64^{\ddagger}$ & $3.50$ [$2.1$, $9.4$] \\
130	      & HT & $4.36$ [$1.2$, $7.0$] & $5.89$ [$1.9$, $9.4$] \\
131	      & Acc.\ $z$ & $7.81$ [$4.4$, $14.4$] & $16.6$ [$9.7$, $34.6$] \\
132	\bottomrule
133	\multicolumn{4}{@{}p{0.9\columnwidth}}{\scriptsize $^\dagger$Per-seed values in Appendix~\ref{app:reproducibility}. Bootstrap CIs: 10{,}000 resamples over $n{=}10$ clean seeds. $^{\ddagger}$Seed-42 single run; multi-seed $|d|{=}3.37$ ($\pm$0.68) in Table~\ref{tab:cohens_d}.}
134	\end{tabular}
135	\end{table}
136	
137	\begin{figure}[t]
138	  \centering
139	  \includegraphics[width=\columnwidth]{fig_4_model_heatmap.pdf}
140	  \caption{$\ell_z^*$ heatmap for 12 leaderboard models across five benchmarks. 57/60 cells exceed $|\ell_z^*| > 1.96$, indicating pervasive IRT assumption violations even absent contamination. Details in Appendix~\ref{app:leaderboard_aberrance}.}
141	  \label{fig:leaderboard_heatmap}
142	\end{figure}
143	
144	\subsection{Ability-Dependent Non-Monotonic Dose-Response}
145	\label{sec:inverted_u}
146	
147	As an exploratory observation, the free-$\theta$ dose-response is non-monotonic for Qwen.
148	Figure~\ref{fig:dose_response} plots the dose-response trajectory, combining the single-seed 5\% estimate (hollow marker) with multi-seed means at 15\%/25\%/50\% ($|d|$: $4.15 \to 5.36 \to 7.44 \to 5.08$), showing signal peaking at 25\% before declining; inter-seed variance at 50\% is high (CV${=}$60\%, range $[1.90, 7.91]$).
149	This non-monotonicity is a $\theta$-estimation artifact: fixed-$\theta$ eliminates the inverted-U ($|d|{=}12.32$ at 50\%, CV reduced to 19\%).
150	Llama's flat trajectory ($|d|{\approx}2.3$--$2.8$) is consistent with its near-zero baseline $\ell_z^*$: the divergence is fully explained by baseline ability differences.
151	Simulation corroborates: two-sided testing achieves ${>}$93\% power at all levels on MMLU (Appendix~\ref{app:simulation}).
152	These results demonstrate that non-monotonic dose-response is not a fundamental limitation of person-fit statistics but a predictable consequence of free-$\theta$ estimation in high-ability models, and that $\theta$-anchoring provides a principled correction.
153	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea3494d8-f864-414c-a7c0-e1b58ba89ddf",
  "isSidechain": true,
  "promptId": "da07976a-f226-4e2d-8dce-e30611d2ccf3",
  "agentId": "a4f6b5b2e69085d89",
  "type": "user",
  "uuid": "931bae34-27d4-4270-a85e-9e2de38f06ce",
  "sourceToolAssistantUUID": "ea3494d8-f864-414c-a7c0-e1b58ba89ddf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T19:41:01.937Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BJ9MMZu5LQGssvPBLNxfQi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "931bae34-27d4-4270-a85e-9e2de38f06ce",
  "isSidechain": true,
  "agentId": "a4f6b5b2e69085d89",
  "requestId": "req_011CbPrbNNMVoqTrGNcFxbJD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d5d454e4-5043-46a9-863f-50d5dee0f1f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DdhGWECHaDNbwX1P6Pnz1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 36740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 643,
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

_source line 12 · 2026-05-25T19:41:01.943Z_

<details><summary>↩ Tool result · `toolu_01BJ9MMZu5LQGssvPBLNxfQi`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Detection vs.\ diagnosis.}
4	The detection-diagnosis tradeoff reveals a design tension absent from prior contamination detection work.
5	Simpler statistics (accuracy $z$-scores, HT) detect contamination more powerfully because they are not attenuated by the Snijders correction or inflated by $\theta$-shift absorption.
6	Yet $\ell_z^*$ provides unique mechanistic insight invisible to non-IRT statistics: $\theta$-shift analysis reveals \emph{why} detection varies across models (baseline ability determines absorption magnitude), seen/unseen decomposition localizes the signal source, and 4PL modeling captures ceiling effects that 3PL misses ($+$55.7pp power on MMLU).
7	Our contribution lies not in proposing a new detection method but in quantifying these theoretically predicted phenomena where magnitudes are not derivable from IRT theory alone.
8	
9	\paragraph{Practical implications.}
10	For practitioners, we recommend a two-stage workflow: (i)~screen with accuracy $z$-scores, which require no item parameters and produce the largest effect sizes; (ii)~characterize flagged models with $\ell_z^*$ to determine whether the signal reflects $\theta$-shift absorption (high-ability model, large $\Delta\theta$) or direct memorization (anomalous successes on hard items without commensurate $\theta$ inflation).
11	$\theta$-anchoring is necessary to stabilize detection for high-ability models (free-$\theta$ CV up to 60\% vs.\ 19\% under $\theta$-fixed; \S\ref{sec:theta_dynamics}).
12	Universal baseline misfit (57/60 cells flagged; Figure~\ref{fig:leaderboard_heatmap}) means absolute $\ell_z^*$ thresholds cannot be used directly; the $\Delta\ell_z^*$ matched-difference design or cross-benchmark comparison is required.
13	
14	\paragraph{Robustness and complementarity.}
15	PSN-IRT provides pre-calibrated 4PL parameters \citep{psnirt2026} that are robust to estimation noise: $\pm$10\% parameter perturbation produces $<$4\% bias in fixed-$\theta$ Cohen's $d$ (Appendix~\ref{app:param_perturb}), because the matched-difference design cancels shared parameter error.
16	Requiring only binary response patterns and an external item bank, $\ell_z^*$ occupies a unique position at the minimal-access end of the detection frontier: it complements logit-based methods \citep{minkprob2024,constat2024} that fail after RL post-training \citep{wang2025fragility}.
17	Our GRPO pilot illustrates this complementarity: Min-K\% AUC drops to chance ($0.493$) after 500 RL steps, while the $\ell_z^*$ response-pattern gap persists at ${\sim}3.3$ across all checkpoints (Figure~\ref{fig:grpo}).
18	This structural invariance (RL reshapes token-level distributions but preserves binary correctness anomalies) suggests that person-fit statistics may remain informative in settings where all probability-based detectors fail, though this $N{=}1$ observation requires multi-family validation.
19	
20	\begin{figure}[t]
21	  \centering
22	  \includegraphics[width=\columnwidth]{fig_grpo.pdf}
23	  \caption{Post-RL trajectory (Qwen, 15\% MMLU). GRPO erases the accuracy gap ($11.4\text{pp} \to 2.1\text{pp}$) while the $\ell_z^*$ gap persists (${\sim}3.3$). $N{=}1$; Appendix~\ref{app:post_rl}.}
24	  \label{fig:grpo}
25	\end{figure}
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5d454e4-5043-46a9-863f-50d5dee0f1f6",
  "isSidechain": true,
  "promptId": "da07976a-f226-4e2d-8dce-e30611d2ccf3",
  "agentId": "a4f6b5b2e69085d89",
  "type": "user",
  "uuid": "e7eb43dc-8bf6-494c-89bc-02cd287275a8",
  "sourceToolAssistantUUID": "d5d454e4-5043-46a9-863f-50d5dee0f1f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T19:41:02.358Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K3y36rMeRgVN2M2wkbcsdc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7eb43dc-8bf6-494c-89bc-02cd287275a8",
  "isSidechain": true,
  "agentId": "a4f6b5b2e69085d89",
  "requestId": "req_011CbPrbNNMVoqTrGNcFxbJD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4eee9918-edd7-4af9-a15b-68c3a903520f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DdhGWECHaDNbwX1P6Pnz1a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 36740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 643,
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

_source line 14 · 2026-05-25T19:41:02.367Z_

<details><summary>↩ Tool result · `toolu_01K3y36rMeRgVN2M2wkbcsdc`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We presented the first empirical characterization of IRT person-fit statistics for LLM benchmark contamination detection, evaluating $\ell_z^*$ across three 7--8B model families (Qwen, Llama, Mistral), two benchmarks (MMLU, ARC-C), and four contamination levels (5\%--50\%).
4	Our controlled experiments reveal three behavioral boundaries: (i)~$\theta$-shift absorption, where contamination inflates ability estimates and attenuates person-fit signals in a model-dependent manner, necessitating $\theta$-anchoring for high-ability models; (ii)~a detection-diagnosis tradeoff, where simpler statistics detect more powerfully but only $\ell_z^*$ supports mechanistic analysis; and (iii)~non-monotonic dose-response under free-$\theta$ estimation, which is a $\theta$-estimation artifact eliminated by anchoring.
5	These findings establish that binary response patterns, combined with externally calibrated item parameters, carry sufficient information for contamination detection, though diagnostic $\theta$-anchoring additionally requires a clean baseline; detection and diagnosis require different tools.
6	
7	A preliminary post-RL pilot suggests person-fit anomalies persist after RL, complementing logit-based methods that fail in this setting.
8	Future work should extend to larger models, pretraining-stage contamination, and multi-family post-RL validation.
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4eee9918-edd7-4af9-a15b-68c3a903520f",
  "isSidechain": true,
  "promptId": "da07976a-f226-4e2d-8dce-e30611d2ccf3",
  "agentId": "a4f6b5b2e69085d89",
  "type": "user",
  "uuid": "13738a4e-b157-41b1-823b-10909024354b",
  "sourceToolAssistantUUID": "4eee9918-edd7-4af9-a15b-68c3a903520f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T19:41:02.509Z_

<details open><summary>🔧 Tool call — Read · `toolu_01UvLFEUdiDSgRGdbFhSq6gg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13738a4e-b157-41b1-823b-10909024354b",
  "isSidechain": true,
  "agentId": "a4f6b5b2e69085d89",
  "requestId": "req_011CbPrbNNMVoqTrGNcFxbJD",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ca4a0a05-9176-46b0-9660-42b97743eb11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DdhGWECHaDNbwX1P6Pnz1a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 643,
      "cache_read_input_tokens": 36740,
      "output_tokens": 565,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 643
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 565,
          "cache_read_input_tokens": 36740,
          "cache_creation_input_tokens": 643,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 643,
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

_source line 16 · 2026-05-25T19:41:02.896Z_

<details><summary>↩ Tool result · `toolu_01UvLFEUdiDSgRGdbFhSq6gg`</summary>

```text
1	\section{Simulation Validation}
2	\label{app:simulation}
3	
4	Under the null (no contamination), bootstrap $\ell_z^*$ tracks $\mathcal{N}(0,1)$: mean bias 0.041 and standard deviation 1.003 on MMLU.
5	Kolmogorov--Smirnov rejection rates vary with benchmark size: 8.3\% for MMLU and HellaSwag ($n > 10{,}000$), 50.0\% for GSM8K ($n = 1{,}319$), 58.3\% for ARC-C ($n = 295$), and 75.0\% for HumanEval ($n = 164$).
6	$\ell_z^*$ is well-calibrated for benchmarks with $n \geq 10{,}000$ items; smaller benchmarks show increasing finite-sample deviations from normality.
7	
8	Two-sided testing eliminates the inverted-U artifact: MMLU achieves 97.8\% power at 15\% contamination and sustains ${>}$93\% at all levels.
9	Power scales with $\sqrt{n}$, as predicted by the noncentrality parameter $\delta \propto \sqrt{n}$.
10	The empirical power function, derived via Gauss--Hermite quadrature ($K=30$) over the ability distribution, achieves $R^2 = 0.957$ against simulated values, with approximate minimum benchmark size of $n \geq 7{,}958$ items for 80\% power at 15\% contamination under MMLU item parameters.
11	
12	\section{4PL vs.\ 3PL Ablation Details}
13	\label{app:4pl_ablation}
14	
15	Table~\ref{tab:4pl_3pl_power} reports detection power (proportion of 2{,}000 simulation replicates rejecting $H_0$ at $\alpha{=}0.05$, two-sided) for 4PL and 3PL parameterizations across five benchmarks and seven contamination levels.
16	The 4PL model yields higher power than 3PL at every non-trivial contamination level on every benchmark.
17	The advantage is largest on MMLU and HellaSwag, where upper-asymptote ($d < 1$) violations are most prevalent, and smallest on ARC-Challenge and HumanEval, where limited item counts constrain power under both parameterizations.
18	
19	Power is non-monotonic at 75\% contamination under 4PL on four of five benchmarks (e.g., MMLU: $.952 \to .938$; GSM8K: $.846 \to .802$).
20	This reflects the $\theta$-shift boundary condition described in \S\ref{sec:inverted_u}: at high contamination fractions, re-estimated $\hat{\theta}$ absorbs part of the aberrance signal, reducing $|\ell_z^*|$.
21	At 100\% contamination, all items are seen and power reaches 1.000 trivially.
22	The 4PL advantage over 3PL depends on accurate estimation of the upper asymptote $d$; with estimation error exceeding ${\sim}10\%$, the effective model behavior approaches 3PL ($d{=}1$) and the power gain diminishes.
23	PSN-IRT's large calibration sample ($12{+}$ models per item) typically yields $d$ standard errors well below this threshold.
24	
25	\begin{table*}[t]
26	\centering
27	\caption{Detection power (proportion rejecting $H_0$ at $\alpha{=}0.05$) under 4PL and 3PL parameterizations across benchmarks and contamination levels ($n{=}2{,}000$ replicates per cell). Bold indicates the 4PL advantage exceeds 5\,pp.}
28	\label{tab:4pl_3pl_power}
29	\small
30	\begin{tabular}{@{}llccccccc@{}}
31	\toprule
32	Benchmark & IRT & 5\% & 10\% & 15\% & 25\% & 50\% & 75\% & 100\% \\
33	\midrule
34	MMLU & 4PL & \textbf{.476} & \textbf{.848} & \textbf{.969} & \textbf{.983} & \textbf{.952} & \textbf{.938} & 1.00 \\
35	     & 3PL & .227 & .340 & .412 & .521 & .676 & .770 & 1.00 \\
36	\addlinespace
37	HellaSwag & 4PL & \textbf{.251} & \textbf{.454} & \textbf{.656} & \textbf{.915} & \textbf{.939} & \textbf{.919} & 1.00 \\
38	          & 3PL & .167 & .241 & .313 & .368 & .508 & .642 & 1.00 \\
39	\addlinespace
40	GSM8K & 4PL & \textbf{.156} & \textbf{.309} & \textbf{.492} & \textbf{.737} & \textbf{.846} & \textbf{.802} & 1.00 \\
41	      & 3PL & .102 & .172 & .285 & .396 & .567 & .577 & 1.00 \\
42	\addlinespace
43	ARC-C & 4PL & .057 & .075 & .087 & \textbf{.130} & \textbf{.285} & \textbf{.493} & 1.00 \\
44	      & 3PL & .054 & .062 & .071 & .076 & .110 & .102 & 1.00 \\
45	\addlinespace
46	HumanEval & 4PL & .076 & .121 & \textbf{.197} & \textbf{.302} & \textbf{.554} & \textbf{.521} & 1.00 \\
47	          & 3PL & .063 & .086 & .120 & .182 & .281 & .315 & 1.00 \\
48	\bottomrule
49	\end{tabular}
50	\end{table*}
51	
52	\section{Seed Sensitivity Analysis}
53	\label{app:seed_sensitivity}
54	
55	\paragraph{Clean-baseline variability.}
56	Table~\ref{tab:seed_sensitivity} reports $\ell_z^*$, accuracy, and $\hat{\theta}_{\text{MLE}}$ across three independent QLoRA runs (seeds 42, 123, 456).
57	For Qwen2.5-7B, $\ell_z^*$ ranges from $7.05$ (seed 123) to $9.53$ (seed 456); the lower value of seed 123 likely reflects seed-specific training dynamics (random initialization, data ordering), but all three seeds produce $\ell_z^* \gg 1.96$, confirming that the elevated baseline reflects systematic model--benchmark misfit rather than seed-specific artifacts.
58	Llama-3.1-8B shows $\ell_z^*$ near zero ($-0.14 \pm 0.97$), consistent with lower baseline misfit.
59	Accuracy variability is negligible for both families (CV $< 0.004$).
60	
61	\begin{table}[t]
62	\centering
63	\caption{Seed sensitivity analysis for clean baseline across three independent runs (seeds 42, 123, 456). CV = coefficient of variation ($\mathrm{std}/|\mathrm{mean}|$). These $n{=}3$ pilot results are superseded by the $n{=}10$ analysis in \S\ref{sec:detection}; retained for methodological transparency.}
64	\label{tab:seed_sensitivity}
65	\footnotesize
66	\resizebox{\columnwidth}{!}{%
67	\begin{tabular}{@{}llcccc@{}}
68	\toprule
69	Model & Metric & Mean & Std & Range & CV \\
70	\midrule
71	Qwen2.5-7B & $\ell_z^*$ & 8.684 & 1.412 & 2.475 & 0.163 \\
72	 & Accuracy & 0.679 & 0.000 & 0.001 & 0.001 \\
73	 & $\hat{\theta}_{\mathrm{MLE}}$ & $-$0.097 & 0.012 & 0.023 & 0.119 \\
74	\midrule
75	Llama-3.1-8B & $\ell_z^*$ & $-$0.141 & 0.965 & 1.929 & 6.860 \\
76	 & Accuracy & 0.594 & 0.002 & 0.004 & 0.004 \\
77	 & $\hat{\theta}_{\mathrm{MLE}}$ & $-$0.645 & 0.019 & 0.036 & 0.029 \\
78	\bottomrule
79	\end{tabular}}
80	\end{table}
81	
82	\paragraph{Cohen's $d$ confidence intervals.}
83	Table~\ref{tab:cohens_d_ci} reports Cohen's $d$ effect sizes with both analytic and bootstrap 95\% confidence intervals.
84	Analytic CIs use $d \pm t_{0.025,\,\text{df}=2} \cdot \text{SE}_d$; with only $n{=}3$ clean seeds (df${=}2$), the critical value $t_{0.025,2} = 4.303$ produces intervals wide enough to cross zero in all four conditions.
85	This is a known limitation of small-sample $t$-based intervals rather than evidence of null effects.
86	Bootstrap CIs (10{,}000 resamples with replacement from the three clean seeds) provide a nonparametric alternative: all four bootstrap intervals exclude zero, supporting the conclusion that contamination produces a reliably detectable signal despite the small reference sample.
87	
88	\begin{table}[t]
89	\centering
90	\caption{Cohen's $d$ with 95\% confidence intervals for contaminated conditions relative to clean baselines ($n{=}3$ seeds). Analytic CIs use $t_{0.025, \text{df}=2}$; bootstrap CIs use 10{,}000 resamples. These $n{=}3$ pilot results are superseded by the $n{=}10$ analysis in \S\ref{sec:detection}; retained for methodological transparency.}
91	\label{tab:cohens_d_ci}
92	\footnotesize
93	\resizebox{\columnwidth}{!}{%
94	\begin{tabular}{@{}llccc@{}}
95	\toprule
96	Model & Cond. & $d$ & Analytic CI & Bootstrap CI \\
97	\midrule
98	Qwen & 15\% & $-$3.42 & [$-$9.92, 3.08] & [$-$3.45, $-$2.82] \\
99	 & 50\% & $-$0.99 & [$-$4.02, 2.04] & [$-$0.99, $-$0.41] \\
100	\midrule
101	Llama & 15\% & $-$2.95 & [$-$8.70, 2.80] & [$-$5.89, $-$2.29] \\
102	 & 50\% & $-$3.31 & [$-$9.63, 3.01] & [$-$6.47, $-$2.59] \\
103	\bottomrule
104	\end{tabular}}
105	\end{table}
106	
107	\paragraph{Cross-family consistency.}
108	Table~\ref{tab:cross_family} confirms that both model families produce large negative Cohen's $d$ under contamination.
109	The $|\Delta d| = 2.32$ gap at 50\% contamination reflects Qwen's non-monotonic dose-response (the $\theta$-shift boundary condition; \S\ref{sec:inverted_u}), not a failure of detection robustness---both families remain well above conventional large-effect thresholds ($|d| > 0.8$) at both contamination levels.
110	
111	\begin{table}[t]
112	\centering
113	\caption{Cross-family consistency of contamination detection ($n{=}3$ pilot). Both families show large negative $d$ under contamination. Superseded by $n{=}10$ results in \S\ref{sec:detection}; retained for methodological transparency.}
114	\label{tab:cross_family}
115	\small
116	\begin{tabular}{@{}lcccl@{}}
117	\toprule
118	Condition & Qwen $d$ & Llama $d$ & $|\Delta d|$ & Consistent? \\
119	\midrule
120	15\% contam. & $-$3.42 & $-$2.95 & 0.47 & Yes \\
121	50\% contam. & $-$0.99 & $-$3.31 & 2.32 & Yes \\
122	\bottomrule
123	\end{tabular}
124	\end{table}
125	
126	\section{Baseline $\ell_z^*$ Interpretation}
127	\label{app:baseline_meaning}
128	
129	The baseline $\ell_z^*$ value reflects a model's difficulty-ordering consistency under the 4PL model, not its accuracy alone.
130	In the PSN-IRT leaderboard data (12 models $\times$ 5 benchmarks, distinct from our controlled experiments), Mistral ($\text{acc}{=}0.514$, lowest among the 12 models) exhibits $\ell_z^*{=}{+}5.42$ (second highest), because its response pattern follows the IRT-predicted difficulty ordering more closely than higher-accuracy models whose responses violate the assumed item structure.
131	This dissociation explains why Mistral produces the strongest contamination signal despite the lowest accuracy: its lower baseline ability ($\hat{\theta}{=}{-}1.16$) provides greater $\theta$-shift headroom.
132	
133	\section{Leaderboard Aberrance Analysis}
134	\label{app:leaderboard_aberrance}
135	
136	We computed $\ell_z^*$ and accuracy $z$-scores for all 12 models $\times$ 5 benchmarks $=$ 60 cells in the PSN-IRT leaderboard dataset.
137	Using the standard $|\ell_z^*| > 1.96$ threshold ($\alpha{=}0.05$, two-tailed), 57 of 60 cells are flagged as aberrant, indicating pervasive IRT assumption violations in production LLM responses.
138	In contrast, accuracy $z$-scores ($|z| > 1.96$) flag only 4 of 60 cells.
139	This stark asymmetry---95\% aberrance by $\ell_z^*$ versus 7\% by accuracy---motivates the $\Delta\ell_z^*$ matched-difference design (\S\ref{sec:did}), which sidesteps absolute thresholds by comparing each model against its own clean baseline.
140	Figure~\ref{fig:leaderboard_heatmap} visualizes this pattern.
141	
142	\section{Item-Level Detection Results}
143	\label{app:item_auroc}
144	
145	Table~\ref{tab:item_auroc} reports item-level contamination detection performance at 15\% contamination on MMLU.
146	All methods perform near random (AUROC $\leq 0.63$), confirming that contamination is diffuse across the response pattern and that model-level aggregation via $\ell_z^*$ is essential.
147	
148	An accuracy $z$-score baseline yields $z{=}160$ at 15\% contamination, but this reflects near-zero cross-seed accuracy variance ($\text{std}{=}0.0003$), not genuine discriminability.
149	In deployment, accuracy variability from prompt format, evaluation harness, and hardware differences inflates the denominator, collapsing the $z$-score.
150	
151	\begin{table}[t]
152	\centering
153	\caption{Item-level contamination detection (AUROC) at 15\% contamination on MMLU.}
154	\label{tab:item_auroc}
155	\footnotesize
156	\begin{tabular}{@{}lc@{}}
157	\toprule
158	Method & AUROC \\
159	\midrule
160	Random baseline & 0.50 \\
161	$\ell_z^*$ itemwise & 0.53 \\
162	LR cross-model & 0.59 \\
163	RF cross-model & 0.63 \\
164	\bottomrule
165	\end{tabular}
166	\end{table}
167	
168	\section{Robustness Analysis}
169	\label{app:robustness}
170	
171	\subsection{$\Delta\ell_z^*$ Under Local Dependence}
172	\label{app:local_dep}
173	
174	IRT person-fit statistics assume local independence---conditional on $\theta$, item responses are independent.
175	LLM benchmarks violate this assumption through topical clustering (e.g., MMLU subjects); resampling-based approaches can provide valid person-fit assessment even under such violations \citep{sinharay2016}.
176	We evaluate whether the $\Delta\ell_z^*$ matched-difference design is robust to local dependence (LD) via two simulation scenarios on 14,042 MMLU items with 1,000 replications each.
177	
178	\paragraph{Shared LD.}
179	Clean and contaminated conditions share identical testlet structure (${\sim}200$ testlets of ${\sim}70$ items, random effect $\gamma_t \sim \mathcal{N}(0, \sigma_\tau)$).
180	Table~\ref{tab:ld_shared} reports absolute $\ell_z^*$ Type~I error and the ratio of $\Delta\ell_z^*$ effect size ($d$) to the no-LD baseline.
181	While absolute $\ell_z^*$ Type~I error inflates severely under LD (0.043$\to$0.939 at $\sigma{=}1.0$), the $\Delta\ell_z^*$ design maintains detection power: $d_{\text{ratio}} \geq 0.93$ for $\sigma_\tau \leq 0.5$ (realistic range), confirming that shared misfit is cancelled by the matched-difference design.
182	
183	\begin{table}[t]
184	\centering
185	\caption{Robustness of $\Delta\ell_z^*$ to shared local dependence (1,000 replications, MMLU). $d_{\text{ratio}}$: effect size relative to the $\sigma_\tau{=}0$ baseline.}
186	\label{tab:ld_shared}
187	\footnotesize
188	\begin{tabular}{@{}lccc@{}}
189	\toprule
190	$\sigma_\tau$ & Abs.\ $\ell_z^*$ Type~I & $d_{\text{ratio}}$ (15\%) & $d_{\text{ratio}}$ (50\%) \\
191	\midrule
192	0.0 & 0.043 & 1.000 & 1.000 \\
193	0.3 & 0.110 & 1.002 & 1.038 \\
194	0.5 & 0.454 & 0.934 & 1.028 \\
195	1.0 & 0.939 & 0.705 & 1.061 \\
196	\bottomrule
197	\end{tabular}
198	\end{table}
199	
200	\paragraph{Asymmetric LD.}
201	In the second scenario, contaminated models' seen items share an additional memory factor ($\gamma_{\text{mem}} \sim \mathcal{N}(0, \sigma_{\text{mem}})$), simulating contamination-specific LD not present in clean conditions ($\sigma_\tau{=}0.5$ fixed).
202	Table~\ref{tab:ld_asym} shows that $\Delta\ell_z^*$ maintains ${\geq}98.5\%$ power across all conditions, even when contamination introduces asymmetric dependence among seen items.
203	
204	\begin{table}[t]
205	\centering
206	\caption{$\Delta\ell_z^*$ detection under asymmetric local dependence ($\sigma_\tau{=}0.5$, contamination-specific memory factor $\sigma_{\text{mem}}$; 1,000 replications, MMLU).}
207	\label{tab:ld_asym}
208	\footnotesize
209	\begin{tabular}{@{}lcccc@{}}
210	\toprule
211	$\sigma_{\text{mem}}$ & Power (15\%) & $d$ (15\%) & Power (50\%) & $d$ (50\%) \\
212	\midrule
213	0.5 & 0.987 & $-$2.107 & 0.991 & $-$2.337 \\
214	1.0 & 0.993 & $-$2.104 & 0.985 & $-$1.587 \\
215	\bottomrule
216	\end{tabular}
217	\end{table}
218	
219	\subsection{Sensitivity to Item Parameter Estimation Error}
220	\label{app:param_perturb}
221	
222	PSN-IRT item parameters carry estimation error from the calibration sample.
223	We evaluate detection sensitivity by adding joint noise to all four parameters: multiplicative perturbation $p' = p \cdot (1 + \mathcal{N}(0, \sigma))$ for $a$, $c$, and $d$; additive perturbation $b' = b + \sigma \cdot \mathcal{N}(0, 1)$ for difficulty.
224	Tables~\ref{tab:param_noise_free} and \ref{tab:param_noise_fixed} report results over 100 trials using Qwen MMLU response vectors.
225	
226	Detection of 15\% contamination is robust to parameter noise under free-$\theta$ (17.4\% bias at $\sigma{=}10\%$, $|d|$ still ${>}5$; Table~\ref{tab:param_noise_free}).
227	The 50\% contamination condition under free-$\theta$ is fragile---consistent with its already-weak signal due to $\theta$-shift absorption (\S\ref{sec:inverted_u}).
228	
229	Under $\theta$-fixed estimation (Table~\ref{tab:param_noise_fixed}), detection is highly robust: 10\% perturbation produces ${<}4\%$ bias in Cohen's $d$, with worst-case $|d| = 3.73$ (15\% contamination) and $12.20$ (50\%)---both far exceeding conventional thresholds.
230	This contrasts sharply with free-$\theta$ estimation, where 50\% contamination Cohen's $d$ collapses to near zero under 10\% noise.
231	The complementarity is clear: conditions where free-$\theta$ detection is fragile (high-baseline-accuracy models with $\theta$-shift absorption) are precisely where $\theta$-fixed anchoring provides the strongest and most noise-robust signal.
232	
233	\begin{table}[t]
234	\centering
235	\caption{Sensitivity of detection to item parameter noise (100 trials, Qwen MMLU, free-$\theta$). \% bias relative to noise-free $d$.}
236	\label{tab:param_noise_free}
237	\footnotesize
238	\begin{tabular}{@{}lcccc@{}}
239	\toprule
240	Noise $\sigma$ & $d$ (15\%) & \% bias & $d$ (50\%) & \% bias \\
241	\midrule
242	0\% & $-$6.575 & --- & $-$1.897 & --- \\
243	5\% & $-$6.010 & 8.6 & $-$0.925 & 51.2 \\
244	10\% & $-$5.433 & 17.4 & $-$0.014 & 99.3 \\
245	\bottomrule
246	\end{tabular}
247	\end{table}
248	
249	\begin{table}[t]
250	\centering
251	\caption{Sensitivity of detection to item parameter noise (100 trials, Qwen MMLU, $\theta$-fixed). Worst-case $|d|$ over 100 trials in parentheses.}
252	\label{tab:param_noise_fixed}
253	\footnotesize
254	\resizebox{\columnwidth}{!}{%
255	\begin{tabular}{@{}lcccc@{}}
256	\toprule
257	Noise $\sigma$ & $d_{\text{fixed}}$ (15\%) & \% bias & $d_{\text{fixed}}$ (50\%) & \% bias \\
258	\midrule
259	0\% & 4.77 & --- & 14.52 & --- \\
260	5\% & 5.07 $\pm$ 0.24 & 6.3 & 14.76 $\pm$ 0.44 & 1.6 \\
261	10\% & 4.95 $\pm$ 0.43 (3.73) & 3.7 & 14.45 $\pm$ 0.85 (12.20) & 0.5 \\
262	\bottomrule
263	\end{tabular}}
264	\end{table}
265	
266	\section{BCa Bootstrap Sensitivity Check}
267	\label{app:bca}
268	
269	As a sensitivity check, we computed bias-corrected and accelerated (BCa) bootstrap confidence intervals for all Cohen's $d$ estimates.
270	BCa CIs were uniformly narrower than the percentile CIs reported in the main text (mean reduction 22\%), confirming that our reported intervals are conservative.
271	The single condition where BCa widens the zero-crossing set---Llama fixed-$\theta$ at 50\% contamination, BCa CI [$-$0.13, 2.21] vs.\ percentile CI [0.17, 2.97]---is already characterized as ineffective in \S\ref{sec:theta_dynamics}.
272	
273	\section{Classical IRT Refit from Leaderboard Data}
274	\label{app:mml_em}
275	
276	To assess whether item parameters can be recovered without PSN-IRT's neural calibration, we applied classical MML-EM estimation (Gauss--Hermite quadrature, $Q{=}31$ nodes) to binary response data from $N{=}178$ models on the Open LLM Leaderboard v1.
277	With 14,042 MMLU items and an examinee-to-item ratio of $N{:}J = 0.013$---far below the $N{>}500$ typically required for stable 3PL estimation---discrimination parameters are severely under-determined.
278	
279	Table~\ref{tab:mml_em} reports parameter correlations between MML-EM-fitted and PSN-IRT parameters.
280	Difficulty shows moderate agreement ($r_b{=}0.663$), but discrimination is essentially unrecovered ($r_a{=}0.127$).
281	Using these MML-EM parameters produces miscalibrated $\ell_z^*$ statistics (mean$\,{=}\,$11.2, expected ${\approx}\,$0), confirming that the refitted model does not capture the data-generating process.
282	This motivates the dependence on PSN-IRT's externally calibrated item bank (\S\ref{sec:framework}).
283	
284	\begin{table}[t]
285	\centering
286	\caption{Parameter correlation between classical MML-EM refit ($N{=}178$ models) and PSN-IRT on MMLU ($n{=}10{,}558$ matched items).}
287	\label{tab:mml_em}
288	\footnotesize
289	\begin{tabular}{@{}llcc@{}}
290	\toprule
291	Model & Parameter & Pearson $r$ & Spearman $\rho$ \\
292	\midrule
293	3PL & $a$ (discrim.) & 0.127 & 0.135 \\
294	3PL & $b$ (difficulty) & 0.663 & 0.684 \\
295	2PL & $a$ (discrim.) & $-$0.029 & 0.050 \\
296	2PL & $b$ (difficulty) & 0.608 & 0.656 \\
297	\bottomrule
298	\end{tabular}
299	\end{table}
300	
301	\section{Post-RL Preliminary Observation}
302	\label{app:post_rl}
303	
304	\citet{wang2025fragility} show that all MIA-based detectors fail after RL post-training.
305	In a single-model pilot ($N{=}1$, Qwen, GRPO), we applied GRPO \citep{shao2024} for 1,500 steps to a contaminated model (15\% MMLU) and evaluated at three checkpoints.
306	GRPO erases the accuracy gap between seen and unseen items ($11.4\text{pp} \to 2.1\text{pp}$), but the $\ell_z^*$ response-pattern gap persists (${\sim}3.3$; Figure~\ref{fig:grpo}), suggesting structural traces of contamination may survive RL alignment.
307	Min-K\% membership inference confirms this dissociation: while SFT yields a weak MIA signal (AUC-ROC${=}0.611$), GRPO training drives AUC to $0.493$ (step~500), $0.493$ (step~1000), and $0.493$ (step~1500)---indistinguishable from random chance ($0.50$) as RL erases memorization-based features while the response-pattern anomaly that $\ell_z^*$ detects persists.
308	This $N{=}1$ observation requires validation across model families, RL methods, and contamination levels before any conclusions can be drawn.
309	
310	\paragraph{GRPO hyperparameters.}
311	Table~\ref{tab:grpo_hyperparams} reports the GRPO training hyperparameters for the post-RL extension (\S\ref{sec:setup}).
312	
313	\begin{table}[t]
314	\centering
315	\caption{GRPO training hyperparameters (Qwen2.5-7B-Instruct, 15\% MMLU contamination).}
316	\label{tab:grpo_hyperparams}
317	\footnotesize
318	\resizebox{\columnwidth}{!}{%
319	\begin{tabular}{@{}ll@{}}
320	\toprule
321	Hyperparameter & Value \\
322	\midrule
323	Learning rate & $5 \times 10^{-6}$ \\
324	Per-device batch size & 2 \\
325	Gradient accumulation steps & 4 \\
326	Num.\ generations per prompt & 16 \\
327	Max completion length & 128 \\
328	Sampling temperature & 1.2 \\
329	Training steps & 1,500 (checkpoints at 500, 1000, 1500) \\
330	Reward function & Correctness-based ($+1.0$ correct, $-1.0$ incorrect) \\
331	LoRA rank / $\alpha$ / dropout & 16 / 32 / 0.05 \\
332	Precision & BF16 \\
333	Seed & 42 \\
334	\bottomrule
335	\end{tabular}}
336	\end{table}
337	
338	\section{QLoRA Training Hyperparameters}
339	\label{app:hyperparams}
340	
341	Table~\ref{tab:hyperparams} reports the QLoRA fine-tuning hyperparameters used across all experiments.
342	All training was conducted on NVIDIA RTX PRO 6000 GPUs (48\,GB VRAM).
343	Each QLoRA SFT run takes approximately 15--25 minutes depending on contamination level and dataset size; the full experimental campaign (including all seeds, contamination levels, and model families) consumed approximately 120 GPU-hours.
344	
345	\begin{table}[t]
346	\centering
347	\caption{QLoRA fine-tuning hyperparameters (shared across all model families and contamination conditions).}
348	\label{tab:hyperparams}
349	\footnotesize
350	\resizebox{\columnwidth}{!}{%
351	\begin{tabular}{@{}ll@{}}
352	\toprule
353	Hyperparameter & Value \\
354	\midrule
355	Quantization & 4-bit NF4 \\
356	LoRA rank & 16 \\
357	LoRA $\alpha$ & 32 \\
358	LoRA dropout & 0.05 \\
359	Target modules & \texttt{q\_proj}, \texttt{k\_proj}, \texttt{v\_proj}, \texttt{o\_proj} \\
360	Learning rate & $2 \times 10^{-4}$ \\
361	Optimizer & AdamW \\
362	Warmup ratio & 0.1 \\
363	Epochs & 3 \\
364	Per-device batch size & 4 \\
365	Gradient accumulation steps & 4 \\
366	Effective batch size & 16 \\
367	Max sequence length & 512 \\
368	Data mixing & Contaminated items shuffled into training set \\
369	\bottomrule
370	\end{tabular}}
371	\end{table}
372	
373	\section{Contamination Run Reproducibility}\label{app:reproducibility}
374	
375	Tables~\ref{tab:qwen_multiseed}--\ref{tab:mistral_multiseed} report per-seed Cohen's $d$ for all model families across contamination levels, computed against the shared $n{=}10$ clean baseline.
376	These tables underpin the multi-seed means and SDs reported in Tables~\ref{tab:cohens_d} and \ref{tab:degradation}.
377	
378	\begin{table}[ht!]
379	\centering
380	\caption{Reproducibility of contamination effect sizes across independent QLoRA runs (Qwen2.5-7B-Instruct, MMLU). Each row shows Cohen's $|d|$ from an independent training seed against the shared $n{=}10$ clean baseline ($\bar{\ell}_z^* = 8.68$, $s = 0.74$). All runs use identical hyperparameters; only the random seed differs.}
381	\label{tab:qwen_multiseed}
382	\footnotesize
383	\begin{tabular}{@{}lcccccc@{}}
384	\toprule
385	& \multicolumn{3}{c}{Free-$\theta$ $|d|$} & \multicolumn{3}{c}{Fixed-$\theta$ $|d|$} \\
386	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
387	Seed & 15\% & 25\% & 50\% & 15\% & 25\% & 50\% \\
388	\midrule
389	42 (original) & 6.57 & 8.22 & 1.90 & 4.77 & 4.96 & 14.52 \\
390	123 & 5.09 & 8.78 & 5.42 & 7.79 & 5.37 & 12.64 \\
391	456 & 4.41 & 5.31 & 7.91 & 7.99 & 7.34 & 9.80 \\
392	\addlinespace
393	Mean & 5.36 & 7.44 & 5.08 & 6.85 & 5.89 & 12.32 \\
394	SD & 1.10 & 1.86 & 3.02 & 1.80 & 1.27 & 2.38 \\
395	CV (\%) & 20.3 & 25.2 & 59.6 & 26.3 & 21.7 & 19.3 \\
396	\bottomrule
397	\end{tabular}
398	\vspace{0.5em}
399	
400	\noindent\textit{Note.} Fixed-$\theta$ estimation anchors $\hat{\theta}$ at the clean-baseline mean ($\theta{=}{-}0.102$), removing $\theta$-shift absorption. The 50\% free-$\theta$ column exhibits high CV (59.6\%), reflecting seed-dependent $\theta$-shift magnitude; fixed-$\theta$ reduces this to 19.3\%, confirming that cross-seed variability at high contamination is driven by ability-estimate instability rather than true signal variance.
401	\end{table}
402	
403	\begin{table}[ht!]
404	\centering
405	\caption{Multi-seed Cohen's $|d|$ for HT and accuracy $z$-score statistics (Qwen2.5-7B-Instruct, MMLU), computed using the chi-squared ratio HT statistic and bootstrap Cohen's $d$ (10{,}000 resamples). These supplement the $\ell_z^*$ values in Table~\ref{tab:degradation}.}
406	\label{tab:ht_acc_multiseed}
407	\footnotesize
408	\begin{tabular}{@{}lcccccc@{}}
409	\toprule
410	& \multicolumn{3}{c}{HT $|d|$} & \multicolumn{3}{c}{Acc.\ $z$ $|d|$} \\
411	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
412	Seed & 15\% & 25\% & 50\% & 15\% & 25\% & 50\% \\
413	\midrule
414	42 (original) & 7.26 & 8.90 & 1.66 & 42.3 & 49.8 & 68.7 \\
415	123 & 5.52 & 9.51 & 5.80 & 47.3 & 53.4 & 70.8 \\
416	456 & 4.72 & 5.10 & 8.41 & 45.4 & 51.3 & 70.4 \\
417	\addlinespace
418	Mean & 5.83 & 7.84 & 5.29 & 45.0 & 51.5 & 70.0 \\
419	SD & 1.30 & 2.39 & 3.41 & 2.5 & 1.8 & 1.1 \\
420	\bottomrule
421	\end{tabular}
422	\vspace{0.5em}
423	
424	\noindent\textit{Note.} HT exhibits high cross-seed variance at 50\% (SD${=}3.41$), mirroring the $\ell_z^*$ pattern: the non-monotonicity observed in seed 42 ($|d|{=}1.66$) does not generalize across seeds. Accuracy $z$-scores are highly stable (CV $< 6\%$) and monotonically increasing with contamination level.
425	\end{table}
426	
427	\begin{table}[ht!]
428	\centering
429	\caption{Multi-seed Cohen's $d$ for Llama-3.1-8B across all contamination levels (MMLU). Each cell shows Cohen's $d$ from an independent training seed against the shared $n{=}10$ clean baseline ($\bar{\ell}_z^* = {+}0.26$, $s = 1.54$). The 5\% condition exhibits higher cross-seed variance (SD${=}0.99$), reflecting the weaker signal from ${\sim}700$ contaminated items (5\%$\times$14{,}042).}
430	\label{tab:llama_multiseed}
431	\footnotesize
432	\begin{tabular}{@{}lcccccc@{}}
433	\toprule
434	& \multicolumn{3}{c}{Per-seed $d$} & & \\
435	\cmidrule(lr){2-4}
436	Contam.\ level & $s_1$ & $s_2$ & $s_3$ & Mean & SD \\
437	\midrule
438	5\%  & $-$3.22 & $-$3.06 & $-$1.44 & $-$2.57 & 0.99 \\
439	15\% & $-$2.11 & $-$3.21 & $-$3.09 & $-$2.80 & 0.60 \\
440	25\% & $-$3.16 & $-$2.28 & $-$2.24 & $-$2.56 & 0.52 \\
441	50\% & $-$2.33 & $-$2.59 & $-$1.99 & $-$2.30 & 0.30 \\
442	\bottomrule
443	\end{tabular}
444	\vspace{0.5em}
445	
446	\noindent\textit{Note.} Unlike Qwen, Llama exhibits no non-monotonic dose-response: mean $|d|$ is approximately flat across contamination levels ($2.30$--$2.80$), consistent with its near-zero baseline $\ell_z^*$ ($+0.26$) and negligible $\theta$-shift absorption (\S\ref{sec:theta_dynamics}). Cross-seed variance decreases with contamination level (CV: 39\% at 5\% $\to$ 13\% at 50\%), suggesting that higher contamination produces a more stable signal despite the flat mean trajectory.
447	\end{table}
448	
449	\begin{table}[ht!]
450	\centering
451	\caption{Multi-seed Cohen's $d$ for Mistral-7B-v0.3 across contamination levels (MMLU). Each cell shows Cohen's $d$ from an independent training seed against the shared $n{=}10$ clean baseline ($\bar{\ell}_z^* = {+}4.02$, $s = 2.05$). The 5\% condition has only $n{=}2$ seeds; its high SD reflects this limited sample.}
452	\label{tab:mistral_multiseed}
453	\footnotesize
454	\begin{tabular}{@{}lcccccc@{}}
455	\toprule
456	& \multicolumn{3}{c}{Per-seed $d$} & & \\
457	\cmidrule(lr){2-4}
458	Contam.\ level & $s_1$ & $s_2$ & $s_3$ & Mean & SD \\
459	\midrule
460	5\%  & $-$2.82 & $-$4.83 & --- & $-$3.83 & 1.42 \\
461	15\% & $-$2.64 & $-$3.98 & $-$3.48 & $-$3.37 & 0.68 \\
462	50\% & $-$3.50 & $-$4.25 & $-$4.51 & $-$4.09 & 0.53 \\
463	\bottomrule
464	\end{tabular}
465	\end{table}
466	
467	\section{Use of AI Assistants}
468	\label{app:ai-assistants}
469	
470	The authors used AI-based writing assistants, including Claude, for limited support during manuscript preparation, including grammar polishing, wording suggestions, LaTeX editing, and code/debugging assistance. The tools were not used to generate the core research ideas, experimental design, methodological decisions, data analysis, or scientific conclusions. All AI-assisted text, code suggestions, and references were manually reviewed and edited by the authors.
471	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ca4a0a05-9176-46b0-9660-42b97743eb11",
  "isSidechain": true,
  "promptId": "da07976a-f226-4e2d-8dce-e30611d2ccf3",
  "agentId": "a4f6b5b2e69085d89",
  "type": "user",
  "uuid": "fa7880d2-39c1-4fb9-b520-d2867294859b",
  "sourceToolAssistantUUID": "ca4a0a05-9176-46b0-9660-42b97743eb11",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-25T19:42:36.659Z_

Now I'll compile a comprehensive catalog of every numerical value extracted from all the .tex files:

## COMPREHENSIVE NUMERICAL CATALOG

### abstract.tex

abstract.tex:4 | n = 10 | "three 7--8B model families ($n{=}10$ clean seeds per family)"
abstract.tex:4 | 14,042 | "MMLU (14,042 items)"
abstract.tex:4 | 295 | "ARC-Challenge (295 items)"
abstract.tex:5 | 2.4x | "amplifies detection by 2.4$\times$"
abstract.tex:5 | 60% | "coefficient of variation from 60%"
abstract.tex:5 | 19% | "to 19%"

---

### introduction.tex

introduction.tex:6 | 5% | "diamonds: 5%"
introduction.tex:6 | 15% | "triangles: 15%"
introduction.tex:6 | 25% | "squares: 25%"
introduction.tex:6 | 50% | "circles: 50%"
introduction.tex:25 | n = 10 | "($n{=}10$ clean seeds each)"
introduction.tex:25 | 7-8B | "three 7--8B model families"
introduction.tex:25 | 4PL | "four-parameter logistic"
introduction.tex:27 | 2.4x | "$\theta$-anchoring amplifies Qwen's multi-seed $|d|$ by 2.4$\times$"
introduction.tex:27 | 50% | "at 50% contamination"
introduction.tex:27 | 60% | "reducing inter-seed CV from 60%"
introduction.tex:27 | 19% | "to 19%"
introduction.tex:30 | 57/60 | "57/60 flagged cells on real-world data"
introduction.tex:30 | 4/60 | "4/60 flagged cells"
introduction.tex:32 | 4.15 | "$|d|: $4.15 \to 5.36 \to 7.44 \to 5.08$"
introduction.tex:32 | 5.36 | "dose-response values (part of sequence)"
introduction.tex:32 | 7.44 | "dose-response values (part of sequence)"
introduction.tex:32 | 5.08 | "dose-response values (part of sequence)"
introduction.tex:32 | 5% | "at 5%"
introduction.tex:32 | 15% | "at 15%"
introduction.tex:32 | 25% | "at 25%"
introduction.tex:32 | 50% | "at 50%"
introduction.tex:32 | 12.32 | "$\theta$-anchoring reveals stable positive dose-response ($|d|{=}12.32$ at 50%)"
introduction.tex:37 | 95% | "single-seed bootstrap 95% CIs"
introduction.tex:37 | n = 10 | "$n{=}10$"

---

### method.tex

method.tex:14 | 46% | "46% of MMLU items have $d_i < 0.95$"
method.tex:14 | 0.95 | "items have $d_i < 0.95$"
method.tex:14 | 55.7pp | "$+$55.7pp gain with 4PL"
method.tex:15 | 39 | "spanning 39 models"
method.tex:15 | r_a = 0.127 | "discrimination recovery degrades to $r_a{=}0.127$"
method.tex:27 | 12.32 | "yields an overall positive dose-response ($|d|{=}12.32$ at 50%)"
method.tex:27 | 50% | "at 50%"
method.tex:35 | 57 | "57 of 60 model-benchmark cells"
method.tex:35 | 60 | "57 of 60 model-benchmark cells"
method.tex:35 | 1.96 | "$|\ell_z^*| > 1.96$"
method.tex:43 | n = 10 | "$n{=}10$ clean seeds"
method.tex:45 | 0.914 | "$J \approx 0.914$ for $n{=}10$"
method.tex:46 | 10,000 | "10,000 resamples"
method.tex:50 | 0.93 | "$d_{\text{ratio}} \geq 0.93$"
method.tex:50 | 0.5 | "at realistic levels ($d_{\text{ratio}} \geq 0.93$ for $\sigma_\tau \leq 0.5$)"
method.tex:50 | 98.5% | "maintains ${\geq}98.5\%$ power"
method.tex:56 | 7-8B | "three 7--8B model families"
method.tex:57 | rank = 16 | "QLoRA; rank\,$=$\,16"
method.tex:57 | alpha = 32 | "$\alpha$\,$=$\,32"
method.tex:58 | 15% | "tested at 15%"
method.tex:58 | 50% | "tested at 50%"
method.tex:59 | 5% | "added 5%"
method.tex:59 | 25% | "added 25%"
method.tex:60 | 5% | "at 5%"
method.tex:60 | 25% | "at 25%"
method.tex:61 | n = 10 | "$n{=}10$ independent clean seeds"
method.tex:62 | n = 3 | "with $n{=}3$ independent QLoRA seeds"
method.tex:62 | 15%/25%/50% | "Qwen at 15%/25%/50%"
method.tex:62 | 5%/15%/25%/50% | "Llama at 5%/15%/25%/50%"
method.tex:62 | 5%/15%/50% | "Mistral at 5%/15%/50%"
method.tex:65 | 14,042 | "MMLU (14,042 items)"
method.tex:65 | 295 | "ARC-Challenge (295 PSN-IRT-calibrated items)"
method.tex:70 | 1,500 | "1,500 steps"
method.tex:71 | N = 1 | "This extension is $N{=}1$"

---

### results.tex

results.tex:6 | n = 10 | "($n{=}10$ clean seeds)"
results.tex:6 | 10,000 | "10,000 resamples"
results.tex:6 | n = 3 | "($n{=}3$ independent runs)"
results.tex:14 | -4.15 | "Qwen MMLU 5%: $-4.15$"
results.tex:14 | [-9.9, -2.7] | "CI [$-9.9$, $-2.7$]"
results.tex:14 | -5.36 | "Qwen MMLU 15%: $-5.36$"
results.tex:14 | ±1.10 | "($\pm$1.10)"
results.tex:14 | -7.44 | "Qwen MMLU 25%: $-7.44$"
results.tex:14 | ±1.86 | "($\pm$1.86)"
results.tex:14 | -5.08 | "Qwen MMLU 50%: $-5.08$"
results.tex:14 | ±3.02 | "($\pm$3.02)"
results.tex:15 | -2.57 | "Llama MMLU 5%: $-2.57$"
results.tex:15 | ±0.99 | "($\pm$0.99)"
results.tex:15 | -2.80 | "Llama MMLU 15%: $-2.80$"
results.tex:15 | ±0.60 | "($\pm$0.60)"
results.tex:15 | -2.56 | "Llama MMLU 25%: $-2.56$"
results.tex:15 | ±0.52 | "($\pm$0.52)"
results.tex:15 | -2.30 | "Llama MMLU 50%: $-2.30$"
results.tex:15 | ±0.30 | "($\pm$0.30)"
results.tex:16 | -3.83 | "Mistral MMLU 5%: $-3.83$"
results.tex:16 | ±1.42 | "($\pm$1.42)"
results.tex:16 | -3.37 | "Mistral MMLU 15%: $-3.37$"
results.tex:16 | ±0.68 | "($\pm$0.68)"
results.tex:16 | -4.09 | "Mistral MMLU 50%: $-4.09$"
results.tex:16 | ±0.53 | "($\pm$0.53)"
results.tex:17 | +3.16 | "Qwen ARC-C 15%: $+3.16$"
results.tex:17 | [2.0, 9.5] | "CI [$2.0$, $9.5$]"
results.tex:17 | +5.30 | "Qwen ARC-C 50%: $+5.30$"
results.tex:17 | [3.6, 15.2] | "CI [$3.6$, $15.2$]"
results.tex:30 | 2.30 | "Llama at 50%: $|d|{=}2.30$"
results.tex:30 | 7.44 | "Qwen at 25%: $|d|{=}7.44$"
results.tex:30 | 4.15 | "Qwen at 5%: $|d|{=}4.15$"
results.tex:30 | 2.57/2.80/2.56/2.30 | "Llama values"
results.tex:30 | 3.83/3.37/4.09 | "Mistral values"
results.tex:31 | 3.16 | "Qwen ARC-C 15%: $|d|{=}3.16$"
results.tex:31 | 5.30 | "Qwen ARC-C 50%: $|d|{=}5.30$"
results.tex:31 | 295 | "295 items"
results.tex:32 | 89.7% | "89.7% baseline accuracy"
results.tex:34 | +8.68 | "Qwen ${+}8.68$"
results.tex:34 | +0.26 | "Llama ${+}0.26$"
results.tex:34 | +4.02 | "Mistral ${+}4.02$"
results.tex:48 | ≈0.5 | "$\Delta\theta{\approx}0.5$"
results.tex:51 | 2.4x | "amplifies Qwen's multi-seed $|d|$ by 2.4$\times$ at 50%"
results.tex:51 | 5.08 | "$5.08 \to 12.32$"
results.tex:51 | 12.32 | "amplifies to $12.32$"
results.tex:52 | 60% | "inter-seed CV from 60%"
results.tex:52 | 19% | "to 19%"
results.tex:55 | 89.7% | "89.7% baseline accuracy"
results.tex:56 | 295 | "295 items"
results.tex:61 | -14.2 | "Qwen's seen-item $\ell_z^*$ shifts by $\Delta{=}{-}14.2$"
results.tex:61 | -1.8 | "unseen items shift by only $\Delta{=}{-}1.8$"
results.tex:66 | +8.68 | "Qwen ($\ell_z^*{=}{+}8.68$)"
results.tex:66 | 2.4x | "shows $2.4{\times}$"
results.tex:66 | +4.02 | "Mistral ($+4.02$)"
results.tex:66 | 1.7x | "shows $1.7{\times}$"
results.tex:66 | +0.26 | "Llama ($+0.26$)"
results.tex:66 | 0.4x | "shows $0.4{\times}$"
results.tex:66 | 0.52 | "comparable $\theta$-shift ($\Delta\theta{=}0.52$)"
results.tex:80 | 4.15 | "Qwen 5%: 4.15"
results.tex:80 | 3.52 | "Qwen 5% fixed: 3.52"
results.tex:80 | 0.8x | "Ratio: 0.8$\times$"
results.tex:80 | [2.9, 5.7] | "CI [2.9, 5.7]"
results.tex:83 | 5.36 | "Qwen 15%: 5.36"
results.tex:83 | 6.85 | "Qwen 15% fixed: 6.85"
results.tex:83 | 1.3x | "Ratio: 1.3$\times$"
results.tex:83 | ±1.80 | "($\pm$1.80)"
results.tex:84 | 2.11 | "Llama 15%: 2.11"
results.tex:84 | 0.58 | "Llama 15% fixed: 0.58"
results.tex:84 | 0.3x | "Ratio: 0.3$\times$"
results.tex:84 | [0, 2.37] | "CI [0, 2.37]"
results.tex:85 | 2.64 | "Mistral 15%: 2.64"
results.tex:85 | 2.69 | "Mistral 15% fixed: 2.69"
results.tex:85 | 1.0x | "Ratio: 1.0$\times$"
results.tex:85 | [1.53, 9.06] | "CI [1.53, 9.06]"
results.tex:88 | 5.08 | "Qwen 50%: 5.08"
results.tex:88 | 12.32 | "Qwen 50% fixed: 12.32"
results.tex:88 | 2.4x | "Ratio: 2.4$\times$"
results.tex:88 | ±2.38 | "($\pm$2.38)"
results.tex:89 | 2.33 | "Llama 50%: 2.33"
results.tex:89 | 0.84 | "Llama 50% fixed: 0.84"
results.tex:89 | 0.4x | "Ratio: 0.4$\times$"
results.tex:89 | [0.17, 2.97] | "CI [0.17, 2.97]"
results.tex:90 | 3.50 | "Mistral 50%: 3.50"
results.tex:90 | 5.80 | "Mistral 50% fixed: 5.80"
results.tex:90 | 1.7x | "Ratio: 1.7$\times$"
results.tex:90 | [3.87, 18.45] | "CI [3.87, 18.45]"
results.tex:103 | 0.0003 | "SD{\approx}0.0003 for Qwen clean seeds"
results.tex:108 | 0.53 | "AUROC{\approx}0.53"
results.tex:109 | 57/60 | "57/60 leaderboard cells"
results.tex:109 | 4/60 | "4/60 for accuracy $z$-scores"
results.tex:110 | 55.7pp | "4PL gains $+$55.7pp power"
results.tex:110 | 96.9% | "$96.9\%$ vs.\ $41.2\%$"
results.tex:110 | 41.2% | "vs. 41.2%"
results.tex:110 | 34.3pp | "HellaSwag $+$34.3pp"
results.tex:110 | 20.7pp | "GSM8K $+$20.7pp"
results.tex:121 | 5.36 | "Qwen $\ell_z^*$ at 15%: 5.36"
results.tex:121 | ±1.10 | "($\pm$1.10)"
results.tex:121 | 5.08 | "Qwen $\ell_z^*$ at 50%: 5.08"
results.tex:121 | ±3.02 | "($\pm$3.02)"
results.tex:122 | 5.83 | "Qwen HT at 15%: 5.83"
results.tex:122 | ±1.30 | "($\pm$1.30)"
results.tex:122 | 5.29 | "Qwen HT at 50%: 5.29"
results.tex:122 | ±3.41 | "($\pm$3.41)"
results.tex:123 | 45.0 | "Qwen Acc. $z$ at 15%: 45.0"
results.tex:123 | ±2.5 | "($\pm$2.5)"
results.tex:123 | 70.0 | "Qwen Acc. $z$ at 50%: 70.0"
results.tex:123 | ±1.1 | "($\pm$1.1)"
results.tex:125 | 2.11 | "Llama $\ell_z^*$ at 15%: 2.11"
results.tex:125 | [1.4, 4.8] | "CI [$1.4$, $4.8$]"
results.tex:125 | 2.33 | "Llama $\ell_z^*$ at 50%: 2.33"
results.tex:125 | [1.6, 5.1] | "CI [$1.6$, $5.1$]"
results.tex:126 | 2.45 | "Llama HT at 15%: 2.45"
results.tex:126 | [1.5, 4.3] | "CI [$1.5$, $4.3$]"
results.tex:126 | 3.07 | "Llama HT at 50%: 3.07"
results.tex:126 | [1.9, 5.3] | "CI [$1.9$, $5.3$]"
results.tex:127 | 22.5 | "Llama Acc. $z$ at 15%: 22.5"
results.tex:127 | [13.6, 47.0] | "CI [$13.6$, $47.0$]"
results.tex:127 | 32.8 | "Llama Acc. $z$ at 50%: 32.8"
results.tex:127 | [19.8, 68.6] | "CI [$19.8$, $68.6$]"
results.tex:129 | 2.64 | "Mistral $\ell_z^*$ at 15%: 2.64"
results.tex:129 | 3.50 | "Mistral $\ell_z^*$ at 50%: 3.50"
results.tex:129 | [2.1, 9.4] | "CI [$2.1$, $9.4$]"
results.tex:130 | 4.36 | "Mistral HT at 15%: 4.36"
results.tex:130 | [1.2, 7.0] | "CI [$1.2$, $7.0$]"
results.tex:130 | 5.89 | "Mistral HT at 50%: 5.89"
results.tex:130 | [1.9, 9.4] | "CI [$1.9$, $9.4$]"
results.tex:131 | 7.81 | "Mistral Acc. $z$ at 15%: 7.81"
results.tex:131 | [4.4, 14.4] | "CI [$4.4$, $14.4$]"
results.tex:131 | 16.6 | "Mistral Acc. $z$ at 50%: 16.6"
results.tex:131 | [9.7, 34.6] | "CI [$9.7$, $34.6$]"
results.tex:148 | 4.15 | "$|d|$: $4.15 \to 5.36 \to 7.44 \to 5.08$"
results.tex:148 | 5.36 | "(part of dose-response sequence)"
results.tex:148 | 7.44 | "(part of dose-response sequence)"
results.tex:148 | 5.08 | "(part of dose-response sequence)"
results.tex:148 | 60% | "CV${=}$60%"
results.tex:148 | [1.90, 7.91] | "range $[1.90, 7.91]$"
results.tex:149 | 12.32 | "fixed-$\theta$ eliminates the inverted-U ($|d|{=}12.32$ at 50%)"
results.tex:149 | 19% | "CV reduced to 19%"
results.tex:150 | 2.3-2.8 | "Llama's flat trajectory ($|d|{\approx}2.3$--$2.8$)"
results.tex:151 | 93% | "achieves ${>}$93% power"

---

### discussion.tex

discussion.tex:6 | 55.7pp | "4PL modeling captures ceiling effects that 3PL misses ($+$55.7pp power on MMLU)"
discussion.tex:11 | 60% | "free-$\theta$ CV up to 60%"
discussion.tex:11 | 19% | "vs.\ 19% under $\theta$-fixed"
discussion.tex:12 | 57/60 | "57/60 cells flagged"
discussion.tex:15 | 4% | "$<$4% bias"
discussion.tex:15 | 10% | "$\pm$10% parameter perturbation"
discussion.tex:17 | 0.493 | "AUC drops to chance ($0.493$)"
discussion.tex:17 | 500 | "after 500 RL steps"
discussion.tex:17 | 3.3 | "$\ell_z^*$ response-pattern gap persists at ${\sim}3.3$"

---

### conclusion.tex

conclusion.tex:3 | 7-8B | "three 7--8B model families"
conclusion.tex:3 | 5%-50% | "four contamination levels (5%--50%)"

---

### appendix.tex

appendix.tex:4 | 0.041 | "mean bias 0.041"
appendix.tex:4 | 1.003 | "standard deviation 1.003"
appendix.tex:5 | 8.3% | "8.3% for MMLU"
appendix.tex:5 | 10,000 | "n > 10{,}000 items"
appendix.tex:5 | 50.0% | "50.0% for GSM8K"
appendix.tex:5 | 1,319 | "($n = 1{,}319$)"
appendix.tex:5 | 58.3% | "58.3% for ARC-C"
appendix.tex:5 | 295 | "($n = 295$)"
appendix.tex:5 | 75.0% | "75.0% for HumanEval"
appendix.tex:5 | 164 | "($n = 164$)"
appendix.tex:8 | 97.8% | "MMLU achieves 97.8% power"
appendix.tex:8 | 93% | "sustains ${>}$93% at all levels"
appendix.tex:10 | 0.957 | "R^2 = 0.957"
appendix.tex:10 | 30 | "$K=30$"
appendix.tex:10 | 7,958 | "approximate minimum benchmark size of $n \geq 7{,}958$ items"
appendix.tex:10 | 80% | "80% power"
appendix.tex:15 | 2,000 | "2{,}000 simulation replicates"
appendix.tex:15 | 0.05 | "$\alpha{=}0.05$"
appendix.tex:19 | 0.952 | "MMLU: $.952"
appendix.tex:19 | 0.938 | "\to .938$"
appendix.tex:19 | 0.846 | "GSM8K: $.846"
appendix.tex:19 | 0.802 | "\to .802$"
appendix.tex:22 | 10% | "estimation error exceeding ${\sim}10\%$"
appendix.tex:23 | 12+ | "($12{+}$ models per item)"
appendix.tex:34 | 0.476 | "MMLU 4PL 5%: .476"
appendix.tex:34 | 0.848 | ".848 at 10%"
appendix.tex:34 | 0.969 | ".969 at 15%"
appendix.tex:34 | 0.983 | ".983 at 25%"
appendix.tex:34 | 0.952 | ".952 at 50%"
appendix.tex:34 | 0.938 | ".938 at 75%"
appendix.tex:35 | 1.00 | "1.00 at 100%"
appendix.tex:35 | 0.227 | "MMLU 3PL 5%: .227"
appendix.tex:35 | 0.340 | ".340 at 10%"
appendix.tex:35 | 0.412 | ".412 at 15%"
appendix.tex:35 | 0.521 | ".521 at 25%"
appendix.tex:35 | 0.676 | ".676 at 50%"
appendix.tex:35 | 0.770 | ".770 at 75%"
appendix.tex:37 | 0.251 | "HellaSwag 4PL 5%: .251"
appendix.tex:37 | 0.454 | ".454 at 10%"
appendix.tex:37 | 0.656 | ".656 at 15%"
appendix.tex:37 | 0.915 | ".915 at 25%"
appendix.tex:37 | 0.939 | ".939 at 50%"
appendix.tex:37 | 0.919 | ".919 at 75%"
appendix.tex:38 | 0.167 | "HellaSwag 3PL 5%: .167"
appendix.tex:38 | 0.241 | ".241 at 10%"
appendix.tex:38 | 0.313 | ".313 at 15%"
appendix.tex:38 | 0.368 | ".368 at 25%"
appendix.tex:38 | 0.508 | ".508 at 50%"
appendix.tex:38 | 0.642 | ".642 at 75%"
appendix.tex:40 | 0.156 | "GSM8K 4PL 5%: .156"
appendix.tex:40 | 0.309 | ".309 at 10%"
appendix.tex:40 | 0.492 | ".492 at 15%"
appendix.tex:40 | 0.737 | ".737 at 25%"
appendix.tex:40 | 0.846 | ".846 at 50%"
appendix.tex:40 | 0.802 | ".802 at 75%"
appendix.tex:41 | 0.102 | "GSM8K 3PL 5%: .102"
appendix.tex:41 | 0.172 | ".172 at 10%"
appendix.tex:41 | 0.285 | ".285 at 15%"
appendix.tex:41 | 0.396 | ".396 at 25%"
appendix.tex:41 | 0.567 | ".567 at 50%"
appendix.tex:41 | 0.577 | ".577 at 75%"
appendix.tex:43 | 0.057 | "ARC-C 4PL 5%: .057"
appendix.tex:43 | 0.075 | ".075 at 10%"
appendix.tex:43 | 0.087 | ".087 at 15%"
appendix.tex:43 | 0.130 | ".130 at 25%"
appendix.tex:43 | 0.285 | ".285 at 50%"
appendix.tex:43 | 0.493 | ".493 at 75%"
appendix.tex:44 | 0.054 | "ARC-C 3PL 5%: .054"
appendix.tex:44 | 0.062 | ".062 at 10%"
appendix.tex:44 | 0.071 | ".071 at 15%"
appendix.tex:44 | 0.076 | ".076 at 25%"
appendix.tex:44 | 0.110 | ".110 at 50%"
appendix.tex:44 | 0.102 | ".102 at 75%"
appendix.tex:46 | 0.076 | "HumanEval 4PL 5%: .076"
appendix.tex:46 | 0.121 | ".121 at 10%"
appendix.tex:46 | 0.197 | ".197 at 15%"
appendix.tex:46 | 0.302 | ".302 at 25%"
appendix.tex:46 | 0.554 | ".554 at 50%"
appendix.tex:46 | 0.521 | ".521 at 75%"
appendix.tex:47 | 0.063 | "HumanEval 3PL 5%: .063"
appendix.tex:47 | 0.086 | ".086 at 10%"
appendix.tex:47 | 0.120 | ".120 at 15%"
appendix.tex:47 | 0.182 | ".182 at 25%"
appendix.tex:47 | 0.281 | ".281 at 50%"
appendix.tex:47 | 0.315 | ".315 at 75%"
appendix.tex:56 | 7.05 | "seed 123: 7.05"
appendix.tex:56 | 9.53 | "seed 456: 9.53"
appendix.tex:57 | 1.96 | "$\ell_z^* \gg 1.96$"
appendix.tex:58 | -0.14 ± 0.97 | "Llama-3.1-8B shows $\ell_z^*$ near zero ($-0.14 \pm 0.97$)"
appendix.tex:59 | 0.004 | "CV < 0.004"
appendix.tex:71 | 8.684 | "Qwen2.5-7B $\ell_z^*$ Mean: 8.684"
appendix.tex:71 | 1.412 | "Std: 1.412"
appendix.tex:71 | 2.475 | "Range: 2.475"
appendix.tex:71 | 0.163 | "CV: 0.163"
appendix.tex:72 | 0.679 | "Qwen Accuracy: 0.679"
appendix.tex:72 | 0.000 | "Std: 0.000"
appendix.tex:72 | 0.001 | "Range: 0.001"
appendix.tex:72 | 0.001 | "CV: 0.001"
appendix.tex:73 | -0.097 | "Qwen $\hat{\theta}_{\mathrm{MLE}}$: $-$0.097"
appendix.tex:73 | 0.012 | "Std: 0.012"
appendix.tex:73 | 0.023 | "Range: 0.023"
appendix.tex:73 | 0.119 | "CV: 0.119"
appendix.tex:75 | -0.141 | "Llama $\ell_z^*$: $-$0.141"
appendix.tex:75 | 0.965 | "Std: 0.965"
appendix.tex:75 | 1.929 | "Range: 1.929"
appendix.tex:75 | 6.860 | "CV: 6.860"
appendix.tex:76 | 0.594 | "Llama Accuracy: 0.594"
appendix.tex:76 | 0.002 | "Std: 0.002"
appendix.tex:76 | 0.004 | "Range: 0.004"
appendix.tex:76 | 0.004 | "CV: 0.004"
appendix.tex:77 | -0.645 | "Llama $\hat{\theta}_{\mathrm{MLE}}$: $-$0.645"
appendix.tex:77 | 0.019 | "Std: 0.019"
appendix.tex:77 | 0.036 | "Range: 0.036"
appendix.tex:77 | 0.029 | "CV: 0.029"
appendix.tex:84 | 4.303 | "$t_{0.025,2} = 4.303$"
appendix.tex:98 | -3.42 | "Qwen 15%: $-$3.42"
appendix.tex:98 | [-9.92, 3.08] | "Analytic CI [$-$9.92, 3.08]"
appendix.tex:98 | [-3.45, -2.82] | "Bootstrap CI [$-$3.45, $-$2.82]"
appendix.tex:99 | -0.99 | "Qwen 50%: $-$0.99"
appendix.tex:99 | [-4.02, 2.04] | "Analytic CI [$-$4.02, 2.04]"
appendix.tex:99 | [-0.99, -0.41] | "Bootstrap CI [$-$0.99, $-$0.41]"
appendix.tex:101 | -2.95 | "Llama 15%: $-$2.95"
appendix.tex:101 | [-8.70, 2.80] | "Analytic CI [$-$8.70, 2.80]"
appendix.tex:101 | [-5.89, -2.29] | "Bootstrap CI [$-$5.89, $-$2.29]"
appendix.tex:102 | -3.31 | "Llama 50%: $-$3.31"
appendix.tex:102 | [-9.63, 3.01] | "Analytic CI [$-$9.63, 3.01]"
appendix.tex:102 | [-6.47, -2.59] | "Bootstrap CI [$-$6.47, $-$2.59]"
appendix.tex:109 | 2.32 | "The $|\Delta d| = 2.32$ gap"
appendix.tex:109 | 0.8 | "exceeds conventional large-effect thresholds ($|d| > 0.8$)"
appendix.tex:130 | 0.514 | "Mistral ($\text{acc}{=}0.514$"
appendix.tex:130 | 5.42 | "$\ell_z^*{=}{+}5.42$"
appendix.tex:131 | -1.16 | "($\hat{\theta}{=}{-}1.16$)"
appendix.tex:136 | 12 | "12 models"
appendix.tex:136 | 5 | "5 benchmarks"
appendix.tex:136 | 60 | "60 cells"
appendix.tex:137 | 57 | "57 of 60 cells"
appendix.tex:137 | 1.96 | "$|\ell_z^*| > 1.96$"
appendix.tex:138 | 1.96 | "$|z| > 1.96$"
appendix.tex:138 | 4 | "4 of 60 cells"
appendix.tex:139 | 95% | "95% aberrance"
appendix.tex:139 | 7% | "7% by accuracy"
appendix.tex:148 | 160 | "z{=}160"
appendix.tex:148 | 0.0003 | "std{=}0.0003"
appendix.tex:160 | 0.50 | "Random baseline: 0.50"
appendix.tex:161 | 0.53 | "$\ell_z^*$ itemwise: 0.53"
appendix.tex:162 | 0.59 | "LR cross-model: 0.59"
appendix.tex:163 | 0.63 | "RF cross-model: 0.63"
appendix.tex:176 | 14,042 | "14,042 MMLU items"
appendix.tex:176 | 1,000 | "1,000 replications"
appendix.tex:179 | 200 | "200 testlets"
appendix.tex:179 | 70 | "70 items"
appendix.tex:181 | 0.043 | "Type I error 0.043"
appendix.tex:181 | 0.939 | "to 0.939"
appendix.tex:181 | 0.93 | "$d_{\text{ratio}} \geq 0.93$"
appendix.tex:181 | 0.5 | "for $\sigma_\tau \leq 0.5$"
appendix.tex:194 | 0.110 | "$\sigma_\tau = 0.3$: 0.110"
appendix.tex:194 | 1.002 | "ratio 1.002"
appendix.tex:194 | 1.038 | "ratio 1.038"
appendix.tex:195 | 0.454 | "$\sigma_\tau = 0.5$: 0.454"
appendix.tex:195 | 0.934 | "ratio 0.934"
appendix.tex:195 | 1.028 | "ratio 1.028"
appendix.tex:196 | 0.939 | "$\sigma_\tau = 1.0$: 0.939"
appendix.tex:196 | 0.705 | "ratio 0.705"
appendix.tex:196 | 1.061 | "ratio 1.061"
appendix.tex:202 | 98.5% | "maintains ${\geq}98.5\%$ power"
appendix.tex:213 | 0.987 | "$\sigma_{\text{mem}} = 0.5$: 0.987 power"
appendix.tex:213 | -2.107 | "d (15%): $-$2.107"
appendix.tex:213 | 0.991 | "Power (50%): 0.991"
appendix.tex:213 | -2.337 | "d (50%): $-$2.337"
appendix.tex:214 | 0.993 | "$\sigma_{\text{mem}} = 1.0$: 0.993 power"
appendix.tex:214 | -2.104 | "d (15%): $-$2.104"
appendix.tex:214 | 0.985 | "Power (50%): 0.985"
appendix.tex:214 | -1.587 | "d (50%): $-$1.587"
appendix.tex:223 | 100 | "100 trials"
appendix.tex:226 | 17.4% | "17.4% bias"
appendix.tex:226 | 5 | "still ${>}5$"
appendix.tex:229 | 4% | "${<}4\%$ bias"
appendix.tex:229 | 3.73 | "worst-case $|d| = 3.73$"
appendix.tex:229 | 12.20 | "(15% contamination) and $12.20$ (50%)"
appendix.tex:243 | -6.575 | "0% noise: $-$6.575"
appendix.tex:243 | 8.6 | "5% bias: 8.6"
appendix.tex:244 | -6.010 | "5% noise: $-$6.010"
appendix.tex:244 | 8.6 | "% bias: 8.6"
appendix.tex:244 | -0.925 | "5% noise 50%: $-$0.925"
appendix.tex:244 | 51.2 | "% bias: 51.2"
appendix.tex:245 | -5.433 | "10% noise: $-$5.433"
appendix.tex:245 | 17.4 | "% bias: 17.4"
appendix.tex:245 | -0.014 | "10% noise 50%: $-$0.014"
appendix.tex:245 | 99.3 | "% bias: 99.3"
appendix.tex:259 | 4.77 | "0% noise: 4.77"
appendix.tex:259 | 14.52 | "0% noise 50%: 14.52"
appendix.tex:260 | 5.07 | "5% noise: 5.07 $\pm$"
appendix.tex:260 | 0.24 | "$\pm$ 0.24"
appendix.tex:260 | 14.76 | "5% noise 50%: 14.76 $\pm$"
appendix.tex:260 | 0.44 | "$\pm$ 0.44"
appendix.tex:260 | 6.3 | "% bias: 6.3"
appendix.tex:260 | 1.6 | "% bias: 1.6"
appendix.tex:261 | 4.95 | "10% noise: 4.95 $\pm$"
appendix.tex:261 | 0.43 | "$\pm$ 0.43"
appendix.tex:261 | 3.73 | "(3.73)"
appendix.tex:261 | 14.45 | "10% noise 50%: 14.45 $\pm$"
appendix.tex:261 | 0.85 | "$\pm$ 0.85"
appendix.tex:261 | 12.20 | "(12.20)"
appendix.tex:261 | 3.7 | "% bias: 3.7"
appendix.tex:261 | 0.5 | "% bias: 0.5"
appendix.tex:270 | 22% | "mean reduction 22%"
appendix.tex:271 | -0.13 | "BCa CI [$-$0.13"
appendix.tex:271 | 2.21 | "2.21]"
appendix.tex:271 | 0.17 | "percentile CI [0.17"
appendix.tex:271 | 2.97 | "2.97]"
appendix.tex:276 | 0.013 | "examinee-to-item ratio of $N{:}J = 0.013$"
appendix.tex:277 | 500 | "typically required for stable 3PL estimation"
appendix.tex:281 | 11.2 | "mean$\,{=}\,$11.2"
appendix.tex:286 | 10,558 | "($n{=}10{,}558$ matched items)"
appendix.tex:290 | 0.127 | "Pearson $r$: 0.127"
appendix.tex:290 | 0.135 | "Spearman $\rho$: 0.135"
appendix.tex:294 | 0.663 | "Pearson $r$: 0.663"
appendix.tex:294 | 0.684 | "Spearman $\rho$: 0.684"
appendix.tex:295 | -0.029 | "Pearson $r$: $-$0.029"
appendix.tex:295 | 0.050 | "Spearman $\rho$: 0.050"
appendix.tex:296 | 0.608 | "Pearson $r$: 0.608"
appendix.tex:296 | 0.656 | "Spearman $\rho$: 0.656"
appendix.tex:306 | 1,500 | "1,500 steps"
appendix.tex:306 | 11.4pp | "accuracy gap ($11.4\text{pp} \to 2.1\text{pp}$)"
appendix.tex:306 | 2.1pp | "to 2.1pp"
appendix.tex:306 | 3.3 | "$\ell_z^*$ response-pattern gap persists (${\sim}3.3$"
appendix.tex:307 | 0.611 | "weak MIA signal (AUC-ROC${=}0.611$)"
appendix.tex:307 | 0.493 | "AUC to $0.493$ (step~500)"
appendix.tex:307 | 0.493 | "AUC $0.493$ (step~1000)"
appendix.tex:307 | 0.493 | "AUC $0.493$ (step~1500)"
appendix.tex:307 | 0.50 | "random chance ($0.50$)"
appendix.tex:323 | 5 × 10^-6 | "Learning rate: $5 \times 10^{-6}$"
appendix.tex:324 | 2 | "Per-device batch size: 2"
appendix.tex:325 | 4 | "Gradient accumulation steps: 4"
appendix.tex:326 | 16 | "Num. generations per prompt: 16"
appendix.tex:327 | 128 | "Max completion length: 128"
appendix.tex:328 | 1.2 | "Sampling temperature: 1.2"
appendix.tex:329 | 1,500 | "Training steps: 1,500"
appendix.tex:329 | 500 | "checkpoints at 500"
appendix.tex:329 | 1000 | "checkpoints at 1000"
appendix.tex:329 | 1500 | "checkpoints at 1500"
appendix.tex:330 | 1.0 | "Reward function: $+1.0$"
appendix.tex:330 | -1.0 | "Reward function: $-1.0$"
appendix.tex:331 | 16 | "LoRA rank: 16"
appendix.tex:331 | 32 | "$\alpha$: 32"
appendix.tex:331 | 0.05 | "dropout: 0.05"
appendix.tex:355 | 16 | "LoRA rank: 16"
appendix.tex:357 | 32 | "LoRA $\alpha$: 32"
appendix.tex:358 | 0.05 | "LoRA dropout: 0.05"
appendix.tex:360 | 2 × 10^-4 | "Learning rate: $2 \times 10^{-4}$"
appendix.tex:364 | 0.1 | "Warmup ratio: 0.1"
appendix.tex:365 | 3 | "Epochs: 3"
appendix.tex:366 | 4 | "Per-device batch size: 4"
appendix.tex:367 | 4 | "Gradient accumulation steps: 4"
appendix.tex:368 | 16 | "Effective batch size: 16"
appendix.tex:369 | 512 | "Max sequence length: 512"
appendix.tex:380 | 10 | "n{=}10$ clean baseline"
appendix.tex:381 | 0.74 | "s = 0.74"
appendix.tex:389 | 6.57 | "Seed 42, 15%: 6.57"
appendix.tex:389 | 8.22 | "Seed 42, 25%: 8.22"
appendix.tex:389 | 1.90 | "Seed 42, 50%: 1.90"
appendix.tex:389 | 4.77 | "Seed 42 fixed, 15%: 4.77"
appendix.tex:389 | 4.96 | "Seed 42 fixed, 25%: 4.96"
appendix.tex:389 | 14.52 | "Seed 42 fixed, 50%: 14.52"
appendix.tex:390 | 5.09 | "Seed 123, 15%: 5.09"
appendix.tex:390 | 8.78 | "Seed 123, 25%: 8.78"
appendix.tex:390 | 5.42 | "Seed 123, 50%: 5.42"
appendix.tex:390 | 7.79 | "Seed 123 fixed, 15%: 7.79"
appendix.tex:390 | 5.37 | "Seed 123 fixed, 25%: 5.37"
appendix.tex:390 | 12.64 | "Seed 123 fixed, 50%: 12.64"
appendix.tex:391 | 4.41 | "Seed 456, 15%: 4.41"
appendix.tex:391 | 5.31 | "Seed 456, 25%: 5.31"
appendix.tex:391 | 7.91 | "Seed 456, 50%: 7.91"
appendix.tex:391 | 7.99 | "Seed 456 fixed, 15%: 7.99"
appendix.tex:391 | 7.34 | "Seed 456 fixed, 25%: 7.34"
appendix.tex:391 | 9.80 | "Seed 456 fixed, 50%: 9.80"
appendix.tex:393 | 5.36 | "Mean 15%: 5.36"
appendix.tex:393 | 7.44 | "Mean 25%: 7.44"
appendix.tex:393 | 5.08 | "Mean 50%: 5.08"
appendix.tex:393 | 6.85 | "Mean fixed 15%: 6.85"
appendix.tex:393 | 5.89 | "Mean fixed 25%: 5.89"
appendix.tex:393 | 12.32 | "Mean fixed 50%: 12.32"
appendix.tex:394 | 1.10 | "SD 15%: 1.10"
appendix.tex:394 | 1.86 | "SD 25%: 1.86"
appendix.tex:394 | 3.02 | "SD 50%: 3.02"
appendix.tex:394 | 1.80 | "SD fixed 15%: 1.80"
appendix.tex:394 | 1.27 | "SD fixed 25%: 1.27"
appendix.tex:394 | 2.38 | "SD fixed 50%: 2.38"
appendix.tex:395 | 20.3 | "CV (%) 15%: 20.3"
appendix.tex:395 | 25.2 | "CV (%) 25%: 25.2"
appendix.tex:395 | 59.6 | "CV (%) 50%: 59.6"
appendix.tex:395 | 26.3 | "CV fixed (%) 15%: 26.3"
appendix.tex:395 | 21.7 | "CV fixed (%) 25%: 21.7"
appendix.tex:395 | 19.3 | "CV fixed (%) 50%: 19.3"
appendix.tex:414 | 7.26 | "Seed 42 HT 15%: 7.26"
appendix.tex:414 | 8.90 | "Seed 42 HT 25%: 8.90"
appendix.tex:414 | 1.66 | "Seed 42 HT 50%: 1.66"
appendix.tex:414 | 42.3 | "Seed 42 Acc z 15%: 42.3"
appendix.tex:414 | 49.8 | "Seed 42 Acc z 25%: 49.8"
appendix.tex:414 | 68.7 | "Seed 42 Acc z 50%: 68.7"
appendix.tex:415 | 5.52 | "Seed 123 HT 15%: 5.52"
appendix.tex:415 | 9.51 | "Seed 123 HT 25%: 9.51"
appendix.tex:415 | 5.80 | "Seed 123 HT 50%: 5.80"
appendix.tex:415 | 47.3 | "Seed 123 Acc z 15%: 47.3"
appendix.tex:415 | 53.4 | "Seed 123 Acc z 25%: 53.4"
appendix.tex:415 | 70.8 | "Seed 123 Acc z 50%: 70.8"
appendix.tex:416 | 4.72 | "Seed 456 HT 15%: 4.72"
appendix.tex:416 | 5.10 | "Seed 456 HT 25%: 5.10"
appendix.tex:416 | 8.41 | "Seed 456 HT 50%: 8.41"
appendix.tex:416 | 45.4 | "Seed 456 Acc z 15%: 45.4"
appendix.tex:416 | 51.3 | "Seed 456 Acc z 25%: 51.3"
appendix.tex:416 | 70.4 | "Seed 456 Acc z 50%: 70.4"
appendix.tex:418 | 5.83 | "HT Mean 15%: 5.83"
appendix.tex:418 | 7.84 | "HT Mean 25%: 7.84"
appendix.tex:418 | 5.29 | "HT Mean 50%: 5.29"
appendix.tex:418 | 45.0 | "Acc z Mean 15%: 45.0"
appendix.tex:418 | 51.5 | "Acc z Mean 25%: 51.5"
appendix.tex:418 | 70.0 | "Acc z Mean 50%: 70.0"
appendix.tex:419 | 1.30 | "HT SD 15%: 1.30"
appendix.tex:419 | 2.39 | "HT SD 25%: 2.39"
appendix.tex:419 | 3.41 | "HT SD 50%: 3.41"
appendix.tex:419 | 2.5 | "Acc z SD 15%: 2.5"
appendix.tex:419 | 1.8 | "Acc z SD 25%: 1.8"
appendix.tex:419 | 1.1 | "Acc z SD 50%: 1.1"
appendix.tex:428 | 700 | "700 contaminated items"
appendix.tex:438 | -3.22 | "Llama 5%, s1: $-$3.22"
appendix.tex:438 | -3.06 | "Llama 5%, s2: $-$3.06"
appendix.tex:438 | -1.44 | "Llama 5%, s3: $-$1.44"
appendix.tex:438 | -2.57 | "Llama 5% Mean: $-$2.57"
appendix.tex:438 | 0.99 | "Llama 5% SD: 0.99"
appendix.tex:439 | -2.11 | "Llama 15%, s1: $-$2.11"
appendix.tex:439 | -3.21 | "Llama 15%, s2: $-$3.21"
appendix.tex:439 | -3.09 | "Llama 15%, s3: $-$3.09"
appendix.tex:439 | -2.80 | "Llama 15% Mean: $-$2.80"
appendix.tex:439 | 0.60 | "Llama 15% SD: 0.60"
appendix.tex:440 | -3.16 | "Llama 25%, s1: $-$3.16"
appendix.tex:440 | -2.28 | "Llama 25%, s2: $-$2.28"
appendix.tex:440 | -2.24 | "Llama 25%, s3: $-$2.24"
appendix.tex:440 | -2.56 | "Llama 25% Mean: $-$2.56"
appendix.tex:440 | 0.52 | "Llama 25% SD: 0.52"
appendix.tex:441 | -2.33 | "Llama 50%, s1: $-$2.33"
appendix.tex:441 | -2.59 | "Llama 50%, s2: $-$2.59"
appendix.tex:441 | -1.99 | "Llama 50%, s3: $-$1.99"
appendix.tex:441 | -2.30 | "Llama 50% Mean: $-$2.30"
appendix.tex:441 | 0.30 | "Llama 50% SD: 0.30"
appendix.tex:446 | 2.30-2.80 | "flat across contamination levels ($2.30$--$2.80$)"
appendix.tex:446 | 39% | "CV: 39% at 5%"
appendix.tex:446 | 13% | "CV: 13% at 50%"
appendix.tex:452 | 2 | "only $n{=}2$ seeds"
appendix.tex:460 | -2.82 | "Mistral 5%, s1: $-$2.82"
appendix.tex:460 | -4.83 | "Mistral 5%, s2: $-$4.83"
appendix.tex:460 | -3.83 | "Mistral 5% Mean: $-$3.83"
appendix.tex:460 | 1.42 | "Mistral 5% SD: 1.42"
appendix.tex:461 | -2.64 | "Mistral 15%, s1: $-$2.64"
appendix.tex:461 | -3.98 | "Mistral 15%, s2: $-$3.98"
appendix.tex:461 | -3.48 | "Mistral 15%, s3: $-$3.48"
appendix.tex:461 | -3.37 | "Mistral 15% Mean: $-$3.37"
appendix.tex:461 | 0.68 | "Mistral 15% SD: 0.68"
appendix.tex:462 | -3.50 | "Mistral 50%, s1: $-$3.50"
appendix.tex:462 | -4.25 | "Mistral 50%, s2: $-$4.25"
appendix.tex:462 | -4.51 | "Mistral 50%, s3: $-$4.51"
appendix.tex:462 | -4.09 | "Mistral 50% Mean: $-$4.09"
appendix.tex:462 | 0.53 | "Mistral 50% SD: 0.53"

---

This comprehensive catalog contains every numerical value found across all seven .tex files, organized by source file and line number, with full context for each value. The numbers span effect sizes, contamination percentages, sample sizes, confidence intervals, power analyses, model parameters, and more.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa7880d2-39c1-4fb9-b520-d2867294859b",
  "isSidechain": true,
  "agentId": "a4f6b5b2e69085d89",
  "requestId": "req_011CbPrbd5tSQzk1UTE5JhC4",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5f5e8a66-aefe-4f76-935d-21b2d70b8192",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/.claude/sessions/director_15982409",
  "sessionId": "df7ba475-8d90-415a-aeb6-4ae6ec2ddc56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "ancient-jingling-beacon",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BBZNKMRexPBbSLxmPUtjma",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 24497,
      "cache_read_input_tokens": 37383,
      "output_tokens": 16139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24497
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 16139,
          "cache_read_input_tokens": 37383,
          "cache_creation_input_tokens": 24497,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24497,
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
