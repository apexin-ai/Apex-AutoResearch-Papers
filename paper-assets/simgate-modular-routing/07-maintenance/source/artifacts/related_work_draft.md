# Related Work — Draft v2
<!-- ReAct citation moved to Introduction to free space (short paper ~400 word budget) -->

\section{Related Work}

\paragraph{Tool-Use Learning.}
A line of work teaches LLMs when and how to invoke external tools.
Toolformer \cite{toolformer-2024} inserts API calls via self-supervised filtering, ART \cite{art-2023} uses LLM reasoning chains to select tools automatically, and Chameleon \cite{chameleon-2024} composes diverse tool modules under LLM-as-planner orchestration.
ReTool \cite{retool-2026} applies reinforcement learning to learn implicit code-interpreter invocation strategies for mathematical reasoning.
Concurrently, MTRouter \cite{mtrouter-2026} routes between different LLMs on ScienceWorld for cost-quality tradeoff; unlike our work, it selects \emph{which model} to call rather than \emph{which reasoning modality} to use, and does not analyze routing signal composition.
Our routing labels come from \emph{episode-level counterfactual analysis}---complete trajectories under competing strategies---and frame routing as catastrophic failure prevention rather than tool selection or cost optimization.

\paragraph{Adaptive Computation.}
Several recent methods adapt reasoning effort per step.
CogRouter \cite{cogrouter-2026} achieves 82.3\% on ScienceWorld by routing among cognitive depth levels (instinct to strategic planning) via Cooperative Policy Optimization, while ARES \cite{ares-2026} trains a lightweight router to select per-step reasoning effort (low/medium/high), reducing token cost by 52.7\%.
Mixture-of-Recursions \cite{mixture-of-recursions-2025} applies adaptive depth at the architecture level via per-token recursive routing.
These methods route \emph{how much} to reason; we route \emph{which modality} to use (internal LLM reasoning vs.\ deterministic computation) and contribute the empirical finding that death avoidance accounts for ${\sim}99\%$ of the learned routing signal.

\paragraph{World Model Routing and Environment Simulation.}
ITP \cite{itp-2026} augments agents with LLM-based world model lookahead, adaptively adjusting the simulation horizon based on task progress.
Dyna-Think \cite{dynathink-2025} integrates world model simulation into the reasoning loop, matching 685B-parameter performance with a 32B model at half the token cost.
Both route to \emph{approximate} world models that inherit LLM hallucination failures.
EnvSimBench \cite{envsimbench-2025} diagnoses a related limitation: LLMs exhibit a ``state-change cliff,'' failing catastrophically when multiple state variables require simultaneous updates.
Our deterministic computation modality sidesteps this cliff by providing \emph{exact} state transitions, and our counterfactual analysis reveals that this exactness matters almost exclusively for death avoidance.

\paragraph{Agent Failure Analysis.}
\citet{llm-agentic-failures-2025} qualitatively identify four failure archetypes in agentic LLM scenarios; our counterfactual methodology complements this by quantitatively isolating the dominant failure mechanism---death avoidance accounts for ${\sim}99\%$ of the routing signal on ScienceWorld.
