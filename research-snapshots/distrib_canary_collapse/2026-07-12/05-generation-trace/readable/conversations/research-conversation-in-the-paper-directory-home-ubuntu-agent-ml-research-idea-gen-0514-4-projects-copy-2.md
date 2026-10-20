# Research conversation: In the paper directory /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/, fin

**Characterizing the Detectability Landscape of Iterative Model Collapse (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ad999017524d4cdd1.jsonl`
- **Structured JSON:** [`0569e15d417f6da01448.json`](../../sessions/05/0569e15d417f6da01448.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-24T15:56:49.685Z_

In the paper directory /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/, find the LaTeX context (captions + surrounding text references) for all figures. Read from introduction.tex, method.tex, experiments.tex, and appendix.tex. For each figure, extract:
1. The \includegraphics path
2. The \caption text
3. Any \label
4. Any nearby \ref mentions in the text

Return a concise summary of each figure's narrative intent based on the caption.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ec5ba50c-898a-489d-8777-d0a519cbb553",
  "agentId": "ad999017524d4cdd1",
  "type": "user",
  "uuid": "2253d9ec-9313-45fb-810b-e8c2e278f5c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-24T15:56:51.321Z_

I'll systematically search through the LaTeX files to extract figure information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2253d9ec-9313-45fb-810b-e8c2e278f5c0",
  "isSidechain": true,
  "agentId": "ad999017524d4cdd1",
  "requestId": "req_011CbMfh1eYuEm3Fe9RiH6DP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7b8617d1-e6c1-44f5-8627-f40def7efbfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0136o91XsW7F4ySdUiUnriaT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35740,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 35740,
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

_source line 3 · 2026-05-24T15:56:51.560Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01EC2nLVCVQaGFGs4W8u9spi`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/ -name \"*.tex\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b8617d1-e6c1-44f5-8627-f40def7efbfc",
  "isSidechain": true,
  "agentId": "ad999017524d4cdd1",
  "requestId": "req_011CbMfh1eYuEm3Fe9RiH6DP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6a6465e6-9e50-4904-8dae-28b0791dcb7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0136o91XsW7F4ySdUiUnriaT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 35740,
      "cache_read_input_tokens": 0,
      "output_tokens": 111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 35740
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 111,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 35740,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 35740,
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

_source line 4 · 2026-05-24T15:56:51.627Z_

<details><summary>↩ Tool result · `toolu_01EC2nLVCVQaGFGs4W8u9spi`</summary>

```text
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
  "parentUuid": "6a6465e6-9e50-4904-8dae-28b0791dcb7e",
  "isSidechain": true,
  "promptId": "ec5ba50c-898a-489d-8777-d0a519cbb553",
  "agentId": "ad999017524d4cdd1",
  "type": "user",
  "uuid": "f0f657d8-1edd-48aa-8b03-af087ddc45e6",
  "sourceToolAssistantUUID": "6a6465e6-9e50-4904-8dae-28b0791dcb7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-24T15:56:54.218Z_

Now let me read the four requested files to extract figure information:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0f657d8-1edd-48aa-8b03-af087ddc45e6",
  "isSidechain": true,
  "agentId": "ad999017524d4cdd1",
  "requestId": "req_011CbMfhA1Lgqtdnn6YXXzkW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3c49018d-afec-43e8-af55-5a230e7b1d00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EAGPENAR2ehCSyagdqTUgH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1660,
      "cache_read_input_tokens": 35740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1660,
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

_source line 6 · 2026-05-24T15:56:54.666Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WHpmrBH6aREfVTiAjcoKYW`</summary>

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
  "parentUuid": "3c49018d-afec-43e8-af55-5a230e7b1d00",
  "isSidechain": true,
  "agentId": "ad999017524d4cdd1",
  "requestId": "req_011CbMfhA1Lgqtdnn6YXXzkW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ad57f848-2ccb-4a50-b2d1-d2dd1aa24f46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EAGPENAR2ehCSyagdqTUgH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1660,
      "cache_read_input_tokens": 35740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1660,
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

_source line 7 · 2026-05-24T15:56:54.677Z_

<details><summary>↩ Tool result · `toolu_01WHpmrBH6aREfVTiAjcoKYW`</summary>

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
12	We map this landscape on Pythia-410M~\cite{biderman2023pythia} across 13 contamination levels with multi-seed replication (Figure~\ref{fig:regime_map}), and find structured terrain rather than smooth degradation: detection is absent through $\alpha{=}0.45$, then jumps from 0/8 to 6/8 significant pairs within a 2-percentage-point interval, before a non-monotonic dip and eventual reliable detection above a power-law boundary $\alpha_c(T)$ (Eq.~\ref{eq:alpha-c-theory}).
13	Cross-architecture evaluation at $\alpha{=}1.0$ across five families (345M--6.9B) supports forward detection in 11/15 conditions, with four non-confirming cases isolating distinct failure modes (\S\ref{sec:generalization}).
14	A second finding is equally consequential: five statistical methods applied to identical data yield null-control false-positive rates from 3\% to 92\%, demonstrating that the landscape one observes depends critically on the method used to probe it.
15	Our canary claim\footnote{Granger precedence establishes temporal predictive improvement, not true causation~\cite{shojaie2022granger}; bivariate tests cannot exclude confounders.} is scoped to diversity metrics (distinct-$n$~\cite{li2016diversity}).
16	
17	Our contributions are:
18	\begin{enumerate}
19	    \item \textbf{We map the detectability landscape} of iterative model collapse (\S\ref{sec:regime}--\ref{sec:dose_response}).
20	    Detection is absent through $\alpha{=}0.45$, then jumps from 0/8 to 6/8 within 2 percentage points; a detection boundary consistent with power-law scaling $\alpha_c(T) \propto T^{-\gamma}$ ($\gamma \in [0.64, 2.08]$; Eq.~\ref{eq:alpha-c-theory}) organizes three confirmed regimes (blind, onset, detection) plus one unexplained non-monotonic anomaly.
21	
22	    \item \textbf{We document method sensitivity as a primary finding} (\S\ref{sec:mmct}).
23	    Five methods yield null-control FPR from 3\% to 92\% ($\kappa{=}0.185$); PermG, the lowest-FPR directional method (11.1\%, CI $[1.2\%, 30.4\%]$), is selected as the primary detector.
24	
25	    \item \textbf{We formalize cascade ordering for canary metric selection} (\S\ref{sec:cascade}).
26	    Under mode amplification, entropy responds before diversity by ${\geq}1$ generation (Design Principles~\ref{thm:entropy_leads}--\ref{prop:div_lag}), confirmed in 14/15 experiments ($\alpha \geq 0.30$; GPT-2-medium s43 bidirectional).
27	\end{enumerate}
28	
29	\begin{figure*}[t]
30	\centering
31	\includegraphics[width=0.55\textwidth]{figures/fig_phase_diagram.pdf}
32	\caption{Detection phase diagram (Pythia-410M, fp32, PermG direction-checked). Each cell shows the number of FDR-significant canary$\to$diversity pairs (of~8) at a given contamination strength~$\alpha$ and observation window~$T$. The dashed curve is the fitted detection boundary $\alpha_c(T) \propto T^{-\gamma}$ with $\gamma \in [0.64, 2.08]$ (profile 95\% CI; \S\ref{sec:theory}). Diamond markers ($\diamond$) flag a non-monotonic anomaly at $\alpha{=}0.60$ (0/8 at $T{\leq}20$); the star ($\star$) marks its dissolution at $T{=}25$ (5/8).}
33	\label{fig:regime_map}
34	\end{figure*}
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad57f848-2ccb-4a50-b2d1-d2dd1aa24f46",
  "isSidechain": true,
  "promptId": "ec5ba50c-898a-489d-8777-d0a519cbb553",
  "agentId": "ad999017524d4cdd1",
  "type": "user",
  "uuid": "a2cd18af-6c66-41ee-8b73-c02b6ad801c3",
  "sourceToolAssistantUUID": "ad57f848-2ccb-4a50-b2d1-d2dd1aa24f46",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-24T15:56:58.945Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JWMSjvuRsNo3TE2qtjsYrH`</summary>

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
  "parentUuid": "a2cd18af-6c66-41ee-8b73-c02b6ad801c3",
  "isSidechain": true,
  "agentId": "ad999017524d4cdd1",
  "requestId": "req_011CbMfhA1Lgqtdnn6YXXzkW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1482be45-e7fb-4c5c-a794-d2d16fc22cb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EAGPENAR2ehCSyagdqTUgH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1660,
      "cache_read_input_tokens": 35740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1660,
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

_source line 9 · 2026-05-24T15:56:58.953Z_

<details><summary>↩ Tool result · `toolu_01JWMSjvuRsNo3TE2qtjsYrH`</summary>

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
35	\begin{figure*}[t]
36	\centering
37	\includegraphics[width=\textwidth]{figures/fig_framework.pdf}
38	\caption{Analytical framework. (a)~Iterative contamination loop: each generation trains on an $\alpha$-fraction synthetic mixture, from which canary (entropy) and downstream (distinct-$n$) metrics are extracted. (b)~Multi-method consensus test (MMCT): five detection methods with varying FPR profiles converge to a $K{\geq}3$ majority vote; PermG is selected as the lowest-FPR directional method. (c)~Signal$\times$Resolution model: sub-linear signal $S(\alpha)$ and finite resolution $R(\alpha)$ produce three confirmed regimes (blind, onset, detection) plus a non-monotonic anomaly, with boundary $\alpha_c(T) \sim T^{-\gamma}$.}
39	\label{fig:framework}
40	\end{figure*}
41	
42	\subsection{Method Sensitivity Analysis}
43	\label{sec:mmct}
44	We compare five lead-lag detection methods in a multi-method comparison~\cite{simonsohn2020specification} (algorithm in Appendix~\ref{app:mmct}), calibrated against null-control ($\alpha{=}0.0$) data where any detection is a false positive.
45	PermG's empirical FPR of 11.1\% (CI $[1.2\%, 30.4\%]$; 6 null seeds) exceeds the nominal 5\% threshold; $K{\geq}3$ consensus yields 16.7\% FPR (6/36), driven primarily by high-FPR methods (PermG contributes to only 2/6 consensus false positives; Appendix~\ref{app:fpr_independence}).
46	The five methods are: naive cross-correlation, differenced cross-correlation (DiffXCorr), threshold onset, permutation Granger causality (PermG), and Toda--Yamamoto~\cite{toda1995statistical}.
47	Detection results use equal-weight majority voting ($K{\geq}3$ of 5 methods, each contributing one vote per pair) with forward-direction filtering; FPR-inverse weighting is used only in exploratory method ranking (Appendix~\ref{app:weight_robustness}).
48	Each method encodes different assumptions, and these differences produce dramatically different FPR profiles.
49	Pooled null-control FPR across six seeds (6-pair basis, 36 pairs): DiffXCorr 2.8\%, PermG 11.1\%, Threshold 27.8\%, Toda--Yamamoto 38.9\%, NaiveXCorr 91.7\% (Appendix~\ref{app:fpr_independence}).
50	We classify a method as \emph{directional} if its test structure inherently separates forward from reverse precedence (PermG tests each direction independently; threshold onset compares crossing order), rather than inferring direction post-hoc from peak lag sign (NaiveXCorr, DiffXCorr).
51	Although DiffXCorr achieves the lowest raw FPR (1/36, 2.8\%), it is bidirectional and cannot distinguish forward from reverse precedence, making it unsuitable as a standalone collapse detector.
52	PermG (4/36, 11.1\%; cluster-adjusted 95\% CI $[1.2\%, 30.4\%]$) is the lowest-FPR directional method with consistent detection at $\alpha \geq 0.50$ across all four weighting schemes (Shapley analysis: Appendix~\ref{app:shapley}).
53	Practitioner-facing alternatives (PPL-slope, variance thresholds) yield 67--100\% FPR under natural training drift (Appendix~\ref{app:naive_baselines}).
54	That method choice alone can shift conclusions from universal significance to complete null on identical data motivates reporting method sensitivity as a primary result rather than relegating it to a robustness check.
55	
56	\paragraph{Permutation Granger causality.}
57	PermG tests whether past values of canary metric $X$ improve prediction of downstream metric $Y$ beyond $Y$'s own history~\cite{shojaie2022granger}.
58	We use classical rather than neural Granger methods~\citep{tank2021neural} because $T{\leq}25$ provides insufficient observations for neural network parameter estimation, and apply 5{,}000 permutations~\citep{phipson2010permutation} on first-differenced series with Benjamini--Hochberg FDR correction at $q{=}0.05$ across 8 canary$\to$downstream pairs (2 canaries $\times$ 4 downstream metrics, sharing canary terms and thus positively dependent).
59	
60	The permutation null controls Type~I error exactly by construction; BH-FDR remains valid under positive regression dependence on a subset (PRDS)~\cite{benjamini2001control} (assumption discussed in Appendix~\ref{app:fpr_independence}).
61	Empirically, 4/36 null-control rejections across six seeds (11.1\%; cluster-adjusted 95\% CI $[1.2\%, 30.4\%]$, ICC${=}0.14$; Appendix~\ref{app:fpr_independence}) confirm adequate size control.
62	Simulation under non-stationary AR(1) DGP ($\varphi{=}0.95$--$0.99$) reveals potential FPR inflation to ${\sim}10\%$, but our empirical series exhibit low persistence (null token entropy $\varphi{=}-0.51$; first-differenced distinct-1 $\varphi{<}0.44$; Appendix~\ref{app:nonstationarity}).
63	PermG also retains ${\sim}80\%$ of raw-levels power at $T{=}11$ versus ${\sim}61\%$ for standard first-differencing, justifying the permutation approach at short series lengths (Appendices~\ref{app:robustness}, \ref{app:power_analysis}, \ref{app:transfer_entropy}).
64	
65	\subsection{Detection Boundary}
66	\label{sec:theory}
67	
68	We model the PermG detection rate as a $T$-dependent steep sigmoid, excluding the non-monotonic anomaly at $\alpha \in [0.55, 0.65]$:
69	\begin{equation}
70	\mathrm{rate}(\alpha, T) = \frac{0.70}{1 + \exp\!\bigl(-100\,(\alpha - \alpha_c(T))\bigr)},
71	\label{eq:joint-sigmoid}
72	\end{equation}
73	fitted to $T{=}10$ data ($n{=}11$, sync-dip excluded; $R^2{=}0.969$).
74	The detection boundary is consistent with power-law scaling in observation length:
75	\begin{equation}
76	\alpha_c(T) = A \cdot T^{-\gamma},
77	\label{eq:alpha-c}
78	\end{equation}
79	where the exponent $\gamma$ is determined by the sub-linear signal model below.
80	
81	\paragraph{Empirical observation (detection boundary).}\label{prop:phase-boundary}
82	Under an empirical sub-linear signal model $S(\alpha) = c \cdot \alpha^\beta$ with $\beta < 1$ (signal exponent, not statistical power), the detection boundary satisfies
83	\begin{equation}
84	\alpha_c(T) = A \cdot T^{-1/(2\beta)},
85	\label{eq:alpha-c-theory}
86	\end{equation}
87	where $A = (z^* \sigma / c)^{1/\beta}$ and $z^* = \Phi^{-1}(\pi^*)$ (justification in Appendix~\ref{app:alpha_c_proof}).
88	
89	\noindent The signal model $S(\alpha) = c\alpha^\beta$ is an empirical parametrization: $\beta$ is fitted from data rather than derived from training dynamics.
90	The power-law form $\alpha_c \propto T^{-1/(2\beta)}$ follows from signal-detection theory (signal-to-noise crossing a threshold), but $\beta$ requires architecture-specific calibration.
91	
92	Cross-$T$ validation (train $T{\in}\{10,20\}$, test $T{\in}\{5,15\}$) yields $\beta{=}0.24$, $\gamma{=}2.08$ (MAE${=}0.106$, CI $6/6$); leave-one-$T$-out CV on the full grid ($T{\in}\{5,10,15,20,25\}$, anomaly excluded) confirms predictive accuracy (MAE${=}0.037$, CI $15/15$; Appendix~\ref{app:alpha_c_proof}).
93	However, $\beta$ is poorly identified: the MLE center estimate $\hat{\beta}{=}0.66$ ($\gamma{\approx}0.76$) diverges from the cross-validation estimate $\beta{=}0.24$ ($\gamma{=}2.08$), with profile 95\% CI $\gamma \in [0.64, 2.08]$.
94	Under PermG's FPR uncertainty ($[1.2\%, 30.4\%]$), $\alpha_c$ estimates carry ${\pm}0.05$ uncertainty; statistical power at $T{\leq}8$ falls below 50\% (Appendix~\ref{app:power_analysis}), so reported boundaries at short $T$ are upper bounds.
95	The qualitative conclusion (detection improves with longer observation) is robust to the specific $\gamma$ value; the precise exponent is a descriptive parametrization rather than a mechanistic prediction.
96	
97	\paragraph{Shape comparison with smooth alternatives.}
98	The scaling exponent alone cannot distinguish smooth from steep-sigmoid boundaries: a concave signal model ($\beta'{=}0.5$) produces $\gamma'{=}1.87$, close to the observed $2.08$.
99	Formal shape testing on dense $T{=}10$ data (17~$\alpha$ values) favors a smooth sigmoid over a literal step function ($\Delta\mathrm{AIC}{=}-110$), but the fitted onset steepness ($k{=}15.7$, 95\% CI $[9.4, 28.2]$; \S\ref{sec:dose_response}) is $3$--$4{\times}$ higher than any smooth signal model predicts.
100	Power simulations confirm this gap: VAR(1) models (1{,}000 per cell; Appendix~\ref{app:power_sim}) produce sigmoids with $k{\approx}5$--$6$, yielding $k_{\mathrm{obs}} / k_{\mathrm{H0}} \approx 3$ (CI lower bound ratio ${\approx}2$), consistent with a genuine phase boundary rather than a gradual power artifact.
101	Since $\alpha_\infty{\approx}0$, any nonzero contamination produces signal ($S \propto \alpha^{0.24}$), but sub-linear growth makes detection a function of $T$.
102	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1482be45-e7fb-4c5c-a794-d2d16fc22cb2",
  "isSidechain": true,
  "promptId": "ec5ba50c-898a-489d-8777-d0a519cbb553",
  "agentId": "ad999017524d4cdd1",
  "type": "user",
  "uuid": "0d022789-cf6d-4d2b-b3ac-f9f971ff510b",
  "sourceToolAssistantUUID": "1482be45-e7fb-4c5c-a794-d2d16fc22cb2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-24T15:56:59.230Z_

<details open><summary>🔧 Tool call — Read · `toolu_015W4gwFFu3j3f1Enr1qj1py`</summary>

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
  "parentUuid": "0d022789-cf6d-4d2b-b3ac-f9f971ff510b",
  "isSidechain": true,
  "agentId": "ad999017524d4cdd1",
  "requestId": "req_011CbMfhA1Lgqtdnn6YXXzkW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f3f927f1-17d4-48b4-823a-78eca37dca2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EAGPENAR2ehCSyagdqTUgH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1660,
      "cache_read_input_tokens": 35740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1660,
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

_source line 11 · 2026-05-24T15:56:59.242Z_

<details><summary>↩ Tool result · `toolu_015W4gwFFu3j3f1Enr1qj1py`</summary>

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
26	Sigmoid regression on the 13-point $T{=}10$ grid yields $\alpha_c = 0.483 \pm 0.006$ ($R^2 = 0.969$; Figure~\ref{fig:dose_response}); dense $\alpha$ sampling (17~values) constrains onset steepness to $k{=}15.7$ (95\% CI $[9.4, 28.2]$), a steep but finite-width sigmoid ($\Delta\mathrm{AIC}{=}-110$ vs.\ step function; Appendix~\ref{app:sigmoid_shape}).
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
41	\begin{figure*}[t]
42	\centering
43	\includegraphics[width=0.55\textwidth]{figures/metric_trajectory.pdf}
44	\caption{Metric trajectories at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead across all four seeds (shaded: inter-seed range). This pattern corresponds to 24/24 forward and 0/24 reverse FDR-significant canary$\to$diversity pairs (6 per seed, mauve excluded).}
45	\label{fig:metric_trajectory}
46	\end{figure*}
47	
48	
49	\subsection{Dose-Response and Detection Regimes}
50	\label{sec:dose_response}
51	
52	\begin{figure}[t]
53	\centering
54	\includegraphics[width=\columnwidth,trim={0 0.4cm 0 0.4cm},clip]{figures/fig_dose_response.pdf}
55	\vspace{-6pt}
56	\caption{PermG dose-response profile (Pythia-410M, $T{=}10$, fp32). Sigmoid fit (shaded 95\% CI) yields $\alpha_c{=}0.483$. Three confirmed regimes: blind ($\alpha{\leq}0.45$, 0/8), onset ($\alpha{\approx}0.50$, 6/8), detection ($\alpha{\geq}0.75$); non-monotonic anomaly at $\alpha{=}0.60$ (0/8) (out of 8 canary$\to$downstream pairs).}
57	\label{fig:dose_response}
58	\end{figure}
59	
60	The PermG dose-response profile (Figure~\ref{fig:dose_response}; full per-method table in Appendix~\ref{app:dose_response}) reveals three confirmed detection regimes---\emph{blind} ($\alpha \leq 0.45$, 0/8 FDR-significant pairs), \emph{onset} ($\alpha \approx 0.50$, 6/8), and \emph{detection} ($\alpha{\geq}0.75$, 6/8 across 4~seeds at $\alpha{=}1.0$)---plus a non-monotonic anomaly at $\alpha \approx 0.60$ (0/8) whose mechanism remains unexplained.
61	At $\alpha{=}0.55$, PermG returns 0/8 FDR-significant pairs despite marginal $p$-values ($p_{\mathrm{fdr}}{=}0.062$--$0.092$); differenced cross-correlation detects 8/8 bidirectionally at this level, confirming that a lead-lag signal exists but falls below PermG's directional detection threshold.
62	At $\alpha{=}0.60$, PermG returns $0/8$ at $T{\leq}20$ but recovers to $5/8$ at $T{=}25$, consistent with $\sqrt{T}$ power scaling (Appendix~\ref{app:t20_comparison}).
63	Notably, $K{\geq}3$ consensus detects 8/8 at $\alpha{=}0.60$, suggesting that the non-monotonic anomaly is PermG-specific rather than a property of the underlying landscape; other methods see through it where PermG's directional test loses power.
64	
65	Method choice is itself a major source of variability: at $\alpha{=}1.0$, direction-checked forward significance spans 0\% to 75\% (Figure~\ref{fig:method_comparison}), with $\kappa{=}0.185$; a specification curve (18~variants; Appendix~\ref{app:spec_curve}) confirms onset invariance.
66	Task degradation corroborates: perplexity jumps $+31\%$ between $\alpha{=}0.50$ and $0.52$ (Appendix~\ref{app:task_degradation}).
67	
68	
69	\begin{figure}[t]
70	\centering
71	\includegraphics[width=\columnwidth]{figures/fig_method_comparison.pdf}
72	\caption{Method sensitivity: FDR-significant forward pairs (\%) across contamination levels (Pythia-410M, seed~42, fp32). PermG (dark blue) achieves 0\% null-control FPR with stable 75\% detection at $\alpha \geq 0.50$. Dashed line: 5\% nominal. Full table in Appendix~\ref{app:dose_response}.}
73	\label{fig:method_comparison}
74	\end{figure}
75	
76	
77	\subsection{Detection Boundary Left-Shift}
78	\label{sec:t20}
79	
80	Longer observation windows push the detection boundary to lower contamination levels: $\alpha_c(5){\geq}1.0$, $\alpha_c(10){=}0.487$, consistent with power-law scaling (\S\ref{sec:theory}).
81	The $\alpha{=}0.45$ column validates this left-shift: undetectable at $T{\leq}10$ (0/8), it crosses into reliable detection at $T{=}15$ (6/8, dual-seed) and remains there at $T{=}20$ and $T{=}25$.
82	Cross-seed replication shows PermG within ${\pm}1$, though boundary cells exhibit sensitivity ($[0, 6]/8$ at $T{=}10$, $\alpha{=}0.50$).
83	The $\alpha{=}0.60$ anomaly dissolves by $T{=}25$ ($5/8$), consistent with $\sqrt{T}$ power scaling; predict-then-verify yields 2/4 boundary predictions within CI (Appendix~\ref{app:t20_prediction_timeline}).
84	
85	
86	\subsection{Cross-Architecture Validation}
87	\label{sec:generalization}
88	
89	To test whether the phase-diagram structure is Pythia-specific, we evaluate PermG at $\alpha{=}1.0$ across 15 model-seed combinations spanning five families, scales 345M--6.9B, and two domains (Table~\ref{tab:generalization}).
90	Forward detection reaches ${\geq}6/8$ in 11/15 conditions, confirming that PermG generalizes to architectures satisfying the monotonic entropy decline assumption (Design Principle~\ref{thm:entropy_leads}).
91	Domain matters: C4 yields the strongest detection (Pythia-1.4B: 2/8 WikiText $\to$ 8/8 C4), suggesting that domain-specific mode structure affects detectability.
92	The four non-confirming conditions each isolate a distinct failure mode: precision sensitivity (GPT-2 bf16: 0/8 vs fp32: 6/8), bidirectional confounding (GPT-2 s43), seed dependence (Pythia-1.4B: s42 2/8, s43 6/8), and entropy decoupling (SmolLM3-3B: 3/8, whose non-monotonic entropy violates Design Principle~\ref{thm:entropy_leads}).
93	
94	\paragraph{FPR caveat.}
95	GPT-2-medium null-control (s42) yields 6/6 PermG forward false positives, an architecture-specific FPR inflation likely driven by its non-standard weight initialization.
96	While $K{\geq}3$ consensus returns 0/6 on GPT-2 null specifically, its overall FPR on Pythia-410M is 16.7\% (6/36; \S\ref{sec:mmct})---higher than standalone PermG---so consensus serves as a robustness mechanism against single-method anomalies rather than a general FPR safety net.
97	Standalone PermG claims require architecture-specific null calibration.
98	
99	Full results are in Table~\ref{tab:generalization} (Appendix~\ref{app:cross_arch_table}).
100	
101	
102	\subsection{Canary-Based Intervention (Proof of Concept)}
103	\label{sec:intervention}
104	
105	As an illustrative proof-of-concept under favorable conditions ($\alpha{=}1.0$, full replacement), we implement predictive cessation: training switches to pure real data when token entropy drops ${>}15\%$ from generation~0.
106	The 15\% threshold was selected post-hoc (robust band $[10\%, 22\%]$, zero false alarms; Appendix~\ref{app:intervention_sensitivity}).
107	The predictive trigger fires at generation~1 (one generation before a reactive distinct-1 baseline), reducing peak perplexity by 64\% ($56.99$ vs.\ $157.09$; Figure~\ref{fig:intervention}) in both Pythia-410M and 1.4B.
108	This single-setting demonstration ($N{=}2$ architectures, $\alpha{=}1.0$, post-hoc threshold) is not rigorously evaluated (CUSUM comparison: Appendix~\ref{app:csmp}).
109	
110	\begin{figure}[t]
111	\centering
112	\includegraphics[width=\columnwidth]{figures/fig_intervention.pdf}
113	\caption{Canary-triggered intervention (Pythia-410M, $\alpha{=}1.0$). Predictive cessation on entropy (generation~1) reduces peak perplexity by 64\% versus reactive triggering on distinct-1 (generation~2).}
114	\label{fig:intervention}
115	\end{figure}
116	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3f927f1-17d4-48b4-823a-78eca37dca2a",
  "isSidechain": true,
  "promptId": "ec5ba50c-898a-489d-8777-d0a519cbb553",
  "agentId": "ad999017524d4cdd1",
  "type": "user",
  "uuid": "455ac52c-9ef0-47ef-9f6e-88ac42600652",
  "sourceToolAssistantUUID": "f3f927f1-17d4-48b4-823a-78eca37dca2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-24T15:56:59.772Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BPrewc8kkSoZwFqWtdEebG`</summary>

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
  "parentUuid": "455ac52c-9ef0-47ef-9f6e-88ac42600652",
  "isSidechain": true,
  "agentId": "ad999017524d4cdd1",
  "requestId": "req_011CbMfhA1Lgqtdnn6YXXzkW",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "324ffdd3-7a09-4e3d-a9e4-c3cede4543b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EAGPENAR2ehCSyagdqTUgH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1660,
      "cache_read_input_tokens": 35740,
      "output_tokens": 320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1660
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 320,
          "cache_read_input_tokens": 35740,
          "cache_creation_input_tokens": 1660,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1660,
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

_source line 13 · 2026-05-24T15:57:00.041Z_

<details><summary>↩ Tool result · reported error · `toolu_01BPrewc8kkSoZwFqWtdEebG`</summary>

```text
File content (37404 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "324ffdd3-7a09-4e3d-a9e4-c3cede4543b4",
  "isSidechain": true,
  "promptId": "ec5ba50c-898a-489d-8777-d0a519cbb553",
  "agentId": "ad999017524d4cdd1",
  "type": "user",
  "uuid": "e359d9d6-52a6-4fe9-9799-18b2c88526d9",
  "toolUseResult": "Error: File content (37404 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "324ffdd3-7a09-4e3d-a9e4-c3cede4543b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-24T15:57:01.595Z_

Let me read the appendix in sections to find any additional figures:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e359d9d6-52a6-4fe9-9799-18b2c88526d9",
  "isSidechain": true,
  "agentId": "ad999017524d4cdd1",
  "requestId": "req_011CbMfhmq85US1WoXuByTUm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e9cc5d67-4a39-4615-920b-59b6466552a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BkijzPQuzFb8kucRv9KDp7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10340,
      "cache_read_input_tokens": 37400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10340,
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

_source line 15 · 2026-05-24T15:57:02.659Z_

<details open><summary>🔧 Tool call — Bash · `toolu_017y7Ld1X2DrbzBXFDFH11V8`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\includegraphics\\|\\\\\\\\caption\\|\\\\\\\\label{fig\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex | head -80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e9cc5d67-4a39-4615-920b-59b6466552a1",
  "isSidechain": true,
  "agentId": "ad999017524d4cdd1",
  "requestId": "req_011CbMfhmq85US1WoXuByTUm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c5e53687-52a8-4019-89c7-0bd970c05e28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BkijzPQuzFb8kucRv9KDp7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10340,
      "cache_read_input_tokens": 37400,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10340,
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

_source line 16 · 2026-05-24T15:57:02.727Z_

<details><summary>↩ Tool result · `toolu_017y7Ld1X2DrbzBXFDFH11V8`</summary>

```text
18:\caption{Metric drift (\%, generation~0$\to$10) for Pythia-410M across contamination levels. Diversity collapse occurs at all $\alpha$ levels, with the strongest decline at low-to-moderate contamination ($\alpha{=}0.25$: distinct-1 $-40.3{\pm}0.3\%$) rather than full replacement ($\alpha{=}1.0$: $-27.8{\pm}1.6\%$). $^\dagger$$\alpha{=}0.10$: single seed (seed~42, preliminary). $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.50$, $\alpha{=}0.75$: 3-seed mean${\pm}$std (seeds 42, 43, 44); $\alpha{=}1.0$: 4-seed mean${\pm}$std (seeds 42, 43, 44, 45).}
45:\caption{Distinct-3 drift (\%, generation~0$\to$10) across contamination levels. $\alpha{=}0.00$, $\alpha{=}0.25$, $\alpha{=}0.75$: 3-seed mean${\pm}$std; $\alpha{=}1.0$: 4-seed mean${\pm}$std; $\alpha{=}0.50$: single seed.}
84:\caption{Observation window sensitivity for Tier~3 consensus ($K{\geq}4/5$) at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Tier~3 pairs: number of canary$\to$downstream pairs (out of 8 validated) reaching $K{\geq}4/5$ method agreement. TY pairs: number of effect-size reference pairs (out of 6) reaching Toda--Yamamoto significance (moderate supplementary method; \S\ref{sec:method}). Consensus stabilizes at $T_{\min}{\geq}5$; TY stabilizes at $T_{\min}{\geq}6$.}
104:\includegraphics[width=\columnwidth]{figures/fig_window_sensitivity.pdf}
105:\caption{Consensus stability across minimum observation windows $T_{\min} \in \{5, \ldots, 10\}$. Left: $K{\geq}3$ consensus count at $\alpha{=}0.75$ (3 seeds). Right: per-method detection count across $T_{\min}$. Consensus stabilises at $T_{\min}{=}5$, confirming that the 10-generation default provides ample statistical power.}
106:\label{fig:window_sensitivity}
119:\caption{Permutation count stability analysis ($\alpha{=}0.75$, 3~seeds, 24 canary$\to$downstream pairs). $p$-values from permutation Granger tests at $n_{\text{perm}}{=}5{,}000$ versus $n_{\text{perm}}{=}10{,}000$.}
139:\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs, 8-pair basis). Null: $\alpha{=}0.0$ (6~seeds 45--50, 36 pairs, 6-pair basis). The expanded null sample reveals modest false positive rates that increase with $q$.}
163:\caption{BH-corrected PermG $p$-values at $\alpha{=}0.45$ (8 canary$\to$downstream pairs $\times$ 2 seeds). Min $p_{\mathrm{fdr}}$ per seed shown. All pairs remain above the $q{=}0.05$ threshold, yielding 0/8 aggregate detection.}
189:\caption{Specification curve summary (1{,}160 specifications, D120-compliant). The blind$\to$onset jump is robust across specifications: 0\% significance rate through $\alpha{=}0.45$, rising to 75\% at $\alpha{=}0.50$.}
211:\includegraphics[width=\columnwidth]{figures/fig_spec_curve.pdf}
212:\caption{Specification curve analysis (1{,}160 configurations). Each point is one analytical specification (method $\times$ pair $\times$ seed); lines trace detection rates across contamination levels. Bottom bar indicates the method for each specification. The blind$\to$onset jump at $\alpha_c{\approx}0.50$ is robust across specifications.}
213:\label{fig:spec_curve}
227:\caption{Transfer Entropy results (12 runs across all $\alpha$ levels). TE\textsubscript{fwd}: canary$\to$downstream; TE\textsubscript{rev}: downstream$\to$canary. Mean uncorrected permutation $p$-values ($n{=}5{,}000$). No pair reaches BH-corrected $q{<}0.05$ in any run.}
267:\caption{Change-point detection under null control ($\alpha{=}0.00$, 3 seeds). CP: detected change-point generation (mean across significant seeds); $|d|$: Cohen's $d$ effect size (mean across all seeds); Sig.\ rate: fraction of seeds where $p{<}0.05$. Overall FPR: 12/18 = 66.7\%.}
287:\caption{Change-point detection at $\alpha{=}0.75$ (3 seeds). CP: detected change-point generation; $|d|$: Cohen's $d$ effect size between pre- and post-change segments. Sig.\ rate: fraction of seeds where $p{<}0.05$.}
323:\caption{Change-point ordering reversal across contamination levels. Under the null ($\alpha{=}0.00$), downstream metrics break before canary metrics; this ordering reverses monotonically as $\alpha$ increases, consistent with the Granger-precedence analysis.}
342:\caption{CUSUM calibration parameters from $\alpha{=}0.0$ null control (3~seeds). $h$: alarm threshold calibrated to achieve FAR${=}$0\%. For $k{\geq}0.25$, the null CUSUM statistic remains at zero, yielding $h \approx 0$.}
367:\caption{CUSUM vs simple calibrated threshold: alarm generation across contamination levels (3~seeds each; all seeds agree on the alarm generation shown). Threshold: metric crosses $\mu_0 - 2\sigma_0$. No CUSUM configuration outperforms the simple threshold at any operating point.}
389:\includegraphics[width=\columnwidth]{figures/fig_cusum_monitoring.pdf}
390:\caption{CUSUM sequential monitoring of token entropy at two contamination levels ($\alpha{=}0.50$, $\alpha{=}0.75$; seed~42). Null control limits calibrated from $\alpha{=}0.0$ runs. At both operating points, the simple $2\sigma$ threshold triggers at the same generation as CUSUM ($k{=}0.25$), confirming that the large initial shift dominates any cumulative memory advantage.}
391:\label{fig:cusum_monitoring}
424:\caption{Multi-Method Consensus Test (MMCT)}
457:\caption{Methodological comparison of canary and monitoring analyses. \checkmark\ = present, $\times$ = absent, $\circ$ = partial (${\leq}2$ levels or limited replication). Diff.\ = differencing/stationarity controls. Multi-M.\ = ${\geq}2$ independent statistical methods. MTC = multiple testing correction. Regime = systematic variation of $\alpha$. Seeds = ${\geq}3$ independent seeds. Arch.\ = ${\geq}2$ architecturally distinct model families.}
520:\caption{Pythia-1.4B phase-diagram cells (fp32, PermG forward, direction-checked).}
546:\includegraphics[width=\columnwidth]{figures/fig_14b_phase.pdf}
547:\caption{Pythia-1.4B phase diagram (PermG forward, 6-pair basis). Each cell shows per-seed detection fractions (s42\,|\,s44 for $T{=}10$; s42\,|\,s43 for $T{=}15$). The detection boundary ($\alpha_c \approx 0.50$) is qualitatively consistent with the 410M results, confirming cross-scale generality.}
548:\label{fig:14b_phase}
575:\caption{Per-method FDR significance (/8 pairs) across contamination levels (Pythia-410M, seed~42, WikiText, fp32). PermG and Diff.\ XCorr use BH-corrected FDR ($q{=}0.05$); Naive XCorr, Threshold, and TY use uncorrected $p{<}0.05$ (no FDR field in pipeline). $\alpha{=}1.0$ from Pythia-410M cross-architecture condition (same seed/domain/precision).}
604:\includegraphics[width=\columnwidth]{figures/fig_per_method_phase.pdf}
605:\caption{Per-method detection heatmaps (Pythia-410M, seed~42, fp32, $T \in \{10, 20\}$). Each panel shows forward-direction detection rate (\%) across contamination levels for one method. PermG exhibits the sharpest onset (0\%$\to$75\% between $\alpha{=}0.45$ and 0.50) with zero null-control detection, while Naive XCorr saturates across all levels including null. TY and Threshold show diffuse, unstable profiles.}
606:\label{fig:per_method_phase}
618:\caption{Naive baseline comparison (Pythia-410M, $T{=}10$, fp32, 3 null-control runs).}
658:\caption{PermG power analysis: $\beta_{50}$ (coupling for 50\% power) under BH-FDR correction ($q{=}0.05$, 8 pairs). $\beta_{50} \cdot \sqrt{T}$ decreases with $T$, indicating power grows faster than $\sqrt{T}$. FPR: false positive rate at $\beta{=}0$ (raw / FDR-corrected). Dashes indicate $<$50\% power not reached within $\beta \leq 2.0$.}
675:\includegraphics[width=\linewidth]{figures/permg_power_curve.pdf}
676:\caption{PermG detection power as a function of coupling strength $\beta$ for five observation lengths ($T{=}6$--$20$; 100 replications $\times$ 5{,}000 permutations, BH FDR $q{=}0.05$). Power increases with both $\beta$ and $T$; at $T{=}6$--$8$, PermG remains underpowered ($<$20\%) even at $\beta{=}2.0$, consistent with the $T{=}10$ minimum required for reliable detection in our experimental setting.}
677:\label{fig:permg_power}
699:\caption{Size (FPR at $\beta{=}0$) and power ($\beta{=}0.6$) under stationary and non-stationary AR(1) DGP ($T{=}11$, 1{,}000 reps, 500 perms). First-differencing maintains nominal size across all $\varphi$; PermG FPR inflates to ${\sim}10\%$ at $\varphi{\geq}0.95$.}
726:\caption{Empirical AR(1) coefficients for token entropy (te) and distinct-1 (d1), raw and first-differenced series. High raw $\varphi$ in d1 reflects deterministic iterative-training decline, not stochastic AR persistence; first-differencing reduces $\varphi$ to $< 0.44$.}
753:\includegraphics[width=\columnwidth]{figures/fig_ar1_diagnostic.pdf}
754:\caption{Empirical AR(1) coefficients by contamination level (Pythia-410M, seed~42, $T{=}10$). (a)~Token entropy: raw $\varphi$ transitions from anti-correlated ($-0.51$) at $\alpha{=}0$ to near-unity ($1.00$) at $\alpha{=}1.0$; first-differencing reduces all values below the $\varphi{=}0.95$ FPR danger zone (dashed red). (b)~Distinct-1: high raw $\varphi$ ($0.81$--$0.97$) across all $\alpha$ including null reflects deterministic trend, not stochastic AR persistence; first-differenced $\varphi$ drops to near zero.}
755:\label{fig:ar1_diagnostic}
781:\caption{Shapley value decomposition (6-pair, mauve excluded). FPR-Shapley computed from 6 null seeds (36 pairs); FNR-Shapley from 45 signal experiments (270 pairs). Combined = FPR + FNR (more negative = better). $2^5{=}32$ coalitions, exact enumeration.}
798:\includegraphics[width=\linewidth]{figures/fig_shapley_contribution.pdf}
799:\caption{Shapley value decomposition of each method's marginal contribution to FPR (positive bars, red) and FNR (negative bars, green/blue), computed from 6 null seeds (36 pairs) and 45 signal experiments (270 pairs). DiffXCorr achieves the best combined Shapley ($-0.299$) via near-zero FPR; PermG ranks second ($-0.141$) as the best directional method. Annotations indicate whether each method's contribution increases or reduces overall error.}
800:\label{fig:shapley}
825:\caption{MMCT weight robustness (3-seed null, 48 experiments): PermG combined Shapley under four weighting schemes. PermG ranks first among directional methods in all cases. Gap = $|\phi^{\text{comb}}_{\text{PermG}} - \phi^{\text{comb}}_{\text{runner-up}}|$. $2^5{=}32$ coalitions, exact enumeration.}
853:\caption{Null-control FPR by method ($\alpha{=}0.0$, 6~seeds 45--50, 6~pairs each). All p-value--based methods (DiffXCorr, PermG, TY) report BH-FDR--corrected rejections at $q{=}0.05$ for fair comparison. Threshold uses a deterministic $3\sigma$ criterion; NaiveXCorr uses uncorrected correlation significance.}
872:\includegraphics[width=\columnwidth]{figures/fig_null_fpr_diagnostic.pdf}
873:\caption{Null-control FPR by method ($\alpha{=}0.0$, 6~seeds, 6-pair basis). Bars: pooled FPR (rejections/36); dots: per-seed FPR. Naive XCorr (91.7\%) and Toda--Yamamoto (38.9\%) vastly exceed the 5\% nominal level (dashed). PermG (11.1\%) is the lowest-FPR directional method; DiffXCorr (2.8\%) is lowest overall but lacks forward/reverse separation.}
874:\label{fig:null_fpr_diagnostic}
885:\includegraphics[width=\columnwidth]{figures/fig_bootstrap_fpr.pdf}
886:\caption{Bootstrap distribution of PermG FPR (10{,}000 resamples, 6 null seeds). Mean FPR $= 11.1\%$ (red line); bootstrap percentile 95\% CI $[0.0\%, 22.2\%]$ (orange band). The Clopper--Pearson cluster-adjusted CI reported in the text ($[1.2\%, 30.4\%]$) is wider due to ICC correction. The distribution is right-skewed: four of six seeds show zero false positives.}
887:\label{fig:bootstrap_fpr}
924:\includegraphics[width=\columnwidth]{figures/fig_detection_surface.pdf}
925:\caption{Detection rate surface over the $\alpha \times T$ operating space (PermG forward, 3 seeds). Contour lines indicate 25\%, 50\%, and 75\% detection rates. The fitted power-law boundary $\alpha_c(T)$ (dashed) separates the blind zone ($\alpha \leq 0.45$) from the reliable detection regime ($\alpha \geq 0.75$). The transition zone ($0.50 \leq \alpha \leq 0.60$) widens at shorter $T$.}
926:\label{fig:detection_surface}
940:\caption{Threshold sensitivity at $\alpha{=}1.0$ (Pythia-410M, s42, fp32). All thresholds trigger at generation~1 (entropy drop 40.7\%$\gg$threshold), producing identical recovery trajectories.}
980:\caption{First-differencing effect by channel type. $|r|$ retention = diff $|r|$ / naive $|r|$. Despite comparable $|r|$ retention, Granger $F$ differs by an order of magnitude. Perplexity channel has limited sample ($n{=}8$); all paired comparisons are from bf16 experiments.}
1008:\includegraphics[width=\columnwidth]{figures/fig_channel_effect.pdf}
1009:\caption{Channel effect size asymmetry. (a)~First-differencing retains comparable correlation magnitude for diversity ($95.2\%$) and perplexity ($100.2\%$) channels, ruling out blanket power loss. (b)~Despite equivalent $|r|$ retention, Granger $F$-statistic is ${\sim}6\times$ higher for diversity ($F{=}67.8$) than perplexity ($F{=}11.5$), reflecting a genuine temporal structure difference: diversity channels exhibit canary-leading lags while perplexity co-moves contemporaneously.}
1010:\label{fig:channel_effect}
1030:\caption{Gaussian MI lower bound (bits) between token entropy and distinct-$n$ diversity metrics ($T{=}11$, Pythia-410M, fp32). Mean across distinct-1/2/3; $\alpha{=}0.05$ excluded (see text). CIs omitted due to width at $T{=}11$.}
1063:\caption{Degradation onset generation (5\% threshold) by metric and condition (Pythia-410M, WikiText, fp32). Token entropy reaches onset at generation~1 in all non-null conditions; distinct-$n$ metrics follow at generation~2.}
1084:\includegraphics[width=\columnwidth]{figures/fig_cascade_onset.pdf}
1085:\caption{Cascade onset timeline (Pythia-410M, WikiText, fp32, 5\% threshold). Token entropy and ECE reach onset at generation~1 (Phase~1, blue shading), while distinct-$n$ metrics follow at generation~2 (Phase~2, orange shading). Perplexity onset occurs at generation~4 only at $\alpha{\geq}0.50$; MAUVE onset is condition-dependent. The ordering $t_H \leq t_D$ holds across all 5 conditions (2 seeds $\times$ 3 $\alpha$ levels minus $\alpha{=}0.25$ s42, which has identical Phase~1 and~2 onset).}
1086:\label{fig:cascade_onset}
1163:\caption{Cascade onset generations (5\% threshold) for representative experiments (Pythia-410M, WikiText, fp32). Phase~1: entropy and ECE ($t_H$, $t_{\mathrm{ECE}}$); Phase~2: diversity ($t_D$, min over distinct-$n$); Phase~3: MAUVE ($t_M$). All conditions confirm the predicted ordering $t_H = t_{\mathrm{ECE}} \leq t_D \leq t_M$.}
1235:\caption{T=20 predict-then-verify comparison (Pythia-410M, seed~42, WikiText, fp32). Excluding $\alpha{=}1.0$, two of four predictions fall within CI ($\alpha{=}0.50$, $0.75$); boundary cases show systematic bias---$\alpha{=}0.45$ falsifies the ceiling hypothesis (under-prediction), $\alpha{=}0.60$ over-predicts under raw $p$-values (v1; matches under FDR v2, not pre-committed).}
1280:\caption{Task degradation across contamination levels (Pythia-410M, seed~42, fp32, generation~10). Perplexity evaluated on held-out WikiText-103.}
1307:\caption{Cross-architecture PermG forward detection ($\alpha{=}1.0$, 15 model-seed combinations across five families---Pythia, GPT-2, OPT, Qwen, SmolLM3---and two domains; Padding-410M is a Pythia variant). PermG fwd $=$ count of FDR-significant forward pairs out of 8.}
1346:\caption{Null-condition FPR for GPT-2-medium ($\alpha{=}0$, $T{=}10$, 6-pair basis). PermG forward detection shows extreme seed dependence; $K{\geq}3$ consensus remains at 0\% across both seeds.}
1366:\caption{Null drift magnitude ($\alpha{=}0$, gen\,0$\to$10; GPT-2-medium: 2 seeds; Pythia-410M: 4 seeds, s46/s48--s50). GPT-2-medium exhibits ${\sim}4{\times}$ stronger entropy drift and ${\sim}7{\times}$ stronger distinct-3 drift than Pythia-410M.}
1392:\includegraphics[width=0.85\linewidth]{figures/fig_cross_arch_heatmap.pdf}
1393:\caption{Cross-architecture PermG forward detection rates at $\alpha{=}1.0$ across 15 model-seed combinations spanning five families (Pythia, GPT-2, OPT, Qwen, SmolLM3; 345M--6.9B). Dark bars: PermG forward detection; light bars: $K{\geq}3$ multi-method consensus. C4-domain training achieves 8/8; SmolLM3-3B (3/8) and Pythia-1.4B s42 (2/8) are the two below-threshold conditions.}
1394:\label{fig:cross_arch_heatmap}
1399:\includegraphics[width=\columnwidth]{figures/fig_fpr_sensitivity.pdf}
1400:\caption{Null-control false positive rates by detection method (Pythia-410M, seed~42, 8-pair basis). PermG achieves the lowest FPR among directional methods; Naive XCorr exceeds 90\%. Dashed line: 5\% nominal level.}
1401:\label{fig:fpr_sensitivity}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c5e53687-52a8-4019-89c7-0bd970c05e28",
  "isSidechain": true,
  "promptId": "ec5ba50c-898a-489d-8777-d0a519cbb553",
  "agentId": "ad999017524d4cdd1",
  "type": "user",
  "uuid": "9860bbab-6354-425f-a02b-eb501651106f",
  "sourceToolAssistantUUID": "c5e53687-52a8-4019-89c7-0bd970c05e28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T15:57:03.269Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018deWKU5SA6BBaoPdsifoLC`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\ref{fig\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9860bbab-6354-425f-a02b-eb501651106f",
  "isSidechain": true,
  "agentId": "ad999017524d4cdd1",
  "requestId": "req_011CbMfhmq85US1WoXuByTUm",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a01eff20-5d75-4611-9d69-b12a98c54e7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BkijzPQuzFb8kucRv9KDp7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10340,
      "cache_read_input_tokens": 37400,
      "output_tokens": 286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10340
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 286,
          "cache_read_input_tokens": 37400,
          "cache_creation_input_tokens": 10340,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10340,
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

_source line 18 · 2026-05-24T15:57:03.339Z_

<details><summary>↩ Tool result · `toolu_018deWKU5SA6BBaoPdsifoLC`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex:12:We map this landscape on Pythia-410M~\cite{biderman2023pythia} across 13 contamination levels with multi-seed replication (Figure~\ref{fig:regime_map}), and find structured terrain rather than smooth degradation: detection is absent through $\alpha{=}0.45$, then jumps from 0/8 to 6/8 significant pairs within a 2-percentage-point interval, before a non-monotonic dip and eventual reliable detection above a power-law boundary $\alpha_c(T)$ (Eq.~\ref{eq:alpha-c-theory}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:26:Sigmoid regression on the 13-point $T{=}10$ grid yields $\alpha_c = 0.483 \pm 0.006$ ($R^2 = 0.969$; Figure~\ref{fig:dose_response}); dense $\alpha$ sampling (17~values) constrains onset steepness to $k{=}15.7$ (95\% CI $[9.4, 28.2]$), a steep but finite-width sigmoid ($\Delta\mathrm{AIC}{=}-110$ vs.\ step function; Appendix~\ref{app:sigmoid_shape}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:60:The PermG dose-response profile (Figure~\ref{fig:dose_response}; full per-method table in Appendix~\ref{app:dose_response}) reveals three confirmed detection regimes---\emph{blind} ($\alpha \leq 0.45$, 0/8 FDR-significant pairs), \emph{onset} ($\alpha \approx 0.50$, 6/8), and \emph{detection} ($\alpha{\geq}0.75$, 6/8 across 4~seeds at $\alpha{=}1.0$)---plus a non-monotonic anomaly at $\alpha \approx 0.60$ (0/8) whose mechanism remains unexplained.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:65:Method choice is itself a major source of variability: at $\alpha{=}1.0$, direction-checked forward significance spans 0\% to 75\% (Figure~\ref{fig:method_comparison}), with $\kappa{=}0.185$; a specification curve (18~variants; Appendix~\ref{app:spec_curve}) confirms onset invariance.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:107:The predictive trigger fires at generation~1 (one generation before a reactive distinct-1 baseline), reducing peak perplexity by 64\% ($56.99$ vs.\ $157.09$; Figure~\ref{fig:intervention}) in both Pythia-410M and 1.4B.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a01eff20-5d75-4611-9d69-b12a98c54e7a",
  "isSidechain": true,
  "promptId": "ec5ba50c-898a-489d-8777-d0a519cbb553",
  "agentId": "ad999017524d4cdd1",
  "type": "user",
  "uuid": "82e0c880-b7b2-4374-b019-dfda31870b45",
  "sourceToolAssistantUUID": "a01eff20-5d75-4611-9d69-b12a98c54e7a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-24T15:57:04.892Z_

Perfect. Now let me use Grep to find all figure references more systematically and extract the complete context:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82e0c880-b7b2-4374-b019-dfda31870b45",
  "isSidechain": true,
  "agentId": "ad999017524d4cdd1",
  "requestId": "req_011CbMfi1wSDwr5ZmzMvjteL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7fcfe647-5b67-4c43-af2d-1566c1f6bb76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GetG13xJFw2qUfwwFkSxRg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7053,
      "cache_read_input_tokens": 47740,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7053,
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

_source line 20 · 2026-05-24T15:57:05.947Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01KeMAzgJDLoUS8UoR4JyjF8`</summary>

```json
{
  "command": "grep -B5 -A15 \"\\\\\\\\begin{figure\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fcfe647-5b67-4c43-af2d-1566c1f6bb76",
  "isSidechain": true,
  "agentId": "ad999017524d4cdd1",
  "requestId": "req_011CbMfi1wSDwr5ZmzMvjteL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6c0af084-726b-4d4b-a453-ca0021e8e5c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GetG13xJFw2qUfwwFkSxRg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 7053,
      "cache_read_input_tokens": 47740,
      "output_tokens": 207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7053
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 207,
          "cache_read_input_tokens": 47740,
          "cache_creation_input_tokens": 7053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7053,
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

_source line 21 · 2026-05-24T15:57:06.000Z_

<details><summary>↩ Tool result · `toolu_01KeMAzgJDLoUS8UoR4JyjF8`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex-    \item \textbf{We formalize cascade ordering for canary metric selection} (\S\ref{sec:cascade}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex-    Under mode amplification, entropy responds before diversity by ${\geq}1$ generation (Design Principles~\ref{thm:entropy_leads}--\ref{prop:div_lag}), confirmed in 14/15 experiments ($\alpha \geq 0.30$; GPT-2-medium s43 bidirectional).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex-\end{enumerate}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex:\begin{figure*}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex-\includegraphics[width=0.55\textwidth]{figures/fig_phase_diagram.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex-\caption{Detection phase diagram (Pythia-410M, fp32, PermG direction-checked). Each cell shows the number of FDR-significant canary$\to$diversity pairs (of~8) at a given contamination strength~$\alpha$ and observation window~$T$. The dashed curve is the fitted detection boundary $\alpha_c(T) \propto T^{-\gamma}$ with $\gamma \in [0.64, 2.08]$ (profile 95\% CI; \S\ref{sec:theory}). Diamond markers ($\diamond$) flag a non-monotonic anomaly at $\alpha{=}0.60$ (0/8 at $T{\leq}20$); the star ($\star$) marks its dissolution at $T{=}25$ (5/8).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex-\label{fig:regime_map}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/introduction.tex-\end{figure*}
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-Lead-lag analysis in iterative model collapse is fragile along three axes, each documented with data from \S\ref{sec:regime}--\ref{sec:dose_response}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-\emph{Method sensitivity}: five detection methods applied to identical data yield forward significance rates spanning 0\% to 92\%, with inter-method agreement at $\kappa{=}0.185$.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-\emph{Spurious regression}: first-differencing eliminates canary$\to$perplexity associations ($F{\approx}0$, $p{=}0.99$) while preserving canary$\to$diversity (24/24$\to$24/24), exposing an entire analysis channel as trend-driven~\cite{granger1974spurious}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-\emph{Regime dependence}: the same Granger test shifts from 0/8 to 6/8 significant pairs within a 2-percentage-point interval ($\alpha{=}0.48 \to 0.50$).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex:\begin{figure*}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-\includegraphics[width=\textwidth]{figures/fig_framework.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-\caption{Analytical framework. (a)~Iterative contamination loop: each generation trains on an $\alpha$-fraction synthetic mixture, from which canary (entropy) and downstream (distinct-$n$) metrics are extracted. (b)~Multi-method consensus test (MMCT): five detection methods with varying FPR profiles converge to a $K{\geq}3$ majority vote; PermG is selected as the lowest-FPR directional method. (c)~Signal$\times$Resolution model: sub-linear signal $S(\alpha)$ and finite resolution $R(\alpha)$ produce three confirmed regimes (blind, onset, detection) plus a non-monotonic anomaly, with boundary $\alpha_c(T) \sim T^{-\gamma}$.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-\label{fig:framework}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-\end{figure*}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-\subsection{Method Sensitivity Analysis}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-\label{sec:mmct}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-We compare five lead-lag detection methods in a multi-method comparison~\cite{simonsohn2020specification} (algorithm in Appendix~\ref{app:mmct}), calibrated against null-control ($\alpha{=}0.0$) data where any detection is a false positive.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-PermG's empirical FPR of 11.1\% (CI $[1.2\%, 30.4\%]$; 6 null seeds) exceeds the nominal 5\% threshold; $K{\geq}3$ consensus yields 16.7\% FPR (6/36), driven primarily by high-FPR methods (PermG contributes to only 2/6 consensus false positives; Appendix~\ref{app:fpr_independence}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-The five methods are: naive cross-correlation, differenced cross-correlation (DiffXCorr), threshold onset, permutation Granger causality (PermG), and Toda--Yamamoto~\cite{toda1995statistical}.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-Detection results use equal-weight majority voting ($K{\geq}3$ of 5 methods, each contributing one vote per pair) with forward-direction filtering; FPR-inverse weighting is used only in exploratory method ranking (Appendix~\ref{app:weight_robustness}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-Each method encodes different assumptions, and these differences produce dramatically different FPR profiles.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-Pooled null-control FPR across six seeds (6-pair basis, 36 pairs): DiffXCorr 2.8\%, PermG 11.1\%, Threshold 27.8\%, Toda--Yamamoto 38.9\%, NaiveXCorr 91.7\% (Appendix~\ref{app:fpr_independence}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/method.tex-We classify a method as \emph{directional} if its test structure inherently separates forward from reverse precedence (PermG tests each direction independently; threshold onset compares crossing order), rather than inferring direction post-hoc from peak lag sign (NaiveXCorr, DiffXCorr).
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\paragraph{Blind zone.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-The canary mechanism has a fundamental limitation: at $\alpha{=}0.10$, distinct-1 has already dropped by $39.6\%$, yet token entropy is indistinguishable from the null ($-5.3\%$ versus $-4.6{\pm}0.4\%$ at $\alpha{=}0.0$).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-The gen-1 entropy deviation spans three orders of magnitude across the $\alpha$ range ($0.5\sigma$ at $\alpha{=}0.10$ to $60\sigma$ at $\alpha{=}0.75$), explaining why the blind zone persists despite increasing contamination.\footnote{Seed~43 at $\alpha{=}0.10$ shows 3/8 versus 0/8 for seed~42; no other sub-threshold level exhibits seed-dependent detection.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-Below $\alpha_c$ at $T{=}10$, diversity collapse proceeds without any detectable Granger-precedence signal, though Gaussian MI remains positive (Appendix~\ref{app:mi_analysis}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:\begin{figure*}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\includegraphics[width=0.55\textwidth]{figures/metric_trajectory.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\caption{Metric trajectories at $\alpha{=}1.0$ (Pythia-410M, 4~seeds). Token entropy drops at generation~1; distinct-1 declines from generations~2--3, with a consistent one-generation canary lead across all four seeds (shaded: inter-seed range). This pattern corresponds to 24/24 forward and 0/24 reverse FDR-significant canary$\to$diversity pairs (6 per seed, mauve excluded).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\label{fig:metric_trajectory}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\end{figure*}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\subsection{Dose-Response and Detection Regimes}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\label{sec:dose_response}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\includegraphics[width=\columnwidth,trim={0 0.4cm 0 0.4cm},clip]{figures/fig_dose_response.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\vspace{-6pt}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\caption{PermG dose-response profile (Pythia-410M, $T{=}10$, fp32). Sigmoid fit (shaded 95\% CI) yields $\alpha_c{=}0.483$. Three confirmed regimes: blind ($\alpha{\leq}0.45$, 0/8), onset ($\alpha{\approx}0.50$, 6/8), detection ($\alpha{\geq}0.75$); non-monotonic anomaly at $\alpha{=}0.60$ (0/8) (out of 8 canary$\to$downstream pairs).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\label{fig:dose_response}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-The PermG dose-response profile (Figure~\ref{fig:dose_response}; full per-method table in Appendix~\ref{app:dose_response}) reveals three confirmed detection regimes---\emph{blind} ($\alpha \leq 0.45$, 0/8 FDR-significant pairs), \emph{onset} ($\alpha \approx 0.50$, 6/8), and \emph{detection} ($\alpha{\geq}0.75$, 6/8 across 4~seeds at $\alpha{=}1.0$)---plus a non-monotonic anomaly at $\alpha \approx 0.60$ (0/8) whose mechanism remains unexplained.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-At $\alpha{=}0.55$, PermG returns 0/8 FDR-significant pairs despite marginal $p$-values ($p_{\mathrm{fdr}}{=}0.062$--$0.092$); differenced cross-correlation detects 8/8 bidirectionally at this level, confirming that a lead-lag signal exists but falls below PermG's directional detection threshold.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-At $\alpha{=}0.60$, PermG returns $0/8$ at $T{\leq}20$ but recovers to $5/8$ at $T{=}25$, consistent with $\sqrt{T}$ power scaling (Appendix~\ref{app:t20_comparison}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-Notably, $K{\geq}3$ consensus detects 8/8 at $\alpha{=}0.60$, suggesting that the non-monotonic anomaly is PermG-specific rather than a property of the underlying landscape; other methods see through it where PermG's directional test loses power.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-Method choice is itself a major source of variability: at $\alpha{=}1.0$, direction-checked forward significance spans 0\% to 75\% (Figure~\ref{fig:method_comparison}), with $\kappa{=}0.185$; a specification curve (18~variants; Appendix~\ref{app:spec_curve}) confirms onset invariance.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-Task degradation corroborates: perplexity jumps $+31\%$ between $\alpha{=}0.50$ and $0.52$ (Appendix~\ref{app:task_degradation}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\includegraphics[width=\columnwidth]{figures/fig_method_comparison.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\caption{Method sensitivity: FDR-significant forward pairs (\%) across contamination levels (Pythia-410M, seed~42, fp32). PermG (dark blue) achieves 0\% null-control FPR with stable 75\% detection at $\alpha \geq 0.50$. Dashed line: 5\% nominal. Full table in Appendix~\ref{app:dose_response}.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\label{fig:method_comparison}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\end{figure}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\subsection{Detection Boundary Left-Shift}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\label{sec:t20}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-Longer observation windows push the detection boundary to lower contamination levels: $\alpha_c(5){\geq}1.0$, $\alpha_c(10){=}0.487$, consistent with power-law scaling (\S\ref{sec:theory}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-The $\alpha{=}0.45$ column validates this left-shift: undetectable at $T{\leq}10$ (0/8), it crosses into reliable detection at $T{=}15$ (6/8, dual-seed) and remains there at $T{=}20$ and $T{=}25$.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-Cross-seed replication shows PermG within ${\pm}1$, though boundary cells exhibit sensitivity ($[0, 6]/8$ at $T{=}10$, $\alpha{=}0.50$).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-The $\alpha{=}0.60$ anomaly dissolves by $T{=}25$ ($5/8$), consistent with $\sqrt{T}$ power scaling; predict-then-verify yields 2/4 boundary predictions within CI (Appendix~\ref{app:t20_prediction_timeline}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-
--
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-As an illustrative proof-of-concept under favorable conditions ($\alpha{=}1.0$, full replacement), we implement predictive cessation: training switches to pure real data when token entropy drops ${>}15\%$ from generation~0.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-The 15\% threshold was selected post-hoc (robust band $[10\%, 22\%]$, zero false alarms; Appendix~\ref{app:intervention_sensitivity}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-The predictive trigger fires at generation~1 (one generation before a reactive distinct-1 baseline), reducing peak perplexity by 64\% ($56.99$ vs.\ $157.09$; Figure~\ref{fig:intervention}) in both Pythia-410M and 1.4B.
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-This single-setting demonstration ($N{=}2$ architectures, $\alpha{=}1.0$, post-hoc threshold) is not rigorously evaluated (CUSUM comparison: Appendix~\ref{app:csmp}).
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex:\begin{figure}[t]
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\centering
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\includegraphics[width=\columnwidth]{figures/fig_intervention.pdf}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\caption{Canary-triggered intervention (Pythia-410M, $\alpha{=}1.0$). Predictive cessation on entropy (generation~1) reduces peak perplexity by 64\% versus reactive triggering on distinct-1 (generation~2).}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\label{fig:intervention}
/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/experiments.tex-\end{figure}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c0af084-726b-4d4b-a453-ca0021e8e5c1",
  "isSidechain": true,
  "promptId": "ec5ba50c-898a-489d-8777-d0a519cbb553",
  "agentId": "ad999017524d4cdd1",
  "type": "user",
  "uuid": "83a0f23c-e036-43a7-8dde-56dbc29d0a28",
  "sourceToolAssistantUUID": "6c0af084-726b-4d4b-a453-ca0021e8e5c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-24T15:57:07.828Z_

Now let me search the appendix for all figures:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83a0f23c-e036-43a7-8dde-56dbc29d0a28",
  "isSidechain": true,
  "agentId": "ad999017524d4cdd1",
  "requestId": "req_011CbMfiDTyeAKBMUNXFaeoU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1cbe631f-b1fa-4d73-807e-b324473ee7f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PMLSzgcZX1eg9ySHydVoQP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 7108,
      "cache_read_input_tokens": 54793,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7108,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 23 · 2026-05-24T15:57:08.360Z_

<details open><summary>🔧 Tool call — Read · `toolu_01YChHhtLMMKdeH5Hyw9fy5P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex",
  "offset": 1,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cbe631f-b1fa-4d73-807e-b324473ee7f6",
  "isSidechain": true,
  "agentId": "ad999017524d4cdd1",
  "requestId": "req_011CbMfiDTyeAKBMUNXFaeoU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bf0b99c6-5bd4-4e33-a461-6a7463e11767",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PMLSzgcZX1eg9ySHydVoQP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 7108,
      "cache_read_input_tokens": 54793,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7108
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 136,
          "cache_read_input_tokens": 54793,
          "cache_creation_input_tokens": 7108,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7108,
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

_source line 24 · 2026-05-24T15:57:08.637Z_

<details><summary>↩ Tool result · `toolu_01YChHhtLMMKdeH5Hyw9fy5P`</summary>

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
139	\caption{FDR threshold sensitivity for permutation Granger significance. Treatment: $\alpha{=}0.75$ (3~seeds, 24 forward-direction pairs, 8-pair basis). Null: $\alpha{=}0.0$ (6~seeds 45--50, 36 pairs, 6-pair basis). The expanded null sample reveals modest false positive rates that increase with $q$.}
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
443	FPR-inverse weighting penalizes methods with high false positive rates on null-control data: naive cross-correlation (FPR${=}91.7\%$) receives weight $w{=}1.09$, while PermG (FPR${=}11.1\%$, the lowest among directional methods; DiffXCorr achieves 2.8\% but lacks directional separation) receives $w{=}9.0$.
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
  "parentUuid": "bf0b99c6-5bd4-4e33-a461-6a7463e11767",
  "isSidechain": true,
  "promptId": "ec5ba50c-898a-489d-8777-d0a519cbb553",
  "agentId": "ad999017524d4cdd1",
  "type": "user",
  "uuid": "3c366e27-a00b-4716-b715-dc5a0d1793fa",
  "sourceToolAssistantUUID": "bf0b99c6-5bd4-4e33-a461-6a7463e11767",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-24T15:57:10.558Z_

Now let me compile the complete figure information from what I've gathered:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c366e27-a00b-4716-b715-dc5a0d1793fa",
  "isSidechain": true,
  "agentId": "ad999017524d4cdd1",
  "requestId": "req_011CbMfiQaxq55Uc5SgvFtQA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e494959c-434a-494c-943f-b08ea802319e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XEHVkCtfETZ3Sq8PQT2PcX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12913,
      "cache_read_input_tokens": 61901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 12913,
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

_source line 26 · 2026-05-24T15:57:11.347Z_

<details open><summary>🔧 Tool call — Bash · `toolu_012YVAwowtAtKaqEGXUZ4dg5`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\label{fig\" /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/docs/paper/appendix.tex | head -40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e494959c-434a-494c-943f-b08ea802319e",
  "isSidechain": true,
  "agentId": "ad999017524d4cdd1",
  "requestId": "req_011CbMfiQaxq55Uc5SgvFtQA",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "02414cd6-3d3b-401e-9c8a-8dd9f2fdb86c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XEHVkCtfETZ3Sq8PQT2PcX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12913,
      "cache_read_input_tokens": 61901,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 118,
          "cache_read_input_tokens": 61901,
          "cache_creation_input_tokens": 12913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12913,
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

_source line 27 · 2026-05-24T15:57:11.415Z_

<details><summary>↩ Tool result · `toolu_012YVAwowtAtKaqEGXUZ4dg5`</summary>

```text
106:\label{fig:window_sensitivity}
213:\label{fig:spec_curve}
391:\label{fig:cusum_monitoring}
548:\label{fig:14b_phase}
606:\label{fig:per_method_phase}
677:\label{fig:permg_power}
755:\label{fig:ar1_diagnostic}
800:\label{fig:shapley}
874:\label{fig:null_fpr_diagnostic}
887:\label{fig:bootstrap_fpr}
926:\label{fig:detection_surface}
1010:\label{fig:channel_effect}
1086:\label{fig:cascade_onset}
1394:\label{fig:cross_arch_heatmap}
1401:\label{fig:fpr_sensitivity}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "02414cd6-3d3b-401e-9c8a-8dd9f2fdb86c",
  "isSidechain": true,
  "promptId": "ec5ba50c-898a-489d-8777-d0a519cbb553",
  "agentId": "ad999017524d4cdd1",
  "type": "user",
  "uuid": "c1f539bb-6211-4f3a-bef2-b67251da30a2",
  "sourceToolAssistantUUID": "02414cd6-3d3b-401e-9c8a-8dd9f2fdb86c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-24T15:57:34.481Z_

Perfect. Now I have comprehensive information about all the figures. Let me compile the final summary:

## Figure Extraction Summary

Based on systematic analysis of introduction.tex, method.tex, experiments.tex, and appendix.tex, here are all figures in the paper with their narrative intent:

**MAIN TEXT FIGURES (5 figures)**

1. **fig_phase_diagram.pdf** (Introduction, line 31)
   - Label: fig:regime_map
   - Caption: "Detection phase diagram (Pythia-410M, fp32, PermG direction-checked). Each cell shows the number of FDR-significant canary→diversity pairs (of 8) at a given contamination strength α and observation window T. The dashed curve is the fitted detection boundary αc(T) ∝ T^(-γ) with γ ∈ [0.64, 2.08] (profile 95% CI; §sec:theory). Diamond markers flag a non-monotonic anomaly at α=0.60 (0/8 at T≤20); the star marks its dissolution at T=25 (5/8)."
   - Intent: Maps the complete detectability landscape across contamination levels and observation lengths, showing sharp phase transitions between blind, onset, and detection regimes.

2. **fig_framework.pdf** (Method, line 37)
   - Label: fig:framework
   - Caption: "Analytical framework. (a) Iterative contamination loop: each generation trains on an α-fraction synthetic mixture, from which canary (entropy) and downstream (distinct-n) metrics are extracted. (b) Multi-method consensus test (MMCT): five detection methods with varying FPR profiles converge to a K≥3 majority vote; PermG is selected as the lowest-FPR directional method. (c) Signal×Resolution model: sub-linear signal S(α) and finite resolution R(α) produce three confirmed regimes (blind, onset, detection) plus a non-monotonic anomaly, with boundary αc(T) ∼ T^(-γ)."
   - Intent: Illustrates the experimental pipeline and the multi-method statistical approach underlying the detectability landscape.

3. **metric_trajectory.pdf** (Experiments, line 43)
   - Label: fig:metric_trajectory
   - Caption: "Metric trajectories at α=1.0 (Pythia-410M, 4 seeds). Token entropy drops at generation 1; distinct-1 declines from generations 2–3, with a consistent one-generation canary lead across all four seeds (shaded: inter-seed range). This pattern corresponds to 24/24 forward and 0/24 reverse FDR-significant canary→diversity pairs (6 per seed, mauve excluded)."
   - Intent: Demonstrates the cascade ordering—entropy as early-warning canary preceding diversity collapse—at full-replacement contamination.

4. **fig_dose_response.pdf** (Experiments, line 54)
   - Label: fig:dose_response
   - Caption: "PermG dose-response profile (Pythia-410M, T=10, fp32). Sigmoid fit (shaded 95% CI) yields αc=0.483. Three confirmed regimes: blind (α≤0.45, 0/8), onset (α≈0.50, 6/8), detection (α≥0.75); non-monotonic anomaly at α=0.60 (0/8) (out of 8 canary→downstream pairs)."
   - Intent: Focuses on the critical onset transition region, showing the steepness of the detection boundary and method performance across contamination levels.

5. **fig_method_comparison.pdf** (Experiments, line 71)
   - Label: fig:method_comparison
   - Caption: "Method sensitivity: FDR-significant forward pairs (%) across contamination levels (Pythia-410M, seed 42, fp32). PermG (dark blue) achieves 0% null-control FPR with stable 75% detection at α ≥ 0.50. Dashed line: 5% nominal. Full table in Appendix§app:dose_response."
   - Intent: Highlights the critical methodological message—that choice of detection algorithm dramatically affects conclusions (0% to 75% detection at α=1.0 across five methods), with PermG selected as the most reliable directional test.

6. **fig_intervention.pdf** (Experiments, line 112)
   - Label: fig:intervention
   - Caption: "Canary-triggered intervention (Pythia-410M, α=1.0). Predictive cessation on entropy (generation 1) reduces peak perplexity by 64% versus reactive triggering on distinct-1 (generation 2)."
   - Intent: Proof-of-concept demonstrating practical utility—entropy as a one-generation-earlier trigger for intervention can reduce model degradation by 64% versus reactive approaches.

**APPENDIX FIGURES (10 figures)**

7. **fig_window_sensitivity.pdf** (Appendix, line 104)
   - Label: fig:window_sensitivity
   - Intent: Validates that the default T=10 observation window is sufficient; consensus stability established at T_min≥5.

8. **fig_spec_curve.pdf** (Appendix, line 211)
   - Label: fig:spec_curve
   - Intent: Specification curve across 1,160 analytical configurations; confirms the blind→onset jump at α_c≈0.50 is robust to analytical choices.

9. **fig_cusum_monitoring.pdf** (Appendix, line 389)
   - Label: fig:cusum_monitoring
   - Intent: Compares CUSUM sequential testing versus simple calibrated threshold monitoring; shows no advantage for CUSUM's cumulative memory when initial entropy drop dominates.

10. **fig_14b_phase.pdf** (Appendix, line 546)
    - Label: fig:14b_phase
    - Intent: Cross-architecture validation at larger scale (Pythia-1.4B); confirms detection boundary consistency at α_c≈0.50 across different model size.

11. **fig_per_method_phase.pdf** (Appendix, line 604)
    - Label: fig:per_method_phase
    - Intent: Per-method heatmaps showing sharp PermG onset (0%→75% between α=0.45–0.50) versus diffuse profiles for other methods.

12. **permg_power_curve.pdf** (Appendix, line 675)
    - Label: fig:permg_power
    - Intent: Power analysis showing PermG requires T≥6–8 for >50% power; justifies the T=10 minimum.

13. **fig_ar1_diagnostic.pdf** (Appendix, line 753)
    - Label: fig:ar1_diagnostic
    - Intent: Stationarity diagnostics; first-differencing reduces AR(1) persistence below danger zone (φ<0.95).

14. **fig_shapley_contribution.pdf** (Appendix, line 798)
    - Label: fig:shapley
    - Intent: Marginal contribution of each method to FPR/FNR; ranks methods by Shapley value.

15. **fig_null_fpr_diagnostic.pdf** (Appendix, line 872)
    - Label: fig:null_fpr_diagnostic
    - Intent: Null-control false positive rates by method; PermG 11.1% is the lowest among directional tests.

16. **fig_bootstrap_fpr.pdf** (Appendix, line 885)
    - Label: fig:bootstrap_fpr
    - Intent: Bootstrap distribution of PermG FPR showing right-skew (mean 11.1%, four of six seeds have zero FP).

17. **fig_detection_surface.pdf** (Appendix, line 924)
    - Label: fig:detection_surface
    - Intent: 3D surface over α×T showing contours of detection rate and the power-law boundary.

18. **fig_channel_effect.pdf** (Appendix, line 1008)
    - Label: fig:channel_effect
    - Intent: Explains why canary→diversity survives first-differencing (lagged temporal structure) while canary→perplexity vanishes (contemporaneous co-movement).

19. **fig_cascade_onset.pdf** (Appendix, line 1084)
    - Label: fig:cascade_onset
    - Intent: Timeline of cascade ordering—entropy/ECE reach onset at generation 1, diversity at generation 2, perplexity at generation 4+.

20. **fig_cross_arch_heatmap.pdf** (Appendix, line 1392)
    - Label: fig:cross_arch_heatmap
    - Intent: Cross-architecture generalization across 15 model-seed combinations (Pythia, GPT-2, OPT, Qwen, SmolLM3); shows 11/15 conditions confirm the entropy-leads-diversity pattern.

All figures collectively establish: (1) the detectability landscape has sharp phase transitions organized by a power-law boundary, (2) method choice is a primary source of variability, (3) entropy precedes diversity with consistent one-generation lag, and (4) the pattern generalizes across architectures with identifiable failure modes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1f539bb-6211-4f3a-bef2-b67251da30a2",
  "isSidechain": true,
  "agentId": "ad999017524d4cdd1",
  "requestId": "req_011CbMficU5jVRWjtUuQyms2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cff3a111-8568-4141-9a7c-f6657665a305",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/.claude/sessions/paper_figure_optimize_7527f1ab",
  "sessionId": "e3a718e1-d291-4556-a690-e32011dfe325",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KF8U7hsNUpQwBDD3qXAjE6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 312,
      "cache_read_input_tokens": 74814,
      "output_tokens": 2222,
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
          "input_tokens": 2,
          "output_tokens": 2222,
          "cache_read_input_tokens": 74814,
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
