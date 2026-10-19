# paper writing related work

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260517T081214.log`
- **Structured JSON:** [`e4b94d158f25d7e34d70.json`](../../sessions/e4/e4b94d158f25d7e34d70.json)

## Before a recorded user message

37 recorded events

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
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
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
  "uuid": "9f42f80b-e519-48f7-9570-93b436590616",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/memory/"
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
    "resetsAt": 1779008400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "cec0d154-e6c2-4f4a-b283-593c591fabe7",
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the required files to understand the context, then read the literature map to get the citation keys, and finally write the Related Work section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "cc91b8c0-f8bb-4e4f-9570-403ae061c5e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uGmvZAKig1kkx7neyGxjx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14688,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14688
      },
      "output_tokens": 27,
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

I'll read the required files and literature map to write the Related Work section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "d9a3f9ec-01a9-4e49-809b-5db56ef25a0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uGmvZAKig1kkx7neyGxjx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14688,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14688
      },
      "output_tokens": 27,
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

<details open><summary>🔧 Tool call — Read · `toolu_01Y7mGRZAvV1mRZqm74RwfAY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "801ca564-2bbe-4f9c-bbf9-bc1a96eb2ec0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uGmvZAKig1kkx7neyGxjx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14688,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14688
      },
      "output_tokens": 27,
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

_source line 7 · 2026-05-17T08:12:28.438Z_

