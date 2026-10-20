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

\subsection{Baselines and Trained Router}
\label{sec:baselines}

\begin{table}[t]
\centering
\small
\begin{tabular}{@{}lcccccc@{}}
\toprule
Strategy & Score & 90\% CI & Succ.\,\% $\uparrow$ & Death\,\% $\downarrow$ & Sim\,\% \\
\midrule
Always-Internal & $-39.07$ & [$-44.89$, $-33.37$] & --- & 42.9 & 0 \\
Always-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 23.7 & 16.3 & 100 \\
Random & $-22.38$ & [$-27.75$, $-17.09$] & --- & 27.8 & 50.3 \\
Oracle & $-6.58$ & [$-10.65$, $-2.43$] & --- & 14.3 & 96.2 \\
\midrule
Trained Router (Ours) & $-10.70$ & [$-15.25$, $-6.38$] & 23.7 & 17.6 & 97.0 \\
\bottomrule
\end{tabular}
\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes; plan-003-e2e-ablation-b-correct / plan-003-baseline-245eps). Confidence intervals via bootstrap (90\%). \emph{Sim\,\%}: fraction of steps routed to the deterministic simulator. The oracle selects the higher-scoring strategy per episode; 96.2\% of its decisions match always-deterministic. The trained router uses the ablation-b implicit checkpoint (plan-004-implicit/final\_adapter, internal\_recall\,=\,51.52\%).}
\label{tab:baselines}
\end{table}

Table~\ref{tab:baselines} reports episode-weighted mean scores, success rates, and death rates for four unconditional strategies and our trained router. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\Delta_{\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.2\% of its routing decisions matching always-deterministic. This \emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\%) proportional to its 50/50 allocation.

The trained router scores $-10.70$ [$-15.25$, $-6.38$], \emph{worse} than always-deterministic by 1.23 points ($\Delta_{\text{vs-det}} = -1.23$; plan-003-e2e-ablation-b-correct). Its 90\% confidence interval includes the always-deterministic point estimate ($-9.47$), so the difference is not statistically significant, but the point estimate is directionally negative. The router routes 97.0\% of steps to the simulator (Sim\,\%), closely tracking always-deterministic, with a 70.6\% episode-level fallback rate (173/245 episodes; plan-003-e2e-ablation-b-correct). In other words, the best router we trained---using the only non-degenerate checkpoint in the project (ablation-b, internal\_recall\,=\,51.52\%)---cannot improve upon the unconditional deterministic baseline. This is consistent with C1: when death avoidance dominates the routing signal, the optimal policy approximates always-deterministic, and a learned router has insufficient signal to deviate productively.

Keyword-based routing (\S\ref{sec:rule}) structurally fails to provide meaningful discrimination. ScienceWorld actions use generic interaction verbs (\texttt{pick up}, \texttt{move}, \texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\%, degenerating to always-deterministic) or negligible (v2: 4.9\%, v3: 2.8\%, both degenerating to always-internal). No keyword granularity bridges this gap (plan-011-rule-based).

\subsection{Router Training as Diagnostic}
\label{sec:router-diagnostic}

A natural question is whether the episode-level counterfactual labels can train a step-level router. We investigate this as a diagnostic probe of label informativeness rather than a routing system proposal, testing two architectures.

\paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\% internal recall in all cases; plan-002-formal-v4 through v6). The episode-level labeling granularity does not transfer to step-level classification through this architecture.

\paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B + LoRA $r\!=\!16$) to internalize routing decisions within its generation process, using 2040 training samples from 11 task types with minority upsampling (\texttt{upsample\_minority=true}; plan-004-ablation-b). At the generation level, the best seed achieves accuracy 65.36\% with balanced accuracy 59.27\% and internal recall 51.52\%---above the 30\% non-degeneracy threshold but only 8 percentage points above random (plan-004-ablation-b). End-to-end deployment of this checkpoint yields $-10.70$ [$-15.25$, $-6.38$] (Table~\ref{tab:baselines}), worse than always-deterministic by 1.23 points (plan-003-e2e-ablation-b-correct).

\paragraph{Seed stability.} To assess the robustness of implicit router training, we repeat ablation-b across 4 seeds (42, 123, 456, 789; plan-004-ablation-b, plan-004-ablation-b-seed123/456/789). Balanced accuracy is stable: 59.27\%, 57.36\%, 57.48\%, 58.31\% ($\mu = 58.1\%$, $\sigma = 0.8\%$), confirming a weak but reproducible learned signal approximately 8 percentage points above random. However, internal recall varies dramatically: 51.52\%, 57.58\%, 75.76\%, 81.82\% (range $>$\,30\,pp). This dissociation---stable discrimination (balanced accuracy) with unstable decision boundaries (internal recall)---indicates that the router captures a marginal signal insufficient to produce a consistent routing policy. The learned decision boundary between ``route to internal'' and ``route to deterministic'' is seed-dependent, shifting across the near-random classification surface. This reinforces C1: under death avoidance dominance, the episode-level labels encode too little non-death signal for a router to learn a stable, productive departure from always-deterministic.

These results yield two observations. First, the counterfactual labels encode genuine routing patterns at the representation level---the implicit router's above-chance balanced accuracy ($58.1 \pm 0.8\%$ across 4 seeds) rules out uninformative labels as the cause of classification head failure, pointing instead to the episode-to-step granularity mismatch as the bottleneck. Second, even when the labels reveal learnable routing patterns, the signal is too weak (8\,pp above random) and the decision boundary too unstable (30+\,pp internal recall variance) to yield end-to-end improvements over the unconditional deterministic baseline.

\subsection{Limitations}
\label{sec:limitations}

Our analysis is conducted on a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. ScienceWorld's severe $-100$ death penalty may amplify the death avoidance signal; environments with less catastrophic failure penalties could exhibit a lower DAF, though the qualitative finding---death avoidance as a major component of routing signal---may still hold. Our counterfactual labels operate at episode granularity; step-level labeling with denser reward signals is a natural extension that could improve both decomposition resolution and router training. The gap between logit-level and generation-level routing accuracy in the implicit router warrants further investigation.
