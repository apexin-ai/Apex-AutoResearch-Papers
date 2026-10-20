# Research conversation: Read the following files in full and report their complete contents back to me. These are LaTeX section files for a pape

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a5995f18396c1763e.jsonl`
- **Structured JSON:** [`dac7cfe4b8ebcc1484b6.json`](../../sessions/da/dac7cfe4b8ebcc1484b6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

17 recorded events

### User

_source line 1 · 2026-05-19T14:25:02.571Z_

Read the following files in full and report their complete contents back to me. These are LaTeX section files for a paper:

1. /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex
5. /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex
6. /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex
7. /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex

For each file, report the FULL content - every line. This is critical for a review process.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "142cd10d-776d-4d99-8e0d-47ee9ec75758",
  "agentId": "a5995f18396c1763e",
  "type": "user",
  "uuid": "7b88883f-907f-4528-b3e6-08196cbf0ec2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_1_38fb0170",
  "sessionId": "356f6463-a842-4ea1-8de2-5e7d9ff33a91",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-19T14:25:04.024Z_

I'll read all seven LaTeX section files for you in full.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b88883f-907f-4528-b3e6-08196cbf0ec2",
  "isSidechain": true,
  "agentId": "a5995f18396c1763e",
  "requestId": "req_011CbC5eUmsWGZv6xnxaWnEw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "345b7c06-1b1d-452b-9409-9ad02c841377",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_1_38fb0170",
  "sessionId": "356f6463-a842-4ea1-8de2-5e7d9ff33a91",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y3viE6Q8Zr2yDJLZwccJ11",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18486,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18486,
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

_source line 3 · 2026-05-19T14:25:04.286Z_

<details open><summary>🔧 Tool call — Read · `toolu_015Bf1bfVwPmLpZr52GtEURG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "345b7c06-1b1d-452b-9409-9ad02c841377",
  "isSidechain": true,
  "agentId": "a5995f18396c1763e",
  "requestId": "req_011CbC5eUmsWGZv6xnxaWnEw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5f028d9e-7c2b-40a2-9441-18aa23a11db4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_1_38fb0170",
  "sessionId": "356f6463-a842-4ea1-8de2-5e7d9ff33a91",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y3viE6Q8Zr2yDJLZwccJ11",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18486,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18486,
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

_source line 4 · 2026-05-19T14:25:04.293Z_

<details><summary>↩ Tool result · `toolu_015Bf1bfVwPmLpZr52GtEURG`</summary>

```text
1	\begin{abstract}
2	Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability, yet no systematic methodology exists for diagnosing \emph{what} drives routing decisions. We introduce an episode-level counterfactual framework that decomposes routing signal into death-avoidance and non-death components. Applied to ScienceWorld (11 task types, 245 episodes, Qwen2.5-7B-Instruct), \textbf{78.9\% of non-tie routing labels} arise from death asymmetry: the internal strategy's hallucination-induced failures trigger catastrophic agent death, while the deterministic strategy survives. This death dominance resists four representative intervention axes spanning retry, self-correction, $10{\times}$ parameter scaling, and action-space restriction; all reduce death rates yet none closes the gap to deterministic safety. A MATH evaluation ($N{=}795$, $p = 0.81$) confirms no routing signal without catastrophic failure. The framework reveals when catastrophic failure makes routing degenerate and when learned routers may add value.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5f028d9e-7c2b-40a2-9441-18aa23a11db4",
  "isSidechain": true,
  "promptId": "142cd10d-776d-4d99-8e0d-47ee9ec75758",
  "agentId": "a5995f18396c1763e",
  "type": "user",
  "uuid": "538d8cf5-be03-44ff-b0f3-f62c21db038d",
  "sourceToolAssistantUUID": "5f028d9e-7c2b-40a2-9441-18aa23a11db4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_1_38fb0170",
  "sessionId": "356f6463-a842-4ea1-8de2-5e7d9ff33a91",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T14:25:04.673Z_

<details open><summary>🔧 Tool call — Read · `toolu_0165aoXyr98merkrkvG3xsLg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "538d8cf5-be03-44ff-b0f3-f62c21db038d",
  "isSidechain": true,
  "agentId": "a5995f18396c1763e",
  "requestId": "req_011CbC5eUmsWGZv6xnxaWnEw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4aa24488-4041-4bca-97ac-b10d8a90e542",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_1_38fb0170",
  "sessionId": "356f6463-a842-4ea1-8de2-5e7d9ff33a91",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y3viE6Q8Zr2yDJLZwccJ11",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18486,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18486,
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

_source line 6 · 2026-05-19T14:25:04.679Z_

<details><summary>↩ Tool result · `toolu_0165aoXyr98merkrkvG3xsLg`</summary>

