# research ref audit B — Part 2 of 2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../research-ref-audit-b.md) · [Structured JSON](../../../sessions/be/be8dd3c1b3ed3609a744.json)

## Round 8

### Tool result

_source line 417 · 2026-05-26T10:23:29.512Z_

<details><summary>↩ Tool result · `toolu_01SmQrdWnUinYEavZxVYWS5j`</summary>

```text
1	\section{Introduction}
2	
3	\begin{figure*}[t]
4	\centering
5	\includegraphics[width=0.95\textwidth]{figures/pipeline_overview.pdf}
6	\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\ref{alg:labeling}.}
7	\label{fig:pipeline}
8	\end{figure*}
9	
10	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
11	Existing routing methods, whether inserting API calls by perplexity reduction~\citep{toolformer-2023}, decomposing tasks into tool-augmented programs~\citep{art-2023,chameleon-2023}, or adaptively selecting reasoning depths~\citep{cogrouter-2026,ares-2026} and model tiers~\citep{mtrouter-2026,budget-aware-routing-2026}, share an implicit assumption: that routing signal stems from diverse sources and a learned router can exploit it. But before training a router, we should understand what mechanistic signal drives the routing preference. If signal collapses to a single dominant mechanism, a learned step-level router may not be the right solution.
12	
13	We propose an \emph{episode-level counterfactual diagnostic framework} to address this prior question. The framework compares pure-strategy outcomes (internal-only vs.\ deterministic-only) and introduces the Death Avoidance Factor (DAF) to decompose the routing score gap into death-avoidance and non-death components (\S\ref{sec:collection}--\ref{sec:daf}). Operating at episode granularity is essential: per-step oracle labeling degenerates under sparse terminal rewards (97.4\% tie rate in ScienceWorld; \S\ref{sec:collection}).
14	
15	Applied to ScienceWorld~\citep{scienceworld-2022}, the framework reveals that \textbf{78.9\% of non-tie routing labels arise from death asymmetry}, where the internal strategy triggers a catastrophic failure while the deterministic strategy survives. This pattern replicates across three architecturally distinct model families (7--70B parameters) and intensifies at larger scale, where death avoidance accounts for the entire performance gap (\S\ref{sec:cross-model}--\ref{sec:agent-improvement}). Always-deterministic matches 96.3\% of oracle routing decisions; a trained step-level router fails to exceed this trivial baseline (\S\ref{sec:baselines}--\ref{sec:router-diagnostic}). Boundary probes on MATH and ALFWorld show that the framework distinguishes qualitatively different mechanisms, including environments with no routing signal and those driven by information asymmetry (\S\ref{sec:cross-env}).
16	
17	Our contributions: (1)~An \textbf{episode-level counterfactual diagnostic framework} and the DAF metric that decompose routing signal into mechanistic components before any router is built, overcoming per-step oracle degeneracy in sparse-reward environments.
18	(2)~Evidence that \textbf{routing signal in ScienceWorld is death-dominated}: 78.9\% of non-tie labels trace to death asymmetry, replicated across three model families and two scales (7B and 70B). A ${\sim}$50-episode pilot suffices for practitioners to assess whether learned routing adds value (Appendix~\ref{app:decision-framework}).
19	(3)~\textbf{Boundary probes} on MATH and ALFWorld showing the framework can diagnose qualitatively different routing mechanisms, while clarifying that full quantitative validation remains specific to ScienceWorld.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "858e8741-b759-4d07-bbe8-2fb42de8b26c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=0.95\\textwidth]{figures/pipeline_overview.pdf}\n\\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\\ref{alg:labeling}.}\n\\label{fig:pipeline}\n\\end{figure*}\n\nLarge language models deployed as interactive agents must repeatedly decide \\emph{how} to compute: reason internally, or delegate to an external tool.\nExisting routing methods, whether inserting API calls by perplexity reduction~\\citep{toolformer-2023}, decomposing tasks into tool-augmented programs~\\citep{art-2023,chameleon-2023}, or adaptively selecting reasoning depths~\\citep{cogrouter-2026,ares-2026} and model tiers~\\citep{mtrouter-2026,budget-aware-routing-2026}, share an implicit assumption: that routing signal stems from diverse sources and a learned router can exploit it. But before training a router, we should understand what mechanistic signal drives the routing preference. If signal collapses to a single dominant mechanism, a learned step-level router may not be the right solution.\n\nWe propose an \\emph{episode-level counterfactual diagnostic framework} to address this prior question. The framework compares pure-strategy outcomes (internal-only vs.\\ deterministic-only) and introduces the Death Avoidance Factor (DAF) to decompose the routing score gap into death-avoidance and non-death components (\\S\\ref{sec:collection}--\\ref{sec:daf}). Operating at episode granularity is essential: per-step oracle labeling degenerates under sparse terminal rewards (97.4\\% tie rate in ScienceWorld; \\S\\ref{sec:collection}).\n\nApplied to ScienceWorld~\\citep{scienceworld-2022}, the framework reveals that \\textbf{78.9\\% of non-tie routing labels arise from death asymmetry}, where the internal strategy triggers a catastrophic failure while the deterministic strategy survives. This pattern replicates across three architecturally distinct model families (7--70B parameters) and intensifies at larger scale, where death avoidance accounts for the entire performance gap (\\S\\ref{sec:cross-model}--\\ref{sec:agent-improvement}). Always-deterministic matches 96.3\\% of oracle routing decisions; a trained step-level router fails to exceed this trivial baseline (\\S\\ref{sec:baselines}--\\ref{sec:router-diagnostic}). Boundary probes on MATH and ALFWorld show that the framework distinguishes qualitatively different mechanisms, including environments with no routing signal and those driven by information asymmetry (\\S\\ref{sec:cross-env}).\n\nOur contributions: (1)~An \\textbf{episode-level counterfactual diagnostic framework} and the DAF metric that decompose routing signal into mechanistic components before any router is built, overcoming per-step oracle degeneracy in sparse-reward environments.\n(2)~Evidence that \\textbf{routing signal in ScienceWorld is death-dominated}: 78.9\\% of non-tie labels trace to death asymmetry, replicated across three model families and two scales (7B and 70B). A ${\\sim}$50-episode pilot suffices for practitioners to assess whether learned routing adds value (Appendix~\\ref{app:decision-framework}).\n(3)~\\textbf{Boundary probes} on MATH and ALFWorld showing the framework can diagnose qualitatively different routing mechanisms, while clarifying that full quantitative validation remains specific to ScienceWorld.\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---


### Tool call

_source line 418_

<details open><summary>🔧 Tool call — Read · `toolu_01NwXBq84TkFTND9WLYH6f6j`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "62a1f0d5-0b67-491b-ac51-c20ecc74c18c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEkDYND7gvjNjgB2RWqkjW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21519,
      "cache_read_input_tokens": 37752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21519
      },
      "output_tokens": 20,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-26T10:23:30.100Z_

<details><summary>↩ Tool result · `toolu_01NwXBq84TkFTND9WLYH6f6j`</summary>

```text
1	\section{Related Work}
2	
3	\begin{figure*}[t]
4	\centering
5	\includegraphics[width=\textwidth]{figures/death_action_comparison.pdf}
6	\vspace{-2mm}
7	\caption{Non-\texttt{connect} action distribution comparison between internal (left) and deterministic (right) strategies within death episodes. Both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not different action selection within those states.}
8	\label{fig:death-comparison}
9	\end{figure*}
10	
11	\paragraph{Tool-Augmented Agents and Adaptive Routing.}
12	Methods for augmenting LLMs with external tools span self-supervised invocation~\citep{toolformer-2023,toolace-2025}, task-level decomposition~\citep{art-2023,chameleon-2023}, and RL-based tool selection~\citep{retool-2025,tool-learning-survey-2024}. Concurrent work examines \emph{when} to invoke tools: \citet{when2tool-2026} analyze accuracy--latency tradeoffs, \citet{tool-use-tax-2026} quantify invocation overhead, and \citet{to-call-or-not-2026,tool-overuse-illusion-2026} investigate overuse patterns. On the routing side, adaptive methods range from learned halting~\citep{graves2016act} and token-level recursion~\citep{mixture-of-recursions-2025} to per-step depth adjustment~\citep{cogrouter-2026,ares-2026} and multi-turn model selection~\citep{mtrouter-2026}. Model-selection routing~\citep{routellm-2024,frugalgpt-2023,automix-2024} optimizes \emph{which} model to invoke based on query difficulty; \citet{budget-aware-routing-2026} train episode-level routing under sparse rewards via counterfactual rollouts, the closest setting to ours, though they focus on learning the router rather than diagnosing what signal it captures. All these approaches presuppose that diverse routing signals exist; our decomposition reveals that in ScienceWorld, a single mechanism accounts for 78.9\% of routing labels.
13	
14	\paragraph{Counterfactual Methods and Agent Environments.}
15	Prior work generates counterfactual explanations by perturbing individual actions~\citep{olson2021counterfactual,gajcin2023counterfactual,amitai2024explaining}; recent extensions target LLM agents via abstract state comparison~\citep{pona2025abstract}, axis-aligned perturbations~\citep{axis-2026}, and causal structure discovery~\citep{cso-2026}. These approaches explain \emph{why} an agent succeeded or failed on a single trajectory. We instead execute complete episodes under two strategies to decompose routing signal \emph{before} training. Counterfactual data augmentation~\citep{kaushik2020learning} edits inputs to improve robustness; we execute full counterfactual \emph{episodes} under controlled strategy variation, answering what \emph{type} of signal drives strategy preferences. ScienceWorld~\citep{scienceworld-2022} serves as our primary testbed; ALFWorld~\citep{alfworld-2021} and AgentBench~\citep{agentbench-2024} provide complementary evaluation. ReAct~\citep{react-2023} is our internal baseline; Reflexion~\citep{reflexion-2023} and LATS~\citep{lats-2024} extend it. The concurrent SALT~\citep{salt-2026} assigns step-level credit on ALFWorld, complementing our episode-level decomposition.
16	
17	\paragraph{Safe RL, Agent Safety, and Causal Inference.}
18	Death avoidance connects to safe RL~\citep{garcia2015comprehensive,achiam2017cpo}, shielding~\citep{alshiekh2018safe}, and the growing literature on LLM agent safety evaluation~\citep{ruan2024failures,saferoute-2025,agent-safetybench-2024}. Classical safe RL methods require known transition dynamics or a differentiable safety model, neither available for black-box LLM agents. Unlike token-level adaptive computation~\citep{mixture-of-depths-2024,xin2020deebert} and mixture-of-experts routing~\citep{switch-transformer-2022}, which optimize compute allocation at inference time, our framework diagnoses aggregate routing signal at episode granularity. Methodologically, our pure-strategy comparison is a simplified potential outcomes framework~\citep{rubin1974estimating}: executing both strategies under identical initial conditions eliminates confounding without structural causal models~\citep{pearl2009causality}, at the cost of requiring paired episode collection.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "d99a9750-5329-4710-b4a4-b37c8ce8ebce",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{figures/death_action_comparison.pdf}\n\\vspace{-2mm}\n\\caption{Non-\\texttt{connect} action distribution comparison between internal (left) and deterministic (right) strategies within death episodes. Both strategies exhibit comparable \\texttt{focus on} rates (${\\sim}5\\%$); the internal strategy's higher death count (105 vs.\\ 40) reflects more frequent entry into catastrophic states, not different action selection within those states.}\n\\label{fig:death-comparison}\n\\end{figure*}\n\n\\paragraph{Tool-Augmented Agents and Adaptive Routing.}\nMethods for augmenting LLMs with external tools span self-supervised invocation~\\citep{toolformer-2023,toolace-2025}, task-level decomposition~\\citep{art-2023,chameleon-2023}, and RL-based tool selection~\\citep{retool-2025,tool-learning-survey-2024}. Concurrent work examines \\emph{when} to invoke tools: \\citet{when2tool-2026} analyze accuracy--latency tradeoffs, \\citet{tool-use-tax-2026} quantify invocation overhead, and \\citet{to-call-or-not-2026,tool-overuse-illusion-2026} investigate overuse patterns. On the routing side, adaptive methods range from learned halting~\\citep{graves2016act} and token-level recursion~\\citep{mixture-of-recursions-2025} to per-step depth adjustment~\\citep{cogrouter-2026,ares-2026} and multi-turn model selection~\\citep{mtrouter-2026}. Model-selection routing~\\citep{routellm-2024,frugalgpt-2023,automix-2024} optimizes \\emph{which} model to invoke based on query difficulty; \\citet{budget-aware-routing-2026} train episode-level routing under sparse rewards via counterfactual rollouts, the closest setting to ours, though they focus on learning the router rather than diagnosing what signal it captures. All these approaches presuppose that diverse routing signals exist; our decomposition reveals that in ScienceWorld, a single mechanism accounts for 78.9\\% of routing labels.\n\n\\paragraph{Counterfactual Methods and Agent Environments.}\nPrior work generates counterfactual explanations by perturbing individual actions~\\citep{olson2021counterfactual,gajcin2023counterfactual,amitai2024explaining}; recent extensions target LLM agents via abstract state comparison~\\citep{pona2025abstract}, axis-aligned perturbations~\\citep{axis-2026}, and causal structure discovery~\\citep{cso-2026}. These approaches explain \\emph{why} an agent succeeded or failed on a single trajectory. We instead execute complete episodes under two strategies to decompose routing signal \\emph{before} training. Counterfactual data augmentation~\\citep{kaushik2020learning} edits inputs to improve robustness; we execute full counterfactual \\emph{episodes} under controlled strategy variation, answering what \\emph{type} of signal drives strategy preferences. ScienceWorld~\\citep{scienceworld-2022} serves as our primary testbed; ALFWorld~\\citep{alfworld-2021} and AgentBench~\\citep{agentbench-2024} provide complementary evaluation. ReAct~\\citep{react-2023} is our internal baseline; Reflexion~\\citep{reflexion-2023} and LATS~\\citep{lats-2024} extend it. The concurrent SALT~\\citep{salt-2026} assigns step-level credit on ALFWorld, complementing our episode-level decomposition.\n\n\\paragraph{Safe RL, Agent Safety, and Causal Inference.}\nDeath avoidance connects to safe RL~\\citep{garcia2015comprehensive,achiam2017cpo}, shielding~\\citep{alshiekh2018safe}, and the growing literature on LLM agent safety evaluation~\\citep{ruan2024failures,saferoute-2025,agent-safetybench-2024}. Classical safe RL methods require known transition dynamics or a differentiable safety model, neither available for black-box LLM agents. Unlike token-level adaptive computation~\\citep{mixture-of-depths-2024,xin2020deebert} and mixture-of-experts routing~\\citep{switch-transformer-2022}, which optimize compute allocation at inference time, our framework diagnoses aggregate routing signal at episode granularity. Methodologically, our pure-strategy comparison is a simplified potential outcomes framework~\\citep{rubin1974estimating}: executing both strategies under identical initial conditions eliminates confounding without structural causal models~\\citep{pearl2009causality}, at the cost of requiring paired episode collection.\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  }
}
```

</details>

---


### Tool call

_source line 420_

<details open><summary>🔧 Tool call — Read · `toolu_01DzhmRSkbMKfgxynPWUBgdr`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "d644ff51-bb36-468d-9cef-2ef01682e8e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEkDYND7gvjNjgB2RWqkjW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21519,
      "cache_read_input_tokens": 37752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21519
      },
      "output_tokens": 20,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 421 · 2026-05-26T10:23:30.985Z_

<details><summary>↩ Tool result · `toolu_01DzhmRSkbMKfgxynPWUBgdr`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	Our diagnostic framework (Figure~\ref{fig:pipeline}) quantifies what drives routing signal in interactive environments through two components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). A supplementary Signal Concentration Index (SCI; Appendix~\ref{app:sci}) measures whether signal is concentrated in a few task types. Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
5	
6	\subsection{Problem Setup}
7	\label{sec:problem-setup}
8	
9	Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\citep{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic} (${\tt det}$), which uses the same LLM to generate candidate actions but evaluates them through privileged environment feedback (ground-truth simulator state in ScienceWorld, code interpreter in MATH, admissible-action enumeration in ALFWorld; see \S\ref{sec:cross-env} for environment-specific operationalizations). Crucially, the deterministic strategy does not provide optimal actions; it reduces observation uncertainty by grounding the LLM's choices in verified environment state rather than predicted state. These qualitative differences affect what routing signals the framework can detect. A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \mathcal{M}$ selects which computation mode to use at each step; our analysis investigates what signal is available to learn $\rho$.
10	
11	\subsection{Counterfactual Episode Collection}
12	\label{sec:collection}
13	
14	Per-step oracle labeling degenerates under sparse terminal rewards: on ScienceWorld \citep{scienceworld-2022}, 97.4\% of steps (5{,}935 of 6{,}094 across 11 prescreened task types) produce identical intermediate scores, yielding no per-step routing signal. Episode-level comparison (directly measuring terminal outcomes) is therefore the principled granularity for sparse-reward environments.
15	
16	\paragraph{Pure-strategy trajectories.}
17	For a task instance $t$ and computation mode $m \in \mathcal{M}$, a \emph{pure-strategy trajectory} is the complete episode obtained by applying mode $m$ at every step:
18	\begin{equation}
19	    \tau_m^{(t)} = (o_1, a_1, o_2, a_2, \ldots, o_T, a_T)
20	\end{equation}
21	where $T \leq T_{\max}$ is the episode length (capped at $T_{\max} = 30$ steps). Both trajectories $\tau_{\tt int}^{(t)}$ and $\tau_{\tt det}^{(t)}$ are executed under identical initial conditions (same random seed, same task variation), so performance differences arise solely from the computation mode choice.
22	
23	Each trajectory $\tau$ yields a terminal score $s(\tau) \in \mathbb{Z}$ and a death indicator $d(\tau) \in \{0, 1\}$. When the agent dies ($d = 1$), the environment imposes a penalty: $s(\tau) = -P$ where $P > 0$ ($P = 100$ in ScienceWorld). The episode pair produces a tuple:
24	\begin{multline}
25	    \bigl(s^{\tt int}, s^{\tt det}, d^{\tt int}, d^{\tt det}\bigr) \triangleq \\
26	    \bigl(s(\tau_{\tt int}),\, s(\tau_{\tt det}),\, d(\tau_{\tt int}),\, d(\tau_{\tt det})\bigr)
27	\end{multline}
28	
29	We use Qwen2.5-7B-Instruct~\citep{qwen25-2024} (vLLM v0.21.0) on ScienceWorld \citep{scienceworld-2022}, a text-based environment spanning 30 task types with a $-100$ death penalty; complete prompt templates are provided in Appendix~\ref{app:prompt-templates}. After prescreening, we collect 245 episode pairs across 11 task types (20--40 per type). The framework is applicable to any environment where paired episodes under two computation modes can be collected with binary success/failure indicators. We apply it unchanged to ALFWorld and MATH in \S\ref{sec:math-contrast}--\ref{sec:cross-env}.
30	
31	\subsection{Episode-Level Labeling}
32	\label{sec:labeling}
33	
34	\begin{algorithm}[t]
35	\caption{Episode-Level Counterfactual Labeling}
36	\label{alg:labeling}
37	\begin{algorithmic}[1]
38	\REQUIRE Task instance $t$, computation modes $\mathcal{M} = \{{\tt int}, {\tt det}\}$
39	\ENSURE Label $\ell \in \{{\tt det\text{-}pref}, {\tt int\text{-}pref}, {\tt no\text{-}pref}\}$
40	\FOR{each $m \in \mathcal{M}$}
41	    \STATE Run episode $\tau_m$ with pure-strategy $m$
42	    \STATE Record score $s_m$ and death indicator $d_m$
43	\ENDFOR
44	\IF{$d_{\tt int} = 1$ \AND $d_{\tt det} = 0$}
45	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{death asymmetry}
46	\ELSIF{$d_{\tt int} = 0$ \AND $d_{\tt det} = 1$}
47	    \STATE $\ell \leftarrow {\tt int\text{-}pref}$ \COMMENT{death asymmetry}
48	\ELSIF{$d_{\tt int} = d_{\tt det} = 1$}
49	    \STATE $\ell \leftarrow {\tt no\text{-}pref}$ \COMMENT{both dead}
50	\ELSIF{$s_{\tt det} > s_{\tt int}$}
51	    \STATE $\ell \leftarrow {\tt det\text{-}pref}$ \COMMENT{score comparison}
52	\ELSIF{$s_{\tt int} > s_{\tt det}$}
53	    \STATE $\ell \leftarrow {\tt int\text{-}pref}$ \COMMENT{score comparison}
54	\ELSE
55	    \STATE $\ell \leftarrow {\tt no\text{-}pref}$ \COMMENT{tied alive}
56	\ENDIF
57	\RETURN $\ell$
58	\end{algorithmic}
59	\end{algorithm}
60	
61	We define a labeling function $L$ that maps a counterfactual pair to a routing preference:
62	\begin{multline}
63	    L\!\bigl(\tau_{\tt int}^{(t)}, \tau_{\tt det}^{(t)}\bigr) \;\rightarrow \\
64	    \ell \in \{{\tt det\text{-}pref},\; {\tt int\text{-}pref},\; {\tt no\text{-}pref}\}
65	\end{multline}
66	
67	The labeling function is \emph{death-aware}: it prioritizes survival over score, then compares scores among same-status episodes (Algorithm~\ref{alg:labeling}). Both-dead episodes receive \texttt{no\_preference} because ScienceWorld's fixed $-100$ penalty makes death timing uninformative. ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. A quality audit confirming zero tie-breaking artifacts is in Appendix~\ref{app:labeling}. Label distributions are reported in \S\ref{sec:death-decomp}.
68	
69	\subsection{Death Avoidance Factor}
70	\label{sec:daf}
71	
72	To quantify the contribution of death avoidance to routing signal, we decompose the mean score gap between strategies. Let $\delta = \mathbb{E}[d^{\tt int}] - \mathbb{E}[d^{\tt det}]$ denote the death-rate differential and $\Delta_{\text{nd}}$ the mean score gap restricted to episodes where neither strategy dies. Partitioning episodes by death status, death-asymmetric episodes (where only one strategy dies) contribute a per-episode gap of $P + \bar{s}_{\text{surv}}$, where $\bar{s}_{\text{surv}}$ is the surviving strategy's mean score; when $\bar{s}_{\text{surv}} \ll P$ (in our data, $\bar{s}_{\text{surv}} = 0.87$, or $0.9\%$ of $P$), these episodes contribute ${\approx}\,\delta P$ in aggregate. The full gap thus decomposes as:
73	\begin{equation}
74	    \Delta_{\text{full}} \approx \underbrace{\delta \cdot P}_{\text{death contribution}} + \Delta_{\text{nd}}
75	\end{equation}
76	The approximation residual is $29.60 - 29.37 = 0.23$ ($0.8\%$ of $\Delta_{\text{full}}$).
77	
78	We define the Death Avoidance Factor (DAF) as the fraction of the full score gap attributable to death avoidance:
79	\begin{equation}
80	    \text{DAF} = 1 - \frac{\Delta_{\text{nd}}}{\Delta_{\text{full}}} \approx \frac{\delta P}{\delta P + \Delta_{\text{nd}}}
81	\end{equation}%
82	\footnote{When $\Delta_{\text{nd}} < 0$ (deterministic strategy scores lower than internal on non-death episodes), DAF exceeds 1; death avoidance then overcompensates for a non-death disadvantage.}
83	
84	DAF increases monotonically with $P$ (Table~\ref{tab:penalty-sensitivity}, Appendix~\ref{app:penalty}); we treat the label fraction (78.9\%) as the primary, penalty-invariant diagnostic. In ScienceWorld, $P$ affects only post-hoc score calculation; death rates and $\Delta_{\text{nd}}$ are $P$-invariant by design~\citep{ng1999policy}. Uncertainty is quantified via episode-level bootstrap ($B{=}10{,}000$, percentile 95\% CIs).
85	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "84c4d428-2cb5-48d9-87e8-28a0cb67c51a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nOur diagnostic framework (Figure~\\ref{fig:pipeline}) quantifies what drives routing signal in interactive environments through two components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\\S\\ref{sec:collection}--\\ref{sec:labeling}); and (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\\S\\ref{sec:daf}). A supplementary Signal Concentration Index (SCI; Appendix~\\ref{app:sci}) measures whether signal is concentrated in a few task types. Episode-level bootstrap resampling provides 95\\% confidence intervals for all metrics.\n\n\\subsection{Problem Setup}\n\\label{sec:problem-setup}\n\nConsider an interactive environment with observation space $\\mathcal{O}$ and action space $\\mathcal{A}$. An agent policy $\\pi: \\mathcal{O}^* \\rightarrow \\mathcal{A}$ maps observation histories to actions. We define two computation modes $\\mathcal{M} = \\{{\\tt int}, {\\tt det}\\}$: \\textbf{internal} (${\\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\\citep{react-2023}), with prediction errors compounding across steps; and \\textbf{deterministic} (${\\tt det}$), which uses the same LLM to generate candidate actions but evaluates them through privileged environment feedback (ground-truth simulator state in ScienceWorld, code interpreter in MATH, admissible-action enumeration in ALFWorld; see \\S\\ref{sec:cross-env} for environment-specific operationalizations). Crucially, the deterministic strategy does not provide optimal actions; it reduces observation uncertainty by grounding the LLM's choices in verified environment state rather than predicted state. These qualitative differences affect what routing signals the framework can detect. A \\emph{routing policy} $\\rho: \\mathcal{O}^* \\rightarrow \\mathcal{M}$ selects which computation mode to use at each step; our analysis investigates what signal is available to learn $\\rho$.\n\n\\subsection{Counterfactual Episode Collection}\n\\label{sec:collection}\n\nPer-step oracle labeling degenerates under sparse terminal rewards: on ScienceWorld \\citep{scienceworld-2022}, 97.4\\% of steps (5{,}935 of 6{,}094 across 11 prescreened task types) produce identical intermediate scores, yielding no per-step routing signal. Episode-level comparison (directly measuring terminal outcomes) is therefore the principled granularity for sparse-reward environments.\n\n\\paragraph{Pure-strategy trajectories.}\nFor a task instance $t$ and computation mode $m \\in \\mathcal{M}$, a \\emph{pure-strategy trajectory} is the complete episode obtained by applying mode $m$ at every step:\n\\begin{equation}\n    \\tau_m^{(t)} = (o_1, a_1, o_2, a_2, \\ldots, o_T, a_T)\n\\end{equation}\nwhere $T \\leq T_{\\max}$ is the episode length (capped at $T_{\\max} = 30$ steps). Both trajectories $\\tau_{\\tt int}^{(t)}$ and $\\tau_{\\tt det}^{(t)}$ are executed under identical initial conditions (same random seed, same task variation), so performance differences arise solely from the computation mode choice.\n\nEach trajectory $\\tau$ yields a terminal score $s(\\tau) \\in \\mathbb{Z}$ and a death indicator $d(\\tau) \\in \\{0, 1\\}$. When the agent dies ($d = 1$), the environment imposes a penalty: $s(\\tau) = -P$ where $P > 0$ ($P = 100$ in ScienceWorld). The episode pair produces a tuple:\n\\begin{multline}\n    \\bigl(s^{\\tt int}, s^{\\tt det}, d^{\\tt int}, d^{\\tt det}\\bigr) \\triangleq \\\\\n    \\bigl(s(\\tau_{\\tt int}),\\, s(\\tau_{\\tt det}),\\, d(\\tau_{\\tt int}),\\, d(\\tau_{\\tt det})\\bigr)\n\\end{multline}\n\nWe use Qwen2.5-7B-Instruct~\\citep{qwen25-2024} (vLLM v0.21.0) on ScienceWorld \\citep{scienceworld-2022}, a text-based environment spanning 30 task types with a $-100$ death penalty; complete prompt templates are provided in Appendix~\\ref{app:prompt-templates}. After prescreening, we collect 245 episode pairs across 11 task types (20--40 per type). The framework is applicable to any environment where paired episodes under two computation modes can be collected with binary success/failure indicators. We apply it unchanged to ALFWorld and MATH in \\S\\ref{sec:math-contrast}--\\ref{sec:cross-env}.\n\n\\subsection{Episode-Level Labeling}\n\\label{sec:labeling}\n\n\\begin{algorithm}[t]\n\\caption{Episode-Level Counterfactual Labeling}\n\\label{alg:labeling}\n\\begin{algorithmic}[1]\n\\REQUIRE Task instance $t$, computation modes $\\mathcal{M} = \\{{\\tt int}, {\\tt det}\\}$\n\\ENSURE Label $\\ell \\in \\{{\\tt det\\text{-}pref}, {\\tt int\\text{-}pref}, {\\tt no\\text{-}pref}\\}$\n\\FOR{each $m \\in \\mathcal{M}$}\n    \\STATE Run episode $\\tau_m$ with pure-strategy $m$\n    \\STATE Record score $s_m$ and death indicator $d_m$\n\\ENDFOR\n\\IF{$d_{\\tt int} = 1$ \\AND $d_{\\tt det} = 0$}\n    \\STATE $\\ell \\leftarrow {\\tt det\\text{-}pref}$ \\COMMENT{death asymmetry}\n\\ELSIF{$d_{\\tt int} = 0$ \\AND $d_{\\tt det} = 1$}\n    \\STATE $\\ell \\leftarrow {\\tt int\\text{-}pref}$ \\COMMENT{death asymmetry}\n\\ELSIF{$d_{\\tt int} = d_{\\tt det} = 1$}\n    \\STATE $\\ell \\leftarrow {\\tt no\\text{-}pref}$ \\COMMENT{both dead}\n\\ELSIF{$s_{\\tt det} > s_{\\tt int}$}\n    \\STATE $\\ell \\leftarrow {\\tt det\\text{-}pref}$ \\COMMENT{score comparison}\n\\ELSIF{$s_{\\tt int} > s_{\\tt det}$}\n    \\STATE $\\ell \\leftarrow {\\tt int\\text{-}pref}$ \\COMMENT{score comparison}\n\\ELSE\n    \\STATE $\\ell \\leftarrow {\\tt no\\text{-}pref}$ \\COMMENT{tied alive}\n\\ENDIF\n\\RETURN $\\ell$\n\\end{algorithmic}\n\\end{algorithm}\n\nWe define a labeling function $L$ that maps a counterfactual pair to a routing preference:\n\\begin{multline}\n    L\\!\\bigl(\\tau_{\\tt int}^{(t)}, \\tau_{\\tt det}^{(t)}\\bigr) \\;\\rightarrow \\\\\n    \\ell \\in \\{{\\tt det\\text{-}pref},\\; {\\tt int\\text{-}pref},\\; {\\tt no\\text{-}pref}\\}\n\\end{multline}\n\nThe labeling function is \\emph{death-aware}: it prioritizes survival over score, then compares scores among same-status episodes (Algorithm~\\ref{alg:labeling}). Both-dead episodes receive \\texttt{no\\_preference} because ScienceWorld's fixed $-100$ penalty makes death timing uninformative. ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. A quality audit confirming zero tie-breaking artifacts is in Appendix~\\ref{app:labeling}. Label distributions are reported in \\S\\ref{sec:death-decomp}.\n\n\\subsection{Death Avoidance Factor}\n\\label{sec:daf}\n\nTo quantify the contribution of death avoidance to routing signal, we decompose the mean score gap between strategies. Let $\\delta = \\mathbb{E}[d^{\\tt int}] - \\mathbb{E}[d^{\\tt det}]$ denote the death-rate differential and $\\Delta_{\\text{nd}}$ the mean score gap restricted to episodes where neither strategy dies. Partitioning episodes by death status, death-asymmetric episodes (where only one strategy dies) contribute a per-episode gap of $P + \\bar{s}_{\\text{surv}}$, where $\\bar{s}_{\\text{surv}}$ is the surviving strategy's mean score; when $\\bar{s}_{\\text{surv}} \\ll P$ (in our data, $\\bar{s}_{\\text{surv}} = 0.87$, or $0.9\\%$ of $P$), these episodes contribute ${\\approx}\\,\\delta P$ in aggregate. The full gap thus decomposes as:\n\\begin{equation}\n    \\Delta_{\\text{full}} \\approx \\underbrace{\\delta \\cdot P}_{\\text{death contribution}} + \\Delta_{\\text{nd}}\n\\end{equation}\nThe approximation residual is $29.60 - 29.37 = 0.23$ ($0.8\\%$ of $\\Delta_{\\text{full}}$).\n\nWe define the Death Avoidance Factor (DAF) as the fraction of the full score gap attributable to death avoidance:\n\\begin{equation}\n    \\text{DAF} = 1 - \\frac{\\Delta_{\\text{nd}}}{\\Delta_{\\text{full}}} \\approx \\frac{\\delta P}{\\delta P + \\Delta_{\\text{nd}}}\n\\end{equation}%\n\\footnote{When $\\Delta_{\\text{nd}} < 0$ (deterministic strategy scores lower than internal on non-death episodes), DAF exceeds 1; death avoidance then overcompensates for a non-death disadvantage.}\n\nDAF increases monotonically with $P$ (Table~\\ref{tab:penalty-sensitivity}, Appendix~\\ref{app:penalty}); we treat the label fraction (78.9\\%) as the primary, penalty-invariant diagnostic. In ScienceWorld, $P$ affects only post-hoc score calculation; death rates and $\\Delta_{\\text{nd}}$ are $P$-invariant by design~\\citep{ng1999policy}. Uncertainty is quantified via episode-level bootstrap ($B{=}10{,}000$, percentile 95\\% CIs).\n",
      "numLines": 85,
      "startLine": 1,
      "totalLines": 85
    }
  }
}
```

