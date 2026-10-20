# Research conversation: Read the following files in /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a383bcd948b1952d6.jsonl`
- **Structured JSON:** [`482ba9da074b22db7a75.json`](../../sessions/48/482ba9da074b22db7a75.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

30 recorded events

### User

_source line 1 · 2026-05-22T10:00:58.457Z_

Read the following files in /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ and report their FULL contents:

1. related_work.tex
2. references.bib (search for "Du" and "Tanaka" entries, and "Schaeffer" entries)
3. introduction.tex (for the contributions list)
4. discussion.tex
5. appendix.tex (search for "specification curve" and "SCA" mentions)

Report exact text verbatim, especially:
- The exact citation entry for Du & Tanaka-Ishii
- The exact contributions list
- The exact discussion section text
- Any mention of Schaeffer et al.
- Any mention of specification curve analysis

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "52a92da4-9638-4bcf-884f-bc5fb5f5990b",
  "agentId": "a383bcd948b1952d6",
  "type": "user",
  "uuid": "aa963d77-87e0-4daa-8c0d-6e9fc344544e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T10:01:00.710Z_

I'll read these files from the paper directory for you. Let me start by checking what files exist and then read each one.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa963d77-87e0-4daa-8c0d-6e9fc344544e",
  "isSidechain": true,
  "agentId": "a383bcd948b1952d6",
  "requestId": "req_011CbHQwHjofX2nYpL8h38Ta",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "69cca307-6544-4bb8-837e-68c7d018da3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W2A62MbeoBMttMv94DQbE4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15713,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15713,
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

_source line 3 · 2026-05-22T10:01:00.883Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01D8dQxhBaURZ9K213FRGuL9`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ -type f -name \"*.tex\" -o -name \"*.bib\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69cca307-6544-4bb8-837e-68c7d018da3a",
  "isSidechain": true,
  "agentId": "a383bcd948b1952d6",
  "requestId": "req_011CbHQwHjofX2nYpL8h38Ta",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "135a8536-82dc-402e-bc5b-8ca57edf144b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01W2A62MbeoBMttMv94DQbE4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15713,
      "cache_read_input_tokens": 0,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15713
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 131,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15713,
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

_source line 4 · 2026-05-22T10:01:01.053Z_

<details><summary>↩ Tool result · `toolu_01D8dQxhBaURZ9K213FRGuL9`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/intro_reframe.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method_reframe.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ethics.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/theory.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work_reframe.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments_reframe.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/discussion_reframe.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "135a8536-82dc-402e-bc5b-8ca57edf144b",
  "isSidechain": true,
  "promptId": "52a92da4-9638-4bcf-884f-bc5fb5f5990b",
  "agentId": "a383bcd948b1952d6",
  "type": "user",
  "uuid": "873847c8-2ba0-40fb-b61b-ef912fe97965",
  "sourceToolAssistantUUID": "135a8536-82dc-402e-bc5b-8ca57edf144b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-22T10:01:02.674Z_

Now let me read the requested files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "873847c8-2ba0-40fb-b61b-ef912fe97965",
  "isSidechain": true,
  "agentId": "a383bcd948b1952d6",
  "requestId": "req_011CbHQwUpZ6CpEg4CQUmKkq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "45f1a226-a498-4bee-b2a1-d654a68493ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RHSYRaASQdq4xGnJTNgiaX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1719,
      "cache_read_input_tokens": 15713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1719,
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

_source line 6 · 2026-05-22T10:01:03.244Z_

<details open><summary>🔧 Tool call — Read · `toolu_013QRhg5pnmRGFUHFFiFzZuZ`</summary>

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
  "parentUuid": "45f1a226-a498-4bee-b2a1-d654a68493ed",
  "isSidechain": true,
  "agentId": "a383bcd948b1952d6",
  "requestId": "req_011CbHQwUpZ6CpEg4CQUmKkq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "286999ab-d11e-455d-aa38-6153b71720fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RHSYRaASQdq4xGnJTNgiaX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1719,
      "cache_read_input_tokens": 15713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1719,
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

### Tool result

_source line 7 · 2026-05-22T10:01:03.254Z_

<details><summary>↩ Tool result · `toolu_013QRhg5pnmRGFUHFFiFzZuZ`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Model collapse and canary metrics.}
5	Iterative training collapse was formalized by \citet{shumailov2024curse} and \citet{alemohammad2024mad}, who showed that recursively replacing real data with model-generated text causes progressive tail erosion; \citet{schaeffer2025position} systematize eight distinct notions of ``collapse'' that this literature conflates.
6	Theoretical analyses have sharpened these results: \citet{dohmatob2024tale} recast collapse as a change in scaling-law exponents, \citet{dohmatob2025strong} proved that collapse can occur even at vanishingly small synthetic fractions, \citet{seddik2025statistical} provide a statistical analysis of iterative contamination dynamics, and \citet{marchi2025challenging} challenge the universality of collapse under diverse training conditions.
7	Several works have proposed monitoring metrics: \citet{du2026geometric} observe that calibration error rises before accuracy degrades, \citet{du2025scales} report ECE increases at 30\% contamination before accuracy drops, \citet{gambetta2024surplexity} introduces surplexity as a collapse detector, and \citet{drayson2025detection} show that machine-generated text detection can prevent collapse, and \citet{li2025verification} propose verification-based mitigation.
8	We differ from the closest predecessor, \citet{du2026geometric}, in four respects: (i)~we compare an entire family of canary metrics; (ii)~we cross-validate across five statistical methods; (iii)~we map detectability as a function of contamination regime; and (iv)~we treat method-selection sensitivity itself as a primary finding.
9	
10	\paragraph{Data mixing phase transitions.}
11	\citet{kazdan2025collapse} map the conditions under which synthetic data triggers collapse versus improves performance, \citet{gu2024cmr} establish a scaling law for critical mixture ratios in continual pre-training, and \citet{gu2025datamixing} show that data mixing can induce phase transitions in knowledge acquisition---a direct theoretical analogue to our detection threshold, where a critical mixing ratio separates qualitatively different detection regimes.
12	
13	\paragraph{Critical transitions and lead-lag methodology.}
14	\citet{scheffer2009early} established that systems approaching tipping points exhibit generic early-warning signals (rising autocorrelation and variance); \citet{dakos2012methods} developed a practical toolkit for estimating such signals, while \citet{boettiger2012limits} quantified detection limits in short time series---directly relevant to iterative training where $T{=}5$--$20$.
15	Crucially, \citet{truong2026phase} prove that entropy collapse in iterative training is a first-order (discontinuous) phase transition, structurally ruling out critical-slowing-down (CSD) early-warning signals.
16	Our ``detection onset'' is a \emph{statistical} threshold (PermG power crossing the detection threshold), not a thermodynamic phase transition, and our cascade ordering describes within-generation temporal ordering of metrics, not CSD-type precursors.
17	The standard framework for testing temporal precedence is Granger causality~\cite{granger1969investigating}, with neural extensions for nonlinear settings~\citep{marcinkevics2022neural}; however, non-stationary series inflate rejection rates~\cite{granger1974spurious}, and the Toda--Yamamoto procedure~\cite{toda1995statistical} addresses this at reduced degrees of freedom severe in short series.
18	These methods are largely absent from the model collapse literature.
19	
20	\paragraph{Analytical robustness.}
21	\citet{bell2022modeling} introduced multiverse analysis to ML, \citet{coretta2023multidimensional} demonstrated that 46 teams reached different conclusions on identical data, and \citet{kapoor2024reforms} synthesized these concerns into a consensus checklist.
22	Our work applies this perspective to model collapse: five methods across multiple contamination regimes produce conclusions ranging from universal significance to complete null.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "286999ab-d11e-455d-aa38-6153b71720fe",
  "isSidechain": true,
  "promptId": "52a92da4-9638-4bcf-884f-bc5fb5f5990b",
  "agentId": "a383bcd948b1952d6",
  "type": "user",
  "uuid": "776de08d-b874-4f03-b294-50e1199e0ac1",
  "sourceToolAssistantUUID": "286999ab-d11e-455d-aa38-6153b71720fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T10:01:03.388Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GEZbv7n2UrTUuAFdvakYnX`</summary>

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
  "parentUuid": "776de08d-b874-4f03-b294-50e1199e0ac1",
  "isSidechain": true,
  "agentId": "a383bcd948b1952d6",
  "requestId": "req_011CbHQwUpZ6CpEg4CQUmKkq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a1b34cb1-29d8-46d2-95bf-e853b38aaed8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RHSYRaASQdq4xGnJTNgiaX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1719,
      "cache_read_input_tokens": 15713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1719,
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

### Tool result

_source line 9 · 2026-05-22T10:01:03.401Z_

<details><summary>↩ Tool result · `toolu_01GEZbv7n2UrTUuAFdvakYnX`</summary>

```text
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
12	Our detection mechanism (Granger-causal temporal precedence) differs from critical-slowing-down indicators, as model collapse is a first-order transition~\cite{truong2026phase} (\S\ref{sec:related_work}).
13	
14	We systematically map this landscape using Pythia-410M~\cite{biderman2023pythia} across thirteen contamination levels with multi-seed replication, applying five statistical methods from econometrics~\cite{granger1974spurious,toda1995statistical} to identical data.
15	The resulting map reveals structured terrain: blind zones where collapse proceeds undetected, a sharp onset where detection jumps from null to reliable within a 2-percentage-point interval, a non-monotonic dip where Granger detection fails despite confirmed causal flow, and a detection boundary $\alpha_c(T)$ that follows a power law in observation length.
16	Cross-architecture validation across five families (345M--6.9B) confirms the landscape generalizes when entropy-diversity coupling is preserved.
17	Granger precedence establishes temporal predictive improvement, not true causality~\cite{shojaie2022granger}; our canary claim is scoped to diversity metrics (distinct-$n$~\cite{li2016diversity}).
18	
19	Our contributions are:
20	\begin{enumerate}
21	    \item \textbf{Detectability landscape characterization} (\S\ref{sec:regime}--\ref{sec:intervention}).
22	    PermG establishes a monotonically decreasing detection boundary $\alpha_c(T) = A \cdot T^{-1/(2\beta)}$ from a sub-linear signal model (Proposition~\ref{prop:phase-boundary}; $\beta{=}0.24$, $\gamma{=}2.08$, cross-$T$ validated MAE${=}0.106$); since $\alpha_\infty{\approx}0$, any nonzero contamination produces signal, but sub-linear growth makes detection a function of $T$.
23	    Predict-then-verify at $T{=}20$ matches 3/5 predictions in saturated regimes, with systematic conservative bias at boundary $\alpha$ (Appendix~\ref{app:t20_prediction_timeline}); canary-triggered cessation reduces peak perplexity by 58\%.
24	
25	    \item \textbf{Formal motivation for canary metric selection} (\S\ref{sec:cascade}).
26	    Under mode amplification, entropy Granger-precedes diversity (Proposition~\ref{thm:entropy_leads}), with a ${\geq}1$-generation lag (Proposition~\ref{prop:div_lag}), confirmed in 14/15 experiments ($\alpha \geq 0.30$; GPT-2-medium s43 bidirectional).
27	
28	    \item \textbf{Method sensitivity as a primary finding} (\S\ref{sec:mmct}--\ref{sec:dose_response}).
29	    Five detection methods yield null-control FPR from 0\% to 92\%; the same Granger test shifts from 0/8 to 6/8 within a 2-percentage-point interval.
30	    The detectability landscape one observes depends critically on the statistical method used to probe it.
31	\end{enumerate}
32	
33	\begin{figure*}[t]
34	\centering
35	\includegraphics[width=0.55\textwidth]{figures/fig_phase_diagram.pdf}
36	\caption{Detection phase diagram (Pythia-410M, fp32, PermG direction-checked). Each cell shows the number of FDR-significant canary$\to$diversity pairs (of~8) at a given contamination strength~$\alpha$ and observation window~$T$. The dashed curve is the theoretical detection boundary $\alpha_c(T) \propto T^{-\gamma}$ with $\gamma{=}2.08$ (Proposition~\ref{prop:phase-boundary}). Diamond markers ($\diamond$) flag the synchronous dip at $\alpha{=}0.60$ (0/8 at $T{\leq}20$); the star ($\star$) marks its dissolution at $T{=}25$ (5/8), validating $\sqrt{T}$ power scaling. Dagger ($\dagger$): seed sensitivity at boundary ($T{=}10$, $\alpha{=}0.50$: s42${=}$6/8, s43${=}$0/8).}
37	\label{fig:regime_map}
38	\end{figure*}
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1b34cb1-29d8-46d2-95bf-e853b38aaed8",
  "isSidechain": true,
  "promptId": "52a92da4-9638-4bcf-884f-bc5fb5f5990b",
  "agentId": "a383bcd948b1952d6",
  "type": "user",
  "uuid": "9ef1db55-34e8-4f83-b6aa-4b82471989f7",
  "sourceToolAssistantUUID": "a1b34cb1-29d8-46d2-95bf-e853b38aaed8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-22T10:01:03.571Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PGuD4V7ZyVzBYwCojoGPMK`</summary>

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
  "parentUuid": "9ef1db55-34e8-4f83-b6aa-4b82471989f7",
  "isSidechain": true,
  "agentId": "a383bcd948b1952d6",
  "requestId": "req_011CbHQwUpZ6CpEg4CQUmKkq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1d4f090b-5e8b-45fe-bf36-2495b8ffd92c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RHSYRaASQdq4xGnJTNgiaX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1719,
      "cache_read_input_tokens": 15713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1719,
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

### Tool result

_source line 11 · 2026-05-22T10:01:03.577Z_

<details><summary>↩ Tool result · `toolu_01PGuD4V7ZyVzBYwCojoGPMK`</summary>

```text
1	\section{Discussion and Conclusion}\label{sec:discussion}
2	
3	\paragraph{Granger precedence is not causation.}
4	Our claim is scoped to temporal predictive improvement~\cite{granger1969investigating,shojaie2022granger}; bivariate tests cannot exclude confounders.
5	$\alpha_c(T)$ decreases monotonically ($\gamma{=}2.08$, cross-$T$ MAE${=}0.106$); predict-then-verify shows systematic conservative bias, and MAUVE floor saturation limits detection to $6/8$.
6	The non-monotonic dip at $\alpha{=}0.60$ dissolves by $T{=}25$ ($5/8$), validating $\sqrt{T}$ scaling; entropy is a one-generation canary (14/15 cascade, $-$58\% perplexity).
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d4f090b-5e8b-45fe-bf36-2495b8ffd92c",
  "isSidechain": true,
  "promptId": "52a92da4-9638-4bcf-884f-bc5fb5f5990b",
  "agentId": "a383bcd948b1952d6",
  "type": "user",
  "uuid": "c4d7e126-6de7-4400-a483-732b7673dfba",
  "sourceToolAssistantUUID": "1d4f090b-5e8b-45fe-bf36-2495b8ffd92c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-22T10:01:03.800Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Qq8BxUZuRXmKYeLA9VLDeH`</summary>

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
  "parentUuid": "c4d7e126-6de7-4400-a483-732b7673dfba",
  "isSidechain": true,
  "agentId": "a383bcd948b1952d6",
  "requestId": "req_011CbHQwUpZ6CpEg4CQUmKkq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "689cf190-f924-4516-9c99-7b66cfd749e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RHSYRaASQdq4xGnJTNgiaX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1719,
      "cache_read_input_tokens": 15713,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1719,
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

_source line 13 · 2026-05-22T10:01:04.027Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B2f2P5jVnAiW1U35YrJjfS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "689cf190-f924-4516-9c99-7b66cfd749e6",
  "isSidechain": true,
  "agentId": "a383bcd948b1952d6",
  "requestId": "req_011CbHQwUpZ6CpEg4CQUmKkq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a0e356ab-5fde-40cb-9cb4-59c70a849c9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RHSYRaASQdq4xGnJTNgiaX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1719,
      "cache_read_input_tokens": 15713,
      "output_tokens": 390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1719
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 390,
          "cache_read_input_tokens": 15713,
          "cache_creation_input_tokens": 1719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1719,
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

_source line 14 · 2026-05-22T10:01:04.037Z_

<details><summary>↩ Tool result · `toolu_01B2f2P5jVnAiW1U35YrJjfS`</summary>

```text
1	% ============================================================
2	% GAME THEORY / ATTRIBUTION
3	% ============================================================
4	
5	@incollection{shapley1953value,
6	  title     = {A Value for $n$-Person Games},
7	  author    = {Shapley, Lloyd S.},
8	  booktitle = {Contributions to the Theory of Games II},
9	  editor    = {Kuhn, Harold W. and Tucker, Albert W.},
10	  pages     = {307--317},
11	  year      = {1953},
12	  publisher = {Princeton University Press},
13	}
14	
15	% ============================================================
16	% CORE MODEL COLLAPSE
17	% ============================================================
18	
19	@article{shumailov2024curse,
20	  title     = {The Curse of Recursion: Training on Generated Data Makes Models Forget},
21	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Gal, Yarin and Papernot, Nicolas and Anderson, Ross},
22	  journal   = {Nature},
23	  year      = {2024},
24	  url       = {https://arxiv.org/abs/2305.17493},
25	}
26	
27	@inproceedings{alemohammad2024mad,
28	  title     = {Self-Consuming Generative Models Go {MAD}},
29	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard},
30	  booktitle = {International Conference on Learning Representations},
31	  year      = {2024},
32	  url       = {https://arxiv.org/abs/2307.01850},
33	}
34	
35	@inproceedings{dohmatob2024tale,
36	  title     = {A Tale of Tails: Model Collapse as a Change of Scaling Laws},
37	  author    = {Dohmatob, Elvis and Feng, Yunzhen and others},
38	  booktitle = {International Conference on Machine Learning},
39	  year      = {2024},
40	  url       = {https://arxiv.org/abs/2402.07043},
41	}
42	
43	@inproceedings{dohmatob2025strong,
44	  title     = {Strong Model Collapse},
45	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
46	  booktitle = {International Conference on Learning Representations},
47	  year      = {2025},
48	  url       = {https://arxiv.org/abs/2410.04840},
49	}
50	
51	@article{du2026geometric,
52	  title     = {Escaping Mode Collapse in {LLM} Generation via Geometric Regulation},
53	  author    = {Du, Xin and Tanaka-Ishii, Kumiko},
54	  journal   = {arXiv preprint arXiv:2605.00435},
55	  year      = {2026},
56	  url       = {https://arxiv.org/abs/2605.00435},
57	}
58	
59	% ============================================================
60	% CANARY / EARLY WARNING METRICS
61	% ============================================================
62	
63	@article{du2025scales,
64	  title     = {Characterizing Model Behavior Under Synthetic Data Training: An Empirical Study Across Scales and Mixing Ratios},
65	  author    = {Du, Y. and Wu, G. and Tang, G. and Wang, W. and Fan, Q.},
66	  journal   = {arXiv preprint arXiv:2510.05133},
67	  year      = {2025},
68	  url       = {https://arxiv.org/abs/2510.05133},
69	}
70	
71	@article{gambetta2024surplexity,
72	  title     = {Learning by Surprise: Surplexity for Mitigating Model Collapse in Generative {AI}},
73	  author    = {Gambetta, Daniele and others},
74	  journal   = {arXiv preprint arXiv:2410.12341},
75	  year      = {2024},
76	  url       = {https://arxiv.org/abs/2410.12341},
77	}
78	
79	
80	@article{sigma2026spectral,
81	  title     = {{SIGMA}: Scalable Spectral Insights for {LLM} Model Collapse},
82	  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},
83	  journal   = {arXiv preprint arXiv:2601.03385},
84	  year      = {2026},
85	  url       = {https://arxiv.org/abs/2601.03385},
86	}
87	
88	
89	
90	@article{seddik2025statistical,
91	  title     = {A Statistical Analysis of Iterative Training Data Contamination},
92	  author    = {Seddik, Mohamed El Amine and others},
93	  journal   = {arXiv preprint arXiv:2602.10531},
94	  year      = {2025},
95	  url       = {https://arxiv.org/abs/2602.10531},
96	}
97	
98	@article{marchi2025challenging,
99	  title     = {Challenging the Universality of Model Collapse},
100	  author    = {Marchi, Andrea and others},
101	  journal   = {arXiv preprint arXiv:2505.19046},
102	  year      = {2025},
103	  url       = {https://arxiv.org/abs/2505.19046},
104	}
105	
106	@article{li2025verification,
107	  title     = {Verification-Based Mitigation of Model Collapse},
108	  author    = {Li, Yang and others},
109	  journal   = {arXiv preprint arXiv:2510.16657},
110	  year      = {2025},
111	  url       = {https://arxiv.org/abs/2510.16657},
112	}
113	
114	% ============================================================
115	% DIVERSITY METRICS (BACKGROUND)
116	% ============================================================
117	
118	
119	@inproceedings{li2016diversity,
120	  title     = {A Diversity-Promoting Objective Function for Neural Conversation Models},
121	  author    = {Li, Jiwei and others},
122	  booktitle = {North American Chapter of the Association for Computational Linguistics},
123	  year      = {2016},
124	  url       = {https://arxiv.org/abs/1510.03055},
125	}
126	
127	% ============================================================
128	% DATA MIXING & ACCUMULATION
129	% ============================================================
130	
131	@inproceedings{kazdan2025collapse,
132	  title     = {Collapse or Thrive? {P}erils and Promises of Synthetic Data in a Self-Generating World},
133	  author    = {Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David L. and Koyejo, Sanmi},
134	  booktitle = {International Conference on Machine Learning},
135	  year      = {2025},
136	  url       = {https://arxiv.org/abs/2410.16713},
137	}
138	
139	@inproceedings{dey2024breaking,
140	  title     = {Is Model Collapse Inevitable? {B}reaking the Curse of Recursion by Accumulating Real and Synthetic Data},
141	  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
142	  booktitle = {International Conference on Machine Learning},
143	  year      = {2024},
144	  url       = {https://arxiv.org/abs/2404.01413},
145	}
146	
147	% ============================================================
148	% MITIGATION & VERIFICATION
149	% ============================================================
150	
151	@article{dces2026counter,
152	  title     = {Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling},
153	  author    = {Zhu, Bingze and Xie, Yubo},
154	  journal   = {Electronics},
155	  year      = {2026},
156	  url       = {https://www.mdpi.com/2079-9292/15/4/869},
157	}
158	
159	@article{drayson2025detection,
160	  title     = {Machine-generated text detection prevents language model collapse},
161	  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
162	  journal   = {arXiv preprint arXiv:2502.15654},
163	  year      = {2025},
164	  url       = {https://arxiv.org/abs/2502.15654},
165	}
166	
167	% ============================================================
168	% POSITION / SURVEY / EPISTEMICS / ANALYTICAL ROBUSTNESS
169	% ============================================================
170	
171	@inproceedings{bell2022modeling,
172	  title     = {Modeling the Machine Learning Multiverse},
173	  author    = {Bell, Samuel J. and Kampman, Onno P. and Dodge, Jesse and Lawrence, Neil D.},
174	  booktitle = {Advances in Neural Information Processing Systems},
175	  year      = {2022},
176	  url       = {https://arxiv.org/abs/2206.05985},
177	}
178	
179	@article{kapoor2024reforms,
180	  title     = {{REFORMS}: Consensus-based Recommendations for Machine-learning-based Science},
181	  author    = {Kapoor, Sayash and Cantrell, Emily and Peng, Kenny and Pham, Thanh Hien and Bail, Christopher A. and Gundersen, Odd Erik and Hofman, Jake M. and Hullman, Jessica and Lones, Michael A. and Malik, Momin M. and Nanayakkara, Priyanka and Poldrack, Russell A. and Raji, Inioluwa Deborah and Roberts, Michael and Salganik, Matthew J. and Serra-Garcia, Marta and Stewart, Brandon M. and Vandewiele, Gilles and Narayanan, Arvind},
182	  journal   = {Science Advances},
183	  volume    = {10},
184	  number    = {18},
185	  pages     = {eadk3452},
186	  year      = {2024},
187	  doi       = {10.1126/sciadv.adk3452},
188	}
189	
190	@article{coretta2023multidimensional,
191	  title     = {Multidimensional Signals and Analytic Flexibility: Estimating Degrees of Freedom in Human-Speech Analyses},
192	  author    = {Coretta, Stefano and Casillas, Joseph V. and Roessig, Simon and Franke, Michael and others},
193	  journal   = {Advances in Methods and Practices in Psychological Science},
194	  volume    = {6},
195	  number    = {3},
196	  year      = {2023},
197	  doi       = {10.1177/25152459231162567},
198	}
199	
200	@article{simonsohn2020specification,
201	  title     = {Specification curve analysis},
202	  author    = {Simonsohn, Uri and Simmons, Joseph P. and Nelson, Leif D.},
203	  journal   = {Nature Human Behaviour},
204	  volume    = {4},
205	  number    = {11},
206	  pages     = {1208--1214},
207	  year      = {2020},
208	  doi       = {10.1038/s41562-020-0912-z},
209	}
210	
211	@article{schaeffer2025position,
212	  title     = {Position: Model Collapse Does Not Mean What You Think},
213	  author    = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},
214	  journal   = {arXiv preprint arXiv:2503.03150},
215	  year      = {2025},
216	  url       = {https://arxiv.org/abs/2503.03150},
217	}
218	
219	% ============================================================
220	% METHODOLOGY (GRANGER / LEAD-LAG)
221	% ============================================================
222	
223	@article{granger1969investigating,
224	  author    = {Granger, Clive W. J.},
225	  title     = {Investigating Causal Relations by Econometric Models and Cross-spectral Methods},
226	  journal   = {Econometrica},
227	  volume    = {37},
228	  number    = {3},
229	  pages     = {424--438},
230	  year      = {1969},
231	  publisher = {Wiley},
232	}
233	
234	@article{shojaie2022granger,
235	  title     = {{Granger} Causality: A Review and Recent Advances},
236	  author    = {Shojaie, Ali and Fox, Emily B.},
237	  journal   = {Annual Review of Statistics and Its Application},
238	  year      = {2022},
239	  url       = {https://arxiv.org/abs/2105.02675},
240	}
241	
242	@article{marcinkevics2022neural,
243	  title     = {{Granger} Causality Using Neural Networks},
244	  author    = {Marcinkevics, Raphael and Vogt, Julia},
245	  journal   = {arXiv preprint arXiv:2208.03703},
246	  year      = {2022},
247	  url       = {https://arxiv.org/abs/2208.03703},
248	}
249	
250	@article{granger1974spurious,
251	  title     = {Spurious Regressions in Econometrics},
252	  author    = {Granger, Clive W. J. and Newbold, Paul},
253	  journal   = {Journal of Econometrics},
254	  volume    = {2},
255	  number    = {2},
256	  pages     = {111--120},
257	  year      = {1974},
258	  doi       = {10.1016/0304-4076(74)90034-7},
259	}
260	
261	@article{toda1995statistical,
262	  title     = {Statistical Inference in Vector Autoregressions with Possibly Integrated Processes},
263	  author    = {Toda, Hiro Y. and Yamamoto, Taku},
264	  journal   = {Journal of Econometrics},
265	  volume    = {66},
266	  number    = {1--2},
267	  pages     = {225--250},
268	  year      = {1995},
269	  doi       = {10.1016/0304-4076(94)01616-8},
270	}
271	
272	@article{page1954continuous,
273	  title     = {Continuous Inspection Schemes},
274	  author    = {Page, E. S.},
275	  journal   = {Biometrika},
276	  volume    = {41},
277	  number    = {1--2},
278	  pages     = {100--115},
279	  year      = {1954},
280	  doi       = {10.1093/biomet/41.1-2.100},
281	}
282	
283	% ============================================================
284	% EARLY WARNING SIGNALS / TIPPING POINTS (ECOLOGICAL THEORY)
285	% ============================================================
286	
287	@article{scheffer2009early,
288	  title     = {Early-warning signals for critical transitions},
289	  author    = {Scheffer, Marten and Bascompte, Jordi and Brock, William A. and Brovkin, Victor and Carpenter, Stephen R. and Dakos, Vasilis and Held, Hermann and van Nes, Egbert H. and Rietkerk, Max and Sugihara, George},
290	  journal   = {Nature},
291	  year      = {2009},
292	  doi       = {10.1038/nature08227},
293	}
294	
295	
296	@article{boettiger2012limits,
297	  title     = {Quantifying Limits to Detection of Early Warning for Critical Transitions},
298	  author    = {Boettiger, Carl and Hastings, Alan},
299	  journal   = {Journal of the Royal Society Interface},
300	  year      = {2012},
301	  doi       = {10.1098/rsif.2012.0125},
302	}
303	
304	@article{dakos2012methods,
305	  title     = {Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data},
306	  author    = {Dakos, Vasilis and Carpenter, Stephen R. and Brock, William A. and Ellison, Aaron M. and Guttal, Vishwesha and Ives, Anthony R. and K\'{e}fi, Sonia and Livina, Vasilis and Seekell, David A. and van Nes, Egbert H. and Scheffer, Marten},
307	  journal   = {PLoS ONE},
308	  year      = {2012},
309	  volume    = {7},
310	  number    = {7},
311	  pages     = {e41010},
312	  doi       = {10.1371/journal.pone.0041010},
313	}
314	
315	@inproceedings{gu2024cmr,
316	  title     = {{CMR} Scaling Law: Predicting Critical Mixture Ratios for Continual Pre-training of Language Models},
317	  author    = {Gu, Jiawei and Yang, Zacc and Ding, Chuanghao and Zhao, Rui and Tan, Fei},
318	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
319	  year      = {2024},
320	  url       = {https://arxiv.org/abs/2407.17467},
321	}
322	
323	@inproceedings{gu2025datamixing,
324	  title     = {Data Mixing Can Induce Phase Transitions in Knowledge Acquisition},
325	  author    = {Gu, Xinran and Liang, Hayden and Pehlevan, Cengiz},
326	  booktitle = {Advances in Neural Information Processing Systems},
327	  year      = {2025},
328	  note      = {Spotlight},
329	  url       = {https://arxiv.org/abs/2505.18091},
330	}
331	
332	@article{calabrese2003hormesis,
333	  title     = {Toxicology Rethinks Its Central Belief},
334	  author    = {Calabrese, Edward J. and Baldwin, Linda A.},
335	  journal   = {Nature},
336	  year      = {2003},
337	  volume    = {421},
338	  number    = {6924},
339	  pages     = {691--692},
340	  doi       = {10.1038/421691a},
341	}
342	
343	% ============================================================
344	% MODELS
345	% ============================================================
346	
347	@inproceedings{biderman2023pythia,
348	  title     = {Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling},
349	  author    = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purber, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and van der Wal, Oskar},
350	  booktitle = {International Conference on Machine Learning},
351	  year      = {2023},
352	  url       = {https://arxiv.org/abs/2304.01373},
353	}
354	
355	% ============================================================
356	% DATASETS
357	% ============================================================
358	
359	@inproceedings{merity2017pointer,
360	  title     = {Pointer Sentinel Mixture Models},
361	  author    = {Merity, Stephen and Xiong, Caiming and Bradbury, James and Socher, Richard},
362	  booktitle = {International Conference on Learning Representations},
363	  year      = {2017},
364	  url       = {https://arxiv.org/abs/1609.07843},
365	}
366	
367	% ============================================================
368	% STATISTICAL METHODOLOGY
369	% ============================================================
370	
371	@article{schreiber2000measuring,
372	  title     = {Measuring Information Transfer},
373	  author    = {Schreiber, Thomas},
374	  journal   = {Physical Review Letters},
375	  volume    = {85},
376	  number    = {2},
377	  pages     = {461--464},
378	  year      = {2000},
379	}
380	
381	@article{phipson2010permutation,
382	  title     = {Permutation P-values Should Never Be Zero: Calculating Exact P-values When Permutations Are Randomly Drawn},
383	  author    = {Phipson, Belinda and Smyth, Gordon K.},
384	  journal   = {Statistical Applications in Genetics and Molecular Biology},
385	  volume    = {9},
386	  number    = {1},
387	  pages     = {Article 39},
388	  year      = {2010},
389	  doi       = {10.2202/1544-6115.1585},
390	}
391	
392	@article{truong2026phase,
393	  title     = {On the Phase Transition of Model Collapse in Iterative Training},
394	  author    = {Truong, Lan V. and Truong, Nhan},
395	  journal   = {arXiv preprint arXiv:2512.12381},
396	  year      = {2026},
397	}
398	
399	@article{benjamini2001control,
400	  title     = {The Control of the False Discovery Rate in Multiple Testing under Dependency},
401	  author    = {Benjamini, Yoav and Yekutieli, Daniel},
402	  journal   = {Annals of Statistics},
403	  volume    = {29},
404	  number    = {4},
405	  pages     = {1165--1188},
406	  year      = {2001},
407	}
408	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a0e356ab-5fde-40cb-9cb4-59c70a849c9c",
  "isSidechain": true,
  "promptId": "52a92da4-9638-4bcf-884f-bc5fb5f5990b",
  "agentId": "a383bcd948b1952d6",
  "type": "user",
  "uuid": "b158f5d5-5916-46f2-8a60-9af27a039bf6",
  "sourceToolAssistantUUID": "a0e356ab-5fde-40cb-9cb4-59c70a849c9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-22T10:01:04.213Z_

<details><summary>↩ Tool result · reported error · `toolu_01Qq8BxUZuRXmKYeLA9VLDeH`</summary>

```text
File content (27284 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "689cf190-f924-4516-9c99-7b66cfd749e6",
  "isSidechain": true,
  "promptId": "52a92da4-9638-4bcf-884f-bc5fb5f5990b",
  "agentId": "a383bcd948b1952d6",
  "type": "user",
  "uuid": "febb2feb-f1b4-4df4-a688-2ff0d2d6f601",
  "toolUseResult": "Error: File content (27284 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "689cf190-f924-4516-9c99-7b66cfd749e6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-22T10:01:10.924Z_

Now let me read the appendix file with specific portions since it's too large:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "febb2feb-f1b4-4df4-a688-2ff0d2d6f601",
  "isSidechain": true,
  "agentId": "a383bcd948b1952d6",
  "requestId": "req_011CbHQwiJvQbGSk2DhFZSN1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1e767de6-0908-4a04-83c1-b3eec85174f5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016oNhYT6qZBQdGqdGMyiWay",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6219,
      "cache_creation_input_tokens": 3167,
      "cache_read_input_tokens": 17432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3167,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 17 · 2026-05-22T10:01:11.862Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01W7bLYjAiHBXDxDzXfFq3JK`</summary>

```json
{
  "command": "grep -n \"specification curve\\|SCA\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e767de6-0908-4a04-83c1-b3eec85174f5",
  "isSidechain": true,
  "agentId": "a383bcd948b1952d6",
  "requestId": "req_011CbHQwiJvQbGSk2DhFZSN1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d0ff7f2e-9c72-4902-af1d-cc599318b119",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016oNhYT6qZBQdGqdGMyiWay",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6219,
      "cache_creation_input_tokens": 3167,
      "cache_read_input_tokens": 17432,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3167
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6219,
          "output_tokens": 118,
          "cache_read_input_tokens": 17432,
          "cache_creation_input_tokens": 3167,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3167,
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

_source line 18 · 2026-05-22T10:01:11.927Z_

<details><summary>↩ Tool result · `toolu_01W7bLYjAiHBXDxDzXfFq3JK`</summary>

```text
165:We assess robustness via specification curve analysis~\cite{simonsohn2020specification}, systematically varying analytical degrees of freedom to test whether the 0/8$\to$6/8 transition is specification-invariant.
166:Our specification curve varies data subsets and pair selections while holding the detection method (PermG) and its hyperparameters fixed, more closely resembling a systematic subset analysis than a full specification curve in the sense of \citet{simonsohn2020specification}.
191:The specification curve confirms that the sharp detection onset is not an artifact of particular analytical choices: the categorical jump from 0\% to ${\geq}75\%$ significance at $\alpha_c{\approx}0.50$ holds across the vast majority of specifications, supporting the main text claim (\S\ref{sec:regime}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0ff7f2e-9c72-4902-af1d-cc599318b119",
  "isSidechain": true,
  "promptId": "52a92da4-9638-4bcf-884f-bc5fb5f5990b",
  "agentId": "a383bcd948b1952d6",
  "type": "user",
  "uuid": "7cc07d03-e78c-47eb-8974-0d15bd213bef",
  "sourceToolAssistantUUID": "d0ff7f2e-9c72-4902-af1d-cc599318b119",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-22T10:01:13.798Z_

Now let me read the relevant sections of the appendix more carefully:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cc07d03-e78c-47eb-8974-0d15bd213bef",
  "isSidechain": true,
  "agentId": "a383bcd948b1952d6",
  "requestId": "req_011CbHQxHGZ4DF2RXoakhMMy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d181ed86-9f40-4c4f-a1e2-a311eaac0f20",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01A6eRMT25VnWkBi6B8VeYn5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6532,
      "cache_read_input_tokens": 20599,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6532,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 20 · 2026-05-22T10:01:14.432Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LfjLynS3sP4vuC7CV4iLMR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 160,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d181ed86-9f40-4c4f-a1e2-a311eaac0f20",
  "isSidechain": true,
  "agentId": "a383bcd948b1952d6",
  "requestId": "req_011CbHQxHGZ4DF2RXoakhMMy",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c6c4aa01-e026-43b7-aa50-7c708bbfef99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01A6eRMT25VnWkBi6B8VeYn5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6532,
      "cache_read_input_tokens": 20599,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6532
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 139,
          "cache_read_input_tokens": 20599,
          "cache_creation_input_tokens": 6532,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6532,
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

_source line 21 · 2026-05-22T10:01:14.439Z_

<details><summary>↩ Tool result · `toolu_01LfjLynS3sP4vuC7CV4iLMR`</summary>

```text
160	
161	\section{Systematic Robustness Analysis}
162	\label{app:spec_curve}
163	
164	The sharp detection onset reported in \S\ref{sec:regime} could in principle depend on specific analytical choices (pair selection, seed, $\alpha$ level, method parameters).
165	We assess robustness via specification curve analysis~\cite{simonsohn2020specification}, systematically varying analytical degrees of freedom to test whether the 0/8$\to$6/8 transition is specification-invariant.
166	Our specification curve varies data subsets and pair selections while holding the detection method (PermG) and its hyperparameters fixed, more closely resembling a systematic subset analysis than a full specification curve in the sense of \citet{simonsohn2020specification}.
167	
168	We construct 1{,}160 analytical specifications from the combinatorial space of: 13 contamination levels ($\alpha$ grid), seed selection ($\{42, 43, 44, 45\}$ where available), 8 canonical canary$\to$downstream pairs (\{token entropy, ECE\} $\times$ \{distinct-1, distinct-2, distinct-3, mauve\}), and method parameters (all PermG with $n_\text{perm}{=}5{,}000$, BH FDR $q{=}0.05$).
169	All specifications use the D120-canonical analysis pipeline with $3\sigma$ threshold calibration (D105) as a hard filter.
170	
171	\begin{table}[h]
172	\centering
173	\small
174	\caption{Specification curve summary (1{,}160 specifications, D120-compliant). The blind$\to$onset jump is robust across specifications: 0\% significance rate through $\alpha{=}0.45$, rising to 75\% at $\alpha{=}0.50$.}
175	\label{tab:spec_curve}
176	\begin{tabular}{lc}
177	\toprule
178	Metric & Value \\
179	\midrule
180	Total specifications & 1{,}160 \\
181	Significant (FDR $q{<}0.05$) & 536 (46.2\%) \\
182	\midrule
183	\emph{By regime} & \\
184	\quad Blind ($\alpha \leq 0.45$) & 0\% \\
185	\quad Onset ($\alpha{=}0.50$) & 75\% \\
186	\quad Detection ($\alpha \geq 0.75$) & 62--75\% \\
187	\bottomrule
188	\end{tabular}
189	\end{table}
190	
191	The specification curve confirms that the sharp detection onset is not an artifact of particular analytical choices: the categorical jump from 0\% to ${\geq}75\%$ significance at $\alpha_c{\approx}0.50$ holds across the vast majority of specifications, supporting the main text claim (\S\ref{sec:regime}).
192	
193	
194	\section{Transfer Entropy Analysis}
195	\label{app:transfer_entropy}
196	
197	Table~\ref{tab:te_results} reports transfer entropy (TE; \citealp{schreiber2000measuring}) results aggregated across all baseline conditions.
198	TE was estimated using 3-bin discretization with permutation testing ($n{=}5{,}000$).
199	No pair reaches BH-corrected significance ($q{=}0.05$) in any condition, confirming that non-parametric information-theoretic methods lack detection power at $T{=}11$.
200	
201	\begin{table}[h]
202	\centering
203	\small
204	\caption{Transfer Entropy results (12 runs across all $\alpha$ levels). TE\textsubscript{fwd}: canary$\to$downstream; TE\textsubscript{rev}: downstream$\to$canary. Mean uncorrected permutation $p$-values ($n{=}5{,}000$). No pair reaches BH-corrected $q{<}0.05$ in any run.}
205	\label{tab:te_results}
206	\resizebox{\columnwidth}{!}{%
207	\begin{tabular}{llcccc}
208	\toprule
209	Canary & Downstream & TE\textsubscript{fwd} (mean) & $p$\textsubscript{fwd} (mean) & TE\textsubscript{rev} (mean) & $p$\textsubscript{rev} (mean) \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6c4aa01-e026-43b7-aa50-7c708bbfef99",
  "isSidechain": true,
  "promptId": "52a92da4-9638-4bcf-884f-bc5fb5f5990b",
  "agentId": "a383bcd948b1952d6",
  "type": "user",
  "uuid": "33dc816d-104f-4b9c-aa43-0b4f17b8d8a1",
  "sourceToolAssistantUUID": "c6c4aa01-e026-43b7-aa50-7c708bbfef99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-22T10:01:21.935Z_

Perfect. Now let me also search for any other mentions of "Schaeffer" in the files I haven't fully reviewed yet:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33dc816d-104f-4b9c-aa43-0b4f17b8d8a1",
  "isSidechain": true,
  "agentId": "a383bcd948b1952d6",
  "requestId": "req_011CbHQxUK5X32Hdk3yfRMzt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2e94c73a-2aca-4160-b3e1-19029fb99d16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01J4zZ1KvimdJBVsMzh4cwTE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 27131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1302,
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

_source line 23 · 2026-05-22T10:01:22.777Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DAfDXAYk4VNtB2kueV9zy8`</summary>

```json
{
  "command": "grep -n \"Schaeffer\\|scheffer\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e94c73a-2aca-4160-b3e1-19029fb99d16",
  "isSidechain": true,
  "agentId": "a383bcd948b1952d6",
  "requestId": "req_011CbHQxUK5X32Hdk3yfRMzt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6b54a14a-e380-484b-993f-08cb151f1805",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01J4zZ1KvimdJBVsMzh4cwTE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 27131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1302,
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

### Tool result

_source line 24 · 2026-05-22T10:01:22.839Z_

<details><summary>↩ Tool result · `toolu_01DAfDXAYk4VNtB2kueV9zy8`</summary>

```text
14:\citet{scheffer2009early} established that systems approaching tipping points exhibit generic early-warning signals (rising autocorrelation and variance); \citet{dakos2012methods} developed a practical toolkit for estimating such signals, while \citet{boettiger2012limits} quantified detection limits in short time series---directly relevant to iterative training where $T{=}5$--$20$.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6b54a14a-e380-484b-993f-08cb151f1805",
  "isSidechain": true,
  "promptId": "52a92da4-9638-4bcf-884f-bc5fb5f5990b",
  "agentId": "a383bcd948b1952d6",
  "type": "user",
  "uuid": "9e372a7e-8b2c-46ce-ade3-8781584b3eed",
  "sourceToolAssistantUUID": "6b54a14a-e380-484b-993f-08cb151f1805",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T10:01:23.912Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01T5C7P2JRcxFXiehikxxaZL`</summary>

```json
{
  "command": "grep -n \"scheffer2009early\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e372a7e-8b2c-46ce-ade3-8781584b3eed",
  "isSidechain": true,
  "agentId": "a383bcd948b1952d6",
  "requestId": "req_011CbHQxUK5X32Hdk3yfRMzt",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dcb37fc8-917a-4ee0-9402-6cd4b0873470",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01J4zZ1KvimdJBVsMzh4cwTE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1302,
      "cache_read_input_tokens": 27131,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1302
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 214,
          "cache_read_input_tokens": 27131,
          "cache_creation_input_tokens": 1302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1302,
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

_source line 26 · 2026-05-22T10:01:23.990Z_

<details><summary>↩ Tool result · `toolu_01T5C7P2JRcxFXiehikxxaZL`</summary>

```text
287:@article{scheffer2009early,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dcb37fc8-917a-4ee0-9402-6cd4b0873470",
  "isSidechain": true,
  "promptId": "52a92da4-9638-4bcf-884f-bc5fb5f5990b",
  "agentId": "a383bcd948b1952d6",
  "type": "user",
  "uuid": "f05babca-2b7d-44bb-90c7-39ad37db4ab3",
  "sourceToolAssistantUUID": "dcb37fc8-917a-4ee0-9402-6cd4b0873470",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-22T10:01:28.314Z_

Let me get the full Scheffer citation:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f05babca-2b7d-44bb-90c7-39ad37db4ab3",
  "isSidechain": true,
  "agentId": "a383bcd948b1952d6",
  "requestId": "req_011CbHQyAtbwmxKJ25A9Aocu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "944dae18-b2bc-4694-8ef8-036dc5a4c80e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01S2C4qFUoFYnxqfLv3UUqyX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 377,
      "cache_read_input_tokens": 28433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 377,
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

_source line 28 · 2026-05-22T10:01:33.069Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AkXN3PmABstF6D53iHCf42`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/references.bib",
  "offset": 286,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "944dae18-b2bc-4694-8ef8-036dc5a4c80e",
  "isSidechain": true,
  "agentId": "a383bcd948b1952d6",
  "requestId": "req_011CbHQyAtbwmxKJ25A9Aocu",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "400566a6-7d83-4bb5-ba6b-565e702766bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01S2C4qFUoFYnxqfLv3UUqyX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 377,
      "cache_read_input_tokens": 28433,
      "output_tokens": 135,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 377
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 135,
          "cache_read_input_tokens": 28433,
          "cache_creation_input_tokens": 377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 377,
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

_source line 29 · 2026-05-22T10:01:33.078Z_

<details><summary>↩ Tool result · `toolu_01AkXN3PmABstF6D53iHCf42`</summary>

```text
286	
287	@article{scheffer2009early,
288	  title     = {Early-warning signals for critical transitions},
289	  author    = {Scheffer, Marten and Bascompte, Jordi and Brock, William A. and Brovkin, Victor and Carpenter, Stephen R. and Dakos, Vasilis and Held, Hermann and van Nes, Egbert H. and Rietkerk, Max and Sugihara, George},
290	  journal   = {Nature},
291	  year      = {2009},
292	  doi       = {10.1038/nature08227},
293	}
294	
295	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "400566a6-7d83-4bb5-ba6b-565e702766bd",
  "isSidechain": true,
  "promptId": "52a92da4-9638-4bcf-884f-bc5fb5f5990b",
  "agentId": "a383bcd948b1952d6",
  "type": "user",
  "uuid": "759343d4-356e-4bd5-bcaf-854f6ee98ddf",
  "sourceToolAssistantUUID": "400566a6-7d83-4bb5-ba6b-565e702766bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-22T10:02:37.869Z_

Perfect. Now let me compile my findings with all the exact text requested:

## Summary Report: Paper File Contents

### 1. **related_work.tex** - FULL CONTENTS

```
\section{Related Work}
\label{sec:related_work}

\paragraph{Model collapse and canary metrics.}
Iterative training collapse was formalized by \citet{shumailov2024curse} and \citet{alemohammad2024mad}, who showed that recursively replacing real data with model-generated text causes progressive tail erosion; \citet{schaeffer2025position} systematize eight distinct notions of ``collapse'' that this literature conflates.
Theoretical analyses have sharpened these results: \citet{dohmatob2024tale} recast collapse as a change in scaling-law exponents, \citet{dohmatob2025strong} proved that collapse can occur even at vanishingly small synthetic fractions, \citet{seddik2025statistical} provide a statistical analysis of iterative contamination dynamics, and \citet{marchi2025challenging} challenge the universality of collapse under diverse training conditions.
Several works have proposed monitoring metrics: \citet{du2026geometric} observe that calibration error rises before accuracy degrades, \citet{du2025scales} report ECE increases at 30\% contamination before accuracy drops, \citet{gambetta2024surplexity} introduces surplexity as a collapse detector, and \citet{drayson2025detection} show that machine-generated text detection can prevent collapse, and \citet{li2025verification} propose verification-based mitigation.
We differ from the closest predecessor, \citet{du2026geometric}, in four respects: (i)~we compare an entire family of canary metrics; (ii)~we cross-validate across five statistical methods; (iii)~we map detectability as a function of contamination regime; and (iv)~we treat method-selection sensitivity itself as a primary finding.

\paragraph{Data mixing phase transitions.}
\citet{kazdan2025collapse} map the conditions under which synthetic data triggers collapse versus improves performance, \citet{gu2024cmr} establish a scaling law for critical mixture ratios in continual pre-training, and \citet{gu2025datamixing} show that data mixing can induce phase transitions in knowledge acquisition---a direct theoretical analogue to our detection threshold, where a critical mixing ratio separates qualitatively different detection regimes.

\paragraph{Critical transitions and lead-lag methodology.}
\citet{scheffer2009early} established that systems approaching tipping points exhibit generic early-warning signals (rising autocorrelation and variance); \citet{dakos2012methods} developed a practical toolkit for estimating such signals, while \citet{boettiger2012limits} quantified detection limits in short time series---directly relevant to iterative training where $T{=}5$--$20$.
Crucially, \citet{truong2026phase} prove that entropy collapse in iterative training is a first-order (discontinuous) phase transition, structurally ruling out critical-slowing-down (CSD) early-warning signals.
Our ``detection onset'' is a \emph{statistical} threshold (PermG power crossing the detection threshold), not a thermodynamic phase transition, and our cascade ordering describes within-generation temporal ordering of metrics, not CSD-type precursors.
The standard framework for testing temporal precedence is Granger causality~\cite{granger1969investigating}, with neural extensions for nonlinear settings~\citep{marcinkevics2022neural}; however, non-stationary series inflate rejection rates~\cite{granger1974spurious}, and the Toda--Yamamoto procedure~\cite{toda1995statistical} addresses this at reduced degrees of freedom severe in short series.
These methods are largely absent from the model collapse literature.

\paragraph{Analytical robustness.}
\citet{bell2022modeling} introduced multiverse analysis to ML, \citet{coretta2023multidimensional} demonstrated that 46 teams reached different conclusions on identical data, and \citet{kapoor2024reforms} synthesized these concerns into a consensus checklist.
Our work applies this perspective to model collapse: five methods across multiple contamination regimes produce conclusions ranging from universal significance to complete null.
```

### 2. **references.bib** - EXACT CITATIONS FOR REQUESTED ENTRIES

**Du & Tanaka-Ishii (2026):**
```
@article{du2026geometric,
  title     = {Escaping Mode Collapse in {LLM} Generation via Geometric Regulation},
  author    = {Du, Xin and Tanaka-Ishii, Kumiko},
  journal   = {arXiv preprint arXiv:2605.00435},
  year      = {2026},
  url       = {https://arxiv.org/abs/2605.00435},
}
```

**Schaeffer et al. (2025):**
```
@inproceedings{schaeffer2025position,
  title     = {Position: Model Collapse Does Not Mean What You Think},
  author    = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},
  journal   = {arXiv preprint arXiv:2503.03150},
  year      = {2025},
  url       = {https://arxiv.org/abs/2503.03150},
}
```

**Scheffer et al. (2009) - Early-warning signals:**
```
@article{scheffer2009early,
  title     = {Early-warning signals for critical transitions},
  author    = {Scheffer, Marten and Bascompte, Jordi and Brock, William A. and Brovkin, Victor and Carpenter, Stephen R. and Dakos, Vasilis and Held, Hermann and van Nes, Egbert H. and Rietkerk, Max and Sugihara, George},
  journal   = {Nature},
  year      = {2009},
  doi       = {10.1038/nature08227},
}
```

### 3. **introduction.tex** - CONTRIBUTIONS LIST (EXACT TEXT)

```
Our contributions are:
\begin{enumerate}
    \item \textbf{Detectability landscape characterization} (\S\ref{sec:regime}--\ref{sec:intervention}).
    PermG establishes a monotonically decreasing detection boundary $\alpha_c(T) = A \cdot T^{-1/(2\beta)}$ from a sub-linear signal model (Proposition~\ref{prop:phase-boundary}; $\beta{=}0.24$, $\gamma{=}2.08$, cross-$T$ validated MAE${=}0.106$); since $\alpha_\infty{\approx}0$, any nonzero contamination produces signal, but sub-linear growth makes detection a function of $T$.
    Predict-then-verify at $T{=}20$ matches 3/5 predictions in saturated regimes, with systematic conservative bias at boundary $\alpha$ (Appendix~\ref{app:t20_prediction_timeline}); canary-triggered cessation reduces peak perplexity by 58\%.

    \item \textbf{Formal motivation for canary metric selection} (\S\ref{sec:cascade}).
    Under mode amplification, entropy Granger-precedes diversity (Proposition~\ref{thm:entropy_leads}), with a ${\geq}1$-generation lag (Proposition~\ref{prop:div_lag}), confirmed in 14/15 experiments ($\alpha \geq 0.30$; GPT-2-medium s43 bidirectional).

    \item \textbf{Method sensitivity as a primary finding} (\S\ref{sec:mmct}--\ref{sec:dose_response}).
    Five detection methods yield null-control FPR from 0\% to 92\%; the same Granger test shifts from 0/8 to 6/8 within a 2-percentage-point interval.
    The detectability landscape one observes depends critically on the statistical method used to probe it.
\end{enumerate}
```

### 4. **discussion.tex** - FULL CONTENTS

```
\section{Discussion and Conclusion}\label{sec:discussion}

\paragraph{Granger precedence is not causation.}
Our claim is scoped to temporal predictive improvement~\cite{granger1969investigating,shojaie2022granger}; bivariate tests cannot exclude confounders.
$\alpha_c(T)$ decreases monotonically ($\gamma{=}2.08$, cross-$T$ MAE${=}0.106$); predict-then-verify shows systematic conservative bias, and MAUVE floor saturation limits detection to $6/8$.
The non-monotonic dip at $\alpha{=}0.60$ dissolves by $T{=}25$ ($5/8$), validating $\sqrt{T}$ scaling; entropy is a one-generation canary (14/15 cascade, $-$58\% perplexity).
```

### 5. **appendix.tex** - SPECIFICATION CURVE ANALYSIS & SCA MENTIONS

**Section: Systematic Robustness Analysis (lines 161-191):**

```
\section{Systematic Robustness Analysis}
\label{app:spec_curve}

The sharp detection onset reported in \S\ref{sec:regime} could in principle depend on specific analytical choices (pair selection, seed, $\alpha$ level, method parameters).
We assess robustness via specification curve analysis~\cite{simonsohn2020specification}, systematically varying analytical degrees of freedom to test whether the 0/8$\to$6/8 transition is specification-invariant.
Our specification curve varies data subsets and pair selections while holding the detection method (PermG) and its hyperparameters fixed, more closely resembling a systematic subset analysis than a full specification curve in the sense of \citet{simonsohn2020specification}.

We construct 1{,}160 analytical specifications from the combinatorial space of: 13 contamination levels ($\alpha$ grid), seed selection ($\{42, 43, 44, 45\}$ where available), 8 canonical canary$\to$downstream pairs (\{token entropy, ECE\} $\times$ \{distinct-1, distinct-2, distinct-3, mauve\}), and method parameters (all PermG with $n_\text{perm}{=}5{,}000$, BH FDR $q{=}0.05$).
All specifications use the D120-canonical analysis pipeline with $3\sigma$ threshold calibration (D105) as a hard filter.

[Table 171-189 omitted for brevity - shows specification curve summary with 1,160 specifications, 0% significance in blind regime ≤0.45, rising to 75% at α=0.50]

The specification curve confirms that the sharp detection onset is not an artifact of particular analytical choices: the categorical jump from 0\% to ${\geq}75\%$ significance at $\alpha_c{\approx}0.50$ holds across the vast majority of specifications, supporting the main text claim (\S\ref{sec:regime}).
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "759343d4-356e-4bd5-bcaf-854f6ee98ddf",
  "isSidechain": true,
  "agentId": "a383bcd948b1952d6",
  "requestId": "req_011CbHQyqs9UsiKVCGzH441T",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aae9829f-870c-47dd-94a8-3a3e1cfce3ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/review_reviewer_1_ec2e4c4e",
  "sessionId": "975870e7-f393-4989-8d8c-e2b093dae357",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017HQA9eh6AS44caWeyYooQS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 312,
      "cache_read_input_tokens": 28810,
      "output_tokens": 2709,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 312
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 2709,
          "cache_read_input_tokens": 28810,
          "cache_creation_input_tokens": 312,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 312,
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