```text
1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	A Qwen2.5-7B-Instruct agent navigating ScienceWorld \cite{scienceworld-2022}, a text-based science simulation with 30 task types, faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \emph{when should an agent route computation externally versus reasoning internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision.
7	Toolformer \cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.
8	More recent adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026} or model tiers \cite{mtrouter-2026}.
9	Concurrent analyses of when and whether to invoke tools~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026} further presuppose diverse routing signals.
10	The shared assumption is that routing signal stems from diverse sources (accuracy, latency, capability matching) and that a learned router can exploit this signal to improve over any fixed strategy.
11	But no prior work has systematically decomposed what drives routing decisions in interactive environments. Without such a decomposition, the field cannot distinguish settings where diverse routing signals justify learned routers from those where a single failure mode dominates and a fixed strategy suffices.
12	
13	We propose a \emph{formal diagnostic framework} for answering this question. The framework comprises (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), a penalty-dependent metric that decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95), a penalty-independent finding that holds regardless of how death is penalized. Under ScienceWorld's specific penalty structure ($P{=}100$), the penalty-weighted DAF reaches $90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$), consistent with the predicted value from observed $\delta{=}0.265$ and $P{=}100$.
14	The internal strategy's hallucination-induced failures trigger catastrophic agent death (a $-100$ penalty), while the deterministic strategy survives the same episodes.
15	Once death episodes are removed, the performance gap collapses to $\Delta_{\text{nd}} = +2.84$. A per-task consistency check ($r = 0.97$) confirms that the near-perfect correlation is a mathematical consequence of death dominance when $P$ is constant (\S\ref{sec:death-decomp}).
16	
17	This framework addresses a methodological gap: per-step oracle comparison degenerates under sparse rewards (97.4\% of ScienceWorld steps produce identical scores regardless of modality; \S\ref{sec:collection}), and keyword-based heuristics fail structurally (\S\ref{sec:baselines}). Our counterfactual approach runs complete episodes under pure-internal (ReAct \cite{react-2023}) and pure-deterministic strategies, then compares episode outcomes. The framework applies to any environment with controllable modality comparison and binary catastrophic outcomes.
18	
19	Two cross-context checks probe the specificity of this finding.
20	First, a MATH Level~4--5 evaluation ($N{=}795$ problems, code interpreter as deterministic modality) confirms no routing signal without catastrophic failure: internal reasoning and code interpretation achieve near-identical accuracy ($73.5\%$ vs.\ $73.0\%$, $p = 0.81$).
21	Second, a cross-model replication with Llama-3.1-8B-Instruct (11 task types, $N{=}220$) shows death dominance replicates across model families with direction consistency 10/10 ($+30.0$~pp vs.\ $+26.5$~pp for Qwen; \S\ref{sec:cross-model}).
22	Four intervention axes test whether death dominance is fragile: retry, Reflexion~\citep{reflexion-2023}, $10{\times}$ parameter scaling (72B), and action-space restriction all reduce death rates, yet none closes the gap to deterministic safety (\S\ref{sec:agent-improvement}). Action filtering (blocking the fatal action during exploration) and 72B scaling yield the strongest reductions yet still leave ${\geq}$12~pp residual gaps, results not predictable from the penalty structure alone.
23	An exploratory router (Qwen3 LoRA, 0.6B--4B) yields flat step-level balanced accuracy ($56$--$59\%$); at episode level, only 4B exceeds the always-deterministic baseline (\S\ref{sec:router-diagnostic}).
24	
25	Our contributions are:
26	\begin{enumerate}
27	    \item \textbf{An episode-level counterfactual diagnostic framework} for decomposing routing signal, with dual penalty-independent and penalty-dependent metrics and router training as a diagnostic probe (\S\ref{sec:collection}--\ref{sec:daf}, \S\ref{sec:router-diagnostic}).
28	
29	    \item \textbf{Evidence that death dominance resists standard interventions}: 78.9\% of non-tie labels arise from death asymmetry; four representative axes (retry, self-correction, $10{\times}$ scaling, action-space restriction) all fail to close the gap, with action filtering and 72B scaling providing the strongest yet insufficient reductions (\S\ref{sec:death-decomp}--\ref{sec:agent-improvement}).
30	
31	    \item \textbf{Cross-environment boundary probes}: MATH ($p = 0.81$) confirms the predicted null; ALFWorld identifies information asymmetry; a Llama-3.1-8B replication ($N{=}220$) confirms cross-model consistency with 10/10 direction consistency (\S\ref{sec:math-contrast}--\ref{sec:cross-model}).
32	\end{enumerate}
33	
34	
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4aa24488-4041-4bca-97ac-b10d8a90e542",
  "isSidechain": true,
  "promptId": "142cd10d-776d-4d99-8e0d-47ee9ec75758",
  "agentId": "a5995f18396c1763e",
  "type": "user",
  "uuid": "72b5f3c0-6f91-4256-852f-324dbe18a1e9",
  "sourceToolAssistantUUID": "4aa24488-4041-4bca-97ac-b10d8a90e542",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_1_38fb0170",
  "sessionId": "356f6463-a842-4ea1-8de2-5e7d9ff33a91",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T14:25:04.880Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MSFs1X6isTkVj18BhwvGUs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72b5f3c0-6f91-4256-852f-324dbe18a1e9",
  "isSidechain": true,
  "agentId": "a5995f18396c1763e",
  "requestId": "req_011CbC5eUmsWGZv6xnxaWnEw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b7254102-affb-486d-ae06-76492bd68b6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_1_38fb0170",
  "sessionId": "356f6463-a842-4ea1-8de2-5e7d9ff33a91",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y3viE6Q8Zr2yDJLZwccJ11",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18486,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18486,
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

_source line 8 · 2026-05-19T14:25:04.886Z_

<details><summary>↩ Tool result · `toolu_01MSFs1X6isTkVj18BhwvGUs`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically (Appendix~\ref{app:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
5	
6	\subsection{Problem Setup}
7	\label{sec:problem-setup}
8	
9	Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modalities $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\cite{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic} (${\tt det}$), where the agent receives ground-truth observations from the environment simulator at each step. A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \mathcal{M}$ selects which modality to use at each step; our analysis investigates what signal is available to learn $\rho$. A reasoning-depth ablation ($n{=}120$) found no significant difference ($p > 0.26$; Appendix~\ref{app:ablations}).
10	
11	\subsection{Counterfactual Episode Collection}
12	\label{sec:collection}
13	
14	Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \cite{scienceworld-2022}, 97.4\% of steps produce identical intermediate scores regardless of modality (5{,}726 of 5{,}878 steps across 11 prescreened task types), yielding no per-step routing signal. The 97.4\% tie rate arises because ScienceWorld assigns rewards only at episode termination; intermediate steps update environment state but do not change the score, so a per-step oracle can only distinguish strategies through downstream consequences visible at episode end. Episode-level comparison is therefore the principled granularity for sparse-reward environments, not a fallback from per-step analysis: it directly measures whether one strategy produces better terminal outcomes than the other, bypassing the uninformative intermediate steps entirely.
15	
16	\paragraph{Pure-strategy trajectories.}
17	For a task instance $t$ and modality $m \in \mathcal{M}$, a \emph{pure-strategy trajectory} is the complete episode obtained by applying modality $m$ at every step:
18	\begin{equation}
19	    \tau_m^{(t)} = (o_1, a_1, o_2, a_2, \ldots, o_T, a_T)
20	\end{equation}
21	where $T \leq T_{\max}$ is the episode length (capped at $T_{\max} = 30$ steps). Both trajectories $\tau_{\tt int}^{(t)}$ and $\tau_{\tt det}^{(t)}$ are executed under identical initial conditions (same random seed, same task variation), so performance differences arise solely from the modality choice.
22	
23	Each trajectory $\tau$ yields a terminal score $s(\tau) \in \mathbb{Z}$ and a death indicator $d(\tau) \in \{0, 1\}$. When the agent dies ($d = 1$), the environment imposes a penalty: $s(\tau) = -P$ where $P > 0$ ($P = 100$ in ScienceWorld). The episode pair produces a tuple:
24	\begin{multline}
25	    \bigl(s^{\tt int}, s^{\tt det}, d^{\tt int}, d^{\tt det}\bigr) \triangleq \\
26	    \bigl(s(\tau_{\tt int}),\, s(\tau_{\tt det}),\, d(\tau_{\tt int}),\, d(\tau_{\tt det})\bigr)
27	\end{multline}
28	
29	We use Qwen2.5-7B-Instruct~\citep{qwen25-2024} (vLLM) on ScienceWorld \cite{scienceworld-2022}, a text-based environment spanning 30 task types with a $-100$ death penalty. After prescreening, we collect 245 episode pairs across 11 task types (20--40 per type). The framework is applicable to any environment where paired episodes under two modalities can be collected with binary success/failure indicators. We apply it unchanged to ALFWorld and MATH in \S\ref{sec:math-contrast}--\ref{sec:cross-env}.
30	
31	\subsection{Episode-Level Labeling}
32	\label{sec:labeling}
33	
34	We define a labeling function $L$ that maps a counterfactual pair to a routing preference:
35	\begin{multline}
36	    L\!\bigl(\tau_{\tt int}^{(t)}, \tau_{\tt det}^{(t)}\bigr) \;\rightarrow \\
37	    \ell \in \{{\tt det\text{-}pref},\; {\tt int\text{-}pref},\; {\tt no\text{-}pref}\}
38	\end{multline}
39	
40	The labeling function is \emph{death-aware}: it prioritizes survival over score, then compares scores among same-status episodes (Algorithm~\ref{alg:labeling}; Appendix~\ref{app:labeling}). ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. Figure~\ref{fig:pipeline} illustrates the overall pipeline; label distributions are reported in \S\ref{sec:death-decomp}.
41	
42	\begin{figure}[t]
43	\centering
44	\includegraphics[width=\columnwidth]{figures/pipeline_overview.pdf}
45	\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\ref{alg:labeling}.}
46	\label{fig:pipeline}
47	\end{figure}
48	
49	\subsection{Death Avoidance Factor}
50	\label{sec:daf}
51	
52	To quantify the contribution of death avoidance to routing signal, we decompose the mean score gap between strategies. Let $\delta = \mathbb{E}[d^{\tt int}] - \mathbb{E}[d^{\tt det}]$ denote the death-rate differential and $\Delta_{\text{nd}}$ the mean score gap restricted to episodes where neither strategy dies. Partitioning episodes by death status, death-asymmetric episodes (where only one strategy dies) contribute a per-episode gap of $P + \bar{s}_{\text{surv}}$, where $\bar{s}_{\text{surv}}$ is the surviving strategy's mean score; when $\bar{s}_{\text{surv}} \ll P$ (in our data, $\bar{s}_{\text{surv}} = 0.87$, or $0.9\%$ of $P$), these episodes contribute ${\approx}\,\delta P$ in aggregate. The full gap thus decomposes as:
53	\begin{equation}
54	    \Delta_{\text{full}} \approx \underbrace{\delta \cdot P}_{\text{death contribution}} + \Delta_{\text{nd}}
55	\end{equation}
56	The approximation residual is $29.60 - 29.37 = 0.23$ ($0.8\%$ of $\Delta_{\text{full}}$).
57	
58	We define the Death Avoidance Factor (DAF) as the fraction of the full score gap attributable to death avoidance:
59	\begin{equation}
60	    \text{DAF} = 1 - \frac{\Delta_{\text{nd}}}{\Delta_{\text{full}}} \approx \frac{\delta P}{\delta P + \Delta_{\text{nd}}}
61	\end{equation}%
62	\footnote{When $\Delta_{\text{nd}} < 0$ (deterministic strategy scores lower than internal on non-death episodes), DAF exceeds 1; death avoidance then overcompensates for a non-death disadvantage.}
63	
64	Since DAF $= \delta P / (\delta P + \Delta_{\text{nd}})$, it increases monotonically with $P$, a mathematical consequence rather than an empirical finding. We therefore report both DAF at the environment default ($P{=}100$) and the penalty-independent death-asymmetry label fraction as complementary metrics.
65	
66	\paragraph{Statistical inference.}
67	We quantify uncertainty via episode-level bootstrap resampling ($B = 10{,}000$). Each resample draws $N = 245$ episodes with replacement, recomputes all metrics, and derives percentile-based 95\% CIs. We resample at the episode level (not the step level) because the episode is the unit of counterfactual comparison. Penalty sensitivity analysis across hypothetical $P$ values is in Appendix~\ref{app:penalty}.
68	
69	We also measure whether death-avoidance signal is concentrated in a few task types via a Signal Concentration Index (SCI $\in [0, 1]$; Appendix~\ref{app:sci}), reported in \S\ref{sec:death-decomp}.
70	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7254102-affb-486d-ae06-76492bd68b6a",
  "isSidechain": true,
  "promptId": "142cd10d-776d-4d99-8e0d-47ee9ec75758",
  "agentId": "a5995f18396c1763e",
  "type": "user",
  "uuid": "05fa1a40-5473-4337-a9f8-228f9a408b9d",
  "sourceToolAssistantUUID": "b7254102-affb-486d-ae06-76492bd68b6a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_1_38fb0170",
  "sessionId": "356f6463-a842-4ea1-8de2-5e7d9ff33a91",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T14:25:05.096Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VkAKiFdyZsiknF1758N38B`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05fa1a40-5473-4337-a9f8-228f9a408b9d",
  "isSidechain": true,
  "agentId": "a5995f18396c1763e",
  "requestId": "req_011CbC5eUmsWGZv6xnxaWnEw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e1b81844-1733-4bea-976e-3d26f9d0ddf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_1_38fb0170",
  "sessionId": "356f6463-a842-4ea1-8de2-5e7d9ff33a91",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y3viE6Q8Zr2yDJLZwccJ11",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18486,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18486,
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

_source line 10 · 2026-05-19T14:25:05.111Z_

<details><summary>↩ Tool result · `toolu_01VkAKiFdyZsiknF1758N38B`</summary>