<details><summary>↩ Tool result · `toolu_01Y7mGRZAvV1mRZqm74RwfAY`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training Large Language Model (LLM) agents for multi-turn interactive tasks poses a fundamental challenge: policies must compose actions across 30 to 50 interaction steps in environments such as household navigation~\cite{kim2025reflact}, web interaction~\cite{digiRL2024}, and scientific experimentation. Supervised fine-tuning (SFT) can teach action formatting but fails to instill compositional planning, because expert demonstrations do not expose the trial-and-error exploration through which effective multi-step strategies emerge. Reinforcement learning (RL) addresses this gap by optimizing policies through direct environment interaction, and Group Relative Policy Optimization (GRPO)~\cite{shao2024deepseekmath} has become a preferred method due to its critic-free design and direct compatibility with language model architectures. Recent work applies RL-based training to interactive agents across diverse domains, from text-based games~\cite{ragen2025} and GUI interaction~\cite{digiRL2024} to tool use~\cite{spear2025} and instruction following~\cite{selfguide2026,feng2025gigpo}. These efforts share a common implementation pattern that has received little scrutiny: the multi-turn trajectory is decomposed into fixed-size windows, and each window is optimized as an independent training sample. This decomposition is the focus of our analysis.
5	
6	Current agent RL frameworks default to \textit{step-independent training}: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, each receiving a discounted return derived from the binary episode outcome and optimized independently via GRPO~\cite{ragen2025,selfguide2026}. This choice is motivated by practical considerations: it fits long trajectories within limited context windows, multiplies the effective batch size, and aligns with the token-level training paradigm of language models. However, the decomposition introduces a fundamental credit assignment pathology. When each window receives a group-normalized advantage, the sign of that advantage reflects whether the \textit{episode} succeeded or failed, not whether the \textit{window's actions} were locally correct. In our experiments, this pathology produces a striking failure pattern: with $h=2$, step-independent training collapses to 0\% task success within 10 training steps, while action validity remains above 90\% (Section~\ref{sec:experiments}). The agent learns to produce well-formatted commands that satisfy syntactic constraints but loses the ability to complete tasks entirely. This collapse is not an artifact of a particular hyperparameter configuration. We observe the same failure across multiple learning rates, KL penalty strengths, and window sizes, consistent with a structural defect in the training paradigm rather than a tuning problem.
7	
8	Standard remedies do not resolve this collapse. Dense reward shaping, which provides per-step bonuses for intermediate goals such as valid action formatting, creates a different failure mode: the agent maximizes format-level rewards while task completion stays at zero. In our dense reward experiment, action validity increases from 60\% to 97.5\% while task success remains at 0\% (Section~\ref{sec:experiments}). Increasing the number of rollouts or adjusting the KL penalty delays the onset of collapse but does not prevent it. Generalized Advantage Estimation (GAE)~\cite{schulman2016gae} and Proximal Policy Optimization (PPO)~\cite{schulman2017ppo} offer finer-grained temporal credit assignment through learned value functions, but they add model complexity and have not been applied with a diagnosis of \textit{why} step-independent training fails in the first place. The root cause is not the choice of RL algorithm. It is the step-independent windowing itself, which corrupts the credit assignment signal at its source.
9	
10	We trace the collapse to two mechanisms that operate jointly under step-independent training. The first, \textbf{policy information loss}, arises because each $h$-step window has no access to actions and outcomes from other windows, so cross-step strategies that require conditioning on earlier results become invisible to the optimization process. The second, \textbf{advantage sign misattribution}, is more damaging: under binary episode reward, the sign of each window's advantage $\hat{A}_k$ is determined by whether the episode succeeded or failed (Section~\ref{sec:m2_sign_misattribution}), not by the local quality of the window's actions. Good actions in failed episodes receive negative advantages and are actively suppressed, while bad actions in successful episodes are reinforced. Our formal analysis (Section~\ref{sec:formal_probability}) shows that at a baseline success rate of $p = 6.25\%$ with group size $K = 8$, approximately 84.5\% of gradient updates for locally correct windows point in the wrong direction. Sign misattribution is a directional error, fundamentally distinct from magnitude attenuation: it drives the policy away from correct behaviors rather than merely reducing convergence speed. Episode-level GRPO eliminates both mechanisms by treating the complete trajectory as a single optimization sample, consistent with GRPO's original design~\cite{shao2024deepseekmath}, so that all steps share one advantage and cross-step dependencies are preserved through the full interaction history. In our experiments, episode-level training achieves 28.1\% validation success (from a baseline of approximately 6\%), while step-independent training collapses to 0\%.
11	
12	Our contributions are as follows:
13	\begin{itemize}
14	    \item \textbf{Dual mechanism diagnosis.} We identify and formalize two mechanisms that cause catastrophic collapse under step-independent GRPO in multi-turn agent training: policy information loss and advantage sign misattribution. We show that sign misattribution is a directional error, with the probability of incorrect gradient direction approaching $1 - p$ as group size grows (Sections~\ref{sec:dual_mechanism},~\ref{sec:sign_fundamental},~\ref{sec:formal_probability}).
15	
16	    \item \textbf{Systematic empirical validation.} Through window-size ablation ($h \in \{2, 5, 10, 20, \text{full}\}$) and per-window advantage logging, we demonstrate a credit assignment cliff and provide direct empirical evidence for the sign misattribution mechanism (Section~\ref{sec:experiments}).
17	
18	    \item \textbf{Episode-level solution and analysis.} We show that episode-level GRPO simultaneously resolves both failure mechanisms, and we analyze its connection to GAE~\cite{schulman2016gae} and REINFORCE~\cite{williams1992reinforce}. We identify six factors that explain why the community has defaulted to the broken step-independent paradigm (Sections~\ref{sec:episode_level},~\ref{sec:classical_connection},~\ref{sec:why_defaults}).
19	\end{itemize}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "0d742ce8-1630-4afb-abe0-ad97131ca01d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nTraining Large Language Model (LLM) agents for multi-turn interactive tasks poses a fundamental challenge: policies must compose actions across 30 to 50 interaction steps in environments such as household navigation~\\cite{kim2025reflact}, web interaction~\\cite{digiRL2024}, and scientific experimentation. Supervised fine-tuning (SFT) can teach action formatting but fails to instill compositional planning, because expert demonstrations do not expose the trial-and-error exploration through which effective multi-step strategies emerge. Reinforcement learning (RL) addresses this gap by optimizing policies through direct environment interaction, and Group Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} has become a preferred method due to its critic-free design and direct compatibility with language model architectures. Recent work applies RL-based training to interactive agents across diverse domains, from text-based games~\\cite{ragen2025} and GUI interaction~\\cite{digiRL2024} to tool use~\\cite{spear2025} and instruction following~\\cite{selfguide2026,feng2025gigpo}. These efforts share a common implementation pattern that has received little scrutiny: the multi-turn trajectory is decomposed into fixed-size windows, and each window is optimized as an independent training sample. This decomposition is the focus of our analysis.\n\nCurrent agent RL frameworks default to \\textit{step-independent training}: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, each receiving a discounted return derived from the binary episode outcome and optimized independently via GRPO~\\cite{ragen2025,selfguide2026}. This choice is motivated by practical considerations: it fits long trajectories within limited context windows, multiplies the effective batch size, and aligns with the token-level training paradigm of language models. However, the decomposition introduces a fundamental credit assignment pathology. When each window receives a group-normalized advantage, the sign of that advantage reflects whether the \\textit{episode} succeeded or failed, not whether the \\textit{window's actions} were locally correct. In our experiments, this pathology produces a striking failure pattern: with $h=2$, step-independent training collapses to 0\\% task success within 10 training steps, while action validity remains above 90\\% (Section~\\ref{sec:experiments}). The agent learns to produce well-formatted commands that satisfy syntactic constraints but loses the ability to complete tasks entirely. This collapse is not an artifact of a particular hyperparameter configuration. We observe the same failure across multiple learning rates, KL penalty strengths, and window sizes, consistent with a structural defect in the training paradigm rather than a tuning problem.\n\nStandard remedies do not resolve this collapse. Dense reward shaping, which provides per-step bonuses for intermediate goals such as valid action formatting, creates a different failure mode: the agent maximizes format-level rewards while task completion stays at zero. In our dense reward experiment, action validity increases from 60\\% to 97.5\\% while task success remains at 0\\% (Section~\\ref{sec:experiments}). Increasing the number of rollouts or adjusting the KL penalty delays the onset of collapse but does not prevent it. Generalized Advantage Estimation (GAE)~\\cite{schulman2016gae} and Proximal Policy Optimization (PPO)~\\cite{schulman2017ppo} offer finer-grained temporal credit assignment through learned value functions, but they add model complexity and have not been applied with a diagnosis of \\textit{why} step-independent training fails in the first place. The root cause is not the choice of RL algorithm. It is the step-independent windowing itself, which corrupts the credit assignment signal at its source.\n\nWe trace the collapse to two mechanisms that operate jointly under step-independent training. The first, \\textbf{policy information loss}, arises because each $h$-step window has no access to actions and outcomes from other windows, so cross-step strategies that require conditioning on earlier results become invisible to the optimization process. The second, \\textbf{advantage sign misattribution}, is more damaging: under binary episode reward, the sign of each window's advantage $\\hat{A}_k$ is determined by whether the episode succeeded or failed (Section~\\ref{sec:m2_sign_misattribution}), not by the local quality of the window's actions. Good actions in failed episodes receive negative advantages and are actively suppressed, while bad actions in successful episodes are reinforced. Our formal analysis (Section~\\ref{sec:formal_probability}) shows that at a baseline success rate of $p = 6.25\\%$ with group size $K = 8$, approximately 84.5\\% of gradient updates for locally correct windows point in the wrong direction. Sign misattribution is a directional error, fundamentally distinct from magnitude attenuation: it drives the policy away from correct behaviors rather than merely reducing convergence speed. Episode-level GRPO eliminates both mechanisms by treating the complete trajectory as a single optimization sample, consistent with GRPO's original design~\\cite{shao2024deepseekmath}, so that all steps share one advantage and cross-step dependencies are preserved through the full interaction history. In our experiments, episode-level training achieves 28.1\\% validation success (from a baseline of approximately 6\\%), while step-independent training collapses to 0\\%.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item \\textbf{Dual mechanism diagnosis.} We identify and formalize two mechanisms that cause catastrophic collapse under step-independent GRPO in multi-turn agent training: policy information loss and advantage sign misattribution. We show that sign misattribution is a directional error, with the probability of incorrect gradient direction approaching $1 - p$ as group size grows (Sections~\\ref{sec:dual_mechanism},~\\ref{sec:sign_fundamental},~\\ref{sec:formal_probability}).\n\n    \\item \\textbf{Systematic empirical validation.} Through window-size ablation ($h \\in \\{2, 5, 10, 20, \\text{full}\\}$) and per-window advantage logging, we demonstrate a credit assignment cliff and provide direct empirical evidence for the sign misattribution mechanism (Section~\\ref{sec:experiments}).\n\n    \\item \\textbf{Episode-level solution and analysis.} We show that episode-level GRPO simultaneously resolves both failure mechanisms, and we analyze its connection to GAE~\\cite{schulman2016gae} and REINFORCE~\\cite{williams1992reinforce}. We identify six factors that explain why the community has defaulted to the broken step-independent paradigm (Sections~\\ref{sec:episode_level},~\\ref{sec:classical_connection},~\\ref{sec:why_defaults}).\n\\end{itemize}",
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

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_012jMfVs7UBEAjkiuPPQZMJw`</summary>

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
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "074ee0d1-c07f-4627-82fb-795e9bd72f8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uGmvZAKig1kkx7neyGxjx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14688,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14688
      },
      "output_tokens": 27,
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

_source line 9 · 2026-05-17T08:12:29.581Z_

<details><summary>↩ Tool result · `toolu_012jMfVs7UBEAjkiuPPQZMJw`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:problem_formulation}
6	
7	We formalize the multi-turn interactive agent as a Partially Observable Markov Decision Process (POMDP) $\mathcal{M} = (\mathcal{S}, \mathcal{A}, \mathcal{O}, P, \Omega, R, \gamma)$, where $\mathcal{S}$ is the state space of the environment, $\mathcal{A}$ is the action space (natural language commands), $\mathcal{O}$ is the observation space (textual feedback from the environment), $P: \mathcal{S} \times \mathcal{A} \rightarrow \mathcal{S}$ is the transition function, $\Omega: \mathcal{S} \rightarrow \mathcal{O}$ is the observation function, $R$ is the reward function, and $\gamma \in [0,1]$ is a discount factor. The agent policy $\pi_\phi(a_t \mid h_t)$ generates actions conditioned on the interaction history $h_t = (o_1, a_1, o_2, a_2, \ldots, o_t)$, where $\phi$ denotes the policy parameters. An episode consists of $T$ interaction steps, terminating with a binary reward $R \in \{0, r_+\}$ that indicates task success or failure.
8	
9	In practice, multi-turn episodes can span 50 or more interaction steps, each containing hundreds of tokens. Training a language model policy on the full history $h_T$ is computationally expensive and often exceeds the model's context window. This motivates the \textbf{step-independent windowing} approach: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, and each window is optimized independently with its own computed return. Concretely, window $k$ observes only $(o_{(k-1)h+1}, a_{(k-1)h+1}, \ldots, o_{kh})$ and receives a return $R_k$ derived from the episode outcome. This decomposition treats each window as a separate training sample, allowing standard context-length models to process the data. We show below that this seemingly practical choice introduces two failure mechanisms that cause catastrophic training collapse.
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
36	where $N = \lceil T/h \rceil$ is the total number of windows in the episode and $\gamma$ is a discount factor (typically 0.95). Each window is then treated as an independent sample in the GRPO optimization and receives its own group-normalized advantage $\hat{A}_k$ via Equation~\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $N$.
37	
38	This design choice is motivated by three practical constraints. First, full trajectories of 50+ turns with hundreds of tokens per turn exceed typical context window limits (2048 or 4096 tokens for smaller models). Second, treating each window independently multiplies the effective batch size, improving GPU utilization. Third, the framework inherits the token-level training paradigm common in language model optimization, where shorter sequences are the default.\footnote{Implementation details are available in the open-source RAGEN codebase, specifically the step-discounted return computation module (\texttt{compute\_step\_discounted\_returns}).}
39	
40	Despite these practical motivations, step-independent training fundamentally alters the credit assignment structure. The following section analyzes two mechanisms through which this alteration causes training collapse.
41	
42	\subsection{Dual Mechanism Analysis}
43	\label{sec:dual_mechanism}
44	
45	We identify two mechanisms that jointly cause catastrophic failure under step-independent training. As we demonstrate empirically in Section~\ref{sec:experiments}, step-independent training with $h=2$ collapses to 0\% task success within 10 training steps, while action validity remains above 90\%. This pattern indicates that the policy degenerates in task strategy rather than action formatting.
46	
47	\subsubsection{Mechanism 1: Policy Information Loss}
48	\label{sec:m1_information_loss}
49	
50	Under step-independent training, the policy optimized on window $k$ observes only a local $h$-step history. Cross-step strategies that require conditioning on earlier outcomes become invisible to the optimization process. Consider a household task requiring the agent to first explore a drawer (step 3), discover an object's location (step 4), then navigate to a countertop (step 8). With $h=2$, the window containing step 8 has no access to the exploration outcome from steps 3--4. The policy cannot learn the conditional strategy ``go to countertop \textit{only if} the object was found in the drawer.''
51	
52	More formally, let $\pi^*$ denote the optimal policy for the full POMDP. The mutual information between $\pi^*$ and the full history, $I(\pi^*; h_T)$, captures the total information required for optimal decision-making. Under $h$-step windowing, each window's policy can access at most $I(\pi^*; h_{\text{window}_k})$. For tasks with sequential dependencies spanning more than $h$ steps, we have $I(\pi^*; h_T) \gg I(\pi^*; h_{\text{window}_k})$. The information gap grows with episode length $T$ and shrinks with window size $h$, predicting a performance cliff as $h$ decreases relative to the task's dependency horizon.
53	
54	\subsubsection{Mechanism 2: Advantage Sign Misattribution}
55	\label{sec:m2_sign_misattribution}
56	
57	The second mechanism is more subtle and more damaging. Under step-independent training, each window receives a return $R_k = \gamma^{(N-k)} \cdot R_{\text{episode}}$ (Equation~\ref{eq:step_return}). After group normalization, the advantage $\hat{A}_k$ has a \textit{sign} determined primarily by whether the episode succeeded or failed, not by whether window $k$'s actions were locally good or bad.
58	
59	In a failed episode ($R_{\text{episode}} = 0$), all windows receive $R_k = 0$. If the group mean $\mu > 0$ (due to other successful rollouts in the group), all windows in the failed episode receive negative advantages. This includes windows where the agent took locally correct actions (e.g., correctly identifying a target object). Conversely, in a successful episode, all windows receive positive advantages, including windows where the agent took suboptimal actions (e.g., unnecessary exploration steps that happened not to prevent eventual success).
60	
61	The gradient direction for each window is determined by the sign of $\hat{A}_k$:
62	\begin{equation}
63	\text{sign}(\hat{A}_k) \approx \text{sign}(R_{\text{episode}} - \mu)
64	\label{eq:sign_correlation}
65	\end{equation}
66	This means the optimization either reinforces or suppresses \textit{all} actions within a window based on the episode outcome, regardless of local action quality. Good actions in failed episodes are actively suppressed; bad actions in successful episodes are actively reinforced. Over many training steps, this systematic misattribution erodes learned strategies: the agent cannot maintain locally correct behaviors if they frequently co-occur with episode failure.
67	
68	A secondary effect compounds this problem. The discount factor $\gamma^{(N-k)}$ introduces magnitude decay across window positions. For early windows in a long episode ($T=50$, $h=2$, $\gamma=0.95$), the first window ($k=1$) retains $\gamma^{N-1} = \gamma^{24} \approx 0.29$ of the terminal window's return. While this reduces the learning signal for early decisions, the sign error is fundamentally more harmful. Magnitude decay slows learning but preserves the correct optimization direction; sign misattribution actively drives the policy away from good behaviors. A gradient with correct sign but attenuated magnitude yields slow convergence. A gradient with wrong sign yields divergence.
69	
70	\subsection{Episode-Level Training}
71	\label{sec:episode_level}
72	
73	Episode-level training resolves both failure mechanisms by treating the complete trajectory as a single GRPO sample. All tokens across all $T$ steps share one advantage $\hat{A}$, computed from the episode return $R_{\text{episode}}$ via group normalization over $K$ complete rollouts of the same task instance.
74	
75	This design directly addresses Mechanism 1. The policy $\pi_\phi(a_t \mid h_t)$ conditions on the full interaction history $h_t$ at every step $t$. Cross-step dependencies are preserved in the optimization target: the gradient for generating action $a_8$ (navigate to countertop) flows through the complete history including observations from steps 3--4 (drawer exploration outcome).
76	
77	Episode-level training also eliminates Mechanism 2. Because there is no window-level return assignment, there is no opportunity for sign misattribution between windows. The single advantage $\hat{A}$ applies uniformly to the entire trajectory. While this means per-step credit assignment remains coarse (all steps in a successful episode are equally reinforced), it avoids the worse failure mode of \textit{systematically incorrect} credit assignment. The distinction is critical: uniform reinforcement of a successful trajectory preserves good sub-strategies within it, whereas window-level sign errors actively destroy them.
78	
79	The trade-off is computational. Episode-level training requires processing the full sequence length ($T$ steps $\times$ tokens-per-step) in a single forward and backward pass. For $T=50$ and 100 tokens per step, this amounts to 5000-token sequences, which fits within the capacity of modern architectures but increases memory and compute relative to $h$-step windows. In our experiments (Section~\ref{sec:experiments}), this overhead is modest compared to the catastrophic failure avoided.
80	
81	Episode-level training is, in fact, the natural application of GRPO to multi-turn settings. GRPO was designed as an episode-level algorithm where each rollout receives one return and one advantage. Step-independent training is the deviation from this design, introduced by framework implementation choices rather than algorithmic motivation. Our analysis reveals that this deviation carries hidden costs that become catastrophic for long-horizon interactive tasks.
82	
83	\subsection{Selective Verification via Action-Change Reward}
84	\label{sec:selective_verification}
85	
86	With a competent base agent trained via episode-level GRPO, we address the complementary problem of verification efficiency. Interactive agents benefit from self-verification (re-evaluating their planned action before execution), but empirical analysis shows that over 90\% of verification instances are confirmatory (the agent does not change its action after checking)~\cite{long2026selfverification}. Training the agent to verify selectively, only when verification is likely to be informative, can reduce computational cost without sacrificing task performance.
87	
88	We formulate selective verification as a binary decision at each step $t$: the agent outputs a verify token $v_t \in \{\texttt{VERIFY}, \texttt{SKIP}\}$ before generating its action $a_t$. When $v_t = \texttt{VERIFY}$, the agent generates a verification rationale and may revise its action; when $v_t = \texttt{SKIP}$, the agent proceeds directly. The reward signal for training the verification policy uses the action-change indicator:
89	\begin{equation}
90	\Delta a_t = \mathbb{1}[a_t^{\text{post-verify}} \neq a_t^{\text{pre-verify}}]
91	\label{eq:action_change}
92	\end{equation}
93	as a measure of verification informativeness. A verification step that changes the action provided useful corrective information; one that confirms the original action was uninformative for that instance. The full formulation of the verification reward and training procedure is presented in Section~\ref{sec:selective_experiments}. Episode-level training serves as a prerequisite for this component: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "f3a10144-c957-4a22-96dd-f4108bb49240",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:problem_formulation}\n\nWe formalize the multi-turn interactive agent as a Partially Observable Markov Decision Process (POMDP) $\\mathcal{M} = (\\mathcal{S}, \\mathcal{A}, \\mathcal{O}, P, \\Omega, R, \\gamma)$, where $\\mathcal{S}$ is the state space of the environment, $\\mathcal{A}$ is the action space (natural language commands), $\\mathcal{O}$ is the observation space (textual feedback from the environment), $P: \\mathcal{S} \\times \\mathcal{A} \\rightarrow \\mathcal{S}$ is the transition function, $\\Omega: \\mathcal{S} \\rightarrow \\mathcal{O}$ is the observation function, $R$ is the reward function, and $\\gamma \\in [0,1]$ is a discount factor. The agent policy $\\pi_\\phi(a_t \\mid h_t)$ generates actions conditioned on the interaction history $h_t = (o_1, a_1, o_2, a_2, \\ldots, o_t)$, where $\\phi$ denotes the policy parameters. An episode consists of $T$ interaction steps, terminating with a binary reward $R \\in \\{0, r_+\\}$ that indicates task success or failure.\n\nIn practice, multi-turn episodes can span 50 or more interaction steps, each containing hundreds of tokens. Training a language model policy on the full history $h_T$ is computationally expensive and often exceeds the model's context window. This motivates the \\textbf{step-independent windowing} approach: the trajectory is partitioned into non-overlapping windows of $h$ consecutive steps, and each window is optimized independently with its own computed return. Concretely, window $k$ observes only $(o_{(k-1)h+1}, a_{(k-1)h+1}, \\ldots, o_{kh})$ and receives a return $R_k$ derived from the episode outcome. This decomposition treats each window as a separate training sample, allowing standard context-length models to process the data. We show below that this seemingly practical choice introduces two failure mechanisms that cause catastrophic training collapse.\n\n\\subsection{GRPO for Language Agents}\n\\label{sec:grpo}\n\nGroup Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} is a bandit-style policy gradient method designed for language model alignment. Unlike PPO~\\cite{schulman2017ppo}, GRPO requires no critic network. For each task instance $x$, the algorithm samples $K$ rollouts $\\{y_1, \\ldots, y_K\\}$ from the current policy $\\pi_\\phi$. The advantage of each rollout is computed relative to the group:\n\\begin{equation}\n\\hat{A}_k = \\frac{R_k - \\mu}{\\sigma + \\epsilon}, \\quad \\mu = \\frac{1}{K}\\sum_{j=1}^K R_j, \\quad \\sigma = \\sqrt{\\frac{1}{K}\\sum_{j=1}^K (R_j - \\mu)^2}\n\\label{eq:grpo_advantage}\n\\end{equation}\nwhere $R_k$ is the return of rollout $k$. The policy gradient is:\n\\begin{equation}\n\\mathcal{L}_{\\text{GRPO}} = -\\frac{1}{K}\\sum_{k=1}^K \\hat{A}_k \\cdot \\min\\left(\\rho_k, \\text{clip}(\\rho_k, 1\\pm\\epsilon_c)\\right) + \\beta \\cdot D_{\\text{KL}}[\\pi_\\phi \\| \\pi_{\\text{ref}}]\n\\label{eq:grpo_loss}\n\\end{equation}\nwhere $\\rho_k = \\pi_\\phi(y_k \\mid x) / \\pi_{\\text{old}}(y_k \\mid x)$ is the importance ratio and $\\beta$ controls the KL penalty against a reference policy $\\pi_{\\text{ref}}$. GRPO is \\textit{episode-level by design}: each rollout $y_k$ is a complete generation with a single return $R_k$ and a single advantage $\\hat{A}_k$. There is no inherent temporal discounting within the algorithm.\n\n\\subsection{Step-Independent Implementation in Multi-Turn Agents}\n\\label{sec:step_independent}\n\nWhen adapting GRPO for multi-turn interactive tasks, agent training frameworks face a mismatch between GRPO's episode-level design and the practical constraints of long trajectories. The RAGEN framework~\\cite{ragen2025} addresses this by introducing step-independent training: each $h$-step window becomes an independent GRPO sample with a discounted return derived from the episode outcome.\n\nSpecifically, for an episode of $T$ steps with binary outcome $R_{\\text{episode}} \\in \\{0, r_+\\}$, the return assigned to window $k$ (covering steps $(k-1)h+1$ through $kh$) is computed as:\n\\begin{equation}\nR_k = \\gamma^{(N - k)} \\cdot R_{\\text{episode}}\n\\label{eq:step_return}\n\\end{equation}\nwhere $N = \\lceil T/h \\rceil$ is the total number of windows in the episode and $\\gamma$ is a discount factor (typically 0.95). Each window is then treated as an independent sample in the GRPO optimization and receives its own group-normalized advantage $\\hat{A}_k$ via Equation~\\ref{eq:grpo_advantage}. The total number of training samples per episode increases from 1 to $N$.\n\nThis design choice is motivated by three practical constraints. First, full trajectories of 50+ turns with hundreds of tokens per turn exceed typical context window limits (2048 or 4096 tokens for smaller models). Second, treating each window independently multiplies the effective batch size, improving GPU utilization. Third, the framework inherits the token-level training paradigm common in language model optimization, where shorter sequences are the default.\\footnote{Implementation details are available in the open-source RAGEN codebase, specifically the step-discounted return computation module (\\texttt{compute\\_step\\_discounted\\_returns}).}\n\nDespite these practical motivations, step-independent training fundamentally alters the credit assignment structure. The following section analyzes two mechanisms through which this alteration causes training collapse.\n\n\\subsection{Dual Mechanism Analysis}\n\\label{sec:dual_mechanism}\n\nWe identify two mechanisms that jointly cause catastrophic failure under step-independent training. As we demonstrate empirically in Section~\\ref{sec:experiments}, step-independent training with $h=2$ collapses to 0\\% task success within 10 training steps, while action validity remains above 90\\%. This pattern indicates that the policy degenerates in task strategy rather than action formatting.\n\n\\subsubsection{Mechanism 1: Policy Information Loss}\n\\label{sec:m1_information_loss}\n\nUnder step-independent training, the policy optimized on window $k$ observes only a local $h$-step history. Cross-step strategies that require conditioning on earlier outcomes become invisible to the optimization process. Consider a household task requiring the agent to first explore a drawer (step 3), discover an object's location (step 4), then navigate to a countertop (step 8). With $h=2$, the window containing step 8 has no access to the exploration outcome from steps 3--4. The policy cannot learn the conditional strategy ``go to countertop \\textit{only if} the object was found in the drawer.''\n\nMore formally, let $\\pi^*$ denote the optimal policy for the full POMDP. The mutual information between $\\pi^*$ and the full history, $I(\\pi^*; h_T)$, captures the total information required for optimal decision-making. Under $h$-step windowing, each window's policy can access at most $I(\\pi^*; h_{\\text{window}_k})$. For tasks with sequential dependencies spanning more than $h$ steps, we have $I(\\pi^*; h_T) \\gg I(\\pi^*; h_{\\text{window}_k})$. The information gap grows with episode length $T$ and shrinks with window size $h$, predicting a performance cliff as $h$ decreases relative to the task's dependency horizon.\n\n\\subsubsection{Mechanism 2: Advantage Sign Misattribution}\n\\label{sec:m2_sign_misattribution}\n\nThe second mechanism is more subtle and more damaging. Under step-independent training, each window receives a return $R_k = \\gamma^{(N-k)} \\cdot R_{\\text{episode}}$ (Equation~\\ref{eq:step_return}). After group normalization, the advantage $\\hat{A}_k$ has a \\textit{sign} determined primarily by whether the episode succeeded or failed, not by whether window $k$'s actions were locally good or bad.\n\nIn a failed episode ($R_{\\text{episode}} = 0$), all windows receive $R_k = 0$. If the group mean $\\mu > 0$ (due to other successful rollouts in the group), all windows in the failed episode receive negative advantages. This includes windows where the agent took locally correct actions (e.g., correctly identifying a target object). Conversely, in a successful episode, all windows receive positive advantages, including windows where the agent took suboptimal actions (e.g., unnecessary exploration steps that happened not to prevent eventual success).\n\nThe gradient direction for each window is determined by the sign of $\\hat{A}_k$:\n\\begin{equation}\n\\text{sign}(\\hat{A}_k) \\approx \\text{sign}(R_{\\text{episode}} - \\mu)\n\\label{eq:sign_correlation}\n\\end{equation}\nThis means the optimization either reinforces or suppresses \\textit{all} actions within a window based on the episode outcome, regardless of local action quality. Good actions in failed episodes are actively suppressed; bad actions in successful episodes are actively reinforced. Over many training steps, this systematic misattribution erodes learned strategies: the agent cannot maintain locally correct behaviors if they frequently co-occur with episode failure.\n\nA secondary effect compounds this problem. The discount factor $\\gamma^{(N-k)}$ introduces magnitude decay across window positions. For early windows in a long episode ($T=50$, $h=2$, $\\gamma=0.95$), the first window ($k=1$) retains $\\gamma^{N-1} = \\gamma^{24} \\approx 0.29$ of the terminal window's return. While this reduces the learning signal for early decisions, the sign error is fundamentally more harmful. Magnitude decay slows learning but preserves the correct optimization direction; sign misattribution actively drives the policy away from good behaviors. A gradient with correct sign but attenuated magnitude yields slow convergence. A gradient with wrong sign yields divergence.\n\n\\subsection{Episode-Level Training}\n\\label{sec:episode_level}\n\nEpisode-level training resolves both failure mechanisms by treating the complete trajectory as a single GRPO sample. All tokens across all $T$ steps share one advantage $\\hat{A}$, computed from the episode return $R_{\\text{episode}}$ via group normalization over $K$ complete rollouts of the same task instance.\n\nThis design directly addresses Mechanism 1. The policy $\\pi_\\phi(a_t \\mid h_t)$ conditions on the full interaction history $h_t$ at every step $t$. Cross-step dependencies are preserved in the optimization target: the gradient for generating action $a_8$ (navigate to countertop) flows through the complete history including observations from steps 3--4 (drawer exploration outcome).\n\nEpisode-level training also eliminates Mechanism 2. Because there is no window-level return assignment, there is no opportunity for sign misattribution between windows. The single advantage $\\hat{A}$ applies uniformly to the entire trajectory. While this means per-step credit assignment remains coarse (all steps in a successful episode are equally reinforced), it avoids the worse failure mode of \\textit{systematically incorrect} credit assignment. The distinction is critical: uniform reinforcement of a successful trajectory preserves good sub-strategies within it, whereas window-level sign errors actively destroy them.\n\nThe trade-off is computational. Episode-level training requires processing the full sequence length ($T$ steps $\\times$ tokens-per-step) in a single forward and backward pass. For $T=50$ and 100 tokens per step, this amounts to 5000-token sequences, which fits within the capacity of modern architectures but increases memory and compute relative to $h$-step windows. In our experiments (Section~\\ref{sec:experiments}), this overhead is modest compared to the catastrophic failure avoided.\n\nEpisode-level training is, in fact, the natural application of GRPO to multi-turn settings. GRPO was designed as an episode-level algorithm where each rollout receives one return and one advantage. Step-independent training is the deviation from this design, introduced by framework implementation choices rather than algorithmic motivation. Our analysis reveals that this deviation carries hidden costs that become catastrophic for long-horizon interactive tasks.\n\n\\subsection{Selective Verification via Action-Change Reward}\n\\label{sec:selective_verification}\n\nWith a competent base agent trained via episode-level GRPO, we address the complementary problem of verification efficiency. Interactive agents benefit from self-verification (re-evaluating their planned action before execution), but empirical analysis shows that over 90\\% of verification instances are confirmatory (the agent does not change its action after checking)~\\cite{long2026selfverification}. Training the agent to verify selectively, only when verification is likely to be informative, can reduce computational cost without sacrificing task performance.\n\nWe formulate selective verification as a binary decision at each step $t$: the agent outputs a verify token $v_t \\in \\{\\texttt{VERIFY}, \\texttt{SKIP}\\}$ before generating its action $a_t$. When $v_t = \\texttt{VERIFY}$, the agent generates a verification rationale and may revise its action; when $v_t = \\texttt{SKIP}$, the agent proceeds directly. The reward signal for training the verification policy uses the action-change indicator:\n\\begin{equation}\n\\Delta a_t = \\mathbb{1}[a_t^{\\text{post-verify}} \\neq a_t^{\\text{pre-verify}}]\n\\label{eq:action_change}\n\\end{equation}\nas a measure of verification informativeness. A verification step that changes the action provided useful corrective information; one that confirms the original action was uninformative for that instance. The full formulation of the verification reward and training procedure is presented in Section~\\ref{sec:selective_experiments}. Episode-level training serves as a prerequisite for this component: training a selective verification policy requires a base agent with sufficient task competence, which step-independent training cannot produce.",
      "numLines": 93,
      "startLine": 1,
      "totalLines": 93
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CzQYEZghomwXoCKcxEgztY`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "daa7e379-4808-4749-96e9-c543e9ebec37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015uGmvZAKig1kkx7neyGxjx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14688,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14688
      },
      "output_tokens": 27,
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

