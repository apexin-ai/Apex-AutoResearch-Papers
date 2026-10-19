# paper writing

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/workers/worker_paper_writing_20260518T120618.log`
- **Structured JSON:** [`c1d2719ffee649bb01a7.json`](../../sessions/c1/c1d2719ffee649bb01a7.json)

## Before a recorded user message

41 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__bootstrap_provenance",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__overleaf_init",
    "mcp__agent-ml-research__overleaf_pull",
    "mcp__agent-ml-research__overleaf_push",
    "mcp__agent-ml-research__overleaf_status",
    "mcp__agent-ml-research__overleaf_sync",
    "mcp__agent-ml-research__paper_agent_post_to_director",
    "mcp__agent-ml-research__paper_agent_request_review",
    "mcp__agent-ml-research__paper_compile_and_check",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "d43448fd-56ae-42c6-8109-33afff746997",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779106200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "07ba0b78-5b1b-4037-8509-a0a984b1c92b",
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the required files to understand the writing norms and the current method.tex file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "921e4a8b-9828-4c87-a537-405194e14180",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UB4aUZ9JSK4PSy6v19N3Pr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14873,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14873
      },
      "output_tokens": 45,
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

_source line 5_

I'll read the required files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "90984d3e-c59d-4eb5-a430-0f0f4726c276",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UB4aUZ9JSK4PSy6v19N3Pr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14873,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14873
      },
      "output_tokens": 45,
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_019XubKUbZpMvPT368ng1dCk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "22822a79-9b1e-4fb1-b17c-dc39aa25ca48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UB4aUZ9JSK4PSy6v19N3Pr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14873,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14873
      },
      "output_tokens": 45,
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

_source line 7 · 2026-05-18T12:06:31.700Z_

<details><summary>↩ Tool result · `toolu_019XubKUbZpMvPT368ng1dCk`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:problem_formulation}
6	
7	We formalize the multi-turn interactive agent as a Partially Observable Markov Decision Process (POMDP) $\mathcal{M} = (\mathcal{S}, \mathcal{A}, \mathcal{O}, P, \Omega, R, \gamma)$, where $\mathcal{S}$ is the state space of the environment, $\mathcal{A}$ is the action space (natural language commands), $\mathcal{O}$ is the observation space (textual feedback from the environment), $P: \mathcal{S} \times \mathcal{A} \rightarrow \mathcal{S}$ is the transition function, $\Omega: \mathcal{S} \rightarrow \mathcal{O}$ is the observation function, $R$ is the reward function, and $\gamma \in [0,1]$ is a discount factor. The agent policy $\pi_\phi(a_t \mid h_t)$ generates actions conditioned on the interaction history $h_t = (o_1, a_1, o_2, a_2, \ldots, o_t)$, where $\phi$ denotes the policy parameters. An episode consists of $T$ interaction steps, terminating with a binary reward $R \in \{0, r_+\}$ that indicates task success or failure.
8	
9	In practice, multi-turn episodes can span 50 or more interaction steps, each containing hundreds of tokens. Training a language model policy on the full history $h_T$ is computationally expensive and often exceeds the model's context length. This motivates the \textbf{step-independent windowing} approach: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, and each window is optimized independently with its own computed return. Concretely, window $k$ observes only $(o_{(k-1)h+1}, a_{(k-1)h+1}, \ldots, o_{kh})$ and receives a return $R_k$ derived from the episode outcome. This decomposition treats each window as a separate training sample, allowing standard context-length models to process the data. We show below that this seemingly practical choice introduces two failure mechanisms that cause catastrophic training collapse.
10	
11	\subsection{GRPO for Language Agents}
12	\label{sec:grpo}
13	
14	Group Relative Policy Optimization (GRPO)~\cite{shao2024deepseekmath} is a bandit-style policy gradient method designed for language model alignment. Unlike PPO~\cite{schulman2017ppo}, GRPO requires no critic network. For each task instance $x$, the algorithm samples $K$ rollouts $\{y_1, \ldots, y_K\}$ from the current policy $\pi_\phi$. The advantage of each rollout is computed relative to the group:
15	\begin{equation}
16	\hat{A}_k = \frac{R_k - \mu}{\sigma + \epsilon}, \quad \mu = \frac{1}{K}\sum_{j=1}^K R_j, \quad \sigma = \sqrt{\frac{1}{K}\sum_{j=1}^K (R_j - \mu)^2}
17	\label{eq:grpo_advantage}
18	\end{equation}
19	where $R_k$ is the return of rollout $k$. The policy gradient is:
20	\begin{equation}
21	\mathcal{L}_{\text{GRPO}} = -\frac{1}{K}\sum_{k=1}^K \hat{A}_k \cdot \min\left(\rho_k, \text{clip}(\rho_k, 1\pm\epsilon_c)\right) + \beta \cdot D_{\text{KL}}[\pi_\phi \| \pi_{\text{ref}}]
22	\label{eq:grpo_loss}
23	\end{equation}
24	where $\rho_k = \pi_\phi(y_k \mid x) / \pi_{\text{old}}(y_k \mid x)$ is the importance ratio and $\beta$ controls the KL penalty against a reference policy $\pi_{\text{ref}}$. GRPO is \textit{episode-level by design}: each rollout $y_k$ is a complete generation with a single return $R_k$ and a single advantage $\hat{A}_k$. There is no inherent temporal discounting within the algorithm.
25	
26	\subsection{Step-Independent Implementation in Multi-Turn Agents}
27	\label{sec:step_independent}
28	
29	When adapting GRPO for multi-turn interactive tasks, agent training frameworks face a mismatch between GRPO's episode-level design and the practical constraints of long trajectories. The RAGEN framework~\cite{ragen2025} addresses this by introducing step-independent training: each $h$-step window becomes an independent GRPO sample with a discounted return derived from the episode outcome.
30	
31	Specifically, for an episode of $T$ steps with binary outcome $R_{\text{episode}} \in \{0, r_+\}$, the return assigned to window $k$ (covering steps $(k-1)h+1$ through $kh$) is computed as:
32	\begin{equation}
33	R_k = \gamma^{(N - k)} \cdot R_{\text{episode}}
34	\label{eq:step_return}
35	\end{equation}
36	where $N = \lceil T/h \rceil$ is the total number of windows in the episode and $\gamma$ is a discount factor (typically 0.95). In practice, intermediate step penalties (e.g., invalid action penalties) contribute additional terms to $R_k$. Our analysis focuses on the dominant component: the discounted terminal reward. Section~\ref{sec:sign_verification} empirically validates that advantage sign remains episode-outcome-dominated even in the presence of per-step penalties. Each window is then treated as an independent sample in the GRPO optimization and receives its own group-normalized advantage $\hat{A}_k$ via Equation~\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $N$.
37	
38	This design choice is motivated by three practical constraints. First, full trajectories of 50+ turns with hundreds of tokens per turn exceed typical context length limits (2048 or 4096 tokens for smaller models). Second, treating each window independently multiplies the effective batch size, improving GPU utilization. Third, the framework inherits the token-level training paradigm common in language model optimization, where shorter sequences are the default.\footnote{Implementation details are available in the open-source RAGEN codebase, specifically the step-discounted return computation module (\texttt{compute\_step\_discounted\_returns}).}
39	
40	Despite these practical motivations, step-independent training fundamentally alters the credit assignment structure. The following section analyzes two mechanisms through which this alteration causes training collapse.
41	
42	\subsection{Dual Mechanism Analysis}
43	\label{sec:dual_mechanism}
44	
45	We identify two mechanisms operating at different layers that jointly cause catastrophic failure under step-independent training. The first operates at the inference layer, establishing a structural performance ceiling by restricting the model's observable context. The second operates at the training layer, actively degrading performance below this ceiling through systematic gradient errors that accumulate over optimization steps. We predict a two-phase collapse under step-independent training: strategic failure (task success drops) while action formatting initially remains intact, followed by complete collapse of both capabilities as wrong-direction gradients accumulate. Section~\ref{sec:experiments} validates this prediction empirically.
46	
47	\subsubsection{Mechanism 1: Policy Information Loss}
48	\label{sec:m1_information_loss}
49	
50	Step-independent training truncates context at both the inference and training layers. At inference time, the policy $\pi_\phi(a_t \mid h_{\text{window}_k})$ generates actions conditioned on only the local $h$-step history, losing access to observations and actions from earlier windows. At the training layer, the optimization target for each window is computed from this same truncated context, so cross-step strategies that require conditioning on earlier outcomes cannot be reinforced. Consider a household task requiring the agent to first explore a drawer (step 3), discover an object's location (step 4), then navigate to a countertop (step 8). With $h=2$, the window containing step 8 has no access to the exploration outcome from steps 3--4, neither at inference (the model cannot condition on it) nor at training (the gradient cannot credit it). The policy cannot learn the conditional strategy ``go to countertop \textit{only if} the object was found in the drawer.''
51	
52	This information loss establishes a structural performance ceiling that is constant across training: it reflects an architectural constraint on the representable strategy space rather than a learned failure. Different window sizes $h$ produce different ceilings, with smaller $h$ imposing tighter constraints on achievable task success. In our h-sweep experiments (Section~\ref{sec:experiments}), initial evaluation performance varies across window sizes, confirming that the ceiling depends on the amount of available context.
53	
54	More formally, let $\pi^*$ denote the optimal policy for the full POMDP. The mutual information between $\pi^*$ and the full history, $I(\pi^*; h_T)$, captures the total information required for optimal decision-making. Under $h$-step windowing, each window's policy can access at most $I(\pi^*; h_{\text{window}_k})$. For tasks with sequential dependencies spanning more than $h$ steps, we have $I(\pi^*; h_T) \gg I(\pi^*; h_{\text{window}_k})$. The information gap grows with episode length $T$ and shrinks with window size $h$, predicting a performance cliff as $h$ decreases relative to the task's dependency horizon.
55	
56	\subsubsection{Mechanism 2: Advantage Sign Misattribution}
57	\label{sec:m2_sign_misattribution}
58	
59	The second mechanism operates at the training layer and, unlike Mechanism 1, is cumulative: its damage increases with each optimization step. Under step-independent training, each window receives a return $R_k = \gamma^{(N-k)} \cdot R_{\text{episode}}$ (Equation~\ref{eq:step_return}). After group normalization, the advantage $\hat{A}_k$ has a \textit{sign} determined primarily by whether the episode succeeded or failed, not by whether window $k$'s actions were locally good or bad.
60	
61	In a failed episode ($R_{\text{episode}} = 0$), all windows receive $R_k = 0$. If the group mean $\mu > 0$ (due to other successful rollouts in the group), all windows in the failed episode receive negative advantages. This includes windows where the agent took locally correct actions (e.g., correctly identifying a target object). Conversely, in a successful episode, all windows receive positive advantages, including windows where the agent took suboptimal actions (e.g., unnecessary exploration steps that happened not to prevent eventual success).
62	
63	The gradient direction for each window is determined by the sign of $\hat{A}_k$:
64	\begin{equation}
65	\text{sign}(\hat{A}_k) \approx \text{sign}(R_{\text{episode}} - \mu)
66	\label{eq:sign_correlation}
67	\end{equation}
68	This means the optimization either reinforces or suppresses \textit{all} actions within a window based on the episode outcome, regardless of local action quality. Good actions in failed episodes are actively suppressed; bad actions in successful episodes are actively reinforced. Over many training steps, this systematic misattribution progressively erodes whatever inference capability the model retains under the truncated context. Even when the policy begins with non-trivial task competence within its $h$-step window, repeated wrong-sign gradient updates suppress this competence. Mechanism 2 should produce observable degradation below the ceiling set by Mechanism 1, with the rate of degradation proportional to the severity of sign misattribution. Section~\ref{sec:experiments} confirms this prediction.
69	
70	A secondary effect compounds this problem. The discount factor $\gamma^{(N-k)}$ introduces magnitude decay across window positions. For early windows in a long episode ($T=50$, $h=2$, $\gamma=0.95$), the first window ($k=1$) retains $\gamma^{N-1} = \gamma^{24} \approx 0.29$ of the terminal window's return. While this reduces the learning signal for early decisions, the sign error is fundamentally more harmful: magnitude decay merely slows convergence, while sign misattribution causes active divergence (Section~\ref{sec:sign_fundamental}).
71	
72	\subsection{Episode-Level Training}
73	\label{sec:episode_level}
74	
75	Episode-level training resolves both failure mechanisms by treating the complete trajectory as a single GRPO sample. All tokens across all $T$ steps share one advantage $\hat{A}$, computed from the episode return $R_{\text{episode}}$ via group normalization over $K$ complete rollouts of the same task instance.
76	
77	This design directly addresses Mechanism 1. The policy $\pi_\phi(a_t \mid h_t)$ conditions on the full interaction history $h_t$ at every step $t$. Cross-step dependencies are preserved in the optimization target: the gradient for generating action $a_8$ (navigate to countertop) flows through the complete history including observations from steps 3--4 (drawer exploration outcome).
78	
79	Episode-level training also eliminates Mechanism 2. Because there is no window-level return assignment, there is no opportunity for sign misattribution between windows. The single advantage $\hat{A}$ applies uniformly to the entire trajectory. While this means per-step credit assignment remains coarse (all steps in a successful episode are equally reinforced), it avoids the worse failure mode of \textit{systematically incorrect} credit assignment. The distinction is critical: uniform reinforcement of a successful trajectory preserves good sub-strategies within it, whereas window-level sign errors actively destroy them.
80	
81	The trade-off is computational. Episode-level training requires processing the full sequence length ($T$ steps $\times$ tokens-per-step) in a single forward and backward pass. For $T=50$ and 100 tokens per step, this amounts to 5000-token sequences, which fits within the capacity of modern architectures but increases memory and compute relative to $h$-step windows. In our experiments (Section~\ref{sec:experiments}), this overhead is modest compared to the catastrophic failure avoided.
82	
83	Episode-level training is, in fact, the natural application of GRPO to multi-turn settings. GRPO was designed as an episode-level algorithm where each rollout receives one return and one advantage. Step-independent training is the deviation from this design, introduced by framework implementation choices rather than algorithmic motivation. Our analysis reveals that this deviation carries hidden costs that become catastrophic for long-horizon interactive tasks.
84	
85	\subsection{Selective Verification via Action-Change Reward}
86	\label{sec:selective_verification}
87	
88	The credit assignment analysis above focuses on training a competent base agent. We outline here a proposed design for a downstream application: selective verification. This component has not been implemented in the current work and is intended as a direction for future investigation.
89	
90	Interactive agents benefit from self-verification (re-evaluating their planned action before execution), but empirical analysis shows that over 90\% of verification instances are confirmatory (the agent does not change its action after checking)~\cite{long2026selfverification}. Training the agent to verify selectively, only when verification is likely to be informative, could reduce computational cost without sacrificing task performance.
91	
92	We formulate selective verification as a binary decision at each step $t$: the agent outputs a verify token $v_t \in \{\texttt{VERIFY}, \texttt{SKIP}\}$ before generating its action $a_t$. When $v_t = \texttt{VERIFY}$, the agent generates a verification rationale and may revise its action; when $v_t = \texttt{SKIP}$, the agent proceeds directly. The reward signal for training the verification policy uses the action-change indicator:
93	\begin{equation}
94	\Delta a_t = \mathbb{1}[a_t^{\text{post-verify}} \neq a_t^{\text{pre-verify}}]
95	\label{eq:action_change}
96	\end{equation}
97	as a measure of verification informativeness. A verification step that changes the action provided useful corrective information; one that confirms the original action was uninformative for that instance. The full formulation of the verification reward and training procedure is presented in Section~\ref{sec:selective_experiments}. Episode-level training serves as a prerequisite for this component: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "53cb8839-7782-43f9-ab08-33c87184b379",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:problem_formulation}\n\nWe formalize the multi-turn interactive agent as a Partially Observable Markov Decision Process (POMDP) $\\mathcal{M} = (\\mathcal{S}, \\mathcal{A}, \\mathcal{O}, P, \\Omega, R, \\gamma)$, where $\\mathcal{S}$ is the state space of the environment, $\\mathcal{A}$ is the action space (natural language commands), $\\mathcal{O}$ is the observation space (textual feedback from the environment), $P: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathcal{S}$ is the transition function, $\\Omega: \\mathcal{S} \\rightarrow \\mathcal{O}$ is the observation function, $R$ is the reward function, and $\\gamma \\in [0,1]$ is a discount factor. The agent policy $\\pi_\\phi(a_t \\mid h_t)$ generates actions conditioned on the interaction history $h_t = (o_1, a_1, o_2, a_2, \\ldots, o_t)$, where $\\phi$ denotes the policy parameters. An episode consists of $T$ interaction steps, terminating with a binary reward $R \\in \\{0, r_+\\}$ that indicates task success or failure.\n\nIn practice, multi-turn episodes can span 50 or more interaction steps, each containing hundreds of tokens. Training a language model policy on the full history $h_T$ is computationally expensive and often exceeds the model's context length. This motivates the \\textbf{step-independent windowing} approach: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, and each window is optimized independently with its own computed return. Concretely, window $k$ observes only $(o_{(k-1)h+1}, a_{(k-1)h+1}, \\ldots, o_{kh})$ and receives a return $R_k$ derived from the episode outcome. This decomposition treats each window as a separate training sample, allowing standard context-length models to process the data. We show below that this seemingly practical choice introduces two failure mechanisms that cause catastrophic training collapse.\n\n\\subsection{GRPO for Language Agents}\n\\label{sec:grpo}\n\nGroup Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} is a bandit-style policy gradient method designed for language model alignment. Unlike PPO~\\cite{schulman2017ppo}, GRPO requires no critic network. For each task instance $x$, the algorithm samples $K$ rollouts $\\{y_1, \\ldots, y_K\\}$ from the current policy $\\pi_\\phi$. The advantage of each rollout is computed relative to the group:\n\\begin{equation}\n\\hat{A}_k = \\frac{R_k - \\mu}{\\sigma + \\epsilon}, \\quad \\mu = \\frac{1}{K}\\sum_{j=1}^K R_j, \\quad \\sigma = \\sqrt{\\frac{1}{K}\\sum_{j=1}^K (R_j - \\mu)^2}\n\\label{eq:grpo_advantage}\n\\end{equation}\nwhere $R_k$ is the return of rollout $k$. The policy gradient is:\n\\begin{equation}\n\\mathcal{L}_{\\text{GRPO}} = -\\frac{1}{K}\\sum_{k=1}^K \\hat{A}_k \\cdot \\min\\left(\\rho_k, \\text{clip}(\\rho_k, 1\\pm\\epsilon_c)\\right) + \\beta \\cdot D_{\\text{KL}}[\\pi_\\phi \\| \\pi_{\\text{ref}}]\n\\label{eq:grpo_loss}\n\\end{equation}\nwhere $\\rho_k = \\pi_\\phi(y_k \\mid x) / \\pi_{\\text{old}}(y_k \\mid x)$ is the importance ratio and $\\beta$ controls the KL penalty against a reference policy $\\pi_{\\text{ref}}$. GRPO is \\textit{episode-level by design}: each rollout $y_k$ is a complete generation with a single return $R_k$ and a single advantage $\\hat{A}_k$. There is no inherent temporal discounting within the algorithm.\n\n\\subsection{Step-Independent Implementation in Multi-Turn Agents}\n\\label{sec:step_independent}\n\nWhen adapting GRPO for multi-turn interactive tasks, agent training frameworks face a mismatch between GRPO's episode-level design and the practical constraints of long trajectories. The RAGEN framework~\\cite{ragen2025} addresses this by introducing step-independent training: each $h$-step window becomes an independent GRPO sample with a discounted return derived from the episode outcome.\n\nSpecifically, for an episode of $T$ steps with binary outcome $R_{\\text{episode}} \\in \\{0, r_+\\}$, the return assigned to window $k$ (covering steps $(k-1)h+1$ through $kh$) is computed as:\n\\begin{equation}\nR_k = \\gamma^{(N - k)} \\cdot R_{\\text{episode}}\n\\label{eq:step_return}\n\\end{equation}\nwhere $N = \\lceil T/h \\rceil$ is the total number of windows in the episode and $\\gamma$ is a discount factor (typically 0.95). In practice, intermediate step penalties (e.g., invalid action penalties) contribute additional terms to $R_k$. Our analysis focuses on the dominant component: the discounted terminal reward. Section~\\ref{sec:sign_verification} empirically validates that advantage sign remains episode-outcome-dominated even in the presence of per-step penalties. Each window is then treated as an independent sample in the GRPO optimization and receives its own group-normalized advantage $\\hat{A}_k$ via Equation~\\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $N$.\n\nThis design choice is motivated by three practical constraints. First, full trajectories of 50+ turns with hundreds of tokens per turn exceed typical context length limits (2048 or 4096 tokens for smaller models). Second, treating each window independently multiplies the effective batch size, improving GPU utilization. Third, the framework inherits the token-level training paradigm common in language model optimization, where shorter sequences are the default.\\footnote{Implementation details are available in the open-source RAGEN codebase, specifically the step-discounted return computation module (\\texttt{compute\\_step\\_discounted\\_returns}).}\n\nDespite these practical motivations, step-independent training fundamentally alters the credit assignment structure. The following section analyzes two mechanisms through which this alteration causes training collapse.\n\n\\subsection{Dual Mechanism Analysis}\n\\label{sec:dual_mechanism}\n\nWe identify two mechanisms operating at different layers that jointly cause catastrophic failure under step-independent training. The first operates at the inference layer, establishing a structural performance ceiling by restricting the model's observable context. The second operates at the training layer, actively degrading performance below this ceiling through systematic gradient errors that accumulate over optimization steps. We predict a two-phase collapse under step-independent training: strategic failure (task success drops) while action formatting initially remains intact, followed by complete collapse of both capabilities as wrong-direction gradients accumulate. Section~\\ref{sec:experiments} validates this prediction empirically.\n\n\\subsubsection{Mechanism 1: Policy Information Loss}\n\\label{sec:m1_information_loss}\n\nStep-independent training truncates context at both the inference and training layers. At inference time, the policy $\\pi_\\phi(a_t \\mid h_{\\text{window}_k})$ generates actions conditioned on only the local $h$-step history, losing access to observations and actions from earlier windows. At the training layer, the optimization target for each window is computed from this same truncated context, so cross-step strategies that require conditioning on earlier outcomes cannot be reinforced. Consider a household task requiring the agent to first explore a drawer (step 3), discover an object's location (step 4), then navigate to a countertop (step 8). With $h=2$, the window containing step 8 has no access to the exploration outcome from steps 3--4, neither at inference (the model cannot condition on it) nor at training (the gradient cannot credit it). The policy cannot learn the conditional strategy ``go to countertop \\textit{only if} the object was found in the drawer.''\n\nThis information loss establishes a structural performance ceiling that is constant across training: it reflects an architectural constraint on the representable strategy space rather than a learned failure. Different window sizes $h$ produce different ceilings, with smaller $h$ imposing tighter constraints on achievable task success. In our h-sweep experiments (Section~\\ref{sec:experiments}), initial evaluation performance varies across window sizes, confirming that the ceiling depends on the amount of available context.\n\nMore formally, let $\\pi^*$ denote the optimal policy for the full POMDP. The mutual information between $\\pi^*$ and the full history, $I(\\pi^*; h_T)$, captures the total information required for optimal decision-making. Under $h$-step windowing, each window's policy can access at most $I(\\pi^*; h_{\\text{window}_k})$. For tasks with sequential dependencies spanning more than $h$ steps, we have $I(\\pi^*; h_T) \\gg I(\\pi^*; h_{\\text{window}_k})$. The information gap grows with episode length $T$ and shrinks with window size $h$, predicting a performance cliff as $h$ decreases relative to the task's dependency horizon.\n\n\\subsubsection{Mechanism 2: Advantage Sign Misattribution}\n\\label{sec:m2_sign_misattribution}\n\nThe second mechanism operates at the training layer and, unlike Mechanism 1, is cumulative: its damage increases with each optimization step. Under step-independent training, each window receives a return $R_k = \\gamma^{(N-k)} \\cdot R_{\\text{episode}}$ (Equation~\\ref{eq:step_return}). After group normalization, the advantage $\\hat{A}_k$ has a \\textit{sign} determined primarily by whether the episode succeeded or failed, not by whether window $k$'s actions were locally good or bad.\n\nIn a failed episode ($R_{\\text{episode}} = 0$), all windows receive $R_k = 0$. If the group mean $\\mu > 0$ (due to other successful rollouts in the group), all windows in the failed episode receive negative advantages. This includes windows where the agent took locally correct actions (e.g., correctly identifying a target object). Conversely, in a successful episode, all windows receive positive advantages, including windows where the agent took suboptimal actions (e.g., unnecessary exploration steps that happened not to prevent eventual success).\n\nThe gradient direction for each window is determined by the sign of $\\hat{A}_k$:\n\\begin{equation}\n\\text{sign}(\\hat{A}_k) \\approx \\text{sign}(R_{\\text{episode}} - \\mu)\n\\label{eq:sign_correlation}\n\\end{equation}\nThis means the optimization either reinforces or suppresses \\textit{all} actions within a window based on the episode outcome, regardless of local action quality. Good actions in failed episodes are actively suppressed; bad actions in successful episodes are actively reinforced. Over many training steps, this systematic misattribution progressively erodes whatever inference capability the model retains under the truncated context. Even when the policy begins with non-trivial task competence within its $h$-step window, repeated wrong-sign gradient updates suppress this competence. Mechanism 2 should produce observable degradation below the ceiling set by Mechanism 1, with the rate of degradation proportional to the severity of sign misattribution. Section~\\ref{sec:experiments} confirms this prediction.\n\nA secondary effect compounds this problem. The discount factor $\\gamma^{(N-k)}$ introduces magnitude decay across window positions. For early windows in a long episode ($T=50$, $h=2$, $\\gamma=0.95$), the first window ($k=1$) retains $\\gamma^{N-1} = \\gamma^{24} \\approx 0.29$ of the terminal window's return. While this reduces the learning signal for early decisions, the sign error is fundamentally more harmful: magnitude decay merely slows convergence, while sign misattribution causes active divergence (Section~\\ref{sec:sign_fundamental}).\n\n\\subsection{Episode-Level Training}\n\\label{sec:episode_level}\n\nEpisode-level training resolves both failure mechanisms by treating the complete trajectory as a single GRPO sample. All tokens across all $T$ steps share one advantage $\\hat{A}$, computed from the episode return $R_{\\text{episode}}$ via group normalization over $K$ complete rollouts of the same task instance.\n\nThis design directly addresses Mechanism 1. The policy $\\pi_\\phi(a_t \\mid h_t)$ conditions on the full interaction history $h_t$ at every step $t$. Cross-step dependencies are preserved in the optimization target: the gradient for generating action $a_8$ (navigate to countertop) flows through the complete history including observations from steps 3--4 (drawer exploration outcome).\n\nEpisode-level training also eliminates Mechanism 2. Because there is no window-level return assignment, there is no opportunity for sign misattribution between windows. The single advantage $\\hat{A}$ applies uniformly to the entire trajectory. While this means per-step credit assignment remains coarse (all steps in a successful episode are equally reinforced), it avoids the worse failure mode of \\textit{systematically incorrect} credit assignment. The distinction is critical: uniform reinforcement of a successful trajectory preserves good sub-strategies within it, whereas window-level sign errors actively destroy them.\n\nThe trade-off is computational. Episode-level training requires processing the full sequence length ($T$ steps $\\times$ tokens-per-step) in a single forward and backward pass. For $T=50$ and 100 tokens per step, this amounts to 5000-token sequences, which fits within the capacity of modern architectures but increases memory and compute relative to $h$-step windows. In our experiments (Section~\\ref{sec:experiments}), this overhead is modest compared to the catastrophic failure avoided.\n\nEpisode-level training is, in fact, the natural application of GRPO to multi-turn settings. GRPO was designed as an episode-level algorithm where each rollout receives one return and one advantage. Step-independent training is the deviation from this design, introduced by framework implementation choices rather than algorithmic motivation. Our analysis reveals that this deviation carries hidden costs that become catastrophic for long-horizon interactive tasks.\n\n\\subsection{Selective Verification via Action-Change Reward}\n\\label{sec:selective_verification}\n\nThe credit assignment analysis above focuses on training a competent base agent. We outline here a proposed design for a downstream application: selective verification. This component has not been implemented in the current work and is intended as a direction for future investigation.\n\nInteractive agents benefit from self-verification (re-evaluating their planned action before execution), but empirical analysis shows that over 90\\% of verification instances are confirmatory (the agent does not change its action after checking)~\\cite{long2026selfverification}. Training the agent to verify selectively, only when verification is likely to be informative, could reduce computational cost without sacrificing task performance.\n\nWe formulate selective verification as a binary decision at each step $t$: the agent outputs a verify token $v_t \\in \\{\\texttt{VERIFY}, \\texttt{SKIP}\\}$ before generating its action $a_t$. When $v_t = \\texttt{VERIFY}$, the agent generates a verification rationale and may revise its action; when $v_t = \\texttt{SKIP}$, the agent proceeds directly. The reward signal for training the verification policy uses the action-change indicator:\n\\begin{equation}\n\\Delta a_t = \\mathbb{1}[a_t^{\\text{post-verify}} \\neq a_t^{\\text{pre-verify}}]\n\\label{eq:action_change}\n\\end{equation}\nas a measure of verification informativeness. A verification step that changes the action provided useful corrective information; one that confirms the original action was uninformative for that instance. The full formulation of the verification reward and training procedure is presented in Section~\\ref{sec:selective_experiments}. Episode-level training serves as a prerequisite for this component: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.",
      "numLines": 97,
      "startLine": 1,
      "totalLines": 97
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01TRCY3M9au9u9RsR7Qj6y2W`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "e25ebe63-8535-47ce-86fd-14105b2e6162",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UB4aUZ9JSK4PSy6v19N3Pr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14873,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14873
      },
      "output_tokens": 45,
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