```text
1	\section{Experiments}
2	
3	We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types (63\%) lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). This scope limits generalizability: conclusions apply to the included subset, not to all ScienceWorld tasks. An anti-cherry-picking analysis confirms that death dominance holds in 18 of these 19 types, with a mean $\Delta\text{DR} = +38.2$\,pp exceeding the included tasks' $+28.7$\,pp (Appendix~\ref{app:per-task}).
4	
5	\subsection{Death Avoidance Decomposition}
6	\label{sec:death-decomp}
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=0.85\columnwidth]{figures/fig1_daf_scatter.pdf}
11	\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$, $p < 10^{-6}$, $n = 11$ task types. This near-perfect correlation is structurally implied by the decomposition (\S\ref{sec:death-decomp}); see text for interpretation.}
12	\label{fig:decomposition}
13	\end{figure}
14	
15	Across 245 episodes, $\Delta_{\text{full}} = +29.60$; excluding death episodes, $\Delta_{\text{nd}} = +2.84$, yielding DAF $= 90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$, episode-level bootstrap, $B{=}10{,}000$; at the default $P{=}100$). The penalty-independent death-asymmetry label fraction is 78.9\% (75 of 95 non-tie labels). Given observed $\delta = 0.265$ and $P = 100$, the predicted DAF $= \delta P / (\delta P + \Delta_{\text{nd}}) = 26.5 / 29.37 \approx 90.3\%$, closely matching the observed value; DAF is thus a derived quantity once $\delta$, $P$, and $\Delta_{\text{nd}}$ are known, while the 78.9\% label fraction is the penalty-independent empirical finding. Of these 75, 54 (72.0\%) reduce to ties when the death penalty is removed entirely: in those episodes, both modalities score zero without death, so the only reason one strategy outscored the other was avoiding the $-100$ penalty. Death avoidance is not merely the dominant but often the \emph{sole} discriminating signal between modalities. The remaining 21 death-asymmetry labels involve episodes where the surviving strategy also earned positive score, but the death penalty still accounts for the majority of the score gap. At $P{=}0$, the 54 sole-signal labels reduce to ties, leaving 41 non-tie labels of which 21 (51.2\%) still involve death asymmetry; the labeling function itself is penalty-independent (Algorithm~\ref{alg:labeling}), but the practical routing value of death avoidance requires $P > 0$.
16	
17	\paragraph{Per-task correlation structure.}
18	The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic (2.6$\times$), consistent with the internal strategy's reliance on self-generated observations that compound prediction errors across steps. Per-task, death rate differential correlates with $\Delta_{\text{full}}$ ($r = 0.97$, $p < 10^{-6}$; Figure~\ref{fig:decomposition}). Since $P$ is constant across all task types, $\Delta_{\text{full}} = P \cdot \delta + \Delta_{\text{nd}}$ makes $\Delta_{\text{full}}$ a linear function of $\delta$ with residual $\Delta_{\text{nd}}$; when DAF $\rightarrow 1$, this residual vanishes and $r \rightarrow 1$ by construction. The near-perfect correlation is therefore a mathematical consequence of death dominance, not an independent empirical finding. We retain it as an internal consistency check. The correlation drops below significance at $P \leq 25$ (Appendix~\ref{app:penalty}). Of 245 episodes, 86 are \texttt{det\_preferred}, 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preference}.
19	
20	\paragraph{Signal concentration and binary structure.}
21	The Signal Concentration Index (SCI $= 0.2147$; Appendix~\ref{app:sci}) confirms low concentration: the top-3 task types account for only $39.8\%$ of total death-rate differential. The aggregate 78.9\% reflects a per-task binary structure: all 10 death-prone task types produce 100\% death-asymmetry labels, while \texttt{find-non-living-thing} (zero deaths, $\Delta = +9.58$ from non-death scores) produces 0\%. The framework thus diagnoses a binary property (``is this environment death-dominated?'') rather than a continuous routing signal. Removing \texttt{find-non-living-thing} raises the label fraction to 100\% and DAF to 96.8\% (Appendix~\ref{app:loto-daf}).
22	
23	\paragraph{Sensitivity and seed robustness.}
24	Episode-level bootstrap ($B = 10{,}000$) yields 95\% CI $[81.6\%, 98.8\%]$ for DAF (Cohen's $d = 3.02$); leave-one-task-out analysis confirms stability (DAF range: 75.9\%--78.9\%; Appendix~\ref{app:loto-daf}). An independent seed replication ($N{=}220$) yields DAF $= 89.7\%$, within 0.7~pp of the primary analysis (Appendix~\ref{app:seed-robustness}). Cluster-robust inference with $K{=}11$ task-type clusters ($p < 0.001$; primary CIs are episode-level, cluster CIs serve as sensitivity analysis) and 28-task directional consistency (100\%) confirm significance (Appendices~\ref{app:wild-cluster}--\ref{app:per-task-ci}).
25	
26	\subsection{Multi-Model Validation}
27	\label{sec:cross-model}
28	
29	A Llama-3.1-8B-Instruct~\citep{llama3-2024} cross-model replication across all 11 task types ($N{=}220$) confirms that death dominance replicates across model families: internal death rate $41.4\%$ vs.\ deterministic $11.4\%$ (death-rate differential $+30.0$~pp), with direction consistency 10/10 on death-prone tasks, 83 deterministic-preferred, 3 internal-preferred (1.4\%, all death-asymmetry reversals), and 134 no-preference labels.
30	Both models exhibit nearly identical internal vulnerability (${\sim}$42\%: Qwen $42.9\%$, Llama $41.4\%$), confirming that death-prone failure is structurally determined; the differential magnitude varies ($+26.5$~pp Qwen, $+30.0$~pp Llama) because deterministic strategy safety is model-dependent ($16.3\%$ vs.\ $11.4\%$).
31	\texttt{identify-life-stages-1} shows cross-model precision matching ($55\%$/$10\%$/$+45$~pp in both models).
32	\texttt{find-non-living-thing} shows zero deaths in both models, consistent with its majority-class answer distribution (\S\ref{sec:discussion}). Both models are in the 7--8B range; $10{\times}$ scaling (\S\ref{sec:agent-improvement}) confirms that death dominance persists across capability levels (Appendix~\ref{app:cross-model}).
33	
34	\subsection{Agent Improvement Baselines}
35	\label{sec:agent-improvement}
36	
37	\begin{table}[t]
38	\centering
39	\small
40	\begin{tabular}{@{}lrr@{}}
41	\toprule
42	Condition & Death\% & $N$ \\
43	\midrule
44	Single-trial baseline & 42.9 & 245 \\
45	Reflexion ($3{\times}$) & 31.4 & 220 \\
46	Qwen2.5-72B ($10{\times}$) & 30.6 & 255 \\
47	Deterministic baseline & 16.3 & 245 \\
48	\midrule
49	\multicolumn{3}{@{}l}{\textit{10 death-prone tasks only:}} \\
50	Death-prone baseline & 48.0 & 200 \\
51	Retry ($5{\times}$) & 43.5 & 200 \\
52	\bottomrule
53	\end{tabular}
54	\caption{Internal-strategy death rates under agent improvement methods. Top: all 11 tasks (72B: independently collected at both internal and deterministic). Bottom: 10 death-prone tasks (\texttt{find-non-living-thing} excluded, 0\% death at all scales). All interventions reduce death rate but none approaches deterministic-level safety.}
55	\label{tab:agent-improvement}
56	\end{table}
57	
58	We test whether agent-level improvement reduces death dominance (Table~\ref{tab:agent-improvement}). Retry ($N{=}5$ attempts without self-correction) yields marginal reduction on death-prone tasks ($43.5\%$ vs.\ $48.0\%$ baseline, $\Delta = -4.5$~pp). Reflexion~\citep{reflexion-2023} (verbal self-reflection between trials) reduces death to 31.4\% across all 11 tasks by rescuing 29.3\% of first-trial deaths, but the gap to deterministic remains 15.1~pp; on the 10 death-prone tasks, Reflexion achieves ${\sim}$35\%. Under Reflexion ($N{=}3$, matched-episode analysis), $\Delta_{\text{nd}} = -0.47$, yielding DAF $> 100\%$: the deterministic advantage is entirely attributable to death avoidance, and in non-death episodes the self-correcting agent slightly outperforms the deterministic baseline. Scaling to Qwen2.5-72B ($10{\times}$ parameters; both internal and deterministic strategies independently collected at 72B, 255 episodes across all 11 task types) reduces death rate to $30.6\%$. The 72B deterministic strategy achieves $2.75\%$ death rate ($\Delta\text{DR} = +27.8$~pp), and $\Delta_{\text{nd}} = +2.28$, yielding DAF $= 92.4\%$ (7B: $90.4\%$); scaling lowers death rate but leaves death dominance intact.
59	
60	\paragraph{Dose-response analysis.}
61	We extend both interventions to $N{=}5$ trials on death-prone tasks ($n{=}200$; Figure~\ref{fig:dose-response}). Retry is nearly flat ($48.0\% \to 43.5\%$, $\Delta = -4.5$~pp over five trials). Reflexion drops steeply to $34.0\%$ at $N{=}3$ ($\Delta = -13.5$~pp, $p < 0.005$) then plateaus ($34$--$36.5\%$ for $N \geq 3$, pairwise $p > 0.5$). Retry's per-trial conditional death rate stays constant at ${\sim}48\%$; Reflexion's declines to ${\sim}31\%$ by Trial~3 (per-task breakdown in Appendix~\ref{app:dose-response}).
62	
63	\begin{figure}[t]
64	\centering
65	\includegraphics[width=\columnwidth]{figures/dose_response.pdf}
66	\caption{Death rate as a function of trial count ($N$) for Retry and Reflexion on 10 death-prone tasks ($n{=}200$). Retry (blue) is nearly flat; Reflexion (red) drops steeply through $N{=}3$ then plateaus. Horizontal lines: 72B scaling baseline ($30.6\%$, all 11 tasks) and deterministic baseline ($16.3\%$). Error bands: Wilson 95\% CIs.}
67	\label{fig:dose-response}
68	\end{figure}
69	
70	\subsection{Cross-Environment Boundary Probes}
71	\label{sec:math-contrast}
72	\label{sec:cross-env}
73	
74	We evaluate two additional environments as boundary probes (Appendix~\ref{app:cross-env-details}). ``Deterministic'' denotes qualitatively different modalities per environment: ScienceWorld uses an oracle simulator with ground-truth state, MATH uses a Python code interpreter, and ALFWorld uses admissible-action enumeration. These are not equivalent computation modes; results probe framework applicability rather than replicate findings.
75	
76	\paragraph{MATH.} On MATH Level~4--5~\citep{math-2021} ($N{=}795$, code interpreter as deterministic modality), internal reasoning and code interpretation achieve near-identical accuracy ($73.5\%$ vs.\ $73.0\%$, McNemar $p = 0.81$, 95\% CI $[-2.6, +3.6]$~pp), with balanced labels (107 vs.\ 95, 74.6\% no-preference). Without catastrophic failure, no routing signal emerges.
77	
78	\paragraph{ALFWorld.} ALFWorld~\citep{alfworld-2021} (6 task types, 135 games) provides the deterministic strategy with admissible actions, an information asymmetry rather than a computation mode switch. The success rate gap is $27.4\%$ vs.\ $3.0\%$ (35 det-preferred, 2 int-preferred, 98 no-preference). The deterministic advantage stems from this information gap, a qualitatively different mechanism that the framework diagnoses without modification.
79	
80	\subsection{Baselines}
81	\label{sec:baselines}
82	
83	\begin{table}[t]
84	\centering
85	\small
86	\resizebox{\columnwidth}{!}{%
87	\begin{tabular}{@{}lccc@{}}
88	\toprule
89	Strategy & Score & 95\% CI & Death \% \\
90	\midrule
91	Always-Internal & $-39.07$ & [$-46.40$, $-32.27$] & 42.9 \\
92	Always-Deterministic & $-9.47$ & [$-14.71$, $-4.29$] & 16.3 \\
93	Random & $-22.38$ & [$-28.67$, $-15.75$] & 27.8 \\
94	Oracle & $-6.58$ & [$-11.54$, $-1.70$] & 14.3 \\
95	\midrule
96	Trained Router$^\dagger$ & $-10.70$ & [$-16.33$, $-5.27$] & 17.6 \\
97	\bottomrule
98	\end{tabular}}
99	\caption{Episode-weighted mean scores on ScienceWorld (11 tasks, 245 episodes). $\dagger$\,Single random seed (42) per episode pair; see Appendix~\ref{app:seed-robustness} for 8-seed robustness analysis.}
100	\label{tab:baselines}
101	\end{table}
102	
103	Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points. The oracle improves only to $-6.58$, with 96.3\% of decisions matching always-deterministic, an \emph{oracle degeneracy}: the optimal routing policy closely resembles unconditional deterministic computation.
104	
105	\subsection{Router Training as Diagnostic Probe}
106	\label{sec:router-diagnostic}
107	
108	We probe whether counterfactual labels can train a step-level router as a diagnostic of label informativeness. The oracle margin (2.89 points) caps routing upside; ${\sim}27.7\%$ of step-level labels are misaligned with episode-level assignments, further limiting learnability. An implicit router (Qwen3, LoRA; Appendix~\ref{app:router-details}) trained at three scales (0.6B, 1.7B, 4B) with 4-seed configurations shows flat step-level balanced accuracy ($56$--$59\%$, within seed variance). At episode level, only 4B exceeds always-deterministic ($59.0 \pm 1.9\%$, $p < 0.005$; Appendix~\ref{app:ablations}); 0.6B and 1.7B remain at or below chance. The multi-step nature of routing (10--50 actions with compounding state uncertainty) creates inherent label noise between step-level decisions and episode-level outcomes.
109	
110	\paragraph{End-to-end deployment.} The 4B router deployed end-to-end ($N{=}245$) scores $-12.03$ (95\% CI: $[-17.82, -6.45]$), not exceeding always-deterministic ($-9.47$). Paraphrase-based augmentation ($25\%$--$800\%$) provides no improvement; the $3.7\%$ internal-preferred base rate makes real-data collection expensive (Appendices~\ref{app:seed-robustness}--\ref{app:ablations}).
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1b81844-1733-4bea-976e-3d26f9d0ddf9",
  "isSidechain": true,
  "promptId": "142cd10d-776d-4d99-8e0d-47ee9ec75758",
  "agentId": "a5995f18396c1763e",
  "type": "user",
  "uuid": "7902b0e4-57d0-4002-a449-fc3571541cd3",
  "sourceToolAssistantUUID": "e1b81844-1733-4bea-976e-3d26f9d0ddf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_1_38fb0170",
  "sessionId": "356f6463-a842-4ea1-8de2-5e7d9ff33a91",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T14:25:05.304Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RJLipoJ1YhfEF82BmsZF6e`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7902b0e4-57d0-4002-a449-fc3571541cd3",
  "isSidechain": true,
  "agentId": "a5995f18396c1763e",
  "requestId": "req_011CbC5eUmsWGZv6xnxaWnEw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "72315033-ccfd-457a-be8e-b7e82085a49f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_1_38fb0170",
  "sessionId": "356f6463-a842-4ea1-8de2-5e7d9ff33a91",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y3viE6Q8Zr2yDJLZwccJ11",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18486,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18486,
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