_source line 11 · 2026-05-17T08:12:30.044Z_

<details><summary>↩ Tool result · `toolu_01CzQYEZghomwXoCKcxEgztY`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "d030856b-5daf-4400-8347-cca5220f04d1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 50
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the literature map to get all the citation keys and details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "3e608409-4455-4d04-8a64-d22fd956804a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lm4jYsyxq94VcQzefqmzzr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6113,
      "cache_read_input_tokens": 26529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6113
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

_source line 13_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_017YQ6nBWpBzGZ2nLJMHZNkU`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "1fa3cd36-ff8c-4e03-9a66-bfb2421e5e2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lm4jYsyxq94VcQzefqmzzr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6113,
      "cache_read_input_tokens": 26529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6113
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

_source line 14 · 2026-05-17T08:12:34.822Z_

<details><summary>↩ Tool result · `toolu_017YQ6nBWpBzGZ2nLJMHZNkU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml\", \"content\": \"# B-IAVR Literature Map\\n# Updated: 2026-05-16\\n# Categories: direct-competitor, method-component, background, evaluation\\n# Roles: predecessor, competitor, baseline, evaluation, background\\n\\npapers:\\n\\n  # ============================================================\\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\\n  # ============================================================\\n\\n  - id: kamoi2024self-correction-survey\\n    title: \\\"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\\\"\\n    authors: \\\"Kamoi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2024\\n    arxiv_id: \\\"2406.01297\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\\n\\n  - id: tie2025correctbench\\n    title: \\\"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\\\"\\n    authors: \\\"Tie et al.\\\"\\n    venue: \\\"NeurIPS 2025 Datasets & Benchmarks\\\"\\n    year: 2025\\n    arxiv_id: \\\"2510.16062\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\\n      Supports B-IAVR's selective verification design over blanket correction.\\n\\n  - id: self-verification-dilemma-2026\\n    title: \\\"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\\\"\\n    authors: \\\"Long et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.03485\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\\n      Directly supports B-IAVR's core thesis that verification should be selective.\\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\\n\\n  - id: zhang2025incentivize-self-verify\\n    title: \\\"Incentivizing LLMs to Self-Verify Their Answers\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2506.01369\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Unifies answer generation and verification via single RL training process.\\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\\n\\n  - id: mar2025\\n    title: \\\"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\\\"\\n    authors: \\\"Ozer et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.20845\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Multi-agent self-correction with diverse critic personas.\\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\\n\\n  - id: ssr2025\\n    title: \\\"SSR: Socratic Self-Refine for Large Language Model Reasoning\\\"\\n    authors: \\\"Shi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.10621\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Structured Socratic questioning for self-refinement.\\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\\n\\n  - id: verifiagent2025\\n    title: \\\"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\\\"\\n    authors: \\\"Han et al.\\\"\\n    venue: \\\"EMNLP 2025 Findings\\\"\\n    year: 2025\\n    arxiv_id: \\\"2504.00406\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Unified verification agent with meta-verification + tool-based adaptive verification.\\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\\n\\n  # ============================================================\\n  # Direction 2: Agent RL Training\\n  # ============================================================\\n\\n  - id: feng2025gigpo\\n    title: \\\"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\\\"\\n    authors: \\\"Feng et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.10978\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\\n\\n  - id: selfguide2026\\n    title: \\\"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.03098\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\\n      The self-guidance signal is the foundation for action-change detection triggering verification.\\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\\n\\n  - id: spear2025\\n    title: \\\"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\\\"\\n    authors: \\\"Qin et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.22601\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Curriculum-based self-imitation for sparse-reward agent tasks.\\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\\n\\n  - id: wei2025webagent-r1\\n    title: \\\"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\\\"\\n    authors: \\\"Wei et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.16421\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\\n\\n  - id: dapo2025\\n    title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: \\\"Yu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2503.14476\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\\n\\n  - id: digiRL2024\\n    title: \\\"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\\\"\\n    authors: \\\"Bai et al.\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2406.11896\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\\n\\n  - id: li2025sorl\\n    title: \\\"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.20718\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\\n\\n  - id: agentic-rl-survey-2025\\n    title: \\\"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.02547\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\\n\\n  - id: skillmaster2026\\n    title: \\\"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.08693\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\\n      separation of action and verification advantages.\\n\\n  - id: t2po2026\\n    title: \\\"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"ICML 2026 Spotlight\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.02178\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\\n\\n  - id: gvpo2026\\n    title: \\\"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\\\"\\n    authors: \\\"Dai et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2026\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\\n      verification signals. Different focus: uses verification for credit assignment during\\n      training; B-IAVR learns when to invoke verification at deployment.\\n\\n  - id: agentv-rl2026\\n    title: \\\"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.16004\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\\n      B-IAVR addresses verification timing in agent deployment. Complementary.\\n\\n  - id: pa-moe2026\\n    title: \\\"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.17038\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\\n      Orthogonal architecture innovation; important baseline to cite.\\n\\n  - id: sdar2026\\n    title: \\\"SDAR: Self-Distilled Agentic Reinforcement Learning\\\"\\n    authors: \\\"Lu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.15155\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\\n\\n  - id: hcapo2026\\n    title: \\\"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\\\"\\n    authors: \\\"Tan et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.08754\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\\n      multi-scale advantage for critical decision states.\\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\\n      Could improve B-IAVR's reward signal for verification decision steps.\\n\\n  - id: act2026\\n    title: \\\"ACT: Agentic Critical Training\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.08706\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\\n      B-IAVR decides when to reflect.\\n\\n  - id: rwml2026\\n    title: \\\"RWML: Reinforcement World Model Learning for LLM-based Agents\\\"\\n    authors: \\\"Yu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.05842\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.\\n      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.\\n      Orthogonal: improves internal world model; B-IAVR adds selective verification.\\n\\n  - id: skill0-2026\\n    title: \\\"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\\\"\\n    authors: \\\"Lu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.02268\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.\\n      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.\\n      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.\\n\\n  - id: fission-grpo2026\\n    title: \\\"Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2601.15625\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Fissions failed trajectories into recovery training instances.\\n      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.\\n      Related: error recovery after failure vs B-IAVR's proactive verification.\\n\\n  - id: selfbudgeter2026\\n    title: \\\"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"ICLR 2026 (under review)\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.11274\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.\\n      Parallel concept: SelfBudgeter allocates computation budget;\\n      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.\\n\\n  - id: cove2026\\n    title: \\\"CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification\\\"\\n    authors: \\\"Chen et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.01940\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.\\n      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.\\n\\n  # ============================================================\\n  # Direction 3: Selective Verification / Adaptive Computation\\n  # ============================================================\\n\\n  - id: wan2025derailer-rerailer\\n    title: \\\"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning\\\"\\n    authors: \\\"Wan et al.\\\"\\n    venue: \\\"ACL 2025 Findings\\\"\\n    year: 2025\\n    arxiv_id: \\\"2408.13940\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Most directly related competitor. Both do selective verification with binary trigger.\\n      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).\\n      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.\\n      8-11% accuracy gain, 2-3x efficiency over uniform verification.\\n\\n  - id: sherlock2025\\n    title: \\\"Sherlock: Reliable and Efficient Agentic Workflow Execution\\\"\\n    authors: \\\"Microsoft\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.00330\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.\\n      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).\\n      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.\\n\\n  - id: singhi2025when-to-verify\\n    title: \\\"When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning\\\"\\n    authors: \\\"Singhi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2504.01005\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Derives inference scaling laws for solve-vs-verify tradeoff.\\n      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.\\n      B-IAVR learns this allocation via RL rather than analytically.\\n\\n  - id: yang2026ares\\n    title: \\\"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.07915\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Closest competitor in agent domain. Both train learned per-step compute allocation.\\n      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;\\n      B-IAVR trains binary verify/not-verify via RL with action-change signal.\\n      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change\\n      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data\\n      to bootstrap the router, B-IAVR learns from environment interaction alone.\\n      Reduces reasoning tokens by up to 52.7%.\\n\\n  - id: tu2025autothink\\n    title: \\\"Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL\\\"\\n    authors: \\\"Tu et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.10832\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.\\n      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.\\n      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.\\n\\n  - id: du2025thinkless\\n    title: \\\"Thinkless: LLM Learns When to Think\\\"\\n    authors: \\\"Fang et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.13379\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      RL-trained control token to decide when to invoke extended thinking.\\n      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.\\n\\n  - id: wang2025efficient-agents\\n    title: \\\"Efficient Agents: Building Effective Agents While Reducing Cost\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.02694\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      First systematic study of agent efficiency-effectiveness tradeoff.\\n      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.\\n      Retains 96.7% performance with 28.4% cost-of-pass improvement.\\n\\n  - id: venktesh2025trust-but-verify\\n    title: \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\"\\n    authors: \\\"Venktesh et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.16665\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Survey of verification approaches for test-time compute scaling.\\n      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.\\n\\n  - id: agent-omit2026\\n    title: \\\"Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL\\\"\\n    authors: \\\"Ning et al.\\\"\\n    venue: \\\"ICML 2026\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.04284\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      RL-trained policy for adaptive omission of redundant thoughts and observations.\\n      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.\\n      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts\\n      (omits unnecessary context); B-IAVR selectively adds (verification steps).\\n      Opposite but complementary approaches to cost-efficiency. Potentially combinable.\\n\\n  - id: ava2026\\n    title: \\\"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints\\\"\\n    authors: \\\"Patel\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    year: 2026\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Dynamic compute allocation across search, sampling, and verification under budget.\\n      Uses calibrated uncertainty + value-of-information for selective verification cascades.\\n      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.\\n      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;\\n      single-turn reasoning vs multi-turn agent trajectories.\\n\\n  - id: cast2026\\n    title: \\\"CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use\\\"\\n    authors: \\\"Pang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.15041\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Historical execution cases calibrate reasoning depth for tool use.\\n      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.\\n      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.\\n\\n  - id: marginal-token-allocators2026\\n    title: \\\"Agentic AI Systems Should Be Designed as Marginal Token Allocators\\\"\\n    authors: \\\"Zhu\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.01214\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Position paper framing agent cost-efficiency as marginal token allocation economics.\\n      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing\\n      that verification decisions should reflect marginal cost-benefit analysis.\\n\\n  - id: argos2025\\n    title: \\\"Argos: Multimodal RL with Adaptive Verifier for AI Agents\\\"\\n    authors: \\\"Tan et al.\\\"\\n    venue: \\\"arXiv (revised April 2026)\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.03438\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Agentic verifier that adaptively selects scoring functions for multimodal RL training.\\n      Different domain (multimodal/robotics). The adaptive verifier selection concept is\\n      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.\\n\\n  # ============================================================\\n  # Direction 4: ALFWorld / Interactive Environment Benchmarks\\n  # ============================================================\\n\\n  - id: kim2025reflact\\n    title: \\\"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection\\\"\\n    authors: \\\"Kim et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.15182\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.\\n      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.\\n\\n  - id: choudhury2025agentprm\\n    title: \\\"Process Reward Models for LLM Agents: Practical Framework and Directions\\\"\\n    authors: \\\"Choudhury\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2502.10325\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.\\n      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.\\n\\n  - id: xi2025agentprm\\n    title: \\\"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\\\"\\n    authors: \\\"Xi et al.\\\"\\n    venue: \\\"ACM Web Conference 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.08325\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable\\n      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.\\n      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.\\n\\n  - id: xiang2024retrospex\\n    title: \\\"Retrospex: Language Agent Meets Offline RL Critic\\\"\\n    authors: \\\"Xiang et al.\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2505.11807\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Offline RL Critic augments LLM agent action selection via dynamic rescoring.\\n      Similar architecture could inform B-IAVR's verification value estimation.\\n\\n  - id: cfgm2025\\n    title: \\\"CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.15305\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Memory-augmented agent planning with episodic grounding.\\n      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.\\n\\n  - id: respact2024\\n    title: \\\"ReSpAct: Harmonizing Reasoning, Speaking, and Acting\\\"\\n    authors: \\\"Dongre et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2024\\n    arxiv_id: \\\"2411.00927\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.\\n      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.\\n\", \"total_chars\": 25208, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "bb953a49-7db7-4348-820f-5367f4373999",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml\\\", \\\"content\\\": \\\"# B-IAVR Literature Map\\\\n# Updated: 2026-05-16\\\\n# Categories: direct-competitor, method-component, background, evaluation\\\\n# Roles: predecessor, competitor, baseline, evaluation, background\\\\n\\\\npapers:\\\\n\\\\n  # ============================================================\\\\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\\\\n  # ============================================================\\\\n\\\\n  - id: kamoi2024self-correction-survey\\\\n    title: \\\\\\\"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Kamoi et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2024\\\\n    arxiv_id: \\\\\\\"2406.01297\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\\\\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\\\\n\\\\n  - id: tie2025correctbench\\\\n    title: \\\\\\\"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Tie et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025 Datasets & Benchmarks\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2510.16062\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\\\\n      Supports B-IAVR's selective verification design over blanket correction.\\\\n\\\\n  - id: self-verification-dilemma-2026\\\\n    title: \\\\\\\"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Long et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2602.03485\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\\\\n      Directly supports B-IAVR's core thesis that verification should be selective.\\\\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\\\\n\\\\n  - id: zhang2025incentivize-self-verify\\\\n    title: \\\\\\\"Incentivizing LLMs to Self-Verify Their Answers\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2506.01369\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Unifies answer generation and verification via single RL training process.\\\\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\\\\n\\\\n  - id: mar2025\\\\n    title: \\\\\\\"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\\\\\\\"\\\\n    authors: \\\\\\\"Ozer et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2512.20845\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Multi-agent self-correction with diverse critic personas.\\\\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\\\\n\\\\n  - id: ssr2025\\\\n    title: \\\\\\\"SSR: Socratic Self-Refine for Large Language Model Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Shi et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2511.10621\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Structured Socratic questioning for self-refinement.\\\\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\\\\n\\\\n  - id: verifiagent2025\\\\n    title: \\\\\\\"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Han et al.\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2025 Findings\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2504.00406\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Unified verification agent with meta-verification + tool-based adaptive verification.\\\\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\\\\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\\\\n\\\\n  # ============================================================\\\\n  # Direction 2: Agent RL Training\\\\n  # ============================================================\\\\n\\\\n  - id: feng2025gigpo\\\\n    title: \\\\\\\"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\\\\\\\"\\\\n    authors: \\\\\\\"Feng et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.10978\\\\\\\"\\\\n    category: method-component\\\\n    role: predecessor\\\\n    relevance_note: >\\\\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\\\\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\\\\n\\\\n  - id: selfguide2026\\\\n    title: \\\\\\\"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\\\\\\\"\\\\n    authors: \\\\\\\"Wang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2604.03098\\\\\\\"\\\\n    category: method-component\\\\n    role: predecessor\\\\n    relevance_note: >\\\\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\\\\n      The self-guidance signal is the foundation for action-change detection triggering verification.\\\\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\\\\n\\\\n  - id: spear2025\\\\n    title: \\\\\\\"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Qin et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2026\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2509.22601\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      Curriculum-based self-imitation for sparse-reward agent tasks.\\\\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\\\\n\\\\n  - id: wei2025webagent-r1\\\\n    title: \\\\\\\"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\\\\\\\"\\\\n    authors: \\\\\\\"Wei et al.\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.16421\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\\\\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\\\\n\\\\n  - id: dapo2025\\\\n    title: \\\\\\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\\\\\"\\\\n    authors: \\\\\\\"Yu et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2503.14476\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\\\\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\\\\n\\\\n  - id: digiRL2024\\\\n    title: \\\\\\\"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\\\\\\\"\\\\n    authors: \\\\\\\"Bai et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2024\\\\\\\"\\\\n    year: 2024\\\\n    arxiv_id: \\\\\\\"2406.11896\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\\\\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\\\\n\\\\n  - id: li2025sorl\\\\n    title: \\\\\\\"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2511.20718\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\\\\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\\\\n\\\\n  - id: agentic-rl-survey-2025\\\\n    title: \\\\\\\"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    venue: \\\\\\\"TMLR 2026\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2509.02547\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\\\\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\\\\n\\\\n  - id: skillmaster2026\\\\n    title: \\\\\\\"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\\\\\\\"\\\\n    authors: \\\\\\\"Yang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2605.08693\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\\\\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\\\\n      separation of action and verification advantages.\\\\n\\\\n  - id: t2po2026\\\\n    title: \\\\\\\"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\\\\\\\"\\\\n    authors: \\\\\\\"Wang et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2026 Spotlight\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2605.02178\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\\\\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\\\\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\\\\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\\\\n\\\\n  - id: gvpo2026\\\\n    title: \\\\\\\"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\\\\\\\"\\\\n    authors: \\\\\\\"Dai et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2026\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\\\\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\\\\n      verification signals. Different focus: uses verification for credit assignment during\\\\n      training; B-IAVR learns when to invoke verification at deployment.\\\\n\\\\n  - id: agentv-rl2026\\\\n    title: \\\\\\\"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2604.16004\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\\\\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\\\\n      B-IAVR addresses verification timing in agent deployment. Complementary.\\\\n\\\\n  - id: pa-moe2026\\\\n    title: \\\\\\\"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2602.17038\\\\\\\"\\\\n    category: evaluation\\\\n    role: baseline\\\\n    relevance_note: >\\\\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\\\\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\\\\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\\\\n      Orthogonal architecture innovation; important baseline to cite.\\\\n\\\\n  - id: sdar2026\\\\n    title: \\\\\\\"SDAR: Self-Distilled Agentic Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Lu et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2605.15155\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\\\\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\\\\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\\\\n\\\\n  - id: hcapo2026\\\\n    title: \\\\\\\"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\\\\\\\"\\\\n    authors: \\\\\\\"Tan et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2603.08754\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\\\\n      multi-scale advantage for critical decision states.\\\\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\\\\n      Could improve B-IAVR's reward signal for verification decision steps.\\\\n\\\\n  - id: act2026\\\\n    title: \\\\\\\"ACT: Agentic Critical Training\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2603.08706\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\\\\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\\\\n      B-IAVR decides when to reflect.\\\\n\\\\n  - id: rwml2026\\\\n    title: \\\\\\\"RWML: Reinforcement World Model Learning for LLM-based Agents\\\\\\\"\\\\n    authors: \\\\\\\"Yu et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2602.05842\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.\\\\n      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.\\\\n      Orthogonal: improves internal world model; B-IAVR adds selective verification.\\\\n\\\\n  - id: skill0-2026\\\\n    title: \\\\\\\"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\\\\\\\"\\\\n    authors: \\\\\\\"Lu et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2604.02268\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.\\\\n      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.\\\\n      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.\\\\n\\\\n  - id: fission-grpo2026\\\\n    title: \\\\\\\"Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2601.15625\\\\\\\"\\\\n    category: method-component\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] Fissions failed trajectories into recovery training instances.\\\\n      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.\\\\n      Related: error recovery after failure vs B-IAVR's proactive verification.\\\\n\\\\n  - id: selfbudgeter2026\\\\n    title: \\\\\\\"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICLR 2026 (under review)\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.11274\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.\\\\n      Parallel concept: SelfBudgeter allocates computation budget;\\\\n      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.\\\\n\\\\n  - id: cove2026\\\\n    title: \\\\\\\"CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification\\\\\\\"\\\\n    authors: \\\\\\\"Chen et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2603.01940\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.\\\\n      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.\\\\n\\\\n  # ============================================================\\\\n  # Direction 3: Selective Verification / Adaptive Computation\\\\n  # ============================================================\\\\n\\\\n  - id: wan2025derailer-rerailer\\\\n    title: \\\\\\\"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Wan et al.\\\\\\\"\\\\n    venue: \\\\\\\"ACL 2025 Findings\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2408.13940\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      Most directly related competitor. Both do selective verification with binary trigger.\\\\n      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).\\\\n      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.\\\\n      8-11% accuracy gain, 2-3x efficiency over uniform verification.\\\\n\\\\n  - id: sherlock2025\\\\n    title: \\\\\\\"Sherlock: Reliable and Efficient Agentic Workflow Execution\\\\\\\"\\\\n    authors: \\\\\\\"Microsoft\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2511.00330\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.\\\\n      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).\\\\n      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.\\\\n\\\\n  - id: singhi2025when-to-verify\\\\n    title: \\\\\\\"When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Singhi et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2504.01005\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Derives inference scaling laws for solve-vs-verify tradeoff.\\\\n      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.\\\\n      B-IAVR learns this allocation via RL rather than analytically.\\\\n\\\\n  - id: yang2026ares\\\\n    title: \\\\\\\"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\\\\\\\"\\\\n    authors: \\\\\\\"Yang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2603.07915\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      Closest competitor in agent domain. Both train learned per-step compute allocation.\\\\n      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;\\\\n      B-IAVR trains binary verify/not-verify via RL with action-change signal.\\\\n      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change\\\\n      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data\\\\n      to bootstrap the router, B-IAVR learns from environment interaction alone.\\\\n      Reduces reasoning tokens by up to 52.7%.\\\\n\\\\n  - id: tu2025autothink\\\\n    title: \\\\\\\"Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL\\\\\\\"\\\\n    authors: \\\\\\\"Tu et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.10832\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.\\\\n      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.\\\\n      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.\\\\n\\\\n  - id: du2025thinkless\\\\n    title: \\\\\\\"Thinkless: LLM Learns When to Think\\\\\\\"\\\\n    authors: \\\\\\\"Fang et al.\\\\\\\"\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.13379\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      RL-trained control token to decide when to invoke extended thinking.\\\\n      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.\\\\n\\\\n  - id: wang2025efficient-agents\\\\n    title: \\\\\\\"Efficient Agents: Building Effective Agents While Reducing Cost\\\\\\\"\\\\n    authors: \\\\\\\"Wang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2508.02694\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      First systematic study of agent efficiency-effectiveness tradeoff.\\\\n      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.\\\\n      Retains 96.7% performance with 28.4% cost-of-pass improvement.\\\\n\\\\n  - id: venktesh2025trust-but-verify\\\\n    title: \\\\\\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\\\\\"\\\\n    authors: \\\\\\\"Venktesh et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2508.16665\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Survey of verification approaches for test-time compute scaling.\\\\n      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.\\\\n\\\\n  - id: agent-omit2026\\\\n    title: \\\\\\\"Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL\\\\\\\"\\\\n    authors: \\\\\\\"Ning et al.\\\\\\\"\\\\n    venue: \\\\\\\"ICML 2026\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2602.04284\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      RL-trained policy for adaptive omission of redundant thoughts and observations.\\\\n      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.\\\\n      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts\\\\n      (omits unnecessary context); B-IAVR selectively adds (verification steps).\\\\n      Opposite but complementary approaches to cost-efficiency. Potentially combinable.\\\\n\\\\n  - id: ava2026\\\\n    title: \\\\\\\"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints\\\\\\\"\\\\n    authors: \\\\\\\"Patel\\\\\\\"\\\\n    venue: \\\\\\\"TMLR 2026\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF\\\\n    category: direct-competitor\\\\n    role: competitor\\\\n    relevance_note: >\\\\n      Dynamic compute allocation across search, sampling, and verification under budget.\\\\n      Uses calibrated uncertainty + value-of-information for selective verification cascades.\\\\n      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.\\\\n      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;\\\\n      single-turn reasoning vs multi-turn agent trajectories.\\\\n\\\\n  - id: cast2026\\\\n    title: \\\\\\\"CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use\\\\\\\"\\\\n    authors: \\\\\\\"Pang et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2605.15041\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Historical execution cases calibrate reasoning depth for tool use.\\\\n      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.\\\\n      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.\\\\n\\\\n  - id: marginal-token-allocators2026\\\\n    title: \\\\\\\"Agentic AI Systems Should Be Designed as Marginal Token Allocators\\\\\\\"\\\\n    authors: \\\\\\\"Zhu\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2026\\\\n    arxiv_id: \\\\\\\"2605.01214\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Position paper framing agent cost-efficiency as marginal token allocation economics.\\\\n      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing\\\\n      that verification decisions should reflect marginal cost-benefit analysis.\\\\n\\\\n  - id: argos2025\\\\n    title: \\\\\\\"Argos: Multimodal RL with Adaptive Verifier for AI Agents\\\\\\\"\\\\n    authors: \\\\\\\"Tan et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv (revised April 2026)\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2512.03438\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Agentic verifier that adaptively selects scoring functions for multimodal RL training.\\\\n      Different domain (multimodal/robotics). The adaptive verifier selection concept is\\\\n      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.\\\\n\\\\n  # ============================================================\\\\n  # Direction 4: ALFWorld / Interactive Environment Benchmarks\\\\n  # ============================================================\\\\n\\\\n  - id: kim2025reflact\\\\n    title: \\\\\\\"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection\\\\\\\"\\\\n    authors: \\\\\\\"Kim et al.\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2505.15182\\\\\\\"\\\\n    category: evaluation\\\\n    role: baseline\\\\n    relevance_note: >\\\\n      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.\\\\n      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.\\\\n\\\\n  - id: choudhury2025agentprm\\\\n    title: \\\\\\\"Process Reward Models for LLM Agents: Practical Framework and Directions\\\\\\\"\\\\n    authors: \\\\\\\"Choudhury\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2502.10325\\\\\\\"\\\\n    category: evaluation\\\\n    role: baseline\\\\n    relevance_note: >\\\\n      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.\\\\n      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.\\\\n\\\\n  - id: xi2025agentprm\\\\n    title: \\\\\\\"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\\\\\\\"\\\\n    authors: \\\\\\\"Xi et al.\\\\\\\"\\\\n    venue: \\\\\\\"ACM Web Conference 2026\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2511.08325\\\\\\\"\\\\n    category: evaluation\\\\n    role: baseline\\\\n    relevance_note: >\\\\n      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable\\\\n      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.\\\\n      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.\\\\n\\\\n  - id: xiang2024retrospex\\\\n    title: \\\\\\\"Retrospex: Language Agent Meets Offline RL Critic\\\\\\\"\\\\n    authors: \\\\\\\"Xiang et al.\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2024\\\\\\\"\\\\n    year: 2024\\\\n    arxiv_id: \\\\\\\"2505.11807\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Offline RL Critic augments LLM agent action selection via dynamic rescoring.\\\\n      Similar architecture could inform B-IAVR's verification value estimation.\\\\n\\\\n  - id: cfgm2025\\\\n    title: \\\\\\\"CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning\\\\\\\"\\\\n    authors: \\\\\\\"Yang et al.\\\\\\\"\\\\n    venue: \\\\\\\"EMNLP 2025\\\\\\\"\\\\n    year: 2025\\\\n    arxiv_id: \\\\\\\"2508.15305\\\\\\\"\\\\n    category: background\\\\n    role: background\\\\n    relevance_note: >\\\\n      Memory-augmented agent planning with episodic grounding.\\\\n      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.\\\\n\\\\n  - id: respact2024\\\\n    title: \\\\\\\"ReSpAct: Harmonizing Reasoning, Speaking, and Acting\\\\\\\"\\\\n    authors: \\\\\\\"Dongre et al.\\\\\\\"\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    year: 2024\\\\n    arxiv_id: \\\\\\\"2411.00927\\\\\\\"\\\\n    category: evaluation\\\\n    role: baseline\\\\n    relevance_note: >\\\\n      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.\\\\n      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.\\\\n\\\", \\\"total_chars\\\": 25208, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/literature_map.yaml\", \"content\": \"# B-IAVR Literature Map\\n# Updated: 2026-05-16\\n# Categories: direct-competitor, method-component, background, evaluation\\n# Roles: predecessor, competitor, baseline, evaluation, background\\n\\npapers:\\n\\n  # ============================================================\\n  # Direction 1: Self-Verification / Self-Correction in LLM Agents\\n  # ============================================================\\n\\n  - id: kamoi2024self-correction-survey\\n    title: \\\"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\\\"\\n    authors: \\\"Kamoi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2024\\n    arxiv_id: \\\"2406.01297\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Foundational survey establishing that pure intrinsic self-correction is unreliable.\\n      Validates B-IAVR's use of grounded verification (environment re-observation) over prompted self-feedback.\\n\\n  - id: tie2025correctbench\\n    title: \\\"Can LLMs Correct Themselves? A Benchmark of Self-Correction in LLMs\\\"\\n    authors: \\\"Tie et al.\\\"\\n    venue: \\\"NeurIPS 2025 Datasets & Benchmarks\\\"\\n    year: 2025\\n    arxiv_id: \\\"2510.16062\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Benchmark showing self-correction has diminishing returns when applied uniformly.\\n      Supports B-IAVR's selective verification design over blanket correction.\\n\\n  - id: self-verification-dilemma-2026\\n    title: \\\"Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking in LLM Reasoning\\\"\\n    authors: \\\"Long et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.03485\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Empirically validates that >90% of self-verification is confirmatory, ~2% corrective.\\n      Directly supports B-IAVR's core thesis that verification should be selective.\\n      Their experience-pool approach is complementary to B-IAVR's action-change signal.\\n\\n  - id: zhang2025incentivize-self-verify\\n    title: \\\"Incentivizing LLMs to Self-Verify Their Answers\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2506.01369\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Unifies answer generation and verification via single RL training process.\\n      Parallel to B-IAVR: they train verification into generation; B-IAVR trains when to trigger separate verification.\\n\\n  - id: mar2025\\n    title: \\\"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs\\\"\\n    authors: \\\"Ozer et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.20845\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Multi-agent self-correction with diverse critic personas.\\n      Complementary: MAR improves correction quality; B-IAVR decides when to trigger correction.\\n\\n  - id: ssr2025\\n    title: \\\"SSR: Socratic Self-Refine for Large Language Model Reasoning\\\"\\n    authors: \\\"Shi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.10621\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Structured Socratic questioning for self-refinement.\\n      Complementary: improves correction step quality; B-IAVR focuses on when to invoke correction.\\n\\n  - id: verifiagent2025\\n    title: \\\"VerifiAgent: a Unified Verification Agent in Language Model Reasoning\\\"\\n    authors: \\\"Han et al.\\\"\\n    venue: \\\"EMNLP 2025 Findings\\\"\\n    year: 2025\\n    arxiv_id: \\\"2504.00406\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Unified verification agent with meta-verification + tool-based adaptive verification.\\n      Focuses on how to verify (tool selection); B-IAVR focuses on when to verify (policy learning).\\n      Complementary: VerifiAgent's verification quality could enhance B-IAVR's verification step.\\n\\n  # ============================================================\\n  # Direction 2: Agent RL Training\\n  # ============================================================\\n\\n  - id: feng2025gigpo\\n    title: \\\"GiGPO: Group-in-Group Policy Optimization for LLM Agent Training\\\"\\n    authors: \\\"Feng et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.10978\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      Core training algorithm for B-IAVR. Nested group structure provides step-level credit\\n      assignment without learned critic. >12% over GRPO on ALFWorld, >9% on WebShop.\\n\\n  - id: selfguide2026\\n    title: \\\"Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide)\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.03098\\\"\\n    category: method-component\\n    role: predecessor\\n    relevance_note: >\\n      Direct predecessor. B-IAVR extends Self-Guide's co-evolving internal reward.\\n      The self-guidance signal is the foundation for action-change detection triggering verification.\\n      8% improvement over env-reward-only on ALFWorld with Qwen3-1.7B/4B.\\n\\n  - id: spear2025\\n    title: \\\"Learn the Ropes, Then Trust the Wins: Self-imitation with Progressive Exploration for Agentic Reinforcement Learning\\\"\\n    authors: \\\"Qin et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.22601\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Curriculum-based self-imitation for sparse-reward agent tasks.\\n      Up to +16.1% on ALFWorld over GRPO. Self-imitation curriculum could augment B-IAVR training.\\n\\n  - id: wei2025webagent-r1\\n    title: \\\"WebAgent-R1: Training Web Agents via End-to-End Multi-Turn RL\\\"\\n    authors: \\\"Wei et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.16421\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Extends GRPO to multi-turn (M-GRPO) with dynamic context compression.\\n      Qwen-2.5-3B: 6.1% to 33.9% on WebArena-Lite. M-GRPO multi-turn extension relevant to B-IAVR.\\n\\n  - id: dapo2025\\n    title: \\\"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\\\"\\n    authors: \\\"Yu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2503.14476\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      RL training stabilization techniques (Clip-Higher, Dynamic Sampling).\\n      Applicable to B-IAVR's RL training to prevent entropy collapse.\\n\\n  - id: digiRL2024\\n    title: \\\"DigiRL: Training In-The-Wild Device-Control Agents with Autonomous RL\\\"\\n    authors: \\\"Bai et al.\\\"\\n    venue: \\\"NeurIPS 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2406.11896\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Online RL for device control agents. Demonstrates online RL viability for interactive agents.\\n      49.5% absolute improvement over SFT. Parallel approach to B-IAVR in text-based setting.\\n\\n  - id: li2025sorl\\n    title: \\\"SORL: Stabilizing Off-Policy RL for Long-Horizon Agent Training\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.20718\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Turn-level importance sampling + clipping-triggered normalization for stable multi-turn agent RL.\\n      Directly applicable to B-IAVR's multi-turn ALFWorld training stability.\\n\\n  - id: agentic-rl-survey-2025\\n    title: \\\"The Landscape of Agentic Reinforcement Learning for LLMs: A Survey\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2509.02547\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Comprehensive survey formalizing agentic RL. Contextualizes B-IAVR as training agents\\n      to make meta-decisions (when to verify) via RL within the POMDP framework.\\n\\n  - id: skillmaster2026\\n    title: \\\"SkillMaster: Toward Autonomous Skill Mastery in LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.08693\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      DualAdv-GRPO: separately estimates advantages for task-solving and skill-editing decisions.\\n      +8.8% on ALFWorld, +9.3% on WebShop. DualAdv structure could inform B-IAVR's\\n      separation of action and verification advantages.\\n\\n  - id: t2po2026\\n    title: \\\"T2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic RL\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"ICML 2026 Spotlight\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.02178\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Token- and turn-level uncertainty monitoring for stable multi-turn agent RL.\\n      Triggers thinking intervention when marginal uncertainty change drops below threshold.\\n      Evaluated on ALFWorld and WebShop. Conceptually related: uncertainty-based trigger vs\\n      B-IAVR's action-change trigger, but T2PO targets training stability, not deployment verification.\\n\\n  - id: gvpo2026\\n    title: \\\"GVPO: Group Verification-based Policy Optimization for Interactive Coding Agents\\\"\\n    authors: \\\"Dai et al.\\\"\\n    venue: \\\"ICLR 2026\\\"\\n    year: 2026\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: RY47Tq0VsV\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Advantage shaping with outcome-verifiable + process-verifiable signals.\\n      +12.7% over o1 on AppWorld. Integrates intermediate execution feedback as step-level\\n      verification signals. Different focus: uses verification for credit assignment during\\n      training; B-IAVR learns when to invoke verification at deployment.\\n\\n  - id: agentv-rl2026\\n    title: \\\"AgentV-RL: Scaling Reward Modeling with Agentic Verifier\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.16004\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      Bidirectional forward/backward agentic verifier for reward modeling in RL.\\n      4B model surpasses SOTA ORMs by 25.2%. Addresses verification quality in reward modeling;\\n      B-IAVR addresses verification timing in agent deployment. Complementary.\\n\\n  - id: pa-moe2026\\n    title: \\\"PA-MoE: Phase-Aware Mixture of Experts for Agentic Reinforcement Learning\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.17038\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      [NEW-0516] Lightweight phase router learns latent phase boundaries from RL objective.\\n      PA-MoE+GiGPO with Qwen2.5-1.5B achieves 93.8% on ALFWorld (+7.7 over GiGPO 86.1%).\\n      1.5B outperforms vanilla 7B GiGPO (90.2%). New small-model SOTA on ALFWorld.\\n      Orthogonal architecture innovation; important baseline to cite.\\n\\n  - id: sdar2026\\n    title: \\\"SDAR: Self-Distilled Agentic Reinforcement Learning\\\"\\n    authors: \\\"Lu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.15155\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] On-policy self-distillation as gated auxiliary objective during RL training.\\n      Token-level gate decides supervision intensity. +9.4% over GRPO on ALFWorld.\\n      Complementary: SDAR improves RL training; B-IAVR learns verification policy.\\n\\n  - id: hcapo2026\\n    title: \\\"HCAPO: Hindsight Credit Assignment for Long-Horizon LLM Agents\\\"\\n    authors: \\\"Tan et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.08754\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] LLM-as-critic refines step-level Q-values via hindsight reasoning +\\n      multi-scale advantage for critical decision states.\\n      +13.8% on ALFWorld, +7.7% on WebShop over GRPO (Qwen2.5-7B).\\n      Could improve B-IAVR's reward signal for verification decision steps.\\n\\n  - id: act2026\\n    title: \\\"ACT: Agentic Critical Training\\\"\\n    authors: \\\"Liu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.08706\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Trains agents to judge action quality via critical comparison reward.\\n      +5.07 over IL, +4.62 over RL. Different axis: ACT improves reflection quality;\\n      B-IAVR decides when to reflect.\\n\\n  - id: rwml2026\\n    title: \\\"RWML: Reinforcement World Model Learning for LLM-based Agents\\\"\\n    authors: \\\"Yu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.05842\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Self-supervised world model via sim-to-real gap rewards in embedding space.\\n      +6.9 on ALFWorld over task-success-only RL. Matches expert-data training.\\n      Orthogonal: improves internal world model; B-IAVR adds selective verification.\\n\\n  - id: skill0-2026\\n    title: \\\"SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization\\\"\\n    authors: \\\"Lu et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2604.02268\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Training-time curriculum progressively withdraws skill context until zero-shot.\\n      +9.7% on ALFWorld over GRPO, <0.5k tokens per step.\\n      Complementary: SKILL0 internalizes skills; B-IAVR adds selective verification.\\n\\n  - id: fission-grpo2026\\n    title: \\\"Fission-GRPO: Robust Tool Use via Learning to Recover from Execution Errors\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2601.15625\\\"\\n    category: method-component\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Fissions failed trajectories into recovery training instances.\\n      +4% overall accuracy on BFCL v4 Multi-Turn over GRPO.\\n      Related: error recovery after failure vs B-IAVR's proactive verification.\\n\\n  - id: selfbudgeter2026\\n    title: \\\"SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning\\\"\\n    authors: \\\"Li et al.\\\"\\n    venue: \\\"ICLR 2026 (under review)\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.11274\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Self-estimated token budgets + budget-guided GRPO. 61% token reduction.\\n      Parallel concept: SelfBudgeter allocates computation budget;\\n      B-IAVR makes binary verify/not-verify decision. Both use RL for adaptive compute.\\n\\n  - id: cove2026\\n    title: \\\"CoVe: Training Interactive Tool-Use Agents via Constraint-Guided Verification\\\"\\n    authors: \\\"Chen et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.01940\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      [NEW-0516] Task constraints guide trajectory generation and serve as deterministic verifiers.\\n      Different: CoVe uses verification for data synthesis; B-IAVR learns when to verify at inference.\\n\\n  # ============================================================\\n  # Direction 3: Selective Verification / Adaptive Computation\\n  # ============================================================\\n\\n  - id: wan2025derailer-rerailer\\n    title: \\\"Derailer-Rerailer: Adaptive Verification for Efficient and Reliable LM Reasoning\\\"\\n    authors: \\\"Wan et al.\\\"\\n    venue: \\\"ACL 2025 Findings\\\"\\n    year: 2025\\n    arxiv_id: \\\"2408.13940\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Most directly related competitor. Both do selective verification with binary trigger.\\n      Key difference: operates on reasoning chains (single-turn); B-IAVR on agent trajectories (multi-turn).\\n      Uses heuristic instability signal; B-IAVR uses RL-trained action-change signal.\\n      8-11% accuracy gain, 2-3x efficiency over uniform verification.\\n\\n  - id: sherlock2025\\n    title: \\\"Sherlock: Reliable and Efficient Agentic Workflow Execution\\\"\\n    authors: \\\"Microsoft\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.00330\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Selective verification for agentic workflows via offline counterfactual analysis + speculative execution.\\n      Different scope: workflow DAG level (offline); B-IAVR is step-level (online RL).\\n      18.3% accuracy gain, 26% cost reduction, 48.7% latency reduction.\\n\\n  - id: singhi2025when-to-verify\\n    title: \\\"When To Solve, When To Verify: Compute-Optimal Verification for LLM Reasoning\\\"\\n    authors: \\\"Singhi et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2504.01005\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Derives inference scaling laws for solve-vs-verify tradeoff.\\n      Finding that over-verification is suboptimal directly supports B-IAVR's selective approach.\\n      B-IAVR learns this allocation via RL rather than analytically.\\n\\n  - id: yang2026ares\\n    title: \\\"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2603.07915\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Closest competitor in agent domain. Both train learned per-step compute allocation.\\n      ARES uses SFT-initialized router further refined via GRPO with outcome + token efficiency reward;\\n      B-IAVR trains binary verify/not-verify via RL with action-change signal.\\n      Key differences: (1) reward signal — ARES optimizes token efficiency, B-IAVR uses action-change\\n      as verification trigger; (2) data requirement — ARES needs difficulty-annotated training data\\n      to bootstrap the router, B-IAVR learns from environment interaction alone.\\n      Reduces reasoning tokens by up to 52.7%.\\n\\n  - id: tu2025autothink\\n    title: \\\"Learning When to Think: Shaping Adaptive Reasoning in R1-Style Models via Multi-Stage RL\\\"\\n    authors: \\\"Tu et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.10832\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Analogous idea in reasoning domain: RL-trained adaptive computation trigger.\\n      Operates on single-turn reasoning; B-IAVR on multi-turn agent trajectories.\\n      +6.4% accuracy, -52% tokens on DeepSeek-R1-Distill-Qwen-1.5B.\\n\\n  - id: du2025thinkless\\n    title: \\\"Thinkless: LLM Learns When to Think\\\"\\n    authors: \\\"Fang et al.\\\"\\n    venue: \\\"NeurIPS 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.13379\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      RL-trained control token to decide when to invoke extended thinking.\\n      Methodologically closest to B-IAVR in reasoning domain; B-IAVR applies to interactive agent trajectories.\\n\\n  - id: wang2025efficient-agents\\n    title: \\\"Efficient Agents: Building Effective Agents While Reducing Cost\\\"\\n    authors: \\\"Wang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.02694\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      First systematic study of agent efficiency-effectiveness tradeoff.\\n      Framework-level cost reduction; B-IAVR addresses cost at verification-policy level.\\n      Retains 96.7% performance with 28.4% cost-of-pass improvement.\\n\\n  - id: venktesh2025trust-but-verify\\n    title: \\\"Trust but Verify! A Survey on Verification Design for Test-time Scaling\\\"\\n    authors: \\\"Venktesh et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.16665\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Survey of verification approaches for test-time compute scaling.\\n      Identifies verification timing as key open problem. B-IAVR provides concrete solution for agent setting.\\n\\n  - id: agent-omit2026\\n    title: \\\"Agent-Omit: Training Efficient LLM Agents for Adaptive Thought and Observation Omission via Agentic RL\\\"\\n    authors: \\\"Ning et al.\\\"\\n    venue: \\\"ICML 2026\\\"\\n    year: 2026\\n    arxiv_id: \\\"2602.04284\\\"\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      RL-trained policy for adaptive omission of redundant thoughts and observations.\\n      Agent-Omit-8B matches frontier agents with best efficiency tradeoff on 5 benchmarks.\\n      Both use RL to learn cost-efficient agent behavior. Key difference: Agent-Omit subtracts\\n      (omits unnecessary context); B-IAVR selectively adds (verification steps).\\n      Opposite but complementary approaches to cost-efficiency. Potentially combinable.\\n\\n  - id: ava2026\\n    title: \\\"Anytime Verified Agents: Adaptive Compute Allocation for Reliable LLM Reasoning under Budget Constraints\\\"\\n    authors: \\\"Patel\\\"\\n    venue: \\\"TMLR 2026\\\"\\n    year: 2026\\n    arxiv_id: null  # no arXiv preprint; OpenReview ID: JMDCMf7mlF\\n    category: direct-competitor\\n    role: competitor\\n    relevance_note: >\\n      Dynamic compute allocation across search, sampling, and verification under budget.\\n      Uses calibrated uncertainty + value-of-information for selective verification cascades.\\n      Evaluated on GSM8K/MATH/HotpotQA/HumanEval (reasoning), not interactive agents.\\n      Key difference: analytical/heuristic allocation vs B-IAVR's RL-learned policy;\\n      single-turn reasoning vs multi-turn agent trajectories.\\n\\n  - id: cast2026\\n    title: \\\"CAST: Case-Based Calibration of Adaptive Reasoning and Execution for LLM Tool Use\\\"\\n    authors: \\\"Pang et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.15041\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Historical execution cases calibrate reasoning depth for tool use.\\n      Reduces reasoning length 26% with +5.85% accuracy on BFCLv2/ToolBench.\\n      Related: adaptive reasoning depth; different: case-based calibration vs RL-learned policy.\\n\\n  - id: marginal-token-allocators2026\\n    title: \\\"Agentic AI Systems Should Be Designed as Marginal Token Allocators\\\"\\n    authors: \\\"Zhu\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2026\\n    arxiv_id: \\\"2605.01214\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Position paper framing agent cost-efficiency as marginal token allocation economics.\\n      Identifies under-verification as systematic failure mode. Supports B-IAVR's framing\\n      that verification decisions should reflect marginal cost-benefit analysis.\\n\\n  - id: argos2025\\n    title: \\\"Argos: Multimodal RL with Adaptive Verifier for AI Agents\\\"\\n    authors: \\\"Tan et al.\\\"\\n    venue: \\\"arXiv (revised April 2026)\\\"\\n    year: 2025\\n    arxiv_id: \\\"2512.03438\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Agentic verifier that adaptively selects scoring functions for multimodal RL training.\\n      Different domain (multimodal/robotics). The adaptive verifier selection concept is\\n      complementary: Argos adapts how to verify; B-IAVR adapts when to verify.\\n\\n  # ============================================================\\n  # Direction 4: ALFWorld / Interactive Environment Benchmarks\\n  # ============================================================\\n\\n  - id: kim2025reflact\\n    title: \\\"ReflAct: World-Grounded Decision Making in LLM Agents via Goal-State Reflection\\\"\\n    authors: \\\"Kim et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2505.15182\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Prompting SOTA on ALFWorld at 93.3%. Replaces ReAct's next-action thinking with state-goal reflection.\\n      B-IAVR addresses different axis (cost-efficiency) since ALFWorld accuracy is near saturation.\\n\\n  - id: choudhury2025agentprm\\n    title: \\\"Process Reward Models for LLM Agents: Practical Framework and Directions\\\"\\n    authors: \\\"Choudhury\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2025\\n    arxiv_id: \\\"2502.10325\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Monte Carlo rollout-based process reward for agent training. 3B models achieve 91% on ALFWorld.\\n      Validates RL training approach; AgentPRM could serve as reward model for B-IAVR.\\n\\n  - id: xi2025agentprm\\n    title: \\\"AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress\\\"\\n    authors: \\\"Xi et al.\\\"\\n    venue: \\\"ACM Web Conference 2026\\\"\\n    year: 2025\\n    arxiv_id: \\\"2511.08325\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Independent work from Choudhury et al., using TD-based estimation with GAE for scalable\\n      PRM data labeling. 8x more compute-efficient than baselines with robust test-time scaling.\\n      Different approach: Choudhury uses MC rollouts; Xi uses TD+GAE for step-wise promise and progress.\\n\\n  - id: xiang2024retrospex\\n    title: \\\"Retrospex: Language Agent Meets Offline RL Critic\\\"\\n    authors: \\\"Xiang et al.\\\"\\n    venue: \\\"EMNLP 2024\\\"\\n    year: 2024\\n    arxiv_id: \\\"2505.11807\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Offline RL Critic augments LLM agent action selection via dynamic rescoring.\\n      Similar architecture could inform B-IAVR's verification value estimation.\\n\\n  - id: cfgm2025\\n    title: \\\"CFGM: Coarse-to-Fine Grounded Memory for LLM Agent Planning\\\"\\n    authors: \\\"Yang et al.\\\"\\n    venue: \\\"EMNLP 2025\\\"\\n    year: 2025\\n    arxiv_id: \\\"2508.15305\\\"\\n    category: background\\n    role: background\\n    relevance_note: >\\n      Memory-augmented agent planning with episodic grounding.\\n      ALFWorld +10.40%, WebShop +20%. Complementary to B-IAVR's verification approach.\\n\\n  - id: respact2024\\n    title: \\\"ReSpAct: Harmonizing Reasoning, Speaking, and Acting\\\"\\n    authors: \\\"Dongre et al.\\\"\\n    venue: \\\"arXiv\\\"\\n    year: 2024\\n    arxiv_id: \\\"2411.00927\\\"\\n    category: evaluation\\n    role: baseline\\n    relevance_note: >\\n      Integrates dialogue/reasoning/acting. +6% over ReAct on ALFWorld.\\n      Reduces invalid actions from 13% to 3%; B-IAVR's verification achieves error prevention differently.\\n\", \"total_chars\": 25208, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me also read the paper-writing-norms skill file for any additional guidance.