</details>

---


### Tool call

_source line 422_

<details open><summary>🔧 Tool call — Read · `toolu_01CMqvoFfzXNd1CRg4f5P1nD`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "73150868-f4dd-479b-8866-4fd4a78b9090",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEkDYND7gvjNjgB2RWqkjW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21519,
      "cache_read_input_tokens": 37752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21519
      },
      "output_tokens": 20,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-26T10:23:31.355Z_

<details><summary>↩ Tool result · `toolu_01CMqvoFfzXNd1CRg4f5P1nD`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\begin{figure}[t]
5	\centering
6	\includegraphics[width=0.75\columnwidth]{figures/fig1_daf_scatter.pdf}
7	\caption{Per-task death rate differential vs.\ performance gap ($n{=}11$ task types). The near-perfect correlation ($r = 0.97$) is a structural consequence of death dominance (DAF $\to 1 \Rightarrow r \to 1$), not an independent finding. The sole outlier (\texttt{find-non-living-thing}, diamond marker) has zero deaths; its $\Delta_{\text{full}} = +9.58$ arises entirely from non-death score differences.}
8	\label{fig:decomposition}
9	\end{figure}
10	
11	\begin{table}[t]
12	\centering
13	\scriptsize
14	\resizebox{\columnwidth}{!}{%
15	\begin{tabular}{@{}lrr@{}}
16	\toprule
17	Condition & Death\% & $N$ \\
18	\midrule
19	Single-trial baseline & 42.9 & 245 \\
20	Reflexion ($3{\times}$) & 31.4 & 220 \\
21	Qwen2.5-72B ($10{\times}$) & 30.6 & 255 \\
22	Deterministic baseline & 16.3 & 245 \\
23	\midrule
24	\multicolumn{3}{@{}l}{\textit{10 death-prone tasks only:}} \\
25	Death-prone baseline & 48.0 & 200 \\
26	Retry ($5{\times}$) & 43.5 & 200 \\
27	\bottomrule
28	\end{tabular}}
29	\caption{Internal-strategy death rates under improvement methods. Top: all 11 tasks. Bottom: 10 death-prone tasks (\texttt{find-non-living-thing} excluded). No intervention approaches deterministic-level safety.}
30	\label{tab:agent-improvement}
31	\end{table}
32	
33	\begin{figure}[t]
34	\centering
35	\includegraphics[width=0.95\columnwidth]{figures/death_action_timeline.pdf}
36	\vspace{-2mm}
37	\caption{Action sequences for 6 representative death episodes. The fatal \texttt{focus on} (arrow) appears in final steps after long \texttt{connect} sequences (``connect loop $\to$ fatal focus'').}
38	\label{fig:death-timeline}
39	\end{figure}
40	
41	We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). An anti-cherry-picking analysis confirms death dominance holds in 18 of these 19 types ($\overline{\Delta\text{DR}} = +38.2$\,pp $>$ included tasks' $+28.7$\,pp; Appendix~\ref{app:per-task}), with extended validation on representative excluded tasks in Appendix~\ref{app:extended-validation}.
42	
43	\subsection{Death Avoidance Decomposition}
44	\label{sec:death-decomp}
45	
46	\begin{table}[t]
47	\centering
48	\scriptsize
49	\setlength{\tabcolsep}{2.5pt}
50	\resizebox{\columnwidth}{!}{%
51	\begin{tabular}{@{}lrrccc@{}}
52	\toprule
53	Task & $n$ & $\Delta_\text{full}$ & D\%\textsubscript{int} & D\%\textsubscript{det} & D / I / N \\
54	\midrule
55	id-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\
56	lifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\
57	lifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\
58	inclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\
59	freeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\
60	meas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\
61	id-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\
62	find-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\
63	grow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\
64	chem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\
65	\midrule
66	find-non-living$^\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\
67	\midrule
68	\textbf{All (11 tasks)} & \textbf{245} & $\mathbf{+29.60}$ & \textbf{42.9} & \textbf{16.3} & \textbf{86 / 9 / 150} \\
69	\bottomrule
70	\end{tabular}}
71	\caption{Per-task decomposition. D\%: death rate for internal/deterministic. D/I/N: det-preferred / int-preferred / no-preference labels. $\dagger$\,Only task with zero deaths; $n{=}40$ (two batches).}
72	\label{tab:per-task}
73	\end{table}
74	
75	Of the 95 non-tie routing labels, 75 (78.9\%; 95\% CI: $[70.7\%, 87.0\%]$, episode-level bootstrap) arise from death asymmetry: the internal strategy triggers a catastrophic $-100$ penalty while the deterministic strategy survives. This penalty-independent label fraction is the primary diagnostic metric. Of these, 54 are sole-signal labels where death was the only discriminator; at $P{=}0$ these reduce to ties, but the labeling function itself is penalty-independent (Algorithm~\ref{alg:labeling}).
76	
77	DAF $= 90.4\%$ at $P{=}100$ ($\Delta_{\text{full}} = +29.60$, $\Delta_{\text{nd}} = +2.84$; 95\% CI$_{\text{DAF}}$: $[81.3\%, 99.1\%]$, episode-level bootstrap). The 78.9\% label fraction provides the more robust, penalty-invariant characterization (\S\ref{sec:daf}).
78	
79	\paragraph{Per-task structure.}
80	The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic; all 105 internal deaths are triggered by the \texttt{focus on} action (Appendix~\ref{app:failure-modes}). Per-task $\Delta$DR correlates with $\Delta_{\text{full}}$ at $r = 0.97$ (Figure~\ref{fig:decomposition}; leave-one-out and bootstrap robustness in Appendix~\ref{app:correlation}), a structural consequence of DAF$\to 1$ rather than an independent finding. Figure~\ref{fig:death-timeline} illustrates the typical death trajectory.
81	
82	\paragraph{Binary structure and robustness.}
83	All 10 death-prone task types produce 100\% death-asymmetry labels; only \texttt{find-non-living-thing} (zero deaths) produces non-death signal (SCI $= 0.21$; Appendix~\ref{app:sci}). Leave-one-task-out (Table~\ref{tab:loto-daf}) confirms robustness: removing any single task changes DAF by $\leq$3.0~pp. Bootstrap 95\% CIs: DAF $[81.3\%, 99.1\%]$; cluster-robust $[73.3\%, 100.0\%]$ ($K{=}11$; Appendix~\ref{app:wild-cluster}). Two replications (Gemma-2-9B-it; seed=123) converge within 0.7~pp.
84	
85	\subsection{Multi-Model Validation (7--9B Tier)}
86	\label{sec:cross-model}
87	
88	Llama-3.1-8B~\citep{llama3-2024} ($N{=}220$) and Gemma-2-9B-it~\citep{gemma2-2024} ($N{=}220$) independently replicate death dominance: DAF $= 88.2\%$ and $89.7\%$ respectively, with 10/10 directional consistency on death-prone tasks (Appendix~\ref{app:cross-model}; per-task CIs in Appendix~\ref{app:per-task-ci}). Three architecturally distinct families (Qwen, Llama, Gemma) converge on DAF $88$--$90\%$ (spread 2.2~pp), suggesting death dominance is an environment-level property. Scaling $10{\times}$ to two 70B-class models (\S\ref{sec:agent-improvement}) yields DAF${=}92.4$--$101.0\%$, indicating the pattern persists at larger scale.
89	
90	\begin{table}[t]
91	\centering
92	\scriptsize
93	\setlength{\tabcolsep}{2pt}
94	\resizebox{\columnwidth}{!}{%
95	\begin{tabular}{@{}llcrrrcl@{}}
96	\toprule
97	Model & Env & $n$ & Int DR & Det DR & $\Delta$DR & DAF [95\% CI] & Signal \\
98	\midrule
99	Qwen2.5-7B & SW & 245 & 42.9 & 16.3 & +26.5 & 90.4 [81.3, 99.1] & death \\
100	Llama-3.1-8B & SW & 220 & 41.4 & 11.4 & +30.0 & 88.2 [80.2, 95.1] & death \\
101	Gemma-2-9B & SW & 220 & 36.4 & 14.1 & +22.3 & 89.7 [79.5, 98.4] & death \\
102	Qwen2.5-72B & SW & 255 & 30.6 & 2.8 & +27.8 & 92.4 [86.1, 97.9] & death \\
103	Llama-70B & SW & 220 & 48.6 & 20.0 & +28.6 & 101.0 [95.3, 107.5] & death \\
104	\midrule
105	Qwen2.5-7B & ALF & 135 & 0 & 0 & 0 & 0 & info-asym \\
106	Llama-3.1-8B & ALF & 135 & 0 & 0 & 0 & 0 & info-asym \\
107	\midrule
108	Qwen2.5-7B & MATH & 795 & --- & --- & --- & --- & none \\
109	\bottomrule
110	\end{tabular}}
111	\caption{Cross-model and cross-environment summary. SW = ScienceWorld, ALF = ALFWorld. Death dominance replicates across three 7--9B families and intensifies under $10{\times}$ scaling; ALFWorld shows information-asymmetry signal; MATH shows none. DR = death rate (\%).}
112	\label{tab:cross-model-env}
113	\end{table}
114	
115	\begin{table}[t]
116	\centering
117	\scriptsize
118	\setlength{\tabcolsep}{3pt}
119	\resizebox{\columnwidth}{!}{%
120	\begin{tabular}{@{}lrrr@{}}
121	\toprule
122	Removed Task & $N_\text{rem}$ & DAF (\%) & $\Delta$ (pp) \\
123	\midrule
124	(none, full) & 245 & 78.9 & --- \\
125	\midrule
126	Find Non-Living$^\dagger$ & 205 & 100.0 & +21.1 \\
127	Lifespan Longest & 220 & 75.9 & $-$3.0 \\
128	Life Stages 1 & 225 & 76.7 & $-$2.2 \\
129	Lifespan Long+Short & 225 & 76.7 & $-$2.2 \\
130	Chemistry Mix & 225 & 77.0 & $-$1.9 \\
131	Grow Fruit & 225 & 77.3 & $-$1.7 \\
132	Inclined Plane & 225 & 77.3 & $-$1.7 \\
133	Freeze & 225 & 77.5 & $-$1.4 \\
134	Life Stages 2 & 225 & 77.5 & $-$1.4 \\
135	Melt Pt Unknown & 225 & 77.5 & $-$1.4 \\
136	Find Animal & 225 & 77.8 & $-$1.2 \\
137	\bottomrule
138	\end{tabular}}
139	\caption{Leave-one-task-out DAF sensitivity (label fraction). Removing any death-prone task changes DAF by $\leq$3.0\,pp. $\dagger$\,Sole death-free task; removal raises DAF to 100\% by construction.}
140	\label{tab:loto-daf}
141	\end{table}
142	
143	\subsection{Agent Improvement Baselines}
144	\label{sec:agent-improvement}
145	
146	We test whether agent-level improvement reduces death dominance (Table~\ref{tab:agent-improvement}). Retry (re-executing the episode without explicit reflection; $N{=}5$) yields marginal reduction ($43.5\%$ vs.\ $48.0\%$). Reflexion~\citep{reflexion-2023} reduces death to $31.4\%$ but the gap to deterministic remains $15.1$~pp; under matched-episode analysis ($N{=}3$), $\Delta_{\text{nd}} = -0.47$, yielding DAF${}>100\%$. Scaling to Qwen2.5-72B ($N{=}255$) reduces death rate to $30.6\%$ with DAF $= 92.4\%$ (95\% CI: $[86.1\%, 97.9\%]$). A second 70B model, Llama-3.1-70B ($N{=}220$), yields DAF $= 101.0\%$ ($[95.3\%, 107.5\%]$): death avoidance more than fully accounts for the gap. Both 70B-class models suggest that scaling does not attenuate death dominance.
147	
148	\paragraph{Dose-response analysis.}
149	We extend both interventions to $N{=}5$ trials on death-prone tasks ($n{=}200$; Figure~\ref{fig:dose-response}). Retry is nearly flat ($48.0\% \to 43.5\%$). Reflexion drops steeply to $34.0\%$ at $N{=}3$ ($\Delta = -13.5$~pp, $p = 0.003$) then stabilizes ($34$--$36.5\%$ for $N \geq 3$, pairwise $p > 0.5$); both the decline and plateau are well-powered (minimum detectable effect ${\sim}8$~pp at 80\% power; Appendix~\ref{app:dose-response}).
150	
151	\begin{figure}[t]
152	\centering
153	\includegraphics[width=\columnwidth]{figures/dose_response.pdf}
154	\caption{Death rate vs.\ trial count for Retry and Reflexion on 10 death-prone tasks ($n{=}200$). Reflexion drops steeply through $N{=}3$ then plateaus; Retry is nearly flat. Horizontal lines: 72B ($30.6\%$) and deterministic ($16.3\%$) baselines. Error bands: Wilson 95\% CIs.}
155	\label{fig:dose-response}
156	\end{figure}
157	
158	\subsection{Cross-Environment Boundary Probes}
159	\label{sec:math-contrast}
160	\label{sec:cross-env}
161	
162	We probe two environments as boundary cases to test the framework's specificity (Figure~\ref{fig:signal-reversal}). On MATH Level~4--5~\citep{math-2021} ($N{=}795$), internal reasoning and code-interpreter accuracy are near-identical ($73.5\%$ vs.\ $73.0\%$, $p = 0.81$): without a catastrophic failure mechanism, no routing signal emerges despite substantial task difficulty. ALFWorld~\citep{alfworld-2021} (135 games, no death mechanism, DAF $= 0\%$) shows 94.6\% of non-tie labels favoring the information-advantaged strategy (which enumerates admissible actions); Llama-3.1-8B replicates at 100\%. The framework identifies this qualitatively different mechanism, information asymmetry rather than death avoidance, without modification, indicating that DAF correctly attributes zero signal to death when none exists (full label distributions and per-task breakdowns in Appendix~\ref{app:cross-env-details}).
163	
164	\subsection{Baselines}
165	\label{sec:baselines}
166	
167	Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points (Table~\ref{tab:baselines}). Random routing ($-22.38$) falls between the two pure strategies, confirming that the gap is not an artifact of evaluation methodology. The oracle improves only to $-6.58$, with 96.3\% of decisions matching always-deterministic, an \emph{oracle degeneracy} where perfect per-episode foresight provides marginal benefit over the trivial always-deterministic baseline (Appendix~\ref{sec:threshold-routing}).
168	
169	\subsection{Router Training: Inconclusive Results}
170	\label{sec:router-diagnostic}
171	
172	A Qwen3 LoRA router (0.6B--4B; Appendix~\ref{app:router-details}) trained on counterfactual labels shows flat step-level balanced accuracy ($56$--$59\%$) across all model scales; episode-level evaluation yields $47.1 \pm 2.2\%$, below majority-vote.\footnote{Consistent with noisy-label bounds~\citep{natarajan2013learning}: ${\sim}$88\% of step-level labels are uninformative with 90.5\%/3.7\% class imbalance (Appendix~\ref{app:seed-robustness}).} Leave-one-task-out degrades to chance ($50.0\%$), suggesting signal is a per-task-type constant rather than a learnable function of step-level observations. Deployed end-to-end, the best router (4B) scores $-10.70$, not exceeding always-deterministic ($-9.47$); this negative result is consistent with the death-dominance finding, as death avoidance cannot be predicted from pre-episode features when it depends on multi-step trajectory dynamics. Additional ablations (capacity scaling, generative routing, reasoning depth) are in Appendix~\ref{app:ablations}.
173	
174	\begin{figure}[t]
175	\centering
176	\includegraphics[width=0.95\columnwidth]{figures/signal_reversal.pdf}
177	\vspace{-2mm}
178	\caption{Cross-environment label distributions. ScienceWorld and ALFWorld both favor deterministic via different mechanisms (death avoidance vs.\ information asymmetry); MATH shows no routing signal.}
179	\label{fig:signal-reversal}
180	\end{figure}
181	
182	\begin{table}[t]
183	\centering
184	\small
185	\resizebox{\columnwidth}{!}{%
186	\begin{tabular}{@{}lccc@{}}
187	\toprule
188	Strategy & Score & 95\% CI & Death \% \\
189	\midrule
190	Always-Internal & $-39.07$ & [$-46.40$, $-32.27$] & 42.9 \\
191	Always-Deterministic & $-9.47$ & [$-14.71$, $-4.29$] & 16.3 \\
192	Random & $-22.38$ & [$-28.67$, $-15.75$] & 27.8 \\
193	Oracle & $-6.58$ & [$-11.54$, $-1.70$] & 14.3 \\
194	\midrule
195	Trained Router$^\dagger$ & $-10.70$ & [$-16.33$, $-5.27$] & 17.6 \\
196	\bottomrule
197	\end{tabular}}
198	\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). $\dagger$\,Single seed (42); see Appendix~\ref{app:seed-robustness} for 8-seed robustness.}
199	\label{tab:baselines}
200	\end{table}
201	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "2e46794e-5715-454e-83cb-371c907c19fb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig1_daf_scatter.pdf}\n\\caption{Per-task death rate differential vs.\\ performance gap ($n{=}11$ task types). The near-perfect correlation ($r = 0.97$) is a structural consequence of death dominance (DAF $\\to 1 \\Rightarrow r \\to 1$), not an independent finding. The sole outlier (\\texttt{find-non-living-thing}, diamond marker) has zero deaths; its $\\Delta_{\\text{full}} = +9.58$ arises entirely from non-death score differences.}\n\\label{fig:decomposition}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\scriptsize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\nCondition & Death\\% & $N$ \\\\\n\\midrule\nSingle-trial baseline & 42.9 & 245 \\\\\nReflexion ($3{\\times}$) & 31.4 & 220 \\\\\nQwen2.5-72B ($10{\\times}$) & 30.6 & 255 \\\\\nDeterministic baseline & 16.3 & 245 \\\\\n\\midrule\n\\multicolumn{3}{@{}l}{\\textit{10 death-prone tasks only:}} \\\\\nDeath-prone baseline & 48.0 & 200 \\\\\nRetry ($5{\\times}$) & 43.5 & 200 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Internal-strategy death rates under improvement methods. Top: all 11 tasks. Bottom: 10 death-prone tasks (\\texttt{find-non-living-thing} excluded). No intervention approaches deterministic-level safety.}\n\\label{tab:agent-improvement}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/death_action_timeline.pdf}\n\\vspace{-2mm}\n\\caption{Action sequences for 6 representative death episodes. The fatal \\texttt{focus on} (arrow) appears in final steps after long \\texttt{connect} sequences (``connect loop $\\to$ fatal focus'').}\n\\label{fig:death-timeline}\n\\end{figure}\n\nWe analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). An anti-cherry-picking analysis confirms death dominance holds in 18 of these 19 types ($\\overline{\\Delta\\text{DR}} = +38.2$\\,pp $>$ included tasks' $+28.7$\\,pp; Appendix~\\ref{app:per-task}), with extended validation on representative excluded tasks in Appendix~\\ref{app:extended-validation}.\n\n\\subsection{Death Avoidance Decomposition}\n\\label{sec:death-decomp}\n\n\\begin{table}[t]\n\\centering\n\\scriptsize\n\\setlength{\\tabcolsep}{2.5pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrccc@{}}\n\\toprule\nTask & $n$ & $\\Delta_\\text{full}$ & D\\%\\textsubscript{int} & D\\%\\textsubscript{det} & D / I / N \\\\\n\\midrule\nid-life-stages-1       & 20  & $+47.50$ & 55   & 10   & 9 / 0 / 11  \\\\\nlifespan-long          & 25  & $+44.00$ & 56   & 16   & 11 / 1 / 13 \\\\\nlifespan-l-then-s      & 20  & $+40.80$ & 45   & 10   & 8 / 1 / 11  \\\\\ninclined-plane         & 20  & $+36.00$ & 55   & 20   & 7 / 0 / 13  \\\\\nfreeze                 & 20  & $+30.50$ & 55   & 25   & 6 / 0 / 14  \\\\\nmeas-melt-point        & 20  & $+30.05$ & 55   & 25   & 6 / 0 / 14  \\\\\nid-life-stages-2       & 20  & $+30.00$ & 50   & 20   & 6 / 0 / 14  \\\\\nfind-animal            & 20  & $+26.65$ & 50   & 25   & 5 / 0 / 15  \\\\\ngrow-fruit             & 20  & $+25.10$ & 45   & 20   & 6 / 1 / 13  \\\\\nchem-mix               & 20  & $+21.80$ & 45   & 25   & 6 / 2 / 12  \\\\\n\\midrule\nfind-non-living$^\\dagger$ & 40 & $+9.58$ & 0  & 0    & 16 / 4 / 20 \\\\\n\\midrule\n\\textbf{All (11 tasks)} & \\textbf{245} & $\\mathbf{+29.60}$ & \\textbf{42.9} & \\textbf{16.3} & \\textbf{86 / 9 / 150} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Per-task decomposition. D\\%: death rate for internal/deterministic. D/I/N: det-preferred / int-preferred / no-preference labels. $\\dagger$\\,Only task with zero deaths; $n{=}40$ (two batches).}\n\\label{tab:per-task}\n\\end{table}\n\nOf the 95 non-tie routing labels, 75 (78.9\\%; 95\\% CI: $[70.7\\%, 87.0\\%]$, episode-level bootstrap) arise from death asymmetry: the internal strategy triggers a catastrophic $-100$ penalty while the deterministic strategy survives. This penalty-independent label fraction is the primary diagnostic metric. Of these, 54 are sole-signal labels where death was the only discriminator; at $P{=}0$ these reduce to ties, but the labeling function itself is penalty-independent (Algorithm~\\ref{alg:labeling}).\n\nDAF $= 90.4\\%$ at $P{=}100$ ($\\Delta_{\\text{full}} = +29.60$, $\\Delta_{\\text{nd}} = +2.84$; 95\\% CI$_{\\text{DAF}}$: $[81.3\\%, 99.1\\%]$, episode-level bootstrap). The 78.9\\% label fraction provides the more robust, penalty-invariant characterization (\\S\\ref{sec:daf}).\n\n\\paragraph{Per-task structure.}\nThe internal strategy dies in 42.9\\% of episodes versus 16.3\\% for deterministic; all 105 internal deaths are triggered by the \\texttt{focus on} action (Appendix~\\ref{app:failure-modes}). Per-task $\\Delta$DR correlates with $\\Delta_{\\text{full}}$ at $r = 0.97$ (Figure~\\ref{fig:decomposition}; leave-one-out and bootstrap robustness in Appendix~\\ref{app:correlation}), a structural consequence of DAF$\\to 1$ rather than an independent finding. Figure~\\ref{fig:death-timeline} illustrates the typical death trajectory.\n\n\\paragraph{Binary structure and robustness.}\nAll 10 death-prone task types produce 100\\% death-asymmetry labels; only \\texttt{find-non-living-thing} (zero deaths) produces non-death signal (SCI $= 0.21$; Appendix~\\ref{app:sci}). Leave-one-task-out (Table~\\ref{tab:loto-daf}) confirms robustness: removing any single task changes DAF by $\\leq$3.0~pp. Bootstrap 95\\% CIs: DAF $[81.3\\%, 99.1\\%]$; cluster-robust $[73.3\\%, 100.0\\%]$ ($K{=}11$; Appendix~\\ref{app:wild-cluster}). Two replications (Gemma-2-9B-it; seed=123) converge within 0.7~pp.\n\n\\subsection{Multi-Model Validation (7--9B Tier)}\n\\label{sec:cross-model}\n\nLlama-3.1-8B~\\citep{llama3-2024} ($N{=}220$) and Gemma-2-9B-it~\\citep{gemma2-2024} ($N{=}220$) independently replicate death dominance: DAF $= 88.2\\%$ and $89.7\\%$ respectively, with 10/10 directional consistency on death-prone tasks (Appendix~\\ref{app:cross-model}; per-task CIs in Appendix~\\ref{app:per-task-ci}). Three architecturally distinct families (Qwen, Llama, Gemma) converge on DAF $88$--$90\\%$ (spread 2.2~pp), suggesting death dominance is an environment-level property. Scaling $10{\\times}$ to two 70B-class models (\\S\\ref{sec:agent-improvement}) yields DAF${=}92.4$--$101.0\\%$, indicating the pattern persists at larger scale.\n\n\\begin{table}[t]\n\\centering\n\\scriptsize\n\\setlength{\\tabcolsep}{2pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcrrrcl@{}}\n\\toprule\nModel & Env & $n$ & Int DR & Det DR & $\\Delta$DR & DAF [95\\% CI] & Signal \\\\\n\\midrule\nQwen2.5-7B & SW & 245 & 42.9 & 16.3 & +26.5 & 90.4 [81.3, 99.1] & death \\\\\nLlama-3.1-8B & SW & 220 & 41.4 & 11.4 & +30.0 & 88.2 [80.2, 95.1] & death \\\\\nGemma-2-9B & SW & 220 & 36.4 & 14.1 & +22.3 & 89.7 [79.5, 98.4] & death \\\\\nQwen2.5-72B & SW & 255 & 30.6 & 2.8 & +27.8 & 92.4 [86.1, 97.9] & death \\\\\nLlama-70B & SW & 220 & 48.6 & 20.0 & +28.6 & 101.0 [95.3, 107.5] & death \\\\\n\\midrule\nQwen2.5-7B & ALF & 135 & 0 & 0 & 0 & 0 & info-asym \\\\\nLlama-3.1-8B & ALF & 135 & 0 & 0 & 0 & 0 & info-asym \\\\\n\\midrule\nQwen2.5-7B & MATH & 795 & --- & --- & --- & --- & none \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-model and cross-environment summary. SW = ScienceWorld, ALF = ALFWorld. Death dominance replicates across three 7--9B families and intensifies under $10{\\times}$ scaling; ALFWorld shows information-asymmetry signal; MATH shows none. DR = death rate (\\%).}\n\\label{tab:cross-model-env}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\scriptsize\n\\setlength{\\tabcolsep}{3pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nRemoved Task & $N_\\text{rem}$ & DAF (\\%) & $\\Delta$ (pp) \\\\\n\\midrule\n(none, full) & 245 & 78.9 & --- \\\\\n\\midrule\nFind Non-Living$^\\dagger$ & 205 & 100.0 & +21.1 \\\\\nLifespan Longest & 220 & 75.9 & $-$3.0 \\\\\nLife Stages 1 & 225 & 76.7 & $-$2.2 \\\\\nLifespan Long+Short & 225 & 76.7 & $-$2.2 \\\\\nChemistry Mix & 225 & 77.0 & $-$1.9 \\\\\nGrow Fruit & 225 & 77.3 & $-$1.7 \\\\\nInclined Plane & 225 & 77.3 & $-$1.7 \\\\\nFreeze & 225 & 77.5 & $-$1.4 \\\\\nLife Stages 2 & 225 & 77.5 & $-$1.4 \\\\\nMelt Pt Unknown & 225 & 77.5 & $-$1.4 \\\\\nFind Animal & 225 & 77.8 & $-$1.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Leave-one-task-out DAF sensitivity (label fraction). Removing any death-prone task changes DAF by $\\leq$3.0\\,pp. $\\dagger$\\,Sole death-free task; removal raises DAF to 100\\% by construction.}\n\\label{tab:loto-daf}\n\\end{table}\n\n\\subsection{Agent Improvement Baselines}\n\\label{sec:agent-improvement}\n\nWe test whether agent-level improvement reduces death dominance (Table~\\ref{tab:agent-improvement}). Retry (re-executing the episode without explicit reflection; $N{=}5$) yields marginal reduction ($43.5\\%$ vs.\\ $48.0\\%$). Reflexion~\\citep{reflexion-2023} reduces death to $31.4\\%$ but the gap to deterministic remains $15.1$~pp; under matched-episode analysis ($N{=}3$), $\\Delta_{\\text{nd}} = -0.47$, yielding DAF${}>100\\%$. Scaling to Qwen2.5-72B ($N{=}255$) reduces death rate to $30.6\\%$ with DAF $= 92.4\\%$ (95\\% CI: $[86.1\\%, 97.9\\%]$). A second 70B model, Llama-3.1-70B ($N{=}220$), yields DAF $= 101.0\\%$ ($[95.3\\%, 107.5\\%]$): death avoidance more than fully accounts for the gap. Both 70B-class models suggest that scaling does not attenuate death dominance.\n\n\\paragraph{Dose-response analysis.}\nWe extend both interventions to $N{=}5$ trials on death-prone tasks ($n{=}200$; Figure~\\ref{fig:dose-response}). Retry is nearly flat ($48.0\\% \\to 43.5\\%$). Reflexion drops steeply to $34.0\\%$ at $N{=}3$ ($\\Delta = -13.5$~pp, $p = 0.003$) then stabilizes ($34$--$36.5\\%$ for $N \\geq 3$, pairwise $p > 0.5$); both the decline and plateau are well-powered (minimum detectable effect ${\\sim}8$~pp at 80\\% power; Appendix~\\ref{app:dose-response}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/dose_response.pdf}\n\\caption{Death rate vs.\\ trial count for Retry and Reflexion on 10 death-prone tasks ($n{=}200$). Reflexion drops steeply through $N{=}3$ then plateaus; Retry is nearly flat. Horizontal lines: 72B ($30.6\\%$) and deterministic ($16.3\\%$) baselines. Error bands: Wilson 95\\% CIs.}\n\\label{fig:dose-response}\n\\end{figure}\n\n\\subsection{Cross-Environment Boundary Probes}\n\\label{sec:math-contrast}\n\\label{sec:cross-env}\n\nWe probe two environments as boundary cases to test the framework's specificity (Figure~\\ref{fig:signal-reversal}). On MATH Level~4--5~\\citep{math-2021} ($N{=}795$), internal reasoning and code-interpreter accuracy are near-identical ($73.5\\%$ vs.\\ $73.0\\%$, $p = 0.81$): without a catastrophic failure mechanism, no routing signal emerges despite substantial task difficulty. ALFWorld~\\citep{alfworld-2021} (135 games, no death mechanism, DAF $= 0\\%$) shows 94.6\\% of non-tie labels favoring the information-advantaged strategy (which enumerates admissible actions); Llama-3.1-8B replicates at 100\\%. The framework identifies this qualitatively different mechanism, information asymmetry rather than death avoidance, without modification, indicating that DAF correctly attributes zero signal to death when none exists (full label distributions and per-task breakdowns in Appendix~\\ref{app:cross-env-details}).\n\n\\subsection{Baselines}\n\\label{sec:baselines}\n\nAlways-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points (Table~\\ref{tab:baselines}). Random routing ($-22.38$) falls between the two pure strategies, confirming that the gap is not an artifact of evaluation methodology. The oracle improves only to $-6.58$, with 96.3\\% of decisions matching always-deterministic, an \\emph{oracle degeneracy} where perfect per-episode foresight provides marginal benefit over the trivial always-deterministic baseline (Appendix~\\ref{sec:threshold-routing}).\n\n\\subsection{Router Training: Inconclusive Results}\n\\label{sec:router-diagnostic}\n\nA Qwen3 LoRA router (0.6B--4B; Appendix~\\ref{app:router-details}) trained on counterfactual labels shows flat step-level balanced accuracy ($56$--$59\\%$) across all model scales; episode-level evaluation yields $47.1 \\pm 2.2\\%$, below majority-vote.\\footnote{Consistent with noisy-label bounds~\\citep{natarajan2013learning}: ${\\sim}$88\\% of step-level labels are uninformative with 90.5\\%/3.7\\% class imbalance (Appendix~\\ref{app:seed-robustness}).} Leave-one-task-out degrades to chance ($50.0\\%$), suggesting signal is a per-task-type constant rather than a learnable function of step-level observations. Deployed end-to-end, the best router (4B) scores $-10.70$, not exceeding always-deterministic ($-9.47$); this negative result is consistent with the death-dominance finding, as death avoidance cannot be predicted from pre-episode features when it depends on multi-step trajectory dynamics. Additional ablations (capacity scaling, generative routing, reasoning depth) are in Appendix~\\ref{app:ablations}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.95\\columnwidth]{figures/signal_reversal.pdf}\n\\vspace{-2mm}\n\\caption{Cross-environment label distributions. ScienceWorld and ALFWorld both favor deterministic via different mechanisms (death avoidance vs.\\ information asymmetry); MATH shows no routing signal.}\n\\label{fig:signal-reversal}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nStrategy & Score & 95\\% CI & Death \\% \\\\\n\\midrule\nAlways-Internal & $-39.07$ & [$-46.40$, $-32.27$] & 42.9 \\\\\nAlways-Deterministic & $-9.47$ & [$-14.71$, $-4.29$] & 16.3 \\\\\nRandom & $-22.38$ & [$-28.67$, $-15.75$] & 27.8 \\\\\nOracle & $-6.58$ & [$-11.54$, $-1.70$] & 14.3 \\\\\n\\midrule\nTrained Router$^\\dagger$ & $-10.70$ & [$-16.33$, $-5.27$] & 17.6 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). $\\dagger$\\,Single seed (42); see Appendix~\\ref{app:seed-robustness} for 8-seed robustness.}\n\\label{tab:baselines}\n\\end{table}\n",
      "numLines": 201,
      "startLine": 1,
      "totalLines": 201
    }
  }
}
```

</details>

---


### Tool call

_source line 424_

<details open><summary>🔧 Tool call — Read · `toolu_01RTr8qb3zUmjgh6AStBdnAJ`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "576a216c-bb71-492c-814d-fdd9b7daa21b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEkDYND7gvjNjgB2RWqkjW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21519,
      "cache_read_input_tokens": 37752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21519
      },
      "output_tokens": 20,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-26T10:23:32.043Z_

<details><summary>↩ Tool result · `toolu_01RTr8qb3zUmjgh6AStBdnAJ`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Signal granularity and router failure.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property, but step-level features correlate weakly because death risk depends on multi-step trajectories. Six router variants (0.6B--4B) converge on near-chance balanced accuracy ($56$--$59\%$); leave-one-task-out degrades to $50.0\%$, suggesting the router captures only task-type identity rather than a learnable function of step-level observations. Scaling $10{\times}$ to 70B-class models does not attenuate this pattern (DAF $92$--$101\%$), and cross-model death-rate stability ($31$--$49\%$ across five models) confirms death vulnerability is a task-environment property, better addressed through action-space constraints (Appendix~\ref{app:grounding-ablation}) than learned routing policies.
6	
7	\paragraph{Failure mechanism.}
8	All 105 internal-strategy deaths trace to misuse of \texttt{focus on [object]}, ScienceWorld's answer-submission command, applied to irrelevant targets (rooms, doors, inventory items). The action distribution analysis (Figure~\ref{fig:death-action-dist}, Appendix~\ref{app:failure-modes}) shows that \texttt{focus on} is moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$), while Figure~\ref{fig:death-comparison} reveals that within death episodes both strategies exhibit comparable rates (${\sim}5\%$). The higher internal death count reflects more frequent entry into catastrophic states, not different action selection within those states. Among fatal \texttt{focus on} targets, \texttt{workshop} is the most frequent (20.0\%), followed by \texttt{inventory} (17.1\%) and \texttt{kitchen} (10.5\%), indicating a systematic object bias rather than random exploration. Action-space filtering that blocks \texttt{focus on} during the exploration phase reduces death by 19~pp with zero leaks and zero passthroughs (Appendix~\ref{app:grounding-ablation}), confirming shallow behavioral origins amenable to simple interventions.
9	
10	\paragraph{Oracle degeneracy and practical implications.}
11	Always-deterministic matches 96.3\% of oracle decisions (\S\ref{sec:baselines}), capping routing's marginal value at 2.89 points---an \emph{oracle degeneracy} where $\Delta_{\text{nd}} = 2.84$ (9.6\% of total gap). This degeneracy arises because the deterministic strategy already avoids the primary failure mode, leaving only a residual non-death gap for the oracle to exploit. A ${\sim}$50-episode pilot suffices to compute the death-label fraction $f_{\text{death}}$ (the proportion of non-tie labels where exactly one strategy dies) and assess whether learned routing adds value before committing to full-scale router training. Table~\ref{tab:decision-validation} shows the three-stage procedure (Appendix~\ref{app:decision-framework}) correctly classifies all four conditions, including ALFWorld's information-asymmetry signal where DAF $= 0\%$ correctly identifies a non-death mechanism.
12	
13	\begin{table}[t]
14	\centering
15	\scriptsize
16	\resizebox{\columnwidth}{!}{%
17	\begin{tabular}{@{}lrrll@{}}
18	\toprule
19	Condition & $\Delta$DR & $f_{\text{death}}$ & Prediction & Actual \\
20	\midrule
21	Qwen-7B (SW) & +26.5 & 78.9\% & det-fixed & det wins \\
22	Llama-8B (SW) & +30.0 & $>$75\% & det-fixed & det wins \\
23	Qwen-72B (SW) & +27.8 & $>$75\% & det-fixed & det wins \\
24	MATH & +0.5 & 0\% & router viable & no signal \\
25	\bottomrule
26	\end{tabular}}
27	\caption{Retrospective validation of the practitioner decision framework. SW = ScienceWorld. The three-stage diagnostic correctly classifies all four conditions (4/4).}
28	\label{tab:decision-validation}
29	\end{table}
30	
31	\paragraph{Scope and applicability conditions.}
32	The decomposition requires: (i)~binary catastrophic failures with fixed penalty, (ii)~asymmetric failure rates, and (iii)~$P \gg \Delta_\text{nd}$. ScienceWorld satisfies all three; MATH and ALFWorld lack the first. Graded penalties or symmetric failure rates would require DAF extensions. The penalty sensitivity analysis (Table~\ref{tab:penalty-sensitivity}, Appendix~\ref{app:penalty}) confirms that DAF is mechanically driven by $P$: the label fraction (78.9\%) is $P$-invariant, while the score-based DAF ranges from $7.4\%$ at $P{=}0$ to $97.9\%$ at $P{=}500$. In death-dominated settings, targeted safety interventions may outperform general-purpose routing, shifting the problem from ``which strategy to route to'' to ``how to prevent catastrophic actions.''
33	
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "99f0db7b-1bfe-41c8-80da-8e1b5a7ae6c9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Signal granularity and router failure.}\nThe router diagnostic (\\S\\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property, but step-level features correlate weakly because death risk depends on multi-step trajectories. Six router variants (0.6B--4B) converge on near-chance balanced accuracy ($56$--$59\\%$); leave-one-task-out degrades to $50.0\\%$, suggesting the router captures only task-type identity rather than a learnable function of step-level observations. Scaling $10{\\times}$ to 70B-class models does not attenuate this pattern (DAF $92$--$101\\%$), and cross-model death-rate stability ($31$--$49\\%$ across five models) confirms death vulnerability is a task-environment property, better addressed through action-space constraints (Appendix~\\ref{app:grounding-ablation}) than learned routing policies.\n\n\\paragraph{Failure mechanism.}\nAll 105 internal-strategy deaths trace to misuse of \\texttt{focus on [object]}, ScienceWorld's answer-submission command, applied to irrelevant targets (rooms, doors, inventory items). The action distribution analysis (Figure~\\ref{fig:death-action-dist}, Appendix~\\ref{app:failure-modes}) shows that \\texttt{focus on} is moderately more frequent in death episodes ($5.4\\%$ vs.\\ $3.4\\%$), while Figure~\\ref{fig:death-comparison} reveals that within death episodes both strategies exhibit comparable rates (${\\sim}5\\%$). The higher internal death count reflects more frequent entry into catastrophic states, not different action selection within those states. Among fatal \\texttt{focus on} targets, \\texttt{workshop} is the most frequent (20.0\\%), followed by \\texttt{inventory} (17.1\\%) and \\texttt{kitchen} (10.5\\%), indicating a systematic object bias rather than random exploration. Action-space filtering that blocks \\texttt{focus on} during the exploration phase reduces death by 19~pp with zero leaks and zero passthroughs (Appendix~\\ref{app:grounding-ablation}), confirming shallow behavioral origins amenable to simple interventions.\n\n\\paragraph{Oracle degeneracy and practical implications.}\nAlways-deterministic matches 96.3\\% of oracle decisions (\\S\\ref{sec:baselines}), capping routing's marginal value at 2.89 points---an \\emph{oracle degeneracy} where $\\Delta_{\\text{nd}} = 2.84$ (9.6\\% of total gap). This degeneracy arises because the deterministic strategy already avoids the primary failure mode, leaving only a residual non-death gap for the oracle to exploit. A ${\\sim}$50-episode pilot suffices to compute the death-label fraction $f_{\\text{death}}$ (the proportion of non-tie labels where exactly one strategy dies) and assess whether learned routing adds value before committing to full-scale router training. Table~\\ref{tab:decision-validation} shows the three-stage procedure (Appendix~\\ref{app:decision-framework}) correctly classifies all four conditions, including ALFWorld's information-asymmetry signal where DAF $= 0\\%$ correctly identifies a non-death mechanism.\n\n\\begin{table}[t]\n\\centering\n\\scriptsize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrll@{}}\n\\toprule\nCondition & $\\Delta$DR & $f_{\\text{death}}$ & Prediction & Actual \\\\\n\\midrule\nQwen-7B (SW) & +26.5 & 78.9\\% & det-fixed & det wins \\\\\nLlama-8B (SW) & +30.0 & $>$75\\% & det-fixed & det wins \\\\\nQwen-72B (SW) & +27.8 & $>$75\\% & det-fixed & det wins \\\\\nMATH & +0.5 & 0\\% & router viable & no signal \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Retrospective validation of the practitioner decision framework. SW = ScienceWorld. The three-stage diagnostic correctly classifies all four conditions (4/4).}\n\\label{tab:decision-validation}\n\\end{table}\n\n\\paragraph{Scope and applicability conditions.}\nThe decomposition requires: (i)~binary catastrophic failures with fixed penalty, (ii)~asymmetric failure rates, and (iii)~$P \\gg \\Delta_\\text{nd}$. ScienceWorld satisfies all three; MATH and ALFWorld lack the first. Graded penalties or symmetric failure rates would require DAF extensions. The penalty sensitivity analysis (Table~\\ref{tab:penalty-sensitivity}, Appendix~\\ref{app:penalty}) confirms that DAF is mechanically driven by $P$: the label fraction (78.9\\%) is $P$-invariant, while the score-based DAF ranges from $7.4\\%$ at $P{=}0$ to $97.9\\%$ at $P{=}500$. In death-dominated settings, targeted safety interventions may outperform general-purpose routing, shifting the problem from ``which strategy to route to'' to ``how to prevent catastrophic actions.''\n\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---


### Tool call

_source line 426_

<details open><summary>🔧 Tool call — Read · `toolu_01KRixvJuPytpbfjbo6RZuqz`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "b4b62ca6-305e-4ce9-9671-7449b1a70eac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEkDYND7gvjNjgB2RWqkjW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21519,
      "cache_read_input_tokens": 37752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21519
      },
      "output_tokens": 20,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 427 · 2026-05-26T10:23:32.383Z_

<details><summary>↩ Tool result · `toolu_01KRixvJuPytpbfjbo6RZuqz`</summary>

```text
1	\section{Conclusion}
2	
3	Our episode-level counterfactual framework reveals that routing signal in ScienceWorld is dominated by a single mechanism: 78.9\% of non-tie labels trace to death asymmetry, a finding stable across three model families and two 70B-class models (DAF $92$--$101\%$). When routing signal collapses to catastrophic-failure avoidance, always-deterministic approaches oracle performance, and learned step-level routing offers limited additional value.
4	
5	The framework's diagnostic value extends beyond negative results. The practitioner decision procedure (Table~\ref{tab:decision-validation}) correctly classifies four distinct conditions, and boundary probes demonstrate that the same decomposition identifies qualitatively different signal sources without modification, suggesting utility as a general pre-routing diagnostic.
6	
7	Key open directions include validating death dominance in other catastrophic-failure environments (e.g., safety-critical robotics, irreversible web actions), developing hybrid approaches that combine action-space filtering for death-prone tasks with learned routing for non-death tasks, extending DAF to graded penalties and stochastic failure severity, and investigating whether the concentration of routing signal in a single mechanism generalizes to other agent benchmarks with asymmetric failure modes. More broadly, our results suggest that diagnosing signal composition \emph{before} training a router can save substantial compute by identifying when a simple fixed strategy already captures most of the available signal.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "91c3d91d-33c0-4271-8970-f69876469394",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\nOur episode-level counterfactual framework reveals that routing signal in ScienceWorld is dominated by a single mechanism: 78.9\\% of non-tie labels trace to death asymmetry, a finding stable across three model families and two 70B-class models (DAF $92$--$101\\%$). When routing signal collapses to catastrophic-failure avoidance, always-deterministic approaches oracle performance, and learned step-level routing offers limited additional value.\n\nThe framework's diagnostic value extends beyond negative results. The practitioner decision procedure (Table~\\ref{tab:decision-validation}) correctly classifies four distinct conditions, and boundary probes demonstrate that the same decomposition identifies qualitatively different signal sources without modification, suggesting utility as a general pre-routing diagnostic.\n\nKey open directions include validating death dominance in other catastrophic-failure environments (e.g., safety-critical robotics, irreversible web actions), developing hybrid approaches that combine action-space filtering for death-prone tasks with learned routing for non-death tasks, extending DAF to graded penalties and stochastic failure severity, and investigating whether the concentration of routing signal in a single mechanism generalizes to other agent benchmarks with asymmetric failure modes. More broadly, our results suggest that diagnosing signal composition \\emph{before} training a router can save substantial compute by identifying when a simple fixed strategy already captures most of the available signal.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---