_source line 12 · 2026-05-19T14:25:05.311Z_

<details><summary>↩ Tool result · `toolu_01RJLipoJ1YhfEF82BmsZF6e`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Tool Use and External Computation in LLMs.}
4	A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}, spanning several functional categories.
5	\emph{Self-supervised} approaches learn tool invocation from loss signals: Toolformer \cite{toolformer-2023} inserts API calls filtered by perplexity reduction; ToolACE \cite{toolace-2025} curates synthetic data for function-calling accuracy.
6	\emph{Token-level} methods embed tools into the model vocabulary: ToolkenGPT \cite{toolkengpt-2023} represents tools as special tokens resolved at inference.
7	\emph{Task-level} decomposition routes subtasks to specialized modules: ART \cite{art-2023} generates tool-augmented programs; Chameleon \cite{chameleon-2023} composes heterogeneous modules per subtask.
8	\emph{RL-based} methods learn routing policies from reward: ReTool \cite{retool-2025} discovers when code execution is preferable to chain-of-thought.
9	All focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
10	Recent concurrent work sharpens this question: \citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect where LLMs default to external tools even when internal knowledge suffices, finding that tool overuse correlates with model uncertainty rather than task difficulty. \citet{when2tool-2026} show tool-call decisions are encoded in hidden states before reasoning, \citet{tool-use-tax-2026} quantify a ``tool-use tax,'' and \citet{to-call-or-not-2026} propose a necessity, utility, and affordability framework. Our decomposition provides environment-grounded evidence: in ScienceWorld, 78.9\% of routing labels trace to catastrophic-failure prevention.
11	
12	\paragraph{Adaptive Computation and Routing.}
13	CogRouter \cite{cogrouter-2026} adapts reasoning depth per step, ARES \cite{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \cite{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \cite{mtrouter-2026} addresses multi-turn routing.
14	RouteLLM \citep{routellm-2024} learns routers from preference data to select between strong and weak models.
15	These optimize \emph{how} to route; we reveal \emph{why} routing helps: in interactive environments, the dominant signal is catastrophic-failure avoidance.
16	
17	\paragraph{Counterfactual Evaluation in RL.}
18	Prior work generates counterfactual explanations for RL agents by perturbing individual actions within a fixed policy \citep{olson2021counterfactual, gajcin2023counterfactual, amitai2024explaining}.
19	Our approach differs in both purpose and granularity: we execute two complete episodes under different routing strategies, producing prospective paired comparisons that isolate routing signal \emph{before} any router is trained.
20	
21	\paragraph{LLM Agent Environments and Reasoning.}
22	ScienceWorld \cite{scienceworld-2022} serves as our primary testbed; Inner Monologue \cite{huang2022inner} grounds LLM planning in embodied feedback; Voyager \cite{wang2023voyager} demonstrates open-ended LLM agents; ALFWorld \cite{alfworld-2021} provides a complementary household environment; AgentBench \cite{agentbench-2024} offers systematic evaluation. \citet{zhou2024webarena} document common failure modes (premature termination, hallucinated actions) in web-based agents, consistent with our finding that state hallucination is the primary internal-strategy failure mechanism. ReAct \cite{react-2023} serves as our internal baseline; Reflexion \cite{reflexion-2023} extends this with verbal self-reflection; LATS \cite{lats-2024} adds tree search. SelfCheckGPT \cite{selfcheckgpt-2023} detects unreliable LLM outputs; our work shows that in interactive environments, such unreliability manifests as catastrophic death.
23	
24	\paragraph{Safe RL.}
25	Safe RL methods \citep{garcia2015comprehensive,tamar2015cvar,achiam2017cpo,crpo-2021} enforce constraints in MDPs; SafeRoute \citep{saferoute-2025} applies adaptive model selection for safety guardrails. Our diagnostic shows modality routing already functions as an implicit safety mechanism in environments with catastrophic failure.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72315033-ccfd-457a-be8e-b7e82085a49f",
  "isSidechain": true,
  "promptId": "142cd10d-776d-4d99-8e0d-47ee9ec75758",
  "agentId": "a5995f18396c1763e",
  "type": "user",
  "uuid": "757402ba-5de0-4c6f-8f7f-723d35383cb9",
  "sourceToolAssistantUUID": "72315033-ccfd-457a-be8e-b7e82085a49f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_1_38fb0170",
  "sessionId": "356f6463-a842-4ea1-8de2-5e7d9ff33a91",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T14:25:05.780Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LCSd6Detbs7eJGLKAxkpv4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "757402ba-5de0-4c6f-8f7f-723d35383cb9",
  "isSidechain": true,
  "agentId": "a5995f18396c1763e",
  "requestId": "req_011CbC5eUmsWGZv6xnxaWnEw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "70543645-7ad0-4c6b-8f7b-4181fcf7e219",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_1_38fb0170",
  "sessionId": "356f6463-a842-4ea1-8de2-5e7d9ff33a91",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y3viE6Q8Zr2yDJLZwccJ11",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18486,
      "cache_read_input_tokens": 0,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18486
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 538,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18486,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18486,
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

_source line 14 · 2026-05-19T14:25:05.790Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JtLSeqgqWQVHjBwoDkZ5wc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70543645-7ad0-4c6b-8f7b-4181fcf7e219",
  "isSidechain": true,
  "agentId": "a5995f18396c1763e",
  "requestId": "req_011CbC5eUmsWGZv6xnxaWnEw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "67ce0e12-a3be-4a6b-bcf1-fb759a5cd941",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_1_38fb0170",
  "sessionId": "356f6463-a842-4ea1-8de2-5e7d9ff33a91",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y3viE6Q8Zr2yDJLZwccJ11",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18486,
      "cache_read_input_tokens": 0,
      "output_tokens": 538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18486
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 538,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18486,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18486,
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

_source line 15 · 2026-05-19T14:25:05.790Z_

<details><summary>↩ Tool result · `toolu_01LCSd6Detbs7eJGLKAxkpv4`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Why the router fails: task-type-level signal.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property (10 of 11 types carry death risk), but step-level features correlate weakly because death risk depends on multi-step state trajectories, not individual action semantics. The 4B router's episode-level improvement ($59.0\%$) without step-level gains ($56$--$59\%$, flat) confirms that capacity scaling captures task-type classification rather than generalizable features. Cross-task-type transfer to physical-science tasks yields chance-level accuracy (49.2\%, 95\% CI $[42.4\%, 55.9\%]$; Appendix~\ref{app:ablations}), and 7 of 11 task types contain only deterministic-preferred labels, making majority-class collapse a structural consequence of the label distribution.
6	
7	\paragraph{Non-triviality of death dominance.}
8	While death dominance itself follows from the penalty structure (\S\ref{sec:daf}), its resistance to intervention was not predictable a priori. Four representative axes spanning retry, self-correction, parameter scaling, and action-space restriction all fail to close the gap to deterministic safety (16.3\%): Retry ($43.5\%$ at $N{=}5$), Reflexion ($34.0\%$ at $N{=}3$, plateauing at $34$--$36.5\%$), $10{\times}$ scaling ($30.6\%$, 72B, $N{=}255$), and action-space filtering ($29.0\%$; Appendix~\ref{app:grounding-ablation}). Action filtering and 72B scaling yield the strongest reductions yet still leave ${\geq}$12~pp residual gaps. Reflexion and scaling converge to overlapping 95\% Wilson CIs ($[27.8\%, 40.8\%]$ and $[25.2\%, 36.5\%]$); this overlap suggests a shared bound from the lack of ground-truth state access. The oracle matches always-deterministic on 96.3\% of decisions (score improvement: 2.89 points), and even with perfect per-task death risk knowledge, threshold routing cannot outperform always-deterministic (Appendix~\ref{sec:threshold-routing}). More aggressive planning-based interventions (Tree-of-Thought backtracking~\citep{tot-2023}, process reward models) remain untested and may further reduce death rates; we characterize a ceiling for the tested intervention classes, not a universal bound.
9	
10	\paragraph{Anatomy of catastrophic failure.}
11	All 105 internal-strategy deaths trace to misuse of \texttt{focus on [object]}, the answer-submission action, as a general interaction command (taxonomy in Appendix~\ref{app:failure-modes}). The root cause is action-space grounding failure: agents parse task descriptions correctly but cannot ground understanding in valid primitives. The internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not different within-episode behavior (${\sim}5\%$ \texttt{focus on} rate in both). \texttt{find-non-living-thing}, the sole zero-death task, uses \texttt{focus on} more frequently than any death-prone task: non-living objects are the majority class, so indiscriminate submissions rarely trigger death; lethality is thus a joint function of action misuse and answer distribution. Direct grounding interventions reduce but do not eliminate vulnerability ($48.0\% \to 37.0\%$ via prompt warning; $\to 29.0\%$ via action-space filter), with ironic effects where warnings increased \texttt{focus on} salience on identification tasks (Appendix~\ref{app:grounding-ablation}).
12	
13	\paragraph{Practitioner decision framework.}
14	We formalize a three-stage diagnostic procedure (${\sim}$50-episode pilot $\to$ death-rate differential $\to$ death-label fraction) with concrete thresholds in Appendix~\ref{app:decision-framework}; retrospective validation confirms correct predictions for all four experimental conditions (Qwen-7B, Llama-8B, Qwen-72B, MATH). Our router training consumed ${\sim}$200 GPU-hours across 28 configurations without exceeding always-deterministic; this framework could have predicted that outcome from a 50-episode pilot at negligible cost.
15	
16	\paragraph{Pure-strategy gap.}
17	Our counterfactual labels derive from pure-strategy episodes, but a deployed router produces mixed trajectories whose state distributions differ from either pure strategy~\citep{dagger-2011}. The 4B router's end-to-end score ($-12.03$) falling below always-deterministic ($-9.47$) may partly reflect this distribution shift rather than label noise alone. Closing this gap requires on-policy data collection under the router's own mixed policy, which is expensive given the 3.7\% internal-preferred base rate (${\sim}1{,}350$ paired episodes for 50 minority-class samples).
18	
19	\paragraph{Framework applicability.}
20	The penalty-independent label fraction (78.9\%) is the primary diagnostic; DAF increases monotonically with $P$ (Appendix~\ref{app:penalty}). The framework requires paired modality episodes with binary catastrophic outcomes. Preliminary pilots on MiniHack~\citep{minihack-2021} navigation tasks (0\% death rate, no monster spawning) and Crafter~\citep{crafter-2022} (100\% death rate for both strategies) produced no death asymmetry, illustrating two boundary conditions: environments lacking a death mechanism yield no routing signal (consistent with the MATH null), while environments where no strategy avoids death lack exploitable asymmetry. The framework's diagnostic power requires an intermediate regime where strategy choice meaningfully affects survival; NetHack~\citep{nethack-2020} combat tasks, where permadeath interacts with strategy quality, remain the most direct replication target; recent benchmarks \citep{balrog-2025,netplay-2024} provide infrastructure.
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70543645-7ad0-4c6b-8f7b-4181fcf7e219",
  "isSidechain": true,
  "promptId": "142cd10d-776d-4d99-8e0d-47ee9ec75758",
  "agentId": "a5995f18396c1763e",
  "type": "user",
  "uuid": "ec5fee7f-3a13-49d3-8b71-3e356d5b6f0c",
  "sourceToolAssistantUUID": "70543645-7ad0-4c6b-8f7b-4181fcf7e219",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_1_38fb0170",
  "sessionId": "356f6463-a842-4ea1-8de2-5e7d9ff33a91",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T14:25:05.805Z_

<details><summary>↩ Tool result · `toolu_01JtLSeqgqWQVHjBwoDkZ5wc`</summary>

```text
1	\section{Conclusion}
2	
3	We presented a diagnostic framework for decomposing routing signal in modular LLM agents via episode-level counterfactual analysis. Applied to ScienceWorld (245 episodes, 11 task types), 78.9\% of non-tie routing labels arise from death asymmetry; agent improvement baselines (retry, self-correction, $10{\times}$ scaling, action-space restriction) confirm this is robust. Cross-domain contrasts support framework predictions: MATH shows no routing signal without catastrophic failure; ALFWorld identifies information asymmetry as an alternative mechanism. Future work should target environments with intermediate death regimes, such as NetHack~\citep{nethack-2020} combat tasks and Crafter~\citep{crafter-2022} with tuned difficulty, building on recent LLM agent benchmarks \citep{balrog-2025,netplay-2024}; evaluation with stronger backbones is another direct open direction.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "67ce0e12-a3be-4a6b-bcf1-fb759a5cd941",
  "isSidechain": true,
  "promptId": "142cd10d-776d-4d99-8e0d-47ee9ec75758",
  "agentId": "a5995f18396c1763e",
  "type": "user",
  "uuid": "2f322f0a-80a3-49dd-a147-5438f037c7e7",
  "sourceToolAssistantUUID": "67ce0e12-a3be-4a6b-bcf1-fb759a5cd941",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_1_38fb0170",
  "sessionId": "356f6463-a842-4ea1-8de2-5e7d9ff33a91",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-19T14:27:21.576Z_

## Complete Contents of Paper Section Files

### 1. abstract.tex

```latex
\begin{abstract}
Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability, yet no systematic methodology exists for diagnosing \emph{what} drives routing decisions. We introduce an episode-level counterfactual framework that decomposes routing signal into death-avoidance and non-death components. Applied to ScienceWorld (11 task types, 245 episodes, Qwen2.5-7B-Instruct), \textbf{78.9\% of non-tie routing labels} arise from death asymmetry: the internal strategy's hallucination-induced failures trigger catastrophic agent death, while the deterministic strategy survives. This death dominance resists four representative intervention axes spanning retry, self-correction, $10{\times}$ parameter scaling, and action-space restriction; all reduce death rates yet none closes the gap to deterministic safety. A MATH evaluation ($N{=}795$, $p = 0.81$) confirms no routing signal without catastrophic failure. The framework reveals when catastrophic failure makes routing degenerate and when learned routers may add value.
\end{abstract}
```

### 2. introduction.tex

```latex
\section{Introduction}

Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
A Qwen2.5-7B-Instruct agent navigating ScienceWorld \cite{scienceworld-2022}, a text-based science simulation with 30 task types, faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \emph{when should an agent route computation externally versus reasoning internally?}

Existing routing approaches frame this as a capability or efficiency decision.
Toolformer \cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.
More recent adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026} or model tiers \cite{mtrouter-2026}.
Concurrent analyses of when and whether to invoke tools~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026} further presuppose diverse routing signals.
The shared assumption is that routing signal stems from diverse sources (accuracy, latency, capability matching) and that a learned router can exploit this signal to improve over any fixed strategy.
But no prior work has systematically decomposed what drives routing decisions in interactive environments. Without such a decomposition, the field cannot distinguish settings where diverse routing signals justify learned routers from those where a single failure mode dominates and a fixed strategy suffices.

