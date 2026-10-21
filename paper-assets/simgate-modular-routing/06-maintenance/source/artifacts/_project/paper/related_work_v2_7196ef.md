\section{Related Work}

\paragraph{Tool-Use Learning.}
A line of work teaches LLMs when and how to invoke external tools.
Toolformer \cite{toolformer-2024} inserts API calls via self-supervised filtering;
ART \cite{art-2023} delegates tool selection to LLM reasoning chains;
Chameleon \cite{chameleon-2024} composes diverse modules under LLM-as-planner orchestration;
and ReTool \cite{retool-2026} applies reinforcement learning to learn implicit code-interpreter invocation for mathematical reasoning.
These methods learn \emph{which tool} to use or \emph{whether} to use one, but do not analyze what signal drives the learned routing policy.
We differ in three ways: (1)~we generate labels via \emph{episode-level counterfactual analysis}---running complete trajectories under competing strategies---rather than self-supervised or RL signals; (2)~we frame routing as catastrophic-failure prevention rather than general tool selection; and (3)~by training an explicit lightweight router decoupled from the backbone, we can diagnose \emph{what} the routing signal encodes, revealing that ${\sim}90\%$ is death avoidance.

\paragraph{Adaptive Computation.}
Several recent methods adapt reasoning effort per step.
CogRouter \cite{cogrouter-2026} achieves state-of-the-art on ScienceWorld (82.3\%) by routing among cognitive depth levels via Cooperative Policy Optimization.
ARES \cite{ares-2026} trains a lightweight router to select per-step reasoning effort, reducing token cost by 52.7\%.
Mixture-of-Recursions \cite{mixture-of-recursions-2025} applies adaptive depth at the architecture level via per-token recursive routing.
These methods route \emph{how much} to reason; we route \emph{which modality} to use (internal LLM reasoning vs.\ deterministic computation).
More importantly, none quantify the composition of their routing signal.
Our counterfactual decomposition reveals that death avoidance accounts for ${\sim}90\%$ of the performance gap---the contribution is this empirical finding and the diagnostic methodology, not the router architecture itself.

\paragraph{World Model Routing.}
ITP \cite{itp-2026} augments agents with LLM-based world model lookahead, adaptively adjusting the simulation horizon based on task progress.
Dyna-Think \cite{dynathink-2025} integrates world model simulation into the reasoning loop, matching 685B-parameter performance with a 32B model at half the token cost.
Both route to \emph{approximate} world models that inherit LLM hallucination failures.
Our deterministic computation modality provides \emph{exact} state transitions, and episode-level counterfactual analysis reveals that this exactness matters almost exclusively for death avoidance: non-death performance is near-equivalent across modalities ($\Delta_\text{nd}$ accounts for only 9.6\% of the full gap).

\paragraph{Agent Frameworks.}
ReAct \cite{react-2023} interleaves reasoning and acting in a single LLM call and serves as a foundational framework for interactive agents, including our internal-reasoning baseline.
ScienceWorld \cite{scienceworld-2022} provides the evaluation environment: 30 science task types requiring multi-step reasoning over rule-governed state transitions with catastrophic failure penalties.
MTRouter \cite{mtrouter-2026} routes between different LLMs on ScienceWorld for cost optimization, but targets model-level selection rather than reasoning-modality selection.
Our work complements these efforts by asking a different question: not \emph{how} to build a better agent framework, but \emph{what} a learned router actually captures.
The answer---that routing signal is dominated by catastrophic-failure prevention---suggests that future agent designs should prioritize safety-aware computation allocation over general-purpose reasoning enhancement.
