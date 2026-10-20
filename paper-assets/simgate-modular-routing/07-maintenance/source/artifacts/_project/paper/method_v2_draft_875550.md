# Method Section — Draft v2 (A-Source: plan-012-full, 11 tasks / 245 episodes)

\section{Method}

\subsection{Counterfactual Episode Collection}
\label{sec:collection}

Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \cite{scienceworld-2022}, 98.2\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.

For each task instance, we execute two complete episodes under identical initial conditions (same random seed, same task variation). The \emph{pure-internal} episode follows the ReAct paradigm \cite{react-2023}, where the LLM interleaves chain-of-thought reasoning with environment actions. The \emph{pure-deterministic} episode uses the environment simulator to compute exact state transitions for each action. In both cases the LLM selects which action to take; deterministic computation replaces only the state-transition prediction, not action selection---equivalent to giving the agent access to a perfect world model.

Each episode pair produces a tuple $(s^{\text{int}}, s^{\text{det}}, d^{\text{int}}, d^{\text{det}})$, where $s$ denotes the terminal score and $d \in \{0,1\}$ indicates agent death. Episodes are capped at 30 steps. The LLM backbone is Qwen2.5-7B-Instruct served via vLLM. We evaluate on ScienceWorld \cite{scienceworld-2022}, which spans 30 task types covering physical and chemical reasoning with a $-100$ penalty upon agent death. After prescreening (5 episodes per type for signal estimation), we perform targeted full collection on 11 task types, yielding 245 episode pairs (20--40 per type).

\subsection{Death-Aware Labeling}
\label{sec:labeling}

Each counterfactual pair receives an episode-level routing label based on $(s^{\text{int}}, s^{\text{det}}, d^{\text{int}}, d^{\text{det}})$. ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. The label is assigned by one of four mutually exclusive cases:

\begin{enumerate}
    \item \textbf{Death asymmetry}: $d^{\text{int}} \neq d^{\text{det}}$ $\rightarrow$ the surviving strategy is preferred.
    \item \textbf{Both dead}: $d^{\text{int}} = d^{\text{det}} = 1$ $\rightarrow$ \texttt{no\_preference}.
    \item \textbf{Score comparison}: both survive and $s^{\text{det}} \neq s^{\text{int}}$ $\rightarrow$ the higher-scoring strategy is preferred.
    \item \textbf{Tied alive}: both survive and $s^{\text{det}} = s^{\text{int}}$ $\rightarrow$ \texttt{no\_preference}.
\end{enumerate}

Across 245 episodes, this yields 86 (35.1\%) \texttt{det\_preferred}, 9 (3.7\%) \texttt{internal\_preferred}, and 150 (61.2\%) \texttt{no\_preference}. The near-absence of \texttt{internal\_preferred} labels combined with the dominance of \texttt{no\_preference} indicates that the deterministic strategy's advantage is concentrated in death avoidance rather than superior task performance when both agents survive.

\subsection{Death Avoidance Factor}
\label{sec:daf}

To quantify the contribution of death avoidance to routing signal, we define the Death Avoidance Factor (DAF):
\begin{equation}
    \text{DAF} = 1 - \frac{\Delta_{\text{no\_death}}}{\Delta_{\text{full}}}
\end{equation}
where $\Delta_{\text{full}}$ is the mean score gap ($s^{\text{det}} - s^{\text{int}}$) across all episodes and $\Delta_{\text{no\_death}}$ is the same gap restricted to episodes where neither strategy results in death. DAF $= 1$ indicates all routing signal stems from death avoidance; DAF $= 0$ indicates all signal stems from non-death performance differences. When $\Delta_{\text{full}} = 0$, DAF is undefined, as no routing signal exists to decompose; we report DAF only for task types where $|\Delta_{\text{full}}| > 0$.

On 245 episodes across 11 task types: $\Delta_{\text{full}} = +29.60$, $\Delta_{\text{no\_death}} = +2.84$, yielding DAF $= 90.41\%$. The cross-task consistency is strong: the Pearson correlation between per-task death rate differential (internal minus deterministic) and $\Delta_{\text{full}}$ is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$) across 11 task types, indicating that knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap.

\subsection{Rule-Based Baseline}
\label{sec:rule}

As a simple routing heuristic, we test keyword-based rules that route to deterministic computation when the action contains science-related verbs. We evaluate three keyword lists of decreasing breadth:

\begin{itemize}
    \item \textbf{v1} (20 generic verbs including \emph{connect}, \emph{move}): matches 85.8\% of actions, degenerating to always-deterministic.
    \item \textbf{v2} (17 science-specific verbs: \emph{heat}, \emph{boil}, \emph{melt}, \emph{freeze}, \ldots): matches 4.9\%, degenerating to always-internal.
    \item \textbf{v3} (12 state-change verbs): matches 2.8\%, degenerating to always-internal.
\end{itemize}

The structural cause is that ScienceWorld actions use generic interaction verbs (\texttt{pick up}, \texttt{move}, \texttt{connect}) rather than science-specific terms. No keyword granularity bridges the gap between near-total and negligible match rates, precluding meaningful routing discrimination. This structural failure motivates observation-based approaches that use environment observations and agent state as routing features rather than action keywords.