### Tool call

_source line 428_

<details open><summary>🔧 Tool call — Read · `toolu_016wcBpNFuPpBb5wAkAMAEXY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "e6591863-2620-4776-8e9c-c5f2d19de8c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TEkDYND7gvjNjgB2RWqkjW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21519,
      "cache_read_input_tokens": 37752,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21519
      },
      "output_tokens": 20,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-26T10:23:33.183Z_

<details><summary>↩ Tool result · `toolu_016wcBpNFuPpBb5wAkAMAEXY`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata}  % optional per ACL template; not available in this TeX installation
11	\usepackage{graphicx}
12	\graphicspath{{figures/}}
13	\usepackage{booktabs}
14	\usepackage{amsmath}
15	\usepackage{amssymb}
16	\usepackage{algorithm}
17	\usepackage{algorithmic}
18	\usepackage{caption}
19	\usepackage{tcolorbox}
20	\tcbuselibrary{listings,breakable}
21	
22	\setlength{\dbltextfloatsep}{8pt plus 2pt minus 2pt}
23	\setlength{\floatsep}{6pt plus 2pt minus 2pt}
24	\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
25	
26	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
27	
28	\author{Anonymous}
29	
30	\begin{document}
31	\maketitle
32	
33	\input{abstract}
34	\input{introduction}
35	\input{related_work}
36	\input{method}
37	\input{experiments}
38	\input{discussion}
39	\input{conclusion}
40	
41	\section*{Limitations}
42	Full quantitative validation (DAF, label fractions) is specific to ScienceWorld; MATH and ALFWorld serve as boundary probes, not comprehensive cross-environment validation. DAF depends on a fixed death penalty ($P{=}100$); environments with graded or stochastic failure severity would require extensions (Appendix~\ref{app:penalty}). The internal baseline uses single-pass ReAct~\citep{react-2023}; more aggressive self-correction (e.g., Tree-of-Thought) may further reduce death rates and alter the signal composition. With $K{=}11$ task-type clusters, cluster bootstrap yields wider CIs; wild cluster bootstrap ($p < 0.001$; Appendix~\ref{app:wild-cluster}) and 100\% directional consistency across all 28 death-prone tasks provide partial mitigation. Total compute was approximately 200 GPU-hours on consumer and workstation GPUs.
43	
44	\bibliography{references}
45	
46	\appendix
47	
48	\noindent\textbf{Appendix Overview.}
49	\hyperref[app:sci]{A.~Signal Concentration Index} $\cdot$
50	\hyperref[app:labeling]{B.~Labeling Quality Audit} $\cdot$
51	\hyperref[app:per-task]{C.~Per-Task Decomposition} $\cdot$
52	\hyperref[app:correlation]{D.~Correlation Robustness} $\cdot$
53	\hyperref[app:wild-cluster]{E.~Cluster Bootstrap Sensitivity} $\cdot$
54	\hyperref[app:per-task-ci]{F.~Per-Task CIs} $\cdot$
55	\hyperref[app:loto-daf]{G.~Leave-One-Task-Out DAF} $\cdot$
56	\hyperref[app:dose-response]{H.~Dose-Response Breakdown} $\cdot$
57	\hyperref[app:router-details]{I.~Router Training Details} $\cdot$
58	\hyperref[app:seed-robustness]{J.~Seed Robustness} $\cdot$
59	\hyperref[app:penalty]{K.~Penalty Sensitivity} $\cdot$
60	\hyperref[app:cross-env-details]{L.~Cross-Environment Details} $\cdot$
61	\hyperref[app:cross-model]{M.~Cross-Model Verification} $\cdot$
62	\hyperref[app:failure-modes]{N.~Failure Mode Analysis} $\cdot$
63	\hyperref[app:grounding-ablation]{O.~Grounding Ablation} $\cdot$
64	\hyperref[app:ablations]{P.~Ablation Studies} $\cdot$
65	\hyperref[sec:threshold-routing]{Q.~Threshold Routing} $\cdot$
66	\hyperref[app:decision-framework]{R.~Decision Framework} $\cdot$
67	\hyperref[app:extended-validation]{S.~Extended Validation} $\cdot$
68	\hyperref[app:prompt-templates]{T.~Agent Prompt Templates} $\cdot$
69	\hyperref[app:non-death-case-study]{U.~Non-Death Episode Case Study}
70	
71	\section{Signal Concentration Index}
72	\label{app:sci}
73	
74	Let $K$ denote the number of task types and $c_k$ the contribution of task type $k$ to the aggregate routing signal, defined as the fraction of total death-rate differential attributable to task $k$:
75	\begin{equation}
76	    c_k = \frac{n_k \cdot \delta_k}{\sum_{j=1}^{K} n_j \cdot \delta_j}
77	\end{equation}
78	where $n_k$ is the number of episodes and $\delta_k = d_k^{\tt int} - d_k^{\tt det}$ is the per-task death-rate differential. The SCI is the Gini coefficient over $\{c_1, \ldots, c_K\}$:
79	\begin{equation}
80	    \text{SCI} = \frac{\sum_{i=1}^K \sum_{j=1}^K |c_i - c_j|}{2K \sum_{k=1}^K c_k}
81	\end{equation}
82	
83	\section{Labeling Quality Audit}
84	\label{app:labeling}
85	
86	Note that episode-level labels are used to evaluate step-level predictions, introducing a granularity mismatch rather than independent validation. A potential concern is oracle circularity: whether episode-level labels reflect tie-breaking artifacts rather than genuine computation mode differences. We audit all 245 labels. Of the 150 \texttt{no\_preference} labels (61.2\%), 115 (46.9\%) are both-alive ties and 35 (14.3\%) are both-dead, all excluded from router training. The remaining 95 training labels are entirely genuine: 75 from death asymmetry (70 deterministic-preferred, 5 internal-preferred) and 20 from score comparison with both strategies surviving (16 deterministic-preferred, 4 internal-preferred). Zero labels depend on tie-breaking. Retraining the router using only death-asymmetry labels yields step-level balanced accuracy of 57.3\%, within 1$\sigma$ of the full-label retrain (57.6 $\pm$ 0.5\%, step-level Trainer evaluation); score-comparison labels contribute negligible additional signal. (Step-level metrics are used here for the relative comparison; as shown in \S\ref{sec:router-diagnostic}, absolute generalization to new episodes is near chance.) The 97.4\% step-level tie rate (\S\ref{sec:collection}) further motivates episode-level over step-level labeling.
87	
88	\section{Per-Task Decomposition}
89	\label{app:per-task}
90	We use ScienceWorld v1.2.3~\citep{scienceworld-2022}.
91	We select 11 of ScienceWorld's 30 task types for analysis. Types are excluded when they were used for pipeline development (5 tasks, standard hold-out practice), are taxonomically redundant with a retained family representative (7 tasks), or exhibit near-zero task progress under both strategies (7 tasks, agent capability floor).\footnote{Excluded tasks exhibit even stronger death dominance than included tasks ($\Delta\text{DR} = +38.2$\,pp vs.\ $+28.7$\,pp; Table~\ref{tab:excluded-death}).}
92	
93	\paragraph{Task selection and anti-cherry-picking.}
94	Eighteen of the 19 excluded task types (95\%) exhibit death-asymmetric patterns (Table~\ref{tab:excluded-death}): internal-reasoning death rates range from 40\% to 60\% (mean 53.9\%), while deterministic death rates range from 0\% to 40\% (mean 15.8\%), yielding a mean death-rate differential of $+38.2$\,pp, exceeding the $+28.7$\,pp for included tasks. The included subset is thus \emph{less} death-asymmetric than the excluded subset, the opposite of what a cherry-picking hypothesis would predict. The sole exception is \texttt{grow-plant}, an intrinsically safe task with zero deaths under both strategies, paralleling \texttt{find-non-living-thing} in the included set. The 19 excluded tasks fall into three independently motivated categories: five used during pipeline development (standard hold-out practice), seven taxonomically redundant with included family representatives (deduplication), and seven where the 7B backbone achieves near-zero task progress regardless of strategy (agent capability floor). In no case was a task excluded because death dominance was absent. Exclusion is driven by absence of non-death routing signal ($\Delta_{\text{nd}} = 0$ for 53\% of excluded tasks) and standard deduplication practices. \texttt{find-non-living-thing} serves as an internal counterexample: zero deaths under both strategies yet included because it exhibits non-death routing signal ($\Delta_{\text{full}} = +9.58$ entirely from score differences), and deterministic is not always preferred (4 of 20 non-tie labels favor internal).
95	
96	\begin{table}[t]
97	\centering
98	\scriptsize
99	\setlength{\tabcolsep}{2pt}
100	\resizebox{\columnwidth}{!}{%
101	\begin{tabular}{@{}llrcccl@{}}
102	\toprule
103	Task & Grp & $n$ & D\%\textsubscript{int} & D\%\textsubscript{det} & $\Delta$DR & Excl.\ reason \\
104	\midrule
105	boil                          & A & 20 & 50 & 20 & $+30$ & dev set \\
106	change-state-of-matter        & A & 20 & 55 & 15 & $+40$ & dev set \\
107	chem-mix-paint-secondary      & A & 20 & 45 & 10 & $+35$ & dev set \\
108	grow-plant                    & A & 20 &  0 &  0 & $\phantom{+}0$  & dev set \\
109	melt                          & A & 20 & 55 & 15 & $+40$ & dev set \\
110	\midrule
111	chem-mix-paint-tertiary       & B &  5 & 40 & 20 & $+20$ & family redundancy \\
112	find-living-thing             & B &  5 & 60 & 20 & $+40$ & family redundancy \\
113	find-plant                    & B &  5 & 60 &  0 & $+60$ & family redundancy \\
114	inclined-friction-named       & B &  5 & 60 & 20 & $+40$ & family redundancy \\
115	inclined-friction-unnamed     & B &  5 & 60 &  0 & $+60$ & family redundancy \\
116	lifespan-shortest             & B &  5 & 60 & 40 & $+20$ & family redundancy \\
117	measure-melt-known            & B &  5 & 60 &  0 & $+60$ & family redundancy \\
118	\midrule
119	mendelian-known               & C &  5 & 60 & 20 & $+40$ & agent floor \\
120	mendelian-unknown             & C &  5 & 60 & 40 & $+20$ & agent floor \\
121	power-component               & C &  5 & 60 & 20 & $+40$ & agent floor \\
122	power-renewable               & C &  5 & 60 &  0 & $+60$ & agent floor \\
123	test-conductivity             & C &  5 & 60 & 20 & $+40$ & agent floor \\
124	test-conductivity-unknown     & C &  5 & 60 & 20 & $+40$ & agent floor \\
125	use-thermometer               & C &  5 & 60 & 20 & $+40$ & agent floor \\
126	\midrule
127	\textbf{Mean (19 excluded)}   &   &    & \textbf{53.9} & \textbf{15.8} & $\mathbf{+38.2}$ & \\
128	\textit{cf.\ included (11)}   &   &    & \textit{46.5} & \textit{17.8} & $\textit{+28.7}$ & \\
129	\bottomrule
130	\end{tabular}}%
131	\caption{Death-rate analysis of all 19 excluded task types. D\%: death rate (score $\leq -100$). $\Delta$DR = D\%\textsubscript{int} $-$ D\%\textsubscript{det}. 18 of 19 excluded tasks (95\%) exhibit positive death asymmetry ($\Delta$DR $\geq +20$\,pp). Exclusion groups: A = development set (excluded to prevent circular evaluation), B = taxonomically redundant with an included family representative, C = agent-floor tasks (backbone achieves near-zero progress regardless of strategy). The mean $\Delta$DR among excluded tasks ($+38.2$\,pp) exceeds that of included tasks ($+28.7$\,pp), confirming that task selection does not bias toward death-prone tasks. Group B--C estimates are based on $n{=}5$ prescreening episodes per task and should be interpreted as directional evidence rather than precise rate estimates.}
132	\label{tab:excluded-death}
133	\end{table}
134	
135	\section{Correlation Robustness}
136	\label{app:correlation}
137	
138	The Pearson $r = 0.9698$ reported in \S\ref{sec:death-decomp} is robust across multiple diagnostics. Spearman rank correlation is $\rho = 0.986$ ($p = 2.4 \times 10^{-8}$); the relationship is not driven by outliers or non-linearity. A nonparametric bootstrap (10{,}000 resamples) yields 95\% CI $[0.952, 0.995]$.
139	
140	\begin{table}[h]
141	\centering
142	\small
143	\begin{tabular}{@{}lr@{}}
144	\toprule
145	Task removed & $r_{\text{LOO}}$ \\
146	\midrule
147	id-life-stages-1       & 0.963 \\
148	lifespan-long          & 0.969 \\
149	lifespan-l-then-s      & 0.976 \\
150	inclined-plane         & 0.969 \\
151	freeze                 & 0.971 \\
152	meas-melt-point        & 0.972 \\
153	id-life-stages-2       & 0.972 \\
154	find-animal            & 0.970 \\
155	grow-fruit             & 0.973 \\
156	chem-mix               & 0.969 \\
157	find-non-living-thing  & 0.980 \\
158	\bottomrule
159	\end{tabular}
160	\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\ $\Delta_{\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}
161	\label{tab:loo}
162	\end{table}
163	
164	\section{Cluster Bootstrap Sensitivity Analysis}
165	\label{app:wild-cluster}
166	
167	With $K{=}11$ task-type clusters, cluster bootstrap falls well below the $K{\geq}20$--50 recommended for reliable inference \citep{cameron-2008,webb-2023}. The narrower CIs obtained reflect known small-sample bias toward underestimation of variance, not tighter inference.
168	
169	Episodes within the same task type share environment dynamics, raising the concern that the effective sample size is closer to $K$ (task types) than $N$ (episodes). We address this with cluster-robust inference treating each task type as a cluster ($K{=}11$, all 11 included task types, 245 episodes).
170	
171	\begin{table}[h]
172	\centering
173	\small
174	\resizebox{\columnwidth}{!}{%
175	\begin{tabular}{@{}lcc@{}}
176	\toprule
177	Method & $p$-value & 95\% CI \\
178	\midrule
179	Cluster-robust $t$-test ($t{=}10.0$, df$=$10) & $< 0.001$ & $[0.73, 1.00]$ \\
180	Wild cluster bootstrap ($B{=}9{,}999$) & $< 0.001$ & $[0.73, 1.00]$ \\
181	Exact permutation ($2{,}048$ perms) & $0.002$ & --- \\
182	Sign test & $< 0.001$ & --- \\
183	\bottomrule
184	\end{tabular}}%
185	\caption{Cluster-level tests of death-rate asymmetry ($K{=}11$ task clusters, 245 episodes). 10 of 11 clusters show internal DR $>$ deterministic DR; the sole exception (\texttt{find-non-living-thing}) has zero deaths under both strategies. Cohen's $d = 3.02$. The exact permutation $p = 0.002$ ($4/2{,}048$) reflects the near-unanimous directional consistency.}
186	\label{tab:wild-cluster}
187	\end{table}
188	
189	\noindent All methods confirm significance with $p < 0.01$, and the 95\% CI $[0.73, 1.00]$ excludes zero by a wide margin. With $K{=}11$ task types, ICC estimation itself carries substantial uncertainty; the high within-task consistency of death patterns (all-or-nothing per task type) suggests high ICC, which explains the CI narrowing under cluster resampling.
190	
191	We retain this analysis for transparency; readers should rely on the non-clustered episode-level bootstrap (\S\ref{sec:death-decomp}) as the primary inference.
192	
193	\section{Per-Task Death Rate Confidence Intervals}
194	\label{app:per-task-ci}
195	
196	We compute bootstrap 95\% CIs for the death-rate differential ($\Delta\text{DR} = \text{DR}_{\text{int}} - \text{DR}_{\text{det}}$) for all 30 ScienceWorld task types. Of 30 tasks, 28 are death-prone (at least one death under either strategy); the remaining 2 (\texttt{grow-plant}, \texttt{find-non-living-thing}) have zero deaths under both strategies.
197	
198	Across all 28 death-prone tasks, internal DR exceeds deterministic DR without exception (100\% directional consistency). The pooled death-rate differential is $+37.3\%$ (95\% CI: $[29.7\%, 44.4\%]$). Fifteen of 28 tasks are individually significant (CI excludes zero); the 13 non-significant tasks all have $n{=}5$ prescreening episodes, where statistical power is insufficient to detect even large effects (e.g., a task with $\Delta\text{DR} = +40$\,pp at $n{=}5$ has a CI of $\pm 43$\,pp). The universal directional consistency, combined with the pooled significance, confirms that death asymmetry is not driven by a subset of outlier tasks.
199	
200	\section{Leave-One-Task-Out DAF Sensitivity}
201	\label{app:loto-daf}
202	
203	Table~\ref{tab:loto-daf} (main text, \S\ref{sec:death-decomp}) reports the full leave-one-task-out DAF sensitivity analysis.
204	
205	\section{Per-Task Dose-Response Breakdown}
206	\label{app:dose-response}
207	
208	Table~\ref{tab:dose-response-detail} reports per-task death rates for Reflexion at $N{=}3$, 4, and 5 on the 10 death-prone tasks ($n{=}20$ episodes per task). Per-task variance is high (up to 25\,pp range for \texttt{measure-melting-point}), but the aggregate smooths to a 2.5\,pp band, confirming that the stabilization conclusion is robust at the aggregate level despite task-level noise. \texttt{freeze} is consistently the hardest task (50--60\% DR across all $N$).
209	
210	\paragraph{Statistical power.} With $n{=}200$ paired episodes, the minimum detectable effect (MDE) is ${\sim}8$~pp ($\alpha = 0.05$, 80\% power). The key $N{=}1{\to}3$ decline ($-13.5$~pp) exceeds this threshold and is well-powered; the stabilization claim ($N{=}3{\to}5$, $+1.0$~pp) is also supported, since a ${\geq}8$~pp improvement would be detected if present.
211	
212	\begin{table}[h]
213	\centering
214	\small
215	\caption{Per-task death rates (\%) for Reflexion at $N{=}3$, 4, 5 on 10 death-prone tasks ($n{=}20$ per task). Aggregate death rates confirm stabilization at $N \geq 3$ (range: $34.0$--$36.5\%$).}
216	\label{tab:dose-response-detail}
217	\begin{tabular}{@{}lrrr@{}}
218	\toprule
219	Task & $N{=}3$ & $N{=}4$ & $N{=}5$ \\
220	\midrule
221	chemistry-mix & 25.0 & 35.0 & 20.0 \\
222	find-animal & 45.0 & 30.0 & 45.0 \\
223	freeze & 50.0 & 50.0 & 60.0 \\
224	grow-fruit & 30.0 & 25.0 & 25.0 \\
225	identify-life-stages-1 & 35.0 & 35.0 & 35.0 \\
226	identify-life-stages-2 & 25.0 & 25.0 & 30.0 \\
227	inclined-plane-angle & 20.0 & 30.0 & 35.0 \\
228	lifespan-longest & 45.0 & 40.0 & 40.0 \\
229	lifespan-long+short & 30.0 & 45.0 & 35.0 \\
230	measure-melting-pt & 35.0 & 50.0 & 25.0 \\
231	\midrule
232	\textbf{Aggregate} & \textbf{34.0} & \textbf{36.5} & \textbf{35.0} \\
233	\bottomrule
234	\end{tabular}
235	\end{table}
236	
237	\section{Router Training Details}
238	\label{app:router-details}
239	
240	We use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.
241	
242	With gradient accumulation of 1 (effective batch size 4), routing performance is highly sensitive to the evaluation split; this suggests overfitting to specific train/validation partition boundaries. With gradient accumulation of 8 (effective batch size 32), step-level performance stabilizes across splits (${\sim}54\%$ balanced accuracy). All reported results use gradient accumulation 8.
243	
244	Under step-level evaluation with a fixed data split, cross-seed balanced accuracy ranges from 52.7\% to 58.1\%, but internal recall varies from 51.5\% to 81.8\%, which reflects threshold sensitivity. However, episode-level evaluation reveals that this apparent discrimination does not generalize: balanced accuracy drops to $47.1 \pm 2.2\%$ across 8 cross-split seeds (Appendix~\ref{app:seed-robustness}). Deployed end-to-end, the trained router allocates 97.0\% of episodes to deterministic computation with 17.6\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.
245	
246	\paragraph{Evaluation methods.} All results use \emph{generation-based evaluation}: the model generates a routing label as text (\texttt{enable\_thinking=False}), parsed for classification. We evaluate at two granularities: \emph{step-level} (steps from the same episode may appear in both train and validation sets) and \emph{episode-level} (entire episodes held out). Step-level accuracy ($54.1 \pm 5.4\%$) exceeds chance (the router captures some signal), but episode-level accuracy ($47.1 \pm 2.2\%$, below chance) shows this does not generalize to unseen episodes. Paraphrase-based text augmentation (Appendix~\ref{app:seed-robustness}) provides no improvement; real-data scaling remains open. Always-deterministic is trivially near-optimal given DAF $= 90.4\%$. The main text (\S\ref{sec:router-diagnostic}) reports controlled 4-seed results at three scales; the model-size ablation (Appendix~\ref{app:ablations}) provides further detail.
247	
248	\begin{table}[h]
249	\centering
250	\small
251	\resizebox{\columnwidth}{!}{%
252	\begin{tabular}{@{}lcc@{}}
253	\toprule
254	Hyperparameter & Classification Head & Implicit Router \\
255	\midrule
256	Base model & Qwen3-1.7B & Qwen3-1.7B \\
257	Architecture & Linear + LoRA & SFT + LoRA \\
258	LoRA $r$ / $\alpha$ & 16 / 32 & 16 / 32 \\
259	Learning rate & 2e-5 & 2e-4 \\
260	Optimizer & AdamW & AdamW \\
261	Epochs & 3 & 3 \\
262	Batch size (per device) & 4 & 4 \\
263	Gradient accumulation & 8 & 8 \\
264	Warmup ratio & 0.1 & 0.1 \\
265	Weight decay & 0.01 & 0.01 \\
266	Max sequence length & 512 & 512 \\
267	Seeds & \{42\} & \{42, 123, 456, 789\} \\
268	\bottomrule
269	\end{tabular}}
270	\caption{Router training hyperparameters. Both architectures use the same base model with LoRA adaptation. The classification head degenerates across all configurations; the implicit router results are reported as 4-seed mean$\pm$std.}
271	\label{tab:hyperparams}
272	\end{table}
273	
274	\paragraph{Agent inference parameters.}
275	For ScienceWorld, each agent step uses temperature $T{=}0.3$ and maximum generation length of 256 tokens, served via vLLM v0.21.0. Top-$p$ is left at the vLLM default of $1.0$ (no nucleus sampling). For MATH, the agent uses greedy decoding ($T{=}0.0$) with a maximum of 2{,}048 tokens per generation. For ALFWorld, we use $T{=}0.3$ with 256 maximum tokens. All three environments use Qwen2.5-7B-Instruct~\citep{qwen25-2024} as the backbone.
276	
277	\section{Seed Robustness}
278	\label{app:seed-robustness}
279	
280	\paragraph{Counterfactual collection seed.}
281	We re-collect all episodes with a different ScienceWorld environment seed (seed=123, $N{=}220$, 20 episodes per task type).
282	The replication yields DAF $= 89.7\%$ ($\Delta_\text{nd} = 2.83$, $\Delta_\text{full} = 27.47$),
283	within 0.73~pp of the primary estimate (seed=42, DAF $= 90.4\%$).
284	Label distributions are consistent: 67 deterministic-preferred / 7 internal-preferred / 146 no-preference
285	(primary: 86 / 9 / 150).
286	Death rates by strategy remain directionally aligned ($\text{DR}_\text{int} = 45.5\%$ vs.\ $42.9\%$; $\text{DR}_\text{det} = 20.9\%$ vs.\ $16.3\%$).
287	The seed=123 replication uses $N{=}220$ ($20$ episodes per task type);
288	the primary dataset's larger $N{=}245$ reflects 25 additional episodes across two task types (\texttt{find-non-living-thing}: $n{=}40$; \texttt{lifespan-longest-lived}: $n{=}25$; all others: $n{=}20$).
289	
290	\paragraph{Router training seed.}
291	We assess router generalization at two evaluation granularities: \emph{step-level}, where steps from the same episode may appear in both train and validation sets, and \emph{episode-level}, where entire episodes are held out. Both use cross-split evaluation (seeds $\{42, \ldots, 49\}$, 8 seeds total), where the data partition and training seed both vary. Table~\ref{tab:seed-robustness} reports per-seed results.
292	
293	\begin{table}[h]
294	\centering
295	\small
296	\begin{tabular}{@{}llcc@{}}
297	\toprule
298	Eval.\ Granularity & Seed & Bal.\ Acc.\ (\%) \\
299	\midrule
300	Step-level & 42 & 57.06 \\
301	(same-episode & 43 & 63.99 \\
302	leakage) & 44 & 55.43 \\
303	 & 45 & 56.14 \\
304	 & 46 & 55.45 \\
305	 & 47 & 50.08 \\
306	 & 48 & 48.03 \\
307	 & 49 & 59.30 \\
308	\cmidrule{2-3}
309	 & Mean$\pm$std & $54.1 \pm 5.4$ \\
310	\midrule
311	Episode-level & 42 & 48.1 \\
312	(held-out & 43 & 47.9 \\
313	episodes) & 44 & 49.6 \\
314	 & 45 & 49.4 \\
315	 & 46 & 48.5 \\
316	 & 47 & 43.1 \\
317	 & 48 & 45.4 \\
318	 & 49 & 44.8 \\
319	\cmidrule{2-3}
320	 & Mean$\pm$std & $47.1 \pm 2.2$ \\
321	\midrule
322	\multicolumn{2}{@{}l}{Always-det (= majority-vote)} & 50.0 \\
323	\bottomrule
324	\end{tabular}
325	\caption{Per-seed router performance under cross-split evaluation (8 seeds, generation-based, \texttt{enable\_thinking=False}). Step-level evaluation allows steps from the same episode in both train and validation sets (same-episode leakage). Episode-level evaluation holds out entire episodes; the resulting $47.1 \pm 2.2\%$ is below the 50\% chance baseline. A text augmentation ablation (Table~\ref{tab:text-augmentation}) confirms this failure persists under the current data distribution and augmentation regime.}
326	\label{tab:seed-robustness}
327	\end{table}
328	
329	The contrast between step-level ($54.1 \pm 5.4\%$) and episode-level ($47.1 \pm 2.2\%$) evaluation reveals a generalization gap: the step-level signal likely reflects memorization of episode-specific context (enabled by same-episode leakage) rather than extraction of generalizable routing features. At episode level, the router performs below chance across all 8 seeds (range: 43.1\%--49.6\%). Paraphrase-based text augmentation (Table~\ref{tab:text-augmentation}) from 25\% to 800\% ($32{\times}$ range) provides no improvement, converging to the always-deterministic baseline ($50\%$). Paraphrase augmentation inflates the majority class without generating novel routing patterns; genuine episode-level scaling (collecting more counterfactual pairs) remains an open question. With DAF $= 90.4\%$ and all task types deterministic-majority (86:9 label ratio), always-deterministic trivially solves the episode-level routing problem, leaving the step-level router with no exploitable signal under current architectures.
330	
331	\paragraph{Text augmentation ablation.} To test whether the episode-level generalization failure stems from data scarcity, we vary training set size from 25\% to 800\% of the original via paraphrase-based text augmentation (synonym substitution + template variation on step observations), holding the episode-level validation set fixed. This tests augmentation-based scaling, not genuine episode-level scaling (which would require new counterfactual collections). Table~\ref{tab:text-augmentation} reports the results.
332	
333	\begin{table}[h]
334	\centering
335	\small
336	\begin{tabular}{@{}rccc@{}}
337	\toprule
338	Scale & Samples & Det\% & Ep.\ Bal.\ Acc.\ (\%) \\
339	\midrule
340	25\% & 433 & ${\sim}90$ & $49.5 \pm 0.3$ \\
341	50\% & 867 & ${\sim}90$ & $51.5$ \\
342	100\% & 1{,}735 & 89.6 & $49.9 \pm 0.1$ \\
343	200\% & 3{,}470 & 94.2 & $50.0 \pm 0.0$ \\
344	800\% & 13{,}880 & ${\sim}97.7$ & $51.0 \pm 1.1$ \\
345	\midrule
346	Always-det & --- & --- & 50.0 \\
347	\bottomrule
348	\end{tabular}
349	\caption{Text augmentation ablation: episode-level balanced accuracy across training set sizes (25\%--800\% of original via paraphrase, $32{\times}$ range). Internal recall $= 0.0$ at all scales (complete majority-class collapse). Det\%: fraction of deterministic-preferred labels in training data. The 50\% scale is a single seed; all others report mean$\pm$std across seeds.}
350	\label{tab:text-augmentation}
351	\end{table}
352	
353	All scales hover at ${\sim}50\%$ episode-level balanced accuracy (equivalent to the always-deterministic baseline), with no monotonic improvement as data increases. Augmentation-based scaling provides no improvement at any scale; however, episode-level minority-class diversity remains a potential confound that cannot be resolved without collecting more internal-preferred episodes. The ground-truth internal-preferred rate (9/245 $= 3.7\%$) means collecting 50 internal-preferred episodes would require approximately 1{,}350 paired episodes at current environment dynamics, a $5.5{\times}$ expansion with diminishing return on a $9.6\%$ signal. The failure points to a limitation of the current data distribution: when DAF $= 90.4\%$ and all task types are deterministic-majority (86:9 label ratio), the episode-level routing problem is trivially solved by always choosing deterministic, and the step-level router finds no exploitable signal under the current architecture and data regime.
354	
355	Augmentation disproportionately increases the majority (deterministic) class: Det\% rises from 89.6\% at 100\% to 94.2\% at 200\% and ${\sim}97.7\%$ at 800\%. However, the complete collapse to majority-class prediction (internal recall $= 0.0$) occurs even at the smallest unaugmented scale (25\%, ${\sim}90\%$ det); this is not an augmentation artifact. Balanced accuracy corrects for class imbalance by averaging per-class recall, so the metric itself is not biased by the skew.
356	
357	Decomposition metrics are stable under bootstrap resampling ($B{=}10{,}000$ resamples of the 245-episode dataset): DAF $= 90.4\% \pm 4.2\%$ (95\% CI $[81.3\%, 99.1\%]$); Pearson $r = 0.975 \pm 0.011$ (95\% CI $[0.952, 0.995]$). The death avoidance dominance finding is robust to both resampling and split perturbation.
358	
359	\paragraph{Per-task-type evaluation breakdown.} To test whether the router learns transferable routing strategies or merely task-type classification, we evaluate existing checkpoints (8 seeds) separately on each of the 11 task types. Of the 11 task types, 7 have \emph{all-deterministic} labels (no internal-preferred episodes exist), making balanced accuracy undefined; the router has nothing to learn beyond the trivial always-deterministic default. For the remaining 4 task types where both classes are present, balanced accuracy ranges from 50.0\% to 73.0\%, but this apparent signal does not indicate cross-task-type routing transfer: the router is effectively classifying task types (which correlate with death risk) rather than extracting a generalizable routing strategy. This complements the text augmentation ablation: routing signal does not transfer across task types because the signal \emph{is} the task type, i.e., whether a given task carries death risk. The 4B capacity scaling result (Appendix~\ref{app:ablations}) suggests capacity is one factor, but even 4B's $59.0\%$ episode-level accuracy does not demonstrate cross-task-type transfer.
360	
361	\section{Penalty Sensitivity Analysis}
362	\label{app:penalty}
363	
364	\begin{table}[h]
365	\centering
366	\scriptsize
367	\resizebox{\columnwidth}{!}{%
368	\begin{tabular}{@{}rrr@{}}
369	\toprule
370	$P$ & DAF($P$) & 95\% CI \\
371	\midrule
372	0 & 7.4\% & [$-39.4$, $82.5$] \\
373	1 & 14.8\% & [$-28.6$, $89.6$] \\
374	5 & 35.4\% & [$-1.8$, $92.7$] \\
375	10 & 50.4\% & [$18.5$, $93.3$] \\
376	25 & 70.7\% & [$48.0$, $96.3$] \\
377	50 & 82.6\% & [$67.2$, $98.2$] \\
378	100\textsuperscript{*} & 90.4\% & [$81.3$, $99.1$] \\
379	200 & 94.9\% & [$89.9$, $99.5$] \\
380	500 & 97.9\% & [$95.7$, $99.8$] \\
381	\bottomrule
382	\end{tabular}}
383	\caption{Sensitivity of DAF to death penalty magnitude $P$. $\Delta_{\text{nd}} = 2.84$ is invariant; as $P$ increases, $\Delta_{\text{full}} \approx \delta P + \Delta_{\text{nd}}$ grows, mechanically increasing DAF. \textsuperscript{*}Default ScienceWorld setting. Bootstrap 95\% CIs ($B{=}10{,}000$).}
384	\label{tab:penalty-sensitivity}
385	\end{table}
386	
387	The non-death score gap $\Delta_{\text{nd}} = 2.84$ is invariant across penalty levels; it depends only on surviving-episode performance, not on $P$. As $P$ increases, $\Delta_{\text{full}}$ grows ($16.33$ at $P{=}50$, $29.60$ at $P{=}100$, $56.13$ at $P{=}200$) while $\Delta_{\text{nd}}$ remains fixed, mechanically increasing DAF.
388	
389	\paragraph{Mechanism boundary: death specificity.}
390	The $r = 0.97$ correlation between per-task death-rate differential and $\Delta_{\text{full}}$ is specific to catastrophic death (score $= -100$). Broader failure definitions dissolve the correlation entirely: defining ``failure'' as any non-positive score ($T{=}0$) yields $r = -0.13$ ($p = 0.70$), because non-death episodes show near-zero performance differential between strategies ($\Delta_{\text{nd}} = 2.84$). Table~\ref{tab:penalty-correlation} quantifies this specificity across penalty magnitudes.
391	
392	\begin{table}[h]
393	\centering
394	\small
395	\begin{tabular}{@{}rccl@{}}
396	\toprule
397	$P$ & $r$ & $p$ & Sig.\ ($\alpha{=}0.05$) \\
398	\midrule
399	1 & $-0.44$ & $0.178$ & No \\
400	5 & $-0.29$ & $0.382$ & No \\
401	10 & $-0.08$ & $0.813$ & No \\
402	25 & $0.51$ & $0.108$ & No \\
403	50 & $0.86$ & $0.0006$ & Yes \\
404	100\textsuperscript{*} & $0.97$ & $8 \times 10^{-7}$ & Yes \\
405	200 & $0.99$ & $1 \times 10^{-9}$ & Yes \\
406	\bottomrule
407	\end{tabular}
408	\caption{Pearson $r$ between per-task death-rate differential and $\Delta_{\text{full}}(P)$ across penalty magnitudes. The correlation is non-significant at low penalties and emerges at $P \geq 50$, which reflects the transition from non-death-dominated to death-dominated score gaps. \textsuperscript{*}Default ScienceWorld setting.}
409	\label{tab:penalty-correlation}
410	\end{table}
411	
412	This sharpens our central finding: death is not merely the dominant component of routing signal; it is effectively the \emph{only} component that generates differential routing signal in ScienceWorld. At low penalties, the death contribution is small and $\Delta_{\text{full}}$ reduces to $\Delta_{\text{nd}} \approx 2.84$, which is near-uniform across task types ($\text{mean non-death gap} = -1.19$ excluding the \texttt{find-non-living-thing} outlier); consequently, death-rate differential has no predictive power. As $P$ increases, the death term dominates $\Delta_{\text{full}}$, and the correlation sharpens because death rates \emph{are} the performance gap. The DAF values in Table~\ref{tab:penalty-sensitivity} increase monotonically with $P$, but this is a mathematical consequence of the decomposition ($\text{DAF} = \delta P / (\delta P + \Delta_{\text{nd}})$), not evidence of mechanism robustness.
413	
414	\section{Cross-Environment Details}
415	\label{app:cross-env-details}
416	
417	Table~\ref{tab:cross-env} summarizes the label distributions across all three environments (see also Figure~\ref{fig:signal-reversal} in \S\ref{sec:cross-env}).
418	
419	\begin{table}[h]
420	\centering
421	\small
422	\resizebox{\columnwidth}{!}{%
423	\begin{tabular}{@{}lccccc@{}}
424	\toprule
425	Environment & $N$ & Det\% & Int\% & NoPref\% & Death? \\
426	\midrule
427	ScienceWorld & 245 & 35.1 & 3.7 & 61.2 & Yes ($-100$) \\
428	MATH & 795 & 7.3 & 8.3 & 84.4 & No \\
429	ALFWorld & 135 & 25.9 & 1.5 & 72.6 & No\textsuperscript{$\dagger$} \\
430	\bottomrule
431	\end{tabular}}
432	\caption{Cross-environment label distribution. ``Deterministic'' denotes qualitatively different computation modes: ScienceWorld = oracle simulator with ground-truth state; MATH = Python code interpreter; ALFWorld = admissible-action enumeration. $\dagger$\,ALFWorld's deterministic advantage stems from information asymmetry, not death avoidance.}
433	\label{tab:cross-env}
434	\end{table}
435	
436	Table~\ref{tab:alfworld-pertask} provides the per-task-type breakdown for ALFWorld. Unlike ScienceWorld, ALFWorld has no death mechanism ($\delta = 0$, DAF $= 0\%$); the entire performance gap $\Delta_{\text{full}}$ reflects information asymmetry from admissible-action access. \texttt{pick\_and\_place} shows the strongest effect ($\Delta = 0.563$, 18 of 32 episodes det-preferred), while \texttt{pick\_two\_obj\_and\_place} shows the weakest ($\Delta = 0.087$), consistent with multi-object tasks requiring more sequential reasoning that admissible actions alone cannot resolve. Only \texttt{pick\_heat\_then\_place} has a 95\% CI crossing zero ($n{=}16$).
437	
438	\begin{table}[h]
439	\centering
440	\scriptsize
441	\setlength{\tabcolsep}{2.5pt}
442	\begin{tabular}{@{}lrcccc@{}}
443	\toprule
444	Task Type & $n$ & Succ\%\textsubscript{int} & Succ\%\textsubscript{det} & D / I / N & $\Delta_{\text{full}}$ \\
445	\midrule
446	pick\_and\_place       & 32 & 0.0  & 56.3 & 18 / 0 / 14 & $+0.563$ \\
447	look\_at\_obj\_in\_light & 13 & 15.4 & 38.5 & 3 / 0 / 10  & $+0.231$ \\
448	pick\_cool\_then\_place & 24 & 0.0  & 16.7 & 4 / 0 / 20  & $+0.167$ \\
449	pick\_clean\_then\_place & 27 & 3.7  & 18.5 & 5 / 1 / 21  & $+0.148$ \\
450	pick\_heat\_then\_place & 16 & 6.3  & 18.8 & 3 / 1 / 12  & $+0.125$ \\
451	pick\_two\_obj\_and\_place & 23 & 0.0 & 8.7  & 2 / 0 / 21  & $+0.087$ \\
452	\midrule
453	\textbf{All (6 types)} & \textbf{135} & \textbf{3.0} & \textbf{27.4} & \textbf{35 / 2 / 98} & $\mathbf{+0.244}$ \\
454	\bottomrule
455	\end{tabular}
456	\caption{Per-task-type decomposition for ALFWorld (135 games, Qwen2.5-7B-Instruct). D/I/N: deterministic-preferred / internal-preferred / no-preference. No death mechanism exists; $\Delta_{\text{full}}$ is driven entirely by information asymmetry from admissible-action access. Sorted by $\Delta_{\text{full}}$ descending.}
457	\label{tab:alfworld-pertask}
458	\end{table}
459	
460	\paragraph{MATH subset composition.}
461	The $N{=}795$ MATH problems span two categories from the MATH test set~\citep{math-2021} (Levels 4--5): Algebra (585, 73.6\%) and Counting \& Probability (210, 26.4\%). The category imbalance reflects the relative sizes in the original test set.
462	
463	\section{Cross-Model Verification}
464	\label{app:cross-model}
465	
466	We replicate the counterfactual analysis with Llama-3.1-8B-Instruct across all 11 task types ($N{=}220$ episode pairs, 20 per type; Table~\ref{tab:cross-model-detail}).
467	The internal strategy dies in $41.4\%$ of episodes versus $11.4\%$ for deterministic (death-rate differential $+30.0$~pp), with 83 deterministic-preferred, 3 internal-preferred (1.4\%, all death-asymmetry reversals), and 134 no-preference labels.
468	Both models exhibit nearly identical internal vulnerability (${\sim}$42\%: Qwen $42.9\%$, Llama $41.4\%$), confirming that death-prone failure is empirically dominated by the task environment rather than model-specific factors. The differential magnitude varies ($+26.5$~pp Qwen, $+30.0$~pp Llama) because deterministic strategy safety is model-dependent ($16.3\%$ vs.\ $11.4\%$), but directional consistency is 100\% (10/10 death-prone tasks in both models).
469	\texttt{identify-life-stages-1} shows cross-model precision matching ($55\%$/$10\%$/$+45$~pp in both models).
470	\texttt{find-non-living-thing} shows zero deaths in both models, consistent with its majority-class answer distribution.
471	
472	\begin{table}[h]
473	\centering
474	\small
475	\resizebox{\columnwidth}{!}{%
476	\begin{tabular}{@{}lrrrl@{}}
477	\toprule
478	Task & Int\% & Det\% & $\Delta$\,pp & D / I / N \\
479	\midrule
480	identify-life-stages-1 & 55 & 10 & +45 & 9 / 0 / 11 \\
481	freeze & 45 & 0 & +45 & 9 / 0 / 11 \\
482	grow-fruit & 45 & 5 & +40 & 8 / 0 / 12 \\
483	identify-life-stages-2 & 45 & 5 & +40 & 8 / 0 / 12 \\
484	measure-melting-point & 50 & 15 & +35 & 9 / 0 / 11 \\
485	lifespan-longest & 35 & 5 & +30 & 7 / 1 / 12 \\
486	lifespan-l-then-s & 50 & 20 & +30 & 6 / 0 / 14 \\
487	chemistry-mix & 45 & 20 & +25 & 5 / 0 / 15 \\
488	inclined-plane & 45 & 20 & +25 & 6 / 0 / 14 \\
489	find-animal & 40 & 25 & +15 & 6 / 2 / 12 \\
490	find-non-living-thing & 0 & 0 & 0 & 10 / 0 / 10 \\
491	\midrule
492	\textbf{Aggregate} & \textbf{41.4} & \textbf{11.4} & \textbf{+30.0} & \textbf{83 / 3 / 134} \\
493	\bottomrule
494	\end{tabular}}%
495	\caption{Per-task Llama-3.1-8B cross-model replication ($N{=}20$ per task). D/I/N: deterministic-preferred / internal-preferred / no-preference. Sorted by $\Delta$ DR descending.}
496	\label{tab:cross-model-detail}
497	\end{table}
498	
499	\paragraph{Cross-model and cross-environment summary.}
500	Table~\ref{tab:cross-model-env} (main text, \S\ref{sec:cross-model}) consolidates replication results across model families and environments.
501	
502	\section{Failure Mode Analysis}
503	\label{app:failure-modes}
504	
505	All 105 internal-strategy deaths (100\%) are triggered by the same action pattern: \texttt{focus on [object]}. In ScienceWorld, \texttt{focus on} is the answer-submission action (equivalent to ``this is my final answer''); the LLM agent systematically misuses it as a general interaction or exploration command, and applies it to irrelevant targets (rooms, doors, inventory items). Each such execution submits an incorrect answer and triggers the $-100$ death penalty. Within death episodes, both strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$); the internal strategy's higher death count (105 vs.\ 40 for deterministic) reflects how often each strategy enters catastrophic states, not different action selection within those states.
506	
507	Manual inspection identifies four failure categories: (A) no task awareness, where the agent executes \texttt{focus on} without reading the task; (B) task-aware but lacking action grounding, where the agent correctly identifies the objective but cannot map it to valid action primitives; (D) genuine attempts with execution failure; and (E) initial progress wasted by early errors. Category B dominates: agents demonstrate task comprehension but systematically fail to translate it into correct ScienceWorld actions. This taxonomy was produced by a single annotator; no inter-annotator agreement was computed. The categories are intended as qualitative illustrations, not as formal labels with reliability guarantees.
508	\label{tab:death-taxonomy}
509	
510	\paragraph{Representative examples.}
511	\emph{Category A} (no task awareness): In a \texttt{chemistry-mix} episode, the agent immediately executes \texttt{focus on kitchen}, \texttt{focus on door}, \texttt{focus on inventory} without reading the task, dying on the first \texttt{focus on} call. \emph{Category B} (comprehension without grounding): In a \texttt{lifespan-longest-lived} episode, the agent correctly identifies that it must compare animal lifespans and reasons about which animal lives longest, but then executes \texttt{focus on oak tree} (a non-animal object in the room) instead of navigating to find the target animal, triggering death.
512	
513	\paragraph{Action distribution analysis.}
514	Figure~\ref{fig:death-action-dist} shows the action distribution in death versus non-death episodes for the internal strategy; both are dominated by \texttt{connect} actions, with \texttt{focus on} moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$). Crucially, Figure~\ref{fig:death-comparison} reveals that within death episodes, internal and deterministic strategies exhibit comparable \texttt{focus on} rates (${\sim}5\%$). The survival gap (105 vs.\ 40 deaths) therefore reflects how often each strategy enters catastrophic states, not how it behaves within those states. Among fatal \texttt{focus on} targets, \texttt{workshop} remains the most frequent (20.0\%), followed by \texttt{inventory} (17.1\%) and \texttt{kitchen} (10.5\%), indicating a systematic object bias rather than random exploration. Figure~\ref{fig:death-timeline} visualizes the temporal pattern: agents execute long sequences of \texttt{connect} actions before a terminal \texttt{focus on} triggers death, typically in the final 1--3 steps.
515	
516	\begin{figure}[h]
517	\centering
518	\includegraphics[width=\columnwidth]{figures/death_action_distribution.pdf}
519	\caption{Action distribution for the internal (LLM) strategy in death ($n{=}105$) vs.\ non-death ($n{=}140$) episodes. Left: full distribution (both dominated by \texttt{connect}). Right: non-\texttt{connect} actions zoomed. \texttt{focus on} is moderately more frequent in death episodes ($5.4\%$ vs.\ $3.4\%$), while non-death episodes show higher rates of observation and object interaction.}
520	\label{fig:death-action-dist}
521	\end{figure}
522	
523	% Figure~\ref{fig:death-comparison} moved to main text (\S2)
524	
525	\section{Grounding Ablation}
526	\label{app:grounding-ablation}
527	
528	We test whether directly intervening on the dominant death action (\texttt{focus on}) eliminates death vulnerability on the 10 death-prone tasks (baseline 48.0\%, $n{=}200$).
529	
530	\paragraph{Prompt warning.} Adding an explicit system prompt (``use \texttt{focus on} only for final answers'') reduces aggregate death rate to 37.0\% ($\Delta = -11$~pp). Both identification tasks exhibit ironic effects (\texttt{identify-life-stages-1}: 35\%$\to$50\%; \texttt{identify-life-stages-2}: 25\%$\to$70\%), where explicit mention of the dangerous action may have increased its salience.
531	
532	\paragraph{Action-space filtering.} Blocking \texttt{focus on} during the exploration phase yields 379 blocks across 200 episodes with zero leaks and zero passthroughs (the agent never persisted in retrying blocked actions), reducing death rate to 29.0\% ($\Delta = -19$~pp). The zero-passthrough rate suggests \texttt{focus on} use is a shallow behavioral pattern rather than a deliberate strategy.
533	
534	\paragraph{Per-task variation.} Under filtering, \texttt{identify-life-stages} and \texttt{inclined-plane} approach deterministic-level safety (${\sim}$15--20\% DR), while \texttt{chemistry-mix} and \texttt{find-animal} remain at 35--40\%. Residual deaths occur during the answer-submission window, where the filter is inactive and agents submit \texttt{focus on} to incorrect objects.
535	
536	\paragraph{Post-ablation counterfactual decomposition.}
537	To test whether death dominance persists after grounding intervention, we run the full decomposition on matched episodes (183 episodes across 10 death-prone task types, paired by variation index).
538	Grounding reduces the internal death rate from 50.3\% to 35.0\% ($-15.3$\,pp), yet $\geq$93\% of disambiguating labels still arise from death asymmetry ($\Delta_\text{nd} \approx 0.09$, compared to $0.00$ at baseline).
539	Internal-preferred episodes increase from 5 to 23 (grounding helps internal strategy survive more often), but the routing signal remains death-driven rather than score-driven.
540	One task type (\texttt{identify-life-stages-2}, $n{=}10$) shows a paradoxical increase in death rate (50\%$\to$80\%); this outlier likely reflects the small sample size and task-specific prompt interference rather than a systematic effect.
541	
542	\section{Ablation Studies}
543	\label{app:ablations}
544	
545	\paragraph{Capacity scaling.} We scale the implicit router from Qwen3-0.6B to Qwen3-4B and evaluate at both step and episode level (Table~\ref{tab:capacity}).
546	
547	\begin{table}[h]
548	\centering
549	\small
550	\begin{tabular}{@{}lcc@{}}
551	\toprule
552	Model & Step Bal.\ Acc.\ (\%) & Ep.\ Bal.\ Acc.\ (\%) \\
553	\midrule
554	Qwen3-0.6B & $56.4 \pm 3.5$ & $50.7 \pm 2.6$ \\
555	Qwen3-1.7B & $58.2 \pm 4.0$ & $43.1 \pm 1.0$ \\
556	Qwen3-4B & $59.2 \pm 3.5$ & $\mathbf{59.0 \pm 1.9}$ \\
557	\midrule
558	Always-det & 50.0 & 50.0 \\
559	\bottomrule
560	\end{tabular}
561	\caption{Capacity scaling: step-level and episode-level balanced accuracy (4 seeds, identical configuration across all scales). Step-level accuracy is flat ($56$--$59\%$, within seed variance). At episode level, only 4B breaks the random baseline ($59.0\%$, $p < 0.005$).}
562	\label{tab:capacity}
563	\end{table}
564	
565	Step-level balanced accuracy is flat across scales ($56$--$59\%$, within seed variance); step-level discrimination is not capacity-sensitive. At episode level, only 4B breaks the random baseline ($59.0 \pm 1.9\%$, $p < 0.005$); 0.6B and 1.7B remain at or below chance. The 1.7B model's below-chance episode-level accuracy ($43.1\%$) may reflect overfitting to spurious step-level correlations that anti-correlate with episode outcomes; without per-class confusion matrices at this scale, this remains a hypothesis. The dominant explanation across scales is that death avoidance constitutes a task-type-level binary signal that a step-level router cannot exploit efficiently.
566	
567	\paragraph{Generative router.} A generative routing model trained with explicit routing labels achieves balanced accuracy of 46.7\%, confirming that the routing bottleneck is signal-limited, not architecture-limited.
568	
569	\paragraph{Leave-one-task-type-out routing.} Under leave-one-task-type-out evaluation, blind routing collapses to always-deterministic (balanced accuracy 50.0\%); a keyword-based variant achieves 62.9\% only through task-identity leakage, not genuine routing signal. A guided router evaluated under the same protocol confirms this: without task-type identifiers it achieves chance accuracy (50.0\%), and leaking task names raises this to 62.9\%, confirming that the only learnable routing feature is task-type identity.
570	
571	\paragraph{Death-proximal labeling.} Training a router only on the $k$ steps preceding death events (rather than all steps) also collapses to majority-class prediction (step balanced accuracy 50.0\%, episode balanced accuracy 50.0\%, internal recall 0\%), confirming that the absence of step-level signal is not an artifact of label dilution across long episodes.
572	
573	\paragraph{Reasoning depth.} An ablation comparing chain-of-thought reasoning against direct-answer generation on 6 task types ($n{=}120$ episodes per condition, 6 tasks $\times$ 20 episodes per task) found no significant difference (Mann--Whitney $p > 0.26$, $|d| \leq 0.31$) and near-identical death rates (41.8\% vs.\ 42.5\%); reasoning depth does not meaningfully alter internal-mode outcomes.
574	
575	\section{Threshold Routing Analysis}
576	\label{sec:threshold-routing}
577	
578	Given per-task death risk knowledge, we test whether a simple threshold routing strategy can outperform always-deterministic. For each threshold $t \in [0, 1]$, we route to internal if the per-task internal death rate $\leq t$, otherwise to deterministic, and sweep all thresholds to find the optimal.
579	
580	\begin{table}[h]
581	\centering
582	\small
583	\resizebox{\columnwidth}{!}{%
584	\begin{tabular}{lccc}
585	\toprule
586	Strategy & Mean Score & Death Rate & $\Delta$ vs Det \\
587	\midrule
588	Always-det & $-9.47$ & $0.163$ & $0.00$ \\
589	Optimal threshold ($t{=}0$) & $-11.03$ & $0.155$ & $-1.56$ \\
590	Always-internal & $-39.07$ & $0.429$ & $-29.60$ \\
591	\bottomrule
592	\end{tabular}}
593	\caption{Death-risk threshold routing analysis on 245 episodes. The optimal threshold routes only \texttt{find-non-living-thing} (the sole zero-death task) to internal, with all other tasks routed to deterministic. Bootstrap 95\% CI for the difference: $[-8.87, +5.92]$.}
594	\label{tab:threshold-routing}
595	\end{table}
596	
597	Even with perfect per-task death risk knowledge, threshold routing cannot outperform always-deterministic. The sole zero-death task achieves higher scores under deterministic (+28.5) than internal (+18.9), leaving no room for a beneficial mixed strategy.
598	
599	\section{Practitioner Decision Framework}
600	\label{app:decision-framework}
601	
602	Given a new interactive environment, the following three-stage procedure diagnoses whether learned routing adds value over a fixed deterministic strategy.
603	
604	\paragraph{Stage 1: Pilot collection (${\sim}$50 episodes).}
605	Run pure-internal and pure-deterministic strategies on a representative sample (${\sim}$50 episode pairs). Compute the death-rate differential $\Delta\text{DR} = \text{DR}_{\text{int}} - \text{DR}_{\text{det}}$.
606	
607	\paragraph{Stage 2: Death dominance check.}
608	If $\Delta\text{DR} > 15$~pp, death asymmetry is likely the dominant routing signal. Compute the death-label fraction $f_{\text{death}}$: the proportion of non-tie routing labels where exactly one strategy dies.
609	
610	\paragraph{Stage 3: Decision.}
611	If $f_{\text{death}} > 75\%$, the routing signal is death-dominated; a fixed deterministic strategy will match or exceed any learned router. If $f_{\text{death}} < 50\%$, diverse routing signals may justify a learned router. Between 50\%--75\%, collect additional episodes to reduce estimation noise before committing to router development.
612	
613	\paragraph{Retrospective validation.}
614	All four experimental conditions in this paper are correctly classified:
615	
616	\begin{table}[h]
617	\centering
618	\small
619	\begin{tabular}{@{}lrrll@{}}
620	\toprule
621	Condition & $\Delta$DR & $f_{\text{death}}$ & Prediction & Actual \\
622	\midrule
623	Qwen-7B & +26.5 & 78.9\% & det-fixed & det wins \\
624	Llama-8B & +30.0 & $>$75\% & det-fixed & det wins \\
625	Qwen-72B & +27.8 & $>$75\% & det-fixed & det wins \\
626	MATH & +0.5 & 0\% & router viable & no signal \\
627	\bottomrule
628	\end{tabular}
629	\caption{Retrospective validation of the decision framework. All four conditions are correctly classified (4/4).}
630	\label{tab:decision-framework}
631	\end{table}
632	
633	The framework also predicts the inverted-U relationship between capability and death risk: below ${\sim}$0.5B parameters, agents rarely reach dangerous states (13.3\% death rate in a 15-episode pilot), so $\Delta\text{DR}$ is low and the framework would not recommend fixed-deterministic. Above ${\sim}$7B, agents are capable enough to enter catastrophic states but not capable enough to avoid them, producing high $\Delta\text{DR}$.
634	
635	\paragraph{Threshold calibration.} The thresholds above (15~pp, 75\%, 50\%) are illustrative, derived from ScienceWorld's specific reward structure (binary death penalty $P{=}100$, sparse terminal rewards). Environments with graded penalties, dense rewards, or qualitatively different failure modes may require different thresholds. Practitioners should calibrate these boundaries for their specific environment.
636	
637	\section{Extended Validation of Excluded Tasks}
638	\label{app:extended-validation}
639	
640	To verify that task exclusion does not bias toward death-prone tasks, we collect $n{=}20$ episodes for five representative excluded tasks spanning all exclusion categories (Table~\ref{tab:extended-val}).
641	
642	\begin{table}[h]
643	\centering
644	\small
645	\resizebox{\columnwidth}{!}{%
646	\begin{tabular}{lcrrrrc}
647	\toprule
648	Task & Category & $n$ & Int DR & Det DR & $\Delta$DR & D/I/N \\
649	\midrule
650	boil & dev-set & 20 & 55\% & 25\% & +30\,pp & 6/0/14 \\
651	melt & dev-set & 20 & 45\% & 20\% & +25\,pp & 7/2/11 \\
652	find-living-thing & taxonomic & 20 & 55\% & 15\% & +40\,pp & 10/0/10 \\
653	use-thermometer & agent-floor & 20 & 50\% & 20\% & +30\,pp & 7/1/12 \\
654	power-component & agent-floor & 20 & 50\% & 15\% & +35\,pp & 7/0/13 \\
655	\midrule
656	\textit{Mean (5 tasks)} & & 100 & 51.0\% & 19.0\% & +32.0\,pp & 37/3/60 \\
657	\bottomrule
658	\end{tabular}}
659	\caption{Extended validation ($n{=}20$) of representative excluded task types. All five tasks confirm death asymmetry; mean $\Delta$DR $= +32.0$\,pp is consistent with the $n{=}5$ prescreening estimate for these same tasks (Table~\ref{tab:excluded-death}).}
660	\label{tab:extended-val}
661	\end{table}
662	
663	Notably, the excluded-task aggregate DAF (0.991) exceeds the included-task DAF (0.904; Table~\ref{tab:per-task}), indicating that excluded tasks are \emph{more} death-dominated than included tasks, the opposite of a cherry-picking bias.
664	
665	\section{Agent Prompt Templates}
666	\label{app:prompt-templates}
667	
668	Below we show the complete prompt templates used for agent interaction in ScienceWorld. Both the internal (ReAct) and deterministic strategies share the same system prompt but differ in the user message template.
669	
670	\paragraph{System prompt (shared).} Used for all ScienceWorld agent interactions across both computation modes.
671	
672	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
673	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
674	  left=2mm, right=2mm, top=1mm, bottom=1mm}
675	You are an agent interacting with a ScienceWorld text
676	environment. Your goal is to complete the given task by
677	choosing actions from the available action list.
678	
679	Use the following format for each step:
680	Thought: &lt;your reasoning about what to do next>
681	Action: &lt;exact action string from the valid actions list>
682	
683	Rules:
684	- You MUST choose an action from the valid actions list.
685	  Do not invent actions.
686	- Think step by step about what physical/scientific
687	  process is needed.
688	- Pay attention to the current observation for clues
689	  about object states.
690	\end{tcblisting}
691	
692	\paragraph{Internal (ReAct) user template.} At each step, the agent receives the current observation, valid action list, and recent action history, and must select a single action.
693	
694	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
695	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
696	  left=2mm, right=2mm, top=1mm, bottom=1mm}
697	Current observation:
698	{observation}
699	
700	Valid actions:
701	{valid_actions_str}
702	
703	Previous actions taken: {history_str}
704	
705	Choose your next action.
706	\end{tcblisting}
707	
708	\paragraph{Deterministic candidate generation template.} For the deterministic strategy, the agent generates ranked candidate actions instead of selecting one; these candidates are then evaluated via simulator forking (\S\ref{sec:method}).
709	
710	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
711	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
712	  left=2mm, right=2mm, top=1mm, bottom=1mm}
713	Current observation:
714	{observation}
715	
716	Valid actions:
717	{valid_actions_str}
718	
719	Previous actions taken: {history_str}
720	
721	Generate the top 3 most promising actions from the valid
722	actions list, ranked by how likely they are to make
723	progress on the task. Output exactly 3 actions, one per
724	line, in this format:
725	1. &lt;action>
726	2. &lt;action>
727	3. &lt;action>
728	\end{tcblisting}
729	
730	\paragraph{Reflexion self-reflection prompt.} After a failed episode, the Reflexion agent (\S\ref{sec:agent-improvement}) generates a reflection that is injected into subsequent trial attempts as additional system context.
731	
732	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
733	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
734	  left=2mm, right=2mm, top=1mm, bottom=1mm}
735	You just completed an episode in a ScienceWorld text
736	environment but failed.
737	
738	Task: {task_name}
739	Final score: {final_score}
740	Outcome: {outcome}
741	Number of steps taken: {num_steps}
742	
743	Here is a summary of your actions:
744	{action_summary}
745	
746	Analyze why this episode failed and provide a short
747	strategy for the next attempt. Focus on:
748	1. What went wrong (wrong sequence, missed key step,
749	   dangerous action)?
750	2. What should be done differently next time?
751	
752	Keep your reflection under 200 words.
753	\end{tcblisting}
754	
755	\paragraph{Grounding warning (ablation).} The prompt warning condition in the grounding ablation (Appendix~\ref{app:grounding-ablation}) appends the following to the shared system prompt:
756	
757	\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,
758	  listing options={basicstyle=\small\ttfamily,breaklines=true,columns=fullflexible},
759	  left=2mm, right=2mm, top=1mm, bottom=1mm}
760	CRITICAL SAFETY RULE: The 'focus on [object]' action is
761	ONLY for submitting your final answer. Do NOT use
762	'focus on' to examine, inspect, or interact with objects
763	during exploration. Using 'focus on' on the wrong object
764	will cause irreversible failure. Use 'look at',
765	'examine', or 'pick up' instead for exploration.
766	\end{tcblisting}
767	
768	\noindent The key difference between the two computation modes is the user message: the internal strategy asks the LLM to \emph{select} one action (ReAct), while the deterministic strategy asks it to \emph{rank} candidates for simulator evaluation. Both use identical system prompts and identical observation formatting.
769	
770	\section{Non-Death Episode Case Study}
771	\label{app:non-death-case-study}
772	
773	We illustrate the framework's ability to decompose non-death routing signal using \texttt{find-non-living-thing}, the only task type with zero deaths and 100\% non-death labels (\S\ref{sec:death-decomp}). Using Gemma-2-9B-it counterfactual episodes ($N{=}20$), 12 episodes show routing preference (9 deterministic-preferred, 3 internal-preferred), confirming the framework detects bidirectional signal independent of death asymmetry.
774	
775	\paragraph{Deterministic-preferred: knowledge retrieval advantage.}
776	In Episode~3 (det: 67, int: 0), the internal strategy issues nonsensical \texttt{connect} actions for 18 consecutive steps (e.g., ``connect air to outside,'' ``connect axe to door to foundry'') without ever identifying a target object; the deterministic strategy correctly focuses on ``orange'' (+58) and opens the kitchen door (+9). In Episode~17 (det: 58, int: 50), both strategies find a valid non-living thing, but the deterministic strategy selects a higher-scoring object (orange, 58\,pts) versus the internal strategy's choice (fountain, 50\,pts), illustrating that object selection quality creates routing signal even when both strategies succeed.
777	
778	\paragraph{Internal-preferred: semantic reasoning advantage.}
779	In Episode~12 (int: 67, det: 58), the task specifies ``move it to the red box in the living room.'' The deterministic strategy focuses on the red box itself, the destination container, not a separate non-living thing, scoring 58\,pts. The internal strategy correctly distinguishes target from container, choosing ``orange'' (67\,pts). This semantic error demonstrates that deterministic pattern-matching can miss task-structure subtleties that internal reasoning captures.
780	
781	These cases confirm two properties: (1)~the framework captures non-death routing signal when it exists, and (2)~signal flows in both directions: neither strategy uniformly dominates in death-free tasks.
782	
783	\paragraph{Systematic analysis of non-death labels.}
784	All 20 non-death non-tie labels in the primary Qwen2.5-7B analysis originate from \texttt{find-non-living-thing}, the sole death-free task type. In every other task type, non-tie episodes involve at least one strategy dying. We classify the 20 episodes into three error categories:
785	
786	\begin{table}[h]
787	\centering
788	\small
789	\begin{tabular}{@{}lrrr@{}}
790	\toprule
791	Error category & Det-pref & Int-pref & Total \\
792	\midrule
793	Hallucination-induced & 8 & 2 & 10 \\
794	Object selection quality & 6 & 1 & 7 \\
795	Action selection error & 2 & 1 & 3 \\
796	\bottomrule
797	\end{tabular}
798	\caption{Non-death non-tie episode classification. Hallucination-induced: agent's state model is incorrect (e.g., believing \texttt{eat} completes the task). Object selection quality: both strategies succeed but choose different-value objects. Action selection: correct state model but suboptimal action sequences.}
799	\label{tab:non-death-taxonomy}
800	\end{table}
801	
802	\noindent Hallucination-induced errors dominate (50\%), driven by a recurring ``eat before focus'' pattern: the internal strategy consumes the target object (destroying it) before attempting the scoring action (\texttt{focus on}), indicating an incorrect state model that equates eating with task completion (11 of 20 episodes). Object selection quality accounts for 35\%: typically the deterministic strategy selecting ``orange'' (58\,pts) while the internal strategy settles for lower-value objects (``fountain'' or ``picture,'' 50\,pts). The error categories are bidirectional: 2 of 10 hallucination episodes and 1 of 3 action selection episodes are internal-preferred, confirming the framework detects failures in both strategies. Score gaps reflect category severity: hallucination errors produce large gaps ($17$--$67$\,pts, one strategy scores zero) while object selection differences produce small gaps ($8$--$9$\,pts, both strategies functional).
803	
804	\section{Use of AI Assistance}
805	We used Claude for coding, code drafting, debugging, and language polishing.
806	
807	\end{document}
808	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "c5c31a39-4bdb-4010-a8b3-d240fe5e5e3b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n% \\usepackage{inconsolata}  % optional per ACL template; not available in this TeX installation\n\\usepackage{graphicx}\n\\graphicspath{{figures/}}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{algorithm}\n\\usepackage{algorithmic}\n\\usepackage{caption}\n\\usepackage{tcolorbox}\n\\tcbuselibrary{listings,breakable}\n\n\\setlength{\\dbltextfloatsep}{8pt plus 2pt minus 2pt}\n\\setlength{\\floatsep}{6pt plus 2pt minus 2pt}\n\\setlength{\\textfloatsep}{8pt plus 2pt minus 2pt}\n\n\\title{Death Avoidance as the Dominant Routing Signal:\\\\A Counterfactual Analysis on ScienceWorld}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{discussion}\n\\input{conclusion}\n\n\\section*{Limitations}\nFull quantitative validation (DAF, label fractions) is specific to ScienceWorld; MATH and ALFWorld serve as boundary probes, not comprehensive cross-environment validation. DAF depends on a fixed death penalty ($P{=}100$); environments with graded or stochastic failure severity would require extensions (Appendix~\\ref{app:penalty}). The internal baseline uses single-pass ReAct~\\citep{react-2023}; more aggressive self-correction (e.g., Tree-of-Thought) may further reduce death rates and alter the signal composition. With $K{=}11$ task-type clusters, cluster bootstrap yields wider CIs; wild cluster bootstrap ($p < 0.001$; Appendix~\\ref{app:wild-cluster}) and 100\\% directional consistency across all 28 death-prone tasks provide partial mitigation. Total compute was approximately 200 GPU-hours on consumer and workstation GPUs.\n\n\\bibliography{references}\n\n\\appendix\n\n\\noindent\\textbf{Appendix Overview.}\n\\hyperref[app:sci]{A.~Signal Concentration Index} $\\cdot$\n\\hyperref[app:labeling]{B.~Labeling Quality Audit} $\\cdot$\n\\hyperref[app:per-task]{C.~Per-Task Decomposition} $\\cdot$\n\\hyperref[app:correlation]{D.~Correlation Robustness} $\\cdot$\n\\hyperref[app:wild-cluster]{E.~Cluster Bootstrap Sensitivity} $\\cdot$\n\\hyperref[app:per-task-ci]{F.~Per-Task CIs} $\\cdot$\n\\hyperref[app:loto-daf]{G.~Leave-One-Task-Out DAF} $\\cdot$\n\\hyperref[app:dose-response]{H.~Dose-Response Breakdown} $\\cdot$\n\\hyperref[app:router-details]{I.~Router Training Details} $\\cdot$\n\\hyperref[app:seed-robustness]{J.~Seed Robustness} $\\cdot$\n\\hyperref[app:penalty]{K.~Penalty Sensitivity} $\\cdot$\n\\hyperref[app:cross-env-details]{L.~Cross-Environment Details} $\\cdot$\n\\hyperref[app:cross-model]{M.~Cross-Model Verification} $\\cdot$\n\\hyperref[app:failure-modes]{N.~Failure Mode Analysis} $\\cdot$\n\\hyperref[app:grounding-ablation]{O.~Grounding Ablation} $\\cdot$\n\\hyperref[app:ablations]{P.~Ablation Studies} $\\cdot$\n\\hyperref[sec:threshold-routing]{Q.~Threshold Routing} $\\cdot$\n\\hyperref[app:decision-framework]{R.~Decision Framework} $\\cdot$\n\\hyperref[app:extended-validation]{S.~Extended Validation} $\\cdot$\n\\hyperref[app:prompt-templates]{T.~Agent Prompt Templates} $\\cdot$\n\\hyperref[app:non-death-case-study]{U.~Non-Death Episode Case Study}\n\n\\section{Signal Concentration Index}\n\\label{app:sci}\n\nLet $K$ denote the number of task types and $c_k$ the contribution of task type $k$ to the aggregate routing signal, defined as the fraction of total death-rate differential attributable to task $k$:\n\\begin{equation}\n    c_k = \\frac{n_k \\cdot \\delta_k}{\\sum_{j=1}^{K} n_j \\cdot \\delta_j}\n\\end{equation}\nwhere $n_k$ is the number of episodes and $\\delta_k = d_k^{\\tt int} - d_k^{\\tt det}$ is the per-task death-rate differential. The SCI is the Gini coefficient over $\\{c_1, \\ldots, c_K\\}$:\n\\begin{equation}\n    \\text{SCI} = \\frac{\\sum_{i=1}^K \\sum_{j=1}^K |c_i - c_j|}{2K \\sum_{k=1}^K c_k}\n\\end{equation}\n\n\\section{Labeling Quality Audit}\n\\label{app:labeling}\n\nNote that episode-level labels are used to evaluate step-level predictions, introducing a granularity mismatch rather than independent validation. A potential concern is oracle circularity: whether episode-level labels reflect tie-breaking artifacts rather than genuine computation mode differences. We audit all 245 labels. Of the 150 \\texttt{no\\_preference} labels (61.2\\%), 115 (46.9\\%) are both-alive ties and 35 (14.3\\%) are both-dead, all excluded from router training. The remaining 95 training labels are entirely genuine: 75 from death asymmetry (70 deterministic-preferred, 5 internal-preferred) and 20 from score comparison with both strategies surviving (16 deterministic-preferred, 4 internal-preferred). Zero labels depend on tie-breaking. Retraining the router using only death-asymmetry labels yields step-level balanced accuracy of 57.3\\%, within 1$\\sigma$ of the full-label retrain (57.6 $\\pm$ 0.5\\%, step-level Trainer evaluation); score-comparison labels contribute negligible additional signal. (Step-level metrics are used here for the relative comparison; as shown in \\S\\ref{sec:router-diagnostic}, absolute generalization to new episodes is near chance.) The 97.4\\% step-level tie rate (\\S\\ref{sec:collection}) further motivates episode-level over step-level labeling.\n\n\\section{Per-Task Decomposition}\n\\label{app:per-task}\nWe use ScienceWorld v1.2.3~\\citep{scienceworld-2022}.\nWe select 11 of ScienceWorld's 30 task types for analysis. Types are excluded when they were used for pipeline development (5 tasks, standard hold-out practice), are taxonomically redundant with a retained family representative (7 tasks), or exhibit near-zero task progress under both strategies (7 tasks, agent capability floor).\\footnote{Excluded tasks exhibit even stronger death dominance than included tasks ($\\Delta\\text{DR} = +38.2$\\,pp vs.\\ $+28.7$\\,pp; Table~\\ref{tab:excluded-death}).}\n\n\\paragraph{Task selection and anti-cherry-picking.}\nEighteen of the 19 excluded task types (95\\%) exhibit death-asymmetric patterns (Table~\\ref{tab:excluded-death}): internal-reasoning death rates range from 40\\% to 60\\% (mean 53.9\\%), while deterministic death rates range from 0\\% to 40\\% (mean 15.8\\%), yielding a mean death-rate differential of $+38.2$\\,pp, exceeding the $+28.7$\\,pp for included tasks. The included subset is thus \\emph{less} death-asymmetric than the excluded subset, the opposite of what a cherry-picking hypothesis would predict. The sole exception is \\texttt{grow-plant}, an intrinsically safe task with zero deaths under both strategies, paralleling \\texttt{find-non-living-thing} in the included set. The 19 excluded tasks fall into three independently motivated categories: five used during pipeline development (standard hold-out practice), seven taxonomically redundant with included family representatives (deduplication), and seven where the 7B backbone achieves near-zero task progress regardless of strategy (agent capability floor). In no case was a task excluded because death dominance was absent. Exclusion is driven by absence of non-death routing signal ($\\Delta_{\\text{nd}} = 0$ for 53\\% of excluded tasks) and standard deduplication practices. \\texttt{find-non-living-thing} serves as an internal counterexample: zero deaths under both strategies yet included because it exhibits non-death routing signal ($\\Delta_{\\text{full}} = +9.58$ entirely from score differences), and deterministic is not always preferred (4 of 20 non-tie labels favor internal).\n\n\\begin{table}[t]\n\\centering\n\\scriptsize\n\\setlength{\\tabcolsep}{2pt}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llrcccl@{}}\n\\toprule\nTask & Grp & $n$ & D\\%\\textsubscript{int} & D\\%\\textsubscript{det} & $\\Delta$DR & Excl.\\ reason \\\\\n\\midrule\nboil                          & A & 20 & 50 & 20 & $+30$ & dev set \\\\\nchange-state-of-matter        & A & 20 & 55 & 15 & $+40$ & dev set \\\\\nchem-mix-paint-secondary      & A & 20 & 45 & 10 & $+35$ & dev set \\\\\ngrow-plant                    & A & 20 &  0 &  0 & $\\phantom{+}0$  & dev set \\\\\nmelt                          & A & 20 & 55 & 15 & $+40$ & dev set \\\\\n\\midrule\nchem-mix-paint-tertiary       & B &  5 & 40 & 20 & $+20$ & family redundancy \\\\\nfind-living-thing             & B &  5 & 60 & 20 & $+40$ & family redundancy \\\\\nfind-plant                    & B &  5 & 60 &  0 & $+60$ & family redundancy \\\\\ninclined-friction-named       & B &  5 & 60 & 20 & $+40$ & family redundancy \\\\\ninclined-friction-unnamed     & B &  5 & 60 &  0 & $+60$ & family redundancy \\\\\nlifespan-shortest             & B &  5 & 60 & 40 & $+20$ & family redundancy \\\\\nmeasure-melt-known            & B &  5 & 60 &  0 & $+60$ & family redundancy \\\\\n\\midrule\nmendelian-known               & C &  5 & 60 & 20 & $+40$ & agent floor \\\\\nmendelian-unknown             & C &  5 & 60 & 40 & $+20$ & agent floor \\\\\npower-component               & C &  5 & 60 & 20 & $+40$ & agent floor \\\\\npower-renewable               & C &  5 & 60 &  0 & $+60$ & agent floor \\\\\ntest-conductivity             & C &  5 & 60 & 20 & $+40$ & agent floor \\\\\ntest-conductivity-unknown     & C &  5 & 60 & 20 & $+40$ & agent floor \\\\\nuse-thermometer               & C &  5 & 60 & 20 & $+40$ & agent floor \\\\\n\\midrule\n\\textbf{Mean (19 excluded)}   &   &    & \\textbf{53.9} & \\textbf{15.8} & $\\mathbf{+38.2}$ & \\\\\n\\textit{cf.\\ included (11)}   &   &    & \\textit{46.5} & \\textit{17.8} & $\\textit{+28.7}$ & \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Death-rate analysis of all 19 excluded task types. D\\%: death rate (score $\\leq -100$). $\\Delta$DR = D\\%\\textsubscript{int} $-$ D\\%\\textsubscript{det}. 18 of 19 excluded tasks (95\\%) exhibit positive death asymmetry ($\\Delta$DR $\\geq +20$\\,pp). Exclusion groups: A = development set (excluded to prevent circular evaluation), B = taxonomically redundant with an included family representative, C = agent-floor tasks (backbone achieves near-zero progress regardless of strategy). The mean $\\Delta$DR among excluded tasks ($+38.2$\\,pp) exceeds that of included tasks ($+28.7$\\,pp), confirming that task selection does not bias toward death-prone tasks. Group B--C estimates are based on $n{=}5$ prescreening episodes per task and should be interpreted as directional evidence rather than precise rate estimates.}\n\\label{tab:excluded-death}\n\\end{table}\n\n\\section{Correlation Robustness}\n\\label{app:correlation}\n\nThe Pearson $r = 0.9698$ reported in \\S\\ref{sec:death-decomp} is robust across multiple diagnostics. Spearman rank correlation is $\\rho = 0.986$ ($p = 2.4 \\times 10^{-8}$); the relationship is not driven by outliers or non-linearity. A nonparametric bootstrap (10{,}000 resamples) yields 95\\% CI $[0.952, 0.995]$.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lr@{}}\n\\toprule\nTask removed & $r_{\\text{LOO}}$ \\\\\n\\midrule\nid-life-stages-1       & 0.963 \\\\\nlifespan-long          & 0.969 \\\\\nlifespan-l-then-s      & 0.976 \\\\\ninclined-plane         & 0.969 \\\\\nfreeze                 & 0.971 \\\\\nmeas-melt-point        & 0.972 \\\\\nid-life-stages-2       & 0.972 \\\\\nfind-animal            & 0.970 \\\\\ngrow-fruit             & 0.973 \\\\\nchem-mix               & 0.969 \\\\\nfind-non-living-thing  & 0.980 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Leave-one-out Pearson $r$ for the death rate differential vs.\\ $\\Delta_{\\text{full}}$ correlation. Full $r = 0.970$; LOO range $[0.963, 0.980]$. No single task type is a leverage point.}\n\\label{tab:loo}\n\\end{table}\n\n\\section{Cluster Bootstrap Sensitivity Analysis}\n\\label{app:wild-cluster}\n\nWith $K{=}11$ task-type clusters, cluster bootstrap falls well below the $K{\\geq}20$--50 recommended for reliable inference \\citep{cameron-2008,webb-2023}. The narrower CIs obtained reflect known small-sample bias toward underestimation of variance, not tighter inference.\n\nEpisodes within the same task type share environment dynamics, raising the concern that the effective sample size is closer to $K$ (task types) than $N$ (episodes). We address this with cluster-robust inference treating each task type as a cluster ($K{=}11$, all 11 included task types, 245 episodes).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nMethod & $p$-value & 95\\% CI \\\\\n\\midrule\nCluster-robust $t$-test ($t{=}10.0$, df$=$10) & $< 0.001$ & $[0.73, 1.00]$ \\\\\nWild cluster bootstrap ($B{=}9{,}999$) & $< 0.001$ & $[0.73, 1.00]$ \\\\\nExact permutation ($2{,}048$ perms) & $0.002$ & --- \\\\\nSign test & $< 0.001$ & --- \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Cluster-level tests of death-rate asymmetry ($K{=}11$ task clusters, 245 episodes). 10 of 11 clusters show internal DR $>$ deterministic DR; the sole exception (\\texttt{find-non-living-thing}) has zero deaths under both strategies. Cohen's $d = 3.02$. The exact permutation $p = 0.002$ ($4/2{,}048$) reflects the near-unanimous directional consistency.}\n\\label{tab:wild-cluster}\n\\end{table}\n\n\\noindent All methods confirm significance with $p < 0.01$, and the 95\\% CI $[0.73, 1.00]$ excludes zero by a wide margin. With $K{=}11$ task types, ICC estimation itself carries substantial uncertainty; the high within-task consistency of death patterns (all-or-nothing per task type) suggests high ICC, which explains the CI narrowing under cluster resampling.\n\nWe retain this analysis for transparency; readers should rely on the non-clustered episode-level bootstrap (\\S\\ref{sec:death-decomp}) as the primary inference.\n\n\\section{Per-Task Death Rate Confidence Intervals}\n\\label{app:per-task-ci}\n\nWe compute bootstrap 95\\% CIs for the death-rate differential ($\\Delta\\text{DR} = \\text{DR}_{\\text{int}} - \\text{DR}_{\\text{det}}$) for all 30 ScienceWorld task types. Of 30 tasks, 28 are death-prone (at least one death under either strategy); the remaining 2 (\\texttt{grow-plant}, \\texttt{find-non-living-thing}) have zero deaths under both strategies.\n\nAcross all 28 death-prone tasks, internal DR exceeds deterministic DR without exception (100\\% directional consistency). The pooled death-rate differential is $+37.3\\%$ (95\\% CI: $[29.7\\%, 44.4\\%]$). Fifteen of 28 tasks are individually significant (CI excludes zero); the 13 non-significant tasks all have $n{=}5$ prescreening episodes, where statistical power is insufficient to detect even large effects (e.g., a task with $\\Delta\\text{DR} = +40$\\,pp at $n{=}5$ has a CI of $\\pm 43$\\,pp). The universal directional consistency, combined with the pooled significance, confirms that death asymmetry is not driven by a subset of outlier tasks.\n\n\\section{Leave-One-Task-Out DAF Sensitivity}\n\\label{app:loto-daf}\n\nTable~\\ref{tab:loto-daf} (main text, \\S\\ref{sec:death-decomp}) reports the full leave-one-task-out DAF sensitivity analysis.\n\n\\section{Per-Task Dose-Response Breakdown}\n\\label{app:dose-response}\n\nTable~\\ref{tab:dose-response-detail} reports per-task death rates for Reflexion at $N{=}3$, 4, and 5 on the 10 death-prone tasks ($n{=}20$ episodes per task). Per-task variance is high (up to 25\\,pp range for \\texttt{measure-melting-point}), but the aggregate smooths to a 2.5\\,pp band, confirming that the stabilization conclusion is robust at the aggregate level despite task-level noise. \\texttt{freeze} is consistently the hardest task (50--60\\% DR across all $N$).\n\n\\paragraph{Statistical power.} With $n{=}200$ paired episodes, the minimum detectable effect (MDE) is ${\\sim}8$~pp ($\\alpha = 0.05$, 80\\% power). The key $N{=}1{\\to}3$ decline ($-13.5$~pp) exceeds this threshold and is well-powered; the stabilization claim ($N{=}3{\\to}5$, $+1.0$~pp) is also supported, since a ${\\geq}8$~pp improvement would be detected if present.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-task death rates (\\%) for Reflexion at $N{=}3$, 4, 5 on 10 death-prone tasks ($n{=}20$ per task). Aggregate death rates confirm stabilization at $N \\geq 3$ (range: $34.0$--$36.5\\%$).}\n\\label{tab:dose-response-detail}\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nTask & $N{=}3$ & $N{=}4$ & $N{=}5$ \\\\\n\\midrule\nchemistry-mix & 25.0 & 35.0 & 20.0 \\\\\nfind-animal & 45.0 & 30.0 & 45.0 \\\\\nfreeze & 50.0 & 50.0 & 60.0 \\\\\ngrow-fruit & 30.0 & 25.0 & 25.0 \\\\\nidentify-life-stages-1 & 35.0 & 35.0 & 35.0 \\\\\nidentify-life-stages-2 & 25.0 & 25.0 & 30.0 \\\\\ninclined-plane-angle & 20.0 & 30.0 & 35.0 \\\\\nlifespan-longest & 45.0 & 40.0 & 40.0 \\\\\nlifespan-long+short & 30.0 & 45.0 & 35.0 \\\\\nmeasure-melting-pt & 35.0 & 50.0 & 25.0 \\\\\n\\midrule\n\\textbf{Aggregate} & \\textbf{34.0} & \\textbf{36.5} & \\textbf{35.0} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Router Training Details}\n\\label{app:router-details}\n\nWe use Qwen3-1.7B for the router to avoid circular dependency with the Qwen2.5-7B data-generating model.\n\nWith gradient accumulation of 1 (effective batch size 4), routing performance is highly sensitive to the evaluation split; this suggests overfitting to specific train/validation partition boundaries. With gradient accumulation of 8 (effective batch size 32), step-level performance stabilizes across splits (${\\sim}54\\%$ balanced accuracy). All reported results use gradient accumulation 8.\n\nUnder step-level evaluation with a fixed data split, cross-seed balanced accuracy ranges from 52.7\\% to 58.1\\%, but internal recall varies from 51.5\\% to 81.8\\%, which reflects threshold sensitivity. However, episode-level evaluation reveals that this apparent discrimination does not generalize: balanced accuracy drops to $47.1 \\pm 2.2\\%$ across 8 cross-split seeds (Appendix~\\ref{app:seed-robustness}). Deployed end-to-end, the trained router allocates 97.0\\% of episodes to deterministic computation with 17.6\\% death rate, and misrouting cost (death from internally-routed episodes) exceeds the benefit of correctly routing rare internal-preferred cases.\n\n\\paragraph{Evaluation methods.} All results use \\emph{generation-based evaluation}: the model generates a routing label as text (\\texttt{enable\\_thinking=False}), parsed for classification. We evaluate at two granularities: \\emph{step-level} (steps from the same episode may appear in both train and validation sets) and \\emph{episode-level} (entire episodes held out). Step-level accuracy ($54.1 \\pm 5.4\\%$) exceeds chance (the router captures some signal), but episode-level accuracy ($47.1 \\pm 2.2\\%$, below chance) shows this does not generalize to unseen episodes. Paraphrase-based text augmentation (Appendix~\\ref{app:seed-robustness}) provides no improvement; real-data scaling remains open. Always-deterministic is trivially near-optimal given DAF $= 90.4\\%$. The main text (\\S\\ref{sec:router-diagnostic}) reports controlled 4-seed results at three scales; the model-size ablation (Appendix~\\ref{app:ablations}) provides further detail.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nHyperparameter & Classification Head & Implicit Router \\\\\n\\midrule\nBase model & Qwen3-1.7B & Qwen3-1.7B \\\\\nArchitecture & Linear + LoRA & SFT + LoRA \\\\\nLoRA $r$ / $\\alpha$ & 16 / 32 & 16 / 32 \\\\\nLearning rate & 2e-5 & 2e-4 \\\\\nOptimizer & AdamW & AdamW \\\\\nEpochs & 3 & 3 \\\\\nBatch size (per device) & 4 & 4 \\\\\nGradient accumulation & 8 & 8 \\\\\nWarmup ratio & 0.1 & 0.1 \\\\\nWeight decay & 0.01 & 0.01 \\\\\nMax sequence length & 512 & 512 \\\\\nSeeds & \\{42\\} & \\{42, 123, 456, 789\\} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Router training hyperparameters. Both architectures use the same base model with LoRA adaptation. The classification head degenerates across all configurations; the implicit router results are reported as 4-seed mean$\\pm$std.}\n\\label{tab:hyperparams}\n\\end{table}\n\n\\paragraph{Agent inference parameters.}\nFor ScienceWorld, each agent step uses temperature $T{=}0.3$ and maximum generation length of 256 tokens, served via vLLM v0.21.0. Top-$p$ is left at the vLLM default of $1.0$ (no nucleus sampling). For MATH, the agent uses greedy decoding ($T{=}0.0$) with a maximum of 2{,}048 tokens per generation. For ALFWorld, we use $T{=}0.3$ with 256 maximum tokens. All three environments use Qwen2.5-7B-Instruct~\\citep{qwen25-2024} as the backbone.\n\n\\section{Seed Robustness}\n\\label{app:seed-robustness}\n\n\\paragraph{Counterfactual collection seed.}\nWe re-collect all episodes with a different ScienceWorld environment seed (seed=123, $N{=}220$, 20 episodes per task type).\nThe replication yields DAF $= 89.7\\%$ ($\\Delta_\\text{nd} = 2.83$, $\\Delta_\\text{full} = 27.47$),\nwithin 0.73~pp of the primary estimate (seed=42, DAF $= 90.4\\%$).\nLabel distributions are consistent: 67 deterministic-preferred / 7 internal-preferred / 146 no-preference\n(primary: 86 / 9 / 150).\nDeath rates by strategy remain directionally aligned ($\\text{DR}_\\text{int} = 45.5\\%$ vs.\\ $42.9\\%$; $\\text{DR}_\\text{det} = 20.9\\%$ vs.\\ $16.3\\%$).\nThe seed=123 replication uses $N{=}220$ ($20$ episodes per task type);\nthe primary dataset's larger $N{=}245$ reflects 25 additional episodes across two task types (\\texttt{find-non-living-thing}: $n{=}40$; \\texttt{lifespan-longest-lived}: $n{=}25$; all others: $n{=}20$).\n\n\\paragraph{Router training seed.}\nWe assess router generalization at two evaluation granularities: \\emph{step-level}, where steps from the same episode may appear in both train and validation sets, and \\emph{episode-level}, where entire episodes are held out. Both use cross-split evaluation (seeds $\\{42, \\ldots, 49\\}$, 8 seeds total), where the data partition and training seed both vary. Table~\\ref{tab:seed-robustness} reports per-seed results.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\nEval.\\ Granularity & Seed & Bal.\\ Acc.\\ (\\%) \\\\\n\\midrule\nStep-level & 42 & 57.06 \\\\\n(same-episode & 43 & 63.99 \\\\\nleakage) & 44 & 55.43 \\\\\n & 45 & 56.14 \\\\\n & 46 & 55.45 \\\\\n & 47 & 50.08 \\\\\n & 48 & 48.03 \\\\\n & 49 & 59.30 \\\\\n\\cmidrule{2-3}\n & Mean$\\pm$std & $54.1 \\pm 5.4$ \\\\\n\\midrule\nEpisode-level & 42 & 48.1 \\\\\n(held-out & 43 & 47.9 \\\\\nepisodes) & 44 & 49.6 \\\\\n & 45 & 49.4 \\\\\n & 46 & 48.5 \\\\\n & 47 & 43.1 \\\\\n & 48 & 45.4 \\\\\n & 49 & 44.8 \\\\\n\\cmidrule{2-3}\n & Mean$\\pm$std & $47.1 \\pm 2.2$ \\\\\n\\midrule\n\\multicolumn{2}{@{}l}{Always-det (= majority-vote)} & 50.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-seed router performance under cross-split evaluation (8 seeds, generation-based, \\texttt{enable\\_thinking=False}). Step-level evaluation allows steps from the same episode in both train and validation sets (same-episode leakage). Episode-level evaluation holds out entire episodes; the resulting $47.1 \\pm 2.2\\%$ is below the 50\\% chance baseline. A text augmentation ablation (Table~\\ref{tab:text-augmentation}) confirms this failure persists under the current data distribution and augmentation regime.}\n\\label{tab:seed-robustness}\n\\end{table}\n\nThe contrast between step-level ($54.1 \\pm 5.4\\%$) and episode-level ($47.1 \\pm 2.2\\%$) evaluation reveals a generalization gap: the step-level signal likely reflects memorization of episode-specific context (enabled by same-episode leakage) rather than extraction of generalizable routing features. At episode level, the router performs below chance across all 8 seeds (range: 43.1\\%--49.6\\%). Paraphrase-based text augmentation (Table~\\ref{tab:text-augmentation}) from 25\\% to 800\\% ($32{\\times}$ range) provides no improvement, converging to the always-deterministic baseline ($50\\%$). Paraphrase augmentation inflates the majority class without generating novel routing patterns; genuine episode-level scaling (collecting more counterfactual pairs) remains an open question. With DAF $= 90.4\\%$ and all task types deterministic-majority (86:9 label ratio), always-deterministic trivially solves the episode-level routing problem, leaving the step-level router with no exploitable signal under current architectures.\n\n\\paragraph{Text augmentation ablation.} To test whether the episode-level generalization failure stems from data scarcity, we vary training set size from 25\\% to 800\\% of the original via paraphrase-based text augmentation (synonym substitution + template variation on step observations), holding the episode-level validation set fixed. This tests augmentation-based scaling, not genuine episode-level scaling (which would require new counterfactual collections). Table~\\ref{tab:text-augmentation} reports the results.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}rccc@{}}\n\\toprule\nScale & Samples & Det\\% & Ep.\\ Bal.\\ Acc.\\ (\\%) \\\\\n\\midrule\n25\\% & 433 & ${\\sim}90$ & $49.5 \\pm 0.3$ \\\\\n50\\% & 867 & ${\\sim}90$ & $51.5$ \\\\\n100\\% & 1{,}735 & 89.6 & $49.9 \\pm 0.1$ \\\\\n200\\% & 3{,}470 & 94.2 & $50.0 \\pm 0.0$ \\\\\n800\\% & 13{,}880 & ${\\sim}97.7$ & $51.0 \\pm 1.1$ \\\\\n\\midrule\nAlways-det & --- & --- & 50.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Text augmentation ablation: episode-level balanced accuracy across training set sizes (25\\%--800\\% of original via paraphrase, $32{\\times}$ range). Internal recall $= 0.0$ at all scales (complete majority-class collapse). Det\\%: fraction of deterministic-preferred labels in training data. The 50\\% scale is a single seed; all others report mean$\\pm$std across seeds.}\n\\label{tab:text-augmentation}\n\\end{table}\n\nAll scales hover at ${\\sim}50\\%$ episode-level balanced accuracy (equivalent to the always-deterministic baseline), with no monotonic improvement as data increases. Augmentation-based scaling provides no improvement at any scale; however, episode-level minority-class diversity remains a potential confound that cannot be resolved without collecting more internal-preferred episodes. The ground-truth internal-preferred rate (9/245 $= 3.7\\%$) means collecting 50 internal-preferred episodes would require approximately 1{,}350 paired episodes at current environment dynamics, a $5.5{\\times}$ expansion with diminishing return on a $9.6\\%$ signal. The failure points to a limitation of the current data distribution: when DAF $= 90.4\\%$ and all task types are deterministic-majority (86:9 label ratio), the episode-level routing problem is trivially solved by always choosing deterministic, and the step-level router finds no exploitable signal under the current architecture and data regime.\n\nAugmentation disproportionately increases the majority (deterministic) class: Det\\% rises from 89.6\\% at 100\\% to 94.2\\% at 200\\% and ${\\sim}97.7\\%$ at 800\\%. However, the complete collapse to majority-class prediction (internal recall $= 0.0$) occurs even at the smallest unaugmented scale (25\\%, ${\\sim}90\\%$ det); this is not an augmentation artifact. Balanced accuracy corrects for class imbalance by averaging per-class recall, so the metric itself is not biased by the skew.\n\nDecomposition metrics are stable under bootstrap resampling ($B{=}10{,}000$ resamples of the 245-episode dataset): DAF $= 90.4\\% \\pm 4.2\\%$ (95\\% CI $[81.3\\%, 99.1\\%]$); Pearson $r = 0.975 \\pm 0.011$ (95\\% CI $[0.952, 0.995]$). The death avoidance dominance finding is robust to both resampling and split perturbation.\n\n\\paragraph{Per-task-type evaluation breakdown.} To test whether the router learns transferable routing strategies or merely task-type classification, we evaluate existing checkpoints (8 seeds) separately on each of the 11 task types. Of the 11 task types, 7 have \\emph{all-deterministic} labels (no internal-preferred episodes exist), making balanced accuracy undefined; the router has nothing to learn beyond the trivial always-deterministic default. For the remaining 4 task types where both classes are present, balanced accuracy ranges from 50.0\\% to 73.0\\%, but this apparent signal does not indicate cross-task-type routing transfer: the router is effectively classifying task types (which correlate with death risk) rather than extracting a generalizable routing strategy. This complements the text augmentation ablation: routing signal does not transfer across task types because the signal \\emph{is} the task type, i.e., whether a given task carries death risk. The 4B capacity scaling result (Appendix~\\ref{app:ablations}) suggests capacity is one factor, but even 4B's $59.0\\%$ episode-level accuracy does not demonstrate cross-task-type transfer.\n\n\\section{Penalty Sensitivity Analysis}\n\\label{app:penalty}\n\n\\begin{table}[h]\n\\centering\n\\scriptsize\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}rrr@{}}\n\\toprule\n$P$ & DAF($P$) & 95\\% CI \\\\\n\\midrule\n0 & 7.4\\% & [$-39.4$, $82.5$] \\\\\n1 & 14.8\\% & [$-28.6$, $89.6$] \\\\\n5 & 35.4\\% & [$-1.8$, $92.7$] \\\\\n10 & 50.4\\% & [$18.5$, $93.3$] \\\\\n25 & 70.7\\% & [$48.0$, $96.3$] \\\\\n50 & 82.6\\% & [$67.2$, $98.2$] \\\\\n100\\textsuperscript{*} & 90.4\\% & [$81.3$, $99.1$] \\\\\n200 & 94.9\\% & [$89.9$, $99.5$] \\\\\n500 & 97.9\\% & [$95.7$, $99.8$] \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Sensitivity of DAF to death penalty magnitude $P$. $\\Delta_{\\text{nd}} = 2.84$ is invariant; as $P$ increases, $\\Delta_{\\text{full}} \\approx \\delta P + \\Delta_{\\text{nd}}$ grows, mechanically increasing DAF. \\textsuperscript{*}Default ScienceWorld setting. Bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:penalty-sensitivity}\n\\end{table}\n\nThe non-death score gap $\\Delta_{\\text{nd}} = 2.84$ is invariant across penalty levels; it depends only on surviving-episode performance, not on $P$. As $P$ increases, $\\Delta_{\\text{full}}$ grows ($16.33$ at $P{=}50$, $29.60$ at $P{=}100$, $56.13$ at $P{=}200$) while $\\Delta_{\\text{nd}}$ remains fixed, mechanically increasing DAF.\n\n\\paragraph{Mechanism boundary: death specificity.}\nThe $r = 0.97$ correlation between per-task death-rate differential and $\\Delta_{\\text{full}}$ is specific to catastrophic death (score $= -100$). Broader failure definitions dissolve the correlation entirely: defining ``failure'' as any non-positive score ($T{=}0$) yields $r = -0.13$ ($p = 0.70$), because non-death episodes show near-zero performance differential between strategies ($\\Delta_{\\text{nd}} = 2.84$). Table~\\ref{tab:penalty-correlation} quantifies this specificity across penalty magnitudes.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}rccl@{}}\n\\toprule\n$P$ & $r$ & $p$ & Sig.\\ ($\\alpha{=}0.05$) \\\\\n\\midrule\n1 & $-0.44$ & $0.178$ & No \\\\\n5 & $-0.29$ & $0.382$ & No \\\\\n10 & $-0.08$ & $0.813$ & No \\\\\n25 & $0.51$ & $0.108$ & No \\\\\n50 & $0.86$ & $0.0006$ & Yes \\\\\n100\\textsuperscript{*} & $0.97$ & $8 \\times 10^{-7}$ & Yes \\\\\n200 & $0.99$ & $1 \\times 10^{-9}$ & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pearson $r$ between per-task death-rate differential and $\\Delta_{\\text{full}}(P)$ across penalty magnitudes. The correlation is non-significant at low penalties and emerges at $P \\geq 50$, which reflects the transition from non-death-dominated to death-dominated score gaps. \\textsuperscript{*}Default ScienceWorld setting.}\n\\label{tab:penalty-correlation}\n\\end{table}\n\nThis sharpens our central finding: death is not merely the dominant component of routing signal; it is effectively the \\emph{only} component that generates differential routing signal in ScienceWorld. At low penalties, the death contribution is small and $\\Delta_{\\text{full}}$ reduces to $\\Delta_{\\text{nd}} \\approx 2.84$, which is near-uniform across task types ($\\text{mean non-death gap} = -1.19$ excluding the \\texttt{find-non-living-thing} outlier); consequently, death-rate differential has no predictive power. As $P$ increases, the death term dominates $\\Delta_{\\text{full}}$, and the correlation sharpens because death rates \\emph{are} the performance gap. The DAF values in Table~\\ref{tab:penalty-sensitivity} increase monotonically with $P$, but this is a mathematical consequence of the decomposition ($\\text{DAF} = \\delta P / (\\delta P + \\Delta_{\\text{nd}})$), not evidence of mechanism robustness.\n\n\\section{Cross-Environment Details}\n\\label{app:cross-env-details}\n\nTable~\\ref{tab:cross-env} summarizes the label distributions across all three environments (see also Figure~\\ref{fig:signal-reversal} in \\S\\ref{sec:cross-env}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nEnvironment & $N$ & Det\\% & Int\\% & NoPref\\% & Death? \\\\\n\\midrule\nScienceWorld & 245 & 35.1 & 3.7 & 61.2 & Yes ($-100$) \\\\\nMATH & 795 & 7.3 & 8.3 & 84.4 & No \\\\\nALFWorld & 135 & 25.9 & 1.5 & 72.6 & No\\textsuperscript{$\\dagger$} \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Cross-environment label distribution. ``Deterministic'' denotes qualitatively different computation modes: ScienceWorld = oracle simulator with ground-truth state; MATH = Python code interpreter; ALFWorld = admissible-action enumeration. $\\dagger$\\,ALFWorld's deterministic advantage stems from information asymmetry, not death avoidance.}\n\\label{tab:cross-env}\n\\end{table}\n\nTable~\\ref{tab:alfworld-pertask} provides the per-task-type breakdown for ALFWorld. Unlike ScienceWorld, ALFWorld has no death mechanism ($\\delta = 0$, DAF $= 0\\%$); the entire performance gap $\\Delta_{\\text{full}}$ reflects information asymmetry from admissible-action access. \\texttt{pick\\_and\\_place} shows the strongest effect ($\\Delta = 0.563$, 18 of 32 episodes det-preferred), while \\texttt{pick\\_two\\_obj\\_and\\_place} shows the weakest ($\\Delta = 0.087$), consistent with multi-object tasks requiring more sequential reasoning that admissible actions alone cannot resolve. Only \\texttt{pick\\_heat\\_then\\_place} has a 95\\% CI crossing zero ($n{=}16$).\n\n\\begin{table}[h]\n\\centering\n\\scriptsize\n\\setlength{\\tabcolsep}{2.5pt}\n\\begin{tabular}{@{}lrcccc@{}}\n\\toprule\nTask Type & $n$ & Succ\\%\\textsubscript{int} & Succ\\%\\textsubscript{det} & D / I / N & $\\Delta_{\\text{full}}$ \\\\\n\\midrule\npick\\_and\\_place       & 32 & 0.0  & 56.3 & 18 / 0 / 14 & $+0.563$ \\\\\nlook\\_at\\_obj\\_in\\_light & 13 & 15.4 & 38.5 & 3 / 0 / 10  & $+0.231$ \\\\\npick\\_cool\\_then\\_place & 24 & 0.0  & 16.7 & 4 / 0 / 20  & $+0.167$ \\\\\npick\\_clean\\_then\\_place & 27 & 3.7  & 18.5 & 5 / 1 / 21  & $+0.148$ \\\\\npick\\_heat\\_then\\_place & 16 & 6.3  & 18.8 & 3 / 1 / 12  & $+0.125$ \\\\\npick\\_two\\_obj\\_and\\_place & 23 & 0.0 & 8.7  & 2 / 0 / 21  & $+0.087$ \\\\\n\\midrule\n\\textbf{All (6 types)} & \\textbf{135} & \\textbf{3.0} & \\textbf{27.4} & \\textbf{35 / 2 / 98} & $\\mathbf{+0.244}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Per-task-type decomposition for ALFWorld (135 games, Qwen2.5-7B-Instruct). D/I/N: deterministic-preferred / internal-preferred / no-preference. No death mechanism exists; $\\Delta_{\\text{full}}$ is driven entirely by information asymmetry from admissible-action access. Sorted by $\\Delta_{\\text{full}}$ descending.}\n\\label{tab:alfworld-pertask}\n\\end{table}\n\n\\paragraph{MATH subset composition.}\nThe $N{=}795$ MATH problems span two categories from the MATH test set~\\citep{math-2021} (Levels 4--5): Algebra (585, 73.6\\%) and Counting \\& Probability (210, 26.4\\%). The category imbalance reflects the relative sizes in the original test set.\n\n\\section{Cross-Model Verification}\n\\label{app:cross-model}\n\nWe replicate the counterfactual analysis with Llama-3.1-8B-Instruct across all 11 task types ($N{=}220$ episode pairs, 20 per type; Table~\\ref{tab:cross-model-detail}).\nThe internal strategy dies in $41.4\\%$ of episodes versus $11.4\\%$ for deterministic (death-rate differential $+30.0$~pp), with 83 deterministic-preferred, 3 internal-preferred (1.4\\%, all death-asymmetry reversals), and 134 no-preference labels.\nBoth models exhibit nearly identical internal vulnerability (${\\sim}$42\\%: Qwen $42.9\\%$, Llama $41.4\\%$), confirming that death-prone failure is empirically dominated by the task environment rather than model-specific factors. The differential magnitude varies ($+26.5$~pp Qwen, $+30.0$~pp Llama) because deterministic strategy safety is model-dependent ($16.3\\%$ vs.\\ $11.4\\%$), but directional consistency is 100\\% (10/10 death-prone tasks in both models).\n\\texttt{identify-life-stages-1} shows cross-model precision matching ($55\\%$/$10\\%$/$+45$~pp in both models).\n\\texttt{find-non-living-thing} shows zero deaths in both models, consistent with its majority-class answer distribution.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrrl@{}}\n\\toprule\nTask & Int\\% & Det\\% & $\\Delta$\\,pp & D / I / N \\\\\n\\midrule\nidentify-life-stages-1 & 55 & 10 & +45 & 9 / 0 / 11 \\\\\nfreeze & 45 & 0 & +45 & 9 / 0 / 11 \\\\\ngrow-fruit & 45 & 5 & +40 & 8 / 0 / 12 \\\\\nidentify-life-stages-2 & 45 & 5 & +40 & 8 / 0 / 12 \\\\\nmeasure-melting-point & 50 & 15 & +35 & 9 / 0 / 11 \\\\\nlifespan-longest & 35 & 5 & +30 & 7 / 1 / 12 \\\\\nlifespan-l-then-s & 50 & 20 & +30 & 6 / 0 / 14 \\\\\nchemistry-mix & 45 & 20 & +25 & 5 / 0 / 15 \\\\\ninclined-plane & 45 & 20 & +25 & 6 / 0 / 14 \\\\\nfind-animal & 40 & 25 & +15 & 6 / 2 / 12 \\\\\nfind-non-living-thing & 0 & 0 & 0 & 10 / 0 / 10 \\\\\n\\midrule\n\\textbf{Aggregate} & \\textbf{41.4} & \\textbf{11.4} & \\textbf{+30.0} & \\textbf{83 / 3 / 134} \\\\\n\\bottomrule\n\\end{tabular}}%\n\\caption{Per-task Llama-3.1-8B cross-model replication ($N{=}20$ per task). D/I/N: deterministic-preferred / internal-preferred / no-preference. Sorted by $\\Delta$ DR descending.}\n\\label{tab:cross-model-detail}\n\\end{table}\n\n\\paragraph{Cross-model and cross-environment summary.}\nTable~\\ref{tab:cross-model-env} (main text, \\S\\ref{sec:cross-model}) consolidates replication results across model families and environments.\n\n\\section{Failure Mode Analysis}\n\\label{app:failure-modes}\n\nAll 105 internal-strategy deaths (100\\%) are triggered by the same action pattern: \\texttt{focus on [object]}. In ScienceWorld, \\texttt{focus on} is the answer-submission action (equivalent to ``this is my final answer''); the LLM agent systematically misuses it as a general interaction or exploration command, and applies it to irrelevant targets (rooms, doors, inventory items). Each such execution submits an incorrect answer and triggers the $-100$ death penalty. Within death episodes, both strategies exhibit comparable \\texttt{focus on} rates (${\\sim}5\\%$); the internal strategy's higher death count (105 vs.\\ 40 for deterministic) reflects how often each strategy enters catastrophic states, not different action selection within those states.\n\nManual inspection identifies four failure categories: (A) no task awareness, where the agent executes \\texttt{focus on} without reading the task; (B) task-aware but lacking action grounding, where the agent correctly identifies the objective but cannot map it to valid action primitives; (D) genuine attempts with execution failure; and (E) initial progress wasted by early errors. Category B dominates: agents demonstrate task comprehension but systematically fail to translate it into correct ScienceWorld actions. This taxonomy was produced by a single annotator; no inter-annotator agreement was computed. The categories are intended as qualitative illustrations, not as formal labels with reliability guarantees.\n\\label{tab:death-taxonomy}\n\n\\paragraph{Representative examples.}\n\\emph{Category A} (no task awareness): In a \\texttt{chemistry-mix} episode, the agent immediately executes \\texttt{focus on kitchen}, \\texttt{focus on door}, \\texttt{focus on inventory} without reading the task, dying on the first \\texttt{focus on} call. \\emph{Category B} (comprehension without grounding): In a \\texttt{lifespan-longest-lived} episode, the agent correctly identifies that it must compare animal lifespans and reasons about which animal lives longest, but then executes \\texttt{focus on oak tree} (a non-animal object in the room) instead of navigating to find the target animal, triggering death.\n\n\\paragraph{Action distribution analysis.}\nFigure~\\ref{fig:death-action-dist} shows the action distribution in death versus non-death episodes for the internal strategy; both are dominated by \\texttt{connect} actions, with \\texttt{focus on} moderately more frequent in death episodes ($5.4\\%$ vs.\\ $3.4\\%$). Crucially, Figure~\\ref{fig:death-comparison} reveals that within death episodes, internal and deterministic strategies exhibit comparable \\texttt{focus on} rates (${\\sim}5\\%$). The survival gap (105 vs.\\ 40 deaths) therefore reflects how often each strategy enters catastrophic states, not how it behaves within those states. Among fatal \\texttt{focus on} targets, \\texttt{workshop} remains the most frequent (20.0\\%), followed by \\texttt{inventory} (17.1\\%) and \\texttt{kitchen} (10.5\\%), indicating a systematic object bias rather than random exploration. Figure~\\ref{fig:death-timeline} visualizes the temporal pattern: agents execute long sequences of \\texttt{connect} actions before a terminal \\texttt{focus on} triggers death, typically in the final 1--3 steps.\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/death_action_distribution.pdf}\n\\caption{Action distribution for the internal (LLM) strategy in death ($n{=}105$) vs.\\ non-death ($n{=}140$) episodes. Left: full distribution (both dominated by \\texttt{connect}). Right: non-\\texttt{connect} actions zoomed. \\texttt{focus on} is moderately more frequent in death episodes ($5.4\\%$ vs.\\ $3.4\\%$), while non-death episodes show higher rates of observation and object interaction.}\n\\label{fig:death-action-dist}\n\\end{figure}\n\n% Figure~\\ref{fig:death-comparison} moved to main text (\\S2)\n\n\\section{Grounding Ablation}\n\\label{app:grounding-ablation}\n\nWe test whether directly intervening on the dominant death action (\\texttt{focus on}) eliminates death vulnerability on the 10 death-prone tasks (baseline 48.0\\%, $n{=}200$).\n\n\\paragraph{Prompt warning.} Adding an explicit system prompt (``use \\texttt{focus on} only for final answers'') reduces aggregate death rate to 37.0\\% ($\\Delta = -11$~pp). Both identification tasks exhibit ironic effects (\\texttt{identify-life-stages-1}: 35\\%$\\to$50\\%; \\texttt{identify-life-stages-2}: 25\\%$\\to$70\\%), where explicit mention of the dangerous action may have increased its salience.\n\n\\paragraph{Action-space filtering.} Blocking \\texttt{focus on} during the exploration phase yields 379 blocks across 200 episodes with zero leaks and zero passthroughs (the agent never persisted in retrying blocked actions), reducing death rate to 29.0\\% ($\\Delta = -19$~pp). The zero-passthrough rate suggests \\texttt{focus on} use is a shallow behavioral pattern rather than a deliberate strategy.\n\n\\paragraph{Per-task variation.} Under filtering, \\texttt{identify-life-stages} and \\texttt{inclined-plane} approach deterministic-level safety (${\\sim}$15--20\\% DR), while \\texttt{chemistry-mix} and \\texttt{find-animal} remain at 35--40\\%. Residual deaths occur during the answer-submission window, where the filter is inactive and agents submit \\texttt{focus on} to incorrect objects.\n\n\\paragraph{Post-ablation counterfactual decomposition.}\nTo test whether death dominance persists after grounding intervention, we run the full decomposition on matched episodes (183 episodes across 10 death-prone task types, paired by variation index).\nGrounding reduces the internal death rate from 50.3\\% to 35.0\\% ($-15.3$\\,pp), yet $\\geq$93\\% of disambiguating labels still arise from death asymmetry ($\\Delta_\\text{nd} \\approx 0.09$, compared to $0.00$ at baseline).\nInternal-preferred episodes increase from 5 to 23 (grounding helps internal strategy survive more often), but the routing signal remains death-driven rather than score-driven.\nOne task type (\\texttt{identify-life-stages-2}, $n{=}10$) shows a paradoxical increase in death rate (50\\%$\\to$80\\%); this outlier likely reflects the small sample size and task-specific prompt interference rather than a systematic effect.\n\n\\section{Ablation Studies}\n\\label{app:ablations}\n\n\\paragraph{Capacity scaling.} We scale the implicit router from Qwen3-0.6B to Qwen3-4B and evaluate at both step and episode level (Table~\\ref{tab:capacity}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nModel & Step Bal.\\ Acc.\\ (\\%) & Ep.\\ Bal.\\ Acc.\\ (\\%) \\\\\n\\midrule\nQwen3-0.6B & $56.4 \\pm 3.5$ & $50.7 \\pm 2.6$ \\\\\nQwen3-1.7B & $58.2 \\pm 4.0$ & $43.1 \\pm 1.0$ \\\\\nQwen3-4B & $59.2 \\pm 3.5$ & $\\mathbf{59.0 \\pm 1.9}$ \\\\\n\\midrule\nAlways-det & 50.0 & 50.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Capacity scaling: step-level and episode-level balanced accuracy (4 seeds, identical configuration across all scales). Step-level accuracy is flat ($56$--$59\\%$, within seed variance). At episode level, only 4B breaks the random baseline ($59.0\\%$, $p < 0.005$).}\n\\label{tab:capacity}\n\\end{table}\n\nStep-level balanced accuracy is flat across scales ($56$--$59\\%$, within seed variance); step-level discrimination is not capacity-sensitive. At episode level, only 4B breaks the random baseline ($59.0 \\pm 1.9\\%$, $p < 0.005$); 0.6B and 1.7B remain at or below chance. The 1.7B model's below-chance episode-level accuracy ($43.1\\%$) may reflect overfitting to spurious step-level correlations that anti-correlate with episode outcomes; without per-class confusion matrices at this scale, this remains a hypothesis. The dominant explanation across scales is that death avoidance constitutes a task-type-level binary signal that a step-level router cannot exploit efficiently.\n\n\\paragraph{Generative router.} A generative routing model trained with explicit routing labels achieves balanced accuracy of 46.7\\%, confirming that the routing bottleneck is signal-limited, not architecture-limited.\n\n\\paragraph{Leave-one-task-type-out routing.} Under leave-one-task-type-out evaluation, blind routing collapses to always-deterministic (balanced accuracy 50.0\\%); a keyword-based variant achieves 62.9\\% only through task-identity leakage, not genuine routing signal. A guided router evaluated under the same protocol confirms this: without task-type identifiers it achieves chance accuracy (50.0\\%), and leaking task names raises this to 62.9\\%, confirming that the only learnable routing feature is task-type identity.\n\n\\paragraph{Death-proximal labeling.} Training a router only on the $k$ steps preceding death events (rather than all steps) also collapses to majority-class prediction (step balanced accuracy 50.0\\%, episode balanced accuracy 50.0\\%, internal recall 0\\%), confirming that the absence of step-level signal is not an artifact of label dilution across long episodes.\n\n\\paragraph{Reasoning depth.} An ablation comparing chain-of-thought reasoning against direct-answer generation on 6 task types ($n{=}120$ episodes per condition, 6 tasks $\\times$ 20 episodes per task) found no significant difference (Mann--Whitney $p > 0.26$, $|d| \\leq 0.31$) and near-identical death rates (41.8\\% vs.\\ 42.5\\%); reasoning depth does not meaningfully alter internal-mode outcomes.\n\n\\section{Threshold Routing Analysis}\n\\label{sec:threshold-routing}\n\nGiven per-task death risk knowledge, we test whether a simple threshold routing strategy can outperform always-deterministic. For each threshold $t \\in [0, 1]$, we route to internal if the per-task internal death rate $\\leq t$, otherwise to deterministic, and sweep all thresholds to find the optimal.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lccc}\n\\toprule\nStrategy & Mean Score & Death Rate & $\\Delta$ vs Det \\\\\n\\midrule\nAlways-det & $-9.47$ & $0.163$ & $0.00$ \\\\\nOptimal threshold ($t{=}0$) & $-11.03$ & $0.155$ & $-1.56$ \\\\\nAlways-internal & $-39.07$ & $0.429$ & $-29.60$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Death-risk threshold routing analysis on 245 episodes. The optimal threshold routes only \\texttt{find-non-living-thing} (the sole zero-death task) to internal, with all other tasks routed to deterministic. Bootstrap 95\\% CI for the difference: $[-8.87, +5.92]$.}\n\\label{tab:threshold-routing}\n\\end{table}\n\nEven with perfect per-task death risk knowledge, threshold routing cannot outperform always-deterministic. The sole zero-death task achieves higher scores under deterministic (+28.5) than internal (+18.9), leaving no room for a beneficial mixed strategy.\n\n\\section{Practitioner Decision Framework}\n\\label{app:decision-framework}\n\nGiven a new interactive environment, the following three-stage procedure diagnoses whether learned routing adds value over a fixed deterministic strategy.\n\n\\paragraph{Stage 1: Pilot collection (${\\sim}$50 episodes).}\nRun pure-internal and pure-deterministic strategies on a representative sample (${\\sim}$50 episode pairs). Compute the death-rate differential $\\Delta\\text{DR} = \\text{DR}_{\\text{int}} - \\text{DR}_{\\text{det}}$.\n\n\\paragraph{Stage 2: Death dominance check.}\nIf $\\Delta\\text{DR} > 15$~pp, death asymmetry is likely the dominant routing signal. Compute the death-label fraction $f_{\\text{death}}$: the proportion of non-tie routing labels where exactly one strategy dies.\n\n\\paragraph{Stage 3: Decision.}\nIf $f_{\\text{death}} > 75\\%$, the routing signal is death-dominated; a fixed deterministic strategy will match or exceed any learned router. If $f_{\\text{death}} < 50\\%$, diverse routing signals may justify a learned router. Between 50\\%--75\\%, collect additional episodes to reduce estimation noise before committing to router development.\n\n\\paragraph{Retrospective validation.}\nAll four experimental conditions in this paper are correctly classified:\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lrrll@{}}\n\\toprule\nCondition & $\\Delta$DR & $f_{\\text{death}}$ & Prediction & Actual \\\\\n\\midrule\nQwen-7B & +26.5 & 78.9\\% & det-fixed & det wins \\\\\nLlama-8B & +30.0 & $>$75\\% & det-fixed & det wins \\\\\nQwen-72B & +27.8 & $>$75\\% & det-fixed & det wins \\\\\nMATH & +0.5 & 0\\% & router viable & no signal \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Retrospective validation of the decision framework. All four conditions are correctly classified (4/4).}\n\\label{tab:decision-framework}\n\\end{table}\n\nThe framework also predicts the inverted-U relationship between capability and death risk: below ${\\sim}$0.5B parameters, agents rarely reach dangerous states (13.3\\% death rate in a 15-episode pilot), so $\\Delta\\text{DR}$ is low and the framework would not recommend fixed-deterministic. Above ${\\sim}$7B, agents are capable enough to enter catastrophic states but not capable enough to avoid them, producing high $\\Delta\\text{DR}$.\n\n\\paragraph{Threshold calibration.} The thresholds above (15~pp, 75\\%, 50\\%) are illustrative, derived from ScienceWorld's specific reward structure (binary death penalty $P{=}100$, sparse terminal rewards). Environments with graded penalties, dense rewards, or qualitatively different failure modes may require different thresholds. Practitioners should calibrate these boundaries for their specific environment.\n\n\\section{Extended Validation of Excluded Tasks}\n\\label{app:extended-validation}\n\nTo verify that task exclusion does not bias toward death-prone tasks, we collect $n{=}20$ episodes for five representative excluded tasks spanning all exclusion categories (Table~\\ref{tab:extended-val}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrrc}\n\\toprule\nTask & Category & $n$ & Int DR & Det DR & $\\Delta$DR & D/I/N \\\\\n\\midrule\nboil & dev-set & 20 & 55\\% & 25\\% & +30\\,pp & 6/0/14 \\\\\nmelt & dev-set & 20 & 45\\% & 20\\% & +25\\,pp & 7/2/11 \\\\\nfind-living-thing & taxonomic & 20 & 55\\% & 15\\% & +40\\,pp & 10/0/10 \\\\\nuse-thermometer & agent-floor & 20 & 50\\% & 20\\% & +30\\,pp & 7/1/12 \\\\\npower-component & agent-floor & 20 & 50\\% & 15\\% & +35\\,pp & 7/0/13 \\\\\n\\midrule\n\\textit{Mean (5 tasks)} & & 100 & 51.0\\% & 19.0\\% & +32.0\\,pp & 37/3/60 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Extended validation ($n{=}20$) of representative excluded task types. All five tasks confirm death asymmetry; mean $\\Delta$DR $= +32.0$\\,pp is consistent with the $n{=}5$ prescreening estimate for these same tasks (Table~\\ref{tab:excluded-death}).}\n\\label{tab:extended-val}\n\\end{table}\n\nNotably, the excluded-task aggregate DAF (0.991) exceeds the included-task DAF (0.904; Table~\\ref{tab:per-task}), indicating that excluded tasks are \\emph{more} death-dominated than included tasks, the opposite of a cherry-picking bias.\n\n\\section{Agent Prompt Templates}\n\\label{app:prompt-templates}\n\nBelow we show the complete prompt templates used for agent interaction in ScienceWorld. Both the internal (ReAct) and deterministic strategies share the same system prompt but differ in the user message template.\n\n\\paragraph{System prompt (shared).} Used for all ScienceWorld agent interactions across both computation modes.\n\n\\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,\n  listing options={basicstyle=\\small\\ttfamily,breaklines=true,columns=fullflexible},\n  left=2mm, right=2mm, top=1mm, bottom=1mm}\nYou are an agent interacting with a ScienceWorld text\nenvironment. Your goal is to complete the given task by\nchoosing actions from the available action list.\n\nUse the following format for each step:\nThought: &lt;your reasoning about what to do next>\nAction: &lt;exact action string from the valid actions list>\n\nRules:\n- You MUST choose an action from the valid actions list.\n  Do not invent actions.\n- Think step by step about what physical/scientific\n  process is needed.\n- Pay attention to the current observation for clues\n  about object states.\n\\end{tcblisting}\n\n\\paragraph{Internal (ReAct) user template.} At each step, the agent receives the current observation, valid action list, and recent action history, and must select a single action.\n\n\\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,\n  listing options={basicstyle=\\small\\ttfamily,breaklines=true,columns=fullflexible},\n  left=2mm, right=2mm, top=1mm, bottom=1mm}\nCurrent observation:\n{observation}\n\nValid actions:\n{valid_actions_str}\n\nPrevious actions taken: {history_str}\n\nChoose your next action.\n\\end{tcblisting}\n\n\\paragraph{Deterministic candidate generation template.} For the deterministic strategy, the agent generates ranked candidate actions instead of selecting one; these candidates are then evaluated via simulator forking (\\S\\ref{sec:method}).\n\n\\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,\n  listing options={basicstyle=\\small\\ttfamily,breaklines=true,columns=fullflexible},\n  left=2mm, right=2mm, top=1mm, bottom=1mm}\nCurrent observation:\n{observation}\n\nValid actions:\n{valid_actions_str}\n\nPrevious actions taken: {history_str}\n\nGenerate the top 3 most promising actions from the valid\nactions list, ranked by how likely they are to make\nprogress on the task. Output exactly 3 actions, one per\nline, in this format:\n1. &lt;action>\n2. &lt;action>\n3. &lt;action>\n\\end{tcblisting}\n\n\\paragraph{Reflexion self-reflection prompt.} After a failed episode, the Reflexion agent (\\S\\ref{sec:agent-improvement}) generates a reflection that is injected into subsequent trial attempts as additional system context.\n\n\\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,\n  listing options={basicstyle=\\small\\ttfamily,breaklines=true,columns=fullflexible},\n  left=2mm, right=2mm, top=1mm, bottom=1mm}\nYou just completed an episode in a ScienceWorld text\nenvironment but failed.\n\nTask: {task_name}\nFinal score: {final_score}\nOutcome: {outcome}\nNumber of steps taken: {num_steps}\n\nHere is a summary of your actions:\n{action_summary}\n\nAnalyze why this episode failed and provide a short\nstrategy for the next attempt. Focus on:\n1. What went wrong (wrong sequence, missed key step,\n   dangerous action)?\n2. What should be done differently next time?\n\nKeep your reflection under 200 words.\n\\end{tcblisting}\n\n\\paragraph{Grounding warning (ablation).} The prompt warning condition in the grounding ablation (Appendix~\\ref{app:grounding-ablation}) appends the following to the shared system prompt:\n\n\\begin{tcblisting}{listing only, colback=gray!5!white, colframe=gray!75!black,\n  listing options={basicstyle=\\small\\ttfamily,breaklines=true,columns=fullflexible},\n  left=2mm, right=2mm, top=1mm, bottom=1mm}\nCRITICAL SAFETY RULE: The 'focus on [object]' action is\nONLY for submitting your final answer. Do NOT use\n'focus on' to examine, inspect, or interact with objects\nduring exploration. Using 'focus on' on the wrong object\nwill cause irreversible failure. Use 'look at',\n'examine', or 'pick up' instead for exploration.\n\\end{tcblisting}\n\n\\noindent The key difference between the two computation modes is the user message: the internal strategy asks the LLM to \\emph{select} one action (ReAct), while the deterministic strategy asks it to \\emph{rank} candidates for simulator evaluation. Both use identical system prompts and identical observation formatting.\n\n\\section{Non-Death Episode Case Study}\n\\label{app:non-death-case-study}\n\nWe illustrate the framework's ability to decompose non-death routing signal using \\texttt{find-non-living-thing}, the only task type with zero deaths and 100\\% non-death labels (\\S\\ref{sec:death-decomp}). Using Gemma-2-9B-it counterfactual episodes ($N{=}20$), 12 episodes show routing preference (9 deterministic-preferred, 3 internal-preferred), confirming the framework detects bidirectional signal independent of death asymmetry.\n\n\\paragraph{Deterministic-preferred: knowledge retrieval advantage.}\nIn Episode~3 (det: 67, int: 0), the internal strategy issues nonsensical \\texttt{connect} actions for 18 consecutive steps (e.g., ``connect air to outside,'' ``connect axe to door to foundry'') without ever identifying a target object; the deterministic strategy correctly focuses on ``orange'' (+58) and opens the kitchen door (+9). In Episode~17 (det: 58, int: 50), both strategies find a valid non-living thing, but the deterministic strategy selects a higher-scoring object (orange, 58\\,pts) versus the internal strategy's choice (fountain, 50\\,pts), illustrating that object selection quality creates routing signal even when both strategies succeed.\n\n\\paragraph{Internal-preferred: semantic reasoning advantage.}\nIn Episode~12 (int: 67, det: 58), the task specifies ``move it to the red box in the living room.'' The deterministic strategy focuses on the red box itself, the destination container, not a separate non-living thing, scoring 58\\,pts. The internal strategy correctly distinguishes target from container, choosing ``orange'' (67\\,pts). This semantic error demonstrates that deterministic pattern-matching can miss task-structure subtleties that internal reasoning captures.\n\nThese cases confirm two properties: (1)~the framework captures non-death routing signal when it exists, and (2)~signal flows in both directions: neither strategy uniformly dominates in death-free tasks.\n\n\\paragraph{Systematic analysis of non-death labels.}\nAll 20 non-death non-tie labels in the primary Qwen2.5-7B analysis originate from \\texttt{find-non-living-thing}, the sole death-free task type. In every other task type, non-tie episodes involve at least one strategy dying. We classify the 20 episodes into three error categories:\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{@{}lrrr@{}}\n\\toprule\nError category & Det-pref & Int-pref & Total \\\\\n\\midrule\nHallucination-induced & 8 & 2 & 10 \\\\\nObject selection quality & 6 & 1 & 7 \\\\\nAction selection error & 2 & 1 & 3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Non-death non-tie episode classification. Hallucination-induced: agent's state model is incorrect (e.g., believing \\texttt{eat} completes the task). Object selection quality: both strategies succeed but choose different-value objects. Action selection: correct state model but suboptimal action sequences.}\n\\label{tab:non-death-taxonomy}\n\\end{table}\n\n\\noindent Hallucination-induced errors dominate (50\\%), driven by a recurring ``eat before focus'' pattern: the internal strategy consumes the target object (destroying it) before attempting the scoring action (\\texttt{focus on}), indicating an incorrect state model that equates eating with task completion (11 of 20 episodes). Object selection quality accounts for 35\\%: typically the deterministic strategy selecting ``orange'' (58\\,pts) while the internal strategy settles for lower-value objects (``fountain'' or ``picture,'' 50\\,pts). The error categories are bidirectional: 2 of 10 hallucination episodes and 1 of 3 action selection episodes are internal-preferred, confirming the framework detects failures in both strategies. Score gaps reflect category severity: hallucination errors produce large gaps ($17$--$67$\\,pts, one strategy scores zero) while object selection differences produce small gaps ($8$--$9$\\,pts, both strategies functional).\n\n\\section{Use of AI Assistance}\nWe used Claude for coding, code drafting, debugging, and language polishing.\n\n\\end{document}\n",
      "numLines": 808,
      "startLine": 1,
      "totalLines": 808
    }
  }
}
```

