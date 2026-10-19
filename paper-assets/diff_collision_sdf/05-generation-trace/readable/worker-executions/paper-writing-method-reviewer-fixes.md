# paper writing method reviewer fixes

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_paper_writing_method_reviewer_fixes_20260526T160819.log`
- **Structured JSON:** [`3c724321f20e2781dd0e.json`](../../sessions/3c/3c724321f20e2781dd0e.json)

## Before a recorded user message

26 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf",
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
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
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
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
  "uuid": "d711e3c3-d5da-4c3a-b4fc-77113dd64406",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/memory/"
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
    "resetsAt": 1779828000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a4d66344-772f-4d38-8899-e81d9fa1932a",
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc"
}
```

---

### Assistant

_source line 4_

I'll start by reading the current method.tex file to understand its structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "59c995e9-4991-4ee8-bda9-c8e5a087caa9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WsuYsRsSxqFesbAYZpeFoq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12071,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12071
      },
      "output_tokens": 2,
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01QuPJvZZKtDWnEp6x47QwrC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "790ba2f7-4dd7-4b5f-b5be-447bce4f5ce4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WsuYsRsSxqFesbAYZpeFoq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12071,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12071
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-26T16:08:31.955Z_

<details><summary>↩ Tool result · `toolu_01QuPJvZZKtDWnEp6x47QwrC`</summary>

```text
1	\section{Experimental Setup and Metrics}\label{sec:method}
2	
3	This section defines the benchmark, models, training procedures, and evaluation metrics that underpin the analyses in Sections~\ref{sec:fake_safety}--\ref{sec:avoidance_source}. The central methodological contribution is the displacement-filtered Collision Avoidance Rate (CAR$_\text{f}$), a corrective metric that separates genuine obstacle avoidance from action collapse (\S\ref{sec:dfcar}).
4	
5	\subsection{Benchmark and Models}\label{sec:benchmark}
6	
7	We conduct all experiments on SafeLIBERO~\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\cite{liu2023libero}. SafeLIBERO augments standard manipulation tasks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety. We select the \textit{object\_pudding} suite (Level~I), which comprises four tabletop manipulation tasks: pick \texttt{orange\_juice}, \texttt{chocolate\_pudding}, \texttt{milk}, or \texttt{bbq\_sauce} and place into a basket. In each task, non-target objects surround the manipulation target, and the MuJoCo physics engine registers any contact between the robot and a non-target object as a collision event.
8	
9	We evaluate two Vision-Language-Action (VLA) models from the Pi0 family~\cite{black2024pi0}. \textbf{Pi0} (${\sim}$2.5B parameters) pairs a PaliGemma vision-language encoder with a dedicated action expert that generates continuous actions via flow matching~\cite{lipman2023flow}. \textbf{Pi0.5} (from Physical Intelligence) extends this architecture with broader pre-training data and serves as a stronger baseline with substantially higher task capability and less susceptibility to action collapse.
10	
11	Table~\ref{tab:configurations} summarizes the six training configurations. Each model is trained for 30K steps. Evaluation uses 50 episodes per task across 4 tasks (200 episodes per configuration). For multi-seed experiments on Pi0.5, we run 3 seeds (600 episodes per configuration). Initial object placements are fixed across methods to ensure fair comparison.
12	
13	\begin{table}[t]
14	\centering
15	\caption{Training configurations. Trainable parameter counts exclude the frozen backbone. The SDF auxiliary heads add $<$660K parameters to the ${\sim}$33.5M LoRA budget.}
16	\label{tab:configurations}
17	\vspace{2pt}
18	\small
19	\begin{tabular}{llr}
20	\toprule
21	Configuration & Description & Trainable Params \\
22	\midrule
23	Pi0 Full-FT & Full fine-tune, flow-matching loss & ${\sim}$3.5B \\
24	Pi0 LoRA & LoRA adapters only & ${\sim}$33.5M \\
25	Pi0+A1 (SDF aux) & LoRA + SDF decoder + EE extractor & ${\sim}$34.2M \\
26	Pi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\sim}$34.2M \\
27	Pi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\sim}$33.5M \\
28	Pi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\lambda \in \{0.005, 0.01, 0.1\}$ & ${\sim}$34.2M \\
29	\bottomrule
30	\end{tabular}
31	\end{table}
32	
33	\subsection{Standard Metrics}\label{sec:standard_metrics}
34	
35	We report two conventional metrics. The \emph{Collision Avoidance Rate} (CAR) is the fraction of episodes in which no collision occurs between the robot and any non-target object:
36	\begin{equation}\label{eq:car}
37	\text{CAR} = \frac{|\{e : \text{safe}(e)\}|}{|E|}
38	\end{equation}
39	where $E$ is the set of all evaluation episodes and $\text{safe}(e)$ indicates that episode $e$ contains zero collision events. The \emph{Task Success Rate} (TSR) is the fraction of episodes where the manipulation task reaches completion:
40	\begin{equation}\label{eq:tsr}
41	\text{TSR} = \frac{|\{e : \text{success}(e)\}|}{|E|}
42	\end{equation}
43	These two metrics are standard in the SafeLIBERO evaluation protocol and in the broader VLA safety literature~\cite{hu2025vlsa,zhang2025safevla}.
44	
45	\subsection{Displacement-Filtered CAR}\label{sec:dfcar}
46	
47	Standard CAR conflates two qualitatively distinct behaviors: a robot that plans a trajectory around obstacles, and a robot that has collapsed into inaction. Both register as ``safe,'' yet only the former reflects collision avoidance capability. We introduce CAR$_\text{f}$, which excludes action-collapsed episodes from both numerator and denominator.
48	
49	\paragraph{Action collapse.} We define an episode $e$ as \emph{action-collapsed} when its maximum end-effector (EE) displacement satisfies
50	\begin{equation}
51	d_{\max}(e) < \tau_d
52	\end{equation}
53	where $d_{\max}(e) = \max_{t} \| \mathbf{p}_t - \mathbf{p}_0 \|_2$ is the maximum Euclidean displacement of the EE from its initial position across all timesteps, and $\tau_d$ is a displacement threshold. We set $\tau_d = 0.1$\,mm, corresponding to sub-actuator-resolution motion.
54	
55	\paragraph{Definition.} The displacement-filtered CAR is:
56	\begin{equation}\label{eq:car_f}
57	\text{CAR}_\text{f} = \frac{|\{e : \text{safe}(e) \;\land\; d_{\max}(e) \geq \tau_d\}|}{|\{e : d_{\max}(e) \geq \tau_d\}|}
58	\end{equation}
59	CAR$_\text{f}$ retains only episodes with sufficient EE motion and measures the collision avoidance rate exclusively among them.
60	
61	\paragraph{Threshold robustness.} The specific choice of $\tau_d$ is not critical. The displacement distribution across all evaluated models is sharply bimodal: collapsed episodes cluster below 1\,$\mu$m, while active episodes exceed 200\,mm. No episodes fall in the intermediate range. This five-order-of-magnitude gap means that any $\tau_d \in [2, 200]$\,mm produces identical filtering results. We verify this empirically in Appendix~\ref{sec:appendix_threshold}.
62	
63	\paragraph{Diagnostic capability.} CAR$_\text{f}$ serves two functions. First, it detects fake safety: Pi0+A1 reports CAR\,=\,91.5\% under the standard metric, but CAR$_\text{f} \approx 0$\% because 99.6\% of its safe episodes are action-collapsed. Second, it validates genuine safety: Pi0.5 achieves CAR$_\text{f}$ equal to its raw CAR (28.5\%), with 0\% of episodes filtered, because all safe episodes involve EE displacement above 288\,mm.
64	
65	\subsection{SDF Auxiliary Training}\label{sec:sdf_aux}
66	
67	We augment the LoRA-adapted VLA with two lightweight auxiliary heads that provide geometric supervision during training.
68	
69	\paragraph{SDF Decoder ($f_\text{SDF}$).} A 4-layer MLP (hidden dimension 256, Softplus activation with $\beta = 5$, ${\sim}$395K parameters) predicts the signed distance $\Phi(\mathbf{x})$ from the current EE position $\mathbf{x}$ to the nearest obstacle surface. The decoder reads from intermediate features of the VLA action expert. The ground-truth signed distance field is precomputed from obstacle meshes using trimesh/pysdf, with values clamped at $\delta = 0.05$\,m and a safety margin $m = 0.01$\,m applied to shift the zero-crossing outward from the obstacle surface.
70	
71	\paragraph{EE Extractor ($f_\text{EE}$).} A 2-layer MLP ($1024 \to 256 \to 3$, ${\sim}$263K parameters) predicts the 3D EE position from the same action expert features. This auxiliary head provides the query point for the SDF decoder and serves as an implicit regularizer on the learned feature representation.
72	
73	\paragraph{Training objective.} The total loss combines the standard flow-matching action loss with the two auxiliary losses:
74	\begin{equation}\label{eq:total_loss}
75	\mathcal{L}_\text{total} = \mathcal{L}_\text{action} + \lambda \left( \mathcal{L}_\text{SDF} + \mathcal{L}_\text{EE} \right)
76	\end{equation}
77	where $\mathcal{L}_\text{SDF}$ is a clamped $L_1$ loss on predicted SDF values with an Eikonal regularizer, $\mathcal{L}_\text{EE}$ is MSE on predicted EE position, and $\lambda$ controls the auxiliary loss weight. We evaluate $\lambda \in \{0.005, 0.01, 0.1\}$. The total auxiliary overhead is $<$660K parameters, less than 2\% of the ${\sim}$33.5M LoRA parameter budget.
78	
79	\paragraph{Optimization.} All models are trained with AdamW, a cosine learning rate schedule decaying from $2.5 \times 10^{-5}$ to $2.5 \times 10^{-6}$, for 30K steps with batch size 32. For Pi0.5+A1, training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization.
80	
81	\subsection{Oracle SDF Refinement}\label{sec:oracle_setup}
82	
83	To test the theoretical upper bound of EE-only SDF refinement (Section~\ref{sec:ee_only}), we replace the learned SDF network with the ground-truth signed distance field computed from the simulation geometry. This eliminates prediction error and isolates the structural limitation of the refinement paradigm.
84	
85	We evaluate three oracle variants:
86	\begin{itemize}
87	\item \textit{Oracle-adaptive}: runtime gradient refinement with a dynamic step size $\alpha$ that scales inversely with gradient magnitude, applied in Cartesian action space.
88	\item \textit{Oracle-fixed}: a constant step size $\alpha = 0.005$, also in Cartesian action space.
89	\item \textit{Oracle-feature}: gradient applied in the VLA's latent feature space rather than directly to Cartesian actions. This variant averages 241.7 refinement steps per episode (vs.\ ${\sim}$14 for the Cartesian variants), as the feature-space gradient must propagate through the action decoder.
90	\end{itemize}
91	Each variant is evaluated for 160 episodes (4 tasks $\times$ 40 episodes) with a single seed. The oracle experiments are designed to test Claim~2 (Section~\ref{sec:ee_only}): if EE-only SDF refinement is structurally sound, oracle performance should exceed unrefined baselines by a wide margin.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "59be8eb5-efe9-4ba2-917b-55b0515ff27a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex",
      "content": "\\section{Experimental Setup and Metrics}\\label{sec:method}\n\nThis section defines the benchmark, models, training procedures, and evaluation metrics that underpin the analyses in Sections~\\ref{sec:fake_safety}--\\ref{sec:avoidance_source}. The central methodological contribution is the displacement-filtered Collision Avoidance Rate (CAR$_\\text{f}$), a corrective metric that separates genuine obstacle avoidance from action collapse (\\S\\ref{sec:dfcar}).\n\n\\subsection{Benchmark and Models}\\label{sec:benchmark}\n\nWe conduct all experiments on SafeLIBERO~\\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\\cite{liu2023libero}. SafeLIBERO augments standard manipulation tasks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety. We select the \\textit{object\\_pudding} suite (Level~I), which comprises four tabletop manipulation tasks: pick \\texttt{orange\\_juice}, \\texttt{chocolate\\_pudding}, \\texttt{milk}, or \\texttt{bbq\\_sauce} and place into a basket. In each task, non-target objects surround the manipulation target, and the MuJoCo physics engine registers any contact between the robot and a non-target object as a collision event.\n\nWe evaluate two Vision-Language-Action (VLA) models from the Pi0 family~\\cite{black2024pi0}. \\textbf{Pi0} (${\\sim}$2.5B parameters) pairs a PaliGemma vision-language encoder with a dedicated action expert that generates continuous actions via flow matching~\\cite{lipman2023flow}. \\textbf{Pi0.5} (from Physical Intelligence) extends this architecture with broader pre-training data and serves as a stronger baseline with substantially higher task capability and less susceptibility to action collapse.\n\nTable~\\ref{tab:configurations} summarizes the six training configurations. Each model is trained for 30K steps. Evaluation uses 50 episodes per task across 4 tasks (200 episodes per configuration). For multi-seed experiments on Pi0.5, we run 3 seeds (600 episodes per configuration). Initial object placements are fixed across methods to ensure fair comparison.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training configurations. Trainable parameter counts exclude the frozen backbone. The SDF auxiliary heads add $<$660K parameters to the ${\\sim}$33.5M LoRA budget.}\n\\label{tab:configurations}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nConfiguration & Description & Trainable Params \\\\\n\\midrule\nPi0 Full-FT & Full fine-tune, flow-matching loss & ${\\sim}$3.5B \\\\\nPi0 LoRA & LoRA adapters only & ${\\sim}$33.5M \\\\\nPi0+A1 (SDF aux) & LoRA + SDF decoder + EE extractor & ${\\sim}$34.2M \\\\\nPi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\\sim}$34.2M \\\\\nPi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\\sim}$33.5M \\\\\nPi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ & ${\\sim}$34.2M \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Standard Metrics}\\label{sec:standard_metrics}\n\nWe report two conventional metrics. The \\emph{Collision Avoidance Rate} (CAR) is the fraction of episodes in which no collision occurs between the robot and any non-target object:\n\\begin{equation}\\label{eq:car}\n\\text{CAR} = \\frac{|\\{e : \\text{safe}(e)\\}|}{|E|}\n\\end{equation}\nwhere $E$ is the set of all evaluation episodes and $\\text{safe}(e)$ indicates that episode $e$ contains zero collision events. The \\emph{Task Success Rate} (TSR) is the fraction of episodes where the manipulation task reaches completion:\n\\begin{equation}\\label{eq:tsr}\n\\text{TSR} = \\frac{|\\{e : \\text{success}(e)\\}|}{|E|}\n\\end{equation}\nThese two metrics are standard in the SafeLIBERO evaluation protocol and in the broader VLA safety literature~\\cite{hu2025vlsa,zhang2025safevla}.\n\n\\subsection{Displacement-Filtered CAR}\\label{sec:dfcar}\n\nStandard CAR conflates two qualitatively distinct behaviors: a robot that plans a trajectory around obstacles, and a robot that has collapsed into inaction. Both register as ``safe,'' yet only the former reflects collision avoidance capability. We introduce CAR$_\\text{f}$, which excludes action-collapsed episodes from both numerator and denominator.\n\n\\paragraph{Action collapse.} We define an episode $e$ as \\emph{action-collapsed} when its maximum end-effector (EE) displacement satisfies\n\\begin{equation}\nd_{\\max}(e) < \\tau_d\n\\end{equation}\nwhere $d_{\\max}(e) = \\max_{t} \\| \\mathbf{p}_t - \\mathbf{p}_0 \\|_2$ is the maximum Euclidean displacement of the EE from its initial position across all timesteps, and $\\tau_d$ is a displacement threshold. We set $\\tau_d = 0.1$\\,mm, corresponding to sub-actuator-resolution motion.\n\n\\paragraph{Definition.} The displacement-filtered CAR is:\n\\begin{equation}\\label{eq:car_f}\n\\text{CAR}_\\text{f} = \\frac{|\\{e : \\text{safe}(e) \\;\\land\\; d_{\\max}(e) \\geq \\tau_d\\}|}{|\\{e : d_{\\max}(e) \\geq \\tau_d\\}|}\n\\end{equation}\nCAR$_\\text{f}$ retains only episodes with sufficient EE motion and measures the collision avoidance rate exclusively among them.\n\n\\paragraph{Threshold robustness.} The specific choice of $\\tau_d$ is not critical. The displacement distribution across all evaluated models is sharply bimodal: collapsed episodes cluster below 1\\,$\\mu$m, while active episodes exceed 200\\,mm. No episodes fall in the intermediate range. This five-order-of-magnitude gap means that any $\\tau_d \\in [2, 200]$\\,mm produces identical filtering results. We verify this empirically in Appendix~\\ref{sec:appendix_threshold}.\n\n\\paragraph{Diagnostic capability.} CAR$_\\text{f}$ serves two functions. First, it detects fake safety: Pi0+A1 reports CAR\\,=\\,91.5\\% under the standard metric, but CAR$_\\text{f} \\approx 0$\\% because 99.6\\% of its safe episodes are action-collapsed. Second, it validates genuine safety: Pi0.5 achieves CAR$_\\text{f}$ equal to its raw CAR (28.5\\%), with 0\\% of episodes filtered, because all safe episodes involve EE displacement above 288\\,mm.\n\n\\subsection{SDF Auxiliary Training}\\label{sec:sdf_aux}\n\nWe augment the LoRA-adapted VLA with two lightweight auxiliary heads that provide geometric supervision during training.\n\n\\paragraph{SDF Decoder ($f_\\text{SDF}$).} A 4-layer MLP (hidden dimension 256, Softplus activation with $\\beta = 5$, ${\\sim}$395K parameters) predicts the signed distance $\\Phi(\\mathbf{x})$ from the current EE position $\\mathbf{x}$ to the nearest obstacle surface. The decoder reads from intermediate features of the VLA action expert. The ground-truth signed distance field is precomputed from obstacle meshes using trimesh/pysdf, with values clamped at $\\delta = 0.05$\\,m and a safety margin $m = 0.01$\\,m applied to shift the zero-crossing outward from the obstacle surface.\n\n\\paragraph{EE Extractor ($f_\\text{EE}$).} A 2-layer MLP ($1024 \\to 256 \\to 3$, ${\\sim}$263K parameters) predicts the 3D EE position from the same action expert features. This auxiliary head provides the query point for the SDF decoder and serves as an implicit regularizer on the learned feature representation.\n\n\\paragraph{Training objective.} The total loss combines the standard flow-matching action loss with the two auxiliary losses:\n\\begin{equation}\\label{eq:total_loss}\n\\mathcal{L}_\\text{total} = \\mathcal{L}_\\text{action} + \\lambda \\left( \\mathcal{L}_\\text{SDF} + \\mathcal{L}_\\text{EE} \\right)\n\\end{equation}\nwhere $\\mathcal{L}_\\text{SDF}$ is a clamped $L_1$ loss on predicted SDF values with an Eikonal regularizer, $\\mathcal{L}_\\text{EE}$ is MSE on predicted EE position, and $\\lambda$ controls the auxiliary loss weight. We evaluate $\\lambda \\in \\{0.005, 0.01, 0.1\\}$. The total auxiliary overhead is $<$660K parameters, less than 2\\% of the ${\\sim}$33.5M LoRA parameter budget.\n\n\\paragraph{Optimization.} All models are trained with AdamW, a cosine learning rate schedule decaying from $2.5 \\times 10^{-5}$ to $2.5 \\times 10^{-6}$, for 30K steps with batch size 32. For Pi0.5+A1, training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization.\n\n\\subsection{Oracle SDF Refinement}\\label{sec:oracle_setup}\n\nTo test the theoretical upper bound of EE-only SDF refinement (Section~\\ref{sec:ee_only}), we replace the learned SDF network with the ground-truth signed distance field computed from the simulation geometry. This eliminates prediction error and isolates the structural limitation of the refinement paradigm.\n\nWe evaluate three oracle variants:\n\\begin{itemize}\n\\item \\textit{Oracle-adaptive}: runtime gradient refinement with a dynamic step size $\\alpha$ that scales inversely with gradient magnitude, applied in Cartesian action space.\n\\item \\textit{Oracle-fixed}: a constant step size $\\alpha = 0.005$, also in Cartesian action space.\n\\item \\textit{Oracle-feature}: gradient applied in the VLA's latent feature space rather than directly to Cartesian actions. This variant averages 241.7 refinement steps per episode (vs.\\ ${\\sim}$14 for the Cartesian variants), as the feature-space gradient must propagate through the action decoder.\n\\end{itemize}\nEach variant is evaluated for 160 episodes (4 tasks $\\times$ 40 episodes) with a single seed. The oracle experiments are designed to test Claim~2 (Section~\\ref{sec:ee_only}): if EE-only SDF refinement is structurally sound, oracle performance should exceed unrefined baselines by a wide margin.",
      "numLines": 91,
      "startLine": 1,
      "totalLines": 91
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

Now I have the full file. Let me identify the key sections and make all four fixes. I'll work through them systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "9483ed33-1e44-4b4f-a523-e6fea43c5d9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPycFBG6jRTGaDU8it4Q6B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3180,
      "cache_read_input_tokens": 23912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3180
      },
      "output_tokens": 2,
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

_source line 8_

<details open><summary>🔧 Tool call — Grep · `toolu_018BNv17qcM2uDyuEyp9Wbg9`</summary>

```json
{
  "pattern": "Pi0\\+A1.*99\\.6|99\\.6.*Pi0\\+A1|99\\.6",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex",
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
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "80ac4e43-90fd-4c39-abfd-8019b67dc92e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GPycFBG6jRTGaDU8it4Q6B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3180,
      "cache_read_input_tokens": 23912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3180
      },
      "output_tokens": 2,
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

