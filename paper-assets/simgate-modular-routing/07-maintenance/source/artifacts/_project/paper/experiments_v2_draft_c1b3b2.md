# Experiments — Draft v2

\section{Experiments}

\subsection{Setup}
\label{sec:exp-setup}

We evaluate on ScienceWorld \cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ penalty upon agent death. Using the counterfactual methodology described in \S\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 episodes per type). The LLM backbone is Qwen2.5-7B-Instruct, served via vLLM, with episodes capped at 30 steps. The internal-reasoning strategy follows the ReAct paradigm \cite{react-2023}; the deterministic strategy uses the environment simulator for exact state transitions.

\subsection{Death Avoidance Decomposition}
\label{sec:death-decomp}

The full performance gap between deterministic and internal strategies across 245 episodes is $\Delta_{\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\Delta_{\text{no\_death}} = +2.84$. The resulting Death Avoidance Factor (\S\ref{sec:daf}) is 90.41\%: approximately 90\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.

This concentration is consistent across task types. The Pearson correlation between per-task death rate differential (internal minus deterministic) and $\Delta_{\text{full}}$ is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$), as shown in Figure~\ref{fig:decomposition}. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\% of episodes compared to 16.3\% for deterministic computation---a 2.6$\times$ ratio that drives the bulk of the observed score difference.

The episode-level label distribution reflects this asymmetry. Of 245 episodes, 86 are labeled \texttt{det\_preferred}, only 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preference}. The near-absence of internal-preferred labels---combined with the dominance of no-preference labels---indicates that when internal reasoning does not lead to catastrophic failure, it performs comparably to deterministic computation. The few internal-preferred episodes arise from tasks where deterministic computation's rigid action space occasionally produces suboptimal trajectories despite avoiding death.

One task reveals the residual non-death signal. \texttt{find-non-living-thing} ($n=40$) is the only task type with zero deaths under both strategies, yet it shows $\Delta_{\text{full}} = +9.58$, entirely from non-death performance differences. This confirms that routing value beyond death avoidance exists: deterministic computation can provide advantages through more accurate state tracking even when agents survive. However, this signal is not the dominant factor across the benchmark. Among the 10 death-prone task types, death avoidance overwhelms non-death differences. For example, \texttt{measure-melting-point-unknown} ($n=20$) exhibits death rates of 55\% (internal) and 25\% (deterministic), producing $\Delta_{\text{full}} = +30.05$---a gap driven primarily by the 30-percentage-point death rate differential rather than non-death performance.

When both modalities survive, their task performance is near-equivalent ($\Delta_{\text{no\_death}} = +2.84$). The value of deterministic computation in this environment is concentrated in preventing catastrophic failures, not in providing positive task guidance.

\subsection{Baselines}
\label{sec:baselines}

\begin{table}[t]
\centering
\small
\begin{tabular}{@{}lccc@{}}
\toprule
Strategy & Score & 95\% CI & Death \% \\
\midrule
Always-Internal & $-39.07$ & [$-44.89$, $-33.37$] & 42.9 \\
Always-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 16.3 \\
Random & $-22.38$ & [$-27.75$, $-17.09$] & 27.8 \\
Oracle & $-6.58$ & [$-10.65$, $-2.43$] & 14.3 \\
\midrule
Trained Router & $-10.70$ & [$-15.25$, $-6.38$] & 17.6 \\
\bottomrule
\end{tabular}
\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). Confidence intervals computed via bootstrap. The oracle selects the higher-scoring strategy per episode; 96.2\% of its decisions match the always-deterministic strategy.}
\label{tab:baselines}
\end{table}

Table~\ref{tab:baselines} reports episode-weighted mean scores and death rates for four unconditional strategies and the trained router. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\Delta_{\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.2\% of its routing decisions matching always-deterministic. This \emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\%) proportional to its 50/50 allocation.

The trained router (Qwen3-1.7B implicit router, seed 42) scores $-10.70$ [A], 1.23 points below always-deterministic [A]. Its death rate (17.6\% [A]) is comparable to always-deterministic (16.3\% [A]), confirming that the router avoids degeneration but does not improve upon unconditional deterministic routing in end-to-end deployment.

Keyword-based routing (\S\ref{sec:rule}) structurally fails to provide meaningful discrimination. ScienceWorld actions use generic interaction verbs (\texttt{pick up}, \texttt{move}, \texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\%, degenerating to always-deterministic) or negligible (v2: 4.9\%, v3: 2.8\%, both degenerating to always-internal). No keyword granularity bridges this gap.

\subsection{Router Training as Diagnostic}
\label{sec:router-diagnostic}

A natural question is whether the episode-level counterfactual labels can train a step-level router. We investigate this as a diagnostic probe of label informativeness rather than a routing system proposal, testing two architectures.

\paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\% internal recall in all cases). The episode-level labeling granularity does not transfer to step-level classification through this architecture.

\paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B) to internalize routing decisions within its generation process. At the logit level, routing patterns emerge: accuracy reaches 74.5\% with balanced accuracy of 79\%, demonstrating that the counterfactual labels encode learnable routing structure beyond what a degenerate always-deterministic predictor captures. At the generation level, however, accuracy drops to 65.36\% with internal recall of 51.5\%, revealing a gap between logit-level pattern recognition and generation-level expression.

End-to-end deployment (Table~\ref{tab:baselines}) confirms this gap: the trained router scores $-10.70$ [A] (CI [$-15.25$, $-6.38$] [A]), 1.23 points below always-deterministic ($-9.47$ [A]). Its 97.0\% [A] simulator invocation ratio means it routes to internal reasoning only 3\% of the time---near-always-deterministic behavior despite non-degenerate logit-level routing patterns.

Across four random seeds (42, 123, 456, 789), balanced accuracy is stable at $58.1 \pm 0.8\%$ [A]---only 8 percentage points above random chance. However, internal recall varies from 51.5\% to 81.8\% [A] (30+ percentage point range), indicating that the decision boundary orientation is seed-dependent while overall discriminability is not. This pattern---consistent weak signal with unstable thresholds---further supports the interpretation that the labels encode minimal routing structure beyond death avoidance: there is enough signal for the model to avoid degeneration, but not enough for robust, seed-invariant routing decisions.

These results yield two observations. First, the counterfactual labels encode genuine routing patterns at the representation level---the logit-level success rules out uninformative labels as the cause of classification head failure, pointing instead to the episode-to-step granularity mismatch as the bottleneck. Second, while the labels reveal learnable routing patterns at the logit level, generation-level expression of these patterns remains an open challenge. Whether this gap stems from the labeling granularity, the generation decoding process, or model capacity is under investigation; step-level counterfactual labeling may be a productive direction for bridging it.

\subsection{Limitations}
\label{sec:limitations}

Our analysis is conducted on a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. ScienceWorld's severe $-100$ death penalty may amplify the death avoidance signal; environments with less catastrophic failure penalties could exhibit a lower DAF, though the qualitative finding---death avoidance as a major component of routing signal---may still hold. Our counterfactual labels operate at episode granularity; step-level labeling with denser reward signals is a natural extension that could improve both decomposition resolution and router training. The gap between logit-level and generation-level routing accuracy in the implicit router warrants further investigation.