We propose a \emph{formal diagnostic framework} for answering this question. The framework comprises (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), a penalty-dependent metric that decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95), a penalty-independent finding that holds regardless of how death is penalized. Under ScienceWorld's specific penalty structure ($P{=}100$), the penalty-weighted DAF reaches $90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$), consistent with the predicted value from observed $\delta{=}0.265$ and $P{=}100$.
The internal strategy's hallucination-induced failures trigger catastrophic agent death (a $-100$ penalty), while the deterministic strategy survives the same episodes.
Once death episodes are removed, the performance gap collapses to $\Delta_{\text{nd}} = +2.84$. A per-task consistency check ($r = 0.97$) confirms that the near-perfect correlation is a mathematical consequence of death dominance when $P$ is constant (\S\ref{sec:death-decomp}).

This framework addresses a methodological gap: per-step oracle comparison degenerates under sparse rewards (97.4\% of ScienceWorld steps produce identical scores regardless of modality; \S\ref{sec:collection}), and keyword-based heuristics fail structurally (\S\ref{sec:baselines}). Our counterfactual approach runs complete episodes under pure-internal (ReAct \cite{react-2023}) and pure-deterministic strategies, then compares episode outcomes. The framework applies to any environment with controllable modality comparison and binary catastrophic outcomes.

Two cross-context checks probe the specificity of this finding.
First, a MATH Level~4--5 evaluation ($N{=}795$ problems, code interpreter as deterministic modality) confirms no routing signal without catastrophic failure: internal reasoning and code interpretation achieve near-identical accuracy ($73.5\%$ vs.\ $73.0\%$, $p = 0.81$).
Second, a cross-model replication with Llama-3.1-8B-Instruct (11 task types, $N{=}220$) shows death dominance replicates across model families with direction consistency 10/10 ($+30.0$~pp vs.\ $+26.5$~pp for Qwen; \S\ref{sec:cross-model}).
Four intervention axes test whether death dominance is fragile: retry, Reflexion~\citep{reflexion-2023}, $10{\times}$ parameter scaling (72B), and action-space restriction all reduce death rates, yet none closes the gap to deterministic safety (\S\ref{sec:agent-improvement}). Action filtering (blocking the fatal action during exploration) and 72B scaling yield the strongest reductions yet still leave ${\geq}$12~pp residual gaps, results not predictable from the penalty structure alone.
An exploratory router (Qwen3 LoRA, 0.6B--4B) yields flat step-level balanced accuracy ($56$--$59\%$); at episode level, only 4B exceeds the always-deterministic baseline (\S\ref{sec:router-diagnostic}).

Our contributions are:
\begin{enumerate}
    \item \textbf{An episode-level counterfactual diagnostic framework} for decomposing routing signal, with dual penalty-independent and penalty-dependent metrics and router training as a diagnostic probe (\S\ref{sec:collection}--\ref{sec:daf}, \S\ref{sec:router-diagnostic}).

    \item \textbf{Evidence that death dominance resists standard interventions}: 78.9\% of non-tie labels arise from death asymmetry; four representative axes (retry, self-correction, $10{\times}$ scaling, action-space restriction) all fail to close the gap, with action filtering and 72B scaling providing the strongest yet insufficient reductions (\S\ref{sec:death-decomp}--\ref{sec:agent-improvement}).

    \item \textbf{Cross-environment boundary probes}: MATH ($p = 0.81$) confirms the predicted null; ALFWorld identifies information asymmetry; a Llama-3.1-8B replication ($N{=}220$) confirms cross-model consistency with 10/10 direction consistency (\S\ref{sec:math-contrast}--\ref{sec:cross-model}).