_source line 9 · 2026-05-26T16:08:37.458Z_

<details><summary>↩ Tool result · `toolu_018BNv17qcM2uDyuEyp9Wbg9`</summary>

```text
63:\paragraph{Diagnostic capability.} CAR$_\text{f}$ serves two functions. First, it detects fake safety: Pi0+A1 reports CAR\,=\,91.5\% under the standard metric, but CAR$_\text{f} \approx 0$\% because 99.6\% of its safe episodes are action-collapsed. Second, it validates genuine safety: Pi0.5 achieves CAR$_\text{f}$ equal to its raw CAR (28.5\%), with 0\% of episodes filtered, because all safe episodes involve EE displacement above 288\,mm.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "34964c18-8651-491c-bb26-068048779d7a",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "63:\\paragraph{Diagnostic capability.} CAR$_\\text{f}$ serves two functions. First, it detects fake safety: Pi0+A1 reports CAR\\,=\\,91.5\\% under the standard metric, but CAR$_\\text{f} \\approx 0$\\% because 99.6\\% of its safe episodes are action-collapsed. Second, it validates genuine safety: Pi0.5 achieves CAR$_\\text{f}$ equal to its raw CAR (28.5\\%), with 0\\% of episodes filtered, because all safe episodes involve EE displacement above 288\\,mm.",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 10_

Good. Now I have the full picture. Let me apply all four fixes.

**Fix 1 (Warning 3 - highest priority):** Change Pi0+A1 to ~658K in Table 1, add footnote, add disclosure paragraph.

**Fix 2 (Warning 1):** Change Pi0 Full-FT from ~3.5B to ~2.5B.

**Fix 3 (Warning 4):** Add Pi0.5 pre-trained row to Table 1, update §3.3 mention.

**Fix 4 (Warning 2):** Add footnote about obstacle displacement for 99.6%.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "57214796-770e-4f50-a156-3c1cbef5535c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KqnotAhSyWMokhvdUyKfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 335,
      "cache_read_input_tokens": 27092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 335
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

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_01Xb178wBPsapcbrFwHg4vQh`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex",
  "old_string": "\\begin{table}[t]\n\\centering\n\\caption{Training configurations. Trainable parameter counts exclude the frozen backbone. The SDF auxiliary heads add $<$660K parameters to the ${\\sim}$33.5M LoRA budget.}\n\\label{tab:configurations}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nConfiguration & Description & Trainable Params \\\\\n\\midrule\nPi0 Full-FT & Full fine-tune, flow-matching loss & ${\\sim}$3.5B \\\\\nPi0 LoRA & LoRA adapters only & ${\\sim}$33.5M \\\\\nPi0+A1 (SDF aux) & LoRA + SDF decoder + EE extractor & ${\\sim}$34.2M \\\\\nPi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\\sim}$34.2M \\\\\nPi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\\sim}$33.5M \\\\\nPi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ & ${\\sim}$34.2M \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
  "new_string": "\\begin{table}[t]\n\\centering\n\\caption{Training configurations. Trainable parameter counts exclude the frozen backbone. The SDF auxiliary heads add $<$660K parameters to the ${\\sim}$33.5M LoRA budget.}\n\\label{tab:configurations}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nConfiguration & Description & Trainable Params \\\\\n\\midrule\nPi0 Full-FT & Full fine-tune, flow-matching loss & ${\\sim}$2.5B \\\\\nPi0 LoRA & LoRA adapters only & ${\\sim}$33.5M \\\\\nPi0+A1 (SDF aux)\\textsuperscript{$\\dagger$} & LoRA + SDF decoder + EE extractor & ${\\sim}$658K \\\\\nPi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\\sim}$34.2M \\\\\nPi0.5 (pre-trained) & No fine-tuning & 0 \\\\\nPi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\\sim}$33.5M \\\\\nPi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ & ${\\sim}$34.2M \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n\\raggedright\\footnotesize\\textsuperscript{$\\dagger$}LoRA adapter weights were not loaded due to a parameter-name mismatch; only the auxiliary SDF and EE heads were trained.\n\\end{table}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "13aac612-0c28-467a-a237-2386e93396cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KqnotAhSyWMokhvdUyKfR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 335,
      "cache_read_input_tokens": 27092,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 335
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

_source line 12 · 2026-05-26T16:08:54.408Z_