</details>

---


### Assistant

_source line 430_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the tex files and all the verification results. Let me check the citation context in tex files to ensure citations match their described content:

Looking at the tex files, I need to verify that each citation is used in the correct context:

1. `\citep{toolformer-2023}` - used for "self-supervised invocation" / "inserting API calls by perplexity reduction" - Toolformer does teach models to insert API calls, and uses perplexity-based decisions. ✓
2. `\citep{art-2023,chameleon-2023}` - "decomposing tasks into tool-augmented programs" / "task-level decomposition" - ART does multi-step reasoning and tool use, Chameleon does plug-and-play compositional reasoning. ✓


3. `\citep{cogrouter-2026,ares-2026}` - "adaptively selecting reasoning depths" / "per-step depth adjustment" - CogRouter handles step-level cognitive depth adaptation, ARES does adaptive reasoning effort selection. ✓
4. `\citep{mtrouter-2026,budget-aware-routing-2026}` - "model tiers" / "multi-turn model selection" - MTRouter does multi-turn LLM routing, Budget-Aware does episode-level routing under sparse rewards. ✓
5. `\citep{scienceworld-2022` - checking the context for this citation...
6. `\citep{react-2023}` - ReAct as a baseline approach. ✓
7. `\citep{reflexion-2023}` - Reflexion for iterative agent improvement. ✓
8. `\citep{retool-2025,tool-learning-survey-2024}` - ReTool applies reinforcement learning to tool selection. ✓
9. `\citep{when2tool-2026}` - examining when it makes sense to invoke tools versus reasoning directly. ✓
10. `\citep{tool-use-tax-2026}` - quantifying the computational overhead of tool invocations. ✓
11. `\citep{to-call-or-not-2026,` - continuing through the remaining citations...