\end{enumerate}

```

### 3. method.tex

```latex
\section{Method}
\label{sec:method}

Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically (Appendix~\ref{app:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.

\subsection{Problem Setup}
\label{sec:problem-setup}

Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modalities $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\cite{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic} (${\tt det}$), where the agent receives ground-truth observations from the environment simulator at each step. A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \mathcal{M}$ selects which modality to use at each step; our analysis investigates what signal is available to learn $\rho$. A reasoning-depth ablation ($n{=}120$) found no significant difference ($p > 0.26$; Appendix~\ref{app:ablations}).

\subsection{Counterfactual Episode Collection}
\label{sec:collection}

Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \cite{scienceworld-2022}, 97.4\% of steps produce identical intermediate scores regardless of modality (5{,}726 of 5{,}878 steps across 11 prescreened task types), yielding no per-step routing signal. The 97.4\% tie rate arises because ScienceWorld assigns rewards only at episode termination; intermediate steps update environment state but do not change the score, so a per-step oracle can only distinguish strategies through downstream consequences visible at episode end. Episode-level comparison is therefore the principled granularity for sparse-reward environments, not a fallback from per-step analysis: it directly measures whether one strategy produces better terminal outcomes than the other, bypassing the uninformative intermediate steps entirely.

\paragraph{Pure-strategy trajectories.}
For a task instance $t$ and modality $m \in \mathcal{M}$, a \emph{pure-strategy trajectory} is the complete episode obtained by applying modality $m$ at every step:
\begin{equation}
    \tau_m^{(t)} = (o_1, a_1, o_2, a_2, \ldots, o_T, a_T)
\end{equation}
where $T \leq T_{\max}$ is the episode length (capped at $T_{\max} = 30$ steps). Both trajectories $\tau_{\tt int}^{(t)}$ and $\tau_{\tt det}^{(t)}$ are executed under identical initial conditions (same random seed, same task variation), so performance differences arise solely from the modality choice.

Each trajectory $\tau$ yields a terminal score $s(\tau) \in \mathbb{Z}$ and a death indicator $d(\tau) \in \{0, 1\}$. When the agent dies ($d = 1$), the environment imposes a penalty: $s(\tau) = -P$ where $P > 0$ ($P = 100$ in ScienceWorld). The episode pair produces a tuple:
\begin{multline}
    \bigl(s^{\tt int}, s^{\tt det}, d^{\tt int}, d^{\tt det}\bigr) \triangleq \\
    \bigl(s(\tau_{\tt int}),\, s(\tau_{\tt det}),\, d(\tau_{\tt int}),\, d(\tau_{\tt det})\bigr)
\end{multline}

We use Qwen2.5-7B-Instruct~\citep{qwen25-2024} (vLLM) on ScienceWorld \cite{scienceworld-2022}, a text-based environment spanning 30 task types with a $-100$ death penalty. After prescreening, we collect 245 episode pairs across 11 task types (20--40 per type). The framework is applicable to any environment where paired episodes under two modalities can be collected with binary success/failure indicators. We apply it unchanged to ALFWorld and MATH in \S\ref{sec:math-contrast}--\ref{sec:cross-env}.

\subsection{Episode-Level Labeling}
\label{sec:labeling}

We define a labeling function $L$ that maps a counterfactual pair to a routing preference:
\begin{multline}
    L\!\bigl(\tau_{\tt int}^{(t)}, \tau_{\tt det}^{(t)}\bigr) \;\rightarrow \\
    \ell \in \{{\tt det\text{-}pref},\; {\tt int\text{-}pref},\; {\tt no\text{-}pref}\}
\end{multline}

The labeling function is \emph{death-aware}: it prioritizes survival over score, then compares scores among same-status episodes (Algorithm~\ref{alg:labeling}; Appendix~\ref{app:labeling}). ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. Figure~\ref{fig:pipeline} illustrates the overall pipeline; label distributions are reported in \S\ref{sec:death-decomp}.

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figures/pipeline_overview.pdf}
\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\ref{alg:labeling}.}
\label{fig:pipeline}
\end{figure}

\subsection{Death Avoidance Factor}
\label{sec:daf}

To quantify the contribution of death avoidance to routing signal, we decompose the mean score gap between strategies. Let $\delta = \mathbb{E}[d^{\tt int}] - \mathbb{E}[d^{\tt det}]$ denote the death-rate differential and $\Delta_{\text{nd}}$ the mean score gap restricted to episodes where neither strategy dies. Partitioning episodes by death status, death-asymmetric episodes (where only one strategy dies) contribute a per-episode gap of $P + \bar{s}_{\text{surv}}$, where $\bar{s}_{\text{surv}}$ is the surviving strategy's mean score; when $\bar{s}_{\text{surv}} \ll P$ (in our data, $\bar{s}_{\text{surv}} = 0.87$, or $0.9\%$ of $P$), these episodes contribute ${\approx}\,\delta P$ in aggregate. The full gap thus decomposes as:
\begin{equation}
    \Delta_{\text{full}} \approx \underbrace{\delta \cdot P}_{\text{death contribution}} + \Delta_{\text{nd}}
\end{equation}
The approximation residual is $29.60 - 29.37 = 0.23$ ($0.8\%$ of $\Delta_{\text{full}}$).

We define the Death Avoidance Factor (DAF) as the fraction of the full score gap attributable to death avoidance:
\begin{equation}
    \text{DAF} = 1 - \frac{\Delta_{\text{nd}}}{\Delta_{\text{full}}} \approx \frac{\delta P}{\delta P + \Delta_{\text{nd}}}
\end{equation}%
\footnote{When $\Delta_{\text{nd}} < 0$ (deterministic strategy scores lower than internal on non-death episodes), DAF exceeds 1; death avoidance then overcompensates for a non-death disadvantage.}

Since DAF $= \delta P / (\delta P + \Delta_{\text{nd}})$, it increases monotonically with $P$, a mathematical consequence rather than an empirical finding. We therefore report both DAF at the environment default ($P{=}100$) and the penalty-independent death-asymmetry label fraction as complementary metrics.

\paragraph{Statistical inference.}
We quantify uncertainty via episode-level bootstrap resampling ($B = 10{,}000$). Each resample draws $N = 245$ episodes with replacement, recomputes all metrics, and derives percentile-based 95\% CIs. We resample at the episode level (not the step level) because the episode is the unit of counterfactual comparison. Penalty sensitivity analysis across hypothetical $P$ values is in Appendix~\ref{app:penalty}.

We also measure whether death-avoidance signal is concentrated in a few task types via a Signal Concentration Index (SCI $\in [0, 1]$; Appendix~\ref{app:sci}), reported in \S\ref{sec:death-decomp}.
```

### 4. experiments.tex

```latex
\section{Experiments}

We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types (63\%) lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). This scope limits generalizability: conclusions apply to the included subset, not to all ScienceWorld tasks. An anti-cherry-picking analysis confirms that death dominance holds in 18 of these 19 types, with a mean $\Delta\text{DR} = +38.2$\,pp exceeding the included tasks' $+28.7$\,pp (Appendix~\ref{app:per-task}).

\subsection{Death Avoidance Decomposition}
\label{sec:death-decomp}

\begin{figure}[t]
\centering
\includegraphics[width=0.85\columnwidth]{figures/fig1_daf_scatter.pdf}
\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$, $p < 10^{-6}$, $n = 11$ task types. This near-perfect correlation is structurally implied by the decomposition (\S\ref{sec:death-decomp}); see text for interpretation.}
\label{fig:decomposition}
\end{figure}

Across 245 episodes, $\Delta_{\text{full}} = +29.60$; excluding death episodes, $\Delta_{\text{nd}} = +2.84$, yielding DAF $= 90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$, episode-level bootstrap, $B{=}10{,}000$; at the default $P{=}100$). The penalty-independent death-asymmetry label fraction is 78.9\% (75 of 95 non-tie labels). Given observed $\delta = 0.265$ and $P = 100$, the predicted DAF $= \delta P / (\delta P + \Delta_{\text{nd}}) = 26.5 / 29.37 \approx 90.3\%$, closely matching the observed value; DAF is thus a derived quantity once $\delta$, $P$, and $\Delta_{\text{nd}}$ are known, while the 78.9\% label fraction is the penalty-independent empirical finding. Of these 75, 54 (72.0\%) reduce to ties when the death penalty is removed entirely: in those episodes, both modalities score zero without death, so the only reason one strategy outscored the other was avoiding the $-100$ penalty. Death avoidance is not merely the dominant but often the \emph{sole} discriminating signal between modalities. The remaining 21 death-asymmetry labels involve episodes where the surviving strategy also earned positive score, but the death penalty still accounts for the majority of the score gap. At $P{=}0$, the 54 sole-signal labels reduce to ties, leaving 41 non-tie labels of which 21 (51.2\%) still involve death asymmetry; the labeling function itself is penalty-independent (Algorithm~\ref{alg:labeling}), but the practical routing value of death avoidance requires $P > 0$.

\paragraph{Per-task correlation structure.}
The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic (2.6$\times$), consistent with the internal strategy's reliance on self-generated observations that compound prediction errors across steps. Per-task, death rate differential correlates with $\Delta_{\text{full}}$ ($r = 0.97$, $p < 10^{-6}$; Figure~\ref{fig:decomposition}). Since $P$ is constant across all task types, $\Delta_{\text{full}} = P \cdot \delta + \Delta_{\text{nd}}$ makes $\Delta_{\text{full}}$ a linear function of $\delta$ with residual $\Delta_{\text{nd}}$; when DAF $\rightarrow 1$, this residual vanishes and $r \rightarrow 1$ by construction. The near-perfect correlation is therefore a mathematical consequence of death dominance, not an independent empirical finding. We retain it as an internal consistency check. The correlation drops below significance at $P \leq 25$ (Appendix~\ref{app:penalty}). Of 245 episodes, 86 are \texttt{det\_preferred}, 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preference}.