<details><summary>↩ Tool result · `toolu_01Xb178wBPsapcbrFwHg4vQh`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "f992f6d3-9f88-4509-8f1b-43c407a1de0c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex",
    "oldString": "\\begin{table}[t]\n\\centering\n\\caption{Training configurations. Trainable parameter counts exclude the frozen backbone. The SDF auxiliary heads add $<$660K parameters to the ${\\sim}$33.5M LoRA budget.}\n\\label{tab:configurations}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nConfiguration & Description & Trainable Params \\\\\n\\midrule\nPi0 Full-FT & Full fine-tune, flow-matching loss & ${\\sim}$3.5B \\\\\nPi0 LoRA & LoRA adapters only & ${\\sim}$33.5M \\\\\nPi0+A1 (SDF aux) & LoRA + SDF decoder + EE extractor & ${\\sim}$34.2M \\\\\nPi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\\sim}$34.2M \\\\\nPi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\\sim}$33.5M \\\\\nPi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ & ${\\sim}$34.2M \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}",
    "newString": "\\begin{table}[t]\n\\centering\n\\caption{Training configurations. Trainable parameter counts exclude the frozen backbone. The SDF auxiliary heads add $<$660K parameters to the ${\\sim}$33.5M LoRA budget.}\n\\label{tab:configurations}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nConfiguration & Description & Trainable Params \\\\\n\\midrule\nPi0 Full-FT & Full fine-tune, flow-matching loss & ${\\sim}$2.5B \\\\\nPi0 LoRA & LoRA adapters only & ${\\sim}$33.5M \\\\\nPi0+A1 (SDF aux)\\textsuperscript{$\\dagger$} & LoRA + SDF decoder + EE extractor & ${\\sim}$658K \\\\\nPi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\\sim}$34.2M \\\\\nPi0.5 (pre-trained) & No fine-tuning & 0 \\\\\nPi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\\sim}$33.5M \\\\\nPi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ & ${\\sim}$34.2M \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n\\raggedright\\footnotesize\\textsuperscript{$\\dagger$}LoRA adapter weights were not loaded due to a parameter-name mismatch; only the auxiliary SDF and EE heads were trained.\n\\end{table}",
    "originalFile": "\\section{Experimental Setup and Metrics}\\label{sec:method}\n\nThis section defines the benchmark, models, training procedures, and evaluation metrics that underpin the analyses in Sections~\\ref{sec:fake_safety}--\\ref{sec:avoidance_source}. The central methodological contribution is the displacement-filtered Collision Avoidance Rate (CAR$_\\text{f}$), a corrective metric that separates genuine obstacle avoidance from action collapse (\\S\\ref{sec:dfcar}).\n\n\\subsection{Benchmark and Models}\\label{sec:benchmark}\n\nWe conduct all experiments on SafeLIBERO~\\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\\cite{liu2023libero}. SafeLIBERO augments standard manipulation tasks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety. We select the \\textit{object\\_pudding} suite (Level~I), which comprises four tabletop manipulation tasks: pick \\texttt{orange\\_juice}, \\texttt{chocolate\\_pudding}, \\texttt{milk}, or \\texttt{bbq\\_sauce} and place into a basket. In each task, non-target objects surround the manipulation target, and the MuJoCo physics engine registers any contact between the robot and a non-target object as a collision event.\n\nWe evaluate two Vision-Language-Action (VLA) models from the Pi0 family~\\cite{black2024pi0}. \\textbf{Pi0} (${\\sim}$2.5B parameters) pairs a PaliGemma vision-language encoder with a dedicated action expert that generates continuous actions via flow matching~\\cite{lipman2023flow}. \\textbf{Pi0.5} (from Physical Intelligence) extends this architecture with broader pre-training data and serves as a stronger baseline with substantially higher task capability and less susceptibility to action collapse.\n\nTable~\\ref{tab:configurations} summarizes the six training configurations. Each model is trained for 30K steps. Evaluation uses 50 episodes per task across 4 tasks (200 episodes per configuration). For multi-seed experiments on Pi0.5, we run 3 seeds (600 episodes per configuration). Initial object placements are fixed across methods to ensure fair comparison.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training configurations. Trainable parameter counts exclude the frozen backbone. The SDF auxiliary heads add $<$660K parameters to the ${\\sim}$33.5M LoRA budget.}\n\\label{tab:configurations}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nConfiguration & Description & Trainable Params \\\\\n\\midrule\nPi0 Full-FT & Full fine-tune, flow-matching loss & ${\\sim}$3.5B \\\\\nPi0 LoRA & LoRA adapters only & ${\\sim}$33.5M \\\\\nPi0+A1 (SDF aux) & LoRA + SDF decoder + EE extractor & ${\\sim}$34.2M \\\\\nPi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\\sim}$34.2M \\\\\nPi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\\sim}$33.5M \\\\\nPi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ & ${\\sim}$34.2M \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Standard Metrics}\\label{sec:standard_metrics}\n\nWe report two conventional metrics. The \\emph{Collision Avoidance Rate} (CAR) is the fraction of episodes in which no collision occurs between the robot and any non-target object:\n\\begin{equation}\\label{eq:car}\n\\text{CAR} = \\frac{|\\{e : \\text{safe}(e)\\}|}{|E|}\n\\end{equation}\nwhere $E$ is the set of all evaluation episodes and $\\text{safe}(e)$ indicates that episode $e$ contains zero collision events. The \\emph{Task Success Rate} (TSR) is the fraction of episodes where the manipulation task reaches completion:\n\\begin{equation}\\label{eq:tsr}\n\\text{TSR} = \\frac{|\\{e : \\text{success}(e)\\}|}{|E|}\n\\end{equation}\nThese two metrics are standard in the SafeLIBERO evaluation protocol and in the broader VLA safety literature~\\cite{hu2025vlsa,zhang2025safevla}.\n\n\\subsection{Displacement-Filtered CAR}\\label{sec:dfcar}\n\nStandard CAR conflates two qualitatively distinct behaviors: a robot that plans a trajectory around obstacles, and a robot that has collapsed into inaction. Both register as ``safe,'' yet only the former reflects collision avoidance capability. We introduce CAR$_\\text{f}$, which excludes action-collapsed episodes from both numerator and denominator.\n\n\\paragraph{Action collapse.} We define an episode $e$ as \\emph{action-collapsed} when its maximum end-effector (EE) displacement satisfies\n\\begin{equation}\nd_{\\max}(e) < \\tau_d\n\\end{equation}\nwhere $d_{\\max}(e) = \\max_{t} \\| \\mathbf{p}_t - \\mathbf{p}_0 \\|_2$ is the maximum Euclidean displacement of the EE from its initial position across all timesteps, and $\\tau_d$ is a displacement threshold. We set $\\tau_d = 0.1$\\,mm, corresponding to sub-actuator-resolution motion.\n\n\\paragraph{Definition.} The displacement-filtered CAR is:\n\\begin{equation}\\label{eq:car_f}\n\\text{CAR}_\\text{f} = \\frac{|\\{e : \\text{safe}(e) \\;\\land\\; d_{\\max}(e) \\geq \\tau_d\\}|}{|\\{e : d_{\\max}(e) \\geq \\tau_d\\}|}\n\\end{equation}\nCAR$_\\text{f}$ retains only episodes with sufficient EE motion and measures the collision avoidance rate exclusively among them.\n\n\\paragraph{Threshold robustness.} The specific choice of $\\tau_d$ is not critical. The displacement distribution across all evaluated models is sharply bimodal: collapsed episodes cluster below 1\\,$\\mu$m, while active episodes exceed 200\\,mm. No episodes fall in the intermediate range. This five-order-of-magnitude gap means that any $\\tau_d \\in [2, 200]$\\,mm produces identical filtering results. We verify this empirically in Appendix~\\ref{sec:appendix_threshold}.\n\n\\paragraph{Diagnostic capability.} CAR$_\\text{f}$ serves two functions. First, it detects fake safety: Pi0+A1 reports CAR\\,=\\,91.5\\% under the standard metric, but CAR$_\\text{f} \\approx 0$\\% because 99.6\\% of its safe episodes are action-collapsed. Second, it validates genuine safety: Pi0.5 achieves CAR$_\\text{f}$ equal to its raw CAR (28.5\\%), with 0\\% of episodes filtered, because all safe episodes involve EE displacement above 288\\,mm.\n\n\\subsection{SDF Auxiliary Training}\\label{sec:sdf_aux}\n\nWe augment the LoRA-adapted VLA with two lightweight auxiliary heads that provide geometric supervision during training.\n\n\\paragraph{SDF Decoder ($f_\\text{SDF}$).} A 4-layer MLP (hidden dimension 256, Softplus activation with $\\beta = 5$, ${\\sim}$395K parameters) predicts the signed distance $\\Phi(\\mathbf{x})$ from the current EE position $\\mathbf{x}$ to the nearest obstacle surface. The decoder reads from intermediate features of the VLA action expert. The ground-truth signed distance field is precomputed from obstacle meshes using trimesh/pysdf, with values clamped at $\\delta = 0.05$\\,m and a safety margin $m = 0.01$\\,m applied to shift the zero-crossing outward from the obstacle surface.\n\n\\paragraph{EE Extractor ($f_\\text{EE}$).} A 2-layer MLP ($1024 \\to 256 \\to 3$, ${\\sim}$263K parameters) predicts the 3D EE position from the same action expert features. This auxiliary head provides the query point for the SDF decoder and serves as an implicit regularizer on the learned feature representation.\n\n\\paragraph{Training objective.} The total loss combines the standard flow-matching action loss with the two auxiliary losses:\n\\begin{equation}\\label{eq:total_loss}\n\\mathcal{L}_\\text{total} = \\mathcal{L}_\\text{action} + \\lambda \\left( \\mathcal{L}_\\text{SDF} + \\mathcal{L}_\\text{EE} \\right)\n\\end{equation}\nwhere $\\mathcal{L}_\\text{SDF}$ is a clamped $L_1$ loss on predicted SDF values with an Eikonal regularizer, $\\mathcal{L}_\\text{EE}$ is MSE on predicted EE position, and $\\lambda$ controls the auxiliary loss weight. We evaluate $\\lambda \\in \\{0.005, 0.01, 0.1\\}$. The total auxiliary overhead is $<$660K parameters, less than 2\\% of the ${\\sim}$33.5M LoRA parameter budget.\n\n\\paragraph{Optimization.} All models are trained with AdamW, a cosine learning rate schedule decaying from $2.5 \\times 10^{-5}$ to $2.5 \\times 10^{-6}$, for 30K steps with batch size 32. For Pi0.5+A1, training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization.\n\n\\subsection{Oracle SDF Refinement}\\label{sec:oracle_setup}\n\nTo test the theoretical upper bound of EE-only SDF refinement (Section~\\ref{sec:ee_only}), we replace the learned SDF network with the ground-truth signed distance field computed from the simulation geometry. This eliminates prediction error and isolates the structural limitation of the refinement paradigm.\n\nWe evaluate three oracle variants:\n\\begin{itemize}\n\\item \\textit{Oracle-adaptive}: runtime gradient refinement with a dynamic step size $\\alpha$ that scales inversely with gradient magnitude, applied in Cartesian action space.\n\\item \\textit{Oracle-fixed}: a constant step size $\\alpha = 0.005$, also in Cartesian action space.\n\\item \\textit{Oracle-feature}: gradient applied in the VLA's latent feature space rather than directly to Cartesian actions. This variant averages 241.7 refinement steps per episode (vs.\\ ${\\sim}$14 for the Cartesian variants), as the feature-space gradient must propagate through the action decoder.\n\\end{itemize}\nEach variant is evaluated for 160 episodes (4 tasks $\\times$ 40 episodes) with a single seed. The oracle experiments are designed to test Claim~2 (Section~\\ref{sec:ee_only}): if EE-only SDF refinement is structurally sound, oracle performance should exceed unrefined baselines by a wide margin.",
    "structuredPatch": [
      {
        "oldStart": 20,
        "oldLines": 14,
        "newStart": 20,
        "newLines": 17,
        "lines": [
          " \\toprule",
          " Configuration & Description & Trainable Params \\\\",
          " \\midrule",
          "-Pi0 Full-FT & Full fine-tune, flow-matching loss & ${\\sim}$3.5B \\\\",
          "+Pi0 Full-FT & Full fine-tune, flow-matching loss & ${\\sim}$2.5B \\\\",
          " Pi0 LoRA & LoRA adapters only & ${\\sim}$33.5M \\\\",
          "-Pi0+A1 (SDF aux) & LoRA + SDF decoder + EE extractor & ${\\sim}$34.2M \\\\",
          "+Pi0+A1 (SDF aux)\\textsuperscript{$\\dagger$} & LoRA + SDF decoder + EE extractor & ${\\sim}$658K \\\\",
          " Pi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\\sim}$34.2M \\\\",
          "+Pi0.5 (pre-trained) & No fine-tuning & 0 \\\\",
          " Pi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\\sim}$33.5M \\\\",
          " Pi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ & ${\\sim}$34.2M \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          "+\\vspace{2pt}",
          "+\\raggedright\\footnotesize\\textsuperscript{$\\dagger$}LoRA adapter weights were not loaded due to a parameter-name mismatch; only the auxiliary SDF and EE heads were trained.",
          " \\end{table}",
          " ",
          " \\subsection{Standard Metrics}\\label{sec:standard_metrics}"
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

_source line 13_

Now fix the §3.3 mention of Pi0.5 CAR=28.5% (Warning 4 part b) and add the obstacle displacement footnote (Warning 2).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "33c46def-5dc3-4232-baa5-fbda16b4b0b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PLbAuAJLwmFgcCcbrPmaZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1145,
      "cache_read_input_tokens": 27427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1145
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

_source line 14_

<details open><summary>🔧 Tool call — Edit · `toolu_0137Be5BFp6uBVGA7bXM4tUr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex",
  "old_string": "\\paragraph{Diagnostic capability.} CAR$_\\text{f}$ serves two functions. First, it detects fake safety: Pi0+A1 reports CAR\\,=\\,91.5\\% under the standard metric, but CAR$_\\text{f} \\approx 0$\\% because 99.6\\% of its safe episodes are action-collapsed. Second, it validates genuine safety: Pi0.5 achieves CAR$_\\text{f}$ equal to its raw CAR (28.5\\%), with 0\\% of episodes filtered, because all safe episodes involve EE displacement above 288\\,mm.",
  "new_string": "\\paragraph{Diagnostic capability.} CAR$_\\text{f}$ serves two functions. First, it detects fake safety: Pi0+A1 reports CAR\\,=\\,91.5\\% under the standard metric, but CAR$_\\text{f} \\approx 0$\\% because 99.6\\% of its safe episodes are action-collapsed.\\footnote{For Pi0{+}A1, displacement is measured at the obstacle rather than the end-effector, as the original evaluation infrastructure recorded obstacle displacement only. The conclusion is independently corroborated by TSR{=}0\\%, confirming complete action collapse.} Second, it validates genuine safety: the pre-trained Pi0.5 (without fine-tuning) achieves CAR$_\\text{f}$ equal to its raw CAR (28.5\\%), with 0\\% of episodes filtered, because all safe episodes involve EE displacement above 288\\,mm."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "43d178e0-9950-42f5-9cfc-c4c5ce64df0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013PLbAuAJLwmFgcCcbrPmaZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1145,
      "cache_read_input_tokens": 27427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1145
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

_source line 15 · 2026-05-26T16:09:06.212Z_

<details><summary>↩ Tool result · `toolu_0137Be5BFp6uBVGA7bXM4tUr`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "b1d6e57c-9cd8-44fd-af41-47962086ee63",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex",
    "oldString": "\\paragraph{Diagnostic capability.} CAR$_\\text{f}$ serves two functions. First, it detects fake safety: Pi0+A1 reports CAR\\,=\\,91.5\\% under the standard metric, but CAR$_\\text{f} \\approx 0$\\% because 99.6\\% of its safe episodes are action-collapsed. Second, it validates genuine safety: Pi0.5 achieves CAR$_\\text{f}$ equal to its raw CAR (28.5\\%), with 0\\% of episodes filtered, because all safe episodes involve EE displacement above 288\\,mm.",
    "newString": "\\paragraph{Diagnostic capability.} CAR$_\\text{f}$ serves two functions. First, it detects fake safety: Pi0+A1 reports CAR\\,=\\,91.5\\% under the standard metric, but CAR$_\\text{f} \\approx 0$\\% because 99.6\\% of its safe episodes are action-collapsed.\\footnote{For Pi0{+}A1, displacement is measured at the obstacle rather than the end-effector, as the original evaluation infrastructure recorded obstacle displacement only. The conclusion is independently corroborated by TSR{=}0\\%, confirming complete action collapse.} Second, it validates genuine safety: the pre-trained Pi0.5 (without fine-tuning) achieves CAR$_\\text{f}$ equal to its raw CAR (28.5\\%), with 0\\% of episodes filtered, because all safe episodes involve EE displacement above 288\\,mm.",
    "originalFile": "\\section{Experimental Setup and Metrics}\\label{sec:method}\n\nThis section defines the benchmark, models, training procedures, and evaluation metrics that underpin the analyses in Sections~\\ref{sec:fake_safety}--\\ref{sec:avoidance_source}. The central methodological contribution is the displacement-filtered Collision Avoidance Rate (CAR$_\\text{f}$), a corrective metric that separates genuine obstacle avoidance from action collapse (\\S\\ref{sec:dfcar}).\n\n\\subsection{Benchmark and Models}\\label{sec:benchmark}\n\nWe conduct all experiments on SafeLIBERO~\\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\\cite{liu2023libero}. SafeLIBERO augments standard manipulation tasks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety. We select the \\textit{object\\_pudding} suite (Level~I), which comprises four tabletop manipulation tasks: pick \\texttt{orange\\_juice}, \\texttt{chocolate\\_pudding}, \\texttt{milk}, or \\texttt{bbq\\_sauce} and place into a basket. In each task, non-target objects surround the manipulation target, and the MuJoCo physics engine registers any contact between the robot and a non-target object as a collision event.\n\nWe evaluate two Vision-Language-Action (VLA) models from the Pi0 family~\\cite{black2024pi0}. \\textbf{Pi0} (${\\sim}$2.5B parameters) pairs a PaliGemma vision-language encoder with a dedicated action expert that generates continuous actions via flow matching~\\cite{lipman2023flow}. \\textbf{Pi0.5} (from Physical Intelligence) extends this architecture with broader pre-training data and serves as a stronger baseline with substantially higher task capability and less susceptibility to action collapse.\n\nTable~\\ref{tab:configurations} summarizes the six training configurations. Each model is trained for 30K steps. Evaluation uses 50 episodes per task across 4 tasks (200 episodes per configuration). For multi-seed experiments on Pi0.5, we run 3 seeds (600 episodes per configuration). Initial object placements are fixed across methods to ensure fair comparison.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training configurations. Trainable parameter counts exclude the frozen backbone. The SDF auxiliary heads add $<$660K parameters to the ${\\sim}$33.5M LoRA budget.}\n\\label{tab:configurations}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nConfiguration & Description & Trainable Params \\\\\n\\midrule\nPi0 Full-FT & Full fine-tune, flow-matching loss & ${\\sim}$2.5B \\\\\nPi0 LoRA & LoRA adapters only & ${\\sim}$33.5M \\\\\nPi0+A1 (SDF aux)\\textsuperscript{$\\dagger$} & LoRA + SDF decoder + EE extractor & ${\\sim}$658K \\\\\nPi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\\sim}$34.2M \\\\\nPi0.5 (pre-trained) & No fine-tuning & 0 \\\\\nPi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\\sim}$33.5M \\\\\nPi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ & ${\\sim}$34.2M \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n\\raggedright\\footnotesize\\textsuperscript{$\\dagger$}LoRA adapter weights were not loaded due to a parameter-name mismatch; only the auxiliary SDF and EE heads were trained.\n\\end{table}\n\n\\subsection{Standard Metrics}\\label{sec:standard_metrics}\n\nWe report two conventional metrics. The \\emph{Collision Avoidance Rate} (CAR) is the fraction of episodes in which no collision occurs between the robot and any non-target object:\n\\begin{equation}\\label{eq:car}\n\\text{CAR} = \\frac{|\\{e : \\text{safe}(e)\\}|}{|E|}\n\\end{equation}\nwhere $E$ is the set of all evaluation episodes and $\\text{safe}(e)$ indicates that episode $e$ contains zero collision events. The \\emph{Task Success Rate} (TSR) is the fraction of episodes where the manipulation task reaches completion:\n\\begin{equation}\\label{eq:tsr}\n\\text{TSR} = \\frac{|\\{e : \\text{success}(e)\\}|}{|E|}\n\\end{equation}\nThese two metrics are standard in the SafeLIBERO evaluation protocol and in the broader VLA safety literature~\\cite{hu2025vlsa,zhang2025safevla}.\n\n\\subsection{Displacement-Filtered CAR}\\label{sec:dfcar}\n\nStandard CAR conflates two qualitatively distinct behaviors: a robot that plans a trajectory around obstacles, and a robot that has collapsed into inaction. Both register as ``safe,'' yet only the former reflects collision avoidance capability. We introduce CAR$_\\text{f}$, which excludes action-collapsed episodes from both numerator and denominator.\n\n\\paragraph{Action collapse.} We define an episode $e$ as \\emph{action-collapsed} when its maximum end-effector (EE) displacement satisfies\n\\begin{equation}\nd_{\\max}(e) < \\tau_d\n\\end{equation}\nwhere $d_{\\max}(e) = \\max_{t} \\| \\mathbf{p}_t - \\mathbf{p}_0 \\|_2$ is the maximum Euclidean displacement of the EE from its initial position across all timesteps, and $\\tau_d$ is a displacement threshold. We set $\\tau_d = 0.1$\\,mm, corresponding to sub-actuator-resolution motion.\n\n\\paragraph{Definition.} The displacement-filtered CAR is:\n\\begin{equation}\\label{eq:car_f}\n\\text{CAR}_\\text{f} = \\frac{|\\{e : \\text{safe}(e) \\;\\land\\; d_{\\max}(e) \\geq \\tau_d\\}|}{|\\{e : d_{\\max}(e) \\geq \\tau_d\\}|}\n\\end{equation}\nCAR$_\\text{f}$ retains only episodes with sufficient EE motion and measures the collision avoidance rate exclusively among them.\n\n\\paragraph{Threshold robustness.} The specific choice of $\\tau_d$ is not critical. The displacement distribution across all evaluated models is sharply bimodal: collapsed episodes cluster below 1\\,$\\mu$m, while active episodes exceed 200\\,mm. No episodes fall in the intermediate range. This five-order-of-magnitude gap means that any $\\tau_d \\in [2, 200]$\\,mm produces identical filtering results. We verify this empirically in Appendix~\\ref{sec:appendix_threshold}.\n\n\\paragraph{Diagnostic capability.} CAR$_\\text{f}$ serves two functions. First, it detects fake safety: Pi0+A1 reports CAR\\,=\\,91.5\\% under the standard metric, but CAR$_\\text{f} \\approx 0$\\% because 99.6\\% of its safe episodes are action-collapsed. Second, it validates genuine safety: Pi0.5 achieves CAR$_\\text{f}$ equal to its raw CAR (28.5\\%), with 0\\% of episodes filtered, because all safe episodes involve EE displacement above 288\\,mm.\n\n\\subsection{SDF Auxiliary Training}\\label{sec:sdf_aux}\n\nWe augment the LoRA-adapted VLA with two lightweight auxiliary heads that provide geometric supervision during training.\n\n\\paragraph{SDF Decoder ($f_\\text{SDF}$).} A 4-layer MLP (hidden dimension 256, Softplus activation with $\\beta = 5$, ${\\sim}$395K parameters) predicts the signed distance $\\Phi(\\mathbf{x})$ from the current EE position $\\mathbf{x}$ to the nearest obstacle surface. The decoder reads from intermediate features of the VLA action expert. The ground-truth signed distance field is precomputed from obstacle meshes using trimesh/pysdf, with values clamped at $\\delta = 0.05$\\,m and a safety margin $m = 0.01$\\,m applied to shift the zero-crossing outward from the obstacle surface.\n\n\\paragraph{EE Extractor ($f_\\text{EE}$).} A 2-layer MLP ($1024 \\to 256 \\to 3$, ${\\sim}$263K parameters) predicts the 3D EE position from the same action expert features. This auxiliary head provides the query point for the SDF decoder and serves as an implicit regularizer on the learned feature representation.\n\n\\paragraph{Training objective.} The total loss combines the standard flow-matching action loss with the two auxiliary losses:\n\\begin{equation}\\label{eq:total_loss}\n\\mathcal{L}_\\text{total} = \\mathcal{L}_\\text{action} + \\lambda \\left( \\mathcal{L}_\\text{SDF} + \\mathcal{L}_\\text{EE} \\right)\n\\end{equation}\nwhere $\\mathcal{L}_\\text{SDF}$ is a clamped $L_1$ loss on predicted SDF values with an Eikonal regularizer, $\\mathcal{L}_\\text{EE}$ is MSE on predicted EE position, and $\\lambda$ controls the auxiliary loss weight. We evaluate $\\lambda \\in \\{0.005, 0.01, 0.1\\}$. The total auxiliary overhead is $<$660K parameters, less than 2\\% of the ${\\sim}$33.5M LoRA parameter budget.\n\n\\paragraph{Optimization.} All models are trained with AdamW, a cosine learning rate schedule decaying from $2.5 \\times 10^{-5}$ to $2.5 \\times 10^{-6}$, for 30K steps with batch size 32. For Pi0.5+A1, training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization.\n\n\\subsection{Oracle SDF Refinement}\\label{sec:oracle_setup}\n\nTo test the theoretical upper bound of EE-only SDF refinement (Section~\\ref{sec:ee_only}), we replace the learned SDF network with the ground-truth signed distance field computed from the simulation geometry. This eliminates prediction error and isolates the structural limitation of the refinement paradigm.\n\nWe evaluate three oracle variants:\n\\begin{itemize}\n\\item \\textit{Oracle-adaptive}: runtime gradient refinement with a dynamic step size $\\alpha$ that scales inversely with gradient magnitude, applied in Cartesian action space.\n\\item \\textit{Oracle-fixed}: a constant step size $\\alpha = 0.005$, also in Cartesian action space.\n\\item \\textit{Oracle-feature}: gradient applied in the VLA's latent feature space rather than directly to Cartesian actions. This variant averages 241.7 refinement steps per episode (vs.\\ ${\\sim}$14 for the Cartesian variants), as the feature-space gradient must propagate through the action decoder.\n\\end{itemize}\nEach variant is evaluated for 160 episodes (4 tasks $\\times$ 40 episodes) with a single seed. The oracle experiments are designed to test Claim~2 (Section~\\ref{sec:ee_only}): if EE-only SDF refinement is structurally sound, oracle performance should exceed unrefined baselines by a wide margin.",
    "structuredPatch": [
      {
        "oldStart": 63,
        "oldLines": 7,
        "newStart": 63,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Threshold robustness.} The specific choice of $\\tau_d$ is not critical. The displacement distribution across all evaluated models is sharply bimodal: collapsed episodes cluster below 1\\,$\\mu$m, while active episodes exceed 200\\,mm. No episodes fall in the intermediate range. This five-order-of-magnitude gap means that any $\\tau_d \\in [2, 200]$\\,mm produces identical filtering results. We verify this empirically in Appendix~\\ref{sec:appendix_threshold}.",
          " ",
          "-\\paragraph{Diagnostic capability.} CAR$_\\text{f}$ serves two functions. First, it detects fake safety: Pi0+A1 reports CAR\\,=\\,91.5\\% under the standard metric, but CAR$_\\text{f} \\approx 0$\\% because 99.6\\% of its safe episodes are action-collapsed. Second, it validates genuine safety: Pi0.5 achieves CAR$_\\text{f}$ equal to its raw CAR (28.5\\%), with 0\\% of episodes filtered, because all safe episodes involve EE displacement above 288\\,mm.",
          "+\\paragraph{Diagnostic capability.} CAR$_\\text{f}$ serves two functions. First, it detects fake safety: Pi0+A1 reports CAR\\,=\\,91.5\\% under the standard metric, but CAR$_\\text{f} \\approx 0$\\% because 99.6\\% of its safe episodes are action-collapsed.\\footnote{For Pi0{+}A1, displacement is measured at the obstacle rather than the end-effector, as the original evaluation infrastructure recorded obstacle displacement only. The conclusion is independently corroborated by TSR{=}0\\%, confirming complete action collapse.} Second, it validates genuine safety: the pre-trained Pi0.5 (without fine-tuning) achieves CAR$_\\text{f}$ equal to its raw CAR (28.5\\%), with 0\\% of episodes filtered, because all safe episodes involve EE displacement above 288\\,mm.",
          " ",
          " \\subsection{SDF Auxiliary Training}\\label{sec:sdf_aux}",
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

_source line 16_

Now add the LoRA mismatch disclosure in §3.4 (SDF Auxiliary Training section), since that's where Pi0+A1 is configured. I'll add it right after the optimization paragraph.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "958da04f-240c-45b0-b6e1-9a8d8369b82a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E6jVMrPukq5uSpvBmD3g6W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 28572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 605
      },
      "output_tokens": 2,
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

<details open><summary>🔧 Tool call — Edit · `toolu_01MRAkTk59Mht5BTQ2gWcf7w`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex",
  "old_string": "\\paragraph{Optimization.} All models are trained with AdamW, a cosine learning rate schedule decaying from $2.5 \\times 10^{-5}$ to $2.5 \\times 10^{-6}$, for 30K steps with batch size 32. For Pi0.5+A1, training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization.\n\n\\subsection{Oracle SDF Refinement}",
  "new_string": "\\paragraph{Optimization.} All models are trained with AdamW, a cosine learning rate schedule decaying from $2.5 \\times 10^{-5}$ to $2.5 \\times 10^{-6}$, for 30K steps with batch size 32. For Pi0.5+A1, training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization.\n\n\\paragraph{Pi0+A1 configuration note.} In the Pi0+A1 configuration, a parameter-name mismatch prevented the LoRA adapter weights from being loaded, so only the auxiliary SDF decoder and EE extractor heads were trained (${\\sim}$658K parameters), while the backbone remained entirely frozen. This caused complete action collapse (TSR\\,=\\,0\\%), as the frozen backbone could not adapt to the downstream tasks. The resulting failure mode reinforces the diagnostic value of CAR$_\\text{f}$: standard CAR reports 91.5\\% for Pi0+A1, but CAR$_\\text{f} \\approx 0$\\% correctly identifies these episodes as fake safety from a frozen robot rather than genuine collision avoidance.\n\n\\subsection{Oracle SDF Refinement}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "8daf4a44-13df-4624-a2f3-7282ea0ae22d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E6jVMrPukq5uSpvBmD3g6W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 605,
      "cache_read_input_tokens": 28572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 605
      },
      "output_tokens": 2,
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

_source line 18 · 2026-05-26T16:09:18.263Z_

<details><summary>↩ Tool result · `toolu_01MRAkTk59Mht5BTQ2gWcf7w`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "18b86f13-b0c3-4efb-8a17-13d22a6287de",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex",
    "oldString": "\\paragraph{Optimization.} All models are trained with AdamW, a cosine learning rate schedule decaying from $2.5 \\times 10^{-5}$ to $2.5 \\times 10^{-6}$, for 30K steps with batch size 32. For Pi0.5+A1, training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization.\n\n\\subsection{Oracle SDF Refinement}",
    "newString": "\\paragraph{Optimization.} All models are trained with AdamW, a cosine learning rate schedule decaying from $2.5 \\times 10^{-5}$ to $2.5 \\times 10^{-6}$, for 30K steps with batch size 32. For Pi0.5+A1, training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization.\n\n\\paragraph{Pi0+A1 configuration note.} In the Pi0+A1 configuration, a parameter-name mismatch prevented the LoRA adapter weights from being loaded, so only the auxiliary SDF decoder and EE extractor heads were trained (${\\sim}$658K parameters), while the backbone remained entirely frozen. This caused complete action collapse (TSR\\,=\\,0\\%), as the frozen backbone could not adapt to the downstream tasks. The resulting failure mode reinforces the diagnostic value of CAR$_\\text{f}$: standard CAR reports 91.5\\% for Pi0+A1, but CAR$_\\text{f} \\approx 0$\\% correctly identifies these episodes as fake safety from a frozen robot rather than genuine collision avoidance.\n\n\\subsection{Oracle SDF Refinement}",
    "originalFile": "\\section{Experimental Setup and Metrics}\\label{sec:method}\n\nThis section defines the benchmark, models, training procedures, and evaluation metrics that underpin the analyses in Sections~\\ref{sec:fake_safety}--\\ref{sec:avoidance_source}. The central methodological contribution is the displacement-filtered Collision Avoidance Rate (CAR$_\\text{f}$), a corrective metric that separates genuine obstacle avoidance from action collapse (\\S\\ref{sec:dfcar}).\n\n\\subsection{Benchmark and Models}\\label{sec:benchmark}\n\nWe conduct all experiments on SafeLIBERO~\\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\\cite{liu2023libero}. SafeLIBERO augments standard manipulation tasks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety. We select the \\textit{object\\_pudding} suite (Level~I), which comprises four tabletop manipulation tasks: pick \\texttt{orange\\_juice}, \\texttt{chocolate\\_pudding}, \\texttt{milk}, or \\texttt{bbq\\_sauce} and place into a basket. In each task, non-target objects surround the manipulation target, and the MuJoCo physics engine registers any contact between the robot and a non-target object as a collision event.\n\nWe evaluate two Vision-Language-Action (VLA) models from the Pi0 family~\\cite{black2024pi0}. \\textbf{Pi0} (${\\sim}$2.5B parameters) pairs a PaliGemma vision-language encoder with a dedicated action expert that generates continuous actions via flow matching~\\cite{lipman2023flow}. \\textbf{Pi0.5} (from Physical Intelligence) extends this architecture with broader pre-training data and serves as a stronger baseline with substantially higher task capability and less susceptibility to action collapse.\n\nTable~\\ref{tab:configurations} summarizes the six training configurations. Each model is trained for 30K steps. Evaluation uses 50 episodes per task across 4 tasks (200 episodes per configuration). For multi-seed experiments on Pi0.5, we run 3 seeds (600 episodes per configuration). Initial object placements are fixed across methods to ensure fair comparison.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training configurations. Trainable parameter counts exclude the frozen backbone. The SDF auxiliary heads add $<$660K parameters to the ${\\sim}$33.5M LoRA budget.}\n\\label{tab:configurations}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nConfiguration & Description & Trainable Params \\\\\n\\midrule\nPi0 Full-FT & Full fine-tune, flow-matching loss & ${\\sim}$2.5B \\\\\nPi0 LoRA & LoRA adapters only & ${\\sim}$33.5M \\\\\nPi0+A1 (SDF aux)\\textsuperscript{$\\dagger$} & LoRA + SDF decoder + EE extractor & ${\\sim}$658K \\\\\nPi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\\sim}$34.2M \\\\\nPi0.5 (pre-trained) & No fine-tuning & 0 \\\\\nPi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\\sim}$33.5M \\\\\nPi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ & ${\\sim}$34.2M \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n\\raggedright\\footnotesize\\textsuperscript{$\\dagger$}LoRA adapter weights were not loaded due to a parameter-name mismatch; only the auxiliary SDF and EE heads were trained.\n\\end{table}\n\n\\subsection{Standard Metrics}\\label{sec:standard_metrics}\n\nWe report two conventional metrics. The \\emph{Collision Avoidance Rate} (CAR) is the fraction of episodes in which no collision occurs between the robot and any non-target object:\n\\begin{equation}\\label{eq:car}\n\\text{CAR} = \\frac{|\\{e : \\text{safe}(e)\\}|}{|E|}\n\\end{equation}\nwhere $E$ is the set of all evaluation episodes and $\\text{safe}(e)$ indicates that episode $e$ contains zero collision events. The \\emph{Task Success Rate} (TSR) is the fraction of episodes where the manipulation task reaches completion:\n\\begin{equation}\\label{eq:tsr}\n\\text{TSR} = \\frac{|\\{e : \\text{success}(e)\\}|}{|E|}\n\\end{equation}\nThese two metrics are standard in the SafeLIBERO evaluation protocol and in the broader VLA safety literature~\\cite{hu2025vlsa,zhang2025safevla}.\n\n\\subsection{Displacement-Filtered CAR}\\label{sec:dfcar}\n\nStandard CAR conflates two qualitatively distinct behaviors: a robot that plans a trajectory around obstacles, and a robot that has collapsed into inaction. Both register as ``safe,'' yet only the former reflects collision avoidance capability. We introduce CAR$_\\text{f}$, which excludes action-collapsed episodes from both numerator and denominator.\n\n\\paragraph{Action collapse.} We define an episode $e$ as \\emph{action-collapsed} when its maximum end-effector (EE) displacement satisfies\n\\begin{equation}\nd_{\\max}(e) < \\tau_d\n\\end{equation}\nwhere $d_{\\max}(e) = \\max_{t} \\| \\mathbf{p}_t - \\mathbf{p}_0 \\|_2$ is the maximum Euclidean displacement of the EE from its initial position across all timesteps, and $\\tau_d$ is a displacement threshold. We set $\\tau_d = 0.1$\\,mm, corresponding to sub-actuator-resolution motion.\n\n\\paragraph{Definition.} The displacement-filtered CAR is:\n\\begin{equation}\\label{eq:car_f}\n\\text{CAR}_\\text{f} = \\frac{|\\{e : \\text{safe}(e) \\;\\land\\; d_{\\max}(e) \\geq \\tau_d\\}|}{|\\{e : d_{\\max}(e) \\geq \\tau_d\\}|}\n\\end{equation}\nCAR$_\\text{f}$ retains only episodes with sufficient EE motion and measures the collision avoidance rate exclusively among them.\n\n\\paragraph{Threshold robustness.} The specific choice of $\\tau_d$ is not critical. The displacement distribution across all evaluated models is sharply bimodal: collapsed episodes cluster below 1\\,$\\mu$m, while active episodes exceed 200\\,mm. No episodes fall in the intermediate range. This five-order-of-magnitude gap means that any $\\tau_d \\in [2, 200]$\\,mm produces identical filtering results. We verify this empirically in Appendix~\\ref{sec:appendix_threshold}.\n\n\\paragraph{Diagnostic capability.} CAR$_\\text{f}$ serves two functions. First, it detects fake safety: Pi0+A1 reports CAR\\,=\\,91.5\\% under the standard metric, but CAR$_\\text{f} \\approx 0$\\% because 99.6\\% of its safe episodes are action-collapsed.\\footnote{For Pi0{+}A1, displacement is measured at the obstacle rather than the end-effector, as the original evaluation infrastructure recorded obstacle displacement only. The conclusion is independently corroborated by TSR{=}0\\%, confirming complete action collapse.} Second, it validates genuine safety: the pre-trained Pi0.5 (without fine-tuning) achieves CAR$_\\text{f}$ equal to its raw CAR (28.5\\%), with 0\\% of episodes filtered, because all safe episodes involve EE displacement above 288\\,mm.\n\n\\subsection{SDF Auxiliary Training}\\label{sec:sdf_aux}\n\nWe augment the LoRA-adapted VLA with two lightweight auxiliary heads that provide geometric supervision during training.\n\n\\paragraph{SDF Decoder ($f_\\text{SDF}$).} A 4-layer MLP (hidden dimension 256, Softplus activation with $\\beta = 5$, ${\\sim}$395K parameters) predicts the signed distance $\\Phi(\\mathbf{x})$ from the current EE position $\\mathbf{x}$ to the nearest obstacle surface. The decoder reads from intermediate features of the VLA action expert. The ground-truth signed distance field is precomputed from obstacle meshes using trimesh/pysdf, with values clamped at $\\delta = 0.05$\\,m and a safety margin $m = 0.01$\\,m applied to shift the zero-crossing outward from the obstacle surface.\n\n\\paragraph{EE Extractor ($f_\\text{EE}$).} A 2-layer MLP ($1024 \\to 256 \\to 3$, ${\\sim}$263K parameters) predicts the 3D EE position from the same action expert features. This auxiliary head provides the query point for the SDF decoder and serves as an implicit regularizer on the learned feature representation.\n\n\\paragraph{Training objective.} The total loss combines the standard flow-matching action loss with the two auxiliary losses:\n\\begin{equation}\\label{eq:total_loss}\n\\mathcal{L}_\\text{total} = \\mathcal{L}_\\text{action} + \\lambda \\left( \\mathcal{L}_\\text{SDF} + \\mathcal{L}_\\text{EE} \\right)\n\\end{equation}\nwhere $\\mathcal{L}_\\text{SDF}$ is a clamped $L_1$ loss on predicted SDF values with an Eikonal regularizer, $\\mathcal{L}_\\text{EE}$ is MSE on predicted EE position, and $\\lambda$ controls the auxiliary loss weight. We evaluate $\\lambda \\in \\{0.005, 0.01, 0.1\\}$. The total auxiliary overhead is $<$660K parameters, less than 2\\% of the ${\\sim}$33.5M LoRA parameter budget.\n\n\\paragraph{Optimization.} All models are trained with AdamW, a cosine learning rate schedule decaying from $2.5 \\times 10^{-5}$ to $2.5 \\times 10^{-6}$, for 30K steps with batch size 32. For Pi0.5+A1, training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization.\n\n\\subsection{Oracle SDF Refinement}\\label{sec:oracle_setup}\n\nTo test the theoretical upper bound of EE-only SDF refinement (Section~\\ref{sec:ee_only}), we replace the learned SDF network with the ground-truth signed distance field computed from the simulation geometry. This eliminates prediction error and isolates the structural limitation of the refinement paradigm.\n\nWe evaluate three oracle variants:\n\\begin{itemize}\n\\item \\textit{Oracle-adaptive}: runtime gradient refinement with a dynamic step size $\\alpha$ that scales inversely with gradient magnitude, applied in Cartesian action space.\n\\item \\textit{Oracle-fixed}: a constant step size $\\alpha = 0.005$, also in Cartesian action space.\n\\item \\textit{Oracle-feature}: gradient applied in the VLA's latent feature space rather than directly to Cartesian actions. This variant averages 241.7 refinement steps per episode (vs.\\ ${\\sim}$14 for the Cartesian variants), as the feature-space gradient must propagate through the action decoder.\n\\end{itemize}\nEach variant is evaluated for 160 episodes (4 tasks $\\times$ 40 episodes) with a single seed. The oracle experiments are designed to test Claim~2 (Section~\\ref{sec:ee_only}): if EE-only SDF refinement is structurally sound, oracle performance should exceed unrefined baselines by a wide margin.",
    "structuredPatch": [
      {
        "oldStart": 81,
        "oldLines": 6,
        "newStart": 81,
        "newLines": 8,
        "lines": [
          " ",
          " \\paragraph{Optimization.} All models are trained with AdamW, a cosine learning rate schedule decaying from $2.5 \\times 10^{-5}$ to $2.5 \\times 10^{-6}$, for 30K steps with batch size 32. For Pi0.5+A1, training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization.",
          " ",
          "+\\paragraph{Pi0+A1 configuration note.} In the Pi0+A1 configuration, a parameter-name mismatch prevented the LoRA adapter weights from being loaded, so only the auxiliary SDF decoder and EE extractor heads were trained (${\\sim}$658K parameters), while the backbone remained entirely frozen. This caused complete action collapse (TSR\\,=\\,0\\%), as the frozen backbone could not adapt to the downstream tasks. The resulting failure mode reinforces the diagnostic value of CAR$_\\text{f}$: standard CAR reports 91.5\\% for Pi0+A1, but CAR$_\\text{f} \\approx 0$\\% correctly identifies these episodes as fake safety from a frozen robot rather than genuine collision avoidance.",
          "+",
          " \\subsection{Oracle SDF Refinement}\\label{sec:oracle_setup}",
          " ",
          " To test the theoretical upper bound of EE-only SDF refinement (Section~\\ref{sec:ee_only}), we replace the learned SDF network with the ground-truth signed distance field computed from the simulation geometry. This eliminates prediction error and isolates the structural limitation of the refinement paradigm."
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

_source line 19_

Now let me verify the final file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "0f43499e-68f4-4951-948f-2216b2ba2519",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYUo3FW8sgZSpHXBBqFzEm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 813,
      "cache_read_input_tokens": 29177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 813
      },
      "output_tokens": 6,
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

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_017XLfzBe6b8JpgVsaW9g5Vw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "87df9408-430e-43b6-978f-0a663f2772b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYUo3FW8sgZSpHXBBqFzEm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 813,
      "cache_read_input_tokens": 29177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 813
      },
      "output_tokens": 6,
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

_source line 21 · 2026-05-26T16:09:20.614Z_

<details><summary>↩ Tool result · `toolu_017XLfzBe6b8JpgVsaW9g5Vw`</summary>

```text
1	\section{Experimental Setup and Metrics}\label{sec:method}
2	
3	This section defines the benchmark, models, training procedures, and evaluation metrics that underpin the analyses in Sections~\ref{sec:fake_safety}--\ref{sec:avoidance_source}. The central methodological contribution is the displacement-filtered Collision Avoidance Rate (CAR$_\text{f}$), a corrective metric that separates genuine obstacle avoidance from action collapse (\S\ref{sec:dfcar}).
4	
5	\subsection{Benchmark and Models}\label{sec:benchmark}
6	
7	We conduct all experiments on SafeLIBERO~\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\cite{liu2023libero}. SafeLIBERO augments standard manipulation tasks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety. We select the \textit{object\_pudding} suite (Level~I), which comprises four tabletop manipulation tasks: pick \texttt{orange\_juice}, \texttt{chocolate\_pudding}, \texttt{milk}, or \texttt{bbq\_sauce} and place into a basket. In each task, non-target objects surround the manipulation target, and the MuJoCo physics engine registers any contact between the robot and a non-target object as a collision event.
8	
9	We evaluate two Vision-Language-Action (VLA) models from the Pi0 family~\cite{black2024pi0}. \textbf{Pi0} (${\sim}$2.5B parameters) pairs a PaliGemma vision-language encoder with a dedicated action expert that generates continuous actions via flow matching~\cite{lipman2023flow}. \textbf{Pi0.5} (from Physical Intelligence) extends this architecture with broader pre-training data and serves as a stronger baseline with substantially higher task capability and less susceptibility to action collapse.
10	
11	Table~\ref{tab:configurations} summarizes the six training configurations. Each model is trained for 30K steps. Evaluation uses 50 episodes per task across 4 tasks (200 episodes per configuration). For multi-seed experiments on Pi0.5, we run 3 seeds (600 episodes per configuration). Initial object placements are fixed across methods to ensure fair comparison.
12	
13	\begin{table}[t]
14	\centering
15	\caption{Training configurations. Trainable parameter counts exclude the frozen backbone. The SDF auxiliary heads add $<$660K parameters to the ${\sim}$33.5M LoRA budget.}
16	\label{tab:configurations}
17	\vspace{2pt}
18	\small
19	\begin{tabular}{llr}
20	\toprule
21	Configuration & Description & Trainable Params \\
22	\midrule
23	Pi0 Full-FT & Full fine-tune, flow-matching loss & ${\sim}$2.5B \\
24	Pi0 LoRA & LoRA adapters only & ${\sim}$33.5M \\
25	Pi0+A1 (SDF aux)\textsuperscript{$\dagger$} & LoRA + SDF decoder + EE extractor & ${\sim}$658K \\
26	Pi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\sim}$34.2M \\
27	Pi0.5 (pre-trained) & No fine-tuning & 0 \\
28	Pi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\sim}$33.5M \\
29	Pi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\lambda \in \{0.005, 0.01, 0.1\}$ & ${\sim}$34.2M \\
30	\bottomrule
31	\end{tabular}
32	\vspace{2pt}
33	\raggedright\footnotesize\textsuperscript{$\dagger$}LoRA adapter weights were not loaded due to a parameter-name mismatch; only the auxiliary SDF and EE heads were trained.
34	\end{table}
35	
36	\subsection{Standard Metrics}\label{sec:standard_metrics}
37	
38	We report two conventional metrics. The \emph{Collision Avoidance Rate} (CAR) is the fraction of episodes in which no collision occurs between the robot and any non-target object:
39	\begin{equation}\label{eq:car}
40	\text{CAR} = \frac{|\{e : \text{safe}(e)\}|}{|E|}
41	\end{equation}
42	where $E$ is the set of all evaluation episodes and $\text{safe}(e)$ indicates that episode $e$ contains zero collision events. The \emph{Task Success Rate} (TSR) is the fraction of episodes where the manipulation task reaches completion:
43	\begin{equation}\label{eq:tsr}
44	\text{TSR} = \frac{|\{e : \text{success}(e)\}|}{|E|}
45	\end{equation}
46	These two metrics are standard in the SafeLIBERO evaluation protocol and in the broader VLA safety literature~\cite{hu2025vlsa,zhang2025safevla}.
47	
48	\subsection{Displacement-Filtered CAR}\label{sec:dfcar}
49	
50	Standard CAR conflates two qualitatively distinct behaviors: a robot that plans a trajectory around obstacles, and a robot that has collapsed into inaction. Both register as ``safe,'' yet only the former reflects collision avoidance capability. We introduce CAR$_\text{f}$, which excludes action-collapsed episodes from both numerator and denominator.
51	
52	\paragraph{Action collapse.} We define an episode $e$ as \emph{action-collapsed} when its maximum end-effector (EE) displacement satisfies
53	\begin{equation}
54	d_{\max}(e) < \tau_d
55	\end{equation}
56	where $d_{\max}(e) = \max_{t} \| \mathbf{p}_t - \mathbf{p}_0 \|_2$ is the maximum Euclidean displacement of the EE from its initial position across all timesteps, and $\tau_d$ is a displacement threshold. We set $\tau_d = 0.1$\,mm, corresponding to sub-actuator-resolution motion.
57	
58	\paragraph{Definition.} The displacement-filtered CAR is:
59	\begin{equation}\label{eq:car_f}
60	\text{CAR}_\text{f} = \frac{|\{e : \text{safe}(e) \;\land\; d_{\max}(e) \geq \tau_d\}|}{|\{e : d_{\max}(e) \geq \tau_d\}|}
61	\end{equation}
62	CAR$_\text{f}$ retains only episodes with sufficient EE motion and measures the collision avoidance rate exclusively among them.
63	
64	\paragraph{Threshold robustness.} The specific choice of $\tau_d$ is not critical. The displacement distribution across all evaluated models is sharply bimodal: collapsed episodes cluster below 1\,$\mu$m, while active episodes exceed 200\,mm. No episodes fall in the intermediate range. This five-order-of-magnitude gap means that any $\tau_d \in [2, 200]$\,mm produces identical filtering results. We verify this empirically in Appendix~\ref{sec:appendix_threshold}.
65	
66	\paragraph{Diagnostic capability.} CAR$_\text{f}$ serves two functions. First, it detects fake safety: Pi0+A1 reports CAR\,=\,91.5\% under the standard metric, but CAR$_\text{f} \approx 0$\% because 99.6\% of its safe episodes are action-collapsed.\footnote{For Pi0{+}A1, displacement is measured at the obstacle rather than the end-effector, as the original evaluation infrastructure recorded obstacle displacement only. The conclusion is independently corroborated by TSR{=}0\%, confirming complete action collapse.} Second, it validates genuine safety: the pre-trained Pi0.5 (without fine-tuning) achieves CAR$_\text{f}$ equal to its raw CAR (28.5\%), with 0\% of episodes filtered, because all safe episodes involve EE displacement above 288\,mm.
67	
68	\subsection{SDF Auxiliary Training}\label{sec:sdf_aux}
69	
70	We augment the LoRA-adapted VLA with two lightweight auxiliary heads that provide geometric supervision during training.
71	
72	\paragraph{SDF Decoder ($f_\text{SDF}$).} A 4-layer MLP (hidden dimension 256, Softplus activation with $\beta = 5$, ${\sim}$395K parameters) predicts the signed distance $\Phi(\mathbf{x})$ from the current EE position $\mathbf{x}$ to the nearest obstacle surface. The decoder reads from intermediate features of the VLA action expert. The ground-truth signed distance field is precomputed from obstacle meshes using trimesh/pysdf, with values clamped at $\delta = 0.05$\,m and a safety margin $m = 0.01$\,m applied to shift the zero-crossing outward from the obstacle surface.
73	
74	\paragraph{EE Extractor ($f_\text{EE}$).} A 2-layer MLP ($1024 \to 256 \to 3$, ${\sim}$263K parameters) predicts the 3D EE position from the same action expert features. This auxiliary head provides the query point for the SDF decoder and serves as an implicit regularizer on the learned feature representation.
75	
76	\paragraph{Training objective.} The total loss combines the standard flow-matching action loss with the two auxiliary losses:
77	\begin{equation}\label{eq:total_loss}
78	\mathcal{L}_\text{total} = \mathcal{L}_\text{action} + \lambda \left( \mathcal{L}_\text{SDF} + \mathcal{L}_\text{EE} \right)
79	\end{equation}
80	where $\mathcal{L}_\text{SDF}$ is a clamped $L_1$ loss on predicted SDF values with an Eikonal regularizer, $\mathcal{L}_\text{EE}$ is MSE on predicted EE position, and $\lambda$ controls the auxiliary loss weight. We evaluate $\lambda \in \{0.005, 0.01, 0.1\}$. The total auxiliary overhead is $<$660K parameters, less than 2\% of the ${\sim}$33.5M LoRA parameter budget.
81	
82	\paragraph{Optimization.} All models are trained with AdamW, a cosine learning rate schedule decaying from $2.5 \times 10^{-5}$ to $2.5 \times 10^{-6}$, for 30K steps with batch size 32. For Pi0.5+A1, training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization.
83	
84	\paragraph{Pi0+A1 configuration note.} In the Pi0+A1 configuration, a parameter-name mismatch prevented the LoRA adapter weights from being loaded, so only the auxiliary SDF decoder and EE extractor heads were trained (${\sim}$658K parameters), while the backbone remained entirely frozen. This caused complete action collapse (TSR\,=\,0\%), as the frozen backbone could not adapt to the downstream tasks. The resulting failure mode reinforces the diagnostic value of CAR$_\text{f}$: standard CAR reports 91.5\% for Pi0+A1, but CAR$_\text{f} \approx 0$\% correctly identifies these episodes as fake safety from a frozen robot rather than genuine collision avoidance.
85	
86	\subsection{Oracle SDF Refinement}\label{sec:oracle_setup}
87	
88	To test the theoretical upper bound of EE-only SDF refinement (Section~\ref{sec:ee_only}), we replace the learned SDF network with the ground-truth signed distance field computed from the simulation geometry. This eliminates prediction error and isolates the structural limitation of the refinement paradigm.
89	
90	We evaluate three oracle variants:
91	\begin{itemize}
92	\item \textit{Oracle-adaptive}: runtime gradient refinement with a dynamic step size $\alpha$ that scales inversely with gradient magnitude, applied in Cartesian action space.
93	\item \textit{Oracle-fixed}: a constant step size $\alpha = 0.005$, also in Cartesian action space.
94	\item \textit{Oracle-feature}: gradient applied in the VLA's latent feature space rather than directly to Cartesian actions. This variant averages 241.7 refinement steps per episode (vs.\ ${\sim}$14 for the Cartesian variants), as the feature-space gradient must propagate through the action decoder.
95	\end{itemize}
96	Each variant is evaluated for 160 episodes (4 tasks $\times$ 40 episodes) with a single seed. The oracle experiments are designed to test Claim~2 (Section~\ref{sec:ee_only}): if EE-only SDF refinement is structurally sound, oracle performance should exceed unrefined baselines by a wide margin.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "311d791c-89a1-4658-b7ee-ca0f8fbe01d3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex",
      "content": "\\section{Experimental Setup and Metrics}\\label{sec:method}\n\nThis section defines the benchmark, models, training procedures, and evaluation metrics that underpin the analyses in Sections~\\ref{sec:fake_safety}--\\ref{sec:avoidance_source}. The central methodological contribution is the displacement-filtered Collision Avoidance Rate (CAR$_\\text{f}$), a corrective metric that separates genuine obstacle avoidance from action collapse (\\S\\ref{sec:dfcar}).\n\n\\subsection{Benchmark and Models}\\label{sec:benchmark}\n\nWe conduct all experiments on SafeLIBERO~\\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\\cite{liu2023libero}. SafeLIBERO augments standard manipulation tasks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety. We select the \\textit{object\\_pudding} suite (Level~I), which comprises four tabletop manipulation tasks: pick \\texttt{orange\\_juice}, \\texttt{chocolate\\_pudding}, \\texttt{milk}, or \\texttt{bbq\\_sauce} and place into a basket. In each task, non-target objects surround the manipulation target, and the MuJoCo physics engine registers any contact between the robot and a non-target object as a collision event.\n\nWe evaluate two Vision-Language-Action (VLA) models from the Pi0 family~\\cite{black2024pi0}. \\textbf{Pi0} (${\\sim}$2.5B parameters) pairs a PaliGemma vision-language encoder with a dedicated action expert that generates continuous actions via flow matching~\\cite{lipman2023flow}. \\textbf{Pi0.5} (from Physical Intelligence) extends this architecture with broader pre-training data and serves as a stronger baseline with substantially higher task capability and less susceptibility to action collapse.\n\nTable~\\ref{tab:configurations} summarizes the six training configurations. Each model is trained for 30K steps. Evaluation uses 50 episodes per task across 4 tasks (200 episodes per configuration). For multi-seed experiments on Pi0.5, we run 3 seeds (600 episodes per configuration). Initial object placements are fixed across methods to ensure fair comparison.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training configurations. Trainable parameter counts exclude the frozen backbone. The SDF auxiliary heads add $<$660K parameters to the ${\\sim}$33.5M LoRA budget.}\n\\label{tab:configurations}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nConfiguration & Description & Trainable Params \\\\\n\\midrule\nPi0 Full-FT & Full fine-tune, flow-matching loss & ${\\sim}$2.5B \\\\\nPi0 LoRA & LoRA adapters only & ${\\sim}$33.5M \\\\\nPi0+A1 (SDF aux)\\textsuperscript{$\\dagger$} & LoRA + SDF decoder + EE extractor & ${\\sim}$658K \\\\\nPi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\\sim}$34.2M \\\\\nPi0.5 (pre-trained) & No fine-tuning & 0 \\\\\nPi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\\sim}$33.5M \\\\\nPi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ & ${\\sim}$34.2M \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n\\raggedright\\footnotesize\\textsuperscript{$\\dagger$}LoRA adapter weights were not loaded due to a parameter-name mismatch; only the auxiliary SDF and EE heads were trained.\n\\end{table}\n\n\\subsection{Standard Metrics}\\label{sec:standard_metrics}\n\nWe report two conventional metrics. The \\emph{Collision Avoidance Rate} (CAR) is the fraction of episodes in which no collision occurs between the robot and any non-target object:\n\\begin{equation}\\label{eq:car}\n\\text{CAR} = \\frac{|\\{e : \\text{safe}(e)\\}|}{|E|}\n\\end{equation}\nwhere $E$ is the set of all evaluation episodes and $\\text{safe}(e)$ indicates that episode $e$ contains zero collision events. The \\emph{Task Success Rate} (TSR) is the fraction of episodes where the manipulation task reaches completion:\n\\begin{equation}\\label{eq:tsr}\n\\text{TSR} = \\frac{|\\{e : \\text{success}(e)\\}|}{|E|}\n\\end{equation}\nThese two metrics are standard in the SafeLIBERO evaluation protocol and in the broader VLA safety literature~\\cite{hu2025vlsa,zhang2025safevla}.\n\n\\subsection{Displacement-Filtered CAR}\\label{sec:dfcar}\n\nStandard CAR conflates two qualitatively distinct behaviors: a robot that plans a trajectory around obstacles, and a robot that has collapsed into inaction. Both register as ``safe,'' yet only the former reflects collision avoidance capability. We introduce CAR$_\\text{f}$, which excludes action-collapsed episodes from both numerator and denominator.\n\n\\paragraph{Action collapse.} We define an episode $e$ as \\emph{action-collapsed} when its maximum end-effector (EE) displacement satisfies\n\\begin{equation}\nd_{\\max}(e) < \\tau_d\n\\end{equation}\nwhere $d_{\\max}(e) = \\max_{t} \\| \\mathbf{p}_t - \\mathbf{p}_0 \\|_2$ is the maximum Euclidean displacement of the EE from its initial position across all timesteps, and $\\tau_d$ is a displacement threshold. We set $\\tau_d = 0.1$\\,mm, corresponding to sub-actuator-resolution motion.\n\n\\paragraph{Definition.} The displacement-filtered CAR is:\n\\begin{equation}\\label{eq:car_f}\n\\text{CAR}_\\text{f} = \\frac{|\\{e : \\text{safe}(e) \\;\\land\\; d_{\\max}(e) \\geq \\tau_d\\}|}{|\\{e : d_{\\max}(e) \\geq \\tau_d\\}|}\n\\end{equation}\nCAR$_\\text{f}$ retains only episodes with sufficient EE motion and measures the collision avoidance rate exclusively among them.\n\n\\paragraph{Threshold robustness.} The specific choice of $\\tau_d$ is not critical. The displacement distribution across all evaluated models is sharply bimodal: collapsed episodes cluster below 1\\,$\\mu$m, while active episodes exceed 200\\,mm. No episodes fall in the intermediate range. This five-order-of-magnitude gap means that any $\\tau_d \\in [2, 200]$\\,mm produces identical filtering results. We verify this empirically in Appendix~\\ref{sec:appendix_threshold}.\n\n\\paragraph{Diagnostic capability.} CAR$_\\text{f}$ serves two functions. First, it detects fake safety: Pi0+A1 reports CAR\\,=\\,91.5\\% under the standard metric, but CAR$_\\text{f} \\approx 0$\\% because 99.6\\% of its safe episodes are action-collapsed.\\footnote{For Pi0{+}A1, displacement is measured at the obstacle rather than the end-effector, as the original evaluation infrastructure recorded obstacle displacement only. The conclusion is independently corroborated by TSR{=}0\\%, confirming complete action collapse.} Second, it validates genuine safety: the pre-trained Pi0.5 (without fine-tuning) achieves CAR$_\\text{f}$ equal to its raw CAR (28.5\\%), with 0\\% of episodes filtered, because all safe episodes involve EE displacement above 288\\,mm.\n\n\\subsection{SDF Auxiliary Training}\\label{sec:sdf_aux}\n\nWe augment the LoRA-adapted VLA with two lightweight auxiliary heads that provide geometric supervision during training.\n\n\\paragraph{SDF Decoder ($f_\\text{SDF}$).} A 4-layer MLP (hidden dimension 256, Softplus activation with $\\beta = 5$, ${\\sim}$395K parameters) predicts the signed distance $\\Phi(\\mathbf{x})$ from the current EE position $\\mathbf{x}$ to the nearest obstacle surface. The decoder reads from intermediate features of the VLA action expert. The ground-truth signed distance field is precomputed from obstacle meshes using trimesh/pysdf, with values clamped at $\\delta = 0.05$\\,m and a safety margin $m = 0.01$\\,m applied to shift the zero-crossing outward from the obstacle surface.\n\n\\paragraph{EE Extractor ($f_\\text{EE}$).} A 2-layer MLP ($1024 \\to 256 \\to 3$, ${\\sim}$263K parameters) predicts the 3D EE position from the same action expert features. This auxiliary head provides the query point for the SDF decoder and serves as an implicit regularizer on the learned feature representation.\n\n\\paragraph{Training objective.} The total loss combines the standard flow-matching action loss with the two auxiliary losses:\n\\begin{equation}\\label{eq:total_loss}\n\\mathcal{L}_\\text{total} = \\mathcal{L}_\\text{action} + \\lambda \\left( \\mathcal{L}_\\text{SDF} + \\mathcal{L}_\\text{EE} \\right)\n\\end{equation}\nwhere $\\mathcal{L}_\\text{SDF}$ is a clamped $L_1$ loss on predicted SDF values with an Eikonal regularizer, $\\mathcal{L}_\\text{EE}$ is MSE on predicted EE position, and $\\lambda$ controls the auxiliary loss weight. We evaluate $\\lambda \\in \\{0.005, 0.01, 0.1\\}$. The total auxiliary overhead is $<$660K parameters, less than 2\\% of the ${\\sim}$33.5M LoRA parameter budget.\n\n\\paragraph{Optimization.} All models are trained with AdamW, a cosine learning rate schedule decaying from $2.5 \\times 10^{-5}$ to $2.5 \\times 10^{-6}$, for 30K steps with batch size 32. For Pi0.5+A1, training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization.\n\n\\paragraph{Pi0+A1 configuration note.} In the Pi0+A1 configuration, a parameter-name mismatch prevented the LoRA adapter weights from being loaded, so only the auxiliary SDF decoder and EE extractor heads were trained (${\\sim}$658K parameters), while the backbone remained entirely frozen. This caused complete action collapse (TSR\\,=\\,0\\%), as the frozen backbone could not adapt to the downstream tasks. The resulting failure mode reinforces the diagnostic value of CAR$_\\text{f}$: standard CAR reports 91.5\\% for Pi0+A1, but CAR$_\\text{f} \\approx 0$\\% correctly identifies these episodes as fake safety from a frozen robot rather than genuine collision avoidance.\n\n\\subsection{Oracle SDF Refinement}\\label{sec:oracle_setup}\n\nTo test the theoretical upper bound of EE-only SDF refinement (Section~\\ref{sec:ee_only}), we replace the learned SDF network with the ground-truth signed distance field computed from the simulation geometry. This eliminates prediction error and isolates the structural limitation of the refinement paradigm.\n\nWe evaluate three oracle variants:\n\\begin{itemize}\n\\item \\textit{Oracle-adaptive}: runtime gradient refinement with a dynamic step size $\\alpha$ that scales inversely with gradient magnitude, applied in Cartesian action space.\n\\item \\textit{Oracle-fixed}: a constant step size $\\alpha = 0.005$, also in Cartesian action space.\n\\item \\textit{Oracle-feature}: gradient applied in the VLA's latent feature space rather than directly to Cartesian actions. This variant averages 241.7 refinement steps per episode (vs.\\ ${\\sim}$14 for the Cartesian variants), as the feature-space gradient must propagate through the action decoder.\n\\end{itemize}\nEach variant is evaluated for 160 episodes (4 tasks $\\times$ 40 episodes) with a single seed. The oracle experiments are designed to test Claim~2 (Section~\\ref{sec:ee_only}): if EE-only SDF refinement is structurally sound, oracle performance should exceed unrefined baselines by a wide margin.",
      "numLines": 96,
      "startLine": 1,
      "totalLines": 96
    }
  }
}
```

</details>

---

### Assistant

_source line 22_

Now let me also update line 11 — the table summary says "six training configurations" but now there are seven rows (added Pi0.5 pre-trained).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "94069c66-4f49-402b-af0b-ba454acde723",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018V63XfgtBhyAf7JuPXo9Dp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3522,
      "cache_read_input_tokens": 29990,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3522
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

_source line 23_

<details open><summary>🔧 Tool call — Edit · `toolu_01JuB3ACrz6Kt9MyEyFG7S59`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex",
  "old_string": "Table~\\ref{tab:configurations} summarizes the six training configurations.",
  "new_string": "Table~\\ref{tab:configurations} summarizes the seven evaluated configurations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "bbf25718-e441-4ada-9159-98345562c691",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018V63XfgtBhyAf7JuPXo9Dp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3522,
      "cache_read_input_tokens": 29990,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3522
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

_source line 24 · 2026-05-26T16:09:26.204Z_

<details><summary>↩ Tool result · `toolu_01JuB3ACrz6Kt9MyEyFG7S59`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "88a85faf-1db2-4db6-840b-23a5699a97c7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/method.tex",
    "oldString": "Table~\\ref{tab:configurations} summarizes the six training configurations.",
    "newString": "Table~\\ref{tab:configurations} summarizes the seven evaluated configurations.",
    "originalFile": "\\section{Experimental Setup and Metrics}\\label{sec:method}\n\nThis section defines the benchmark, models, training procedures, and evaluation metrics that underpin the analyses in Sections~\\ref{sec:fake_safety}--\\ref{sec:avoidance_source}. The central methodological contribution is the displacement-filtered Collision Avoidance Rate (CAR$_\\text{f}$), a corrective metric that separates genuine obstacle avoidance from action collapse (\\S\\ref{sec:dfcar}).\n\n\\subsection{Benchmark and Models}\\label{sec:benchmark}\n\nWe conduct all experiments on SafeLIBERO~\\cite{hu2025vlsa}, a collision-aware evaluation extension of the LIBERO simulation platform~\\cite{liu2023libero}. SafeLIBERO augments standard manipulation tasks with per-timestep collision detection and non-target obstacle annotations, enabling systematic measurement of both task completion and safety. We select the \\textit{object\\_pudding} suite (Level~I), which comprises four tabletop manipulation tasks: pick \\texttt{orange\\_juice}, \\texttt{chocolate\\_pudding}, \\texttt{milk}, or \\texttt{bbq\\_sauce} and place into a basket. In each task, non-target objects surround the manipulation target, and the MuJoCo physics engine registers any contact between the robot and a non-target object as a collision event.\n\nWe evaluate two Vision-Language-Action (VLA) models from the Pi0 family~\\cite{black2024pi0}. \\textbf{Pi0} (${\\sim}$2.5B parameters) pairs a PaliGemma vision-language encoder with a dedicated action expert that generates continuous actions via flow matching~\\cite{lipman2023flow}. \\textbf{Pi0.5} (from Physical Intelligence) extends this architecture with broader pre-training data and serves as a stronger baseline with substantially higher task capability and less susceptibility to action collapse.\n\nTable~\\ref{tab:configurations} summarizes the six training configurations. Each model is trained for 30K steps. Evaluation uses 50 episodes per task across 4 tasks (200 episodes per configuration). For multi-seed experiments on Pi0.5, we run 3 seeds (600 episodes per configuration). Initial object placements are fixed across methods to ensure fair comparison.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training configurations. Trainable parameter counts exclude the frozen backbone. The SDF auxiliary heads add $<$660K parameters to the ${\\sim}$33.5M LoRA budget.}\n\\label{tab:configurations}\n\\vspace{2pt}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nConfiguration & Description & Trainable Params \\\\\n\\midrule\nPi0 Full-FT & Full fine-tune, flow-matching loss & ${\\sim}$2.5B \\\\\nPi0 LoRA & LoRA adapters only & ${\\sim}$33.5M \\\\\nPi0+A1 (SDF aux)\\textsuperscript{$\\dagger$} & LoRA + SDF decoder + EE extractor & ${\\sim}$658K \\\\\nPi0+A3 (learned SDF) & LoRA + SDF decoder w/ gradient refinement & ${\\sim}$34.2M \\\\\nPi0.5 (pre-trained) & No fine-tuning & 0 \\\\\nPi0.5 LoRA & LoRA fine-tune on Pi0.5 & ${\\sim}$33.5M \\\\\nPi0.5+A1 (SDF aux) & LoRA + SDF aux on Pi0.5, $\\lambda \\in \\{0.005, 0.01, 0.1\\}$ & ${\\sim}$34.2M \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{2pt}\n\\raggedright\\footnotesize\\textsuperscript{$\\dagger$}LoRA adapter weights were not loaded due to a parameter-name mismatch; only the auxiliary SDF and EE heads were trained.\n\\end{table}\n\n\\subsection{Standard Metrics}\\label{sec:standard_metrics}\n\nWe report two conventional metrics. The \\emph{Collision Avoidance Rate} (CAR) is the fraction of episodes in which no collision occurs between the robot and any non-target object:\n\\begin{equation}\\label{eq:car}\n\\text{CAR} = \\frac{|\\{e : \\text{safe}(e)\\}|}{|E|}\n\\end{equation}\nwhere $E$ is the set of all evaluation episodes and $\\text{safe}(e)$ indicates that episode $e$ contains zero collision events. The \\emph{Task Success Rate} (TSR) is the fraction of episodes where the manipulation task reaches completion:\n\\begin{equation}\\label{eq:tsr}\n\\text{TSR} = \\frac{|\\{e : \\text{success}(e)\\}|}{|E|}\n\\end{equation}\nThese two metrics are standard in the SafeLIBERO evaluation protocol and in the broader VLA safety literature~\\cite{hu2025vlsa,zhang2025safevla}.\n\n\\subsection{Displacement-Filtered CAR}\\label{sec:dfcar}\n\nStandard CAR conflates two qualitatively distinct behaviors: a robot that plans a trajectory around obstacles, and a robot that has collapsed into inaction. Both register as ``safe,'' yet only the former reflects collision avoidance capability. We introduce CAR$_\\text{f}$, which excludes action-collapsed episodes from both numerator and denominator.\n\n\\paragraph{Action collapse.} We define an episode $e$ as \\emph{action-collapsed} when its maximum end-effector (EE) displacement satisfies\n\\begin{equation}\nd_{\\max}(e) < \\tau_d\n\\end{equation}\nwhere $d_{\\max}(e) = \\max_{t} \\| \\mathbf{p}_t - \\mathbf{p}_0 \\|_2$ is the maximum Euclidean displacement of the EE from its initial position across all timesteps, and $\\tau_d$ is a displacement threshold. We set $\\tau_d = 0.1$\\,mm, corresponding to sub-actuator-resolution motion.\n\n\\paragraph{Definition.} The displacement-filtered CAR is:\n\\begin{equation}\\label{eq:car_f}\n\\text{CAR}_\\text{f} = \\frac{|\\{e : \\text{safe}(e) \\;\\land\\; d_{\\max}(e) \\geq \\tau_d\\}|}{|\\{e : d_{\\max}(e) \\geq \\tau_d\\}|}\n\\end{equation}\nCAR$_\\text{f}$ retains only episodes with sufficient EE motion and measures the collision avoidance rate exclusively among them.\n\n\\paragraph{Threshold robustness.} The specific choice of $\\tau_d$ is not critical. The displacement distribution across all evaluated models is sharply bimodal: collapsed episodes cluster below 1\\,$\\mu$m, while active episodes exceed 200\\,mm. No episodes fall in the intermediate range. This five-order-of-magnitude gap means that any $\\tau_d \\in [2, 200]$\\,mm produces identical filtering results. We verify this empirically in Appendix~\\ref{sec:appendix_threshold}.\n\n\\paragraph{Diagnostic capability.} CAR$_\\text{f}$ serves two functions. First, it detects fake safety: Pi0+A1 reports CAR\\,=\\,91.5\\% under the standard metric, but CAR$_\\text{f} \\approx 0$\\% because 99.6\\% of its safe episodes are action-collapsed.\\footnote{For Pi0{+}A1, displacement is measured at the obstacle rather than the end-effector, as the original evaluation infrastructure recorded obstacle displacement only. The conclusion is independently corroborated by TSR{=}0\\%, confirming complete action collapse.} Second, it validates genuine safety: the pre-trained Pi0.5 (without fine-tuning) achieves CAR$_\\text{f}$ equal to its raw CAR (28.5\\%), with 0\\% of episodes filtered, because all safe episodes involve EE displacement above 288\\,mm.\n\n\\subsection{SDF Auxiliary Training}\\label{sec:sdf_aux}\n\nWe augment the LoRA-adapted VLA with two lightweight auxiliary heads that provide geometric supervision during training.\n\n\\paragraph{SDF Decoder ($f_\\text{SDF}$).} A 4-layer MLP (hidden dimension 256, Softplus activation with $\\beta = 5$, ${\\sim}$395K parameters) predicts the signed distance $\\Phi(\\mathbf{x})$ from the current EE position $\\mathbf{x}$ to the nearest obstacle surface. The decoder reads from intermediate features of the VLA action expert. The ground-truth signed distance field is precomputed from obstacle meshes using trimesh/pysdf, with values clamped at $\\delta = 0.05$\\,m and a safety margin $m = 0.01$\\,m applied to shift the zero-crossing outward from the obstacle surface.\n\n\\paragraph{EE Extractor ($f_\\text{EE}$).} A 2-layer MLP ($1024 \\to 256 \\to 3$, ${\\sim}$263K parameters) predicts the 3D EE position from the same action expert features. This auxiliary head provides the query point for the SDF decoder and serves as an implicit regularizer on the learned feature representation.\n\n\\paragraph{Training objective.} The total loss combines the standard flow-matching action loss with the two auxiliary losses:\n\\begin{equation}\\label{eq:total_loss}\n\\mathcal{L}_\\text{total} = \\mathcal{L}_\\text{action} + \\lambda \\left( \\mathcal{L}_\\text{SDF} + \\mathcal{L}_\\text{EE} \\right)\n\\end{equation}\nwhere $\\mathcal{L}_\\text{SDF}$ is a clamped $L_1$ loss on predicted SDF values with an Eikonal regularizer, $\\mathcal{L}_\\text{EE}$ is MSE on predicted EE position, and $\\lambda$ controls the auxiliary loss weight. We evaluate $\\lambda \\in \\{0.005, 0.01, 0.1\\}$. The total auxiliary overhead is $<$660K parameters, less than 2\\% of the ${\\sim}$33.5M LoRA parameter budget.\n\n\\paragraph{Optimization.} All models are trained with AdamW, a cosine learning rate schedule decaying from $2.5 \\times 10^{-5}$ to $2.5 \\times 10^{-6}$, for 30K steps with batch size 32. For Pi0.5+A1, training proceeds in two phases: Phase~1 (steps 0--5K) trains only the auxiliary heads on detached features with the backbone frozen; Phase~2 (steps 5K--30K) unfreezes LoRA parameters for joint optimization.\n\n\\paragraph{Pi0+A1 configuration note.} In the Pi0+A1 configuration, a parameter-name mismatch prevented the LoRA adapter weights from being loaded, so only the auxiliary SDF decoder and EE extractor heads were trained (${\\sim}$658K parameters), while the backbone remained entirely frozen. This caused complete action collapse (TSR\\,=\\,0\\%), as the frozen backbone could not adapt to the downstream tasks. The resulting failure mode reinforces the diagnostic value of CAR$_\\text{f}$: standard CAR reports 91.5\\% for Pi0+A1, but CAR$_\\text{f} \\approx 0$\\% correctly identifies these episodes as fake safety from a frozen robot rather than genuine collision avoidance.\n\n\\subsection{Oracle SDF Refinement}\\label{sec:oracle_setup}\n\nTo test the theoretical upper bound of EE-only SDF refinement (Section~\\ref{sec:ee_only}), we replace the learned SDF network with the ground-truth signed distance field computed from the simulation geometry. This eliminates prediction error and isolates the structural limitation of the refinement paradigm.\n\nWe evaluate three oracle variants:\n\\begin{itemize}\n\\item \\textit{Oracle-adaptive}: runtime gradient refinement with a dynamic step size $\\alpha$ that scales inversely with gradient magnitude, applied in Cartesian action space.\n\\item \\textit{Oracle-fixed}: a constant step size $\\alpha = 0.005$, also in Cartesian action space.\n\\item \\textit{Oracle-feature}: gradient applied in the VLA's latent feature space rather than directly to Cartesian actions. This variant averages 241.7 refinement steps per episode (vs.\\ ${\\sim}$14 for the Cartesian variants), as the feature-space gradient must propagate through the action decoder.\n\\end{itemize}\nEach variant is evaluated for 160 episodes (4 tasks $\\times$ 40 episodes) with a single seed. The oracle experiments are designed to test Claim~2 (Section~\\ref{sec:ee_only}): if EE-only SDF refinement is structurally sound, oracle performance should exceed unrefined baselines by a wide margin.",
    "structuredPatch": [
      {
        "oldStart": 8,
        "oldLines": 7,
        "newStart": 8,
        "newLines": 7,
        "lines": [
          " ",
          " We evaluate two Vision-Language-Action (VLA) models from the Pi0 family~\\cite{black2024pi0}. \\textbf{Pi0} (${\\sim}$2.5B parameters) pairs a PaliGemma vision-language encoder with a dedicated action expert that generates continuous actions via flow matching~\\cite{lipman2023flow}. \\textbf{Pi0.5} (from Physical Intelligence) extends this architecture with broader pre-training data and serves as a stronger baseline with substantially higher task capability and less susceptibility to action collapse.",
          " ",
          "-Table~\\ref{tab:configurations} summarizes the six training configurations. Each model is trained for 30K steps. Evaluation uses 50 episodes per task across 4 tasks (200 episodes per configuration). For multi-seed experiments on Pi0.5, we run 3 seeds (600 episodes per configuration). Initial object placements are fixed across methods to ensure fair comparison.",
          "+Table~\\ref{tab:configurations} summarizes the seven evaluated configurations. Each model is trained for 30K steps. Evaluation uses 50 episodes per task across 4 tasks (200 episodes per configuration). For multi-seed experiments on Pi0.5, we run 3 seeds (600 episodes per configuration). Initial object placements are fixed across methods to ensure fair comparison.",
          " ",
          " \\begin{table}[t]",
          " \\centering"
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

_source line 25_

All four warnings fixed. Verification summary:

1. **Table 1 — Pi0 Full-FT**: `~3.5B` → `~2.5B` (line 23) ✓
2. **Table 1 — Pi0+A1**: `~34.2M` → `~658K` with `\textsuperscript{$\dagger$}` marker and table footnote explaining parameter-name mismatch (lines 25, 33) ✓
3. **Table 1 — Pi0.5 (pre-trained)**: New row added with 0 trainable params (line 27) ✓
4. **§3.3 Pi0.5 mention**: Changed to "the pre-trained Pi0.5 (without fine-tuning)" (line 66) ✓
5. **§3.3 obstacle displacement footnote**: Added to the 99.6% sentence, noting obstacle-based displacement measurement and TSR=0% corroboration (line 66) ✓
6. **§3.4 LoRA mismatch disclosure**: New paragraph "Pi0+A1 configuration note" explaining the mismatch, action collapse consequence, and dfCAR diagnostic value (line 84) ✓
7. **"six" → "seven"** configurations count updated (line 11) ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "uuid": "8ec7b560-4ffc-40b3-886e-e363c6e46a07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NZc8mKPmoHbY1WjxjNeZ6n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 264,
      "cache_read_input_tokens": 33512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 264
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

_source line 26_

All four warnings fixed. Verification summary:

1. **Table 1 — Pi0 Full-FT**: `~3.5B` → `~2.5B` (line 23) ✓
2. **Table 1 — Pi0+A1**: `~34.2M` → `~658K` with `\textsuperscript{$\dagger$}` marker and table footnote explaining parameter-name mismatch (lines 25, 33) ✓
3. **Table 1 — Pi0.5 (pre-trained)**: New row added with 0 trainable params (line 27) ✓
4. **§3.3 Pi0.5 mention**: Changed to "the pre-trained Pi0.5 (without fine-tuning)" (line 66) ✓
5. **§3.3 obstacle displacement footnote**: Added to the 99.6% sentence, noting obstacle-based displacement measurement and TSR=0% corroboration (line 66) ✓
6. **§3.4 LoRA mismatch disclosure**: New paragraph "Pi0+A1 configuration note" explaining the mismatch, action collapse consequence, and dfCAR diagnostic value (line 84) ✓
7. **"six" → "seven"** configurations count updated (line 11) ✓

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 66263,
  "duration_api_ms": 67335,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "2440eb8a-660d-4292-8281-de7d836504fc",
  "total_cost_usd": 0.32454225,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 21935,
    "cache_read_input_tokens": 211523,
    "output_tokens": 3189,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 21935,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 323,
        "cache_read_input_tokens": 33512,
        "cache_creation_input_tokens": 264,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 264
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1847,
      "outputTokens": 14,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0019169999999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 3189,
      "cacheReadInputTokens": 211523,
      "cacheCreationInputTokens": 21935,
      "webSearchRequests": 0,
      "costUSD": 0.32262525,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3d601499-8e40-49e4-8679-71afc11d2215"
}
```

</details>

---