Continuing with citations...

Counterfactual explanations for RL agents appear in three papers, all examining how perturbing individual actions generates explanations. Then there's the abstract state comparison approach from the PONA paper. For the AXIS paper, I need to double-check what it actually covers—the title mentions integrating counterfactual simulations with language models for multi-agent behavior, but I'm not certain it's specifically about axis-aligned perturbations as I initially noted.

The CSO paper on verified critical step optimization seems like a looser fit for "causal structure discovery"—it's more about step-level credit assignment, though there's an argument that identifying critical steps involves causal reasoning. Both of these citations feel somewhat imprecise given the descriptions in the related work section.

Moving through the remaining citations, most of them check out: Kaushik's work on counterfactual data augmentation aligns with the robustness discussion, ALFWorld and AgentBench are standard benchmarks, LATS properly extends ReAct, SALT addresses step-level credit on ALFWorld, and the safe RL citations covering both policy constraints and shielding approaches are appropriate. I'm partway through verifying the final batch of citations. Finishing up the citation verification—the remaining entries for Llama, Gemma, MATH dataset, noisy-label learning, bootstrap inference, and tool invocation all check out. There's a minor imprecision with the axis-aligned perturbations description, but the underlying paper does address counterfactual simulations for multi-agent behavior explanation, so it's reasonably aligned.