\paragraph{Signal concentration and binary structure.}
The Signal Concentration Index (SCI $= 0.2147$; Appendix~\ref{app:sci}) confirms low concentration: the top-3 task types account for only $39.8\%$ of total death-rate differential. The aggregate 78.9\% reflects a per-task binary structure: all 10 death-prone task types produce 100\% death-asymmetry labels, while \texttt{find-non-living-thing} (zero deaths, $\Delta = +9.58$ from non-death scores) produces 0\%. The framework thus diagnoses a binary property (``is this environment death-dominated?'') rather than a continuous routing signal. Removing \texttt{find-non-living-thing} raises the label fraction to 100\% and DAF to 96.8\% (Appendix~\ref{app:loto-daf}).

\paragraph{Sensitivity and seed robustness.}
Episode-level bootstrap ($B = 10{,}000$) yields 95\% CI $[81.6\%, 98.8\%]$ for DAF (Cohen's $d = 3.02$); leave-one-task-out analysis confirms stability (DAF range: 75.9\%--78.9\%; Appendix~\ref{app:loto-daf}). An independent seed replication ($N{=}220$) yields DAF $= 89.7\%$, within 0.7~pp of the primary analysis (Appendix~\ref{app:seed-robustness}). Cluster-robust inference with $K{=}11$ task-type clusters ($p < 0.001$; primary CIs are episode-level, cluster CIs serve as sensitivity analysis) and 28-task directional consistency (100\%) confirm significance (Appendices~\ref{app:wild-cluster}--\ref{app:per-task-ci}).

\subsection{Multi-Model Validation}
\label{sec:cross-model}

A Llama-3.1-8B-Instruct~\citep{llama3-2024} cross-model replication across all 11 task types ($N{=}220$) confirms that death dominance replicates across model families: internal death rate $41.4\%$ vs.\ deterministic $11.4\%$ (death-rate differential $+30.0$~pp), with direction consistency 10/10 on death-prone tasks, 83 deterministic-preferred, 3 internal-preferred (1.4\%, all death-asymmetry reversals), and 134 no-preference labels.
Both models exhibit nearly identical internal vulnerability (${\sim}$42\%: Qwen $42.9\%$, Llama $41.4\%$), confirming that death-prone failure is structurally determined; the differential magnitude varies ($+26.5$~pp Qwen, $+30.0$~pp Llama) because deterministic strategy safety is model-dependent ($16.3\%$ vs.\ $11.4\%$).
\texttt{identify-life-stages-1} shows cross-model precision matching ($55\%$/$10\%$/$+45$~pp in both models).
\texttt{find-non-living-thing} shows zero deaths in both models, consistent with its majority-class answer distribution (\S\ref{sec:discussion}). Both models are in the 7--8B range; $10{\times}$ scaling (\S\ref{sec:agent-improvement}) confirms that death dominance persists across capability levels (Appendix~\ref{app:cross-model}).

\subsection{Agent Improvement Baselines}
\label{sec:agent-improvement}

\begin{table}[t]
\centering
\small
\begin{tabular}{@{}lrr@{}}
\toprule
Condition & Death\% & $N$ \\
\midrule
Single-trial baseline & 42.9 & 245 \\
Reflexion ($3{\times}$) & 31.4 & 220 \\
Qwen2.5-72B ($10{\times}$) & 30.6 & 255 \\
Deterministic baseline & 16.3 & 245 \\
\midrule
\multicolumn{3}{@{}l}{\textit{10 death-prone tasks only:}} \\
Death-prone baseline & 48.0 & 200 \\
Retry ($5{\times}$) & 43.5 & 200 \\
\bottomrule
\end{tabular}
\caption{Internal-strategy death rates under agent improvement methods. Top: all 11 tasks (72B: independently collected at both internal and deterministic). Bottom: 10 death-prone tasks (\texttt{find-non-living-thing} excluded, 0\% death at all scales). All interventions reduce death rate but none approaches deterministic-level safety.}
\label{tab:agent-improvement}
\end{table}

We test whether agent-level improvement reduces death dominance (Table~\ref{tab:agent-improvement}). Retry ($N{=}5$ attempts without self-correction) yields marginal reduction on death-prone tasks ($43.5\%$ vs.\ $48.0\%$ baseline, $\Delta = -4.5$~pp). Reflexion~\citep{reflexion-2023} (verbal self-reflection between trials) reduces death to 31.4\% across all 11 tasks by rescuing 29.3\% of first-trial deaths, but the gap to deterministic remains 15.1~pp; on the 10 death-prone tasks, Reflexion achieves ${\sim}$35\%. Under Reflexion ($N{=}3$, matched-episode analysis), $\Delta_{\text{nd}} = -0.47$, yielding DAF $> 100\%$: the deterministic advantage is entirely attributable to death avoidance, and in non-death episodes the self-correcting agent slightly outperforms the deterministic baseline. Scaling to Qwen2.5-72B ($10{\times}$ parameters; both internal and deterministic strategies independently collected at 72B, 255 episodes across all 11 task types) reduces death rate to $30.6\%$. The 72B deterministic strategy achieves $2.75\%$ death rate ($\Delta\text{DR} = +27.8$~pp), and $\Delta_{\text{nd}} = +2.28$, yielding DAF $= 92.4\%$ (7B: $90.4\%$); scaling lowers death rate but leaves death dominance intact.

\paragraph{Dose-response analysis.}
We extend both interventions to $N{=}5$ trials on death-prone tasks ($n{=}200$; Figure~\ref{fig:dose-response}). Retry is nearly flat ($48.0\% \to 43.5\%$, $\Delta = -4.5$~pp over five trials). Reflexion drops steeply to $34.0\%$ at $N{=}3$ ($\Delta = -13.5$~pp, $p < 0.005$) then plateaus ($34$--$36.5\%$ for $N \geq 3$, pairwise $p > 0.5$). Retry's per-trial conditional death rate stays constant at ${\sim}48\%$; Reflexion's declines to ${\sim}31\%$ by Trial~3 (per-task breakdown in Appendix~\ref{app:dose-response}).

\begin{figure}[t]
\centering
\includegraphics[width=\columnwidth]{figures/dose_response.pdf}
\caption{Death rate as a function of trial count ($N$) for Retry and Reflexion on 10 death-prone tasks ($n{=}200$). Retry (blue) is nearly flat; Reflexion (red) drops steeply through $N{=}3$ then plateaus. Horizontal lines: 72B scaling baseline ($30.6\%$, all 11 tasks) and deterministic baseline ($16.3\%$). Error bands: Wilson 95\% CIs.}
\label{fig:dose-response}
\end{figure}

\subsection{Cross-Environment Boundary Probes}
\label{sec:math-contrast}
\label{sec:cross-env}

We evaluate two additional environments as boundary probes (Appendix~\ref{app:cross-env-details}). ``Deterministic'' denotes qualitatively different modalities per environment: ScienceWorld uses an oracle simulator with ground-truth state, MATH uses a Python code interpreter, and ALFWorld uses admissible-action enumeration. These are not equivalent computation modes; results probe framework applicability rather than replicate findings.

\paragraph{MATH.} On MATH Level~4--5~\citep{math-2021} ($N{=}795$, code interpreter as deterministic modality), internal reasoning and code interpretation achieve near-identical accuracy ($73.5\%$ vs.\ $73.0\%$, McNemar $p = 0.81$, 95\% CI $[-2.6, +3.6]$~pp), with balanced labels (107 vs.\ 95, 74.6\% no-preference). Without catastrophic failure, no routing signal emerges.

\paragraph{ALFWorld.} ALFWorld~\citep{alfworld-2021} (6 task types, 135 games) provides the deterministic strategy with admissible actions, an information asymmetry rather than a computation mode switch. The success rate gap is $27.4\%$ vs.\ $3.0\%$ (35 det-preferred, 2 int-preferred, 98 no-preference). The deterministic advantage stems from this information gap, a qualitatively different mechanism that the framework diagnoses without modification.

\subsection{Baselines}
\label{sec:baselines}

\begin{table}[t]
\centering
\small
\resizebox{\columnwidth}{!}{%
\begin{tabular}{@{}lccc@{}}
\toprule
Strategy & Score & 95\% CI & Death \% \\
\midrule
Always-Internal & $-39.07$ & [$-46.40$, $-32.27$] & 42.9 \\
Always-Deterministic & $-9.47$ & [$-14.71$, $-4.29$] & 16.3 \\
Random & $-22.38$ & [$-28.67$, $-15.75$] & 27.8 \\
Oracle & $-6.58$ & [$-11.54$, $-1.70$] & 14.3 \\
\midrule
Trained Router$^\dagger$ & $-10.70$ & [$-16.33$, $-5.27$] & 17.6 \\
\bottomrule
\end{tabular}}
\caption{Episode-weighted mean scores on ScienceWorld (11 tasks, 245 episodes). $\dagger$\,Single random seed (42) per episode pair; see Appendix~\ref{app:seed-robustness} for 8-seed robustness analysis.}
\label{tab:baselines}
\end{table}

Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points. The oracle improves only to $-6.58$, with 96.3\% of decisions matching always-deterministic, an \emph{oracle degeneracy}: the optimal routing policy closely resembles unconditional deterministic computation.

\subsection{Router Training as Diagnostic Probe}
\label{sec:router-diagnostic}

We probe whether counterfactual labels can train a step-level router as a diagnostic of label informativeness. The oracle margin (2.89 points) caps routing upside; ${\sim}27.7\%$ of step-level labels are misaligned with episode-level assignments, further limiting learnability. An implicit router (Qwen3, LoRA; Appendix~\ref{app:router-details}) trained at three scales (0.6B, 1.7B, 4B) with 4-seed configurations shows flat step-level balanced accuracy ($56$--$59\%$, within seed variance). At episode level, only 4B exceeds always-deterministic ($59.0 \pm 1.9\%$, $p < 0.005$; Appendix~\ref{app:ablations}); 0.6B and 1.7B remain at or below chance. The multi-step nature of routing (10--50 actions with compounding state uncertainty) creates inherent label noise between step-level decisions and episode-level outcomes.

\paragraph{End-to-end deployment.} The 4B router deployed end-to-end ($N{=}245$) scores $-12.03$ (95\% CI: $[-17.82, -6.45]$), not exceeding always-deterministic ($-9.47$). Paraphrase-based augmentation ($25\%$--$800\%$) provides no improvement; the $3.7\%$ internal-preferred base rate makes real-data collection expensive (Appendices~\ref{app:seed-robustness}--\ref{app:ablations}).
```

### 5. related_work.tex

```latex
\section{Related Work}

\paragraph{Tool Use and External Computation in LLMs.}
A growing body of work augments language models with external tools \citep{tool-learning-survey-2024}, spanning several functional categories.
\emph{Self-supervised} approaches learn tool invocation from loss signals: Toolformer \cite{toolformer-2023} inserts API calls filtered by perplexity reduction; ToolACE \cite{toolace-2025} curates synthetic data for function-calling accuracy.
\emph{Token-level} methods embed tools into the model vocabulary: ToolkenGPT \cite{toolkengpt-2023} represents tools as special tokens resolved at inference.
\emph{Task-level} decomposition routes subtasks to specialized modules: ART \cite{art-2023} generates tool-augmented programs; Chameleon \cite{chameleon-2023} composes heterogeneous modules per subtask.
\emph{RL-based} methods learn routing policies from reward: ReTool \cite{retool-2025} discovers when code execution is preferable to chain-of-thought.
All focus on \emph{learning to use tools}; we ask a prior question: \emph{what signal drives the routing decision?}
Recent concurrent work sharpens this question: \citet{tool-overuse-illusion-2026} identify a cognitive-illusion effect where LLMs default to external tools even when internal knowledge suffices, finding that tool overuse correlates with model uncertainty rather than task difficulty. \citet{when2tool-2026} show tool-call decisions are encoded in hidden states before reasoning, \citet{tool-use-tax-2026} quantify a ``tool-use tax,'' and \citet{to-call-or-not-2026} propose a necessity, utility, and affordability framework. Our decomposition provides environment-grounded evidence: in ScienceWorld, 78.9\% of routing labels trace to catastrophic-failure prevention.

\paragraph{Adaptive Computation and Routing.}
CogRouter \cite{cogrouter-2026} adapts reasoning depth per step, ARES \cite{ares-2026} selects among reasoning effort levels, Mixture-of-Recursions \cite{mixture-of-recursions-2025} learns token-level recursion depths, and MTRouter \cite{mtrouter-2026} addresses multi-turn routing.
RouteLLM \citep{routellm-2024} learns routers from preference data to select between strong and weak models.
These optimize \emph{how} to route; we reveal \emph{why} routing helps: in interactive environments, the dominant signal is catastrophic-failure avoidance.

\paragraph{Counterfactual Evaluation in RL.}
Prior work generates counterfactual explanations for RL agents by perturbing individual actions within a fixed policy \citep{olson2021counterfactual, gajcin2023counterfactual, amitai2024explaining}.
Our approach differs in both purpose and granularity: we execute two complete episodes under different routing strategies, producing prospective paired comparisons that isolate routing signal \emph{before} any router is trained.

\paragraph{LLM Agent Environments and Reasoning.}
ScienceWorld \cite{scienceworld-2022} serves as our primary testbed; Inner Monologue \cite{huang2022inner} grounds LLM planning in embodied feedback; Voyager \cite{wang2023voyager} demonstrates open-ended LLM agents; ALFWorld \cite{alfworld-2021} provides a complementary household environment; AgentBench \cite{agentbench-2024} offers systematic evaluation. \citet{zhou2024webarena} document common failure modes (premature termination, hallucinated actions) in web-based agents, consistent with our finding that state hallucination is the primary internal-strategy failure mechanism. ReAct \cite{react-2023} serves as our internal baseline; Reflexion \cite{reflexion-2023} extends this with verbal self-reflection; LATS \cite{lats-2024} adds tree search. SelfCheckGPT \cite{selfcheckgpt-2023} detects unreliable LLM outputs; our work shows that in interactive environments, such unreliability manifests as catastrophic death.

\paragraph{Safe RL.}
Safe RL methods \citep{garcia2015comprehensive,tamar2015cvar,achiam2017cpo,crpo-2021} enforce constraints in MDPs; SafeRoute \citep{saferoute-2025} applies adaptive model selection for safety guardrails. Our diagnostic shows modality routing already functions as an implicit safety mechanism in environments with catastrophic failure.
```

### 6. discussion.tex

```latex
\section{Discussion}
\label{sec:discussion}

\paragraph{Why the router fails: task-type-level signal.}
The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property (10 of 11 types carry death risk), but step-level features correlate weakly because death risk depends on multi-step state trajectories, not individual action semantics. The 4B router's episode-level improvement ($59.0\%$) without step-level gains ($56$--$59\%$, flat) confirms that capacity scaling captures task-type classification rather than generalizable features. Cross-task-type transfer to physical-science tasks yields chance-level accuracy (49.2\%, 95\% CI $[42.4\%, 55.9\%]$; Appendix~\ref{app:ablations}), and 7 of 11 task types contain only deterministic-preferred labels, making majority-class collapse a structural consequence of the label distribution.

\paragraph{Non-triviality of death dominance.}
While death dominance itself follows from the penalty structure (\S\ref{sec:daf}), its resistance to intervention was not predictable a priori. Four representative axes spanning retry, self-correction, parameter scaling, and action-space restriction all fail to close the gap to deterministic safety (16.3\%): Retry ($43.5\%$ at $N{=}5$), Reflexion ($34.0\%$ at $N{=}3$, plateauing at $34$--$36.5\%$), $10{\times}$ scaling ($30.6\%$, 72B, $N{=}255$), and action-space filtering ($29.0\%$; Appendix~\ref{app:grounding-ablation}). Action filtering and 72B scaling yield the strongest reductions yet still leave ${\geq}$12~pp residual gaps. Reflexion and scaling converge to overlapping 95\% Wilson CIs ($[27.8\%, 40.8\%]$ and $[25.2\%, 36.5\%]$); this overlap suggests a shared bound from the lack of ground-truth state access. The oracle matches always-deterministic on 96.3\% of decisions (score improvement: 2.89 points), and even with perfect per-task death risk knowledge, threshold routing cannot outperform always-deterministic (Appendix~\ref{sec:threshold-routing}). More aggressive planning-based interventions (Tree-of-Thought backtracking~\citep{tot-2023}, process reward models) remain untested and may further reduce death rates; we characterize a ceiling for the tested intervention classes, not a universal bound.

\paragraph{Anatomy of catastrophic failure.}
All 105 internal-strategy deaths trace to misuse of \texttt{focus on [object]}, the answer-submission action, as a general interaction command (taxonomy in Appendix~\ref{app:failure-modes}). The root cause is action-space grounding failure: agents parse task descriptions correctly but cannot ground understanding in valid primitives. The internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not different within-episode behavior (${\sim}5\%$ \texttt{focus on} rate in both). \texttt{find-non-living-thing}, the sole zero-death task, uses \texttt{focus on} more frequently than any death-prone task: non-living objects are the majority class, so indiscriminate submissions rarely trigger death; lethality is thus a joint function of action misuse and answer distribution. Direct grounding interventions reduce but do not eliminate vulnerability ($48.0\% \to 37.0\%$ via prompt warning; $\to 29.0\%$ via action-space filter), with ironic effects where warnings increased \texttt{focus on} salience on identification tasks (Appendix~\ref{app:grounding-ablation}).

\paragraph{Practitioner decision framework.}
We formalize a three-stage diagnostic procedure (${\sim}$50-episode pilot $\to$ death-rate differential $\to$ death-label fraction) with concrete thresholds in Appendix~\ref{app:decision-framework}; retrospective validation confirms correct predictions for all four experimental conditions (Qwen-7B, Llama-8B, Qwen-72B, MATH). Our router training consumed ${\sim}$200 GPU-hours across 28 configurations without exceeding always-deterministic; this framework could have predicted that outcome from a 50-episode pilot at negligible cost.

\paragraph{Pure-strategy gap.}
Our counterfactual labels derive from pure-strategy episodes, but a deployed router produces mixed trajectories whose state distributions differ from either pure strategy~\citep{dagger-2011}. The 4B router's end-to-end score ($-12.03$) falling below always-deterministic ($-9.47$) may partly reflect this distribution shift rather than label noise alone. Closing this gap requires on-policy data collection under the router's own mixed policy, which is expensive given the 3.7\% internal-preferred base rate (${\sim}1{,}350$ paired episodes for 50 minority-class samples).

\paragraph{Framework applicability.}
The penalty-independent label fraction (78.9\%) is the primary diagnostic; DAF increases monotonically with $P$ (Appendix~\ref{app:penalty}). The framework requires paired modality episodes with binary catastrophic outcomes. Preliminary pilots on MiniHack~\citep{minihack-2021} navigation tasks (0\% death rate, no monster spawning) and Crafter~\citep{crafter-2022} (100\% death rate for both strategies) produced no death asymmetry, illustrating two boundary conditions: environments lacking a death mechanism yield no routing signal (consistent with the MATH null), while environments where no strategy avoids death lack exploitable asymmetry. The framework's diagnostic power requires an intermediate regime where strategy choice meaningfully affects survival; NetHack~\citep{nethack-2020} combat tasks, where permadeath interacts with strategy quality, remain the most direct replication target; recent benchmarks \citep{balrog-2025,netplay-2024} provide infrastructure.
```

### 7. conclusion.tex

```latex
\section{Conclusion}

We presented a diagnostic framework for decomposing routing signal in modular LLM agents via episode-level counterfactual analysis. Applied to ScienceWorld (245 episodes, 11 task types), 78.9\% of non-tie routing labels arise from death asymmetry; agent improvement baselines (retry, self-correction, $10{\times}$ scaling, action-space restriction) confirm this is robust. Cross-domain contrasts support framework predictions: MATH shows no routing signal without catastrophic failure; ALFWorld identifies information asymmetry as an alternative mechanism. Future work should target environments with intermediate death regimes, such as NetHack~\citep{nethack-2020} combat tasks and Crafter~\citep{crafter-2022} with tuned difficulty, building on recent LLM agent benchmarks \citep{balrog-2025,netplay-2024}; evaluation with stronger backbones is another direct open direction.
```

---

All seven sections have been read in full and provided above. These files contain the complete LaTeX content for the paper on diagnosing routing signal in modular LLM agents through episode-level counterfactual analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f322f0a-80a3-49dd-a147-5438f037c7e7",
  "isSidechain": true,
  "agentId": "a5995f18396c1763e",
  "requestId": "req_011CbC5eigXySHswcJfppVS5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "46f5829d-a5f6-49a8-a5f6-8f6a76162386",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/review_reviewer_1_38fb0170",
  "sessionId": "356f6463-a842-4ea1-8de2-5e7d9ff33a91",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013trJgSpExzH2ingA99Wn6D",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 13597,
      "cache_read_input_tokens": 18486,
      "output_tokens": 11599,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13597
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 11599,
          "cache_read_input_tokens": 18486,
          "cache_creation_input_tokens": 13597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13597,
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