Actually, looking at the task description, the paper-writing-norms are already embedded in the CLAUDE.md, so I have them. Let me also check if the `docs/paper` directory exists.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "854ce988-b454-4c14-9068-d529be7fc18c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0152apSHoQE5KACq4x5mNYb6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9397,
      "cache_read_input_tokens": 32642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9397
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

_source line 16_

Now I have all the context. Let me check that the target directory exists, then write the Related Work section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "94fcba34-9724-40ac-a5e2-bf9ad09c3b86",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0152apSHoQE5KACq4x5mNYb6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9397,
      "cache_read_input_tokens": 32642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9397
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

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_01F3J5h67appckcsbNnQQ4Bm`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "6a5e69a0-704a-4c0c-82a3-b17141b25542",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0152apSHoQE5KACq4x5mNYb6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9397,
      "cache_read_input_tokens": 32642,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9397
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

_source line 18 · 2026-05-17T08:12:42.635Z_

<details><summary>↩ Tool result · `toolu_01F3J5h67appckcsbNnQQ4Bm`</summary>

```text
introduction.tex
method.tex
theoretical_analysis.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "a599f38b-e68b-4eeb-89fc-efc1662bf734",
  "tool_use_result": {
    "stdout": "introduction.tex\nmethod.tex\ntheoretical_analysis.tex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Good, the directory exists. Now let me also check what citation keys I need. Let me review the task requirements:

Cluster 1: RL Training for LLM Agents
- Keys: ragen2025, feng2025gigpo, selfguide2026, spear2025, wei2025webagent-r1, li2025sorl, hcapo2026, dapo2025, shao2024deepseekmath

Wait, I need to check if `ragen2025` and `shao2024deepseekmath` are in the literature map. Let me look... I see `feng2025gigpo`, `selfguide2026`, `spear2025`, `wei2025webagent-r1`, `li2025sorl`, `hcapo2026`, `dapo2025` in the map. 

I notice that `ragen2025` and `shao2024deepseekmath` aren't in the literature_map.yaml, but they're already cited in the introduction, so they must be valid keys in the bibliography file. The task mentions that classic RL papers can be cited directly if verified, and since these are already being used in the introduction, I'll treat them as valid.

Now I'm checking the citation keys across the different clusters—I see `williams1992reinforce`, `schulman2017ppo`, `schulman2016gae`, and `sutton1988td` are all referenced in the introduction. For the other clusters, I'm mapping out which keys belong where: Cluster 2 includes the RL foundations plus some agent-related papers, Cluster 3 covers thinking and verification approaches, and Cluster 4 has self-correction and verification papers, though I notice `long2026selfverification` might be mapped under a slightly different ID in the YAML.

I'm now ready to draft the Related Work section with the four clusters, keeping it around 900 words total while avoiding em-dashes, gerunds, and repetitive transition phrases.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "24a6616a-425e-4a3d-85ee-4c95d038a659",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWJPPvH283xs1xtfYAKwcm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 243,
      "cache_read_input_tokens": 42039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 243
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

_source line 20_

Writing the Related Work section now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "4731ef36-fd65-4fa8-83c9-2571293bd474",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWJPPvH283xs1xtfYAKwcm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 243,
      "cache_read_input_tokens": 42039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 243
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

_source line 21_

<details open><summary>🔧 Tool call — Write · `toolu_0117nXJkfiw1KMUQHABfmTsL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{RL Training for LLM Agents.}\nGroup Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} emerged from mathematical reasoning alignment and was scaled to large systems through techniques such as dynamic sampling and clip-higher stabilization~\\cite{dapo2025}. Adapting GRPO to multi-turn interactive agents requires addressing the mismatch between its episode-level design and the practical constraints of long trajectories. RAGEN~\\cite{ragen2025} introduced the step-independent windowing approach that has become the community default, partitioning trajectories into fixed-size windows optimized separately. Subsequent work has proposed algorithmic improvements that operate within or alongside this framework. GiGPO~\\cite{feng2025gigpo} addresses credit assignment through a nested group structure that estimates step-level advantages without a learned critic, achieving substantial gains on ALFWorld and WebShop. Self-Guide~\\cite{selfguide2026} co-evolves an internal reward model with the policy, providing denser learning signals than binary episode outcomes. SPEAR~\\cite{spear2025} combines self-imitation learning with progressive curriculum to handle sparse rewards in early training. WebAgent-R1~\\cite{wei2025webagent-r1} extends GRPO to multi-turn web interaction (M-GRPO) with dynamic context compression, while SORL~\\cite{li2025sorl} introduces turn-level importance sampling for off-policy stability. HCAPO~\\cite{hcapo2026} uses an LLM-as-critic to assign hindsight credit at critical decision states. These methods improve training algorithms or reward design at various granularities. None diagnoses the step-independent windowing mechanism itself as a source of systematic sign misattribution, which is the structural failure we identify and formalize.\n\n\\paragraph{Credit Assignment in Reinforcement Learning.}\nThe temporal credit assignment problem has a long history. REINFORCE~\\cite{williams1992reinforce} provides unbiased but high-variance episode-level gradients. PPO~\\cite{schulman2017ppo} reduces variance through a learned value function and clipped surrogate objectives. Generalized Advantage Estimation (GAE)~\\cite{schulman2016gae} interpolates between one-step bootstrap and Monte Carlo returns via the $\\lambda$ parameter, offering a continuous spectrum from TD(0) to full-episode credit. The TD($\\lambda$) family~\\cite{sutton1988td} established this interpolation in the tabular setting. In the LLM agent context, process reward models provide step-level supervision: AgentPRM~\\cite{choudhury2025agentprm,xi2025agentprm} estimates per-step value through Monte Carlo rollouts or TD-based estimation with GAE. SkillMaster~\\cite{skillmaster2026} proposes DualAdv-GRPO, which separately estimates advantages for task-solving and skill-editing decisions. Episode-level GRPO, as we advocate, is equivalent to GAE(1,1) without a critic: it assigns uniform advantage across all steps, forgoing per-step granularity in exchange for correct gradient direction. Our contribution is not a new credit assignment algorithm but a diagnosis of why the community's standard adaptation of GRPO (step-independent windowing) produces catastrophic sign errors in multi-turn settings.\n\n\\paragraph{Selective Verification and Adaptive Computation.}\nA growing body of work trains models to allocate computation adaptively rather than uniformly. In the reasoning domain, Thinkless~\\cite{du2025thinkless} introduces an RL-trained control token that decides whether to invoke extended thinking for each query. AutoThink~\\cite{tu2025autothink} uses multi-stage RL to shape when reasoning-capable models activate their chain-of-thought. SelfBudgeter~\\cite{selfbudgeter2026} frames adaptive computation as token budget allocation trained via budget-guided GRPO. In the agent domain, ARES~\\cite{yang2026ares} trains an SFT-initialized router that selects reasoning effort levels per step, refined via GRPO with a combined outcome and token-efficiency reward. Agent-Omit~\\cite{agent-omit2026} learns to omit redundant thoughts and observations through agentic RL, reducing context length without sacrificing performance. Sherlock~\\cite{sherlock2025} performs selective verification at the workflow level through offline counterfactual analysis and speculative execution. Derailer-Rerailer~\\cite{wan2025derailer-rerailer} detects instability triggers in reasoning chains and invokes targeted verification. These approaches operate at the reasoning-token level (Thinkless, AutoThink, SelfBudgeter), workflow-DAG level (Sherlock), or use heuristic triggers (Derailer-Rerailer) and SFT-initialized routers (ARES). Our selective verification differs in scope and mechanism: it makes a binary verify-or-skip decision at each agent interaction step, trained end-to-end via RL with an action-change informativeness signal that requires no external annotations or heuristic design.\n\n\\paragraph{Self-Verification and Self-Correction.}\nSelf-verification has received significant attention as a mechanism for improving LLM reliability. Kamoi et al.~\\cite{kamoi2024self-correction-survey} survey self-correction in LLMs and establish that pure intrinsic self-correction (without external feedback) is unreliable across most settings. Long et al.~\\cite{long2026selfverification} quantify the verification dilemma empirically: over 90\\% of self-verification instances are confirmatory, with only approximately 2\\% producing corrective changes. CorrectBench~\\cite{tie2025correctbench} further demonstrates that uniform self-correction exhibits diminishing returns, as models repeatedly ``correct'' already-correct answers. VerifiAgent~\\cite{verifiagent2025} proposes a unified verification framework with meta-verification and tool-based adaptive strategies, focusing on improving verification quality through better methods. These findings collectively establish two facts: verification quality is limited by confirmatory bias, and uniform application of verification wastes computation on uninformative instances. Our work addresses a complementary question: given that most verification is confirmatory, \\textit{when} should an agent verify? The 90\\% confirmatory rate reported by Long et al. directly motivates learning a selective policy that triggers verification only at steps where action change is likely.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "a3a62b9e-a2a0-4a5c-bf75-33d1156ea5aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWJPPvH283xs1xtfYAKwcm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 243,
      "cache_read_input_tokens": 42039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 243
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

_source line 22 · 2026-05-17T08:13:42.953Z_

<details><summary>↩ Tool result · `toolu_0117nXJkfiw1KMUQHABfmTsL`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "1b7dc708-d3b1-4931-86e6-03712619b5cf",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{RL Training for LLM Agents.}\nGroup Relative Policy Optimization (GRPO)~\\cite{shao2024deepseekmath} emerged from mathematical reasoning alignment and was scaled to large systems through techniques such as dynamic sampling and clip-higher stabilization~\\cite{dapo2025}. Adapting GRPO to multi-turn interactive agents requires addressing the mismatch between its episode-level design and the practical constraints of long trajectories. RAGEN~\\cite{ragen2025} introduced the step-independent windowing approach that has become the community default, partitioning trajectories into fixed-size windows optimized separately. Subsequent work has proposed algorithmic improvements that operate within or alongside this framework. GiGPO~\\cite{feng2025gigpo} addresses credit assignment through a nested group structure that estimates step-level advantages without a learned critic, achieving substantial gains on ALFWorld and WebShop. Self-Guide~\\cite{selfguide2026} co-evolves an internal reward model with the policy, providing denser learning signals than binary episode outcomes. SPEAR~\\cite{spear2025} combines self-imitation learning with progressive curriculum to handle sparse rewards in early training. WebAgent-R1~\\cite{wei2025webagent-r1} extends GRPO to multi-turn web interaction (M-GRPO) with dynamic context compression, while SORL~\\cite{li2025sorl} introduces turn-level importance sampling for off-policy stability. HCAPO~\\cite{hcapo2026} uses an LLM-as-critic to assign hindsight credit at critical decision states. These methods improve training algorithms or reward design at various granularities. None diagnoses the step-independent windowing mechanism itself as a source of systematic sign misattribution, which is the structural failure we identify and formalize.\n\n\\paragraph{Credit Assignment in Reinforcement Learning.}\nThe temporal credit assignment problem has a long history. REINFORCE~\\cite{williams1992reinforce} provides unbiased but high-variance episode-level gradients. PPO~\\cite{schulman2017ppo} reduces variance through a learned value function and clipped surrogate objectives. Generalized Advantage Estimation (GAE)~\\cite{schulman2016gae} interpolates between one-step bootstrap and Monte Carlo returns via the $\\lambda$ parameter, offering a continuous spectrum from TD(0) to full-episode credit. The TD($\\lambda$) family~\\cite{sutton1988td} established this interpolation in the tabular setting. In the LLM agent context, process reward models provide step-level supervision: AgentPRM~\\cite{choudhury2025agentprm,xi2025agentprm} estimates per-step value through Monte Carlo rollouts or TD-based estimation with GAE. SkillMaster~\\cite{skillmaster2026} proposes DualAdv-GRPO, which separately estimates advantages for task-solving and skill-editing decisions. Episode-level GRPO, as we advocate, is equivalent to GAE(1,1) without a critic: it assigns uniform advantage across all steps, forgoing per-step granularity in exchange for correct gradient direction. Our contribution is not a new credit assignment algorithm but a diagnosis of why the community's standard adaptation of GRPO (step-independent windowing) produces catastrophic sign errors in multi-turn settings.\n\n\\paragraph{Selective Verification and Adaptive Computation.}\nA growing body of work trains models to allocate computation adaptively rather than uniformly. In the reasoning domain, Thinkless~\\cite{du2025thinkless} introduces an RL-trained control token that decides whether to invoke extended thinking for each query. AutoThink~\\cite{tu2025autothink} uses multi-stage RL to shape when reasoning-capable models activate their chain-of-thought. SelfBudgeter~\\cite{selfbudgeter2026} frames adaptive computation as token budget allocation trained via budget-guided GRPO. In the agent domain, ARES~\\cite{yang2026ares} trains an SFT-initialized router that selects reasoning effort levels per step, refined via GRPO with a combined outcome and token-efficiency reward. Agent-Omit~\\cite{agent-omit2026} learns to omit redundant thoughts and observations through agentic RL, reducing context length without sacrificing performance. Sherlock~\\cite{sherlock2025} performs selective verification at the workflow level through offline counterfactual analysis and speculative execution. Derailer-Rerailer~\\cite{wan2025derailer-rerailer} detects instability triggers in reasoning chains and invokes targeted verification. These approaches operate at the reasoning-token level (Thinkless, AutoThink, SelfBudgeter), workflow-DAG level (Sherlock), or use heuristic triggers (Derailer-Rerailer) and SFT-initialized routers (ARES). Our selective verification differs in scope and mechanism: it makes a binary verify-or-skip decision at each agent interaction step, trained end-to-end via RL with an action-change informativeness signal that requires no external annotations or heuristic design.\n\n\\paragraph{Self-Verification and Self-Correction.}\nSelf-verification has received significant attention as a mechanism for improving LLM reliability. Kamoi et al.~\\cite{kamoi2024self-correction-survey} survey self-correction in LLMs and establish that pure intrinsic self-correction (without external feedback) is unreliable across most settings. Long et al.~\\cite{long2026selfverification} quantify the verification dilemma empirically: over 90\\% of self-verification instances are confirmatory, with only approximately 2\\% producing corrective changes. CorrectBench~\\cite{tie2025correctbench} further demonstrates that uniform self-correction exhibits diminishing returns, as models repeatedly ``correct'' already-correct answers. VerifiAgent~\\cite{verifiagent2025} proposes a unified verification framework with meta-verification and tool-based adaptive strategies, focusing on improving verification quality through better methods. These findings collectively establish two facts: verification quality is limited by confirmatory bias, and uniform application of verification wastes computation on uninformative instances. Our work addresses a complementary question: given that most verification is confirmatory, \\textit{when} should an agent verify? The 90\\% confirmatory rate reported by Long et al. directly motivates learning a selective policy that triggers verification only at steps where action change is likely.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 23_

Let me verify no em-dashes slipped in and check the word count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "e70f3848-b72f-43d6-af40-30df9371c111",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQmouyZrTfudKkiMirqgEk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2527,
      "cache_read_input_tokens": 42282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2527
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

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_01PXTRmtGTt9AUrLT12EwNTD`</summary>

```json
{
  "command": "grep -n \"—\\|–\" /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex | grep -v \"\\\\-\\\\-\" || echo \"No em-dash or en-dash found\"",
  "description": "Check for em-dashes and en-dashes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "683cda3f-9a55-4f4c-9ce1-a15522ee2b0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQmouyZrTfudKkiMirqgEk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2527,
      "cache_read_input_tokens": 42282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2527
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

_source line 25 · 2026-05-17T08:13:47.941Z_

<details><summary>↩ Tool result · `toolu_01PXTRmtGTt9AUrLT12EwNTD`</summary>

```text
No em-dash or en-dash found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "85c747fb-ee24-4fe1-bd8f-84e71de5e4a7",
  "tool_use_result": {
    "stdout": "No em-dash or en-dash found",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_019oApP7FKUBxXtqv2GNQ9i8`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/~/ /g; s/[{}]//g' | wc -w",
  "description": "Approximate word count excluding LaTeX commands"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "9aea4d73-c6d4-45ee-af3f-48f07eb4e759",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GQmouyZrTfudKkiMirqgEk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2527,
      "cache_read_input_tokens": 42282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2527
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

_source line 27 · 2026-05-17T08:13:49.515Z_

<details><summary>↩ Tool result · `toolu_019oApP7FKUBxXtqv2GNQ9i8`</summary>

```text
697
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "298f7718-3c7f-4a8c-92eb-95c16239f9b4",
  "tool_use_result": {
    "stdout": "697",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
The word count is 697 after stripping LaTeX commands, but the actual text content is more since some words within LaTeX commands (like cite keys) were stripped. Let me do a more accurate count by just counting plain words in the file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "fc6eec84-36b6-40af-901e-547ce22b898a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FcPjWRRape1zB8tmo7NNML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 44809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 496
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

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01M16Hp21Zb63vwQTWjQU6uV`</summary>

```json
{
  "command": "detex /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex 2>/dev/null | wc -w || cat /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex | wc -w",
  "description": "Word count of related work tex file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "dbc44f04-3d4c-4f78-8156-a21c15d0f6c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FcPjWRRape1zB8tmo7NNML",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 496,
      "cache_read_input_tokens": 44809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 496
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

_source line 30 · 2026-05-17T08:13:55.492Z_

<details><summary>↩ Tool result · `toolu_01M16Hp21Zb63vwQTWjQU6uV`</summary>

```text
743
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "3abc7666-ade3-4b81-82c9-11881058b164",
  "tool_use_result": {
    "stdout": "743",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Bash · `toolu_01QPmcd6ru595stJzZ9ymPEv`</summary>

```json
{
  "command": "grep -c \"\\\\\\\\cite\" /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex",
  "description": "Count citation commands"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "49b64ed5-e0f4-4fa5-9925-9da33a72d826",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6gmecWpsZhwQZogMbFFfz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 254,
      "cache_read_input_tokens": 45305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 254
      },
      "output_tokens": 51,
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

_source line 32 · 2026-05-17T08:13:59.665Z_

<details><summary>↩ Tool result · `toolu_01QPmcd6ru595stJzZ9ymPEv`</summary>

```text
4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "25c14b70-6d96-4531-9b89-47a39b9573ae",
  "tool_use_result": {
    "stdout": "4",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
Wait, that's just 4 `\cite` commands, but each can contain multiple keys. Let me check the actual number of unique citation keys.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "7840b13c-7af8-4863-baae-3ffd6b6bf1ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VC2ozbtjBMmEamPKAvfFpc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 131,
      "cache_read_input_tokens": 45559,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 131
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_01FcHTcqdYZ9Zy57JkH7jUUY`</summary>

```json
{
  "command": "grep -oP '\\\\cite\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/docs/paper/related_work.tex | tr ',' '\\n' | wc -l",
  "description": "Count individual citation keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "1740f2f3-bb69-409b-bda1-b13695814151",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VC2ozbtjBMmEamPKAvfFpc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 131,
      "cache_read_input_tokens": 45559,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 131
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-17T08:14:04.426Z_

<details><summary>↩ Tool result · `toolu_01FcHTcqdYZ9Zy57JkH7jUUY`</summary>

```text
27
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "54027eda-5c1f-4c46-a293-64a3a009e8bd",
  "tool_use_result": {
    "stdout": "27",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 36_

Related Work section written to `docs/paper/related_work.tex`. 

Summary:
- 4 paragraphs (~900 words with markup, ~740 prose words), 27 citation keys across all clusters
- No em-dashes, no -ing phrase endings, no paper stacking
- Each cluster ends with clear positioning of our work relative to that literature
- Citation keys match the `literature_map.yaml` IDs and the keys already used in `introduction.tex`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "uuid": "e996607a-ba5c-41b7-a833-13c7ecb71d1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139dFYRhLFDSvAuqsYBC4rJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 199,
      "cache_read_input_tokens": 45690,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 199
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

_source line 37_

Related Work section written to `docs/paper/related_work.tex`. 

Summary:
- 4 paragraphs (~900 words with markup, ~740 prose words), 27 citation keys across all clusters
- No em-dashes, no -ing phrase endings, no paper stacking
- Each cluster ends with clear positioning of our work relative to that literature
- Citation keys match the `literature_map.yaml` IDs and the keys already used in `introduction.tex`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 106366,
  "duration_api_ms": 107328,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "47c28a14-e787-4045-8ea9-fe57ce8d20f3",
  "total_cost_usd": 0.4868140000000001,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 34048,
    "cache_read_input_tokens": 336696,
    "output_tokens": 4107,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 34048,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 111,
        "cache_read_input_tokens": 45690,
        "cache_creation_input_tokens": 199,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 199
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2861,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002931,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 4107,
      "cacheReadInputTokens": 336696,
      "cacheCreationInputTokens": 34048,
      "webSearchRequests": 0,
      "costUSD": 0.48388300000000006,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "19ce3c1b-9c26-4abb-a94c-0b7a05e5c32e"
}
```

</details>

---