_source line 9 · 2026-05-18T12:06:32.181Z_

<details><summary>↩ Tool result · `toolu_01TRCY3M9au9u9RsR7Qj6y2W`</summary>

````text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
101	### 3.2 整体叙事结构
102	
103	```
104	现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结
105	```
106	
107	### 3.3 禁忌
108	
109	- **禁止泛泛介绍**：不要开头就写 "LLMs have shown remarkable capabilities..."，要从具体问题切入
110	- **禁止缺少过渡**：每段之间必须有逻辑连接
111	- **禁止实验报告风格**：Introduction 不是 "我们做了 X 实验得到了 Y 结果" 的罗列
112	- 每条 Contribution 必须有对应的 section/table 支撑
113	- Contribution 列表中不能出现未在前文铺垫过的概念
114	
115	---
116	
117	## 四、Related Work 写作规范
118	
119	### 4.1 目标
120	
121	让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。
122	
123	### 4.2 结构要求
124	
125	- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）
126	- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系
127	- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口
128	
129	### 4.3 禁忌
130	
131	- **禁止论文堆砌**：不要写成 "A proposed X. B proposed Y. C proposed Z." 的列表
132	- **目标不是展示读了多少论文**，而是做归纳和比较
133	- Contribution claim（"To our knowledge, no prior work..."）应放在 Introduction，不在 Related Work
134	
135	### 4.4 引用充足度
136	
137	- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**
138	- 任何一类缺失，审稿人会立刻看出来调研不充分
139	- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足
140	
141	---
142	
143	## 五、去 AI 写作风格（硬规则）
144	
145	以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**
146	
147	### 5.1 严禁破折号（最显著的 AI 痕迹）
148	
149	**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**
150	
151	- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**
152	- 替代方式：用逗号、括号或拆分为两个句子
153	- 强制检查命令：
154	  ```bash
155	  grep -n "—" paper/*.tex     # em-dash，每处人工判断是否必要
156	  grep -n " – " paper/*.tex   # 解释性 en-dash，几乎都应删除
157	  ```
158	- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）
159	
160	### 5.2 段落与句式
161	
162	- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的
163	- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句
164	- **禁止 -ing 短语结尾**：如 "..., highlighting the applicability of..." / "..., demonstrating the effectiveness of..."。这是 AI 写作最典型的标志之一
165	- **禁止连续使用 "Furthermore" / "Moreover" / "Additionally"**：一段内最多用一个过渡词
166	- **避免 "It is worth noting that..." / "Notably, ..."**：直接写要说的内容
167	
168	### 5.3 用词黑名单
169	
170	- 避免 "delve into" / "leverage" / "utilize" / "facilitate" — 用 "explore" / "use" / "enable"
171	- 避免 "a myriad of" / "a plethora of" — 用 "many" / "various"
172	- 避免 "in the realm of" / "in the context of" — 直接说
173	- 避免 "paradigm shift" / "novel" 过度使用
174	
175	### 5.4 校对清单（4 步）
176	
177	1. 全文 proofread 语法和拼写
178	2. 检查所有代词/指示词（this, that, it）是否指代明确
179	3. **`grep "—"` + `grep " – "` 全文清零**（删除所有解释性 dash，§5.1）
180	4. `grep "ing,"` 模式——大部分 -ing 分词短语需要改写
181	
182	---
183	
184	## 六、图表与视觉规范
185	
186	### 6.1 知识密度原则
187	
188	- **图表的信息必须紧凑**——不能为了美观而留大量白空间
189	- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中
190	- 能用 inline text 说清的不要占一整个 Figure
191	
192	### 6.2 表格规范
193	
194	- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）
195	- 小数精度全表统一
196	- 最优加粗、次优下划线
197	- Caption 必须自包含
198	
199	### 6.3 图片规范
200	
201	- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签
202	- 图中字体 >= 7pt（打印后仍可读）
203	- 栏宽约束需匹配目标 venue 模板要求
204	- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页
205	
206	### 6.4 空间效率
207	
208	- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源
209	- 优先使用 `\subfigure` 合并相关图
210	- Table 能 inline 就不要单独浮动
211	- 图表占比与其对叙事的贡献成正比
212	
213	---
214	
215	## 七、投稿前通用准备
216	
217	### 7.1 模板必须官方（硬规则）
218	
219	- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）
220	- **不要用**：
221	  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）
222	  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）
223	  - 组里学长留的旧版本（来源不明、无法追溯）
224	- 风险：
225	  - 样式不符合 → desk reject
226	  - margin 不对 → 被审稿人质疑诚信
227	  - reference 格式错 → 被认为不规范
228	- 流程：先查会议官网 templates → 找不到再 `WebSearch "{venue} {year} latex template official"` → 仍找不到汇报 Director（不要用就近年版本顶替）
229	- `\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致
230	
231	### 7.2 投稿要求逐项核对
232	
233	- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A
234	- 页数限制：查目标会议官网
235	- 匿名化要求：review 版 vs camera-ready 版本设置不同
236	- 行号开启（review 版常需）
237	- 字体大小、margin 不得修改 sty 文件
238	
239	### 7.3 最终修改 10 项检查流程
240	
241	提交前必须逐一检查：
242	1. 所有最新实验结果已全部录入
243	2. 根据实验结果将叙事调至最优状态
244	3. 附录所有内容在正文中被引用且融入叙事
245	4. 无数据堆砌（每个数字服务于叙事推进）
246	5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）
247	6. 全文主线统一（idea 变化后各章节逻辑一致）
248	7. 所有专有名词有定义
249	8. 无 AI 风格标志（dash、-ing phrases、过度分段）
250	9. 图表知识密度高、无视觉遮挡
251	10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础
252	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "e0c07207-cc45-4729-a6f2-caca7d139e49",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n\n### 3.2 整体叙事结构\n\n```\n现有进展 → 关键缺口 → 本文洞察 → 方法概述 → 实验证据 → 贡献总结\n```\n\n### 3.3 禁忌\n\n- **禁止泛泛介绍**：不要开头就写 \"LLMs have shown remarkable capabilities...\"，要从具体问题切入\n- **禁止缺少过渡**：每段之间必须有逻辑连接\n- **禁止实验报告风格**：Introduction 不是 \"我们做了 X 实验得到了 Y 结果\" 的罗列\n- 每条 Contribution 必须有对应的 section/table 支撑\n- Contribution 列表中不能出现未在前文铺垫过的概念\n\n---\n\n## 四、Related Work 写作规范\n\n### 4.1 目标\n\n让审稿人相信：作者理解这个领域，知道自己的方法站在什么位置，清楚相对已有工作的真实增量在哪里。\n\n### 4.2 结构要求\n\n- 把已有工作分成几个清晰的主题（如模型训练、推理增强、工具调用、数据构建、评测等）\n- 每类简要说明：已有方法做了什么、解决了哪些问题、和本文的关系\n- 帮助读者理解：哪些是本文直接继承的，哪些方法不同但解决相似问题，哪些留下了本文要解决的缺口\n\n### 4.3 禁忌\n\n- **禁止论文堆砌**：不要写成 \"A proposed X. B proposed Y. C proposed Z.\" 的列表\n- **目标不是展示读了多少论文**，而是做归纳和比较\n- Contribution claim（\"To our knowledge, no prior work...\"）应放在 Introduction，不在 Related Work\n\n### 4.4 引用充足度\n\n- 引用必须覆盖：**直接相关方法、baseline 论文、评测 benchmark 论文、理论基础**\n- 任何一类缺失，审稿人会立刻看出来调研不充分\n- 引用密度参照目标会议近年录用论文的量级——明显偏少意味着 Related Work 调研不足\n\n---\n\n## 五、去 AI 写作风格（硬规则）\n\n以下模式是 AI 生成文本的典型标志，审稿人一眼能看出。**必须全部消除。**\n\n### 5.1 严禁破折号（最显著的 AI 痕迹）\n\n**这是 AI 写作最容易被识别的标志，审稿人最敏感。单列为最高优先级硬规则。**\n\n- 解释性 em-dash（—，U+2014）和 en-dash（–，U+2013）必须**全部删除**\n- 替代方式：用逗号、括号或拆分为两个句子\n- 强制检查命令：\n  ```bash\n  grep -n \"—\" paper/*.tex     # em-dash，每处人工判断是否必要\n  grep -n \" – \" paper/*.tex   # 解释性 en-dash，几乎都应删除\n  ```\n- 例外（允许保留）：表格分隔符、数字范围（`2020–2024`、`pp. 12–18`）、专有名词（`Newton–Raphson`）\n\n### 5.2 段落与句式\n\n- **禁止过度分段**：不需要每 2-3 句就换段，自然段 5-8 句是正常的\n- **减少关系从句**（which, that, who）：能用简洁直接的句子就不用从句\n- **禁止 -ing 短语结尾**：如 \"..., highlighting the applicability of...\" / \"..., demonstrating the effectiveness of...\"。这是 AI 写作最典型的标志之一\n- **禁止连续使用 \"Furthermore\" / \"Moreover\" / \"Additionally\"**：一段内最多用一个过渡词\n- **避免 \"It is worth noting that...\" / \"Notably, ...\"**：直接写要说的内容\n\n### 5.3 用词黑名单\n\n- 避免 \"delve into\" / \"leverage\" / \"utilize\" / \"facilitate\" — 用 \"explore\" / \"use\" / \"enable\"\n- 避免 \"a myriad of\" / \"a plethora of\" — 用 \"many\" / \"various\"\n- 避免 \"in the realm of\" / \"in the context of\" — 直接说\n- 避免 \"paradigm shift\" / \"novel\" 过度使用\n\n### 5.4 校对清单（4 步）\n\n1. 全文 proofread 语法和拼写\n2. 检查所有代词/指示词（this, that, it）是否指代明确\n3. **`grep \"—\"` + `grep \" – \"` 全文清零**（删除所有解释性 dash，§5.1）\n4. `grep \"ing,\"` 模式——大部分 -ing 分词短语需要改写\n\n---\n\n## 六、图表与视觉规范\n\n### 6.1 知识密度原则\n\n- **图表的信息必须紧凑**——不能为了美观而留大量白空间\n- 一张图如果只传达一个简单信息，要么缩小要么合并到其他图中\n- 能用 inline text 说清的不要占一整个 Figure\n\n### 6.2 表格规范\n\n- 表格和正文文字不能视觉重叠（检查 column 宽度和 alignment）\n- 小数精度全表统一\n- 最优加粗、次优下划线\n- Caption 必须自包含\n\n### 6.3 图片规范\n\n- 数值标签不能被线、bar、点遮住——用白色背景或偏移标签\n- 图中字体 >= 7pt（打印后仍可读）\n- 栏宽约束需匹配目标 venue 模板要求\n- 概念图/流程图要有信息量，不要画一个 trivial 的 pipeline 然后占半页\n\n### 6.4 空间效率\n\n- 顶会正文页数严格受限（具体页数查目标会议官网），每 cm² 都是宝贵资源\n- 优先使用 `\\subfigure` 合并相关图\n- Table 能 inline 就不要单独浮动\n- 图表占比与其对叙事的贡献成正比\n\n---\n\n## 七、投稿前通用准备\n\n### 7.1 模板必须官方（硬规则）\n\n- LaTeX 模板**必须从目标会议官网下载**（CallForPapers / Author Instructions 页面）\n- **不要用**：\n  - 网上他人转载的复制版本（可能被改过 margin / 行号设置）\n  - 上一年的模板（参数可能变：字体、margin、行号、anonymous 选项等）\n  - 组里学长留的旧版本（来源不明、无法追溯）\n- 风险：\n  - 样式不符合 → desk reject\n  - margin 不对 → 被审稿人质疑诚信\n  - reference 格式错 → 被认为不规范\n- 流程：先查会议官网 templates → 找不到再 `WebSearch \"{venue} {year} latex template official\"` → 仍找不到汇报 Director（不要用就近年版本顶替）\n- `\\documentclass[]{}` 选项必须与目标 venue + 阶段（review / camera-ready）一致\n\n### 7.2 投稿要求逐项核对\n\n- 目标会议如要求 Checklist / Ethical Statement / Broader Impact Statement / Reproducibility Statement，必须**认真填每一项**，不要全写 N/A\n- 页数限制：查目标会议官网\n- 匿名化要求：review 版 vs camera-ready 版本设置不同\n- 行号开启（review 版常需）\n- 字体大小、margin 不得修改 sty 文件\n\n### 7.3 最终修改 10 项检查流程\n\n提交前必须逐一检查：\n1. 所有最新实验结果已全部录入\n2. 根据实验结果将叙事调至最优状态\n3. 附录所有内容在正文中被引用且融入叙事\n4. 无数据堆砌（每个数字服务于叙事推进）\n5. Abstract 和 Introduction 具有吸引力（不是实验报告风格）\n6. 全文主线统一（idea 变化后各章节逻辑一致）\n7. 所有专有名词有定义\n8. 无 AI 风格标志（dash、-ing phrases、过度分段）\n9. 图表知识密度高、无视觉遮挡\n10. Reference 覆盖直接相关方法、baseline、benchmark、理论基础\n",
      "numLines": 252,
      "startLine": 1,
      "totalLines": 252
    }
  }
}
````

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01DF65kXDgWcwsAYeEyu23Vt`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "6e1a1667-3ad0-439b-92e1-b9c4b87ef41a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UB4aUZ9JSK4PSy6v19N3Pr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14873,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14873
      },
      "output_tokens": 45,
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

_source line 11 · 2026-05-18T12:06:32.436Z_

<details><summary>↩ Tool result · `toolu_01DF65kXDgWcwsAYeEyu23Vt`</summary>

````text
1	---
2	name: latex-paper
3	description: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。
4	scope: global
5	tags:
6	- latex
7	- paper-writing
8	- academic
9	- citation
10	- submission
11	version: 1
12	roles:
13	- agent
14	- worker
15	---
16	
17	# LaTeX 论文写作全流程
18	
19	ML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。
20	
21	---
22	
23	## 1. 工作模式
24	
25	开始前选择模式：
26	
27	| 模式 | 说明 | 适用 |
28	|------|------|------|
29	| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |
30	| **Improve** | 改写已有章节，强化论证 | 修改稿 |
31	| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |
32	
33	---
34	
35	## 2. Claim-Evidence 方法论
36	
37	**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**
38	
39	### 2.1 一句话贡献
40	
41	在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。
42	
43	### 2.2 Claim-Evidence Map
44	
45	为每个 contribution 建立 claim→evidence 映射表：
46	
47	| Contribution | Claim | Evidence | Table/Figure |
48	|-------------|-------|----------|-------------|
49	| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |
50	| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |
51	| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |
52	
53	**没有直接证据支撑的 claim 必须删除或降级为 discussion。**
54	
55	### 2.3 章节起草顺序
56	
57	```
58	1. Introduction + Experiments（先确定 claim 和 evidence）
59	2. Method（评估问题稳定后再写细节）
60	3. Related Work
61	4. Abstract + Title（核心 claim 定型后最后写）
62	```
63	
64	### 2.4 Quality Gates
65	
66	投稿前必须通过：
67	- [ ] 前两段出现显式 novelty 声明
68	- [ ] 每个 contribution 有可验证的 evidence
69	- [ ] Abstract / Intro / Conclusion 的 claim 一致
70	- [ ] Limitations 真实且技术性诚实
71	- [ ] 审稿人两分钟内能识别 delta
72	
73	---
74	
75	## 3. 引用防幻觉（CRITICAL）
76	
77	**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**
78	
79	### 3.1 黄金法则
80	
81	```
82	IF 无法程序化获取引用:
83	    → 标记 [CITATION NEEDED] 或 \cite{PLACEHOLDER_verify}
84	    → 明确告知用户
85	    → 绝不编造看似合理的引用
86	```
87	
88	### 3.2 五步验证流程
89	
90	```
91	1. SEARCH  → Semantic Scholar API 搜索关键词
92	2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）
93	3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）
94	4. CHECK   → 确认你引用的 claim 确实出自该论文
95	5. ADD     → 加入 .bib 文件
96	```
97	
98	### 3.3 API 速查
99	
100	| API | 用途 | 限制 |
101	|-----|------|------|
102	| **Semantic Scholar** | ML/AI 论文搜索 | 1 RPS (免费) |
103	| **CrossRef** | DOI → BibTeX | 需 mailto 头 |
104	| **arXiv** | 预印本搜索 | 3s 间隔 |
105	
106	```python
107	# DOI → BibTeX（最可靠的方式）
108	import requests
109	def doi_to_bibtex(doi: str) -> str:
110	    r = requests.get(f"https://doi.org/{doi}",
111	                     headers={"Accept": "application/x-bibtex"})
112	    r.raise_for_status()
113	    return r.text
114	
115	# Semantic Scholar 搜索
116	from semanticscholar import SemanticScholar
117	sch = SemanticScholar()
118	results = sch.search_paper("attention mechanism transformers", limit=5)
119	for p in results:
120	    print(f"{p.title} | DOI: {p.externalIds.get('DOI', 'N/A')}")
121	```
122	
123	### 3.4 引用处理规则
124	
125	| 情况 | 处理 |
126	|------|------|
127	| 找到论文 + DOI + BibTeX | 直接用 |
128	| 找到论文，无 DOI | 用 arXiv BibTeX |
129	| 论文存在但无法获取 BibTeX | 标记 placeholder，告知用户 |
130	| 不确定论文是否存在 | 标记 `[CITATION NEEDED]`，告知用户 |
131	| "我觉得有篇关于 X 的论文" | **绝不引用** — 先搜索或标记 |
132	
133	---
134	
135	## 4. 顶会模板速查
136	
137	### 4.1 ML/AI 会议
138	
139	| 会议 | 页数限制 | 主文件 | 样式文件 | 必须项 |
140	|------|---------|--------|---------|--------|
141	| **NeurIPS** | 9 页 | `main.tex` | `neurips.sty` | Paper Checklist |
142	| **ICML** | 8 页 (+1 camera-ready) | `example_paper.tex` | `icml2026.sty` | Broader Impact |
143	| **ICLR** | 9 页 (+1) | `iclr_conference.tex` | `iclr_conference.sty` | LLM 使用声明 |
144	| **ACL/EMNLP** | 8 页 (long) | `acl_latex.tex` | `acl.sty` | Limitations 必须 |
145	| **AAAI** | 7 页 (+1) | `aaai_template.tex` | `aaai.sty` | 严格样式 |
146	| **COLM** | 9 页 (+1) | `colm_conference.tex` | `colm_conference.sty` | 语言模型聚焦 |
147	
148	### 4.2 系统会议
149	
150	| 会议 | 页数限制 | 模板类型 | 关键要求 |
151	|------|---------|---------|---------|
152	| **OSDI** | 12 页 (+2) | USENIX `usenix.sty` | Research / Operational 双 track |
153	| **NSDI** | 12 页 | USENIX | Introduction 预筛 |
154	| **ASPLOS** | 12 页 | ACM `acmart.cls (sigplan)` | 前 2 页快速评审 |
155	| **SOSP** | 12 页 | ACM `acmart.cls (sigplan)` | 可选 Artifact Evaluation |
156	
157	### 4.3 模板使用原则
158	
159	```bash
160	# 1. 复制整个模板目录（不要只拷 .tex）
161	cp -r templates/neurips2025/ ~/papers/my-paper/
162	
163	# 2. 先编译未修改的模板，确认能跑通
164	latexmk -pdf main.tex
165	
166	# 3. 逐章替换内容，频繁编译
167	```
168	
169	**禁止事项：**
170	- 不要修改 `.sty` 文件
171	- 不要在会议模板间复制 `\usepackage` 行
172	- 不要只复制 `.tex` 而不带 `.sty/.bst`
173	
174	---
175	
176	## 5. 写作规范
177	
178	### 5.1 时间分配（Neel Nanda）
179	
180	花**大致相等**的时间在：
181	1. Abstract
182	2. Introduction
183	3. 图表
184	4. **其余所有内容加起来**
185	
186	审稿人读论文的顺序：标题 → 摘要 → 引言 → 图表 → 也许正文。
187	
188	### 5.2 Abstract 五句法（Sebastian Farquhar）
189	
190	```
191	1. 你做了什么（"We introduce/prove/demonstrate..."）
192	2. 为什么这很难且重要
193	3. 怎么做的（含专业关键词以便检索）
194	4. 有什么证据
195	5. 最惊人的数字/结果
196	```
197	
198	删除一切泛泛的开头：~~"Large language models have achieved remarkable success..."~~
199	
200	### 5.3 句子级清晰度（Gopen & Swan）
201	
202	| 原则 | 规则 |
203	|------|------|
204	| 主谓紧邻 | 不要在主语和动词之间插入长从句 |
205	| 重点在句尾 | 把关键数字/结论放在句末 |
206	| 旧信息在前 | 先放读者已知的内容，再引入新概念 |
207	| 动词表达动作 | "We analyzed" 而非 "We performed an analysis" |
208	
209	### 5.4 常见修改
210	
211	| 问题 | 修复 |
212	|------|------|
213	| Abstract 太泛 | 删第一句（如果它能放在任何 ML 论文前面） |
214	| Introduction 超 1.5 页 | 背景挪到 Related Work |
215	| 实验没有显式 claim | 每个实验前加 "This tests whether..." |
216	| 缺统计显著性 | 加 error bars + 运行次数 + 计算方法 |
217	
218	---
219	
220	## 6. 投稿工程链
221	
222	### 6.1 构建
223	
224	```bash
225	# 推荐：latexmk 一键构建
226	latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
227	
228	# 手动：需要多次编译
229	pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
230	```
231	
232	### 6.2 Lint + 格式化
233	
234	```bash
235	# Lint: 检查常见 LaTeX 问题
236	chktex main.tex
237	
238	# 格式化: 减少 diff 噪声
239	latexindent -w main.tex
240	```
241	
242	### 6.3 图表格式
243	
244	| 类型 | 格式 | 说明 |
245	|------|------|------|
246	| 矢量图（plot、diagram） | PDF | matplotlib: `plt.savefig('fig.pdf')` |
247	| 照片/heatmap | PNG 600dpi 或 TIFF | 栅格图 |
248	| 表格 | `booktabs` 包 | `\toprule/\midrule/\bottomrule` |
249	
250	```latex
251	\usepackage{booktabs}
252	\begin{tabular}{lcc}
253	\toprule
254	Method & Accuracy $\uparrow$ & Latency $\downarrow$ \\
255	\midrule
256	Baseline & 85.2 & 45ms \\
257	\textbf{Ours} & \textbf{92.1} & 38ms \\
258	\bottomrule
259	\end{tabular}
260	```
261	
262	**图表规范：**
263	- 用色盲友好色板（Okabe-Ito 或 Paul Tol）
264	- 图内不放标题（用 caption）
265	- Caption 独立可理解（不依赖正文）
266	- 最佳值加粗，标注方向符号（↑ 越高越好，↓ 越低越好）
267	
268	### 6.4 投稿打包
269	
270	```bash
271	# 清理辅助文件
272	latexmk -c
273	
274	# 打包投稿
275	zip -r submission.zip main.tex *.sty *.bst *.bib figures/ --exclude='*.aux' --exclude='*.log'
276	```
277	
278	### 6.5 常见失败点
279	
280	| 问题 | 解决 |
281	|------|------|
282	| 图片格式混用导致编译失败 | 统一用 PDF |
283	| 字体未嵌入 | `pdffonts output.pdf` 检查 |
284	| Overfull box 过多 | 关键位置手动调行 |
285	| 引用缺字段 | 检查 DOI/年份/期刊名 |
286	| 超页数 | 用 `\vspace{-Xpt}` 微调，或精简内容 |
287	
288	---
289	
290	## 7. 会议转投
291	
292	当论文被拒或转投其他会议时：
293	
294	### 7.1 ML/AI 会议间转换
295	
296	| 转换 | 页数变化 | 关键调整 |
297	|------|---------|---------|
298	| NeurIPS → ICML | 9→8 | 删 1 页，加 Broader Impact |
299	| ICML → ICLR | 8→9 | 可扩展实验 + LLM 声明 |
300	| NeurIPS → ACL | 9→8 | 按 NLP 惯例重组 + Limitations |
301	| ICLR → AAAI | 9→7 | 大幅精简，严格样式 |
302	
303	### 7.2 转投原则
304	
305	1. **永远用目标模板重新开始** — 复制目标模板，迁移内容，不要合并 preamble
306	2. **只迁移正文内容** — 不复制 `\usepackage`、header/footer 命令
307	3. **根据审稿意见改进** — 但不要在新稿中提及旧投稿（双盲）
308	4. **检查目标会议特殊要求** — checklist、ethics statement、LLM 声明等
309	
310	---
311	
312	## 8. 投前清单
313	
314	### 通用清单
315	
316	- [ ] Abstract/Intro/Conclusion 的 claim 一致
317	- [ ] 每个 contribution 有对应 evidence
318	- [ ] 所有引用已程序化验证（无幻觉引用）
319	- [ ] Error bars + 运行次数 + 统计方法
320	- [ ] Limitations 章节存在且诚实
321	- [ ] 匿名化（双盲审稿）
322	- [ ] 符合页数限制
323	- [ ] 所有图表有自包含 caption
324	- [ ] `.bib` 中无缺失字段
325	- [ ] PDF 编译无 warning
326	
327	### 会议特定
328	
329	| 会议 | 额外要求 |
330	|------|---------|
331	| NeurIPS | 16 项 Paper Checklist（附录，不计页数） |
332	| ICML | Broader Impact Statement |
333	| ICLR | LLM 使用声明 |
334	| ACL/EMNLP | Limitations 章节（必须），Ethics Statement |
335	| AAAI | 严格样式文件合规 |
336	
337	---
338	
339	## 参考资源
340	
341	**写作方法论：**
342	- [Neel Nanda: How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/) — What/Why/So What 框架
343	- [Farquhar: How to Write ML Papers](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/) — 五句法 Abstract
344	- [Gopen & Swan: Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) — 读者预期 7 原则
345	- [Lipton: Heuristics for Scientific Writing](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/) — 用词
346	- [Perez: Easy Paper Writing Tips](https://ethanperez.net/easy-paper-writing-tips/) — 微观清晰度
347	
348	**API：**
349	- [Semantic Scholar](https://api.semanticscholar.org/api-docs/) | [CrossRef](https://www.crossref.org/documentation/) | [arXiv](https://info.arxiv.org/help/api/)
350	
351	**会议官方：**
352	- [NeurIPS](https://neurips.cc/) | [ICML](https://icml.cc/) | [ICLR](https://iclr.cc/) | [ACL](https://www.aclweb.org/) | [AAAI](https://aaai.org/) | [EMNLP](https://2025.emnlp.org/)
353	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "f1b93a79-7fff-4537-902f-1926c58b618a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md",
      "content": "---\nname: latex-paper\ndescription: ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。\nscope: global\ntags:\n- latex\n- paper-writing\n- academic\n- citation\n- submission\nversion: 1\nroles:\n- agent\n- worker\n---\n\n# LaTeX 论文写作全流程\n\nML/AI 顶会论文从草稿到投稿的完整指南。整合 Orchestra Research、VibeSkills、claim2evidence 三方最佳实践。\n\n---\n\n## 1. 工作模式\n\n开始前选择模式：\n\n| 模式 | 说明 | 适用 |\n|------|------|------|\n| **Build** | 从实验笔记/结果/代码生成论文 | 新稿 |\n| **Improve** | 改写已有章节，强化论证 | 修改稿 |\n| **Audit** | 输出风险列表 + 缺失证据 + 修复建议 | 投前检查 |\n\n---\n\n## 2. Claim-Evidence 方法论\n\n**核心原则：论文是一个有中心贡献的故事，不是实验的堆砌。**\n\n### 2.1 一句话贡献\n\n在写任何内容之前，必须能用一句话说清贡献。如果不能，说明还没准备好写论文。\n\n### 2.2 Claim-Evidence Map\n\n为每个 contribution 建立 claim→evidence 映射表：\n\n| Contribution | Claim | Evidence | Table/Figure |\n|-------------|-------|----------|-------------|\n| C1: 方法 X 在 Y 上 SOTA | 比所有 baseline 高 ≥2% | 5-seed 平均，p<0.05 | Table 1 |\n| C2: 消融证明 Z 是关键 | 去掉 Z 后掉 >5% | 消融实验 | Table 2 |\n| C3: 计算效率 | 比 baseline 快 3× | FLOPs + wall-clock | Figure 3 |\n\n**没有直接证据支撑的 claim 必须删除或降级为 discussion。**\n\n### 2.3 章节起草顺序\n\n```\n1. Introduction + Experiments（先确定 claim 和 evidence）\n2. Method（评估问题稳定后再写细节）\n3. Related Work\n4. Abstract + Title（核心 claim 定型后最后写）\n```\n\n### 2.4 Quality Gates\n\n投稿前必须通过：\n- [ ] 前两段出现显式 novelty 声明\n- [ ] 每个 contribution 有可验证的 evidence\n- [ ] Abstract / Intro / Conclusion 的 claim 一致\n- [ ] Limitations 真实且技术性诚实\n- [ ] 审稿人两分钟内能识别 delta\n\n---\n\n## 3. 引用防幻觉（CRITICAL）\n\n**AI 生成引用有 ~40% 错误率。绝对禁止凭记忆写 BibTeX。**\n\n### 3.1 黄金法则\n\n```\nIF 无法程序化获取引用:\n    → 标记 [CITATION NEEDED] 或 \\cite{PLACEHOLDER_verify}\n    → 明确告知用户\n    → 绝不编造看似合理的引用\n```\n\n### 3.2 五步验证流程\n\n```\n1. SEARCH  → Semantic Scholar API 搜索关键词\n2. VERIFY  → 至少 2 个来源确认论文存在（S2 + arXiv/CrossRef）\n3. RETRIEVE → 通过 DOI 获取 BibTeX（程序化，非记忆）\n4. CHECK   → 确认你引用的 claim 确实出自该论文\n5. ADD     → 加入 .bib 文件\n```\n\n### 3.3 API 速查\n\n| API | 用途 | 限制 |\n|-----|------|------|\n| **Semantic Scholar** | ML/AI 论文搜索 | 1 RPS (免费) |\n| **CrossRef** | DOI → BibTeX | 需 mailto 头 |\n| **arXiv** | 预印本搜索 | 3s 间隔 |\n\n```python\n# DOI → BibTeX（最可靠的方式）\nimport requests\ndef doi_to_bibtex(doi: str) -> str:\n    r = requests.get(f\"https://doi.org/{doi}\",\n                     headers={\"Accept\": \"application/x-bibtex\"})\n    r.raise_for_status()\n    return r.text\n\n# Semantic Scholar 搜索\nfrom semanticscholar import SemanticScholar\nsch = SemanticScholar()\nresults = sch.search_paper(\"attention mechanism transformers\", limit=5)\nfor p in results:\n    print(f\"{p.title} | DOI: {p.externalIds.get('DOI', 'N/A')}\")\n```\n\n### 3.4 引用处理规则\n\n| 情况 | 处理 |\n|------|------|\n| 找到论文 + DOI + BibTeX | 直接用 |\n| 找到论文，无 DOI | 用 arXiv BibTeX |\n| 论文存在但无法获取 BibTeX | 标记 placeholder，告知用户 |\n| 不确定论文是否存在 | 标记 `[CITATION NEEDED]`，告知用户 |\n| \"我觉得有篇关于 X 的论文\" | **绝不引用** — 先搜索或标记 |\n\n---\n\n## 4. 顶会模板速查\n\n### 4.1 ML/AI 会议\n\n| 会议 | 页数限制 | 主文件 | 样式文件 | 必须项 |\n|------|---------|--------|---------|--------|\n| **NeurIPS** | 9 页 | `main.tex` | `neurips.sty` | Paper Checklist |\n| **ICML** | 8 页 (+1 camera-ready) | `example_paper.tex` | `icml2026.sty` | Broader Impact |\n| **ICLR** | 9 页 (+1) | `iclr_conference.tex` | `iclr_conference.sty` | LLM 使用声明 |\n| **ACL/EMNLP** | 8 页 (long) | `acl_latex.tex` | `acl.sty` | Limitations 必须 |\n| **AAAI** | 7 页 (+1) | `aaai_template.tex` | `aaai.sty` | 严格样式 |\n| **COLM** | 9 页 (+1) | `colm_conference.tex` | `colm_conference.sty` | 语言模型聚焦 |\n\n### 4.2 系统会议\n\n| 会议 | 页数限制 | 模板类型 | 关键要求 |\n|------|---------|---------|---------|\n| **OSDI** | 12 页 (+2) | USENIX `usenix.sty` | Research / Operational 双 track |\n| **NSDI** | 12 页 | USENIX | Introduction 预筛 |\n| **ASPLOS** | 12 页 | ACM `acmart.cls (sigplan)` | 前 2 页快速评审 |\n| **SOSP** | 12 页 | ACM `acmart.cls (sigplan)` | 可选 Artifact Evaluation |\n\n### 4.3 模板使用原则\n\n```bash\n# 1. 复制整个模板目录（不要只拷 .tex）\ncp -r templates/neurips2025/ ~/papers/my-paper/\n\n# 2. 先编译未修改的模板，确认能跑通\nlatexmk -pdf main.tex\n\n# 3. 逐章替换内容，频繁编译\n```\n\n**禁止事项：**\n- 不要修改 `.sty` 文件\n- 不要在会议模板间复制 `\\usepackage` 行\n- 不要只复制 `.tex` 而不带 `.sty/.bst`\n\n---\n\n## 5. 写作规范\n\n### 5.1 时间分配（Neel Nanda）\n\n花**大致相等**的时间在：\n1. Abstract\n2. Introduction\n3. 图表\n4. **其余所有内容加起来**\n\n审稿人读论文的顺序：标题 → 摘要 → 引言 → 图表 → 也许正文。\n\n### 5.2 Abstract 五句法（Sebastian Farquhar）\n\n```\n1. 你做了什么（\"We introduce/prove/demonstrate...\"）\n2. 为什么这很难且重要\n3. 怎么做的（含专业关键词以便检索）\n4. 有什么证据\n5. 最惊人的数字/结果\n```\n\n删除一切泛泛的开头：~~\"Large language models have achieved remarkable success...\"~~\n\n### 5.3 句子级清晰度（Gopen & Swan）\n\n| 原则 | 规则 |\n|------|------|\n| 主谓紧邻 | 不要在主语和动词之间插入长从句 |\n| 重点在句尾 | 把关键数字/结论放在句末 |\n| 旧信息在前 | 先放读者已知的内容，再引入新概念 |\n| 动词表达动作 | \"We analyzed\" 而非 \"We performed an analysis\" |\n\n### 5.4 常见修改\n\n| 问题 | 修复 |\n|------|------|\n| Abstract 太泛 | 删第一句（如果它能放在任何 ML 论文前面） |\n| Introduction 超 1.5 页 | 背景挪到 Related Work |\n| 实验没有显式 claim | 每个实验前加 \"This tests whether...\" |\n| 缺统计显著性 | 加 error bars + 运行次数 + 计算方法 |\n\n---\n\n## 6. 投稿工程链\n\n### 6.1 构建\n\n```bash\n# 推荐：latexmk 一键构建\nlatexmk -pdf -interaction=nonstopmode -halt-on-error main.tex\n\n# 手动：需要多次编译\npdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex\n```\n\n### 6.2 Lint + 格式化\n\n```bash\n# Lint: 检查常见 LaTeX 问题\nchktex main.tex\n\n# 格式化: 减少 diff 噪声\nlatexindent -w main.tex\n```\n\n### 6.3 图表格式\n\n| 类型 | 格式 | 说明 |\n|------|------|------|\n| 矢量图（plot、diagram） | PDF | matplotlib: `plt.savefig('fig.pdf')` |\n| 照片/heatmap | PNG 600dpi 或 TIFF | 栅格图 |\n| 表格 | `booktabs` 包 | `\\toprule/\\midrule/\\bottomrule` |\n\n```latex\n\\usepackage{booktabs}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Accuracy $\\uparrow$ & Latency $\\downarrow$ \\\\\n\\midrule\nBaseline & 85.2 & 45ms \\\\\n\\textbf{Ours} & \\textbf{92.1} & 38ms \\\\\n\\bottomrule\n\\end{tabular}\n```\n\n**图表规范：**\n- 用色盲友好色板（Okabe-Ito 或 Paul Tol）\n- 图内不放标题（用 caption）\n- Caption 独立可理解（不依赖正文）\n- 最佳值加粗，标注方向符号（↑ 越高越好，↓ 越低越好）\n\n### 6.4 投稿打包\n\n```bash\n# 清理辅助文件\nlatexmk -c\n\n# 打包投稿\nzip -r submission.zip main.tex *.sty *.bst *.bib figures/ --exclude='*.aux' --exclude='*.log'\n```\n\n### 6.5 常见失败点\n\n| 问题 | 解决 |\n|------|------|\n| 图片格式混用导致编译失败 | 统一用 PDF |\n| 字体未嵌入 | `pdffonts output.pdf` 检查 |\n| Overfull box 过多 | 关键位置手动调行 |\n| 引用缺字段 | 检查 DOI/年份/期刊名 |\n| 超页数 | 用 `\\vspace{-Xpt}` 微调，或精简内容 |\n\n---\n\n## 7. 会议转投\n\n当论文被拒或转投其他会议时：\n\n### 7.1 ML/AI 会议间转换\n\n| 转换 | 页数变化 | 关键调整 |\n|------|---------|---------|\n| NeurIPS → ICML | 9→8 | 删 1 页，加 Broader Impact |\n| ICML → ICLR | 8→9 | 可扩展实验 + LLM 声明 |\n| NeurIPS → ACL | 9→8 | 按 NLP 惯例重组 + Limitations |\n| ICLR → AAAI | 9→7 | 大幅精简，严格样式 |\n\n### 7.2 转投原则\n\n1. **永远用目标模板重新开始** — 复制目标模板，迁移内容，不要合并 preamble\n2. **只迁移正文内容** — 不复制 `\\usepackage`、header/footer 命令\n3. **根据审稿意见改进** — 但不要在新稿中提及旧投稿（双盲）\n4. **检查目标会议特殊要求** — checklist、ethics statement、LLM 声明等\n\n---\n\n## 8. 投前清单\n\n### 通用清单\n\n- [ ] Abstract/Intro/Conclusion 的 claim 一致\n- [ ] 每个 contribution 有对应 evidence\n- [ ] 所有引用已程序化验证（无幻觉引用）\n- [ ] Error bars + 运行次数 + 统计方法\n- [ ] Limitations 章节存在且诚实\n- [ ] 匿名化（双盲审稿）\n- [ ] 符合页数限制\n- [ ] 所有图表有自包含 caption\n- [ ] `.bib` 中无缺失字段\n- [ ] PDF 编译无 warning\n\n### 会议特定\n\n| 会议 | 额外要求 |\n|------|---------|\n| NeurIPS | 16 项 Paper Checklist（附录，不计页数） |\n| ICML | Broader Impact Statement |\n| ICLR | LLM 使用声明 |\n| ACL/EMNLP | Limitations 章节（必须），Ethics Statement |\n| AAAI | 严格样式文件合规 |\n\n---\n\n## 参考资源\n\n**写作方法论：**\n- [Neel Nanda: How to Write ML Papers](https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/) — What/Why/So What 框架\n- [Farquhar: How to Write ML Papers](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/) — 五句法 Abstract\n- [Gopen & Swan: Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf) — 读者预期 7 原则\n- [Lipton: Heuristics for Scientific Writing](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/) — 用词\n- [Perez: Easy Paper Writing Tips](https://ethanperez.net/easy-paper-writing-tips/) — 微观清晰度\n\n**API：**\n- [Semantic Scholar](https://api.semanticscholar.org/api-docs/) | [CrossRef](https://www.crossref.org/documentation/) | [arXiv](https://info.arxiv.org/help/api/)\n\n**会议官方：**\n- [NeurIPS](https://neurips.cc/) | [ICML](https://icml.cc/) | [ICLR](https://iclr.cc/) | [ACL](https://www.aclweb.org/) | [AAAI](https://aaai.org/) | [EMNLP](https://2025.emnlp.org/)\n",
      "numLines": 353,
      "startLine": 1,
      "totalLines": 353
    }
  }
}
````

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context. Let me analyze the current method.tex and plan the edits according to the D073 narrative revision task.