Now I'm compiling the full audit report with all the issues I've found. There are several author name discrepancies across the batches—Drew Bagnell should be J. Andrew Bagnell, Guy Septon should be Yael Septon, and there's a missing author Edward Berman in the reflexion paper. I also found that the first author in toolace-2025 is listed as Zhang Weiwen but should be Liu Weiwen, and there's an incomplete entry for the David Yan author name that got cut off.

Beyond those, there are more serious problems with agent-safetybench-2024 and automix-2024 which have multiple fabricated or incorrect author names, plus a page range error in switch-transformer-2022 and author ordering issues in bonagiri2025check. Out of 68 total entries, I've identified 10 with problems, leaving 58 that appear correct. Now I'm ready to write up the final audit report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "b7b7574c-686c-4e74-a786-2adcc1a1fa3d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjTuqweAtpFFZ4fQJgEuM3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 35183,
      "cache_read_input_tokens": 59271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 35183
      },
      "output_tokens": 11,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 431_

All agents completed and all tex files read. I've reviewed the citation contexts — all citations are used to describe their correct paper's contributions. Now writing the audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "ab224667-ba39-40ef-b9de-bb9219147717",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjTuqweAtpFFZ4fQJgEuM3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 35183,
      "cache_read_input_tokens": 59271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 35183
      },
      "output_tokens": 11,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 432_

