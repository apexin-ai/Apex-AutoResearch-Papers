# Method — Draft v1

\section{Method}

We describe our methodology in four parts: counterfactual episode collection (\S\ref{sec:collection}), death-aware labeling (\S\ref{sec:labeling}), the death avoidance factor (\S\ref{sec:daf}), and a rule-based baseline analysis (\S\ref{sec:rule}).

\subsection{Counterfactual Episode Collection}
\label{sec:collection}

As motivated in \S1, per-step oracle labeling degenerates under sparse rewards. We instead adopt \emph{episode-level counterfactual analysis}: for each task instance, we run two complete episodes under identical initial conditions (same random seed):

\begin{itemize}
    \item \textbf{Pure-internal}: all steps use the LLM's internal reasoning following the ReAct paradigm \cite{react-2023}, where the agent interleaves chain-of-thought reasoning with environment actions.
    \item \textbf{Pure-deterministic}: all steps use deterministic external computation via the environment simulator, providing exact state transitions.
\end{itemize}

Each episode produces a tuple $(s^{\text{int}}, s^{\text{det}}, d^{\text{int}}, d^{\text{det}})$, where $s$ denotes episode score and $d \in \{0, 1\}$ indicates whether the agent died. Episodes are capped at [PLACEHOLDER: 30] steps. We use Qwen2.5-7B-Instruct as the LLM backbone, served via vLLM.

We evaluate on ScienceWorld \cite{scienceworld-2022}, which provides [PLACEHOLDER: 30] task types spanning physical and chemical reasoning. For each task type, we first run a prescreening phase (5 episodes) to identify tasks where both strategies can be meaningfully compared, then collect the full dataset of [PLACEHOLDER: 20] episodes per task. The final dataset comprises [PLACEHOLDER: 249] episodes across all [PLACEHOLDER: 30] task types.

\subsection{Death-Aware Labeling}
\label{sec:labeling}

We assign an episode-level routing label to each counterfactual pair based on the four-tuple $(s^{\text{int}}, s^{\text{det}}, d^{\text{int}}, d^{\text{det}})$, distinguishing four signal types ordered by priority:

\begin{enumerate}
    \item \textbf{Death asymmetry}: one strategy results in agent death while the other survives ($d^{\text{int}} \neq d^{\text{det}}$). The surviving strategy is labeled as preferred. This constitutes the strongest routing signal, as it reflects a catastrophic outcome difference rather than a marginal score gap.
    \item \textbf{Tied alive}: both strategies survive and their scores differ by at most a threshold $\tau$ ($|s^{\text{int}} - s^{\text{det}}| \leq \tau$, $d^{\text{int}} = d^{\text{det}} = 0$). Label: \texttt{no\_preference}.
    \item \textbf{Both dead}: both strategies result in death ($d^{\text{int}} = d^{\text{det}} = 1$). Label: \texttt{no\_preference}, as neither strategy provides a viable routing signal.
    \item \textbf{Score comparison}: both survive but scores differ beyond $\tau$ ($|s^{\text{int}} - s^{\text{det}}| > \tau$, $d^{\text{int}} = d^{\text{det}} = 0$). The higher-scoring strategy is preferred.
\end{enumerate}

The resulting label distribution across [PLACEHOLDER: 249] episodes is: [PLACEHOLDER: 41\%] \texttt{det\_preferred}, [PLACEHOLDER: 0.5\%] \texttt{internal\_preferred}, and [PLACEHOLDER: 59\%] \texttt{no\_preference}. The near-absence of \texttt{internal\_preferred} labels and the dominance of \texttt{det\_preferred} labels---driven overwhelmingly by death asymmetry---indicate that deterministic computation's primary advantage lies in avoiding catastrophic failures rather than achieving higher task scores.

\subsection{Death Avoidance Factor}
\label{sec:daf}

To quantify the contribution of death avoidance to routing signal, we define the \emph{Death Avoidance Factor} (DAF). Let $\Delta_{\text{full}}$ be the mean score gap between deterministic and internal strategies across all episodes, and $\Delta_{\text{no\_death}}$ be the same gap computed only over episodes where neither strategy results in death:
\begin{equation}
    \text{DAF} = 1 - \frac{\Delta_{\text{no\_death}}}{\Delta_{\text{full}}}
\end{equation}
DAF $= 1$ indicates that the routing signal is entirely attributable to death avoidance; DAF $= 0$ indicates it derives entirely from non-death performance differences.

Across the full dataset, [PLACEHOLDER: $\Delta_{\text{full}} = +37.9$] and [PLACEHOLDER: $\Delta_{\text{no\_death}} = +0.2$], yielding [PLACEHOLDER: DAF $= 0.99$]. Death avoidance accounts for virtually all of the observed routing advantage. Per-task analysis further confirms this: [PLACEHOLDER: 25] of [PLACEHOLDER: 30] tasks exhibit DAF $\geq 0.95$, while a small number of tasks show genuine non-death advantages (e.g., \texttt{measure-melting-point-unknown} with DAF $= 0.594$). The Pearson correlation between per-task death rate differential and score gap is [PLACEHOLDER: $r = 0.989$] ([PLACEHOLDER: $p < 0.0001$]), demonstrating that knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap.

\subsection{Rule-Based Baseline}
\label{sec:rule}

A natural question is whether simple heuristics can approximate learned routing. We test keyword-based rules that route to deterministic computation when the current action contains science-related verbs, under the hypothesis that actions involving physical or chemical state changes benefit most from exact computation.

We evaluate three keyword lists of decreasing breadth:
\begin{itemize}
    \item \textbf{v1} (20 generic verbs including \texttt{connect}, \texttt{move}): matches [PLACEHOLDER: 85.8\%] of actions, degenerating to an always-deterministic policy.
    \item \textbf{v2} (17 science-specific: \texttt{heat}, \texttt{boil}, \texttt{melt}, \texttt{freeze}): matches [PLACEHOLDER: 4.9\%], degenerating to always-internal.
    \item \textbf{v3} (12 state-change verbs): matches [PLACEHOLDER: 2.8\%], similarly degenerating.
\end{itemize}

The structural cause is that ScienceWorld actions use generic interaction verbs (\texttt{pick up}, \texttt{move}, \texttt{connect}) rather than science-specific terms, making keyword overlap with the underlying task semantics either near-total or negligible. No keyword granularity provides meaningful routing discrimination, motivating observation-based or learned routing approaches.