Key changes needed:
1. §3.1 - Keep as is
2. §3.2 - Keep as is
3. §3.3 - Keep as is
4. §3.4 - Modify framing per D073:
   - M1: info loss kills generalization (not "establishes ceiling")
   - M2: sign misattribution breaks training stability (not "cumulative degradation")
   - End prediction: three training dynamics instead of two-phase collapse
   - No quantitative percentage decomposition
5. §3.5 - Keep as is
6. §3.6 (NEW) - Factorial Experiment Design (~300 words)
7. §3.7 (shortened) - Selective Verification (current §3.6 shortened to ~100 words)

Now I'm carefully planning the edits. For §3.4, I need to reframe M1 around how information loss directly undermines generalization ability, and M2 around how sign misattribution creates instability during training with high variance and unpredictable behavior. The ending should shift from describing a two-phase collapse to articulating three distinct training dynamics.

Let me re-examine the current §3.4 opening to understand what needs changing. The mechanism descriptions need to move away from "structural performance ceiling" and "cumulative damage" language toward more direct causal explanations of how each mechanism breaks the learning process.

For M1, I need to reframe the information loss not as establishing a fixed ceiling but as fundamentally preventing generalization—the model might memorize local patterns on its training distribution but lacks the cross-step context needed for genuine task understanding. For M2, the gradient corruption doesn't just erode performance progressively; it destabilizes training itself, creating high variance and potentially triggering oscillation or collapse depending on which error dominates. The closing should reflect these revised mechanisms rather than predicting a two-phase collapse sequence. I'm identifying two mechanisms at different layers that drive training failure under step-independent optimization. The first restricts the model's observable context at inference time, destroying its ability to reason across steps. The second introduces systematic gradient sign errors during training, creating unstable dynamics that can manifest as monotonic collapse, oscillation followed by degradation, or stable learning depending on which mechanism dominates. These predictions align with what the experiments should reveal. This information loss destroys the policy's ability to generalize beyond local, single-window strategies. The model may learn to produce valid actions within its observable context, but it cannot acquire strategies that require conditioning on outcomes from earlier steps. The constraint is structural: no amount of training can recover information that is absent from the input. Different window sizes impose different degrees of information loss, with smaller windows restricting the representable strategy space more severely. In our h-sweep experiments, initial evaluation performance varies across window sizes, reflecting the direct relationship between available context and the policy's generalization capacity.

Formally, I can express this through mutual information: the optimal policy depends on information from the full history, but windowing limits each decision to only what's visible in that window. For tasks with dependencies spanning more than h steps, this creates a significant information gap that grows with episode length and shrinks with window size, predicting a sharp performance drop as the window becomes too small.

The second mechanism operates differently—it corrupts the learning process itself rather than constraining what the policy can represent. Unlike the information bottleneck, this doesn't prevent the policy from learning certain strategies; instead, it actively breaks the gradient signal that drives optimization. The damage compounds with each training step, degrading the quality of learned representations in ways that become increasingly difficult to recover from.

This mechanism breaks training stability in a fundamental way. When the gradient signal gets corrupted by sign misattribution, the optimization dynamics become unpredictable—training might collapse monotonically, oscillate erratically, or show periods of improvement followed by sudden degradation, depending on how severe the misattribution is and what the task distribution looks like.

The distinction matters because magnitude decay just slows convergence, but sign errors cause active divergence from the optimal solution. That's the core difference between the two mechanisms.

Now I need to add a new section on the factorial experiment design after the episode-level training section, then shift the selective verification section down and condense it. Looking at the existing §3.6 content, I see it discusses credit assignment for training a base agent, then pivots to proposing selective verification as a downstream application that hasn't been implemented yet. The section then explains the motivation—most verification attempts don't change the agent's action—and introduces a formulation where the agent decides whether to verify before generating each action.

The next thinking continues this formulation by defining how to measure whether verification was actually useful: we track whether the agent's action changed after verification, and use that signal to train the verification policy itself. The key insight is that this selective verification component depends on having a competent base agent first, which is why the episode-level training discussion comes before it.

I'll compress this naturally: We measure verification informativeness by tracking whether the agent changes its action after reviewing—a change indicates useful correction, while confirmation means that verification step was wasted. This action-change signal trains the selective verification policy, though the full training procedure is detailed later. Importantly, this component requires a sufficiently competent base agent as a foundation, which is why episode-level training must come first. I'm working through the edits systematically—first revising the introduction to section 3.4, then updating the mechanism descriptions, and inserting a new section on factorial experiment design that outlines a 2×2 experimental setup to isolate the effects of each mechanism independently.

Now I'm detailing the four experimental conditions and how comparing them reveals which mechanism drives the observed training instability—Cell A has both mechanisms active, Cell B eliminates sign misattribution while keeping information loss, and Cell D removes both effects entirely, allowing me to attribute performance differences to specific mechanisms. I'm identifying two failure mechanisms at different layers—one at inference that creates a performance ceiling through limited context, and another at training that actively degrades performance below that ceiling. this ceiling through systematic gradient errors that accumulate over optimization steps. We predict a two-phase collapse under step-independent training: strategic failure (task success drops) while action formatting initially remains intact, followed by complete collapse of both capabilities as wrong-direction gradients accumulate. Section~\ref{sec:experiments} validates this prediction empirically.

We identify two mechanisms operating at different layers that jointly cause training failure under step-independent optimization. The first operates at the inference layer: by restricting the model's observable context, it destroys the policy's ability to generalize to tasks that require cross-step reasoning. The second operates at the training layer: systematic gradient sign errors destabilize the optimization process, producing high-variance training dynamics that range from catastrophic collapse to erratic oscillation. Together, these mechanisms predict three distinct training regimes depending on which mechanism dominates: (a) monotonic collapse when both mechanisms are severe, (b) oscillation followed by degradation when sign misattribution is the primary driver, and (c) stable learning when episode-level training eliminates both. Section~\ref{sec:experiments} validates these predictions empirically.

This information loss destroys the policy's ability to generalize beyond local, single-window strategies. The model may learn to produce valid actions within its observable context, but it cannot acquire conditional strategies that depend on outcomes from earlier steps. The constraint is structural: no amount of training can recover information that is absent from the input, and different window sizes impose varying degrees of this information loss. I'm working through the edits to clarify the mechanisms and their experimental predictions. For Mechanism 2, I need to emphasize that it destabilizes the training process itself rather than just constraining what can be learned—the gradient corruption creates unpredictable dynamics that can manifest as collapse, oscillation, or intermittent degradation depending on task conditions. Before revising the selective verification section, I should insert a new subsection on the factorial experiment design to properly structure the empirical validation. I'm refining the selective verification section to be more concise. The first paragraph already captures the key idea—a binary verify/skip decision with action-change rewards—and notes it's not yet implemented, so that stays. I'll trim the second paragraph to remove the detailed formula and citation, keeping just the essential concept while staying under 100 words total.

Now I'm thinking about the implementation order for these edits. Since they're all in the same section but don't overlap, I can work through them sequentially to avoid any conflicts in the file.

For the next point about episode-level training being a prerequisite: the key insight is that you need a competent base agent before you can train a selective verification policy, and step-independent training won't get you there. That's the core constraint I should focus on. I'm checking the M2 section for "ceiling" language that needs updating—line 68 references "the ceiling set by Mechanism 1" which I've already flagged. I also notice the cumulative degradation framing in lines 67-68 with phrases like "progressively erodes" and "repeated wrong-sign gradient updates" that should shift toward describing training instability with high variance and potential collapse instead.

Looking at the paragraph revision, I see the old version emphasizes predictable degradation proportional to misattribution severity, but the new framing should focus on how wrong-sign gradients corrupt the optimization signal and destabilize training rather than producing measurable degradation. The sentence appears to cut off mid-thought, so I'll finish it naturally: the instability manifests as unpredictable oscillations or collapse rather than smooth degradation.

Now I'm checking the word count for section 3.4—it's currently around 600+ words but the task specifies ~500, so I need to be strategic about consolidating these edits without losing the core framing shift. I also notice there's a partial note about M1 that got cut off, so I'll need to circle back to that once I finalize the main paragraph changes. 完成第三个预测：当采用 episode-level 的方法消除这两个机制后，模型能够实现稳定学习。同时要避免量化分解两个机制各自贡献的陷阱——不能声称某个机制贡献了具体的百分比或数值改进。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "143579cf-51ce-4468-8976-3c5e3ebea76d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013vZRpRmVQe9b7SKtdJ515F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14830,
      "cache_read_input_tokens": 26714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14830
      },
      "output_tokens": 8,
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

_source line 13_

Now I have all context. I'll make the edits to §3.4 (reframe M1/M2 per D073), insert new §3.6 (Factorial Design), and shorten the current §3.6 into §3.7.

Starting with the §3.4 intro paragraph.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "56268bbc-a63b-4b4e-a9c5-01ea05c47bda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013vZRpRmVQe9b7SKtdJ515F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14830,
      "cache_read_input_tokens": 26714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14830
      },
      "output_tokens": 8,
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

_source line 14_

