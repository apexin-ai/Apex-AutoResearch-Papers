# Related Work — Draft v2 (patched: MTRouter, EnvSimBench, DAF→90%)

\section{Related Work}

\paragraph{Tool-Use Learning.}
A line of work teaches LLMs when and how to invoke external tools.
Toolformer \cite{toolformer-2024} inserts API calls via self-supervised filtering, while ART \cite{art-2023} uses LLM reasoning chains to select tools automatically, and Chameleon \cite{chameleon-2024} composes diverse tool modules under LLM-as-planner orchestration.
More recently, ReTool \cite{retool-2026} applies reinforcement learning to learn implicit code-interpreter invocation strategies for mathematical reasoning.
Our work differs along three axes: (1) we generate routing labels via \emph{episode-level counterfactual analysis}---running complete trajectories under competing strategies---rather than self-supervised or RL-based signals; (2) we frame routing as \emph{catastrophic failure prevention} rather than general tool selection; and (3) we train an explicit lightweight router decoupled from the backbone LLM, enabling diagnostic analysis of what the routing signal encodes.

\paragraph{Adaptive Computation.}
Several recent methods adapt reasoning effort per step.
CogRouter \cite{cogrouter-2026} achieves 82.3\% on ScienceWorld by routing among cognitive depth levels (instinct to strategic planning) via Cooperative Policy Optimization, while ARES \cite{ares-2026} trains a lightweight router to select per-step reasoning effort (low/medium/high), reducing token cost by 52.7\%.
Mixture-of-Recursions \cite{mixture-of-recursions-2025} applies adaptive depth at the architecture level via per-token recursive routing.
MTRouter \cite{mtrouter-2026} routes among different LLMs to optimize cost-quality tradeoffs on ScienceWorld; in contrast, we route between \emph{computation modalities} (internal reasoning vs.\ deterministic computation) and focus on understanding what the routing signal encodes rather than optimizing cost.
These methods route \emph{how much} or \emph{which model} to reason with; we route \emph{which modality} to use and contribute the empirical finding that death avoidance accounts for ${\sim}90\%$ of the learned routing signal.

\paragraph{World Model Routing.}
ITP \cite{itp-2026} augments agents with LLM-based world model lookahead, adaptively adjusting the simulation horizon based on task progress.
Dyna-Think \cite{dynathink-2025} integrates world model simulation into the reasoning loop, matching 685B-parameter performance with a 32B model at half the token cost.
Both route to \emph{approximate} world models that inherit LLM hallucination failures.
EnvSimBench \cite{envsimbench-2026} demonstrates that LLMs catastrophically fail at multi-variable state transitions---a finding that provides the mechanistic basis for our observation that exact state transitions primarily prevent agent death rather than improving non-death task performance.
Our deterministic computation modality provides \emph{exact} state transitions, and our counterfactual analysis reveals that this exactness matters almost exclusively for death avoidance---non-death performance is near-equivalent between modalities.

\paragraph{Agent Frameworks.}
ReAct \cite{react-2023} interleaves reasoning and acting in a single LLM call and serves as a foundational framework for interactive agents including our internal-reasoning baseline.
Our work complements ReAct by analyzing \emph{when} reasoning should yield to deterministic computation and finding that the answer is concentrated in catastrophic failure scenarios.