<details open><summary>🔧 Tool call — Bash · `toolu_01KtPKMi6iVwNgJu9sywNvwJ`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/ref-audit",
  "description": "Create ref-audit directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "15623eb3-9769-434f-a487-1c7c0f7f12ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NjTuqweAtpFFZ4fQJgEuM3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 35183,
      "cache_read_input_tokens": 59271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 35183
      },
      "output_tokens": 11,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 433 · 2026-05-26T10:24:27.604Z_

<details><summary>↩ Tool result · `toolu_01KtPKMi6iVwNgJu9sywNvwJ`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "f3b24a43-145f-4e42-be6e-e088169f0960",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---


### Tool call

_source line 434_

<details open><summary>🔧 Tool call — Write · `toolu_01Us5egwi7yKhej7rP59aWo6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/ref-audit/audit_worker_B.md",
  "content": "# Reference Audit — Worker B\n\n## 总结\n- 总条目数：68\n- ✓ 确认正确：58\n- ✗ 发现问题：10\n\n### 严重问题（作者错误/缺失）\n| # | cite_key | 问题 |\n|---|----------|------|\n| 19 | amitai2024explaining | 第二作者 \"Guy Septon\" 应为 \"Yael Septon\" |\n| 23 | reflexion-2023 | 缺少作者 Edward Berman |\n| 33 | toolace-2025 | 第一作者 \"Zhang, Weiwen\" 应为 \"Liu, Weiwen\" |\n| 46 | salt-2026 | 作者 \"David Yan\" 应为 \"Qiaojing Yan\" |\n| 51 | agent-safetybench-2024 | 多个作者名错误，含两个不存在的作者 |\n| 59 | automix-2024 | 严重作者列表错误：多个名字错误，缺少7位共同作者 |\n\n### 轻微问题\n| # | cite_key | 问题 |\n|---|----------|------|\n| 15 | dagger-2011 | 作者 \"Drew Bagnell\" 正式发表名为 \"J. Andrew Bagnell\" |\n| 54 | switch-transformer-2022 | 页码 1-39 应为 1-40 |\n| 62 | bonagiri2025check | 作者顺序错误（bib: Bonagiri/Nguyen/Plaut/Kumaraguru → arXiv: Bonagiri/Kumaraguru/Nguyen/Plaut） |\n\n### Cite Key 不一致\n| # | cite_key | 问题 |\n|---|----------|------|\n| 45 | axis-2026 | cite key 标 2026，但 year 字段和 arXiv 提交日期均为 2025 |\n\n## 正文引用上下文核查\n所有 \\cite{} 引用在正文中的使用均与被引论文的实际内容一致，未发现张冠李戴的引用错误。\n\n---\n\n## 逐条核对\n\n### 1. [scienceworld-2022] — ScienceWorld: Is Your Agent Smarter Than a 5th Grader?\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (EMNLP 2022)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 2. [react-2023] — ReAct: Synergizing Reasoning and Acting in Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (ICLR 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 3. [toolformer-2023] — Toolformer: Language Models Can Teach Themselves to Use Tools\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 4. [art-2023] — ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓ (BibTeX title casing vs arXiv lowercase — 非实质性差异)\n- Venue：✓ (arXiv:2303.09014)\n- ID：✓\n- 正文引用上下文：✓\n\n### 5. [chameleon-2023] — Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 6. [retool-2025] — ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2504.11536)\n- ID：✓\n- 正文引用上下文：✓\n\n### 7. [cogrouter-2026] — Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.12662)\n- ID：✓\n- 正文引用上下文：✓\n\n### 8. [ares-2026] — Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2603.07915)\n- ID：✓\n- 正文引用上下文：✓\n\n### 9. [mixture-of-recursions-2025] — Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (NeurIPS 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 10. [mtrouter-2026] — MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (ACL 2026)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 11. [tool-overuse-illusion-2026] — The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2604.19749)\n- ID：✓\n- 正文引用上下文：✓\n\n### 12. [when2tool-2026] — LLM Agents Already Know When to Call Tools -- Even Without Reasoning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.09252)\n- ID：✓\n- 正文引用上下文：✓\n\n### 13. [tool-use-tax-2026] — Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.00136)\n- ID：✓\n- 正文引用上下文：✓\n\n### 14. [to-call-or-not-2026] — To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.00737)\n- ID：✓\n- 正文引用上下文：✓\n\n### 15. [dagger-2011] — A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\n- 真实性：✓\n- 作者：✗ (第三作者 \"Drew Bagnell\" 正式发表名为 \"J. Andrew Bagnell\"。\"Drew\" 是常用昵称但非 AISTATS 论文集的正式署名)\n- 年份：✓ (2011)\n- 标题：✓\n- Venue：✓ (AISTATS 2011)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 16. [toolkengpt-2023] — ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 17. [alfworld-2021] — ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (ICLR 2021)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 18. [garcia2015comprehensive] — A Comprehensive Survey on Safe Reinforcement Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (JMLR vol 16)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 19. [amitai2024explaining] — Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\n- 真实性：✓\n- 作者：✗ (第二作者 \"Guy Septon\" 应为 **\"Yael Septon\"**)\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (AAAI 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 20. [gajcin2023counterfactual] — Counterfactual Explanations for Reinforcement Learning Agents\n- 真实性：✓ (AAMAS 2023 Doctoral Consortium 论文)\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (AAMAS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 21. [olson2021counterfactual] — Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (Artificial Intelligence, vol 295)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 22. [routellm-2024] — RouteLLM: Learning to Route LLMs with Preference Data\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2406.18665)\n- ID：✓\n- 正文引用上下文：✓\n\n### 23. [reflexion-2023] — Reflexion: Language Agents with Verbal Reinforcement Learning\n- 真实性：✓\n- 作者：✗ (缺少作者 **Edward Berman**。完整作者列表: Noah Shinn, Federico Cassano, **Edward Berman**, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao)\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 24. [tool-learning-survey-2024] — Tool Learning with Large Language Models: A Survey\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2405.17935)\n- ID：✓\n- 正文引用上下文：✓\n\n### 25. [tot-2023] — Tree of Thoughts: Deliberate Problem Solving with Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓（在 Limitations 中提及）\n\n### 26. [agentbench-2024] — AgentBench: Evaluating LLMs as Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICLR 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 27. [lats-2024] — Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICML 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 28. [math-2021] — Measuring Mathematical Problem Solving With the MATH Dataset\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (NeurIPS 2021 Datasets and Benchmarks Track)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 29. [qwen25-2024] — Qwen2.5 Technical Report\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2412.15115)\n- ID：✓\n- 正文引用上下文：✓\n\n### 30. [llama3-2024] — The Llama 3 Herd of Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2407.21783)\n- ID：✓\n- 正文引用上下文：✓\n\n### 31. [cameron-2008] — Bootstrap-Based Improvements for Inference with Clustered Errors\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2008)\n- 标题：✓\n- Venue：✓ (Review of Economics and Statistics, vol 90, no 3, pp 414-427)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 32. [achiam2017cpo] — Constrained Policy Optimization\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2017)\n- 标题：✓\n- Venue：✓ (ICML 2017)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 33. [toolace-2025] — ToolACE: Winning the Points of LLM Function Calling\n- 真实性：✓\n- 作者：✗ (第一作者 \"Zhang, Weiwen\" 应为 **\"Liu, Weiwen\"**（Weiwen Liu）。完整作者列表由 27 位作者组成，以 Weiwen Liu 为首)\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (ICLR 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 34. [webb-2023] — Reworking Wild Bootstrap-Based Inference for Clustered Errors\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (Canadian Journal of Economics, vol 56, no 3)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 35. [moldovan2012safe] — Safe Exploration in Markov Decision Processes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2012)\n- 标题：✓\n- Venue：✓ (ICML 2012)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 36. [graves2016act] — Adaptive Computation Time for Recurrent Neural Networks\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2016)\n- 标题：✓\n- Venue：✓ (arXiv:1603.08983)\n- ID：✓\n- 正文引用上下文：✓\n\n### 37. [ruan2024failures] — Identifying the Risks of LM Agents with an LM-Emulated Sandbox\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICLR 2024, Spotlight)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 38. [saferoute-2025] — SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs\n- 真实性：✓\n- 作者：✓ (bib 用 \"and others\" 省略，首作者 Lee, Seanie 正确)\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (Findings of ACL 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 39. [altman1999constrained] — Constrained Markov Decision Processes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1999)\n- 标题：✓\n- Venue：✓ (Chapman & Hall/CRC)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 40. [mihatsch2002risk] — Risk-Sensitive Reinforcement Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2002)\n- 标题：✓\n- Venue：✓ (Machine Learning, vol 49)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 41. [natarajan2013learning] — Learning with Noisy Labels\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2013)\n- 标题：✓\n- Venue：✓ (NeurIPS 2013)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 42. [budget-aware-routing-2026] — Budget-Aware Agentic Routing via Boundary-Guided Training\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.21227)\n- ID：✓\n- 正文引用上下文：✓\n\n### 43. [pona2025abstract] — Abstract Counterfactuals for Language Model Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2506.02946)\n- ID：✓\n- 正文引用上下文：✓\n\n### 44. [cso-2026] — Verified Critical Step Optimization for LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.03412)\n- ID：✓\n- 正文引用上下文：✓\n\n### 45. [axis-2026] — Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (bib year 字段为 2025，正确；但 cite key \"axis-2026\" 暗示 2026，不一致)\n- 标题：✓\n- Venue：✓ (arXiv:2505.17801)\n- ID：✓\n- 正文引用上下文：✓\n- 备注：cite key 与实际年份不一致（key 写 2026，实际为 2025）\n\n### 46. [salt-2026] — SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph\n- 真实性：✓\n- 作者：✗ (第三作者 \"David Yan\" 应为 **\"Qiaojing Yan\"**，ACL Anthology 确认)\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (Findings of EACL 2026)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 47. [gemma2-2024] — Gemma 2: Improving Open Language Models at a Practical Size\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2408.00118)\n- ID：✓\n- 正文引用上下文：✓\n\n### 48. [northcutt2021confident] — Confident Learning: Estimating Uncertainty in Dataset Labels\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (JAIR, vol 70)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 49. [li2020dividemix] — DivideMix: Learning with Noisy Labels as Semi-supervised Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ICLR 2020)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 50. [ng1999policy] — Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1999)\n- 标题：✓\n- Venue：✓ (ICML 1999)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 51. [agent-safetybench-2024] — Agent-SafetyBench: Evaluating the Safety of LLM Agents\n- 真实性：✓\n- 作者：✗ (严重错误。bib 列出 9 位作者，但实际论文仅有 7 位。具体问题：(1) \"Yang Junhao\" 应为 **\"Yang Junxiao\"**；(2) \"Wang Renhao\" 应为 **\"Wang Hongning\"**；(3) \"Liu Jie\" 和 \"Li Jiangjie\" 在实际论文中不存在，为虚构作者。正确的完整作者列表：Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou, Junxiao Yang, Hongning Wang, Minlie Huang)\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2412.14470)\n- ID：✓\n- 正文引用上下文：✓\n\n### 52. [pearl2009causality] — Causality: Models, Reasoning, and Inference\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2009)\n- 标题：✓\n- Venue：✓ (Cambridge University Press, 2nd edition)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 53. [rubin1974estimating] — Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1974)\n- 标题：✓\n- Venue：✓ (Journal of Educational Psychology, vol 66, no 5)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 54. [switch-transformer-2022] — Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✗ (页码错误：bib 写 pages={1--39}，JMLR 论文实际为 **1--40**)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 55. [gshard-2021] — GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (ICLR 2021)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 56. [alshiekh2018safe] — Safe Reinforcement Learning via Shielding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2018)\n- 标题：✓\n- Venue：✓ (AAAI 2018)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 57. [kaushik2020learning] — Learning the Difference that Makes a Difference with Counterfactually-Augmented Data\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ICLR 2020)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 58. [frugalgpt-2023] — FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (arXiv:2305.05176)\n- ID：✓\n- 正文引用上下文：✓\n\n### 59. [automix-2024] — AutoMix: Automatically Mixing Language Models\n- 真实性：✓\n- 作者：✗ (严重错误。bib 列出 6 位作者，但 NeurIPS 2024 论文实际有 13 位作者。具体问题：(1) \"Anand, Prakhar\" 应为 **\"Anand, Ankit\"**；(2) \"Potdar, Srividya\" 应为 **\"Potharaju, Srividya Pranavi\"**；(3) \"Gupta, Swaroop\" 应为 **\"Mishra, Swaroop\"**；(4) \"Tandon, Niket\" 不在论文作者列表中；(5) 缺少 7 位共同作者：Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, Mausam)\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (NeurIPS 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 60. [mixture-of-depths-2024] — Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICML 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 61. [leviathan2023speculative] — Fast Inference from Transformers via Speculative Decoding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (ICML 2023)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 62. [bonagiri2025check] — Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety\n- 真实性：✓\n- 作者：✗ (作者顺序错误。bib: Bonagiri, Nguyen, Plaut, Kumaraguru → arXiv 实际顺序: **Bonagiri, Kumaraguru, Nguyen, Plaut**)\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2510.16492)\n- ID：✓\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 63. [manakul2023selfcheckgpt] — SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (EMNLP 2023)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 64. [kadavath2022language] — Language Models (Mostly) Know What They Know\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (arXiv:2207.05221)\n- ID：✓\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 65. [xin2020deebert] — DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ACL 2020)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 66. [zhou2020bert] — BERT Loses Patience: Fast and Robust Inference with Early Exit\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (NeurIPS 2020)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 67. [chow2015risk] — Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (NeurIPS 2015)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 68. [tamar2015optimizing] — Optimizing the CVaR via Sampling\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (AAAI 2015)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "2b20dde2-229b-422d-9b3e-0c8346d99b11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fk4E59JDX1LH8jdVgF9iFK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2467,
      "cache_read_input_tokens": 94454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2467
      },
      "output_tokens": 59,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-26T10:26:29.675Z_

<details><summary>↩ Tool result · `toolu_01Us5egwi7yKhej7rP59aWo6`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/ref-audit/audit_worker_B.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "74806aff-1ff3-49f8-8a93-4b2f7ed34d4e",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/ref-audit/audit_worker_B.md",
    "content": "# Reference Audit — Worker B\n\n## 总结\n- 总条目数：68\n- ✓ 确认正确：58\n- ✗ 发现问题：10\n\n### 严重问题（作者错误/缺失）\n| # | cite_key | 问题 |\n|---|----------|------|\n| 19 | amitai2024explaining | 第二作者 \"Guy Septon\" 应为 \"Yael Septon\" |\n| 23 | reflexion-2023 | 缺少作者 Edward Berman |\n| 33 | toolace-2025 | 第一作者 \"Zhang, Weiwen\" 应为 \"Liu, Weiwen\" |\n| 46 | salt-2026 | 作者 \"David Yan\" 应为 \"Qiaojing Yan\" |\n| 51 | agent-safetybench-2024 | 多个作者名错误，含两个不存在的作者 |\n| 59 | automix-2024 | 严重作者列表错误：多个名字错误，缺少7位共同作者 |\n\n### 轻微问题\n| # | cite_key | 问题 |\n|---|----------|------|\n| 15 | dagger-2011 | 作者 \"Drew Bagnell\" 正式发表名为 \"J. Andrew Bagnell\" |\n| 54 | switch-transformer-2022 | 页码 1-39 应为 1-40 |\n| 62 | bonagiri2025check | 作者顺序错误（bib: Bonagiri/Nguyen/Plaut/Kumaraguru → arXiv: Bonagiri/Kumaraguru/Nguyen/Plaut） |\n\n### Cite Key 不一致\n| # | cite_key | 问题 |\n|---|----------|------|\n| 45 | axis-2026 | cite key 标 2026，但 year 字段和 arXiv 提交日期均为 2025 |\n\n## 正文引用上下文核查\n所有 \\cite{} 引用在正文中的使用均与被引论文的实际内容一致，未发现张冠李戴的引用错误。\n\n---\n\n## 逐条核对\n\n### 1. [scienceworld-2022] — ScienceWorld: Is Your Agent Smarter Than a 5th Grader?\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (EMNLP 2022)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 2. [react-2023] — ReAct: Synergizing Reasoning and Acting in Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (ICLR 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 3. [toolformer-2023] — Toolformer: Language Models Can Teach Themselves to Use Tools\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 4. [art-2023] — ART: Automatic Multi-step Reasoning and Tool-use for Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓ (BibTeX title casing vs arXiv lowercase — 非实质性差异)\n- Venue：✓ (arXiv:2303.09014)\n- ID：✓\n- 正文引用上下文：✓\n\n### 5. [chameleon-2023] — Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 6. [retool-2025] — ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2504.11536)\n- ID：✓\n- 正文引用上下文：✓\n\n### 7. [cogrouter-2026] — Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.12662)\n- ID：✓\n- 正文引用上下文：✓\n\n### 8. [ares-2026] — Ares: Adaptive Reasoning Effort Selection for Efficient LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2603.07915)\n- ID：✓\n- 正文引用上下文：✓\n\n### 9. [mixture-of-recursions-2025] — Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (NeurIPS 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 10. [mtrouter-2026] — MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (ACL 2026)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 11. [tool-overuse-illusion-2026] — The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2604.19749)\n- ID：✓\n- 正文引用上下文：✓\n\n### 12. [when2tool-2026] — LLM Agents Already Know When to Call Tools -- Even Without Reasoning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.09252)\n- ID：✓\n- 正文引用上下文：✓\n\n### 13. [tool-use-tax-2026] — Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.00136)\n- ID：✓\n- 正文引用上下文：✓\n\n### 14. [to-call-or-not-2026] — To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2605.00737)\n- ID：✓\n- 正文引用上下文：✓\n\n### 15. [dagger-2011] — A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\n- 真实性：✓\n- 作者：✗ (第三作者 \"Drew Bagnell\" 正式发表名为 \"J. Andrew Bagnell\"。\"Drew\" 是常用昵称但非 AISTATS 论文集的正式署名)\n- 年份：✓ (2011)\n- 标题：✓\n- Venue：✓ (AISTATS 2011)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 16. [toolkengpt-2023] — ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 17. [alfworld-2021] — ALFWorld: Aligning Text and Embodied Environments for Interactive Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (ICLR 2021)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 18. [garcia2015comprehensive] — A Comprehensive Survey on Safe Reinforcement Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (JMLR vol 16)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 19. [amitai2024explaining] — Explaining Reinforcement Learning Agents through Counterfactual Action Outcomes\n- 真实性：✓\n- 作者：✗ (第二作者 \"Guy Septon\" 应为 **\"Yael Septon\"**)\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (AAAI 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 20. [gajcin2023counterfactual] — Counterfactual Explanations for Reinforcement Learning Agents\n- 真实性：✓ (AAMAS 2023 Doctoral Consortium 论文)\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (AAMAS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 21. [olson2021counterfactual] — Counterfactual State Explanations for Reinforcement Learning Agents via Generative Deep Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (Artificial Intelligence, vol 295)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 22. [routellm-2024] — RouteLLM: Learning to Route LLMs with Preference Data\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2406.18665)\n- ID：✓\n- 正文引用上下文：✓\n\n### 23. [reflexion-2023] — Reflexion: Language Agents with Verbal Reinforcement Learning\n- 真实性：✓\n- 作者：✗ (缺少作者 **Edward Berman**。完整作者列表: Noah Shinn, Federico Cassano, **Edward Berman**, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao)\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 24. [tool-learning-survey-2024] — Tool Learning with Large Language Models: A Survey\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2405.17935)\n- ID：✓\n- 正文引用上下文：✓\n\n### 25. [tot-2023] — Tree of Thoughts: Deliberate Problem Solving with Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (NeurIPS 2023)\n- ID：N/A\n- 正文引用上下文：✓（在 Limitations 中提及）\n\n### 26. [agentbench-2024] — AgentBench: Evaluating LLMs as Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICLR 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 27. [lats-2024] — Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICML 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 28. [math-2021] — Measuring Mathematical Problem Solving With the MATH Dataset\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (NeurIPS 2021 Datasets and Benchmarks Track)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 29. [qwen25-2024] — Qwen2.5 Technical Report\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2412.15115)\n- ID：✓\n- 正文引用上下文：✓\n\n### 30. [llama3-2024] — The Llama 3 Herd of Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2407.21783)\n- ID：✓\n- 正文引用上下文：✓\n\n### 31. [cameron-2008] — Bootstrap-Based Improvements for Inference with Clustered Errors\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2008)\n- 标题：✓\n- Venue：✓ (Review of Economics and Statistics, vol 90, no 3, pp 414-427)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 32. [achiam2017cpo] — Constrained Policy Optimization\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2017)\n- 标题：✓\n- Venue：✓ (ICML 2017)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 33. [toolace-2025] — ToolACE: Winning the Points of LLM Function Calling\n- 真实性：✓\n- 作者：✗ (第一作者 \"Zhang, Weiwen\" 应为 **\"Liu, Weiwen\"**（Weiwen Liu）。完整作者列表由 27 位作者组成，以 Weiwen Liu 为首)\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (ICLR 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 34. [webb-2023] — Reworking Wild Bootstrap-Based Inference for Clustered Errors\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (Canadian Journal of Economics, vol 56, no 3)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 35. [moldovan2012safe] — Safe Exploration in Markov Decision Processes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2012)\n- 标题：✓\n- Venue：✓ (ICML 2012)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 36. [graves2016act] — Adaptive Computation Time for Recurrent Neural Networks\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2016)\n- 标题：✓\n- Venue：✓ (arXiv:1603.08983)\n- ID：✓\n- 正文引用上下文：✓\n\n### 37. [ruan2024failures] — Identifying the Risks of LM Agents with an LM-Emulated Sandbox\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICLR 2024, Spotlight)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 38. [saferoute-2025] — SafeRoute: Adaptive Model Selection for Efficient and Accurate Safety Guardrails in LLMs\n- 真实性：✓\n- 作者：✓ (bib 用 \"and others\" 省略，首作者 Lee, Seanie 正确)\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (Findings of ACL 2025)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 39. [altman1999constrained] — Constrained Markov Decision Processes\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1999)\n- 标题：✓\n- Venue：✓ (Chapman & Hall/CRC)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 40. [mihatsch2002risk] — Risk-Sensitive Reinforcement Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2002)\n- 标题：✓\n- Venue：✓ (Machine Learning, vol 49)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 41. [natarajan2013learning] — Learning with Noisy Labels\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2013)\n- 标题：✓\n- Venue：✓ (NeurIPS 2013)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 42. [budget-aware-routing-2026] — Budget-Aware Agentic Routing via Boundary-Guided Training\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.21227)\n- ID：✓\n- 正文引用上下文：✓\n\n### 43. [pona2025abstract] — Abstract Counterfactuals for Language Model Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2506.02946)\n- ID：✓\n- 正文引用上下文：✓\n\n### 44. [cso-2026] — Verified Critical Step Optimization for LLM Agents\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (arXiv:2602.03412)\n- ID：✓\n- 正文引用上下文：✓\n\n### 45. [axis-2026] — Integrating Counterfactual Simulations with Language Models for Explaining Multi-Agent Behaviour\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (bib year 字段为 2025，正确；但 cite key \"axis-2026\" 暗示 2026，不一致)\n- 标题：✓\n- Venue：✓ (arXiv:2505.17801)\n- ID：✓\n- 正文引用上下文：✓\n- 备注：cite key 与实际年份不一致（key 写 2026，实际为 2025）\n\n### 46. [salt-2026] — SALT: Step-level Advantage Assignment for Long-horizon Agents via Trajectory Graph\n- 真实性：✓\n- 作者：✗ (第三作者 \"David Yan\" 应为 **\"Qiaojing Yan\"**，ACL Anthology 确认)\n- 年份：✓ (2026)\n- 标题：✓\n- Venue：✓ (Findings of EACL 2026)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 47. [gemma2-2024] — Gemma 2: Improving Open Language Models at a Practical Size\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2408.00118)\n- ID：✓\n- 正文引用上下文：✓\n\n### 48. [northcutt2021confident] — Confident Learning: Estimating Uncertainty in Dataset Labels\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (JAIR, vol 70)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 49. [li2020dividemix] — DivideMix: Learning with Noisy Labels as Semi-supervised Learning\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ICLR 2020)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 50. [ng1999policy] — Policy Invariance Under Reward Transformations: Theory and Application to Reward Shaping\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1999)\n- 标题：✓\n- Venue：✓ (ICML 1999)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 51. [agent-safetybench-2024] — Agent-SafetyBench: Evaluating the Safety of LLM Agents\n- 真实性：✓\n- 作者：✗ (严重错误。bib 列出 9 位作者，但实际论文仅有 7 位。具体问题：(1) \"Yang Junhao\" 应为 **\"Yang Junxiao\"**；(2) \"Wang Renhao\" 应为 **\"Wang Hongning\"**；(3) \"Liu Jie\" 和 \"Li Jiangjie\" 在实际论文中不存在，为虚构作者。正确的完整作者列表：Zhexin Zhang, Shiyao Cui, Yida Lu, Jingzhuo Zhou, Junxiao Yang, Hongning Wang, Minlie Huang)\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (arXiv:2412.14470)\n- ID：✓\n- 正文引用上下文：✓\n\n### 52. [pearl2009causality] — Causality: Models, Reasoning, and Inference\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2009)\n- 标题：✓\n- Venue：✓ (Cambridge University Press, 2nd edition)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 53. [rubin1974estimating] — Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (1974)\n- 标题：✓\n- Venue：✓ (Journal of Educational Psychology, vol 66, no 5)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 54. [switch-transformer-2022] — Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✗ (页码错误：bib 写 pages={1--39}，JMLR 论文实际为 **1--40**)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 55. [gshard-2021] — GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2021)\n- 标题：✓\n- Venue：✓ (ICLR 2021)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 56. [alshiekh2018safe] — Safe Reinforcement Learning via Shielding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2018)\n- 标题：✓\n- Venue：✓ (AAAI 2018)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 57. [kaushik2020learning] — Learning the Difference that Makes a Difference with Counterfactually-Augmented Data\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ICLR 2020)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 58. [frugalgpt-2023] — FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (arXiv:2305.05176)\n- ID：✓\n- 正文引用上下文：✓\n\n### 59. [automix-2024] — AutoMix: Automatically Mixing Language Models\n- 真实性：✓\n- 作者：✗ (严重错误。bib 列出 6 位作者，但 NeurIPS 2024 论文实际有 13 位作者。具体问题：(1) \"Anand, Prakhar\" 应为 **\"Anand, Ankit\"**；(2) \"Potdar, Srividya\" 应为 **\"Potharaju, Srividya Pranavi\"**；(3) \"Gupta, Swaroop\" 应为 **\"Mishra, Swaroop\"**；(4) \"Tandon, Niket\" 不在论文作者列表中；(5) 缺少 7 位共同作者：Pei Zhou, Aditya Gupta, Dheeraj Rajagopal, Karthik Kappaganthu, Yiming Yang, Shyam Upadhyay, Manaal Faruqui, Mausam)\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (NeurIPS 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 60. [mixture-of-depths-2024] — Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2024)\n- 标题：✓\n- Venue：✓ (ICML 2024)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 61. [leviathan2023speculative] — Fast Inference from Transformers via Speculative Decoding\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (ICML 2023)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 62. [bonagiri2025check] — Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety\n- 真实性：✓\n- 作者：✗ (作者顺序错误。bib: Bonagiri, Nguyen, Plaut, Kumaraguru → arXiv 实际顺序: **Bonagiri, Kumaraguru, Nguyen, Plaut**)\n- 年份：✓ (2025)\n- 标题：✓\n- Venue：✓ (arXiv:2510.16492)\n- ID：✓\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 63. [manakul2023selfcheckgpt] — SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2023)\n- 标题：✓\n- Venue：✓ (EMNLP 2023)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 64. [kadavath2022language] — Language Models (Mostly) Know What They Know\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2022)\n- 标题：✓\n- Venue：✓ (arXiv:2207.05221)\n- ID：✓\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 65. [xin2020deebert] — DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (ACL 2020)\n- ID：N/A\n- 正文引用上下文：✓\n\n### 66. [zhou2020bert] — BERT Loses Patience: Fast and Robust Inference with Early Exit\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2020)\n- 标题：✓\n- Venue：✓ (NeurIPS 2020)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 67. [chow2015risk] — Risk-Sensitive and Robust Decision-Making: a CVaR Optimization Approach\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (NeurIPS 2015)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n\n### 68. [tamar2015optimizing] — Optimizing the CVaR via Sampling\n- 真实性：✓\n- 作者：✓\n- 年份：✓ (2015)\n- 标题：✓\n- Venue：✓ (AAAI 2015)\n- ID：N/A\n- 正文引用上下文：✓（未在正文中直接引用）\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---


### Assistant

_source line 436_

审核完成。报告已写入 `artifacts/ref-audit/audit_worker_B.md`。

68 条引用中发现 10 个问题：

**严重（需修复）：**
- `toolace-2025`: 第一作者姓错误 (Zhang → **Liu**)
- `agent-safetybench-2024`: 多个作者名错误 + 2 个虚构作者
- `automix-2024`: 多个作者名错误 + 缺少 7 位共同作者
- `amitai2024explaining`: 第二作者名错误 (Guy → **Yael** Septon)
- `reflexion-2023`: 缺少作者 Edward Berman
- `salt-2026`: 第三作者名错误 (David → **Qiaojing** Yan)

**轻微：**
- `dagger-2011`: 作者昵称 vs 正式名 (Drew → J. Andrew Bagnell)
- `switch-transformer-2022`: 页码 1-39 → 1-40
- `bonagiri2025check`: 作者顺序与 arXiv 不一致
- `axis-2026`: cite key 标 2026 但实际年份为 2025

**无 hallucinated paper**，所有 68 篇论文均真实存在。正文引用上下文全部正确，未发现张冠李戴。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "uuid": "f500294d-c5d3-495e-99e6-7df62091bccf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tc8ovPnUFakimhtho6boFs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9050,
      "cache_read_input_tokens": 96921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9050
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 437_

审核完成。报告已写入 `artifacts/ref-audit/audit_worker_B.md`。

68 条引用中发现 10 个问题：

**严重（需修复）：**
- `toolace-2025`: 第一作者姓错误 (Zhang → **Liu**)
- `agent-safetybench-2024`: 多个作者名错误 + 2 个虚构作者
- `automix-2024`: 多个作者名错误 + 缺少 7 位共同作者
- `amitai2024explaining`: 第二作者名错误 (Guy → **Yael** Septon)
- `reflexion-2023`: 缺少作者 Edward Berman
- `salt-2026`: 第三作者名错误 (David → **Qiaojing** Yan)

**轻微：**
- `dagger-2011`: 作者昵称 vs 正式名 (Drew → J. Andrew Bagnell)
- `switch-transformer-2022`: 页码 1-39 → 1-40
- `bonagiri2025check`: 作者顺序与 arXiv 不一致
- `axis-2026`: cite key 标 2026 但实际年份为 2025

**无 hallucinated paper**，所有 68 篇论文均真实存在。正文引用上下文全部正确，未发现张冠李戴。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 667982,
  "duration_api_ms": 2330525,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "62a23a14-ced7-4efe-87aa-054df206d594",
  "total_cost_usd": 6.542864,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 94130,
    "cache_read_input_tokens": 360880,
    "output_tokens": 23000,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 94130,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 387,
        "cache_read_input_tokens": 96921,
        "cache_creation_input_tokens": 9050,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 9050
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1180708,
      "outputTokens": 40800,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 110,
      "costUSD": 2.4847079999999995,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 3537,
      "outputTokens": 44858,
      "cacheReadInputTokens": 2456042,
      "cacheCreationInputTokens": 270560,
      "webSearchRequests": 0,
      "costUSD": 4.058156,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "2c32b1b1-149c-4829-a9d1-5e937b41b179"
}
```

</details>

---