<details open><summary>🔧 Tool call — Edit · `toolu_013Z1WNusUtDz7PLk3esB8iY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "old_string": "We identify two mechanisms operating at different layers that jointly cause catastrophic failure under step-independent training. The first operates at the inference layer, establishing a structural performance ceiling by restricting the model's observable context. The second operates at the training layer, actively degrading performance below this ceiling through systematic gradient errors that accumulate over optimization steps. We predict a two-phase collapse under step-independent training: strategic failure (task success drops) while action formatting initially remains intact, followed by complete collapse of both capabilities as wrong-direction gradients accumulate. Section~\\ref{sec:experiments} validates this prediction empirically.",
  "new_string": "We identify two mechanisms operating at different layers that jointly cause training failure under step-independent optimization. The first operates at the inference layer: by restricting the model's observable context, it destroys the policy's ability to generalize to tasks that require cross-step reasoning. The second operates at the training layer: systematic gradient sign errors destabilize the optimization process, producing high-variance training dynamics that range from catastrophic collapse to erratic oscillation. Together, these mechanisms predict three distinct training regimes depending on which mechanism dominates: (a) monotonic collapse when both mechanisms are severe, (b) oscillation followed by degradation when sign misattribution is the primary driver, and (c) stable learning when episode-level training eliminates both. Section~\\ref{sec:experiments} validates these predictions empirically."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "cc38ef4c-bc55-4c94-b3b8-7fd4e57661d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013vZRpRmVQe9b7SKtdJ515F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14830,
      "cache_read_input_tokens": 26714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14830
      },
      "output_tokens": 8,
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

_source line 15 · 2026-05-18T12:08:45.100Z_

<details><summary>↩ Tool result · `toolu_013Z1WNusUtDz7PLk3esB8iY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "c01e445c-a205-4057-be1a-9d32b63dcb81",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "oldString": "We identify two mechanisms operating at different layers that jointly cause catastrophic failure under step-independent training. The first operates at the inference layer, establishing a structural performance ceiling by restricting the model's observable context. The second operates at the training layer, actively degrading performance below this ceiling through systematic gradient errors that accumulate over optimization steps. We predict a two-phase collapse under step-independent training: strategic failure (task success drops) while action formatting initially remains intact, followed by complete collapse of both capabilities as wrong-direction gradients accumulate. Section~\\ref{sec:experiments} validates this prediction empirically.",
    "newString": "We identify two mechanisms operating at different layers that jointly cause training failure under step-independent optimization. The first operates at the inference layer: by restricting the model's observable context, it destroys the policy's ability to generalize to tasks that require cross-step reasoning. The second operates at the training layer: systematic gradient sign errors destabilize the optimization process, producing high-variance training dynamics that range from catastrophic collapse to erratic oscillation. Together, these mechanisms predict three distinct training regimes depending on which mechanism dominates: (a) monotonic collapse when both mechanisms are severe, (b) oscillation followed by degradation when sign misattribution is the primary driver, and (c) stable learning when episode-level training eliminates both. Section~\\ref{sec:experiments} validates these predictions empirically.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:problem_formulation}\n\nWe formalize the multi-turn interactive agent as a Partially Observable Markov Decision Process (POMDP) $\\mathcal{M} = (\\mathcal{S}, \\mathcal{A}, \\mathcal{O}, P, \\Omega, R, \\gamma)$, where $\\mathcal{S}$ is the state space of the environment, $\\mathcal{A}$ is the action space (natural language commands), $\\mathcal{O}$ is the observation space (textual feedback from the environment), $P: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathcal{S}$ is the transition function, $\\Omega: \\mathcal{S} \\rightarrow \\mathcal{O}$ is the observation function, $R$ is the reward function, and $\\gamma \\in [0,1]$ is a discount factor. The agent policy $\\pi_\\phi(a_t \\mid h_t)$ generates actions conditioned on the interaction history $h_t = (o_1, a_1, o_2, a_2, \\ldots, o_t)$, where $\\phi$ denotes the policy parameters. An episode consists of $T$ interaction steps, terminating with a binary reward $R \\in \\{0, r_+\\}$ that indicates task success or failure.\n\nIn practice, multi-turn episodes can span 50 or more interaction steps, each containing hundreds of tokens. Training a language model policy on the full history $h_T$ is computationally expensive and often exceeds the model's context length. This motivates the \\textbf{step-independent windowing} approach: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, and each window is optimized independently with its own computed return. Concretely, window $k$ observes only $(o_{(k-1)h+1}, a_{(k-1)h+1}, \\ldots, o_{kh})$ and receives a return $R_k$ derived from the episode outcome. This decomposition treats each window as a separate training sample, allowing standard context-length models to process the data. We show below that this seemingly practical choice introduces two failure mechanisms that cause catastrophic training collapse.\n\n\\subsection{GRPO for Language Agents}\n\\label{sec:grpo}\n\nGroup Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} is a bandit-style policy gradient method designed for language model alignment. Unlike PPO~\\cite{schulman2017ppo}, GRPO requires no critic network. For each task instance $x$, the algorithm samples $K$ rollouts $\\{y_1, \\ldots, y_K\\}$ from the current policy $\\pi_\\phi$. The advantage of each rollout is computed relative to the group:\n\\begin{equation}\n\\hat{A}_k = \\frac{R_k - \\mu}{\\sigma + \\epsilon}, \\quad \\mu = \\frac{1}{K}\\sum_{j=1}^K R_j, \\quad \\sigma = \\sqrt{\\frac{1}{K}\\sum_{j=1}^K (R_j - \\mu)^2}\n\\label{eq:grpo_advantage}\n\\end{equation}\nwhere $R_k$ is the return of rollout $k$. The policy gradient is:\n\\begin{equation}\n\\mathcal{L}_{\\text{GRPO}} = -\\frac{1}{K}\\sum_{k=1}^K \\hat{A}_k \\cdot \\min\\left(\\rho_k, \\text{clip}(\\rho_k, 1\\pm\\epsilon_c)\\right) + \\beta \\cdot D_{\\text{KL}}[\\pi_\\phi \\| \\pi_{\\text{ref}}]\n\\label{eq:grpo_loss}\n\\end{equation}\nwhere $\\rho_k = \\pi_\\phi(y_k \\mid x) / \\pi_{\\text{old}}(y_k \\mid x)$ is the importance ratio and $\\beta$ controls the KL penalty against a reference policy $\\pi_{\\text{ref}}$. GRPO is \\textit{episode-level by design}: each rollout $y_k$ is a complete generation with a single return $R_k$ and a single advantage $\\hat{A}_k$. There is no inherent temporal discounting within the algorithm.\n\n\\subsection{Step-Independent Implementation in Multi-Turn Agents}\n\\label{sec:step_independent}\n\nWhen adapting GRPO for multi-turn interactive tasks, agent training frameworks face a mismatch between GRPO's episode-level design and the practical constraints of long trajectories. The RAGEN framework~\\cite{ragen2025} addresses this by introducing step-independent training: each $h$-step window becomes an independent GRPO sample with a discounted return derived from the episode outcome.\n\nSpecifically, for an episode of $T$ steps with binary outcome $R_{\\text{episode}} \\in \\{0, r_+\\}$, the return assigned to window $k$ (covering steps $(k-1)h+1$ through $kh$) is computed as:\n\\begin{equation}\nR_k = \\gamma^{(N - k)} \\cdot R_{\\text{episode}}\n\\label{eq:step_return}\n\\end{equation}\nwhere $N = \\lceil T/h \\rceil$ is the total number of windows in the episode and $\\gamma$ is a discount factor (typically 0.95). In practice, intermediate step penalties (e.g., invalid action penalties) contribute additional terms to $R_k$. Our analysis focuses on the dominant component: the discounted terminal reward. Section~\\ref{sec:sign_verification} empirically validates that advantage sign remains episode-outcome-dominated even in the presence of per-step penalties. Each window is then treated as an independent sample in the GRPO optimization and receives its own group-normalized advantage $\\hat{A}_k$ via Equation~\\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $N$.\n\nThis design choice is motivated by three practical constraints. First, full trajectories of 50+ turns with hundreds of tokens per turn exceed typical context length limits (2048 or 4096 tokens for smaller models). Second, treating each window independently multiplies the effective batch size, improving GPU utilization. Third, the framework inherits the token-level training paradigm common in language model optimization, where shorter sequences are the default.\\footnote{Implementation details are available in the open-source RAGEN codebase, specifically the step-discounted return computation module (\\texttt{compute\\_step\\_discounted\\_returns}).}\n\nDespite these practical motivations, step-independent training fundamentally alters the credit assignment structure. The following section analyzes two mechanisms through which this alteration causes training collapse.\n\n\\subsection{Dual Mechanism Analysis}\n\\label{sec:dual_mechanism}\n\nWe identify two mechanisms operating at different layers that jointly cause catastrophic failure under step-independent training. The first operates at the inference layer, establishing a structural performance ceiling by restricting the model's observable context. The second operates at the training layer, actively degrading performance below this ceiling through systematic gradient errors that accumulate over optimization steps. We predict a two-phase collapse under step-independent training: strategic failure (task success drops) while action formatting initially remains intact, followed by complete collapse of both capabilities as wrong-direction gradients accumulate. Section~\\ref{sec:experiments} validates this prediction empirically.\n\n\\subsubsection{Mechanism 1: Policy Information Loss}\n\\label{sec:m1_information_loss}\n\nStep-independent training truncates context at both the inference and training layers. At inference time, the policy $\\pi_\\phi(a_t \\mid h_{\\text{window}_k})$ generates actions conditioned on only the local $h$-step history, losing access to observations and actions from earlier windows. At the training layer, the optimization target for each window is computed from this same truncated context, so cross-step strategies that require conditioning on earlier outcomes cannot be reinforced. Consider a household task requiring the agent to first explore a drawer (step 3), discover an object's location (step 4), then navigate to a countertop (step 8). With $h=2$, the window containing step 8 has no access to the exploration outcome from steps 3--4, neither at inference (the model cannot condition on it) nor at training (the gradient cannot credit it). The policy cannot learn the conditional strategy ``go to countertop \\textit{only if} the object was found in the drawer.''\n\nThis information loss establishes a structural performance ceiling that is constant across training: it reflects an architectural constraint on the representable strategy space rather than a learned failure. Different window sizes $h$ produce different ceilings, with smaller $h$ imposing tighter constraints on achievable task success. In our h-sweep experiments (Section~\\ref{sec:experiments}), initial evaluation performance varies across window sizes, confirming that the ceiling depends on the amount of available context.\n\nMore formally, let $\\pi^*$ denote the optimal policy for the full POMDP. The mutual information between $\\pi^*$ and the full history, $I(\\pi^*; h_T)$, captures the total information required for optimal decision-making. Under $h$-step windowing, each window's policy can access at most $I(\\pi^*; h_{\\text{window}_k})$. For tasks with sequential dependencies spanning more than $h$ steps, we have $I(\\pi^*; h_T) \\gg I(\\pi^*; h_{\\text{window}_k})$. The information gap grows with episode length $T$ and shrinks with window size $h$, predicting a performance cliff as $h$ decreases relative to the task's dependency horizon.\n\n\\subsubsection{Mechanism 2: Advantage Sign Misattribution}\n\\label{sec:m2_sign_misattribution}\n\nThe second mechanism operates at the training layer and, unlike Mechanism 1, is cumulative: its damage increases with each optimization step. Under step-independent training, each window receives a return $R_k = \\gamma^{(N-k)} \\cdot R_{\\text{episode}}$ (Equation~\\ref{eq:step_return}). After group normalization, the advantage $\\hat{A}_k$ has a \\textit{sign} determined primarily by whether the episode succeeded or failed, not by whether window $k$'s actions were locally good or bad.\n\nIn a failed episode ($R_{\\text{episode}} = 0$), all windows receive $R_k = 0$. If the group mean $\\mu > 0$ (due to other successful rollouts in the group), all windows in the failed episode receive negative advantages. This includes windows where the agent took locally correct actions (e.g., correctly identifying a target object). Conversely, in a successful episode, all windows receive positive advantages, including windows where the agent took suboptimal actions (e.g., unnecessary exploration steps that happened not to prevent eventual success).\n\nThe gradient direction for each window is determined by the sign of $\\hat{A}_k$:\n\\begin{equation}\n\\text{sign}(\\hat{A}_k) \\approx \\text{sign}(R_{\\text{episode}} - \\mu)\n\\label{eq:sign_correlation}\n\\end{equation}\nThis means the optimization either reinforces or suppresses \\textit{all} actions within a window based on the episode outcome, regardless of local action quality. Good actions in failed episodes are actively suppressed; bad actions in successful episodes are actively reinforced. Over many training steps, this systematic misattribution progressively erodes whatever inference capability the model retains under the truncated context. Even when the policy begins with non-trivial task competence within its $h$-step window, repeated wrong-sign gradient updates suppress this competence. Mechanism 2 should produce observable degradation below the ceiling set by Mechanism 1, with the rate of degradation proportional to the severity of sign misattribution. Section~\\ref{sec:experiments} confirms this prediction.\n\nA secondary effect compounds this problem. The discount factor $\\gamma^{(N-k)}$ introduces magnitude decay across window positions. For early windows in a long episode ($T=50$, $h=2$, $\\gamma=0.95$), the first window ($k=1$) retains $\\gamma^{N-1} = \\gamma^{24} \\approx 0.29$ of the terminal window's return. While this reduces the learning signal for early decisions, the sign error is fundamentally more harmful: magnitude decay merely slows convergence, while sign misattribution causes active divergence (Section~\\ref{sec:sign_fundamental}).\n\n\\subsection{Episode-Level Training}\n\\label{sec:episode_level}\n\nEpisode-level training resolves both failure mechanisms by treating the complete trajectory as a single GRPO sample. All tokens across all $T$ steps share one advantage $\\hat{A}$, computed from the episode return $R_{\\text{episode}}$ via group normalization over $K$ complete rollouts of the same task instance.\n\nThis design directly addresses Mechanism 1. The policy $\\pi_\\phi(a_t \\mid h_t)$ conditions on the full interaction history $h_t$ at every step $t$. Cross-step dependencies are preserved in the optimization target: the gradient for generating action $a_8$ (navigate to countertop) flows through the complete history including observations from steps 3--4 (drawer exploration outcome).\n\nEpisode-level training also eliminates Mechanism 2. Because there is no window-level return assignment, there is no opportunity for sign misattribution between windows. The single advantage $\\hat{A}$ applies uniformly to the entire trajectory. While this means per-step credit assignment remains coarse (all steps in a successful episode are equally reinforced), it avoids the worse failure mode of \\textit{systematically incorrect} credit assignment. The distinction is critical: uniform reinforcement of a successful trajectory preserves good sub-strategies within it, whereas window-level sign errors actively destroy them.\n\nThe trade-off is computational. Episode-level training requires processing the full sequence length ($T$ steps $\\times$ tokens-per-step) in a single forward and backward pass. For $T=50$ and 100 tokens per step, this amounts to 5000-token sequences, which fits within the capacity of modern architectures but increases memory and compute relative to $h$-step windows. In our experiments (Section~\\ref{sec:experiments}), this overhead is modest compared to the catastrophic failure avoided.\n\nEpisode-level training is, in fact, the natural application of GRPO to multi-turn settings. GRPO was designed as an episode-level algorithm where each rollout receives one return and one advantage. Step-independent training is the deviation from this design, introduced by framework implementation choices rather than algorithmic motivation. Our analysis reveals that this deviation carries hidden costs that become catastrophic for long-horizon interactive tasks.\n\n\\subsection{Selective Verification via Action-Change Reward}\n\\label{sec:selective_verification}\n\nThe credit assignment analysis above focuses on training a competent base agent. We outline here a proposed design for a downstream application: selective verification. This component has not been implemented in the current work and is intended as a direction for future investigation.\n\nInteractive agents benefit from self-verification (re-evaluating their planned action before execution), but empirical analysis shows that over 90\\% of verification instances are confirmatory (the agent does not change its action after checking)~\\cite{long2026selfverification}. Training the agent to verify selectively, only when verification is likely to be informative, could reduce computational cost without sacrificing task performance.\n\nWe formulate selective verification as a binary decision at each step $t$: the agent outputs a verify token $v_t \\in \\{\\texttt{VERIFY}, \\texttt{SKIP}\\}$ before generating its action $a_t$. When $v_t = \\texttt{VERIFY}$, the agent generates a verification rationale and may revise its action; when $v_t = \\texttt{SKIP}$, the agent proceeds directly. The reward signal for training the verification policy uses the action-change indicator:\n\\begin{equation}\n\\Delta a_t = \\mathbb{1}[a_t^{\\text{post-verify}} \\neq a_t^{\\text{pre-verify}}]\n\\label{eq:action_change}\n\\end{equation}\nas a measure of verification informativeness. A verification step that changes the action provided useful corrective information; one that confirms the original action was uninformative for that instance. The full formulation of the verification reward and training procedure is presented in Section~\\ref{sec:selective_experiments}. Episode-level training serves as a prerequisite for this component: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.",
    "structuredPatch": [
      {
        "oldStart": 42,
        "oldLines": 7,
        "newStart": 42,
        "newLines": 7,
        "lines": [
          " \\subsection{Dual Mechanism Analysis}",
          " \\label{sec:dual_mechanism}",
          " ",
          "-We identify two mechanisms operating at different layers that jointly cause catastrophic failure under step-independent training. The first operates at the inference layer, establishing a structural performance ceiling by restricting the model's observable context. The second operates at the training layer, actively degrading performance below this ceiling through systematic gradient errors that accumulate over optimization steps. We predict a two-phase collapse under step-independent training: strategic failure (task success drops) while action formatting initially remains intact, followed by complete collapse of both capabilities as wrong-direction gradients accumulate. Section~\\ref{sec:experiments} validates this prediction empirically.",
          "+We identify two mechanisms operating at different layers that jointly cause training failure under step-independent optimization. The first operates at the inference layer: by restricting the model's observable context, it destroys the policy's ability to generalize to tasks that require cross-step reasoning. The second operates at the training layer: systematic gradient sign errors destabilize the optimization process, producing high-variance training dynamics that range from catastrophic collapse to erratic oscillation. Together, these mechanisms predict three distinct training regimes depending on which mechanism dominates: (a) monotonic collapse when both mechanisms are severe, (b) oscillation followed by degradation when sign misattribution is the primary driver, and (c) stable learning when episode-level training eliminates both. Section~\\ref{sec:experiments} validates these predictions empirically.",
          " ",
          " \\subsubsection{Mechanism 1: Policy Information Loss}",
          " \\label{sec:m1_information_loss}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Edit · `toolu_01GcM6eeC2ZQBwQFjq1WHueL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "old_string": "This information loss establishes a structural performance ceiling that is constant across training: it reflects an architectural constraint on the representable strategy space rather than a learned failure. Different window sizes $h$ produce different ceilings, with smaller $h$ imposing tighter constraints on achievable task success. In our h-sweep experiments (Section~\\ref{sec:experiments}), initial evaluation performance varies across window sizes, confirming that the ceiling depends on the amount of available context.",
  "new_string": "This information loss destroys the policy's ability to generalize beyond local, single-window strategies. The model may learn to produce valid actions within its observable context, but it cannot acquire conditional strategies that depend on outcomes from earlier steps. The constraint is structural: no amount of training can recover information that is absent from the input. Different window sizes $h$ impose different degrees of information loss, with smaller $h$ restricting the representable strategy space more severely. In our h-sweep experiments (Section~\\ref{sec:experiments}), initial evaluation performance varies across window sizes, reflecting the direct relationship between available context and the policy's generalization capacity."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "b91fd8f3-a760-4257-bfb8-f834652eb0b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DgDwq6wTMj2i674eXDVMUe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7115,
      "cache_read_input_tokens": 41544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7115
      },
      "output_tokens": 67,
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

_source line 17 · 2026-05-18T12:08:50.583Z_

<details><summary>↩ Tool result · `toolu_01GcM6eeC2ZQBwQFjq1WHueL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "57170dce-b498-4552-b070-6fba61843244",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "oldString": "This information loss establishes a structural performance ceiling that is constant across training: it reflects an architectural constraint on the representable strategy space rather than a learned failure. Different window sizes $h$ produce different ceilings, with smaller $h$ imposing tighter constraints on achievable task success. In our h-sweep experiments (Section~\\ref{sec:experiments}), initial evaluation performance varies across window sizes, confirming that the ceiling depends on the amount of available context.",
    "newString": "This information loss destroys the policy's ability to generalize beyond local, single-window strategies. The model may learn to produce valid actions within its observable context, but it cannot acquire conditional strategies that depend on outcomes from earlier steps. The constraint is structural: no amount of training can recover information that is absent from the input. Different window sizes $h$ impose different degrees of information loss, with smaller $h$ restricting the representable strategy space more severely. In our h-sweep experiments (Section~\\ref{sec:experiments}), initial evaluation performance varies across window sizes, reflecting the direct relationship between available context and the policy's generalization capacity.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:problem_formulation}\n\nWe formalize the multi-turn interactive agent as a Partially Observable Markov Decision Process (POMDP) $\\mathcal{M} = (\\mathcal{S}, \\mathcal{A}, \\mathcal{O}, P, \\Omega, R, \\gamma)$, where $\\mathcal{S}$ is the state space of the environment, $\\mathcal{A}$ is the action space (natural language commands), $\\mathcal{O}$ is the observation space (textual feedback from the environment), $P: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathcal{S}$ is the transition function, $\\Omega: \\mathcal{S} \\rightarrow \\mathcal{O}$ is the observation function, $R$ is the reward function, and $\\gamma \\in [0,1]$ is a discount factor. The agent policy $\\pi_\\phi(a_t \\mid h_t)$ generates actions conditioned on the interaction history $h_t = (o_1, a_1, o_2, a_2, \\ldots, o_t)$, where $\\phi$ denotes the policy parameters. An episode consists of $T$ interaction steps, terminating with a binary reward $R \\in \\{0, r_+\\}$ that indicates task success or failure.\n\nIn practice, multi-turn episodes can span 50 or more interaction steps, each containing hundreds of tokens. Training a language model policy on the full history $h_T$ is computationally expensive and often exceeds the model's context length. This motivates the \\textbf{step-independent windowing} approach: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, and each window is optimized independently with its own computed return. Concretely, window $k$ observes only $(o_{(k-1)h+1}, a_{(k-1)h+1}, \\ldots, o_{kh})$ and receives a return $R_k$ derived from the episode outcome. This decomposition treats each window as a separate training sample, allowing standard context-length models to process the data. We show below that this seemingly practical choice introduces two failure mechanisms that cause catastrophic training collapse.\n\n\\subsection{GRPO for Language Agents}\n\\label{sec:grpo}\n\nGroup Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} is a bandit-style policy gradient method designed for language model alignment. Unlike PPO~\\cite{schulman2017ppo}, GRPO requires no critic network. For each task instance $x$, the algorithm samples $K$ rollouts $\\{y_1, \\ldots, y_K\\}$ from the current policy $\\pi_\\phi$. The advantage of each rollout is computed relative to the group:\n\\begin{equation}\n\\hat{A}_k = \\frac{R_k - \\mu}{\\sigma + \\epsilon}, \\quad \\mu = \\frac{1}{K}\\sum_{j=1}^K R_j, \\quad \\sigma = \\sqrt{\\frac{1}{K}\\sum_{j=1}^K (R_j - \\mu)^2}\n\\label{eq:grpo_advantage}\n\\end{equation}\nwhere $R_k$ is the return of rollout $k$. The policy gradient is:\n\\begin{equation}\n\\mathcal{L}_{\\text{GRPO}} = -\\frac{1}{K}\\sum_{k=1}^K \\hat{A}_k \\cdot \\min\\left(\\rho_k, \\text{clip}(\\rho_k, 1\\pm\\epsilon_c)\\right) + \\beta \\cdot D_{\\text{KL}}[\\pi_\\phi \\| \\pi_{\\text{ref}}]\n\\label{eq:grpo_loss}\n\\end{equation}\nwhere $\\rho_k = \\pi_\\phi(y_k \\mid x) / \\pi_{\\text{old}}(y_k \\mid x)$ is the importance ratio and $\\beta$ controls the KL penalty against a reference policy $\\pi_{\\text{ref}}$. GRPO is \\textit{episode-level by design}: each rollout $y_k$ is a complete generation with a single return $R_k$ and a single advantage $\\hat{A}_k$. There is no inherent temporal discounting within the algorithm.\n\n\\subsection{Step-Independent Implementation in Multi-Turn Agents}\n\\label{sec:step_independent}\n\nWhen adapting GRPO for multi-turn interactive tasks, agent training frameworks face a mismatch between GRPO's episode-level design and the practical constraints of long trajectories. The RAGEN framework~\\cite{ragen2025} addresses this by introducing step-independent training: each $h$-step window becomes an independent GRPO sample with a discounted return derived from the episode outcome.\n\nSpecifically, for an episode of $T$ steps with binary outcome $R_{\\text{episode}} \\in \\{0, r_+\\}$, the return assigned to window $k$ (covering steps $(k-1)h+1$ through $kh$) is computed as:\n\\begin{equation}\nR_k = \\gamma^{(N - k)} \\cdot R_{\\text{episode}}\n\\label{eq:step_return}\n\\end{equation}\nwhere $N = \\lceil T/h \\rceil$ is the total number of windows in the episode and $\\gamma$ is a discount factor (typically 0.95). In practice, intermediate step penalties (e.g., invalid action penalties) contribute additional terms to $R_k$. Our analysis focuses on the dominant component: the discounted terminal reward. Section~\\ref{sec:sign_verification} empirically validates that advantage sign remains episode-outcome-dominated even in the presence of per-step penalties. Each window is then treated as an independent sample in the GRPO optimization and receives its own group-normalized advantage $\\hat{A}_k$ via Equation~\\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $N$.\n\nThis design choice is motivated by three practical constraints. First, full trajectories of 50+ turns with hundreds of tokens per turn exceed typical context length limits (2048 or 4096 tokens for smaller models). Second, treating each window independently multiplies the effective batch size, improving GPU utilization. Third, the framework inherits the token-level training paradigm common in language model optimization, where shorter sequences are the default.\\footnote{Implementation details are available in the open-source RAGEN codebase, specifically the step-discounted return computation module (\\texttt{compute\\_step\\_discounted\\_returns}).}\n\nDespite these practical motivations, step-independent training fundamentally alters the credit assignment structure. The following section analyzes two mechanisms through which this alteration causes training collapse.\n\n\\subsection{Dual Mechanism Analysis}\n\\label{sec:dual_mechanism}\n\nWe identify two mechanisms operating at different layers that jointly cause training failure under step-independent optimization. The first operates at the inference layer: by restricting the model's observable context, it destroys the policy's ability to generalize to tasks that require cross-step reasoning. The second operates at the training layer: systematic gradient sign errors destabilize the optimization process, producing high-variance training dynamics that range from catastrophic collapse to erratic oscillation. Together, these mechanisms predict three distinct training regimes depending on which mechanism dominates: (a) monotonic collapse when both mechanisms are severe, (b) oscillation followed by degradation when sign misattribution is the primary driver, and (c) stable learning when episode-level training eliminates both. Section~\\ref{sec:experiments} validates these predictions empirically.\n\n\\subsubsection{Mechanism 1: Policy Information Loss}\n\\label{sec:m1_information_loss}\n\nStep-independent training truncates context at both the inference and training layers. At inference time, the policy $\\pi_\\phi(a_t \\mid h_{\\text{window}_k})$ generates actions conditioned on only the local $h$-step history, losing access to observations and actions from earlier windows. At the training layer, the optimization target for each window is computed from this same truncated context, so cross-step strategies that require conditioning on earlier outcomes cannot be reinforced. Consider a household task requiring the agent to first explore a drawer (step 3), discover an object's location (step 4), then navigate to a countertop (step 8). With $h=2$, the window containing step 8 has no access to the exploration outcome from steps 3--4, neither at inference (the model cannot condition on it) nor at training (the gradient cannot credit it). The policy cannot learn the conditional strategy ``go to countertop \\textit{only if} the object was found in the drawer.''\n\nThis information loss establishes a structural performance ceiling that is constant across training: it reflects an architectural constraint on the representable strategy space rather than a learned failure. Different window sizes $h$ produce different ceilings, with smaller $h$ imposing tighter constraints on achievable task success. In our h-sweep experiments (Section~\\ref{sec:experiments}), initial evaluation performance varies across window sizes, confirming that the ceiling depends on the amount of available context.\n\nMore formally, let $\\pi^*$ denote the optimal policy for the full POMDP. The mutual information between $\\pi^*$ and the full history, $I(\\pi^*; h_T)$, captures the total information required for optimal decision-making. Under $h$-step windowing, each window's policy can access at most $I(\\pi^*; h_{\\text{window}_k})$. For tasks with sequential dependencies spanning more than $h$ steps, we have $I(\\pi^*; h_T) \\gg I(\\pi^*; h_{\\text{window}_k})$. The information gap grows with episode length $T$ and shrinks with window size $h$, predicting a performance cliff as $h$ decreases relative to the task's dependency horizon.\n\n\\subsubsection{Mechanism 2: Advantage Sign Misattribution}\n\\label{sec:m2_sign_misattribution}\n\nThe second mechanism operates at the training layer and, unlike Mechanism 1, is cumulative: its damage increases with each optimization step. Under step-independent training, each window receives a return $R_k = \\gamma^{(N-k)} \\cdot R_{\\text{episode}}$ (Equation~\\ref{eq:step_return}). After group normalization, the advantage $\\hat{A}_k$ has a \\textit{sign} determined primarily by whether the episode succeeded or failed, not by whether window $k$'s actions were locally good or bad.\n\nIn a failed episode ($R_{\\text{episode}} = 0$), all windows receive $R_k = 0$. If the group mean $\\mu > 0$ (due to other successful rollouts in the group), all windows in the failed episode receive negative advantages. This includes windows where the agent took locally correct actions (e.g., correctly identifying a target object). Conversely, in a successful episode, all windows receive positive advantages, including windows where the agent took suboptimal actions (e.g., unnecessary exploration steps that happened not to prevent eventual success).\n\nThe gradient direction for each window is determined by the sign of $\\hat{A}_k$:\n\\begin{equation}\n\\text{sign}(\\hat{A}_k) \\approx \\text{sign}(R_{\\text{episode}} - \\mu)\n\\label{eq:sign_correlation}\n\\end{equation}\nThis means the optimization either reinforces or suppresses \\textit{all} actions within a window based on the episode outcome, regardless of local action quality. Good actions in failed episodes are actively suppressed; bad actions in successful episodes are actively reinforced. Over many training steps, this systematic misattribution progressively erodes whatever inference capability the model retains under the truncated context. Even when the policy begins with non-trivial task competence within its $h$-step window, repeated wrong-sign gradient updates suppress this competence. Mechanism 2 should produce observable degradation below the ceiling set by Mechanism 1, with the rate of degradation proportional to the severity of sign misattribution. Section~\\ref{sec:experiments} confirms this prediction.\n\nA secondary effect compounds this problem. The discount factor $\\gamma^{(N-k)}$ introduces magnitude decay across window positions. For early windows in a long episode ($T=50$, $h=2$, $\\gamma=0.95$), the first window ($k=1$) retains $\\gamma^{N-1} = \\gamma^{24} \\approx 0.29$ of the terminal window's return. While this reduces the learning signal for early decisions, the sign error is fundamentally more harmful: magnitude decay merely slows convergence, while sign misattribution causes active divergence (Section~\\ref{sec:sign_fundamental}).\n\n\\subsection{Episode-Level Training}\n\\label{sec:episode_level}\n\nEpisode-level training resolves both failure mechanisms by treating the complete trajectory as a single GRPO sample. All tokens across all $T$ steps share one advantage $\\hat{A}$, computed from the episode return $R_{\\text{episode}}$ via group normalization over $K$ complete rollouts of the same task instance.\n\nThis design directly addresses Mechanism 1. The policy $\\pi_\\phi(a_t \\mid h_t)$ conditions on the full interaction history $h_t$ at every step $t$. Cross-step dependencies are preserved in the optimization target: the gradient for generating action $a_8$ (navigate to countertop) flows through the complete history including observations from steps 3--4 (drawer exploration outcome).\n\nEpisode-level training also eliminates Mechanism 2. Because there is no window-level return assignment, there is no opportunity for sign misattribution between windows. The single advantage $\\hat{A}$ applies uniformly to the entire trajectory. While this means per-step credit assignment remains coarse (all steps in a successful episode are equally reinforced), it avoids the worse failure mode of \\textit{systematically incorrect} credit assignment. The distinction is critical: uniform reinforcement of a successful trajectory preserves good sub-strategies within it, whereas window-level sign errors actively destroy them.\n\nThe trade-off is computational. Episode-level training requires processing the full sequence length ($T$ steps $\\times$ tokens-per-step) in a single forward and backward pass. For $T=50$ and 100 tokens per step, this amounts to 5000-token sequences, which fits within the capacity of modern architectures but increases memory and compute relative to $h$-step windows. In our experiments (Section~\\ref{sec:experiments}), this overhead is modest compared to the catastrophic failure avoided.\n\nEpisode-level training is, in fact, the natural application of GRPO to multi-turn settings. GRPO was designed as an episode-level algorithm where each rollout receives one return and one advantage. Step-independent training is the deviation from this design, introduced by framework implementation choices rather than algorithmic motivation. Our analysis reveals that this deviation carries hidden costs that become catastrophic for long-horizon interactive tasks.\n\n\\subsection{Selective Verification via Action-Change Reward}\n\\label{sec:selective_verification}\n\nThe credit assignment analysis above focuses on training a competent base agent. We outline here a proposed design for a downstream application: selective verification. This component has not been implemented in the current work and is intended as a direction for future investigation.\n\nInteractive agents benefit from self-verification (re-evaluating their planned action before execution), but empirical analysis shows that over 90\\% of verification instances are confirmatory (the agent does not change its action after checking)~\\cite{long2026selfverification}. Training the agent to verify selectively, only when verification is likely to be informative, could reduce computational cost without sacrificing task performance.\n\nWe formulate selective verification as a binary decision at each step $t$: the agent outputs a verify token $v_t \\in \\{\\texttt{VERIFY}, \\texttt{SKIP}\\}$ before generating its action $a_t$. When $v_t = \\texttt{VERIFY}$, the agent generates a verification rationale and may revise its action; when $v_t = \\texttt{SKIP}$, the agent proceeds directly. The reward signal for training the verification policy uses the action-change indicator:\n\\begin{equation}\n\\Delta a_t = \\mathbb{1}[a_t^{\\text{post-verify}} \\neq a_t^{\\text{pre-verify}}]\n\\label{eq:action_change}\n\\end{equation}\nas a measure of verification informativeness. A verification step that changes the action provided useful corrective information; one that confirms the original action was uninformative for that instance. The full formulation of the verification reward and training procedure is presented in Section~\\ref{sec:selective_experiments}. Episode-level training serves as a prerequisite for this component: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.",
    "structuredPatch": [
      {
        "oldStart": 49,
        "oldLines": 7,
        "newStart": 49,
        "newLines": 7,
        "lines": [
          " ",
          " Step-independent training truncates context at both the inference and training layers. At inference time, the policy $\\pi_\\phi(a_t \\mid h_{\\text{window}_k})$ generates actions conditioned on only the local $h$-step history, losing access to observations and actions from earlier windows. At the training layer, the optimization target for each window is computed from this same truncated context, so cross-step strategies that require conditioning on earlier outcomes cannot be reinforced. Consider a household task requiring the agent to first explore a drawer (step 3), discover an object's location (step 4), then navigate to a countertop (step 8). With $h=2$, the window containing step 8 has no access to the exploration outcome from steps 3--4, neither at inference (the model cannot condition on it) nor at training (the gradient cannot credit it). The policy cannot learn the conditional strategy ``go to countertop \\textit{only if} the object was found in the drawer.''",
          " ",
          "-This information loss establishes a structural performance ceiling that is constant across training: it reflects an architectural constraint on the representable strategy space rather than a learned failure. Different window sizes $h$ produce different ceilings, with smaller $h$ imposing tighter constraints on achievable task success. In our h-sweep experiments (Section~\\ref{sec:experiments}), initial evaluation performance varies across window sizes, confirming that the ceiling depends on the amount of available context.",
          "+This information loss destroys the policy's ability to generalize beyond local, single-window strategies. The model may learn to produce valid actions within its observable context, but it cannot acquire conditional strategies that depend on outcomes from earlier steps. The constraint is structural: no amount of training can recover information that is absent from the input. Different window sizes $h$ impose different degrees of information loss, with smaller $h$ restricting the representable strategy space more severely. In our h-sweep experiments (Section~\\ref{sec:experiments}), initial evaluation performance varies across window sizes, reflecting the direct relationship between available context and the policy's generalization capacity.",
          " ",
          " More formally, let $\\pi^*$ denote the optimal policy for the full POMDP. The mutual information between $\\pi^*$ and the full history, $I(\\pi^*; h_T)$, captures the total information required for optimal decision-making. Under $h$-step windowing, each window's policy can access at most $I(\\pi^*; h_{\\text{window}_k})$. For tasks with sequential dependencies spanning more than $h$ steps, we have $I(\\pi^*; h_T) \\gg I(\\pi^*; h_{\\text{window}_k})$. The information gap grows with episode length $T$ and shrinks with window size $h$, predicting a performance cliff as $h$ decreases relative to the task's dependency horizon.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Edit · `toolu_011dFwHZmTwZ8UVAkuA95NtC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "old_string": "predicting a performance cliff as $h$ decreases relative to the task's dependency horizon.",
  "new_string": "predicting a generalization cliff as $h$ decreases relative to the task's dependency horizon."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "5e674b51-4e73-468e-a1e7-3545ba86affc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6JKkWxMLgrewhDVD59441",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 431,
      "cache_read_input_tokens": 48659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 431
      },
      "output_tokens": 72,
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

_source line 19 · 2026-05-18T12:08:54.290Z_

<details><summary>↩ Tool result · `toolu_011dFwHZmTwZ8UVAkuA95NtC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "9c234db1-5319-41fe-9963-45b3c588bee4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "oldString": "predicting a performance cliff as $h$ decreases relative to the task's dependency horizon.",
    "newString": "predicting a generalization cliff as $h$ decreases relative to the task's dependency horizon.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:problem_formulation}\n\nWe formalize the multi-turn interactive agent as a Partially Observable Markov Decision Process (POMDP) $\\mathcal{M} = (\\mathcal{S}, \\mathcal{A}, \\mathcal{O}, P, \\Omega, R, \\gamma)$, where $\\mathcal{S}$ is the state space of the environment, $\\mathcal{A}$ is the action space (natural language commands), $\\mathcal{O}$ is the observation space (textual feedback from the environment), $P: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathcal{S}$ is the transition function, $\\Omega: \\mathcal{S} \\rightarrow \\mathcal{O}$ is the observation function, $R$ is the reward function, and $\\gamma \\in [0,1]$ is a discount factor. The agent policy $\\pi_\\phi(a_t \\mid h_t)$ generates actions conditioned on the interaction history $h_t = (o_1, a_1, o_2, a_2, \\ldots, o_t)$, where $\\phi$ denotes the policy parameters. An episode consists of $T$ interaction steps, terminating with a binary reward $R \\in \\{0, r_+\\}$ that indicates task success or failure.\n\nIn practice, multi-turn episodes can span 50 or more interaction steps, each containing hundreds of tokens. Training a language model policy on the full history $h_T$ is computationally expensive and often exceeds the model's context length. This motivates the \\textbf{step-independent windowing} approach: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, and each window is optimized independently with its own computed return. Concretely, window $k$ observes only $(o_{(k-1)h+1}, a_{(k-1)h+1}, \\ldots, o_{kh})$ and receives a return $R_k$ derived from the episode outcome. This decomposition treats each window as a separate training sample, allowing standard context-length models to process the data. We show below that this seemingly practical choice introduces two failure mechanisms that cause catastrophic training collapse.\n\n\\subsection{GRPO for Language Agents}\n\\label{sec:grpo}\n\nGroup Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} is a bandit-style policy gradient method designed for language model alignment. Unlike PPO~\\cite{schulman2017ppo}, GRPO requires no critic network. For each task instance $x$, the algorithm samples $K$ rollouts $\\{y_1, \\ldots, y_K\\}$ from the current policy $\\pi_\\phi$. The advantage of each rollout is computed relative to the group:\n\\begin{equation}\n\\hat{A}_k = \\frac{R_k - \\mu}{\\sigma + \\epsilon}, \\quad \\mu = \\frac{1}{K}\\sum_{j=1}^K R_j, \\quad \\sigma = \\sqrt{\\frac{1}{K}\\sum_{j=1}^K (R_j - \\mu)^2}\n\\label{eq:grpo_advantage}\n\\end{equation}\nwhere $R_k$ is the return of rollout $k$. The policy gradient is:\n\\begin{equation}\n\\mathcal{L}_{\\text{GRPO}} = -\\frac{1}{K}\\sum_{k=1}^K \\hat{A}_k \\cdot \\min\\left(\\rho_k, \\text{clip}(\\rho_k, 1\\pm\\epsilon_c)\\right) + \\beta \\cdot D_{\\text{KL}}[\\pi_\\phi \\| \\pi_{\\text{ref}}]\n\\label{eq:grpo_loss}\n\\end{equation}\nwhere $\\rho_k = \\pi_\\phi(y_k \\mid x) / \\pi_{\\text{old}}(y_k \\mid x)$ is the importance ratio and $\\beta$ controls the KL penalty against a reference policy $\\pi_{\\text{ref}}$. GRPO is \\textit{episode-level by design}: each rollout $y_k$ is a complete generation with a single return $R_k$ and a single advantage $\\hat{A}_k$. There is no inherent temporal discounting within the algorithm.\n\n\\subsection{Step-Independent Implementation in Multi-Turn Agents}\n\\label{sec:step_independent}\n\nWhen adapting GRPO for multi-turn interactive tasks, agent training frameworks face a mismatch between GRPO's episode-level design and the practical constraints of long trajectories. The RAGEN framework~\\cite{ragen2025} addresses this by introducing step-independent training: each $h$-step window becomes an independent GRPO sample with a discounted return derived from the episode outcome.\n\nSpecifically, for an episode of $T$ steps with binary outcome $R_{\\text{episode}} \\in \\{0, r_+\\}$, the return assigned to window $k$ (covering steps $(k-1)h+1$ through $kh$) is computed as:\n\\begin{equation}\nR_k = \\gamma^{(N - k)} \\cdot R_{\\text{episode}}\n\\label{eq:step_return}\n\\end{equation}\nwhere $N = \\lceil T/h \\rceil$ is the total number of windows in the episode and $\\gamma$ is a discount factor (typically 0.95). In practice, intermediate step penalties (e.g., invalid action penalties) contribute additional terms to $R_k$. Our analysis focuses on the dominant component: the discounted terminal reward. Section~\\ref{sec:sign_verification} empirically validates that advantage sign remains episode-outcome-dominated even in the presence of per-step penalties. Each window is then treated as an independent sample in the GRPO optimization and receives its own group-normalized advantage $\\hat{A}_k$ via Equation~\\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $N$.\n\nThis design choice is motivated by three practical constraints. First, full trajectories of 50+ turns with hundreds of tokens per turn exceed typical context length limits (2048 or 4096 tokens for smaller models). Second, treating each window independently multiplies the effective batch size, improving GPU utilization. Third, the framework inherits the token-level training paradigm common in language model optimization, where shorter sequences are the default.\\footnote{Implementation details are available in the open-source RAGEN codebase, specifically the step-discounted return computation module (\\texttt{compute\\_step\\_discounted\\_returns}).}\n\nDespite these practical motivations, step-independent training fundamentally alters the credit assignment structure. The following section analyzes two mechanisms through which this alteration causes training collapse.\n\n\\subsection{Dual Mechanism Analysis}\n\\label{sec:dual_mechanism}\n\nWe identify two mechanisms operating at different layers that jointly cause training failure under step-independent optimization. The first operates at the inference layer: by restricting the model's observable context, it destroys the policy's ability to generalize to tasks that require cross-step reasoning. The second operates at the training layer: systematic gradient sign errors destabilize the optimization process, producing high-variance training dynamics that range from catastrophic collapse to erratic oscillation. Together, these mechanisms predict three distinct training regimes depending on which mechanism dominates: (a) monotonic collapse when both mechanisms are severe, (b) oscillation followed by degradation when sign misattribution is the primary driver, and (c) stable learning when episode-level training eliminates both. Section~\\ref{sec:experiments} validates these predictions empirically.\n\n\\subsubsection{Mechanism 1: Policy Information Loss}\n\\label{sec:m1_information_loss}\n\nStep-independent training truncates context at both the inference and training layers. At inference time, the policy $\\pi_\\phi(a_t \\mid h_{\\text{window}_k})$ generates actions conditioned on only the local $h$-step history, losing access to observations and actions from earlier windows. At the training layer, the optimization target for each window is computed from this same truncated context, so cross-step strategies that require conditioning on earlier outcomes cannot be reinforced. Consider a household task requiring the agent to first explore a drawer (step 3), discover an object's location (step 4), then navigate to a countertop (step 8). With $h=2$, the window containing step 8 has no access to the exploration outcome from steps 3--4, neither at inference (the model cannot condition on it) nor at training (the gradient cannot credit it). The policy cannot learn the conditional strategy ``go to countertop \\textit{only if} the object was found in the drawer.''\n\nThis information loss destroys the policy's ability to generalize beyond local, single-window strategies. The model may learn to produce valid actions within its observable context, but it cannot acquire conditional strategies that depend on outcomes from earlier steps. The constraint is structural: no amount of training can recover information that is absent from the input. Different window sizes $h$ impose different degrees of information loss, with smaller $h$ restricting the representable strategy space more severely. In our h-sweep experiments (Section~\\ref{sec:experiments}), initial evaluation performance varies across window sizes, reflecting the direct relationship between available context and the policy's generalization capacity.\n\nMore formally, let $\\pi^*$ denote the optimal policy for the full POMDP. The mutual information between $\\pi^*$ and the full history, $I(\\pi^*; h_T)$, captures the total information required for optimal decision-making. Under $h$-step windowing, each window's policy can access at most $I(\\pi^*; h_{\\text{window}_k})$. For tasks with sequential dependencies spanning more than $h$ steps, we have $I(\\pi^*; h_T) \\gg I(\\pi^*; h_{\\text{window}_k})$. The information gap grows with episode length $T$ and shrinks with window size $h$, predicting a performance cliff as $h$ decreases relative to the task's dependency horizon.\n\n\\subsubsection{Mechanism 2: Advantage Sign Misattribution}\n\\label{sec:m2_sign_misattribution}\n\nThe second mechanism operates at the training layer and, unlike Mechanism 1, is cumulative: its damage increases with each optimization step. Under step-independent training, each window receives a return $R_k = \\gamma^{(N-k)} \\cdot R_{\\text{episode}}$ (Equation~\\ref{eq:step_return}). After group normalization, the advantage $\\hat{A}_k$ has a \\textit{sign} determined primarily by whether the episode succeeded or failed, not by whether window $k$'s actions were locally good or bad.\n\nIn a failed episode ($R_{\\text{episode}} = 0$), all windows receive $R_k = 0$. If the group mean $\\mu > 0$ (due to other successful rollouts in the group), all windows in the failed episode receive negative advantages. This includes windows where the agent took locally correct actions (e.g., correctly identifying a target object). Conversely, in a successful episode, all windows receive positive advantages, including windows where the agent took suboptimal actions (e.g., unnecessary exploration steps that happened not to prevent eventual success).\n\nThe gradient direction for each window is determined by the sign of $\\hat{A}_k$:\n\\begin{equation}\n\\text{sign}(\\hat{A}_k) \\approx \\text{sign}(R_{\\text{episode}} - \\mu)\n\\label{eq:sign_correlation}\n\\end{equation}\nThis means the optimization either reinforces or suppresses \\textit{all} actions within a window based on the episode outcome, regardless of local action quality. Good actions in failed episodes are actively suppressed; bad actions in successful episodes are actively reinforced. Over many training steps, this systematic misattribution progressively erodes whatever inference capability the model retains under the truncated context. Even when the policy begins with non-trivial task competence within its $h$-step window, repeated wrong-sign gradient updates suppress this competence. Mechanism 2 should produce observable degradation below the ceiling set by Mechanism 1, with the rate of degradation proportional to the severity of sign misattribution. Section~\\ref{sec:experiments} confirms this prediction.\n\nA secondary effect compounds this problem. The discount factor $\\gamma^{(N-k)}$ introduces magnitude decay across window positions. For early windows in a long episode ($T=50$, $h=2$, $\\gamma=0.95$), the first window ($k=1$) retains $\\gamma^{N-1} = \\gamma^{24} \\approx 0.29$ of the terminal window's return. While this reduces the learning signal for early decisions, the sign error is fundamentally more harmful: magnitude decay merely slows convergence, while sign misattribution causes active divergence (Section~\\ref{sec:sign_fundamental}).\n\n\\subsection{Episode-Level Training}\n\\label{sec:episode_level}\n\nEpisode-level training resolves both failure mechanisms by treating the complete trajectory as a single GRPO sample. All tokens across all $T$ steps share one advantage $\\hat{A}$, computed from the episode return $R_{\\text{episode}}$ via group normalization over $K$ complete rollouts of the same task instance.\n\nThis design directly addresses Mechanism 1. The policy $\\pi_\\phi(a_t \\mid h_t)$ conditions on the full interaction history $h_t$ at every step $t$. Cross-step dependencies are preserved in the optimization target: the gradient for generating action $a_8$ (navigate to countertop) flows through the complete history including observations from steps 3--4 (drawer exploration outcome).\n\nEpisode-level training also eliminates Mechanism 2. Because there is no window-level return assignment, there is no opportunity for sign misattribution between windows. The single advantage $\\hat{A}$ applies uniformly to the entire trajectory. While this means per-step credit assignment remains coarse (all steps in a successful episode are equally reinforced), it avoids the worse failure mode of \\textit{systematically incorrect} credit assignment. The distinction is critical: uniform reinforcement of a successful trajectory preserves good sub-strategies within it, whereas window-level sign errors actively destroy them.\n\nThe trade-off is computational. Episode-level training requires processing the full sequence length ($T$ steps $\\times$ tokens-per-step) in a single forward and backward pass. For $T=50$ and 100 tokens per step, this amounts to 5000-token sequences, which fits within the capacity of modern architectures but increases memory and compute relative to $h$-step windows. In our experiments (Section~\\ref{sec:experiments}), this overhead is modest compared to the catastrophic failure avoided.\n\nEpisode-level training is, in fact, the natural application of GRPO to multi-turn settings. GRPO was designed as an episode-level algorithm where each rollout receives one return and one advantage. Step-independent training is the deviation from this design, introduced by framework implementation choices rather than algorithmic motivation. Our analysis reveals that this deviation carries hidden costs that become catastrophic for long-horizon interactive tasks.\n\n\\subsection{Selective Verification via Action-Change Reward}\n\\label{sec:selective_verification}\n\nThe credit assignment analysis above focuses on training a competent base agent. We outline here a proposed design for a downstream application: selective verification. This component has not been implemented in the current work and is intended as a direction for future investigation.\n\nInteractive agents benefit from self-verification (re-evaluating their planned action before execution), but empirical analysis shows that over 90\\% of verification instances are confirmatory (the agent does not change its action after checking)~\\cite{long2026selfverification}. Training the agent to verify selectively, only when verification is likely to be informative, could reduce computational cost without sacrificing task performance.\n\nWe formulate selective verification as a binary decision at each step $t$: the agent outputs a verify token $v_t \\in \\{\\texttt{VERIFY}, \\texttt{SKIP}\\}$ before generating its action $a_t$. When $v_t = \\texttt{VERIFY}$, the agent generates a verification rationale and may revise its action; when $v_t = \\texttt{SKIP}$, the agent proceeds directly. The reward signal for training the verification policy uses the action-change indicator:\n\\begin{equation}\n\\Delta a_t = \\mathbb{1}[a_t^{\\text{post-verify}} \\neq a_t^{\\text{pre-verify}}]\n\\label{eq:action_change}\n\\end{equation}\nas a measure of verification informativeness. A verification step that changes the action provided useful corrective information; one that confirms the original action was uninformative for that instance. The full formulation of the verification reward and training procedure is presented in Section~\\ref{sec:selective_experiments}. Episode-level training serves as a prerequisite for this component: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.",
    "structuredPatch": [
      {
        "oldStart": 51,
        "oldLines": 7,
        "newStart": 51,
        "newLines": 7,
        "lines": [
          " ",
          " This information loss destroys the policy's ability to generalize beyond local, single-window strategies. The model may learn to produce valid actions within its observable context, but it cannot acquire conditional strategies that depend on outcomes from earlier steps. The constraint is structural: no amount of training can recover information that is absent from the input. Different window sizes $h$ impose different degrees of information loss, with smaller $h$ restricting the representable strategy space more severely. In our h-sweep experiments (Section~\\ref{sec:experiments}), initial evaluation performance varies across window sizes, reflecting the direct relationship between available context and the policy's generalization capacity.",
          " ",
          "-More formally, let $\\pi^*$ denote the optimal policy for the full POMDP. The mutual information between $\\pi^*$ and the full history, $I(\\pi^*; h_T)$, captures the total information required for optimal decision-making. Under $h$-step windowing, each window's policy can access at most $I(\\pi^*; h_{\\text{window}_k})$. For tasks with sequential dependencies spanning more than $h$ steps, we have $I(\\pi^*; h_T) \\gg I(\\pi^*; h_{\\text{window}_k})$. The information gap grows with episode length $T$ and shrinks with window size $h$, predicting a performance cliff as $h$ decreases relative to the task's dependency horizon.",
          "+More formally, let $\\pi^*$ denote the optimal policy for the full POMDP. The mutual information between $\\pi^*$ and the full history, $I(\\pi^*; h_T)$, captures the total information required for optimal decision-making. Under $h$-step windowing, each window's policy can access at most $I(\\pi^*; h_{\\text{window}_k})$. For tasks with sequential dependencies spanning more than $h$ steps, we have $I(\\pi^*; h_T) \\gg I(\\pi^*; h_{\\text{window}_k})$. The information gap grows with episode length $T$ and shrinks with window size $h$, predicting a generalization cliff as $h$ decreases relative to the task's dependency horizon.",
          " ",
          " \\subsubsection{Mechanism 2: Advantage Sign Misattribution}",
          " \\label{sec:m2_sign_misattribution}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_01LzmuiHQRj67LgEgEDJMHDT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "old_string": "The second mechanism operates at the training layer and, unlike Mechanism 1, is cumulative: its damage increases with each optimization step.",
  "new_string": "The second mechanism operates at the training layer and, unlike Mechanism 1, directly disrupts the optimization process rather than constraining the representable strategy space."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "d34da6b8-032b-4eda-8a07-5e77b73fec40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A6gK7bDrp5WpPPu8RQgY2z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 238,
      "cache_read_input_tokens": 49090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 238
      },
      "output_tokens": 72,
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

_source line 21 · 2026-05-18T12:08:58.197Z_

<details><summary>↩ Tool result · `toolu_01LzmuiHQRj67LgEgEDJMHDT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "19474999-873a-44fb-bb62-c14aa3d9be30",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "oldString": "The second mechanism operates at the training layer and, unlike Mechanism 1, is cumulative: its damage increases with each optimization step.",
    "newString": "The second mechanism operates at the training layer and, unlike Mechanism 1, directly disrupts the optimization process rather than constraining the representable strategy space.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:problem_formulation}\n\nWe formalize the multi-turn interactive agent as a Partially Observable Markov Decision Process (POMDP) $\\mathcal{M} = (\\mathcal{S}, \\mathcal{A}, \\mathcal{O}, P, \\Omega, R, \\gamma)$, where $\\mathcal{S}$ is the state space of the environment, $\\mathcal{A}$ is the action space (natural language commands), $\\mathcal{O}$ is the observation space (textual feedback from the environment), $P: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathcal{S}$ is the transition function, $\\Omega: \\mathcal{S} \\rightarrow \\mathcal{O}$ is the observation function, $R$ is the reward function, and $\\gamma \\in [0,1]$ is a discount factor. The agent policy $\\pi_\\phi(a_t \\mid h_t)$ generates actions conditioned on the interaction history $h_t = (o_1, a_1, o_2, a_2, \\ldots, o_t)$, where $\\phi$ denotes the policy parameters. An episode consists of $T$ interaction steps, terminating with a binary reward $R \\in \\{0, r_+\\}$ that indicates task success or failure.\n\nIn practice, multi-turn episodes can span 50 or more interaction steps, each containing hundreds of tokens. Training a language model policy on the full history $h_T$ is computationally expensive and often exceeds the model's context length. This motivates the \\textbf{step-independent windowing} approach: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, and each window is optimized independently with its own computed return. Concretely, window $k$ observes only $(o_{(k-1)h+1}, a_{(k-1)h+1}, \\ldots, o_{kh})$ and receives a return $R_k$ derived from the episode outcome. This decomposition treats each window as a separate training sample, allowing standard context-length models to process the data. We show below that this seemingly practical choice introduces two failure mechanisms that cause catastrophic training collapse.\n\n\\subsection{GRPO for Language Agents}\n\\label{sec:grpo}\n\nGroup Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} is a bandit-style policy gradient method designed for language model alignment. Unlike PPO~\\cite{schulman2017ppo}, GRPO requires no critic network. For each task instance $x$, the algorithm samples $K$ rollouts $\\{y_1, \\ldots, y_K\\}$ from the current policy $\\pi_\\phi$. The advantage of each rollout is computed relative to the group:\n\\begin{equation}\n\\hat{A}_k = \\frac{R_k - \\mu}{\\sigma + \\epsilon}, \\quad \\mu = \\frac{1}{K}\\sum_{j=1}^K R_j, \\quad \\sigma = \\sqrt{\\frac{1}{K}\\sum_{j=1}^K (R_j - \\mu)^2}\n\\label{eq:grpo_advantage}\n\\end{equation}\nwhere $R_k$ is the return of rollout $k$. The policy gradient is:\n\\begin{equation}\n\\mathcal{L}_{\\text{GRPO}} = -\\frac{1}{K}\\sum_{k=1}^K \\hat{A}_k \\cdot \\min\\left(\\rho_k, \\text{clip}(\\rho_k, 1\\pm\\epsilon_c)\\right) + \\beta \\cdot D_{\\text{KL}}[\\pi_\\phi \\| \\pi_{\\text{ref}}]\n\\label{eq:grpo_loss}\n\\end{equation}\nwhere $\\rho_k = \\pi_\\phi(y_k \\mid x) / \\pi_{\\text{old}}(y_k \\mid x)$ is the importance ratio and $\\beta$ controls the KL penalty against a reference policy $\\pi_{\\text{ref}}$. GRPO is \\textit{episode-level by design}: each rollout $y_k$ is a complete generation with a single return $R_k$ and a single advantage $\\hat{A}_k$. There is no inherent temporal discounting within the algorithm.\n\n\\subsection{Step-Independent Implementation in Multi-Turn Agents}\n\\label{sec:step_independent}\n\nWhen adapting GRPO for multi-turn interactive tasks, agent training frameworks face a mismatch between GRPO's episode-level design and the practical constraints of long trajectories. The RAGEN framework~\\cite{ragen2025} addresses this by introducing step-independent training: each $h$-step window becomes an independent GRPO sample with a discounted return derived from the episode outcome.\n\nSpecifically, for an episode of $T$ steps with binary outcome $R_{\\text{episode}} \\in \\{0, r_+\\}$, the return assigned to window $k$ (covering steps $(k-1)h+1$ through $kh$) is computed as:\n\\begin{equation}\nR_k = \\gamma^{(N - k)} \\cdot R_{\\text{episode}}\n\\label{eq:step_return}\n\\end{equation}\nwhere $N = \\lceil T/h \\rceil$ is the total number of windows in the episode and $\\gamma$ is a discount factor (typically 0.95). In practice, intermediate step penalties (e.g., invalid action penalties) contribute additional terms to $R_k$. Our analysis focuses on the dominant component: the discounted terminal reward. Section~\\ref{sec:sign_verification} empirically validates that advantage sign remains episode-outcome-dominated even in the presence of per-step penalties. Each window is then treated as an independent sample in the GRPO optimization and receives its own group-normalized advantage $\\hat{A}_k$ via Equation~\\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $N$.\n\nThis design choice is motivated by three practical constraints. First, full trajectories of 50+ turns with hundreds of tokens per turn exceed typical context length limits (2048 or 4096 tokens for smaller models). Second, treating each window independently multiplies the effective batch size, improving GPU utilization. Third, the framework inherits the token-level training paradigm common in language model optimization, where shorter sequences are the default.\\footnote{Implementation details are available in the open-source RAGEN codebase, specifically the step-discounted return computation module (\\texttt{compute\\_step\\_discounted\\_returns}).}\n\nDespite these practical motivations, step-independent training fundamentally alters the credit assignment structure. The following section analyzes two mechanisms through which this alteration causes training collapse.\n\n\\subsection{Dual Mechanism Analysis}\n\\label{sec:dual_mechanism}\n\nWe identify two mechanisms operating at different layers that jointly cause training failure under step-independent optimization. The first operates at the inference layer: by restricting the model's observable context, it destroys the policy's ability to generalize to tasks that require cross-step reasoning. The second operates at the training layer: systematic gradient sign errors destabilize the optimization process, producing high-variance training dynamics that range from catastrophic collapse to erratic oscillation. Together, these mechanisms predict three distinct training regimes depending on which mechanism dominates: (a) monotonic collapse when both mechanisms are severe, (b) oscillation followed by degradation when sign misattribution is the primary driver, and (c) stable learning when episode-level training eliminates both. Section~\\ref{sec:experiments} validates these predictions empirically.\n\n\\subsubsection{Mechanism 1: Policy Information Loss}\n\\label{sec:m1_information_loss}\n\nStep-independent training truncates context at both the inference and training layers. At inference time, the policy $\\pi_\\phi(a_t \\mid h_{\\text{window}_k})$ generates actions conditioned on only the local $h$-step history, losing access to observations and actions from earlier windows. At the training layer, the optimization target for each window is computed from this same truncated context, so cross-step strategies that require conditioning on earlier outcomes cannot be reinforced. Consider a household task requiring the agent to first explore a drawer (step 3), discover an object's location (step 4), then navigate to a countertop (step 8). With $h=2$, the window containing step 8 has no access to the exploration outcome from steps 3--4, neither at inference (the model cannot condition on it) nor at training (the gradient cannot credit it). The policy cannot learn the conditional strategy ``go to countertop \\textit{only if} the object was found in the drawer.''\n\nThis information loss destroys the policy's ability to generalize beyond local, single-window strategies. The model may learn to produce valid actions within its observable context, but it cannot acquire conditional strategies that depend on outcomes from earlier steps. The constraint is structural: no amount of training can recover information that is absent from the input. Different window sizes $h$ impose different degrees of information loss, with smaller $h$ restricting the representable strategy space more severely. In our h-sweep experiments (Section~\\ref{sec:experiments}), initial evaluation performance varies across window sizes, reflecting the direct relationship between available context and the policy's generalization capacity.\n\nMore formally, let $\\pi^*$ denote the optimal policy for the full POMDP. The mutual information between $\\pi^*$ and the full history, $I(\\pi^*; h_T)$, captures the total information required for optimal decision-making. Under $h$-step windowing, each window's policy can access at most $I(\\pi^*; h_{\\text{window}_k})$. For tasks with sequential dependencies spanning more than $h$ steps, we have $I(\\pi^*; h_T) \\gg I(\\pi^*; h_{\\text{window}_k})$. The information gap grows with episode length $T$ and shrinks with window size $h$, predicting a generalization cliff as $h$ decreases relative to the task's dependency horizon.\n\n\\subsubsection{Mechanism 2: Advantage Sign Misattribution}\n\\label{sec:m2_sign_misattribution}\n\nThe second mechanism operates at the training layer and, unlike Mechanism 1, is cumulative: its damage increases with each optimization step. Under step-independent training, each window receives a return $R_k = \\gamma^{(N-k)} \\cdot R_{\\text{episode}}$ (Equation~\\ref{eq:step_return}). After group normalization, the advantage $\\hat{A}_k$ has a \\textit{sign} determined primarily by whether the episode succeeded or failed, not by whether window $k$'s actions were locally good or bad.\n\nIn a failed episode ($R_{\\text{episode}} = 0$), all windows receive $R_k = 0$. If the group mean $\\mu > 0$ (due to other successful rollouts in the group), all windows in the failed episode receive negative advantages. This includes windows where the agent took locally correct actions (e.g., correctly identifying a target object). Conversely, in a successful episode, all windows receive positive advantages, including windows where the agent took suboptimal actions (e.g., unnecessary exploration steps that happened not to prevent eventual success).\n\nThe gradient direction for each window is determined by the sign of $\\hat{A}_k$:\n\\begin{equation}\n\\text{sign}(\\hat{A}_k) \\approx \\text{sign}(R_{\\text{episode}} - \\mu)\n\\label{eq:sign_correlation}\n\\end{equation}\nThis means the optimization either reinforces or suppresses \\textit{all} actions within a window based on the episode outcome, regardless of local action quality. Good actions in failed episodes are actively suppressed; bad actions in successful episodes are actively reinforced. Over many training steps, this systematic misattribution progressively erodes whatever inference capability the model retains under the truncated context. Even when the policy begins with non-trivial task competence within its $h$-step window, repeated wrong-sign gradient updates suppress this competence. Mechanism 2 should produce observable degradation below the ceiling set by Mechanism 1, with the rate of degradation proportional to the severity of sign misattribution. Section~\\ref{sec:experiments} confirms this prediction.\n\nA secondary effect compounds this problem. The discount factor $\\gamma^{(N-k)}$ introduces magnitude decay across window positions. For early windows in a long episode ($T=50$, $h=2$, $\\gamma=0.95$), the first window ($k=1$) retains $\\gamma^{N-1} = \\gamma^{24} \\approx 0.29$ of the terminal window's return. While this reduces the learning signal for early decisions, the sign error is fundamentally more harmful: magnitude decay merely slows convergence, while sign misattribution causes active divergence (Section~\\ref{sec:sign_fundamental}).\n\n\\subsection{Episode-Level Training}\n\\label{sec:episode_level}\n\nEpisode-level training resolves both failure mechanisms by treating the complete trajectory as a single GRPO sample. All tokens across all $T$ steps share one advantage $\\hat{A}$, computed from the episode return $R_{\\text{episode}}$ via group normalization over $K$ complete rollouts of the same task instance.\n\nThis design directly addresses Mechanism 1. The policy $\\pi_\\phi(a_t \\mid h_t)$ conditions on the full interaction history $h_t$ at every step $t$. Cross-step dependencies are preserved in the optimization target: the gradient for generating action $a_8$ (navigate to countertop) flows through the complete history including observations from steps 3--4 (drawer exploration outcome).\n\nEpisode-level training also eliminates Mechanism 2. Because there is no window-level return assignment, there is no opportunity for sign misattribution between windows. The single advantage $\\hat{A}$ applies uniformly to the entire trajectory. While this means per-step credit assignment remains coarse (all steps in a successful episode are equally reinforced), it avoids the worse failure mode of \\textit{systematically incorrect} credit assignment. The distinction is critical: uniform reinforcement of a successful trajectory preserves good sub-strategies within it, whereas window-level sign errors actively destroy them.\n\nThe trade-off is computational. Episode-level training requires processing the full sequence length ($T$ steps $\\times$ tokens-per-step) in a single forward and backward pass. For $T=50$ and 100 tokens per step, this amounts to 5000-token sequences, which fits within the capacity of modern architectures but increases memory and compute relative to $h$-step windows. In our experiments (Section~\\ref{sec:experiments}), this overhead is modest compared to the catastrophic failure avoided.\n\nEpisode-level training is, in fact, the natural application of GRPO to multi-turn settings. GRPO was designed as an episode-level algorithm where each rollout receives one return and one advantage. Step-independent training is the deviation from this design, introduced by framework implementation choices rather than algorithmic motivation. Our analysis reveals that this deviation carries hidden costs that become catastrophic for long-horizon interactive tasks.\n\n\\subsection{Selective Verification via Action-Change Reward}\n\\label{sec:selective_verification}\n\nThe credit assignment analysis above focuses on training a competent base agent. We outline here a proposed design for a downstream application: selective verification. This component has not been implemented in the current work and is intended as a direction for future investigation.\n\nInteractive agents benefit from self-verification (re-evaluating their planned action before execution), but empirical analysis shows that over 90\\% of verification instances are confirmatory (the agent does not change its action after checking)~\\cite{long2026selfverification}. Training the agent to verify selectively, only when verification is likely to be informative, could reduce computational cost without sacrificing task performance.\n\nWe formulate selective verification as a binary decision at each step $t$: the agent outputs a verify token $v_t \\in \\{\\texttt{VERIFY}, \\texttt{SKIP}\\}$ before generating its action $a_t$. When $v_t = \\texttt{VERIFY}$, the agent generates a verification rationale and may revise its action; when $v_t = \\texttt{SKIP}$, the agent proceeds directly. The reward signal for training the verification policy uses the action-change indicator:\n\\begin{equation}\n\\Delta a_t = \\mathbb{1}[a_t^{\\text{post-verify}} \\neq a_t^{\\text{pre-verify}}]\n\\label{eq:action_change}\n\\end{equation}\nas a measure of verification informativeness. A verification step that changes the action provided useful corrective information; one that confirms the original action was uninformative for that instance. The full formulation of the verification reward and training procedure is presented in Section~\\ref{sec:selective_experiments}. Episode-level training serves as a prerequisite for this component: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.",
    "structuredPatch": [
      {
        "oldStart": 56,
        "oldLines": 7,
        "newStart": 56,
        "newLines": 7,
        "lines": [
          " \\subsubsection{Mechanism 2: Advantage Sign Misattribution}",
          " \\label{sec:m2_sign_misattribution}",
          " ",
          "-The second mechanism operates at the training layer and, unlike Mechanism 1, is cumulative: its damage increases with each optimization step. Under step-independent training, each window receives a return $R_k = \\gamma^{(N-k)} \\cdot R_{\\text{episode}}$ (Equation~\\ref{eq:step_return}). After group normalization, the advantage $\\hat{A}_k$ has a \\textit{sign} determined primarily by whether the episode succeeded or failed, not by whether window $k$'s actions were locally good or bad.",
          "+The second mechanism operates at the training layer and, unlike Mechanism 1, directly disrupts the optimization process rather than constraining the representable strategy space. Under step-independent training, each window receives a return $R_k = \\gamma^{(N-k)} \\cdot R_{\\text{episode}}$ (Equation~\\ref{eq:step_return}). After group normalization, the advantage $\\hat{A}_k$ has a \\textit{sign} determined primarily by whether the episode succeeded or failed, not by whether window $k$'s actions were locally good or bad.",
          " ",
          " In a failed episode ($R_{\\text{episode}} = 0$), all windows receive $R_k = 0$. If the group mean $\\mu > 0$ (due to other successful rollouts in the group), all windows in the failed episode receive negative advantages. This includes windows where the agent took locally correct actions (e.g., correctly identifying a target object). Conversely, in a successful episode, all windows receive positive advantages, including windows where the agent took suboptimal actions (e.g., unnecessary exploration steps that happened not to prevent eventual success).",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_01GYgQonPzAkUN6eYuQqeVAx`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "old_string": "Over many training steps, this systematic misattribution progressively erodes whatever inference capability the model retains under the truncated context. Even when the policy begins with non-trivial task competence within its $h$-step window, repeated wrong-sign gradient updates suppress this competence. Mechanism 2 should produce observable degradation below the ceiling set by Mechanism 1, with the rate of degradation proportional to the severity of sign misattribution. Section~\\ref{sec:experiments} confirms this prediction.",
  "new_string": "Over training, this systematic misattribution corrupts the optimization signal. Even when the policy begins with non-trivial task competence within its $h$-step window, wrong-sign gradient updates can suppress this competence in unpredictable ways. Mechanism 2 breaks training stability: the corrupted gradient signal produces volatile optimization dynamics that may manifest as monotonic collapse, erratic oscillation, or periods of apparent progress followed by sudden degradation. Section~\\ref{sec:experiments} confirms these predictions across multiple experimental conditions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "3cb5e1a6-de8d-4e4d-89ea-c6a085f2ef2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVB7FxGhxg4pTfaFP1ZZSt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 259,
      "cache_read_input_tokens": 49328,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 259
      },
      "output_tokens": 72,
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

_source line 23 · 2026-05-18T12:09:03.083Z_

<details><summary>↩ Tool result · `toolu_01GYgQonPzAkUN6eYuQqeVAx`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "e1453da7-6fff-4bea-9f5c-56b2cc0b572d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "oldString": "Over many training steps, this systematic misattribution progressively erodes whatever inference capability the model retains under the truncated context. Even when the policy begins with non-trivial task competence within its $h$-step window, repeated wrong-sign gradient updates suppress this competence. Mechanism 2 should produce observable degradation below the ceiling set by Mechanism 1, with the rate of degradation proportional to the severity of sign misattribution. Section~\\ref{sec:experiments} confirms this prediction.",
    "newString": "Over training, this systematic misattribution corrupts the optimization signal. Even when the policy begins with non-trivial task competence within its $h$-step window, wrong-sign gradient updates can suppress this competence in unpredictable ways. Mechanism 2 breaks training stability: the corrupted gradient signal produces volatile optimization dynamics that may manifest as monotonic collapse, erratic oscillation, or periods of apparent progress followed by sudden degradation. Section~\\ref{sec:experiments} confirms these predictions across multiple experimental conditions.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:problem_formulation}\n\nWe formalize the multi-turn interactive agent as a Partially Observable Markov Decision Process (POMDP) $\\mathcal{M} = (\\mathcal{S}, \\mathcal{A}, \\mathcal{O}, P, \\Omega, R, \\gamma)$, where $\\mathcal{S}$ is the state space of the environment, $\\mathcal{A}$ is the action space (natural language commands), $\\mathcal{O}$ is the observation space (textual feedback from the environment), $P: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathcal{S}$ is the transition function, $\\Omega: \\mathcal{S} \\rightarrow \\mathcal{O}$ is the observation function, $R$ is the reward function, and $\\gamma \\in [0,1]$ is a discount factor. The agent policy $\\pi_\\phi(a_t \\mid h_t)$ generates actions conditioned on the interaction history $h_t = (o_1, a_1, o_2, a_2, \\ldots, o_t)$, where $\\phi$ denotes the policy parameters. An episode consists of $T$ interaction steps, terminating with a binary reward $R \\in \\{0, r_+\\}$ that indicates task success or failure.\n\nIn practice, multi-turn episodes can span 50 or more interaction steps, each containing hundreds of tokens. Training a language model policy on the full history $h_T$ is computationally expensive and often exceeds the model's context length. This motivates the \\textbf{step-independent windowing} approach: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, and each window is optimized independently with its own computed return. Concretely, window $k$ observes only $(o_{(k-1)h+1}, a_{(k-1)h+1}, \\ldots, o_{kh})$ and receives a return $R_k$ derived from the episode outcome. This decomposition treats each window as a separate training sample, allowing standard context-length models to process the data. We show below that this seemingly practical choice introduces two failure mechanisms that cause catastrophic training collapse.\n\n\\subsection{GRPO for Language Agents}\n\\label{sec:grpo}\n\nGroup Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} is a bandit-style policy gradient method designed for language model alignment. Unlike PPO~\\cite{schulman2017ppo}, GRPO requires no critic network. For each task instance $x$, the algorithm samples $K$ rollouts $\\{y_1, \\ldots, y_K\\}$ from the current policy $\\pi_\\phi$. The advantage of each rollout is computed relative to the group:\n\\begin{equation}\n\\hat{A}_k = \\frac{R_k - \\mu}{\\sigma + \\epsilon}, \\quad \\mu = \\frac{1}{K}\\sum_{j=1}^K R_j, \\quad \\sigma = \\sqrt{\\frac{1}{K}\\sum_{j=1}^K (R_j - \\mu)^2}\n\\label{eq:grpo_advantage}\n\\end{equation}\nwhere $R_k$ is the return of rollout $k$. The policy gradient is:\n\\begin{equation}\n\\mathcal{L}_{\\text{GRPO}} = -\\frac{1}{K}\\sum_{k=1}^K \\hat{A}_k \\cdot \\min\\left(\\rho_k, \\text{clip}(\\rho_k, 1\\pm\\epsilon_c)\\right) + \\beta \\cdot D_{\\text{KL}}[\\pi_\\phi \\| \\pi_{\\text{ref}}]\n\\label{eq:grpo_loss}\n\\end{equation}\nwhere $\\rho_k = \\pi_\\phi(y_k \\mid x) / \\pi_{\\text{old}}(y_k \\mid x)$ is the importance ratio and $\\beta$ controls the KL penalty against a reference policy $\\pi_{\\text{ref}}$. GRPO is \\textit{episode-level by design}: each rollout $y_k$ is a complete generation with a single return $R_k$ and a single advantage $\\hat{A}_k$. There is no inherent temporal discounting within the algorithm.\n\n\\subsection{Step-Independent Implementation in Multi-Turn Agents}\n\\label{sec:step_independent}\n\nWhen adapting GRPO for multi-turn interactive tasks, agent training frameworks face a mismatch between GRPO's episode-level design and the practical constraints of long trajectories. The RAGEN framework~\\cite{ragen2025} addresses this by introducing step-independent training: each $h$-step window becomes an independent GRPO sample with a discounted return derived from the episode outcome.\n\nSpecifically, for an episode of $T$ steps with binary outcome $R_{\\text{episode}} \\in \\{0, r_+\\}$, the return assigned to window $k$ (covering steps $(k-1)h+1$ through $kh$) is computed as:\n\\begin{equation}\nR_k = \\gamma^{(N - k)} \\cdot R_{\\text{episode}}\n\\label{eq:step_return}\n\\end{equation}\nwhere $N = \\lceil T/h \\rceil$ is the total number of windows in the episode and $\\gamma$ is a discount factor (typically 0.95). In practice, intermediate step penalties (e.g., invalid action penalties) contribute additional terms to $R_k$. Our analysis focuses on the dominant component: the discounted terminal reward. Section~\\ref{sec:sign_verification} empirically validates that advantage sign remains episode-outcome-dominated even in the presence of per-step penalties. Each window is then treated as an independent sample in the GRPO optimization and receives its own group-normalized advantage $\\hat{A}_k$ via Equation~\\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $N$.\n\nThis design choice is motivated by three practical constraints. First, full trajectories of 50+ turns with hundreds of tokens per turn exceed typical context length limits (2048 or 4096 tokens for smaller models). Second, treating each window independently multiplies the effective batch size, improving GPU utilization. Third, the framework inherits the token-level training paradigm common in language model optimization, where shorter sequences are the default.\\footnote{Implementation details are available in the open-source RAGEN codebase, specifically the step-discounted return computation module (\\texttt{compute\\_step\\_discounted\\_returns}).}\n\nDespite these practical motivations, step-independent training fundamentally alters the credit assignment structure. The following section analyzes two mechanisms through which this alteration causes training collapse.\n\n\\subsection{Dual Mechanism Analysis}\n\\label{sec:dual_mechanism}\n\nWe identify two mechanisms operating at different layers that jointly cause training failure under step-independent optimization. The first operates at the inference layer: by restricting the model's observable context, it destroys the policy's ability to generalize to tasks that require cross-step reasoning. The second operates at the training layer: systematic gradient sign errors destabilize the optimization process, producing high-variance training dynamics that range from catastrophic collapse to erratic oscillation. Together, these mechanisms predict three distinct training regimes depending on which mechanism dominates: (a) monotonic collapse when both mechanisms are severe, (b) oscillation followed by degradation when sign misattribution is the primary driver, and (c) stable learning when episode-level training eliminates both. Section~\\ref{sec:experiments} validates these predictions empirically.\n\n\\subsubsection{Mechanism 1: Policy Information Loss}\n\\label{sec:m1_information_loss}\n\nStep-independent training truncates context at both the inference and training layers. At inference time, the policy $\\pi_\\phi(a_t \\mid h_{\\text{window}_k})$ generates actions conditioned on only the local $h$-step history, losing access to observations and actions from earlier windows. At the training layer, the optimization target for each window is computed from this same truncated context, so cross-step strategies that require conditioning on earlier outcomes cannot be reinforced. Consider a household task requiring the agent to first explore a drawer (step 3), discover an object's location (step 4), then navigate to a countertop (step 8). With $h=2$, the window containing step 8 has no access to the exploration outcome from steps 3--4, neither at inference (the model cannot condition on it) nor at training (the gradient cannot credit it). The policy cannot learn the conditional strategy ``go to countertop \\textit{only if} the object was found in the drawer.''\n\nThis information loss destroys the policy's ability to generalize beyond local, single-window strategies. The model may learn to produce valid actions within its observable context, but it cannot acquire conditional strategies that depend on outcomes from earlier steps. The constraint is structural: no amount of training can recover information that is absent from the input. Different window sizes $h$ impose different degrees of information loss, with smaller $h$ restricting the representable strategy space more severely. In our h-sweep experiments (Section~\\ref{sec:experiments}), initial evaluation performance varies across window sizes, reflecting the direct relationship between available context and the policy's generalization capacity.\n\nMore formally, let $\\pi^*$ denote the optimal policy for the full POMDP. The mutual information between $\\pi^*$ and the full history, $I(\\pi^*; h_T)$, captures the total information required for optimal decision-making. Under $h$-step windowing, each window's policy can access at most $I(\\pi^*; h_{\\text{window}_k})$. For tasks with sequential dependencies spanning more than $h$ steps, we have $I(\\pi^*; h_T) \\gg I(\\pi^*; h_{\\text{window}_k})$. The information gap grows with episode length $T$ and shrinks with window size $h$, predicting a generalization cliff as $h$ decreases relative to the task's dependency horizon.\n\n\\subsubsection{Mechanism 2: Advantage Sign Misattribution}\n\\label{sec:m2_sign_misattribution}\n\nThe second mechanism operates at the training layer and, unlike Mechanism 1, directly disrupts the optimization process rather than constraining the representable strategy space. Under step-independent training, each window receives a return $R_k = \\gamma^{(N-k)} \\cdot R_{\\text{episode}}$ (Equation~\\ref{eq:step_return}). After group normalization, the advantage $\\hat{A}_k$ has a \\textit{sign} determined primarily by whether the episode succeeded or failed, not by whether window $k$'s actions were locally good or bad.\n\nIn a failed episode ($R_{\\text{episode}} = 0$), all windows receive $R_k = 0$. If the group mean $\\mu > 0$ (due to other successful rollouts in the group), all windows in the failed episode receive negative advantages. This includes windows where the agent took locally correct actions (e.g., correctly identifying a target object). Conversely, in a successful episode, all windows receive positive advantages, including windows where the agent took suboptimal actions (e.g., unnecessary exploration steps that happened not to prevent eventual success).\n\nThe gradient direction for each window is determined by the sign of $\\hat{A}_k$:\n\\begin{equation}\n\\text{sign}(\\hat{A}_k) \\approx \\text{sign}(R_{\\text{episode}} - \\mu)\n\\label{eq:sign_correlation}\n\\end{equation}\nThis means the optimization either reinforces or suppresses \\textit{all} actions within a window based on the episode outcome, regardless of local action quality. Good actions in failed episodes are actively suppressed; bad actions in successful episodes are actively reinforced. Over many training steps, this systematic misattribution progressively erodes whatever inference capability the model retains under the truncated context. Even when the policy begins with non-trivial task competence within its $h$-step window, repeated wrong-sign gradient updates suppress this competence. Mechanism 2 should produce observable degradation below the ceiling set by Mechanism 1, with the rate of degradation proportional to the severity of sign misattribution. Section~\\ref{sec:experiments} confirms this prediction.\n\nA secondary effect compounds this problem. The discount factor $\\gamma^{(N-k)}$ introduces magnitude decay across window positions. For early windows in a long episode ($T=50$, $h=2$, $\\gamma=0.95$), the first window ($k=1$) retains $\\gamma^{N-1} = \\gamma^{24} \\approx 0.29$ of the terminal window's return. While this reduces the learning signal for early decisions, the sign error is fundamentally more harmful: magnitude decay merely slows convergence, while sign misattribution causes active divergence (Section~\\ref{sec:sign_fundamental}).\n\n\\subsection{Episode-Level Training}\n\\label{sec:episode_level}\n\nEpisode-level training resolves both failure mechanisms by treating the complete trajectory as a single GRPO sample. All tokens across all $T$ steps share one advantage $\\hat{A}$, computed from the episode return $R_{\\text{episode}}$ via group normalization over $K$ complete rollouts of the same task instance.\n\nThis design directly addresses Mechanism 1. The policy $\\pi_\\phi(a_t \\mid h_t)$ conditions on the full interaction history $h_t$ at every step $t$. Cross-step dependencies are preserved in the optimization target: the gradient for generating action $a_8$ (navigate to countertop) flows through the complete history including observations from steps 3--4 (drawer exploration outcome).\n\nEpisode-level training also eliminates Mechanism 2. Because there is no window-level return assignment, there is no opportunity for sign misattribution between windows. The single advantage $\\hat{A}$ applies uniformly to the entire trajectory. While this means per-step credit assignment remains coarse (all steps in a successful episode are equally reinforced), it avoids the worse failure mode of \\textit{systematically incorrect} credit assignment. The distinction is critical: uniform reinforcement of a successful trajectory preserves good sub-strategies within it, whereas window-level sign errors actively destroy them.\n\nThe trade-off is computational. Episode-level training requires processing the full sequence length ($T$ steps $\\times$ tokens-per-step) in a single forward and backward pass. For $T=50$ and 100 tokens per step, this amounts to 5000-token sequences, which fits within the capacity of modern architectures but increases memory and compute relative to $h$-step windows. In our experiments (Section~\\ref{sec:experiments}), this overhead is modest compared to the catastrophic failure avoided.\n\nEpisode-level training is, in fact, the natural application of GRPO to multi-turn settings. GRPO was designed as an episode-level algorithm where each rollout receives one return and one advantage. Step-independent training is the deviation from this design, introduced by framework implementation choices rather than algorithmic motivation. Our analysis reveals that this deviation carries hidden costs that become catastrophic for long-horizon interactive tasks.\n\n\\subsection{Selective Verification via Action-Change Reward}\n\\label{sec:selective_verification}\n\nThe credit assignment analysis above focuses on training a competent base agent. We outline here a proposed design for a downstream application: selective verification. This component has not been implemented in the current work and is intended as a direction for future investigation.\n\nInteractive agents benefit from self-verification (re-evaluating their planned action before execution), but empirical analysis shows that over 90\\% of verification instances are confirmatory (the agent does not change its action after checking)~\\cite{long2026selfverification}. Training the agent to verify selectively, only when verification is likely to be informative, could reduce computational cost without sacrificing task performance.\n\nWe formulate selective verification as a binary decision at each step $t$: the agent outputs a verify token $v_t \\in \\{\\texttt{VERIFY}, \\texttt{SKIP}\\}$ before generating its action $a_t$. When $v_t = \\texttt{VERIFY}$, the agent generates a verification rationale and may revise its action; when $v_t = \\texttt{SKIP}$, the agent proceeds directly. The reward signal for training the verification policy uses the action-change indicator:\n\\begin{equation}\n\\Delta a_t = \\mathbb{1}[a_t^{\\text{post-verify}} \\neq a_t^{\\text{pre-verify}}]\n\\label{eq:action_change}\n\\end{equation}\nas a measure of verification informativeness. A verification step that changes the action provided useful corrective information; one that confirms the original action was uninformative for that instance. The full formulation of the verification reward and training procedure is presented in Section~\\ref{sec:selective_experiments}. Episode-level training serves as a prerequisite for this component: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.",
    "structuredPatch": [
      {
        "oldStart": 65,
        "oldLines": 7,
        "newStart": 65,
        "newLines": 7,
        "lines": [
          " \\text{sign}(\\hat{A}_k) \\approx \\text{sign}(R_{\\text{episode}} - \\mu)",
          " \\label{eq:sign_correlation}",
          " \\end{equation}",
          "-This means the optimization either reinforces or suppresses \\textit{all} actions within a window based on the episode outcome, regardless of local action quality. Good actions in failed episodes are actively suppressed; bad actions in successful episodes are actively reinforced. Over many training steps, this systematic misattribution progressively erodes whatever inference capability the model retains under the truncated context. Even when the policy begins with non-trivial task competence within its $h$-step window, repeated wrong-sign gradient updates suppress this competence. Mechanism 2 should produce observable degradation below the ceiling set by Mechanism 1, with the rate of degradation proportional to the severity of sign misattribution. Section~\\ref{sec:experiments} confirms this prediction.",
          "+This means the optimization either reinforces or suppresses \\textit{all} actions within a window based on the episode outcome, regardless of local action quality. Good actions in failed episodes are actively suppressed; bad actions in successful episodes are actively reinforced. Over training, this systematic misattribution corrupts the optimization signal. Even when the policy begins with non-trivial task competence within its $h$-step window, wrong-sign gradient updates can suppress this competence in unpredictable ways. Mechanism 2 breaks training stability: the corrupted gradient signal produces volatile optimization dynamics that may manifest as monotonic collapse, erratic oscillation, or periods of apparent progress followed by sudden degradation. Section~\\ref{sec:experiments} confirms these predictions across multiple experimental conditions.",
          " ",
          " A secondary effect compounds this problem. The discount factor $\\gamma^{(N-k)}$ introduces magnitude decay across window positions. For early windows in a long episode ($T=50$, $h=2$, $\\gamma=0.95$), the first window ($k=1$) retains $\\gamma^{N-1} = \\gamma^{24} \\approx 0.29$ of the terminal window's return. While this reduces the learning signal for early decisions, the sign error is fundamentally more harmful: magnitude decay merely slows convergence, while sign misattribution causes active divergence (Section~\\ref{sec:sign_fundamental}).",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 24_

Now insert the new §3.6 (Factorial Experiment Design) before the current Selective Verification subsection.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "d2228161-2ed0-431e-ba86-1fd4c1954e2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VikDJnWTwrC4Vv9o7mKSTy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 525,
      "cache_read_input_tokens": 49587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 525
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

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Edit · `toolu_01DAQpujZdhcQs27LZ5LfRYe`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "old_string": "\\subsection{Selective Verification via Action-Change Reward}\n\\label{sec:selective_verification}\n\nThe credit assignment analysis above focuses on training a competent base agent. We outline here a proposed design for a downstream application: selective verification. This component has not been implemented in the current work and is intended as a direction for future investigation.\n\nInteractive agents benefit from self-verification (re-evaluating their planned action before execution), but empirical analysis shows that over 90\\% of verification instances are confirmatory (the agent does not change its action after checking)~\\cite{long2026selfverification}. Training the agent to verify selectively, only when verification is likely to be informative, could reduce computational cost without sacrificing task performance.\n\nWe formulate selective verification as a binary decision at each step $t$: the agent outputs a verify token $v_t \\in \\{\\texttt{VERIFY}, \\texttt{SKIP}\\}$ before generating its action $a_t$. When $v_t = \\texttt{VERIFY}$, the agent generates a verification rationale and may revise its action; when $v_t = \\texttt{SKIP}$, the agent proceeds directly. The reward signal for training the verification policy uses the action-change indicator:\n\\begin{equation}\n\\Delta a_t = \\mathbb{1}[a_t^{\\text{post-verify}} \\neq a_t^{\\text{pre-verify}}]\n\\label{eq:action_change}\n\\end{equation}\nas a measure of verification informativeness. A verification step that changes the action provided useful corrective information; one that confirms the original action was uninformative for that instance. The full formulation of the verification reward and training procedure is presented in Section~\\ref{sec:selective_experiments}. Episode-level training serves as a prerequisite for this component: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.",
  "new_string": "\\subsection{Factorial Experiment Design}\n\\label{sec:factorial_design}\n\nThe dual mechanism analysis yields testable predictions about how each mechanism independently affects training. To isolate their qualitative effects, we design a $2 \\times 2$ factorial experiment that varies two factors: (1) the observation window, controlling whether policy information loss (Mechanism 1) is present, and (2) the advantage granularity, controlling whether sign misattribution (Mechanism 2) is present. The four conditions are:\n\n\\begin{itemize}\n\\item \\textbf{Cell A} (truncated observation $+$ step-level advantage): Window size $h{=}2$ with per-window advantage computation. Both mechanisms are active. The policy suffers from information loss \\textit{and} receives corrupted gradient signals.\n\\item \\textbf{Cell B} (truncated observation $+$ episode-level advantage): Window size $h{=}2$ with a single episode-level advantage shared across all windows. Only Mechanism 1 is active; sign misattribution is eliminated because all windows in an episode receive the same advantage sign.\n\\item \\textbf{Cell D} (full observation $+$ episode-level advantage): The complete trajectory is processed as a single sequence with episode-level advantage. Neither mechanism is active.\n\\end{itemize}\n\nComparing Cell A against Cell B isolates the effect of sign misattribution while holding information loss constant. If Cell B exhibits more stable training dynamics than Cell A, the difference is attributable to Mechanism 2. Comparing Cell B against Cell D isolates the effect of information loss while both conditions use episode-level advantage. The performance gap between these two cells reflects how truncated context limits the policy's generalization to tasks with cross-step dependencies.\n\nThis factorial design tests qualitative predictions about training dynamics, not quantitative effect decomposition. We expect Cell A to exhibit the most unstable training (oscillation or collapse), Cell B to train more stably but plateau below Cell D due to the information constraint, and Cell D to achieve monotonic improvement. Section~\\ref{sec:experiments} reports the results.\n\n\\subsection{Selective Verification}\n\\label{sec:selective_verification}\n\nWe propose selective verification as a direction for future investigation. At each step, the agent would output a binary decision $v_t \\in \\{\\texttt{VERIFY}, \\texttt{SKIP}\\}$ before generating its action, and the training signal would use an action-change indicator (whether verification actually altered the action) to reward informative verification. This component has not been implemented and is proposed as a direction for future investigation. Episode-level training serves as a prerequisite: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "9fa4257d-9a53-4b3e-9bcb-29b56e2d683a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VikDJnWTwrC4Vv9o7mKSTy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 525,
      "cache_read_input_tokens": 49587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 525
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

### Tool result

_source line 26 · 2026-05-18T12:09:29.537Z_

<details><summary>↩ Tool result · `toolu_01DAQpujZdhcQs27LZ5LfRYe`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "d38ba1bd-46ab-4f79-8c0d-ab67a658c37e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
    "oldString": "\\subsection{Selective Verification via Action-Change Reward}\n\\label{sec:selective_verification}\n\nThe credit assignment analysis above focuses on training a competent base agent. We outline here a proposed design for a downstream application: selective verification. This component has not been implemented in the current work and is intended as a direction for future investigation.\n\nInteractive agents benefit from self-verification (re-evaluating their planned action before execution), but empirical analysis shows that over 90\\% of verification instances are confirmatory (the agent does not change its action after checking)~\\cite{long2026selfverification}. Training the agent to verify selectively, only when verification is likely to be informative, could reduce computational cost without sacrificing task performance.\n\nWe formulate selective verification as a binary decision at each step $t$: the agent outputs a verify token $v_t \\in \\{\\texttt{VERIFY}, \\texttt{SKIP}\\}$ before generating its action $a_t$. When $v_t = \\texttt{VERIFY}$, the agent generates a verification rationale and may revise its action; when $v_t = \\texttt{SKIP}$, the agent proceeds directly. The reward signal for training the verification policy uses the action-change indicator:\n\\begin{equation}\n\\Delta a_t = \\mathbb{1}[a_t^{\\text{post-verify}} \\neq a_t^{\\text{pre-verify}}]\n\\label{eq:action_change}\n\\end{equation}\nas a measure of verification informativeness. A verification step that changes the action provided useful corrective information; one that confirms the original action was uninformative for that instance. The full formulation of the verification reward and training procedure is presented in Section~\\ref{sec:selective_experiments}. Episode-level training serves as a prerequisite for this component: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.",
    "newString": "\\subsection{Factorial Experiment Design}\n\\label{sec:factorial_design}\n\nThe dual mechanism analysis yields testable predictions about how each mechanism independently affects training. To isolate their qualitative effects, we design a $2 \\times 2$ factorial experiment that varies two factors: (1) the observation window, controlling whether policy information loss (Mechanism 1) is present, and (2) the advantage granularity, controlling whether sign misattribution (Mechanism 2) is present. The four conditions are:\n\n\\begin{itemize}\n\\item \\textbf{Cell A} (truncated observation $+$ step-level advantage): Window size $h{=}2$ with per-window advantage computation. Both mechanisms are active. The policy suffers from information loss \\textit{and} receives corrupted gradient signals.\n\\item \\textbf{Cell B} (truncated observation $+$ episode-level advantage): Window size $h{=}2$ with a single episode-level advantage shared across all windows. Only Mechanism 1 is active; sign misattribution is eliminated because all windows in an episode receive the same advantage sign.\n\\item \\textbf{Cell D} (full observation $+$ episode-level advantage): The complete trajectory is processed as a single sequence with episode-level advantage. Neither mechanism is active.\n\\end{itemize}\n\nComparing Cell A against Cell B isolates the effect of sign misattribution while holding information loss constant. If Cell B exhibits more stable training dynamics than Cell A, the difference is attributable to Mechanism 2. Comparing Cell B against Cell D isolates the effect of information loss while both conditions use episode-level advantage. The performance gap between these two cells reflects how truncated context limits the policy's generalization to tasks with cross-step dependencies.\n\nThis factorial design tests qualitative predictions about training dynamics, not quantitative effect decomposition. We expect Cell A to exhibit the most unstable training (oscillation or collapse), Cell B to train more stably but plateau below Cell D due to the information constraint, and Cell D to achieve monotonic improvement. Section~\\ref{sec:experiments} reports the results.\n\n\\subsection{Selective Verification}\n\\label{sec:selective_verification}\n\nWe propose selective verification as a direction for future investigation. At each step, the agent would output a binary decision $v_t \\in \\{\\texttt{VERIFY}, \\texttt{SKIP}\\}$ before generating its action, and the training signal would use an action-change indicator (whether verification actually altered the action) to reward informative verification. This component has not been implemented and is proposed as a direction for future investigation. Episode-level training serves as a prerequisite: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:problem_formulation}\n\nWe formalize the multi-turn interactive agent as a Partially Observable Markov Decision Process (POMDP) $\\mathcal{M} = (\\mathcal{S}, \\mathcal{A}, \\mathcal{O}, P, \\Omega, R, \\gamma)$, where $\\mathcal{S}$ is the state space of the environment, $\\mathcal{A}$ is the action space (natural language commands), $\\mathcal{O}$ is the observation space (textual feedback from the environment), $P: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathcal{S}$ is the transition function, $\\Omega: \\mathcal{S} \\rightarrow \\mathcal{O}$ is the observation function, $R$ is the reward function, and $\\gamma \\in [0,1]$ is a discount factor. The agent policy $\\pi_\\phi(a_t \\mid h_t)$ generates actions conditioned on the interaction history $h_t = (o_1, a_1, o_2, a_2, \\ldots, o_t)$, where $\\phi$ denotes the policy parameters. An episode consists of $T$ interaction steps, terminating with a binary reward $R \\in \\{0, r_+\\}$ that indicates task success or failure.\n\nIn practice, multi-turn episodes can span 50 or more interaction steps, each containing hundreds of tokens. Training a language model policy on the full history $h_T$ is computationally expensive and often exceeds the model's context length. This motivates the \\textbf{step-independent windowing} approach: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, and each window is optimized independently with its own computed return. Concretely, window $k$ observes only $(o_{(k-1)h+1}, a_{(k-1)h+1}, \\ldots, o_{kh})$ and receives a return $R_k$ derived from the episode outcome. This decomposition treats each window as a separate training sample, allowing standard context-length models to process the data. We show below that this seemingly practical choice introduces two failure mechanisms that cause catastrophic training collapse.\n\n\\subsection{GRPO for Language Agents}\n\\label{sec:grpo}\n\nGroup Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} is a bandit-style policy gradient method designed for language model alignment. Unlike PPO~\\cite{schulman2017ppo}, GRPO requires no critic network. For each task instance $x$, the algorithm samples $K$ rollouts $\\{y_1, \\ldots, y_K\\}$ from the current policy $\\pi_\\phi$. The advantage of each rollout is computed relative to the group:\n\\begin{equation}\n\\hat{A}_k = \\frac{R_k - \\mu}{\\sigma + \\epsilon}, \\quad \\mu = \\frac{1}{K}\\sum_{j=1}^K R_j, \\quad \\sigma = \\sqrt{\\frac{1}{K}\\sum_{j=1}^K (R_j - \\mu)^2}\n\\label{eq:grpo_advantage}\n\\end{equation}\nwhere $R_k$ is the return of rollout $k$. The policy gradient is:\n\\begin{equation}\n\\mathcal{L}_{\\text{GRPO}} = -\\frac{1}{K}\\sum_{k=1}^K \\hat{A}_k \\cdot \\min\\left(\\rho_k, \\text{clip}(\\rho_k, 1\\pm\\epsilon_c)\\right) + \\beta \\cdot D_{\\text{KL}}[\\pi_\\phi \\| \\pi_{\\text{ref}}]\n\\label{eq:grpo_loss}\n\\end{equation}\nwhere $\\rho_k = \\pi_\\phi(y_k \\mid x) / \\pi_{\\text{old}}(y_k \\mid x)$ is the importance ratio and $\\beta$ controls the KL penalty against a reference policy $\\pi_{\\text{ref}}$. GRPO is \\textit{episode-level by design}: each rollout $y_k$ is a complete generation with a single return $R_k$ and a single advantage $\\hat{A}_k$. There is no inherent temporal discounting within the algorithm.\n\n\\subsection{Step-Independent Implementation in Multi-Turn Agents}\n\\label{sec:step_independent}\n\nWhen adapting GRPO for multi-turn interactive tasks, agent training frameworks face a mismatch between GRPO's episode-level design and the practical constraints of long trajectories. The RAGEN framework~\\cite{ragen2025} addresses this by introducing step-independent training: each $h$-step window becomes an independent GRPO sample with a discounted return derived from the episode outcome.\n\nSpecifically, for an episode of $T$ steps with binary outcome $R_{\\text{episode}} \\in \\{0, r_+\\}$, the return assigned to window $k$ (covering steps $(k-1)h+1$ through $kh$) is computed as:\n\\begin{equation}\nR_k = \\gamma^{(N - k)} \\cdot R_{\\text{episode}}\n\\label{eq:step_return}\n\\end{equation}\nwhere $N = \\lceil T/h \\rceil$ is the total number of windows in the episode and $\\gamma$ is a discount factor (typically 0.95). In practice, intermediate step penalties (e.g., invalid action penalties) contribute additional terms to $R_k$. Our analysis focuses on the dominant component: the discounted terminal reward. Section~\\ref{sec:sign_verification} empirically validates that advantage sign remains episode-outcome-dominated even in the presence of per-step penalties. Each window is then treated as an independent sample in the GRPO optimization and receives its own group-normalized advantage $\\hat{A}_k$ via Equation~\\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $N$.\n\nThis design choice is motivated by three practical constraints. First, full trajectories of 50+ turns with hundreds of tokens per turn exceed typical context length limits (2048 or 4096 tokens for smaller models). Second, treating each window independently multiplies the effective batch size, improving GPU utilization. Third, the framework inherits the token-level training paradigm common in language model optimization, where shorter sequences are the default.\\footnote{Implementation details are available in the open-source RAGEN codebase, specifically the step-discounted return computation module (\\texttt{compute\\_step\\_discounted\\_returns}).}\n\nDespite these practical motivations, step-independent training fundamentally alters the credit assignment structure. The following section analyzes two mechanisms through which this alteration causes training collapse.\n\n\\subsection{Dual Mechanism Analysis}\n\\label{sec:dual_mechanism}\n\nWe identify two mechanisms operating at different layers that jointly cause training failure under step-independent optimization. The first operates at the inference layer: by restricting the model's observable context, it destroys the policy's ability to generalize to tasks that require cross-step reasoning. The second operates at the training layer: systematic gradient sign errors destabilize the optimization process, producing high-variance training dynamics that range from catastrophic collapse to erratic oscillation. Together, these mechanisms predict three distinct training regimes depending on which mechanism dominates: (a) monotonic collapse when both mechanisms are severe, (b) oscillation followed by degradation when sign misattribution is the primary driver, and (c) stable learning when episode-level training eliminates both. Section~\\ref{sec:experiments} validates these predictions empirically.\n\n\\subsubsection{Mechanism 1: Policy Information Loss}\n\\label{sec:m1_information_loss}\n\nStep-independent training truncates context at both the inference and training layers. At inference time, the policy $\\pi_\\phi(a_t \\mid h_{\\text{window}_k})$ generates actions conditioned on only the local $h$-step history, losing access to observations and actions from earlier windows. At the training layer, the optimization target for each window is computed from this same truncated context, so cross-step strategies that require conditioning on earlier outcomes cannot be reinforced. Consider a household task requiring the agent to first explore a drawer (step 3), discover an object's location (step 4), then navigate to a countertop (step 8). With $h=2$, the window containing step 8 has no access to the exploration outcome from steps 3--4, neither at inference (the model cannot condition on it) nor at training (the gradient cannot credit it). The policy cannot learn the conditional strategy ``go to countertop \\textit{only if} the object was found in the drawer.''\n\nThis information loss destroys the policy's ability to generalize beyond local, single-window strategies. The model may learn to produce valid actions within its observable context, but it cannot acquire conditional strategies that depend on outcomes from earlier steps. The constraint is structural: no amount of training can recover information that is absent from the input. Different window sizes $h$ impose different degrees of information loss, with smaller $h$ restricting the representable strategy space more severely. In our h-sweep experiments (Section~\\ref{sec:experiments}), initial evaluation performance varies across window sizes, reflecting the direct relationship between available context and the policy's generalization capacity.\n\nMore formally, let $\\pi^*$ denote the optimal policy for the full POMDP. The mutual information between $\\pi^*$ and the full history, $I(\\pi^*; h_T)$, captures the total information required for optimal decision-making. Under $h$-step windowing, each window's policy can access at most $I(\\pi^*; h_{\\text{window}_k})$. For tasks with sequential dependencies spanning more than $h$ steps, we have $I(\\pi^*; h_T) \\gg I(\\pi^*; h_{\\text{window}_k})$. The information gap grows with episode length $T$ and shrinks with window size $h$, predicting a generalization cliff as $h$ decreases relative to the task's dependency horizon.\n\n\\subsubsection{Mechanism 2: Advantage Sign Misattribution}\n\\label{sec:m2_sign_misattribution}\n\nThe second mechanism operates at the training layer and, unlike Mechanism 1, directly disrupts the optimization process rather than constraining the representable strategy space. Under step-independent training, each window receives a return $R_k = \\gamma^{(N-k)} \\cdot R_{\\text{episode}}$ (Equation~\\ref{eq:step_return}). After group normalization, the advantage $\\hat{A}_k$ has a \\textit{sign} determined primarily by whether the episode succeeded or failed, not by whether window $k$'s actions were locally good or bad.\n\nIn a failed episode ($R_{\\text{episode}} = 0$), all windows receive $R_k = 0$. If the group mean $\\mu > 0$ (due to other successful rollouts in the group), all windows in the failed episode receive negative advantages. This includes windows where the agent took locally correct actions (e.g., correctly identifying a target object). Conversely, in a successful episode, all windows receive positive advantages, including windows where the agent took suboptimal actions (e.g., unnecessary exploration steps that happened not to prevent eventual success).\n\nThe gradient direction for each window is determined by the sign of $\\hat{A}_k$:\n\\begin{equation}\n\\text{sign}(\\hat{A}_k) \\approx \\text{sign}(R_{\\text{episode}} - \\mu)\n\\label{eq:sign_correlation}\n\\end{equation}\nThis means the optimization either reinforces or suppresses \\textit{all} actions within a window based on the episode outcome, regardless of local action quality. Good actions in failed episodes are actively suppressed; bad actions in successful episodes are actively reinforced. Over training, this systematic misattribution corrupts the optimization signal. Even when the policy begins with non-trivial task competence within its $h$-step window, wrong-sign gradient updates can suppress this competence in unpredictable ways. Mechanism 2 breaks training stability: the corrupted gradient signal produces volatile optimization dynamics that may manifest as monotonic collapse, erratic oscillation, or periods of apparent progress followed by sudden degradation. Section~\\ref{sec:experiments} confirms these predictions across multiple experimental conditions.\n\nA secondary effect compounds this problem. The discount factor $\\gamma^{(N-k)}$ introduces magnitude decay across window positions. For early windows in a long episode ($T=50$, $h=2$, $\\gamma=0.95$), the first window ($k=1$) retains $\\gamma^{N-1} = \\gamma^{24} \\approx 0.29$ of the terminal window's return. While this reduces the learning signal for early decisions, the sign error is fundamentally more harmful: magnitude decay merely slows convergence, while sign misattribution causes active divergence (Section~\\ref{sec:sign_fundamental}).\n\n\\subsection{Episode-Level Training}\n\\label{sec:episode_level}\n\nEpisode-level training resolves both failure mechanisms by treating the complete trajectory as a single GRPO sample. All tokens across all $T$ steps share one advantage $\\hat{A}$, computed from the episode return $R_{\\text{episode}}$ via group normalization over $K$ complete rollouts of the same task instance.\n\nThis design directly addresses Mechanism 1. The policy $\\pi_\\phi(a_t \\mid h_t)$ conditions on the full interaction history $h_t$ at every step $t$. Cross-step dependencies are preserved in the optimization target: the gradient for generating action $a_8$ (navigate to countertop) flows through the complete history including observations from steps 3--4 (drawer exploration outcome).\n\nEpisode-level training also eliminates Mechanism 2. Because there is no window-level return assignment, there is no opportunity for sign misattribution between windows. The single advantage $\\hat{A}$ applies uniformly to the entire trajectory. While this means per-step credit assignment remains coarse (all steps in a successful episode are equally reinforced), it avoids the worse failure mode of \\textit{systematically incorrect} credit assignment. The distinction is critical: uniform reinforcement of a successful trajectory preserves good sub-strategies within it, whereas window-level sign errors actively destroy them.\n\nThe trade-off is computational. Episode-level training requires processing the full sequence length ($T$ steps $\\times$ tokens-per-step) in a single forward and backward pass. For $T=50$ and 100 tokens per step, this amounts to 5000-token sequences, which fits within the capacity of modern architectures but increases memory and compute relative to $h$-step windows. In our experiments (Section~\\ref{sec:experiments}), this overhead is modest compared to the catastrophic failure avoided.\n\nEpisode-level training is, in fact, the natural application of GRPO to multi-turn settings. GRPO was designed as an episode-level algorithm where each rollout receives one return and one advantage. Step-independent training is the deviation from this design, introduced by framework implementation choices rather than algorithmic motivation. Our analysis reveals that this deviation carries hidden costs that become catastrophic for long-horizon interactive tasks.\n\n\\subsection{Selective Verification via Action-Change Reward}\n\\label{sec:selective_verification}\n\nThe credit assignment analysis above focuses on training a competent base agent. We outline here a proposed design for a downstream application: selective verification. This component has not been implemented in the current work and is intended as a direction for future investigation.\n\nInteractive agents benefit from self-verification (re-evaluating their planned action before execution), but empirical analysis shows that over 90\\% of verification instances are confirmatory (the agent does not change its action after checking)~\\cite{long2026selfverification}. Training the agent to verify selectively, only when verification is likely to be informative, could reduce computational cost without sacrificing task performance.\n\nWe formulate selective verification as a binary decision at each step $t$: the agent outputs a verify token $v_t \\in \\{\\texttt{VERIFY}, \\texttt{SKIP}\\}$ before generating its action $a_t$. When $v_t = \\texttt{VERIFY}$, the agent generates a verification rationale and may revise its action; when $v_t = \\texttt{SKIP}$, the agent proceeds directly. The reward signal for training the verification policy uses the action-change indicator:\n\\begin{equation}\n\\Delta a_t = \\mathbb{1}[a_t^{\\text{post-verify}} \\neq a_t^{\\text{pre-verify}}]\n\\label{eq:action_change}\n\\end{equation}\nas a measure of verification informativeness. A verification step that changes the action provided useful corrective information; one that confirms the original action was uninformative for that instance. The full formulation of the verification reward and training procedure is presented in Section~\\ref{sec:selective_experiments}. Episode-level training serves as a prerequisite for this component: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.",
    "structuredPatch": [
      {
        "oldStart": 82,
        "oldLines": 16,
        "newStart": 82,
        "newLines": 22,
        "lines": [
          " ",
          " Episode-level training is, in fact, the natural application of GRPO to multi-turn settings. GRPO was designed as an episode-level algorithm where each rollout receives one return and one advantage. Step-independent training is the deviation from this design, introduced by framework implementation choices rather than algorithmic motivation. Our analysis reveals that this deviation carries hidden costs that become catastrophic for long-horizon interactive tasks.",
          " ",
          "-\\subsection{Selective Verification via Action-Change Reward}",
          "-\\label{sec:selective_verification}",
          "+\\subsection{Factorial Experiment Design}",
          "+\\label{sec:factorial_design}",
          " ",
          "-The credit assignment analysis above focuses on training a competent base agent. We outline here a proposed design for a downstream application: selective verification. This component has not been implemented in the current work and is intended as a direction for future investigation.",
          "+The dual mechanism analysis yields testable predictions about how each mechanism independently affects training. To isolate their qualitative effects, we design a $2 \\times 2$ factorial experiment that varies two factors: (1) the observation window, controlling whether policy information loss (Mechanism 1) is present, and (2) the advantage granularity, controlling whether sign misattribution (Mechanism 2) is present. The four conditions are:",
          " ",
          "-Interactive agents benefit from self-verification (re-evaluating their planned action before execution), but empirical analysis shows that over 90\\% of verification instances are confirmatory (the agent does not change its action after checking)~\\cite{long2026selfverification}. Training the agent to verify selectively, only when verification is likely to be informative, could reduce computational cost without sacrificing task performance.",
          "+\\begin{itemize}",
          "+\\item \\textbf{Cell A} (truncated observation $+$ step-level advantage): Window size $h{=}2$ with per-window advantage computation. Both mechanisms are active. The policy suffers from information loss \\textit{and} receives corrupted gradient signals.",
          "+\\item \\textbf{Cell B} (truncated observation $+$ episode-level advantage): Window size $h{=}2$ with a single episode-level advantage shared across all windows. Only Mechanism 1 is active; sign misattribution is eliminated because all windows in an episode receive the same advantage sign.",
          "+\\item \\textbf{Cell D} (full observation $+$ episode-level advantage): The complete trajectory is processed as a single sequence with episode-level advantage. Neither mechanism is active.",
          "+\\end{itemize}",
          " ",
          "-We formulate selective verification as a binary decision at each step $t$: the agent outputs a verify token $v_t \\in \\{\\texttt{VERIFY}, \\texttt{SKIP}\\}$ before generating its action $a_t$. When $v_t = \\texttt{VERIFY}$, the agent generates a verification rationale and may revise its action; when $v_t = \\texttt{SKIP}$, the agent proceeds directly. The reward signal for training the verification policy uses the action-change indicator:",
          "-\\begin{equation}",
          "-\\Delta a_t = \\mathbb{1}[a_t^{\\text{post-verify}} \\neq a_t^{\\text{pre-verify}}]",
          "-\\label{eq:action_change}",
          "-\\end{equation}",
          "-as a measure of verification informativeness. A verification step that changes the action provided useful corrective information; one that confirms the original action was uninformative for that instance. The full formulation of the verification reward and training procedure is presented in Section~\\ref{sec:selective_experiments}. Episode-level training serves as a prerequisite for this component: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.",
          "\\ No newline at end of file",
          "+Comparing Cell A against Cell B isolates the effect of sign misattribution while holding information loss constant. If Cell B exhibits more stable training dynamics than Cell A, the difference is attributable to Mechanism 2. Comparing Cell B against Cell D isolates the effect of information loss while both conditions use episode-level advantage. The performance gap between these two cells reflects how truncated context limits the policy's generalization to tasks with cross-step dependencies.",
          "+",
          "+This factorial design tests qualitative predictions about training dynamics, not quantitative effect decomposition. We expect Cell A to exhibit the most unstable training (oscillation or collapse), Cell B to train more stably but plateau below Cell D due to the information constraint, and Cell D to achieve monotonic improvement. Section~\\ref{sec:experiments} reports the results.",
          "+",
          "+\\subsection{Selective Verification}",
          "+\\label{sec:selective_verification}",
          "+",
          "+We propose selective verification as a direction for future investigation. At each step, the agent would output a binary decision $v_t \\in \\{\\texttt{VERIFY}, \\texttt{SKIP}\\}$ before generating its action, and the training signal would use an action-change indicator (whether verification actually altered the action) to reward informative verification. This component has not been implemented and is proposed as a direction for future investigation. Episode-level training serves as a prerequisite: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.",
          "\\ No newline at end of file"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 27_

Let me verify the final result.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "8d2481c2-b977-4a62-9896-1363be1b3d66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W5GmvaA9jfRaQaL2ZN8HxG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1287,
      "cache_read_input_tokens": 50112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1287
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

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01XQHCJ5kecdyccBy8vGuWwh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "552faa90-2f03-49ba-b7a7-4a6ead6d24ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W5GmvaA9jfRaQaL2ZN8HxG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1287,
      "cache_read_input_tokens": 50112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1287
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

### Tool result

_source line 29 · 2026-05-18T12:09:37.751Z_

<details><summary>↩ Tool result · `toolu_01XQHCJ5kecdyccBy8vGuWwh`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:problem_formulation}
6	
7	We formalize the multi-turn interactive agent as a Partially Observable Markov Decision Process (POMDP) $\mathcal{M} = (\mathcal{S}, \mathcal{A}, \mathcal{O}, P, \Omega, R, \gamma)$, where $\mathcal{S}$ is the state space of the environment, $\mathcal{A}$ is the action space (natural language commands), $\mathcal{O}$ is the observation space (textual feedback from the environment), $P: \mathcal{S} \times \mathcal{A} \rightarrow \mathcal{S}$ is the transition function, $\Omega: \mathcal{S} \rightarrow \mathcal{O}$ is the observation function, $R$ is the reward function, and $\gamma \in [0,1]$ is a discount factor. The agent policy $\pi_\phi(a_t \mid h_t)$ generates actions conditioned on the interaction history $h_t = (o_1, a_1, o_2, a_2, \ldots, o_t)$, where $\phi$ denotes the policy parameters. An episode consists of $T$ interaction steps, terminating with a binary reward $R \in \{0, r_+\}$ that indicates task success or failure.
8	
9	In practice, multi-turn episodes can span 50 or more interaction steps, each containing hundreds of tokens. Training a language model policy on the full history $h_T$ is computationally expensive and often exceeds the model's context length. This motivates the \textbf{step-independent windowing} approach: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, and each window is optimized independently with its own computed return. Concretely, window $k$ observes only $(o_{(k-1)h+1}, a_{(k-1)h+1}, \ldots, o_{kh})$ and receives a return $R_k$ derived from the episode outcome. This decomposition treats each window as a separate training sample, allowing standard context-length models to process the data. We show below that this seemingly practical choice introduces two failure mechanisms that cause catastrophic training collapse.
10	
11	\subsection{GRPO for Language Agents}
12	\label{sec:grpo}
13	
14	Group Relative Policy Optimization (GRPO)~\cite{shao2024deepseekmath} is a bandit-style policy gradient method designed for language model alignment. Unlike PPO~\cite{schulman2017ppo}, GRPO requires no critic network. For each task instance $x$, the algorithm samples $K$ rollouts $\{y_1, \ldots, y_K\}$ from the current policy $\pi_\phi$. The advantage of each rollout is computed relative to the group:
15	\begin{equation}
16	\hat{A}_k = \frac{R_k - \mu}{\sigma + \epsilon}, \quad \mu = \frac{1}{K}\sum_{j=1}^K R_j, \quad \sigma = \sqrt{\frac{1}{K}\sum_{j=1}^K (R_j - \mu)^2}
17	\label{eq:grpo_advantage}
18	\end{equation}
19	where $R_k$ is the return of rollout $k$. The policy gradient is:
20	\begin{equation}
21	\mathcal{L}_{\text{GRPO}} = -\frac{1}{K}\sum_{k=1}^K \hat{A}_k \cdot \min\left(\rho_k, \text{clip}(\rho_k, 1\pm\epsilon_c)\right) + \beta \cdot D_{\text{KL}}[\pi_\phi \| \pi_{\text{ref}}]
22	\label{eq:grpo_loss}
23	\end{equation}
24	where $\rho_k = \pi_\phi(y_k \mid x) / \pi_{\text{old}}(y_k \mid x)$ is the importance ratio and $\beta$ controls the KL penalty against a reference policy $\pi_{\text{ref}}$. GRPO is \textit{episode-level by design}: each rollout $y_k$ is a complete generation with a single return $R_k$ and a single advantage $\hat{A}_k$. There is no inherent temporal discounting within the algorithm.
25	
26	\subsection{Step-Independent Implementation in Multi-Turn Agents}
27	\label{sec:step_independent}
28	
29	When adapting GRPO for multi-turn interactive tasks, agent training frameworks face a mismatch between GRPO's episode-level design and the practical constraints of long trajectories. The RAGEN framework~\cite{ragen2025} addresses this by introducing step-independent training: each $h$-step window becomes an independent GRPO sample with a discounted return derived from the episode outcome.
30	
31	Specifically, for an episode of $T$ steps with binary outcome $R_{\text{episode}} \in \{0, r_+\}$, the return assigned to window $k$ (covering steps $(k-1)h+1$ through $kh$) is computed as:
32	\begin{equation}
33	R_k = \gamma^{(N - k)} \cdot R_{\text{episode}}
34	\label{eq:step_return}
35	\end{equation}
36	where $N = \lceil T/h \rceil$ is the total number of windows in the episode and $\gamma$ is a discount factor (typically 0.95). In practice, intermediate step penalties (e.g., invalid action penalties) contribute additional terms to $R_k$. Our analysis focuses on the dominant component: the discounted terminal reward. Section~\ref{sec:sign_verification} empirically validates that advantage sign remains episode-outcome-dominated even in the presence of per-step penalties. Each window is then treated as an independent sample in the GRPO optimization and receives its own group-normalized advantage $\hat{A}_k$ via Equation~\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $N$.
37	
38	This design choice is motivated by three practical constraints. First, full trajectories of 50+ turns with hundreds of tokens per turn exceed typical context length limits (2048 or 4096 tokens for smaller models). Second, treating each window independently multiplies the effective batch size, improving GPU utilization. Third, the framework inherits the token-level training paradigm common in language model optimization, where shorter sequences are the default.\footnote{Implementation details are available in the open-source RAGEN codebase, specifically the step-discounted return computation module (\texttt{compute\_step\_discounted\_returns}).}
39	
40	Despite these practical motivations, step-independent training fundamentally alters the credit assignment structure. The following section analyzes two mechanisms through which this alteration causes training collapse.
41	
42	\subsection{Dual Mechanism Analysis}
43	\label{sec:dual_mechanism}
44	
45	We identify two mechanisms operating at different layers that jointly cause training failure under step-independent optimization. The first operates at the inference layer: by restricting the model's observable context, it destroys the policy's ability to generalize to tasks that require cross-step reasoning. The second operates at the training layer: systematic gradient sign errors destabilize the optimization process, producing high-variance training dynamics that range from catastrophic collapse to erratic oscillation. Together, these mechanisms predict three distinct training regimes depending on which mechanism dominates: (a) monotonic collapse when both mechanisms are severe, (b) oscillation followed by degradation when sign misattribution is the primary driver, and (c) stable learning when episode-level training eliminates both. Section~\ref{sec:experiments} validates these predictions empirically.
46	
47	\subsubsection{Mechanism 1: Policy Information Loss}
48	\label{sec:m1_information_loss}
49	
50	Step-independent training truncates context at both the inference and training layers. At inference time, the policy $\pi_\phi(a_t \mid h_{\text{window}_k})$ generates actions conditioned on only the local $h$-step history, losing access to observations and actions from earlier windows. At the training layer, the optimization target for each window is computed from this same truncated context, so cross-step strategies that require conditioning on earlier outcomes cannot be reinforced. Consider a household task requiring the agent to first explore a drawer (step 3), discover an object's location (step 4), then navigate to a countertop (step 8). With $h=2$, the window containing step 8 has no access to the exploration outcome from steps 3--4, neither at inference (the model cannot condition on it) nor at training (the gradient cannot credit it). The policy cannot learn the conditional strategy ``go to countertop \textit{only if} the object was found in the drawer.''
51	
52	This information loss destroys the policy's ability to generalize beyond local, single-window strategies. The model may learn to produce valid actions within its observable context, but it cannot acquire conditional strategies that depend on outcomes from earlier steps. The constraint is structural: no amount of training can recover information that is absent from the input. Different window sizes $h$ impose different degrees of information loss, with smaller $h$ restricting the representable strategy space more severely. In our h-sweep experiments (Section~\ref{sec:experiments}), initial evaluation performance varies across window sizes, reflecting the direct relationship between available context and the policy's generalization capacity.
53	
54	More formally, let $\pi^*$ denote the optimal policy for the full POMDP. The mutual information between $\pi^*$ and the full history, $I(\pi^*; h_T)$, captures the total information required for optimal decision-making. Under $h$-step windowing, each window's policy can access at most $I(\pi^*; h_{\text{window}_k})$. For tasks with sequential dependencies spanning more than $h$ steps, we have $I(\pi^*; h_T) \gg I(\pi^*; h_{\text{window}_k})$. The information gap grows with episode length $T$ and shrinks with window size $h$, predicting a generalization cliff as $h$ decreases relative to the task's dependency horizon.
55	
56	\subsubsection{Mechanism 2: Advantage Sign Misattribution}
57	\label{sec:m2_sign_misattribution}
58	
59	The second mechanism operates at the training layer and, unlike Mechanism 1, directly disrupts the optimization process rather than constraining the representable strategy space. Under step-independent training, each window receives a return $R_k = \gamma^{(N-k)} \cdot R_{\text{episode}}$ (Equation~\ref{eq:step_return}). After group normalization, the advantage $\hat{A}_k$ has a \textit{sign} determined primarily by whether the episode succeeded or failed, not by whether window $k$'s actions were locally good or bad.
60	
61	In a failed episode ($R_{\text{episode}} = 0$), all windows receive $R_k = 0$. If the group mean $\mu > 0$ (due to other successful rollouts in the group), all windows in the failed episode receive negative advantages. This includes windows where the agent took locally correct actions (e.g., correctly identifying a target object). Conversely, in a successful episode, all windows receive positive advantages, including windows where the agent took suboptimal actions (e.g., unnecessary exploration steps that happened not to prevent eventual success).
62	
63	The gradient direction for each window is determined by the sign of $\hat{A}_k$:
64	\begin{equation}
65	\text{sign}(\hat{A}_k) \approx \text{sign}(R_{\text{episode}} - \mu)
66	\label{eq:sign_correlation}
67	\end{equation}
68	This means the optimization either reinforces or suppresses \textit{all} actions within a window based on the episode outcome, regardless of local action quality. Good actions in failed episodes are actively suppressed; bad actions in successful episodes are actively reinforced. Over training, this systematic misattribution corrupts the optimization signal. Even when the policy begins with non-trivial task competence within its $h$-step window, wrong-sign gradient updates can suppress this competence in unpredictable ways. Mechanism 2 breaks training stability: the corrupted gradient signal produces volatile optimization dynamics that may manifest as monotonic collapse, erratic oscillation, or periods of apparent progress followed by sudden degradation. Section~\ref{sec:experiments} confirms these predictions across multiple experimental conditions.
69	
70	A secondary effect compounds this problem. The discount factor $\gamma^{(N-k)}$ introduces magnitude decay across window positions. For early windows in a long episode ($T=50$, $h=2$, $\gamma=0.95$), the first window ($k=1$) retains $\gamma^{N-1} = \gamma^{24} \approx 0.29$ of the terminal window's return. While this reduces the learning signal for early decisions, the sign error is fundamentally more harmful: magnitude decay merely slows convergence, while sign misattribution causes active divergence (Section~\ref{sec:sign_fundamental}).
71	
72	\subsection{Episode-Level Training}
73	\label{sec:episode_level}
74	
75	Episode-level training resolves both failure mechanisms by treating the complete trajectory as a single GRPO sample. All tokens across all $T$ steps share one advantage $\hat{A}$, computed from the episode return $R_{\text{episode}}$ via group normalization over $K$ complete rollouts of the same task instance.
76	
77	This design directly addresses Mechanism 1. The policy $\pi_\phi(a_t \mid h_t)$ conditions on the full interaction history $h_t$ at every step $t$. Cross-step dependencies are preserved in the optimization target: the gradient for generating action $a_8$ (navigate to countertop) flows through the complete history including observations from steps 3--4 (drawer exploration outcome).
78	
79	Episode-level training also eliminates Mechanism 2. Because there is no window-level return assignment, there is no opportunity for sign misattribution between windows. The single advantage $\hat{A}$ applies uniformly to the entire trajectory. While this means per-step credit assignment remains coarse (all steps in a successful episode are equally reinforced), it avoids the worse failure mode of \textit{systematically incorrect} credit assignment. The distinction is critical: uniform reinforcement of a successful trajectory preserves good sub-strategies within it, whereas window-level sign errors actively destroy them.
80	
81	The trade-off is computational. Episode-level training requires processing the full sequence length ($T$ steps $\times$ tokens-per-step) in a single forward and backward pass. For $T=50$ and 100 tokens per step, this amounts to 5000-token sequences, which fits within the capacity of modern architectures but increases memory and compute relative to $h$-step windows. In our experiments (Section~\ref{sec:experiments}), this overhead is modest compared to the catastrophic failure avoided.
82	
83	Episode-level training is, in fact, the natural application of GRPO to multi-turn settings. GRPO was designed as an episode-level algorithm where each rollout receives one return and one advantage. Step-independent training is the deviation from this design, introduced by framework implementation choices rather than algorithmic motivation. Our analysis reveals that this deviation carries hidden costs that become catastrophic for long-horizon interactive tasks.
84	
85	\subsection{Factorial Experiment Design}
86	\label{sec:factorial_design}
87	
88	The dual mechanism analysis yields testable predictions about how each mechanism independently affects training. To isolate their qualitative effects, we design a $2 \times 2$ factorial experiment that varies two factors: (1) the observation window, controlling whether policy information loss (Mechanism 1) is present, and (2) the advantage granularity, controlling whether sign misattribution (Mechanism 2) is present. The four conditions are:
89	
90	\begin{itemize}
91	\item \textbf{Cell A} (truncated observation $+$ step-level advantage): Window size $h{=}2$ with per-window advantage computation. Both mechanisms are active. The policy suffers from information loss \textit{and} receives corrupted gradient signals.
92	\item \textbf{Cell B} (truncated observation $+$ episode-level advantage): Window size $h{=}2$ with a single episode-level advantage shared across all windows. Only Mechanism 1 is active; sign misattribution is eliminated because all windows in an episode receive the same advantage sign.
93	\item \textbf{Cell D} (full observation $+$ episode-level advantage): The complete trajectory is processed as a single sequence with episode-level advantage. Neither mechanism is active.
94	\end{itemize}
95	
96	Comparing Cell A against Cell B isolates the effect of sign misattribution while holding information loss constant. If Cell B exhibits more stable training dynamics than Cell A, the difference is attributable to Mechanism 2. Comparing Cell B against Cell D isolates the effect of information loss while both conditions use episode-level advantage. The performance gap between these two cells reflects how truncated context limits the policy's generalization to tasks with cross-step dependencies.
97	
98	This factorial design tests qualitative predictions about training dynamics, not quantitative effect decomposition. We expect Cell A to exhibit the most unstable training (oscillation or collapse), Cell B to train more stably but plateau below Cell D due to the information constraint, and Cell D to achieve monotonic improvement. Section~\ref{sec:experiments} reports the results.
99	
100	\subsection{Selective Verification}
101	\label{sec:selective_verification}
102	
103	We propose selective verification as a direction for future investigation. At each step, the agent would output a binary decision $v_t \in \{\texttt{VERIFY}, \texttt{SKIP}\}$ before generating its action, and the training signal would use an action-change indicator (whether verification actually altered the action) to reward informative verification. This component has not been implemented and is proposed as a direction for future investigation. Episode-level training serves as a prerequisite: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "4b3ea9ad-b408-44cd-99d4-12a7b0101766",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:problem_formulation}\n\nWe formalize the multi-turn interactive agent as a Partially Observable Markov Decision Process (POMDP) $\\mathcal{M} = (\\mathcal{S}, \\mathcal{A}, \\mathcal{O}, P, \\Omega, R, \\gamma)$, where $\\mathcal{S}$ is the state space of the environment, $\\mathcal{A}$ is the action space (natural language commands), $\\mathcal{O}$ is the observation space (textual feedback from the environment), $P: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathcal{S}$ is the transition function, $\\Omega: \\mathcal{S} \\rightarrow \\mathcal{O}$ is the observation function, $R$ is the reward function, and $\\gamma \\in [0,1]$ is a discount factor. The agent policy $\\pi_\\phi(a_t \\mid h_t)$ generates actions conditioned on the interaction history $h_t = (o_1, a_1, o_2, a_2, \\ldots, o_t)$, where $\\phi$ denotes the policy parameters. An episode consists of $T$ interaction steps, terminating with a binary reward $R \\in \\{0, r_+\\}$ that indicates task success or failure.\n\nIn practice, multi-turn episodes can span 50 or more interaction steps, each containing hundreds of tokens. Training a language model policy on the full history $h_T$ is computationally expensive and often exceeds the model's context length. This motivates the \\textbf{step-independent windowing} approach: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, and each window is optimized independently with its own computed return. Concretely, window $k$ observes only $(o_{(k-1)h+1}, a_{(k-1)h+1}, \\ldots, o_{kh})$ and receives a return $R_k$ derived from the episode outcome. This decomposition treats each window as a separate training sample, allowing standard context-length models to process the data. We show below that this seemingly practical choice introduces two failure mechanisms that cause catastrophic training collapse.\n\n\\subsection{GRPO for Language Agents}\n\\label{sec:grpo}\n\nGroup Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} is a bandit-style policy gradient method designed for language model alignment. Unlike PPO~\\cite{schulman2017ppo}, GRPO requires no critic network. For each task instance $x$, the algorithm samples $K$ rollouts $\\{y_1, \\ldots, y_K\\}$ from the current policy $\\pi_\\phi$. The advantage of each rollout is computed relative to the group:\n\\begin{equation}\n\\hat{A}_k = \\frac{R_k - \\mu}{\\sigma + \\epsilon}, \\quad \\mu = \\frac{1}{K}\\sum_{j=1}^K R_j, \\quad \\sigma = \\sqrt{\\frac{1}{K}\\sum_{j=1}^K (R_j - \\mu)^2}\n\\label{eq:grpo_advantage}\n\\end{equation}\nwhere $R_k$ is the return of rollout $k$. The policy gradient is:\n\\begin{equation}\n\\mathcal{L}_{\\text{GRPO}} = -\\frac{1}{K}\\sum_{k=1}^K \\hat{A}_k \\cdot \\min\\left(\\rho_k, \\text{clip}(\\rho_k, 1\\pm\\epsilon_c)\\right) + \\beta \\cdot D_{\\text{KL}}[\\pi_\\phi \\| \\pi_{\\text{ref}}]\n\\label{eq:grpo_loss}\n\\end{equation}\nwhere $\\rho_k = \\pi_\\phi(y_k \\mid x) / \\pi_{\\text{old}}(y_k \\mid x)$ is the importance ratio and $\\beta$ controls the KL penalty against a reference policy $\\pi_{\\text{ref}}$. GRPO is \\textit{episode-level by design}: each rollout $y_k$ is a complete generation with a single return $R_k$ and a single advantage $\\hat{A}_k$. There is no inherent temporal discounting within the algorithm.\n\n\\subsection{Step-Independent Implementation in Multi-Turn Agents}\n\\label{sec:step_independent}\n\nWhen adapting GRPO for multi-turn interactive tasks, agent training frameworks face a mismatch between GRPO's episode-level design and the practical constraints of long trajectories. The RAGEN framework~\\cite{ragen2025} addresses this by introducing step-independent training: each $h$-step window becomes an independent GRPO sample with a discounted return derived from the episode outcome.\n\nSpecifically, for an episode of $T$ steps with binary outcome $R_{\\text{episode}} \\in \\{0, r_+\\}$, the return assigned to window $k$ (covering steps $(k-1)h+1$ through $kh$) is computed as:\n\\begin{equation}\nR_k = \\gamma^{(N - k)} \\cdot R_{\\text{episode}}\n\\label{eq:step_return}\n\\end{equation}\nwhere $N = \\lceil T/h \\rceil$ is the total number of windows in the episode and $\\gamma$ is a discount factor (typically 0.95). In practice, intermediate step penalties (e.g., invalid action penalties) contribute additional terms to $R_k$. Our analysis focuses on the dominant component: the discounted terminal reward. Section~\\ref{sec:sign_verification} empirically validates that advantage sign remains episode-outcome-dominated even in the presence of per-step penalties. Each window is then treated as an independent sample in the GRPO optimization and receives its own group-normalized advantage $\\hat{A}_k$ via Equation~\\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $N$.\n\nThis design choice is motivated by three practical constraints. First, full trajectories of 50+ turns with hundreds of tokens per turn exceed typical context length limits (2048 or 4096 tokens for smaller models). Second, treating each window independently multiplies the effective batch size, improving GPU utilization. Third, the framework inherits the token-level training paradigm common in language model optimization, where shorter sequences are the default.\\footnote{Implementation details are available in the open-source RAGEN codebase, specifically the step-discounted return computation module (\\texttt{compute\\_step\\_discounted\\_returns}).}\n\nDespite these practical motivations, step-independent training fundamentally alters the credit assignment structure. The following section analyzes two mechanisms through which this alteration causes training collapse.\n\n\\subsection{Dual Mechanism Analysis}\n\\label{sec:dual_mechanism}\n\nWe identify two mechanisms operating at different layers that jointly cause training failure under step-independent optimization. The first operates at the inference layer: by restricting the model's observable context, it destroys the policy's ability to generalize to tasks that require cross-step reasoning. The second operates at the training layer: systematic gradient sign errors destabilize the optimization process, producing high-variance training dynamics that range from catastrophic collapse to erratic oscillation. Together, these mechanisms predict three distinct training regimes depending on which mechanism dominates: (a) monotonic collapse when both mechanisms are severe, (b) oscillation followed by degradation when sign misattribution is the primary driver, and (c) stable learning when episode-level training eliminates both. Section~\\ref{sec:experiments} validates these predictions empirically.\n\n\\subsubsection{Mechanism 1: Policy Information Loss}\n\\label{sec:m1_information_loss}\n\nStep-independent training truncates context at both the inference and training layers. At inference time, the policy $\\pi_\\phi(a_t \\mid h_{\\text{window}_k})$ generates actions conditioned on only the local $h$-step history, losing access to observations and actions from earlier windows. At the training layer, the optimization target for each window is computed from this same truncated context, so cross-step strategies that require conditioning on earlier outcomes cannot be reinforced. Consider a household task requiring the agent to first explore a drawer (step 3), discover an object's location (step 4), then navigate to a countertop (step 8). With $h=2$, the window containing step 8 has no access to the exploration outcome from steps 3--4, neither at inference (the model cannot condition on it) nor at training (the gradient cannot credit it). The policy cannot learn the conditional strategy ``go to countertop \\textit{only if} the object was found in the drawer.''\n\nThis information loss destroys the policy's ability to generalize beyond local, single-window strategies. The model may learn to produce valid actions within its observable context, but it cannot acquire conditional strategies that depend on outcomes from earlier steps. The constraint is structural: no amount of training can recover information that is absent from the input. Different window sizes $h$ impose different degrees of information loss, with smaller $h$ restricting the representable strategy space more severely. In our h-sweep experiments (Section~\\ref{sec:experiments}), initial evaluation performance varies across window sizes, reflecting the direct relationship between available context and the policy's generalization capacity.\n\nMore formally, let $\\pi^*$ denote the optimal policy for the full POMDP. The mutual information between $\\pi^*$ and the full history, $I(\\pi^*; h_T)$, captures the total information required for optimal decision-making. Under $h$-step windowing, each window's policy can access at most $I(\\pi^*; h_{\\text{window}_k})$. For tasks with sequential dependencies spanning more than $h$ steps, we have $I(\\pi^*; h_T) \\gg I(\\pi^*; h_{\\text{window}_k})$. The information gap grows with episode length $T$ and shrinks with window size $h$, predicting a generalization cliff as $h$ decreases relative to the task's dependency horizon.\n\n\\subsubsection{Mechanism 2: Advantage Sign Misattribution}\n\\label{sec:m2_sign_misattribution}\n\nThe second mechanism operates at the training layer and, unlike Mechanism 1, directly disrupts the optimization process rather than constraining the representable strategy space. Under step-independent training, each window receives a return $R_k = \\gamma^{(N-k)} \\cdot R_{\\text{episode}}$ (Equation~\\ref{eq:step_return}). After group normalization, the advantage $\\hat{A}_k$ has a \\textit{sign} determined primarily by whether the episode succeeded or failed, not by whether window $k$'s actions were locally good or bad.\n\nIn a failed episode ($R_{\\text{episode}} = 0$), all windows receive $R_k = 0$. If the group mean $\\mu > 0$ (due to other successful rollouts in the group), all windows in the failed episode receive negative advantages. This includes windows where the agent took locally correct actions (e.g., correctly identifying a target object). Conversely, in a successful episode, all windows receive positive advantages, including windows where the agent took suboptimal actions (e.g., unnecessary exploration steps that happened not to prevent eventual success).\n\nThe gradient direction for each window is determined by the sign of $\\hat{A}_k$:\n\\begin{equation}\n\\text{sign}(\\hat{A}_k) \\approx \\text{sign}(R_{\\text{episode}} - \\mu)\n\\label{eq:sign_correlation}\n\\end{equation}\nThis means the optimization either reinforces or suppresses \\textit{all} actions within a window based on the episode outcome, regardless of local action quality. Good actions in failed episodes are actively suppressed; bad actions in successful episodes are actively reinforced. Over training, this systematic misattribution corrupts the optimization signal. Even when the policy begins with non-trivial task competence within its $h$-step window, wrong-sign gradient updates can suppress this competence in unpredictable ways. Mechanism 2 breaks training stability: the corrupted gradient signal produces volatile optimization dynamics that may manifest as monotonic collapse, erratic oscillation, or periods of apparent progress followed by sudden degradation. Section~\\ref{sec:experiments} confirms these predictions across multiple experimental conditions.\n\nA secondary effect compounds this problem. The discount factor $\\gamma^{(N-k)}$ introduces magnitude decay across window positions. For early windows in a long episode ($T=50$, $h=2$, $\\gamma=0.95$), the first window ($k=1$) retains $\\gamma^{N-1} = \\gamma^{24} \\approx 0.29$ of the terminal window's return. While this reduces the learning signal for early decisions, the sign error is fundamentally more harmful: magnitude decay merely slows convergence, while sign misattribution causes active divergence (Section~\\ref{sec:sign_fundamental}).\n\n\\subsection{Episode-Level Training}\n\\label{sec:episode_level}\n\nEpisode-level training resolves both failure mechanisms by treating the complete trajectory as a single GRPO sample. All tokens across all $T$ steps share one advantage $\\hat{A}$, computed from the episode return $R_{\\text{episode}}$ via group normalization over $K$ complete rollouts of the same task instance.\n\nThis design directly addresses Mechanism 1. The policy $\\pi_\\phi(a_t \\mid h_t)$ conditions on the full interaction history $h_t$ at every step $t$. Cross-step dependencies are preserved in the optimization target: the gradient for generating action $a_8$ (navigate to countertop) flows through the complete history including observations from steps 3--4 (drawer exploration outcome).\n\nEpisode-level training also eliminates Mechanism 2. Because there is no window-level return assignment, there is no opportunity for sign misattribution between windows. The single advantage $\\hat{A}$ applies uniformly to the entire trajectory. While this means per-step credit assignment remains coarse (all steps in a successful episode are equally reinforced), it avoids the worse failure mode of \\textit{systematically incorrect} credit assignment. The distinction is critical: uniform reinforcement of a successful trajectory preserves good sub-strategies within it, whereas window-level sign errors actively destroy them.\n\nThe trade-off is computational. Episode-level training requires processing the full sequence length ($T$ steps $\\times$ tokens-per-step) in a single forward and backward pass. For $T=50$ and 100 tokens per step, this amounts to 5000-token sequences, which fits within the capacity of modern architectures but increases memory and compute relative to $h$-step windows. In our experiments (Section~\\ref{sec:experiments}), this overhead is modest compared to the catastrophic failure avoided.\n\nEpisode-level training is, in fact, the natural application of GRPO to multi-turn settings. GRPO was designed as an episode-level algorithm where each rollout receives one return and one advantage. Step-independent training is the deviation from this design, introduced by framework implementation choices rather than algorithmic motivation. Our analysis reveals that this deviation carries hidden costs that become catastrophic for long-horizon interactive tasks.\n\n\\subsection{Factorial Experiment Design}\n\\label{sec:factorial_design}\n\nThe dual mechanism analysis yields testable predictions about how each mechanism independently affects training. To isolate their qualitative effects, we design a $2 \\times 2$ factorial experiment that varies two factors: (1) the observation window, controlling whether policy information loss (Mechanism 1) is present, and (2) the advantage granularity, controlling whether sign misattribution (Mechanism 2) is present. The four conditions are:\n\n\\begin{itemize}\n\\item \\textbf{Cell A} (truncated observation $+$ step-level advantage): Window size $h{=}2$ with per-window advantage computation. Both mechanisms are active. The policy suffers from information loss \\textit{and} receives corrupted gradient signals.\n\\item \\textbf{Cell B} (truncated observation $+$ episode-level advantage): Window size $h{=}2$ with a single episode-level advantage shared across all windows. Only Mechanism 1 is active; sign misattribution is eliminated because all windows in an episode receive the same advantage sign.\n\\item \\textbf{Cell D} (full observation $+$ episode-level advantage): The complete trajectory is processed as a single sequence with episode-level advantage. Neither mechanism is active.\n\\end{itemize}\n\nComparing Cell A against Cell B isolates the effect of sign misattribution while holding information loss constant. If Cell B exhibits more stable training dynamics than Cell A, the difference is attributable to Mechanism 2. Comparing Cell B against Cell D isolates the effect of information loss while both conditions use episode-level advantage. The performance gap between these two cells reflects how truncated context limits the policy's generalization to tasks with cross-step dependencies.\n\nThis factorial design tests qualitative predictions about training dynamics, not quantitative effect decomposition. We expect Cell A to exhibit the most unstable training (oscillation or collapse), Cell B to train more stably but plateau below Cell D due to the information constraint, and Cell D to achieve monotonic improvement. Section~\\ref{sec:experiments} reports the results.\n\n\\subsection{Selective Verification}\n\\label{sec:selective_verification}\n\nWe propose selective verification as a direction for future investigation. At each step, the agent would output a binary decision $v_t \\in \\{\\texttt{VERIFY}, \\texttt{SKIP}\\}$ before generating its action, and the training signal would use an action-change indicator (whether verification actually altered the action) to reward informative verification. This component has not been implemented and is proposed as a direction for future investigation. Episode-level training serves as a prerequisite: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.",
      "numLines": 103,
      "startLine": 1,
      "totalLines": 103
    }
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Let me verify the file against the requirements:

1. ✅ §3.1 Problem Formulation - unchanged
2. ✅ §3.2 GRPO for Language Agents - unchanged
3. ✅ §3.3 Step-Independent Implementation - unchanged
4. ✅ §3.4 Dual Mechanism Analysis - reframed per D073:
   - ✅ M1: "destroys the policy's ability to generalize" instead of "establishes ceiling"
   - ✅ M2: "breaks training stability", "volatile optimization dynamics" instead of "cumulative"
   - ✅ Three training regimes predicted: monotonic collapse, oscillation-then-degradation, stable learning
   - ✅ No quantitative percentage decomposition
5. ✅ §3.5 Episode-Level Training - unchanged
6. ✅ §3.6 Factorial Experiment Design - new section added
7. ✅ §3.7 Selective Verification - shortened

Now checking for style issues like em-dashes and -ing phrase endings to ensure consistency with the document's conventions.

I need to verify whether the removed equation label and citation are referenced elsewhere in the paper, since deleting them could break cross-references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "8e41eb98-af1b-43be-aec9-f404422bdab4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017crgbZznnxNY3V2uFu7jvc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4584,
      "cache_read_input_tokens": 51399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4584
      },
      "output_tokens": 8,
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

_source line 31_

Let me check for any references to removed labels or citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "d011e5b4-e895-4a2f-bf32-78e08e8bcf67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017crgbZznnxNY3V2uFu7jvc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4584,
      "cache_read_input_tokens": 51399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4584
      },
      "output_tokens": 8,
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

_source line 32_

<details open><summary>🔧 Tool call — Grep · `toolu_01MKKive7AGi7SxsSzUuZNvx`</summary>

```json
{
  "pattern": "action_change|long2026selfverification|selective_experiments",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "141766da-86e8-4bdf-975f-00bbef261eb2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017crgbZznnxNY3V2uFu7jvc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4584,
      "cache_read_input_tokens": 51399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4584
      },
      "output_tokens": 8,
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

_source line 33 · 2026-05-18T12:09:53.877Z_

<details><summary>↩ Tool result · `toolu_01MKKive7AGi7SxsSzUuZNvx`</summary>

```text
docs/paper/related_work.tex:14:[Omitted long matching line]
docs/paper/experiments.tex:121:\label{sec:selective_experiments}
docs/paper/references.bib:85:@article{long2026selfverification,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "f347e171-e40c-4a24-a491-27be144270ef",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:14:[Omitted long matching line]\ndocs/paper/experiments.tex:121:\\label{sec:selective_experiments}\ndocs/paper/references.bib:85:@article{long2026selfverification,",
    "numLines": 3
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Grep · `toolu_01JabkRjEiPZqBRMovpRAe2G`</summary>

```json
{
  "pattern": "—|\" – \"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "e0e9df1d-1b0b-4b7a-9489-6cc942e23bf3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017crgbZznnxNY3V2uFu7jvc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4584,
      "cache_read_input_tokens": 51399,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4584
      },
      "output_tokens": 8,
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

_source line 35 · 2026-05-18T12:09:54.648Z_

<details><summary>↩ Tool result · `toolu_01JabkRjEiPZqBRMovpRAe2G`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "93ca816a-33e5-4a29-a540-46b7a7bc3f3c",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
The `sec:selective_experiments` label exists in experiments.tex (line 121), but the reference to it was removed from method.tex. That's fine because the method section no longer needs to reference the detailed experimental section. The `\label{sec:selective_experiments}` still exists in experiments.tex, so it won't cause a compilation error.

The `long2026selfverification` citation exists in references.bib and is also referenced in related_work.tex. So it's still being cited elsewhere. No broken reference issue.


Now I need to check if the `eq:action_change` label that was removed is referenced anywhere else in the document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "a4685b56-a042-4d49-8ae5-ba81d3cbf7a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhUaDX4tHc4g5Z8J5ZhgEN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 55983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 944
      },
      "output_tokens": 8,
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

_source line 37_

<details open><summary>🔧 Tool call — Grep · `toolu_01MKtYWYpjRAzDQRaFH9ZRPx`</summary>

```json
{
  "pattern": "eq:action_change",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "b9d4b0dd-6a0d-4d9b-8747-41d5fcb93d95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LhUaDX4tHc4g5Z8J5ZhgEN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 55983,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 944
      },
      "output_tokens": 8,
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

_source line 38 · 2026-05-18T12:10:01.533Z_

<details><summary>↩ Tool result · `toolu_01MKtYWYpjRAzDQRaFH9ZRPx`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "5d9225af-2279-4b37-8efc-0223019fd1f7",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Assistant

_source line 39_

No broken references. No em-dashes or en-dashes in the file. All labels preserved. The `long2026selfverification` citation is still used in related_work.tex so the bib entry won't be orphaned.

Changes made to `method.tex`:

- **§3.4 intro**: Replaced "ceiling" + "cumulative degradation" framing with D073 narrative. Now predicts three training regimes: (a) monotonic collapse, (b) oscillation-then-degradation, (c) stable learning.
- **M1**: "destroys generalization ability" replaces "establishes ceiling". Model can learn local strategies but cannot generalize to cross-step reasoning tasks.
- **M2**: "breaks training stability" replaces "cumulative erosion". Volatile, unpredictable optimization dynamics instead of progressive degradation.
- **§3.6 (new)**: Factorial experiment design. 2x2 (observation window x advantage granularity) with Cells A/B/D. Emphasizes qualitative separation, not quantitative decomposition.
- **§3.7 (shortened)**: Selective Verification reduced from ~250 words to ~80 words. Formula removed. Marked as unimplemented future direction.

[WORKER DONE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "uuid": "e3be9ff7-c52f-4cf6-b0c5-1988fc34becc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XrZbRbbdZt6nbypUWMkmAZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 295,
      "cache_read_input_tokens": 56927,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 295
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

### Runtime record

_source line 40_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779124200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "57f610d6-c836-4f77-b263-b85cc1254163",
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519"
}
```

---

### Task result

_source line 41_

No broken references. No em-dashes or en-dashes in the file. All labels preserved. The `long2026selfverification` citation is still used in related_work.tex so the bib entry won't be orphaned.

Changes made to `method.tex`:

- **§3.4 intro**: Replaced "ceiling" + "cumulative degradation" framing with D073 narrative. Now predicts three training regimes: (a) monotonic collapse, (b) oscillation-then-degradation, (c) stable learning.
- **M1**: "destroys generalization ability" replaces "establishes ceiling". Model can learn local strategies but cannot generalize to cross-step reasoning tasks.
- **M2**: "breaks training stability" replaces "cumulative erosion". Volatile, unpredictable optimization dynamics instead of progressive degradation.
- **§3.6 (new)**: Factorial experiment design. 2x2 (observation window x advantage granularity) with Cells A/B/D. Emphasizes qualitative separation, not quantitative decomposition.
- **§3.7 (shortened)**: Selective Verification reduced from ~250 words to ~80 words. Formula removed. Marked as unimplemented future direction.

[WORKER DONE]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 224592,
  "duration_api_ms": 225675,
  "num_turns": 14,
  "stop_reason": "end_turn",
  "session_id": "ea96cb5f-dc44-4b86-a8bf-5ffd4920b519",
  "total_cost_usd": 0.8109312500000001,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 45381,
    "cache_read_input_tokens": 491184,
    "output_tokens": 11140,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 45381,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 297,
        "cache_read_input_tokens": 56927,
        "cache_creation_input_tokens": 295,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 295
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3053,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003148,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 11140,
      "cacheReadInputTokens": 491184,
      "cacheCreationInputTokens": 45381,
      "webSearchRequests": 0,
      "costUSD": 0.80778325,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3c60ae89-0e6e-4dd7-8334-fc27fefbb994"
}
```

</details>

---
